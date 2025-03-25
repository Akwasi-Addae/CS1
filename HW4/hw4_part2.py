import hw4_util

def daily(data):
    state = input("Enter the state: ")
    print(state)
    for i in data:
        if i[0] == state:
            data = i
            break

    if len(data) != 16:
        print("State", state, "not found")
        return
    
    daily_positive = sum(i[2:9])/7/i[1]*100000

    print("Average daily positives per 100K population:", round(daily_positive,1))

def pct(data):
    state = input("Enter the state: ")
    print(state)
    for i in data:
        if i[0] == state:
            data = i
            break

    if len(data) != 16:
        print("State", state, "not found")
        return

    positive = sum(data[2:9])
    negative = sum(data[9:16])
    
    print("Average daily positive percent:", round(positive/(positive+negative)*100,1))

def quar(data):
    states = []
    for i in data:
        if sum(i[2:9])/7/i[1]*100000 > 10 or 100*sum(i[2:9])/(sum(i[2:9])+sum(i[9:16])) > 10:
            states.append(i[0])

    print("Quarantine states:")
    hw4_util.print_abbreviations(states)

def high(data):
    state = data[0][0]
    rate = 0                # random value

    for i in data:
        val = sum(i[2:9])/7/i[1]*100000
        if val > rate:
            rate = val
            state = i[0]


    print("State with highest infection rate is", state)
    print("Rate is", round(rate,1), "per 100,000 people")


index = 0
while index >= 0:
    print("...")
    index = int(input("Please enter the index for a week: "))
    print(index)

    if 1 <= index <= 29:
        request = input("Request (daily, pct, quar, high): ")
        print(request)
        request = request.lower()
        data = hw4_util.part2_get_week(index)

        if(request == "daily"):
            daily(data)
        elif request == "pct":
            pct(data)
        elif request == "quar":
            quar(data)
        elif request == "high":
            high(data)
        else:
            print("Unrecognized request")
    elif index > 25:
        print("No data for that week")

# li = [189,147,128,132,106,125,118]
# print(sum(li)/7)