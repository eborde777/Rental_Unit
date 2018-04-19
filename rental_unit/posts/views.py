from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy 
from .models import Post, City

from .forms import PostForm

# Create your views here.

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts:post_detail')

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        instance_id = self.kwargs.get('pk')
        post_obj = Post.objects.get(id=instance_id)
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
    fields = ('title', 'new_state', 'citites')
    success_url = reverse_lazy('post_changeList')


# load cities based on State using Ajax, look at post_form.html
def load_cities(request):
    state_id = request.GET.get('state')
    cities = City.objects.filter(state_id=state_id).order_by('city')
    return render(request, 'posts/city_dropdown.html', {'cities':cities})
