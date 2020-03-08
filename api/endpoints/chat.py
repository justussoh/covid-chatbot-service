class Chat:

    def on_post(self, request, response):
        data = request
        reply = dict()
        if data['queryResult']['queryText'] == 'yes':
            reply = {
                "fulfillmentText": "Ok. Tickets booked successfully.",
            }
        elif data['queryResult']['queryText'] == 'no':
            reply = {
                "fulfillmentText": "Ok. Booking cancelled.",
            }
        response.media = reply
