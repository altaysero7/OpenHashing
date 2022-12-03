"""
    Test file for creating a list data structure to compare the running time with
    the hash table created in the hash_3_1.py file.
"""

from time import process_time


if __name__ == "__main__":
    print()
    # Initialize the list
    start_time = process_time()
    array_list = []
    finished_time = process_time()
    print("The array list is created in " +
        str(finished_time-start_time) + " seconds.\n")
    # Append the data from the words_alpha.txt to the list
    start_time = process_time()
    with open("words_alpha.txt", "r", encoding='UTF-8') as f1:
        for line in f1:
            l = line.strip()
            array_list.append(l)
    finished_time = process_time()
    print("The data is appended to the array list in " +
        str(finished_time-start_time) + " seconds.\n")
    # Find the exact words between the kaikkisanat.txt and the array list
    start_time = process_time()
    MATCH = 0
    with open("kaikkisanat.txt", "r", encoding='UTF-8') as f2:
        for line in f2:
            l = line.strip()
            if l in array_list:
                MATCH += 1
    finished_time = process_time()
    print("There are", MATCH, "exact words found in the array list.")
    print("The 'find the exact words from kaikkisanat.txt' task is completed in " +
        str(finished_time-start_time) + " seconds.\n")
