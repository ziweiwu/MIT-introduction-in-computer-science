s='abcbcd'

result = []
final = []

for letters in s:
    result=result + [letters]
    if result ==sorted(result) and len(result) >= len(final):
        final = result
    elif result != sorted (result):
        result = [result [len(result)-1]]

print(final)


        
        


