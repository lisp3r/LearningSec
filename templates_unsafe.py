from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route("/")
def home():
    template = """<!DOCTYPE html>
            <html>
                <head><title>Say hello</title></head>
                <body>
                    <h2>Hello, %s!</h2>
                </body>
            </html>"""

    if user := request.args.get('user'):  # {{ os.__dict__ }}
        return render_template_string(template % user)
    else:
        return render_template_string(template % "Hello, tell your name")


app.run()
