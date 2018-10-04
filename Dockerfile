FROM python:3

# Force the stdout and stderr streams to be unbuffered
ENV PYTHONUNBUFFERED 1

# Create and use directory for code
RUN mkdir /app
WORKDIR /app

# Add Python dependencies
ADD requirements/ /app/requirements
ADD requirements.txt /app/

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements/dev.txt

# Copy app source code to the working directory
ADD . /app/
