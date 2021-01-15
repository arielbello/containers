FROM python:3-alpine

#install server stuff
RUN pip3 install flask gunicorn

WORKDIR /app

COPY . .

EXPOSE 8000

CMD ["gunicorn", "-w 2", "-b", "0.0.0.0:8000", "flaskapp:app"]