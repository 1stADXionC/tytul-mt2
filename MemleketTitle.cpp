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

static std::map<uint8_t, uint16_t> affMap = 
{
    { APPLY_MAX_HP, 100 },
    { APPLY_STEAL_HP, 10 },
    { APPLY_STEAL_SP, 10 }
};

static std::vector<std::pair<uint32_t, uint8_t>> itemList = 
{
    {70251, 1},
    {70252, 1},
    {70253, 1}
};

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

    if (changeIdx == -1) {
        for (uint16_t i = AFFECT_MEMLEKET1; i <= AFFECT_MEMLEKET3; ++i) {
            ch->RemoveAffect(i);
        }

        ch->SetMemleket(-1);
        ch->ComputePoints();
        ch->PointsPacket();
        ch->ChatPacket(CHAT_TYPE_INFO, "Tytuł wyłączony.");
        return;
    }

    bool checkItems = true;
    for (const auto& i : itemList) {
        if (ch->CountSpecifyItem(i.first) < i.second) {
            checkItems = false;
            break;
        }
    }

    if (!checkItems) {
        ch->ChatPacket(CHAT_TYPE_INFO, "Nie masz wymaganych przedmiotów.");
        return;
    }

    for (uint16_t i = AFFECT_MEMLEKET1; i <= AFFECT_MEMLEKET3; ++i) {
        ch->RemoveAffect(i);
    }

    for (const auto& i : itemList) {
        ch->RemoveSpecifyItem(i.first, i.second);
    }

    uint8_t idx = 0;
    for (const auto& i : affMap) {
        ch->AddAffect(
            AFFECT_MEMLEKET1 + idx++,
            aApplyInfo[i.first].bPointType,
            i.second,
            0,
            INFINITE_AFFECT_DURATION,
            0,
            false
        );
    }

    ch->SetMemleket(changeIdx);
    ch->ComputePoints();
    ch->PointsPacket();
    ch->ChatPacket(CHAT_TYPE_INFO, "Tytuł został zmieniony.");
}

auto CMemleketTitle::SendToClient(LPCHARACTER ch) -> void {
    if (!ch || !ch->GetDesc()) { return; }

    TPacketGCMemleketInfo titleInfo{};
    BYTE idx = 0;
    for (const auto& j : itemList) {
        titleInfo.dwVnum[idx] = j.first;
        titleInfo.dwCount[idx] = j.second;
        ++idx;
    }
    idx = 0;
    for (const auto& j : affMap) {
        titleInfo.wAffType[idx] = j.first;
        titleInfo.bAffValue[idx] = j.second;
        ++idx;
    }
    ch->GetDesc()->Packet(&titleInfo, sizeof(TPacketGCMemleketInfo));
}

#endif

