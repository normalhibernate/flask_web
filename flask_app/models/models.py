#!/usr/bin/env python
# coding=utf-8

from sqlalchemy.dialects.mysql import BIGINT, DATETIME, INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base
from flask_app import db
Base = declarative_base()
metadata = Base.metadata



class Alarmcontactor(Base):
    __tablename__ = 'alarmcontactor'

    recordId = db.Column(db.String(50), primary_key=True)
    stationId = db.Column(db.String(50))
    name = db.Column(db.String(50))
    phone = db.Column(db.String(20))


class Alarminfo(Base):
    __tablename__ = 'alarminfo'

    recordId = db.Column(INTEGER(11), primary_key=True)
    stationId = db.Column(db.String(50))
    item = db.Column(db.String(50))
    _type = db.Column(db.String(20))
    data = db.Column(db.String(50))
    info = db.Column(db.String(50))
    condition = db.Column(db.String(100))
    At = db.Column(BIGINT(20), index=True)


class Carbonsampler(Base):
    __tablename__ = 'carbonsampler'

    recordId = db.Column(INTEGER(11), primary_key=True)
    stationId = db.Column(db.String(50))
    At = db.Column(BIGINT(20), index=True)
    WorkID = db.Column(db.String(50))
    BeginTime = db.Column(BIGINT(20))
    EndTime = db.Column(BIGINT(20))
    RealtimeFlow = db.Column(db.Float)
    TotalFlow = db.Column(db.Float)
    StandardVolume = db.Column(db.Float)
    WorkingVolume = db.Column(db.Float)
    AmbientTemp = db.Column(db.Float)
    AmbientHumi = db.Column(db.Float)
    Pressure = db.Column(db.Float)
    FaultAlarm = db.Column(db.String(10))


class Carbonsampler1h(Base):
    __tablename__ = 'carbonsampler1h'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Carbonsampler5m(Base):
    __tablename__ = 'carbonsampler5m'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Carbonsamplerday(Base):
    __tablename__ = 'carbonsamplerday'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Carbonsamplermonth(Base):
    __tablename__ = 'carbonsamplermonth'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Carbonsamplerrecord(Base):
    __tablename__ = 'carbonsamplerrecord'

    recordId = db.Column(INTEGER(11), primary_key=True)
    stationId = db.Column(db.String(50))
    At = db.Column(BIGINT(20), index=True)
    WorkID = db.Column(db.String(50))
    BeginTime = db.Column(BIGINT(20))
    EndTime = db.Column(BIGINT(20))
    RealtimeFlow = db.Column(db.Float)
    TotalFlow = db.Column(db.Float)
    StandardVolume = db.Column(db.Float)
    WorkingVolume = db.Column(db.Float)
    AmbientTemp = db.Column(db.Float)
    AmbientHumi = db.Column(db.Float)
    Pressure = db.Column(db.Float)
    FaultAlarm = db.Column(db.String(10))
    UpdateFlag = db.Column(TINYINT(1))


class Carbonsampleryear(Base):
    __tablename__ = 'carbonsampleryear'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Datastreaminfo(Base):
    __tablename__ = 'datastreaminfo'

    primaryId = db.Column(INTEGER(11), primary_key=True)
    dsId = db.Column(db.String(50))
    stationId = db.Column(db.String(50))
    dataRange = db.Column(db.String(20))
    deviceId = db.Column(db.String(10))
    unit = db.Column(db.String(10))
    name = db.Column(db.String(50))


class Devicealarmstate(Base):
    __tablename__ = 'devicealarmstates'

    recordId = db.Column(INTEGER(11), primary_key=True)
    stationId = db.Column(db.String(50))
    alarmItem = db.Column(db.String(50))
    alarmStates = db.Column(db.String(50))


