/* Javascript for MusicStaffXBlock. */
function MusicStaffXBlock(runtime, element, init_args) {
    
    
    var uid = element.dataset.usage.replace(/\./g,"-");
    var editor_id = "abc-editor-" + uid;
    var status_id = "status-" + uid;
    
    
    function tuneUpdated(result) {
        //$('#'+status_id).html('saved');
    }

    var tuneHandlerUrl = runtime.handlerUrl(element, 'store_tune');
    
    $(function ($) {
    
        var opts = {
            paper_id:"paper-"+uid,
            midi_id:"midi-"+uid,
            warnings_id:"warnings-"+uid,
            renderParams: {},
            midiParams:{}
        };
    
        var abc_editor = new ABCJS.Editor(editor_id, opts);
        
        $('#'+editor_id).on('change keyup paste', function(e){ });
    
        $('#'+editor_id).typing({
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
