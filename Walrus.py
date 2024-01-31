"""Walrus operator(':='): 
   Performing assignment to a variable and executing an expression/ function at the same execution. 
   useful to reduce lines of code 
"""
def analyse_text(text:str) -> dict: # '->' specifies that the analyse_text() function should return a dict only 
    details:dict ={'words' :(words := text.split()), 
    # 'details:dict' specifies that we are declaring a dictionary named 'details'
                   'amount': len(words),
                   'chars': len(''.join(words)),
                   'reversed': words[::-1]
                  }
    return details
print(analyse_text('name my is Ishu'))
"""
here with the help of walrus operator, the two tasks we are doing at the same execution are:
1: words=text.split()
2: {"words" : words}
"""