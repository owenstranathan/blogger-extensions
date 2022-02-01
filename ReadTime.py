from math import ceil

from blogger.utils import UserExtension, initializer


class ReadTimeExtension(UserExtension):
    @initializer
    def __init__(self, logger, working_dir, out_dir, site_data, jinja_env):
        pass

    def pre_render_post(self, name, post):
        number_of_words = len(post.body_text.split(" "))
        AVG_WORDS_PER_MIN = 240
        length_to_read = number_of_words / AVG_WORDS_PER_MIN
        post.metadata["readtime"] = "{}{}".format("<" if length_to_read < 1 else "", ceil(length_to_read))
