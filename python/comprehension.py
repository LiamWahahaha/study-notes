chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}

rank_dict = {key: name for key, name in chile_ranks.items()}
chile_len_set = {len(key) for key in chile_ranks}

print(rank_dict)
print(chile_len_set)
