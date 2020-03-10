from django.urls import path
from .views import index, login, pb, sb, checklist, addChecklistItem, completeChecklistItem, deleteChecklistItem


urlpatterns = [
    # wenn Anfrage reinkommt, dann übergebe das der Funktion index aus der views.py
    path('', login, name='login.html'),
    path('home', index, name='index.html'),
    path('pb', pb, name='pb.html'),
    path('sb', sb, name='sb.html'),
    path('checklist', checklist, name='checklist.html'),
    path('addChecklistItem', addChecklistItem, name='addChecklistItem'),
    path('completeChecklistItem/<itemId>', completeChecklistItem, name='completeChecklistItem'),
    path('deleteChecklistItem/<itemId>', deleteChecklistItem, name='deleteChecklistItem')
]
