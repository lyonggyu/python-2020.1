'''
Created on 2020. 4. 29.

@author: lyonggyu
'''
#함수 선언 부분
#    설명: 키보드로부터 값을 받아들이는 함수
#    입력:
#            startNum: 시작 값
#            endNum: 끝 값
#    리턴: 키보드로부터 받아들인 값
def readValue(startNum, endNum):
    isCorrect = False;
    inputValue = 0;
    while(True):
        inputValue = input("숫자를 입력하시오: ");
        try:
            inputValue = int(inputValue);
            if((inputValue >= startNum) and (inputValue <= endNum)):
                isCorrect = True;
        except:
            print("");
            print("올바른 숫자를 입력하시오.");
        if(isCorrect):
            break;
    
    return inputValue;

#    설명: for 반복문을 이용해 구구단 출력
#    입력:
#            start: 구구단 시작 단
#            end: 구구단 끝 단
#            numOfRow: 한 행에 출력한 단 개수
def printGugudanWithFor(startNum, endNum, numOfRow):
    quotient = (endNum - startNum + 1) // numOfRow;
    for i in range(quotient):
        printGugudanForFor(startNum + i * numOfRow, startNum + (i + 1) * numOfRow, numOfRow);
        print("");
    printGugudanForFor(startNum + quotient * numOfRow, endNum + 1, (endNum + 1) - (startNum + quotient * numOfRow));

#    설명: 실제로 for를 활용해 구구단을 출력하는 함수
#    입력:
#            newStart: 구구단 시작 단
#            newEnd: 구구단 끝 단
#            numOfRow: 한 행에 출력한 단 개수
def printGugudanForFor(newStart, newEnd, numOfRow):
    rowCount = 1;
    for i in range(1, 10):
        for j in range(newStart, newEnd):
            print("\t", j, "X", i, "=", (j * i), "\t", end = "");
            rowCount += 1;
            if(rowCount > numOfRow):
                rowCount = 1;
                print("");

#    설명: while 반복문을 이용해 구구단 출력
#    입력:
#            startNum: 구구단 시작 단
#            endNum: 구구단 끝 단
#            numOfRow: 한 행에 출력한 단 개수
def printGugudanWithWhile(startNum, endNum, numOfRow):
    quotient = (endNum - startNum + 1) // numOfRow;
    index = 0;
    while(index < quotient):
        printGugudanForWhile(startNum + index * numOfRow, startNum + (index + 1) * numOfRow, numOfRow);
        index += 1;
        print("");
    printGugudanForWhile(startNum + quotient * numOfRow, endNum + 1, (endNum + 1) - (startNum + quotient * numOfRow));

#    설명: 실제로 while을 활용해 구구단을 출력하는 함수
#    입력:
#            newStart: 구구단 시작 단
#            newEnd: 구구단 끝 단
#            numOfRow: 한 행에 출력한 단 개수
def printGugudanForWhile(newStart, newEnd, numOfRow):
    rowCount = 1;
    index = 1;
    while(index < 10):
        indexDan = newStart;
        while(indexDan < newEnd):
            print("\t", indexDan, "X", index, "=", (indexDan * index), "\t", end = "");
            rowCount += 1;
            if(rowCount > numOfRow):
                rowCount = 1;
                print("");
            indexDan += 1;
        index += 1;

#    설명: 리스트를 이용해 구구단 출력
#    입력:
#            startNum: 구구단 시작 단
#            endNum: 구구단 끝 단
#            numOfRow: 한 행에 출력한 단 개수
def printGugudanWithList(startNum, endNum, numOfRow):
    middleList = [];
    lastList = [];
    quotient = (endNum - startNum + 1) // numOfRow;
    remainder = (endNum - startNum + 1) % numOfRow;
    for i in range(1, 10):
        for j in range(startNum, endNum + 1):
            row = str(j) + " X " + str(i) + " = " + str(j * i);
            middleList.append(row);
        lastList.append(middleList);
        middleList = [];
    
    for i in range(quotient):
        printGugudanForList(lastList, i, numOfRow, 0);
        print("");
    if(remainder != 0):
        printGugudanForList(lastList, quotient, numOfRow, remainder);

#    설명: 실제로 리스트를 이용해 출력하는 함수
#    입력:
#            resultList: 구구단이 저장되어 있는 리스트
#            quotient: 2차 리스트에서 numOfRow 개수만큼 끊어서 출력하기 위해
#            numOfRow: 한 행에 출력될 단의 개수
#            remainder: numOfRow 개수만큼 출력된 남은 나머지 개수 지정
#                        (일반적으로 0이고 나머지가 있을 때만, 나머지 값 지정)
def printGugudanForList(resultList, quotient, numOfRow, remainder):
    printIndex = quotient * numOfRow;
    for i in range(9):
        for j in range(numOfRow):
            if((remainder != 0) and (j >= remainder)):
                break;
            print("\t", resultList[i][printIndex], "\t", end = "");
            printIndex += 1;
        print("");
        printIndex = quotient * numOfRow;


#전역 변수 선언 부분


#메인 코드 부분
if __name__ == '__main__':
    print("for 문 이용 시 1 입력, while 문 이용 시 2 입력, 리스트 이용 시 3을 입력하시오.");
    selection = readValue(1, 3);
    
    print("");
    print("2 ~ 9 사이로 구구단의 시작 단을 입력하시오.");
    startNum = readValue(2, 9);
    
    print("");
    print(startNum, "~ 9 사이로 구구단의 끝 단을 입력하시오.");
    endNum = readValue(startNum, 9);
    
    print("");
    if((endNum - startNum + 1) == 1):
        numOfRow = 1;
    else:
        numOfRowEnd = endNum - startNum + 1;
        print("1 ~", numOfRowEnd, "사이로 한 행에 출력할 단의 개수를 입력하시오.");
        numOfRow = readValue(1, numOfRowEnd);
    
    print("");
    print("구구단 출력:");
    if(selection == 1):
        printGugudanWithFor(startNum, endNum, numOfRow);
    elif(selection == 2):
        printGugudanWithWhile(startNum, endNum, numOfRow);
    else:
        printGugudanWithList(startNum, endNum, numOfRow);