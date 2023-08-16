FROM ubuntu:latest
LABEL authors="zetop"

ENTRYPOINT ["top", "-b"]