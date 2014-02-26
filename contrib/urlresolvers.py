from django.core.urlresolvers import reverse
from LazyEvaluation import lazy

reverse_lazy = lambda name=None, *args : lazy(reverse, str)(name, args=args)
