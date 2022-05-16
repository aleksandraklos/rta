FROM python:3.9

WORKDIR /RTA

COPY requirements.txt .

COPY RTA_model_1.pkl .

COPY model.py .

COPY app.py .

RUN pip install -r requirements.txt

CMD ["python", "./app.py"]
