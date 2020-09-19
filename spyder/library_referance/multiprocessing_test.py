
# ::::: Simple Example ::::: #
# from multiprocessing import Pool

# def f(x):
#     return x*x

# if __name__ == '__main__':
#     with Pool(5) as p:
#         print(p.map(f, [1, 2, 3]))


# ::::: Getting CPU Count ::::: #
# import multiprocessing

# print('cpu_count:',multiprocessing.cpu_count())


# ::::: Process Class ::::: #
# from multiprocessing import Process

# def f(name):
#     print('hello', name)

# if __name__ == '__main__':
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()



