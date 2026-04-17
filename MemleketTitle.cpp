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

auto CMemleketTitle::SelectTitle(const int8_t titleIDX, LPCHARACTER ch) -> void {
    if (!ch || !ch->GetDesc()) { 
        return; 
    }

    if (titleIDX < -1) {
        return;
    }

    if (ch->GetMemleket() == titleIDX) {
        ch->ChatPacket(CHAT_TYPE_INFO, "Już masz ten tytuł!");
        return;
    }

    UpdateTitle(ch, titleIDX);
}

auto CMemleketTitle::UpdateTitle(LPCHARACTER ch, const int8_t changeIdx) -> void {
    if (!ch || !ch->GetDesc()) {
        return;
    }

    for (uint16_t i = AFFECT_MEMLEKET1; i <= AFFECT_MEMLEKET3; ++i) {
        ch->RemoveAffect(i);
    }

    if (changeIdx == -1) {
        ch->SetMemleket(-1);
        ch->ComputePoints();
        ch->PointsPacket();
        return;
    }

    if (changeIdx < 0) {
        return;
    }

    int titleStep = changeIdx;

    int srednie = titleStep;      
    int hp      = titleStep * 100; 
    int krytyk  = titleStep;      

    ch->AddAffect(
        AFFECT_MEMLEKET1,
        aApplyInfo[APPLY_NORMAL_HIT_DAMAGE_BONUS].bPointType,
        srednie,
        0,
        INFINITE_AFFECT_DURATION,
        0,
        false
    );

    ch->AddAffect(
        AFFECT_MEMLEKET2,
        aApplyInfo[APPLY_MAX_HP].bPointType,
        hp,
        0,
        INFINITE_AFFECT_DURATION,
        0,
        false
    );

    ch->AddAffect(
        AFFECT_MEMLEKET3,
        aApplyInfo[APPLY_CRITICAL_PCT].bPointType,
        krytyk,
        0,
        INFINITE_AFFECT_DURATION,
        0,
        false
    );

    ch->SetMemleket(changeIdx);
    ch->ComputePoints();
    ch->PointsPacket();
}

auto CMemleketTitle::SendToClient(LPCHARACTER ch) -> void {
    if (!ch || !ch->GetDesc()) {
        return;
    }

    TPacketGCMemleketInfo titleInfo{};
    ch->GetDesc()->Packet(&titleInfo, sizeof(TPacketGCMemleketInfo));
}

#endif

