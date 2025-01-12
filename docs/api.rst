.. py:currentmodule:: pleco

===================
API Reference
===================

The `pleco` module establishes an API for defining and evaluating data expectations.

Expectations
------------

Expectations represent a set of constraints that data should satisfy. At minimum,
expectations must satisfy the :class:`Expectation` interface, i.e., provide a
:meth:`Expectation.build_result` method.

Given that expectations frequently interpret observation counts or aggregate values, the
:class:`CountExpectation` and :class:`ValueExpectation` classes provide additional
interfaces for these cases, respectively.

.. autoclass:: Expectation
    :members:
    :exclude-members: model_config

.. autoclass:: CountExpectation
    :members:
    :exclude-members: model_config
    :show-inheritance:

.. autoclass:: ValueExpectation
    :members:
    :exclude-members: model_config
    :show-inheritance:

.. autoclass:: Suite
    :members:
    :exclude-members: model_config

Severity
--------

.. autoclass:: Severity
    :members:
    :exclude-members: __new__

Constraints
-----------

Constraints establish the conditions that data must satisfy to be considered valid.
Constraints are not required for an expectation, and some expectations may have more
than one constraint.

.. autoclass:: Constraint
    :members:
    :exclude-members: model_config


Results
-------

.. autoclass:: Result
    :members:
    :exclude-members: model_config

.. autoclass:: CountResult
    :members:
    :exclude-members: model_config
    :show-inheritance:

.. autoclass:: ValueResult
    :members:
    :exclude-members: model_config
    :show-inheritance:

.. autoclass:: Results
    :members:
    :exclude-members: model_config

Runners
-------

.. autoclass:: Runner
    :members:
    :exclude-members: model_config


