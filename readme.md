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
- Merge Testcase

## Test Usage

```
$ pytest
```

You can test with `pytest`.



## Single Threading Testcase

A(addition_set), R(removal_set), add(add operation), rm(remove operation), v(Value)

| State   | Operation | Result(Value, Timestamp) | Test Method      |
| ------- | --------- | ------------------------ | ---------------- |
| A(v, 1) | add(v, 0) | v, 1                     | test_add_state() |
| A(v, 1) | add(v, 1) | v, 1                     | test_add_state() |
| A(v, 1) | add(v, 2) | v, 2                     | test_add_state() |
| A(v, 1) | rm(v, 0)  | v, 1                     | test_add_state() |
| A(v, 1) | rm(v, 1)  | v, 1                     | test_add_state() |
| A(v, 1) | rm(v, 2)  | None                     | test_add_state() |
| R(v, 1) | add(v, 0) | None                     | test_rm_state()  |
| R(v, 1) | add(v, 1) | v, 1                     | test_rm_state()  |
| R(v, 1) | add(v, 2) | v, 2                     | test_rm_state()  |
| R(v, 1) | rm(v, 0)  | None                     | test_rm_state()  |
| R(v, 1) | rm(v, 1)  | None                     | test_rm_state()  |
| R(v, 1) | rm(v, 2)  | None                     | test_rm_state()  |

These tests are modfied the original testcases by [Roshi](https://github.com/soundcloud/roshi).

## Multiple Threading Testcase

| Operation1 | Operation2 | Result(Value, Timestamp) | Test Method            |
| ---------- | ---------- | ------------------------ | ---------------------- |
| add(v, 1)  | add(v, 0)  | v, 1                     | test_multi_threading() |
| add(v, 1)  | add(v, 1)  | v, 1                     | test_multi_threading() |
| add(v, 1)  | add(v, 2)  | v, 2                     | test_multi_threading() |
| add(v, 1)  | rm(v, 0)   | v, 1                     | test_multi_threading() |
| add(v, 1)  | rm(v, 1)   | v, 1                     | test_multi_threading() |
| add(v, 1)  | rm(v, 2)   | None                     | test_multi_threading() |
| rm(v, 1)   | add(v, 0)  | None                     | test_multi_threading() |
| rm(v, 1)   | add(v, 1)  | v, 1                     | test_multi_threading() |
| rm(v, 1)   | add(v, 2)  | v, 2                     | test_multi_threading() |
| rm(v, 1)   | rm(v, 0)   | None                     | test_multi_threading() |
| rm(v, 1)   | rm(v, 1)   | None                     | test_multi_threading() |
| rm(v, 1)   | rm(v, 2)   | None                     | test_multi_threading() |

Multiple Threading Testcase has an random waiting time which will get a nondeterministic order.
however, timestamp is a mock so that we can get same result in spite of the order.



### Merge Testcase

Merge testcase is similar to Multiple Threading Testcase. however, These are deterministic order and It will test whether merge behavior is work or not.



# References
- https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type
- https://github.com/pfrazee/crdt_notes#sets
- https://hal.inria.fr/inria-00555588/PDF/techreport.pdf
- https://github.com/soundcloud/roshi