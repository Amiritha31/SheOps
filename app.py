from flask import Flask

app=Flask(_name_)

@app.route("/")
def home():
    return "Hello from SheOps"
app.run(host="0.0.0.0",port=5001)
