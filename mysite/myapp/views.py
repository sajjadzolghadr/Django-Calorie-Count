from django.shortcuts import render
from .models import Food,Consume
# Create your views here.
def index(request):
    foods = Food.objects.all()

    if request.method == "POST":
        food_id = request.POST.get("food")
        food = Food.objects.get(id=food_id)
        Consume.objects.create(
            user=request.user,
            food_consume=food
        )
    else:
        consumed_food = Consume.objects.filter(user=request.user)
    return render(request, "myapp/index.html", {
        "foods": foods,
        "consumed_food": consumed_food
    })