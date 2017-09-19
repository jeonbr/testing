import re
from functools import partial
import graphene
import inspect

NAME_PATTERN = r'^[_a-zA-Z][_a-zA-Z0-9]*$'
COMPILED_NAME_PATTERN = re.compile(NAME_PATTERN)

def is_graphene(obj, target):
    if inspect.isclass(obj):
        return issubclass(obj, target)
    else:
        return issubclass(type(obj), target)


is_graphene_list = partial(is_graphene, target=graphene.types.structures.List)
is_graphene_object = partial(is_graphene, target=graphene.types.objecttype.ObjectType)
is_graphene_scalar = partial(is_graphene, target=graphene.types.scalars.Scalar)



def is_valid_name(name):
    return COMPILED_NAME_PATTERN.match(name)


def assert_valid_name(name):
    '''Helper to assert that provided names are valid.'''
    assert COMPILED_NAME_PATTERN.match(name), 'Names must match /{}/ but "{}" does not.'.format(NAME_PATTERN, name)


def clear_name(name):
    cleared = name.lower().replace("-", "_").replace("+", "_")
    try:
        int(cleared[0])
        return "I" + cleared
    except:
        return cleared


def cleared(dic):
    if isinstance(dic, dict):
        result = {}
        for k, v in dic.items():
            result[clear_name(k)] = cleared(v)
        return result
    elif isinstance(dic, list):
        result = []
        for item in dic:
            result.append(cleared(item))
        return result
    else:
        return dic
