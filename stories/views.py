from django.shortcuts import render, get_object_or_404
from .models import Story,Poem

# Create your views here.
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