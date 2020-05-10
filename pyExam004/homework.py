'''
Created on 2020. 4. 29.

@author: lyonggyu
'''

import random;

#함수 선언 부분
#    설명: 임의의 주사위 숫자를 구하는 함수
#    리턴: 주사위 숫자값 반환
def getDiceNumber():
    return random.randrange(1, 7);


#전역 변수 선언 부분


#메인 코드 부분
if __name__ == '__main__':
    print("A가 주사위를 던집니다...", end="");
    firstValue = getDiceNumber();
    print("");
    print("\t값은", firstValue);
    print("B가 주사위를 던집니다...", end="");
    secondValue = getDiceNumber();
    print("");
    print("\t값은", secondValue);
    if(firstValue > secondValue):
        print("A가 이겼습니다.");
    elif(firstValue < secondValue):
        print("B가 이겼습니다.");
    else:
        print("A와 B가 비겼습니다.");