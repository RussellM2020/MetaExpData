import pickle
fobj = open("Returns_seed4.csv", "rb")
a = pickle.load(fobj)
print(a)

