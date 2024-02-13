import torchvision.transforms as transforms

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Grayscale(),
    transforms.Resize(size=(28, 28), antialias=True),
    transforms.Normalize((0.5,), (0.5,))
])
