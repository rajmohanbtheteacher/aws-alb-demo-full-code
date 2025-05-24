import boto3
import json

def get_first_alb_metadata():
    elbv2 = boto3.client('elbv2', region_name='us-east-1')  # Adjust region if needed
    try:
        albs = elbv2.describe_load_balancers()['LoadBalancers']
        if not albs:
            return {"error": "No ALBs found"}
        alb = albs[0]
        alb_dns = alb['DNSName']
        alb_arn = alb['LoadBalancerArn']

        listeners = elbv2.describe_listeners(LoadBalancerArn=alb_arn)['Listeners']
        listener = listeners[0] if listeners else {}

        target_groups = elbv2.describe_target_groups(LoadBalancerArn=alb_arn)['TargetGroups']
        tg = target_groups[0] if target_groups else {}

        return {
            "dns_name": alb_dns,
            "listener_port": listener.get("Port", "N/A"),
            "listener_protocol": listener.get("Protocol", "N/A"),
            "target_group": tg.get("TargetGroupName", "N/A")
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    metadata = get_first_alb_metadata()
    with open("alb-metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)
    print("✅ ALB metadata written to alb-metadata.json")
