not_self = []

for n in range(10000):
    dn = n
    while True:
        for digit in str(dn):
            dn += int(digit)
        if dn < 10000:
            not_self.append(dn)
        else:
            break
            
set(not_self)

answers = [i for i in range(1,10001)]

for answer in answers:
    if answer in not_self:
        continue
    else:
        print(answer)