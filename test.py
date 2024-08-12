import pandas as pd

data = pd.DataFrame(range(100),columns=["sayilar",])
print(data)



clData = data[~((data["sayilar"]<5) | (data["sayilar"]>90))]
print(clData)