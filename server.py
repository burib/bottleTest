import bottle

@bottle.get('/')
def hello():
    return bottle.static_file('index.html', '.')

@bottle.post('/POST')
def hello():
    bottle.request.content_type = 'application/json'
    bottle.response.content_type = 'application/json'

    responseData = {
        "data": {
            "json": bottle.request.json,
            "bodyRead": bottle.request.body.read()
        }
    }

    print(responseData)

    return responseData

@bottle.delete('/DELETE')
def hello():
    bottle.response.content_type = 'application/json'
    
    responseData = {
        "data": {
            "json": bottle.request.json,
            "bodyRead": bottle.request.body.read()
        }
    }

    print(responseData)

    return responseData

bottle.run(host='localhost', port=8080, debug=True)
