from flask import Flask, render_template, Markup
import markdown
POST_DIR = 'content/posts'

app = Flask(__name__)
app.config.from_object(__name__)

#PURE FLASK ROUTINES (app.route, filters, ... )

articles_list = []
en = True
max_elem = 5

#HOME PAGE
@app.route('/')
def index():
    f = open('content/posts/en/test.md' , 'r')
    elems_list, summary_list = get_last_elems()
    dates = []
    titles = []
    summaries = []
    for elem in elems_list:
        dates.append( elem[0] )
        titles.append( elem[1] )

    for summary in summary_list :
        summaries.append( summary[0] )


    return render_template('home.html', title_list = titles , date_list = dates
                          , summarie_list = summaries, page = 1)


#ABOUT
@app.route('/about')
def about():
    return render_template('about.html', page = 2)

#Contact
@app.route('/contact')
def contact():
    return render_template('contact.html' , page = 3)

#ARTICLES
@app.route('/article/en/<int:id_article>')
def print_article_en(id_article):
    f = open('content/posts/en/{}.md'.format(get_article_name(id_article, False) ) , 'r' )
    return render_template('article.html', content = f.read())

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

#PYTHON TOOLS (file management ... )

def get_article_name( id_article , fr):
    global articles_list
    if( id_article < len(articles_list) ):
        return articles_list[id_article][1 + int(fr)]
    else:
        fill_article_lis()
        if( id_article < len(articles_list) ):
            return articles_list[id_article][1 + int(fr)]
        else:
            return "<center><h3><b>Article not disponible</b></h3></center>"

def fill_article_list():
    """
        fill article_list with the data in content/(en/fr)/summary.txt
        tuple date , titre anglais , titre francais
    """
    global articles_list
    global en
    articles_list =[]

    if (en == True ):
        f = open('content/en/summary.txt' , 'r' )
    else:
        f = open('content/fr/sommaire.txt' , 'r' )

    for line in f:
        if line[0] == '#':
            continue
        articles_list.append( line[:-1].split(' , '))


def get_last_elems_en():
    """
        return 5 last elems, or the max if not enough articles
    """
    global articles_list # date , titre , nom article 
    global max_elem 
    global en

    fill_article_lis()
    list_size = len( articles_list )
    max_elem = 5 if list_size >= 5 else list_size
    metadata_list = []
    summary_list = []

    for i in range(0, max_elem):
        tmp_line = articles_list[ -(i+1) ]
        metadata_list.append( tmp_line )
        #read the english summary
        if( en == True ):
            f1 = open('content/posts/en/{}_summary.md'.format( tmp_line[2] )  , 'r')
        else:
        #read the french
            f1 = open('content/posts/fr/{}_summary.md'.format( tmp_line[2] ) , 'r')
        summary_list.append(  f1.read() )

    return metadata_list, summary_list
    






if __name__ == "__main__":
    app.run(debug=True)
