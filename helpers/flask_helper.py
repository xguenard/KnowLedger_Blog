#flask helper

#Hello World
from flask import Flask
app = Flask(__name__)

@app.route('/coucou')#will be launch when I go to mysite/coucou
def dire_coucou():
    return 'Coucou !'

#Permet d'avoir des variables dans les liens
@app.route('/article/<int:id_article>')
def article(id_article = 0):#pensez aux cas par default
    id_article = int( id_article)
    return article_path(id_article)


#GET and Post dispatcher
#En fonction de la methode HTTP utilisee, je vais appeler la page avec post ou get
#pour cela je dois importer les requetes flask
from flask import request
#request.path permet d'avoir le chemin de la requete, useless en general

#@app.route('/test', methods=['GET' , 'POST'])
#def testouille():
#   if request.method == 'GET':
        #Logiquement je vais afficher un formulaire
 #   else :
  #      return
        #Logiquement je vais afficher la page en resultat du formulaire


#sans template
@app.route('/')
def accueil():
    mots = ["bonjour", "à", "toi,", "visiteur."]
    puces = ''.join("<li>{}</li>".format(m) for m in mots)
    return """<!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8" />
                <title>{titre}</title>
            </head>
        
            <body>
                <h1>{titre}</h1>
                <ul>
                    {puces}
                </ul>
            </body>
        </html>""".format(titre="Bienvenue !", puces=puces)

#avec template
@app.route('/2')
def accueil2():
    mots  = ['bonjour' , 'poulet']
    return render_template('accueil.html', titre = "Bienvenue !", mots = mots )
#Jinja format dans le html pour que les remplacements soient bien operes.
#Dans le html pour joindre le css on utilise url_for
#<link href="{{ url_for('static', filename='mon_style.css') }}" rel="stylesheet" type="text/css" />


#permet d'ajouter la variable titre a tous les templates jinja
#les variables request, config, session et g sont accessibles a tout fichier template
#on peut mettre plein de choses dans l'objet g, par ex g.titre = "bienvenue"
@app.context_processor
def passer_titre():
    return dict(titre = "testouille")

#Creer des fonctions que l'on pourra utiliser dans les templates
@app.template_filter('nom_du_filtre')
def formater_distance(dist):
    return dist/100

#Creer des tests pour les if
def is_impair(n):
    return True if n%2 == 0 else False
app.jinja_env.test['impair'] = is_impair


if __name__ == '__main__':
    app.run(debug = True )
