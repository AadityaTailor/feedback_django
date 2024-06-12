from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView

# Create your views here.

class ReviewView(View):
    def get(self,req):
        form=ReviewForm()
        return render(req,"reviews/review.html",{"form":form})

    def post(self,req):
        form=ReviewForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")


def review(request):
    if request.method=="POST":
        # existing_model=Review.objects.get(pk=1)
        form=ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            # review=Review(user_name=form.cleaned_data['user_name'],review_text=form.cleaned_data['review_text'],rating=form.cleaned_data["rating"])
            # review.save()
            # print(form.cleaned_data)
            # uname=request.POST["username"]
            return HttpResponseRedirect("/thank-you")
    else:
        form =ReviewForm()
    return render(request,"reviews/review.html",{"form":form})

class ThanksYouView(TemplateView):
    template_name="reviews/thank_you.html"

    def get_context_data(self, **kwargs): 
        context= super().get_context_data(**kwargs)
        context["message"]="This works!"
        return context
    
class ReviewListView(ListView):
    template_name="reviews/review_list.html"
    model=Review
    context_object_name="reviews"

    # def get_queryset(self):
    #     base_query=super().get_queryset()
    #     data=base_query.filter(rating__gt=4)
    #     return data

class SignleReviewView(DetailView):
    template_name="reviews/single_review.html"
    model=Review

    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     context=super().get_context_data(**kwargs)
    #     review_id=kwargs["id"]
    #     selected_review=Review.objects.get(pk=review_id)
    #     context["review"]=selected_review
    #     return context     

# def thank_you(request):
#     return render(request,"reviews/thank_you.html")