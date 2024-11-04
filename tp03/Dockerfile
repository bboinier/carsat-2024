FROM golang:1.13
ENV CGO_ENABLED=0 

WORKDIR web
COPY index.html .
COPY main.go .

RUN go build -o /web/server
RUN chmod +x /web/server

CMD ["/web/server"]
ENV USER=saukratesk
EXPOSE 80
