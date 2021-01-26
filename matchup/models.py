# from django.db import models
from djongo import models
from django import forms


# Create your models here.

class MatchModel(models.Model):
    activity_name = models.CharField(max_length=100)

    class Meta:
        abstract = True


class MatchKeyword(models.Model):
    keyword = models.CharField(max_length=100)
    image_key = models.FileField()

    # class Meta:
    #     abstract = True

    def __str__(self):
        return '%s, %s' % (self.keyword, self.image_key)


class KeywordForm(forms.ModelForm):
    class Meta:
        model = MatchKeyword
        fields = (
            'keyword', 'image_key'
        )


class MatchDefinition(models.Model):
    definition = models.CharField(max_length=100)
    image_def = models.FileField()

    # class Meta:
    #     abstract = True

    def __str__(self):
        return '%s, %s' % (self.definition, self.image_def)


class DefinitionForm(forms.ModelForm):
    class Meta:
        model = MatchDefinition
        fields = (
            'definition', 'image_def'
        )


class MatchContent(models.Model):
    match = models.EmbeddedField(model_container=MatchModel, null=False)

    match_image = models.FileField(blank=True)
    match_keyword = models.CharField(max_length=255)
    match_definition = models.TextField()
    match_image_one = models.FileField(blank=True)
    match_keyword_one = models.CharField(max_length=255)
    match_definition_one = models.TextField()
    match_image_two = models.FileField(blank=True)
    match_keyword_two = models.CharField(max_length=255)
    match_definition_two = models.TextField()
    match_image_three = models.FileField(blank=True)
    match_keyword_three = models.CharField(max_length=255)
    match_definition_three = models.TextField()
    match_image_four = models.FileField(blank=True)
    match_keyword_four = models.CharField(max_length=255)
    match_definition_four = models.TextField()
    objects = models.DjongoManager()


# creating matchup game
class Entry(models.Model):
    match = models.EmbeddedField(model_container=MatchModel, null=False)
    keywords = models.EmbeddedField(model_container=MatchKeyword, model_form_class=KeywordForm)
    definitions = models.EmbeddedField(model_container=MatchDefinition, model_form_class=DefinitionForm)
    objects = models.DjongoManager()

