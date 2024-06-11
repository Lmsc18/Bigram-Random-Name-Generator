import torch 
import json

with open('itos.json', 'r') as file:
    itos = json.load(file)
itos = {int(k): v for k, v in itos.items()}
P=torch.load("tensor.pt")
def generate():
    ix=0
    sl=[]
    while True:
        p=P[ix]
        ix=torch.multinomial(p,num_samples=1,replacement=True).item()
        sl.append(itos[ix])
        if ix == 0:
            break
    name="".join(sl[:-1])
    return name