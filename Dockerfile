FROM python:3-alpine
MAINTAINER Graham Moore "graham.moore@sesam.io"
COPY ./service /service
WORKDIR /service
RUN pip install -r requirements.txt
EXPOSE 5000/tcp
ENTRYPOINT ["python"]
CMD ["datasource-service.py"]
