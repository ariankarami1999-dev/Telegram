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
<img src="https://cdn4.telesco.pe/file/t_r6O36fvFxyDz1cSWQQxM_R963RZymQu0Y3nFYBC1MGGWfwTroQzz9pkWk54W8-us6MEe7uNk_jdvNKj9sbMlswZYFQk6McxvosjumEPRuXpL2y7_awoYQGVfzkGxolqzCqHwPcLFMhsZGtH8Erh8jW0Ji3wx2bCFlk8_BhEnaondz4Aqfa3tsZlkhwslWzCq-HUX0RjTjV0wOidraFWH1DvfzsInd9KBvxK9P9DUJFG908oSlXjTL7phDeJ4uJT0TjRDnIn12qWX-ZG09JA95LwQRjC9gtlxfcNxp_6Shm2RyLh3zCIA_JIV-k_RNk3B9C3s6zHY7pfFe0l3clnQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.24M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 00:21:54</div>
<hr>

<div class="tg-post" id="msg-664083">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ترامپ امضای توافق با اسرائیل ر3ا به رئیس‌جمهور لبنان تبریک گفت
🔹
پایگاه آکسیوس، نزدیک به منابع اطلاعاتی رژیم صهیونیستی گزارش داد دونالد ترامپ با رئیس‌جمهور لبنان «جوزف عون» تماس گرفته است.
🔹
طبق ادعای این رسانه ترامپ در این تماس تلفنی امضای چارچوب توافق با اسرائیل را به طرف لبنانی تبریک گفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/akhbarefori/664083" target="_blank">📅 00:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664082">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANhM94UKdTff-6YvXiMbQ_VxS_uODCmuN0hoF9OI1kEpmLq6eI5tT_bTHg6yP4Dxkb8S-tSFGasaml6EJr3zGNNDUGc-Dmim16SqgVNBBBLqfZmcYjLFCCt9PTDysI8YFIc22nPuVp5xRCJof_jW9tAjph67uoiUmjCV4_QUU2mKV6uNsJMtM9TZJ6nNHxpIVsY6m4Rt9eUJv_9waQXwO-g2CVsvFTMmBiViawBuvqiIwy21j1PSokLYt6mEDYrVnYJUElp-UmsZfowRFnMdCtOSM5p7ZtTJgdPj0tgZXXU_AfGaXb_tyDnaozXUqnfTOeKibIuKH-DW6eG_8SFPkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تو هر کشور چند روز باید کار کنی تا بتونی بازی GTA 6 رو بخری؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/akhbarefori/664082" target="_blank">📅 00:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664081">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAyVxIIMy9Wf2lqHpFoCHG0Xcz7TEh9N8l7WJNKw0qisq3C88dghXdFYinOM_VW-qOPGn5gS4qDNcTPpYTVqVuczINCa_kIDmCgqV_3Bn3CimPo_7jZBgb38KvAjicWWr_CQF2XkkkCOqAgbbq_l9vllX6gqxA23fPHuskIkOMWNwcU15dY9l41WvjNiSetDj4_C6-tw_H-CnuMWGg-tjFPdeaSnphKLuhNVnWgYMxQI70wVdKht1l7wdFEwy5v_rWVplBqKceQqabIM6C8ZbBVJM3E9L-In3XXAMqV0IsAZd3zNY4qg7XESH6_KBTNKTg4HWxeKAQOBD0Ho40tgIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جانشین ولادیمیر پوتین درگذشت! | سرگئی ایوانوف که بود؟
🔹
سرگئی ایوانوف، وزیر دفاع اسبق روسیه، معاون نخست‌وزیر و نماینده ویژه رئیس‌جمهور این کشور، در سن ۷۳ سالگی درگذشت.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3226136</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/664081" target="_blank">📅 00:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664080">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
حمله هوایی رژیم صهیونیستی به النصیرات در مرکز غزه
🔹
منابع خبری از حمله هوایی رژیم صهیونیستی به النصیرات در مرکز نوار غزه خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/664080" target="_blank">📅 00:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664079">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
بقائی: این یک تناقض آشکار و استدلالی مغالطه‌آمیز است که با هدف فرار از مسئولیت بابت همدستی در یک عمل شدیداً متخلفانه بین‌المللی مطرح می‌شود
🔹
از یک سو به‌صورت علنی هرگونه کمک یا حمایت از متجاوزان را انکار می‌کنند، اما از سوی دیگر آشکارا به ارائه «حمایت‌های…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/664079" target="_blank">📅 00:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664078">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5xnCP46eiLHd1NeXGykqP2sdJ07FQukSh-ytPuEl1qwl8aAEGUMCIjkIijVKhMa3KuJ4-a6Gkxy-Oxiwv8XlETiVcSRy3UYQzADlCOBBTWx4VzY8Nhfe3BizovbBLbqshuZFoCS7kue95DL-TysvrLDyNAi4JJpgCfEApEoDcjyUCS7_BUKzdKYUyixDZnxRaI6YhcBJM8YMtwLrSw5KiA2rQc3X8ClRuFq0nYjO4jRUhiQovcfg-Bnxp8-aSN46a6WuG7RPHCaBSplMH8pZjfuKoYdSSOP5TOTgIAhM32LBI6tM7vQL_6xFlSZKa2fGIb1jiFVYzFc0gys_EHbOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/akhbarefori/664078" target="_blank">📅 00:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664077">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
رسانه‌های فرانسه گزارش دادند که در ۲۴ ساعت گذشته ۱۰۹ مورد مرگ مرتبط با موج گرمای شدید ثبت شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/664077" target="_blank">📅 23:53 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664076">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda6118ec8.mp4?token=AtcJ53MV0Xorl93wnFsh2DqVAMDb1NDWKZ0MzHim2KjR3xJTDPDYYOjGONX-0Iu5BIF7wAcQgTqwc48PoHx0oaPeQ_dz1e4b5ue3Mf8rUPJ09P_82q0LKH1H9NjrWNHaAhFmmvML6TD9cf4Pi7qNBx62jsed1VICSyIOJrtHO_PIU-AJH3CKfeEP7dpxoxXABPqicbjWhqJwdaqZCIclrTaT3tvGbp9vDWrUqwWM-Asdx0npYAGLjb8b934C_14DW3CxN2xtoxMPEIxXBEoc1olc82QNlui0VovXeJQg0Y_D7ZaxG3wBGhS0kUYP6l4Vs8_1fYei-svdZ7ELDKVmDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda6118ec8.mp4?token=AtcJ53MV0Xorl93wnFsh2DqVAMDb1NDWKZ0MzHim2KjR3xJTDPDYYOjGONX-0Iu5BIF7wAcQgTqwc48PoHx0oaPeQ_dz1e4b5ue3Mf8rUPJ09P_82q0LKH1H9NjrWNHaAhFmmvML6TD9cf4Pi7qNBx62jsed1VICSyIOJrtHO_PIU-AJH3CKfeEP7dpxoxXABPqicbjWhqJwdaqZCIclrTaT3tvGbp9vDWrUqwWM-Asdx0npYAGLjb8b934C_14DW3CxN2xtoxMPEIxXBEoc1olc82QNlui0VovXeJQg0Y_D7ZaxG3wBGhS0kUYP6l4Vs8_1fYei-svdZ7ELDKVmDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ری اکشن جالب قلعه نویی از لحظه گل تا مردود شدنش
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/664076" target="_blank">📅 23:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664075">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac9cc1551.mp4?token=IOG-yKxyGoRfRV77gMK2BYF7gWmCY2lzBDPCeHj8V5VIaAsoNZbOU-q7iGHRubQh2oxNgQ3NWmDdPILc_iHi-5tt1gMJ-F1rwox9KZFq2VWNFfYktjPJU3Hp7YEBZgUvcYle3M9k1H836mctzbd53pF66X5OqqFPX05hMgjTMCbfqH-CDVluywA2VaKbunEtcjtmLQvhRB3OGJwx73LnwxBoW_OV4ngNXftKzosULI68lLzA6vTd9NsPCMDe0NudTN8jQQSDXmVn_Pmfz3sdaIHs7iJ2vZ-dXUsXYjDE9fmvxudX_-BQxeFXlgG9knXHxgeUBj6iCqGA__gfr6oNQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac9cc1551.mp4?token=IOG-yKxyGoRfRV77gMK2BYF7gWmCY2lzBDPCeHj8V5VIaAsoNZbOU-q7iGHRubQh2oxNgQ3NWmDdPILc_iHi-5tt1gMJ-F1rwox9KZFq2VWNFfYktjPJU3Hp7YEBZgUvcYle3M9k1H836mctzbd53pF66X5OqqFPX05hMgjTMCbfqH-CDVluywA2VaKbunEtcjtmLQvhRB3OGJwx73LnwxBoW_OV4ngNXftKzosULI68lLzA6vTd9NsPCMDe0NudTN8jQQSDXmVn_Pmfz3sdaIHs7iJ2vZ-dXUsXYjDE9fmvxudX_-BQxeFXlgG9knXHxgeUBj6iCqGA__gfr6oNQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کواکبیان، نماینده سابق مجلس: مسئولی گفت کاری می‌کنیم اسرائیل دوباره حمله کند تا مردم بیایند پشت نظام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/664075" target="_blank">📅 23:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664067">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m7l0LPKGZ53ikVUb0QRpgw3D3MylGookjqNxUkW-I4A28qq6lI94VNVln7od6N4CcE0GNvns6pYs6aCmhyZrWmHmVyfgcocOo5PBZ5SIvaqttvOgm8DM8nXJwlLNVsn0aVIPj6aYaRQM_f3QnTR5H8CVSKiwdZvetSVpmLXaH1-VxWQXvk_t1-PWCE7WawHVVqI1N8eatiVtL9GgNdTVR1lHSfIs8WvchS_8Cvdp1OaXowj3JErd7EzXn4Oy8AtMG-T_RDdiGpyiPp28ldQVOpp_9z5dciYwQ7Igja5LPckzyEp0Wr1Ao3ZY5t6ByfqkJEt1hoh88DK5ZnTd4L7Q-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qytph3g6_0C4FZ1LWipQ31-qCgQIur6VpB4EPkzRkXZsMPx695JdfSumHBj4gKbBFvQig4pRl8K87XMonxXxg4Gtfdb-aJ-BkypkssRBwTIoUJTcUx2iJG6tp7UyJ_99mI6AZwoUnQBB5wRtoyGZXfEikX41yN9lBrajsb5ct-ME3WgXF0hD-Ut4OPcIXumNoFbcNACfNSxu-qOcZBoqPvenJKCR8O6K231dsatJsCFmkxNhQNwB-eDTat-GGs6qOTxMYLanw8N5q1s67jlH48l4oplmgFnsAV0gJ-za4LJsmuvPXsEhUFC8H_pWXpmHL7s6EycTDtgkkdMIu8voRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IU1asXyCcFrWn6BorQKc4kmxIAdeYwvD89-pRQobxqW_r5wJppX3BybcwgN-64kMj-y3KC8SogkOUE6I_d7GgcAnIxMbaWGkKJ5w52yeIaZmh020njkrt_hLZmx_3KubFFj7lGpS0H2Zmw7lJWCJi-LpwUcYDGvWJxMMB19KZMBO4XRCT8wp-DeQZM8w-kOxDYfuwF99J7WQJ847rkUHM8_9PWQLdidMDkxrr73C7Ib8wQOHrDJL_Q0PS6d-ABJit8zcVB-_l9PUFIxU7p7QoJ--6IhjSJiOIOjqekSVPo3P13G6Ms1vKHAjxUOa5nn2XY4G-FCh3Lv_sF5HIucCjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TkqcmloH4PrCTx1mvgK9TkZ2UWhcQ51tVwv_oTPtZp-0jmvCj6rbjqjAGtr-7PCtnuSlfhQhSTgFQXYOkXbfiMVJnc3fPIuxGwun6d79vPbAvyQzIRa-z76BmM-PZ53OJbItSWbkJOhQTOP4gM26rIknDo7WNCqcjmTk-tkWoVmroK3pvc8Q9E_PbRmhNGBiXQY1RmLpy4znKno6kao3xK6mlEDbHxcO_jslUmSApolhsM-1RxuhIahPqr_I61qC27W4xVNi6pnlxPTMe2M1Oo8r_kvCNvzYwPxlF-2W7K4wkt86F5aTQFYx3kTFGM8mPVZ2rJit56Po9yCovPP4CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m7scZLbBky1dvLiwCD7yq89Fsxr1ssrzlr9-q-R7bHXjw1EfxqL5_oVFStnFZpDrfzDLwiTZu8VpIjpDuVzxmzNVh1MMeTw41Heck26TicXtxBE_Mumq_i32vJlC7a3zY1NentSNNEz0yqUorvR7HXm-XIVjpRHAhoBwo4KUrQFdjcAegqdF_O30VhwrW8ImEx_mNIGn4sNtJk7e28koGuomD7-z_Fqs-ioIZRPQZi9guySKyelyiTGv1aIh4-d08cEQeKUA1oVIZmdea96FjXX02cxHlTv6zHvMorR6hX58_lp1YJlF_UkdsQWWWXlmAWzXDZkKkh8HeS5lGYZKSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YUCot9WQJH1ocAY5Zd_OdCtbRIhkllUXIJRv5cnZi2iiV7NsEJajBxRVCMsLg6JNy-DZHtaVUllrEp7i0L9leJlmppPu7vcAdjcKY9MN357TmX9dY1u1nBpbuAA0ZFSvsV0okeakD0Z0seKIcDTSZcnrpuMc8dq4lCuzM0sJEmZAjP-1NQkC8Bavqm68Umry7l4sjdZxmA8cyIeFdp-4gKqYXDaHwMMbgQCTFYeFxtPqTzxpA4H9N7t20uxchTFOXuFrnKYIRBagEBL9Qf4lx0uMN8Xif17iJ_ido5QqCcDHb92AmC8oXCMIJJgOBZasVsyv8P7YJsn2Q9PijzkIuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fRI-PBdUuwExBfz7dIZ8WHcu8f14Yrjh9ccDaQqNvnumNtTiybXLoaxCKPcnpMxYYaUp0j6L5u3XKdQon2O2q0BZRry7icX8EJ9sro8CgCTyWq6jNVhm6lNe1sGI97cTg8sfV0Oy6zXtbHzlPgbnPVCsTTCCkd-dnQGmsUKR08TBbLpvrwQ7aBqihE05j18-JgvZIWR8z7NBXBoHVev75bAUhyEIhq62A7PAtk64E-IA95_cwB6a4egJDaV9asPlHruLpkZ_JElrR_OW_QHL8O-CF1jJSL-K0YsxHDjBkKy2AQe7STLcU_sLPkXUj6irIk_Cdrf9JNstcfMxGQxEIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jTyLjCP7Olc_97QljSLPasiozfLNPHUN8XyGGlmFnt61N7U4YEcx9evgKhowz1w_ytzqOTv_kIexQgUClkZcuvGM8LDlJav2NBG50_8HWZ1Wpum__G6rZ0EfTn7ZPKvMo3SCjsx1Ak5A1u4RQ64YjuasgvnDupmN6yzA4qY-6XCZwAVwnOZ37hFkw3CsZ5EW2A59eJJ0IuDI_-FmSj8jVhmUAAN7o74gd7YtUq8vLq_8eIiMdnSuz3ZY4SXVCNq1gXQGftZ2dyGKG6XJdTDHnpuggVy1jAyo1DHJYnig7-DZsc6D4sDs3K7cLZ98WEDP3iMkF1bCHn8s1z5g36zBpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
اینجا عطر نذری، با عطر اخلاص درآمیخته است...
▫️
دست‌هایی که بی‌نام و نشان، اما با دلی سرشار از ارادت، برای پخت نذری روز عاشورا کنار هم جمع شدند؛ تا سهمی هرچند کوچک در خدمت به عزاداران امام حسین(ع) داشته باشند.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/664067" target="_blank">📅 23:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664066">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
اختلالات گسترده برق هم‌زمان در چندین شهر رژیم صهیونیستی
🔹
ده‌ها هزار نفر از ساکنین سرزمین‌های اشغالی در اوج گرما بدون برق ماندند
🔹
رسانه‌های عبری زبان در گزارشی از انفجار، آتش‌سوزی و قطع برق گسترده در چندین شهر فلسطین اشغالی ازجمله شهرهای حیفا، ایلات و کفریونا خبر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/664066" target="_blank">📅 23:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664065">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
اندیشکده واشنگتن: تعیین قوانین تردد در تنگه هرمز در دست ایران است
اندیشکده واشنگتن:
🔹
نظم سنتی دریانوردی در تنگه هرمز عملاً فروپاشیده و ایران با تحمیل مسیرهای جایگزین، کنترل جدیدی بر تردد کشتی‌ها اعمال کرده است.
🔹
ایران بازگشت به وضعیت پیشین را برای ماه‌ها غیرممکن ساخته و کشتی‌ها را ناگزیر به استفاده از مسیرهای تحت نظارت  خود کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/664065" target="_blank">📅 23:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664055">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OouKMF9joPGDjQq2UpWWP8uOg2dGRLn1Lm3X43MFadLOOsFyt-WnVcv-0vDLy6QoisNHX8YLyrFP_-_1ZjyZStx07oM20o1rrj5We0a1L-X2NujFfJ7V98xkyoxVxHHbU4wBNyCX29vx3Bg3tcIwV6x9bkg5keBe4udY3SaXhmEAmP7Ku5kiQ8aF8S6BxXzYo3Giqafgrsg8kEYcUIy4bd0YUW1x_MC9anjGueq9uaIGoclj5KT4PXR8VacOHhe_naz68mdWL05X9Y-N6BlFqNiVlzMP57zx1j_pPi1-dV0yIRiScnDx-ebhcKplNjtJKFdyxjto5gwVbJVEjnegWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g0fkYA8ysijxi-mIEiBzyQKWlSfT2YKuMUL5lnqBJxHcmWUB6ng32R5qGmwWPkymYCtqhntiGLz0Ku3sKis1qcoCJVHuSDia93mZRk8ZXz_wuxETtgcR_V0aMY2nhXkEjwTiMxb82AwCZ-88iEpbRetS0AGWbVSchi2tgTAvOQ5I_Pxw51phqjsRieEdAO4Kydvx906U-DX2iVT67I3IrPAtu_iMFQz7mnoWbAGmPiJrrEhdaX76q-Np4yYjBqxO93rQ3pYzlbIJvcaPPsFAhDzZp0u9YLcbvR9_qKSzzHiymC66JGs4B_2k4OkODy4mMtAraSocmq6d9omBeBITuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jXb90NFstZN0RS8WIXAfrJPydHVxL_FyloRZK-FVRAzK9pPEXsJhixX2_0ABmLNOde0Lgd1D3tTLXKi7ajIS_gwrl-OE8OKGMvg4Upt5lGVoZEZfYe-3vwz_de3jd3JEg8mG4CSkSPlqLUfVQO5x6eQ4xZDgnj7TYoN-DWnVIaOdCz8pv4watlvlE57tpgHHWZFF4xFMLB7oJhqmEQXalae-Pv0qWomI-Qbd8vHK1-Z5UxSjf-op5N8KafXZ39ze6-2cupvUoOLJiwJ0d0vBI04Fl7pzv5FfD7UkbC6H6CttgbI7MRaypzJs9LdBZvOxWk7_PeSVrmJ_nU05Yc31TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UzMCPQ5RzgMQQiUdfbq35P_WUx8xMJTeAmYgJdEagy28aCRC6P8tNrwL_vYR66D_PUD64Wjk2iuCd9UbQFvCCtSqtqbEw1mvcpkFiApaOM-xQiqHd1m0lSue0enSWd6QjN53d4nO-EepI48TqU-Gdbcwhr-yjTiTroWqok_J9xfAjMrkNWukkqAHfVGfLukqL5akLHRwLK-Qoj_aJBdYYZkPBu6mhHa8SnhUZaM6jGAcUu66zwdz0Ne6QHJjwtGnc6kudb0oHz21xtspjotgC53ydnINowvHJARAZyYSaVLyaKfkpNiAzmAbSgBMDZ2PoZRUuROmmKIPwtlSmokUDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cLP6QN6uUZUZs8zWI6ulL-za0DAHfNVy0UW9GWGf_XZvVYQeQctpFA8xvh_gHB8tjha-rnz7M8C84H09dAeeqXMAzX9wq4GrOc8i5w9mgmniJ3LBPLK9NLIahZaUmdhimEqr6jjt-gfaGOkmRL898c6VhQPsKb-W4WmNtC_GUKUFmIMchCkHxrbr3QFfOsZkEZUOXqDkzcNFMXOXzGin3Ci52QXiDtSwVVn58DKJzfIVKbGAQToa-2c2c-EHFkwBmZMOMKP3DGdljXnx2VKrwFhVMOWxwFLzTQqn_A68skmT6JU0BnZeHg9itmm0tplOrzrPPbi_c9wxaeRr3c5RTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XemLGu08MCGp0Au774rMRIg6tHEoozq5ROZfawTF7_9GS-Z0_VbNAwfgboN5rXDUrsRBxtwKY3l4vzkDhbYDmaY3zs_qxFwtXsnCHXlPQ2bYD9boFlcG8uqqXOSfF6d1UUDMFESIQR5KWFgbFUNMZvf3rWh-RZEvekFxYE77Bys5U2893SAic15FKmwSV3kNOai14hoOlP-bIES8QNfO4Sya2Sse9JlAQ6hBbOxYWJI-2pmfiwjpU-MuS1TVc39X77nwHjyRMSxny9hD9X5CUYxQ1GeX9o24pgtP5XrGjvhy-175IgG9RpuvEMk_QqgfFIt3SSOxklMl5WQLIND2yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4ldHBaHh1AL3AnH-2PGnTk6BrpLFHYAsX2XNxoQ8HO_Px1KY3K10umsRlNSc9A8Fh8GOgWHBagn6S4Gp_nbOua3TQ_Df7k2iCCF9kdMUTupkWUGpHREvQezmjQHN2-4GZf_G6bugS-Z_KI_MifMJbLKPx8c_z0PHfnf6l0IK2_fDZxoxRQGZBitpejQzcvtK-eh5CBx49QgEutn65TCQD8TqVTCMdIhgkNhTeULbReRFFPq9Dk8jdQixWVJvEbItUL6Td3xEEvzd50awW9a_rQ7cUZElXQk_-RPg3KPxfwAMh86kMCmRaQsy5M7Jl3s7PMk0KjxB-Lua9AGRnO_Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U7fq0x3oqR9FwUdAcXOPBTGzFr5xtqg8iIdEsDYrSTDRRc_CGHzxPBtv_mVT19X0RnD4iBT3cBiWW1dzGRCzRMMyijKnlsCZ7Q1iLXTZ8j2pCaZvI2ClpNr3B7TtbOu1E4Q3k7BvG16JsdiPdjzh8t7GLyn5HgV6qx690K9p9vK5VK72L0bOzog_er4D_BHJIH4_n1T1bdHGBOVvgHSVvtreR4IAVjuZQxXqF3hWk_-LE0wnEMRCtMmzDSSdBVBouYysbcHkZz-IY7rMWsXp-kBtAk1W8Q8QvWsM7A9owre8RSo2BJxGhNXt-eGtfThObIXUa3X1naaDN1jPKQpJrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K1XUtQqZy_NmHQRTYGAsLSN2HhntgQ3nO5u7HdYR0aGbx3ilhGEJ1N29AseG0BEQCQpHjJ_ObOzJt3u7jaAdq5c-HnQwNd3jaX5eP0H-n9iBGR28u8_ZyygIhvoRprNwlSabYWXSFXUtZwtu-0H5d7ezrveCk-Uf4XB7DpIEtw35uVX00h3ZpB05Bfk3cF95ZKVHMw6C7qgj1_BbWwXwOZZ-PpY9l3BKdg4B121WlsEGOlvctI_lDt3iIiqXQ8GTXwZV539Kg8OO7wRvD3hlD4IL4BEABF1wTfVy6_Ud29kMO410RbuRdLR6NTDa-PXgh56zcYzOPhdEQjEyUf9fAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cdHzyrcsKzCFL7YwclBaIfKaUUwGq72bG_2n4_a9HCUq5C98c5bPmTZ42K5HQA-ml3FR9zVR0Rm4hXjstGjz4Urh9QXU9ku0-5S3utPbjJiPzYpoa0m5VaWrxnmrJcwyF8lonAZgYr55MEyViXyMGP7M4ZRPyje4Z7ydB_KzVGYmd1MWuiXLdrVvypuzgeoSyvLiFSjs0Vv5FhFCkvWz8cAo_bYNkDAAnKGYRBxX2AATyBplVGApUx-NfR8ECL8nZGtX6173tv32_sZ64EIliuLZeLqyMWBInUSNbR_pHiOiNk2qNmQBhrp6zQBOwldavNRsWkIi44inkmZ_XtM83g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از حادثه ترور نافرجام رهبر شهید انقلاب در مسجد ابوذر در ششم تیرماه سال ۱۳۶۰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/664055" target="_blank">📅 23:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664054">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
پشت‌پرده درگیری های شبانه ایران و آمریکا/ یک اشتباه باعث «جنگ بزرگ» می شود
👇
khabarfoori.com/fa/tiny/news-3226117
🔹
ادعاهای تازه درباره نحوه ترور شهید کمال خرازی
👇
khabarfoori.com/fa/tiny/news-3225979
🔹
نانسی عجرم: امیدوارم تیم ملی ایران ببازد!
👇
khabarfoori.com/fa/tiny/news-3226080
🔹
جانشین ولادیمیر پوتین درگذشت! | سرگئی ایوانوف که بود؟
👇
khabarfoori.com/fa/tiny/news-3226136
🔹
کلید صعود ایران در دستان این مرد است
👇
khabarfoori.com/fa/tiny/news-3225973
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/664054" target="_blank">📅 23:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664053">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce687d0de.mp4?token=G0WXZP3FceAkpo0CdFhCfnUAIqh-cpPNNw9TTYKAkXjS-vRUtnqTJxYD713Pfe5XnAVHPtBK8fBf4v4x9O3ytvfmN1E1kZh1i5eZXJBNbvkZ5o4S7Tr0ncul2dzrB7moXK7iX9PaJCA03zwz437g0BiVG-Rq5sBM-6njn4VFhANHMfSGXR67qNEf2z6wu43LIPO8f5Csvf07cyyIkkg_BcYLn4P2pGdpskpXMUsudix1Q4VbehadhPxtQ3WEH2ULpGnAbd7s1Yi0S63iBQrfYa70y528f2TkJc3oGY1-rGsyien7xcOsEWDTS1R95Ds5KhX8tN61ceaaeceSt-x_WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce687d0de.mp4?token=G0WXZP3FceAkpo0CdFhCfnUAIqh-cpPNNw9TTYKAkXjS-vRUtnqTJxYD713Pfe5XnAVHPtBK8fBf4v4x9O3ytvfmN1E1kZh1i5eZXJBNbvkZ5o4S7Tr0ncul2dzrB7moXK7iX9PaJCA03zwz437g0BiVG-Rq5sBM-6njn4VFhANHMfSGXR67qNEf2z6wu43LIPO8f5Csvf07cyyIkkg_BcYLn4P2pGdpskpXMUsudix1Q4VbehadhPxtQ3WEH2ULpGnAbd7s1Yi0S63iBQrfYa70y528f2TkJc3oGY1-rGsyien7xcOsEWDTS1R95Ds5KhX8tN61ceaaeceSt-x_WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار حسن‌زاده: نماز در صبح روز دوم مراسم وداع، بر پیکر رهبر شهید انقلاب اقامه خواهد شد؛ یعنی صبح ۱۴ تیر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/664053" target="_blank">📅 23:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664052">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
بیانیه جمعی از اعضای مجلس خبرگان رهبری پیرو پیام راهگشای رهبر انقلاب
🔹
جمعی از اعضای مجلس خبرگان رهبری در پیرو پیام راهگشای رهبر حکیم انقلاب اسلامی (مدظله‌العالی) و حوادث اخیر، بیانیه ۱۰ ماده‌ای خطاب به مردم بصیر و انقلابی ایران اسلامی صادر کرد.
🔹
در بخشی از این بیانیه آمده: از ملت عزیز تقاضا داریم که کماکان حضور آگاهانه و با صلابت خویش را در میدان ادامه دهند و ضمن حفظ اتحاد مقدس و پرهیز از هر اقدام مخل این اتحاد، به سخنان تفرقه‌افکنانۀ برخی ناآگاهان که به دنبال محدودسازی این بعثت‌الهی هستند اعتنایی نداشته باشند. حضور مردم تازمانی که رهبری معظم (مدظله‌العالی) مصلحت بدانند ضروری و تعیین کننده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/664052" target="_blank">📅 23:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664051">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
سردار حسن‌زاده: مسیر اصلی مراسم تشییع رهبر شهید در تهران
🔹
خیابان دماوند-خیابان انقلاب-خیابان آزادی-اتوبان شهید لشگری-اتوبان آزادگان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/664051" target="_blank">📅 23:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664050">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKWt9KIxxzaZU95SPnyf2D5-riKycVUKRCraV2MJK_twlFh5og-c8qARnks9bfUO8mARmAfXPbNUkzwEy1GgE3eO_HcsV3cW_x1BNFGleQ6Zax9aaRj7NREOR9LLoqyuSNvq9GTBwmlSBEbr2IuNPdHn5rjOtdGEMzu9NMZvFmz2oM3gBqNfJrrtyUKU4prncyuc5N19NeP7QxuV2lRfWFmX7Ll6uwxpbidsWdW1w7luAia4MPYk5RsxcS9xV5AF2VPAqbyJyOZgJbe6Uc8p-ynm15mmKQNYqu0cG6zAfcjbkoSDtosxqlDlYIl-3j7mSDl0aMRzesuHf-ESd0Y_eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ دوباره دست به دامن ai شد
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/664050" target="_blank">📅 23:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664049">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24769656e6.mp4?token=m_RIwizhbSdUPkdNlhPeIOGT0XMf5wkhRNS3wGUzIF1qvxOVVt7TEfeLEV1WfvwiooxGUz7eXf_MWE9wR5q5doUiCODSJTK6YW-y-8Gg9jYBXeUuUlvR_SiiVZkUVIJG3og-uc9fqpZCmVQv_qo67ef3z2lQpxX9utd9vxCvJfBgDCpO8lXe4qa4rgtw2TBI5frKezyJRkXOwNlgz_xC7hE_117XTlvYOaA67RYFzPf6E3bm8HUFYCR7X7JTXJmMX5QB5hxn4bcwriN9AFSsu0OlWcBATzU-h7CIFsIQM8fziNisWziVv8wKs_T8naVJiyp3teFpDVR2GOg4ps489w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24769656e6.mp4?token=m_RIwizhbSdUPkdNlhPeIOGT0XMf5wkhRNS3wGUzIF1qvxOVVt7TEfeLEV1WfvwiooxGUz7eXf_MWE9wR5q5doUiCODSJTK6YW-y-8Gg9jYBXeUuUlvR_SiiVZkUVIJG3og-uc9fqpZCmVQv_qo67ef3z2lQpxX9utd9vxCvJfBgDCpO8lXe4qa4rgtw2TBI5frKezyJRkXOwNlgz_xC7hE_117XTlvYOaA67RYFzPf6E3bm8HUFYCR7X7JTXJmMX5QB5hxn4bcwriN9AFSsu0OlWcBATzU-h7CIFsIQM8fziNisWziVv8wKs_T8naVJiyp3teFpDVR2GOg4ps489w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علت مخفی و مرموز از آفساید شدن گل بازی ایران و مصر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/664049" target="_blank">📅 23:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664048">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
سردار حسن‌زاده: ما نمی‌توانیم در مراسم وداع با رهبر شهید توقف جمعیت داشته باشیم
🔹
برنامه‌ریزی این‌گونه است که مردم از یک نقطه وارد مصلی شوند و پیکر مطهر را ببیند و ظرف ۱۵ دقیقه از آن بخش خارج شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/664048" target="_blank">📅 23:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664047">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcsGj78JfDMWCetoeh8GR6yXBuZgH-SUjwz5lO08PljHvRP52-0LqGXltE6DYRB010SlhCGtDBDSkUU_7ZgNAVmc2SkZbEcHmBiuzrhzZvzx4oMN37eV3ujcWuQp8FMjWaxjmpjaTe_n7vQOQyTYHNzNmKNfW01dpsH0kj-glTf7OhXMIF6TEQJuJFvr8XMhBbMyHaX2qiX6pp9Tke6dk_m6xPt_xJOjDGhtsuZzZs-Q_myCReJxqJrs2bGeWVat-rFy1lnPu8cdutbVYe6K-3l-W-Gej143yc4gMXPvUDnUaQEuaRqe9t2lifF7IYcyEdK9gwDM0rzC5aIWm0zyrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: این یک تناقض آشکار و استدلالی مغالطه‌آمیز است که با هدف فرار از مسئولیت بابت همدستی در یک عمل شدیداً متخلفانه بین‌المللی مطرح می‌شود
🔹
از یک سو به‌صورت علنی هرگونه کمک یا حمایت از متجاوزان را انکار می‌کنند، اما از سوی دیگر آشکارا به ارائه «حمایت‌های فنی و لجستیکی» اذعان دارند؛ حمایت‌هایی که جنگ غیرقانونی آمریکا و اسرائیل علیه ایران را ممکن، تسهیل و پشتیبانی کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/664047" target="_blank">📅 23:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664046">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
رکود در مسکن ادامه‌دار است
سعید لطفی، دبیر اتحادیه مشاوران املاک تهران:
🔹
دولت باید با در نظر گرفتن وام‌های کم بهره، از خریداران واقعی مسکن و خانه اولی‌ها حمایت کند تا بازار مسکن رونق گیرد.
🔹
وقتی تولید مسکن نداریم، نمی‌توانیم انتظار کاهش قیمت اجاره‌بها را داشته باشیم.
🔹
تا زمانی که دولت از خریداران واقعی حمایت نکند، رکود در مسکن ادامه‌دار است./خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/664046" target="_blank">📅 23:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664045">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdb08ab33f.mp4?token=IVC3Q8ol3AVjUcZ8yPeImvKqM-RF5SQAl9OBznQZiXbrSOrHvJYChbh-mUVmCBR26QSADSyqtvBzfMQurgL89Oito_U6nOCw_pem0BmmsHliF9KtAYYObIRDCcspSfe52d7xbgmWx_dJ7OfeYpbJYWDU9TebrY2TbSPteZfvYOcxfgkMKIORJ6GSKWCtMQu3yZnNgJgBnSuHUf0Ny1Xc02DNtLU86EICwVNMRUqdERaGWDTfukHMqY6N0ntXy6ur5-cFlMKJs2vC3jGJmusMD28Eqm4T9qNCI4fp-QYU9ONRDbNC0hcz8iu_IBSXrMd56QqC_P_xRwESAHizlGnA6XizemnqPDHA130gn-qzmZpNFi3PYccIGhnrBs8krsAo7Zw4EgLkrMPEaaPyiDuQoYej8IZUs6uaE0DvbkKoBlQL1USXn97EWYP4DSMGGH-TTc4pbe93C-t1B258BTpIa5UR3ZVfBJn4py_qV_VMJDHMY8kQg1sgwmoKA1DHqZ3qcdF6OSC9XqhNG6MoaCJ_5KxtcqyzWxAAWHsmxTOR11XijDYp2ZWOsafsMuWonFMc_VpWpKAI0FXHzMaj6P9rzZEuwoZYIb5EMBWjql9hPW6uktTOKnzcMo2odnqqYe6HX8akx6TJuPvhGGMCEba7uR3A0zAzXPQrTSrN3lcHogw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdb08ab33f.mp4?token=IVC3Q8ol3AVjUcZ8yPeImvKqM-RF5SQAl9OBznQZiXbrSOrHvJYChbh-mUVmCBR26QSADSyqtvBzfMQurgL89Oito_U6nOCw_pem0BmmsHliF9KtAYYObIRDCcspSfe52d7xbgmWx_dJ7OfeYpbJYWDU9TebrY2TbSPteZfvYOcxfgkMKIORJ6GSKWCtMQu3yZnNgJgBnSuHUf0Ny1Xc02DNtLU86EICwVNMRUqdERaGWDTfukHMqY6N0ntXy6ur5-cFlMKJs2vC3jGJmusMD28Eqm4T9qNCI4fp-QYU9ONRDbNC0hcz8iu_IBSXrMd56QqC_P_xRwESAHizlGnA6XizemnqPDHA130gn-qzmZpNFi3PYccIGhnrBs8krsAo7Zw4EgLkrMPEaaPyiDuQoYej8IZUs6uaE0DvbkKoBlQL1USXn97EWYP4DSMGGH-TTc4pbe93C-t1B258BTpIa5UR3ZVfBJn4py_qV_VMJDHMY8kQg1sgwmoKA1DHqZ3qcdF6OSC9XqhNG6MoaCJ_5KxtcqyzWxAAWHsmxTOR11XijDYp2ZWOsafsMuWonFMc_VpWpKAI0FXHzMaj6P9rzZEuwoZYIb5EMBWjql9hPW6uktTOKnzcMo2odnqqYe6HX8akx6TJuPvhGGMCEba7uR3A0zAzXPQrTSrN3lcHogw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت رسیدگی به هوا و خنکی برای گاوها در خارج اروپا خیلی بهتر از مردم داخل اروپاست
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/664045" target="_blank">📅 23:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664044">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8b1b81c91.mp4?token=otE9rxorrPhGfxcK1pj4Rl5XgSuzXJm_I58KKR5FfUh-I0742BvdKP5QbbQx2B7PZ_546Q5k-6a8NriH2uDcx3oFcLxjbrIP6hPv06bIht3-7260CQxD7fiucoWz1rUzCh8ea96vRaCIKP10zmUc0TI8LO24_FncY08F8epGAt2y6a8uerkb3VZg3Meg4dV35WlbeSZ9O7XEhnecTCCR8qo6BAXAfi3V6G2antJnkZQEitYCjUlJYSQ560X8Ba1tT6yB4QmB2r8oJRsaGaP07aYHq4fRJmbChgaP8YaY3bceohQrdOcdZFKe8N5QUyxdHuiahJ86zxnlxbX1B4RgMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8b1b81c91.mp4?token=otE9rxorrPhGfxcK1pj4Rl5XgSuzXJm_I58KKR5FfUh-I0742BvdKP5QbbQx2B7PZ_546Q5k-6a8NriH2uDcx3oFcLxjbrIP6hPv06bIht3-7260CQxD7fiucoWz1rUzCh8ea96vRaCIKP10zmUc0TI8LO24_FncY08F8epGAt2y6a8uerkb3VZg3Meg4dV35WlbeSZ9O7XEhnecTCCR8qo6BAXAfi3V6G2antJnkZQEitYCjUlJYSQ560X8Ba1tT6yB4QmB2r8oJRsaGaP07aYHq4fRJmbChgaP8YaY3bceohQrdOcdZFKe8N5QUyxdHuiahJ86zxnlxbX1B4RgMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار حسن‌زاده: در مصلای تهران بر پیکر رهبر شهید انقلاب نماز اقامه خواهد شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/664044" target="_blank">📅 23:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664043">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
ادعای وزیر جنگ رژیم اسرائیل: اگر ایران علیه اجرای توافق لبنان اقدام کند، پاسخ می‌دهیم
یسرائیل کاتز، وزیر جنگ اسرائیل:
🔹
به ارتش دستور داده ام برای حضور طولانی مدت در «منطقه امنیتی» در جنوب لبنان آماده باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/664043" target="_blank">📅 22:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664042">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ju1gfignLK30NQ3Y05xzwSHg88ZYaI2ApLV_H6onv78dX9ph_PY8gOdpPIUfjcThswPKSYs2fGnR0Ua8B41P45IwXBLXeRL1OhMAQ3680DhvDyn2TdsQ5Mde8pwSFnlGjOwg1R1RtEjS4XzW3RV1bTAd_ijFzdOqJP_K0px_5aLQ6eWllTjs-kmlNjsKdxHGmRHabUKPZuqvcbQES-pHm19LazEfja6Eh1SqizVbZxNEgS3-tUuj2ld8_fTwj-NFjlr2qfHWYztXlqzrK9-vCteNIeLGOndO0C1zs6EUpZ_srrvG9c4lBi293_12cB78ZwgQty-S2-SEe5XLi_NEyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه مدت‌زمان انتظار برای دیدن پزشک متخصص
در کانادا و در بریتانیا بیش از نیمی از بیماران باید بیشتر از ۴ هفته برای ویزیت پزشک متخصص در صف انتظار بمانند.
ایران با ثبت آمار تنها ۲ درصد انتظار بالای ۴ هفته، یکی از در دسترس‌ترین سیستم‌های ویزیت متخصص را دارد.
میانگین زمان انتظار بیماران در ایران برای ویزیت پزشک متخصص فقط ۴.۳ روز و برای پزشک فوق‌تخصص ۷.۶ روز است.
@amarfact</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/664042" target="_blank">📅 22:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664041">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
۴ فرد مسلح به یک مقر نیروهای شبه‌نظامی در شهر کراچی نفوذ کرده‌اند
🔹
در حمله به کراچی، کشته‌ها و زخمی‌هایی وجود دارد و در حال حاضر امکان تعیین دقیق شمار تلفات وجود ندارد/انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/664041" target="_blank">📅 22:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664040">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cb911549f.mp4?token=k_CudD69BJ4X15TLr-sID4fshGX8rBHkXzKDrQv4KDnkUYNSpvDTsm8mp8x4a0R1jQAuIWXY_1iPxUwxcd4mvTkkvlspl-kDuzZYnh8cboYpxD17ZWNgSb8TdKRHmg1FARfMffIOBeFmpPblP7dxBqfNT3XIUi2Ld60Z4lYQlTB2rUHprrsoGd_cW7b3Ioz1QDKzC4pLjGJG90Yg3tlhNWqiqTmHVKErnrO_kroEbtH9Qs3f68kONCHN3XQV_c4TJCEDe1li_KGffXC-gcjyuvf2R_VHcbauPWsDjIJatXqcTW_Sazj8HtDP_XzPqVtMTWGo_8YloPGH9rfwnaQ7eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cb911549f.mp4?token=k_CudD69BJ4X15TLr-sID4fshGX8rBHkXzKDrQv4KDnkUYNSpvDTsm8mp8x4a0R1jQAuIWXY_1iPxUwxcd4mvTkkvlspl-kDuzZYnh8cboYpxD17ZWNgSb8TdKRHmg1FARfMffIOBeFmpPblP7dxBqfNT3XIUi2Ld60Z4lYQlTB2rUHprrsoGd_cW7b3Ioz1QDKzC4pLjGJG90Yg3tlhNWqiqTmHVKErnrO_kroEbtH9Qs3f68kONCHN3XQV_c4TJCEDe1li_KGffXC-gcjyuvf2R_VHcbauPWsDjIJatXqcTW_Sazj8HtDP_XzPqVtMTWGo_8YloPGH9rfwnaQ7eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار حسن‌زاده: در مصلای تهران بر پیکر رهبر شهید انقلاب نماز اقامه خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/664040" target="_blank">📅 22:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664039">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
دومین تیم صعود کننده به لیگ برتر فوتبال ایران مشخص شد
🔹
تیم فوتبال مس شهر بابک پس از کسب پیروزی در هفته ۳۱ لیگ آزادگان، مجوز حضور در رقابت‌های لیگ برتر را کسب کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/664039" target="_blank">📅 22:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664038">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-hv0Bxf-swBtAr6KPvmVGgHpP9nwtry4FJJltb8a8AHNToh0kPgNP9y_BWjGwhwbuhGdAjNREZCABGdLXYo1xUcLVhzdgyIa698czNg5OAnFBkQmBDwm1SJZTWRQZUnEiO4rIkCyAgFahOTHC2cv6j4XEZE-ju_HoCJDSU6iWs3YKlRfT1iWwphYNfN7zRlByTzAgAjChGuDSP4N00Xv52CtP4j_C_6fVAytnWQ-N4Obrizj1PlPeuydEePyVWCf6rAsqtbNAGH5le_bkARtvPWeYcVgmegPKmPL9XGJNMUvoR05J9NKnMuevAKCPDy1X1pC_L0711HqHbxPRPrOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت‌پرده درگیری های شبانه ایران و آمریکا/ یک اشتباه باعث «جنگ بزرگ» می شود
🔹
رابطه ایران و آمریکا همواره در خطر بوده و این دو در «لبه تیغ» حرکت می‌ کنند و ممکن است هر لحظه وارد جنگ بزرگ شوند‌.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3226117</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/664038" target="_blank">📅 22:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664037">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R59carns7NS7yrQKvLAvgIGwN6lv5VgIKocO_tuVjdtg4KjdfU9N74AWDSFlGH-ziz4uIbAo_ISzCa45KXXsv0a3EM7k_RF797Ie0XqyjgdP4kTBT4tqbAn4kq_RjTwiq-JQWXBHEDE8SWFMU0zwp1MbMRv4KpZhRgCOIehHwx45hM3LJW24BY4UJuDtQzrvFdrK9Kp0yjM8ZEeaXjBXpc_4HM3FNwZpnQfo9uMIbzDz1Q-pRj2w64a2Y6PNKKZYKnZl4YNcgxcRdaBu9QsUReFkcoBTiPVIKGTGE5I21oes8rkOHqEInsazIjbCxXlSYfjhiktTNdmMp6exfz8KBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌ان: شمار قربانیان زلزله‌های مرگبار ونزوئلا به بیش از ۱,۴۳۰ نفر رسید
🔹
مقام‌های ونزوئلا اعلام کردند شمار قربانیان زلزله‌های این هفته به دست‌کم ۱,۴۳۰ نفر رسیده است.
🔹
پس‌لرزه‌های متعدد عملیات امدادرسانی را دشوار کرده و نگرانی‌ها از افزایش بیشتر تلفات را افزایش داده است. هزاران نفر نیز در این حادثه زخمی یا بی‌خانمان شده‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/664037" target="_blank">📅 22:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664036">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd486c8659.mp4?token=vMLL0CvUfQrp5fqWuTBQu3MpmUef9xI1SdR1y0tuv_sVeCTMxXI8LWoRfoKxrLAX1ecEh7NI9p64MrPQGyF7tI7BKsFMhc8h9np1E6NCyGnOHXmzKk4GJvU22I0VXJuC6T_4lK__WRsJLimjCNRRNNmy7TB6gwVM43Rd7mx8_E6iHiVrb__2QuYOSWWOVPGt03NWfbD2amd3Y24s4gNd9At6zhxz27mRgcF5p7hrvoeYLlkyBz6rSX8hsZcPWaUbhJFqe3CRoEvKH3SGy808BCmv3H8ZXNAuWXBCAlNOUYJnxkczTPnR8mB6gIYTGd83adGUHAkJN9MREx6xpR-utZnLOyhZ9uA_Ni__wVzDcCEgbMsZ2E0L-KmYzZysh34ylfrR6jCHZdhbuUolYjG1lIIeecoJJjPxunCzde43iXd-WnLS8DUej879Vpf0BkEzUxjmyZTXyuB2zXoph8LQuA1n7B_vcjw8sKghxjwdjkbkVHmcbkuFZzPUqjiyI3nvORie7xzEE_2y1W4yDwZSgUedq8AUVw9yW1aKxJP0gQ-xUIJLMparAPZRp4vyd9fNXIPvGPvM-iewTzeJceE0nuIO-0OYghXjx7J-qGOm79RDL28kcfMJH5UbjqIjjq5xh2LxW17uSqRiUqBebNHCBVpX0Z8XXoMPSaVZ331Qh0k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd486c8659.mp4?token=vMLL0CvUfQrp5fqWuTBQu3MpmUef9xI1SdR1y0tuv_sVeCTMxXI8LWoRfoKxrLAX1ecEh7NI9p64MrPQGyF7tI7BKsFMhc8h9np1E6NCyGnOHXmzKk4GJvU22I0VXJuC6T_4lK__WRsJLimjCNRRNNmy7TB6gwVM43Rd7mx8_E6iHiVrb__2QuYOSWWOVPGt03NWfbD2amd3Y24s4gNd9At6zhxz27mRgcF5p7hrvoeYLlkyBz6rSX8hsZcPWaUbhJFqe3CRoEvKH3SGy808BCmv3H8ZXNAuWXBCAlNOUYJnxkczTPnR8mB6gIYTGd83adGUHAkJN9MREx6xpR-utZnLOyhZ9uA_Ni__wVzDcCEgbMsZ2E0L-KmYzZysh34ylfrR6jCHZdhbuUolYjG1lIIeecoJJjPxunCzde43iXd-WnLS8DUej879Vpf0BkEzUxjmyZTXyuB2zXoph8LQuA1n7B_vcjw8sKghxjwdjkbkVHmcbkuFZzPUqjiyI3nvORie7xzEE_2y1W4yDwZSgUedq8AUVw9yW1aKxJP0gQ-xUIJLMparAPZRp4vyd9fNXIPvGPvM-iewTzeJceE0nuIO-0OYghXjx7J-qGOm79RDL28kcfMJH5UbjqIjjq5xh2LxW17uSqRiUqBebNHCBVpX0Z8XXoMPSaVZ331Qh0k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور هیچ وقت سرطان نگیریم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/664036" target="_blank">📅 22:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664035">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ادعای ونس: قیمت نفت الان به ۷۳ دلار در هر بشکه بازگشته، در حالی که تا ۱۲۶ دلار رسیده بود؛ این نشانه‌ای است که یک اتفاق واقعی دارد می‌افتد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/664035" target="_blank">📅 22:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664034">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
بقایی: ظرف ۳٠ روز از توافق نهایی نیروهای آمریکایی باید از منطقه پیرامونی ایران خارج شوند
🔹
جزئیات این گزاره باید در حین مذاکرات مورد بحث قرار گیرد.
🔹
یک تعهد دیگر این است که آمریکا در حین مذاکرات به نیروهای خود در منطقه اضافه نکند
🔹
ما این موضوع را به طور…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/664034" target="_blank">📅 22:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664033">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef2292562.mp4?token=qVT3-ooJmC19h_bkA7qQU5HjghyJqe56P24Ig-AZXLK6LAWah7kktTUx_WBeqHD_MftyFXZEEeJ0bgahexxHq0krsCn0Jf8mDqQ58-Dqmqsq-T8wBQ8HQ77PBTXi0aO5km-uDvp9h4eh96qomSCtbxSmBZ4ruqv9E8WeiBvLwtpA85SqlXAIjvZ8Kbpy_4hNZ5NkXbdRqiXMbTKHlil4ZawNQxERWLHv6f7UYGRhU3v4wvQyZnQkOyO1U2V1mQXvwfo38YjVmIxAmKMv_05HTn-M_cst6piDkB27EciB0V16l8SQI3LGl5ybzuws6Yayle4TP2EJ-tGJxLkq30UHiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef2292562.mp4?token=qVT3-ooJmC19h_bkA7qQU5HjghyJqe56P24Ig-AZXLK6LAWah7kktTUx_WBeqHD_MftyFXZEEeJ0bgahexxHq0krsCn0Jf8mDqQ58-Dqmqsq-T8wBQ8HQ77PBTXi0aO5km-uDvp9h4eh96qomSCtbxSmBZ4ruqv9E8WeiBvLwtpA85SqlXAIjvZ8Kbpy_4hNZ5NkXbdRqiXMbTKHlil4ZawNQxERWLHv6f7UYGRhU3v4wvQyZnQkOyO1U2V1mQXvwfo38YjVmIxAmKMv_05HTn-M_cst6piDkB27EciB0V16l8SQI3LGl5ybzuws6Yayle4TP2EJ-tGJxLkq30UHiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راه حسینی
🔹
همراهان عزیز خبرفوری ؛ محبت به امام حسین(ع) در صدای شما جاری شد. روایت‌هایی کوتاه از کارهایی که به عشق سیدالشهدا(ع) انجام می‌دهید.
🔹
این ویدئو، روایت شنیدنی از صدای دل‌های شماست.
🔸
الوفوری را دنبال کنید
👇
#ایران_حسینی
@Alo_fori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/664033" target="_blank">📅 22:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664032">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
کیفرخواست پروندهٔ رضا پهلوی و عوامل اینترنشنال و من‌وتو صادر شد
دادستان تهران:
🔹
کیفرخواست رضا پهلوی و تعدادی از عوامل شبکه‌های اینترنشنال و من‌وتو به اتهام زمینه‌سازی برای اغتشاشات روزهای ۱۸ و ۱۹ دی‌ماه سال ۱۴۰۴ صادر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/664032" target="_blank">📅 22:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664031">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b451747df6.mp4?token=IzPGNIurJ_WG3Nf8rXgkAiUoXmPTwpp5fIsHmP3tK0X6ak99ZKlNDCNFhwlC_uT1k6UjmG0KGGZYQ2jiKbHNA2Sw4ugrdUFXLtYT0OKfJH9C5DInVUfDj2Ad9y-E-sXH9fhIGxPYdYmt4qQ9fkAN-Jdl4k5ae9CXFPxkpsMhk6o8Ie1Brm9LNPI8jdVwBq3rcVvWLG70pbxqRMGms1Al2uJXhK7qNteQjUUFxgPo0HRK9NONZmDx8DmuAmPPhc5NozXXd_eghwEuaTFTLPrvcymsc3PDkJhUNbZX6eeCkUyzAXyXEsUEDgQx2ln29O0Ghh2NeNdEcJkNNyKD-4jx2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b451747df6.mp4?token=IzPGNIurJ_WG3Nf8rXgkAiUoXmPTwpp5fIsHmP3tK0X6ak99ZKlNDCNFhwlC_uT1k6UjmG0KGGZYQ2jiKbHNA2Sw4ugrdUFXLtYT0OKfJH9C5DInVUfDj2Ad9y-E-sXH9fhIGxPYdYmt4qQ9fkAN-Jdl4k5ae9CXFPxkpsMhk6o8Ie1Brm9LNPI8jdVwBq3rcVvWLG70pbxqRMGms1Al2uJXhK7qNteQjUUFxgPo0HRK9NONZmDx8DmuAmPPhc5NozXXd_eghwEuaTFTLPrvcymsc3PDkJhUNbZX6eeCkUyzAXyXEsUEDgQx2ln29O0Ghh2NeNdEcJkNNyKD-4jx2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهوی خبیث، دقایقی پیش، از عون و سلام، چاکران درگاه ترامپ در بیروت، اینطور تشکر کرد: از دولت لبنان بابت شجاعتی که نشان داد، تشکر می‌کنم #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/664031" target="_blank">📅 22:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664030">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a7cfe3b9.mp4?token=HvpTWJ3twkkG5ES1CalLIA9L7PW_2GSKjK6UeTWmaKr_nY-OjN1fp8bvNOro33CEd3KlPWJswA_PgvAJQFZDfkmpAgeH826F7w0LuQtgsgZpjtFnntePA5Q3w8RdykZjiUq8vng6TyJitMSqMOkUgeLn-s4byoL0G1Zk-KJRrIXnutjZgOr4EkD1E4brvFUnGmEWSLB-lp0LZVaeUbiBfJJqoktYMaEyoed6K2-OqT9K5FTtx1-T8hGJOFtoaewXJwpGE8C7pGXCmygEhpF2ns-O3PS3DG_aKlJlwGXkpKGtw4VBPzQ-vRfB4rSyaJs9iS70u-MphQKozrtIZr36Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a7cfe3b9.mp4?token=HvpTWJ3twkkG5ES1CalLIA9L7PW_2GSKjK6UeTWmaKr_nY-OjN1fp8bvNOro33CEd3KlPWJswA_PgvAJQFZDfkmpAgeH826F7w0LuQtgsgZpjtFnntePA5Q3w8RdykZjiUq8vng6TyJitMSqMOkUgeLn-s4byoL0G1Zk-KJRrIXnutjZgOr4EkD1E4brvFUnGmEWSLB-lp0LZVaeUbiBfJJqoktYMaEyoed6K2-OqT9K5FTtx1-T8hGJOFtoaewXJwpGE8C7pGXCmygEhpF2ns-O3PS3DG_aKlJlwGXkpKGtw4VBPzQ-vRfB4rSyaJs9iS70u-MphQKozrtIZr36Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
بیمه؛ طاقی استوار
…
بعضی چیزها برای ماندن ساخته می‌شوند
مثل اطمینانی که دوام روزهای سخت است…
✅
بیمه‌بازار؛ همراهی برای آسودگی
#بیمه_بازار
⁩
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/664030" target="_blank">📅 22:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664029">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
عراقچی به عراق می‌رود
‌
🔹
وزیر امور خارجه جمهوری اسلامی ایران، فردا یکشنبه در راس یک هیئت دیپلماتیک به عراق سفر خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/664029" target="_blank">📅 22:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664028">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
نتانیاهو: هیئتی را به واشنگتن خواهم فرستاد تا منافع امنیتی اسرائیل را در رابطه با پرونده هسته‌ای ایران تبیین کند #Demon
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/664028" target="_blank">📅 22:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664026">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
اندیشکده آمریکایی: ایران از اهرم تنگه هرمز به طور قابل توجه استفاده می‌کند
اندیشکده جنگ:
🔹
ایران بر الزام خود برای تأیید عبور کشتی‌ها از تنگه  هرمز پافشاری می‌کند.
🔹
این امر اهرم قابل توجهی به ایران می‌دهد که می‌تواند به دلخواه از آن استفاده کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/664026" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664025">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iw9tFmuaOmIQev3bN9qAq1ZhiAsZcpQPfO76JXcQZNKC9WqmfqB1bx2dapTo2ntEWgrSb12Gr2PectjhK1gEQf2UqW-uUsWORjetitRJQKEzMRQ51smvWDcyaxai4Mr8-Eb3pAuJ4qbzXwe-HkOOmtmw_OSvEj8qi7CAG27QkqU0no7cmBgUZZNFTJe9u833DpPaCC0bBu_YEwmnM-RxPofWSzYcknwpZqAwMUcR5WTnAWByZtDxeGVLE-s_TyrXaqDrRDXsirIDRL8gt-SvlbRylIHcqKwCiIHgkGkqVoxjJ76kcZ4rbpt4zpVD1hMsisXPHwFaNjp8TY6bmvJn5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چگونه قلب دیگران را تسخیر کنیم؟
🔹
امام علی می‌فرماید: هرکس حق کسی را ادا کند که حق او را ادا نمی‌کند، دل او را تسخیر می‌کند؛ زیرا احسان دشمنی را به دوستی بدل می‌سازد. قرآن نیز به دفع بدی با نیکی فرمان می‌دهد. در حقیقت، انسان‌ها بندۀ احسان‌اند و با نیکی…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/664025" target="_blank">📅 22:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664024">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
استاندار خراسان‌رضوی: محل خاکسپاری رهبر شهید در حرم رضوی هنوز نهایی نشده است ‌
🔹
به تأکید رهبر شهید انقلاب محل تدفین باید به‌گونه‌ای انتخاب شود که زیارت حرم امام رضا(ع) تحت تأثیر قرار نگیرد. محل تدفین هنوز به‌طور قطعی تعیین نشده و چند گزینه در دست بررسی است./فارس…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/664024" target="_blank">📅 22:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664023">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
نتانیاهو: به ارتش اسرائیل بر داشتن آزادی عمل کامل برای دفع هرگونه تهدید در لبنان تاکید کرده‌ام
🔹
ما به اقدامات خود در لبنان علیه هرگونه تهدید فوری ادامه می‌دهیم؛ روز گذشته ۷ تن از نیروهای حزب‌الله را که در خانه‌ای دور از نیروهای ما بودند، هدف قرار دادیم.…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/664023" target="_blank">📅 21:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664022">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
نتانیاهو: آمریکا و دولت لبنان با ماندن ما در منطقهٔ امنیتی جنوب لبنان موافقت کرده‌اند
🔹
اسرائیل و لبنان بر سر دو منطقه امنیتی برای راستی‌آزمایی و خلع سلاح حزب الله توافق کردند.
🔹
توافق با لبنان را به لطف ضربات مهلکی که به حزب‌الله وارد کردیم، به سرانجام رساندیم.…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/664022" target="_blank">📅 21:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664021">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
نتانیاهو: ما طرف قرارداد ایران و آمریکا نیستیم  نتانیاهو مدعی شد:
🔹
دولت لبنان برای اولین بار می‌گوید که خواهان صلح با اسرائیل است و این یک تغییر اساسی است. #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/664021" target="_blank">📅 21:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664020">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
نتانیاهو: هر زمان که لازم باشد وارد خاک لبنان خواهیم شد و در آنجا با قدرت تمام عملیات انجام می‌دهیم #Demon
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/664020" target="_blank">📅 21:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664019">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
نتانیاهو: هر زمان که لازم باشد وارد خاک لبنان خواهیم شد و در آنجا با قدرت تمام عملیات انجام می‌دهیم
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/664019" target="_blank">📅 21:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664018">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زیارت-عاشورا-pdf.pdf</div>
  <div class="tg-doc-extra">115.8 KB</div>
