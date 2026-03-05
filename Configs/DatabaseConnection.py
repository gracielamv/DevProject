from sqlalchemy import create_engine, text

# from Neon Database
DATABASE_URL = "postgresql://neondb_owner:npg_liPJOq0xy5nc@ep-holy-glade-a8iwuwwe-pooler.eastus2.azure.neon.tech/ba_database?sslmode=require&channel_binding=require"

engine = create_engine(DATABASE_URL)

"""
if __name__ == '__main__':
    try:
        with engine.connect() as conn:
            result = conn.execute(text('SELECT * from places'))
            for i in result:
                print(f"The name retrieved is {i[1]}")
                # print(i)
    except Exception as e:
        print(f"Connection failed: more details in the following:"
              f"{e}")
"""