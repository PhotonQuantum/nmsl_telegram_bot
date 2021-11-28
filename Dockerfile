FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./nmsl_bot ./nmsl_bot
CMD ["python", "-m", "nmsl_bot.__main__"]
