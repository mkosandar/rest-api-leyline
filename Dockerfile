FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DATABASE_URL=postgresql://user:password@db:5432/dbname

CMD ["flask", "run", "--host=0.0.0.0", "--port=3000"]
