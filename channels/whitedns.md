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
<img src="https://cdn4.telesco.pe/file/kpjQtVPilPeC1JLTGf6mxEfaA5jrblLc7Do0kHc2g5WhEiWLxYQZPmVZJYQx4ZzU4uSiTXRFMDU2QDTRTrV7MtpQd23el1uoD88DH_HyhfTm93UebpUmR4xxL5p25dczll8vh3zUz2Yf4VLj0o9jz7zpL4jnPiiE7LP5DFknC0kX5hEVA8HSSscsTkGb1KHagbKaegYj4vJQPf8kvmp7BY0WIigPJoETzEm3ioaln8OHE99UeX0HL2iU3Q40vWPmhyjiw-v6yGbc6M-NotPgReSwVzM32kKJVRmdl-sijGQ8Tm3FewkQO24SQz6AYpzMYwdm9AoltKvVElbVQVw1yw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 108K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 14:57:31</div>
<hr>

<div class="tg-post" id="msg-1216">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⚠️
⚠️
⚠️
⚠️
اطلاعیه مهم
با بالا گرفتن تنش‌ها و با توجه به تجربه‌ای که از قطعی سراسری اینترنت داشتیم، پیشنهاد می‌کنم دوستانی که تازه به جمع ما اضافه شده‌اند، مطالب زیر را با دقت مطالعه کنند.
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/whitedns/1216" target="_blank">📅 14:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1215">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">White DNS
pinned «
دوستان برای همه اینها اموزش هم گذاشتیم که الان لینک را اضافه کردیم .  لطفا بدون دیدن این اموزش ها سوال نکنید
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1215" target="_blank">📅 13:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1214">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">درود به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
🌟
با توجه به شرایط کنونی خاورمیانه، ترجیحاً هم اپلیکیشن WhiteDNS را نصب/آپدیت کنید و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/whitedns/1214" target="_blank">📅 13:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1213">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1213" target="_blank">📅 12:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1212">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/iqlHhVhfBTxSUtdwlVbDqfGH-cVnVTgMVaMYQt-sujReF4cfuP66kCCX-nQbwYB_lQ1c63g4hz43Kn726fN9K79kc1Vgp6MhKFZaZohDFLIJqNJTlsqiPTxAIb-cap0-g5VmvY8cG6Nfp8ARxrKVaTExqwhJkdMu61C-aa3v5vG5Gk08NUsml8DiDqZwLVfWbPnIp4TPsz8lR7fCfqiUUqgAlYmvGR7PylX54zKvuR336HvUVHMnzVUtSigmL00fKgH7eYQKZNrcsB702vXu8CDXcibE3z67QmGwVW6h_1J_UdrFXNEa-bg6t4UtcCb1EqzjbxoozJ3juN6rDmgAXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :
ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.
پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است همیشه کامل یا دقیق نباشند. این ربات به اینترنت زنده دسترسی ندارد، جایگزین پشتیبانی انسانی نیست و اگر اطلاعات کافی نداشته باشد قادر به پاسخگویی نیست. لطفاً اطلاعات حساس یا شخصی خود را برای ربات ارسال نکنید.
برای مدیریت بهتر منابع و کنترل هزینه‌ها، محدودیت استفاده از ربات به شکل زیر تنظیم شده است:
- هر کاربر می‌تواند در هر ۵ دقیقه حداکثر ۳ سؤال بپرسد.
🕒
- سقف استفاده روزانه برای هر کاربر ۵۰ سؤال است.
📊
- در صورت رسیدن به محدودیت، ربات زمان تقریبی انتظار را نمایش می‌دهد.
⏳
- دستور /search و سایر دستورات عمومی شامل این محدودیت نیستند.
🚫
- محدودیت‌ها پس از راه‌اندازی مجدد ربات نیز حفظ می‌شوند.
🔄
این تغییر باعث پایداری بیشتر ربات و دسترسی منصفانه‌تر برای همه کاربران می‌شود. سپاس از همراهی شما
🌱
لازم به ذکر است در صورت سواستفاده این محدودیت بیشتر خواهد شد - پس خواهشمندیم با استفاده درست جلوی به ادامه این خدمات کمک کنید
لینک ربات :
@WhiteDnsResponder_bot
🔗
@whitedns</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/whitedns/1212" target="_blank">📅 12:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1211">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/SaTYqjq-wd4BjVgYH1k9qqxVIdsmlZeJV5-unEWFVlx-GboKkda5PkJKXmkeOYC9JnAWsoGnNut1YateihFxnBm3Pg_Z5N0Sir0y6rAnQOPZ6sOW-lRmi5e3XD3ueSkWoqtg8LN_Pfv6sDWgmXS1fsRjImByNiSSHRVl6ayevsJXc4y-qutWcYaRSvhhrHWaAhlzZ6q7DDVJeG2sEZ0U0eve_ILJVgaUka4_o9KSV9j6SUaUM9ynQxU9MYOEE3PbBfrRhjpZSdGPqQYtFzah8GnIPpr_RV-k_GrXgYzzikPSsxaOeHPBZR30ksBRuO1Ecd_Ow8Tg0YFPCRvv5HfIlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
🌟
با توجه به شرایط کنونی خاورمیانه، ترجیحاً هم اپلیکیشن WhiteDNS را نصب/آپدیت کنید و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی دست یابید.
🌐
📱
لینک‌های مورد نیاز:
دانلود ورژن آخر اپلیکیشن WhiteDNS اندروید | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
🛡
آموزش
دانلود ورژن آخر اپلیکیشن WhiteDNS ویندوز | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
💻
آموزش
دانلود ورژن آخر اپلیکیشن TheFeed اندروید | جایگزین تلگرام در شرایط سخت و محدودیت شدید اینترنت
🔄
آموزش
لینک‌ها با توجه به نیاز کاربران آپدیت میشن.
🔄
@whitedns</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/whitedns/1211" target="_blank">📅 12:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1210">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/c6VyQAtDNMPVfKqk_eA0MdZH9SfsFyNCZ6UmDTdJnblE5Zdw6cnAU3uaPOzsJpMF-mSrnJP4L7rWYndBo0avsraOoe5UMjA0vZ25dXmqKs_JxIQ7iDO8qXVedWwtGDbdArgmDRy26kF4UkN2z4wE68TW2YT5jZb9Lq-_anClX-Sw10eA4lb32KF_DZIhpw9rhElaY_a8B6lNb8j0Bh7SB3WfGttuN8tUxQrBzwRpMhLZl1zJ4s8XJCW3foZeikEU7wWnqEyJ24zxmGU3Nkq_j0bec_y68FZiGHASAFGhdextgrFEaiFMOzikqWpXXQ_7EO-HYg5Jm7IgliXWOPJbag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد کردن تنظیمات بهینه در whitedns android</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/whitedns/1210" target="_blank">📅 12:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1208">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/rnaSpnfNMkmDH7gbzAjEFLLO2M-7avrmkr6U0AYI1CHdY8wVMwKEfhQhk3Fi05voTek0JXGR-bLwuIOiiVtB0axbBm6VMCWKY5LTQdrclk9t_d9VmHxKtcU3d04OuHqfFch1X-Cq_GGfHbf8cMPSRtM4g4ZL---hgbt2m-OwrvlYIXPXS2fBSSPAR9qCPNRk5h7dtl34w_p9FPGOTVMZveLF9yka9Asp4u4wn9eLObSWHDQyUYhitjYPpcAZxRNmse77uUe6l7iWZvXLAZsMIrk44kNVyOWd7xjj_eguXulZfEtFB6kjhblLeuBynLSfeZurdEMcrwZ1PbhKEj3V-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد کردن تنظیمات بهینه در Whitedns windows</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/whitedns/1208" target="_blank">📅 12:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1206">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Android.zip</div>
  <div class="tg-doc-extra">2.5 KB</div>