class Deviceinfo(Base):
    __tablename__ = 'deviceinfo'

    primaryId = db.Column(INTEGER(11), primary_key=True)
    devId = db.Column(db.String(10))
    ENO = db.Column(db.String(10))
    stationId = db.Column(db.String(50))
    name = db.Column(db.String(50))
    deviceType = db.Column(db.String(50))
    deviceModel = db.Column(db.String(20))
    status = db.Column(db.String(10))
    states = db.Column(db.String(4096))
    properties = db.Column(db.String(4096))
    commands = db.Column(db.String(4096))
    url = db.Column(db.String(50))
    interval = db.Column(INTEGER(11))


class DjangoMigration(Base):
    __tablename__ = 'django_migrations'

    id = db.Column(INTEGER(11), primary_key=True)
    app = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    applied = db.Column(DATETIME(fsp=6), nullable=False)


class Drywetdeposition(Base):
    __tablename__ = 'drywetdeposition'

    recordId = db.Column(INTEGER(11), primary_key=True)
    stationId = db.Column(db.String(50))
    At = db.Column(BIGINT(20))
    BeginTime = db.Column(BIGINT(20))
    EndTime = db.Column(BIGINT(20))
    Moisture = db.Column(db.Float)
    RainIntensity = db.Column(db.Float)
    AmbientTemp = db.Column(db.Float)
    CaseTemp = db.Column(db.Float)
    BucketTemp = db.Column(db.Float)
    RainSensor = db.Column(db.Float)
    FaultAlarm = db.Column(db.String(10))


class Electricrecord(Base):
    __tablename__ = 'electricrecord'

    recordId = db.Column(INTEGER(11), primary_key=True)
    stationId = db.Column(db.String(50))
    At = db.Column(BIGINT(20), index=True)
    Power = db.Column(db.Float)
    count = db.Column(db.Float)


class Extralargea(Base):
    __tablename__ = 'extralargeas'

    recordId = db.Column(INTEGER(11), primary_key=True)
    stationId = db.Column(db.String(50))
    At = db.Column(BIGINT(20), index=True)
    WorkID = db.Column(db.String(50))
    BeginTime = db.Column(BIGINT(20))
    EndTime = db.Column(BIGINT(20))
    RealtimeFlow = db.Column(db.Float)
    TotalFlow = db.Column(db.Float)
    StandardVolume = db.Column(db.Float)
    WorkingVolume = db.Column(db.Float)
    AmbientTemp = db.Column(db.Float)
    AmbientHumi = db.Column(db.Float)
    Pressure = db.Column(db.Float)
    FaultAlarm = db.Column(db.String(10))


class Extralargeas1h(Base):
    __tablename__ = 'extralargeas1h'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Extralargeas5m(Base):
    __tablename__ = 'extralargeas5m'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Extralargeasday(Base):
    __tablename__ = 'extralargeasday'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Extralargeasmonth(Base):
    __tablename__ = 'extralargeasmonth'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Extralargeasrecord(Base):
    __tablename__ = 'extralargeasrecord'

    recordId = db.Column(INTEGER(11), primary_key=True)
    stationId = db.Column(db.String(50))
    At = db.Column(BIGINT(20), index=True)
    WorkID = db.Column(db.String(50))
    BeginTime = db.Column(BIGINT(20))
    EndTime = db.Column(BIGINT(20))
    RealtimeFlow = db.Column(db.Float)
    TotalFlow = db.Column(db.Float)
    StandardVolume = db.Column(db.Float)
    WorkingVolume = db.Column(db.Float)
    AmbientTemp = db.Column(db.Float)
    AmbientHumi = db.Column(db.Float)
    Pressure = db.Column(db.Float)
    FaultAlarm = db.Column(db.String(10))
    UpdateFlag = db.Column(TINYINT(1))


class Extralargeasyear(Base):
    __tablename__ = 'extralargeasyear'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Hpicrecord(Base):
    __tablename__ = 'hpicrecord'

    recordId = db.Column(INTEGER(11), primary_key=True)
    stationId = db.Column(db.String(50))
    At = db.Column(BIGINT(20), index=True)
    DoseRate = db.Column(db.Float)
    Humi = db.Column(db.Float)


