from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
import subprocess

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/generate/")
def generate(data: TextInput):
    text = data.text

    # Read template and replace placeholder
    with open("template.py", "r") as file:
        code = file.read().replace("{{TEXT_PLACEHOLDER}}", text)

    # Save the updated script
    with open("dynamic_scene.py", "w") as file:
        file.write(code)

    # Generate video using Manim
    output_file = "DynamicText.mp4"
    subprocess.run(["manim", "-qm", "-o", output_file, "dynamic_scene.py", "DynamicText"])

    return FileResponse(output_file)