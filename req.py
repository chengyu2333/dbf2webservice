from req_post import PostReq
from req_get import GetReq
from cache import Cache
import config
import requests

class Req(PostReq, GetReq):
    pass

    # def commit_data(self, data):
    #     id_cache = Cache("tmp/id_cache.txt")
    #     id = id_cache.get_value(data['hqzqdm'])
    #     if id:
    #         url = config.api_put.format(id=id)
    #         response = requests.get(url)
    #         if response.status_code == 200:
    #             print(response.text)
    #     else:
    #         # post and cache id
    #         pass



# Req().commit_data()