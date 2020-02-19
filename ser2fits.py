from ser import Ser
import cv2

if __name__ == "__main__":
    import sys
    
    
    fid = Ser(sys.argv[-1])
    
    for i in range(0, fid.count - 1):
        img = fid.load_img(i) * 1.0
        v = img - np.min(img)
        v = img / np.max(img)
        
        cv2.imshow("image", v)
        cv2.waitKey(1)
        
        
    fid.close()

