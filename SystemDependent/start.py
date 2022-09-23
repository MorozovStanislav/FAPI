import uvicorn
import config

if __name__ == '__main__':
    uvicorn.run('next_app:next_app',host=config.host,port=config.port,reload=config.reload)