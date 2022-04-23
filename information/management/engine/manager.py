from django.core.paginator import Paginator

from authentication.models import CustomUser
from proposition.models.proposition import Proposition


class Manager():
    """Manager manager class.
    """
    def __init__(self):
        pass

    def set_cus_use_pag_obj_context(self, request):
        custom_users = self.__get_custom_user_queryset(request)
        paginator = Paginator(custom_users, 5)
        page_number = request.GET.get('page')
        page_objects = paginator.get_page(page_number)
        return page_objects

    def __get_custom_user_queryset(self, request):
        queryset = (
            CustomUser.objects.filter(
                collectivity_id__exact=request.user.collectivity
            ).order_by('-balance')[:25]
        )
        return queryset

    def set_custom_users_propositions_counts_context(self, request):
        custom_user_p_counts = []
        custom_users = CustomUser.objects.filter(
            collectivity_id=request.user.collectivity
        )
        for custom_user in custom_users:
            custom_user_p_count = {'id': None, 'count':None}
            proposition_count = (
                Proposition.objects.filter(
                    proposition_creator_id=custom_user.id
                ).count()|
                Proposition.objects.filter(
                    proposition_taker_id=custom_user.id
                ).count()
            )
            custom_user_p_count['id'] = custom_user.id
            custom_user_p_count['count'] = proposition_count
            custom_user_p_counts.append(custom_user_p_count)
        return custom_user_p_counts
