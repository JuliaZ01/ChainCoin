import redis
import zerorpc
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
# print(type(hash1))
# print(type(hash1)== type('abc'))


result = c.getcontractad('d7d27196ef98a7606a15c0361144d1c58f30c90fabaf822249386dfb4429a823')
print(result[0]['contract_address'])

