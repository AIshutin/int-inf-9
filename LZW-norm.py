original_1 = 'abacabadabacabae'
coded_1 = [3, 0, 2, 2, 1, 5]
symbols_1 = ['a', 'b', 'c', 'd', 'e']

original_2 = 'In a hole in the ground there lived a hobbit'
coded_2 = [1, 10, 0, 2, 0, 7, 11, 9, 5, 0, 8, 17, 13, 7, 24,
           6, 12, 11, 14, 10, 4, 0, 28, 5, 12, 24, 9, 8, 15,
           5, 36, 19, 21, 3, 3, 8, 13]
symbols_2 = [' ', 'I', 'a', 'b', 'd', 'e', 'g', 'h',
             'i', 'l', 'n', 'o', 'r', 't', 'u', 'v']

original_3 = ('���? ��� ����� �� ������, ��� �� ������ '
              '����� �������? �� ����� ��� ��������� �������, '
              '��� �� �����? � ������!')
coded_3 = [9, 26, 22, 3, 0, 8, 10, 18, 0, 11, 22, 19, 15,
           19, 0, 16, 10, 0, 7, 22, 25, 25, 17, 31, 2, 0,
           29, 34, 0, 21, 49, 21, 15, 24, 12, 10, 28, 0,
           26, 65, 32, 46, 13, 10, 21, 13, 19, 17, 17, 36,
           6, 22, 0, 18, 22, 13, 14, 49, 26, 27, 26, 0, 23,
           24, 22, 28, 22, 14, 17, 79, 0, 20, 17, 26, 17, 77,
           17, 57, 88, 15, 70, 30, 0, 54, 14, 45, 36, 5, 0,
           4, 77, 79, 17, 1]
symbols_3 = [' ', '!', ',', '?', '�', '�', '�', '�', '�',
             '�', '�', '�', '�', '�', '�', '�', '�', '�',
             '�', '�', '�', '�', '�', '�', '�', '�', '�',
             '�', '�', '�', '�', '�', '�']

def make_table():
    ans = dict()
    temp = 0
    '''for i in range(5):
        ans[chr(i + ord("a"))] = str(i)
        temp += 1'''
    for i in range(256):
        ans[chr(i)] = str(temp)
        temp += 1
    return [ans, temp]
        
def encodeLZW(string):
    if len(string) == 0:
        return []
    (table, last) = make_table()
    curr = ""
    ans = []
    for el in string:
        if curr + el in table:
            curr = curr + el
        else:
            ans.append(str(table[curr]))
            table[curr + el] = str(last)
            last += 1
            curr = el
    ans.append(table[curr])
    return ans
            
def decodeLZW(string):
    #print(string)
    table1, last = make_table()
    table = dict()
    was = set("")
    for el in table1:
        was.add(el)
        table[str(table1[str(el)])] = str(el)
    ans = []
    prev = ""
    s = ""
    #print(was)
    for new in string:
        #print('===========')
        #print(new, table, ans)
        s = table[new]
        #print(prev, s)
        ans.append(s)      
        if prev + s[0] not in was:
            table[str(last)] = prev + s[0]
            was.add(prev + s[0])
            last += 1
        prev = s
    '''print(table, was)
    print("ANS: ", ans)'''
    return "".join(ans)
        
import LZW_tester as test
test.testEncoder(encodeLZW)
test.testDecoder(decodeLZW)
'''
print(decodeLZW(encodeLZW(original_3)) == original_3)
print("---------------")
print(original_1)
print(coded_1)
print(symbols_1)'''