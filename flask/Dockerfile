FROM python:3-alpine

#install server stuff
RUN pip3 install flask

WORKDIR /app

COPY . .

#EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]