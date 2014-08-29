import SimpleHTTPServer, SocketServer , sys


port = sys.argv[1]

def RunServer():
    try:
      httphandler = SimpleHTTPServer.SimpleHTTPRequestHandler
      httpd = SocketServer.TCPServer(("",int(port)),httphandler)
      print "python webserver, serving at port "+ port
      httpd.serve_forever()

    except(KeyboardInterrupt, SystemExit):
        print " Exiting..."
        sys.exit
    except:
      print "There was a prblem starting the webserver at port "+ port

RunServer()
