import dns.resolver, sys

resolver = dns.resolver.Resolver()

try:
	alvo = sys.argv[1]
	wdlist = sys.argv[2]
except:
	print("Usage: python3 dnsbrute.py [target] [wordlist]")
try:
	with open(wdlist, "r" ) as arq:
		subdominios = arq.read().splitlines()
except:
	print("erros ao abrir arquivo")
	sys.exit()

for subdominio in subdominios:
	try:
		sub_alvo = f"{subdominio}.{alvo}"
		results = resolver.resolve(sub_alvo, "A")
		for  r in results:
			print(f"{sub_alvo} -> {r}")
	except:
		pass
