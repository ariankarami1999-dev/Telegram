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
<img src="https://cdn1.telesco.pe/file/Hz4oJlR8e3gmp7oYoJdjv-6DbveYqoewpENbCoNg4hevBWFrllOMR9NfVFJEC6eLPztRyTsrPLurr7cmHADis55CPSOgSjkrKCX4OlqzBjCMA_YnQVBq6w4mu0mA6WlgAdIVLY1kdSdDiBY2u_Xaj1E_knoCMPoiJMICsMisP-QnZHYn_eS6phbKMITtXckMYKYIceSWTiE1ACrIFBni3FxtNePDY-pSmWd59XUcjCPGXBmOFE7d3Oo52ymbXAsGQjZle7-UZW5FMLor_HAGVLKVVnqwEVC1RH7rEH-Hs3BYKmaAketkBFYz7nL9rvOmGh8Y9FAsKyDVIH4HKiyN5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 161K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 19:58:23</div>
<hr>

<div class="tg-post" id="msg-3956">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کافیه یه آیپی تمیز بذارید توی بخش Advanced, ip fronting
زیر ۲ ثانیه کانکت میشه</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/MatinSenPaii/3956" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3955">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🌎
نسخه جدید WhiteDNS VPN V0.0.4
⛏
در این نسخه • ظاهر اپلیکیشن تغییر کرده  • امکان اضافه کردن آی پی تمیز خودتون اضافه شده تا اگر اسکن میکنید با آی پی های خودتون به کانفیگ ها وصل بشید.  • پرچم کشوری که بهش وصل شدیدرو بهتون نشون میده.  • با کمک یکی از بچه های…</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/MatinSenPaii/3955" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3950">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3950" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/MatinSenPaii/3950" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3949">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slNx6JgRZpHEAKei4DNkSNhpiAC1j4FEymFfJrBgyAf0DYI83MbEZBAnN-NoLpZFMR1CGY0xERG9QgZc2TQNr1k92o8VgolTX_3cj_YJXMz7ijoWunGBCJtaGvCVQGrzMxMqN5R0OkCHDAuaJUNLxEZxYgsr3ZpJnpjDfCmlIQPEg7MJqZ7il7GbzdD7L6XRjgOuwRmMYHFovjIGFN8Kem79gmVlbWNA9g8VulMldhOYs-Tl0atsgdmwLp9RG18oDwRsiRTKNDO5vtwE5qxlkC0qUu6veDcz-mufkm91jnNyywMuPMPRw8bxyB3Vn3B7E9_jE6_Qu3RkuDAvmoiyEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
نسخه جدید WhiteDNS VPN V0.0.4
⛏
در این نسخه
• ظاهر اپلیکیشن تغییر کرده
• امکان اضافه کردن آی پی تمیز خودتون اضافه شده تا اگر اسکن میکنید با آی پی های خودتون به کانفیگ ها وصل بشید.
• پرچم کشوری که بهش وصل شدیدرو بهتون نشون میده.
• با کمک یکی از بچه های گروه، یکسری از مشکلات امنیتی اپلیکین رفع شده.
💬
اگر براتون وصل نمیشه، فقط و فقط مشکل از شبکه شما هستش. آی پی تمیز پیدا کنید و داخل فیلد IP Fronting قرار بدید و براتون کار میوفته.
@WhiteDNS</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/MatinSenPaii/3949" target="_blank">📅 18:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3948">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">34.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3948" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/3948" target="_blank">📅 14:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3947">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K1UBVF3EXg_asss840SRhkNvwmzALJwezVCqtHaLtQl9_TySDpbjMhwOHXo02isYOgrhWYJwMhp-rTSyAi6boKDcLhRnzXFBA6VfnHkQOAMFBST8AGZUQWrdPXApBIB4A_CH8efAHDirotlYxApEL3rLNP1qefvl1pCbkCprdS2Lc5b27imvNPM_qnnLoT6kjCdRdeQUad8Rda1NYuiLfEgIQSHgKJxfBKWduLaIWSbhgbIlTm0bLyoo7I0PP7pwL9-1w3yZqDeW2v9XLVicmUZpVDRHOwDwIm1206JmJe8yfzzfFUiZqv-fZzebOJZwud_hrOSN2uCE78xPqtp6lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از contributerهای پروژه‌ی senpaiscanner، دوست عزیزمون hidden-node، نسخه‌ی اندروید اسکنر رو توسعه دادن. طرز کارکردش دقیقا شبیه به اسکنر دسکتاپه. نصب کنید و یه تست بکنید
👇</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/3947" target="_blank">📅 14:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3946">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">✍️
دوستان برای جلوگیری از هرگونه سردرگمی، ما در حال حاضر سه اپلیکیشن مختلف داریم:
🛡
۱. WhiteDNS Application
این اپلیکیشن بر پایه‌ی MasterDNS ساخته شده و مخصوص زمان‌هایی است که فیلترینگ و اختلالات اینترنت خیلی شدید می‌شود.
در شرایط عادی فعلاً کاربرد خاصی برای استفاده روزمره ندارد.
🛡
۲. WhiteDNS VPN
این یک اپلیکیشن ساده‌ی VPN برای کاربران اندروید است.
اگر فقط می‌خواهید راحت وصل شوید، این گزینه برای شماست.
🛡
۳. WhiteDNS BPB
این اپلیکیشن برای ساخت و راه‌اندازی BPB روی گوشی اندروید است.
یعنی بیشتر برای کسانی است که می‌خواهند خودشان یک پنل BPB بسازند و مدیریت کنند.
🛡
۴. WhiteDNS Installer Bot
آیدی بات:
@WhiteDNS_installer_bot
در این بات می‌توانید کارهای زیر را انجام دهید:
• نصب MasterDNS Server
• دریافت لیست IPهای سفید Cloudflare
• دریافت کانفیگ رایگان VLESS
• تبدیل کانفیگ‌های خودتان به کانفیگ‌هایی که پشت IPهای سفید Cloudflare قرار می‌گیرند
🛡
۵. WhiteDNS Installer Wizard
لینک گیت‌هاب:
https://github.com/iampedii/WhiteDNS-Wizard
این ابزار برای کانفیگ خودکار سرور شخصی شما استفاده می‌شود.
با استفاده از آن می‌توانید سرور خودتان را همراه با پنل شخصی 3X-UI راه‌اندازی و تنظیم کنید.
❤️
یک نکته مهم:
اینکه اسم برند ما WhiteDNS است، به این معنی نیست که همه‌ی سرویس‌ها و اپلیکیشن‌هایی که می‌سازیم حتماً بر پایه DNS هستند.
ما از اسم WhiteDNS به عنوان نام برند استفاده می‌کنیم، اما راهکارهایی که ارائه می‌دهیم می‌توانند VPN، BPB، MasterDNS یا تکنولوژی‌های دیگر باشند.
@WhiteDNS
🌎</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/MatinSenPaii/3946" target="_blank">📅 12:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3944">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i7B5u3k5yLazl6UHWvufDblX7FPmxLeXYMbrfLWOQgv4s6ZOZF7wO0gG-PgDVto8ngrpqUtz6fsYglZ0Lkf0IhWznewqArxsuk6g12p3BJrR0vFTnyKCZOhpmq9ut6GorLoRHJx-WiQBgrZyGvx0slDfIXo-VNUnfAljdSmmY27JY2YW_oG1R1K_LikwK2cIqUQDFRrvDDpV9a6WqtBeiWwL-TlYbdZn-CXc8h7Bo5LGl9DSHJ6HRlY-BNwzzyVYWm9tpEiF7FO_Uy-w8cquOQUfsQKF980d-7I5BlIb2o9J2nmWev-98a_TNzB1qfTZPRn2hL3JV9NIzDgUognA_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kzsyoRBbNnweKvyD-ibxV3RfbIHPWiAdZiJoqpANnr7yJC_rcGnWzD-WmEL2XwioU40JV3YgNMRzBbTi9QSHmtVHA4Ak2wgiF_rpg0WW3uGEZKGO_pdbxlA8py61RLyhwQnHsnExKr8DcOmo_qXXtPdEPQPT_XTvqq1ZVsm5nvMKxVeXy_O3xeIftqkIs3ZNqKUkM4gOxHHYHNV43ejFL6_5rtoWKmr62E1L-lZMtiI5nVORtRwI1LDaj9QAy95yJPIyF3ionnWdV20_xfGrcg9DMq4ast19sMppws6O2txaasoKmFGyYSoQlrsImDWPn-E_uVnVd8qtrYZAEQ91yA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی از بچه‌ها اینو واسم فرستاد و گفت گویا V2box، به صورت آزمایشی SNI-Spoof آورده. یه تست بکنید ببینم داستان چیه:)</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/3944" target="_blank">📅 00:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3943">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">دوستان عزیز
❤️
در چند روز گذشته متوجه شدیم که بعضی افراد و کانال‌ها، به جای همکاری و ساختن، مسیر تخریب و سوءاستفاده را انتخاب کرده‌اند.
این افراد که ظاهراً در فضای اینترنت آزاد و کانال‌های مشابه فعالیت می‌کنند، برای جذب مخاطب بیشتر حاضرند هر کاری انجام دهند؛ حتی اگر نتیجه‌ی کارشان آسیب‌زدن به پروژه‌هایی باشد که با زحمت و هدف کمک به کاربران ساخته شده‌اند.
چند روز پیش اپلیکیشن WhiteDNS VPN را معرفی کردیم؛ اپلیکیشنی که هدفش این است کاربران بدون نیاز به تنظیمات پیچیده، فقط با زدن یک دکمه به بهترین کانفیگ‌های آماده و تست‌شده‌ی ما وصل شوند.
اما متأسفانه برخی کانال‌ها شروع کرده‌اند به استخراج کانفیگ‌های داخل اپلیکیشن و انتشار آن‌ها خارج از برنامه.
دوست عزیز، اگر مسئله فقط بستن مسیر دسترسی شما بود، ما ده‌ها راه برای رمزنگاری، تغییر مدل درخواست‌ها و محدود کردن این رفتارها بلد بودیم. اما شرایط اینترنت آزاد و محدودیت‌هایی که کاربران با آن درگیرند باعث شده ما تا حد ممکن ساده، باز و قابل استفاده طراحی کنیم.
مشکل اینجاست که همین رفتارهای مخرب در گذشته به پروژه‌های خوب و ارزشمندی مثل Slipnet ضربه زد. وقتی هر ابزار مفیدی به جای حمایت، هدف استخراج، کپی و سوءاستفاده قرار بگیرد، در نهایت انگیزه و امکان ادامه دادن از بین می‌رود.
واقعاً هدف چیست؟ آن کانفیگی که با زحمت استخراج می‌کنید، همان چیزی است که بخش زیادی از آن در لینک‌های ساب ما هم وجود دارد. چیزی که روزانه هزاران نفر را متصل نگه می‌دارد فقط یک لیست کانفیگ نیست؛ پشت آن اسکنرها، تست سرعت، بررسی مداوم، فیلتر کردن کانفیگ‌های خراب و یک سیستم کامل قرار دارد.
ما این ابزارها را در مدت کوتاهی، با انرژی و فشار زیاد ساختیم تا به کاربران کمک کنیم. لطفاً به جای تخریب، کپی‌برداری و گرفتن انگیزه‌ی تیم، سازنده باشید.
ما از نقد، همکاری و حتی پیشنهادهای جدی استقبال می‌کنیم؛ اما سوءاستفاده از ابزارهایی که برای کمک عمومی ساخته شده‌اند، نه کمکی به اینترنت آزاد می‌کند و نه به کاربران.
اجازه بدهید این مسیر ادامه پیدا کند.
✍️
@WhiteDNS</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/3943" target="_blank">📅 23:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3942">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">این پست سگاروی عزیز رو بخونید، و اگر دوست داشتید همکاری کنید:
https://t.me/AiSegaro/120</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/3942" target="_blank">📅 18:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3941">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-text">تیم داشته باشم، دوست دارم از خودِ شما کمک بگیرم. اگر دانشجو یا دانش‌آموز هستید و مهارت ترجمه دارید، این می‌تواند یک
کار نیمه‌وقت منعطف
برای شما باشد تا در ازای کمک به ترجمه و ادیت، درآمد کسب کنید. آیا این مدل همکاری برایتان جذاب است؟
هدف من این است:
سریع‌تر به محتوای آموزشی مورد نظرتان برسید.
هزینه‌ها برای هر نفر ناچیز باشد (پول یک قهوه!).
بالاترین کیفیتِ ممکن (ترجمه انسانی) را تحویل بگیرید.
یک زنجیره همکاری برای دوستانی که دنبال کار نیمه‌وقت هستند ایجاد کنیم.
هر پیشنهادی در مورد نحوه قیمت‌گذاری، فرمت‌ها و اجرای بهتر دارید، در کامنت‌ها بنویسید.
من تک‌تک نظرات شما را می‌خوانم تا بهترین مدل را برای شروع استارت بزنیم.
این فرصتی است که با هم یک کتابخانه آموزشیِ قدرتمند بسازیم!</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/3941" target="_blank">📅 18:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3940">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1e7OiFXHrdJiBMhljyFZJ6KvEiozY1ed-06SNMQbb6LR-YroYaR5bHepeeV-sPvBsP1AV-av_c7Q7JslOc6B8NUZ95Q4M84fIq_DQzMQsK8sqs8kwJD5ZJo0M8G9rZAH7QQnQitk-dDnw7tWIPiLRwvZ8gFqToIvsrszKPBmD9JKWbRob1hlbG9UkEtnQogWjF-LXDphGvh8VulAYq2c6PC8iBM71wEVN_fAf9tteBtuxvZpMYX5KWCB86E6Ixzw92oTKxtk7PdV91E7pRL8xbkMemwzbKgc80ZVqNXDG9Sin6YEv4k9IEvR8Srk7OWJt0wE9S4KQdu1S2AQ_wIfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به همگی، یک پیشنهاد ویژه برای دسترسی بهتر به محتوای آموزشی!
همان‌طور که می‌دانید، درخواست برای ترجمه و زیرنویس کردن ویدیوهای یوتیوب، یودمی و کورسرا زیاد است. از آنجایی که کیفیت و دقت برای من خط قرمز است، فرآیند آماده‌سازی ویدیوها (ساخت زیرنویس، ترجمه دقیق و ادیت) بسیار زمان‌بر است.
برای حل این چالش، قصد دارم یک
«کانال مستقل»
برای مدیریت درخواست‌های شما راه‌اندازی کنم تا با مدل
«مشارکت جمعی» (Crowdfunding)
، ویدیوها را به صورت عمومی و با کیفیت بالا آماده کنیم. در این مدل، به جای اینکه یک نفر هزینه کامل را بدهد، با مشارکت چند نفر، ویدیو برای همه آزاد می‌شود.
اما قبل از شروع، می‌خواهم «شما» تصمیم‌گیرنده باشید.
برای اینکه این سیستم عادلانه و دقیق باشد، دوست دارم در مورد جزئیات زیر در کامنت‌ها با هم صحبت کنیم:
مدل هزینه‌کرد:
به نظرتان چه مبلغی برای «مشارکت جمعی» منطقی است؟ (پیشنهاد شما برای ویدیوهای زیر یک ساعت و بالای یک ساعت چیست؟)
فرمت خروجی:
ترجیح می‌دهید فایل زیرنویس (SRT) را جداگانه دریافت کنید یا ویدیویِ چسبیده شده (Hardsub) که آماده پخش است؟
یک فرصت برای شما:
اگر تعداد درخواست‌ها زیاد شود و نیاز به</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/3940" target="_blank">📅 18:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3939">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P0Wuefc7QwaNEheIsFKe8PCfv5KeL4JE5L0O3J3GiyJKwu9qpLM9J2yKwfpwgQ0eIObv50SKpHGKK_ZMFpRLnY3EQprg__vYxEXIzRXgbRQxNNeKm2sPnyyULsBB7sY4xL3Y3_rxLDrJ5E8roeXcJhO4zWpGFJ_AX5ihE5j7-kaj5upGljkpXzIe56u97J6tm4KGmQYKiWTsSiWKOfnqJKGCCb8kZOT1IVu4OZXuDZlaoxQNmLUpDRLEwH9bxANZePAQ4bAGPMviwUPydSgKZsr_soLu4bvHz50PHTiHxmxqT6flznn2acv9EPJNUxyixnaFukoerTxOd-c_hWCEvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی از دوستان این مشکل رو داشتن که تلگرام واسشون باز می‌شد، هیچی دیگه باز نمی‌شد. یا یوتوب و ... باز نمی‌شد   مشکل احتمالا از کلاینتتونه و dns اش. باید تشریف ببرید توی تنظیمات v2rayng و Domestic DNSرو از چیزی که هست، به 9.9.9.9 و یا 9.9.9.12 تغییر بدید. همینطور…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/3939" target="_blank">📅 17:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3938">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ku0-M5nsfsHfL3ldENvqIN9oYwjgSpFxqYb3UzAjk8CAqDA1c4D0-6Q839CUIReC_MHWrihzu-lL9FP407AGsj6Y3xaCAozC5u2NyiJwCBw2awDfCVdjYKPuju7oL4SlE2IWaX-IziTgO4Yda9k2cXimyIaEsuW2NC58y4upKu0C8v5ol1fo8mDG7Atq35dcaeEg8kGMznO60ss4HlWlhkOdjXunkUcSzMul5RureDnVOPwKaID380eAw_iboMj6ON1A96Bf-rSVLVeyo7MTqz__IGvLJBKxE7SljjEVD9HO9tQD6bl-z2ZJBOToqD92FlK4hWqaC-8NFVuEIQlIkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
بدون دانش برنامه‌نویسی و کاملا رایگان، اپلیکیشن اندروید بساز! (فعلا اپلیکیشن ساده
😁
)
⚡️
لینک‌های استفاده شده توی ویدئو:
1- خود AiStudio گوگل:
https://aistudio.google.com
2- پرامپت ساز ریک:
https://chatgpt.com/g/g-6a319e2a22648191836468df375a3763-prmpt-sz-ndrwyd
⭐️
توی این ویدئو:
1- بهتون نشون میدم که چطوری می‌تونید از یه پرامپت ساده، یه اپلیکیشن ساده با تم دلخواه تحویل بگیرید
📲
2- توی مرورگر، Emulator اندروید بالا میاریم و با اپلیکیشنمون کار می‌کنیم
🏆
3- و در نهایت، اپلیکیشن رو مستقیم روی گوشیمون نصب می‌کنیم!
📱
🤎
اسپانسر ویدئو:
خانه EB، خیریه حمایت از کودکان مبتلا به ای‌بی و بیماران پروانه‌ای:
https://ebhome.ngo
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگانه و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/3938" target="_blank">📅 11:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3937">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ویدئوش آخرای ادیتشه
🔋
می‌ذارم تا ظهر</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/3937" target="_blank">📅 10:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3934">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J6ufsDENeHaD10C-jgmNCKgzGvaLSYCVGASmIpVJVZEFjno79Rnf8ozzhivmYDQYVeGNjXZAVVZn3EpR8QD8eXJe3GRkRclrsEv4E1-2nzGvIEAsaK_Hac4l-bjNqh1ioIriflJ8xkiPjuaUi4o2r5n1Zh3wAwzj2oNC1V9n3EQW28PmeYBmd3oOlfjcKmhoyy1VbsJdvcub-2m-o5AKAc0g8rgryZLqjPy7GHSAThNRVErB0cdMyaai6DUBycaTsWL1VrqcvrtfpRDkynzD571qGOmYOBL72nk-Ywt-18ygaenSfAyPpYiqEcAhsVXUn_RL_oLhCAd3zv3saOkfKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l8xdAhn-uUJXG2e4ggwVADNMETcTjX-c4BkKu71f5vk7z6YV7VNOvWkrrvGD3TsWbksXHF03S3KTPki_Z7wSHHa59Z1aoWBV9V6YTYo7ogfNqYhM4Oj6v6a0wlzcnCyLUxt4nbiiZ335_eqS0yBAnPkH5lajaOY2qeHvYJXtwwP-ITJJ3ylPjhQzmhciiRIIpTA6pk-2TM5ZixpXGDbz63v7UuFTE3_BnoZ1FMiBUPh5Anwaxyh70RFNMztETZZXXo67TCN-nx0tibvfAoW17njay8f3h7yTnV3RPXF9_q0-cYpPLDGTG2-BUrjNnFNzAomA4G6cun5Db1UZNcz2Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a_CkLxjN8Jmk_fZbi7xXy4yCptFXMBHDBkMpiKPaCkDNbe4eqnxZtFkZRtt8gqnC1bJb9R8NkXVoI87UhYDphWywEDNh3nvL0uZWR_Vnz3RJC7Q9rY2OBfK212BccocRFmxqqmjbCyYzmg7qa4xPLYp1b4xy1RthGR-DQGaZCketVCT_LVofgXj_9D2S8YEGt_Rt-bpWjcOvcp-ZGYTiZv3IKSFVkuGiHzM5TAr8fVx2AEJfM6qJH0o5D6Agn1PK3RsGZ_3umpuF34hXc_1yFnxYSIX-G8MJlX7jDqmW7RfZdddfcc16V-W3UsI_wldOkEEG6ktVXSNOsKagYcWP1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه اپلیکیشن مسخره‌ی اندروید با AI گوگل نوشتم مجانی، توی بیست دقیقه
ویدئوش رو ضبط کردم که به شما هم یاد بدم. اصلا چیز خفنی نیست اما خب بامزست</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/3934" target="_blank">📅 23:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3933">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">میگن Cursor یه چیزی ساخته که SpaceX اومده 60 میلیارد دلار خریدتش
نمی‌دونم چقدر حقیقت داره این حرف اما سرمایه‌گذاری خوبی انجام داده. به زودی CLI کدنویسی grok رو شاهد باشیم احتمالا</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/3933" target="_blank">📅 21:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3932">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">آموزش کوتاه استفاده از :
WhiteDns BPB  1.1.0
📱
📡</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/3932" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3931">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ورژن 0.0.3 خیلی بهتر شده رفقا. حدودا بعد از 20 الی 30 ثانیه وصل میشه روی همه‌ی اپراتورها و سرعتش هم عالیه
منتها می‌تونید از خود Wizard استفاده کنید و بسازید برای خودتون</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/3931" target="_blank">📅 18:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3926">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.3-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3926" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/3926" target="_blank">📅 18:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3925">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/3925" target="_blank">📅 17:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3922">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iT0nqFHwKtn3yZWDfTpzJ8VQtoGvC7RY7_daetaNL0bNnbc_L4jKR6_GO4rlwCfcbpY73dc_MN-R0nySrsu3IxyejkhZJ8XUXrfTk6r3QNNOMXIBViWkJvgOhgP5Bf5xE9kMgQ3x0QBxNhMfqFX4DB3C2UQ8hiT21BJMRK5wXCrJ8F_lrIN6Jqnb1vWiIj6nihKCWAfR-L9iIUln27rzhN2hXHatAidrNOCxSLnJ0KsznwWrq9e2XsDBFSts6AHA3fmfeFFzJUKnSkXs_jB0o5D5hJyYZvo0Q0DVWts6o-PcnrL9a0YIpmtAfCJYsv60PWLAlVbLmQ6HxzLsOwmaew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rlUudQXWEJcGeBsGXOlU9F7hpKcP-XN7denJ7PfaOf4hYyfoqgkLeyvqxKmWfCczbPyndlrQUT_Nav1diNnxhDB1cr9X2vyJHFq1CGgcgaWddAZAbDEvM9nVzIFKtPNLGO-Wk3FMUQqicoRHTVsbqWhzUeMDrpqP9HjjsTWMfPOiKg_UAuGRYFB4EnSmA906_26SngPAoCMa7GkrTHdyDUfZZN_MJy33VY57MmXwFwwpX14HSrRUdraF5rX78bo3fydxJh45UX3OJQY3sOqgtoharpXpeo7MBzPzlAg8EZTcno2z2Rm7O3mYBg81CcXV2QK01uV1I85ONaBZTepZvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PR6MKfNBpo3GBAXlH8JwsMvIApdHiiSWHrdblLfJ-9qh2ElFQuGBHWfVGZIJ7OE9pYegzxDgeDhOBNICicmAO66DbcCceljfu2o-G6l_BaYh7Jxv-B48fOQmJmLjXTykzyhtpHKfpKrce-vZ3etIdy9C4EoLUsXMB9S6EFhSZkUhkLVHRop_TxQreVi_pH6v8nqLADR1SieTAJQyrKHk_IiOnORbpkB5O1cV5QgXXqhftrE92085mHmQbxmHiftCTKm6oh3NXwZYwDBkhDmYnXPOnp8l6_K5Q62-ut6z4nchG5ifeYC-OaeiBHl24D5i5Zxi2aqakyguFfQ3SGw6bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بالاخره قابلیت ضبط صفحه نمایش به همراه دوربین سلفی، به اندروید 17 اضافه شد و دیگه نیازی نیست این کارو با نرم‌افزارهای مجزا یا تیک‌تاک و... انجام بدیم. کلی قابلیت باحال هم برای گوشی‌های تاشو اضافه شده؛ از جمله foldable gaming(که توی تصویر دوم می‌بینید) و ارتقای مولتی تسکینگ
اطلاعات کامل تغییرات:
https://blog.google/products-and-platforms/platforms/android/android-17-features/</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/3922" target="_blank">📅 15:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3921">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">برق داره دوباره نوسان میکنه
اگه سیستم داشتم به جای لپ تاپ، از صبح تا الان 15 بار خاموش شده بود
فکر کنم باز می‌خوان قطع کنن اه</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/3921" target="_blank">📅 15:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3920">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">😂
😂
😂</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/3920" target="_blank">📅 14:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3919">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ugj-PuYQJ0UA3SQQsFR5Cg08Y2h3pWCx1KiN5FLgOo5-wqRNhYJQwr1Y6mz86sJ1eRw1sHLgI0RFpRNmtVaGLr5JDHqBc0rASUVCV8zy-f3fYQT6qqDRItb24S1kNAi4uXb-CcvUo8qbVdFJebokFsB1wg93bAsRBC9rB4jvZIh6J6vJN7w4w8ktTcY4X0Olm4ryiqecZ9TPpvnQSEQUtoO0WrNlsDIsE1EFMx7thzzoPinYKssDjMnpTf8Udp5lTkzCHlCDii1atpfH2DlF9ZLL1NGFC9tk6Py1je5JOgJxdBLSM0vDWIieNfaO0NXR38ISKpBkqeQ9AOBjMgT8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭
😭</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/3919" target="_blank">📅 14:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3918">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fumJ4RqGTeurTuZpQrOxjknN7cRY8XQX8kRcuEzdnAHxlZKilK_HfmKLKkV_CiVXoPtT6OdUz42FtNS1ORwWn_NcF2fQhbMEgrmMvrdYh8YPEqUyIpA8LS5NkuQO-c4aVBMpmGHf4T4C1U8EKvSmzRmZQhyf2J50_BGRyEPQf1JezIyQs7-Odly2i4nA3f_zmf6J-YIVNS6DESxPv0LKgy5fX3cnJXc3lbrQintUqlwLthMpzUfpJ4jDlhmdWCUYiSBOpfUdiIlRxIKknu3pbzK01VTb5sJ3-ilZEb5DwWQ08OAK5I1t9nwz6vqnctLqtnoEdulxQtE9UsUZiwz_YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیدات کردم مهدی جان
🥳</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/3918" target="_blank">📅 14:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3917">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QRRfPu5GL2A1qoPddETTJ6hg6vQWBeB9OKPuXKzOuvVwrgrKG_zw0NcRScsKMrrdGIw4yXXTtyYfuH4Fr12A0EppFUpXaohqGOjygJBPe5-Sb7yyZBgassWx7nQ7Yb0BU4c32KvsvVqdYZ7B2D6qXTNOebGprBZorjbwV-d1j_2rp0HR3EOfMAlCXy9BXrTTvjeH_dXJwvG4irxuPjetkJyxkycVZ3lUeC5Gw3YQmspUP8DKUsxAqZ2NdoQc983PXu6RzCJemtTz6NhjKKLPCLF2vKu2q6qzueO30yDGVGT4hZkwdpwoF0Wzs58fL9McsV-XIOZtW863ota9yLlwEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندتا از بچه‌ها تفریحشون اینه برن وارد پنلی که من توی هر ویدئو میسازم بشن و پسووردش رو عوض کنن و برای خودشون لینک ساب بسازن استفاده کنن
😂</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/3917" target="_blank">📅 13:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3916">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/3916" target="_blank">📅 12:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3915">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XDdEIYy2H0zhtXGiwdP2CTEFfdvZO1_uKHYPk7RBNKvdPg3gp_oiqPvOEmuSY2uCzr00gOYgQoDHcOy9tEBA1PNgrRr5uBa7REZPaRm2tOI5KExT0jmXzfVdruKSvMQ2SRPor-i0TsaGDA0yNJAHErc3Bfy3CFTSbvrGzV9E5vFybYJcjVvWCwkagKvhNABwgcx_t1GZSdqUMMvNuX_DiNl76-vBFyFH955YNfMLxCm2NGtZS9w1Sej9ZUcPCLKrZ-c1Or_9wTiHaLVXumglkrEnZamc-pEiCGUbtFuMVkWM5TW1EfqB-0G2RIIVeHsI9LV_B7CkKHhNAFO9sFZZoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/MatinSenPaii/3915" target="_blank">📅 05:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3913">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/3913" target="_blank">📅 03:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3912">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">من که عددی نیستم والا نمیدونم وحید آنلاین و اینا چطوری هندل میکنن که آیدی خودشونم گذاشتن
😫</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/3912" target="_blank">📅 01:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3911">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/MatinSenPaii/3911" target="_blank">📅 00:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3910">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3910" target="_blank">📅 00:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3909">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود رفقا من داخل این پست میخوام توضیح بدم این بکاپ ها و این ip به چه درد میخوره؟
ببینید قبلا یعنی تا چند روز پیش شما تو ایرانسل اسکن میزدید واسه ip اینا ۱۰۰ تا میداد برای مثال ولی الان هر  چی میزنید ۵ تا به زور بهتون میده و ip اصلی که
188.114.97.6
میشد که ملت روش وصل بودن رو بستن
❗️
یعنی ip ها کلا رفت تو دیوار کاملا خاکستری شد
اینجا (patterniha) بهش اشاره کرد:
https://t.me/patt_channel_x/68
بعد حالا همه ip ها واسه همه جواب نمیده باید ببرید پشت gpt با یه سری ip محدود برای sni spoof استفاده کنید.
جدا از اون میتونید تست کنید این لیست ip ها رو که واسه شما وایت باشن و مستقیم بتونید داخل پنل های bpb و نهان و... استفاده کنید
🫰
ip:
103.160.204.34
185.193.30.94
45.8.211.57
199.181.197.1
159.112.235.52
170.114.45.239
104.17.21.111
104.24.200.94
188.114.97.6
آموزش ساخت پنل bpb
آموزش sni spoof
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/3909" target="_blank">📅 00:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3908">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X1pzikcrusefI_2uw19ogaCDDZFZmSbbf6_mStfNGEJXGK2l6qrUK-5vig-7O0RdA_biiUEtq1hY_aLF15XrQFq9fewj_gaNd75Okx9oSwDQXYMJ4AofGjzy1ZFQR65opCX7jPDXq4MGnAzzmgLixsYnNfUTqD14ppCu1siN2Tq10tqJl1HNdqF5iVUinEc1hd-3z28xFZAaaqGK08cBB5ryT4LxL8qnE5-LHrzxJGGcayiXtdpeshA0QeuB8d5g6s8Y7E-Awci-SdWhr04KByUCtzys3WTF3rO2dwfSdH1hAXtm2tm3Lc7fb4RgDQz8N_iIUKEK3C90DvFyZMTDxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/MatinSenPaii/3908" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3907">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">متشکرم از بچه‌هایی که دونیت می‌کنن. چه کسایی که استارز می‌زنید، چه کسایی که به ولت‌ها دونیت می‌کنید، همه باارزشه.
من دسترسیم به ولتم قطع شده بود و مجددا وصل شد الان، دیدم دوتا از دوستان 3 و 20 دلار بیت‌کوین دونیت کرده بودن. ممنونم ازتون
❤️</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/MatinSenPaii/3907" target="_blank">📅 20:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3906">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/MatinSenPaii/3906" target="_blank">📅 19:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3905">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر:
https://dash.cloudflare.com/
لینک پروژه‌ی نهان:
https://github.com/itsyebekhe/nahan
لینک اسکنر:
https://github.com/MatinSenPai/SenPaiScanner
لینک ربات ProxyIP یـ‌بـ‌خـ:
t.me/nahanproxyipbot
لینک ویدئوی اندروید:
https://youtu.be/2otJfXgNWCM
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش ساخت پنل نهان
2- اتصال به ربات تلگرام و api کلودفلر
3- ساخت کاربر و مدیریتشون
4- رفع مشکل وارد نشدن ساب در  V2rayNG و ارور 1031 و 1101
5- اسکن آیپی تمیز با اسکنر SenPaiScanner
6- پیدا کردن و تنظیم ProxyIP بر اساس کشور یا بر اساس سرعت اتصال(توی ویدئو نشون دادم چقدر سرعتم بالا رفت برای دانلود)
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره
با تشکر از
YeBeKHe
عزیز
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
(نسخه باکیفیت‌تر)
💰
دونیت</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/MatinSenPaii/3905" target="_blank">📅 19:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3904">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">داریم تستش می‌کنیم این رو، و خارق‌العادست. دم ویسپر و پدی و بچه‌ها گرم واقعا توی ۱ دقیقه پنل BPB ساخته شد واسم و الان دارم پیام میدم باهاش</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/3904" target="_blank">📅 19:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3903">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-BPB-v1.1.0.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3903" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">معرفی نسخه اولیه WhiteDNS BPB
نسخه اولیه اپلیکیشن WhiteDNS BPB منتشر شد.
این برنامه برای کسانی ساخته شده که می‌خواهند پنل BPB خودشان را راحت‌تر روی Cloudflare راه‌اندازی و مدیریت کنند، بدون اینکه لازم باشد همه مراحل را دستی و پیچیده انجام بدهند.
با این اپ می‌توانید:
✅
به حساب Cloudflare خود وصل شوید
✅
پنل BPB جدید بسازید
✅
پنل‌های ساخته‌شده را داخل خود اپ ببینید و مدیریت کنید
✅
پنل BPB را با مرورگر داخلی اپ باز کنید
✅
لینک‌های سابسکریپشن مختلف پنل را ببینید
✅
سابسکریپشن‌ها را کپی یا مستقیم وارد بخش VPN کنید
✅
کانفیگ‌ها را تست کنید
✅
از داخل اپ به VPN وصل شوید
✅
لاگ‌ها و وضعیت اتصال را بررسی کنید
در این نسخه تلاش شده همه چیز ساده و مرحله‌به‌مرحله باشد؛ از اتصال Cloudflare گرفته تا ساخت پنل، گرفتن سابسکریپشن و اتصال VPN.
اپلیکیشن هنوز در نسخه اولیه است، پس ممکن است در بعضی دستگاه‌ها یا شرایط خاص نیاز به بهبود داشته باشد. اگر مشکلی دیدید یا پیشنهادی داشتید، خوشحال می‌شویم گزارش کنید تا نسخه‌های بعدی بهتر و کامل‌تر شوند.
WhiteDNS BPB v1.0.0
@WhiteDNS</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/3903" target="_blank">📅 19:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3902">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">توی NPV tunnel هیچکدوم از مشکلاتی که داخل MahsaNG داشتم رو ندارم. احتمالا به خاطر dns‌هاش هست اما خود V2rayNG و Mahsa و V2rayN خیلی اذیت کردن این چند وقت سر BPB خلاصه یه تست بکنید</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/3902" target="_blank">📅 17:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3901">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">توی NPV tunnel هیچکدوم از مشکلاتی که داخل MahsaNG داشتم رو ندارم. احتمالا به خاطر dns‌هاش هست اما خود V2rayNG و Mahsa و V2rayN خیلی اذیت کردن این چند وقت سر BPB
خلاصه یه تست بکنید</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/3901" target="_blank">📅 17:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3900">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مقامات هند، تلگرام را تا 22 ژوئن در این کشور مسدود کردند.</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/MatinSenPaii/3900" target="_blank">📅 15:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3897">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qF_ybvDwNo3oGlEvSy7v9SJwAO48bOhafyiGM2BKdKZ5tGnog4mQ3F6PZ05k_cPay4SfrbEv9VLPJL9-n25O3vCg9QHDTzITY3PEkSeLCbhTH_fWT5hqtx9j2DNekOCoCgx88KfBE7r0kF-dW8rCKDegvl_5hHcPFDc-AUM1f92s-myd605y5DIMZkyH1qDlsHmQ8qyOHYMh04A_mpwHvkH625wMGo64_FbUvHy1XlJt7cEBz2M575Q8Mwn4pTprLYVBLPvmx2-LxfG4GlE9DKpN5pMtwzuF9FUH5wvzjCqfZntz-mQUkUXyYrF-AN1Hba1omw1Ixp7Qlif1woYTRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v186YLRC4TPCLtQafp8ryJhgkzXwvijGETd6KTkSWgiRLU6irnEsOlhqnox2yO4Fi0SwIXscqEvZ0XUocLQEy_9PgiSFwqZkXtJpWt5iwyZiKWEbepT4JO-D-2n0h_WVvkM71C-44Yx-AILKDYwfYIeHJnDiHKDF8IGBHHkQs1-FlUm2xUjvS5sFP1WxitfSsj0KxTcJEZSw_p9NDz-D062OLVyueoRuTXpBRayfmRvytWc86fxnQOat4WbzB1W1REHo6aEkYfZ7_MQc-V08I2OBNey5bjQXlOorD0vuGZFLsUIPrBaCw0TT5peamUQOZ1Tzs3XBJifUJEtl8gGCIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fkjh-KfGFWRktRurPDVA9v-UwZq2qtU3JVoPw952CaMj5SUa6U4U-THF1MmSkz0Gc3QBdQco-GamKTCzEDP3sgc7uk5ou1Wcs4hXjJN6EW9E1FCZndA3F5xKLV7ApS2d935WU4AYWV6HoRZlHOmXJJAJkaIu_SZnay90Srt0PfB2TNw26bQCmfBbsybPk0R5HOI7wW_4VIwgn7GHH6mylbg_Pxu6l0ZCnykwdfA2tcZA7hwsGT0InNCEjsDUdIWo-IcqN3jckn6FqczlvwBSqAYi60IFpb5Ghn6wNWXaLcBE8LBJodgUJY_Xyg1LozT2aaPYKgGgSOnVUzzNpd3gig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بعد میگن چرا کامنت‌ها رو جواب نمیدی
چون 90 درصدشون جواب توی ویدئو هست، اما ویدئو رو کامل ندیدن
✉️
مثلا اینا کامنت‌های ویدئو BPB هست</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/MatinSenPaii/3897" target="_blank">📅 12:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3894">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iu-g1VJN93bHNRSE0VqnY_RgqkNv6yAqW5JINg3sQc73hdm9hY0k0Nm36jFuBYSuUaKYGfg99DP0_04PU5pBC6VRON75YiaT5JrMJNuEh8UcbEFFHqJWEtiyBlmJ007Og2S14x-Rn94yB7VD-z_PkUAUYPdTGnWnx8sCrrpTZBOrXu2x2lhH2fUg_EpM8viAPFz3u6kXhhv1hFj-hsJZOMwfOfMHUujYsDauXOu3BaTymkxyo1628QSgAKMWjLTGkxxgcZBXhhGYiP6-EloIeT3PPR0p6DMNI8SJ5qEygqHF3dtjLm2HLv53HrR9P6jOwSb3vudXhb1Rbq5Yk5awkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cgREXOKZgn8az52S0HvsmV5NW6rkOskuNaGS0bbESJ7BteMutD5NXael8hOXQfNhOgZU5FAC4nTOMlUelFw36Ghw5shPG6ZlAZjXjRkuVzbC2utBGS9mdyBqWU9OxBWxQwdMHa0sDuysf7CY57qB5fPH6p4hVa0kZL73WswyIW1lbKGU-86JlvAeoQYn-IVVsSjapXs-YeS1YEPdHn2qGtK-FSyJPQwr_AXWEcQErZJtO-7Cdfy_9xj1V0GfHHT5ECTh9A5pzoo-gZTjb77esn28ONJUOiV9T5sVb8vwO2x1KSrG9Dthnqc0ja3PqIVTzknXurXBQFyrHzElbSBMqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PDUwlLL_VpB6fVB-nE_UoTexe-jZjrBsO2GTjDV7p9eQAfrdk6M_vJ9bzG8V1eIpyKUhX5fD9qCN5JTB_KKaarqS5y30vqmLZLEhht0W0Gw7OU3WF0M58kDbLoHloRG9sMIpKHQzpdtqtCCoyHSxR5DBFg7iWjdF1jdZfMgVRXVfIBbOwHMLr8adL_XFC30D19oNxyAuj0VQjcqmnxyie3p6fzWYsXq1ufKxh-Tb7pHwNP6KEvGjofQzksioeY9ZwzT2RPcXFyq-wbQASA55usCK0-zfCUQLv1S-Am3MiJE5u7kOsOKdQWI501KQENqFJ7SSjc2VPss_WHGbM7K-bQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا با WhiteDNS BPB هر کاربر اندروید می‌تواند تنها با گوشی خودش، پنل اختصاصی خود را راه‌اندازی و استفاده کند.</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/MatinSenPaii/3894" target="_blank">📅 11:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3893">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">از دو روز پیش، دیدم که سرعت آپلود کانفیگ‌های مستقیم پشت کلودفلر روی یه سری اپراتورا توی منطقه‌ی ما به شدت افت کرده.
و بعد که چک کردم، متوجه شدم سرعت آپلود خود اینترنت خام کمه و زیر 1 مگابیت، و مشکل از کانفیگا هم نیست.
پیر شدیم برای یه اینترنت خوب</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/MatinSenPaii/3893" target="_blank">📅 09:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3892">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">شمع iced blueberry
🫐</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/MatinSenPaii/3892" target="_blank">📅 16:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3891">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLaFeghNLOT0uMg0PjvkM7SXpMPJ-qi7y_0E6W7SmqZ3npeALu6TJFfbvWjrm89YPuhnHq4VXJWlLeSSAQoqtLRFvo60cDPmaDBlG9dcfeygt1B2bhqemS3D6VNdeo-xWvDDmMzj0wiK2I3P_cekX5-2aB2Pea3djIeG4T53tzOV1vL9usfX8_r_CjpK7fl846mpL6Dkyax8n5Za9puEYHZ2_zmT0urgSyZ9SpQw3Aahhsr-HFsV4W3BRvfVnjZH0LCWAWTDuhdBRhxq7yXSxKXD1FYeuxHe470p0Bn_KisLwZ3S2bKaxjx6j1tb70b9P2wLJTwNSNNOolDhB4liZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
جدا از همه چی رفقا این ابزار رو خودم قبلا ساختم این ابزار چیه؟
این ابزار کارش اینه که شما لینک ساب بدید کانفیگ میده با فرمت های مختلف و همچنین این که کانفیگ بدید بهتون ساب میده یه سری آپدیت ها براش میدم تا بتونید مستقیم تو اپلیکیشن ها استفاده کنید ولی فعلا داشته باشید و ازش استفاده کنید.
لینک ابزار:
✅
https://xsparvin.github.io/Abzar/
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/MatinSenPaii/3891" target="_blank">📅 13:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3890">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EEbf6G6Ty9Dm9ar4ihP3LkXRCLO3pVP0JS2nUlXdk7VMXQosE0QSC8isFicYFAucRRAN4vFS-7ICZZZ9I4jieaew1ddpHEjGYrPjYAvU7GW7wOQvXgTf8gRuugMskFXxQADvDVzgBVPHS3-zRqsZCnW9ucD0q6zWh_u4MSdidBteun19nDyJb9ZGWbubNwGzXOnEZjCIImeFrzG3jhLjgXb0_BXI9wNyaZNR3xrzHs6eSVtAPHdJ6nJ3Ln3IEEETtAIrl3BiWSNyO4RcJAomgGMHB8cFFh2Vmh4HdiEhYMoGzbe_MAmyubqEjfUUKp5GA5PRnY3rpDnddpNdotD-8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اول که ممنون از لطفتون و بازخورداتون، دوم اینکه اسکنر حجم زیادی میخوره حواستون به این نکته باشه
🧐</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/3890" target="_blank">📅 10:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3888">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/riKmiMVOty-EytC8bTnHk9v9PeVukZimtcqOGys8qb7OJT01eoHi0SpfB0fkP1AboWMXf7UXuUeG_KJ5eKo2tfv1rD1Y3HvJppDtrz5j_eEBi2dnbM4Hv4-VrEj6qB3XyzDadd3iUf4MI5kXO2GE-HPb88BzXfnTvR6dGGG3-uLO67nd0Ia2qgzWRhxdRDISpv3xyAfTJK1L2aBwwE5aX4jzMMVn2bim31NlcOEJ9JO9W8_RNjTgj1Rw_Y3KdL7OK0jIDFe6r8GzkCbafrjD0a558rUnWZucoLWbMm0TsQrCN6ZUF2v_7oYjQfxeHzS1Q9S-cLH-0Vg1dei6d-5fnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ta7GcH4rd9GLP5c8jsLnZ0Bpkgi0GCUHDIqZESyMD6_d8W7_fkUXvbbQaUm_4EPo7QQHs6VVr4TQERxrQ6jfABDN0lSyLFQ8lVNO-FR2bxYHBkz6JBTyjuuzqq-Ao6EacV1kLCrLAq44vspFLEq755l5A4T_MpB1i4A6u4OanPbQbN1wKrcUjVbGVEclPNkkfPF2CnoqKTRSGBFbYk_9xDRqwFBTrH68-7x-L6Ctl87yGvVKKxvoABklQF1MEwqNrzgkFS2CZxDzt801TCC16G9-C2wHlRpHcg-9tjmGqsOTjj9epX5cHI5XPlCIV9Ho-U_oGabPTEeOx2rWGIOLYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور: @nahanproxyipbot</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/MatinSenPaii/3888" target="_blank">📅 10:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3887">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kf66nb1PjyVmTB-TcEtbP91xEOf80GRlaQR9xADddeOFX6S7wg-mI4vzaxQQIvtE4ujPq5QgGDnEmD06AQeGMLR1rVba7hOMJuZVj3pVQ41bsuDN_B9Pt9TwrazPNQgHN0bJOsdG280cF-yQDwPsZI3JxagvPiTIibuAxO4dwyhyzlo7hiIEX9MLwu5zgLUyDUvaDhTd7NcWiwGTh5_4NG47nOnV7yeDrI683WEtC-5l-2Qzr-ispIg-g3b5W5xBJbbrUFr7-sOb4c-_MJlYcEpfo0IBIFwqdej6AKVSk1C2qomN3l1JuJKzT8VdOoweZbA3E8fT3WtN2OCVNjuLMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور:
@nahanproxyipbot</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/3887" target="_blank">📅 10:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3886">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خب قیمت دلار اومده 165
انگار جدی جدی توافق(که نه، تفاهم) شده</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/3886" target="_blank">📅 09:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3885">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ud_pVSMLjVfNN-LC4jVcOIczA5qVMf-Kbj21xf8_ghHPNvqNt4pF4Ar1vAjddZG9CU9lqfX8ZIcFm0DROr-D_e_aHXfBrsLVObU1tZQryo4t5xt55fJbAQ3XhvWe70yESMXswPwI6cZdtRQeg3j-cVjzYo29JtXSVfOyHIAKn3qKZosCffdhKVRltL-CXX3rP0_Buk2JOqqQKWr_C09eroDudufMja045RCszHFNGLZCsVAudAI_yMqt862VgEzgL_0wQhONLElAoyx49YNklbXuDmM172epUb1CXjhdTo1-PjLaV6tKot-LvG4WQ5NP767r4_1jdFEtwLCB4pHmqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پروژه‌ی جالب دیدم به اسم SurfSense، که بهش می‌گن جایگزین اوپن سورس NotebookLM
📞
اگه از NotebookLM میاید، باید بگم که SurfSense همون کارو می‌کنه؛ صرفا با کنترل کامل دست خودتون. خلاصه بخوام بگم، یه agent تحقیقاتی اوپن‌سورس و با تمرکز روی حریم خصوصیه که شبیه به کار NotebookLM رو انجام میده.
👍
مزایا نسبت به NotebookLM:
• اتصال به ۲۵+ منبع: گوگل درایو، Notion، Slack، YouTube، GitHub و افزونه‌ی مرورگر برای ذخیره‌ی هر صفحه‌ای (حتی پشت لاگین)
• آزادی انتخاب مدل: ۱۰۰+ مدل از طریق LiteLLM، یا اجرای کاملاً لوکال با Ollama و vLLM
• بدون محدودیت داده: هیچ سقفی روی تعداد منبع و نوت‌بوک نیست، و دیتا روی سرور(یا سیستم) خودت می‌مونه
• جستجوی بهتر: RAG دومرحله‌ای در برابر سرچ تک‌مرحله‌ای NotebookLM
• قابلیت‌های تیمی جالب: به شما رول‌های Owner/Admin/Editor/Viewer میده + چت و کامنت و...
• تولید پادکستا بدون محدودیته
😭
معایب:
• نصبش هلو برو توی گلو نیست واقعا. رو اعصابه — باید با dependency، API key و فایل‌های Env کلنجار برید
• هنوز کاملاً production-ready نیست و در حال توسعه‌ی فعاله
• باید خودت میزبانی و نگهداری کنی؛ طبیعتا که راحتی NotebookLM رو نداره
#️⃣
جمع‌بندی:
صادقانه بگم، NotebookLM همچنان ساده‌تر و آماده‌تره ولی کاملاً بسته‌ست. SurfSense سخت‌تر راه میفته ولی دیتا و انتخاب مدل کاملاً دست خودته. اگه با self-hosting و سرور هم بخواید پیش برید، به درد بخورترینه.
🔗
ریپوی اصلی:
github.com/MODSetter/SurfSense
آدرس خود وبسایتش برای دانلود مستقیم نرم‌افزار:
https://www.surfsense.com/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/MatinSenPaii/3885" target="_blank">📅 08:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3884">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/MatinSenPaii/3884" target="_blank">📅 21:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3883">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/MatinSenPaii/3883" target="_blank">📅 19:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3882">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n9YIdxZ5bpt8hf66XQu8NjItwzkndsj_znj9kEKrgyXP-6xlWlXmmqgR9rW3gvZOpaqUAUgpY63Gza3A8jNEJj5deq42b6ZQvnqB7K3va7v8xRwoMOhAvCAhGCnrkR3T5Qb99OCrFW7ZGMkB_XV-mNQeyyW0d_n4Yjs38JHu8Cl3TPo6bBgBgeupvfTnxJqXND2mD-P0FBEgRFZA5MKi7H0v5MVCQUZbeuJP4ueROJjS8jo7xi9RSzCHEKVgKeDaDoeGH4WUAIvBJzfnY4KlWUpE-trJaSJHEu1pPS8ctIa7Uf6Ti0DiWZGUVq1XYdjRyC4HZS0ZEV9WqUvOX3kxuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این ارور رو برای اسکنر یا هر پروژه‌ی دیگه‌ای می‌گیرید، ترموکس رو از گیتهاب نصب کنید؛ درست میشه
https://github.com/termux/termux-app/releases</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/MatinSenPaii/3882" target="_blank">📅 18:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3881">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HfYZlFoOIzOpgyFyGCGZccLoQ0l5GEnqcqarqH32xD8TOV10BycioYJ4CcEg4BCdVnxe33pUYZgbkdIvec3FjCofC4FhOsqDLhULWVLNjy_byEHB_sJBFAFhkfYXUtRYzkd8ECdTcjs7Rb_Rdv9-jTq2gUEW41u6IyEzsUR94ECB_qtqQy9-QwILrE_zBrKfjsL247VQDn7rbrvY0pvJsL2mtYol_zQ1AtwLB4_Ug2vIV2OEYx2BEU7Z-jdRwgU50-rLFTM_Gf8YZyQWyJx_DfYqaZrbDQeYOO6FOiKMc7pgMQxcyNRBQLsXJFf0xPAb4WpMpHxZDqwET2z1TqP5qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من الان خودم با سرعت عالی وصلم روی ایرانسل. ۲۰ ثانیه طول کشید حدودا، منتها ممکنه تا چند دقیقه طول بکشه. ولی وقتی وصل بشه دیگه کانکت می‌مونه و قطعی نداره</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/MatinSenPaii/3881" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3876">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.2-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3876" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه جدید اپ WhiteDNS VPN آماده شده.
در این نسخه
• سرعت اتصال بهتر شده
• مشکل داغ شدن گوشی رفع شده
• اپ همانقدر ساده مانده و فقط شما باید دکمه اتصال رو بزنید
متاسفانه باید نسخه قدیم رو پاک کنید و این ورژن رو از اول نصب کنید. این مشکل از ورژن بعدی نخواهد بود.
ممنون
🔥
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/MatinSenPaii/3876" target="_blank">📅 15:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3875">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WF34PD6da-2xT-sEPLWD_gXNszfgMhD00VAg2-XZECiq89NQPQEwbwuxqOeJ_l4oIy9987_gSAknsAxraElXg48EA5EsHWLYja8_DiLBCzyyjeCAOfJPMvohpurIFQTTq9V5w2J6cdec8NzFWAigujRoQQxZLzx70-zyvPlOfwPU8sFI1yi80_VIqkfkhEm9706QM-hQLz6MTLuCJVsAKqMk6X7vfh2iILjxojCItzWWt1cqGoLFXsEbvtfedTAfC_dYzc5IGDQ_s-V9SH71ZCUeTXV8XVscxJFcN2Ld5tEoBFGjuLUyvJyX71vXLirUVYpj_NVIJFtmg0Cme_r38Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکرشو نمی‌کردم یه روزی قالب وردپرس رو هم بگن بیاید اقساطی بخرید</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/MatinSenPaii/3875" target="_blank">📅 13:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3874">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خب دوستان به نظر من اشتباه کردم و فونت وزیر متن هستش. مسئله اینجا بود که از من پرسید، گفتش چه ترکیبی بزنم؟ چندتا داشت، یکیش فونت مربع+یکان‌بخ بود. منم زدم همین و بعد دیدم اصلا پولیه. اما الان انگار وزیر متن انتخاب کرده
نکته اینجاست که چرا اصلا فونت‌های پولی و غیررایگان باید بهشون اشاره کنه یا دروغ بگه
🤔</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/MatinSenPaii/3874" target="_blank">📅 12:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3872">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n_NdvFkfhmdumqrsXVSx_JSIpXVcGlFTXtqny2rx8rBq2DiaiOmUsSQYsSdgEyVHyhn_QNThS7LIVj1tfGKlNyfihHB743k4IQdHXdmnWRPHvefN__Gk09Qtmvz42uKSaXumJbKcNT6CZ-vSJKxCpBRDlhnmo9H74h694mU3GPcz4uk8CjuHjYJLvrcqGSujY8XrcM5V9VIkiS-JnYwW5in1mGBEPn5JKhyZqlTYTiM0dgxb_lubOg0Ifh9eq_Y2lP-_gJDX4TWlN0fh3Av7xrmKBQcDsQJ3NSrl3H2182iV9usp90W1B0X-8fr1hoegXHVM-aFaXSVYpvLyNeg2og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fZPqMDzFgz2ujY4qT4uzIy75aHOLF4-woCu8ZdvPuUNEeSJiwBBH_F5aXhwKpP0mkGFUdDi_WSag4P1481rk0-oAlDon9Q5WNrjQMj1tze54z_xYaYO8fuXPOgCab3cgOsqdTIc-7Xep-WFIa_R5dCWSHnPR6jXBTO8CVMcgNqVYe88xYjNyu2HMeHS8W2YErFJL3G81ZiuHj9BlBesPpNt9Pnm0pd_oUNaZ__xkTZjzYJPfhQYNvBj6ptoMH2d9OEBO4cOAkogtVmBVkZUOntxfleqiZ6vbR2xBmvWficFd9CQZ5bwYvd0KQxSfnxsSULjVPjY9RP1OgCnNtiVvPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کنم کپی‌رایت برای کلاد شوخی‌ای بیش نیست. اون از قابلیت اکستنشنش که کل UI و المنت‌های صفحه وب رو درجا کپی میکرد، اینم از این</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/MatinSenPaii/3872" target="_blank">📅 11:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3871">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GYwVp-jp-pwJqbgMygQw3ZFqYSwmDVoDelzLLoNpTT9HlOpKBv30eOLXz5fYNrN791-GdgFoxfohy-9uV6lLgmivUQODmRHSKP2fQQfJIjt-d17zYxKiCISJMv-_7pgt0TSzzNqYwCdzf0Tz_drd0AQczU3_zVfwAVpGNbENqABBcf4TnPSSlCXnNwSIZ3gXW123IHema2UCqbHeTWIy4FwlZFtM62iWnc2MA-8WaDqF2EIIsrRnqTeORYJbSzpHmdxpcSzCkkpLPrnHWyvqLvltEgB4Olvk0l4bniAfbRLnB_fKskyhCxOZeK-z6id_4v8Esdnj1i6M3PsAy2umdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این حد بگم که رفت فونت پولی ۵۹۹ هزار تومنی رو نمی‌دونم از کجا پیدا کرد و گذاشت توی پروژه
🤣
🤣
🤣
اصلا یه کار عجیبی کرد</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/MatinSenPaii/3871" target="_blank">📅 10:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3870">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">در این حد بگم که رفت فونت پولی ۵۹۹ هزار تومنی رو نمی‌دونم از کجا پیدا کرد و گذاشت توی پروژه
🤣
🤣
🤣
اصلا یه کار عجیبی کرد</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/MatinSenPaii/3870" target="_blank">📅 10:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3869">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">من منتظرم که شرایطم استیبل بشه، حدودا ۶-۷ تا ایده‌ی خوب یادداشت کردم هم راجب AI و برنامه‌نویسی هم واسه اینترنت آزاد که واستون ویدئوش رو بسازم</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/3869" target="_blank">📅 10:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3868">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">من منتظرم که شرایطم استیبل بشه، حدودا ۶-۷ تا ایده‌ی خوب یادداشت کردم هم راجب AI و برنامه‌نویسی هم واسه اینترنت آزاد که واستون ویدئوش رو بسازم</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/3868" target="_blank">📅 10:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3867">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏
بدافزارهایی که با ترساندن هوش مصنوعی پنهان می‌مانند!
تصور کنید یک سارق بعد از دزدی، یادداشتی آنقدر وحشتناک جلوی در خانه بگذارد که مامور پلیس بعد از خواندنش، با خود بگوید «بیخیال…» و اصلاً بازرسی را ادامه ندهد! پژوهشگران متوجه شده‌اند در موج تازه‌ای از حملات نرم‌افزاری، هکرها از ترفندی مشابه برای فریب دادن هوش مصنوعی استفاده می‌کنند؛ آن‌ها بدافزارهایی می‌سازند که بخشی از متن‌شان طوری نوشته شده که هوش مصنوعی از بررسی هرچه بیشتر صرف نظر می‌کند!
ابزارهای هوش مصنوعی کنونی، ترمزهایی از پیش تعریف‌شده دارند. برای مثال اگر از آن‌ها راجع به نحوه‌ی ساخت «بدافزار»، «تسلیحات شیمیایی» یا «تسلیحات اتمی» سوال کنید، فوراً ترمزشان کشیده می‌شود و از پاسخ دادن طفره می‌روند. حالا هکرها متوجه شده‌اند که با افزودن این نوع از متون ممنوعه به بدافزارها یا نرم‌افزارهای معتبری که آلوده شده‌اند، می‌توان فرایند بررسی امنیتی کدها از سوی هوش مصنوعی را هم مختل کرد.
به زبان ساده، مهاجم سعی دارد کاری کند که ابزار امنیتی وقتی به بدافزار می‌رسد، به‌جای بررسی دقیق کدها با خود بگوید: «من اصلاً اجازه ندارم این را تحلیل کنم» و از آن رد شود.
﻿
این نوع حمله نشانه‌ای است از ورود به مرحله تازه‌ای در امنیت سایبری؛ مهاجمان دیگر فقط انسان‌ها را فریب نمی‌دهند، بلکه رفتار هوش مصنوعی هم هدف قرار می‌گیرد و ترفندها در گذر زمان فقط پیچیده‌تر و خلاقانه‌تر خواهند شد.
✍️
NooshDaroo</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/3867" target="_blank">📅 08:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3866">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8ltUHEcBjsqqTTztapGWvdYtD7vSqldVPw2UfbQ6gYQvyLSkoFvIUcJXxQKgiCSp6WRpzy3Hy1o0xTH62q_VzV1gkIl7_PFH03OU1nqq6Sp9D0HSbyaCnZYVhp2zPdtVkUBTPZmSU5s1ZRxGY25S_EOLoiZWOqk7vSUNixs7SAZaquebz3x5Gtrb2iqwE0VcFFnXEyW-TbiLmLcSp8YgbslCX9mMlgLqK3rRU1KD7RIBDH7oeXpBe99uSMQA9olMi0BtJa3uy2KCBjM-bgNSQ3yOOnvdgnFfnJFA1IN3FTSSrl1CkWygkbMHx_VKBf2XB_q4TyVyCl1K0bWLAoY1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید دفید قراره قابلیت چت با رمزنگاری e2e داشته باشه؛
باهاش میشه ارتباط امن با خارج و داخل ایران داشت.
کل این قابلیت با ریزالور ها کار‌ میکنه تا توی فیلترینگ و قطعی شدید هم وصل بمونه.
طبق تست های من یک‌ سرور متوسط با ۸ گیگ رم و ۴ کور سی‌پی‌یو میتونه تا ۵ هزار کاربر انلاین رو هندل کنه!
اینجوری کار میکنه که هر کاربر یک اکانت رندم واسش ساخته میشه که توی سرور های مختلف ادرس اکانتش ثابت هست؛
ادرس اکانت شامل ۲۰ حرف انگلیسیه که هرکی این رو داشه باشه میتونه بهتون پیام بده.
(سیستم اکانتینگش تقریبا شکل شبکه اتریوم هست، یعنی‌یک seed دارید که با اون یک اکانت ساخته میشه)
کلاینت هر ۱۵ ثانیه به سرور هایی که بهش وصل هست درخواست میده و پیام های جدید رو میگیره و تقریبا برای ارسال یک پیام چند کلمه ای باید حدود ۴‌ کوئری دی ان اس کوچیک‌به سرور بفرسته!
واسه اینکه به سرور ها فشار نیاد محدودیت های سختگیرانه گذاشتم، ولی همه این محدودیت ها توی سرور قابل تنظیم هست و اگر سرور شخصی راه بندازید میتونید محدودیت هارو کمتر کنید.
https://x.com/i/status/2065531715041239193</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/3866" target="_blank">📅 01:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3865">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ml3CM_9lfyggd8uQX7pN8-g5smCfZGoR_QRkUIFFydXoHjdfv_lhk7s1moDiIqFhTJLZbqJqQWCdaAoTC71I7ZnQSgahs7pCO1WibsKivn2Er-ELlOdiaf7-pOEgu8XaTcb-r8eAcKHel7mTSzadkb6gZU42CvhtelKOEMMbqtp3UtHGtWSVzBuzsy-edgbowQS6INpsuzNppgkO9Gp9WkkSpcfNv-XQRoyQayDRCdqyjCekitd2a3DScfestlVhCewGdpww3lmVSfL0M6H1W9Wey7Ev7X5EgSGDni2FTLK5TWPpT3MCZd8mBQ3C37HTvcvApkCrJZVFyBABDBk3jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا به هیچ وجه روی کانفیگ Websocket معمولی سرور شخصیتون نباید اسکنر ران کنید. فقط روی Workerهاتون انجام بدید که ارزشی ندارن و ابیوز هم نمی‌خورن</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/MatinSenPaii/3865" target="_blank">📅 19:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3864">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">برای اندروید و ترموکس، کسایی که مشکل دارن طبق این آموزش دوستمون برن</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/MatinSenPaii/3864" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3863">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">برقا باز شروع کردن به رفتن؟ خیلی دیدم امروز توییتر وسط کد و گیم و ادیت و... برقشون رفته بود</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/MatinSenPaii/3863" target="_blank">📅 17:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3862">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مرحله اول  همه بخش مرحله یک  رو کپی و توی ترموکس بذار
pkg update && pkg upgrade -y
pkg install golang git -y</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/MatinSenPaii/3862" target="_blank">📅 15:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3861">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دیسلایک فیک میزنن انقد خوشحال میشم پولشونو میریزن جوب
😂
(توی یه ثانیه یهو ۱۸۰ تا اومد)</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/MatinSenPaii/3861" target="_blank">📅 14:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3860">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نمیدونم این کانالای تلگرامی چه گیری روی ری‌اکشن دارن
میگن ری‌اکشن بزنین انرژی بگیریم. انگار از ری‌اکشن برق تولید می‌کنن
عقل ندارن راحتن به خدا</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/MatinSenPaii/3860" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3859">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دیسلایک فیک میزنن انقد خوشحال میشم
پولشونو میریزن جوب
😂
(توی یه ثانیه یهو ۱۸۰ تا اومد)</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/MatinSenPaii/3859" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3856">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dpms0dH8RADxmK0Yx_4xZcM8lP6iq02v7YVnBr0tn_nP_Qx1u6c-W4sxhVhQujoWF2KTAZ7HnjBRzG9ofg0STsNr6Aw4id8hs5VVodgepuQR3ZjA1YeO7gGH_iigTMI9jv9kZP4IwL5EP2fwL5iEK9_iQUiuAxLfWI7QEDu4tkL3h29rbJ4_ZlKzkOcT0cBDsxBUKs8JTgiU_wrQ89ZGMuQVJIyUAQ-wojuGySkXgvHGlgjyDqcIi12GK4udauqi9kAqB7tKuNw9OOlK1TtksZKKFTrx9F-IbxvWr2HNVG4HhAff8SA45IqHTUpc91Yz16vaqF_Ja23ZL7ePjBReGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ldSYtWnB57M4VbsQmRFecjafEjqx2s05ta7Basm5LoAz9G37qIYRl8-w6ndsg8Y51xgRFHVuVXeLaHkV-FsBLunVOI5PTCzOOy1FbwDq1F1aUIIcNqyIrcfm6mlUrPeNWFyfgvgID3N_UB4_CILq8l1QY_nETECWHD2DYwboaDxq_RaIjFyvxRjSuYlObgOMIx1reCHh7BaJrvpURhR3gn-JK8HSyrmjz_X8v-nyCbb8AeuqtMzfM3XVPFwGW1FEKyfwojY8As7YTw-6BAEzm9ZD8yQumblVQ8WGVQdvQCUVeQ1BQDNZEMWcF03ogiGouOSzbnk1lf98iJt5BxuB2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P-gNupzwOWK9iF-7PnImZSLo1Hp65fEdsf0tRorsBlqOilnCvI8AFHZiV8t8xBwO3y1GdWW5BTdDktJgREiv3oHKtUvyGoWTskK3Bfvy5tEhOYwiClkxVaplJ1t0TAWTX7G9JylfnTIe36ZNbct9DzaHnEfAnUW4K_TdpxYEQ_6vIrhheUNjdF7RbW72dGK85GqEPTsk-fM6pEtBJGHpc_Kpehs5L0RdY0DMVORSyzLZR274wh2ztGPIgDiIEc-mdWTjevrVF4rVjGIVMVwzv_Ldhal6TL8OxDJWpOSBRA3ey5zi3uDESf3yKkY0nBBORawMXHUWFwgyi1VmInGd9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن 0.7.1 از SenPaiScanner منتشر شد
✉️
😏
پروتکل‌های جدید
: پشتیبانی از
Shadowsocks
و
VMess
اضافه شد — هر دو از فاز ۱ اسکن تا فاز ۲ xray کاملا کار می‌کنن.
🧮
خروجی چندفرمتی
: با زدن
e
بعد از فاز ۲ می‌تونید نتایج رو به سه فرمت صادر کنید:
1- لیست Subscription
2- Sing-Box JSON
3- Clash YAML
🔥
تنظیمات سرعت
: فیلتر حداقل سرعت، تست سرعت آپلود، آدرس سرعت‌سنج دلخواه، و سایز sample قابل تنظیم.
🤖
ذخیره تنظیمات
: تنظیمات اسکن ذخیره می‌شن و گزینه «retry last scan» هم اضافه شد.
📚
پشتیبانی از CIDR
: حالا می‌تونید توی
ips.txt
، مستقیم رنج‌های
/13
و... بنویسید.
📱
اولین نسخه پیش‌نمایش
اپ اندروید
با Kotlin و Jetpack Compose اضافه شد. معماری MVVM، تم‌بندی کامل، و ساخت خودکار APK از طریق CI/CD(هرچند CI/CD باید روش کار بشه هنوز).
لینک دانلود آخرین نسخه:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.7.1</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/MatinSenPaii/3856" target="_blank">📅 13:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3855">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دوستان، این شکلی میتونید به من پیام بدید:
https://t.me/MatinSenPaii?direct
اما از اونجایی که دایرکت به شدت شلوغه، و من پیامها رو اسکرول می‌کنم پایین، ممکنه گاهی اوقات زده باشه سین شده، اما من نخوندم در واقع</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/MatinSenPaii/3855" target="_blank">📅 12:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3854">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حقیقتا MiMo اگر پلن پولی بده، خودم اولین مشتریش هستم. توی تسک‌های متوسط Backend شاهکار کرد امروز
هم توی سرعت
هم توی دقت</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/MatinSenPaii/3854" target="_blank">📅 12:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3853">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هم پشتیبانی از Trojan و Vmess و Shadowsocks اضافه شده
هم تشخیص ISP
هم تست آپلود و شخصی‌سازی تست دانلود
هم WebSocket(که بهتره On بذارید)
هم هسته رو به کلی بازنویسی کردم
و این به کوشش دوستان عزیز برنامه‌نویس دیگه هم بودش که اسمشون توی Release note میاد و contributer پروژه هستن. من شاید 20 درصد از این 10 هزار خط کد که اضافه شد توی این ورژن رو نوشته بودم</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/MatinSenPaii/3853" target="_blank">📅 12:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3851">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/huaqoZeEC3XP7mqJW6GZ8qYoOB4D9eDQAr5ev4OvIE5bIM1VyPzZHsXHHzyC252CchECLx0J_oiRskKtPohswOV_0l3pMThShKCSA0_EMn1rXTnmYIlWfuZ1uPvcdTbISi2HF9dKUWsJB3mkQMGTkjY_byTrKEQCXlGTEe4JDm5JlwTCJxQNbMekS3NyLa8y7U9Iz88-VOmEGd6cgY_O0BgBiCNoc8iX5g02AB_tb4sqWuNVYudKXbAcatJocDJY89Ksw9YKtgpT09OfXBlL4zVn7ZBs_If36BgL7GHRapLVcDNHGBk_ATkDkZVoJp6cDVkffElX-xoUKxAqEZjBCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jXY5wSZgHpkLbKq_XoI_eFporXx9eFFtoBYGilTe3DeambaGsgemAFQC3aTj7gyZajYtMd7ZVXt0betRWuK9oMgJibwhvqXTi5POgQJn3gmzcFvP77WHqpCAwB_f0FUKfupaJ4qpyhhynN8gitBYl3FyY2lii9phsba6IAF-4ZhOnMvb5zdHyg8sWcL0rIpazO9M_hmWpqo8wSYj-LrPJoc9hEzJGGpswe0lOLUz8DBVSLMjsxy-U-w4d-6rwNP83SYSO7DVmYoRq6OrDlS60WHq-tQEmSNMDykBAy0VMMmNEFS9WXfR-eq__dZaGuR2Jcfa-sk3vca4usstGLkXdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بازخوردهای خوبی گرفت این ورژن که باعث خوشحالیه
❤️</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/3851" target="_blank">📅 11:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3850">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DEQTD-P9ImhYBg_vCngTCoZXEE0uQcHHV0G_rlA_HsDaptnzcdrKgi7Fy6vnlE4mcHC5eqzAVOPJKmlAGTAuJWfChwbSNKBm6xeqIi16Jcx2mD3vKS8X6vnMxhAd6_A58eIHAZy4gncRddiwspAA2clqqR57uY8naTP2loWk1-xyuE4rTCF9qUtOo7AEqhNwhln52_--ujsA8bwIIrqTcGn4IMFB6NniSGEjxV_o9BxuAwhkso2fsCujrZIcA_WI87yIVLXWECkDyP_QjDNMmyHUmtITRRfHaB-OLHI0Pp_uagofMDgRAdl9PHvuI4YXtVJTxu0RVp8ffFYdRpB76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازخوردهای خوبی گرفت این ورژن که باعث خوشحالیه
❤️</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/3850" target="_blank">📅 11:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3849">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/3849" target="_blank">📅 11:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3848">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tkZlXpoC-PnvPgj6_YVdEk9ufg1BDV6Bj-eXjE29mGeZECMThGnpdhMgCiVJthtefjZCQVFDUzFZlPF3tFkOxh78_IrCTusm5ylAr0go6GmMefVffhvP1lVYLC2WH6pAUoPE6pWSIkFHsdu-k2wR4UsOmWxTRTbXJgy4vwVO1xXwBzgRk4b6rQBMexVoSn5PiSH9eXVqucTFNV2GTy8Klhgs4jn79p2RzRsrkK-SA89VShvi3pVCR2BFeDV9G7vjT3Tryz4Z-3upo8aA1vdaTKJ4m9yHyaz0V3ng1XzPWvibysOqXmfM3b44zghr-NimtEKEt4NHLi6PNbXOplJ2Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان خوب، لطف کرد و هسته‌ی اندروید و تمام چیزی که برای ورژن اندروید نیاز داریم اد کرده، صرفا منتظرم که خود اسکنر عملکردش به بهترین سطح برسه، اون موقع نسخه‌ی اندروید هم بیلد میگیرم</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/3848" target="_blank">📅 11:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3847">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نکته‌ی خنده‌دار اینجاست که دولت آمریکا دستور داده دسترسی به این مدل‌ها برای هر فرد غیرآمریکایی (foreign national) — حتی داخل آمریکا و حتی کارکنان غیرآمریکایی آنتروپیک — مسدود بشه!!  آنتروپیک اعلام کرده که چک کردن ملیت کاربران به صورت عملی ممکن نیست، بنابراین…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/3847" target="_blank">📅 11:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3846">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/3846" target="_blank">📅 11:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3845">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/3845" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3838">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">32 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3838" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خب، دوستای من هستید یه تست از اسکنر ورژن 0.7.0 بگیرید؟</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/MatinSenPaii/3838" target="_blank">📅 11:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3837">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خب، دوستای من
هستید یه تست از اسکنر ورژن 0.7.0 بگیرید؟</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/3837" target="_blank">📅 10:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3836">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FTxpWOiPdfZTK7lMZWg88609UvmDGNSROfoZN3Dq83kSVTQb01LSMMTvZQtc6jbD2am-DphQ5HFUz44tWrWBxEDnkoVGjSDDY5d21GeuhsjcRufIW1usjH7i8boDpx3-hJ2hx0cRH29wXq5kcyZIzqh1k47ik0GSbbv6zN_U_yWJN_3TVBNpBeCYz3HmUjnKXxAQEnmxZkz4Wg9HhCKhSYBGmiaucIHPOccWwKIGsw7gKbupsptpLAoCEhR7y95-bsmIbEhrocAO197for-BNb281r_hmWRnPLDcl9qqm4WaxeI49pBskIEzuWXtG_vQfKUJRKLB5vXXeUZ8d32Tzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لپ تاپ اوکی شده الان اومدم تست کردم MiMo رو و خوشگله یه تست پرفورمنسی بریم باهاش روی SenPaiScanner</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/3836" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3835">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZGnG2lv4727c5qTi6YJELP4FZHHojSpW_WJrhMGKZquBth-0uamXw5vgXbK6XsSIPMt_-y0d5Kigsmf3XQ3GES7CuCH3JBWPULhppnWUwZBLjIW89xOFlQ91q5O69RJ_xC9_kQzMo4bp49fP0EFrDgBi31PwtSUulGw7_7yMXEUefRs2nHoRQnIoWOHcnNRcRC7W2mWrJHKeNB3x7ZGT2MLSDIIdeTD-DKm7hFM6163gV9PWF_4F1ttfq3Ol-ifdPT2RsHLgYA-KrOSMDBnhhsdcvZs6MHRjBcaZR5Mkx_CzlFDpWiiUt0CXoqIEHCJ6ajtm6FZMruqnSqauNgfAkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد  توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش فورک OpenCode هست!).  خلاصه‌ی ماجرا: تیم…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/3835" target="_blank">📅 10:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3834">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">برگام! آنتروپیک به دستور دولت آمریکا و دلایل امنیت ملی، دسترسی به مدل Fable 5 رو برای همه‌ی کاربرا مسدود کرد!!</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/3834" target="_blank">📅 09:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3833">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RWRyyXkSZUA-eN2m1_dTk4KHct3B-8ppCxzYSazFryrEwtl4jtCS9CxpmIQhWLjF_-xKjZThopg888GMj5xpO7u4Yd-4w-tV1XZ2z2b726owne8vWIx8Ge-4__qTB5BGywC4oC195UWMSqcB8pkhcXiRtC-c9UFKT7yp-NMhMR3_YR1nDSAizv-W68Nj63PnsVBmDtV7ksqlry-m1tayr4VmLKZBqs7zpQA_uUV9mSNKSjCU6h1xxDucIhvAY1Unt3jmt3vSO3wwvHqC0uuYjkAABFpfhuTzeFYFdJRRpQE8BN8vdeLDzL230jX3G0cCiYZ3ycOnnl1NEihXINRsRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام! آنتروپیک به دستور دولت آمریکا و دلایل امنیت ملی، دسترسی به مدل Fable 5 رو برای همه‌ی کاربرا مسدود کرد!!</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/MatinSenPaii/3833" target="_blank">📅 09:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3832">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">این سایت رو یکی از دوستان معرفی کرد برای دامنه‌ی رایگان، یه امتحان کنید http://l53.net/</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/MatinSenPaii/3832" target="_blank">📅 02:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3831">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aEyuOsrn3nj8oPlvp7bshVSypmx27fa1_CpLa0jQg2l_T2lkhyUAsr90fjC1XhoIf8hSlg1i540a9s5v-r1_C77kSk_zA6SZG6ow3YDC-vNY7RdVZQqfwFfiLVc2lRBSxUhDVn3U7I9R0KhU0CobDh9U3wiquIsVdtPV3ykbWKMVk8iAsanx2ZAME8RUeFAYkFI_P5hzZOzyMR9MnHWIFVxkMCay0whHro0luT_hmMktyraS8qDjSbAKlcmsngPGwdHO_ytesLJ7IlOKMtwCpLkFAvak1x9SNu0p4vDAp-k-vRkUavkRAwuOqaL5yRZOLZ7P9bnz3dsxfzEUt0u9GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت رو یکی از دوستان معرفی کرد برای دامنه‌ی رایگان، یه امتحان کنید
http://l53.net/</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/MatinSenPaii/3831" target="_blank">📅 01:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3830">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">من شرایط ضبط نداشتم دوستان. یه مشکلی هم برای لپ تاپم پیش اومده که باید بدم تعمیر و ممکنه کلا مادربوردش بسوزه اگه روشن کنم ترجیح میدم ریسک نکنم چون دیگه پول ندارم بخرم
😂
تعمیر شد، آموزش‌هایی که قول داده بودم رو ضبط می‌کنم</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/3830" target="_blank">📅 01:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3829">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWireguard Configᵛᵖⁿ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=upFWNOmkKB61d8QcJNYwT56yqxR-6bvYu0aV_V3_cTi3SRLsDeaZqneHydwmZofNAc4CcaW8CyQkT-XDDeCTeWkLwQfJKCpm4UbwwYwgmCOwPONoSRhYytJ-1frPDPsQkD1uSYGzfIjO-_Uy3WDmPgBrD9FeFkRyL0TCBpCVChCy_4KndQVZ9x-bOy1Ggzp8W08qZvOIT08v6emAOgizSLDy11RrXHInR_caYOmcXJJhOR-Wv9lptpkSe5ti7msv4dmrbz81E2dR8ms3WpLDEZaPom7SNQwDq8LWQsqkbu-ALTrXU902xWK3pGcJVcJt1Sass8b2-HE59A0iGdw5HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=upFWNOmkKB61d8QcJNYwT56yqxR-6bvYu0aV_V3_cTi3SRLsDeaZqneHydwmZofNAc4CcaW8CyQkT-XDDeCTeWkLwQfJKCpm4UbwwYwgmCOwPONoSRhYytJ-1frPDPsQkD1uSYGzfIjO-_Uy3WDmPgBrD9FeFkRyL0TCBpCVChCy_4KndQVZ9x-bOy1Ggzp8W08qZvOIT08v6emAOgizSLDy11RrXHInR_caYOmcXJJhOR-Wv9lptpkSe5ti7msv4dmrbz81E2dR8ms3WpLDEZaPom7SNQwDq8LWQsqkbu-ALTrXU902xWK3pGcJVcJt1Sass8b2-HE59A0iGdw5HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سا
خت کانفیگ Amnezia VPN
• صبرکنید ای پی ها رو لود کنه
• بعد یکی انتخاب کنید
• تیک فعال سازی پارامترهای امنزیا 1.5 حتما بزنید
• بزنید روی ساخت کانفیگ Amneziawg
• دانلود کنید وارد کنید داخل Amnezia VPN
• میتونیدم کانفیگو کپی کنید + بزنید بعد insert بزنید کانفیگ اضافه بشه
🟡
فعلا روی ایرانسل
💯
جوابه(همراه اول ،مخابرات،سامانعلی)
📍
ای پی جدید هم اضافه می‌کنم
https://darknessshade.github.io/Amnezia-VPN-Config/
@ConfigWireguard</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/MatinSenPaii/3829" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3828">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کلا فکر کنم ساعت از ۱۲ میگذره دکمه‌ی بمبارونشون روی سیریک گیر می‌کنه</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/MatinSenPaii/3828" target="_blank">📅 00:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3827">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Srdfxmg8sJU8JfYZhZiwYUMWbpBdPbnXPK9hgIE5sPMLtwumRLtmRmuATy7SkU0slUx6RGTu87mZHiOnUxTQYUCWwWJbNqLqu5XwsJtW-iY06dqEpD5MI_U3LQkSR96dJqX7gbbPtV5wI6JREMLcP-gnwdjw4pSyHWO4qXVyLZ_lc-QyExZWfzZxsc-0LvRLeVJXUDm1Cqbsdbt7_mM1-qwZLtWaWhWUpf406lXoMIaVHP4U9Q2BL9xrQ0xmo1i7we_yM6qRndpDqEAb_SVmFqLeVHvk0IReCIzmz-LFzFQiwp3VbxoxbozQV1qW_uLuZ7Z3wuJd9IvBvTFNPfyZBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد  توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش فورک OpenCode هست!).  خلاصه‌ی ماجرا: تیم…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/MatinSenPaii/3827" target="_blank">📅 00:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3825">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اگر مشکل باز نشدن توییتر با پنل BPB دارید، همونطور که توی
ویدئوی تنظیماتش
یاد دادم، NAT64 یا ProxyIP ست کنید. اگر باز هم نشد، صرفا کانفیگتون رو عوض کنید با چندتا کانفیگ تست کنید، درست میشه.
proxy chain هم صد درصد درستش می‌کنه.</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/MatinSenPaii/3825" target="_blank">📅 21:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3824">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YZq1v6GEZlncDBMzak2d6nDFhTCudqj8k5sdGtlfGMjXtrdDbxTG4rXTNVJSA2sF0XM1EIi0NTujGvWeovpX5AIz7BLMFV8LOREebFdDbJSmKEZiYKMR2lOMPYkxyNeLqrdEWYV47Axf0sCumJXvlFHMUDfIYszkeFajWUamDm6OTfyebd-er8Cqc_AOjMYEkWT_nWp41pqFs9RogtgDNbmOfXZIbO6x6piOqLgSVa3wUUICisV_v4N8b_hXeIkDANSrVpku7mhAWFLDwufQj76SZmbEcE2Ax765N-gYrGLQaVW3j47dxOl2fYYq0E8-j2zI-3uQsssVfVPA2xfVCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد
توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش
فورک OpenCode
هست!).
خلاصه‌ی ماجرا: تیم MiMo شیائومی به‌تازگی، دو روز پیش (۱۰ ژوئن ۲۰۲۶) نسخه‌ی
v0.1.0
از یه
AI coding agent اوپن‌سورس
با لایسنس MIT منتشر کرده که توی ترمینال کار می‌کنه و برای پروژه‌های پیچیده و
long-horizon
(بیش از ۲۰۰ مرحله) ساخته شده. این ابزار فقط کد نمی‌نویسه؛ می‌تونه دستور اجرا کنه، با Git کار کنه و در طول جلسات مختلف، درک عمیقی از پروژه‌ت رو حفظ کنه.
از اون‌جا که نسخه v0.1.0 هست، طبیعتاً یه پروژه‌ی اولیه و اکتشافیه — ولی معماری‌ش جدی و قابل‌بررسیه.
ویژگی‌های جذابش:
۱. حافظه ماندگار (Persistent Memory):
برخلاف ابزارهای فعلی که فقط به context window مدل تکیه می‌کنن، اینجا یه subagent جداگانه (به اسم checkpoint-writer) توی پس‌زمینه کار می‌کنه و تصمیم‌ها و پیشرفت رو لحظه‌به‌لحظه ثبت می‌کنه. حافظه روی
SQLite FTS5
(جست‌وجوی full-text) ذخیره می‌شه و توی فایل‌هایی مثل
MEMORY.md
،
checkpoint.md
و
tasks/<id>/progress.md
نگه‌داری می‌شه. وقتی context پر می‌شه، خودش از روی آخرین checkpoint بازسازیش می‌کنه؛ یعنی دیگه نیازی نیست پروژه رو از اول یاد بگیره.
۲. ویژگی Dream و Distill (خودتکاملی):
دستور
/dream
به راحتی جلسات اخیر رو اسکن می‌کنه، دانش مهم رو به حافظه پروژه منتقل می‌کنه و موارد قدیمی رو حذف می‌کنه. دستور
/distill
هم کارهای تکراری رو پیدا می‌کنه و تبدیلشون می‌کنه به skill یا command قابل‌استفاده مجدد. هر چی بیشتر کار کنی، بهتر «پروژه‌ی شما رو می‌شناسه».
۳. قابلیت Max Mode (آزمایشی):
چند راه‌حل موازی تولید می‌کنه (best-of-N) و با یه مدل داور بهترین رو انتخاب می‌کنه. که با
experimental.maxMode
توی فایل کانفیگ می‌تونید فعالش کنید.
۴. قابلیت Goal Mode:
با دستور
/goal
یه شرط توقف تعیین می‌کنی؛ وقتی agent می‌خواد متوقف بشه، یه
مدل داور مستقل
چک می‌کنه که واقعاً شرط برآورده شده یا نه — در نتیجه جلوی توقف زودهنگام و خوش‌بینانه رو می‌گیره.
۵. ویژگی Compose Mode:
با زدن کلید Tab فعال می‌شه و یه workflow ساختاریافته برای توسعه مبتنی بر spec ارائه می‌ده — با skillهای داخلی برای planning، اجرا، code review، TDD، دیباگ و merge. کل چرخه از spec تا کد نهایی.
۶. ورودی صوتی، Git و Multimodal:
ورودی صوتی real-time با
/voice
(بر پایه MiMo ASR و TenVAD، مخصوص کاربران لاگین‌شده)؛ مستقیم با Git پروژه‌ت کار می‌کنه و multimodal هم هست.
۷. سازگار با Claude Code:
authentication، skillها، MCP serverها و دستورهای قبلی رو توی یه مرحله import می‌کنه از پروژه‌ای که داشتید با Claude می‌زدید.
۸. انعطاف‌پذیری مدل:
MiMo Auto به‌صورت
رایگان(1 میلیون توکن اگز اشتباه نکنم) برای مدت محدود
و بدون کانفیگ در دسترسه، ولی خودش هم از هر API سازگار با OpenAI و prov/erهایی مثل Anthropic، DeepSeek، Kimi و GLM هم پشتیبانی می‌کنه — یعنی vendor lock-in نداریم.
نتیجه؟
طبق ادعای شیائومی، توی بنچمارک‌های SWE-Bench Pro و Terminal Bench 2 (به‌ترتیب ۶۲٪ و ۷۳٪)، با همون مدل پایه حدوداً
۵ درصد
از Claude Code جلوتره(که هنوز بعید میدونم. به چینی‌ها اعتماد ندارم). اما می‌گن تفاوت واقعی‌ش جایی خودش رو نشون می‌ده که کار طولانی و چندمرحله‌ای باشه — نه «له کردن»، ولی برتری معناداری توی long-horizon.
نحوه استفاده (خیلی ساده):
۱. نصب یک‌خطی (Mac/Linux):
curl -fsSL https://mimo.xiaomi.com/install | bash
(بهترین تجربه با iTerm یا ترمینال VSCode)
ویندوز:
npm install -g @mimo-ai/cli
۲. اولین اجرا:
خودش راهنمایی می‌کنه — MiMo Auto (رایگان) رو انتخاب می‌کنیم، با حساب شیائومی لاگین می‌کنیم، از Claude Code Import می‌کنیم تنظیمات و... رو، یا خودمون می‌سازیم.
۳.
می‌ریم تو پروژه و کار رو بهش می‌سپریم (با زدن Tab بین agentهای build / plan / compose سوییچ می‌کنیم).
لینک‌ها:
- گیت‌هاب:
github.com/XiaomiMiMo/MiMo-Code
- سایت:
mimo.xiaomi.com/en/mimocode
- بلاگ فنی (درباره long-horizon):
mimo.xiaomi.com/en/blog/mimo-code-long-horizon
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/MatinSenPaii/3824" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3819">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XZp-YT9DsTtkCcMhbFWTHs620r6sN0HKaktdkc0_1zJj4aqMPeTK_TBUrsHz9QpNjZcEY69EMTyhZjG-zVn_XG5Xck9PWNPX7eXFO58UfVMNWZb6BmbtToR-7Dhygv8ijttukF2P8xLmIvs8sABFAek-0kBhoEr2C_EDQs1TmwGS9s7QWtn62Z7jxYz7b17b51aGGTAGMBr8hlOLKTSlQ83pi3jjFpWglwZ2B-NbKX24beEQxLIRfmO727OzkwaEoHuEnxvj8djIeQv_yeMahFxnfOHD6aP0zbRmURH00QaYLjH5vHH9LNpT3wPjMvLA8GagGuMGvp47V_VMHdqW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از ChatGPT بپرسید که
یه عدد بین ۱ تا ۱۰۰ انتخاب کن
بهتون به احتمال زیاد میگه 73! علتش رو هم از خودش پرسیدم:
وقتی کسی می‌گوید «یه عدد بین ۱ تا ۱۰۰ انتخاب کن»، من واقعاً عدد تصادفی تولید نمی‌کنم؛ بیشتر یک عدد دلخواه را انتخاب می‌کنم. بعضی عددها مثل ۷۳، ۳۷، ۴۲ یا ۶۹ به خاطر الگوهای آماری و داده‌های آموزشی بیشتر از بقیه به ذهن مدل می‌آیند.
جالب اینجاست که در آزمایش‌ها، وقتی از انسان‌ها می‌خواهند یک عدد «تصادفی» بین ۱ تا ۱۰۰ بگویند، عدد ۳۷ بیش از حد انتظار انتخاب می‌شود. مغز آدم‌ها از اعداد خیلی گرد (مثل ۵۰) فرار می‌کند و به سمت اعدادی می‌رود که «تصادفی‌تر به نظر می‌رسند». من هم تا حدی همین سوگیری را دارم.
پس اگر چند نفر قبلاً همین سؤال را پرسیده باشند، کاملاً ممکن است من دوباره ۷۳ را گفته باشم
امروز توی توییتر اینو دیده بودم و واسم جالب بود علتش</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/MatinSenPaii/3819" target="_blank">📅 15:35 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
