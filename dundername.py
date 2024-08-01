"""__name__ is a built in variable in python which stores info about the namespace in which the python
program is being executed """
import dundername2
__name__='mynamespace' 
print(__name__) #the implicit definition of the variable gets overriden and no error is produced
"""allows you to include code in the script that should only run when the script is executed directly, 
not when it's imported"""