</div>
<a href="https://t.me/whitedns/1206" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/whitedns/1206" target="_blank">📅 12:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1205">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/JMRnbZk-MVo8alE7k6jv8krOruGbFRsXnmrQNk0uy9i4OK-p-tTFMJCAOZmd7VZAQIVYIrGpsO5h77ViJFzMXJudr8E5cs33mJ2CTwsnIf9u8yt-Yqc53WoxBWi6avnvGqn_OUA_DbYfu6bZyirmvpmOsSScQdUaEO1MDsiVsrp_-1ecuwPAz8kvqno6WgvUguTSFo0_zqPMYSxCV97aX2a2t_5hZC2OKkQdKrw2F-V9YqREAkI78wF0tSiVNsf1xXL2xir1Tn2pKPe2JhkS9Jt1-w_Xlq5mnxFWygu6fHEBL20QAG2JAmOy2utGYqN3eup6OiJizysqAxcPViYM9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
افزایش سرعت اتصال WhiteDNS
یکی از مشکلاتی که بسیاری از کاربران با اون مواجه هستن، اتصال موفق
WhiteDNS
با سرعت پایین یا ناپایداره.
✅
یکی از مؤثرترین راه‌ها برای افزایش سرعت و پایداری اتصال، استفاده از تنظیمات بهینه میباشد (البته استفاده از سرور و کانفیگ اختصاصی هم تأثیر قابل توجهی روی کیفیت اتصال داره).
📦
به همین منظور، ۳ تنظیمات پرسرعت برای
اندروید
و
ویندوز
آماده کردیم که می‌تونید از اون‌ها استفاده کنید.
🍏
کاربران آیفون:
اپلیکیشن
CoreForge
به‌صورت پیش‌فرض تنظیمات بسیار مناسبی داره و در اکثر مواقع نیازی به استفاده از تنظیمات اضافی نخواهید داشت.
📥
نحوه استفاده:
• فایل تنظیمات رو مستقیماً داخل اپلیکیشن
Import
کنید.
• یا فایل رو باز کرده و محتوای اون رو
Copy/Paste
کنید.
⚠️
توجه
:
این تنظیمات فقط
مخصوص اپلیکیشن WhiteDNS
(مناسب اینترنت ملی) هستن و به درد استفاده در
WhiteDNS VPN
نمیخورن ؛ لطفاً این دو مورد رو با هم اشتباه نگیرید.
💡
نکته مهم
:
ممکنه این تنظیمات باعث افزایش مصرف اینترنت بشن. بنابراین بعد از اضافه کردنشون ، مقادیر Download Dup و Upload Dup رو متناسب با نیاز خودتون تنظیم کنید:
🔹
مقادیر
بالاتر
👈
مصرف اینترنت بیشتر
✅
اتصال پایدارتر
🔹
مقادیر
پایین‌تر
👈
مصرف اینترنت کمتر
✅
اتصال حساس‌تر و شکننده‌تر
❤️
امیدواریم این تنظیمات تجربه‌ای سریع‌تر و پایدارتر از WhiteDNS براتون فراهم کنه.
@whitedns</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/whitedns/1205" target="_blank">📅 12:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1204">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1204" target="_blank">📅 11:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1199">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">19.2 MB</div>
</div>
<a href="https://t.me/whitedns/1199" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/whitedns/1199" target="_blank">📅 11:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1198">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Toqy_prG_NvAoze0NHJQywAY6sY4U3uzaxRWCkwqw0IOwDk6qxognV-hYmQ2pDV2aeIrnw_TS0CMZhr7K8q9cDhp3o_K0iD4cjfPKCuKMOKrv_rROz1M__2L8dKNIhEdi1QpP_9-CqbSLPIzhdHmecs7m-9FX4Sn8eFULG_DI_gKKjMz1N5iAIWyX_d2R-jO06YD2wnd31PF1JU6rXYVCLhE2CkdTRrpZ6FMAF-zNuFCfeqRyo4FPUaTH-hIL1QY57cQv0G0a0Uq0BrJM-4w-3eALRNdErcpxT9xRxyTId9n4gDcb_SnYpYTAnUf8IWDKC0u6yD-GK4_HjfzXzt2dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نسخه 0.0.9 اپلیکیشن WhiteDNS VPN منتشر شد
در نسخه جدید، اپلیکیشن
WhiteDNS VPN به‌طور کامل فارسی‌سازی شده است
تا استفاده از بخش‌ها و تنظیمات مختلف آن برای کاربران ساده‌تر و قابل‌فهم‌تر باشد.
همچنین ظاهر اپلیکیشن به‌طور کامل به‌روزرسانی شده و قابلیت‌های جدیدی برای کنترل بهتر اتصال، DNS و کانفیگ‌های شخصی اضافه کرده‌ایم.
قابلیت‌های جدید:
• فارسی‌سازی کامل اپلیکیشن
• طراحی و ظاهر جدید اپلیکیشن
• امکان اضافه کردن DNS اختصاصی با پروتکل‌های
DoH
و
DoT
• امکان وارد کردن سابسکریپشن‌های شخصی با فرمت‌های
Mihomo، V2Ray و JSON
• امکان تعیین پورت دلخواه برای قابلیت
IP Fronting
• ارتقا و بهبود بخش
Connection
و فرایند اتصال
• اضافه شدن قابلیت
TLS Integrity Test
قابلیت
IP Fronting
به‌خصوص در دوران قطعی یا اختلالات شدید اینترنت می‌تواند بسیار کاربردی باشد. حتی در شرایط فعلی نیز کاربران می‌توانند با استفاده از IPهای تمیز Cloudflare، بعضی از کانکشن‌هایی را که به‌صورت عادی کار نمی‌کنند دوباره فعال کنند.
قابلیت
TLS Integrity Test
نیز برای کاربرانی اضافه شده که هنگام استفاده از بعضی کانفیگ‌ها، برای اتصال به سرویس‌هایی مانند
ChatGPT
با مشکل مواجه می‌شوند.
با فعال کردن این گزینه، اپلیکیشن پیش از اتصال، سلامت و یکپارچگی TLS را بررسی می‌کند. اگر TLS دست‌کاری یا جایگزین نشده باشد و تست با موفقیت انجام شود، اپلیکیشن به کانفیگ متصل خواهد شد.
در صورتی که یک کانفیگ این تست را با موفقیت پشت سر نگذارد، اپلیکیشن بررسی کانفیگ‌های دیگر را ادامه می‌دهد تا یک اتصال سالم و مناسب پیدا کند.
فعال کردن این قابلیت ممکن است زمان اتصال را کمی افزایش دهد، اما می‌تواند مشکل باز نشدن ChatGPT و سرویس‌های مشابه را برطرف کند.
پیشنهاد می‌کنیم همه کاربران از همین حالا اپلیکیشن را دانلود کرده و آن را به آخرین نسخه به‌روزرسانی کنند. این نسخه یکی از راهکارهایی است که برای شرایط قطعی و اختلالات شدید اینترنت روی آن کار کرده‌ایم و ممکن است در چنین شرایطی بتوانیم استفاده بسیار بیشتری از قابلیت‌های آن داشته باشیم.
📱
WhiteDNS VPN v0.0.9</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/whitedns/1198" target="_blank">📅 11:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1196">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I3YjlONBSGIRx3Z9sFGJiSEuTX8wr1c8318mMsLHRFbMoe80L3rzUq55zacZOZF0w-t1suUB-TUabY0fx-5GDmG1rqEcWxtDvY8RzNw3y4yuShnSuDa472AU1X4neMWsQrU3dmxkbuPeQoaIUBbt6rEXrqoFlhS8SfPZVzdPCFoN3zvo5joXg9UOQeU677C3p78DUfBeY-sqHIIinBafQ8lW4Mxsme1TDoS9qC71ozVANCAp26r3a08aqvq7X5ExurkAz6gNpMDTAyuSAp_HjaUCeOysG8wDTABnE5gZ1E5bB_zFFyPDpzCDGCLEBlsCrr2jppLPU1-jzhX8JngxWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M6B0hJ6ufcZN8MGBxDjQf4zO-Ob-L2x7n44cDqn63dXYhBEtpwoM8xSmV30ocSeXZ3P50iRukBqLqaKIk5eh9w-xENCTLee2SirksqtBLS5G_-L843jNJNcpH8caEXD1fBcdgjE477Ok-SvC2y4U5GSu4F7X2lWjzGnbT3bum9e3lmNHl9eJ3t82buQIDD5ZOGwXCmQ3BNvOa1tJIfZqnNEJOubBvmrUyCz0ebZxPjofi7ZpYBwJ_ubFrMNr5FJ3sLANRQROpiCzI6Lk9tCrIjD42ZmlfFhyUnkUKhR_4Zo_zuTOi2q4AaYxmeknIV_5EOT8kaeQJwVP3OK93xcX-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آپدیت جدید Aether-GUI (نسخه 0.4.0) با هسته‌ی جدید!
نسخه‌ی جدید برنامه آماده‌ست. توی این آپدیت، هسته‌ی اصلی (Aether Core) به ورژن
1.2.0
ارتقا پیدا کرده و قابلیت‌های زیر به GUI اضافه شده:
🔵
رفع مشکل وضعیت Connected فیک:
قبل از این، بخش Validation ابزار با پینگ کردن
1.1.1.1
(که داخل شبکه‌ی خود کلودفلر هست) وضعیت رو متصل نشون می‌داد؛ در حالی که ممکن بود ترافیک واقعی اینترنت قطع باشه و لود نشه. حالا ابزار یک ریزالور خارجی رو هدف قرار میده و باید ۲ بار پشت هم موفق بشه. یعنی وقتی می‌نویسه Connected، واقعاً متصله.
🔵
اضافه شدن انتخاب ترنسپورت برای MASQUE:
توی بخش Advanced الان می‌تونید نوع پروتکل ارتباطی MASQUE رو تغییر بدید:
HTTP/3 (QUIC):
حالت پیش‌فرض؛ سریع‌ترین هاندشیک و بهترین کارایی (اگر شبکه شما با UDP مشکلی نداشته باشه).
HTTP/2 (TCP):
کاملاً شبیه به ترافیک عادی HTTPS؛ مناسب برای زمان‌هایی که شبکه شما UDP/QUIC رو اختلال می‌اندازه یا مسدود می‌کنه.
تنظیمات انتخابی شما به‌طور خودکار ذخیره و در استارت‌آپ بعدی اعمال میشه. (این سوییچ فقط روی پروتکل MASQUE تاثیر داره و برای WireGuard/gool غیرفعاله).
🔵
به درخواست دوستان فرانت کار لوگو هم از دیفالت عوض شد
🤠
دانلود نسخه 0.4.0:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.4.0</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/whitedns/1196" target="_blank">📅 04:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1195">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/eWe42sKpK5io-1ZBDwAWoVh7Acsu4M_02tzGTyJ69_G_fPtnhOBCvA6RYzsu2d8yAbkNbk23lCCn8hWUUZPj8RTXPIxvrCjCHLL4xZLiYTDflpUghlXM9Czae2N9GSEdaSt-B_HFC8va2f2m_FmvPB8BXNb5dp9FxfTK2uf6D_UR0SVQBR11Z1HSMAvp9_QFOJnkLKtf3OUJW0IOatMRZc1y3HfK62fz5xx1AQHXqAR_YsPIS5OQ5nk6D8KAo10iePCQTs7CFQnbJe7EBVTNSSc-9qBFUKpaVV0-CjzTD_1AAh2OYK86yBlzltuF6VHh_M4gIWkK5-F4d_xp1x1zgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
راهنمای جامع تنظیمات APN اپراتورهای ایرانی
📱
📥
۱. مراحل تنظیم در اندروید (Android):
1. وارد
تنظیمات (Settings)
شوید.
2. به بخش
اتصالات (Connections)
یا شبکه و اینترنت بروید.
3. بخش
شبکه‌های موبایل (Mobile Networks)
را باز کنید.
4. وارد گزینه
نام نقاط دسترسی (Access Point Names یا APN)
شوید.
5. روی
افزودن (Add / +)
بزنید تا APN جدید ساخته شود.
6. فیلدهای
Name
و
APN
را مطابق لیست زیر پر کنید (بقیه گزینه‌ها مثل پروکسی و پورت حتماً خالی باشند).
7. از منوی سه نقطه بالا گزینه
Save (ذخیره)
را بزنید و آن را فعال کنید.
🍏
۲. مراحل تنظیم در آیفون (iOS):
1. وارد
تنظیمات (Settings)
شوید.
2. به بخش
Cellular (تلفن همراه)
بروید.
3. گزینه
Cellular Data Network
را انتخاب کنید.
4. در بخش
Cellular Data
، روبه‌روی گزینه
APN
مقدار مربوط به اپراتور خود را (از لیست زیر) وارد کنید.
5. یک‌بار اینترنت گوشی یا حالت پرواز را خاموش و روشن کنید.
📋
لیست مقادیر APN اپراتورها (برای کپی آسان روی کلمه‌ها ضربه بزنید):
🔹
همراه اول (MCI)
* Name: MCCI Internet
* APN: mcinet
🔹
ایرانسل (Irancell)
* Name: Irancell-GPRS
* APN: mtnirancell
🔹
رایتل (RighTel)
* Name: RighTel
* APN: rightel
🔹
شاتل موبایل (Shatel Mobile)
* Name: Shatel Mobile
* APN: shatelmobile
🔹
سامانتل (Samantel)
* Name: Samantel
* APN: samantel
🔹
تالیه (Taliya)
* Name: Taliya GPRS
* APN: taliyagprs
⚠️
نکته بسیار مهم:
اگر در فیلدهای
Proxy (پروکسی)
یا
Port (پورت)
در تنظیمات گوشی شما هرگونه عدد، آدرس یا کلمه‌ای وارد شده باشد، سرعت اینترنت شما به شدت افت خواهد کرد یا کاملاً قطع می‌شود. حتماً بررسی کنید که این دو بخش کاملاً
خالی
یا روی
Not set
باشند.
@whitedns</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/whitedns/1195" target="_blank">📅 16:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1194">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1194" target="_blank">📅 13:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1192">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :   ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.    پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/whitedns/1192" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1191">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1191" target="_blank">📅 12:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1190">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/PTmOvkLImULCwt2ZDpKhuSQxbAgdP7W0j8HjMGgBmIBAOTQrJEGY-VOSGh1gihddr2zyalYKp0LOCD8PjKfYZeRcGyWWZrUpR5-bxljYgl2RcaYLyRlfygYgjZAlj44Qy8fw4A0n_wJcA6is8BVqQsN5QeH3Odn5hG_u2ZoiXjOxBn39HQf5ahrKJeNv-bYMqqbfGuGLjqBu2qkR4zgNC9uhKHgF5tttJipFW3kJdRlxob5Kuagi5zuHQARsfJ6Y17lsFc_nFHKIMTz2DlWkEPAnz31A1BbznaZOOXy_AiezakB5UgtJE-_uUDb36-IyfRGLl0pvDRmSW5DpDA1Abg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :
ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.
پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است همیشه کامل یا دقیق نباشند. این ربات به اینترنت زنده دسترسی ندارد، جایگزین پشتیبانی انسانی نیست و اگر اطلاعات کافی نداشته باشد قادر به پاسخگویی نیست. لطفاً اطلاعات حساس یا شخصی خود را برای ربات ارسال نکنید.
برای مدیریت بهتر منابع و کنترل هزینه‌ها، محدودیت استفاده از ربات به شکل زیر تنظیم شده است:
- هر کاربر می‌تواند در هر ۵ دقیقه حداکثر ۳ سؤال بپرسد.
🕒
- سقف استفاده روزانه برای هر کاربر ۵۰ سؤال است.
📊
- در صورت رسیدن به محدودیت، ربات زمان تقریبی انتظار را نمایش می‌دهد.
⏳
- دستور /search و سایر دستورات عمومی شامل این محدودیت نیستند.
🚫
- محدودیت‌ها پس از راه‌اندازی مجدد ربات نیز حفظ می‌شوند.
🔄
این تغییر باعث پایداری بیشتر ربات و دسترسی منصفانه‌تر برای همه کاربران می‌شود. سپاس از همراهی شما
🌱
لازم به ذکر است در صورت سواستفاده این محدودیت بیشتر خواهد شد - پس خواهشمندیم با استفاده درست جلوی به ادامه این خدمات کمک کنید
لینک ربات :
@WhiteDnsResponder_bot
🔗
@whitedns</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/whitedns/1190" target="_blank">📅 12:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1188">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🛡
ورژن جدید WhiteDNS VPN
👆
👆</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/whitedns/1188" target="_blank">📅 11:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1183">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">19.2 MB</div>
</div>
<a href="https://t.me/whitedns/1183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/whitedns/1183" target="_blank">📅 11:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1182">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXZCgPpPzDJy4KGEN_beVlnu9TqDJyMlwZNoX8CcwSn1928WlrPlvg-JMvI2TanKbj-C0NKDX0uJ3VRCsZIF-zFiWs5Q5sP9ekn6e9UmtArasqYIHMg-blk2raXBQ4hkCjFpLQbF-u4mFQYaCVznHNvPJKRv8nk3eICF7DpsT8afob9hbgw6tUeOHWQt5G2cJ8j_am8XzZq3Mhm4v9Y12FvtS2SGAlkG2-GeTiN2M6onJXnxgcMQn-ct0nxrhNQd-QwfIa-vxMLHYcdy0ekjeevCVSHdU8fK9KXFM3qb44yIdexbLK3s4-mZMDve4ie3QYZXXmVQ8VtU9tzezXyABQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نسخه 0.0.9 اپلیکیشن WhiteDNS VPN منتشر شد
در نسخه جدید، اپلیکیشن
WhiteDNS VPN به‌طور کامل فارسی‌سازی شده است
تا استفاده از بخش‌ها و تنظیمات مختلف آن برای کاربران ساده‌تر و قابل‌فهم‌تر باشد.
همچنین ظاهر اپلیکیشن به‌طور کامل به‌روزرسانی شده و قابلیت‌های جدیدی برای کنترل بهتر اتصال، DNS و کانفیگ‌های شخصی اضافه کرده‌ایم.
قابلیت‌های جدید:
• فارسی‌سازی کامل اپلیکیشن
• طراحی و ظاهر جدید اپلیکیشن
• امکان اضافه کردن DNS اختصاصی با پروتکل‌های
DoH
و
DoT
• امکان وارد کردن سابسکریپشن‌های شخصی با فرمت‌های
Mihomo، V2Ray و JSON
• امکان تعیین پورت دلخواه برای قابلیت
IP Fronting
• ارتقا و بهبود بخش
Connection
و فرایند اتصال
• اضافه شدن قابلیت
TLS Integrity Test
قابلیت
IP Fronting
به‌خصوص در دوران قطعی یا اختلالات شدید اینترنت می‌تواند بسیار کاربردی باشد. حتی در شرایط فعلی نیز کاربران می‌توانند با استفاده از IPهای تمیز Cloudflare، بعضی از کانکشن‌هایی را که به‌صورت عادی کار نمی‌کنند دوباره فعال کنند.
قابلیت
TLS Integrity Test
نیز برای کاربرانی اضافه شده که هنگام استفاده از بعضی کانفیگ‌ها، برای اتصال به سرویس‌هایی مانند
ChatGPT
با مشکل مواجه می‌شوند.
با فعال کردن این گزینه، اپلیکیشن پیش از اتصال، سلامت و یکپارچگی TLS را بررسی می‌کند. اگر TLS دست‌کاری یا جایگزین نشده باشد و تست با موفقیت انجام شود، اپلیکیشن به کانفیگ متصل خواهد شد.
در صورتی که یک کانفیگ این تست را با موفقیت پشت سر نگذارد، اپلیکیشن بررسی کانفیگ‌های دیگر را ادامه می‌دهد تا یک اتصال سالم و مناسب پیدا کند.
فعال کردن این قابلیت ممکن است زمان اتصال را کمی افزایش دهد، اما می‌تواند مشکل باز نشدن ChatGPT و سرویس‌های مشابه را برطرف کند.
پیشنهاد می‌کنیم همه کاربران از همین حالا اپلیکیشن را دانلود کرده و آن را به آخرین نسخه به‌روزرسانی کنند. این نسخه یکی از راهکارهایی است که برای شرایط قطعی و اختلالات شدید اینترنت روی آن کار کرده‌ایم و ممکن است در چنین شرایطی بتوانیم استفاده بسیار بیشتری از قابلیت‌های آن داشته باشیم.
📱
WhiteDNS VPN v0.0.9</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/whitedns/1182" target="_blank">📅 11:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1181">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1181" target="_blank">📅 08:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1180">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/rX48XXnoZ22sZdMHfzZDCZ_yIvpiCtjUU0AsPkPfMcBGW14B0C1x5YXzHTjX26qRDcoF3kd75Gcz8nazQ7T2b5xqCEx8vyLGzGhA7UCX7TNKKv3Rz7gt6surQNLc1flwevpn89uk68Iwwq6kxNAdK3-0fjoW_Q3iJ7Dvm3kC9BLVXYwzB1cs6Ym4qEiljWaLjcY6HNl1WGFDW-5uvS0tKyrJjsRrxtTNsQpEIjzGVyhKd2CRAtDhEglNFu3VWFtxM64fjHq9pe4dL-ewtx65UiAi_px04z7vs1POOfuRidZQqr_ZSk67YqnmUg8CaFibM4y7jSpUjMyKyPALFUR7aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی کانال یوتوب WhiteDNS
🌐
اگر به دنبال آموزش‌های تخصصی و کاربردی برای دور زدن فیلترینگ، پیدا کردن آی‌پی‌های تمیز و ساخت سرورهای شخصی هستید، این کانال یکی از بهترین مراجع آموزشی است!
🎓
در این کانال می‌آموزید:
🔹
آموزش صفر تا صد V2Ray
و راه‌اندازی پنل‌های ثنایی (3x-ui)
🔹
پیدا کردن آی‌پی تمیز با
WhiteDNS Scanner
🔹
راه‌اندازی
پروکسی MTProto
برای اتصال بدون قطعی تلگرام
🔹
معرفی ابزارها و کلاینت‌های مختلف (مثل CoreForge برای iOS و FlClash برای اندروید)
🔹
راهکارهای ارتباطی برای زمان قطعی کامل اینترنت
📡
و .................................
برای یادگیری ساخت فیلترشکن‌های امن و پرسرعت، همین الان به این کانال سر بزنید و سابسکرایب کنید.
👇
🔗
https://www.youtube.com/@WhiteDNS</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/whitedns/1180" target="_blank">📅 08:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1179">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✍️
در مدتی که اینترنت وصل بود، تیم ما تلاش کرد ابزارها و روش‌های جدیدی آماده کند تا در صورت بروز قطعی شدید، بتوانیم بهتر از شما پشتیبانی کنیم.
متأسفانه بسیاری از این ابزارها را تا امروز منتشر نکرده‌ایم که برای این تصمیم دلایل منطقی و امنیتی وجود دارد.
در صورت شروع محدودیت یا قطعی گسترده، تلاش می‌کنیم این روش‌ها را به‌تدریج معرفی و در اختیار شما قرار دهیم.
برای شروع، تعدادی سرور MasterDNS نیز منتشر خواهیم کرد. با این حال، پیشنهاد می‌کنیم در صورت امکان، یک سرور تهیه کنید و با استفاده از ربات زیر آن را به‌سادگی کانفیگ کنید:
@WhiteDNS_installer_bot
❤️
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/whitedns/1179" target="_blank">📅 04:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1177">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/N1oB7yYw0KYbTxICbr-CKPTPjhjOUz7AjCzkpok7Fntw-oOjO5Zcz1457xWk6uWs9SjIdyDR-UuT6cDRQGXy426mlZikLAJuiTyUOOgHZWj3-1lcsoCmUkrDDBwBypG7hR6zCI3_xaPX4IDod4y8IURbk2UJcmlqJ1EXv-GDg3-24fbqNWPBt8kLG95d8GJhUTBlkVNdfOtcUbvQpIhihe_RjCB2cx7q-Jh4s2IY1XpJAMcwc6XqsMHJqOmNMy3MOuDESiAbOSGcJPCFfzAdHAwN4GrwGTaFwncwHyJYHeiYEDgyCA6877hTiMrIUHwcvZWZfDNEN3B5QrkDWwa8XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
دستیار هوشمند کانال WhiteDNS
👉
@WhiteDnsResponder_bot
✅
جواب سریع |
✅
۲۴ ساعته |
✅
رایگان
نحوه استفاده:
۱. روی لینک بزنید
۲. Start
۳. سوالتان را بنویسید
مثال: چطور فیلترشکن نصب کنم؟
/search عبارت — جستجوی مستقیم
/contact — ارتباط با ادمین
⚠️
ربات WhiteDNS در چه زمینه‌هایی جواب می‌دهد:
✅
فیلترشکن و VPN
✅
DNS و تنظیمات اینترنت
✅
آموزش نصب اپلیکیشن‌های WhiteDNS
✅
رفع مشکلات اتصال
✅
Warp و Cloudflare
✅
تنظیمات اندروید، آیفون، ویندوز، مک
✅
سوالات مربوط به قطعی اینترنت
❌
ربات قادر به پاسخ‌گویی به سوالات غیرمرتبط با موضوعات کانال نیست.
💡
نکته: اگر جواب دقیق نگرفتید، سوالتان را طور دیگری بنویسید یا از دکمه جستجو استفاده کنید.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/whitedns/1177" target="_blank">📅 17:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1176">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/HiiFgIz0QBCyhI1AVKV3nNKtvx_ucM4jqwevpY9-emk3pUimrUFcNP0s0lDigrJ31N4mtDskxey4tcAWN8vx4NPEMlYI23maUPbmM71lZygGDTeuhx0hzWFRLPFbZMfhH8rdAgvvHnx3GMuXPNNQynaMKW61rVr6_apkI42itGF6kjmDLwNJjJLucUz67XU6ZEIYiBXyIkcdPbF-u56dn1FDEVFkYf8qW9glFCpvqnBxqfc-3BfTwMk995hRi1YCr6EA3YwxXDYjfK8cwu-lAO6v3K6aJhl22dpj8slVBbdw4vTTt56WSkHJVbsDeewEKHDFBSqY3a3Xg2Lhuioo9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
OnionHop V3.7.2 - انتشار جدید: اتصال هوشمند و عیب‌یابی شفاف
آیا می‌خواهید ترافیک سیستم خود را بدون درگیری با تنظیمات پیچیده از شبکه Tor عبور دهید؟ OnionHop، ابزار متن‌باز، سبک و قدرتمند ویندوز، برای همین کار ساخته شده است. نسخه جدید 3.7.2 تمرکز ویژه‌ای بر پایداری در شبکه‌های سانسور شده و شفافیت عملکرد دارد.
✨
امکانات و قابلیت‌های کلیدی:
🛡
حفاظت دوگانه:
انتخاب بین حالت
پراکسی
(سبک) و
VPN
(سیستمی).
🌉
عبور از سانسور شدید:
پشتیبانی کامل از Bridgeهای Tor، شامل
obfs4
,
Snowflake
,
WebTunnel
,
meek
, and
dnstt
.
🌍
انتخاب کشور خروجی:
امکان انتخاب دقیق کشور نود خروجی (Exit Node) برای تغییر موقعیت جغرافیایی.
🔒
امنیت بالا:
شامل
Kill Switch
(قطع خودکار اینترنت در صورت قطعی Tor)،
DNS امن (DoH)
و پشتیبانی از
IPv6
.
🚦
تونل‌بندی هوشمند (Split Tunneling):
انتخاب کنید کدام برنامه‌ها از Tor عبور کنند و کدام‌یک مستقیماً متصل شوند.
🤖
اتصال هوشمند (Smart Connect):
قابلیت جدیدی که به طور خودکار بهترین استراتژی اتصال، موتور Tor و Bridge را برای شبکه شما انتخاب می‌کند.
📢
مهم‌ترین تغییرات نسخه v3.7.2:
۱. تشخیص و تأیید ۱۰۰٪ پل‌های WebTunnel
در نسخه‌های قبلی، برنامه فقط آنلاین بودن CDN را بررسی می‌کرد. در نسخه ۳.۷.۲، OnionHop یک
اتصال آزمایشی واقعی (Handshake)
با خود پل برقرار می‌کند تا مطمئن شود که آیا واقعاً ترافیک را عبور می‌دهد یا خیر. این یعنی دیگر پل‌های خراب به اشتباه «سالم» نمایش داده نمی‌شوند و شما زمان را برای تست اتصال‌های مرده تلف نمی‌کنید.
۲. عیب‌یابی شفاف با لاگ‌های دقیق
اگر یک Pluggable Transport (مثل obfs4 یا Snowflake) به هر دلیلی اجرا نشود، دیگر با پیام‌های مبهم مثل "status code 2" مواجه نمی‌شوید. OnionHop قبل از اجرا همه‌چیز را بررسی می‌کند و دلیل دقیق خطا را در لاگ‌ها نشان می‌دهد؛ مثلاً: فایل اجرایی خراب است، نسخه اشتباه پردازنده است، یا مجوز دسترسی وجود ندارد.
🛠
راهنمای قدم‌به‌قدم اتصال (How-To Connect Guide)
براساس اطلاعات مخزن گیت‌هاب، نحوه اتصال بسیار ساده است:
نصب و اجرا:
فایل نصبی (.exe) را از لینک زیر دانلود کرده و اجرا کنید.
اولین اجرا (انتخاب حالت):
Proxy Mode (پیشنهادی):
اگر فقط برای مرورگر یا برنامه‌های خاصی به Tor نیاز دارید، این حالت را انتخاب کنید. نیازی به دسترسی Administrator ندارد. باید تنظیمات پراکسی برنامه خود را روی
SOCKS5 127.0.0.1:9050
قرار دهید.
TUN/VPN Mode (دسترسی ادمین):
اگر می‌خواهید
تمام ترافیک ویندوز
(کل سیستم) از Tor عبور کند، این حالت را انتخاب کنید. این کار با استفاده از Wintun و sing-box انجام می‌شود.
انتخاب پل (در شبکه‌های فیلتر شده):
به بخش
Scanner
بروید. اگر در شبکه‌ای با محدودیت هستید،
Bridges
را فعال کنید و روی
Scan
کلیک کنید تا برنامه‌ها پل‌های سالم را برای شما پیدا کنند.
اتصال:
روی دکمه بزرگ
Connect
کلیک کنید.
Smart Connect:
برای راحتی بیشتر، می‌توانید Smart Connect را در حالت خودکار قرار دهید تا برنامه خودش بهترین تنظیمات را اعمال کند.
🔗
لینک‌های رسمی
🔗
متن‌باز و رایگان
#اوپن_سورس
🚀
دانلود مستقیم نسخه V3.7.2:
https://github.com/center2055/OnionHop/releases/tag/v3.7.2
🌐
وبسایت رسمی:
https://www.onionhop.de
@whitedns</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/whitedns/1176" target="_blank">📅 14:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1175">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns16.7.2026.txt</div>
  <div class="tg-doc-extra">18.3 KB</div>
