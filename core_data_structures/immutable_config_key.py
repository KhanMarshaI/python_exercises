# Immutable Config Key
# Build a frozenset of (host, port, protocol) triples and use it as keys in a dict that stores timeout values.

import random

triples  = [("10.0.0.1", 22, "TCP"), ("10.0.0.1", 53, "UDP"), ("10.0.0.2", 80, "TCP")]

triplesFrozenset = frozenset(triples)

timeoutDict = dict()

for i in triplesFrozenset:
    timeoutDict.update({i:random.randint(1,30)})

print(timeoutDict)