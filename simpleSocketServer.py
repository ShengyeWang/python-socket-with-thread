import socket
import threading

class ThreadSocket(object):
	"""
	
	"""
	todo_list = {
		'task_01':'see someone',
		'task_02':'read book',
		'task_03':'play basketball'

	}

	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sock.bind((self.host, self.port))

	def listen(self):
		self.sock.listen(5)
		while True:
			client, address = self.sock.accept()
			client.settimeout(60)
			threading.Thread(target=self.handleClientRequest, args=(client, address)).start()

	def handleClientRequest(self, client, address):
		while True:
			try:
				data = client.recv(1024)
				if data:
					#client.send(data)
					if 'GET' in data:
						method,task_id,status = data.split('/')
						result = self.todo_list.get(task_id,'no key match')
						print 'result',result
						response = str(result)
					else:
						response = 'data no found'

					response = response+'\r\n'
					client.send(response)
				else:
					raise error("Client has disconnected")
			except:
				client.close()
		
if __name__ == '__main__':
	server=ThreadSocket('',9000)
	server.listen()
