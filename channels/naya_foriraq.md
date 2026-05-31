<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/BZr_XNe9WRyxpmTg-IaMYDbDNMY7rwJ0Koc25irX_wSYZoYivlSuuAYxQzAPZFUhLXHT_MET4ZPhnFHdbTp_4Q2Iwrx_rk01xiyeJat9moHVelZEhc32thjf-a1hL8XPV5SbIfRmCer0tEoI0R6I5pvnHiq0gcF56zzBfbpXUG-s95VbSbw8a62sbXXiA-ypckU2nmqc3f4e6-G1TsY9u-IY1vd05ZsSmbUTdno2h_LXgVh0OjmUi4hVm-xV0Z5uGx1_M115ETIBPDbjGh_yolCYhNKg0kodKlwjIVq0sf9CsXGmYM1jgwAxFw7S32jIIpx2qiCvtpK9boi3fH_3YA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 250K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 14:58:45</div>
<hr>

<div class="tg-post" id="msg-76514">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/288c09ebfb.mp4?token=TPGY_TpRO_KnMvSXEPzCl-AvpID8KgXl2kAmg_iQHtPAY-y01YoDegI-88OcNr0OaZjlMwXj3Ac4p0pcySNSreFKhNRNM6KB7Yr5altME_ZJA66vW-_6XEtKHUOzWjYwngDi1tZ14A0OUWWOyOlbYuacHU-oWD-dIe_DrAOMxkhbAsJJWJeRviq0MPMS4AMwEufS8urtuOaGa9BMIaog7aRq_fRKJs3b_9GheLveE2P38oKJzmY7UjVFFebYpARUuBzfQgj2vbfbNiNWKREeycssdcKbQTvZY4nBHuRoUiCXmnYgO5YNKqyAx42-r1IWRbuAQ7fezgmUnaWn1e5aVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/288c09ebfb.mp4?token=TPGY_TpRO_KnMvSXEPzCl-AvpID8KgXl2kAmg_iQHtPAY-y01YoDegI-88OcNr0OaZjlMwXj3Ac4p0pcySNSreFKhNRNM6KB7Yr5altME_ZJA66vW-_6XEtKHUOzWjYwngDi1tZ14A0OUWWOyOlbYuacHU-oWD-dIe_DrAOMxkhbAsJJWJeRviq0MPMS4AMwEufS8urtuOaGa9BMIaog7aRq_fRKJs3b_9GheLveE2P38oKJzmY7UjVFFebYpARUuBzfQgj2vbfbNiNWKREeycssdcKbQTvZY4nBHuRoUiCXmnYgO5YNKqyAx42-r1IWRbuAQ7fezgmUnaWn1e5aVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم صاروخي يستهدف مقرات حزب الحرية المعارض في مدينة تشامشار بمحافظة أربيل شمال العراق.</div>
<div class="tg-footer">👁️ 501 · <a href="https://t.me/naya_foriraq/76514" target="_blank">📅 14:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76513">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇷
سماع دوي انفجار في جزيرة قشم الايرانية.</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/naya_foriraq/76513" target="_blank">📅 14:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76512">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇷
سماع دوي انفجار في جزيرة قشم الايرانية.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/naya_foriraq/76512" target="_blank">📅 14:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76511">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW7Pukqvp0NrCIzhwMoViRpktniNZkDK2I6YKSQ-eSC_-mUzjNWSFGXgEPhe5XwJWxSbOcYAc50RvcGlccKHzDCFiWYQ0KmU9mOjI8BYDMR5cpKmgEC2TmFxMGZhre2KUDCxtD0WPA9nMaZzwhMfsv2s6tcYtd_0YMvFdWmZW6hmA4qG0JRXsQ7afLRFUJYrNUY-42yh1U1_73mfWCT0TSlKrS_9kTVxsi43z5EQT5SW6uF4Kb9VWIHJEBhO97jlLczLB_nEhORWpxRt-aFY1B9rS6iu6pPtJjti41ouoxGdAIzrHoC9fbzw_fK-aIDDSC6rBVsOLwB_lnQNXZOkpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">{فَيُرْسِلَ عَلَيْكُمْ قَاصِفًا مِّنَ الرِّيحِ} - [الإسراء 69]</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/naya_foriraq/76511" target="_blank">📅 14:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76510">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇷
رويترز
: 3 منصات بحرية تستأنف الإنتاج بحقل بارس الجنوبي للغاز في إيران.</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/naya_foriraq/76510" target="_blank">📅 14:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76509">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🌟
🌟
حزب الله يطلق صواريخ دفاع جوي نحو مروحيات الاجلاء بجنوب لبنان.</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/naya_foriraq/76509" target="_blank">📅 13:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76508">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
‏رئيس بيلاروسيا
: على أرمينيا الحذر الشديد حتى لا يتكرر المشهد الأوكراني هناك.</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/naya_foriraq/76508" target="_blank">📅 13:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76507">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/282721e690.mp4?token=FPkU-S0YydxpMwZ-UmPToi0g280VlFs-VQsw-ew8QsdjPUQnA3oUEB-8LNnit29fJ7kJ4Urf83hATt4NpfGYbaue03KK7SjVIl4TzIIbRv4MuuTgCBV3ozbV10yiZeUGodxtbXRYyhBumvelb-MOvMMZYxa49iqV7VP2Xylw4ANJPza9YEh5-VIRrb6M9yL3jQ6glz1PY_6Obt9m0oQuzKsdUeb53YffUeiJE2_AnWS4SW1pA38DmKCsu5cr48SaAdY73TLwqOnp1BL0XTMXM4G3aR9wkALCjRzaNtbJnEtP_Gwum3dS6W-Ef9B4K6W1X9Bs_BnHwsM9cF5_vhfVW7RrkKLmXwmuKjHZLPQU7w1B_hNlwdIpOaTG0zLrJdVSEP05MDOCeqq0fRY63CqDJjrNjoN-BwDX2B8vl2lhNMGcgRIe8ZeBiCTUz-jTsUcqEQYM7EzrubMD-q3qE1osVMspIS57NZcURx6DrGNUif2NW86nEkpX7GjJ7aDM7towZ6DlD1bM5P8gvp-5s7puFp5GnB8zYSstyChPak1vHxyWyMmqsGeqgZpRlgTbYaOPSuEQnsjnMFj5ulJ8tfw8JyrrCGL7Du1OrZaWEPQLTrcINgzYcq8ln-N6gmrE0N6r1pvig9hgBzZ4820qn5GBUpHhX6uIQUarRG3hHMtVZ3c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/282721e690.mp4?token=FPkU-S0YydxpMwZ-UmPToi0g280VlFs-VQsw-ew8QsdjPUQnA3oUEB-8LNnit29fJ7kJ4Urf83hATt4NpfGYbaue03KK7SjVIl4TzIIbRv4MuuTgCBV3ozbV10yiZeUGodxtbXRYyhBumvelb-MOvMMZYxa49iqV7VP2Xylw4ANJPza9YEh5-VIRrb6M9yL3jQ6glz1PY_6Obt9m0oQuzKsdUeb53YffUeiJE2_AnWS4SW1pA38DmKCsu5cr48SaAdY73TLwqOnp1BL0XTMXM4G3aR9wkALCjRzaNtbJnEtP_Gwum3dS6W-Ef9B4K6W1X9Bs_BnHwsM9cF5_vhfVW7RrkKLmXwmuKjHZLPQU7w1B_hNlwdIpOaTG0zLrJdVSEP05MDOCeqq0fRY63CqDJjrNjoN-BwDX2B8vl2lhNMGcgRIe8ZeBiCTUz-jTsUcqEQYM7EzrubMD-q3qE1osVMspIS57NZcURx6DrGNUif2NW86nEkpX7GjJ7aDM7towZ6DlD1bM5P8gvp-5s7puFp5GnB8zYSstyChPak1vHxyWyMmqsGeqgZpRlgTbYaOPSuEQnsjnMFj5ulJ8tfw8JyrrCGL7Du1OrZaWEPQLTrcINgzYcq8ln-N6gmrE0N6r1pvig9hgBzZ4820qn5GBUpHhX6uIQUarRG3hHMtVZ3c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صانعة الأفلام الوثائقية الأسترالية جولييت لامونت، التي تم احتجازها بعد أن اعترضت إسرائيل أسطول المساعدات إلى غزة في شهر مايو، في مقابلة جديدة أنها تعرضت للاغتصاب من قبل جندي إسرائيلي داخل حاوية شحن غامضة، بينما كانت مقيدة بالأصفاد والأغلال.
كما تصف أيضًا تعذيب الماء، والضرب، ومشاهدة الجنود يستخدمون أسلحة الصعق الكهربي (التيزر) في وجوه النشطاء.</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/naya_foriraq/76507" target="_blank">📅 13:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76506">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🌟
🌟
🌟
حدث أمني صعب يتعرض له جيش الاحتلال ومروحيات إجلاء دخلت أجواء جنوب لبنان القطاع الشرقي.</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/naya_foriraq/76506" target="_blank">📅 13:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76505">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">لا تزال صواريخ الاحتلال تحاول اعتراض هجمات حزب الله</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/naya_foriraq/76505" target="_blank">📅 13:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76504">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bc349f8e1.mp4?token=bJC2MfZvUWzMXePgKwCn5GKbn9MPdHZynnGG_CIhdwf7Tu2ySC0O1bpbzZ9WOl-phLPV6IPCh7X2Rs2HIw-00Lrf3HqQ3HUlS7nrFBgnIck4aXsdvZqidDXjYx9w34UKUHVDSjwIUV0EmwL8URlowzIvdDkVLqxylY8QAGh9HtEm-GtSP0yQpjRrRgOV6oRCFVx4t2ZN9G5S9RIhizjYY8jcOGhAc2WucCSERii4PYBs9813C3HyTw1nCFKaFv4V4FBMttvi9kw9TB7QPyZ5zm3miboxcZD_o7AEYt0k8Yfs_Ea69_VQpZ0vRr6ZSoMenszwSYXCC2HFpt9fxpy5AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bc349f8e1.mp4?token=bJC2MfZvUWzMXePgKwCn5GKbn9MPdHZynnGG_CIhdwf7Tu2ySC0O1bpbzZ9WOl-phLPV6IPCh7X2Rs2HIw-00Lrf3HqQ3HUlS7nrFBgnIck4aXsdvZqidDXjYx9w34UKUHVDSjwIUV0EmwL8URlowzIvdDkVLqxylY8QAGh9HtEm-GtSP0yQpjRrRgOV6oRCFVx4t2ZN9G5S9RIhizjYY8jcOGhAc2WucCSERii4PYBs9813C3HyTw1nCFKaFv4V4FBMttvi9kw9TB7QPyZ5zm3miboxcZD_o7AEYt0k8Yfs_Ea69_VQpZ0vRr6ZSoMenszwSYXCC2HFpt9fxpy5AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لا تزال صواريخ الاحتلال تحاول اعتراض هجمات حزب الله</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/naya_foriraq/76504" target="_blank">📅 13:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76503">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51230d4a55.mp4?token=cULcKxPk6MNm22Llzxjr94LSHLpQE87PaV6sY7CTdVq6dWEX_xgxmGBSGAxEtAsDYomXle4GgyAWEkN1fISozkpTqsU6FgLfhQjFGqNfb4GfRBQe0--WuF-fRsqkJRhtPbSxvaf1haetUiRsf4EJim8xVRSmXXi6g5O4fyRtVC7rMv2uvKbsfWmFe5IVgAdLzdGmFUGVMRLJG4eW98xzNQx1B_sAC_te35AeeW1urXVwiAEHcWFKlIlsLd3WqYpbG8pLzbQBqejvegLcl-DeHO7yJOZRb_-qvWBhweoR3zYzy9s-lFrNx7UTbQtBGT_oiQ1DP61xeJgpOYHgXJ9CIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51230d4a55.mp4?token=cULcKxPk6MNm22Llzxjr94LSHLpQE87PaV6sY7CTdVq6dWEX_xgxmGBSGAxEtAsDYomXle4GgyAWEkN1fISozkpTqsU6FgLfhQjFGqNfb4GfRBQe0--WuF-fRsqkJRhtPbSxvaf1haetUiRsf4EJim8xVRSmXXi6g5O4fyRtVC7rMv2uvKbsfWmFe5IVgAdLzdGmFUGVMRLJG4eW98xzNQx1B_sAC_te35AeeW1urXVwiAEHcWFKlIlsLd3WqYpbG8pLzbQBqejvegLcl-DeHO7yJOZRb_-qvWBhweoR3zYzy9s-lFrNx7UTbQtBGT_oiQ1DP61xeJgpOYHgXJ9CIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
غارات صهيونية على مدينة صور جنوب لبنان</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/naya_foriraq/76503" target="_blank">📅 12:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76502">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">هجوم صاروخي يستهدف مقرات حزب الحرية المعارض في مدينة تشامشار بمحافظة أربيل شمال العراق.</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/naya_foriraq/76502" target="_blank">📅 12:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76501">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">جيش الاحتلال يصدر تحذيراً نتيجة إطلاق صواريخ من لبنان.</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/naya_foriraq/76501" target="_blank">📅 12:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76499">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjDwQK35zHT-h26EljgvAnwvlxKSCbNDsIo8QpDimH7XMBWAJCegjdolWun7AW7md1--c285qDG2Q3sI2Azkc7zJqDcHaN7ivlvW8q-xodebuVuHrKzJs5Cxy6QAa6xqvzljXFb4cadTVpXq_Uo9iaLlg6UtoLNtXFDVdjkFnu6DBAWmiJBwfVu-zJ6kXrkTMbr9V68pYFs-P6fut1K48DgB3SU61zS_j9phccqoR0s4poOFQ3HRoIjtSA6X6M0pWdnDYFyvBaq0dPqjm0IXhX-VEH51b24OgO7DYJlL-unLrAZk6hnW8AL52QWnFdLDXq6XeowFxgnAa8FpKj1D3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15e46c68c3.mp4?token=rc8cmoVXYRATe27P5JqFlzbkh4Erl2KzYuw7oYdg6_pRW_aTgkk_0lKPMuCZRBcIpFXXTh2PhC5ewOiwNUSEhHdVxCsGybOjyD1SDNGuluO6WKCySs_FxG1Kfkb2LQs4hjewr8_ZepiKWQH0KMRbHwixnZe7jiJsyYM2lMxbIo_rbkma-eIAIimIcdHlXPrSYQpIlOaCBzVgh8KgZhKubmbPrwfPwBUVHCQjKc7mZZswo9soEsPovhtx4UuJNTBHLkhXk8-oSpzsB9Sdf4cwzX3IaIFWmavaIusR0aQmahcWxSZXdHLRHtipwmmLcrH4A70y8hUSzSK8E2KgN_kA9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15e46c68c3.mp4?token=rc8cmoVXYRATe27P5JqFlzbkh4Erl2KzYuw7oYdg6_pRW_aTgkk_0lKPMuCZRBcIpFXXTh2PhC5ewOiwNUSEhHdVxCsGybOjyD1SDNGuluO6WKCySs_FxG1Kfkb2LQs4hjewr8_ZepiKWQH0KMRbHwixnZe7jiJsyYM2lMxbIo_rbkma-eIAIimIcdHlXPrSYQpIlOaCBzVgh8KgZhKubmbPrwfPwBUVHCQjKc7mZZswo9soEsPovhtx4UuJNTBHLkhXk8-oSpzsB9Sdf4cwzX3IaIFWmavaIusR0aQmahcWxSZXdHLRHtipwmmLcrH4A70y8hUSzSK8E2KgN_kA9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات شديدة تهز نهاريا ومحيطها.</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/naya_foriraq/76499" target="_blank">📅 12:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76498">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🌟
🏴‍☠️
نهاريا تحت قصف حزب الله</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/naya_foriraq/76498" target="_blank">📅 12:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76497">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baCdUErM8yEP_AtcDEzWJgCKbw9FeAzTvkIOpIslePnScFLnN0IGLVNblGslRJoRZs92efleAiQc7bZ14LxxmbHK5t9jrB3DKWMgPbYa0aUg82G9Foa9LGl2zhmSp6L5DhhdOb1kUJ-UH18NHKuMgjhRmroRQ1_lw9xeQCquUNN1AYWverW-jwt-CK6VAzpAic8JGDir1lqOYkN0FhipTj8cK5imy9Hwt5KSGrblbnsiZZrnxoQfKaOZKhoLkDBTsWJbVKeXfzSUZh-Mcs9eOcXMVZ1OZAIU6yLQUSVrW-p7lESvimjG7teoiesq2KS95mlkALx8hbYfmVS40C98RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🏴‍☠️
نهاريا تحت قصف حزب الله</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/naya_foriraq/76497" target="_blank">📅 12:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76496">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🏴‍☠️
⚔️
ماذا يعني ذلك ؟   يبدو أن " إسرائيل " قررت وتستعد فعليًا لتوسيع المواجهة، خصوصًا في العمق اللبناني، وهي تتقدم نحو النبطية لفرض كماشة عسكرية مستغلة الآلة التدميرية وسياسة الأرض المحروقة. فيما يكتفي حزب الله بتطبيق “نظرية الكلب والبرغوث”: تقدم أكثر، كمائن،…</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/naya_foriraq/76496" target="_blank">📅 12:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76495">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🌟
🏴‍☠️
نهاريا تحت قصف حزب الله</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/naya_foriraq/76495" target="_blank">📅 12:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76494">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c192cff683.mp4?token=DzIw1wj7Q7TiM1ZJMwDzr6d32CFnmD62v7-32B49QKANPv3Vjq98Tl2T6UutLWY5iwVO3aHykkfwVxHq7lMMYv55vJTQjMt2LEu455apuaPaI1Nx6dfn0_FgAl8uHRVral_xxMoksrZ4eSqHTjGE-6L9_S6FFu9UrFPCLGG0XdQb-l4smg5xQBYbWZL7ZO5TE2NWZtG5IL9uKJNe2pVVlQbJJDi2vnfnFlAu98lwYgO58kgvb2IOTFCtISDSK_BYsCMaPWrq16Fv9gLzbmlWNlpGm9eyTu3m372Bb9pbS4LJ7YWIbegIQtvfdN_hSkD5sk3RHtnoBfZnRND68sjMRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c192cff683.mp4?token=DzIw1wj7Q7TiM1ZJMwDzr6d32CFnmD62v7-32B49QKANPv3Vjq98Tl2T6UutLWY5iwVO3aHykkfwVxHq7lMMYv55vJTQjMt2LEu455apuaPaI1Nx6dfn0_FgAl8uHRVral_xxMoksrZ4eSqHTjGE-6L9_S6FFu9UrFPCLGG0XdQb-l4smg5xQBYbWZL7ZO5TE2NWZtG5IL9uKJNe2pVVlQbJJDi2vnfnFlAu98lwYgO58kgvb2IOTFCtISDSK_BYsCMaPWrq16Fv9gLzbmlWNlpGm9eyTu3m372Bb9pbS4LJ7YWIbegIQtvfdN_hSkD5sk3RHtnoBfZnRND68sjMRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
غارات صهيونية على مدينة صور جنوب لبنان</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/naya_foriraq/76494" target="_blank">📅 12:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76493">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzJjr6cdcp-05PqDfUBZgFiz-W7J-ykL2KiDnIJOKOL97MgOIJWKVEwq93rIvazSsOVQhmxpMWVToPAD467KlhQzxNS4b9fhiiSKv7Pc716KaLAOqG2g2DhQzJ50iI2NfWfou9wfm7CppbHfB-HK5tkyNyHsxazwLfNeGxCeAv8O9TobK4tJahaLrwJk9f2oxWfFJ4uo5TYttzsEhGD0RQsJv9qdo5xGCj-IbH1RUYcx_Ez_FEiEFi0m7JNLUyoJTGvtPVtnGaQxlDJx2RLF3FjEyGrIfSR0GsYJ55EViwHFGtL9FGVm4g9smewbEE8dgDViVfaw0UOhrM8aDo8gJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
تحليل أجرته Ynet العبرية:
يظهر أن إسرائيل قد وقعت في فخ من صنعها في لبنان، حيث يوفر عبور نهر الليطاني عنوانًا رئيسيًا مثيرًا، لكن دون استراتيجية خروج واضحة، مما يترك جيش الدفاع الإسرائيلي متورطًا بينما يوسع حزب الله مدى صواريخه وتهدد المحادثات الأمريكية الإيرانية بسحب البساطة من تحت العملية.</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/naya_foriraq/76493" target="_blank">📅 11:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76492">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnpTt0-9UVmVbrMcRMinOTHxg0zcOUQYztuuWH93KuMEn3CL_S50uxfVEfNBoDiSUNqo4qiCzLI41pPV7gZXKtMCI7qG0obuA_TsT-z6xvIS2mfgoV9F0yysw6yR1B3cI3b0-D_wYLMi9UtNj6ZFatVfcWYq-jUAPLzF7qM5tRCXxv0Npj-mjPywS50rlOPLEUEp1d2vNaz0daXLPQkrDR6HK1MMgv0pu2MnYK73-BgXHnDNsp97spLk3mqnYMhcFdRg-3HVfiLdIFM84iqHfRupv-NcrkU5ZvRFE2gDgYKjRdaAN3jZfG9Cb9BrAaGmocVpgQsozCC7TYqznP9tAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
انفجارات ضخمة تهز الجليل الأعلى في الشمال المحتل.</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/naya_foriraq/76492" target="_blank">📅 11:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76491">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e1090629.mp4?token=PZY91skugxpnur05NJMs6-qQ7awkizKcncOkS1iKr43qJPhCiG1EZnc_tcPIA4grkE4xZrgSLrtmYg1Dlvb-O3G4IqvDz34o5rwnyI5ioQY2nuvx7XH4uT_bE_R_4A3d81PttU4BkwADfttEHpf-7alavJRu_avLJOHwo9mypxE4mLm8hZkaQsMowXxJ92REIdjXTgGP9ZdQ4Cqk1f3hkGhoXkaSCIez1nVyn_IEyJmExiz94f_Aw2w0s6vx-B5xgfwRV57K1p2Z0SaKgm1ZEVVt2grrYbgMokLa7UmavYgssfqFmYsrA5uHatacRBDBIjn4bYtsqQWRsBkhoG9E2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e1090629.mp4?token=PZY91skugxpnur05NJMs6-qQ7awkizKcncOkS1iKr43qJPhCiG1EZnc_tcPIA4grkE4xZrgSLrtmYg1Dlvb-O3G4IqvDz34o5rwnyI5ioQY2nuvx7XH4uT_bE_R_4A3d81PttU4BkwADfttEHpf-7alavJRu_avLJOHwo9mypxE4mLm8hZkaQsMowXxJ92REIdjXTgGP9ZdQ4Cqk1f3hkGhoXkaSCIez1nVyn_IEyJmExiz94f_Aw2w0s6vx-B5xgfwRV57K1p2Z0SaKgm1ZEVVt2grrYbgMokLa7UmavYgssfqFmYsrA5uHatacRBDBIjn4bYtsqQWRsBkhoG9E2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
صحيفة تايمز أوف إسرائيل: جيش الاحتلال الإسرائيلي يسيطرعلى قلعة بوفور (الشقيف) الاستراتيجية في جنوب لبنان كجزء من الحملة المستمرة ضد حزب الله.</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/naya_foriraq/76491" target="_blank">📅 11:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76490">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3af04a6e44.mp4?token=XXFJCbtZjZRtDLeOsK3QCwRD6zLSzqjulcsJE6g0SbeDntLetkXKkTOtT2-957xUKU9SK_6sa8-CjrCVT6B7h57VJxwfLTBlYLzLKIdtRtsLQAl1PqjyG1jnpQCGO1bi0y4xPBKj_8ZsY4r3B_yhKK4smbVhGBR0fbVoZNn5FZWIKlase7duNFyH26bSnMs9u5dtCnUip-AO6m0Nld-j-07CDZxoNelEE9pA9-sI79-u4g590vcwDZ-wxs2AtuSCUO9BHfznKH5HbPKUn9uX5GYBTVCgAkGt1bHHKQt_EGOibCGbmyVRHtKAWldC5zhIMJ_GStinmcaIOBCIba8AXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3af04a6e44.mp4?token=XXFJCbtZjZRtDLeOsK3QCwRD6zLSzqjulcsJE6g0SbeDntLetkXKkTOtT2-957xUKU9SK_6sa8-CjrCVT6B7h57VJxwfLTBlYLzLKIdtRtsLQAl1PqjyG1jnpQCGO1bi0y4xPBKj_8ZsY4r3B_yhKK4smbVhGBR0fbVoZNn5FZWIKlase7duNFyH26bSnMs9u5dtCnUip-AO6m0Nld-j-07CDZxoNelEE9pA9-sI79-u4g590vcwDZ-wxs2AtuSCUO9BHfznKH5HbPKUn9uX5GYBTVCgAkGt1bHHKQt_EGOibCGbmyVRHtKAWldC5zhIMJ_GStinmcaIOBCIba8AXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🏴‍☠️
قوات اليونيفيل تنسحب من الجنوب اللبناني بعد اشتداد المعارك بين حزب الله وجيش الاحتلال الإسرائيلي.</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/naya_foriraq/76490" target="_blank">📅 10:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76489">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPD8_EamnKvFlYBq36yk8Ewox4tpgSF6dZVWcWf-zYUCShLDkHADPzE_2-uORjU2oG1QlzClCY_eNK8eJDhzUaCf_sJnXgpGRGu5IOD3LJZ8bUtBwrciJwEKmYPdm50z8LzNAqUdcQA44jUQHME1bYgQKSHgfCNixshlHVTEl5qm6PmAfj2ClzwfLwFIlqQTDPRWSygDkMozHk9MHPJMTbsbM-UZdLVIClCa03eTyRZt3bDyVYRkpMAyJ4G1jNNc2n24figywZEJSdMAY0jGKwfsjrViuhZRdi0vr5vGwEynrGD5YHgG_q-iHu0LqeOz52G86PjDF9ORKL0y1OP1Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
رصد هدف مشبوه لنظام التعرف الآلي (AIS) يدّعي أنه ناقلة نفط ترفع العلم الأمريكي بالقرب من مضيق هرمز.</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/naya_foriraq/76489" target="_blank">📅 10:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76488">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yzvt6Kbkg62dQ0CKltZo-OKul9Qe02kIHJy8vrj9X467MMMlIUCcbEkkBYia6BOs5VfxQKpV8USVHzG6L_MKStQEsBBM7JQFfZkACuPgWg3tEz_nWjAbCAmPm6LBWgYithn7YyY5JM4-qbQ3Rd_bYHwn3Cn3__rZWSFlw4BwDuCdgmUGs6WnW9z2xjW88Z4SCsFvkjpJHFbcTauh1wcgGYE3WtthJndVpmqixjejvGrZ-zVhgHRx1yGrr4vmtPlrQ0QYaLYh78Zxe_74w3MeYWv0Mfo2D-Cmy4fWUKsdtW65VTPvT5fvkachT1CatTPXk0Rt6ZRs1Gp9zCxdffPUzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
نيويورك تايمز: يحاول ترامب تصوير حرب إيران على أنها على وشك الانتهاء ونجاح كامل، لكن روايته لا تتوافق مع الواقع، وبعد سنوات من فرض روايته للأحداث، يواجه الآن أزمة تتعارض مع قصته.</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/naya_foriraq/76488" target="_blank">📅 10:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76487">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s62VVSFrVjsBbxb51rJLq7jFcYg-WEJS33jZK-LIMqSs8P9NCMcRhJiNPmDa8KDZK2X7imBir_la_O6ojez6WiYczR_ERIdWewWKXbA6XCELLuwNlxOyheB2YZuHNCAoZv2OSdxpV41KRwjldEasvYePCxwDG1l_5w25_aOm7oyMaARmO8_fhfA-ZmjLIqpWtM3ZVebT5-gP2Jj7p2yuWVzLAckON3W8tIHAfJnifCDgJUCfr-dSqjXaHykj9MbsbBLmT2CVPnzEPNkBfEcE8WnJUBR4WJnCDLXXJVqq7h_6P2zICfaaau0JW62NxhlwyowAJKCSSYq51EI-ABJ8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
صحيفة تايمز أوف إسرائيل: جيش الاحتلال الإسرائيلي يسيطرعلى قلعة بوفور (الشقيف) الاستراتيجية في جنوب لبنان كجزء من الحملة المستمرة ضد حزب الله.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/76487" target="_blank">📅 08:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76486">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇺🇸
ترامب:  ستكون قاعة الاحتفالات هنا.  يُطلع د ترامب زوجته لارا ترامب على كواليس بناء قاعة الاحتفالات في البيت الأبيض، والتي وصفها بأنها هدية منه ومن "الوطنيين العظماء" لأمريكا.  "ستكون هذه القاعة الأروع من نوعها على الإطلاق".</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/76486" target="_blank">📅 08:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76485">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇺🇸
ترامب: تنتهي كلمة "Dumb" بحرف B، لكن معظم الناس لا يعرفون ذلك.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/76485" target="_blank">📅 08:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76484">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6fr8vtgUMhuQgk2f-DNGqWPbazcNdeT5JcH_zKRqeeA0IbR6pGUytJHPotg33ISRvcTyIgucskBocq6lDpjCOnkbdaEYvQiU8VnLaKjkkOxDWW844YSlClxyc0h1ui_9_cbuzk5TgIyLqL2Pnk1nIVJoUVnJ2joWnbtqV8TdgvBDTJ272e7qns_M3xzK_Dx5cN8XuaiEYl1Unrl1KgvpgM2iDNAw6bvsggr8rmX3QLhAkz-zVO9EB7WowvHUmOE9SnWKTi57QYFKFpBg-lrVDyDiyNgWLZupA3oIvMJtjuz0xS-uz7u5tBBVTBWEh3Wf3CxN5bQVgZLuFQV_7NoVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
كانت نتائج الفحص البدني الخاص بي، الذي أُجري في مركز والتر ريد الطبي العسكري، والتي تم إصدارها للتو، جيدة للغاية.
على عكس الرؤساء الأمريكيين الآخرين، الذين لم يخض أي منهم اختبارًا معرفيًا معتمدًا عالي الصعوبة، سجلت 30 نقطة مثالية من أصل 30، والتي تعتبر "ذكاءً استثنائيًا".</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/76484" target="_blank">📅 08:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76483">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f80b8dab03.mp4?token=heCKkjrfXtVudTddpAq4Z6V6xv93u3UM7Io1QbblFDcwprK-c7uOYq7tdjnUHDI_3Lb6z1uWn2oJ27q9ChSLTIDERfu_h6ylgokzSYvJhEh5SrQdces4HbiCo7D-SPVAT6JlSOjIUb-qZCxC1Y9xh7RpS7hTFg5SgYKgAJzB-G4ScJL9nJ5se9AUxbLYTnKlRIMQk6eJsiriOzG2wogFbYQqWscUnKTpg4viEpi5BHz4ybBsK1rbBO32sPefJRaXHACR2c7g765xaM-oGxAtF8HwJJb3LZ1m8HrUoYlRG4cVzY8yLZ0iVkZ6RPbYePbFBX_oY38bur71tYvz_pST9Aqlz1It8bnrRr9Pyi4cdVL2W40MBKVgdb7oFHee8XPUWU3cJ9OVViBKAHRIzsdAWEQnIlYjFBZ41z-JSOntFrp0jeFaEU5sP4R1YjuuJJ1qbF0OHRvFREueSUMEtQv2b4lXCW8vX4zH-jzwOpfmBrnsWa1CBMQN6jsp0Pya06we_bPKSDlqJl5DZES4YQlD-Z9TD8q4uzE3fjy4YWFiBVF_XqCYOojalC86pM3RGbNMUg31vvsIewpuhULG82NEha908-DwZrKFHi6o5qFHOIaHTm1QIp9vhfXEpIMTYA2PjTi6P2yRgBTyvJebMV_MBoZsr8QjUuk-X2XLo9TjU68" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f80b8dab03.mp4?token=heCKkjrfXtVudTddpAq4Z6V6xv93u3UM7Io1QbblFDcwprK-c7uOYq7tdjnUHDI_3Lb6z1uWn2oJ27q9ChSLTIDERfu_h6ylgokzSYvJhEh5SrQdces4HbiCo7D-SPVAT6JlSOjIUb-qZCxC1Y9xh7RpS7hTFg5SgYKgAJzB-G4ScJL9nJ5se9AUxbLYTnKlRIMQk6eJsiriOzG2wogFbYQqWscUnKTpg4viEpi5BHz4ybBsK1rbBO32sPefJRaXHACR2c7g765xaM-oGxAtF8HwJJb3LZ1m8HrUoYlRG4cVzY8yLZ0iVkZ6RPbYePbFBX_oY38bur71tYvz_pST9Aqlz1It8bnrRr9Pyi4cdVL2W40MBKVgdb7oFHee8XPUWU3cJ9OVViBKAHRIzsdAWEQnIlYjFBZ41z-JSOntFrp0jeFaEU5sP4R1YjuuJJ1qbF0OHRvFREueSUMEtQv2b4lXCW8vX4zH-jzwOpfmBrnsWa1CBMQN6jsp0Pya06we_bPKSDlqJl5DZES4YQlD-Z9TD8q4uzE3fjy4YWFiBVF_XqCYOojalC86pM3RGbNMUg31vvsIewpuhULG82NEha908-DwZrKFHi6o5qFHOIaHTm1QIp9vhfXEpIMTYA2PjTi6P2yRgBTyvJebMV_MBoZsr8QjUuk-X2XLo9TjU68" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: تنتهي كلمة "Dumb" بحرف B، لكن معظم الناس لا يعرفون ذلك.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/76483" target="_blank">📅 08:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76482">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🏴‍☠️
إعلام العدو :
يُعدّ الهجوم الذي شنّته طائرة مسيّرة مفخخة في تمام الساعة العاشرة والنصف مساءً على قوات جفعاتي نقطةً مثيرةً للقلق بشكلٍ خاص، إذ يُشير إلى أن حزب الله يمتلك على ما يبدو القدرة على ضرب قوات الجيش الإسرائيلي باستخدام طائرات مسيّرة مفخخة حتى في الليل، وهي طائرات مُجهّزة على ما يبدو بأجهزة رؤية ليلية، ما يسمح بتوجيهها في الوقت الفعلي وضرب القوات حتى في الظلام.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/76482" target="_blank">📅 08:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76480">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/laIUmw_aysHSzrQokjbnDWtqCLNqRWtBgqULYMtIGfZ4l_9R7H7tKda1oQu__cH6I0MJ4s8_ZBdD0Jol0u_kaUfuin9-e_G5R7pKNINeCmpSaQ1W0ztHT1QUM8_XGwyd1GVufgVxlYkHKfXeBd1vc9FHEiuOyMN6po9fzGfzoFJ5b0-nePnCZ5NIuhl_PFcUELS14zGdHSZVxHqp-t_idu0i1B8Kf7yY3t-FUJOCP96VCoSnYYJRmAoPjBHqIrB25QrD4Xhc17rOqI4KwmjYqx863vEHpYRDmUsDDNe5nJvQlniZQP6m6LM7lKUAe1_tHlfn7PFZaxb_g1hrprUCtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hSXdRW6U7cSAYTq9tR_z9lalj3v-vWxPnnTaH_Kfc8CUCPfAwVIM1UawXMTTvtPKkx_TYDqcLNwPLpexc4rI0A5OYamFTXKyGlwMvuFIFxxAadPuu2ld41lLF_t_cZqnUgEU2jcj8Jr3bJPXnfLdEKZcXMEDHb4oq990Ef1gyCslG-4Wrg702vcG4kcdS7GA6s0q5swt0m60jugcy4_ye3o7Pv79l9YM0UT5pUFcVo2XbHLewIIyDbqL2UagyDUymTPUEQVj1j9ZZEooq5Zbj3iZi3GUCif79f9UhSRr264PSqi1Xo78sFGkinOlgvNoCAvmVm0K5ZNMdibHL83qdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌟
🇮🇷
تعرضت طائرة التزود بالوقود KC-135 التابعة لسلاح الجو الأمريكي (الجناح الجوي لجيش ألاسكا) لأضرار من شظايا بسبب ضربة إيرانية في المملكة العربية السعودية.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/76480" target="_blank">📅 01:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76479">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🌟
🌟
إصابة ضابطين إسرائيليين بجروح خطيرة إثر استهداف منزل في جنوب لبنان كان يتواجد فيه قائد فرقة بالجيش الإسرائيلي، في هجوم نفذه حزب الله.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/76479" target="_blank">📅 00:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76478">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjPjFJsb2SNWogZ4hFDwvSZZT-r4kbdY0Qu05dk52SF-4Rc4cjUoLsQw6ZP1dBFdwCMMIr8wY2ht292A4RNa9IG0c9i8l4n95YUCEslZEJGj6L7RJgi1YI3l81jXT4BiyIFUhT-h8447yQ4AtPuLwTxrB0TGVcCsI1f9drzFGjdwexwe3UfIM_4w_XcuoO2FtgKtbSbswchB5MP7QVI1nnT0mxpWfhBJ8gxr-a9BAIrq-I1IBb6TKVzGSUcZQGqfBu7dsCwstFmMV6Yl5k2eY9wyeD7irL9ez7DHz0gFSMNelwzvvXP2NZIHfDZ7cb9g3yI8-r00JKclMvObsTG1SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب:يجب أن يشرح أحدهم للبابا أن عمدة مدينة شيكاغو عديم الفائدة، وأن إيران لا يمكنها أن تمتلك سلاحًا نوويًا!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/76478" target="_blank">📅 00:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76477">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🌟
🌟
إصابة ضابطين إسرائيليين بجروح خطيرة إثر استهداف منزل في جنوب لبنان كان يتواجد فيه قائد فرقة بالجيش الإسرائيلي، في هجوم نفذه حزب الله.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/76477" target="_blank">📅 00:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76476">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">أصابت طائرة مسيرة مبنى توربينات في محطة زابوريزهيا للطاقة النووية، محدثةً ثقباً في جداره. وقد طلبت الوكالة الدولية للطاقة الذرية الوصول إلى المبنى لمعاينة الأضرار.
‏رئيس الوكالة الدولية للطاقة الذرية رافائيل جروسي: الهجمات على المواقع النووية "تشبه اللعب بالنار".</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/76476" target="_blank">📅 00:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76475">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LufQKhMusjj0kVvV89ngcErO9L02Nl1CTJGU3bGRMtnzJdSxjHkrPGJwlBuoxzc-q5RUsvOUO4jvuRUMZ2Y2sQRM4I2czOoapo0oBwA0JofC6ECNL-0bv1fAReIvvyuFuyFmedHst92UzHZyjwoFRspuAfvEMEsqKBYONzCzQ0MoLBy9QY-jhAxZB_Ql1X1sXHTGNbhF8RZFLhCIVU9l-NzlWF-2b18KkFDMGTBNH0nV8rQy-2gSd_J4eknk80esKlqE8GULhsmg5PFFVmFJ46AOI_M9phTRyHQok0t1IBl14cj2k9e5-0_g_XJCzGI9QADUYypGwC_vgbNq0ZRh9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب
:يجب أن يشرح أحدهم للبابا أن عمدة مدينة شيكاغو عديم الفائدة، وأن إيران لا يمكنها أن تمتلك سلاحًا نوويًا!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/76475" target="_blank">📅 00:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76474">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYDDcQTgNxMJ31OOO6LCVeL4btzYxh2KCBt6HDBZxSbV6E2YUovUpZdZhW75oGcd5BW2h_WkHFjHXs_7j2R99KDrEcQDGcOugdyDAy23yAYoqmH_3oHhlYrbVeM-51DNdyY6L2C4TDervh-J-a29GS1BRZCDhBIXWcgTbWvh0ElCYg7xqCgm6v1FBWPFb7DwaQHOhu7PH-yPlBpZXIaPx0HCGP5PHTS_DXh4Exo7EZXzJds1b9RRs0Nshwg09iu7jXk2tEVdT2b9X4crr6KqgnufOjJcQHaurYKa_YTr_1rLo_omXydVLPHT9xQ5IQ4FYITXaPc6SqXt5a6Ff313aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
شيخ عام عشيرة البو مرعي في محافظة الأنبار غربي العراق و رئيس لجنة الإعمار في مجلس محافظة الأنبار سابقا يشيد بمبادرة الزيدي لمحاربة الفساد ويعلن طوعيا لرئيس الوزراء للتعاون مع المجلس السياسي للنزاهة والرقابة لاسترداد المال العام خصوصا للخروقات التي حدثت بمحافظة الأنبار</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/76474" target="_blank">📅 23:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76473">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🌟
🌟
إصابة أربعة منتسبين من قوات الحشد الشعبي إثر انقلاب عجلة عسكرية في بادية السلمان بمحافظة المثنى جنوبي العراق.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/76473" target="_blank">📅 23:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76472">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🏴‍☠️
مشاهد تظهر تساقط الصواريخ التي اطلقها حزب الله على شواطئ نهاريا وهروب الصهاينة نحو الملاجئ.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/76472" target="_blank">📅 23:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76471">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🌟
رغم معاناة المواطنين في إقليم كردستان من نقص الخدمات وتردي الأوضاع المعيشية، أرسلت مؤسسة البارزاني الخيرية أكثر من 1000 شاحنة مساعدات إنسانية إلى محافظة دير الزور السورية، في خطوة وُصفت بأنها تأتي لكسب ودّ الجولاني، عقب ارتفاع منسوب مياه نهر الفرات نتيجة فتح تركيا سدودها.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/76471" target="_blank">📅 22:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76470">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🙂
السؤال هو: من اين جاء الحلبوسي بـ500 الف دولار ليقدمها كهدية وما هي ثروته الكاملة اذن وما هو منصبه في الدولة ليكون هذه الثروة الطائلة وحتى لو كان لديه منصب هل راتبه يكفي لمنح فقط هدية بنصف مليون دولار وهل مهنة التجارة في الدهن الحر تجارة رابحة الى هذه الدرجة؟!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/76470" target="_blank">📅 22:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76469">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🏴‍☠️
‏عقب الهجمات الصاروخية لحزب الله..  جيش الإحتلال الإسرائيلي يعلن عن تحديث سياسة الدفاع لقيادة الجبهة الداخلية ابتداءً من اليوم.  ‏وقف أنشطة التعليم في مناطق خط المواجهة على حدود لبنان.  ‏إغلاق الشواطئ أمام العامة في مناطق خط المواجهة على حدود لبنان.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76469" target="_blank">📅 22:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76468">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/475b6b42c5.mp4?token=Vn-_EXtP0JuNj27LuIt-zZCKzVGAj-BFjLUfyeFG10WYMPrhWMQcWB94Vs8y2ozTpiHZwYQujWRvIZ2aWXxl-xnBwPTwMcOuZ1JAYfl-8iAURLa13fCLxY6pjQMFqfOHxB3jixHUKu6CDLtu5dct_ufHNLMd1o7TpxU4XNcVDFl1td23xNuhUsWu_MIJI-zrM-O1l9n0uwi7ziNQThanGeSWkpqfLaQvCTtl01pwQrAB0m9WgkWkO4uffWFIVG5FSxRczEPjotV7jW-sPCkug-sK7sgOBwn1q6hAKzSQuu4U8a6uScJ5wHzaHnd6dDPSZB0EJC6Rwmwn9mbeJR3HMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/475b6b42c5.mp4?token=Vn-_EXtP0JuNj27LuIt-zZCKzVGAj-BFjLUfyeFG10WYMPrhWMQcWB94Vs8y2ozTpiHZwYQujWRvIZ2aWXxl-xnBwPTwMcOuZ1JAYfl-8iAURLa13fCLxY6pjQMFqfOHxB3jixHUKu6CDLtu5dct_ufHNLMd1o7TpxU4XNcVDFl1td23xNuhUsWu_MIJI-zrM-O1l9n0uwi7ziNQThanGeSWkpqfLaQvCTtl01pwQrAB0m9WgkWkO4uffWFIVG5FSxRczEPjotV7jW-sPCkug-sK7sgOBwn1q6hAKzSQuu4U8a6uScJ5wHzaHnd6dDPSZB0EJC6Rwmwn9mbeJR3HMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سماع دوي انفجار كبير في جميع أنحاء بوسطن الأمريكية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76468" target="_blank">📅 22:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76467">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🏴‍☠️
‏
عقب الهجمات الصاروخية لحزب الله..
جيش الإحتلال الإسرائيلي يعلن عن تحديث سياسة الدفاع لقيادة الجبهة الداخلية ابتداءً من اليوم.
‏وقف أنشطة التعليم في مناطق خط المواجهة على حدود لبنان.
‏إغلاق الشواطئ أمام العامة في مناطق خط المواجهة على حدود لبنان.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76467" target="_blank">📅 22:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76466">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇺🇸
سماع دوي انفجار كبير في جميع أنحاء بوسطن الأمريكية.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76466" target="_blank">📅 22:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76465">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95bbb8a10a.mp4?token=vGU5V06wnnN3jKpAVC_Fg7mt89UN1pk2Xll_pyz7qdCM3fRKhlZmyp0UtSPX8RMy1iWIpCjXYYlVYCE6qDsz1I5gS1b-qYQi2l86jmBrWZqGzfM-c2GmG5o_7G6Yn5Prd2KeyvN1AMgVAFgQ2owQmcB2HZl00FR26FP2EZrb0T3zDHTKyye04N_ewX1fJB03T02iygzF2LT86mUIne7sgLLGzTTV2UxYlwzEK9rNHatKArbIL2EmC3rzBe0mYt3dcG4lX7w0frkJ5U-WT5O5bVXGdra3Piuofkm5bHJfszgT0Ia9jQlCb6uvUNAEF_6GzTXdWYsgCTb4w6knduUS9komnnBoiGwQAiC4pO9bsRdunOM0QxzkpwsyYIERVX57o4opXaxkVwB5bCENEIzNk-9ihxPjDhq7QMYbB1ahl4EeZVYOPIUYk1PD70K27gUvzqq_YkeS8RYZYom0Q5nxVO2iw2624G3i1qwpCIoY6cxozzPvRIymmNPjcoGXqgaxYWxk2JyNTq-8TUaQco9QnjL1jIyrlr-LBMBOLmlm5t4oVgdKtih7sJ9KZEde2Ve_UXrpY_KRqp1zR8AX-sR67K70qbCuKR6UkWDXaOQxMEj52ODKnnULzed1nJtBxZQttgBPCTJtT4kBiSC7CuU0GyjwbbnlsFceCOAFiOQeXBI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95bbb8a10a.mp4?token=vGU5V06wnnN3jKpAVC_Fg7mt89UN1pk2Xll_pyz7qdCM3fRKhlZmyp0UtSPX8RMy1iWIpCjXYYlVYCE6qDsz1I5gS1b-qYQi2l86jmBrWZqGzfM-c2GmG5o_7G6Yn5Prd2KeyvN1AMgVAFgQ2owQmcB2HZl00FR26FP2EZrb0T3zDHTKyye04N_ewX1fJB03T02iygzF2LT86mUIne7sgLLGzTTV2UxYlwzEK9rNHatKArbIL2EmC3rzBe0mYt3dcG4lX7w0frkJ5U-WT5O5bVXGdra3Piuofkm5bHJfszgT0Ia9jQlCb6uvUNAEF_6GzTXdWYsgCTb4w6knduUS9komnnBoiGwQAiC4pO9bsRdunOM0QxzkpwsyYIERVX57o4opXaxkVwB5bCENEIzNk-9ihxPjDhq7QMYbB1ahl4EeZVYOPIUYk1PD70K27gUvzqq_YkeS8RYZYom0Q5nxVO2iw2624G3i1qwpCIoY6cxozzPvRIymmNPjcoGXqgaxYWxk2JyNTq-8TUaQco9QnjL1jIyrlr-LBMBOLmlm5t4oVgdKtih7sJ9KZEde2Ve_UXrpY_KRqp1zR8AX-sR67K70qbCuKR6UkWDXaOQxMEj52ODKnnULzed1nJtBxZQttgBPCTJtT4kBiSC7CuU0GyjwbbnlsFceCOAFiOQeXBI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
المجرم الصهيوني بن غفير يدعو إلى إستهداف وتدمير الضاحية الجنوبية لبيروت.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/76465" target="_blank">📅 21:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76464">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2928afc4bf.mp4?token=Ez7BKGh0_mJ7qIZ-evu638yPZOTEh65ZCWsiEA7T4h5VdtjPo1WRAm9T0s7F64uVUvLHd1c-y2ZRuKHFi1Xj3WWuKJSFq17k5vnMV2KLZn_0MNM3N3dPH8G6Pi1g09md1_B8xvGCk7nbdCofHRq8eyQIVvUwIGHetUL_6qKWaQl42aqEjxCHXfMFm-6GJT6m64X0IifkFXJwu38vbJxN8iH53JPYiWU5D6X1XJpWCLxkNiPmgAcNCYCU3RgsXw_JpCu5CgQMnRdBHEKCBcWys3zXwvEcZxSzPBZ7K4SDvqABlKhECo6HO6blJKB3HeA0632p7p_MnyHpKDHwgpVXkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2928afc4bf.mp4?token=Ez7BKGh0_mJ7qIZ-evu638yPZOTEh65ZCWsiEA7T4h5VdtjPo1WRAm9T0s7F64uVUvLHd1c-y2ZRuKHFi1Xj3WWuKJSFq17k5vnMV2KLZn_0MNM3N3dPH8G6Pi1g09md1_B8xvGCk7nbdCofHRq8eyQIVvUwIGHetUL_6qKWaQl42aqEjxCHXfMFm-6GJT6m64X0IifkFXJwu38vbJxN8iH53JPYiWU5D6X1XJpWCLxkNiPmgAcNCYCU3RgsXw_JpCu5CgQMnRdBHEKCBcWys3zXwvEcZxSzPBZ7K4SDvqABlKhECo6HO6blJKB3HeA0632p7p_MnyHpKDHwgpVXkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
من حرب رمضان..
مشاهد تظهر قصف عنيف للعدو الصهيوأمريكي على مدينة خرم آباد غربي إيران.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76464" target="_blank">📅 21:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76463">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🌟
حزب الله ينشر:
תזכורת... שום "אזור בטחון" לא ימנע את הפעלתן</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76463" target="_blank">📅 21:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76462">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3Rv5KNwtpyYZidu4VMW-47Y-3_AvEuUDE3oS6Fqj3NRbt4u23Jlo19eYbT8a_6kXIULAprishmClP6pXm6fLtBPyMdJI4Tk7Zq51UGshMfIERcfcOOy7y9w34MULdbevHYJHGQmAOCTaqAhx8jyVyK1q1hh2LbScULKNjmeFqv1zkcj3rXKZzkNUMMt6GomgDk1A_3H3NHwmrkIuzgwh5mGCFd9oIP8lyTjiyxTFBj34XcdIycZ6XiFnWVlLiVoXPn1rLp9AhLxJdPP2eOBj0jII5qAhtKo4oxicJXf7H4DHnCopgjpkpc60xgMv7eC44nLHTeT0NI8VZCFZ190ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
قصف صهيوني بالقنابل الفسفورية المحرمة دولياً على بلدة ارنون بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76462" target="_blank">📅 21:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76461">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
الجيش أعد خطة هجومية في عمق لبنان بانتظار موافقة المستوى السياسي.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76461" target="_blank">📅 20:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76460">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joB-DaJmFyvrHi0jNRPMwmJgrtgnUxH1gWiB_sHHOnS12xbxR1R2W8xL7bPvnwpYi7M05gug6U3rtrKJMLp78Lr_WP4vWcb6J6A86Y8xf7BksRqMYdCqeImW2jqRLJdnObtlDESHxXkmdQdsV04bYSAX6YmO7FY8thBlaWxmGz9muXxwBDHZwziYoyCNNX6hsaBQPRHLvzYM64F1oLqurhc1hpbll0RqvpuxJYwVbPtVN_0YCs7BaIx8hyCZ4zlNodVwgNUZCXRqAmRTeTTpVQIfihVv_Nir8aSE0AgIiejsPtqhyNGsR7PrvrKN_mQPm013MQ2AQ5nfisOdzVMCuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: أفهم أن الفنانين يُعانون من "التوتر" فيما يتعلق بأدائهم يوم الأربعاء، لذا أفكر في جلب أكبر جاذبية في العالم، الرجل الذي يحصل على جمهور أكبر بكثير من إلفيس في ذروة مسيرته المهنية، ويفعل ذلك بدون غيتار، الرجل الذي يحب بلدنا أكثر من أي شخص آخر، والرجل…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76460" target="_blank">📅 20:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76459">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwwZdarpf1B3tCWzARb2GLObWIkxePSQKgJB1SgTJu1IqcsyejlZF6_9fdDCFmHuYafy13lNovED48sRvcJcl93qEFl57vnKgkfHir7o3cgI9XzBAs65JdOEdy6de4zP4KEUXOnGrhMKUODSIJ8e_ULhGFJgbkd_THYLxr-hrStsB6648gAE8MQTyzzPPn8BuLPgmahKWOTSGxJijJdUI-3tmSLAsOlqaNamjX_iKUhOy2ghCqLv21A1sSQZEgf2zFPoCDJrOGiZih4hTD_rikjO5dzINXeW9T55XnBXo6aUZlFauKvUo4xCTla_W6htc_DyCwwodhHHdewwHvfxkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🏴‍☠️
إصابات مباشرة لصواريخ حزب الله وإرتفاع أعمدة الدخان في كرمئيل ومحيطها بالشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76459" target="_blank">📅 20:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76458">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1775fa1285.mp4?token=dU-tF-qyZrXuItoYAfevKj6ih4RDObUSzSDCBmLOjYvLA2P66gpdGppaJkQhkesR6bJvmt-4yL-8MiWpKOLXM1tFFmNa1n_7msqBFGjVVZ-E4BOMcO_bNUQflLGfcoNc6KPBaMI5_zR4aI85jmWPu46YYiOX1OHNds9k0cpczOasFaMIz7szFejJIKJ_GILRCOHJwDV5Z7r3fV4iAl5p8PLgY3DSr12FpkXvpJIrX3kIFNHUS-smbaqcLzrX8pA8hL2OSg6M3Z4Esx5K04cUUvmbmMXCVUJm6qM9D21VQS1krjUuVBcTioWNVEopQAlHzSd4BbOYZC-DrndS_XrQOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1775fa1285.mp4?token=dU-tF-qyZrXuItoYAfevKj6ih4RDObUSzSDCBmLOjYvLA2P66gpdGppaJkQhkesR6bJvmt-4yL-8MiWpKOLXM1tFFmNa1n_7msqBFGjVVZ-E4BOMcO_bNUQflLGfcoNc6KPBaMI5_zR4aI85jmWPu46YYiOX1OHNds9k0cpczOasFaMIz7szFejJIKJ_GILRCOHJwDV5Z7r3fV4iAl5p8PLgY3DSr12FpkXvpJIrX3kIFNHUS-smbaqcLzrX8pA8hL2OSg6M3Z4Esx5K04cUUvmbmMXCVUJm6qM9D21VQS1krjUuVBcTioWNVEopQAlHzSd4BbOYZC-DrndS_XrQOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
صواريخ حزب الله تجتاح سماء الجليل الاعلى والدفاعات الصهيونية تحاول الاعتراض.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76458" target="_blank">📅 20:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76457">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a8de7f694.mp4?token=d1t43nH_TG4oLf1fITPpze68NaADQq2IeZMREBPLIO4K60vdwHqM5YRYdCURxt9L53oE-aiT5tb-icVlxDuxfXbu16zkfveH-F2JYyYlkYt-DPGxqj4lD2KSsRXuo7zQySNEMzkH5O6Ru7OkZ4unp68f54Mm59G5H_N8yMic1j55ZZHso3srql0ana72smn6Iw86wt7HH16Hi21tPAvFOrDAl5dO0s0A_k9PBXfaUK4K1TbT5EhkYzBq1kwvT5_YmB09qB-PdIk1jNYEhps0x2qtnXK4TQJ9ShUdLPD6O-0Xf5YiEsGZpwnIVfZpCBLoMUzXrcUG3URJqV2CkWmIYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a8de7f694.mp4?token=d1t43nH_TG4oLf1fITPpze68NaADQq2IeZMREBPLIO4K60vdwHqM5YRYdCURxt9L53oE-aiT5tb-icVlxDuxfXbu16zkfveH-F2JYyYlkYt-DPGxqj4lD2KSsRXuo7zQySNEMzkH5O6Ru7OkZ4unp68f54Mm59G5H_N8yMic1j55ZZHso3srql0ana72smn6Iw86wt7HH16Hi21tPAvFOrDAl5dO0s0A_k9PBXfaUK4K1TbT5EhkYzBq1kwvT5_YmB09qB-PdIk1jNYEhps0x2qtnXK4TQJ9ShUdLPD6O-0Xf5YiEsGZpwnIVfZpCBLoMUzXrcUG3URJqV2CkWmIYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة تهز الجليل الاعلى المحتل</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76457" target="_blank">📅 20:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76456">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e19000063.mp4?token=VWXA5Isz_uxH90KdeTYk7alaXUcukIA79HFHmO43OVhy86v6dh1lqK-1CT7uvmnrxatGiFFtCWUHeUtzcO0rkOn_dCA5um1ZNhncG7ERkUoY4WQVk-W_eFJs9KjdcrhcIpAd8zSmGPEpXZhb-qtstez_nOFmrDajawux8mWdzcXHt9dyalyQmgUfcNdEWeIyVKLMOwGzncnRL5JYD3QDzvXwwNYXqlyULN4PSOT3iAFPwjjEzY5gQWSh0TVvF6ofIi1DM3OCxIbaNvRSyukvI162z97LjaTGgqGCv5Z3XW-vq3JmjIg8SURuyMc5M91cG7RK6Fk3_7g8XqoIxmg_qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e19000063.mp4?token=VWXA5Isz_uxH90KdeTYk7alaXUcukIA79HFHmO43OVhy86v6dh1lqK-1CT7uvmnrxatGiFFtCWUHeUtzcO0rkOn_dCA5um1ZNhncG7ERkUoY4WQVk-W_eFJs9KjdcrhcIpAd8zSmGPEpXZhb-qtstez_nOFmrDajawux8mWdzcXHt9dyalyQmgUfcNdEWeIyVKLMOwGzncnRL5JYD3QDzvXwwNYXqlyULN4PSOT3iAFPwjjEzY5gQWSh0TVvF6ofIi1DM3OCxIbaNvRSyukvI162z97LjaTGgqGCv5Z3XW-vq3JmjIg8SURuyMc5M91cG7RK6Fk3_7g8XqoIxmg_qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
إطلاق رشقة صاروخية من لبنان نحو عمق الجليل في الشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/76456" target="_blank">📅 20:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76455">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1Q3Qf0ZAaklF2-xwTKxv66W1YRlKaKemoIDHbZ9UFi9bY0BoL2rRHWw86R-UFNZGVkvUfTIlFckRIo0N2ZysEhU67j9Nc5SGmdAQVV1F9MYaaL1gK-QwFDEngimNLjNK5EsNo8uU6RQmnH5fVI3uqcIaDPjylKPjKcY_pxH7iw0gQCXsGB9GAB2WckhXON1ValhZsQfc3MZYUH6W8nijyYN3k5sPW1XUdMX4aKP5caNNcHkQ9RbkbKIayfpDpWcg0hd2SJMNR_95V1Dxx-btUo8JOkQ8_V2o8y6zq6_4IkssRCYGLo_8eQ7Dn3EGWUHgf2vPwb0msHOYPvdN1HaQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
أفهم أن الفنانين يُعانون من "التوتر" فيما يتعلق بأدائهم يوم الأربعاء، لذا أفكر في جلب أكبر جاذبية في العالم، الرجل الذي يحصل على جمهور أكبر بكثير من إلفيس في ذروة مسيرته المهنية، ويفعل ذلك بدون غيتار، الرجل الذي يحب بلدنا أكثر من أي شخص آخر، والرجل الذي يقول البعض إنه أعظم رئيس في التاريخ (THE GOAT!)، دونالد ج. ترامب، ليحل محل هؤلاء "الفنانين" ذوي الأجور المرتفعة والمستوى المتوسط، وإلقاء خطابًا رئيسيًا، محفزًا البلاد للأمام كما فعلت منذ أن أصبحت رئيسًا!
قبل عامين، كانت الولايات المتحدة "ميتة". الآن لدينا البلد "الأكثر سخونة" في أي مكان في العالم. لا أريد ما يسمى "الفنانين" الذين يحصلون على أموال أكثر من اللازم، والذين ليسوا سعداء. أريد فقط أن أكون محاطًا بأشخاص سعداء، وأشخاص أذكياء، وأشخاص ناجحين، وأشخاص يعرفون كيف يفوزون.
لذلك، بنسخة من هذه الحقيقة، أأمر ممثلي ببحث جدوى إقامة تجمع "أمريكا عادت" يوم الأربعاء، واشنطن العاصمة، في نفس الوقت ونفس المكان. فقط الوطنيين العظماء مدعوون - سيكون احتفالًا مجنونًا وجميلًا بأمريكا!</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76455" target="_blank">📅 19:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76454">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🌟
إطلاق رشقة صاروخية من لبنان نحو عمق الجليل في الشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76454" target="_blank">📅 19:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76453">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇺🇸
‏
مسؤول أميركي:
إيقاف سفينة تجارية حاولت التوجه نحو ميناء إيراني ؛ ‏الناقلة "ليان ستار" تجاهلت تحذيرات قواتنا البحرية في خليج عمان.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/76453" target="_blank">📅 19:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76452">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
25-05-2026
غرفة قيادة تابعة لجيش العدو الإسرائيلي في ثكنة أفيفيم على الحدود اللبنانيّة الجنوبيّة بمحلّقة أبابيل الانقضاضية.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76452" target="_blank">📅 19:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76451">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XruwmDb9-wYSm29Mfa54L-tM2BKEEWdOlbilPrg4IC3mXiFYBUC2PaDZdrG6yQ69o5B5sizk2X2NjVtZYQFzk_KN2R3vZd3gkktIdjkReXOaPXK4V6LG0_FZgg5BxhefKNu-xOwi8eeqXNA56-4g1037ai-hMrphwOzubBbv8sJ-NSh9KwqGq1hq0coHVDyvlH1bZ6_M6SoQ1nesSGMWiKLSEQ6B_7Irmr2LPVVGjgQ0l2vmuEc06F2BsC5L3MIQ9zjjEcZKEZImNHS9XYaQi05-iPCPiJBVn8wbY_7O35g4NwhUvj57A-i9jJ9b0vJ98D_koC-0Lq3s7FOAq5Lkuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
قصف صهيوني بالقنابل الفسفورية المحرمة دولياً على بلدة ارنون بجنوب لبنان.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/76451" target="_blank">📅 18:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76450">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇷
مقر خاتم الأنبياء المركزي:
نظراً لأهمية سلامة هذا الممر المائي، يُشدد على ضرورة التزام جميع السفن، التجارية منها والناقلات، بالمرور عبر المسارات المحددة فقط، والحصول على تصريح من البحرية التابعة للحرس الثوري الإسلامي. وأي مخالفة لهذه اللوائح ستُعرّض أمن الملاحة للخطر الشديد. كما يُحذّر من أن أي عمل تقوم به السفن العسكرية للتدخل في إدارة مضيق هرمز أو تعطيل الملاحة سيُقابل بردود فعل عنيفة من القوات المسلحة للجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76450" target="_blank">📅 18:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76449">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف دبابتي ميركافا وقوة عسكرية تابعة لجيش الإحتلال الإسرائيلي في بلدة زوطر الشرقية بجنوب لبنان بعدد من الصواريخ الموجهة.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76449" target="_blank">📅 18:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76448">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b701e99bcc.mp4?token=XMO4zNeXmsQolPcg64Uuft2rKiOt3dz0T8ovi8AX3A_9K0RDZ_suJKtJivwl712MdpudWDrM-k10CU4IpFqWpz9LClZ_2d83JEwoiia5OP95UIOibGmjsahPVxnIG_uJ4vtcErpT_H8fQOc8mO7QF4GoHdNtFsNmM0jmmKOE3x1xJaoFViGPlQDXVMkgG9bLXt36WaSzKP2qTqc5tbEibdXG54iidmQjxIUv4uqP1w8TgHQDl1ctgd-DhOOT3_8Ba3S9dOMm7ohZjuTwayAst-xDqiC-ViefKDzufOCx5trxoxnPqE26bXbuOmrdJJzqNtbQeLOIqSuI8f11mmNRTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b701e99bcc.mp4?token=XMO4zNeXmsQolPcg64Uuft2rKiOt3dz0T8ovi8AX3A_9K0RDZ_suJKtJivwl712MdpudWDrM-k10CU4IpFqWpz9LClZ_2d83JEwoiia5OP95UIOibGmjsahPVxnIG_uJ4vtcErpT_H8fQOc8mO7QF4GoHdNtFsNmM0jmmKOE3x1xJaoFViGPlQDXVMkgG9bLXt36WaSzKP2qTqc5tbEibdXG54iidmQjxIUv4uqP1w8TgHQDl1ctgd-DhOOT3_8Ba3S9dOMm7ohZjuTwayAst-xDqiC-ViefKDzufOCx5trxoxnPqE26bXbuOmrdJJzqNtbQeLOIqSuI8f11mmNRTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
مشاهد تظهر تساقط الصواريخ التي اطلقها حزب الله على شواطئ نهاريا وهروب الصهاينة نحو الملاجئ.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76448" target="_blank">📅 18:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76447">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف دبابتي ميركافا وقوة عسكرية تابعة لجيش الإحتلال الإسرائيلي في بلدة زوطر الشرقية بجنوب لبنان بعدد من الصواريخ الموجهة.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/76447" target="_blank">📅 18:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76446">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1ecb8455d.mp4?token=KAbryvOy2N1tbrmKqrSpISI5ir7iu5IoFwXC09aroORmxy0II6p1NfMXtk2ShFxX4CPWCU_THKlm0IWb9CyUKG6LjkNeocCSz-fpaKndG2gnMk_M_FaDoPZeqIdAMQN8DwfJYcHMKic1rG6Sy2zbhWM2h9gy2NF_Kwz9oYN5ctVb0FNB9S0ubg37wz7xhe85ab_bQVJ9Y7T4mSUxcfDQFF7XJSqC-dAb-7GnbaX0OASCBjcElyMrPHb3Ntz4XHd3qOrWgTTsd-XXcGJ5zsEYQVzfeB6KvifTjIi-5HJs5lzo0HKliPOcayYrR8qwJfQCaUkQ9UWlAD0zquEMB_7774WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1ecb8455d.mp4?token=KAbryvOy2N1tbrmKqrSpISI5ir7iu5IoFwXC09aroORmxy0II6p1NfMXtk2ShFxX4CPWCU_THKlm0IWb9CyUKG6LjkNeocCSz-fpaKndG2gnMk_M_FaDoPZeqIdAMQN8DwfJYcHMKic1rG6Sy2zbhWM2h9gy2NF_Kwz9oYN5ctVb0FNB9S0ubg37wz7xhe85ab_bQVJ9Y7T4mSUxcfDQFF7XJSqC-dAb-7GnbaX0OASCBjcElyMrPHb3Ntz4XHd3qOrWgTTsd-XXcGJ5zsEYQVzfeB6KvifTjIi-5HJs5lzo0HKliPOcayYrR8qwJfQCaUkQ9UWlAD0zquEMB_7774WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
في الوقت الذي تنتشر فيه صور قادة إقليم كردستان في شوارع المحافظات العراقية بكل حرية، مُنع مواطن من دخول محافظة دهوك شمالي العراق بسبب وضعه صورًا للشهيد السيد علي الخامنئي والشهيد أبي مهدي المهندس على مركبته.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76446" target="_blank">📅 18:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76445">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca5e397810.mp4?token=Fdyi-YEPU2X2Eeo2ZT5EMqcceXdecRgFS0t6dlXzWlhLTV_9u8yP55saNwloqoHzvSPHvlNlNSr8fasdVeAer3mp7zg5-jPznldpInPpslYUv76k4izvndzogeUG7pxt0E72ssQ_oo1tB8CyDUIDfdivLKZczVMcF8IJFIGZ8u9My3Vx0IKsr0l4K_cObt8RQhxaU-tcWsLjLvan_rrw4mgBS3W7rjHXvTAe3h_BbzyHboGQUikWcgzyy27gMBFq_Lj44uACVkxH95kifXZZtNYUsLngAZAEZ_FEU07lUeW4VHAxUY_iece68LtzKgXNjYgBgoYwHZcA7RmL-fjY6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca5e397810.mp4?token=Fdyi-YEPU2X2Eeo2ZT5EMqcceXdecRgFS0t6dlXzWlhLTV_9u8yP55saNwloqoHzvSPHvlNlNSr8fasdVeAer3mp7zg5-jPznldpInPpslYUv76k4izvndzogeUG7pxt0E72ssQ_oo1tB8CyDUIDfdivLKZczVMcF8IJFIGZ8u9My3Vx0IKsr0l4K_cObt8RQhxaU-tcWsLjLvan_rrw4mgBS3W7rjHXvTAe3h_BbzyHboGQUikWcgzyy27gMBFq_Lj44uACVkxH95kifXZZtNYUsLngAZAEZ_FEU07lUeW4VHAxUY_iece68LtzKgXNjYgBgoYwHZcA7RmL-fjY6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
مشاهد تظهر تساقط الصواريخ التي اطلقها حزب الله على شواطئ نهاريا وهروب الصهاينة نحو الملاجئ.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76445" target="_blank">📅 17:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76444">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_9aN_mEsl3menJ9XhsV05q4aH3WsFP55HrJEJL-AKYicf9JuVJn6NhmsTij5DNa4YWphiFW0I6CokgYU1EOIuOmecO1A2RRVHKsa0YbBqZDkjzzIR0eVuiHVff2Ak8uQfhbSfoUZgb8C1GAZ26Kqqa5YSQhNksn3vosrI7JKDNhEbhpBnr0p8RzVpuiZpuRF0rQdKzUHXfkMKlcecuZxQd0T8zBq7RLbhwQ-a5iOCjvNHaWjpL-JCTtCHk4H_Z9EOcpSaa_TbOp0u0HSZpNpCF0X1ookS9G9FtdAFsTmQZqemTwM4LSv0Fml1FNokDRJbVI_NrE_La01rqgAvVjvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول خطوة عملية
لضم سرايا السلام للقوات الامنية ؛ الزيدي يلتقي ابو دعاء وتحسين الحميداوي</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76444" target="_blank">📅 16:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76443">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1476d1a303.mp4?token=ba-v2aFhij2WLNQbqvUye23D-Zxvo0JTHAZuj1K5PpuqfG0F1WfvSanQENjwUVbj9vali7EqqyxA_gVRXJgUsJ2hb2oAe6TKed0O4sqC4dllbmdKk0FZRuopv6FN6k-D3XwyahaWKoFIj1TJcf1ndQwoPNxjDJzHajTC7slLXnjZHO7SixCwE41AdUaSW6DFu9rIHc0M5va_BkjJiVFz0MDxul4ttlDNiHh5-JHRn6FH7NvxSw8ojKwXI7xtuwVtzMf5tNBrSBxRJuek4tTESbkZGyGVjhKEHL8aSPUN3QvTbWh3ApQi0f-Smu_wSlDgahDo1Iqhsgvzr0kcrZGjUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1476d1a303.mp4?token=ba-v2aFhij2WLNQbqvUye23D-Zxvo0JTHAZuj1K5PpuqfG0F1WfvSanQENjwUVbj9vali7EqqyxA_gVRXJgUsJ2hb2oAe6TKed0O4sqC4dllbmdKk0FZRuopv6FN6k-D3XwyahaWKoFIj1TJcf1ndQwoPNxjDJzHajTC7slLXnjZHO7SixCwE41AdUaSW6DFu9rIHc0M5va_BkjJiVFz0MDxul4ttlDNiHh5-JHRn6FH7NvxSw8ojKwXI7xtuwVtzMf5tNBrSBxRJuek4tTESbkZGyGVjhKEHL8aSPUN3QvTbWh3ApQi0f-Smu_wSlDgahDo1Iqhsgvzr0kcrZGjUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
انفجار طائرة بدون طيار اطلقها حزب الله قرب مستوطنة المطلة.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/76443" target="_blank">📅 15:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76442">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 27-05-2026 تجمّع آليات وجنود جيش العدو الإسرائيلي على أطراف بلدة زوطر الشرقية جنوبيّ لبنان بالصواريخ والقذائف المدفعيّة.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76442" target="_blank">📅 15:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76441">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇶
طيران حربي يجوب سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/76441" target="_blank">📅 15:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76440">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🌟
‏
مركز الأمن البحري العماني:
نحث السفن على توخي الحذر إثر رصد جسم عائم يشتبه بأنه لغم غرب منطقة المرور في هرمز.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76440" target="_blank">📅 15:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76439">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">#بالوثيقة
🌟
الاتحاد العراقي لكرة القدم يتهم رئيس الاتحاد السابق عدنان درجال بسرقة (500) الف دولار اهداها الحلبوسي للاعبين بعد التأهل لكأس العالم.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/76439" target="_blank">📅 15:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76438">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7kS68dBYywhuZ5E2AMNZ8B-B-Iqus-seGUMaQGQLRCf8dyLJIjueqpNzaj-bRLMON3fM3BIU_ziNEU5zpCK7RHur9nSQ_HPj0sPDyrHKuWsG_aM8ke8vpLubc5ISq3NeRrpNid6iwHaUhMCurHW2MzDLHJ8O5gr4hIBp3ID3Py7_xG0SRz4rXFFj3nbVmu63ngS882mTNkmeMb35eUGYW8R6xmu3H23Z85lhzjzMghM4iCZhZgRUX2aWwUNu1DV9kLzkgWEQuDCH2vFjcTNqIZv-fwRqhJhFnJ4IHIPopELIp3tC7sWLIPK4YKIz5CX7k0RVJa-_V0HJaToIoTZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوة خاصة تعتقل "عدنان محمد حمود الجميلي" وكيل وزارة النفط العراقية ومدير عام مصافي بيجي بتهم فساد</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/76438" target="_blank">📅 15:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76436">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmuAt5kzDVUpXqAN0jO3_GgS9ec8nAPzPbrqHzYQj4QAwuUgw-jS3uibtdeMi7HdCFdA5K5n7D2XNWAODDvRDUWkxB6uN2pTW6hPY-jr9ny28W9AzZGpnkPdoJqXEPjao8nE27X1WIxfK6ylLk-IO_FWBEBqgjotfMqeQJJDBJZPsqYOjqR-J8p6ySdcFFSFjgxRZEsSxQ6xVc1Yw0nZS4WcgU9CJTm51udKXgUOgiWz0wXpIqWabJJKD_C0ZlHA88mmphkcVfCGdVv8qUiuXIWSM8wIMWhj0FmowCxa-ThPdvLHK9MTsFuf8nRmw-IiL6H_ERtuO_KOETFWfeVWlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
فوز المرشح يونس محمود لرئاسة الاتحاد العراقي لكرة القدم.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76436" target="_blank">📅 15:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76435">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🏴‍☠️
إذاعة جيش العدو:
انفجرت محلّقة مفخخة في منطقة عسكرية في منطقة شوميراه</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76435" target="_blank">📅 14:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76434">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">قوة خاصة تعتقل "عدنان محمد حمود الجميلي" وكيل وزارة النفط العراقية ومدير عام مصافي بيجي بتهم فساد</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76434" target="_blank">📅 14:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76433">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇺🇦
زيلينسكي:
الجيش الأوكراني يضرب منشأة النفط الروسية في أرمافير، على بعد 500 كم من الحدود الأوكرانية</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76433" target="_blank">📅 14:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76432">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eO8ktW1p-3Ii4yPNfRxMZ7Sug61D9tU3q2qrx5Wj_wQ_wGIudEdcioZmN6FDKUpOac12DomjWL81B66q52xajhrPvdXSI_9dHWY41vHv5m-2gQ7MuyngJ9hxgzB6rtzpfQCznTXyC8GQGhjHPgpXdBw1CMXx5_VI7xv0wQ6vT7yaVjs--aKcOadOufFL16ows5oL7h2crxoZxlELh1gkAVm8BX7o81MEcIYD2Qd5A_7KhUPgxVv1uWDAMOxKPqDJm1g7rg1Kvr5hNOGzxpnEnUwvSfugoTSlM0fddW16exyCrgzM8NhoYhCJLJQIn0nv8O5vRx5yaCMMSexxowKiCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوة خاصة تعتقل "عدنان محمد حمود الجميلي" وكيل وزارة النفط العراقية ومدير عام مصافي بيجي بتهم فساد</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/76432" target="_blank">📅 14:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76430">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
انفجار محلّقة مفخخة قبل قليل داخل موقع عسكري مواجه لمستوطنة شلومي بالجليل الغربي وفي جنوب لبنان منذ ساعات الصباح هاجمت 5 محلّقات مفخخة
قوات الجيش الإسرائيلي
.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76430" target="_blank">📅 13:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76429">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇷
🇹🇷
اشتباكات عند الحدود الايرانية التركية بين القوات المسلحة الايرانية وارهابيين ؛ مقتل 2 إرهابيين وإصابة أخرين.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76429" target="_blank">📅 13:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76428">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">📰
صحيفة المونيتور عن مصدر استخباراتي إسرائيلي رفيع المستوى: كانت خطة إطاحة النظام الإيراني بالتعاون مع الكرد شاملة ومفصلة، الأميركيون كانوا على دراية تامة بالخطة لأنهم تلقوا إحاطة شاملة. الكرد كانوا متحمسين لتنفيذ العملية لكن واشنطن أوقفتها في اللحظة الأخيرة</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/76428" target="_blank">📅 13:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76427">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">📰
صحيفة المونيتور عن مصدر استخباراتي إسرائيلي رفيع المستوى:
كانت خطة إطاحة النظام الإيراني بالتعاون مع الكرد شاملة ومفصلة، الأميركيون كانوا على دراية تامة بالخطة لأنهم تلقوا إحاطة شاملة. الكرد كانوا متحمسين لتنفيذ العملية لكن واشنطن أوقفتها في اللحظة الأخيرة</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76427" target="_blank">📅 13:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76426">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⚔️
كتائب حزب الله : نرحب بكل خطوة يتخذها "  الأخوة غير المنخرطين "   بحصر السلاح بيد الدولة</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76426" target="_blank">📅 13:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76425">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⚔️
كتائب حزب الله : نرحب بكل خطوة يتخذها
"  الأخوة غير المنخرطين "
بحصر السلاح بيد الدولة</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76425" target="_blank">📅 13:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76424">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو مجاهد العساف</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_QtTJ_nByIT8JO_dwkRwf2IUxMzeZjR-HKskgUo_WCmOtFiGZZuh6TPbt-5OngoHYsO3e4l4CXGA8mdG5sNVKxFns61MiS5pTLslQgomcG83W0KNNjYCC7ZVDEhQyc3Gx8Y0kzIpJ8HVbDz3b62_fOJOvGYWsHmjnccB6egHgCN05S3o6eZhSwl_Nvxc_AaS66bXcNptXqioXlQt-zhj8vhHN0W49XpsUZg6sOfHA7OznOGpDZqLJtaC1xnfu3JYlcPRPlQuVigSemZekQpER7Irm3bTqc126mj1j43k7w-6VXELUxEtFz95QFxMmZV4HWbb1PmLj6SvZIwzXGiPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/76424" target="_blank">📅 12:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76423">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dfa76d18e.mp4?token=eusSkK8k2zeGquG23THDZbEkOQBtryawa_SE8X42mdlMyis9H2pNtlxzQZRpVt_US4DzkVv8DANXTLBqX5MeyxjGQWbvHNpgzsAUM0oZANQQRTR2ooXEJYcfNpeEZe-mNriO8vmYEOsabMzfiLJZ2dP-wYzQbmtO5XIuSdPBFlviMIV5eJUCY_fDu51P_pj9_Y2z-k7g63Ixth7WGx1eV6jG8wUuhQ6QtuamFnx8NtFAtvKn-jBxU1eUcT28EU5q0RWDSEXmduiCuSNxtLDNf_Byn52lQpQoyZTkXxuyN5KdjITWZzjNR0AgIbQ3qrpONdBIJEoQdLYR2OGzDypOplGd9VUpgg5kXJV0l8rQFuwdCWS5PUVwIHt0w_xtBAA79JB7R_7qp2qSRWosu4UY7mrLBEAvz7AdKEZVNgQqr5-GdAhRBYJ6-xRvMrYP2qgSIVOsjIMiJiVqV86t6_DkJ5zjK18bOvmCHRBNgbXlLQxpknZR7ftrhTSNenzD496V1QGkjRMvGLZDaBIrTOxYzRtUKGw1QZBF9w5Ai775yUdQ691TsIVJ2UmH46cwyweVZ9hePAFMCjj8x9HpBwVrwUHfg5i-ZZK08FCwC5N7vscRf0ZLODx-PbX1d5v5fbSlWjAyQLJ4i7GrmHNQl5TSRoQja7nfPO7zBxpL1F1u_Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dfa76d18e.mp4?token=eusSkK8k2zeGquG23THDZbEkOQBtryawa_SE8X42mdlMyis9H2pNtlxzQZRpVt_US4DzkVv8DANXTLBqX5MeyxjGQWbvHNpgzsAUM0oZANQQRTR2ooXEJYcfNpeEZe-mNriO8vmYEOsabMzfiLJZ2dP-wYzQbmtO5XIuSdPBFlviMIV5eJUCY_fDu51P_pj9_Y2z-k7g63Ixth7WGx1eV6jG8wUuhQ6QtuamFnx8NtFAtvKn-jBxU1eUcT28EU5q0RWDSEXmduiCuSNxtLDNf_Byn52lQpQoyZTkXxuyN5KdjITWZzjNR0AgIbQ3qrpONdBIJEoQdLYR2OGzDypOplGd9VUpgg5kXJV0l8rQFuwdCWS5PUVwIHt0w_xtBAA79JB7R_7qp2qSRWosu4UY7mrLBEAvz7AdKEZVNgQqr5-GdAhRBYJ6-xRvMrYP2qgSIVOsjIMiJiVqV86t6_DkJ5zjK18bOvmCHRBNgbXlLQxpknZR7ftrhTSNenzD496V1QGkjRMvGLZDaBIrTOxYzRtUKGw1QZBF9w5Ai775yUdQ691TsIVJ2UmH46cwyweVZ9hePAFMCjj8x9HpBwVrwUHfg5i-ZZK08FCwC5N7vscRf0ZLODx-PbX1d5v5fbSlWjAyQLJ4i7GrmHNQl5TSRoQja7nfPO7zBxpL1F1u_Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
شنت قوات زلينسكي الأوكرانية مدعومة بمعلومات من استخبارات الناتو هجوماً على مطار تاغانروغ العسكري ليلاً، مما أدى إلى تدمير منظومة صواريخ إسكندر الباليستية وطائرتين من طراز Tu-142 على الأرض.
‏
تدمير طائرتين من طراز Tu-142 في ليلة واحدة، وهذا يمثل ضربة قوية لروسيا:
‏تُعدّ طائرة Tu-142 طائرة دورية بحرية ومضادة للغواصات تعود إلى الحقبة السوفيتية، وهي مشتقة من قاذفة القنابل Tu-95 Bear. وقد استخدمتها روسيا بشكل أساسي للاستطلاع البحري بعيد المدى، ودوريات مكافحة الغواصات لتتبع تحركات غواصات الناتو، وحمل طوربيدات قادرة على حمل رؤوس نووية في بعض الأحيان.
‏الحقيقة هي أن روسيا لم يتبق لديها سوى عدد قليل جدًا من هذه الطائرات. فقد تقلص أسطول طائرات Tu-142 على مدى سنوات دون وجود بديل حديث قيد الإنتاج.
﻿</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76423" target="_blank">📅 12:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76422">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 27-05-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي على الأطراف الجنوبيّة لبلدة زوطر الشرقية جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76422" target="_blank">📅 12:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76421">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81bb9767dc.mp4?token=uxB9HZ4F42lsURTexFCoBbw9aQJQPSvlBbf1_X1jci8Sbj_1DDwnghxPc3NrwR-doqgS7eSFdSNwAmgsRY0Lq5UlqlcHWhtr2xHm5unLGeLlH9PppUhwKREk9G71C8lexLf1eOC2peGm5RI9cr4S8tbEBSixd0fS-0HPg-6IzzjEQ00tppCw0DprJek6c-Z5JEow13jI65j4KQ_OvMurQB02GFiIPbPnIsbfGqTIswkPm-NFwuTK8U-ZvuiQWKd7YyjYKHVfzrCbGR4rxTwDbfj4322-M20_BLLSI6VF4tkdWxq9H5r8IXWHU5Y273F3rqIkiqytwB5a9Ek-KEP0ggIvwXPh7uS8HTPDOieOiZIbW3J71TYvMZVIbRqa8ymDw2O-M5GifXbIpdERRXRbeJUk8iAWybFhR_OX-i_3JjSf4mORJPYV4JlElIlIVCVNYjRS9h9irvmJiM7S3z0BLBM_P9AwEtMgWCWpdL7ARZPh0338EuBNBp97coLg2i428A3mFQUR4iprBt9yV54z7c26DBbA_7Q42Ymhcmki_4QhTxh23KUBqiEnd3sPkjwyRmpZN-GwUwDZNwAnjtZioUlys6cB_ZkA6vbKxDNUPhtuA33VHvco_jNUq1dnuQVTwM0CwQn25JfMr8246XUoQBJ8gEEipx8za7BSNzlyi5k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81bb9767dc.mp4?token=uxB9HZ4F42lsURTexFCoBbw9aQJQPSvlBbf1_X1jci8Sbj_1DDwnghxPc3NrwR-doqgS7eSFdSNwAmgsRY0Lq5UlqlcHWhtr2xHm5unLGeLlH9PppUhwKREk9G71C8lexLf1eOC2peGm5RI9cr4S8tbEBSixd0fS-0HPg-6IzzjEQ00tppCw0DprJek6c-Z5JEow13jI65j4KQ_OvMurQB02GFiIPbPnIsbfGqTIswkPm-NFwuTK8U-ZvuiQWKd7YyjYKHVfzrCbGR4rxTwDbfj4322-M20_BLLSI6VF4tkdWxq9H5r8IXWHU5Y273F3rqIkiqytwB5a9Ek-KEP0ggIvwXPh7uS8HTPDOieOiZIbW3J71TYvMZVIbRqa8ymDw2O-M5GifXbIpdERRXRbeJUk8iAWybFhR_OX-i_3JjSf4mORJPYV4JlElIlIVCVNYjRS9h9irvmJiM7S3z0BLBM_P9AwEtMgWCWpdL7ARZPh0338EuBNBp97coLg2i428A3mFQUR4iprBt9yV54z7c26DBbA_7Q42Ymhcmki_4QhTxh23KUBqiEnd3sPkjwyRmpZN-GwUwDZNwAnjtZioUlys6cB_ZkA6vbKxDNUPhtuA33VHvco_jNUq1dnuQVTwM0CwQn25JfMr8246XUoQBJ8gEEipx8za7BSNzlyi5k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇸🇾
الانهيارات تصل إلى الحدود العراقية السورية.. انهيار جسر المراشدة _الباغوز بريف دير الزور الشرقي والمحاذية تماماً للعراق بسبب فيضان نهر الفرات.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76421" target="_blank">📅 12:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76420">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ول ستريت جورنال:
اشتكت السعودية للولايات المتحدة من أن هجمات الإمارات على إيران تزيد من خطر تعرض منشآت الطاقة الإقليمية لهجمات إيرانية. وطالبت السعودية الولايات المتحدة بالضغط على الإمارات لوقف الهجمات الانتقامية والانضمام إلى الجهود الدبلوماسية التي تبذلها دول المنطقة .</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76420" target="_blank">📅 11:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76419">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇩🇪
إغلاق مطار ميونيخ في ألمانيا بعد رصد مسيّرة</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76419" target="_blank">📅 11:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76418">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Homayoun Shajarian - Iran e Man (همایون شجریان و سهراب پورناظری…</div>
  <div class="tg-doc-extra">Melodifa</div>
</div>
<a href="https://t.me/naya_foriraq/76418" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#شاركها</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76418" target="_blank">📅 11:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76417">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
🇮🇷
أفادت وكالة بلومبيرغ بإصابة عدد من أفراد الجيش الأمريكي وتضرر طائرتين مسيرتين من طراز MQ-9 Reaper بشكل بالغ في قاعدة علي السالم الجوية الكويتية خلال هجوم إيراني وقع مطلع هذا الأسبوع. وذكرت القيادة المركزية الأمريكية (سنتكوم) أن الدفاعات الجوية الكويتية…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/76417" target="_blank">📅 11:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76416">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇺🇸
🇮🇷
أفادت وكالة بلومبيرغ بإصابة عدد من أفراد الجيش الأمريكي وتضرر طائرتين مسيرتين من طراز MQ-9 Reaper بشكل بالغ في قاعدة علي السالم الجوية الكويتية خلال هجوم إيراني وقع مطلع هذا الأسبوع. وذكرت القيادة المركزية الأمريكية (سنتكوم) أن الدفاعات الجوية الكويتية اعترضت صاروخاً كان يستهدف القاعدة في 27 مايو/أيار، إلا أن بلومبيرغ أفادت بأن شظايا من الصاروخ المعترض أصابت القاعدة.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76416" target="_blank">📅 11:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76415">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76415" target="_blank">📅 11:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76414">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🌟
حزب الله: فجرنا مسيّرة إسرائيليّة من نوع "هرمز  450 - زيك" في أجواء بلدة زوطر الشرقيّة بصاروخ أرض جو.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76414" target="_blank">📅 11:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76413">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92fdb1ed99.mp4?token=rhKY7TtzX1vQvWsOYJm387UJ5PauMghY6dLmBtTQ4me7t7IxXQAodqq9Zist2u33wAs2wNjMI4qV8jtuoPRK8kuRFXQOy9RvTGr6H1VrtWPRNG-gymZ6MTPX3-jm8rsQgpAMaeUjwz21U3hZRqZnojwKLVw2zKc4eb2HX2sHgxeEqXKB1Np8hZybrEreepL0daCBCLpfo9RvnXfE_Yg_XHEHQ4sblLEqSnWpYpI4IhIbrzIbdZTJ-rrcmhiFnv-vyDDz-6BLnh_LfTrCQjKUKScuc0L5xSSYSHFPTZ8yTrkJNj0afSMyXuo0NDF6HuYornZ4k6uyqPGvGIxfdMywEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92fdb1ed99.mp4?token=rhKY7TtzX1vQvWsOYJm387UJ5PauMghY6dLmBtTQ4me7t7IxXQAodqq9Zist2u33wAs2wNjMI4qV8jtuoPRK8kuRFXQOy9RvTGr6H1VrtWPRNG-gymZ6MTPX3-jm8rsQgpAMaeUjwz21U3hZRqZnojwKLVw2zKc4eb2HX2sHgxeEqXKB1Np8hZybrEreepL0daCBCLpfo9RvnXfE_Yg_XHEHQ4sblLEqSnWpYpI4IhIbrzIbdZTJ-rrcmhiFnv-vyDDz-6BLnh_LfTrCQjKUKScuc0L5xSSYSHFPTZ8yTrkJNj0afSMyXuo0NDF6HuYornZ4k6uyqPGvGIxfdMywEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">" سيوف بيد الزيدي "
ارتياح شعبي كبير في الشارع العراقي بعد أغنية الفنان حاتم العراقي بأغنية تتغنى بدولة رئيس الوزراء والإنجازات العظيمة المتحققة و التي عبر عنها مراقبون على انها سمفونية او معلقة او تشبه بخارطة طريق للخروج من بوتقة الأزمة السياسية التي تمر بالبلاد على أمل ان يخرج المارد من القمقم ويرجع العراق يصدر الكهرباء لدول الجوار  …</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76413" target="_blank">📅 10:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76412">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfFF513sH825lH8ttFageg04p5w-8PdejQhC0uVE2r3dBVIM6rqYAAjr2k_9FakNOksVNFhtuoSof3_ku7L2v-0qBocd57b-0xw8GpqZbofjn8ftfxOPA0r2vMlKlbiFVe-DvIkqy-ey6ADjHo6n3OgHAkk7FdmNDh7gFFZGhmFG9vs0YCj7GStQL61YUBca3uJHln4ycZ1uNLdRf0TMUJGUIDqWiLB4aEf18tHNlSnbacvb0D53WU84urHlfmkNjzj61pZxx6D24QLf_9w6cj5w98k2-OxXMddHO80kyniIOua3s-nsQ6nz0lQ5jYhQhjhs1fguCGOjSwOvo3mIWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏥
في حالة نادرة جداً.. ولادة طفل برأسين داخل مستشفى اليرموك بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/76412" target="_blank">📅 10:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76409">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UBl-UoeupuVimUO047c1NErd8TmRZ2bXtt57jp4Oa7yHFOX7UH0YWxlSAxyDleKmEsxCQBeBTVoT8iDUFDvFY3KB48Mx_TzAb4eM7MkPIXe-zfHw1SCrxdeVjQeb2flS34DpM9CZZPQZiZOgLkQI5yDS2rVEvihL44-Xcor1v01p0LULKxr6q576GEIhh9b9t2ihQ1w9bZ35cV6bBdqHjnIwpr4_OJJBTs4raKZcSN8YzMALS0EVe0tYIGBbTbfROMZ7-o3mjWUPIGQ5u-h_lWhLd8jM5QtBeak7HRKc4na-j3YnJSA2kiUcbluNsBeh_34kKrDolv5XF_8FZBML1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X7URDggGEaQLonAMKCCiYIZgvlXPLVtz-cVIvfGY7MeHR9H6K7DRGCl7y7oFSDd-EHnjEiolvwalnXPZyjvzeT67rsYxlNMozHPAsqDmmT9g6Qs0cTpts4_sBrm4qC-M6BEqR4I7dUikUYP_gklXgHsy7ofEO-7cEheUjPArf5M-S3yZEcFKOgzo32OAwFM23uvF5YuX2gi9zzDeIqHaMpwYEP2k4ulgUAnIxoPNnJ7msOX5rw-O3Peea-8hLmTd5lNCnfIl6NXv-ZPNNQ08Oj_U6cnd9dZwFaAnnjtDLwl-jQ45Sa8p-Z1TgeGLriofoaEQeknAY2K76_i9IdO4Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UydUDm5CHtL09T7p9NzTIcXJgrru2s4yGqpazUHwLQu1QLA11aT5wo86kyWyCemmdYE6BwDIYRECl2HYsX9ca2jf2iOOTMymvag1ryRYrG2ojFSkK1woIPgivmRIXPBM8a_Xo2s5M9S2ZJyvRg89Tby1Hq44-yW_HEaZ6x_SidhQTUihpoEDV_BJzEIwZNEtq-i2VIQCetBK-QBN_dhBtc4qGCLf1WREaoDe0yLFGp8WT9QjgADKzfnqM21yWi3JlzdFAdMjA5nKABx6HZ2hn6AOU0jbk-hscp_4gofnVxsabGtVxKb7-c2I8Xe8ZBMPnu711jXdKhCSaLrb67e3sw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
أصدر البيت الأبيض أحدث تقرير للفحص البدني الذي خضع له ترامب.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76409" target="_blank">📅 09:59 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
