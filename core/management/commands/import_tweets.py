import json

from core import models


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

id_fields = {
    'user': 'user_id',
    'media': 'media_id',
    'user_mentions': 'user_mention_id',
    'tweet': 'tweet_id'
}

def import_multiple(lst, model, foreign_key_value=None):
    return [import_single(item, model, foreign_key_value) for item in lst]


# How do you check if the model already exists?

def import_single(dictionary, model, foreign_key_value=None):
    print(model)
    m = model()
    child_models = []
    for field, value in dictionary.items():
        if field in ignore_fields:
            continue
        elif field == 'entities':
            for entity_name, entity_list in dictionary['entities'].items():
                child_models.extend(import_multiple(entity_list, one_to_many[entity_name]))
        elif field in one_to_many:
            child_models.extend(import_multiple(value, one_to_many[field], foreign_key_value=dictionary[id]))
        elif field == 'id':
            settatr(m, id_fields[model], value)
        else:
            setattr(m, field, value)
    #m.save()
    for child_models in child_model:
        child_model.save()
    return m


with open("tweets.json", 'r') as tweets_file:
    tweet_data = json.loads(tweets_file.read())
    line = 1
    for tweet_datum in tweet_data:
        print(line)
        line = line + 1
        import_single(tweet_datum, models.Tweet)
