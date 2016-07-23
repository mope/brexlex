from django.db import models


# IDs are different
# ID strings aren't used
# in_reply_to_status_id_str not used

class User(models.Model):
    user_id = models.BigIntegerField()
    name = models.CharField()
    screen_name = models.CharField()
    location = models.CharField()
    url = models.URLField()
    description = models.CharField(max_length=511)
    protected = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    followers_count = models.IntegerField()
    friends_count = models.IntegerField()
    listed_count = models.IntegerField()
    favourites_count = models.IntegerField()
    statuses_count = models.IntegerField()
    created_at = models.DateTimeField()
    time_zone = models.CharField()
    geo_enabled = models.BooleanField()
    contributors_enabled = models.BooleanField()
    is_translator = models.BooleanField()
    profile_background_color = models.CharField()
    profile_background_image_url = models.URLField()
    profile_background_image_url_https = models.URLField()
    profile_background_tile = models.BooleanField()
    profile_background_link_color = models.CharField()
    profile_sidebar_border_color = models.CharField()
    profile_sidebar_fill_color = models.CharField()
    profile_text_color = models.CharField()
    profile_use_background_image = models.BooleanField()
    profile_image_url = models.URLField()
    profile_image_url_https = models.URLField()
    default_profile = models.BooleanField()
    default_profile_image = models.BooleanField()
    following = models.CharField()
    follow_request_sent = models.CharField()
    notifications = models.CharField()


class Hashtag(models.Model):
    tweet = models.ForeignKey(
        'core.Tweet',
        on_delete=models.CASCADE,
        related_name='hashtags'
    )
    text = models.CharField(max_length=255)
    index_1 = models.IntegerField(required=False)
    index_2 = models.IntegerField(required=False)


class Url(models.Model):
    tweet = models.ForeignKey(
        'core.Tweet',
        on_delete=models.CASCADE,
        related_name='urls'
    )
    url = models.URLField()
    expanded_url = models.URLField()
    display_url = models.URLField()
    index_1 = models.IntegerField(required=False)
    index_2 = models.IntegerField(required=False)


class MediaSize(models.Model):
    media = models.ForeignKey(
        'core.Tweet',
        on_delete=models.CASCADE,
        related_name='sizes'
    )
    name = models.CharField()
    w = models.IntegerField()
    h = models.IntegerField()
    resize = models.CharField()


class Media(models.Model):
    tweet = models.ForeignKey(
        'core.Tweet',
        on_delete=models.CASCADE,
        related_name='media'
    )
    media_id = models.BigIntegerField()
    index_1 = models.IntegerField(required=False)
    index_2 = models.IntegerField(required=False)
    media_url = models.URLField()
    media_url_https = models.URLField()
    url = models.URLField()
    display_url = models.URLField()
    extended_url = models.URLField()
    type = models.CharField()


class Tweet(models.Model):
    created_at = models.DateTimeField()
    tweet_id = models.BigIntegerField()
    text = models.CharField()
    source = models.CharField()
    truncated = models.BooleanField(default=False)
    in_reply_to_status_id = models.BigIntegerField(required=False)
    in_reply_to_user_id = models.BigIntegerField(required=False)
    in_reply_to_screen_name = models.CharField(required=False)
    user = models.ForeignKey(
        'core.User',
        on_delete=models.CASCADE,
        related_name='tweets'
    )
    geo = models.CharField(required=False)
    coordinates = models.CharField(required=False)
    place = models.CharField(required=False)
    contributors = models.CharField(required=False)
    retweeted_status = models.ForeignKey(
        'core.Tweet',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='retweets'
    )
    is_quote_status = models.BooleanField(default=False)
    quoted_status_id = models.BigIntegerField(required=False)
    quoted_status = models.ForeignKey(
        'core.Tweet',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='quotes'
    )
    retweet_count = models.IntegerField()
    favorite_count = models.IntegerField()
    favorited = models.BooleanField(default=False)
    retweeted = models.BooleanField(default=False)
    possibly_sensitive = models.BooleanField(default=False)
    filter_level = models.CharField(required=False)
    lang = models.CharField(required=False)
    timestamp_ms = models.CharField()
