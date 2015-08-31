# hcj-utils
## Adding virtualenv
```
mkvirtualenv --python=/usr/bin/python3 missingkids
pip install -r requirements.txt
```

## Run python with env vars from file
```
export $(cat .env | xargs) && python manage.py
```
