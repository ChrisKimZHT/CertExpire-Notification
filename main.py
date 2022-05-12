import re
import subprocess
from datetime import datetime
from notification import msg

# 报警阈值
threshold = 60
# 查询域名列表
domain_list = [
    "www.baidu.com"
]


def remain_time(domain):
    command = f"curl -Ivs https://{domain} --connect-timeout 10"
    cert_info = subprocess.getstatusoutput(command)[1]
    # start_date = datetime.strptime(re.search("start date: (.*)", cert_info).group(1), "%b %d %H:%M:%S %Y GMT")
    expire_date = datetime.strptime(re.search("expire date: (.*)", cert_info).group(1), "%b %d %H:%M:%S %Y GMT")
    return (expire_date - datetime.now()).days


if __name__ == "__main__":
    result_list = []
    success = 0
    fail = 0
    alert = 0
    for dom in domain_list:
        try:
            result_list.append({"domain": dom, "remain": remain_time(dom)})
            success += 1
        except:
            result_list.append({"domain": dom, "remain": -1})
            fail += 1
    result_list = sorted(result_list, key=lambda x: x["remain"])
    alert_str = ""
    for res in result_list:
        if res["remain"] <= threshold:
            alert_str += f"{res['domain']}: {res['remain']} 天\n"
            alert += 1
    message = f"【证书到期查询】\n" \
              f"成功: {success} 个\n" \
              f"失败: {fail} 个\n" \
              f"告警: {alert} 个\n"
    if alert:
        message += f"告警列表:\n" + alert_str
    print(message)
    msg(message)
