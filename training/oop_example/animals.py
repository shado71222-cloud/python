from training.oop_example.doggos import doggos
from training.oop_example.cattos import cattos

class Animal:
    dog1=doggos("jully",6)
    dog2=doggos("perry",9)
    cat1=cattos("gingy",12)
    dog1.awuf()
    dog2.awuf()
    cat1.meow()
    dog1.calc_distance(12,10)