import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

#esto para configurar lo que se puede ver por la web
@app.get('/')
def get_list():
    return[1,2,3]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    #return{ 'name': 'Platzi'}
    return """
        <h1>Hola soy una página</h1>
        <p>Soy un párrafo</p>
    """
#estos 2 métodos anteriores se verán en la web
def run():
    store.get_categories()
    
if __name__ == '__main__':
    run()