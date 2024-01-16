FROM python:3.11.2

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app
ENV FLASK_APP=data_science_app.py
WORKDIR /app

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
