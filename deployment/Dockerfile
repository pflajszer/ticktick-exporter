# Python image to use.
FROM python:3.12.7

# SET WORKDIR TO /app
WORKDIR /app

# Copy Repo contents into /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
RUN playwright install
RUN playwright install-deps   

CMD ["python", "main.py"]