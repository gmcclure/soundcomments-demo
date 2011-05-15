$(document).ready(function(){
    $.getJSON('/story_comments/1/', function(comments){
        $('section$main article p').each(function(idx){
            var c = 0, comment_list = [];
            block = $(this);

            $.each(comments, function(key, comment){
                if(comment.block_id==block.attr('id')){ 
                    c += 1; 
                    comment_list.push(comment);
                }
            });

            block.append(' <span class="comments">' + c + ' comments</span>');
            block.append('<div class="comment_list" style="display: none;">');
            block.append('</div>');

            converter = new Showdown.converter();

            $.each(comment_list, function(idx, comment){
                block.find('div.comment_list')
                    .append('<div class="comment"><ul><li>' 
                          + comment.user_name                   + ' said on '
                          + comment.when                        + ':</li><li>'
                          + converter.makeHtml(comment.comment) + '</li></ul></div');
            });
        });

        $('span.comments').click(function(){
            form = $('div#comment_form');

            if(form.length > 0){ 
                form.parent().slideUp('normal', function(){
                    form.remove();
                });
            }

            block = $(this).parent().find('div.comment_list');

            if(block.parent().attr('id') != form.parent().parent().attr('id')){
                $.get('/comment_form/1/' + block.parent().attr('id') + '/', function(data){
                    block.append('<div id="comment_form">' + data + '</div>').parent().find('div.comment_list').slideDown();
                    $('#comment_form').formly();
                });
            }
        });
    });
});
