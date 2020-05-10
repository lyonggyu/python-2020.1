'''
Created on 2020. 4. 29.

@author: lyonggyu
'''

import turtle;

# 함수 선언 부분
#    설명: 키보드에서 금액을 받아들이는 함수
#    리턴: 정상적인 금액을 리턴
def readValue():
    isCorrect = False;
    inputValue = 0;
    while(True):
        inputValue = input("숫자를 입력하시오:   ");
        try:
            inputValue = int(inputValue);
            isCorrect = True;
        except:
            print("");
            print("올바른 숫자를 입력하시오.");
        if(isCorrect):
            break;
    
    return inputValue;

#    설명: 거북이를 표현하기 위한 창 설정
def setTurtle():
    turtle.title("거북이로 2진수 표현하기");
    turtle.shape("turtle");
    turtle.setup(1050, 350);
    turtle.screensize(1000, 300);
    turtle.penup();
    turtle.left(90);

#    설명: 주어진 값을 정해진 위치에 거북이로 표현
#    입력:
#            yPos: 거북이의 y좌표 설정
#            value: 거북이로 표현할 숫자값
def displayTurtle(yPos, value):
    binary = bin(value);
    xPos = 470;
    for i in range(len(binary) - 2):
        turtle.goto(xPos, yPos);
        if(value & 1):
            turtle.color("red");
            turtle.turtlesize(2);
        else:
            turtle.color("blue");
            turtle.turtlesize(1);
        turtle.stamp();
        xPos -= 60;
        value >>= 1;


# 전역 변수 선언 부분


# 메인 코드 부분
if __name__ == '__main__':
    print("첫 번째 숫자입니다.");
    firstNum = readValue();
    print("두 번째 숫자입니다.");
    secondNum = readValue();

    setTurtle();
    displayTurtle(130, firstNum);
    displayTurtle(70, secondNum);
    displayTurtle(10, firstNum & secondNum);
    displayTurtle(-50, firstNum | secondNum);
    displayTurtle(-110, firstNum ^ secondNum);

    turtle.done();
 
