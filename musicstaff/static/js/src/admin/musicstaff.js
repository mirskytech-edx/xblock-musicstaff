function MusicStaffStudio(runtime, element, init_args) {


    $(element).find('.save-button').bind('click', function() {
        var data = {
            'question': $(element).find('#musicstaff_question').val(),
            'starttune': $(element).find('#musicstaff_starttune').val()
        };
        
        var handlerUrl = runtime.handlerUrl(element, 'studio_edit');
        console.log('runtime url' + handlerUrl);
        $.post(handlerUrl, JSON.stringify(data)).done(function(response) {
            console.log(response);
            window.location.reload(false);
        });

    
    });
    
    $(element).find('.cancel-button').bind('click', function() {
        runtime.notify('cancel', {});
    });


    $(function ($) {
        console.log('initializing js in studio');
    });
   
}