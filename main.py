from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    model = {"title":"Welcome Jenkins Ardley to the AppEngine autoscaled page. Don't forget to aim the deploy script at your personal CSR repo."}
    return render_template('index.html', model=model)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)

