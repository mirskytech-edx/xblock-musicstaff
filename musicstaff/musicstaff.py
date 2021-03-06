"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
import uuid

from xblock.core import XBlock
from xblock.fields import Scope, String
from xblock.fragment import Fragment

from django.utils.translation import ugettext as _


class MusicStaffXBlock(XBlock):
    """
    An XBlock that allows you to compose a song using the ABC music notation.
    
    for reference: http://abcnotation.com/
    """
    
    display_name = String(
        display_name='Music Staff',
        default='Music Staff Question',
        scope=Scope.settings,
        help="Music staff display setting"
    )
    
    
    question = String(
        default="",
        scope=Scope.content,
        help="The question to ask the user to complete."
    )   
    
    
    default_tune_scale = \
"""
M:C
L:1/4
K:C
|]A2 B C'/2D'/2|e/4f/4g/4a/4|]"""
    
    
    tune = String(
        default="", scope=Scope.user_state,
        help="The answer for the user.",    
    )
    
    start_tune=String(
        default=default_tune_scale, scope=Scope.content,
        help="A starting point for the user"
    )
    
    display_tune = "abcdef"

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        """
        This renders the view for the XBlock. It poses a question and asks
        the student to create a musical composition as an answer.
        """
        
        self.display_tune = self.tune if self.tune else self.start_tune
        self.display_question = self.question if self.question else "<span class='error'>no question specified</span>"
        
        # base template
        html = self.resource_string("static/html/musicstaff.html")
        
        frag = Fragment(html.format(self=self))
        
        # stylesheets
        frag.add_css(self.resource_string("static/css/pure/pure-min.css"))
        frag.add_css(self.resource_string("static/css/musicstaff.css"))
        
        # library dependencies
        frag.add_javascript(self.resource_string("static/js/libs/raphael.js"))        
        frag.add_javascript(self.resource_string("static/js/libs/abcjs_editor_9.9.js"))
        frag.add_javascript(self.resource_string("static/js/libs/jquery.typing-0.2.0.min.js"))
        
        # javascript & initialization
        frag.add_javascript(self.resource_string("static/js/src/musicstaff.js"))
        frag.initialize_js('MusicStaffXBlock')
        
        return frag
    
    def studio_view(self, context=None):
        """
        This renders the view for the XBlock. It poses a question and asks
        the author to configure the music-related topic.
        """    
        
        self.display_tune = self.tune if self.tune else self.start_tune
                
        html = self.resource_string("static/html/admin/musicstaff.html")        
        frag = Fragment(html.format(self=self))
                
        frag.add_css(self.resource_string("static/css/admin/musicstaff.css"))        
        frag.add_javascript(self.resource_string("static/js/libs/jquery.typing-0.2.0.min.js"))
        frag.add_javascript(self.resource_string("static/js/src/admin/musicstaff.js"))
        
        frag.initialize_js('MusicStaffStudio')
        
        return frag
    
    
    

    @XBlock.json_handler
    def store_tune(self, data, suffix=''):
        """
        Saves the answer of what the user is composing
        """
        self.tune = data['tune']
        return {"tune": self.tune}
    
    @XBlock.json_handler    
    def studio_edit(self, data, suffix=''):
        print "data %s" % data
        self.question = data.get('question',"")
        self.start_tune = data.get('starttune',"")
        return {'status':"ok"}


    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        
        example_in_24_time = "X:1\\nT:Simple Scale\\nM:C\\nL:2/4\\nK:C\\nC,/2 D,2 E,/4 F,|G, A, B, C|D E F G|A B c d|e f g a|b c' d' e'|f' g' a' b'|]"
        
        return [
            ("MusicStaffXBlock",
             """<musicstaff question="Write a scale of eigth notes."/>
             """),
            ("Multiple MusicStaffXBlock",
             """<vertical_demo>
                <musicstaff question="Compose the first four bars of Mozart's 5th Symphony."/>
                <musicstaff question="Create a riff which exemplifies jazz in the 1940s."/>
                <musicstaff question="Translate the given tune into 4/4 time" start="%s"/>
                </vertical_demo>
             """ % example_in_24_time),
        ]
