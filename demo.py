class dateAnnotedMessage:
    date = ''
    hour = ''
    messageText = 'text'
    def __init__(self, date ,messageHour,messageText):
        #messageArray[0] = time that message sent
        self.date = date
        self.hour = messageHour
        self.messageText = messageText

    def __str__(self):
        print("date of message: " + self.date + "\thour of message : " + self.hour + "\ttext of message : " + self.messageText)


def removeNewLines(fileName):
    File = open(fileName, "r", encoding="utf8")

    allMessages = []
    stillSameMessage = ''
    for line in File:
        if (('-' not in line) and (':' not in line)) or ('http' in line):
            stillSameMessage += line.replace('\n', ' ').replace('-', ' ').replace(':', ' ').replace('\n', ' ')
        else:
            allMessages.append(line.replace('\n', ' '))
            stillSameMessage = ''

    File.close()

    for i in allMessages:
        if i.count('\n') > 0:
            return "parse edilemedi"

    return allMessages


def categoryByDate(messageArray):
    alldates = []
    for message in messageArray:
        dateAndMessage = message.split('-')
        fullDate = dateAndMessage[0].split(' ')
        date = dateAndMessage[0]
        time = fullDate[1:]
        message = dateAndMessage[1:]
        alldates.append(date)
        # else:
        #     alldates[alldates.index(date)].append(dateAnnotedMessage(date, time, message))
    alldates = set(alldates)
    return alldates

newLinesRemoved = removeNewLines("bestDataEver.txt")
for i in newLinesRemoved:
    print(i)

categorizedByDateList = categoryByDate(newLinesRemoved)

for i in categorizedByDateList:
    print(i)