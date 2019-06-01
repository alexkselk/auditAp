from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'main.html')

def upload(request):
    x = ""
    if "x" in request.POST:
        x = request.POST["x"]


    # fl = "request.FILES[];

    fl = 1
    for f in request.FILES:  # myfile is the name of your html file button
         fl = fl + 1

    #     filename = f.name
    #     flist.append(filename)



    return render(request, 'upload.html', {'x': x, 'fl': fl})

