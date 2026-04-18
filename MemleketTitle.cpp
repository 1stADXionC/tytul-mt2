#include "stdafx.h"
#ifdef ENABLE_MEMLEKET_SYSTEM
#include "../../common/service.h"
#include "../../common/length.h"
#include "../../common/tables.h"
#include "packet.h"
#include "MemleketTitle.h"
#include "buffer_manager.h"
#include "char.h"
#include "db.h"
#include "desc.h"
#include "constants.h"

namespace
{
	const CMemleketTitle::TBonusData s_aTitleBonus[3] =
	{
		// Tytuł 0
		{
			APPLY_NORMAL_HIT_DAMAGE_BONUS, 5,
			APPLY_MAX_HP, 1000,
			APPLY_CRITICAL_PCT, 5
		},

		// Tytuł 1
		{
			APPLY_ATT_SPEED, 10,
			APPLY_MOV_SPEED, 10,
			APPLY_MAX_SP, 500
		},

		// Tytuł 2
		{
			APPLY_STR, 12,
			APPLY_DEX, 12,
			APPLY_CON, 12
		}
	};
}

auto CMemleketTitle::ClearBonusAffects(LPCHARACTER ch) -> void
{
	if (!ch)
		return;

	for (uint16_t i = AFFECT_MEMLEKET1; i <= AFFECT_MEMLEKET3; ++i)
		ch->RemoveAffect(i);
}

auto CMemleketTitle::ApplyBonusAffects(LPCHARACTER ch, int8_t bonusIdx) -> void
{
	if (!ch)
		return;

	if (bonusIdx < 0 || bonusIdx > 2)
		return;

	const TBonusData& bonus = s_aTitleBonus[bonusIdx];

	ch->AddAffect(
		AFFECT_MEMLEKET1,
		aApplyInfo[bonus.applyType1].bPointType,
		bonus.applyValue1,
		0,
		INFINITE_AFFECT_DURATION,
		0,
		false
	);

	ch->AddAffect(
		AFFECT_MEMLEKET2,
		aApplyInfo[bonus.applyType2].bPointType,
		bonus.applyValue2,
		0,
		INFINITE_AFFECT_DURATION,
		0,
		false
	);

	ch->AddAffect(
		AFFECT_MEMLEKET3,
		aApplyInfo[bonus.applyType3].bPointType,
		bonus.applyValue3,
		0,
		INFINITE_AFFECT_DURATION,
		0,
		false
	);
}

auto CMemleketTitle::SelectTitle(const int8_t titleIDX, LPCHARACTER ch) -> void
{
	if (!ch || !ch->GetDesc())
		return;

	if (titleIDX < -1 || titleIDX > 2)
		return;

	UpdateTitle(ch, titleIDX);
	SendToClient(ch);
}

auto CMemleketTitle::SelectBonus(const int8_t titleIDX, LPCHARACTER ch) -> void
{
	if (!ch || !ch->GetDesc())
		return;

	if (titleIDX < -1 || titleIDX > 2)
		return;

	UpdateBonus(ch, titleIDX);
	SendToClient(ch);
}

auto CMemleketTitle::UpdateTitle(LPCHARACTER ch, const int8_t changeIdx) -> void
{
	if (!ch || !ch->GetDesc())
		return;

	if (changeIdx < -1 || changeIdx > 2)
		return;

	ch->SetMemleket(changeIdx);
}

auto CMemleketTitle::UpdateBonus(LPCHARACTER ch, const int8_t changeIdx) -> void
{
	if (!ch || !ch->GetDesc())
		return;

	if (changeIdx < -1 || changeIdx > 2)
		return;

	ClearBonusAffects(ch);
	ch->SetMemleketBonus(changeIdx);

	if (changeIdx == -1)
	{
		ch->ComputePoints();
		ch->PointsPacket();
		return;
	}

	ApplyBonusAffects(ch, changeIdx);

	ch->ComputePoints();
	ch->PointsPacket();
}

auto CMemleketTitle::SendToClient(LPCHARACTER ch) -> void
{
	if (!ch || !ch->GetDesc())
		return;

	TPacketGCMemleketInfo titleInfo{};
	titleInfo.bHeader = HEADER_GC_MEMLEKET;
	titleInfo.bTitle = ch->GetMemleket();
	titleInfo.bBonus = ch->GetMemleketBonus();

	ch->GetDesc()->Packet(&titleInfo, sizeof(TPacketGCMemleketInfo));
}

#endif