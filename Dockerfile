FROM python:3.9
WORKDIR /app
COPY fir.py .
CMD [ "python","fir.py"]
