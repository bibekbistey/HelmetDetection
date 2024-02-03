import cv2 as cv
import numpy as np


# Draw the predicted bounding box
def draw_bounding_box(classId, conf, left, top, right, bottom, frame, classes):
    frame_count = 0
    cv.rectangle(frame, (left, top), (right, bottom), (255, 178, 50), 3)
    label = '%.2f' % conf
    if classes:
        assert(classId < len(classes))
        label = '%s:%s' % (classes[classId], label)

    label_size, base_line = cv.getTextSize(label, cv.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    top = max(top, label_size[1])

    label_name,label_conf = label.split(':')
    if label_name == 'Helmet':
        cv.rectangle(frame, (left, top - round(1.5*label_size[1])), (left + round(1.5*label_size[0]), top + base_line),
                     (255, 255, 255), cv.FILLED)
        cv.putText(frame, label, (left, top), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,0), 1)
        frame_count+=1


