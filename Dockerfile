# syntax=docker/dockerfile:1
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYHTONBUFFERED 1

# Set working directory
WORKDIR /OCR_P8

# Install dependencies
COPY requirements.txt /OCR_P8/
RUN pip install -r requirements.txt 

# Copy project
COPY . /OCR_P8/