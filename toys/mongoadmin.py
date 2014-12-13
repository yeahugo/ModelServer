from mongonaut.sites import MongoAdmin
from toys.models import Toy

class ToyAdmin(MongoAdmin):
    list_fields = ('name','thumbnail','image','create_date')
    search_fields = ('name')

    def has_view_permission(self, request):
        return True

    def has_edit_permission(self, request):
        return True

    def has_add_permission(self, request):
        return True


Toy.mongoadmin = ToyAdmin()
