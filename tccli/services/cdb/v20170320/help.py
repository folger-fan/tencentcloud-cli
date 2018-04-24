# -*- coding: utf-8 -*-
DESC = "cdb-2017-03-20"
INFO = {
  "DescribeDBInstanceGTID": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      }
    ],
    "desc": "本接口(DescribeDBInstanceGTID)用于查询云数据库实例是否开通了GTID，不支持版本为5.5以及以下的实例。"
  },
  "DescribeDBInstanceCharset": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      }
    ],
    "desc": "本接口(DescribeDBInstanceCharset)用于查询云数据库实例的字符集，获取字符集的名称。"
  },
  "DescribeBackupConfig": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例短实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。"
      }
    ],
    "desc": "本接口(DescribeBackupConfig)用于查询数据库备份配置信息。"
  },
  "DeleteBackup": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。"
      },
      {
        "name": "BackupId",
        "desc": "备份任务Id。"
      }
    ],
    "desc": "本接口(DeleteBackup)用于删除数据库备份。"
  },
  "IsolateDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值"
      }
    ],
    "desc": "本接口(IsolateDBInstance)用于销毁云数据库实例，销毁之后不能通过IP和端口访问数据库，按量计费实例销毁后直接下线。\n\n本接口不支持包年包月实例；"
  },
  "ModifyBackupConfig": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。"
      },
      {
        "name": "ExpireDays",
        "desc": "备份过期时间，单位为天，最小值为7天，最大值为732天。"
      },
      {
        "name": "StartTime",
        "desc": "备份时间范围，格式为：02:00-06:00，起点和终点时间目前限制为整点，目前可以选择的范围为： 02:00-06:00，06：00-10：00，10:00-14:00，14:00-18:00，18:00-22:00，22:00-02:00。"
      },
      {
        "name": "BackupMethod",
        "desc": "目标备份方法，可选的值：logical - 逻辑冷备，physical - 物理冷备。"
      }
    ],
    "desc": "本接口(ModifyBackupConfig)用于修改数据库备份配置信息。"
  },
  "ModifyInstanceParam": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例短Id列表。"
      },
      {
        "name": "ParamList",
        "desc": "要修改的参数列表。每一个元素是name和currentValue的组合。name是参数名，currentValue是要修改成的值。"
      }
    ],
    "desc": "本接口(ModifyInstanceParam)用于修改云数据库实例的参数。"
  },
  "ModifyDBInstanceProject": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例ID数组，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      },
      {
        "name": "NewProjectId",
        "desc": "项目的ID。"
      }
    ],
    "desc": "本接口(ModifyDBInstanceProject)用于修改云数据库实例的所属项目。"
  },
  "DescribeBackups": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，最小值为0。"
      },
      {
        "name": "Limit",
        "desc": "单次请求返回的数量，默认值为20，最大值为100。"
      }
    ],
    "desc": "本接口(DescribeBackups)用于查询云数据库实例的备份数据。"
  },
  "DescribeBackupDatabases": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。"
      },
      {
        "name": "StartTime",
        "desc": "开始时间，格式为：2017-07-12 10:29:20。"
      },
      {
        "name": "SearchDatabase",
        "desc": "要查询的数据库名前缀。"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量。"
      },
      {
        "name": "Limit",
        "desc": "分页大小，最大值为2000。"
      }
    ],
    "desc": "本接口(DescribeBackupDatabases)用于查询备份数据库列表。"
  },
  "CreateDBInstanceHour": {
    "params": [
      {
        "name": "EngineVersion",
        "desc": "MySQL版本，值包括：5.5、5.6和5.7，请使用[查询可创建规格（支持可用区、配置自定义）](https://cloud.tencent.com/document/api/253/6109)接口获取可创建的实例版本"
      },
      {
        "name": "UniqVpcId",
        "desc": "私有网络ID，如果不传则默认选择基础网络，请使用[查询私有网络列表](/document/api/215/15778)"
      },
      {
        "name": "UniqSubnetId",
        "desc": "私有网络下的子网ID，如果设置了 UniqVpcId，则 UniqSubnetId 必填，请使用[查询子网列表](/document/api/215/15784)"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID，不填为默认项目。请使用[查询项目列表](https://cloud.tencent.com/document/product/378/4400)接口获取项目ID"
      },
      {
        "name": "GoodsNum",
        "desc": "实例数量，默认值为1, 最小值1，最大值为100"
      },
      {
        "name": "Memory",
        "desc": "实例内存大小，单位：MB，请使用[查询可创建规格（支持可用区、配置自定义）](https://cloud.tencent.com/document/api/253/6109)接口获取可创建的内存规格"
      },
      {
        "name": "Volume",
        "desc": "实例硬盘大小，单位：GB，请使用[查询可创建规格（支持可用区、配置自定义）](https://cloud.tencent.com/document/api/253/6109)接口获取可创建的硬盘范围"
      },
      {
        "name": "Zone",
        "desc": "可用区信息，该参数缺省时，系统会自动选择一个可用区，请使用[查询可创建规格（支持可用区、配置自定义）](https://cloud.tencent.com/document/api/253/6109)接口获取可创建的可用区"
      },
      {
        "name": "MasterInstanceId",
        "desc": "实例ID，购买只读实例或者灾备实例时必填，该字段表示只读实例或者灾备实例的主实例ID，请使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872)接口查询云数据库实例ID"
      },
      {
        "name": "InstanceRole",
        "desc": "实例类型，默认为 master，支持值包括：master-表示主实例，dr-表示灾备实例，ro-表示只读实例"
      },
      {
        "name": "MasterRegion",
        "desc": "主实例的可用区信息，购买灾备实例时必填"
      },
      {
        "name": "Port",
        "desc": "自定义端口，端口支持范围：[ 1024-65535 ]"
      },
      {
        "name": "Password",
        "desc": "设置root帐号密码，密码规则：8-64个字符，至少包含字母、数字、字符（支持的字符：_+-&=!@#$%^*()）中的两种，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义"
      },
      {
        "name": "ParamList",
        "desc": "参数列表，参数格式如ParamList.0.Name=auto_increment&ParamList.0.Value=1。可通过[查询参数列表](/document/product/236/6369)查询支持设置的参数"
      },
      {
        "name": "ProtectMode",
        "desc": "数据复制方式，默认为0，支持值包括：0-表示异步复制，1-表示半同步复制，2-表示强同步复制，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义"
      },
      {
        "name": "DeployMode",
        "desc": "多可用区域，默认为0，支持值包括：0-表示单可用区，1-表示多可用区，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义"
      },
      {
        "name": "SlaveZone",
        "desc": "备库1的可用区ID，默认为zoneId的值，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义"
      },
      {
        "name": "BackupZone",
        "desc": "备库2的可用区ID，默认为0，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义"
      },
      {
        "name": "SecurityGroup",
        "desc": "安全组参数"
      },
      {
        "name": "RoGroup",
        "desc": "只读实例信息"
      },
      {
        "name": "AutoRenewFlag",
        "desc": "自动续费标记，值为0或1"
      },
      {
        "name": "InstanceName",
        "desc": "实例名称"
      }
    ],
    "desc": "本接口(CreateDBInstanceHour)用于创建按量计费的实例，可通过传入实例规格、MySQL 版本号和数量等信息创建云数据库实例，支持主实例、灾备实例和只读实例的创建。\n\n您还可以使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872)接口查询该实例的详细信息。\n\n1. 首先请使用[查询可创建规格（支持可用区、配置自定义）](https://cloud.tencent.com/document/api/253/6109)接口查询可创建的实例规格信息，然后请使用[查询价格（按量计费）](https://cloud.tencent.com/document/api/253/5176)接口查询可创建实例的售卖价格；\n2. 单次创建实例最大支持 100 个，实例时长最大支持 36 个月；\n3. 支持创建 MySQL5.5、MySQL5.6和MySQL5.7 版本；\n4. 支持创建主实例、灾备实例和只读实例；"
  },
  "ModifyDBInstanceName": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      },
      {
        "name": "InstanceName",
        "desc": "实例名称。"
      }
    ],
    "desc": "本接口(ModifyDBInstanceName)用于修改云数据库实例的名称。"
  },
  "CreateBackup": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。"
      },
      {
        "name": "BackupMethod",
        "desc": "目标备份方法，可选的值：logical - 逻辑冷备，physical - 物理冷备。"
      }
    ],
    "desc": "本接口(CreateBackup)用于创建数据库备份。"
  },
  "ModifyDBInstanceVipVport": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      },
      {
        "name": "DstIp",
        "desc": "目标IP。"
      },
      {
        "name": "DstPort",
        "desc": "目标端口，支持范围为：[1024-65535]。"
      },
      {
        "name": "UniqVpcId",
        "desc": "私有网络统一ID。"
      },
      {
        "name": "UniqSubnetId",
        "desc": "子网统一ID。"
      }
    ],
    "desc": "本接口(ModifyDBInstanceVipVport)用于修改云数据库实例的IP和端口号，也可进行基础网络转VPC网络和VPC网络下的子网变更。"
  },
  "DescribeDBInstanceRebootTime": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例的ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。"
      }
    ],
    "desc": "本接口(DescribeDBInstanceRebootTime)用于查询云数据库实例重启预计所需的时间。"
  },
  "DescribeBackupTables": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。"
      },
      {
        "name": "StartTime",
        "desc": "开始时间，格式为：2017-07-12 10:29:20。"
      },
      {
        "name": "DatabaseName",
        "desc": "指定的数据库名。"
      },
      {
        "name": "SearchTable",
        "desc": "要查询的数据表名前缀。"
      },
      {
        "name": "Offset",
        "desc": "分页偏移。"
      },
      {
        "name": "Limit",
        "desc": "分页大小，最大值为2000。"
      }
    ],
    "desc": "本接口(DescribeBackupTables)用于查询指定的数据库的备份数据表名。"
  },
  "DescribeDBInstances": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "项目ID，可使用[查询项目列表](https://cloud.tencent.com/document/product/378/4400)接口查询项目ID"
      },
      {
        "name": "InstanceTypes",
        "desc": "实例类型，可取值：1-主实例，2-灾备实例，3-只读实例"
      },
      {
        "name": "Vips",
        "desc": "实例的内网IP地址"
      },
      {
        "name": "Status",
        "desc": "实例状态，可取值：0-创建中，1-运行中，4-删除中，5-隔离中"
      },
      {
        "name": "Offset",
        "desc": "记录偏移量，默认值为0"
      },
      {
        "name": "Limit",
        "desc": "单次请求返回的数量，默认值为20，最大值为100"
      },
      {
        "name": "SecurityGroupId",
        "desc": "安全组ID"
      },
      {
        "name": "PayTypes",
        "desc": "付费类型，可取值：0-包年包月，1-小时计费"
      },
      {
        "name": "InstanceNames",
        "desc": "实例名称"
      },
      {
        "name": "TaskStatus",
        "desc": "实例任务状态，可能取值：<br>0-没有任务<br>1-升级中<br>2-数据导入中<br>3-开放Slave中<br>4-外网访问开通中<br>5-批量操作执行中<br>6-回档中<br>7-外网访问关闭中<br>8-密码修改中<br>9-实例名修改中<br>10-重启中<br>12-自建迁移中<br>13-删除库表中<br>14-灾备实例创建同步中"
      },
      {
        "name": "EngineVersions",
        "desc": "实例数据库引擎版本，可能取值：5.1、5.5、5.6和5.7"
      },
      {
        "name": "VpcIds",
        "desc": "私有网络的ID"
      },
      {
        "name": "ZoneIds",
        "desc": "可用区的ID"
      },
      {
        "name": "SubnetIds",
        "desc": "子网ID"
      },
      {
        "name": "CdbErrors",
        "desc": "是否锁定标记"
      },
      {
        "name": "OrderBy",
        "desc": "排序的字段，目前支持：\"InstanceId\", \"InstanceName\", \"CreateTime\", \"DeadlineTime\""
      },
      {
        "name": "OrderDirection",
        "desc": "排序方式，目前支持：\"ASC\"或者\"DESC\""
      },
      {
        "name": "WithSecurityGroup",
        "desc": "是否包含安全组信息"
      },
      {
        "name": "WithExCluster",
        "desc": "是否包含独享集群信息"
      },
      {
        "name": "ExClusterId",
        "desc": "独享集群ID"
      },
      {
        "name": "InstanceIds",
        "desc": "实例ID"
      },
      {
        "name": "InitFlag",
        "desc": "初始化标记，可取值：0-未初始化，1-初始化"
      },
      {
        "name": "WithDr",
        "desc": "是否包含灾备实例"
      },
      {
        "name": "WithRo",
        "desc": "是否包含只读实例"
      },
      {
        "name": "WithMaster",
        "desc": "是否包含主实例"
      }
    ],
    "desc": "本接口(DescribeDBInstances)用于查询云数据库实例列表，支持通过项目ID、实例ID、访问地址、实例状态等来筛选实例。\n\n1. 不指定任何过滤条件, 则默认返回20条实例记录，单次请求最多支持返回100条实例记录；\n2. 支持查询主实例、灾备实例和只读实例信息列表。"
  },
  "DescribeProjectSecurityGroups": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "项目ID。"
      }
    ],
    "desc": "本接口(DescribeProjectSecurityGroups)用于查询项目的安全组详情。"
  },
  "AssociateSecurityGroups": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "安全组Id。"
      },
      {
        "name": "InstanceIds",
        "desc": "实例ID列表，一个或者多个实例Id组成的数组。"
      }
    ],
    "desc": "本接口(AssociateSecurityGroups)用于安全组批量绑定实例。"
  },
  "DescribeSlowLogs": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，最小值为0。"
      },
      {
        "name": "Limit",
        "desc": "返回记录数量，默认值为20，最大值为100。"
      }
    ],
    "desc": "本接口(DescribeSlowLogs)用于获取云数据库实例的慢查询日志。"
  },
  "InitDBInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值"
      },
      {
        "name": "NewPassword",
        "desc": "实例新的密码，密码规则：8-64个字符，至少包含字母、数字、字符（支持的字符：!@#$%^*()）中的两种"
      },
      {
        "name": "Vport",
        "desc": "实例的端口"
      },
      {
        "name": "Parameters",
        "desc": "实例的参数列表，目前支持设置“character_set_server”、“lower_case_table_names”参数。其中，“character_set_server”参数可选值为[\"utf8\",\"latin1\",\"gbk\",\"utf8mb4\"]；“lower_case_table_names”可选值为[“0”,“1”]"
      }
    ],
    "desc": "本接口(InitDBInstances)用于初始化云数据库实例，包括初始化密码、默认字符集、实例端口号等"
  },
  "OpenWanService": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值"
      }
    ],
    "desc": "本接口(OpenWanService)用于开通实例外网访问"
  },
  "CreateDBInstance": {
    "params": [
      {
        "name": "Memory",
        "desc": "实例内存大小，单位：MB，请使用[查询可创建规格（支持可用区、配置自定义）](https://cloud.tencent.com/document/api/253/6109)接口获取可创建的内存规格"
      },
      {
        "name": "Volume",
        "desc": "实例硬盘大小，单位：GB，请使用[查询可创建规格（支持可用区、配置自定义）](https://cloud.tencent.com/document/api/253/6109)接口获取可创建的硬盘范围"
      },
      {
        "name": "Period",
        "desc": "实例时长，单位：月，可选值包括[1,2,3,4,5,6,7,8,9,10,11,12,24,36]"
      },
      {
        "name": "GoodsNum",
        "desc": "实例数量，默认值为1, 最小值1，最大值为100"
      },
      {
        "name": "Zone",
        "desc": "可用区信息，该参数缺省时，系统会自动选择一个可用区，请使用[查询可创建规格（支持可用区、配置自定义）](https://cloud.tencent.com/document/api/253/6109)接口获取可创建的可用区"
      },
      {
        "name": "UniqVpcId",
        "desc": "私有网络ID，如果不传则默认选择基础网络，请使用[查询私有网络列表](/document/api/215/15778)"
      },
      {
        "name": "UniqSubnetId",
        "desc": "私有网络下的子网ID，如果设置了 UniqVpcId，则 UniqSubnetId 必填，请使用[查询子网列表](/document/api/215/15784)"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID，不填为默认项目。请使用[查询项目列表](https://cloud.tencent.com/document/product/378/4400)接口获取项目ID"
      },
      {
        "name": "Port",
        "desc": "自定义端口，端口支持范围：[ 1024-65535 ]"
      },
      {
        "name": "InstanceRole",
        "desc": "实例类型，默认为 master，支持值包括：master-表示主实例，dr-表示灾备实例，ro-表示只读实例"
      },
      {
        "name": "MasterInstanceId",
        "desc": "实例ID，购买只读实例时必填，该字段表示只读实例的主实例ID，请使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872)接口查询云数据库实例ID"
      },
      {
        "name": "EngineVersion",
        "desc": "MySQL版本，值包括：5.5、5.6和5.7，请使用[查询可创建规格（支持可用区、配置自定义）](https://cloud.tencent.com/document/api/253/6109)接口获取可创建的实例版本"
      },
      {
        "name": "Password",
        "desc": "设置root帐号密码，密码规则：8-64个字符，至少包含字母、数字、字符（支持的字符：_+-&=!@#$%^*()）中的两种，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义"
      },
      {
        "name": "ProtectMode",
        "desc": "数据复制方式，默认为0，支持值包括：0-表示异步复制，1-表示半同步复制，2-表示强同步复制"
      },
      {
        "name": "DeployMode",
        "desc": "多可用区域，默认为0，支持值包括：0-表示单可用区，1-表示多可用区"
      },
      {
        "name": "SlaveZone",
        "desc": "备库1的可用区信息，默认为zone的值"
      },
      {
        "name": "ParamList",
        "desc": "参数列表，参数格式如ParamList.0.Name=auto_increment&ParamList.0.Value=1。可通过[查询参数列表](/document/product/236/6369)查询支持设置的参数"
      },
      {
        "name": "BackupZone",
        "desc": "备库2的可用区ID，默认为0，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义"
      },
      {
        "name": "AutoRenewFlag",
        "desc": "自动续费标记，可选值为：0-不自动续费；1-自动续费"
      },
      {
        "name": "MasterRegion",
        "desc": "主实例地域信息，购买灾备实例时，该字段必填"
      },
      {
        "name": "SecurityGroup",
        "desc": "安全组参数"
      },
      {
        "name": "RoGroup",
        "desc": "只读实例参数"
      },
      {
        "name": "InstanceName",
        "desc": "实例名称"
      }
    ],
    "desc": "本接口(CreateDBInstance)用于创建包年包月的云数据库实例（包括主实例、灾备实例和只读实例），可通过传入实例规格、MySQL 版本号、购买时长和数量等信息创建云数据库实例。\n\n您还可以使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872)接口查询该实例的详细信息。\n\n1. 首先请使用[查询可创建规格（支持可用区、配置自定义）](https://cloud.tencent.com/document/api/253/6109)接口查询可创建的实例规格信息，然后请使用[查询价格（包年包月）](https://cloud.tencent.com/document/api/236/1332)接口查询可创建实例的售卖价格；\n\n2. 单次创建实例最大支持 100 个，实例时长最大支持 36 个月；\n\n3. 支持创建 MySQL5.5 、 MySQL5.6 、 MySQL5.7 版本；\n\n4. 支持创建主实例、只读实例、灾备实例；"
  },
  "ModifyDBInstanceSecurityGroups": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。"
      },
      {
        "name": "SecurityGroupIds",
        "desc": "要修改的安全组ID列表，一个或者多个安全组Id组成的数组。"
      }
    ],
    "desc": "本接口(ModifyDBInstanceSecurityGroups)用于修改实例绑定的安全组。"
  },
  "DescribeDBImportRecords": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。"
      },
      {
        "name": "StartTime",
        "desc": "开始时间，时间格式如：2016-01-01 00:00:01。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，时间格式如：2016-01-01 23:59:59。"
      },
      {
        "name": "Offset",
        "desc": "分页参数 , 偏移量 , 默认值为0。"
      },
      {
        "name": "Limit",
        "desc": "分页参数 , 单次请求返回的数量 , 默认值为20。"
      }
    ],
    "desc": "本接口(DescribeDBImportRecords)用于查询云数据库导入任务操作日志。"
  },
  "SwitchForUpgrade": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同"
      }
    ],
    "desc": "本接口(SwitchForUpgrade)用于切换访问新实例，针对主升级中的实例处于待切换状态时，用户可主动发起该流程"
  },
  "DescribeTasks": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值"
      },
      {
        "name": "AsyncRequestId",
        "desc": "异步任务请求ID，执行 CDB 相关操作返回的 AsyncRequestId"
      },
      {
        "name": "TaskTypes",
        "desc": "任务类型，不传值则查询所有任务类型，可能的值：1-数据库回档；2-SQL操作；3-数据导入；5-参数设置；6-初始化；7-重启；8-开启GTID；9-只读实例升级；10-数据库批量回档；11-主实例升级；12-删除库表；13-切换为主实例；"
      },
      {
        "name": "TaskStatus",
        "desc": "任务状态，不传值则查询所有任务状态，可能的值：-1-未定义；0-初始化; 1-运行中；2-执行成功；3-执行失败；4-已终止；5-已删除；6-已暂停；"
      },
      {
        "name": "StartTimeBegin",
        "desc": "第一个任务的开始时间，用于范围查询，时间格式如：2017-12-31 10:40:01"
      },
      {
        "name": "StartTimeEnd",
        "desc": "最后一个任务的开始时间，用于范围查询，时间格式如：2017-12-31 10:40:01"
      },
      {
        "name": "Offset",
        "desc": "记录偏移量，默认值为0"
      },
      {
        "name": "Limit",
        "desc": "单次请求返回的数量，默认值为20，最大值为100"
      }
    ],
    "desc": "本接口(DescribeTasks)用于查询云数据库实例任务列表。"
  },
  "CreateDBImportJob": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例的ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。"
      },
      {
        "name": "FileName",
        "desc": "文件名称。"
      },
      {
        "name": "User",
        "desc": "云数据库的用户名。"
      },
      {
        "name": "Password",
        "desc": "云数据库实例User账号的密码。"
      },
      {
        "name": "DbName",
        "desc": "导入的目标数据库名，不传表示不指定数据库。"
      }
    ],
    "desc": "本接口(CreateDBImportJob)用于创建云数据库数据导入任务。"
  },
  "CloseWanService": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      }
    ],
    "desc": "本接口(CloseWanService)用于关闭云数据库实例的外网访问。关闭外网访问后，外网地址将不可访问。"
  },
  "StopDBImportJob": {
    "params": [
      {
        "name": "AsyncRequestId",
        "desc": "异步任务的请求ID。"
      }
    ],
    "desc": "本接口(StopDBImportJob)用于终止数据导入任务。"
  },
  "DescribeBackupDownloadDbTableCode": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。"
      },
      {
        "name": "StartTime",
        "desc": "开始时间，格式为：2017-07-12 10:29:20。"
      },
      {
        "name": "DatabaseTableList",
        "desc": "待下载的数据库和数据表列表。"
      }
    ],
    "desc": "本接口(DescribeBackupDownloadDbTableCode)用于查询备份数据分库分表下载位点。"
  },
  "DescribeBinlogs": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，最小值为0。"
      },
      {
        "name": "Limit",
        "desc": "单次请求返回的数量，默认值为20，最大值为100。"
      }
    ],
    "desc": "本接口(DescribeBinlogs)用于查询云数据库实例的二进制数据。"
  },
  "DescribeDBSecurityGroups": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。"
      }
    ],
    "desc": "本接口(DescribeDBSecurityGroups)用于查询实例的安全组详情。"
  },
  "UpgradeDBInstanceEngineVersion": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值"
      },
      {
        "name": "EngineVersion",
        "desc": "主实例数据库引擎版本，支持值包括：5.6和5.7"
      },
      {
        "name": "WaitSwitch",
        "desc": "切换访问新实例的方式，默认为0，升级主实例时，可指定该参数，升级只读实例或者灾备实例时指定该参数无意义，支持值包括：0-立刻切换，1-时间窗切换；当该值为1时，升级中过程中，切换访问新实例的流程将会在时间窗内进行，或者用户主动调用接口[切换访问新实例](https://cloud.tencent.com/document/api/403/4392)触发该流程"
      }
    ],
    "desc": "本接口(UpgradeDBInstanceEngineVersion)用于升级云数据库实例版本，实例类型支持主实例、灾备实例和只读实例。"
  },
  "UpgradeDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值"
      },
      {
        "name": "Memory",
        "desc": "升级后的内存大小，单位：MB，为保证传入 Memory 值有效，请使用[查询可创建规格（支持可用区、配置自定义）](https://cloud.tencent.com/document/api/253/6109)接口获取可升级的内存规格"
      },
      {
        "name": "Volume",
        "desc": "升级后的硬盘大小，单位：GB，为保证传入 Volume 值有效，请使用[查询可创建规格（支持可用区、配置自定义）](https://cloud.tencent.com/document/api/253/6109)接口获取可升级的硬盘范围"
      },
      {
        "name": "ProtectMode",
        "desc": "数据复制方式，支持值包括：0-异步复制，1-半同步复制，2-强同步复制，升级主实例时可指定该参数，升级只读实例或者灾备实例时指定该参数无意义"
      },
      {
        "name": "DeployMode",
        "desc": "部署模式，默认为0，支持值包括：0-单可用区部署，1-多可用区部署，升级主实例时可指定该参数，升级只读实例或者灾备实例时指定该参数无意义"
      },
      {
        "name": "SlaveZone",
        "desc": "备库1的可用区信息，默认为实例的Zone，升级主实例为多可用区部署时可指定该参数，升级只读实例或者灾备实例时指定该参数无意义。可通过<a href='/document/product/236/6921' title='查询云数据库可售卖规格'>查询云数据库可售卖规格</a>查询支持的可用区"
      },
      {
        "name": "EngineVersion",
        "desc": "主实例数据库引擎版本，支持值包括：5.5、5.6和5.7"
      },
      {
        "name": "WaitSwitch",
        "desc": "切换访问新实例的方式，默认为0，升级主实例时，可指定该参数，升级只读实例或者灾备实例时指定该参数无意义，支持值包括：0-立刻切换，1-时间窗切换；当该值为1时，升级中过程中，切换访问新实例的流程将会在时间窗内进行，或者用户主动调用接口[切换访问新实例](https://cloud.tencent.com/document/api/403/4392)触发该流程"
      },
      {
        "name": "BackupZone",
        "desc": "备库2的可用区ID，默认为0，升级主实例时可指定该参数，升级只读实例或者灾备实例时指定该参数无意义"
      },
      {
        "name": "InstanceRole",
        "desc": "实例类型，默认为 master，支持值包括：master-表示主实例，dr-表示灾备实例，ro-表示只读实例"
      }
    ],
    "desc": "本接口(UpgradeDBInstance)用于升级云数据库实例，实例类型支持主实例、灾备实例和只读实例"
  },
  "DisassociateSecurityGroups": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "安全组Id。"
      },
      {
        "name": "InstanceIds",
        "desc": "实例ID列表，一个或者多个实例Id组成的数组。"
      }
    ],
    "desc": "本接口(DisassociateSecurityGroups)用于安全组批量解绑实例。"
  }
}