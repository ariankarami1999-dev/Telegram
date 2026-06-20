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
<img src="https://cdn4.telesco.pe/file/ohJkvxcbBl1svpoh22ptzIfbPgMl0XMzaWEmrgsnZJpNTCho_HFgis0_dxAbh3Y2ik5ra_6q4R82w0G5X_lEXfsI6FBzaDDr-iWzY98DJLGisDiRf60yITCO8Y23QuXs07LIvJNJAhJArDVCpDaUtvHmk3xm-IUlIMU6dv5z2Bj6lTU59IOBsdUAQgEpIZabcT234PBD4LTbLb0Kr5lQTqNS169P_I_l8enRSHcgAOfKXvIAHjbYmXeVVyor4C25gJhOrbN7m177UJIN8TcIgIMTu7Lcn52Nefzy8412r1EZdgBPLdI2UKl_zfvwkULqxea8V3CUxtKjJNwF7BZd6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 222K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 15:53:56</div>
<hr>

<div class="tg-post" id="msg-66554">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5613ad59bb.mp4?token=H_CyeK2xd-mK7pOlufVNUFkqlYJ-JD6c2XU4h1XqA1gkRNhP9d4152RDMMr_UsNWYLXdcQ8SJsDtCFLdNvGnA9J49hf3wxcJFt6o3OHrXs7WndcS7WpVzVECmhDhrk-vfcMEjh50wCKZrWt4-BNDSGt7XUBuLAuMpEZISYjFeRbu8ORpRbK47SGRA-RvhfMnSIX-ywIu-ZeBP9Irumq81rgi7Qah68oAqXw37ZHAdSDuw6_1kZm4z3BCNvS85unBgMDmR1uz5ZsiqHtBViaTk4KZ2LevK1u8DPWPNxFAyvcjgXq0aFNlmslZYT0m5n2F458gflXr0VQYD0pFbPAtuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5613ad59bb.mp4?token=H_CyeK2xd-mK7pOlufVNUFkqlYJ-JD6c2XU4h1XqA1gkRNhP9d4152RDMMr_UsNWYLXdcQ8SJsDtCFLdNvGnA9J49hf3wxcJFt6o3OHrXs7WndcS7WpVzVECmhDhrk-vfcMEjh50wCKZrWt4-BNDSGt7XUBuLAuMpEZISYjFeRbu8ORpRbK47SGRA-RvhfMnSIX-ywIu-ZeBP9Irumq81rgi7Qah68oAqXw37ZHAdSDuw6_1kZm4z3BCNvS85unBgMDmR1uz5ZsiqHtBViaTk4KZ2LevK1u8DPWPNxFAyvcjgXq0aFNlmslZYT0m5n2F458gflXr0VQYD0pFbPAtuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❤️
فاکس نیوز:
بنا به گزارش‌ها، استیو ویتکاف و جرد کوشنر، فرستادگان کاخ سفید، امروز برای اولین دور مذاکرات در مورد توافق هسته‌ای احتمالی ایران در سوئیس خواهند بود، در حالی که اسرائیل به اهداف حزب‌الله در لبنان حمله می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/news_hut/66554" target="_blank">📅 15:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66553">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a273b0e83a.mp4?token=UelRZB1X05LpP_7C0iLp1TUHO_c7r_pip3y12ukVx4Av9qhEQp70KI4xPnOWjWzy_oAfSVNsblKpWetoMtOpIjzfaf1PJ-ElAn8LDNHZzP_fGZBMdYm-ij2I_C5F2ATByylQ82Yrd4iw0gryPX8LXBIXvrYBy6EvM3KoKjjLrIfPPqROtDMZw6bS0xbBUeTOqryGlwUQPYEhFvY8QPvWGxC5DZwhEjQO-3tpTpSqo0I5Aa4Yq3Q8F99jYSmSa9Tdr891KKeA19EbvBIShrd4wA6PpRbMdTJmWm4QhYiFb-5Pa7e8A4a83lHHSLvLiDAKUNQ4x4tiXitN1Buz4OGlaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a273b0e83a.mp4?token=UelRZB1X05LpP_7C0iLp1TUHO_c7r_pip3y12ukVx4Av9qhEQp70KI4xPnOWjWzy_oAfSVNsblKpWetoMtOpIjzfaf1PJ-ElAn8LDNHZzP_fGZBMdYm-ij2I_C5F2ATByylQ82Yrd4iw0gryPX8LXBIXvrYBy6EvM3KoKjjLrIfPPqROtDMZw6bS0xbBUeTOqryGlwUQPYEhFvY8QPvWGxC5DZwhEjQO-3tpTpSqo0I5Aa4Yq3Q8F99jYSmSa9Tdr891KKeA19EbvBIShrd4wA6PpRbMdTJmWm4QhYiFb-5Pa7e8A4a83lHHSLvLiDAKUNQ4x4tiXitN1Buz4OGlaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله هوایی اسراییل به مواضع حزب‌الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/news_hut/66553" target="_blank">📅 15:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66552">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJQ4Af5l0pM3ufgj31HLyVQ_jNGxixWN0zS4pNncPNXOu2UUqMnMTvIMCOBRHW-IMER7M_FgltX_YmSzrruZlpGHPSJVCK6usrroKMobviM6boe2USlOvl9vMXR-JZIzmK9Ua8nx0IMWTnwxmrUI3W3BuJoeDNmnDNwTRNiA5TyhWYkV0KVFX4juaCtl5r-s2sw7LbuUMdlONmrgRQSz57vuz3hnu9DfqDNmw4LBesw-U1hgSlXx2Iht8gPyIGMDsOUJ6Q2wOrXOgmNLhRxT8TNQoiMh6GExBv9qzlUag9xiMJzqfGLU03dG0hymkuGZsDCeDEMJpiNKPiouVKbnpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش دفاعی اسرائیل:
نقض مکرر آتش‌بس: حزب‌الله بیش از ۵۰ موشک به سمت سربازان ارتش اسرائیل که در جنوب لبنان فعالیت می‌کردند، شلیک کرد.
به منظور رفع تهدیدها و در پاسخ به نقض آشکار آتش‌بس توسط حزب‌الله، ارتش اسرائیل در طول شب ده‌ها پایگاه زیرساخت‌های تروریستی حزب‌الله و تروریست‌ها را در جنوب لبنان هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/news_hut/66552" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66551">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66551" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/news_hut/66551" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66550">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXcpZJbLQOk0_xOofbUe_vgU_TnXZHko3ncC0wljj-inOoBjwX0UNWfOWkoRJXE0YDP4C5whrr1_g2fWHU5HyhIfe5sGP-Z5jxq2tp5YIflZBoG3JIABtUrtsAJOU2fHOP3oiwkQfQa6BE9ZlJwBx-SHf26G1GNshxeGMvkn0obYeNOOKiSHNOP73PdpJ7askMR0KIukiDP1D_vn5HsxwsMjZo655LyeZV46GiF0CdvhW9IBDSSPoBcKWcA1KyABc85YZotHtxF4t0dtHEzTql3wyAhoiHXdpCjKR2WWM7AuHKutbSp_-mp9DCraZK0Ohbdbm213qBMyHyRJ-e1abQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/news_hut/66550" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66549">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7zVc0gmxAdwrdyyzN_PsSHXboTA46w-iQM1jLKSdF872SXn1NehdQV9K93oB0nLC3AeBwhunrRzC3l6dY1PhRHm_PkzznwGG4eJG6iFtJnthIVdfCiNoI_2_kfA9doUARU7cbnQ37QbNJW8UTZeLmeCXUmK-JeTnlXRL44ZpsA0gtzEBZsgpC7xIZB1ccUbr5yGCHckuVTpUVUfxhnYFXHRkgroh_U2DhZBVTFYdzJsXp3QaeLnzCL9kyMx2ZTbEtrJGM9IdvHwwwyi9uF3xm-Ng1kNrgT5JJQosIJAIbyYFu1L5AxJBYyRkvAYWZR_hvgQvv4hmARaF414n_iaKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
چپ‌های رادیکال احمق و دموکرات‌ها بالاخره فهمیدند که ما در جنگ خود علیه ایران چقدر خوب عمل کردیم، کشوری که از نظر نظامی کاملاً شکست خورد. اوباما فقط به آنها میلیاردها دلار نقدی می‌داد و هرگز از ارتش خسته‌مان در آن زمان برای انجام کاری که باید برای مهار بزرگ‌ترین حامی تروریسم در جهان — ایران — انجام می‌شد، استفاده نکرد.
آنها هیچ احترامی برای آن قائل نبودند. آنها او را، مانند جو خواب‌آلود بایدن، رهبر ضعیف و ناکارآمد می‌دانستند — و در این مورد ۱۰۰٪ حق داشتند.
ایران به مدت ۴۷ سال بدون مجازات باقی مانده بود تا اینکه من آمدم. و سپس همه چیز تغییر کرد. آمریکا بازگشت!!! رئیس‌جمهور دونالد جی ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/news_hut/66549" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66548">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
شناورها در صورت رعایت نکردن مسیر دریایی جنوب جزیره لارک،  ممکن است با «خطراتی» از جمله برخورد با مین، تصادف دریایی یا هدف قرار گرفتن مواجه شوند و مسئولیت آن بر عهده خود آن‌ها خواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/news_hut/66548" target="_blank">📅 14:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66547">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXkopTs0BPYS6hFohEBSehhkZGiQQEJ_jej0tHtHqWyZENT7E7DtjAZvopgJKwux4rCiHq8DaPn3PUtB5EUY47z8FURiLsNfZQQCZX7DnXHtjOl4Z3UDGndYeS4d6T-fnEJ0pndAsalVMtRtzArKy3sidtXFuRBpXmLE2M8aCZgOXnK1yeM7ufFQXDAi1grHX9wb0Sk_bGKSvrkMPOPMLz8xpcCADkniuaKJYBP4-VQUB897FF-CoLne-1jfaoD740IGrzF53Jwb98bWilPL4LVzv5wGlwn3IfECImosgMiCUL6TMzurs6vuU6e_QUPAZDImnnLQZP6vjQdx-1_b4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
هیئت ایرانی در مذاکرات این کشور و آمریکا تهدید کرده است اگر حملات اسرائیل به لبنان ادامه داشته باشد، تهران از مذاکره با واشینگتن صرف نظر خواهد کرد.
این منابع تاکید کردند مهم ترین مسئله اختلافی ایران و آمریکا پرونده لبنان است و محسن نقوی، وزیر کشور پاکستان، در این زمینه پیام هایی را به تهران منتقل خواهد کرد. نقوی روز شنبه وارد مشهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/66547" target="_blank">📅 14:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66546">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
نیویورک تایمز:
منابع غربی از نتانیاهو خواستند حمله به لبنان را متوقف کند تا ایران خروجش از مذاکرات را توجیه نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/66546" target="_blank">📅 13:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66545">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8c_sI4bhpD3XlcUC4C3Fm1ONNWynX_9FsHirWI9tlJysgPmAacUXFG0lQnhquIt66zeHGL-GeQ0IglieoMfwg2vSwAMIzPXlwXsDFUOvKFjlj41dAYUeIsWu5x7k01YX4uWNUlzYUem2ELCeJwQCE2sQIrGN3lPUed1dyqMiCpqOX4wnvtnFWoAqLouf4D0Sj60yU24vv4lPkDBPLg-f1jiNRP9RtQ_BdCOQnAUC_C7YKF4ntKSKRLhDvXKPtpoe0_ybSs9vE-ud935cazBLcHcFEABnKpVm28fTmb41fjSefm3HOGUzRFEVWNbv5kkgagXGp0yYQ_wKyLlL5NReA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رویترز:
توافق احتمالی ایالات متحده و ایران برای پایان دادن به جنگ و کاهش تحریم‌ها می‌تواند سپاه پاسداران ایران را به طور قابل توجهی تقویت کند.
سپاه یک امپراتوری تجاری گسترده در حوزه‌های نفت، ساخت و ساز، کشتیرانی، مخابرات و زیرساخت‌ها ایجاد کرده است.
سپاه پاسداران در موقعیت خوبی برای به دست آوردن سهم قابل توجهی از مزایای حاصل از صادرات مجدد نفت، سرمایه‌گذاری خارجی و یک صندوق بازسازی ۳۰۰ میلیارد دلاری پیشنهادی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/66545" target="_blank">📅 13:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66544">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
وزیر کشور پاکستان برای دیدار با مقامات جمهوری اسلامی وارد مشهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/66544" target="_blank">📅 13:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66543">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTFKrpLbsUTt3VrGIUzYrmTaC-3UPhAjoqG4JjvP3V9Xhi-2vOIfOA400zctzFX4-9YyztLlSb-QG4AYv9jpqTQX5vx6wcZBUkj70bQSc_zfkSaAtKquHE0sfWtR9Xgv2mXNbPJau_axV-o-eyQrTXxWL4AZ8JOFmVunYlhnrNoyIfTgmACtSyl7AbBpQXaLCooqdrbmq7HFuHsK0nY6y4ajXUNGxdoP6BHe5phIMu_2FAA-968nyloD42hTBtLGWA5A-CabnKpuS7jANdmtqLT8mGiH1wVgDeX_Bb8HQ0ucDu-lF4MvOEjf3EYOIxbAD7AWxeYbOTMbvA4dh4ZAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قابی از حملات صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/66543" target="_blank">📅 13:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66542">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrQyu_9bC2V9JG69shEaRJbMN-of0J7fvIYlPWMD1wmsx0F5lvAGwcFiZkI8OaLGyHsSdSfb_g66o-0jws8e-gpIGNLwnUpgnVGV5Uv9Ir-9A3b9EJVcw1lsVjfKNONvsWaVVhmdiGOSPm7rrjjXD4ivvIG5bJwWKlqF1-1TC1z7TMbl9RfUjLzraYneSdTUXWgADd5Yn6G9ErylSk0uHqXqPW0iQS6mPRQ6xAjB46hha0ZvaW473aYzVol16gI6B6HFNvoT7G3rreWku8KNlACvyxPX0fiQV3Jx4dCJ2cynGjVb7NUwspIAofQ9IB14z5NX1WKMGbHJzMyTm357EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اتاق جنگ اسرائیل:
نیروی هوایی اسرائیل در واکنش به ادامه شلیک موشک‌های حزب‌الله و نقض مکرر آتش‌بس، اهداف تروریستی حزب‌الله را در سراسر لبنان هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66542" target="_blank">📅 12:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66541">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/417add4a63.mp4?token=P3zHPcDp4y7kSuQqpSOETteZEiaHFpapcbySd5nTztKqeJ4MioYPBYjbmA5GohWPVV-2OkZzOcaZq84mR5u89Czp6-nIbVmH9fTx9UTu9xHBdxSiCu9exf6SjCoLZR5ckH094FAfbG9VXYkWdaaOuwzvXK7T1FC7vLGtUV5L1MFfDbZ2fZaEcMQP44OJhbVLH7jrT00InYA0PpW4SGyG4oH9nnHXWCKovtQ2VGX1k4jgb-52zrQZDEXkDut1CvTqbbrGZguUa7fqxTmTj1aFvUBRaw83XRHJVVggL76yyEKPu9VVLsDv1FVMyoGZer5UgSHKCmjMNIPFJmZC-rorGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/417add4a63.mp4?token=P3zHPcDp4y7kSuQqpSOETteZEiaHFpapcbySd5nTztKqeJ4MioYPBYjbmA5GohWPVV-2OkZzOcaZq84mR5u89Czp6-nIbVmH9fTx9UTu9xHBdxSiCu9exf6SjCoLZR5ckH094FAfbG9VXYkWdaaOuwzvXK7T1FC7vLGtUV5L1MFfDbZ2fZaEcMQP44OJhbVLH7jrT00InYA0PpW4SGyG4oH9nnHXWCKovtQ2VGX1k4jgb-52zrQZDEXkDut1CvTqbbrGZguUa7fqxTmTj1aFvUBRaw83XRHJVVggL76yyEKPu9VVLsDv1FVMyoGZer5UgSHKCmjMNIPFJmZC-rorGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوس جواد مینوازد
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/66541" target="_blank">📅 11:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66540">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda1b3db16.mp4?token=pjNHMs9qtLIRlV47A1VXKuHtX83FdvIai1dASQTfKSJU2eaqG0cwn2F-g9F7RoLe_qoDCRIwU-c-pkKbLK7qxiOsxxjkUeRHjrnt3EIQpuI_nZzZgee0ENb66fJbxuC8RX3brxoATdc_l6172qg-qGOubXpcXeUrqZVRH1URu9rxr5ehPTGxbHG3FuwLvILQ90V2EURyDsQpU0CTSyX9_D0jD2BVFYlfum9g9_0ROIzPrsoHovo7lrpEXKv7SnVNKH_Zxb-Co4YmswYalaGJM-5nh3A9N6KBXU7dWJ1N6SX0yJhpCZ6_lPsmWiJ38fEeFZM1EGDHqqquAOwvGAsEeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda1b3db16.mp4?token=pjNHMs9qtLIRlV47A1VXKuHtX83FdvIai1dASQTfKSJU2eaqG0cwn2F-g9F7RoLe_qoDCRIwU-c-pkKbLK7qxiOsxxjkUeRHjrnt3EIQpuI_nZzZgee0ENb66fJbxuC8RX3brxoATdc_l6172qg-qGOubXpcXeUrqZVRH1URu9rxr5ehPTGxbHG3FuwLvILQ90V2EURyDsQpU0CTSyX9_D0jD2BVFYlfum9g9_0ROIzPrsoHovo7lrpEXKv7SnVNKH_Zxb-Co4YmswYalaGJM-5nh3A9N6KBXU7dWJ1N6SX0yJhpCZ6_lPsmWiJ38fEeFZM1EGDHqqquAOwvGAsEeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
حدادعادل: والا منم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66540" target="_blank">📅 11:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66539">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4121482563.mp4?token=somjypIJQkeXmQnY6A21d8xpjQ5rRhWbOqMhtNx9fqa_zeJfVQ_3K1Q_-op8baN7DdjTiC-v7oSDJh72t_Cc-WbrEyiHIBdftHQ6gVQm22bnK0ziLC38BO5-dMBQh3-8ouc3_gZEmi4V3XYDEq-OYYFxD0-kKm_bPK9mTMOcV-7SEwnYnpIsbNGiEAT0zWY01pUQiOkucgzHc4552YomLUMVSQWimRJtbJsCpKJjC5GtSscICr1XlwvN6oXb0FglCqI0htlCFZO2i2ficx0n2sGiinHn4EZq3u98CbOLHDkyoM7_OOCKA1X4pZ58LH9izge6Se9NLQutsQzLRsSD3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4121482563.mp4?token=somjypIJQkeXmQnY6A21d8xpjQ5rRhWbOqMhtNx9fqa_zeJfVQ_3K1Q_-op8baN7DdjTiC-v7oSDJh72t_Cc-WbrEyiHIBdftHQ6gVQm22bnK0ziLC38BO5-dMBQh3-8ouc3_gZEmi4V3XYDEq-OYYFxD0-kKm_bPK9mTMOcV-7SEwnYnpIsbNGiEAT0zWY01pUQiOkucgzHc4552YomLUMVSQWimRJtbJsCpKJjC5GtSscICr1XlwvN6oXb0FglCqI0htlCFZO2i2ficx0n2sGiinHn4EZq3u98CbOLHDkyoM7_OOCKA1X4pZ58LH9izge6Se9NLQutsQzLRsSD3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇺🇸
‏ترامپ درباره کشته شدن قاسم سلیمانی:
اسرائیل در آخرین لحظه، زمانی که من سلیمانی را کشتم، از عملیات کنار کشید. قرار بود این کار با اسرائیل انجام شود. یک عملیات مشترک بود.
ما ۳۰ روز روی آن کار کرده بودیم. او فقط با هواپیماهای مسافربری و در میان تعداد زیادی از مردم سفر می‌کرد، چون می‌دانست ما آن هواپیما را سرنگون نخواهیم کرد. می‌دانید، هواپیمای نظامی قضیه‌اش فرق می‌کند.
او سوار هواپیما شد و همه چیز طبق برنامه پیش می‌رفت. اما یک روز قبل از عملیات، اسرائیل به ما گفت که در حمله شرکت نخواهد کرد. من هم این را درک کردم، چون برای آن‌ها چندان مناسب نبود.
اما من سراغ چند ژنرال رفتم؛ نه آدم‌های نادانی مثل میلی و بعضی از این افراد که واقعاً آدم‌های احمقی بودند و تصمیم گرفتند تجهیزات راجا بگذارند. من هیچ‌وقت تجهیزات را جا نمی‌گذارم.
به چند نفر از افراد کاربلد مراجعه کردم و گفتم: “نظر شما چیست؟
آن‌ها گفتند: “می‌توانیم بدون آن‌ها هم این کار را انجام دهیم؛ نیازی به آن‌ها نداریم، قربان.
پرسیدم: “آیا به همان خوبی خواهد بود؟
گفتند: “به همان خوبی یا حتی بهتر.
و آن حمله بدون هیچ نقصی انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66539" target="_blank">📅 10:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66538">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aceb39213f.mp4?token=WePaD2_p1JFvHSLloG8smPfQA2x2__n2nswpneAelsHMTsl7HxUY1nkcZ-NU0m9Oa8OQPQaKG5BOwy8QUTo7HVM37BO-d3X3ZUyXd5iggZSk417-s9HA_RY3sH7Jml5GwOvaNEGY3jxvWu1FgI1v6imSAWwHUXT-JI0Lqe0OJCclcfJG_kdHZSdHZ-iToiH4ByUrbGXgt3SskEUGOryTiRZiSUBx-eKak4iV_pzefuRPwO3fRxiNync5O239pDqkaUj0WjRGY-QtsI505jGpUzqd0Lvn-Wcs-dWh8VdjiPfJBb-X8tZjoOLz5tifP-WrAE2cmbEC05Y5e8aBzy24ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aceb39213f.mp4?token=WePaD2_p1JFvHSLloG8smPfQA2x2__n2nswpneAelsHMTsl7HxUY1nkcZ-NU0m9Oa8OQPQaKG5BOwy8QUTo7HVM37BO-d3X3ZUyXd5iggZSk417-s9HA_RY3sH7Jml5GwOvaNEGY3jxvWu1FgI1v6imSAWwHUXT-JI0Lqe0OJCclcfJG_kdHZSdHZ-iToiH4ByUrbGXgt3SskEUGOryTiRZiSUBx-eKak4iV_pzefuRPwO3fRxiNync5O239pDqkaUj0WjRGY-QtsI505jGpUzqd0Lvn-Wcs-dWh8VdjiPfJBb-X8tZjoOLz5tifP-WrAE2cmbEC05Y5e8aBzy24ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تهدید به قتل پزشکیان توسط مداح حکومت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66538" target="_blank">📅 10:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66537">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae617fb56.mp4?token=l-uKTmmoTR276k9YVjapm1sgLq9iAQND-72VzMGsax5QKaEryAv4xqYl8myaHJ4RgdI-pCq31I1NXQIVKA0PFS6Qs66ix2BJlbEu_TTQ01TO5GV4P9eqssy8vR1-7Wx6ENx0Zdixtnl4TZwqniik79vrAAT5AbVzmtR8ecR7JvVNEC0ErarOK9cpWTnlBhNXIuWOkxUEsa1th-_3T8T5dTDInQMiivPpU4PPlQvnJgP-4iLYdZZyR6h9XNYu0gY1ovY-HxzFQqn1Y1O-UGV9XagOCMlMkwrmrMPwLwcIIqx88myaaahEkDIPPKS6x4Tf3By6C73qUibSq9yej2oOQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae617fb56.mp4?token=l-uKTmmoTR276k9YVjapm1sgLq9iAQND-72VzMGsax5QKaEryAv4xqYl8myaHJ4RgdI-pCq31I1NXQIVKA0PFS6Qs66ix2BJlbEu_TTQ01TO5GV4P9eqssy8vR1-7Wx6ENx0Zdixtnl4TZwqniik79vrAAT5AbVzmtR8ecR7JvVNEC0ErarOK9cpWTnlBhNXIuWOkxUEsa1th-_3T8T5dTDInQMiivPpU4PPlQvnJgP-4iLYdZZyR6h9XNYu0gY1ovY-HxzFQqn1Y1O-UGV9XagOCMlMkwrmrMPwLwcIIqx88myaaahEkDIPPKS6x4Tf3By6C73qUibSq9yej2oOQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات اسرائیل به مواضع حزب‌الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66537" target="_blank">📅 09:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66536">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7deed372.mp4?token=OGqZUzJNCbj8f00zo8-6h4OBbdAq_htvpPBcjTbURB4IOReNWD5nQaQOYoLyqgqTfBeW50_cYF1ySOQOs9O0klPXOn1mkUIOJnNe-xC2fpXQd2N91DZrvDwZRFJUnNs-jUupUv96v658HOYn51ku78m28GzhRN_g-pFOUtLG0BVIFYvOc2CI1A3E7mecFaNP0LRI9s8D-yJlY-PV9FVWi_1fC3l5cDN3LhQEvXMg3TljyEAzVzFOziDnNaT3S7FyEcm5E5dB_vw0K4H-tHGCQeRdrF-BX7nxA2cEfXZ4Ilunpvr8ma1ocFcDcgQ7UO51S0UDXb8a8tmVV3f-w3EQow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7deed372.mp4?token=OGqZUzJNCbj8f00zo8-6h4OBbdAq_htvpPBcjTbURB4IOReNWD5nQaQOYoLyqgqTfBeW50_cYF1ySOQOs9O0klPXOn1mkUIOJnNe-xC2fpXQd2N91DZrvDwZRFJUnNs-jUupUv96v658HOYn51ku78m28GzhRN_g-pFOUtLG0BVIFYvOc2CI1A3E7mecFaNP0LRI9s8D-yJlY-PV9FVWi_1fC3l5cDN3LhQEvXMg3TljyEAzVzFOziDnNaT3S7FyEcm5E5dB_vw0K4H-tHGCQeRdrF-BX7nxA2cEfXZ4Ilunpvr8ma1ocFcDcgQ7UO51S0UDXb8a8tmVV3f-w3EQow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ هواپیمای «ایر فورس وان»را که از قطر به عنوان هدیه دریافت کرده بود معرفی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66536" target="_blank">📅 09:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66535">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a046173b76.mp4?token=mTyt2q_5NwuI79H5URLbLxIulv5Y2wxjPmTa5Xk6GV5zu4Tjna_DVtYk6tvT6XsgtaD7IRnfqWHxshO5wqUNxCyMGeu6yqE4peEyCElr4RjkXFMxbvTh235z6UM4FzT-BpT5LOsBmMISpDFpQXBg-Kwo-Tvi5an0zxIty1F4wzLDidF9kTsNtz10o20LmqXz_SEtKldrRsToq6wtGi8XsniNebD2YIVEU2GZi7YW14IK82qDO7eUz-e3rVyVgcl6u7RhscPYPGv9NMNSreHkkv08enNYChvaEHMGjQhpewuJzq9jQelgRdAgDpmg8fARIEfkbNk4E-K8KPX3hOiCSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a046173b76.mp4?token=mTyt2q_5NwuI79H5URLbLxIulv5Y2wxjPmTa5Xk6GV5zu4Tjna_DVtYk6tvT6XsgtaD7IRnfqWHxshO5wqUNxCyMGeu6yqE4peEyCElr4RjkXFMxbvTh235z6UM4FzT-BpT5LOsBmMISpDFpQXBg-Kwo-Tvi5an0zxIty1F4wzLDidF9kTsNtz10o20LmqXz_SEtKldrRsToq6wtGi8XsniNebD2YIVEU2GZi7YW14IK82qDO7eUz-e3rVyVgcl6u7RhscPYPGv9NMNSreHkkv08enNYChvaEHMGjQhpewuJzq9jQelgRdAgDpmg8fARIEfkbNk4E-K8KPX3hOiCSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف در حال اهدای تندیس حاج قاسم به نیکلاس مادورو (خرداد۱۴۰۴)
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66535" target="_blank">📅 09:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66534">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
🔴
فقط نظاره گر فوتبال نباش پیش بینی کن و پول دربیار
💵
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66534" target="_blank">📅 01:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66533">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUqoJ4iOUxQuTDI9k3DMWqxSXpL0MHJjL1pV4eQiOz66lUWSwE1AmTCXK9Q6tB5gHtFCfxGPYj4MBdhO4FcX6TFQFSJSLt3q6vH6fSdBm0q7-Rf9KLcYVXYrMm0rJrgtSUht7kPeLLfcNTy58ng2RYM6Soteui2HhxCKOguB445Be9dVVRAkIHaqfMN_M1OvpzvavVQztecC03tmk0VMjZ0LBsOJLkuUUMUAshLzp7B21ihP4kk3ExW8KDGzjun9txMjL6hVTSpe_NOVkHgT46gWPR86zcgNN40iOb9E85Fnv4TY1tUcJrVzFNmKgqYPSThYNGIg44B1V67IUdYWLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66533" target="_blank">📅 01:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66532">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb104aecb9.mp4?token=NOoE_K6gSOZbFGFlQRl8hvZTi9Qw-43OKUbZEMtPx54VHHYdmZQminRSmKTRLrMVudwarKAuIY4Qgs2Zo1bO9ryTtFCCNUo-vN4iUibdwXCNlalBa8COcz9XNyLy1eNyeEg_F30wwTH7-0dEUCtkKZUhPpiST-M5SSQbIzzJ7r75v76vXgIh0LPJ7hQnusb_BIiz6wD1DwC6glb1bLzlBRRsO1_GZey9ZaX_Jf23DHKekVEPPHDT4wc-j2Ny_sQYhzJ7ASARVwLhlPDJNy6tbF2SIHRbem1wXYZ1YNca0JVaTdpacEwEko3N2xWuE-Xpxz-em8J9IyDNxDXkgOQK4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb104aecb9.mp4?token=NOoE_K6gSOZbFGFlQRl8hvZTi9Qw-43OKUbZEMtPx54VHHYdmZQminRSmKTRLrMVudwarKAuIY4Qgs2Zo1bO9ryTtFCCNUo-vN4iUibdwXCNlalBa8COcz9XNyLy1eNyeEg_F30wwTH7-0dEUCtkKZUhPpiST-M5SSQbIzzJ7r75v76vXgIh0LPJ7hQnusb_BIiz6wD1DwC6glb1bLzlBRRsO1_GZey9ZaX_Jf23DHKekVEPPHDT4wc-j2Ny_sQYhzJ7ASARVwLhlPDJNy6tbF2SIHRbem1wXYZ1YNca0JVaTdpacEwEko3N2xWuE-Xpxz-em8J9IyDNxDXkgOQK4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هم اکنون شیرینی آتش‌بس در لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66532" target="_blank">📅 00:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66531">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d8d08f74c.mp4?token=hkfBz-zGtSfbvRuxM7kWiQPtZro56VDtwpUAJ4QPcC6Mntv5ymBHtXYNtQpazr1t2mivUaCdI4FRfR_GU4wiDs4RWz5XJhHHioABysseZTcIjuRzLHiagtFJNuTkVcozEz9SHWtcXJIbQPLDsONbgYqMSiY8qg33_sK7zYpY2nNk8Iic_393au1wbnJj_1Zi58NLvdccGKErMvWT7dW2mS1FxNJn94a_3pSwcvsbYW1OYvZYfnZ2jswXcR0iSy_-ZoL1IVtnH8DoT-9HBE8eKz7rH1ObfYo1OVGTL-41l8TlSSkVGrsQJ049LyaudXuVtFLdYl_WjCoXidaYPdDWzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d8d08f74c.mp4?token=hkfBz-zGtSfbvRuxM7kWiQPtZro56VDtwpUAJ4QPcC6Mntv5ymBHtXYNtQpazr1t2mivUaCdI4FRfR_GU4wiDs4RWz5XJhHHioABysseZTcIjuRzLHiagtFJNuTkVcozEz9SHWtcXJIbQPLDsONbgYqMSiY8qg33_sK7zYpY2nNk8Iic_393au1wbnJj_1Zi58NLvdccGKErMvWT7dW2mS1FxNJn94a_3pSwcvsbYW1OYvZYfnZ2jswXcR0iSy_-ZoL1IVtnH8DoT-9HBE8eKz7rH1ObfYo1OVGTL-41l8TlSSkVGrsQJ049LyaudXuVtFLdYl_WjCoXidaYPdDWzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت پزشکیان
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66531" target="_blank">📅 00:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66530">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21fdcbfae8.mp4?token=tM3nc8jODxvczAHNyyUZbU4ecAsazZIOkSnDW_tOW_T42riGwtPYp9e7Gu67vLO0rhLtJmbUiEgcHNEPdr9-VITh6IRtXISRQDDciwOAOvOZ2UW5k3SXwrEudgk5XUtCjBeoYIcfaEl8m8lYCkAu_FwZWEStcBTMWOenpjNwytj_rYqbecCQIlPdiU-jOktn602exo6bGRe2ZZoR7ZLVkWsRK73tIjkzGetD1mtEMbKPqVjA0m1sBMpbJwp-b4Mft7PXn2PnJGQAmMNM0iByovpGeLl4a6eXhzG6AN6TYNNHProhoGzQ6i5lAXu-kM0_oOVIJ2aXtCui4KCNkWaPYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21fdcbfae8.mp4?token=tM3nc8jODxvczAHNyyUZbU4ecAsazZIOkSnDW_tOW_T42riGwtPYp9e7Gu67vLO0rhLtJmbUiEgcHNEPdr9-VITh6IRtXISRQDDciwOAOvOZ2UW5k3SXwrEudgk5XUtCjBeoYIcfaEl8m8lYCkAu_FwZWEStcBTMWOenpjNwytj_rYqbecCQIlPdiU-jOktn602exo6bGRe2ZZoR7ZLVkWsRK73tIjkzGetD1mtEMbKPqVjA0m1sBMpbJwp-b4Mft7PXn2PnJGQAmMNM0iByovpGeLl4a6eXhzG6AN6TYNNHProhoGzQ6i5lAXu-kM0_oOVIJ2aXtCui4KCNkWaPYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد بایدن:
ما مردی داشتیم که نمی‌توانست از پله‌ها بالا برود، و من نمی‌خواهم در مورد این صحبت کنم چون اگر کمی زمین بخورم، می‌گویند: «اوه، این وحشتناک است.»
باشه، می‌تواند اتفاق بیفتد.
اما شما نمی‌توانید هر بار که روی صحنه می‌روید، زمین بخورید.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66530" target="_blank">📅 23:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66529">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5871cd20e4.mp4?token=mZxm-aSPETqnVWje93mF_0xSqXU-natRqIfOtcCaApFYE3UMdwkV8KHUCEYwjXd0D5_USRJG0iarC8kU5dFszn1e59BOBYKZLUJVOwR9No6bA-HeD7Zp5IsmpqVzcBbxYAUIuTxmv5Twp12E3pxQWB09i4vHyZyqMcy0WRk145qx6FFQjWBfxf42cf9MKODELd5F-JId0mCU4d2zr-TQyEwGrnwQkZon__tegz5QPwyu2FMYo8JkeglHr8X1sYBLBDkpkWzV2vhssQ52dRaP7fIufi25DS-PjWvmlMvMfmneLTzb0ilQ0YDndKwUKt1SN_VLgBq07OcPX6RJWvfQ8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5871cd20e4.mp4?token=mZxm-aSPETqnVWje93mF_0xSqXU-natRqIfOtcCaApFYE3UMdwkV8KHUCEYwjXd0D5_USRJG0iarC8kU5dFszn1e59BOBYKZLUJVOwR9No6bA-HeD7Zp5IsmpqVzcBbxYAUIuTxmv5Twp12E3pxQWB09i4vHyZyqMcy0WRk145qx6FFQjWBfxf42cf9MKODELd5F-JId0mCU4d2zr-TQyEwGrnwQkZon__tegz5QPwyu2FMYo8JkeglHr8X1sYBLBDkpkWzV2vhssQ52dRaP7fIufi25DS-PjWvmlMvMfmneLTzb0ilQ0YDndKwUKt1SN_VLgBq07OcPX6RJWvfQ8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت
ترامپ در مورد ایران:
من بزرگترین پل آنها را خراب کردم چون آنها دیر به جلسه آمدند. آنها گفتند که این خیلی خوب نیست.
آن پل، این پل جورج واشنگتن آنهاست. من آن را در سه دقیقه از بین بردم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66529" target="_blank">📅 23:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66528">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e43d6d5b.mp4?token=q4zACvkAbi7IjWmS-yEP3Tcr0_mGcWQ7ztRPG2lJOlQgwXAd1fr2hay4xhsw9pVlfrsH2Q6e5gnExjuqsIb7ups1fqk05hgjCfymyMfNtuk781VnMuM0VA1YBbfPkR4Z2qcMRBctGMvY6Jn_gxDEMn8Z92w15Lqklxt7iu8ad_vj944WN6y6QJCSnwfJYYoD3y7iYUmaUzgEn3IYpTkhqU7bbepoSd1pUKeNMeOgeOfFlD7UJ9pgVuOJ7BODJK5LGNXsVN2LD3IyLjaSHuKQV3JslVHc-vdJp7DSwimDPE7ll2Z69WJMdtrw4AJqeQ-plSa9ik_Vdp4CBlfYnOWpiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e43d6d5b.mp4?token=q4zACvkAbi7IjWmS-yEP3Tcr0_mGcWQ7ztRPG2lJOlQgwXAd1fr2hay4xhsw9pVlfrsH2Q6e5gnExjuqsIb7ups1fqk05hgjCfymyMfNtuk781VnMuM0VA1YBbfPkR4Z2qcMRBctGMvY6Jn_gxDEMn8Z92w15Lqklxt7iu8ad_vj944WN6y6QJCSnwfJYYoD3y7iYUmaUzgEn3IYpTkhqU7bbepoSd1pUKeNMeOgeOfFlD7UJ9pgVuOJ7BODJK5LGNXsVN2LD3IyLjaSHuKQV3JslVHc-vdJp7DSwimDPE7ll2Z69WJMdtrw4AJqeQ-plSa9ik_Vdp4CBlfYnOWpiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگر همین حالا به آن‌ها حمله می‌کردم—در حالی که ما قرار نیست نیروی زمینی بفرستیم، و شما هم نیروی زمینی نمی‌خواهید، درست است؟
اگر نیروی زمینی نفرستیم، احتمالاً همان افراد به اعماق غارها می‌روند. به آن‌ها “غارهای گرانیتی” می‌گویند. آن‌ها بسیار مستحکم هستند.
آن‌ها خیلی عمیق می‌روند، و بعد وقتی ما متوقف شویم، بیرون می‌آیند و احتمالاً همان رهبران قبلی خواهند بود.
در حال حاضر تنگه هرمز کاملاً بسته شده بود.
پر از مین می‌شد و موشک‌ها از بالای کشتی‌های میلیارددلاری عبور می‌کردند. آن کشتی‌ها دیگر هرگز عبور نمی‌کردند.
ما برای ماه‌ها نفت نداشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66528" target="_blank">📅 23:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66527">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7522060f48.mp4?token=VyJutoiEJxkYIN56nz22NJPUHLT8OhiGdpPpSaAXVBqKv3fAbfXM8MTXpFa-_KKU-VLrm0fEOX04P_Yrommr5hmvzOtDhekBDtiHn632CCGczs3XtrPywdqIyM1ZRubSMeqGZklvu4rd2EVRQev18psSTNwZn892n3eCU76roi4AtFLO-Hl76DieniL_IrKO-bC4ApywItt_8Xb5zoj65tzVi6is9QwMJEiGHo20Pa0-yZXuyV_KtntEWTSYV2cOIZ1SQwbsoGk_Mc3nrh1Je14xuOesFLx8dqilBRZefkxYVLXtgcEvKxJYE0JDUiq53Zm-bMPrJpxj9LjqzJfb0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7522060f48.mp4?token=VyJutoiEJxkYIN56nz22NJPUHLT8OhiGdpPpSaAXVBqKv3fAbfXM8MTXpFa-_KKU-VLrm0fEOX04P_Yrommr5hmvzOtDhekBDtiHn632CCGczs3XtrPywdqIyM1ZRubSMeqGZklvu4rd2EVRQev18psSTNwZn892n3eCU76roi4AtFLO-Hl76DieniL_IrKO-bC4ApywItt_8Xb5zoj65tzVi6is9QwMJEiGHo20Pa0-yZXuyV_KtntEWTSYV2cOIZ1SQwbsoGk_Mc3nrh1Je14xuOesFLx8dqilBRZefkxYVLXtgcEvKxJYE0JDUiq53Zm-bMPrJpxj9LjqzJfb0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آتش‌سوزی کلیسا در خیابان بوشویک در بروکلین
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66527" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66526">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2baf2d277c.mp4?token=iQSu-onoZ1dCcXF-6-y7e9yPbcm52VNDj0UkdHbE2QUoLFecBAv4jicbTfSLS8IDeyQHl2lWcXRAgQ_K8Uw04MV2bkqWSgB0v7GWaz-V450XPCOdXfrpu_blxZsxyRGNDYl4jHCuntoOxkERSH2Hs48RrdsgaGoh6KoWESfn5_mR4xlKXOMIQwSX8qHUvqeNu84egUyPV_iXQ5FPFsynu89CMMkjk1eKwxtpDRYtq4kJwUsqDDYFyN93CmQv70Eyl1xtMa0GlHZ8Lwp0Jw6-_-SnwZpZ2hUYRLgHcEgVFEyly2PTk-fL1chNwXyl_tM5Z8qJ0bnk_ar_aYxfxp6Xtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2baf2d277c.mp4?token=iQSu-onoZ1dCcXF-6-y7e9yPbcm52VNDj0UkdHbE2QUoLFecBAv4jicbTfSLS8IDeyQHl2lWcXRAgQ_K8Uw04MV2bkqWSgB0v7GWaz-V450XPCOdXfrpu_blxZsxyRGNDYl4jHCuntoOxkERSH2Hs48RrdsgaGoh6KoWESfn5_mR4xlKXOMIQwSX8qHUvqeNu84egUyPV_iXQ5FPFsynu89CMMkjk1eKwxtpDRYtq4kJwUsqDDYFyN93CmQv70Eyl1xtMa0GlHZ8Lwp0Jw6-_-SnwZpZ2hUYRLgHcEgVFEyly2PTk-fL1chNwXyl_tM5Z8qJ0bnk_ar_aYxfxp6Xtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارک کاپوتو از اکسیوس:
این چه تغییر رژیمی است که‌ انجام داده اید؟ شما خامنه‌ای جونیور (جوان) را همچنان در ایران دارید.
پرزیدنت ترامپ: خامنه‌ای جونیور با پدر متفاوت است. آن‌ها افراد متفاوتی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66526" target="_blank">📅 22:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66525">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5016d97e5.mp4?token=O2mQD0rhMc4Do3ERrSnXKDenlelCAqBLVRG39NCH1ijOF4gkBdT_9_FRabghr2BV9o2Y_N8mGTmDN0RCE4i3Uro5tY5CXdjXWvO0HXxxTuHZJgBcXXYkZN_uEoTLoG0eETvGB-ZRcnvd7f9WcwCyZG3zAx0BHaRr6iOP7QvwVy4d6Q7vDRh5xoGl3nX3fYJJVIL_Ow8dluv2q9V3c1tmDF_iRZ-zrwx21psYVge-gRB2p3n7DYy9e0cGPWA-1dKG7q6h-48m7NGCTbhyDQrjxH6cXmwkYR6ahuelGuEcGhG3vj0Kv556ySbNcnbJITyX4zYnLooDLwJT9cZ_z3tkGwUIvjWWiXR2Q--HeEEpurNZn3Odk9QKp_UXAFAzY86bVMwuYtr2QCOiZxXw2kPAHcrZHsz3snrnLC8wONzaNeo0jrJOKcvWyDVM-0IFPXXbzGIB8GYXms-DQ7ZGBmUgniEalWz5rXxNjf0CiLHUc_KyJ8wqWHT1-E4BPoq6ly7BS9ZiIHPqx9dI9L9rEOs-bxzLTGbrDoVhMtpvfuS40EPa9ggND5TdxEo-kgjXYftiaivKCtNSDcxbWs8hfxB2Fyvz1Mkc11xGlt3S3Qc6OzovuepLSZd2BY-2xnp45WpzMe4Su9qqYoD9yIu-cdRJ1flhGvVh52cY-drkBkfxFpo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5016d97e5.mp4?token=O2mQD0rhMc4Do3ERrSnXKDenlelCAqBLVRG39NCH1ijOF4gkBdT_9_FRabghr2BV9o2Y_N8mGTmDN0RCE4i3Uro5tY5CXdjXWvO0HXxxTuHZJgBcXXYkZN_uEoTLoG0eETvGB-ZRcnvd7f9WcwCyZG3zAx0BHaRr6iOP7QvwVy4d6Q7vDRh5xoGl3nX3fYJJVIL_Ow8dluv2q9V3c1tmDF_iRZ-zrwx21psYVge-gRB2p3n7DYy9e0cGPWA-1dKG7q6h-48m7NGCTbhyDQrjxH6cXmwkYR6ahuelGuEcGhG3vj0Kv556ySbNcnbJITyX4zYnLooDLwJT9cZ_z3tkGwUIvjWWiXR2Q--HeEEpurNZn3Odk9QKp_UXAFAzY86bVMwuYtr2QCOiZxXw2kPAHcrZHsz3snrnLC8wONzaNeo0jrJOKcvWyDVM-0IFPXXbzGIB8GYXms-DQ7ZGBmUgniEalWz5rXxNjf0CiLHUc_KyJ8wqWHT1-E4BPoq6ly7BS9ZiIHPqx9dI9L9rEOs-bxzLTGbrDoVhMtpvfuS40EPa9ggND5TdxEo-kgjXYftiaivKCtNSDcxbWs8hfxB2Fyvz1Mkc11xGlt3S3Qc6OzovuepLSZd2BY-2xnp45WpzMe4Su9qqYoD9yIu-cdRJ1flhGvVh52cY-drkBkfxFpo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره مجتبی خامنه‌ای:
من آیت الله را کشتم و متأسفانه آیت الله دیگر را آزار دادم.
من او را ملاقات نکردم. من با او صحبت نکردم، اما مردم از او صحبت می کردند.
اما او شجاعت خاصی دارد زیرا به شدت مجروح شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66525" target="_blank">📅 22:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66524">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb514f4019.mp4?token=Vo2Zr_jnFpG_JUCFAenqvsZ_PA6loRXp--KNaZoST3ivXZns-wwtcRLO8fIMLXO05Fnkk3zeA3jzogcNQrQLxTRSWanSdHoP2s5yhPSTuy-rrol2jeHhp_mnO3IhNO-5S9Ta7rhPp_TeA2HDGAAuXPJCFhoY7N9-3lo7D1aR1pRJdzFuWxAyffujwTddM2URU30P-J00BZFZs3r36Zr2tBEvLNVrR3HiSrKuXi5OJTggua_gK0gowKXmP3Eh-MmPybd0rghE0e0g9WdZxM_qyfdo_Qa2Lcf3MYhu9fM_yU1rDKZw5UnKMeLGdC7TX4Y9YW1MH18NeIHB9Z9bkgk9mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb514f4019.mp4?token=Vo2Zr_jnFpG_JUCFAenqvsZ_PA6loRXp--KNaZoST3ivXZns-wwtcRLO8fIMLXO05Fnkk3zeA3jzogcNQrQLxTRSWanSdHoP2s5yhPSTuy-rrol2jeHhp_mnO3IhNO-5S9Ta7rhPp_TeA2HDGAAuXPJCFhoY7N9-3lo7D1aR1pRJdzFuWxAyffujwTddM2URU30P-J00BZFZs3r36Zr2tBEvLNVrR3HiSrKuXi5OJTggua_gK0gowKXmP3Eh-MmPybd0rghE0e0g9WdZxM_qyfdo_Qa2Lcf3MYhu9fM_yU1rDKZw5UnKMeLGdC7TX4Y9YW1MH18NeIHB9Z9bkgk9mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره ایران:
این ایده که اماراتی‌ها قرار است یک میلیارد دلار برای ساخت نیروگاه در ایران سرمایه‌گذاری کنند، اگر ایرانی‌ها رفتار خود را تغییر نداده باشند، پوچ است.
آنها این کار را نخواهند کرد. ما اجازه این کار را نخواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66524" target="_blank">📅 22:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66523">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9895e96f.mp4?token=i2svOUt6VpU_8-VeCnvwf0bhyVB6Te1tgdVeqFSNZq7X-F_35KPorM0eNbz-HHOdDZQ0mK4HjGJTFaAXqyvX2IK7W5xj1dRj3_oGcBUI2ZZ0F9NbkDOz38E_3aIQ80XjXxQE0-1Y4XQFMZ54zgypjFird7L0M1x0iazvieX71-IDQ9oSIz9M_q8uaSn1ZW8VS1SGkJPXgsy4BhZEBtU7f0FJfMzniCCcpLGUAZCPVa3e-RA2s4o6pENcbhoz5pFp5xDO6f1wrJw9UfvQa8yvhRCSH-6NCnhDcuqDrAHDyGeqFFeAkeKKyzUpjrU4c78lyzx420R4a-fWw3FUYk6t2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9895e96f.mp4?token=i2svOUt6VpU_8-VeCnvwf0bhyVB6Te1tgdVeqFSNZq7X-F_35KPorM0eNbz-HHOdDZQ0mK4HjGJTFaAXqyvX2IK7W5xj1dRj3_oGcBUI2ZZ0F9NbkDOz38E_3aIQ80XjXxQE0-1Y4XQFMZ54zgypjFird7L0M1x0iazvieX71-IDQ9oSIz9M_q8uaSn1ZW8VS1SGkJPXgsy4BhZEBtU7f0FJfMzniCCcpLGUAZCPVa3e-RA2s4o6pENcbhoz5pFp5xDO6f1wrJw9UfvQa8yvhRCSH-6NCnhDcuqDrAHDyGeqFFeAkeKKyzUpjrU4c78lyzx420R4a-fWw3FUYk6t2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏پیشنهاد جی‌دی‌ونس به ایران:
گزینه الف این است که شما همچنان مانند یک رژیم تروریستی رفتار کنید، که در این صورت به معنای واقعی کلمه هیچ چیزی به دست نمی‌آورید.
گزینه ب این است که شما مانند یک رژیم عادی رفتار کنید، و ایالات متحده، به عنوان مثال، اگر قطری‌ها یا اماراتی‌ها می‌خواستند در کشور شما سرمایه‌گذاری کنند، در واقع به آنها اجازه می‌داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66523" target="_blank">📅 22:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66522">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f005383e.mp4?token=dXdcKYuMKKrJsg33ExATO6INld_EHKKnLCTXb7C-JDesXwCXoF8UevIanhBo9GzTUzZiKuM5hrSrO3ROsBNlS4gL_05AIwb4ehtlwMz_M45MPKEPcc8uIa62XAqMEz-tHyD55LS5Xpr_uw6HeWTQ-y9W8lsT6V471VfKmAiqipDYtEv7QYy4fH_rNGme79jADfZXdSYT_OMscuz60719sV2Qcff6UY1HTAZlex175XdAn4tAH9NfNMp039Fgnxp_QThYEd0_f-klPK6tUoNk8QSENnromuZd3D7b0UXzlu1l8N1hlo7v_yzbeLes07DgosR2Nrsy9KVuKk7hCzRIbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f005383e.mp4?token=dXdcKYuMKKrJsg33ExATO6INld_EHKKnLCTXb7C-JDesXwCXoF8UevIanhBo9GzTUzZiKuM5hrSrO3ROsBNlS4gL_05AIwb4ehtlwMz_M45MPKEPcc8uIa62XAqMEz-tHyD55LS5Xpr_uw6HeWTQ-y9W8lsT6V471VfKmAiqipDYtEv7QYy4fH_rNGme79jADfZXdSYT_OMscuz60719sV2Qcff6UY1HTAZlex175XdAn4tAH9NfNMp039Fgnxp_QThYEd0_f-klPK6tUoNk8QSENnromuZd3D7b0UXzlu1l8N1hlo7v_yzbeLes07DgosR2Nrsy9KVuKk7hCzRIbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی ونس درباره اسرائیل:
من از تصمیم ترامپ برای پایان دادن به توافق ایران دفاع کرده‌ام و اغلب متوجه شده‌ام که استدلال‌ها این است که «اسرائیل فکر نمی‌کند این خوب است، بنابراین بد است.»
واکنش من این است: نظرات اسرائیل مهم است، اما اساساً آنها از هم جدا هستند
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66522" target="_blank">📅 21:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66521">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ebdd0a4c.mp4?token=PmPHF_8ZQKUH_p5LB0P7AvKnSGSQ94zfUjwtK9gROlKlQStbzmHS0StFR7KMFLKjG9fJvWybmLFM_io2EroYWRLudcoQNi6phr8FCzNUDq3RQsoRUYjzP-dfxdDHuxShbVucnhGQFh8mTHJ7Fq314UVpM-vcT2CbDwQfP7tfADHJrJdgAZLOPtNQlNVV_Zx8tG_YzMs1EhFa6l0otYSWi9AOeazeEXMvZdiEORbt1tkq6Cfi2AmqM9TrbLUJxs1lqJDGAx_JwVCMHiRbZqy5hZbHmb5HbRi5RCIat_m_X5hgT0aJtPHkc6TAF5MGd9hBtPY92NWpoM15sLXEsOAMxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ebdd0a4c.mp4?token=PmPHF_8ZQKUH_p5LB0P7AvKnSGSQ94zfUjwtK9gROlKlQStbzmHS0StFR7KMFLKjG9fJvWybmLFM_io2EroYWRLudcoQNi6phr8FCzNUDq3RQsoRUYjzP-dfxdDHuxShbVucnhGQFh8mTHJ7Fq314UVpM-vcT2CbDwQfP7tfADHJrJdgAZLOPtNQlNVV_Zx8tG_YzMs1EhFa6l0otYSWi9AOeazeEXMvZdiEORbt1tkq6Cfi2AmqM9TrbLUJxs1lqJDGAx_JwVCMHiRbZqy5hZbHmb5HbRi5RCIat_m_X5hgT0aJtPHkc6TAF5MGd9hBtPY92NWpoM15sLXEsOAMxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره اسرائیل:
اسرائیل شریک خوبی است، همانطور که بریتانیا یا فرانسه شرکای خوبی هستند.
این بدان معنا نیست که ما همیشه منافع همسو خواهیم داشت
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66521" target="_blank">📅 21:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66520">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c3443a503.mp4?token=Qp6yrrcTp5U_w4RLex7ES4si8TxWQg4QvdruuRmMRVfLVjV_nYKFN5h_nErMN1RYggUg4-4C6a2kvhlESlAI1w_fnuWvZT4Wiueb_Pqwl8mCeZjj4SBYafyW-ddMDuKexWzNrdNX5lKc0jZ8nkX2H02k4Hzw--EII1flSXs9HSBF74B7iEhQoAHU673X2g6wwquOMfWZ6L2_UwDK_Chcm7Z4ubxLc17m4cfl--sOdmdpkIDRKW6_oNQktoZophOjgJewY_QWbBZwWD6zocCbdNlMlDkMv7yJMNwsSIGJ1uzJKb4-LgOwgRMkFUYovAu1_swSTkOdZdVH3sAJR04kZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c3443a503.mp4?token=Qp6yrrcTp5U_w4RLex7ES4si8TxWQg4QvdruuRmMRVfLVjV_nYKFN5h_nErMN1RYggUg4-4C6a2kvhlESlAI1w_fnuWvZT4Wiueb_Pqwl8mCeZjj4SBYafyW-ddMDuKexWzNrdNX5lKc0jZ8nkX2H02k4Hzw--EII1flSXs9HSBF74B7iEhQoAHU673X2g6wwquOMfWZ6L2_UwDK_Chcm7Z4ubxLc17m4cfl--sOdmdpkIDRKW6_oNQktoZophOjgJewY_QWbBZwWD6zocCbdNlMlDkMv7yJMNwsSIGJ1uzJKb4-LgOwgRMkFUYovAu1_swSTkOdZdVH3sAJR04kZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی ونس درباره ایران:
باز کردن تنگه هرمز دلیل کاهش قیمت نفت از اوج ۱۲۶ دلار به حدود ۷۵ دلار در امروز است.
و همچنین به همین دلیل است که قیمت بنزین، اکنون که ما صحبت می‌کنیم، برای اولین بار از ماه مارس، با وجود افزایش به میانگین حدود ۴.۶۰ دلار، به زیر ۴ دلار رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66520" target="_blank">📅 21:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66519">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUX7iBPvPHY6lWOR-KUbMQdyEehmXt47H9DdA5cVLxn82_-Bh_GslB2QBy_L1PeG7JFT2zidNMLmo0FUHFT5rqjXv_ckeynV69mt54fW9gMrtJ6pntpsy1STtz6cTFDhrvylT0kymIa0592UI4pxgOqryOR_ABnORPyfHL04J9JFzzW3kenOg_ExtHa8ry-0hB_5zmxtgcfIDxXn5fIwPnkbYOk3aWPfC3spaf_GyRSlnODYWIqTaqctY-uW0s4wOk4OZOtnAZmzPIUBbKwpoOBKVuNiSdl8I1QeVHw64A8SHxkMb3GJQI7bkPxbwgEMo8xoxqVDOfggrEInpgy94Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هیئت قطری رفته سوئیس ولی ایران و آمریکا نرفتن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66519" target="_blank">📅 21:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66518">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BH3SOOli3d1_sgjEVOmK6PPMePR1hARyqINV31VHhzVqkKzFaJ_XMgkeGSjEIyVOI_5Vs4r0aMcSxX2jzB_2_xCSM-z3u_BrrWaPnsaPhlvOunNvQWJ49LMd3mnJRKvfT5uHBzUJ1ry2-q-ck_4MOYVu4JWhodSzI5t4U9yQruGiYGqsH0pRJAg7eDP2E_vcQkMWkVLbXnN-fyhINbAMozj7iaN5dWU7L3WhW3lSr61egsI5GxVtlmFEfulAkUZ9e5ASGYvoUqs9FgrcApVELYEHRqTY6Aqx0hXWkRUz-K_9iDH2DrLg2tXlHimCZJq2lW2ks1bi2VigZJ5HyxwYGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌پست:
آمریکا ادعای «مزخرف» مبنی بر اینکه امارات متحده عربی - یا هر کشور دیگری - دارایی‌های مسدود شده ایران را آزاد کرده است، رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66518" target="_blank">📅 21:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66517">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNgZ9HBxj79ye60u9nMRf52a_gqF9bHApZp8IaD-308_bkifGy9NH0lVkyvht7g_elAJm6KktyPQfqM1HmOTBQl5g0HxWferz46ZPQH-zFz7kNEDNFQZ482VW3QrHL9Hd0-ro8scEByL0Jc8TTbJq9AZk0-WqK8AoZGf5m0RqOkIdPUaczO4x3gwxKOk0ox_miXjw9t3SuekiE-Pke-0sQIPYVs3tQE8-jxYqDuEoYH0fdpjVZbptAfYwqTMZDO6LN4BxN-nDV2kh1dG_O2mM7SDuMJbn9FwmaQ0SzU5xwELl2qpxpJjFKNFdci7BXd7ew4DQgHiKwiuBDYImEWoow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان‌های اطلاعاتی ایالات متحده به دولت ترامپ هشدار دادند که نتانیاهو احتمالاً اقداماتی انجام خواهد داد که می‌تواند توافق صلح جدید ایالات متحده و ایران را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66517" target="_blank">📅 20:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66516">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700e55c3c3.mp4?token=kqT9h1wVmWwh5UGrbhBkA1difQo_7nucZoYUByrhEeVCcjfwu8QKsfS-xBIcm67uZvlgTWp0VlTJRcOE5tWiAoJVxxY41tmo-mzDd-HOSImL5XWYPqMRYtvtDkXAXdtW8gBoxhc_gfBXkZqZa9CiN9xZnXpP8-tzo5Ms76f2HFcH-DewJTmDuYXGJtYzF9pE-CoHCE3w3_hZCEHRDFwbQzhDg6FJRubHTMB7J6ITI5cKWDOJGKtsVc_9pF_8BjDjflr2CAODwvVQJXGqMUSYkrtjCWrQWQIjhwywhO_rhqRvvoHC1lVXEyXP5qO7tmZfx6ZckYJ5LUdbY_Azy_7Jew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700e55c3c3.mp4?token=kqT9h1wVmWwh5UGrbhBkA1difQo_7nucZoYUByrhEeVCcjfwu8QKsfS-xBIcm67uZvlgTWp0VlTJRcOE5tWiAoJVxxY41tmo-mzDd-HOSImL5XWYPqMRYtvtDkXAXdtW8gBoxhc_gfBXkZqZa9CiN9xZnXpP8-tzo5Ms76f2HFcH-DewJTmDuYXGJtYzF9pE-CoHCE3w3_hZCEHRDFwbQzhDg6FJRubHTMB7J6ITI5cKWDOJGKtsVc_9pF_8BjDjflr2CAODwvVQJXGqMUSYkrtjCWrQWQIjhwywhO_rhqRvvoHC1lVXEyXP5qO7tmZfx6ZckYJ5LUdbY_Azy_7Jew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم، دبیر کل حزب‌الله:
امروز در لبنان، ما با خطرناک‌ترین مرحله تاریخ خود و بزرگترین توطئه مشترک آمریکایی، اسرائیلی و بین‌المللی روبرو هستیم که آینده کشور و فرزندانمان را تهدید می‌کند.
هدف اصلی این طرح، ریشه‌کن کردن و حذف کامل مقاومت و پایگاه مردمی آن در لبنان است.
دشمنان برای دستیابی به این هدف، ابتدا جنگی جنایتکارانه و بی‌حد و حصر را آغاز کردند و با کشتار غیرنظامیان و تخریب گسترده، مقاومت را به زانو درآوردند.
در گام بعدی، ایالات متحده و رژیم صهیونیستی پس از مشاهده تغییرات در معادلات منطقه‌ای پس از تحولات سوریه، توافقات قبلی را نقض کردند تا موازنه قدرت را به نفع خود تغییر دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66516" target="_blank">📅 20:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66515">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46f332c84e.mp4?token=HZ1ny79WqXqadHQO4GvfGtzVm6bgX_OnjJRYCUfF_013AZv7x5DJocAgcYlbZG27550_XD9whCpas-iT78wDa_sdUaU-_ZlcFtM5KL9xQp1nWBLUPC_nsVJdamwDbQ5mMwdDjT4pXZOEXkDppNdOxraFa8FHNRRXGSo-MEDiNpfpt7ZuELtQaVCJuT8mvgP8-atIZO2NTLuTqUzS7FNPbVsNNbwXtGTleWMgqx_aI8R-79Jd8o9CC9dYdYpTcGwL5KpyOGKtibGlYVRxLfTfTTlWQoalHAK7LwLemaGFeIouy-EtX0pe6e8AeIC7pWv6yMm7tNvDHHouHgrHVYX2OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46f332c84e.mp4?token=HZ1ny79WqXqadHQO4GvfGtzVm6bgX_OnjJRYCUfF_013AZv7x5DJocAgcYlbZG27550_XD9whCpas-iT78wDa_sdUaU-_ZlcFtM5KL9xQp1nWBLUPC_nsVJdamwDbQ5mMwdDjT4pXZOEXkDppNdOxraFa8FHNRRXGSo-MEDiNpfpt7ZuELtQaVCJuT8mvgP8-atIZO2NTLuTqUzS7FNPbVsNNbwXtGTleWMgqx_aI8R-79Jd8o9CC9dYdYpTcGwL5KpyOGKtibGlYVRxLfTfTTlWQoalHAK7LwLemaGFeIouy-EtX0pe6e8AeIC7pWv6yMm7tNvDHHouHgrHVYX2OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم دبیر کل حزب‌الله:
پروژه نابودی حزب‌الله شکست خورده است، نقشه‌های اسرائیل به بن‌بست رسیده است و پیروزی نهایی، یعنی اخراج کامل و قطعی اشغالگران از هر وجب از خاک لبنان اجتناب‌ناپذیر است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66515" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66514">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66514" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66514" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66513">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66513" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66512">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
نعیم قاسم، دبیرکل حزب‌الله لبنان:«تا زمانی که توان ایستادگی داریم، چرا باید تسلیم شویم؟.»
حزب‌الله خلع سلاح نخواهد شد. این سلاح‌ها برای مقابله با اسرائیل هستند.ما تصمیمی «به سبک کربلا» گرفتیم و این تصمیم همچنان به قوت خود باقی است.
«ما وحدت نیروهای مقاومت را حفظ کرده‌ایم و وحدت جنبش امل، حزب‌الله و سایر نیروها همچنان در کنار ما برقرار است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66512" target="_blank">📅 19:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66511">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3cm7cKiCFu7D1PcgLtfiKSliuHQK_EgoAHtRxyQvdMi0veA5tdO6xn8Ov7iJXPCQa3GssMEAhJBmVbH0ifrghm5_TTR4XEfGdf-hIpd__fnKFSUzvRXmP6ziQultUvQ4VYq_rwk0JzSdf0zjNuFiAfuXCrcWoGLK4og2TDij1KWM7-jtZ-TF2EtwhQwvFRqOFm4hQOhjroP-sgkRGA4RwLQwsP7PQYEAz6jUmZJ5miTSf64mcOn0qeFsvXsDNtjZ4Noxf28V0dDanGixDi576gKKeTJXww7baaEG0vLATCS1J6VBN8fTJvhhI9b-A-hosZ50AztWbqHmIiernR9GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اتاق جنگ اسرائیل:
رژیم تروریستی ایران از نیروی نیابتی خود، حزب‌الله، برای حمله به اسرائیل استفاده می‌کند، به این امید که بتواند وقتی اسرائیل پاسخ می‌دهد، اسرائیل را به خاطر از مسیر خارج کردن مذاکرات سرزنش کند.
ایالات متحده باید به حمایت از حق اسرائیل برای دفاع از خود در برابر رژیم نسل‌کش ایران و نیروهای نیابتی آن ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66511" target="_blank">📅 19:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66510">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0ea7af18.mp4?token=viz_1M9ytgh0kr6xlmhZQZ4Bbc521TWdAUWOOz9BqIEa4mC_av91j4T2BwiV_Du1P-j5grOlBpR33-9PLgd2w4rlW8gb5x2QXL7SWQaLBiKxj2wfUBdIuFQP3UNaC_qwWxDpGXiN3S-TOkpJG4Idb9s9pxD6BPlorhjlbzQgtNis3euiiQYRUS5UN77VD7qvNol4wsWlTvQGl-IVDgOVhsQS_gvsquY1oWG58BJM4SJI5hnQkW8qZxFhT-unoi2praRfMUmt7P42UMaM4l_a73-ShTRidxJeh9yTQm_uXWWIgrxX2GBGKz3pXlLfhCHIMEop5LWfRSQPnzy4zcUmog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0ea7af18.mp4?token=viz_1M9ytgh0kr6xlmhZQZ4Bbc521TWdAUWOOz9BqIEa4mC_av91j4T2BwiV_Du1P-j5grOlBpR33-9PLgd2w4rlW8gb5x2QXL7SWQaLBiKxj2wfUBdIuFQP3UNaC_qwWxDpGXiN3S-TOkpJG4Idb9s9pxD6BPlorhjlbzQgtNis3euiiQYRUS5UN77VD7qvNol4wsWlTvQGl-IVDgOVhsQS_gvsquY1oWG58BJM4SJI5hnQkW8qZxFhT-unoi2praRfMUmt7P42UMaM4l_a73-ShTRidxJeh9yTQm_uXWWIgrxX2GBGKz3pXlLfhCHIMEop5LWfRSQPnzy4zcUmog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
«هر مشکلی در خاورمیانه مستقیماً به ایران برمی‌گردد. حزب‌الله؟ ایران. شبه‌نظامیان شیعه که عراق را نابود و تهدید می‌کنند؟ ایران. حماس؟ ایران. حوثی‌ها؟ ایران. اسد که در سوریه مردم را قتل عام می‌کند؟ ایران. این رژیم هزاران هزار نفر را کشته است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66510" target="_blank">📅 19:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66509">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWNOCFMTDejrQSdUNHxolOj0vQwVUzHaUFzCdeojSghHY4XG1Y2uudS7fL0ib2SJQLqOafuOOmfPb9HDnDlL00MC3zZcGqKrbeS7PcgVjGvQ1-VZEVI5IxYYaXgdPx2B7XUYzzBy2KBCQOxK2x6efT9gVvwlpPl71MmEd1Mi2AYARicGZi3mW6uwzueMSTdcAO3Dcgn48O7fJojE3HS6LnpvhFoL0zbPotzF3bXkVmF-KDMy8ivmnK7JWCacffjPKdgO05oxGEi7k4PulFAgf-Q-3Xs12waKRrTDwRNUTGkEX6ngi7txr10rcB2UFU6oZbytvg4rEGyaO40crO9eVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اسرائیل هیوم به ترامپ:
می‌تونستی بزرگ‌ترین رئیس‌جمهور تاریخ باشی، اما شکست خوردی
شما به منافع جهان متمدن ضربه زدی و ممکنه به‌عنوان رئیس‌جمهوری در یادها بمانی که باعث تحقیر آمریکا شد
به اسرائیل خیانت کردی و حالا تمام تحقیرهایی که قبلا باهاش روبه‌رو بودی، کاملا موجه به نظر می‌رسد
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66509" target="_blank">📅 18:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66508">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ:
ما از روی استیصال پای میز مذاکره نرفته ایم.این ایران بود که از سر استیصال آمد. کارشان تمام شده است!
ما این دوره ۶۰ روزه را تا آخر پیش می‌بریم. آن‌ها هیچ پولی دریافت نخواهند کرد؛ حتی یک سنت هم نه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66508" target="_blank">📅 18:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66507">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c09804d09.mp4?token=DzKC913AsN6IIJ9iCFVxhJBoamRoD7joF44wAEJA5FLmkHf5-Wtwdpw3_1pfBHZXHh7PoNEp6fZ_SCqFpvq4cjaeN84zML2DcqQDGJW5I-580CGMWh7KnNKryfpKnOjtUox5Zr_rANX7klQKgimZAHPPxMH50xwFCTBbugGCSuPdRJYcsBGH5G4tcPW1GU_D18WBJGQBTV2RZn5xa9i3TD6e2NbwBN0o3fqjEUy_ymiHQFiusDyaqc8VzUNX57R9Qux3M6MzVMG01X1Ct8iOKIb--P-6q7iA308kk0iG7B7ct5KS1RydL6U1ZouYe-7Ez6y30mLhIr60cylUWHYvOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c09804d09.mp4?token=DzKC913AsN6IIJ9iCFVxhJBoamRoD7joF44wAEJA5FLmkHf5-Wtwdpw3_1pfBHZXHh7PoNEp6fZ_SCqFpvq4cjaeN84zML2DcqQDGJW5I-580CGMWh7KnNKryfpKnOjtUox5Zr_rANX7klQKgimZAHPPxMH50xwFCTBbugGCSuPdRJYcsBGH5G4tcPW1GU_D18WBJGQBTV2RZn5xa9i3TD6e2NbwBN0o3fqjEUy_ymiHQFiusDyaqc8VzUNX57R9Qux3M6MzVMG01X1Ct8iOKIb--P-6q7iA308kk0iG7B7ct5KS1RydL6U1ZouYe-7Ez6y30mLhIr60cylUWHYvOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
همانطور که دستور دادم، ارتش اسرائیل با قدرت به ۱۵۰ هدف حزب‌الله در لبنان حمله کرد و ده‌ها تروریست را از بین برد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66507" target="_blank">📅 18:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66506">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">Live Tennis</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66506" target="_blank">📅 18:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66505">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faa1be6643.mp4?token=TW2Q8nU9Hd3vDQqsZFK2EiTauOux88CAX5fg9kyCxDVOFAjOr81C6s0ano0H5Ul-uwAyI3KUQ9K2_gnj1FSrweiYehMwmYXURKbR97A91mfxJ1-SvfIjWU5H4Q6pH8dp4CM-AHsmfVlhd0kTRsc3go5XpDryAFvkQTQ3_z2LppYriAEsxeFeFyL_o50tx4ytA3zf70p3YTcmWiCgkrxLibBK366kSDETJsq4zhx9sLGZEaVwlyUGrRAoiGeoigMWCYJA9xSvv2ZyR5ej8mvX_b-s5uzlex7MhtRhy-XD7tzsdTXUdkzGXcQfEi_-FJG63jPNeAYh92aj3xUiqvZpQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faa1be6643.mp4?token=TW2Q8nU9Hd3vDQqsZFK2EiTauOux88CAX5fg9kyCxDVOFAjOr81C6s0ano0H5Ul-uwAyI3KUQ9K2_gnj1FSrweiYehMwmYXURKbR97A91mfxJ1-SvfIjWU5H4Q6pH8dp4CM-AHsmfVlhd0kTRsc3go5XpDryAFvkQTQ3_z2LppYriAEsxeFeFyL_o50tx4ytA3zf70p3YTcmWiCgkrxLibBK366kSDETJsq4zhx9sLGZEaVwlyUGrRAoiGeoigMWCYJA9xSvv2ZyR5ej8mvX_b-s5uzlex7MhtRhy-XD7tzsdTXUdkzGXcQfEi_-FJG63jPNeAYh92aj3xUiqvZpQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محکم تر بززززن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66505" target="_blank">📅 18:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66504">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4b87f1a5b.mp4?token=TE5u96v3HGrL-UdRTgoa4Sa8uDHEZQDMj-rKQ6bfV1VS2T6TR-LTd5UJCadsVBrul-Jv9UiDwOrcvNrNOH6kn3ud2ZjuTHa6D_eQi_4WJNe2wbXDtR32cpO6x5nyr5tA2WclW9M4sZDDkvBBeO4WYkPUwaWBOcPiH5oQk6pzZt7VWHopsfcWP43y17uWqIYjve3D8gFVDPMxcn_VrFH8ZB9dZhmhJUGa7sLzQYqg5Bxw2qus4nWa-Ldk91D1ja5Yzfsm18HyZ50ywOfp9z7wIfeIw8P4sJubzcDXXDEMfR7tpeOorrevO8KohtHEWB7yZMUb5u7YWABVs9y9Mq1ykQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4b87f1a5b.mp4?token=TE5u96v3HGrL-UdRTgoa4Sa8uDHEZQDMj-rKQ6bfV1VS2T6TR-LTd5UJCadsVBrul-Jv9UiDwOrcvNrNOH6kn3ud2ZjuTHa6D_eQi_4WJNe2wbXDtR32cpO6x5nyr5tA2WclW9M4sZDDkvBBeO4WYkPUwaWBOcPiH5oQk6pzZt7VWHopsfcWP43y17uWqIYjve3D8gFVDPMxcn_VrFH8ZB9dZhmhJUGa7sLzQYqg5Bxw2qus4nWa-Ldk91D1ja5Yzfsm18HyZ50ywOfp9z7wIfeIw8P4sJubzcDXXDEMfR7tpeOorrevO8KohtHEWB7yZMUb5u7YWABVs9y9Mq1ykQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از لحظه سوخت‌گیری جت های جنگنده F16در حین انجام عملیات گشت زنی بر فراز خاورمیانه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66504" target="_blank">📅 17:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66503">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3273d3f5c.mp4?token=qlr0DkpSK8c2QsWsId5Bq0gWWoOhc6kbMG3_zZTRSFEfjPpZMnxfPr6NwlV-DJHbw70c5tsuc7Ny_Zyi99A6t7uJfaIgGZOrI-WiDgFBW43YNsuQaoH0v_CABACXfUyin4RwlmV7PDpWwajck_4inwa0w2Vl1qnsSMGYdijjca2FXL9UN-mwCr-OkrtRhaa7m8sDuc_7ZDOsWcEXDslsfD7tnagycMTo2QTzGLLWN1y3fTuqZTJ9T_aOQMcVaR0X9DPMl3gzvs1LX42mShJ0n395qAODRMPq-CFEww4xeME9Mxl1pk7w2HJ-3iyFoXrl-cXhqk8FVB0lVNalxeUstg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3273d3f5c.mp4?token=qlr0DkpSK8c2QsWsId5Bq0gWWoOhc6kbMG3_zZTRSFEfjPpZMnxfPr6NwlV-DJHbw70c5tsuc7Ny_Zyi99A6t7uJfaIgGZOrI-WiDgFBW43YNsuQaoH0v_CABACXfUyin4RwlmV7PDpWwajck_4inwa0w2Vl1qnsSMGYdijjca2FXL9UN-mwCr-OkrtRhaa7m8sDuc_7ZDOsWcEXDslsfD7tnagycMTo2QTzGLLWN1y3fTuqZTJ9T_aOQMcVaR0X9DPMl3gzvs1LX42mShJ0n395qAODRMPq-CFEww4xeME9Mxl1pk7w2HJ-3iyFoXrl-cXhqk8FVB0lVNalxeUstg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ بعد از نشست G7 پشت سر جرجیا ملونی نخست وزیر ایتالیا گفته:
این زن همش التماس میکرد باهاش عکس بگیرم. حالا جرجیا در جوابش گفته:دروغه، شوکه شده‌‌م. نمی‌دونم چرا ترامپ با متحدانش این‌طور رفتار می‌کنه؟
ولی یک چیز رو به خاطر داشته باش: من و ایتالیا هرگز التماس نمی‌کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66503" target="_blank">📅 17:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66502">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
سخنگوی ارتش اسرائیل:
منطقه امنیتی در جنوب لبنان ۱۰ کیلومتر امتداد دارد و ما به تقویت نیروهای خود در آنجا ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66502" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66501">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLlVRqQvrk_QNtiN2qrZN6xpk2KDtvXO8y1m2dsrlY698XrSZUoE-Kxu-hySPK9YqYdlk3Hpc3-p0T9THN3uqL00BRA0vvH_YMN2poC8ZOdAPwSxE459NX-vSPljvm15q6xhicz6jmrxhU5_uKVrnzpntP8zmpmwtXUfC-mMCbHL7P2alukOqdKyYUoU-BWkkx8YYvqRczAlmDSlagdhD_bI72iq7qgP0Smklt6ZHU8GsyVGJtQb5webT3EHLwLLHm38i8Esugzfc6T4KTULCA6hwn3XzsC6p0FshfsUOCDdT_aZbt0ls38rP6Px16lgVmKRugMf24sAv02jBWhx7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اتاق جنگ اسرائیل:
اسرائیل و حزب‌الله به توافق آتش‌بس جدیدی دست یافته‌اند. حزب‌الله از توقف بمباران اسرائیل و پایبندی به توافق‌های آتش‌بس قبلی خودداری کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66501" target="_blank">📅 16:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66500">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryqkUZW7gOQTQB42rCtz3hxOiH5SiP9fG5V0JK9qg7jNhd2YxxlAo4Uf3L0dZVxWD-CM1X08BM9py5WkEfpDAjyVd9q_9GldIP7LuEzcVxM_3eqgKOzcFiC5zfiKDwo62KggtS4DOVVdR5e0gdpCMYAffg4I3bQD64N4FJSXum4yjC8uhrpLaaIbkreG95uQFD9N1TM_Ua1WBtKDKRFfmLbmhojPraSZSWA47miDKcT_dgcuRF_MHOIYEGBD0FozrLoZAGEj97q04q6x93gCXfB72tPWlvPx2oIchH40oCJiqjf8Ej4ALtGVQFv5R93uhRRdLbu4uhzaGP2_I5wedA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:
یک مقام ارشد آمریکایی به من گفت: اسرائیل و حزب‌الله بر سر آتش‌بس مجدد از ساعت ۴ بعد از ظهر به وقت اسرائیل توافق کرده‌اند. این توافق جدید با میانجیگری آمریکا و قطر پس از مذاکرات با اسرائیل و ایران حاصل شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66500" target="_blank">📅 16:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66499">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MoNcSLYmcZC5nYNijid4HYJOHuyulGAyVNDjQCoE3F-qDPoREVLsrw3Z6rhy32205pc2WN4WgTwFzR2yQpAc95zFCbXmaV95Mn1ZTYzX6Eq2TC61xcrGZ0NZNsCVB5kY7uYQ-nGlHF4A5EQ9qNRagcy14o_0-7ofjjNWQy0q6nogCGvI7BN5JN8qf9CHhvKSwPwlJU7zQuvwskBOwEXeFMOREuDRTrfsVDnlZKGgqbFlh3povc-S7PMHuTvoRfLQPMu6DNNd7waB4a-CUXLJjPM0mRo9zy9Jf4Evt-9x_BJW2GGO2hUiDWM1MSFLQ0anW1RJNHFeUzg0ujwCCi4zCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما از روی ناچاری ملاقات نکردیم، ایران این کار را کرد. آنها کارشان تمام است! ما 60 روز را بازی خواهیم کرد. آنها نه پولی می‌گیرند، نه ده سنت!
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66499" target="_blank">📅 16:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66498">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEX-Jp0RnAhyH3F5hSew4IOl_93BvPKrYFoXNAZguEATnEK32QDwZE4o7EIN4QWoDewJVi32so63ICRX4iK27lSv1adVkOs-6H6959yNACPkZw2K7GjclqTZXCmjfTUBjCyhlQ1bsYGxP-Lr6nEqXigZnCDTJdip0HSdf8tof4dsxW4SVnCYi9YwwHFKDokQUZPSRzZo03dfsWJ64R6TL0Lga0doQJktd_iQ00b94t75cssFX5D9DtKoihGXRVtiolNdFNRcmSnTCjZAZzKLsGBXVjX3RqI_5bu7hUs9wiNE4DoV2hPyN-o_9yxC5O62yxr_v0aN_dxiE-tgycIwZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
این جنگ ایران را تضعیف کرده است! ایران دیگر نه نیروی هوایی دارد، نه نیروی دریایی، نه تجهیزات پدافند هوایی، نه رادار، و تقریباً هیچ چیز دیگری. با این حال، دموکرات‌ها می‌گویند ایران اکنون نسبت به چهار ماه پیش وضعیت بهتری دارد.
می‌توانید تصور کنید که کسی چنین حرفی بزند و از آن جان سالم به در ببرد؟ بعضی‌ها واقعاً تا چه حد می‌توانند احمق باشند؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66498" target="_blank">📅 16:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66497">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
‏اسماعیل بقایی سخنگوی وزارت خارجه:
آمریکا مسئول حملات اسرائیل به لبنان است. جمهوری اسلامی همه تدابیر لازم را برای صیانت از منافع، امنیت و حقوق خود و متحدانش اتخاذ می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66497" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66496">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgsK1SfmoSLbHAq8xd9oeusfmJpa_vebW_qrHgxWe6hTDZkma_eMjqkHQttbHfSaZ5fjw2oGifKnA5KdMAw_FrgBF_m1jDfOqHsBCCENV7bHbt2cq-c8D6I6f2wHwIE79vL9JJdkFTCHQWyR8HWqAkczB57A0D5Y_bGrRlxtS-JvTIMHTkUuh4xyB6bnMLwvCo0qjwuqsEcwuTRIPjezRc1_EMC4DiyhRek60XZl4wJmvOgUz4mphmMFzpdPdQ3tQwueaBhAp-jzcMecYGOsaR3lZuMi2UgUXgf38pp8yYKkqYCbNwcXtOvGWlBbjm99I3VLp9I0AMUcdooXUCimjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اینفوگرافی خدمات فعال‌شده پس از رفع اختلال فنی</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66496" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66495">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec2c7bdfe.mp4?token=lxko11YaaWo4oPo3nCYYvxZu2F3szfSkQIMoPc3NbmKlKwPXnMHwF1qQ_zzlPH98Sn6ymUo-QyJA-BH9pEvYuh3vSO1wm1apfXXK3GqaREZ2r9ZXeSvs7kVdRLwQBbEAPrrVoJ41FPhLYsYA-gZam36SOBgriq8iADQZX5RCBxSIqbQ68pdtkghhAb_Cl2fpFrfnfVy17hP5m6Ev9LZ7TejfkiOvPyaGNclFMqF0FPjDWXl6OxSxlKmVReKGLaAqYk44Xrq-V-nzfEobqqW086RBFpzyLK4HgQ8ZD6eufBVt0GeL4hsCksC0feIL1j4QFjjX2J3Qvf0GKAY0-Oxd_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec2c7bdfe.mp4?token=lxko11YaaWo4oPo3nCYYvxZu2F3szfSkQIMoPc3NbmKlKwPXnMHwF1qQ_zzlPH98Sn6ymUo-QyJA-BH9pEvYuh3vSO1wm1apfXXK3GqaREZ2r9ZXeSvs7kVdRLwQBbEAPrrVoJ41FPhLYsYA-gZam36SOBgriq8iADQZX5RCBxSIqbQ68pdtkghhAb_Cl2fpFrfnfVy17hP5m6Ev9LZ7TejfkiOvPyaGNclFMqF0FPjDWXl6OxSxlKmVReKGLaAqYk44Xrq-V-nzfEobqqW086RBFpzyLK4HgQ8ZD6eufBVt0GeL4hsCksC0feIL1j4QFjjX2J3Qvf0GKAY0-Oxd_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران شهر نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66495" target="_blank">📅 15:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66494">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f017f858a.mp4?token=d-u2j8awWm_m_0lHbty6fyAe2urrN1i4H17O4us5l7ij23pxtiHIbm-OzBXSaKrupRLc_ccdX5j4U-NiLdNZsKJzdwBfD6qo2PoHP5vmQkbVgTrqRxDIedL62lymFq_sbx5BKNJ8HVZQ3vwrVm6Ur3tSnq7Cis6COU2QoUkq3q5pV_RZ9imX-sPi-Aikb1Ucb_vmT1Wa_SQbolfgDpwdXYkiUXGanaMKswkSeNOl7gKudISZWR_A91nyMQmllxsT8TLND8KSWiDPeeJg7MrsGaz39GgHJC9Fuud1vyhA4yy5RWagYaySE80LL_SZFsCondyagqr0M1kf94_MBOWLeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f017f858a.mp4?token=d-u2j8awWm_m_0lHbty6fyAe2urrN1i4H17O4us5l7ij23pxtiHIbm-OzBXSaKrupRLc_ccdX5j4U-NiLdNZsKJzdwBfD6qo2PoHP5vmQkbVgTrqRxDIedL62lymFq_sbx5BKNJ8HVZQ3vwrVm6Ur3tSnq7Cis6COU2QoUkq3q5pV_RZ9imX-sPi-Aikb1Ucb_vmT1Wa_SQbolfgDpwdXYkiUXGanaMKswkSeNOl7gKudISZWR_A91nyMQmllxsT8TLND8KSWiDPeeJg7MrsGaz39GgHJC9Fuud1vyhA4yy5RWagYaySE80LL_SZFsCondyagqr0M1kf94_MBOWLeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آیا می‌توانید جلوی حملهٔ اسرائیل به لبنان را بگیرید؟
ترامپ: «بله. آن‌ها احترام زیادی برای من قائل هستند و هر چه بگویم انجام می‌دهند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66494" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66493">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66493" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66493" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66492">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hlz2SvUvKrpNw9c_RnKX3V6clEW_OZCmbTh0RHq8y_zSLFK_Y2C0s3iWjLr7fgou9dMjPNnVrGFDrtljPFhyeCBJixdIASYNDjwwLkBYs85aZkVz9iUyiYPjQWkeuxvcGFBluWbAXJSyurI2bVXNVMC5NLxC3Lym0EdWPaWT1klOEIS3AwkMjnwP4i9dhltlKPrxamllpQX5Vak2IfvxrS1wQ5jMIQxZvJJh9sEWjvCW5iiejlQxXOZOizee7QRssQMNDBBM5u7XpFvC1P1BiJNTMi4EFy0mXV6PiLjb30PFOGDW6AGMijXJGs0jKlxGGtB-PpYrLH4QoPB72-woBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66492" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66491">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkLmXTnnkeXdi88PAfvlmVqcqOL2SWNJ19aiMrTEDrikEVjzmPlgqtzk7LtVXmyKLqOYLqLs9rj5PCLZsjCn7cXJT06KqAUMfFU25TyAcm_5siueuSRhsGhuWK8bVZnZmweHhg0MTgM_QiAqb8l-S5tDqazRHVg1m1U21QR-u0wiMDZTj1UzKvYZnx3F5GMM3DXtx3gQSPJxnPORXBr_erQcsH0IO7vxDlcbCNUSbFAuxjpTkMLYEV6tFlXQFbPgoT6oC6TSbNrly3pxMbYBHrkKrSRd5Zl2xmjx79jTmv9_5F57jjaFnXSCMbXqRCCsqcLDBGr2tIGIJzW61yZAXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل به فارسی؛نخست وزیر نتانیاهو:
پس از حمله جنایتکارانه حزب‌الله که نقض آشکار آتش‌بس است، دیشب به ارتش اسرائیل دستور دادم که با قدرت به حزب‌الله حمله کند.
ارتش اسرائیل به بیش از ۸۰ هدف تروریستی حمله کرد و ده‌ها تروریست را از بین برد. متعاقباً، ارتش اسرائیل امروز صبح به مقر حزب‌الله در بقاع حمله کرد.
امروز صبح با وزیر دفاع و رئیس ستاد کل، ارزیابی وضعیت را انجام دادم.
دستور من واضح است: اسرائیل حمله به سربازان یا خاک ما را تحمل نخواهد کرد و بهای بسیار سنگینی را برای این حملات از حزب‌الله خواهد گرفت.
ارتش اسرائیل برای خنثی کردن هرگونه تهدیدی علیه نیروها و خاک ما اقدام خواهد کرد.
همانطور که به صراحت تاکید کردم: اسرائیل تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان باقی خواهد ماند تا از شهرهای شمالی محافظت کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66491" target="_blank">📅 15:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66490">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc6524eaa.mp4?token=DTROqNmyBrw3vjqx1gfJWRAsBQxmrsGsKv0WK2hlaGkMmH4gPiF8YFLO3aRPP9MHYiN7CsYtQwCRDmRAqzGNLjZ5zbWx31_DcEZSWblr_f7Gn2CLFer5Fqczm-Y5wEZU94J4mxqshEGvRw6OvLI8qpk4WP4ws6kAI8MhA8I-IJnv14F8R9aOvKtLNPgyfChAIPFItEz7wHcCCsJhTAa-LgAe-U6b4_kOWO2oFNjJwRMjSTXFBnyxja1iLvtJDO-zRYz20dpQqPtN3uSObOaSlGhj4kGp_973k9XLK3SuxJfMeBYzEts_wPMcfXV-nSiwD74BRoKcTszh9DVdQgffCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc6524eaa.mp4?token=DTROqNmyBrw3vjqx1gfJWRAsBQxmrsGsKv0WK2hlaGkMmH4gPiF8YFLO3aRPP9MHYiN7CsYtQwCRDmRAqzGNLjZ5zbWx31_DcEZSWblr_f7Gn2CLFer5Fqczm-Y5wEZU94J4mxqshEGvRw6OvLI8qpk4WP4ws6kAI8MhA8I-IJnv14F8R9aOvKtLNPgyfChAIPFItEz7wHcCCsJhTAa-LgAe-U6b4_kOWO2oFNjJwRMjSTXFBnyxja1iLvtJDO-zRYz20dpQqPtN3uSObOaSlGhj4kGp_973k9XLK3SuxJfMeBYzEts_wPMcfXV-nSiwD74BRoKcTszh9DVdQgffCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.  @News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66490" target="_blank">📅 15:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66489">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71570c04a1.mp4?token=QPzDMEoo7_kpiAENO-s5dJki2vqIDnu5HFNZnbtAucMgA8ueOco38sHqb43osHAnpDGMKaBTKGwi3s2sL_xUcvSEwomWhejaW0XnoyLJrO97HdRDdUH2OcGbFQtRzTFd-C6-Zvm_0TblT_nHd7O16f0zZ1OR7J9uJnZwQQoWEQbAwRbWLIF24-ENdrFgrp2xoK_zqX0-Ey2UI8eyN4zMvmiBLOozBYEdPM-ric0o1jtu9KhQINqg_NXHatfydD95IL-mxAFRywbKqUNuFrRqnjjlRiUW649b1mgjB6G1tULnhRGfGYdXguesW4T2NM8VhXzMArAZK88GdaQ0HtQhVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71570c04a1.mp4?token=QPzDMEoo7_kpiAENO-s5dJki2vqIDnu5HFNZnbtAucMgA8ueOco38sHqb43osHAnpDGMKaBTKGwi3s2sL_xUcvSEwomWhejaW0XnoyLJrO97HdRDdUH2OcGbFQtRzTFd-C6-Zvm_0TblT_nHd7O16f0zZ1OR7J9uJnZwQQoWEQbAwRbWLIF24-ENdrFgrp2xoK_zqX0-Ey2UI8eyN4zMvmiBLOozBYEdPM-ric0o1jtu9KhQINqg_NXHatfydD95IL-mxAFRywbKqUNuFrRqnjjlRiUW649b1mgjB6G1tULnhRGfGYdXguesW4T2NM8VhXzMArAZK88GdaQ0HtQhVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66489" target="_blank">📅 15:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66488">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3bba52e8.mp4?token=iUqZWtm9yxP2ykz02pKXf715LsMnIo9PqFajUjSZaemNaFhuTNK1QEKGKzpdcmyBPaD1eBeS_PU9EP6FncbtGCKz8RKr47FcyTcXwAD4l1vSEDzjCsbEXRJnY5foveSBtx_yMgmeLcF8TR9tHGQnoEqhtFgwf_JNCdikoJLXdncPbbefH2BdBZvbQL4PnyJh1reRvTAkSTESai_nnN6ykEwkcLDHetIhV4Y4-BKJjTX7WLDWdpc829c6lzoL9fX9CC-SGbEzGtXuQNxLMf4oQt-6O084AAbkggaSWe_elR7eAmkcVPz5HeJ6z_OTijz3NbvGMCQO5q9nUY6unkTO9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3bba52e8.mp4?token=iUqZWtm9yxP2ykz02pKXf715LsMnIo9PqFajUjSZaemNaFhuTNK1QEKGKzpdcmyBPaD1eBeS_PU9EP6FncbtGCKz8RKr47FcyTcXwAD4l1vSEDzjCsbEXRJnY5foveSBtx_yMgmeLcF8TR9tHGQnoEqhtFgwf_JNCdikoJLXdncPbbefH2BdBZvbQL4PnyJh1reRvTAkSTESai_nnN6ykEwkcLDHetIhV4Y4-BKJjTX7WLDWdpc829c6lzoL9fX9CC-SGbEzGtXuQNxLMf4oQt-6O084AAbkggaSWe_elR7eAmkcVPz5HeJ6z_OTijz3NbvGMCQO5q9nUY6unkTO9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
هم‌اکنون سپاه در بیسیم کانال ۱۶ دریایی.
“از آنجا که خروج اسرائیل از لبنان و لغو کامل محاصره دریایی و خروج نیروهای تروریستی آمریکایی از خلیج فارس و منطقه از جمله شرایط اصلی توافق بین ایران و ایالات متحده است. تنگه هرمز تا زمان تحقق این دو شرط بسته خواهد ماند، به همه کشتی‌ها دستور داده شده برای امنیت و سلامت خود به تنگه هرمز نزدیک نشود، هر شناوری که از این دستور سرپیچی کند مورد هدف قرار خواهد گرفت.”
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66488" target="_blank">📅 14:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66487">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
مرندی عضو تیم مذاکرات :
ترامپ بار دیگر ثابت کرد به تعهداتش پایبند نیست.
رژیم صهیونیستی مجازات میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66487" target="_blank">📅 14:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66485">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شعارهای دیشب مداح حکومتی در مراسم محرم
😐
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66485" target="_blank">📅 14:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66484">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddac5fcdb8.mp4?token=Oto7dIl9jCewRZKhrN3VJ97umCBCIa6ln5zffkmAm4j1FWmV0sgBOBu7O7yYnRiN369cUDj-ykST_S01sbhLWx1XEqPqHnUNfuFl1VnoWgk7Wi00VKPf_GcNUa-QU7HFST82q8My07RNVjreDmfMBVybYfmDr7wnoKaet6p3Zg_cLOUZpjt2TO9mtlyhJR13sSarX3kccAgJrzLcqoiWyU6OrrR4PPDg-sm_ISSWTIpUoXwangIV_RrmCfX3BfBCHKgFw8GGTOKlx1HhCXDrMBNzd9t_i8NqgLDfKiaHUHc8qLOyucVo9O6KYcKLK3YKkQ-CiWhPQd_TbwwgVeNy6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddac5fcdb8.mp4?token=Oto7dIl9jCewRZKhrN3VJ97umCBCIa6ln5zffkmAm4j1FWmV0sgBOBu7O7yYnRiN369cUDj-ykST_S01sbhLWx1XEqPqHnUNfuFl1VnoWgk7Wi00VKPf_GcNUa-QU7HFST82q8My07RNVjreDmfMBVybYfmDr7wnoKaet6p3Zg_cLOUZpjt2TO9mtlyhJR13sSarX3kccAgJrzLcqoiWyU6OrrR4PPDg-sm_ISSWTIpUoXwangIV_RrmCfX3BfBCHKgFw8GGTOKlx1HhCXDrMBNzd9t_i8NqgLDfKiaHUHc8qLOyucVo9O6KYcKLK3YKkQ-CiWhPQd_TbwwgVeNy6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
املاکی در مراسم اعطای مدال هرکاری کرد نتونست گیره مدال رو بندازه داخل و گفت میخوام یک مدل دیگه برات ببندم و مدال رو گره زد و نزدیک بود طرف رو خفه کنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66484" target="_blank">📅 13:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66483">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
‼️
وزیر خارجه پاکستان: مذاکرات سوئیس بدلیل مشغله کاری مسئولان ایرانی در ایام محرم به تعویق افتاد
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66483" target="_blank">📅 13:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66482">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd02588050.mp4?token=eF3vgtJv7E-x_4BgsFtLbCQEV23lIlejvWXKTwDz9B1SWEFdH21AWRimzb4HJ02xnaj0IPzZloc7tBi50rmzpFLHh42gw8LbNpTcpUoF2MVGmxZMglMLNykeBkSt3m9WP30ArvzIZ5QMGPwKSge_SjbGI0BKGQX3vESfBhIdGRhjO8FOz28p7s1uwUx3o0SHCbTih41ye8OR3JD2xY60G5FfxsQ9IvuPslSuzOODbT7RW6lP9ekMeQy2tdle0pIvkoftPTnBEaGhZx6JMPksvXbdRD53-rCplZs22dbIoUeA0jNBMoPFpKCk2p2aPk6K4uWwBevpoQEwVqBCzw3JHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd02588050.mp4?token=eF3vgtJv7E-x_4BgsFtLbCQEV23lIlejvWXKTwDz9B1SWEFdH21AWRimzb4HJ02xnaj0IPzZloc7tBi50rmzpFLHh42gw8LbNpTcpUoF2MVGmxZMglMLNykeBkSt3m9WP30ArvzIZ5QMGPwKSge_SjbGI0BKGQX3vESfBhIdGRhjO8FOz28p7s1uwUx3o0SHCbTih41ye8OR3JD2xY60G5FfxsQ9IvuPslSuzOODbT7RW6lP9ekMeQy2tdle0pIvkoftPTnBEaGhZx6JMPksvXbdRD53-rCplZs22dbIoUeA0jNBMoPFpKCk2p2aPk6K4uWwBevpoQEwVqBCzw3JHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلاش سربازان روس برای سرنگونی پهبادها
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66482" target="_blank">📅 13:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66481">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d70873ad.mp4?token=BlKb9Fc88uh48Odv_ug6FQLAmd1wRDV6RcT9ITjxJATf_R3zHodsVswhzBDDAFiVyiT0_et8H6UN-Pwg5o9Jj3UOdOff5_7N9rNxKnF-yHfe7PLo9wNedg0zZoXnFz_m_7pQPC34be92WcLiovczEYo7iPMTjscL7QYcveZtL1iK7AErMdsjIosJi6OQe41-UMsF1G4PQjExQeTZ66URzdyBaZb9lWd3xFhuAkU3terWgGR_aycFyw5YaTdcegyl1HC_3hXbvowjVf0HzMitJt7lr6izDw-uR8VnB81Kw6dOzuQdPV7ckdYM2kU9gT6iYhI_YLzlRq1KoqGuENoQ7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d70873ad.mp4?token=BlKb9Fc88uh48Odv_ug6FQLAmd1wRDV6RcT9ITjxJATf_R3zHodsVswhzBDDAFiVyiT0_et8H6UN-Pwg5o9Jj3UOdOff5_7N9rNxKnF-yHfe7PLo9wNedg0zZoXnFz_m_7pQPC34be92WcLiovczEYo7iPMTjscL7QYcveZtL1iK7AErMdsjIosJi6OQe41-UMsF1G4PQjExQeTZ66URzdyBaZb9lWd3xFhuAkU3terWgGR_aycFyw5YaTdcegyl1HC_3hXbvowjVf0HzMitJt7lr6izDw-uR8VnB81Kw6dOzuQdPV7ckdYM2kU9gT6iYhI_YLzlRq1KoqGuENoQ7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتز، وزیر دفاع اسرائیل، درباره سوریه:
ما آنجا می‌جنگیم. ما به الجولانی نیاز نداریم. الجولانی، تروریست کت و شلواری، نیازی ندارد که بیاید و به ما کمک کند.
ما سوریه را خوب می‌شناسیم. او قرار نیست در لبنان به ما کمک کند. او باید در سوریه بماند، در کار ما دخالت نکند و ما را مجبور به دخالت در کار خود نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66481" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66480">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15d1aff21.mp4?token=fnBiR3ILhipem248BjLLAXzXpes--Y3SEhNxnIVUJk4EWTBYwWqdyCXElOXUnSM1DvZTLUzXGpbEX16OMBVN50tfmYaAwC6K5h8FhudjbPnn2edT8wACx1vV94_3AN-1Zjwf76UDa6j7R1TLp6H57fr2Oz3s7Fq0OtZc_3_cAb5CqJvl91d4J-1_36c1CD9w-TnV9EVFLtxpdWdUTubtht86NRCxWrpVvhvxkst3AK0eUkwLl6w4UXJXp2QD9tfWSBG_sHNmNcn6Mxts90gEnhmTEln69H1D38aZ4uBbR42bZVj4npnD-86R60OsbbCjDa-E1cqwFPRtf8DYhgHGeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15d1aff21.mp4?token=fnBiR3ILhipem248BjLLAXzXpes--Y3SEhNxnIVUJk4EWTBYwWqdyCXElOXUnSM1DvZTLUzXGpbEX16OMBVN50tfmYaAwC6K5h8FhudjbPnn2edT8wACx1vV94_3AN-1Zjwf76UDa6j7R1TLp6H57fr2Oz3s7Fq0OtZc_3_cAb5CqJvl91d4J-1_36c1CD9w-TnV9EVFLtxpdWdUTubtht86NRCxWrpVvhvxkst3AK0eUkwLl6w4UXJXp2QD9tfWSBG_sHNmNcn6Mxts90gEnhmTEln69H1D38aZ4uBbR42bZVj4npnD-86R60OsbbCjDa-E1cqwFPRtf8DYhgHGeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حملات گسترده ارتش اسرائیل به مواضع حزب‌الله
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66480" target="_blank">📅 12:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66479">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae8db95bdf.mp4?token=YVwdQBYPnHjJK5Nd2DhDG78qlk3clO6M1v24dsgHaqQjfptq1C88n2K0UzGwrCWWnoNBrABYtzxfxnrASWai7BJhUdNSr47fTpj1UnjekqmBr1Z2fUBZLrVDYrUJ2Pq6H7A7jD58pikhRGZflnU3foHCpvheFb1AoGjuAp2eB-8Ku6cqxscldyo4lvH4rYOrm3ORsTG6PlB7sYsOQM1zTZX3THobQRYxQ0eUfzci23SW6zxAK3L9szfDX0ZBtbBMfOQn7lFPm68D2zeaBdIOkPnFoevrMPnIBATq2DLN9uHljlou4rCjSUo4kUZrUk-75HOYtPWS56Eoz7DJQIXJ4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae8db95bdf.mp4?token=YVwdQBYPnHjJK5Nd2DhDG78qlk3clO6M1v24dsgHaqQjfptq1C88n2K0UzGwrCWWnoNBrABYtzxfxnrASWai7BJhUdNSr47fTpj1UnjekqmBr1Z2fUBZLrVDYrUJ2Pq6H7A7jD58pikhRGZflnU3foHCpvheFb1AoGjuAp2eB-8Ku6cqxscldyo4lvH4rYOrm3ORsTG6PlB7sYsOQM1zTZX3THobQRYxQ0eUfzci23SW6zxAK3L9szfDX0ZBtbBMfOQn7lFPm68D2zeaBdIOkPnFoevrMPnIBATq2DLN9uHljlou4rCjSUo4kUZrUk-75HOYtPWS56Eoz7DJQIXJ4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر دفاع اسرائیل:
ارتش اسرائیل باید در آن سوی مرز، فراتر از مرز، از کشور اسرائیل در برابر سازمان‌های جهادی در لبنان، سوریه و غزه دفاع کند.
ما از «مناطق امنیتی» حرکت نخواهیم کرد، نه در سوریه، نه در غزه و نه در لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66479" target="_blank">📅 12:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66478">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmcQ_rTT9hAYYWmBAUMIqKsx-gCF-SfLah1OtW6gVReHLFyTAPRKakm3lBW2RkjPwTc64HKFgTemluQdtx57QjaCm1PXeOWTblxAc7g-znS-uYXXT32Gl1oacoopxgzLpbOJtIy0LHvksguhBNDLsReVhwTznF5qXIZ7No8zJvc2O32NmsIepOHmwpDoGVOivzfga7naO7rPSvq7QEpYLSfIF-IUrsAqjF_9dsGKvJxMIOwnq8h4BXL6ak0GcV6z9JEjVU9uN-OKJJoQuXcC1S43ETQ8Bpsep0QA8cbtAfVef4UiBwb1oX5l220KLDgfGwgn07qA4VqXpTym6F5r5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
گوش‌بفرمانیم، وظیفهٔ محول‌شده به ما توسط مقام معظم رهبری پیگیری تحقق شروط و بندهای تفاهم است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66478" target="_blank">📅 12:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66477">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=X4PADtfjnq0OZdWvK-yRBxCDTgzKfhmxw2Y0huFBfIBAk83fGKt9vPYIJYJgR_BYk2f2aAZYWvXgbe_Qa0b0rr98WSVC1ziTgIun4GgHq-F3dyhWh51NQx9WVYeKXxDDZwcP6VxkYNo5h6rPS2Q7BMEDUYVTTK1X_sE11F1dd0t9S1x2X8aIqAEyg7_WQOleAq3XjOCLoQcw9CU3mJyGUBeVrLV36pJOsxbF5ry7ERJWVq3173Y9YMNcPzy-eg8hnq3uaIiTvtfkQEoWEX1Sug29cEsl-XG_-pTErAjUM8ZC0G5JpY1III4cGGyK7YRq50RnTUpBljNhPKXO8nyZEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=X4PADtfjnq0OZdWvK-yRBxCDTgzKfhmxw2Y0huFBfIBAk83fGKt9vPYIJYJgR_BYk2f2aAZYWvXgbe_Qa0b0rr98WSVC1ziTgIun4GgHq-F3dyhWh51NQx9WVYeKXxDDZwcP6VxkYNo5h6rPS2Q7BMEDUYVTTK1X_sE11F1dd0t9S1x2X8aIqAEyg7_WQOleAq3XjOCLoQcw9CU3mJyGUBeVrLV36pJOsxbF5ry7ERJWVq3173Y9YMNcPzy-eg8hnq3uaIiTvtfkQEoWEX1Sug29cEsl-XG_-pTErAjUM8ZC0G5JpY1III4cGGyK7YRq50RnTUpBljNhPKXO8nyZEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بمباران شدید نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66477" target="_blank">📅 12:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66476">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cbfc5535.mp4?token=GZJg0IsdexQQ6LHU8b8yiP9vLHeTyQKqzk4Bixvk9hSKhN_R6N5utv9VVtd_tX_VrLIP3WAHWpUXqE-f-qwveLxtIUdtNAqtSvfA6ja4-Le-QYFpThDFSyL-taUtBD3VuZp5d0HYqrWCwNPWYzeqPqAyBMcfxxPhC8rLWVfG63Rss6sVKfpP5LCfLSY2AVM9OVHaC0nxOCLKnlc3DNbWCUwlYk90bdVZ_CkwQ7mT95QMkF7q75kVT1dJ300tpqG-wCpQeU-dZqrL0_H6fkJZbuSy9G-lsIOe3eimASSuzVHsnX-4VRV-CdqzZDd4eIBk_YDTsC9beqeCFec5ATmVSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cbfc5535.mp4?token=GZJg0IsdexQQ6LHU8b8yiP9vLHeTyQKqzk4Bixvk9hSKhN_R6N5utv9VVtd_tX_VrLIP3WAHWpUXqE-f-qwveLxtIUdtNAqtSvfA6ja4-Le-QYFpThDFSyL-taUtBD3VuZp5d0HYqrWCwNPWYzeqPqAyBMcfxxPhC8rLWVfG63Rss6sVKfpP5LCfLSY2AVM9OVHaC0nxOCLKnlc3DNbWCUwlYk90bdVZ_CkwQ7mT95QMkF7q75kVT1dJ300tpqG-wCpQeU-dZqrL0_H6fkJZbuSy9G-lsIOe3eimASSuzVHsnX-4VRV-CdqzZDd4eIBk_YDTsC9beqeCFec5ATmVSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتس، وزیر جنگ اسرائیل:«حتی اگر ترامپ چیز دیگری بگوید، هیچ‌کس نمی‌تواند به ما بگوید چه کار کنیم و ما قبلاً این را ثابت کرده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66476" target="_blank">📅 12:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66474">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba86fa7681.mp4?token=UEkvABkxAVQk7QumapA9OoyQywkLJ0VMvZ-DAr3UCFvlZ4mHjEKCPB7zQeDb2nUmsIbP39iH87uD-sqGCOCewfBCQ-5JbQtdn0_XBePrfvmRRHpjKZTwteeUMj4gnAoQ0DuRVvZoSVebG9pKYTnQjQU2JmYzaB0rmCwxAcS7JLE74F1YL5oBOD3heQAr3QQGA7lCALhVDOwe5-05KxWdsLP8Qg4YPFlJyStiwXapuYSK2ic0suDVwBrB7Zczu5j24EBAmaA2JGeZId75cPiRy9evoZ5sa8tjIhHxeHtmHmdJrzkHt6NO2eu8w12QloGRnsDv3J_MoePs7k2CvUtIAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba86fa7681.mp4?token=UEkvABkxAVQk7QumapA9OoyQywkLJ0VMvZ-DAr3UCFvlZ4mHjEKCPB7zQeDb2nUmsIbP39iH87uD-sqGCOCewfBCQ-5JbQtdn0_XBePrfvmRRHpjKZTwteeUMj4gnAoQ0DuRVvZoSVebG9pKYTnQjQU2JmYzaB0rmCwxAcS7JLE74F1YL5oBOD3heQAr3QQGA7lCALhVDOwe5-05KxWdsLP8Qg4YPFlJyStiwXapuYSK2ic0suDVwBrB7Zczu5j24EBAmaA2JGeZId75cPiRy9evoZ5sa8tjIhHxeHtmHmdJrzkHt6NO2eu8w12QloGRnsDv3J_MoePs7k2CvUtIAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی شبا میری اعتراضات و روزا میری راهپیمایی:
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66474" target="_blank">📅 12:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66473">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc0be5a6ce.mp4?token=T-wUfxKCgPY_QDATVbSZDMbMX74asGiUkujTT8mPdYuI4oM7xQfSzDWtDcIAhWqbEONXc8nyOnuGat8gw2BYBqxbdwshahgjjweuQOTfzjeNcTN_GtRzkHePy7HqLPwyPAEJ-4GK6axfjsI8c7TATOq7c63gFqZ0O8jR8npfNFE5Le48QfQWNPGMvwvPpMYHJrYGjs-PJ6OHNLrQXq8eoVR5ZB9U0UTuSiB6ow4dQqIGCF03dz8UX3vxgN2EAcruruBvHODOuQg9F1ExNu8C9cnuXI6RD_TyOT8ri-4K_SGAizpNAyHK5Kwg2dW-f-JfaTu0Uo3sZaswz6e0AUNJ8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc0be5a6ce.mp4?token=T-wUfxKCgPY_QDATVbSZDMbMX74asGiUkujTT8mPdYuI4oM7xQfSzDWtDcIAhWqbEONXc8nyOnuGat8gw2BYBqxbdwshahgjjweuQOTfzjeNcTN_GtRzkHePy7HqLPwyPAEJ-4GK6axfjsI8c7TATOq7c63gFqZ0O8jR8npfNFE5Le48QfQWNPGMvwvPpMYHJrYGjs-PJ6OHNLrQXq8eoVR5ZB9U0UTuSiB6ow4dQqIGCF03dz8UX3vxgN2EAcruruBvHODOuQg9F1ExNu8C9cnuXI6RD_TyOT8ri-4K_SGAizpNAyHK5Kwg2dW-f-JfaTu0Uo3sZaswz6e0AUNJ8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نبوغ اوکراینی ها در شکار پهباد
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66473" target="_blank">📅 11:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66469">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iugeilnXwAIcJGZ3b8g9NvVx_oMTEA7dHGZ0_hgOfhx8Irxnszbl1PMZaXi1YRzJ3fSAo9VALm-Bj578JKAbwd-pDInDBng3TA7oEEW2KNW794fOomMQdPye992V8U1b9jn3ncZyBTIbyn9aYbeDr9le4ZLyd1P3w_Vh8-IkjVSc66FFCMKNAZGRBS0VQUepZQvAzdzslWQxvlA37ZQ64ZjM6AvBtpA4gfuNgLmYSCKr0UBsFi6oFPLnFgG8IwaIeZrI0L8GF1JfClDtzeqBM1gDZEHGO-sKmCvkt9gz240-mdO4x6bi0MLX4SPhrcKeUN1mlEZjI_-3q_9fhAn_ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hUO1ARzRU8chUzCVXl2FuucjibbCs4XJv1v1HaXV1Zb8n9CQ3oFkJOfi-FXzIfBIbqVwm67TkBomZX2cYTvMmuhRmivHuhz7AtX0j3Zd7i3613sQLENOSODUwAi7rjdY_swrtohPBGVfLSZB3Wl6Cm_Ncxb1bLu6osRQgt1Tn3y0EAQtR5jy0HQn7qYpzDGtGt_H9aGLASFweBfZr5AMTZgrAPJDt3pSOg8kibWFx9E8uXrc1-oB0g85BPBTPVVJMOsKv_U-MwQ35D45DBrKWjPpgT4rEcKYrkVfIUvZU-DOxlTmWUvLwjZel34khJQTU1Zvmx6VRx_PKpgQIj5gzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YR126RsZ6Spt8hPItz6L7DVjBKkp1MxCzwtl5LLLl91kw5N1toVqNeBKEuRG35PQlBAGqcmGxYeq34IIaymwhbqpkxaFRj9ORMg5Tlh5oRHpCpu78EuRGKVn84Wv5wCn7pT2wZxbkvj12pi3B42DQzIMeSRR566EK1UghAV7Tz5AxvqBEHF3r34cZNQFhw6ChuNvP3CrPVwHEbKSsjtlhGVUrcFHFlsqVYax6plO6QkRUW4wR4zSj0ivvC6BHFGXKAjxEU8eOL6Fy2BZQU2rtI9A4CWh9F7B9nPnsye_OdvnPp51qS2ZwaOBBDmiMCTeA7Y85emnXb2Pffef99HJlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cb0e601ac.mp4?token=pGt9TrrT2LwqGpuJrFkpp2hiyAVF7FgT60ylqu9ZKBlUgAu1VKiMzW2y_qM8nzhjvI79kM3UYWJlmao03LcC1spiuCIhIkA92-bj9Qj9c4pAB0GYXa5yF6u1AKLDQDnk7X92_5NmHAXEZvKXt8JUK7d_6ijwS0U2zkXdwgqhPNhssUxqHPustF4_AmR4Tw_jyt1v9cY08DvO4M0i-qLscOUPd6c63AMhqSjiJNlZ_JGiolrnolyv94QUw0IOjYsvf8PmiHpP87m0_FxNBc0sYL02nvSCDhpSd3NYONuvpaeIDJlDiTrX6NySNckvvwFs7M0CfVnnL7LRAYsVkMnoEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cb0e601ac.mp4?token=pGt9TrrT2LwqGpuJrFkpp2hiyAVF7FgT60ylqu9ZKBlUgAu1VKiMzW2y_qM8nzhjvI79kM3UYWJlmao03LcC1spiuCIhIkA92-bj9Qj9c4pAB0GYXa5yF6u1AKLDQDnk7X92_5NmHAXEZvKXt8JUK7d_6ijwS0U2zkXdwgqhPNhssUxqHPustF4_AmR4Tw_jyt1v9cY08DvO4M0i-qLscOUPd6c63AMhqSjiJNlZ_JGiolrnolyv94QUw0IOjYsvf8PmiHpP87m0_FxNBc0sYL02nvSCDhpSd3NYONuvpaeIDJlDiTrX6NySNckvvwFs7M0CfVnnL7LRAYsVkMnoEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات ارتش اسرائیل به نقاط مختلف در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66469" target="_blank">📅 11:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66468">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-g31N-VOL5kx52klp8RadyiuHoJ8LiLvluGfR8Bwt6N7oq6W34dJPpfSA_mL9EwalAIxh-JHvp_8dACwIiqC4CdoB_p5-PpKe2WBAEdlYKxkQbAE_9toO5p_jVo1nQXmJ-6vsA0H9MwKeBHmsJSY5F-QbqAWc5X-BkMLUI2tMpYunitAG18C5TzLveoulIPTCKRYD1jtdMkVUPkHGQxWhQe6UnQ9jWr0-7m7EkeUDuZcO1RFoiLjHS3FMbvQNA_EZ-qqonxO6WVD3sl2nJvjBi0HX12oUGnDr0T4bPbkpKr4OtNC7t32mjr137yPZoV2uZK7nXvmdOWSRFk21JtUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت ‏مسکو، روز ۱۵۷۶م عملیات نظامی ‌ویژه ۳ روزه پوتین در اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66468" target="_blank">📅 10:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66467">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7be955089.mp4?token=Q6CPBt21Hskg_CVq-p3uQFQEyOKevJ1SNMLh_VbmcU_Z43EgAUZfdyPoPxjeKvhxwhkpcg0iaalmPgmpqpeHycfAgNAJghSpynNJfOpkXvsAg6mqttvfvxxFJJK9ph7iUyqaHAnU83iMQjh7cqW03JSVSoShfBBDnHnMECMaLNqeZ9J-dlGaiQ4ERMXmSGljncafll7TuENxLuaiDc_qzrNSDIMYyezk8rsybLlzEYSzPwR0HP1Ehz1JWvuEKbhxTQheefX9rqrWlR4QJzLVwk7RLwmFACNdbIOtMPOZgyQZ1B8eXtTfRXPw_6_ey_nylKTBssyRmxSey98mqNwRDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7be955089.mp4?token=Q6CPBt21Hskg_CVq-p3uQFQEyOKevJ1SNMLh_VbmcU_Z43EgAUZfdyPoPxjeKvhxwhkpcg0iaalmPgmpqpeHycfAgNAJghSpynNJfOpkXvsAg6mqttvfvxxFJJK9ph7iUyqaHAnU83iMQjh7cqW03JSVSoShfBBDnHnMECMaLNqeZ9J-dlGaiQ4ERMXmSGljncafll7TuENxLuaiDc_qzrNSDIMYyezk8rsybLlzEYSzPwR0HP1Ehz1JWvuEKbhxTQheefX9rqrWlR4QJzLVwk7RLwmFACNdbIOtMPOZgyQZ1B8eXtTfRXPw_6_ey_nylKTBssyRmxSey98mqNwRDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری: شما گفته بودید که فقط تسلیم بی‌قیدوشرط را می‌خواهید. اما این تفاهم‌نامه شبیه تسلیم بی‌قیدوشرط به نظر نمی‌رسد.
ترامپ: خب، در واقع احتمالا تسلیم بی‌قیدوشرط است.
مجری: واقعا؟
ترامپ: من این‌طور فکر می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66467" target="_blank">📅 10:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66466">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/040ce8f378.mp4?token=hPtUH676_GN5EhDEgZkHlqB7A0s0VwopkhbRFhnOYas8nz0joASaPcl8rJ0XiWHrq9LkYBJ65KkCggdKcEP7bl7ds3_4ifCaJZMPKodHwTgN7ASikArxD6uTsbXNZ4kQ0l6rmQYp0oRlji7sCczJ4eJZm-F-ldP1-Cc-ez33NApKGclDju3dwlvnJDgOlSzoYAqZWr9Yag5qc-FV4klHbY3q-3aVoX_JGy-d8pVpaqIE4OVYimk_kXyrHxrdu7JL1g3u2s0aOOZf_OJg6leLXtjDF2q8j5GYPIhF1ERDLoFwy-_scQGQqQCqMP4dz6HPNFm2AJpFe87w9ddty4H6KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/040ce8f378.mp4?token=hPtUH676_GN5EhDEgZkHlqB7A0s0VwopkhbRFhnOYas8nz0joASaPcl8rJ0XiWHrq9LkYBJ65KkCggdKcEP7bl7ds3_4ifCaJZMPKodHwTgN7ASikArxD6uTsbXNZ4kQ0l6rmQYp0oRlji7sCczJ4eJZm-F-ldP1-Cc-ez33NApKGclDju3dwlvnJDgOlSzoYAqZWr9Yag5qc-FV4klHbY3q-3aVoX_JGy-d8pVpaqIE4OVYimk_kXyrHxrdu7JL1g3u2s0aOOZf_OJg6leLXtjDF2q8j5GYPIhF1ERDLoFwy-_scQGQqQCqMP4dz6HPNFm2AJpFe87w9ddty4H6KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ به شیخ محمد بن زاید:
وقتی انقدر ثروتمند باشی، میتونی انقدر آروم صحبت کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66466" target="_blank">📅 10:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66465">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635e862fe5.mp4?token=KUcjr2wPpV5a4amkOEsCxett6tBKkMwQ3E8sENZM9ssS5njN1I4BOd-ng6HnDIeKTKZ5V1FFfx8Pqlp9T5wImYsljHXsnoNxJFiL-FHgs28t-y68pApj90oigV92oH6UNLub5pDIky3Q17dTcsOR-b23q6_R9V4bgq-Cm7jwHVZfWb2bgUOfKUNBZqC-Ot7jmd-b71_78Os_CPA4DwFA6RDbr_GFueH5eA8H0VCXYBUlvVbhJ9wgyEZgM5_W4tZ6C_T1tEmAbNpuuTA6WPKf9yogxTBfdRMTANhvUQsLvCKRefD0Y1G_jj5GTq5GNtXpJK7DLeM6S31JZD6YIMEBUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635e862fe5.mp4?token=KUcjr2wPpV5a4amkOEsCxett6tBKkMwQ3E8sENZM9ssS5njN1I4BOd-ng6HnDIeKTKZ5V1FFfx8Pqlp9T5wImYsljHXsnoNxJFiL-FHgs28t-y68pApj90oigV92oH6UNLub5pDIky3Q17dTcsOR-b23q6_R9V4bgq-Cm7jwHVZfWb2bgUOfKUNBZqC-Ot7jmd-b71_78Os_CPA4DwFA6RDbr_GFueH5eA8H0VCXYBUlvVbhJ9wgyEZgM5_W4tZ6C_T1tEmAbNpuuTA6WPKf9yogxTBfdRMTANhvUQsLvCKRefD0Y1G_jj5GTq5GNtXpJK7DLeM6S31JZD6YIMEBUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختران حاج گاسم
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66465" target="_blank">📅 09:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66461">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E28aGXu3HntVXZCcUhu0hjk1XZNBETMeISqQ7wBgiEmnq7cwcK-Ky30f37WMxZSPmMM30li3dWZ7mRiG87q3Ti_NDEY-Vlw0GYwp4BwtqcG17AGjJKwQY3U3w4DJeskF-pRYL8U1FcWMILZlmnTRSbPbwn5heRWKPfbjY9pWW4oOKStUdivVSD8f-j5-mHt8bXBJ6kctDfr1E7nlYlNZFBvOmYdDy1oipd4V8BCMP5DMEqDHoNuSrmoMsUCi3SMdnUadQ8nqfe4Nbtv7oAfkIBBPJCcUpCtH1y61Z3ZO5Hi0L0zJlDHdcgJpv9_CkHnRxSYF7-_Y2_6WXdId5DS3rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a17f4667.mp4?token=oZtPBIejI4KEU4h-k2u0HxCTouCxgTe9M0kUk_XpDSOc58zuNiSQnT7myzYN6-3GgkkwZCgIfTNgKgmRMt3_lZzIzhTYNdcYToC3RObFi7rVv0psWCMuGxuTW4ROt_OFCA9uiBS1mrUqWZSDAJ-Fxxzq9K1Ec2w8PpuYcFVUTaPJ4WvJU5Iws5bOx5RJkT3_Spp_fQAdHqA6FTD8rsuAS9SGH2F5gR458nCp9BWBAfY2bWl9IlEbtq2b3R6G8Eb67pn1C7t9FG8felyTfbMh3hm9bvJ_oDrn_nrGpiQHe5gSXi4FLdSwWy0h6UqjISTiil6NZBcX1LqhhOV-h_NOLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a17f4667.mp4?token=oZtPBIejI4KEU4h-k2u0HxCTouCxgTe9M0kUk_XpDSOc58zuNiSQnT7myzYN6-3GgkkwZCgIfTNgKgmRMt3_lZzIzhTYNdcYToC3RObFi7rVv0psWCMuGxuTW4ROt_OFCA9uiBS1mrUqWZSDAJ-Fxxzq9K1Ec2w8PpuYcFVUTaPJ4WvJU5Iws5bOx5RJkT3_Spp_fQAdHqA6FTD8rsuAS9SGH2F5gR458nCp9BWBAfY2bWl9IlEbtq2b3R6G8Eb67pn1C7t9FG8felyTfbMh3hm9bvJ_oDrn_nrGpiQHe5gSXi4FLdSwWy0h6UqjISTiil6NZBcX1LqhhOV-h_NOLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات شبانه ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66461" target="_blank">📅 09:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66460">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66460" target="_blank">📅 01:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66459">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ScWM53tKA-cPXyMzLBxhG4iYLh7r5fF7AbPTFvQ3p0zEXB2cSxuNoO7zf9E9AAvTluI4RpbUP1MopLd7T21KYquCED1lX2wUQsdqomUGUdAJHOK76h7kCIGTXip1DVg1WZc15KOr2WrZxSNoW3OozzrcgPEE0v11Vvbdyez0REe0XvI3EtjiX6rF3ZjdoTFASc320-36pAsqY94PsHSY8WdzakaX1MF4gyIzoIu_0QuOa9-GdFp3DfAR_dkqOltBn-mge7mD6iy5WuumrClbJHB-WTfc-l7Vy_LKQJ4_PwL16suyVxSy2MilJobnUe51YDnx9joh9arjbfwCYkfyfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66459" target="_blank">📅 01:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66458">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
‏به گزارش المیادین، هیات مذاکره‌کننده جمهوری اسلامی در پی تداوم حملات اسرائیل به جنوب لبنان، سفر خود به سوئیس را تعلیق کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66458" target="_blank">📅 00:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66457">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30a4159b30.mp4?token=Z2nhexPzeTQVFMY0p_puDlBkt_pA90n8YZaZPFq2OjGKyH33i7Do7qJGRK7TepEInF19Fa160g1XUdiaoiyLPESF8MO3Q66s0k3avpWaxEdzLpk1idzPpnWPCw62COTmvVLNt9_Yl6VikCJ5OnTuYwm3Aaflzpr3h1Yb1UqExFgfQEytw2zlRWUFqzpX_Gd9moSA6fQk97j-0ri1May-hCssjyrIwV9um7er1YOEU8xWSck2U-oB-yNTj9-Y2TBLGXZPC55MeNr0NkTAaZXW7deHDvwhiYQklClJ4SK5KKhBW70sCJD8UHkc8Y1Qw2ZkCZVqeZPsE1lNPTmidN-cNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30a4159b30.mp4?token=Z2nhexPzeTQVFMY0p_puDlBkt_pA90n8YZaZPFq2OjGKyH33i7Do7qJGRK7TepEInF19Fa160g1XUdiaoiyLPESF8MO3Q66s0k3avpWaxEdzLpk1idzPpnWPCw62COTmvVLNt9_Yl6VikCJ5OnTuYwm3Aaflzpr3h1Yb1UqExFgfQEytw2zlRWUFqzpX_Gd9moSA6fQk97j-0ri1May-hCssjyrIwV9um7er1YOEU8xWSck2U-oB-yNTj9-Y2TBLGXZPC55MeNr0NkTAaZXW7deHDvwhiYQklClJ4SK5KKhBW70sCJD8UHkc8Y1Qw2ZkCZVqeZPsE1lNPTmidN-cNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
آیا در جامعه اسرائیل افرادی هستند که بخواهند ایران را به لیبی تبدیل کنند، یعنی یک دولت شکست‌خورده با ۹۰ میلیون جمعیت؟ احتمالا بله.
اما نمی‌دانم که بی‌بی (نتانیاهو) چنین چیزی بخواهد.
من شخصا هیچ‌وقت چنین گفت‌وگویی با او نداشته‌ام. گفت‌وگوی جالبی هم می‌تواند باشد.
اما همین را الان می‌گویم: آیا تبدیل شدن ایران به یک «لیبی ایرانی» برای ایالات متحده آمریکا خوب است؟ قطعا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/66457" target="_blank">📅 00:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66456">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47cfe42200.mp4?token=giuVuc_Y9LexwefAa-lE9Fn3gDtsUlIXxGBd7ueDMTS1YefjYV3baYsE9sK352bt7RpS1U6fXbJaRZVb_i62iCcFATH126YhHa0klzsSIh-QFwfyweDpmBH2qi029ZVkOiSS9Wz_zXokVS9FCMjkWOalwB8fWOgwx_r_BuhKzituUw5VCluNuXKy4f-FRymJ_FCGoF-4595tE_HmDIv2xbwodD-heA8r_YWPV6R6qmX7D0ovgSpqLcMjXCJc-Kk9jHMfajCbg7QR0UA34ov-iie65lWzmoKMrZJMvRfO55NDN99R4r5AN2JSX_6qWpIeCrXUXplJ1v0NgRNHro4yqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47cfe42200.mp4?token=giuVuc_Y9LexwefAa-lE9Fn3gDtsUlIXxGBd7ueDMTS1YefjYV3baYsE9sK352bt7RpS1U6fXbJaRZVb_i62iCcFATH126YhHa0klzsSIh-QFwfyweDpmBH2qi029ZVkOiSS9Wz_zXokVS9FCMjkWOalwB8fWOgwx_r_BuhKzituUw5VCluNuXKy4f-FRymJ_FCGoF-4595tE_HmDIv2xbwodD-heA8r_YWPV6R6qmX7D0ovgSpqLcMjXCJc-Kk9jHMfajCbg7QR0UA34ov-iie65lWzmoKMrZJMvRfO55NDN99R4r5AN2JSX_6qWpIeCrXUXplJ1v0NgRNHro4yqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس این انتقام ما چیشد؟
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/66456" target="_blank">📅 23:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66455">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad18edc1d.mp4?token=jwQnSxrod17JW-tGiSHnn63Ly6ekW9zU2B2cjf-xoPfCYDH865ildL95b79YHRSPBzX0LCIwcyTLs8YRtOyk92umxMznu7EvzJ95pvNQVknTPq8hTbIHF_gNLVE2uQMm_b4-EGcAuy4txJs_y6bHsQPQ9Lqhm26UxM0zJb6b_fzejMwgYq_exOU-eeIH0ZNJXGvt5xO5GZryZ5Aif-QnREGaDbzZk68TGIAsqXdUASqDidO5uAh0LBJYDv45UhdFYSCcZPxA5xbczaz_xAvuWd2libGBH8FSAce4RyA50Wlm6_ZoGDoGHIk9g_NBYTHsY6AqtjKCev8B9MaGuUNX2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad18edc1d.mp4?token=jwQnSxrod17JW-tGiSHnn63Ly6ekW9zU2B2cjf-xoPfCYDH865ildL95b79YHRSPBzX0LCIwcyTLs8YRtOyk92umxMznu7EvzJ95pvNQVknTPq8hTbIHF_gNLVE2uQMm_b4-EGcAuy4txJs_y6bHsQPQ9Lqhm26UxM0zJb6b_fzejMwgYq_exOU-eeIH0ZNJXGvt5xO5GZryZ5Aif-QnREGaDbzZk68TGIAsqXdUASqDidO5uAh0LBJYDv45UhdFYSCcZPxA5xbczaz_xAvuWd2libGBH8FSAce4RyA50Wlm6_ZoGDoGHIk9g_NBYTHsY6AqtjKCev8B9MaGuUNX2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
آنچه من به برخی از منتقدان این توافق که شنیده‌ام می‌گویم این است که آن‌ها می‌گویند: “خب، ایران این همه منفعت به دست خواهد آورد.”
من دوباره همان چیزی را که قبلاً گفته‌ام تکرار می‌کنم و احتمالاً مجبور خواهم بود چندین بار دیگر هم تکرارش کنم: ایران دقیقاً چه منفعتی به دست می‌آورد که قبلاً نداشت؟ پاسخ این است: هیچ چیز.
آن‌ها هیچ چیزی به دست نمی‌آورند مگر اینکه رفتارشان را تغییر دهند. اگر رفتارشان را تغییر دهند، آن چیزی است که باید از آن استقبال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66455" target="_blank">📅 23:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66453">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‼️
یسرائیل کاتز به کانال ۱۴:
ارتش اسرائیل دستورهایی دریافت کرده است تا در صورت لزوم، برای عملیات دیگری در ایران آماده شود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/66453" target="_blank">📅 22:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66452">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMXf-sUKZSnpHnlQi99w-7_S22yOQlUUNv5gO-TeCNPEg4r1KlLynojGvBdA9WTp-uPTgQFL1h-SosKCkibUJ4nAOn9K87K3XTZPoZdRGqB9IwP9NxnxBR7GB4Ba9_MV_M2OX6Dr2NHthVas-YqFXOvL_ada42CMxOw5tBdnewp6AH5nZYjr4N9sBOeZZ8dK8QkwgMVTtjXdgwX07v4R0zdosL9itfzv04ltqjP2IotU5brEJ_R3jHrnlvDRvxLq22zqwda07mJzH-HvY-JfqDYsBmJxuvwAfaVaNtTN8J-R_CRt-aUviZ05_3wUSXFFLEEDP8mlXRAryhHTQqLT4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در تروث سوشال:
ایالات متحده به صلح متعهد است و ما همه را در منطقه خاورمیانه تشویق می‌کنیم که به تعهد خود برای پیشبرد مذاکرات ما به زیبایی پایبند باشند. بازارها از آنچه که با کاهش قیمت نفت و افزایش سهام اتفاق می‌افتد، لذت می‌برند. ما انتظار آتش‌بس کامل در همه جبهه‌ها، از جمله لبنان، حزب‌الله و اسرائیل را داریم. از توجه شما به این موضوع متشکریم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66452" target="_blank">📅 21:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66451">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">هات نیوز | HotNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/news_hut/66451" target="_blank">📅 21:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66450">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم  @News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66450" target="_blank">📅 21:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66449">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">این پیام یعنی پایان پزشکیان و جریان اصلاح‌طلب در ایران، و آغاز حکومت نظامیان به سردستگی قالیباف #hjAly‌</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66449" target="_blank">📅 21:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66448">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم  @News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66448" target="_blank">📅 21:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66447">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNr3kN1B6LztzsKGhqDXq8vBy_VVOOkQMe4QmSXC9QZ6vFVnKo0XEw-baPsKX3uR6MkZSappFPFI1T7ykv91zxEo8w-HIXJrx63t0zPUwFQZ6p0Y_BWt5tt8NTSLdXRTQQZccY1dyW_wr5OLcxkz9pkf-Mo3XFSH0tggtFMdU9u5vbVzpouw1cCj6iGgjbeN6zDxMIywN3ES6Q-EoWqH59-8q-g0RygIygYZvwDPdm62mpSgBXd7jwR9de9bQiaoo4-TaP1ROCqo_pXG6fSn7aiwwmgxy6cJoTbPdD5FKZyLBpgy3gT8z2BvIy63ZSuu005Zk0M7jD8i1GSINKZ0zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/66447" target="_blank">📅 21:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66446">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5gQVzuDhUZ8L8OkzMXnHAZxQCW2SDjW6lkEeaWxrHTZU-r4UyUxVMwZG__4Hl36vLj_bqv4rfbtjpb3aYaIo1FvQU3T8G6e31OOd3XHFbb_y-0jpfY1bwfPFhdxnaRiiimC7TTc5ZFtHTN_AQJBk0744qyt7adlwnGbRXsm87PC9xtMYIaJnSn7qmOKG8hdCB8IO3LJpyJ3_VRJjM45hFYahP8wmcGxap9-rclpOx0vU8Oha4w-W2ZeXAAyjOYKRllZrigjKCsjTJnkIGnodz79amP72pR2b3ODPpKYue6y9xXM0yxBWieuzobgz_vuYJr2ysFa07XyCLbxk1dTpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ: آمریکا هیچ پولی به ایران نمی‌دهد. اخبار پرداخت 300 میلیارد دلار به ایران فیک است. تمام آنچه برای آمریکا وجود دارد، موفقیت، کاهش قیمت نفت و پیروزی است. وضعیت بازار سهام را بررسی کنید. پروپاگاندای دموکرات‌ها در کار است!!!
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66446" target="_blank">📅 20:44 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
