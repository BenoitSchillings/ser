from ser import Ser
import cv2
import numpy as np
from astropy.io import fits


if __name__ == "__main__":
    import sys
    
    
    fid = Ser(sys.argv[-1])
    
    for i in range(0, fid.count - 1):
        img = fid.load_img(i)
        hdr = fits.header.Header()
        fits.writeto(sys.argv[-1] + str(i) + ".fits", img, hdr, overwrite=True)

        v = img - np.min(img)
        v = img / np.max(img)
        
        cv2.imshow("image", v)
        cv2.waitKey(1)
        
        
    fid.close()

