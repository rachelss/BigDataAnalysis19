import pandas as pd
import sys

def count_words_in_book(filename):
    """
    
    """
    with open(filename,'r') as current_file:
        text = current_file.read()
    
    text = text.lower()

    #get ride of punctuations
    punctuation = [',','.','"',"'",";",':']
    for punc in punctuation:
        text = text.replace(punc,"")
    text = text.replace("\n","") #replace newlines
    text = text.split() #split long string into words
    
    text_word_count_dict = {}
    for word in text:
        if word in text_word_count_dict:
            text_word_count_dict[word] +=1
        else:
            text_word_count_dict[word] = 1
            
    text_word_count_df = pd.DataFrame.from_dict(text_word_count_dict,orient = 'index',columns = ['word_count'])
    text_word_count_df_sorted = text_word_count_df.sort_values(by = ['word_count'],ascending=False)
    
    return(text_word_count_df_sorted)
    
#myfile = "../Gutenberg/Books_EngFr/English/shakespeare/Romeo and Juliet.txt"
   #path to file
myfile = sys.argv[1]
book_df = count_words_in_book(myfile) #book_df is a dataframe of words sorted by count
print(book_df.iloc[0:10])
