FROM python:3-alpine

#install server stuff
RUN pip3 install flask

WORKDIR /app

COPY . .

EXPOSE 8080

CMD flask run --host="0.0.0.0" --port=8080	