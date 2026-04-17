import ui, localeInfo, net, dbg
import player

class MemleketWindow(ui.ScriptWindow):
	MAX_ITEM_SIZE = 3

	def __init__(self):
		super(MemleketWindow, self).__init__()
		self.Initialize()
		self.LoadWindow()

	def __del__(self):
		super(MemleketWindow, self).__del__()

	def Destroy(self):
		self.ClearList()
		self.ClearDictionary()
		self.Initialize()

	def Initialize(self):
		self.selectedIdx = -1
		self.window_dict = {}

	def Open(self):
		net.SendChatPacket("/lo4d_m3ml3k3ts")
		self.EnableRefreshSymbol()
		self.SetTop()
		self.SetCenterPosition()
		self.Show()

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def EnableRefreshSymbol(self):
		self.window_dict['ref_symbol'].Show()

	def DisableRefreshSymbol(self):
		self.window_dict['ref_symbol'].Hide()

	def ClearList(self):
		listBox = self.window_dict.get('list_box')
		if listBox:
			listBox.RemoveAllItems()

	def LoadTitleList(self):
		if localeInfo.MEMLEKET_LIST:
			tempList = localeInfo.MEMLEKET_LIST
			for idx in range(1, len(tempList)):
				up = ui.RadioButton()
				up.SetUpVisual("new_title/button/xlarge1.png")
				up.SetOverVisual("new_title/button/xlarge2.png")
				up.SetDownVisual("new_title/button/xlarge3.png")
				up.SetPosition(5, 0)
				up.SetText(tempList[idx])
				up.SetEvent(ui.__mem_func__(self.UpdateInfos), idx - 1)
				up.Show()
				self.window_dict['list_box'].AppendItem(up)
		self.DisableRefreshSymbol()
		self.UpdateInfos(0)

	def LoadItemList(self, idx, vnum, count):
		import item
		item.SelectItem(int(vnum))
		itemName = item.GetItemName()
		itemStr = "{} x {}".format(itemName, count)
		crrKey = "item_info%d"%idx
		self.window_dict[crrKey].SetText(itemStr)

	def LoadAffList(self, idx, affType, affVal):
		crrKey = "aff_info%d"%idx
		import uitooltip
		affStr = uitooltip.GET_AFFECT_STRING(int(affType), int(affVal))
		self.window_dict[crrKey].SetText(affStr)

	def LoadWindow(self):
		try:
			ui.PythonScriptLoader().LoadScriptFile(self, "uiscript/memleket.py")
		except KeyError, msg:
			dbg.TraceError("NewTitlesWindow #1")

		try:
			self.__BindObjects()
		except KeyError, msg:
			dbg.TraceError("NewTitlesWindow #2 - %s" % str(msg))

		try:
			self.__BindEvents()
		except KeyError, msg:
			dbg.TraceError("NewTitlesWindow #3 - %s" % str(msg))

	def __BindObjects(self):
		child = self.GetChild
		self.window_dict = {
			'title_bar' : child("TitleBar"),
			'title_text' : child("title_text"),
			'ref_symbol' : child("RefreshSymbol"),
			'list_box' : child("ListBox"),
			'scroll_bar' : child("scroll_bar"),
			'send_button' : child("send_button"),
		}

		for i in range(self.MAX_ITEM_SIZE): # max item - aff size
			itemInfo = child("item_info%d"%(i))
			self.window_dict['item_info%d'%i] = itemInfo
			affInfo = child("aff_info%d"%(i))
			self.window_dict['aff_info%d'%i] = affInfo

	def __BindEvents(self):
		self.window_dict['title_bar'].SetCloseEvent(self.Close)

		self.window_dict['list_box'].SetItemStep(27)
		self.window_dict['list_box'].SetViewItemCount(7)
		self.window_dict['list_box'].SetItemSize(299,46)
		self.window_dict['list_box'].SetScrollBar(self.window_dict['scroll_bar'])

		self.window_dict['send_button'].SetEvent(ui.__mem_func__(self.UpdateTitle))

	def OnRunMouseWheel(self, a):
		if a > 0:
			self.window_dict["scroll_bar"].OnUp()
		else:
			self.window_dict["scroll_bar"].OnDown()

	def UpdateTitle(self):
		net.SendChatPacket("/ch4ng3_m3ml3k3t {}".format(self.selectedIdx))

	def UpdateInfos(self, selectedIdx):
		for obj in self.window_dict['list_box'].GetItems():
			obj.SetUp()

		realBtn = self.window_dict['list_box'].GetItemWithIndex(selectedIdx)
		if realBtn is not None:
			realBtn.Down()
		self.selectedIdx = selectedIdx + 1


	def OnRunMouseWheel(self, a):
		scroll = self.window_dict["scroll_bar"]
		if not scroll.IsShow():
			return False
		if not self.IsInPosition():
			return False
		if a > 0:
			scroll.OnUp()
		else:
			scroll.OnDown()
		return True
