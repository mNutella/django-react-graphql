import graphene
from graphene_django.debug import DjangoDebug

import users.schema


class Query(users.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="_debug")


schema = graphene.Schema(query=Query)
