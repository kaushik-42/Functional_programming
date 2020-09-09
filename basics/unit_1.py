What is Functional Programming?

>>> import collections
>>> scientist=collections.namedtuple('scientist',['name','field','born','nobel',])
>>> ada=scientist("ada","math",1254,False)
>>> ada.born
1254
>>> ada.name
'ada'
>>> ada['name']
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: tuple indices must be integers or slices, not str
>>> ada.name="Kaushik: ps cannot be updated"
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
AttributeError: can't set attribute
>>>