</div>
<a href="https://t.me/whitedns/1175" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@whitedns
🔗</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/whitedns/1175" target="_blank">📅 12:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1174">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/OYAHatIq-erR55FyzS3u3GxjvU9Xl26D94h0vcjMoTPPj-nQ3Lo9pe0k_HD1Wxmoeh-HIYWB8JPZsm_Dctke5KoiliYDgW6CZxNpcwreM5SF6K0soH-uERyc_4aFV5CibjBSg4l4kKgrDa84Q_4ymkFehadXljt7DiYkn4fw1s42rgbezNaD_dYQAY_u0Rs6gMIQ3ZUxXP-obxYf2M567vuUxuuTKyXRSPSeZr0vD9tG9poXk59R4O7YK08a-DNLhyBhFXKIf0wKdYhhMbFlIiMdB0qFGrzc-Sx85Q_R5dn4zpm1vhkAL35WBERrISZNvynVu-JAEoJlBBgksLGD0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">16.7.2026
فایل زیر را دانلود کنید
⬇️
1. کانفیگ‌های داخل فایل را کپی و در برنامه v2ray وارد کنید
📋
یا
2. خود فایل را از طریق گزینه import locally در برنامه v2ray وارد کنید
📥
@whitedns
🔗</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/whitedns/1174" target="_blank">📅 12:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1173">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1173" target="_blank">📅 12:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1172">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/UgF2IJeAI_W4Up3JHezwCBeQCaw64x7XOagB5mTTpo8yKYpDad0hSJUEiTxVzzODOx0tpbIaZLJ0_f5oY7pQXymtM7-tFhRct4kb2uGl7EA_Fl7Ie7Fw3edeJquWEFXRgMMUd1rEAPxvKa1rRx8WfDbQrKuIdYR3pvbzI1sarENrOLGsx-3-lhAZzhAiHBmVPovNcgiE7G7t4zen9xJ17szNInpCy43x-Wy_RR-M1namdFXuVvqkePuO-XqUXAQMYy7OuTMKtLfMnueekslBI_NIKZxHWwPWHtuxFmx59_P8j_i6Aq68vWAVx-c3k58YYmPOKkexLihdCB47GDCL-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش جامع استفاده از
WhiteDNS VPN
و
WhiteDNS Scanner
برای اتصال امن و پرسرعت!
🚀
🛡
رایگان
در این ویدیو به بررسی تخصصی ابزارهای اختصاصی *WhiteDNS* پرداخته شده است که به شما کمک می‌کند بدون نیاز به دانش فنی پیچیده، به اینترنت آزاد متصل شوید.
🌐
🔓
خلاصه‌ای از مباحث آموزش داده شده:
📝
راه‌اندازی WhiteDNS VPN:
نحوه نصب اپلیکیشن و اتصال اولیه بدون آی‌پی تمیز (0:00 - 5:30)
⚙️
📲
*
اسکنر قدرتمند WhiteDNS:
آموزش کامل کار با بخش *IP Scanner* برای پیدا کردن آی‌پی‌های تمیز و پرسرعت (7:40 - 18:00)
🔍
⚡️
*
کاربردهای حرفه‌ای اسکنر:
بررسی قابلیت‌های پیشرفته مانند *SNI Scan*، *HTTP Proxy Scan* و *Config Maker* برای ساخت کانفیگ‌های شخصی‌سازی شده (20:30 - 27:30)
🛠
🔧
*
نکات طلایی:
نحوه استخراج آی‌پی‌های تمیز از دیتاسنترهای مختلف و استفاده از آن‌ها در برنامه‌هایی مثل *v2rayNG* و *Psiphon* (22:40 - 25:00)
💎
🌍
✅
این ابزارها با رابط کاربری ساده، برای همه کاربران (مبتدی تا حرفه‌ای) مناسب است.
👨‍💻
👩‍💻
📥
لینک‌های دانلود:
- دانلود اسکنر: [GitHub WhiteDNS]
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/1.3.5
- دانلود اپلیکیشن: [Telegram Channel]
(
https://t.me/whitedns/1072
)
💬
با تماشای این ویدیو، سرعت و پایداری اتصال خود را به شکل چشمگیری افزایش دهید!
📈
🚀
لینک ویدیو :
👇
https://www.youtube.com/watch?v=N5hKuWXp37w&t=57s
@whitedns</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/whitedns/1172" target="_blank">📅 11:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1171">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/FUoU2F5b0WhPNwlgAiJMNhQqeNOWUw9EXw6iBGdZONttXAZPP8lWgWyrGW-Vj4KRzUge7WXQFmDUMTC5s_ZNG-Du5j5KaLcdHDIKpWvXZz-66Q0G17hmqnPiABTQj4D2yGVHsATjPlpxuT8DP3EBhKyz3pezKe9-Ji0BrNlisd_qoaP2nnCWftR3b7qfKuEkxdiZg6jkD6q-XW-EZ1Sa8G-NJFyycaxo2nSIrce_wQNzlU80OE2vv2LOqDw754mEoILf7ejyDz-usZVPGflA2fC-2UAEcupeCqHoDetjJYZAI-8UZXfCt8ekMa_s7a270rFCQzysluaoIzYSzudo2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش کامل راه‌اندازی V2Ray با پنل قدرتمند 3x-ui از صفر تا صد!
🎓
اخیراً با کاهش محدودیت‌های اینترنت، روش‌های باکیفیت و پایدار دوباره فعال شده‌اند. در این ویدیو،
WhiteDNS
🛡
تمام مراحل راه‌اندازی سرور شخصی و فیلترشکن اختصاصی را به زبان ساده و کاربردی آموزش می‌دهد:
🔹
سرور و دامین:
نکات کلیدی برای انتخاب سرور خارج و ثبت دامین در کلادفلر
☁️
.
🔹
نصب پنل 3x-ui:
نحوه نصب این پنل کاربردی با استفاده از هسته Xray بر روی سرور
🛠
.
🔹
ساخت Inbound:
آموزش مرحله به مرحله ساخت اولین ورودی برای فیلترشکن
🔄
.
🔹
تنظیمات کلادفلر (Cloudflare):
نحوه ثبت DNS ریکوردها و تنظیمات امنیتی ضروری
🔒
.
🔹
استفاده از آی‌پی تمیز کلادفلر (Cloudflare Clean IP):
روشی برای بهبود سرعت و دور زدن فیلترینگ با جایگذاری آی‌پی‌های تمیز
🚀
.
🔹
ساخت کاربر و استفاده از کانفیگ:
نحوه اضافه کردن کاربر و دریافت کدهای تنظیمات برای استفاده در برنامه‌هایی مثل v2rayNG
📱
.
این ویدیو یک راهنمای کامل برای کسانی است که می‌خواهند فیلترشکن اختصاصی خود را با امنیت و سرعت بالا راه‌اندازی کنند. اگر هنوز شروع نکرده‌اید، این فرصت را از دست ندهید!
✨
برای دیدن آموزش کامل، روی لینک زیر کلیک کنید:
👇
🎥
https://www.youtube.com/watch?v=vVjqNQBUGIc
🆔
@WhiteDNS</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/whitedns/1171" target="_blank">📅 09:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1170">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nTXMLMUYc9Ro4UeqxGlnKf_I4NZArdTnQOOrCVPlpD1M6eJ-Xvhg8xkae6AQqP0-SYciA_UC0uwy2hNyywQe_vvOsiHMntnRw23Y_C4JXGnwz2PZwNqESXmdbBlGFqs-NzBsqFsE8cm5WyTWo9Gc1Rlmo0jOveMCOI3j4Iw_W8QVfDVfFbEZwaV9Arxdb7KpbsJuMX1_PdZtsBnzEHEAaoGvkjvnqw_TNap_tVwzo5wFieyxYiRWZupWtW3JR1ef4uoOGD0gP_V1UdJ-CNbMpiZiL8NIeu1bp7uTxR0SxdR-COUWK7QsL2j_njNC8VhOJKd68iEP6JeVvl5u-xS1lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
اتصال رایگان و پرسرعت با پروژه Aether + پروتکل ویژه گیم Wireguard
⚡️
لینک پروژه‌ی اصلی:
https://github.com/CluvexStudio/Aether
لینک پروژه GUI من:
https://github.com/MatinSenPai/Aether-GUI
دستور نصب از ترموکس:
curl -fsSL https://raw.githubusercontent.com/CluvexStudio/aether/main/aether.sh -o aether.sh && chmod +x aether.sh && ./aether.sh install
دستور غیرفعال کردن محدودیت مصرف CPU و باتری:
termux-wake-lock
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره. حتی نیاز به اکانت کلودفلر هم نداره
😂
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/whitedns/1170" target="_blank">📅 13:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1169">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/o6s2gN3XLOCdfnHeMpthSrpnxj2xsGXbfLNBVLbHB_SO_PK6BJVCRdo5yMGlwHFtxScoLw9w3F1MQGAAzZCbBGywn3ncQ6NJU-P2ofuRIuRBQ5FULIhSVEsPoCbYD1_NGBDVmynkWBtFbtKgoGTZGcS5KrQ6YAuOsfofRA9U0Cr2o2ilbuQca2m3H3UepePvcmVjwpTPT5DCnS1xMl4G-X5QvSJhb_xXYlbmT8-_QeH0dluLCFv3kCofbRm1gCjyAkJHyddCoX-1uRh5OFfP2d1uAB8M0U84rt8KthzKStPrHvAX4bWSyUcmrMGJ8k4JZnTsTSCGiSflFpdJYoojlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر برای استفاده از سرویس‌های هوش مصنوعی (AI) مشکل دارید
🤖
این پراکسی را چک کنید
🔍
برنامه یک اپلیکیشنِ نوار منو (Menu bar)  و یک داشبورد محیط ترمینال است که به عنوان یک
مرکز کنترل و مانیتورینگ برای ایجنت‌های Claude Code
عمل می‌کند.
به طور خلاصه، این ابزار کارهای زیر را انجام می‌دهد:
نظارت یکپارچه بر ایجنت‌ها:
وضعیت تمام ایجنت‌های در حال اجرای Claude Code را در یک نگاه نشان می‌دهد؛ بنابراین دقیقا می‌دانید کدام ایجنت در حال کار است، کدام متوقف شده (خطا داده) و کدام منتظر تایید شماست.
بررسی وضعیت اینترنت و سرور:
به صورت مداوم وضعیت اتصال اینترنت شما و سرورهای Anthropic را چک می‌کند تا در صورت توقف کار ایجنت، دلیل واقعی آن (مثلاً کندی اینترنت یا مشکل خودِ Anthropic) را به شما بگوید.
حفظ لوکیشن (Location Fencing):
ایجنت‌های شما را روی یک کشور خاص قفل می‌کند. اگر VPN شما قطع شود، به جای اینکه ایجنت‌ها با خطای دسترسی (مانند خطای 403) از کار بیفتند، درخواست‌های آن‌ها را موقتاً متوقف نگه می‌دارد تا دوباره به اینترنتِ همان کشور متصل شوید و کارشان را از سر بگیرند.
ردیابی مصرف (Usage Tracking):
میزان مصرف واقعیِ محدودیت‌های اکانت شما را (با خواندن دیتای خود Claude) به طور دقیق نمایش می‌دهد.
https://ghhrmnzdh.github.io/tower/
🔗
@whitedns</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/whitedns/1169" target="_blank">📅 09:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1168">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns 15.7.2026.txt</div>
  <div class="tg-doc-extra">48.7 KB</div>
