from app import app

@app.route("/")
@app.route("/index")
def index():
    return "hello from dev"

app.run(debug=True)
