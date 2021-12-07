# FSK_Raffle

This is a small project intended to implement a simple raffle application in flask. It expects a json dictionary consisting of a list(array) of participants and an integer representing a number of winners (with the constraint that this does not exceed the length of the participants array) and returns the list of winners.

## Installation 

To install the application, you should install all the dependencies in the `requirements.txt` file using the command below:

```bash
pip install -r requirements.txt
```

## Running the Application

After installation, set the FLASK_APP environment variable and run the application. Heres is how ypu should set the FLASK_APP variable from the websited root folder:

```bash
export FLASK_APP=app.py
flask run
```

## API Reference

The API has a single endpoint `POST /winners/get`

Here is a sample request and response:

```bash
 curl -X POST -H 'Content-Type:application/json' -d '{"participants":["Gift","Chimphonda","Mphatso","GiftXXVI"], "winners":1}' http://127.0.0.1:5000/winners/get
```

```json
{
  "success": true,
  "winners": ["Gift"]
}
```

## Error Codes

In case of an error, the API may return the following error codes:

```http
400
403
405
422
500
```

Here is an example of an error response:

```bash
curl -X POST -H 'Content-Type:application/json' -d '{"winners":1}' http://127.0.0.1:5000/winners/get
```

```json
{
  "error": 422,
  "message": "unprocessable",
  "success": false
}
```
