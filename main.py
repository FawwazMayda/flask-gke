from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "This is Flask"

@app.route("/status")
def status():
    return "Try to get some txt files using /file"

@app.route("/file")
def file():
    try:
        txt_to_write = "Counter Attack CountryBall"
        with open("new_file.txt","w+") as f:
            f.writelines(txt_to_write)
        f.close()
        return "Able to write"
    except:
        return "Unable to write"

if __name__ == "__main__":
    app.run(debug=True,port=5000)