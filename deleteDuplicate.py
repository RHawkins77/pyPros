
lines_seen = set() # holds lines already seen
outfile = open("unpaidReports.txt", "w")
for line in open("unpaidReports21.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
