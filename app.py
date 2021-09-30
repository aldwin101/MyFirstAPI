import mariadb
from flask import Flask, request, Response
import json

app=Flask(__name__)

animals = [
    {
        'name' : 'tiger'
    }, 
    {
        'name' : 'lion'
    }, 
    {
        'name' : 'elephant'
    }
]

@app.route('/animal', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def animal_list():
    if(request.method == 'GET'):
        return Response(json.dumps(animals),
                        mimetype='application/json',
                        status=200)
    elif (request.method == 'POST'):
        return Response(json.dumps("Created successfully"),
                        mimetype="application/json",
                        status=200)
    elif (request.method == 'PATCH'):
        return Response(json.dumps("Updated successfully"),
                        mimetype="application/json",
                        status=200)
    elif (request.method == 'DELETE'):
        return Response(json.dumps("Deleted Successfully"),
                        mimetype="application/json",
                        status=200)
    else:
        print('You have encountered an error')