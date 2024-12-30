import os

pages = ["pages/index.astro", "pages/info.astro", "layouts/Layout.astro", "components/Navbar.astro"]

for page in pages:
    url = os.path.join(os.getcwd(), "src", page)

    with open(url, 'r') as f:
        data = f.read()

    data = data.replace('src="/', 'src="/tam251/')

    data = data.replace('href="/', 'href="/tam251/')

    with open(url, 'w') as f:
        f.write(data)