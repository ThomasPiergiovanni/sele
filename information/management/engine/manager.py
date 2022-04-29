from datetime import timedelta
from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.utils import timezone

from json import dumps

from authentication.models import CustomUser
from chat.models.discussion import Discussion
from collectivity.models.collectivity import Collectivity
from config.settings import MAPBOX_TOKEN
from proposition.models.proposition import Proposition
from vote.models.voting import Voting


class Manager():
    """Manager manager class.
    """
    def __init__(self):
        pass
    
    def set_home_context(self, context):
        context['mapbox_url'] = self.__set_mapboxurl_json()
        context['vector_layer'] = self.__set_vectorlayer_geojson()
        context['stats_data'] = self.__set_stats_data_json()
        context['all_p_counts'] = self.__set_p_counts(timezone.now())
        context['all_cu_counts'] = self.__set_cu_counts(timezone.now())
        context['all_co_counts'] = self.__set_all_co_counts()
        context['all_v_counts'] = self.__set_all_v_counts()
        return context

    def __set_mapboxurl_json(self):
        data = {
            'url': 'https://api.mapbox.com/styles/v1/thomaspiergiovanni/ckmm3'+
            'kryyu79j17ptmgsmg9c9/tiles/{z}/{x}/{y}?access_token=' +
            MAPBOX_TOKEN
        }
        data_json = dumps(data)
        return data_json
 
    def __set_vectorlayer_geojson(self):
        """
        """
        data_json = serialize(
            'geojson', 
            Collectivity.objects.filter(activity__exact='yes'),
            geometry_field='feat_geom',
            fields=('name','insee_code', 'activity')
        )
        return data_json

    def __set_stats_data_json(self):
        """
        """
        ref_date = self.__set_ref_dates()
        label = self.__set_stats_label(ref_date)
        cu_counts = self.__set_stats_cu_counts(ref_date)
        p_counts = self.__set_stats_p_counts(ref_date)
        stats_data = self.__set_stats_data(label, cu_counts, p_counts)
        data_json = dumps(stats_data)
        return data_json

    def __set_ref_dates(self):
        ref_dates = {
            'r0': None,'r1': None,'r2': None, 'r3': None,
            'r4': None,'r5': None
        }
        ref = timezone.now()
        ref_dates['r0'] = ref.replace(day=1)
        ref_dates['r1'] = self.__set_previous_date(ref_dates['r0'])
        ref_dates['r2'] = self.__set_previous_date(ref_dates['r1'])
        ref_dates['r3'] = self.__set_previous_date(ref_dates['r2'])
        ref_dates['r4'] = self.__set_previous_date(ref_dates['r3'])
        ref_dates['r5'] = self.__set_previous_date(ref_dates['r4'])
        return ref_dates

    def __set_previous_date(self, first_day):
        last_day = first_day - timedelta(days=1)
        previous_date = last_day.replace(day=1)
        return previous_date

    def __set_stats_label(self, ref_date):
        label = {
            'm_0': None,'m_min_1': None,'m_min_2': None, 'm_min_3': None,
            'm_min_4': None,'m_min_5': None
        }
        label['m_0'] = self.__set_mm_yyyy(ref_date['r0'])
        label['m_min_1'] = self.__set_mm_yyyy(ref_date['r1'])
        label['m_min_2'] = self.__set_mm_yyyy(ref_date['r2'])
        label['m_min_3'] = self.__set_mm_yyyy(ref_date['r3'])
        label['m_min_4'] = self.__set_mm_yyyy(ref_date['r4'])
        label['m_min_5'] = self.__set_mm_yyyy(ref_date['r5'])
        return label
    
    def __set_mm_yyyy(self, ref_date):
        mm_yyyy = (
            str(ref_date.date().month) + "-" + str(ref_date.date().year)
        )
        return mm_yyyy

    def __set_stats_cu_counts(self, ref_date):
        cu_counts = {
            'cu_0': None,'cu_min_1': None,'cu_min_2': None, 'cu_min_3': None,
            'cu_min_4': None,'cu_min_5': None
        }
        cu_counts['cu_0'] = self.__set_cu_counts(ref_date['r0'])
        cu_counts['cu_min_1'] = self.__set_cu_counts(ref_date['r1'])
        cu_counts['cu_min_2'] = self.__set_cu_counts(ref_date['r2'])
        cu_counts['cu_min_3'] = self.__set_cu_counts(ref_date['r3'])
        cu_counts['cu_min_4'] = self.__set_cu_counts(ref_date['r4'])
        cu_counts['cu_min_5'] = self.__set_cu_counts(ref_date['r5'])
        return cu_counts

    def __set_cu_counts(self, ref_date):
        cu_counts = (
            CustomUser.objects.filter(date_joined__lte=ref_date).count()
        )
        return cu_counts

    def __set_stats_p_counts(self, ref_date):
        p_counts = {
            'p_0': None,'p_min_1': None,'p_min_2': None, 'p_min_3': None,
            'p_min_4': None,'p_min_5': None
        }
        p_counts['p_0'] = self.__set_p_counts(ref_date['r0'])
        p_counts['p_min_1'] = self.__set_p_counts(ref_date['r1'])
        p_counts['p_min_2'] = self.__set_p_counts(ref_date['r2'])
        p_counts['p_min_3'] = self.__set_p_counts(ref_date['r3'])
        p_counts['p_min_4'] = self.__set_p_counts(ref_date['r4'])
        p_counts['p_min_5'] = self.__set_p_counts(ref_date['r5'])
        return p_counts
    
    def __set_p_counts(self, ref_date):
        p_counts = (
            Proposition.objects.filter(creation_date__lte=ref_date).count()
        )
        return p_counts

    def __set_stats_data(self, label, cu_counts, p_counts):
        data = {
            'labels': [
                str(label['m_min_5']),
                str(label['m_min_4']),
                str(label['m_min_3']),
                str(label['m_min_2']),
                str(label['m_min_1']),
                str(label['m_0'])
            ],
            'cu_counts': [
                str(cu_counts['cu_min_5']),
                str(cu_counts['cu_min_4']),
                str(cu_counts['cu_min_3']),
                str(cu_counts['cu_min_2']),
                str(cu_counts['cu_min_1']),
                str(cu_counts['cu_0'])
            ],
            'p_counts': [
                str(p_counts['p_min_5']),
                str(p_counts['p_min_4']),
                str(p_counts['p_min_3']),
                str(p_counts['p_min_2']),
                str(p_counts['p_min_1']),
                str(p_counts['p_0'])
            ]
        }
        return data
    
    def __set_all_co_counts(self):
        return Collectivity.objects.filter(activity__exact='yes').count()

    def __set_all_v_counts(self):
        return Voting.objects.all().count()
    
    def set_collectivity_dashboard_context(self, request, context):
        context['custom_user_pag_obj'] = (
            self.__set_custom_user_page_obj(request)
        )
        context['custom_users_p_counts'] = (
            self.__set_custom_user_p_counts(request)
        )
        context['proposition_pag_obj'] = (
            self.__set_proposition_page_obj(request)
        )
        context['discussion_pag_obj'] = self.__set_discussion_page_obj(request)
        context['voting_pag_obj'] = self.__set_voting_page_obj(request)
        context['collectivity_p_counts'] = (
            self.__set_collectivity_p_counts(request)
        )
        context['collectivity_cu_counts'] = (
            self.__set_collectivity_cu_counts(request)
        )
        context['collectivity_d_counts'] = (
            self.__set_collectivity_discussion_counts(request)
        )
        context['collectivity_v_counts'] = (
            self.__set_collectivity_voting_counts(request)
        )
        return context

    def __set_custom_user_page_obj(self, request):
        """This method returns Custom User page objects.
        """
        custom_users = self.__get_custom_user_queryset(request)
        return self.__set_page_objects(request, custom_users)

    def __get_custom_user_queryset(self, request):
        """This method returns a queryset of Custom User.
        """
        queryset = (
            CustomUser.objects.filter(
                collectivity_id__exact=request.user.collectivity
            ).order_by('-balance')[:25]
        )
        return queryset
    
    def __set_page_objects(self, request, objects):
        paginator = Paginator(objects, 5)
        page_number = request.GET.get('page')
        page_objects = paginator.get_page(page_number)
        return page_objects

    def __set_custom_user_p_counts(self, request):
        """This method returns a list of dictionnary items. Dictionnary keys 
        are custom user id and the counts of propositions involving that
        same custom user.
        """
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

    def __set_proposition_page_obj(self, request):
        propositions = self.__get_proposition_queryset(request)
        return self.__set_page_objects(request, propositions)

    def __get_proposition_queryset(self, request):
        queryset = (
            Proposition.objects.filter(
                proposition_creator_id__collectivity_id__exact=
                request.user.collectivity
            ).order_by('-creation_date')[:25]
        )
        return queryset

    def __set_discussion_page_obj(self, request):
        discussions = self.__get_discussion_queryset(request)
        return self.__set_page_objects(request, discussions)

    def __get_discussion_queryset(self, request):
        queryset = (
            Discussion.objects.filter(
                discussion_custom_user_id__collectivity_id__exact=
                request.user.collectivity,
                discussion_discussion_type_id__exact=None
            ).order_by('-creation_date')[:25]
        )
        return queryset

    def __set_voting_page_obj(self, request):
        votings = self.__get_voting_queryset(request)
        return self.__set_page_objects(request, votings)

    def __get_voting_queryset(self, request):
        queryset = (
            Voting.objects.filter(
               voting_custom_user_id__collectivity_id__exact=
                request.user.collectivity
            ).order_by('-creation_date')[:25]
        )
        return queryset

    def __set_collectivity_p_counts(self, request):
        """This method returns the counts of propositions for the custom user 
        collectivity.
        """
        p_counts = Proposition.objects.filter(
            proposition_creator_id__collectivity_id=request.user.collectivity
        ).count()
        return p_counts

    def __set_collectivity_cu_counts(self, request):
        """This method returns the counts of custom user for the custom user 
        collectivity.
        """
        cu_counts = CustomUser.objects.filter(
            collectivity_id=request.user.collectivity
        ).count()
        return cu_counts

    def __set_collectivity_discussion_counts(self, request):
        """This method returns the counts of discussion for the custom user 
        collectivity. Only discussion of discussion type == None are returned.
        """
        discussion_counts = Discussion.objects.filter(
            discussion_custom_user_id__collectivity_id=
            request.user.collectivity,
            discussion_discussion_type_id__exact=None,
        ).count()
        return discussion_counts

    def __set_collectivity_voting_counts(self, request):
        """This method returns the counts of voting for the custom user 
        collectivity. Only discussion of discussion type == None are returned.
        """
        voting_counts = Voting.objects.filter(
            voting_custom_user_id__collectivity_id=
            request.user.collectivity,
        ).count()
        return voting_counts
