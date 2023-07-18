FROM python:3.6
WORKDIR /
COPY /the-real-devops-challenge /the-real-devops-challenge
WORKDIR /the-real-devops-challenge
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
