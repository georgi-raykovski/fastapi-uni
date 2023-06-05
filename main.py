from fastapi import FastAPI, status, HTTPException, Depends
from request_types import RequestBody
from model import get_target_idx, get_model_instance, NaiveBayesModel
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def root():
    """
       Root endpoint to test the API.
    """
    return {"message": "Hello World"}


@app.get('/healthcheck', status_code=status.HTTP_200_OK)
def perform_healthcheck():
    """
       Health check endpoint to verify the API's availability.
    """
    return {'healthcheck': 'Everything OK!'}


@app.post("/fit", status_code=status.HTTP_200_OK)
def fit(model: NaiveBayesModel = Depends(get_model_instance)):
    """
    Endpoint to trigger the training process for the model.
    """
    try:
        model.fit()
        return {"message": "Model training complete!"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@app.post("/predict_single/", status_code=status.HTTP_200_OK)
def predict_single(data: RequestBody, model: NaiveBayesModel = Depends(get_model_instance)):
    """
        Endpoint to predict the class based on input features.
    """
    try:
        test_data = [[
            data.sepal_length,
            data.sepal_width,
            data.petal_length,
            data.petal_width
        ]]

        result = model.predict(test_data)

        return {'class': get_target_idx(result[0])}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@app.get("/evaluation", status_code=status.HTTP_200_OK)
def evaluate_model(model: NaiveBayesModel = Depends(get_model_instance)):
    """
       Endpoint to perform model evaluation on a predefined evaluation dataset.
    """
    try:
        report = model.get_evaluation_metrics()
        return JSONResponse(content=report)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
