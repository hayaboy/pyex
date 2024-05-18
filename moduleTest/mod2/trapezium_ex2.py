def addition(x, y):
    return x + y

def multiplication(x, y):
    return x * y

def divided_by_2(x):
    return x / 2

# 파일 자체실행시 결과확인하고자 하면 진입점 만든 후 
if __name__ == '__main__':
    print(addition(10, 5))
    print(multiplication(10, 5))
    print(divided_by_2(50))
