def dataTypes(type: str):
    match(type.lower()):
        case "integer": return 4
        case "long": return 8
        case "float":return 4
        case "double": return 8
        case "char": return 1
        case _: return 0
dtype= input("Enter the data type, for which you want size: ")
if dataTypes(dtype)>0:
    print(f"The size of {dtype} is {dataTypes(dtype)} bytes!")
else:
    print("Invalid value")