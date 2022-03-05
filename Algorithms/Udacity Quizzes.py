import numpy as np
import pandas as pd


print(np.mean([4, -12, 10, 4, 10, 2, -11, 23, 12]))


class Base:
    def __init__(self, i = 0):
        self.i = i

class Derived(Base):
    def __init__(self, j = 0):
        super().__init__(10)
        self.j = j

def main():
    d = Derived()
    print(d.i)
    print(d.j)
    
if __name__ == "__main__":
    main()



X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(X[-1, :].sum())


array_1 = np.array([[1, 2, 7], [3, 4, 8]])
array_2 = np.array([[1, 2], [3, 9], [4, 16]])
print(np.dot(array_1, array_2))


numbersData = {
    'one': [1, 1, 1, 1, 1, 1],
    'two': [1, 2, 3, 4, 5, 6],
    'three': [1, 1, 1, 3, 3, 3] }

df = pd.DataFrame(numbersData)

print(df['two'].map(lambda x: x>= np.mean(df['three'])))

print(df['two'][df['two'] >= df['three'].mean()])
