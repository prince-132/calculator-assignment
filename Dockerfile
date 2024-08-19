FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
# Set ENTRYPOINT to ensure pytest is available
ENTRYPOINT ["pytest"]
CMD ["python", "calculator.py"]