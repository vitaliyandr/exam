#���� �����:
#�) �� � ���� ���� ���� ���������� ������
#�) �� � ������� ���� ���� ����������� ������
#�) �� ����� ����� (�) ������� ���� ����
#�) �� ������ 5 ���� ����
#�) ������ ���� ����� ����� (�)

try:
    a = int(input('Enter the number n: '))
    x = sum(int(digit) for digit in str(a))
    digit = a % 10
    mult = 1
    b = mult * digit
    if x >= 10 and x < 100:
        print("Yes")
    else:
        print("No")
    if x >= 100 and x < 1000:
        print("Yes")
    else:
        print("No")
    if x > a:
        print("Yes")
    else:
        print("No")
    if b // 5:
        print("Yes")
    else:
        print("No")
    if x // a:
        print("Yes")
    else:
        print("No")
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
