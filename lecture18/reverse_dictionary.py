import pandas as pd
import numpy as np
from operator import itemgetter
dictionary = {'zach': 4, 'brandon':1, 'chris':99}
#print(sorted(dictionary.keys()))

blah = pd.DataFrame(dictionary.items())
print(blah)
exit(1)
reversed = sorted(dictionary.items(), key=itemgetter(1))
print(reversed)
for i in reversed:
    print(str(i[0]) + " val:" + str(i[1]))
