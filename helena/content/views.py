from django.views.generic import TemplateView, ListView, FormView
from content.models import Genres, Galleries
from content.forms import FeedBackForm


class IndexView(TemplateView):

    """ simple template for index page """

    template_name = 'index.html'


class GenresView(ListView):

    """ list with genres """

    model = Genres
    template_name = 'genres.html'


class GalleryView(ListView):

    """ list with gallery page """

    model = Galleries
    paginate_by = 25
    template_name = 'gallery.html'


class ContactsView(FormView):

    """ simple template for contacts page """

    form_class = FeedBackForm
    template_name = 'contacts.html'
