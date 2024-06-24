import os 
import gradio as gr
import subprocess

import cv2
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

def infer(image,modeid):

    print(image)

    img_cartoon = pipeline(Tasks.image_portrait_stylization,
                       model=modeid)
    result = img_cartoon(image)
    cv2.imwrite('res.png', result[OutputKeys.OUTPUT_IMG])

    return "./res.png"


def infer_video(video,modeid):

    cmd = rf".\py39\python.exe run_vid.py --video_path={video} --model_name={modeid}"

    res = subprocess.Popen(cmd)

    res.wait()

    

    return "./res.mp4"


with gr.Blocks() as demo:
    title= gr.Markdown("""
    DCT-Net: Domain-Calibrated Translation for Portrait Stylization](https://github.com/menyifang/DCT-Net)
    """
    )
    with gr.Row():
        image = gr.Image(label='图片', type='filepath')
        result = gr.Image(label='Output')
    with gr.Row():
        video_input = gr.Video(label="视频")
        result_video = gr.Video(label='Output')
    with gr.Row():
        modeid = gr.Dropdown(label="风格模型选择",choices=[("日漫风格", "damo/cv_unet_person-image-cartoon_compound-models"),
                                                                ("3D风格", "damo/cv_unet_person-image-cartoon-3d_compound-models"),
                                                                ("手绘风格", "damo/cv_unet_person-image-cartoon-handdrawn_compound-models"),
                                                                ("素描风格", "damo/cv_unet_person-image-cartoon-sketch_compound-models"),
                                                                ("艺术风格", "damo/cv_unet_person-image-cartoon-artstyle_compound-models"),
                                                                ("SD设计风格", "damo/cv_unet_person-image-cartoon-sd-design_compound-models"),
                                                                ("SD插图风格", "damo/cv_unet_person-image-cartoon-sd-illustration_compound-models")
                                                                ],value="damo/cv_unet_person-image-cartoon_compound-models")
                                                                
    run_button = gr.Button('转绘图片')
    run_video = gr.Button('转绘视频')
    run_button.click(fn=infer, inputs=[image,modeid], outputs=result)
    run_video.click(fn=infer_video, inputs=[video_input,modeid], outputs=result_video)
demo.launch(inbrowser=True)