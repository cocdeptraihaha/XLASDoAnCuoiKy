import streamlit as st
from streamlit_option_menu import option_menu
import base64

st.set_page_config(
    page_title="Đồ án xử lý ảnh số",
    page_icon="📷",
    layout="wide", 
)

def get_image_as_base64(path):
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

image_base64 = get_image_as_base64("background_img.jpg")



st.title("Xử Lý Ảnh Số - Đồ án cuối kỳ📖")

#menu
with st.sidebar:
    selected = option_menu(
        "Danh mục",
        ["Trang chủ", "Nội dung Đồ án", "Liên hệ"],
        icons=["house", "book", "envelope"],
        menu_icon="cast",
        default_index=0,
    )


if selected == "Trang chủ":
    st.subheader("GVHD: ThS. Trần Tiến Đức")
    st.markdown("**Lớp:** ***DIPR430685_Xu ly anh so_ Nhom 07CLC***")
    st.markdown("**Nhóm sinh viên thực hiện:**")
    st.markdown("""
        - ***Nguyễn Đình Lợi*** - **22110181**
        - ***Nguyễn Thanh Tính*** - **22110247**
    """)
    st.markdown("""
    <div style="color: red; font-size: 20px;">
        <b>Lời cảm ơn</b>
    </div>
    """, unsafe_allow_html=True)
    st.write("""
        Xin cảm ơn thầy **ThS. Trần Tiến Đức** đã tận tình hướng dẫn và giúp đỡ chúng em trong quá trình học 
             tập và thực hiện đồ án. Chúc thầy thật nhiều sức khỏe và niềm vui.
    """)
    st.image("background_img.jpg", caption="Digital Image Processing", use_container_width=True)


elif selected == "Nội dung Đồ án":
    st.header("Nội dung báo cáo đồ án cuối kỳ: Xử lý ảnh số")
    st.write("""
        Đồ án cuối kỳ môn học Xử lý ảnh số gồm các phần sau:
        1. **Nhận dạng khuôn mặt**
        - Nhận dạng khuôn mặt 5 bạn trong khung hình, sử dụng model onnx.
        <br>
        2. **Nhận dạng 5 loại đối tượng**
        - Nhận dạng 5 loại trái cây.
             <br>
        3. **Xử lý ảnh**
        - Xử lý ảnh chương 3.
        - Xử lý ảnh chương 4.
        - Xử lý ảnh chương 9.
        <br> 
        4. **Bài tập làm thêm**
        - Nhận dạng các đối tượng trong ảnh, sử dụng model onnx.
        
    """, unsafe_allow_html=True)

elif selected == "Liên hệ":
    st.header("Thông tin liên hệ nhóm sinh viên thực hiện đồ án cuối kỳ")
    st.write("""
    Nếu cần liên hệ với nhóm sinh viên chúng em, thầy có thể liên lạc qua các địa chỉ sau:

    - ***Nguyễn Đình Lợi***
        - **Email:** 22110181@student.hcmute.edu.vn
        - **Số điện thoại:** 0362434303

    <br>

    - ***Nguyễn Thanh Tính***
        - **Email:** 22110247@student.hcmute.edu.vn
        - **Số điện thoại:** 
    """, unsafe_allow_html=True)