"""
Question : Create a dictionary containing the number as key and their frequency as their value.
Input : A list of numbers.
Link : https://www.youtube.com/watch?v=Ocd_uHpsQyg&list=PLhR2IpV1b2FwWwviBHRrR118YAaSlyhTU&index=10&ab_channel=CodeandDebug
"""
def frequency_counter(lst):
    res_dict = {}
    for element in lst:
        if element not in res_dict:
            res_dict[element] = 1
        else:
            res_dict[element] += 1
    return res_dict

if __name__ == "__main__":
    sample_input = [5,6,7,7,1,9,111,1,1,5,1,1]
    print("Output : ",frequency_counter(sample_input))