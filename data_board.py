#Author : Roche Christopher
#File created on 01 Aug 2019 7:24 PM

import cherrypy

class data_board:
    def __init__(self, port=20010, host="127.0.0.1"):
        self.port = port
        self.host = host
        self.data = ""
        self.server = self.server()


    class server(object):

        def __init__(self):
            self.data = ""

        @cherrypy.expose
        def index(self):
            return "The Eagle has landed!"

        @cherrypy.expose
        def get_data(self):
            return self.data

        def set_data(self, data):
            self.data = str(data)

    def start_server(self):

        cherrypy.config.update({'server.socket_port': self.port})
        cherrypy.config.update({'server.socket_host': self.host})
        cherrypy.tree.mount(self.server)
        cherrypy.engine.start()

    def stop_server(self):
        cherrypy.engine.stop()

    def set_data(self, data):
        self.data = data
        self.server.set_data(str(data))



if __name__ == "__main__":
    cherrypy.config.update({'server.socket_port':18002})
    cherrypy.tree.mount(data_board.server())
    cherrypy.engine.start()