import pandas as pd
import numpy as np

file1 ="data.csv"

data = pd.DataFrame(data = pd.read_csv(file1))
print(data)

concepts = np.array(data.iloc[:,:-1])
print(concepts)

target = np.array(data.iloc[:,-1])
print(target)

def learn (concepts,target):
    sh = concepts[0].copy()
    print("\nInitialization of specific and general hypothesis : ")
    print(sh)
    gh=[['?'for i in range(len(sh))]for i in range(len(sh))]
    print(gh)
    print('\n')
    for i,h in enumerate(concepts):
        if target[i] == 'Yes':
            for x in range(len(sh)):
                if(h[x] != sh[x]):
                    sh[x] ='?'
                    gh[x][x] = '?'
        if target[i] =='No':
           for x in range(len(sh)):
                if h[x] != sh[x] :
                    gh[x][x] = sh[x]
                else:
                    gh[x][x] = '?'
        print("\nSteps of candidate elimination algorithm ",i+1)
        print(sh)
        print(gh)
        
    ind = [i for i,val in enumerate(gh)if val ==['?','?','?','?','?','?']]
        
    for i in ind:
            gh.remove(['?','?','?','?','?','?'])
    return sh,gh
    
        
s_final,g_final = learn(concepts,target)
print("final sh :,",s_final,sep="\n")
print("final gh :,",g_final,sep="\n")





