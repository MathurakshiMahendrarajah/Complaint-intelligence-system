import gradio as gr
from inference import predict_complaint

def analyze_complaint(text):
    if not text or len(text.strip()) < 10:
        return "", ""

    result = predict_complaint(text)
    return result['category'], result['urgency']

def clear_all():
    return "", "", ""

with gr.Blocks() as demo:
    gr.Markdown("## Customer Complaint Intelligence System")

    gr.Markdown(
        """
**Supported Domain:** Banking & Financial Services complaints  

**Examples:**  
• Credit reporting issues  
• Bank account or card problems  
• Loan, mortgage, or debt collection complaints  
• Money transfers and payment issues  

⚠️ Non-financial complaints (e.g., medical, retail, social media) may produce unreliable results.
"""
    )

    complaint_input = gr.Textbox(
        lines=8,
        placeholder="Enter customer complaint here...",
        label="Customer Complaint"
    )

    with gr.Row():
        submit_btn = gr.Button("Analyze Complaint")
        clear_btn = gr.Button("Clear")

    with gr.Row():
        category_box = gr.Textbox(label="Category", interactive=False)
        urgency_box = gr.Textbox(label="Urgency", interactive=False)

    submit_btn.click(analyze_complaint, inputs=complaint_input, outputs=[category_box, urgency_box])
    clear_btn.click(clear_all, outputs=[complaint_input, category_box, urgency_box])

demo.launch()