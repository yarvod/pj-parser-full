from rest_framework import serializers

from constants import MessageEntityTypes


class EntityRawSerializer(serializers.Serializer):
    type = serializers.SerializerMethodField()
    offset = serializers.IntegerField()
    length = serializers.IntegerField()
    url = serializers.URLField(allow_blank=True, allow_null=True, required=False)

    @staticmethod
    def get_type(obj):
        return MessageEntityTypes.MAP_CLASSES.get(obj.__class__.__name__, '')


class MessageEntityRawSerializer(serializers.Serializer):
    text = serializers.SerializerMethodField()
    entity = serializers.SerializerMethodField()

    @staticmethod
    def get_text(obj):
        return obj[1]

    @staticmethod
    def get_entity(obj):
        return EntityRawSerializer(obj[0]).data


class MessageRawSeralizer(serializers.Serializer):
    message = serializers.CharField()
    # entities = serializers.SerializerMethodField()

    # @staticmethod
    # def get_entities(obj):
    #     entities = obj.get_entities_text()
    #     return MessageEntityRawSerializer(entities, many=True).data

