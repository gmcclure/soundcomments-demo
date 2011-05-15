from django.db import models
from django.contrib.comments.models import Comment

class CommentWithBlockId(Comment):
    block_id = models.PositiveIntegerField()
