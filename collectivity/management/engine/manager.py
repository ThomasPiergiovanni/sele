from collectivity.models.postal_code import PostalCode


class Manager():
    """Manager manager class.
    """
    def __init__(self):
        pass

    def get_postal_code(self, collectivity):
        postal_code = PostalCode.objects.get(collectivity_id__exact=collectivity.id)
        return postal_code.postal_code
