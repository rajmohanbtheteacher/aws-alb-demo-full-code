
import boto3
import json

def get_alb_metadata(alb_name_prefix):
    elbv2 = boto3.client('elbv2')
    albs = elbv2.describe_load_balancers()['LoadBalancers']
    alb = next((a for a in albs if alb_name_prefix in a['LoadBalancerName']), None)
    if not alb:
        return {"error": "ALB not found"}

    alb_dns = alb['DNSName']
    alb_arn = alb['LoadBalancerArn']
    listeners = elbv2.describe_listeners(LoadBalancerArn=alb_arn)['Listeners']
    first_listener = listeners[0] if listeners else {}
    target_groups = elbv2.describe_target_groups(LoadBalancerArn=alb_arn)['TargetGroups']
    first_tg = target_groups[0] if target_groups else {}

    return {
        "dns_name": alb_dns,
        "listener_port": first_listener.get("Port", "N/A"),
        "listener_protocol": first_listener.get("Protocol", "N/A"),
        "target_group": first_tg.get("TargetGroupName", "N/A")
    }

if __name__ == "__main__":
    metadata = get_alb_metadata("alb-demo-site")
    with open("alb-metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)
    print("ALB metadata written to alb-metadata.json")
