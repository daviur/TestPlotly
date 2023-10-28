FROM python:3-alpine

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
ADD pages /app/
RUN pip install -r requirements.txt
ADD . /app/

ENTRYPOINT [ "python" ]
CMD ["main.py"]