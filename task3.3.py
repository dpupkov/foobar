def oddsToOne(s):
    return (1 if s[-1:] in ['1', '3', '5', '7', '9'] else 0)
    
def divByTwo(s):
    new_s = ''
    add = 0

    for ch in s:
        new_dgt = (ord(ch) - ord('0')) // 2 + add
        new_s = '%s%d' % (new_s, new_dgt)
        add = oddsToOne(ch) * 5

    if new_s != '0' and new_s.startswith('0'):
        new_s = new_s[1:]

    return new_s
    
def convert_str(num):
    new_s = ''
    
    if num == '0':
        stack = '0'
    else:
        stack = ''
        while num != '0':
            stack = '%d%s'%(oddsToOne(num), stack)
            num = divByTwo (num)

    return(stack)

def add_bit(binary):
    carry = '1'
    binary=list(binary)
    answer = ''
    
    for i in range(len(binary)-1, -1, -1):
        if binary[i] == '0':
            binary[i] = '1'
            return("".join(binary))
        else:
            binary[i] = '0'
    return('1'+''.join(binary))
   
    
def solution(n):
    if n == '0':
        return(0)
    
    binary = convert_str(n)
    operations = 0
    
    while len(binary) != 1:
        if binary[-3:] == '111':
            binary = add_bit(binary)
            operations += 1
        elif binary[-1:] == '1':
            binary = binary[:-1]+'0'
            operations += 1
        else:
            binary = binary[:-1]
            operations += 1
    
    return(operations)



#import sys
#print(solution(sys.argv[1]))
print(solution('8'*350))