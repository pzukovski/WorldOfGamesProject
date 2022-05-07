FROM python:alpine

RUN adduser -D paul

USER paul
ENV PATH="/home/paul/.local/bin:${PATH}"

RUN pip install --upgrade pip
WORKDIR /home/paul
COPY ./flask/ .
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "MainScores.py"]
