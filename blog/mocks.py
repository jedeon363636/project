from django.http import Http404

class Post():
    POSTS =[
        {'id':1, 'title':'Premier Post', 'body':'c est mon premier poste'},
        {'id':2, 'title':'Deuxième Post', 'body':'c est mon deuxième poste'},
        {'id':3, 'title':'Troisème Post', 'body':'c est mon troisième poste'},
    ]

    @classmethod
    def all(cls):
      return cls.POSTS

    @classmethod
    def find(cls, id):
      try:

         return cls.POSTS[int(id) - 1]
      except:
        raise Http404('Désolé,ce post {} n existe pas'.format(id))