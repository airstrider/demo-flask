from flask import Flask, render_template, request
import simple_linear_srv

app = Flask(__name__)


@app.route("/")
def main():
    # return render_template('simple_linear_req.html')
    return "ok"


# The five REST APIs below return the JSON format results
@app.route("/linear/simple", methods=["POST"])
def simple():
    return simple_linear_srv.simple_linear(request)


if __name__ == "__main__":
    app.run()
    # app.run(debug=True, port=9090)
