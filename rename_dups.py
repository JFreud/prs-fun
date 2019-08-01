import numpy as np
import pandas as pd



def rename_dups(filename):
    tb = pd.read_table(filename, delim_whitespace = True, header = None, low_memory=False) #low_memory deprecated, just get rid of the error emssage
    tb = tb.rename(columns={tb.columns[1]:"id"})
    #tb['id'] = tb['id'].where((~tb['id'].duplicated()) & (~(tb['id'] == ".")), tb['id'] + "_dp")
    tb['id'] = tb['id'].where(~tb['id'].duplicated(), tb['id'] + "_dp")
    tb = tb.replace("._dp", ".") # this is super inefficient but I couldnt get it to work in the where method
    tb.to_csv("1kg_phase1_all.bim", header=None, index=None, sep='\t', mode='w')


def check_dups(filename):
    fp = open(filename, "r")
    #for line in iter(fp.readline, ''):
    for line in fp:
        line_tok = line.split()
        rs = line_tok[1]
        if "dup" in rs:
            print(rs)
    fp.close()

if __name__ == '__main__':
    #rename_dups("1kg_phase1_all_old.bim")
    check_dups("1kg_phase1_all.bim")
