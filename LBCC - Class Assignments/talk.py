import sys
from sayings import goodbye

if len(sys.argv) !=2:
    sys.exit
name = sys.argv[1]
goodbye(name)