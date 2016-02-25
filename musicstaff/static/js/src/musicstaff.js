/* Javascript for MusicStaffXBlock. */
function MusicStaffXBlock(runtime, element, init_args) {
    
    // the music element
    var melement = element;
    
    // url for async handler to store the music
    var tuneHandlerUrl = runtime.handlerUrl(element, 'store_tune');
    
    
    // on initialization...
    $(function ($) {
    
        // specify where the music and warnings get drawn, disable others
        var opts = {
            canvas:$(melement).find('#abc-paper').get(0),
            renderParams: {},
            warnings:$(melement).find('#abc-warnings').get(0),
            midiParams:{}
        };
    
        // elements for rendering
        var textarea = $(melement).find('#abc-editor');
        var status = $(melement).find('#abc-status');
    
        // initialize the ABC editor
        var editor = new window.ABCJS.edit.EditArea(textarea.get(0));
        var abc_editor = new ABCJS.Editor(editor, opts);
        
        //handle text area event changes manually
        //$(textarea).on('change keyup paste', function(e){ });
    
        //typing js creates typing events, instead of key events
        $(textarea).typing({
        
            //when user starts typing...
            start: function(event, $elem) {
                status.html('typing');
            },
            
            //delay in between key presses allowed before stop event
            delay:1000,
            
            //when user stops typing...
            stop: function(event, $elem) {
            
                status.html('saving...');
                
                //store the given draft of the music
                $.ajax({
                    type: "POST",
                    url: tuneHandlerUrl,
                    data: JSON.stringify({"tune": event.target.value }),
                    success: function() {
                        status.html('saved');                    
                    }
                });
                
            }
         });

    });
}