</div>
<a href="https://t.me/whitedns/1168" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/whitedns/1168" target="_blank">📅 09:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1167">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YChrJ0AC4DwWua63q39BmKIaPvc0f2lGI-nPd-YOZjbYXvwK4Xzq8h0qBqfZtPCIWT9MpDj4L5Fvloy4soLOyqAmtqbJJONry3ZI5IuTu-n6Bkfxkg7aJj7e5HI5IJSz0sQQ9Dm4942YuCPTPelw8_Afcen-cRUnjca2YPJTF__9YxCpt9nA9FaUo_Mi3JhgcZpG6kM7Ikk1PwAfqANuwoShoqA4atGYqYNQPFWF-xYXHHW44-oTmqITk5fD5SxrzvH1Djgm9FeUeHOMPE44WLmkiNigZFGw7KjRO6GoKMlbdz-80HssLdrNb4z1ogVaseqvCEZtvTU6_Hv4uTd3Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">15.7.2025
📅
فایل زیر را دانلود کنید
⬇️
1. کانفیگ‌های داخل فایل را کپی و در برنامه v2ray وارد کنید
📋
یا
2. خود فایل را از طریق گزینه import locally در برنامه v2ray وارد کنید
📥
@whitedns
🔗</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/whitedns/1167" target="_blank">📅 09:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1166">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سلام به همه
👋
یک موضوع مهم که خیلی از کاربران VPN با آن آشنا نیستند، مسئله‌ی DNS Leak یا همان نشت DNS است.
شاید برای شما هم پیش آمده باشد که VPN روشن است و آی‌پی شما تغییر کرده، اما بعضی سایت‌ها یا سرویس‌ها همچنان شما را به‌عنوان کاربر ایرانی شناسایی می‌کنند یا دسترسی‌تان را محدود می‌کنند.
DNS نشت یعنی چه؟
وقتی وارد یک سایت می‌شوید، دستگاه شما ابتدا از یک سرویس DNS می‌پرسد آدرس واقعی آن سایت چیست. اگر این درخواست به‌جای عبور از داخل VPN، از طریق اینترنت اصلی یا شرکت ارائه‌دهنده اینترنت شما ارسال شود، به آن DNS Leak می‌گویند.
به زبان ساده، با اینکه VPN روشن است، بخشی از اطلاعات اتصال واقعی شما هنوز قابل مشاهده است.
چرا مهم است؟
DNS Leak ممکن است باعث شود:
• موقعیت یا کشور واقعی شما تشخیص داده شود
• بعضی سایت‌ها همچنان دسترسی شما را محدود کنند
• حریم خصوصی شما کاهش پیدا کند
• اتصال VPN شما آن‌طور که انتظار دارید کامل و امن نباشد
چطور تست کنیم؟
1. ابتدا VPN را روشن کنید
2. وارد سایت زیر شوید:
https://ipleak.net
3. چند ثانیه صبر کنید تا نتیجه نمایش داده شود
4. بخش DNS Addresses را بررسی کنید
اگر در نتیجه نام شرکت اینترنت شما، کشور واقعی شما یا DNSهای مربوط به اینترنت اصلی‌تان نمایش داده شد، احتمالاً VPN شما DNS Leak دارد.
پیشنهاد می‌کنیم همیشه از VPNهایی استفاده کنید که نشت DNS ندارند تا هم حریم خصوصی بهتری داشته باشید و هم سرویس‌ها کمتر بتوانند موقعیت واقعی شما را تشخیص دهند.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/whitedns/1166" target="_blank">📅 08:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1165">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Whitedns-14.7.2026.txt</div>
  <div class="tg-doc-extra">241.5 KB</div>
