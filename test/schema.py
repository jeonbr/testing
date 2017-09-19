import graphene
import requests
import urllib
from util import *
from type_mapping import *

class ObjectTypePool:
    def addObjectClass(self, classname, dic):
        setattr(self, classname, type(classname, (graphene.ObjectType,), dic))

    def hasObjectClass(self, classname):
        return hasattr(self, classname)


objs = ObjectTypePool()


def make_mapping(dic, obj_name=None):
    if isinstance(dic, dict):
        dic = cleared(dic)

        result = {}
        for k, v in dic.items():
            if isinstance(v, dict):
                sub_result = make_mapping(v, k)
                if is_graphene_object(sub_result):
                    result[k] = graphene.Field(sub_result)
                elif is_graphene_list(sub_result):
                    result[k] = sub_result
                elif is_graphene_scalar(sub_result):
                    result[k] = sub_result()
            elif isinstance(v, list):
                result[k] = make_mapping(v, k)
            else:
                result[k] = graphene.Field(graphene_map[v])
        if len(result) > 0 and not objs.hasObjectClass(obj_name):
            objs.addObjectClass(obj_name, result)
            return getattr(objs, obj_name)
    elif isinstance(dic, list):
        sub_result = make_mapping(dic[0], obj_name)
        if is_graphene_scalar(sub_result):
            return graphene.List(sub_result)
        elif isinstance(sub_result, list):
            return graphene.List(make_mapping(sub_result, obj_name))
        elif is_graphene_object(sub_result):
            return graphene.List(sub_result)
    else:
        try:
            return graphene_map[dic]
        except KeyError as e:
            pass


make_mapping(Mygene_map, 'Mygene')
make_mapping(Metadata_map, 'Metadata')
make_mapping(Myvariant_map, 'Myvariant')

Mygene = getattr(objs, 'Mygene')
Metadata = getattr(objs, 'Metadata')
Myvariant = getattr(objs, 'Myvariant')


class GeneQuery(graphene.ObjectType):
    max_score = graphene.Float()
    took = graphene.Int()
    total = graphene.Int()
    hits = graphene.List(Mygene)


objs.hits = Mygene
objs.GeneQuery = GeneQuery


def get_mygene(id):
    url = "http://mygene.info/v3/gene/{}".format(id)
    r = requests.get(url).json()
    r = cleared(r)
    return fill_object(Mygene, r)


def get_metadata():
    url = "http://mygene.info/v3/metadata"
    r = requests.get(url).json()
    r = cleared(r)
    return fill_object(Metadata, r)


def get_genequery(q):
    dic = {
        "q": q,
        "fields": "all",
        "size": 1000
    }
    url = "http://mygene.info/v3/query"
    r = requests.get(url, params=dic).json()
    r = cleared(r)
    return fill_object(GeneQuery, r)


def get_myvariant(variantid):
    url = "http://myvariant.info/v1/variant/{}".format(urllib.parse.quote(variantid))
    r = requests.get(url).json()
    r = cleared(r)
    return fill_object(Myvariant, r)


def fill_object(obj, data_dic):
    input_dic = {}

    for k, v in obj._meta.local_fields.items():
        if is_graphene_object(v.type):
            try:
                input_dic[k] = fill_object(getattr(objs, k), data_dic[k])
            except KeyError as e:
                pass

        elif is_graphene_list(v.type):
            if is_graphene_scalar(v.type.of_type):
                try:
                    input_dic[k] = data_dic[k]
                except:
                    pass
            elif is_graphene_object(v.type.of_type):
                sublist = []
                for item in data_dic[k]:
                    try:
                        sublist.append(fill_object(getattr(objs, k), item))
                    except:
                        pass
                input_dic[k] = sublist
        elif is_graphene_scalar(v.type):
            try:
                input_dic[k] = data_dic[k]
            except:
                pass
    if len(input_dic) == 0:
        return
    return obj(**input_dic)


class Query(graphene.ObjectType):
    mygene = graphene.Field(Mygene, id=graphene.String())
    metadata = graphene.Field(Metadata)
    genequery = graphene.Field(GeneQuery, q=graphene.String())
    myvariant = graphene.Field(Myvariant, variantid=graphene.String())

    def resolve_mygene(self, args, context, info):
        return get_mygene(args['id'])

    def resolve_metadata(self, args, context, info):
        return get_metadata()

    def resolve_genequery(self, args, context, info):
        return get_genequery(args['q'])

    def resolve_myvariant(self, args, context, info):
        return get_myvariant(args['variantid'])


schema = graphene.Schema(query=Query)
