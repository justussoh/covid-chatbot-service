from data.redisFetch import getFromRedis

class Chat:

    def on_post(self, request, response):
        data = request.media
        query_result = data['queryResult']
        intent = query_result['intent']['displayName']
        reply = get_fulfillment(intent)
        response.media = reply


def get_fulfillment(intent):
    response = get_fulfillment_message(intent)
    if response['type'] == 'text':
        return _simple_message_response(response['content'])
    elif response['type'] == 'url':
        return _url_message_response(response['content'])
    return _simple_message_response("Sorry can you say that again!")


def get_fulfillment_message(intent_name):
    response = dict()
    if intent_name == "Virus Situation - Total Worldwide Cases":
        response['type'] = "text"
        response['content'] = "There are currently {} cases worldwide".format(123)
    elif intent_name == "Best Practices":
        response['type'] = "url"
        response['content'] = {
            'url': 'https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public',
            'text': 'WHO recommends the following practices',
            'button_text': 'View Details',
            'title': 'Coronavirus disease (COVID-19) advice for the public',
            'subtitle': 'Basic protective measures against the new coronavirus',
            'image_url': 'https://www.who.int/images/default-source/health-topics/coronavirus/social-media-squares/blue-1.tmb-1024v.png?sfvrsn=3d15aa1c_1',
        }
    return response


def _simple_message_response(text):
    reply = {
        "fulfillmentText": text,
        "payload": {
            "facebook": {
                "text": text
            }
        }
    }
    return reply


def _url_message_response(context):
    reply = {'fulfillmentMessages': [{
        'payload': {
            "facebook": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [
                            {
                                "title": context["title"],
                                "image_url": context['image_url'],
                                "subtitle": context['subtitle'],
                                "default_action": {
                                    "type": "web_url",
                                    "url": context['url'],
                                    "webview_height_ratio": "tall",
                                },
                                "buttons": [
                                    {
                                        "type": "web_url",
                                        "url": context['url'],
                                        "title": context['button_text']
                                    }
                                ]
                            }
                        ]
                    }
                }
            }
        }
    }]
    }
    return reply

