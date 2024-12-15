import requests
import configuration
import data

def post_new_order(body=data.order_body):

    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

    return response
def get_order(track):

    response = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                            params={"t": track})
    return response
