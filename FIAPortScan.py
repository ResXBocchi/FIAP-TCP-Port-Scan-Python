#!/usr/share/python3
import socket
import sys

#rm95147

def valida_ip(ip):

        if len(ip.split('.')) != 4: # valida se IPv4 foi passado 
                print("Certifique-se de passar um endereço IPv4\n")
                sys.exit(0)


if len(sys.argv) < 2 or len(sys.argv) >= 4:
        print("Modo de uso:\npython3 FIAPortScan.py <ip> [ports - default 1-1023]")
        print("python3 FIAPortScan.py 127.0.0.1 22,80")
        print("python3 FIAPortScan.py 127.0.0.1")
        print("python3 FIAPortScan.py -i - Modo interativo")
        sys.exit(0) # se os parametros estiverem fora do esperado orienta o usuario

elif len(sys.argv) == 2:    

        if sys.argv[1] == "-i": #verifica e implementa o modo interativo
                
                ip = input("Insira o IP a ser escaneado\n")
                valida_ip(ip)

                portas = input("Insira a porta, ou portas separadas por virgulas\n")

                if portas != "":
                        portas = [int(n) for n in portas.split(',')]
                else:
                        portas = range(1,1024)
        else:

                ip = sys.argv[1]
                valida_ip(ip)
                portas = range(1,1024) # range de portas a ser escaneado
                                       # caso nenhuma porta seja especificada

else:
        try:
                ip = sys.argv[1]
                valida_ip(ip)
                portas = [int(n) for n in sys.argv[2].split(',')]
                                # list comprehension para converter a string de
                                # portas separadas por virgulas em numeros inteiros
        except:
                pass

abertas = [] # lista de portas abertas

for porta in portas: # realiza as etapas abaixo nas portas do range

        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        response = sock.connect_ex((ip,porta)) # tenta estabelecer conexao

        if response == 0:
                print("Porta {} - Aberta".format(porta))
                abertas.append(porta) # se obtiver sucesso o informa e
                                      #adiciona a porta na lista de abertas

if len(abertas) != 0:
        print("Portas abertas: {}".format(abertas))

        print("As demais entre 1 e 1023 estão fechadas" if len(sys.argv) == 2 or sys.argv[1] != "-i" and portas != range(1,1024) else\
              "As demais dentre as portas especificadas estao fechadas")
                                        # se houver portas abertas as informa

else:
        print("Nenhuma porta entre 1 e 1023 aberta.")
                  # caso contrario informa que estao fechadas
#rm95147
