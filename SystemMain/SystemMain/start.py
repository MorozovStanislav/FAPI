import uvicorn
import config

if __name__ == '__main__':
    uvicorn.run('basic_app:basic_app',host=config.host,port=config.port,reload=config.reload)