from flask import Flask
print(__name__)
app = Flask(__name__)

@app.route('/')
def run():
    return "executed."

if __name__ == "__main__":
    print('running')
    app.run()