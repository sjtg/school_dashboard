from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from classroom.models  import Student, Subject, User

class StudentSignUpForm(UserCreationForm):
	interests = forms.ModelMultipleChoiceField(
		queryset=Subject.objects.all(),
		widget=forms.CheckboxSelectMultiple,
		required=True
	)
	
	class Meta(UserCreationForm.Meta):
		model = User

	@transaction.atomic
	def save(self):

		user = super().save(commit=False)
		user.is_student =True
		user.save()
		student = Student.objects.create(user=user)
		student.interest.add(*self.cleaned_data.get('interests'))
		return user
