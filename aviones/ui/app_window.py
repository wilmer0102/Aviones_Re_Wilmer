from services.avion_service import AvionService
from uuid import UUID
import tkinter as tk
from tkinter import ttk, messagebox

class AppWindow(tk.Tk):
    is_to_update_avion = False
    avion_uuid_to_update = ""

    def __init__(self, service: AvionService) -> None:
        super().__init__()
        self.service = service
        self.title("Tkinter con POO + Capas")
        self.geometry("600x500")
        self.create_widget()

    def create_widget(self):
        self.render_entries()

        self.insert_btn = tk.Button(
            self, text="Ingresa un avion", command=self.insert_avion)
        self.insert_btn.pack()

        self.delete_btn = tk.Button(
            self, text="Eliminar", command=self.delete_avion)
        self.delete_btn.pack()

        self.update_btn = tk.Button(
            self, text="Actualizar", command=self.update_avion)
        self.update_btn.pack()

        self.create_data_table()
        self.render_data_table()

    def render_entries(self):
        label_aerolinea = tk.Label(self, text="Ingresa tu aerolinea")
        label_aerolinea.pack()
        self.entry_aerolinea = tk.Entry(self)
        self.entry_aerolinea.pack()

        label_modelo = tk.Label(self, text="Ingresa tu modelo")
        label_modelo.pack()
        self.entry_modelo = tk.Entry(self)
        self.entry_modelo.pack()

        label_capacidad = tk.Label(self, text="Ingresa tu capacidad")
        label_capacidad.pack()
        self.entry_capacidad = tk.Entry(self)
        self.entry_capacidad.pack()

        label_destino = tk.Label(self, text="Ingresa tu destino")
        label_destino.pack()
        self.entry_destino = tk.Entry(self)
        self.entry_destino.pack()

    def clear_entries(self):
        self.entry_aerolinea.delete(0, "end")
        self.entry_modelo.delete(0, "end")
        self.entry_capacidad.delete(0, "end")
        self.entry_destino.delete(0, "end")
        self.entry_aerolinea.focus()

    def insert_avion(self):
        aerolinea = self.entry_aerolinea.get()
        modelo = self.entry_modelo.get()
        capacidad = self.entry_capacidad.get()
        destino = self.entry_destino.get()

        if self.is_to_update_avion:
            uuid = UUID(self.avion_uuid_to_update)
            self.service.update_one(uuid, aerolinea, modelo, int(capacidad), destino)
            self.clear_entries()
            self.render_data_table()
            messagebox.showinfo(title="Información", message="Avion actualizado!")
            self.is_to_update_avion = False
            self.avion_uuid_to_update = ""
            self.insert_btn.config(text="Ingresa un avion")
            return

        self.service.create_one(aerolinea, modelo, int(capacidad), destino)
        self.render_data_table()
        self.clear_entries()

    def create_data_table(self):
        self.tree = ttk.Treeview(self, columns=("uuid", "aerolinea", "modelo", "capacidad", "destino"), show="headings")

        self.tree.column("uuid", anchor="center", width=100)
        self.tree.column("aerolinea", anchor="center", width=100)
        self.tree.column("modelo", anchor="center", width=100)
        self.tree.column("capacidad", anchor="center", width=100)
        self.tree.column("destino", anchor="center", width=100)

        self.tree.heading("uuid", text="ID")
        self.tree.heading("aerolinea", text="Aerolinea")
        self.tree.heading("modelo", text="Modelo")
        self.tree.heading("capacidad", text="Capacidad")
        self.tree.heading("destino", text="Destino")
        self.tree.pack()

    def delete_avion(self):
        selection = self.tree.selection()
        if not selection:
            messagebox.showinfo(title="Información", message="No hay avion para eliminar!")
            return
        selected_avion = self.tree.item(selection[0], "values")
        self.service.delete_one(UUID(selected_avion[0]))
        self.render_data_table()

    def update_avion(self):
        selection = self.tree.selection()
        if not selection:
            messagebox.showinfo(title="Información", message="No hay avion para actualizar!")
            return
        selected_avion = self.tree.item(selection[0], "values")
        uuid, aerolinea, modelo, capacidad, destino = selected_avion
        self.entry_aerolinea.insert(0, aerolinea)
        self.entry_modelo.insert(0, modelo)
        self.entry_capacidad.insert(0, capacidad)
        self.entry_destino.insert(0, destino)
        self.is_to_update_avion = True
        self.avion_uuid_to_update = uuid
        self.insert_btn.config(text="Actualizar avion")

    def render_data_table(self):
        aviones = self.service.find_all()
        for item in self.tree.get_children():
            self.tree.delete(item)
        for avion in aviones:
            avion_uuid = str(avion.uuid)
            self.tree.insert("", "end", values=(
                avion_uuid, avion.aerolinea, avion.modelo, avion.capacidad, avion.destino))