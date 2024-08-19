FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run pytest when the container launches
ENTRYPOINT ["pytest"]

CMD ["python", "calculator.py"]