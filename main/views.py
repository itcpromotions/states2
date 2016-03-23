from django.shortcuts import render, render_to_response, redirect 

from django.template import RequestContext 

#from django.http import HttpResponse

from main.models import State, City, StateCapital

#from django.views.decorators.csrf import csrf_exempt
#from django.views.generic import View

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from main.forms import CitySearchForm, CreateCityForm, CityEditForm

from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def city_delete(request, pk):
	City.objects.get(pk=pk).delete()
	
	return redirect('/city_search/')


@login_required
def city_edit (request, pk):

	print 'REQUEST TYPE -- %s' % (request.method)

	request_context = RequestContext(request)
	context ={}

	city = City.objects.get(pk=pk)

	form = CityEditForm(request.POST or None, instance=city)

	context['form'] = form 

	context['city'] = city 
	
	if form.is_valid():
		form.save() 
		return redirect('/state_list/')

	return render_to_response('city_edit.html', context, context_instance=request_context)

# Create your views here

@login_required
def city_create(request):
	request_context = RequestContext(request)
	context = {}

	if request.method =='POST':
		form = CreateCityForm(request.POST)
		context['form'] = form

		if form.is_valid():
			form.save()
			context['fadi'] = "city is saved"
			return render_to_response('city_create.html', context, context_instance=request_context)
		else:
			context['valid'] = form.errors
			return render_to_response('city_create.html', context, context_instance=request_context)

	else:
		form = CreateCityForm()
		context['form'] = form

		return render_to_response('city_create.html', context, context_instance=request_context)

def city_search(request):
	request_context = RequestContext(request)
	context ={}
	if request.method =='POST':
		form = CitySearchForm(request.POST)
		context['form'] = form

		if form.is_valid():
			name = "%s" % form.cleaned_data['name']
			state = form.cleaned_data['state']

			context ['city_list'] = City.objects.filter(name__startswith=name, state__name__startswith=state)

			return render_to_response('city_search.html', context, context_instance=request_context)

		else:
			context['valid'] = form.errors 

			return render_to_response('city_search.html', context, context_instance=request_context)

	else: 
		form = CitySearchForm()
		context["form"] = form
		return render_to_response('city_search.html', context, context_instance=request_context)

def state_list(request):
	context = {}
	states = State.objects.all()
	context['states'] = states
	return render(request, 'state_list.html', context)


class StateListView(ListView):
	model = State
	template_name = "state_list.html"
	context_object_name = "states"

def state_detail(request):
	context = {}
	state = State.objects.get(pk=pk)
	context['state'] = state

	return render(request, 'state_detail.html', context)

class StateDetailView(DetailView):
	model = State
	template_name = "state_detail.html"
	context_object_name = "state"

# @csrf_exempt
# def get_search(request):

# 	get_var = request.GET.get('q', None)

# 	print dir(request)

# 	print request.GET
# 	print request.POST

# 	text_string = ''
# 	text_string += 'Search Term: %s <br>' % get_var
# 	text_string += """

# 	<form action="/get_search/" method="GET">
# 	Search Cities:
# 	<input type='text' name='q'>
# 	<br>

# 	<input type='submit' value="Submit">
	
# 	</form>
	
# 	"""

# 	if get_var != None:
# 		cities = City.objects.filter(name__icontains=get_var)
# 		for city in cities:
# 			text_string += '%s <br>' % city.name

# 	return HttpResponse(text_string)

# @csrf_exempt	
# def get_post(request):

# 	get_var = request.GET.get('q', None)
# 	post_var = request.POST.get('q', None)

# 	print request.GET
# 	print request.POST

# 	text_string = ''
# 	text_string += 'Get Var: %s <br>' % get_var
# 	text_string += 'Post Var: %s <br>' % post_var
# 	text_string += """

# 	<form action="/get_post/" method="POST">
# 	Enter Var:
# 	<input type='text' name='q'>
# 	<br>

# 	<input type='submit' value="Submit">
	
# 	</form>
	
# 	"""

# 	return HttpResponse(text_string)

# def state_detail(request, name):

# 	state = State.objects.get(name=name)

# 	cities = state.city_set.all()

# 	text_string = '<h1><b> %s </h1></b>'  % state.name

# 	for city in cities:
# 		try:
# 			text_string += '<h5>%s </h5>' % city.name
# 		except Exception, e:
# 			print e

# 	return HttpResponse(text_string)

# def state_list(request):

# 	states = State.objects.all()

# 	state_list = []

# 	for state in states:
# 		state_list.append("<a href='/state_detail/%s'> %s </a></br>" % (state.name, state.name))

# 	return HttpResponse(state_list)	

# #def detail_view(request, pk):
# 	#speed_object = State.objects.get (pk=pk)
# 	#context = {}
# 	#context['speed_object'] = speed_object

# 	#return render_to_response('detail_view.html', context, context_instance=RequestContext(request))


# def capital_list(request):

# 	capitals = StateCapital.objects.all()

# 	capital_list = []
	
# 	for capital in capitals:
# 		capital_list.append("<h1>Capital of the State:</h1> %s </br>" % (capital.name))
# 	return HttpResponse(capital_list)


# def state_capital_list(request):

# 	capitals = StateCapital.objects.all()

# 	state_capital_list = []


# 	for capital in capitals:

# 		state_capital_list.append("<h3> State Name: %s <h3> <h4> Capital Name: %s </h4> </br>" % (capital.state.name, capital.name))

# 	return HttpResponse(state_capital_list)	

# def state_capital_list_two(request):

# 	states = State.objects.all()

# 	state_capital_list_two = []

# 	for state in states:

# 		state_capital_list_two.append("State: %s and Capital: %s </br>" % (state.name, state.statecapital.name))

# 	return HttpResponse(state_capital_list_two)	



# #def detail_view(request, pk):
# 	#speed_object = State.objects.get (pk=pk)
# 	#context = {}
# 	#context['speed_object'] = speed_object

# 	#return render_to_response('detail_view.html', context, context_instance=RequestContext(request))