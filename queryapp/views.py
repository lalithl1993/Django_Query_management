from django.shortcuts import render,get_object_or_404,redirect
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.template import RequestContext
from django.http import HttpResponseRedirect
from queryapp.models import *
from queryapp.forms import *
from django.contrib.auth import authenticate

def index(request):
	return render_to_response("index.html")

# def tr_login(request):
# 	return render_to_response("tr_login.html",context_instance=RequestContext(request))
	#return HttpResponseRedirect('/result/')

# def trloginInfo(request):
# 	try:
# 		if request.POST:
# 			uname=request.POST.get('uname')
# 			pwd=request.POST.get('pwd');
# 			return render_to_response("trloginInfo.html",{'name':uname,'pwd1':pwd},context_instance=RequestContext(request))
# 	except:
# 		pass
# 		return render_to_response("trloginInfo.html",context_instance=RequestContext(request))
# # def all(request):
# 	return render_to_response('all.html',{'StudList':loginInfo.objects.all()})

def tr_add(request):
	form = studentForm(request.POST or None)
	if form.is_valid():
		instance= form.save(commit=False)
		instance.save()
	context={
		"form": form
	}
	return render(request,"tr_add.html",context)


def st_ask(request):
	form = questionForm(request.POST or None)
	if form.is_valid():
		instance= form.save(commit=False)
		instance.save()
	context={
		"form": form
	}
	return render(request,"st_ask.html",context)

# def trloginInfo(request):
# 	try:
# 		return render_to_response('trloginInfo.html',{'members':student.objects.all()},context_instance=RequestContext(request))
# 	except:
# 		pass
# 		return render_to_response('trloginInfo.html',{'message':"fetching failed"},context_instance=RequestContext(request))

def tr_disp(request):
	try:
		return render_to_response('tr_disp.html',{'students':student.objects.all()},context_instance=RequestContext(request))
	except:
		pass
		return render_to_response('tr_disp.html',{'message':"fetching failed"},context_instance=RequestContext(request))

# def tr_question(request):
# 	try:
# 		return render_to_response('tr_question.html',{'questions':question.objects.all()},context_instance=RequestContext(request))
# 	except:
# 		pass
# 		return render_to_response('tr_question.html',{'message':"fetching failed"},context_instance=RequestContext(request))


# def tr_answer(request):
# 	if request.GET:
# 		qid=request.GET.get('qid')
# 		Q=request.GET.get('Q')
# 	form = answerForm(request.POST or None)
# 	if form.is_valid():
# 		instance= form.save(commit=False)
# 		instance.save()
# 	context={
# 		"form": form,
# 		"qid":qid,
# 		"Q": Q,
# 	}
# 	return render(request,"tr_answer.html",context)




# def tr_history(request):
# 	try:
# 		return render_to_response('tr_history.html',{'historys':history.objects.all()},context_instance=RequestContext(request))
# 	except:
# 		pass
# 		return render_to_response('tr_history.html',{'message':"fetching failed"},context_instance=RequestContext(request))



def tr_edit(request,id=None):
	instance=get_object_or_404(student,id=id)
	form = studentForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance= form.save(commit=False)
		instance.save()
		# return HttpResponseRedirect(instance.get_absolute_url(tr_disp))
	context={
		"usn":instance.usn,
		"instance": instance,
		"form":form,
	}
	return render(request,"tr_edit.html",context)

def tr_delete(request,id=None):
	instance=get_object_or_404(student,id=id)
	instance.delete()
	#message.success(request,"Sucessfully Deleted")
	return redirect("/queryapp/tr_disp/")



	# def tr_add(request):
	# form = studentForm(request.POST or None)
	# if form.is_valid():
	# 	instance= form.save(commit=False)
	# 	instance.save()
	# context={
	# 	"form": form
	# }
	# return render(request,"tr_add.html",context)
def tr_answer(request):
	if request.GET:
		qid=request.GET.get('qid')
		Q=request.GET.get('Q')
	instance1=get_object_or_404(question,id=qid)	
	form1= questionForm(request.POST or None, instance=instance1)
	form = answerForm(request.POST or None)
	if form.is_valid():
		#question.objects.status
		instance1=form1.save(commit=False)
		instance= form.save(commit=False)
		instance.save()
		instance1.save()
		return redirect("/queryapp/tr_question/")
	context={
		"form": form,
		"qid":qid,
		"Q": Q,
		"form1":form1
	}
	return render(request,"tr_answer.html",context)


def tr_question(request):
	try:
		return render_to_response('tr_question.html',{'questions':question.objects.filter(status=0)},context_instance=RequestContext(request))
	except:
		pass
		return render_to_response('tr_question.html',{'message':"fetching failed"},context_instance=RequestContext(request))


def tr_history(request):
	try:
		answers=[]
		questionn=[]
		for questions in question.objects.filter(status=1):
			questionn.append(questions.question)
			answers.append(get_object_or_404(answer,qid=questions.id).answer)
			
		print(questionn)
		print(answers)


		context={
		"ques_ans":zip(questionn,answers)
		}
		

		return render_to_response('tr_history.html',context,context_instance=RequestContext(request))
	except:
		pass
		return render_to_response('tr_history.html',{'message':"fetching failed"},context_instance=RequestContext(request))



def st_history(request):
	try:
		answers=[]
		questionn=[]
		for questions in question.objects.filter(status=1):
			questionn.append(questions.question)
			answers.append(get_object_or_404(answer,qid=questions.id).answer)
			
		print(questionn)
		print(answers)


		context={
		"ques_ans":zip(questionn,answers)
		}
		

		return render_to_response('st_history.html',context,context_instance=RequestContext(request))
	except:
		pass
		return render_to_response('tr_history.html',{'message':"fetching failed"},context_instance=RequestContext(request))






# def teacher(request):
# 	try:
# 		return render_to_response('teacher.html',{'message':"welcome"},context_instance=RequestContext(request))
# 	except:
# 		pass
# 		return render_to_response('teacher.html',{'message':"fetching failed"},context_instance=RequestContext(request))

	



def tr_login(request):
	#user=student.objects.all()
		if request.POST:
			name=request.POST.get('uname')
			password=request.POST.get('pwd')
			print(name)
			print(password)
			try:
				user = get_object_or_404(teacher,name=name, password=password)
			except:
				user=None
			if user is not None:
				print("User is valid, active and authenticated")
				return render_to_response("teacher.html",context_instance=RequestContext(request))
				#return redirect('../teacher/')
			else:
				print("The username and password were incorrect.")
			return render_to_response("tr_login.html",context_instance=RequestContext(request))
		else:
			return render_to_response("tr_login.html",context_instance=RequestContext(request))


def st_login(request):
	#user=student.objects.all()
		if request.POST:
			name=request.POST.get('uname')
			password=request.POST.get('pwd')
			print(name)
			print(password)
			try:
				user = get_object_or_404(student,usn=name, password=password)
			except:
				user=None
			if user is not None:
				print("User is valid, active and authenticated")
				return render_to_response("student.html",context_instance=RequestContext(request))
			else:
				print("The username and password were incorrect.")
			return render_to_response("st_login.html",context_instance=RequestContext(request))
		else:
			return render_to_response("st_login.html",context_instance=RequestContext(request))
 	