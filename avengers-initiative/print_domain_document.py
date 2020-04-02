from xpms_helper.model import domain_util, document_util


def print_domain_document(config, **kwargs):
    doc_id = config["context"]["doc_id"]
    solution_id = config["context"]["solution_id"]
    payload = {"solution_id": solution_id, "doc_id": doc_id, "root_id": doc_id}
    domain_obj = domain_util.get_domain_object(payload)
    document_obj = document_util.get_document_object(payload)
    return {"domain": domain_obj, "document": document_obj}

local_config = {"context":{"doc_id":"testdocid","solution_id":"testsolid"}}
k = angshu_test(local_config)
print(k)
