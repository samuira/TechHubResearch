import copy


class A(object):
    def __init__(self):
        self.a = {"a": [2,4]}


class B(object):
    def __init__(self):
        self.a1 = A()


class C(object):
    def __init__(self):
        self.a2 = B()


if __name__ == '__main__':

    c = C()
    c_r = c

    c_s = copy.copy(c)
    c_d = copy.deepcopy(c)

    # modifying referance
    print('modifying reference')
    c_r.a2.a1.a['a'][0] = 'reference'
    print('reference', id(c_r.a2),'shallow', id(c_s.a2), 'deep', id(c_d.a2))
    print(c.a2.a1.a, c_r.a2.a1.a, c_s.a2.a1.a, c_d.a2.a1.a)

    # modifying shallow
    print('modifying shallow')
    c_s.a2.a1.a['a'][0] = 'shallow'
    print('reference', id(c_r.a2), 'shallow', id(c_s.a2), 'deep', id(c_d.a2))
    print(c.a2.a1.a, c_r.a2.a1.a, c_s.a2.a1.a, c_d.a2.a1.a)

    # modifying deep
    print('modifying deep')
    c_d.a2.a1.a['a'][0] = 'deep'
    print('reference', id(c_r.a2), 'shallow', id(c_s.a2), 'deep', id(c_d.a2))
    print(c.a2.a1.a, c_r.a2.a1.a, c_s.a2.a1.a, c_d.a2.a1.a)

    # difference between referencing and shallow copy
    """
    when we introduce a new element or a new member or an object in shallow copying and deep copy object, the changes will not 
    reflect in original copy. but if we introduce a new element or a new member or an object in reference, the changes
    will reflect in original object.
    """
    print('difference between referencing and shallow copy')
    print('new member introduce in shallow copy')
    c_s.a3 = A() # introducing a new object in shallow copy.
    print('shallow:',c_s.a3.a) # this a3 object is only in shallow copy
    try:
        print('original:',c.a3.a) # this will give us an error. as a3 is only introduce in shallow copy.
    except Exception as e:
        print('original',e)

    print('new member introduce in reference')
    c_r.a4 = A() # introducing a new object in reference.
    print('reference:',c_r.a4.a) # this a4 object is introduce in reference as well as in original object.
    print('original:',c.a4.a) # this will not give us any error. because changes has been made in reference will reflect in original object

    print('new member introduce in deep copy')
    c_d.a5 = A()  # introducing a new object in deep copy.
    print('deep:',c_d.a5.a)  # this a5 object is only in deep copy
    try:
        print('original:',c.a5.a)  # this will give us an error. as a5 is only introduce in shallow copy.
    except Exception as e:
        print('original:',e)
    print('--------------------------------------')





    c = C()
    b = 2
    obj = [c, b]
    c_r = obj
    c_s = copy.copy(obj)
    c_d = copy.deepcopy(obj)
    print(id(c_r[0]), id(c_s[0]), id(c_d[0]))