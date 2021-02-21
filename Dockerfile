FROM python:3.6
#RUN apk add --update python py-pip
RUN pip install --upgrade pip
COPY requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt
COPY main.py /src
COPY .env /src
# COPY buzz /src/buzz
# CMD python /src/app.py
#COPY mainapp /src
COPY weblog.csv /src
CMD python /src/main.py