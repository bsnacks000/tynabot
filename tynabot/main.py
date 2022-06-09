import re
from typing import Any, Dict, Optional, Tuple
from fastapi import Depends, FastAPI, Query, HTTPException, Request
from fastapi.responses import JSONResponse
import pydantic

from starlette.exceptions import HTTPException as StarletteHTTPException

from typing import Optional

description="""
## The API that just wants to be left alone... 
Maybe I can help you but I'm definitely rolling my eyes.

"""

app = FastAPI(title='tynabot', version='6.6.6', description=description)

@app.exception_handler(404)
async def unicorn_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": f"Oh my gadddd.... read the fucking manual ---> {request.app.docs_url}"},
    )



class SearchParams(pydantic.BaseModel): 
    spew: str=Query(None, description='literally anything...')



class Response(pydantic.BaseModel): 
    """ Our spews are only well formed..."""
    spew : Dict[str, Any]


_speaks = [
    'Ya daag... do a went', 
    'Yeah nah...', 
    'Nah yeah...',
    "why does george's open at 7am? what someone wants gravy fries at 5am?", 
    "You can only humor me for so long. At some point there WILL be a reckoning...", 
    "Sit yeetself down, face the wall, and think about your bad decisions...",
    "People don't realize how much damage the human jaw can do...",
    "Get in loser... we're going caring!",
    "start the rapture", 
    "Get in loser... we're going to therapy!", 
    "Thumb in bum and mind in neutral!"
]

_sizes = [ 
    "tiny", 
    "large", 
    "medium", 
    "xtra-large"
]

_quality = [
    "chipped", 
    "shiny", 
    "grimy", 
    "fake",
    "flawless"
]

_urls = [
    'https://www.youtube.com/watch?v=9QCgqQdmr0M', 
    'https://www.youtube.com/watch?v=0DfGf4M3QZo', 
    'https://www.youtube.com/watch?v=5XIiuu26rr0', 
    'https://media.giphy.com/media/zfNAMCrhSQzte/giphy.gif', 
    'https://media.giphy.com/media/kAbWiuvtzoG3e/giphy.gif', 
    'https://media.giphy.com/media/MFVI64gIopnOTDeeO9/giphy.gif', 
    'https://media.giphy.com/media/DgKmkc1ALiKukjTGOw/giphy.gif', 
    'https://media.giphy.com/media/Nwu2uXxlN74VG/giphy.gif',
]


import random

def _look_for_treasures(s: str) -> Tuple[Optional[int], str]: 
    
    s = s.lower()
    if re.search(r"(gold) (teeth)", s): 
        return Response(spew={
            'message': random.choice(_speaks),
            'amount': random.randint(1, 666), 
            'size': random.choice(_sizes),
            'quality': random.sample(_quality, 2)
        })        
    else: 
        raise HTTPException(status_code=400, detail={"message": f'{random.choice(_speaks)}', "distraction": f'{random.choice(_urls)}'})


@app.get('/', tags=['get away from me'], response_model=Response)
async def look_for_treasures(params: SearchParams=Depends()):
    """Checks the search for special bois and delivers an appropriate response.
    """ 
    if not params.spew: 
        raise HTTPException(status_code=404, detail="Don't be sorry just be better.")
    return _look_for_treasures(params.spew)
