import cv2

img = cv2.imread("../../Computer-Vision-with-Python/DATA/00-puppy.jpg")

while True:
    cv2.imshow("Puppy", img)

    # INFO:
    # If we wait for 1ms AND the key pressed is the ESC key,
    # then we break out of the loop
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
