from flask import Flask, render_template, Markup
import markdown
import data_wrapper

POST_DIR = 'content/posts'

app = Flask(__name__)
app.config.from_object(__name__)


website_content = data_wrapper.Content()
#PURE FLASK ROUTINES (app.route, filters, ... )

#HOME PAGE
@app.route('/')
def index():
    global website_content
    website_content.is_en = True
    article_preview , meta_preview = website_content.getPreviewList()
    dates = []
    titles = []

    for elem in meta_preview:
        dates.append( elem[0] )
        titles.append( elem[1] )

    return render_template('home.html', title_list = titles , date_list = dates
                          , summaries_list = article_preview, page = 1)


@app.route('/fr')
def index_fr():
    return render_template('home.html')
#ABOUT
@app.route('/about')
def about():
    return render_template('about.html', page = 2)

#Contact
@app.route('/contact')
def contact():
    return render_template('contact.html' , page = 3)

#ARTICLES
@app.route('/article/fr/<int:id_article>')
def print_article_fr(id_article):
    f = open('content/posts/fr/{}.md'.format( get_article_name( id_article , True )) , 'r' )
    return render_template('article.html', content = f.read())

#FILTERS
@app.template_filter("markdown")
def render_markdown(markdown_text):
    return Markup( markdown.markdown( markdown_text))

@app.template_filter("max_elem")
def get_max():
    global max_elem
    return max_elem

@app.template_filter("puce_url")
def puce():
    return url_for('static', filename='image/pointer.png')

if __name__ == "__main__":
    app.run(debug=True)
