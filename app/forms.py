from typing import List

from django import forms


def get_my_choices(tracks):
    choice_list: List = []
    for idx, track in enumerate(tracks):
        choice_list.append((str(idx), track))
    return choice_list


class TracksForm(forms.Form):
    def __init__(self, tracks=None, *args, **kwargs):
        super(TracksForm, self).__init__(*args, **kwargs)
        title = 'Choose a track from this MIDI file'
        self.fields[title] = forms.ChoiceField(choices=get_my_choices(tracks))

