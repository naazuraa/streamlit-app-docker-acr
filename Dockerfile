FROM python:3.9.0
EXPOSE 8501
CMD mkdir -p /app
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . /app
COPY . .
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]
