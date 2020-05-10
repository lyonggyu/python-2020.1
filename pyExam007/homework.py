'''
Created on 2020. 4. 30.

@author: lyonggyu
'''

#함수 선언 부분
#    설명: 입력을 받아들이는 함수
#    리턴: 받아들인 입력을 반환
def readValue():
    return input("숫자, 영문 대소문자, 한글, 기타 문자로 구성된 문자열을 입력하시오:   ");

#    설명: 입력 문자열에서 숫자, 영문 대문자, 영문 소문자, 한글, 기타 문자 개수 계산
#    입력:
#            inputString: 입력된 문자열
def countCharacters(inputString):
    numOfNumber = 0;
    numOfUpperCase = 0;
    numOfLowerCase = 0;
    numOfHangul = 0;
    numOfEtc = 0;
    for i in range(len(inputString)):
        ch = ord(inputString[i]);
        if((ch >= 48) and (ch <= 57)):
            numOfNumber += 1;
        elif((ch >= 65) and (ch <= 90)):
            numOfUpperCase += 1;
        elif((ch >= 97) and (ch <= 122)):
            numOfLowerCase += 1;
        elif(ch <= 127):
            numOfEtc += 1;
        else:
            numOfHangul += 1;
    print("대문자:", numOfUpperCase, ", 소문자:", numOfLowerCase, ", 숫자:", numOfNumber, ", 한글:", numOfHangul, ", 기타:", numOfEtc);


#전역 변수 선언 부분


#메인 코드 부분
if __name__ == '__main__':
    countCharacters(readValue());