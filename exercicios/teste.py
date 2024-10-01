def primo(n, divisor=None):
    if divisor is None:
        divisor = n - 1  
    if n < 2:
        return False  
    if divisor == 1:
        return True 
    if n % divisor == 0:
        return False 
    return primo(n, divisor - 1) 

n = int(input())
if (primo(n)):
    print("é primo")
else:
    print("n é primo")