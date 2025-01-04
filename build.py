import shutil
import os
from pathlib import PurePath

banned_dirs = [
    'Dynamics',
    'Solid_Mechanics',
    'Statics',
    'mathjax',
    'static',
    '_astro'
]

## NAVBAR

_astro = os.listdir('./dist/_astro')

css = [c for c in _astro if c[-4:] == '.css']
js = [j for j in _astro if j[-3:] == '.js']

links_to_replace = {
    "url(/fonts/source-sans-pro/SourceSansPro-Regular.otf": "url(../fonts/source-sans-pro/SourceSansPro-Regular.otf",
    "url(/fonts/source-sans-pro/SourceSansPro-Semibold.otf": "url(../fonts/source-sans-pro/SourceSansPro-Semibold.otf",
    "url(/fonts/source-sans-pro/SourceSansPro-Bold.otf": "url(../fonts/source-sans-pro/SourceSansPro-Bold.otf",
    "url(/fonts/Montserrat-Bold.ttf": "url(../fonts/Montserrat-Bold.ttf"
}

for file in css:
    name = os.path.join('./dist/_astro', file)

    with open(name, 'r') as f:
        data = f.read()

    for wrong, correct in links_to_replace.items():
        data = data.replace(wrong, correct)
    
    with open(name, 'w') as f:
        f.write(data)

home = os.path.join(os.getcwd(), 'dist')

print(css)

def explore_dir_and_move(home, dir):
    #print(os.path.join(home, dir))
    dirs = [d for d in os.listdir(os.path.join(home, dir)) if (os.path.isdir(os.path.join(os.path.join(home, dir), d)) and d not in banned_dirs)]
    htmls = [d for d in os.listdir(os.path.join(home, dir)) if (d == 'index.html')]
    js = [d for d in os.listdir(os.path.join(home, dir)) if (d[-3:] == '.js')]
    #print(dirs, htmls, js)
    if dir != '':
        for h in htmls:
            try:
                
                ppth = PurePath(os.path.join(os.path.join(home, dir), h))
                file_name = ppth.parts[-2]+'.html'
                #print(os.path.join("/".join(ppth.parts[:-2]), file_name))
                shutil.move(os.path.join(os.path.join(home, dir), h), os.path.join("/".join(ppth.parts[:-2]), file_name))
            except Exception as e:
                print(e)
                pass

        for j in js:
            try:
                
                ppth = PurePath(os.path.join(os.path.join(home, dir), j))
                file_name = ppth.parts[-2]+'.js'
                
                if j == 'canvases.js':
                    #print(os.path.join("/".join(ppth.parts[:-2]), file_name))
                    shutil.move(os.path.join(os.path.join(home, dir), j), os.path.join("/".join(ppth.parts[:-2]), file_name))
                else:
                    #print(os.path.join("/".join(ppth.parts[:-2]), j))
                    shutil.move(os.path.join(os.path.join(home, dir), j), os.path.join("/".join(ppth.parts[:-2]), j))
            except Exception as e:
                print(e)
                pass
        
    for d in dirs:
        explore_dir_and_move(home, os.path.join(dir, d))
    return dirs

explore_dir_and_move(home, '')

## PAGES WITH CONTENT
links_to_replace = {
    f"href=\"/_astro/{css[0]}\"": f"href=\"_astro/{css[0]}\"",
    "href=\"/favicon2.png\"":"href=\"favicon2.png\"",
    "href=\"/bootstrap.min.css\"": "href=\"bootstrap.min.css\"",
    "src=\"/bootstrap.min.js\"": "src=\"bootstrap.min.js\"",
    "src=\"/mathjax/tex-chtml.js\"": "src=\"mathjax/tex-chtml.js\"",
    "src=\"/jquery-2.1.4.min.js\"": "src=\"jquery-2.1.4.min.js\"",
    "src=\"/sha1.js\"": "src=\"sha1.js\"",
    "src=\"/static/js/themes.js\"": "src=\"static/js/themes.js\"",
    "src=\"/static/js/simplified_view.js\"": "src=\"static/js/simplified_view.js\"",
    "href=\"/static/css/main.css\"": "href=\"static/css/main.css\"",
    "href=\"/bootstrap-icons.min.css\"": "src=\"bootstrap-icons.min.css\"",
    "href=\"/static/css/lightTheme.css\"": "href=\"static/css/lightTheme.css\"",
    "href=\"/static/css/darkTheme.css\"": "href=\"static/css/darkTheme.css\"",
    "href=\"/static/css/themes.css\"": "href=\"static/css/themes.css\"",
    "href=\"/static/css/sidebar.css\"": "href=\"static/css/sidebar.css\"",
    "href=\"/static/css/tables.css\"": "href=\"static/css/tables.css\"",
}

srcs = [
    'blocki.png',
    'image.png',
    'image2.png',
    'iclicker.png',
    'pl.png',
    'blocki2.png',
    'campuswire.ico',
    'prairietest.ico',
    'box.png',
    'icons/moon.png',
    'icons/sun.png',
    'icons/list.png'
]

for s in srcs:
    links_to_replace[f'src="/{s}"'] = f'src="{s}"'

pages = [p for p in os.listdir('./dist') if p[-4:] == 'html']

print(pages)

for page in pages:
    print(page)
    with open(os.path.join(home, page), 'r') as file:
        data = file.read()

    for wrong, correct in links_to_replace.items():
        print(wrong, correct)
        data = data.replace(wrong, correct)

    for p in pages:
        if p == 'index.html':
            link_name1 = 'href="/"'
            link_name2 = 'href="/#'

            data = data.replace(link_name1, 'href="./index.html"')
            data = data.replace(link_name2, 'href="./index.html#')
        else:
            link_name1 = '"/' + p.replace('.html', '') + '"'
            link_name2 = '"/' + p.replace('.html', '') + '#'

            data = data.replace(link_name2, '"./'+p+'#')
            data = data.replace(link_name1, '"./'+p + '"')
        
    
    with open(os.path.join(home, page), 'w') as file:
        file.write(data)

special_rewrites = {
    "theme_icon.src = (\"/icons/moon.png\");":"theme_icon.src = (\"icons/moon.png\");",
    "theme_icon.src = (\"/icons/sun.png\");":"theme_icon.src = (\"icons/sun.png\");",
    "><p class=\"fw-bold text-center m-0\">": " /><p class=\"fw-bold text-center m-0\">"
}

for page in pages:
    with open(os.path.join(home, page), 'r') as file:
        data = file.read()

    for wrong, correct in special_rewrites.items():
        data = data.replace(wrong, correct)
    
    with open(os.path.join(home, page), 'w') as file:
        file.write(data)

        
        