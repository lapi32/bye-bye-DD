import pip
pip.main(['install', 'flask'])

from flask import Flask, render_template_string, send_file, abort
import os

app = Flask(__name__)


PORT_NUM = 3000


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


PAGE_TEMPLATE = """
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">        <title>Google Classroom</title>
    </head>
    <body>
        <h1>anything but work 😭</h1>
        <ul>
            {% for f in html_files %}
            <a href="{{ url_for('see_file', filename=f) }}">
                <li>{{ f }}</li>
            </a>
            {% endfor %}

            <li>
                <a 
                    href = "https://www.kroger.com/product/images/xlarge/front/0001300000218"
                    target = "_blank"
                    rel = "noopener noreferrer"
                    >MUSSTAARD
                </a>
            </li>
        </ul>
    </body>
</html>
"""




@app.route("/")
def homepage():
   
    try:
        all_files = os.listdir(BASE_DIR)
        htmls = []
        for item in all_files:  
            if item.endswith(".html"):
                htmls.append(item)
    except Exception as e:
     
        return f"Couldn't read directory: {str(e)}", 500
    
    return render_template_string(PAGE_TEMPLATE, html_files=htmls)


@app.route("/view/<filename>")
def see_file(filename):

    if not filename.lower().endswith(".html"):
        abort(400, description="Not an HTML file, probably my fault")
    
    fpath = os.path.join(BASE_DIR, filename)

    if not os.path.isfile(fpath):

        abort(404, description="File not found, probably my fault")
    
    return send_file(fpath)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT_NUM)
