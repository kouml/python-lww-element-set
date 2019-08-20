import threading
import time
import random

import pytest

from lww_element_set import LwwElementSet

class TestLwwElementSet():
    @pytest.mark.parametrize('op, v, t, exp_l, exp_t', [
        ('add', 'test_value', 0, 1, 1),
        ('add', 'test_value', 1, 1, 1),
        ('add', 'test_value', 2, 1, 2),
        ('rm', 'test_value', 0, 1, 1),
        ('rm', 'test_value', 1, 1, 1),
        ('rm', 'test_value', 2, 0, None)
    ])
    def test_add_state(self, op, v, t, exp_l, exp_t):
        lww = LwwElementSet()
        lww.add('test_value', 1)
        if op == 'add':
            lww.add(v, t)
        if op == 'rm':
            lww.remove(v, t)
        assert len(lww.get_all()) == exp_l and lww.get_element_with_timestamp(v) == exp_t

    @pytest.mark.parametrize('op, v, t, exp_l, exp_t', [
        ('add', 'test_value', 0, 0, None),
        ('add', 'test_value', 1, 1, 1),
        ('add', 'test_value', 2, 1, 2),
        ('rm', 'test_value', 0, 0, None),
        ('rm', 'test_value', 0, 0, None),
        ('rm', 'test_value', 0, 0, None)
    ])
    def test_rm_state(self, op, v, t, exp_l, exp_t):
        lww = LwwElementSet()
        lww.remove('test_value', 1)
        if op == 'add':
            lww.add(v, t)
        if op == 'rm':
            lww.remove(v, t)
        assert len(lww.get_all()) == exp_l and lww.get_element_with_timestamp(v) == exp_t

    @pytest.mark.parametrize('op1, v1, t1, op2, v2, t2, exp_l, exp_t', [
        ('add', 'test_value', 1, 'add', 'test_value', 0, 1, 1),
        ('add', 'test_value', 1, 'add', 'test_value', 1, 1, 1),
        ('add', 'test_value', 1, 'add', 'test_value', 2, 1, 2),
        ('add', 'test_value', 1, 'rm', 'test_value', 0, 1, 1),
        ('add', 'test_value', 1, 'rm', 'test_value', 1, 1, 1),
        ('add', 'test_value', 1, 'rm', 'test_value', 2, 0, None),
        ('rm', 'test_value', 1, 'add', 'test_value', 0, 0, None),
        ('rm', 'test_value', 1, 'add', 'test_value', 1, 1, 1),
        ('rm', 'test_value', 1, 'add', 'test_value', 2, 1, 2),
        ('rm', 'test_value', 1, 'rm', 'test_value', 0, 0, None),
        ('rm', 'test_value', 1, 'rm', 'test_value', 1, 0, None),
        ('rm', 'test_value', 1, 'rm', 'test_value', 2, 0, None),
    ])
    def test_multi_threading(self, op1, v1, t1, op2, v2, t2, exp_l, exp_t):
        lww = LwwElementSet()

        def sleep_and_run(lww, func, value, times):
            random_wait_time = random.random()
            time.sleep(random_wait_time)
            if func == 'add':
                lww.add(value, times)
            elif func == 'rm':
                lww.remove(value, times)

        th1 = threading.Thread(target=sleep_and_run, args=(lww, op1, v1, t1))
        th1.start()
        th2 = threading.Thread(target=sleep_and_run, args=(lww, op2, v2, t2))
        th2.start()

        th1.join()
        th2.join()
        assert len(lww.get_all()) == exp_l and lww.get_element_with_timestamp(v1) == exp_t