</div>
<a href="https://t.me/whitedns/1165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1165" target="_blank">📅 18:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1164">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/kdnWmjcB462a9Qo7fnqx3eGWPLpl2uTm0d6tbAphY5Vz1OYJfikGcPjj0ZuEzEn3o5JwMDoqO7A1f2c8FZu3LovUMQYVZ8FvVZ4vQEcz5BkXYZbL0b2416iLHxe1nd51IGn4QDCUwMtr2Rge-le_Bm94klRCAFn6uLnuQEzPXjLRwDWmHWCO2fYFLOmlGHdkEPpvdgm12e89VIofV9_XY5Jmv5R5z8B-81a4jTzEbKcCQcRdVTp1Jnn5aWO14s_9NieFJQK68RmUCJ7pffdBJuOTB3xgF6nTBJc2Pkk4NfDCZcmyTloDzVnQc0S9n6vYatTFSqQUiigF7r14lPWRqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">14.7.2026
فایل زیر را دانلود کنید
⬇️
1. کانفیگ‌های داخل فایل را کپی و در برنامه v2ray وارد کنید
📋
یا
2. خود فایل را از طریق گزینه import locally در برنامه v2ray وارد کنید
📥
@whitedns
🔗</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/whitedns/1164" target="_blank">📅 18:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1163">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/TtP_4rXX37cuJTTpJjiK7_DParBrvc_E1Hm9yalm3Y64vNRqaKX2_Q7NfdY3BlNkn62CPThYBdj1oeXlk_JqFStd_acZ9Kzx5yjNnB0jhq4qWPJen-J_m3-WutajNTIHhO--hwoXyIh6a_agIBAoG3gkGmQEcCVzR94CjmmXucxiEuAKd5YkJfDLLhGPzQyjfktDL4yzsn6Hu73Rqw-AXr7cvyTHuZF_KQJ1YmeRaTaLXw0u_w8D2kdJ6XL3yJbacP_5B4TgBbl2X6_T-jkadE4ctuNu6wt5MEudJAaew_2ncGyD34H5ljtc1tPgwtiMNFzoOJtH5gjK3elr58k3xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
دستیار هوشمند کانال WhiteDNS
👉
@WhiteDnsResponder_bot
✅
جواب سریع |
✅
۲۴ ساعته |
✅
رایگان
نحوه استفاده:
۱. روی لینک بزنید
۲. Start
۳. سوالتان را بنویسید
مثال: چطور فیلترشکن نصب کنم؟
/search عبارت — جستجوی مستقیم
/contact — ارتباط با ادمین
⚠️
ربات WhiteDNS در چه زمینه‌هایی جواب می‌دهد:
✅
فیلترشکن و VPN
✅
DNS و تنظیمات اینترنت
✅
آموزش نصب اپلیکیشن‌های WhiteDNS
✅
رفع مشکلات اتصال
✅
Warp و Cloudflare
✅
تنظیمات اندروید، آیفون، ویندوز، مک
✅
سوالات مربوط به قطعی اینترنت
❌
ربات قادر به پاسخ‌گویی به سوالات غیرمرتبط با موضوعات کانال نیست.
💡
نکته: اگر جواب دقیق نگرفتید، سوالتان را طور دیگری بنویسید یا از دکمه جستجو استفاده کنید.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/whitedns/1163" target="_blank">📅 17:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1162">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">White DNS
pinned «
👆
⭕️
⭕️
⭕️
⭕️
موقت :   پرونده اتصال سریع و اسان برای افرادی که دانش و امکان درست کردن کانفیگ ندارند با چند پست بالا بسته شد   این مدل اتصال در صورت قطعی  سراسری کار نخواهد کرد
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1162" target="_blank">📅 17:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1161">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👆
⭕️
⭕️
⭕️
⭕️
موقت :
پرونده اتصال سریع و اسان برای افرادی که دانش و امکان درست کردن کانفیگ ندارند با چند پست بالا بسته شد
این مدل اتصال در صورت قطعی  سراسری کار نخواهد کرد
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/whitedns/1161" target="_blank">📅 17:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1156">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-IP-Scanner-x86_64-release.apk</div>
  <div class="tg-doc-extra">15.6 MB</div>
