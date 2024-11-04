## Before
docker image build -t go-server .

docker container run -d -p 804:80 go-server

image is 800MB on Linux; 5.2GB on Windows

## After
docker image build -t go-server -f Dockerfile.optimized .

docker container run -d -p 805:80 go-server

image is 15MB on Linux; 230MB on Windows

## Linux

```
>docker image ls go-ser*
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE 
go-server            optimized           acd8afedcb0d        16 minutes ago      15.3MB
go-server            latest              87d6bce2a950        19 minutes ago      802MB
```

## Windows

```
>docker image ls go-ser*
REPOSITORY          TAG                 IMAGE ID            CREATED              SIZE
go-server           optimized           2f017c0f1524        About a minute ago   260MB
go-server           latest              42013cf1495c        2 minutes ago        5.14GB
```
