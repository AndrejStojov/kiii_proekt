from django.shortcuts import render, redirect
from exam.forms import ExamForm
from exam.models import Exam, Profesor, ExamProfesor
def index(request):
    exams=Exam.objects.all().filter(user=request.user)
    if request.GET.get('search') is not None:
        exams=exams.filter(name__icontains=request.GET.get('search'))

    return render(request, 'index.html', {'exams':exams})

def details(request,id):
    exam=Exam.objects.filter(id=id).first()
    examprofesor=ExamProfesor.objects.filter(exam=exam)
    return render(request, 'details.html',{'exam':exam,'profesors':examprofesor})

def add(request):
    form = ExamForm()
    if request.method == 'POST':
        postForm=ExamForm(request.POST,files=request.FILES)
        if postForm.is_valid():
            exam=postForm.save(commit=False)
            exam.image=postForm.cleaned_data['image']
            exam.user=request.user
            exam.save()
            professors=postForm.cleaned_data['profesors']
            if professors:
                profesor_list=professors.split(',')
                for profesor in profesor_list:
                    profesor_obj=Profesor.objects.filter(name=profesor).first()
                    if profesor_obj:
                        ExamProfesor.objects.create(exam=exam,profesor=profesor_obj)
            return redirect('index')

    return render(request, 'add.html',{'form':form})

def edit(request,id):
    exam_instance=Exam.objects.filter(id=id).first()
    form = ExamForm(instance=exam_instance)
    if request.method == 'POST':
        postForm = ExamForm(request.POST, files=request.FILES,instance=exam_instance)
        if postForm.is_valid():
            exam = postForm.save(commit=False)
            exam.image = postForm.cleaned_data['image']
            exam.user = request.user
            exam.save()
            professors = postForm.cleaned_data['profesors']
            if professors:
                profesor_list = professors.split(',')
                for profesor in profesor_list:
                    profesor_obj = Profesor.objects.filter(name=profesor).first()
                    if profesor_obj:
                        ExamProfesor.objects.create(exam=exam, profesor=profesor_obj)
            return redirect('index')

    return render(request, 'add.html', {'form': form})

def delete(request,id):
    exam=Exam.objects.filter(id=id).first()
    if request.method=='POST':
        exam.delete()
        return redirect('index')
    return render(request, 'delete.html', {'exam': exam})