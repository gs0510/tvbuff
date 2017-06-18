tvbuff
======

​:tv: tvbuff is a command line tv guide that helps you track your
favorite shows

Installation
------------

-  From source:

.. code:: bash

    $ git clone https://github.com/gs0510/tvbuff
    $ cd tvbuff/
    $ sudo python setup.py install

Usage
-----

Search for the next episode
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ tvbuff next "Game of Thrones"

Search for the previous episode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ tvbuff previous "Game of Thrones"

Get a list of episodes screening on a particular dat
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ tvbuff list "US" "2016-05-18"

Get episode list of a particular TV show
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ tvbuff episodes "Silicon Valley"

Help
~~~~

.. code:: bash

    $ tvbuff -h