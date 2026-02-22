def number_pattern(n):
    cadena = ""
    if not isinstance(n, int) :
        return "Argument must be an integer value"
    if n < 1 :
        return "Argument must be an integer greater than 0"
    else :
        for num in range(1,n+1):
            if num == n:
                cadena += str(num)
            else :
                cadena += str(num) + " "
        return cadena
print(number_pattern(4))
            