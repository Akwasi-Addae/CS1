def parse(file):
    ''' Function for parsing the 2 documents'''
    output = []
    word = ''
    
    for line in open(file, encoding = "ISO-8859-1"):
        for i in line:                  # Check every letter
            if i.isalpha() and (65<=ord(i)<=90 or 97<=ord(i)<=122):             # Wasn't working correctly when I would read the '-' character, so I had to add the ord function
                word += i
            if i == "\r" or i == "\t" or i == "\n" or i == ' ':     # Stop constracting the word when we reach special characters
                if len(word) > 0:
                    output.append(word.lower().strip())
                word = ''

    return output

def average(words):
    '''To calculate the average word length'''
    m = 0
    for i in words:
        m += len(i)

    return m/len(words)

def ratio_distinct(words):
    '''Calculate the ratio of distinct words'''
    return len(set(words)) / len(words)

def word_sets(words, max_size):
    '''Get the word sets'''
    # Initialize a list
    li = []
    for i in range(0, max_size):        # Set each value to be a set
        li.append(set())

    for i in words:
        li[len(i)-1].add(i)

    return li

def word_pairs(words, max_sep):
    '''Get the word pairs as a list of tuples'''
    pairs = []

    # Get word pairs
    for i in range(0, len(words)-1):  
        for j in range(i + 1, min(i + max_sep + 1, len(words))):
            pairs.append((words[i],words[j]))

    return pairs

def ratio_distinct_pairs(pairs):
    '''Get the ratio of distinct pairs'''
    return len(set(pairs))/len(pairs)

if __name__ == "__main__":
    file_lists = []
    files = []
    part4 = []
    word_set_lists = []

    # Get the input files and max setps and ppen the files into a list
    files.append(input("Enter the first file to analyze and compare ==> ").strip())
    print(files[0])
    files.append(input("Enter the second file to analyze and compare ==> ").strip())
    print(files[1])
    max_sep = int(input("Enter the maximum separation between words in a pair ==> "))
    print(max_sep)

    # Get stop words
    stop_words = set()
    for stop in open("stop.txt", encoding = "ISO-8859-1"):
        words = stop.split()
        for i in words:
            stop_words.add(i.replace("'",""))
    
    # Parse the 2 docs
    file_lists.append(parse("{}".format(files[0])))
    file_lists.append(parse("{}".format(files[1])))
    
    # Remove stop words
    for i in stop_words:                            # Go through stop words and for each value, remove them from files
        while i in file_lists[0]:                   
            file_lists[0].remove(i)
        while i in file_lists[1]:
            file_lists[1].remove(i)

    # Calculate max word lengths
    maxes = [0,0]
    for i in file_lists[0]:
        if len(i) > maxes[0]:
            maxes[0]=len(i)

    for i in file_lists[1]:
        if len(i) > maxes[1]:
            maxes[1]=len(i)
        
    for i in range(0,2):
        print()
        print("Evaluating document", files[i])

        # Average
        print("1. Average word length: {0:.2f}".format(average(file_lists[i])))

        # Ratio of distinct words
        print("2. Ratio of distinct words to total words: {0:.3f}".format(ratio_distinct(file_lists[i])))

        # # Word sets
        print("3. Word sets for document " + files[i] + ":")
        word_set_lists.append(word_sets(file_lists[i], maxes[i]))
       
        for j in range(1, maxes[i]+1):
            # Print the word length and then the number of words 
            if len(word_set_lists[i][j-1]) != 0:
                print(" " *(4-len(str(j))) + "{0}:".format(j) + " " * (4-len(str(len(word_set_lists[i][j-1])))) + "{0}:".format(len(word_set_lists[i][j-1])), end=" ")
            else:
                print(" " *(4-len(str(j))) + "{0}:".format(j) + " " * (4-len(str(len(word_set_lists[i][j-1])))) + "0:")
                continue
            
            # Print the words themselves
            if 0 < len(word_set_lists[i][j-1]) < 7:         # If there are 6 or fewer
                last = 0
                for q in sorted(word_set_lists[i][j-1]):    # Sort the words
                    if last+1 == len(word_set_lists[i][j-1]):    # Remove the extra space at the end of last word when we get to the last word
                        print(q)
                    else:
                        print(q, end=" ")
                    last+=1         
            else:                                           # Output for when we have more than 6 words 
                count = 0
                for q in sorted(word_set_lists[i][j-1]):
                    if count == 3:                          # Print the ...
                        print("...", end=" ")
                    if count > len(word_set_lists[i][j-1]) - 4 or count < 3:    # Print the words
                        if count+1 != len(word_set_lists[i][j-1]):          # Add the end=(" ")
                            print(q, end=" ")
                        else:                                               # Print the last word without the end=(" ")
                            print(q)
                    count += 1            

        print("4. Word pairs for document " + files[i])
        word_pairs_list = word_pairs(file_lists[i], max_sep)
        distinct_pairs = set()
        for i in word_pairs_list:
                distinct_pairs.add(tuple(sorted(i)))

        # Save the distinct pairs for later use to compute word pair similarity
        part4.append(distinct_pairs)

        print(" ", len(distinct_pairs), "distinct pairs")
        count = 0
        distinct_pairs = list(distinct_pairs)
        distinct_pairs.sort()
        middle = False
        for i in distinct_pairs:
            if count < 5 or count >= len(distinct_pairs) - 5:
                print(" ", i[0],i[1])
            
            if count == 5 and not middle:
                print("  ...")
                middle = True
            count+=1
            
        print("5. Ratio of distinct word pairs to total: {0:.3f}".format(len(distinct_pairs)/len(word_pairs_list)))

    print()
    print("Summary comparison")

    # Average longer words
    if average(file_lists[0]) >  average(file_lists[1]):
        print("1. {0} on average uses longer words than {1}".format(files[0],files[1]))
    else:
        print("1. {0} on average uses longer words than {1}".format(files[1],files[0]))
    
    # Overall use similarity
    jaccard_words = len(set(file_lists[0]) & set(file_lists[1])) / len(set(file_lists[0]) | set(file_lists[1]))
    print("2. Overall word use similarity: {0:.3f}".format(jaccard_words))
    
    # Similarity by length
    max_length = max(maxes)
    word_sets_file1 = word_sets(file_lists[0], max_length)
    word_sets_file2 = word_sets(file_lists[1], max_length)
    print("3. Word use similarity by length:")
    for length in range(1, max_length + 1):  # Start from 1 and go to max word length
        if length - 1 < len(word_sets_file1):
            set1 = word_sets_file1[length - 1]
        else:
            set1 = set() 

        if length - 1 < len(word_sets_file2):
            set2 = word_sets_file2[length - 1]
        else:
            set2 = set()

        if set1 | set2:
            jaccard_length = len(set1 & set2) / len(set1 | set2)
        else:
            jaccard_length = 0
        print(" "*(4-len(str(length))) + "{0}: {1:.4f}".format(length,jaccard_length))

    # Word pair similarity
    print("4. Word pair similarity: {0:.4f}".format(len(part4[0] & part4[1]) / len(part4[0] | part4[1])))
