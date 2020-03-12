# import functools
# import json
#
# from tornado import gen
# from tornado import httpclient
# from tornado import httputil
# from tornado import ioloop
# from tornado import websocket
#
# APPLICATION_JSON = 'application/json'
#
# DEFAULT_CONNECT_TIMEOUT = 30
# DEFAULT_REQUEST_TIMEOUT = 30
#
#
# class WebSocketClient(object):
# 	"""Base for web socket clients.
# 	"""
#
# 	DISCONNECTED = 0
# 	CONNECTING = 1
# 	CONNECTED = 2
#
# 	def __init__(self, url, io_loop=None,
# 				 connect_timeout=DEFAULT_CONNECT_TIMEOUT,
# 				 request_timeout=DEFAULT_REQUEST_TIMEOUT):
#
# 		self.connect_timeout = connect_timeout
# 		self.request_timeout = request_timeout
# 		self._io_loop = io_loop or ioloop.IOLoop.current()
# 		self._ws_connection = None
# 		self._connect_status = self.DISCONNECTED
# 		self.connect(url)
#
# 	def connect(self, url):
# 		"""Connect to the server.
# 		:param str url: server URL.
# 		"""
# 		self._connect_status = self.CONNECTING
# 		headers = httputil.HTTPHeaders({'Content-Type': APPLICATION_JSON})
# 		request = httpclient.HTTPRequest(url=url,
# 										 connect_timeout=self.connect_timeout,
# 										 request_timeout=self.request_timeout,
# 										 headers=headers)
# 		ws_conn = websocket.WebSocketClientConnection(request)
# 		ws_conn.connect_future.add_done_callback(self._connect_callback)
#
# 	def send(self, msg):
# 		"""Send message to the server
# 		:param str data: message.
# 		"""
#
# 		if self._ws_connection:
# 			self._ws_connection.write_message(msg)
#
# 	def close(self, reason=''):
# 		"""Close connection.
# 		"""
#
# 		if self._connect_status != self.DISCONNECTED:
# 			self._connect_status = self.DISCONNECTED
# 			self._ws_connection and self._ws_connection.close()
# 			self._ws_connection = None
# 			self.on_connection_close(reason)
#
# 	def _connect_callback(self, future):
# 		if future.exception() is None:
# 			self._connect_status = self.CONNECTED
# 			self._ws_connection = future.result()
# 			self.on_connection_success()
# 			self._read_messages()
# 		else:
# 			self.close(future.exception())
#
# 	def is_connected(self):
# 		return self._ws_connection is not None
#
# 	@gen.coroutine
# 	def _read_messages(self):
# 		while True:
# 			msg = yield self._ws_connection.read_message()
# 			if msg is None:
# 				self.close()
# 				break
#
# 			self.on_message(msg)
#
# 	def on_message(self, msg):
# 		"""This is called when new message is available from the server.
# 		:param str msg: server message.
# 		"""
#
# 		print(msg)
#
# 	def on_connection_success(self):
# 		"""This is called on successful connection ot the server.
# 		"""
#
# 		pass
# 		print('connected')
# 		self.send('apple')
#
# 	def on_connection_close(self, reason):
# 		"""This is called when server closed the connection.
# 		"""
# 		pass
#
# 		print('closed')
#
#
# def main():
# 	io_loop = ioloop.IOLoop.instance()
# 	ws_url = 'ws://echo.websocket.org'
# 	client = WebSocketClient(ws_url)
# 	# ws_url = 'ws://127.0.0.1:8090/ws'
#
# 	try:
# 		io_loop.start()
# 	except KeyboardInterrupt:
# 		client.close()


from tornado import gen
from tornado.ioloop import IOLoop, PeriodicCallback
from tornado.websocket import websocket_connect


class Client(object):
	def __init__(self, url, ioloop=None, timeout=5):
		self.url = url
		self.timeout = timeout
		self.ioloop = ioloop or IOLoop.instance()
		self.ws = None
		self.connect()
		self.ioloop.start()

	@gen.coroutine
	def stay_connected(self):
		if not self.ws:
			self.ws = yield websocket_connect(self.url)

	def send(self, msg):
		self.stay_connected()
		self.ws.write_message(msg)

	@gen.coroutine
	def connect(self):
		try:
			self.on_connecting()
			self.ws = yield websocket_connect(self.url)

			self.connected()
		except Exception as e:
			print("Connection error:", e)
		else:
			self.run()

	def connected(self):
		self.on_open()
		self.run()

	def on_open(self):
		pass

	@gen.coroutine
	def run(self):
		while True:
			msg = yield self.ws.read_message()
			if msg is None:
				self.on_close()
				self.ws = None
				break
			self.on_message(msg)

	def on_connecting(self):
		pass

	def on_close(self):
		pass

	def on_message(self, msg):
		pass


if __name__ == "__main__":
	class NewClient(Client):
		def on_connecting(self):
			print(f'Connecting to {self.url}')

		def on_open(self):
			print(f'Connected to {self.url}')
			self.send('Happy')

		def on_message(self, msg):
			print(f"On message: {msg}.")

		def on_close(self):
			print("Connection closed.")


	client = NewClient("ws://echo.websocket.org")

# if __name__ == '__main__':
# 	main()
