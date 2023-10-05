print("=== Changer Symbol String ===")
print("Example for changing '-' symbol to 'to' character \n\n")

while True:
    targetString = input("convert '-' -> 'to' (or enter 'quit' to exit): ")

    if targetString == 'quit':
        break

    updatedString = targetString.replace("-", "to")

    print(f"Modified string: {updatedString}\n")
    print("============================")

