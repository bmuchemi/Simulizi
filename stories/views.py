from django.shortcuts import render, get_object_or_404
from .models import Story,Poem,Sport
from .api import fetch_data_from_api

# Create your views here.
def api(request):
    api_data = fetch_data_from_api()
    # Process and use api_data in your view logic
    return render(request, 'hadithi/sports_view.html', {'api_data': api_data})

def home(request):
    return render(request,'hadithi/home.html')

def about(request):
    stories = Story.objects.all()
    return render(request, 'hadithi/all_stories.html', {'stories': stories})

def story_list(request):
    stories = Story.objects.all()
    return render(request, 'hadithi/stories.html', {'stories': stories})

def poem_list(request):
    poems = Poem.objects.all()
    return render(request, 'hadithi/poems.html', {'poems':poems})

def story_detail(request, story_id): 
    story = get_object_or_404(Story, id=story_id)
    return render(request, 'hadithi/single_stories.html', {'story': story})

def poem_detail(request, poem_id): 
    poem = get_object_or_404(Poem, id=poem_id)
    return render(request, 'hadithi/single_poems.html', {'poem': poem})

def sports_view(request):
    sport = Sport.objects.all()
    return render(request,'hadithi/sports_view.html',{'sport':sport})

def sports(request, desk_id):
    sports = get_object_or_404(Sport, id=desk_id)
    return render(request, 'hadithi/sportsdesk.html',{'sports': sports})