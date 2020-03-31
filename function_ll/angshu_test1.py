from xpms_helper.model import domain_util

def angshu_test1(**kwargs):
    json= domain_util.get_domain_object({"solution_id": "daglib", "doc_id": "66ae918d-c45a-463f-beed-8b6415289846", "root_id": "66ae918d-c45a-463f-beed-8b6415289846"})
    print(json)

