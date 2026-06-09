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
<img src="https://cdn4.telesco.pe/file/suH594awH74CDTcN8S4_hhLc4FXGmy5GQy8ewUVdKGVIPonsPnKrG8NX3zWUgr6C6HNXLRl5WtuNTizdPZswfPtfleFO2GQR2JoQwkm3hvE4fnHm5mRx0xJhV3K_uiGGglK4yRl2H-ehh59xddC6eKSGCVMc1tvtTMuXTVk_IoxtP-XutbMTQk7oWk3ByvuBUU4AtAWrggDE_I7_uk99Totbd3zEBaWVRGx0wljG1Qm-AHk64jSDVKhIQjnvWq64kRCYNFjNeVeKH4h051ol531ffM2nMk3f282BCKNnykUE-bAx4QY4qMyq1XoVEo6-1LFTt1XcDr_mleA7zSypUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 13:59:26</div>
<hr>

<div class="tg-post" id="msg-133104">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
✅
پرسپولیس برای تورنمنت سه‌جانبه استارت زد
⏺
باشگاه پرسپولیس: نخستین تمرین تیم فوتبال پرسپولیس بعد از ۷ هفته تعطیلی برای حضور در تورنمنت سه جانبه اعلام شده از سوی مسئولان فدراسیون فوتبال، عصر امروز از ساعت ۱۸ در زمین شماره ۳ ورزشگاه آزادی برگزار شد. در تمرین…</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/SorkhTimes/133104" target="_blank">📅 12:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133103">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
🇮🇷
آمریکا بلیت هواداران ایران را مصادره کرد
⚪️
فدراسیون فوتبال خبر داده آمریکا، میزبان بازی‌های ایران در اقدامی غیرمنتظره، سهمیه بلیت اختصاص‌یافته به فدراسیون فوتبال ایران را از آن‌ها سلب کرده و در شرایط فعلی امکان ارائه حتی یک بلیت از طریق فدراسیون به هواداران…</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/SorkhTimes/133103" target="_blank">📅 12:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133102">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‼️
هو شدن ترامپ در فینال بسکتبال NBA
🚫
وقتی دوربین‌ها هنگام پخش سرود ملی آمریکا در فینال NBA، ترامپ را نشان دادند، او با صدای بلند توسط مخاطبان هو شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/SorkhTimes/133102" target="_blank">📅 12:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133101">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🚀
آف ویژه سرویس نامحدود
🚀
1‌کاربره فقط و فقط 600T
2 کاربره فقط و فقط 700T
3 کاربره فقط و فقط 800T
ثبت سفارش و پشتیبانی:
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 565 · <a href="https://t.me/SorkhTimes/133101" target="_blank">📅 12:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133099">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
بیانیه رسمی فیفا: دیدار ایران و مصر قطعا دیدار افتخار همجنسگرایان خواهد بود و به هیچ عنوان این رویداد لغو نخواهد شد.  در این دیدار ارزشهای همجنسگرایی را به جهان نشان خواهیم داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/SorkhTimes/133099" target="_blank">📅 11:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133098">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
ویلای علی کریمی توسط قوه قضاییه مصادره شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SorkhTimes/133098" target="_blank">📅 11:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133097">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYeg9R-pMDJTWObwXxmWJVaKTC6KFU_dhKGWkKPqRn2VluutdvJgCMrXZb8Yk9O-7-ITioXl8Is0S0dJFkiNXYdh9KSbM7dxHNMXH8QyKnhXRhEwP3otCEa_jNlnwmpqjH-JAIO31adpBvS3T5gjb6YF9di1dy6XobLr6s8ZFSDMJgWeE4EbaD4H5DT5B0iwwD2eort7fuWwKaEFgX9NovedNrqtbgUsLaCOVi3-2NgLBXA-XNtuuqq7I3BMPsa64EqSM2DpI082Z3Svfx-2oUMs-AuL1WNzUlUB7D3bBbZdWZFhHxLN_UGPY560aDluS75mkUPUMsYfM_QHHp2Ilg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ویلای علی کریمی توسط قوه قضاییه مصادره شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SorkhTimes/133097" target="_blank">📅 11:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133096">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0309c6ebab.mp4?token=LUachFEE2M1RWb1ebRENuPrC6E8KOfnD9UGDRjhYJSKcE_mNLOwhD-V_wPzW2QDUOLG7zrA4Sk_Z7ex2sADptv1D600BwS7cSuhAJt6kbwJ1GiEjVtpd-Jg4QOtH4x2WsXgHEcvjWFBzuQU-sgmKRR_IZ2cIiehwoVbmu7UTfqvfKUgOOzNeayc8aX9C-OOw6JjCm-RnRUEqwt_NbQlh29xm73UeDDV6cP4AhC6c2LRGbzuMWEa0n8X1lLRSuy5q1oh0S2XHhGIDoTYGNMUBPjpvaolmqV8VUfDNwSxi1u6ZNzTF29idwdF9Y4e7z5MWeo-0YUii8KhMnTA99qJj4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0309c6ebab.mp4?token=LUachFEE2M1RWb1ebRENuPrC6E8KOfnD9UGDRjhYJSKcE_mNLOwhD-V_wPzW2QDUOLG7zrA4Sk_Z7ex2sADptv1D600BwS7cSuhAJt6kbwJ1GiEjVtpd-Jg4QOtH4x2WsXgHEcvjWFBzuQU-sgmKRR_IZ2cIiehwoVbmu7UTfqvfKUgOOzNeayc8aX9C-OOw6JjCm-RnRUEqwt_NbQlh29xm73UeDDV6cP4AhC6c2LRGbzuMWEa0n8X1lLRSuy5q1oh0S2XHhGIDoTYGNMUBPjpvaolmqV8VUfDNwSxi1u6ZNzTF29idwdF9Y4e7z5MWeo-0YUii8KhMnTA99qJj4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هو شدن ترامپ در فینال بسکتبال NBA
🚫
وقتی دوربین‌ها هنگام پخش سرود ملی آمریکا در فینال NBA، ترامپ را نشان دادند، او با صدای بلند توسط مخاطبان هو شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SorkhTimes/133096" target="_blank">📅 11:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133095">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CR_3-zmvcZ6IEmTH5BX3l6BsPRVcElhZzqbhy3GDv-InkXZHUJ0WlldQ88lgJjN44HyeoRqvqIjreVUipqmD3vVl3gwVZm48zkdhhVLwjViK_YmeVbc5c0Qum914dDmXXdd_m__DkJB50XUixfweS2mKtTTVeqmh6tQdgstTD-2ktpqsJBCVmW_LIclU3HtF1_AAmbUcCIdmN7_UptPLErgNS5mmcYNb_8ZSdjmEad_mLmegc9MChavzSqARUJpz4WDiz2QUVaFOtTqkwyxDURTnQ6rz04iL6tMMiWUbJtzL0k7p7b_8BImOg5NdY8rkor69PFkt5krZtPAd0_xe8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
فیفا در آستانه جام جهانی 2026 از طرحی جدید با عنوان «سوپر شات‌اوت» رونمایی کرده که به تماشاگران این فرصت را می‌دهد در ازای پرداخت 79$ ، نام خود و کشورشان را در جریان مسابقات روی نمایشگر ورزشگاه‌ها ببینند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SorkhTimes/133095" target="_blank">📅 09:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133094">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
🚨
🇺🇸
ترامپ : فکر نمی‌کنم که به این زودی‌ها اسرائیل با ایران وارد جنگ شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SorkhTimes/133094" target="_blank">📅 09:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133093">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D17wfQBKyfG16MyMrsC-5a132YNSA5NW9usnxly6Iwj6pjYFfaUOCFCGxhcxUdG7j_7PGr0l2Ww2NGNWRL6OtUOUlP9QckPesma4Z_GyG2nxuGxQm9oxoKuQu-O6bUSS_FuoJbPckEVxJCFntxACvefiOYtNFu4-Nh-NcNeObkADeID96a6w3YY9P-53emoERmM9_9NU2sJtIkEOEPXFvkl0iqIe_My1W4oUnqmTxqHMSf9R7zwWk8fcWEsZsWuxe-9cnvxh3IB-av6ffsveSlDXEyhnjRVwdqQPgxp_nrDwsMaKNilrNyjC9MZKz3rMbQ9UcbYsUj-4DwFuCph1Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مهدی تارتار: پیشنهاد پرسپولیس؟ اول اینکه هر کسی من را از نزدیک می‌شناسد، می‌داند وقتی با تیمی قرارداد دارم با هیچکس مذاکره نمیکنم
◻️
من به آقای اوسمار که سرمربی با شخصیت و کاربلدی هم هستند، از همین‌جا می‌گویم که به ایران بیاید. ایران امن است و هیچ مشکلی برای کار وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SorkhTimes/133093" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133091">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bho-aJJINyKqtGzOjnyjdd1QJnmxfDpeaQ7eaRgQxs_2TMz2CcgNdEMSTqT9CS31K-d4M4YNLibJP8SMaWiWSbUq6IhxkZsiJDC3rDR9C9G64xPEjVxqhd_OZlRoeChKMkE5XAI7CR2pij3Z9G6JdsES9e4mQtsOiVmVPucXCTUB0x68Hnw7Geaqey9Is_0R1NMhsKDwECEseJ1f62R3M3bEKRVkjS-Za_uz2I2MxVauKyifa5LGDwRP9PDQe0QYQLkrNUK56znqBXljACEoKIqPkfb0Xvufd-EyiBOQ6BzumHQGFKajYiHreAJEKFPsqHTNloMy7wZDU5qPiLx0CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🤐
دیدار سوم از فینال ان‌بی‌ای رو بین دوتیم سن‌آنتونیو اسپرز
📀
و نیویورک نیکس
⚔
رو در سایت اسپورت نود با آپشن‌های متنوع پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/133091" target="_blank">📅 01:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133090">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
‼️
ترامپ: به نتانیاهو گفتم درست رفتار نکنی در برابر ایران تنهات میزارم!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/133090" target="_blank">📅 01:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133088">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❤️
❤️
گل اول ازبکستان به هلند توسط ایگور سرگیف مهاجم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/133088" target="_blank">📅 00:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133087">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f57eeddf50.mp4?token=XYqMWZuw-tRDBQMwOLmsu0Q4tNWY9qt33omd1ZiITVm6PRnMSHSmjboyNfcISx6ZMdkvrp3OB2kGFpHOcdybZ77MWkPUApzHgD7AMCM4_BRQ4BLEO97YDMGtH4Pf96Tfldy0p6DOt2T67OsVfUJnQvtnMkiqmMzVxT4ibXJxiLfEkYlcod5oRHQr19OeoJ8l7S1Ma4WUnskZbEWsM-vsICWNsZmalAnarK42SgHoeebYT0bjZN8Z5ZIQtfcm3Kn_54BmtJL3Wj_8uvIBU3VtAknBUIPH-WNejmaurgDMtkDmzSPD5_PNxM0S4qfTqBsi6eYXkHieS4o1mM4H_ZpxOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f57eeddf50.mp4?token=XYqMWZuw-tRDBQMwOLmsu0Q4tNWY9qt33omd1ZiITVm6PRnMSHSmjboyNfcISx6ZMdkvrp3OB2kGFpHOcdybZ77MWkPUApzHgD7AMCM4_BRQ4BLEO97YDMGtH4Pf96Tfldy0p6DOt2T67OsVfUJnQvtnMkiqmMzVxT4ibXJxiLfEkYlcod5oRHQr19OeoJ8l7S1Ma4WUnskZbEWsM-vsICWNsZmalAnarK42SgHoeebYT0bjZN8Z5ZIQtfcm3Kn_54BmtJL3Wj_8uvIBU3VtAknBUIPH-WNejmaurgDMtkDmzSPD5_PNxM0S4qfTqBsi6eYXkHieS4o1mM4H_ZpxOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
❤️
گل اول ازبکستان به هلند توسط ایگور سرگیف مهاجم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/133087" target="_blank">📅 00:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133086">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
اوستون اورونوف یکی از ضعیف ترین بازیکن تیمش در دیدار دوستانه مقابل هلند بود و دقیقه ۵۴ تعویض شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/133086" target="_blank">📅 00:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133085">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❗️
🔴
غایبان پرسپولیس در تورنمنت کسب سهمیه آسیا، پیام نیازمند، حسین کنعانی، میلاد محمدی، امیرحسین محمودی، علی علیپور، سرگیف و اورونوف هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/133085" target="_blank">📅 00:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133084">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPNFyG_2oGeIm_d_2ispTXbYkwDlqeic5Abxa5AGIyAhE5fGcg_fjQTM3iE8B3Ti3cXPz4JlvYk4VXmp4JBo2zced01qUJmkEfJ4p_oa0mHx0lWwifDhqHVWR3fsj-P4r67dGSJ8Tav0WQ97Th6m66RQcpNvce65bc-PG3WK7Hq4_yVMkFTq61SqmArjOL3fpmoWhAmco0itHe6gMDRSj3qgajCKdbcoOIm6N-v1QFjnkjJoYtpZaLBPVeVZ8doKWlNdmENXoXY3WKDCf08jwxWOSIWzgFoBpy7f9sTvaH_jeNhXjXT2MRs9f6xH9bpfniDxAuUJepf4oDSxeTOWSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اورونوف در ترکیب اصلی ازبکستان مقابل هلند   دیدار دوستانه
🕙
ساعت ۲۲:۱۵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/133084" target="_blank">📅 00:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133083">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
🇷🇺
شنیده می‌شود که باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده، هر باشگاهی که این بازیکن رو می‌خواهد باید مبلغ یک میلیون دلار به عنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/133083" target="_blank">📅 23:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133081">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
در سکوت و سکرت....  فعلا،مذاکرات داره خوب پیش میره///قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/133081" target="_blank">📅 23:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133080">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
اوسمار کراش زده رو آریا و لیموچی و حزباوی و باشگاه در تلاشه برای جذب شون راهی پیدا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/133080" target="_blank">📅 23:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133077">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❗️
حمید درخشان:
🌟
من خودم خداداد عزیزی را سال ۷۵ به عنوان یار کمکی به پرسپولیس آوردم اما الان نباید او را بیاورند چون بی انصافی است. پرسپولیس این همه پیشکسوت دارد، از آن‌ها انتخاب کنید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/133077" target="_blank">📅 23:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133076">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❗️
🔴
حمید درخشان:
◻️
کار فدراسیون فوتبال و سازمان لیگ درست نیست. اگر قرار بود که این اتفاق بیفتد باید بین ۶ تیم بالای جدول یک تورنمنت می‌گذاشتند و آنها با هم بازی می‌کردند و قهرمان این تورنمنت می‌توانست به آسیا معرفی شود. متاسفانه این تصمیم شخصی فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/133076" target="_blank">📅 23:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133075">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
دانیال اسماعیلی فر ۱ ساله با تراکتور تمدید کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/133075" target="_blank">📅 23:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133074">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فرهیختگان: دانیال تمدید میکنه با تراکتور و برگشتش کنسله
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/133074" target="_blank">📅 23:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133073">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
استاد بزرگ تاکتیک‌های ناشناخته امیر اردشیر قلعه نوعی تو بازی دوستانه دیروز نیمه‌دوم محمودی و حبیب‌نژاد خط خورده رو بازی داد ولی دنیس اکرت که تو لیست نهایی بود هنوز یه بازی به میدان نرفته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/133073" target="_blank">📅 22:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133072">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYqdLG3Q1HrYP7Hh6pZdfnIbyTXd6J3m6_bPAYtv61UsV14s3R9shA19UtxcITwHRa5Dw4GMWadq_LyD-SySSBfj3sR4SzGmywcA5oMvxRnHwVDkExzhtCHxl1cewxVmbo6OTnUqyd4OuqJIGaZQr0UX08sdOlUGWOG3nGfobx2UgNY7MPsnsJ5fGbEJbbXv5a7WnQtWPo3lNT0prOFqkLKOOrSDi4UzFstawm6VLVm6CMGXzXoM-iXI6JARhIkpQoIYe_RXPhyOJOMc6YLS2dE75eMRRFyQ8F7D1mA5zMOz-FVsyxpVawGFjKwOzQH4LLcyU2gcb1DH5pwzczLarg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
PulseGate | اتصال بدون مرز
🔥
اینترنت مخصوص نت ملی
⚡
سرعت بالا
🎮
پینگ پایین
🛡
امنیت بالا
📱
سازگار با همه دستگاه‌ها
♾
کاربر نامحدود
💰
پلن‌های اقتصادی از 250 هزار تومان
📩
ثبت سفارش و پشتیبانی:
@Winstn_Churchill
@PulseGatee
⏳
ظرفیت برخی سرورها محدود است؛ برای فعال‌سازی سریع‌تر پیام بده</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/133072" target="_blank">📅 21:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133071">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
اوستون اورونوف و ایگور سرگیف در لیست نهایی ازبکستان برای جام‌جهانی قرار گرفتند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/133071" target="_blank">📅 21:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133070">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
ترامپ : اسرائیلی‌ها وقتی جنگنده‌هاشون تو مسیر ایران بودن، به ما خبر دادن
🔴
من هم سریع وارد عمل شدم و تلاش کردم ابعاد حمله محدودتر بشه
🔴
همچنین پنج کشور منطقه با من تماس گرفتن و خواستن روی نتانیاهو فشار بیارم که حمله نکنه
🔴
من هم با نتانیاهو صحبت کردم و…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/133070" target="_blank">📅 21:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133068">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
ورزش سه: مهدی ترابی مصدوم شده و ممکن است لیست تیم ملی تغییر کند و از بین هادی حبیبی نژاد و امیرحسین محمودی یک نفر مسافر جام جهانی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/133068" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133062">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bjoehhuV5Ch174G0JUnoGU1GKJ29IvpuGQVnX44BCktkHbnoNy5sE7Eb2Ms1JyURkRaH5b_g95p9YBzK2_OOWC9JeRJeubopckp18LZVDsU9vp9yj290zTMo6fHy_0Jk_99OuqzZ4gPk1QC8DJF7PrB0p2TlJzELFafuKyJu9OXp_JXtFA2L523rlVwGdI2reeFwqyzr25IDjz8-u1jL4mzy9u-dNsJ_8iXxhLjauUTy5XIBfWxdq9uaaizVOonvHb2W5iQCO7djOq2ROSHE0e4sdrqf7aRkiEY_3wcS4QaLpgOTvmaUrqAa7o7pj8CYkUpn1o0Jt_P__LQQZC7ndg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JGpjZBAqYGH6NmXCXM9wjGRaV7Bi_rS87-Wm24skT0ddnCPkmtXXJWY4DEB7w0aT90YF7vOdQTfyJQUM9z3FhJV6ydIqIXsUdi8JAvkBv4YkFU6GQdZnEmEyLDdnRJG_OjH0b2RwbzuIFmEfqlnEnJ3ds4aycUzx-O2nOsljker7aPXS5Difqgeitk1b3VZg_l3K5PdwElADb_rxhA4lDuBaYoBWRQMKvTIc4Y1su3GI-5xSNrdNGBmeyxxMlI128h8rxBTv3Y18Wx-4HY2lXcK9wWB7QF5ak0JkTpo6n6DRIvO7aW1aA-C-DENjWT_de1YqV3vjp3e-wAPMtervRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-5EPzS6FrJnEYZpi5s0Fj1VXFH92th1feflzGloQN-NqFjpD-iXBC8d2LQCJDHXnOgJL_xWpfW_wsQcAZDqQGEztVtBjTyr78fPvFEO8WdCWClTBwlduAKVTzQFpu0pmAn_Lj7J1ROBrh7HdJVcMcipTgVO0vmOy-KGMZM_HqyhG8zuJZT7NWbZjNA8j_-oLh5gk-50Aa5ld9yR9Fm4EH8z5DA1QD6Ct_5yptKrwmsBWDRa_wE9cFcoopK_A1hIdWi5VdSFR9XDtjfyRxi70fnfVpJzAmNtf1cK0lGD7kf36VIYtbu7INZDF0BSHy1kW31PGPGN8m2NEFtIoX_BFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EK6Eb7lbbARqOsGrzTfGUKojHUMwDCUVDtCBO0tnbE6XGSe6R8f7J04JnNVm_VApKQBKdKKORUj_x8N6y9VvcQiJraF6ACSCMuLcTADHMgROZIgP0OS5ZRIDIolHFIb9LttDRim_ITSDy8iNT4daVeWxFFbYKtLiR6T1IM_h_TWo7MjbJ6R36oNPsNzpG9GzaPZDOGtt847E936MXbJh44nXs-KcMVyCdk_MONpJna0SsMJpCiUPQOjsORU_5nQ9bL5Xs3fvZmXrMu3xbjxX_1q_zMEalHGqs4EIhCwrWQWSy79KJcEtU03Xqf8x2B9KuYvzfz_Tk3CsWlfttEmo8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aFmGrZHmbRuU1cyc5ysu7fkojkq-sw7xdprTemskXlXzkuWJNzRgRZ2p6U7mogbUtLb28S_2Exxg1gBswVjoBpXvTMd01recD53ZF3NDsyPWfB2no7IMWYhutPV7GZ58qMrTFXuULkGmAmomvIuY3bW8ejw3LMz8a6cUl27pIFIXGrMgkHZAWtYZCSoy_JcmF0aNzBnB8PXFMNs3qT9jfhY2JFD-gPXeb0l2resZ6swOWRXjrkhBQoCuMUmTBweAFlzUjY7IgmUBFNym6a_kR-hCJhxCCK0gLcafOLHTnBxORLHnluKzFexsJaEZHFXQfgwLsm50po9dsvXnWtXiRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TH9LWtJF1VpzaD5JfjH9ioL6hKEwRPXukKET_SXhJ6Tom3zCh61SK8yhDNwOWsC3xcpTdRpnNM3BWqyCA4Y7pMTHpPmG_VW2FYFd1nP_tf7ofCvB9RAGQy1kcgo6J_i_yJeMzg76WFk-8Kce1XqImxDBw2DRjHsFSrq0TiX9AbQmjA9xCFCrS4VEVXCDEb2Q1EDv8ql9E7boAxP9wLtvHFFCP9JXQAuh6mYw41bcDV3KbMAg4e6nQVJPZh7MXTy2BXVxSbdKrjuNbhAKiwWZd8MysdOEkOtBp2CN0hHqC3nIxZlbavI0d-zzt0-CW1emz4KJheLJjamqkLBuScHbEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
آغاز دوباره تمرینات پرسپولیس برای حضور در تورنمنت سه‌جانبه؛ پرسپولیسی‌ها پس از وقفه‌ای چند هفته‌ای، کار خود را از سر گرفتند
.
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/133062" target="_blank">📅 21:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133061">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇺🇸
ترامپ به نیوزنیشن: یک جنگ دیگر را پایان دادم در مجموع ۹‌ جنگ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/133061" target="_blank">📅 21:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133060">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
قالیباف: اگر دیپلماسی را صرفا گفت و گو در اتاق های دربسته و لبخندهای دیپلماتیک بدانیم، از همان ابتدا شکست می خوریم و اگر صرفا به عملیات های نظامی و جنگ تکیه کنیم نمی توانیم از حقوق خود به طور کامل دفاع کنیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/133060" target="_blank">📅 21:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133059">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08f4d5075d.mp4?token=PGUiOZP5V7upv0M8KoyuqM5BpeKHZP4NE_1o3_BrQ0qTU3t0r_mj_osek_P9WMliw2QkMQFTbPKhFpKW_eAdFqzyIBglOirJbbicQOUaeCBumPZSwjTrSRKMPdlr9TKhZHSqnquT08HD0rJbTvBaAHa9MHO1l4cdlnsFJI8OpQRHDUiaB3t2WbeoDtd6Wsz_fOX5bS8RlWnJaZvj2OLFHW4-r330PrPyntyq2YBrVEzs_VXvAuuaqDX0TP3y28qhHaSuUxtHG01DtTVUj2vy8PdDcVBRX_ybuGkV31TGO5LLorr2Flh7SRxfml2bjXp6RkH8wFo1oDzU4cwRL8okTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08f4d5075d.mp4?token=PGUiOZP5V7upv0M8KoyuqM5BpeKHZP4NE_1o3_BrQ0qTU3t0r_mj_osek_P9WMliw2QkMQFTbPKhFpKW_eAdFqzyIBglOirJbbicQOUaeCBumPZSwjTrSRKMPdlr9TKhZHSqnquT08HD0rJbTvBaAHa9MHO1l4cdlnsFJI8OpQRHDUiaB3t2WbeoDtd6Wsz_fOX5bS8RlWnJaZvj2OLFHW4-r330PrPyntyq2YBrVEzs_VXvAuuaqDX0TP3y28qhHaSuUxtHG01DtTVUj2vy8PdDcVBRX_ybuGkV31TGO5LLorr2Flh7SRxfml2bjXp6RkH8wFo1oDzU4cwRL8okTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت رو از دست نده، همین الان وارد سایت شو و گردونه رو بچرخون!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/133059" target="_blank">📅 21:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133057">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‼️
🟪
چلنگر، مترجم برانکو: او نمی‌خواهد به طور کلی سرمربیگری کند
‼️
مذاکره پرسپولیس بسیار محترمانه و خوب بود. حتی برانکو به آقای اینانلو گفت اگر یک سال پیش شخص شما با همین ادبیات و محتویات با من مذاکره می‌کردید شاید الان من سرمربی پرسپولیس بودم!
🟪
اما در مقطع…</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SorkhTimes/133057" target="_blank">📅 20:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133056">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حضور وحید امیری در تمرین پرسپولیس  وحید امیری بازیکن پیشین پرسپولیس، برای طی کردن دوران درمان خود در تمرین تیم حاضر شد.  به گزارش رسانه رسمی باشگاه پرسپولیس، در نخستین تمرین تیم فوتبال پرسپولیس بعد از تعطیلات، وحید امیری بازیکن پیشین تیم هم حضور داشت تا روند…</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/133056" target="_blank">📅 20:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133055">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇺🇸
ترامپ به نیوزنیشن: یک جنگ دیگر را پایان دادم در مجموع ۹‌ جنگ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/133055" target="_blank">📅 20:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133054">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6mxdKQmLkhxTGIKQmunYCm1bzGY1zI0mk2HBsecLBs4xbxekibp4dRPVUMNgkBMo_b_aysuKwBKfEz5Hfj5tvWcDVZIGmJPoOS28jQANokBAZiywlOKM5IE-gMZnFWSFh1P_cicd1WUcZrPR3B68Ts0LEUjvKTMKZRN70VhbHWqdzCo0T-ddAOZ9WdaSAP6oqjnvufiUAx19Mr4SLGAyCevKL9y0yKMvzNs5BpfTo8cOuKb9FOiQByYojSUR46MztGDdSFozUyfszNREQ2-oq-FKE5Y_w5cXGGsyUxscZ6KbooPVF7KHhWESXQQsyDqkSqBlchttMjSGDBEqnxgOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تلنگر | #افشاگری
🚨
‼️
نفر بعدی کسی نیست جز مدیرعامل اسبق باشگاه که در این روز ها تمام تلاش خودشو به کار گرفته تا چوب لای چرخ باشگاه بزاره تا پرسپولیس به آسیا نره و به پرسپولیس برگرده…!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/133054" target="_blank">📅 19:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133053">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mh2urITuOubYATEsT5FWdPIVYZG0jSp5BsRXpyY5CP6Ly60x3li-0u4Za4j9n6WHDKOKZUg4B1-tRrb6kUW2jLgl0HAcidaBdU6CkYa4DUTkFzu_qltkSlfaydagJF1mGT7jloHaygI7T1MSAMwGpbMnzTjtdw92suMxABQ_Tt8gkP704-R4AMzO3EKV-lqpGmhjI4M5dre6TBA_2ARydpXNKaWBQ8PV4zdwd16njJYLjBxP_9x7_myFZaZoQJNDfJaxtvLeBll2JcTefilq6yl_0VnkkRPl8DBFdDntXxNMlrYXbBpXH04f99cuUkx5iFdDDNRpErWOXvYipXZLjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تمرین امروز پرسپولیس بدون حضور خارجی‌ها و ملی‌پوشان و سروش رفیعی برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/133053" target="_blank">📅 19:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133051">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
تمرین امروز پرسپولیس بدون حضور خارجی‌ها و ملی‌پوشان و سروش رفیعی برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/133051" target="_blank">📅 18:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133049">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hd2SHtjkCm0MSKCv8VIBq9SHWbUX5_uu6HAf8xy4xWkzsiqJNXSw9O7-YXJ9JQrmOsQk5m9-DU2x4utOepmQwIeekr_-DSJQM7wvzrBCOyRNckLQ-Ba7uypT3aeDmMwV2PnL4AdkFqrF-QsNd88n933HlCWP6z1cGyhhXqYi1wGLD27vDYu_qtCQTJZvFTYN6WTt7s0BLJkmHjFyId1bmS6oNhAbZBA6OAYYGUgFDy95o7umnbjcss8raqcGuSrjNs9_sKq-1LQfz1vBkxcQn6p4HObiZMFZkMkS4qx8d3K6oKqo-83Hru8h0-VqdTwtjrzneREhOdpQE0i-SvSyyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مصطفی قنبرپور، پیشکسوت پرسپولیس و مدیر اسبق این تیم، به‌عنوان سرمربی تیم نونهالان(زیر ۱۵ سال) و مدیر تیم‌های این رده سنی انتخاب شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/133049" target="_blank">📅 16:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133048">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
کرمانشاهی، معاون پرسپولیس: بنظرم مسابقات را برگزار کنیم خیلی بهتر است. اینکه سهمیه‌ها براساس جدول فعلی باشد، خوشایند باشگاه پرسپولیس نیست. پرسپولیس روند صعودی داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/133048" target="_blank">📅 15:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133047">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
محسن خلیلی: پرسپولیس همیشه خواهان جذب علی قلی زاده بوده اما خودش نمیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/133047" target="_blank">📅 15:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133046">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/133046" target="_blank">📅 15:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133045">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDViBqeO_T15yy5Hq45-MLU4MStHSf_uyy6KBwl8EqbzysEoMi_wGD7ucMC3UDhTJ5EX5xv8CzjRTi_EkQc6v9f3vXlhth44a6FolYROWYmFjsbnSFzkD-6KruvqPcQVc-PeioCKLNA9KUaWJSHK-3TM8kfv-kymQKvQcZANxWsCbbME8uuvFimD0slLcajeSdrF0beRPXu_hEBkgaXzTkIujjlBeuDaeH2I2Bkl3LQRRn2AZynUNkzM0PMbob2Kk5vH9HG-FCleTzXlWqlbTT-AB9eOakK8Mj8BzGJMH_4qto9Vbq5MzLzMQrcej9du5PqIFVcQ7pn0jhU1T64Izg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ به نیوزنیشن: یک جنگ دیگر را پایان دادم در مجموع ۹‌ جنگ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/133045" target="_blank">📅 15:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133042">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
🔴
فرشید حقیری: حدادی 3 تا جلسه با خداداد عزیزی برگزار کرده و خودش کامل در جریان امضای قرارداد هستش برای همین نمیاد تکذیبش کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/133042" target="_blank">📅 15:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133041">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👀
صلوات بفرستید…..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/133041" target="_blank">📅 15:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133040">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚀
صدا و سیما: جنگ پس از شکست دشمن به پایان رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/133040" target="_blank">📅 15:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133039">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
فووووووری/ با اعلام قرارگاه خانم الانبیا جنگ ۱۲ ساعته و اسراییل تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/133039" target="_blank">📅 15:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133038">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
قرارگاه خاتم‌الانبیا: پاسخی دردناک به رژیم داده شد و توقف عملیات نیروهای مسلح اعلام می‌گردد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/133038" target="_blank">📅 14:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133037">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
قرارگاه خاتم‌الانبیا: پاسخی دردناک به رژیم داده شد و توقف عملیات نیروهای مسلح اعلام می‌گردد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/133037" target="_blank">📅 14:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133036">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✅
🔴
فوری ترامپ:  هر دو طرف، اسرائیل و ایران، به دنبال آتش بس فوری هستند! مذاکرات نهایی در مورد "صلح" به شرط دوری از ناآگاهی یا حماقت در راه است.   محاصره به قوت خود باقی خواهد ماند تا زمانی که "توافق نهایی" حاصل شود.   همه چیز باید به سرعت حرکت کند. با تشکر…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/133036" target="_blank">📅 14:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133035">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‼️
🇺🇸
ترامپ:  اسرائیل و ایران باید فورا«تیراندازی» رو متوقف کنن رئیس جمهور دونالد جی. ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/133035" target="_blank">📅 14:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133034">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
نائب ریس کمیسیون صنایع: امکان قطع اینترنت بین‌الملل وجود دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/133034" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133033">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAVoKfiCzFvNjGFf88b1SyFutiW-lvkYjzMUkcGYcjORb6f1bO0OH2gmcdxlEU8P_AKZtIzo6lQdOHzsE-WfbQt-ksktRJUpsE7HfMlJ9mPxGhHxSPW9OKoA4dsefh0TJMpmmttwxi0zSZa4rv-rZv7QWft346T2R0bIna8mO_2ybQz4e7FSz7JLNiFTyJZzFWo8r3Cj3CMqRPY1knZ7ah1mv0W1sJ4lTrkBlqA5vgPOzGKlxrVmsQGqjjs92DApNry42Eqc_rfEVgHbpmWbmDKhRghxTYf7a7pZwnl07D5aYIfhdhaQJgsac8VrRgAliHx798Rjlj0aO67-3aqm6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تمرین امروز پرسپولیس بدون حضور خارجی‌ها و ملی‌پوشان و سروش رفیعی برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/133033" target="_blank">📅 14:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133031">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
فرشید حقیری: امروز جلسه محرمانه بوده و سرپرست جدید پرسپولیس انتخاب شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/133031" target="_blank">📅 13:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133030">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
🚨
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه  علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه  احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی  سامان قدوس، روزبه…</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/133030" target="_blank">📅 13:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133029">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
مدیرعامل و رئیس هیئت مدیره پرسپولیس هیچ اطلاعی از سرپرستی خداداد عزیزی ندارند و تا به حال جلسه‌ای با او نداشته اند.
♦️
اما منابع دیگری به ما اطلاع دادند خداداد عزیزی در روزهای گذشته با شخص احمدی مدیرعامل بانک شهر جلساتی داشته است/شاهین
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/133029" target="_blank">📅 13:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133027">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7hnvIziIXiPS3cpaOpsOL6yifQ0vBcfjI79FXHqxtIkf7kTrOAUQ2f4OvzUQzi7z0nmOqliwvJ6ToT9E1edYvNkAyR7_hsK6IdNiKMFREPsOApf_lUzXI3sBhUMhSoDbuylQTcJ5ggbf0_yJPaxWtDk5aoln3qLlcZXIsY2IUE9GMY-44GUyRU5IY790fImuOdguJaDf9Z5HLQkjQv2V-Bz9dn7MSCRshqm85UISxAfWm7-ib5VWZPL5StRjfBaCumacpf3KhIAMn9jvAkhLBWZKOajC_NnguLaG_EsPxf_o3k2cUOQIx2tH8kCX2TS4FifWCC7xbzGHLt1WAPybQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
ترامپ:
اسرائیل و ایران باید فورا«تیراندازی» رو متوقف کنن رئیس جمهور دونالد جی. ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/133027" target="_blank">📅 13:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133026">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=c5sGBOZxkkG6MgYJYu-kvYV3Vu6GjnJHGo78iHUdGKtjMXw3Qxlit9yAgpfa76ALU5Di6M0LX7WdhDtxW4-ett326Ts6lKU3kfft4huyAoYSxKs7rNg9S-i5QEbf_ccKL0ej__S6wU1KfSfL_Mwc3IbLlQsz8enE1pJ5JoqwGhPS9q90mqI9j_foV_MPrFhoTjFqCOwQkIIoh27jTjJ1MOgS40ab0t-5oAecI1qqpHKqGVygQhe6wz6EHn9fzGDB7qKeo-ut4S71aeQHA2lHgFJ9I90v9qyuDa2fifMTQNWei8DIF92-brS_OpG5Oj2eVsPZbk16XZexPomCT7oTJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=c5sGBOZxkkG6MgYJYu-kvYV3Vu6GjnJHGo78iHUdGKtjMXw3Qxlit9yAgpfa76ALU5Di6M0LX7WdhDtxW4-ett326Ts6lKU3kfft4huyAoYSxKs7rNg9S-i5QEbf_ccKL0ej__S6wU1KfSfL_Mwc3IbLlQsz8enE1pJ5JoqwGhPS9q90mqI9j_foV_MPrFhoTjFqCOwQkIIoh27jTjJ1MOgS40ab0t-5oAecI1qqpHKqGVygQhe6wz6EHn9fzGDB7qKeo-ut4S71aeQHA2lHgFJ9I90v9qyuDa2fifMTQNWei8DIF92-brS_OpG5Oj2eVsPZbk16XZexPomCT7oTJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- همه اون لحظه‌ای که سایت نصفه لود میشه و VPN قاطی میکنه رو تجربه کردیم، مخصوصاً وقتی وسط بازی یا ثبت پیش‌بینی باشی.
😑
- ربات رسمی تلگرام وینکوبت کارو راحت و ورود به سایت رو آسون کرده:
👇
-
🤖
@Wincobet_bot
-
🤖
@Wincobet_bot
- برای کسایی که بیشتر وقتشون توی تلگرامه، خیلی کاربردیه.</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/133026" target="_blank">📅 13:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133025">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
غیررسمی/ خداداد عزیزی به عنوان سرپرست جدید پرسپولیس انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/133025" target="_blank">📅 13:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133024">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
اوسمار تا پایان هفته برمیگرده به ایران و تا اون موقع کریم باقری تمرینات پرسپولیس رو برعهده میگیره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/133024" target="_blank">📅 12:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133023">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
‼️
اختلال شدید در اینترنت. فیلترشکن های رایگان دارن از کار میفتن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/133023" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133020">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
برای رفتن به بله و روبیکا آماده اید؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/133020" target="_blank">📅 12:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133019">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
🚨
فوری؛ انفجار مهیب در غرب تهران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/133019" target="_blank">📅 11:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133018">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
برای رفتن به بله و روبیکا آماده اید؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/133018" target="_blank">📅 11:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133017">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
باشگاه پرسپولیس:
‼️
ما با آقای تارتار مذاکره نکردیم. این حرف‌ها برای بازارگرمی است. پرسپولیس تاکنون هیچ‌گونه مذاکره‌ای با تارتار یا هیچکس دیگه‌ای نداشته و این ادعاها صحت ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/133017" target="_blank">📅 11:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133016">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
همزمان با صف شلیک موشکها هموطنان‌ هم صف پمپ بنزین رو تشکیل دادند تا این سنت حسنه و ملی رعایت بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/133016" target="_blank">📅 11:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133015">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇷
🇪🇬
🏆
دیدار بین ایران و مصر در سیاتل از سوی کمیته محلی برگزاری این دیدار از جام جهانی بعنوان"مسابقه افتخار"(Pride Match)برای همجنس‌گرایان نامیده شد!
‼️
‼️
پ.ن:طارمی و صلاح باید بازوبندی رنگین کمون(همجنس گرایی)ببندن.
🫣
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/133015" target="_blank">📅 10:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133014">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
🚨
آغاز رسمی جنگ
‼️
سپاه پاسداران خبر از آغاز رسمی جنگ با عملیات «نصر» داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/133014" target="_blank">📅 10:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133013">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
🚨
دستیار اوسمار در راه تهران/ ساعت تمرین تغییر کرد
✈️
جولیانو والیم بدنساز برزیلی پرسپولیس فردا ساعت ۱۴ به تهران خواهد رسید تا اولین جلسه تمرینی پرسپولیس برای آماده‌سازی جهت کسب سهمیه آسیایی را برگزار کند.
⏰
تمرین پرسپولیس که قرار بود ساعت ۱۱ برگزار شود به…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/133013" target="_blank">📅 10:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133012">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
آن‌ها مداركی به دست آورده‌اند كه نشان می‌دهد چادرملو مجوز قطعی حرفه‌ای نگرفته و مشروط به يك  توافق بدهی حقوق است.
⏺
چادرملو به پيمان بابایی از يک سال قبل بدهی دارد و هنوز سندی در اين مورد ارائه نداده است،اگر چادرملو تا فردا اين سند را ارائه ندهد بعد از شكست…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/133012" target="_blank">📅 10:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133011">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
🚨
دستیار اوسمار در راه تهران/ ساعت تمرین تغییر کرد
✈️
جولیانو والیم بدنساز برزیلی پرسپولیس فردا ساعت ۱۴ به تهران خواهد رسید تا اولین جلسه تمرینی پرسپولیس برای آماده‌سازی جهت کسب سهمیه آسیایی را برگزار کند.
⏰
تمرین پرسپولیس که قرار بود ساعت ۱۱ برگزار شود به…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/133011" target="_blank">📅 09:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133010">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
🚨
آغاز رسمی جنگ
‼️
سپاه پاسداران خبر از آغاز رسمی جنگ با عملیات «نصر» داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/133010" target="_blank">📅 08:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133009">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
آغاز جنگ ....اگه دوباره قطع شد همه چیز .مراقب خودتون و خانواده تون باشید ...خدا به همه رحم کنه .بازم جنگ .بازم استرس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/133009" target="_blank">📅 08:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133008">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e2e80c06fa.mp4?token=BEE1UVvrDlsd1i7C_EAT8MeQH2aeO1_T28MyR62_v6JJdtvmLP4Qf8-3DMtzuDnJ3IxCcaNajMgAw5vTBtrohAnpREWNROw-G6fynzAotTNFo43k_p0qj1C_mTcIFDDAO3Fsg8FEt__kBfDu96Kt1mzccg5qY_MKc_LYoKCjMzuXe8nEacmYzLIHbE9iicOPuyHMT_GNm_EvZB9i-ROyvUrGIo-d95WdwPpeU6bK3nc6afdWfciot6qJo9sZe16mUPqQcUhW3sp4zbduEMiQCBE1CZvoq5oe773Ds_tY0AroJkDwWT9YvNNox57Sd5TFYmU99CCfhGdjrcwpRbU1qg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e2e80c06fa.mp4?token=BEE1UVvrDlsd1i7C_EAT8MeQH2aeO1_T28MyR62_v6JJdtvmLP4Qf8-3DMtzuDnJ3IxCcaNajMgAw5vTBtrohAnpREWNROw-G6fynzAotTNFo43k_p0qj1C_mTcIFDDAO3Fsg8FEt__kBfDu96Kt1mzccg5qY_MKc_LYoKCjMzuXe8nEacmYzLIHbE9iicOPuyHMT_GNm_EvZB9i-ROyvUrGIo-d95WdwPpeU6bK3nc6afdWfciot6qJo9sZe16mUPqQcUhW3sp4zbduEMiQCBE1CZvoq5oe773Ds_tY0AroJkDwWT9YvNNox57Sd5TFYmU99CCfhGdjrcwpRbU1qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
#فوری
| کانال ۱۴ به نقل از یک مقام اسرائیلی:
🔻
ما تأیید می‌کنیم که یک تأسیسات پتروشیمی در ایران هدف قرار گرفته است
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/133008" target="_blank">📅 08:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133007">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
ساعتی پیش ارتش اسرائیل به اهدافی در تهران ، اصفهان ، کرمانشاه و... حمله کرد ؛ این حمله از خاک عراق انجام شد و بسیار محدود بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/133007" target="_blank">📅 07:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133006">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری، زیرنویس شبکه خبر و تایید شنیده شدن صدای انفجار در تهران، تبریز و اصفهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/133006" target="_blank">📅 07:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133005">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8O3EWZBxRKDLr8ew9D2p635Tv5GW6QccaazZh-GGyfOMMoNYbUey-bV-32jVWXYSk3wJdigghcGv1WqR3pDTJm_fBbSI7MORs8yHrHComOJekc7ZiCGl-veOuDJ6WO_TEzRajzOIQyF0erR8ENHHxnu8XyohE6NUrvFfbNbL9gEHTivJ74hsMrLhVZHBkrA1DytLnPH0YnYyYIkxUhbsnL6A_sJH5LonZeX4BFlALcAv4jp6uS-aANu2NvcjLhB9eSeNKi0SWRpk1F8jS2qN7dXQdLMyCz2xGKJN9sfikWHBjdaTnCskFmao8EUANXS8w-7IRrJOj1FeICL-zx41A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری، زیرنویس شبکه خبر و تایید شنیده شدن صدای انفجار در تهران، تبریز و اصفهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/133005" target="_blank">📅 07:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133004">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1AR_9LN24LDkF8B7srPGsWdQ2vlBSx8D1ZGUiRlKjzloiD5cS-uM6DsK0nVkoVLsvQFVeQ-gS-ikjMYuahCyt3vzBEaBX1z4pdBFSZEMzJ66CZ0OVHjyafIyNcCQGntx9_kBqaou6Gz-apD2uAJxxP9P8Xhy4CJXPgnnWWQRPLivz9oeEFEQ_M2-mX6_8RhnVUuCHTrMe-0QFrvGVUK8--z9DrOZeJaMpIZ3HSgdbfv_KeWCOQktTuxVad4UvKlxbTxuifIgncRZc5O9HW9yZfaJ7eZl_buPa3JmGWyHihOHYK1npndhj1tgPDCzlhtjZ5VUXmyvP8Ya1txevh34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس خوش‌آمدگویی برای کاربران جدید
🟢
کاربران جدید وینکوبت پس از ثبت‌نام و اولین واریز خود می‌توانند از بونوس خوش‌آمدگویی استفاده کنند.
📌
میزان بونوس تا ۱۰٪ مبلغ واریزی و تا سقف ۵ میلیون تومان می‌باشد.
📌
شرایط استفاده از بونوس:
حداقل ۱ گردش با ضریب ۱.۸
🔗
همچنین حداکثر مبلغ قابل برداشت از طریق این بونوس، ۱۰ میلیون تومان می‌باشد.
🔗
همین حالا وارد ربات وینکوبت بشید و پس از ثبت‌نام و اولین واریز خود، بونوس خود را دریافت کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/133004" target="_blank">📅 01:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133003">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚀
🔥
الجزیره: امشب ایران حدود ۱۰ موشک بالستیک به شمال اسرائیل شلیک کرد که ۴ اصابت به تأسیسات نظامی دیوید تایید شده و چند نظامی در این حملات مجروح شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/133003" target="_blank">📅 01:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133002">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
محمد عباس زاده با قراردادی 2 ساله به فولاد خوزستان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/133002" target="_blank">📅 01:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133000">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
کانال ۱۲ رژیم: ترامپ و نتانیاهو اکنون در حال گفتگو هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/133000" target="_blank">📅 00:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132999">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
باراک راوید، خبرنگار آکسیوس: ترامپ به من خبر داد «الان دارم با نتانیاهو تماس می‌گیرم و به او می‌گویم که در پاسخ به ایران حمله نکند.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/132999" target="_blank">📅 00:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132998">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
🎙
بازگشا، سخنگوی باشگاه:  بعد صحبت هایی که با کادرفنی و بازیکنای خارجی داشتیم قرار بر این شد که براشون بلیط بگیریم بیان.  سرپرست شدن محسن خلیلی هم تصمیم آقای حدادی بود که هیئت مدیره هم موافقت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/132998" target="_blank">📅 00:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132997">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
✅
عقب‌نشینی ترامپ: حملات اسرائیل به لبنان با من هماهنگ نشده بود  ترامپ در گفت‌وگو با فاکس‌نیوز: از حملات اسرائیل به لبنان خوشحال نیستم و این حملات با هماهنگی ایالات‌متحده انجام نشده‌اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/132997" target="_blank">📅 00:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132996">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
ترامپ به کان نیوز: فکر می‌کنم اسرائیل به اندازه کافی پاسخ داده است. نیازی به پاسخ بیشتر نیست. ما می‌توانیم پس از ۳۰۰۰ سال به صلح دست یابیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/132996" target="_blank">📅 00:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132995">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❗️
ترامپ به شبکه 12 اسرائیل
🚨
📰
:   در حمله موشکی هیچکس آسیب ندید. اگر نتانیاهو پاسخ دهد ، این ادامه خواهد داشت و ادامه خواهد داشت  ما بسیار به توافق برای پایان جنگ نزدیک هستیم و این توافق خوبی خواهد بود  نمیخواهم این موضوع توافق را به هم بزند. هر دو طرف حمله…</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/132995" target="_blank">📅 00:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132994">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
باراک راوید، خبرنگار آکسیوس: ترامپ به من خبر داد «الان دارم با نتانیاهو تماس می‌گیرم و به او می‌گویم که در پاسخ به ایران حمله نکند.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/132994" target="_blank">📅 23:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132993">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
ترامپ: به توافق با ایران نزدیک شده‌ایم و نمی‌خواهم اکنون در مذاکرات اختلال ایجاد کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/132993" target="_blank">📅 23:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132992">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❗️
دونالد ترامپ به Axios گفت که فوراً با نتانیاهو تماس خواهد گرفت تا به او بگوید که به ایران حمله متقابل نکند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/132992" target="_blank">📅 23:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132991">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
ترامپ : موشکاتونو شلیک کردین بسه ، بیاید پای میز مذاکره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/132991" target="_blank">📅 23:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132990">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
فورییییی
🚨
🚨
ترامپ خطاب به ایران: موشک ها را زدید و دیگر بس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/132990" target="_blank">📅 23:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132989">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
#فوری | ارتش اسرائیل:
🔻
آتش بس میان ایران و اسرائیل پایان یافت
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/132989" target="_blank">📅 23:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132988">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❗️
🔴
نت بلاکس: ترافیک اینترنت ایران 25درصد کاهش یافت/ اختلالات شدید در اینترنت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/132988" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132987">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
🔴
نت بلاکس: ترافیک اینترنت ایران 25درصد کاهش یافت/ اختلالات شدید در اینترنت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/132987" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132986">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
آغاز جنگ ....اگه دوباره قطع شد همه چیز .مراقب خودتون و خانواده تون باشید ...خدا به همه رحم کنه .بازم جنگ .بازم استرس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/132986" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132984">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
#فوری | ارتش اسرائیل:
🔻
آتش بس میان ایران و اسرائیل پایان یافت
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/132984" target="_blank">📅 22:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132983">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a27b87875.mp4?token=mgarelLj-_YbOVD2SdfZ0-SthoLVJTYYQQdilqbluJYq-7hopoSIayKHILTxRIfO1tAo8hilBf6C1ghgLHrtmBXOYMAsp5pfqc0bc1U9TF4pVsHdSY6ufLjk4Q_sPjKf-7fmoDUdQVA3v1JGxpBp9OyDuLXQXWnyBn_3aiSc4vbgVK9qqdNFjgd_jlQADtKCa1NgL2XsCDJl3s51ny8A0e5mot2avo2AbQhyHRbhMkGakHmOVE3CaH9HogS-GKKVg_G35ii2mgP5_VU_T1kTTzpE6RKstb-ocFL34iZXesEMyQ5C_lCYQsHZXOBls9CC8pWhPx8OhtLy-Rm8cJdayA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a27b87875.mp4?token=mgarelLj-_YbOVD2SdfZ0-SthoLVJTYYQQdilqbluJYq-7hopoSIayKHILTxRIfO1tAo8hilBf6C1ghgLHrtmBXOYMAsp5pfqc0bc1U9TF4pVsHdSY6ufLjk4Q_sPjKf-7fmoDUdQVA3v1JGxpBp9OyDuLXQXWnyBn_3aiSc4vbgVK9qqdNFjgd_jlQADtKCa1NgL2XsCDJl3s51ny8A0e5mot2avo2AbQhyHRbhMkGakHmOVE3CaH9HogS-GKKVg_G35ii2mgP5_VU_T1kTTzpE6RKstb-ocFL34iZXesEMyQ5C_lCYQsHZXOBls9CC8pWhPx8OhtLy-Rm8cJdayA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
| ارتش اسرائیل:
🔻
آتش بس میان ایران و اسرائیل پایان یافت
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/132983" target="_blank">📅 22:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132982">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری/سخنگوی کمیسیون امنیت ملی:  اسرائیل باید تنبیه بشه، امشب آسمان سرزمین‌های اشغالی را نگاه کنید  پ.ن آغاز جنگ
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/132982" target="_blank">📅 22:32 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
