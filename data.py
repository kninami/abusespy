CRITERIA = [
    {"id": "R-001", "category": "신고(Reporting)",       "question": "피해자가 신고할 수 있는 공식 채널이 있습니까?"},
    {"id": "R-002", "category": "신고(Reporting)",       "question": "신고 절차가 공개되어 있습니까?"},
    {"id": "R-003", "category": "신고(Reporting)",       "question": "신고 결과를 통보합니까?"},
    {"id": "V-001", "category": "피해자보호(Victim)",    "question": "계정 차단 기능이 있습니까?"},
    {"id": "V-002", "category": "피해자보호(Victim)",    "question": "특정 사용자의 연락을 제한할 수 있습니까?"},
    {"id": "V-003", "category": "피해자보호(Victim)",    "question": "증거 보존 방법을 제공합니까?"},
    {"id": "V-004", "category": "피해자보호(Victim)",    "question": "피해자 지원 기관 정보를 제공합니까?"},
    {"id": "T-001", "category": "투명성(Transparency)",  "question": "신고 처리 기간이 공개되어 있습니까?"},
    {"id": "T-002", "category": "투명성(Transparency)",  "question": "연례 투명성 보고서를 발행합니까?"},
    {"id": "T-003", "category": "투명성(Transparency)",  "question": "콘텐츠 삭제 기준이 공개되어 있습니까?"},
    {"id": "E-001", "category": "집행(Enforcement)",     "question": "반복 가해자 정책이 있습니까?"},
    {"id": "E-002", "category": "집행(Enforcement)",     "question": "계정 정지 기준이 공개되어 있습니까?"},
    {"id": "E-003", "category": "집행(Enforcement)",     "question": "재가입 방지 정책이 있습니까?"},
    {"id": "H-001", "category": "유해행위(Harm)",        "question": "스토킹 관련 정책이 있습니까?"},
    {"id": "H-002", "category": "유해행위(Harm)",        "question": "비동의 이미지 유포 정책이 있습니까?"},
    {"id": "H-003", "category": "유해행위(Harm)",        "question": "아동 대상 피해 정책이 있습니까?"},
    {"id": "H-004", "category": "유해행위(Harm)",        "question": "신변 위협 대응 절차가 있습니까?"},
]

PLATFORMS = {
    "instagram": {
        "name": "Instagram",
        "color": "#E1306C",
        "emoji": "📸",
        "description": "Meta가 운영하는 사진·동영상 공유 소셜 미디어 플랫폼",
    },
    "x": {
        "name": "X (Twitter)",
        "color": "#000000",
        "emoji": "𝕏",
        "description": "Elon Musk가 인수 후 리브랜딩한 마이크로블로깅 소셜 네트워크",
    },
    "discord": {
        "name": "Discord",
        "color": "#5865F2",
        "emoji": "🎮",
        "description": "커뮤니티와 게이머를 위한 음성·채팅 메시징 플랫폼",
    },
    "telegram": {
        "name": "Telegram",
        "color": "#26A5E4",
        "emoji": "✈️",
        "description": "보안과 속도에 중점을 둔 클라우드 기반 메시징 플랫폼",
    },
}

