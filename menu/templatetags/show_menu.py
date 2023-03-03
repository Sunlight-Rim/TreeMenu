from ..models import MenusModel
from django import template


register = template.Library()

def render_menu(menu, selected=None):
    result = ""
    if selected:
        len_selected = len(selected)
        i = 0
        for path, option in menu.items():
            # Opened options
            if len_selected > i and selected[i] == option[-1]:
                i+=1
                result += '<div class="option" onclick="location.href=\''+path+'\'">' \
                +'    '*len(option)+'👉  <span class="select">'+option[-1]+'</span></div>'
            # Not opened options
            elif len(option) == 1 or (len_selected >= i and selected[i-1] == option[-2]) or (len_selected > 1 and selected[i-2] == option[-2]):
                result += '<div class="option" onclick="location.href=\''+path+'\'">' \
                +'    '*len(option)+'◽  <span>'+option[-1]+'</span></div>'
    else:
        # Shows main menu if url is '/' or wrong
        for path, option in menu.items():
            if len(option) == 1:
                result += '<div class="option" onclick="location.href=\''+path+'\'">' \
                +'    '*len(option)+'◽  <span>'+option[-1]+'</span></div>'
    return result

@register.simple_tag
def show_menu(menu_name, url):
    # Only one DataBase request
    menus = MenusModel.objects.all()
    # Define a menu, O(1)
    menu = {o.title: o.options for o in menus}[menu_name]
    # menu.get(url) defines a selected option, O(1)
    return render_menu(menu, menu.get(url))