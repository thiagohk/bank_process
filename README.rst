============
bank_process
============


Load bank accounts and transactions and prints the processed results in CSV format.


Description
===========

Install the command (it may require sudo):

.. code:: shell

   python3 setup.py install

Execute loader:

.. code:: shell

   load-transactions <accounts CSV file> <transactions CSV file>
   Example: load-transactions accounts.csv transactions.csv

An error log file, called transactions_loader.log, will be generated.

Execute unit tests (it may require sudo):

.. code:: shell

   python3 setup.py test

For help 

.. code:: shell

   load-transactions --help


Note
====

This project has been set up using PyScaffold 3.2.3. For details and usage
information on PyScaffold see https://pyscaffold.org/.


