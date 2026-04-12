import ui
import uiScriptLocale
import app
import net
import dbg
import snd
import player
import mouseModule
import wndMgr
import skill
import playerSettingModule
import quest
import localeInfo
import uiToolTip
import constInfo
import emotion
import chr
import guild
import uiUploadMark
import uiPickMoney
import uiCommon
import uiGuild
import guild

SHOW_ONLY_ACTIVE_SKILL = False
SHOW_LIMIT_SUPPORT_SKILL_LIST = []
HIDE_SUPPORT_SKILL_POINT = False

if (localeInfo.IsEUROPE()):
	HIDE_SUPPORT_SKILL_POINT = True	
	SHOW_LIMIT_SUPPORT_SKILL_LIST = [121, 122, 123, 124, 126, 127, 129, 128, 131, 137, 138, 139, 140]
else:
	HIDE_SUPPORT_SKILL_POINT = True

FACE_IMAGE_DICT = {
	playerSettingModule.RACE_WARRIOR_M	: "icon/face/warrior_m.tga",
	playerSettingModule.RACE_WARRIOR_W	: "icon/face/warrior_w.tga",
	playerSettingModule.RACE_ASSASSIN_M	: "icon/face/assassin_m.tga",
	playerSettingModule.RACE_ASSASSIN_W	: "icon/face/assassin_w.tga",
	playerSettingModule.RACE_SURA_M		: "icon/face/sura_m.tga",
	playerSettingModule.RACE_SURA_W		: "icon/face/sura_w.tga",
	playerSettingModule.RACE_SHAMAN_M	: "icon/face/shaman_m.tga",
	playerSettingModule.RACE_SHAMAN_W	: "icon/face/shaman_w.tga",
}
def unsigned32(n):
	return n & 0xFFFFFFFFL
	
class TitleListItem(ui.Window):
	def __init__(self, parentWnd, index, text):
		ui.Window.__init__(self)

		self.parentWnd = parentWnd
		self.index = index

		self.SetSize(130, 18)

		self.mark1 = ui.TextLine()
		self.mark1.SetParent(self)
		self.mark1.SetPosition(2, 1)
		self.mark1.SetText("[ ]")
		self.mark1.SetPackedFontColor(0xffffffff)
		self.mark1.Show()

		self.mark1Button = ui.Button()
		self.mark1Button.SetParent(self)
		self.mark1Button.SetPosition(2, 1)
		self.mark1Button.SetSize(20, 16)
		self.mark1Button.SetUpVisual("d:/ymir work/ui/blank.tga")
		self.mark1Button.SetOverVisual("d:/ymir work/ui/blank.tga")
		self.mark1Button.SetDownVisual("d:/ymir work/ui/blank.tga")
		self.mark1Button.SetEvent(lambda : self.parentWnd.ToggleVisibleTitle(self.index))
		self.mark1Button.Show()

		self.mark2 = ui.TextLine()
		self.mark2.SetParent(self)
		self.mark2.SetPosition(24, 1)
		self.mark2.SetText("[ ]")
		self.mark2.SetPackedFontColor(0xffffffff)
		self.mark2.Show()

		self.name = ui.TextLine()
		self.name.SetParent(self)
		self.name.SetPosition(48, 1)
		self.name.SetText(text)
		self.name.SetPackedFontColor(0xffffffff)
		self.name.Show()

		self.hitButton = ui.Button()
		self.hitButton.SetParent(self)
		self.hitButton.SetPosition(42, 0)
		self.hitButton.SetSize(88, 18)
		self.hitButton.SetUpVisual("d:/ymir work/ui/blank.tga")
		self.hitButton.SetOverVisual("d:/ymir work/ui/blank.tga")
		self.hitButton.SetDownVisual("d:/ymir work/ui/blank.tga")
		self.hitButton.SetEvent(lambda : self.parentWnd.SelectTitleFromList(self.index))
		self.hitButton.Show()

		self.Show()

	def SetSelected(self, isSelected):
		if isSelected:
			self.name.SetPackedFontColor(0xffffff00)
		else:
			self.name.SetPackedFontColor(0xffffffff)

	def SetMarks(self, leftChecked, rightChecked):
		if leftChecked:
			self.mark1.SetText("[X]")
		else:
			self.mark1.SetText("[ ]")

		if rightChecked:
			self.mark2.SetText("[X]")
		else:
			self.mark2.SetText("[ ]")    

