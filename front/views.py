# from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.list import ListView


from . import forms, models


class PictureListView(ListView):
    model = models.Picture
    paginate_by = 20


class PictureCreateView(View):
    form_class = forms.PictureForm
    success_url = reverse_lazy('pictures:list')
    template_name = 'front/picture_create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            context = {'form': form}
            return render(request, self.template_name, context)


# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'front/simple_upload.html', {
#             'uploaded_file_url': uploaded_file_url
#         })
#     return render(request, 'front/simple_upload.html')


# def model_form_upload(request):
#     if request.method == 'POST':
#         form = forms.PictureForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('pictures:list')
#     else:
#         form = forms.PictureForm()
#     context = {'form': form}
#     return render(request, 'front/picture_create.html', context)
