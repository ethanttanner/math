# 1.Generate a data set consisting of the length of each word used in the letter signed by A MOURNER. Be sure to disregard any text that uses
#       proper names, numbers, abbreviations, or titles.
# 2.Calculate the summary statistics for the letter's word lengths. Compare your findings with those of the known authors, and speculate about the identity of A MOURNER.
# 3.Compare the two Adams summaries. Discuss the viability of word-length analysis as a tool for resolving disputed documents.
# 4.What other information would be useful to identify A MOURNER?

import statistics as stats

def getWordLength( text ):
    words = text.split()
    average = sum(len(word) for word in words) / len(words)
    return average   

        
def main():
    mournerText = "The general Sympathy and Concern for the Murder of the Lad by the base and infamous on the Instant, will be sufficient Reason for your Notifying the Public that he will be buried from his Father's House, opposite, on Monday next, when all the Friends of Liberty may have an Opportunity of paying their last Respects to the Remains of this little Hero and first Martyr to the noble Cause—Whose manly Spirit (after this Accident happened) appear'd in his discreet Answers to his Doctor, his Thanks to the Clergymen who prayed with him, and Parents, and while he underwent the greatest Distress of bodily Pain; and with which he met the King of Terrors. These Things, together with the several heroic Pieces found in his Pocket, particularly Summit of human Glory, gives Reason to think he had a martial Genius, and would have made a clever Man."
    avgWordLength = getWordLength(mournerText)
    

    
    words = mournerText.split()
    wordLength = []
    letterSum = 0
    wordCount = 0
    for word in words:
        wordLength.append(len(word))
        letterSum += len(word)
        wordCount += 1
    median = stats.median(wordLength)
    mode = stats.mode(wordLength)
    std = stats.stdev(wordLength)
    var = stats.variance(wordLength)
    minLength = min(wordLength)
    maxLength = max(wordLength)
    rangee = (maxLength-minLength)
    print('Summary Statistics of MOURNER letter:\n')
    
    print('Mean: ', round(avgWordLength, 2))
    print('Median: ', median)
    print('Mode: ', mode)
    print('Standard deviation: ', round(std, 2))
    print('Sample Variance: ', round(var, 2))
    print('Range:', rangee)
    print('Minimum: ', minLength)
    print('Maximum: ', maxLength)
    print('Sum: ', letterSum)
    print('Count: ', wordCount)
    
    
#2 Most of the summary statistics that i calculated were closed to John Hancock's writing, my sample variance was much lower but our article was also much shorter.
    
    
#3 Both of Adams entries have very similar summary statistics, and he uses the highes range of word length of all the authors. Word-length analaysis probably works pretty well, because most authors have similar word usage in different passages.

#4 For this article specifically a longer text section would be helpful and would create more meaningful results. It would also be helpful to get comparable text from the same printer that the mourner text came from.


if __name__ == "__main__":
    main()

