def aprialFidrillation(frequency):
    print(len(frequency))
    if len(frequency) > 60:
        frequency = frequency[:60:-1]
    count = 0

    if frequency.count(-1) > 5:
        return "Negative"
    elif -1 not in frequency:
        pass
    else:
        frequency = [x for x in frequency if x!= -1]
        print(frequency)
    for i in range(len(frequency)-1):
        if frequency[i] == frequency[i+1]:
            continue
        else:
            count += 1

    if count > 10:
        return "Positive"

    else:
        return "Negative"

print(aprialFidrillation([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
print(aprialFidrillation([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
print(aprialFidrillation([1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
print(aprialFidrillation([1,1,1,-1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
