import os
from flask import Flask, render_template, request, redirect, url_for
from gradio_client import Client as GradioClient, file
import cv2

# Gradio가 사용할 임시 디렉토리 설정
os.environ["TMPDIR"] = "static/tmp"
os.makedirs("static/tmp", exist_ok=True)

# Flask 애플리케이션 초기화
app = Flask(__name__)

# 업로드된 이미지 및 결과 이미지를 저장할 디렉토리
UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["RESULT_FOLDER"] = RESULT_FOLDER

# Gradio Client 초기화 지연
gradio_client = None

def get_gradio_client():
    """Gradio Client를 필요할 때만 초기화"""
    global gradio_client
    if gradio_client is None:
        gradio_client = GradioClient("Nymbo/Virtual-Try-On")
    return gradio_client

def call_gradio_api(person_image_path, garment_image_path):
    """Gradio API 호출 및 결과 처리"""
    try:
        # Gradio Client 초기화 지연
        client = get_gradio_client()
        result = client.predict(
            dict={"background": file(person_image_path), "layers": [], "composite": None},
            garm_img=file(garment_image_path),
            garment_des="Test Garment Description",
            is_checked=True,
            is_checked_crop=True,
            denoise_steps=30,
            seed=42,
            api_name="/tryon"
        )

        # API 결과 처리
        if result and len(result) > 0:
            try_on_image_path = result[0]

            # 결과 이미지를 읽어와 Flask의 static 디렉토리에 저장
            if os.path.exists(try_on_image_path):
                result_image = cv2.imread(try_on_image_path)
                output_path = os.path.join(app.config["RESULT_FOLDER"], "result.png")
                cv2.imwrite(output_path, result_image)
                return output_path
        return None
    except Exception as e:
        print(f"Error calling Gradio API: {e}")
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # 사용자로부터 업로드된 파일 처리
        person_image = "../" + request.form.get("person_image")
        garment_image = "../" + request.form.get("garment_image")

        if not person_image or not garment_image:
            return "Both person and garment images are required!", 400

        # 파일 저장
        # person_png_path = convert_to_png(person_image, "person_image.png")
        # garment_png_path = convert_to_png(garment_image, "garment_image.png")
        person_png_path = person_image
        garment_png_path = garment_image

        # Gradio API 호출
        result_path = call_gradio_api(person_png_path, garment_png_path)

        if result_path:
            # 결과를 보여주는 페이지로 리디렉션
            return redirect(url_for("result", filename="result.png"))
        else:
            return "Error occurred during the virtual try-on process.", 500

    return render_template("index.html")

@app.route("/result/<filename>")
def result(filename):
    # 결과 이미지를 표시하는 페이지 렌더링
    image_url = url_for("static", filename=f"results/{filename}")
    return render_template("result.html", image_url=image_url)

def convert_to_png(file, output_filename):
    """
    업로드된 이미지를 PNG로 변환하여 저장합니다.
    """
    try:
        # 파일을 임시 경로에 저장
        temp_path = os.path.join(app.config["UPLOAD_FOLDER"], "temp.jpg")
        file.save(temp_path)

        # OpenCV를 사용하여 PNG로 변환
        img = cv2.imread(temp_path)
        png_path = os.path.join(app.config["UPLOAD_FOLDER"], output_filename)
        cv2.imwrite(png_path, img, [cv2.IMWRITE_PNG_COMPRESSION, 9])  # PNG 압축 수준 설정
        os.remove(temp_path)  # 임시 파일 삭제
        return png_path
    except Exception as e:
        print(f"Error converting {file.filename} to PNG: {e}")
        return None

if __name__ == "__main__":
    app.run(debug=True, port=5000)
