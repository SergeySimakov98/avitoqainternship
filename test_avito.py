import pytest
import requests
from steps import create_item, create_item_without_name, create_item_with_invalid_sellerID_type, create_item_without_body, get_item_by_id, get_statistic_by_item_id, get_items_by_sellerID

def test_succes_create_item():

    response = create_item()

    assert response.status_code == 200
    assert 'Сохранили объявление' in response.text

def test_unsucces_create_item_without_required_field():

    response = create_item_without_name()

    assert response.status_code == 400
    assert response.json()['result']['message'] == 'поле name обязательно'

def test_unsucces_create_item_with_invalid_sellerID_type():

    response = create_item_with_invalid_sellerID_type()

    assert response.status_code == 400
    assert response.json()['status'] == 'не передано тело объявления'

def test_unsucces_create_item_without_body():

    response = create_item_without_body()

    assert response.status_code == 400
    assert response.json()['result']['message'] == 'поле name обязательно'

def test_get_item_by_id():

    response = get_item_by_id(item_uuid='a41a5034-9fd1-4965-903f-f23061fc216a')

    assert response.status_code == 200
    assert response.json()[0]['id'] == 'a41a5034-9fd1-4965-903f-f23061fc216a'

def test_get_item_with_invalid_id():

    response = get_item_by_id(item_uuid='8a25e9bc-2736-4eee-ab13-2e5964350c7d')

    assert response.status_code == 404
    assert response.json()['result']['message'] == 'item 8a25e9bc-2736-4eee-ab13-2e5964350c7d not found'

def test_get_item_with_invalid_id_type():

    response = get_item_by_id(item_uuid='1234567890')

    assert response.status_code == 400
    assert response.json()['result']['message'] == 'ID айтема не UUID: 1234567890'

def test_get_statistic_by_item_id():

    response = get_statistic_by_item_id(item_uuid='a41a5034-9fd1-4965-903f-f23061fc216a')

    assert response.status_code == 200
    assert response.json()[0]['contacts'] == 3
    assert response.json()[0]['likes'] == 1
    assert response.json()[0]['viewCount'] == 10

def test_get_statistic_with_invalid_id():

    response = get_statistic_by_item_id(item_uuid='8a25e9bc-2736-4eee-ab13-2e5964350c7d')

    assert response.status_code == 404
    assert response.json()['result']['message'] == 'statistic 8a25e9bc-2736-4eee-ab13-2e5964350c7d not found'

def test_get_statistics_with_invalid_id_type():

    response = get_statistic_by_item_id(item_uuid='1234567890')

    assert response.status_code == 400
    assert response.json()['result']['message'] == 'передан некорректный идентификатор объявления'

def test_get_items_by_sellerID():

    response = get_items_by_sellerID(sellerID='291324')

    assert response.status_code == 200
    items_list = response.json()
    test_pass_flag = False
    for item in items_list:
        if item['id'] == 'a00d6148-d9d2-47b2-8eda-5d32615a5181':
            test_pass_flag = True

    assert test_pass_flag == True

def test_get_items_by_sellerID_without_items():

    response = get_items_by_sellerID(sellerID='456230')

    assert response.status_code == 200
    assert response.json() == []

def test_get_items_by_sellerID_with_invalid_sellerID_type():

    response = get_items_by_sellerID(sellerID='456230invalid')

    assert response.status_code == 400
    assert response.json()['result']['message'] == 'передан некорректный идентификатор продавца'
