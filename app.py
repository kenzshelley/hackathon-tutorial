from flask import Flask, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/users")
def show_page():
    users = ["kenz", "addie", "nastasia", "jamie"]
    return render_template('page.html', users=users)

if __name__ == "__main__":
    app.run()
