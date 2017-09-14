FROM ubuntu:14.04

# Update OS
RUN sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list \
    && apt-get update && apt-get -y upgrade \
    && apt-get install -y python-dev python-pip

# Set the default directory for our environment
ENV HOME /api
WORKDIR /api

# Add requirements.txt
ADD requirements.txt /api

# Install uwsgi Python web server and requirements
RUN pip install uwsgi && pip install -r requirements.txt

# Create app directory
ADD src/ /api

# Expose port 8000 for uwsgi
EXPOSE 8000

ADD docker-entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