class CharacterWindow(ui.ScriptWindow):

	ACTIVE_PAGE_SLOT_COUNT = 8
	SUPPORT_PAGE_SLOT_COUNT = 12

	PAGE_SLOT_COUNT = 12
	PAGE_HORSE = 2

	SKILL_GROUP_NAME_DICT = {
		playerSettingModule.JOB_WARRIOR	: { 1 : localeInfo.SKILL_GROUP_WARRIOR_1,	2 : localeInfo.SKILL_GROUP_WARRIOR_2, },
		playerSettingModule.JOB_ASSASSIN	: { 1 : localeInfo.SKILL_GROUP_ASSASSIN_1,	2 : localeInfo.SKILL_GROUP_ASSASSIN_2, },
		playerSettingModule.JOB_SURA		: { 1 : localeInfo.SKILL_GROUP_SURA_1,		2 : localeInfo.SKILL_GROUP_SURA_2, },
		playerSettingModule.JOB_SHAMAN		: { 1 : localeInfo.SKILL_GROUP_SHAMAN_1,	2 : localeInfo.SKILL_GROUP_SHAMAN_2, },
	}

	STAT_DESCRIPTION =	{
		"HTH" : localeInfo.STAT_TOOLTIP_CON,
		"INT" : localeInfo.STAT_TOOLTIP_INT,
		"STR" : localeInfo.STAT_TOOLTIP_STR,
		"DEX" : localeInfo.STAT_TOOLTIP_DEX,
	}


	STAT_MINUS_DESCRIPTION = localeInfo.STAT_MINUS_DESCRIPTION

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.state = "STATUS"
		self.isLoaded = 0

		self.toolTipSkill = 0
				
		self.__Initialize()
		self.__LoadWindow()

		self.statusPlusCommandDict={
			"HTH" : "/stat ht",
			"INT" : "/stat iq",
			"STR" : "/stat st",
			"DEX" : "/stat dx",
		}

		self.statusMinusCommandDict={
			"HTH-" : "/stat- ht",
			"INT-" : "/stat- iq",
			"STR-" : "/stat- st",
			"DEX-" : "/stat- dx",
		}

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __Initialize(self):
		self.refreshToolTip = 0
		self.curSelectedSkillGroup = 0
		self.canUseHorseSkill = -1

		self.toolTip = None
		self.toolTipJob = None
		self.toolTipAlignment = None
		self.toolTipSkill = None

		self.faceImage = None
		self.statusPlusLabel = None
		self.statusPlusValue = None
		self.activeSlot = None
		self.tabDict = None
		self.tabButtonDict = None
		self.pageDict = None
		self.titleBarDict = None
		self.statusPlusButtonDict = None
		self.statusMinusButtonDict = None

		self.skillPageDict = None
		self.questShowingStartIndex = 0
		self.questMainShowingStartIndex = 0
		self.questSubShowingStartIndex = 0
		self.questMainScrollBar = None
		self.questSubScrollBar = None
		self.questSlot = None
		self.questNameList = None
		self.questLastTimeList = []
		self.questLastCountList = []
		self.questRowButtonList = None
		self.selectedQuestGlobalIndex = -1
		self.questDetailTitle = None
		self.questDetailLineList = None
		self.skillGroupButton = ()

		self.activeSlot = None
		self.activeSkillPointValue = None
		self.supportSkillPointValue = None
		self.skillGroupButton1 = None
		self.skillGroupButton2 = None
		self.activeSkillGroupName = None

		self.guildNameSlot = None
		self.guildNameValue = None
		self.characterNameSlot = None
		self.characterNameValue = None

		self.emotionToolTip = None
		self.soloEmotionSlot = None
		self.dualEmotionSlot = None

		self.offerDialog = None
		self.popup = None
		self.markSelectDialog = None
		self.symbolSelectDialog = None
		self.inputDialog = None
		self.guildInfo = {}
		self.largeMarkBox = None
		self.enemyGuildNameList = []

		self.titleListBox = None
		self.titleScrollBar = None
		self.selectedTitleIndex = -1
		self.titleItemList = []
		self.visibleTitleIndex = -1

		self.selectedTitleName = None
		self.selectedTitleDescList = []
		self.selectedTitleBonusList = []

	def Show(self):
		self.__LoadWindow()

		ui.ScriptWindow.Show(self)

	def __LoadScript(self, fileName):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, fileName)	
		
	def __BindObject(self):
		self.toolTip = uiToolTip.ToolTip()
		self.toolTipJob = uiToolTip.ToolTip()
		self.toolTipAlignment = uiToolTip.ToolTip(130)		

		self.faceImage = self.GetChild("Face_Image")

		faceSlot=self.GetChild("Face_Slot")
		if 949 == app.GetDefaultCodePage():
			faceSlot.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowJobToolTip)
			faceSlot.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideJobToolTip)

		self.statusPlusLabel = self.GetChild("Status_Plus_Label")
		self.statusPlusValue = self.GetChild("Status_Plus_Value")		

		self.characterNameSlot = self.GetChild("Character_Name_Slot")			
		self.characterNameValue = self.GetChild("Character_Name")
		self.guildNameSlot = self.GetChild("Guild_Name_Slot")
		self.guildNameValue = self.GetChild("Guild_Name")
		self.characterNameSlot.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowAlignmentToolTip)
		self.characterNameSlot.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideAlignmentToolTip)

		self.activeSlot = self.GetChild("Skill_Active_Slot")
		self.activeSkillPointValue = self.GetChild("Active_Skill_Point_Value")
		self.supportSkillPointValue = self.GetChild("Support_Skill_Point_Value")
		self.skillGroupButton1 = self.GetChild("Skill_Group_Button_1")
		self.skillGroupButton2 = self.GetChild("Skill_Group_Button_2")
		self.activeSkillGroupName = self.GetChild("Active_Skill_Group_Name")

		self.tabDict = {
			"STATUS"	: self.GetChild("Tab_01"),
			"SKILL"		: self.GetChild("Tab_02"),
			"EMOTICON"	: self.GetChild("Tab_03"),
			"QUEST"		: self.GetChild("Tab_04"),
            "GUILD"		: self.GetChild("Tab_05"),
            "TITLES"	: self.GetChild("Tab_06"),
		}

		self.tabButtonDict = {
			"STATUS"	: self.GetChild("Tab_Button_01"),
			"SKILL"		: self.GetChild("Tab_Button_02"),
			"EMOTICON"	: self.GetChild("Tab_Button_03"),
			"QUEST"		: self.GetChild("Tab_Button_04"),
            "GUILD"		: self.GetChild("Tab_Button_05"),
            "TITLES"	: self.GetChild("Tab_Button_06"),
		}

		self.pageDict = {
			"STATUS"	: self.GetChild("Character_Page"),
			"SKILL"		: self.GetChild("Skill_Page"),
			"EMOTICON"	: self.GetChild("Emoticon_Page"),
			"QUEST"		: self.GetChild("Quest_Page"),
            "GUILD"		: self.GetChild("Guild_Page"),
            "TITLES"	: self.GetChild("Titles_Page"),
		}

		self.titleBarDict = {
			"STATUS"	: self.GetChild("Character_TitleBar"),
			"SKILL"		: self.GetChild("Skill_TitleBar"),
			"EMOTICON"	: self.GetChild("Emoticon_TitleBar"),
			"QUEST"		: self.GetChild("Quest_TitleBar"),
            "GUILD"		: self.GetChild("Guild_TitleBar"),
            "TITLES"	: self.GetChild("Titles_TitleBar"),
		}

		self.statusPlusButtonDict = {
			"HTH"		: self.GetChild("HTH_Plus"),
			"INT"		: self.GetChild("INT_Plus"),
			"STR"		: self.GetChild("STR_Plus"),
			"DEX"		: self.GetChild("DEX_Plus"),
		}

		self.statusMinusButtonDict = {
			"HTH-"		: self.GetChild("HTH_Minus"),
			"INT-"		: self.GetChild("INT_Minus"),
			"STR-"		: self.GetChild("STR_Minus"),
			"DEX-"		: self.GetChild("DEX_Minus"),
		}

		self.skillPageDict = {
			"ACTIVE" : self.GetChild("Skill_Active_Slot"),
			"SUPPORT" : self.GetChild("Skill_ETC_Slot"),
			"HORSE" : self.GetChild("Skill_Active_Slot"),
		}

		self.skillPageStatDict = {
			"SUPPORT"	: player.SKILL_SUPPORT,
			"ACTIVE"	: player.SKILL_ACTIVE,
			"HORSE"		: player.SKILL_HORSE,
		}

		self.skillGroupButton = (
			self.GetChild("Skill_Group_Button_1"),
			self.GetChild("Skill_Group_Button_2"),
		)

		
		global SHOW_ONLY_ACTIVE_SKILL
		global HIDE_SUPPORT_SKILL_POINT
		if SHOW_ONLY_ACTIVE_SKILL or HIDE_SUPPORT_SKILL_POINT:	
			self.GetChild("Support_Skill_Point_Label").Hide()

		self.soloEmotionSlot = self.GetChild("SoloEmotionSlot")
		self.dualEmotionSlot = self.GetChild("DualEmotionSlot")
		self.__SetEmotionSlot()

		self.questShowingStartIndex = 0
		self.questMainShowingStartIndex = 0
		self.questSubShowingStartIndex = 0

		try:
			self.questMainScrollBar = self.GetChild("Quest_ScrollBar_Title_Main")
		except:
			self.questMainScrollBar = None

		try:
			self.questSubScrollBar = self.GetChild("Quest_ScrollBar_Title_Sub")
		except:
			self.questSubScrollBar = None

		if self.questMainScrollBar:
			self.questMainScrollBar.SetScrollEvent(ui.__mem_func__(self.OnQuestMainScroll))

		if self.questSubScrollBar:
			self.questSubScrollBar.SetScrollEvent(ui.__mem_func__(self.OnQuestSubScroll))

		self.questNameList = []
		self.questLastTimeList = []
		self.questLastCountList = []

		for i in xrange(quest.QUEST_MAX_NUM):
			self.questNameList.append(self.GetChild("Quest_Name_0" + str(i)))

		self.questRowButtonList = []
		for i in xrange(quest.QUEST_MAX_NUM):
			self.questRowButtonList.append(self.GetChild("Quest_Row_0" + str(i)))

		self.questDetailTitle = self.GetChild("Quest_Detail_Title")
		self.questDetailTitle.SetFontName("Tahoma:16")

		self.questDetailLineList = []
		self.questDetailLineList.append(self.GetChild("Quest_Detail_Line_01"))
		self.questDetailLineList.append(self.GetChild("Quest_Detail_Line_02"))
		self.questDetailLineList.append(self.GetChild("Quest_Detail_Line_03"))
		self.questDetailLineList.append(self.GetChild("Quest_Detail_Line_04"))
		self.questDetailLineList.append(self.GetChild("Quest_Detail_Line_05"))

		self.guildInfo = {
			"nameSlot" : self.GetChild("GuildNameValue"),
			"masterNameSlot" : self.GetChild("GuildMasterNameValue"),
			"guildLevelSlot" : self.GetChild("GuildLevelValue"),
			"curExpSlot" : self.GetChild("CurrentExperienceValue"),
			"lastExpSlot" : self.GetChild("LastExperienceValue"),
			"memberCountSlot" : self.GetChild("GuildMemberCountValue"),
			"levelAverageSlot" : self.GetChild("GuildMemberLevelAverageValue"),
			"uploadMarkButton" : self.GetChild("UploadGuildMarkButton"),
			"uploadSymbolButton" : self.GetChild("UploadGuildSymbolButton"),
			"declareWarButton" : self.GetChild("DeclareWarButton"),
			"offerButton" : self.GetChild("OfferButton"),
		}

		self.largeMarkBox = self.GetChild("LargeGuildMark")
		self.largeMarkBox.AddFlag("not_pick")

		self.enemyGuildNameList = []
		self.enemyGuildNameList.append(self.GetChild("EnemyGuildName1"))
		self.enemyGuildNameList.append(self.GetChild("EnemyGuildName2"))
		self.enemyGuildNameList.append(self.GetChild("EnemyGuildName3"))
		self.enemyGuildNameList.append(self.GetChild("EnemyGuildName4"))
		self.enemyGuildNameList.append(self.GetChild("EnemyGuildName5"))
		self.enemyGuildNameList.append(self.GetChild("EnemyGuildName6"))

		for i in xrange(1, 7):
			try:
				self.GetChild("EnemyGuildCancel%d" % i).Hide()
			except:
				pass

		self.markSelectDialog = uiUploadMark.MarkSelectDialog()
		self.markSelectDialog.SAFE_SetSelectEvent(self.__OnSelectMark)

		self.symbolSelectDialog = uiUploadMark.SymbolSelectDialog()
		self.symbolSelectDialog.SAFE_SetSelectEvent(self.__OnSelectSymbol)

		self.offerDialog = uiPickMoney.PickMoneyDialog()
		self.offerDialog.LoadDialog()
		self.offerDialog.SetMax(9)
		self.offerDialog.SetTitleName(localeInfo.GUILD_OFFER_EXP)
		self.offerDialog.SetAcceptEvent(ui.__mem_func__(self.OnOffer))

		try:
			self.titleListBox = self.GetChild("TitleList")
		except:
			self.titleListBox = None

		try:
			self.titleScrollBar = self.GetChild("TitleScrollBar")
		except:
			self.titleScrollBar = None

		try:
			self.selectedTitleName = self.GetChild("SelectedTitleName")
		except:
			self.selectedTitleName = None

		self.selectedTitleDescList = []
		for i in xrange(1, 4):
			try:
				self.selectedTitleDescList.append(self.GetChild("SelectedTitleDesc%d" % i))
			except:
				self.selectedTitleDescList.append(None)

		self.selectedTitleBonusList = []
		for i in xrange(1, 4):
			try:
				self.selectedTitleBonusList.append(self.GetChild("SelectedTitleBonus%d" % i))
			except:
				self.selectedTitleBonusList.append(None)

	def __SetSkillSlotEvent(self):
		for skillPageValue in self.skillPageDict.itervalues():
			skillPageValue.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
			skillPageValue.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectSkill))
			skillPageValue.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
			skillPageValue.SetUnselectItemSlotEvent(ui.__mem_func__(self.ClickSkillSlot))
			skillPageValue.SetUseSlotEvent(ui.__mem_func__(self.ClickSkillSlot))
			skillPageValue.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
			skillPageValue.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
			skillPageValue.SetPressedSlotButtonEvent(ui.__mem_func__(self.OnPressedSlotButton))
			skillPageValue.AppendSlotButton("d:/ymir work/ui/game/windows/btn_plus_up.sub",\
											"d:/ymir work/ui/game/windows/btn_plus_over.sub",\
											"d:/ymir work/ui/game/windows/btn_plus_down.sub")

	def __SetEmotionSlot(self):

		self.emotionToolTip = uiToolTip.ToolTip()

		for slot in (self.soloEmotionSlot, self.dualEmotionSlot):
			slot.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
			slot.SetSelectItemSlotEvent(ui.__mem_func__(self.__SelectEmotion))
			slot.SetUnselectItemSlotEvent(ui.__mem_func__(self.__ClickEmotionSlot))
			slot.SetUseSlotEvent(ui.__mem_func__(self.__ClickEmotionSlot))
			slot.SetOverInItemEvent(ui.__mem_func__(self.__OverInEmotion))
			slot.SetOverOutItemEvent(ui.__mem_func__(self.__OverOutEmotion))
			slot.AppendSlotButton("d:/ymir work/ui/game/windows/btn_plus_up.sub",\
											"d:/ymir work/ui/game/windows/btn_plus_over.sub",\
											"d:/ymir work/ui/game/windows/btn_plus_down.sub")

		for slotIdx, datadict in emotion.EMOTION_DICT.items():
			emotionIdx = slotIdx

			slot = self.soloEmotionSlot
			if slotIdx > 50:
				slot = self.dualEmotionSlot

			slot.SetEmotionSlot(slotIdx, emotionIdx)
			slot.SetCoverButton(slotIdx)

	def __SelectEmotion(self, slotIndex):
		if not slotIndex in emotion.EMOTION_DICT:
			return

		if app.IsPressed(app.DIK_LCONTROL):
			player.RequestAddToEmptyLocalQuickSlot(player.SLOT_TYPE_EMOTION, slotIndex)
			return

		mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_EMOTION, slotIndex, slotIndex)

	def __ClickEmotionSlot(self, slotIndex):
		print "click emotion"
		if not slotIndex in emotion.EMOTION_DICT:
			return

		print "check acting"
		if player.IsActingEmotion():
			return

		command = emotion.EMOTION_DICT[slotIndex]["command"]
		print "command", command

		if slotIndex > 50:
			vid = player.GetTargetVID()

			if 0 == vid or vid == player.GetMainCharacterIndex() or chr.IsNPC(vid) or chr.IsEnemy(vid):
				import chat
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EMOTION_CHOOSE_ONE)
				return

			command += " " + chr.GetNameByVID(vid)

		print "send_command", command
		net.SendChatPacket(command)

	def ActEmotion(self, emotionIndex):
		self.__ClickEmotionSlot(emotionIndex)

	def __OverInEmotion(self, slotIndex):
		if self.emotionToolTip:

			if not slotIndex in emotion.EMOTION_DICT:
				return

			self.emotionToolTip.ClearToolTip()
			self.emotionToolTip.SetTitle(emotion.EMOTION_DICT[slotIndex]["name"])
			self.emotionToolTip.AlignHorizonalCenter()
			self.emotionToolTip.ShowToolTip()

	def __OverOutEmotion(self):
		if self.emotionToolTip:
			self.emotionToolTip.HideToolTip()

	def __BindEvent(self):
		for i in xrange(len(self.skillGroupButton)):
			self.skillGroupButton[i].SetEvent(lambda arg=i: self.__SelectSkillGroup(arg))

		self.RefreshQuest()
		self.__HideJobToolTip()

		for (tabKey, tabButton) in self.tabButtonDict.items():
			tabButton.SetEvent(ui.__mem_func__(self.__OnClickTabButton), tabKey)

		for (statusPlusKey, statusPlusButton) in self.statusPlusButtonDict.items():
			statusPlusButton.SAFE_SetEvent(self.__OnClickStatusPlusButton, statusPlusKey)
			statusPlusButton.ShowToolTip = lambda arg=statusPlusKey: self.__OverInStatButton(arg)
			statusPlusButton.HideToolTip = lambda arg=statusPlusKey: self.__OverOutStatButton()

		for (statusMinusKey, statusMinusButton) in self.statusMinusButtonDict.items():
			statusMinusButton.SAFE_SetEvent(self.__OnClickStatusMinusButton, statusMinusKey)
			statusMinusButton.ShowToolTip = lambda arg=statusMinusKey: self.__OverInStatMinusButton(arg)
			statusMinusButton.HideToolTip = lambda arg=statusMinusKey: self.__OverOutStatMinusButton()

		for titleBarValue in self.titleBarDict.itervalues():
			titleBarValue.SetCloseEvent(ui.__mem_func__(self.Hide))

		for i in xrange(len(self.questRowButtonList)):
			self.questRowButtonList[i].SetEvent(lambda arg=i: self.__SelectQuestRow(arg))

		self.guildInfo["uploadMarkButton"].SetEvent(ui.__mem_func__(self.__OnClickSelectGuildMarkButton))
		self.guildInfo["uploadSymbolButton"].SetEvent(ui.__mem_func__(self.__OnClickSelectGuildSymbolButton))
		self.guildInfo["declareWarButton"].SetEvent(ui.__mem_func__(self.__OnClickDeclareWarButton))
		self.guildInfo["offerButton"].SetEvent(ui.__mem_func__(self.__OnClickOfferButton))

		if self.titleListBox and self.titleScrollBar:
			self.titleListBox.SetItemStep(18)
			self.titleListBox.SetViewItemCount(12)
			self.titleListBox.SetItemSize(130, 18)
			self.titleListBox.SetScrollBar(self.titleScrollBar)
			self.titleScrollBar.Show()

	def __LoadWindow(self):
		if self.isLoaded == 1:
			return
		self.isLoaded = 1

		try:
			if localeInfo.IsARABIC():
				self.__LoadScript(uiScriptLocale.LOCALE_UISCRIPT_PATH + "CharacterWindow.py")
			else:
				self.__LoadScript("UIScript/CharacterWindow.py")

			print(">>> CharacterWindow.py załadowany pomyślnie")

			self.__BindObject()
			print(">>> __BindObject() OK")

			self.__BindEvent()
			print(">>> __BindEvent() OK")

		except Exception as e:
			import traceback, exception
			traceback.print_exc()
			exception.Abort("CharacterWindow ERROR: " + str(e))

	def Destroy(self):
		self.ClearDictionary()

		self.__Initialize()

	def Close(self):
		if 0 != self.toolTipSkill:
			self.toolTipSkill.Hide()

		self.Hide()

	def SetSkillToolTip(self, toolTipSkill):
		self.toolTipSkill = toolTipSkill

	def __OnClickStatusPlusButton(self, statusKey):
		try:
			statusPlusCommand=self.statusPlusCommandDict[statusKey]
			net.SendChatPacket(statusPlusCommand)
		except KeyError, msg:
			dbg.TraceError("CharacterWindow.__OnClickStatusPlusButton KeyError: %s", msg)

	def __OnClickStatusMinusButton(self, statusKey):
		try:
			statusMinusCommand=self.statusMinusCommandDict[statusKey]
			net.SendChatPacket(statusMinusCommand)
		except KeyError, msg:
			dbg.TraceError("CharacterWindow.__OnClickStatusMinusButton KeyError: %s", msg)


	def __OnClickTabButton(self, stateKey):
		self.SetState(stateKey)

	def SetState(self, stateKey):
		
		self.state = stateKey

		for (tabKey, tabButton) in self.tabButtonDict.items():
			if stateKey!=tabKey:
				tabButton.SetUp()

		for tabValue in self.tabDict.itervalues():
			tabValue.Hide()

		for pageValue in self.pageDict.itervalues():
			pageValue.Hide()

		for titleBarValue in self.titleBarDict.itervalues():
			titleBarValue.Hide()

		self.titleBarDict[stateKey].Show()
		self.tabDict[stateKey].Show()
		self.pageDict[stateKey].Show()

		if "GUILD" == stateKey:
			self.RefreshGuildInfo()

		if "TITLES" == stateKey:
			self.LoadTitlePageList()

	def RefreshTitleMarks(self):
		for i in xrange(len(self.titleItemList)):
			leftChecked = (i == self.visibleTitleIndex)
			rightChecked = False
			self.titleItemList[i].SetMarks(leftChecked, rightChecked)

	def ToggleVisibleTitle(self, titleIdx):
		if self.visibleTitleIndex == titleIdx:
			self.visibleTitleIndex = -1
		else:
			self.visibleTitleIndex = titleIdx

		self.RefreshTitleMarks()

		if self.visibleTitleIndex == -1:
			net.SendChatPacket("/change_memleket -1")
		else:
			net.SendChatPacket("/change_memleket %d" % (self.visibleTitleIndex + 1))

	def SetTitleInfo(self, selectedIdx):
		self.ClearTitleInfo()

		if not self.selectedTitleName:
			return

		titleName = localeInfo.MEMLEKET_LIST[selectedIdx + 1]
		self.selectedTitleName.SetText(titleName)

		descList = [
			"To jest przykładowy opis.",
			"Tu później podepniesz dane z serwera.",
		]

		bonusList = [
			"+1000 HP",
			"+10 Siły",
			"+5% na potwory",
		]

		for i in xrange(len(self.selectedTitleDescList)):
			if self.selectedTitleDescList[i]:
				if i < len(descList):
					self.selectedTitleDescList[i].SetText(descList[i])
				else:
					self.selectedTitleDescList[i].SetText("")

		for i in xrange(len(self.selectedTitleBonusList)):
			if self.selectedTitleBonusList[i]:
				if i < len(bonusList):
					self.selectedTitleBonusList[i].SetText(bonusList[i])
				else:
					self.selectedTitleBonusList[i].SetText("")

	def ClearTitleList(self):
		if self.titleListBox:
			self.titleListBox.RemoveAllItems()
		self.titleItemList = []

	def LoadTitlePageList(self):
		self.ClearTitleList()

		if not self.titleListBox:
			return

		if not localeInfo.MEMLEKET_LIST:
			return

		for idx in xrange(1, len(localeInfo.MEMLEKET_LIST)):
			item = TitleListItem(self, idx - 1, localeInfo.MEMLEKET_LIST[idx])
			item.SetMarks(False, False)
			self.titleListBox.AppendItem(item)
			self.titleItemList.append(item)

		if self.titleScrollBar:
			self.titleScrollBar.SetPos(0.0)

		if len(self.titleItemList) > 0:
			self.SelectTitleFromList(0)

		self.RefreshTitleMarks()

	def SelectTitleFromList(self, selectedIdx):
		self.selectedTitleIndex = selectedIdx

		for i in xrange(len(self.titleItemList)):
			self.titleItemList[i].SetSelected(i == selectedIdx)

		self.SetTitleInfo(selectedIdx)

	def ClearTitleInfo(self):
		if self.selectedTitleName:
			self.selectedTitleName.SetText("")

		for line in self.selectedTitleDescList:
			if line:
				line.SetText("")

		for line in self.selectedTitleBonusList:
			if line:
				line.SetText("")

	def GetState(self):
		return self.state

	def __GetTotalAtkText(self):
		minAtk=player.GetStatus(player.ATT_MIN)
		maxAtk=player.GetStatus(player.ATT_MAX)
		atkBonus=player.GetStatus(player.ATT_BONUS)
		attackerBonus=player.GetStatus(player.ATTACKER_BONUS)

		if minAtk==maxAtk:
			return "%d" % (minAtk+atkBonus+attackerBonus)
		else:
			return "%d-%d" % (minAtk+atkBonus+attackerBonus, maxAtk+atkBonus+attackerBonus)

	def __GetTotalMagAtkText(self):
		minMagAtk=player.GetStatus(player.MAG_ATT)+player.GetStatus(player.MIN_MAGIC_WEP)
		maxMagAtk=player.GetStatus(player.MAG_ATT)+player.GetStatus(player.MAX_MAGIC_WEP)

		if minMagAtk==maxMagAtk:
			return "%d" % (minMagAtk)
		else:
			return "%d-%d" % (minMagAtk, maxMagAtk)

	def __GetTotalDefText(self):
		defValue=player.GetStatus(player.DEF_GRADE)
		if constInfo.ADD_DEF_BONUS_ENABLE:
			defValue+=player.GetStatus(player.DEF_BONUS)
		return "%d" % (defValue)
	
	def RefreshStatus(self):
		if self.isLoaded==0:
			return

		try:
			self.GetChild("Level_Value").SetText(str(player.GetStatus(player.LEVEL)))
			self.GetChild("Exp_Value").SetText(str(unsigned32(player.GetEXP())))
			self.GetChild("RestExp_Value").SetText(str(unsigned32(player.GetStatus(player.NEXT_EXP)) - unsigned32(player.GetStatus(player.EXP))))
			self.GetChild("HP_Value").SetText(str(player.GetStatus(player.HP)) + '/' + str(player.GetStatus(player.MAX_HP)))
			self.GetChild("SP_Value").SetText(str(player.GetStatus(player.SP)) + '/' + str(player.GetStatus(player.MAX_SP)))

			self.GetChild("STR_Value").SetText(str(player.GetStatus(player.ST)))
			self.GetChild("DEX_Value").SetText(str(player.GetStatus(player.DX)))
			self.GetChild("HTH_Value").SetText(str(player.GetStatus(player.HT)))
			self.GetChild("INT_Value").SetText(str(player.GetStatus(player.IQ)))

			self.GetChild("ATT_Value").SetText(self.__GetTotalAtkText())
			self.GetChild("DEF_Value").SetText(self.__GetTotalDefText())

			self.GetChild("MATT_Value").SetText(self.__GetTotalMagAtkText())
			#self.GetChild("MATT_Value").SetText(str(player.GetStatus(player.MAG_ATT)))

			self.GetChild("MDEF_Value").SetText(str(player.GetStatus(player.MAG_DEF)))
			self.GetChild("ASPD_Value").SetText(str(player.GetStatus(player.ATT_SPEED)))
			self.GetChild("MSPD_Value").SetText(str(player.GetStatus(player.MOVING_SPEED)))
			self.GetChild("CSPD_Value").SetText(str(player.GetStatus(player.CASTING_SPEED)))
			self.GetChild("ER_Value").SetText(str(player.GetStatus(player.EVADE_RATE)))

		except:
			#import exception
			#exception.Abort("CharacterWindow.RefreshStatus.BindObject")
			##  ƨ 
			pass

		self.__RefreshStatusPlusButtonList()
		self.__RefreshStatusMinusButtonList()
		self.RefreshAlignment()

		if self.refreshToolTip:
			self.refreshToolTip()

	def __RefreshStatusPlusButtonList(self):
		if self.isLoaded==0:
			return

		statusPlusPoint=player.GetStatus(player.STAT)

		if statusPlusPoint>0:
			self.statusPlusValue.SetText(str(statusPlusPoint))
			self.statusPlusLabel.Show()
			self.ShowStatusPlusButtonList()
		else:
			self.statusPlusValue.SetText(str(0))
			self.statusPlusLabel.Hide()
			self.HideStatusPlusButtonList()

	def __RefreshStatusMinusButtonList(self):
		if self.isLoaded==0:
			return

		statusMinusPoint=self.__GetStatMinusPoint()

		if statusMinusPoint>0:
			self.__ShowStatusMinusButtonList()
		else:
			self.__HideStatusMinusButtonList()

	def RefreshAlignment(self):
		point, grade = player.GetAlignmentData()

		import colorInfo
		COLOR_DICT = {	0 : colorInfo.TITLE_RGB_GOOD_4,
						1 : colorInfo.TITLE_RGB_GOOD_3,
						2 : colorInfo.TITLE_RGB_GOOD_2,
						3 : colorInfo.TITLE_RGB_GOOD_1,
						4 : colorInfo.TITLE_RGB_NORMAL,
						5 : colorInfo.TITLE_RGB_EVIL_1,
						6 : colorInfo.TITLE_RGB_EVIL_2,
						7 : colorInfo.TITLE_RGB_EVIL_3,
						8 : colorInfo.TITLE_RGB_EVIL_4, }
		colorList = COLOR_DICT.get(grade, colorInfo.TITLE_RGB_NORMAL)
		gradeColor = ui.GenerateColor(colorList[0], colorList[1], colorList[2])

		self.toolTipAlignment.ClearToolTip()
		self.toolTipAlignment.AutoAppendTextLine(localeInfo.TITLE_NAME_LIST[grade], gradeColor)
		self.toolTipAlignment.AutoAppendTextLine(localeInfo.ALIGNMENT_NAME + str(point))
		self.toolTipAlignment.AlignHorizonalCenter()

	def __ShowStatusMinusButtonList(self):
		for (stateMinusKey, statusMinusButton) in self.statusMinusButtonDict.items():
			statusMinusButton.Show()

	def __HideStatusMinusButtonList(self):
		for (stateMinusKey, statusMinusButton) in self.statusMinusButtonDict.items():
			statusMinusButton.Hide()

	def ShowStatusPlusButtonList(self):
		for (statePlusKey, statusPlusButton) in self.statusPlusButtonDict.items():
			statusPlusButton.Show()

	def HideStatusPlusButtonList(self):
		for (statePlusKey, statusPlusButton) in self.statusPlusButtonDict.items():
			statusPlusButton.Hide()

	def SelectSkill(self, skillSlotIndex):

		mouseController = mouseModule.mouseController

		if False == mouseController.isAttached():

			srcSlotIndex = self.__RealSkillSlotToSourceSlot(skillSlotIndex)
			selectedSkillIndex = player.GetSkillIndex(srcSlotIndex)

			if skill.CanUseSkill(selectedSkillIndex):

				if app.IsPressed(app.DIK_LCONTROL):

					player.RequestAddToEmptyLocalQuickSlot(player.SLOT_TYPE_SKILL, srcSlotIndex)
					return

				mouseController.AttachObject(self, player.SLOT_TYPE_SKILL, srcSlotIndex, selectedSkillIndex)

		else:

			mouseController.DeattachObject()

	def SelectEmptySlot(self, SlotIndex):
		mouseModule.mouseController.DeattachObject()

	## ToolTip
	def OverInItem(self, slotNumber):

		if mouseModule.mouseController.isAttached():
			return

		if 0 == self.toolTipSkill:
			return

		srcSlotIndex = self.__RealSkillSlotToSourceSlot(slotNumber)
		skillIndex = player.GetSkillIndex(srcSlotIndex)
		skillLevel = player.GetSkillLevel(srcSlotIndex)
		skillGrade = player.GetSkillGrade(srcSlotIndex)
		skillType = skill.GetSkillType(skillIndex)

		## ACTIVE
		if skill.SKILL_TYPE_ACTIVE == skillType:
			overInSkillGrade = self.__GetSkillGradeFromSlot(slotNumber)

			if overInSkillGrade == skill.SKILL_GRADE_COUNT-1 and skillGrade == skill.SKILL_GRADE_COUNT:
				self.toolTipSkill.SetSkillNew(srcSlotIndex, skillIndex, skillGrade, skillLevel)
			elif overInSkillGrade == skillGrade:
				self.toolTipSkill.SetSkillNew(srcSlotIndex, skillIndex, overInSkillGrade, skillLevel)
			else:
				self.toolTipSkill.SetSkillOnlyName(srcSlotIndex, skillIndex, overInSkillGrade)

		else:
			self.toolTipSkill.SetSkillNew(srcSlotIndex, skillIndex, skillGrade, skillLevel)

	def OverOutItem(self):
		if 0 != self.toolTipSkill:
			self.toolTipSkill.HideToolTip()

	## Quest
	def __SelectQuest(self, slotIndex):
		self.__SelectQuestRow(slotIndex)

	def __SelectQuestRow(self, localIndex):
		questIndex = self.questShowingStartIndex + localIndex

		if questIndex >= quest.GetQuestCount():
			return

		self.selectedQuestGlobalIndex = questIndex
		self.__RefreshQuestDetail()

	def __RefreshQuestDetail(self):
		if self.selectedQuestGlobalIndex < 0 or self.selectedQuestGlobalIndex >= quest.GetQuestCount():
			self.questDetailTitle.SetText("Wybierz misje")
			for line in self.questDetailLineList:
				line.SetText("")
			return

		try:
			data = quest.GetQuestData(self.selectedQuestGlobalIndex)
			print "QUEST DATA =", data
			print "QUEST DATA LEN =", len(data)

			self.questDetailTitle.SetText("")
			for i in xrange(5):
				if i < len(data):
					self.questDetailLineList[i].SetText("data[%d] = %s" % (i, str(data[i])))
				else:
					self.questDetailLineList[i].SetText("")

		except:
			self.questDetailTitle.SetText("Wybierz misje")
			for line in self.questDetailLineList:
				line.SetText("")

	def RefreshQuest(self):
		if self.isLoaded == 0:
			return

		questCount = quest.GetQuestCount()

		if self.questMainScrollBar:
			self.questMainScrollBar.Show()                    
			if questCount <= quest.QUEST_MAX_NUM:                         
				self.questShowingStartIndex = 0
			else:            
				scrollLineCount = max(0, questCount - quest.QUEST_MAX_NUM)
				pos = self.questMainScrollBar.GetPos()
				self.questShowingStartIndex = int(scrollLineCount * pos)

		if self.questSubScrollBar:
			self.questSubScrollBar.Show()                     
			if questCount <= 5:      
				self.questSubShowingStartIndex = 0
			else:            
				scrollLineCount = max(0, questCount - 5)
				pos = self.questSubScrollBar.GetPos()
				self.questSubShowingStartIndex = int(scrollLineCount * pos)

		questRange = range(quest.QUEST_MAX_NUM)
		for i in questRange:
			if i < questCount:
				try:
					data = quest.GetQuestData(self.questShowingStartIndex + i)
					if data and len(data) > 0 and data[0] is not None:
						self.questNameList[i].SetText(str(data[0]))
						self.questNameList[i].Show()
						self.questRowButtonList[i].Show()
					else:
						self.questNameList[i].SetText("")
						self.questNameList[i].Hide()
						self.questRowButtonList[i].Hide()
				except:
					self.questNameList[i].SetText("")
					self.questNameList[i].Hide()
					self.questRowButtonList[i].Hide()
			else:
				self.questNameList[i].Hide()
				self.questRowButtonList[i].Hide()

		self.__UpdateQuestClock()
		self.__RefreshQuestDetail()

	def __UpdateQuestClock(self):
		return

	def RefreshGuildInfo(self):
		if self.isLoaded == 0:
			return

		if not self.guildInfo:
			return

		if not guild.IsGuildEnable():
			self.guildInfo["nameSlot"].SetText("-")
			self.guildInfo["masterNameSlot"].SetText("-")
			self.guildInfo["guildLevelSlot"].SetText("0")
			self.guildInfo["curExpSlot"].SetText("0")
			self.guildInfo["lastExpSlot"].SetText("0")
			self.guildInfo["memberCountSlot"].SetText("0 / 0")
			self.guildInfo["levelAverageSlot"].SetText("0")
			for nameTextLine in self.enemyGuildNameList:
				nameTextLine.SetText(localeInfo.GUILD_INFO_ENEMY_GUILD_EMPTY)
			self.guildInfo["uploadMarkButton"].Hide()
			self.guildInfo["uploadSymbolButton"].Hide()
			self.guildInfo["declareWarButton"].Hide()
			self.guildInfo["offerButton"].Hide()
			return

		self.guildInfo["nameSlot"].SetText(guild.GetGuildName())
		self.guildInfo["masterNameSlot"].SetText(guild.GetGuildMasterName())
		self.guildInfo["guildLevelSlot"].SetText(str(guild.GetGuildLevel()))

		curExp, lastExp = guild.GetGuildExperience()
		curExp *= 100
		lastExp *= 100
		self.guildInfo["curExpSlot"].SetText(str(curExp))
		self.guildInfo["lastExpSlot"].SetText(str(lastExp))

		curMemberCount, maxMemberCount = guild.GetGuildMemberCount()
		if maxMemberCount == 0xffff:
			self.guildInfo["memberCountSlot"].SetText("%d / %s" % (curMemberCount, localeInfo.GUILD_MEMBER_COUNT_INFINITY))
		else:
			self.guildInfo["memberCountSlot"].SetText("%d / %d" % (curMemberCount, maxMemberCount))

		self.guildInfo["levelAverageSlot"].SetText(str(guild.GetGuildMemberLevelAverage()))

		guildID = net.GetGuildID()
		if self.largeMarkBox:
			self.largeMarkBox.SetIndex(guildID)
			self.largeMarkBox.SetScale(3)

		for i in xrange(min(guild.ENEMY_GUILD_SLOT_MAX_COUNT, len(self.enemyGuildNameList))):
			name = guild.GetEnemyGuildName(i)
			nameTextLine = self.enemyGuildNameList[i]
			if name:
				nameTextLine.SetText(name)
			else:
				nameTextLine.SetText(localeInfo.GUILD_INFO_ENEMY_GUILD_EMPTY)

		self.guildInfo["offerButton"].Show()
		mainCharacterName = player.GetMainCharacterName()
		masterName = guild.GetGuildMasterName()
		if mainCharacterName == masterName:
			self.guildInfo["uploadMarkButton"].Show()
			self.guildInfo["declareWarButton"].Show()
			if guild.HasGuildLand():
				self.guildInfo["uploadSymbolButton"].Show()
			else:
				self.guildInfo["uploadSymbolButton"].Hide()
		else:
			self.guildInfo["uploadMarkButton"].Hide()
			self.guildInfo["uploadSymbolButton"].Hide()
			self.guildInfo["declareWarButton"].Hide()

	def __PopupMessage(self, msg):
		popup = uiCommon.PopupDialog()
		popup.SetText(msg)
		popup.SetAcceptEvent(lambda arg=True, popup=popup: popup.Close())
		popup.Open()
		self.popup = popup

	def __OnClickSelectGuildMarkButton(self):
		if guild.GetGuildLevel() < int(localeInfo.GUILD_MARK_MIN_LEVEL):
			self.__PopupMessage(localeInfo.GUILD_MARK_NOT_ENOUGH_LEVEL)
		elif not guild.MainPlayerHasAuthority(guild.AUTH_NOTICE):
			self.__PopupMessage(localeInfo.GUILD_NO_NOTICE_PERMISSION)
		else:
			self.markSelectDialog.Open()

	def __OnClickSelectGuildSymbolButton(self):
		if guild.MainPlayerHasAuthority(guild.AUTH_NOTICE):
			self.symbolSelectDialog.Open()
		else:
			self.__PopupMessage(localeInfo.GUILD_NO_NOTICE_PERMISSION)

	def __OnClickDeclareWarButton(self):
		self.inputDialog = uiGuild.DeclareGuildWarDialog()
		self.inputDialog.Open()

	def __OnSelectMark(self, markFileName):
		ret = net.UploadMark("upload/" + markFileName)
		if net.ERROR_MARK_UPLOAD_NEED_RECONNECT == ret:
			self.__PopupMessage(localeInfo.UPLOAD_MARK_UPLOAD_NEED_RECONNECT)
		return ret

	def __OnSelectSymbol(self, symbolFileName):
		net.UploadSymbol("upload/" + symbolFileName)

	def __OnClickOfferButton(self):
		curEXP = unsigned32(player.GetStatus(player.EXP))
		if curEXP <= 100:
			self.__PopupMessage(localeInfo.GUILD_SHORT_EXP)
			return
		self.offerDialog.Open(curEXP, 100)

	def OnOffer(self, exp):
		net.SendGuildOfferPacket(exp)

	def __GetStatMinusPoint(self):
		POINT_STAT_RESET_COUNT = 112
		return player.GetStatus(POINT_STAT_RESET_COUNT)

	def __OverInStatMinusButton(self, stat):
		try:
			self.__ShowStatToolTip(self.STAT_MINUS_DESCRIPTION[stat] % self.__GetStatMinusPoint())
		except KeyError:
			pass

		self.refreshToolTip = lambda arg=stat: self.__OverInStatMinusButton(arg) 

	def __OverOutStatMinusButton(self):
		self.__HideStatToolTip()
		self.refreshToolTip = 0

	def __OverInStatButton(self, stat):	
		try:
			self.__ShowStatToolTip(self.STAT_DESCRIPTION[stat])
		except KeyError:
			pass

	def __OverOutStatButton(self):
		self.__HideStatToolTip()

	def __ShowStatToolTip(self, statDesc):
		self.toolTip.ClearToolTip()
		self.toolTip.AppendTextLine(statDesc)
		self.toolTip.Show()

	def __HideStatToolTip(self):
		self.toolTip.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnUpdate(self):
		self.__UpdateQuestClock()

	## Skill Process
	def __RefreshSkillPage(self, name, slotCount):
		global SHOW_LIMIT_SUPPORT_SKILL_LIST

		skillPage = self.skillPageDict[name]

		startSlotIndex = skillPage.GetStartIndex()
		if "ACTIVE" == name:
			if self.PAGE_HORSE == self.curSelectedSkillGroup:
				startSlotIndex += slotCount

		getSkillType=skill.GetSkillType
		getSkillIndex=player.GetSkillIndex
		getSkillGrade=player.GetSkillGrade
		getSkillLevel=player.GetSkillLevel
		getSkillLevelUpPoint=skill.GetSkillLevelUpPoint
		getSkillMaxLevel=skill.GetSkillMaxLevel
		for i in xrange(slotCount+1):

			slotIndex = i + startSlotIndex
			skillIndex = getSkillIndex(slotIndex)

			for j in xrange(skill.SKILL_GRADE_COUNT):
				skillPage.ClearSlot(self.__GetRealSkillSlot(j, i))

			if 0 == skillIndex:
				continue

			skillGrade = getSkillGrade(slotIndex)
			skillLevel = getSkillLevel(slotIndex)
			skillType = getSkillType(skillIndex)

			## ¸ ų  ó
			if player.SKILL_INDEX_RIDING == skillIndex:
				if 1 == skillGrade:
					skillLevel += 19
				elif 2 == skillGrade:
					skillLevel += 29
				elif 3 == skillGrade:
					skillLevel = 40

				skillPage.SetSkillSlotNew(slotIndex, skillIndex, max(skillLevel-1, 0), skillLevel)
				skillPage.SetSlotCount(slotIndex, skillLevel)

			## ACTIVE
			elif skill.SKILL_TYPE_ACTIVE == skillType:
				for j in xrange(skill.SKILL_GRADE_COUNT):
					realSlotIndex = self.__GetRealSkillSlot(j, slotIndex)
					skillPage.SetSkillSlotNew(realSlotIndex, skillIndex, j, skillLevel)
					skillPage.SetCoverButton(realSlotIndex)

					if (skillGrade == skill.SKILL_GRADE_COUNT) and j == (skill.SKILL_GRADE_COUNT-1):
						skillPage.SetSlotCountNew(realSlotIndex, skillGrade, skillLevel)
					elif (not self.__CanUseSkillNow()) or (skillGrade != j):
						skillPage.SetSlotCount(realSlotIndex, 0)
						skillPage.DisableCoverButton(realSlotIndex)
					else:
						skillPage.SetSlotCountNew(realSlotIndex, skillGrade, skillLevel)

			## ׿
			else:
				if not SHOW_LIMIT_SUPPORT_SKILL_LIST or skillIndex in SHOW_LIMIT_SUPPORT_SKILL_LIST:
					realSlotIndex = self.__GetETCSkillRealSlotIndex(slotIndex)
					skillPage.SetSkillSlot(realSlotIndex, skillIndex, skillLevel)
					skillPage.SetSlotCountNew(realSlotIndex, skillGrade, skillLevel)

					if skill.CanUseSkill(skillIndex):
						skillPage.SetCoverButton(realSlotIndex)

			skillPage.RefreshSlot()


	def RefreshSkill(self):

		if self.isLoaded==0:
			return

		if self.__IsChangedHorseRidingSkillLevel():
			self.RefreshCharacter()
			return


		global SHOW_ONLY_ACTIVE_SKILL
		if SHOW_ONLY_ACTIVE_SKILL:
			self.__RefreshSkillPage("ACTIVE", self.ACTIVE_PAGE_SLOT_COUNT)
		else:
			self.__RefreshSkillPage("ACTIVE", self.ACTIVE_PAGE_SLOT_COUNT)
			self.__RefreshSkillPage("SUPPORT", self.SUPPORT_PAGE_SLOT_COUNT)

		self.RefreshSkillPlusButtonList()

	def CanShowPlusButton(self, skillIndex, skillLevel, curStatPoint):

		## ų 
		if 0 == skillIndex:
			return False

		##   Ѵٸ
		if not skill.CanLevelUpSkill(skillIndex, skillLevel):
			return False

		return True

	def __RefreshSkillPlusButton(self, name):
		global HIDE_SUPPORT_SKILL_POINT
		if HIDE_SUPPORT_SKILL_POINT and "SUPPORT" == name:
			return

		slotWindow = self.skillPageDict[name]
		slotWindow.HideAllSlotButton()

		slotStatType = self.skillPageStatDict[name]
		if 0 == slotStatType:
			return

		statPoint = player.GetStatus(slotStatType)
		startSlotIndex = slotWindow.GetStartIndex()
		if "HORSE" == name:
			startSlotIndex += self.ACTIVE_PAGE_SLOT_COUNT

		if statPoint > 0:
			for i in xrange(self.PAGE_SLOT_COUNT):
				slotIndex = i + startSlotIndex
				skillIndex = player.GetSkillIndex(slotIndex)
				skillGrade = player.GetSkillGrade(slotIndex)
				skillLevel = player.GetSkillLevel(slotIndex)

				if skillIndex == 0:
					continue
				if skillGrade != 0:
					continue

				if name == "HORSE":
					if player.GetStatus(player.LEVEL) >= skill.GetSkillLevelLimit(skillIndex):
						if skillLevel < 20:
							slotWindow.ShowSlotButton(self.__GetETCSkillRealSlotIndex(slotIndex))

				else:
					if "SUPPORT" == name:						
						if not SHOW_LIMIT_SUPPORT_SKILL_LIST or skillIndex in SHOW_LIMIT_SUPPORT_SKILL_LIST:
							if self.CanShowPlusButton(skillIndex, skillLevel, statPoint):
								slotWindow.ShowSlotButton(slotIndex)
					else:
						if self.CanShowPlusButton(skillIndex, skillLevel, statPoint):
							slotWindow.ShowSlotButton(slotIndex)
					

	def RefreshSkillPlusButtonList(self):

		if self.isLoaded==0:
			return

		self.RefreshSkillPlusPointLabel()

		if not self.__CanUseSkillNow():
			return

		try:
			if self.PAGE_HORSE == self.curSelectedSkillGroup:
				self.__RefreshSkillPlusButton("HORSE")
			else:
				self.__RefreshSkillPlusButton("ACTIVE")

			self.__RefreshSkillPlusButton("SUPPORT")

		except:
			import exception
			exception.Abort("CharacterWindow.RefreshSkillPlusButtonList.BindObject")

	def RefreshSkillPlusPointLabel(self):
		if self.isLoaded==0:
			return

		if self.PAGE_HORSE == self.curSelectedSkillGroup:
			activeStatPoint = player.GetStatus(player.SKILL_HORSE)
			self.activeSkillPointValue.SetText(str(activeStatPoint))

		else:
			activeStatPoint = player.GetStatus(player.SKILL_ACTIVE)
			self.activeSkillPointValue.SetText(str(activeStatPoint))

		supportStatPoint = max(0, player.GetStatus(player.SKILL_SUPPORT))
		self.supportSkillPointValue.SetText(str(supportStatPoint))

	## Skill Level Up Button
	def OnPressedSlotButton(self, slotNumber):
		srcSlotIndex = self.__RealSkillSlotToSourceSlot(slotNumber)

		skillIndex = player.GetSkillIndex(srcSlotIndex)
		curLevel = player.GetSkillLevel(srcSlotIndex)
		maxLevel = skill.GetSkillMaxLevel(skillIndex)

		net.SendChatPacket("/skillup " + str(skillIndex))

	## Use Skill
	def ClickSkillSlot(self, slotIndex):

		srcSlotIndex = self.__RealSkillSlotToSourceSlot(slotIndex)
		skillIndex = player.GetSkillIndex(srcSlotIndex)
		skillType = skill.GetSkillType(skillIndex)

		if not self.__CanUseSkillNow():
			if skill.SKILL_TYPE_ACTIVE == skillType:
				return

		for slotWindow in self.skillPageDict.values():
			if slotWindow.HasSlot(slotIndex):
				if skill.CanUseSkill(skillIndex):
					player.ClickSkillSlot(srcSlotIndex)
					return

		mouseModule.mouseController.DeattachObject()

	## FIXME : ų   ȣ  ش  ãƼ Ʈ Ѵ.
	##         ſ ո.  ü ؾ ҵ.
	def OnUseSkill(self, slotIndex, coolTime):

		skillIndex = player.GetSkillIndex(slotIndex)
		skillType = skill.GetSkillType(skillIndex)

		## ACTIVE
		if skill.SKILL_TYPE_ACTIVE == skillType:
			skillGrade = player.GetSkillGrade(slotIndex)
			slotIndex = self.__GetRealSkillSlot(skillGrade, slotIndex)
		## ETC
		else:
			slotIndex = self.__GetETCSkillRealSlotIndex(slotIndex)

		for slotWindow in self.skillPageDict.values():
			if slotWindow.HasSlot(slotIndex):
				slotWindow.SetSlotCoolTime(slotIndex, coolTime)
				return

	def OnActivateSkill(self, slotIndex):

		skillGrade = player.GetSkillGrade(slotIndex)
		slotIndex = self.__GetRealSkillSlot(skillGrade, slotIndex)

		for slotWindow in self.skillPageDict.values():
			if slotWindow.HasSlot(slotIndex):
				slotWindow.ActivateSlot(slotIndex)
				return

	def OnDeactivateSkill(self, slotIndex):

		skillGrade = player.GetSkillGrade(slotIndex)
		slotIndex = self.__GetRealSkillSlot(skillGrade, slotIndex)

		for slotWindow in self.skillPageDict.values():
			if slotWindow.HasSlot(slotIndex):
				slotWindow.DeactivateSlot(slotIndex)
				return

	def __ShowJobToolTip(self):
		self.toolTipJob.ShowToolTip()

	def __HideJobToolTip(self):
		self.toolTipJob.HideToolTip()

	def __SetJobText(self, mainJob, subJob):
		if player.GetStatus(player.LEVEL)<5:
			subJob=0

		if 949 == app.GetDefaultCodePage():
			self.toolTipJob.ClearToolTip()

			try:
				jobInfoTitle=localeInfo.JOBINFO_TITLE[mainJob][subJob]
				jobInfoData=localeInfo.JOBINFO_DATA_LIST[mainJob][subJob]
			except IndexError:
				print "uiCharacter.CharacterWindow.__SetJobText(mainJob=%d, subJob=%d)" % (mainJob, subJob)
				return

			self.toolTipJob.AutoAppendTextLine(jobInfoTitle)
			self.toolTipJob.AppendSpace(5)

			for jobInfoDataLine in jobInfoData:
				self.toolTipJob.AutoAppendTextLine(jobInfoDataLine)

			self.toolTipJob.AlignHorizonalCenter()

	def __ShowAlignmentToolTip(self):
		self.toolTipAlignment.ShowToolTip()

	def __HideAlignmentToolTip(self):
		self.toolTipAlignment.HideToolTip()

	def RefreshCharacter(self):

		if self.isLoaded==0:
			return

		## Name
		try:
			characterName = player.GetName()
			guildName = player.GetGuildName()
			self.characterNameValue.SetText(characterName)
			self.guildNameValue.SetText(guildName)
			if not guildName:
				if localeInfo.IsARABIC():
					self.characterNameSlot.SetPosition(190, 34)
				else:
					self.characterNameSlot.SetPosition(109, 34)

				self.guildNameSlot.Hide()
			else:
				self.characterNameSlot.SetPosition(153, 34)
				self.guildNameSlot.Show()
		except:
			import exception
			exception.Abort("CharacterWindow.RefreshCharacter.BindObject")

		race = net.GetMainActorRace()
		group = net.GetMainActorSkillGroup()
		empire = net.GetMainActorEmpire()

		## Job Text
		job = chr.RaceToJob(race)
		self.__SetJobText(job, group)

		## FaceImage
		try:
			faceImageName = FACE_IMAGE_DICT[race]

			try:
				self.faceImage.LoadImage(faceImageName)
			except:
				print "CharacterWindow.RefreshCharacter(race=%d, faceImageName=%s)" % (race, faceImageName)
				self.faceImage.Hide()

		except KeyError:
			self.faceImage.Hide()

		## GroupName
		self.__SetSkillGroupName(race, group)

		## Skill
		if 0 == group:
			self.__SelectSkillGroup(0)

		else:
			self.__SetSkillSlotData(race, group, empire)

			if self.__CanUseHorseSkill():
				self.__SelectSkillGroup(0)

	def __SetSkillGroupName(self, race, group):

		job = chr.RaceToJob(race)

		if not self.SKILL_GROUP_NAME_DICT.has_key(job):
			return

		nameList = self.SKILL_GROUP_NAME_DICT[job]

		if 0 == group:
			self.skillGroupButton1.SetText(nameList[1])
			self.skillGroupButton2.SetText(nameList[2])
			self.skillGroupButton1.Show()
			self.skillGroupButton2.Show()
			self.activeSkillGroupName.Hide()

		else:

			if self.__CanUseHorseSkill():
				self.activeSkillGroupName.Hide()
				self.skillGroupButton1.SetText(nameList.get(group, "Noname"))
				self.skillGroupButton2.SetText(localeInfo.SKILL_GROUP_HORSE)
				self.skillGroupButton1.Show()
				self.skillGroupButton2.Show()

			else:
				self.activeSkillGroupName.SetText(nameList.get(group, "Noname"))
				self.activeSkillGroupName.Show()
				self.skillGroupButton1.Hide()
				self.skillGroupButton2.Hide()

	def __SetSkillSlotData(self, race, group, empire=0):

		## SkillIndex
		playerSettingModule.RegisterSkill(race, group, empire)

		## Event
		self.__SetSkillSlotEvent()

		## Refresh
		self.RefreshSkill()

	def __SelectSkillGroup(self, index):
		for btn in self.skillGroupButton:
			btn.SetUp()
		self.skillGroupButton[index].Down()

		if self.__CanUseHorseSkill():
			if 0 == index:
				index = net.GetMainActorSkillGroup()-1
			elif 1 == index:
				index = self.PAGE_HORSE

		self.curSelectedSkillGroup = index
		self.__SetSkillSlotData(net.GetMainActorRace(), index+1, net.GetMainActorEmpire())

	def __CanUseSkillNow(self):
		if 0 == net.GetMainActorSkillGroup():
			return False

		return True

	def __CanUseHorseSkill(self):

		slotIndex = player.GetSkillSlotIndex(player.SKILL_INDEX_RIDING)

		if not slotIndex:
			return False

		grade = player.GetSkillGrade(slotIndex)
		level = player.GetSkillLevel(slotIndex)
		if level < 0:
			level *= -1
		if grade >= 1 and level >= 1:
			return True

		return False

	def __IsChangedHorseRidingSkillLevel(self):
		ret = False

		if -1 == self.canUseHorseSkill:
			self.canUseHorseSkill = self.__CanUseHorseSkill()

		if self.canUseHorseSkill != self.__CanUseHorseSkill():
			ret = True

		self.canUseHorseSkill = self.__CanUseHorseSkill()
		return ret

	def __GetRealSkillSlot(self, skillGrade, skillSlot):
		return skillSlot + min(skill.SKILL_GRADE_COUNT-1, skillGrade)*skill.SKILL_GRADE_STEP_COUNT

	def __GetETCSkillRealSlotIndex(self, skillSlot):
		if skillSlot > 100:
			return skillSlot
		return skillSlot % self.ACTIVE_PAGE_SLOT_COUNT

	def __RealSkillSlotToSourceSlot(self, realSkillSlot):
		if realSkillSlot > 100:
			return realSkillSlot
		if self.PAGE_HORSE == self.curSelectedSkillGroup:
			return realSkillSlot + self.ACTIVE_PAGE_SLOT_COUNT
		return realSkillSlot % skill.SKILL_GRADE_STEP_COUNT

	def __GetSkillGradeFromSlot(self, skillSlot):
		return int(skillSlot / skill.SKILL_GRADE_STEP_COUNT)

	def SelectSkillGroup(self, index):
		self.__SelectSkillGroup(index)

	def OnQuestMainScroll(self):
		if not self.questMainScrollBar:
			return

		questCount = quest.GetQuestCount()
		if questCount > quest.QUEST_MAX_NUM:
			scrollPos = self.questMainScrollBar.GetPos()
			scrollLineCount = max(0, questCount - quest.QUEST_MAX_NUM)
			self.questShowingStartIndex = int(scrollLineCount * scrollPos)

		self.RefreshQuest()

	def OnQuestSubScroll(self):
		if not self.questSubScrollBar:
			return

		questCount = quest.GetQuestCount()
		if questCount > 5:
			scrollPos = self.questSubScrollBar.GetPos()
			scrollLineCount = max(0, questCount - 5)
			self.questSubShowingStartIndex = int(scrollLineCount * scrollPos)

		self.RefreshQuest()