# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth import login

from django.shortcuts import redirect

from django.views.generic import CreateView

from .forms import StudentSignUpForm
from . models import User

# Create your views here.


class StudentSignUpView(CreateView):
	model = User
	form_class = StudentSignUpForm
	template_name = 'registration/signup_form.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'student'
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return redirect('students:quiz_list')
