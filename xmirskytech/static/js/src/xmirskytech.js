/* Javascript for MirskytechXBlock. */
function MirskytechXBlock(runtime, element) {
    
    function tuneUpdated(result) {
        $('#status').html('saved');
    }

    var tuneHandlerUrl = runtime.handlerUrl(element, 'store_tune');

    //$('#abc').on('change keyup paste', function(e){ });
    
    $('#abc-editor').typing({
        start: function(event, $elem) {
            $('#status').html('typing');
        },
        stop: function(event, $elem) {
            $('#status').html('saving...');
            $.ajax({
                type: "POST",
                url: tuneHandlerUrl,
                data: JSON.stringify({"tune": event.target.value }),
                success: tuneUpdated
            });
            
        },
        delay:1000
     });    
    
    
    
    
    $(function ($) {
    
        var music_editor = "abc-editor";    
    
        var opts = {
            paper_id:"paper0",
            midi_id:"midi",
            warnings_id:"warnings",
            renderParams: {},
            midiParams:{}
        };
    
        var abc_editor = new ABCJS.Editor(music_editor, opts);

    });
}
