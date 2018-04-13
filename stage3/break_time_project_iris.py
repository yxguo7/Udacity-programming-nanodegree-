import time
import webbrowser

total_breaks = 3
break_count = 1
print "This working period started on " + time.ctime()
while break_count < 4:
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=d9TpRfDdyU0")
    break_count += 1



