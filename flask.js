from flask import Flask, request, jsonify
import torch
from models import Generator
import os

app = Flask(__name__)

# Load GAN Model
generator = Generator()
generator.load_state_dict(torch.load("generator.pth"))
generator.eval()

@app.route('/generate', methods=['POST'])
def generate_image():
    try:
        noise = torch.randn(1, 100)  # Generate random noise
        fake_image = generator(noise).detach().numpy()
        output_path = "static/generated_image.png"
        # Save image (convert if needed)
        os.makedirs("static", exist_ok=True)
        # Assuming save_image function to convert tensor to image
        save_image(fake_image, output_path)
        return jsonify({"result_image": f"http://localhost:5000/{output_path}"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)