from rest_framework import serializers
from ..models import Episode, EpisodeComment, Playlist, Playmusic, EpisodeLike
from apps.main.v1.serializers import MiniCategorySerializer, MiniTagSerializer


class MiniEpisodeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeComment
        fields = ['author', 'message']


class EpisodeGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ['id', 'author', 'title', 'category', 'image', 'music', 'tags', 'description', 'comment_episode',
                  'created_date']

    category = MiniCategorySerializer(read_only=True)
    tags = MiniTagSerializer(read_only=True, many=True)
    comment_episode = MiniEpisodeCommentSerializer(read_only=True, many=True)


class EpisodePOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ['id', 'author', 'title', 'category', 'image', 'music', 'tags', 'description', 'created_date']


class EpisodeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeComment
        fields = ['id', 'author', 'episode', 'message']

    def create(self, validated_data):
        request = self.context['request']
        episode_id = self.context['episode_id']
        author_id = request.user.profile_user.id
        message = validated_data.get('message')
        instance = EpisodeComment.objects.create(episode_id=episode_id, author_id=author_id, message=message)
        return instance


class MiniEpisodelikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ['music']


class MiniEpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playmusic
        fields = ['title']

    title = serializers.CharField(source='episode.title')


class PlaylistGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'author', 'title', 'playmusic_set', 'create_date']

    playmusic_set = MiniEpisodeSerializer(read_only=True, many=True)


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'author', 'title', 'create_date']

    def create(self, validated_data):
        request = self.context['request']
        author_id = request.user.profile_user.id
        title = validated_data.get('title')
        instance = Playlist.objects.create(author_id=author_id, title=title)
        return instance


class PlaymusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playmusic
        fields = ['id', 'play_list', 'episode', 'create_date']
        extra_kwargs = {
            'play_list': {'required': False},
            'episode': {'required': False},
        }

    # def create(self, validated_data):
    #     request = self.context['request']
    #     play_list_id = self.context['play_list_id']
    #     episode = validated_data.get('episode')
    #     instance = Playmusic.objects.create(play_list_id=play_list_id, episode=episode)
    #     return instance


class PlaylistDesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'author', 'title', 'create_date']

    def create(self, validated_data):
        request = self.context['request']
        play_list_id = self.context['play_list_id']
        instance = Playmusic.objects.create(play_list_id=play_list_id)
        return instance


class LikeGETSerializer(serializers.ModelSerializer):
    episode = MiniEpisodelikeSerializer(read_only=True)

    class Meta:
        model = EpisodeLike
        fields = ['id', 'episode']


class LikePOSTSerilazer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeLike
        fields = ['id', 'author', 'episode']
        extra_kwargs = {
            'author': {'required': False},
            'episode': {'required': False},
        }
