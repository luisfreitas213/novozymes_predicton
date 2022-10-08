import setup_processing as sp
from itertools import combinations_with_replacement


# create combinations

def dict_combinations(sample_list, sample_seq):
    # create dictionary
    final_dict = {}
    for k in sample_seq:
        final_dict.update({str(k):[]})
        
    # create all combinations in list of tuples 
    list_combinations = list()
    for n in range(2,max(sample_seq)+1):
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

    print(final_dict)
