import re

class ClientRequestParser:
	def __init__(self, data, db):
		"""
		The `data` is string from client side!
		"""
		try:
			pattern = re.compile(r'(?P<method>.*)/(?P<command>.*)/(?P<status>.*)')
			m = pattern.match(data)
			self.request_data=m.groupdict()
			self.request_method = self.request_data.get('method','No Key Found')
			self.db=db
		except :
			print 'client command error'
			self.request_method = 'no method'

		
	def get(self, db, task_id):
		response = db.get(task_id,'Key No Found')
		return response 

	def post(self,db, command):
		pattern = re.compile(r'(?P<key>.*)=(?P<value>.*)')
		m = pattern.match(command)
		post_data = m.groupdict()
		key=post_data.get('key','Key No Found')
		value=post_data.get('value','Key No Found')
		db[key]=value
		response='submit success'
		return response 
		

	def response(self):
		response=''
		if self.request_method  == 'GET':
			print 'Get method'
			task_id=self.request_data.get('command','No Key Found')
			response=self.get(self.db, task_id)
		elif self.request_method == 'POST':
			command=self.request_data.get('command','No Key Found')
			response=self.post(self.db, command)
		else:
			response = 'client request error'
	
		response=response+'\r\n'
		return response
