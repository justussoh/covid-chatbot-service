from data.redisFetch import updateRedis, getFromRedis

class OK:

    def on_get(self, request, response):
        success = updateRedis()
        if (success) :
            print(getFromRedis('UK', 'Deaths'))
            response.media = getFromRedis('all', 'Deaths')
        else:
            response.media = {"status" : "not OK"}
            