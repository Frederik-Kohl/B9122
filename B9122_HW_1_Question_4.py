fh = open("question4.txt")  # Open text file
txt = fh.read()  # Read contents of text file and store in string
fh.close()  # Close file
txt = txt.lower()  # Convert all letters to lowercase
words = txt.split()  # Obtain list of words from string, words may also be separated by \n. Hence don't specify sep
count_dict = dict.fromkeys(words, 0)  # Construct dictionary where words are keys

for word in words:  # Iterate through list and count occurrences, adding each occurrence to the value in the dict
        count_dict[word] = count_dict[word] + 1

sorted_list = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)  # Sort list in decreasing order
for i in range(0, 5):
    print((sorted_list[i])[1], (sorted_list[i])[0])  # Print first 5 words in list, but each tuple reversed
