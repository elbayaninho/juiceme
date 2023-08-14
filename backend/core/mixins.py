from rest_framework import permissions

from .permissions import IsCandidateEditorPermission


class CandidateEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsCandidateEditorPermission]