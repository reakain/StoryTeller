FROM python:3.8-alpine

COPY bots/config.py /bots/
COPY bots/autoreply.py /bots/
COPY bots/questmaker.py /bots/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "autoreply.py"]