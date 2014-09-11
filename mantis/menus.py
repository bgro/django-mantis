from menu import Menu, MenuItem
from django.core.urlresolvers import reverse

def user_name(request):
    return "%s, %s" % (request.user.last_name, request.user.first_name)


# User menu when logged in
Menu.add_item( "mantis_main",
               MenuItem(user_name,
                        "",
                        weight = 1000,
                        children = (MenuItem("Edit user config", reverse("url.dingos.admin.view.userprefs"), weight = 10 ),
                                    MenuItem("Edit API Keys", reverse("url.dingos.admin.view.oauthedit"), weight = 20 ),
                                    MenuItem("Edit saved searches", reverse("url.dingos.admin.edit.savedsearches"), weight = 20 ),
                                    MenuItem("Switch Authoring Group", reverse("url.dingos_authoring.action.switch_authoring_group"), weight = 30 ),
                                    MenuItem("Log out",
                                             reverse("admin:logout"),
                                             weight = 100
                                         )
                        ),
                        check = lambda request: request.user.is_authenticated()
               )
)

# Login button if user is not authenticated
#Menu.add_item( "mantis_main",
#               MenuItem("Log In",
#                        reverse("url.mantis.startpage"),
#                        weight = 1000,
#                        check = lambda request: not request.user.is_authenticated()
#               )
#)
