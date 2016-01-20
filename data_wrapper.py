#PYTHON TOOLS (file management ... )
class Content:
    
    def __init__(self):
        """
            Data wrapper initializer
        """
        self.preview_max = 5

        self.en_article_preview_list = []
        self.en_metadata_list = []

        self.fr_article_preview_list = []
        self.fr_metadata_list = []
        self.is_en = True

        self.fill_atricles_metadatas()
    
    def fill_atricles_metadatas(self):
        """
            will get all data for previews, titles, dates...
        """
        self.en_article_preview_list = []
        self.en_metadata_list = []
        en_file = open('content/posts/en/summary.txt')

        for line in en_file:
            if line[0] == '#':
                continue
            self.en_metadata_list.append( line[:-1].split(' , ' ) )
        
        for row in self.en_metadata_list:
            tmp = open('content/posts/en/{}_preview.md'.format( row[2] ) , 'r' )
            self.en_article_preview_list.append( tmp.read() )
        
        self.fr_article_preview_list = []
        self.fr_metadata_list = []
        fr_file = open('content/posts/fr/sommaire.txt')

        for line in fr_file:
            if line[0]  == '#':
                continue
            self.fr_metadata_list.append( line[:-1].split(' , ') )

        for row in self.fr_metadata_list:
            tmp = open('content/posts/fr/{}_preview.md'.format( row[2] ) , 'r' )
            self.fr_article_preview_list.append( tmp.read() )
    
    def get_article(self, title ):
        """
            return the article
        """
        if any( elm[2] == title for elm in self.en_metadata_list):
            self.is_en = True
            f = open('content/posts/en/{}.md'.format( title ) , 'r' )
            return f.read()
        if any( elm[2] == title for elm in self.fr_metadata_list):
            self.is_en = False
            f = open('content/posts/fr/{}.md'.format( title ) , 'r' )
            return f.read()
        return 'These aren\'t the droids you are looking for...'

    def get_preview_img_path( self, title ):
       """
           given a title return the image's path related to this title.
       """
       return "images/{}_preview_img.png".format( title )



    def get_size_preview(self ):
        nb_articles = 0

        if self.is_en :
            nb_articles = len( self.en_metadata_list )
        else :
            nb_articles =  len( self.fr_metadata_list )

        return nb_articles if nb_articles < self.preview_max else self.preview_max


    def get_preview_list(self ):
        nb = self.get_size_preview( )
        if self.is_en:
            return self.en_article_preview_list[ -nb : ] , self.en_metadata_list[-nb:]
        else:
            return self.fr_article_preview_list[ -nb : ] , self.fr_metadata_list[-nb:]

    def get_full_list( self ):
       if self.is_en:
           return self.en_article_preview_list[:: -1] \
                   , self.en_metadata_list[:: -1], len(self.en_metadata_list)
       else:
           return self.fr_article_preview_list[:: -1] \
                   , self.fr_metadata_list[:: -1], len(self.fr_metadata_list)

