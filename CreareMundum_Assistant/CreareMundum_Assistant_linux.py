#!/usr/bin/python3

from random import random
from gi.repository import Gtk, Pango

class SearchDialog(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Search", parent, Gtk.DialogFlags.MODAL, buttons=(Gtk.STOCK_FIND, Gtk.ResponseType.OK, Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))

        box = self.get_content_area()

        label = Gtk.Label("Insert text you want to search for:")
        box.add(label)

        self.entry = Gtk.Entry()
        box.add(self.entry)

        self.show_all()

class MyWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="CreareMundum Assistant")
		self.set_border_width(15)
		
		self.grid = Gtk.Grid(column_spacing=8)
		self.add(self.grid)

		self.set_default_size(-1, 350)

		self.create_button_dice()
		self.create_diceview()
		self.create_textview()
		self.create_toolbar()
		self.create_buttons()

	def create_button_dice(self):
		self.button = Gtk.Button(label="Roll the dice")
		self.button.connect("clicked", self.on_button_clicked_dice)

		self.grid.attach(self.button, 0, 2, 1, 1)

	def on_button_clicked_dice(self, widget):
		d4 = randint(1, 4)
		d6 = randint(1, 6)
		d8 = randint(1, 8)
		d10 = randint(1, 10) 
		d12 = randint(1, 12)
		d20 = randint(1, 20)
		d100 = randint(1, 100)
		text="\nDé 4 = %d"%d4+"\nDé 6 = %d"%d6+"\nDé 8 = %d"%8+"\nDé 10 = %d"%d10+"\nDé 12 = %d"%d12+"\nDé 20 = %d"%d20+"\nDé 100 = %d"%d100
		self.text_final.set_text(text)

	def create_diceview(self):
		self.text_final = Gtk.Label()
		self.grid.attach_next_to(self.text_final, self.button, Gtk.PositionType.TOP, 1, 3)
		d4 = randint(1, 4)
		d6 = randint(1, 6)
		d8 = randint(1, 8)
		d10 = randint(1, 10) 
		d12 = randint(1, 12)
		d20 = randint(1, 20)
		d100 = randint(1, 100)
		text="\nDé 4 = %d"%d4+"\nDé 6 = %d"%d6+"\nDé 8 = %d"%8+"\nDé 10 = %d"%d10+"\nDé 12 = %d"%d12+"\nDé 20 = %d"%d20+"\nDé 100 = %d"%d100
		self.text_final.set_text(text)


	def create_toolbar(self):
		toolbar = Gtk.Toolbar()
		self.grid.attach(toolbar, 1, 0, 3, 1)

		button_bold = Gtk.ToolButton.new_from_stock(Gtk.STOCK_BOLD)
		toolbar.insert(button_bold, 0)

		button_italic = Gtk.ToolButton.new_from_stock(Gtk.STOCK_ITALIC)
		toolbar.insert(button_italic, 1)

		button_underline = Gtk.ToolButton.new_from_stock(Gtk.STOCK_UNDERLINE)
		toolbar.insert(button_underline, 2)

		button_bold.connect("clicked", self.on_button_clicked, self.tag_bold)
		button_italic.connect("clicked", self.on_button_clicked, self.tag_italic)
		button_underline.connect("clicked", self.on_button_clicked, self.tag_underline)

		toolbar.insert(Gtk.SeparatorToolItem(), 3)

		radio_justifyleft = Gtk.RadioToolButton()
		radio_justifyleft.set_stock_id(Gtk.STOCK_JUSTIFY_LEFT)
		toolbar.insert(radio_justifyleft, 4)

		radio_justifycenter = Gtk.RadioToolButton.new_with_stock_from_widget(radio_justifyleft, Gtk.STOCK_JUSTIFY_CENTER)
		toolbar.insert(radio_justifycenter, 5)

		radio_justifyright = Gtk.RadioToolButton.new_with_stock_from_widget(radio_justifyleft, Gtk.STOCK_JUSTIFY_RIGHT)
		toolbar.insert(radio_justifyright, 6)

		radio_justifyfill = Gtk.RadioToolButton.new_with_stock_from_widget(radio_justifyleft, Gtk.STOCK_JUSTIFY_FILL)
		toolbar.insert(radio_justifyfill, 7)

		radio_justifyleft.connect("toggled", self.on_justify_toggled,Gtk.Justification.LEFT)
		radio_justifycenter.connect("toggled", self.on_justify_toggled,Gtk.Justification.CENTER)
		radio_justifyright.connect("toggled", self.on_justify_toggled,Gtk.Justification.RIGHT)
		radio_justifyfill.connect("toggled", self.on_justify_toggled,Gtk.Justification.FILL)

		toolbar.insert(Gtk.SeparatorToolItem(), 8)

		button_clear = Gtk.ToolButton.new_from_stock(Gtk.STOCK_CLEAR)
		button_clear.connect("clicked", self.on_clear_clicked)
		toolbar.insert(button_clear, 9)

		toolbar.insert(Gtk.SeparatorToolItem(), 10)

		button_search = Gtk.ToolButton.new_from_stock(Gtk.STOCK_FIND)
		button_search.connect("clicked", self.on_search_clicked)
		toolbar.insert(button_search, 11)

	def create_textview(self):
		scrolledwindow = Gtk.ScrolledWindow()
		scrolledwindow.set_hexpand(True)
		scrolledwindow.set_vexpand(True)
		self.grid.attach(scrolledwindow, 1, 1, 3, 1)

		self.textview = Gtk.TextView()
		self.textbuffer = self.textview.get_buffer()
		self.textbuffer.set_text("Creare Mundum")
		scrolledwindow.add(self.textview)

		self.tag_bold = self.textbuffer.create_tag("bold",weight=Pango.Weight.BOLD)
		self.tag_italic = self.textbuffer.create_tag("italic",style=Pango.Style.ITALIC)
		self.tag_underline = self.textbuffer.create_tag("underline",underline=Pango.Underline.SINGLE)
		self.tag_found = self.textbuffer.create_tag("found",background="yellow")

	def create_buttons(self):
		check_editable = Gtk.CheckButton("Editable")
		check_editable.set_active(True)
		check_editable.connect("toggled", self.on_editable_toggled)
		self.grid.attach(check_editable, 1, 2, 1, 1)

	def on_button_clicked(self, widget, tag):
		bounds = self.textbuffer.get_selection_bounds()
		if len(bounds) != 0:
			start, end = bounds
			self.textbuffer.apply_tag(tag, start, end)

	def on_clear_clicked(self, widget):
		start = self.textbuffer.get_start_iter()
		end = self.textbuffer.get_end_iter()
		self.textbuffer.remove_all_tags(start, end)

	def on_editable_toggled(self, widget):
		self.textview.set_editable(widget.get_active())


	def on_justify_toggled(self, widget, justification):
		self.textview.set_justification(justification)

	def on_search_clicked(self, widget):
		dialog = SearchDialog(self)
		response = dialog.run()
		if response == Gtk.ResponseType.OK:
			cursor_mark = self.textbuffer.get_insert()
			start = self.textbuffer.get_iter_at_mark(cursor_mark)
			if start.get_offset() == self.textbuffer.get_char_count():
				start = self.textbuffer.get_start_iter()

				self.search_and_mark(dialog.entry.get_text(), start)

		dialog.destroy()

	def search_and_mark(self, text, start):
		end = self.textbuffer.get_end_iter()
		match = start.forward_search(text, 0, end)

		if match != None:
			match_start, match_end = match
			self.textbuffer.apply_tag(self.tag_found, match_start, match_end)
			self.search_and_mark(text, match_end)

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()


