from src.domain.info import InfoRepository, Info
import sys

sys.path.insert(0, "")


database_path = "data/database.db"

info_repository = InfoRepository(database_path)

info_repository.save(Info(app_my_notes="f5-my-notes-app2"))
