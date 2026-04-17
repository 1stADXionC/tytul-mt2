import uiScriptLocale

QUEST_ICON_BACKGROUND = 'd:/ymir work/ui/game/quest/slot_base.sub'

SMALL_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_00.sub"
MIDDLE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_01.sub"
LARGE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_03.sub"
XLARGE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_04.sub"
ICON_SLOT_FILE = "d:/ymir work/ui/public/Slot_Base.sub"
FACE_SLOT_FILE = "d:/ymir work/ui/game/windows/box_face.sub"
ROOT_PATH = "d:/ymir work/ui/game/windows/"

LOCALE_PATH = uiScriptLocale.WINDOWS_PATH

window = {
	"name" : "CharacterWindow",
	"style" : ("movable", "float",),

	"x" : 24,
	"y" : (SCREEN_HEIGHT - 37 - 361) / 2,

	"width" : 365,
	"height" : 361,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 365,
			"height" : 361,

			"children" :
			(
				{
					"name" : "Skill_TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 7,

					"width" : 349,
					"color" : "red",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":0, "y":-1, "text":uiScriptLocale.CHARACTER_SKILL, "all_align":"center" },
						#{ "name":"TitleName", "type":"image", "style" : ("attach",), "x":101, "y" : 1, "image" : LOCALE_PATH+"title_skill.sub", },
					),
				},
				{
					"name" : "Emoticon_TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 7,

					"width" : 349,
					"color" : "red",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":0, "y":-1, "text":uiScriptLocale.CHARACTER_ACTION, "all_align":"center" },
					),
				},
				{
					"name" : "Quest_TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 7,

					"width" : 349,
					"color" : "red",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":0, "y":-1, "text":uiScriptLocale.CHARACTER_QUEST, "all_align":"center" },
					),
				},
                {
					"name" : "Guild_TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 7,

					"width" : 349,
					"color" : "red",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":0, "y":-1, "text":uiScriptLocale.CHARACTER_GUILD, "all_align":"center" },
					),
				},
				{
					"name" : "Titles_Page",
					"type" : "window",
					"style" : ("attach",),

					"x" : 0,
					"y" : 0,

					"width" : 365,
					"height" : 328,

					"children" :
					(
						{ "name" : "Titles_TitleBar", "type" : "titlebar", "style" : ("attach",), "x" : 8, "y" : 7, "width" : 349, "color" : "red", "children" :
					(
						{ "name":"TitleName", "type":"text", "x":0, "y":-1, "text":uiScriptLocale.CHARACTER_TITLES, "all_align":"center" },
					),
				},
				{
					"name" : "TitleListBoard",
				"type" : "thinboard",
				"x" : 8,
				"y" : 32,
				"width" : 185,
				"height" : 288,

				"children" :
				(	
					{ "name":"TitleListHeader", "type":"text", "x":92, "y":6, "text":"Lista tytu³ów", "text_horizontal_align":"center" },

				{
					"name" : "TitleList",
					"type" : "listboxex",
					"x" : 20,
					"y" : 36,
					"width" : 130,
					"height" : 230,
					"viewcount" : 12,
				},
				{
					"name" : "TitleScrollBar",
					"type" : "scrollbar",
					"x" : 170,
					"y" : 36,
					"size" : 220,
				},
			),
		},

		{
			"name" : "TitleInfoBoard",
			"type" : "thinboard",
			"x" : 198,
			"y" : 32,
			"width" : 159,
			"height" : 288,

			"children" :
			(
				{ "name":"TitleInfoHeader", "type":"text", "x":79, "y":6, "text":"Opis tytu³u", "text_horizontal_align":"center" },

				{ "name":"SelectedTitleName", "type":"text", "x":79, "y":35, "text":"", "text_horizontal_align":"center" },

				{ "name":"SelectedTitleDesc1", "type":"text", "x":10, "y":78, "text":"" },
				{ "name":"SelectedTitleDesc2", "type":"text", "x":10, "y":94, "text":"" },
				{ "name":"SelectedTitleDesc3", "type":"text", "x":10, "y":110, "text":"" },
                { "name":"SelectedTitleDesc4", "type":"text", "x":10, "y":126, "text":"" },
                { "name":"SelectedTitleDesc5", "type":"text", "x":10, "y":142, "text":"" },

				{ "name":"SelectedTitleBonus1", "type":"text", "x":10, "y":165, "text":"", "r":1.0, "g":0.6, "b":0.0 },
				{ "name":"SelectedTitleBonus2", "type":"text", "x":10, "y":181, "text":"", "r":1.0, "g":0.6, "b":0.0 },
				{ "name":"SelectedTitleBonus3", "type":"text", "x":10, "y":197, "text":"", "r":1.0, "g":0.6, "b":0.0 },
							),
						},
					),
				},
				## Tab Area
				{
					"name" : "TabControl",
					"type" : "window",

					"x" : 0,
					"y" : 328,

					"width" : 362,
					"height" : 31,

					"children" :
					(
						## Tab
						{
							"name" : "Tab_01",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : 250,
							"height" : 31,

							"image" : LOCALE_PATH+"tab_1.sub",
						},
						{
							"name" : "Tab_02",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : 250,
							"height" : 31,

							"image" : LOCALE_PATH+"tab_2.sub",
						},
						{
							"name" : "Tab_03",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : 250,
							"height" : 31,

							"image" : LOCALE_PATH+"tab_3.sub",
						},
						{
							"name" : "Tab_04",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : 250,
							"height" : 31,

							"image" : LOCALE_PATH+"tab_4.sub",
						},
                        {
							"name" : "Tab_05",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : 250,
							"height" : 31,

							"image" : LOCALE_PATH+"tab_4.sub",
						},
                        {
							"name" : "Tab_06",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : 250,
							"height" : 31,

							"image" : LOCALE_PATH+"tab_4.sub",
						},
						## RadioButton
						{
							"name" : "Tab_Button_01",
							"type" : "radio_button",

							"x" : 6,
							"y" : 5,

							"width" : 53,
							"height" : 27,
						},
						{
							"name" : "Tab_Button_02",
							"type" : "radio_button",

							"x" : 61,
							"y" : 5,

							"width" : 67,
							"height" : 27,
						},
						{
							"name" : "Tab_Button_03",
							"type" : "radio_button",

							"x" : 130,
							"y" : 5,

							"width" : 61,
							"height" : 27,
						},
						{
							"name" : "Tab_Button_04",
							"type" : "radio_button",

							"x" : 192,
							"y" : 5,

							"width" : 55,
							"height" : 27,
						},
                        {
							"name" : "Tab_Button_05",
							"type" : "radio_button",

							"x" : 248,
							"y" : 5,

							"width" : 55,
							"height" : 27,
						},
                        {
							"name" : "Tab_Button_06",
							"type" : "radio_button",

							"x" : 304,
							"y" : 5,

							"width" : 55,
							"height" : 27,
						},
					),
				},

				## Page Area
				{
					"name" : "Character_Page",
					"type" : "window",
					"style" : ("attach",),

					"x" : 0,
					"y" : 0,

					"width" : 250,
					"height" : 304,

					"children" :
					(

						## Title Area
						{
							"name" : "Character_TitleBar", "type" : "titlebar", "style" : ("attach",), "x" : 61, "y" : 7, "width" : 296, "color" : "red",
							"children" :
							(
								#{ "name" : "TitleName", "type" : "image", "style" : ("attach",), "x" : 70, "y" : 1, "image" : LOCALE_PATH+"title_status.sub", },
								{ "name" : "TitleName", "type":"text", "x":0, "y":-1, "text":uiScriptLocale.CHARACTER_MAIN, "all_align":"center" },
							),
						},

						## Guild Name Slot
						{
							"name" : "Guild_Name_Slot",
							"type" : "image",
							"x" : 60,
							"y" :27+7,
							"image" : LARGE_VALUE_FILE,

							"children" :
							(
								{
									"name" : "Guild_Name",
									"type":"text",
									"text":" ?",
									"x":0,
									"y":0,
									"r":1.0,
									"g":1.0,
									"b":1.0,
									"a":1.0,
									"all_align" : "center",
								},
							),
						},

						## Character Name Slot
						{
							"name" : "Character_Name_Slot",
							"type" : "image",
							"x" : 153,
							"y" :27+7,
							"image" : LARGE_VALUE_FILE,

							"children" :
							(
								{
									"name" : "Character_Name",
									"type":"text",
									"text":"?? ?",
									"x":0,
									"y":0,
									"r":1.0,
									"g":1.0,
									"b":1.0,
									"a":1.0,
									"all_align" : "center",
								},
							),
						},

						## Header
						{ 
							"name":"Status_Header", "type":"window", "x":3, "y":31, "width":0, "height":0, 
							"children" :
							(
								## Lv
								{
									"name":"Status_Lv", "type":"window", "x":9, "y":30, "width":37, "height":42, 
									"children" :
									(
										{ "name":"Level_Header", "type":"image", "x":0, "y":0, "image":LOCALE_PATH+"label_level.sub" },
										{ "name":"Level_Value", "type":"text", "x":19, "y":19, "fontsize":"LARGE", "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									),
								},

								## EXP
								{
									"name":"Status_CurExp", "type":"window", "x":53, "y":30, "width":87, "height":42,
									"children" :
									(
										{ "name":"Exp_Slot", "type":"image", "x":0, "y":0, "image":LOCALE_PATH+"label_cur_exp.sub" },
										{ "name":"Exp_Value", "type":"text", "x":46, "y":19, "fontsize":"LARGE", "text":"12345678901", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },									),
								},

								## REXP
								{
									"name":"Status_RestExp", "type":"window", "x":150, "y":30, "width":50, "height":20, 
									"children" :
									(
										{ "name":"RestExp_Slot", "type":"image", "x":0, "y":0, "image":LOCALE_PATH+"label_last_exp.sub" },
										{ "name":"RestExp_Value", "type":"text", "x":46, "y":19, "fontsize":"LARGE", "text":"12345678901", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									),
								},
							),
						},

						## Face Slot
						{ "name" : "Face_Image", "type" : "image", "x" : 11, "y" : 11, "image" : "d:/ymir work/ui/game/windows/face_warrior.sub" },
						{ "name" : "Face_Slot", "type" : "image", "x" : 7, "y" : 7, "image" : FACE_SLOT_FILE, },

						## ? ?	
							{ "name":"Status_Standard", "type":"window", "x":3, "y":100, "width":200, "height":250,
							"children" :
							(
								## ? ?
								{ "name":"Character_Bar_01", "type":"horizontalbar", "x":12, "y":8, "width":223, },
								{ "name":"Character_Bar_01_Text", "type" : "image", "x" : 13, "y" : 9, "image" : LOCALE_PATH+"label_std.sub", },
								
								##  ? ?
								{ 
									"name":"Status_Plus_Label", 
									"type":"image", 
									"x":150, "y":11, 
									"image":LOCALE_PATH+"label_uppt.sub", 
									
									"children" :
									(
										{ "name":"Status_Plus_Value", "type":"text", "x":62, "y":0, "text":"99", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									),
								},

								## ? ? ?
								{"name":"Status_Standard_ItemList1", "type" : "image", "x":17, "y":31, "image" : LOCALE_PATH+"label_std_item1.sub", },
								{"name":"Status_Standard_ItemList2", "type" : "image", "x":100, "y":30, "image" : LOCALE_PATH+"label_std_item2.sub", },

								## HTH
								{
									"name":"HTH_Label", "type":"window", "x":50, "y":32, "width":60, "height":20,
									"children" :
									(
										{ "name":"HTH_Slot", "type":"image", "x":0, "y":0, "image":SMALL_VALUE_FILE },
										{ "name":"HTH_Value", "type":"text", "x":20, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										{ "name":"HTH_Plus", "type" : "button", "x":41, "y":3, "default_image" : ROOT_PATH+"btn_plus_up.sub", "over_image" : ROOT_PATH+"btn_plus_over.sub", "down_image" : ROOT_PATH+"btn_plus_down.sub", },
									),
								},
								## INT
								{
									"name":"INT_Label", "type":"window", "x":50, "y":32+23, "width":60, "height":20,
									"children" :
									(
										{ "name":"INT_Slot", "type":"image", "x":0, "y":0, "image":SMALL_VALUE_FILE },
										{ "name":"INT_Value", "type":"text", "x":20, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										{ "name":"INT_Plus", "type" : "button", "x" : 41, "y" : 3, "default_image" : ROOT_PATH+"btn_plus_up.sub", "over_image" : ROOT_PATH+"btn_plus_over.sub", "down_image" : ROOT_PATH+"btn_plus_down.sub", },
									)
								},
								## STR
								{
									"name":"STR_Label", "type":"window", "x":50, "y":32+23*2, "width":60, "height":20,
									"children" :
									(
										{ "name":"STR_Slot", "type":"image", "x":0, "y":0, "image":SMALL_VALUE_FILE },
										{ "name":"STR_Value", "type":"text", "x":20, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										{ "name":"STR_Plus", "type" : "button", "x" : 41, "y" : 3, "default_image" : ROOT_PATH+"btn_plus_up.sub", "over_image" : ROOT_PATH+"btn_plus_over.sub", "down_image" : ROOT_PATH+"btn_plus_down.sub", },
									)
								},
								## DEX
								{
									"name":"DEX_Label", "type":"window", "x":50, "y":32+23*3, "width":60, "height":20, 
									"children" :
									(
										{ "name":"DEX_Slot", "type":"image", "x":0, "y":0, "image":SMALL_VALUE_FILE },
										{ "name":"DEX_Value", "type":"text", "x":20, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										{ "name":"DEX_Plus", "type" : "button", "x" : 41, "y" : 3, "default_image" : ROOT_PATH+"btn_plus_up.sub", "over_image" : ROOT_PATH+"btn_plus_over.sub", "down_image" : ROOT_PATH+"btn_plus_down.sub", },
									)
								},

								{ "name":"HTH_Minus", "type" : "button", "x":9, "y":35, "default_image" : ROOT_PATH+"btn_minus_up.sub", "over_image" : ROOT_PATH+"btn_minus_over.sub", "down_image" : ROOT_PATH+"btn_minus_down.sub", },
								{ "name":"INT_Minus", "type" : "button", "x":9, "y":35+23, "default_image" : ROOT_PATH+"btn_minus_up.sub", "over_image" : ROOT_PATH+"btn_minus_over.sub", "down_image" : ROOT_PATH+"btn_minus_down.sub", },
								{ "name":"STR_Minus", "type" : "button", "x":9, "y":35+23*2, "default_image" : ROOT_PATH+"btn_minus_up.sub", "over_image" : ROOT_PATH+"btn_minus_over.sub", "down_image" : ROOT_PATH+"btn_minus_down.sub", },
								{ "name":"DEX_Minus", "type" : "button", "x":9, "y":35+23*3, "default_image" : ROOT_PATH+"btn_minus_up.sub", "over_image" : ROOT_PATH+"btn_minus_over.sub", "down_image" : ROOT_PATH+"btn_minus_down.sub", },

								####

								## HP
								{
									"name":"HEL_Label", "type":"window", "x":145, "y":32, "width":50, "height":20,
									"children" :
									(
										{ "name":"HP_Slot", "type":"image", "x":0, "y":0, "image":LARGE_VALUE_FILE },
										{ "name":"HP_Value", "type":"text", "x":45, "y":3, "text":"9999/9999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									),
								},
								## SP
								{
									"name":"SP_Label", "type":"window", "x":145, "y":32+23, "width":50, "height":20, 
									"children" :
									(
										{ "name":"SP_Slot", "type":"image", "x":0, "y":0, "image":LARGE_VALUE_FILE },
										{ "name":"SP_Value", "type":"text", "x":45, "y":3, "text":"9999/9999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								## ATT
								{
									"name":"ATT_Label", "type":"window", "x":145, "y":32+23*2, "width":50, "height":20, 
									"children" :
									(
										{ "name":"ATT_Slot", "type":"image", "x":0, "y":0, "image":LARGE_VALUE_FILE },
										{ "name":"ATT_Value", "type":"text", "x":45, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									),
								},
								## DEF
								{
									"name":"DEF_Label", "type":"window", "x":145, "y":32+23*3, "width":50, "height":20, 
									"children" :
									(
										{ "name":"DEF_Slot", "type":"image", "x":0, "y":0, "image":LARGE_VALUE_FILE },
										{ "name":"DEF_Value", "type":"text", "x":45, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
							),
						},
						
						## ?  ?	
							{ "name":"Status_Extent", "type":"window", "x":3, "y":221, "width":200, "height":50, 
							"children" :
							(

								## ?  ?
								{ "name":"Status_Extent_Bar", "type":"horizontalbar", "x":12, "y":6, "width":223, },
								{ "name":"Status_Extent_Label", "type" : "image", "x" : 13, "y" : 8, "image" : LOCALE_PATH+"label_ext.sub", },

								## ? ? ?
								{"name":"Status_Extent_ItemList1", "type" : "image", "x":11, "y":31, "image" : LOCALE_PATH+"label_ext_item1.sub", },
								{"name":"Status_Extent_ItemList2", "type" : "image", "x":128, "y":32, "image" : LOCALE_PATH+"label_ext_item2.sub", },

								## MSPD - ? ?
								{
									"name":"MOV_Label", "type":"window", "x":66, "y":33, "width":50, "height":20, 
									"children" :
									(
										{ "name":"MSPD_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"MSPD_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},

								## ASPD -  ?
								{
									"name":"ASPD_Label", "type":"window", "x":66, "y":33+23, "width":50, "height":20, 
									"children" :
									(
										{ "name":"ASPD_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"ASPD_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},

								## CSPD - ? ?
								{
									"name":"CSPD_Label", "type":"window", "x":66, "y":33+23*2, "width":50, "height":20, 
									"children" :
									(
										{ "name":"CSPD_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"CSPD_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},

								## MATT -  ?
								{
									"name":"MATT_Label", "type":"window", "x":183, "y":33, "width":50, "height":20, 
									"children" :
									(
										{ "name":"MATT_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"MATT_Value", "type":"text", "x":26, "y":3, "text":"999-999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},

								## MDEF -  
								{
									"name":"MDEF_Label", "type":"window", "x":183, "y":33+23, "width":50, "height":20, 
									"children" :
									(
										{ "name":"MDEF_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"MDEF_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},

								## ?
								{
									"name":"ER_Label", "type":"window", "x":183, "y":33+23*2, "width":50, "height":20, 
									"children" :
									(
										{ "name":"ER_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"ER_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},

							),
						},
					),
				},
				{
					"name" : "Skill_Page",
					"type" : "window",
					"style" : ("attach",),

					"x" : 0,
					"y" : 24,

					"width" : 250,
					"height" : 304,

					"children" :
					(

						{
							"name":"Skill_Active_Title_Bar", "type":"horizontalbar", "x":15, "y":17, "width":223,

							"children" :
							(
								{ 
									"name":"Active_Skill_Point_Label", "type":"image", "x":145, "y":3, "image":LOCALE_PATH+"label_uppt.sub",
									"children" :
									(
										{ "name":"Active_Skill_Point_Value", "type":"text", "x":62, "y":0, "text":"99", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									),
								},

								## Group Button
								{
									"name" : "Skill_Group_Button_1",
									"type" : "radio_button",

									"x" : 5,
									"y" : 2,

									"text" : "Group1",
									"text_color" : 0xFFFFE3AD,

									"default_image" : "d:/ymir work/ui/game/windows/skill_tab_button_01.sub",
									"over_image" : "d:/ymir work/ui/game/windows/skill_tab_button_02.sub",
									"down_image" : "d:/ymir work/ui/game/windows/skill_tab_button_03.sub",
								},

								{
									"name" : "Skill_Group_Button_2",
									"type" : "radio_button",

									"x" : 50,
									"y" : 2,

									"text" : "Group2",
									"text_color" : 0xFFFFE3AD,

									"default_image" : "d:/ymir work/ui/game/windows/skill_tab_button_01.sub",
									"over_image" : "d:/ymir work/ui/game/windows/skill_tab_button_02.sub",
									"down_image" : "d:/ymir work/ui/game/windows/skill_tab_button_03.sub",
								},

								{
									"name" : "Active_Skill_Group_Name",
									"type" : "text",

									"x" : 7,
									"y" : 1,
									"text" : "Active",

									"vertical_align" : "center",
									"text_vertical_align" : "center",
									"color" : 0xFFFFE3AD,
								},

							),
						},

						{
							"name":"Skill_ETC_Title_Bar", "type":"horizontalbar", "x":15, "y":200, "width":223,

							"children" :
							(
								{
									"name" : "Support_Skill_Group_Name",
									"type" : "text",

									"x" : 7,
									"y" : 1,
									"text" : uiScriptLocale.SKILL_SUPPORT_TITLE,

									"vertical_align" : "center",
									"text_vertical_align" : "center",
									"color" : 0xFFFFE3AD,
								},

								{ 
									"name":"Support_Skill_Point_Label", "type":"image", "x":145, "y":3, "image":LOCALE_PATH+"label_uppt.sub",
									"children" :
									(
										{ "name":"Support_Skill_Point_Value", "type":"text", "x":62, "y":0, "text":"99", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									),
								},
							),
						},
						{ "name":"Skill_Board", "type":"image", "x":13, "y":38, "image":"d:/ymir work/ui/game/windows/skill_board.sub", },

						## Active Slot
						{
							"name" : "Skill_Active_Slot",
							"type" : "slot",

							"x" : 0 + 16,
							"y" : 0 + 15 + 23,

							"width" : 223,
							"height" : 223,
							"image" : ICON_SLOT_FILE,

							"slot" :	(
											{"index": 1, "x": 1, "y":  4, "width":32, "height":32},
											{"index":21, "x":38, "y":  4, "width":32, "height":32},
											{"index":41, "x":75, "y":  4, "width":32, "height":32},

											{"index": 3, "x": 1, "y": 40, "width":32, "height":32},
											{"index":23, "x":38, "y": 40, "width":32, "height":32},
											{"index":43, "x":75, "y": 40, "width":32, "height":32},

											{"index": 5, "x": 1, "y": 76, "width":32, "height":32},
											{"index":25, "x":38, "y": 76, "width":32, "height":32},
											{"index":45, "x":75, "y": 76, "width":32, "height":32},

											{"index": 7, "x": 1, "y":112, "width":32, "height":32},
											{"index":27, "x":38, "y":112, "width":32, "height":32},
											{"index":47, "x":75, "y":112, "width":32, "height":32},

											####

											{"index": 2, "x":113, "y":  4, "width":32, "height":32},
											{"index":22, "x":150, "y":  4, "width":32, "height":32},
											{"index":42, "x":187, "y":  4, "width":32, "height":32},

											{"index": 4, "x":113, "y": 40, "width":32, "height":32},
											{"index":24, "x":150, "y": 40, "width":32, "height":32},
											{"index":44, "x":187, "y": 40, "width":32, "height":32},

											{"index": 6, "x":113, "y": 76, "width":32, "height":32},
											{"index":26, "x":150, "y": 76, "width":32, "height":32},
											{"index":46, "x":187, "y": 76, "width":32, "height":32},

											{"index": 8, "x":113, "y":112, "width":32, "height":32},
											{"index":28, "x":150, "y":112, "width":32, "height":32},
											{"index":48, "x":187, "y":112, "width":32, "height":32},
										),
						},

						## ETC Slot
						{
							"name" : "Skill_ETC_Slot",
							"type" : "grid_table",
							"x" : 18,
							"y" : 221,
							"start_index" : 101,
							"x_count" : 6,
							"y_count" : 2,
							"x_step" : 32,
							"y_step" : 32,
							"x_blank" : 5,
							"y_blank" : 4,
							"image" : ICON_SLOT_FILE,
						},

					),
				},
				{
					"name" : "Emoticon_Page",
					"type" : "window",
					"style" : ("attach",),

					"x" : 0,
					"y" : 24,

					"width" : 250,
					"height" : 304,

					"children" :
					(
						## ?? 
						{ "name":"Action_Bar", "type":"horizontalbar", "x":12, "y":11, "width":223, },
						{ "name":"Action_Bar_Text", "type":"text", "x":15, "y":13, "text":uiScriptLocale.CHARACTER_NORMAL_ACTION },

						## Basis Action Slot
						{
							"name" : "SoloEmotionSlot",
							"type" : "grid_table",
							"x" : 30,
							"y" : 33,
							"horizontal_align" : "center",
							"start_index" : 1,
							"x_count" : 6,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,
							"x_blank" : 0,
							"y_blank" : 0,
							"image" : ICON_SLOT_FILE,
						},

						## ? ? 
						{ "name":"Reaction_Bar", "type":"horizontalbar", "x":12, "y":8+150, "width":223, },
						{ "name":"Reaction_Bar_Text", "type":"text", "x":15, "y":10+150, "text":uiScriptLocale.CHARACTER_MUTUAL_ACTION },

						## Reaction Slot
						{
							"name" : "DualEmotionSlot",
							"type" : "grid_table",
							"x" : 30,
							"y" : 180,
							"start_index" : 51,
							"x_count" : 6,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,
							"x_blank" : 0,
							"y_blank" : 0,
							"image" : ICON_SLOT_FILE,
						},
					),
				},
				{
					"name" : "Quest_Page",
					"type" : "window",
					"style" : ("attach",),

					"x" : 0,
					"y" : 24,

					"width" : 360,
					"height" : 304,

					"children" :
					(
						{ "name":"Quest_Left_Bar", "type":"horizontalbar", "x":8,   "y":8,  "width":140, },
						{ "name":"Quest_Left_Title_Main", "type":"text", "x":14, "y":10, "text":"G³ówna misja", },
                        
						{ "name":"Quest_Right_Bar", "type":"horizontalbar", "x":155, "y":8,  "width":202, },
						{ "name":"Quest_Right_Title", "type":"text", "x":161, "y":10, "text":"Treœæ misji", },

						{ "name":"Quest_List_Back", "type":"bar", "x":8,   "y":28, "width":140, "height":266, },
						{ "name":"Quest_Info_Back", "type":"bar", "x":155, "y":28, "width":202, "height":266, },

						{ "name":"Quest_Left_Bar_Sub", "type":"horizontalbar", "x":8, "y":165, "width":140, },
						{ "name":"Quest_Left_Title_Sub", "type":"text", "x":14, "y":145, "text":"Dodatkowe misje", },

						{
							"name" : "Quest_ScrollBar_Title_Main",
							"type" : "scrollbar",
							"x" : 135,  
							"y" : 34,
							"size" : 110,
						},

						{
							"name" : "Quest_ScrollBar_Title_Sub",
							"type" : "scrollbar",
							"x" : 135,  
							"y" : 160,
							"size" : 138,
						},

						{ "name" : "Quest_Name_00", "type" : "text", "text" : "Nazwa misji", "x" : 16, "y" : 35 },
						{ "name" : "Quest_Name_01", "type" : "text", "text" : "Nazwa misji", "x" : 16, "y" : 50 },
						{ "name" : "Quest_Name_02", "type" : "text", "text" : "Nazwa misji", "x" : 16, "y" : 65 },
						{ "name" : "Quest_Name_03", "type" : "text", "text" : "Nazwa misji", "x" : 16, "y" : 80 },
						{ "name" : "Quest_Name_04", "type" : "text", "text" : "Nazwa misji", "x" : 16, "y" : 95 },
						{ "name" : "Quest_Detail_Title", "type" : "text", "text" : "Wybierz misje", "x" : 161, "y" : 38 },
						{ "name" : "Quest_Detail_Line_01", "type" : "text", "text" : "Tutaj bedzie opis", "x" : 161, "y" : 64 },
						{ "name" : "Quest_Detail_Line_02", "type" : "text", "text" : "zaznaczonej misji.", "x" : 161, "y" : 80 },
						{ "name" : "Quest_Detail_Line_03", "type" : "text", "text" : "", "x" : 161, "y" : 96 },
						{ "name" : "Quest_Detail_Line_04", "type" : "text", "text" : "", "x" : 161, "y" : 112 },
						{ "name" : "Quest_Detail_Line_05", "type" : "text", "text" : "", "x" : 161, "y" : 128 },

						{
							"name" : "Quest_Row_00",
							"type" : "button",
							"x" : 10,
							"y" : 35,
							"width" : 100,
							"height" : 14,
							"default_image" : "d:/ymir work/ui/blank.tga",
							"over_image" : "d:/ymir work/ui/blank.tga",
							"down_image" : "d:/ymir work/ui/blank.tga",
						},
						{
							"name" : "Quest_Row_01",
							"type" : "button",
							"x" : 10,
							"y" : 50,
							"width" : 100,
							"height" : 14,
							"default_image" : "d:/ymir work/ui/blank.tga",
							"over_image" : "d:/ymir work/ui/blank.tga",
							"down_image" : "d:/ymir work/ui/blank.tga",
						},
						{
							"name" : "Quest_Row_02",
							"type" : "button",
							"x" : 10,
							"y" : 65,
							"width" : 100,
							"height" : 14,
							"default_image" : "d:/ymir work/ui/blank.tga",
							"over_image" : "d:/ymir work/ui/blank.tga",
							"down_image" : "d:/ymir work/ui/blank.tga",
						},
						{
							"name" : "Quest_Row_03",
							"type" : "button",
							"x" : 10,
							"y" : 80,
							"width" : 100,
							"height" : 14,
							"default_image" : "d:/ymir work/ui/blank.tga",
							"over_image" : "d:/ymir work/ui/blank.tga",
							"down_image" : "d:/ymir work/ui/blank.tga",
						},
						{
							"name" : "Quest_Row_04",
							"type" : "button",
							"x" : 10,
							"y" : 95,
							"width" : 100,
							"height" : 14,
							"default_image" : "d:/ymir work/ui/blank.tga",
							"over_image" : "d:/ymir work/ui/blank.tga",
							"down_image" : "d:/ymir work/ui/blank.tga",
						},

					),
				},
				{
					"name" : "Guild_Page",
					"type" : "window",
					"style" : ("attach",),

					"x" : 0,
					"y" : 24,

					"width" : 360,
					"height" : 304,

					"children" :
					(
						## Guild Info Title
		{
			"name":"Guild_Info_Title_Bar", "type":"horizontalbar", "x":5, "y":10, "width":167,
			"children" :
			(
				{ "name":"Guild_Info_Point_Value", "type":"text", "x":8, "y":3, "text":uiScriptLocale.GUILD_INFO, },

				## GuildName
				{
					"name" : "GuildName", "type" : "text", "x" : 3, "y" : 31, "text" : uiScriptLocale.GUILD_INFO_NAME,
					"children" :
					(
						{
							"name" : "GuildNameSlot",
							"type" : "image",
							"x" : 70,
							"y" : -2,
							"image" : LARGE_VALUE_FILE,
							"children" :
							(
								{"name" : "GuildNameValue", "type":"text", "text":uiScriptLocale.GUILD_INFO_NAME_VALUE, "x":0, "y":0, "all_align":"center"},
							),
						},
					),
				},

				## GuildMaster
				{
					"name" : "GuildMaster", "type" : "text", "x" : 3, "y" : 57, "text" : uiScriptLocale.GUILD_INFO_MASTER,
					"children" :
					(
						{
							"name" : "GuildMasterNameSlot",
							"type" : "image",
							"x" : 70,
							"y" : -2,
							"image" : LARGE_VALUE_FILE,
							"children" :
							(
								{"name" : "GuildMasterNameValue", "type":"text", "text":uiScriptLocale.GUILD_INFO_MASTER_VALUE, "x":0, "y":0, "all_align":"center"},
							),
						},
					),
				},

				## GuildLevel
				{
					"name" : "GuildLevel", "type" : "text", "x" : 3, "y" : 93, "text" : uiScriptLocale.GUILD_INFO_LEVEL,
					"children" :
					(
						{
							"name" : "GuildLevelSlot",
							"type" : "slotbar",
							"x" : 70,
							"y" : -2,
							"width" : 45,
							"height" : 17,
							"children" :
							(
								{"name" : "GuildLevelValue", "type":"text", "text":"30", "x":0, "y":0, "all_align":"center"},
							),
						},
					),
				},

				## CurrentExperience
				{
					"name" : "CurrentExperience", "type" : "text", "x" : 3, "y" : 119, "text" : uiScriptLocale.GUILD_INFO_CUR_EXP,
					"children" :
					(
						{
							"name" : "CurrentExperienceSlot",
							"type" : "image",
							"x" : 70,
							"y" : -2,
							"image" : LARGE_VALUE_FILE,
							"children" :
							(
								{"name" : "CurrentExperienceValue", "type":"text", "text":"10000000", "x":0, "y":0, "all_align":"center"},
							),
						},
					),
				},

				## LastExperience
				{
					"name" : "LastExperience", "type" : "text", "x" : 3, "y" : 145, "text" : uiScriptLocale.GUILD_INFO_REST_EXP,
					"children" :
					(
						{
							"name" : "LastExperienceSlot",
							"type" : "image",
							"x" : 70,
							"y" : -2,
							"image" : LARGE_VALUE_FILE,
							"children" :
							(
								{"name" : "LastExperienceValue", "type":"text", "text":"123123123123", "x":0, "y":0, "all_align":"center"},
							),
						},
					),
				},

				## GuildMemberCount
				{
					"name" : "GuildMemberCount", "type" : "text", "x" : 3, "y" : 171, "text" : uiScriptLocale.GUILD_INFO_MEMBER_NUM,
					"children" :
					(
						{
							"name" : "GuildMemberCountSlot",
							"type" : "image",
							"x" : 70,
							"y" : -2,
							"image" : LARGE_VALUE_FILE,
							"children" :
							(
								{"name" : "GuildMemberCountValue", "type":"text", "text":"30 / 32", "x":0, "y":0, "all_align":"center"},
							),
						},
					),
				},

				## GuildMemberLevelAverage
				{
					"name" : "GuildMemberLevelAverage", "type" : "text", "x" : 3, "y" : 197, "text" : uiScriptLocale.GUILD_INFO_MEMBER_AVG_LEVEL,
					"children" :
					(
						{
							"name" : "GuildMemberLevelAverageSlot",
							"type" : "image",
							"x" : 108,
							"y" : -2,
							"image" : SMALL_VALUE_FILE,
							"children" :
							(
								{"name" : "GuildMemberLevelAverageValue", "type":"text", "text":"53", "x":0, "y":0, "all_align":"center"},
							),
						},
					),
				},

			),
		},

		## Button
		{
			"name" : "OfferButton",
			"type" : "button",
			"x" : 127,
			"y" : 100,
			"text" : uiScriptLocale.GUILD_INFO_OFFER_EXP,
			"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
		},

		###############################################################################################################

		## Guild Mark Title
		{
			"name":"Guild_Mark_Title_Bar", "type":"horizontalbar", "x":188, "y":10, "width":167,
			"children" :
			(

				{ "name":"Guild_Mark_Title", "type":"text", "x":8, "y":3, "text":uiScriptLocale.GUILD_MARK, },

				## LargeGuildMark
				{
					"name" : "LargeGuildMarkSlot",
					"type" : "slotbar",
					"x" : 5,
					"y" : 24,
					"width" : 48+1,
					"height" : 36+1,
					"children" :
					(
						{
							"name" : "LargeGuildMark",
							"type" : "mark",
							"x" : 1,
							"y" : 1,
						},
					),
				},

			),
		},

		## UploadButton
		{
			"name" : "UploadGuildMarkButton",
			"type" : "button",
			"x" : 260,
			"y" : 33,
			"text" : uiScriptLocale.GUILD_INFO_UPLOAD_MARK,
			"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
		},
		{
			"name" : "UploadGuildSymbolButton",
			"type" : "button",
			"x" : 260,
			"y" : 33 + 23,
			"text" : uiScriptLocale.GUILD_INFO_UPLOAD_SYMBOL,
			"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
		},

		## Guild Mark Title
		{
			"name":"Guild_Mark_Title_Bar", "type":"horizontalbar", "x":188, "y":85, "width":167,
			"children" :
			(

				{ "name":"Guild_Mark_Title", "type":"text", "x":8, "y":3, "text":uiScriptLocale.GUILD_INFO_ENEMY_GUILD, },

				{
					"name" : "EnemyGuildSlot1",
					"type" : "image",
					"x" : 4,
					"y" : 27 + 26*0,
					"image" : XLARGE_VALUE_FILE,
					"children" :
					(
						{"name" : "EnemyGuildName1", "type":"text", "text":uiScriptLocale.GUILD_INFO_ENEMY_GUILD_EMPTY, "x":0, "y":0, "all_align":"center"},
					),
				},
				{
					"name" : "EnemyGuildSlot2",
					"type" : "image",
					"x" : 4,
					"y" : 27 + 26*1,
					"image" : XLARGE_VALUE_FILE,
					"children" :
					(
						{"name" : "EnemyGuildName2", "type":"text", "text":uiScriptLocale.GUILD_INFO_ENEMY_GUILD_EMPTY, "x":0, "y":0, "all_align":"center"},
					),
				},
				{
					"name" : "EnemyGuildSlot3",
					"type" : "image",
					"x" : 4,
					"y" : 27 + 26*2,
					"image" : XLARGE_VALUE_FILE,
					"children" :
					(
						{"name" : "EnemyGuildName3", "type":"text", "text":uiScriptLocale.GUILD_INFO_ENEMY_GUILD_EMPTY, "x":0, "y":0, "all_align":"center"},
					),
				},
				{
					"name" : "EnemyGuildSlot4",
					"type" : "image",
					"x" : 4,
					"y" : 27 + 26*3,
					"image" : XLARGE_VALUE_FILE,
					"children" :
					(
						{"name" : "EnemyGuildName4", "type":"text", "text":uiScriptLocale.GUILD_INFO_ENEMY_GUILD_EMPTY, "x":0, "y":0, "all_align":"center"},
					),
				},
				{
					"name" : "EnemyGuildSlot5",
					"type" : "image",
					"x" : 4,
					"y" : 27 + 26*4,
					"image" : XLARGE_VALUE_FILE,
					"children" :
					(
						{"name" : "EnemyGuildName5", "type":"text", "text":uiScriptLocale.GUILD_INFO_ENEMY_GUILD_EMPTY, "x":0, "y":0, "all_align":"center"},
					),
				},
				{
					"name" : "EnemyGuildSlot6",
					"type" : "image",
					"x" : 4,
					"y" : 27 + 26*5,
					"image" : XLARGE_VALUE_FILE,
					"children" :
					(
						{"name" : "EnemyGuildName6", "type":"text", "text":uiScriptLocale.GUILD_INFO_ENEMY_GUILD_EMPTY, "x":0, "y":0, "all_align":"center"},
					),
				},

			),
		},

		## CancelButtons
		{
			"name" : "EnemyGuildCancel1",
			"type" : "button",
			"x" : 310,
			"y" : 111 + 26*0,
			"text" : uiScriptLocale.CANCEL,
			"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
		},
		{
			"name" : "EnemyGuildCancel2",
			"type" : "button",
			"x" : 310,
			"y" : 111 + 26*1,
			"text" : uiScriptLocale.CANCEL,
			"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
		},
		{
			"name" : "EnemyGuildCancel3",
			"type" : "button",
			"x" : 310,
			"y" : 111 + 26*2,
			"text" : uiScriptLocale.CANCEL,
			"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
		},
		{
			"name" : "EnemyGuildCancel4",
			"type" : "button",
			"x" : 310,
			"y" : 111 + 26*3,
			"text" : uiScriptLocale.CANCEL,
			"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
		},
		{
			"name" : "EnemyGuildCancel5",
			"type" : "button",
			"x" : 310,
			"y" : 111 + 26*4,
			"text" : uiScriptLocale.CANCEL,
			"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
		},
		{
			"name" : "EnemyGuildCancel6",
			"type" : "button",
			"x" : 310,
			"y" : 111 + 26*5,
			"text" : uiScriptLocale.CANCEL,
			"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
		},

		## DeclareWar
		{
			"name" : "DeclareWarButton",
			"type" : "button",
			"x" : 250 + 15,
			"y" : 264,
			"text" : uiScriptLocale.GUILD_INFO_DECALRE_WAR,
			"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
		},
					),
				},
			),
		},
	),
}
