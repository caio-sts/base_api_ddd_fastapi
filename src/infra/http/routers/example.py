from dependency_injector.wiring import Provide, inject
from src.application.usecases.interfaces.get_all_examples import IGetAllExamples
from src.di import DependencyContainer
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/examples",
    tags=["examples"],
)

@router.get("/")
@inject
async def get_all_examples(
    get_all_examples: IGetAllExamples = Depends(Provide[DependencyContainer.get_all_examples]),
):
    return get_all_examples.execute()
