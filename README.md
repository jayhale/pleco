# Pleco

Straightforward data validation since the Jurassic.

---

_This is a work in progress, use it at your own risk!_

## Goals

- Intuitive and simple to use - the opposite of Great Expectations
- Consistently structured - e.g., don't make type checks and value checks behave differently (looking at you Pandera)
- Focused on doing one thing well - loading, partitioning, reporting, etc. belong to others
- 100% coverage of [Great Expectations core]

## Progress and Potential Path Forward

- [x] Foundational interfaces: `Expectation` and `Runner`
- [x] Initial Pandas support: `PandasRunner`, 22% coverage of core expectations
- [ ] Initial Polars support
- [ ] Initial PySpark support
- [ ] Compatability package that allows users to define expectations exactly how they're defined in Great Expectations
- [ ] 100% coverage of single-column expectations from Great Expectations 
- [ ] 100% coverage of multi-column expectations from Great Expectations

[great expectations core]: https://github.com/great-expectations/great_expectations/blob/develop/great_expectations/expectations/core/__init__.py