class Hpicrecord1h(Base):
    __tablename__ = 'hpicrecord1h'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Hpicrecord5m(Base):
    __tablename__ = 'hpicrecord5m'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Hpicrecordday(Base):
    __tablename__ = 'hpicrecordday'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Hpicrecordmonth(Base):
    __tablename__ = 'hpicrecordmonth'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Hpicrecordyear(Base):
    __tablename__ = 'hpicrecordyear'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Iodinesampler(Base):
    __tablename__ = 'iodinesampler'

    recordId = db.Column(INTEGER(11), primary_key=True)
    stationId = db.Column(db.String(50))
    At = db.Column(BIGINT(20), index=True)
    WorkID = db.Column(db.String(50))
    BeginTime = db.Column(BIGINT(20))
    EndTime = db.Column(BIGINT(20))
    RealtimeFlow = db.Column(db.Float)
    TotalFlow = db.Column(db.Float)
    StandardVolume = db.Column(db.Float)
    WorkingVolume = db.Column(db.Float)
    AmbientTemp = db.Column(db.Float)
    AmbientHumi = db.Column(db.Float)
    Pressure = db.Column(db.Float)
    FaultAlarm = db.Column(db.String(10))


class Iodinesampler1h(Base):
    __tablename__ = 'iodinesampler1h'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Iodinesampler5m(Base):
    __tablename__ = 'iodinesampler5m'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Iodinesamplerday(Base):
    __tablename__ = 'iodinesamplerday'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Iodinesamplermonth(Base):
    __tablename__ = 'iodinesamplermonth'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Iodinesamplerrecord(Base):
    __tablename__ = 'iodinesamplerrecord'

    recordId = db.Column(INTEGER(11), primary_key=True)
    stationId = db.Column(db.String(50))
    At = db.Column(BIGINT(20), index=True)
    WorkID = db.Column(db.String(50))
    BeginTime = db.Column(BIGINT(20))
    EndTime = db.Column(BIGINT(20))
    RealtimeFlow = db.Column(db.Float)
    TotalFlow = db.Column(db.Float)
    StandardVolume = db.Column(db.Float)
    WorkingVolume = db.Column(db.Float)
    AmbientTemp = db.Column(db.Float)
    AmbientHumi = db.Column(db.Float)
    Pressure = db.Column(db.Float)
    FaultAlarm = db.Column(db.String(10))
    UpdateFlag = db.Column(TINYINT(1))


class Iodinesampleryear(Base):
    __tablename__ = 'iodinesampleryear'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Largea(Base):
    __tablename__ = 'largeas'

    recordId = db.Column(INTEGER(11), primary_key=True)
    stationId = db.Column(db.String(50))
    At = db.Column(BIGINT(20), index=True)
    WorkID = db.Column(db.String(50))
    BeginTime = db.Column(BIGINT(20))
    EndTime = db.Column(BIGINT(20))
    RealtimeFlow = db.Column(db.Float)
    TotalFlow = db.Column(db.Float)
    StandardVolume = db.Column(db.Float)
    WorkingVolume = db.Column(db.Float)
    AmbientTemp = db.Column(db.Float)
    AmbientHumi = db.Column(db.Float)
    Pressure = db.Column(db.Float)
    FaultAlarm = db.Column(db.String(10))


class Largeas1h(Base):
    __tablename__ = 'largeas1h'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Largeas5m(Base):
    __tablename__ = 'largeas5m'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Largeasday(Base):
    __tablename__ = 'largeasday'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Largeasmonth(Base):
    __tablename__ = 'largeasmonth'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Largeasrecord(Base):
    __tablename__ = 'largeasrecord'

    recordId = db.Column(INTEGER(11), primary_key=True)
    stationId = db.Column(db.String(50))
    At = db.Column(BIGINT(20), index=True)
    WorkID = db.Column(db.String(50))
    BeginTime = db.Column(BIGINT(20))
    EndTime = db.Column(BIGINT(20))
    RealtimeFlow = db.Column(db.Float)
    TotalFlow = db.Column(db.Float)
    StandardVolume = db.Column(db.Float)
    WorkingVolume = db.Column(db.Float)
    AmbientTemp = db.Column(db.Float)
    AmbientHumi = db.Column(db.Float)
    Pressure = db.Column(db.Float)
    FaultAlarm = db.Column(db.String(10))
    UpdateFlag = db.Column(TINYINT(1))


