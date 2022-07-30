import pandas as pd
import numpy as np
from apyori import apriori
path =
df = pd.read_csv(path, header=None)
transactions = []
for i in range(0,7501):
    transactions.append([str(df.values[i,j]) for j in range(0,20)])

rules = apriori(transactions= transactions, min_support=0.003, min_confidence=0.2,min_lift=3,min_length= 2,max_length=2)

results = list(rules)

def inspect(rules):
    lhs = [tuple(result[2][0][0])[0] for result in results]
    rhs = [tuple(result[2][0][1])[0] for result in results]
    support = [result[1] for result in results]

    return list(zip(lhs,rhs,support))
resdf = pd.DataFrame(inspect(results), columns= ['left hand','right hand','Support'])

print(resdf.nlargest(n=10,columns='Support'))
