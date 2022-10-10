import setup_processing as sp
from itertools import combinations_with_replacement
import csv


# create combinations

def dict_combinations(sample_list, sample_seq):
    # create dictionary
    final_dict = {}
    for k in sample_seq:
        final_dict.update({str(k):[]})
        
    # create all combinations in list of tuples 
    list_combinations = list()
    for n in sample_seq:
        list_combinations += list(combinations_with_replacement(sample_list, n))

    # append combinations in correct key of dictionary order
    for comb in list_combinations:
        result = ''
        for i in comb:
            result += i
        for j in sample_seq:
            if len(result) == j:
                final_dict[str(j)].append(result)
                
    return final_dict


if __name__ == "__main__":
    sample_list = sp.LIST_LETTERS
    sample_seq = sp.LIST_SEQ
    
    final_dict = dict_combinations(sample_list, sample_seq)
    
    
    # Read csv data
    with open('../data/train.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        
    # create new head
    head = data[0]
    head_letters = []
    head_order = []
    for i in sample_seq:
        for h in final_dict[f'{i}']:
            head_letters.append(h)
        for j in range(1,401):
            head_order.append(f'{i}_l_{j}')
            
    #print(head)
    row = data[1]
    protein = row[1]
    
    #for position calculate array
    #print(protein)
    
    print(protein)
    
    position_result = {}
    count_result = {}
    for k in sample_seq:
        position_result.update({str(k):[]})
    
    # run positions
    for position in range(0,len(protein)):
        # position by seq
        for seq in sample_seq:
            # if it is not a invalid seq
            if len(protein[position:(position+seq)]) == seq:
                if protein[position:(position+seq)] in count_result:
                    count_result[f'{protein[position:(position+seq)]}'] += 1
                else:
                    count_result.update({protein[position:(position+seq)]:1})
                position_result[str(seq)].append(protein[position:(position+seq)])
                
    print(count_result)
    print(position_result)
                
                

    
