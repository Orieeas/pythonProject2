FROM python:3.10
WORKDIR /pythonProject2

COPY main.py /pythonProject2/main.py

RUN pip install pymongo uvicorn fastapi

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


