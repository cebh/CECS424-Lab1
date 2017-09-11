import re

input = "$0,123.45"

pattern = "\$(\*)*(0|[1-9](|[0-9]|[0-9][0-9])(\,[0-9][0-9][0-9])*)(|\.[0-9][0-9])"

match = re.match(pattern, input, flags=0)

if(match):
    print "Match"
else:
    print "Not Matched"