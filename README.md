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

## Clean out all .pyc files recursively
```
find . -name '*.pyc' -delete
```

## [Finding all files containing a string](http://stackoverflow.com/a/16957078)
```
grep -rnw . -e "pattern"
grep -rnw . -e "pattern" --include=\*.{c,h} --exclude-dir={dir1,dir2,*.dst}
```
