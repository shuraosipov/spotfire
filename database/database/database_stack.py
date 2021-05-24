from aws_cdk import core as cdk
import aws_cdk.aws_rds as rds
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_secretsmanager as sm


class DatabaseStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        rds_admin_secret = sm.Secret.from_secret_name_v2(self, "SecretFromName", "rds_admin")
        
        vpc = ec2.Vpc.from_lookup(self, "VPC",
            # This imports the default VPC but you can also
            # specify a 'vpcName' or 'tags'.
            is_default=True
        )
        
        cluster = rds.DatabaseCluster(self, "Database",
            engine=rds.DatabaseClusterEngine.aurora_postgres(version=rds.AuroraPostgresEngineVersion.VER_12_4),
            credentials=rds.Credentials.from_secret(rds_admin_secret),
            instance_props={
                # "instance_type": ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MEDIUM),
                "delete_automated_backups": True,
                "instance_type": ec2.InstanceType("t3.medium"),
                "vpc_subnets": {
                    "subnet_type": ec2.SubnetType.PUBLIC
                    # "subnet_group_name": "private-db-subnet-group"
                },
                "vpc": vpc
            }
    )

        
