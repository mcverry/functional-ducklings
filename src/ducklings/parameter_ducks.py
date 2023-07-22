import inspect
import typing
from collections import abc
from functools import wraps

T = typing.TypeVar("T")

SeqOR = typing.Union[T, typing.Sequence[T]]


def duck_sequence(
    seq_or_instance: SeqOR[T], sequence_constructor=list
) -> typing.Sequence[T]:
    """
    Args:
      list_or_instance: an instance or a sequence of instances

    Returns:
      A sequence of instance(s).
    """

    if isinstance(seq_or_instance, abc.Sequence) and not isinstance(
        seq_or_instance, str
    ):
        return seq_or_instance
    return sequence_constructor([seq_or_instance])  # FIXME


def duck_sequence_param(paramName: str):
    def decorator(fn):
        paramIndex = _get_param_index(fn, paramName)

        @wraps(fn)
        def wrapper(*args, **kwargs):
            args, kwargs = _update_param_value_by_name_or_index(
                args, kwargs, paramName, paramIndex, duck_sequence
            )
            return fn(*args, **kwargs)

        return wrapper

    return decorator


def _get_param_index(fn, paramName) -> int | None:
    sig = inspect.signature(fn)
    for name, index in zip(sig.parameters.keys(), range(10)):
        if name == paramName:
            return index
    return None


def _update_param_value_by_name_or_index(
    args, kwargs, paramName, paramIndex, value_update_func
):
    args = list(args)
    if paramName in kwargs:
        old_value = kwargs[paramName]
    else:
        old_value = args[paramIndex]

    new_value = value_update_func(old_value)

    if paramName in kwargs:
        kwargs[paramName] = new_value
    else:
        args[paramIndex] = new_value

    return tuple(args), kwargs
