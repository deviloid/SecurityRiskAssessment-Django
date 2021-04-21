from django.forms import RadioSelect, CheckboxSelectMultiple


class RadioSelectButtonGroup(RadioSelect):
    """
    This widget renders a Bootstrap 4 set of buttons horizontally instead of typical radio buttons.

    Much more mobile friendly.
    """

    template_name = "widgets/radio_select_button_group.html"

class CheckboxInputGroup(CheckboxSelectMultiple):
    """
    This widget renders a Bootstrap 4 set of buttons horizontally instead of typical radio buttons.

    Much more mobile friendly.
    """

    template_name = "widgets/checkbox_input_group.html"

