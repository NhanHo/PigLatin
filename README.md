# How to run
- Has pip installed
- Python 3.x

```
pip install -r requirements.txt
export FLASK_APP=pig_latin/pig_latin.py
flask run
```

- The microservice will be running at `localhost:5000`

```curl -XPOST -H "Content-Type: text/plain" --data "glove happy" localhost:5000```

# Implementation Note
- The endpoint is at root "/"
- The requirement of adding "yay" to the end for a silent letter was not implemented. As I'm not sure if there is a good way to do it besides hard coding all the possible words.
- We returns error 400 if the string contain any non-ascii character
- Any non-alphanumeric character is considered punctuations.
