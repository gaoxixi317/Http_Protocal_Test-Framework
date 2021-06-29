from datetime import datetime
class Common:

    @classmethod
    def get_request_data_str(cls, request_data):
        # "cardno": "330326198903081211","key":"9db2cea46ad46bb9804a7b35ea663873"
        list_data = request_data.split(',')
        result = ''
        for data in list_data:
            result += data.replace(':', '=').replace('"', '')
            result += '&'
        return result[:-1]

    @classmethod
    def get_request_data_dict(cls, request_data):
        result = {}
        list_data = request_data.split(',')
        for data in list_data:
            key = data.split(':')[0].replace('"', '')
            value = data.split(':')[1].replace('"', '')
            result[key] = value
        return result

    @classmethod
    def get_current_time(cls):
        return datetime.now()

if __name__ == '__main__':
    print(Common.get_request_data_dict('"cardno":"330326198903081211","key":"9db2cea46ad46bb9804a7b35ea663873"'))
    print(Common.get_request_data_str('cardno:330326198903081211,key:9db2cea46ad46bb9804a7b35ea663873'))
