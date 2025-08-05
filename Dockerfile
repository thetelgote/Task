FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]




#--change the code 


# FROM python:3.10

# WORKDIR /app

# COPY app.py .

# RUN pip install flask bugsnag

# CMD ["python", "app.py"]
