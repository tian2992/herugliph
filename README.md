# Herugliph

## What it does

Analyzes a text string according to the rules of "HeruCode" Language. 
Returns a JSON with counted verbs, prepositions and the vocabulary used in the given string.

## How to Run

To run try installing Flask and running

```
$ python app.py
```

You can also use Docker 

```bash
$ docker build -t heru .
$ docker run -e PORT=8080 -p 8080:8080 heru
```

To test the POST value, use curl_post.sh to hit localhost:8080 endpoint using Test Set A

You can also run logic and unit tests using Nose ```nosetest``` or any other pytest runner.

## Endpoints

* ```/parse``` : POST a JSON document with 'text' as data field
* ```/parse_post``` : POST a 'text' variable as data field