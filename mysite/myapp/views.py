from django.shortcuts import render,redirect
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

    consumed_food = Consume.objects.filter(user=request.user)
    total_calories = 0
    total_carbs = 0
    total_protein = 0
    total_fats = 0

    for c in consumed_food:
        total_calories += c.food_consume.calories
        total_carbs += c.food_consume.carbs
        total_protein += c.food_consume.protein
        total_fats += c.food_consume.fats
    daily_goal = 2000
    progress = min((total_calories / daily_goal) * 100, 100)
    return render(request, "myapp/index.html", {
        "foods": foods,
        "consumed_food": consumed_food,
        "total_calories": total_calories,
        "total_carbs": total_carbs,
        "total_protein": total_protein,
        "total_fats": total_fats,
        "daily_goal": daily_goal,
        "progress": progress,
    })
def delete_consume(request,id):
    consume = Consume.objects.get(id=id)
    if request.method == "POST":
        consume.delete()
        return redirect("/")
    return render(request, "myapp/delete.html",{'consume':consume})