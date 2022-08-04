from extractor.base import Field
from for_parsel.usemodel.model import SimpleDictModel, BaseModel, JsonPathModel
from pprint import pprint


class Foo(JsonPathModel):
    a = Field()


f1 = Foo(a=1)
f2 = Foo.load({"a": 2})

if __name__ == '__main__':
    print(f1.a)
    print(f2.a)
