FROM golang:1.13 AS builder

ENV CGO_ENABLED=0
COPY main.go .
RUN go build -o /server

# app
FROM alpine:3.9
ENV IMAGE_API_URL="http://iotd/image" \
    ACCESS_API_URL="http://accesslog/access-log"

CMD ["/web/server"]

WORKDIR /web
COPY index.html .
COPY --from=builder /server .
RUN chmod +x server
