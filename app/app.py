import os

from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


database = []


class Event(BaseModel):
    name: str
    description: str
    quantity_of_tickets: int
    is_sold: bool = False
    owner: str
    date: str
    expires_sel_date: str


@app.post('/event')
async def create_event(event: Event) -> Event:
    database.append(event)
    return event


@app.get('/event/{event_id}')
async def list_a_event(event_id: int) -> Event:
    if event_id >= len(database):
        raise HTTPException(status_code=404, detail='Evento nao encontrado :(')

    return database[event_id]


@app.get('/events')
async def list_all_events() -> List[Event]:
    return database


@app.put('/event/{event_id}')
async def update_event(event_id: int, event: Event) -> List[Event]:
    if event_id >= len(database):
        raise HTTPException(status_code=404, detail='Evento nao encontrado :(')

    database[event_id] = event
    return database


@app.delete('/event/{event_id}')
async def remove_a_event(event_id: int) -> str:
    if event_id >= len(database):
        raise HTTPException(status_code=404, detail='evento nao encontrado :(')

    database.pop(event_id)
    return 'Evento excluído com sucesso!'
