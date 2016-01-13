from flask import Flask, render_template, Markup, url_for
import markdown
import data_wrapper

POST_DIR = 'content/posts'

app = Flask(__name__)
app.config.from_object(__name__)


website_content = data_wrapper.Content()
#PURE FLASK ROUTINES (app.route, filters, ... )

#HOME PAGE
def render_home( lang ):
    global website_content
    website_content.is_en = lang
    article_preview , meta_preview = website_content.getPreviewList()
    
    readmore = "Readmore"
    if not lang:
        readmore = "Lire"

    return render_template('home.html', metadata_list = meta_preview
                          , article_list = article_preview
                          , nb_elem = website_content.getSizePreview()
                          , read_link = readmore
                          , page = 1)


@app.route('/')
def index():
    return render_home( True )
    
@app.route('/fr')
def index_fr():
    return render_home( False )

#ABOUT
@app.route('/about')
def about():
    return render_template('about.html', page = 2)

#Contact
@app.route('/contact')
def contact():
    return render_template('contact.html' , page = 3)

#ARTICLES
@app.route('/articles')
def print_all_articles():
    global website_content
    prevs , metas, nb_elem = website_content.getFullList()
    return render_template('articles_list.html', prevs_list = prevs, meta_list = metas 
                          , nb_elems = nb_elem, page = 4)


@app.route('/article/<article_title>')
def print_article(article_title):
    global website_content
    return render_template('article.html', content = website_content.getArticle( article_title ) )

#FILTERS
@app.template_filter("markdown")
def render_markdown(markdown_text):
    return Markup( markdown.markdown(markdown_text))

@app.template_filter("preview_image_url")
def get_image_path( title ):
    global website_content
    return website_content.getPreviewImagePath( title ) 

@app.context_processor
def header_data():
    global website_content
    if website_content.is_en:
        return dict( home = "Home" , about = "About", read_more = "Read more")
    else:
        return dict( home = "Accueil" , about = "A propos" , read_more = "Lire")

if __name__ == "__main__":
    app.run(debug=True)