class Largeasyear(Base):
    __tablename__ = 'largeasyear'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Lastupdate(Base):
    __tablename__ = 'lastupdate'

    recordId = db.Column(INTEGER(11), primary_key=True)
    SNOENO = db.Column(db.String(50))
    At = db.Column(BIGINT(20), index=True)


class Logrecord(Base):
    __tablename__ = 'logrecord'

    recordId = db.Column(INTEGER(11), primary_key=True)
    stationId = db.Column(db.String(50))
    At = db.Column(BIGINT(20), index=True)
    content = db.Column(db.String(100))


class N42filerecord(Base):
    __tablename__ = 'n42filerecord'

    recordId = db.Column(INTEGER(11), primary_key=True)
    stationId = db.Column(db.String(50))
    At = db.Column(BIGINT(20), index=True)
    ID = db.Column(db.String(50))
    FilePath = db.Column(db.String(200))


class Naidoseraterecord(Base):
    __tablename__ = 'naidoseraterecord'

    recordId = db.Column(INTEGER(11), primary_key=True)
    stationId = db.Column(db.String(50))
    At = db.Column(BIGINT(20), index=True)
    DoseRate = db.Column(db.Float)


class Naidoseraterecord1h(Base):
    __tablename__ = 'naidoseraterecord1h'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Naidoseraterecord5m(Base):
    __tablename__ = 'naidoseraterecord5m'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Naidoseraterecordday(Base):
    __tablename__ = 'naidoseraterecordday'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Naidoseraterecordmonth(Base):
    __tablename__ = 'naidoseraterecordmonth'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Naidoseraterecordyear(Base):
    __tablename__ = 'naidoseraterecordyear'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Naisperecord(Base):
    __tablename__ = 'naisperecord'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(100))
    Spe = db.Column(db.Text)
    NuclideResult = db.Column(db.String(2000))


class Serverstatu(Base):
    __tablename__ = 'serverstatus'

    recordId = db.Column(INTEGER(11), primary_key=True)
    name = db.Column(db.String(30))
    Ip = db.Column(db.String(20))
    status = db.Column(db.String(10))
    lastupdatetime = db.Column(BIGINT(64))
    port = db.Column(INTEGER(11))
    priority = db.Column(INTEGER(11))
    type = db.Column(db.String(30))


class Stationinfo(Base):
    __tablename__ = 'stationinfo'

    stationId = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    stationHost = db.Column(db.String(50))
    status = db.Column(db.String(10))


class Tritiumsampler(Base):
    __tablename__ = 'tritiumsampler'

    recordId = db.Column(INTEGER(11), primary_key=True)
    stationId = db.Column(db.String(50))
    At = db.Column(BIGINT(20), index=True)
    WorkID = db.Column(db.String(50))
    BeginTime = db.Column(BIGINT(20))
    EndTime = db.Column(BIGINT(20))
    RealtimeFlow = db.Column(db.Float)
    TotalFlow = db.Column(db.Float)
    StandardVolume = db.Column(db.Float)
    WorkingVolume = db.Column(db.Float)
    AmbientTemp = db.Column(db.Float)
    AmbientHumi = db.Column(db.Float)
    Pressure = db.Column(db.Float)
    FaultAlarm = db.Column(db.String(10))


