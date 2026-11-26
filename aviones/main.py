from repositories.avion_repository import AvionRepository
from services.avion_service import AvionService
from ui.app_window import AppWindow

def main():
    repository = AvionRepository()
    service = AvionService(repository)
    app_window = AppWindow(service)
    app_window.mainloop()

if __name__ == "__main__":
    main()
    