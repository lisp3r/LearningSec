from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route("/")
def home():
    template = """<!DOCTYPE html>
        <html>
            <head><title>Say hello</title></head>
            <body>
                <h2>Hello, {{ username }}!</h2>
            </body>
        </html>"""

    if user := request.args.get('user'):
        return render_template_string(template, username=user)
    else:
        return render_template_string(template, username="tell us your name")


app.run()