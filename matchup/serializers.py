from rest_framework import serializers
from .models import GameList
from rest_meets_djongo.serializers import DjongoModelSerializer


# class MatchModelSerializer(serializers.ModelSerializer):
#     match_image = serializers.SerializerMethodField()
#
#     class Meta:
#         fields = '__all__'
#         model = MatchModel
#
#     def get_match_image(self, obj):
#         re_serializer = MatchModelSerializer(obj.match_image, many=True)
#         return re_serializer.data
#
#
# class MatchContentSerializer(DjongoModelSerializer):
#     class Meta:
#         # fields = ['activity_name', 'match_image', 'match_keyword', 'match_definition', 'created_at']
#         fields = '__all__'
#         model = MatchContent
#         abstract = True
#
#
# class StringListField(serializers.ListField):
#     child = serializers.CharField()
#
#
# class EntrySerializer(DjongoModelSerializer):
#     # keywords = serializers.SerializerMethodField()
#     # definitions = serializers.SerializerMethodField()
#     # match = serializers.SerializerMethodField()
#
#     class Meta:
#         fields = ('keywords', 'definitions', 'match', 'id')
#         model = Entry
#         # abstract = True
#
#     def get_keywords(self, obj):
#         return_data = None
#         if type(obj.keywords) == list:
#             embedded_list = []
#             for item in obj.keywords:
#                 embedded_dict = item.__dict__
#                 for key in list(embedded_dict.keys()):
#                     if key.startswith('_'):
#                         embedded_dict.pop(key)
#                 embedded_list.append(embedded_dict)
#             return_data = embedded_list
#         else:
#             embedded_dict = obj.embedded_field
#             for key in list(embedded_dict.keys()):
#                 if key.startswith('_'):
#                     embedded_dict.pop(key)
#             return_data = embedded_dict
#         return return_data
#
#     def get_definitions(self, obj):
#         return_data = None
#         if type(obj.definitions) == list:
#             embedded_list = []
#             for item in obj.definitions:
#                 embedded_dict = item.__dict__
#                 for key in list(embedded_dict.keys()):
#                     if key.startswith('_'):
#                         embedded_dict.pop(key)
#                 embedded_list.append(embedded_dict)
#             return_data = embedded_list
#         else:
#             embedded_dict = obj.embedded_field
#             for key in list(embedded_dict.keys()):
#                 if key.startswith('_'):
#                     embedded_dict.pop(key)
#             return_data = embedded_dict
#         return return_data
#



class GameListSerializer(serializers.ModelSerializer):
    keyword = serializers.ListField(child=serializers.CharField())
    img_key = serializers.ListField(child=serializers.FileField())
    definition = serializers.ListField(child=serializers.CharField(max_length=500))
    mat_name = serializers.CharField()

    class Meta:
        fields= '__all__'
        model = GameList