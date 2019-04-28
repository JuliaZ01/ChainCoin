import redis
import zerorpc
import time
from decimal import *
# r = redis.StrictRedis(host='localhost', port=6379)
# r.publish('CreateKeypair', 'createaccount')
user = 'buQf5VAcYgWhJTp9Fywpu7W9KWfnUTK55MHt'
prkey = 'privbyrGtc3YaTLf4iWPU68Dwx83j8jjLvsoqAS3zbjVX5BcDvP7uYhE'
coins = 5
c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4343")

# kp = c.keypair()
# print(kp)
# address = kp[0:36]
# pbkey = kp[36:112]
# prkey = kp[112:]

# hash1 = c.createproject(user, coins, prkey)
# print(hash1)
# time.sleep(15)
# if type(hash1)== type('abc'):
# 	result = c.getcontractad(hash1)
# 	print(result)

# ad = 'buQgTbz6V9XUvcJ1iRSH9bwCBL7REQQb6fK4'
# pr = 'privby54uXkXxCv91Z6YP1Ax6b26EhsMeY2s2CzzbutP2RrwgpqeeckA'
# hash1 = c.settleweight(ad, pr)
# print(hash1)

#invest
# user = 'buQgTbz6V9XUvcJ1iRSH9bwCBL7REQQb6fK4'
# pr = 'privby54uXkXxCv91Z6YP1Ax6b26EhsMeY2s2CzzbutP2RrwgpqeeckA'
# cad = 'buQeWwePKNvJb34RETBFnGr7yNbxfJ6Zauu7'
# hash1 = c.investproject(user, pr, cad, 3)
# print(hash1)
#settle
# cad = 'buQeWwePKNvJb34RETBFnGr7yNbxfJ6Zauu7'
# hash1 = c.settleContract(cad)
# print(hash1)
# 
# # addmeta
# ad = 'buQYhiGqsUawbz47FW3vtN5zKtMYcgMZcCDn'
# pr = 'privbwj3dpQfkCdCq539prht19JPLpGHs9Er4gK1b5QqTJAaz7X1Jdqy'
# name = '志愿'
# detail = '养老院'
# hash1 = c.addVolunteer(ad, pr, name, detail)
# print(hash1)
# getbalance
address = 'buQYhiGqsUawbz47FW3vtN5zKtMYcgMZcCDn'

a = c.getBalance(address)
print (a)
num = Decimal(a)/100000000
print (num)
print (type(num))