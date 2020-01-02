import os

class Config:
  SECRET_KEY = os.environ.get('WTFORM_SECRET') or 'thisismysecret'