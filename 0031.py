from time import process_time

start = process_time()
res=0

#i love for loops

for one in range(201):
    for two in range(101):
        if one*1 + two*2 >200:
            break
        for five in range(41):
            if one * 1 + two * 2 + five*5 > 200:
                break
            for ten in range(21):
                if one * 1 + two * 2 + five*5 + ten*10 > 200:
                    break
                for twenty in range(11):
                    if one * 1 + two * 2 + five * 5 + ten * 10 + twenty*20> 200:
                        break
                    for fifty in range(5):
                        if one * 1 + two * 2 + five * 5 + ten * 10 +twenty*20 + fifty*50> 200:
                            break
                        for hundo in range(3):
                            if one * 1 + two * 2 + five * 5 + ten * 10 + twenty * 20 + fifty * 50 + hundo*100 > 200:
                                break
                            for twoHundo in range(2):
                                if one*1+two*2+five*5+ten*10+twenty*20+fifty*50+hundo*100+twoHundo*200 ==200:
                                    res+=1

print(res)
end = process_time()
print(f"{end-start}seconds")