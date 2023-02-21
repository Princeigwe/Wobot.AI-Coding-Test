from rest_framework import permissions

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        ''' with this defined permission, the logged in user will be the 
            only person to perform action on a resource, wherever this permission is called
        '''
        return obj.owner == request.user