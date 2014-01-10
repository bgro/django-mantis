from menu import Menu, MenuItem
from django.core.urlresolvers import reverse

Menu.add_item( "mantis_main",
               MenuItem("List, Filter & Search", "",
                        weight = 50,
                        children = (
                            MenuItem("Info Object List (generic filter)", reverse("url.dingos.list.infoobject.generic"), weight = 40 ),
                            MenuItem("Info Object List (filter by ID)", reverse("url.dingos.list.infoobject.by_id"), weight = 50 ),
                            MenuItem("Fact Search (simple)", reverse("url.dingos.search.fact.simple"), weight = 40 ),
                        ),

                        )
)



Menu.add_item( "mantis_main",
               MenuItem("Saved Filters/Searches", "",
                        weight = 50,
                        children = ()

               )
)


def user_name(request):
    if request.user.is_authenticated():
        return request.user.username
    else:
        return "Not logged in"

def login_name(request):
    if request.user.is_authenticated():
        return "Log out"
    else:
        return "Log in"


Menu.add_item( "mantis_main",
               MenuItem(user_name,
                        "",
                        weight = 50,
                        children = (MenuItem("View user config", reverse("url.dingos.admin.view.userprefs"), weight = 40 ),
                                    MenuItem("Edit saved searches", reverse("url.dingos.admin.edit.savedsearches"), weight = 40 ),
                                    MenuItem(login_name,
                                             reverse("admin:logout"),
                                             weight = 40,
                                             # Seems that the check functionality of simple menu
                                             # is somehow broken.
                                             #check = lambda request: request.user.is_authenticated())
                                    )
                        )

               )
)






