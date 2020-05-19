num = [["59647042"], ["01260528"], ["01616970", "69921388", "53451508"], ["710", "042", "633"]]
# invoice = ["91132057", "53977042", "69565958", "13359685", "52822508", "64268088", "95756107", "67921388", "15269483", "31208591", "85601171", "31697745", "94191710", "87883887", "33598443", "01260528", "01626970"]
invoice = ["53977042", "67921388", "01260528", "91132057"]
out = {'特別獎': 0, '特獎': 0, '頭獎': 0, '二獎': 0, '三獎': 0, '四獎': 0, '五獎': 0, '六獎': 0, '沒中獎': 0}

def check(inv):
    for chk in num[2]:
        for i in range(0,6):
            if inv[i:8] == chk[i:8]:
                out[list(out.keys())[2+i]] += 1
                return 1
    for chk in num[3]:
        if inv[5:8] == chk:
            out['六獎']+=1
            return 1
    return 0

##First
while num[0][0] in invoice:
    out['特別獎'] += 1
    invoice.remove(num[0][0])

while num[1][0] in invoice:
    out['特獎'] += 1
    invoice.remove(num[1][0])

for index in invoice:
    if not check(index):
        out['沒中獎']+=1
        
print(out)
##Second
print(out['特別獎']*10000000+out['特獎']*2000000+out['頭獎']*200000+out['二獎']*40000+out['三獎']*10000+out['四獎']*4000+out['五獎']*1000+out['六獎']*200)