import simplejson

from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from storycomments.models import CommentWithBlockId
from storyview.models import Story

def comment_form(request, story_id, block_id):
    story = get_object_or_404(Story, id=story_id)
    c = { 'story': story, 'block_id': block_id }
    c.update(csrf(request))
    return render_to_response('storycomments/comment_form.html', c, context_instance=RequestContext(request))

def get_page_comments_as_json(request, story_id):
    comments = CommentWithBlockId.objects.filter(object_pk=story_id).order_by('block_id')
    json_rsp = []
    for comment in comments:
        d = comment.submit_date
        c = {}
        c['user_name'] = comment.user_name
        c['block_id']  = comment.block_id
        c['when']      = d.strftime('%A, %B %d, %Y')
        c['comment']   = comment.comment
        json_rsp.append(c)

    return HttpResponse(simplejson.dumps(json_rsp), content_type='application/json; charset=utf8')
