from flask import Flask, send_from_directory, render_template

app = Flask(__name__)


# URL GET: http://localhost/ ->> get_index() -->> client

# http:// localhost  /path/path/something.html

# http:// -> scheme
# localhost -> hostname
# /path1/path2/something.html -> URL path
# / - root path

@app.route("/")
def get_index():
    return r"""<!doctype html><html lang="en">
<body>
    <h1>Simple static index</h1>
    <ul>
        <li><a href="/pages/page1.html">Page1</a></li>
        <li><a href="/pages/page2.html">Page2</a></li>
        <li><a href="/template/data1">Template. Parameter: data1 </a></li>
        <li><a href="/template/data2">Template. Parameter: data2 </a></li>
    </ul>
</body>
</html>"""

# URL GET: http://localhost/pages/page1.html
# <type:name>
@app.route("/pages/<path:path_segment_name>")
def get_static_page(path_segment_name):
    return send_from_directory("pages", path_segment_name)


# URL GET: http://localhost/template/anything

@app.route("/template/<path:function_parfm_from_path>")
def get_template_page(function_parfm_from_path=None):
    return render_template(
        'page3.html.j2',
        template_param=function_parfm_from_path)
