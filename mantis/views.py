from dingos.view_classes import BasicTemplateView
from braces.views import SuperuserRequiredMixin

from django.contrib import messages

from dingos import DINGOS_TEMPLATE_FAMILY

class MessagingTestView(SuperuserRequiredMixin,BasicTemplateView):
    """
    View for editing the saved searches of a user.
    """

    template_name = 'dingos/%s/details/base_details.html' % DINGOS_TEMPLATE_FAMILY
    title = 'Test of Messaging Framework'

    def get_context_data(self, **kwargs):
        context = super(MessagingTestView, self).get_context_data(**kwargs)
        context['content'] = "If the Messaging Framework works, there should be a green bar above with a message that the framework works!"
        return context


    def get(self, request, *args, **kwargs):
        messages.success(request,"Message framework works!!!")
        return super(BasicTemplateView,self).get(request, *args, **kwargs)

