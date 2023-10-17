# start from Ubuntu 18.04
FROM ubuntu:18.04

# Install necessary utilities
RUN apt-get update && apt-get install -y \
    software-properties-common \
    curl \
    git

# Set up Git config
RUN git config --global user.email "evanrich2404@gmail.com" && \
    git config --global user.name "evanrich2404"

# add deadsnakes PPA (this is for python 3.7 on older ubuntu) and install python 3.7
RUN add-apt-repository ppa:deadsnakes/ppa -y && \
    apt-get update && \
    apt-get install -y \
    python3.7 \
    python3.7-dev \
    python3-pip \
    python3.7-venv

# Set Python 3.7 as the default
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Install redis server
# RUN apt-get install -y redis-server

# Grab GPG keys for MySQL
RUN apt-get install -y wget gnupg && \
    wget -O /tmp/RPM-GPG-KEY-mysql https://repo.mysql.com/RPM-GPG-KEY-mysql && \
    apt-key add /tmp/RPM-GPG-KEY-mysql

# Install MySQL 5.7
RUN apt-get install -y wget gnupg && \
    wget -O /tmp/RPM-GPG-KEY-mysql https://repo.mysql.com/RPM-GPG-KEY-mysql && \
    apt-key add /tmp/RPM-GPG-KEY-mysql && \
    wget https://dev.mysql.com/get/mysql-apt-config_0.8.15-1_all.deb && \
    DEBIAN_FRONTEND=noninteractive dpkg -i mysql-apt-config_0.8.15-1_all.deb && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server=5.7.30-1ubuntu18.04 && \
    rm mysql-apt-config_0.8.15-1_all.deb

# Install necessary python packages
RUN python3 -m pip install \
    pycodestyle==2.5 \
    sqlalchemy==1.3.8 \
    flask \
    flask_sqlalchemy \
    flask-babel \
    parameterized
    # redis

# example venv
# RUN python3 -m venv /path/to/new/virtual/environment

# Setup redis server ip
# RUN sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf

# Expose any necessary ports
EXPOSE 5000 3306

# Copy start script and set as entrypoint
COPY start.sh /start.sh
RUN chmod +x /start.sh
ENTRYPOINT ["/start.sh"]
