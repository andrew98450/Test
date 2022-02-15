FROM python:3.9-slim

RUN pip install -r requirement.txt

CMD ["python", "main.py"]
