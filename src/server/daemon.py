from tornado.httpserver import HTTPServer
from tornado.web import Application

class ServerDaemon(object):

	def __init__(self) -> None:
		raise NotImplementedError

	def run(self) -> None:
		raise NotImplementedError