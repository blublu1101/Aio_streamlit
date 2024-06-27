import streamlit as st


def media_elements():
    st.markdown("""
    Documentation: [Media elements](https://docs.streamlit.io/develop/api-reference/media)
    
    # Media elements
    
    ## image
    `st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")`
    """)
    st.image('./static/images/bsh_logo.png', caption='Sunrise by the mountains')

    # audio
    st.markdown("""
    ## audio
    `st.audio(data, format="audio/wav", start_time=0, *, sample_rate=None, end_time=None, loop=False, autoplay=False)`
    """)
    # st.audio("cat-purr.mp3", format="audio/mpeg", loop=True)

    # logo
    st.markdown("""
    ## logo
    `st.logo(image, *, link=None, icon_image=None)`
    """)
    # st.logo('./static/images/bsh_logo.png', link="https://streamlit.io/gallery", icon_image='./static/images/bsh_logo.png')

    HORIZONTAL_RED = './static/images/bsh_logo.png'
    ICON_RED = './static/images/bsh_logo.png'
    HORIZONTAL_BLUE = './static/images/bsh_logo.png'
    ICON_BLUE = './static/images/bsh_logo.png'
    options = [HORIZONTAL_RED, ICON_RED, HORIZONTAL_BLUE, ICON_BLUE]
    sidebar_logo = st.selectbox("Sidebar logo", options, 0)
    main_body_logo = st.selectbox("Main body logo", options, 1)
    st.logo(sidebar_logo, icon_image=main_body_logo)
    st.sidebar.markdown("Hi!")

    # video
    st.markdown("""
    ## video
    `st.video(data, format="video/mp4", start_time=0, *, subtitles=None, end_time=None, loop=False, autoplay=False, 
    muted=False)`
    """)
    # video_file = open('myvideo.mp4', 'rb')
    # video_bytes = video_file.read()
    # st.video(video_bytes)

    VIDEO_URL = "https://www.bilibili.com/video/BV1ym421T7eV/?spm_id_from=333.788.recommend_more_video.0&vd_source=b67bb3c501133ea47f1a4340c6785298"
    st.video(VIDEO_URL, subtitles="./static/vtt/subtitles.vtt")

    # Third-party components
    st.markdown("""
    ## Third-party components
    [Image Comparison](https://github.com/fcakyon/streamlit-image-comparison) \n
    [Streamlit Cropper](https://github.com/turner-anderson/streamlit-cropper) \n
    [Image Coordinates](https://github.com/blackary/streamlit-image-coordinates) \n
    [Streamlit Lottie](https://github.com/andfanilo/streamlit-lottie) \n
    [Streamlit Webrtc](https://github.com/whitphx/streamlit-webrtc) \n
    [Drawable Canvas](https://github.com/andfanilo/streamlit-drawable-canvas) \n
    """)
