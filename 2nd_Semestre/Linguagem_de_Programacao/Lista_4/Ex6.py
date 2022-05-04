e = input(">>> ")
led = 0
for i in range(len(e)):
    if e[i] == '1':
        led += 2
    elif e[i] == '7':
        led += 3
    elif e[i] == '4':
        led += 4
    elif e[i] == '2' or e[i] == '3' or e[i] == '5':
        led += 5
    elif e[i] == '6' or e[i] == '9'or e[i] == '0':
        led += 6
    else:
        led += 7
print(f">>> {led}")