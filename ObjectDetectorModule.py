import cv2


classNames= []
classFile = 'coco.names'
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt' # Have to change this Path to a complete path in Pi
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

def getObjects(img,thres,nms,draw=True,objects=[]): # If we write it false, it'll not draw and thus increase frame rate; objects specified by the user.
    classIds, confs, bbox = net.detect(img,confThreshold=thres,nmsThreshold=nms)
    # print(classIds,bbox)
    if len(objects) == 0: objects = classNames  # We want to detect all the classes.
    objectInfo = []
    if len(classIds) != 0:
        for classId,confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            className = classNames[classId - 1]
            if className in objects:
                objectInfo.append([box,className])  # Append bounding box and class name.
                if (draw):
                    # We put it inside the big loop because we want to send the information of the bounding box and the class name as well.
                    cv2.rectangle(img,box,color=(0,255,0),thickness=2)
                    cv2.putText(img,className.upper(),(box[0]+10,box[1]+30),
                                cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                                cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    return img,objectInfo


# We want it to run by itself and other scripts to be able to access it
if __name__ == "__main__":
    # Grab the image:
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    # cap.set(10,70) # Brightness

    while True:
        success, img = cap.read()
        result,objectInfo = getObjects(img,0.45,0.2,objects=['cup','mouse'])
        # print(objectInfo)
        # Display this:
        cv2.imshow("Output", img)
        cv2.waitKey(1)
