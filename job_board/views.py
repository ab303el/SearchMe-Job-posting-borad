from django.shortcuts import render , HttpResponse , get_object_or_404
from .models import jobPosting , jobcategories

# Create your views here.

def index(request , pk):

    # job = jobPosting.objects.all()
    # print(job)

    # active_postings = jobPosting.objects.filter(is_active=True)
    # job_posting = get_object_or_404(jobPosting , jobcategories = pk , is_active = True)
    job_posting = jobPosting.objects.filter(jobcategories =pk, is_active=True)


    context = {
        'job_postings': job_posting
    }
    return render(request , 'job_board/index.html',context )

def detail(request , pk):
    # job_Posting = jobPosting.objects.get(pk = pk)
    job_posting = get_object_or_404(jobPosting , pk = pk , is_active = True)
    context = {
        'job_postings':job_posting
    }
    return render(request ,'job_board/detail.html' ,context)
def main(request):
    active_postings = jobPosting.objects.filter(is_active=True)
    categories = jobcategories.objects.all()

    context={
        'categories' : categories ,
        'posting': active_postings


    }
    return render(request , 'job_board/main.html' , context)