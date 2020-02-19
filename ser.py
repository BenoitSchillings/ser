import numpy as np
from pprint import pprint

class Ser(object):

    def __init__(self, fname):
        self._fid = open(fname, 'rb')
        self.get_sizes()

    def get_sizes(self):
        self.xsize = np.int32(self.read_at(26, 1, np.int32)[0])
        self.ysize = np.int32(self.read_at(30, 1, np.int32)[0])
        self.depth = np.int32(self.read_at(34, 1, np.int32)[0]) // 8
        self.count = np.int32(self.read_at(38, 1, np.int32)[0])
        pprint(vars(self))
        self.image_size = self.xsize * self.ysize

    def read_at(self, pos, size, ntype):
        self._fid.seek(pos)
        return np.fromfile(self._fid, ntype, size)
        
        

    def swap16(x):
        return uint16.from_bytes(x.to_bytes(2, byteorder='little'), byteorder='big', signed=False)

    def count():
        return self.count

    def load_img(self, image_number):
        if (image_number >= self.count or image_number < 0):
            return 0
            
        if (self.depth == 2):
            img = self.read_at(178 + image_number * self.image_size * self.depth, self.image_size, np.uint16)
        else:
            img = self.read_at(178 + image_number * self.image_size, self.image_size, np.uint8)  
            img = img.astype(np.uint16)
            img = img * 255 
            
        out = img.reshape((self.ysize, self.xsize)).astype(np.uint16)
        
        
        #out = out[0:1024,0:1024]
        return out

    def close(self):
        self._fid.close()


import cv2

if __name__ == "__main__":
    import sys
    
    
    fid = Ser(sys.argv[-1])
    sum = fid.load_img(0) * 1.0
    
    for i in range(0, fid.count - 1):
        img = fid.load_img(i)
        sum = sum + img
        v = sum / np.max(sum)
        
        cv2.imshow("image", 50.0*v)
        cv2.waitKey(1)
        
        
    fid.close()