</div>
<a href="https://t.me/whitedns/1156" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اگر براتون سوال پیش اومده که لیست ipfronting ها را از کجا آوردیم . پاسخ خیلی ساده است
😊
👇
با استفاده از Whitedns Ip finder
🛠
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases
📂
@whitedns
📱</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/whitedns/1156" target="_blank">📅 17:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1155">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Wa-FQ86ewcQm7WLTvTKEsK-7WjRn2ERuelJkVuDseqaIeWnodJ9X2r5JJkxyfKPEouqzi0uOuip-iH2g_nNqXn20vljThMEF8YPVu7e5_8cPemweZ9DmO8UBdQaX-MvAHEEzKNiH15XfcGtehm2POw1yqXGxWk1YBlCr7O4k9s_0TSQsiJqZJn3nXr9au0I0b6akJbe1_-RtVoUAUJRZL7XO4gCUIJEmyCvo6ExJMPQemmQj5XIo3VVaAtVSrFYUP1yHruZiW-QGpLGdjo3BGnEdLfHUXwVpXxyaLWkD9mtY5H2ke_jAlcjvbR-WNNazHvGpYBxDFy4eQBYzEm-MJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/whitedns/1155" target="_blank">📅 17:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1154">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cBggGFgU1wsHcoCy4IB0Z3AnyFmM-Kn9emcC9MgvmOhliwkZLzOwxsZ073qJ4x0MUvcC5j_cmukpbjNGnuRb_lACx2kkQG6pnbpzwO4DmvmcPhdtFAJr9Xkk0oVSO8elMC6XcK27lcW3FYRkUhwplzfYLC8kXWYGmURSqJZnzVz1nuJHOXa_S72KTWHavPgIf6NgZb25wnM5oNH8Sbzv3k2UXFxQKIhhY2e6pskEX7tUSpIeDsbjWHHq94uYk6A9Nrk_3uKOHrmGK6BYF9yGkdBmpaGUoLh98kroGCn_2IQafmTke6Cmo2JR8NBJlb4jocFBh00Yk5VKoBZ4fslLCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان :
در صورتی که موفق نشدید با برنامه whitedns vpn وصل بشید
🙄
🔌
وارد قسمت advanced بشید و ای پی های زیر را دونه دونه امتحان کنید
👇
🛠
2.189.86.45
2.189.86.102
2.189.86.42
2.189.86.46
2.189.86.41
185.8.173.179
2.189.86.44
45.149.77.160
194.62.43.166
94.101.184.211
37.152.185.169
37.152.182.54
185.226.118.234
185.231.182.55
185.226.118.234
185.231.182.55
185.226.117.67
185.228.236.4
2.189.86.43
2.144.21.79
2.144.21.120
2.144.21.79
2.144.23.129
2.144.21.120</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/whitedns/1154" target="_blank">📅 17:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1152">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">White DNS
pinned «
دوستان :
👋
یک مورد کوچیک در مورد whitedns VPN بگم
📱
این اپلیکیشن بر اساس کانفیگ های متناسب با هسته x-ray یا سینگ باکس هست ، به طور مثال vless ,vmess, Trojan ,....
⚙️
اگر وصل شد حتما اول با مرورگر یک تست بگیرید
🌐
، اگر هیچی باز نشد ، دکمه refresh را بزنید…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1152" target="_blank">📅 16:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1151">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دوستان :
👋
یک مورد کوچیک در مورد whitedns VPN بگم
📱
این اپلیکیشن بر اساس کانفیگ های متناسب با هسته x-ray یا سینگ باکس هست ، به طور مثال vless ,vmess, Trojan ,....
⚙️
اگر وصل شد حتما اول با مرورگر یک تست بگیرید
🌐
، اگر هیچی باز نشد ، دکمه refresh را بزنید
🔄
اینقدر این کار را تکرار کنید تا یک کانکشن پایدار متناسب با وضعیت شما براتون پیدا بشه و هر بار تست کنید روی مرورگر
🧪
✅
تیم whitedns
👥
@whitedns
📩</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/whitedns/1151" target="_blank">📅 16:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1146">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.8-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/whitedns/1146" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اپلیکیشن Whitedns vpn 0.0.8
📱
یک برنامه بر پایه هسته‌های x-ray و singbox است که بدون نیاز به وارد کردن اطلاعات و تنها با فشردن دکمه‌های Connect یا Refresh، به راحتی یک اتصال اینترنت مناسب ایجاد می‌کند
🚀
🌐
.
ٌ
@Whitedns</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/whitedns/1146" target="_blank">📅 16:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1145">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/unm29l_oMLYchyWpADPgpTyc6erZOARdxVu8pTIcmvatQ0pPwcnqx4aBqok09-vHK7fqeA47SPQWKRHvB550giE42NkJoUmbDkX8H6Yfuu9RiMbL1ushA8J-rjNIucn5UHSrWZqjLjUKmCO0XLFb14zerlp65Wawi3YPcjTR6QPz8Y40zFPusuOoiX79S2O70FA80r88zLAeI5RhNVEq8vCM9b5s8VL8gHd6wm8yKY21mFD80mMufRJ9TMMNjEPaSGmPcjyjQUHZWyHztHHRBpQYZPzQLynjOLeHL_ny4Vm0bKglt66dBgX75NPtKE-oVD4VxbqAMa9eEwa9CTpwOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/whitedns/1145" target="_blank">📅 16:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1144">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">برای اینکه دوستان قاطی نکنند، ما دو نوع اپلیکیشن برای اتصال داریم
📱
:
۱
. اپلیکیشن بر پایه پروتکل‌های DNS محور مثل masterdns, stormdns, ...
🌐
مثل Whitedns 1.5.1
۲. اپلیکیشن بر پایه هسته‌های x-ray, singbox که پروتکل‌هایی مثل vless, vmess, ... دارند
⚙️
مثل  0.0.8 whitedns vpn</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/whitedns/1144" target="_blank">📅 16:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1136">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-poll">
<h4>📊 وضعیت اینترنت چطوره ؟</h4>
<ul>
<li>✓ ☺️مثل قبل هست  , وصلیم</li>
<li>✓ 😔اختلال داره ولی وصلیم</li>
<li>✓ 😡اختلال شدید ، به ندرت وصل میشیم</li>
</ul>
</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/whitedns/1136" target="_blank">📅 16:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1135">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🛡
مدتی پیش اپلیکیشنی برای اسکن Resolverهای متد DNS ساختیم که می‌توانید آخرین نسخه‌ی آن را از لینک زیر دانلود کنید:
https://github.com/WhiteDNS/IP-Range-Scout-Android/releases/tag/v0.1.2
اگر امکان اسکن Resolverها را ندارید، می‌توانید از ربات ما استفاده کنید:
@dns_resolvers_bot
همچنین اگر برای اولین‌بار از WhiteDNS استفاده می‌کنید، پیشنهاد می‌کنیم در گروه اصلی، تاپیک «اولین شروع» را مطالعه کنید.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/whitedns/1135" target="_blank">📅 03:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1134">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">درود به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه. با توجه به شرایط کنونی خاورمیانه، ترجیحا هم اپلیکیشن WhiteDNS را نصب/آپدیت کرده و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/whitedns/1134" target="_blank">📅 03:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1133">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">درود به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
با توجه به شرایط کنونی خاورمیانه، ترجیحا هم اپلیکیشن WhiteDNS را نصب/آپدیت کرده و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی دست یابید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/whitedns/1133" target="_blank">📅 00:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1129">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkukEXmRr0xD70Q_zSTIOHtAVdfbzJgnhUv99lWn-EmH5L-sMGeWLaNGg47fp29STII6j_qQYJkWff1ha-tj59Def41R0kNkG5zK4M5LPDc8djSoIuvjJI4EiHbg8E7Drabqm-ON0cDjViz2wmfV3QjCANKlg1xXoJp7WtjMaZ7mZ8t5FxrFqizPKPw-vvrpXan3tYUSt-geAeCJeSJZGdqdLEepBkc0GdDrkG0eNQvvgkzddWkISDxlW0_hqlDufesShOwGS-hwYM7f6340aQT4OvsX6wSqwSIXwPdnz1OACla2N-i3elGvd1qjgqc0eeE-BtFqN5MhZwR2wIkzWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
آموزش کامل TheFeed از صفر تا صد
جایگزین تلگرام برای قطعی کامل اینترنت
در این ویدیو، اپلیکیشن TheFeed را از صفر تا صد بررسی می‌کنیم؛ از اضافه‌کردن کانفیگ و پیدا کردن DNS و ریزالور سالم گرفته تا مشاهده کانال‌ها، دریافت محتوا و فعال‌سازی پیام‌رسان داخلی.
🇺🇦
تماشا آموزش در یوتیوب:
https://youtu.be/Jg0Utycz7DE
این اپ یک پلتفرم مبتنی بر DNS است که برای شبکه‌های محدود و شرایط اختلال یا قطعی اینترنت طراحی شده است. این اپلیکیشن علاوه بر دریافت محتوای کانال‌ها، امکان گفت‌وگوی امن بین کاربران را نیز فراهم می‌کند.
📦
دانلود فایل‌های اصلی TheFeed:
https://t.me/thefeedfile
⚙️
کانفیگ‌های عمومی TheFeed:
https://t.me/thefeedconfig
📢
کانال WhiteDNS:
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/whitedns/1129" target="_blank">📅 17:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1127">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1127" target="_blank">📅 14:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1126">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/uwmE8ROsBg8b8eY0LytPB08rmyjp5o8nSj3N0SHIcLs0yZ9ET9gQZ8o7YlhX7_L23GFq3kJS5NfLP12eu8bb-ZiGAkCaMhhCvmROmxx3S-hirXmFnQlE34_MG-vpxSH4egIa4pYcr6CTMq9ITcXJomCtgGCJF5n-wFZbyX4FV5n16es5UYYwI7j4FwOqVnm1US4knRujHiVd-X2cpfIO0iTRchGHRWdNaMIyMb-Q530GTnXO7ko5qLS-qexPhLYH0OiwCGxhQDiXZxf3I4Th6QomjXdV8dcKR6HXQkNh1ZH3TksGdr_-d0ScNwY1VWs9O7vUw30H8zcyCHXAgGhPUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
دستیار هوشمند کانال WhiteDNS
👉
@WhiteDnsResponder_bot
✅
جواب سریع |
✅
۲۴ ساعته |
✅
رایگان
نحوه استفاده:
۱. روی لینک بزنید
۲. Start
۳. سوالتان را بنویسید
مثال: چطور فیلترشکن نصب کنم؟
/search عبارت — جستجوی مستقیم
/contact — ارتباط با ادمین
⚠️
ربات WhiteDNS در چه زمینه‌هایی جواب می‌دهد:
✅
فیلترشکن و VPN
✅
DNS و تنظیمات اینترنت
✅
آموزش نصب اپلیکیشن‌های WhiteDNS
✅
رفع مشکلات اتصال
✅
Warp و Cloudflare
✅
تنظیمات اندروید، آیفون، ویندوز، مک
✅
سوالات مربوط به قطعی اینترنت
❌
ربات قادر به پاسخ‌گویی به سوالات غیرمرتبط با موضوعات کانال نیست.
💡
نکته: اگر جواب دقیق نگرفتید، سوالتان را طور دیگری بنویسید یا از دکمه جستجو استفاده کنید.</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/whitedns/1126" target="_blank">📅 13:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1125">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">White DNS
pinned «
⚠️
⚠️
⚠️
⚠️
اطلاعیه مهم  با بالا گرفتن تنش‌ها و با توجه به تجربه‌ای که از قطعی سراسری اینترنت داشتیم، پیشنهاد می‌کنم دوستانی که تازه به جمع ما اضافه شده‌اند، مطالب زیر را با دقت مطالعه کنند.  در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1125" target="_blank">📅 10:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1124">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🌎
آموزش کامل WhiteDNS Desktop بری ازمان قطعی اینترنت
لینک مشاهده ویدیو
https://www.youtube.com/watch?v=Mc--GlKw2wg</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/whitedns/1124" target="_blank">📅 05:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1123">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⚠️
⚠️
⚠️
⚠️
اطلاعیه مهم
با بالا گرفتن تنش‌ها و با توجه به تجربه‌ای که از قطعی سراسری اینترنت داشتیم، پیشنهاد می‌کنم دوستانی که تازه به جمع ما اضافه شده‌اند، مطالب زیر را با دقت مطالعه کنند.
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/whitedns/1123" target="_blank">📅 02:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1122">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMasterDnsVPN</strong></div>
<div class="tg-text">👋
درود،
⬅️
ایران موشک بخوره یا موشک بزنه اعضای اینجا زیاد میشن، همه چیز آروم باشه اعضای اینجا کم میشه، تعداد ممبرای این کانال شده یه چیزی مثل «شاخص پیتزای پنتاگون»
😂
⬅️
ولی من واقعا دوست ندارم، اینترنت قطع بشه و شمارو دوباره سر همون موضوع قبلی اینجا ببینم
😕
امیدوارم وضعیت اینترنت جوری درست بشه که اعضای این کانال صفر بشن، ولی مارو یادتون نره
😁
❤️
پیروز و سربلند باشید.
🤨
با تشکر فراوان،
امین محمودی
🗓
18 تیر ماه 1405</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/whitedns/1122" target="_blank">📅 02:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1120">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge
https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/whitedns/1120" target="_blank">📅 10:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1119">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🛡
معرفی CoreForge برای iOS فیلترشکن ساده و قدرتمند مخصوص آیفون  دوستان عزیز،  اپلیکیشن CoreForge برای iOS آماده تست عمومی شده و می‌تونید از طریق TestFlight نصبش کنید.
📥
نصب CoreForge از TestFlight: https://testflight.apple.com/join/u1vfEHur   CoreForge برای…</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/whitedns/1119" target="_blank">📅 10:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1118">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🛡
معرفی CoreForge برای iOS
فیلترشکن ساده و قدرتمند مخصوص آیفون
دوستان عزیز،
اپلیکیشن CoreForge برای iOS آماده تست عمومی شده و می‌تونید از طریق TestFlight نصبش کنید.
📥
نصب CoreForge از TestFlight:
https://testflight.apple.com/join/u1vfEHur
CoreForge برای شرایط سخت اینترنت طراحی شده؛ مخصوصاً زمان‌هایی که اختلال شدید داریم، خیلی از روش‌های معمول وصل نمی‌شن، یا حتی اینترنت به سمت حالت بسته و محدود می‌ره. خلاصه برای همان روزهایی که اینترنت تصمیم می‌گیرد انسانیت را ترک کند.
این اپ دو حالت اصلی دارد:
✍️
RelayForge
حالت پیشنهادی و روزمره برای استفاده عادی
مناسب وب‌گردی، اپلیکیشن‌ها، تماس، شبکه‌های اجتماعی و استفاده عمومی
✍️
DnsForge
حالت اضطراری برای زمان‌هایی که بیشتر روش‌ها بسته شده‌اند
این حالت از تونل DNS استفاده می‌کند و برای شرایط قطعی شدید یا اینترنت ملی می‌تواند کمک‌کننده باشد. سرعتش مثل VPN معمولی نیست، اما برای دسترسی اضطراری، پیام‌رسان، وب ساده و کارهای ضروری طراحی شده.
🛡
قابلیت‌های مهم CoreForge:
• مخصوص iPhone / iOS
• اتصال ساده و سریع
• پشتیبانی از کانفیگ و اشتراک
• تست و انتخاب بهترین مسیر اتصال
• حالت Full Tunnel
• حالت اضطراری DNS Tunnel
• مناسب دوران اختلال شدید و قطعی اینترنت
• طراحی شده برای استفاده ساده، حتی برای کاربران غیر فنی
📌
نکته مهم:
DnsForge آخرین راه‌حل است. یعنی اول از RelayForge استفاده کنید، اگر روش‌های معمول جواب ندادند، سراغ DnsForge برید. اینترنت خودش به اندازه کافی اذیت می‌کند، ما دیگر لازم نیست داوطلبانه سخت‌ترش کنیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/whitedns/1118" target="_blank">📅 10:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1117">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♨️
معرفی ربات جدید WhiteDNS برای راه‌اندازی و مدیریت سرور شخصی MasterDNS
♨️
ربات جدید WhiteDNS آماده استفاده است.
👉
@WhiteDNS_installer_bot   این ربات به شما کمک می‌کند بدون نیاز به درگیر شدن با مراحل پیچیده نصب، سرور شخصی MasterDNS خودتان را روی VPS راه‌اندازی…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/whitedns/1117" target="_blank">📅 06:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1116">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdIlPnG76leyKZe6EI-FrL6naC9cIMazAmrK5Qp1C3VGp0-xc6EgzpYAKqmkSRFzyqn2I--3bDCJd54jokqb1_MNur4NtLGYLf_eqs7b0VuvFBp65g0ib-S5azF1yvar7d4_tfsYUyw4GX9qeETl-V0lB-TRAECJ5njpXzkX6jh9TRw4ZFlRjnj-B9_AK5bRtssctN35htBrgmUJe3QhciZ6VjDurt-aQNaqIqlPeB1fGpcGUh-g7-Kd43YwRglpdpAwVMahyAF7_-ku02vnzw0dihHT0eREAioMPXf8XQ-MCK2fblzvLU6hlDOgx8nyyQzpscDmDYXh-t-FcVZ4ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♨️
معرفی ربات جدید WhiteDNS برای راه‌اندازی و مدیریت سرور شخصی MasterDNS
♨️
ربات جدید WhiteDNS آماده استفاده است.
👉
@WhiteDNS_installer_bot
این ربات به شما کمک می‌کند بدون نیاز به درگیر شدن با مراحل پیچیده نصب، سرور شخصی MasterDNS خودتان را روی VPS راه‌اندازی و از طریق تلگرام مدیریت کنید.
✅
نصب خودکار MasterDNS روی VPS
✅
مدیریت سرور از داخل تلگرام
✅
دریافت اطلاعات اتصال و Encryption Key
✅
بررسی وضعیت سرور
✅
ری‌استارت و مدیریت سرویس
✅
مناسب برای استفاده شخصی، دوستان و خانواده
🔐
نکات امنیتی:
اطلاعات کاربر، اطلاعات ورود به سرور، رمز عبور، کلیدها و مشخصات VPS به هیچ عنوان ذخیره یا لاگ نمی‌شود.
اطلاعات فقط در همان لحظه برای اتصال به سرور و اجرای دستور مورد نیاز استفاده می‌شود و بعد از پایان نصب یا اجرای هر دستور، توسط ربات نگهداری نمی‌شود.
بعد از انجام عملیات، اطلاعات ورود و مشخصات سرور توسط هیچ‌کس قابل مشاهده یا دسترسی نیست.
به همین دلیل، کاربران همچنان مالک کامل سرور، دامنه و تنظیمات خودشان هستند.
این ربات فروشنده سرور یا دامنه نیست.
کاربران باید:
* دامنه خودشان را تهیه کنند
* سرور خودشان را تهیه کنند
* دی‌ان‌اس های لازم را روی دامنه تنظیم کنند
هدف ما این است که راه‌اندازی و مدیریت سرور شخصی برای کاربران ساده‌تر شود؛
نه این‌که همه وابسته به چند سرور عمومی و متمرکز بمانند. ما باور داریم کاربران سرعت و پایداری بیشتری با سرورهای شخصی و غیرمتمرکز خواهند داشت.
⚠️
این ربات در اولین نسخه عمومی منتشر می‌شود و ممکن است هنوز باگ یا مشکل داشته باشد.
لطفاً مشکلات و بازخوردها را برای ما ارسال کنید تا سریع‌تر بهترش کنیم.
ویدیو آموزشی خرید سرور و دامنه و تنظیم دی‌ان‌اس به زودی داخل چنل قرار خواهد گرفت.
@WhiteDNS</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/whitedns/1116" target="_blank">📅 06:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1115">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✍️
دوستان :
آیدی ادمین که توی دیسکریپشن کانال گذاشته شده، برای حل مشکلات شخصی شما نیست. ممنون که لطف می‌کنید و درد دل‌های روزانه خودتون رو برای ما می‌فرستید، ولی متاسفانه قادر نیستیم پاسخگو باشیم چون تعداد پیام‌ها خیلی خیلی زیاد هست.
اینکه موبایل شما و یا کامپیوتر شما دچار مشکل شده، یا اینترنت شما کار نمی‌کنه، شرکت تامین‌کننده اینترنت شما کلاه سرتون  می‌گذاره، و یا اپلیکیشن‌هایی که ما گذاشتیم دچار فلان مشکل هست و غیره رو برای آی‌دی ادمین نفرستید، توی گروه مرتبط با خودش مطرح کنید.
آیدی ادمین فقط و فقط برای مواردی هست که شما قادر نیستید توی گروه های عمومی ما براش پاسخی پیدا کنید (که تقریبا غیر ممکن است )و یا گزارش و یا یک مورد خیلی فوری را میخواهید به دست تیم ما برسونید
در ضمن بازم تاکید می‌کنیم برای اون دسته از دوستان طلبکار و بی ادب  ، شما حقوق ما را نمی‌دید و ما هم از جایی بودجه نمی‌گیریم ، ما بدهی به شما نداریم ، بی ادبی شما جوابش فقط بلاک شدن و حذف شما از کانال و گروه های ماست ،
از امروز مواردی غیر مرتبط به هیچ عنوان پاسخ داده نمیشود
سپاس
❤️
تیم whitedns</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/whitedns/1115" target="_blank">📅 10:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1114">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا
اگر داخل پنل های نهان و bpb یا هر فیلترشکنی که دارید مشکل باز شدن یه سری اپلیکیشن ها رو دارید(تلگرام،یوتوب و...) طبق تنظیمات زیر داخل هر کلاینت برید این تنظیمات رو داره:
Dns:
💎
9.9.9.12
8.26.56.26
8.8.8.8
8.8.4.4
208.67.220.220
208.67.222.222
Fragment:
✅
Google.com
Length:10-20
Interval:10-20
Packets:1-1
💡
نکته:قسمت فرگمنت بیشتر برای مشکل آپلود یا باز نشدن اپ هاست لذومی نیست حتما روشن کنید.
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/whitedns/1114" target="_blank">📅 04:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1113">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/nlfJN0FIJXFjzMmkfnhprnYL2ByPbJqUEEls27Y5SQppuJ2rW-OUFRy2fw7fNCLgk2gWfIJtHjbbIJCh0d1Q17lRHXFRbxZhdlh1oaztf_2qN2HO1CCvlkeURQc7bXogLAoWYcobQxXoAaBafSBdn8mRNu28U5yg9DJpwgTOOVcx37CNtUlQZWZy6FbPD9gdr98D6KJ7ll8nX85LPAizmS0aQ5YvI8odDBoTY7-wkgPfe9jjYzPppxWSgaZi6FnoAv9BY-gbzGrr0SMoXbCBW4TYWsBr7bVgIKq1DJvpSRx4ULnSmFpJJ6wjl4o_26aRVFdWKHPgcC1fdPnSj8Vj1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/whitedns/1113" target="_blank">📅 20:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1110">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhitednsProxyProfiler-Android-v1.0.7.apk</div>
  <div class="tg-doc-extra">55.4 MB</div>
