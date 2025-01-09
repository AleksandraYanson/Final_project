#Александра Янсон, 25А когорта - Финальный проект. Инженер по тестированию плюс

import sender_stand_request

# Автотест для проверки получения данных о заказе по треку
def test_get_order_by_track():
    order_by_track = sender_stand_request.get_order_by_track()
    assert order_by_track.json() != ""
    assert order_by_track.status_code == 200