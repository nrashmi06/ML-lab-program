import pandas as pd 
#file = "C:\Users\rashm\Downloads\data.csv"
data = pd.read_csv("C:\\Users\\rashm\\Downloads\\data.csv")

hypothesis = ['%' for _ in range(len(data.columns) - 1)]

positive = data[data['enjoy sport'] == 'Yes'].iloc[:,:-1].values.tolist()
for e in positive : 
    for i in range (len(e)):
        if hypothesis[i] !='%'and hypothesis[i] != e[i]:
            hypothesis[i] ='?'
            print(hypothesis)
        else:
            hypothesis[i] = e[i]
            
print("the maximally specific Fins S hypothesis for the given training example is :")
print(hypothesis)
