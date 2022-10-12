import setup_processing as sp
from itertools import combinations_with_replacement
import csv
import threading

lock = threading.Lock()



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

def cript_protein(row, string_limit):
    protein = row[1][:string_limit]
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
                

    
    result_list = []
    for i in head_letters:
        result_list.append(0)
        
        
    for i in count_result:
        for j in range(0,len(head_letters)):
            if i == head_letters[j]:
                result_list[j] = count_result[i]
    
                    
    position_result_list = []
    for i in head_order:
        position_result_list.append('')
    
    for i in position_result:
        c = 0
        for j in position_result[i]:
            c += 1
            position_insert = (string_limit*(int(i)-1))+c
            position_result_list[position_insert] = j
            
                
    result = [row[0],row[2],row[4]]+ result_list + position_result_list
    
    # acquire the lock
    lock.acquire()
    # write row
    file = open('../data/new_train.csv', 'a', newline='')
    with file:
        write = csv.writer(file)
        write.writerow(result)
    
    # release the lock
    lock.release()



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
        for j in range(1,sp.STRING_LIMIT + 1):
            head_order.append(f'{i}_l_{j}')
            
    head_result = ['seq_id', 'pH', 'tm'] + head_letters + head_order
    
    # write head
    file = open('../data/new_train.csv', 'w', newline='')
        
    with file:
        write = csv.writer(file)
        write.writerow(head_result)
    
    for row in data[1:]:
            threading.Thread(target = cript_protein, args = (row, sp.STRING_LIMIT,)).start()
            # blocked limit 900 threads
            while int(threading.active_count()) >= 900:
                True
    
         
    # finish process
    stop = 0
    while stop != len(data):
        with open('../data/new_train.csv', newline='') as f:
            reader = csv.reader(f)
            new_data = list(reader)
        stop = len(new_data)
        print('wait process finished')
    
    print('Stop Process')
          

        
