from mystructures import StaticTypeStack
import pytest

def test_push_correct_type():
    stack = StaticTypeStack(int)
    assert stack.push(10) is True
    assert stack.push(20) is True
    assert len(stack) == 2

def test_push_incorrect_type():
    stack = StaticTypeStack(int)
    assert stack.push("string") is False
    assert len(stack) == 0

def test_pop():
    stack = StaticTypeStack(int)
    stack.push(10)
    stack.push(20)
    assert stack.pop() is True
    assert len(stack) == 1
    assert stack.pop() is True
    assert len(stack) == 0
    assert stack.pop() is False

def test_empty_pop():
    stack = StaticTypeStack(int)
    assert stack.pop() is False
    assert stack.push(10) is True
    assert stack.pop() is True
    assert stack.pop() is False

def test_len():
    stack = StaticTypeStack(int)
    assert len(stack) == 0
    stack.push(10)
    assert len(stack) == 1
    stack.push(20)
    assert len(stack) == 2

def test_getitem():
    stack = StaticTypeStack(int)
    stack.push(10)
    stack.push(20)
    assert stack[0].value == 10
    assert stack[1].value == 20
    with pytest.raises(IndexError):
        stack[2]

def test_iteration():
    stack = StaticTypeStack(int)
    stack.push(10)
    stack.push(20)
    items = [item.value for item in stack]
    assert items == [10, 20]