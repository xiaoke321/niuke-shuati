

class A(object):
    pass

class B(A):
    pass


b = B()


if __name__ == '__main__':
    print(isinstance(b, object))
    print(issubclass(b, B))