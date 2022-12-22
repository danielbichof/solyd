import socket, sys

def scan(host, port):
	try:
		for port in ports:
			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client.settimeout(0.05)
			code = client.connect_ex((host, int(port)))
			if code == 0:
				print(f"[+] {port} open")
	except Exception as error:
		print(error)
if __name__ == "__main__":
	if len(sys.argv) >=2:
		host = sys.argv[1]
		if len(sys.argv) >= 3:
			ports = sys.argv[2].split(",")
		else:
			ports = ['21', '22', '40', '80', '433', '8080', '5555', '4444']
		scan(host, ports)
	else:
		print("Usage: python3 port_scaning.py [host] [ports -> (22,422,80)]")
