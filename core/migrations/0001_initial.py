# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-23 13:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('index_1', models.IntegerField(blank=True, null=True)),
                ('index_2', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_id', models.BigIntegerField()),
                ('index_1', models.IntegerField(blank=True, null=True)),
                ('index_2', models.IntegerField(blank=True, null=True)),
                ('media_url', models.URLField()),
                ('media_url_https', models.URLField()),
                ('url', models.URLField()),
                ('display_url', models.URLField()),
                ('extended_url', models.URLField()),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('w', models.IntegerField()),
                ('h', models.IntegerField()),
                ('resize', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('tweet_id', models.BigIntegerField()),
                ('text', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=255)),
                ('truncated', models.BooleanField(default=False)),
                ('in_reply_to_status_id', models.BigIntegerField(blank=True, null=True)),
                ('in_reply_to_user_id', models.BigIntegerField(blank=True, null=True)),
                ('in_reply_to_screen_name', models.CharField(blank=True, max_length=255, null=True)),
                ('geo', models.CharField(blank=True, max_length=255, null=True)),
                ('coordinates', models.CharField(blank=True, max_length=255, null=True)),
                ('place', models.CharField(blank=True, max_length=255, null=True)),
                ('contributors', models.CharField(blank=True, max_length=255, null=True)),
                ('is_quote_status', models.BooleanField(default=False)),
                ('quoted_status_twitter_id', models.BigIntegerField(blank=True, null=True)),
                ('retweet_count', models.IntegerField()),
                ('favorite_count', models.IntegerField()),
                ('favorited', models.BooleanField(default=False)),
                ('retweeted', models.BooleanField(default=False)),
                ('possibly_sensitive', models.BooleanField(default=False)),
                ('filter_level', models.CharField(blank=True, max_length=255, null=True)),
                ('lang', models.CharField(blank=True, max_length=255, null=True)),
                ('timestamp_ms', models.CharField(blank=True, max_length=255, null=True)),
                ('quoted_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quotes', to='core.Tweet')),
                ('retweeted_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='retweets', to='core.Tweet')),
            ],
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('expanded_url', models.URLField()),
                ('display_url', models.URLField()),
                ('index_1', models.IntegerField(blank=True, null=True)),
                ('index_2', models.IntegerField(blank=True, null=True)),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='urls', to='core.Tweet')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('screen_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('description', models.CharField(max_length=511)),
                ('protected', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('followers_count', models.IntegerField()),
                ('friends_count', models.IntegerField()),
                ('listed_count', models.IntegerField()),
                ('favourites_count', models.IntegerField()),
                ('statuses_count', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('time_zone', models.CharField(max_length=255)),
                ('geo_enabled', models.BooleanField()),
                ('contributors_enabled', models.BooleanField()),
                ('is_translator', models.BooleanField()),
                ('profile_background_color', models.CharField(max_length=255)),
                ('profile_background_image_url', models.URLField()),
                ('profile_background_image_url_https', models.URLField()),
                ('profile_background_tile', models.BooleanField()),
                ('profile_background_link_color', models.CharField(max_length=255)),
                ('profile_sidebar_border_color', models.CharField(max_length=255)),
                ('profile_sidebar_fill_color', models.CharField(max_length=255)),
                ('profile_text_color', models.CharField(max_length=255)),
                ('profile_use_background_image', models.BooleanField()),
                ('profile_image_url', models.URLField()),
                ('profile_image_url_https', models.URLField()),
                ('default_profile', models.BooleanField()),
                ('default_profile_image', models.BooleanField()),
                ('following', models.CharField(max_length=255)),
                ('follow_request_sent', models.CharField(max_length=255)),
                ('notifications', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserMention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_name', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('mention_id', models.BigIntegerField()),
                ('index_1', models.IntegerField(blank=True, null=True)),
                ('index_2', models.IntegerField(blank=True, null=True)),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentions', to='core.Tweet')),
            ],
        ),
        migrations.AddField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweets', to='core.User'),
        ),
        migrations.AddField(
            model_name='size',
            name='media',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='core.Tweet'),
        ),
        migrations.AddField(
            model_name='media',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='core.Tweet'),
        ),
        migrations.AddField(
            model_name='hashtag',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hashtags', to='core.Tweet'),
        ),
    ]