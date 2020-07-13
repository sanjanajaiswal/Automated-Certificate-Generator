
import cv2  

f = open("names.txt","r")
names_list = f.read().split("\n")
#print(names_list)

f1 = open("coords.txt","r")
coordinates = f1.read().split("\n")

flag=True

for i in range(len(names_list)):


    name_to_print = names_list[i]
    date_to_print = "23/03/2020"   
    # Load image in OpenCV  
    image = cv2.imread("certificate.jpg")  

    cv2.putText(image,name_to_print,(int(coordinates[0]), int(coordinates[1])),2,1,(0,0,0)) 
    cv2.putText(image,date_to_print,(int(coordinates[2]), int(coordinates[3])),2,1,(0,0,0)) 

    
    if flag:
        cv2.imshow('Certificate', image) #Shows sample image
        flag=False
    path = ''
    cv2.imwrite('./output/'+name_to_print+'.png',image)
    #os.startfile('output.png')
      

    cv2.destroyAllWindows()
    




