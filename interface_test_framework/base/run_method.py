import requests

class RunMethod:

    @classmethod
    def post_main(cls, url, data, headers=None):
        if headers:
            return requests.post(url=url, data=data, headers=headers)
        else:
            return requests.post(url=url, data=data)

    @classmethod
    def get_main(cls, url, data=None, headers=None):
        if data:
            url = url + '?' + data
        if headers:
            return requests.get(url, headers=headers)
        else:
            return requests.get(url)