import sys
import socket

s = socket.socket()
host = '192.168.1.7'
port = 8888

print("Waiting for connection...\n")
try:
	s.connect((host, port))
except socket.error as e:
	print(str(e))

Response = s.recv(1024)
print(Response)

while True:
	Input = input('Choose mathematical function, [L]ogarithmic, [S]quare Root or [E]xponential. Enter the first capital letter only or [Q] to quit: ')

	if Input == 'L' or Input == 'S' or Input == 'E':
		value = input("Enter a value: ")
		Input = Input + ":" + value

		s.send(str.encode(Input))
	elif Input == 'Q':
		print("Quitting app")
		s.send(str.encode(Input))
		sys.exit()
	else:
		print("Invalid input! Enter only L, S, or E")
		sys.exit()

	Response = s.recv(1024)
	print(Response.decode("utf-8"))

s.close()
