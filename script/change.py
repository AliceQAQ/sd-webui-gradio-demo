import gradio as gr
from pathlib import Path
from modules import script_callbacks, shared
import json
import os

# Webui root path
ROOT_DIR = Path().absolute()


def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as GPT_Blocks:
        gr.HTML(
            "<p id='change',style=\"margin-bottom:0.75em\">This is a test.Designed by yuki</p>")
        with gr.Row():
            with gr.Column(scale=45):
                textbox_info = gr.Textbox(label='Something else', value=f'Holy shit',
                                          readonly=True, elem_id="shit_one")
            auto_trans_btn = gr.Button(value="Press to start", variant='primary', elem_id="auto_trans_btn")
            with gr.Column(scale=80):
                change_btn = gr.Button(value="change", variant='primary', elem_id="change_btn")

    return [(GPT_Blocks, "GPT-Lu", "GPT-Lu")]


script_callbacks.on_ui_tabs(on_ui_tabs)