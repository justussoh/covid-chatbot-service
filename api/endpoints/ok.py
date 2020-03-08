from data.fetch_data import fetch_data


class OK:

    def on_get(self, request, response):
        response.media = fetch_data()
        # response.media = {'status': 'OK'}
