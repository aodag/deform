Deform
======

.. :mod:`deform` is a Python HTML form generation library.

:mod:`deform` は Python の HTMLフォーム生成ライブラリの１つです。

.. The design of :mod:`deform` is heavily influenced by the `formish
.. <http://ish.io/projects/show/formish>`_ form generation library.  Some
.. might even say it's a shameless rip-off; this would not be completely
.. inaccurate.  It differs from formish mostly in ways that make the
.. implementation (arguably) simpler and smaller.

:mod:`deform` の設計は、 `formish <http://ish.io/projects/show/formish>`_ 
フォーム生成ライブラリから大きく影響を受けています。
パクリと言われるかもしれませんが、それは正確ではありません。
formish からの大きな違いは、実装がシンプルかつ小さくなっていることです。

.. :mod:`deform` uses :term:`Colander` as a schema library,
.. :term:`Peppercorn` as a form control deserialization library, and
.. :term:`Chameleon` to perform HTML templating.

:mod:`deform` は、 :term:`Colander` をスキーマライブラリとして使います。
:term:`Peppercorn` をフォームコントロールをデシリアライズするライブラリとして使います。
:term:`Chameleon` を HTML テンプレートに使います。

.. :mod:`deform` depends only on Peppercorn, Colander, Chameleon and an
.. internationalization library named translationstring, so it may be
.. used in most web frameworks (or antiframeworks) as a result.

:mod:`deform` は、 PeppercornとColander, Chameleon, 
そして、国際化ライブラリのtranslationstring に依存します。
結果的に、多くのフレームワークもこれらを使うことになるでしょう。

.. Alternate templating languages may be used, as long as all templates
.. are translated from the native Chameleon templates to your templating
.. system of choice and a suitable :term:`renderer` is supplied to
.. :mod:`deform`.

全てのテンプレートをChameleonテンプレートから、他のテンプレートに変換して、
:term:`renderer` を :mod:`deform` に指定することで、
他のテンプレート言語も利用可能になります。

Topics
======

.. toctree::
   :maxdepth: 2

   basics.rst
   components.rst
   serialization.rst
   templates.rst
   widget.rst
   app.rst
   ajax.rst
   i18n.rst
   api.rst
   interfaces.rst
   glossary.rst
   changes.rst

Demonstration Site
==================

.. Visit `deformdemo.repoze.org <http://deformdemo.repoze.org>`_ to view an
.. application which demonstrates most of Deform's features.  The source code
.. for this application is also available in the `deform package on GitHub
.. <https://github.com/Pylons/deform>`_.

`deformdemo.repoze.org <http://deformdemo.repoze.org>`_ に行けば、
ほとんどの Deform の機能を網羅したデモアプリケーションを見ることができます。
このソースコードは、 
`deform package on GitHub <https://github.com/Pylons/deform>`_
から取得できます。

Support and Development
=======================

.. To report bugs, use the `bug tracker
.. <https://github.com/Pylons/deform/issues>`_.

バグの報告には
`bug tracker <https://github.com/Pylons/deform/issues>`_ を使ってください。

.. If you've got questions that aren't answered by this documentation, contact
.. the `Pylons-discuss maillist
.. <http://groups.google.com/group/pylons-discuss>`_ or join the `#pylons IRC
.. channel <irc://irc.freenode.net/#pylons>`_.

このドキュメントで解決しない問題がある場合は、
`Pylons-discuss maillist <http://groups.google.com/group/pylons-discuss>`_ 
に連絡してみるか、
`#pylons IRC channel <irc://irc.freenode.net/#pylons>`_
に接続してください。

.. Browse and check out tagged and trunk versions of :mod:`deform` via the
.. `deform package on GitHub <https://github.com/Pylons/deform>`_.  
.. To check out the trunk, use this command::

開発版の :mod:`deform` を使いたい場合は、`deform package on GitHub <https://github.com/Pylons/deform>`_ を参照してください。
チェックアウトするには、以下のコマンドを使います。

   git clone git://github.com/Pylons/deform.git

.. To find out how to become a contributor to :mod:`deform`, please see the
.. `Pylons Project contributor documentation
.. <http://docs.pylonsproject.org/#contributing/>`_.

:mod:`deform` のコントリビューターになるには、
`Pylons Project contributor documentation
<http://docs.pylonsproject.org/#contributing/>`_.
をご覧ください。

Index and Glossary
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Thanks
======

Without these people, this software would not exist:

- The Formish guys (http://ish.io)

- Tres Seaver

- Fear Factory (http://fearfactory.com)

- Midlake (http://midlake.net)

