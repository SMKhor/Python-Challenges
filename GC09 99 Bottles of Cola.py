n = 99
for i in range (99):
    if n == 1:
        print("1 bottle of cola on the wall. 1 bottle of cola, take one down, pass it around. \nNo more bottles of cola on the wall. No more bottles of cola, go to the store to buy some more.")
        break
    print("%d bottles of cola on the wall. %d bottles of cola, take one down, pass it around." % (n,n))
    n = n - 1
