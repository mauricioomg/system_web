from django.contrib.auth.models import User
from django.views import generic
from django.db.models import Q


""" HOME """
class ListUsersView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'list_users'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        object_list = User.objects.all()
        if query is not None:
            object_list = object_list.filter(Q(username__icontains=query))
        return object_list.order_by('username')
""" END_HOME """