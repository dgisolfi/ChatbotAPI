FROM ubuntu:latest
MAINTAINER Daniel Gisolfi
EXPOSE 5525
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
WORKDIR /ChatBotApi
COPY ./src .
COPY README.md . 
COPY requirements.txt .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["__init__.py"]

