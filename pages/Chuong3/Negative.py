import streamlit as st
import numpy as np
from PIL import Image
import cv2
def app():
    def Negative(imgin):
        L = 256
        M, N = imgin.shape[:2]
        imgout = np.zeros((M, N), np.uint8)
        for x in range(M):
            for y in range(N):
                r = imgin[x, y]
                s = L - 1 - r
                imgout[x, y] = s
        return imgout

    st.title('Ứng dụng đảo ngược màu sắc ảnh')

    st.markdown('**Vui lòng tải lên hình ảnh:**')
    img_file_buffer = st.file_uploader("", type=["bmp", "png", "jpg", "jpeg"])
    if img_file_buffer is not None:
        image = Image.open(img_file_buffer)
        st.image(image, caption='Hình ảnh được tải lên', use_container_width=True)

        frame = np.array(image)

        if st.button('Đảo ngược màu sắc'):
            if len(frame.shape) == 3:
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            result_image = Negative(frame)
            st.image(result_image, caption='Kết quả sau khi đảo ngược màu sắc', use_container_width=True)
