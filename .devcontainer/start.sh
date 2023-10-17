#!/bin/bash

# Start Redis
# service redis-server start

# Start MySQL
service mysql start

# Add any other commands or services you'd like to run
# ...

# Keep the container running (if no other foreground process is provided)
tail -f /dev/null
