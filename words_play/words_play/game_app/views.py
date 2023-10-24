from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from .models import Word
from .forms import LetterForm
from django.http import HttpResponseRedirect
from .game_play import Puzzle

# Create your views here.

# class GamePage(generic.TemplateView):
#     template_name = "game_app/game_detail.html"
#
#
#     def get(self, request, *args, **kwargs):
#         form = LetterForm()
#         words_list = models.Word.objects.all()
#         return self.render_to_response({'form':form, 'words_list': words_list})
#
#     def post(self, request, *args, **kwargs):
#         form = LetterForm(request.POST)
#         if form.is_valid():
#             # Process the form data here
#             # For example, you can save it to the database
#             pass
#             return HttpResponseRedirect('/game/')
#         return self.render_to_response({'form': form})


class DescriptionList(generic.ListView):
    model = Word
    template_name = 'game_app/descriptions.html'  # Create an HTML template to display the list of groups
    context_object_name = 'descriptions'


class GuessingPage(generic.DetailView):
    model = Word
    template_name = 'game_app/guessing_page.html'  # Create an HTML template to display the group details
    context_object_name = 'puzzle'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     # Add additional variables to the context
    #     context['hidden_word'] = Puzzle(Word.word)
    #     # context['another_variable'] = 'You can pass multiple variables.'
    #
    #     return context
