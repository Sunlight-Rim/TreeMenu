from ..models import MenusModel
from django import template


register = template.Library()

@register.simple_tag
def show_menu(menu_name, url):
    result = ""
    # Only one DataBase request
    menus = MenusModel.objects.all()
    # Select a menu
    menu = { o.title: o.options for o in menus }[menu_name]
    url = url.split('/'); urllen = len(url); i = 1
    for path, option in menu.items():
        # Opened options
        if path.count('/') >= i and urllen > i and path.split('/')[i] == url[i]:
            i+=1
            result += '<div class="option" onclick="location.href=\''+path+'\'">' \
            +'    '*len(option)+'👉  <span style="color: #5da6ff">'+option[-1]+'</span></div>'
        # Not opened options
        else:
            result += '<div class="option" onclick="location.href=\''+path+'\'">' \
            +'    '*len(option)+'💠  <span>'+option[-1]+'</span></div>'
    return result