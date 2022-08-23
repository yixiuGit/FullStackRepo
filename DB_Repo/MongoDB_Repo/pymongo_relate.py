from pymongo import MongoClient, errors

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["netboxAPI"]
mycol = mydb["netbox_specs"]

#using aggreation to retrieve data from queryset object
pipeline = [ {
  "$group": {"_id": "$specsData.paths./dcim/cable-terminations/.get"}
}]

result = mycol.aggregate(pipeline)
for i in result:
    print(i)
print(type(result))

# output of print(i)
"""{'_id': {'operationId': 'dcim_cable-terminations_list', 'description': 'Overrides ListModelMixin to allow processing ExportTemplates.', 
    'parameters': [{'name': 'id', 'in': 'query', 'description': '', 'required': False, 'type': 'string'}, {'name': 'cable', 'in': 'query', 
    'description': '', 'required': False, 'type': 'string'}, {'name': 'cable_end', 'in': 'query', 'description': '', 'required': False, 'type': 'string'}, 
    {'name': 'termination_type', 'in': 'query', 'description': '', 'required': False, 'type': 'string'}, 
    {'name': 'termination_id', 'in': 'query', 'description': '', 'required': False, 'type': 'string'}, 
    {'name': 'id__n', 'in': 'query', 'description': '', 'required': False, 'type': 'string'}, 
    {'name': 'id__lte', 'in': 'query', 'description': '', 'required': False, 'type': 'string'}, 
    {'name': 'id__lt', 'in': 'query', 'description': '', 'required': False, 'type': 'string'}, 
    {'name': 'id__gte', 'in': 'query', 'description': '', 'required': False, 'type': 'string'}, 
    {'name': 'id__gt', 'in': 'query', 'description': '', 'required': False, 'type': 'string'}, 
    {'name': 'cable__n', 'in': 'query', 'description': '', 'required': False, 'type': 'string'}, 
    {'name': 'cable_end__n', 'in': 'query', 'description': '', 'required': False, 'type': 'string'},
    {'name': 'termination_type__n', 'in': 'query', 'description': '', 'required': False, 'type': 'string'},
    {'name': 'termination_id__n', 'in': 'query', 'description': '', 'required': False, 'type': 'string'}, 
    {'name': 'termination_id__lte', 'in': 'query', 'description': '', 'required': False, 'type': 'string'}, 
    {'name': 'termination_id__lt', 'in': 'query', 'description': '', 'required': False, 'type': 'string'}, 
    {'name': 'termination_id__gte', 'in': 'query', 'description': '', 'required': False, 'type': 'string'},
    {'name': 'termination_id__gt', 'in': 'query', 'description': '', 'required': False, 'type': 'string'}, 
    {'name': 'ordering', 'in': 'query', 'description': 'Which field to use when ordering the results.', 'required': False, 'type': 'string'}, 
    {'name': 'limit', 'in': 'query', 'description': 'Number of results to return per page.', 'required': False, 'type': 'integer'}, 
    {'name': 'offset', 'in': 'query', 'description': 'The initial index from which to return the results.', 'required': False, 'type': 'integer'}], 
    'responses': {'200': {'description': '', 'schema': {'required': ['count', 'results'], 'type': 'object', 
    'properties': {'count': {'type': 'integer'}, 'next': {'type': 'string', 'format': 'uri', 'x-nullable': True}, 
    'previous': {'type': 'string', 'format': 'uri', 'x-nullable': True}, 'results': {'type': 'array', 'items': {'$ref': '#/definitions/CableTermination'}}}}}}, 
    'tags': ['dcim']}}
"""
