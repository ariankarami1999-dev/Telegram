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
<img src="https://cdn4.telesco.pe/file/Mqp4b6MVJutlKUoaHv3Sd5VFu9uSE30R2iJsqVub6gWTOZ42nClqmjnCKG-ohFdRxFLL75yY2PEIhHyVtGAugG9fBrP3id2j-i2libHd3TWahGb5uJKacBODhbAgcl0NM0PyT8_UEgmR_jva7nw8_-4HxcaO1R9U2mlJaFEDdXeeZ8H2Fc0BKE3pNEuPhZD7LlcFvtDz9_qDJX2T0_-8JYfHY6dBcrR9oGW-ia9t4oL1hzOfsTiLlZBF4__POWilEeGmvxXhCGIFMLgFM4JutPqX5NW5WwVRtiRX2z_PM49yxhY5ucBD0O8MGPPAnaU5GhoEU5RN1dQHySaR8FyHzA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 954K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 18:51:00</div>
<hr>

<div class="tg-post" id="msg-129577">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
جر و بحث مجری و کارشناس صداوسیما با هم بر سر نقض تفاهمنامه ایران-آمریکا
🔴
کارشناس صداوسیما: شما وکیل مدافع تیم مذاکره کننده هستی! پس من سوال می‌پرسم و شما پاسخ بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/alonews/129577" target="_blank">📅 18:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129576">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caed9884f2.mp4?token=U3JDUoR-vIoHaLDwfJG26hydY2ytEBOMCmEvhhCWl63Y1_VKEo6X8YsUrNRUK1HhP-_JXmyg0-A-A6a3YK-YyDJtfhKPBMMIXD9G-pWJYfgibhibmq5xg_SxF7zSWAxQMzU0wN_99oV8AIf8fi_K1nfdbXJuxrsgo8jcIGchhPxs_bSSwYussPaYd0umHYZCabmxWWmha2kiURjdjqgQ9BCGFnEMi3oSgmZ55X4PUAkZvYQ-KAJpSGQ1fRhPbXUFd2J_pjo52X8M21RyTHsbEHxyd_8kQUz_chDrZ8m_IthNgLtQaKq7i8cCq26jQHOepP2eZjIKdt7bw_h46OWbgaBDDGyANddcxvDdaRNDM9hyEL_I49d_ttkjgc7tRowKBTSjDvvzb_uWqQAgtO9X4WJavS7sDj_WvASQE7Kk-JPajKoynJH40-FpeRe4CcFIJo0HS85iSWOT94CdLZDhD13o4oDT7fZjB_y9TKu-v_uFOA8x9EBBOYohoLhlR7ZGewUXfHxJveqFq-7nREo8dFV6cpR2-3VUkje-NoV_Up8SUqQbiRGxYLhmYWyc5B91m9oTULucQYY4vHocL9QkdEJXhR5yyJKP--oesgrMhwar0gfN4n7ugqg_4LAvxf1uytmHNA6PAkLG5SLmtb4hXPo6WBA2fYajUJ0HRA0bxpo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caed9884f2.mp4?token=U3JDUoR-vIoHaLDwfJG26hydY2ytEBOMCmEvhhCWl63Y1_VKEo6X8YsUrNRUK1HhP-_JXmyg0-A-A6a3YK-YyDJtfhKPBMMIXD9G-pWJYfgibhibmq5xg_SxF7zSWAxQMzU0wN_99oV8AIf8fi_K1nfdbXJuxrsgo8jcIGchhPxs_bSSwYussPaYd0umHYZCabmxWWmha2kiURjdjqgQ9BCGFnEMi3oSgmZ55X4PUAkZvYQ-KAJpSGQ1fRhPbXUFd2J_pjo52X8M21RyTHsbEHxyd_8kQUz_chDrZ8m_IthNgLtQaKq7i8cCq26jQHOepP2eZjIKdt7bw_h46OWbgaBDDGyANddcxvDdaRNDM9hyEL_I49d_ttkjgc7tRowKBTSjDvvzb_uWqQAgtO9X4WJavS7sDj_WvASQE7Kk-JPajKoynJH40-FpeRe4CcFIJo0HS85iSWOT94CdLZDhD13o4oDT7fZjB_y9TKu-v_uFOA8x9EBBOYohoLhlR7ZGewUXfHxJveqFq-7nREo8dFV6cpR2-3VUkje-NoV_Up8SUqQbiRGxYLhmYWyc5B91m9oTULucQYY4vHocL9QkdEJXhR5yyJKP--oesgrMhwar0gfN4n7ugqg_4LAvxf1uytmHNA6PAkLG5SLmtb4hXPo6WBA2fYajUJ0HRA0bxpo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از مانور مشترک نیروی هوایی ترکیه و مصر که در مصر برگزار شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/alonews/129576" target="_blank">📅 18:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129575">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مذاکرات دو ساعت دیگر به اتمام می‌رسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/129575" target="_blank">📅 18:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129574">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزیر انرژی آمریکا به ای‌بی‌سی:
۶۷ کشتی دیروز از تنگه هرمز عبور کردند و حجم نفت در حال عبور، نزدیک به میزان پیش از جنگ است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/129574" target="_blank">📅 18:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129573">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
سفیر ایالات متحده در اسرائیل:
آمریکایی‌ها، چه درک کنند و چه نه، باید به خاطر مردم یهودی به خدا سپاسگزار باشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/129573" target="_blank">📅 18:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129572">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سفیر ایالات متحده در اسرائیل، مایک هاکبی
:
آمریکایی‌ها، چه درک کنند و چه نه، باید به خاطر مردم یهودی به خدا سپاسگزار باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/129572" target="_blank">📅 18:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129571">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
فوری / ترامپ: نزدیک است که مسئله حزب‌الله را به سوریه بسپرم
🔴
آمریکا ممکن است در آینده در صورت لزوم تنگه هرمز را تصاحب کرده و عوارض دریافت کند
🔴
این به معنای حضور آمریکا به عنوان «فرشته نگهبان» تنگه هرمز و خاورمیانه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/129571" target="_blank">📅 18:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129570">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBgyHKWegjXuCO_-GCW8JDRAji9FVBCFqdhmF7l4JMJTHAea3oWLFkhHbjiR3GSUArsJ3ZVRJLCOCyKkm9i4vPC-wkFENX_IL9ouQk0Qyi4ETQMlyVrVbsnh_rO7cDShIfB1eV15yhDcCQA7KPUgUuiH8r1S22_pLTm7rhR0BgOkun2cvZz1EXPhzzkZwk0Vz0ZNITMJjQbGFFsheWUAW9OtIEGqbtQR5PV9rMMRLcKAxOz8Wr-FNLAA9f5D33ojni-sTfM4paAdOUmPJFgXSSwbtrtfYkFnfnYVQ6D6mz1ONyef29-3RBRz4sbgJcWhTvolFWtfoY103G8yxvNFRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بند اول تفاهم‌نامه اسلام‌آباد: جمهوری اسلامی ایران و ایالات متحده آمریکا متعهد می‌ شوند از تهدید یا استفاده از زور علیه یکدیگر خودداری کنند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/129570" target="_blank">📅 18:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129569">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMSpA1YUnc4i47AqprSvDj2tvlj9lmmXpDv3GpJK6NvdAjz6uihya4NT-81Nac5RU9yF_CKKIgDpKW61hyUSxc25_pgRK6Sj6b9jGh3Dx9iDtfLyhHLPpjluSPAoxe3Xzg-oL3cxLDMlb3lkW5-9Pti7n0h6cCOq8TpwYyoF16eZ6PMYOi-TZzJzRI5sa2sBPbaJkmVA7EAlhJ_cW2DdaHUhqdWMBRezGbOAdZU2pix_irfT2niLQYcVsm3EuArmQuEB4ISj52eBTCgxH6F7KEjtPuJGTUCP6ThtMz2D5KrHkylm5T8IS31OhL4SXMRNp0OIkMr181ZP7oyTRMR_ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی هوایی اسرائیل به
اردوگاه
البریج تو لُبنان، حملهِ کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/129569" target="_blank">📅 17:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129568">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ef202698d.mp4?token=dNPB6p4HjeZu2nh7eNhu9UgGE9ksQWbMRr5UNFfHgqwbEtemkwTjSKKpUuLYKmfZPSjqC-8KjXt7VvREOxsVZaf80fWBbT28MWpDIN9GRPcoKYrllGl_9wRRYLQAkvW9uYIFJIcA87oZ4jadidrUB-wPaia4ViQpxdfat2yWUhNPg76FgcJNX-C_Ekll1Xbv37_ryTYlmmUYZEhUntTRbjfnrCyEJ-l-d-4MrVZX7IZ6tww8jQ8y78XYyYvNFl2UVnM6sxF4O7dMjppj2yorysYTc0h4yGgdbewX6bGDs8PcGPoBLlO-yb7CpGNX3d2gYzooX-DC5jMTw86-Lbuvmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ef202698d.mp4?token=dNPB6p4HjeZu2nh7eNhu9UgGE9ksQWbMRr5UNFfHgqwbEtemkwTjSKKpUuLYKmfZPSjqC-8KjXt7VvREOxsVZaf80fWBbT28MWpDIN9GRPcoKYrllGl_9wRRYLQAkvW9uYIFJIcA87oZ4jadidrUB-wPaia4ViQpxdfat2yWUhNPg76FgcJNX-C_Ekll1Xbv37_ryTYlmmUYZEhUntTRbjfnrCyEJ-l-d-4MrVZX7IZ6tww8jQ8y78XYyYvNFl2UVnM6sxF4O7dMjppj2yorysYTc0h4yGgdbewX6bGDs8PcGPoBLlO-yb7CpGNX3d2gYzooX-DC5jMTw86-Lbuvmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیبر امنیت داخلی آمریکا، مولین : شاهد افزایش غیرعادی شهروندان ایرانی هستیم
🔴
اونا سعی می‌کنن از مرز شمالی آمریکا، نه مرز جنوبی، مخفیانه وارد کشور بشن
🔴
این موضوع نگران‌کنند‌ست برای ما
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/129568" target="_blank">📅 17:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129567">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
سازمان دریانوردی بریتانیا: گزارشی از حادثه‌ای در ۵۰ مایل دریایی سواحل یمن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/129567" target="_blank">📅 17:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129566">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
رئیس ستاد کل ارتش اسرائیل: آتش‌بس اعلام شده در لبنان شکننده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/129566" target="_blank">📅 17:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129565">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKTk1evUmfsTUJyJ_GS3UVCWPqRuEBl92uOKb5rSZcndS-6PkFXZ3wmvo-93K0O2p5qasvCG9J8VpGrgLrVdLlN1CUzgo2ReXvVBCC_4_Gez0jpOi5I7kOYYhrOf8-3x0QvlvYdxr4dDUnTkjULwYIC1XLFlnvjHwNZ2ffUAg7hNnpY8Rh2UEK0e0hUFeeWKR-NC8i-YiEarZsSU5WIv1DXwSB3DY9qMyT5lyMQyZ0UyDEucyctpRcmAQ9VcldGKCnYCl1qx9FKb1qLcB3mdWX0w7KiGP21il0AH2U4ktnvCPYJrdOy1yXGeE6jz1aZCYqNBBFV5Sd5XNy7gnFjtkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: کیر استارمر از سمت نخست‌وزیری بریتانیا استعفا خواهد داد.
🔴
او در دو موضوع خیلی مهم به‌طور بدی شکست خورد — مهاجرت و انرژی (باز کردن استخراج نفت دریای شمال!). برایش آرزوی موفقیت می‌کنم!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/129565" target="_blank">📅 17:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129564">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IILiHMq4cfg5UNYRxz62AVtw1ycAjpktMmeAsgQA2hywgCHz-tQIIBwHgmz2UjnvbjymnQON3nlM2s_9lV6R13Jshm1zQo0f_hW-bbwc6IGRyzGrU_sLUGkFa3ZsQXkMBpsjP-9i0zR-Y8-ljCS1Ri4KOB5YpeokYUZKyo9dKPHZ-jSfLZ22drBWD4HkTOAxPFRz3AKwi5g277sLxVHrO6aq98I9mjdKxDlszbZybcU5bTR2ecHmQgSQDBoi1x_iywu_Dl7xSBTYOBZIZR8J3Ondlfyzt2w9iaVxBMqgzwBUpl3o5gyJMe8_Kbn_PW89yQTGYLJd2pP6sT2Jvp7W-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی، عضو سابق تیم مذاکره‌کننده در واکنش به توییت ترامپ در مورد عوارض تنگه هرمز: هزینه‌ای دریافت خواهد شد، این قطعی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/129564" target="_blank">📅 17:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129563">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فوری/ترامپ: یادداشت تفاهم صرفاً تمدید آتش‌بس است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/129563" target="_blank">📅 17:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129562">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6305ad17ad.mp4?token=gyZd4fHhHXmwewMLkJWfDxtSJqd7lOLh1yaD0Qf4zIRFFAXw0-RvWeu0qx0F1PgrO1mbF-UhpwW8-ycyRmIPjKHr4-KU4F3VhLkvgzP8mLNo4MZ6PqaOUomglFblqshDO1fwjae0Utp6bd_wbHp8lfmzNainM9YcVSxelPmViZUTibBpPf6q2GDwGuH8zEjvfxjbpEIBuPrDz0XCfkd8wjfafub5eASmEtXsBlg3Amfz-9MU2o7AEbjNhzA2wzFRZKyykveLaPNGqvM5Klel8RlCn0dHu3sV0LHq6z6-TGqVXPFQpJcTxc3iAccCukTqbglPcHtlC2ic8Pn18Djkdx1k82izHoNLAWondv4XPkhMZwXFJSx-6oJCrtitLDA8-8Za7cWWMWEfBtbcYNA5KTNRPwY2Iv7uw2hKsmV5-RlXNzHHSxY4f2zFYdV1tEMRVMSNuMCNtftBsfbrDJYsZqyjFKUlbzhzFUe99DZQozucWOcr25xSzqwlBQegqfFHVht3IQLPxXfgfgsKIYpsF2_xCBzfXhsLV8_RiXkVC5YvC5cTPhTeR4qV9n9DxZE-fMM7KNO09PBxDy87AQtjNzxs5rxv_eR4Rk5BotuXpslGziVW0szBBUxvGGkeVa3bxRubJ8Fh7qXQFhK4izAgo6QVk2oaBQKh-ATDKtBR6Sc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6305ad17ad.mp4?token=gyZd4fHhHXmwewMLkJWfDxtSJqd7lOLh1yaD0Qf4zIRFFAXw0-RvWeu0qx0F1PgrO1mbF-UhpwW8-ycyRmIPjKHr4-KU4F3VhLkvgzP8mLNo4MZ6PqaOUomglFblqshDO1fwjae0Utp6bd_wbHp8lfmzNainM9YcVSxelPmViZUTibBpPf6q2GDwGuH8zEjvfxjbpEIBuPrDz0XCfkd8wjfafub5eASmEtXsBlg3Amfz-9MU2o7AEbjNhzA2wzFRZKyykveLaPNGqvM5Klel8RlCn0dHu3sV0LHq6z6-TGqVXPFQpJcTxc3iAccCukTqbglPcHtlC2ic8Pn18Djkdx1k82izHoNLAWondv4XPkhMZwXFJSx-6oJCrtitLDA8-8Za7cWWMWEfBtbcYNA5KTNRPwY2Iv7uw2hKsmV5-RlXNzHHSxY4f2zFYdV1tEMRVMSNuMCNtftBsfbrDJYsZqyjFKUlbzhzFUe99DZQozucWOcr25xSzqwlBQegqfFHVht3IQLPxXfgfgsKIYpsF2_xCBzfXhsLV8_RiXkVC5YvC5cTPhTeR4qV9n9DxZE-fMM7KNO09PBxDy87AQtjNzxs5rxv_eR4Rk5BotuXpslGziVW0szBBUxvGGkeVa3bxRubJ8Fh7qXQFhK4izAgo6QVk2oaBQKh-ATDKtBR6Sc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: اگر لازم باشد ممکن است تنگه را تصرف کنیم. من آن‌ها را کاملاً نابود خواهم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/129562" target="_blank">📅 17:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129561">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11fa55788.mp4?token=RRXNXEaz_SYlKywufn-EVwIVDpVF7Jvq-fkL8Wofi4Lb8X4lJFVeCUrKtV0GlzOaGHraNplAvt8OVTURTrrdaAvTCYky8W0-DUTpcZe7lYBLaxGnemyFM_GZp7YPB4BCODXbgj6IiZRGqsNBQqtGMjDyvR0MTcrPX7wPNpTGRP-GCpxLDlY3-HF_DNh98tZJ4Uzy3c9K_n6Rvmvkmyz5AY5B50R-nNqm9vEcGT-jE6aptbxkgmdFd4cskqmir3kscu1S6B5PS0SBdGhpdIRsnWnHjIm9UUks9v7bT8WSJdnYmusc6VJ9DHlliHG-pY-osYlXdv4IK7tVPmJB5LrxB74EBNlluYwP5SRFe4RLyfdIvJ677P_94Gwl7C54X1139x35ZBp3UbDksA2Dl8L3WZ0o4YD_9IDKI4IAGxc9O53xcaUABshrSadX1CGF03rBjzhgKT1W_vYEdVsMZQEzXhx9hvViSxwst_B2eyY3wRiivPmmTwJyaXcXYW4S02Dx4DxEn4JmyKwKV7edg4rcbSPh1pFFVHj1VdPiJJII1kZo7ScuDmH06nZJW_UF3ExSQlkPF-eUCn-cQMVsQI1a3M99p8OlHam1bTuzmcoGlAiM1XKmjPPDzdPvlJLw6E8JMSgfQQUl3Xd-SJlQlMgiHg54l5c-glXJAFqODGvbgCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11fa55788.mp4?token=RRXNXEaz_SYlKywufn-EVwIVDpVF7Jvq-fkL8Wofi4Lb8X4lJFVeCUrKtV0GlzOaGHraNplAvt8OVTURTrrdaAvTCYky8W0-DUTpcZe7lYBLaxGnemyFM_GZp7YPB4BCODXbgj6IiZRGqsNBQqtGMjDyvR0MTcrPX7wPNpTGRP-GCpxLDlY3-HF_DNh98tZJ4Uzy3c9K_n6Rvmvkmyz5AY5B50R-nNqm9vEcGT-jE6aptbxkgmdFd4cskqmir3kscu1S6B5PS0SBdGhpdIRsnWnHjIm9UUks9v7bT8WSJdnYmusc6VJ9DHlliHG-pY-osYlXdv4IK7tVPmJB5LrxB74EBNlluYwP5SRFe4RLyfdIvJ677P_94Gwl7C54X1139x35ZBp3UbDksA2Dl8L3WZ0o4YD_9IDKI4IAGxc9O53xcaUABshrSadX1CGF03rBjzhgKT1W_vYEdVsMZQEzXhx9hvViSxwst_B2eyY3wRiivPmmTwJyaXcXYW4S02Dx4DxEn4JmyKwKV7edg4rcbSPh1pFFVHj1VdPiJJII1kZo7ScuDmH06nZJW_UF3ExSQlkPF-eUCn-cQMVsQI1a3M99p8OlHam1bTuzmcoGlAiM1XKmjPPDzdPvlJLw6E8JMSgfQQUl3Xd-SJlQlMgiHg54l5c-glXJAFqODGvbgCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در واکنش به حرف پزشکیان که گفته بود «از حق غنی‌سازی خود عقب‌نشینی نمی‌کنیم» گفت: بهتره مراقب حرف زدنش باشه. بهتره رفتارش رو درست کنه، وگرنه بقیه کشورش رو هم در اختیار می‌گیریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/129561" target="_blank">📅 17:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129560">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
نخست‌وزیر قطر: ما شاهد فداکاری و تلاش‌های بزرگی از سوی ونس، نخست‌وزیر پاکستان و وزیر امور خارجه ایران بودیم.
🔴
آنچه امروز در این نشست رخ می‌دهد برای امنیت منطقه و جهان اهمیت دارد.
🔴
نشست امروز تنها آغاز راه برای تحقق اهداف است.
🔴
این فقط آغاز است و ما برای آینده‌ای بهتر برای منطقه‌مان تلاش می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/129560" target="_blank">📅 17:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129559">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gA51k04LquzDbroSFR8cIQtCei-Nqyy7Pjw48rtmKnZgmX4mreH4bAxRSUwYeYvuLndoHk3acVuheyd8H-HzbopCLYLKUNmSRJH0mcaD-aPcj3ZKq7geVQLGZ4vgp4n9iGXsktBcoqKTrlSk8lY5zwjbVctCow1c0MuCl1KrjZ7fbf8HBpgas2geA_RUqJ81aWQtqSGdCuoBmUuww0hwFrLwhbDYLcnvU8fVub4PDXYus6sohI4YlUux0sLtGL0v0gBEFyP_Gt7MKKM8geFNAvG8VmtsGL7YdC-NYZtFw0gd53jV1F8Qfip0FXpzSBmPMFCxwZwn-kQAjN_LBsFKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ :  ایران باید فوراً جلوی دردسرسازی نیروهای نیابتی پردرآمد خود در لبنان را بگیرد. اگر این کار را نکنند، ما دوباره به ایران ضربه سختی خواهیم زد، درست مثل هفته گذشته، فقط شدیدتر!!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/129559" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129558">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b4fe6074.mp4?token=RqRKLJXOgBYx-e-PnmE_0zpKWy9BVfKeGFAckNYYHPc59vMN0BrpZfv-3vbCpW07wRT4QYm3BYUDBZe8eZbFdSUWajpL5O7r5TMKkjb6P1b63Ob3aTYuFOwqoEYgfxtgSse21oTDiHYsmnD-PF968iWG7h6bIexy-hyt3FmmgiJgP7Ksvmo6UHoBM0qcmN6BsarKeHFOtwAaqjYfVzXKTUkh3bVDwD4y6UHmbA6x_uslN875I8MlvMTJbPM5ntdX-iNiAgYx7_oiXODaFqjrT8D-RxsUaUu0W6IwWZQN5hPV_HBmmRr6mpiQxvv9bHdvHFBlW8Y4W3Ddph_tEdcIVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b4fe6074.mp4?token=RqRKLJXOgBYx-e-PnmE_0zpKWy9BVfKeGFAckNYYHPc59vMN0BrpZfv-3vbCpW07wRT4QYm3BYUDBZe8eZbFdSUWajpL5O7r5TMKkjb6P1b63Ob3aTYuFOwqoEYgfxtgSse21oTDiHYsmnD-PF968iWG7h6bIexy-hyt3FmmgiJgP7Ksvmo6UHoBM0qcmN6BsarKeHFOtwAaqjYfVzXKTUkh3bVDwD4y6UHmbA6x_uslN875I8MlvMTJbPM5ntdX-iNiAgYx7_oiXODaFqjrT8D-RxsUaUu0W6IwWZQN5hPV_HBmmRr6mpiQxvv9bHdvHFBlW8Y4W3Ddph_tEdcIVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: دیروز ۱۹ میلیون بشکه نفت خام به دلیل این تفاهم‌نامه با ایرانی‌ها از خلیج فارس خارج شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/129558" target="_blank">📅 17:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129557">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: دیروز با مقامات ایرانی صحبت کردم و به آنها در مورد بستن تنگه هرمز هشدار دادم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/129557" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129556">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ترامپ: من یک گزینه ۶۰ روزه دارم؛ بعد از آن می‌توانم هر کاری که بخواهم انجام دهم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/129556" target="_blank">📅 16:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129555">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
تسنیم: هیات ایرانی با عکس مشترک با هیات آمریکایی مخالفت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/129555" target="_blank">📅 16:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129554">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
صدا و سیما: خروج خبرنگاران در پی شرط قالیباف برای عدم حضور رسانه‌ها در این نشست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/129554" target="_blank">📅 16:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129553">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
جی‌دی ونس: باز شدن تنگه هرمز و متوقف کردن برنامه هسته‌ای ایران، کارهایی است که همین حالا به سرانجام رسیده. حالا سؤال اصلی این است که چقدر می‌توانیم جلوتر برویم و دستاوردهای بیشتری داشته باشیم. آیا می‌توانیم روابط منطقه را برای همیشه متحول کنیم، یا دوباره برمی‌گردیم به همان روش‌های قدیمی؟ روش‌هایی که دوست نداریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/129553" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129552">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: اگر ایرانی‌ها تنگه هرمز را ببندند، کشورشان نابود خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/129552" target="_blank">📅 16:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129551">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان، شهباز شریف: از رئیس‌جمهور ترامپ به‌خاطر رهبری دوراندیش و بسیار پویا تشکر می‌کنم که منجر به برگزاری این جلسه امروز شده است.
🔴
فکر می‌کنم اینجا قرار است بحث‌های فوق‌العاده‌ای داشته باشیم که امیدوارم در آینده به نتایج بسیار مثمر ثمری منجر شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/129551" target="_blank">📅 16:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129550">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
دقایقی پیش نشست چهارجانبۀ ایران، آمریکا، قطر و پاکستان در سوئیس آغاز شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/129550" target="_blank">📅 16:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129549">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ونس: هدف ما تغییر شکل خاورمیانه از طریق دیپلماسی مشترک است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/129549" target="_blank">📅 16:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129548">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
جی دی ونس، معاون ترامپ: پیشرفت قابل توجهی در ساعات اخیر حاصل شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/129548" target="_blank">📅 16:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129547">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ونس : همه رهبران بزرگ دنیا اینجان
چون ایشون به ما قدرت داده که راه‌حل دیپلماتیک برای کلی از مسائل مهمی پیدا کنیم که برای مردم آمریکا مهمه
🔴
ولی فکر می‌کنم برای کل دنیا هم مهمه دولت باز ما حرکت می‌کنه و برنامه هسته‌ای ایران رو ادامه می‌ده
🔴
همه این کارها از قبل انجام شده
🔴
سؤال الان اینه که چقدر بیشتر می‌تونیم با هم انجام بدیم؟
🔴
می‌تونیم ورق رو برگردونیم؟ می‌تونیم تغییر کنیم؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/129547" target="_blank">📅 16:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129546">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQWr_yjCB096OYvr6txnVKsQwlBfAM0dJ8-mRGaxnM-8OTX37h46TnTs2-SO0ZXJ0wE-w-_mY_QfgYJkOZhPW3ob8SnE9aNDMiXB8YfoJdOgJzukYUtDdAp9fTp6WG_jhmp7U3JCZ4jxMpdaiJDzbPnezFojPX6XKwT4_26mZn-uXm4p1ohiNZJJXTLFpPlsCNK74icD-plpzqi6NT93fBYOEQlj7OjgnZKxLyTNAkccUNk9t-go007yFiBv8G2-0GeDbvY2XjAHR7kdNy-Lsl2PzlM4sQtE9FWYI0PoQjX2nXB5u-dX_rZZJE2aBFhDlCCPqCPJyVqcmuciAIqy7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاهش قیمت تتر همزمان با شروع مذاکرات مستقیم ایران و آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/129546" target="_blank">📅 16:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129545">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ایلان ماسک : هوش مصنوعی داره جای و شغل آدما رو میگیره، واسه همین دولت باید مستقیم به حساب مردم پول بریزه تا اقتصاد فرو نپاشه و تبعات هوش مصنوعی جبران شه. حالا با تولید ارزون و انبوه توسط هوش مصنوعی و رباتیک، تورم کاهش پیدا میکنه و حتی ممکنه دچار تورم منفی بشیم، پس دولت هم چاره‌ای نداره جز اینکه بین مردم پول پخش کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/129545" target="_blank">📅 16:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129544">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
فایننشال تایمز به نقل از دیپلمات آگاه از مذاکرات: میانجی‌گران ابتدا درباره سازوکاری برای نظارت بر نقض‌ها و حفظ صلح در لبنان بحث می‌کنند
🔴
در مورد اعزام هیئت ایرانی به سوئیس، مقامات قطری به ایران گفتند که اگر هیئتی اعزام نکند، عملاً به نتانیاهو «حق وتو بر جنگ» را داده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129544" target="_blank">📅 16:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129543">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
گزارش تازه دیلی میل به بررسی احتمال تغییر رویکرد روسیه در جنگ اوکراین و بحث‌های مرتبط با استفاده احتمالی از سلاح‌های هسته‌ای توسط مسکو می‌پردازد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/129543" target="_blank">📅 16:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129542">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
مصر، ترکیه، عربستان سعودی و پاکستان بیانیه‌ای مشترک صادر کردند.
🔴
در بیانیه مشترک وزیران امور خارجه مصر، ترکیه، عربستان سعودی و پاکستان آمده است: بر اهمیت دستیابی سریع به پایان مرحله بعدی مذاکرات تأکید می‌کنیم.
🔴
تأکید می‌کنیم که تلاش‌ها باید نگرانی‌ها و ملاحظات کشورهای منطقه را در نظر بگیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129542" target="_blank">📅 15:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129541">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
وب‌سایت «زتیو» به نقل از منابع آگاه: ترامپ به شدت از نتانیاهو عصبانی است؛ او گفته که دولت اسرائیل سعی دارد او را فریب دهد تا دوباره جنگی تمام عیار با ایران راه بیندازد
🔴
رئیس‌جمهور آمریکا به شدت در این باره فحش می‌دهد.
🔴
در حال حاضر، او قطعاً از اسرائیلی‌ها بیشتر از ایرانی‌ها عصبانی است
🔴
حملات مداوم اخیر به لبنان، ترامپ را بیش از پیش به سمت مخالف فشارهای تل‌آویو سوق داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129541" target="_blank">📅 15:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129540">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emQtrb9-JwCnuYW_qqIp5YY_F4pCOKd_gqdKROQKFBlYwTODh4HzVTYXCztVTbE7do_ZvthA1u7OSZs5D3APhwLE5ORjNnlIJhm5waGzenEkVTMZ1rm8oKwVaRO8EjZFukYN8EH9oMpv0eV3NhuGLeaZ_YD8dQo57Ls-YeStWcfy9yXbX9TUozu9mAJcSPZtPOakZsgyBnMI-oxfZ_0n7sONyllnFzvjX3eusSpTQXsk5w20MvL2hJcrklDJUSLPr7cGzJLUzQ1xk9uNHbnMPqJO5J3XOI4wrzgE6S3Wh76L1Rk7MQbv0rhhByqqfr1TfI2pwiO_x6zDjpQYi7FvyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ روز پدر را با تبلیغ دولت خود تبریک گفت: روز پدر مبارک! کشور ما عالی عمل می‌کند. تعداد مشاغل و بازار سهام رکورد زده، بهترین اقتصاد تاریخ! بزرگترین ارتش جهان، تا به امروز. ما در همه جبهه‌ها پیروز می‌شویم، پیروزی‌ای که هرگز سابقه نداشته است. خدا همه شما را حفظ کند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/129540" target="_blank">📅 15:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129539">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
امارات به عنوان اولین کشور عربی، استفاده از شبکه‌های اجتماعی رو برای افراد زیر 15 سال ممنوع کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/129539" target="_blank">📅 15:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129537">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06cd39a29.mp4?token=h5Mk7o3qluMmrIWNK2ND_TOcOYk0kiOPa05ybAf2YAH1WH_30yoBgn33wQUG7LVJiR1w6nfYyRjw8d3o-DzIDUE2RUZFvhEpdo3k8KRmJwmtnIWIt5jK-2DascvR7dkEQ_-P8wl7htArv-XApBLM4hDYgHuYXxcPQTezXwffO0bWWLGlzANwgbgDWz4ftSj-6mhlWvAd0YhCu_81402HsSVfeyTOO6nq0Qj_uuPSdvB5NFxTRUMj_lYTSgvIY5EDv-VbcNSG8oZnUhCK6Am-vzo-gB4WNPXH_tO1BoWpEHUwtG6CUZFICEo1-RS3pCp8R5wkyywqlNmSsE9iSsmjTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06cd39a29.mp4?token=h5Mk7o3qluMmrIWNK2ND_TOcOYk0kiOPa05ybAf2YAH1WH_30yoBgn33wQUG7LVJiR1w6nfYyRjw8d3o-DzIDUE2RUZFvhEpdo3k8KRmJwmtnIWIt5jK-2DascvR7dkEQ_-P8wl7htArv-XApBLM4hDYgHuYXxcPQTezXwffO0bWWLGlzANwgbgDWz4ftSj-6mhlWvAd0YhCu_81402HsSVfeyTOO6nq0Qj_uuPSdvB5NFxTRUMj_lYTSgvIY5EDv-VbcNSG8oZnUhCK6Am-vzo-gB4WNPXH_tO1BoWpEHUwtG6CUZFICEo1-RS3pCp8R5wkyywqlNmSsE9iSsmjTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت فعلی در سوئیس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129537" target="_blank">📅 15:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129536">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2df66b5d.mp4?token=JQRfsbKWlfoIpzOYhh1I3ffF-fxjCLsIYH24OjSuFhgBO1nTKloQlVh8i15Nutskcb2Ist_VUsiB7kWa_ccv_ioMVRlIMgLJF-EEamBJUiVLHcCwsf_xRUJT3z3u2VFJl_4NRKM22z1m0vFmcqG2vonFkd5jgmk7_BHnMUBlJz7remN4G7TKHMi1A0SG4E1EKIGcpwGVkBU5ipjhEBAcE96V-Di94YGm0d8hxrhBQl5FuqD7ukIObQcjvOVmx3gLrOADB0s8S9l_L2c-Ddf8Vw4aQQ7Auz_ktN1xZOSJQdm7ta2ixLgelg6x1I7trErM8-VX-kobdMIOpJzpVhN3Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2df66b5d.mp4?token=JQRfsbKWlfoIpzOYhh1I3ffF-fxjCLsIYH24OjSuFhgBO1nTKloQlVh8i15Nutskcb2Ist_VUsiB7kWa_ccv_ioMVRlIMgLJF-EEamBJUiVLHcCwsf_xRUJT3z3u2VFJl_4NRKM22z1m0vFmcqG2vonFkd5jgmk7_BHnMUBlJz7remN4G7TKHMi1A0SG4E1EKIGcpwGVkBU5ipjhEBAcE96V-Di94YGm0d8hxrhBQl5FuqD7ukIObQcjvOVmx3gLrOADB0s8S9l_L2c-Ddf8Vw4aQQ7Auz_ktN1xZOSJQdm7ta2ixLgelg6x1I7trErM8-VX-kobdMIOpJzpVhN3Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شوک در حزب‌الله
گزارش‌ها حاکی از آن است که محاصره ستاد کل حزب‌الله در جنوب لبنان و در ارتفاعات «تپه علی طاهر» در حومه نبطیه، باعث بهت و سردرگمی در میان نیروهای این گروه شده است.
بر اساس این ادعاها، نیروهای ارتش اسرائیل موفق شده‌اند به یک مرکز فرماندهی زیرزمینی و ستاد اصلی حزب‌الله در جنوب لبنان، که گفته می‌شود با حمایت جمهوری اسلامی ساخته شده، نفوذ کرده و آن را تحت کنترل بگیرند.
این محل پیش‌تر در دوران حیات سید حسن نصرالله به‌عنوان یکی از پایگاه‌های مهم معرفی شده بود و در همان زمان نیز موضوع رونمایی از موشک «عماد ۴» مطرح شده بود.
در ادامه این گزارش‌ها ادعا می‌شود احتمال گرفتار شدن صدها نیروی حزب‌الله در این مقر وجود دارد و گفته شده ممکن است تعدادی کشته یا بازداشت شده باشند. همچنین اخبار تاییدنشده‌ای از بازداشت حدود ۳۰ نفر و انتقال آن‌ها برای بازجویی منتشر شده است.
حزب‌الله در تاریخ ۱۸ آگوست ۲۰۲۴ از شهر موشکی «عماد ۴» رونمایی کرده بود؛ اقدامی که در آن زمان به‌عنوان نمایش قدرت و پیام بازدارنده علیه اسرائیل مطرح شد.
در حال حاضر نیروهای اسرائیلی در حال پیشروی زمینی در این منطقه هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129536" target="_blank">📅 15:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129535">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
گویا علی الاصول راجع به مسائل هسته‌ای هم مذاکره خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/129535" target="_blank">📅 15:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129534">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزیر خارجه پاکستان: آمریکا درخواست انتقال ذخایر هسته‌ای ایران را مطرح کرد و ما به راه‌حلی با عنوان «کاهش سطح غنی‌سازی» رسیدیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/129534" target="_blank">📅 15:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129533">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtg-0jfbL9xdh_w-V4ngVrrnNy5ml_DLjlm4UW8n9Wa9s14EMFsN_qY9mHbIG1YvHiUq-3IpI340O_xPeRVyNt2n7nDN1jmu5N5lJUKdGBAxbJEICRumO2roxC6OLk7NoXXQd_046vzNaRDhTE17AWerNIBQZq3_NzS68C1uBCcfSd-C5F_1N16jo3wSNzXM9kc2RywJf1-ZdRbbrMenrfGJE_71_1l6vH01L2B1U7IObha1pebsoN_RQ6aAXx6preJLN192iRNHkjns-s4T_6p5Y9qB9lhzTjwVEXqcfw6oTmZz3cTsSzf135IDwIVSEpep1dyxyeUBVWvcGiChXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون سوئیس، جمع پایدار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/129533" target="_blank">📅 15:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129532">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UW_tw_LAnWZ88mAXBnJV1KhEFx_1XOmoxO1lVNAp0FJnaqn3sH9Jmo716EF4ep55d3DKdm6uSupDgaGjtmagIk7-n9jx3icd2hnaO7Rx1NToobuJp9CmyTlT4f1mGTOXCsQqhu3i-GKhzYau-k7zuAQm3oonWmn4F-wnuCqUIgA3-Pb4EiERmuVRovPyWgT3F8KN3g_qxb5AwKXk1jMxNNlPaMNxKh3Tehbxv8UTWpCGqMN2qvmgLfH6TTQesgSPbzNXFkxH8ltTV7fI8OM_deEyDpgKhFww92Dj_5NI8ctggexJ0l-0oT6ZgSn4jCLxWiwmAH1HBikZOAzggP3TUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت عالی سد کرج
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/129532" target="_blank">📅 15:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129531">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وزیر خارجه پاکستان به الحدث:
🔴
ما موفق شدیم آمریکا و ایران را به گفت‌وگو ترغیب کنیم و به آتش‌بس دست یابیم.
🔴
ما توانستیم آمریکا و ایران را برای نخستین بار پس از ۴۷ سال پای میز مذاکره بنشانیم.
🔴
ما در هماهنگی با شرکا و متحدان خود این میانجی‌گری را به نتیجه رساندیم.
🔴
جنگ میان آمریکا و ایران فاجعه‌بار بود و تأثیرات منفی شدیدی بر اقتصاد (منطقه و جهان) داشته است.
🔴
سه تیم فنی در مذاکرات بین آمریکا و ایران مشارکت دارند.
🔴
کمیته‌های فنی در حال بحث دربارهٔ پرونده هسته‌ای، دارایی‌های مسدودشده ایران و موضوع لبنان هستند.
🔴
در طول دورهٔ ۶۰ روزه، هیچ گونه عوارض عبوری در تنگه هرمز اعمال نخواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/129531" target="_blank">📅 15:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129530">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
برگزاری نشست سه جانبه ایران، امریکا و قطر با موضوع لبنان و اموال بلوکه شده
🔴
نشست سه جانبه ایران، امریکا و قطر با موضوع آتش بس فراگیر در لبنان و اموال بلوکه شده ایران هم اکنون در محل مذاکرات در حال برگزاری است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/129530" target="_blank">📅 14:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129529">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
خبرنگار صداو سیما: یک دور رفت و برگشت پیام با واسطه پاکستان بین دو‌طرف انجام شده یک دیدار هم با هیئت قطری برگزار شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129529" target="_blank">📅 14:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129528">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
اسرائیل کاتز، وزیر دفاع اسرائیل، اعلام کرد که ارتش اسرائیل (IDF) همچنان برای مقابله با تهدیدات در لبنان آزادی عمل کامل دارد؛ این اظهارات پس از پاسخ گسترده اسرائیل به آخرین حمله حزب‌الله مطرح شد.
🔴
او تأکید کرد که نیروهای اسرائیلی در منطقه امنیتی واقع در امتداد مرز باقی خواهند ماند و اسرائیل از جنوب لبنان عقب‌نشینی نخواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129528" target="_blank">📅 14:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129527">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBInMfR6k1-1n_UrEehJtTDjJNUfkUdow6ZjHsZE8EH2WP-qARJygd_skIYESpYnC8dDzaVhWvK5dNcv9YWG6hKXhiSMFiPSomso-FHY7Vyvak7xLCEMqivQgCEhfimNxscMt-YMZQkB40JGQdaG0b2uVf2tB-2HOBv8fTmgcXMaDk0_Xtbe9weHxgih_IuQEoRscxPqR3y9LSq4IiH1mP0zmkvlOBSOJVtRh-vkImiAm3adAZZsW98WDyJIfLgxCsTmJbzSKGrtPKQn3CrL-CCW1HQasvPpDl-swIbVDWNwscctDMAbZNfXKNCqm9d8nuMIMfwNtDODtJPXLnZVNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بقایی:ایران مصمم است روند اجرای تعهدات طرف مقابل را با وسواس و جدیت پیگیری کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/129527" target="_blank">📅 14:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129526">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
پزشکیان: ادامه جنگ به نفع هیچ فرد یا گروهی نیست
رئیس جمهور:
🔴
ادامه جنگ به نفع هیچ فرد یا گروهی نیست. بر اساس همه تحقیقاتی که در جهان انجام شده است، هر جنگی موجب اختلال در رشد، توسعه اقتصادی و اجتماعی و افزایش فقر و بیکاری می‌شود.
🔴
این سخن به معنای ترس از جنگ نیست. ارتش، سپاه، نیروهای هوافضا و مردم ما نشان دادند که با قدرت در برابر تجاوز ایستادگی می‌کنند و اگر جنگ ادامه پیدا می‌کرد، با قدرت می‌ماندند و مقاومت می‌کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129526" target="_blank">📅 14:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129525">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjrjnvKteWIN3RYTWBwInNWKjzUfK9mEJ2zRfH4F4J0ETIDMliGDXgCpACDx_mrl1403DY7ffKtmMJKkRCOG8XyrVx_-GwslkIeVwnehRoYmHoZv2FJUTy6oHbLNzjd2w4us7wiPOumD3Q6g793VBK6H6E99nII32L3RBRB1ux6fPReI3VgrPKOTtoAgHqZWOomgxgd61M2xge0O_-sTXpv89tgNWTYFXtPZsOaPHCdaNs8TTpbP0FgjiRmz9QfVbVXmFcprmx_7QsIGT0WBsEGwj53pSDnLx37YiiRr_V8kxyKraRhqFwh3OwJ5ieKU652S4oc3Yxt0BETSvKq-Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیام ایگنازیو کاسیس وزیر امور خارجه سوئیس پس از دیدار با عراقچی
🔴
جناب عراقچی به سوئیس خوش آمدید.
🔴
در نشست دریاچه لوسرن، ما چارچوبی برای گفت‌وگو و تبادل نظر فراهم می‌کنیم.
🔴
در شرایطی دشوار و پیچیده، رابطه مبتنی بر اعتماد میان سوئیس و ایران، که در مأموریت ما به عنوان حافظ منافع نیز بازتاب یافته است، همچنان در خدمت دیپلماسی و در راستای صلح و امنیت در خاورمیانه قرار دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129525" target="_blank">📅 14:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129524">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
پزشکیان: در شورای‌عالی امنیت ملی تقریباً همه اعضا متفق بودند که این اتفاق باید رخ دهد و تنها یک نفر نظر متفاوت داشت که وجود یک نظر مخالف در یک مجموعه نیز ایرادی ندارد
🔴
مقام معظم رهبری به دولت اختیار داده‌اند تا این مسیر را دنبال کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129524" target="_blank">📅 14:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129523">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4776c5951.mp4?token=cuLlRRlXyHUdJV3AYuhsBgJaJOWmRcZL4bRfEkjdAQ0vjlJX2bEfG0Abwx-wSHIrqzqBcq8PgUzGQTFJTtU_d9L-rdqAZJKAtGGRr75MThztxkLYRkXx4j2ai-FmOI9nB68yZR5udKyA0SE3n2lYK97laP8ocQgcnAI4OxAI2_Rxic5d9yw3w3FKSmQsI_B0iI5s9_UVnQrOU0sc2vs66l9E1Z2iFWJF66H_rG9uw8krESupAfTvK-t1Izx-msAm--C9w2uoJCE3oh52xqO4AZYYceUvaXuuSZWA6yEkJyfdMmOt3sCTGD7UW4nr5I7wCNfIlXChIVSc03x_sIQbIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4776c5951.mp4?token=cuLlRRlXyHUdJV3AYuhsBgJaJOWmRcZL4bRfEkjdAQ0vjlJX2bEfG0Abwx-wSHIrqzqBcq8PgUzGQTFJTtU_d9L-rdqAZJKAtGGRr75MThztxkLYRkXx4j2ai-FmOI9nB68yZR5udKyA0SE3n2lYK97laP8ocQgcnAI4OxAI2_Rxic5d9yw3w3FKSmQsI_B0iI5s9_UVnQrOU0sc2vs66l9E1Z2iFWJF66H_rG9uw8krESupAfTvK-t1Izx-msAm--C9w2uoJCE3oh52xqO4AZYYceUvaXuuSZWA6yEkJyfdMmOt3sCTGD7UW4nr5I7wCNfIlXChIVSc03x_sIQbIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار تیم مذاکره کننده آمریکا با شهباز شریف
🔴
تیم مذاکره کننده آمریکایی به ریاست ونس امروز در جریان مذاکرات چهارجانبه ایران و آمریکا با مشارکت کشورهای میانجی، با شهباز شریف، نخست وزیر پاکستان دیدار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/129523" target="_blank">📅 13:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129522">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o590J0qTLJfN9oJDk5POoL-YW9dJXTtgQJ5NvQO3Z8xfCMETU98NcrhTaBvMh76Wxs7nd2lYKqH0skt01KFwmv67kO7xVNYpcIG7a2UzJf56FOL2DTAkBMKpo_p1LE-I3QFgFgUjvlYeyuREKX-djaoTzUYWetkB2sEwB-AekUqOGXnKkD1FQpTZvVY_pmtTW4rrlRlHXEROs1BJ6vDPw34jHMz_eOxGdtr8O0guwu77kZwgXRRgOiODyNBGN6iWjaH4ZHe9sr4yTrAsdI934sRggredMEQnb8R3h6eW8NfCGSwCzodKS9aFzzV0b8_p9AmtNXV7srsCZTVY61aFqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدیر کل آژانس بین‌المللی انرژی اتمی گروسی گفت که با وزیر امور خارجه سوئیس کاسیس در بویگن‌اشتوک دیدار کرد.
🔴
«در این لحظه حساس، مهم است که به دیپلماسی هر فرصتی برای موفقیت داده شود.»
🔴
گروسی همچنین از حمایت طولانی‌مدت سوئیس از آژانس بین‌المللی انرژی اتمی و تعهد آن به دیپلماسی تشکر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129522" target="_blank">📅 13:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129521">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
پزشکیان: دوران محاصره دریایی یک بشکه نفت هم صادر نکردیم البته طی دو روز گذشته ۱۶ میلیون بشکه نفت صادر کرده ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129521" target="_blank">📅 13:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129520">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
شهباز شریف نخست وزیر پاکستان با ونس معاون رییس جمهور امریکا، در حضور کوشنر، ویتکوف و فرمانده ارتش پاکستان دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/129520" target="_blank">📅 13:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129519">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68daaf45ba.mp4?token=oshJPjd0OPh6mK1QFQ1_szVPXkLMtUN9CmwH2DtgHD5juk3ZsfFqtQvek8B7BR9szSaQjv6bYdKxah2Ukuz0v3a7RFPsExH5p1KEJqWyBIntcXTTTpivjLob4FdL4ocvLmjyuDipnFUt8W4QzMWxJLr8RxBVJCUuwmTRtislh8mFsGHhTJrq9peSC2oQ8AINgBj7m-nu3U6xFYIOo-Ws1CDekEcJwCFMl17nYM8TiSqq7fX5CWDlMP_mSqza3DRhPpnBvCHsjgyYh0PpVW34YcJHb3RfdnEOQ1rMPoknsZ3ES_jI66pYYZ6X4Gshl9g_aqdK9SzVhJrHiqkE6ZZ7nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68daaf45ba.mp4?token=oshJPjd0OPh6mK1QFQ1_szVPXkLMtUN9CmwH2DtgHD5juk3ZsfFqtQvek8B7BR9szSaQjv6bYdKxah2Ukuz0v3a7RFPsExH5p1KEJqWyBIntcXTTTpivjLob4FdL4ocvLmjyuDipnFUt8W4QzMWxJLr8RxBVJCUuwmTRtislh8mFsGHhTJrq9peSC2oQ8AINgBj7m-nu3U6xFYIOo-Ws1CDekEcJwCFMl17nYM8TiSqq7fX5CWDlMP_mSqza3DRhPpnBvCHsjgyYh0PpVW34YcJHb3RfdnEOQ1rMPoknsZ3ES_jI66pYYZ6X4Gshl9g_aqdK9SzVhJrHiqkE6ZZ7nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عارف، معاون پزشکیان : دنبال جنگ نیستیم
🔴
ولی اگه کسی بخواد شاخ بشه و جنگ رو تحمیل کنه، جوابش رو جوری می‌دیم که یادش نره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/129519" target="_blank">📅 13:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129518">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZe-4TiOQ2e-TxMsUWMiIGqD6EVfabbBmLti_IDgJGsojgG_hjqMq5g8f6_zQN_ANCwC7eTuupoiWQ4NeWxgFikQ9j-uO-HLLRapFxVo5LC-jjK9noXsSiseUqY4M6conSTg3YDtPExXl7xKSMeDC-qXynovMPUVQP6NlGLzkkgOJsfDzf4Rj6ZTWwtXnQ2QObyxc1M-bpSmOyXmpiI7cWXEPmJHUHzfM5zvTfzftJ--qwOqGVL90cIB_43Oj9xTSjStNHbGYQgM1T8ZMRYcldcCUbFX6u2W360ubvYGLuwT3jpqLTpGjhNBE7lwMU4yxCpU8syV-T25Ui9QrnYPxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با وجود اعلام توقف گران‌فروشی اپراتورها در طرح اینترنت پرو، ایرانسل همچنان هر گیگ اینترنت پرو را با قیمت ۴۰ هزار تومان عرضه می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/129518" target="_blank">📅 12:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129517">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kiq3d45H-g9kBbEGOf8SgDmqMgIYX0Mte5kZdA6XdmU5XJTIwsntf9c68v4GUE13VF_9WyRRVcqkouQEPJORptCP2XpBYH51p4xao0Ar1zSVDQppMnwjBCqljJ4vAuqYp_zzIg92-AjEBFJawINyLo7KugnVsi4vki398DPU43fA4SZrgHKP1417uA-A2amv07IeYm1ZflR9vTXEhe4PEkkcTuQyGReyapc3bJOcSa29obRZImIjbdYcSJCcPksXmaecfaQIVJrF4llgJee6fnUitHJeKSuNKhNY7nmUZHERuGyZzVxgJkKh2Z8NuZJnLmSYTt6XKV8CdlUcbG_h_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمار رسمی اعلام شده از وضعیت پتروشیمی‌های کشور که پس از حمله اسرائیل شاهد حدودا ۸۷ درصد کاهش تولید نسبت به سال گذشته بوده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/129517" target="_blank">📅 12:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129516">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSn88XApNGJ4uxiocdBok4w8-Hx_T--EnBa5OXE1QRQaZt54aqQxt95a8NVYpuJDtUYnfEgQiHBDki1Z71a434_Iyauu9AMiIJkW6Tpx9MIdD6WpnqNFbcWQBwET-NoYBRzSovJ8OflbgTRerx2bXpn5rOdD-44UhXnfJT-NVM8JD0DjuijToiRMQCdz1E4VfYsJoMITRYIzZRHNYlPW968BQgdrodAzQ78NBoyI0AKx1nStZI1wMRGhJmS3jAwFLeXf6BF55ymRboPNInjJ0DABA4NQYqN2R1lmfkMR2TrCU1syj--PnZEW91MVIrwVUwzPfJeCsLHe6P4qKgWC8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان : قراره ۶ میلیارد دلار از پول‌های بلوکه‌ شده ایران برگرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/129516" target="_blank">📅 12:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129515">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/056df7a897.mov?token=R6R25U-UBqnkBKOJtAiQTaVYtHEypAfZkTO_54xRfkslRXsZuzvFfIT7J0vMXwQB2DSCo9iNFwcw2_aHeJmLFkqajC7SacKis3W_PehtUzeimV3dUsHBiLjNM1NYIH5TshQMPATFARQXOec8GadiH1M0OZy0O_6xUKiZ3ejdNSxAgSR47DsAAiJnRYBSNg3V9wJ9fWFEXCWK_1quRkJh0HbH2k9tNSSJWucydEFwKFVPyU4HK6rC01VhFEW6pJxn7wPB82RfC4qZs7XAViTNcbw9onh82_CeZT0hLnpSzfKByDNsqQ2TCyR8USuhtwB3nY3j7FC5JlOXLtTEi1SOew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/056df7a897.mov?token=R6R25U-UBqnkBKOJtAiQTaVYtHEypAfZkTO_54xRfkslRXsZuzvFfIT7J0vMXwQB2DSCo9iNFwcw2_aHeJmLFkqajC7SacKis3W_PehtUzeimV3dUsHBiLjNM1NYIH5TshQMPATFARQXOec8GadiH1M0OZy0O_6xUKiZ3ejdNSxAgSR47DsAAiJnRYBSNg3V9wJ9fWFEXCWK_1quRkJh0HbH2k9tNSSJWucydEFwKFVPyU4HK6rC01VhFEW6pJxn7wPB82RfC4qZs7XAViTNcbw9onh82_CeZT0hLnpSzfKByDNsqQ2TCyR8USuhtwB3nY3j7FC5JlOXLtTEi1SOew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هیات جمهوری اسلامی عازم ساختمان محل مذاکرات شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/129515" target="_blank">📅 12:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129514">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9S3zJ5qGoN2mLBo0bLBBzZYwa_INHg4dPzjLkzSNXczPHtJmDL-ciZGcCCChcN6m8ej8Qf1okmdkGvVAN_u4ZGeKm3Ed3bXCZ6Z-WwSqOFvHb-4Fa8x7Ue3HDsNfYpjz8dIShyd-cQ7Cu9kDjOWe6cIUL6nyZd8Tv_3RmKxIH2maXnNjxDjILcYDqnCwg6hXFShV-xEWEt-qgUNMAqJmENxanTaiWnU5-4B3zD7maVo3diD6NsBRSoOdTRRxDtp_zCVdHLVV6zM546nQKJ653zMtNai6bFPvmxBpfmL3zwI5dbrpcRxIzDzO8SG5wIE4V7J_UMowDyMckrFPyQ3IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نمایی از محل مذاکرات در بورگن‌اشتوک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/129514" target="_blank">📅 12:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129513">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
هیات جمهوری اسلامی ایران عازم ساختمان محل مذاکرات شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/129513" target="_blank">📅 12:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129512">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سخنگوی هیئت مذاکره کننده ایران:
برای اطمینان از اجرای یادداشت تفاهم به صورت مستمر از طریق میانجی‌ها تبادل پیام می‌کنیم
🔴
در جلسه بعد از ظهر، هیئت‌های نمایندگان هر ۴ کشور در یک اتاق حضور خواهند داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/129512" target="_blank">📅 11:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129511">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سخنگوی هیئت مذاکره کننده ایران: قرار است یک جلسه یک روزه داشته باشیم
🔴
برنامه‌ریزی به این صورت است که صبح دیدار دوجانبه با هیئت ‌های قطری و پاکستانی به عنوان میانجی‌های این روند خواهیم داشت
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/129511" target="_blank">📅 11:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129510">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
فارس به نقل از یک منبع نظامی: تنگۀ هرمز همچنان بسته است و نیروی دریایی سپاه نیز تا اطلاع ثانوی هیچ‌گونه مجوزی برای عبور شناورها صادر نمی‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/129510" target="_blank">📅 11:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129509">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سخنگوی هیئت مذاکره کننده ایران:
قرار است یک جلسه یک روزه داشته باشیم
🔴
برنامه‌ریزی به این صورت است که صبح دیدار دوجانبه با هیئت ‌های قطری و پاکستانی به عنوان میانجی‌های این روند خواهیم داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/129509" target="_blank">📅 11:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129508">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
اسکای نیوز عربی : پیش از شروع مذاکرات ایران وآمریکا، جلسه‌ای بین هیئت‌های ایرانی و سوئیسی در اقامتگاه بورگن‌اشتوک سوئیس برگزار شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/129508" target="_blank">📅 11:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129507">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
حمله بن‌گویر به ترامپ: باید بدانیم چگونه به رئیس‌جمهور بگوییم «نه»؛ توقف آتش‌بس یک اشتباه بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/129507" target="_blank">📅 11:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129506">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
تمام مفاد تفاهم‌نامه امضا شده بین ایران و آمریکا به نفع ماست و دستاوردهای این گفت‌وگو و مذاکره عیان خواهد.
🔴
ترامپی که ما را از انجام بسیاری از کارها منع ‌می‌کرد، در سخنرانی اخیر خود تمام آن‌ها را حق مردم و ملت دانست.
🔴
۶ میلیارد دلار پول ما در قطر برخواهد گشت
🔴
نتانیاهو اولین ناراضی از مذاکرات است.
🔴
تنها نکته آمریکا این است که ما بمب اتم نداشته باشیم.
🔴
این موردی است که رهبر شهید هم بارها فرمودند ما بمب اتم نمی‌خواهیم. آمریکا گفت همین را بنویس و امضا کن، ما هم امضا کردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/129506" target="_blank">📅 11:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129505">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
عراقچی و وزیر خارجه سوئیس در بورگن‌اشتوک دیدار کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/129505" target="_blank">📅 11:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129504">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
پزشکیان: به‌زودی مبلغ کالابرگ را افزایش میدهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129504" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129503">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
یک منبع مطلع به ای ۲۴ نیوز:  یکی از اولین خواسته‌های آمریکایی‌ها در مسئله هسته‌ای - اجازه دادن به بازرسان آژانس بین‌المللی انرژی اتمی برای بازدید از سایت‌های هسته‌ای در ایران به منظور بررسی وضعیت به‌روز شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/129503" target="_blank">📅 11:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129502">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
وزیر نفت: پس از توافق، کشور بزرگ‌ترین سکوی سرمایه‌گذاری خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/129502" target="_blank">📅 11:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129501">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
تنگه هرمز هنوز به صلح نرسیده است؛ با وجود اعلام صلح، بیش از ۵۰۰ کشتی همچنان در دو سوی تنگه هرمز در انتظارند و بازگشت به شرایط عادی زمان‌بر خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/129501" target="_blank">📅 11:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129500">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سی‌ان‌ان‌: در جنگ علیه ایران، قدرت نظامی آمریکا آن‌گونه که واشنگتن تصور می‌کرد، قاطع و تعیین کننده ظاهر نشد
🔴
در چین برخی صراحتاً گفته‌اند که پکن از این جنگ سود برده
🔴
این درگیری بر برداشت جهانی از چین، تأثیر گذاشته
🔴
جنگ مذکور قدرت بازدارندگی کلی آمریکا در موضوع تایوان را به طور قابل توجهی کاهش داده
🔴
بسیاری معتقد هستند که پکن در بهار امسال، تهران را به سمت مذاکرات با واشنگتن سوق داده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/129500" target="_blank">📅 11:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129499">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری / المیادین نخستین نشست رسمی در سوئیس ساعت ۱۶ به وقت تهران برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/129499" target="_blank">📅 10:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129497">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uWOFvW5kk32hzFnQ9TJGefD_a-x8-_O8AyRiC28yuy6PDhmunFfOAMZDeJGrkHe5KVL5EJBk7jh3MTq02aWUTxsvkrw-R138YOkQc8w1wOa8wiEIrWCE6rSG3kgzoE2WXqKy7uPhagdaUWIieCOttrYu6ryYScEsUaCDLnV4_Pfsit2Ur5AUrNwz9oRb-6vp-7zRsOc0gKdGWaaUREkK9kiklYjyKHxXJmIZ60m359LQOuM4uvzGNI--mG43upBgPkoqLWZ7NGMM5HIdOF5OJN6TXy2QijjM74bj-DwLIffnQPHRoRVoaF9N1uG-r-Bod1Cx70nBvwancH83TLG7jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/enk__ntfnQ65VdW6Jlh5eQDSLW1vf4UdrdnhnaGl1HyxvFrf4KB87wYV2LW8Qv2eDMYYkV2-aeyU3c5FGDt6i3MX3OyZUTdpCTLG_FmzL-xsffxZy1aE1_ajsJ6K6yCuU2FxMSDY4zeBHmFFlmtnwSIkTTb9wLvTVXQEUSykZKy3LamgXobQy0lKOOtWsES41sv4FOcMhU9zYKH4oia3wt_ar9Ci7tKPfy6GF0qTwsnd4QU-BgRYalcAg_a5nH3Bov6d1oUBM4MqCesCFOjo-qv8MVzWg3Mh7ovhCcxET0iLKBrbPMNI65J7fryqPNllBvtBieioYTPUT9GqTM7Vvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پرادو ۲۰۲۵ در امارات ۵۰ هزار دلاره در ایران ۴۳ میلیارد تومان ، حتی اگر دلار رو ۱۸۰ هزار تومان درنظر بگیریم و ضرب در ۴ بکنیم هم به قیمت ۳۸ الی ۴۳ میلیاردی این خودرو در ایران نمیرسیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/129497" target="_blank">📅 10:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129495">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/efqrvMSHTgi288r1WadthWgqFJ4Kexv2Qb9kYjHuAwcuaA7lImt6Yhxt06sUU8Xd5ghiFP-6IvKVdTpLr-lJYIsAGvqDPG1CLgigPSj7ujLrYAn4-il1Bj_GwDSL7yzabe8UDd3JZMPev9db2h-kYe6NwtTSKVWkqcwjMW3LMLZDougGcKQN7CmzgWgc47s9W6MNJl0ea06aV3aTIQhaQrOD5OJ8Pc9IQVsxIGWfeYOhh2BbN1ICP9_esFeJID4XtLMqm_WbhCcSHel9J2E0MrmEFrx0vbTjw5dKwWD4EjBSrDSxctkuqSz2ap5KDpnlUZoyS950fJ3BvWoM4T8z6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GdprpM-H3g_j4PxuhPTMAsSgNhCfAcpbvG7SH-y_XqbXLFI9WHRo2S7AfZnerRBseD_HJcC3jjaqOYrjov9HopfslLE-P_ACgVicPkEhMOSmCdeECMqT6Wp2C02hPXGqreKzs965rdowhUIi6VaG3U23Hl3eZcpKFLfW5yFB21lvIiIh8ehwb-XdgoqQMwEYXvX-A4awUT2D0JAU702lB73oTHk3DZ70Rn5UqvkIBlLEk1AhAQR9SP8tWwcqzGZSnKuIg61kJjo4TaqEtQgOHI2tUN_PyEEtXvQSJOemiRMv30V5soUE7LyJ14rJzoHvfUscKPJdNFdwksl1Kwu01Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از ورود هیأت ایرانی به سوئیس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/129495" target="_blank">📅 10:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129494">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجار در دزفول
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/129494" target="_blank">📅 10:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129493">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ترامپ: شاید اگر توافق با ایران حاصل نشود، برای عبور از تنگه هرمز تعرفه وضع خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/129493" target="_blank">📅 10:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129492">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLLZ03gArmgEL8SMEfJpb2UBq0CMPxb5pax0onDBXXBlmqJdkZHhrbHwWKtujVbXozu6JRh1aKgKWLmgj7WAnb5D_PX8TvRLgGDdy1rs9e2R3dCxRqy3qIK-7jFy67y8Vjbn_R4r7uZMSY40tcPzQl_UrmXRMMHUQ5yGYQqLzpN8iCpPyFY624OSc7Uz53rh76yynR2SYuOwlFdbDLBrqC1O8Mpyk6hZH7ibtAKRWJoQYSRRfFreKt-GEuvsMbNnu2r2ElB1o2HOO9eP0-QdJwSCRPN7snvefwYMkP7PCwlWel0rdWr9B1ytSBVhSy16IjhZXXxwv0o6xFmTJqlskQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال ، محسن رضایی: هرگونه خوش‌بینی مورد سوء‌استفادهٔ دشمن قرار می‌گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/129492" target="_blank">📅 10:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129491">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
الجزیره: شکاف در روابط ترامپ و نتانیاهو به اوج خود رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/129491" target="_blank">📅 10:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129490">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
خبرنگار الجزیره در نزدیکی اقامتگاه بورگن‌‌اشتوک سوئیس : ظهر امروز به وقت محلی قرار‌است مراسم نمادین امضا و مبادله متن توافق مرحله اول میان دو هیات ایران و آمریکا برگزار شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/129490" target="_blank">📅 10:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129489">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
سی‌بی‌اس به نقل از یک دیپلمات شرکت کننده در مذاکرات سوئیس: ادغام پرونده آتش‌بس لبنان در مذاکره با ایران، یک تحول راهبردی برای دولت ترامپ به شمار می‌رود
🔴
دولت آمریکا از راهبرد جدا نگه داشتن منازعات مختلف در خاورمیانه، دست کشید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/129489" target="_blank">📅 10:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129488">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkPXo1rcHS5cm-B6TAH9KDgWdKE1C0EOGhOk5ERMxduKLyWcHTK8pnzj5IBe_37r3XzMFRQRh6sVLE2RdMO3llzZsIe5iF4dsGZTcaMGBahkeAJFSLZe6szXmHgE-wLKgiDeBmc-xetDnG_opPzYC0cM7oNe5NjtnW0-zAZXgyUgnn9TY7OHjUjdzZBNBpdsxmtHBPPnWAcOEFOCdgowo50wL__L50_C4POUWG_z5E2tfQMuizmE0p2_HqldnbAFjqAPI1rfOf5PzIyAyiMqWMkrmSz0LgWHuV-cLoWgpA56zPtgADJvuV8dtwvqqOWiLD68b2XEZ4faXyyk109E3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترمینال سوخت کرچ که توسط روسیه اشغال شده بود، صبح امروز با حملات پهپادی اوکراین منهدم شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/129488" target="_blank">📅 10:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129487">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
عاصم منیر، فرمانده ارتش پاکستان لحظاتی پیش وارد سوئیس شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/129487" target="_blank">📅 09:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129486">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
عاصم منیر، فرمانده ارتش پاکستان لحظاتی پیش وارد سوئیس شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/129486" target="_blank">📅 09:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129485">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک منبع دیپلماتیک: پرونده لبنان نخستین موضوع در نشست اضطراری خواهد بود که به مذاکرات سوئیس افزوده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/129485" target="_blank">📅 09:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129484">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193ac2578c.mp4?token=qzltmUCYvCPgRUyjC0SUOdERBYFBIOccSFepWTST3aCrPmOoTvkGC47i1QwnmmUvAOiJ6cOvZ6RFPLgNGVA5I7OBdaAbLBfO7_y5j006G282HJbDbyY7Ba8X8Rs7lb8uBCw3qvOLJXkyC-BQzmjIbKqd1vwaaTno3qGkhABVKO_1tAKFt1S-Q3O-fV5wdXVltdIttLp7toLy9GeT6NK2OpfyJ0QGVOdUzZgNCbveNol1cALMiw9NdsF0VuCam1JZT1xeCYxbP5qhnQiLevDfCXrHejBZP3gIXNvbHojo5CUu8LyDdo6o8BMP7epF--jUP8hSnlPOwJlByfzxVj88Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193ac2578c.mp4?token=qzltmUCYvCPgRUyjC0SUOdERBYFBIOccSFepWTST3aCrPmOoTvkGC47i1QwnmmUvAOiJ6cOvZ6RFPLgNGVA5I7OBdaAbLBfO7_y5j006G282HJbDbyY7Ba8X8Rs7lb8uBCw3qvOLJXkyC-BQzmjIbKqd1vwaaTno3qGkhABVKO_1tAKFt1S-Q3O-fV5wdXVltdIttLp7toLy9GeT6NK2OpfyJ0QGVOdUzZgNCbveNol1cALMiw9NdsF0VuCam1JZT1xeCYxbP5qhnQiLevDfCXrHejBZP3gIXNvbHojo5CUu8LyDdo6o8BMP7epF--jUP8hSnlPOwJlByfzxVj88Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش پزشکیان به مداحی که می‌خواست با تیغ، حلقومش رو ببُره:
🔴
خو فحش بدن؛ هر چی بیشتر بدن، خدا از گناه‌های من بیشتر کم می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/129484" target="_blank">📅 09:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129483">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
به گزارش روزنامه بریتانیایی "آبزرور"، نخست‌وزیر بریتانیا، کی‌یر استارمر، انتظار می‌رود دوشنبه آینده از سمت خود استعفا دهد و قصد کناره‌گیری دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129483" target="_blank">📅 09:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129482">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pxFDy2pO7kX_IqYbC2tuSeuIZWeXUKrgr3_aPWigoQPUnzNpaVXYf8S7onoJGTcT9xOeVO40DuJpYKZhnCT_RIDKGipsXmaA-ehOlVq_zG7sLils8o0hZKvBse9F3nD23C0UUIKx8FpWnWyLGHt6F761c0ka_piOl8O8P4kyozHK5dT8iJJOWDlqnOEF_88eHpKmtZqQoNvZX76Rj88IntkzIupaM3oP0ZhLavqkuxRozgNisuY6ZFOBhEtSTPItR5_5wMYdEHvV0K8zePLv6Q1ILeIXTRbvP8Z9U_pMS8Mt7viMSpGX1qpdFAkK0ak5LO_5RjjSOys-XwTpoHx4Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امیر قلعه‌نویی با انتشار این تصویر به شایعات درمورد ساعتش خاتمه داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/129482" target="_blank">📅 09:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129481">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
روزنامه وال استریت ژورنال: آمریکا پیشنهاد داد، ایران تنها برای خرید دارو، غذا و کالاهای بشردوستانه به ۶ میلیارد دلار دارایی مسدودشده‌اش در قطر دسترسی داشته باشد؛ ایران هنوز این طرح را نپذیرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/129481" target="_blank">📅 09:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129480">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک دیپلمات:
یک نشست اضطراری درباره لبنان به مذاکرات ایران و آمریکا در سوئیس اضافه شده؛ این موضوع نخستین دستور کاری است که مورد بررسی قرار می‌گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/129480" target="_blank">📅 09:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129479">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IC1ZHASSyMnoemyCvfS_9NkgkJgkr-dAxzZbj5ag5FtP-NBCWlxAjmnn-cB0An1amOnKBjHsG-GW1Tqad2YYJZG0o4Tzxiyz54BfrQy1XMWqj5EkP0fI8LiqhhNJtxdsKCZ-jAMQ1zMztPsHlnR2NtMv1S3fAX_Ei7X9UCQT426USbl9FeYhLhawbvszhQ2ehG7SXIeU1pT8eV3Fs3_1VUZyBpfPd-WR98kJe3Py60x0Ppf8cbf3tkY6k3phr7-rsA5BWpaUE8lqRLu_X1THlCfBVTdjUWpMxB9dOrwmnFiD8T75H1hAm2V-suK42eEl2Mcb4pTm9kvZDJks_RZ3bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسین شریعتمداری: مسئولان نظام برای بازگرداندن  بحرین به سرزمین اصلی ایران اقدام کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/129479" target="_blank">📅 08:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129478">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
رادیوی اسرائیل: کشته شدن ۶ سرباز از جمله یک افسر ارشد و مجروح شدن بیش از ۲۰ نفر در حملات حزب الله در لبنان از پنجشنبه گذشته.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/129478" target="_blank">📅 08:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129477">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
خبرنگار الحدث: ونس، معاون رئیس‌جمهور آمریکا برای شرکت در مذاکرات با ایران وارد سوئیس شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/129477" target="_blank">📅 08:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129476">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DO-mFV_AkJ5bN3JlNyg44VFIgDcoDFEVeo4C2bes_Py3E2jwA5qFJcWAcRCSNFeVLmeKhaZvpiV6W3udQm6pK0w8wuD9XO3RKLf3DIVw8nKZBFaCt12cBemljJA8FYcv0JCS5w28hDcWXC0bG3jPu-osZvSCmCaogWVKqoPeZVuVPfyEtiZxKur2feZ1Cj_6E7liGszxmUOSG7qe2aoaSSt3beBTAVsIulDSr15bKje-LQ7XzalkasSTeQvI6gCUf7gF65sjjWbyVljnvLmZiIKTA6NMUGElPtDkSO4gJosWsstKDVkE1xKrHxS1Vpnwv-8x0oE62FKewR0vwhb3_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) روز شنبه، با انتشار تصویری اعلام کرد که یک جنگنده پنهان‌کار F-35 نیروی هوایی آمریکا بر فراز خاورمیانه توسط یک تانکر سوخت‌رسان «کی‌سی-۱۳۵ استراتوتانکر» (KC-135 Stratotanker) سوخت‌گیری کرده است. سنتکام تاکید کرد که نیروهای آمریکایی به گشت‌زنی‌های مداوم خود در آسمان منطقه ادامه می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/129476" target="_blank">📅 08:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129475">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd6e8762e.mp4?token=WINPgRMTeldk4L5DvQEC4boFOtKinG_TcYfSU83HWq0C3yQyjEoo8c1gseGx8FLKm0dpW-1aju8Do1o8J3Vu-wciWISAKDhLTMbRqrUqS5_Jz9X2Mx0UeYcAhEarB7-i6fbCsCLpfvC4LTKuOldhVwEY_mXzTspX33LSKV8yAgqWM7qi1OFPZ_WoTCq2L2Zv3mJGt2ERmxSiprenFjFoXuSPBlY3d1NMpsxX0XTw0BPEQ1bNQQMwKTHy14IuSswiHfc7hXiH2JyPepfM0cbYO_I3eTaaTdspN8oJWLqJIlAQNrkd4IVuHI9zgTPhKcEjseWPR9pq9S_TcgGU9f0hVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd6e8762e.mp4?token=WINPgRMTeldk4L5DvQEC4boFOtKinG_TcYfSU83HWq0C3yQyjEoo8c1gseGx8FLKm0dpW-1aju8Do1o8J3Vu-wciWISAKDhLTMbRqrUqS5_Jz9X2Mx0UeYcAhEarB7-i6fbCsCLpfvC4LTKuOldhVwEY_mXzTspX33LSKV8yAgqWM7qi1OFPZ_WoTCq2L2Zv3mJGt2ERmxSiprenFjFoXuSPBlY3d1NMpsxX0XTw0BPEQ1bNQQMwKTHy14IuSswiHfc7hXiH2JyPepfM0cbYO_I3eTaaTdspN8oJWLqJIlAQNrkd4IVuHI9zgTPhKcEjseWPR9pq9S_TcgGU9f0hVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چند ساعت پیش عباس خوش قدم (سید عباس عراقچی) رسید زوریخِ سوئیس، الانم این شهر طوفان شدیدی شده و کلی درخت افتاده روی مردم و مصدوم زیاد داشته.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/alonews/129475" target="_blank">📅 02:39 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
