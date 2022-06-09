FROM bsnacks000/python-poetry:latest

RUN mkdir app 
WORKDIR /app  
ADD . /app
COPY . /app 

RUN apt-get update \
    && apt-get install git -y -f \
    && poetry install 

ENTRYPOINT [ "/app/docker-entrypoint.sh" ]