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

@app.route("/users")
class User:
    def get(self, req, res):
        res.text = "List of all users"
    
    def post(self, req, res):
        res.text = "Create a new user"