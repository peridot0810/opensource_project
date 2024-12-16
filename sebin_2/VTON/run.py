import os
os.environ["TMPDIR"] = "/home/her/s/VTON/tmp"

from gradio_client import Client, file

# Client 인스턴스 생성
client = Client("Nymbo/Virtual-Try-On")

# API 호출 및 결과 출력
result = client.predict(
    dict={"background": file('/home/her/s/VTON/background_image/001-woman.png'), "layers": [], "composite": None},
    garm_img=file('/home/her/s/VTON/garment_image/001-black_mustang.png'),
    garment_des="Hello!!",
    is_checked=True,
    is_checked_crop=True, # 이미지 사이즈 유지
    denoise_steps=30,
    seed=42,
    api_name="/tryon"
)
print(result)
#print(client._info())
