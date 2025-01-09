import requests
import configuration
import data

# Создание нового заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body)
response = post_new_order(data.order_body)
print(response.status_code)
print(response.json())

# Сохранение трека заказа
def save_track():
    response = post_new_order(data.order_body)
    return response.json()['track']
print(response.json()['track'])

#Выполнение запроса на получения заказа по треку заказа
def get_order_by_track():
    track = save_track()
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_BY_TRACK + str(track))
response = get_order_by_track()
print(response.status_code)
print(response.json())