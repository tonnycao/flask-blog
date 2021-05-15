# flask-post-sqlite

Create a virtualenv and activate it:
```
 python3 -m venv venv
 source venv/bin/activate
```

Install Flaskr

```
pip install -e .
```

Run
```
export FLASK_APP=flasker
export FLASK_ENV=development
flask init-db
flask run
python3 run.py --port=8080
```