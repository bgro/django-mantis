from menu import Menu, MenuItem
from django.core.urlresolvers import reverse

Menu.add_item( "mantis_main",
               MenuItem("List & Filter", "",
                        weight = 50,
                        children = (
                            MenuItem("Info Object List (generic filter)", reverse("url.dingos.list.infoobject.generic"), weight = 40 ),
                            MenuItem("Info Object List (filter by ID)", reverse("url.dingos.list.infoobject.by_id"), weight = 50 ),
                        ),

                        )
)

Menu.add_item( "mantis_main",
               MenuItem("Search", "",
                        weight = 50,
                        children = (
                            MenuItem("Fact Search (simple)", reverse("url.dingos.search.fact.simple"), weight = 40 ),
                        ),

                        )
)






