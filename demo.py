
def removeNewLines(fileName):
    File = open(fileName, "r", encoding="utf8")

    allMessages = []
    stillSameMessage = ''
    for line in File:
        if ('-' not in line) and (':' not in line) and (line.count('/') != 2):
            stillSameMessage += line
        else:
            allMessages.append(line.replace('\n',' '))
            stillSameMessage = ''

    File.close()

    f = open("demofile2.txt", "a", encoding="utf8")

    for i in allMessages:
        if i.count('\n') > 0:
            return "parse edilemedi"

    return allMessages


newLinesRemoved = removeNewLines("bestDataEver.txt")