JUDGEMENTS = [
    # ── R-001 ────────────────────────────────────────────────────────────────
    {"criterion_id": "R-001", "service": "telegram",  "verdict": "unclear",
     "evidence_summary": "수신자가 메시지를 신고했다는 표현은 있으나 공식 신고 채널은 명시되지 않음",
     "evidence_quotes": "피싱, 스팸 및 기타 악용 사례와 텔레그램 서비스 약관 위반을 방지하기 위해, 운영진은 수신자가 신고한 메시지를 확인할 수 있습니다.",
     "sources": "safety.html"},
    {"criterion_id": "R-001", "service": "x",         "verdict": "yes",
     "evidence_summary": "개별 게시물, 리스트, 프로필에서 직접 신고할 수 있는 공식 신고 채널이 명시되어 있음",
     "evidence_quotes": "스팸, 가학적이거나 유해한 내용, 부적절한 광고, 자해 및 사칭 등의 특정 위반 사항이 있는 경우 개별 게시물, 리스트 또는 프로필에서 직접 신고할 수 있습니다.",
     "sources": "reporting.html"},
    {"criterion_id": "R-001", "service": "discord",   "verdict": "yes",
     "evidence_summary": "Discord에 계정, 서버 또는 콘텐츠 위반을 신고하라는 공식 안내가 있음",
     "evidence_quotes": "지침을 위반한 것으로 보이는 계정, 서버 또는 콘텐츠를 발견할 경우, 저희에게 신고해주세요.",
     "sources": "Community-Guidelines.html / reporting.html"},
    {"criterion_id": "R-001", "service": "instagram", "verdict": "yes",
     "evidence_summary": "내장 신고 옵션이 공식 신고 채널로 명시돼 있다",
     "evidence_quotes": "If you see something that you think may violate any of our guidelines, please help us by using our built-in reporting option.",
     "sources": "Instagram Community Guidelines FAQs.html"},

    # ── R-002 ────────────────────────────────────────────────────────────────
    {"criterion_id": "R-002", "service": "telegram",  "verdict": "no",
     "evidence_summary": "관련 조항 발견 불가", "evidence_quotes": "", "sources": ""},
    {"criterion_id": "R-002", "service": "x",         "verdict": "yes",
     "evidence_summary": "프로필 신고 절차의 단계가 공개되어 있음",
     "evidence_quotes": "신고하려는 프로필을 엽니다. 더 보기 아이콘을 선택합니다. 신고를 선택한 후 신고할 규정 위반 유형을 선택합니다.",
     "sources": "reporting.html"},
    {"criterion_id": "R-002", "service": "discord",   "verdict": "yes",
     "evidence_summary": "메시지 신고를 시작하는 구체적 절차가 공개되어 있음",
     "evidence_quotes": "신고하려는 메시지를 선택하세요. 모바일에서는 메시지를 길게 터치하고 데스크톱에서는 마우스 오른쪽 버튼을 클릭하세요.",
     "sources": "reporting.html"},
    {"criterion_id": "R-002", "service": "instagram", "verdict": "yes",
     "evidence_summary": "게시물·메시지·계정 신고 방법이 구체적으로 공개돼 있다",
     "evidence_quotes": "You can report individual pieces of content to us by tapping the three dots above a post, holding on a message, or by visiting an account.",
     "sources": "Instagram Account Safety.html"},

    # ── R-003 ────────────────────────────────────────────────────────────────
    {"criterion_id": "R-003", "service": "telegram",  "verdict": "no",
     "evidence_summary": "관련 조항 발견 불가", "evidence_quotes": "", "sources": ""},
    {"criterion_id": "R-003", "service": "x",         "verdict": "unclear",
     "evidence_summary": "후속 조치 이메일 및 알림은 명시되어 있으나 신고 결과 통보 여부로 직접 판단하기는 어려움",
     "evidence_quotes": "X에서 신고자에게 보내는 후속 조치 이메일 및 알림에 신고한 게시물 텍스트가 포함됩니다.",
     "sources": "reporting.html"},
    {"criterion_id": "R-003", "service": "discord",   "verdict": "yes",
     "evidence_summary": "신고 접수 사실을 시스템 DM이나 이메일로 알린다고 명시함",
     "evidence_quotes": "신고를 제출하면 신고가 접수되었음을 알리는 시스템 DM이나 이메일을 보내드립니다. 신고 결과 정책 위반이 확인되면 알려드립니다.",
     "sources": "reporting.html"},
    {"criterion_id": "R-003", "service": "instagram", "verdict": "no",
     "evidence_summary": "근거 없음", "evidence_quotes": "", "sources": ""},

    # ── V-001 ────────────────────────────────────────────────────────────────
    {"criterion_id": "V-001", "service": "telegram",  "verdict": "no",
     "evidence_summary": "피해자가 사용할 수 있는 계정 차단 기능에 대한 명시 조항 발견 불가",
     "evidence_quotes": "", "sources": ""},
    {"criterion_id": "V-001", "service": "x",         "verdict": "no",
     "evidence_summary": "근거 없음", "evidence_quotes": "", "sources": ""},
    {"criterion_id": "V-001", "service": "discord",   "verdict": "yes",
     "evidence_summary": "사용자를 무시하거나 차단할 수 있다고 명시함",
     "evidence_quotes": "언제든지 상호작용을 제한하거나 더 이상 상호작용하고 싶지 않은 사용자를 무시하거나 차단할 수 있다는 점도 기억하세요.",
     "sources": "reporting.html"},
    {"criterion_id": "V-001", "service": "instagram", "verdict": "no",
     "evidence_summary": "근거 없음", "evidence_quotes": "", "sources": ""},

    # ── V-002 ────────────────────────────────────────────────────────────────
    {"criterion_id": "V-002", "service": "telegram",  "verdict": "unclear",
     "evidence_summary": "계정의 연락 제한 조치는 명시되어 있으나 피해자가 직접 제한할 수 있는 기능인지 불분명함",
     "evidence_quotes": "사용자가 보낸 메시지에 대한 스팸 신고가 운영진에 의해 확인될 경우, 해당 계정은 일시적 또는 영구적으로 타인과의 연락이 제한될 수 있습니다.",
     "sources": "safety.html"},
    {"criterion_id": "V-002", "service": "x",         "verdict": "no",
     "evidence_summary": "근거 없음", "evidence_quotes": "", "sources": ""},
    {"criterion_id": "V-002", "service": "discord",   "verdict": "yes",
     "evidence_summary": "상호작용 제한, 무시, 차단 기능을 안내함",
     "evidence_quotes": "언제든지 상호작용을 제한하거나 더 이상 상호작용하고 싶지 않은 사용자를 무시하거나 차단할 수 있다는 점도 기억하세요.",
     "sources": "reporting.html"},
    {"criterion_id": "V-002", "service": "instagram", "verdict": "yes",
     "evidence_summary": "메시지를 보낼 수 있는 상대를 제한하는 정책이 명시돼 있다",
     "evidence_quotes": "Messaging restrictions: Teens will be placed in the strictest messaging settings, so they can only be messaged by people they follow or are already connected to.",
     "sources": "Teen Accounts.html"},

    # ── V-003 ────────────────────────────────────────────────────────────────
    {"criterion_id": "V-003", "service": "telegram",  "verdict": "no",
     "evidence_summary": "관련 조항 발견 불가", "evidence_quotes": "", "sources": ""},
    {"criterion_id": "V-003", "service": "x",         "verdict": "no",
     "evidence_summary": "근거 없음", "evidence_quotes": "", "sources": ""},
    {"criterion_id": "V-003", "service": "discord",   "verdict": "unclear",
     "evidence_summary": "메시지 URL 확인 방법은 있으나 증거 보존 방법으로 명시되어 있는지는 판단 불가",
     "evidence_quotes": "EU 디지털 서비스법에 따라 메시지를 신고하는 경우, 메시지 URL이 요구됩니다. 메시지 URL이 귀하의 장치의 클립보드에 복사될 것입니다.",
     "sources": "reporting.html"},
    {"criterion_id": "V-003", "service": "instagram", "verdict": "no",
     "evidence_summary": "근거 없음", "evidence_quotes": "", "sources": ""},

    # ── V-004 ────────────────────────────────────────────────────────────────
    {"criterion_id": "V-004", "service": "telegram",  "verdict": "no",
     "evidence_summary": "관련 조항 발견 불가", "evidence_quotes": "", "sources": ""},
    {"criterion_id": "V-004", "service": "x",         "verdict": "yes",
     "evidence_summary": "아동 성 착취 관련 외부 신고 기관 정보가 제공됨",
     "evidence_quotes": "아동 성 착취 자료를 배포하거나 이를 조장하는 콘텐츠를 다른 인터넷 사이트에서 발견할 경우 NCMEC 또는 지역 경찰서로 신고하세요.",
     "sources": "safety.html"},
    {"criterion_id": "V-004", "service": "discord",   "verdict": "yes",
     "evidence_summary": "위기 상황 지원 기관인 Crisis Text Line 연락 방법을 제공함",
     "evidence_quotes": "미국에 거주하는 경우, 741741번으로 DISCORD란 문자를 보내 Crisis Text Line에 연락하면 자원봉사 위기상담사가 도와드릴 것입니다.",
     "sources": "reporting.html"},
    {"criterion_id": "V-004", "service": "instagram", "verdict": "yes",
     "evidence_summary": "지원 기관에 연락하라고 안내하며 국가별 지원 기관 목록을 실제 기관명과 함께 제공한다",
     "evidence_quotes": "If you or someone you love is going through a difficult time, please contact an organization that can provide the support you need.",
     "sources": "Instagram Account Safety.html"},

    # ── T-001 ────────────────────────────────────────────────────────────────
    {"criterion_id": "T-001", "service": "telegram",  "verdict": "no",
     "evidence_summary": "관련 조항 발견 불가", "evidence_quotes": "", "sources": ""},
    {"criterion_id": "T-001", "service": "x",         "verdict": "yes",
     "evidence_summary": "신고 승인 및 해결에 걸릴 수 있는 기간이 공개되어 있음",
     "evidence_quotes": "X는 24시간 이내에 올바른 방식으로 제출된 신고를 승인합니다. 신고는 일반적으로 며칠 내에 해소되지만 최대 30일이 걸릴 수 있습니다.",
     "sources": "reporting.html"},
    {"criterion_id": "T-001", "service": "discord",   "verdict": "yes",
     "evidence_summary": "고위험 신고 24~48시간, 저위험 신고 일주일 이내 목표 검토 기간을 공개함",
     "evidence_quotes": "높은 수준의 피해 신고: Discord는 24시간에서 48시간 이내에 검토하는 것을 목표로 합니다. 낮은 수준의 피해 신고: Discord는 이 카테고리의 신고를 일주일 이내에 검토하는 것을 목표로 합니다.",
     "sources": "reporting.html"},
    {"criterion_id": "T-001", "service": "instagram", "verdict": "unclear",
     "evidence_summary": "상시 검토 체계는 명시하지만 개별 신고의 처리 기간은 명시하지 않아 판단 불가",
     "evidence_quotes": "These teams are based in locations worldwide in order to give coverage to reports 24 hours a day, seven days a week.",
     "sources": "Instagram Community Guidelines FAQs.html"},

    # ── T-002 ────────────────────────────────────────────────────────────────
    {"criterion_id": "T-002", "service": "telegram",  "verdict": "unclear",
     "evidence_summary": "분기별 투명성 보고서는 명시되어 있으나 연례 보고서 발행 여부는 명시되지 않음",
     "evidence_quotes": "데이터가 공유되는 경우, 해당 내용은 분기별 투명성 보고서에 포함되어 게시됩니다.",
     "sources": "safety.html"},
    {"criterion_id": "T-002", "service": "x",         "verdict": "no",
     "evidence_summary": "근거 없음", "evidence_quotes": "", "sources": ""},
    {"criterion_id": "T-002", "service": "discord",   "verdict": "yes",
     "evidence_summary": "투명성 보고서에서 신고 및 조치 세부 내용을 확인할 수 있다고 명시함",
     "evidence_quotes": "접수된 신고와 커뮤니티 지침 또는 서비스 약관 위반에 대한 조치의 세부 내용은 투명성 보고서에서 확인할 수 있습니다.",
     "sources": "reporting.html / transparency Report.pdf"},
    {"criterion_id": "T-002", "service": "instagram", "verdict": "no",
     "evidence_summary": "근거 없음", "evidence_quotes": "", "sources": ""},

    # ── T-003 ────────────────────────────────────────────────────────────────
    {"criterion_id": "T-003", "service": "telegram",  "verdict": "unclear",
     "evidence_summary": "금지 콘텐츠 기준은 명시되어 있으나 삭제 기준으로 직접 명시되어 있는지는 불분명함",
     "evidence_quotes": "공개적으로 볼 수 있는 텔레그램 채널, 봇 등을 통해 폭력을 조장하는 행위.",
     "sources": "service-guidelines.html"},
    {"criterion_id": "T-003", "service": "x",         "verdict": "yes",
     "evidence_summary": "콘텐츠 제한 기준 및 삭제 사유가 약관에 공개되어 있음",
     "evidence_quotes": "당사는 저작권, 상표권 침해 혐의가 있거나 사칭, 위법한 행위 또는 가학적 내용 등 이용자 계약을 위반하는 콘텐츠를 삭제할 수 있는 권리가 있습니다.",
     "sources": "community-guidelines.html / terms.html"},
    {"criterion_id": "T-003", "service": "discord",   "verdict": "yes",
     "evidence_summary": "위반 발견 시 콘텐츠 삭제 등 집행 조치를 취할 수 있다고 명시함",
     "evidence_quotes": "When we proactively or reactively discover a violation of these Guidelines, we may take a number of enforcement steps based on the severity of the violation, including issuing warnings, removing content.",
     "sources": "Community-Guidelines.html"},
    {"criterion_id": "T-003", "service": "instagram", "verdict": "yes",
     "evidence_summary": "허용·비허용 콘텐츠 기준이 공개돼 있으며, 위반 시 게시물을 제거한다는 기준이 공개돼 있다",
     "evidence_quotes": "It is our policy to remove content that violates our community guidelines. We may remove entire posts if either the imagery or associated captions violate our guidelines.",
     "sources": "Instagram Community Guidelines FAQs.html"},

    # ── E-001 ────────────────────────────────────────────────────────────────
    {"criterion_id": "E-001", "service": "telegram",  "verdict": "no",
     "evidence_summary": "반복 가해자에 대한 별도 정책 발견 불가", "evidence_quotes": "", "sources": ""},
    {"criterion_id": "E-001", "service": "x",         "verdict": "yes",
     "evidence_summary": "상습적 운영원칙 위반자의 신규 계정 생성을 방지하는 정책이 명시되어 있음",
     "evidence_quotes": "당사의 운영원칙을 위반하여 귀하의 계정이 정지된 경우, 당사는 상습적 운영원칙 위반자가 신규 계정을 생성하는 것을 방지하기 위하여 식별 정보를 무기한 보관할 수 있습니다.",
     "sources": "privacy.html"},
    {"criterion_id": "E-001", "service": "discord",   "verdict": "unclear",
     "evidence_summary": "재범 감소를 언급하지만 반복 가해자 정책의 구체 기준으로 직접 제시되지는 않음",
     "evidence_quotes": "Prevention: how we work to reduce escalation and recidivism over time.",
     "sources": "transparency Report.pdf"},
    {"criterion_id": "E-001", "service": "instagram", "verdict": "no",
     "evidence_summary": "근거 없음", "evidence_quotes": "", "sources": ""},

    # ── E-002 ────────────────────────────────────────────────────────────────
    {"criterion_id": "E-002", "service": "telegram",  "verdict": "yes",
     "evidence_summary": "심각한 위반 시 계정 차단 가능성이 명시되어 있음",
     "evidence_quotes": "더욱 심각한 위반의 경우, 계정이 차단될 수 있습니다. 텔레그램 서비스 약관을 준수하지 않을 경우 텔레그램 또는 일부 서비스 이용이 일시적 또는 영구적으로 제한될 수 있습니다.",
     "sources": "safety.html / service-guidelines.html"},
    {"criterion_id": "E-002", "service": "x",         "verdict": "yes",
     "evidence_summary": "계정 정지 또는 해지 기준이 공개되어 있음",
     "evidence_quotes": "당사의 합리적인 소견으로 볼 때 귀하가 본 약관을 위반한 것으로 판단될 경우, 당사는 언제든지 귀하의 계정을 정지 또는 해지하거나 서비스 제공을 중단할 수 있습니다.",
     "sources": "terms.html"},
    {"criterion_id": "E-002", "service": "discord",   "verdict": "yes",
     "evidence_summary": "위반 심각도에 따라 계정 접근 임시 정지 또는 계정 영구 제거가 가능하다고 명시함",
     "evidence_quotes": "When we proactively or reactively discover a violation of these Guidelines, we may take a number of enforcement steps including issuing warnings, removing content, temporarily suspending account access to Discord, or permanently removing violative accounts.",
     "sources": "Community-Guidelines.html"},
    {"criterion_id": "E-002", "service": "instagram", "verdict": "yes",
     "evidence_summary": "커뮤니티 가이드라인 위반 시 계정을 비활성화할 수 있다고 명시한다",
     "evidence_quotes": "We also may disable entire accounts for violations of our Community Guidelines. Our team works 24/7 to review and remove content and accounts that go against our Community Guidelines.",
     "sources": "Instagram Community Guidelines FAQs.html"},

    # ── E-003 ────────────────────────────────────────────────────────────────
    {"criterion_id": "E-003", "service": "telegram",  "verdict": "no",
     "evidence_summary": "관련 조항 발견 불가", "evidence_quotes": "", "sources": ""},
    {"criterion_id": "E-003", "service": "x",         "verdict": "yes",
     "evidence_summary": "아동 성 착취 정책 위반자의 신규 계정 생성 금지 및 정지 계정 식별 정보 보관이 명시되어 있음",
     "evidence_quotes": "대부분의 경우, 트위터의 아동 성 착취 관련 정책을 위반한 계정은 즉시 영구 정지됩니다. 그에 더하여 정책 위반자는 추후 신규 계정 생성 또한 금지됩니다.",
     "sources": "safety.html / privacy.html"},
    {"criterion_id": "E-003", "service": "discord",   "verdict": "yes",
     "evidence_summary": "영구 집행 조치 이후 새 계정이나 커뮤니티 생성을 통한 회피를 금지함",
     "evidence_quotes": "Discord에서 진행하는 영구적 집행 조치를 회피하지 마세요. 여기에는 Discord의 플랫폼 규정을 위반하여 제거된 후 새로운 계정 또는 커뮤니티를 생성하거나 기존 계정 또는 커뮤니티를 사용하는 행위가 포함됩니다.",
     "sources": "Community-Guidelines.html"},
    {"criterion_id": "E-003", "service": "instagram", "verdict": "no",
     "evidence_summary": "근거 없음", "evidence_quotes": "", "sources": ""},

    # ── H-001 ────────────────────────────────────────────────────────────────
    {"criterion_id": "H-001", "service": "telegram",  "verdict": "no",
     "evidence_summary": "스토킹 관련 명시 조항 발견 불가", "evidence_quotes": "", "sources": ""},
    {"criterion_id": "H-001", "service": "x",         "verdict": "unclear",
     "evidence_summary": "특정인을 대상으로 한 학대 금지는 있으나 스토킹 정책으로 명시되어 있지는 않음",
     "evidence_quotes": "폭력/학대: 가학적인 콘텐츠를 공유하거나, 특정인을 대상으로 한 학대에 관여하거나, 타인에게 학대를 선동하는 행위는 허용되지 않습니다.",
     "sources": "community-guidelines.html"},
    {"criterion_id": "H-001", "service": "discord",   "verdict": "unclear",
     "evidence_summary": "괴롭힘 금지 조항은 있으나 스토킹 관련 정책으로 명시되어 있는지는 판단 불가",
     "evidence_quotes": "괴롭힘을 조장하거나, 조직하거나, 가담하지 마세요. 성희롱, 밴 또는 차단 회피 등 어떠한 형태의 괴롭힘도 허용되지 않습니다.",
     "sources": "Community-Guidelines.html"},
    {"criterion_id": "H-001", "service": "instagram", "verdict": "unclear",
     "evidence_summary": "괴롭힘성 연락 금지 조항은 있으나 스토킹 정책으로 직접 명시되지는 않아 판단 불가",
     "evidence_quotes": "Spam – This is not allowed on Instagram (creating or submitting unwanted email, comments, likes or other forms of commercial or harassing communications).",
     "sources": "Instagram Community Guidelines FAQs.html"},

    # ── H-002 ────────────────────────────────────────────────────────────────
    {"criterion_id": "H-002", "service": "telegram",  "verdict": "unclear",
     "evidence_summary": "불법 음란물 게시 금지는 있으나 비동의 이미지 유포 정책으로 직접 명시되어 있지는 않음",
     "evidence_quotes": "공개적으로 볼 수 있는 텔레그램 채널, 봇 등에 불법적인 음란물을 게시하지 마십시오.",
     "sources": "service-guidelines.html"},
    {"criterion_id": "H-002", "service": "x",         "verdict": "yes",
     "evidence_summary": "동의 없이 제작 또는 배포된 사적인 사진과 동영상 게시 및 공유 금지가 명시되어 있음",
     "evidence_quotes": "동의를 얻지 않은 신체 노출: 동의 없이 제작 또는 배포된 타인의 사적인 사진 또는 동영상을 게시하거나 공유해서는 안 됩니다.",
     "sources": "community-guidelines.html"},
    {"criterion_id": "H-002", "service": "discord",   "verdict": "yes",
     "evidence_summary": "동의 없는 성적 콘텐츠 공유·배포를 금지하며 NCII를 엄격히 금지하고 제거 노력한다고 명시함",
     "evidence_quotes": "만 18세 이상의 다른 사람에 대한 성적으로 노골적이거나 선정적인 콘텐츠를 당사자의 명시적 동의 없이 공유, 배포 또는 제작해서는 안 됩니다. Discord strictly prohibits NCII.",
     "sources": "Community-Guidelines.html / transparency Report.pdf"},
    {"criterion_id": "H-002", "service": "instagram", "verdict": "no",
     "evidence_summary": "근거 없음", "evidence_quotes": "", "sources": ""},

    # ── H-003 ────────────────────────────────────────────────────────────────
    {"criterion_id": "H-003", "service": "telegram",  "verdict": "yes",
     "evidence_summary": "아동 학대가 금지되는 불법 활동 예시로 명시되어 있음",
     "evidence_quotes": "대부분의 국가에서 불법으로 간주되는 활동에 참여하는 것. 여기에는 아동 학대, 불법 상품 및 서비스의 판매 또는 제공 등이 포함됩니다.",
     "sources": "service-guidelines.html"},
    {"criterion_id": "H-003", "service": "x",         "verdict": "yes",
     "evidence_summary": "아동 성 착취에 대한 무관용 정책이 명시되어 있음",
     "evidence_quotes": "트위터에서는 아동 성 착취 행위와 관련하여 무관용 정책을 고수합니다.",
     "sources": "safety.html"},
    {"criterion_id": "H-003", "service": "discord",   "verdict": "yes",
     "evidence_summary": "아동 성학대를 묘사·조장·정상화하는 콘텐츠 제작·게시·공유를 금지함",
     "evidence_quotes": "Do not create, post, solicit, share, or make attempts to distribute content on Discord that depicts, promotes, or attempts to normalize child sexual abuse.",
     "sources": "Community-Guidelines.html"},
    {"criterion_id": "H-003", "service": "instagram", "verdict": "yes",
     "evidence_summary": "청소년 계정에 자동 보호 설정을 적용하는 별도 정책이 명시돼 있다",
     "evidence_quotes": "We're introducing Instagram Teen Accounts to reassure parents that teens are having safe experiences with built-in protections on automatically.",
     "sources": "Teen Accounts.html"},

    # ── H-004 ────────────────────────────────────────────────────────────────
    {"criterion_id": "H-004", "service": "telegram",  "verdict": "unclear",
     "evidence_summary": "폭력 조장 금지는 있으나 신변 위협 대응 절차는 명시되어 있지 않음",
     "evidence_quotes": "공개적으로 볼 수 있는 텔레그램 채널, 봇 등을 통해 폭력을 조장하는 행위.",
     "sources": "service-guidelines.html"},
    {"criterion_id": "H-004", "service": "x",         "verdict": "yes",
     "evidence_summary": "폭력적인 위협을 신고할 수 있는 절차와 위해 위협 금지가 명시되어 있음",
     "evidence_quotes": "폭력적인 발언: 폭력 행위나 위해를 위협하거나 선동하거나 미화하거나 이에 대한 욕구를 표출해서는 안 됩니다.",
     "sources": "reporting.html / community-guidelines.html"},
    {"criterion_id": "H-004", "service": "discord",   "verdict": "yes",
     "evidence_summary": "실현 가능한 폭력 위협 시 현지 법 집행기관 연락 안내와 위해 위협 금지가 명시됨",
     "evidence_quotes": "실현 가능한 폭력 위협을 받고 있으며 본인 또는 다른 사람이 즉각적인 위험에 처해 있는 경우, 현지 법 집행기관에 연락하세요.",
     "sources": "reporting.html / Community-Guidelines.html"},
    {"criterion_id": "H-004", "service": "instagram", "verdict": "yes",
     "evidence_summary": "즉각적인 신체적 위험 시 현지 법집행기관 연락 안내와 협력 방침이 명시된다",
     "evidence_quotes": "If someone you know is in immediate physical danger, please contact local law enforcement. We may work with law enforcement, including when we believe that there's risk of physical harm or threat to public safety.",
     "sources": "Instagram Account Safety.html"},
]


