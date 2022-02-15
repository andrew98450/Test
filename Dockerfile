FROM python:3.9-slim

COPY . ./

RUN pip install -r requirement.txt

CMD ["python", "main.py"]
