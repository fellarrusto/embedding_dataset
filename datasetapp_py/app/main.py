import json
import io
from app.utils import get_random_pdf_text
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.models import DataEntry, Dataset
from app.database import SessionLocal, engine
from app.models import Base

app = FastAPI()

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

Base.metadata.create_all(bind=engine)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/random-pdf/")
async def random_pdf():
    return {"text": get_random_pdf_text()}

@app.post("/submit/")
async def submit_data(data: DataEntry):
    db = SessionLocal()
    try:
        new_entry = Dataset(anchor=data.anchor, positive=data.positive)
        db.add(new_entry)
        db.commit()
        return {"message": "Dati inseriti con successo"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()

@app.get("/generate_jsonl/")
async def generate_jsonl():
    db = SessionLocal()
    try:
        records = db.query(Dataset).all()
        jsonl_content = "\n".join([json.dumps({"id": r.id, "anchor": r.anchor, "positive": r.positive}) for r in records])
        
        # Creare un file in memoria
        file_like = io.StringIO(jsonl_content)
        
        # Usare StreamingResponse per avviare il download
        return StreamingResponse(file_like, media_type="application/jsonl", headers={"Content-Disposition": "attachment; filename=dataset.jsonl"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()