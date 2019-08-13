from django.contrib.sites.shortcuts import get_current_site
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from datetime import date, time, datetime
from ..models import SeenDetails, AssignLinks
from django.contrib.sites.models import Site


## Middleware developed by baig052@gmail.com

class FilterIPMiddleware(MiddlewareMixin):
    # Check if client IP is allowed
    def process_request(self, request):
        ip = self.get_client_ip(request)
        path = request.get_full_path()

        # path_check = path.split("/")
        # path_check = list(filter(None, path_check))  # fastest

        return self.validate_path(path, ip, request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def validate_path(self, path, ip, request):
        # if not path.split('/')[-2] in ['/admin_dashboard', '/admin_login', '/admin', '/admin_dashboard/',
        #                                '/admin_login/', '/admin/']:
        if '/lawyer/' in path and 'admin' not in path:
            url_check = AssignLinks.objects.filter(link_id__endswith=path)
            if url_check.exists():
                assign_obj = url_check.first()
                assign_link_id = getattr(assign_obj, "id")
                if not SeenDetails.objects.filter(ip=ip, assign_links_id=assign_link_id).exists():
                    if assign_obj.left:
                        assign_obj.left = assign_obj.left - 1
                        assign_obj.used = assign_obj.used + 1
                        assign_obj.save()
                        seen_details = SeenDetails()
                        seen_details.assign_links_id = assign_link_id
                        seen_details.ip = ip
                        seen_details.date = str(date.today())
                        seen_details.time = str(datetime.now().time())
                        seen_details.url_seen = path
                        seen_details.save()
                        return
                    else:
                        return HttpResponse("You are out of Views", status=403)
                else:
                    raw_seen = SeenDetails.objects.get(ip=ip, assign_links_id=assign_link_id)
                    raw_seen.date = str(date.today())
                    raw_seen.time = str(datetime.now().time())
                    raw_seen.url_seen = path
                    raw_seen.save()
                    return
            else:
                return HttpResponse("Please buy views first.", status=403)
        else:
            return
