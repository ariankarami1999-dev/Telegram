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
<img src="https://cdn4.telesco.pe/file/EU5c2yAGjUBlWox8KcvH719BvL-vjFYZQNAhIakn7AAq5HIIESIQ14X3JtrDHabn5MUrZmFP2Ih4jn_OnIUWroAlIA944hM19StBUUC16xcCq83NS9uz3_WV7XJyu-h6_4-I_OSZe1kr0f1H807Rfvo0kyDYGkK_RGEjYDBX14Jj2BM2P1x2dL67EIvzeTQGkeQ-_8ecNBSsISO0HWR3fWAygNbUzppnlKHMqwgKUqihvNsxLUrTeVJwMSyt-mecCY-BsVXdRO9BILqPmEfiGeTvbJSoq5LI_EACeEbdwrCESit2_AUK8B7k05npJKTkPvigpGnytCF7AWsyBdbpGw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 323K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 17:53:23</div>
<hr>

<div class="tg-post" id="msg-24470">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rzddh3S9A0gKM9d_5xrvTtgPkOhFIhW0NqkuqckpUDx5oA3yCSEPa-O4xU-uM_jJDZvFKjX00pQ_PF5cq5JhA-nTaqazCLPuAqieV8RWPdavUYsyi2lL5MwL_tax_OjEJlTerGEQwYbrvgcioCHRpu4IRmL3T9VtDMpGoO01PpIVXxPED7GtD2VgLv3XtS81mt3OiawRZsUdSGbmnGIznNujeQqQAjECF0vI--9qu-K9DkLlPgXdlBM3MLmceT5HZAty5g31G2v6EIDrA_f6VcG9XulXlYg4QxPVe2KPE_neHp9TgoqHKotV28JudU-kvRjzoxHLUBTSEljC0lUtTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇺🇸
فدراسیون فوتبال آمریکا در اقدامی جدید به فیفا نامه زده و گفته‌آماده‌ایم که رقابت های جام جهانی 2038 رو به تنهایی در آمریکا برگزار کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/persiana_Soccer/24470" target="_blank">📅 17:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24469">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTJPecoUXtUKZFl5nT0gP0Hr5Yi3GNSfXuOIM_onkA3mrYjGZxghDJTNt2jJNRG45QYlNATnVTQ_4o7OVhW5BAe8zvjWUW_OnWBd8JP2udf1VV73CLF_aL9jJPQSqCgpyo2NtRtUDjIwAkEZ7PohhGEwsfXhPYm0AHuKMVXzFkvcXA7rOtL5fEFCM0J1QFSdRXGE0aROjDe9vo35J7yeaxIHKRjKuZI7La8moL3LkONYXSxvWTRPGcCKZWAndSX17g6R0IMCRavVS_0VL9SgMSZNkpRPkIGUv4-QMlXudaMWkj1OdmY7ApgUIRVMPhpOFWfI7UXvUH6UCzwwYHA-tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ گابریل پین دستیار فصل گذشته تیم سپاهان از طریق‌نماینده‌رسمی‌اش آمادگی خود را برای عقدقرارداد بااستقلال و اضافه شدن به کادرفنی سهراب‌بختیاری‌زاده اعلام کرده و علی تاجرنیا منتظر پاسخ نهایی سرمربی‌آبی‌ها دراین‌باره است. این مربی ایتالیا از سپاهان…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/24469" target="_blank">📅 17:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24468">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kbnnzt24GrTjoQjNMmcP-AAzOvgGfvU4zUeRcBsKlNdm7BrxToj5kfV7REotrF_W3_Nysd2TtqYDg9fOyTTeOTkPLBe6udTfsxDVtF9vpoI-n8m4p5j-UKJd-ZGTgR9IpD1WTrCUxxBXtxmU4vx3Lsu2VwRgSDJaHREkWkSZfvpj3czoLTm15aIe4xWOrPvEW8aDcIHB7GmFrRjrG2kOHbokg-x53NC6S5xhpz9UNV1dxvtn0aD0xtgocQLCsw8IaX2oI8BBXEwrd13tNLmnAmK5-jQRPIiLV4eWzDwAsqGA4y9Eu5fXYBOyAHkwoJAJKxPuNoyeUreSTtT5RvBjCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دخترخانوم پاکو خمز مربی سابق تراکتور در کنار خواهرش؛ بعداز اینکه نادیا گفته بود دوست داره به خاطر رونالدو پرتغال قهرمان جام جهانی بشه رسانه‌های‌اسپانیایی بهش حمله کرده‌بودن‌که‌گفته‌‌من‌‌فقط نظر شخصی خودم رو گفتم و حتی اگ در فینال پرتغال مقابل اسپانیا…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/24468" target="_blank">📅 16:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24467">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsGMifHXJV_0ZrtRNJ3rbkAmZr-ngSeE1zOuxU6vfNOkW-cV1L8hzjqf5rPBGwb1I1Kg4B_JjC1qoms47XPbNjhWsN2qYaPIKJvO0ClmpinhSWxlDlZtNz7zzmzWxG8wotI2kwcdNvJkO1zbOhw1nqu_hNkPbUbQrqRS2Cp7z4p8H8Nq6Uai96T_W1yqhmP-T3viTkFWQRQ6xVcEXoOv_Xlv0CSLw6h3UE3ZFDJWOG1nAEjUQo2EQmEvi4q2LgJxrFHEU6F8hujtwSfa7OYXmYpxjN5kS-c_pdH1EHVqGe0Q5jr0rlLZW73GClosOgXoEeyvSphlMbF4e0H4l_Qfvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ پرز از اشتباهش درباره مارتین اودگارد درست کرد؛ باشگاه رئال مادرید برای انتقال پاز به کومو 60میلیون‌یوروگرفته و یه بندهم تو قرار دادش‌گذاشته که هر وقت نیاز شد با پرداخت مبلغی ناچیز این ستاره آرژانتینی رو به برنابیو برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/24467" target="_blank">📅 16:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24466">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7vx4BE_YWhYp-qqyioLFeqUj8GgJCHUy_YzzeyIdlxCl3ZsQEV7kMmCvlU-K-XEcszK6uiWeAdEVQ50SZFZ8Op7L-NZmOp2pOQvYSFd7RytCABrnmpJjHXskgXj6NTlcxeU6Up9moMsLme2tJDn2qJ23L7-x6dImAl-cTR-H69wGspkiwrS43T9L20EYvogwCTN2j9Rb1ylInsvN22EN4j5YvVAg3imdOZqqbbWHTtCeI0rkQXniQUme5F5P2z-hmpT7NbAnIzwOMIlN8yIxcZAiQCIWCKEeM_uwRQM6lD3baFHYAqer08ZEvFO0C-fgchhbIzUUWh0RJ_AS8HA1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جان سینا اسطوره کشتی کج جهان:
ظرف روز های آینده برای امضای یک قرارداد اسپانسرینگ مهم با همسرم به ایران و شهر زیبای شیراز سفر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/24466" target="_blank">📅 16:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24465">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKk7FD0gwumuwarwtXGYgoh-OyNcOKDM8CVOzSJDGtIqzSnznYLTVgNrbfAIcapfBSHqiQi35ojy1ZiSEy3IgwF-WMJdBaLtdHlw1IMysazewyfqibwOY0UGK8jsh8kXKmZmkwBVn-6cEUSTlByqtDtNcedPmkO_OmIfWq5d74jH6QQzmkI2cvT2lBl9e2hkfU-3ung5oIWuKbfccGnVQSC-ngi6ASblBZXwT1t76rEi3P92hjPv-uCR4GJvSqDjrwSvo2fRfnPCeNdsdWBVn0GuMgVwhu0FEmhCb6Jp_E7YkcYu2YUhghYtck3G20Nvqai5d8AbULWV3tB-UOfB2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌ برای‌دراگان‌اسکوچیچ بلیط گرفته و این‌سرمربی این‌هفته رسما وارد تهران میشه. قرارداد اسکوچیچ با تیم پرسپولیس دو ساله است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/24465" target="_blank">📅 15:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24464">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZhQR8zLAb06zPZjceI6rn8cGlFMcY-LZLJPltvns64eMiLa6cZOySGqzhnpcVOIazMSexACUAzWV2ZWdoKqMkxxXVWUlFUUNH3v1fy-nlZqZUYPd9wN9rnhlyuz32sKPJtRo13ZUnEeg0NIQ2NSLoY3jhCR4qHuATqxjJo0icH_YoBgpsXv4OZ_Wly7TAtdsy5EPTEdGa3Yl3FKxCBxrR7bA5c8T8khcIH0-lkkYDabrZfvLsOC5AauDWRmA8fzDziE2J9WLx7tTcr36JaV--P-JdYrbGYpdEV5szLCCBz1Iv3iK8caxnb_0o3pJiob2KIkx13_0UQ17YecLuxRDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی استاد خرابکارب در بازی‌ های بزرگ
: خراب کردن موقعیت مقابل پرتغال در جام جهانی 2018، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت های 2019 و تضعیف‌تیم‌مقابل ژاپن، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت‌های 2019 و تضعیف ایران مقابل ژاپن، خراب‌کردن موقعیت مقابل آمریکا درجام‌جهانی 2022 و عدم‌صعود ایران به دور بعد، گرفتن کارت‌قرمزجلوی‌تیم سوریه و خراب کردن موقعیت ها مقابل قطر در جام ملت های 2023، قرار گرفتن باسن مبارک مهدی طارمی در خط آفساید و مردود شدن گلش مقابل بلژیک در جام جهانی 2026، خراب کردن پنالتی مقابل مصر در جام جهانی 2026 و کشاندن ایران به اما و اگر برای صعود به دور بعد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/24464" target="_blank">📅 15:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24463">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNTX46FQeGlwsJtCe-1cxbVYYqrDvHmc3yjZe87upnD-_IKDz2SGhP4QucuhxOlBXklAEk3EqxDX-2svTlJU0cOmMK1zhRKBCaPb4JgkbNWH-OmVGRPYbXuUinbCayZeUCnK8bVC_K4nLepn7LvTenlOkfkDAXYwjCv7N7CeMRbYU5lJDcBv2I7xqio9q-a0IF6xfgithKiklkPQxbFGBYU8SSp-sySonC4RZfdrOaRTrsZR8Jhh599zcnVjb-YfpkmUONpFHgK803u3B85Ll7zbjHdfpsgPqYEkrytbaRoduYclDvCpHhxA25BSdxH9F2zEjG_I2020TpQK40pc4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/24463" target="_blank">📅 15:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24462">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30dc88d38c.mp4?token=HNjWfMpwIuYeRpHM7VcT-ZAQc8flttrJ_SAF71c6TsTSvTmzMgeXp4fpk8mvN_WmHB6OX0BTHQbqsvnM4_ZKrnI2UVQOLkNM2DUpKhfRsLtkVnqTX-b2zGpgUIxTF85rGiy7QHeWO0zABNQ0pCJg7OL_kK-lWBxI2WkHVdcj9nhFbrbl1gBiOkEplqM1kzzbDv4V7Q-Inwoo4JXM1SzUSuojKeU6J7dqNkF84rI5oLEYRdzjWBNyD7XeZSB7X9NBxsjyS8_iPJ5Ob0qzA-Oa1Gni9EBV_BojHELVEBxGCmMVweJ9riaq2yUWEGXvHmh4zoS-8ssh_Acx-k1doy4njQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30dc88d38c.mp4?token=HNjWfMpwIuYeRpHM7VcT-ZAQc8flttrJ_SAF71c6TsTSvTmzMgeXp4fpk8mvN_WmHB6OX0BTHQbqsvnM4_ZKrnI2UVQOLkNM2DUpKhfRsLtkVnqTX-b2zGpgUIxTF85rGiy7QHeWO0zABNQ0pCJg7OL_kK-lWBxI2WkHVdcj9nhFbrbl1gBiOkEplqM1kzzbDv4V7Q-Inwoo4JXM1SzUSuojKeU6J7dqNkF84rI5oLEYRdzjWBNyD7XeZSB7X9NBxsjyS8_iPJ5Ob0qzA-Oa1Gni9EBV_BojHELVEBxGCmMVweJ9riaq2yUWEGXvHmh4zoS-8ssh_Acx-k1doy4njQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برای‌صعود شاگردان امیرقلعه‌نویی به مرحله بعد باید یکی از این‌اتفاقات رقم بخوره: الجزایر - اتریش: مسابقه برنده داشته‌باشه؛ کنگو - ازبکستان: تساوی یا برد ازبکستان؛ کرواسی - غنا: پیروزی غنا؛ طبق گفته رسانه‌های خارجی ایران85درصدشانس‌صعود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/24462" target="_blank">📅 15:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24461">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384d776b9f.mp4?token=nrW_ObZrjwX29wPAKyIvWFm9nYNon0YmlRCSxPFqfkgD_8MyBlgQC9uE2CehG4hTHwgaphc-AJZYXzIHLPVprJhRHCN-kHusOryq_ug5iyXzih1DeSjp5DoBi7XBxrmrJDwB3RMhkf73Aj77rSpL6GeEDIKKy-0aL327zDNvxAVR1Nrjc1OUYFaStZBor0IKh9D96lRAJrbT21LAL-ziXom5r6-YKhZAkhwsmzoVE5ms9WwtYMIM-LuaxxedCXMaeishxN8WTm29fGaCV2Lbwl1q8LSJtIS6Ecu9z6-weW9ORxsboJyXOu27-XyNLToOZX_U6oWyn-xIhuJn7d3ON1qRLrxXPhWAbou1lxS0xWWOPM75ugPeSD0mxhm2X1SynemyYcZycjp2OCkpreaMW3xYgZbk61-o30P4P9FO6mZOiH94CauFhDy_1HMxS3VZFPaxSdvRGV14J2oEap1DQJFO1WqqxS8yoBEeIB6eTso4WXqzSbeSUFQk-ooDnIL-3l3E7jU-5NmqiZGhVu-3Yja1i1bciXwWs0MH1IKJEO8lpl7T_IWoi9wYx-kWOtft5tbgjJESnDj0ZB611CYKtTSevZ7DxUOS22_PzsYB2egfjgXpDHD5s89LTjrZkaQkDQQH8v_2HAahLi0yd7eRmKGW0HTSsv7CQUuA5h37MNM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384d776b9f.mp4?token=nrW_ObZrjwX29wPAKyIvWFm9nYNon0YmlRCSxPFqfkgD_8MyBlgQC9uE2CehG4hTHwgaphc-AJZYXzIHLPVprJhRHCN-kHusOryq_ug5iyXzih1DeSjp5DoBi7XBxrmrJDwB3RMhkf73Aj77rSpL6GeEDIKKy-0aL327zDNvxAVR1Nrjc1OUYFaStZBor0IKh9D96lRAJrbT21LAL-ziXom5r6-YKhZAkhwsmzoVE5ms9WwtYMIM-LuaxxedCXMaeishxN8WTm29fGaCV2Lbwl1q8LSJtIS6Ecu9z6-weW9ORxsboJyXOu27-XyNLToOZX_U6oWyn-xIhuJn7d3ON1qRLrxXPhWAbou1lxS0xWWOPM75ugPeSD0mxhm2X1SynemyYcZycjp2OCkpreaMW3xYgZbk61-o30P4P9FO6mZOiH94CauFhDy_1HMxS3VZFPaxSdvRGV14J2oEap1DQJFO1WqqxS8yoBEeIB6eTso4WXqzSbeSUFQk-ooDnIL-3l3E7jU-5NmqiZGhVu-3Yja1i1bciXwWs0MH1IKJEO8lpl7T_IWoi9wYx-kWOtft5tbgjJESnDj0ZB611CYKtTSevZ7DxUOS22_PzsYB2egfjgXpDHD5s89LTjrZkaQkDQQH8v_2HAahLi0yd7eRmKGW0HTSsv7CQUuA5h37MNM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای دم صبی جواد خیابانی و پژمان راهبر از این صحبت های امیر قلعه نویی شروع شد که گفته خدا باماقهره. جوادخیابانی هم گفت این حرف قلعه نویی چرت و پرت بوده یعنی چه خدا با ما قهره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/24461" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24460">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346c907015.mp4?token=SA_4aGWbqzwwj7U3F2eqFoS5D1MhckgpYYu88AGGCTWSa3Wr6ysD2IVpo3JJfYS9MrFQxTuVRkEgvX5sDQRiLI-oGdLsP-8sgUPpu9z40V6Q64-_sPZS-UWGEfXBY6eMAfypE68wZc9bj2-XoZrL5t5nssW81XUF_8qhsjyMv999IJe5WY91_GChzIKv9sJrD0tR-C7DxbYxdMVgLfaAHk-P5NnhYsz3Wa5bSf61RBSVwAZNlEhRpW2fffG8hkrEIJZ8oLo3oAVThSYhRtr64eibsZJN93fpKwTs4D4Z8DKKEdiwrydOZ1kmQiC33lGF5ifFHnAkFCxJSvs3BzjnyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346c907015.mp4?token=SA_4aGWbqzwwj7U3F2eqFoS5D1MhckgpYYu88AGGCTWSa3Wr6ysD2IVpo3JJfYS9MrFQxTuVRkEgvX5sDQRiLI-oGdLsP-8sgUPpu9z40V6Q64-_sPZS-UWGEfXBY6eMAfypE68wZc9bj2-XoZrL5t5nssW81XUF_8qhsjyMv999IJe5WY91_GChzIKv9sJrD0tR-C7DxbYxdMVgLfaAHk-P5NnhYsz3Wa5bSf61RBSVwAZNlEhRpW2fffG8hkrEIJZ8oLo3oAVThSYhRtr64eibsZJN93fpKwTs4D4Z8DKKEdiwrydOZ1kmQiC33lGF5ifFHnAkFCxJSvs3BzjnyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
مسعود اوزیل هافبک‌ترک‌تبارسابق‌آلمان‌که فراتر از یک هافبک بود، مسعود درتیم‌های وردربرمن، رئال مادريد، آرسنال‌بازی‌کرد‌. اون درقهرمانی آلمان درجام جهانی 2014 هم حضور داشت، اوزیل در خاطراتش میگه وقتی که آلمان میبرد آلمانی بودم ولی وقتی‌که آلمان میباخت یک ترک مهاجر بودم، بهمین دلیل سال 2019 از تیم ملی آلمان خداحافظی کرد و در سال 2023 هم برای همیشه از فوتبال کناری گیری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/24460" target="_blank">📅 14:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24459">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVr-5_FidoL4XTdfSURIEHAXtTbSbYGj8vYv6t_GoZp_7gMwTQJXVYiPSxEZcbrq-jbhENGZIy5hf8G20fG0gPC2KcwcVDcdMMErpgeBkLvAZkIFJMRZCaC8noID7lGl4F2Bplws1M2Suq4w-WpBbrLKKQ2k2eePiAEsB4KrYIdSkMJp7mgDIk5t6WHg-3VM5yH3-0ekTfmH9o_W081bKKjVoaJR2yb6bf_hRgUnkOm8V2PpEEoSQsDoXtf0p4VvBaKEh--QUJ7Gf4jkpWB0_3GEOr6eADylQDzJaUFAYLkq7mrFFAoJOnPf7OXkl5Fp6o1p6Pr_A4G6lHqnf2833g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/24459" target="_blank">📅 14:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24458">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l41HJhKF6LnPSmcNwFJ0-rOUKYZeABfHDFoJU0PB_j7rtVEV3v0LOsO4i8QKgXh7w1UEf7iMsh0dkvRU-xxkT8roY7kNQTMtRCOji51F6qpPXjz8b2-5cjI4Q3whTGaaGnRIc0uq15nzmwTj4Feh64ALoDvwIjNMngYBL46X68FhbhanNC7A__jMMxwlFOPJJTzMaphNBv2MzTWOM1MreHMSk5j7vWLBWUfv5qAmq2j07rho0EsH29QIRpXCn3f_QvTaPSjFeiWenM9sc6v8yynv1FxrcYzzXMqUZwPhF3WUipJEx9q6hTVY1Q-1lh0yKi5Gm_pDs9iRCyQrVqZy_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برونا مندونسا مدل ترنس اعلام‌کرده که تقریباً دو سال رابطه پنهانی با یک بازیکن سابق تیم ملی برزیل داشته و اون‌هم برای رازداری 100 هزار دلار دریافت کرده که البته گفته بدلیل علاقه‌مم بوده این رازداری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/24458" target="_blank">📅 14:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24457">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/143e37e8ab.mp4?token=OA57Uhpisx01uSO72TmgsneCyVYAk-qWiXtXkBNvmlAQKyO6nbAdrJgEnOCuhgvalmIW_bNPT6AAh9vIFmsFOpFYrVMpGRMriJBpVx2FRMQ8U8MLNTDf5BG6YNbALDAUbZEPNlOBWeB5JPWOpCPqE6FeN7K3-RUFDe8VcqIhP5C_f3hunCsxTbtlOeQ3ksxSCAYeFQ_4qqhl4PUygjr_hpyUAoYl7-jZeSYu9MZYn1d2QdD8nTdHnVYEOG-A-1FskzZlhAE5CXONEmsXb_PydVEWJPdzD4pVpEJGVX3xlXEBnTqw98iL33B1O5WYbwvxX8nfY5RRp3vnTz9feggOJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/143e37e8ab.mp4?token=OA57Uhpisx01uSO72TmgsneCyVYAk-qWiXtXkBNvmlAQKyO6nbAdrJgEnOCuhgvalmIW_bNPT6AAh9vIFmsFOpFYrVMpGRMriJBpVx2FRMQ8U8MLNTDf5BG6YNbALDAUbZEPNlOBWeB5JPWOpCPqE6FeN7K3-RUFDe8VcqIhP5C_f3hunCsxTbtlOeQ3ksxSCAYeFQ_4qqhl4PUygjr_hpyUAoYl7-jZeSYu9MZYn1d2QdD8nTdHnVYEOG-A-1FskzZlhAE5CXONEmsXb_PydVEWJPdzD4pVpEJGVX3xlXEBnTqw98iL33B1O5WYbwvxX8nfY5RRp3vnTz9feggOJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/24457" target="_blank">📅 13:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24456">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVsEgcskMcZjVj4q8HerJRkiras4qcDmPj9NS5Wuxl4XtF1ntM7LskFvl7VzCoGnLm9OyPyl85igB6qjwfWfgxnSOCdIDz9d1wK7NDMVi5zZdGDq-B99lTGA3UXcBadsSbjnyMEm1xqudoLOV9UvSE4NxyNp02ZGWPqHYQ3lny7UmvWcFpSPGYZ6DlCkxK7cpY9tKbPQ-3IkJ9Z482kenuXrfK1XMRlDsM-q2ZdDij0asSKIy51v-cGtg4P7Ihf5oZnieZzKAKmWDhNbwCOSGiBZt5_Xd2xP8ouToYQwM86PSpAKJ2B31mi8VeLIiPFfcuTQw6WfaWe0W01fmzGPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/24456" target="_blank">📅 13:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24455">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUtu09Gcvr-XXvECxIY5S-qu9iT-cCQwvpzNAmeLaCyn1y5FsZJ5WXIM_EyX92xNh74cInSG8U4MhP41miiCvC54OnXLKbNim1mlJxX-Hdb97qqqmperGF7lPgZv3p5QYWhDJj7nQwUzNotz8DYdM815KAW3mAWZaq75rgu-uYgr90r8cy4Vq31XLb9uzr8JC9Hbvkv_EVJxR-Y2Ocyv3IWvSAS5k_zOjNSz1E70T5VBv9ipDmnbfe-SMixOF2TEp1JFt7JzYn8_cOGMBRthARYfSph3NNNWp4rvJcT7p9KwhQq-cVdi_RrM8sYzkDZKIf2Dff_u9m6_uYEAGMNH_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/24455" target="_blank">📅 13:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24454">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qR9mMzi5qSaLMF9PdUiTmG2xTlr02eF5B7kbAd7v_XtQQDGFCtYlRd2EPz_KKSj9cC2oZZth7PnxvbVpQmq6hE5I9bifZCDPEQIbhuAxvgC5OKsVAaDQS-pPmuwjPZux_rc8NR1sxMwvLVzxteuKtCUlfLrRnRuef-l4xOM0ScSoWRx9Xvfb7P3WXjX0Eu3baH4x7nJYF_-OzogmCbCbgZ47oPmOlAJqNIOvIJ0bHaCNKBmBMudIL-LDLWALk0TjHoG4wakxxw_Ehf27x962ImXTqpmzPnZFZ-lL2kKHvnebMOOaNgElLVmRChhoDLU2e36msKycDuoLkugad64REg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/24454" target="_blank">📅 12:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24453">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_GciaDBWBF8yKnGLqJ0LEDxlHCMu228rqShXe6QDcvos5CIXZEzHnIPhaVdoxk5v3DywkYpEqPXZGq_2QXWHSzBsZWdjL6u0v2Ie4EcGH1gJGOl2vYWQ0OspvGEPJvOUdt5MMLToQPGl5FGB5U3Yq0otx2sA_3cdZu95h6tRk4E7jhAJEJ3s3PRcVI8xdNDayBQwhV6Yjcbmp-Ad6bR45kpCN1t1gOd5zYh3cdwKUETqQ83t85dR1KyEgR9-uJEfwjA36u1IWMtr-sBn5TVIaqUmy1GJONHQVBf1-_sY_MJ3ViuV38_-UfILweKAiFg5psaDdvskhB-dJGXbPVfLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ ابوالفضل رزاق‌پور مدافع چپ 27 ساله فولاد خوزستان درآستانه‌جدایی از این تیم قرار گرفته است. همانطور که پیش‌تر نیز خبر دادیم رزاق پور مدنظر باشگاه پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24453" target="_blank">📅 12:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24452">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvd_VYhXptc6rOMRBFaERu_fG2iTvM7R1mFSGNDrt1ttj7yGai7mPoS62P6k2qz1swxBUPTkiCVvoSiUeE7nZe1StlK_b-JMJH0aNbLhcLm0PnDJQZDiVEYl2ToR5BZSw6dQUd9p275fTlT6w8snfz1E9a4008s0Y9j8dI9C87xdrRZRg9oboTgn5XJx8seVjFvEeqlMH93Ugsk5TeRjzf8qyq46fvWvXVA7fLXDTkXjczz9rC54maXVc0r_AVWQzmzbGR__ThNa01EDBibsHZb79H_LpQBZCLzxqqj3RP0XMqJPWyT_GVFyRU5ZpWg0-Vi7Hatr_cQYoI8hXNr8_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عذرخواهی رامین‌رضاییان ستاره استقلال از مردم ایران بعدازتوقف‌مقابل مصر: شرمندتون شدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24452" target="_blank">📅 12:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24450">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V12f2BdpS4D4FkCGuYkAIfXHRJC9WUdjZKHfM1OjuenfhIFNf72freQns5J31A53MrKpTLr8ZIMH8aUEsy6nqH8uBLLNsOPAVOPPpOuCGrRYuP2ik9622Xv6rrOMH2Ei4c2KwKAEjpCIWHN6WWVub7zAPGmChcUQZ3XzUFvTDENKFcyrPlM1BIEIxrnRXc0mbrDuhTnDIqYpCrxIJl19tKVATRLzNyxsjO1ZLsfdw5yoYGflEAeMqmuzSTayNpJZKfPfoWBFtoZS6V_jkld-x8nbRXOm_t4wKaRNZSJeiw9_bv8pgtTb8NFLSeqbT9DTepXb1s2pB-s5HeMMcrGlEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/thm8BtiyZ1Ud2gxucbnx8coPNxl9DLJlv_zKnLd7KWu-F8k0UWH1ngBm5uVf3wdWg2_eB1EEs7aAjZz7mJ8QzxDwQLFX4rpw6UrpDptLAAedmeuJdefVenTYEa1XtFze-OIUR12Ax__vM1FmclB0vd8v7DU7KlVWhYcC-T9_AJ86nWg2kXzlQRhUqRukh9HNjr9MVSTbSSye04VRnl9tMyOFGXKgrzca2kUI6fgv_GT6X3C2kRJFzKfXjN76uU2DCKgkurQ20WAdrGHES03rMNbpNWIbu-HhnYmaOevWKmiMMu7aQLyxKlyslr8VhGcenckFefHpwXmYJL351pg4gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
پارتنر برخی‌ازبازیکنان‌تیم‌ملی‌برزیل؛ جالبه بدونید کارولین لیما با نیمار جورنیور و ادر میلیتائو هم بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24450" target="_blank">📅 11:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24449">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B41mGB3Kc_RcDu0b0y8ujwIPdm-uIperSWRGY6pWXc7eY7nWQZTvVMfKibLCg6hxJEhwN_AUT4CsQkOBbtccnxeMdYStcn1xs1fr9Ux1A8BVD0hY-Meaa0e6RgChhc342I8uEVEuL1_leirTUINCL6RMdEAmD6AHGwLQ9HiQcEWEOc8C3woT65tMYGuvKBkiwOiREdIrTvQgsxpONY0a687E-kSfSHEDyVwqgS64S1IA3J9t1uinBFg6pRTNKXUKk4eCpr2sihO_OTx79rX_3q4fk73VHBUYTnOLJhjWTk3rsafbPLCTVeFHsRKgQI6coZoAdD-TI_q9WP90mLljxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی رسانه پرشیانا؛ با اعلام پیمان حدادی مدیرعامل باشگاه پرسپولیس اوسمار ویرا رسما از جمع سرخپوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24449" target="_blank">📅 11:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24448">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_7qJs34fbW6NKx0cWUgp2UORriwOVYIyouHx4WGtBhKheGlCGDTvH6zyHZfz1wjPr2azLYxz1qYnuJQA_b_FhPulC6fzDPWVumXrXClHdx9_6iSw3Xd9Iz5OBrEobluWqwkcaxTKsDqfFOTjfkbTFtTyPzJYM2oQrT2EelwiIz4YZ502Vd0RewJzCr2jckbXPu0IhBlnCRt2kxxwar3hEW9Pe9kVOF2ur-Mosg0UtZBIMM4XCQg2mZkqJSdK27ieVPzFFTmx1g6IukVLUa_yUwlAjLzy6mOvEaEml2kGSCakGHEVBXjzrxCN0U6Y0TvNAoBxmguJm9lk8Hdd0ioAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
#تکمیلی؛یوسف مزرعه ستاره‌جوان فولاد به مدیران این تیم اعلام‌کرده که از استقلال آفر رسمی دریافت‌کرده و نمیخواد این‌فرصت‌رو از دست بده و ازباشگاه‌خواسته با فروش او به آبی‌ها موافقت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24448" target="_blank">📅 10:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24447">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=cv2HX_c5InvZWydbzRGX5h2l5Q9BnQYb8-vnhAkrF_yCHLGPUzNKBGt2wnZr9c45HkaPD3X_EaxPEoS79Oaob-FhBWR7gOBVwP8MkZTPvfW7hOBiZHgmL7PxoWX6Axvdbd3qH_chncRp5iZgj-2XjgGxTBFEF9uZvoi3lGaeQl7q5spoPfPaYIf8WQolV3VLJcI40A0OvnfSDnrxVQMZFotqzakt4ayeiUW4QcDMricYGZLRo4b7WHPwI4DY_rCihy7aiSZMHmtgld015adYKm747JxJZ5zWgifVvtKLgfKRlMemKnQIoAI-Hld2oGckxczEBr9RU2GtRyA-Z4vlWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=cv2HX_c5InvZWydbzRGX5h2l5Q9BnQYb8-vnhAkrF_yCHLGPUzNKBGt2wnZr9c45HkaPD3X_EaxPEoS79Oaob-FhBWR7gOBVwP8MkZTPvfW7hOBiZHgmL7PxoWX6Axvdbd3qH_chncRp5iZgj-2XjgGxTBFEF9uZvoi3lGaeQl7q5spoPfPaYIf8WQolV3VLJcI40A0OvnfSDnrxVQMZFotqzakt4ayeiUW4QcDMricYGZLRo4b7WHPwI4DY_rCihy7aiSZMHmtgld015adYKm747JxJZ5zWgifVvtKLgfKRlMemKnQIoAI-Hld2oGckxczEBr9RU2GtRyA-Z4vlWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای جوادخیابانی‌ و پژمان‌راهبر در ویژه برنامه زنده جام جهانی؛ حالا شماها دعواتون رو بکنید ما که میدونیم همش فیلمه که برنامتون بیشتر دیده بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24447" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24446">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=HY40YNjB-BviLW2NlBaNBQLcUpXyEbFujxNjQpq5JpozwrdoCLCuSbBhmXIgGfe54-uOWV1lDPwKALWP4YyljihsIIdFLYZ_TZFRm_U6_Hj78N9ydIasGMDRHrpPNuPwmnr9CGfqMZgeJYCLOSIY4Fllp_Rcn4sy9AH0dmyLfvs9AlO0kKDwdUMmoTicDBiNoUW24hmVzzkcCp6DV6CFcmo9OgiFUOQqkBTjjDBc0o3fHUlmV2tAefbaqjMDAzKRgsFwtLrUm2G1kUMYgPeMzfbHy_KmZgzwY7CtSDELgwMVtJA1vD4LW87TnCBMtt_AST2jR5GTWgsUW9B-KqJ_9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=HY40YNjB-BviLW2NlBaNBQLcUpXyEbFujxNjQpq5JpozwrdoCLCuSbBhmXIgGfe54-uOWV1lDPwKALWP4YyljihsIIdFLYZ_TZFRm_U6_Hj78N9ydIasGMDRHrpPNuPwmnr9CGfqMZgeJYCLOSIY4Fllp_Rcn4sy9AH0dmyLfvs9AlO0kKDwdUMmoTicDBiNoUW24hmVzzkcCp6DV6CFcmo9OgiFUOQqkBTjjDBc0o3fHUlmV2tAefbaqjMDAzKRgsFwtLrUm2G1kUMYgPeMzfbHy_KmZgzwY7CtSDELgwMVtJA1vD4LW87TnCBMtt_AST2jR5GTWgsUW9B-KqJ_9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
رامین رضاییان بعنوان‌بهترین‌بازیکن دیدار امروز ایران - مصر انتخاب شد؛ رامین رضاییان نه‌تنها اولین فوتبالیست ایرانی‌ست که در دو جام جهانی گل زده، اولین سه‌گلهٔ ایران در تاریخ جام‌های جهانی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24446" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24445">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cQpxDpGbqnlgkK3Rbxj2Q9dBwnOsoE3-D5JGXFygACicpziCHJ-9N2s6AsKZfEHsOCODzhh0RVdlEO4dplF9x1BSuauqIwBueXVpsyggjdBMjubB3JTeF351mQRuz5HM50t3ZOCEFxT73z2mQZJK-nHIAdnh70FcvP19POxMBD2SgQ-p6EXpyz91VutIb28UxpjJH5feoYsmSvJmz4UlBZEByfe_S0peqfNc93oVtjRrwCd8goYG9-MJq0nYlGluTZwjPEoxG0M2cev6QpcxvG5crMvFPG9yloMrFgvYoqDrCGdQ2WpcnqRjBzdLgNBLQpKvCgnI2fSiN4FYD94bDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود بسایت فیلترشکن خود را خاموش کنید
.
🌐
Link
🔜
MelBet1.net
🌐
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24445" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24444">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcM0OBt99WRA5Uos-TiZhOkHaFZpwBP54jFkTbvfse5jfBgmPGOUm5MMwbz5YGXwK2jLkOf0ntXga5mgg74kRnsTv7UynMgSCja68aGASusY6RYpP5TYc2KryoPPj6P9WceSPYmMUeQXeQ5dft6ZWk5bi73qaM10nhotvIoKdEw7XPsv_jiL6lE6PGx-mry8bm8BR26VyI9XrjonRWArVEVj4jTjhqfe6TTTYUsoM4MDvaE72DE07DXIPQnTlXox2rf3eWucY_Ue6rGIUrUPzuVjk0Sithk05kpE5e4IB55KCb4tJ5uOLTK31EG2CLMWk2aa2pi0oQ3CFk3F-XHinQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24444" target="_blank">📅 10:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24443">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWCPrDrMzlnNd1J7RXDliW_M7dZik636rgxceQ4-6oIipsIHY_mce3g_xYAdiCpb5oN03FmXFAzGSyG_b1smCSSi-Qa42Z2AHCnbv8_kMd0k5q1UvBEpOKlgMxTJaZEdvV3sxM1GH3-huC_SqjXe74pqEs2_J6jx1rxq2zffONTZrKsxSwPOpxU8mFzMweHpa_ETUYTpQds0VCIbNh0pepE0wFRbztzQ6W53rdIHDKwiXmsxNAtLvHroG3i3jCiiCKsqFgbvpu1E8gvsuw7gWsOxdtq3hb8u9-gFvndLb_WMm3qqInps4nRpd_rtqRa4twijk-LMBB51-wbfImgwpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ همان طور که سه روز پیش خبر دادیم؛ دراگان اسکوچیج سرمربی‌فصل آینده باشگاه پرسپولیس خواهد بود و به زودی برای انجام مراسم رونمایی به تهران‌خواهدآمد. اسکوچیچ پیش قرارداد داخلی خود را با سرخپوشان پایتخت امضا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24443" target="_blank">📅 09:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24442">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=JZ5xq6in4u2PYADex6CeL81NBrJTolOg19BEZzSmd2UHajC0VPB0nAIH2UWA9B_0-E9y2e7uG1roTCSE8sbF8vtvINoYyZh0fGWwtFJ8l-xGvcacNCHiYhICfkzMQvz6JP8rWdmwfQarFdX8vkezKlibjq_3-CE_WJtkpzk1hq399yjVbIiCAJjtM09SrPSrFocVG00L_3CPxqy6G9Vl3CXv54aUEWjqchK0-9dypNhGfHQWea39I7bHzBTLUFzl9ouW0Pf6a6viviH6hrl-lJxQajTtWTvt8TyYBi5EI-76Xs5BSBLTxU2Bo7TGS2prYNa8cd-8BGv_eHn4QLHrAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=JZ5xq6in4u2PYADex6CeL81NBrJTolOg19BEZzSmd2UHajC0VPB0nAIH2UWA9B_0-E9y2e7uG1roTCSE8sbF8vtvINoYyZh0fGWwtFJ8l-xGvcacNCHiYhICfkzMQvz6JP8rWdmwfQarFdX8vkezKlibjq_3-CE_WJtkpzk1hq399yjVbIiCAJjtM09SrPSrFocVG00L_3CPxqy6G9Vl3CXv54aUEWjqchK0-9dypNhGfHQWea39I7bHzBTLUFzl9ouW0Pf6a6viviH6hrl-lJxQajTtWTvt8TyYBi5EI-76Xs5BSBLTxU2Bo7TGS2prYNa8cd-8BGv_eHn4QLHrAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
امیر رولکس‌ازحرکت‌جدیدومخصوصش رونمایی کرد؛ اینبار دیگه فکر‌کنم گفت خودم که نمیفهمم چی میگم، اینام نمیفهمن ولش‌کنم بهتره، مسخرم نمیکنن. ضمن اینکه ژنرال درسه بازی‌جام‌جهانی روی نیمکت ایران شکست‌ناپذیرماند. رکوردی تاریخی برای او!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24442" target="_blank">📅 09:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24441">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24441" target="_blank">📅 09:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24440">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdd214fefc.mp4?token=lY8rGEE9L2qi_MHPjvyj0GftcUSW2uuT7e6o2s1snz5AXrDVREyxYBK9cL-O4V-FmX7I-YNEOq1-dzFXrgAc99m6PzJJeX3QuM51Gj33L_O1ge0iTbETHrDenzd-uR5feB1h_26G2y3JRFgtTQ5d4GtB0b1FiGvTgZBPeMk8JF3sXzvS04Oqw92IDQBYTP73mJ1W_I8ylaS_YLIqqQlL_5cWXgzj9M-c3GjZic0_-okPVSk2D115K-XDe7Eb98RTMsdZCkcaYKE7E2MZ6-qYyinXm0jOKM3prIF0DrqhMwmtgEO0HB2vMTpojPaBQQKw-P79MCtLSSlQgyi2yybEFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdd214fefc.mp4?token=lY8rGEE9L2qi_MHPjvyj0GftcUSW2uuT7e6o2s1snz5AXrDVREyxYBK9cL-O4V-FmX7I-YNEOq1-dzFXrgAc99m6PzJJeX3QuM51Gj33L_O1ge0iTbETHrDenzd-uR5feB1h_26G2y3JRFgtTQ5d4GtB0b1FiGvTgZBPeMk8JF3sXzvS04Oqw92IDQBYTP73mJ1W_I8ylaS_YLIqqQlL_5cWXgzj9M-c3GjZic0_-okPVSk2D115K-XDe7Eb98RTMsdZCkcaYKE7E2MZ6-qYyinXm0jOKM3prIF0DrqhMwmtgEO0HB2vMTpojPaBQQKw-P79MCtLSSlQgyi2yybEFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24440" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24439">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3p_lI-E2REPNXyna3jvjtj2giB6uGGTfiD6R6V1aetrDAq8cWo078NfF4PdDUj38iXGQlDvDREatJVwA0LsoSt2Z3q01g5dXyTd2MFgOU2VBbUwg5h2qSdKbBsiIRNShHogzS2LgWoZL1C3Z6-ZJWeKaMAWPVgJzf3Xss3v987V2mpCpIaAV70PGqpmLFYtG624aKqUx7JEySF21VmPWuPStb_-lcpHTfO1DjiD8N32tvYJr8cZZf8jxb-7ux7KlVepEJou8htAyBa9es8TqAs9tLyoBFaOwLIWN9gX55yq83jbnY0l1AgOPuw9FkG1NOl4jtCjmP7lXZUtsjMcWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24439" target="_blank">📅 09:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24437">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24437" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24436">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekZ3AQtAsiogZd5bkwUyRgIhZ85XjZLylomXD3CAdSiCbdu5RXCWnxx46_t01LKlrJBbsp7WvzOfdtYNVXXJ4K_Nr-KhTrJrjywC-gjZhXCUPvZM5n2c89alTazwEC81esUQ12siJjK-ZfhrbI2rCCeV0WqlhG5LSKS7Zlfz8UOqq74G6Hqx0VFOuIbu8wA2PfxXDw4qVD3k5qsxOS6h6sdHVHwH3dYEKboklNWwRc9bcvp7dkGwr2Njn8PuqfKvoJcfV3TTvhDdogBZnsUpus6t4nKljhzHFOnZm14Tb3tzidpWlrjHm8E5TX5MrPwNSKADsf0A0RIKjJasALKyMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول برترین تیم‌های سوم جام جهانی؛ شاگردان امیر قلعه نویی در رتبه ششم قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24436" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24435">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJJH6goyXjy6R9jZ3yBDy_xo8msXxmaqdexRl7xg3rICQQnCDGiohZblZFIPeN6mYbZ10rqra9Sxrk7RobvZgKbxk4J0xJKg4SxMdy4d27tWTmjmp1Omvcsaf84Vtm5I12c0bJhq1qdlsZ611AShhk3iYIaLJ73q5TRBUfeuXrFbcRwjJntnR8FsGjIF3FynMqyaHOTj0FtDRjJfm7cLMcMONp5HwzreHUe596-YrzZMnjVpTCny1x2yYec-Rlv3bEjtbsMw8JiYrp-5UGVHMb8OXnV4x14Cs4jkWoHwiUPx8xH9LZFM0vMIeYgNvWicTXHe7hB3e7lsJXE7txuBlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته سوم جام جهانی 2026؛ مصر و بلژیک مقتدرانه راهی مرحله حذفی شدند. کار صعود ایران به مرحله بعدی به اما و اگر کشیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24435" target="_blank">📅 08:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24433">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/da3UosetIEKuiidwrW9LSzFTpDsWrx4yyznraEm8VDu69s2llJZ5tyCjR6ezSUDe93uahQZ4vGomf9RpYDB-EXu4kieUNuUg8GSkjU8Lhi_ou87HUUmA526-1Eg-1dODhLd1MWWd-IWZQxJI3neEOA66fNeafGbco2DdUltAgmaySKWHJ76YiXeEcjD1hkY5yW6Q5Kv-z2igPxzEER3wjoJaoqPbU1LCDI2qhFpRz7gQ0jTiH9Vg6ndIRFZZ5F7Ka3wmhi6WfcaJSJVo95CqBqnTsEF2f6z1fEkuASkcGvyBVeOX7b8PbGbRkcihhnOWDquLaJ3fQhzMp9UjR9YiPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DeElx7aN0rc5SloSe0hFJlGMVJuSTZmT59GoeUx6THAhJSY7BA_13RXwAi5glW5_YV-Dd-rKvf9xZGrwGcXe-LXofJkp62xtELnSl3L0VYIz2RiBbqPIluCByCwNy7EpWPp4d1DuaU9CSd1ILATJLAl5QyyfdJ7-bNlknMwKUsIMYS-e8zWO4NQVm3CPJ5tPcgu3VNxULHapNkGSeviJmbeUVul2SxB2I6NULIezzBPBZYPZU03PN8pxG4Orsw0kUcyk78q-XIn_2MzqEsjhP0DOsN-uIH24Dl2AqMA1oRjHKifvH6WiNP59ZPPVQo_oYJ0w8zvWFpaFY3pOaV2wAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24433" target="_blank">📅 08:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24429">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwTVhMiKYofUrKnlTNb98vPqlSkxNDal1bvrw7u9AUsoWDAzd83MZMIw1VVApbSLyO-o9henudaRbXHeNN0CsYbXxbIpfQMPAALpk9gsCdsQXxc--upwP1ABMB5NL4vmNg7yYmuswFIOrHzK3m03MwmmMxudNYvHLwarwDVEfCopVYhPEZrnpjavLELW8uYDVEGGzkxfefdR-HaxJwd4_qhsV5xV0XdIgqxx0EIMVia_4VaTorvTDHV5lKp44d9L4mBmMa6wgFxKT4s7b3OdPyLxfJTarEs5PR_m7R2sFioyBmyM0ssYLdpeCqRGcNnUg0SFpZMBi9b66hiBU1s_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛ از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24429" target="_blank">📅 05:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24428">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVjTH4lAS_MZm1ghiMkdw8DKjiWiJVXQ-RnAWYEZ3fn4D0O78WfFUhFHk4A-DEVua70gdD7La9hEhaRV8drZmHjN9U8FoU8zmg36dSL4ToAl6WmjrmSR-zoRFJbJxGUfwuR4SoHXiklBMDkrKOdknJDTJgProBS25jTpkgJV7vrTNH9ZuxZGO8qgyJiOX4LeWciYskw_fI3j_5pcBYENIwsNCGrUH2qnNDLj6rwG8u2WEfXyc7nSjYnvySAi_96KuUQsWh6vSWrdlRxQyjSru2ZqUUta-c3BZ0y5EhEhuYuimdy7xrQEfleFQyz7-x3LFrKdvkFx6dsF7Lo52dSlAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24428" target="_blank">📅 05:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24426">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RhfOCpzuGNdmFMOwiAD0QhoOdilXCBvap_Z5V5QF8yx5DBkyYwvNsjxvm_iD0XOARHnGufQmWDHlUn35fa_0XL8CWOVRVljh2FW0QcRjtnUiXG3ycXdMhJQjdr-J4tiRcHpFK4ghecCGGcYJaCD4AnO0bJ2AdfC93XwREHZ12XwiSvVr2bbnnNt4z-L9AJPdRGAgnlzOzbIS6o8YTLIBSvuyjys5JIp7gvMyRmCtJsXDh4TY0o1LqyeMpdB8zjTiU0rDS4qhKb3LMVwR7Em5hJxm2dhdUS9wkRjNn7izKnU6udmnj-JcwDhekkZUHlXD79BK38iJY6CekK6plGiXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A3OeGbDn4LYryA1jwZNvuvxxrBHhRnFllTBTDOf2rrac2xoB7fL76siUnegpZm0YPN9WdGYx_ow1lz0ODv4pXzKtu42fwoDh0vDIe5oq8Rk3lG0Lmzpb0xQEuNbJZ8aNIlet9jxFSb-Cg4boPWdia-i9T5CrM9J1FrKS-LThp6DRXLJ4nqo6PsCQb2_K7Ew4p3eQ6ZhJKHX_5J6C5lhxsexYxtzgz2j7hpO8DLCSrbiW5-AZBwUS-nOPO2pAn9Y3YyAELJZmPzbfRTv3DgZPcp7fJmZSmMNLCulbLONxxTC1kvKP5YpR81nEVGVR1YBRU4ZaSFhkscYEDFrOkhCA2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇪🇬
عمر مرموش ستاره‌ تیم‌ملی مصر: ایران تیم خوبی داره بازی‌ های قبلیشون رو دیدیم اما ما اینجا هستیم که قاطعانه این‌بازیو ببریم و صدرنشین راهی مرحله بعد شویم. بنظرم بازی رو سه - هیچ میبریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24426" target="_blank">📅 05:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24425">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4QZ1W0PlGgfRBdi-zjjsJbMZGxUf1D9U1YIg9coYFVgAwlDqcRZWVTd5s06BnBWiTme0tuGLPZ6ubqvCTIT0XcIslRd4ZbKVc-RDVTFuR4MRrN3XyRhi01HWnsad1zagkVxWtk5d_maNoJcc79pzmFo3vLq3_TNo-SOiz5_UcNfRPfpm6CtLjAyU5kLiOz7fe0P--9hWyc_6Iv3i0YS2zX6-aD2hkUi3AL_-qflxJL79c_alaeJNV_i1Ea9I4LiICjtdATN8xUUZ9n06TmrOZ1I9YtmFweXHtr1mqlDxy7BqxVOIKUkgdUUD0f592fuJyOjtiSjFuNS9mSHxzPOVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌‌های‌رسانه‌پرشیانا
؛ ابوالفضل جلالی از دو باشگاه اماراتی الشارجه و الوحده پیشنهاد دریافت کرده و درصورتی که مدیریت باشگاه استقلال برای تمدید قرارداد اقدام نکنند لژیونر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24425" target="_blank">📅 04:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24424">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L12aU-tU_V7AkUkwO63EYDej9TnASmHkpfAsujoflaFlO1d81nfndta-KbUUc_8cAZuuxfLMKK2sYt30krY7qj2h3h7R7zf7guskN36FnAKtLNr0styp270Ief8mkMEzi9bGoUkYxzChsAnD9Xbqeq1FKUbuuH-ldi0a6IVMWvIqwcCzmGf4bIPFky0DUj8Hj1UtQXwRMPgfVEt2puRlrmRkybWZhnUN9AeqdF8rymiIdHFsQmBhEKovLvP5V6NEEpxpdgHkZKvHK__9n5MW73hp78l_I678Po5GvumTIkIt7HFEOL2hI6so6ufbiS1PnVKsOLoVSt-M04RlFfMvZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تورنمنت‌آسیایی؛شکست‌عجیب‌سرخپوشان مقابل جوانان چادرملو؛ فرصت‌آسیایی‌شدن‌از دست رفت. از بین چادرملو و گل‌گهر یکی راهی سطح دو میشوند.
🔴
پرسپولییس
1️⃣
-
2️⃣
چادرملو اردکان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24424" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24423">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e59cd1cdf5.mp4?token=Trx1mTGP4Qf7PBZMR605Evoe-_XZmSoHVR_hRgBWdoWDOXKxR__aVazpxXWCVfhDOnzml6pv1wPo0QkFo8ARbWVy2UK0fq8UxtV7f0cBNGP-3OSxNS7KlfukcqcAbuMjMcP-_dv5kp67o4c0QpmERWQJ5NZs56HU2RT2rrc71OQ5URAxV8qziA9LsYYkF6DBPa6YWHquvKqCVH-z3q36OA9i8jDp6Kei3aFWbUEoYY5_sek7JfSCvsL-zY7uU5alB7BSR3ShLszWGCwvUPrBl8czcvlRvgHwPhI2740FCMFHxsyvA40iV_6n8kpiw2vag3OH1Y9mY03X1heTTYcLBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e59cd1cdf5.mp4?token=Trx1mTGP4Qf7PBZMR605Evoe-_XZmSoHVR_hRgBWdoWDOXKxR__aVazpxXWCVfhDOnzml6pv1wPo0QkFo8ARbWVy2UK0fq8UxtV7f0cBNGP-3OSxNS7KlfukcqcAbuMjMcP-_dv5kp67o4c0QpmERWQJ5NZs56HU2RT2rrc71OQ5URAxV8qziA9LsYYkF6DBPa6YWHquvKqCVH-z3q36OA9i8jDp6Kei3aFWbUEoYY5_sek7JfSCvsL-zY7uU5alB7BSR3ShLszWGCwvUPrBl8czcvlRvgHwPhI2740FCMFHxsyvA40iV_6n8kpiw2vag3OH1Y9mY03X1heTTYcLBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
عارف غلامی بازیکن استقلال به این شکل جواب صحبت‌های مجری‌صداوسیما رو داد: آدم صندلی دزد از مفت بر هم مفت‌بر تره. اشاره به همون شعر شایع.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24423" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24422">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8VCEIoNU5n65TsKv9znnlmvFjmoEv-xzDAEQ_W2CdwQjh1_2ienEaVI71RWK-NKq0YN9KVP6SkWjBEBkNgTHwv3Bm4_VIyZ8LiUyBpzwhSwVKwJsgn_FUHwHPoNkS1sZtQ_OPuKHX93SKpU6UE92m7ED8fc67_bE9L19LW5M1S_Ev_hiRbrTsaxFJhpdTKbqPw4-0TRYKxwl4UtvubL7xpGOTNL3MO5bWAL0OFMmEGFg82Gi7JQXqL7h70e04vykEtFXU_anG6kd5x1LggcXtCTPD1mffw7ICdOEo8YUgKI9DVp82aYlfyBc9Mnu66YSR6vP8T-Xi0kWKj5RCg_0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ایران - مصر | نبرد صعود
دو تمدن بزرگ، دو تاریخ کهن، یک میدان سرنوشت‌ساز…
این فقط یک بازی فوتبال نیست؛ جنگی برای بقا، افتخار و رسیدن به مرحله بعد است.
ایران اگر این بازی را ببرد، صعودش قطعی می‌شود؛ یعنی ۹۰ دقیقه تا یک جشن بزرگ ملی
🇮🇷
🎁
شرط رایگان ورزشی
💰
۲۶ میلیون تومان بونوس
🌍
فعالیت در ۴۹ کشور
📡
رسانه بین‌المللی
📺
پخش زنده بدون سانسور بازی داخل کانال تلگرام
📅
ششم تیر
⏰
ساعت ۶:۳۰ صبح
⚽
ایران vs مصر
صبح زود بیدار می‌شیم، چون بعضی بازی‌ها ارزش نخوابیدن دارن.
ایران برای صعود، ایران برای افتخار، ایران برای تاریخ
❤️
🇮🇷
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/24422" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24421">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELWu4IPvf72l58knE1y0C95ImT36hU_FQkcxx_qIRbIgX0kJtV9ekdQyg3-9wbLWIZoanVm3FPcdhWPnBkj2-vx6xXN4nchPQJ68SM7G4Qp33o9q5TNpnZoesYmRgmV2AdugUGnc0zuIY0cO11VYYw7df5oylf572uIHKZgpSvEr-TaTuS_VRBYvYs6DAMOLR7YkFY4K-fsMwG9WDbyYPJfrNA6kkDAIm3F-qoqvORNFkAs2qBG5SceVrgapzbhIwB1StitLpCntJWqJqKltyTp7ym_XlwEWX4ZraLmjcT7dOt-5PRi7b1caTZU4S5ULCohJc4ci-qDlT9uh0y4tzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24421" target="_blank">📅 02:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24420">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=GQ2_1Lh1_uYnL3V2Rbp9ruvneh2G9nbH-F20-MaNqAU7NF_bwVgsCxL35mKqrxPulrNXaAxonY-ba48MserwmPFFjxJEIhuq-a7FyzCgFEfJ7_Simj4HiTPW8W0GVtNjNbXXmP9pkdEN2U2ql-ZQ39aAYfo0NYPMvARC3OJYEC822faEK8pZBQGcmPBLx-IC4Lm4jL4lRZPNI7fJ5SK0rmIWVLUAn-9V2t474b1pVGFjn-edLs5mMQ6lmSCqF8l9Br9gG_IN4WIRFHnePvRbKh0ddEHjzh-G6dATSllIf6Tdh7Xz7gXbMuxOVWUZ3iBxMvBykxVR3seN8gUwWZyO1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=GQ2_1Lh1_uYnL3V2Rbp9ruvneh2G9nbH-F20-MaNqAU7NF_bwVgsCxL35mKqrxPulrNXaAxonY-ba48MserwmPFFjxJEIhuq-a7FyzCgFEfJ7_Simj4HiTPW8W0GVtNjNbXXmP9pkdEN2U2ql-ZQ39aAYfo0NYPMvARC3OJYEC822faEK8pZBQGcmPBLx-IC4Lm4jL4lRZPNI7fJ5SK0rmIWVLUAn-9V2t474b1pVGFjn-edLs5mMQ6lmSCqF8l9Br9gG_IN4WIRFHnePvRbKh0ddEHjzh-G6dATSllIf6Tdh7Xz7gXbMuxOVWUZ3iBxMvBykxVR3seN8gUwWZyO1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24420" target="_blank">📅 01:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24419">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSKFPCW2VvfFvqhZ06pia-Ehjcqr7ljQi4CU6zsAIcmhj8YXpfZHFBL4R3k12TYPONLTz-llz7Bgok6aMo6-8EyrL4IfGSaN-fbD7nIESu3_NBrziASraC3YSwWCRJ0eW4OVjNX5_-iYiRmYcWJ05V2dFQEB6mejL-J2IKSXNLiBSngyOFtB9xFJ84Ue6ixu6SSHgx665DG-Vh5mIGtwJEnqjj1kzLUQ9pE85aOzPrYuTQ6KTAc2xZT_SuHXLPvXHcc9XLfmAhNDghjp4PoEEZ8jQ_BceDUaPkJAJ8um-qqmQbJLtnAy2HBDlR4VYn86T-YK4y9eoUzyrRUCBLDoag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با برد پنج بر صفر سنگال مقابل عراق؛ حالا اگه بلژیک‌نیوزیلند رونبره‌ ایران برای‌صعود باید حتما مصر رو ببره وگرنه بعنوان تیم سومم صعود نمیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24419" target="_blank">📅 01:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24417">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXVgK7F755e7gOkNbw7rPuWpTQurE-eLAtJ_r2r4kpIFjN_ehTB3wsNp4HUeZG7caVbJdvmGf3wJJ9ycpI4QK59_d5K9EVf_7hK26Mc6YFb9ppC8nkzapBkkeSiby5PqGs36S9qdyx580Ayz9oEuZWJp4aF_QA0E5yXFrBQv700VDBK4Gmo6ZoY6Yem9PoRuwc7lfeEl7yhVUhdwzLvYL_bWILBr6h1aF91SP2Et5hl2TI5QwSmWUB3d6JJ0zur-vGnGgIIiswDZyo_zh-6_jl-uDDFi5saAz4sXaNrzW-4RqUodZEYTvQpsTjfJfjIRTj_JsL6iWfSLAyDZJ7xpaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛
از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24417" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24416">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2qSqnytQRNnEgGbVGm-hOBcFnbv5Sd0YuK5zsK5tg6e35MVraFrx7kZQNIyDXk_0zRqLvgHmUA2KsKfWpSkCVlsrguXXTv75I6TGC76orLzu4BRKtUZrcYepfKjLE5GcWoZwM42AAYufFWMo0ZLq7wSI0mf82bLkmKevD1sgBgYPNVYFFP1cYRt3sYRhMZzN866mx44hNDBHh8mMRFwm8nfT5bh4TJUJ0aDpHlGvuVwxMzYVNkspO_Ix5EcD-O97cf_7Kk85pssjAvPLjy-46DHcdf3Wehq2m9hgR1wTpHbJOBOFLMZJ7MkGfUkhGF0xaSSP_tgRVcgshnQs-Fn3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌دیروز؛
از شکست تحقیرآمیز عراق مقابل سنگال تا برد فرانسه برابر نروژ در غیاب هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24416" target="_blank">📅 01:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24415">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqcqnduprOaDkYOiiWxAx2mZcpwBwV5sk6cLeZ3WTk-1joHFbuWRTIosv6W_NocJ0NoSDXX25rcLmMfAOuxNEQag4qETBzz8ZPebHeXZ2rtwbwhSexikxxOUHq0_5ySNCK3uXDbzprECkQWymbHQ-JPLyWWgwXA_mas5IbnbkpgkyPqgsEva0x_VjJT04yojGO7_q1AAwKBRvYwXmY1jEUPRVE6U3VP59JxElsGldh_oAUNL-4Yzk6WL0-NN7kZsPcWvskswNwdYLSry2iXEw5NW1jmJULejmM3RuXihs6B6VALYaPUF-cNhoO6V4l_fdPw4NjgL9ASPPZfNLxdsSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هایلایتی از عملکرد فوق العاده ابراهیم بایش وینگر عراقی الریاض‌عربستان که تاسال 2026 با این باشگاه قرارداد داره اما‌باپرداخت 1.5 میلیون دلار درتابستان پیش‌رو بند فسخ قراردادش فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24415" target="_blank">📅 01:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24414">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🏆
هفته‌سوم جام‌ جهانی؛ فرانسه مقتدرانه صعود کرد و احتمالا در مرحله بعدی به مصاف سوئد میره. نروژی‌ها هم بعنوان‌تیم‌دوم به ساحل عاج میخوره. سنگال هم‌احتمالابعنوان تیم سوم راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24414" target="_blank">📅 01:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24413">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xm2T8HUiHNCzbOXtP0epR53prDR71czlOHilzHdd8d97qWE8v2o7qCyZYG9mUSD54MsF9GLE7R5NIwa8iZbhFqZqDOEkp-M3xtpEUHpKw0WvKHIjzbQCSbll5sOFGD6NLFr68cRWxD1Fbsc4cgW6wzDmTJxEZ_s2z2jNonOXjSxIo8aDRQXRHTFmLm8wOgexaFvw2T5pNDvCRBxobS2u8HLgYUGXGPhHytW4DSyw5XmDbCN-K-wdj78H96s9GQSxxgQadcibMsh8tQBSO-79IVuf-h6lIkHWvQK4StV__pSplWqL5H9FgiYA7iZ0s9DdIf-81HzN3jUlgvbG7ow0nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
علی‌تاجرنیا رئیس‌هیات‌مدیره آبی‌ها: وکلای ایتالیایی بهم قول دادند تاآخرهفته پنجره باز میشود. انشالله تو هفته آینده خبرهای خوبی خواهید شنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24413" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24412">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLhd5iXNYhVBaxNZTn3qSv1GV0Cb9JYFHlhL7dsBTjp1wPVkqQrBJP3jrVOgWIMLvYcBgKZJOAuSjKtlpLCaltMHowz1mX6XwvzwuclGWN90YMEY3RXWU6m9KRhmMZw1c6pCjRL8OupQUCQYucrkhOjNJzGzgf9ZYKJ0Fge6OVpU0hzcfmq79BwuBRrYd6KCbqavXQKVu6gtzr6OuNB3N2WVub9gcTgalMoH0xfeiZvAiTRI2z-e0qwLNTOwh_BfbpqdC0goyC1s4Q_iTzFX7oPmvg1UNKbkchlyeks331TINGHybvDYOjhOro3N2yAZLmJIxvhMrnIxedy3f73wpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله‌حذفی‌ رقابت‌های‌جام‌جهانی؛ داره کم‌کم جذاب‌وجذاب‌تر میشه این دوره از رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24412" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24410">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxSXgiERf5n0OMDRKXC7eG7ArnDWYdQ0nc7LqcyQ0QpnK8AoiQQGCGIkwcAY2cqSDaXqc9gQhPv1qPXZ72r3x2lPUWWPfvRWB_JQM9Cu87Uh8o94Oekl8SkT-oCReQrXe8z4_NZAw-EF7oLQmn1ePexS8T0KfCMDfdZ41tVXz6BpGFbahwa3VGWDXRV6UsHn9IuiXhJkaj0yCObx-hwm2k4dJIsYGFuGqlRIJz0ebg3HE1pw3I3tsdZcHfnYlqKLjf1bSwsCMQL8DyvrM0xYnUu9m8T7HjG50pmRHzwy3gfVMyNJPK9cJc7St-PVEz-Vtp6_Hb_CeenU-7mQxvmVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم جام‌ جهانی؛ فرانسه مقتدرانه صعود کرد و احتمالا در مرحله بعدی به مصاف سوئد میره. نروژی‌ها هم بعنوان‌تیم‌دوم به ساحل عاج میخوره. سنگال هم‌احتمالابعنوان تیم سوم راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24410" target="_blank">📅 00:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24409">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mg_cgDpjNxU3frGg8nQVu0jsDuTehN5lQbeYFtl0afj8tlWZ57YAN5ntxpxDBldrgotnJKTLTGIRU_6Qx1--3z1E1XHH4tnakp9bgFuouIKvs-t-Cu5BKa4lEMisBog3Pe2ulh8XHtaLTGOpQh2UvOmVAXKHuq2GpofXymQgULTR0o2eWF-Rl6IJA6EwyA3yvrMkgRLrH5G2QSkXNG6CxbU8PE1dDlhj0v-nBN6Z82ODj7WejfW4xPZ18G7E90H3RP2dTrKlYbHu9qY4AU5B0q2ee079kaZ7WDbhI7AxZcxIAgi4zoCqomncWSzaY-fP4Dq722wxCbWZqBR-jFtFog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با برد پنج بر صفر سنگال مقابل عراق؛ حالا اگه بلژیک‌نیوزیلند رونبره‌ ایران برای‌صعود باید حتما مصر رو ببره وگرنه بعنوان تیم سومم صعود نمیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24409" target="_blank">📅 00:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24408">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqYAUnvzYpC5S40Y_zKYEl7DeNaiWqD1xxiFq_-oTEE5dHw4i314j8FDtTe355XDAZmxFHnpGlS4-wb-_0OLYRh8CJrpB99_yjL64FGvBN9x4jGfpq_G4OI1eTNPZ6KRtuZXQaFzGRhpAdtkaCG97Q4Du46Hmy9agTdOIZ9VDFM9Ny-PbYgK_VHFBXZNA0cu2fs9H3Ydqyd34ZXT2S4DQiXKQLDMy44SBmUv-TVk-3E2lI9bU19Yls9pMFWU9z9KEGo7Pl8KljVUOC5DmlCijOHXJ2e7TU0M2CRSRerei2h_gaVZCzfo0Jvahxq3mx_Th-eSILZgQsfOZlYja6Fw2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تمام مسیرهای احتمالی شاگردان امیر قلعه نویی در مرحله حذفی رقابت‌های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24408" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24407">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-GA3k0d7X8AHoy6VOtUoC2gnoSeFV-C_DcOp3QW9TUDUDH15_baVmUk1ofGCJYc5pIUOTu9sTUhwYamJ-9-bmnnzW5feZcJgYqOoTOdNmvjPG158XJfokCHNNcYKbukHnW8mD8IXQe2mfOY50S4rkw33q00UWB_gjpu-FiKEbUwmvnTuMHj_ilc7ymdx1BZZpdvNMsChKzs8i44zMgzUsPzhlW2-x0zx34iDDd1bD9lorQcOvJQjk1zqKAEcGPUU6h9vctnro_o-3e_xFZzkN_1jYJAxd2A4-tuXTgOTiNEFCY0OA14l_lFigvYEhR9D5ARbTre3VL6hBJ6vHx4Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24407" target="_blank">📅 00:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24406">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5uLrM5FXhwZsCGXBggMqCo25tkSUbGjp5HLsNoCdREy5buQ4UqNAN-BcmWruspZbGu2Gzf2DCX-zgpidDfDNF6AtWUmcbbpND0fwSB8EuCk1S-RhDa2uDx87Afa4UerRpkwpomT5Bq8F2Zolxmai0jxkQgTekTzrWtUQ8_n8mJIG7mi-dmN2INkoGgU-GZbWkPfzeZf-KDseGl-82Bu-MQVKimVQiumHrmHd0aDsGYUEwOXa63xHMz-7Fir3DFb7F9a18O7xawORNZRCCJ3VfoOrkVFeZrd59actSxyDNEUeow9tT50OkH0HmH86HvsSnkCs7sxq3BNKS2N-7DrrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ این‌استوری‌جدید اوسمار ویرا مربوط به آخرین بازی اوروی نیمکت باشگاه پرسپولیسه. اوسمار به حدادی اعلام کرده با دریافت رقم توافق شده 900 هزاردلار فسخ خواهدکرد. ضمن‌اینکه نماینده اوسمار با باشگاه تراکتور مذاکرات مفصلی داشته…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24406" target="_blank">📅 23:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24405">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec8965f3fd.mp4?token=WoASAXc8QgKm09GH2zylDqr-JSTRCoCbR81TE66txCG4IxN5gssvFwhCxyKokfomko2DFNkXugYcZUWFOjgBdnsU42fWp0i1WcDO0kcbYQWfWbAT83cM1MyvAC6BREBWclyTuQzkvTJbVzao3w_KtBeb8EBq0JrvI40uTt_cKdGvYZqKC79MTSyCa55Z9b0mZHhhNmpv6lQ8tLMGwOD7jelyKq2TUtm3jccKD2UwoKRIetwQ46z-Y8ushPrRT2leizGJ3wTPS8fEzROfPTx_HZroeNeDcUNOPS2nRZCP0FFaRvHAex554ajjODJQeZ7T5g4GpiacwC-T9rxY0RegCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec8965f3fd.mp4?token=WoASAXc8QgKm09GH2zylDqr-JSTRCoCbR81TE66txCG4IxN5gssvFwhCxyKokfomko2DFNkXugYcZUWFOjgBdnsU42fWp0i1WcDO0kcbYQWfWbAT83cM1MyvAC6BREBWclyTuQzkvTJbVzao3w_KtBeb8EBq0JrvI40uTt_cKdGvYZqKC79MTSyCa55Z9b0mZHhhNmpv6lQ8tLMGwOD7jelyKq2TUtm3jccKD2UwoKRIetwQ46z-Y8ushPrRT2leizGJ3wTPS8fEzROfPTx_HZroeNeDcUNOPS2nRZCP0FFaRvHAex554ajjODJQeZ7T5g4GpiacwC-T9rxY0RegCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تورنمنت‌آسیایی؛شکست‌عجیب‌سرخپوشان مقابل جوانان چادرملو؛ فرصت‌آسیایی‌شدن‌از دست رفت. از بین چادرملو و گل‌گهر یکی راهی سطح دو میشوند.
🔴
پرسپولییس
1️⃣
-
2️⃣
چادرملو اردکان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24405" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24404">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpNgawlMHSjI-t0xIEGdy7HNVEMNuJ3fbbfIJQm3P36e7wGq2XJdgfNAUnfjds0BjWkxxLvxAPyX0AIzHpF73n6kDAClpDjIEoNrkxplEZ_jc2c_hIRtC-pU5YsaE2HdLmHybwipUDF4UA-_Qa0TzDyy-X9V_arNkjqvJ8bOIerxXG8Z2wCLMj4GEs6bjbk0w7nmwr8kIXw7aZlAddIAk7MbK6l0Z0gnuvuUxYp4m9kLU1_Gv3xV46q-rB9psD9Jxe1cRIWyuAfj1nGCrwAfwbVGkGMYPkNhjpF57ndPSMO702UGRr3X4grjdZhFgxU8jZjZivMZOhWifJ70cHx3Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گل اول چادرملو به پرسپولیس توسط سیروس صادقیان در دقیقه 57؛ بازی حالا یک بر یک شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24404" target="_blank">📅 23:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24403">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c65cc2b59.mp4?token=uJlQKKruDAwwXED2-V-5E9NBuiIy_AbsIzeAFEy_LnkBqHUeERhjw_uFRoAOXenp3zM-dVayKBlB1sXDtDuEBWqNHk5ljV3_b3HVif6czJmM_OZGSH14_br7a_R-Mwnl8VUwmVT5RHiylfM1qz0rDAHoGKn0p3nUOY7e2nNKt-9ZVxjfgTfFt-LkJeoknk7CsdAa4vBq7MVJDQuROei77WrPv_w8y26NJMgnmY5P_EsLrfS7-9mYvBSd-r4i0gJHF1VSS2XI_J_pFj0_tOl7a-0J8bJtRB8OgKJRLISsOfujCRELN9berBFUAmw4ef6He2VfA8iy9djZz6JRBN1J8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c65cc2b59.mp4?token=uJlQKKruDAwwXED2-V-5E9NBuiIy_AbsIzeAFEy_LnkBqHUeERhjw_uFRoAOXenp3zM-dVayKBlB1sXDtDuEBWqNHk5ljV3_b3HVif6czJmM_OZGSH14_br7a_R-Mwnl8VUwmVT5RHiylfM1qz0rDAHoGKn0p3nUOY7e2nNKt-9ZVxjfgTfFt-LkJeoknk7CsdAa4vBq7MVJDQuROei77WrPv_w8y26NJMgnmY5P_EsLrfS7-9mYvBSd-r4i0gJHF1VSS2XI_J_pFj0_tOl7a-0J8bJtRB8OgKJRLISsOfujCRELN9berBFUAmw4ef6He2VfA8iy9djZz6JRBN1J8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌جهانی ۲۰۲۶ رسماًبه‌پُر‌تماشاگرترین‌دوره تاریخ جام جهانی تبدیل‌شد. مجموع‌تماشاگران بازی‌های جام جهانی‌فقط در ۱۵ روز از ۳.۶ میلیون نفر عبور کرد. این عدد رکورد قبلی مربوط به جام جهانی ۱۹۹۴ آمریکا حدود ۳.۵ میلیون نفر رو شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24403" target="_blank">📅 22:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24402">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abdda890a5.mp4?token=G21EI4Qs2CoTPAinZL0eD7fUDaErHIYM9GoWDHPdbddn4SbxRNlFA8vY1dY2xc1C8xjXu74S_mgqcfzqequDc_Bj83HdFFWSQpFsp4HEzJWpWXX1DW5CtMQJVLDPr2e00CefOd0RBN2Ec88jm7AukdTZDgivtPiVIHShKuWC6b9_aKSUcotBEQ0WBp0sFgDFywWOt4xz51RSM5FWzIbS7GDNM4bwJ8MtR45XKGGZ_emKI6ozztc4DN3G6fPMbzXc26wI9V6iQ4Tcwtg8dI-UFcirJQq64lIndYDS-yp5CYhnJf267ktN8DUYBnfDLRhDMsAL-iO2CxCJLK_llyC1Wn7fhhJAEItQqBvWUM1IyLVE5_LenGwBiZwiPZIKEnCpCRGWDhJ6A4_Y9TWfGoO9wPNmFKuwyHiRtO2JzHH_FoZQGHY43dCTAF4cJ1GFQ8pNvIiRy-fHAw6nMip6xBWdVYUoXbC1C7ohKuEbxIUxNpDV7W7UfgC6hlw7z4Z44NUPljguM0W-UNoFrIY_qvwUD48YiUdolSNwCzTrrb0n19WhCfAlBN38LzPC8EbLSw00NKr5gU6rf4dz2F8__e4xLkp6PNKPvRZXrfjfQtkEry9zbxH-TBaQzhGT2bxZjxyCDAma_XKwNrmN8b4iUYTQJbAWRK7MFV4izkKGPd39AzI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abdda890a5.mp4?token=G21EI4Qs2CoTPAinZL0eD7fUDaErHIYM9GoWDHPdbddn4SbxRNlFA8vY1dY2xc1C8xjXu74S_mgqcfzqequDc_Bj83HdFFWSQpFsp4HEzJWpWXX1DW5CtMQJVLDPr2e00CefOd0RBN2Ec88jm7AukdTZDgivtPiVIHShKuWC6b9_aKSUcotBEQ0WBp0sFgDFywWOt4xz51RSM5FWzIbS7GDNM4bwJ8MtR45XKGGZ_emKI6ozztc4DN3G6fPMbzXc26wI9V6iQ4Tcwtg8dI-UFcirJQq64lIndYDS-yp5CYhnJf267ktN8DUYBnfDLRhDMsAL-iO2CxCJLK_llyC1Wn7fhhJAEItQqBvWUM1IyLVE5_LenGwBiZwiPZIKEnCpCRGWDhJ6A4_Y9TWfGoO9wPNmFKuwyHiRtO2JzHH_FoZQGHY43dCTAF4cJ1GFQ8pNvIiRy-fHAw6nMip6xBWdVYUoXbC1C7ohKuEbxIUxNpDV7W7UfgC6hlw7z4Z44NUPljguM0W-UNoFrIY_qvwUD48YiUdolSNwCzTrrb0n19WhCfAlBN38LzPC8EbLSw00NKr5gU6rf4dz2F8__e4xLkp6PNKPvRZXrfjfQtkEry9zbxH-TBaQzhGT2bxZjxyCDAma_XKwNrmN8b4iUYTQJbAWRK7MFV4izkKGPd39AzI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
#نقل‌وانتقالات|رسانه‌‌های عربستانی: عبدالرزاق حمدالله مهاجم کهنه‌کار مراکشی قصد داره در ژانویه قراردادش رو باالشباب‌فسخ‌کنه و از این تیم جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24402" target="_blank">📅 22:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24399">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28a6fd59e1.mp4?token=IcDU8s7eB5W68kyuuE_7-vgai9TNM0lpwR80_kKhpfO6VLT0AoVboacX07zwFOJa4OmzmjEnDVdQIR3WdmFsd4Nq6eeCawfN23WNTQWUVERBx5JsuebLx-hEjdh0LAKh1ybzFmzlYwHzHXrYKncJe2hKvh6Q7Tz-0dN5zmibouP6PQUdVlqh5woixBkS8-ucbX8HgnivqdNCwYPRIBx9O9i3aDcjy0oP67DGpiZkl_VwHj1KAstz1_0QSEjS6PtnEmvXGFqEfP4wRQgtrudetvQ9l4gThYyWDRxXwAsmV4VdJDnzNN9idEuvr_LRthMaxhwfnqGZ2kVCxzaMZB5o0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28a6fd59e1.mp4?token=IcDU8s7eB5W68kyuuE_7-vgai9TNM0lpwR80_kKhpfO6VLT0AoVboacX07zwFOJa4OmzmjEnDVdQIR3WdmFsd4Nq6eeCawfN23WNTQWUVERBx5JsuebLx-hEjdh0LAKh1ybzFmzlYwHzHXrYKncJe2hKvh6Q7Tz-0dN5zmibouP6PQUdVlqh5woixBkS8-ucbX8HgnivqdNCwYPRIBx9O9i3aDcjy0oP67DGpiZkl_VwHj1KAstz1_0QSEjS6PtnEmvXGFqEfP4wRQgtrudetvQ9l4gThYyWDRxXwAsmV4VdJDnzNN9idEuvr_LRthMaxhwfnqGZ2kVCxzaMZB5o0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به چادرملو اردکان توسط محمدامین‌کاظمیان دردقیقه 49 در تورنمنت آسیایی! این گل توسط داور بازی رد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24399" target="_blank">📅 21:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24398">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3569629639.mp4?token=AbNElVhzR06ydkAo2VC1BnFKjIXoG2JqUGgTx2JUYUWNQrYgrtyDqo_GHrrmn-fPgcLhfjkRrBpvdIQOHPGU38Upe5HwkjS7SpyZEEuqcKQyVaNiHH1IBuIry-BvDo6rI74Dqh-XVWy-QcnoerOfsj15x5X8YPMkRKzWuloCZi3-8gyPaYqB33F2hci_LM2rNYb0aC4C3aAUemnLL8ORP20vGswGld-Ewzs9jEi2b9yBAqX2X9gM-OaNhDvyqQcZCDNFr29CXPafm3W0-qTJJv8NzwnMmdCTdWywm5ySwPc1lh4m2o6SQZK2SGKmtUbRhgTjH544AXET56pmVqeqCFRKWDQK_4TdL6KUXJKvrEsgFUIdY2sM48XCFegxJw2up95Kg29PyO7_S3GO4mRM8WaeSF5lIlIJaY470s8I8GNPYv0GHRRG3IfyYOkTRcpCOgosSm6fGkfRFZxgjEwKA3ZmI1lDkRjQrlhLmjzQYNEIq__Q2ZlbxtN3V6Tlpy1ctUb0pMDQwXldfNg-v-EWGG7doNCv-BLblNKK9MRft4XmulNBsQSoSwY_TJFIBwU1XHeZNFSu_pFTULypdu-jEkMgEmFNCciwPkv1oBpHgGuh4O6CRYm3HFnjiqdvzx0AYbnUXqepwT9Rpn0sVSyJsY9W7gEi9dUedvtA5XLybYo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3569629639.mp4?token=AbNElVhzR06ydkAo2VC1BnFKjIXoG2JqUGgTx2JUYUWNQrYgrtyDqo_GHrrmn-fPgcLhfjkRrBpvdIQOHPGU38Upe5HwkjS7SpyZEEuqcKQyVaNiHH1IBuIry-BvDo6rI74Dqh-XVWy-QcnoerOfsj15x5X8YPMkRKzWuloCZi3-8gyPaYqB33F2hci_LM2rNYb0aC4C3aAUemnLL8ORP20vGswGld-Ewzs9jEi2b9yBAqX2X9gM-OaNhDvyqQcZCDNFr29CXPafm3W0-qTJJv8NzwnMmdCTdWywm5ySwPc1lh4m2o6SQZK2SGKmtUbRhgTjH544AXET56pmVqeqCFRKWDQK_4TdL6KUXJKvrEsgFUIdY2sM48XCFegxJw2up95Kg29PyO7_S3GO4mRM8WaeSF5lIlIJaY470s8I8GNPYv0GHRRG3IfyYOkTRcpCOgosSm6fGkfRFZxgjEwKA3ZmI1lDkRjQrlhLmjzQYNEIq__Q2ZlbxtN3V6Tlpy1ctUb0pMDQwXldfNg-v-EWGG7doNCv-BLblNKK9MRft4XmulNBsQSoSwY_TJFIBwU1XHeZNFSu_pFTULypdu-jEkMgEmFNCciwPkv1oBpHgGuh4O6CRYm3HFnjiqdvzx0AYbnUXqepwT9Rpn0sVSyJsY9W7gEi9dUedvtA5XLybYo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به چادرملو اردکان توسط محمدامین‌کاظمیان دردقیقه 49 در تورنمنت آسیایی! این گل توسط داور بازی رد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24398" target="_blank">📅 21:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24397">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMwRCMHH1nwWetqRaVvbbbIsqIqgqdE9vPHjfK1-Zr5xmaZp7xCLNp3yx4HR_RmG7kcLwVmXQ5Pbv-TGH7iuf1GdbkPp960HVwl7-Sxm6mQLdR3BNvJ98sbzOFEgIkVfKglfqarAeWnVVuRbw77Efx4pEeTK1Pktv4TllHhlZSdYOmGVaM24ES6GAC3pGTSfkGuJAVk2GcZjPcgc7Ak1N-mpBILCvoEg6FrPzb5_ceUzq1YEUSPLAUKWg3t2Odxkb9-Lv9VtA0iZsLWd13Yd4myLiJtXCGA1WRcZgDIbGd6LmeJwbUuHoWcPEeAc7peSg5KbjCigL2vg0bzfCDkmYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی والیبال ایران با ژاپن؛ ساعت 18:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24397" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24396">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=up5kJC4w--PtfIIFfdr6uhKTQypY_stpLBq-jIoeDANbtq9IL7Nt7YWBKsLnKCf4e2z7CfAIk7rSGgkz89zffz4BRuq7lf7JpUzxSrbxRdlmum534QH25rCHIsPTQYhyEDs2Q6E1KZoRW4D7kx0PpKzWmSotwGeUpIN1oFxMhwC25Mk3rpb-VMR2J15A6C-0hMfwXg0ZKTyEuPMHDztXP8rQwRwK5lhCsiqZpxxIYJ8etFrnnwj7aibDnrJK8QMsb8SW45I-4IHg62orLxyNQwm8tEmu-hMQv027JpidIiEo0lh8ongr_kXYJAtXDxGFvr115JCwThp8BGiEkC-ScUwfqT6QsCBMzC57sZ8H_2Cs8RmK8jxkFpo6bTqtLUHPlnYCheakWUarfDNk4FU1pBJVvrYHYD3z69ag16cAck8xrnhJRDZA4ryhFWUCMyV-0-o0bn_tqa8MOeSxcfJgPmJZCET2DW-0lJ0VQ2K-g3OMKHm2l4idNyz0mXxaN2x0RzVAYCM0kLt1BRRFRlhABHNIcabwov62vTguigXnh1Dv27roreZ8MiQHmvqToq0Hpn4QMtAvXEV0K1pNkfyERZmEvlhSn1yINpU8tV-LPbi_jcD_hWS1XoWU6kiTJjZNMMt-4yIkwbER3yu1sKXrY3TIzYcjm4PXSyBe06y54rY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=up5kJC4w--PtfIIFfdr6uhKTQypY_stpLBq-jIoeDANbtq9IL7Nt7YWBKsLnKCf4e2z7CfAIk7rSGgkz89zffz4BRuq7lf7JpUzxSrbxRdlmum534QH25rCHIsPTQYhyEDs2Q6E1KZoRW4D7kx0PpKzWmSotwGeUpIN1oFxMhwC25Mk3rpb-VMR2J15A6C-0hMfwXg0ZKTyEuPMHDztXP8rQwRwK5lhCsiqZpxxIYJ8etFrnnwj7aibDnrJK8QMsb8SW45I-4IHg62orLxyNQwm8tEmu-hMQv027JpidIiEo0lh8ongr_kXYJAtXDxGFvr115JCwThp8BGiEkC-ScUwfqT6QsCBMzC57sZ8H_2Cs8RmK8jxkFpo6bTqtLUHPlnYCheakWUarfDNk4FU1pBJVvrYHYD3z69ag16cAck8xrnhJRDZA4ryhFWUCMyV-0-o0bn_tqa8MOeSxcfJgPmJZCET2DW-0lJ0VQ2K-g3OMKHm2l4idNyz0mXxaN2x0RzVAYCM0kLt1BRRFRlhABHNIcabwov62vTguigXnh1Dv27roreZ8MiQHmvqToq0Hpn4QMtAvXEV0K1pNkfyERZmEvlhSn1yINpU8tV-LPbi_jcD_hWS1XoWU6kiTJjZNMMt-4yIkwbER3yu1sKXrY3TIzYcjm4PXSyBe06y54rY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل‌اول‌پرسپولیس به چادرملو توسط کاظمیان در دقیقه 28 در تورنمنت سه جانیه سطح دو آسیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24396" target="_blank">📅 21:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24395">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKbXl-AEpV1JLDNFaER4E1DJZq-FLrRIOQrm1ZZAZ_1fzGyiHLvwHXZ8zV1j9WTl7l6qnnV5rlwOXJjKzSBgQfA39HxLjL7NCkPr6mAmVOk9sGKByKYelnZjdlRckGk3eeLuzJcK9M32FNisi-k8vEG2UYimzDAJk62Fn8dhP9UfODQEFv7sb_APLOXuymA7Winx9Wvg9J3XGaL4wPe2fXoT1_ARvzSSH93NhvFJ_Pun_WFo3NJ5fS92UuKzQOih8bLlzEhL3ZL7IxxqKQzYQ_rkZ_rHQ6yeR3inCyFnCB0eAAMc6bkw1aEMjStwVNLg2yBnoUCPUKF_m_O-Ol6OXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#نقل‌وانتقالات
|باشگاه آث‌میلان با پرداخت 50 میلیون‌یورو به‌PSGگونزالو راموس مهاجم 25 ساله این تیم رو به خدمت گرفت. قرارداد ستاره پرتغالی باروسونری تا سال 2031 اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24395" target="_blank">📅 20:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24394">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBeWsTwnn7dYkfXqgb_Fjxu2Cpy3UGON-FYZ8NizqUl35TFYNKW2yASi1IRIfgsaa64nfShuXPQok8QOOUpNOWOBOgA244h71hMqSH0FjhBpRRI079dp2bO6smSRPV1UeZkWbZy5XgQZ8Baq7hhGj5LIM5i_uyJVuj-BKhu4PEpHrhwrH6-RUITDAlcHoPlxM_9_iLxjiVLQE-y2Ak6RDTdPraaM7zvI9pKGpfVF3ySekqRFbdifhOYqwuD4GR3j1xRK3bZBpuj-FgWvInW6d7JulNBD1Euzx7U0-xBJgMNmYBhHXz8pb2WYCrq99kxUlS4uDW6zQ2MRiCAGzOUxgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس باارسال‌ایمیلی به باشگاه ملوان انزالی خواستار جذب فرهان حعفری هافبک تهاجمی 20 ساله این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24394" target="_blank">📅 20:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24392">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ohPVPSX5yYYNelyGxeQUgSMW6119r52-Kqqr4ZvDNzdgRac7Oc-Pr6W7TfLAIWhAeymi2nKkdLlynWJERUnVKjx0UuI5rLr7Q6x79ZAv48Zg-UWl5Ftu4-RmlpFWfcvt6RPW35bVFrjDESgMujZVWwfaZvSRA8udE136WHVfF26JDWrH7HSecKKWfU6FJQWWlsk4x_INsJaw29jLuZFw_IuSx1e_psSjqeRujINPKJUGCVCg9FhJflg6cnlcAFzHyBmeXiqLbtCmcNApU8U1RSJzIGV7pVZy2V4Ai3ABtl0Y5Fne-1WiMQuXXOfWU1kM9mbYnJBn6I9fWrE-wMEICQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gm_qzfSIAv0NmBgBtg-RGC6rAX0ULUFxwjNdp_L1pPM-naYz_Zoqh1eL6j-8ULxrmgkAHDdCoBGcu68qCcC1T3rrRsyBtfjNhnGzNRVm5gUmh7JjVLJZj0CprHx4pT0Q7JEzdiQeadrF1iALBPQL4xRA2XLLqLo7boLsqFWFPW6oXwo38KvKWMvnSLlOP3yj3sTtmWOqL9BW0lHaXVGWFFG-9RSqgb1Y3w7fJrjWD4qwnB1ABMv5gCf2CWGleo1EZDLdU5p3fNtl3dHLSq9xdWhijnLQvoJLl-T40uLDqju0RG625IESomX6_f1YMEZsduDQZtEKtHyRzyABki9KJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ناتالیا شادل مدل استرالیایی دوس‌دختر کنان ییلدیز بازیکن یوونتوس. این دو حدود سال ۲۰۲۵ با هم آشنا شدن و رابطه‌شون رو خیلی خصوصی و دور از رسانه نگه داشتند. ناتالیا مدل قدبلند با حدود ۱۸۲ سانتی‌متر هستش و قبلاً شایعه‌هایی درباره رابطه‌هاش با زنان وجود داشته‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24392" target="_blank">📅 20:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24391">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vy8wI8C9A-34_9gL8_UJ0syOwZ_vyhdTCuszUtEYGx9cPXrjBqC-QxD-BtrHDmNpr8aHFFM4IyKeAwopSQkt2qG-nCpr_8apts767AVzZghs8XZIbibzc16KuMH9P7WIF738mURk9dYqPJIREdYtkDb7sZLyUlKc89x6u8y2gdtwSR3M1feeG0ysqjRuCpvVYHbZvY-SKiSLuWvNwu3eZ3nyV4WhzBKfnl5cLq42nJ-beRTXOFgxnXVe_6eboSphSnNgY5HF_AhJHQuJwjcP4y_k4flLO0NDn5H8Pc9eZABXRvc1ZJ29xVw1FroOrIgTL8ED94tZijs5idIJgAyusA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تورنمتت آسیایی؛ لیست بازیکنان کامل دو تیم چادر ملو اردکان
🆚
پرسپولیس برای دیدار امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24391" target="_blank">📅 19:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24390">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3mnbeM7Nn9AAQPtUTKWDf6S8ZrVIHQ6of7GTSvAAuiGhMKH3BNf5_LRdUvC4V2YHHHFh_q7d47yNsa0gOsuasoSZ-Z6ezSqY-sp36nLtcrzwaNtW2FvXIxmhYPmM7BpcxMc3g0Qm6zjo-g3-ADw-UA5gzCYDe4W4Z7Z6Esjfj-1eU2WXT3LOWy7Kx1LJ3XwP5jk1WSdDTJ6s7OS_uJYMtZGbfFvexKZc-iIfhwxcHQBGyO3T9LG5F3tP4VmmbMk9bRU8A7qiUXll_WMBxo0Va5wMgVcW3_mMzI8Gp7W13sxoY5PQTN_kOmuLMKmdpwR0enO4-t65LdlMmtbshFy2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تورنمتت آسیایی؛ لیست بازیکنان کامل دو تیم چادر ملو اردکان
🆚
پرسپولیس برای دیدار امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24390" target="_blank">📅 19:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24389">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOTDtxxvWaFYaxBCF6odLH9HzLhwxR3PDdtyrhvifRTINRib1eS033INlQpnH-9qQojRb0R24ZSLferVlOryjo8K43h83j1XG0PXGhlfNQpZOnlNkpizHtB-HZq6KyrrqX7tS4zrfV0Rc77vekCyVrcyyRjjfyfGJk5fMKJuYBClC1vsw_lNCguDZ56Fg7NHOptuFxSrFN3tYnIuWhVLeO6rxwEYyzgLyXJ6AiObOHpYM_4Q6AjB-mlY4oQ5vmfpd6mB8Vr9aB1k2iN1sfbMYKxYThRK9SM3gSBtwLTtmt0u2ASeChpybHunabDhWWQnCzsYLA8kY2J19oVLqZC3hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب‌احتمالی‌پرسپولیس برای دیدار امروز برابر چادرملو اردکان در تورنمنت سهمیه آسیایی؛ 18:45
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24389" target="_blank">📅 19:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24388">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NK567m-nuMVQIasF2v6uTO6zwUdFnRdcLO4UuJqv1ltRCQnfl1dvTT1f2nT3RqLaQgUWT0olpm1ufh-WFX2hYwp829BIVadoX7cC8dhee4dOQN1_dR04qkfsVG4nSJpQnh_6KBrLq0f-tCy0gjsY6MBqGgyc9297iD3akZRUegDcgS1txtjJXfMSmhj910BYeXiTbSxjiYOVN9r5dtPgPjQc2tfGhX7C4GsOPMIkxlKn706R1dLxfesvG5Vdr0KqHRKQwcFTj0i7Y5EMpWdnhQhrg01dvXyQ1rA9e39bRsZXDcjqvzJCJjov-E5AkWHaGbbmiZ9fUgh_C_Io6OKeiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌اخباردریافتی‌پرشیانا؛علی تاجرنیا رئیس هیات‌مدیره‌تیم‌ استقلال صحبت‌هایی با مهدی هاشمی نسب پیشکسوت آبی‌ها انجام داده تا درصورت توافق بین دو طرف؛ هاشمی نسب بعنوان یکی از دستیاران سهراب بختیاری زاده به جمع آبی پوشان برگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24388" target="_blank">📅 19:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24387">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3ZCk7SrX4CsdqPXmqIwc1Zd2mTfzELX4iQkP_G1KMC7W7NWUkPP39CWJItZJ7bXxCf1Ch_240CgC9cepHT4uHex1EnIBEcbugsdB6P8RLcO7Z70ZvYkmUi7bsBOFXEPz0o1AvkM40NjtbqqjQ2HxRltulxuXCMsN8Za2eWXit5-jaajeWztF_cTLK16FrU-_X3NrKCJNF6PUtG8TAS7gmE-rzQnkJKY3BlP8LCuSB2KFh_p7QRpFp_j9bSAFhnon0obaaCDjqcKuAMNjqE7K9T8sS_x4L2vCGH6K1NkdNF2vxn1tZq_pmEAr-i_dorZFIVJaH-rnHuYjq3jgDWRMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24387" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24386">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drzelFT0lllSLKM1mkevo0ZRlcapz5CXpjR-Dr4o_gy_D-cgje86A2nQQKoHtwRudPsZSDXiNWVvDaIRvFJcCg1V2jSFTKuQDgubIE0RCT_9p7srjOq3Ikinsvcl0uSTlLhPxXcMTVR0wABsz78JgfTDFewqREsX12B0oeeoA7BHqa-D0y0YprHJsA6VU6x-x6MQ1OtGQt-Y0qeiit0zoOifeZwI13kWKzXWYgym6S-tqSrU_p4pltQczgSdqxlrWgKg1xF8Wc_eo70DMhXSSv9Mqcs4wrPXRcJAC9xqiqma5Djr-O5Y1NU_OBFlKi_iRxqyktN3QrEPbH0Fxh05bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24386" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24384">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQsCoIyikDN1Nd9l6pKJrwlsI2F67JIbjKW8WlXWMAYJD163yE_kmG7vEetwyd69PBd0u7-Lss10u7AW7f3sD_IB8hFBRooCj8E-yCLbV2qiXtVpl-d5dK4_JMtBE4n7-VO3BNpzsrAQzDHkZu0_kBi0rmP_S4lmPM_AYssBY1ZljFE7VrTz6WQx3HMpsyXNhtOIuAZ1Vur7-oMA0-6qhrNIMRCpdolYmf3jBy8R_6fErBUbrHx1tdtOP-PxgEKXs_VKqu1usZ_tOrqeYb8SVtO9w3BXiUfnj54T-jW_dKof25xrdOO3qTCPr65ACMA4Mt2AERoCeEyiPqO-3RTScA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آخرین وضعیت تیم‌های صعود کننده و حذف‌ شده جام جهانی ۲۰۲۶
؛ تعدادی از تیم‌ها صعود خود بمرحله یک‌سی‌ودوم‌نهایی‌را قطعی کرده‌اند و برخی دیگر از گردونه رقابت‌ها کنار رفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24384" target="_blank">📅 18:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24383">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaL-_OiWEfSK6w40AkjI0RNG1rAfOreqXdFeVraOWBkU_WyIBgTggDHXVMZB7tl0dPLF0dlO-Nl630OQ9pPA7VCwScCl8ajPWdrLPBbPACtSXKHOqQ4VTylUHC23UnSYf835udArBOaSobT_zFsyKXFjjXxAv7voA9impcQK5S8CdK2nIM_wcdiqhIIr7wtWbJj_WdwnXfBGneejIOiOXbhulahSvirYvGtN4UYzo6-q9o-Kfd8kUOhCpCtxlxH1AgmJ2-QpqgjyOVgqzeEMYNQpT4JAmje8HmJG-I7nHa2NIFcvUQQl-22CPaEHW0diKjWepiVo3eQ_hjFS8ePr4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛
ترکیب تیم ملی والیبال ایران با ژاپن؛ ساعت 18:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24383" target="_blank">📅 18:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24382">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJO3Pw4lKslXSYw9mE0A3YJNI06g6N43mlzBTrD2MW5jg0TFBfdb9XzemGy5IVOyjOcMeXq8kmucY0U9FS5gLg5jjtDdEAcvLBznoj5Sa5l19oCWe387MyIaUwee6zZZCQ3YJ1BY4lBdxlBO-9SOo6SQuONJ_Smh8Y4ub6wmwc39Gbzqu6p8EcIwo3DrMbwlM8Zx-0D6Yv1AdaMHmQ28B_JEM-f4BrTWZiurtfxaXawIUpThlCJ0XvLH2GZPpb3TYKXhQpr3Aezdya1wU61-bHZqkGh5yh2m7WYRznBlMqATts53XdoqTi6MoDKfbguOuqxiTuFwXT_OnDngurg1IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24382" target="_blank">📅 17:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24381">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cd3DZ01i5_fMTpIAICoFnk3TRTN2qGxzzEwCenWt6Na7d3ENr3RUe555pLGmQ_ADM6uT8rKyXOcwOPFCc2hLRLWeXlqedsrHyoM-zolTOZvnGAOsl_9_f6_vE0zQIQERiPB93fevXc7VFPu65sbhzt6KD6v_le1kWxYJeLpX4TsVsJ3G84XNo5Nf5sID0B_V_K2G7PuXVo_w9UIoiBQItPNYuR1nkidghbrdjWB_v3eQ6LNmhMPtZu7b6ZmfjxBDnCmWEFnW1n0XJXfv171bhhJzhs9egabAyEibYhCJx-kADLKOZlBrYWYVzA-HaxsItlzyzQK8gpNhA29H6y8nuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرچم‌حمایت‌ازهمجنسگراهابین‌پرچم‌ایران و مصر قرارگرفت؛ فرداصب قراره ورزشگاه رو از پر از پرچم های رنگین‌کمانی ببینیم. فیفا گفته هرکی از قوانین ما پیروی نکنه بین 250 تا یک میلیون دلار جریمه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24381" target="_blank">📅 17:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24380">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoarWdTq15OE6bULm6B46d3Buxz4zbRkhn6RkIJEdakNlD7W5ew8rGcJF4ZRO45ymMnk-Zu7ZbVlr1xeKpef9kJQ9sR7uz9SJs4ub8L_qWt1FBQHR0viGZsby2yy-QASyjLZom1vhgmcG-5XI0HxW50EJTl7NTIw56UY_KNWkAveX8gRiPjBcaNY5knLeZ_GNoE7WDpRgllSQlhjBXfw75J_7bATQdvGWsS88ril0FO_Y3kgltGLWCgTvTdItBUfeFzf0XIKD0cP31iEeGTWR7oSH5FnaT-lULUAEgv693xnerSWNa9k4eVvuGniryIHeeo2gJEXK85wAcD1kTOUpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت‌ باشگاه‌ پرسپولیس روز گذشته با‌ارسال نامه‌ای رسمی به باشگاه الوحده خواستار جذب مبین دهقان هافبک دفاعی جوان و آینده دار این باشگاه اماراتی شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24380" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24379">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-NtTnQjGILfeGfRFuy_Rp0OoQw6MoJbwobbJoyG_55AgifESAj0t6_TFnds9Ma-TS6iXFedRi2J6S7-vauoNCru-F-CIXQCIR8cJ_5XpHlMx7j8nR4UK_EF3ppmd7jk2Zi2nsvtYw3mtsOFluaTVj_j3z9oAzIlAhz584NU9w2pnttKxpkP18LPe3j0J6dd98Yo78b_-TnLy9s4h9b-ObMgoSrIijZyEKCfKJSBkn68rS8LpuvQ6HxPkncCtVoz6EORubEMD6jfuYrFuZBNrn1usGogKpJFqYAiEQN5X7VqZn6l4D4KrLawFftlbtwelpi8CWVgDVG_PvpznKUZFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ داکنز نازون مهاجم 31 ساله تیم استقلال دربازی بامداد امروز مقابل تیم ملی مراکش این‌شلیک وحشتناک‌رو روانه دروازه مراکشی ها کرد که‌با سوپر واکنش استثنایی یاسین بونو مواجه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24379" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24378">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2f7b8fb9.mp4?token=pUuNiLR1IuDQHpSnXPplAEIhcofiXSEeFupdmiq5xcDZmMrzT3NQrBPSOShMQHEcKHR2I0lYkDiTfhOldTYfBxnnfwwGmFKS5MMXf27uBNMzNQESQogFNqOffHLE5iucCZOQYPOfyUQAbUcvdTUvEwO6Cz55e-JZ9I8Bs3KOFwFGFlCx-CW696ZgQhR9v6faqKwUYh9cBgcbiDhfmqFumQqMix8FS2FH65t7-MXPw5j9uUhhOAWVJKF6fKYMRfjPjUKyNvvXg7Nek46a6iibi0ANeInPBclIbKkQaxR25U_iKuIqcNAZiUfwK6tVBBdTuVocdcaEYK3LU2UVjUztAjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2f7b8fb9.mp4?token=pUuNiLR1IuDQHpSnXPplAEIhcofiXSEeFupdmiq5xcDZmMrzT3NQrBPSOShMQHEcKHR2I0lYkDiTfhOldTYfBxnnfwwGmFKS5MMXf27uBNMzNQESQogFNqOffHLE5iucCZOQYPOfyUQAbUcvdTUvEwO6Cz55e-JZ9I8Bs3KOFwFGFlCx-CW696ZgQhR9v6faqKwUYh9cBgcbiDhfmqFumQqMix8FS2FH65t7-MXPw5j9uUhhOAWVJKF6fKYMRfjPjUKyNvvXg7Nek46a6iibi0ANeInPBclIbKkQaxR25U_iKuIqcNAZiUfwK6tVBBdTuVocdcaEYK3LU2UVjUztAjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
توصیه جالب جواد خیابانی به محمد جواد حسین نژاد ستاره باشگاه‌ماخاچ‌قلعه: هیجوقت تنها نمون. همیشه مادرت رو همراه خودت داشته باش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24378" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24377">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnl_KjtrrPF-m2J9vsxY6NgibdlMyH7BBsj_OxST-HfYPwQdtMe7Yr3nyRSnwO7xz7UnVBqVxnof9plYS5IerJq8-SFtv1fcddr8CayqrLC8kiCOlbiAgjvEm2NIVBGKjlmVVzxlxOU7NULk3akUWHQh4_Fnqo36D7ZaQuLFexe2-t6VUjS4LPJ70rAZnacgbwSv500Y_tyZX8rJP_JmLwB5bfwTn6b0B3e3je3DGK6i3F0aljxDs9cwfSxJBAknYhQH3vryJbwhWaonOHwqfXbEFI-IPZwAjq7HukoMmEF6zS4cshn3nmz-wK7xc5U2rXGghkObVdoEzdFqofH5-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران
-
مصر
نمونده.
🇮🇷
⚽️
🇪🇬
⭐️
با پیش‌بینی این بازی، هم
۲ برابر
امتیاز
می‌گیری و هم وارد
قرعه‌کشی
iPhone 17
می‌شی.
📱
🔥
باجمع‌کردن‌امتیازاین بازی، یک قدم به برنده شدن موتور، توپ طلا، PS5، iPhone17  و ده‌ها جایزه‌ی هیجان‌انگیز دیگه نزدیک‌تر شو.
🛵
📱
🎮
فرصت‌رو از دست‌نده‌والان‌پیش‌بینیت رو ثبت کن
👇
🔗
روی «
لینک
» بزن!
@Snappofficial
🏆</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24377" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24376">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvYPWp8LbBq51BHrQvIdslTTeFh_0XbDYCx8iEZVLqfZ7TV4DC3Ldth9oPcOgrHdS_EjtnuJIJCPd1NBL0eoj7TfVhqyXH_JnGsZYDKw_0V7qNIQ8hYUkOet3JmSHFpklcN5xIWqJIElqIDic3lX07jZpdfkCHJQJJQo3IkaF-AWM0geS99GaN9BobgGghqeMA1kYWOdPC9xBBskBOZaM7qdD0jBTZnvygnjRyXXWL3Xr1eJWvoCi8irmQAmVYWUFcMO_nR7qBEtvf8pJKUUj266ZeuFsApUBKLJBbPDwCGNGqc4e9v8AGK8GiJgv-E76bomqeh7GjMS0nrl7ZviMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی
؛ پرز از اشتباهش درباره مارتین اودگارد درست کرد؛
باشگاه رئال مادرید برای انتقال پاز به کومو 60میلیون‌یوروگرفته و یه بندهم تو قرار دادش‌گذاشته که هر وقت نیاز شد با پرداخت مبلغی ناچیز این ستاره آرژانتینی رو به برنابیو برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24376" target="_blank">📅 15:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24375">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTDt2yhQJ1nPVIvIOZ5n1XWDdW9TPJSlsEaXe8W0N6Xfl9umubsBcyyBqJnjuswF-C_3cxXsjlHHIldtrOtCceuJDEcf1emmISaiRuFOXlw7-MmuCgz2OiMFXs8__Lz2Op-w_HGKcMHGfyTJJQtGRKYUTISbERqlzt7c6kBGlNEJgVlbrxV-2FAuDgCN_qL0uwaa-UhZddcJOegZH8Q-kaTelPW-qj3a_ZGg0l_nMlK4_zzlIqcHGIp6IhygsBc8oI_bPOV_NjVpN2G1ebmZWNY-4DgHGYQiNNh29n6Czm2zGJgB1OA_CO5xMjeBuUuMCMrYORD9NCsd7k41GJGx7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
اسکای‌اسپورت:باشگاه‌اینترمیلان آماده است برای‌جذب نیکو پاز ستاره‌آرژانتینی‌رئال مادرید نزدیک 70 میلیون یوروهزینه‌کنه. پرز با دریافت این مبلغ بال در میاره و قطعا ستاره جوان تیمش رو میفروشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24375" target="_blank">📅 15:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24373">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c26EYPnXMWMt2a3NzhUpGjy5PuZgCjnwYJ86W6X_FbWPhHRAYLUFR39fb_roguYvV_yOXKUySEPIqTI3MLA4qQZRpZGStzyxhZPz9OK56zC1gm33cdX6FcHV6kHE4pzrxbBP3fWepd5DxOdrFXaHoqqSXqjJDag_yvSaAdC29_h6ydoAs8Nu8bDp5NYzNuER7DgYie0Lvu0X2d-qrdtqcqoR_jf1vl9yuvqpB_4JFNpMASkq858KzOHiDWl6dmHKXsHNidNQljVIxJTphyzzGnsr3VXeoUYt2dE_Z05p3J_HX_xKAFF0_8mqoHX1P20mbGMIVELHxgd1WOLKxELcxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=pNnBlJaJAN9QbLusrO7WxsRpQkulm_eo3zRZtObygfuLJTxELW2A6HcZBlEkjm7AGv0MCzQQNauQyFBfwigkxb_nrZf-o1WGbsp2-1XlO04bTgkK6NicrMpNZdazYXAozrjFXT6CJmJiftAdIp7BMHwFEwcjKjTuwP1XQ1BCvjthf8ukwKtSEQrPjdcKJKAaINgisiAMWfvwMOAM4_nEXEUTJNNwkmkj0HpNSmGsLdTh6bsz6UalHL_lo7yeTgcbcx5e7z68AY_jfbWhT3vq5lzOf8f0vAE_C3pSQloOiHONrgO3kVaxr75E8lGumYvBcCAhYZ_teJFZJGarLkftLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=pNnBlJaJAN9QbLusrO7WxsRpQkulm_eo3zRZtObygfuLJTxELW2A6HcZBlEkjm7AGv0MCzQQNauQyFBfwigkxb_nrZf-o1WGbsp2-1XlO04bTgkK6NicrMpNZdazYXAozrjFXT6CJmJiftAdIp7BMHwFEwcjKjTuwP1XQ1BCvjthf8ukwKtSEQrPjdcKJKAaINgisiAMWfvwMOAM4_nEXEUTJNNwkmkj0HpNSmGsLdTh6bsz6UalHL_lo7yeTgcbcx5e7z68AY_jfbWhT3vq5lzOf8f0vAE_C3pSQloOiHONrgO3kVaxr75E8lGumYvBcCAhYZ_teJFZJGarLkftLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سباستین بکاکس؛ سرمربی ۴۵ ساله اکوادور بعد از اینکه دیشب تونستن آلمانی‌ها رو شکست بدن و به مرحله بعد راه پیداکنن اینطوری از بین جمعیت همسرشو پیداکرد و از نرده ها بالا رفت تا بغلش کنه. البته صداوسیما این صحنه ماندگار که تیتر همه‌رسانه‌هاشده روکامل سانسور کرد تا یه وقت تحریک نشیم. برد اکوادور روی احتمال صعود ایران هم تاثیر گذاشته و ایران با مساوی جلوی مصر احتمال صعودش به عنوان تیم سوم فعلا از 90 درصد به 60 درصد رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24373" target="_blank">📅 15:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24372">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0edb018d7.mp4?token=AhPLvBSooe4u5NUtsWCODNlo8CUaPM4N26GyaJf3uROGB4zHQJ0Rx7wO5nS6TH3AGKUb6j6OhlFcxrZDj_FN_Zs32OjMA3ZN8b65b_oh3oRKBOIntI8CFc3xB5tuj_-5eXfz50ce7luPJYCAbGey-pncok4oR-vjBOZURxCgciNAoYLE7ODdG3WbSLaZawNaYr8tLf6xhHLGffSj4awrridxBMGCaYk9rHCozZW6UCKhnV6OXtWR-xc9BgeD4XOMx4mjzR-ZjoaIoTc4vCLIQkRAr4_DT-1S22jATD2HLxAK3Cz_VnyjGL3OqjROFagAG1mQHq4QUSFQYeoK0GaQOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0edb018d7.mp4?token=AhPLvBSooe4u5NUtsWCODNlo8CUaPM4N26GyaJf3uROGB4zHQJ0Rx7wO5nS6TH3AGKUb6j6OhlFcxrZDj_FN_Zs32OjMA3ZN8b65b_oh3oRKBOIntI8CFc3xB5tuj_-5eXfz50ce7luPJYCAbGey-pncok4oR-vjBOZURxCgciNAoYLE7ODdG3WbSLaZawNaYr8tLf6xhHLGffSj4awrridxBMGCaYk9rHCozZW6UCKhnV6OXtWR-xc9BgeD4XOMx4mjzR-ZjoaIoTc4vCLIQkRAr4_DT-1S22jATD2HLxAK3Cz_VnyjGL3OqjROFagAG1mQHq4QUSFQYeoK0GaQOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏰
بیدارموندن‌ساعت 3:30 صبح برای درس خوندن
🆚
بیدار موندن ساعت3:30برای بازیای جام‌جهانی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24372" target="_blank">📅 15:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24370">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cudbgcrhUoeQ4dlTOxAXJ4AkotSLQIIdbVTevULTYUHjxExpz1edh69pvdFnESHHaX4qxazIAWMK83JvIZn2rU0NNXzmB256urk03-dLSV6ssuIsGCniXnXIBdrk5yt5r2pIw7zPB1jAny9C0hL_RhWSoacacUaYCntzv66YfMZPPCt9XnCiEGPB9qGwWH49CC49pLWQDKkIHE3VT_TSZAz1Xn39H2lJi2toYFXWea7t-LG4YEuas9KMUl1VkrpG8wAkiGJh7mZPhlpkfnca7_xmoI0oVrSuy_UI9WHnbhMICIT4E7MfJF7ZSRamk_VWuO3F7TzkkgXtxRNGjkOxmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dbdox9Zjb8nrB1q7Ff125y6WhGFkLPVMSAp5hM3RuhIuayb20JNbpw4PVUPsDTw7O5WOUtO-wYKwSWm1ScCuf0cGrprbsi34jkczdQUc2t7ap423W7zD_fG_RSEAoB27p9ACHuXKT5QeFGCsRf56hfH1FV53CuSAMN1Lc3bVwBWEHxRVG5rT_6KNpTJgVg1r8o2mLv11BERqPq1ui0uwC-ReCsQj2pXuDYa8o-QOAtr3iN_CsUWXygoDWUvb3SJTytZZqSwblioZNvKNY32iG_0hoCXUd1UsiLT5bSImxXmNk0luNivqyz7WjHcMm5fNry-SQbz_fI_PUJvuqc29VA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24370" target="_blank">📅 15:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24369">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxsODYejdHEIbKluSIqZFiDxCXJRvEnIiaaL7_OmBs9QK__IzqxpF5SNY-l-rel_T8smRsKZtIvrv91iBVz4c6a3sNlGcoYxI9m-GOn8j7uQi31B_wdLSmcUzp71hKUoMWwayNcVJQuRL7D0JlnPCZPgkg79MLQMUpQCKbXkv3gR40VtvAWCA9--AxkTphlhYO3jQhaul0p5jZGdHIR68HdhepPnaj0dnMovxzMpEGBYV-G21syRnY83RZJhwYBwO4OnL9VgGKYYQQzEgTHTXokdV9kF7aVQioSD3az5H43mEAvz8JF40ZYLSGdJ9NQYz6fjMrADuHBHQnN7R8wHUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال ۲۰۱۶ سمیر نصری که‌بصورت‌قرضی‌تو سویا بازی می‌کرد، برای درمان‌سرماخوردگی به یه کلینیک تولس‌آنجلس رفت و بهش سرم ویتامین وصل کردن. بعد از اینکه کلینیک عکسش رو برای تبلیغات منتشر کرد از اکانت توییترنصری چند توییت عجیب منتشر شد که ادعا می‌کرد علاوه بر سرم، «خدمات جنسی» هم بهش ارائه شده! توییت‌ها خیلی زود پاک شدن و نصری گفت‌اکانتش‌هک‌شده.بعضیا هم حدس می‌زدن کار دوست‌دخترش بوده؛ نصری امروز 39 ساله شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24369" target="_blank">📅 14:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24368">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ab6e00db3.mp4?token=bn1qTn6pVw2HOoE_D8u6XnN1HgvlVeUFFLQ_v3iaaNxUs_c2y1EtSo_-o0G7HLrekMDfb16930QRSV8va3XxeE9czsjCr1C6ZZo4ommcsi7ccs-FpStJuWn7sYZdiSQFKdbgH5M7-awEuVwHev4xhaXtL4CMWnYo1tXiLX_737rnc5SVEfkWbPhslaJYfHFVqdGPiDf2gwhG_gSdYNDyEdxxx1Pj4tzxZd08_DPs2Rnn532PwLumkReKmHL5-OXnW6bSz2hz5ObjKf20aw1jOS7BZsV_Vpjw2iuonhbeiAUXWTOdxbB-CDM_YM7TaVdDMIg2kCrPdMmO-wZ8S0zWPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ab6e00db3.mp4?token=bn1qTn6pVw2HOoE_D8u6XnN1HgvlVeUFFLQ_v3iaaNxUs_c2y1EtSo_-o0G7HLrekMDfb16930QRSV8va3XxeE9czsjCr1C6ZZo4ommcsi7ccs-FpStJuWn7sYZdiSQFKdbgH5M7-awEuVwHev4xhaXtL4CMWnYo1tXiLX_737rnc5SVEfkWbPhslaJYfHFVqdGPiDf2gwhG_gSdYNDyEdxxx1Pj4tzxZd08_DPs2Rnn532PwLumkReKmHL5-OXnW6bSz2hz5ObjKf20aw1jOS7BZsV_Vpjw2iuonhbeiAUXWTOdxbB-CDM_YM7TaVdDMIg2kCrPdMmO-wZ8S0zWPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیم‌های ملی ژاپن و برزیل بعد از اینکه از مرحله گروهی خود صعود کردن به همدیگه خوردند و این مصاف جذاب رو رقم بزنند مصافی که قبل ها در کارتون‌محبوب فوتبالیست‌ها پیش‌بینی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24368" target="_blank">📅 14:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24367">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=dm50CfP8DQvamQXlIsPuU4hfSANJ-i2TW0hmJqAAWZXjpujHTdIr-kNBB0e5y6uCGdCaSme9T2NJ2eczcep881RexrqIBmVfTD2bCL90cIDm3thkFXz5D37huBqoGV18YYVnGKfIHYRgL0Xj1TkK8CdgEJAOsP9FnNFHQRxC-Cw5Qmt7Vg6orm2aHlYOtv74RsHMcwDQSSC-Yy-B0BcOKPNd8QVWKL5zKFH4JAMKj0KWokWfnUgbkiJgsgKZl2-2K9uE4JgDfw9mrIryVQT5K1cPNZzdIQdn_diwmx3pgg8R6wQXWna5vm_t6nD-snziKa--IHu5PVAdbBKnQO9Fdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=dm50CfP8DQvamQXlIsPuU4hfSANJ-i2TW0hmJqAAWZXjpujHTdIr-kNBB0e5y6uCGdCaSme9T2NJ2eczcep881RexrqIBmVfTD2bCL90cIDm3thkFXz5D37huBqoGV18YYVnGKfIHYRgL0Xj1TkK8CdgEJAOsP9FnNFHQRxC-Cw5Qmt7Vg6orm2aHlYOtv74RsHMcwDQSSC-Yy-B0BcOKPNd8QVWKL5zKFH4JAMKj0KWokWfnUgbkiJgsgKZl2-2K9uE4JgDfw9mrIryVQT5K1cPNZzdIQdn_diwmx3pgg8R6wQXWna5vm_t6nD-snziKa--IHu5PVAdbBKnQO9Fdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه نویی درباره حضور پرچم‌های رنگین‌ کمانی‌وبرگزاری‌مراسم‌حمایت از جامعه LGBTQ در ورزشگاه سیاتل گفت: مااینجابرای فوتبال هستیم نه مسائل دیگر. تمرکزمابرروی مسابقه‌وکسب موفقیت است. درخصوص موضوعاتی که در دین ما ممنوع است و وجود ندارد، نمی‌خواهیم صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24367" target="_blank">📅 14:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24366">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBgw3qpK_Mj4eufCgYrZYTnunPDbmxjF2ShOQjykPFTetwB2-LUm4g0uamx7U4vbxCgt-gq8exnzq8bSWRc39_hGHBvNTD9CuF9Oiq-0EOk9Xdtm6uzfx0S6N1SFx3hC5FBECwpVnYw26Jb9PsWXBF9Wf2q6NseWId6436uvDv49aZZFo_uYaGbmG5QLOkvvlWzPmJLdMDM31SId4UAL9mDaa6B8b0zurkkWXJG0jpqmHCdMhHUY6q24sOSzjKP3pSzfCMpZ4x2wl5In_a-yKdqgvIXsZhe0EIS-4HL-ufaXwOaxsyzcr4q8QNImt0BM4XWAWAyhQkAZO0o_qgp44w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
دو پست کریس رونالدو و لئو مسی در ایستاگرام رکورد داران بیشترین لایک در جام جهانی شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24366" target="_blank">📅 13:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24365">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTebTIWWb3tSoS5jHL_FT7UhwGQ_CjfIBuDzVDGfrnVWq_EA7izldCRbIRa11KewfJBAB9RR1xUKKiFRkhErVpPfeUg80m3b5Gxx1tP-UdTsYjU_eojYeGrGOSKwM1KSMXQsKROdvw7bkuPB6ArrRWgb1FXM4Q_fRpWE3uEZlGLMOOpMNkkj4E7DbpxqBYZVCmeDxbJrJ3-6MwY3kjMc49b9uIiwwE3vpqAdmjCdLxdHys4HqwZRpZN0eiYiQ4pm8w0UkhH5k9nSvoz9af2t9Bh3k-veveLXIDiwv2EPJMaV2hnbT8p5j-KTmcXyTIlNoQDVV7NgZBf486FufJwXjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇬
عمر مرموش ستاره‌ تیم‌ملی مصر:
ایران تیم خوبی داره بازی‌ های قبلیشون رو دیدیم اما ما اینجا هستیم که قاطعانه این‌بازیو ببریم و صدرنشین راهی مرحله بعد شویم. بنظرم بازی رو سه - هیچ میبریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24365" target="_blank">📅 13:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24364">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roj1LUKWr4b4L8c9f_gLHpQ6FvCaFt57-bh8EqSrzI8sTbshFX42B0Y-9eIzZz2qSBXxp0g77vWD3Am7J6Mw7r2qx4hT25wt_BRGuAaPWbo5rYeA_knA-Fl84D33tYNve9wK1JTbbn0yz6rJBQitR6wHOSooJE_2Sfkleds_f0Ym0j4rU_a88OCeDW__1lbP5Vx-dg5mZffwXStmbL2k2tJLiFrY3J_jNifeJd2Eg62DMrPgUtyjpLpOizpn0RH7GDTW_2NeeU4RnMKSyKNFdQda89JzzsmtoOmFQpP5pYtoMo7l5M4ZXQy7fMSvm3xQmxjo8fDRwexf1D0BRSL5CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
اسکای‌اسپورت:باشگاه‌اینترمیلان آماده است برای‌جذب نیکو پاز ستاره‌آرژانتینی‌رئال مادرید نزدیک 70 میلیون یوروهزینه‌کنه. پرز با دریافت این مبلغ بال در میاره و قطعا ستاره جوان تیمش رو میفروشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24364" target="_blank">📅 13:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24363">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuJ3fm94HdGH9ujSR4Y2W4aCYVCI-PiX745MUPn4lgX3PiB67xBhMDhSCU8dN8znpwBJdvoJLY7nEUcTyC8_ehhgcCxndki2IthFA3Cu99-VqkUVGakaj9mkPgYrrHCO7H89PH5F0aottjurR3p9LO93jguhKsKPwVbe6DXeTBdzO5pKzeZx314Aza580VueXBdP5mq96-CnkEkajZKo7PXd5Qs-cX2-7-Tst0CsjjxW8hCeNxXiS7xd3LC4qXWRdAhJp1Pyeb16N5SaScnF610lRiZQV7ze029KLEVpkHdLM4wBhpHju4OT3n2wNrkmoESu2dccdOcF9VynOvHidQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24363" target="_blank">📅 12:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24362">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDdL9Hw8necxcJRQZuxhims0Eqa5K5GY1j52MsQf67kBeF5xta5quSPfoEfTnBhVpHVFAY2Hwl4QXuixPNOhzTCrGX-rJOK20ynid-YUkzIPQ0t2OvIxtIi_hxFBhbnAdUztJ0ljvVh4qE9C39Z6j9lPhoeq8B_glgUVXfuYH_oR3DR_fOZ6gD-R9pO6_-I3UsgCRZ6oWqmzUfdjN2DT0ovWKS3BTIqb788b_asWeMC_JPtfjjMfOX6cd_yj_xK9xjWbQPKNatvVK5B9Wfhe2PqLP0EEfN1mZ9K2ggabXMRh394XFc85fOcTKvR_Mv6-oM8LZn_tqLwg6Hyu_2oHTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب‌احتمالی‌پرسپولیس برای دیدار امروز برابر چادرملو اردکان در تورنمنت سهمیه آسیایی؛ 18:45
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24362" target="_blank">📅 12:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24361">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kblcapgt5ya3Ke4tHn-Bm0Ayxomd16-sChbqSNUmSKvVH4rhMh8FCEIUMwZdXe5aYN_dVZ2-PrNLNX11IeepsLQxjtmgW0o_-OXGEhuM_8cZy3uKjASFO1gLERIMHISrOfgz3g91ioDX_6rMgb8SW2V0bWPsTlDCVLz5e1kMFvWm-a4RWSPI8DAoK2kDhcgTyDTWIu2zcCddmpJf0_fEVmUU4BDOfLnFZmYSrgcV2IVVNLf2xC7FJOAKyXm2_yp-nI_rVgsbgYk2jLmk7SZeHi7XXrl5-yYKRHM4cYuCI7c0_porvcsqgbkEej6HBc3OQ22lvq0L02zsCtEtz-PrdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون درآستانه‌دیدار فرداصب با مصر بیانیه داده و گفته‌رژه‌همجنسگراها قبل بازی رنگ پرچم کرنر و پرچم‌های بین تماشاگرا و هرچیزی که مختص این موضوعه به ما ربطی نداره و به اجبار فیفاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24361" target="_blank">📅 12:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24360">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b03de0d7d.mp4?token=EstamQ87AQEH2ETG4PU7dlReMwy_WGfq4RquiXkG_LZ8RL9Eyf26SzP0GnQ-MsJLs0H_E4rW-4pV-ETWz4ySi5QTdnvfXT13GT3U3p7uljknkEcZP7IMrwyL93oUpGQF2-znHDs-7am_5nKZOdfKS3Y7SP2DtFG9ngFoFxJjJDggpqO0SjQNZg9g7tE-p_9c4GK-i_a7Cl5TkCDbo5r9ZoTlYqJixppn2cUjIy3yyY6c3iSObSSqGTZpgT-dVSaQgMctDogFq2jmGxJbz92OK21Y4gbdYvYNdqb3puZ7hsXs5_oe1fZ-bVqQYyE9W8jCvohLRF3r7zfGINy2FPBmDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b03de0d7d.mp4?token=EstamQ87AQEH2ETG4PU7dlReMwy_WGfq4RquiXkG_LZ8RL9Eyf26SzP0GnQ-MsJLs0H_E4rW-4pV-ETWz4ySi5QTdnvfXT13GT3U3p7uljknkEcZP7IMrwyL93oUpGQF2-znHDs-7am_5nKZOdfKS3Y7SP2DtFG9ngFoFxJjJDggpqO0SjQNZg9g7tE-p_9c4GK-i_a7Cl5TkCDbo5r9ZoTlYqJixppn2cUjIy3yyY6c3iSObSSqGTZpgT-dVSaQgMctDogFq2jmGxJbz92OK21Y4gbdYvYNdqb3puZ7hsXs5_oe1fZ-bVqQYyE9W8jCvohLRF3r7zfGINy2FPBmDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌هایی‌که‌کمترین‌درصدمالکیت رو درتمام تاریخ جام‌جهانی داشتن رو ببینید باحضور افتخاری ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24360" target="_blank">📅 12:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24359">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXLgb3DMDvByHJs-itrkDOqxIVCvhHP0uKepnAmFA9-oKqYikZ-YJcfqNjei3Nc5XjQA7saimPU2TI4UISBhiKy9XjSb4Sw2kvr1bq2n6iB2gJ4jdB6GGHHBMfZmbLGynyhon_X5frqnVpvGgj3JoqSeWcbOcoVwMvJT_43OqDymc5eisnAr5feInQ4gsgb8Ya5Wtx0WmUcfYDX9ee-tiLh0Y142IkXgRzPjRFH9HKjWBcygHVoM1ENZ2_I_CYBqvF6DDjuw3qd7XTxh3aIYfHJgEIE7FFEqxXq8nBdrWtObEOpyKJ52tB7ccoD4flNCcb_SwrRwufmVNrA4PfhuCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخبار مثبت 18 و جذاب جام جهانی رو در پرشیانا آنلاین میزاریم. اونایی که جنبش رو دارند اونجا هم جوین‌باشند. ادمیناپست‌های خوبی میزنن.
🫦
🫦
🔘
@Persiana_Pluss
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24359" target="_blank">📅 12:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24358">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFSTRw14HBe2yRDhwqL7lmuNFowEUlfN26j92DloHCO3HLO3iAe_c_rn2zaAuOVujiDAR8gtXY1X1C4nKM-snIRVY3BLw3_zc8IAGn0yzt3ZbMxoRgS1MmajopZBLkDcFJzVR21C1jpXG3Vwm2Jh9T7fa8Uw-b0P04rjPIfiIrEGkNkoZTn075LE7Q9ad_8Xd9FTr9GLblYeGHGjQHxq_RwvOG3JwioqlVWIJL6IJYT0-2pcEu841Bt7-lXNomHVZCPrp3wql_pNbAi0FcEYMOLsiyzDadimIJzEok8wQXv-XR4tmeT5mKT35N4zmXYBWI8sY0UfCPEETkTUqu5a8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تونی کروس: دراوج‌فوتبالم و درسن 34 سالگی خداحافظی کردم تامردم روزهای درخشانم رو از یاد نبرند. موندن نویر درفوتبال درسن40 سالگی نه تنها هیچ کمکی به تیمش نخواهد کرد بلکه باعث خواهد شد که مردم روزهای درخشانش رو از یاد ببرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24358" target="_blank">📅 11:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24357">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCOVETTm9zpqpSSjuhVfj5XvW5x_hJc1pMBAB-ookHpBk2w9jGtSAyAQFlFDxANjEmys-buM90WW3o_eFoasHaDuWtj9P1UF2VDUp55qdFBmbT1jtqwB441R3PK3Jie4sSBdHrhdpkMGvE8-CsYsZIZ76dN86sTtwo722llby6t03VblotkV9jIIIEl9INJwMdlZuCnwXvXXc2pqiJjbzkF_MQK9ZHcG4ZncqpNBd7hDInAt_O7eF9PBcNBnYnonOxUYdamJcaeqTOYpLEdI0g7nF7aJ2UkJRnkIO0A2jEQz3molXFBcv-ZSBIorggSdX1y_pJkVvo4yVpMQI3xMwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الانگا بعدازمساوی‌سوئد باژاپن خیلی‌ناراحت بود و فکر میکرد صعود نمیکنن. بعد از بازی رفتن باهاش صحبت کردن گفتن آروم باش، صعود می‌کنیم. پاترم توکنفرانس گفت بهش گفته بودیم مساوی هم کافیه ولی یادش نبوده. بهرحال‌الان می‌دونه و خوشحاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24357" target="_blank">📅 11:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24356">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhos05ggYtvGM6SRnRfQs4TGYDB0eM2rDFDcLWYTo4zomcxxDnWDJCMJZbwElQ8FdPF0_MzH6Pzh5xYU_eejlkwQKQYmnzKMovVHtg8KV6wSPseF205vACmeryLSsfNhZIyQjs7_LUlE1QGzy0ahyJLk1y5fHMm787nxHymHBL2RqqvRkxHCtm6UAaJm-yrz_gxz2AkjmBiFb-k5s_PXONUu9aB4nzbqxlMglON5OaaNP2CVix3krZ4LAB2Gm6splFNKCw5jxcrLDqzpWXygDeXGaCW5keuCbQ3vY1RvJ0BxYdQsuuOzu-HTseJKheVYKK-xNIaUBTIGp6ziNxa90A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
ستارگان رئال مادرید؛ وینیسیوس، امباپه و بلینگهام در این جام‌جهانی در اوج آمادگی بوده اند و ۶ مورد از ۷ جایزه بهترین بازیکن زمین را برده اند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24356" target="_blank">📅 11:06 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