def compute_score(service: str) -> float:
    """Return score 0‑10 (yes=1, unclear=0.5, no=0)."""
    weights = {"yes": 1.0, "unclear": 0.5, "no": 0.0}
    entries = [j for j in JUDGEMENTS if j["service"] == service]
    if not entries:
        return 0.0
    total = sum(weights.get(j["verdict"], 0.0) for j in entries)
    return round(total / len(entries) * 10, 1)


def get_platform_data(service: str) -> dict:
    """Return full platform dict with judgements indexed by criterion_id."""
    platform = PLATFORMS[service].copy()
    platform["service"] = service
    platform["score"] = compute_score(service)
    judgements = {j["criterion_id"]: j for j in JUDGEMENTS if j["service"] == service}
    platform["judgements"] = judgements
    return platform


def get_category_scores(service: str) -> dict:
    """Return per-category score dict."""
    weights = {"yes": 1.0, "unclear": 0.5, "no": 0.0}
    categories: dict[str, list[float]] = {}
    for j in JUDGEMENTS:
        if j["service"] != service:
            continue
        criterion = next((c for c in CRITERIA if c["id"] == j["criterion_id"]), None)
        if not criterion:
            continue
        cat = criterion["category"]
        categories.setdefault(cat, []).append(weights.get(j["verdict"], 0.0))
    return {cat: round(sum(v) / len(v) * 10, 1) for cat, v in categories.items()}
