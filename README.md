This is part of the ping-pong example program, where the ponger is the echo server.
And pinger is the client.
To run this application, first create a docker image:
docker build -t ponger .
To run the ponger in docker:
docker run -d --net=host --name pong ponger

To see logs,
docker logs pong
