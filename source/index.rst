.. rtd_sphinx_needs documentation master file, created by
   sphinx-quickstart on Tue May 20 19:50:35 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Sphinx-needs docs
=================

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.

A basic example of rst.
Text written on the next line in rst is rendered as part of the same line above.

Text with a line space above it as rendered as a new paragraph. So in essence there is no way to enforce a new line on demand.

Here is a list:

* a list item
* some more

.. req:: Basic need example
    :id: basic_example1
    :tags: test
    :collapse: true

    A basic example of rst inside a need.
    Text written on the next line in rst is rendered as part of the same line above.

    Text with a line space above it as rendered as a new paragraph. So in essence there is no way to enforce a new line on demand.

    Here is a list:

    * a list item
    * some more


.. req:: Example Requirement
   :id: EX_REQ_001
   :tags: test
   :status: open

   A simple requirement used as example.
   The content supports all kind of Sphinx features, like:

   **Bold** or *italic* text

   Web links, like this `google <https://google.com>`__ link.

   Or even images:    