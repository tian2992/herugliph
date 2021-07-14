# Herugliph

## What it does

Analyzes a text string according to the rules of "HeruCode" Language. 
Returns a JSON with counted verbs, prepositions and the vocabulary used in the given string.

## How to Run

To run try installing Flask and running

```python app.py```

## Endpoints

* ```/parse``` : POST a JSON document with 'text' as data field
* ```/parse_post``` : POST a 'text' variable as data field