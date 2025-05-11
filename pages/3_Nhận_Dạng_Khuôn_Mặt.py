import streamlit as st
import cv2 as cv
import numpy as np
import joblib
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import tempfile
import os

st.title('Ứng dụng nhận diện khuôn mặt')
st.sidebar.title("Nhóm sinh viên thực hiện:")
st.sidebar.write("""
                - 1. **Nguyễn Đình Lợi - 22110181**
                - 2. **Nguyễn Thanh Tính - 22110247**
                """)

def str2bool(v):
    return v.lower() in ('yes', 'true', 't', '1')

def load_model(model_path):
    return joblib.load(model_path)

face_detection_model = 'model/face_detection_yunet_2023mar.onnx'
face_recognition_model = 'model/face_recognition_sface_2021dec.onnx'
svc = load_model('model/svc.pkl')
mydict = ['Dat', 'Hieu', 'Loi', 'Tinh', 'Triet']

color_map = {
    'Dat': (0, 255, 0),  
    'Hieu': (0, 0, 255),  
    'Loi': (255, 0, 255),   
    'Tinh': (255, 255, 0), 
    'Triet': (0, 0, 0),
    'Unknown': (128, 0, 128)       
}

detector = cv.FaceDetectorYN.create(face_detection_model, "", (320, 320), 0.9, 0.3, 5000)
recognizer = cv.FaceRecognizerSF.create(face_recognition_model, "")

class RecognizedVideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        h, w, _ = img.shape
        img_resized = cv.resize(img, (320, 320))

        faces = detector.detect(img_resized)
        if faces[1] is not None:
            scale_factor_w = w / 320
            scale_factor_h = h / 320

            for i, face in enumerate(faces[1][:6]):
                face_align = recognizer.alignCrop(img_resized, face)
                face_feature = recognizer.feature(face_align)
                test_predict = svc.predict(face_feature)
                result = mydict[test_predict[0]]

                coords = face[:-1]
                coords[0] *= scale_factor_w
                coords[1] *= scale_factor_h
                coords[2] *= scale_factor_w
                coords[3] *= scale_factor_h
                color = color_map.get(result, color_map['Unknown']) 
                cv.rectangle(img, (int(coords[0]), int(coords[1])), (int(coords[0]+coords[2]), int(coords[1]+coords[3])), color, 2)
                cv.putText(img, result, (int(coords[0]), int(coords[1]) - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
        return img

def process_video_file(video_file):
    # Tạo file tạm thời để lưu video
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_file.read())
    
    # Mở video
    cap = cv.VideoCapture(tfile.name)
    
    # Tạo placeholder để hiển thị video
    stframe = st.empty()
    
    # Xử lý từng frame
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            
        # Resize frame
        frame_resized = cv.resize(frame, (320, 320))
        
        # Phát hiện khuôn mặt
        faces = detector.detect(frame_resized)
        
        if faces[1] is not None:
            scale_factor_w = frame.shape[1] / 320
            scale_factor_h = frame.shape[0] / 320
            
            for face in faces[1][:6]:
                face_align = recognizer.alignCrop(frame_resized, face)
                face_feature = recognizer.feature(face_align)
                test_predict = svc.predict(face_feature)
                result = mydict[test_predict[0]]
                
                coords = face[:-1]
                coords[0] *= scale_factor_w
                coords[1] *= scale_factor_h
                coords[2] *= scale_factor_w
                coords[3] *= scale_factor_h
                
                color = color_map.get(result, color_map['Unknown'])
                cv.rectangle(frame, 
                           (int(coords[0]), int(coords[1])), 
                           (int(coords[0]+coords[2]), int(coords[1]+coords[3])), 
                           color, 2)
                cv.putText(frame, result, 
                          (int(coords[0]), int(coords[1]) - 10), 
                          cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
        
        # Hiển thị frame
        stframe.image(frame, channels="BGR")
    
    # Giải phóng tài nguyên
    cap.release()
    os.unlink(tfile.name)

# Tạo tabs
tab1, tab2 = st.tabs(["Camera", "Video File"])

with tab1:
    st.header("Nhận diện khuôn mặt qua camera")
    webrtc_streamer(key="face-recognition", video_transformer_factory=RecognizedVideoTransformer)

with tab2:
    st.header("Nhận diện khuôn mặt qua video")
    video_file = st.file_uploader("Chọn file video", type=['mp4', 'avi', 'mov'])
    
    if video_file is not None:
        st.video(video_file)
        if st.button("Bắt đầu nhận diện"):
            process_video_file(video_file)