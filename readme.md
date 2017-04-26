Django site built following the Django by Example text book, by Antonio Melé
============================================================================

## Chapter One

This chapter takes the reader from a zero to a Django quick-start app. It includes setting up a virtual environment and then using the built-in `startapp` function. A basic post model is created, and then the database migrated. A superuser is created, allowing the user to login to the Django admin interface. Next the Django ORM is introduced, and a basic queryset is manipulated. The basic blog is finished off with an index template, some pagination and an alternative class-based view.

## Chapter Two

Using the blog from Chatper 1, some additional features are added, such as a comment system and email forwarding functionality. I didn't find it necessary to actually setup the SMTP connection for email sending. A tagging system is also setup using django-taggit, which is extended to a 'similar posts' section at the bottom of blog posts. The chapter ends with a reasonably well-featured blog.

## Chapter Three

This chapter starts off by setting up some custom tempalate tags, such as total post count, most recent posts and most commented posts, based on the Django helper functions, such as `simple_tag` and `inclusion_tag`. The next part is to create a custom template filter, and the book chooses markdown, so you are able to write markdown in a blog post and have it rendered properly. After that some supporting website features, such as an xml sitemap and an RSS feed are setup. This is nice, as it gently introduces the reader to machine readable interfaces. The final part of this chapter is quite involved, and requires the installation of Java and Haystack. It produces an asynchronously generated index, which speeds up search. This requires Solr to be runnning, and the schema needs to be manually generated. Personally, I don't think this is really necessary at this stage, and introducing Java might be daunting to the novice.

## Chapter Four

 