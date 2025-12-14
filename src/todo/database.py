from pathlib import Path

from sqlalchemy.engine.base import Engine
from sqlmodel import Session, SQLModel, create_engine, select

from todo.task import Task

# Module-level engine (singleton - created once, reused)
_engine = None


def get_db_path() -> Path:
    """
    Get the path to the database file.
    """

    db_dir = Path.home() / ".todocli"
    db_dir.mkdir(exist_ok=True)
    return db_dir / "todo.db"


def get_engine() -> Engine:
    """
    Get or create the database engine (singleton pattern).
    """

    global _engine
    if _engine is None:
        db_path = get_db_path()
        db_url = f"sqlite:///{db_path}"
        _engine = create_engine(db_url, echo=False, connect_args={"check_same_thread": False, "timeout": 10})
    return _engine


def initialize_database() -> None:
    """
    Initialize the database (create tables if they don't exist).
    """

    engine = get_engine()

    # SQLModel/metadata is a catalog of all models defined with SQLModel
    #   Reads all your SQLModel class definitions
    #   Generates CREATE TABLE SQL statements
    #   Executes them on the database (only if tables don't exist)

    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    """
    Get a new database session.
    """

    engine = get_engine()
    return Session(engine)


def close_engine() -> None:
    """
    Close the database engine and all connections.
    """

    global _engine
    if _engine is not None:
        _engine.dispose()
        _engine = None


if __name__ == "__main__":
    # Initialize database (create tables)
    initialize_database()

    # Use session for operations
    with get_session() as session:
        task = Task(description="Sample Task", priority=1, status=0)
        print(f"Initialized database and created task: {task}")
        session.add(task)
        session.commit()

        # Query
        statement = select(Task).where(Task.description == "Sample Task")
        task_retrieved = session.exec(statement).first()
        print(task_retrieved)

    # Properly close engine at end of program
    close_engine()
    print("Database engine closed.")
