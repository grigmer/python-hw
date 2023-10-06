def numsum(s):
    
    count = 0
    
    for i in s:
    
        if "1"<= i and "9" >= i:
            count += int(i)
    
    return count


print(numsum(input()))