'''
Created on 2020. 4. 30.

@author: lyonggyu
'''

#함수 선언 부분
#    설명: 입력을 받아들이는 함수
#    리턴: 받아들인 입력을 반환
def readValue():
    return input("반드시 숫자가 포함된 문자열을 입력하시오:   ");

#    설명: 입력 문자열에서 숫자를 제거하는 함수
#    입력:
#            inputString: 입력된 문자열
def makeNewString(inputString):
    newString = "";
    for i in range(len(inputString)):
        if((ord(inputString[i]) < 48) or (ord(inputString[i]) > 57)):
            newString += str(inputString[i]);
    print("변환 결과:", newString);


#전역 변수 선언 부분


#메인 코드 부분
if __name__ == '__main__':
    makeNewString(readValue());