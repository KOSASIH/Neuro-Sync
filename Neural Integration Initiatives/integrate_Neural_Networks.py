import torch
import torch.nn as nn
from torchvision import models

def integrateNeuralNetworks(model_type, input_size, num_classes):
    """
    Integrate various neural network architectures.
    
    Parameters:
    model_type (str): Type of the neural network architecture.
    input_size (tuple): Input size of the neural network.
    num_classes (int): Number of classes for the classification task.
    
    Returns:
    model (nn.Module): Integrated neural network model.
    """
    
    if model_type == 'resnet18':
        model = models.resnet18(pretrained=True)
        num_ftrs = model.fc.in_features
        model.fc = nn.Linear(num_ftrs, num_classes)
        
    elif model_type == 'resnet34':
        model = models.resnet34(pretrained=True)
        num_ftrs = model.fc.in_features
        model.fc = nn.Linear(num_ftrs, num_classes)
        
    elif model_type == 'resnet50':
        model = models.resnet50(pretrained=True)
        num_ftrs = model.fc.in_features
        model.fc = nn.Linear(num_ftrs, num_classes)
        
    elif model_type == 'resnet101':
        model = models.resnet101(pretrained=True)
        num_ftrs = model.fc.in_features
        model.fc = nn.Linear(num_ftrs, num_classes)
        
    elif model_type == 'resnet152':
        model = models.resnet152(pretrained=True)
        num_ftrs = model.fc.in_features
        model.fc = nn.Linear(num_ftrs, num_classes)
        
    elif model_type == 'vgg11':model = models.vgg11(pretrained=True)
        num_ftrs = model.classifier[6].in_features
        model.classifier[6] = nn.Linear(num_ftrs, num_classes)
        
    elif model_type == 'vgg13':
        model = models.vgg13(pretrained=True)
        num_ftrs = model.classifier[6].in_features
        model.classifier[6] = nn.Linear(num_ftrs, num_classes)
        
    elif model_type == 'vgg16':
        model = models.vgg16(pretrained=True)
        num_ftrs = model.classifier[6].in_features
        model.classifier[6] = nn.Linear(num_ftrs, num_classes)
        
    elif model_type == 'vgg19':
        model = models.vgg19(pretrained=True)
        num_ftrs = model.classifier[6].in_features
        model.classifier[6] = nn.Linear(num_ftrs, num_classes)
        
    else:
        raise ValueError("Invalid model type")

    # Freeze the weights of the pre-trained layers
    for param in model.parameters():
        param.requires_grad = False

    # Add a new layer for the input size
    model.input_layer = nn.Sequential(
        nn.Linear(input_size[0], input_size[1]),
        nn.ReLU(),
        nn.Dropout(0.2)
    )

    # Add the new layer to the model
    model.add_module('input_layer', model.input_layer)

    return model
