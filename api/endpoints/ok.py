from data.redisFetch import updateRedis, getFromRedis

class OK:

    def on_get(self, request, response):
        success = updateRedis()
        if (success) :
            print(getFromRedis('UK', 'Deaths'))
            response.media = getFromRedis('all', 'Deaths').decode("utf-8")
        else:
            response.media = {"status" : "not OK"}
            