# -*- coding: utf-8 -*-

import typing as T
from pathlib_mate import Path

from .enum_arch_group import ArchGroupIconEnum
from .enum_arch_service import ArchServiceIconEnum
from .enum_category import CategoryIconEnum
from .enum_resource import ResourceIconEnum
from ..paths import dir_custom_asset


class CommonEnum:
    job = ResourceIconEnum.res_aws_iot_device_defender_iot_device_jobs
    cluster = ResourceIconEnum.res_amazon_ec2_instances
    policy = ResourceIconEnum.res_aws_iot_policy
    dashboard = ResourceIconEnum.res_amazon_opensearch_service_opensearch_dashboards
    queue = ResourceIconEnum.res_amazon_simple_queue_service_queue
    user = dir_custom_asset.joinpath("iam-users.png")
    group = dir_custom_asset.joinpath("iam-groups.png")


# fmt: off
class IconMapping:
    # --------------------------------------------------------------------------
    # Main service
    # --------------------------------------------------------------------------
    s3 = ArchServiceIconEnum.arch_amazon_simple_storage_service
    iam = ArchServiceIconEnum.arch_aws_identity_and_access_management
    ec2 = ArchServiceIconEnum.arch_amazon_ec2
    vpc = ArchServiceIconEnum.arch_amazon_virtual_private_cloud
    dynamodb = ArchServiceIconEnum.arch_amazon_dynamodb
    rds = ArchServiceIconEnum.arch_amazon_rds
    sns = ArchServiceIconEnum.arch_amazon_simple_notification_service
    sqs = ArchServiceIconEnum.arch_amazon_simple_queue_service
    lambda_ = ArchServiceIconEnum.arch_aws_lambda
    cloudformation = ArchServiceIconEnum.arch_aws_cloudformation
    cloudwatch = ArchServiceIconEnum.arch_amazon_cloudwatch
    ecr = ArchServiceIconEnum.arch_amazon_elastic_container_registry
    athena = ArchServiceIconEnum.arch_amazon_athena
    secretsmanager = ArchServiceIconEnum.arch_amazon_sagemaker
    kms = ArchServiceIconEnum.arch_aws_key_management_service
    kinesis = ArchServiceIconEnum.arch_amazon_kinesis
    sagemaker = ArchServiceIconEnum.arch_amazon_sagemaker
    stepfunctions = ArchServiceIconEnum.arch_aws_step_functions
    cloudfront = ArchServiceIconEnum.arch_amazon_cloudfront
    route53 = ArchServiceIconEnum.arch_amazon_route_53
    apigateway = ArchServiceIconEnum.arch_amazon_api_gateway
    cognito = ArchServiceIconEnum.arch_amazon_cognito
    ecs = ArchServiceIconEnum.arch_amazon_elastic_container_service
    redshift = ArchServiceIconEnum.arch_amazon_redshift
    oss = ArchServiceIconEnum.arch_amazon_opensearch_service
    codecommit = ArchServiceIconEnum.arch_aws_codecommit
    codebuild = ArchServiceIconEnum.arch_aws_codebuild
    codepipeline = ArchServiceIconEnum.arch_aws_codepipeline
    codedeploy = ArchServiceIconEnum.arch_aws_codedeploy
    emr = ArchServiceIconEnum.arch_amazon_emr
    glue = ArchServiceIconEnum.arch_aws_glue
    lakeformation = ArchServiceIconEnum.arch_aws_lake_formation
    quicksight = ArchServiceIconEnum.arch_amazon_quicksight
    dms = ArchServiceIconEnum.arch_aws_database_migration_service
    elasticache = ArchServiceIconEnum.arch_amazon_elasticache
    documentdb = ArchServiceIconEnum.arch_amazon_documentdb
    memorydb = ArchServiceIconEnum.arch_amazon_memorydb_for_redis
    keyspaces = ArchServiceIconEnum.arch_amazon_keyspaces
    timestream = ArchServiceIconEnum.arch_amazon_timestream
    neptune = ArchServiceIconEnum.arch_amazon_neptune
    efs = ArchServiceIconEnum.arch_amazon_efs
    fsx = ArchServiceIconEnum.arch_amazon_fsx
    glacier = ArchServiceIconEnum.arch_amazon_simple_storage_service_glacier
    elasticbeanstalk = ArchServiceIconEnum.arch_aws_elastic_beanstalk
    eks = ArchServiceIconEnum.arch_amazon_elastic_kubernetes_service
    cloudtrail = ArchServiceIconEnum.arch_aws_cloudtrail
    systemsmanager = ArchServiceIconEnum.arch_aws_systems_manager
    eventbridge = ArchServiceIconEnum.arch_amazon_eventbridge
    costmanagement = ArchServiceIconEnum.arch_aws_cost_explorer
    iq = ArchServiceIconEnum.arch_aws_iq
    mq = ArchServiceIconEnum.arch_amazon_mq
    acm = ArchServiceIconEnum.arch_aws_certificate_manager
    iot = ArchServiceIconEnum.arch_aws_iot_core
    lex = ArchServiceIconEnum.arch_amazon_lex
    msk = ArchServiceIconEnum.arch_amazon_managed_streaming_for_apache_kafka
    ram = ArchServiceIconEnum.arch_aws_resource_access_manager
    ses = ArchServiceIconEnum.arch_amazon_simple_email_service
    swf = None
    waf = ArchServiceIconEnum.arch_aws_waf
    mwaa = ArchServiceIconEnum.arch_amazon_managed_workflows_for_apache_airflow
    qldb = ArchServiceIconEnum.arch_amazon_quantum_ledger_database
    xray = ArchServiceIconEnum.arch_aws_x_ray
    alexa = ArchServiceIconEnum.arch_alexa_for_business
    batch = ArchServiceIconEnum.arch_aws_batch
    chime = ArchServiceIconEnum.arch_amazon_chime
    macie = ArchServiceIconEnum.arch_amazon_macie
    polly = ArchServiceIconEnum.arch_amazon_polly
    backup = ArchServiceIconEnum.arch_aws_backup
    braket = None
    cloud9 = ArchServiceIconEnum.arch_aws_cloud9
    config = ArchServiceIconEnum.arch_aws_config
    kendra = ArchServiceIconEnum.arch_amazon_kendra
    status = None
    amplify = ArchServiceIconEnum.arch_aws_amplify
    appmesh = ArchServiceIconEnum.arch_aws_app_mesh
    appsync = ArchServiceIconEnum.arch_aws_appsync
    billing = ArchServiceIconEnum.arch_aws_billing_conductor
    chatbot = None
    connect = ArchServiceIconEnum.arch_amazon_connect
    outpost = ArchServiceIconEnum.arch_aws_outposts_family
    support = ArchServiceIconEnum.arch_aws_support
    artifact = ArchServiceIconEnum.arch_aws_artifact
    cloudhsm = ArchServiceIconEnum.arch_aws_cloudhsm
    cloudmap = ArchServiceIconEnum.arch_aws_cloud_map
    codeguru = ArchServiceIconEnum.arch_amazon_codeguru
    codestar = ArchServiceIconEnum.arch_aws_codestar
    datasync = None
    deeplens = ArchServiceIconEnum.arch_aws_deeplens
    forecast = ArchServiceIconEnum.arch_amazon_forecast
    freertos = None
    gamelift = ArchServiceIconEnum.arch_amazon_gamelift
    opsworks = ArchServiceIconEnum.arch_aws_opsworks
    pinpoint = ArchServiceIconEnum.arch_amazon_pinpoint
    sumerian = None
    textract = ArchServiceIconEnum.arch_amazon_textract
    transfer = ArchServiceIconEnum.arch_aws_transfer_family
    worklink = ArchServiceIconEnum.arch_amazon_worklink
    workmail = ArchServiceIconEnum.arch_amazon_workmail
    appstream = ArchServiceIconEnum.arch_amazon_appstream
    deepracer = ArchServiceIconEnum.arch_aws_deepracer
    detective = ArchServiceIconEnum.arch_amazon_detective
    guardduty = ArchServiceIconEnum.arch_amazon_guardduty
    inspector = ArchServiceIconEnum.arch_amazon_inspector
    iot1click = ArchServiceIconEnum.arch_aws_iot_1_click
    iotevents = ArchServiceIconEnum.arch_aws_iot_events
    lightsail = ArchServiceIconEnum.arch_amazon_lightsail
    medialive = ArchServiceIconEnum.arch_aws_elemental_medialive
    robomaker = ArchServiceIconEnum.arch_aws_robomaker
    translate = ArchServiceIconEnum.arch_amazon_translate
    blockchain = ArchServiceIconEnum.arch_amazon_managed_blockchain
    comprehend = ArchServiceIconEnum.arch_amazon_comprehend
    devicefarm = None
    mediastore = ArchServiceIconEnum.arch_aws_elemental_mediastore
    snowfamily = None
    transcribe = ArchServiceIconEnum.arch_amazon_transcribe
    workspaces = ArchServiceIconEnum.arch_amazon_workspaces_family
    augmentedai = ArchServiceIconEnum.arch_amazon_augmented_ai_a2i
    autoscaling = ArchServiceIconEnum.arch_aws_auto_scaling
    cloudsearch = ArchServiceIconEnum.arch_amazon_cloudsearch
    iotsitewise = ArchServiceIconEnum.arch_aws_iot_sitewise
    marketplace = ArchServiceIconEnum.arch_aws_marketplace_light
    mediatailor = ArchServiceIconEnum.arch_aws_elemental_mediatailor
    personalize = ArchServiceIconEnum.arch_amazon_personalize
    rekognition = ArchServiceIconEnum.arch_amazon_rekognition
    securityhub = ArchServiceIconEnum.arch_aws_security_hub
    codeartifact = ArchServiceIconEnum.arch_aws_codeartifact
    controltower = ArchServiceIconEnum.arch_aws_control_tower
    datapipeline = ArchServiceIconEnum.arch_aws_data_pipeline
    iotanalytics = ArchServiceIconEnum.arch_aws_iot_analytics
    launchwizard = None
    mediaconnect = ArchServiceIconEnum.arch_aws_elemental_mediaconnect
    mediaconvert = ArchServiceIconEnum.arch_aws_elemental_mediaconvert
    mediapackage = ArchServiceIconEnum.arch_aws_elemental_mediapackage
    migrationhub = ArchServiceIconEnum.arch_aws_migration_hub
    singlesignon = None
    directconnect = ArchServiceIconEnum.arch_aws_direct_connect
    frauddetector = ArchServiceIconEnum.arch_amazon_fraud_detector
    groundstation = ArchServiceIconEnum.arch_aws_ground_station
    iotgreengrass = ArchServiceIconEnum.arch_aws_iot_greengrass
    organizations = ArchServiceIconEnum.arch_aws_organizations
    accessanalyzer = ArchServiceIconEnum.arch_aws_identity_and_access_management
    developertools = None
    iotthingsgraph = None
    licensemanager = ArchServiceIconEnum.arch_aws_license_manager
    serverlessrepo = ArchServiceIconEnum.arch_aws_serverless_application_repository
    servicecatalog = ArchServiceIconEnum.arch_aws_service_catalog
    storagegateway = ArchServiceIconEnum.arch_aws_storage_gateway
    trustedadvisor = ArchServiceIconEnum.arch_aws_trusted_advisor
    ec2imagebuilder = ArchServiceIconEnum.arch_amazon_ec2_image_builder
    managedservices = None
    computeoptimizer = ArchServiceIconEnum.arch_aws_compute_optimizer
    directoryservice = ArchServiceIconEnum.arch_aws_directory_service
    elastictranscoder = ArchServiceIconEnum.arch_amazon_elastic_transcoder
    globalaccelerator = ArchServiceIconEnum.arch_aws_global_accelerator
    iotdevicedefender = ArchServiceIconEnum.arch_aws_iot_device_defender
    iotdevicemanagement = ArchServiceIconEnum.arch_aws_iot_device_management
    wellarchitectedtool = None
    servermigrationservice = None
    cleanrooms = ArchServiceIconEnum.arch_aws_clean_rooms
    datazone = ArchServiceIconEnum.arch_amazon_datazone
    # --------------------------------------------------------------------------
    # Sub menu
    # --------------------------------------------------------------------------
    ec2_instances = ResourceIconEnum.res_amazon_ec2_instance
    ec2_launchaninstance = ResourceIconEnum.res_amazon_ec2_instance
    ec2_amis = ResourceIconEnum.res_amazon_ec2_ami
    ec2_volumes = ResourceIconEnum.res_amazon_elastic_block_store_volume
    ec2_snapshots = ResourceIconEnum.res_amazon_elastic_block_store_snapshot
    ec2_elasticips = ResourceIconEnum.res_amazon_ec2_elastic_ip_address
    ec2_networkinterfaces = ResourceIconEnum.res_amazon_vpc_elastic_network_interface
    ec2_dashboard = CommonEnum.dashboard
    vpc_vpcs = ResourceIconEnum.res_amazon_vpc_virtual_private_cloud_vpc
    vpc_routetables = ResourceIconEnum.res_amazon_vpc_router
    vpc_endpoints = ResourceIconEnum.res_amazon_vpc_endpoints
    vpc_elasticips = ResourceIconEnum.res_amazon_ec2_elastic_ip_address
    vpc_internetgateways = ResourceIconEnum.res_amazon_vpc_internet_gateway
    vpc_natgateways = ResourceIconEnum.res_amazon_vpc_nat_gateway
    vpc_vpnconnections = ResourceIconEnum.res_amazon_vpc_vpn_connection
    vpc_networkacls = ResourceIconEnum.res_amazon_vpc_network_access_control_list
    s3_buckets = ResourceIconEnum.res_amazon_simple_storage_service_bucket
    s3_object_lambda_access_points = ResourceIconEnum.res_amazon_simple_storage_service_s3_object_lambda_access_points
    iam_roles = ResourceIconEnum.res_aws_identity_access_management_role
    iam_policies = ResourceIconEnum.res_aws_iot_policy
    iam_users = CommonEnum.user
    iam_user_groups = CommonEnum.group
    iam_new_role = ResourceIconEnum.res_aws_identity_access_management_role
    iam_new_policy = CommonEnum.policy
    dynamodb_tables = ResourceIconEnum.res_amazon_dynamodb_table
    dynamodb_items = ResourceIconEnum.res_amazon_dynamodb_items
    lambda_functions = ResourceIconEnum.res_aws_lambda_lambda_function
    lambda_newfunction = ResourceIconEnum.res_aws_lambda_lambda_function
    lambda_layers = ResourceIconEnum.res_aws_opsworks_layers
    batch_jobdefinitions = CommonEnum.job
    batch_jobqueues = ResourceIconEnum.res_amazon_simple_queue_service_queue
    batch_jobs = CommonEnum.job
    batch_computeenvironments = CommonEnum.cluster
    batch_scheduling_policies = CommonEnum.policy
    batch_dashboard = CommonEnum.dashboard
    cloudwatch_loggroups = ResourceIconEnum.res_amazon_cloudwatch_logs
    cloudwatch_metrics = ResourceIconEnum.res_amazon_cloudwatch_metrics_insights
    cloudwatch_alarms = ResourceIconEnum.res_amazon_cloudwatch_alarm
    cloudwatch_dashboard = CommonEnum.dashboard
    kinesis_datastreams = ArchServiceIconEnum.arch_amazon_kinesis_data_streams
    kinesis_firehose = ArchServiceIconEnum.arch_amazon_kinesis_data_firehose
    kinesis_videostreams = ArchServiceIconEnum.arch_amazon_kinesis_video_streams
    sqs_queues = ResourceIconEnum.res_amazon_simple_queue_service_queue
    sns_topics = ResourceIconEnum.res_amazon_simple_notification_service_topic
    sns_pushnotifications = ResourceIconEnum.res_amazon_simple_notification_service_http_notification
    sns_dashboard = CommonEnum.dashboard
    glue_databases = ResourceIconEnum.res_aws_glue_data_catalog
    glue_tables = ResourceIconEnum.res_aws_glue_data_catalog
    glue_crawlers = ResourceIconEnum.res_aws_glue_crawler
    glue_jobs = CommonEnum.job
    oss_managed_clusters_dashboard = CommonEnum.dashboard
    oss_managed_clusters_domains = ResourceIconEnum.res_amazon_opensearch_service_index
    oss_serverless_dashboard = CommonEnum.dashboard
    oss_serverless_collections = ResourceIconEnum.res_amazon_opensearch_service_index
    eventbridge_eventbuses = ResourceIconEnum.res_amazon_eventbridge_default_event_bus
    eventbridge_rules = ResourceIconEnum.res_amazon_eventbridge_rule
    eventbridge_schemas = ResourceIconEnum.res_amazon_eventbridge_schema
    eventbridge_schedules = ResourceIconEnum.res_amazon_eventbridge_scheduler
    eventbridge_partnereventsources = ResourceIconEnum.res_amazon_eventbridge_saas_partner_event
    sagemaker_studio = ArchServiceIconEnum.arch_amazon_sagemaker_studio_lab
    sagemaker_studiolab = ArchServiceIconEnum.arch_amazon_sagemaker_studio_lab
    sagemaker_rstudio = ArchServiceIconEnum.arch_amazon_sagemaker_studio_lab
    sagemaker_canvas = ResourceIconEnum.res_amazon_sagemaker_canvas
    sagemaker_models = ResourceIconEnum.res_amazon_sagemaker_model
    sagemaker_trainingjobs = ResourceIconEnum.res_amazon_sagemaker_train
    sagemaker_hyperparametertuningjobs = ResourceIconEnum.res_amazon_sagemaker_train
# fmt: on

icon_mapping = {k: v for k, v in IconMapping.__dict__.items() if not k.startswith("_")}
icon_mapping["lambda"] = icon_mapping["lambda_"]
del icon_mapping["lambda_"]


def id_to_icon(id: str) -> T.Optional[Path]:
    parts = id.split("-", 1)
    # service
    if len(parts) == 1:
        return icon_mapping.get(id)
    # sub menu
    else:
        # try to find icon of sub menu
        v = icon_mapping.get(id.replace("-", "_"))
        # if not found, use the main service icon
        if v is None:
            return icon_mapping.get(parts[0])
        else:
            return v
