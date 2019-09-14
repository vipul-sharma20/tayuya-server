import traceback

from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from app.utils import divide_notes

from tayuya import MIDIParser
from tayuya import Tabs


@require_http_methods(['GET', 'POST'])
def home(request):
    """
    Landing Page
    """
    if request.method == 'POST':
        midi_file = request.FILES['midi']

        # store file in tmp storage
        fs = FileSystemStorage()
        filename = fs.save(midi_file.name, midi_file)

        # set some session data
        request.session['file_name'] = filename
        request.session['midi_file_name'] = midi_file.name

        mid = MIDIParser(settings.MEDIA_ROOT + filename)

        # find all tracks in MIDI file
        tracks = mid.midi_file.tracks
        data = [track.name for track in tracks]

        return render(request, 'tracks.html', {'data': data})

    else:
        return render(request, 'index.html')


@require_http_methods(['GET', 'POST'])
def render_tabs(request):
    """
    Render Tabs
    """
    if request.method == 'POST':
        filename = request.session['file_name']
        midi_file_name = request.session['midi_file_name']

        channel = int(request.POST.get('track', 0))

        try:
            mid = MIDIParser(settings.MEDIA_ROOT + filename, channel)
            tabs = Tabs(mid.notes_played(), mid.get_key())
            to_play = [tabs.generate_notes(tabs.find_start())]

            alternatives: list = []

            for alternative in to_play:
                alternatives.append(list(divide_notes(alternative, 30)))

            return render(request, 'render.html',
                          {'alternatives': alternatives,
                           'name': midi_file_name.split('.')[0]})
        except:
            traceback.print_exc()
            return render(request, '500.html')
    else:
        return redirect('home_view')
