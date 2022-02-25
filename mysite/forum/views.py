from django.shortcuts import render
from .models import Topic, Message

def index(request):
    TOPIC_LIST = Topic.objects.all()
    return render(request, "forum/index.html", {"topics": TOPIC_LIST})

def forum(request, topic):

    topic = Topic.objects.get(name=topic)
    messages = Message.objects.filter(topic=topic).order_by('created_at')

    try:
        message = request.POST["message"]
        Message.objects.create(
            topic=topic,
            content=message,
        )
    except:
        pass

    return render(request, "forum/forum.html", {"messages": messages, "topic": topic})