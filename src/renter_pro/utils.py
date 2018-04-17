import random
from django.utils.text import slugify

def generate_unique_post_id_and_slug(instance):
    new_post_id = str(random.sample(range(10000000), 1)[0])
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(unique_post_id=new_post_id).exists()
    if qs_exists:
        return generate_unique_post_id_and_slug(instance)
    
    slug = slug_generator(instance, post_id=new_post_id)
    return new_post_id, slug

def slug_generator(instance, new_slug=None, post_id=None):
    if new_slug is not None:
        slug = new_slug
    else:
        title = slugify(instance.title)
        slug = "{title}-{postid}".format(
            title = title,
            postid = post_id
        )
    
    # Klass = instance.__class__
    # qs_exists = Klass.objects.filter(slug=slug).exists()
    # if qs_exists:
    #     new_slug = "{slug}-{postid}".format(
    #         slug = slug,
    #         postid = generate_post_id(instance)
    #     )

    return slug
