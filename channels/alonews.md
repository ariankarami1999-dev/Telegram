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
<img src="https://cdn4.telesco.pe/file/CJyCIUPhVO5NWmVKZlnon13tPJ7RRghp6_B3Y-RgkDd97qtf5WAhrqiTXEwZ-SXvTuER-i7vHjpIZrYuJRoy5SaPRStAgpnWCEOBGp_j9qnrT-A5lvQjiGnIWPNHZL7nSDm6_FdEKSYsxy_q2doVHVBU-HlKx0auFB27iW-yUzAfUROc7v_WJ_E5BNWPTna_rYgS8RGIK9baCXki0TEbHNz2EAM-0RQWkauGAwVLq7hvtXoULdIc8jLv8XbTslUIwXuymHj-dr0od_04C157iyi2ri08Vdk3IjJYGKgV8zR6INwPH95CmoKAysIgeoZy0Cvq_Dx8uaq0QtKdRzhOug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 947K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 20:30:22</div>
<hr>

<div class="tg-post" id="msg-129898">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
روبیو : یه سری مسائل هم خارج از اون توافق (MOU) هست؛ ولی باید روشون حرف زده بشه
🔴
ایده «پایان کامل درگیری‌ها تو کل منطقه» از نظرشون عملاً شدنی نیست
🔴
چون می‌گن تا وقتی گروه‌های نیابتی ایران از عراق موشک و پهپاد می‌زنن و در درگیری‌ها (مثل حماس و حزب‌الله)…</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/alonews/129898" target="_blank">📅 20:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129897">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce086fb77.mp4?token=evuTRqVeebdA-iwN9yEkjo7yRTj8YlMO8E2W09wyg0ml_tMJgtzA2QjtSfEMaeyg8L1PAQ-5qE7xjd4WpLbJm8qgxpxyPmjd1aTjjevAyAoc8xTTR6ANZT-zqCkKg4_8iUfXxTMPCTu0aDV1JvvgQd11mm6WjZrQG-3HnIq_ASNH9vMf-k2Ex2Pbn2kUcWDcWTgMUNVvZeyZyZxWWx6UfaulY1m0mFj2JdvAThAWT95MfWIdIHhTd4DR5oH8VZD4iuceftW6VBKApDAEPwZ0Bx_4TGEK7ZTtvWWHKpovHenxlZ_-jc0wQ3uHX_09aKER_THZWK4j5pO3AfQ8bMQO3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce086fb77.mp4?token=evuTRqVeebdA-iwN9yEkjo7yRTj8YlMO8E2W09wyg0ml_tMJgtzA2QjtSfEMaeyg8L1PAQ-5qE7xjd4WpLbJm8qgxpxyPmjd1aTjjevAyAoc8xTTR6ANZT-zqCkKg4_8iUfXxTMPCTu0aDV1JvvgQd11mm6WjZrQG-3HnIq_ASNH9vMf-k2Ex2Pbn2kUcWDcWTgMUNVvZeyZyZxWWx6UfaulY1m0mFj2JdvAThAWT95MfWIdIHhTd4DR5oH8VZD4iuceftW6VBKApDAEPwZ0Bx_4TGEK7ZTtvWWHKpovHenxlZ_-jc0wQ3uHX_09aKER_THZWK4j5pO3AfQ8bMQO3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: بحث موشکی در تفاهم‌نامه نیست و هیچ‌وقت وجود نخواهد داشت
🔴
اگر موشک‌های ما نبود اسرائیل و آمریکا ایران را مثل غزه شخم می‌زدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/alonews/129897" target="_blank">📅 20:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129896">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed9cc22773.mp4?token=skMKXcfh5jcD0J72ef7nKKwHnSEZQUjMzgb2if4Dfty9OuUCWFy_yhmFfWg-KWS8U_o_LCYVPKfDUJ2kihf6TFxrr23vNJM8HIdpfvfJ5bJx1gVdaSxuyO8yn9vvAJvBtV2tSOSPcsRMl0x5BKJKXS0NMf3Jtk6ThX8dp4TpXviD4bgzUEpe0icUNdSYTH6chKYp0nT9U0x8-6E-32A753hvnincq0mMDQsKXjhpssQ3GJvXdMhzSKaMxi3V2-kF4BKm7_3B-8WFiq-v1u_8YNpRVcRz-CYF9dcyJX1yA_3YDjsIgZySw4b1XNqGtPXKl3Kr1nXsA0iVpxdLtoeBQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed9cc22773.mp4?token=skMKXcfh5jcD0J72ef7nKKwHnSEZQUjMzgb2if4Dfty9OuUCWFy_yhmFfWg-KWS8U_o_LCYVPKfDUJ2kihf6TFxrr23vNJM8HIdpfvfJ5bJx1gVdaSxuyO8yn9vvAJvBtV2tSOSPcsRMl0x5BKJKXS0NMf3Jtk6ThX8dp4TpXviD4bgzUEpe0icUNdSYTH6chKYp0nT9U0x8-6E-32A753hvnincq0mMDQsKXjhpssQ3GJvXdMhzSKaMxi3V2-kF4BKm7_3B-8WFiq-v1u_8YNpRVcRz-CYF9dcyJX1yA_3YDjsIgZySw4b1XNqGtPXKl3Kr1nXsA0iVpxdLtoeBQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان دکترای افتخاری از پاکستان دریافت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/alonews/129896" target="_blank">📅 20:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129895">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
روبیو : یه سری مسائل هم خارج از اون توافق (MOU) هست؛ ولی باید روشون حرف زده بشه
🔴
ایده «پایان کامل درگیری‌ها تو کل منطقه» از نظرشون عملاً شدنی نیست
🔴
چون می‌گن تا وقتی گروه‌های نیابتی ایران از عراق موشک و پهپاد می‌زنن و در درگیری‌ها (مثل حماس و حزب‌الله) نقش دارن، نمی‌شه گفت تنش تموم شده
🔴
برای همین این موضوع هم داخل چارچوب مذاکرات می‌مونه و بعداً روش تصمیم می‌گیرن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/129895" target="_blank">📅 19:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129894">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
وزیر خارجه آمریکا، روبیو : موضوعی که همیشه مطرحه
🔴
اینه که الان یه مسئله مربوط به ایران درباره لُبنان وجود داره و اون هم حمایت و پشتیبانی از حزب‌الله
🔴
این موضوع هم بخشی از گفت‌وگوها با ایرانی‌ها خواهد بود
🔴
اما درباره آینده لُبنان، این کشور متعلق به مردم لُبنانه و باید از طریق دولت منتخب و حاکمیت خودش تصمیم‌گیری بشه
🔴
ما هم قراره با همین چارچوب جلو بریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/129894" target="_blank">📅 19:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129893">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/36127e8772.mp4?token=g442y_qPDggp1PGO9Bu4Kk4B4ZIdMbW287oOgjlVAbt7hdr1ZLpUYEoXyyYroLdJ3AaV2P1xce4kvtic2chVCodTlvaM3GJBgLJSpfHA8NU1cNiSCPk61Qb-MzS0GkZXvgLKgIJw_5TMOvAbGweGdS-cm17MnlL2Zy8phFtyT0wP4NxVfe45DmUpPOgdmNu7sGsl-P0SeQ0TbyvWqPo7SIf-bRXtinbsA4Kjd1vwwN3EXRImRMdNSDDXpTHFFdICWrx44EkoxgL2mqxrWz1rLCPihKhUncIk-NgBjtB1zQ16uPSEzdPrpv-JgqWVepx_IzhxDjKMgu1hOGUX49I5Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/36127e8772.mp4?token=g442y_qPDggp1PGO9Bu4Kk4B4ZIdMbW287oOgjlVAbt7hdr1ZLpUYEoXyyYroLdJ3AaV2P1xce4kvtic2chVCodTlvaM3GJBgLJSpfHA8NU1cNiSCPk61Qb-MzS0GkZXvgLKgIJw_5TMOvAbGweGdS-cm17MnlL2Zy8phFtyT0wP4NxVfe45DmUpPOgdmNu7sGsl-P0SeQ0TbyvWqPo7SIf-bRXtinbsA4Kjd1vwwN3EXRImRMdNSDDXpTHFFdICWrx44EkoxgL2mqxrWz1rLCPihKhUncIk-NgBjtB1zQ16uPSEzdPrpv-JgqWVepx_IzhxDjKMgu1hOGUX49I5Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعرخوانی شهباز شریف به زبان فارسی در حضور مسعود پزشکیان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/129893" target="_blank">📅 19:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129892">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان، شهباز شریف:
این تفاهم‌نامه به موشک‌های بالستیک اشاره‌ای ندارد. این موضوع هرگز در دستور کار نبوده است؛ هرگز در دستور کار قرار نگرفته است.طرف ایرانی هرگز حتی تمایلی به بحث درباره آن نداشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/129892" target="_blank">📅 19:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129891">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان: آیت‌الله سیدمجتبی خامنه‌ای، رهبر ایران، را تحسین می‌کنم که در این شرایط حساس ایران را رهبری کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/129891" target="_blank">📅 19:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129890">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
نخست وزیر پاکستان:  کارشکنی هایی وجود دارد که می خواهند تفاهم نامه بین آمریکا و ایران را از مسیر خود خارج کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/129890" target="_blank">📅 19:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129889">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
بر اساس آخرین گزارش بانک مرکزی، رشد اقتصادی کشور در سال ۱۴۰۴ با کاهش منفی ۰.۷ درصد، منفی اعلام شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/129889" target="_blank">📅 19:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129888">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
شهباز شریف، نخست‌وزیر پاکستان: تفاهم‌نامه امضاشده میان تهران و واشنگتن ظرف شصت روز آینده به یک توافق بلندمدت تبدیل خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/129888" target="_blank">📅 19:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129887">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/187ae17961.mp4?token=BH2fUWcICTqi-DggHmj3egvlrh0CsKhQW3n_auSDNvZwjgiaEu7Zf1M-TN2kwCj6ZsA7Tk7-QzWtdYkRfak2SAiFUGjGFn67qaGzfTWLgDrepPGvBP37zJNjVImftbrHNCMpzK4Bb2br8JX2eOq8vqTHZz-PolnlcRYkZ2EHgQ3EGZurpAa1OTM2RGDpRjDHsVZVRRpugzNLL4GSpSscoiPYxbqG8L3rc9fHPZsylRBnIbxx4rqyVD8o1KeQKkpfZsq9dsksjHjt1grLgwsISOi00kbMZcN0RY5iwURZOYXuqNxPQ6em4VPR3RleO55zZCVN0P2nou8qPHPt6eOPJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/187ae17961.mp4?token=BH2fUWcICTqi-DggHmj3egvlrh0CsKhQW3n_auSDNvZwjgiaEu7Zf1M-TN2kwCj6ZsA7Tk7-QzWtdYkRfak2SAiFUGjGFn67qaGzfTWLgDrepPGvBP37zJNjVImftbrHNCMpzK4Bb2br8JX2eOq8vqTHZz-PolnlcRYkZ2EHgQ3EGZurpAa1OTM2RGDpRjDHsVZVRRpugzNLL4GSpSscoiPYxbqG8L3rc9fHPZsylRBnIbxx4rqyVD8o1KeQKkpfZsq9dsksjHjt1grLgwsISOi00kbMZcN0RY5iwURZOYXuqNxPQ6em4VPR3RleO55zZCVN0P2nou8qPHPt6eOPJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ثابتی: تنگه رو مفت باز کردیم بدون اینکه هیچ عوارضی بگیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/129887" target="_blank">📅 19:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129886">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
نفتالی بنت، نخست‌وزیر سابق اسرائیل:
ما در دیپلماسی عمومی بدترین در جهان هستیم. اگر اسرائیل یک شرکت روابط عمومی بود، قطعاً ما را استخدام نمی‌کردم.
🔴
با احمقانه نبودن شروع به کار کنید!
🔴
بن-گور چیزهای بی‌معنی و احمقانه توییت می‌کند تا قوی به نظر برسد، و سپس من باید در یک دوجین مصاحبه در سی‌ان‌ان و بی‌بی‌سی برای پاک‌کردن این به‌هم‌ریختگی وقت بگذارم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/129886" target="_blank">📅 19:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129885">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ریاست جمهوری لبنان: ونس و وزیر خارجه آمریکا تأکید کردند که آن‌ها پیگیری اجرای تفاهمات مذاکرات سوئیس، از جمله تشکیل یک کمیته مشترک متشکل از ایالات متحده، لبنان و ایران برای تثبیت آتش‌بس در لبنان و نظارت بر اجرای اقدامات مرتبط را ادامه خواهند داد
🔴
آن‌ها گفته‌اند که ترتیبات مربوط به حوزه اختیارات این کمیته و نحوه تشکیل آن، در دست بررسی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/129885" target="_blank">📅 18:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129884">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvVMOQCRK9wO2JaZNBFASKRSv6VrCuX4QuecPLP_Bq8oLeeYjLcNPg2ZwKw4zaN6bLIn_PrpagDabSOapmPrtxEegQVS6387Xu13UNuwbynmNk3o6km1PZaQI0yv2G_w4rDHhX2vfrfCevFWXCadPP7tqncSVjUyghZngitbYnkcaT7v__0mlJM8cqRPPOS8dyE7ctSM0LD1PLrsmdLQMlCLUsuq9gsGOcdwS3MowLp1dCs5G-J4CnrmREPPXqPRkjmFM3oCPcO-aKiqgo0C2ouhLah1g13xCHaNNs3TNRaBtwjZkJfofcJKy_Qr6GQc_s80Dch3dUzmgdW5ncD-UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: مردم نگران نباشن، یکشنبه قطعا جلسه مجلس رو برگزار میکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/129884" target="_blank">📅 18:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129883">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
به علت گرمای هوای ۳۲ درجه ای در فرانسه 18 نفر جان باختند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/129883" target="_blank">📅 18:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129882">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYr3dkrPQc6Q73Y--EGCqjgOEImbTuXQjSCW4KwWmLg3n7BGBairmXC0rr3lHbl5pFt4bMm0TSvYxCFiVunRAf6uE3Z7Es6Y2fEKguWMv6my-d3OIPKSBzN3SXO5ULgLhf5rEx2zq7DCNXOixDBVUc3pXajy8XoHpL8N9nzij4QQPD2lEizXwTZ7ZhkMgewHaCtZYIHh8CcQklqrfNw2OO0UTbV4fWNfw2P2kmqIaSbemJPiQvZfLDOYgrW62ML-bJABEdUXf1mbrdmxEG41vX2ZwxbseCyddNA4EvxCfLUQW7iVFAfChS75YpiUBmw2J82uaNvAZPSmgc2JBWSe9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جلیلی: رهبری با مذاکرات مخالف نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/129882" target="_blank">📅 18:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129881">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxHWuNXg-2KZ7nUKmnro-5cYQs31qQGEtlejUIGrOk944hQ5RcnT1DJKwAb_nt6zDuDSbY1S2LzFc9JbuQhe21oI2OkRaW3H5_-wIRzJlz9GgEMRNFvvAVR2OmWuReUh9d-wy6C-a68xAOKFmcgq6SgJURvqUqks3L4zl6u60qISEFGN1hZGIDsEyFhOtxQLhlsMDu9vGImiT8n0WAzvq2nYixF0IjWPNHaKGJtn5z35gd1ldAorxggYBzR6xHAxbf8f2k3MgQKk_GY6Z-nnyL2q8HaW-43__gkhw6zaxySZ4rkLTAvxYuDDv3wiDsACCEquRAoFVMD5md0ugkTNkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور لبنان، جوزف عون، خواستار پایان «اشغال اسرائیلی» جنوب لبنان شد و گفت که کشور او «کمتر از» خروج کامل اسرائیل را نخواهد پذیرفت.
در بیانیهای که از سوی دفتر او منتشر شد، عون ابراز امیدواری کرد که دور فعلی مذاکرات در دستیابی به اهداف لبنان، از جمله بازگرداندن حاکمیت کامل بر تمام خاک لبنان و گسترش اقتدار دولتی در سراسر کشور، «تصمیم‌گیرنده» باشد.
او افزود که «تنها انتخاب ما حاکمیت ملی ماست» و دولت لبنان باید به تنهایی مسئولیت محافظت از تمام شهروندان و تضمین حقوق و آزادی‌های آنان را بر عهده بگیرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/129881" target="_blank">📅 18:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129880">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INR7hpkUHYAoTPs3gl1pYw17Zz3V9UKptKcSAG4SBT5sWga93Ldrctobg1zJF8ozLnOu50q3k2aQfC0_RU4LfM0ayWploqijCRIWTLn3aYW_6kl7ez7jlm5hefsxpft9tRKKM4omu3prISYsbkydEPxyz0N38YqZ3dFJMZB4RxDMj_Bx_uPyqH-0Tlbfvb10KS5sJZDShG3ncP7rddEb7kgPN84ZH9bpp_lChAQIKt8Fx6mHl8NRYo9-DYoGa0vZJE9UUzDJvmFbSV06G0swDqJ54KYjiksa2lT80poPCMbmFQqdruzP-y5PeakfkyU8lVsZX4NNEgOcF7O1hQxYYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
ناو هواپیمابر USS جورج اچ. دبلیو. بوش (CVN 77) در دریای عرب در حال حرکت است.
دو ناو هواپیمابر به فعالیت خود در خاورمیانه ادامه می‌دهند در حالی که نیروهای آمریکایی همچنان حضور دارند و هوشیار هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/129880" target="_blank">📅 18:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129879">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
فایننشال‌تایمز:
با وجود افزایش سطح تردد کشتی‌ها در تنگه هرمز، مالکان همچنان سردرگم هستند؛ این وضعیت در حالی شکل گرفته که ایران کشتی‌ها را تهدید به عبور از مسیر نزدیک سواحل خود کرده و آمریکا مسیر عمان را پیشنهاد می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/129879" target="_blank">📅 17:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129878">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed01390a1c.mp4?token=pYUzNMpz-gnjzp--nwiuj58j9kqGJDZWUQT6tFbVhjc6PGVEmNjgNUmXkCmOudMDfLyJVPzYRuREuv4W1AkwHVlcS2UPsfapeHcEOnQ5tlCxtRuBxBBC-XICejtODa0kYkZ7hf0u36nPWQFOM5AtkC_6NwV3EWCRizpYj8ukYIBapH2MS1hddxNT3o6CiFqoI6sSHcOSimdme0XwrMR2xdjVzszSAZiLzP3KGERHjyU3CKGDEvND89jJNw1tiaczbts8J_tEJ8N5h43718Oq-B1X69Hv6kz6pk8krrH1PaPvRBitq2xhhWrvBI71ZC0ow6YsCPjtTYXDYapoaM249w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed01390a1c.mp4?token=pYUzNMpz-gnjzp--nwiuj58j9kqGJDZWUQT6tFbVhjc6PGVEmNjgNUmXkCmOudMDfLyJVPzYRuREuv4W1AkwHVlcS2UPsfapeHcEOnQ5tlCxtRuBxBBC-XICejtODa0kYkZ7hf0u36nPWQFOM5AtkC_6NwV3EWCRizpYj8ukYIBapH2MS1hddxNT3o6CiFqoI6sSHcOSimdme0XwrMR2xdjVzszSAZiLzP3KGERHjyU3CKGDEvND89jJNw1tiaczbts8J_tEJ8N5h43718Oq-B1X69Hv6kz6pk8krrH1PaPvRBitq2xhhWrvBI71ZC0ow6YsCPjtTYXDYapoaM249w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آیت الله العظمی سید صادق شیرازی، مرجع بزرگ شیعیان: در دوران پیغمبر و امیرالمومنین یک نفر کشته سیاسی هم وجود نداشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129878" target="_blank">📅 17:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129877">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
عاصم منیر به دیدار پزشکیان رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129877" target="_blank">📅 17:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129876">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
واکنش تیم مذاکره کننده به مذاکره موشکی: خلاف است و از اساس تکذیب می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129876" target="_blank">📅 17:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129875">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gb7Yh7C68GnD64Doy5VKyK1HN2ufZbeeaPg_hgLwG-qhRTq0qRuZZbK1uKAPPZnaT7i9PP8EkBZWUVP8CJ7GtQw1EbmoDMH1h9icAJWi5EgSLV8Y6DLmN4XEkGCw87No0SJhikUGsdTkvtswpacxqX1PWeBVvK18uR4S6Rt8jdnDX82VcSC4OWdLLuf-vSTfzc1ng0A8PN5mZRyMIF9yrir5Sb64lx2UZY7CNmYZnKtlxkuXfcWzCHzJT5jjPK37AKAuAyFQSKP9Fl-EsPTxSb1F8ubj09ejYVlOZZYW_9F033ILVd4ppaNQB8URPAJkFDDIJ7ME6eza9wl1hB2wPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت‌ها در بازار طلا، سکه و ارز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129875" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129874">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AadpCUku4RkIgi2B7EQ5I8wXr5MXNLnlfU70bR9JJIzKqeYh8Fgnf3O-o--hFPr3Auy8RHsGTbkQ2IPRjDhkKXOq-grpvQJqQODApf5E01kXR5VVlp9Sa6vEuAJLypM35pce7s0zPXHdABpE5F4_l1cD3qgIBNhq9KF4EJqBIk5qnOZQx5855Z5dqPaLdWtqJJTA0MTISDdNIOKmJXmbF2kx7oWa-9uwxlPphu2adZK6JwCgGhSDl_sudbSCn96D8sE_W8uQ2L1BeIOKh2cTY45Kn__NjxhKAYq_7-0thc3q3217XrenOxxN40geFRJl3DQS_adaHVeDEIJ2T0HcSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک پست در تازه‌ترین جلد خود، توافق ترامپ با ایران را به تمسخر گرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129874" target="_blank">📅 16:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129873">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
العربیه:
"سعید ایروانی، نماینده ایران در سازمان ملل‌ میگوید انتقال اورانیوم غنی‌شده ایران به خاک روسیه، یکی از گزینه‌های روی میز در مذاکرات است."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/129873" target="_blank">📅 16:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129872">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQYNC_jVt8YcmYFJ2UFtNTBfeGG_7TSlqW59F7JXpp4Ikpr1wjP3vnlLxEAcOGIcYJgFTj9qbtiEIX0vGQd7jWsTSoKrnE_RVPHFm9BOU_ouwPPenbz1iPo1JAxeMRU6dw8HLyRkdQGKf-Kza0EPOvPkofAHzE94fOYkcE_Uxtz_cQHV20qirBgXHyBmhthdWfi7QE4WY6BVI0-j4WF0cNHa70ltd9h8VEPlwnoHmW7u-vtcIgkEGuPwHGV0qps6mEdpQmjOQWQu1cft5CE1v8cDDCCYN-i01VOGimpftoeWXY5xmncSjEaczQkYtqXhR9prhPh_b1Yu5TRBW-Vydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجلس از عملکرد عالی وزیر ارتباطات در ایام جنگ تقدیر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129872" target="_blank">📅 16:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129871">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16bfcc9aaf.mp4?token=mea74tqnUR08bfdxn8TUpJVHm5I_4k9WAF2H4ps7ulOx6iJWqMwo2dKmAgDrg2K1jZaLXr4Ncvrg5T39B7s0QSkwAaRW7NzXulcynMMfjQd7TKHuOkcnbjR1S2XGQebdwfzkYjTu8Waoe6xjMuakNg7q2s8-_Gt7so_gHu10vf1fRuR4imSstpjVm5muWnhAPTXRTFttcGSYJ9Rl0mN9D7Q0qVz4tGFqkDHIl2Ydtg5clqmKmvwfa-qVX1tlNWcEn3-yoTyCdbKli_ucTJJb0Bzi4mx7TeiTBGsD3bl0tyHbiHZzIzEWkNLBezqO2p0ATS7q8TZt3hOeR5r7g4OgZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16bfcc9aaf.mp4?token=mea74tqnUR08bfdxn8TUpJVHm5I_4k9WAF2H4ps7ulOx6iJWqMwo2dKmAgDrg2K1jZaLXr4Ncvrg5T39B7s0QSkwAaRW7NzXulcynMMfjQd7TKHuOkcnbjR1S2XGQebdwfzkYjTu8Waoe6xjMuakNg7q2s8-_Gt7so_gHu10vf1fRuR4imSstpjVm5muWnhAPTXRTFttcGSYJ9Rl0mN9D7Q0qVz4tGFqkDHIl2Ydtg5clqmKmvwfa-qVX1tlNWcEn3-yoTyCdbKli_ucTJJb0Bzi4mx7TeiTBGsD3bl0tyHbiHZzIzEWkNLBezqO2p0ATS7q8TZt3hOeR5r7g4OgZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی دوتا دسته میرسن به هم
مداحاشون:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129871" target="_blank">📅 15:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129870">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
وزیر قطع ارتباطات:
تا زمان عادی‌شدن کامل شرایط بانک‌ها، خدمات مشترکان تلفن همراه و ثابت به‌دلیل پرداخت‌نشدن قبوض، قطع نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129870" target="_blank">📅 15:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129869">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
لیست بانک‌هایی که همچنان با اختلال مواجه هستند:
ملت
تجارت
کشاورزی
ملی
صادرات
دی
بلو
کارآفرین
اختلال
❌
نفروختن دلار و طلا
✔️
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/129869" target="_blank">📅 15:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129868">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
شهباز شریف: توافق ایران و آمریکا یک تحول خوشایند است
🔴
نخست‌وزیر پاکستان: پیشرفت مثبت بین دو طرف، نه تنها برای خاورمیانه، بلکه در سطح بین‌المللی نیز یک تحول خوشایند است.
🔴
توافق ایران و آمریکا گامی مهم در جهت تقویت امنیت و ثبات در منطقه است.
🔴
مذاکرات همچنین…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129868" target="_blank">📅 15:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129867">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
زنده از ادمین ارسالی به کربلا/آزار و اذیت شش امامی‌ها توسط دوازده امامی‌ها در حرم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/129867" target="_blank">📅 15:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129866">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaaTePv5Hj_uQTsZ4UY05JlHip8bF62jmsYgTqn4J22iZW5criCKLh__pzBdO0ZTPhBYTqRLjdCtls2nwNJi95rycP6joD4mi_lhn6evTK3lEAv_cQ2WIeOeJsVZZkQQHhBF7Kf7C0bpQY07jJFZIoMiGjI2SjQ0u7aHrLbcseDFhW-PdewEAxAVUeRrTt1jM0iaXehJF38BEPxBNiYXgi_Z0C455EWxV7TFvsEKakJtVePUqPYaaeNfhJAFeVjWA8mcdYabKXdmR7zbG8P6MevSFOWvU7h5l3c_KzVSoqtk9c3aIxLppoTvl6fv2eojDW1stxGQq05BBaKMaDI7Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لحظه ورود عاشقانه پزشکیان به پاکستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129866" target="_blank">📅 15:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129865">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=RmSgShCdJR7_XwiQRKqUvddHOUeihQuVNU32EsMoXqyTGvaVzpnpfE24Pwjp6UQJbWiqJ9h_yljDBwA13d7UJ9TkMxrd0YTZA13M08ECjDwzY2By-mbogs-fCLOk4RyjLFtTrbr6_3vEaWQjJz4zyGbOHH92jYMBcG4aKvQ-Gmr5GH_EMO751AHPxENztOxQeRwRgFQnEwLI7klTRKGsrTfgTGB5rHvCWHzFjXPEJS3pUeRZ707Ul3Za7B8bvZt9JQ3VECP_pKX2DhEwlsZUUcClSDribbT87FCDvUEw8YYNzneT8wIsym8yRAZg4GxMhj1hkRRG-m4UnHJ65zbHFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=RmSgShCdJR7_XwiQRKqUvddHOUeihQuVNU32EsMoXqyTGvaVzpnpfE24Pwjp6UQJbWiqJ9h_yljDBwA13d7UJ9TkMxrd0YTZA13M08ECjDwzY2By-mbogs-fCLOk4RyjLFtTrbr6_3vEaWQjJz4zyGbOHH92jYMBcG4aKvQ-Gmr5GH_EMO751AHPxENztOxQeRwRgFQnEwLI7klTRKGsrTfgTGB5rHvCWHzFjXPEJS3pUeRZ707Ul3Za7B8bvZt9JQ3VECP_pKX2DhEwlsZUUcClSDribbT87FCDvUEw8YYNzneT8wIsym8yRAZg4GxMhj1hkRRG-m4UnHJ65zbHFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوی منتشر شده از عباس عراقچی و همتی که وسط مذاکرات با آمریکا پا شدن رفتن بازی ایران و بلژیکو تماشا کردن
🔴
اینجا گفته بودن مذاکرات ترک میکنیم اما رفتن فوتبال ببینن
🔴
فقط اونجاش که گفت الکی الکی رفتیم سمت دروازه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129865" target="_blank">📅 15:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129864">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4XwEMuOlZNvomy9uQ9DZDeQi7vxSdv591TDMRmLNnTMchXruKyxQhvZoYNayZVZXE1z5lzElxq9jTY2ddWS2ZwDqDnkTpUlUKzGCfrBM5sC4yf4EcZTk95I5P5fpd9-HgHVC2OWRYoOQlPHa_kMFPRNn4-MZrHK0RZmy0Smfvl9idX_MbqAMIcjyHDHNuHDzbTbwaoDvXW2Qi2En57H303aq8xzWVWfL2EF8EkPzPVHDDkOPTXHtXvSOoc8wxUndZtYDNipGKF_ULDiAqPmr_CL5snB_J2ooev27fF5tK-FVQpWjrZjCEBuD1ZHilS1Iz1sd5p7fxDUV1ZBpuQyTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: دیروز 19 میلیون بشکه نفت از تنگه هرمز عبور کرد
دونالد ترامپ در تروث سوشیال:
🔴
«دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز خارج شد که یک رکورد تاریخی است.
🔴
قیمت نفت در حال کاهش است و جهان مکانی بسیار امن‌تر شده است!!!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129864" target="_blank">📅 15:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129863">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
زنده از کربلا/بیرون کردن شش امامی‌ها توسط دوازده امامی‌ها(اکثرا عرزشیا)
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129863" target="_blank">📅 15:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129862">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44e336ac3a.mp4?token=ectkXx6USHIRvioXzdHpbIg2G5WzS3sQuce2h9tf0zxlfufkVLfBCgw6GBmOUUwDzfdurEwIU0IASujUHt2ZoPjHV63humjYUVOf-JHzqvZqPibYdtimtNmTSpZcAVwNdzhTsDx9xYLOV8dTprWivn5UC1hZqFpujeJ6eq0uEwzQwdmedxqlZ4neimLzPUs5iFoLrHhT4o-fe-FjMNLvSbrbiLlYhPt6cI0cyP2ZOs16OkJUiI8tiZpN0Z7tity6Ax4a4Ha4E-gS-zeoSN_OYOD9lLbpVS7Ts8TviE2lr7tNg9SbPGM-YA3owE_NNJcrXguREOrTvmMgY4O1iwOb8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44e336ac3a.mp4?token=ectkXx6USHIRvioXzdHpbIg2G5WzS3sQuce2h9tf0zxlfufkVLfBCgw6GBmOUUwDzfdurEwIU0IASujUHt2ZoPjHV63humjYUVOf-JHzqvZqPibYdtimtNmTSpZcAVwNdzhTsDx9xYLOV8dTprWivn5UC1hZqFpujeJ6eq0uEwzQwdmedxqlZ4neimLzPUs5iFoLrHhT4o-fe-FjMNLvSbrbiLlYhPt6cI0cyP2ZOs16OkJUiI8tiZpN0Z7tity6Ax4a4Ha4E-gS-zeoSN_OYOD9lLbpVS7Ts8TviE2lr7tNg9SbPGM-YA3owE_NNJcrXguREOrTvmMgY4O1iwOb8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زنده از کربلا/بیرون کردن شش امامی‌ها توسط دوازده امامی‌ها(اکثرا عرزشیا)
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129862" target="_blank">📅 15:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129861">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFyBMY7s4kj1ZNnuVjb1eWmvaAl5CkStrAWpAhNMxZrdQty2A2qkxElt7yxxgB9xqEqJ3k4X5IUvCJ_e5btvrYQIynqfDMEDHfvzXa56wR0pc1zvsLAuS1vIpJDwOF73rl8cx7xNNF1InTFK3U8nfm8T67xWBsPxgY1SiUG_Qvo2CEnMRllIDO6dHeXPxz3KMG3l1wYCjEkSI1TKnMiq7WpVFdMM0BVfChwhg9tidjJrbKlyiXIo4EcLrhWdZ5qAC_SvjuBoKOB1_S_fqClEI8NpMcwN5Zx2tQeh5XTpG0gMe7HQubQztRkhLTYo1PajuPRVRG5fgiiINAE-Q-dJng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: با وجود اعتراضات آنها و اظهارات نادرست درباره‌ی خلاف آن، همراه با تبلیغات گسترده اخبار جعلی که تمام تلاش خود را می‌کنند تا پیروزی آمریکا را هرچه کوچک‌تر و بی‌اهمیت‌تر نشان دهند، ایران کاملاً و به طور کامل با بالاترین سطح بازرسی‌های هسته‌ای برای سال‌های طولانی آینده (بی‌نهایت!!!) موافقت کرده است. این امر «صداقت هسته‌ای» را تضمین خواهد کرد.
🔴
اگر آنها با این موضوع موافقت نمی‌کردند، هیچ مذاکره‌ی بیشتری صورت نمی‌گرفت! بر اساس این و دیگر امتیازات بزرگ که ایران داده است، من موافقت کردم که تنگه هرمز باز بماند، بدون هیچ محاصره دریایی بیشتر.
🔴
با این حال، همه کشتی‌ها در محل باقی می‌مانند در صورت نیاز به بازگرداندن محاصره، که در حال حاضر بسیار بعید به نظر می‌رسد. پول و/یا تحریم‌هایی که خزانه‌داری آمریکا آزاد می‌کند، به صورت سپرده مشروط تحت کنترل آمریکا قرار می‌گیرد و برای خرید مواد غذایی و کالاهای پزشکی، منحصراً از ایالات متحده، از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما استفاده خواهد شد.
🔴
این‌ها چیزهایی هستند که ایران به شدت به آنها نیاز دارد. این یک بحران انسانی است و من ضروری می‌دانم که اکنون کمک کنیم، قبل از اینکه خیلی دیر شود. مذاکرات خوب پیش می‌رود!
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129861" target="_blank">📅 15:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129860">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ناآرامی در حرم امام حسین
🔴
بیرون کردن شش امامی‌ها از حرم توسط دوازده امامی‌های ایرانی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129860" target="_blank">📅 14:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129859">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
شهباز شریف: توافق ایران و آمریکا یک تحول خوشایند است
🔴
نخست‌وزیر پاکستان: پیشرفت مثبت بین دو طرف، نه تنها برای خاورمیانه، بلکه در سطح بین‌المللی نیز یک تحول خوشایند است.
🔴
توافق ایران و آمریکا گامی مهم در جهت تقویت امنیت و ثبات در منطقه است.
🔴
مذاکرات همچنین شامل دارایی‌های هسته‌ای، موشک‌های بالستیک و دارایی‌های مسدود شده ایران خواهد بود.
🔴
ما کاملا امیدواریم که این تفاهم‌نامه طی ۶۰ روز آینده به یک توافق بلندمدت تبدیل شود و منجر به صلح در جهان شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129859" target="_blank">📅 14:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129858">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0051256b1.mp4?token=jyBBkP0u4lhG4o97AmaY828dQdVIudJXkAHvKwuDRC_E15lGwQRKgsFQJk7SYQCWhuMngnku9PU39FZh35EeaArea6HpTWbn3uYwg2Ut5K6up2AdeTPrL_yw3WWArtkCUMvRPr7JESx2pYE6WNW9l6RNx34hNIOEoQXLOPXFOCebTMes7TvlxbgkQhfvpFDvS0UTnutLJ1uRKZc6rxTlOKJIJ1U7JLuibT4vzs3_mbEnVAfMZpU38mxuGRnxuUE9TSXl2T3MVsA0NcQGOmIS1UUA2ZeLwqwNIdXkSUCw84f3vySpKpF5do77PJno7uBsO6ppOrweugTbVzf-bK-AYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0051256b1.mp4?token=jyBBkP0u4lhG4o97AmaY828dQdVIudJXkAHvKwuDRC_E15lGwQRKgsFQJk7SYQCWhuMngnku9PU39FZh35EeaArea6HpTWbn3uYwg2Ut5K6up2AdeTPrL_yw3WWArtkCUMvRPr7JESx2pYE6WNW9l6RNx34hNIOEoQXLOPXFOCebTMes7TvlxbgkQhfvpFDvS0UTnutLJ1uRKZc6rxTlOKJIJ1U7JLuibT4vzs3_mbEnVAfMZpU38mxuGRnxuUE9TSXl2T3MVsA0NcQGOmIS1UUA2ZeLwqwNIdXkSUCw84f3vySpKpF5do77PJno7uBsO6ppOrweugTbVzf-bK-AYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سیل هجوم ملت به شمال
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129858" target="_blank">📅 14:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129857">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
کل کل شش امامی‌ها و دوازده امامی‌ها به صحن حرم امام حسین کشیده شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129857" target="_blank">📅 14:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129856">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53c18f2de.mp4?token=X5dgygxfvJmT4g70RgZvggt7j8w_e2H-So0A7XCPIi6tLyd6hjRrmOi6kW8YEj09v34n0I2BsKlzAY_mXpkS9ftLqGie6lzUVpopPdG-YqgPVcWvLfrOVMqtXhwjmQn5xc_H0XX-UyVNM3YyqJunmpjfYp6cVgTJ7bOyN0jskM3gANRBy2NMHnO0qHWQ6SsQE3TxZDVeV_MxwPyj3AWMrGW-Xf9D05O1OdktosuxdFosg7WORDqrYIQh8zSVES9sqJD7fFzkwIdoCnl4idJpMc3eYrSfEK-N5SX8EYnpKITYbygJU0Na9jFFjteZ3zsGb7OaB1_RzXF5zf4FoqkSqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53c18f2de.mp4?token=X5dgygxfvJmT4g70RgZvggt7j8w_e2H-So0A7XCPIi6tLyd6hjRrmOi6kW8YEj09v34n0I2BsKlzAY_mXpkS9ftLqGie6lzUVpopPdG-YqgPVcWvLfrOVMqtXhwjmQn5xc_H0XX-UyVNM3YyqJunmpjfYp6cVgTJ7bOyN0jskM3gANRBy2NMHnO0qHWQ6SsQE3TxZDVeV_MxwPyj3AWMrGW-Xf9D05O1OdktosuxdFosg7WORDqrYIQh8zSVES9sqJD7fFzkwIdoCnl4idJpMc3eYrSfEK-N5SX8EYnpKITYbygJU0Na9jFFjteZ3zsGb7OaB1_RzXF5zf4FoqkSqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کل کل شش امامی‌ها و دوازده امامی‌ها به صحن حرم امام حسین کشیده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129856" target="_blank">📅 14:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129855">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69da8218d5.mp4?token=Mpu6wi-bVJ_7Hx3Fvc8h39hCXMgxnbzE-ZCjSpNmtYZEpPT1EcWU099wT9UocfB1dDTztgI3-Ar5eVAq_Zv2tylg4Kv3kwezQQ6FGSTR4E8JEctJYiDDkyCrcH4iPn8M2rN6D-odewaUBhXt5nfBNg7F-py2HYZ-Tu1C58RbXGAnv6IjxtuIk0QGQRpShqxVmiyF1YkZJ5PthRumRIOv-ZdP5YromtRc93USUeCSyNO5yoR-nyjpZGb2fEkM7eOZDddVUkiH4Lz-cbU6x9Hgit9KzFswfBYDanTQ-1hF7z3cCgEckDEm8vrJ7y8htHsHswsLqRX5wrfLecmSzKWxVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69da8218d5.mp4?token=Mpu6wi-bVJ_7Hx3Fvc8h39hCXMgxnbzE-ZCjSpNmtYZEpPT1EcWU099wT9UocfB1dDTztgI3-Ar5eVAq_Zv2tylg4Kv3kwezQQ6FGSTR4E8JEctJYiDDkyCrcH4iPn8M2rN6D-odewaUBhXt5nfBNg7F-py2HYZ-Tu1C58RbXGAnv6IjxtuIk0QGQRpShqxVmiyF1YkZJ5PthRumRIOv-ZdP5YromtRc93USUeCSyNO5yoR-nyjpZGb2fEkM7eOZDddVUkiH4Lz-cbU6x9Hgit9KzFswfBYDanTQ-1hF7z3cCgEckDEm8vrJ7y8htHsHswsLqRX5wrfLecmSzKWxVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دعوای 6امامی‌ها و 12امامی‌ها در کربلا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129855" target="_blank">📅 14:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129854">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
تعطیلی استان تهران در۱۳ و ۱۴ تیر؛ دوشنبه ۱۵ تیر کل کشور تعطیل شد
🔴
بر اساس تصویب دولت روز‌های شنبه و یکشنبه ۱۳ و ۱۴ تیر استان تهران و دوشنبه ۱۵ تیر کل کشور تعطیل است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/129854" target="_blank">📅 14:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129853">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f83b16848.mp4?token=RpIZIovCIUuDjx-RuCBnAdvYo1-6ihjLmMp-jXMsgWyVQfl_X5Rnk66_LAmebMT92eGA-6f69lkgl2-8eos4vAdbXQT-BO_t7M0Vl5Up3HlXsWm930m4g3APZDPA8tvDUeEmOYA0bactNiGtdo5zx7QXlVHW-uzoeIbPZ2RTXEHTZDSjy7v1Ae4ASKjggT69JLxcwyxo21EnYoxsGlyViOovcIo-66h2YKyOd-Oc1nwUao87AHZFFb6RJCpczHt0ziv5KPbDDv4LX1O9KYyqB4y7nHyHyCxOokMpRiuKjf28aAqKbqbhtyDaU3hRzFfNXzM2y720PxGYJ267caRHY1iSxkh-pFk1C1xBp_AdmKT_W1dyJIYwAaWahQd9ekiAuzQxAYUIpJetClG_NX-WfrST7iUsDgbaZsQWTZCIA0sGCDbEoAx0GY2INIZb0dpjl9iu5ugeeBf4Qqo2CnSrT2lNQsccmeGoIv25ILpWyV7NZNPYiXvkoArXpDTqhTqtSzC9i9ifaXysXe2ExrzHlDBZhBY_wUEXE29YLH_ju5WfNr9SzOV5ya0in-PO2YHXnlrY_Tp4MH-LIENyIfM-nc2QA25AjEJW5mw5OfAlDPocJ-Ewd2CVo9MxUoyUk2l39Lg5P1GEV9T6r4j7LCU43vUxmDzm6fHCKGAztuNa9KM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f83b16848.mp4?token=RpIZIovCIUuDjx-RuCBnAdvYo1-6ihjLmMp-jXMsgWyVQfl_X5Rnk66_LAmebMT92eGA-6f69lkgl2-8eos4vAdbXQT-BO_t7M0Vl5Up3HlXsWm930m4g3APZDPA8tvDUeEmOYA0bactNiGtdo5zx7QXlVHW-uzoeIbPZ2RTXEHTZDSjy7v1Ae4ASKjggT69JLxcwyxo21EnYoxsGlyViOovcIo-66h2YKyOd-Oc1nwUao87AHZFFb6RJCpczHt0ziv5KPbDDv4LX1O9KYyqB4y7nHyHyCxOokMpRiuKjf28aAqKbqbhtyDaU3hRzFfNXzM2y720PxGYJ267caRHY1iSxkh-pFk1C1xBp_AdmKT_W1dyJIYwAaWahQd9ekiAuzQxAYUIpJetClG_NX-WfrST7iUsDgbaZsQWTZCIA0sGCDbEoAx0GY2INIZb0dpjl9iu5ugeeBf4Qqo2CnSrT2lNQsccmeGoIv25ILpWyV7NZNPYiXvkoArXpDTqhTqtSzC9i9ifaXysXe2ExrzHlDBZhBY_wUEXE29YLH_ju5WfNr9SzOV5ya0in-PO2YHXnlrY_Tp4MH-LIENyIfM-nc2QA25AjEJW5mw5OfAlDPocJ-Ewd2CVo9MxUoyUk2l39Lg5P1GEV9T6r4j7LCU43vUxmDzm6fHCKGAztuNa9KM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار عراقچی با رئیس جمهور و نخست وزیر پاکستان ساعاتی قبل از ورود پزشکیان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/129853" target="_blank">📅 14:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129852">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
اختلال گسترده در شبکه بانکی کشور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/129852" target="_blank">📅 13:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129851">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
نتانیاهو: ما ضربات سنگینی به جمهوری اسلامی و حزب الله وارد کردیم ولی پروسه ما هنوز تمام نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/129851" target="_blank">📅 13:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129850">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
شهباز شریف نخست وزیر پاکستان تصریح کرد پیشرفت مثبت در مذاکرات بین دو طرف نه تنها در سطح خاورمیانه، بلکه در سطح بین‌المللی نیز یک تحول خوشایند است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/129850" target="_blank">📅 13:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129849">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
منابع العربیه: عباس عراقچی، وزیر خارجه ایران گفت‌وگوهای جداگانه‌ای با مقامات پاکستانی انجام خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/129849" target="_blank">📅 13:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129848">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
نماینده دائمی ایران در سازمان ملل: تنگه هرمز باز است و هیچ‌گونه عوارضی برای عبور از آن دریافت نمی‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/129848" target="_blank">📅 13:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129847">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
نتانیاهو: حمایت دوستان آمریکایی‌مان را بسیار ارج می‌نهم، اما نیازمند رهایی از وابستگی و ساخت یک نظام تسلیحاتی مستقل هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/129847" target="_blank">📅 12:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129846">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سخنگوی هیئت مذکره کننده:
آنچه در مذاکرات به دست آمده، تنها بخشی از حقوق تضییع‌شده ایران است
🔴
لغو محاصره دریایی به معنای اعطای امتیاز به ایران نیست، بلکه به معنای بازگرداندن حقوقی است که پیش‌تر از ایران سلب شده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/129846" target="_blank">📅 12:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129845">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ba9HECCh-VqczHYWsKXMNItyjv3BNW807w7Qv1JjbYSG9TeRRu_UdnH-4e7uwTFx89XDWvjsYxRVXSeGYwmEm_Q2w01d7QPlotWp7Z-WuSRDiAA0i03x_8keXQFWEhIyN19Oet6i4DFXTd46ROvMN_98VGpHIb-EZL-7iEF0xbUmyMnqYM5Hh2H22I_wLSjtJwNO32uBKvzp5P9nXTj8AST7NeKSBn9SqvkZEg5teWlv6z1BxPayyI1qJIG-rFVKzd5CQ_TIRysZk-qnALV6tQ60lgWoEVgFsy1aHC7z0CkpEN3DWGcBWZGEKESzYGyKg1vqyQWmXxv1VQqj6Zv7Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت نیروگاه برق کرچ روسیه که امروز مورد حمله اوکراین قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/129845" target="_blank">📅 12:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129844">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vn3kHHJcmP6zz4EMUmOZ6-2n-wUV3xlt8_yi2MTeSwapa6DgNKTdfG-uFJzmh0RgLRuAOl9_rF7s_9HxxUL5PIdzrxG8WUIk2Rn1BoXd62gYn7BzNndaTdR_uq0CQi-FU9XVoYWsMT7Ko_QAQ6TJnpKsRRyhQhsdVfL3UX5RKleON2QUpv1Zeq_seTyohgD7MhOcMYTefxIS8Vy8u75iYGjgCBbn2dJhsHdBHaz4ATkS31fQZrBBTrmhr6UBxf62vTxRW4n-mrfZYyTpXXCl5s1Ttg_vZFWBgtaHr0lLJZPMZmSgoKEVch_EQo8lRk2c00gGCN8u3flnrEZfJtkjAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
المیادین: عراقچی یکشنبه به بغداد سفر می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/129844" target="_blank">📅 12:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129843">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4VxpbWwdK1cCf6KJc2SVmQ6aILcilK79AYqoTLRdyjauXE3Kr8UNPzsnbmDgAdQZScssRCY_w_uik1bDNOFBeV9uTm6bVdxxgWPtLw2NLEqKMiNYW9ES4gw2vew2X7tSMROfYfCfH-R8y3O26jwbEjU25a8WN_2Ruv9Ftw5rTdjc0eASJbYV3ursRA114MD0hU_Sf6lj9pfR7TqhK3ATyz1lvwAeBzKQcZGmZ5xgUgS-usqqVhsnxhvoAB15HcT81ZrtePHXHyDIHpeX0E94C7lH3-qnsLbdEao0GpzTibiM6-cBRf_cBsNcAslvy0cf6pC6GS76015giMyvd1OwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات ارتش اسرائیل به کفر تبنیت جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129843" target="_blank">📅 12:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129842">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: تا زمانی که حزب‌الله کاملاً منحل نشود، از منطقه الشقیف در لبنان عقب‌نشینی نمی‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129842" target="_blank">📅 12:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129841">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: جلسه چهارجانبه با حضور ایران، آمریکا و دو میانجی حدود یک ساعت و نیم ادامه پیدا کرد؛ قرار بر این شد که پس از یک وقفه کوتاه نیم‌ساعته، جلسه ادامه پیدا کند
🔴
نشست چهارجانبه پس از تهدید ترامپ تشکیل نشد و بحثی که ادامه یافت، تبادل پیام از طریق میانجی‌ها بود
🔴
پس از تصمیم به توقف مذاکرات، هیچ تماس مستقیمی با طرف آمریکایی نداشتیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/129841" target="_blank">📅 12:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129840">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: دربارهٔ اموال آزادشدهٔ ایران هر طور صلاح بدانیم تصمیم می‌گیریم و هیچ محدودیتی دراین‌باره وجود ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129840" target="_blank">📅 12:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129834">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VYWOHqUJnTqLebUh_VYUJq9QObkr5TyKjcNXSDywOAeS3fCc0vOgvcBrwKmvPEztu9KhMqlNE9hOQbrEEIgiNIu3wtG2B7-mZ8HDIQliUHnqRB4Udd20BXOs5jpCSE3GMTklAp-hJJiYWDYu7w7BAeWcaJzVacbk_zM6PPN84T7R4IpKq2YuGzwdUQqss0WEsCLHTkbyntxi1uD4v4nQovpg-8cw0NKnj9eC4jeRhU_gbxZcFnI2QI5ZaBJS8k8ckYj32N44xfs7q0uhCPB4RWoMGQBLYAl-QMN-CbLG44hCUVI5V6mVLGFDmcpLr_oh-S6yn7GKswg-Ib_qwGnzyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kNRXyUQSv_SAayn7ilGpIUvyJu_rf7SiMdc1xJgyGunhucDLwyhdVtMN3jSBG7D0yJvA3SEy6DZDng2-I5w1yoe__irb00qrcAS9edmv4qB7msjsBdgBl8ZGhvKE2EZfyG5Fj1pu7qI1xF4PKRISUFuBhe07ou5D2JHCCbR-v_IqE5T00QQP6qX0C7o4YJhv2aisn4DCOMbDzwC-UqYHzu4VBPg9sZxJoNIeetrSR_0JVvb5Zl2Wlv5BWo9655ftmJk2j_WiG7RNFNeJwtU9U15xLwcgKRpWwAGhCbd6SBQ1AW0aI77CVJ8mAWIRu5CtbXZ0Fwu79SC1eOcBYbhbIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hTQjrGbysmFBAj98okS-0WqW74L0dZrKepeEa15z3hQHtdSsdI4byE2GRFLQzqII50woF9hAP2oRUEZDRRXoe3zFQhbDJH6pmAtl9XrUroYHh_sPdIq4GOgV6O4dhNwxl6AOzYkVAcaszWdJ9LMBi5D_cUnAwQi7f1o4m9QUHy9TQj24PMP6UgGMu1UnUDrUdYyhdl4ehY5jQm2b-KhKu2-jcg19kzs2qNlf1Nfwp92MWZh-rXdNOy629wVjMpo36IQ00nu2o7hpPO1RjcpVSu370V-FBxrsuEOjnQEuSy7C8LyJqGcNtc-aIFMHs5DQjVdsLHZ0JIrjKyNwLLmaVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KEZon6bCoKEIvCqu0_-S2h5gpJSd8SkwmMmzLkR_P33TyWhDwcmMVLXvVWpDZ56f5mwvsyxdrY-5Nc6WacSPj3ww9SP37UJpNfjAof5MHJ_reuqXN3SiNZL5WJtVwamQGHZtwH1PQWxuEEbjejp8ao9v--SmmrE77_fM9XyOSLc73J7sQ50-cu8sQALxl5RYMxhUAuX643kHxubvXxEjxQ7qWsv2WyM6auE7hvvC5FPvORzABJx7pf36iZNlzLfHTx5Lu_WUW5x_4lT6hbUIgcTsLOraiyAOKM7BCv-1WXPQB8rfvePrvwsRabFLQZ-nnnYa8DMw0XzAVjbF6qGfOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q6aZyUqL6J2feDllT8-sd0JBdJRCYXcLW3FFHMT28PedtMXy6jYXoM2yrYxqgkYp1loGOc-KKzraxRvna54XomvRT15oa6InnCEW5AcwFc7adpgCAtrLbuxJLGVlXm9YBpcOtYlEsKCVzxtIGX-4i_6bqYRzYsGqWCruaLknLoPTWZr_IjPt25D9m6vA9WzhvIwYKxSmUpluRLLuV-PrUZzAbC_Uxybs-ir5KAm2zcbETJv2vXaWEgOYQaVxs6HbBHAcY9hhAAmIwKrBLG-P7gn0HP7_Vd5dwYF11d0svm1EpMSnBeb8MS811mWqTIZS9awzroGKFhSOlDSM8eXnjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QUwoW_KcsssUpCdVeOIezmLeIdsmbBHEZstzGprEigHgmx-c-NUIIBlK-N6F455Qe9DBMy-_K36mebuuZXPmSvNExDW7ci6LXGa5LUdYakAHl__fhcsTXP6mB4xIwweIz4sd1Kkcp3LDPouJY8aCd5zTJq4hVI8sGg1x5jYPojzqxuqtx9jKWt8XfLgKzaz8-Gb_dOoCjJ08PZYfFo8hGGvru9J3m56mgqHwOoVDJXUNHL-P8t6p6CrznCRU7ytaESrHILIMcmhV-QIx-UxZ-qbE3SxvyUZQtRAYV-yPMN_VzXau9UzZb69jtWGu4lVPU0edeS58hx05kmH2g-NssA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از دیدار و رایزنی  قالیباف و هیئت همراه با سلطان عمان در مسقط با دستور کار ترتیبات مدیریت تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129834" target="_blank">📅 11:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129833">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a802fb01d.mp4?token=PY_PAXQo_OX6Yd6Wn1uj4uSycCKlFenTeqNPixxZQvLaR1GjR7ijgfwMEs5wRpe_Eo_VCVgs3w5MEywiCMkOxxl0NPqLf7GrRdERWqgKlTa_l2NJda9i98PzFLc6hh-kp98VwxVSd-3Ubm2fDk6F6kVzRwqbOmo1v1O9OoihB1RT1sBYf9wysmiT4S9gijz37-tVbXszlbuTP78MfOu7DGA6My9uRsTHmj2XdntnfpLkzzjr_EjI1Pp3a8SDuV__zjGt56K1FoTYQm3sobGJPej88F361FEnX0_JkDi09SzYPJp0RqPJrgkcjL0AQDT1w0EyPoQJ-ADfK_3a6kSgJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a802fb01d.mp4?token=PY_PAXQo_OX6Yd6Wn1uj4uSycCKlFenTeqNPixxZQvLaR1GjR7ijgfwMEs5wRpe_Eo_VCVgs3w5MEywiCMkOxxl0NPqLf7GrRdERWqgKlTa_l2NJda9i98PzFLc6hh-kp98VwxVSd-3Ubm2fDk6F6kVzRwqbOmo1v1O9OoihB1RT1sBYf9wysmiT4S9gijz37-tVbXszlbuTP78MfOu7DGA6My9uRsTHmj2XdntnfpLkzzjr_EjI1Pp3a8SDuV__zjGt56K1FoTYQm3sobGJPej88F361FEnX0_JkDi09SzYPJp0RqPJrgkcjL0AQDT1w0EyPoQJ-ADfK_3a6kSgJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: تا ۳۰ روز پس از توافق نهایی، نیروهای نظامی آمریکا باید از منطقه پیرامونی ایران خارج شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129833" target="_blank">📅 11:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129832">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18a1a4f110.mp4?token=ugx7DGRGCnz8E7MdR-AtSyfKGK6tc1y0dAQZLJPGjdlv11jr92muzreR_zd6-3hI1Pzbf63tVcyFyuGftd254U9uv2h-QBcJ-jq7BLbSWrYqjdheAKUQOpeL5E29P8j4KKPUjSoIIDeK5VKtupa-2Z-bl8rciRrrrgXDX6SiQIzET-Bj0ARcvojXyu8AsMT_SMTM60BLdGd2vpl5ka1QdysT1comoIxyApsHtZYFFJkSoE2eiIQ50hlOzcMG5ZHx8yHvqPqTW4-uAkzaIRs5Ptg4I8-vCiOqpeV_dLbx0SDybHYQJOUo8GbihIAxSQ9oA8hMPfE-3dY_0G099Bh8SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18a1a4f110.mp4?token=ugx7DGRGCnz8E7MdR-AtSyfKGK6tc1y0dAQZLJPGjdlv11jr92muzreR_zd6-3hI1Pzbf63tVcyFyuGftd254U9uv2h-QBcJ-jq7BLbSWrYqjdheAKUQOpeL5E29P8j4KKPUjSoIIDeK5VKtupa-2Z-bl8rciRrrrgXDX6SiQIzET-Bj0ARcvojXyu8AsMT_SMTM60BLdGd2vpl5ka1QdysT1comoIxyApsHtZYFFJkSoE2eiIQ50hlOzcMG5ZHx8yHvqPqTW4-uAkzaIRs5Ptg4I8-vCiOqpeV_dLbx0SDybHYQJOUo8GbihIAxSQ9oA8hMPfE-3dY_0G099Bh8SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: ما در توافق با آمریکا امتیازی دریافت نکردیم؛ تا الان صرفا بخشی از حقوق تضییع شده ایران را پس گرفتیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129832" target="_blank">📅 11:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129831">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58a20450c.mp4?token=em9mntvdAP39ItO1xuFcREUzdYIARB8icxE7bVGqw_eBpOgzkzxJ4he34FH_y6TNvpsqhVOEhd-_0KidnGbw-CdyVnl1jfmV-Tdv62s2shkV-Wr7N1JsmkLGTdvyR0lB7M7vZpFEBQRaMImQ_tl4BwQQOvMslyPrR5vZXE5EeWF6CiP75t2LN7VsbqBBlBNBJdqOBQGgF2JDaBxOYvUqCnSWlyB_4TtHFIcryTXD57gQVtkZ7zGinaRJOl9IndvHNRxnroBlg32U3Qho55R_QcjOFN4Cz6YVDFgr1jw9wG0YCs86CSeWUtke9tl53F2oWavRdyLq4naTHwmILIjYqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58a20450c.mp4?token=em9mntvdAP39ItO1xuFcREUzdYIARB8icxE7bVGqw_eBpOgzkzxJ4he34FH_y6TNvpsqhVOEhd-_0KidnGbw-CdyVnl1jfmV-Tdv62s2shkV-Wr7N1JsmkLGTdvyR0lB7M7vZpFEBQRaMImQ_tl4BwQQOvMslyPrR5vZXE5EeWF6CiP75t2LN7VsbqBBlBNBJdqOBQGgF2JDaBxOYvUqCnSWlyB_4TtHFIcryTXD57gQVtkZ7zGinaRJOl9IndvHNRxnroBlg32U3Qho55R_QcjOFN4Cz6YVDFgr1jw9wG0YCs86CSeWUtke9tl53F2oWavRdyLq4naTHwmILIjYqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی : قالیباف به چین میرود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129831" target="_blank">📅 11:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129830">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fec08cc90a.mp4?token=GChniO4phq77AlPljIJ14cs-rCFbqCAKL4gaExw1WPOYgtvNQLLBD9fGyELws2A7Fh1KoiE0uBRqVU7KZ9kpxTbmgD7jvBEdaXz5YWJKP1mINfAIfPSB6tPDmW55lgi3TOx5LPzPGFOeIN2O7-faOlAhsdTlR-wtaFgL0rTZsvA0dGVMB-WLhpaAp3XogApPLIHXRIvxpNBz5JnjY5CvAlLS9nKJalNG6LIEHKYBC8HtIu_NiJjOxNNLFszCG4LI4LE1gFDpdCKl3oQlRtbTJTDGjZW-UybjuLOTxEGfLItdA2mHiL0hgjQx-lblkadHltKyf1848feZna7gbXK49g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fec08cc90a.mp4?token=GChniO4phq77AlPljIJ14cs-rCFbqCAKL4gaExw1WPOYgtvNQLLBD9fGyELws2A7Fh1KoiE0uBRqVU7KZ9kpxTbmgD7jvBEdaXz5YWJKP1mINfAIfPSB6tPDmW55lgi3TOx5LPzPGFOeIN2O7-faOlAhsdTlR-wtaFgL0rTZsvA0dGVMB-WLhpaAp3XogApPLIHXRIvxpNBz5JnjY5CvAlLS9nKJalNG6LIEHKYBC8HtIu_NiJjOxNNLFszCG4LI4LE1gFDpdCKl3oQlRtbTJTDGjZW-UybjuLOTxEGfLItdA2mHiL0hgjQx-lblkadHltKyf1848feZna7gbXK49g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مجوز فروش نفت و محصولات پتروشیمی دیروز صادر شد و از همان زمان قابلیت اجرا دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129830" target="_blank">📅 11:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129829">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9061886b7c.mp4?token=nvyAY5_GH_1GVMzQ8smgc-4hiNfxJC4tU4dxCROdwJfQAKDg2Tm129KoX2gFYEMStPMzIVRg90TYZQ005AaL6-4uEGefvh2bSSogKpdu4Bo3T_JE7IXtiPsk3eJgqgLIWkLIogmywyfV_KX2FKnaBwu7gTpYo8s1ADXTbNShjVL5JmTnOmrgZaJXvyyZGwRgQhXroo6BMy09ERklouvoMOzdfiGZyVKu7Noeus1xLexje4iu53xsI8X4_E7EltLFUKJLPgc9t3h_tAfopOEScFkPmjCrI709VdMF_uZrJv2DJj7GVVh0yzk7vLTMS5H8hArmbqWORPprr_PItb1OyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9061886b7c.mp4?token=nvyAY5_GH_1GVMzQ8smgc-4hiNfxJC4tU4dxCROdwJfQAKDg2Tm129KoX2gFYEMStPMzIVRg90TYZQ005AaL6-4uEGefvh2bSSogKpdu4Bo3T_JE7IXtiPsk3eJgqgLIWkLIogmywyfV_KX2FKnaBwu7gTpYo8s1ADXTbNShjVL5JmTnOmrgZaJXvyyZGwRgQhXroo6BMy09ERklouvoMOzdfiGZyVKu7Noeus1xLexje4iu53xsI8X4_E7EltLFUKJLPgc9t3h_tAfopOEScFkPmjCrI709VdMF_uZrJv2DJj7GVVh0yzk7vLTMS5H8hArmbqWORPprr_PItb1OyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: طرف ما بر اساس یادداشت تفاهم ۲۸ خرداد دولت آمریکا است/ تعهد ما مبتنی بر تعهد طرف مقابل است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129829" target="_blank">📅 11:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129828">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5565eeff1.mp4?token=JOoxoIiLb0hopTAUG8WsAcSwFZjfLem0SOOGklOq8MgVWlIo-nT4Xniup19esKYXTmL1el5TlxtqdE8k_Z6FnU2uGLv5XFUwMSh5cs3Sp_4XdkCXQBRplen48OwKm9AHiWUHC049QrXyBJSf-QNGwEfNE8OMuWt8OThuwp8R-p8fOgrkixt0dp2vNi3goDiLDqBom71DPdVg1WQZaf0yczhS0n7AaOxei30ODVrpH_uruKtIJDFe2oymKTCLDEoQMlTbS6KGHJbZWlBP4jGdVirtG4eXM-8wPBGQlJ5K1_JGiOGSPNpYfi68o-k7NLrRjbnxxCGZYvNvY_i1LNr02Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5565eeff1.mp4?token=JOoxoIiLb0hopTAUG8WsAcSwFZjfLem0SOOGklOq8MgVWlIo-nT4Xniup19esKYXTmL1el5TlxtqdE8k_Z6FnU2uGLv5XFUwMSh5cs3Sp_4XdkCXQBRplen48OwKm9AHiWUHC049QrXyBJSf-QNGwEfNE8OMuWt8OThuwp8R-p8fOgrkixt0dp2vNi3goDiLDqBom71DPdVg1WQZaf0yczhS0n7AaOxei30ODVrpH_uruKtIJDFe2oymKTCLDEoQMlTbS6KGHJbZWlBP4jGdVirtG4eXM-8wPBGQlJ5K1_JGiOGSPNpYfi68o-k7NLrRjbnxxCGZYvNvY_i1LNr02Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توضیحات بقایی درباره خروج خبرنگاران از سالن اجلاس چهارجانبه: ما برای کار رسانه‌ای و تبلیغاتی به سوئیس نرفته بودیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129828" target="_blank">📅 11:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129827">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
مایک والتز، سفیر آمریکا در سازمان ملل:
جمهوری اسلامی با بازگشت بازرسان هسته‌ای به ایران موافقت کرده و این اولین گام برای توافقی گسترده‌تره.
🔴
برخلاف برجام، این بار بازرسی‌ها باید در هر زمان و هر مکان ممکن باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/129827" target="_blank">📅 11:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129826">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60eb3a2c96.mp4?token=JprendbKtPnDCcS9lhdLNEgmnR-SX3h7_muy1LFNHji9m8Zp__1aa1OgX3uoPCL-ey8_jo8pxTf4HH8Ft2qukMUjJKkVfmEeZNjibeSp9H9c9gIiWVuApUWo39ODr4pUDLS7UfLSIXMe0GcwF4VkcvOu23pIq_-3ySb_uKkwsabhznCOz3YN_ix6kkas4OpZ8RmzXwySpKBwAVnFtAwv7fn-exC4NLMBHZJaUjUyOWh7tMGLjT28PTHv2cnCdFNHajl-GAG4xgY5SL-v1_N8DggvAPGNVSd0YRHtJuDK14KzSLTRy8b9DqWpYT86F7OdQZus7CmhQ5o83pq_ef1yYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60eb3a2c96.mp4?token=JprendbKtPnDCcS9lhdLNEgmnR-SX3h7_muy1LFNHji9m8Zp__1aa1OgX3uoPCL-ey8_jo8pxTf4HH8Ft2qukMUjJKkVfmEeZNjibeSp9H9c9gIiWVuApUWo39ODr4pUDLS7UfLSIXMe0GcwF4VkcvOu23pIq_-3ySb_uKkwsabhznCOz3YN_ix6kkas4OpZ8RmzXwySpKBwAVnFtAwv7fn-exC4NLMBHZJaUjUyOWh7tMGLjT28PTHv2cnCdFNHajl-GAG4xgY5SL-v1_N8DggvAPGNVSd0YRHtJuDK14KzSLTRy8b9DqWpYT86F7OdQZus7CmhQ5o83pq_ef1yYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: توانمندی دفاعی و موشکی ایران هیچگاه موضوع مذاکره با هیچ طرفی نخواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/129826" target="_blank">📅 11:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129825">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27922d07c6.mp4?token=Np8Ngbg5MnjdsDkn1oPvAVzhWHZe0FQdQD73mUn2wOBsVVQeqStSi5nFr6HDWllKIWJOPAQ-Y3MeZF9_3F8vykacjdByFaOQFUOgW11230jiDfh9UtOXSzEaLiLdkHofrs9hkf--YmdPeAyYcjadrxitaNWleAsjs7zVSgma7ck2dYLnAsvyA8HwLQU3WAbpadB36HBXZriB7KTOau04gj5hIsPpBYRuTipvCTk0BF-PQmkj5EstS_R6psP2JiQBLEyESVQuH530sIk1ambcNqWzMhCyBP26PXRiHc6-RXOXtUlxeenQ53dj_zTgJORmCpSxPoxJyZ_46l6hysetpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27922d07c6.mp4?token=Np8Ngbg5MnjdsDkn1oPvAVzhWHZe0FQdQD73mUn2wOBsVVQeqStSi5nFr6HDWllKIWJOPAQ-Y3MeZF9_3F8vykacjdByFaOQFUOgW11230jiDfh9UtOXSzEaLiLdkHofrs9hkf--YmdPeAyYcjadrxitaNWleAsjs7zVSgma7ck2dYLnAsvyA8HwLQU3WAbpadB36HBXZriB7KTOau04gj5hIsPpBYRuTipvCTk0BF-PQmkj5EstS_R6psP2JiQBLEyESVQuH530sIk1ambcNqWzMhCyBP26PXRiHc6-RXOXtUlxeenQ53dj_zTgJORmCpSxPoxJyZ_46l6hysetpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: مجوز فروش نفت و محصولات پتروشیمی دیروز صادر شد و از همان زمان قابلیت اجرا دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/129825" target="_blank">📅 11:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129824">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: برای ما جالب است که فلسفه و هدف جنگ، که قبلاً اعلام کرده بودند از بین بردن تمدن و فروپاشی ایران است، تقلیل پیدا کرده به ثروتمندتر کردن کشاورزان آمریکایی.
🔴
ما در رابطه با اموال آزادشده ایران، هر طور که به صرفه و صلاح کشور باشد، تصمیم می‌گیریم. در رابطه با خرید کالا، وزارت کشاورزی ما و سایر بخش‌هایی که متولی امر هستند، هر آن‌طور که تشخیص بدهند، هم بر اساس قیمت و هم بر اساس کیفیت، تصمیم می‌گیرند. لذا هیچ محدودیتی در این رابطه وجود ندارد.
🔴
مجوزهایی که در رابطه با بحث فروش نفت صادر شد، از دیروز اجرایی شده است. سایر موارد هم مشخصاً در رابطه با هزینه‌کرد از دارایی‌های محدودشده یا مسدودشده ایران به همین ترتیب است.
🔴
آقای همتی دیروز توضیحات مفصلی در این رابطه داد. مهم این است که اموال مسدودشده ایران در دسترس است و برای استفاده آزادانه ایران، هر طور که تشخیص بدهد، برای تأمین کالاهایی که مدنظر کشور است، قابل استفاده خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129824" target="_blank">📅 11:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129823">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
بر اساس مصوبه امروز شورای شهر تهران، مترو و اتوبوس‌های بی‌آرتی تا ۱۹ تیر رايگان می‌ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129823" target="_blank">📅 11:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129822">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
الجزیره: «تغییری بزرگ» در سیاست آمریکا؛ ایران اکنون می‌تواند نفت خود را با قیمت کامل بفروشد
🔴
این اقدام صد‌ها میلیون دلار درآمد اضافی برای اقتصاد ایران به همراه خواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129822" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129821">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d72b824858.mp4?token=Oyhf6jsxhu7y-W5M4_u1ZztEZwHEjOuZOoJ9uTWRJM5fJXe6oPXM7xuKo99Qk14mFDBECFBVT2UxL6sbIJYMJosCej9F2_UmPfXsN-KIXL5yrDxYOGq1dCQRyFbaAmMqPvSL0Y6E5505YleBaKmDwnJJ1Sm5prMr1FpnKpwN6ggogMRoICDnmamwdJcI2fTrkpPd7NMmpNso6FezXq_SAPFqDjpCumAVbwekvdJNsaSorrcVFrKR2AK4fsu_pyXstfohEv4zAQqC04Ow3Rg4X3mpcklOT8Z_q4wKZimYWxTwimVbFsijDSoYkhvdfCApT9OIahXw6tkO8yV3UPJHPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d72b824858.mp4?token=Oyhf6jsxhu7y-W5M4_u1ZztEZwHEjOuZOoJ9uTWRJM5fJXe6oPXM7xuKo99Qk14mFDBECFBVT2UxL6sbIJYMJosCej9F2_UmPfXsN-KIXL5yrDxYOGq1dCQRyFbaAmMqPvSL0Y6E5505YleBaKmDwnJJ1Sm5prMr1FpnKpwN6ggogMRoICDnmamwdJcI2fTrkpPd7NMmpNso6FezXq_SAPFqDjpCumAVbwekvdJNsaSorrcVFrKR2AK4fsu_pyXstfohEv4zAQqC04Ow3Rg4X3mpcklOT8Z_q4wKZimYWxTwimVbFsijDSoYkhvdfCApT9OIahXw6tkO8yV3UPJHPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی تکذیب کرد: نه دیداری با گروسی داشتیم و نه برنامه‌ای برای بازرسی آژانس از تاسیسات هسته‌ای آسیب‌دیده ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129821" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129820">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oc9iZ8iyjBkm0FUW9iGn6SGzRKJgWpmHdgM3HYnpPONbcPP3LjNeGZzG1G5RVlOkXMHyhWJZqinqZKkSONVfqaHjOhSIBWm7cCZgzOD5YBsVjZp7uCj8koPfvk-Q1wVagN2R0N6TNGjbLJBjERlf968OTVDkNT4fB8p4TnVF3FXfzXu_kI9n1pys7UHe4UJOoCpoBho90cK0nBPpUU40jKUOZQZTq_Hb03j3TSEfMQuOcMZVxqX663sIKy2JTrDofK5rKfwa4l5OOcCxmIs-wvwZejJQWYb8puNXu6exutGf2cgO6TiMB_1t3oDuF5GFabiNo1Ss_ThIa1fJxUfvag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز:  روبیو با وظیفه سختی برای متقاعد کردن متحدان محتاط خلیج فارس در مورد بازگرداندن روابط با ایران روبرو است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129820" target="_blank">📅 11:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129819">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
سازمان ملل: برای نخستین بار از مارس هیچ حمله هوایی در لبنان ثبت نشد
🔴
استفان دوجاریک، سخنگوی سازمان ملل، اعلام کرد که روز یکشنبه نخستین روز از زمان آغاز درگیری‌ها در دوم مارس بود که نیروهای حافظ صلح سازمان ملل در جنوب لبنان هیچ پرتابه یا رهگیری هوایی ثبت نکردند. او افزود که این وضعیت تا صبح دوشنبه نیز ادامه داشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129819" target="_blank">📅 11:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129818">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-izk_HMjxdjxPqp9-SPuXm4012om9PmJD3Xxk4Bg8kXMid7JW6Kkifp9xNQD1pP0HZjFqF7w3gaj3AK_pq1hsI80kTMudEN-3bSRT88VLKhLTjqDyG1C5LOY4JBkhj_2Qbg98YJC9bDX5Nt0a-RmVEwGan49yQBMxYeXsKJOWB2gElvSgidhtXpI6eRUhAKyvpYRAny8zfFUs3w1aLe00yz6Q2Ye5mIPCbkqmhpkAB88GOv2Mb522a1FEyPmnjKxcAOTFtg0N7YoNGNK7jnKXFJP1GMYnVw6_LJvl8noF76TN2paOF-EW4eCDEx5HXV_Y4TYYwcE9SuQpRXUsoKdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سلیمی، نماینده تهران: با توجه به تغییر شرایط، آن دلیل ابتدایی که موجب می‌شد صحن تعطیل باشد، دیگر منتفی شده و ان‌شاءالله به زودی شاهد بازگشایی صحن خواهیم بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129818" target="_blank">📅 11:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129817">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkx4-OMn8rolsYRKfMdS6K1Tvy8pW2QHkvOFOK2y3Z3T3BGwDAzs_rJiE8fF9nD3SOZuckwoIH6npa09BK9EU4IyiZvLdF0X-44Pv2bUiOon9mUPYaBEEYsDdtg3QpFrUtG3hEFcR7LlwHu7kaaSVYCdQJanc5OTfRmJYaPotawYNCNk8W0m6MHjuzOioGQILAkjb9AH2W2_qWilk_A0ceE-aTKXskaROAcz8y05-GLaxv76hHjwp3dF50R8o1fFQk2rzWbjz3-ScKuPlr-n-13QfGez7ubYgd86f37F0o53kcvR_td__8jy0Xgu5AFqMtrPpGLXHsf33IOk6dsd9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: اونا مردمشون رو گشنه نگه داشتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/129817" target="_blank">📅 10:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129816">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وزیر دفاع پاکستان: حصول توافق میان ایران و آمریکا ممکن است به پایانِ حیات سیاسی نتانیاهو و حتی بازداشت او منجر شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/129816" target="_blank">📅 10:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129815">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
پزشکیان عازم پاکستان شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/129815" target="_blank">📅 10:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129814">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8dpi-JAfBtdfrLn4WnOL2yaLeKo3Ot9zBfO57ccHBkZLPONMltTrmfZfS7IIpOxicBkbOq_qyFeuLCCCrR0mAoVeXPuOE6KgKo1VJrtZilbzPeK0cdNowyCgmg1VkURvVjuNS5Nk9CNeEoI0MHdP3b3JrIWjtfmk8Dmh5x1mE60UdTWxXPSzCwJXUzckJpLuSXVSszDCzAxXP6d04AMvo7AShre9AScumXgRkgcxfDTsSY9XqHxkT6Ev2e1HKGtIjNtiLTaCs6-c1bBDqqH1uZhOhSVDs5d546BcgSiifeh8AYvcyAuTPAeKrgQINViB_U9SjjVPFAE1QEF6DBl2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زنگنه، نماینده مجلس:
یکشنبه آتی، صحن مجلس، کار خود را آغاز می کند/ احتمالا با موضوع بررسی روند اجرای تفاهم نامه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/129814" target="_blank">📅 10:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129813">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16290e355b.mp4?token=GbmoZt51WXKLpkI9ZOGoN8XcTrKYDbUz893A2G_nyCGKSU0RwVPATDSaIvcJplOE-5xmdGcwgvkV4pCKJWMBfMRZCyNrgJgXZ856eFFrQmnEKNGByJFcVoZ9czb8laS2eGyQ2N4Je7rfUbAQ_snvbik6OkaG1qUmZQhzvhQhvixPwCEUcgFVXc81dfRW_mgTetXJ50ksu_ciDtDNMatGQoC34tZK7RKSpIDxvWyupFBI50W1pVy8nLHrA2lL7RE3oIU00HNylrZ0IJaNy8TPxHiWdCkm9i2rNySqhHQlknZBx0IvXX6fbnE4P7Alf6pMVWqz1lqKwEpjlHNkAnmdgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16290e355b.mp4?token=GbmoZt51WXKLpkI9ZOGoN8XcTrKYDbUz893A2G_nyCGKSU0RwVPATDSaIvcJplOE-5xmdGcwgvkV4pCKJWMBfMRZCyNrgJgXZ856eFFrQmnEKNGByJFcVoZ9czb8laS2eGyQ2N4Je7rfUbAQ_snvbik6OkaG1qUmZQhzvhQhvixPwCEUcgFVXc81dfRW_mgTetXJ50ksu_ciDtDNMatGQoC34tZK7RKSpIDxvWyupFBI50W1pVy8nLHrA2lL7RE3oIU00HNylrZ0IJaNy8TPxHiWdCkm9i2rNySqhHQlknZBx0IvXX6fbnE4P7Alf6pMVWqz1lqKwEpjlHNkAnmdgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقوع یک آتش‌سوزی در شهر هیوستون ایالت تگزاس آمریکا موجب برخاستن ستون‌های عظیم دود بر فراز این شهر شد
🔴
تا این لحظه جزئیات دقیقی درباره دلیل آغاز آتش‌سوزی، میزان خسارات احتمالی یا تلفات انسانی منتشر نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/129813" target="_blank">📅 10:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129812">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ustYFDpKMyHLx3aTYH1orj2zMeB1Y9dCorb7IJe7JQHvcPgXXTS_rJN94ED_T2F8Qk7XpFNXBHketMPI8ab7WP_7Ihk0FXzkDZMpEjuyqvXmGiaBixhoYSAJE0ogg9pNEuIm73bm8xpESKuhjRPh-ScJAXDA8NL7Om2RhPm2Nn2Bvrd_Hdrl0GW5uHd7oZzwmj8f4ZUbgAA7P7yq80tL0ZWtrQ93tBJmKGg5xNqSLUXs7UYcCy7FHgBrvl-X0GkRnMpr-TUoyUPYk-_XxTQRaAxuab3rsTIBOpTT73ylRj_TCeh1PuFTniAUYoBjW_QGKEolXMR4HDATXyL_a8MuHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقامات بهداشتی کشور کنگو اعلام کردند با تشدید شیوع ویروس ابولا، شمار مرگ‌ومیر ناشی از این بیماری به 267 نفر افزایش یافته است.
🔴
تا کنون 1048 مورد ابتلای قطعی به این ویروس مرگبار در این کشور به ثبت رسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129812" target="_blank">📅 10:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129811">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
روانشناس اسرائیلی ، اوری گلر روانشناس مطرح جهان به کانال 14 اسرائیل: ایران از سلاح الکترو مغناطیسی با فرکانس پایین برای شستشوی مغزی و تحت تأثیر قرار دادن ترامپ برای پذیرش تفاهم‌ نامه استفاده میکند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/129811" target="_blank">📅 10:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129810">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
کاخ سفید : به هئیت مذاکره کننده اعتماد کنید
🔴
آنها به مذاکرات ادامه خواهند داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/129810" target="_blank">📅 10:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129809">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
داده‌های کشتیرانی: طی 24 ساعت گذشته، دست‌کم 20 کشتی از تنگه هرمز عبور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/129809" target="_blank">📅 09:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129808">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش :بر این اساس، امتحانات نهایی پایه یازدهم از ۲۰ تیر ۱۴۰۵ و پایه دوازدهم از ۲۱ تیر ۱۴۰۵ طبق برنامه اعلام‌شده برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/129808" target="_blank">📅 09:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129807">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
نتانیاهو و وزیر دفاع، کاتس :
ارتش قراره همین‌طور ادامه بده تهدیدها رو خنثی کنه و تو منطقه امنیتی جنوب لُبنان بمونه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/129807" target="_blank">📅 09:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129805">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
ترامپ: خودروسازان آمریکایی تولید سلاح را آغاز خواهند کرد
🔴
رئیس جمهور آمریکا در کاخ سفید به خبرنگاران گفت: «آنها برنامه‌هایی برای تغییر کاربری کارخانه‌ها دارند. ما قصد داریم سلاح‌هایی از جمله موشک‌های پاتریوت، موشک‌های تاماهاک و موارد دیگر تولید کنیم.»
🔴
طبق گزارش‌های متعدد رسانه‌ای، درگیری با ایران زرادخانه‌های ایالات متحده را به طور قابل توجهی تخلیه کرده و خطر جنگ‌های جدید را ایجاد کرده است.
🔴
در ماه آوریل، کانال‌های تلویزیونی ایالات متحده ادعا کردند که تنها در هفت هفته، ایالات متحده تقریبا نیمی از ذخایر موشک‌های پاتریوت و حدود ۳۰ درصد از موشک‌های تاماهاک خود را استفاده کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/129805" target="_blank">📅 09:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129804">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d480841643.mp4?token=FcyFrkKNHHjL7iYAZ-rYr5oNrOd2Q7YL2QB9Cn83sXJe8UKLaRhAqIzbRMCL9qu9XjrXLUNlRMn0MJkzOkYTvhA0sovYNTpvmUGUDYtM_M8KNsGuF5RVQPnMA5TE0yt9wQYv1Lb5MeznRrZ7ViwW4JKavsKQvYIzKyeRd9JeSytGZS5HJn7VFZnHqxbxvIamXqdzot8qnfR34qXaEwbnIoQnRzbd3Bz9tmwE5ErbSFU_FIlF5N0IbLsBl0Vx1Rf-Xm40tTYkDlz5CJyMJnhmaDyy2AaR6COPFGm04V3ZNcHohtRlfYhFMuWmxysTlW4G14FobBQ3157ASdMh5Q33OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d480841643.mp4?token=FcyFrkKNHHjL7iYAZ-rYr5oNrOd2Q7YL2QB9Cn83sXJe8UKLaRhAqIzbRMCL9qu9XjrXLUNlRMn0MJkzOkYTvhA0sovYNTpvmUGUDYtM_M8KNsGuF5RVQPnMA5TE0yt9wQYv1Lb5MeznRrZ7ViwW4JKavsKQvYIzKyeRd9JeSytGZS5HJn7VFZnHqxbxvIamXqdzot8qnfR34qXaEwbnIoQnRzbd3Bz9tmwE5ErbSFU_FIlF5N0IbLsBl0Vx1Rf-Xm40tTYkDlz5CJyMJnhmaDyy2AaR6COPFGm04V3ZNcHohtRlfYhFMuWmxysTlW4G14FobBQ3157ASdMh5Q33OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک روحانی: اسم بچه‌هاتون رو امیر نزارید، ریشه این اسم بهایی هست
🔴
امیرها همه آدمای مشکل دار و ناجوری هستن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/129804" target="_blank">📅 08:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129803">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7BCKjT9JL_NFrsVLWBcjaZrukvGVsjEWLQwdyMhNtH2yG5ml-C3J4dzQ8wKJLc9inZx87bUIw_PzDVxhVrQYC82HChJbZ5SXTbJFchLODAMrJpH0zbbZhUbWe5C19P2dFjXH2K97CSI8a3dD5OItVZHQVBsgEg03Fd-Mc7hRoaYaH2_TvEW8KOYblIDHUjiMiWdZUzsgOAgkhCIenqNiYiy1XeVg-vM3Es5P8f6_yParRwGU_IcV1z6mo0YN827VulrfQnatElqPY4TZNUZErAaq2W5EV6cXMPHr5013z10t5PchwO3qXT10v6PuuXayUBANexbVmmpCdCW0ATHqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غضنفروف نماینده مجلس: جمعی از نمایندگان یکشنبه به مجلس خواهند رفت؛ اگر در بسته بود همانجا تحصن می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/129803" target="_blank">📅 07:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129802">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vr-kWCyG76ifauT9JR_zI6y-injBriu-Y4LCK74kDntC88DSyaVfd98KKYCoT-lphHBe8PK5OcZdRhtVBgpCNLx1cqKruPhaOmZqoO5TIft3nNaBO1V6qEnyF7dHeUbaOWY9q9LXd7ts97MOg7sQjFe-UDoZJWejWt3O5MhqZCmjwXIo2ZhStdmXWckXUKTK3_OfL2DLSCqa_bs2VKmI12vV1fjaSTUMln0wc6zyaWzA6Y9QMdX4LtLQTaHWvs7pZrD-Un8ZnsGVngiSvBgfg6KiB1CElombExW3LYHfUH8II0cEAkcEUUaJdCwJbLNP8FPDOsE7oPK7BGEC0_5OlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: مفتی مفتی تنگه رو دادیم رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/129802" target="_blank">📅 07:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129801">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبارفوری مذاکره | مذاکرات ایران امریکا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1gXkgzY63HtkKC1paUhlYL4XztGA91zeYU5dPdF3MtTQ6bBBYwXDJK17RI1Ifz15DrZeAB15beA2OpmiWq6tKCScGM8_HeBhQWen2a8KppiRwDsL7xr4GR5ubX7Svk_BoTwYSYQQKyEWL9sakj6ri5e4uoTtQXtXxhExHapSqoW9DUHbAxfznqle5Py-nwM2DVEVrbY7y09jTozDec6wvDfFX4rYLq-oGNx915PJixrzQlrSMfMi2YBP3ihf-Z8r7V_zgpjHdgRa5UCiWc55Y9_jWgYVZghbmP1jVBZHJqavPPcUD_-SsKP2anEtFXJ8dL3c8ppvnoDwFjW2Qg44Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/129801" target="_blank">📅 01:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129800">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1Ba0stzGiquBIC0cuEwyirThEGDeb3Z92C_tuQlggU0v--3PL_HHBjA9Y5mvA-uJeD6aWZmO-LbBZTt6c8xDJMAyOUwHDAAW9IerZ-j_LpSORRiwiCJQfmgCoKFGJUH5VZulLIXQOFQVY6KnGbkTCI6MEGnWMU8e_dItuLTvixPdNShqBM4whQcOgU01qhC6M80QhMgvhk4WhYeVcKvmwakMMOAedt0MM-8m5UT_wliSm_7Jx8DrUi_tstR3BDl6AeCTS6a4gesM9TTqjyi6QiUL-LZsHZqlC_FYZZlGicx9XAhcfsfiOdQ0rfEaoBrHI5bpcv9PDVCQ3vnUGLLPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عماد الدین باقی: طبق بند 2 توافق ایران و آمریکا، از این به بعد شعار مرگ بر آمریکا یا سوزاندن پرچم این کشور و لگد کردنش تو مراسم‌ها و اجتماعات رسمی (مثل نماز جمعه) ممنوعه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/129800" target="_blank">📅 01:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129799">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وزیر خارجه عمان: به قانون بین‌المللی و تضمین عبور امن و بدون اخذ عوارض از تنگه هرمز  پایبندیم. به مذاکره‌کنندگان ایرانی بر تعهد خود به قانون بین‌المللی در ارتباط با تنگه هرمز، تاکید کردیم. مذاکرات سازنده‌ای با قالیباف و عراقچی درباره یادداشت تفاهم انجام دادیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/129799" target="_blank">📅 01:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129798">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W66FMdhNAdBqeWMP7Dg50N-6_OHVfjLn5Gr1fq7bHSCPybhIBSZErvjstvOVg_5eArxu58JsSN_nBI-SdpkFCz088XOahZShEx8wdIdpQlX03VXxxcaH877JwZRKw8z9zJAJlEQv_KWizucSvAbJ9AVqYJ0Sg3LfGJaDhEyIilTj1v9AstJ2msbWyattppd5rLKgAoOYupo4kpl_ySdN1BPNVLrBwNxvNhGSoNz9-MlaYjJlvOSsz9-zk75Rt33GoBMB8quVkrpq7xkYpxH_SQlDT6QVJ5FRG5Tzoayj0_R527OPzd42LwErmhgXqxJzy0FPCUkr_V0e8HYUfFR_zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چند روز دیگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/129798" target="_blank">📅 01:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129796">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
گویا علاوه بر سویا و گندم، قرار است سیب زمینی دشت مغان هم از آمریکا خریداری بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/129796" target="_blank">📅 00:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129794">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7mFR3sfBpfH4MA4FCmC3g0pw1-3w8mMAaoJaP0mTaIZKUvFZSTVsxYJEDbOmboySpt025tIqIPkKO-2_nb489GwqhDSb4rQm-ViP0AKAKzNFC698DAVKUtXnonsCfdxj0ZtNYJY9XVkrdR8KqKw9olGuuapn_KTP11eux5XoYiV6txk9ssNfxlbhA67TWntZ2v5CoALXE0-voXlTeXBZ11psDrV5z-7JFQcubdceygJdoHlgJZPB4nLvZTHZYfTEE99ytlJk3Ym_LSbsyKJZgDHAmuUQx4M4AY4fxYvJjGiKr4lNxEmDMXtO8xb6pev75T-kiKWtfvW7vUbxmmlUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PQ8H5bn1iBP-nOuAHXXcOQN2PI9IAb0Vnw8QxkNvNrdf22f68P8RyvEzZfwR2AY4i60SPML-4r5KDlUvtH8LpwhLejoauZmMVyqluCfWW3RSiX_-q62Aj4sEu0W0C4aejQ0FB55AHdwNsCJRGK6oecUhMvfDpzjN4175MATLvwGOYFnfwr_MzpTlQOfg0uhVF9hS0B783k0RAl8Fo3IYql65o9xApVrJwtWSTJdepytFjtSD05uBH0QAge2o32_6WmLxjSzg-FrSbl4bicRvGVzkUYa6zpmRsNgxGrZEH3oGbQq9DKtP0PRh55llyXkVMOC8lmPNcX4D6STv_ertbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایران صاحب پیرترین ترکیب تاریخ جام جهانی شد
!
تیم ملی ایران در دیدار مقابل بلژیک با میانگین سنی ۳۲.۵ سال، پیرترین ترکیب اصلی تاریخ جام‌های جهانی را به میدان فرستاد و رکوردی تاریخی را به نام خود ثبت کرد.
@AloSport</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/129794" target="_blank">📅 00:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129793">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
یکی نفت رو میگیره بجاش سنگ پا و سوزن نخ کن میده یکی هم پولا نمیده و بجاش سویا میده
🔴
دیس ایز ایسلامیک ریپابلیک آو ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/129793" target="_blank">📅 00:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129792">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11e0b59223.mp4?token=nkDd_Kt3LKzRy6rCyo_-xahLhqWlfMejpmmf8mqDZuzc5XY-IhDsQ-WjoG_GGgd1EOFQ65_1UrONugEMjCxqAs7ADyZiQL_37i2S0-GF_T7pItrYGuFRpX5pxSr2S6boc7_pFzbGqu68LodJAu8KK9QbUH02CAD9wk2_Xw5xpCV0w_O90LTAd8Nk910aaPnBDez4ueZXNEdswZP3UPAIOl8VtMShl5wD3-NdeSwXctyBmmAZcSxOFD9_KyqCjjCXTEc2Bew7c5lIuTOmbApP_H_HNG-JidMc_MlVlrZ7tyM6pRsE3sqYfLzIrD7OUZDJuYtbrRGdu1LPSdr5-Xt_CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11e0b59223.mp4?token=nkDd_Kt3LKzRy6rCyo_-xahLhqWlfMejpmmf8mqDZuzc5XY-IhDsQ-WjoG_GGgd1EOFQ65_1UrONugEMjCxqAs7ADyZiQL_37i2S0-GF_T7pItrYGuFRpX5pxSr2S6boc7_pFzbGqu68LodJAu8KK9QbUH02CAD9wk2_Xw5xpCV0w_O90LTAd8Nk910aaPnBDez4ueZXNEdswZP3UPAIOl8VtMShl5wD3-NdeSwXctyBmmAZcSxOFD9_KyqCjjCXTEc2Bew7c5lIuTOmbApP_H_HNG-JidMc_MlVlrZ7tyM6pRsE3sqYfLzIrD7OUZDJuYtbrRGdu1LPSdr5-Xt_CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف و تیم مذاکره‌کننده وقتی ۱۲میلیارد دلار رو میدن تا از آمریکایی‌ها سویا و گندم بخرن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/129792" target="_blank">📅 00:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129791">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommorteza</strong></div>
<div class="tg-text">داداش حساب کردم پشمات میریزه .نفری ۷۰ کیلو غلات میرسه بهمون</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/129791" target="_blank">📅 00:29 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
