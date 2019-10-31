from django.shortcuts import render

# Create your views here.


def wjn_home(req):

    print('前端数据GET', req.GET)
    print('前端数据POST',req.POST)
    print('前端file',req.FILES)
    for item in req.FILES:
        obj = req.FILES.get(item)
        filename = obj.name

        f = open(filename,'wb')
        for line in obj.chunks():
            f.write(line)
        f.close()

    return render(req,'index.html')