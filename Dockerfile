#Deriving the latest base image
FROM python:latest


#Labels as key value pair
LABEL Maintainer="Priya Pathak"


WORKDIR /usr/app/src

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python","-u","./main.py"]