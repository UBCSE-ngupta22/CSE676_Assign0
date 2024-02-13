from flask import Flask, render_template, request
import torch
from PIL import Image
from neuralnetwork import CNN, labels
from preprocess import transform

app = Flask(__name__)

model = CNN()
# Load the trained model
model.load_state_dict(torch.load(
    'ngupta22_assignment0_bonus/model/ngupta22_assignment0_bonus.pt'))
model.eval()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the uploaded image file
    file = request.files['image']

    img = Image.open(file)

    img = transform(img).unsqueeze(0)
    
    # Make prediction
    with torch.no_grad():
        output = model(img)
        predicted = labels[output.argmax().item()]

    return render_template('result.html', prediction=predicted)

if __name__ == '__main__':
    app.run(debug=True)
