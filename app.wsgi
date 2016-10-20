#!/usr/bin/python3.5
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/cs373f-idb/")

from app.app import app as application

