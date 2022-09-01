print("Times Tables Generator (up until 20)")
string = input("Which time table would you like to print out? ")
num = int(string)
numcol1 = ["%s X 1" % string, "%s X 2" % string, "%s X 3" % string, "%s X 4" % string, "%s X 5" % string, "%s X 6" % string, "%s X 7" % string, "%s X 8" % string, "%s X 9" % string, "%s X 10" % string,
           "%s X 11" % string, "%s X 12" % string, "%s X 13" % string, "%s X 14" % string, "%s X 15" % string,"%s X 16" % string, "%s X 17" % string, "%s X 18" % string, "%s X 19" % string, "%s X 20" % string]
g = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
numcol2 = []
for i in g:
    numcol2.append(i * num)

print("\n%s Times Table" % string)
for i in range(20):
    print(f"{numcol1[i]:^15} {numcol2[i]:^15}")
