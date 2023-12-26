from models.ImageGener import StyleGan
from models.TTS import tacotron
model = StyleGan()
model2= tacotron()

for epoch in epochs:
    for idx, data in enumerate(dataloader):


# 학습 완료되면 model.pt가 저장.