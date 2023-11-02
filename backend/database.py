from sqlalchemy import create_engine


url = "postgres://postgres:zaq12wsx@localhost:5432/testing"

engine = create_engine(
    url
)