class Tritiumsampler1h(Base):
    __tablename__ = 'tritiumsampler1h'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Tritiumsampler5m(Base):
    __tablename__ = 'tritiumsampler5m'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Tritiumsamplerday(Base):
    __tablename__ = 'tritiumsamplerday'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Tritiumsamplermonth(Base):
    __tablename__ = 'tritiumsamplermonth'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Tritiumsamplerrecord(Base):
    __tablename__ = 'tritiumsamplerrecord'

    recordId = db.Column(INTEGER(11), primary_key=True)
    stationId = db.Column(db.String(50))
    At = db.Column(BIGINT(20), index=True)
    WorkID = db.Column(db.String(50))
    BeginTime = db.Column(BIGINT(20))
    EndTime = db.Column(BIGINT(20))
    RealtimeFlow = db.Column(db.Float)
    TotalFlow = db.Column(db.Float)
    StandardVolume = db.Column(db.Float)
    WorkingVolume = db.Column(db.Float)
    AmbientTemp = db.Column(db.Float)
    AmbientHumi = db.Column(db.Float)
    Pressure = db.Column(db.Float)
    FaultAlarm = db.Column(db.String(10))
    UpdateFlag = db.Column(TINYINT(1))


class Tritiumsampleryear(Base):
    __tablename__ = 'tritiumsampleryear'

    recordId = db.Column(INTEGER(11), primary_key=True)
    At = db.Column(BIGINT(20))
    stationId = db.Column(db.String(50))
    Avg = db.Column(db.Float)
    Max = db.Column(db.Float)
    Min = db.Column(db.Float)


class Userinfo(db.Model):
    __tablename__ = 'userinfo'

    username = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(50))


class Wsrecord(Base):
    __tablename__ = 'wsrecord'

    recordId = db.Column(INTEGER(11), primary_key=True)
    stationId = db.Column(db.String(50))
    At = db.Column(BIGINT(20), index=True)
    Humidity = db.Column(db.Float)
    Moisture = db.Column(db.Float)
    Pressure = db.Column(db.Float)
    Temperature = db.Column(db.Float)
    WindDirection = db.Column(INTEGER(11))
    WindSpeed = db.Column(db.Float)


class Wsrecord1h(Base):
    __tablename__ = 'wsrecord1h'

    recordId = db.Column(INTEGER(11), primary_key=True)
    stationId = db.Column(db.String(50))
    At = db.Column(BIGINT(20), index=True)
    HumidityAvg = db.Column(db.Float)
    MoistureAvg = db.Column(db.Float)
    PressureAvg = db.Column(db.Float)
    TemperatureAvg = db.Column(db.Float)
    WindDirectionAvg = db.Column(INTEGER(11))
    WindSpeedAvg = db.Column(db.Float)
    HumidityMax = db.Column(db.Float)
    MoistureMax = db.Column(db.Float)
    PressureMax = db.Column(db.Float)
    TemperatureMax = db.Column(db.Float)
    WindDirectionMax = db.Column(INTEGER(11))
    WindSpeedMax = db.Column(db.Float)
    HumidityMin = db.Column(db.Float)
    MoistureMin = db.Column(db.Float)
    PressureMin = db.Column(db.Float)
    TemperatureMin = db.Column(db.Float)
    WindDirectionMin = db.Column(INTEGER(11))
    WindSpeedMin = db.Column(db.Float)


class Wsrecord5m(Base):
    __tablename__ = 'wsrecord5m'

    recordId = db.Column(INTEGER(11), primary_key=True)
    stationId = db.Column(db.String(50))
    At = db.Column(BIGINT(20), index=True)
    HumidityAvg = db.Column(db.Float)
    MoistureAvg = db.Column(db.Float)
    PressureAvg = db.Column(db.Float)
    TemperatureAvg = db.Column(db.Float)
    WindDirectionAvg = db.Column(INTEGER(11))
    WindSpeedAvg = db.Column(db.Float)
    HumidityMax = db.Column(db.Float)
    MoistureMax = db.Column(db.Float)
    PressureMax = db.Column(db.Float)
    TemperatureMax = db.Column(db.Float)
    WindDirectionMax = db.Column(INTEGER(11))
    WindSpeedMax = db.Column(db.Float)
    HumidityMin = db.Column(db.Float)
    MoistureMin = db.Column(db.Float)
    PressureMin = db.Column(db.Float)
    TemperatureMin = db.Column(db.Float)
    WindDirectionMin = db.Column(INTEGER(11))
    WindSpeedMin = db.Column(db.Float)


