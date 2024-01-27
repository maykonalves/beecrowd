duration = int(input())

hours = duration//3600
minutes = (duration-(hours*3600))//60
seconds = (duration-(hours*3600)-(minutes*60))

print("{}:{}:{}".format(hours,minutes,seconds))