import sys


q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    final_string = ""
    for i in s:
        if i in "hackerrank":
            final_string = final_string + i

    if final_string == "hackerrank":
        print "YES"
    else:
        print "NO"