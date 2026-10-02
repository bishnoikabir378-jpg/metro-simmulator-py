with open('metro_data.txt', 'r') as f:
    nested = []
    for line in f:
        x = line.strip().split(",")
        nested.append(x)

    blue1 = nested[0:53]
    magenta = nested[53:78]
    blue2 = nested[78:87]

    def mintohm(minutes):
        h = minutes // 60
        m = minutes % 60
        return f"{h:02d}:{m:02d}"
    try:
        start = input("starting station-").strip().lower()
        end = input("end station-").strip().lower()
        inputtime = input("time (HH:MM)")
        
        for row in nested:
                if len(row) < 2:
                    continue
                if row[1] == start:
                    global s
                    s = row
                if row[1] == end:
                    global e
                    e = row

        if not s or not e:
                print("Station not found!")
        else:
                global first, last
                first = nested.index(s)
                last = nested.index(e)
                time = 0
                
        if s in blue1 and e in blue1:
                    hops = abs(last - first)
                    time = 2 * hops
        if s in magenta and e in magenta:
                    hops1 = hops2 =hops  = abs(last - first)
                    time = 2 * hops
        if s in blue2 and e in blue2:
                    hops = abs(last - first)
                    time = 2 * hops
        if (s in blue1 and e in magenta):
                hops1 = abs(first - 13) + abs(last - 53)
                hops2 = abs(first - 45) + abs( last-77)
                hops = min(hops1, hops2)
                if hops == hops1:
                    print("Change at Janakpuri West")
                    
                else:
                    print("Change at Botanical Garden")
                    
                time = 2 * hops + 3
        if (s in magenta and e in blue1):
                hops1 = abs(first - 53) + abs(last - 13)
                hops2 = abs(first - 77) + abs(last - 45)
                hops = min(hops1, hops2)
                if hops == hops1:
                    print("Change at Janakpuri West")
                    
                if hops == hops2:
                    print("Change at Botanical Garden")
                    
                time = 2 * hops +3
                
        if (s in blue1 and e in blue2):
                hops = abs(first -34) + abs(last - 78)
                print("Change at yamuna bank")
                time = 2 * hops + 3
        if (s in blue2 and e in blue1):
                hops = abs(first -78) + abs(last - 34)
                print("Change at yamuna bank")
                time = 2 * hops + 3
        if (s in blue2 and e in magenta):
                hops = abs(first -78) + abs(last - 77) 
                print("Change at yamuna bank and botanical garden")
                time = (2 * hops) + 6
        if (s in magenta and e in blue2):
                hops= hops1 = hops2= abs(first -77) + abs(last - 78)  
                print("Change at botanical garden and yamuna bank")
                time = (2 * hops) + 6
        try:
        
                print(f"estimated time:{time} minutes")
        except:
                print("cannot calculate time")
        for i in range(len(blue1)):
            a =360 + 2*i
            blue1[i].append(a)

        for i in range(len(blue1)):
            blue1[i].append(a-2*i)
        for i in range(len(magenta)):
            b = 360 + 2*i
            magenta[i].append(b)
        for i in range(len(magenta)):
            magenta[i].append(b - 2*i)
        for i in range(len(blue2)):
            c = 358 + 2*i
            blue2[i].append(c)
        for i in range(len(blue2)):
            blue2[i].append(c - 2*i)

        def hmtomin(x):
            h, m = map(int, x.split(":"))
            return h * 60 + m

        def nexttrain(inputtime):
            # inputtime in HH:MM format
            minutes = hmtomin(inputtime)
            
            if minutes < 360 or minutes > 1380:  # before 6:00 or after 23:00
                return None
            
            # peak hours
            if (480 <= minutes < 600) or (1020 <= minutes < 1140):
                freq = 4
            else:
                freq = 8
            global probtime
            probtime = ((minutes + freq - 1) // freq) * freq
        
            

            if first <= last and s not in magenta: #train going forward
                if s in blue1 and e in magenta  :
                    if s in blue1[14:44]:
                        if hops == hops1 : #train going backward
                            if probtime <= int(s[6]):
                                return mintohm(s[6])
                            else:
                                return mintohm(probtime)
                        if hops == hops2 : #train going forward
                            if probtime <= int(s[5]):
                                return mintohm(s[5])
                            else:
                                return mintohm(probtime)
                    else:
                        if hops == hops1 : #train going backward
                            if probtime <= int(s[5]):
                                return mintohm(s[5])
                            else:
                                return mintohm(probtime)
                        if hops == hops2 : #train going forward
                            if probtime <= int(s[6]):
                                return mintohm(s[6])
                            else:
                                return mintohm(probtime)
                        
                if probtime <= int(s[5]):
                        return mintohm(s[5])
                else:
                    return mintohm(probtime)
            if first > last and s not in magenta: #train going backward
                if probtime <= int(s[6]):
                    return mintohm(s[6])
                else:
                    return mintohm(probtime)

            if s in magenta and e not in magenta:
                if hops == hops2 : #train going forward
                    if probtime <= int(s[5]):
                        return mintohm(s[5])
                    else:
                        return mintohm(probtime)
                if hops == hops1 : #train going backward
                    if probtime <= int(s[6]):
                        return mintohm(s[6])
                    else:
                        return mintohm(probtime)
            if s in magenta and e in magenta :
                if first <= last: #train going forward
                    if probtime <= int(s[5]):
                        return mintohm(s[5])
                    else:
                        return mintohm(probtime)
                if first > last: #train going backward
                    if probtime <= int(s[6]):
                        return mintohm(s[6])
                    else:
                        return mintohm(probtime)
                
                 

        
        nexttraintime = nexttrain(inputtime)
        if nexttraintime:
            print("Next train at",start,"going towards",end,":", nexttraintime)
        else:
            print("no service available at this time")
    except:
        print("invalid input")



    try:
        def fare(hops):
            if hops <= 2:
                return 10
            elif hops <= 5:
                return 20
            elif hops <= 9:
                return 30
            elif hops <= 14:
                return 40
            elif hops <= 19:
                return 50
            else:
                return 60
        fare = fare(hops)
        print(f"Fare: Rs. {fare}")

    except:
        print("cannot calculate fare")


    def timereach():
         reachtime = hmtomin(nexttraintime) + time
         return mintohm(reachtime)
    try:
        print("You will reach at", timereach())
    except:
        print("cannot calculate reach time")

    print("--------have a nice and safe journey--------"
