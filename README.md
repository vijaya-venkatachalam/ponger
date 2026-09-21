This is part of the ping-pong example program, where the ponger is the echo server.
And pinger is the client.
To run this application, first create a docker image:
docker build -t ponger .
To run the ponger in docker:
docker network create mynet
docker run --net=mynet --name server --hostname ponger -d ponger

To see logs,
docker logs -f server
