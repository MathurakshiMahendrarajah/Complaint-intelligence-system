import gradio as gr
from inference import predict_complaint

def analyze_complaint(text):
    if not text or len(text.strip()) < 10:
        return "", ""  # empty outputs for invalid input

    result = predict_complaint(text)
    return result['category'], result['urgency']

def clear_all():
    return "", "", ""  # clears input and outputs

with gr.Blocks() as demo:
    gr.Markdown("## Customer Complaint Intelligence System")
    gr.Markdown("Classifies complaints and flags urgency professionally.")

    with gr.Row():
        complaint_input = gr.Textbox(
            lines=8, 
            placeholder="Enter customer complaint here...",
            label="Customer Complaint"
        )

    with gr.Row():
        submit_btn = gr.Button("Analyze Complaint")
        clear_btn = gr.Button("Clear")

    with gr.Row():
        category_box = gr.Textbox(
            label="Category",
            placeholder="Category will appear here...",
            interactive=False
        )
        urgency_box = gr.Textbox(
            label="Urgency",
            placeholder="Urgency level will appear here...",
            interactive=False
        )

    submit_btn.click(analyze_complaint, inputs=complaint_input, outputs=[category_box, urgency_box])
    clear_btn.click(clear_all, inputs=None, outputs=[complaint_input, category_box, urgency_box])

demo.launch()