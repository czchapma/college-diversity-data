#Run python validateFiles.py before checking in!

def validate(filename):
    f = open(filename, 'r')
    header_cols = f.readline().count(",")
    data = f.readlines()
    count = 2
    error = False
    for line in data:
        if line.count(",") != header_cols:
            error = True
            print "Error in " + filename + " at line " + str(count) + " expected " + str(header_cols) + " columns"
        count += 1
    if not error:
        print filename + " is all set for checking in!" 


validate("gender.csv")
validate("race.csv")
