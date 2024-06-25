from django.shortcuts import render
from review.forms import reviewForm
from django.http import HttpResponseRedirect
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView

# Create your views here.

class review(View):
    def get(self,request):
        form=reviewForm()
        print("request method is get ")    


        return render(request,"review/review.html",{
           "forms_data":form
    })

        

    def post(self,request):
        form=reviewForm(request.POST)

        if form.is_valid():
            review_data=Review(user_name=form.cleaned_data["user_name"],
                               feedback=form.cleaned_data["feedback"],
                               rating=form.cleaned_data["rating"])
            review_data.save()

            return HttpResponseRedirect("review/thank-you")
        else:
            return render(request,"review/review.html",{
           "forms_data":form
    })


class ThankYouView(TemplateView):
    template_name="review/thank-you.html"

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"]="This is Works!!!!!!"
        return context
    

# class review_list(TemplateView):
#     template_name = "review/review_list.html"

    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews=Review.objects.all()
#         context["reviews_list"]=reviews
#         return context
    




class review_list(ListView):
    template_name = "review/review_list.html"
    model=Review
    context_object_name="reviews_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        data=queryset.filter(rating__gt=4)
        return data



class single_template_view(TemplateView):
    template_name = "review/single_template.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id=kwargs["id"]
        reviews=Review.objects.get(pk=review_id)
        context['review']=reviews
        return context
    

    

    
    









# def review(request):
#     if request.method=="POST":
#         form=reviewForm(request.POST)

#         if form.is_valid():
#             review_data=Review(user_name=form.cleaned_data["user_name"],
#                                feedback=form.cleaned_data["feedback"],
#                                rating=form.cleaned_data["rating"])
#             review_data.save()

#             return HttpResponseRedirect("review/thank-you")
        
       
        
#     else:
#         form=reviewForm()
#         print("request method is get ")    


#     return render(request,"review/review.html",{
#         "forms_data":form
#     })




# def thank_you(request):
#      return render(request,"review/thank-you.html")