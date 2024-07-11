from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from typing import List, Optional
import shutil
import os
import uuid

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend URL if known
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load DialoGPT-medium model and tokenizer
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Pydantic models
class ChatRequest(BaseModel):
    user_input: str
    character_id: str

class ChatResponse(BaseModel):
    response: str

class CharacterBase(BaseModel):
    name: str
    greeting: str
    personality_description: str
    backstory: str

class CharacterCreate(CharacterBase):
    pass

class Character(CharacterBase):
    id: str
    avatar_url: Optional[str] = None

# In-memory storage for characters (replace with database in production)
characters_db = {}

# Create character endpoint
@app.post("/characters/", response_model=Character)
async def create_character(character: CharacterCreate, avatar: UploadFile = File(...)):
    char_id = str(uuid.uuid4())
    avatar_filename = f"{char_id}_{avatar.filename}"
    avatar_path = os.path.join("avatars", avatar_filename)

    with open(avatar_path, "wb") as buffer:
        shutil.copyfileobj(avatar.file, buffer)

    new_character = Character(
        id=char_id,
        name=character.name,
        greeting=character.greeting,
        personality_description=character.personality_description,
        backstory=character.backstory,
        avatar_url=f"/avatars/{avatar_filename}"
    )
    characters_db[char_id] = new_character
    return new_character

# List all characters endpoint
@app.get("/characters/", response_model=List[Character])
async def list_characters():
    return list(characters_db.values())

# Get character by ID endpoint
@app.get("/characters/{char_id}", response_model=Character)
async def get_character(char_id: str):
    character = characters_db.get(char_id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character

# Chat endpoint
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    user_input = request.user_input
    character = characters_db.get(request.character_id)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    
    # Customize the conversation based on character's backstory and personality
    prompt = f"{character.greeting}\n\n{character.backstory}\n\nUser: {user_input}\n{character.name}:"
    try:
        responses = generator(prompt, max_length=100, num_return_sequences=1)
        response_text = responses[0]['generated_text'].split(f"{character.name}:")[1].strip()
        return ChatResponse(response=response_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)





