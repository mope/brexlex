import json

from core import models


ignore_fields = [
    'id_str',
    'in_reply_to_status_id_str',
    'in_reply_to_user_id_str',
    'symbols'
]

model_identifiers = {
    'User': 'user_id',
    'Hashtag': 'text',
    'Url': 'url',
    'Media': 'tweet',
    'UserMention': 'user_mention_id',
    'Tweet': 'tweet_id'
}

twitter_object_identifiers = {
    'User': 'id',
    'Hashtag': 'text',
    'Url': 'url',
    'Media': 'tweet',
    'UserMention': 'id',
    'Tweet': 'id'
}

one_to_many = {
    'hashtags': models.Hashtag,
    'urls': models.Url,
    'media': models.Media,
    'sizes': models.Size,
    'user_mentions': models.UserMention,
}

one_to_one = {
    'user': models.User,
    'tweet': models.Tweet,
    'quoted_status': models.Tweet,
    'retweeted_status': models.Tweet,
}

id_fields = {
    'user': 'user_id',
    'media': 'media_id',
    'user_mentions': 'user_mention_id',
    'tweet': 'tweet_id'
}

def import_multiple(lst, model, foreign_key_value=None, foreign_key_field=None):
    for item in lst:
        import_single(item, model, foreign_key_value)


# How do you check if the model already exists?
# Import things in the right order

def import_single(dictionary, model, foreign_key_value=None, foreign_key_field=None):
    try:
        model.objects.get(**{identifiers[model.__name__]: dictionary[twitter_object_identifiers[model.__name__]]})
        return
    except (DoesNotExist, KeyError):
        continue
    m = model()
    for field, value in dictionary.items():
        if field in ignore_fields:
            continue
        elif field == 'entities':
            for entity_name, entity_list in dictionary['entities'].items():
                import_multiple(entity_list, one_to_many[entity_name])
        elif field in one_to_many:
            import_multiple(
                value,
                one_to_many[field],
                foreign_key_value=dictionary[id]
            )
        elif field in one_to_one:
            import_single(
                value,
                one_to_one[field],
                foreign_key_value=dictionary[id]
            )
        elif field == 'id':
            setattr(m, id_fields[model], value)
        else:
            setattr(m, field, value)
    m.save()


with open("tweets.json", 'r') as tweets_file:
    tweet_data = json.loads(tweets_file.read())
    line = 1
    for tweet_datum in tweet_data:
        print(line)
        line = line + 1
        import_single(tweet_datum, models.Tweet)
