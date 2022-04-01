# import os
# os.remove("r1.txt")

import os
if os.path.exists("r3.txt"):
    os.remove("r3.txt")
else:
    print("file does not exist")

