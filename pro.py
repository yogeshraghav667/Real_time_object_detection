import cv2
from gui_buttons import Buttons

# Initialize Buttons
button = Buttons()
button.add_button("person", 20, 20)
button.add_button("cell phone", 20, 100)
button.add_button("keyboard", 20, 180)
button.add_button("remote", 20, 260)
button.add_button("scissors", 20, 340)

net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights","dnn_model/yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320, 320), scale=1/255)

# LOad class lists
classes = []
with open("dnn_model/classes.txt", "r") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)

print("object lists")
print(classes)

# Initialize camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2000)

# button_person = False

def click_button(event, x, y, flags, paraas):
    global button_person
    if event == cv2.EVENT_LBUTTONDOWN:
        button.button_click(x, y)



# Create window
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", click_button)

while True:
    # Get frames
    ret, frame = cap.read()

    # Get active button list
    active_buttons = button.active_buttons_list()
    print("Active button", active_buttons)

    # Object Detection
    (class_ids, scores, bboxes) = model.detect(frame)
    for class_id, score, bbox in zip(class_ids, scores, bboxes):
        (x, y ,w, h) = bbox
        class_name = classes[class_id]

        if class_name in active_buttons:
            cv2.putText(frame, str(class_name), (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (200, 0, 50), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (200, 0, 50), 3)

    # Display buttons
    button.display_buttons(frame)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.realease()
cv2.destroyAllWindows()