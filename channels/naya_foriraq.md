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
<img src="https://cdn4.telesco.pe/file/JnnyQkrRsvSzmDSq3Yg4SZ2waZAhmPUCKbSB-GByg5_h1fM3AbpLE0W69bFXxwtC-qBcr3Yu7krB38k5q6u-BKxKaHkpfm6vp4y9miekcmSGlEojIf6pEm3vzYRDLw-n1axQ-r3LvgxEZ0hVJdTsLT2Dnl7E-V6vhBjh4PzTTpt4lP1Fd7UCWkM1VD67a3zW0IuvYByI1KVAXk8bECbsMUbvpER2NC3qoM7N5iVL_WDqh0JXmDYr45wB1pr8zeAg0zn41DSK3u4HKm-WPQlmMJVGjt4yiaQMaFl_lWWgOD-jTugRt90cJKkbjgIOo2f5Q_DaU2txLegRZ6UpC1lAPg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 266K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 01:50:47</div>
<hr>

<div class="tg-post" id="msg-91303">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c6dca259.mp4?token=RkiFcmq9UBFG3u1yDMQVyZonwKKWqB7qYI5gfAmwcftjN1ombs6tFB6GkU4z9hrHkBV4gzsq7p54yF9u8LtJGXwS4EmO5xj-LXkTSQ8CDQE23ZT1kzPKxvNqqL3GS1eykhu2kiwyV2fvRLdlsNxtXYjD18284VvjX5bI-novCp_DPZ1mcD_h7_Cvjppc5OH20OQfGFDxZgWWO4Jf85phAJM9Hh3fcLIyssLnHc5W192Y8VGaO3G_SBghYcBWR5xvGYkt1Zc1QvIqJFmut63d6-rP4ipJHnatGk9f8aOyc4W2H6pLNY2Qg08_U5U7aYeW7UrGsCx721ejign53eiHkiEhzre45dbqqcL1XeNx6dtUzhlaR3nOJy51_CgAYkdA5E9u0qwpczlHw8XyaEyyT_muG32OCbHym6-0xkha-96GHpeh0Ak4dLPbPv_78Qdo6I__qUeO1aXU02xPVjCKBvGkY1RYjOpggnm-pUSPREYa2EOHyFAE9eAkd8G50_aj5Xt9h5APIsmmBDV7eWZjhvN6uJS3wL1PhP_KmF0sK2LSmGiYNFhIpV-5to4rbQTvkrUozsHapl8DFnQkQRCH4W7nWHfri26KXDT2IAnjw-j-U41BOuvo98IBc2sBKBMycqO_VAl9Y717s0C1UTWDCLiEKC51ls0yBXAYsyf2whQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c6dca259.mp4?token=RkiFcmq9UBFG3u1yDMQVyZonwKKWqB7qYI5gfAmwcftjN1ombs6tFB6GkU4z9hrHkBV4gzsq7p54yF9u8LtJGXwS4EmO5xj-LXkTSQ8CDQE23ZT1kzPKxvNqqL3GS1eykhu2kiwyV2fvRLdlsNxtXYjD18284VvjX5bI-novCp_DPZ1mcD_h7_Cvjppc5OH20OQfGFDxZgWWO4Jf85phAJM9Hh3fcLIyssLnHc5W192Y8VGaO3G_SBghYcBWR5xvGYkt1Zc1QvIqJFmut63d6-rP4ipJHnatGk9f8aOyc4W2H6pLNY2Qg08_U5U7aYeW7UrGsCx721ejign53eiHkiEhzre45dbqqcL1XeNx6dtUzhlaR3nOJy51_CgAYkdA5E9u0qwpczlHw8XyaEyyT_muG32OCbHym6-0xkha-96GHpeh0Ak4dLPbPv_78Qdo6I__qUeO1aXU02xPVjCKBvGkY1RYjOpggnm-pUSPREYa2EOHyFAE9eAkd8G50_aj5Xt9h5APIsmmBDV7eWZjhvN6uJS3wL1PhP_KmF0sK2LSmGiYNFhIpV-5to4rbQTvkrUozsHapl8DFnQkQRCH4W7nWHfri26KXDT2IAnjw-j-U41BOuvo98IBc2sBKBMycqO_VAl9Y717s0C1UTWDCLiEKC51ls0yBXAYsyf2whQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇸🇾
الجولاني يكشر انيابه:
الجولان هي أراضٍ سورية تقع تحت اعتراف الأمم المتحدة. لا يوجد أي نقاش حول هذه الأراضي ومن هي الجهة التي تملكها.
والقنيطرة ودرعا وريف دمشق والسويداء؟؟؟
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 793 · <a href="https://t.me/naya_foriraq/91303" target="_blank">📅 01:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91302">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPeS3HgA_svLKLJOkLCPOz10EYkBv6zxQCtoYBsMZSXzoSbP8iAeerpuS9fIKUn1Lvkiinjc7UZkPku5zvOvM-HCT0nuyNqry_ZQnA0MISYBhg0TrrQv6fWzoO5UNsv3PTlbQ9eYNzMhpJBvlQIMgWNnhPWSxNsxOwz2jeTvbDVmMUxR-GQFmH27pqQndEvaYV5cIr83b5gbYz9M89Z7kaDWT_rn0GsY8K4QYM6QntYvC95erTEHEcEgIsifqzmW4PuaPtqpfZfYzVVBrJUt9mIBL8GMG2v0aU8QOB1Vi_6zxRVg_7VdvZ5qQVMm07mM7f1qphkC9BGbAPTq8SHFyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انصحك راجع التاريخ واتمعن بماضـــــيه
مطارك ياهو حول بيه بيام الكفائــــــــيه
شلون ترد الزاير شتگل للعباس</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/naya_foriraq/91302" target="_blank">📅 01:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91301">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔻
إشتباكات صاروخية بالقرب من مضيق هرمز.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/naya_foriraq/91301" target="_blank">📅 01:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91300">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOIoGn3e35biJ8up9KZ2Len7ku0XnpVIpx6QnSOs7INR1NkSO4V0TdH-yrQ14bsUPI6iIiG3_mKjW34BXS7HwbeYzS-w0Dbg7HY6yOgrYWn-eU6BlkhDUuhtrI8CpbYTpkhWc7WPZaXhIoOTPIa0VdlAg6lAqZcnZYtswdqmjqSvqU1Lk3p-zJ6cshn-IYcrojDjKZLU7jnZsQBhGhwXiQ4Hp24UZqfCLM1N-NmANsQh77pzhK-3yT7SxNdtrUwORid_rRqKda6KbbLfPDJMoOtEkC9OwaKCcFTPP4CFDYtx6o275ergR3b-Kne-MTkMeXyqLEVCxN71qGC-1TrWVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اسعار النفط تنخفض لتصل الى 97 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/naya_foriraq/91300" target="_blank">📅 01:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91299">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔻
إشتباكات صاروخية بالقرب من مضيق هرمز.</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/naya_foriraq/91299" target="_blank">📅 01:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91298">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇶
خلية الاعلام الامني العراقي:
مناقشة تسليم السيطرات الأمنية في المحافظات المذكورة إلى قوات وزارة الداخلية وخروج قوات الجيش والحشد الشعبي من داخل المدن وفق ترتيبات وآليات يجري تحديد تفاصيلها بما يضمن انسيابية العمل الأمني واستمرار حفظ الأمن.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/91298" target="_blank">📅 00:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91297">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇺🇸
شرطة نيويورك:
تم فحص الطرد الذي يوجد امام مبنى الامم المتحدة والتأكد من عدم وجود أي شبهة جنائية في مدينة نيويورك.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/91297" target="_blank">📅 00:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91296">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f63dc50f21.mp4?token=Q49dVKnm_NWsWgLyKb2MXabhfVUsq9TdRkNpJmxj0Gk6tZqREzl8Y-MdTe5C8NdFPZ6QXPh88Ztx25MKfIWufOPEvklGqnxaZifJjr87sphx8-__9Se6c8Ynq65i8do-9vhTJaArs3QWZMc3kmqIqCr40LaBnk3O7G4eNEqWPfEce5JzuacAQIkgSn7azOVidljRzORBMcyV_xQDBTJrXTdHV-1vD90_BJxpJQt4WtdJU-ama0HuAqWkvehKl8WlqBH6DdLaDCbxJeFr56bETtN4byQZ_DP8moUqpyL285oaJZh3X8KbpY2A-BqixVNMzWt01iKrxiZwHoeDK7D2hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f63dc50f21.mp4?token=Q49dVKnm_NWsWgLyKb2MXabhfVUsq9TdRkNpJmxj0Gk6tZqREzl8Y-MdTe5C8NdFPZ6QXPh88Ztx25MKfIWufOPEvklGqnxaZifJjr87sphx8-__9Se6c8Ynq65i8do-9vhTJaArs3QWZMc3kmqIqCr40LaBnk3O7G4eNEqWPfEce5JzuacAQIkgSn7azOVidljRzORBMcyV_xQDBTJrXTdHV-1vD90_BJxpJQt4WtdJU-ama0HuAqWkvehKl8WlqBH6DdLaDCbxJeFr56bETtN4byQZ_DP8moUqpyL285oaJZh3X8KbpY2A-BqixVNMzWt01iKrxiZwHoeDK7D2hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
الاعلام السعودي ينشر:
علموا أولادكم أننا أقدم دولة في الشرق الأوسط.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/91296" target="_blank">📅 23:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91295">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇱
اعلام العدو:
تفعيل انذار امني قرب الحدود الاردنية خوفا من عملية تسلل نحو الاراضي الفلسطينة المحتلة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/91295" target="_blank">📅 23:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91294">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇶
وزارة النفط العراقية:
كمية النفط المصدرة في شهر آب وصلت إلى 70 مليون برميل.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/91294" target="_blank">📅 23:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91293">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇷
مقر خاتم الأنبياء المركزي:
إن التصريحات العدائية والتهديدات المتكررة التي يطلقها رئيس الولايات المتحدة الأمريكية ضد إيران، والتي تأتي في سياق استغلال منبر الأمم المتحدة لتبرير العدوان وخلق حالة من عدم الاستقرار والنهب في العالم، هي في الواقع مجرد أداة للدعاية الداخلية، ولا تستند إلى حقائق ميدانية.
إن هذه التصريحات تعكس الجمود الاستراتيجي للولايات المتحدة في عدوانها ضد الشعب الإيراني.
إن تكرار الادعاءات والتهديدات التي لا أساس لها، في ظل تدهور الجيش الأمريكي، ليس دليلًا على القوة، بل هو دليل على اليأس الاستراتيجي.
إيران الإسلامية لطالما كانت ركيزة الأمن في المنطقة، وخاصة بالنسبة للتجارة الحرة والدولية؛ في حين أن الولايات المتحدة، بحضورها غير المشروع وغير القانوني والمتجاوز في منطقة غرب آسيا، هي مصدر تهديد وعدم استقرار. وتسعى، لتعويض سلسلة الهزائم المتتالية في أعمالها العدوانية ضد إيران والنهب البحري، إلى أسر الاقتصاد العالمي.
إن خطاب رئيس الولايات المتحدة الأمريكية لا يغير حسابات القوة، ولن يعوض أبدًا مكانة هذا البلد المتدهورة في النظام العالمي الجديد، ولا الهزائم المهينة التي تكبدتها الولايات المتحدة في الحرب ضد إيران وجبهة المقاومة.
إن القوات المسلحة القوية والفعالة في إيران الإسلامية، التي تستفيد من تجارب الدفاع المقدس في الحرب الثمانية سنوات والحربين المفروضتين، مستعدة تمامًا لتقديم ضربات أقوى وأكثر تدميرًا وغير متوقعة للمعتدين وقادة الولايات المتحدة وإسرائيل.
إن شاء الله، سيقوم رئيس الجمهورية الإسلامية الإيرانية بنقل رسالة الشعب الشجاع والقوات المسلحة البطلة وقوة إيران التي لا تقهر إلى العالم في منتدى الأمم المتحدة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/91293" target="_blank">📅 23:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91292">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/91292" target="_blank">📅 23:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91291">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVO8OsfUlSndAg_lWVRr2rkULJIADXE28Bx8PV8q71zcpQtmIsvmcwNJNcOsz0I7WQtCAi3K4jxRXKnRifIPSZx4YklUPfevRx1Cd8NpGOtc1YP6RiAs-B5jYpAMOZz-yTjSCWZeNjd_Do_ChrRYskudr2rnhgj-H2n-FKuLYQT2MTtBi93fj3UCxoQydZSa194u_eu2OAZ3o6Yxd8vHteICLLh8iwFsoLmqfSJ5IGrmhPfcdIH5Gfo9j-vFGws1yZUBVuprTWd2v1knOI2ltFuGAwTt2FRIFXyFakP2OBro8nalgjOx_nO5HN9r4HAsMryeVCrLD6Qtb0T0LTm2iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
جمهورنا الكريم
...
🔻
لغرض التواصل معنا ونقل مشاكلكم وارسال الاخبار والمواد الصورية والفديوات ، سنكون على مدار الساعة معكم نجيبكم.
للمراسلة
@Nayaforiraq_bot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/91291" target="_blank">📅 23:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91290">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c14b8577.mp4?token=GXdBy9ntOxBfyU7JIyM8_UtecT9gHQ9kc4l63VhMfPL6lVwTY2a8Cu_A6htu1t828qpvDaX8EYIopMcFpL172Hgr3BXQ7jyQspKnT16uksvY-okN7T5RgiYY0L07PolIMzjL5foAw-tzWhRfJ5p5qFM6GOORH4KnDkN_2lF6C4UvobfmQWFZsNm9yqFCu_uPYh45XJ6KoT5ybl1nmz4LahuDUDyMBHPdr3Sccx5zmiHTv-ss-QWZVKmkeakorBdGYD7m01CLgxdU5KQrQXsNCjbn6_Tciwxu5SHNGea87MGFsYoELQPhaYrzz0AWoEOUfNP-ZN-rb5JN1Qe8YVgm0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c14b8577.mp4?token=GXdBy9ntOxBfyU7JIyM8_UtecT9gHQ9kc4l63VhMfPL6lVwTY2a8Cu_A6htu1t828qpvDaX8EYIopMcFpL172Hgr3BXQ7jyQspKnT16uksvY-okN7T5RgiYY0L07PolIMzjL5foAw-tzWhRfJ5p5qFM6GOORH4KnDkN_2lF6C4UvobfmQWFZsNm9yqFCu_uPYh45XJ6KoT5ybl1nmz4LahuDUDyMBHPdr3Sccx5zmiHTv-ss-QWZVKmkeakorBdGYD7m01CLgxdU5KQrQXsNCjbn6_Tciwxu5SHNGea87MGFsYoELQPhaYrzz0AWoEOUfNP-ZN-rb5JN1Qe8YVgm0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
التلفزيون الايراني: إبلاغ شروط إيران لفتح مضيق هرمز كان السبب في قبول طلب فيتكاف لعقد هذا الاجتماع.  تم إبلاغ الموقف الإيراني القاطع لممثل الولايات المتحدة خلال هذا الاجتماع.  رفع الحصار البحري بشكل فوري، وسداد جميع الأموال المجمدة لإيران بشكل فوري، وإنهاء…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/91290" target="_blank">📅 23:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91289">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇺🇸
ترامب: مسؤولون أمريكيون اجتمعوا مع وفد إيراني في وقت سابق لمدة ثلاث ساعات، كان الاجتماع مع إيران مثمرًا جدًا، ومن المقرر عقد اجتماع آخر في المستقبل القريب.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/91289" target="_blank">📅 22:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91288">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">#هام
النجباء تهدّد مبعوثَ ترامب:
🔻
ستحمل مشروعَ نزع السلاح معك إلى القبر!
Al-Nujaba Threatens Trump’s Envoy:
🎬
You will take your disarmament project to the grave
‼️
Message from the Iraqi Resistance to Tom Barrack: You and your boss, Donald Trump, should realize that Iraq is not the Plaza Hotel</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/91288" target="_blank">📅 22:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91287">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔻
من أُحد إلى علي الطاهر
قد تتغيّر الوجوه، وتتبدّل ساحات المواجهة،
لكن الطريق واحد: أن تبقى واقفًا حين يريدك الجميع أن تنكسر.
من بين الغبار والركام، ومن قلب كل امتحانٍ قاسٍ، يولد الثبات من جديد.
ليس لأن الطريق سهل، بل لأن التراجع ليس قدرًا.
﴿فَاسْتَقِمْ كَمَا أُمِرْتَ وَمَنْ تَابَ مَعَكَ وَلَا تَطْغَوْا ۚ إِنَّهُ بِمَا تَعْمَلُونَ بَصِيرٌ﴾
🔻
انتاج نايا على التلغرام
#حسن_مات_كالحسين</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/91287" target="_blank">📅 21:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91286">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇺🇸
ترامب: مسؤولون أمريكيون اجتمعوا مع وفد إيراني في وقت سابق لمدة ثلاث ساعات، كان الاجتماع مع إيران مثمرًا جدًا، ومن المقرر عقد اجتماع آخر في المستقبل القريب.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/91286" target="_blank">📅 21:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91285">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇺🇸
ترامب
: مسؤولون أمريكيون اجتمعوا مع وفد إيراني في وقت سابق لمدة ثلاث ساعات، كان الاجتماع مع إيران مثمرًا جدًا، ومن المقرر عقد اجتماع آخر في المستقبل القريب.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91285" target="_blank">📅 21:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91284">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏
🇺🇸
جيش الاحتلال الأميركي ينشر صورة لمنظومة فالانكس للدفاع الجوي بالشرق الأوسط.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91284" target="_blank">📅 21:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91283">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇶
انفجار عبوة محلية الصنع امام احد المنازل في محافظة ذي قار جنوبي العراق.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/91283" target="_blank">📅 21:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91282">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igpJCR6bT--jmM9cKGwwQ9MZwCdNwQ_mYePfKEsZ31yopnRPBv3_b_YcDbb-eyUVHT3x8xlK-RfltjMM-ZkX806sG3RbKhUDjhuoFSyugqV6K974UxJtxFBKaGgbfEiG50hY6zCEVlN72KrQEGuy6b-IfKiuQe5xkul1PvlorD1MTw6ClPi191tOkOXCJIqqkYCdE8wq3uGw2LIfFKuc8sC4nvVsaIii6KLQfLAYPT1w79Ngp1bKMKprdR_3NM-A0h1DHjuSTSwODg8UtI3NdYDw1_jOoVbPRpMFgpdLKSN6bqdYB-hzx-5C86bmeeLLMT2_Ly81A0cjlsE006FL4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
المتحدث بأسم المقاومة الاسلامية كتائب سيد الشهداء:
هل غلق المطارات امام الطيران الايراني يشبه منع الماء عن عيال الحسین ع ؟!!!!
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91282" target="_blank">📅 20:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91281">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇺🇸
🇮🇶
المبعوث الاميركي:
نزع سلاح الفصائل أمر مهم للعراق والعراقيين.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91281" target="_blank">📅 20:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91280">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f3ddfe5aa.mp4?token=pIGC3KHxOBNmo01uO_7UnA99Cnr8btdMzWjxvwECySdV0kyLmMII7SCeYp2OwqH9pdHtFLFwATGeGAkAxj8y9VOOa5uW2bMmgqn1T_ewjKsNVI-cIB5j4XAATgNjvZ7hiQgNR_QZsaRl1lEOvQnf1sMm5_UjOIFCRx9srUdxIYARB3jHAHauEmcJoepfSgItSn7VP5b_y0zU1NygMh_OfqH341TA-q0uIne2F_gsVCP4_5oMdjYuW2Y8KsJobR8vTfskGlfmHz40w9Rmw6gDDCthu26dtzY1V3fDNaW73ByezZ9f5i_94OAHjS_IYvxlU1ReTJWz9tOT1TNP2nGglw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f3ddfe5aa.mp4?token=pIGC3KHxOBNmo01uO_7UnA99Cnr8btdMzWjxvwECySdV0kyLmMII7SCeYp2OwqH9pdHtFLFwATGeGAkAxj8y9VOOa5uW2bMmgqn1T_ewjKsNVI-cIB5j4XAATgNjvZ7hiQgNR_QZsaRl1lEOvQnf1sMm5_UjOIFCRx9srUdxIYARB3jHAHauEmcJoepfSgItSn7VP5b_y0zU1NygMh_OfqH341TA-q0uIne2F_gsVCP4_5oMdjYuW2Y8KsJobR8vTfskGlfmHz40w9Rmw6gDDCthu26dtzY1V3fDNaW73ByezZ9f5i_94OAHjS_IYvxlU1ReTJWz9tOT1TNP2nGglw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇸🇾
أثناء كلمة أردوغان مؤسس سوريا الجديدة، يظهر فيديو مصور أن الجولاني يتجاهل كلمة مؤسس دولته وهو يتصفح الإنستغرام.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/91280" target="_blank">📅 20:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91279">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17fea0ab54.mp4?token=EL77gK8gN7KtZqWE0XVoGlTpS4MIAmT_AInYgsekcEhT2DgR2cB-xLJPNQn0wKShVMJdlIC1vsm3V9nntlx8BsrdwjYfNl9ukDbHSW95nFBUlqfdnVF5g2MAZkScKP3VLCIWAlBw6ScZvmys4n4gOA33EEbkU3nqXQqbQ5gWPGsFjTrtSKETDcPF8Iv3hD41SbimjCdVQbP3X7itj4GIbDaod6HaxpZuMpkLsbqLhAwdCf_fQ35F5djeJfJmP19ZLxecy7aF_ypM54FE58Sg3wKJsgsB79WLQF2Tj3J1v6i132zvTAMijtLbxpfV0HkbKS6mogeX5wpfqTe7EEQ_dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17fea0ab54.mp4?token=EL77gK8gN7KtZqWE0XVoGlTpS4MIAmT_AInYgsekcEhT2DgR2cB-xLJPNQn0wKShVMJdlIC1vsm3V9nntlx8BsrdwjYfNl9ukDbHSW95nFBUlqfdnVF5g2MAZkScKP3VLCIWAlBw6ScZvmys4n4gOA33EEbkU3nqXQqbQ5gWPGsFjTrtSKETDcPF8Iv3hD41SbimjCdVQbP3X7itj4GIbDaod6HaxpZuMpkLsbqLhAwdCf_fQ35F5djeJfJmP19ZLxecy7aF_ypM54FE58Sg3wKJsgsB79WLQF2Tj3J1v6i132zvTAMijtLbxpfV0HkbKS6mogeX5wpfqTe7EEQ_dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
‏بريطانيا تستدعي القائم بالأعمال الإسرائيلي بسبب المشروع الاستيطاني E1، وتعلن أنها ستفرض عقوبات ردا على التوسع الاستيطاني الإسرائيلي.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/91279" target="_blank">📅 20:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91278">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇱
🇸🇾
جيش العدو الاسرائيلي:
قبل قليل وصل 14 مواطنًا إسرائيليًا إلى منطقة ألوني هباشان واجتازوا الحدود إلى داخل الأراضي السورية.
مو مشان شي مشان صحتك يا غالي
😆
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91278" target="_blank">📅 20:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91277">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامب: سنبني قاعدتين عسكريتين رئيسيتين في غرينلاند</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/91277" target="_blank">📅 20:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91275">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
‏
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 19 غارة جوية من خلال طائرات "F15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف، استهدفت محافظات تعز والجوف ومأرب وخلفت شهداء وجرحى بينهم أطفال ونساء ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد على بلدِنا العزيز 936 غارةً وصاروخاً.
‏إن المجازر التي ارتكبها العدو السعودي المجرم بحق أبناء شعبنا ستكون عواقبها عليه وخيمة بإذن الله وقوته.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91275" target="_blank">📅 20:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91274">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
المتحدث باسم لجنة الأمن القومي في البرلمان الايراني:
السفن المخالفة التي تعبر مضيق هرمز ستواجه بالإضافة إلى دفع غرامة تعادل 20% من قيمة حمولتها- إجراءً يقضي بالحجز المؤقت على السفينة لحين سداد الغرامة.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91274" target="_blank">📅 19:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91273">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">الولايات المتحدة والدنمارك وغرينلاند يوقعان اتفاقية بخصوص غرينلاند بدون تاريخ انتهاء</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/91273" target="_blank">📅 19:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91272">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇱
بن غفير:
خطتي لمنصب وزير الأمن تشمل تشجيع "الهجرة الطوعية" لسكان قطاع غزة واعتقال قيادات السلطة الفلسطينية داعمة الإرهاب ونزع سلاح السلطة الفلسطينية وتغيير تعليمات إطلاق النار ودعم الجنود ورفع رواتبهم ومنحهم أراضي مجانا.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91272" target="_blank">📅 19:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91271">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">غرق سفينة كانت تقل شباب اكراد عراقيين من مدينة رانية في البحر الأبيض المتوسط كانوا يحاولون الوصول الى اوروبا بسبب تردي الوضع الاقتصادي في اقليم كردستان</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91271" target="_blank">📅 19:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91270">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">غرق سفينة كانت تقل شباب اكراد عراقيين من مدينة رانية في البحر الأبيض المتوسط كانوا يحاولون الوصول الى اوروبا بسبب تردي الوضع الاقتصادي في اقليم كردستان</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/91270" target="_blank">📅 19:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91269">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الملك الاردني: إذا كان لدى أي شخص أدنى شك في أن الأزمة في منطقتنا تظل محصورة فيها فما عليه سوى النظر إلى فواتير الطاقة والمواد الغذائية للأسر العادية في مختلف بقاع العالم</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91269" target="_blank">📅 18:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91268">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇶
اليابان تخفض مستوى تحذير السفر إلى 9 محافظات عراقية.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/91268" target="_blank">📅 18:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91267">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cdd28462e.mp4?token=f7-coSM_GOHTalqSWfg5uUYmyRMdGZYVL9LYBsD9QbiitT1s33fn2MLzUG4XpJ7pLXpu8a_K0fIcaNf3o9jBDLDbEhSaTXKdzsievGafajnGR7eh3n1WQZhamnb2iblMl2gkUcwsc0o7F_ucFhd4ri9zTVL4GiwWWfh2LLB_dLd2iWAcvVGMSa3sjjn_LFY0tgaXWRMpRfHHDohwMZrKqz-kJehOHleopDqNBgc3AqxtFxTU8drAgQi-miv_6jsDAceujkHqWM6IZmYJII8DofGSrxIqVRnr6rYlUmC-InvkEeFZQs6P7ofW4ut72eTFBSPGl-gAgoRwaPMG1bsiral4JwTwlm5-NLVA0FfPCFLoTwjFaMM11vlX78heyeFUFaFMfz4uT2YocHI_NMW-YwQ0yR6SDibZNBoWxkUOu9bwumAZ47a-QwLg0qgzUlUMyQxSeMwjm3rRoAtxfh8TCZhMbKq3xrVKjMvWfu0yZRapbuCdRFdwAntPwNL-ONEo9k_WFiGxMDXdJSW1_AQX77Kdld-x7OH27BWZNJovpwK1mFeswp56a-S4gPkQsZ_bTKrKHKVBujHqe2-XOktjCplQqVaHNRlHIDvpNtkzBi45XazOkyGyNE7l4d5jXBzgppdkchEN915NYNpAKlMiHEKiSLrR-T4wjYyNBgCYtic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cdd28462e.mp4?token=f7-coSM_GOHTalqSWfg5uUYmyRMdGZYVL9LYBsD9QbiitT1s33fn2MLzUG4XpJ7pLXpu8a_K0fIcaNf3o9jBDLDbEhSaTXKdzsievGafajnGR7eh3n1WQZhamnb2iblMl2gkUcwsc0o7F_ucFhd4ri9zTVL4GiwWWfh2LLB_dLd2iWAcvVGMSa3sjjn_LFY0tgaXWRMpRfHHDohwMZrKqz-kJehOHleopDqNBgc3AqxtFxTU8drAgQi-miv_6jsDAceujkHqWM6IZmYJII8DofGSrxIqVRnr6rYlUmC-InvkEeFZQs6P7ofW4ut72eTFBSPGl-gAgoRwaPMG1bsiral4JwTwlm5-NLVA0FfPCFLoTwjFaMM11vlX78heyeFUFaFMfz4uT2YocHI_NMW-YwQ0yR6SDibZNBoWxkUOu9bwumAZ47a-QwLg0qgzUlUMyQxSeMwjm3rRoAtxfh8TCZhMbKq3xrVKjMvWfu0yZRapbuCdRFdwAntPwNL-ONEo9k_WFiGxMDXdJSW1_AQX77Kdld-x7OH27BWZNJovpwK1mFeswp56a-S4gPkQsZ_bTKrKHKVBujHqe2-XOktjCplQqVaHNRlHIDvpNtkzBi45XazOkyGyNE7l4d5jXBzgppdkchEN915NYNpAKlMiHEKiSLrR-T4wjYyNBgCYtic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد الكوبي يغادر قاعة الجمعية العامة للأمم المتحدة أثناء كلمة ترامب</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/91267" target="_blank">📅 18:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91266">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامب: كوبا ستسقط. الحرية قادمة إلى كوبا.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/91266" target="_blank">📅 18:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91265">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامب: نحن نعمل بشكل وثيق جدًا مع قادة روسيا وأوكرانيا، وسنحقق ذلك. أعتقد أن هذا الأمر سيحدث بشكل أسرع مما يتفهمه الناس. لقد انتهى الأمر.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/91265" target="_blank">📅 18:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91264">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الوفد الكوبي يغادر قاعة الجمعية العامة للأمم المتحدة أثناء كلمة ترامب</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91264" target="_blank">📅 18:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91263">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🌟
🇺🇸
ترامب:  لدي قرار كبير يجب اتخاذه. هل سيتم التوصل إلى اتفاق مع إيران يسمح لها بإعادة البناء وخلق دولة أكبر بكثير مما كانت عليه من قبل، ربما واحدة من أعظم الدول في الشرق الأوسط أو حتى في العالم؟  أم هل سأدمر الجمهورية الإسلامية وأفعل ذلك بسرعة، دون إعطائهم…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/91263" target="_blank">📅 18:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91262">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وزارة الطاقة السعودية:
تعليقًا على ما ذكره معالي وزير النفط العراقي، باسم محمد خضير العبادي، ورئيس مجلس الإدارة والمدير العام لشركة تسويق النفط العراقية "سومو"، المهندس علي نزار الشطري، خلال جلسة مجلس النواب العراقي، بشأن قيام المملكة العربية السعودية بشراء 25 ناقلة نفطية وربط ذلك بارتفاع تكاليف نقل النفط العراقي، أوضحت الوزارة أن المملكة لم تقم بشراء الناقلات الـ25 المشار إليها، وأن هذه المعلومة غير صحيحة، مؤكدةً أن هذا التوضيح لا ينتقص بأي حال من حق المملكة الكامل في اتخاذ ما تراه مناسبًا من قرارات تجارية واستثمارية، وفقًا لاحتياجاتها ومصالحها
‏الارتفاع الحاد في تكاليف نقل النفط يعود إلى عوامل تختلف عما أشار إليه وزير النفط العراقي والمدير العام لشركة "سومو"، ومن بينها التصعيد العسكري في المنطقة، والهجمات الإيرانية المعلنة على السفن، والاضطرابات في حركة الملاحة عبر مضيق هرمز، وما ترتب على ذلك من ارتفاع حاد في مخاطر الشحن وتكاليف التأمين، وتراجع أعداد الناقلات المستعدة للعمل في المنطقة.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/91262" target="_blank">📅 18:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91261">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامب: سنحيي الذكرى الثالثة للهجوم الذي وقع في 7 أكتوبر في إسرائيل. لقد قام إرهابيون مولتهم إيران بتعذيب وتشويه وقتل 1200 مدني بريء، بمن فيهم العشرات من الأمريكيين. وقد احتفل المرشد الأعلى الإيراني بهذه المجزرة ووصفها بأنها "خدمة للإنسانية".</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/91261" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91260">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eed65c16.mp4?token=rkGsGtFznvOtr7Nh4K2U8onBhP7LMUCGeP5qSdFKh8qIskKqjYLcXK3CaIgG0yI-9sd9cfmro8_9dPeluv5GRJ9j7xXoMnm0cAP434J_yT9QkPuplxAKyzGEpx0Isyiow7I7S6qr5Adk6rpLA6uxEP5hO9aOrjbBeeu5bzcp-PwYt6iQ1ms0fX98iEsKNYroUuYAqqW0DptuYFeXc2mPYvkKhCc30AVVfIIv6EeODj36-_ne7NYkM1FxuiHyQs_Pg5_in-_BmrNyULGGNUcxF1q3wqRW7_AkB0Pat9AklZaLE51y-Zb0DILE2n1NJWFoaJZqglsK93QAGI3o0EpZS1lTOxej_NyWE6tqlBSOtVSTgPy3P7LfhT8HJBjH59ciRImYJaf5KL54hDEhrMLgOMWs46pPkTD4_DOHrJ9yMiPbQsMOfYrCWGwWQ9tIi0i5PQDQ4AS9b0m39DRT92SMKLc00qRjjBIcgJfeCizfff8rALba7zL-ZuYMOKU28BsR1SWkdN5CdJS4eM0At-ZLPR9fA2oHCJHzCpdZBsB0fnqB_C7ta_zBCJOK3Tqq5EfTo3e9GbqUYcQgSswBW_xyMw_mkJmo_bYNoxfDd9JGr0cgS7Q93ctSsIwx0GKPtWMcyT9GtbQRg-yrOmL45_LtNHyl_OBU_VfuXsyxEWKPEzk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eed65c16.mp4?token=rkGsGtFznvOtr7Nh4K2U8onBhP7LMUCGeP5qSdFKh8qIskKqjYLcXK3CaIgG0yI-9sd9cfmro8_9dPeluv5GRJ9j7xXoMnm0cAP434J_yT9QkPuplxAKyzGEpx0Isyiow7I7S6qr5Adk6rpLA6uxEP5hO9aOrjbBeeu5bzcp-PwYt6iQ1ms0fX98iEsKNYroUuYAqqW0DptuYFeXc2mPYvkKhCc30AVVfIIv6EeODj36-_ne7NYkM1FxuiHyQs_Pg5_in-_BmrNyULGGNUcxF1q3wqRW7_AkB0Pat9AklZaLE51y-Zb0DILE2n1NJWFoaJZqglsK93QAGI3o0EpZS1lTOxej_NyWE6tqlBSOtVSTgPy3P7LfhT8HJBjH59ciRImYJaf5KL54hDEhrMLgOMWs46pPkTD4_DOHrJ9yMiPbQsMOfYrCWGwWQ9tIi0i5PQDQ4AS9b0m39DRT92SMKLc00qRjjBIcgJfeCizfff8rALba7zL-ZuYMOKU28BsR1SWkdN5CdJS4eM0At-ZLPR9fA2oHCJHzCpdZBsB0fnqB_C7ta_zBCJOK3Tqq5EfTo3e9GbqUYcQgSswBW_xyMw_mkJmo_bYNoxfDd9JGr0cgS7Q93ctSsIwx0GKPtWMcyT9GtbQRg-yrOmL45_LtNHyl_OBU_VfuXsyxEWKPEzk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: أعتقد أننا سنتوصل إلى اتفاق مع إيران بعد انتخابات التجديد النصفي.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/91260" target="_blank">📅 18:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91259">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏ترامب: علي أن أتخذ قرارًا كبيرًا بشأن فيما إذا كنت أود إبادة إيران أو السماح لها بالاستمرار والازدهار</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/91259" target="_blank">📅 18:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91258">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامب: لقد صنعوا صاروخاً قادراً على ضرب أوروبا، وكانوا فخورين جداً بذلك. آمل أن يدرك الأوروبيون ذلك. كان هدف إيران هو إكمال قنبلتها النووية خلف هذا الدرع الصاروخي الباليستي التقليدي.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/91258" target="_blank">📅 18:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91257">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7587284f78.mp4?token=kRHX72Q4U3xSJjhYBu44CmSz4ip6Ahop00p5v96boewiUJGix-SnExRqbo3x1KIHCS-gN3a93cYDUtwWA25fc5AWsQH9idP-EnE0M-UaguwmXdZVMezjPfenwy-VCaOinmWsPBFx6U8YCz6YTFTbJrf75SmgDMiIB7lQZ5HHJJMsbNn8LNpzVpAEfr7QdGWAspI7kB5CR0sj9tJS2ehhNaS_6sOnoMNRqnQd85As7R18R1J8-EdrnFMir31_PeNG4P4XiZoVQNXvuV5H74O5Z8ZsK4PGqaBGSqsKLRb5qYc2_uNcSbAOYgeYeFYzojyQmshzdgpuyZZiiir_48kdfTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7587284f78.mp4?token=kRHX72Q4U3xSJjhYBu44CmSz4ip6Ahop00p5v96boewiUJGix-SnExRqbo3x1KIHCS-gN3a93cYDUtwWA25fc5AWsQH9idP-EnE0M-UaguwmXdZVMezjPfenwy-VCaOinmWsPBFx6U8YCz6YTFTbJrf75SmgDMiIB7lQZ5HHJJMsbNn8LNpzVpAEfr7QdGWAspI7kB5CR0sj9tJS2ehhNaS_6sOnoMNRqnQd85As7R18R1J8-EdrnFMir31_PeNG4P4XiZoVQNXvuV5H74O5Z8ZsK4PGqaBGSqsKLRb5qYc2_uNcSbAOYgeYeFYzojyQmshzdgpuyZZiiir_48kdfTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: أدعو إيران إلى إبرام صفقة</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/91257" target="_blank">📅 18:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91256">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامب يبدا باسطوانة دمرنا البحرية الايرانية وسلاح الجو والصواريخ والمسيرات</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/91256" target="_blank">📅 18:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91255">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامب: هدف إيران كان استكمال السعي للحصول على قنبلة نووية ولو نجحوا لبثوا الذعر والموت إلى ما لانهاية</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/91255" target="_blank">📅 18:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91254">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏ترامب: دعونا إيران للتوقيع على اتفاق لكنها رفضت</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/91254" target="_blank">📅 18:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91253">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11e8def986.mp4?token=l08toiWxN0sRKnuvXzmyty7eiD_sEN35ecrsGVc81CxzxkSxz70YfiOUhqFhNgaaggixYM88CaYLkIrFvogAV89bFsbJ8ooLPNZPbsYvBjlmWFRxd7S_LujbIz3uNCM0ruCcNQahBMg7h8vCeV74VlcG4ArjAjT2u1F-cRFpFiYZbVuKh1VO1FFI8mCQy0NtJ-6My7Fa3Skby0TX8SzkuXtxei2UiYnkt2hISztUGLYkq08dh1wVM8eiaBfD37_EzG7Dxceszn8VTSpxWtkPiwJ86PO53aUGEK_bUKZdjT2moo0vyL391LUAg-jgKv-FEnTUae9ogXhrIFXwf8z14A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11e8def986.mp4?token=l08toiWxN0sRKnuvXzmyty7eiD_sEN35ecrsGVc81CxzxkSxz70YfiOUhqFhNgaaggixYM88CaYLkIrFvogAV89bFsbJ8ooLPNZPbsYvBjlmWFRxd7S_LujbIz3uNCM0ruCcNQahBMg7h8vCeV74VlcG4ArjAjT2u1F-cRFpFiYZbVuKh1VO1FFI8mCQy0NtJ-6My7Fa3Skby0TX8SzkuXtxei2UiYnkt2hISztUGLYkq08dh1wVM8eiaBfD37_EzG7Dxceszn8VTSpxWtkPiwJ86PO53aUGEK_bUKZdjT2moo0vyL391LUAg-jgKv-FEnTUae9ogXhrIFXwf8z14A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: تستمر إيران في تطوير أسلحة باليستية</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/91253" target="_blank">📅 18:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91252">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏ترامب: إيران هي الراعي الأول للإرهاب في العالم</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/91252" target="_blank">📅 18:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91251">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏ترامب: إيران هي الراعي الأول للإرهاب في العالم</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/91251" target="_blank">📅 18:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91250">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تحطم طائرة مقاتلة امريكية من طراز F-16 في قاعدة سبانغدالم الالمانية</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91250" target="_blank">📅 17:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91249">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اكسيوس:
عدة دول وسيطة تتواصل مع الولايات المتحدة وإيران لترتيب اجتماع رفيع المستوى.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/91249" target="_blank">📅 17:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91248">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇺🇸
🌟
ترامب:
من الآن فصاعدًا، لن تسمح الولايات المتحدة بوجود أي تهديدات لأمريكا في أي مكان في نصف الكرة الغربي.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91248" target="_blank">📅 17:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91247">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">الامين العام للامم المتحدة غوتيريش:
ما يسمى وقفا لإطلاق النار في الشرق الأوسط ليس أكثر من إطلاق نار لكن أقل حدة.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/91247" target="_blank">📅 16:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91246">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
مشاهد إضافية من عملية "والله أشد بأساً وأشد تنكيلا" العسكرية النوعية.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91246" target="_blank">📅 16:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91245">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇺🇸
مسؤول امريكي لـCNN:
أخبر ترامب مستشاريه بأنه يرغب في لقاء مسؤولين إيرانيين يحضرون الجمعية العامة للأمم المتحدة في نيويورك إذا كانت الظروف مناسبة.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/91245" target="_blank">📅 16:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91244">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انفجارات تهز مضيق هرمز بعد استهداف حرس الثورة لسفن مخالفة</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/91244" target="_blank">📅 16:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91243">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏
مصادر حكومية عراقية:
لا قرار الى الان بمنع الطائرات الإيرانية من استخدام المجال الجوي للبلاد او الهبوط بالمطارات العراقية.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/91243" target="_blank">📅 16:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91242">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6lwNHOBWy-2M5U9jdSx_-XVigyWwoGujuAVY3eT4lPcAIOi4hRLYsCbT1sMqkAUU6RoDQUMZGofV3yioglETLZn0-MG74pfBRbGp5QG18WzpHTAwivBPTZLu_gFVCXyqCFBlQ0um_p5_qUdBiM36WMoj8seFiEzh3KmoHlmKU15lji5H8JuwkAfrmhRDnDoAp34s8Fo2Y21NSI_gVLyCYrsO8Kx_C4HUl3fXozfs_6y1NyZ5bQ1lNEdyf2cm7XsWDDoLe-e3E4OAebjY4Vjmv4iGxLWsYC_nyNkYIOS8Q0QrFNKGfoFrWF-zg1_heqN7KhbIzQH_evSpYKGZoGplg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
توقف تقني لطائرة الرئيس الإيراني في الجزائر أثناء توجهها لنيويورك</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/91242" target="_blank">📅 15:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91240">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇺🇸
الاعلام الامريكي:
دول الخليج تخطط لإخبار ترامب بتجنب أي تصعيد مع إيران، من المتوقع أن يجتمع قادة الخليج مع ترامب في نيويورك يوم الثلاثاء.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91240" target="_blank">📅 15:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91239">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icG_HRma9X0zumpp4HFQVturyZ-IJmLMxFmYwvHP6omf_rL7y9DSTGvne0-SAi2Y41lYHkkKEIs6kOXDeyd1zam3mUXzfICroPni3_sszoW2iO05n5FHRH7LLhP3mPq_uwWw9tKzDgyun6TJDfUIHM7b-tnPFoyS8SqF_BMupXF5ouyJebUuHwXTQPH-2GDfRC3bKd-s12qnaRvnrXPhT6n413wTY1QY6Y0bD5jmDmZBMf3uYQrc1SWmgzZKHgu7RTmiluA6pEJiY9oD2FXHB3SBAvXZdL1luslBmOfIS-ull2YUGwA_DmUmcbmUNBZcOZ7AoVagMUV1g8LUlbG3mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
المعاون الجهادي للمقاومة الإسلامية حركة النجباء عبد القادر الكربلائي:
المقاومة باقية، والحشد باق رغم أنف ترامب المجرم وسمساره الصهيوني باراك، فلن ننثني ولن نتراجع، وسنبقى حماة الوطن والسيادة والمقدسات حتى النصر أو الشهادة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91239" target="_blank">📅 15:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91238">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCuqc8ldBvKMeAB3kH9kzJa0q3tRFl1brKVlaoozOQZ5QXap6MZ9DEiI10uE_9S__uxcdC8MjXDaE10TH8emBoCJxN74ouubJ3C7uPxk0nqByzL8dmECVhfJm2TtfUB-u5mcJvxlBPYGm00ohPtGO-FVlQ3ZRzdBIs4k1ha9VNwDV9YSE1Y0ztmFqOehD7g-yCMtFd-BrH6lo-Y3kyUWaEvV9L_kdnHtGTpDhH3P4N6hnnRNb5rXkcx45-HBq428SpPTBtCcdflgeQDHhhL6WUtaSuXUpIUpKnpJxvWPLNPzsqygvsowuqqmHU_pI44C93KNfHkWXy7w-jBN3C2IGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇺🇸
ترامب:
الجبناء والخونة سيحبون أن يقولوا إن الولايات المتحدة تعاني من نقص في الذخائر. هذا ليس صحيحًا.
لدينا كمية من الذخائر تفوق ما يمكننا تصوره استخدامًا، ونحن نقوم الآن بزيادة هذه الكمية إلى مستويات لم نشهدها من قبل.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/91238" target="_blank">📅 14:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91237">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed350d7bc2.mp4?token=CYljdw8BwOkt_rUFUO_QsdT89MnJ4FYJt3puGDAMrAlPRh_HqO_krkRt5_Sp_nmaL3jDsrTT8OM8iQXUoQ4fTy6niwkWkbk04uKJ3SvMBNnfaXD9z2UlPr4BAeuASPbECtv5IzapUMucfdXwBOBXWQM9xXZb8cbQea4cj1a-6jkmz7PWsE5w7X_hA_nr7op1Icv_8tnFTAarSPRc4ZPGNUmQTij6KlGylJnCYkTDt1FdfSDIwfuBDdZUI2EbWGlTut3v0fnoLogYu6bJ4eVZM8T2ZvJis3HXh308YZUb1vrYjqDBBOTbo8ubmr4B6fXyOCPd_BB_f7SO3h89cxGwzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed350d7bc2.mp4?token=CYljdw8BwOkt_rUFUO_QsdT89MnJ4FYJt3puGDAMrAlPRh_HqO_krkRt5_Sp_nmaL3jDsrTT8OM8iQXUoQ4fTy6niwkWkbk04uKJ3SvMBNnfaXD9z2UlPr4BAeuASPbECtv5IzapUMucfdXwBOBXWQM9xXZb8cbQea4cj1a-6jkmz7PWsE5w7X_hA_nr7op1Icv_8tnFTAarSPRc4ZPGNUmQTij6KlGylJnCYkTDt1FdfSDIwfuBDdZUI2EbWGlTut3v0fnoLogYu6bJ4eVZM8T2ZvJis3HXh308YZUb1vrYjqDBBOTbo8ubmr4B6fXyOCPd_BB_f7SO3h89cxGwzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتن ياهو يهاجم ممداني:
عارٌ عليكم، يا سيد مممداني. عارٌ عليكم لدعمكم لوحوش حماس الذين ذبحوا شعبنا. عارٌ عليكم لإثارة الفتن والاضطرابات ضد اليهود في نيويورك. سأتوجه إلى الأمم المتحدة. سأقول الحقيقة عن جنودنا الأبطال، وسأقول الحقيقة عنكم.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/91237" target="_blank">📅 14:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91236">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇺🇸
وزير الخارجية الامريكي: لا أعتقد أن هناك أي ترتيبات حالية لاجتماع بين ترامب ورئيس إيران ولكن ترامب منفتح على الاجتماع مع أي شخص.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/91236" target="_blank">📅 14:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91235">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇺🇸
وزير الخارجية الامريكي:
لا أعتقد أن هناك أي ترتيبات حالية لاجتماع بين ترامب ورئيس إيران ولكن ترامب منفتح على الاجتماع مع أي شخص.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/91235" target="_blank">📅 14:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91234">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
ترقبوا الساعة الرابعة عصرا مشاهد إضافية من عملية "والله أشد بأساً وأشد تنكيلا" العسكرية النوعية.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91234" target="_blank">📅 14:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91233">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇷
🇵🇰
‏
مصدر دبلوماسي إيراني:
باكستان لم تحسم قرارها بشأن تعليق رحلات شركات الطيران الإيرانية.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/91233" target="_blank">📅 13:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91232">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">السعودية تعلن استئناف تشغيل خط أنابيب النفط الذي يربط بين شرق السعودية وغربها</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/91232" target="_blank">📅 13:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91231">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇷
🇺🇸
مسؤول إيراني رفيع المستوى:
- طهران ترحب بعودة الدبلوماسية إذا اتخذت الولايات المتحدة خطوات ملموسة.
- وفد إيراني موجود في نيويورك بصلاحية كاملة لإحياء الدبلوماسية مع الولايات المتحدة
- تم تسليم مقترح إيران إلى الولايات المتحدة عبر وسطاء في السادس عشر من سبتمبر.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/91231" target="_blank">📅 13:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91230">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇹🇷
🇮🇷
شركات الطيران التركية "طيران تركيا"، و"بيغاسوس"، و"إيه جت" تلغي جميع رحلاتها إلى إيران اعتبارًا من 21 سبتمبر</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/91230" target="_blank">📅 13:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91229">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇶
قائد القوات البرية العراقية:
القائد العام كلف رئيس أركان الجيش الفريق أول الركن عبد الأمير يار الله بإدارة ملف سنجار وفرض السيادة الأمنية الكاملة وأي مسلح غير عراقي يجب أن يغادر سنجار ولا يمكن قبول وجوده</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/91229" target="_blank">📅 12:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91228">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اوكرانيا: استهدفنا مصفاتي نفط في أوفا وسمارا داخل روسيا</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/91228" target="_blank">📅 12:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91227">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ول ستريت جورنال: ‏أنفقت السعودية أشهرًا في إعادة توجيه النفط للالتفاف حول مضيق هرمز. الآن، يضطر ملك النفط في العالم إلى العودة إلى الممر المائي الذي كان يحاول تجنبه.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/91227" target="_blank">📅 12:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91226">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇾🇪
رئيس اللجنة الوطنية لشؤون الاسرى في اليمن:
قام النظام السعودى المجرم ليل أمس باستهداف سجن يضم أعداد من الأسرى في  مدينة الحزم بمحافظة الجوف مما أدى إلى مقتل 9 أسرى ممن تم أسرهم في الأحداث الأخيرة.
وسوف ننشر لاحقاً قائمة بأسمائهم.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/91226" target="_blank">📅 11:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91225">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏
🇨🇳
🇮🇷
الصين تعلن معارضتها للعقوبات الأميركية على شركات الطيران الإيرانية
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/91225" target="_blank">📅 11:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91224">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j83WX-67jBfTFiS93-NRw7dPiRRIOf-XVJugsIJvojAkjKWan76Va7UQd8NI9gTTgryBLHK5bVtZugzCpxXFC1KJhfgtaXroE-w3X2lw8aoIdgk0QS3IIZ_qNRiPyr4bSmH6ACNX2ldeBLCY_94tNCJ0UjTXz15zX1zO_O_Vl0cv_7LsdPPaEuxLmynPmlN98XAhneEA4rgIvIeZOSmT6NJfwlFHMhGEkDRgdhQHsaJgyiRRjiNmoEXn3iePJADcvdxM_XIWZs8ki_IJoZ7kv1r6xsKUJyiT8xHaX7rLkWdkGBpNsqr1CjQAR43FaipR9sKAQdosxEPLblZFPEsf1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
تفعيل الدفاعات الجوية في نجران  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/91224" target="_blank">📅 10:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91223">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇸🇦
تفعيل الدفاعات الجوية في نجران
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/91223" target="_blank">📅 10:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91221">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyfH0oUaVFw5vSpbBSA-D5jiBQtMBeBKfefzLworbuD4tiPbjRu7gExb7MXRCJKNPqoMCvvw3xBM1Yr4G7bP5YkDN-TdFMpXUOWdFFpf_Fau3i4nVJUV3mvExW2uWs3a0KE6coZA-74K37AC0yDTdTMt1K5hiA_bQCNbmKrRMMKcCTa2vU3LPKyWFpbt-Mpj-ciZ-mgJ_HSXmrGbLG4O-oduG4zXMB35ltXhmzkvVprch4KljdapgLFbsXHZZVj0UGWUy7S4uC5nfTtePoOzge3ECJPRXH0WDxjMX3s9EFEq1ZG0A0Iif9soSQDnKLBAEAWvDwv92rk38QhR5_bw7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
إرتفاع أسعار النفط العالمية حيث تجاوز سعر البرميل الواحد  102 دولار.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/91221" target="_blank">📅 09:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91220">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي بعدد من الصواريخ يطال مديرية الظاهر والمناطق المجاورة ضمن محافظة صعدة اليمنية.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/91220" target="_blank">📅 08:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91219">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇾🇪
عضو المكتب السياسي لأنصارالله "حزام الأسد":
استطاعت الأجهزة الأمنية، بفضل الله تعالى وبتعاون المواطنين، إفشال عملية إرهابية حاول نظام العدو السعودي من خلالها تفجير دراجات نارية مفخخة، واستخدام انتحاريين لاستهداف بعض الأسواق والمساجد في العاصمة صنعاء.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/91219" target="_blank">📅 08:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91216">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYU8ZZgoTOk9sWLoPWBRRPFJWXTLOK-G1o2xDJZsyFEr3R2qKi8nQ4_PLQlTjBmMtljbt39JiimA_zIIRMTar38ht38yjlp6JVJef7OiPRS4pPcBbTYRqX82kFa5TaH59RvNIEh3CzAz8cVDzAErqXOntOFU2PLVLiOxzbCIYBiy0nkvlYw23Fd3dJMBPcKfEEBmlOnzoWqk1R9rAL3hJNxr_6eajAqhpYhrq5rXfQ2saeqaSnadVg0uTiqnE8QSHzw_jN5wpzD3P0oZgEBbL53vpsePOK_-LU_EjK-rj10Qw1pG7l3pNcc-zoAUIizXLkcU8QZF79SlhMfzrzOsPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42e0df582f.mp4?token=qmscbAi0OQ6tTclcxrcax6MfEzW8PdcSvh13MAq0sj6PslpaRENS_vNJqA1C2JJsp9EYNw5WWAaZzdYIzMjA8CYr_QGBc7QptYAcIYZgrZn6KbO0mni1paAsk6nNm2iJAVN4JVtk-3oyN_WxbQdX1X835oW0uO0svC47JSbp4NoP5vyYJVj1bIbfggdwM2lIscz1jqJLLMjVRbmL_-6uF9_eWaEJspIMeEyaGJ7kkNDiGYq7aE2os2sv9KGDViYCcrF55I6fZjN4m2CFBavF7IvgRkcU2ATXxkYYkwHNnNOZCSLJAq7KYLGaSlD1ABjvRSvKCrZMusFP2m__cWmWtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42e0df582f.mp4?token=qmscbAi0OQ6tTclcxrcax6MfEzW8PdcSvh13MAq0sj6PslpaRENS_vNJqA1C2JJsp9EYNw5WWAaZzdYIzMjA8CYr_QGBc7QptYAcIYZgrZn6KbO0mni1paAsk6nNm2iJAVN4JVtk-3oyN_WxbQdX1X835oW0uO0svC47JSbp4NoP5vyYJVj1bIbfggdwM2lIscz1jqJLLMjVRbmL_-6uF9_eWaEJspIMeEyaGJ7kkNDiGYq7aE2os2sv9KGDViYCcrF55I6fZjN4m2CFBavF7IvgRkcU2ATXxkYYkwHNnNOZCSLJAq7KYLGaSlD1ABjvRSvKCrZMusFP2m__cWmWtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي واسع يستهدف مدينة دنبرو، ثالث أكبر مدن أوكرانيا وأعمدة النيران والدخان تتصاعد منها.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/91216" target="_blank">📅 04:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91215">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇸🇦
🇾🇪
بنك الأهداف السعودي في العدوان على مدينة المخا اليمنية.. 6 شهداء و8 جرحى من المدنيين، بينهم أطفال ونساء.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/91215" target="_blank">📅 03:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91214">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StwTKjVGaPjYzanCXyxD_xwNtiBrXi8ZNZ25Thh752OiBD-M0ePIee_DcNhK0WsYD0Jkt-YbwGORF3dFs_oxzh9w3eK07z7yv5Kf4dS_QAY6z3gUjK8jivIwYJrepGsdhwNFYhMUqFL5FKgrXBr2t51l-8Z6FXI7za4ht0_rHt061fyCobNddefi_dul3ApHSGZ48rOoJaHfQPZbYjVUCAi0JfGNibr79_-PvdhWD-TA9JcEyxoL8tvk-iO2fmw-zkDa8r404wGQFblI7Dk_wDKK8FhMCKDPZQFexQObS6W10lq7FYYzK5sjfWZKbxrd90R5S_uTeM4M9tm_rs5Ckw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
طيران العدو السعودي يستهدف عدة مواقع في المخا.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/91214" target="_blank">📅 02:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91213">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇸🇦
🇾🇪
إندلاع إشتباكات مسلحة داخلية بين مرتزقة السعودية في منطقة زنجبار بمحافظة أبين اليمنية.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/91213" target="_blank">📅 02:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91212">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZPoBh3Q5s5dDXzCdiOGVmAQvY5euEyr2rJippwX4VcKo13yjL_Hkh9ELUpVOelioV0uNS5NIAoHjuUuXmXk7THk-CmHYFk6KTTlTe0tGX3GWG5-Ban_0OuAKKG3JKgqiKay2dswnOdaT8GN8M5B6lbjddoYA5kn8J7s2bpsTl6XtrYFObd52jMMbEh1dziuc5Gf3qJSBAkPV9lp-GPvl23Pa1U3gqFe1ArLjDN8CcfDC60c6u97aM5vXchRG-uhK28ZE-B9UJeB7gP5538NKMh_bqTH62D2iwh64ghxYvDwDkV3Yl_C4ACQQNLXbQhb_J2VU--9ymDSUhTqd-E7tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
رئاسة وزراء العراق: حصر السلاح سيبدأ بفترة ٩٠ يوما لا تهاجم فيها الفصائل أو تتعرض لهجمات أمريكية، سنعتبر الجماعات المسلحة خارجة على القانون إذا واصلت عملها بعد انتهاء المهلة، المجموعات ستبدأ تسليم أسلحتها على أن تنتهي العملية بحلول 30 يونيو 2027، خسرنا 60%…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/91212" target="_blank">📅 01:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91211">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇾🇪
عضو المكتب السياسي لأنصار الله "حزام الأسد":
تخوض قواتنا المسلحة، بعون الله تعالى، معركةً مصيريةً مع نظام العدو السعودي المجرم، واتساعُ رقعة المواجهة سيحتّم توسيعَ وتنويعَ الخيارات في اختيار الأهداف.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/91211" target="_blank">📅 01:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91208">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/szJbfvbfVJBV9Cp7WmPT7NWHzpfe_M8ECJxsCkto8KGr6fsqsuBDCAzjPfCp0mt7ujXRRiy37rV5_QX1vjUjZa6eJXTPY5lZoFVuocmTvZQ89GZpGyNJa9QJ0eSAyH4cS8QivhQJDEp7L7BQNmVkGR7XZeYalOz8txz1hjQ1i1CdTeWmH1QBdpKaMbvmCdziLtkZKst7DvppJXNofsjfX8q20i4-50mkIBgMtUvGj8RbFiQDu8pa5EyK_583PcPZ28bWuDehdZV5pZMh5jtcYoPsrM-5agfZ-iOl0D5cm9URPT_FLUwQ4--NNpJuV3U7fWjrkz7EVlB7Em5Gl9niPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mzL0FnAeiSsy0hblUMSMBiOW8eWDhIqS4Kq1CkAT2wIPguXm-69Aq0vU36eRFThgqE-Rdg_yUw5m1Pc8-BAoY61yoNRD1wDBH90k1GvLr0QmSYpPwIoTZGGIbeT_BZJkaA04_J7gWYXAYaNhQBbLNRhbX3xCvDdnIFUOJfO_dOa081kQvYlDJDJM5LlxKz_Jc65GtR0wLqfB3bluXH5JHvJiC2LmCYCDO8n79DnKIi0usSl2EGDTVHX7_BiP9xAOjNmdAwAH4A7Mpm4wv7zsP2n-EcyGl9Jl3oM57xgmBQ_T4PG4AMkz-4Rsk8OQXQQhU17GEkiF7vZxfI1-lW6zKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oXNP_Nj8leAjNPv6ju1D9QqG4DunY2Gw75BZqow0HgLWdzaEfCOV5GgfSGDcYs8uT0mP9URaeDgk0_AdVDwWR_E_f9Zvluh6N8H2jd3_xAW6E3NUyXqIqfgXKRNpDIjcmLYkeJ8TBF69nsY-yVFyGlVSvhVnnO_HBsHcMlsml-CdxJiwtOSVK_cibvJjvTxKvyydxETrRT2buW9sghANpIDVvxhY3rSzE_R0pFEQkdUJLgPki_P4v8qyLvRuHm3EKqE9nROCq51926HU4Fw84vwqJmh0wzwVp8s2K7O5NzmTnkGn1Wpi64EB7osUh59LaenNcYIrdGvDTWYOkwkS0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">علماء اليمن يردّون على مزاعم استهداف مكة
بيان صادر عن علماء اليمن يرفض مزاعم استهداف مكة المكرمة، ويؤكد أن المقدسات الإسلامية يجب أن تبقى بعيدة عن التوظيف السياسي والإعلامي، داعياً إلى التثبت من الأخبار وعدم الانجرار وراء حملات التضليل.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/91208" target="_blank">📅 01:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91207">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a5c10fbadc.mp4?token=Q7qnCoko5l5ArQhec-jf_XkleADyzcG7PhqIAdGsJIYbayM6gYilwoeEXYezbJUvsGG2-bUXMOb69O4bdMkT9XCpxI31Gisi7PzwlrL_Yl7wLwLmpuHOS8T3yXxqWytl02Xu6T5sPnNHVeW_AZBKpcZnEZUu4jEps9E83WzpXQla3bq67T1S6ccx6gvEBuezodXY3Is3mKFDCFdQJ65ueUaVrhyMTZ5a0TExJUyz8KtMbMobfSSqMKmJ2j4ImpaWzCp6WqEGJQ5twXnIfYttX230rK8lvS8msEVhwFrTxAqtn_zpOq1mQubtlGVr2l-j2GfhuEciW3dHsl1j_ioJGw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a5c10fbadc.mp4?token=Q7qnCoko5l5ArQhec-jf_XkleADyzcG7PhqIAdGsJIYbayM6gYilwoeEXYezbJUvsGG2-bUXMOb69O4bdMkT9XCpxI31Gisi7PzwlrL_Yl7wLwLmpuHOS8T3yXxqWytl02Xu6T5sPnNHVeW_AZBKpcZnEZUu4jEps9E83WzpXQla3bq67T1S6ccx6gvEBuezodXY3Is3mKFDCFdQJ65ueUaVrhyMTZ5a0TExJUyz8KtMbMobfSSqMKmJ2j4ImpaWzCp6WqEGJQ5twXnIfYttX230rK8lvS8msEVhwFrTxAqtn_zpOq1mQubtlGVr2l-j2GfhuEciW3dHsl1j_ioJGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های بزرگ و رسمی آمریکا، از جمله CNN، Fox News و NBC، در اقدامی کم‌سابقه، پوشش مستقیم سخنان دونالد ترامپ را بایکوت کرده و حتی از اعزام خبرنگار برای پوشش مصاحبه‌ها و سخنرانی‌هایش خودداری کردند.
ابعاد این موضوع به حدی رسیده که امروز، هنگام سخنرانی ترامپ، نبود خبرنگاران رسانه‌ها برای پوشش مستقیم و دریافت صدای او، انتقال و انتشار دقیق اظهارات او را با مشکل مواجه کرد.
@Naya_Press</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/91207" target="_blank">📅 01:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91206">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇾🇪
🇸🇦
طيران العدو السعودي يستهدف عدة مواقع في المخا.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/91206" target="_blank">📅 01:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91205">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇾🇪
🇸🇦
رئيس الوزراء البريطاني بورنهام: وافق على طلب المملكة العربية السعودية بتوفير خدمات تزويد الطائرات بالوقود جوًا جوًا بشكل مؤقت لأغراض دفاعية بهدف تحقيق الاستقرار في المنطقة.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/91205" target="_blank">📅 00:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91204">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0517e652d0.mp4?token=APmXAtbA_KhWbyKP1lDYKPoibekt6F2-AV1mfSjexlKN0RvDSK1EU51FB8RJguHPmbb44tgov2jbkalKumGkqK9zenQVz-Mprq7iiUub5eZi2zMvOQiXfqsprsdN10wO-Ylr2eiQcNj9tYzoih5xR4igX91ZKPNfSUXjmLwBsr40mi7pS6MsoK80Dh4zRwWER8aqbwGeqgkfB0oKLfEeOcf4ulnwcjGUiauRHknJZLeNtlHm9WNhVjronDapnc9BaPn_NqBljdF30Pb3muxrcWi852vtfqsGyyGr2KwBaxg9sBWzgJq8vr4PELo_lUwIA4sa8pw8OLJ0BSERdVKEIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0517e652d0.mp4?token=APmXAtbA_KhWbyKP1lDYKPoibekt6F2-AV1mfSjexlKN0RvDSK1EU51FB8RJguHPmbb44tgov2jbkalKumGkqK9zenQVz-Mprq7iiUub5eZi2zMvOQiXfqsprsdN10wO-Ylr2eiQcNj9tYzoih5xR4igX91ZKPNfSUXjmLwBsr40mi7pS6MsoK80Dh4zRwWER8aqbwGeqgkfB0oKLfEeOcf4ulnwcjGUiauRHknJZLeNtlHm9WNhVjronDapnc9BaPn_NqBljdF30Pb3muxrcWi852vtfqsGyyGr2KwBaxg9sBWzgJq8vr4PELo_lUwIA4sa8pw8OLJ0BSERdVKEIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب
: سأعقد اجتماعات اليوم بشأن إيران، والأمور لا تسير على ما يرام.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/91204" target="_blank">📅 00:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91203">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇾🇪
🇸🇦
الاعلام الايطالي:
إيطاليا نقلت خلال الساعات الماضية بعض طائراتها العسكرية من قاعدة الطائف السعودية بسرية تامة وبسرعة بسبب المخاوف الأمنية من الاستهداف اليمني لقواعد السعودية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/91203" target="_blank">📅 00:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91202">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏
🇰🇵
كوريا الديمقراطية الشعبية العظمى تعلن عن اختبار نظام أسلحة قتالية جديد
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/91202" target="_blank">📅 00:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91201">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇾🇪
🇸🇦
بريطانيا على وشك الاتفاق على تقديم المساعدة للجيش السعودي لمواجهة الحوثيين.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/91201" target="_blank">📅 00:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91200">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
استعدادات في إسرائيل لاحتمال التصعيد مع إيران.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/91200" target="_blank">📅 00:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91199">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي: ‏
تدفع الولايات المتحدة أكثر من 30 مليون دولار يومياً مقابل حصارها البحري لمضيق هرمز، مما يُرهق ميزانية البحرية الأمريكية، ويُثقل كاهل البحارة، ويُضعف جاهزية القوات البحرية العالمية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/91199" target="_blank">📅 23:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91198">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇶
رئاسة وزراء العراق:
حصر السلاح سيبدأ بفترة ٩٠ يوما لا تهاجم فيها الفصائل أو تتعرض لهجمات أمريكية، سنعتبر الجماعات المسلحة خارجة على القانون إذا واصلت عملها بعد انتهاء المهلة، المجموعات ستبدأ تسليم أسلحتها على أن تنتهي العملية بحلول 30 يونيو 2027، خسرنا 60% من عائدات النفط الشهرية بسبب الحرب.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/91198" target="_blank">📅 23:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91197">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seLblEODeO48snO_wA-1bSHd_Eiitkb_LBmlvtRvLLKr2aosSZGGEA34xO1eqBZmqzTw3qxFcBWmBFm-Q4FBi4J_e1soTXdNgcKdOh0EJ6N2djV0zNuNhDwh1IbGsSxkZcrytKyWWKjAvX6MzpbBo_n0X776xpZWe1y5QG4mNkMmf9bEJsjk2yUStgAsPo5CSv2ciH_iR5GYkXgQI_IpSqNXUc0wD2QlB1rh3hfzRxqkPWUplAxDKZKLQ0RXqUIsDVk_68CxQ-DMQ116b7IVhrOKs9qXvdHmLEVIAojXhZAmW24fJYm6cNX4Y_5jCz1u3HT6EDUEtQszVyQRshrTDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الناطق الرسمي لكتلة بدر
النيابية:
تحذير للحكومة العراقية وسلطة الطيران المدني من الانصياع للإملاءات الأمريكية وفرض حظر جوي على الطيران المدني الإيراني ومنعه من استخدام الأجواء والمطارات العراقية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/91197" target="_blank">📅 23:43 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
