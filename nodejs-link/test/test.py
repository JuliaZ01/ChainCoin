import redis
import zerorpc
import time
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
user = 'buQgTbz6V9XUvcJ1iRSH9bwCBL7REQQb6fK4'
pr = 'privby54uXkXxCv91Z6YP1Ax6b26EhsMeY2s2CzzbutP2RrwgpqeeckA'
cad = 'buQeWwePKNvJb34RETBFnGr7yNbxfJ6Zauu7'
hash1 = c.investproject(user, pr, cad, 3)
print(hash1)
#settle
# cad = 'buQeWwePKNvJb34RETBFnGr7yNbxfJ6Zauu7'
# hash1 = c.settleContract(cad)
# print(hash1)