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
<img src="https://cdn4.telesco.pe/file/OcA9oU9QPTndMhxsxWOTHCWJ3bZrVdUZ5TrO6Hw4XQysfrmOCnhntcXrMhTkC6Fl8wbodEgL7Y3hExvjtJQ7lbIqUG6pFNOmGNHc6XsEIAB4pwJ5O3BCBAt63X5crSFWwIYWVrRFSaqf4PpuTSsRWEoGEx_-a8P2_8Wds8A3i-NK-5PBaDrUfV_KgBRohoSK3jbOnushSuB2yj-7chp7JqIX5m1UtKsS27Xg7igjtHL3GTk3x8NdAkj3N63LukTd0Uiinz3lSpWvSq1BtPe_2RVkXQhkSs9DeIsSIHX_H76QA9UShyZEQgC3qSLJ2c4_TWAVajQQpAnGxH-QRHMDUg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 586K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 14:43:39</div>
<hr>

<div class="tg-post" id="msg-26542">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g36of68ua5lMn12R2QEpJJfcdDOlHb4evFa_8L8iawR4te7QfV79cHW4ThVM25d60DeY1jT-m4_bOf6pQH9A3xjdTK1UIOHopF3R8FqTycxLR2bni3F8vOX5oyNB0nk4Eb99Q0QpqEEkV8BleoeLazOkdGWMvGTFBxbjnvZH-lCqeQpVHWI2sCOIEhzgnEoMQCa7NXZnvEuXi8eEM6NdXSLxRAYIZqtIRKoJPBTFgBZhcV43ikPvS94tXLnE9utRfu7MYtTlwgmS-qnsR7YjaTTKXFDU5afFcemGwcVscNq5jbXC5TyXLkOdefCO0AXaKodfqqAN-CmFwTN8rlbTpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/persiana_Soccer/26542" target="_blank">📅 14:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26541">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8HVOEFgsqTdh6EGiGM0nhGO_JGjDm3vImg-gyyb8Ac5tAT1lw6x4Hgt9lDvltZxdufEy-0mro-E6gj6rUDvKhYMtTtUUtbGUddymyAMqIJzKpJOSWyDWsz6Fy5eyEc06DfveAuHknXY3UfI5cBfQ45u_YqA9t9K1ejwnhcPGMxgNOEgnXcZkJdLkADLyg2dJ3lax3wAhi_EXe4SInJ9fH3aAZ8-DgLeHzgAFP1ig-xcBNObUpatafKXkKQo3d6Dz0ZUc7tkciOtpTvgvFLc18g3sQJnthy7OTXPqZ1Nl3ypxI0bPpRirQZwR0lfnEfc7UxAFpIuKCb4_6YkR_FIAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌البانیایی‌تیم استقلال برای جلسه‌مهم با علی‌تاجرنیا رئیس هیات مدیره استقلال وارد ساختمان‌باشگاه‌شد. این جلسه مربوط به تمدید قرارداد این فوق ستاره آلبانیایی است و ممکن است همین امروز قرارداد آسانی سه ساله تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/26541" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26540">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myEUM4LfVoGAktSpz__EHsRUJGm-jbzTAeaCzIVL_kElalS6SI8qrXSGDalGv5XM76UaGtwqXiLeC_bcmB6JoffKHuoLINqAQ8H3OrF9bULvuOFK_eFibMsRWrakoX4ksok-f44RHDv3NBQanfGVrKDR6FhXXuVe2NsnrBp-nGpYuoihTyXS3iBs8WNSB3eonbMhB0D_v2DDsc57nsa6c4mHyrwN7-2Bne7gQTAb6-KuvxpfAHzEwjTPlRT564mftQ-QEAGKZYPkyh_5r_Uz734xacdV-nXhDpxZU_835oy2f_FNMlhTXQGXeiBvT3QmIOgprLUs5gyO2PgQ91zJhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق گفته رسانه‌های یونانی؛ مهدی طارمی مهاجم 34 ساله المپیاکوس در لیست مازاد این تیم قرار گرفته و باید تا میدون آزادی بدوعه برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/26540" target="_blank">📅 13:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26539">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn6a1eYzY7IAMvsK7-_3lQB8CDdM692rqGEBTMlN9MJrUBsqso91MPF_koMSl4Xm1kG1SuAkDBmSUMm_ISKCS7G0TtmF_XvBueiv5ACIzyn5RPy1ZYtv3edgv6sJGCD_na43TUosZmk3gc9IPLqpN3BrPuA-z8vmz8JmZ1x0Nmuc9kttU8SWXJagQS99HuIp5MryEmAp4Y6nFOTnFZilFlDDLNp7RiV0M8oiNarubpRhFjfvkL-28bAt_NG8AKjUoQj25uoySe4M3VJEKwq1dfqx8SOTGRti1T_H-SXqyaBPI-BTOYmf0TKPI5PKjqRRq7TGBKuremOmbUhQJtq1YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
مهدی طارمی: حالا که دیگه صعود نکردیم اصلا نباید سوار هواپیما بشیم و تا فرودگاه امام میدوییم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/26539" target="_blank">📅 12:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26537">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=uwKqCZ4HfuM-1Vvha_eX4JEMOdLMHTPatNwE6yBifbfS3lhCYqJA6NdILpk3CwWzTj4OE1bpZPjRGylhDVNYHyBSahdEqU4xF4SxdT_7gf-cNnF4bpglUfFohO2HR4pkbcPI9vYDg-Yc-G-CmsvHU34pf2wVKn9oReVCyYDV_1hoHP-b17sVfWRO4TLl9RkAPUrLixiBD9B6ZAq39KQ0xPFjk4J3mf_ijpR3FQuzTYbqt9hguyrA433Z3YvLtjentttnJYwCy5Tg0nPo6chTzYFEocYw_ZQ98RjTzS9cIWqQs6WhEA-kGLFBBxNHT5zUmbrQjAnAgAE3u8zvhlMjBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=uwKqCZ4HfuM-1Vvha_eX4JEMOdLMHTPatNwE6yBifbfS3lhCYqJA6NdILpk3CwWzTj4OE1bpZPjRGylhDVNYHyBSahdEqU4xF4SxdT_7gf-cNnF4bpglUfFohO2HR4pkbcPI9vYDg-Yc-G-CmsvHU34pf2wVKn9oReVCyYDV_1hoHP-b17sVfWRO4TLl9RkAPUrLixiBD9B6ZAq39KQ0xPFjk4J3mf_ijpR3FQuzTYbqt9hguyrA433Z3YvLtjentttnJYwCy5Tg0nPo6chTzYFEocYw_ZQ98RjTzS9cIWqQs6WhEA-kGLFBBxNHT5zUmbrQjAnAgAE3u8zvhlMjBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
فکر میکنی برگردون رونالدو جلو یوونتوس از برگردون تو بهتر بود؟ زلاتان ابراهیموویچ: اگه تو فاصله بیشتراز40متراز دروازه زده، آره بهتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/26537" target="_blank">📅 12:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26536">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYi1qd0y94-tUhZZ_LDlzg9JxOlwB2-qt09RFb0IR-L8r0CfMAl_bP4gObtynSDFG8totKzSTiVR6UTPWpm1aP0s60ZimT_Lv6JB3VJVJBrgxzIFUYGWLlWMD17PUcFfrOFMPqXm4PJqN2jBtz-PKZ_PKTRMRkxGaDsCpatbO0paljPn9aActhnAAI9txAJ4x8MjFvy4EvpjUaY6u5Ih_J8NY2_y6dm9RSfLfX9r-7kZiXVu3Txbrd9MhN2NhkafQN8gshh7pvxwtssnCgYMhPkTEM_lSgr18kotCvwMkwPIFPI169SoNqqc2jR5hUOPTSf9GKQVu2HiOcfhvU3O5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/26536" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26535">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuC6yZ90xYW_VDFyxdjZ_6EVQeoT1titII7-PxI3nCeaBrfiBRZuSKR6L2i5r-zOdUVxsLa2dlY7yj1gNWCb-mX8ohuc1wm7V6Wr53w5g6RTfKv2boGznc8Tdn4p-CHRvAgJ1jKV1J9VPku8f4zyfllVk_s9607WrgKYnwmhutBDdsODHk9vFJR8aV_BrrwNiLOY_V4wH5wHp-Sv1MjG8ZOmyha4XKY8QHc3hB5C3S5VYFFs2HnRBb--upnWj7Tdygwp061HPu4QAWJKC0rpVV8CVjsQI58FIz_qL8Zx5h1bvWmuCxyLGtQzW_tTBHFTDT4r09ZJw8_TW3myefXafQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سعید آقایی مدافع چپ 31 ساله سپاهان و پرسپولیس برای عقد قرارداد دو ساله با مدیریت تیم فجرسپاسی به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/26535" target="_blank">📅 11:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26533">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f10IkFTZeAnG0mQW9KqpyZWCcyHI557L3hPbGBSpdaL0hB8Xs5W1KzTb8jvqEfqx4ayPhp9YjkZLSSgHXJt2X3nA1xxL6t2hHmLhraFTkc4131Cv_Xo1HsiWTJX3m02l0-OzYYOnW0wiInvXosq-RQJX4odDkbsx7WvXhtUYVIhGr_lj-FVN81zFz8_zweL9A60905vC_9gdTw-KLBBcL-OAY2GGoQ8bny1XoGk9ExIGXKfkM_Eh5f0N07a0SRZrWc-W4WL3aKDVGFKffwu0BURKJHFnleX0F4svzOnneB70jByud3cySovsdaPJgLHjPdjZHF1gqbFrogGaNj9U9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مصوبات جدید سازمان لیگ فوتبال در مورد نقل و انتقالات در فصل آینده رقابت‌های لیگ‌برتر:
‼️
افزایش لیست بزرگسالان هر تیم‌لیگ‌برتری از 20 بازیکن به 21 بازیکن؛ افزایش لیست زیر 25 سال هر تیم از دو بازیکن به پنج بازیکن؛ افزایش سهیمه لیگ برتری هرتیم‌از 7 بازیکن…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/26533" target="_blank">📅 10:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26532">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4_2XYAWcZ6-9bsLS50OGFaaQVpEr_QXGe4L8djHhp5jf49KotNjj3xlOb6aduNSfalLai7VfNg9FGXO8d7LTdfqUOVR7MQNBHC7b3MKYsdbX5-Jovz8zNkzvttgcw48R8Xp_aGzlXXFSL71n__COuGxuaoJgPVNafELt2x72N1PgBl31GSLxnXmcygMDNCD4gT-vS7bzfjONF7xeBq0vbaavsGckLG5b2BtZQq5uxHCFVfK8D6QotcIC0NXMlMlcRCJR90SwT_i8PKHiAdR5joMneqft86RJrDtDtY5DQP_jDfTiS_7fgo4EoUhhNTtLG-rvCLfWbupjGu538cmaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/26532" target="_blank">📅 10:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26531">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWwuJTUf98mouHzKY_GVZ_-IvaWVMs5S6bE1iYKjUi1qulLhdGtkLmz7vmIycghjTBAt2tZNIRYx6PeHcbyHAPO32Fu0X81Q56qqGpJuQMk8EiLnq8NRevfwJbVTAsnm58pPVeY5EhKVW_rz19BwPhYV7HCIFkuFILbgGuuG4FrdHvs2Ex8JEz-DdcSL5mXqu1dumDlDUM9H_MwGgKekjjAW-iH5_vPHZOXyeKV_tQHzWWjhS_zIj6UO1pe8kwEbLVBTWCZYq8A3GYupmYG0XFnCsj60NYrLbByMkPKwdqD_fgTF1TFHFlf_Vmf5aZ5gwuk4DSytooypq_pKAPAnSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه‌بدونید بعداز زلزله ویرانگر بم، باشگاه رئال مادرید اونجایه‌مدرسه‌فوتبال‌تاسیس کرد، استادیوم و مجوعه ورزشی ساخت و درنهایت بخاطر فساد و پارتی‌بازی‌مسئولین و فرزندانشون داخل این مدرسه فوتبال، کلا منحل شد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/26531" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26529">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=LwxnxGFrKzPXjFJNzA-PaFTGSEOmfz9TKivi64Hh8yK2SsH_4qqP9b5P7aevZJat5igMqvQeDkteeH-PT-LGnL5Z_ElebWotjzX707UwFawZLBu8MJ-_dZDnpLjVNMQyoMuZM5Y-lPHjI3_82PZJ6dwGcOt6P63ImnyA7jBmdTKB3pJHPTVPvm_2G4BOlmvAm4x7HnaGCtvrC2C-PNTUUCTuPpD3Ahhjv3QQ-Ad9wW9jmb-IBv-EOR4biL9EwpnvhAXvE-3Soq9dGwOtry4UXSZWYYXutDhSkvrkf_7hlvN63loU2CuWjrsVvHnk38OHOYf6DQiuyWInCMKN9pm-NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=LwxnxGFrKzPXjFJNzA-PaFTGSEOmfz9TKivi64Hh8yK2SsH_4qqP9b5P7aevZJat5igMqvQeDkteeH-PT-LGnL5Z_ElebWotjzX707UwFawZLBu8MJ-_dZDnpLjVNMQyoMuZM5Y-lPHjI3_82PZJ6dwGcOt6P63ImnyA7jBmdTKB3pJHPTVPvm_2G4BOlmvAm4x7HnaGCtvrC2C-PNTUUCTuPpD3Ahhjv3QQ-Ad9wW9jmb-IBv-EOR4biL9EwpnvhAXvE-3Soq9dGwOtry4UXSZWYYXutDhSkvrkf_7hlvN63loU2CuWjrsVvHnk38OHOYf6DQiuyWInCMKN9pm-NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی نوستالژی و خاطره انگیز از تقابل جذاب نیمار نوجوان مقابل رونالدینیو در لیگ سری‌آ برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/26529" target="_blank">📅 07:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26528">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9X6gOLn6kpt-86pKG3WWbLK13wG3ZgGS96-El9WGsaMYr8P9QLLdEm0wnIQ7OCBBUF4IcVCnobRkrk--nnCfOZ7pUKLJy7OOyfGWGXCf1cgJh1tmNeyBn8q5qgvXwVc5qMozy4PxaxoahnDV_kL767V62-sfbR15fjjqupi3t0B1RQtO_fPAVJZo6E9DM2Wtci4S4UDtnLzC_a3m4FCxLHHYAmNt35x39K4p9OPv7B-11H34jOKNEmH2bdtMgmOVpooV5m66Auby57VoEEXfAiguMrmZRRjySTt29BzzZvfYoPPcrfsSVdLM5UpHsHWK6_qFG4ddSQ02rXiDHyjmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26528" target="_blank">📅 01:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26526">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWW3GF9MWkjS4dPreOUBx3gyp2rJh2CzbvbykEucx6f0A-u7dfDf2HYgelLMODa5kOl9GN2Kkngkx659mMVty18KZH_eLmNd-FoeofBQ5a-fFATsJI5d3GcBNEp0AfOHnDQ_KchmsepeEzIJZLOxAKGX4q5IcaGSoA3Lq_AAtLc7csaRnDbVr9NSzXIFoGo_PmpZkKs8PN97X4LGFZagM7r3HzhTd7My0wVCdT7dCCi4I2bJ2-fokuNX4336z-0uo63zBjS90wDSybWzuPyBi4qgJW1lmvMrM10r0U6PW32E9hYvTrh-O2npUE-GdYM5BsCneJ8pFdwCHDAUN6vOXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ جذاب دیدارها‌ی‌‌ امروز؛
مصاف تدارکاتی شاگردان آندونی ایرائولا برابر ساندرلند در آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26526" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26525">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlbe0LozYbzoGYxo9d4gxRQOpFnISs5buboi1oDCcjGE48dy6ZWtxQzX83uqYKXAsQqfaRxDLYdltci9_-AlIt4b3nCtiqrYligbIxijkIbOq3JGu0ETY24fev23-sGKJtYfebJF8bLjIk-3M7MVR9B_JQl9iBskfp9o0F9XBEsph14KG7mXZEpAj9jyY3S41_EtIwkSgtvpQbHbqghMQwysCcyDoqtpGi-vUqO3U8KTktJev1HLQHsJaAn0HwaY_tKtlO7U0koYjI1465uvCMFP-aveujf1-akagHoBbYiS_fTYWeRYCYLmhmQIfhX5pxjOZzv3hLcQF9ADu-XQpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
توقف روسونری مقابل سلتیک و برتری‌ماخاچ‌قلعه‌درحضورکوتاه‌ حسین‌نژاد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26525" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26524">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvQ5Gz_3tBlyImysuBTtGrz0h4qzim1kQZNHfN187S_07R4Deb0Y1snYQ6WKKpP9OS4LQBIPoh-0xTZ593bOfFfmA5CfFG3YBvyLvfoLZsaCujC_K1Qh9KXDeuW_6V2D6tVqAXlvh9jfIGXuGb3_vIs9nwifRgE2Qd2xYOwbz2A6gaTJnXs_DSJdlKiph8o_GCsJZ3d7aoPMpS8gkKrd3kk_e1xnHdbIfsz4K1EiEWty9EdYfCkACezl8_BlRZhwAc4yDce52uLLURhwys-0Qj9LY1etS3WZ8ExFEaY5qTWiuVt5PbSGN5bQQVW8xEOhlzTSgsW1x5mu89aBuk9oxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26524" target="_blank">📅 01:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26523">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgWqhqSaGo-LfI3qw5FM6-oJ-nQkrqvzt0vB_9qnnwVzpwAZ8YVB2U-Zp-jNP1j6UvXhIFgiH6hNQETBwrmEMHiA8ENYPDljpmVi2RtAXRDd9OvIXBvC2AYYF6ozxkwID5BlswDCt2hVg9ETWMxUJz3VczYnlS4DLJ_iXcTnTs0bAtZhn3jyQWbTf9X4vXn7F4pCBXi0Cetz-C8K__TV4djt6hs-yfS-37X1c9Z0tjkz_FaVnq0yQ4I4yOnX7SZJrfs4qgAM1WdgKMfX944M4JuHY3sPUO-qcSRnRYShHVQ_AlRu5TwDkLHm1Sq4B55149VTMFwhpzt8rfsioo_Lew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
یکی‌از مسئولان سازمان لیگ؛ خبر فسخ قرار داد رامین رضاییان با باشگاه در سازمان لیگ رو تایید کرد. بدین ترتیب اگه پنجره باز نشود و رامین بخواهد قرارداد جدیدی با تیم استقلال امضا کند تا نیم فصل مجوز بازی برای آبی پوشان پایتخت نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26523" target="_blank">📅 01:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26522">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9gPe1-SD9TcaKDeboOb-ZCmQdBISlIC-en0zloiPu4Le8xW-NOxTh0NroLnSy5dUa_QmFariyrQKctyzPSQBoDkwuTViFmPhPaVX-4wjBE_ugWplrwfKjQWChAaRWUivTpNI7DmUBak-7mmNK_3vAfBb18fmHPqXwIQ3ZFTnj2gzztUv6g-Nldtj_wJPLcFJnB1VgC3HZgqSDMofPMca5KqxFHi-M9FfzEIEifvABDdiCbppRZb-Vzx_4bjzBPcdxTGyGNO34AgZweH8kf46Pi6SykBzisSKjJrKD-6gt-xgQz4I02A-bEkD3c4ktaj_0VUTGiAXpwt36swDBoPpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#تکمیلی؛ خب دیگه تمومه رومانو هم تایید کرد؛ یان دیومانده 19 ساله با قراردادی شش ساله به رئال‌مادرید پیوست. پرز قراره بزودی پول رو بزنه به حساب باشگاه لایپزیگ و این انتقال رسمی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26522" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26521">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34e9fb51c.mp4?token=uIPzfpxm1PWNsPu79RRefZHyZC8CcVv1vLiZBbJEeTYAtm6AB0Kml8cG3DB6fzEJ6pPsg4HrN-fxKwQzJ4ETgT-aAt5-v3u_JJn6xgUIehT3JS6Nj4wYIDg4Utrtj_RdOS-RcT67t37GKxwrgLqMgNBjxQNerkwJ9vMqhvIU9Ekh_GdntNWIbR7iecQMEfmkn-uKtTzcu5YyI2xxgU2eEbHEEtQwt3hRz5LtoL8kOgvxoi8Zh71hzEZjx-maQ2JBlxUYCjWkbVF7tYW55i2DUa7zb4xQaMoqnbrbcne8cPPFtdlt3Zur4zIfU4SSaANceT2HaWo8lX3_k1MTkMEeVjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34e9fb51c.mp4?token=uIPzfpxm1PWNsPu79RRefZHyZC8CcVv1vLiZBbJEeTYAtm6AB0Kml8cG3DB6fzEJ6pPsg4HrN-fxKwQzJ4ETgT-aAt5-v3u_JJn6xgUIehT3JS6Nj4wYIDg4Utrtj_RdOS-RcT67t37GKxwrgLqMgNBjxQNerkwJ9vMqhvIU9Ekh_GdntNWIbR7iecQMEfmkn-uKtTzcu5YyI2xxgU2eEbHEEtQwt3hRz5LtoL8kOgvxoi8Zh71hzEZjx-maQ2JBlxUYCjWkbVF7tYW55i2DUa7zb4xQaMoqnbrbcne8cPPFtdlt3Zur4zIfU4SSaANceT2HaWo8lX3_k1MTkMEeVjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26521" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26519">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aidk2iBT0I0yxrZeTc4IfHGIPV_cUMRVrewmJlYM07zj0iczcRISIFowSTK1d15pACP9i0MRyIRQc383fShyZoPfhLTTNrRsTnAHZxtMGh9pqzrjdGkKPYdN9a-OARCt95NWwWLJL6EXMWNcX-5WDQ5AOnuoOuZLHSYuYOyptusYKeC6MBG2XjpDCwO5bhi81gZUi5F8V2QAD8OXnFot1Xjya5Ktozusd1NKk3YOEGzcVRmoj9wRPowi3NvdMRRU42XJ_vnp6yxCu83iPYcGCqtXAgRqeFG_NswpEfzxL5_uIulk1d9BbOHgINGdLjI2oWizFYOhDmgb2xpRIeie_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛بعداز رونمایی‌از محمد خلیفه؛ اگر اتفاق‌خاصی‌ رخ ندهد باشگاه‌ استقلال کار های انتقال مهدی گودرزی ستاره جوان خیبر هم نهایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26519" target="_blank">📅 00:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26518">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuW2fPiJ33hgQFWZzkSRbl0DHaQdIyxjMVCvsKkGArrq9n15FecW4i_7AG9WsV6iSR-Say0vEbaoMLEoJ3TrKVkaYZWQctC93VnJmmvzeqpnJXggDel_nKbLx5TqZ4hfdl9WOjjHhC0KFoNQwTIdWxMckq5qrcG2wdg6MiM_iN8iE8YMLYpshrNce7hmCH1Pz44TamzDYJY3RSakElU-ySz7vtWzBkcZK4wqiMcClcyvymC6-mu4d2061gzxqSczgLXtBxzFQF1q2kR8Q45gKDnuT25F4OBO56lpiw1onNUndihjnt63efG9mpWMAWP_dHi0TYqP3dnEFtffBlwmjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رونالدو و جورجینا هم به این‌شکل در تدارک گرفتن عروسیشون هستند؛ این چه سمی بود اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26518" target="_blank">📅 00:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26517">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDBAcHEqAo91YxDi238AxWj_twwFPZjsQ8lQlbO0MGuUQ5WB6S4IA_c1lJDyxKQoLPNrPM8FD6QcG9Gl23xvtlgoPzmDXO3kWqBGJefXHI1sblCjukph675nZNlcxPZH34dtQv4sAxgHUjnOpIDmCnCA5eR4FgWzfQKaiL5VerT8dSJYUiMGtHSVP5kZ1W-IikB6GsSdYpj0JL7zvV6tSUnmRdYO6F52gdXf6jEogJApu2M422LqTEu5pqP_LrMoHYxb0PkxpUkH_bIO-QQ31Ql9Ve0Nudt0TZIK6xksxlXRzkKgQLWRh98_aZNJPKsfWH5IID3dVf4dQ2X15CxCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌ازدقایقی‌قبل‌با مدیربرنامه محمد مهدی محبی و خودِ بازیکن تماس گرفته و در تلاشه که زودتر این بازیکن قرارداد رو امضا کند. به محض امضای محبی در کانال خواهیم گفت. دو تیم پرسپولیس و اتحاد کلبا بر سر این انتقال به توافق رسیده اند و فقط امضا محبی…</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26517" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26516">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAMgDTbw4OJ_rFYZiZeDAZSsS3xfc5HWGNV3GvC3Qo-mZrT3BMPOUFkkxIjsn7jBPWdJha2bahi7qC8SRB1s4hut5daQ03IjF3jl33fx4FMEZ-v-R93eslrHFMRMkE-RJm6m4SJoWkQwOZWaO87IPmUui9k1tNTpX5BPh71V_opTa7TAua27LhFOLa_ghDXlEXOog_Jl7VSV8fQneNB23c_DIFf6sgnzUFdM-zbGoxeYZh7slgBNOPa4fjjKU4Vv7hDYNEE-CGTcSve6vCGmgiqwB69gJpU9ggHrRI6kP1K7Cfexqf7PRUoJZ-507-xd0xXtZVGbck8xwSlAfa3GPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
"هبا عبوک" اکس اشرف حکیمی که دنبال ثروت اشرف بود و بعدفهمید که همه چیز بنام مادرشه، بایک‌شاهزاده قطری که 2 میلیارد دلار ثروت‌داره رسماواردرابطه شده. هبا و شاهزاده تو جریان جام جهانی 2022 با هم آشنا شدند، زمانی که هبا هنوز همسر اشرف بود هم دنبال ثروت اشرف…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26516" target="_blank">📅 23:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26515">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUQ1qCL8jNAG744ZxELh92aMe4P9L97d6vrzk2SHkvtLb_bIfYU10jheDbZkOglF1oryquX4NcFVXsgn_eu2A-rOi82lwOFvBl6y8u2Y7wktsVD1SEZvMD-64C64_X8A60KtB1HRYYblgAFfVHFRH48lGpeDitfnrI5ZDhsPhH2Y9wjv7TukNd_S8Z_SB7DDtmLzIFdbROZLij3HNzEHJVjhSZWqYBD8GzggNml1SWYOomKCFYTHx8WQxVL32D34ULL_IoefNxw1LJT0BsJCEBV4kexXjnt9hLUVX1TBvzgZyESBGnx9QySAUjKdurUxh3LRnvAo0wOxBPVVtcVOHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی:
باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26515" target="_blank">📅 23:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26514">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5E7eNKT2qIVvi5dNfSDtnp1NXaWvAZNlGr2wWg8HXRpNAIWgf8tyvr4irtG0B-EgeVillD1R44ic8r-I6EfeIQ4pRzT4Ph7bma--ea6z3UP2BTjTcVT1dACLZhb2ZQCrjs-lGm4_IAq9tM5tabNVkJe-Mf367vwLtgeh2sgD-cd66YN7cY-PCREsB49IPA6YavucuPvidsM9Xn16vsgwpuYELpIbebq_5bsZybs_4V6JxvSwz5AjkKsiFjlXnPDrlgcfYjRpBLYXe6JRBCFbo3YX19H8oIOy_KWKaAmuyHJ1GWOoO359Sdrfeu6tukJ4iv36RnFS5dSc-KSfpR3pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#فوری؛ نشریه ESPN: یان دیومانده ستاره 19 ساله تیم لایپزیگ باعقدقراردادی شش ساله رسما به باشگاه رئال مادرید پیوست. باشگاه بزودی پوستر رونمایی از وینگر جدید خود را منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26514" target="_blank">📅 22:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26513">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TP8M7Vcvku3y7fOzIMpxkxrNlA1HPNR_K6O4aC0Ze4ZhomBBMNBo38kh-0r-uC2apfFc4KnZlDYFTkmKj-3jEYC4BwMBboc4-skTmmE_mZ5GAV_7SZYpx-IPdhtCxCbP1y9NHxrrKEKLPoHsLttJohXuCbStkEFz9t01vpLYLk-JQTOv3XywWh9EhJeCNOTqSiiAh-xveCoIFKW3fA8LfKS4mob9fYELr_wykPRrVEnrKiXPoXC14fvkdgQUwAT8yekypa1f6E6LlXltXikTguheQIYSPzsh-Lg5cExzQ46nIMd-GI-YzRZxI8KhM0T679wGr6kNXgEeV9yEcIv3-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین پیگیری‌ های پرشیانا؛ قراره که امشب حدود ساعت 23:00 محمد محبی قراردادش رو با پرسپولیس امضا کنه و رسما پرسپولیسی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/26513" target="_blank">📅 22:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26512">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t38KPbavUbvzIRjEkIhTFQkYwzTU622JmZWR2iBu3KKxp3en7DQbbEiuWFzF0cPV6PmKRTICF6ARmK5Hk8aLNVpOs1ayxVFh-p8ZPpOAB3Egi9belCIfvlLhwNEg6_pCWkYoLVcpcr6nPbFCZTVhiDJcSXl4NEihL4Z5G0S1kjTLDKEKGFxNasvGToxuauq--L8kr4OMdjKEsCfdPdjjbvjlWDg41UViG2-RH-seDL6ttBi2UhJJxVMhYil17qZLWXM_8c70AtENTqcwlW7em7JGv6qWxDjnF4mU5rV18gC6c5Rj_4jc7An0v1Hy8gltGmzsug5dhpPZV_f7B1W8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال ایران عالیه؛ مدیریت گل گهر ساعت 2 با جواد نکونام جلسه داشتند، ساعت پنج به سید مهدی رحمتی زنگ زدندکه‌بیاد داخل جلسه، چند دیقه پیش هم خبرش‌اومدکه‌با رحمتی 3 ساله بستن تموم شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/26512" target="_blank">📅 22:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26511">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmOaMaI_EGthyf3RM6rUWLPtBAjlt9_F-XHgiQTpJyAlB1Vg84iASYe1PCM9Ed3PGlUmhdbT3igYKInPvlH7HB5nt74lri1oLA12AkLFzB46eZgBQMqy_l0-4TnL0mGuUYbndmeg5_J1o9L9bZkwWpcxfIY8zWrsFNzC5zK3XtUNqKqrw-Fk0HbseHLpD3yvfGp7nBfUhP_iEFHDpJ32kIL5pvRpk6mDOKiX5r7EbeCuh66az43xcceG35fX3jlmqP1O3Hx2EqSIC7fjMvb_mzZKXdBD_4sUBLyBW8O8ul72ec1Z3CBiqa_DARD6a2MxqhCcx_-l4nTAzaoD_ZzOnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/26511" target="_blank">📅 21:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26510">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtquUy-R6ikFIqINgrFGk4ugVCXU0snt0ILpTL7YKNF38LHK2y7jJwHLqojl3EYhKD_VtrFbROWE6GTkFjsEmFKd3Z_KGTJtUgZzHXzC8W0lU8Qejfp_ixftLkEu0bQYd5bZpaJWYT_UZrTCNQ_pumhaELv7h_SZFd6dvzbuiANFFg5cvyny3BsBXOO-bMo7pV7LbVqKc1puWcLbqLNTR1sh1UezaAPQCF7ZSjGzOdoTf-W4_w8HFhaXarxMMbTKFQBsJumc2Plmud0PbkwTeMsDT2P5nSMz1GlyzGflUbZsGqhiqUKCUTkDEPxG-wR7p0EH6aNjcXj9zMpw3RZsgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26510" target="_blank">📅 21:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26509">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2mrS9euB5MEqseVRIFkiKrp3GP58-oE9b5vk0B96dqsdQGq186oqaz8fHFsiTSxSwvNWdn9HPScxOOBJIzWruBTIcXRbThH9iVbAkY1eEtvdKIVHFh2dOHhCjFMnzliK5Mz6HbtoJnbgf1_qsAibV0DwlDyYeGyj50dZsd231Wz9yP2xwX109p2igMoeb6wQO_FZGg3r0Or099s7BGkiOUYnJJJ2e5DbbuBOnttVltGEi4rV61jYlXpx1VuE4oJpyKG7KsMs-1_Moc6a8-93kk8oTRjpX27un19hcUWe9iaZuUEQV5NeBmbXtNyNwHoIJ8QvZTISH-IkDsbhDgeVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/26509" target="_blank">📅 21:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26508">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S00gYz_2hc7mnR8S-ArDgrvk7aCir0s5KgIJJID-azVMDPb-RqUK741LSUYywd2ZORn_IMjQ8w_EIo8ehu9-X_EuHgD2Zub7BxOF99ZKYlZkVLZGv_4iJJqJnK4AVUkmug-6K4y1y0BG8F6FALbdfV951X_DhsMHRjkHNY_0dMcw66GUi1c90RQE9TWQEogH43_hxc4xzI6lhnDSHyb2hxi_VKng1WUymd4ELZnrFOK_bRx5g1Ta1aZhcQX12dGw8Ffd7ncu9Hzs8A5a6xwrcw679Rq7uftVcQy63JCaXlAlPkYGPuBPUhS2sVxFX06KrE6wu7W8QcwLkNbUG1QIpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای دیومانده بازیکن جدید رئال‌ مادرید هم مثل عثمان دمبله قبلا یه مصاحبه اسیدی کرده: الگوی من رونالدو عه؛ خبرنگار: مسی یا رونالدو؟ قطعا مسی!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/26508" target="_blank">📅 21:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26507">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smz0PI0c5HKvLc7bO4R5RJvg56gs5sicfisVgEmIllco5AjOGrPJ-GgZY-8_Ce2KxfYkwnU06Oq2Ul-PvYz1VATLfdLzt6nO8oxeeKcGCYPJr3RGxeWNbVENLVJ3fYik10a6uUC7k37nX8uRNFPWC74bS4Tqm58Ycm1xpgxUObiKPmM32WaJC0ew7pWSy5JsqJk9eWVovRDtgRVM424-rMMCyUSKdW2q0eizwh2GXXMcXbhaUgGnz_2kyAwrAyT1Qs3pZG_TdrAb8TYmhX0TN5-ZmcdKqAzxLMAjSl9LI66mZUX45hpK5-kIEC2Jg7CafhuoB6FN-AJsueJp8dO6bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخ آغاز رقابت‌های فصل‌جدید پنج لیگ معتبر اروپایی؛ تنها سه هفته تا شروع لالیگای اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26507" target="_blank">📅 21:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26506">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qqyf4EKDs4MqWd5WzfZdW3W5vcYrOgp-yxlUuCC3z2eXaNC7-chpa4_4rOhSZZgfof1TDYHJXooQEg5w08Pz0SK3SqhTwU7LnJoa5L2j_ck16xxpLygYUmVUjOFI_IR-5G3RSM4VHxXv2HbMxsFVZXMSZ9DIqjFKAx0PeNyr_OqKsvyHAtzahsu6CYX7DtK13TQT_MTqKP7fgPYmxLJU8Bso0cH_r4E-Po9qE-IHa3QhkVbfTkGcLhmLJamynyGDgteVjhZ7YoIbpLtwdECIDXqfVuDWuAVyMSeUMYz0gtFXcNnVi4GaeFanLxlK7p7MZSLjy8aouYNawdQMAywdnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسکای‌اسپورت: کارانتقال یان دیومانده به رئال مادرید نهایی شده و طی ساعات آینده کهکشانی‌ ها 115 میلیون یورو به تیم لایپزیگ پرداخت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26506" target="_blank">📅 20:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26505">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPiceNX24zIfDyOTcRAgQBWGyjm2ST27dDCR_H3ayuYafJv2L0xxUZRbo_d6QbVZn9u5oAlEBkHksbRBA6VoZoJMh_Mw6Rjw3V7FZhgF7FbTMpXJV7094xdUlAKDnbY3CEW55HD5lKj2wobThicvDx3FQ0bgQAIK08JBop_zZQt2-1r1rUc6J-TZd7hIk8Y11xLxt9gnTHMyvONPmISUX-uUqwbl5DUL0n5uHnSrOMb92wUA7rDTRU7SkvjCFzihFONZEcIQsWUWrLg48-qFGap8HpfmWJg0tf5iXkW-DABgh14vohGA1MftNvgZD7DTM0wmwK3j_BLOSz8n6RFa8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26505" target="_blank">📅 20:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26504">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rarU7zf1yAvDCRZjbQ7Ne17MZSoNp42bxNtFVWr_xYFAO7UQ9xrH8NwzMUehY92crbQxTCD9tZv7Kp4_Ug9y3rRQmpzffp3QBkFePXFJdNhCpr90NJP24KfeVpIb-L6pZuQeAqXCN6EZ89rzAqTV8i6mTPHJZ4hlKElGFBRmBTFa3N2HVxRM-4b8fQSnEqYhIvPB3xps1ICTeaQtZC0Xfo-_OoyvDtNxprgP-LA8UeodfK4EdmM3ykyH3kUzVyRiAGg16DPxXRzCe63SgoSxih50cCEHTORTApEnIaKhM0tkqsX0t3DT-IUuoWlYh7mWJdKhHxE7CUpdqYY_qGA4vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/persiana_Soccer/26504" target="_blank">📅 20:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26503">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HN6j_B590iqREK5-qNI_jn3wGrn9JyJRFCpPF0EvzUSbvM5cToDLc6vZusSa3kGW0pR1SOs6liMSjvq6fHayI1zdDmsEfvzHWdmieWF7Nzda-7WPpmwjoD8AZQ1BLqfg-6YGfT4VkWD459MP65KJ_7soXdU6h0FpoWnxsXZx2uhHuGupaEPXjpy-tP50qwTDTaPnnoYjcyqL42LbKl1O5AGA6De0J1WzVvG39ZH8Xe8h4ut1XVxB91Fbf4HJpDTkEUk2LJGfPK9oeZcPhqNfeYjYfUWFBHT44BvDlP__5A43aBr22OfodhGnTQgqS4tkAJydh6Hu6mOZJh76lEZ0nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/26503" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26502">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=JRAQuOFONB6tWbwU7kAfc-bnKt6MFzTORu7GPiTeuNHDBFQFeY9IOkoBVyx092PjbCV7aO-IpVHE3fA7y2H3D_w3onqrWYd2uzjPEBdvu8eX1SxJKGEaG2QXKFm7dfqKsq3H0lXjzudGGb_bk3yRWkJ3YRxfNU0LFGrWTwdpLQqaYXvDbDGYxb3ECejSEu5UdJghvrVLL0rBmwk53Lt3KuL_cN0_Ub_h3fjROczF9-dTMY-hlMedEdDv0jUrwy46K5lWKiDwTH7AhzEPhPM9SedI51RPpzBLQpDaUgnaicB6GthPw1kLOCcbfB1dFDOkdwfu2vuAJaKAgkFyxeeVtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=JRAQuOFONB6tWbwU7kAfc-bnKt6MFzTORu7GPiTeuNHDBFQFeY9IOkoBVyx092PjbCV7aO-IpVHE3fA7y2H3D_w3onqrWYd2uzjPEBdvu8eX1SxJKGEaG2QXKFm7dfqKsq3H0lXjzudGGb_bk3yRWkJ3YRxfNU0LFGrWTwdpLQqaYXvDbDGYxb3ECejSEu5UdJghvrVLL0rBmwk53Lt3KuL_cN0_Ub_h3fjROczF9-dTMY-hlMedEdDv0jUrwy46K5lWKiDwTH7AhzEPhPM9SedI51RPpzBLQpDaUgnaicB6GthPw1kLOCcbfB1dFDOkdwfu2vuAJaKAgkFyxeeVtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26502" target="_blank">📅 20:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26501">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iy64FGMCR0OMFK8MoE8bLxm77OGaQfm-oUZKkV5MO-3ytpCaN4Gt2H8b2YvpqPYQmUzbOS1tqohgYihfPg9Z2hxqpka5JQ8J7p_2NTm0-1u-vYriovzPDFbPa-SSac59XxtwS5YQs3aRJYNLTMO7oib_7O-Dus2jOKxsykmbUIfrTdjJ5G4qR6ZN4re1dovAb95KAAtl_E1VV8nhLJRfEOxd8vJlzwoas1gMIaM74cEIfP5HFUpI0Zsz1OWTGoHf-nfRNb_odxdJmD1tPhGo2T8IfZ9GoCvssEVd58veuFyYHuxOuFGcLSZPIY1FKCpReHc9tPjqjWj1_svAf_an1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ یاسر آسانی دقایقی قبل برای‌دریافت مطالباتش و مذاکره با آبی‌ها برای تمدید قراردادش وارد ساختمان این باشگاه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/26501" target="_blank">📅 19:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26499">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8lg0Rd4Rv6igXhaN6fvzTrXJz7YOwU3J2G64CiDKoBAewxs0Z4maYknIZ8e7h8bPavM5YIPQPv23I_vpqxYIwh7V2bZuoynB2B7dEla0nmO6yPVlB0-F9zwYBdCnXDTgeW5M6RAF7QO_4sWcPLqc-hsu53LtXXK3EhGwVma2EV5GjdThuL8g2-vswJWMDV2R5vz1aUTa14LhxrGTCTa-3dzwwEBeD2SGwKrqRHv94DZ9dXeCvppGKk0BmRPzGZkhoYpYNSAhNZ0yv25V_xpmVQ-fmnz_ZKtKQWp8b-VzGrSeNyLKCvy-yAsaI1zLHrmYaKl_zmG8UyFMcbOLeqFiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#اختصاصی‌پرشیانا #فوری؛رونمایی از تنها آفر اروپایی‌فعلی محمد محبی ستاره تیم ملی ایران
🔵
باشگاه لخ پوزنان سه روز پیش آفری دو ساله به ارزش 1.8 میلیون‌دلار به محمدمحبی داده. رقمی که برای هر فصل 900 هزار دلار به‌ شمار می‌آید. باشگاه استقلال نیز آفری‌سه‌ساله…</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/persiana_Soccer/26499" target="_blank">📅 19:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26498">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujP6i54xA_dqwHrwqePbYNfxCNzKrztmnYrVLjnBJ93Y2qPUcaiO9VSbAFpFu_9iEuE2Yu00F-5EjwYOutps-1jU2ePXCPf8Q7sfBuiwalca5TryAKdc_1_60wxTZXRHK0-9pCdgk02Wu2iZWqacMFJTfcEKYgjCNiNoQrYnXMuTPFDDz0TeIBMYp12rOcmrjgosGSk8GoBUQ-uervfqF4CcKA-H8V7wTvAJRcG0_iig4HZevMS6jFi_q6oCPV2Kt-5qcaPkFMxslP2iIbrsO3t725uOvTuuYyYFfWEHLFhRIwmm5y9qPF1_AkE1CJMYMK4OZBz8maJQ2RBVepx11w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/persiana_Soccer/26498" target="_blank">📅 18:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26497">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=iSn1WxMoQgu-gNgsOZw9xUprBNBgLKYJScLyhB2_pe3WEwcO35g_MhR9S9t9akO_WRxYu0ojYkdnCKjfWUNctqQBkBGK-ifgrknh99yuzpkBUv8_KYeaNVgLqbfTyW5VEVQ45Vzm3CT00sPm81iONgUTJ0RoF3B_OB9VTSozXI-U3K5i-jWtkaI_N9ciKKrow3wuuUX2mTKuGKw1y0stQUEvTYw0B6mU4w-u-aWMThZtR83_dEQhBFQ1Vk5Jde7i8zLBPVAvMKkJ4FGSFZT1cf-8cruWWZeLfi_1hEmBrRygLJOUWoQM6h6HdEp8ZUJ4CfUJ7sKziDD1ALDTchM8SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=iSn1WxMoQgu-gNgsOZw9xUprBNBgLKYJScLyhB2_pe3WEwcO35g_MhR9S9t9akO_WRxYu0ojYkdnCKjfWUNctqQBkBGK-ifgrknh99yuzpkBUv8_KYeaNVgLqbfTyW5VEVQ45Vzm3CT00sPm81iONgUTJ0RoF3B_OB9VTSozXI-U3K5i-jWtkaI_N9ciKKrow3wuuUX2mTKuGKw1y0stQUEvTYw0B6mU4w-u-aWMThZtR83_dEQhBFQ1Vk5Jde7i8zLBPVAvMKkJ4FGSFZT1cf-8cruWWZeLfi_1hEmBrRygLJOUWoQM6h6HdEp8ZUJ4CfUJ7sKziDD1ALDTchM8SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام سانتی آئونا فردا باشگاه رئال مادرید انتقال یان دیومانده 19 ساله رو نهایی خواهد کرد و هفته اینده نیز به شکل رسمی از او رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/persiana_Soccer/26497" target="_blank">📅 18:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26496">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpyTxZFEAoP9BM2HviZtJfBHiMq59oCxBw5nvVV1mVT6Qs6bljl5WBCzR2-pF6RGf-jjaFp2dL1puSeanVzCSeT4dXscTru549PgKJvdoU7yFbhYuENaMdW3HAxr-oWuzunrEFztALTkadWV_7ElwKZYPgicMGi-64n6K_f0Dj3xX1tJ5svQ0gPtIZHtMY0R6kKVG8ObeYXF_vYo4MNB4KYXDr5av2HiOQM3jPzu4fq6DOzjVT4xmXefkgnFSbC-qHCq9gxaWMK3p818u1UlYfHBOVtI1Ra9_sMlQAzkPLfAXgla6g6Rqoae3cCWUvfyDNbBFEPd8cqO5UgxonX8Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛اگر اتفاق عجیب و غریبی رخ ندهد؛ محمد مهدی محبی تاساعات آینده قرارداد سه ساله اش رو با باشگاه پرسپولیس امضا خواهد کرد. لطیفی فر هم صبح رضایت نامه‌اش صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/persiana_Soccer/26496" target="_blank">📅 18:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26495">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d8219701.mp4?token=FUCEHyDy0WPeqp1NcH9-zm4gFgE8ofAL17Gl6rAi4WWszfTQO2aythF9M_hxXrIAlqm-ksf7oWUVJ60AqT7rPuDBXGqO80No3JfDwo7pec4HrYGePw9NdlSQMLJ-8gAmPlvcckTdctBNds0z-SisteWDggf_eCwy-CAil4FxwUSEMR2jJ1_bXt8ZgpwuhXHUORgrc3vaIZj1yfmbzuaSaXS_RmfP7D4HTTgbQgLxJhVMgZcq9PodV4FD517LhOD-r2BBD5hiWhzZ_5gdOupTaVD5qScsYC1E5b0I0KdELjPoVRHUvEzvYPWCK0chn5FEYqHP9pz9_DNdiaywH8dQ1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d8219701.mp4?token=FUCEHyDy0WPeqp1NcH9-zm4gFgE8ofAL17Gl6rAi4WWszfTQO2aythF9M_hxXrIAlqm-ksf7oWUVJ60AqT7rPuDBXGqO80No3JfDwo7pec4HrYGePw9NdlSQMLJ-8gAmPlvcckTdctBNds0z-SisteWDggf_eCwy-CAil4FxwUSEMR2jJ1_bXt8ZgpwuhXHUORgrc3vaIZj1yfmbzuaSaXS_RmfP7D4HTTgbQgLxJhVMgZcq9PodV4FD517LhOD-r2BBD5hiWhzZ_5gdOupTaVD5qScsYC1E5b0I0KdELjPoVRHUvEzvYPWCK0chn5FEYqHP9pz9_DNdiaywH8dQ1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/persiana_Soccer/26495" target="_blank">📅 18:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26493">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZAs6mqplif62hrS0d9frK9kX39jmpRIUey9H3_EwLeHRy_WTf8v5Qsgyz0J5_IZ30JKxnePuT6nX0nIPI9OAVu_5YLXY8hmtX5WxvESfO0OmxXHU-CHsos20UDrw07RkT4LgLhXgjhWtxXaZRIoeQYtZyHaFQ4W5n5KpvBvDZ2RvHxbWJ1pzCB0JNVXFXClUKUExFsGJ3TRC7oJbMftTnQuNydHJo_rxbFaPtijs_GApzX94FySFZ2JaQVB689pYo68-Q2URBZImOY0rskmka15ADTsRJHDosVsOCItFLNGr0KdSKXY5QqEO-NZ78GmKwoTBjUw83Z2_7gDgtwVDcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XVDgR1XTrKJs5-7TIPs3m9zpxi-U-i0u7BdWoGm5z1zCKQbwXTrZNSaj6nyEwk2gwCpvU0xhEkZv-ltZFvh-nOfd0aI6WkWtiokTUre7ZsqdOYbH5AHprlFkdvLSpQKac9boE_98eZ8JXiKC6BcXBIeRduk2xk3PebAamXIqNJ5yZ5Ki-53TqwHskvhFEyMKl7keYprxc1jGd8uHzVLpxe1GSz8q3oHwcrEpsHoAnZzHe4TUrt6FdyiPWkOlCIUVZdpHAP8MEFNwMjx1WORDNV0czCOO_tEH_ycB3L_HVjZbMOzq3BRXQ9EhkE6D2qAnx7KlFi3uxkAuKtJWvHXUfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال درسن خیلی کم اولین جام جهانی دوران حرفه‌ای‌اش را تجربه کرده است و اگر همه‌چیز خوب پیش برود، این شانس را دارد که در شش جام جهانی دیگر هم بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26493" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26492">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXTUcc-f-spn8zl4fG48pbGxsEufvRn1FlgpfBbl3Z4tMMLLoj9o8JspYx-dt4JIfnTxkf78_2yL0_GlASg6GbMtftEbBcXiLLWTBKGrW8poMON8m-24M72Jv7Ew1ImopOGJqETzQVQqRs5ar4NSXEwPj5cQrlgX_4eBJFmdJSS5GAMs6-0ax7hP39KAlilBsxOG5f8tNxY_esTSz7BeRIJmaXuVDjHkLWiE6hNl2259Z4JA9icGyXRZemiit0XVr687sCnyjiHC-AkB5lHjZRApBjUL8oQLxF1Yw6r0rhjKhLYwvjEO7vYo9WsBJHrKKIpQcQi_QqueubUr1Q623A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فوری؛ طبق‌شنیده‌های‌رسانه پرشیانا؛ یاسر آسانی شب‌گذشته‌با منیر الحدادی ستاره‌فصل گذشته استقلال ویدیوکال گرفته و ازشرایط آروم ایران برای او توضیح داده. منیر به یاسر آسانی گفته دو پیشنهاد دریافت کرده و اگه با یکی از این دو باشگاه به توافق نهایی نرسه احتمال…</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26492" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26491">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQ6BKhuv-GQjqcxevTZ8rFq5oEHpg_4FF1Kq9sYbKGgxtL9LrRMmQxkVnAjzTmZ9Mm8scQkQMhdTASNCSIy36KDCl-JSOrYlnGPXFZOoLSggEc6yN2StSgqzOIlfBQkM_yvfYSMWHoKhlT1WzcXfg_w-ua3-39dRnrskdDoTtDNWWhd_1OGitfFY28sPbmuEALHehsg-k6Ke2nv_ns4chxaldxKQr0STT6B8oC-OXLL4Mr3N3ta14MNfRf6nDnG37d0FMKM_KutHoaQsSBbb235GQQiNrSgsLYhHqJZNsj92FIKvdxJpP1rKUy9wSlMfDiHAFld8djPxHWqrPmlwrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26491" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26490">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzR592ZijCwol2mJ5r_GqZtF-WZtDgCwpPjI-ClLXIO8mJ8sLBuYUHX9oVrodUlLVnlDI6NkGSp_Wm-nXjVsqR8XOBYMuZdrgDNRHiF072dkDZc-2XT07PnnxbpaZ0dcA3VIfHap28KQLJ0vJvKM-axSS-ioPzhb-Qa4QwriktxCU6y86PesSD3FEy_Kf03n149-R89Vn5gucbk64irVOOi4GQXsGnqjyrgK5TUV_eN7uHjZd9RI-MsSokDUMcINh_i_zwtiekALd1-YRFhWo1xhbmGhbUC2h7ADxyj6Wg_R4oTmWwCoiZXqEdRzi4Ju_pNS6ew4Ybj-IseTpT_4dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری: باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26490" target="_blank">📅 17:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26488">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0Em04XE0WO9oc8n11Ve9mvwe9_UlBTcgb94MTMa_kLVsPNVaubY9jQdhLPK2MFKsUCKI64g5h7cREq8hLgL7PfaxZEyStWXBXCm06br7t8FFSOHtt8GHYmRCQ-87GMMN3dqZjO6i_3gDLFq73K5gN7L3DRNymgn2xNFd-mq7uAKmqKfeGZxOJT59kVvR9KGTOokR3rhrRWWujU2V5Tkb1ESuLqTk-VCC0e0zfXm8ioEoQIluaHWKINUjj5asSNwYjVqOY_2Jy8i8dOugSmJBrLy0mpYHTjub5oe5CUmsQGQaaCqWf7TKw679vw8qfg29uSjJ9Ymm-X9LoqE3ZzBpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پرشیانا به عنوان اولین رسانه؛ یاسرآسانی‌بجای‌سوپرلیگ‌ترکیه به پرمیرلیگ ایران‌برگشت؛ بااعلام‌باشگاه استقلال ستاره آلبانیایی آبی ها دقایقی قبل‌رسما وارد تهران شد و از فردا در تمرینات آبی پوشان پایتخت حاضر خواهد شد.  پ.ن: یه بنده خدایی رفته…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26488" target="_blank">📅 17:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26487">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/26487" target="_blank">📅 16:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26486">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnzQ03qg3sFF-ggVTgBbdbKkszSIHpI5l2ZGzAimjGOoWF3X9Q9_2Sb3wvXBjv4SdwaJMEQKdPbzAPfDAKBO_pIrI1PcyK7vGMB21iidxcZU21A5AA0C7YVrvfZRFuK7vFVYq7W2mlx2eeHHdlyEWLDE32Z6e7CUbPW8uJcDPE944MRIW89ruPhqAHGnK6Okld8aez0QgFtX4JoreUEtfIhkkDFlVRd6zR8fJfl76oyBtsTwJJ_iuwfWrHpYfmAd2KjpTpkcC3SIqGlFnQkRQ0r3_DNRnpc1sDR319Kiw6zNE_MoB8x_yn-Z9MGNF1sdZQnX_pksBrz8mCkZ9KIWlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26486" target="_blank">📅 16:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26485">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uO-_dhpO3WDZEtnUAkZ6Ja8nycE1d3wid-hzRqzhBQaAeXMPQ9r4riZ1fzZZsjXuE_uXU3tO-QfTonLkuD6F-QJg_8c1qKxNM6lzH6Z11IqiXDXfDhZGLptzF_FRtDGNpkHAn9VgPgIiPI5SzOuwT2AUKiPC3VHPm71vLa9vhD0hwTHYUPu2jQBYmKVGrmvOghGQQN23xf0eJjxo3uN0hyYhXRoVFoEPBGJnyecLQppX7BN93Vvn6LHrTHArBHNKyJeIEjhp6LzLGkXpxFH5uqTEPEICdzxGeh8lClWnGJmsOsIPPdqZXNHh7EVrrsl03v-BfLRYh2eIp7nvGNPrBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
🇨🇮
بعد از علاقه یان دیومانده به پیوستن به رئال مادرید و مثبت‌پیش‌رفتن مذاکرات بین طرفین؛ باشگاه‌پاریسن‌ژرمن از خرید این فوق ستاره پیشمون شد. بزودی کارهای‌انتقال‌رسمی دیومانده 19 ساله به برنابئو توسط مدیریت رئالی ها انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26485" target="_blank">📅 16:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26484">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=NFl4hxjys4_pT0C-5Q0KCqziqOGoefAZjO3RPl-AjbjLS-isX0HEaC_JYIykJCxFPP-CKUKcs83eFt98NAJ6oZplUlLye-t2bj4dNw15_2K_wGYRs2jzHzYe0xtgxX0lAZxuKvcEaCYGHcgmZb1svH0VqDMWN7BkQ6a32YS3UqBj6mQ1wqS-Yt1k37hpwl8X_qermu-qB74z9up9wnJBw7o7Obf6b2q2x_EGeO8Ol_Nf56nFABsBkeNnMxVj12cD28yo2mdpgTxLqpAiz8BGb10kSa-sf7EpgytxZdeM-YEUHJkyUmf85AotoD5-4zbMakiIbwbSuAKJyyaFm2O4bJQ3no9MbyMavlQ_vUO3JUDUpmRPtI7OFu7WlenhobDrcykFILqFqS5Bb0pXBC7C3suRS7XREea9kWFPfBw4gX7QSaEZ2PduAseN2XjuLjoYlc9gNCB-SBWfLJ9q9TxEH7oUMV3MctvaBmm8eGBfLnDwfVNjBcvvj9vxDezBo_QXtTKH9NgxRLQ0YCHZyxilAMSxMBFuw_XTMSUMTHwnNOueQsisrs0z-YR4XfO3sY4NHqygIxhfDdpq4JfC3VFTecQDwGPbT8JxeSp9xNFPGxLq80QV4A64W1UDwguOjIsUEXfIsJnQjzOrej06tTM8GIIMTkVrZ78kAHILUBY4f08" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=NFl4hxjys4_pT0C-5Q0KCqziqOGoefAZjO3RPl-AjbjLS-isX0HEaC_JYIykJCxFPP-CKUKcs83eFt98NAJ6oZplUlLye-t2bj4dNw15_2K_wGYRs2jzHzYe0xtgxX0lAZxuKvcEaCYGHcgmZb1svH0VqDMWN7BkQ6a32YS3UqBj6mQ1wqS-Yt1k37hpwl8X_qermu-qB74z9up9wnJBw7o7Obf6b2q2x_EGeO8Ol_Nf56nFABsBkeNnMxVj12cD28yo2mdpgTxLqpAiz8BGb10kSa-sf7EpgytxZdeM-YEUHJkyUmf85AotoD5-4zbMakiIbwbSuAKJyyaFm2O4bJQ3no9MbyMavlQ_vUO3JUDUpmRPtI7OFu7WlenhobDrcykFILqFqS5Bb0pXBC7C3suRS7XREea9kWFPfBw4gX7QSaEZ2PduAseN2XjuLjoYlc9gNCB-SBWfLJ9q9TxEH7oUMV3MctvaBmm8eGBfLnDwfVNjBcvvj9vxDezBo_QXtTKH9NgxRLQ0YCHZyxilAMSxMBFuw_XTMSUMTHwnNOueQsisrs0z-YR4XfO3sY4NHqygIxhfDdpq4JfC3VFTecQDwGPbT8JxeSp9xNFPGxLq80QV4A64W1UDwguOjIsUEXfIsJnQjzOrej06tTM8GIIMTkVrZ78kAHILUBY4f08" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26484" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26483">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSG5HdMpv6vuSixFUCmouiADgkruC7C-YOTv-3AJU2B7lSMG2vUbMoCZwAAVnNNBuQ5vAnXoiSiT_WiiGCb3mSWPV8fM1ZQHvC2CpGwFXAdxqHsqZxI-hFx2qZAcs3F46uHpVQHq82LVGTf6Ny4NhKcxzXv4ON8eo0joctJdmirq6btFOIe68F4Z8lB3p3lEjG2Ic45pq7-LtZWbDv_SG1-1xPzhytJVQ81YcTkjH28-JwzARyNDPqj762Is8rF_3r59pgans7qjtt-_7LyKbbjSgm-ECHG5Bk0m3hJozogwZoE73ZV9uBdJT86lv2NXlbqYiumcufOGkCRfLTS4Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد زکی‌پور برای عقد قرارداد دو ساله با تیم تراکتور به توافق نهایی رسیده و بزودی از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26483" target="_blank">📅 15:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26482">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dcy8-1H_ziStLzZS-9GuOCnlxuAFSrnTbMow5I9NW1_TuCkKfAwAiPFydNPVWvqKVGPWhnroQWcsJtxKJNgI7jVqnFWSa0qdZh8KEgQEJrDRxb1bHzdktnPrtyNLQY0x4e8baOOZB_GOPuLxjszXvjBOQ2zX2ikj4cvEb05ZoY_TWSPCCgzhXdeUQn84U_SfR_gkYU1PSZQ3lXr_nneBSbqS0An3mhdhu9lPSBWsQao1SaLztZAL52VL46XkMNWe_GoZUPvsAmqk9f55227i4yTjmR4P6uLHQ2wD4jjzxIb8V0RfSWF4OT2M-OOtDTzAjkfjMijw8uugQ6UBjqfK0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یعنی نژاد پرست تر از سیاها نداریم. 99 درصد سیاهای پولدار فقط بادختر سفید تو رابطه میرن. اگه نژاد پرست نبودن این آمار باید نزدیک 50 درصد بود. نژادپرستی‌فقط‌واسه‌بقیه بده. واسه خودشون خوبه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26482" target="_blank">📅 15:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26480">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIORCVESFXdfNtljwjk78laZAq6G0g7D8nG40T96od9KcIIeZJAkhlXm9msmKYkZalHSuiFBfUEqaaqsvP_8-o1uUtxlCcfEfYWuaELpppLX0RBMiOfeCx2e5wLjGVjNOSOqLRY35JjcS9S2kZOybKIWmK1AZrowFptFT2WjMsiO8go8RDlezbi9DDyjrlZ076CRP691ne3j9w1adowSfYKqbXMEutVs1_UUb3EzLjOypHUsDStEG03KNWgrCGZj2EeB8w-oobf2At3IpMmMN3dDtKC6-BJ1LpG9FjvHBE-wAZCICGgBIuSmp4zmcbK1k7b3vxKHXBwk_e_NBavvUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا و پس فردا هوای گرمتر از نرمال میشه و دیگه بعدش برای یه دوره طولانی کاهش محسوس دما و دمای خنک‌تر از نرمال برای اکثر نقاط کشور داریم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26480" target="_blank">📅 15:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26478">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYuKcsv4UEbp9DRw_aZ9uoMZ3hdcA1HHOTs9nlcG2e2JSiHzHiQ1CEcUt9nGALwf-fL9so1PBbjJ_Q7uf3tr5Rhq3CcI4mO5zz49DXg_XsbOX_OpFZzxEk2OrSiBVgKpvJrBFv16im-FYyY3EjBytv1-AgpW8fC4B7qktb1yVK-FZo_skAV17ntgCwx8C-NA1zR_Sm8GT2cAgiBED_RKH2k2vVE8_BOhQxg-6pVfNqU13uoOUh0028p6gW9GxSTXOFgh6QOD4KBRGcVx4Vldbld4DPAQGciIMNTSwt46B-n2ulxb9qreQIU3EN6JG_n9wIbecGLeNgrQQ47nUPIdNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇨🇮
#فوری؛ خوزه‌فلیکس دیاز: باشگاه رئال مادرید بزودی باپرداخت115میلیون‌یورو به لایپزیگ یان دیومانده ستاره19ساله این‌تیم رو جذب خواهد کرد. تمام توافقان بین سه طرف انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26478" target="_blank">📅 14:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26477">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSZD29FBR9YtOEoHiiwyXE6N1tRCQteWtmagcJUEMIrwkDsQYB7UAcar-3wP34xWc-Hsx4XpGa_mOt2ETq9FqJZ0JZdOlk_TshwJKNZygtEWcJM6Gw3PSEB86DkZgEGHkSORx-JPJ3rNeu0QbQPH3qK4sH5tYt9eE6CPhdXi7J47knDQZSmM-8yLBJ7tWnYfOV3OuZFlMqX83DOrcAKu_4zH9Yfrql_moIi_ZEv_Q-pcdylSW0Jp6Hr95NPO7lzL7Is7wPk2Nb9tvQHzPvYow90T6UZ9wRNX-Nt0KQLKmyz94We8V4cBJGFyYYlH8Pq7QLjH_5ZldcEPPjTXbNv_Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26477" target="_blank">📅 14:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26476">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeF_4mWOdtFr9MLYn7O9a8bajAz8ztwVZMEM_KqEIPG-2y_n2Vv0OYpbadMYHSagc4FqrBkG7Kb1AAakdAcuFDz4LTaa6svQVYd7O8AAGlofGwoekmH3depHX-vPNOpUr3bSojppsHkn2IgqwaaDwjB-NLcejc9DLsTdy98bw-Ux5AxooQH4n-fMEPuO3RKbcaSkE1Pn1_2ZjHSaZdAUENHhVGbZrV_zvGPW_b7jTyYw7DhQeOAMT_avzbIIJXXyFGQxaSod-OAZRoCnyx_guC9l6Z0UJWVxGKCb-I305uqcI-m8Pd7FjHFVcEp5mM-Z4Fks3T2jA-qnrxX_vE155A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26476" target="_blank">📅 14:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26475">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=od3JIlffowRCxMHm1zySlzO60EJxo8dre_8bG4bu0janP2nFbLus9iT4-pbES8reieWrJVEDlAvt8B5c9ZMOiS53q88tEjd5IFMXtZN-q1l-NQUG4EtjRGACStstrxChsqnWrlF_9xAEjXR2me5Dn5e1_bD05rx6bJRq9f_kmW8-JmbTfu-byKofhSLPnnpTv9XUM4dEJlfDbaH6KhW6lGrF9fifsI8Yy4qro4q4mF5jkLa1IkZMnF-bpAGPhRyg6RVfgSrtMkOLBMlRru8nFpKfgpvo0eTj4x0v7AR-aRahQdaF1LUJR7YxNXDCKIOpuJfqsSGga-SZEjLc6kBETQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=od3JIlffowRCxMHm1zySlzO60EJxo8dre_8bG4bu0janP2nFbLus9iT4-pbES8reieWrJVEDlAvt8B5c9ZMOiS53q88tEjd5IFMXtZN-q1l-NQUG4EtjRGACStstrxChsqnWrlF_9xAEjXR2me5Dn5e1_bD05rx6bJRq9f_kmW8-JmbTfu-byKofhSLPnnpTv9XUM4dEJlfDbaH6KhW6lGrF9fifsI8Yy4qro4q4mF5jkLa1IkZMnF-bpAGPhRyg6RVfgSrtMkOLBMlRru8nFpKfgpvo0eTj4x0v7AR-aRahQdaF1LUJR7YxNXDCKIOpuJfqsSGga-SZEjLc6kBETQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شکیرا به بچه هایی که توی اجرا جام جهانی‌ اش بودن قول‌داده‌که میبرشون مادرید باهاشون اجرا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26475" target="_blank">📅 14:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26474">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vc5ENbhlpVRKpcNx8CCF-gigaOJfP8h4C4sumFCJdeRQu6YK90MRoA2m9rGtkkzJg2p5Ch2tz5lqBA9fr6D5Eqtm4CD2MWXIUSQErscUtqwNVRypzuv7uYDJtOis90d-jXr53ySbb8zCOo_EEJo0TX6OBmPlHKk1MmtN1Tr81eLCXePg89QhjJt2l_GitFdl5B0CnztrCtwIhFrTrKp3LXai6JXalUsJn6fR8HZp4A0iGCiH3KJETXXxiQRDD6MEL02O0KHp7mMSLufREOK5r5iTztd4QApuH1SEkE2ZlYbornTC4biMn5RyzIm40FtlSms0wdOsVxqMdWJpLngjbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد زکی پور و آرش رضاوند هر کدوم به ترتیب 20 و 15 میلیاردتومان‌به‌باشگاه‌سپاهان تخفیف دادند و در جمع طلایی پوشان زاینده رود موندگار شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26474" target="_blank">📅 14:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26473">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkcQDVvrMwl8tEnRLA_lPDYTbQx0-rErSLiTxedEcZ9k7EuqoBbVyLxJoDo4z77AVsGnTRdXELHK69g9YuJXFtR3GBj3wueipbYrEjq99f9K7W1cPEoILwhoN_IbbPJ44fOAKnN95nD7sHl6uqiQROssqa_mtTOleKhqurYJxcZOYOOfoaAmpzHgSF9GTMn7KOYEnCP_921nLFKktNsLYS8ELgW5xlA8Tb7Ruzz8uUZEGx1FY4I3Tw3nuwZqv3oZ1lJITVDoT_3mJEPSFZ6ErnHCFyg3UxJgc2FJ-17QMaGQYikOJgQ3jf7ZFf9sa0yjdSc6YniwBtVOLyiFJq9uPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26473" target="_blank">📅 13:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26472">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gT6IzMR6EaFRezDhN6l69yDRuxNrxX6MjQAM-Mt4OaapeBeV5bQhEXqHyZrkl7RsGiaV5mAYgSBy_zPJOdEFioad2Su1gkMhhJVAbm-pjqlxBDcBsbtp_TgvMblB1ohVdeF6w1bOOcyIcF9kW3Hkn7pLpF0h-N3Oo33LAGwsRR3VTM5QX2J0gusqLv_0ZL6jluUu6-bsH9HctalbCiCqFgNiBH7ZDz-h8YKvouGSYtMVXxA-x1PP5PYKJEMLbMVdle4Ed6syNnFUNnh8MZMshHw9ipNZC86MhsZJ_aagdsKPtfH-E9m5X1Wt52g7EbhbXsOXMKv3qnoAuWizovkjyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26472" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26471">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0I04OXNvlyCrIsBKvxnfCx5UA2nFdnyDU0kehqwy6F8J057q7rp1YOH3a_zCDdQWeggoeXtrPYEjNCGAAviqwDJDD3thtExGJb0zTu40OvQoEeckNfl8_XrGfbxr5mdM0TwG915A5iXquTz_cD6jDC0CA00kodFQQvoiqNBkIXbp77O-opPFdfGWTHg96ctVBOsn3OvS27yFLbUFJAfGh2DbXy5MJUMkE6_GW86c9hfZbfZcELOon3D4ZDmU2tvnBEhqa8_FgDJZ4K8bnV7rSJ12hrOmenJOuVSoNUa0zMH4pUAvNgXqJCuDYGz9eP0wuaUOn2afsbKgjbuRLmHfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم! آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26471" target="_blank">📅 13:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26470">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9xNIK0IhV4k2qqx5exRBkUuloIzpQe8p61EK0FlvTcFIQXxgcqAEFf9mNQNgGs-3lyJvCboDV3Hav6VXIEDc5D5oBaespQ06vJwd7RqKonvUmlyJ6OeRTA6XFqL1lQdcVECz8di57IEMnjPJFwD9XZUgK3LIM4kmUnj3RDAJn7vCQYFMqJGouBDSsrVigXmKFIFRTx1mZr7H3qL0gw9QGnGZ4K1Mh--bD7c105kQAKFZPdwSYK0UjouTOt0QP2n1FvriJx2pa2UiH6ccdkoea6VyuNN8_lpLbshgCsiyryYrLcsTy3NSo6-TnPb03McH35PEQyHNYZuPUZdm5nGAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26470" target="_blank">📅 12:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26469">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1e4OYuF8QgaZ2uU8KSFsdkTFmeBSV0Ek0PDQWm8Z8Eg49yZSQLLjhjN49dWKeQf-w02LcSzTGNlEU-w3HJ_qK8zA2-FgcMIMdEonp4TQRTlLcVrDUDSPa2CrgGCGkPFdVa5FquMx1MdjbQ5EzbQjUtq1SA52YmK153aIUR5BWhE-P5QvG72Zh62ru9dQ7mj1kBm660s2OXo0MFN3pyNa5IZ8kIHKNoSobZUbWHmDPxYUn8V2ct7O3din8V_VhvODbiuDcBs7evLDymAnRHKvJOVLYFzNlhzEKfJwz0aOvXbI8_Epdftjch1LMMny942Rfiz_oEzNGvuHzXHAFksVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26469" target="_blank">📅 12:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26468">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4LtFagRqJt9xXSqTTu7eEtKJIcPNO7dTIdvffVAuKqHgdIAgvytyMBpynhyDX0xcAk-b9RYQg-BxIED6DtOelw4Zd_ld6Vt28oJw5zQFKqcfdXvdWC6PYME54eIvrThPsXWUq55wzLGOs41b_RZrgs_CreOhQcc2mY529h48-l-FR_X-bmgfgoqPeaHaa2yu9nLL6Trq9tgvPbUCiIb_D9h3zcIO4tkYASI9-YrOLU6qjnjmCoA_j37yIdDvxWEA6eCxL_G7QOeOxTjpOVU1pjuvhizB0NmsuhaVFA25xINgZt3Q1E6stCPFFPQw6V78X7QmPwy4I2EIO_AP_fkBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دلیل اینکه باشگاه تراکتور هنوز از محمد مهدی محبی رونمایی نکرده رضایت نامه 1.2 میلیون‌دلاری‌اوست‌که اتحاد کلبایی‌ها تعیین کرده‌اند. تراکتوری‌هادر حال مذاکره هستن تا رقم رو کم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26468" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26467">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrjZymKkrr8shFTKRg0jQcsTc_kyCK-578RNYU88s7vJIqig6pxNwJj4FWH2fsrtwp_fyzZDn9B_yW3JBKjr92wtcc-AJw4GgE-fzB97cT4Z4wyckr_yUfJyucTYt7duy1tOIrGNBnmx3wjJUvGWQIOfYcES--F44j1hFFj-Sny1yvfnO_sDODfxtqIUqBxtFl5l7j96VNA0ZjYyel04mnplMxqaIlLLxyK8kziw2xh0IUP8uS57KEDL9IzFYP6_14zRHEJOunaAfs0qeGfVLd9gFpNyWjB9arkf2w8IuFKqZyZjAVoYSd0TWQBbT87ClNLZczBjqS7iKqO4M73DBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26467" target="_blank">📅 12:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26466">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFFjeYjJRK9NRQ2fFEGaGI91iOGEgiKvvKVddC87-KM8pyzCi6B0knqToHeUzZBQx4ytY3rlmdobKLEA6M7G67X7N665IsI3q94QZPDvDQZ53Y_6PWOsU4-RV9t9Wt1hJqIscjKuzqhKEoY-YbOpPgm8i7vfLcTbT6vPxLgiW6oGh8_TOd0u74HS_Ea_4fZ-vdrHwyt4XtBu2-eBTrHNmMd24Y14kSLUw1jFyKKySKbvtdO6hTAJeDkBXZd9xWk9EGbXQ1mMQxMnq23k-WifaFVsMIs_4qC527YmkuWM513VsxpSe-oJG_yQMeqyS3eebkz5UxSO1S9MYt8VOfUzUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26466" target="_blank">📅 12:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26465">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5ubcIQE9mvQH_eFZ3JoWOgMooX-tCe70ra52zQg3N3ZFyapu4t3W5uV8wIVePuGZP_3U8ONRQ7N_6j4SSSyYm6Zy_g84svSs2hogydKThqIx5KGNrHtrcdPFv2BVZJ8JbH2Y1bKG5d_J0squhc4uetu75RzcXJ9vNnFKejN4vir2wKVLUF1zLG0aKFIUlI96haiYGHtXE-lXd7HFGiHaMYXVzeO64q5ul_l0nnNlcMWLtkfb3ksNDuYAbhvO2gb_B258791lKzSCAV_8RKfK52bs0VQHxjTw5nO-l6Bre1pKUhSdZpVMevSqJEW-4c0qgdZlUpAxuhE5fNgVTaFwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو برای چهارمین سال متوالی پردرآمدترین ورزشکار سال 2026 معرفی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26465" target="_blank">📅 12:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26464">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=iLu7mj8c8uw-0hYnNq629_htrteCZKDs8CLgR8VYTjV_Apm68JDcnEO3wv3xQLIvNrf8Coo9vJfglxmjEEEDBelHke-bEwrIeMrKb46rxKOv6jHMlB622xEBdXRCSEbjqFdRm9fOgMepNpdrjKFrntP3Cs2M44-lO7SJH9slEZpSv2EnLtGlJgEH83SJA-K6y1gT0I_ZD7JES2lCVCQIYLIofuHI1sxCo-ojdCuPN9wOHiH3te93Gbmevx0AL2mCDYeqC9FQBM2_6PRwhZVKTDyFNwjOd4Y0tQass3l7y0Gy-QVms65YtmGqlpehNO19ITEWh826yMHIKi0QPgzWsbggJwnAkxnpp_XYQwTjqy4f73XTghlEddYE_3WzBtbbZAcI7Ig3OmfvGxD3aklyA-1tXrwCujoxnhcPgKJCVzMfLuq1vYJR1l8zBRCUV1tp8rBRQlyV3w8mL39_b_3J1rqXqRW55QVa0bKOoNK_enVtvix4VsDGU1AOiv_SjKfO0fa2TmDxXtAeiF_6V0DPvKj3in0EwOdpKS1rwQJztKXRnDS1vfKqRGPSCI9vN993TYT1IgwvFuJXtqf2Crfmjztepe3D_Fhxr4ZPGJyPi2xfGh2OTnFNQewP6nIjfiwhWDZ9pIq33aFER_-XJGq0CQVfwzJ2fz8DhLvzSU5BeVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=iLu7mj8c8uw-0hYnNq629_htrteCZKDs8CLgR8VYTjV_Apm68JDcnEO3wv3xQLIvNrf8Coo9vJfglxmjEEEDBelHke-bEwrIeMrKb46rxKOv6jHMlB622xEBdXRCSEbjqFdRm9fOgMepNpdrjKFrntP3Cs2M44-lO7SJH9slEZpSv2EnLtGlJgEH83SJA-K6y1gT0I_ZD7JES2lCVCQIYLIofuHI1sxCo-ojdCuPN9wOHiH3te93Gbmevx0AL2mCDYeqC9FQBM2_6PRwhZVKTDyFNwjOd4Y0tQass3l7y0Gy-QVms65YtmGqlpehNO19ITEWh826yMHIKi0QPgzWsbggJwnAkxnpp_XYQwTjqy4f73XTghlEddYE_3WzBtbbZAcI7Ig3OmfvGxD3aklyA-1tXrwCujoxnhcPgKJCVzMfLuq1vYJR1l8zBRCUV1tp8rBRQlyV3w8mL39_b_3J1rqXqRW55QVa0bKOoNK_enVtvix4VsDGU1AOiv_SjKfO0fa2TmDxXtAeiF_6V0DPvKj3in0EwOdpKS1rwQJztKXRnDS1vfKqRGPSCI9vN993TYT1IgwvFuJXtqf2Crfmjztepe3D_Fhxr4ZPGJyPi2xfGh2OTnFNQewP6nIjfiwhWDZ9pIq33aFER_-XJGq0CQVfwzJ2fz8DhLvzSU5BeVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
یورگن کلوپ بایک‌شرط‌هدایت تیم ملی آلمان راپذیرفت؛ احترام به حریم خانواده‌اش. او تأکید کرد اگر این مرز رعایت نشود، بدون درخواست غرامت یا حق فسخ، تیم را ترک خواهد کرد و این مأموریت را آخرین چالش بزرگ دوران مربیگری‌اش می‌داند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26464" target="_blank">📅 11:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26463">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb3Of5HpSlBhbKhyZlml8sxcK0PVcR9y7ADrtd-Iz2FQzBhw9rd2B3LPqlbFxwz-7zpxMhaQCq8alSY1nkLsY1YEfv97Ea2fzETOq-24AseeR_XaH_5OpC7eBG-iCLVpz6g29xP1gR7pAJUFvPpZH4DLcnLHqaO6-4h0iMRqHvA9n-dhjTfdK7mZM6c_w9Zu1Y1YRHSAAHDNRaWXBbSgcKxAa7xlxZ4wUetJPp4tJ3AADbFPehvsbHJ5WDAreXbLedY1lh439ri1Ebl6PlH3z5vrkZ5lhj4rzWqmXcf31qGuauHGa3v2-7ZZTPmFYvbTvA-mlT63nwx7I0qpxHXALw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لی کانگ‌ این هافبک هجومی کره‌ای فصل پیش پاری‌سن‌ژرمن، با قراردادی به ارزش ۴۰ میلیون یورو راهی‌اتلتیکومادریدشد.کانگ‌این در پاریس ۱۲۴ بار به میدان رفت و۱۶گل و۱۶پاس گل به نامش ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26463" target="_blank">📅 11:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26462">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEbLTsHacGGcgpgcxc_1Ady7TcQJJjZM0DObfJcOCthMZ-vefoTNfE0PXoLu1Ly24Tet4v7nZBki1zyKIaDya0s5IsSZDsQlbltAW6A2w46ATwu5R4pDkJ0XnK8c5_XE98grIXV63u-gXQBBkt7HcV9Bg1Kor3Vu_G7DWVp6RB5s7bgxx8D5yeg9EccTrI6PbBVkpmjgh9A-Z41TF-E1tjGH-CYhgleaFo1FPqi9uO0kvTDRAWZ38W3ei1JEkvzlA5KNvPD5aa-Kq5_nI0waZ47qr94LLp7kmuInHG8a04YZzEUHqy6jy1Vf2YpCkZuy3DFyQrDDYNZuZal7YpfMWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26462" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26461">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaygmygezavsQWdyLT_XvlJRtS6BJlLLce9PnfIOQ8NJRBQqUdE3mcC_2YPQSvd74bPin530mSOuwprxIa2ZEMgIy67GROItqOMclrXVprqtgl_yeQCRmsaGURa0uYtl70AkJsq3ToYzN7k5zrOghtamCgevLeDzvKFDAlCoGwhTZYQqcsa0Uig8bHoF42WpDzGkzgiluW1ZCVkIGdofmKbxIj1gKPerq3ypUWSXri3jkzXdL79WxH1vicU8U75g0YJXLAqh8ztNogkGaBhGZ8qAlgBm8whw2GhZifXTU_rDLCeNhYH1d1mTC3C1kOsUjDL1pKDKePgHIQ1buHDCDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
گل‌های‌دیدار بامداد امروز اینترمیامی
🆚
شیکاکو فایر؛ تقابل دو ستاره سابق بارسا در یک قاب. سوارز دبل‌کرد، لواندوفسکی هم اولیت بازیشو انجام داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26461" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26460">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYJdnznKWPiN2tbwTTPFffAPvf2S4iY9xo4UDJzik7ovhz1fLyfeCb_nqFCReEzXigCV2wXDZVVIYpSRJVqiTmAfmCuaat1WCv2s2sCmqctjVYKga-U-tN2iqtogp8Yo9xwTgwS3_K4lf712BJK4RHTMh0b-yoEjdYbZenDNuM-iNs93aMhJ4iHFgXRSDo5ojZwAsRuH1x5qzBcTxO_YDP0_nZsQUU_RMpujhbbxmG6vrI_wZGPy890TxaxA_ySHvpCt8kzXM5Fow_NsUhZt1-s39zLoqDX8Lu-84Addt1fGfyPltrUyQRBO9w6GFbOVQMN64vrgfPx3CQlWyTu6RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
5️⃣
میلیون‌ریال‌فری‌بت‌مخصوص بازی سلتیک و میلان
🎁
🎰
با ثبت حداقل 10 میلیون ریال پیش بینی در بازی سلتیک و میلان ، در صورت پیشبینی اشتباه 5,000,000 ریال فری بت هدیه بگیرید .
⚽️
سلتیک
🟢
✖️
🔴
میلان
⏰
فردا ساعت 17:30
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک  کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
🎰
پخش زنده‌ی تمام مسابقات
کلیک کنید
💰
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr3
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26460" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26459">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbLAmhYpTfeEzCzY13KElmk78anZLATtUwlw4fQf0EVHawT-gwsIS-f61ttb1ftWE6P6YJMdWnIoYI6O7AzbdM_Y8HlXlK_6dMWMMkL7yTCIKxp8Vvz1u9mHUlhvYXeWNsdbCZgl8v9BSUPngxi4_rll-ZkCHRgA6rKx86hhJRwFL6rwc7MWx4qpPYiZoqxQEECejg42sORD1X3rCVxnoSUfwZ24A7sN88U-T5OfDJrvjpRDIqR-qftd6y_CAmhrnjHioDXX-KnkSB3-nQEsN6SH2U_bEB4s2xdmegVkNuZdbUFzp9fzvYqp-gDjYeFtGlyd0uCEborZNUtYdI_c6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26459" target="_blank">📅 11:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26458">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXfMCOpkD8t-FSBaQEeNqGzAoFEUZJWhugS0Y_4MJc2Chblnrm73ueRzwmHMPj8zxnKBUMKH9_-SHUY7O2bAi0yPs6TiKcGPOuV_9rvwG8wp6Mi5k7lhiJ3t7E8cO1DPhOG3xjHb_OlAD9bwoMAMmTaItBsJyQcF6ohOWZEpGqC19KrvwLQlbZQV_MM5soIxmGCxRQOnUsnEpEKS2HOjU_RehA1tWwBwqDs5UmaeGpMYwZdeK7WQAgstahItFs9jeurlHxkjScBFqKrgXF7d82E2bwCMIazdASyezARZMRZyWAltrNRNJRH8hyoXjlgPtf9-nVp8Ud3FOWp17a-IcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26458" target="_blank">📅 10:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26457">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ep2DGg7K8mKnEQKsGwa5_XLNUWdi4f-ebXhodokEpxMx1zog7SzHynL8L2IgTrhZJxJ5JL9UDbEkFkpEYqxuLJXgybL7l9BABWagqDA0p_bVXImqWOzzTAY7TrWxV7OKqAV6YQ6rGu-FX6M7rAguw4YTx5Q1ftFqdQduSvWIzDdcjMWdjOiuvNifd8zhSxww7YJxgP2gHbzwnOs9R920VMlMtpckCv-9z04iVUD7CJp9aC-AidquYFHRDl4hKYwvJL7ZWyuBuO8tFFjHj8PvAYBlfOYWDeCCk6FjoDg_as_HzP_rCpRjlCwxsr-sFaE8rEAJ4IfBbUGl2tT6p_cfIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
هایلایتی‌ازعملکرد خیره کننده یان دیومانده ستاره ساحل عاجی لایپزیگ در فصل گذشته رقابت ها که در آستانه پیوستن به رئال مادرید قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26457" target="_blank">📅 09:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26456">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=kuYlBZOs_DVB-qK-rxWE7YL8DGRSGjqOF53PHec6bCNJpSM7grhe5oLZxGvkzJ_NbTPpEJ7_i-M_VhqYPASYkBhESPspbIYe3B9ULN1lybItMfurMmVww_OL8v4sjgAsGSN5ld-1-S0PVwPpJ_G7HyHYjR1Bh43aMqDrBxxgmanAcjFbSCdRKaxlrQ3n5GHXQt-XW1IDdND8S7kqlEwsujQitz7JqA3ofciHXeDyPOIFcBfpv3yFgwFdv5i04J3NPZZgIArStIedRiSstx_aibUGZcDbG7k-4eG3m4ms4uYdgf_7D_KKcEHbGB8GZnh29Rol4F4f2lHjC4_CJaOP-zXRgVE76HAZES8puCTzlB3F58GPYrAsQ7zpNA7Z2LtjZd3ZmJ_mKW3PD7eaI75yrVU3OOejI2HCnJfM0AlGw_P8nojRy_ia_xvWK0-nCxW7LoO-s73FmIKarhFdHeYETskA4sqzzsw1pl0M7zgnTJdH6P_OxKZVVsRtVJgXK3agvREigUhmqRXmta6LUnQwX__DBZnbwDqvk8WPEflUuY4kXGuNccvvGCEBCmMSS6-a6HoUnF0CN4nY35CWsFeWp0Pz8n_Vfh5CmDaX2yE6KqQ9A8rHH5QaaasNRzBoiUOb_Ls8u4a8_HQ-b1VgKJoB--7shO9q2DaM47GRqSrum_I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=kuYlBZOs_DVB-qK-rxWE7YL8DGRSGjqOF53PHec6bCNJpSM7grhe5oLZxGvkzJ_NbTPpEJ7_i-M_VhqYPASYkBhESPspbIYe3B9ULN1lybItMfurMmVww_OL8v4sjgAsGSN5ld-1-S0PVwPpJ_G7HyHYjR1Bh43aMqDrBxxgmanAcjFbSCdRKaxlrQ3n5GHXQt-XW1IDdND8S7kqlEwsujQitz7JqA3ofciHXeDyPOIFcBfpv3yFgwFdv5i04J3NPZZgIArStIedRiSstx_aibUGZcDbG7k-4eG3m4ms4uYdgf_7D_KKcEHbGB8GZnh29Rol4F4f2lHjC4_CJaOP-zXRgVE76HAZES8puCTzlB3F58GPYrAsQ7zpNA7Z2LtjZd3ZmJ_mKW3PD7eaI75yrVU3OOejI2HCnJfM0AlGw_P8nojRy_ia_xvWK0-nCxW7LoO-s73FmIKarhFdHeYETskA4sqzzsw1pl0M7zgnTJdH6P_OxKZVVsRtVJgXK3agvREigUhmqRXmta6LUnQwX__DBZnbwDqvk8WPEflUuY4kXGuNccvvGCEBCmMSS6-a6HoUnF0CN4nY35CWsFeWp0Pz8n_Vfh5CmDaX2yE6KqQ9A8rHH5QaaasNRzBoiUOb_Ls8u4a8_HQ-b1VgKJoB--7shO9q2DaM47GRqSrum_I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛باشگاه‌لایپزیگ رسما اعلام کرده که برای‌ فروش یان دیومانده 130 میلیون یورو میخواد. خبرنگاران نزدیک به او نیز میگن یک بازیکن بزرگ از رئال جدا میشه تا شرایط جذب دیومانده فراهم شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26456" target="_blank">📅 08:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26455">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇦🇷
با‌اعلام‌رسانه‌های آرژانتینی؛ لئو مسی اسطوره آرژانتین و کاپیتان اینترمیامی در روزهای اخیر پای چپ‌‌خودش‌‌رو به‌مبلغ 880 میلیون دلار بیمه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26455" target="_blank">📅 08:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26454">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5TciGxE7T6DtOaPmBHhUU-EvJvnf3zLCwm9SZ5ZzEFNNSCXPN32q9kWYODDm_CI4s4EUOYvT-VcLVk7LyWB9mcFDagN26zWaCx6J6AYGH_mvUBj4HVsNFevZYDejYAxJhPszG6hFYtx9Aw-Kc_vV4F8Yjd0LdJFXtfmEsilG0dC9U0G9Fv9lKv4SWlh9Alc4C44fPRgou-Tn_ktR0ku5qgYJq3yWikmY43oNd52KkfVMBe04dUvW325yeWRC5G_ovhV6l_6Hlwl6zaSYCkUobfVBiQTEn5oEVETvmwdtJTSVd4jpuuVKnDQsm_3kedIbljcxqBqLCoVbbVvJdO2Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
مسابقات دوستانه باشگاهی و آغاز فصل جدید برای محمدجواد حسین‌نژاد و اللهیار صیادمنش در روسیه و لهستان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26454" target="_blank">📅 08:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26453">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPyEBxwm-bU3PpEwJsEzWN_Lc-6aE8xulXaHgco4gYpVXrPuTDJNydfcx8utG6lY4LoLoXo0-ZyCn7es5G0Gh9JgfQ7kaHrYMJBh8qOKxE17ZG58KncZEnuZadWaiyC-vE04Be3hjI3rZXchc82Qng67aUP9X3iZaK87Ntms9np9Qh5L1XTV1DYzNQP8dontOfWBkrPWiaI7oO_0A-bxVSvunVJOH0W7ZB3W6FvirGm-VsQGP4mTjPvjOomjKnqk9GPI5uVkAjAy1bRCUxCtJbA93THZBRqHZvcXoqT9kVYfQUtkEIcoWeeHX8DNRTwejorOXxqEy0JPUEw6Jrk8aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو: باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون…</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26453" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26452">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EN5pxl1ixp1nU7pRmkeAtszYua__BTo3pOaGxo1a1dC7v-0NnZQ49Pn6ySPD_1l97ejyi3nzmnzJd--kVzj5fKjZD7ESE0yiSk3WmiZYlXHEut6W3tKIS5NAnHyVLB1H2nlY56wY_e2NncYHttrzLJ_TLHNbjw6O6AWQUNa47PMCJTJHhf6zsOGAg0JQARtUTW8-52Xeu-XdP-8xkpseK20dsT20CMUeSSySVjMFtjYzuhiauswHnxZ4RRwkEweVW0edUxeYkPTNwZagyqCGluOPdj8e3AY-yt7CBmygr3rYlmlt4iH6wAsaQUgg7OxYVlJIPbbbo-vhEzfBW4Szkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو:
باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون یورو میخواهیم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26452" target="_blank">📅 00:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26451">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyjvZ1eTVuzKs1MFPGHM1I6t-VEgj9tnMlNJXoVsobWqKVGrPonPjT6WE0_ShbRYDU8vciiz_D_1V1YSVDmKnycBpflS2o7B3h0ay5Rp88zDpAGqAi8_33fnC8FF7uGAsqiANAWxD2w0-34DwMYieedjz-RpRY9Shmpd33yBKWatre6vj--eX68KNACqI4u9k1cShmC6_R73rkYd39NwgTpxHkwtQBVQz_ApJMqOXr6h_SpVFvewNQmWk3E0SSMkZIVE5SeQNVLhhoGMClFmLMBj3y3FlFg6uIQusFjK6wZeTop3KCiJ_wcWiKRATQQK5a-INA5HbV_36r4nLZWMRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26451" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26450">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjdNpCbdyBba_YLzGBHMTVBld1r3V1tmtFcDx4PYjgXn0oxa7QAL8DjRWtEz5azNDCNo8Jnc06FiZjJo6Z0YhPnS9AmCVm6c6TRWLyqgYPOXKu8VbEmVGqQqSJFyEgQwxx-U90B-mN8bw2jcU3iZH5HTFBhkObVM4D3iRwoZeTlPz7wpaJdMSdxJfoFrBIUz1u0Z0hcmprYvlisOVAfUkgF3I_eong5b2nXilqMDjtwoki19uHH37C_OheD_D7aUnyfQ30SYZvmKjqIJh451ZZk1k5YO0O-sUQEjbj502cHi6-NQV7-OQDRZP2gOi25phEAPcySbjpU1Ea6x4AheBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26450" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26448">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxZIhMNeY7sieYe2QhHaPZa-49Hnl3EU9fLeJi9ObdxgdBlhTt78Y_x4Pkqm6tXpIyjVPIz6reRMN4yhGwgbbjaTRmDjFcY7Jtov23S5qbrvCQS0ZIkjeeJifT49_J1z-i1I1N3TYz16gvC36j3NrabCaBueZ17L21bX3XySZip34UToC2XQvi7vPa3qiTdiQpq5g6U1xG8BUvdZMFKTQSpXCjNjwpB1ukMGI4JGzQ5QRdtsunzUycd2bBR3EtN9uawQlguLG1Mk7b8TgfAtws4x1rTwj5H9zzzwGnPaN5JZXMKgt_nI0nElXVkyteEwf0sAv56sK-FQtDMKqJ3WIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26448" target="_blank">📅 00:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26447">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdERgZWlMNt8QqNxsDiV9Cn8_UwpnCpwcz6hXcsk-BQdVuL2lk3idExnTRq_H6Re6xK4LqzGC06yKMe47h3_19bjesvyjlIVhw-05e5NRt-C0Q3H90xDsQaqqdQByPVlmt-JkwHuNHpE1DA06pOCgcXq7nUoSjvp93AIyico6p-9VCUekjDoADbHP6XW-oXW48amAiVhMWRlu562O-a8Ji0Kwp5Qiy_AMooGGiNT3Tq5nRB-lrQy-enqCpPBrK329Y-8OVrUZwUYlyyVcWrFaZqOsKGhDSHy-FpVGcVLMW7DP8LB6kTE8IfGcP1MRarO9AUL1RwdRgiuY1doaW_mGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26447" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26446">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPepizfxBveBJs1QpZSp_fMkdTUzZum-zNUAcPud06CzV5x7lfb5SRYw_ucWc3tevpGFPrdtlP-7Gkio7ibAuPPODtScKaWA70eRrrO6jvM5l6yUjvWMwYBUMkKnVsgLXdZHVVCUjnUTYbNCnpGWJjMml-XXl-bw9PKn-8Y2q2K2hD0tTzH1XwfzY4ty7R10dPhADhwCCxrQSyV6J0FQ9W0X26YRoS84mf_H7H7n8mnTDxE7DVaI1-y5Y58u2xbL9pJDUtp8rkYnOat8XciDUD24Ejr9qs42dIv3t9ICsOCNyYXjo5PNYItzNts2PIxx4dCX_V6XyNmLFCCoU0dJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26446" target="_blank">📅 00:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26445">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZP3uN9dqyC9Gcwh0gI6tBAplLY1r0Mha5ZsEI8fQJ6z-IfiYtNcBmZH7NCuYzIcI3kPuRh6tmqwNWCM0ML4gMlslYooPkdgmA_5Nn1IKaeIYX5ZwuGhQNMB56DMyNx0-2AwfL5k2450IVas3CqkBLbF8K9oruqTyFpvWPyd2pBwWWbxwFEUp1AsMYm4vwzD5PQ-4QXisTe8_FFSRDr67Rtk9048Z7NoFh21zrP5ofG9YlxlISwy_zdvev-ZdZa3nvnPMPrXGxQWGKXAr2gKZUd44CmDsLIcvrsKORP92UAtScmq6GYRjR4EhwPsR9-tEgYuOOkzwFU3l7MMj7X9XuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26445" target="_blank">📅 23:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26444">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCXvhlvihq432ym4CkYJDfDNVPi2eU-ejjz9hgYcpjaJnyowwGOz2sXG_zuTJGDXsGnAtcSEk8YygWdmOLjpPN-CKc_j0abxdCEn2iI6B_Pg_3-YHERkdmJn7jjrg0-ASuBuduYlVw5fJipKtoGWvPRZoJ1Cd4XqTo6n31gjTTJHqMr1QifJITZuKHwZc2GnBSqAF_23pRC3d4tBil6j224ECp8vpP5_GLPivbZxTqKa50x6ke9qjMXr0gXBx3M_9TA6N39zLntKlBbPWAJdfpSJVuNwiOJ4SnsT5VzxzBTJ5qDrApReK9Lw8BBFuLt25vKF4--usDuKnkQ0dCyneg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🇮🇷
بااعلام ایجنت درترانسفرمارکت؛ رامین رضاییان ستاره 36 ساله‌استقلال رسما ازجمع آبی‌ها جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26444" target="_blank">📅 23:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26443">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOMlhbCdZoPVdi8WIVTDvcYK8fayFDdHdHFwUJQaseYNiiReygL90BLIHHQ-cmXtLZfbYz8atswD5AwWwU3JBcnak43sOcghwkDrzZGVcQFl6d0zlvZQmUqD4cSxmOHqvJNLDN3kRt6himfqEtvuhOXNYCXCgz09dD7OK2zevMiSqTai5oKYi1AD5Qbu-TokMJ6HCZqx00Z6x5Q23HlhVKFjVG2RgNloyfhh5TIOrnvEwtRFowGtPTh0EMQVtZdyQzb0-R1-h2h4pwpiL2xvpH3AcvGQJ1icpkgjOuHwqZtPLUyM6UVENguVPaPl2zVoPQWzAE0LVDtroIotJ48iIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تاج رئیس فدراسیون در اردیبهشت قصد داشت استقلال رو بعنوان قهرمان این فصل رقابت‌ها انتخاب کنه و حتی‌به‌مدیران این باشگاه این موضوع اطلاع داد اما بعدِ تماس مدیران باشگاه پرسپولیس با مسعود پزشکیان و بادستوررئیس‌جمهور تاج از انتشار این خبر خودداری‌کرد.…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26443" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26442">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuvCO3pKeOIirk0kbbcvIx2Hm_X0nYJiEuwYAPNHd_RizSENwpuQyflQ33PYAgkwueZxMt1PpTibOWfl3O-gwQhhXXDyQJqNIcnr1lm2SM5VAfeIKDTVPe5CNvpjylpFlvkhLf1zJF870fAA2qNIWYa-xb3rpF0cbTjrn09sx4GmEIRrpPyhmmiyDWWVfijZdN4edGg_ReweE5Lkcc8unJ2wpnxCDUqaX5h8p16Laydiq9vOtztFepTNVxNRFWnuM6NqrSu67ZEjudUcSeJ6v7gVqpgKRKHSOIT2U_WB1qVGQhBdinN6Bu3SfMnfJYSa4pHh-8FQ9Ksw0lyxGSxDuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق اخبار دریافتی پرشیانا از مدیریت‌باشگاه‌پرسپولیس؛ فردا رضایت‌نامه دانیال ایری و کسری‌طاهری‌توسط‌‌نساجی برای سرخپوشان پایتخت صادرخواهدکرد. محمدرضا اخباری و پوریا لطیفی فر نیز دراین‌هفته رونمایی میشوند. اما برای پست دفاع چپ‌هنوزتوافق‌نهایی حاصل…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26442" target="_blank">📅 23:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26441">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBLDDOawOJjQf3ttF34A6ya7Kyh4bWRS6XzXYYFvLpRuBAJzUhwJl_JAhDstlc8utBzc7s0hS2QRhgBVT8vHSZkeLA16cXZDRPBC9jYc6k0ljOE-fFzGIIvtIt1V0MqZ_B_sHJM9VG9arAE2tWN2Iu2TdILNpmucktbvDfTnrbo_bxIn274MmQaRlMwdKKvG3vCWqsU7C1-IPx0DKqKCbFYR4hkxUVrMlctfIT_vTyP7CxKxsB4GIIgx1YpXc7EkBEJOoyXBh_FlSY4I81QB1M1l9o9Ju6p9amfwfpGmPDFBQiUU3bZv5epQsw1eRf1edUgPfjL7eSnqAdparx-cTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
افشاگری جالب زلاتان ابراهیموویچ:
وقتی میخواستیم‌بریم‌استادیوم برای‌دیدن بازی فینال سوار هلیکوپتر شدیم و باید اعتراف کنم که از ترس خودم روخراب‌کرده‌بودم که یهو یادم اومد اگه سقوط کنیم هانری هم میمیره و این از استرسم کم کرد. با خودم میگفتم زلاتا‌ن نگران نباش تو بمیری‌ هانریم میمره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26441" target="_blank">📅 22:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26440">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=Y0y27wsL8kekv4nteOt9NH1WrYONQ4XD353GZz39TxAVO0CeF7YIdJugQteC91HSsvS5LtbqYreYwhX1NmRHMSdjIpDc4JEEV8dh4cbSZKFOojfhCWvxcWq2tCI0C-A0BNmazD9632h3DAKQMZY8mExL72iiokHIxwY5tZDlkuC7urHQHd_UPPlewy6T1aHtTIVcTupqz5vtP3b0vqsZ6iHF7dkVOJOsacih6IL-UdY3nAb0grmHTGSpoVc6C-T--WbjYU7WB6dbKf44mIxU5aRED40HiHJ4KtwgBWT8MSnCG80fdnJkc7y_LJ9Y_kLWDKItU5x6rSYHD-wGkW2vkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=Y0y27wsL8kekv4nteOt9NH1WrYONQ4XD353GZz39TxAVO0CeF7YIdJugQteC91HSsvS5LtbqYreYwhX1NmRHMSdjIpDc4JEEV8dh4cbSZKFOojfhCWvxcWq2tCI0C-A0BNmazD9632h3DAKQMZY8mExL72iiokHIxwY5tZDlkuC7urHQHd_UPPlewy6T1aHtTIVcTupqz5vtP3b0vqsZ6iHF7dkVOJOsacih6IL-UdY3nAb0grmHTGSpoVc6C-T--WbjYU7WB6dbKf44mIxU5aRED40HiHJ4KtwgBWT8MSnCG80fdnJkc7y_LJ9Y_kLWDKItU5x6rSYHD-wGkW2vkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26440" target="_blank">📅 22:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26439">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGxES1Bos-G3b8cSxrC6_ZyfQwqY2L1wz0bpWAEMDDdfDoanice77ufYygvpx65ZK5dwoJnlO6MChGRJ7Y0L8pg8O-JMMfQsMngXL9LX6lvNUfPkfJjiU6VcWikzYvkC4G1VXMikOV3pBKOpWMxp8jz3O7I-OW-XanQyLdeKRXAUrgXYcHVbpnxUCtDBWND2uZ7ehrq2m2RMu8INxkGlTt0aCHqPrHcKRnAOxEKTH0JmhyOoqqtx14OnVdoZ6KOdYNjJ2rYhKhaZYb_EyMeSAHVi4ovwb63-jLN9lOle1MzVywcWZMZZJtgxeFBhWsWPkA3NzQNBPELcVcT5KkL6_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
دیوید اورنشتاین: رئال مذاکرات‌رسمی خود را برای جذب رودری ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی آغاز کرده‌است. سران باشگاه رئال مادرید از جذب رودی اطمینان کامل دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26439" target="_blank">📅 22:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26438">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMFPav8iBwh29bvFasrN5_nNDo5hC_kP2yVvBXauK1v964-TpVrmbrBH8e6fLMFKC_cA97-L5URuIYAczJ70jWizWn8H8SSpxZTXrueSCur1DILdcN4O9pbLin2qO0icgOhzN-kYLXFhGGOL8FxYtCrygfbFZ0yHwuv8GGdpY42gTsmLcqqhNjdFOt65wEDE6hwOqpQZhbuD9geZQrw9U-gh5GfWV5056rsUGmCwf-B4_B-su0QkigCC_UG1MQiPfTMgVhHPMibQbz9oOc9z42q4A1ZO8UwcQMqUngWmbs64FKFddQ79RQbx5zUB2QMZB827cwvR52azjGXWk03QXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باشگاه رئال مادرید با رودری ستاره تیم ملی اسپانیا به توافق کامل رسیده است و حالا فقط توافق به منچسترسیتی برای‌این انتقال باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26438" target="_blank">📅 21:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26437">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXrwSF895yA2DaxQFvC7k8evjNfMr5VcEpd1g9h3oDEBXvA40gi9clJuvo_KvFAcmLyJ-TPDra1XZ-fKlUjfbEw19G0dSZcS5y7R9QPRiV9IUxw3OaDWXmO5-fBnInAzBo6vQFn5ijcuxvfO8RBDCzUOUGBVv-z0s_i2WE1H_BfHsmv14Eh7cbVrgp3oJ92bSa0IPWL37toLDuyEsOkpW3ltrSBGMp9-F57BPwM6pheTXYyq7fhzypvdlqO7cJaRPvf9f0994UHPJp7W_cJ1XRnkFa2RUPrStm88K9_L7L4152fYpy9dCOKOy6-y5mXtGpxZDmwqs7ThATbSQZYldQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26437" target="_blank">📅 21:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26436">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixLP22LKay8PBw8c-bi4uwSahsizpSwnuqUVAJx3fC4JdqaOLiHkVCWX88yNWoFC3NC-60bsGvx9gCN0av3lZ6Fe-3VZXHbILsDxD8ng6ZbqE1mu79HyiDe6rnA7PoFET5goO541ssDeTSthj27DHCAj21Hj0ADTgNw2H65qUNpB1HaOY6BwXbGk6XlrTRdoUcs2OG9aQ5Sg0fwHMYTQTajBHE-W9RTNUsFbs7UdLwfI3PBwZc8AtOldl7Kpux_eXfgpHjvCt_OAdj6Io8YQ1JYoN3IYU9kZzu275yRKpF6V4n-B4vHa7j7U6JzxLTtexuId09kzo15g68E3QZeQZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26436" target="_blank">📅 21:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26435">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8b4ce1c09.mp4?token=AsUz7BrD0WdE0jkgK9H54Wy71kA1SuC_LGgG1niKyrcXt4HQ1ZFlA2RbBmthjQBENjCtXUtzfx0XSgCeTFEdMNqpTIVkZJeSWpqE2JArDPLk7QEhZxO6LshMihLVHljmMY8pI43IxDOEk_M5shM5Nau3El6fvnlcYaNNgrOXk2sUoR--tERikhoyRJt3MQt7WZCKuD4Tym7bh929M92D8_v3tpDLB9wFKq_PM74iH8IgLG3mrgpFYj9Ajqj6JzQalASQtdez5YMd-94gFHDhRrazy3-dR6y1en8ebTVoeLZUx2GpU0HDIJtQoCpCduFVfYf5UmzIKkFaWuruy2FalYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8b4ce1c09.mp4?token=AsUz7BrD0WdE0jkgK9H54Wy71kA1SuC_LGgG1niKyrcXt4HQ1ZFlA2RbBmthjQBENjCtXUtzfx0XSgCeTFEdMNqpTIVkZJeSWpqE2JArDPLk7QEhZxO6LshMihLVHljmMY8pI43IxDOEk_M5shM5Nau3El6fvnlcYaNNgrOXk2sUoR--tERikhoyRJt3MQt7WZCKuD4Tym7bh929M92D8_v3tpDLB9wFKq_PM74iH8IgLG3mrgpFYj9Ajqj6JzQalASQtdez5YMd-94gFHDhRrazy3-dR6y1en8ebTVoeLZUx2GpU0HDIJtQoCpCduFVfYf5UmzIKkFaWuruy2FalYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/26435" target="_blank">📅 21:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26434">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_JdrwMV_lT9jxg9tYeD0iZLunzDhWf_xaXtzDfPN5gZ0MESXb5C5jutBPL5M5GH-dFrc2wXOLgrQcZGICJ5OiHfyDkDhD_YZg1ugYMJdaBqZdCv3KktmYfN4jyxFZk3GqTNua9l8tDdApNePBboO3iZEvDlnEgcvHAlTLzm2LN70BUWxmGSxKNKOO8gLreFEwXyKqtfVFIcOBlNskC28keCZSE-ykQt0YaAOw685qVkp36VfghbYidTBsWhMLt1BXumX3HXtlf4Ce9umgvueVcSpeqRuDeDh4EfERG5eEdFz7i-S27u7_EqgUdqTAVHCAk8vRNeG0HDTwRSQx5UFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
#فوری
؛متاسفانه‌خبررسید اکبرعبدی بازیگر سینما و تلویزیون دقایقی قبل در سن 66 سالگی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26434" target="_blank">📅 21:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26433">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wo2oVpMhuyj0oFrOSSxLPJsPE06RrfXQZIzRZmi5JZKTNkCqSgB7T8985P2WqKY09bV7wuOGm2qOhPrfi7yD3yX8aNUUWmhSzkG6yL1vJ1v9XcglagmeulXEMRUbj9NNkK4tpuVXCr2tDbTsaJSKUZpJDuG6uJ5iMIXvTawdupmf3Zws8RQ2Pz-J2WAT_ZzFpp61qCbZXhsk3UqAioetqPzX3XoLHqG4qsFzksv-5Oi_OkK3ftYZZW_JRd6dF3OXG6AR2yiPK2K15bPShnbnNF23oc1PSRdklWE8vE1seaUo7T0zqyRwchaCe_HxyLjP-CSQ9eGr1AU-i_jDnaYgXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#اختصاصی‌پرشیانا
#فوری
؛
باشگاه سپاهان با احسان محروقی مهاجم 27 ساله و گلزن تیم فولاد خوزستان واردمذاکره‌شده تادرصورت توافق نهایی با این‌بازیکن‌قرارداد امضا کند. محروقی پیش تر مدنظر تارتار نیز بود که با موندن سرگیف در پرسپولیس قید جذب ستاره فولادی هارو زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26433" target="_blank">📅 21:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26432">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSKbjDljNRKQIsAmgMZFxVq63z4CDQN3OTSEO4bwir_loriWFBU68lzMwz4Fo-BugePyhlEDYZGk8HgOQa2VEeKsxZjjsOQkK79DjLoSf2tgjawiCHAs3b3FpSVK_97Orb35bygK_wxlMrQEDL7YqXeTt8zeOoMaDi2GNmru0vJknIYalT7xlLbAn2pIXRUEqzGxOFiy3bsl0M_Xo-YblpkvzwYK9kwyVmgZpXKOGya0-ni4iWVHOonQ31xnDGfaOAHjy1W0ormocmSvT2GEol6IBdSVP_3LiOw7Z1DFPy2S2bUniMk0gs8hy0u_G1gqecyeP3ERLrD2FCJ4mtBZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چلسی‌ که۳۸بازیکن‌تواسکواد خودش داره "بزرگ ترین اسکواد لیگ‌جزیره" و فقط میتونه ۲۵ بازیکنش روتو لیگ‌برتر ثبت کنه مکسنس لاکروا رو هم خرید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26432" target="_blank">📅 20:10 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
