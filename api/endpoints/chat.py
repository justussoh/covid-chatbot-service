from data.redisFetch import getFromRedis

class Chat:

    def on_post(self, request, response):
        data = request.media
        query_result = data['queryResult']
        intent = query_result['intent']['displayName']
        fulfillment_message = get_fulfillment_message(intent)
        reply = {
            "fulfillmentText": fulfillment_message,
            "payload": {
                "facebook": {
                    "text": fulfillment_message
                }
            }
        }
        response.media = reply


def get_fulfillment_message(intent_name):
    if intent_name == "Virus Situation - Total Worldwide Cases":
        return "There are currently {} cases worldwide".format(123) # replace 123 with getFromRedis(location, field): REFER TO REDIS FILE FOR BREAK DOWN OF AVAIL FIELDS
    return "No query found"
