from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from votes.models import Candidate

class IndexView(generic.ListView):
    template_name = 'votes/index.html'
    context_object_name = 'Top 20 Knesset members'

    def get_queryset(self):

        return Candidate.objects[:20]

