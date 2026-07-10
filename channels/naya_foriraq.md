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
<img src="https://cdn4.telesco.pe/file/ZrO6_-f3fU_izCZHTjD1mPUgrQOpC7KWpforSbIOXgRnXO86xVurZ5CABgvvEXhdutQxq3QJ8wx-ZXu5g4HsNRptCi4eqHNhxP-sZddinVE7uFaq0CDAd-cgTSUQ7UtCIHuR8InOlIukOo0d_SuWecAD2HMlZ3Nya6IzpYCcnLb5t0G_JCUi1b4AEshXowvGkAyubCPk5xNJUxon_QXUeQWNWfeOysAsU3Rd4VqHeecsV1t5RX1CjvH-iA6Vl2wC3ZL5CNOuPRrCOYBADI2xa6qwoTZv19Dp7Epz-OB8--o-0e_SVQysDu9CAV14rUDe_UCs6xnTgGTulnN1VTN9WA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 259K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 03:28:18</div>
<hr>

<div class="tg-post" id="msg-82272">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مسؤول أمريكي:
عدم شن الجيش الأمريكي ضربات جديدة على إيران الخميس جاء نتيجة جهود إقليمية لخفض التصعيد</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/82272" target="_blank">📅 02:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82271">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtBahM6bN4tXrb3W9InQ5MvESEwaom0wLK1N1BfoZ1KgJOyygsfO3uxvFOJV6PPNhED_Wt7rwLnKXXv2wNsLULOnQpX4QN-fJJrdPeIeyqmwJo9wWzI7rW1IdTYcdgwhma5_TULCF5h28OpvdmFf9HFFg4RAwhTH7KhkB_9sDtIqUWVWMU-aaFqV-2jHuSOgPv4ro9G787tqoPtReDPVfYV_Yq_JljhsM5hmHdgJTAAfW5YD_SBNERz9DZ5Buw9pHRv7Urz3xe6lSO8KWsH3-edkUoiGjRGb1XeoocOFAC0JQ5YBcXvSnLqWrfiQoOIF2-RkwtzMYE26EG_beaM-YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الآن تم دفن أمامنا القائد
💔
الصلاة الصلاة يرحمكم الله
#قوموا_لله
🏴</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/82271" target="_blank">📅 01:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82270">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇷
مصدر إيراني: لم يحدث أي حادث أمني قرب مرقد الإمام الرضا (ع) أو على طول مسار تشييع جثمان الشهداء.  "بلوار سرافرازان" في غرب مشهد، ويبعد أكثر من 15 كيلومترًا عن مرقد الإمام الرضا (ع).</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/82270" target="_blank">📅 01:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82269">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇰🇵
كوريا الديمقراطية الشعبية العظمى : بيونغ يانغ قررت تعزيز قواتها النووية نوعيا وكميا</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/82269" target="_blank">📅 01:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82268">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇷
مساعد الأمن لمحافظة خراسان الرضوية الإيرانية: إطلاق نار في منطقة "بلوار سرافرازان" في مدينة مشهد المقدسة، أسفر عن مقتل شخصين؛ هوية القتلى لم يتم تحديدها بعد.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/82268" target="_blank">📅 01:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82267">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">كما اكدنا لكم ان العدوان انطلق من الكويت وتحت غطاء معلوماتي من قاعدة الظهران الأمريكية في السعودية</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/82267" target="_blank">📅 00:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82266">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇷
مساعد الأمن لمحافظة خراسان الرضوية الإيرانية:
إطلاق نار في منطقة "بلوار سرافرازان" في مدينة مشهد المقدسة، أسفر عن مقتل شخصين؛ هوية القتلى لم يتم تحديدها بعد.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/82266" target="_blank">📅 00:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82265">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbrm0_7l5QQQsbT1hPNj_SqEwPo0pi0ReqJitDzn3e74L01LBblNJ9-v7QrimbJufcQDbAZWFFFUxLhgf1KXoenh2yZQiLcoOqFXNkj0km-W7ykqg9VY_s95uabki256m5eOkJkRBqsG_azpcCniIgw1IE5Nyc3t6TjhvToWpoy0Ngq7qWp758r1q5VtW7ks1WWvDnzjX04s5A9EIuGtk4DHwuNTeZtFfOykHzQMfb8Qp44TUxOwy54inmbUOspGaUw6x88LeYci_ro3Z66JHDZzn8BgYa0h5-3zBbrCZJEr80sOnaodNJT2-NkqK0dQ9UaFx7ZSAQb6jZ82crwjdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الكويت تقتل العراق</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/82265" target="_blank">📅 00:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82264">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBT1sqKYlrcJ7G6TlhJHhT02NROP-5EU-t9iLEgsMshrM-njv75XzjtTeIHJ4eA6pfZWYsPHNOKcdyFWOEL_sX-EmqMalDPOI-xbMp060Ae630KW-UFtEt3TfYQ01WN1Ylvx98Sx6JCuuXToUrLm1huQCELjk387tggzfAfne_r122Z28VJpv1ayZrUpM9YAqNXdAkGWTA08o86zCtjFYemdsbWKwnf9-mdsGbAsQLCIrL8_TISS99qawcVn-hcw_vURGocJC1ncsQF-uOHJHqzOB8soNz37tyYAnB_8YXnF22-WqUPj4fuAHON8nBz0u1VLgOZla5Wepb2agaJ4Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رسالة من رجال ساحة المعركة إلى المشيعين:
الحمد لله أنكم ملأتم الفراغ الذي تركناه في تشييع الإمام الشهيد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/82264" target="_blank">📅 00:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82263">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو مهدي الجعفري</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RO3wSPRCkAGgI6O93N4FEPPlcSw-Gepgzgvknk98fZUJww9rsyEmFih_jmt8XDGtPrTSB3UGGcXBt92IAYZPFJTHCgOqhjARbThmErw3ZiJO0fJpuzWzHrfAB8uUH4q_AeRHzoN1-4OkCx01DpcTdAOx1hsNYALUPW7uG7-z4qIY8dJj5EdoP1co8TcBGxP73CdOtbEwM43X_hx_y1_UB7L2xi1r9BX5S5IcQZRn6HU9UU9P1crft5NLd7qQCHgGcAWnqB1_4axkB3pj9sxeHeRjADoiWcPLbZ4JrgiZaYGKWohCTaPMRxjYRfJCdic7TDD-eRxEAR_E0Cu6D3ZSpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شُكْرٌ بِحَجْمِ الْجُمُوعِ الْمِلْيُونِيَّةِ لِنَجْلِ الْمَرْجَعِ الْأَعْلَى، سَمَاحَةِ السَّيِّدِ مُحَمَّد رِضَا السِّيسْتَانِيِّ؛ عَلَى انْتِقَائِهِ الْمُفْرَدَاتِ الْبَلِيغَةَ الَّتِي تَحَدَّثَ بِهَا خِلَالَ مَرَاسِمِ تَشْيِيعِ السَّيِّدِ الْوَلِيِّ الْمُسْتَطَابِ، مُعْتَمَدِ الْمَرْجِعِيَّةِ الرَّشِيدَةِ فِي الْعَتَبَةِ الْحُسَيْنِيَّةِ الْمُقَدَّسَةِ، سَمَاحَةِ الشَّيْخِ الْمُجَاهِدِ عَبْدِ الْمَهْدِي الْكَرْبَلَائِيِّ.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/82263" target="_blank">📅 00:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82262">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac4250178.mp4?token=NEx4O-u6WugpTEahOfHgxkApazBW62HA2k5d8ZmrLgMPNfJSQwdXLSPAkXhfL-HkrKB976gj34uTXRLnQk3oaLR79a-LHyx8Aq-0tYr4IQtJrphMAvvY83J38NoEsgVtU8ROhkmnIqXgpZJyGGW2Dz_o59mIY5oMukyzXV7lPW4tefTGq7iTf0vZ1iGKud4uI2Jrij0WjF5Mt67z99aDLiIgP6Em7QnJkrtVnNOOwFApvIkEkqqiTgIL77PQh4--EgfF8FrNagTSfaxYJ7mKv0Ku9vbhZ1V4YWv0wbR5XzuGPDMMdU9qPuNin1FwAjD4iITLZMV0vCPsmbrm6ibxsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac4250178.mp4?token=NEx4O-u6WugpTEahOfHgxkApazBW62HA2k5d8ZmrLgMPNfJSQwdXLSPAkXhfL-HkrKB976gj34uTXRLnQk3oaLR79a-LHyx8Aq-0tYr4IQtJrphMAvvY83J38NoEsgVtU8ROhkmnIqXgpZJyGGW2Dz_o59mIY5oMukyzXV7lPW4tefTGq7iTf0vZ1iGKud4uI2Jrij0WjF5Mt67z99aDLiIgP6Em7QnJkrtVnNOOwFApvIkEkqqiTgIL77PQh4--EgfF8FrNagTSfaxYJ7mKv0Ku9vbhZ1V4YWv0wbR5XzuGPDMMdU9qPuNin1FwAjD4iITLZMV0vCPsmbrm6ibxsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بعد 24 ساعة من لقاء الجولاني وترامب وتلقي تعليمات لمهاجمة حزب الله.. عصابات الجولاني تشن حملة أمنية على حي عش الورور العلوي وتعتقل عدد كبير من الشبان العلوية حيث لفقت التهمة مسبقاً "خلية مسؤولة عن تفجيرات دمشق مرتبطة بحزب الله" وذلك لذريعة الدخول في حرب لبنان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/82262" target="_blank">📅 00:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82261">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/391970061f.mp4?token=uizkovjxXvnzVe6KyWF-vTxxBMAq8Y-p1Le3PSnYITAZfzeIYyIxfykGJVTTJOtU_Zc3Cve6d3MS0jYfFHhHwNUFp_0g2NmcFDST_aG_le_Y8BQm0R1EltXynl4xahHDt5PwOZfzLcEbYi5Fnz6PVdFqjBpfM1G7j6IgHyd4UNnGYwXN7rNkwqH5rontzFa8NmeyZLFh9OLlqLKAodc_m2yRyHfsKUJKg7ayRkqsK1z0YwoXZE8ynG2cDm0HjVPSaYfS8meW5ivI_hxoOP0IFyfZvtxWAyCxmuXEiFl2IZx_lpi8neELRs3lRAapSdGMsswgWpDZVdtkmSe5p7PcB7ZBxVZ_kq7E6ma67CAjOQzj8SVl97vzIdOjI-VIA6J3uRBP3T0eSktmokcSbP005cVgtAc6DCaPtr84Rrw3u7Y9BWBBAChwSPGdy7GVp3twKp0PK6qgmqSKol6x7fraQZUZLfXJzo-na9qKiX-gCVaCEP8XEaDJ0I2F61iqfVCoIASzU1d7BQ-fWaY_IIUQRtHMYJ83bpU7BGyM_Vsub7U9xBVcbXb18o_BV9Z7b1cZbHIzZbVPIX3HUNi_GbPRoUNbRt_HXt-JYcTI7l7K-GeQS29iJlfP9t4QiB1Yld-0ZeVFh65nFModHaRIU8UkbDV5TKa6P5JqqM-1euQr85I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/391970061f.mp4?token=uizkovjxXvnzVe6KyWF-vTxxBMAq8Y-p1Le3PSnYITAZfzeIYyIxfykGJVTTJOtU_Zc3Cve6d3MS0jYfFHhHwNUFp_0g2NmcFDST_aG_le_Y8BQm0R1EltXynl4xahHDt5PwOZfzLcEbYi5Fnz6PVdFqjBpfM1G7j6IgHyd4UNnGYwXN7rNkwqH5rontzFa8NmeyZLFh9OLlqLKAodc_m2yRyHfsKUJKg7ayRkqsK1z0YwoXZE8ynG2cDm0HjVPSaYfS8meW5ivI_hxoOP0IFyfZvtxWAyCxmuXEiFl2IZx_lpi8neELRs3lRAapSdGMsswgWpDZVdtkmSe5p7PcB7ZBxVZ_kq7E6ma67CAjOQzj8SVl97vzIdOjI-VIA6J3uRBP3T0eSktmokcSbP005cVgtAc6DCaPtr84Rrw3u7Y9BWBBAChwSPGdy7GVp3twKp0PK6qgmqSKol6x7fraQZUZLfXJzo-na9qKiX-gCVaCEP8XEaDJ0I2F61iqfVCoIASzU1d7BQ-fWaY_IIUQRtHMYJ83bpU7BGyM_Vsub7U9xBVcbXb18o_BV9Z7b1cZbHIzZbVPIX3HUNi_GbPRoUNbRt_HXt-JYcTI7l7K-GeQS29iJlfP9t4QiB1Yld-0ZeVFh65nFModHaRIU8UkbDV5TKa6P5JqqM-1euQr85I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارة الخارجية العراقية: وفاة أحد الصيادين العراقيين الذين تم اعتقالهم من قبل خفر السواحل الكويتي.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/82261" target="_blank">📅 23:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82260">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حاكم مدينة كنارك الإيرانية: الأجهزة المعنية هرعت على الفور إلى موقع الهجوم والتحقيق جار في أبعاده وتفاصيله</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/82260" target="_blank">📅 23:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82259">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مكتب نتنياهو: أطلع ترامب نتنياهو على التحركات الأمريكية ضد إيران.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/82259" target="_blank">📅 23:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82257">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇶
الإطار التنسيقي في العراق : نتقدم بخالص الشكر والتقدير إلى جميع المشاركين وإلى كل من أسهم في تنظيم وإقامة مراسم تشييع نعش السيد علي الخامنئي في النجف الأشرف وكربلاء المقدسة</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/naya_foriraq/82257" target="_blank">📅 23:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82256">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔻
مصادر لنايا: الصواريخ الأخيرة التي استهدفت إيران انطلقت من الكويت</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/naya_foriraq/82256" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82255">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مصدر إيراني ينفي وقوع انفجارات في بندر عباس وقشم وسيريك وجاسك.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/naya_foriraq/82255" target="_blank">📅 23:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82254">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">محافظ بوشهر الإيرانية: نحقق في أسباب الانفجارات في بوشهر وجغادك إن كانت ناجمة عن دفاعات جوية أو مقذوفات معادية</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/naya_foriraq/82254" target="_blank">📅 22:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82253">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇺🇦
🇷🇺
الجيش الأوكراني يعلن مقتل أربعة من أفراد طاقم طائرة هليكوبتر من طراز Mi-8 بعد تحطم الطائرة أثناء اعتراض طائرات بدون طيار روسية في منطقة بولتافا في 30 يونيو.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/naya_foriraq/82253" target="_blank">📅 22:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82252">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مصدر إيراني ينفي وقوع انفجارات في بندر عباس وقشم وسيريك وجاسك.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/naya_foriraq/82252" target="_blank">📅 22:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82251">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd6632e1f9.mp4?token=nTjP0TOa527tv_uzZY5iAsB2CjeyzxPP8Y8UKgQze9EUKaXk36EV_SKX3IL5hsxq-R-00PEASS347PzkCFwYeBd4DC8BYOEFEeToYgt_NTtZJZ3RekHCNCCluv5_o2Sj08wyMPFZa3_D71ZUrLXJqN-9yV0DLAW4Bz9ZAUf7Tw7tuMw2rrsYWjv2sYwpd8b2LxEP_PtQqLgJlB4Nwdh_yKzrnErkaZ9zb2ipLwLmZIWPO7bJxJ-60YbOYxh60H5R6ip--dc7ucZv6qhbGg6mRukDpwut6YKGivVFTajhYJypVi7O6k_a1GGhEdS2-a_pSFe3F33rqitKYBoH74Z71w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd6632e1f9.mp4?token=nTjP0TOa527tv_uzZY5iAsB2CjeyzxPP8Y8UKgQze9EUKaXk36EV_SKX3IL5hsxq-R-00PEASS347PzkCFwYeBd4DC8BYOEFEeToYgt_NTtZJZ3RekHCNCCluv5_o2Sj08wyMPFZa3_D71ZUrLXJqN-9yV0DLAW4Bz9ZAUf7Tw7tuMw2rrsYWjv2sYwpd8b2LxEP_PtQqLgJlB4Nwdh_yKzrnErkaZ9zb2ipLwLmZIWPO7bJxJ-60YbOYxh60H5R6ip--dc7ucZv6qhbGg6mRukDpwut6YKGivVFTajhYJypVi7O6k_a1GGhEdS2-a_pSFe3F33rqitKYBoH74Z71w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنشر لأول مرة
رئيس أركان الحشد الشعبي الحاج ابو فدك المحمداوي يقوم بمسح مقتنيات المشيعيين طلبوا النذر والذكرى من الضريح الشريف.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/naya_foriraq/82251" target="_blank">📅 22:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82250">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">أنباء عن تفعيل الدفاعات الجوية في شابهار وسيستان وبلوشستان إيران</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/82250" target="_blank">📅 22:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82249">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اكسيوس نقلا عن مصدر أمريكي : ليس لنا أي علاقة باي ضربة ع إيران حاليا</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/82249" target="_blank">📅 22:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82248">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اكسيوس نقلا عن مصدر أمريكي : ليس لنا أي علاقة باي ضربة ع إيران حاليا</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/82248" target="_blank">📅 22:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82247">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اكسيوس نقلا عن مصدر أمريكي : ليس لنا أي علاقة باي ضربة ع إيران حاليا</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/82247" target="_blank">📅 22:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82246">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔻
مصادر لنايا: الصواريخ الأخيرة التي استهدفت إيران انطلقت من الكويت</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/82246" target="_blank">📅 22:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82245">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مصدر إيراني ينفي وجود انفجارات في جزيرة خرج</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/82245" target="_blank">📅 21:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82244">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=md4BjzMZr9oZGlTlcxd4XbosuSYXTuF3_RB9_hxdj5X3BE7C-625DoFD8P6JUZjYcdhSX1V7rXd3FPluWBb-O3Qwxcks04IGLZC03MzmEJs0734RIDWz737Ww-TD5u099vWTwPdDgHhEi1o63wRrKOvz31vX04nKgMF443Ut7b6vCkcFw319eNqUxcS-n0LBFu9uBiLqBYERGODJLftjKKRiyLIGMBrJRdFFVDU_NZrmqWrVv6tQw__vnd_LrUxKrP9f9SS1QMSynmYnEO0U2qQ2pPifcBb_DP-7by9M3SqSN9bq8d47mz_STQRlTiHIwzRrgPssQHluEosuB4CAvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=md4BjzMZr9oZGlTlcxd4XbosuSYXTuF3_RB9_hxdj5X3BE7C-625DoFD8P6JUZjYcdhSX1V7rXd3FPluWBb-O3Qwxcks04IGLZC03MzmEJs0734RIDWz737Ww-TD5u099vWTwPdDgHhEi1o63wRrKOvz31vX04nKgMF443Ut7b6vCkcFw319eNqUxcS-n0LBFu9uBiLqBYERGODJLftjKKRiyLIGMBrJRdFFVDU_NZrmqWrVv6tQw__vnd_LrUxKrP9f9SS1QMSynmYnEO0U2qQ2pPifcBb_DP-7by9M3SqSN9bq8d47mz_STQRlTiHIwzRrgPssQHluEosuB4CAvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظات من الصلاة على جثمان "شهيد إيران" والمرجع الأعلى للشيعة في العالم، سماحة آية الله العظمى السيد علي الحسيني الخامنئي، من قبل آية الله الحاج السيد مصطفى الحسيني الخامنئي.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/82244" target="_blank">📅 21:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82243">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سماع انفجارات في بندر عباس</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/82243" target="_blank">📅 21:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82242">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">عدوان على الأهواز</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/82242" target="_blank">📅 21:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82241">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/799e0dcd32.mp4?token=vaU8dSVyTZLES9_Xsmy1mk_qt0vJ2hy7lhC6C4k9Z0g4vczJ92bie05LqszsnmGFE98qOYUpUJi_1pkpIEThWEjJFY_I_xP5tiVcEf34dqV0PI-Edm4kTguw5wvpV5tG1CecDqgi4FQ3kR-e88cslEKmg4hbWPoKnd3vFDYTxhAVXtjR9QL9jfl6T1hzG6WsZThd2xlM4tby7L0yj2u-cakFncN1OMlbOuZDOYWxyMfZZQI3TMQ2MrzQOtEQK6zZ6MXYuGiX1cS2Exks158TPoz7A9ff3tGMBOjec8pmjVXTpf-kl5qNUxrE7jqOkdIUjMR6KXpd-p4AVXlWEhi7gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/799e0dcd32.mp4?token=vaU8dSVyTZLES9_Xsmy1mk_qt0vJ2hy7lhC6C4k9Z0g4vczJ92bie05LqszsnmGFE98qOYUpUJi_1pkpIEThWEjJFY_I_xP5tiVcEf34dqV0PI-Edm4kTguw5wvpV5tG1CecDqgi4FQ3kR-e88cslEKmg4hbWPoKnd3vFDYTxhAVXtjR9QL9jfl6T1hzG6WsZThd2xlM4tby7L0yj2u-cakFncN1OMlbOuZDOYWxyMfZZQI3TMQ2MrzQOtEQK6zZ6MXYuGiX1cS2Exks158TPoz7A9ff3tGMBOjec8pmjVXTpf-kl5qNUxrE7jqOkdIUjMR6KXpd-p4AVXlWEhi7gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران في مدينة كنارك الإيرانية</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/naya_foriraq/82241" target="_blank">📅 21:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82239">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تفعيل الدفاعات الجوية في بوشهر الآن</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/82239" target="_blank">📅 21:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82238">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">أنباء عن تفعيل الدفاعات الجوية في شابهار وسيستان وبلوشستان إيران</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/82238" target="_blank">📅 21:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82237">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">أنباء عن تفعيل الدفاعات الجوية في شابهار وسيستان وبلوشستان إيران</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/82237" target="_blank">📅 21:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82236">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">أنباء عن تفعيل الدفاعات الجوية في شابهار وسيستان وبلوشستان إيران</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/82236" target="_blank">📅 21:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82235">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cb7818d5a.mp4?token=Gh4loOcnpxZZGDJ3qM0vZ3vYlx0iQewK8t9bRnturJrqFT0dHQFZ8jds7Vng_Lk-jv_75O7zI_ylLX5aQ1H08Gf7JHK1345G44uBNYIjILV5598Z2UqZMbFf-WDebCzJHNg6B2VQpVtK215hhhYHelxa7oR8vpNlbs06aP28wasNvdvNX8jgM7mPqzpr2t6Q1U3xZhpJgCBf1ee8nWSxQBABpUexAJ3a1zprsVIXbJMI_vnHmkFXbJHkI8_hV_rpyD6rWRvihD6Sr-m3n6teAGY8VrPxyMFklWhSqDmnEsjqLBRFn4IYPSgSh6VqSxFl6bLZBKciuYxppGk-9dURwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cb7818d5a.mp4?token=Gh4loOcnpxZZGDJ3qM0vZ3vYlx0iQewK8t9bRnturJrqFT0dHQFZ8jds7Vng_Lk-jv_75O7zI_ylLX5aQ1H08Gf7JHK1345G44uBNYIjILV5598Z2UqZMbFf-WDebCzJHNg6B2VQpVtK215hhhYHelxa7oR8vpNlbs06aP28wasNvdvNX8jgM7mPqzpr2t6Q1U3xZhpJgCBf1ee8nWSxQBABpUexAJ3a1zprsVIXbJMI_vnHmkFXbJHkI8_hV_rpyD6rWRvihD6Sr-m3n6teAGY8VrPxyMFklWhSqDmnEsjqLBRFn4IYPSgSh6VqSxFl6bLZBKciuYxppGk-9dURwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مديرية الإعلام في الحشد الشعبي:
ويأتي الشكر، من حيث ينبغي أن يبدأ، إلى القائد المشرف ميدانياً على الجزء الأكبر من هذا الحدث، رئيس أركان هيئة الحشد الشعبي أبو فدك، الذي كان حاضراً في الميدان طوال ساعات العمل، يتابع التفاصيل لحظةً بلحظة، ويقود الجهد التنظيمي والأمني كما تُقاد المهام الكبرى، حتى اكتملت هذه المراسم بالصورة التي تليق بعظمة المناسبة.
كما نتقدم بعظيم الامتنان إلى رئيس هيئة الحشد الشعبي الأستاذ فالح الفياض، وإلى جميع قادة العمليات ومديري المديريات ومنتسبي هيئة الحشد الشعبي، الذين واصلوا الليل بالنهار لأيام طويلة، وسخروا جميع الإمكانات الأمنية واللوجستية والخدمية، وفاءً لواجبهم الوطني والأخلاقي، وإيماناً منهم بأن خدمة هذا الحدث مسؤولية تاريخية قبل أن تكون مهمة وظيفية.
وأخيراً، فإنني أعتذر لكل الشخصيات والمؤسسات والمديريات والكوادر التي لم تُذكر أسماؤها في هذا البيان، ليس انتقاصاً من دورها أو غفلةً عن فضلها، وإنما خشية الإطالة، أو بسبب الإرهاق الذي رافق أيام العمل المتواصل. فلكل من أسهم، صغيراً كان أم كبيراً، بصمة ستبقى محفورة في ذاكرة هذا اليوم التاريخي، وسيظل العراق يعتز بما قدّمه أبناؤه من صورة مشرّفة في الوفاء والتنظيم والانتماء.
﻿</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/82235" target="_blank">📅 21:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82234">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔻
مديرية الإعلام في الحشد الشعبي:
نخص بالشكر المدونين والمؤثرين في شبكات التواصل الاجتماعي، الذين كان لهم دور بارز في إيصال رسالة هذا الحدث التاريخي إلى العالم، إذ حققت المواد الإعلامية الخاصة بالمراسم عبر مختلف المنصات مئات الملايين من المشاهدات والتفاعلات، لتؤكد الحضور الاستثنائي لهذا الحدث في الفضاء الرقمي، وتعكس صورة مشرقة عن وفاء العراقيين وعظمة هذه المناسبة.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/82234" target="_blank">📅 21:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82233">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c8950292.mp4?token=WVsyYIy5bm5-dMIl9RFCSmh9q2CxI4jvrNeLnwW5u32eEch1k3Zfy-t37gljzi_jMnmaV_kugiCQehNO-Dw9wnSvVaOWoRSwdMMzlp9RwTiHtkOnSS8a_gx3IzUCT_g6oHF1YuHhk3VN0RN2E12E68Wt0fPB4vuclE3UtozZpXfLEzGqTZspqds8BNrvHp4O4NCywQKX8oKTxXiVE2wvKK1XSjllh8kJ8ruQxB8ouNzGZxUE46P5JNMF9y8KkHPK64Atyz3SXkvA8DOq-Ulaln-HaU5bxbcskBGBUVvMpUFX7IFkEmnbdV2-7lmOW98sAHA8UyM6LDH95fZVCgW-VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c8950292.mp4?token=WVsyYIy5bm5-dMIl9RFCSmh9q2CxI4jvrNeLnwW5u32eEch1k3Zfy-t37gljzi_jMnmaV_kugiCQehNO-Dw9wnSvVaOWoRSwdMMzlp9RwTiHtkOnSS8a_gx3IzUCT_g6oHF1YuHhk3VN0RN2E12E68Wt0fPB4vuclE3UtozZpXfLEzGqTZspqds8BNrvHp4O4NCywQKX8oKTxXiVE2wvKK1XSjllh8kJ8ruQxB8ouNzGZxUE46P5JNMF9y8KkHPK64Atyz3SXkvA8DOq-Ulaln-HaU5bxbcskBGBUVvMpUFX7IFkEmnbdV2-7lmOW98sAHA8UyM6LDH95fZVCgW-VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحضير مكان دفن جثمان الشهيد السيد علي الخامنئي في حرم الإمام الرضا (عليه السلام).</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/82233" target="_blank">📅 21:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82232">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">على الرغم من رفض نتنياهو للانسحاب
‏مسؤول أميركي: سيتم تحديد أول منطقة تجريبية تنسحب منها إسرائيل من لبنان خلال أيام</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/82232" target="_blank">📅 21:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82231">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">كان العبرية: في إسرائيل، يُعتقد أن الاشتباكات بين إيران والولايات المتحدة ستستمر في الأيام القادمة في الوقت الحالي، يتعلق الأمر بصراع بين الولايات المتحدة وإيران، دون تدخل إسرائيلي ومع ذلك، على الرغم من ذلك، فإن كبار المسؤولين في إسرائيل كانوا يرغبون في الحصول على موافقة من ترامب لشن هجمات إسرائيلية بمفرده</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/82231" target="_blank">📅 20:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82230">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">لقطات متنوعة عراقية حشداوية
من تشيع السيد القائد الخامنئي بين كربلاء المقدسة والنجف الأشرف</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/82230" target="_blank">📅 20:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82229">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔻
نائب العمليات في منظمة الإطفاء في زنجان الإيرانية: نفي وقوع انفجار في زنجان ومصدر الدخان ناتج عن حريق في ورشة إعادة تدوير.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/82229" target="_blank">📅 20:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82228">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مسؤول أميركي: الصواريخ والمسيّرات الإيرانية لم تسبب أضرارا جسيمة
أمريكا تتملص من الرد بحجة الأضرار غير جسيمة</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/82228" target="_blank">📅 19:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82227">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">"سي ان ان" عن مصادر: قطر وباكستان تعملان على إعادة أميركا وإيران إلى طاولة المفاوضات</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/82227" target="_blank">📅 19:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82226">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اسماعيل بقائي: ‏
سافر الرسول من بلاد فارس إلى خراسان عن طريق السفينة.
‏إذا فاضت عيناي بالدموع خلفها،
‏صرخةٌ ينبغي أن أكتبها على شكل وداعك
‏فليخرج صراخ من قلب كل من يقرأه.
‏سعدي
‏اليوم، تُودّع إيران شهيدها إلى مثواه الأخير، وتُسلمه إلى علي بن موسى الرضا (عليه السلام). إن جسد رجل عظيم يقع على أكتاف شعبٍ دافع عن هذه الأرض لسنواتٍ طويلة في وجه تقلبات الأحداث، وحافظ على وحدتها وقوتها في وجه كل أنواع الاضطرابات، ثم سعى إلى الشهادة في سبيل الله، ونال هذه الرحيلة المجيدة.
‏طويل القامة، كشجرة السرو الإيرانية، يستمتع دائماً بشمس المقاومة والمثابرة، وقامته، كظل ثابت، امتدت فوق هذه الأرض؛ أصبح "السيد الوطني" في النهاية "نار إيران".
‏في ثقافتنا الإسلامية، لا تُعدّ الشهادة نهايةً للحياة، بل بدايةً لحياةٍ أخرى؛ إنها تحررٌ من ضيق الدنيا وانضمامٌ إلى رحابة القرب الإلهي. فمن منظور هذا المذهب، لا يغيب الشهيد عن الدنيا، بل هو حيٌّ بفضل وعد الله، ويرزقه ربه. لذا، فالشهادة ليست نهاية المجاهد، بل هي ذروة مسيرته ولحظة لقائه بالحبيب الأبدي.
‏إن قافلة الشهداء، من كربلاء إلى يومنا هذا، هي خيط لا ينقطع في تاريخ الإيمان والسعي وراء الشرف؛ خيط كل حلقة فيه هي استمرار لنفس الطريق الأحمر ونفس العهد الأبدي مع الحقيقة، "الذي لا يبايعه أحد مثله".
‏في عيون العثّات العمياء، يمكن إلقاء رجال الله في التراب، ولكن في عيون رجال الله، جسدهم وروحهم كالبخور الذي تفوح منه رائحة شهية من لهيب الاستشهاد:
‏قال المفرقع سراً للدخان
‏قلبي لا ينبض وأنا سعيد بالعودة.
‏أتمنى أن يدرك قيمتي وأن يكون ممتناً لي.
‏رأى كاندير في هلاكه عودة للربح.
‏كان العود مربوطاً بعقد من رأسه إلى أخمص قدميه.
‏تم فتح باب الغياب لتلك العقود.
‏أهلاً وسهلاً بك يا صديقي آكل اللهب.
‏يا أيها الفاني، يا شهيدي، يا الشاهد الفخور!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/82226" target="_blank">📅 19:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82225">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">#ترفيهي
‏بيان لدول مجلس التعاون الخليجي: ‏أي اعتداء على أي دولة في المجلس هو اعتداء مباشر على كافة دول الخليج</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/82225" target="_blank">📅 18:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82224">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بدأ نقل جثمان قائد الثورة الشهيد إلى حرم الإمام الرضا (ع) لإقامة صلاة الجنازة والدفن</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/82224" target="_blank">📅 18:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82222">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t8YvgoW7sJLd6x2O5gU_nz5eHgmYyZOc3z-jplpiyKEJCyrkbbFOtHQC3nipFaadTOWwViXBvvqprIhvvSS-nOy5QGvvCkGiCCeP0KTPUphnvIP_--6jFY4Q8RAzi8_nqpfwJv4Su1fZFuyUdwaTis8mkv_ttAHFv2o1-pzGuXzMRqQWC1F8rDv9JPRkLwKahOnzte3x_bHQUWSh3lSS9YyPWIk4sB7brx-fk--tG29HqgOPwNmQAihH8mOadL80qWdMYJbgpK919pdl4YOlMvFQnNEW83tC1GTZ86kff4LJcwrOJPDe8cskckjgljfvPJfE2N4X8piRyfL310SUuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eAN8AoUJu4jn_unN0gJB6AoDcU-Rm-aGLJYb-4fNs9wf5sAcxDxZpjqdUHaE_96cwaA_I4kRnmCt_Zr_sS-r0RN1XY-AH5gpMhnb3pXUEwcws8tqtURYPqYenQ5OWzY2HmE3bCYI6KnKfJpzO1hidtle3FFT-z1sDN73GVMIFqKrhhexRWPVsHsSN7WXH9vUajILT4w1_hbHnR511FkJpC-c00L833Yn9o9xhzAcdZOP1ODXCQKDfDj_y9scWJEQpY4CPoZkLki-yNnmTAFM2CQg_O_DQsvhbG3uKAQaKA3LGT2AopTBHZW04lOY1G0nRL4hPvj3OXRrxLOe4NmVYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طيران التزويد بالوقود الأمريكي ينشط في سماء الأردن هذه اللحظات</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/82222" target="_blank">📅 18:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82221">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔻
نتنياهو: لو لم نتحرك لكانت إيران قد امتلكت أسلحة نووية والحرب لم تنته بعد وتحديات جديدة تبرز أمامنا</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/82221" target="_blank">📅 18:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82220">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-17_7MPJI3L2flGbzLq1QcxNNCIHQw0_nD77Q3UX6aPrBHb8kPLfFxv1mv1MXF8WzVZlM9EqrjkMrwarv_U8qgqb9cSIwq5CN7ZN8bhYryXeq-eC865KRkmTEHM6Okgai-lY9cKx4xGsD_ZHbEGYi_UCJ8Ss-NoAp7jsnZiu5IZYL4JScQac1zbQoDCkRqrP8k6IUmHNXzmhYhD9Kf13G2SmrutTRcoZXpc9m73bm5DiYShqBM-OFaPxRy9Uu7MXyayG0rSBBFDeM5Z8MBXVyjTRadl0ge2Xo2ylNdPqqtq-EKTUpN5ufm3Ig83wEj3MUkgDCzGY2IxAgGPeTTMgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران التزويد بالوقود الأمريكي ينشط في سماء الأردن هذه اللحظات</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/82220" target="_blank">📅 18:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82219">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhO-TpiEn9JKZtMV9eLQggvlkSUG9qqMuGvsze43EyQNX5bxYsu6KOGTU7rHHh9SaH6QfrzvZfQQQbWTdxJJOY9UUP3pLytWeF6-3C6-2JxIkhkj9akv3TYRAy4lzSXXqYDelVQEWP1tUyVRH0tb79g8PGUmE3J4x_m9V4wcnToLbryOwdfM1g6_csu2WGrwUjRMYLpu8xg8427qHYGsFXZEmWhmdub1vnFjmtf_fMmAJpxoBbZAjZlXx8qSjT2ZayjER2MQ-9zkQ-fp7XMVO-lVnn_9pVqNWilb2qWJ-MCa2v1QNGxwMLbPLNunsrbrILbMCJwJVZ0n6cjrmdKAfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحاج ابو فدك المحمداوي في الصف الأول يتصدر جموع المشيعين في مشهد المقدسة</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/82219" target="_blank">📅 18:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82218">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏وزير دفاع الاحتلال برسالة لـ إيران: جيشنا في حالة تأهب واستعداد لاستئناف المعركة</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/82218" target="_blank">📅 18:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82217">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بدأ نقل جثمان قائد الثورة الشهيد إلى حرم الإمام الرضا (ع) لإقامة صلاة الجنازة والدفن</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/82217" target="_blank">📅 18:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82216">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وزارة الخارجية العراقية: وفاة أحد الصيادين العراقيين الذين تم اعتقالهم من قبل خفر السواحل الكويتي.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/82216" target="_blank">📅 18:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82215">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وزير الخارجية الايراني لقائد الجيش الباكستاني: من حق إيران الدفاع عن نفسها ضد أي مغامرات أخرى من جانب الجيش الأمريكي</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/82215" target="_blank">📅 18:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82214">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇶
هيئة الاعلام والاتصالات العراقية: العراق سيأخذ من شركة ستارلينك 9% من واردات الشركة 8% مباشر و1% للخدمة الشاملة الى جانب 15% الضريبة المفروضة على شركات الاتصالات</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/82214" target="_blank">📅 18:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82213">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇶
هيئة الاعلام والاتصالات العراقية: العراق سيأخذ من شركة ستارلينك 9% من واردات الشركة 8% مباشر و1% للخدمة الشاملة الى جانب 15% الضريبة المفروضة على شركات الاتصالات</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/82213" target="_blank">📅 18:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82212">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇶
هيئة الاعلام والاتصالات العراقية:
العراق سيأخذ من شركة ستارلينك 9% من واردات الشركة 8% مباشر و1% للخدمة الشاملة الى جانب 15% الضريبة المفروضة على شركات الاتصالات</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/82212" target="_blank">📅 18:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82211">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇺🇸
القائم بالاعمال الامريكي في بغداد:
نتشاور مع الحكومة العراقية لدعم خيارات العراق لبناء المرونة فيما يتعلق بإنتاج الكهرباء على المدى القصير.
لعد جنرال الكتريك شجانت تسوي من 2003 ولليوم ، يومية موقعين عقد وياها وضخ فلوس ونفس الطاس ونفس الحمام
😄</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/82211" target="_blank">📅 17:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82210">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb52071cdf.mp4?token=QkCTA7AllPCjmEeS4IzLLB1XbfxFxRYjAP9XoTz3yw-EAxBWUmdspeXy4uwQeWvHCXqJFHZeiM9vt4vRN-m_ZGuTTPDD6WhBg6OT7XPTJa4CRY8fVl0gTO6PXdC9wcvjD9Y6sE0SaN2cpkJh-lK1B-FJ7De255KocZIjNYuB7PuAe-HQPuELC-4ljqxmH9O7O32nd71_HPBU7snU9yHBhznrOJZi4_C_nnwTjlOcL-WMirb5ed3H7lFxAopA-xb-5uz2RssTLsIRftiAsQXcezLXjlPcmHOMLie6D_8nij6LxgNTKpW0H75o5xZ8pHb9IYVdSet8FwmmyHxRTttZAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb52071cdf.mp4?token=QkCTA7AllPCjmEeS4IzLLB1XbfxFxRYjAP9XoTz3yw-EAxBWUmdspeXy4uwQeWvHCXqJFHZeiM9vt4vRN-m_ZGuTTPDD6WhBg6OT7XPTJa4CRY8fVl0gTO6PXdC9wcvjD9Y6sE0SaN2cpkJh-lK1B-FJ7De255KocZIjNYuB7PuAe-HQPuELC-4ljqxmH9O7O32nd71_HPBU7snU9yHBhznrOJZi4_C_nnwTjlOcL-WMirb5ed3H7lFxAopA-xb-5uz2RssTLsIRftiAsQXcezLXjlPcmHOMLie6D_8nij6LxgNTKpW0H75o5xZ8pHb9IYVdSet8FwmmyHxRTttZAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔰
كما قال الشيخ أكرم الكعبي: سلاحنا وديعةُ الإمام الحجة (عج) وقد تجلت آثار هذه الوديعة في مشهد الوفاء المليوني الذي شهدته النجف في وداع الإمام الخامنئي (رض)
#قوموا_لله
#كونوا_احرارا
ً</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/82210" target="_blank">📅 17:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82209">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏وزير الطاقة التركي: نخطط لتوقيع اتفاقية مع العراق بشأن خط أنابيب لاستمرار تصدير النفط لـ12 شهر اخرى.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/82209" target="_blank">📅 17:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82208">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مطار النجف الاشرف الدولي يعود للعمل امام الرحلات التجارية بعد الإغلاق المؤقت</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/82208" target="_blank">📅 17:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82207">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇷
بيان لحرس الثورة الاسلامية:
بسم
الله
قاصم
الجبارين
«
فَمَنِ
اعْتَدَىٰ
عَلَيْكُمْ
فَاعْتَدُوا
عَلَيْهِ
بِمِثْلِ
مَا
اعْتَدَىٰ
عَلَيْكُمْ
»
لقد ذكرنا في البيان السابق أن تكرار العدوان سيوسع نطاق ردنا ليشمل قواعد العدو الأخرى في المنطقة، وفي المرحلة الثانية من الرد على اعتداءات الجيش الأمريكي القاتل للأطفال، قمنا بتحويل هذا التهديد إلى فعل
دكّ مقاتلو القوة الجوفضائية التابعة للحرس الثوري في تمام الساعة 14:20 من بعد ظهر اليوم مركز قيادة وسيطرة العدو في غرب آسيا وقاعدة العدو الجوية في الأزرق بالأردن بـ 10 صواريخ باليستية
في حال تكرار عدوان الجيش الأمريكي الإرهابي، لن تكون بقية القواعد الأمريكية في المنطقة في مأمن من نيراننا الكثيفة
وما
النصر
إلا
من
عند
الله
العزيز
الحكيم</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/82207" target="_blank">📅 16:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82206">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/643cebc914.mp4?token=fJnjJy-D1XxPrUJNPli149cXUkSNglIUqRihCyo9idr6UvqBCmfxCZu6TWT3v9zPQkZ_O7jdDlUmXNAfizC6W49ATV6s3eeXWu1-Xrm12Xfx6sXoYl4VcAHRF-cmmJ9elSGWvO6UUq4znniERvEm9fZOQDLJwHWI8inQqTMluBf2F0L3nSRy5ZT8Bpf74BLLcRhATnPtT9mbHvRXT_Ejsv3x0Dt9sQ4A-qtATFuKITu0KZd0cZ2sbazqJd_hyFGqFmH1-68Qv7N5rEPoBWbMeDrBEv-aNY4bkE1c1_loN74_1H0N4BoQzzmAZ4m7DkzUsobSrupUUu2yzCtCif88eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/643cebc914.mp4?token=fJnjJy-D1XxPrUJNPli149cXUkSNglIUqRihCyo9idr6UvqBCmfxCZu6TWT3v9zPQkZ_O7jdDlUmXNAfizC6W49ATV6s3eeXWu1-Xrm12Xfx6sXoYl4VcAHRF-cmmJ9elSGWvO6UUq4znniERvEm9fZOQDLJwHWI8inQqTMluBf2F0L3nSRy5ZT8Bpf74BLLcRhATnPtT9mbHvRXT_Ejsv3x0Dt9sQ4A-qtATFuKITu0KZd0cZ2sbazqJd_hyFGqFmH1-68Qv7N5rEPoBWbMeDrBEv-aNY4bkE1c1_loN74_1H0N4BoQzzmAZ4m7DkzUsobSrupUUu2yzCtCif88eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
لحظة تدمير طائرة MQ9 الامريكية بواسطة الدفاع الجوي الايراني.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/82206" target="_blank">📅 16:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82205">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇩🇿
شركة سوناطراك الجزائرية: حادث في مصفاة أرزيو.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/82205" target="_blank">📅 16:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82204">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">قطر توقف زيادة إنتاج الغاز الطبيعي المسال بعد الهجوم على ناقلة النفط في مضيق هرمز</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/82204" target="_blank">📅 16:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82203">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇷
قائد مقر خاتم الانبياء المركزي:
هذا الحزن والغضب سيستمران في طريق الثأر لقتلة القائد الشهيد، القوات المسلحة ستعمل، بدعم الله والشعوب المسلمة، على محاسبة منفذي ما وصفها بالجرائم الإرهابية</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/82203" target="_blank">📅 16:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82202">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وزارة الخارجية العراقية:
وفاة أحد الصيادين العراقيين الذين تم اعتقالهم من قبل خفر السواحل الكويتي.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/82202" target="_blank">📅 16:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82201">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🌟
مجلس النواب العراقي يُصوت على إعفاء رئيس الهيئة الوطنية للاستثمار حيدر مكية من منصبه واحالة الملفات إلى هيئة النزاهة.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/82201" target="_blank">📅 15:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82200">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7-Wck-hf77HL5cmQObwM1SZ7sErfT53hyq72pWRE0xHkNSc91I_Arigiwyt6P-GRK1C734dAoHD_P-OCjX09RPfYY6M_0bf6rEJd7V1MnC3exB9u-oX2OcGDzSi0kTHyYMQOjEozV6LTlEf_St-ZPHACO2U_ZR8JA01CL4Y-3jHkSdniQ2KsOmsoqwAjQHSkWRUXeopv9snbWzrjoxNhwudxpdMmNoR1aMeuVI22Ic_e5RcikttdvN8yQsa7jkL_cS-EBZIuf0T_xA8Nu5bRI91t0zv0dKPUTbypupqYn0l1vZkpR1kdI-yI7I9dH74cSbVNY0iFA_z4QZ3iesDBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
جهاز الأمن الوطني العراقي يعلن إلقاء القبض على أحد تجار المخدرات الدوليين ينتحل صفة "إعلامي حربي" كما تم ضبط ما يزيد على 111 ألف حبة من نوع كبتاجون بحوزة متهم اخر في محافظة ذي قار</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/82200" target="_blank">📅 15:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82199">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇺🇸
‏
القيادة المركزية الأميركية:
ضربنا أكثر من 170 هدفا في إيران خلال اليومين الماضيين</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/82199" target="_blank">📅 15:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82198">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇬🇧
وزيرة الخارجية البريطانية:
إيران ترغب في بقاء مضيق هرمز رهينة لديها</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/82198" target="_blank">📅 15:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82197">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCnlDfXaUMi5CKZBR9BgccdsihCFoOFixn6y2pFcZi8-lUHVjq37r3WvfyuLnA2CnNACZrIkM8diAnZiAqRZb-mWAtrzpcBST4ZVHTKW4yIDEZqIiDz1k19008KI6dUKh-9Y3eGMdsmd428zTKa1jfOiGhv6aVfuU_YoiFTjDzATkcclrwInNAbPLD12YXlDhkbyqdKmQrbvEUxuAlM3U7lFvadP5w7h_2HharAx99qKcOxKndKxbpyDAgv1PBiEHYtjY3TmXVkTiVXAvEYP3f2spzdb-pUDrqzPWVxnZ_DtzBR37ZSlzO4VWOZ_sXQJCVWDSqFDJ2GHwcPzCfx8Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدر إيراني مطلع: تحليق طائرات مقاتلة تابعة للقوات المسلحة الإيرانية لتأمين سماء مدينة مشهد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/82197" target="_blank">📅 15:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82196">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الله اكبر
اطلاقات جديدة ضخمة من ايران</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/82196" target="_blank">📅 15:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82195">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اللجنة المنظمة لمراسم تشييع قائد الثورة في العراق: الإحصاءات الأولية غير الرسمية تشير الى مشاركة اكثر من 10 ملايين شخص في التشييع.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/82195" target="_blank">📅 15:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82194">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b16f8a8793.mp4?token=eWMqntsCx8zSWHZ-eYa5lxFQHAbS73zeP49iZ_YGksedOy7WUXyu_BTwKMzeTiFFEvzCqL_nyTgv6C6gEf-0bZ1LOa9kp3yrvN-l_WXCk3qAmj4fokvN3hFcOJwd-LRrQx-ABqb9HwawO9_AMridQw3ZvkhJnhLR-u-mvYnFiMyO5_ZnagXwT3zHlk8QaNpbKTGvq0xS34V3ordynfrTgwTwAajxYOxlrkhiAY-4eo4jrnkFn7NnF_fUECq3imRJhvQO5p3UDDFRSjIRxXZ10FIWxaUgAGA5iYzJt3T_jsMjHDvfenkCB2W6JJ4tTXGnBevvANUUGqN5nT9Bnqby3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b16f8a8793.mp4?token=eWMqntsCx8zSWHZ-eYa5lxFQHAbS73zeP49iZ_YGksedOy7WUXyu_BTwKMzeTiFFEvzCqL_nyTgv6C6gEf-0bZ1LOa9kp3yrvN-l_WXCk3qAmj4fokvN3hFcOJwd-LRrQx-ABqb9HwawO9_AMridQw3ZvkhJnhLR-u-mvYnFiMyO5_ZnagXwT3zHlk8QaNpbKTGvq0xS34V3ordynfrTgwTwAajxYOxlrkhiAY-4eo4jrnkFn7NnF_fUECq3imRJhvQO5p3UDDFRSjIRxXZ10FIWxaUgAGA5iYzJt3T_jsMjHDvfenkCB2W6JJ4tTXGnBevvANUUGqN5nT9Bnqby3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الخارجية القطرية ندين الاعتداء الإيراني على الاردن
#مبلاش
افتكر انا قلتلك مبلاش</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/82194" target="_blank">📅 15:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82193">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اطلاقات اضافية من ايران باتجاه القواعد الامريكية في الاردن</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/82193" target="_blank">📅 15:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82192">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بحرية الحرس الثوري بشأن مضيق هرمز: بسم الله الرحمن الرحيم
🔹
تحية للأمة البصيرة والشجاعة التي أظهرت، بحضورها المذهل وتشييعها لملايين من شهيد القائد في إيران والعراق، أن هذا هو الزمان الذي ينتهي فيه جبروت القوى، وأن هذا القرن هو عصر هيمنة إرادة الأمم.
🔹
وتحية…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/82192" target="_blank">📅 15:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82191">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoKWyCsG_-ymplio2EJ2jzSLirbJeGbUC-ATUGiht5DqAZAMc-6Ww2606tbEPnj1rFVsIGAJPSm4SwjG99NepXn-r85KzkoP6MatTeBAf56aTnWo4zwGMyN1WpnTnoi6iIIh5fy3ddE4nQqdI0mMsxSEI1vuvneC15NGGIVU9le7LeIRV1lz24Ruawf5_i-dmkeYpBf__D3GWr1bcDOsUjultlGV3cvpA444r1oQ3tAcXSQ1YqBadmloCw95cthWJPBiZ3TsG0qmLHk6qGMp5Et32WQ9HvB8AbE1ncak9SZ6Ofew4CSfVM_MV-NusIbiKtj2x7ksiXhwCVD0N_4d-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بحرية الحرس الثوري بشأن مضيق هرمز:
بسم الله الرحمن الرحيم
🔹
تحية للأمة البصيرة والشجاعة التي أظهرت، بحضورها المذهل وتشييعها لملايين من شهيد القائد في إيران والعراق، أن هذا هو الزمان الذي ينتهي فيه جبروت القوى، وأن هذا القرن هو عصر هيمنة إرادة الأمم.
🔹
وتحية للمقاتلين الشجعان في الإسلام الذين أثبتوا، برد فعلهم القوي على انتهاكات الجيش الأمريكي الذي يقتل الأطفال، أن مصير المعركة لا يحدده امتلاك الأسلحة، بل قوة الإيمان.
🔹
المقاتلون الذين، خلال الأسبوعين الماضيين، عززوا سيطرتهم على مضيق هرمز وأمنوه، وبإعادة فتحه تدريجياً، رفعوا قدرة المرور إلى حوالي 50٪ من حركة السفن قبل الحرب، وهم بصدد زيادة قدرة حركة السفن التي تحصل على تصريح من قوات البحرية التابعة لحرس الثورة الإسلامية لعبور المسارات المحددة من قبل الجمهورية الإسلامية، مع الالتزام الصارم بقواعد الأمن.
🔹
نعلن مرة أخرى أنه لا يحق للأجانب أي حصة في هذه الأرض وفي مضيق هرمز. إن مغامرات الجيش الإرهابي الأمريكي وتدخله في تحديد مسارات المرور، بالإضافة إلى أنه سيواجه رداً قوياً منا، يعيق أيضاً عملية إعادة الفتح التدريجية، ويعرض مصالح الدول التي تستفيد من مضيق هرمز لخطر كبير.
قوات البحرية التابعة لحرس الثورة الإسلامية.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/82191" target="_blank">📅 15:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82190">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">الله أكبر
انفجارات تهز قاعدة موفق السلطي الجوية في مدينة الزرقاء مجددا</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/82190" target="_blank">📅 15:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82189">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انفجارات تهز الاردن</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/82189" target="_blank">📅 15:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82188">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">انفجارات تهز الاردن</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/82188" target="_blank">📅 15:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82187">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROxM2tW70tcnEluqA511X328Cq4cnfl8xDkbMh-YwfuD6HHRnGtEApdqSUxDsvLosmD8BVMmxIbAki2T-apRwy83dzBqm6zK6519_SbNSIKf0z1ctpdAWYymC4H4xZEPUy4VMxS71RDCMvIAJLOLAfmq7WhaD3MUXGJPESAliLpbSKdMtSQJGfaXcnacJNL4k2Kpmf-nDHF0kSngjEpBhSMGwtxqr7FKui1PPkwzSETTQEZxGh63v48Ub5XFLnzHByVl7hTpPs4qOKgVzYSPQ0iLWM5YUuj94jiEPAT54iSOpFXWQwxraqb5EtNW80QkTEVnSlHEFHPA6GrJz10W8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رصد نايا.. الإعلام الإيراني</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/82187" target="_blank">📅 15:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82186">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">احتراق طائرة أمريكية مقاتلة من طراز F 16 بظروف غامضة في مطار عسكري باليونان</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/82186" target="_blank">📅 15:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82185">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مصدر إيراني مطلع: الأنباء حول إنفجار في شيراز غير صحيحة والصور المتداولة على الإنترنت قديمة وتستخدم كجزء من الحرب النفسية للعدو.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/82185" target="_blank">📅 15:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82184">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سماع دوي انفجار في كرمان</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/82184" target="_blank">📅 14:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82183">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">انباء عن غلق الاجواء السورية</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/82183" target="_blank">📅 14:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82182">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">توقف شبه تام لحركة الملاحة في مضيق هرمز</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/82182" target="_blank">📅 14:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82181">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انفجارات عنيفة تهز أربيل</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/82181" target="_blank">📅 14:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82180">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">انفجارات عنيفة تهز أربيل</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/82180" target="_blank">📅 14:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82179">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نائب محافظ هرمزغان الإيرانية: في الهجمات العدوانية التي نفذها الجيش الإرهابي الأمريكي على الرصيف التجاري والصيادي في سيريك، استشهد 3 أشخاص وأصيب 15 آخرون.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/82179" target="_blank">📅 14:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82178">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏الجيش الأردني يدعي اعترضنا وأسقطنا 8 صواريخ إيرانية اخترقت أجواء البلاد</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/82178" target="_blank">📅 14:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82177">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">احتراق طائرة أمريكية مقاتلة من طراز F 16 بظروف غامضة في مطار عسكري باليونان</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/82177" target="_blank">📅 14:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82176">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دوي صافرات الإنذار بقاعدة فكتوريا بالقرب من مطار بغداد الدولي</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/82176" target="_blank">📅 14:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82175">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مصدر إيراني مطلع: تحليق طائرات مقاتلة تابعة للقوات المسلحة الإيرانية لتأمين سماء مدينة مشهد.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/82175" target="_blank">📅 14:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82174">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78ce8a7b3.mp4?token=kIElEe__eDgeZFtVRG_bJp7PRYIvnmCmqbNN4wz4MkFcfMpihXocpS_T5SNldyYo_Y90n3kxQTQ_9KFQ-7rv-RuSEIuD4e8BazBJSvxxT_rbw1Q397vvR79-QxQHC-o8vPYTruu3CxbplL0duDOvnFJ-gTPbWHGfe_aOmTUwRBVzwxHWxt28Yj6yjTZVsUY5CFtDNCDKGQG5FM9AiC8u150-aeBGKnX3zDVlixSKGbRkYHHiLLZ159r8DP-CAjL8FMFqwSytUa9l0ct_L-bl78zonoO3x1-_Ax5ZyojXV91tIXSPrW5xXmaXky8YzpYTc9PlvijSTtKu8sO2vE1CSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78ce8a7b3.mp4?token=kIElEe__eDgeZFtVRG_bJp7PRYIvnmCmqbNN4wz4MkFcfMpihXocpS_T5SNldyYo_Y90n3kxQTQ_9KFQ-7rv-RuSEIuD4e8BazBJSvxxT_rbw1Q397vvR79-QxQHC-o8vPYTruu3CxbplL0duDOvnFJ-gTPbWHGfe_aOmTUwRBVzwxHWxt28Yj6yjTZVsUY5CFtDNCDKGQG5FM9AiC8u150-aeBGKnX3zDVlixSKGbRkYHHiLLZ159r8DP-CAjL8FMFqwSytUa9l0ct_L-bl78zonoO3x1-_Ax5ZyojXV91tIXSPrW5xXmaXky8YzpYTc9PlvijSTtKu8sO2vE1CSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيقات اضافية من الاردن</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/82174" target="_blank">📅 14:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82173">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/235cd514d2.mp4?token=nk-uJY3TdSMgxV9hPdWzLYoySPx6Fnytp-hCP_UFz3qF-VsjRlSnPKk3_7bgsFvp2my3CLerJqxaC6ZNgJ7vBSIfjK015r4evGFJgpAmr0CwIyHMYDuPUJN_GDp-0MvU9lNihx4OhTK6U6fnHmQTbltANUH0Mg_TTnGQiFafiMxq7i1GdcUYEGu1imQtVMjqmvKG-3wlXtp57w4qTOtQMgOgPIw61yzgDeg0-7ACeH3LrhGtUISA3ZtawhTVP4Fd4qX1m7p3i0SOjUYhIDxZnEtU2WQCgNG_aFk06bqP0G2yaRVC1-g55WnuDCcqVmHipjFCCPspy7C2szX7dxFaXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/235cd514d2.mp4?token=nk-uJY3TdSMgxV9hPdWzLYoySPx6Fnytp-hCP_UFz3qF-VsjRlSnPKk3_7bgsFvp2my3CLerJqxaC6ZNgJ7vBSIfjK015r4evGFJgpAmr0CwIyHMYDuPUJN_GDp-0MvU9lNihx4OhTK6U6fnHmQTbltANUH0Mg_TTnGQiFafiMxq7i1GdcUYEGu1imQtVMjqmvKG-3wlXtp57w4qTOtQMgOgPIw61yzgDeg0-7ACeH3LrhGtUISA3ZtawhTVP4Fd4qX1m7p3i0SOjUYhIDxZnEtU2WQCgNG_aFk06bqP0G2yaRVC1-g55WnuDCcqVmHipjFCCPspy7C2szX7dxFaXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيقات اضافية من الاردن بعد الهجوم الصاروخي الايراني على القواعد الامريكية</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/82173" target="_blank">📅 14:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82172">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">الأردن تزعم التصدي للصواريخ الايرانية</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/82172" target="_blank">📅 14:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82171">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzTiswhoLDMJnHqpqulrBH1ipjRvz3pYbeFiWsODUIl6PeT2xlF4xMjElYeeQkm3pBG6ZJBGzzfo8lSagMZCrVKYRguUXp1DrM7lopZaKQ0IRolmLFSveA5G3gGFiJrQBHJ8Aqc03zJ4H6ODV9iT6OyYiu3DR07aox2aDYRNhPOdD3WAHbTwZ8M5WcpZ_Mx77cGNYDAgyDrXTZjZxP2NnDZfKK8P943AE-xU9MQwhL3HAAGlp3GgVOYp2F7SSt_WJ2JXnffh9R0V7W5FLTbpz7R8_RDBW6YznzKGWOzsmR5Hb4cA5djyeMs0Sol28wxCi-oaOv8aYXRxMd584SZDBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة قادمة من إثيوبيا تفشل في الهبوط في مطار بن غريون بسبب القصف الإيراني للأردن.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/82171" target="_blank">📅 14:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82170">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">طائرة قادمة من إثيوبيا تفشل في الهبوط في مطار بن غريون بسبب القصف الإيراني للأردن.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/82170" target="_blank">📅 14:40 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
