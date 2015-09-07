from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse #, Http404
#from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.core import serializers

from .models import Election, Result, Country

from jsonview.decorators import json_view
from django.http import JsonResponse
import json


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'elections/index.html'
    context_object_name = 'latest_election_list'

    def get_queryset(self):
        """Return the last five elections."""
        return Election.objects.order_by("-updated_at")[:5]

class DetailView(generic.DetailView):
    model = Election
    template_name = 'elections/detail.html'

# def index(request):
#     """docstring for index(request)"""
#     latest_election_list = Election.objects.order_by("-updated_at")[:5]
#     # template = loader.get_template('elections/index.html')
#     # context = RequestContext(request, {
#     #     'latest_election_list': latest_election_list,
#     # })
#     context = {'latest_election_list': latest_election_list}
#     return render(request, 'elections/index.html', context)
#     #return HttpResponse(template.render(context))
#     #return HttpResponse("Hello World. Welcome to Abatow - the election tracker for Africa")
#
# def detail(request, election_id):
#     """docstring for detail"""
#     # try:
#     #     election = Election.objects.get(pk=election_id)
#     # except Election.DoesNotExist:
#     #     raise Http404("Election does not exist")
#     election = get_object_or_404(Election, pk=election_id)
#
#     #results = election.get()
#     return render(request, "elections/detail.html", {"election": election })
#
def create(request):
    """docstring for detail"""
    # try:
    #     election = Election.objects.get(pk=election_id)
    # except Election.DoesNotExist:
    #     raise Http404("Election does not exist")
    
    return render(request, 'elections/create.html')
    
    # if request.POST['countryname'] is None:
    #     return render(request, 'elections/create.html', {
    #         'error_message': "You didn't add a name for the country "
    #     })
    #
    # c = Country(name=request.POST['country'],
    #         nameslug=sluggify(request.POST['country']), total_registed=request.POST['total_registered'])
    # msg = "Failed to save"
    # if c.save() :
    #     msg = "Saved Country with name %s " (c.name)
    #
    # return render(request, 'elections/create.html', {
    #         'error_message': "You didn't add a name for the country "
    #     })
    #results = election.get()

@json_view
def detail_json(request, election_id):
    """docstring for detail_json"""
    election = get_object_or_404(Election, pk=election_id)
    #response =JsonResponse(election.result_set.all(),safe=False)
    #return response.content
    #return election.result_set.all()
    results = {}
    for er in election.result_set.all():
         results[er.candidate.fullname] = er.votes
    return results
    # return json.dumps(results)
    # response = JsonResponse(results)
    # return response.content
    #return JsonResponse(election.result_set.all().values(), safe=False)
    #data = serializers.serialize("json", election.result_set.all())
    #return HttpResponse(data, content_type='application/json')
