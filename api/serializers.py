from rest_framework import serializers
from user.models import Post


class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='post:detail',
        lookup_field='slug'
    )

    username = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'username',
            'title',
            'content',
            'url',
            'created',
            'modified_by',
        ]

    def get_username(self, obj):
        return str(obj.user.username)
