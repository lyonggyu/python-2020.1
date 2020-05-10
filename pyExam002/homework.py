'''
Created on 2020. 4. 29.

@author: lyonggyu
'''

# 함수 선언 부분
#    설명: 키보드에서 금액을 받아들이는 함수
#    리턴: 정상적인 금액을 리턴
def readValue():
    isCorrect = False;
    inputValue = 0;
    while(True):
        inputValue = input("교환할 금액을 입력하시오:   ");
        try:
            inputValue = int(inputValue);
            isCorrect = True;
        except:
            print("");
            print("올바른 금액을 입력하시오.");
        if(isCorrect):
            break;
    
    return inputValue;

#    설명: 입력받은 금액을 몫과 나머지로 변환
#    입력:
#            value: 변환할 값
#            unit: 변환할 단위 숫자(50000, 10000, 5000, 1000, 500, 100, 50, 10 중 하나)
#    리턴: 몫과 나머지 리스트 반환
#            몫: 해당하는 변환 단위 개수
#            나머지: 해당 단위로 변환하고 남은 나머지
def exchangeMoney(value, unit):
    result = [];
    result.append(value // unit);
    result.append(value % unit);
    
    return result;


# 전역 변수 선언 부분


#메인 코드 부분
if __name__ == '__main__':
    moneyUnit = [50000, 10000, 5000, 1000, 500, 100, 50, 10];
    inputValue = readValue();
    for i in range(len(moneyUnit)):
        result = [];
        if(inputValue >= moneyUnit[i]):
            result = exchangeMoney(inputValue, moneyUnit[i]);
            inputValue = result[1];
            if(moneyUnit[i] >= 1000):
                print(moneyUnit[i], "원 변환:", result[0], "장");
            else:
                print(moneyUnit[i], "원 변환:", result[0], "개");
    print("나머지 금액:", inputValue, "원");