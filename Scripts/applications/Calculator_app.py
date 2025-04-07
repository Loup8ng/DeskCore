#applications calculatrice
def calul (ch1:int, ch2: int, opération :chr ): 
    if opération == "-":
        résultat =  ch1-ch2
    elif opération == "+": 
        résultat= ch1+ch2
    elif opération == "*": 
        résultat = ch1*ch2
    elif opération == "/": 
        résultat = ch1/ch2

    return résultat