# Python Tricks

`mylist = ['a'] * 6`

set's symmetric_difference, symmetric_difference_update

frozenset

`from timeit import default_timer as timer`

`from collections import Counter`

`from collections import namedtuple`

`from collections import OrderedDict`

`from collections import defaultdict`

`from collections import deque`

`from itertools import product`

`from itertools import permutations`

`from itertools import combinations, combinations_with_replacement`

`from itertools import accumulate`

`from itertools import groupby`

`from itertools import count, cycle, repeat`

`import operator`

`from functools import reduce`

```py
import json
person = {"name": "Brian", "age": "30"}
personJSON = json.dumps(person, indent=4, sort_keys=True)
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)
person2 = json.loads(personJson)
with open('person.json', 'r') as file:
    person = json.load(file)
```

`import secrets`

`sys.getsizeof(...)`

generator yield

`from multiprocessing import Process, Value, Array, Lock, Queue, Pool`

`from Threading import thread`

`from comntextlib import contextmanager`

@contextmanager
