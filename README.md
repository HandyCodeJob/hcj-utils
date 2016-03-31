# hcj-utils
## Adding virtualenv
```
mkvirtualenv --python=/usr/bin/python3 missingkids
pip install -r requirements.txt
```

## Write all envars from heroku app to .env file
```
heroku config | tail -n +2 | perl -pe 's/(\w*):\s*(\S*)/$1=$2/g' >> .env
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
