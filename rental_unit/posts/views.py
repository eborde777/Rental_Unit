from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from dal import autocomplete

from .models import Post, City, State

from .forms import PostForm

# Create your views here.

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('posts:post_detail', kwargs={'slug': self.object.slug})

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        slug = self.kwargs.get('slug')
        post_obj = Post.objects.get(slug=slug)
        context['post']  = post_obj
        return context

    # def get_object(self, *args, **kwargs):
	# 	request = self.request
	# 	slug = self.kwargs.get('slug')

	# 	instance = get_object_or_404(Product, slug=slug, active=True)

	# 	# pk = self.kwargs.get('pk')
	# 	# instance = Product.objects.get_by_id(pk)
	# 	# if instance is None:
	# 	# 	raise Http404("Product doesn't exists")
	# 	return instance


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'new_state', 'cities')
    success_url = reverse_lazy('post_changeList')


# Manual process to load cities based on State using Ajax, look at post_form.html
# def load_cities(request):
#     state_id = request.GET.get('state')
#     cities = City.objects.filter(state_id=state_id).order_by('city')
#     return render(request, 'posts/city_dropdown.html', {'cities':cities})


# load cities based on State using Ajax, look at post_form.html
class CityAutoComplete(autocomplete.Select2QuerySetView):

    
    def get_queryset(self):
        city_qs = City.objects.all()
        state = self.forwarded.get('state')
        if state:
            city_qs = city_qs.filter(state = state)
            if self.q:
                city_qs = city_qs.filter(city__istartswith=self.q)
        else:
            city_qs = None
        return city_qs

# Below is just creating choice field to datalist on our form
class StateAutoComplete(autocomplete.Select2QuerySetView):
    
    def get_queryset(self):
        state_qs = State.objects.all()
       
        if self.q:
            state_qs = state_qs.filter(state__istartswith=self.q)

        return state_qs
