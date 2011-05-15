from storycomments.models import CommentWithBlockId
from storycomments.forms import CommentFormWithBlockId

def get_model():
    return CommentWithBlockId

def get_form():
    return CommentFormWithBlockId
