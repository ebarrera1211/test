from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Board


def index(request):
    boards_list = Board.objects.all()
    template = loader.get_template('webapp/index.html')
    context = {
        'boards_list': boards_list,
    }
    return HttpResponse(template.render(context, request))

def boards(request):
    return HttpResponse("You're looking at board %s." % board_id)