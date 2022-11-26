# File Storage Server
This is a simple file upload/download service. Users will get a link if they upload files to service. Users can download files from given link.




## Tech Stack

**Client&Server:** Python Flask

**DB:** SQLITE3


## Installation with Docker

1. Use the following docker image to make fileStorage container.
```
FROM python:3.9.15

RUN apt update -y 

RUN apt install --upgrade -y pip 

RUN pip install Flask 

WORKDIR /home/

EXPOSE 9000

CMD ["tail", "-f", "/dev/null"]
```
2. In the container, git clone file-storage-server repo(fork https://gitlab.com/jinho-choi123/file-storage-server.git).
3. Run the following command to install packages.
```
$ pip install -r requirements.txt
```
4. Run the following command to start dev server.
```
$ python index.py
```
