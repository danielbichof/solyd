import paramiko

host = "127.0.0.1"
user = "kali"
passwd = "kali"


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user,  password=passwd)


stdin, stdout, stderr = client.exec_command("ls")

print(stdout.readlines())