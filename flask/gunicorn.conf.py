bind = "unix:/tmp/disco-elysium.sock"
workers = 3
timeout = 120
# Access log - records incoming HTTP requests
accesslog = "/var/log/disco-elysium/access.log"
# Error log - records Gunicorn server goings-on
errorlog = "/var/log/disco-elysium/error.log"
# Whether to send Flask output to the error log 
capture_output = True
# How verbose the Gunicorn error logs should be 
loglevel = "info"