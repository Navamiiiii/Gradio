import gradio as gr

# Close any previously running Gradio instances
gr.close_all()

# Define the core logic function
def greet(name):
    return "Hello, " + name + "!"

# Create the Gradio interface
demo = gr.Interface(
    fn=greet,
    inputs=[gr.Textbox(label="Name")],
    outputs=[gr.Textbox()],
)

# Launch the local web server
demo.launch()
