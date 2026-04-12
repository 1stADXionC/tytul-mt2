#pragma once
class CMemleketTitle : public singleton<CMemleketTitle>
{
public:
    CMemleketTitle() = default;
    ~CMemleketTitle() = default;
    auto    SelectTitle(int8_t titleIDX, LPCHARACTER ch) -> void;
    auto    UpdateTitle( LPCHARACTER ch, int8_t changeIdx = -1) -> void;
    auto    SendToClient(LPCHARACTER ch) -> void;
};