class Wsrecordday(Base):
    __tablename__ = 'wsrecordday'

    recordId = db.Column(INTEGER(11), primary_key=True)
    stationId = db.Column(db.String(50))
    At = db.Column(BIGINT(20), index=True)
    HumidityAvg = db.Column(db.Float)
    MoistureAvg = db.Column(db.Float)
    PressureAvg = db.Column(db.Float)
    TemperatureAvg = db.Column(db.Float)
    WindDirectionAvg = db.Column(INTEGER(11))
    WindSpeedAvg = db.Column(db.Float)
    HumidityMax = db.Column(db.Float)
    MoistureMax = db.Column(db.Float)
    PressureMax = db.Column(db.Float)
    TemperatureMax = db.Column(db.Float)
    WindDirectionMax = db.Column(INTEGER(11))
    WindSpeedMax = db.Column(db.Float)
    HumidityMin = db.Column(db.Float)
    MoistureMin = db.Column(db.Float)
    PressureMin = db.Column(db.Float)
    TemperatureMin = db.Column(db.Float)
    WindDirectionMin = db.Column(INTEGER(11))
    WindSpeedMin = db.Column(db.Float)


class Wsrecordmonth(Base):
    __tablename__ = 'wsrecordmonth'

    recordId = db.Column(INTEGER(11), primary_key=True)
    stationId = db.Column(db.String(50))
    At = db.Column(BIGINT(20), index=True)
    HumidityAvg = db.Column(db.Float)
    MoistureAvg = db.Column(db.Float)
    PressureAvg = db.Column(db.Float)
    TemperatureAvg = db.Column(db.Float)
    WindDirectionAvg = db.Column(INTEGER(11))
    WindSpeedAvg = db.Column(db.Float)
    HumidityMax = db.Column(db.Float)
    MoistureMax = db.Column(db.Float)
    PressureMax = db.Column(db.Float)
    TemperatureMax = db.Column(db.Float)
    WindDirectionMax = db.Column(INTEGER(11))
    WindSpeedMax = db.Column(db.Float)
    HumidityMin = db.Column(db.Float)
    MoistureMin = db.Column(db.Float)
    PressureMin = db.Column(db.Float)
    TemperatureMin = db.Column(db.Float)
    WindDirectionMin = db.Column(INTEGER(11))
    WindSpeedMin = db.Column(db.Float)


class Wsrecordyear(Base):
    __tablename__ = 'wsrecordyear'

    recordId = db.Column(INTEGER(11), primary_key=True)
    stationId = db.Column(db.String(50))
    At = db.Column(BIGINT(20), index=True)
    HumidityAvg = db.Column(db.Float)
    MoistureAvg = db.Column(db.Float)
    PressureAvg = db.Column(db.Float)
    TemperatureAvg = db.Column(db.Float)
    WindDirectionAvg = db.Column(INTEGER(11))
    WindSpeedAvg = db.Column(db.Float)
    HumidityMax = db.Column(db.Float)
    MoistureMax = db.Column(db.Float)
    PressureMax = db.Column(db.Float)
    TemperatureMax = db.Column(db.Float)
    WindDirectionMax = db.Column(INTEGER(11))
    WindSpeedMax = db.Column(db.Float)
    HumidityMin = db.Column(db.Float)
    MoistureMin = db.Column(db.Float)
    PressureMin = db.Column(db.Float)
    TemperatureMin = db.Column(db.Float)
    WindDirectionMin = db.Column(INTEGER(11))
    WindSpeedMin = db.Column(db.Float)
