import torch

# Load the .pth file
file_path = "TrainData.pth"
checkpoint = torch.load(file_path)

# Access and print the model state
model_state = checkpoint["model_state"]

# Print the model state
print(model_state)
