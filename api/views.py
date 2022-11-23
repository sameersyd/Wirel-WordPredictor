from rest_framework.response import Response
from rest_framework.decorators import api_view
from next_word_prediction import GPT2

gpt2 = GPT2()

def predict(text):
    return gpt2.predict_next(text, 5)

@api_view(['GET'])
def getData(request):
    text = request.GET.get('text')
    predictions = predict(text)
    return Response({'predictions': predictions})