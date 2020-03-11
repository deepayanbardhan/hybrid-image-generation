import cv2
import numpy as np

def ft(img):
    d= np.fft.fft2(img)
        
    #FOR DISPLAYING THE FREQUENCY ANALYSIS:
    """mag=(20*np.log(np.abs(ds)))
    mag=mag/np.max(mag)*255
    #mag[mag>255]=255
    mag=np.uint8(mag)
    
    cv2.imshow('freq',mag)
    cv2.waitKey(0)"""
    return d

def ift(freq_img):
    f_ishift = np.fft.ifftshift(freq_img)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.uint8(np.abs(img_back))
    return img_back

def hybrid(img1,img2):
    fft1=ft(img1)
    fft2=ft(img2)
    newfft=(2*fft1+1*fft2)/3;
    return ift(newfft)

img1 = cv2.imread('mac.jpg',0)
img2 = cv2.imread('kfc.jpg',0)
ans=hybrid(img1,img2)
#DISPLAY
cv2.imshow('image1',img1)
cv2.imshow('image2',img2)
cv2.imshow('hybrid',ans)
cv2.waitKey(0)
