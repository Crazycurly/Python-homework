import sys
while(1):
    try:
        file = open(input('請輸入檔案名稱：'), 'r',encoding='UTF-8')
        try:
            for line in file:
                print(line, end = '')
        finally:
            if file:
                file.close()
                break
    except FileNotFoundError:
        print('找不到檔案!\n')