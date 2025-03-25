def number_happy(sentence):
    count = 0
    positive = ["laugh", "happiness", "love", "excellent", "good", "smile"]

    # Add up the number of times you find each positive in the sentence
    for i in positive:
        count += sentence.count(i)
    return count

def number_sad(sentence):
    count = 0
    negative = ["bad", "sad", "terrible", "horrible", "problem", "hate"]
    
    # Add up the number of times you find each negative in the sentence
    for i in negative:
        count += sentence.count(i)
    return count


if __name__ == "__main__":
    # Put the sentence in lower case so that you can find all matches
    sentence = input("Enter a sentence => ")
    print(sentence)
    sentence=sentence.lower()

    # Perform sentiment analysis
    pos = number_happy(sentence)
    neg = number_sad(sentence)

    print("Sentiment:", '+'*pos + "-"*neg)

    if(pos > neg):
        print("This is a happy sentence.")
    elif(pos < neg):
        print("This is a sad sentence.")
    else:
        print("This is a neutral sentence.")