</div>
<a href="https://t.me/whitedns/1110" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پروفایلر پروکسی WhiteDNS نسخه ۱.۰.۷
🛠
پروفایلر پروکسی WhiteDNS یک ابزار تشخیصی برای ویندوز و اندروید است که بهترین ترکیب‌های پروتکل پروکسی/VPN را در یک شبکه پیدا می‌کند. این ابزار می‌تواند هم بررسی‌های محلی بدون VPS و هم تأییدات عمیق‌تر مبتنی بر VPS را اجرا کند.
🌐
ویژگی‌های اصلی
اسکن شبکه محلی:
آزمایش سریع بدون نیاز به اعتبارنامه‌های VPS.
🏠
اسکن VPS:
تأیید از راه دور عمیق‌تر با استفاده از اعتبارنامه‌های VPS شما.
🖥
تست پروتکل‌های VLESS، VMess، Trojan، Shadowsocks، WireGuard، Hysteria و HTTP.
🚀
پشتیبانی از انتقال‌های TCP/RAW، WebSocket، gRPC، XHTTP، HTTPUpgrade و mKCP.
🔄
پشتیبانی از ترکیب‌های TLS، REALITY و بدون امنیت (در صورت معتبر بودن).
🔒
تشخیص دسترسی‌پذیری، فیلترینگ، پورت‌های مسدود شده، مشکلات SNI/TLS و رفتارهای شبیه DPI.
🔍
نمایش نتایج تشخیصی دقیق و اطمینان از شواهد محلی.
📊
کمک به شناسایی ترکیب‌های ایمن‌تر پروتکل، پورت، انتقال و امنیت.
🛡
نحوه استفاده
برای یک آزمایش سریع بدون VPS، گزینه
اسکن شبکه محلی
را انتخاب کنید.
⚡️
از
تنظیمات پیشرفته
برای تست پروتکل‌ها، پورت‌ها، مقادیر SNI، انتقال‌ها و انواع امنیتی بیشتر استفاده کنید.
⚙️
وقتی به شواهد قوی‌تر سمت سرور نیاز دارید، گزینه
اسکن VPS
را انتخاب کنید.
🌍
آی‌پی VPS، پورت SSH، نام کاربری و رمز عبور یا کلید SSH خود را وارد کنید.
🔑
اسکن را شروع کنید و پروفایل پیشنهادی کارآمد یا نتایج تشخیصی را بررسی کنید.
✅
نکته مهم
اسکن محلی نشان می‌دهد که شبکه فعلی شما به چه مواردی دسترسی دارد. اسکن VPS شواهد قوی‌تری ارائه می‌دهد زیرا هم سمت کلاینت و هم آنچه واقعاً به VPS می‌رسد را بررسی می‌کند.
🧐
نسخه:
۱.۰.۷
🏷
@WhiteDNS</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/whitedns/1110" target="_blank">📅 19:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1109">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سلام
❤️
توی این آموزش، تمام بخش‌های برنامه V2Ray را از مبتدی تا حرفه‌ای به‌صورت کامل بررسی کردیم؛ از اضافه کردن کانفیگ و Subscription گرفته تا تنظیمات پیشرفته، Routing، آپدیت برنامه و حالت‌های مختلف Tunnel.
🇺🇦
لینک آموزش در یوتیوب:
https://youtu.be/i1-XenoSalk?si=5jbQK3BrGAe4ctsu
اگر موضوع یا نرم‌افزار دیگری هست که دوست دارید آموزش کاملش را ببینید، داخل کامنت‌های یوتیوب یا گروه تلگرام پیشنهاد بدید تا برای آن هم آموزش تهیه کنیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/whitedns/1109" target="_blank">📅 18:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1108">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDr Alan(Dr . A)</strong></div>
<div class="tg-text">چجوری کانفیگ رایگان بسازم بدون دردسر؟
🤔
همه چیز با یک کلیک در WhiteDNS BPB
🚀
مرحله 1:
اول از همه برنامه رو نصب کنید و وارد برنامه بشید
📲
مرحله 2:
وقتی وارد برنامه شدید دکمه Connect CloudFlare رو بزنید
☁️
مرحله 3:
وقتی به مرورگر هدایت شدید، اطلاعات حساب Cloudflare خود را وارد کنید
🔐
مرحله 4:
بعد از وارد کردن اطلاعات به یک صفحه منتقل میشید که از شما میخواد اجازه استفاده WhiteDNS BPB رو از اکانت کلادفلر خودتون رو بدید. برای این کار به پایین صفحه اسکرول کنید و دکمه آبی رنگ Authorize رو بزنید
✅
مرحله 5:
دو حالت وجود دارد. یا شما میخواد یک برنامه رو انتخاب کنید که باید برنامه WhiteDNS BPB رو انتخاب کنید. یا به یک صفحه دیگه منتقل میشید در این حالت به برنامه WhiteDNS BPB برگردید و دکمه I Finished رو بزنید
🏁
﻿
مرحله 6:
بعد از اتصال حساب کلادفلر شما به برنامه، به تب(بخش) Bpb Deployment برید و دکمه eCreat Panel رو بزنید
⚙️
مرحله 7:
به یک صفحه منتقل میشید که میتونید تغییرش ندید و بزارید در حالت پیش فرض بمونه و دکمه آبی رنگ Create Panel رو بزنید
مرحله 8:
بعد از کمی صبر پنل شما با موفقیت ساخته میشه. دکمه Subscriptions رو بزنید و اولین ساب رو کپی کنید
📋
مرحله 9:
میتونید اون لینک ساب رو در برنامه های v2ray / v2box ... وارد کنید یا از داخل تب VPN در برنامه WhiteDNS BPB لینک رو وارد کنید و همونجا به کانفیگا وصل بشید
🌐
⚠️
توجه:
به هیچ وجه از ایمیل های فیک و رندوم استفاده نکنید
🚫
حتما باید اکانت کلادفلر شما Verify شده باشه در غیر این صورت با خطا مواجه میشید
❌
اگر از فیلترشکن استفاده می‌کنید، توجه داشته باشید که باید ایپی شما ثابت
باشه
🛡️
لینک دانلود نرم افزار:
https://t.me/whitedns/1018
@WhiteDNS
با تشکر
🙏</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/whitedns/1108" target="_blank">📅 04:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1106">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy
فیلترشکن قوی و پرسرعت برای تلگرام
https://www.youtube.com/watch?v=pyvB6VSPhwg
@WhiteDNS</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/whitedns/1106" target="_blank">📅 19:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1105">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود رفقا یکی از بچها زحمت کشید یه ویدیو کوتاه واسه این ابزار درست کن با کمی بهینه و میانبر واسه دریافت توکن که میتونید ببینید و واسه خودتون و خانوادتون فیلترشکن رایگان بسازید
✅
ویدیو یوتیوب:
📹
https://www.youtube.com/watch?v=e8FNffowfYo
بات دکی:
👑
@itsyebekhebot
نوا پروکسی دریافت توکن:
✅
https://novaproxy.online/install
داشبورد کلودفلر:
💎
https://dash.cloudflare.com
ایمیل فیک:
⚡️
@TempMail_org_bot
خلاصه: داخل ویدیو نحوه دریافت توکن آسون تر شده و این که یه سری بهینه سازی هم داخل ویدیو هست
❗️
@yebekhe
👑
@mehdisedighinasab
💎
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/whitedns/1105" target="_blank">📅 16:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1102">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">↗️
تعداد کانکشن های موفق WhiteDNS VPN در ۲ هفته به ۱۰۰هزار رسیده
.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/whitedns/1102" target="_blank">📅 15:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1101">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGq-rVStkNOl82_5llTCTPANLK9Vhcs1VPSzdCszEj7R8k3VzWDOqR33Tx2BKDBMYD9hHHo6Py2AVVU4afsfxorYFIza5UUfXumywMQaPFY3FfKb3GNA-XIMHx6e6EhFAO7wfxkyVlsZ_U6pcIydsQzIzoog1P-iHusQGaZMBxzJ6Nuoa88i7dnngxzNweYwKppiToe-U7fWzVGuJmIjXixBJyjEAyTtL-B-ia_DG14rMHaPzZDgmj01nL0SYxrlQtYSDxtU-Q5CVdAtxJppnFJXoZoYwn3vSDQUIFfL96TCjWVQ9_1wOYplI2hKHrOI6Zycc9yzMepKJ_evWV3pJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📇
دوستانی که امکان اسکن ندارند، می‌توانند از تاپیک «IP تمیز» در گروه استفاده کنند. دوستان دیگر IPهای تمیز را آنجا به اشتراک گذاشته‌اند و می‌توانید از همان‌ها استفاده کنید.
لینک گروه
https://t.me/+-Uc2AHI2d8Q2MzA0
آموزش استفاده از IP سفید
https://youtu.be/N5hKuWXp37w?t=1092&si=mdL0Q8Q9H039IAiL</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/whitedns/1101" target="_blank">📅 08:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1100">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=vrG1Dq_stN87WpsjBDjhTOAxhYKZJSnOVnCQccjCD0hx0HfK0qsG4gQCkRN21ZobFdVwuqq-6FdENsixBRfAyV5s6ut8RTSwe_3DaKjx5aVWqEarBZmxqpfExsQF3re5jx6ZclMcuQ3n7-fZDzVMAa5EYHDhy25fGW4zayMTQwzlxegSv484qhR5WPpiq5m3S2Cbpldvr1cWKOqRW502KhnrC1-i8kWHD1D-Brlko17-HznKwok7pyp2gTWuPKs3BKJuklXkScZihOcmTOU2vGqVq8titvrXzrNUQKR3R18kTocwZyb6rIorjty-darkZ8qjfuiZS_asIgON2JoHcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=vrG1Dq_stN87WpsjBDjhTOAxhYKZJSnOVnCQccjCD0hx0HfK0qsG4gQCkRN21ZobFdVwuqq-6FdENsixBRfAyV5s6ut8RTSwe_3DaKjx5aVWqEarBZmxqpfExsQF3re5jx6ZclMcuQ3n7-fZDzVMAa5EYHDhy25fGW4zayMTQwzlxegSv484qhR5WPpiq5m3S2Cbpldvr1cWKOqRW502KhnrC1-i8kWHD1D-Brlko17-HznKwok7pyp2gTWuPKs3BKJuklXkScZihOcmTOU2vGqVq8titvrXzrNUQKR3R18kTocwZyb6rIorjty-darkZ8qjfuiZS_asIgON2JoHcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">https://www.youtube.com/watch?v=Z069VNFAgAc
ایجاد بی‌نهایت آدرس ایمیل با یک دامنه روی کلودفلر
📧
آیا می‌دانستید می‌توانید با استفاده از قابلیت Email Routing در ، بی‌نهایت ایمیل شخصی‌سازی‌شده برای دامنه خود بسازید و همه آن‌ها را در یک صندوق دریافت مدیریت کنید؟
در این ویدیو، نحوه راه‌اندازی این سیستم کاربردی را یاد می‌گیرید که برای مدیریت بهتر ایمیل‌ها و جلوگیری از اسپم عالی است.
@whitedns</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/whitedns/1100" target="_blank">📅 17:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1099">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🛡
ویدیو آموزش استفاده از WhiteDNS Scanner
+
WhiteDNS VPN
https://youtu.be/N5hKuWXp37w
با استفاده از اسکنر WhiteDNS می‌تونید آی‌پی‌های تمیز و مناسب Cloudflare رو پیدا کنید، تست سرعت بگیرید، خروجی دقیق بگیرید و بعد از آی‌پی‌های سالم برای اتصال بهتر داخل اپ WhiteDNS VPN استفاده کنید.
در این آموزش یاد می‌گیرید:
- دانلود و نصب WhiteDNS Scanner
- اسکن IP و CIDR
- پیدا کردن IPهای تمیز Cloudflare
- تست سرعت و کیفیت آی‌پی‌ها
- استفاده از خروجی اسکنر
- دانلود و راه‌اندازی WhiteDNS VPN
- اتصال رایگان با گوشی موبایل
- انتخاب IP مناسب برای اتصال پایدارتر
📹
ویدیو
https://youtu.be/N5hKuWXp37w
📥
دانلود WhiteDNS Scanner
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3.4
📱
دانلود اپ WhiteDNS VPN
https://t.me/whitedns/1072
📢
کانال تلگرام WhiteDNS
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/whitedns/1099" target="_blank">📅 15:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1098">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔭
برای دوستانی که می‌خوان سرور شخصی خودشون رو راه‌اندازی کنن، کیفیت VPSهای این سایت واقعاً خوبه:
https://yottasrc.com
چند نکته مهم:
* شماره و کشور ایران رو قبول می‌کنه
* پرداخت با ارز دیجیتال داره، روی شبکه‌های مختلف
* آی‌پی‌های سرورها کیفیت خیلی خوبی دارن
* پورت ۱۰ گیگابیت ارائه می‌ده، که برای سرعت و پایداری واقعاً مهمه
* لوکیشن‌های متنوعی هم داره
برای ساخت سرور شخصی، VPN، DNS یا تست‌های فنی، گزینه‌ی خیلی مناسبیه.
منبع
@WhiteDNS</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/whitedns/1098" target="_blank">📅 11:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1097">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/whitedns/1097" target="_blank">📅 14:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1096">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSJ_j4QjKTMkf7Ijrj_L21jbdAU7SVapvU0VCsqhorKdTDrpKaQwZuqGp3AdAHoKN1MYAKf7o4Dy3prMxJb2Ozcfosj-NXQZOWIWK3MVvXcYeS8Pu2FX72bb12kAte8qn-OD9U4-AKkEP971GMEYKWBC3I3BmEXcmVm6JVpn05y_7weAL-23QYPHmYmFdikSScxqFLjISEITq-yYivC2dBWUNCHqW2HYlVaCK0xiBlPfN04xOPcO-0veG809YHew1buM1KiCiudXyfN9x4YBJj0A_mbrm4A11-TX7itgbg0c-S2jlxxGn_rBmw5AXKjeQ98cJSHwYOjwmNwrnIgRBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/whitedns/1096" target="_blank">📅 10:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1095">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/whitedns/1095" target="_blank">📅 05:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1094">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/whitedns/1094" target="_blank">📅 05:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1093">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.
نتیجه این تست، هر ۳۰دقیقه داخل این مخزن گیتهاب برای سرویس های متفاوت قابل دسترسی خواهد بود.
🌎
ساب مناسب اپ های V2Ray, V2rayNG & ...
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
🌎
ساب مناسب Clash Mi, Clash Party
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
🍏
IOS App
: Clash Mi, Karing
👾
Android App
: Clash Party, Karing
👍
Mac App
: Clash Party
📱
Windows App
: Clash Party
📱
Linux App
: Clash Party
@WhiteDNS</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/whitedns/1093" target="_blank">📅 05:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1088">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS Desktop  منتشر شد
👆
👆
👆
👆</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/whitedns/1088" target="_blank">📅 11:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1082">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta6-linux-amd64.deb</div>
  <div class="tg-doc-extra">19.1 MB</div>
