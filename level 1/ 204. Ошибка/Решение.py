n = int(input())

all_bag=0
bag_in_server = []

for i in range(0,n):
  a, b = input().split()
  bag = int(a)*int(b)
  all_bag += bag
  bag_in_server.append(bag)

# print(all_bag)
# print(bag_in_server)

for b in bag_in_server:
  print(b/all_bag)
