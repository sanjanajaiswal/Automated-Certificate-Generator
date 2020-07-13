import cv2 as cv

f = open("coords.txt","w")

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        #img[:] = 0
        cv.putText(img,"coordinates (%d,%d)"%(x,y),(60,60),2,1,(0,255,0)) 
        f.write(str(x)+"\n")                                              
        f.write(str(y)+"\n")                                              
                                                                          
# Create a black image, a window and bind the function to window
img = cv.imread("certificate.jpg")


#cv.imshow('image',img)
cv.namedWindow('image')

while(1):
    cv.setMouseCallback('image',draw_circle)
    cv.imshow('image',img)
    if cv.waitKey(10) & 0xFF==27:   #Press Escape Key to terminate window
        break
cv.destroyAllWindows()   



f.close()