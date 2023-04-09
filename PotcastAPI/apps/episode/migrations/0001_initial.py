# Generated by Django 4.2 on 2023-04-08 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profil', '0001_initial'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=202)),
                ('image', models.ImageField(blank=True, null=True, upload_to='episode/')),
                ('music', models.FileField(blank=True, null=True, upload_to='music/')),
                ('description', models.TextField()),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profil.profile')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_episode', to='main.category')),
                ('tags', models.ManyToManyField(related_name='tag_episode', to='main.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=202)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profil.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Playmusic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episode', to='episode.episode')),
                ('play_list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='episode.playlist')),
            ],
        ),
        migrations.CreateModel(
            name='EpisodeLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profil.profile')),
                ('episode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='episodelike', to='episode.episode')),
            ],
        ),
        migrations.CreateModel(
            name='EpisodeComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profil.profile')),
                ('episode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_episode', to='episode.episode')),
            ],
        ),
    ]
