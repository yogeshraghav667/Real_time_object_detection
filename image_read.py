import cv2

path=input("Enter the path of image:-")
print("path==",path)

choose=input("""
1.Gray
2.RGB""")
if choose==1:
    img1 = cv2.imread(path, 0)
    img2=cv2.resize(img1, (1000,700))
    cv2.imshow("converted image", img2)
    k=cv2.waitKey(0)
    if k==ord("S"):
        cv2.imwrite("D:\\output.png",img2)
    else:
        cv2.destroyAllWindows()
    print(img2)
else:
    img1 = cv2.imread(path, 1)
    img2 = cv2.resize(img1, (1000, 500))
    cv2.imshow("converted image", img2)
    k=cv2.waitKey(0)
    if k==ord("S"):
        cv2.imwrite("D:\\output.png",img2)
    else:
        cv2.destroyAllWindows()
    print(img2)