</div>
<a href="https://t.me/akhbarefori/664018" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
فایل pdf
#متن_زیارت_عاشورا
همراه با ترجمه
@Heyate_gharar</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/664018" target="_blank">📅 21:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664017">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">-زیــارت‌عاشـــورا</div>
  <div class="tg-doc-extra">علی فانی</div>
</div>
<a href="https://t.me/akhbarefori/664017" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
صوت
#زیارت_عاشورا
🎙
#علی_فانی
@Heyate_gharar</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/664017" target="_blank">📅 21:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664016">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b29a5b4f0.mp4?token=cF7_dREhepUueVsFHmyDdLp5vg9vxWVtSdawimkVSKJxBGjcQDUNh34qdkN8JZQ-VPdz6xz9pJQq4gM9KbpYbGSAE_SzXOJ3XEtsrgxDYtXoYQM7ITSGjNTuTZeGw29sambx8tLXgP_QUb2pcjO_UvqlfvRL8HnB0hZ2d_Dio8-mlzuf_NHAaGv1l7hAsAblIEwn23DIKym9ZpoP0NhV5M2UkDfPSt8FbbVekZZgDmYkFzlerkoJx_Cpd_ykzem0RmZjyuYSBSZ7jYrs-xr7hIhf4YcF42b9ZBRgo62qn4HgBRQHXhhKXcWvPX6Gqqk6LAmcu31iv3E4-b79EB_Maw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b29a5b4f0.mp4?token=cF7_dREhepUueVsFHmyDdLp5vg9vxWVtSdawimkVSKJxBGjcQDUNh34qdkN8JZQ-VPdz6xz9pJQq4gM9KbpYbGSAE_SzXOJ3XEtsrgxDYtXoYQM7ITSGjNTuTZeGw29sambx8tLXgP_QUb2pcjO_UvqlfvRL8HnB0hZ2d_Dio8-mlzuf_NHAaGv1l7hAsAblIEwn23DIKym9ZpoP0NhV5M2UkDfPSt8FbbVekZZgDmYkFzlerkoJx_Cpd_ykzem0RmZjyuYSBSZ7jYrs-xr7hIhf4YcF42b9ZBRgo62qn4HgBRQHXhhKXcWvPX6Gqqk6LAmcu31iv3E4-b79EB_Maw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ترفند مهم و مفید برای سلامتی بدن
‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/664016" target="_blank">📅 21:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664015">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXymGruTvu9XBv0tw3SnjJLBiEmRKeaSu8xh9gtLi1Qd6X_X_yLKTFpYNX_8r7O2-26KaPtZJOKZYFeoDAq9BTWCpKo0Nq5Vu6miwKGeI7UqA67n_RCFxMYTRUlskihvtgIfyNhtBjMG_LnYJRngZBgz7jUPsRmkE43GYa6-7kgquO1mNligNMYoPfx9wRMpjtz7H3xyMp8Bs8f-PWRa2hpeS788KfuAlKLvFJvhcsUQ-Xwrw4ymzcCw3P2QMGTAk-3oS5Ni7sJ45bbPFhZk77y9u9J4oJwhS4wxm4Mrd3sbBWeF4Pr_6c4SQ7jF5GtqitENwS85xbANjZYT3Kltqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتانیاهو در سایه سکوت خفت بار مقامات لبنانی، رسماً اشغال خاک لبنان را کلید زد
🔹
نخست‌وزیر رژیم صهیونیستی در یک کنفرانس خبری با نمایش نقشه‌ای از مناطق جنوب لبنان، مدعی شد با مقامات دولت لبنان درباره حضور و اشغال بخش‌هایی از خاک این کشور به توافق رسیده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/664015" target="_blank">📅 21:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664014">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ونس مدعی شد: مذاکرات با ایران موفقیت‌آمیز بوده است
ادعای معاون رئیس‌جمهور آمریکا:
🔹
اگر با ایران به توافق نهایی برسیم، عالی می‌شود.
🔹
افزایش جریان نفت از طریق تنگه هرمز نشانه‌ای از وقوع یک اتفاق واقعی است، اما توافق آتش‌بس با ایران همیشه کمی آشفته خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/664014" target="_blank">📅 21:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664012">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc606f8ae6.mp4?token=HeS1oXgg6dlZwDy8OZ-KHdcaDWc5tSMpHvsk0_N1OVqBYeh67QBPTOrioeqXQOR5AD5iLr3amFwge7CROIqCrTqF1DCFDhHYIRIKmoRPw0ecCpP-zMqjpPqhswf2xfNkU3HzEDmFr-NtWqhw7bUs1YuHdr9AzXARSvRyK5ZrlPH17M8zcQt87nRhMf-qmCKGvfY_qWlzWO8WH613uDLPzyiSvS9kKWGd9OmoE9Fxg0d0ol-scZCC8nb_0RivwBMJfYM3jI7wDVK9VnPijLvyUoMuV9FmVuSxDavpGegLY136dMLWyMAMy4jC3FRCttgNNjp0Ya9TzgaX25vGjHmin79VvmJ3gkmi0t87hMc57EYlKQb6QX8SHz6cZvA5Z90GyOSW4iJwL70c0WUZtYH7mKevgafFLnyVS3WRwROh5nRxDuXpfvqcITVyC-dANFLsK4Zm-uxmyA846atsRpBDv7puPvXc0eN0jUJCVURmQ9bFRLgaLylM7YGjbdyETs-LOnDJV0Ok4FcnW5FZ3cZuVNQqwRY7HE5Wam-JYk8Ae3-5CTqKvvZ4zokaYu9LzEdF_XCRp68HkjkttQjGgCqoDTPSG4vkns7MsODhdqccJjrBMArbo-KOB6Y0N4H_Tj8BR32MhLqHewtTxlrZL-VU4eIOvezEP2DV8e4M3v3FlcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc606f8ae6.mp4?token=HeS1oXgg6dlZwDy8OZ-KHdcaDWc5tSMpHvsk0_N1OVqBYeh67QBPTOrioeqXQOR5AD5iLr3amFwge7CROIqCrTqF1DCFDhHYIRIKmoRPw0ecCpP-zMqjpPqhswf2xfNkU3HzEDmFr-NtWqhw7bUs1YuHdr9AzXARSvRyK5ZrlPH17M8zcQt87nRhMf-qmCKGvfY_qWlzWO8WH613uDLPzyiSvS9kKWGd9OmoE9Fxg0d0ol-scZCC8nb_0RivwBMJfYM3jI7wDVK9VnPijLvyUoMuV9FmVuSxDavpGegLY136dMLWyMAMy4jC3FRCttgNNjp0Ya9TzgaX25vGjHmin79VvmJ3gkmi0t87hMc57EYlKQb6QX8SHz6cZvA5Z90GyOSW4iJwL70c0WUZtYH7mKevgafFLnyVS3WRwROh5nRxDuXpfvqcITVyC-dANFLsK4Zm-uxmyA846atsRpBDv7puPvXc0eN0jUJCVURmQ9bFRLgaLylM7YGjbdyETs-LOnDJV0Ok4FcnW5FZ3cZuVNQqwRY7HE5Wam-JYk8Ae3-5CTqKvvZ4zokaYu9LzEdF_XCRp68HkjkttQjGgCqoDTPSG4vkns7MsODhdqccJjrBMArbo-KOB6Y0N4H_Tj8BR32MhLqHewtTxlrZL-VU4eIOvezEP2DV8e4M3v3FlcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حفظ یکساله و دوساله قرآن کریم به صورت رایگان
✅
ویژه دختران و پسران۱۴ تا ۲۲
🔹
اعتکاف با قرآن در جوار حرم مطهر امام رضا علیه السلام
🔹
اطلاعات بیشتر در
👇
http://Samenoon.com
https://eitaa.com/samenalhojajj</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/664012" target="_blank">📅 21:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664010">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
ایرنا بررسی کرد؛ عدم پرداخت حق عائله‌مندی به همسران بازمانده تک‌نفره، ناشی از قانون است
🔹
عدم پرداخت حق عائله‌مندی به برخی همسران بازمانده تک‌نفره مستمری‌بگیر، این روزها به یکی از مطالبات مطرح‌شده از سوی این گروه تبدیل شده است.
بر اساس گزارش ایرنا، عدم پرداخت حق عائله‌مندی به همسران بازمانده تک‌نفره ناشی از چارچوب قانونی موجود است.
🔹
طبق اعلام سازمان تأمین اجتماعی، این سازمان صرفاً مجری قوانین است و تنها می‌تواند مزایایی را پرداخت کند که در قانون برای آن پیش‌بینی شده باشد. در قوانین فعلی، برای همسران بازمانده تک‌نفره تنها مستمری بازماندگان در نظر گرفته شده و کمک‌هزینه عائله‌مندی جزو این مزایا نیست.
🔹
بنابراین، در صورت طرح و تصویب اصلاحات قانونی، امکان بازنگری در این موضوع وجود خواهد داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/664010" target="_blank">📅 21:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664008">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtJp1jnohHmIswdUJ9N6PEOkKMmzUbeJb--d5yMNSX6GI7OVb7858DwaJ1tZnvmQ5pvSqyuB4xkjTuk5VshjdNIf-jyc_mZaRj8kWjpCaNKMphHT32XfXeZywgzVYZL1MNbNwkaMHTtc3WlQNa7-7tRwtxXMjuXy3Hfy-2MGPJmpOEoKMp6xGq5b3UU0jtKQxzjlRf89uve-RGt5th2FQ5xMZp22W3zxZJ4-P5citlR6yI0Qks18Jy2CZBEJsTQiqeScTyu2IUaPdbcxZZLCIAtPKQb_ziJoJq3vBv1L8kqqpbIcqgWm70gm3jJYOe3tXCHyMrctes39bllHFqC-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خیز مرد شیعه برای شکست ترامپ و دار و دسته اش/ ممدانی، آماده جنگ با مرد مو زرد
🔹
جرات و شجاعت جمهوری خواهان در انتخابات 2016 سبب شد که ترامپ به قدرت برسد و حزب جمهوری خواه یک پوست اندازی مناسب کند. دموکرات ها از این پوست اندازی ترسیدند و به همین دلیل، انتخابات 2024 را هم علی رغم تمایل کمرنگ هریس به سوسیالیسم، باختند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3226025</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/664008" target="_blank">📅 21:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664007">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c05CjH-u72dD8XGPrlfYrOfsP_mLyA9_eGk9NqKSUUYtUnyWQcQcEljOY18-wSNzuo7nt_Y0unx5K2IdGxV7x6B67ibU5HR6PI5FBXqIScwWXIN9gcI3hNd-OzivNUN_SPta-MuomyYeP50N2hJ2uVC8QXhKxQxOhWgYBd5ddqvJQG01f4ULLxDwzRXxJ5bf2XkU7YWAzZTOfJWUdrVPbX5rSrb-7-XDn7L2w4i3zcy3vWBTLCxO9lDeo1b81PSvVHFDFeISXsb-68-BWXgfV1ZTzUYzgG3x1AcrSzHxwdMYeJNJjLoMcwuQsLIaB43e9-v4L8c-GEZJnRv1GkT0Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رونمایی از استوک‌های جدید نایکی کریستیانو رونالدو
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/664007" target="_blank">📅 21:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664006">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
۱۰۰۰ مدرسه تهران آماده اسکان زائران رهبر شهید  وزارت آموزش‌وپرورش:
🔹
بیش از هزار مدرسه در تهران برای اسکان زائران آماده شده است.
🔹
زائران بر اساس تقسیم‌بندی ستاد برگزاری مراسم به مراکز اسکان هدایت می‌شوند. #بدرقه_یار   #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/664006" target="_blank">📅 21:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664005">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOf1asrHyrOBTn6Ovc26_MxpYxQ0Z88VT0f1IgN6RDwrGhoIjm9kYuDKQ-my877iXj4-zQgItMJsvoTUliQKxI_C5GbwGxFa48ESk3CI9xLcWR9FubU4cPHtjRSa0XkCTK26Qkf126SkLjJaKi-QHzB4PDwJk2Ko-Z8sYzpDIZXz_zI8E5_EYvpPnJbbhHVb4DSEYS7SElGAjmTyLvtqIsEFzNpUuOP9olgxTe_URcSrvRjB8NArHJXUqjokDN6uJh7v6o-wp0dYBdDWE_cX-bDNt4gvyHunCc7vNRCYNFmG0S02ocdL9-pcnQC1MRZApkF3WtfC0CHaM4r77A7OGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی سریال: سوپرانز ۱۹۹۹ـ۲۰۰۷| ( The  Sopranos)
🔹
ژانر: کمدی سیاه، درام مافیایی
🔹
امتیاز (IMDb): ۹.۲
🔹
خلاصه: رئیس قدرتمند مافیا، کسی که همه از او حساب می‌برند، ناگهان خودش را روی مبل یک روان‌درمانگر می‌بیند. سوپرانوز از همین نقطه شروع می‌شود؛ جایی که قدرت، خانواده، خشونت و روان انسان در هم گره می‌خورند و سریالی می‌سازند که به عقیده بسیاری همچنان بهترین سریال تاریخ است.
🔹
۶ فصلی
#فوری_فیلم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/664005" target="_blank">📅 21:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664004">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_i-wRWQCSttOXGZ9HYTjoQsPL7AVHXhAQBFbaY7qkxEUN1gN1czXeEvKVC7QewDlEzmtAE1KKi8LddQWXvGJ4qd07h0W-PYfpAyVQ8h7dSYJWTh0omy9NblDN4qfc37bkP-iiLMTDegvl1RFJ3zrPY-WtEPIXustE63ANrMl7QtR_E34j1rPIvzQYerlh37-l4V_FIrAoEx7ei1IGC6J-FxtplYTV7PcELF7AVe4uzsoUF1oUWptQmuGt7L4jWkGQFxJ-7gfN6iMOxteTOoayFPBIknr07Ms7RCX9ZASLLw3BCRX34AE4_53wAOts9g3OUH0Le5zZxv2KAXDAQKjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت‌های محلی در صدر انتخاب‌های عزاداری محرم
🔸
در این نظرسنجی بیش از ۳۸ هزار نفر شرکت کردند که سهم روبیکا ۵۴٪، بله حدود ۳۳٪ و تلگرام ۱۳٪ بوده است.
🔸
حدود ۸۳٪ شرکت‌کنندگان در عزاداری محرم شرکت می‌کنند و ۱۷٪ هم شرکت نمی‌کنند.
🔸
بیش از نیمی از شرکت‌کنندگان برای شرکت در عزاداری محرم، هیئت‌های محلی و حدود ۱۸٪ هم تلویزیون را ترجیح می‌دهند.
@amarfact</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/664004" target="_blank">📅 21:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664003">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
برخی خبرگزاری‌ها از قطعی برق بیشتر منطقه پیروزی تهران اطلاع می‌دهند
🔹
مشکل فنی در یکی از پست‌های ۲۳٠ شرق تهران علت قطعی برق است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/664003" target="_blank">📅 20:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664002">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f64a18e0.mp4?token=G3XXLWfea5mxquD3nlfSnRuqxxCkebDZ2zf4LO7AuFxGctNLYa0MLEWtosoGYcPE_D90ZvmaM9nVPjI0y2ogFcBPRk_3PXJySFOrHEkhjXN4J2B0E2Pt9sKUyiH4sx8LIyYU-59GDJc80D31sAshG1r50DhSjl0JVMtHt-R69Xtp4b9r2nnmIvN6Qklp7WCBMl3BvMUtfnLS2oRrmXqQag0H8rCKUG1N8m4cwnnAjGChqe1_scv5ge7lbMYwclH5ZUI4sTWnHWELd-sYadqMZ0wWsyHLK6qD-aSwYzAVeOZMdeS0NmMDyKKgNi5por3f_GczJ7GP1oyxrjOKyo1vwgWJYXbX5KqVZhj-qjL8kemoTd3TA8mkgPLxZWn5XCpemcfN-4QQNg6XQMSOFMHIRSrLLe-WphOdLHeHj09iZc3JcWWjWox3l-FdLhDatlxnLXbNF7dl5rGaMadeGA0rQzG135pB-Z9oTtn1bF19waMmCvW8wT8_q4BQJSejC4YHlnvncmN6bi9A8Fic_TyJeTbzJDDU0-5bl1r3lozgB9vBpmpeyq-wY7LjISY8Nsdg3bpMClO6IUGaZr9rDoiDgFuKxCq2pzEvqyOeUunurrfxb7w-tXbcOIOUhe2odN8PxXLSsFcP5qyl9b8UBPXnykOsd_Od6KdH0F6m-mFqpFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f64a18e0.mp4?token=G3XXLWfea5mxquD3nlfSnRuqxxCkebDZ2zf4LO7AuFxGctNLYa0MLEWtosoGYcPE_D90ZvmaM9nVPjI0y2ogFcBPRk_3PXJySFOrHEkhjXN4J2B0E2Pt9sKUyiH4sx8LIyYU-59GDJc80D31sAshG1r50DhSjl0JVMtHt-R69Xtp4b9r2nnmIvN6Qklp7WCBMl3BvMUtfnLS2oRrmXqQag0H8rCKUG1N8m4cwnnAjGChqe1_scv5ge7lbMYwclH5ZUI4sTWnHWELd-sYadqMZ0wWsyHLK6qD-aSwYzAVeOZMdeS0NmMDyKKgNi5por3f_GczJ7GP1oyxrjOKyo1vwgWJYXbX5KqVZhj-qjL8kemoTd3TA8mkgPLxZWn5XCpemcfN-4QQNg6XQMSOFMHIRSrLLe-WphOdLHeHj09iZc3JcWWjWox3l-FdLhDatlxnLXbNF7dl5rGaMadeGA0rQzG135pB-Z9oTtn1bF19waMmCvW8wT8_q4BQJSejC4YHlnvncmN6bi9A8Fic_TyJeTbzJDDU0-5bl1r3lozgB9vBpmpeyq-wY7LjISY8Nsdg3bpMClO6IUGaZr9rDoiDgFuKxCq2pzEvqyOeUunurrfxb7w-tXbcOIOUhe2odN8PxXLSsFcP5qyl9b8UBPXnykOsd_Od6KdH0F6m-mFqpFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین اخبار و حواشی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/664002" target="_blank">📅 20:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664000">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
مردم نگران پیامدهای اختلال‌ اخیر بانکی نباشند   بانک مرکزی:
🔹
در پی اختلال‌ ایجادشده در بخشی از خدمات بانکی، بانک مرکزی از نخستین ساعات وقوع این شرایط، موضوع آثار ناشی از این اختلال‌ در امور جاری مردم و فعالان اقتصادی را در دست بررسی قرار داده است و حمایت…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/664000" target="_blank">📅 20:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663999">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUbnSg-HapVr_Uru3ulYxx1MN39L5uLQHHTzqakVCRUUB7Fu_1iz-kRz6sJqwl8DNCUHcNmJfw_GHMgHYHgYgd8F7EsbvFX5vMLMiCgFELomMAlIxVf3HHXvaITPP_bfybN_al9PZvt9Z4af2QtY0EORufTK45HRuXANbCHq7ZMg8RFcCbbq1LKB_vP1BbtOp0QcTvNYTIYg2-tymN0T0NV6kHcUlUOfhXTb5fnQ1fQNpxNY0L4Ay0cou5BAwO4ih6igfECF5ydoHKi4QSf8hYDCEEFUBu_RQXA_n_UdaZ4VzY3WU7dl1ULWLDTdtBsiEwuf9UFg4nMcPmMoxivAAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصر مادر دنیاست و ایران غرور دنیا
🔹
نوشته امروز یک شهروند مصری در سیاتل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/663999" target="_blank">📅 20:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663998">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
روایت تکان‌دهنده یک تجربه نزدیک به مرگ؛ ادعای سفر تا آسمان پنجم و بازگشت به زندگی
🔹
00:05:30 رنگ آسمان دگرگون شد و آوای آشنا خبر از مرگ داد
🔹
00:23:20 دعوت شدن به آسمان هفتم برای ملاقات با پروردگار
🔹
00:30:50 جوان ظاهر شدن روح پیرمرد در عالم برزخ بعد از مرگ
🔹
00:41:45 خبررسانی از درگذشت فرد آشنا در بازگشت از کما و صحت‌سنجی آن توسط خانواده
🔹
00:45:35 متوسل شدن به حضرت ابالفضل در زمین و آسمان
🔹
00:57:00 عدم اجازه ورود جبرئیل به آسمان هفتم
🔹
01:03:00 محدودیت‌های دنیایی انسان در مقایسه با عالم برزخ
🔹
قسمت بیست‌وسوم (وقت رفتن)، فصل چهارم
🔹
#تجربه‌گر
: حسن‌رضا هادی‌زاده
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/663998" target="_blank">📅 20:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663997">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70efb8d7c.mp4?token=sFUNz33jC-VCyxvi1BK5qDXzblp8dzk1Aq6UT2rhUOGNULdkRX80MEpjHeHrc33DVYDKPX_Yr5BvduRCdl4oKp8Anl6LaxOdkeNDefUqdJxKSmdnDTQEgW4VYMG2UaBeVvKHkSTDjN_T85CvErfLd1fiZPTFFiqtAZANx1F_3Lr5jIdhBHOpgJe4PqCw77fqqXnDl7M5MeVfQZMrY5d1J93fesMyjC-cXxEql3MWVJs6dT4cByCNNNVns7g5MNdJHWqf1wntBiqYjM1z1QkBPCwNOFXS7d0vkmYXPVh6c4ygH2JDeaS7QIlmfFyoeOYiLZz2HbaHwnFyAxCnxdZ7aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70efb8d7c.mp4?token=sFUNz33jC-VCyxvi1BK5qDXzblp8dzk1Aq6UT2rhUOGNULdkRX80MEpjHeHrc33DVYDKPX_Yr5BvduRCdl4oKp8Anl6LaxOdkeNDefUqdJxKSmdnDTQEgW4VYMG2UaBeVvKHkSTDjN_T85CvErfLd1fiZPTFFiqtAZANx1F_3Lr5jIdhBHOpgJe4PqCw77fqqXnDl7M5MeVfQZMrY5d1J93fesMyjC-cXxEql3MWVJs6dT4cByCNNNVns7g5MNdJHWqf1wntBiqYjM1z1QkBPCwNOFXS7d0vkmYXPVh6c4ygH2JDeaS7QIlmfFyoeOYiLZz2HbaHwnFyAxCnxdZ7aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سفیدپوشی سبلان در نخستین روزهای تابستان
🔹
در ششمین روز از فصل تابستان بارش برف سنگینی قله مرتفع سبلان را در استان اردبیل سفیدپوش کرد
#اخبار_اردبیل
در فضای مجازی
👇
@Akhbarardebill</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/663997" target="_blank">📅 20:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663996">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmGAszWCzBgUrdhrXWn3EZd0yH2Nzf6_FTeU03QkZsh_6LYGzPHModWQzYQTmk7y4QgI1DF8R1C5NOH_775l0J--11X2umyX89ga1pLiJ5V2EKQgiURVhOR-We2-DJF4Il9qxuTrYGxy7wjYLgVzrdyqfJRUwDvoN_lqUGQHdti-5mXu9rz4uyL3mfNmFOhkzujytxP00Kuq5worLZhftBz98_aCC3QxC5iUYCtK8SygOcNWX_7JQjJYqAUz-CgJDz6T-z_3JDrfZs4X-jEAs_oxOijF1MOq5TAnHNGGBZXrQR8NYV5uSuFqVH-s89dbjhg27hE6WFjcdGqd70xqPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
به تو از دور سلام
چله زیارت عاشورا تا اربعین حسینی
#روز_سوم
▫️
امروز با خواندن زیارت عاشورا به نیت شهید بزرگوار
آوینا برزگر
، دل‌هایمان را به سوی امام حسین (ع) میبریم. امیدواریم که ایشان ما را پیش اربابمان شفاعت کنند
@Heyate_gharar</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/663996" target="_blank">📅 20:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663994">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJd939om1OERzrCe5Pd4B-awHSLIIGaTRx9mwyzlHZuv_SZ7EAbDLyJ4HTb1ZlIWbLWQmcT-WiVtYxXj0ox58ugs2KKoxKjelSikaQ_ZVoKh0C0E4GzbM-WLx1VHlj5RA-FQqOyMs0YLWqfSTrP9XaL0buGbQoPI8AtFRbLtz0lexZ8O1DlEOwNp9KXdI1PLAZLWWvl7NileOaR0lE5pcbJkaIHIFDl4_siXGnYA6jJ6nvlupkKxhlS1i6knGeU5zF8KAyf39lee0sginBwHsDFQE_xWLw5coM0aMQDaEhMRicRDF3-kYF6NzSX_3tgn3fcLqevSqhHu0XgmrUkycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jjgGLunDCkbI8hS9jADUlABs3CcfoOCvGzFI8Mkz_MoCvhvRfcWS5WRtbiys1A6A-NzXa6OQh5zMHc5LdPfMBlWU8ZuIo6BbezPFzbLVSr-liBPP5g3rh_xAu-tshtApPmu4Zg8hkp1nPwYKBFXwr-3Ye16cf3TLBuTii-vulng_yhjfbmb8Pff9BBqXOosFs6bVAhC_dggRbGmje5Czi_IBW6Fdt9gJxmy0lxQWYK26L3LPNQlzxROBEO_2h0thMzfdYP0pCpCaLVk313U-YYyoMNQHBWMH85rxDudyeuK7F8PbWyapO_-oaVRc0LodllW-zlWI_nTn1DuMwZ-ZYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پیراهن‌هایی که هیچ‌وقت از تنِ فوتبال درنمی‌آیند
🔹
«پیراهن‌های همیشه» با قلم جذاب حمیدرضا صدر، سفریه بین اسطوره‌های فوتبال؛ از پله و کرایف تا مسی و رونالدو، با نگاهی احساسی، نوستالژیک و پرشور. کتابی برای عاشقان مستطیل سبز که قصه مردان ماندگار فوتبال را طوری روایت می‌کند که هم هیجان‌زده‌ات می‌کند، هم دلتنگ.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/663994" target="_blank">📅 20:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663993">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f5c83348.mp4?token=MyJTyTSDKCF9EJDkMh_TCwPwIAfrkaZYPJz2jQ4dU91nK_JbvOfFrZ0udxiabsqHJYdZtGTPoHmLiNCLyxtRIHRYV6SDNt0947MxGpQJMCwYvxo-kh9lk_i04PKob2m4Hf4O00G7nPSvPC0uVsZuPdfmRCSW6Jw9NW-y5nZ5RzNtkv0GRwiftRSPNWSLoirYgb6RexPUeGDQYxGm1DxBYc_vBtGTI1-n6j6t6lcxUGxYwYbNyeDWTTi_ztGU1FZoFrFlb04LTJe6UPC7dJboJ-ABtm-JtlIVK06gInuOevgtzC6WRJu9Q6uRnrU8EzJVoLuk0JfRmq3nV33h4zvqBowYW09dCZxv9yIuHUxko0NKxXdRTWpaaXC53SldpWcfA39ixSHh04fH2NzF-qjGtStvkXJ4Mx7fjbVau9zXuTvk-j4G7IYSkeA9nFtaoxtAMIHhjwRQDS7agWOVnYtTJ-K2_qkVRpppsQkUThLLtxLXe-D93kTawnK1wp8jFz4QV9I_cCbAkl_UuO8OppcHweXZQLKf8P-Bi-C7P0q4AtSQ2ezk4_zllDjpM9WCZswdHTvm5JRIXnWThGVQe7LMzaW_21FJiZ6GJBk6xtUeR7v4J43bMXixL5sTkCTub_ixDFKjsh_G7kiBNEEbft6EofaowrJv3YtYmqUy98sjVxk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f5c83348.mp4?token=MyJTyTSDKCF9EJDkMh_TCwPwIAfrkaZYPJz2jQ4dU91nK_JbvOfFrZ0udxiabsqHJYdZtGTPoHmLiNCLyxtRIHRYV6SDNt0947MxGpQJMCwYvxo-kh9lk_i04PKob2m4Hf4O00G7nPSvPC0uVsZuPdfmRCSW6Jw9NW-y5nZ5RzNtkv0GRwiftRSPNWSLoirYgb6RexPUeGDQYxGm1DxBYc_vBtGTI1-n6j6t6lcxUGxYwYbNyeDWTTi_ztGU1FZoFrFlb04LTJe6UPC7dJboJ-ABtm-JtlIVK06gInuOevgtzC6WRJu9Q6uRnrU8EzJVoLuk0JfRmq3nV33h4zvqBowYW09dCZxv9yIuHUxko0NKxXdRTWpaaXC53SldpWcfA39ixSHh04fH2NzF-qjGtStvkXJ4Mx7fjbVau9zXuTvk-j4G7IYSkeA9nFtaoxtAMIHhjwRQDS7agWOVnYtTJ-K2_qkVRpppsQkUThLLtxLXe-D93kTawnK1wp8jFz4QV9I_cCbAkl_UuO8OppcHweXZQLKf8P-Bi-C7P0q4AtSQ2ezk4_zllDjpM9WCZswdHTvm5JRIXnWThGVQe7LMzaW_21FJiZ6GJBk6xtUeR7v4J43bMXixL5sTkCTub_ixDFKjsh_G7kiBNEEbft6EofaowrJv3YtYmqUy98sjVxk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای عجیب شفا گرفتن دختر «شهین تسلیمی» در کانادا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/663993" target="_blank">📅 20:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663992">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlV0DdRiKLiBp7zlEEYk7ZM2zCb18mj31Ddb00yMrM7foRUxhNT-aORYTNYFRnlBwj_HJN4MKgxKaVLL0fWysiJxxiY_KsOE1ew2r0sszIP8lupPrwLBfKtB4ECIhZdDuq-X0K1VDOltRCUX9O-0WPtqdtvnmg-VlVdfY_5qj3GD-nGLk_prsjPX-oOIzf5rbeZdEv4iKDk0fML3mnWZi83HQtCc8N8I1QVt1FUyVRmhkMJqz3Nbn1ESitJlKIsQynpVD0HMp7Adq-m7CLtwdOc_xsjw6BMoPl13tayWdQ6AIsgagsnrCjOHfvsN6IfQ-ky-4S2OvEsTFZJPQ9ZAPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚘
بازار خرید و فروش ماشین از نگاه شما
در یک نظرسنجی کوتاه  شرکت کنید و دیدگاه خود را درباره بازار خرید و فروش خودرو با ما به اشتراک بگذارید.
🙏🏼
🎁
به پاس همراهی شما، یک هدیه 3 میلیون تومانی به قید قرعه به یکی از شرکت‌کنندگان اهدا می‌شود.
🔹
بدون نیاز به ثبت‌نام یا اطلاعات شخصی.
برای شرکت در نظرسنجی وارد لینک زیر بشوید
👇
👇
https://survey.porsline.ir/s/sJ9hb8Dc</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/663992" target="_blank">📅 20:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663991">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02331900f.mp4?token=sCLiq64yPhVMx6qR-AtXeCO4KLZ6Nl4f-cSOSTonLGTPChC3QTEImNjl__avSQSri1z5ZUwYjIPL4fd_idGJ-YI_Vlm5Joo8KK1Gi6JxuYcppT5omyngmcz3qDDIiaFpVI0hBcomqcnumtBvMBu_b6N2QGhmBJxQPd9fMN5lP6SMtkoniOvVTXSD2BDrAhSkYD4hF70WBt7fUFQ7v-6k-NxoAbm3ty0o5REA_GSb9oVICjB1sB-HCxRbafGe8mL_lOOmOlwEdOF8rgvHOr10G1LuRGgP3SJ3M9YqJroDgCWUiBvIAJfUiC-REGiO-jQDLmIuBZiOa81_jKMv9MbUcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02331900f.mp4?token=sCLiq64yPhVMx6qR-AtXeCO4KLZ6Nl4f-cSOSTonLGTPChC3QTEImNjl__avSQSri1z5ZUwYjIPL4fd_idGJ-YI_Vlm5Joo8KK1Gi6JxuYcppT5omyngmcz3qDDIiaFpVI0hBcomqcnumtBvMBu_b6N2QGhmBJxQPd9fMN5lP6SMtkoniOvVTXSD2BDrAhSkYD4hF70WBt7fUFQ7v-6k-NxoAbm3ty0o5REA_GSb9oVICjB1sB-HCxRbafGe8mL_lOOmOlwEdOF8rgvHOr10G1LuRGgP3SJ3M9YqJroDgCWUiBvIAJfUiC-REGiO-jQDLmIuBZiOa81_jKMv9MbUcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی زیبا از دسته فلامینگوهای مهاجر در تالاب میانکاله
#اخبار_گلستان
در فضای مجازی
👇
@AkhbareGolestan</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/663991" target="_blank">📅 20:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663988">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Be9fyRS3Z8HOnfHu7NNn2ITeoLv4Ms_6u8PmK99yVJQAdyuIp4a6Ryk0lG1t0Py1zhuaRAPiFX6qoxmHI-lHrZQAH0VKKaecNri59oPRiovSuvAoONTxJa6vIBwEWBVX7HN5Icv1HA-ziakIt9uifft9av5lWqYkHx_AfUd5n9P96aikhniko5YoouCX8TlW4vL8YUNEFTtH1-_8XcUwjAvsJhGYA30pABsHrSJUG8mklO1B0hU6dTt6VJVdVVMpdpg-9WCgZfMUZviVfVpJ8Pp7bTAh4ROqftyhP8ZLvnM9ycXAVG2JMQh0kxlWJpaL_dE3oIszyl0QgVCz2n4TlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
آخر ترمه و پروژه‌هایی که عقب انداختی، همه روی هم تلنبار شدن؟
حل تمرین و آماده‌کردن ارائه می‌تونه ساعت‌ها وقتت رو بگیره؛ اما ابزارهای هوش مصنوعی مثل
ChatGPT
و
Claude
کمکت می‌کنن تو چند دقیقه انجامشون بدی.
🚀
اشتراک پرمیوم ابزارهای هوش مصنوعی موردنیازت رو با
قیمت مناسب و پشتیبانی فعال
از پارس پرمیوم تهیه کن.
💚
🎁
دست‌خالی نرو!
کد تخفیف اختصاصی مخاطبان کانال
خبر
فوری به تعداد محدود
👇🏼
FORI405
مشاهده محصولات و خرید
راهنمای خرید و کدهای تخفیف بعدی داخل کانال پارس پرمیوم
👇🏼
@ParsPremium</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/663988" target="_blank">📅 20:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663986">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSlHFJy9c_LJQe3FD0zI0vBmdywWtSsO2PR2meQsbzW9fOsQpLeExqa5weqNZTIdOFrvJx2kkhXZTKCmxM2UD8Droz5bkuyG2MYzwZmqvbt8SGVJOAJbfDPEmf7eFqHqPx4BTCq5keBJ15KWwsQvN9SsuTFwckplKSDBej3whYrfZPT7vUrg2CQsWfnhEai4fxRDDDbPr9W4MOisTV7h5Yv44f6juRUboskJPCdcYslP9xYETxo8GdRYvOvZi9YZVkPsfx-WLHYS94oKA2YOZ1SnjdYC25wNGusLQwIK54LiymirAxUtpYuLgwHZaCr6zeHGGOwd881g_AXcJIyw0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کرواسی را ببرید تا ما صعود کنیم
🔹
درخواست جالب سفارت ایران در غنا از تیم ملی این کشور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/663986" target="_blank">📅 19:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663985">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyLyTNUtfDJrjAsPTYu0jsNw68shTpXCj0GvdYlQYtoUp4664RaL7mn8Mmy6jttnoxUKZgG4NssoDOjeYd1N1t1feQjVVYY3YmJfQj1OG18j8FgOiRsBi4TOco6M0eRSIo8mhGlyh6BbukR17iK76Lu5Z6PqpJUYX7fgiuW1Ud1u1nk82IN-aRA5q2FERE9dwnTNH7vXM92yylC1KgqzxcvUIqPK3SK5n_SWmQ8BZO2JH5hF4_dBgY8MVHUBHJPnrz3m2Q1hsD3frK3lUsiOwglU20w9RUYcrK6gLgV9cJMCvC6aMpgR3Mi2FNlseWnvrPgvcW79o_1slfzG5ja4iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بز کوهی ماقبل تاریخی که در حال انقراض است
🔹
سایگا یک نوع بز کوهی است که در مناطقی که پوشش استپ دارند در اوراسیا زندگی می‌کند
🔹
این حیوان در چین و‌ مغولستان تقریباً به کلی منقرض شده که یکی از دلایل اصلی آن، کاربرد دارویی شاخ "کَل سَکایی" در طب چینی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/663985" target="_blank">📅 19:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663984">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a77dcd6e7b.mp4?token=Xmzq_KjCNPLKIjNDqkzgULDzbU9Rb8NXTyDv7ESZXDKlZh0x9YURyJAQQfDw7yQSQcbAxcTOFPjJx6w_JUbM2nSZ3KVGr5VzGrKpoxm2uQh2bQNFyyZNUefWb6b1rNu_RnQvBlAzYszLG5C288acFiSf_FbPEeYEUTtdLq9zv8nhBT3-jRMmyQjoCMe9Mnda3Kva_OytUEJIyUfp--4EUstm1GG_nuRwAYTk7E0Mq18-my69T1Mm1-Lv_Fx89yKw7GGGl8xMx2bOWVRCOa41UckUD8NSMHsYiIs8pLrD5KSLM45WaUMLAoBR1zUQP3fG7HgpNQDYdiztD3WXsi9Aog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a77dcd6e7b.mp4?token=Xmzq_KjCNPLKIjNDqkzgULDzbU9Rb8NXTyDv7ESZXDKlZh0x9YURyJAQQfDw7yQSQcbAxcTOFPjJx6w_JUbM2nSZ3KVGr5VzGrKpoxm2uQh2bQNFyyZNUefWb6b1rNu_RnQvBlAzYszLG5C288acFiSf_FbPEeYEUTtdLq9zv8nhBT3-jRMmyQjoCMe9Mnda3Kva_OytUEJIyUfp--4EUstm1GG_nuRwAYTk7E0Mq18-my69T1Mm1-Lv_Fx89yKw7GGGl8xMx2bOWVRCOa41UckUD8NSMHsYiIs8pLrD5KSLM45WaUMLAoBR1zUQP3fG7HgpNQDYdiztD3WXsi9Aog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسکو: پالایشگاه نفت اوکراین در زاپوریژیا را هدف قرار دادیم
🔹
وزارت دفاع روسیه اعلام کرد نیروهای مسلح این کشور یکی از تاسیسات مجتمع سوخت و انرژی را که در خدمت نیروهای مسلح اوکراین در منطقه زاپوریژیا قرار داشت، هدف قرار دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/663984" target="_blank">📅 19:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663983">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
اداره هوانوردی آمریکا: در حال بررسی ماجرای نزدیک شدن یک پهپاد به هواپیمای مسافربری هستیم
سی‌ان‌ان:
🔹
خلبان هواپیمای مسافربری شرکت یونایتد ایرلاینز اعلام کرد که  هنگام فرود در نیوجرسی نزدیک بود با این پهپاد برخورد کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/663983" target="_blank">📅 19:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663980">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
عراقچی: از هیچ تلاشی برای پیگیری فاجعه بمباران سردشت در مجامع بین‌المللی دریغ نمی‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/663980" target="_blank">📅 19:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663979">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
هزینه جنگ با ایران برای آمریکا فاش شد؛ ۷ میلیارد دلار فقط برای دو نوع موشک
پایگاه خبری UNN:
🔹
طبق گزارش مرکز مطالعات استراتژیک و بین‌المللی (CSIS)، بیش از هزار موشک تاماهاک استفاده شده، بیش از ۲ میلیارد دلار هزینه داشته و هزینه‌های موشک‌های پاتریوت به حدود ۵ میلیارد دلار رسیده است.
🔹
با نرخ تولید فعلی، ذخایر پاتریوت ممکن است تنها تا اواسط سال ۲۰۲۹ به سطح قبل از جنگ بازگردد و ذخایر تاماهاک زودتر از پایان سال ۲۰۳۰ به دست نخواهد آمد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/663979" target="_blank">📅 19:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663978">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-x6c1E-d_iKotRLPy6NTq4tiibMM2Om6pcx4AOpbAN0M15e0rN5mfK7R215X7OZd0aKPe6rPkRd5slvH7P2yYHIRwsVetpVgnpg69CLHJQwC5yUOm6EFE248zoOVgDkBuRp7-ww3K64QLp420HxbYs1EtytaLdYju0kT7dFU2DCQggtid8I3FXbyKljshNyq9rCPsVaRKnGmE-cUk0Ffd26pb940xM8q7Mm2qDkNi8eEep7qeZq1kBaYdlL7XPtDVZlM9g8o9WzCgm6hrJilinIGvdfQyouhZPOT1RMcb7zVd0S3nSItlenjgJqKIdhy-9GGiPCG6XhNnmIzbs2Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استان‌هایی با بیشترین تردد وسایل نقلیه/ یک چهارم ترددها در تهران انجام می‌شود
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/663978" target="_blank">📅 19:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663976">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
هم‌اکنون دود غلیظ ناشی از آتش‌سوزی لندینگ‌کرافت حامل خودرو از مقابل پارک آفتاب ۲ قشم به‌وضوح قابل مشاهده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/663976" target="_blank">📅 19:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663975">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-TIqNXzlmY5qTq4iLkRk71mqpLHSMJxLJgqTlq2nCOe4OATeIb0x-w5QcyX7cb8ZSM37Q9Ui_vasZs5cgKboFc13fjlQMqkvZDl6hltv9s6MrukTIh4VEQtRzj-ECpj32Y6sNmN16cy5unne6zLhmHeYjRUm73qTl7SpZiLUaaqmOAzmJlN9jd9R1GYRnOoMrJdrVOFbLYDMWRQjpnuHCxOcKu4CalLVWyD5sjM62LsTHdTJgJEgTkE1Ptpahs9PNv2Jps2yF20KXCe9K1n7xaebTq4MMX3mDhWxDxNKk2PXLtZTPz-1Ap0c9KzZP11tqUgas-G4BsPh36Ug3FpSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینفانتینو: بازی ایران و مصر تمام چیزی بود که فوتبال نیاز داشت
🔹
رئیس فیفا پس از تساوی یک بر یک ایران و مصر در گروه G جام جهانی ۲۰۲۶، از این دیدار به عنوان «بازی‌ای عالی و سرشار از احساسات» یاد کرد و گفت: «از دقیقه اول تا آخر، تمام آن چیزی که فوتبال نیاز داشت، در این بازی بود.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/663975" target="_blank">📅 19:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663974">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4150f04d6.mp4?token=u8x6OkefGPJE31-brbVvCgVlhW8Qw9N7sPE6sbdUoP5nYPEOjvyMfKQY1b5Wsnuv9oEWhEzFjelYxc6qhFZ53DNMwuPbf_TQGhMZVDTagd9o8PRRs7Wdbd6Qbl8caZ0Uv-gL4zbJf8wibRdjqC24w9FFzZfdJwGQGvSXiIwlCzv-jO5YEt_iwFjQGyswKUT9WKf4KAMCsY96mHMqzgLhAYnrQDu1icIqhuvGxz2jnA3BWwL2BFdm6eMbJ_Vu6R3mo4Je_CheQ3w0HrvjbHUY5FC--yysjQzXuNI3jEpOcWYAhlbgYWV5qme77E3n0g8cNDzQRx_9knhdiltcHcTEIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4150f04d6.mp4?token=u8x6OkefGPJE31-brbVvCgVlhW8Qw9N7sPE6sbdUoP5nYPEOjvyMfKQY1b5Wsnuv9oEWhEzFjelYxc6qhFZ53DNMwuPbf_TQGhMZVDTagd9o8PRRs7Wdbd6Qbl8caZ0Uv-gL4zbJf8wibRdjqC24w9FFzZfdJwGQGvSXiIwlCzv-jO5YEt_iwFjQGyswKUT9WKf4KAMCsY96mHMqzgLhAYnrQDu1icIqhuvGxz2jnA3BWwL2BFdm6eMbJ_Vu6R3mo4Je_CheQ3w0HrvjbHUY5FC--yysjQzXuNI3jEpOcWYAhlbgYWV5qme77E3n0g8cNDzQRx_9knhdiltcHcTEIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیتِ امروز صبح در سراسر ایران
🇮🇷
🔹
وقتی پای تیم ملی در میان باشد، ایران یکدل می‌شود؛ ۹۰ دقیقه هیجان، امید و همدلی
❤️
🤍
💚
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/663974" target="_blank">📅 19:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663973">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
پاسخ صریح و تند نماینده ایران در اجلاس بین‌المجالس اسلامی در باکو به ادعاهای نماینده امارات: شما شریک خون بیش از ۳۵۰۰ شهید و ۳۰ هزار مجروح ایرانی هستید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/663973" target="_blank">📅 19:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663972">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8117fb79ce.mp4?token=WfOrED-710fyaDmfHFgxULyGuEEML3H5PKOPrqa4zDfdcWH1JiLq0ZRqTOelWnv8vC8h2gbpy-KwXbGdK9MtoWzbkYWbxZJG4XbvWx6kwz7KZ0-hRR_hRLmWJ5kL1fgqFAn7u6h8vkOKsNQVpcmttgH-J-hkkbtPbzaR_mHCrHKyHNdILu4YHLFLbx8qvf_n6AVAp3KxjMC7YB54ymYXAtjiciJKA8S9bmIC779QgGgKlcQNF9OgKkZ0rERHsfluH_H0GawVIXeb_2m4x5pdq6l8jVmnGh56LSnZ1PHZJSLzawaFUIz31o7IZKdE9VbFER5QcxX_rqgKLILZ4z-NIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8117fb79ce.mp4?token=WfOrED-710fyaDmfHFgxULyGuEEML3H5PKOPrqa4zDfdcWH1JiLq0ZRqTOelWnv8vC8h2gbpy-KwXbGdK9MtoWzbkYWbxZJG4XbvWx6kwz7KZ0-hRR_hRLmWJ5kL1fgqFAn7u6h8vkOKsNQVpcmttgH-J-hkkbtPbzaR_mHCrHKyHNdILu4YHLFLbx8qvf_n6AVAp3KxjMC7YB54ymYXAtjiciJKA8S9bmIC779QgGgKlcQNF9OgKkZ0rERHsfluH_H0GawVIXeb_2m4x5pdq6l8jVmnGh56LSnZ1PHZJSLzawaFUIz31o7IZKdE9VbFER5QcxX_rqgKLILZ4z-NIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهروندان ونزوئلایی در حال جستجو در میان آوار خانه‌هایشان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/663972" target="_blank">📅 19:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663970">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckvxGU0ZOUEMXoU4tSvfLXB7I1x_qX4sJ-WuRjqcVQwQtt3tad3f4D9pzeUR-jOqAZok2ACvDULHcRWrtvT2xR5nQKN_1kcScEgY9oeGJRyDmvA1L2XMxKubGMuP0yjzoh2nXWpdwo_WxL2ETIVHJUXRCnxDBqGYzN6E0hyYJF8NRQ9yFjV99pSsy40Ga7OI-Xsa0t9OGRALDfATbRPPIK_fMiPWGdzR091uIN1pvI3grEaWAFMILUKN00af62mYQrbK-s2Dkw2pupkHBZglkT0wOdoaVVBRu-A28cmnAwklgUdxchWDC9IYjuHBMk87W-O-WxIPn3Gcu8XeNIxO1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/663970" target="_blank">📅 19:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663965">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uynzi_7SIcCFUOi_GDkIOobF7LAW2aiUR6A-VGwDyAqj3XnYLkrW2q76qYYb13Y_ZN6qjbH-x54EbkdZvXvmMssJSsiJkIMsepE8-yOU-R5TiYDwY8eXyYaDgqwP1YqSm6qHM2t7KBOEVbB4sgT6su6McAo5gFYNMaKPD7tct4W88nay_8Nu666Zx3nFdhh6jpTYd4BN3D4TvEoTEW8K8NjSE-fvdWaG_WPSNfswRUkCr3Ego-zsFgFc8eukmTkRVdc5A9TWOdE0k__v339iDAhIveC_Bv2KmEne21To6lCCFvxYvcOsv9Z46UeB9GSqP5O_aVNsAVdZ_Z1BXegZzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cd-ldb3fcvdONnew3AHD6q5XSxas8pji5P2xNoFFs2Qb6veF_PmCXcoQvz-sNt-MPtmTgTRAjpfrsCyYZAu1ro4O8eKg-61NQkYLXcUEh6ZraucWJY8v4US_EFiDF6hZi6PQZcCizuKZy6QqwwF-W6jM_LkwBo1uFQZNxs50TYAsi9_EA5lCtusf-dnI8ZCo0NQv8-1usW4RgBrQp3vdxl3ZU534NTHC7xJ8OxSz6uLEX9StIQQUwo5I3pMCNWo5GqyDK-ncyNGSO8EkrywOkkZhmJmzhDasl8j3p_ztaUM9iar_tZz1c-2Ch62tKL70p63PlK3uj_PTIX5hFZJ9kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vCDgHiIboUzREqkTc4t6GsEPt5rkJl9ieDlpPF_VfNH-w7LILMYrSDbl_lHrtcnlb7DuodQ6pUh-usrxnx3AQG7oOVNcrPK14fz2MOChGUqA1GFQPEaDXZPGvm25fnbOt340tb-T4BNx0EgYPUP9hBhM4NRq414Ro1TrqnJxdyMrTXRTGc6ZcI75HqTBdm6rbKo3-tTb7uZLR_vcsnxt3gXcG24jRP3JjHXyiSnQqlqa8f2g5NmfpPUI1fITItXSLVCD2h3j5n8d9HEZWPOg2SQLjRdoMir_dzUD75uOVYrEQ-CIm-kwHSqg_Laby50RlX9tWk0eXnlL_zOHxsyqrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aBW283dfhY9eOJ1yU6ohqxumCPmV--tNcdWuPraPTdwlHJTOkdv6TSelcSkwlmpe-7uiQ6GeG1woRyZrxNXo78BuPTaqgWmI924BeFbJEeJdu1NLcpK0NfJtVXIkOhPrz_ONp42NVyODdCy0G8Qg6hRlq69Zo88AddY5pr5UR-232DZAIeNFGWSqk-jY92wcasoBAu-YZKNi8xZEp7cKuODww02-We8aKiz4rrfTv2HfU8eIOUJnjQsuYVOfrEVovlS9Yd8x-hchjwwqKe5-VaVvvWutdn5x5hXV4V0wA3mkDDB1m6rFcGhNeZbiAIqCZBcr7PpMocU8Pm-e17Utcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hATrglia8YNnQndlkWmgdNKwAzxggpTI0QKuutsag1HNZuH74sF024D74aw-f8vsxWxQ7Z-GRkEZLyi6taAfw51wcgYwsw987JbEba1HKNNXeIfq_OzBNCGCsB2YcMmvfQFPyn_6hMsJVGaQG18DE5WO4Y00S9H7Qy0qspbBlbGtcVJE9nlFYUMYtRMk3j2CfHIX3wP7TNUMU282tCwBpIKiTtteO3SCXOXXADoqL66YvI3lI5aKGOa49WFCyubIaVMipQx5Va8b_Ce-nRgPVzQN3JslX6qp6rXu4GSeWBx06Bmia6WVvyxUTVI2F2S09MjivOPUS4MyDwAxaPjAvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دسر مورد علاقه‌ات رو به انگلیسی بلدی؟
🍰
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/663965" target="_blank">📅 18:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663964">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
تماس فوری اسلام‌آباد با تهران
ایندیاتودی:
🔹
وزیر خارجه پاکستان، پس از حملات جدید آمریکا و ایران که تنش‌ها را در منطقه خلیج‌فارس افزایش داد، تلفنی با عباس عراقچی صحبت کرد. این تماس پس از آن صورت گرفت که تلاش اخیر برای برقراری صلح در غرب آسیا با شکست مواجه شد.
🔹
اسلام‌آباد اعلام کرد که در جریان این تماس تلفنی، اسحاق‌دار بر تعهد اسلام‌آباد برای ایفای «نقش سازنده» خود در دستیابی به صلح و ثبات پایدار در منطقه تأکید کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/663964" target="_blank">📅 18:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663963">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e3f53f3c9.mp4?token=omNKSGGnHFnRktVi7RFPGG6nR4Y6OO-0S3ueV3PDudgu-2Z47AGOsYyZu7yvaU1OcSQiqL48X1gbRzPSvdoZeEMC6jHQnH49Mov3f2wmvUquGFwT_AgbF-Wt2ny1vOVlAKIBc7nVlxbvIhdt6po-uKXU2Do1yvC2eQOIFWildYyATAVSLXjodpdL_HT2i_22RLQLyL1cROsVsAIIJkwHu-8BJuN4mIYMtOSCl9jP6rYuGQZE-mN20eEPc_TmfzCuWQB8JREj2Yg-Xu8_aTN75B-YeVSYj6YyJW0Vdv0BeXLiFiy8V1SBHHbJtPfZFAZUevLhBvCM8oAKUIGY7XGP21tdhVePYfG258FN95QWmlL3zG_GcftNP5VZHe8Z9tmG1n6bCFUfyRnofo9mXb7iPxjL480KQo6FHiJIfQoblZtRIT7FR5Q3ORdIuKCYj7dw0gaLP-xtI52X-Hw-KOjFepq10dicj1N8l0s-ENbZIzijIFFf2d0XOnQgzwky_-RyeYTt4yriyjPLPARdwcUJq4xgx_TNS2cos4wKHpIHpy6fZw9ULDJL9EDL2wqQolc1GXKXxCyU-ZiThvjR_dI3zOrlcZHmpYwPXvScIls8hGRcKUdWUQLycS00sR_ZA42UoD0icc17OH9_a-0QFq90O_BQ5zbLzn4OsQUC4gI_oeo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e3f53f3c9.mp4?token=omNKSGGnHFnRktVi7RFPGG6nR4Y6OO-0S3ueV3PDudgu-2Z47AGOsYyZu7yvaU1OcSQiqL48X1gbRzPSvdoZeEMC6jHQnH49Mov3f2wmvUquGFwT_AgbF-Wt2ny1vOVlAKIBc7nVlxbvIhdt6po-uKXU2Do1yvC2eQOIFWildYyATAVSLXjodpdL_HT2i_22RLQLyL1cROsVsAIIJkwHu-8BJuN4mIYMtOSCl9jP6rYuGQZE-mN20eEPc_TmfzCuWQB8JREj2Yg-Xu8_aTN75B-YeVSYj6YyJW0Vdv0BeXLiFiy8V1SBHHbJtPfZFAZUevLhBvCM8oAKUIGY7XGP21tdhVePYfG258FN95QWmlL3zG_GcftNP5VZHe8Z9tmG1n6bCFUfyRnofo9mXb7iPxjL480KQo6FHiJIfQoblZtRIT7FR5Q3ORdIuKCYj7dw0gaLP-xtI52X-Hw-KOjFepq10dicj1N8l0s-ENbZIzijIFFf2d0XOnQgzwky_-RyeYTt4yriyjPLPARdwcUJq4xgx_TNS2cos4wKHpIHpy6fZw9ULDJL9EDL2wqQolc1GXKXxCyU-ZiThvjR_dI3zOrlcZHmpYwPXvScIls8hGRcKUdWUQLycS00sR_ZA42UoD0icc17OH9_a-0QFq90O_BQ5zbLzn4OsQUC4gI_oeo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پنالتی لحظه آخری ایران مقابل مصر دزدیده شد
حیدر سلیمانی، کارشناس داوری:
🔹
گل دوم ایران هرچند آفساید بود، اما در آغاز همان حمله، برخورد دروازه‌بان مصر با سر سعید عزت‌اللهی در محوطه جریمه باید به سود ایران پنالتی اعلام می‌شد.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/663963" target="_blank">📅 18:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663961">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a6be612c.mp4?token=e14bbxcAyI-71TXEns5EGQHzed0plV4JLr9iWwSnshjigDeFh70v9fwWlyMg9WMXPAQIajLSNIn9CxSbwQrUukG4c_uOmsDGIVyG8BDmD7FKYAMoqzObKJOux4bMRlI2gPpUg7lGFUt4lcCZ_UA1XerlXM9aORi6KNoov23IJeDq2DctJlBNMRMiev5VCtaGNtjgIsAhiFBKQGClry4h3mCGyC3bXe_Fz6S7i5sRL_FHzdcTyvZD7-KFz00PUPg8dmPQD3oOh223jGiVIPtqlTu46sqESFbYaxrxKBEosVvGX5vU8GpKz-phTp7Kmq7I-CxzCWD4WRC1Yig05nnbXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a6be612c.mp4?token=e14bbxcAyI-71TXEns5EGQHzed0plV4JLr9iWwSnshjigDeFh70v9fwWlyMg9WMXPAQIajLSNIn9CxSbwQrUukG4c_uOmsDGIVyG8BDmD7FKYAMoqzObKJOux4bMRlI2gPpUg7lGFUt4lcCZ_UA1XerlXM9aORi6KNoov23IJeDq2DctJlBNMRMiev5VCtaGNtjgIsAhiFBKQGClry4h3mCGyC3bXe_Fz6S7i5sRL_FHzdcTyvZD7-KFz00PUPg8dmPQD3oOh223jGiVIPtqlTu46sqESFbYaxrxKBEosVvGX5vU8GpKz-phTp7Kmq7I-CxzCWD4WRC1Yig05nnbXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عصبانیت بلاگر ترکیه‌ای از تصمیم داور بازی
ایران و مصر
بلاگر ترکیه‌ای در واکنش به تصمیم داور:
🔹
قسم می‌خورم آن صحنه آفساید نبود. من ایرانی نیستم، اما معتقدم سیاست نباید وارد ورزش شود. ایران شایسته نتیجه بهتری بود، باید فیفا رو تحریم کنیم چقدر شما بی آبرو هستید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/663961" target="_blank">📅 18:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663959">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzda1XxrC7XIHrYljLGesRdUDJ8E6h_9Dlg25jCRnyvcvMWW9P_SvBX3KwgCgXn_Wnh7Dfuo9QKQqOODdKsF4XjlzgwXIpI_SjAZGJIX80maWVuahLIyeKOPejdq39f9Is4Soip_pJYc_Gvu-pOBp-ULee57si6JulAoEPqvssL3uXc2MWoYpQBJStx5NX-XR8vzOJWwh531ivZHjrULfedQE5J0-wfLloWEkRyrGl2a1FWPyu04D5FqhuJep5Lb8Ak_h5zmqpb2hj7irQxW8L88j_rVrKv4JFPSQt9UK0bB118wzdRRbAYRZ55y5VB2mMikFO4qTQD7v_nsEV666w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسکوچیچ سرمربی پرسپولیس شد
/ایسنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/663959" target="_blank">📅 18:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663958">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ثبت‌نام زائران و میزبانان مراسم تشییع رهبر شهید در پیام رسان‌های داخلی  دبیر ستاد اسکان شهرداری تهران:
🔹
ثبت‌نام زائران و میزبانان مراسم تشییع رهبر شهید از طریق بات «باید برخاست» در پیام‌رسان‌های «بله»، «ایتا» و «سروش پلاس» آغاز شد.
🔹
زائران می‌توانند برای…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/663958" target="_blank">📅 18:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663956">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe8d3874a.mp4?token=jjpdxPaCKaFGnPWpTmRZ4IynaexVblKSNqiGnZ-9fByvc-bfGspwq0lD-XOWs0zv-_W1yWAcqdwGsNzL6165lCyc5qkWyNUFN0DXggQUalGDMU_fgwBZOi_DAZ7KvyZ7iJ1wXThPmjH9MiTs8WkHCSLkpCnEHiqfNgfL13zpl1XDDx0IRq50DzeoUclW957GnjDFBEmurN5PBfxK854KkyUp0UnGkKRXRFvJIOC2WbyTddqy65C1Aro7gnQGEqi4lXD8d2KCqmSho-dZWRdiRIXZzvl3xVUR3--jBuZDCfZxiC7i5lTxI75e1UWzQYFEDJqDIrYYqlt5byHYZbyvsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe8d3874a.mp4?token=jjpdxPaCKaFGnPWpTmRZ4IynaexVblKSNqiGnZ-9fByvc-bfGspwq0lD-XOWs0zv-_W1yWAcqdwGsNzL6165lCyc5qkWyNUFN0DXggQUalGDMU_fgwBZOi_DAZ7KvyZ7iJ1wXThPmjH9MiTs8WkHCSLkpCnEHiqfNgfL13zpl1XDDx0IRq50DzeoUclW957GnjDFBEmurN5PBfxK854KkyUp0UnGkKRXRFvJIOC2WbyTddqy65C1Aro7gnQGEqi4lXD8d2KCqmSho-dZWRdiRIXZzvl3xVUR3--jBuZDCfZxiC7i5lTxI75e1UWzQYFEDJqDIrYYqlt5byHYZbyvsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون دود غلیظ ناشی از آتش‌سوزی لندینگ‌کرافت حامل خودرو از مقابل پارک آفتاب ۲ قشم به‌وضوح قابل مشاهده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/663956" target="_blank">📅 18:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663955">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
خانه‌های دلاری در مشهد!
رستمی، رئیس اتحادیه مشاورین املاک:
🔹
وجود معاملات خرید و فروش املاک با ارزهایی مانند طلا، دلار، یورو و ارزهای دیجیتال در برخی نقاط مشهد قابل انکار نیست.
🔹
افرادی که چنین شیوه‌ای از معامله را پیشنهاد می‌کنند، معمولاً خود در حوزه طلا، دلار و یا دیگر موارد فعالیت دارند؛ با تکنیک‌های این بازار آشنا هستند و می‌خواهند مسیرشان با موانع کمتری مواجه شود.
🔹
با توجه به نوسانات لحظه‌ای قیمت ارز و طلا، توصیه می‌شود از انجام چنین معاملاتی خودداری شود؛ زیرا در نهایت ممکن است متحمل ضرر شوند.
🔹
هرگونه معامله ملکی با ارزهایی غیر از ریال با مشکلات قانونی همراه است و در صورت مشاهده، برخورد جدی با آن انجام خواهد شد./ اخبارمشهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/663955" target="_blank">📅 18:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663954">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qo4xq9ihJWJuRx_ZDjukajc32BViMhGkG-nH1Xb776xmdyOwwHLVByMnTYoo7Q1jwnciGRKolIsxVoMmAXpYjsMBcu7Ht04ErKEekQtdIpkY0ryU82JhxZhY7lxgdpLFUqK1klG1uLqw3sTM9Z6Sddm0z0Q_RUb21amUZbOuQvDu6NUx9_fAkPK6YLKY_uVzVB-kMe5Imm5aX5PfQ7Lrgne2IY7Q1MrhptGVwWLQbNTpAHPOj3gcEb4PV9XGamPjr93MRFq7DeAQwlM6vm5pJnd0tsEODwkNQVYG2SRFBArUnQZxsKfo5EEHv5te1hU_L_5AxDN5538YZqlO0FnsyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فریب دود ملایم سیگار الکترونیکی را نخورید
متخصص طب ایرانی:
🔹
تصور بی‌ضرر بودن سیگار الکترونیکی به‌دلیل نداشتن احتراق، یک باور اشتباه است و این محصول می‌تواند آسیب‌های جدی به ریه وارد کند.
🔹
ویپ حاوی ترکیبات خطرناکی مانند فرمالدهید، آکرولئین، فلزات سنگین و مواد شیمیایی طعم‌دهنده است که باعث التهاب و تخریب بافت ریه می‌شوند و حتی وابستگی بیشتری ایجاد می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/663954" target="_blank">📅 18:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663952">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5WxpicLtESzGWpa5Cryv8aRW8lZAGtabD0tEA_SRxVwp16w_hLNPNbXqtpO8xU8UOdN5euJVL7wFJWN57oMQ2HvEOmtgzl7L1hTTatlt1s9_vdC4s2DAAt6T1D9XlsXCDr9uVcbcNXuqtHQFlmvhJH3yJvLBJFMxg-mBrxSosPKIKUgOBkGw5fp-eafzbeDFaXGMIN9wxPsz554_LTvZdX6dZrkUieq8chg5o1uQXiftOV0x_m-vnG9pzbnv0ipljURDL0My_8LIq9zi9V-zpIgZ-oMulLDQlaCAkCQDeQhzTLaulNVquZWzapcbW1yP5BboSoec90awVy_4TJdyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نامش ام‌وهب بود؛ بانویی که در کربلا، کنار پیکر همسرش، عاشقانه به شهادت رسید!
🔹
شاید اکثر ما داستان عاشقانه شهادت تنها بانوی شهید عاشورا را ندانیم. زنی که پس از شهادت همسرش بر بالین او آمد، خون از چهره‌اش پاک کرد و او را به بهشت بشارت داد. شمر که این صحنه…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/663952" target="_blank">📅 18:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663946">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pyyGgu3pxlV_nnTcfBCtzRkRlgV8g341iJZpi0tK7fkL2zonw-34S1SJx6am7B_dluTdZZmQugtqQrSRqRqJQ6Sqs0WtgdqRN-Leew3Ib9bDV1j5rgOthiiAj_gBn-lgyuEMbdp23ladoaubWMhg6Moknd51wvBSrYOs7IZFp8-PCFspzqtKqI5I5yav5lKeo-OdPxcL_xfKpkAqSedxLPRQeF7RJgp64MwOBGbAToPMYu3JdvBtFbK7Hp9Hy0kIGuEdXcbt6e7GYUM__lorhi7LpkSLcZJ9plPNlSiJDo6vA6hghyMSqMx-AQH05fJhH49I51__5rOiboouunEdiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZahvFVwQg8X68xXm1RjdQiOiA3xVoNKqtbmE8EOjbCt-QjZjA2xb9OEdh6rkRWptH9VMApCFtpB27yjtLfBXIWsc4xDwZ8LSSqEo35vy7mMHAsUCMOii9M2bI80n15hjyC4GlHuneJ07RmKRQrIdz6UzWmaEK26KimfSDJa90w_sBnJA9yvl9qOcYhEnSjUaNIOA8kSAGqTAlhubBvaJtyex-3giRvwFWI3KHrfQGDAW9ZYZdJ98MtAjJfWvTrwBQdJ6tPcAODjHVhWFQqnP2P_JzkgD57SVyKN_dEghYebwRZMui-iaz1wPsP3Y6CXhJncfgGuQE3-XCbCjx0Vfhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mu6roRT3am1DzJBgshyLHqEeAx45J-6oWDVcwJbjtYyABUs9Vnk2IuF4WLBHPXKmL6XrY3pECeHLV1HhZ3vdP0_zShVCM3Xagv61z9XWd8z-UG8rUFXntqRjjSmnPrs53LB_Lk2f_K6YtvKmiBhvXQEUQ4zODnBB5VKe6OuuEn3R976qMZDbWCOAvvnGVanwiyoUU5lBc4Ob8dLZkuRzIsoLFIqI0Be0LznX2lbeJiUo4PPAOsgq-xTs-MxRukSvmyEy696G2BmVKN5ENh3zuQ4wXZaN6G1qS7sVks6OOQj_xAPXgQ9Ol0eCPbalhXrVtfmLp5gbPeKF56qhqd5TKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DCgQlfS17mbxO6Mm9rFzA-c-A9P3F5-FuCWHWmOHrVgaqqqe2fv026IuClcr3YO5FvT8YsVBvUdyydcPkxXM7KNSYipw9gr1Mk0OPm-MZEdCSpsH7e7an9U5-XLzaKQMKe9E6Mr1NwNsw5yjv-Dp2n8U0BEBz8i01gmhudVy9UJkvI7wARNzq4jtwPhrTo94m6PJTaF8PoLg82eW_utEn5vzLPX4jJ2YOAfvImTQ5-Nn0h-u_UAg_4DZfHHnwMvdWwJGHVfEEK3YB7LVxjDKSNEQ-zqnHbu9XHrCOnTOdmqtjkXxXy9NG-ajsE4UiE_0JGEydY2JC1dmWu6yJGO9Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FrDtrFhe8T-GQ-rzvd87DRT21Zlt5HzTM-Q2aN1mrzKbk2BRs05TUawMFwTviIJTlv9ELCi8fo-QfEYQQN7svFMRJOhWJJ3z98OyboHfPpUGfOoleLRuWs6iLus4By-CEJxBjvKZNVwT6_KW4Znd1EplSmOcaWldPc-ZEKP5UHiZ7inCZIwalpv-frpu3J4q0Cp7gXDgTgARpsxt0nzjW6trhoaEOyP6PD1xpUFc2qaz_xTxIHU1lojxoJEuKt19KCAgE6KWNqrcXvc5iiS9zgQBWw8nMkjwi9bcdKSEEDWeJv3idJKKhEXuSM0xOoFyVCQUIoDUKssEUXGW163vEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nK0e_ZfqFTWY-fJfjXGT4xBQO8WBqUgFPvKpgOnHV2N7AmDhUw4NVjs_nPFYIkMfbJZrbtMkuIx5kLXv13wkdJ7cRNixTIwPNAZjvFQwre2Oyif_HRpKtRN4v8W5XXLJqfshNT7-A1EcwwcEx680xWYwiRy7yiSO2FazoPk9ElAy8QRKiJFD3JWC23kY6V695Kv12TLKPllDOZ-alW3iXaXQ8B1t0vRW9fmnP8R-BlnyyUWLPveEhw6sBPzQEPvuqi_ZD0NU3kuV7FNwp9c7QOYNirXdHymjws1OhLOogVAOWcKM_mIoAukjSEmARnlyCGpAhF8U-PuTxBs1noGsOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
۵ باور غلط درباره قهوه که هنوز خیلی‌ها باور دارند!
☕️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/663946" target="_blank">📅 17:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663945">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d38ff0718d.mp4?token=HF4WSUmNe37cAEuP1mGBIitJu8Ym2w3-Ub3VV92VZo8KRDoYff8SjNc7r28uTrMRTKRLROFMa9LZqxC3YbTAgNfYhscnO7som8yA-tGE5hW4i8-pn-ItqjP7SKTdRacql2zvQYMfwLczrqyvF99_AfU3uV6RoAYN2BGTuNAQSPJiTitFUxo9KnWF3ZYqXMZc80Rk-IDmt0NGVvhHZHumnsmcAQjuS8R3gmJve3oYYRQ99h1avCByY9mg1L4DYIkzhvb5QooHBnPrlWihncLQYp__-HvE7RcWLpk6X3mSk0YPzc2iUjCEoU98nEDlRltoFW-XjLd12nD0VRnlrMgjfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d38ff0718d.mp4?token=HF4WSUmNe37cAEuP1mGBIitJu8Ym2w3-Ub3VV92VZo8KRDoYff8SjNc7r28uTrMRTKRLROFMa9LZqxC3YbTAgNfYhscnO7som8yA-tGE5hW4i8-pn-ItqjP7SKTdRacql2zvQYMfwLczrqyvF99_AfU3uV6RoAYN2BGTuNAQSPJiTitFUxo9KnWF3ZYqXMZc80Rk-IDmt0NGVvhHZHumnsmcAQjuS8R3gmJve3oYYRQ99h1avCByY9mg1L4DYIkzhvb5QooHBnPrlWihncLQYp__-HvE7RcWLpk6X3mSk0YPzc2iUjCEoU98nEDlRltoFW-XjLd12nD0VRnlrMgjfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثبت تصویر سیاه‌گوش در جنگل‌های ارسباران
🔹
سیاه‌گوش، گربه‌سانی وحشی و کمیاب با گوش‌های نوک‌تیز و دسته‌موهای سیاه است که از گونه‌های ارزشمند حیات‌وحش ایران محسوب می‌شود.
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇🏻
@azarbaijan_sharghi</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/663945" target="_blank">📅 17:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663940">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C95R69uslpHW_uOmdoGBiyFYM41Yn1D1frJxKO9zYxLRS9wdG9y7EOMSZ-cm0HIfGUXJPH9Qm2ZB21u_pkvnOEuKWOtxYR0Fbez5fLWLR6eHSTDKjp-ULfsoZYa1_epVhmxJ03RF5FckcHReS8Yeqjo9JmFOa-oFSDTl_ZFQxye0hSZg8LWU_KKjeeqUEFtZ2zuqya3f3y9z2D1zqKwNSSqSF8jE-FzAlAvzBGl1aoiROChjvuoAjompvgdgKlVV3daymkknqCjA0TdeFu580mug1P3jptLHN8Tlcy1e0T695gFn2nNrSpiXmuyPYf_lBvsmhtwVmwXJ4Vhh9HBHxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غول هوش مصنوعی آنتروپیک در آستانۀ بازگشت
آکسیوس:
🔹
دولت ترامپ احتمالاً این هفته محدودیت مدل Fable 5 را برمی‌دارد؛ این مدل ۱۵ روز پیش به‌دلیل نگرانی‌های امنیتی متوقف شده بود.
اما چرا این مدل قدرتمند است؟
🔹
شرکت Stripe با آن یک پایگاه کد ۵۰ میلیون‌خطی را در یک روز بازنویسی کرد؛ کاری که برای مهندسان بیش از ۲ ماه زمان می‌برد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/663940" target="_blank">📅 17:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663939">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1622775009.mp4?token=VmOh6kk8WI5lhj2ABgdq1L_VTXtRPNWJXBPiO8jWujW-Sb-vXUaM7UCnT0JdF4tikEw0FLzsnyIwawZ9tx5AZTIZwBvKJN7_CA8bF6Oj6Ox7xJWCQ6fkxWGNgDxDgRqO8hQ7p9oEgvUoUSjMY_RnIJSXCFWSBUrOu7vZoGTAotpf7VFPgPXAIo7BjV6x6D_DJvY348sZyr4wBUJiQ0tZRrR5W8AujhPzc1Ai0bZOe1LeRv93iEFrn8he2Srh3BuK7soL__hmhlE772nGCa67h3eG9xSiS73bLXUtaCZj9bijIxPqlqSHDbzc7WgMRvWzT3uvXug55-j5UU4MnoNShQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1622775009.mp4?token=VmOh6kk8WI5lhj2ABgdq1L_VTXtRPNWJXBPiO8jWujW-Sb-vXUaM7UCnT0JdF4tikEw0FLzsnyIwawZ9tx5AZTIZwBvKJN7_CA8bF6Oj6Ox7xJWCQ6fkxWGNgDxDgRqO8hQ7p9oEgvUoUSjMY_RnIJSXCFWSBUrOu7vZoGTAotpf7VFPgPXAIo7BjV6x6D_DJvY348sZyr4wBUJiQ0tZRrR5W8AujhPzc1Ai0bZOe1LeRv93iEFrn8he2Srh3BuK7soL__hmhlE772nGCa67h3eG9xSiS73bLXUtaCZj9bijIxPqlqSHDbzc7WgMRvWzT3uvXug55-j5UU4MnoNShQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
برخورد هواپیما به آسمان‌خراش ۵۱۸ متری در پکن
🔹
یک هواپیما با آسمان‌خراشی به ارتفاع ۱۷۰۰ فوت در پکن برخورد کرد و سپس به زمین سقوط کرد که منجر به تخلیه ساختمان شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/663939" target="_blank">📅 17:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663938">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGTze18quMXScpIYSVX1IKIcTOmS2P01Y3cFSZsiyqtJ9ZlnRelRWjqLwWBJXLWJ2dVVRtXDVCy5y_IOKx354sqAxVCEkXm3KX5xIEe7HUCxQypaMY_MNAlwwGwMxsdpqYAXlRpMR418tdaYmKIujSFCxKfQovgPUh_oUhU55x8bisedeYzek5jJ5EFCmG7tqEQ7BOlITaGJjp-ffLHIIV9OV-Fi2JrXLtppF8jldi4Lrn-bD1lXpxdAoZBMDNjb1qRmegFcMFu89TTpVgi_2f784dVx03R5VYe9QwQjZ0IDUqgcyjuqTGtCFcOrQB1Pn_GgMM10SiVqhBVy1SFIkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
+۹۰
🔹
در سومین دیدار تیم ملی فوتبال ایران در رقابت‌های جام جهانی، شاگردان امیرقلعه‌نویی برابر مصر به میدان رفتند و در دیداری پرهیجان به تساوی یک بر یک رضایت دادند. ملی‌پوشان ایران که نمایش قابل قبولی ارائه کردند، در دقیقه ۹۳ موفق شدند برای دومین بار دروازه مصر را باز کنند، اما پس از بازبینی صحنه توسط کمک‌داور ویدئویی،این گل مردود اعلام شد تا فرصت کسب سه امتیاز از دست برود. با وجود این نتیجه، عملکرد شایسته تیم ملی امیدها را برای صعود زنده نگه داشته است. بر اساس پیش‌بینی‌ها و محاسبات جدول، ایران همچنان از شانس بالایی برای حضور در مرحله بعد برخوردار است و احتمال صعود این تیم به دور حذفی بیش از ۹۰ درصد برآورد می‌شود. این موضوع امیدواری هواداران را افزایش داده است.
🔹
هفتصدوهشتادوچهارمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/663938" target="_blank">📅 17:33 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
