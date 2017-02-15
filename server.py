import bottle

@bottle.get('/')
def hello():
    return bottle.static_file('index.html', '.')

@bottle.post('/POST')
def hello():
    bottle.response.content_type = 'application/json'

    return {
        "data": {
            "json": bottle.request.json,
            "bodyRead": bottle.request.body.read()
        }
    }

@bottle.delete('/DELETE')
def hello():
    bottle.response.content_type = 'application/json'
    
    return {
        "data": {
            "json": bottle.request.json,
            "bodyRead": bottle.request.body.read()
        }
    }

bottle.run(host='localhost', port=8080, debug=True)
