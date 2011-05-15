from django.shortcuts import get_object_or_404, render_to_response
from storyview.models import Story

def index(request):
    story = get_object_or_404(Story, id=1)
    return render_to_response('storyview/index.html', { 'story': story, })
