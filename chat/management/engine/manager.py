# pylint: disable=E1101,R0201
"""Chat manager module.
"""
from datetime import date

from django.core.paginator import Paginator
from django.utils import timezone

from chat.models.comment import Comment
from chat.models.discussion import Discussion


class Manager():
    """Chat manager class.
    """

    def create_discussion(self, form, custom_user, discussion_type):
        """Method creating Discussion into DB.
        """
        Discussion.objects.create(
            subject=form.cleaned_data['subject'],
            creation_date=date.today(),
            discussion_custom_user=custom_user,
            discussion_discussion_type=discussion_type
        )

    def set_page_objects_context(self, request, search_input):
        """Method setting Discussion page objects.
        """
        discussions = self.__get_discussion_queryset(request, search_input)
        paginator = Paginator(discussions, 6)
        page_number = request.GET.get('page')
        page_objects = paginator.get_page(page_number)
        return page_objects

    def __get_discussion_queryset(self, request, search_input):
        """Method getting Discussion queryset.
        """
        queryset = None
        if search_input:
            queryset = (
                Discussion.objects.filter(
                    discussion_custom_user_id__collectivity_id__exact=request
                    .user.collectivity,
                    discussion_discussion_type_id__exact=None,
                    subject__icontains=search_input
                ).order_by('-creation_date')
            )
        else:
            queryset = (
                Discussion.objects.filter(
                    discussion_custom_user_id__collectivity_id__exact=request
                    .user.collectivity,
                    discussion_discussion_type_id__exact=None,
                ).order_by('-creation_date')
            )
        return queryset

    def set_session_vars(self, request, search_input):
        """Method setting collectivity discusssion form search to a session
        variable.
        """
        request.session['c_d_v_f_search_input'] = search_input

    def create_comment(self, form, custom_user, id_discussion):
        """Method creating Comment into DB.
        """
        Comment.objects.create(
            comment=form.cleaned_data['comment'],
            creation_date=timezone.now(),
            comment_discussion_id=id_discussion,
            comment_custom_user_id=custom_user.id
        )
