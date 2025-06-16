def frequency_counter(lst):
    hash_map = dict()
    for element in lst:
        hash_map[element] = hash_map.get(element,0)+1
    return hash_map
if __name__ == "__main__":
    sample_input = [5,6,7,7,1,9,111,1,1,5,1,1]
    print("Output : ",frequency_counter(sample_input))