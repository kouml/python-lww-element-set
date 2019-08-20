# Overall
This is a simple lww-element-set implementation by Python.

# Directories
```shell
lww_element_set
├── lww_element_set.py
├── lww_element_set_test.py
└── README.md
```

# Requirements
```
Python: 3.6
pytest: 3.0.5
```

# Test Overall
Test is wrriten in `lww_element_set_test.py`.
- Single Threading Testcase
    - test_add_state()
    - test_rm_state()
- Multiple Threading Testcase
  - test_multi_threading()

You can test with `pytest`.
Multiple Threading Testcase has an random waiting time which will get a nondeterministic order.
however, timestamp is a mock so that we can get same result.

# References
- https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type
- https://github.com/pfrazee/crdt_notes#sets
- https://hal.inria.fr/inria-00555588/PDF/techreport.pdf
