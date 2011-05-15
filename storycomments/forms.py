from django import forms
from django.contrib.comments.forms import CommentForm
from storycomments.models import CommentWithBlockId

class CommentFormWithBlockId(CommentForm):
    block_id = forms.IntegerField()

    def get_comment_model(self):
        return CommentWithBlockId

    def get_comment_create_data(self):
        data = super(CommentFormWithBlockId, self).get_comment_create_data()
        data['block_id'] = self.cleaned_data['block_id']
        return data
