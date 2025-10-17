from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date
class Producer(BaseModel):
    name: str
    address: str
    city: str
    state: str
    zip: str
    contactName: Optional[str]
    phone: Optional[str]
    fax: Optional[str]
    email: Optional[str]

class Insured(BaseModel):
    name: str
    address: str
    city: str
    state: str
    zip: str

class Insurer(BaseModel):
    insurerName: str
    naicNumber: str
    label: str

class GeneralLiabilityLimits(BaseModel):
    eachOccurrence: str
    damageToRentedPremises: str
    medExp: str
    personalInjury: str
    generalAggregate: str
    productsAggregate: str

class CommercialPolicy(BaseModel):
    type: str
    insrLtr: str
    addlInsd: bool
    subrWvd: bool
    policyNumber: str
    policyEff: date  
    policyExp: date  
    limits: dict  # You can replace with separate limits model per type

class CertificateHolder(BaseModel):
    name: str
    address: str

class Signature(BaseModel):
    signedBy: str
    title: str
    signatureImage: str
    signedDate: date  

class Certificate(BaseModel):
    date: date  
    certificateNumber: str
    revisionNumber: str
    producer: Producer
    insured: Insured
    insurers: List[Insurer]
    policies: List[CommercialPolicy]
    descriptionOfOperations: Optional[str]
    certificateHolder: CertificateHolder
    signature: Signature
    issuedBy: Optional[str]
