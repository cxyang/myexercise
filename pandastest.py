import pandas as pd

sdata = {
    'Ohio':35000,
    'Texas':71000,
    'Oregon':16000,
    'Utah':5000
}
states = ['California', 'Ohio', 'Oregon', 'Texas']

obj3 = pd.Series(sdata)
obj4 = pd.Series(sdata, index=states)

obj4.name = 'poopulation'
obj4.index.name = 'state'

#print(obj4)
#print(obj3+obj4)

data = {'state':['Ohio','Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year':[2000, 2001, 2002, 2001, 2002, 2003],
        'pop':[1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data, index=['one', 'two', 'three', 'four', 'five', 'six'] ,columns=['year', 'state', 'pop','tee'])

print(frame['state'])
