from fastapi import FastAPI

app= FastAPI()


BANDS=[
    {id: 1, "name": "The Beatles", "genre": "Rock"},
    {id: 2, "name": "Nirvana", "genre": "Grunge"},
    {id: 3, "name": "Led Zeppelin", "genre": "Rock"},
    {id: 4, "name": "The Rolling Stones", "genre": "Rock"}
    ]


@app.get("/")
async def root():
    return {"message": "Hello World"}   
    
