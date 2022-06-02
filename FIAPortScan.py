#!/usr/share/python3
import socket
import sys
#rm95147

def valida_ip(ip):
        if len(ip.split('.')) != 4:
                print("Certifique-se de passar um endereço IPv4\n")
                sys.exit(0)

if len(sys.argv) < 2 or len(sys.argv) >= 4:
        print("Modo de uso:\npython3 FIAPortScan.py <ip> [ports - default 1-1023]")
        print("python3 FIAPortScan.py 127.0.0.1 22,80")
        print("python3 FIAPortScan.py 127.0.0.1")
        print("python3 FIAPortScan.py -i - Modo interativo")
        sys.exit(0)     #orienta o usuario caso os argumentos estejam fora do esperado
elif len(sys.argv) == 2:      #caso receba um unico argumento, verifica se eh ip ou -i
        if sys.argv[1] == "-i":                   #verifica e inicia o modo interativo
                ip = input("Insira o IP a ser escaneado\n")
                valida_ip(ip)
                portas = input("Insira a porta, ou portas separadas por virgulas\n")
                if portas != "":
                        portas = [int(n) for n in portas.split(',')]
                else:
                        portas = range(1,1024)
        else:               # caso receba o ip o valida e define as portas como 1-1023
                ip = sys.argv[1]
                valida_ip(ip)
                portas = range(1,1024) 
else:            # caso receba ips e portas verifica o ip e trata a entrada das portas
        try:
                ip = sys.argv[1]
                valida_ip(ip)
                portas = [int(n) for n in sys.argv[2].split(',')] # list comprehension
        # para converter a string de portas separadas por virgulas em numeros inteiros
        except:
                pass

abertas = []                                           #inicia lista de portas abertas

for porta in portas: #tenta conexao tcp nas portas definidas e as informa caso consiga
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        response = sock.connect_ex((ip,porta))
        if response == 0:
                print("Porta {} - Aberta".format(porta))
                abertas.append(porta)            # adiciona as portas abertas na lista

if len(abertas) != 0:
        print("Portas abertas: {}".format(abertas))
        print("As demais entre 1 e 1023 estão fechadas" if len(sys.argv) == 2 or\
			   	 sys.argv[1] != "-i" and portas != range(1,1024) else\
              "As demais dentre as portas especificadas estao fechadas")
                                                 # se houver portas abertas as informa
else:
        print("Nenhuma porta entre 1 e 1023 aberta.")
#rm95147
