import unittest
from client import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    stock_one_price = (quotes[0]['top_ask']['price'] + quotes[0]['top_bid']['price']) / 2
    stock_second_price = (quotes[1]['top_ask']['price'] + quotes[1]['top_bid']['price']) / 2
    # print stock_one_price
    # print stock_second_price

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # Same as above as the price of the stock is the average

    stock_one_price = (quotes[0]['top_ask']['price'] + quotes[0]['top_bid']['price']) / 2
    stock_second_price = (quotes[1]['top_ask']['price'] + quotes[1]['top_bid']['price']) / 2
    # print stock_one_price
    # print stock_second_price

  """ ------------ Add more unit tests ------------ """

  def test_getRatio_calculateRatio(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    stock_one_price = (quotes[0]['top_ask']['price'] + quotes[0]['top_bid']['price']) / 2
    stock_second_price = (quotes[1]['top_ask']['price'] + quotes[1]['top_bid']['price']) / 2
    ratio = stock_one_price/stock_second_price
    # print ratio

  def test_getRatio_SecondStockZero(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    stock_one_price = (quotes[0]['top_ask']['price'] + quotes[0]['top_bid']['price']) / 2
    # print stock_one_price
    stock_second_price = (quotes[1]['top_ask']['price'] + quotes[1]['top_bid']['price']) / 2
    # print stock_second_price
    if stock_one_price or stock_second_price == 0:
      print("Error: One stock is priced at 0")
    else:
      ratio = stock_one_price / stock_second_price
      # print ratio


if __name__ == '__main__':
    unittest.main()

