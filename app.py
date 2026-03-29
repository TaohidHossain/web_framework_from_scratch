from api import API

app = API()

@app.route("/home")
def home(request, response):
    response.text = "Home"

@app.route("/about")
def about(request, response):
    response.text = "About"

@app.route("/hello/{name}")
def greetings(request, response, name):
    response.text = f"Hello {name}"

@app.route("/add/{a: d}/{b: d}")
def add(request, response, a, b):
    result = a + b
    response.text = f"{a} + {b} = {result}"