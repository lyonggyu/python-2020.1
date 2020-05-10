'''
Created on 2020. 4. 29.

@author: lyonggyu
'''

# 함수 선언 부분
#     설명: 키보드로부터 숫자 입력
#     리턴: 입력받은 값 반환
def readValue():
    isCorrect = False;
    while(True):
        inputValue = input("0 ~ 9, a ~ f로 구성된 숫자를 입력하시오:  ");
        try:
            int(inputValue, 16);
            isCorrect = True;
        except:
            print("");
            print("올바른 숫자를 입력하시오.");
        if(isCorrect):
            break;
    
    return inputValue;

#    설명: 10진수인지 검사하는 함수
#    입력
#            value: 10진수인 지 검사할 숫자
#    리턴: 10진수일 경우 True 반환
def isDecimal(value):
    isCorrect = False;
    try:
        int(value, 10);
        isCorrect = True;
    except:
        pass;
    
    return isCorrect;

# 전역변수 선언 부분


# 메인 코드 부
if __name__ == '__main__':
    inputValue = readValue();
    if(isDecimal(inputValue)):
        print("\t입력값:", inputValue, ": 10진수");
        print("\t입력값이 16진수 일 경우:", int(inputValue, 16));
    else:
        print("\t입력값:", inputValue, ": 16진수");
        print("\t10진수 값:", int(inputValue, 16));