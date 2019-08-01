import pandas as pd
import numpy as np

def count_pop(filename, cols):
    pop_dict = dict()
    origins = pd.read_csv(filename, header=0, usecols=cols)
    pop_count = origins['Population'].value_counts().to_dict()
    for key in pop_count:
        pop_dict[key] = origins[origins['Population'] == key]['Sample'].values.tolist()
    return pop_dict

def score(filename, cols):
    scores = dict()
    pop_dict = count_pop("1000_genome_info.csv", [0,1])
    score_raw = pd.read_csv(filename,sep='\s+',header=0,usecols=cols)
    for key in pop_dict:
        num = len(score_raw[score_raw['IID'].isin(pop_dict[key])]['SCORE']) #this seems super inefficient but idk how pandas works
        if num == 0:
            num = 1
        score_total = score_raw[score_raw['IID'].isin(pop_dict[key])]['SCORE'].sum()
        scores[key] = score_total/num
    return scores



if __name__ == '__main__':
    score_avg = score("plink.profile", [1,5])
    print(score_avg)
