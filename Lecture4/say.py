# import cowsay
# import sys
#
# if len(sys.argv) == 2:
#     cowsay.trex("Hello, " + sys.argv[1])
# else:
#     sys.exit("Usage: say.py <your_name>")

import sys

from sayings import hello, goodbye


if len (sys.argv) == 2:
    goodbye(sys.argv[1])
