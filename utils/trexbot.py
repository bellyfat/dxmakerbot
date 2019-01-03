#!/usr/bin/env python3
__author__ = "atcsecure"
__copyright__ = "All rights reserved"
__credits__ = ["atcsecure"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "atcsecure"
__status__ = "Alpha"

import json
import time
from bittrex.bittrex import Bittrex, API_V2_0

my_bittrex = Bittrex(None, None)

def getmarketprice(marketname):
  # get market price
  markets = []
  markets = marketname.split('-')
  print (marketname)
  if markets[1] == 'BTC':
    print ('split')
    marketname = '{0}-{1}'.format(markets[1], markets[0])
    print (marketname)
  summary = my_bittrex.get_market_summary(marketname)
  for attempt in range(0,5):
      try:
        lastprice = summary['result'][0]['Last'] 
      except Exception as e:
        print('API call attempt# {2} - exception/error {0}, bittrex called failed for {1}'.format(e, marketname, attempt))
        print(summary)
        time.sleep(2.5)
        lastprice = 0
        continue
      break
  return lastprice

def getpricedata(maker, taker):
  basemarket = ('BTC-{0}'.format(maker))
  takermarket = ('BTC-{0}'.format(taker))
  print ('maker: {0}, taker: {1}'.format(maker,taker))
  print ('basemarket: %s' % basemarket)
  if maker == 'BTC':
    marketprice = 1/getmarketprice(takermarket)
    return marketprice
  makerprice = getmarketprice(basemarket)
  print ('takermarket: %s' % takermarket)
  if taker == 'BTC':
    marketprice = makerprice
  else:
    takerprice = getmarketprice(takermarket)
    try:
      marketprice = makerprice / takerprice
    except:
      marketprice = 0

  return marketprice


# vim: tabstop=2 expandtab shiftwidth=2 softtabstop=2
