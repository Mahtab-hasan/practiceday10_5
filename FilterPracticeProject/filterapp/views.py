
from django.shortcuts import render
import datetime
def home_view(request):
    blogs = {'author': 'rohim' , "age" : 20,'list':["python","django","database","heroalom"],"birthday":datetime.datetime.now(),"val": " " ,"courses":[
        {
            "id" : 1,
            "name": "python",
            "fee" : 500,
        },
        {
            "id" : 2,
            "name": "programming hero",
            "fee": 2000
        },
        {
            "id" : 3,
            "name": "django",
            "fee": 3973
        },
        ]}

    context = {'blogs':blogs}
    return render(request,'filterapp/home.html',context)
