from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func
from microserv_api import models

def get_regions(db: Session):
    results = db.query(models.Region).all()
    return results


def get_region_by_id(db: Session, region_id: int):
    results = db.query(models.Region).filter(models.Region.region_id == region_id).first()
    return results


def get_region_depts_by_id(db: Session, region_id: int):
    results = db.query(models.Region).options(joinedload(models.Region.depts)).filter(models.Region.region_id == region_id).all()
    print(type(results))
    return results

def get_department_by_id(db: Session, dept_id: int):
    results = db.query(models.Department).filter(models.Department.dept_id == str(dept_id)).first()
    return results

def get_municipality_by_code(db: Session, code: int):
    results = db.query(models.Municipality).filter(models.Municipality.mun_code == str(code)).all()
    return results