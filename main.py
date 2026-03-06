from fastapi import FastAPI
import uvicorn

import routes.deployments_routes.deployment_api

app = FastAPI()

app.include_router(routes.deployments_routes.deployment_api.router)

def main():
    uvicorn.run(app, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()