</div>
<a href="https://t.me/whitedns/1082" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/whitedns/1082" target="_blank">📅 11:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1081">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cu6zk8-CR3-mdUPx7v06MGaVk9YmWH_cpajTLU-1W9yQer73r_vp6Rx_9C-uXhz1bDuAWny0q8gki5dTI2hMEFavL4DO-1brKzqIm4HBHQAM8mofC5wO4Ep8D47r6jVcL4uM6zexqdR-k-UoNkz79mbjhetxnf-Lb3QOx1ToXpde4iiMzkfBBl5m8nTTXqwYIzTEHr8X2ormh9TcGuRmU-We1zDp2kQ68Q_CiRtg3xNW376uP6Wbou3B-hYIQSVfd2_zYhgPS18RZFKmXqKgYApfkGbtOmR35G7uuk3t9scOchr_UElRaUMATzuAy_tmszSvialHqDTB1FL3UYO02w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS Desktop 1.0.0-beta6 منتشر شد
در این نسخه، ماژول جدید WhiteDNS VPN به WhiteDNS Desktop اضافه
شده.
امکانات این نسخه:
• اضافه شدن WhiteDNS VPN به اپ دستکتاپ
•  انتخاب هوشمند بهترین سرور
•  نمایش کشور و وضعیت سرورها
•  اتصال بدون نیاز به تنظیمات پیچیده
•  تجربه کاربری ساده و روان</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/whitedns/1081" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1080">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⚠️
⚠️
⚠️
⚠️
اطلاعیه مهم
با بالا گرفتن تنش‌ها و با توجه به تجربه‌ای که از قطعی سراسری اینترنت داشتیم، پیشنهاد می‌کنم دوستانی که تازه به جمع ما اضافه شده‌اند، مطالب زیر را با دقت مطالعه کنند.
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/whitedns/1080" target="_blank">📅 04:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1079">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIh8nQ0Fio2nKK1NLN3-ycwvBFLgQ2b62ytEnBCWtLihVSCxl5m4flyQyPpp5mLX2vBcLuh5aV1hWof5-xs_YQTd41rsniT1alaY_XPKEfPTgptCBbf51_Apu3IQAZRCvsVpX3RiLVAu1H796poHzO4x03mhyV7A7V6HVA5FKzT2vbHJVcezSz_rXHp9tFKU5-eSBicjNZkn0Csl8Sx7BslqwSA7EFHJeQoQHaOwDoe7jnmjlzZVAYCSnY31dgh6rQBsAsrVoKTM9eYrWV7A1JFM5KNlltgSkfb7vEPqzLPcOd6S1vJdKRbsSoxT7lv5Kz5hcIL28ZO07o8tvrULSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
ورژن جدید WhiteDNS Desktop تقریبا آماده شده
در این ورژن همان وی‌پی‌ان داخل اپ اندروید
برای ویندوز، مک و لینوکس قابل دسترسی خواهد بود.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/whitedns/1079" target="_blank">📅 16:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1077">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚀
اسکنر WhiteDNS  اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن. https://github.com/WhiteDNS/WhiteDNS…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/whitedns/1077" target="_blank">📅 03:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1076">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyCvSwpzaAyIGhjvBfb7XqSL0mb1IcjEGUZHAb2tyfoUcQFGCP5YtlBu_rzRBPAAca6934ZBul8InGYwrOkILTCT3-fpgd3F_PGZ9nyG1UU--crkl8s3FpJVxkj6pLzO9Gl8w2GygzCeRgGdooDPlVMe7LKRN9PtNV7SSB2ynksUAWfRkXqLJrbBI2X7Erx3x3zNT5kILgJskf8M5A1W9dUs92vCGt6UMRMiFi6Qb9uM65dcireaBPeX1kUbb75rD2HkCiJjiJtvZFMnYpkj2sjKH8OowLg96iFTbVvhIW5zqO5lSNHmiia6g8qI2aGwmktf2_s1rcL89P1Lk5bKXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
اسکنر WhiteDNS
اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ
مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن.
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3desktop
📱
نسخه اندروید
سبک، بهینه‌شده برای موبایل و قابل استفاده روی گوشی، با امکانات کاربردی نسخه دسکتاپ.
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3.4
⛏
قابلیت‌ها:
• لیست آماده از ASNهای ایران و ASNهای معروف داخل اپ
• امکان وارد کردن لیست آی‌پی دلخواه
• Health Check برای توقف خودکار اسکن در زمان ناپایداری اینترنت و ادامه بعد از پایدار شدن اتصال
• ادیت یک کانفیگ و ساخت تعداد زیادی کانفیگ روی آی‌پی‌های تمیز با چند کلیک
• استخراج آی‌پی از داخل کانفیگ‌ها
• تست سرعت دانلود و آپلود آی‌پی‌های اسکن‌شده
• انتخاب پورت از لیست آماده یا وارد کردن پورت دلخواه
• لاگ پیشرفته برای بررسی لحظه‌ای روند اسکن
• خروجی کامل و دقیق از نتایج اسکن
متدهای اسکن:
⭐️
IP Scan
برای پیدا کردن آی‌پی‌های تمیز از دیتاسنترهای داخلی و خارجی و استفاده در کانفیگ‌ها.
⭐️
HTTP Scan
برای پیدا کردن آی‌پی‌هایی که امکان استفاده به عنوان پروکسی HTTP رو دارن.
⭐️
SOCKS5 Scan
برای شناسایی آی‌پی‌هایی که می‌تونن به عنوان پروکسی SOCKS5 استفاده بشن.
⭐️
SNI Scanner
برای اسکن دامنه‌های موردنظر روی لیست آی‌پی‌ها و پیدا کردن آی‌پی‌های مناسب برای SNI Spoofing.
⭐️
Speed Test
برای تست سرعت دانلود، آپلود و Packet Loss آی‌پی‌های اسکن‌شده، همراه با رتبه‌بندی خودکار.
این ابزار برای کاربرهایی ساخته شده که می‌خوان با دقت بیشتری آی‌پی‌ها رو بررسی کنن، خروجی تمیزتر بگیرن و زمان کمتری برای تست دستی تلف کنن.</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/whitedns/1076" target="_blank">📅 03:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1074">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">White DNS
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1074" target="_blank">📅 17:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1073">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M98n6JJSGNRi3xwwiLfvX_2dkkJjANM4rerZtQpF4hfN7vGNEnJ1dberHvWGNjpH2GwI4TbN_d_xWjphzrZG8bkUSZ3FWdKtm8rNhsN_H9tMulhhuU_BrNv1015qP92lfIYt9p53I1H4ghOU6mnBRsgWccPEkTvyYBz1UV7tfgbaVLRTSpuoVC7MYTu0uoUJBCsHttxBpfVyAV-u1DCruaZZacYcz7NZBGTsxYsg-vVlfx7Gj35yQTEod73Sde9Oz0CxDEG0YDU7lVbkSqHtbfpAsRQtlNitp7ZOr0bDQBer_quKmPdn8RM0U5Gt6YnIe5JdDRsqfFPBJcd9-Fqszg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا شد
😎
۷۰۰ اتصال موفق در ۳۰دقیقه گذشته.
ممنون از همه دوستان که کمک ما تست کردند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/whitedns/1073" target="_blank">📅 16:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1068">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.8-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/whitedns/1068" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⭐
نسخه جدید WhiteDNS VPN 0.0.8 منتشر شد
میدونم آپدیت کردن این سرعت یکم برای هم شما هم من سخته. اما تونستم دقیق مورد رو پیدا کنم و فیکسش کن
ی
م.
ممنون از تمام دوستانی که نسخه‌های قبلی رو تست کردند و مشکلات رو گزارش دادند.
⛏
در این نسخه، مشکل لود شدن بعضی سرویس‌ها مثل یوتیوب و اینستاگرام برطرف شده و اتصال‌ها پایدارتر شده‌اند.
✍️
از همه شما بابت اختلال‌ها و مشکلاتی که در اتصال داشتیم صمیمانه عذرخواهی می‌کنیم. ممنون که همراه ما هستید و با گزارش‌هاتون کمک می‌کنید WhiteDNS بهتر بشه.
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/whitedns/1068" target="_blank">📅 15:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1062">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS VPN 0.0.6 منتشر شد
👆</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/whitedns/1062" target="_blank">📅 13:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1057">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.6-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/whitedns/1057" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/whitedns/1057" target="_blank">📅 12:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1056">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOrLOPYIwimJEPq3x88EfNOB5DxLeqUwfXW3B17S0uRaEoaBbv9jHjpgxjc9qkH2FmiTUYLXemlrNKtIQIPHKJgA7txAYNQ2j4OKLEWMQOWn075_qmhMKGFHn9d-MGVFa9qUVS7mtUkmYMMCf4b0UDUlp17W6yenL2OArb1wt-b3bI4lCiP8xZhONZpD6WaROzxL1JWbXai97p55gm9NltJ2dmlkq2z_81vWh8BFuI1jYzS6McoBG3eED2pXVYEpjDjePFix2Er9HfWcEH5MQuCBru3-rmFLugQngpYv-9NYXZ7SBCm8bvZ9Ne6XG6tT9cpofNpdHsOZrCzjRdd8zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS VPN 0.0.6 منتشر شد
با مشکلاتی که دیروز برامون پیش اومد، فرصت این رو پیدا کردیم همزمان با درست کردن مشکل کردن اسکنر  ها، روی سرعت اتصال هارو هم بهتر کنیم و تا شاید کاربر های بیشتری بتونن بدوم IP Fronting وصل بشن.
🌈
در این ورژن، سرعت اتصال شما با اختلاف زیادی بهتر شده
🌈
اپ پایدار تر از همیشه هستش.
🌈
اپ از نظر ظاهری بهتر شده.
🌈
مشکل اتصال و نمایش کشور اشتباه حل شده.
نتیجه اتصال و سرعت خودتون رو زیر همین
پست بهمون بگید
ممنون از همراهی شما
@WhiteDNS</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/whitedns/1056" target="_blank">📅 12:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1055">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🛡
سلام به همه دوستان عزیز
بابت اختلالی که امروز توی سرویس WhiteDNS VPN پیش اومد واقعاً عذرخواهی می‌کنیم.
متأسفانه یه مشکل فنی برای سرورها ایجاد شده بود که باعث شد بعضی از اتصال‌ها درست کار نکنن. خوشبختانه مشکل برطرف شده و سرورها دوباره در دسترس هستن.
برای اینکه لیست جدید سرورها داخل اپ براتون آپدیت بشه، یکی از این کارها رو انجام بدید:
• یک‌بار دیتای اپ WhiteDNS VPN رو پاک کنید.
• یا اپ رو حذف و دوباره نصب کنید.
• یا حداکثر تا ۳ ساعت صبر کنید تا اپ خودش تنظیمات جدید رو از سرور بگیره.
شاید سرعت کانکت شدن کمی پایینتر آمده باشد اما به زودی اون مورد هم حل میکنیم.
ممنون از صبوری و همراهی‌تون
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/whitedns/1055" target="_blank">📅 08:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1054">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🌎
سلام به همراه عزیز WhiteDNS
تغییرات جدیدی روی سرویس WhiteDNS VPN اعمال شده که از همین حالا در دسترس هستند:
✅
تمام کانکشن‌ها با دقت بالا از نظر DNS Leak بررسی و اعتبارسنجی می‌شوند.
✅
قوانین جدید پراکسی اضافه شده تا سایت‌های داخلی ایران به صورت مستقیم باز شوند و دیگر نیازی نباشد برای دسترسی به آن‌ها VPN را قطع کنید.
✅
تبلیغات از بسیاری از وب‌سایت‌ها حذف می‌شوند تا تجربه بهتری داشته باشید.
برای استفاده از این قابلیت‌ها نیازی به آپدیت اپلیکیشن نیست. کافی است یکی از کارهای زیر را انجام دهید:
• یک‌بار دیتای اپ WhiteDNS VPN را پاک کنید.
• یا اپلیکیشن را مجدداً نصب کنید.
• یا حداکثر تا ۳ ساعت صبر کنید تا تنظیمات جدید به صورت خودکار از سرور دریافت شوند.
ممنون از همگی.
🙏
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/whitedns/1054" target="_blank">📅 13:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1052">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یکی از اولین آدم‌هایی که از این پروژه حمایت کرد،
ویکی‌تجربه
بود. زمانی که اینجا فقط حدود ۱۰۰۰ نفر بودیم.
شاید خودشون هیچ‌وقت ندونن، ولی با به اشتراک گذاشتن پروژه، یکی از کسایی بودن که به ما انگیزه دادن ادامه بدم. بعضی وقتا یه حمایت کوچیک، بیشتر از چیزی که فکر می‌کنیم روی مسیر یه نفر تاثیر می‌ذاره.
خیلی وقته دیگه خبری ازشون نیست. حتی دیدم دامنه سایتشون هم تمدید نشده.
کار درست انجام دادن توی ایران سخته. درست موندن و باوجدان زندگی کردن هم سخت‌تر.
من حتی این عزیز رو از نزدیک نمی‌شناسم و اسم واقعیشون رو هم نمی‌دونم، ولی همیشه قدردان لطفشون بودم.
امیدوارم هرجا هستن، سالم باشن و حال دلشون خوب باشه.
🥲</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/whitedns/1052" target="_blank">📅 16:31 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
