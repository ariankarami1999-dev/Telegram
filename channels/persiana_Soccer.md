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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 16:19:14</div>
<hr>

<div class="tg-post" id="msg-24466">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7vx4BE_YWhYp-qqyioLFeqUj8GgJCHUy_YzzeyIdlxCl3ZsQEV7kMmCvlU-K-XEcszK6uiWeAdEVQ50SZFZ8Op7L-NZmOp2pOQvYSFd7RytCABrnmpJjHXskgXj6NTlcxeU6Up9moMsLme2tJDn2qJ23L7-x6dImAl-cTR-H69wGspkiwrS43T9L20EYvogwCTN2j9Rb1ylInsvN22EN4j5YvVAg3imdOZqqbbWHTtCeI0rkQXniQUme5F5P2z-hmpT7NbAnIzwOMIlN8yIxcZAiQCIWCKEeM_uwRQM6lD3baFHYAqer08ZEvFO0C-fgchhbIzUUWh0RJ_AS8HA1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جان سینا اسطوره کشتی کج جهان:
ظرف روز های آینده برای امضای یک قرارداد اسپانسرینگ مهم با همسرم به ایران و شهر زیبای شیراز سفر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/persiana_Soccer/24466" target="_blank">📅 16:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24465">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKk7FD0gwumuwarwtXGYgoh-OyNcOKDM8CVOzSJDGtIqzSnznYLTVgNrbfAIcapfBSHqiQi35ojy1ZiSEy3IgwF-WMJdBaLtdHlw1IMysazewyfqibwOY0UGK8jsh8kXKmZmkwBVn-6cEUSTlByqtDtNcedPmkO_OmIfWq5d74jH6QQzmkI2cvT2lBl9e2hkfU-3ung5oIWuKbfccGnVQSC-ngi6ASblBZXwT1t76rEi3P92hjPv-uCR4GJvSqDjrwSvo2fRfnPCeNdsdWBVn0GuMgVwhu0FEmhCb6Jp_E7YkcYu2YUhghYtck3G20Nvqai5d8AbULWV3tB-UOfB2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌ برای‌دراگان‌اسکوچیچ بلیط گرفته و این‌سرمربی این‌هفته رسما وارد تهران میشه. قرارداد اسکوچیچ با تیم پرسپولیس دو ساله است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/24465" target="_blank">📅 15:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24464">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZhQR8zLAb06zPZjceI6rn8cGlFMcY-LZLJPltvns64eMiLa6cZOySGqzhnpcVOIazMSexACUAzWV2ZWdoKqMkxxXVWUlFUUNH3v1fy-nlZqZUYPd9wN9rnhlyuz32sKPJtRo13ZUnEeg0NIQ2NSLoY3jhCR4qHuATqxjJo0icH_YoBgpsXv4OZ_Wly7TAtdsy5EPTEdGa3Yl3FKxCBxrR7bA5c8T8khcIH0-lkkYDabrZfvLsOC5AauDWRmA8fzDziE2J9WLx7tTcr36JaV--P-JdYrbGYpdEV5szLCCBz1Iv3iK8caxnb_0o3pJiob2KIkx13_0UQ17YecLuxRDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی استاد خرابکارب در بازی‌ های بزرگ
: خراب کردن موقعیت مقابل پرتغال در جام جهانی 2018، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت های 2019 و تضعیف‌تیم‌مقابل ژاپن، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت‌های 2019 و تضعیف ایران مقابل ژاپن، خراب‌کردن موقعیت مقابل آمریکا درجام‌جهانی 2022 و عدم‌صعود ایران به دور بعد، گرفتن کارت‌قرمزجلوی‌تیم سوریه و خراب کردن موقعیت ها مقابل قطر در جام ملت های 2023، قرار گرفتن باسن مبارک مهدی طارمی در خط آفساید و مردود شدن گلش مقابل بلژیک در جام جهانی 2026، خراب کردن پنالتی مقابل مصر در جام جهانی 2026 و کشاندن ایران به اما و اگر برای صعود به دور بعد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/24464" target="_blank">📅 15:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24463">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNTX46FQeGlwsJtCe-1cxbVYYqrDvHmc3yjZe87upnD-_IKDz2SGhP4QucuhxOlBXklAEk3EqxDX-2svTlJU0cOmMK1zhRKBCaPb4JgkbNWH-OmVGRPYbXuUinbCayZeUCnK8bVC_K4nLepn7LvTenlOkfkDAXYwjCv7N7CeMRbYU5lJDcBv2I7xqio9q-a0IF6xfgithKiklkPQxbFGBYU8SSp-sySonC4RZfdrOaRTrsZR8Jhh599zcnVjb-YfpkmUONpFHgK803u3B85Ll7zbjHdfpsgPqYEkrytbaRoduYclDvCpHhxA25BSdxH9F2zEjG_I2020TpQK40pc4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/24463" target="_blank">📅 15:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24462">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/24462" target="_blank">📅 15:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24461">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/24461" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24460">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/24460" target="_blank">📅 14:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24459">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVr-5_FidoL4XTdfSURIEHAXtTbSbYGj8vYv6t_GoZp_7gMwTQJXVYiPSxEZcbrq-jbhENGZIy5hf8G20fG0gPC2KcwcVDcdMMErpgeBkLvAZkIFJMRZCaC8noID7lGl4F2Bplws1M2Suq4w-WpBbrLKKQ2k2eePiAEsB4KrYIdSkMJp7mgDIk5t6WHg-3VM5yH3-0ekTfmH9o_W081bKKjVoaJR2yb6bf_hRgUnkOm8V2PpEEoSQsDoXtf0p4VvBaKEh--QUJ7Gf4jkpWB0_3GEOr6eADylQDzJaUFAYLkq7mrFFAoJOnPf7OXkl5Fp6o1p6Pr_A4G6lHqnf2833g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/24459" target="_blank">📅 14:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24458">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l41HJhKF6LnPSmcNwFJ0-rOUKYZeABfHDFoJU0PB_j7rtVEV3v0LOsO4i8QKgXh7w1UEf7iMsh0dkvRU-xxkT8roY7kNQTMtRCOji51F6qpPXjz8b2-5cjI4Q3whTGaaGnRIc0uq15nzmwTj4Feh64ALoDvwIjNMngYBL46X68FhbhanNC7A__jMMxwlFOPJJTzMaphNBv2MzTWOM1MreHMSk5j7vWLBWUfv5qAmq2j07rho0EsH29QIRpXCn3f_QvTaPSjFeiWenM9sc6v8yynv1FxrcYzzXMqUZwPhF3WUipJEx9q6hTVY1Q-1lh0yKi5Gm_pDs9iRCyQrVqZy_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برونا مندونسا مدل ترنس اعلام‌کرده که تقریباً دو سال رابطه پنهانی با یک بازیکن سابق تیم ملی برزیل داشته و اون‌هم برای رازداری 100 هزار دلار دریافت کرده که البته گفته بدلیل علاقه‌مم بوده این رازداری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/24458" target="_blank">📅 14:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24457">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/24457" target="_blank">📅 13:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24456">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVsEgcskMcZjVj4q8HerJRkiras4qcDmPj9NS5Wuxl4XtF1ntM7LskFvl7VzCoGnLm9OyPyl85igB6qjwfWfgxnSOCdIDz9d1wK7NDMVi5zZdGDq-B99lTGA3UXcBadsSbjnyMEm1xqudoLOV9UvSE4NxyNp02ZGWPqHYQ3lny7UmvWcFpSPGYZ6DlCkxK7cpY9tKbPQ-3IkJ9Z482kenuXrfK1XMRlDsM-q2ZdDij0asSKIy51v-cGtg4P7Ihf5oZnieZzKAKmWDhNbwCOSGiBZt5_Xd2xP8ouToYQwM86PSpAKJ2B31mi8VeLIiPFfcuTQw6WfaWe0W01fmzGPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/24456" target="_blank">📅 13:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24455">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUtu09Gcvr-XXvECxIY5S-qu9iT-cCQwvpzNAmeLaCyn1y5FsZJ5WXIM_EyX92xNh74cInSG8U4MhP41miiCvC54OnXLKbNim1mlJxX-Hdb97qqqmperGF7lPgZv3p5QYWhDJj7nQwUzNotz8DYdM815KAW3mAWZaq75rgu-uYgr90r8cy4Vq31XLb9uzr8JC9Hbvkv_EVJxR-Y2Ocyv3IWvSAS5k_zOjNSz1E70T5VBv9ipDmnbfe-SMixOF2TEp1JFt7JzYn8_cOGMBRthARYfSph3NNNWp4rvJcT7p9KwhQq-cVdi_RrM8sYzkDZKIf2Dff_u9m6_uYEAGMNH_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/24455" target="_blank">📅 13:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24454">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qR9mMzi5qSaLMF9PdUiTmG2xTlr02eF5B7kbAd7v_XtQQDGFCtYlRd2EPz_KKSj9cC2oZZth7PnxvbVpQmq6hE5I9bifZCDPEQIbhuAxvgC5OKsVAaDQS-pPmuwjPZux_rc8NR1sxMwvLVzxteuKtCUlfLrRnRuef-l4xOM0ScSoWRx9Xvfb7P3WXjX0Eu3baH4x7nJYF_-OzogmCbCbgZ47oPmOlAJqNIOvIJ0bHaCNKBmBMudIL-LDLWALk0TjHoG4wakxxw_Ehf27x962ImXTqpmzPnZFZ-lL2kKHvnebMOOaNgElLVmRChhoDLU2e36msKycDuoLkugad64REg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/24454" target="_blank">📅 12:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24453">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_GciaDBWBF8yKnGLqJ0LEDxlHCMu228rqShXe6QDcvos5CIXZEzHnIPhaVdoxk5v3DywkYpEqPXZGq_2QXWHSzBsZWdjL6u0v2Ie4EcGH1gJGOl2vYWQ0OspvGEPJvOUdt5MMLToQPGl5FGB5U3Yq0otx2sA_3cdZu95h6tRk4E7jhAJEJ3s3PRcVI8xdNDayBQwhV6Yjcbmp-Ad6bR45kpCN1t1gOd5zYh3cdwKUETqQ83t85dR1KyEgR9-uJEfwjA36u1IWMtr-sBn5TVIaqUmy1GJONHQVBf1-_sY_MJ3ViuV38_-UfILweKAiFg5psaDdvskhB-dJGXbPVfLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ ابوالفضل رزاق‌پور مدافع چپ 27 ساله فولاد خوزستان درآستانه‌جدایی از این تیم قرار گرفته است. همانطور که پیش‌تر نیز خبر دادیم رزاق پور مدنظر باشگاه پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/24453" target="_blank">📅 12:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24452">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvd_VYhXptc6rOMRBFaERu_fG2iTvM7R1mFSGNDrt1ttj7yGai7mPoS62P6k2qz1swxBUPTkiCVvoSiUeE7nZe1StlK_b-JMJH0aNbLhcLm0PnDJQZDiVEYl2ToR5BZSw6dQUd9p275fTlT6w8snfz1E9a4008s0Y9j8dI9C87xdrRZRg9oboTgn5XJx8seVjFvEeqlMH93Ugsk5TeRjzf8qyq46fvWvXVA7fLXDTkXjczz9rC54maXVc0r_AVWQzmzbGR__ThNa01EDBibsHZb79H_LpQBZCLzxqqj3RP0XMqJPWyT_GVFyRU5ZpWg0-Vi7Hatr_cQYoI8hXNr8_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عذرخواهی رامین‌رضاییان ستاره استقلال از مردم ایران بعدازتوقف‌مقابل مصر: شرمندتون شدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/24452" target="_blank">📅 12:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24450">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V12f2BdpS4D4FkCGuYkAIfXHRJC9WUdjZKHfM1OjuenfhIFNf72freQns5J31A53MrKpTLr8ZIMH8aUEsy6nqH8uBLLNsOPAVOPPpOuCGrRYuP2ik9622Xv6rrOMH2Ei4c2KwKAEjpCIWHN6WWVub7zAPGmChcUQZ3XzUFvTDENKFcyrPlM1BIEIxrnRXc0mbrDuhTnDIqYpCrxIJl19tKVATRLzNyxsjO1ZLsfdw5yoYGflEAeMqmuzSTayNpJZKfPfoWBFtoZS6V_jkld-x8nbRXOm_t4wKaRNZSJeiw9_bv8pgtTb8NFLSeqbT9DTepXb1s2pB-s5HeMMcrGlEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/thm8BtiyZ1Ud2gxucbnx8coPNxl9DLJlv_zKnLd7KWu-F8k0UWH1ngBm5uVf3wdWg2_eB1EEs7aAjZz7mJ8QzxDwQLFX4rpw6UrpDptLAAedmeuJdefVenTYEa1XtFze-OIUR12Ax__vM1FmclB0vd8v7DU7KlVWhYcC-T9_AJ86nWg2kXzlQRhUqRukh9HNjr9MVSTbSSye04VRnl9tMyOFGXKgrzca2kUI6fgv_GT6X3C2kRJFzKfXjN76uU2DCKgkurQ20WAdrGHES03rMNbpNWIbu-HhnYmaOevWKmiMMu7aQLyxKlyslr8VhGcenckFefHpwXmYJL351pg4gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
پارتنر برخی‌ازبازیکنان‌تیم‌ملی‌برزیل؛ جالبه بدونید کارولین لیما با نیمار جورنیور و ادر میلیتائو هم بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/24450" target="_blank">📅 11:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24449">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B41mGB3Kc_RcDu0b0y8ujwIPdm-uIperSWRGY6pWXc7eY7nWQZTvVMfKibLCg6hxJEhwN_AUT4CsQkOBbtccnxeMdYStcn1xs1fr9Ux1A8BVD0hY-Meaa0e6RgChhc342I8uEVEuL1_leirTUINCL6RMdEAmD6AHGwLQ9HiQcEWEOc8C3woT65tMYGuvKBkiwOiREdIrTvQgsxpONY0a687E-kSfSHEDyVwqgS64S1IA3J9t1uinBFg6pRTNKXUKk4eCpr2sihO_OTx79rX_3q4fk73VHBUYTnOLJhjWTk3rsafbPLCTVeFHsRKgQI6coZoAdD-TI_q9WP90mLljxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی رسانه پرشیانا؛ با اعلام پیمان حدادی مدیرعامل باشگاه پرسپولیس اوسمار ویرا رسما از جمع سرخپوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/24449" target="_blank">📅 11:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24448">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-gP1YFiFvj0wgAFEXw0aZJNuKCE7hRE-JjTxd0vffue5qz7pqVuf54TzuOiBKoE4p9FBdhAv7aXyCXrIqSou38s5a3hz7KK1jDr5RCtPTIFC4_FlB0fXSHy7gOsS9WIInzugpbc5yA0eoO1L7EIYCedCeuOWrnixDbPCP3KvF524x0rIMyaurcdpzbZk8z12ONbL0q4UAmxxgEkVB1VwzQDk8lDkIE2VUTAVbrwEIDurUUp7wpgqY0nLoX2A4Zy1GjR9vjfhzGbl7Q1KX6lhJCtVLrXO_Z3EAMx45zF8-iUwQU9yTXkb_Jd2XEA95BNX_ncnFLLIkbU63D9HykhEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
#تکمیلی؛یوسف مزرعه ستاره‌جوان فولاد به مدیران این تیم اعلام‌کرده که از استقلال آفر رسمی دریافت‌کرده و نمیخواد این‌فرصت‌رو از دست بده و ازباشگاه‌خواسته با فروش او به آبی‌ها موافقت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24448" target="_blank">📅 10:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24447">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=ruXP6QwfzosqaBYtY1LCeP3wGc9m0qkkffoMYEDmZmKIR-M1GWghX31UkRbCgn_OmKEPtMkqbMaewIg80iZy0ICcSGawkEVEpwzvu5zN4SfRNhip9n6CBxZyg3WD_8itMAWesF1NSu6-UZd6D7MuNF-eWAE41VQ_frwtCZGpkNtESseY7ySkupJO2PB1gsq4BK0Y9LhF74eW06ThfDGb4TuUNMBQvklK2Swu6ivTuLDYI4HJm_B7PIVLfWF_caqT0Du-U4T3km3mcIZlyICFWzewSVg3G-yqn44ofskGcJuBPOyghGXLgDD5__FtIjXQHIeSivW3twGln1FDE9Jo-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=ruXP6QwfzosqaBYtY1LCeP3wGc9m0qkkffoMYEDmZmKIR-M1GWghX31UkRbCgn_OmKEPtMkqbMaewIg80iZy0ICcSGawkEVEpwzvu5zN4SfRNhip9n6CBxZyg3WD_8itMAWesF1NSu6-UZd6D7MuNF-eWAE41VQ_frwtCZGpkNtESseY7ySkupJO2PB1gsq4BK0Y9LhF74eW06ThfDGb4TuUNMBQvklK2Swu6ivTuLDYI4HJm_B7PIVLfWF_caqT0Du-U4T3km3mcIZlyICFWzewSVg3G-yqn44ofskGcJuBPOyghGXLgDD5__FtIjXQHIeSivW3twGln1FDE9Jo-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای جوادخیابانی‌ و پژمان‌راهبر در ویژه برنامه زنده جام جهانی؛ حالا شماها دعواتون رو بکنید ما که میدونیم همش فیلمه که برنامتون بیشتر دیده بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24447" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24446">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=E6K0i-nAfZFlhw5NtmrJMa4DO8u5FkkfMsD24r4IDyN3xGgkyp3g2YuyceVCVSGYAht9Icek2HZA0k16ubOk8EAba2ny05L3jaoh1E68Zoo_CwEvpcv5_AVGx20gC8wH_GQE44hF2eOqVjensenRVkbDh-C8ljsCn0LR4c7B1vpvCnZCGPj8Oqd4it-Rli8Bjas4TcAN6ox8y-2wM53RYiyQsE3SDuOv68m9efn9mdVG54GDOIWNBnlZKrJw_ZwbdXvzcCW44tG6OuJwmK0pv1Kp37SFiMGjQ8FMkdJnefJWGflN_dTvkIJEyDthmxkMcKXikf0ql9Z0Mb8uzXh8aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=E6K0i-nAfZFlhw5NtmrJMa4DO8u5FkkfMsD24r4IDyN3xGgkyp3g2YuyceVCVSGYAht9Icek2HZA0k16ubOk8EAba2ny05L3jaoh1E68Zoo_CwEvpcv5_AVGx20gC8wH_GQE44hF2eOqVjensenRVkbDh-C8ljsCn0LR4c7B1vpvCnZCGPj8Oqd4it-Rli8Bjas4TcAN6ox8y-2wM53RYiyQsE3SDuOv68m9efn9mdVG54GDOIWNBnlZKrJw_ZwbdXvzcCW44tG6OuJwmK0pv1Kp37SFiMGjQ8FMkdJnefJWGflN_dTvkIJEyDthmxkMcKXikf0ql9Z0Mb8uzXh8aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
رامین رضاییان بعنوان‌بهترین‌بازیکن دیدار امروز ایران - مصر انتخاب شد؛ رامین رضاییان نه‌تنها اولین فوتبالیست ایرانی‌ست که در دو جام جهانی گل زده، اولین سه‌گلهٔ ایران در تاریخ جام‌های جهانی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24446" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24445">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/24445" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24444">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_V3YceXbGAM0v0aXqm1KzXLZwW-S7oYD9algK7P6KH79pPTZwBWpF_RLRDFB_kBxuBz33ah7HdogZDBAcDGTsNbI-nnwGFekZQUBfyYzYcOsbdIGJDf0WZP59eibyu0UDMq01bHf2IKwme7vkE7J7u0GSBASKb7mw5_dTlcoR9xV78t-uo4s8NY4-zardFC6AEkt7OUsQqD9EJZwGcG8EixsfIoLMcYNxiR8VhHlpsPW253655gNv7NKUf-h1rEYc9THBOCdW68YA0K_ZuNXHHWguCWOdcVmmwuRKKJY4_i06Wvpv-GF3-uPKVukumNpDroWxvoaGZk9Jiyhsrt_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24444" target="_blank">📅 10:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24443">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWCPrDrMzlnNd1J7RXDliW_M7dZik636rgxceQ4-6oIipsIHY_mce3g_xYAdiCpb5oN03FmXFAzGSyG_b1smCSSi-Qa42Z2AHCnbv8_kMd0k5q1UvBEpOKlgMxTJaZEdvV3sxM1GH3-huC_SqjXe74pqEs2_J6jx1rxq2zffONTZrKsxSwPOpxU8mFzMweHpa_ETUYTpQds0VCIbNh0pepE0wFRbztzQ6W53rdIHDKwiXmsxNAtLvHroG3i3jCiiCKsqFgbvpu1E8gvsuw7gWsOxdtq3hb8u9-gFvndLb_WMm3qqInps4nRpd_rtqRa4twijk-LMBB51-wbfImgwpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ همان طور که سه روز پیش خبر دادیم؛ دراگان اسکوچیج سرمربی‌فصل آینده باشگاه پرسپولیس خواهد بود و به زودی برای انجام مراسم رونمایی به تهران‌خواهدآمد. اسکوچیچ پیش قرارداد داخلی خود را با سرخپوشان پایتخت امضا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24443" target="_blank">📅 09:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24442">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=U6z5saCjFHR6glbEuXFmN_o4hi_PjqeDgSDdgQSHPW1lrx20LYoWOqqCWwzdcDQymL0yPjr5WW__Q_6reGHDouCkfZKSxna9cbaIQFRUHDQm9rEuUZFkGKdvwgi3F9xJI8AWSzUa9Z62Ot3vY9QxzxWfieSULoroKnd9TOLxwa5nlh9GJRtAva1KOH9tqhwHSj-f5UPLgbfdrj8F1vjy-GrdooSkhFWKIYcTyfk7-zhaUlTgBGXMNRJP_UOjhKMoC3_Gn7C5M_mP6jK6WkGCRP5ZFx7OQrwe9Wp2OnwGAySBXMxIdz7mo_DtBf40n0nQHYU87oPrwGnbkKUjSGCcVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=U6z5saCjFHR6glbEuXFmN_o4hi_PjqeDgSDdgQSHPW1lrx20LYoWOqqCWwzdcDQymL0yPjr5WW__Q_6reGHDouCkfZKSxna9cbaIQFRUHDQm9rEuUZFkGKdvwgi3F9xJI8AWSzUa9Z62Ot3vY9QxzxWfieSULoroKnd9TOLxwa5nlh9GJRtAva1KOH9tqhwHSj-f5UPLgbfdrj8F1vjy-GrdooSkhFWKIYcTyfk7-zhaUlTgBGXMNRJP_UOjhKMoC3_Gn7C5M_mP6jK6WkGCRP5ZFx7OQrwe9Wp2OnwGAySBXMxIdz7mo_DtBf40n0nQHYU87oPrwGnbkKUjSGCcVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
امیر رولکس‌ازحرکت‌جدیدومخصوصش رونمایی کرد؛ اینبار دیگه فکر‌کنم گفت خودم که نمیفهمم چی میگم، اینام نمیفهمن ولش‌کنم بهتره، مسخرم نمیکنن. ضمن اینکه ژنرال درسه بازی‌جام‌جهانی روی نیمکت ایران شکست‌ناپذیرماند. رکوردی تاریخی برای او!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24442" target="_blank">📅 09:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24441">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24441" target="_blank">📅 09:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24440">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24440" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24439">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxXGRvLH8Snbgjd5mgOJVwonQH-f6_harj3PiecHDUsD9UjLLN5yThw3qkuTo9ZSYMKfma8tDPQOGM5YYMlMae4p92A-7mY2O1SSuOcPydKL0X-rl6K1zdM0yzZZY7aRSskwnTkOgNZ6KppQxqf46PuGVVD_4onzv6WHV-gu4Mp25RX6XoiNa4GDObUs258kDVsAP7AF0RXza55OfkNAIF8Ly8pzwrBRCmsngITqlAvE0VjmCF-YjwBrvsemM77cgejGvLZR7OUjMcufdbXhlsf8hw0InPWrvm8mRjsx1vyK1LR6L4fG4weVa2Fep6Ff4-lGC5ggoL7ZRn-8m8jSfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24439" target="_blank">📅 09:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24437">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24437" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24436">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbPTWvcQ3H2SQsQ6SZkZgURWQCZDOe_sEXTV7pXDNejxjuVfovlxzkfaFv_wKlvGM0MOUMZ6aGKging7WlOSxAT6xUCYXRtf4p21CpgQUedE6F2yipz4EIkaVIuawLIMLfOjTcoFIdQ4HSJj-swM8ukdHBuOoxG6FTdn5f4n7sQC5zOdM3HbfQ7SsIL7XSb2w2p4nQBtsVpIfOweB2vL-pTVVb0wI4KQYeGnAo5VOA_YbcZSOoX2MvgyzXGoXlthwLD4TK-51WpQYW40NafgfO26MsyJrlki9Yi3x_3XJuUI7fZ_RovEXlxt3pk93ljhZdNwoOuSpapqV3KY7Qopwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول برترین تیم‌های سوم جام جهانی؛ شاگردان امیر قلعه نویی در رتبه ششم قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24436" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24435">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJJH6goyXjy6R9jZ3yBDy_xo8msXxmaqdexRl7xg3rICQQnCDGiohZblZFIPeN6mYbZ10rqra9Sxrk7RobvZgKbxk4J0xJKg4SxMdy4d27tWTmjmp1Omvcsaf84Vtm5I12c0bJhq1qdlsZ611AShhk3iYIaLJ73q5TRBUfeuXrFbcRwjJntnR8FsGjIF3FynMqyaHOTj0FtDRjJfm7cLMcMONp5HwzreHUe596-YrzZMnjVpTCny1x2yYec-Rlv3bEjtbsMw8JiYrp-5UGVHMb8OXnV4x14Cs4jkWoHwiUPx8xH9LZFM0vMIeYgNvWicTXHe7hB3e7lsJXE7txuBlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته سوم جام جهانی 2026؛ مصر و بلژیک مقتدرانه راهی مرحله حذفی شدند. کار صعود ایران به مرحله بعدی به اما و اگر کشیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24435" target="_blank">📅 08:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24433">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzbT6Tk2ayTABkq_Wz2sGXnKdTdVY_87WOfL20Ojlqotz6Ar0oaVPqjuIdfNFXVnu6jDfMMkh8bXGTfun0_0xE1dDzq6i9OIDWoaitQWYN2yO7fg_sk06SeHoZ8bj2LSrqx9fJ27L0w1yGa4fVwhM4LK0clv36Fu2yETylR_p1WkdoozNLgOZOz7cQEzwfPSr-rEE4y9JirtMxMzS719Hju4z8L33sS3awE1QHLBvc3yxf8sILuH_S1Va9aMa5Okva-dQcbUUwxSJ_pnbsnSYSjqdCBMhS1FSMuEpeBCri02Rb3J42vxyO-aKW3U_y-vK4qVuORuiHBA0rVIC9D3Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DeElx7aN0rc5SloSe0hFJlGMVJuSTZmT59GoeUx6THAhJSY7BA_13RXwAi5glW5_YV-Dd-rKvf9xZGrwGcXe-LXofJkp62xtELnSl3L0VYIz2RiBbqPIluCByCwNy7EpWPp4d1DuaU9CSd1ILATJLAl5QyyfdJ7-bNlknMwKUsIMYS-e8zWO4NQVm3CPJ5tPcgu3VNxULHapNkGSeviJmbeUVul2SxB2I6NULIezzBPBZYPZU03PN8pxG4Orsw0kUcyk78q-XIn_2MzqEsjhP0DOsN-uIH24Dl2AqMA1oRjHKifvH6WiNP59ZPPVQo_oYJ0w8zvWFpaFY3pOaV2wAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24433" target="_blank">📅 08:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24429">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwTVhMiKYofUrKnlTNb98vPqlSkxNDal1bvrw7u9AUsoWDAzd83MZMIw1VVApbSLyO-o9henudaRbXHeNN0CsYbXxbIpfQMPAALpk9gsCdsQXxc--upwP1ABMB5NL4vmNg7yYmuswFIOrHzK3m03MwmmMxudNYvHLwarwDVEfCopVYhPEZrnpjavLELW8uYDVEGGzkxfefdR-HaxJwd4_qhsV5xV0XdIgqxx0EIMVia_4VaTorvTDHV5lKp44d9L4mBmMa6wgFxKT4s7b3OdPyLxfJTarEs5PR_m7R2sFioyBmyM0ssYLdpeCqRGcNnUg0SFpZMBi9b66hiBU1s_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛ از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24429" target="_blank">📅 05:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24428">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVjTH4lAS_MZm1ghiMkdw8DKjiWiJVXQ-RnAWYEZ3fn4D0O78WfFUhFHk4A-DEVua70gdD7La9hEhaRV8drZmHjN9U8FoU8zmg36dSL4ToAl6WmjrmSR-zoRFJbJxGUfwuR4SoHXiklBMDkrKOdknJDTJgProBS25jTpkgJV7vrTNH9ZuxZGO8qgyJiOX4LeWciYskw_fI3j_5pcBYENIwsNCGrUH2qnNDLj6rwG8u2WEfXyc7nSjYnvySAi_96KuUQsWh6vSWrdlRxQyjSru2ZqUUta-c3BZ0y5EhEhuYuimdy7xrQEfleFQyz7-x3LFrKdvkFx6dsF7Lo52dSlAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24428" target="_blank">📅 05:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24426">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O1uJw8l4yODDIVpYehAUbLN1YWhVnj42aSVZLBIdsUkXqDzBLwMTOcxjTpTmfKM3Q3W4CL3Nv9iD1_0033dji1e2u3Y_Jh3K_G-X-YvpG3Njb4ryaGF6xIVyzkLgawNbic2c6YeuPg-nfLc3KLDMrUi2HFphWqg-8Ftc412BVrnrwrCQiLrHgL86gPab9zs2F1doRi1MkHrL7i3AeIlg7Uj1djesKydumdxJxAwjvoVk85wyP2Rt-47h9Zh4vgw2Be7Q1qu_-5MI4TvKj1Nvni9sB39Ny-QQ4P7-TvNkbHg0Zxf4U-ZJUlK982OdVivHqMjRiqO3uyKPQaYeirw1Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RelPq8vYmQ4NTzaQvBninuixSa0yX9VcNmpn_mxuQdMITFQa9n8oYhidNx_2xLIw02NPXjfEGlCVcvtFcveqLj1FUTyP83QoMiwZdNmWGUpTnbSCscySzEQthfCZ1XoSBz-mOL3NH82szLsf9cJv6I8458qKlr5QI8YmHuSpoXCTvnpqU-sP3ar2uH7P3JKYI5wL0p3B8g6yMRemMTCRJSwI2lAUUQtkcXG7Vja2CBI46KmZx2xe1GmwTb77AhM6jyxWWrisP4AT2y-WAbjXSedZYukJvMRPLPhQg5nFRgi9Op0dQhUxd36WMg9CVQbXW9ik0hZUYpR8yHZ0TLemoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇪🇬
عمر مرموش ستاره‌ تیم‌ملی مصر: ایران تیم خوبی داره بازی‌ های قبلیشون رو دیدیم اما ما اینجا هستیم که قاطعانه این‌بازیو ببریم و صدرنشین راهی مرحله بعد شویم. بنظرم بازی رو سه - هیچ میبریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24426" target="_blank">📅 05:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24425">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4HVPo3d4IfL61UK2ZeR1l6suOQfc3FVaJi56hjo4jEvDJ21ovvUuK-zpDKSUk69SOiUoHjgELHGzVxofax8L0qFK4jf03c8YPDQsLI_Z7ZZsbmbzNASSEQ4QObu67Zwm_RP2ouGLDyHhoUV7aeV2gfk-KWPrY27ew66_SPOpvrTsvA7cDE0ENPwmn0j0KEzQ4wH_BApNNM7jGV89ttphdHAcHJgKEKgALPWWcA96tsAGKolXNLstyXcW9n50fJjm7EFGSdjCGasnHmFRDJ1QWiCBS11kAGsoKYUUhZyKgt1zwm8ehzgK0BJUTiqXzIr_4MwJXXMWB6DQTapKtyVWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌‌های‌رسانه‌پرشیانا
؛ ابوالفضل جلالی از دو باشگاه اماراتی الشارجه و الوحده پیشنهاد دریافت کرده و درصورتی که مدیریت باشگاه استقلال برای تمدید قرارداد اقدام نکنند لژیونر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24425" target="_blank">📅 04:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24424">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEd8Ff4eC6XcCrFX1_oTzfdkdPSYvqpbA8kviTYfhLsrK5oGSXsIhPxfjbg_oEgzQ5r0wub1FpqwdY6ev6EXAH9GQC8UGVtaWyqNkTyQmf_mdV_Ubhh-jZyXA7com58ih-4QyP3N-hk2ZFt9jBddRKgUO3NP-DjDE5X_4ZH6QNe9JOdiSaUMrHJCKxcnUmh9T0N5DeqMLsPjpdW1i0vCYwTLbuwgbqcNHMoIfQFHq8SCZ55vSSKDNoclWh45Xjp6cFK6jMXOcoZIQIO_8djw7dCOJTN6v10j0JOjhVNozFjvkEyx0kGc2azRZFaX38sD18ALvALyTDh8IKxzmoMdkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24424" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24423">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e59cd1cdf5.mp4?token=L9b_biLFgo1tBln0nnlYA-jQYfMTiTfer1AS0W9tNgbR5q9jVIG3PNGsvYqhmPTeauAvKqFciw0aD7O2n_3tvJHLzFbr6w7tXwjMo2UIjGVl5HZhpIxCsOzk4Hyl0CEc66cIs094rvB_mFh488dCn4frCVW1BzjiUFGMh4RGY8h4GgFshySKoNXC1GU9IRrZqjau5S9PqDzVw98p3n3mDzWq_UcBrJ1gK0hWBxpZ2fBO8fwUIUr0WQKhOr3hPpsuAxW_GWigk-MMZxYxx6M7iKZpYgRl9eGfsMry2emLILkTTH2tTms98VVlcBGdxS4q46Irv8bMxh1QQQM7hZXj1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e59cd1cdf5.mp4?token=L9b_biLFgo1tBln0nnlYA-jQYfMTiTfer1AS0W9tNgbR5q9jVIG3PNGsvYqhmPTeauAvKqFciw0aD7O2n_3tvJHLzFbr6w7tXwjMo2UIjGVl5HZhpIxCsOzk4Hyl0CEc66cIs094rvB_mFh488dCn4frCVW1BzjiUFGMh4RGY8h4GgFshySKoNXC1GU9IRrZqjau5S9PqDzVw98p3n3mDzWq_UcBrJ1gK0hWBxpZ2fBO8fwUIUr0WQKhOr3hPpsuAxW_GWigk-MMZxYxx6M7iKZpYgRl9eGfsMry2emLILkTTH2tTms98VVlcBGdxS4q46Irv8bMxh1QQQM7hZXj1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
عارف غلامی بازیکن استقلال به این شکل جواب صحبت‌های مجری‌صداوسیما رو داد: آدم صندلی دزد از مفت بر هم مفت‌بر تره. اشاره به همون شعر شایع.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/24423" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24422">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUNMOVAjKJFPpz9CLPzspDZE2TidhB729TLGLqwvsywXuRL0cjcsZ7ybOC7zp2M8W3Dkrp6CMDG9sjtwOBfg-jrqZWhdTX8rlCwjdNRsqZkkByK06bcMS3Q0HDXeeGWdSf-6WNjqO1wUkpjPDA9-E4276-ckSnjiVQKOrQ-EcIU3Q_FN9qoDD626prLxzEr00we2QeLEHAWYVcaDMInofkTCyjv368QImCj9QVhHaSUALwIfzyme-Rk-ySiSh8oUmKs5D0bGJl-ICsGxzJFF2HtKaZNtfoX0S92MR2bRbLoSsTxHLhFINVeug3okZY0kuVTayg1HXSUTbAS64qXG7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/24422" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24421">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzjtjrlQmDnNjls3-e6K0oc8ViJwjouX-s333Yl_ClDjrICLDIP_UT3SW1JNGSKjlLY-0jz4_YKmvwBeTTZ5UF-rvN7XrHZVtO0NsOmJPjiMvvnGMfPzmOngLuayQPM7MCL8QLUm4Vbhknuwdj9HoXb61siGlbhy4mLDHpApOqub57I5WRdqTYMfGp_mvxVDVbOCBfNbi9zd04FQ_pUsazuN3-p3HmCtefWdyIUXPYpkF3lEVR0V3V3HAq82i-oR9CVOfYHOpsur8G1xzMKgFfAQmHuR5Gzco1zSXnM_hl7m-AoZB3WjNYYC44GvI1P3k7PyjBR-AvtMyU1_MJILMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24421" target="_blank">📅 02:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24420">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=HR4hjQwvDbRHIzbC0sZmkYUF3bRV5xNsWmNBDU9zSzhfKxG1yviUZuGUnPS-QNtprAwr0cwscw6QbAimH_jbr6HtHeOhrtVLykIloPGoMFZ3--I7JLgji6rh66_lYRg1LGAgUuiO0q8TBTF_WHIIWP40u8F5UeQ2lcU45Q1SRJDrlelNWV8CqQ7NG17MsULkzzlVyU-knQpmy7lXnyMHRj92ZhnjvtdG_mTh7DBsTn9W8rBID5EZB_GiZwmCtWqcT0t5x4t2TUW3Z2wLOAoG9ZOWNJDy0k5jximAQa6yTrs6Jpn8gpuQtyce9rhv1jlPnIskYdjWK387UrJCa0YIjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=HR4hjQwvDbRHIzbC0sZmkYUF3bRV5xNsWmNBDU9zSzhfKxG1yviUZuGUnPS-QNtprAwr0cwscw6QbAimH_jbr6HtHeOhrtVLykIloPGoMFZ3--I7JLgji6rh66_lYRg1LGAgUuiO0q8TBTF_WHIIWP40u8F5UeQ2lcU45Q1SRJDrlelNWV8CqQ7NG17MsULkzzlVyU-knQpmy7lXnyMHRj92ZhnjvtdG_mTh7DBsTn9W8rBID5EZB_GiZwmCtWqcT0t5x4t2TUW3Z2wLOAoG9ZOWNJDy0k5jximAQa6yTrs6Jpn8gpuQtyce9rhv1jlPnIskYdjWK387UrJCa0YIjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24420" target="_blank">📅 01:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24419">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzomeDuZiv297ONE6q6-HsMqZ4Y3OdTItNwvt9wfNGRMW7Q3Q5vbrRV_QJlKFqH7zNyB4Xq6pcngLxNRCo2tqJ0sa7m3IhYfXCW4vjVK-bHVV6EOqqgY4CmQYBdYvcf1C-O-585VgsMw11mufv6R3pNRbWvquPyCNMfzlF9YPfVBcB-DfZcRMipqTqqZy1XFqAOT35ldan8rx-eghFJVnpMxksgVD0ZfwUXwZl1CVbSkxrDxjSj6iT5z6wF1Dla1CQjQtFf07bNDrg40Zg5NxhGfMegP6SQwDOdTBHstzwkWlnj_AhcqEEJot09UJGk6uQQ1OPuBqExG3UJSpsAitA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با برد پنج بر صفر سنگال مقابل عراق؛ حالا اگه بلژیک‌نیوزیلند رونبره‌ ایران برای‌صعود باید حتما مصر رو ببره وگرنه بعنوان تیم سومم صعود نمیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24419" target="_blank">📅 01:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24417">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1DnXo8_ROvbYaLUsrXO9HcFtFhyNJvFfYAip7TYj4ISG-_N6FdF1Mp3Mw-9yNr_7ThxX_9dPd2CvWEbP2eCiPGTAXCMdfOH8ORJCeEEEhwV2eZz2i9erkipxPoi-B_ia71zHJONZVEdJs_wZP6-s8b1VvLgCA4z9Ai0nab7SNtwRf7dkIC2YcAc0ZKNu6YSzTgjYowxNgOb8purfnvRjaKuYwbNPMivJQajBXaxX6LS4VT59mhhv_FV3pdZ-VXa9EakPIEG2iVzdGJZpt6nDVHPlqqRfICB7rx2HrgILjcku20lbRf-wF4RttTPTwaKYXpgB3V1Ava7qhiCfTd82g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛
از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24417" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24416">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaimqWgzoEWszjoi3c83Wqk8Ai-8FculBEA60tzDEqS84tUS-xY6GV3u8TEcxF8UjURMeZ5su_1NoYRI2t8b7QxPSDoQnt7iXdAPr6RGvmP4QFLEkvOc3cE7o3WWuN2SHQTwj2o2LfRq6mWK8JLZEzTCaQq0IeWCJRf5kqzcixROadxJjGYcJC6wDZiHXSo49WE3b5HCGHV4sQua1qc2PzTkP0-xFmSi6lsnl3PqVyKcevrF-B5VKkj9fS_lZzpofM96SXNAT8yTNXLKR0WR581jnHMqeoGH_sz0Hee0v1BSQCyT0Tg3_WQz133P1ZIK71Hb3_J1Gpi_o1MMSi4ETg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌دیروز؛
از شکست تحقیرآمیز عراق مقابل سنگال تا برد فرانسه برابر نروژ در غیاب هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24416" target="_blank">📅 01:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24415">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPldQeY7imV9BLF4qFclFd53CPbQFTmDWuJ3YLZpYi_CFoZji2U1G25w3_XO-qLh0N7WFL1-FAuQgpxy4DjCa9-scNNSdrZvwNJUftC4oq_ZNwNUc2TCi4CEMIBWUhPLPuYrLwdgfGTHFKmim76m_8jHHkGXWNs7TVFM-B2FT1l8t6Sn9R9CJU2kDvjptrXmDSqDcDzlPJAg7KYYkHz2ImYEWGDAayBTCws7vOmMYJcQgIHHOB-0TA6YBkOO82M08g1zmLmSHu-xRafsihiDWCvxPWjEdHDj-Ed-UrcQSLVT-XIdvh7U1FbkJ6mBOIcRtFC3pTg3OM2RScoiyX455g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هایلایتی از عملکرد فوق العاده ابراهیم بایش وینگر عراقی الریاض‌عربستان که تاسال 2026 با این باشگاه قرارداد داره اما‌باپرداخت 1.5 میلیون دلار درتابستان پیش‌رو بند فسخ قراردادش فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24415" target="_blank">📅 01:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24414">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🏆
هفته‌سوم جام‌ جهانی؛ فرانسه مقتدرانه صعود کرد و احتمالا در مرحله بعدی به مصاف سوئد میره. نروژی‌ها هم بعنوان‌تیم‌دوم به ساحل عاج میخوره. سنگال هم‌احتمالابعنوان تیم سوم راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24414" target="_blank">📅 01:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24413">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3TtugJiI4DRn1b2w2vrTGqmHxAF3qA65CK9XGWKrWKqh-V28bcwsYKNmQ67uYBhSLi96aqcorUrX8VMfitkecUoRB0drR10_55HC9bmIkq79pGyXwDmNcl-N-J9pvjAXuc8q03YNwkLiIJ8z3QPZ4W9UfkMu-4VZKv_fyJJHV4P8K6FH2FeltBgPJ68eICg-0HkzgTtoG-O1QoVjPAomfdGqwDuxHBcbU2wwR9LU6E9jJ3ywLeFFtGou8R3ToaS8XMCtOTEaLXbWTCp-3C046RorLuZ3VNYEINkRNFnlWDYKmGlwdNJEO3_Z2ZL1tDIhRaC9LGI8CC2_iNhYMNDeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
علی‌تاجرنیا رئیس‌هیات‌مدیره آبی‌ها: وکلای ایتالیایی بهم قول دادند تاآخرهفته پنجره باز میشود. انشالله تو هفته آینده خبرهای خوبی خواهید شنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24413" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24412">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDd1Y7vs8bTLfoO6MiUg_0iB8ywqJyj6k-p-as7GWN9yI_h84MFYzmY75CcISRgclAhcRXRsiT4rh2fUuOEQMdHtQ_410lqebZqUBtOilbXZKASJqEbyDS7VhVJc-LW_t04e1kL_w3ohGJMIr5BJPtqR-3l1xcfrPNrvguRhs7vrtz4DTJsN7_gtnpGUpHOIbPlWnzJRTHKCdTzhpJ09pLmIDbX-R71ofa4TP6ycWQaTd5f8WsZ7IIxawCuBVtlpzUBMSvoA3CBmeQCV5ZDcV6YgQHX8swGkthKU1wpSdjzYjUPvn2p61Z6BsTE55tk2IOnlFD8bj-G7BOP8rG9SQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله‌حذفی‌ رقابت‌های‌جام‌جهانی؛ داره کم‌کم جذاب‌وجذاب‌تر میشه این دوره از رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24412" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24410">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khKSJC-hVW53aWxtw0_QsQEoxonrPXJA1Fyw_S4pVy_HEy8138r4wTYMfgHsujvNuw1_JTozYrVNAmNmXTTaBPgefTQA4IIebDm4xvsFi8IM-mZ71Xh0SSrJQC04tW6Di2k3BQPrhj1uZ_U3h0ew9Y7PTAmOJJcCBbIU_djPaFIxpHOkpHlfmaKLYcUVgCxzyB71N_tLluuX01VTUjBy1U1e8IkwoIlTa7Vm9S1Aw6bUbeFa7OBLG2k4qDWRmOvaeTS1p_kSIajLO7q5vVU8MKs0O0yjhWs92oPK5wEOrLWRZg5-HUJ2tOwCFaa0Xo9IdIRczK0PahgYOw_8ey8kdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم جام‌ جهانی؛ فرانسه مقتدرانه صعود کرد و احتمالا در مرحله بعدی به مصاف سوئد میره. نروژی‌ها هم بعنوان‌تیم‌دوم به ساحل عاج میخوره. سنگال هم‌احتمالابعنوان تیم سوم راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24410" target="_blank">📅 00:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24409">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XR19KrBS0voWMfhLFJMoHUtrDuwxSGQsRdyy4eCLUYjurSwLwKk60yd2gUnoICFXVEYGgEFOKGyzHZNVUj-lqttWk1CSI5JjAdDIIURPFrUDBAQ5uLvKWQwiAEivMo0MRqN6xF-74Nh-kYeLxIYMH4U9w4wgFMZout9GGC-uHWms4JVBW_f-JNcmNF0ArN3G8LrpB4NWycpjQhMRM3So2U3BUasKaENi8FeQCk75fkggCyc9HqsD-jQJPaS1BO55v3eB1AKKeWRHIQbKbgYQNSp5nmtBNBIlESdwyLbLtPovOOICM8vZDJVe4CYOMKjUSpMrVINGJoZBGwWaRNb0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با برد پنج بر صفر سنگال مقابل عراق؛ حالا اگه بلژیک‌نیوزیلند رونبره‌ ایران برای‌صعود باید حتما مصر رو ببره وگرنه بعنوان تیم سومم صعود نمیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24409" target="_blank">📅 00:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24408">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_RZXn0mSUSfvmtCbGKLuuxjLsN7M32UO2Xu5RTWyAYzTm6pCO9z7073b4KcAlOM6H0lqHEXshoL-gzddFmM78MNxbCWGOgQ7l9hLW6TlaZTWBIBwlJHDh3fELQaSUDoro6QIaNwXQ44F4ymJcz-8QAKcOWbd6B2F0BTbNBtyzHJ_XDl9hZg09xMdB91K3UUR8te90Ha6RFG-xuWI5QnOrf98WJcvLz35FfH4JX1E-XAr3cGox2ASF9ZnmtKlYzEwmGUb_c4eeGY5y7y61tuNvhyFLD_4IVAZEcWRhbSvH55dpmJ6ciha_raYf8Pv39ur-_UIbZzSMzRy8i9HzMgyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تمام مسیرهای احتمالی شاگردان امیر قلعه نویی در مرحله حذفی رقابت‌های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24408" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24407">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGO0cfoEOvFMaLbkGP8GX0vL_mNF_CLKOfnsE9BgDcctJ9VCq29kzDghKJ-VnWBv2uUF2aUwJMyV09C5JIMcsAtOniiIS-_YSVJg4NsPwguhJIJuX2RuZ2IjC8lb9nVs3KFbbTGVw6R8n07lCmNUnbGy0Z8HAZcEwmoxGov1ct-4sGWvlyQlUYuTvgzZiIPujC91VFUT2RthhF9nB4EnqFdUAvIoU1v5QGRaF482fa40zc5aqLnFf1hNFIjxiFw6jxXHJhn1HYyp6fTsGM98aZCHQ5MhuIt1BCwjSwYU00KIG5e-qq6oL5Rj57WhQvYHQgD_ocJRprDBDi9IB5C4fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24407" target="_blank">📅 00:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24406">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L41cYLSZ4c4He0uXoHAiecbr4SaXNOwW4QFkDuScbxfOEsGv8hoUeINxYiExjedOhIR-o_RnsS0TmnFOZWi3A6P6wTXTMuik8tTdT-WuzAr_C22SO6pyiNjIITdjmMg14Bob1jWwg0xGJpNm-8YL7rIZSsSxilnB_Hd5MfmURJ_vhUu2zR6Hb1AT4UWUnjbprXcrsX9qVyjso9wlWC1w75SqeL612cZD-FHZ7nehvUBzjvXYGxE3ICG_oLfLBNyqUpHnb3P8clBqUeocdg-99mL0RvKqcDeKkGtzA9Uw7n1c1tK-NL6SlWBrGHl84wNq869LFrQ5rWFuK5yqHPzHGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ این‌استوری‌جدید اوسمار ویرا مربوط به آخرین بازی اوروی نیمکت باشگاه پرسپولیسه. اوسمار به حدادی اعلام کرده با دریافت رقم توافق شده 900 هزاردلار فسخ خواهدکرد. ضمن‌اینکه نماینده اوسمار با باشگاه تراکتور مذاکرات مفصلی داشته…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24406" target="_blank">📅 23:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24405">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec8965f3fd.mp4?token=OT2v877ZWvfkC-7aDTOVY3GAN-HC9yDeCa5RxzMHWyA2zm17Ek0LYowq4OIkZpccO4-iXmiaxDf1mZv7Cu7oJKB6FkL4bYkn4WDahJdYsHs8M4FiuhDI4Gs6KVdN6PVaLnz9AaRPyWGECJIobKc07ULUOMvrwT6HQkF2qn2oFhov8UHRLw2TLoaxJOG4NJXBCKrAWjVyqz5bHZrJ5gRn0PqoyXggtyxQXLkuIlwv11dojnskRuIwEw1wIGJjtDJLp0MfTMFbMnIcn36wd0CYuWZ0EP0K12HK-2m1nw3tQ-d3o3-c22R_aqs5oPOJjO5Ki6krEms7Ah-YvwrArBOJYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec8965f3fd.mp4?token=OT2v877ZWvfkC-7aDTOVY3GAN-HC9yDeCa5RxzMHWyA2zm17Ek0LYowq4OIkZpccO4-iXmiaxDf1mZv7Cu7oJKB6FkL4bYkn4WDahJdYsHs8M4FiuhDI4Gs6KVdN6PVaLnz9AaRPyWGECJIobKc07ULUOMvrwT6HQkF2qn2oFhov8UHRLw2TLoaxJOG4NJXBCKrAWjVyqz5bHZrJ5gRn0PqoyXggtyxQXLkuIlwv11dojnskRuIwEw1wIGJjtDJLp0MfTMFbMnIcn36wd0CYuWZ0EP0K12HK-2m1nw3tQ-d3o3-c22R_aqs5oPOJjO5Ki6krEms7Ah-YvwrArBOJYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24405" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24404">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3WtZm0aLPu9vwffN7waikkXT3aMhRjOHWl1IUfIgnRLnT1Gc1mrG0-IiZDuHP4CyOMNuHH8bPA27PtQAa8FNyBsMwEDDd6sJbq2RNZ-AIeqkh_uEZuJE9WXeLEx18pgarEBqyb9Nz87IJAsNpdQ8cyBzXKHITjNxJvE8H2OcJ9YDdjre9sousVXtu_8ld5PD_So9AmKlrON2GVSllop1DghxHAbmjkv7k_OC8AbsuNth2v4zN6CQPjXvsSV1iLx2rGyxlD1Wwh4vFpt3x00aCqJZ3StS-n44otgJuqqyXv5naAjZ3FzYJJFyLcNSmPMTsPDLkAM2Gfzj-zUGE-yRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گل اول چادرملو به پرسپولیس توسط سیروس صادقیان در دقیقه 57؛ بازی حالا یک بر یک شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24404" target="_blank">📅 23:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24403">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c65cc2b59.mp4?token=S2Pa8ICYhQelHmk6cvSUH2WPfFzzKX9A9NIenxL1TY51JIy4jETpR7n19tp0qBkIXhI5xMoFveCW4oDkW4pMYt-p8hRGGrSmlDU45_YSREddHDJzcqzhdnX79hVZX9uUJ21U6kTNchbveGQtRalat-hbwaW_w_HVUA4kHQ8UXGtLxUJ8bP8O0zEieSZLl8fkj_WS8BrQQAtT8WFYcOFkq6AUcl6WmzRNFWSYrIHZP3qQHFTUBGeYT4q5B3yeO7bNS5l02mtV75LDMNqB90U2uuNA8Or2H9_n-U2b_58fVegFr47LJy18VnfC0K3wZ9Mxj3lVDvnDkU0oxkFaZ1r0eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c65cc2b59.mp4?token=S2Pa8ICYhQelHmk6cvSUH2WPfFzzKX9A9NIenxL1TY51JIy4jETpR7n19tp0qBkIXhI5xMoFveCW4oDkW4pMYt-p8hRGGrSmlDU45_YSREddHDJzcqzhdnX79hVZX9uUJ21U6kTNchbveGQtRalat-hbwaW_w_HVUA4kHQ8UXGtLxUJ8bP8O0zEieSZLl8fkj_WS8BrQQAtT8WFYcOFkq6AUcl6WmzRNFWSYrIHZP3qQHFTUBGeYT4q5B3yeO7bNS5l02mtV75LDMNqB90U2uuNA8Or2H9_n-U2b_58fVegFr47LJy18VnfC0K3wZ9Mxj3lVDvnDkU0oxkFaZ1r0eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌جهانی ۲۰۲۶ رسماًبه‌پُر‌تماشاگرترین‌دوره تاریخ جام جهانی تبدیل‌شد. مجموع‌تماشاگران بازی‌های جام جهانی‌فقط در ۱۵ روز از ۳.۶ میلیون نفر عبور کرد. این عدد رکورد قبلی مربوط به جام جهانی ۱۹۹۴ آمریکا حدود ۳.۵ میلیون نفر رو شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24403" target="_blank">📅 22:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24402">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abdda890a5.mp4?token=KxXxT-MBS6F00pEK3-0p5HF-Y46OAQajbAP6QVZFgpjVRemTe1gWkVrrhlFzmVi_FAjQIN_mWrRUAdfORNgcEo7tyXqheg9zF31H7YPYKZt7KTdlX98qtT34U3ek6c9pK2E43nZM4O5Bb1uojU8FTtztg0e0ytzuG2GeRI5m2YiWjCe22KQn2kr_3dgGIuhR0zRsOchEk7oTkPHC2126IxQBfiaIwTgmp22hKCVSyXpD28VIK-Yr68DgogSSeMwZpJwilC7Jw_tw3c1S6oydRubyWDBfnGDYUDZZ1kt-Zy6lOr8x3wRCN7RZ0bECOqaYrTTDR9Ql18RHd5d8y0t7u612haFv7AvPe3l4jTQYEBLJQSQuYzwLxq2u5NKatkql-wljaT47il0_tuNDAiEunSWnt3hSPA3uxRy6o7oXxlZGksTTZKRcqjHYhSTmSzQdi_wmMUQQkcqIUcAmcdzknkQi1-W4FVz9gUe2TjLxqhQWsQGLmFy-hsmFgPbGpWxvdXHKcNp25TlIB67RM1FrjSNV7fHpIBzFwUyxjTQsL0v-sQmTwI7_4ErvPPY54HimYU-eeGGlVRVFijnNsCojM-nap1WBD6UsL_UIrdh59DWfy7fUorbzjMbO9LSKMs5Z7-6D9cRP2yA_X8UzugJ62S101kLd5jHMMO7CRdNmdzY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abdda890a5.mp4?token=KxXxT-MBS6F00pEK3-0p5HF-Y46OAQajbAP6QVZFgpjVRemTe1gWkVrrhlFzmVi_FAjQIN_mWrRUAdfORNgcEo7tyXqheg9zF31H7YPYKZt7KTdlX98qtT34U3ek6c9pK2E43nZM4O5Bb1uojU8FTtztg0e0ytzuG2GeRI5m2YiWjCe22KQn2kr_3dgGIuhR0zRsOchEk7oTkPHC2126IxQBfiaIwTgmp22hKCVSyXpD28VIK-Yr68DgogSSeMwZpJwilC7Jw_tw3c1S6oydRubyWDBfnGDYUDZZ1kt-Zy6lOr8x3wRCN7RZ0bECOqaYrTTDR9Ql18RHd5d8y0t7u612haFv7AvPe3l4jTQYEBLJQSQuYzwLxq2u5NKatkql-wljaT47il0_tuNDAiEunSWnt3hSPA3uxRy6o7oXxlZGksTTZKRcqjHYhSTmSzQdi_wmMUQQkcqIUcAmcdzknkQi1-W4FVz9gUe2TjLxqhQWsQGLmFy-hsmFgPbGpWxvdXHKcNp25TlIB67RM1FrjSNV7fHpIBzFwUyxjTQsL0v-sQmTwI7_4ErvPPY54HimYU-eeGGlVRVFijnNsCojM-nap1WBD6UsL_UIrdh59DWfy7fUorbzjMbO9LSKMs5Z7-6D9cRP2yA_X8UzugJ62S101kLd5jHMMO7CRdNmdzY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
#نقل‌وانتقالات|رسانه‌‌های عربستانی: عبدالرزاق حمدالله مهاجم کهنه‌کار مراکشی قصد داره در ژانویه قراردادش رو باالشباب‌فسخ‌کنه و از این تیم جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24402" target="_blank">📅 22:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24399">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28a6fd59e1.mp4?token=l8ILcglpNnq9vGMr93S9QuWwYy1ZTBo8n-BObz4JuGBJWFmfwYlFTnxb5z14MI8ZEhBcSkhPW5e3T81d1oj9qiIGwAHqtSFRiTEN2G2uFhPg5swrSRzOJ5-tnNcjzTzbmFOpa-3bTxDOHL5pWkJj65JINiYfZIfI66txsjyYc-75qCyQxWGxwnHTDq0_0TwGB_VHw52xNREYGdgPqctUlncC-tPwOxUWJZqdB2_woGVZgc89uw3ruj-MiIy5KwaYG8f_vUZKCMWRN6odTNIRvEVxj4Nsu4B1Bn-pRg1mZvMagVHQfhl6W3IX1Sg6HWoZdG7f2RcBMUef_ULgsjf4gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28a6fd59e1.mp4?token=l8ILcglpNnq9vGMr93S9QuWwYy1ZTBo8n-BObz4JuGBJWFmfwYlFTnxb5z14MI8ZEhBcSkhPW5e3T81d1oj9qiIGwAHqtSFRiTEN2G2uFhPg5swrSRzOJ5-tnNcjzTzbmFOpa-3bTxDOHL5pWkJj65JINiYfZIfI66txsjyYc-75qCyQxWGxwnHTDq0_0TwGB_VHw52xNREYGdgPqctUlncC-tPwOxUWJZqdB2_woGVZgc89uw3ruj-MiIy5KwaYG8f_vUZKCMWRN6odTNIRvEVxj4Nsu4B1Bn-pRg1mZvMagVHQfhl6W3IX1Sg6HWoZdG7f2RcBMUef_ULgsjf4gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به چادرملو اردکان توسط محمدامین‌کاظمیان دردقیقه 49 در تورنمنت آسیایی! این گل توسط داور بازی رد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24399" target="_blank">📅 21:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24398">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3569629639.mp4?token=mNMG44ZejQXTNHF1zvCOzDRO_lp3ehfIKhlG4XLQihgI2hd_FnBFcgVCpVoNR3PgRUyljRbiPI74QXGN7EB-pYufRurxPxhJt30fFPJ7-FjeGa2yC2yQJ9IG-rtaXovNzS_6OlJ7s2KolJbktEyBPESaG7_toBa7EWwve4Vl2VVw_PBTpv3jn6r-0J_uwFq-SrHLVyx1xBe1m8KUAuDeng-wMQJxIweDEKjAHbk1rf5LtepPpVYYJ8k_IUoMD1vye_IOMEfFwU07B1X0Bi3qx-BQa35oeg28jZCYlOCQ_3iDaT73NSXAvE_KZgDAdbJ8lipfKjgtbDj1XAYYP8eZB1UdTzoBZ9PLGTjIbYks-wCr8L08-1JagBk0hVjdwtK3lYxdgux8T4o7KfeiWsHPZNiVI1SADcsIlQQ3fDS3JoveWgK3ipkvU8cFTmnqLD02izCkKmPl_zs9kCYoRZBwta9t5mzxm1BTiO71Pnq76SgWecoQTXhba4RV-ejAHjKZdWqssWfP3egFGrNt06o2vyttzck8byc6rM4V_o50W2EiKRjH-785SDF-QiFAd26ZviQfkjiWlF7jghx82YikR_aAaF41kczQ1t_tEsMKjHlGwh7dHbnVWfIc58GL13SVkVBmS1gAZiy3o5XnQmmP699NTMGZBUqNDHkQsiVSgM0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3569629639.mp4?token=mNMG44ZejQXTNHF1zvCOzDRO_lp3ehfIKhlG4XLQihgI2hd_FnBFcgVCpVoNR3PgRUyljRbiPI74QXGN7EB-pYufRurxPxhJt30fFPJ7-FjeGa2yC2yQJ9IG-rtaXovNzS_6OlJ7s2KolJbktEyBPESaG7_toBa7EWwve4Vl2VVw_PBTpv3jn6r-0J_uwFq-SrHLVyx1xBe1m8KUAuDeng-wMQJxIweDEKjAHbk1rf5LtepPpVYYJ8k_IUoMD1vye_IOMEfFwU07B1X0Bi3qx-BQa35oeg28jZCYlOCQ_3iDaT73NSXAvE_KZgDAdbJ8lipfKjgtbDj1XAYYP8eZB1UdTzoBZ9PLGTjIbYks-wCr8L08-1JagBk0hVjdwtK3lYxdgux8T4o7KfeiWsHPZNiVI1SADcsIlQQ3fDS3JoveWgK3ipkvU8cFTmnqLD02izCkKmPl_zs9kCYoRZBwta9t5mzxm1BTiO71Pnq76SgWecoQTXhba4RV-ejAHjKZdWqssWfP3egFGrNt06o2vyttzck8byc6rM4V_o50W2EiKRjH-785SDF-QiFAd26ZviQfkjiWlF7jghx82YikR_aAaF41kczQ1t_tEsMKjHlGwh7dHbnVWfIc58GL13SVkVBmS1gAZiy3o5XnQmmP699NTMGZBUqNDHkQsiVSgM0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به چادرملو اردکان توسط محمدامین‌کاظمیان دردقیقه 49 در تورنمنت آسیایی! این گل توسط داور بازی رد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24398" target="_blank">📅 21:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24397">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3O1Y3mMMu2sVJj0Bw8ELxrLMVeQY0A-14EDl6nmEauZ4QQKZDqmGSVh_7bU8yH-4FISSWQxfluxARRJQfpHvAxvmhXWlAdUub1qTqtgUIWaGXKyJM36B8ookQpI1k6DKZpLGufM1G-2lqyOJ4Ze_0NOKDpnFbRuUDsJFad4q9ODGHsNEn_iOpxKYUiKkgHWtsCrhcCWL-eDhifgrEtJsSHmVucr6AqmoqD3LMdDj5Jyaj2jW7_MlrgztcJnyhEkNzPXw_2qZDS5CnYv1xFMJeJlb-Nbs3bmr10Sn_5r8vk7YTMRW3PDUdh4XerotqN7igj8dE9Se3b_QEoaLD0skg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی والیبال ایران با ژاپن؛ ساعت 18:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24397" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24396">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=TJKHbFYEdWAk66JPMyp3kAKu3ez_BNTyRsgyGemdmQyorScCapdCBOYiQ3mFAIVLTi6g2v6I9AG7Mdfr36PsZWkyyKvQH-Cwwib-etByWrvEtO4BaEcCHyRX271dckZzE-ZGA9BcB4kJ9onqroL22X28u6sgOwB-1lhRYB5c05ek0lreBELRIwM0v8uZkT4cCcfPg0gGghxMDNmWKAmNlSDvS7t3SnV6AsyDniltKnDCGbyPFqGvMmA5b8eVxFebfMm606tmh8F8gB3Plxf6gpudquvwFFDFHz-TeoIUf_UmA1CuJAdNTJl-VvZrCRLpnQ4J2uxPKKpRZNV_NHKUQnDll9OWBUjxxAoqKMzrwzc3OdgUvThZsE_hw9whFmfwTP28mR1KgKVL5LIf7MUlZBNtOur5L7IQYLCVEem-13aa9ObJwOf2EAe4Hud1n3j6Vq6_HFtL5nyTOErgyM8R8ppp39ObLhtY5Ga9pkO_8JP1QtN42W9hZwXeFxUc5oOMI82Qf1QOPD_LI5zbSD1FQzBUnEECwSJPiI_n_sChCkz0oM3qo6qoKL1UXrSw9B1nsD3gyR4_MGMuVzy3wHdcgPIvc7FkSBdrFf5O6AIAzC6LrW5WaAUDAlIdcCJbJgXkRLFahTu_7UnC6udK3m6qGVaD255XVF5iWFB9VMfp7V0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=TJKHbFYEdWAk66JPMyp3kAKu3ez_BNTyRsgyGemdmQyorScCapdCBOYiQ3mFAIVLTi6g2v6I9AG7Mdfr36PsZWkyyKvQH-Cwwib-etByWrvEtO4BaEcCHyRX271dckZzE-ZGA9BcB4kJ9onqroL22X28u6sgOwB-1lhRYB5c05ek0lreBELRIwM0v8uZkT4cCcfPg0gGghxMDNmWKAmNlSDvS7t3SnV6AsyDniltKnDCGbyPFqGvMmA5b8eVxFebfMm606tmh8F8gB3Plxf6gpudquvwFFDFHz-TeoIUf_UmA1CuJAdNTJl-VvZrCRLpnQ4J2uxPKKpRZNV_NHKUQnDll9OWBUjxxAoqKMzrwzc3OdgUvThZsE_hw9whFmfwTP28mR1KgKVL5LIf7MUlZBNtOur5L7IQYLCVEem-13aa9ObJwOf2EAe4Hud1n3j6Vq6_HFtL5nyTOErgyM8R8ppp39ObLhtY5Ga9pkO_8JP1QtN42W9hZwXeFxUc5oOMI82Qf1QOPD_LI5zbSD1FQzBUnEECwSJPiI_n_sChCkz0oM3qo6qoKL1UXrSw9B1nsD3gyR4_MGMuVzy3wHdcgPIvc7FkSBdrFf5O6AIAzC6LrW5WaAUDAlIdcCJbJgXkRLFahTu_7UnC6udK3m6qGVaD255XVF5iWFB9VMfp7V0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل‌اول‌پرسپولیس به چادرملو توسط کاظمیان در دقیقه 28 در تورنمنت سه جانیه سطح دو آسیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24396" target="_blank">📅 21:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24395">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXgjH7t3mOjmZQH3b3D4xZBRd3YoiLdUxrOldf9f2cXCz2VxYA1xJ2WqAJXY89ghX6EW4hEqpu0BtQvRWTQbgcsj7e6lg7_psyQ7Ry-n_Lvhw91ldXa9bLQBAZE2zhf7wub3O7NcobsLTFEp0CI8sMPT1gkYGjy2Dy6I1-785XJW1k-PatROQW1HYXRpNo2IkDvkNyMGOabhH9yaAM72a1r1C9akd1ltPCpemkYseWtyw0VEUz4ZLjIjoKaERvCIarzwI3JI7fg5-kRdSPWhJt9AeEbEWJRIwANm9j6KtfbQpP8JKESeNnJwQADVRZH856rAPYrZOnA5uiRcHHnJ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#نقل‌وانتقالات
|باشگاه آث‌میلان با پرداخت 50 میلیون‌یورو به‌PSGگونزالو راموس مهاجم 25 ساله این تیم رو به خدمت گرفت. قرارداد ستاره پرتغالی باروسونری تا سال 2031 اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24395" target="_blank">📅 20:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24394">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDmGRVlct44J1W6t7rZkNBgD33UZ3dqsqwd1X1LxrS2Ll7kd1VeUbZkIEaNLiO6X_SCQFIoHXc2ei6ejD3I0vzZ-C4mPPf-LACy5PGTw3ZOB61Y1Zs4UGF_NfYToPOeWsoeKv51V2HVuurQ2YIioJeEneAdWf21EyqbguKbN36A-PpfLcoWWRYt4NaqHww6DmRDt8-HgqdWI_V82Os4Sgxl562sR1Y2Lw_yJEQcmvy6qksEdEoSDQFxT_hvpodYD42QyOGyzd18ONnS-uQZT20svtU7T6KOU7d_lhuE4SL3Fkz-31EQNxhzNOB126cP3xOFtXyvIVClI_2IzJzua5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس باارسال‌ایمیلی به باشگاه ملوان انزالی خواستار جذب فرهان حعفری هافبک تهاجمی 20 ساله این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24394" target="_blank">📅 20:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24392">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R28aj_TrM6Rc0Q_zwEOMQSfHO3F-eGsHobmH8p0VEbZYSCyCOBb2RZ_5rdyVqEf22lHFzr0YQCxVxr0haBrZi2Zf5oLdC2XmDu1fPBwzz9q90SvpqfDYiNFYqkYXQjGu1wOc_d-JgR4Y9pVYi55v1lnvgnkLzQWTS5G-5TglwoRYVQ5aBxxAiypxuxSwxip-I65oynLpqij6Vyb33ltwyG3vmp3CTQG2mci9ow7dKC8nyr4nzQn0dXNMXD9ddpTzeiJTDqSDjaMqKetROy9KLJViHCXdAcu_r5_y_8qeCp-dU-yP9HTYgo56P_ziW190phH7hdCoVBlW-TAEFLYEwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NuNgO2q2zErKEXoYOWexPHjMWiF4zPo-gQMAlE3Fwty4NIpIG3qVThm7LbijG8rNnCPu_Obq5q602cXp5iULiBmcCnEHgJIr8rqv-Jmwyqm2qnuCc2-VqpH9Fxi6AMtmTDWqIG0v_Uh3gre1q0yI8TXT6woJXy9o3gf1vYt9kvtet-njzC7z7Ot9FTzHxck6GFA4mK1YTbJ0ltZptRt0YNymchqLUoG1Ynlf1His_lVPfs1JjZPVy1XAZA1xd-KVLlIfTUvrh9JExJGsmi0qmn86uI-zpfEyL6rWiI0jnayQt6Ne_7NjL6o9wOyr8sEPokRRNLcqWuI_DCoB1mqWaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ناتالیا شادل مدل استرالیایی دوس‌دختر کنان ییلدیز بازیکن یوونتوس. این دو حدود سال ۲۰۲۵ با هم آشنا شدن و رابطه‌شون رو خیلی خصوصی و دور از رسانه نگه داشتند. ناتالیا مدل قدبلند با حدود ۱۸۲ سانتی‌متر هستش و قبلاً شایعه‌هایی درباره رابطه‌هاش با زنان وجود داشته‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24392" target="_blank">📅 20:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24391">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMg-UYYNsNwr1fHT5sBLufySO2m_yJI7AC-C2aJu4ICbKSdWFkb6CqpGgTyquW4lb-8MVRZOzgUINn3EovPl3__SU9yNQJmjkwmpwrEEfhWoDnHx6QNommCXqK66J5r3fIPg9SUUwwrYxDwBt31Fbx2_AtP0B0nyxzk1-Xl96cAnS2x_frJPa1KPZZ-qlvIYvIk3sjF8W8sc8TprT2EtdyEJBwmzR_T68PEIpINLKsn_w4rdG04PzbUo8YJu9db3MgyQXTA0WacQ7Ywyj3NEa_rOI7ZYjKKUT8kDNCuUt_Ld5GFAyw-esVeUclFmKBziZzFf0AZt7dGES6Y1ASw57A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تورنمتت آسیایی؛ لیست بازیکنان کامل دو تیم چادر ملو اردکان
🆚
پرسپولیس برای دیدار امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24391" target="_blank">📅 19:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24390">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpX31H34sD-2uOAxIekY_JnZ0MOtbSQjsSGzvSjjMCEgSjK5rTQkElCwPUTiK11MAisHvaochLHK-IFaRsWiuOKmsxbyPdYj8bVpkT2SDAXwvW4KoWFmlI298Exk7z9q4BVbU4wMpSVrR6oXcOV2J-HdIlNeJnM0rsapmk6SkryBweVfzx6rtkIWZHXwe5gYyj-mX6FwHgoywUuBbHnDCvF2qEKT7SAnj--VBRlPOd5aV62xy6q0BzZQZDB0lTZMSzv5LjhbjDxwzbbWiAwY4ytr561kqgOdrIadNDbNwiVMC1IRZyFNkHVlucv2FbHE9bOrYKXGgDLWDoVmpZ65lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تورنمتت آسیایی؛ لیست بازیکنان کامل دو تیم چادر ملو اردکان
🆚
پرسپولیس برای دیدار امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24390" target="_blank">📅 19:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24389">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hn-cVb6r8lzx7ZbBQtKcXc0or_pd0hmi3wIuuPuhJmutPHojq6-1HnDV22m28mp-RMLVdY1O98Y5DHh-c4JWPwZILYXgWr2gw6oLtuP3Yfy2TSYPKEo10JpvycnmUJmA2H2mI5prFZnOxGZzeMcIEEo-bd4XKp3KKLw2MwB_oKFkHsOhVUxCsXeSkr332Zf7RC3Ub5vVPKHgcMhz6Bjquv9MwuKkE8LP33WKNEfeAOvB6kM_IxCEUl0R8l2OEBzUFT3uQfeZQQ5Izm7nWVfc700I8Df3_fTEf1xbPsGVhEAZOoSEfmQlUF5aaGB_qzJ1y5nQM_jqL8A8JibTxz1rEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب‌احتمالی‌پرسپولیس برای دیدار امروز برابر چادرملو اردکان در تورنمنت سهمیه آسیایی؛ 18:45
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24389" target="_blank">📅 19:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24388">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Znot2qLaYsJ9eXzggSLcDGp53Utma7Xo29P3g1YNWCl7e2mGJboVbMVKAaQZWktXv4ifCvN31RpQrwf0_kTeVXgf8YEBj7P6MI9BhKowRs8gf75agOzDi0Z2HR8Bfd2eKupIxeIY4WGxmNXro-1A1lvisQ14QrfKoJjPrAnnIXKAujWN7aPxW0lBK4VZXcK9Zpw1aN8549Et-ptWmn3S41SbnBA0muFCxj-GGycQt0ucs-20nkqpCRXZXxyM0YEb9ylWYmLi1YRoMaL04oh6WZqQx3h5wNHFUMXCiMHVE3yv3YhUfPPhlfgZRuih3TpaPzly5wmUenYZDaHncoG0vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌اخباردریافتی‌پرشیانا؛علی تاجرنیا رئیس هیات‌مدیره‌تیم‌ استقلال صحبت‌هایی با مهدی هاشمی نسب پیشکسوت آبی‌ها انجام داده تا درصورت توافق بین دو طرف؛ هاشمی نسب بعنوان یکی از دستیاران سهراب بختیاری زاده به جمع آبی پوشان برگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24388" target="_blank">📅 19:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24387">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlXpMegKgycoOEfKC9GBB86GB71vX70BNZ0BsEtBdN9ZA4XheXoG0wkziLcbWwEqd_d-Zq6W0Ph-yiN__TGGOltA4Z4B9__BD__m5YIMVMpFx6fJ2nG4njHzsj0g_vbQ7yy5qMf1Sk0jyxpWZdK2lNYnCgLTXd_vYn0cbRXz43Vf59UHfX5h_7_1I42qkcm7lMWJwfDfU_hC8iS8Je9j6lGPWe-x5lFchKGgfNkQG2YJtd8GG0kNNeUXxXjltVRUl_19qm4-czeoJMrp9AduqOc2IYpu5PfVr34Q8tATgskDyyf1tEGUuOYY2sqotYpHQD0A44uWTIhKg1u-SVKIqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24387" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24386">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVfG3MPvVvK4KaxPlTPk3KvWLPTuI9S5Dxa4lhnohG7LBaX9OpNK6ey4ROXtel_E57qcDpFV7JJQ-bgIkcXgkhw90qKzP7zGR-YUv9dMh8xr_xibozqFqBF2Rnb4HnaojNH8A0-uUf96j3r0U17iz-664wNftNuBWMOGbQ9_F5EJdtNdO6DyHzkR1hn8OWk--ZoH1Z08wCErpgcd_c0soCmcGZTHxqQXVPOTBylov3dz5w17Yz42to0Wb52j-XUXNOcTHjkAN6PYXt_KoLB8qVIn5XUeRgBdUs5gzCtpYmciPwAAaketfJhI749sBg9Y0-HS7YET6wem01KHASHvVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24386" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24384">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOCblQ0xZEyHKrZ4LPx3R7P5cdvEw7qEML-YHEmBoyu-x4O-iCYHiM4baykqdBDLFQg_yEBbbxj4RRmHzQzbi2vBY2vI2BUnWLUng1i6q5qIORYjhG3kCs-U8SODIL3UKeys7ollY6FSKzhvJnhZ4y_ETxJP4zreg5s05WIQeSGcZrwS5rqZEbYJdpXuOi0rtMULsIw8yxSzPQ6SWpDL03Q2Wy1M-7RLetX2NMArdhGBM1oVo-NdwiuJjiUgOcXhJU_gBZ2YLPjrkH5f79RKJti2d0ANWPSMeOQBKfjsATZqdRv69Y9U0a_d0HzEcZVNF9ECgJYUDoUYd1TVa1E1Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آخرین وضعیت تیم‌های صعود کننده و حذف‌ شده جام جهانی ۲۰۲۶
؛ تعدادی از تیم‌ها صعود خود بمرحله یک‌سی‌ودوم‌نهایی‌را قطعی کرده‌اند و برخی دیگر از گردونه رقابت‌ها کنار رفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24384" target="_blank">📅 18:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24383">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFPOBPH4DL2CL61y7zXH1NijIAisr1kXTo6UAcefew0ivdKrmiyhbn9sgcQvkN-rzrgN0MdkpNTTJ6Jqa-NoyrSV0f77HwTBhP29j98hXYWMsOZV50sqlxOS2tS7VwHqXfoHIXyb0ib7l8Puan_snkhRCvbE6rjb6FIm8Ye3ClP8lR08j2LACo0Z-dP2Gk4PBZEs__VzKuxx43QehBMWIoWPPsdKhi6bzMTLJJxHzMW2y06deAkVPQ_UNiauAhOBHMysqKTQAt6O_BTvcNF--urEaIt_GrlVmw_mqjUU99WytGbZemdd3YV7dWBtVmO9xizgy4-RO0H80iznxti5ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛
ترکیب تیم ملی والیبال ایران با ژاپن؛ ساعت 18:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24383" target="_blank">📅 18:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24382">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSvKhmrsdunfCb1xAy_iatXwB0E9JsU8IQ0T4BM9d9x1JaIy6S35yrdMrM4bbjBM8VxkpsGrAD6jXwa458Qk-L-oEGUaf-eS-1bzDh-I4dbmiEjQaA1bCZcf4RZXfAftW_NqnuPJVPcyk_9xskJPW0pSzkGXjFURHrWo44nmjlwsP7tKZbor8dqYyLwRAScXVbSxYWwnYWCRe0GhaB_jzwvEFxFzQ4Pq5pItMCner0MkYLINchL1osLD0C5r7fGN1BxKYN4CgYtOIht5ghg8OYyHK6-ca_TAcxem5C-zLUbpDiyEPl-kv8AOms2Wcs-dXpKtmxoDTFy5MkzTVsUdvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24382" target="_blank">📅 17:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24381">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4zx8UiC7m2mS7w1hRQfwBNoPvbcAhofKHP7gCWfc0D2StkX27fsmfMDvgV21xAlr59N5zKmUiAQQ93aSdEB18xBSlMJ4Z4mDz1VeRGMp1ebqK2C97ZpRdp1co8wzOLSZOI9Wc55G7Zv57esf-qQis0EeJhXTkngAZYUysB63wcJyySVYue4QSANRs0569_iwG07Yq9hbjlpuu_nEvUsyAQE6Ime61DBOw7ij7_Il76wBrd-FF_4Bfz623MGMLvoN6gUEa8NocK6GTgAk2YlqWafSfbRxJrWH1E2maLwyIdmn24T-tnRNrJvEDq44FMK1ae2-UHpghlZHtFbGr9gKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرچم‌حمایت‌ازهمجنسگراهابین‌پرچم‌ایران و مصر قرارگرفت؛ فرداصب قراره ورزشگاه رو از پر از پرچم های رنگین‌کمانی ببینیم. فیفا گفته هرکی از قوانین ما پیروی نکنه بین 250 تا یک میلیون دلار جریمه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24381" target="_blank">📅 17:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24380">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxYnDFzXNwDF43DOdYcAQkd2hNOvxqrsk9qCtX8TcPFE9F_7RtaT1yfiIu1cqBvSq0RaZyPrefNRyEulSK440-KZx7Zxqf_nCCbdTMVMBvLyGucOnfL_lXJ0Pgz8jd8kEQ79IDMvjFcgTio9t0aVZA6xBtd7V5HPz_6zmQ2HSpX7hgrvDoXslFhUuLpOMSDk9gm4nbHZE09LugNPbDk7MUSmHMD5DMlYPf87-YWgZ_cG_NRWZdM-JFyd08AEmycJJ6t1r4KRKU3urE2jmubvsndx6v-EK84R9z-RAIyqrUbgKUExv-dpj60F2DGn7XKCCiBqrWcYUUC7AltsvmOjeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت‌ باشگاه‌ پرسپولیس روز گذشته با‌ارسال نامه‌ای رسمی به باشگاه الوحده خواستار جذب مبین دهقان هافبک دفاعی جوان و آینده دار این باشگاه اماراتی شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24380" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24379">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opqQjMWj8oQuvx_t_bCyF1miAXOLRkId9XJ19JyNMPYvVgnLbadan9da8j877fuf7z4FBudCyLiT3APLicQWvb9gIfTZONQG5ZGUO-svNW2n2MQYNVCqHlmUVk3jiXg-J8c3JCei5H1dcEmnH9KXB4ir0CUIQjOrZXfgB0zwRvlEVO1idS7j6qkl0siYk544JJywNdXP28c9vUMNn-feA-KOaYt0-DRuUMiKkFWsmHKurvOcNAwrC_N-9EbOUekzUEz6muJJHVAeQXw2HeYertfndZj0Mh15s4NoH9M7Y8eyRfWHSu9UxPpZ77Re_ZpzvEtrGnoj4RhHLP6kt3cPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ داکنز نازون مهاجم 31 ساله تیم استقلال دربازی بامداد امروز مقابل تیم ملی مراکش این‌شلیک وحشتناک‌رو روانه دروازه مراکشی ها کرد که‌با سوپر واکنش استثنایی یاسین بونو مواجه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24379" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24378">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2f7b8fb9.mp4?token=TmjyoDNmf-N09gJmAuoOJzrzAEF1EpSJyvhStduZE0LmYKj6EicYtU387uorv9uK5EnbmzFD7BiQmJX1IItK3a0Hi__4xbbnxNq-33ygyCiMhiVyTiRv-dGUY5DoMbOvdtFZk6kX7pz1Rtipq4XkIcR1Fx6FN6LgVbsUbUDKfPQq3zGblvHXiQg4Bgsttk8BpXTaL7Dl8rbP3b3wO-0kyNGEZ5INx-_d7VsFiRoFJq2NI_ojCYFmlEKxCBvVYZdoj9zJrg0TVqiSm3TOtH4Q9i06BdsOH2lhJCUEsvunasWdGn7SwHfsb_4swbX70lSmL6j0U622nDViQAbOcq9guDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2f7b8fb9.mp4?token=TmjyoDNmf-N09gJmAuoOJzrzAEF1EpSJyvhStduZE0LmYKj6EicYtU387uorv9uK5EnbmzFD7BiQmJX1IItK3a0Hi__4xbbnxNq-33ygyCiMhiVyTiRv-dGUY5DoMbOvdtFZk6kX7pz1Rtipq4XkIcR1Fx6FN6LgVbsUbUDKfPQq3zGblvHXiQg4Bgsttk8BpXTaL7Dl8rbP3b3wO-0kyNGEZ5INx-_d7VsFiRoFJq2NI_ojCYFmlEKxCBvVYZdoj9zJrg0TVqiSm3TOtH4Q9i06BdsOH2lhJCUEsvunasWdGn7SwHfsb_4swbX70lSmL6j0U622nDViQAbOcq9guDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
توصیه جالب جواد خیابانی به محمد جواد حسین نژاد ستاره باشگاه‌ماخاچ‌قلعه: هیجوقت تنها نمون. همیشه مادرت رو همراه خودت داشته باش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24378" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24377">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjjjyW3t7CPyIZEYCREHLVxU1v2JfzWJUosjXNkZcLeAlUajdi2UruzWAVgGWpO9BEADm_wJ8Ee9QRloPwN4Gp9FBi9I6O2imfrtLZ63ePwOseCON7nqCU9aPTGM7DeM0xP7l7yS2pJxmOv5zhNvH04FkIl4B7z4q00PB1OMXwrLS2NCgyFzTSscpfO7W178fLJq-8KkZK9d195odr3YWvxcDy428omK8EmFosUHZ_C7qFEv5zI94g45vZQ-VtogTgmsVVDOA9HunO5ScSOpzMDyIfJnkRxCarLnZSsmssXFWgCL0kD3Wlfaih7LUJG_4IbRhPnUsQ8YyrqDL2W1ZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24377" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24376">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6YlKcGKbXVVY0JdbE6hrok1S8KaexqjFie4_7A1d85Q3p47baIdWSeTKaZR24R5hbi2S3A9BoOym258S2XlTeIBoFQXlSKIyFWsgkdVGivm9S1qbVhtu_Qyrp2U9wJyyXHh9yjcz1LHXWHJTMpZIzYTw6yRDCB_Rh3Su2K8htp1yrlVHhPOfXFvQYkceat0OmFtHdSd5Rf_g-55ef05TrfpR76XEJupNtu0zNy4IbxeVkLRCry0SpRo6UiiduaEgrfnfn9yDTTWex862TifcYElBTrM00Lqx_yz65pkRDky1uhD54_Xa-uKfVkAKUoSgBzj3PiwBQLZNyrN_ARApw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی
؛ پرز از اشتباهش درباره مارتین اودگارد درست کرد؛
باشگاه رئال مادرید برای انتقال پاز به کومو 60میلیون‌یوروگرفته و یه بندهم تو قرار دادش‌گذاشته که هر وقت نیاز شد با پرداخت مبلغی ناچیز این ستاره آرژانتینی رو به برنابیو برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24376" target="_blank">📅 15:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24375">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUa3rUe-FQIQnCcxGqQqjHbuvEW3hscCqwdMVPExHhG5z2w0LmzrqiSbjUDscPEz4P8GXqVtT5zlkQ3gGESirBg72iJLX7XlcHmPXGH4HinnlF2jQAjhBS1YGhfAnSOfov1G077c97hp_al4wPp_SnFVDyCs0_EJYQltr2TGMhZoyRCnnPi2xf5SNeFnkAcLconBAt3qJ9cT8Mle-3KbnTQAuiaDKFinTXevteF_PMS-0xKCZ0T8XrOHXi5GxfipTwGqAwm2cZX9-QMkWlgtklV4bpuHLpu6-_NVJdj_v33SPMUf7plC07h5AgvUOKsbSt8Av51lXAxpG8hV5Wuh_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
اسکای‌اسپورت:باشگاه‌اینترمیلان آماده است برای‌جذب نیکو پاز ستاره‌آرژانتینی‌رئال مادرید نزدیک 70 میلیون یوروهزینه‌کنه. پرز با دریافت این مبلغ بال در میاره و قطعا ستاره جوان تیمش رو میفروشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24375" target="_blank">📅 15:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24373">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKxlXJEpCsBPE7Dksdb-m_zT1g3DpQQSo8AK_CdWVYXAs_T_MhPjd2NiDgVaacpFxI5cA341kGn7Khg1w0VOlFKkgWjpBQphLOqCGoVDji5DKBp_h3K5I6nyA6qH1eldmwkJkSdwv5YvUd_9eLb_V8QNp8gapX2TxzlfB_4HTIX59H3xKAERvoo0xLGvpqjLK82YdGcADK_DB_Omrc9R1lDBFkpEfhM_EUEf-7mmdY5HHFfd3fN6YDhXEQyI_dPXMzylZOmMDXY5deYBlHdtO9QHMf1lQwTB7fTfXqCXybCj3neQCvFEoPeLI1e0J_AbzJudj9x1k_PVPnEN2cxpCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=cC8lWsmd-r8oSxUMPSDx_18AuCa3_Cqb4FiZ42eciu1NSuK14TV9xpgn2nu3pula8IXVQYdiveKQ9xEEvIiBpkRFsvQWbqEe5akMcOxAoLTl3DayaxMb9p116wwfZgTVs_y11d0Idv9Tt6Pgm2f6TGIMi8jqsEmgZHY2jEgHN2Kp15xjsC3_U1QNs6KYu6lR1bqYUBScni8iVSak3mCkJ75ruL2MMzXqsBRNDotWf-h5dtbaWTsA9bVXBWG7ouHK4OA07T-mLthnzKCmnsbs-jCIU_Mx-Gha0BHhoJR9vIhFvATj_xtx8rPGxz-VZq1YUoo1x0gKGx3dk29hrdLzUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=cC8lWsmd-r8oSxUMPSDx_18AuCa3_Cqb4FiZ42eciu1NSuK14TV9xpgn2nu3pula8IXVQYdiveKQ9xEEvIiBpkRFsvQWbqEe5akMcOxAoLTl3DayaxMb9p116wwfZgTVs_y11d0Idv9Tt6Pgm2f6TGIMi8jqsEmgZHY2jEgHN2Kp15xjsC3_U1QNs6KYu6lR1bqYUBScni8iVSak3mCkJ75ruL2MMzXqsBRNDotWf-h5dtbaWTsA9bVXBWG7ouHK4OA07T-mLthnzKCmnsbs-jCIU_Mx-Gha0BHhoJR9vIhFvATj_xtx8rPGxz-VZq1YUoo1x0gKGx3dk29hrdLzUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سباستین بکاکس؛ سرمربی ۴۵ ساله اکوادور بعد از اینکه دیشب تونستن آلمانی‌ها رو شکست بدن و به مرحله بعد راه پیداکنن اینطوری از بین جمعیت همسرشو پیداکرد و از نرده ها بالا رفت تا بغلش کنه. البته صداوسیما این صحنه ماندگار که تیتر همه‌رسانه‌هاشده روکامل سانسور کرد تا یه وقت تحریک نشیم. برد اکوادور روی احتمال صعود ایران هم تاثیر گذاشته و ایران با مساوی جلوی مصر احتمال صعودش به عنوان تیم سوم فعلا از 90 درصد به 60 درصد رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24373" target="_blank">📅 15:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24372">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0edb018d7.mp4?token=hR-mIn1D3Fby5VzNPhCzyDub4nbUgLjSveNk7knuBF0uJObUV5KIe-rZJc1gb1xsQVFuzdUFY5mGSxyNeDIuX4r27wdvWSGycqWd5DaPqaZgPMsjCWCoBumscOFY7QHjb_nGzTF2OtWiZfhvdyXjoq_P2NaZMbq4iCD25erbBetnQsDE6Tob8GHEuIwQX8FTzsX7wkcrG_c1nvnDWnrt6OPqXsInQczNIN1-0GkU_gRCavlolAsCVXeHHNWNdAV3RWdQOl_e22NhL-rnv9a7OlBFfzddd-mpPCpWcKUkHNnSOjwNOdS1yy1LUgcVfJJ7Ebnko1ckNifNvqmXw_AqEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0edb018d7.mp4?token=hR-mIn1D3Fby5VzNPhCzyDub4nbUgLjSveNk7knuBF0uJObUV5KIe-rZJc1gb1xsQVFuzdUFY5mGSxyNeDIuX4r27wdvWSGycqWd5DaPqaZgPMsjCWCoBumscOFY7QHjb_nGzTF2OtWiZfhvdyXjoq_P2NaZMbq4iCD25erbBetnQsDE6Tob8GHEuIwQX8FTzsX7wkcrG_c1nvnDWnrt6OPqXsInQczNIN1-0GkU_gRCavlolAsCVXeHHNWNdAV3RWdQOl_e22NhL-rnv9a7OlBFfzddd-mpPCpWcKUkHNnSOjwNOdS1yy1LUgcVfJJ7Ebnko1ckNifNvqmXw_AqEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏰
بیدارموندن‌ساعت 3:30 صبح برای درس خوندن
🆚
بیدار موندن ساعت3:30برای بازیای جام‌جهانی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24372" target="_blank">📅 15:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24370">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YHZd1dUpy5K3iJnUI3IqUn5B7ilwYQrQTlpw8D_iGoky6mlmQXdn3E70J0rlCd_n776bb7Bvst383JkKTqL9ks0CuY1PO12P9D0CQUfwg0Q0t0Sh_Nnt7MYBUjAWbxEwK93MINricGPnN2zrqduZwxKAero7ooLJ27hNNPI04dK9_PcENvUsuaQUiffTb5psGBItBW4eMmtuKINoO3XGs3VAtgk0uHRbbY5bqsPMUHxiyPLEy3Xbb6VxScgtJYytk-nTVdRlBAXcz3NfjU2i4_aQNbiYDGDih4PENHUbckpiVQaQraJ4Pi0yExpfE1c7nkT0rbIuTr_JY4tg-ixKlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pDHGvMnoiWSR3xKa8Etv2NzZ5w3MnHnUVTw9oGa0v4TSd6gKu4nWmuxDyILShu7RIyAw5ugsI-1ji9260-KdQli9WxodHcpw_Y-NcMIy0RJdsChgNdSjTsGAsfAqGWWZ50Hc7KHgWv2NYwILNcUAlNUfQqtg3GxsfaCWGiR7KGikEBoy6Vb42HQTpxyix2u9-N-YF3avDV_3rlq1DI2Vdrs9YV9eh09sE2FvNkPl8aoYRI8lSMICY01f5udEf9gN5YpqvIkFlXd33-_KH40dm34Eyglc2PeRnlM7SQ32SKrNWTjD8tv8ScIzfxxng2MRabWd5jnSj-NQhZQr-fGMPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DthTsS3oD5iuweloL8p4ztMJABLu0ayMD5hlACe4NiMZ2SWaoY5v2hBiSB5K1YjjidyYI17dqayU6ZVb5IxMJWXvYyGKrmH-dvpnfoLwnGTkb4r7JqzhqFKlZldLp290loZydVDKTOFIrCd5mNJziMZtYa504II_Dq7MuDgCwE64n_8Ppcwz3qhlThkFn-LzsG5kJLTducqT2MRgLic1hgpDes9QUnOBC1YSqO1m6_P8W88Uki6AIERQ5CKUgIpYQmH62db3tTqnpytJecOPHZFHUAywo4CR-2Kf3UWH2xf2y2PDec8c-fWPXMTv0rJ61-62xCSGIlY05uhSIoQ4MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال ۲۰۱۶ سمیر نصری که‌بصورت‌قرضی‌تو سویا بازی می‌کرد، برای درمان‌سرماخوردگی به یه کلینیک تولس‌آنجلس رفت و بهش سرم ویتامین وصل کردن. بعد از اینکه کلینیک عکسش رو برای تبلیغات منتشر کرد از اکانت توییترنصری چند توییت عجیب منتشر شد که ادعا می‌کرد علاوه بر سرم، «خدمات جنسی» هم بهش ارائه شده! توییت‌ها خیلی زود پاک شدن و نصری گفت‌اکانتش‌هک‌شده.بعضیا هم حدس می‌زدن کار دوست‌دخترش بوده؛ نصری امروز 39 ساله شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24369" target="_blank">📅 14:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24368">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ab6e00db3.mp4?token=qbAJycSpFSuBHrANfHIGtyG6ifkScLTEvSBPpte5QQNhDdx7fsASlbtSXkZ52yGr_FlNHUa64_jCwbqz5HY71V9BhI8l_LxJc9EuUJh2aVxccXhdYgGi79yz0NlpwDRFYj_025HjaWniokhCOYk2OBubK0SM56mtceYcAwEP-Gwbna8RI7V-cCi-V97dg7PkakckLvUBEqZKQuEOCjURdCeq6uqp7oFZ7qjj8eeETtggM1cxYd0S827NkRBSUMCVv1_2V7bl5X6fNbue6wP2KXuR_dL__Dj53bRyOLrcS-tCiUiMee3QDVO4rZv8VYi2MZ0jejPlgLRkVihVfMioIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ab6e00db3.mp4?token=qbAJycSpFSuBHrANfHIGtyG6ifkScLTEvSBPpte5QQNhDdx7fsASlbtSXkZ52yGr_FlNHUa64_jCwbqz5HY71V9BhI8l_LxJc9EuUJh2aVxccXhdYgGi79yz0NlpwDRFYj_025HjaWniokhCOYk2OBubK0SM56mtceYcAwEP-Gwbna8RI7V-cCi-V97dg7PkakckLvUBEqZKQuEOCjURdCeq6uqp7oFZ7qjj8eeETtggM1cxYd0S827NkRBSUMCVv1_2V7bl5X6fNbue6wP2KXuR_dL__Dj53bRyOLrcS-tCiUiMee3QDVO4rZv8VYi2MZ0jejPlgLRkVihVfMioIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیم‌های ملی ژاپن و برزیل بعد از اینکه از مرحله گروهی خود صعود کردن به همدیگه خوردند و این مصاف جذاب رو رقم بزنند مصافی که قبل ها در کارتون‌محبوب فوتبالیست‌ها پیش‌بینی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24368" target="_blank">📅 14:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24367">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=q5lE8Yty3inCJzgmR-7JFD6gcy5zROwPni71lQbgbAsuQ6DTu927IMGyfRhyP43ngJ7qNdhMEQuzGYVmI-O1hk5tnqcdUb6U98jO-YhJ0nKumHaKwQ8yl0yPWU7A6UHNYCOtUgJ_QVCXlKvBDa3Bbafo2IPm3Hd0_HcoBzuSKm1f7muvYJ07jSOwNiz6FvuQ1w2CrAzQwF5KWSzaDwYqpRySB61NyYHGSWiaf-OtTtaA3YbiQGse0buhV0tbBaT8kstuukCWekqmXMSq47NyJsO-aXL2Ao3r_DV9Atvrig0fKHfHzYen6J49Z_IRfxI63eQXCZYCRXgw7AlK8qQBmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=q5lE8Yty3inCJzgmR-7JFD6gcy5zROwPni71lQbgbAsuQ6DTu927IMGyfRhyP43ngJ7qNdhMEQuzGYVmI-O1hk5tnqcdUb6U98jO-YhJ0nKumHaKwQ8yl0yPWU7A6UHNYCOtUgJ_QVCXlKvBDa3Bbafo2IPm3Hd0_HcoBzuSKm1f7muvYJ07jSOwNiz6FvuQ1w2CrAzQwF5KWSzaDwYqpRySB61NyYHGSWiaf-OtTtaA3YbiQGse0buhV0tbBaT8kstuukCWekqmXMSq47NyJsO-aXL2Ao3r_DV9Atvrig0fKHfHzYen6J49Z_IRfxI63eQXCZYCRXgw7AlK8qQBmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه نویی درباره حضور پرچم‌های رنگین‌ کمانی‌وبرگزاری‌مراسم‌حمایت از جامعه LGBTQ در ورزشگاه سیاتل گفت: مااینجابرای فوتبال هستیم نه مسائل دیگر. تمرکزمابرروی مسابقه‌وکسب موفقیت است. درخصوص موضوعاتی که در دین ما ممنوع است و وجود ندارد، نمی‌خواهیم صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24367" target="_blank">📅 14:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24366">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsNDv5iK9A9Gf4igaPdsSsquRxDC0rcbQ3PycBFmfOtCwKGBajFZMtz6HgIa4ztdtEIGP3MW7SZxsPW8LgEwUTXAd3eoLkNlj2AO_Wt2ifqXUtGJDkZkipffQILFfGEaBH4REk_xLkDaqjwyokW8o05rP1AGm0yuqzy8eo7pYaN_kRnHkzIcMfUQOXA2JRKVJYNFKDoB3I0DleVRcyMf1hcLixYcGdSFkF9DbJW8s6iapyzJjWrUbyiEqLZgoWEIwgDB1oFjg0zECAkmPS52_M_RC64t7sNy5iOW5XnyrpB4uuJSX3gHuJf6yF7Q2WRYqRl33lK6Mrf_U5_jNi6VlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
دو پست کریس رونالدو و لئو مسی در ایستاگرام رکورد داران بیشترین لایک در جام جهانی شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24366" target="_blank">📅 13:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24365">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvIJ7hYA61qJy27YtugnEJQe7GUEB0F3w07AyrS2j99aE0UuGnMq0RWANoY9LNskpfxuzlYC1Go3SWPEUzvl4FcgbMKXdYKos5ZEzxh5zlIzlTYVqrPTKFAqKAeQ5372uG3RbWkPFXsh853tYAU2h-QTJ8GCRf1MLMNLWSZ0Sg-LGfnS9N_syItvHUu8k2FXuh5umt2F_oi-LzqkKwZhV-4ysRS1uLCtgyHOvZ--ZEprWeJKzpkE8hOAWo48t2My2pR7_e2kBWcNvuWD1pcnFjfLx4YORTUfvV1YxHKPDGtPVeLIS__nsKhsn9NJlPmzXeDXSzwD5IhCx47ERPFdDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇬
عمر مرموش ستاره‌ تیم‌ملی مصر:
ایران تیم خوبی داره بازی‌ های قبلیشون رو دیدیم اما ما اینجا هستیم که قاطعانه این‌بازیو ببریم و صدرنشین راهی مرحله بعد شویم. بنظرم بازی رو سه - هیچ میبریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24365" target="_blank">📅 13:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24364">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AchRgiPUFSK2Mtcj0uNxvjAuJDdko0e_q-Mpg3cnNNIGRHyAyREBhkUL-U5PRBRUDR1H9Q46TyfoCXHTwjBLEMIjakSJkojbb1XxUAyt4vpLYXdJOvqryCyvb_kINiFL19K7DPKwdzVafpAcBKOjKGCq0CqHPrq_i4BxEfhXXUzAFbRlISF9wtIileS6dNVwUtAjuenvJRAJXkqCibOdd0caLimJC8xP9GijtWSwwe9MjWLW4vWjCYlffPNDIfnyYqz4cITQhRKpq3qIljdiibBDWA-vHeLENuKA6BS1BVFl-3CQuThVykD6qgmwyJDGywZdQW3UqwusUuxkp84Erg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
اسکای‌اسپورت:باشگاه‌اینترمیلان آماده است برای‌جذب نیکو پاز ستاره‌آرژانتینی‌رئال مادرید نزدیک 70 میلیون یوروهزینه‌کنه. پرز با دریافت این مبلغ بال در میاره و قطعا ستاره جوان تیمش رو میفروشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24364" target="_blank">📅 13:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24363">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ti0ZutKkCnj-b1FHiVhqVEZe1P-X5Tzshup8Tg3FmYkqM_qaljUNaQNezwQVXl1ThGFchoInlza7gZEq3ss6cvjR6X__TFKqVmEJ29i4pzbmYYBn60A8tPV0jkbkPUa0E2vaaAp7XOASBfgkiXrp82maG9N-vb5vNrAxaRYXJl2yJtKANBjrbmGza7XgmkflnzpwjdyYD4vwn6v2ozJ3Gm-c-AcOf4yVTWrDkhVavvQuE5cSVYj2Sii_54DoTe5AKp02WNNrdhbD2QUpUk5wS0xSQJsoEWar36Bm1AVdTXFSlXmv8zdUQaDVd53CrYonrvMRdNYzWGroWdqbxiLz8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24363" target="_blank">📅 12:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24362">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0QnP4yZ4_Kg60R5PrCqH1Hx1IlohfYDStigiuzLwXUNyoqChOZjT9l6k231UpqhJ5clZBzboY8Al5wa68E-gBcwh4ndmWFFFfK-_hgB3J1hz97L6vAK5wH1v8nDpmVez9T3aiGPDN8hlb4Ij5k-CmQIK1f4WICnuojj9xiXwA_ku54G94w_WnR1PzJ1BcxpXRMHBLYzPBJbYRMlUQihLMYfyBDJ0gJjJthXgdgZ-6h42TBlb7Y_3fnlMVuC0YAEtiIchZjllAjYOxFJbfz68yumBAwoaFhdKEoW-EScmvLNux5WrCP5FUZx3LXZ3snHrBo8J8jJhE5KvOTSfpdixQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب‌احتمالی‌پرسپولیس برای دیدار امروز برابر چادرملو اردکان در تورنمنت سهمیه آسیایی؛ 18:45
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24362" target="_blank">📅 12:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24361">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iz3rnpPW2uqp4Sto3DGTIuDjQjiXv3E0ZMlO3gwPrIlsJX7nqpSymuXOO5LTmZtQ0NLvVaQceNuBwpl8_ehLBvP9IGAXfr2RyqHbqFK8bRkizYFrtGL-J8kdjKSh0H4vUnNj95I1yiQ7tDRnXOw8kzJTUrfRzdTY7yOcJ3-Hf-NJiQA_HsJqgifpL72rgBsKdtbNr1Z36JKGaVD8Bw58SIcNseBtFPw9QLk3HGLJNl4AOateYblQYHnhZbpLNlGHNOQ5_Y7MCRGxnceS4dCPo2tdRfwTwKRz5eTq_IDDfjirS73CHfzX9L4X84ErR_CiwJMaUDXbuA99FOxb32hExA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون درآستانه‌دیدار فرداصب با مصر بیانیه داده و گفته‌رژه‌همجنسگراها قبل بازی رنگ پرچم کرنر و پرچم‌های بین تماشاگرا و هرچیزی که مختص این موضوعه به ما ربطی نداره و به اجبار فیفاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24361" target="_blank">📅 12:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24360">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b03de0d7d.mp4?token=slzgG8aApLR-Sch51DRmsFiTJnAXta4uQNLja8wRwtYF56M1wbIL5c8hE59Ej6LcSJJ43pstBJ-cGDXD99qJ7LdLWVKQMn3wfszkbknSlHgA1iK7XSAcExwYgeMnFtWTy3KRUQrb7Lu2dtvs7-viOq6WhdAyU7gN5lVI0aIvVWmD4lgwZVPyXxBuJuWvgOD2aQCS8-zM3lzAgqOBdxRzLLYy0q97vxlFGECAQqqpwdGdiHXqGX6qh5VWXpT0F4rymYRZU1xql_-Tmy3mLlYK4AG8cmnKEl1gTP2VtO4TGVwlmBBgYWrxlAOoA19RMb9lznV5ZXdyRngz8cPe3q1G6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b03de0d7d.mp4?token=slzgG8aApLR-Sch51DRmsFiTJnAXta4uQNLja8wRwtYF56M1wbIL5c8hE59Ej6LcSJJ43pstBJ-cGDXD99qJ7LdLWVKQMn3wfszkbknSlHgA1iK7XSAcExwYgeMnFtWTy3KRUQrb7Lu2dtvs7-viOq6WhdAyU7gN5lVI0aIvVWmD4lgwZVPyXxBuJuWvgOD2aQCS8-zM3lzAgqOBdxRzLLYy0q97vxlFGECAQqqpwdGdiHXqGX6qh5VWXpT0F4rymYRZU1xql_-Tmy3mLlYK4AG8cmnKEl1gTP2VtO4TGVwlmBBgYWrxlAOoA19RMb9lznV5ZXdyRngz8cPe3q1G6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌هایی‌که‌کمترین‌درصدمالکیت رو درتمام تاریخ جام‌جهانی داشتن رو ببینید باحضور افتخاری ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24360" target="_blank">📅 12:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24359">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZ65FuZObN8o2atEiO2s2tAcfKacleRVPSi9q8ynW5j7v79d-Fp7uZzKh53NOwRMSdWVkoNt4iQJItahzzD83cqy_xvNdK92JjXhbiXSW4s6Mq1YUO70s7VSFUQSNB_BFA6h0tJ2cB24e6AedfX9zgSTwR_4CfQ7anYQ57i9fM0xnJ7eY_FCaooy6i967wvDKRMRXlXvRS5STWbt3t1JY7D5TXAxSho086mglNtPtmd0nzdK_7Zp_cqppX8hNOzzhWiFTm_stmn3NcGSHsC5CvM02iUEEReQQgTTXZxh1SCK71Yt1fGVpfYDwyTEmmeYrGItKvb7xoJPc3UqKThEtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOzehQTS3iZQWF-Oh-2MptIsB1W_DU6pQhAoAMcwjDnXOPGwwmUsstyWEv9W0kF7V2bGTFTfYFe8znudErm50-nCgEl5Ob-LHPjTMeKGbU0AHhiYzibfcmORTwczRDCYLUr_tjOEPYX_g80QqlBMqF8i2s9mEhtRW9RbItusnE-3Rl7nscZUpolh8MkIu_CTWEgcjsZ6V66QfRgpFoN-sFirgk4XeTEEldBpgsREKSVwAga483Snf-V7Z5nsK5YTR4ono0OK7nRtdiFz9QJYPmrv20PLN6vIYF8VthZZPG7JHQdgOhrjgokIn7_Auqe803s6RRXfhvvZtlPXG7mrPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تونی کروس: دراوج‌فوتبالم و درسن 34 سالگی خداحافظی کردم تامردم روزهای درخشانم رو از یاد نبرند. موندن نویر درفوتبال درسن40 سالگی نه تنها هیچ کمکی به تیمش نخواهد کرد بلکه باعث خواهد شد که مردم روزهای درخشانش رو از یاد ببرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24358" target="_blank">📅 11:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24357">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMmoWJHu3GVieNLVhPoR38WR6z_QfR9piXfEY0rqXyp2oD1vi9RSxKz2m_XMQ51oTkM7dEQjy9CAvYdLsVtGnORJFMa6oyKCmmD9mYYqbjExGwbdhU-Gp4sM94_ijR2shvesNPATFIEUkCVrODwTD7U5Mj0FgzsNvKxY_a9OdnOPCjiRJ4osH-wS3X6VMemNhvH0-LUdm0Vgo4zFMWAUukXUJW1S-J_YZ3f508TRo5o6Ml07b8mMgzmp2aQhbwn6vBUUVJ0r_Ve-ZTQhAtb0Q1eItJWT762bVgQ1OBO8n3WoL_0-mqyxe6rdbU08e7-by9zTpCtDLO5Sn5E63MyxGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الانگا بعدازمساوی‌سوئد باژاپن خیلی‌ناراحت بود و فکر میکرد صعود نمیکنن. بعد از بازی رفتن باهاش صحبت کردن گفتن آروم باش، صعود می‌کنیم. پاترم توکنفرانس گفت بهش گفته بودیم مساوی هم کافیه ولی یادش نبوده. بهرحال‌الان می‌دونه و خوشحاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24357" target="_blank">📅 11:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24356">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BanwbHmNxBxaPWHGBCGAsndXVYii8BsaZrTG4QnqfjNAaqkmN5xr_FDgVnkuR8P62-QC_4oI71P_nc-XMOFdEXa7l_uq7wif0UoJWIgoV12S_zecgRIOZPd2UVbqsN84a6mRr-fZY6bJzi-BqVJUDVFFF7evBtYZJ4AbQgZSC1gZxy8iEZg054u_sAxc9Fpv1mY8DaOzPQ7lizJFjQRgy9OyMHS1QRrm1zRBjMpLtrwTIfJK35J-GwLrodIXRY4nv54yvTF-gARs6u5f1qjPppkdwz_XXE9CdeJrCbG7LYY5GkTwCNOjBba6AaTfalt6IChnv4lgNv8Dap2NpSI-5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
ستارگان رئال مادرید؛ وینیسیوس، امباپه و بلینگهام در این جام‌جهانی در اوج آمادگی بوده اند و ۶ مورد از ۷ جایزه بهترین بازیکن زمین را برده اند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24356" target="_blank">📅 11:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24355">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jK7b_-B7pRpmWSCKJVOqmZmFD_2mQzI7Q1IgVvrnZ9Bjwq6UK1WJ0wO-H9kTMmuFlbbT-h6kgaSqrQYye7lhdFh8tzdAk9UXNC63EwWlg0tnZcAbGIkI_Y6JDYOdYZoXx7dH-yFO7FV1hpUxdp8WIW0I2euvNjGTyuA-mPx6OL53r0FWsNx44v0ACKbweBMuTiTIve4Z0Wyuv1Zz4UYYB1YZE5DDAIHsAchf3XZzC7Pg7mOu3J0eDv8RwRnwAHEDTYdhii07AOqn6Km0nI7bNk1q_owWsx2AiKCkIz8NE3nMkCBf2i4jC5Z7pAOF738Xnie4pD9ovXxHX24UNcKNkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ مبین دهقان هافبک میانی الوحده امارات از وضعیتش در این تیم رضایت ندارد و به‌دنبال بازگشت به لیگ برتره. دهقان فصل گذشته قبل از عقد قرارداد با الوحده در آستانه پیوستن‌به تیم پرسپولیس قرار داشت اما عدم توافق مالی دوباشگاه‌مانع…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24355" target="_blank">📅 10:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24354">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0e3e7e8d6.mp4?token=T7nMAk4osUhoLuSIP6R3MKqRAjbhBr_F-7dtThbk9wCobEqvqj7UjYWTjuIWOlnFOGwu2bX2I9vI5YnwCmsKdorC7pE02kO0UPAIfaZmxXmsFOwxPFPHO1vCUNgBCNkMJajHzIk8YGu9ye13i5Cx44TsaBw29OujZ_kb0H5BAttdbL66DyDk08Gq95o5uZv28H8gLcBMTNZ6_JsPefbKyT4CBcY1_5xk34jjIGC8Df2eZWh_lOjy_Io8pO1xljwW2ne6v_GOkqPpZd5w217YCDppS32XRdbIB2jDrA-y5ZTGbLSxbgnSILPLC8FDYk5skAqdKpiUMfUb4W6EiFhKbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0e3e7e8d6.mp4?token=T7nMAk4osUhoLuSIP6R3MKqRAjbhBr_F-7dtThbk9wCobEqvqj7UjYWTjuIWOlnFOGwu2bX2I9vI5YnwCmsKdorC7pE02kO0UPAIfaZmxXmsFOwxPFPHO1vCUNgBCNkMJajHzIk8YGu9ye13i5Cx44TsaBw29OujZ_kb0H5BAttdbL66DyDk08Gq95o5uZv28H8gLcBMTNZ6_JsPefbKyT4CBcY1_5xk34jjIGC8Df2eZWh_lOjy_Io8pO1xljwW2ne6v_GOkqPpZd5w217YCDppS32XRdbIB2jDrA-y5ZTGbLSxbgnSILPLC8FDYk5skAqdKpiUMfUb4W6EiFhKbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇪🇸
ژوزه‌مورینیو:
من دوست دارم بازیکنای رئال مادرید درجام‌جهانی ببازن و برگردن به تمرینات تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24354" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24353">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇵🇹
🇵🇹
سوپرگل دیدنی نونو مندس ستاره تیم ملی پرتغال دربازی‌مقابل ازبکستان رو از نگاهی متفاوت ببینید؛ همشون فکر کردن که رونالدو میخواد بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24353" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24351">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPvRO6A-v5_t8xoWxwAMa0vXe9AfT68lbI2TaE0F9VAXsLlJbcIsmZgCmcqTKIYYPbJ9OcaL3fT6AMDEDsgze6Td9Gf2LLc0fIJPZuGh1vXFn1ZUb-kLqTk-Z95IGsYZ8lbb0tS_-d92lFQlxS7l06-4JFJK9DACz0Ezlu7w5dMIY1qJjuDM7KU5CXeFloGQaNrgaJZbUntVceYXwGTeAU5gbVOQtpVx0SagWJoDr_TE0jVD8V8UHgR94zDtSnTImPoSzdpjnOI_6m-M2rP3bFMbaiuddNLzctqcOWS7FMTOp4FHYmCUv4lRFuB_wwKOieNG5ORBoijMquesz-Mi6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24351" target="_blank">📅 09:39 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
