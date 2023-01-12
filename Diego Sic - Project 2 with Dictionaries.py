#Diego Sic
#Project 2 - DNA Identification

def strs_to_ints(l_strs):
    '''Type converts a list of strings to integers. Returns a new list.'''
    # This is called a list comprehension. It is a compact way of accumulating a new list.
    return [int(s) for s in l_strs]

def breaking_data_base_in_dic_v2(Doc):
    '''
    This function will break the lines of a document,
    and separate the elements using "," as the parameter.
    Each line will be saved in a list, and all llines will be
    saved in individual lists.
    Parameter:
        A file object, contents formatted as CSV, open in read mode.
    Return:
        A dictonary with all the first columns as keys
        and the values are the rest of the values in the line of the
        respective key 
    '''
    d = {}
    first_line = True

    for line in Doc:
        line = line.strip().split(",")
        if first_line:
            d[line[0]] = line[1:]
            first_line = False
        else:
            # Column 1 = name, all others = numbers
            d[line[0]] = strs_to_ints(line[1:])

    return d

def counting_repetions(lines_2, str_to_check):
    '''This function will check how many repetions
    of a DNA type there are in a sequence using a specific
    string describing the DNA type to check, and will return 
    the maximum num of repetions
    Parameter:
        A string with a DNA sequence(lines_2) and
        a string of 4 characters with the DNA type desire 
        to check (str_to_check)
    Return:
        A int describing the maximum amount of repetions
        of the DNA types that has been checked'''
    counter = 0  
    list_of_counters = []
    for i in range(len(lines_2)):
        if lines_2[i:i+4] == str_to_check:
            counter += 1
            for j in range(i+4,len(lines_2),4):       
                if lines_2[j:j+4] == lines_2[i:i+4]:
                    counter += 1

            list_of_counters.append(counter)
            counter = 0

    results = max(list_of_counters)
    return results

def check_sequence_matches(lines_2, d):
    '''This function will use a dictionary
    to determine the quantity of times a DNA
    type appers in a sequence storaged in a list.
    Parameter:
        A string describing a DNA sequence(lines_2)
        a dictionary with the names and DNA types
    Return:
        A list describing how many the DNA types
        apper'''
    results = []
    l_keys = list(d.keys())  
    for str_to_check in d[l_keys[0]]:
        results.append(counting_repetions(lines_2,str_to_check))
    return results

def check_data_base(d, lines_2):
    '''This function will check if the results of the function
    "check sequence" matches with the data in the dictionary
    Parameter:
        A string describing a DNA sequence(lines_2)
        a dictionary with the names and DNA types
    Return:
        A string with the name of the match if exist
        otherwise will return "no match"'''

    name = "No match"
    l_keys = list(d.keys())
    results = check_sequence_matches(lines_2, d)

    for key in l_keys:
        if key != l_keys[0]:
            for i in range(len(d[key])):
                list_to_work = d[key]
                list_to_work[i] = int(list_to_work[i])
            if d[key] == results:
                name = key       
    return name

def main():
    #Open the document
    Doc = open("Data_base.txt", "r")
    dictionary = breaking_data_base_in_dic_v2(Doc)  
    Doc.close()

    sequence = open("sequence1.txt", "r")
    lines_0 = sequence.read()
    sequence.close()
    name_coincidence = check_data_base(dictionary, lines_0)
    print(name_coincidence)

    sequence = open("sequence2.txt", "r")
    lines_1 = sequence.read()
    sequence.close()
    name_coincidence = check_data_base(dictionary, lines_1)
    print(name_coincidence)
    
    sequence = open("sequence3.txt", "r")
    lines_2 = sequence.read()
    sequence.close()
    name_coincidence = check_data_base(dictionary, lines_2)
    print(name_coincidence)
    
    sequence = open("sequence4.txt", "r")
    lines_3 = sequence.read()
    sequence.close()
    name_coincidence = check_data_base(dictionary, lines_3)
    print(name_coincidence)

if __name__ == "__main__":
    main()
