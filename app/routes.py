from app import app
from config import API_BASE

@app.route('/')
@app.route(API_BASE + '/index')
def index():
    return "Hello, World!"
