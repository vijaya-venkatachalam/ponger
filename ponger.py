from responder.server import EchoServer

ser = EchoServer("0.0.0.0", 8001)
ser.echo_loop()

