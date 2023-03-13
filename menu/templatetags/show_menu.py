from ..models import MenusModel
from django import template


register = template.Library()

def render_menu(options, selected=None):
    result = ""
    if selected:
        len_selected = len(selected)
        i = 0
        for path, titles in options.items():
            # Opened options
            if len_selected > i and selected[i] == titles[-1]:
                i+=1
                result += '<div class="option" onclick="location.href=\''+path+'\'">' \
                +'    '*len(titles)+'👉  <span class="select">'+titles[-1]+'</span></div>'
            # Not opened options
            elif len(titles) == 1 or (len_selected >= i and selected[i-1] == titles[-2]) \
            or (len_selected > 1 and selected[i-2] == titles[-2]):
                result += '<div class="option" onclick="location.href=\''+path+'\'">' \
                +'    '*len(titles)+'◽  <span>'+titles[-1]+'</span></div>'
    else:
        # Shows main menu if url is '/' or wrong
        for path, titles in options.items():
            if len(titles) == 1:
                result += '<div class="option" onclick="location.href=\''+path+'\'">' \
                +'    '*len(titles)+'◽  <span>'+titles[-1]+'</span></div>'
    return result

@register.simple_tag
def show_menu(menu_name, url):
    # Only one DataBase request
    menus = MenusModel.objects.all()
    # Select a menu, O(1)
    options = {m.title: m.options for m in menus}[menu_name]
    # options.get(url) determinates a selected option by url, O(1)
    return render_menu(options, options.get(url))
