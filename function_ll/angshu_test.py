from xpms_helper.model import domain_util


def angshu_test():
    json= domain_util.get_domain_object({"solution_id": "ddd", "doc_id": "ssss", "root_id": "ssss"})
    print(json)


angshu_test()

