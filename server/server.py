import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import platform
import socket
import re
import uuid
import json
import psutil
import logging
import datetime

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        self.write(get_self_info())


def get_self_info():
    try:
        info = {}
        info['platform'] = platform.system()
        info['platform_release'] = platform.release()
        info['platform_version'] = platform.version()
        info['architecture'] = platform.machine()
        info['hostname'] = socket.gethostname()
        info['ip_address'] = socket.gethostbyname(socket.gethostname())
        info['processor'] = platform.processor()
        info['ram'] = str(
            round(psutil.virtual_memory().total / (1024.0 ** 3)))+" GB"
        info['time'] = str(datetime.datetime.now())
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([(r"/", MainHandler)])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    print("Server started at port: " + str(options.port))
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
