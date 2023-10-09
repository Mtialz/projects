time = input("Enter time with 00:00:00 format      ")
timeparts = time.split(':')

if len(timeparts) == 3:
    hours, minutes, seconds = map(int,timeparts)
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    print("total second", total_seconds)
else:
    print("Invalid format")
