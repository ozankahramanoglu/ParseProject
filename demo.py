import re
import numpy

class dateAnnotedMessage:
    date = ''
    hour = ''
    messageText = ''
    def __init__(self, date ,messageHour,messageText):
        """Every message know date, hour and text of its own"""
        self.date = date
        self.hour = messageHour
        self.messageText = messageText

    def __str__(self):
        return "date of message: " + self.date + "\thour of message : " + self.hour + "\ttext of message : " + self.messageText

    def __dict__(self):
        return {"date": self.date,
                "hour": self.hour,
                "message": self.messageText}


def removeNewLines(fileName):
    """Clean the code from new lined messages"""
    File = open(fileName, "r", encoding="utf8")

    allMessages = []
    stillSameMessage = ''
    for line in File:
        if not re.match("[0-3][0-9].[0-1][0-9].20[0-9][0-9]\\s[0-2][0-9]:[0-5][0-9]\\s-.*.", line):
            stillSameMessage += line.replace('\n', ' ').replace('-', '').replace(':', '').replace('\\', '').replace('"', '').rstrip('\n')
            #stillSameMessage += re.sub(r'[^A-Za-z0-9 -.ğĞüÜİıŞşÖöÇç:,><!+%()[\]{}]+', ' ', line)
        else:
            allMessages.append(line.replace('\n', ' ').replace('\\', '').replace('"', '').rstrip('\n') + stillSameMessage)
            #allMessages.append(re.sub(r'[^A-Za-z0-9 -.ğĞüÜİıŞşÖöÇç:,><!+%()[\]{}]+', ' ', line) + stillSameMessage)
            stillSameMessage = ''

    File.close()

    for i in allMessages:
        if i.count('\n') > 0:
            return "parse edilemedi"

    return allMessages


def categoryByDate(messageArray):
    """Categorize the messages based on date"""
    alldates = {}
    for message in messageArray:
        dateAndMessage = message.split('-')
        fullDate = dateAndMessage[0].split(' ')
        date = fullDate[0]

        time = ''.join([str(elem) for elem in fullDate[1:]])  #timeSTR.join(fullDate[1:])

        message = ''.join([str(elem) for elem in dateAndMessage[1:]]) #messageSTR.join(dateAndMessage[1:])

        if date not in alldates:
            messageArr =[]
            messageArr.append(dateAnnotedMessage(date, time, message))
            alldates[date] = messageArr
        else:
            appendedMessages = alldates.get(date)
            appendedMessages.append(dateAnnotedMessage(date, time, message))
            alldates[date] = appendedMessages
    return alldates


if __name__ == "__main__":
    newLinesRemoved = removeNewLines("bestDataEver.txt")
    categorizedByDateList = categoryByDate(newLinesRemoved)

    # for i in categorizedByDateList:
    #     for k in categorizedByDateList[i]:
    #         print(k)

    f = open("result.json", "a+", encoding="utf8")
    f.writelines("{" + '\n')
    otherCount = 0
    for date in categorizedByDateList:
        otherCount += 1
        f.writelines("\t\"" + date + "\": [" + '\n')
        count = 0
        for messages in categorizedByDateList[date]:
            count += 1
            f.writelines("\t\t{" + '\n')
            f.writelines("\t\t\t\"date\": \"" + messages.date + "\"," + '\n')
            f.writelines("\t\t\t\"hour\": \"" + messages.hour + "\"," + '\n')
            f.writelines("\t\t\t\"message\": \"" + messages.messageText + "\"" + '\n')
            if count == len(categorizedByDateList[date]):
                f.writelines("\t\t}" + '\n')
            else:
                f.writelines("\t\t}," + '\n')
        if otherCount == len(categorizedByDateList):
            f.writelines("\t]" + '\n')
        else:
            f.writelines("\t]," + '\n')
    f.writelines("}" + '\n')
    f.close()
