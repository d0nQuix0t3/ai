FROM python:3.7
ADD ./ai-dash /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python index.py