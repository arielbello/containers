FROM debian:10-slim

#All de Apts
RUN apt update && apt install -y --no-install-recommends \
	python3 \
	python3-pip \
	firefox-esr 

#Python packages
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# ALL the files
COPY . app/

WORKDIR app/
# Add webdriver to system path
# RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-linux64.tar.gz
# RUN tar -xf 
RUN mv geckodriver /usr/local/bin/
RUN chmod 555 /usr/local/bin/geckodriver

EXPOSE 8080

CMD ["gunicorn", "-w 2", "-b", "0.0.0.0:8080", "app:app"]