import os
import joblib
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ComplaintForm
from .helper_functions import vect


cur_dir = os.path.dirname(__file__)
model = joblib.load(os.path.join(cur_dir, 'models', 'svm.joblib'))


def index(request):
	return render(request, 'main/index.html')


def lodge_complain(request):
	label = {
			-1: 'Negative',
			0: 'Neutral', 
			1:'Positive',
	}
	if request.method == 'POST':
		form = ComplaintForm(request.POST)
		if form.is_valid():
			complaint = form.save(commit=False)
			text = [complaint.complaint]
			X = vect.transform(text)
			complaint.sentiment = label[model.predict(X)[0]]
			if complaint.name == None:
				complaint.name = 'Anonymous'
			complaint.save()
			messages.success(request, 'Complaint sent successfully!')
			return redirect('main:index')
		else:
			messages.error(request, 'Error sending complaint!')
	else:
		form = ComplaintForm()
	context = {
		'form': form,
	}
	return render(request, 'main/lodge_complain.html', context)
