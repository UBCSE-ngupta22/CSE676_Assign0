from flask import Flask, render_template, request, jsonify
import torch
import torchvision.transforms as transforms
from PIL import Image

app = Flask(__name__)

# Load your PyTorch model
model = torch.load('your_model.pt', map_location=torch.device('cpu'))
model.eval()

# Define image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# Define the home route to render the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Define a prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the image from the request
        img = Image.open(request.files['image']).convert('RGB')
        img = transform(img).unsqueeze(0)

        # Make a prediction
        with torch.no_grad():
            output = model(img)

        # Process the output as needed
        result = output.argmax().item()

        return render_template('result.html', prediction=result)

    except Exception as e:
        return jsonify({'error': str(e)})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)