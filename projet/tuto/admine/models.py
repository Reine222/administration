from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=250)
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    statut = models.BooleanField()
    def __str__(self):
        return self.nom


class Article(models.Model):
    image = models.ImageField(upload_to='blog_image')
    titre = models.CharField(max_length=250)
    date = models.DateField(auto_now=False, auto_now_add=False)
    #categorie = models.ForeignKey("Categorie", on_delete=models.CASCADE, related_name = 'CategorieArticle')
    auteur = models.ForeignKey( User, on_delete=models.CASCADE, related_name = 'UserArticle')
    description = models.TextField()
    content = models.TextField()
    tag = models.ManyToManyField("Tag",related_name ='TagArticle')
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    statut = models.BooleanField()
    def __str__(self):
        return self.titre

class Commentaire(models.Model):
    image = models.ImageField(upload_to='blog_image')
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    nom = models.CharField(max_length=250)
    utilisateur = models.ForeignKey( User, on_delete=models.CASCADE, related_name = 'UserCommentaire')
    message = models.TextField()
    article = models.ForeignKey("Article", on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    statut = models.BooleanField()
    def __str__(self):
        return self.nom


class Tag(models.Model):
    nom = models.CharField(max_length=250)
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    statut = models.BooleanField()
    def __str__(self):
        return self.nom


