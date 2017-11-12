from django.template import Library

register = Library()


from mooc.courses.models import Enrollment


'''
Esse inclusion_tag converte essa função para uma tag e o django pode usar chamando esse template]  
'''
@register.inclusion_tag('courses/templatetags/my_courses.html')
def my_courses(user):
	enrollments = Enrollment.objects.filter(user=user)
	context = {
		'enrollments': enrollments
	}
	return context

@register.assignment_tag
def load_my_courses(user):
	return Enrollment.objects.filter(user=user)