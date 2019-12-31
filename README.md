# administration
tuto admin Django

# 1-list_display
# 2-list_filter
# 3-search_field
# 4-date_hierarchy
# 5-actions
# 6-list_display_links
# 7-ordering
# 8-inlines
# 9-readonly_fields
# 10-list_per_page
# 11-filter_horizontal
# 12-fieldsets


# 1- Importation des models dans le fichier admin.py : 
from . import models
# 2- Integrer Django admin interface :
suivre le tuto sur le github de parrain
# 3- Creer l'admin : voici un exemple a suivre

      from django.contrib import admin



      #-------------------------------------- IMPORTATION DES MODELS ---------------------------------------------#
      from . import models

      #-------------------------------------- IMPORTATION DE MARK_SAFE ---------------------------------------------#
      from django.utils.safestring import mark_safe


      # Register your models here.

      #-------------------------------------- CLASSE PERMETTANT D'AJOUTER LE MODEL COMMENTAIRE EN LIGNE dans la page detail de article ----------------------#

      class CommentaireInline(admin.TabularInline):
          model = models.Commentaire
          extra = 0


      #-------------------------------------- CREATION DU MODEL CATEGORIE DANS L'ADMIN ---------------------------------------------#




      @admin.register(models.Categorie)
      class CategorieAdmin(admin.ModelAdmin):
          list_display = ('nom', 'date_add', 'date_upd', 'statut',)
          list_filter = ('date_add', 'date_upd', 'statut',)
          search_field = ('nom')
          actions = ('active', 'desactive') 
          def active(self, request, queryset):
              queryset.update(statut = True)
              self.message_user(request, 'Activer une categorie')
          active.short_description = 'active categorie'

          def desactive(self, request, queryset):
              queryset.update(statut = False)
              self.message_user(request, 'Desactiver une categorie')
          desactive.short_description = 'desactive categorie'
          ordering = ('nom',)
          list_per_page = 1
          date_hierarchy = ('date_add')




      #-------------------------------------- CREATION DU MODEL ARTICLE DANS L'ADMIN ---------------------------------------------#

      @admin.register(models.Article)
      class ArticleAdmin(admin.ModelAdmin):

          # AFFICHAGE DES CHAMPS DU MODEL DANS L'ADMIN #
          
          list_display = ('auteur', 'titre', 'date', 'description', 'content', 'date_add', 'date_upd', 'statut', 'view_image',)


          # FILTRAGE DU MODEL DANS L'ADMIN #
          
          list_filter = ('date', 'date_add', 'date_upd', 'statut',)


          #  CHAMPS DE RECHERCHE DU MODEL DANS L'ADMIN #
          
          search_field = ('titre')


          # MODIFIER LES SATATUTS DU MODEL DANS L'ADMIN #
          
          actions = ('active', 'desactive') 
          def active(self, request, queryset):
              queryset.update(statut = True)
              self.message_user(request, 'Activer une categorie')
          active.short_description = 'active categorie'

          def desactive(self, request, queryset):
              queryset.update(statut = False)
              self.message_user(request, 'Desactiver une categorie')
          desactive.short_description = 'desactive categorie'


          # ORDONNER DES CHAMPS DU MODEL DANS L'ADMIN #
          
          ordering = ('titre',)


          # CREATION DE PAGINATION( 1 element par page dans cet exemple) DANS L'ADMIN #
          
          list_per_page = 1


          # ORDONNER DES CHAMPS DU MODEL EN FONCTION DE LA DATE DANS L'ADMIN #
          
          date_hierarchy = ('date')


          # AFFICHAGE DES CHAMPS DU MODEL COMME DES LIENS DANS L'ADMIN #
          
          list_display_links = ('view_image', 'titre',)


          # AFFICHAGE DES MODELS EN LIGNE SOUS LE DETAIL DU MODEL DANS L'ADMIN #
          
          inlines = [CommentaireInline]


          # AFFICHAGE DE L'IMAGE DANS LE DEATAIL DU MODEL DANS L'ADMIN #
          
          readonly_fields = ['detail_image']


          # AFFICHAGE DES MODELS SOUS LA MEME FORME QUE LES GROUPES DANS L'ADMIN (utiliser pour les relations ManyToMany) #
          
          filter_horizontal = ('tag',)


          #  STRUCTURER LES CHAMPS DU MODEL AVEC DES PANNELS DANS L'ADMIN #
          
          fieldsets = [
              ('les clés etrangeres', {'fields': ['auteur', 'tag',]}),
              ('les champs specifiques', {'fields': ['titre', 'description', 'date', 'content', 'image']}),
              ('les champs standards', {'fields': ['statut',]}),
          ]

          # FONCTION PERMETTANT D'AFFICHER L'IMAGE DANS LA TABLE ET LE DETAIL DU MODEL #
          def view_image(self, obj):
              return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))

          def detail_image(self, obj):
              return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))



      #-------------------------------------- CREATION DU MODEL COMMENTAIRE DANS L'ADMIN ---------------------------------------------#


      @admin.register(models.Commentaire)
      class CommentaireAdmin(admin.ModelAdmin):
          list_display = ('utilisateur', 'article', 'nom', 'date', 'message', 'date_add', 'date_upd', 'statut','view_image',)
          list_filter = ('date_add', 'date_upd', 'statut',)
          search_field = ('utilisateur')
          readonly_fields = ['detail_image']

          def view_image(self, obj):
              return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))

          def detail_image(self, obj):
              return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))



      #-------------------------------------- CREATION DU MODEL TAG DANS L'ADMIN ---------------------------------------------#


      @admin.register(models.Tag)
      class TagAdmin(admin.ModelAdmin):
          list_display = ('nom', 'date_add', 'date_upd', 'statut',)
          list_filter = ('date_add', 'date_upd', 'statut',)
          search_field = ('nom')
