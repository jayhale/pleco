from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective
from sphinx.util.typing import ExtensionMetadata


class ImplIconDirective(SphinxDirective):
    required_arguments: int = 1

    icons = {
        "pandas": "/assets/impl_icons/pandas-color.svg",
    }

    def run(self) -> list[nodes.Node]:
        impl_type = self.arguments[0]

        icon_image = self.icons.get(impl_type)

        return [nodes.image("", uri=icon_image, alt=impl_type)]


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_directive("impl-icon", ImplIconDirective)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
