import json

from . import models


ignore_fields = [
    'id_str',
    'in_reply_to_status_id_str',
    'in_reply_to_user_id_str',
    'symbols'
]

one_to_many = {
    'hashtags': models.Hashtag,
    'urls': models.Url,
    'media': models.Media,
    'sizes': models.Size,
    'user_mentions': models.UserMention,
}

one_to_one = {
    'user': models.User,
    'tweet': models.Tweet
}


def import_multiple(lst, model):
    for item in lst:
        import_single(item, model)


def import_single(dictionary, model):
    m = model()
    for field, value in dictionary.items():
        if field in ignore_fields:
            continue
        if field == 'entities':
            for entity_name, entity_list in dictionary['entities'].items():
                import_multiple(entity_list, one_to_many[entity_name])
        if field in one_to_many:
            import_multiple(value, one_to_many[field])
        else:
            setattr(model, field, value)


with open("tweets.json", 'r') as tweets_file:
    tweet_data = json.loads(tweets_file)
    for tweet_datum in tweet_data:
        import_single(tweet_data, models.Tweet)
