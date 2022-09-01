hour = int(input("Hour:"))
minutes = str(input("Minutes:"))
daynight = input("AM or PM?")

if len(minutes) < 2:
    minutes = str(minutes)
    minutes = "0" + minutes

if hour < 12 and daynight in ["pm", "PM"]:
    hour = hour + 12
    print("%d:%s" % (hour,minutes))

if hour == 11 or 10:
    print("%d:%s" % (hour,minutes))

if hour < 10 and daynight in ["am", "AM"]:
    print("0%d:%s" % (hour, minutes))

if hour == 12 and daynight in ["pm", "PM"]:
    print("%d:%s" % (hour,minutes))

if hour == 12 and daynight in ["am","AM"]:
    print("00:%s" % minutes)
