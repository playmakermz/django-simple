from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, 'home/index.html')

def power(request):
    fin = 0
    if request.method == 'POST':
        x = request.POST['x']
        y = request.POST['y']
        print(x, y)

        fin = int(x) ** int(y)

    main = {
        'fin':fin,
        'title':'perpangkatan / power',
        'judul':'perpangkatan / power',
    }
    return render(request, 'hitung/index.html', main)

def division(request):
    fin = 0
    if request.method == 'POST':
        x = request.POST['x']
        y = request.POST['y']
        print(x, y)

        fin = int(x) // int(y)
            

    main = {
        'fin':fin,
        'title':'akar / floor division',
        'judul':'akar / floor division',
        
    }

    return render(request, 'hitung/index.html', main)