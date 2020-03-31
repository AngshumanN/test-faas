from xpms_helper.model import domain_util

def angshu_test1(**kwargs):
    json= domain_util.get_domain_object({"solution_id": "libdag", "doc_id": "d79c768b-7282-4e64-a14f-625205d4c5d3", "root_id": "d79c768b-7282-4e64-a14f-625205d4c5d3"})
    return json
