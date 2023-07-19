from django.shortcuts import render
from django.http import *
import base64
from django.views.decorators.csrf import csrf_exempt
import json
# from .utils import decodeImage
# from .predict import ocr
# Create your views here.
def home(request):
        return render(request,'qr.html') 

@csrf_exempt
def capture_image(request):
        # return render(request,'sample.html')
        if request.method == "POST":
                Data = json.load(request)
                image = Data.get('image')
                # data = request.POST.get("image")
                print(image)
                
                if image:
                        # decodeImage(image, clApp.filename)
                        # result = clApp.objectDetection.getPrediction()
                        # Remove the "data:image/png;base64," prefix from the data URL
                        image_data = image.split(",")[1]

                        # Decode the base64-encoded image data
                        decoded_image = base64.b64decode(image_data)

                        # Save the image or perform other processing
                        with open("captured_image.png", "wb") as f:
                                f.write(decoded_image)
                                print("saves")
                                return JsonResponse({"status": "Image received"})
        print("sahil")
        return JsonResponse({"status": "Invalid request"}, status=200)
