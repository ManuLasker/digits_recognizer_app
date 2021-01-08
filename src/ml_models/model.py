import os
import torch
import json
from torchvision import transforms

class DigitClassifier():
    model = None
    preprocess_transforms = None
    
    @classmethod
    def load_model(cls):
        if cls.model is None:
            cls.model = torch.jit.load(os.getcwd()+"/static/mnist_digit.torch.pt",
                                   map_location=torch.device("cpu"))
            stats = json.load(open(os.getcwd()+"/static/stats.json", "r"))
            cls.preprocess_transforms = transforms.Compose(
                transforms=[
                    transforms.Resize((28, 28)),
                    transforms.ToTensor(),
                    transforms.Normalize(mean=stats["mean"],
                                         std=stats["std"])
                ]
            )
        return cls.model, cls.preprocess_transforms
    
    @classmethod
    def predict(cls, im):
        model, preprocess_transforms = cls.load_model()
        tensor_img = preprocess_transforms(im)
        model.eval()
        with torch.no_grad():
            prediction:torch.Tensor = model(tensor_img.unsqueeze(0))
        class_prob, class_idx = prediction.softmax(dim=1).max(dim=1)
        return {"class_name": class_idx.item(),
                "prob": str(float(round(class_prob.item()*100, 1)))+"%"}
        