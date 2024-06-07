from datetime import datetime
from fastapi import APIRouter, HTTPException
from app.models.request import AdditionRequest
from app.models.response import AdditionResponse
from app.services.addition_service import perform_addition
from app.utils.logging_config import logger


router = APIRouter()


@router.post("/add", response_model=AdditionResponse)
async def add_numbers(request: AdditionRequest):
    try:
        logger.info(f"Received request with batchid: {request}")
        started_at = datetime.utcnow()
        result = perform_addition(request.payload)
        completed_at = datetime.utcnow()
        value = AdditionResponse(
            batchid=request.batchid,
            response=result,
            status="complete",
            started_at=started_at,
            completed_at=completed_at
        )
        logger.info(f"Completed processing batchid: {value}")
        return value
    except Exception as e:
        logger.error(f"Error processing batchid: {request} - {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
