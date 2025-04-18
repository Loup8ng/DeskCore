#applications calculatrice
def calul (ch1:float, ch2: float, opération :chr ): 
    if opération == "-":
        résultat =  ch1-ch2
    elif opération == "+": 
        résultat= ch1+ch2
    elif opération == "*": 
        résultat = ch1*ch2
    elif opération == "/": 
        résultat = ch1/ch2

    return résultat
