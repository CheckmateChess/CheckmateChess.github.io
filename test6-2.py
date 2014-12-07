from Checkmate import Checkmate
from socket import *
from Test import Test
from json import *

test = Test()

s1 = socket(AF_INET, SOCK_STREAM)
s1.connect(("0.0.0.0", 20001))

data = test.send(s1, '{"op":"start","params":["single","easy","None"]}')
data = loads(data)
gameid = data['gameid']

test.send(s1, '{"op":"play","params":["setdepth","1"]}')
test.send(s1, '{"op":"play","params":["nextmove","%s","%s"]}' % ('White', 'a4'))

test.send(s1, '{"op":"exit"}')


s1 = socket(AF_INET, SOCK_STREAM)
s1.connect(("0.0.0.0", 20001))

test.send(s1, '{"op":"connect" ,"gameid":"%d"}' % gameid)
test.send(s1, '{"op":"play","params":["getboard"]}')
