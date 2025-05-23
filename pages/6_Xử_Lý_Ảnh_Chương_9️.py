import streamlit as st
from pages.Chuong9 import ConnectedComponent, CountRice
class MultiApp:
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # app = st.sidebar.radio(
        app = st.selectbox(
            'Chọn chủ đề:',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()
app = MultiApp()

st.subheader("""
Bài tập đồ án xử lý ảnh chương 9
""")
st.sidebar.title("Nhóm sinh viên thực hiện:")
st.sidebar.write("""
                - ***Nguyễn Đình Lợi***
                    - **Email:** 22110181@student.hcmute.edu.vn
                - ***Nguyễn Thanh Tính***
                    - **Email:** 22110247@student.hcmute.edu.vn
                """)

app.add_app("Đếm thành phần liên thông của miếng phi lê gà (ConnectedComponent)", ConnectedComponent.app)
app.add_app("Đếm hạt gạo (CountRice)", CountRice.app)


app.run()