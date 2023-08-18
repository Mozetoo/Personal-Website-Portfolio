FROM python:3.9-alpine
LABEL maintainer = 'Personal_website'

COPY ./requirement.txt /requirement.txt
COPY ./home /home

ENTRYPOINT ["top", "-b"]