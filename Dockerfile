FROM python:3.9-slim

RUN pip install remi pycryptodome

CMD ["python", "main.py"]
