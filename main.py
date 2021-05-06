import cv2
import os

def video2imgs(videoPath, id):
    video = cv2.VideoCapture(videoPath)
    ret = True
    while ret:
        ret, frame = video.read()
        imgId = video.get(1)
        savePath = f"./{videoPath.split('/')[-1]}2imgs"
        if frame is not None:
            frame = cv2.resize(frame, (400, 400))
            if os.path.exists(savePath):
                cv2.imwrite(f"{savePath}/{id}_{str(round(imgId))}.jpg", frame)
            else:
                os.mkdir(savePath)
                cv2.imwrite(f"{savePath}/{id}_{str(round(imgId))}.jpg", frame)
        # cv2.imwrite(f"./{videoPath.split('/')[-1]}2imgs/{id}_{str(imgId)}.jpg", frame) if os.path.exists(savePath) else os.mkdir(savePath)

if __name__ == "__main__":
    videoPath = "./data/video.mp4"
    stuId = "19061206"
    video2imgs(videoPath, stuId)
