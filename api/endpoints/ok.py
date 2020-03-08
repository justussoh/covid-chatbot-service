class OK:

    def on_get(self, request, response):
        response.media = {'status': 'OK'}
