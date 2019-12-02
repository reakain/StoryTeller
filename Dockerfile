FROM python:3.8-slim-buster

COPY bots/config.py /bots/
COPY bots/autoreply.py /bots/
COPY bots/storybuilder.py /bots/
COPY bots/source_text/kingarther.txt /bots/source_text/
COPY bots/source_text/robinhood.txt /bots/source_text/
COPY bots/source_text/knights.txt /bots/source_text/
COPY bots/source_text/grimm.txt /bots/source_text/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt
RUN python3 -m spacy download en_core_web_sm

WORKDIR /bots
CMD ["python3", "autoreply.py"]
