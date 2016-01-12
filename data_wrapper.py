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

        self.fillAtriclesAndMetadatas()
    
    def fillAtriclesAndMetadatas(self):
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
    
    def GetArticle(self, title ):
        """
            return the article
        """
        if self.is_en:
            f = open('content/posts/en/{}.md'.format( title ) , 'r' )
            return f.read()
        else:
            f = open('content/posts/fr/{}.md'.format( title ) , 'r' )
            return f.read()


    def getSizePreview(self ):
        nb_articles = 0

        if self.is_en :
            nb_articles = len( self.en_metadata_list )
        else :
            nb_articles =  len( self.fr_metadata_list )

        return nb_articles if nb_articles < self.preview_max else self.preview_max


    def getPreviewList(self ):
        nb = self.getSizePreview( )
        if self.is_en:
            return self.en_article_preview_list[ -nb : ] , self.en_metadata_list[-nb:]
        else:
            return self.fr_article_preview_list[ -nb : ] , self.fr_metadata_list[-nb:]


