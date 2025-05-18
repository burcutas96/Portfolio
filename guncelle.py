# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

KULLANICI = "burcutas96"
REPO_ISIMLERI = [
    "ReCapProject",
    "GameDemo",
    "FormProject",
    "Portfolio",
    "NewDesignWebSite",
    "HotelSite"
]

from ghapi.all import GhApi
from Renkler   import RENKLER
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("GITHUB_TOKEN")

api = GhApi(token)

# Repo verilerini dict'e çevir (isimlerine göre kolayca erişmek için)
tum_repolar = {
    repo["name"]: repo for repo in api.repos.list_for_user(username=KULLANICI, per_page=100)
    if repo["name"] in REPO_ISIMLERI
}

# Sıralamayı REPO_ISIMLERI listesine göre yap
repolar = [tum_repolar[isim] for isim in REPO_ISIMLERI if isim in tum_repolar]

with open("__index.html", "r", encoding="utf-8") as dosya:
    eldeki_dosya = dosya.read()

eklenecek_metin = "".join(
    f"""
<div class="col-md-6 col-lg-4 d-flex flex-column">
    <div class="repo repo-border d-flex flex-column justify-content-between">
        <div>
            <div class="project-head d-flex">
                <div class="p-icon me-3">
                    <svg aria-hidden="true" height="20" viewBox="0 0 16 16" version="1.1" width="20" data-view-component="true" class="octicon octicon-repo mr-1 color-fg-muted">
                        <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
                    </svg>
                </div>
                <div class="p-repo-title">
                    <a href="https://github.com/{KULLANICI}/{repo.get("name")}" target="_blank">{repo.get("name")}</a>
                </div>
            </div>
            <div class="project-body my-4">
                <p>
                    {repo.get("description") or "~"}
                </p>
            </div>
        </div>
        <div class="project-footer d-flex justify-content-between align-items-end">
            <div class="project-footer-left">
                <span class="repo-language-color" style="background-color:{RENKLER[repo.get("language")]} !important"></span>
                <span class="repo-language text-uppercase">{repo.get("language")}</span>
            </div>
            <div class="project-footer-right">
                <i class="bi bi-star"></i>
                <span class="point me-3">{repo.get("stargazers_count")}</span>
                <svg aria-hidden="true" height="16" viewBox="0 0 24 24" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked blankslate-icon">
                    <path d="M8.75 19.25a3.25 3.25 0 1 1 6.5 0 3.25 3.25 0 0 1-6.5 0ZM15 4.75a3.25 3.25 0 1 1 6.5 0 3.25 3.25 0 0 1-6.5 0Zm-12.5 0a3.25 3.25 0 1 1 6.5 0 3.25 3.25 0 0 1-6.5 0ZM5.75 6.5a1.75 1.75 0 1 0-.001-3.501A1.75 1.75 0 0 0 5.75 6.5ZM12 21a1.75 1.75 0 1 0-.001-3.501A1.75 1.75 0 0 0 12 21Zm6.25-14.5a1.75 1.75 0 1 0-.001-3.501A1.75 1.75 0 0 0 18.25 6.5Z"></path>
                    <path d="M6.5 7.75v1A2.25 2.25 0 0 0 8.75 11h6.5a2.25 2.25 0 0 0 2.25-2.25v-1H19v1a3.75 3.75 0 0 1-3.75 3.75h-6.5A3.75 3.75 0 0 1 5 8.75v-1Z"></path>
                    <path d="M11.25 16.25v-5h1.5v5h-1.5Z"></path>
                </svg>
                <span class="point">{repo.get("forks")}</span>
            </div>
        </div>
    </div>
</div>
""".strip()
    for repo in repolar
)

with open("index.html", "w", encoding="utf-8") as dosya:
    dosya.write(eldeki_dosya.replace("{{ REPOLAR }}", eklenecek_metin))