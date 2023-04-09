from rest_framework import serializers
from ..models import Episode, CommentEpisode, Playmusic, Playlist, EpisodeLike
from ...main.models import Category, Tag


class MiniCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']
        ref_name = 'mini_category'


class MiniTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']
        ref_name = 'mini_tag'


class MiniCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentEpisode
        fields = ['id', 'message']
        ref_name = 'mini_comment'


class EpisodeGETSerializer(serializers.ModelSerializer):
    comment_episode = MiniCommentSerializer(read_only=True, many=True)
    category = MiniCategorySerializer(read_only=True)
    tags = MiniTagSerializer(read_only=True, many=True)

    class Meta:
        model = Episode
        fields = ['id', 'title', 'category', 'image', 'music', 'tags', 'description', 'comment_episode',
                  'created_date']
        ref_name = 'salom'


class EpisodePOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ['id', 'title', 'category', 'image', 'music', 'tags', 'description', 'created_date']


class EpisodeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentEpisode
        fields = ['id', 'author', 'episode', 'message', 'created_date']

    def create(self, validated_data):
        request = self.context['request']
        episode_id = self.context['episode_id']
        author_id = request.user.profile_user.id
        message = validated_data.get('message')
        instance = CommentEpisode.objects.create(episode_id=episode_id, author_id=author_id, message=message)
        return instance


# class PlaylistPOSTSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Playlist
#         fields = ['id', 'episodes']


class PlayListEpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['episodes']


class MiniEpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ['id', 'title', 'music']


class PlaylistGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'author', 'title', 'episodes']

    episodes = MiniEpisodeSerializer(many=True)


class PlaylistRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'author', 'title', 'episodes']


class EpisodeLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeLike
        fields = ['author', 'episode']

    def create(self, validated_data):
        request = self.context['request']
        episode_id = self.context['episode_id']
        author_id = request.user.profile_user.id
        instance = EpisodeLike.objects.create(author_id=author_id, episode_id=episode_id)
        return instance
