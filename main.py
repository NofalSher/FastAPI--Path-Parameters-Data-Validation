from fastapi import FastAPI, HTTPException

app= FastAPI()

BANDS = [
    {"id": 1, "name": "The Beatles", "genre": "Rock"},
    {"id": 2, "name": "Nirvana", "genre": "Grunge"},
    {"id": 3, "name": "Led Zeppelin", "genre": "Rock"},
    {"id": 4, "name": "The Rolling Stones", "genre": "Rock"}
]


@app.get("/bands")
async def bands() -> list[dict]:
    return BANDS

@app.get("/bands/{band_id}", status_code=206)
async def band(band_id: int) -> dict:
    for band in BANDS:
        if band["id"] == band_id:
            return band
        if band is None:
            raise HTTPException(status_code=404, detail="Band not found")        
    return {"error": "Band not found"}


@app.get("/bands/genre/{genre}")
async def bands_by_genre(genre: str) -> list[dict]:
    filtered_bands = [band for band in BANDS if band["genre"].lower() == genre.lower()]
    if not filtered_bands:
        raise HTTPException(status_code=404, detail="No bands found for this genre")
    return filtered_bands