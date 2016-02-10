# XBlock Music Staff

An XBlock that allows you to compose a song using the [ABC music notation][1].

## Usage

use the `musicstaff` tag to instantiate a music staff xblock.

#### Option: `question` (required)
Description: The question that the user should answer
Example: `"Write a scale of eighth notes.""`

#### Option: `start` (optional)

Description: A starting point for the user's answer

Example: `X:1\\nT:Simple Scale\\nM:C\\nL:2/4\\nK:C\\nC,/2 D,2 E,/4 F,|G, A, B, C|D E F G|A B c d|e f g a|b c' d' e'|f' g' a' b'|]`

## Examples

single music staff xblock instance

     <musicstaff question="Write a scale of eigth notes."/>

multiple music staff xblocks

    <vertical_demo>
        <musicstaff question="Compose the first four bars of Mozart's 5th Symphony."/>
        <musicstaff question="Create a riff which exemplifies jazz in the 1940s."/>
        <musicstaff question="Translate the given tune into 4/4 time" start="X:1\nT:Simple Scale\nM:C\nL:2/4\nK:C\nC,/2 D,2 E,/4 F,|G, A, B, C|D E F G|A B c d|e f g a|b c' d' e'|f' g' a' b'|]"/>
    </vertical_demo>


[1]: http://abcnotation.com/examples
