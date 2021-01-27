# from django.db import models
# from djongo import dmodels
from django.utils.html import mark_safe
from django import forms
from django.contrib.postgres.fields import ArrayField, JSONField
from django.utils.timezone import now
from django.db import models




# Create your models here.

# class MatchModel(dmodels.Model):
#     activity_name = dmodels.CharField(max_length=100)
#
#     class Meta:
#         abstract = True
#
#
# class MatchKeyword(dmodels.Model):
#     keyword = dmodels.CharField(max_length=100)
#     image_key = dmodels.FileField(blank=True)
#
#     # class Meta:
#     #     abstract = True
#
#     def __str__(self):
#         return '%s, %s' % (self.keyword, self.image_key)
#
#
# class KeywordForm(forms.ModelForm):
#     class Meta:
#         model = MatchKeyword
#         fields = (
#             'keyword', 'image_key'
#         )
#
#
# class MatchDefinition(dmodels.Model):
#     definition = dmodels.CharField(max_length=100)
#     image_def = dmodels.FileField(blank=True)
#
#     # class Meta:
#     #     abstract = True
#
#     def __str__(self):
#         return '%s, %s' % (self.definition, self.image_def)
#
#
# class DefinitionForm(forms.ModelForm):
#     class Meta:
#         model = MatchDefinition
#         fields = (
#             'definition', 'image_def'
#         )
#
#
# class MatchContent(dmodels.Model):
#     match = dmodels.EmbeddedField(model_container=MatchModel, null=False)
#
#     match_image = dmodels.FileField(blank=True)
#     match_keyword = dmodels.CharField(max_length=255)
#     match_definition = dmodels.TextField()
#     match_image_one = dmodels.FileField(blank=True)
#     match_keyword_one = dmodels.CharField(max_length=255)
#     match_definition_one = dmodels.TextField()
#     match_image_two = dmodels.FileField(blank=True)
#     match_keyword_two = dmodels.CharField(max_length=255)
#     match_definition_two = dmodels.TextField()
#     match_image_three = dmodels.FileField(blank=True)
#     match_keyword_three = dmodels.CharField(max_length=255)
#     match_definition_three = dmodels.TextField()
#     match_image_four = dmodels.FileField(blank=True)
#     match_keyword_four = dmodels.CharField(max_length=255)
#     match_definition_four = dmodels.TextField()
#     objects = dmodels.DjongoManager()
#
#
# # creating matchup game
# class Entry(dmodels.Model):
#     match = dmodels.EmbeddedField(model_container=MatchModel, null=False)
#     keywords = dmodels.EmbeddedField(model_container=MatchKeyword, model_form_class=KeywordForm)
#     definitions = dmodels.EmbeddedField(model_container=MatchDefinition, model_form_class=DefinitionForm)
#     objects = dmodels.DjongoManager()
#


class MatName(models.Model):
    active_name = models.CharField(max_length=100)

    class Meta:
        abstract = True


class GameList(models.Model):
    keyword = ArrayField(models.CharField(max_length=100))
    img_key = ArrayField(models.FileField(blank=True))
    definition = ArrayField(models.CharField(max_length=500))
    mat_name = models.CharField(max_length=100)

    def __str__(self):
        return self.mat_name

    # def image_key_tag(self):
    #     if self.img_key:
    #         return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.photo))
    #     else:
    #         return mark_safe('<img src="/media/document/default.jpg" width="50" height="50" />')
    #
    # image_tag.short_description = 'Image'