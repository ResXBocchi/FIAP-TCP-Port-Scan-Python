#!/usr/share/python3
import socket
import sys

#rm95147

portas = range(1,1024) # range de portas a ser escaneado
abertas = [] # lista de portas abertas
ip = sys.argv[1] # ip passado por argumento do script

for porta in portas: # realiza as etapas abaixo nas portas do range

	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	response = sock.connect_ex((ip,porta)) # tenta estabelecer conexao

	if response == 0:
		print("Porta {} - Aberta".format(porta))
		abertas.append(porta) # se obtiver sucesso o informa e
				      #adiciona a porta na lista de abertas

if len(abertas) != 0:
	print("Portas abertas:\n{}\nAs demais entre 1 e 1023 estão fechadas"\
.format(abertas)) # se houver portas abertas as informa

else:
	print("Nenhuma porta entre 1 e 1023 aberta.")
		  # caso contrario informa que estao fechadas

#rm95147


