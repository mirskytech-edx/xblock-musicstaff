"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, String
from xblock.fragment import Fragment


class MirskytechXBlock(XBlock):
    """
    An XBlock that allows you to compose a song using the ABC music notation.
    
    
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.    
    
    question = String(
        default="",
        scope=Scope.user_state,
        help="The question to ask the user to complete."
    )   
    
    
    default_tune_scale = """X:1
T:Simple Scale
M:C
L:1/4
K:C
C, D, E, F,|G, A, B, C|D E F G|A B c d|e f g a|b c' d' e'|f' g' a' b'|]"""
    
    
    tune = String(
        default=default_tune_scale, scope=Scope.user_state,
        help="A simple counter, to show something happening",    
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        This renders the view for the XBlock. It poses a question and asks
        the student to create a musical composition as an answer.
        """
        
        # base template
        html = self.resource_string("static/html/xmirskytech.html")
        
        frag = Fragment(html.format(self=self))
        
        # stylesheets
        frag.add_css(self.resource_string("static/css/pure/pure-min.css"))
        frag.add_css(self.resource_string("static/css/xmirskytech.css"))
        
        # library dependencies
        frag.add_javascript(self.resource_string("static/js/libs/abcjs_editor_2.3-min.js"))
        frag.add_javascript(self.resource_string("static/js/libs/jquery.typing-0.2.0.min.js"))
        
        # javascript & initialization
        frag.add_javascript(self.resource_string("static/js/src/xmirskytech.js"))
        frag.initialize_js('MirskytechXBlock')
        
        return frag

    @XBlock.json_handler
    def store_tune(self, data, suffix=''):
        """
        Saves the answer of what the user is composing
        """
        self.tune = data['tune']
        return {"tune": self.tune}


    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        
        example_in_24_time = """X:1
    T:Simple Scale
    M:C
    L:1/4
    K:C
    C, D, E, F,|G, A, B, C|D E F G|A B c d|e f g a|b c' d' e'|f' g' a' b'|]"""        
        
               
        return [
            ("MirskytechXBlock",
             """<xmirskytech question="Write a scale of eigth notes."/>
             """),
            ("Multiple MirskytechXBlock",
             """<vertical_demo>
                <xmirskytech question="Compose the first four bars of Mozart's 5th Symphony."/>
                <xmirskytech question="Create a riff which exemplifies jazz in the 1940s."/>
                <xmirskytech question="Translate the given tune into 4/4 time" tune="%s"/>
                </vertical_demo>
             """ % example_in_24_time),
        ]
