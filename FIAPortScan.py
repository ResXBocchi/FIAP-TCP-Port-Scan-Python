#!/usr/share/python3
import socket
import sys
#rm95147

def orientacao():    # orienta o usuario caso os argumentos estejam fora do esperado
        print("Modo de uso:\npython3 FIAPortScan.py <ip> [ports - default 1-1023]")
        print("python3 FIAPortScan.py 127.0.0.1 22,80")
        print("python3 FIAPortScan.py 127.0.0.1")
        print("python3 FIAPortScan.py -i - Modo interativo")
        sys.exit(0)
def valida_ip(ip):   # valida se o argumento passado se assemelha a um IPv4
        if len(ip.split('.')) != 4:
                print("Certifique-se de passar um endereço IPv4")
                sys.exit(0)
def scan(ip,portas):
	abertas = []  #inicia lista de portas abertas
	for porta in portas: #tenta conexao tcp nas portas definidas e as informa caso consiga
        	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        	response = sock.connect_ex((ip,porta))
        	if response == 0:
                	print("Porta {} - Aberta".format(porta))
                	abertas.append(porta)            # adiciona as portas abertas na lista
	if len(abertas) != 0:
        	print("Portas abertas: {}".format(abertas))
        	print("As demais entre 1 e 1023 estão fechadas" if portas == range(1,1024) else\
              	"As demais dentre as portas especificadas estao fechadas")
                	                                 # se houver portas abertas as informa
	else:
        	print("Nenhuma porta entre 1 e 1023 aberta.\n")
def interativo(): # inicia o modo interativo
	saida = ""
	while saida != "s":
		ip = input("Insira o IP a ser escaneado\n")
		valida_ip(ip)
		portas = input("Insira a porta, ou portas separadas por virgulas (padrao 1 a 1023)\n")
		if portas != "":
			portas = [int(n) for n in portas.split(',')]
		else:
			portas = range(1,1024)
		scan(ip,portas)
		saida = input("Digite 's' para sair\n")
	sys.exit(0)

#Condicional para verificar os argumentos e chamar a funcao apropriada

if len(sys.argv) < 2 or len(sys.argv) >= 4:
	orientacao()

elif sys.argv[1] == "-i":
        interativo()
else:
        ip = sys.argv[1]
        valida_ip(ip)
        portas = [int(n) for n in sys.argv[2].split(',')] if len(sys.argv) == 3 else range(1,1024)
        scan(ip,portas)
#rm95147
