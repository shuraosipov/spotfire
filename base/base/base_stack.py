from aws_cdk import core as cdk
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_rds as rds
import aws_cdk.aws_secretsmanager as sm

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class BaseStack(cdk.Stack):
    pass
    # def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
    #     super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        
cidr_range = "10.0.0.0/16"
db_instance_size = "t3.medium"


class VpcStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, vpc_name: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, vpc_name,
            cidr=cidr_range,
            max_azs=3,
            subnet_configuration = [
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="Ingress",
                    cidr_mask=24
                ),
                
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE,
                    name="App",
                    cidr_mask=24
                ),
                
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.ISOLATED,
                    name="Database",
                    cidr_mask=28
                ),
                
            ]
            
        )
        
        self.vpc=vpc


class DatabaseStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        rds_admin_secret = sm.Secret.from_secret_name_v2(self, "SecretFromName", "rds_admin")
        
        cluster = rds.DatabaseCluster(self, "Database",
            removal_policy=cdk.RemovalPolicy.DESTROY,
            engine=rds.DatabaseClusterEngine.aurora_postgres(version=rds.AuroraPostgresEngineVersion.VER_12_4),
            credentials=rds.Credentials.from_secret(rds_admin_secret),
            instance_props={
                "delete_automated_backups": True,
                "instance_type": ec2.InstanceType(db_instance_size),
                "vpc_subnets": {
                    "subnet_type": ec2.SubnetType.ISOLATED
                },
                "vpc": vpc
            }
        )
        
        cluster.connections.allow_default_port_internally()