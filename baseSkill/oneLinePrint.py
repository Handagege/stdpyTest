import sys
import time
from collections import deque
fancy_loading = deque('>--------------------')
for progress in range(100):
        time.sleep(0.5)
        print "Download progress: %d   \r" % (progress),
        #sys.stdout.write("Download progress: %d%%   \r" % (progress))
        sys.stdout.flush()
        
#while True:
#        print '\r%s' % ''.join(fancy_loading),
#        fancy_loading.rotate(1)
#        #sys.stdout.flush()
#        time.sleep(0.08)
