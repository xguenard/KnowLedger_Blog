from flask import Flask, render_template, Markup
import markdown
POST_DIR = 'content/posts'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    f = open('content/posts/en/test.md' , 'r')
    return render_template('home.html', content = f.read())

@app.template_filter("markdown")
def render_markdown(markdown_text):
    return Markup( markdown.markdown( markdown_text))

@app.template_filter("puce_url")
def puce():
    return url_for('static', filename='image/pointer.png')

if __name__ == "__main__":
    app.run(debug=True)
