# theveterangames.co.uk

Static archive site for the Veteran Games and Conference (Registered Charity No. 1202198), replacing the Webflow site. Plain HTML and CSS, no JavaScript framework, no CMS, no build step needed to host.

## Structure

| Path | What it is |
|---|---|
| `index.html` | Home |
| `games.html` | About the Games, plus the Conference (`#conference`) |
| `wellbeing.html`, `team.html`, `partners.html` | About pages |
| `archive/` | Press (6), news (3), letters (9) and short testimonials |
| `app.html` | The Veteran Games app (Military App) |
| `members.html` | Members' web app sign-in (Military App embed) |
| `contact.html`, `privacy.html`, `404.html` | |
| `about/`, `events/`, `press-release/` etc. | Redirect stubs so old Webflow URLs land on the new pages |
| `assets/` | CSS, self-hosted fonts and local images |
| `_src/` | Generator script and source CSS (ignored by GitHub Pages) |

## Editing

Content lives in `_src/build.py`; styles in `_src/style.css`. After changing either:

```
python3 _src/build.py
```

That regenerates every HTML file, the stylesheet, `sitemap.xml`, `robots.txt` and `CNAME`. Commit the results. Small text fixes can also be made directly in the HTML, but they will be overwritten next time the script runs.

## Deploying to GitHub Pages

1. Create a repo and push this folder to `main`.
2. Repo **Settings → Pages**: Source = *Deploy from a branch*, branch `main`, folder `/ (root)`.
3. The `CNAME` file sets the custom domain to `www.theveterangames.co.uk`.
4. At the DNS provider:
   - `www` → `CNAME` → `<github-username>.github.io`
   - apex `theveterangames.co.uk` → `A` records `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` (GitHub then redirects the apex to `www`)
5. Once the certificate is issued, tick **Enforce HTTPS**.
6. Only then cancel the Webflow site plan, so there is no gap.

## Notes

- No forms. The old Webflow forms (contact, legacy gift, group code request) are replaced by email and phone details, so the site processes no personal data itself.
- The Military App embed on `members.html` loads `cdn.militaryapp.org/embed-scripts/embed-app.js`, exactly as the Webflow page did.
- Old URLs redirect via meta-refresh stubs. GitHub Pages serves `/about/the-team` from `about/the-team.html`.
