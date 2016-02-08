/* Javascript for MirskytechXBlock. */
function MirskytechXBlock(runtime, element) {

    function updateCount(result) {
        $('.count', element).text(result.count);
    }

    var handlerUrl = runtime.handlerUrl(element, 'increment_count');

    $('p', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"hello": "world"}),
            success: updateCount
        });
    });
    
    $(function ($) {
        abc_editor = new ABCJS.Editor("abc", { paper_id: "paper0", midi_id:"mid", warnings_id:"warnings" });
        abc_editor.show_midi = false;
    });
}
