/* Javascript for MusicStaffXBlock. */
function MusicStaffXBlock(runtime, element, init_args) {
    
    var melement = element;
    
    //var uid = element.dataset.usage.replace(/\./g,"-");
    //var editor_id = "abc-editor-" + uid;
    //var status_id = "status-" + uid;
    
    
    function tuneUpdated(result) {
        //$('#'+status_id).html('saved');
    }

    var tuneHandlerUrl = runtime.handlerUrl(element, 'store_tune');
    
    $(function ($) {
    
        var opts = {
            canvas_el:$(melement).find('#abc-paper').get(0),
            renderParams: {},
            midiParams:{}
        };
    
        var textarea = $(melement).find('#abc-editor');
    
        var abc_editor = new ABCJS.Editor(textarea.get(0), opts);
        
        $(textarea).on('change keyup paste', function(e){ });
    
        $(textarea).typing({
            start: function(event, $elem) {
                //$('#'+status_id).html('typing');
            },
            stop: function(event, $elem) {
                //$('#'+status_id).html('saving...');
                $.ajax({
                    type: "POST",
                    url: tuneHandlerUrl,
                    data: JSON.stringify({"tune": event.target.value }),
                    success: tuneUpdated
                });
                
            },
            delay:1000
         });

    });
}
