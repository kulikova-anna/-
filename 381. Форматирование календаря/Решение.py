# nDays, weekday = input().split()
test = ["30 Monday", "31 Tuesday", "28 Wednesday", "30 Thursday", "31 Friday", "30 Saturday", "30 Sunday", ]

def calendar(test):
  nDays, weekday = test.split()
  weekday_list = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  weekday_index = weekday_list.index(weekday)
  print(weekday_index)
  no_day_print = ".. "*weekday_index
  n=weekday_index
  for day in range(1,int(nDays)+1):
    if day<10:
      day_print = f".{day}"
    else:
      day_print = day

    if n<6:
      end_block = " "
      n+=1
    else:
      end_block = "\n"
      n=0
    if day==1:
        print(f"{no_day_print}{day_print}", end=end_block)
    else:
      print(day_print, end=end_block)

for t in test:
  print(" ")
  print("NEW MONTH")
  calendar(t)
