import concurrent.futures
import configparser
import pathlib
import random
import re
import socket
import subprocess
import urllib.error
import urllib.request

ip_test_api = "https://checkip.amazonaws.com"
tcp_port_test_api = "https://check-host.net/check-tcp?host={address}&max_nodes=3"

def print_info(msg):
    print(f"\\033[34m{msg}\\033[0m")

def print_warn(msg):
    print(f"\\033[33m{msg}\\033[0m")

def print_error(msg):
    print(f"\\033[31m{msg}\\033[0m")

def test_tcp_port(ip, port):
    def sock_accept(sock):
        con, addr = sock.accept()
        con.close()
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('0.0.0.0', int(port)))
        sock.listen()
        
        future = executor.submit(sock_accept, sock)

        req = urllib.request.Request(tcp_port_test_api.format(address=f"{ip}:{port}"))
        req.add_header('Accept', 'application/json')
        req.add_header('User-Agent', 'curl/7.81.0')

        try:
            response = urllib.request.urlopen(req, timeout=10)
            response.close()
        except (urllib.error.URLError, urllib.error.HTTPError):
            print_error("API used in tcp port test appears to be unavailable.")
            sock.close()
            return False

        try:
            future.result(timeout=15)
            return True
        except concurrent.futures.TimeoutError:
            return False
        finally:
            sock.close()

try:
    with urllib.request.urlopen(ip_test_api, timeout=10) as response:
        external_ip = response.read().decode(response.headers.get_content_charset())
except (urllib.error.URLError, urllib.error.HTTPError, TypeError):
        print_error("API used in IP test appears to be unavailable.")
        exit(1)

print(external_ip)

if test_tcp_port(external_ip.strip(), "42000"):
    print(f"Test passed. 42000")
else:
    print(f"Test failed. 42000")

if test_tcp_port(external_ip.strip(), "42001"):
    print(f"Test passed. 42001")
else:
    print(f"Test failed. 42001")