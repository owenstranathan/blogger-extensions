import re

from blogger.utils import UserExtension, initializer

class PageForPostExtension(UserExtension):
    @initializer
    def __init__(self, logger, working_dir, out_dir, site_data, jinja_env):
        pass

    def pre_render_post(self, name, post):
        name = name.strip(".md")
        regex = r'\d{4}-\d{2}-\d{2}-'
        datelessName = re.sub(regex, "", name)
        post.metadata["path"] = f"{post.metadata['date'].strftime('%Y')}/{post.metadata['date'].strftime('%m')}/{post.metadata['date'].strftime('%d')}/{datelessName.lower()}.html"
        post.metadata["link"] = f"{self.site_data['url']}/{post.metadata['path']}"

    def should_skip_template(self, name, template, posts):
        if name != "post.html":
            return False
        for name, post in posts.items():
            rendered = template.render(site=self.site_data, post=post, posts=list(posts.values()))
            out = self.out_dir / f"{post.metadata['path']}"
            if not out.parent.exists():
                out.parent.mkdir(parents=True)
            self.logger.info(f"Writing post rendered template to {out}")
            with out.open("w", encoding="utf-8") as outf:
                outf.write(rendered)
        return True

