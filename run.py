from app import app
from config import DevelopmentConfig

# application config
app.config.from_object(DevelopmentConfig)

if __name__ == '__main__':
    app.run()
