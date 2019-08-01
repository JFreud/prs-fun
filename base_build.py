import numpy as np
import pandas as pd

def get_weights(filename, hd, cols, tolog):
    weights = pd.read_csv(filename, header=hd, usecols=cols)
    weights = weights.dropna()
    weights[tolog]= weights[tolog].apply(np.log)
    return weights






if __name__ == '__main__':
    weights = get_weights("weights.csv", 1, [0,4,12], "OR.2")
    weights = weights.rename(columns={weights.columns[1]:"Allele"})
    weights.Allele = weights.Allele.str[2:] #format data to only have major allele
    print(weights)
    weights.to_csv("myprofile.raw", header=None, index=None, sep=' ', mode='w')
