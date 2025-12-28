import requests
import pytest

def create_item():

    body = {
  "sellerID": 291324,
  "name": "Toyota Carina",
  "price": 25000,
  "statistics": {
    "likes": 1,
    "viewCount": 10,
    "contacts": 3
  }
}
    response = requests.post(url='https://qa-internship.avito.com/api/1/item', json = body)

    return response

def create_item_without_name():

    body = {
  "sellerID": 291324,
  "price": 25000,
  "statistics": {
    "likes": 1,
    "viewCount": 10,
    "contacts": 3
  }
}
    response = requests.post(url='https://qa-internship.avito.com/api/1/item', json = body)

    return response

def create_item_with_invalid_sellerID_type():

    body = {
  "sellerID": '291324',
  "price": 25000,
  "statistics": {
    "likes": 1,
    "viewCount": 10,
    "contacts": 3
  }
}
    response = requests.post(url='https://qa-internship.avito.com/api/1/item', json = body)

    return response

def create_item_without_body():

    body = {}

    response = requests.post(url='https://qa-internship.avito.com/api/1/item', json = body)

    return response

def get_item_by_id(item_uuid):

    response = requests.get(url=f'https://qa-internship.avito.com/api/1/item/{item_uuid}')

    return response

def get_statistic_by_item_id(item_uuid):

    response = requests.get(url=f'https://qa-internship.avito.com/api/1/statistic/{item_uuid}')

    return response

def get_items_by_sellerID(sellerID):

    response = requests.get(url=f'https://qa-internship.avito.com/api/1/{sellerID}/item')

    return response
