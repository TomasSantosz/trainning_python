import os ##impota biblioteca que permite utilizar recursos do SO

print("=" * 60)
ip_host = input("Digite o ip ou host a ser verificado: ")

## os -> comandos do sistema
os.system('ping -n 6 {}'.format(ip_host))
print("-" * 60)

with open('host.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        os.system('ping ' + ip)