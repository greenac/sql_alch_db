# coding: utf-8
from sqlalchemy import ARRAY, Boolean, Column, DateTime, Float, ForeignKey, Index, Integer, JSON, Numeric, String, Text, UniqueConstraint
from sqlalchemy.schema import FetchedValue
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql.base import INET
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(512))
    avatarUrl = db.Column(db.String(255))
    firstName = db.Column(db.String(255))
    lastName = db.Column(db.String(255))
    phoneNumber = db.Column(db.String(255))
    dateOfBirth = db.Column(db.String(255))
    loginReward = db.Column(db.Boolean)
    ssnSerialNumber = db.Column(db.Text)
    microdepositEnabled = db.Column(db.Boolean, server_default=db.FetchedValue())
    facebookId = db.Column(db.String(255), unique=True)
    facebookToken = db.Column(db.String(255))
    tosAcceptedAt = db.Column(db.DateTime(True))
    deviceId = db.Column(db.Text)
    dwollaId = db.Column(db.Text)
    identityCheckState = db.Column(db.String(255), server_default=db.FetchedValue())
    veratadStatus = db.Column(NullType, server_default=db.FetchedValue())
    veratadTimestamp = db.Column(db.DateTime(True))
    payoutStatus = db.Column(NullType, server_default=db.FetchedValue())
    pushId = db.Column(db.String(255))
    pushToken = db.Column(db.String(255))
    state = db.Column(db.String(255), server_default=db.FetchedValue())
    primaryBankAccountId = db.Column(db.Integer)
    inTheGame = db.Column(db.Boolean, server_default=db.FetchedValue())
    gotBonusWin = db.Column(db.Boolean, server_default=db.FetchedValue())
    inTheGameSince = db.Column(db.DateTime(True))
    inDeposit = db.Column(db.Boolean, server_default=db.FetchedValue())
    inDepositSince = db.Column(db.DateTime(True))
    requireW9 = db.Column(db.Boolean, server_default=db.FetchedValue())
    availableBalance = db.Column(db.Numeric(20, 8), server_default=db.FetchedValue())
    totalBalance = db.Column(db.Numeric(20, 8), server_default=db.FetchedValue())
    level = db.Column(db.Integer)
    loginOption = db.Column(db.String(255))
    lastLoginBonus = db.Column(db.DateTime(True))
    bankLinkedAt = db.Column(db.DateTime(True))
    shouldRelinkBankApp = db.Column(db.Boolean, server_default=db.FetchedValue())
    quovoUserId = db.Column(db.Integer, unique=True)
    lastSessionStartedAt = db.Column(db.DateTime(True))
    activatedAt = db.Column(db.DateTime(True))
    lastClosedAt = db.Column(db.DateTime(True))
    afMediaSource = db.Column(db.String(255))
    balanceChecked = db.Column(db.Boolean, server_default=db.FetchedValue())
    ip = db.Column(db.String(255))
    gaid = db.Column(db.String(255))
    idfa = db.Column(db.String(255))
    idfv = db.Column(db.String(255))
    instanceId = db.Column(db.String(255))
    riskScore = db.Column(db.Integer, server_default=db.FetchedValue())
    isTrusted = db.Column(db.Boolean, server_default=db.FetchedValue())
    transitions = db.Column(db.JSON)
    createdAt = db.Column(db.DateTime(True), nullable=False)
    updatedAt = db.Column(db.DateTime(True), nullable=False)
