FROM python:3
ENV database=priyanka
ENV user=postgres
ENV password=postgres
ENV host=postgres.cwehvtlrigrg.ap-south-1.rds.amazonaws.com
ENV port=5432
WORKDIR /usr/scr/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python","app.py"]
