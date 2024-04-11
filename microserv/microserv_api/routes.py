from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from microserv_api import crud
from microserv_api import app, get_db


@app.get("/region")
async def get_regions(db: Session = Depends(get_db)):
    results = crud.get_regions(db)
    if results is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No department found")
    return results


@app.get("/region/{region_id}")
async def get_region_by_id(region_id: int, db: Session = Depends(get_db)):
    results = crud.get_region_by_id(db, region_id=region_id)
    if results is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No region found")
    return results


@app.get("/region/depts/{region_id}")
async def get_region_depts_by_id(region_id: int, db: Session = Depends(get_db)):
    results = crud.get_region_depts_by_id(db, region_id=region_id)
    if results is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No region found")
    return results

@app.get("/dept/{dept_id}")
async def get_department_by_id(dept_id: int, db: Session = Depends(get_db)):
    results = crud.get_department_by_id(db, dept_id=dept_id)
    if results is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No department found")
    return results

@app.get("/mun/code/{code}")
async def get_municipality_by_code(code: int, db: Session = Depends(get_db)):
    results = crud.get_municipality_by_code(db, code=code)
    if results is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No municipality found")
    return results