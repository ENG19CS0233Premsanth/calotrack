from django.shortcuts import render,redirect
from calapp.models import calmodel,finalmodel
from calapp.forms import calform,addcalform,dropform

# Create your views here.

def calview(request):
    cal_model=calmodel.objects.all()
    form1=calform()
    food_item = []
    if request.method=="POST":
        form1=calform(request.POST)
        if form1.is_valid():
            print("valid")
            food_name = form1.cleaned_data['name']
            print(food_name)
            # to filter the data
            food_item = calmodel.objects.filter(name=food_name)
            quantity = form1.cleaned_data['quantity']
            for i in food_item:
                i.quantity *= quantity
                i.protien *= quantity
                i.carbs *= quantity
                i.fat *= quantity
                i.nutrients *= quantity

        # print("should have done")
    return render (request,'index.html',{'cal_model':cal_model,'form1':form1,'food_item':food_item})

def addcontent(request):
    soloform=addcalform()
    if request.method=="POST":
        soloform=addcalform(request.POST)
        if soloform.is_valid():
            soloform.save()
        print("should be updated")
    return render(request,'addcontent.html',{'caloform':soloform})

def chview(request):
    form3 = dropform()
    if request.method=="POST":
        form3=dropform(request.POST)
        if form3.is_valid():
            print("valid")
            form3.save()
        food_name=form3.cleaned_data['consumedfood']
        food_item=calmodel.objects.filter(name=food_name).first()
        quant=form3.cleaned_data['quantity']
        print(quant)
        s_instance=finalmodel(name=food_item.name,quantity=quant,protien=food_item.protien * quant,
        carbs= food_item.carbs * quant,
        fat=food_item.fat * quant,
        nutrients=food_item.nutrients,
        vitamins=food_item.vitamins)
        s_instance.save()
    saved=finalmodel.objects.all()
    tp,tc,tf=0,0,0
    for i in saved:
        tp+=i.protien
        tc+=i.carbs
        tf+=i.fat
    
    return render (request,'chcontent.html',{'form3':form3,'saved':saved,'tp':tp,'tc':tc,'tf':tf})

def del1(request,pk):
    res = finalmodel.objects.get(id=pk)
    res.delete()
    return redirect('chcontent')
def new(request,pk):
    data = calmodel.objects.filter(id=pk)
    return render(request,'new.html',{'data':data})
def upd(request,pk):
    res = finalmodel.objects.get(id=pk)
    if request.method=='POST':
        form7 = addcalform(request.POST,instance=res)
        if form7.is_valid():
            form7.save()
    res = finalmodel.objects.get(id=pk)
    form7 = addcalform(instance=res)
    return render(request,'up.html',{'form7':form7})
def favour(request,pk):
    is_fav = False
    res = request.POST.get("food_id")
    var= calmodel.objects.get(id=res)
    if var:
        is_fav=True
    print("res",res)
    return render(request,'index.html',{'if_fav',is_fav})
