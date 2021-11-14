from __future__ import with_statement
import string
COLORS = ["red", "white", "green", "purple", "pink", "gray", "black", "yellow", "brown", "blue", "orange"]


class Report:

    def __init__(self, path):
        self.numLineInText = 0
        self.numWordInText = 0
        self.uniqueWord = set()
        self.dictFrequencyWord = {}
        self.dictFrequencyColors = {}
        self.listOfLongestK = []
        self.listOfCurrentK = []
        self.listLengthOfSentences = []
        self.lastSentence = ""
        self.collectStatisticalData(path)

    def collectStatisticalData(self, path):
        try:
            with open(path, 'r', errors='ignore') as f:
                for line in f:
                    cleanLineArray = self.cleanLine(line)  # We will get a clean array of words without punctuation and without \n
                    self.countLineInText()  # Assuming empty rows are counted
                    self.countWordsInText(cleanLineArray)  # Assuming punctuation is not considered a word
                    self.countUniqueWord(cleanLineArray)
                    self.countFrequencyOfWord(cleanLineArray)
                    self.longestSequenceWithoutK(cleanLineArray)
                    self.lengthOfSentence(line)
                    self.countFrequencyOfColors(cleanLineArray)
        except EnvironmentError:  #
            print('Error reading the file,Please make sure the path is correct')
            exit(1)

    def longestSequenceWithoutK(self, line):
        for word in line:
            if 'k' not in word:
                self.listOfCurrentK.append(word)
            else:
                if len(self.listOfCurrentK) > len(self.listOfLongestK):
                    self.listOfLongestK = self.listOfCurrentK.copy()
                self.listOfCurrentK = []

    def getLongestSequenceWithoutK(self):
        str1 = ' '.join(self.listOfLongestK)
        return str1

    def countLineInText(self):
        self.numLineInText += 1

    def countUniqueWord(self, line):
        for word in line:
            if word != '':
                self.uniqueWord.add(word)

    def countWordsInText(self, line):#line is array
        self.numWordInText += len(line)

    def getNumUniqueWord(self):
        return len(self.uniqueWord)

    def countFrequencyOfWord(self, line):
        for word in line:
            if word in self.dictFrequencyWord.keys():
                self.dictFrequencyWord[word] += 1
            else:
                self.dictFrequencyWord[word] = 1

    def getWordHighestFrequency(self):
        self.dictFrequencyWord = sorted(self.dictFrequencyWord.items(), key=lambda x: x[1], reverse=True)
        return next(iter(self.dictFrequencyWord))

    def lengthOfSentence(self, line):
        line = line.replace("-", ' ')
        endRest = line.find('.')
        while endRest != -1:
            self.lastSentence += line[:endRest+1]
            print(self.lastSentence.split())
            self.listLengthOfSentences.append(len(self.lastSentence.split()))
            self.lastSentence = ""
            line = line[endRest+1:]
            endRest = line.find('.')
        self.lastSentence += line

    def getMaxLengthOfSentence(self):
        return max(self.listLengthOfSentences)

    def getAverageLengthOfSentence(self):
        return sum(self.listLengthOfSentences)/len(self.listLengthOfSentences)

    def countFrequencyOfColors(self, line):
        for word in line:
            if word.strip() in COLORS:
                if word.strip() in self.dictFrequencyColors.keys():
                    self.dictFrequencyColors[word] += 1
                else:
                    self.dictFrequencyColors[word] = 1

    def getStatisticalReport(self):
        with open("statisticalData.txt", 'w', encoding='utf-8') as f:
            f.write("File statistics:\n")
            f.write("1-The amount of lines:\n")
            f.write(str(self.numLineInText))
            f.write("\n2-The amount of words:\n")
            f.write(str(self.numWordInText))
            f.write("\n3-The amount of unique words:\n")
            f.write(str(self.getNumUniqueWord()))
            f.write("\n4-Size of longest Sequence by word:\n")
            f.write(str(self.getMaxLengthOfSentence()))
            f.write("\n4-Size of Average Sequence by word:\n")
            f.write(str(self.getAverageLengthOfSentence()))
            f.write("\n5-The word with highest frequency:\n")
            f.write(str(self.getWordHighestFrequency()))
            f.write("\n6-Longest Sequence without k:\n")
            f.write(str(self.getLongestSequenceWithoutK()))
            f.write("\n8- Freqency of colors:\n")
            f.write(str(self.dictFrequencyColors))

    def cleanLine(self, line):
        lineL = line.lower()
        lineL = lineL.replace("'s", '')
        lineL = lineL.replace("-", ' ')
        for ch in string.punctuation:
            lineL = lineL.replace(ch, " ")
        lineL.strip()
        return lineL.split()

        return cleanString.split()


if __name__ == '__main__':
    print('Enter File path:')
    filePath = input()
    report = Report(filePath)
    report.getStatisticalReport()



    # r"C:\Users\ataraelmaliach\Desktop\8200\dickens.txt"
