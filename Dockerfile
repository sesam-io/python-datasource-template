FROM ubuntu:latest
MAINTAINER Graham Moore "graham.moore@sesam.io"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY ./service /service
WORKDIR /service
RUN pip install -r requirements.txt	
EXPOSE 5000/tcp
ENTRYPOINT ["python"]
CMD ["datasource-service.py"]