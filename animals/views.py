from django.shortcuts import render
from animals.models import *
from django.views.generic import TemplateView,View
from django.http import JsonResponse
from datetime import datetime
# Create your views here.



class LandingPage(TemplateView):
    template_name="animals/landing.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['category']=list(selectionModel.objects.all().values('animal').distinct())
        context['records']=ResultsModel.objects.all()
        return context


class ExtractBreed(View):
    def post(self,request):
        animal=request.POST.get('animalcategory')
        Breeds=list(selectionModel.objects.filter(animal=animal).values('breed'))
        return render(request,'animals/breeds.html',{'breeds':Breeds})


class AddRecords(View):
    def post(self,request):
        animal=request.POST.get('animalcategory')
        breedoption=request.POST.get('breedtypes')
        Dates=request.POST.get('Datefields')
        provided_date_obj=datetime.strptime(Dates,"%Y-%m-%d")
        todays=datetime.now()

        try:
            iquery=ResultsModel(animal=animal,breed=breedoption,created_date=Dates)
            iquery.save()
            records=ResultsModel.objects.all()
            category=list(selectionModel.objects.all().values('animal').distinct())
            return render(request,"animals/recordsnew.html",{'records':records,'category':category})
        except Exception as e:
            print(e)
