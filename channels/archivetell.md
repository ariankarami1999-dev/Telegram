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
<img src="https://cdn4.telesco.pe/file/UXB_Fyb6h_dq83q3SUJ-aXyAj0tspuXqTHGpgXmdRR6WRCqrU2Vpg6pgFy5tywK4k_DJYe0oTBGZA7WWNOa5seGXWxdkDHwc13tX9pbH8QNEHuUHFuPcSbWnPrL6GyuX6MR_AUa3vDtmiqKdGcJXi3cg2uPu_gIXNSDpRk7RJ7ZcfD8TQXFLthIe8fj08eYmT5I3G7tAbHVh-EOgtXsA6wG3CREPfhT4Spwk_WjyIxiYbKuHYd6UKPmDuvDbX4M2afrunN1ySgEVMTdZT-AXBbFwlBd1nrSw_Y8zbqX-ucrfIDBIImKUEiCvqUR5hyiyI7CI307AS7osUXvCFAFw0A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 23:53:56</div>
<hr>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqmH-9C509CHVIPz6R3f-_pYc59iHAJN5KkyYsORn7EtcpCvFllL0FlroCLxtVVr6h3TZdldG-gK80DI-CLcyFOhCeixw-AOAVMQ15rT40bV0Uw4u51tXRwxDC7acP2O6wLoEyM6E7V2QBTwdc3gESbaX-RetvAAH-dubbxUU4IuMASU8PMQNwtFzDKDbZV7oPzZ4MFyhfSJaCyAXg9WQoZtX4AVs9gaqTwecc5Y5K0v2p6UwcBPBHECmhmkVgQZ-_x3QvRpdbll42ITCxqElMtIf5VJwt8PbdHCIhp9RB_XxJ7xSRyCJGr0Cbygi_gBgOxYUsX3Zq2yqPHuCX6lXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
DeepSeek Harness Studio
رابط گرافیکی ویندوزی برای DeepSeek Harness
🤔
بدون نیاز به ترمینال یا Node.js!
🤔
نصب خودکار در اولین اجرا
🤔
وب UI رسمی داخل برنامه
🤔
پشتیبانی از پروکسی داخلی
💎
https://github.com/ScannerVpn/DeepSeekHarnessGui
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 683 · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VUiLBv_AkdtpzhUpl_7KMgP8gXI5vBC0TYGCpaRV9f-3KxMenCXYTlg4C15_JE2i2tzCFwack9X3PX8uXDK3lOWz1idgJY3NSliSHU4B2g8kdA3MkKVVBuUmkJzsG8TYutaDORDqc5QuG8ndjQsSeXZrMssqlYY9ZgbGVNnB0GRQjKm9byaaITKNy_wUHbjRUfvJUSXv6KhOarrInImsPwPKffbeBz-oNZs29zxj8b18TbnjL57aVcTsVSDLv4OjnCBGxQ4zDGUr0WDvGAGtS0_NfppTeFpjH6Fi5kHLnh6bUCwlQClyRar0uyd9ixSA9wfg184IHohphcgscZj4wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQeb7O8DO8vORoFr3JuK8cRb-VFBVAOg6i9vo89IKkwTc05hWG7E-_KneI93Y59LkjdUMQGgC1S52z4YwiqN3cWTO7Fyu_jYKtzBfuzI_CG9f5KDIeUCEEunE6Bb8JsQmJ4-tcJfb3GBsSSDylZJkxkLb6YuVTV4Sd_Zb8xFUERujx0O7GDSA8dXUu62T3r9Xz9N5HMD08Hvt8Mch8svZwrqcEDVrIwobvgKWw4yzJYqrY8dHOXgi1AZJpQN8nfWNpTvPzr1iV6HGHbdTv_xjmT2NA2lHYYygWTTx0yp7vqMN2iCjjn3rWk1q6l3iptp211IDwR982kfMvU0xEW2fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NNvQdgTKYzfeH3Mq8Bsky7sCzUniXP73ybg_xd2NWJ-7Fwwita2p7SxAqBEn7OUYsYDepurEeUP_b3MY24dyObztYRQBtBreAzafLwCD9MPkfzj7jh9tnH4vu_5SAgdL9Doc1rnsbHeEaIRXyn4JG5wW8pVNrH-MhwXaRTa6oc0sfEXoYtx-hGf_Yl0BhW1ixbZob2YfVSgkOClQ8afSZe25m9RfZOECRCZdM0jc_WixyKz3fkiSzsA_oDH2RIRS15v7y9bZZWSiqdrk-tNtNR4A752Dzor9zW_lNFrWgllo7VZrJgm8lgXY7_GHIAfAMclvG0N0umZxZmUvgl_OCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cuYeOvyCS8KD03MN7oph1L34Wsw_sK1HSbipovcrwRVZiUKRza4Z7hxYhL9Fzk0AGhh2rR7f_MHnfRpHZ1zwsD9Zje7vT37TssMl-QQrO1EY2j1rigsqz8IaoZ9QspscYkejsSQ1TS9QdfPu5IHf_jlJQ5mVmCmMQEpZ2CiLKEDHrjxbyT0074beIgFVA4JgWC9uqQBt6I-OdEoMxdC4DWSJgbhzbRtkQP0nGpuy-skVV3Q8I4W_kJ5WCmrDY3CscMcrmwMlPT0JN8agMZ4gUsJFY3HP6TUhsbOlz55K15rLCFA4w3WJZwmWOggDWh1T7IfGP-uITesUa5e1Wc_CTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🛍
خرید اکانت
Windscribe
با کریپتو از طریق
Build a Plan
اگر قصد دارید اشتراک
Windscribe
تهیه کنید، می‌توانید از بخش
Build a Plan
پلن دلخواه خودتان را بسازید
⚡️
کافی است مقدار دیتای موردنیاز و مدت اشتراک را انتخاب کنید، سپس در مرحله پرداخت گزینه
Crypto
را انتخاب کرده و پرداخت را با ارز دیجیتال انجام دهید
🪙
🔵
انعطاف‌پذیر و اقتصادی
🔵
امکان انتخاب لوکیشن‌های دلخواه
🔵
پرداخت با ارزهای دیجیتال
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tx77ME1qUc9lDZk1RkQ1GH7KqK4Plv2AWiy3lEbIrbgzymwL4JcWrMg8h3xeLJfvoXVSZfjzbFZ_XJkOEfjU6W-Vkjt2mFtjXeTKz5onuRb_yRIvzgZg8xTm9NFazRCzZ4Rka381LDZzMbYK32w0WgKiTAw5ae0QTqJ3_eFgPQNOPZTh0FpaKyFj1fngO_FRqX-TX93w5TdxnMNWB_lozry8RUjMBuJEzgp5C3IMDVyYxIfU8d2fZIO_9FSO5sJTEAoxEfQctYxRI9u4OiPGCAl4kCdUfserBgynHI-XX2rcHpVwUCYpi7mGDnFEej0epw1yY5b7QtdQrt8UznuFJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!
‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون
‌GLM-5.3 Flash⁩
محصول شرکت چینی
‌Z.ai
⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی تست واقعی با ‌Cline⁩، هر دو مدل از پس باگ بر اومدن، اما Ox Alpha با مصرف یک سوم توکن و سرعتی خیره‌کننده‌، برنده بی‌‌چون ‌و چرای میدان شد
😎
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">عکس‌های داغونت رو تبدیل به شاهکار کن
✨
دیگه لازم نیست از عکس‌های بی‌کیفیت بگذری! نورون InvSR رو پیدا کردیم که هر پیکسل رو زنده می‌کنه، بهش عمق و جزئیات واقعی اضافه می‌کنه.
🔥
📦
نصب لوکال از
گیت‌هاب
🖥
آنلاین رو
Hugging Face
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">Avast SecureLine VPN
4KAX6F-Q7LM6J-5LCJ6E
3N7RAW-SG38HJ-5LCJ7W
BJS8N3-NNAVTJ-5LCJZJ
J3BSAR-XJZR32-5LCJME
VUYR9T-JZ5GBJ-5LCJVN
23RWWJ-SEAQGJ-5LCJTN
GFU46H-QA2CDJ-5LCJBE
7SKUU3-S97Y42-5LCJD6
UENGEB-Y9NGA2-5LCJEE
EBF8PY-8CPH82-5LCJ6J
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0bhoQBhoWlVU2oF3J1nsViDr5Xm6ZsbJZ1Mb6qVEI26WpYlSMEmjYH6nxEffekUzfltNuKDc0nwTnlCj0HFcK10QQs4y9EKGDty_3QgUaSXQNXkkwqK61XHGDe1S08_9qB391vVIEsMn--IUBJtCp6-a67IyqBS593OB-UyI9meRNk9SX2V46vHv80rzKy6ZJbmLfsGEQIyUKu_LrF297dpNN7xJ3CICUYyyPhGKFoUQU1hVtiE9LY2Xi8b8GY9auZiTT6qmhAjaffSEvt46VeuSqFUFTXYhEicZaJv9HrkIa27hrwBEnTo0-l7MC-A5QQoL3Nks9WETvSNleCvnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب
قدیمی داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
100 دلار
و شخص دریافت کننده
175 دلار
دریافت می‌کند!
فقط در کلاینت های گفته شده در Docs میتوان API را استفاده کرد
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_yTfSmsX0wrH2tf-cOakp6AKNeADt6GH76ZguvJ8GuYxaEUmlKl9BbTk9uwWDZDX9sJRkIGNr5Qv60djQ7CWxjXx2EpBrknsvqG5p1MWithJcHV0p0fkVOoZBm4Wnf4zlaFmishFNx8LGnnmnX7E1fZbHCnDGBtVvXT1PVlwKTYcZVlIE_nkA5WwbU02cdp3xBnUg3grL81iUbTJecPWDhWpEZIuGCiOGc4pK0izFDkREbQru7jY2M2jCvaC-hpbcwddAuG0ExT8hRGzLnZCwgPxdW2wFeM3rQtIikQfX54T3M98Sb3aERUsxtzN_TRFSCTPGRgRHW7BSzhqfabDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل‌های قدرتمند MiniMax M3 و M2.7 به مدت ۱۴ روز کاملاً رایگان و نامحدود روی GMI Cloud در دسترسه
⚠️
⚡️
📌
از
۲۴
اوت تا
۶
سپتامبر
🔥
همراه با
Speech 2.8
و
Music 3.0
🪧
دسترسی از طریق
API
خود
GMI
یا
OpenRouter
💎
بدون محدودیت استفاده
⛓
Link
🔝
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsZBEHSN0ucZTNKcqNATVG86HCPKvtkby4YtJssT3ti6eMeOMsyIe2lkUuITMNYqrQiAjLTw3fXHOTsgb-KgZN5kEX3qiDW84TvfyfpNYzftga3wERp9-HMA9bXGgV-9AwSiiWJw6P-Aa9uODmNOqLfQ2R9IceT2WzWJ1-eOSbs-Bn4-MgsX1UJ4zsV6oyJ1k04cBGwlBQRX0-9tZBj8o5UDr77cEvtrE9UN74nfp9uRExDSy1It0zyoStXU7NTHkSYzYQIBEc1WWJ7l4ptVSJOyAX89V-cnnAvtANgc6n1NQACPnexSa7kx4PTCyaxm-T11r3BZtlUwKoowNjGAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API بسیاری از مدل ها مانند
💥
🆓
:
Gemini 3.7 Flash | Gemini 3.5 | Flash-Lite | Gemini 3.6 Flash | GPT-OSS 20B | NVIDIA Nemotron | Nano 9B V2 | NVIDIA Nemotron | Nano 12B V2 VL | Ling 3.0 Flash | North Mini Code
✅
📌
Base URL :
http://aihubmix.com/v1
🔗
لینک ثبت نام در سایت
🔗
لیست مدل های رایگان
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oroOlp_EAzpUOJoTvN5rPi0xfjq1wVtdpriRRjM2O8xtuJY0afyIP83A30PggpNK6bQlqCvDQqW-lF_ta3tDzg0mHog6fUNlo_En27PY8seF0YwfYP0gbp4XDpHh_m3XvHHWX1JW9xAalT26jw1ausXRdO-kkepXIiU0909XJ16akirR1EYib4W1nl-VtCwj_q0wBmxmn2LpQ3lVgms-4ROkGyytSksAx_8U8UXWcEdXLIf2rNbBaUrg9cV_mAzDMJe-GTDbDpY6rxl1Aukj9eQgFrFdskNcSm6Qm_0Ww9pdFX4brqIbNqWCHEnixVKfenla_uM_D4y5IQHPFMAdgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به برترین مدل های ساخت ویدیو
💥
🆓
Seedance 2.5 | Kling V3 | Minimax H3 | Seedance 2 | Seedance 2 fast | Happy Horser | Kling V3 Omni | Kling O1 | Q3 Pro Video | Q2 Pro Video
✅
با این سایت 1000 عدد کریدیت معادل 10 دلار برای دسترسی به مدل های بالا دریافت میکنید
🚀
✨
مراحل فعال‌سازی :
1️⃣
وارد
این سایت
بشید
2️⃣
پلن رایگان رو انتخاب کنید
3️⃣
با اکانت گیتهاب یا گوگل ثبت نام کنید
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL : https://api.b.ai/v1
📌
Model ID : deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید …</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIXJrC7ovCe_oIbvv4DWWI20n2z5kG_oQRXyk1UsfXvVGgiZrpsn-dVNe4tNkEPhbKBSEeGFZBvK0dOg2eKX2dZr_1ewSIOPMeQRdTebCU5Wjw9JHvoJSDrpBSeY2EHP1-ycGXo0l2TPlABQKxBzvJCiRPQbyibYHuq7Few51-kbXo5Rg6iA076y30pfMabF1fMZ6CSZvEaGlufFYH6SLBw2P9OcODx8zqAyhXzfebhIz9l_5IKREhKn6odmom3GCZxy1tTqxS3TQfQ3rFEKA8TVb04ORMvi5pmf0J23Zqx2rCbcUwNZchl6gdJewsIUMPhcSKavflSgNxjFoOOMjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی رایگان به GLM 5.3
شرکت
Z.ai
یک اپ دسکتاپ جدید به اسم AutoClaw معرفی کرده که یه دستیار هوش مصنوعی agentic است — یعنی می‌تونه به‌جای تو روی فایل‌ها، مرورگر، برنامه‌های آفیس و حتی پیام‌رسان‌هایی مثل تلگرام و واتساپ کار کنه.
😎
🎁
هدیه ثبت‌نام:
کاربران جدید ۲۶,۰۰۰ اعتبار (معادل تقریبی ۲۰ دلار) می‌گیرن که تا ۳۰ روز اعتبار داره و می‌تونی باهاش مدل پرچمدار جدید GLM-5.3 و همچنین DeepSeek رو امتحان کنی
✨
مراحل دریافت:
1️⃣
برو به
autoclaw.z.ai
2️⃣
نسخه دسکتاپ رو دانلود کن (macOS یا Windows، نصب کمتر از ۱ دقیقه)
3️⃣
با ایمیل ثبت‌نام و وارد شو
4️⃣
۲۶,۰۰۰ اعتباری که داخل پلتفرم منتظرته رو فعال کن
⌛
زمان محدوده، هر لحظه ممکنه تموم بشه — الان ثبت‌نام کن!
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7556">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کانفیگ amneziavpn
[Interface]
PrivateKey = YM8CabYhib72x4z1G3Tv6YPTzkN1EgieYgzRAiEOXGA=
Address = 10.0.0.3/32
DNS = 1.1.1.1,8.8.8.8
MTU = 1280
Jc = 8
Jmin = 74
Jmax = 195
S1 = 115
S2 = 80
S3 = 44
S4 = 21
H1 = 220741314
H2 = 689752078
H3 = 1491205382
H4 = 2102461473
[Peer]
PublicKey = MF3gfbfjik3PoBeXrASElNP8OOXDlalC1ZCmLfqUuSo=
PresharedKey = 5AUecEnESNGx35D0nM1REFG1HAGtUuLTxlzhUHDhkSM=
AllowedIPs = 0.0.0.0/0
Endpoint = 65.109.215.18:51820
PersistentKeepalive = 15
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgUe40BOGs_WAQ8ijCV34k6HG6-IAuWgvhbExZnJQU4TCHif1sXD9jL8-z9MiKZ0_X6NCG4-FpO-MdFQqeNEkfqwANI562Ct8frPVLxsbD7HNkRPTwGqP4caGhSzDvKU4K2ayOVj8AejgSzxnmXQ3m0FMx7QyU-4RSvdiUBvH00I1L0SOH-y-t3503CPowbPd9m3MW0Lsyi8sioqxRz8N0qDemMwdJkphcDMMMWUY45r-XUZpR0_Ri73AlTyMI_mLiLW51AAOtY4GNPrFC3BQfNn_PnhV7eT8Y7ezw9erf03JTO-ZCCVJv7bYZyazlEp3HOZfFdJB1jhDjGVjYAeqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)
همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟
پروژه «روح‌گرام» یک یوزربات فوق‌پیشرفته و اوپن‌سورس با اتصال به Google Gemini هست که مستقیماً روی اکانت تلگرام شخصی شما سوار میشه و رفتارهای یک انسان واقعی رو شبیه‌سازی می‌کنه!
🔥
قابلیت‌های خفن روح‌گرام:
⭐
کدهای رمزی و نامحسوس (Stealth):
با کدهای ۳ رقمی مثل 777 یا 666 کنترل میشه و دستورات بلافاصله بعد از ارسال پاک میشن تا هیچ‌کس نفهمه!
⚡
شبیه‌ساز واقعی تایپ و خوانش:
🌹
قبل از جواب دادن، اول به اندازه طول پیام «مکث خواندن» می‌کنه، بعد علامت ...typing رو فعال می‌کنه و با سرعت دست انسان تایپ می‌کنه!
🎭
تغییر آنی شخصیت
🎲
با یه دستور ساده لحنش رو عوض کنید.
دریافت و استفاده از پروژه از گیت هاب:
https://github.com/faithsaly5-stack/GhostGram
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=LKtgp-q0aOfxrEin0_0tUyR_oQMlzTgWAIulIyxLmOfUCti_8HI7hB4tcoDQBAXi50rzHlR8Cqh9SQ8uAG4CAPKpOGIoOlgawW8jZ5vdqIjxoXQLOPAn_v-HSGP6oBMtsafHJ_WPN0WaJTCwnIkOlwMQjA9NYAArHBPVab4zUjmD7EwvlWTJCFXYvyhBFJWCBrvvUDFYlFkSlDwgKU970322Eche75dw6qVbUMl9_7JXOmVvCsCgxy015J_sVS4gSAiVBuGjIQKK_H7OSXkGi3Xg82gU1-I3JWUycgd9y0lCrrBRr8wl8FSGWJbzQ2EyPJF2XSCUV7x-Nt9-f1iCYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=LKtgp-q0aOfxrEin0_0tUyR_oQMlzTgWAIulIyxLmOfUCti_8HI7hB4tcoDQBAXi50rzHlR8Cqh9SQ8uAG4CAPKpOGIoOlgawW8jZ5vdqIjxoXQLOPAn_v-HSGP6oBMtsafHJ_WPN0WaJTCwnIkOlwMQjA9NYAArHBPVab4zUjmD7EwvlWTJCFXYvyhBFJWCBrvvUDFYlFkSlDwgKU970322Eche75dw6qVbUMl9_7JXOmVvCsCgxy015J_sVS4gSAiVBuGjIQKK_H7OSXkGi3Xg82gU1-I3JWUycgd9y0lCrrBRr8wl8FSGWJbzQ2EyPJF2XSCUV7x-Nt9-f1iCYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡
مدل‌های غول‌پیکر روی سیستم گیمینگ خودت!
محققان دانشگاه‌های UC Berkeley و MIT سورس‌کد سیستمی به نام FreeToken رو منتشر کردن که مدل‌های بزرگ MoE رو بدون کوانتیزاسیون شدید، روی سخت‌افزار معمولی اجرا می‌کنه. سیستم به‌صورت هوشمند محاسبات رو بین GPU، CPU و RAM توزیع می‌کنه.
💻
📊
نتایج کلیدی:
🔺
مدل Qwen3.6 35B روی لپ‌تاپ با RTX 4060 8GB تا ۳۹ توکن بر ثانیه
🔺
مدل DeepSeek-V4-Flash 284B روی RTX 5090: ۲۲ تا ۲۵ توکن بر ثانیه
🔺
حتی مدل ۷۵۳ میلیاردی GLM-5.2 روی یک GPU ورک‌استیشن قابل اجراست
✨
ویژگی‌های دیگه:
🔺
پشتیبانی از ۲۰+ مدل باز MoE با فرمت‌های مختلف کوانتیزاسیون
🔺
یک API سازگار با Anthropic/OpenAI برای اتصال به Claude Code، Codex و ابزارهای مشابه
🔺
نصب یک‌کلیکی با GUI برای ویندوز و لینوکس، بدون نیاز به تبدیل GGUF
🔺
متن‌باز و رایگان با لایسنس Apache 2.0
🔗
لینک مخزن گیتهاب
🔗
لینک وب‌سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=cP9IGynaiALKhicLx6dHhmOGJejbnA_Ug2nZz6AV6ZncFI-4yWZ8bMW8Zd4x1cwDsu8NwuOtb12H9x9bELmYloydNFzlIA8R7EeNx1W5i75-uqHQjVa1TkAqYiSYBpvyak6vncGbDsIHQ4mkBWIWKiGFO__0hilEzleG2dsLSgs6JOg6s8ysDGMzDI5JKfIbh7vzs2MPfsF17litaR5c5rXzaUjvrCPtTtenJ8sDpNo_079OKSFt9WPNmMQdsInCgQVfmBtJVi35Gziqk_2S5KZSqL4XHwo9naWPJTfjWx0bc5Yg_JSu-wIKE_B0THvFgJEn8q2Nx11snwXBOUoe-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=cP9IGynaiALKhicLx6dHhmOGJejbnA_Ug2nZz6AV6ZncFI-4yWZ8bMW8Zd4x1cwDsu8NwuOtb12H9x9bELmYloydNFzlIA8R7EeNx1W5i75-uqHQjVa1TkAqYiSYBpvyak6vncGbDsIHQ4mkBWIWKiGFO__0hilEzleG2dsLSgs6JOg6s8ysDGMzDI5JKfIbh7vzs2MPfsF17litaR5c5rXzaUjvrCPtTtenJ8sDpNo_079OKSFt9WPNmMQdsInCgQVfmBtJVi35Gziqk_2S5KZSqL4XHwo9naWPJTfjWx0bc5Yg_JSu-wIKE_B0THvFgJEn8q2Nx11snwXBOUoe-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت خروجی 0x Alpha و fable 5 در یک نگاه
👀
تو کل سطح اینترنت واقعا اتفاق های خیره کننده ای با این مدل رقم خورده
🔥
➡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7548">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVfuSWuYA0zD2XC2EqQfpVWuiQB7xzxMOx0nrJsLydcoCRfXZ9KlBXA3gx0alWnN_eGVgngH4kuGBL2qBhR4U31YbJDQ5UlM_jViTRNgsxz0jUgDNcjOCdsp0RoAe34Dq-x9jvtRDeKJCmuXuXz0-tZUPvdDw2sVVdKBU8VxAdmnukGcGxbE6GIcejrwqXzrTRLhZWuzpXYIZtFga4DxqDjdDnPyMM0PqiVDD21J8dhHdqT25zCfD4kqYVYBPuH5ZKmLt2FjVVPLuduAgf4W91V5GHW9tA3cGyFtKcHNWlAhGTNpIO7NHLM7qm1H2laurjAtjjSWjQkxDMtACCnohQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔬
دانشمند هوش مصنوعی که خودش مقاله می‌نویسه
یک پوشه از داده خام رو بهش می‌دی، یه جهت تحقیقاتی مشخص می‌کنی، و سیستم از فرضیه‌سازی تا مقاله‌ی نهایی PDF رو خودش انجام می‌ده.
🧪
✨
ویژگی‌ها:
🔺
کار با هر فرمتی: تصویر، صدا، ویدیو، اسکن سه‌بعدی، جدول، فرمول
🔺
درک مستقیم داده‌ی خام علمی، بدون تبدیل انسانی به جدول
🔺
سه مرحله: فرضیه‌سازی → آزمایش با کد واقعی → نگارش مقاله با DOI معتبر
🔺
اعتبارسنجی داخلی: هر عدد باید از خروجی واقعی کد تأیید بشه
🔺
سه روش اجرا: دسکتاپ، CLI، ماژول ادغام با ایجنت‌ها
🔺
پشتیبانی از Windows، macOS، Linux
🔗
لینک وب‌سایت
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7548" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7547">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUuitS0AkL7GkJy9Ek6kFSsHLSrlgH_7EGUZYZ9mIf1GIUs76YyLb1RX_grMyBn-eyXV01L_jx7bcR-BvjT3drdjnlYlbgLduoo6YRzu_6VjUeVcD6N3UdI4GYAa6v1rcmGuLYEpOW_rECZxJSFDCW7Zmv8jUJVgL04MPYqdGauxVGRGqynHxSnfMX0d0yKun3zGaDTsne69kBPtmGEE54DUB8ZajIZJQtkbvmt1oTMjHEbdSbV2qaIkR8nqbqUxKf1lGXii3TFN-4j733qB7-X25Gb0k0f_2Jx-ndvfUPi7E77sK3LTfpD-KQ1Uqt359BO6quPSmlyv25QUE9Zlog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جدا کردن صدا و موسیقی با یک کلیک
یک ابزار آنلاین رایگان مبتنی بر هوش مصنوعی Demucs که صدای خواننده رو از موسیقی پس‌زمینه جدا می‌کنه. کافیه فایل صوتی رو آپلود کنی.
🎶
✨
ویژگی‌ها:
🔺
آپلود فایل محلی با فرمت‌های مختلف
🔺
جدا کردن خودکار صدای خواننده از موسیقی
🔺
پیش‌نمایش آنلاین قبل از دانلود
🔺
دانلود جداگانه‌ی تِرَک صدا و موسیقی
🔺
بدون نیاز به ثبت‌نام یا حساب کاربری
مناسب برای موزیسین‌ها، خواننده‌ها، تولیدکننده‌های محتوا و ادیتورهای صوتی که سریع نیاز به جدا کردن استم دارن.
✅
🔗
لینک ورود به سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IW_YHguj0lE5nZTAbYmW9qEBx1oxSB5_69MyiBXWLqNoZvL3EcadBaFsTHlMN0lUvhKPnu_4oYqVPnk4tDFfSxTTcjp47tvMQu44K6QnbhMLlw4se3QL3LbExeokRpECMShZsqOjRckNdVRIDrKHHgs0_ut_qSRFfs9vil7B839RjWcFiwieOveIitCqM-ifxFPjZ2nENBRrtBvvyHJV2-3MyaevN3ZtGoMks6uavE0JdoGwMiXJ1fWFbBRVjLA9k_q39lIJOUHb8bmn742jmxiM3imVb6wi64cXEFWSx-xQl3kxDhuBeGhLqUWpICvzEunBgJGfUEROxDEZ5uWfXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 دلار برای استفاده از API مدل های هوش منصوعی زیر
😎
🆓
Opus 5 | GPT 5.6 Sol
✅
در سایت زیر با ایمیل یا اکانت گیتهاب ثبت نام کنید
( ابتدا کپچای سایت رو تکمیل کنید )
سپس کلید خود را بسازید
✅
📌
Base URL :
https://true-sota.com/v1
📌
Model ID :
claude-opus-5
|
gpt-5.6-sol
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">DeepSeek V4 Pro
| MiniMax M3
♾
♾
♾
♾
♾
ApiKey
—
sk-dc9d4b7df36ba555-rcaq9e-2790fa25
Model
—
am/deepseek-v4-pro
/
am/deepseek-v4-flash
/
am/minimax-m3
URL
:
https://anymodel.org
♾
♾
♾
♾
♾
Free
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7544" target="_blank">📅 21:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7543">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به
هرمس
اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7542" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7541">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">5 میلیون توکن برای استفاده از GLM
💥
🆓
به مدت 5 روز هروز 3 میلیون توکن برای GLM 5.3 و 2 میلیون توکن برای GLM 5 Turbo برای کاربران جدید در اپیکیشن Zcode
✨
مراحل دریافت :
1️⃣
وارد سایت z.ai بشید و با اکانت جدید ثبت نام کنید
2️⃣
برنامه Zcode رو دانلود کنید…</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7541" target="_blank">📅 19:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7540">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=sD7i7T1pCxUyDDh9YJ0BwL28JzFYS5oitikqg_CEbpE5LRj0UxvU7JbX-SC9TNfIdkxp_PzoqZhkYrFt2se1yq34B_wK6uJK058GTLmbl9ysdupJ-qsExfNBbWmT_qVi1nYVDqF_4ZSMuJ2fZ5DvIVacZcjbNZNk0_q5YcDT-K8PK0KwIauri_5H16O3qbbAOjHyljsxMIUvGILfeJtpFTuYscd3E9pVnKbtH1_ZrBVu0FzoNU08t_OirlpDlAv1y9BqWtrE4PlT3fSYJDvbzq55CoxPwVF5zfotNWI7tjLaxLERjQxShpoGY5qEb9oyqps9qyep0GdW4lLYcWSYFFLWQgobZBvYYoRdDsBZIS9AA1WwCv32cszkKT2BMVb2uw0KtvtnNFP0fd3pPUM4o47WdAil7wz4HquFOor7y4zyYt-cRa9yrKlHuTBF6fkKREdkKbl6vfMcdcN1CoXdB3fFXmjFCjFd-cIIEQa07s--rXOEDctEOs8-HopQ7s22N3Yb8NWFG-or2hnEdGO_42aZ5KcJe-WNnahWTHPkanA5N9dgSslIdAjxqParA7zmUi14S5p35GpCuQbbvvviOBIVTGsGSf9gZQGwAqXjgtnP1dNSXvkPGB41XWyHnh8Xr208LAgFr6nKC8_X_jzRb-MiFBJUBDhwZRzo2zRN3Qo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=sD7i7T1pCxUyDDh9YJ0BwL28JzFYS5oitikqg_CEbpE5LRj0UxvU7JbX-SC9TNfIdkxp_PzoqZhkYrFt2se1yq34B_wK6uJK058GTLmbl9ysdupJ-qsExfNBbWmT_qVi1nYVDqF_4ZSMuJ2fZ5DvIVacZcjbNZNk0_q5YcDT-K8PK0KwIauri_5H16O3qbbAOjHyljsxMIUvGILfeJtpFTuYscd3E9pVnKbtH1_ZrBVu0FzoNU08t_OirlpDlAv1y9BqWtrE4PlT3fSYJDvbzq55CoxPwVF5zfotNWI7tjLaxLERjQxShpoGY5qEb9oyqps9qyep0GdW4lLYcWSYFFLWQgobZBvYYoRdDsBZIS9AA1WwCv32cszkKT2BMVb2uw0KtvtnNFP0fd3pPUM4o47WdAil7wz4HquFOor7y4zyYt-cRa9yrKlHuTBF6fkKREdkKbl6vfMcdcN1CoXdB3fFXmjFCjFd-cIIEQa07s--rXOEDctEOs8-HopQ7s22N3Yb8NWFG-or2hnEdGO_42aZ5KcJe-WNnahWTHPkanA5N9dgSslIdAjxqParA7zmUi14S5p35GpCuQbbvvviOBIVTGsGSf9gZQGwAqXjgtnP1dNSXvkPGB41XWyHnh8Xr208LAgFr6nKC8_X_jzRb-MiFBJUBDhwZRzo2zRN3Qo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
استودیوی هوش مصنوعی که خودش کارگردانی می‌کنه!
اپیکیشن MiniMax Design یک اپلیکیشن مستقل برای ویندوز و مک‌ هست . کافیه ایده‌ت رو توضیح بدی، هوش مصنوعی خودش برنامه‌ریزی، اجرا، کنترل کیفیت و نهایی‌سازی پروژه رو انجام می‌ده.
✅
✨
ویژگی‌ها:
🎬
ساخت تیزر تبلیغاتی، گرافیک، بنر، محتوای کاربرساخته (UGC) و انیمیشن
🧩
ادغام فیلم‌نامه، استوری‌بورد، ویدیو، تصویر، صدا و ادیتور در یک فضای کاری واحد
🔌
دسترسی به پلاگین‌ها و مهارت‌های تخصصی متعدد
📂
امکان وارد کردن فایل‌های محلی و اتصال به سرویس‌های خارجی از طریق API
💰
بعد از ثبت‌نام، ۳۰۰۰ کردیت رایگان اولیه به کاربر داده می‌شه
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7540" target="_blank">📅 19:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7539">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnCPInem0Ri8skv5WOc7MEd2r6m_QWppxyAgLxcCGZNW0qHUDH0P3uLybyyd7i43rV0qDD6hCdWoPbSLlOWoPq5dAfYH-kBgyZXe6TmW0FTz-ddFOpYtsJirHs7Y-7eGM0nRD_ZbqZ5eMfOzuCc4jcNDrwL36slatozyZHmngg5MzzGfizF7aDiuPIfqccV0BDnxT1wXAhDAM1rO5FcQ6gB4k3NyHngmaHOVv4IleydYVMBiVDDyHjS0Okd7cG4MRY54LS5_fZ_wVv8ga0IasDO9u74rBcNBD2UsfythRA8lEM0ufwudZ2-8fX5r8igigjbqZOAWAF59Xa6mEeafNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐳
۹۷ ابزار جادویی برای DeepSeek Harness — یک دستور، قدرت نامحدود!
یک لیست باز از افزونه‌ها برای DeepSeek Harness (dsh) — با یک دستور می‌تونی قابلیت جدید به ایجنت اضافه کنی.
🔌
✨
دسته‌بندی پلاگین‌ها:
💻
بهبود رابط کاربری — TUI، پنل‌های کناری، پالت دستورات
💬
نشست‌ها و پیام‌ها — شاخه‌بندی تاریخچه، اشتراک‌گذاری گفتگو، حافظه
🛠
ابزارها — اتصال به دیتابیس، CSV، JSON، regex، آمار
⚙
اتوماسیون — هماهنگی چند-ایجنت، زمان‌بند وظایف
🔔
اعلان‌ها — اتصال به تلگرام، هشدار دسکتاپ
🧩
توسعه/رانتایم — ممیزی امنیتی، sandbox، ابزارهای گیت
🎮
فقط برای سرگرمی — بازی‌های کوچک، استیکر، پت مجازی
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7539" target="_blank">📅 18:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7538">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKdt4ztNkg2Qcv0u2kQ4_MpBXFDwe56RlmJUihwZzYeSxLeMNgeOzBjSCH5ytGofVeD-MKtWCJ_o__klDNPO1768aWJ-2CZViV1GCzfE4tPNe47YPVdJyov_uocIZjz5VBBa5tzeKy_sxt5wG9nvgNreywirlYdsynPqL0blC533JrbC1dR9iM7gavb1xx76zkk-_Vg4lczhGKomm_Gx70FCkUQPrAd5CN7FWbzMYaMy73ItDlbUf6kGWfPWN6Yx8oP00SYC4L8aKiWHScSv339XzKcgSbd55rgVHrlsTDJHYCncIldzJVg8nvGjizi3B3AT0-2ahqaPsxO7sEBikw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
پروکسی وب جدید تلگرام — پنهان‌شدن پشت سایت‌های معمولی
تلگرام یک روش جدید برای دور زدن فیلترینگ آماده کرده که ترافیک پروکسی رو کاملاً شبیه ترافیک عادی وب می‌کنه.
🥸
⚙️
نحوه‌ی کار:
🖥
تلگرام دسکتاپ یک مرورگر کوچک داخلی باز می‌کنه و یک اتصال معمولی HTTPS/WebSocket با دامنه‌ای برقرار می‌کنه که ظاهرش شبیه یه سایت عادیه
📦
کل ترافیک MTProxy در یک جریان واحد بسته‌بندی و از طریق این کانال مبدل ارسال می‌شه
↔
روی سرور، یک نود واسط (relay) این جریان رو به اتصالات جدا تفکیک می‌کنه و بدون رمزگشایی، به MTProxy معمولی می‌فرسته
🌐
دامنه هم‌زمان یک سایت عادی نشون می‌ده، و صفحه‌ی «پل» فقط برای تلگرام و بعد از تأیید باز می‌شه
🎯
نتیجه:
کل ترافیک از دید ارائه‌دهنده‌ی اینترنت مثل بازدید از یه سایت معمولی به نظر می‌رسه — یعنی پنهان‌کاری تقریباً کامل در برابر فیلترینگ.
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7538" target="_blank">📅 16:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7537">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWg4KAKM_xDqjBXgmRGkGHrA2GpJpzFp-DOqzb99jwstGYvGftlntDL5WLNaQJxjFcCjzu5GiKFl6jej_SC38qn6dZpkzSBIwEDkSCPAqXX2gIlr052zXV0ha4nSHFdVfcwWWgRr2XpInv74vHYYvflUEZ2cvw3vk86UzSRAVZCp9nCBPuBcN_NOw0ATMv6rJ5Wx8tY4XDmOQG8L2jBzy_aQf8_1t6Lr7v67allxa_5JstgdH6oBncDOW7xHx3rCt_RoHk_TqV9EZ-Gfw2_0Jw_ct0NprkQgZCrwqTp4RJ_ZPKiQnrhxiqWmVBL9BF6BQdyTQFeR3MIu1TNrL-zjJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
زمین بازی هوش مصنوعی برای ساخت چهره و آثار هنری
سایت Artbreeder یک ابزار رایگان آنلاین برای ساخت تصاویر با هوش مصنوعیه که تو ساخت چهره، کاراکتر، منظره و هنر انتزاعی خیلی خوب عمل می‌کنه.
🖼
با کشیدن اسلایدرها می‌تونی ویژگی‌های چند تصویر مختلف رو با هم ترکیب کنی و یه تصویر کاملاً جدید بسازی.
⚡️
✨
ویژگی‌ها:
🧬
ترکیب و «تولیدمثل» تصاویر با تنظیم سن، جنسیت، حالت چهره و...
🖌
ابزارهای متنوع مثل Composer، Splicer و Collager
🤝
کامیونیتی فعال برای ریمیکس و اشتراک‌گذاری آثار
⚠️
نکته‌ی مهم:
تو پلن رایگان، تصاویری که می‌سازی
به‌صورت پیش‌فرض عمومی
هستن و همه می‌تونن ببیننشون.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7537" target="_blank">📅 15:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7536">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlE3f0qlaiVMwnYSQwKbTokSKFhWwNOIcp4z0Fjxv647Kj1FO7KB4YMvSsgYmg1WZZN0xkAKuSRhXG9FANrGrBpV1dhJOlOX4iYWEyxf1L_v8VAtm69OOMsatJPZmI5-j37Qs6eQUUhLEYeyR3DOn6243W-NP1rFl6OGdOJQZohBjMTTBwErxjlvn4XuzmzqDF2Om_GytgeFDWVjar3Jpp0DRGguOF0cgQHM32ecMx2gVBYJWltpSeFc0IJw7ohdmW9l0MHm12hAMZhmY4x99E-VgSs6N9ub_5_4frWs7FsRHy-F8MpXYsOTu1U_myAOZ0_HsWwuOxyKXzck5WbzPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
دروازه‌ی رایگان به میلیون‌ها مقاله علمی
سایت CORE یکی از بزرگ‌ترین موتورهای جست‌وجوی مقالات با دسترسی آزاد (Open Access) در دنیاست.
🌎
بیش از ۴۰۰ میلیون رکورد علمی رو ایندکس کرده و برای بیش از ۴۰ میلیون تاشون، دسترسی به متن کامل رایگانه — بدون نیاز به اشتراک یا پرداخت پول.
🆓
✨
ویژگی‌ها:
🔍
جست‌وجوی پیشرفته
📥
دانلود مستقیم PDF بدون پی‌وال
🎓
پوشش تقریباً همه‌ی رشته‌ها
اگه دانشجویی و داری پایان‌نامه، مقاله یا مرور ادبیات می‌نویسی، CORE می‌تونه یکی از منابع خیلی خوب برای پیدا کردن رفرنس‌های معتبر و رایگان باشه.
📝
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7536" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7535">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDAKHbEQHk2eR20DSgD4gt_Wd-KnsC7KRlUqe8w5TeLJxeXchVV3BV1Jyt_K_YC0xKEPaG4uQdDTIc43Z107gnlUJkKQY9Ys_cN2RiDXYkwUjjReEOkmjMFAS_XmLu5C363exx9Xz5P0ay2QALc2Yj-fVaDKlo3GwsajUFnkhA8OTs5WjNaG-Dy7guRcH9J09ToqUG25KBZitjo3TaLhr6UQtYF4oLN5eBGuO-_i7uV30g0XObPQfR9VQj5MPlmREI6NXIjX6b-1MyI_wtwWa4TwgnqhGDWdhy9GdB0kRav70vXweNJRv4FF1MSW8O4JLoiW31je7ctsmxY6qWTf3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتبار رایگان API تا ۳۰۰ دلار بدون نیاز به کارت بانکی
🆓
🧠
فقط با اکانت
گیت‌هاب
ثبت‌نام کن و بسته به سن
اکانتت
اعتبار رایگان بگیر
✅
با این اعتبار می‌تونی از
مدل‌های قوی
مثل
GPT
،
Qwen
،
DeepSeek
و بقیه استفاده کنی بدون اینکه هزینه‌ای
پرداخت
کنی
🟩
Link
🔗
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7535" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7534">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-text">🚀
آپدیت جدید ربات وگا
🧠
حافظه هوشمند وگا
از این پس وگا اطلاعات مهم شما را به خاطر می‌سپارد تا گفتگوهای پیوی طبیعی‌تر و شخصی‌تری داشته باشید.
💬
حافظه در پیوی:
اسم، سن، دستورات و قوانین دلخواه شما ذخیره و در گفتگوهای بعدی استفاده می‌شود ( قابل حذف کردن هست )
👥
حافظه ماندگار در گروه:
دو نوع حافظه مجزا
• حافظه عمومی: قوانینی که برای همه اعضای گروه اعمال می‌شود
• حافظه فردی: اطلاعات هر کاربر به‌صورت جداگانه در همان گروه ذخیره می‌شود
از بخش «سرویس‌های هوشمند» گروه فعال می‌شود و قابلیت ریست نیز دارد
♻️
📊
حافظه کلی ربات نیز گسترش یافت. وگا اکنون پیام‌های بیشتری را در گروه‌ها و پیوی‌ها به خاطر می‌سپارد.
🧰
جعبه ابزار جدید در پیوی
پنج ابزار کاربردی اضافه شد:
💵
بررسی قیمت ارزها
📰
آخرین اخبار
🌐
تعامل با وب
🌎
مشخصات IP
💱
تبدیل ارز
🌐
تعامل با وب:
لینک هر سایتی را ارسال کنید تا وگا از آن اسکرین‌شات بگیرد، لینک‌های صفحه را استخراج کند، یا به HTML/JSON تبدیل کند
🌎
مشخصات IP:
آدرس IP یا دامنه را ارسال کنید تا لوکیشن، دیتاسنتر و سایر مشخصات آن نمایش داده شود
💱
تبدیل ارز:
به‌سرعت بفهمید هر مقدار از یک ارز معادل چقدر از ارز دیگر است
🛠️
بهبودهای فنی
✅
تمام باگ‌ها و مشکلات گزارش‌شده برطرف شد
⚡️
ریت لیمیت گفتگو از ۳۰ به ۴۰ افزایش یافت
🤖
مدل هوش مصنوعی جدید DeepSeek V4 Flash (0731) اضافه شد
✉️
هر مشکلی مشاهده کردید، به پشتیبانی ربات گزارش دهید
💡
ما همچنان در حال توسعه و بهبود ربات هستیم. منتظر قابلیت‌های جدید باشید!
🧠
Vega AI
| هوشمندتر از همیشه</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7534" target="_blank">📅 00:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7533">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvp1cLm9Cy-Y8jEeuEEmxJ9zGomZVhi3gBT4Uxymy3ckkH7_fztpOTpR0zzcXGSTPjT0R7QjbvtnIbqMv5ikdumXut_fQLOIpEVE2Y2vnZX_CkClM5kcVDCoiWZQDw-gY2Jm2NCLDG09zDThzps55SGp-VE2VrtTaMS4hLVxpPmEV-AtnGUY0xUcyhGWLmzQf55rS6oYaSZm75J2eTpd0dL0eO72_o0t26Q1OBXASuLARny45w35fo2lXnqxabUbRVyeGbnTvraFEe-ZT36QldoYUg87Gg6LGSfh9qQe9bxq5F5CpeZzA1GzDMl_sUiFm1_dyWV_suzNQ8dUuzwj8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی کاملا رایگان به مدل های هوش منصوعی زیر
💥
🆓
Opus 4.8 | ox alpha | Kimi k3 | GLM 5.2 | Deepseek V4 Flash 0731 | muse spark 1.2 | Mimo 2.5 | GPT 5.4 | Grok 4.1 | Haiku 4.5
✅
📌
Base URL :
https://api.yjs.im/v1/
موقع ساخت کلید حتما گروه Free یا Free lite رو انتخاب کنید ، قبلش به بخش Playground برید تا بفهمید هر گروه چه مدل هایی رو پشتیبانی میکنه
✅
برای استفاده از مدل های رایگان داشتن کریدیت نیازی نیست
❗️
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=NyGuDkW7NBeZnXwwTl6mgZALGV5MAiPUTxAfA_9MChqlv_VJtkeYkQZBreax84yLU8GL2elmw0RXRxml0kUvsbrGFYUeDM2xeGyoGdC8m1allVyBe2eXpU-9HuKeuo09Zgrm9Op6aFbVHO4cMGYcFCOuRHtIVTzxQ8QkXuLEfPNmjyD2yW9xsGnDt2DqKk0MDHXVE_q2aZk-plZJOgWVlk6FevV67k3zGku16BMnNN00fFx_w9tqcDuiMSbyzrq8pZA25sS0d2zWJYU_4Myx3p8AvnWuv4eIgCUoShfNmrY4sW11C3iKQD8isIJ7KjQYsj0jLNSpmec8n6rplAwYsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=NyGuDkW7NBeZnXwwTl6mgZALGV5MAiPUTxAfA_9MChqlv_VJtkeYkQZBreax84yLU8GL2elmw0RXRxml0kUvsbrGFYUeDM2xeGyoGdC8m1allVyBe2eXpU-9HuKeuo09Zgrm9Op6aFbVHO4cMGYcFCOuRHtIVTzxQ8QkXuLEfPNmjyD2yW9xsGnDt2DqKk0MDHXVE_q2aZk-plZJOgWVlk6FevV67k3zGku16BMnNN00fFx_w9tqcDuiMSbyzrq8pZA25sS0d2zWJYU_4Myx3p8AvnWuv4eIgCUoShfNmrY4sW11C3iKQD8isIJ7KjQYsj0jLNSpmec8n6rplAwYsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
بزرگ‌ترین نقشه جهان منتشر شد
دانشمندان بزرگ‌ترین و دقیق‌ترین نقشه‌ای که تا امروز از جهان ساخته شده رو منتشر کردن؛ حاصل ۱۳ سال رصد بی‌وقفه با ده‌ها تلسکوپ برتر دنیا.
📊
اعداد و ارقام قابل توجه:
🪐
۴ میلیارد جرم آسمانی
☀️
نزدیک به ۶ تریلیون پیکسل
📷
برگرفته از ۲۶۳ هزار عکس
این فقط یه تصویر ساده نیست؛ دقیق‌ترین و جزئی‌ترین تصویری‌ه که تا حالا از کیهان ثبت شده و بعید هست به این زودی‌ها دقیق‌تر از این ساخته بشه.
🔭
می‌تونید خودتون توی این نقشه کاوش کنید و گم بشید توی ابعاد کهکشان‌ها:
🔗
لینک سایت برای مشاهده
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxK-D3lWMXokrHh0u6U6uiE9xj_aEE6bkPJ27QXa4zFLXgwnXUJAVSqHmnIfjXv1f4xX2KWaqTDRE9n7RnW8sUsvZQWMbpgSqkJaBqdrafW2zfA8aVYHR0WDsOVcf5E5eM6zxUxGUoE62SJXbOdylsyaXZ_e5Y59tYf7TFarEOGU_4mmcks4coNmpE73iQqtOT6vSzmULx5uaUCH1o6ZciHNUKvOic-VwdI4V0kKAO144mXkKhXrL5nXljQZiPgsDrXNHChoBNu0yMBnT9JsDBbPolixe-lik3FyxftzhgT4pTm5HM9OCB6BTgGLsfMIvkJAkrd2Fzp7I5Ur8aA7Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل استلثِ ناشناس Ox Alpha رایگان شد
🥷
مدلی ناشناس با نام
Ox Alpha
، بدون هیچ اعلام رسمی از سمت سازنده‌اش، روی OpenRouter به صورت یک هفته رایگان و OpenCode منتشر شد
⚡
✍️
مشخصات فنی:
🔺
پنجره کانتکست: ۱ میلیون توکن
🔺
حداکثر خروجی: ۱۳۱ هزار توکن
🔺
ورودی مولتی‌مدال: متن، تصویر، ویدیو
🔺
قیمت: رایگان طی دوره پیش‌نمایش
🥸
سازنده مدل مشخص نیست. این یک انتشار «استلث» است — یک تأمین‌کننده ناشناس در حال آزمایش مدل است، و OpenRouter صرفاً درخواست‌ها را روتینگ می‌کند، نه توسعه‌دهنده یا مالک آن.
🇨🇳
❓
درباره منشأ مدل، برخی کاربران گزارش داده‌اند که در پاسخ به سؤالات حساس ژئوپلیتیکی (از جمله تایوان) رفتاری مشابه مدل‌های چینی نشان می‌دهد. این صرفاً یک گمانه‌زنی است و هویت سازنده رسماً تأیید نشده.
📈
طبق ادعای برخی کاربران، این مدل در تسک‌های کدنویسی agentic عملکرد قابل‌توجهی داشته، هرچند این ارزیابی‌ها فیدبک کاربری هستند، نه بنچمارک مستقل رسمی.
🔒
بر اساس توضیحات ارائه‌شده، داده‌های ارسالی طی دوره تست برای آموزش مدل استفاده نخواهد شد
🔗
لینک صفحه در OpenRouter
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7530" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7529">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbFBNqTzB6U8fh8IorW8gtAmRC-bnqEyW2pR7O48kJERoBIKVsvRplzy128xxfdfuRfoeeaa9mWrckMCLaa1FFaVfouFxu8Vy468LH8B-LocneIiauxbgo8Ggna-hK7Dm2hvarZ8zw-JmAHMUuimXuBZOmOs4pNKTMAF0GqMNA8Sj5LFLJmnCbLl8qQllWpOM6wQiBiRrarxKu4-eH7OwxTVatL-8ppHjuqAXircmone4SDprOisg5u9dIno4ieFhHZnJx68nKU8SKEN4mzecZ-Tzmu6bEtml5P6HY3fA0o4ZUuxFzn8CEES7zIkR7LHOh2ERDj4TKfCOpjDbEwojA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">70 دلار برای دسترسی به API بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدمت یکساله باشه )
داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
40 دلار
و شخص دریافت کننده
70 دلار
دریافت می‌کند!
همچنین تا 25 دلار پاداش لاگین روزانه
🎉
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-RN0hFLyYvhsN4Dc5ZF3amsYJXkopTZfFptMHh2YaaswoX9b3ZiwNdJoefrug_VDYgWkHzlPSDBUemghTqtlyW0WCAXG1RWW_HssBwOOdogWV1g5kVYzmGA_0o9uSaL7l6tWY_kn4pz_KjhE3QZbhsVbGoR6A_sPanXuTgSaT7XOzM6yzPB_qOzOS71Y36ySGKBR9y30NOV1AJlhblzmTO3Eg960q7FrUiPOm7dW7HapdNaeDXriNkjsDCqlwM5WMomsYV3CnnDtrcmabOKatbNeG2wnYDN4WxAoz2JVCPnOsjGCA_QNYFVPWdxi5mkNCvpKV_HcJrdSYKLVnUILg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7525">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8XERogOoizNRd2Vyk1om7y8uSy5S3xtrb9mobjan3v1_cW6P1N2r-_PRZM8FaJ8RFUvm6yCiTVFyMVDj9x70J_tXYhZeB6V477xkCf-EbBWyGJdr2tjvqb1aMzB9mOECD8DNI0-U8--6a0OMsRviYZ0X6vcXzNbqY6aI0Ks9viDxp0D4kAYqbjz0Mgf3YcYP4Mv24dvfH1h9LiteHUtyhK41CiONucaGjBFXE3NPm77gTVUl_4r2AbdrXoNEPhYCYJwTo7iHRX2QeAZ6_c6SDCQprwfirL7hoK1SCKj36LokmMbvz5Ch_vt5xGF60fqGVDx1dNwf-2m6JwouRQ26Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 میلیون توکن برای دسترسی به API هوش منصوعی زیر
💥
🆓
Deepseek V4 Flash 0731 | Kimi k2.6 | MiniMax M2.7
✅
📌
Base URL :
https://hskyauefqcgbvgvxkluj.supabase.co/functions/v1/gonka
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7525" target="_blank">📅 20:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7524">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔒
بهترین ایمیل‌های امن و خصوصی
اگه دنبال یه سرویس ایمیل هستی که حریم خصوصیت رو جدی بگیره، رمزنگاری کنه و داده کمتری ازت جمع کنه، این‌ها بهترین گزینه‌ها هستن
🛡
🇨🇭
Proton Mail
— معروف‌ترین ایمیل رمزنگاری‌شده، با پشتیبانی کامل E2E
🇩🇪
Tuta Mail
— تمرکز کامل روی حریم خصوصی، رمزنگاری در هسته سرویس
🇧🇪
Mailfence
— پشتیبانی از OpenPGP، مناسب کاربرای حرفه‌ای
🇺🇸
Riseup
— سرویس غیرانتفاعی با تمرکز بر حریم خصوصی
🇳🇱
StartMail
— قابلیت ایمیل مستعار (alias) برای حفظ گمنامی
🇩🇪
Posteo
— بدون تبلیغات، حداقل جمع‌آوری داده
🇸🇪
CounterMail
— امنیت بالا، پشتیبانی کامل از OpenPGP
🇨🇦
Hushmail
— مناسب استفاده شخصی و حرفه‌ای، رمزنگاری‌شده
🇩🇪
mailbox
— سرویس قدیمی و معتبر آلمانی با PGP
🇨🇭
Librem Mail
— از تیم Purism، تمرکز بر حفاظت داده
⚠️
نکته مهم:
داشتن رمزنگاری همیشه به این معنی نیست که ایمیلت کاملاً end-to-end رمز شده — یعنی گاهی خودِ سرویس‌دهنده هم می‌تونه محتوای ایمیلت رو بخونه، هیچ ایمیلی هم امنیت 100% تضمین نمی‌کنه؛ این چیز به عوامل زیادی بستگی داره: تو کدوم کشور سرور داره، چطور داده‌هات رو ذخیره می‌کنه، و حتی خودت چقدر رعایت می‌کنی
❗️
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7524" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7523">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6HqzkveAvb-zlE2_cvMmYnqW9rMojGMk_BnMun2415Oepb8gnMG9sitj_5d5d0at1zHYGfkEv2EFtdPfa4kZkSwA1Ny_p6mJWmSF9jQqAjh5ydp8r6c-abUL-mj5CZ1TAjk4piIwSWkvrYlG1BAGDyy1XHdx_OT0B2HEQAo_CF2I6-rkED1184RqBhvvhjgkOkjqSNU5_ho4Jrlci8D9lH_NhARC-gUrsQVwTe9tQMxigIi6HzEZjFkXj6wJG625TxhqIi1rSF0hzns8al4kcpRTmmk_XxRIRrZaBfyNPkVRRQXHHNVSGwdm_uecxvjacIYRqONGjDHT506zMCFBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">60 دلار کریدیت رایگان برای استفاده از API بهترین مدل های جهان
💥
🆓
این سایت 50 دلار + 10 دلار هدیه رفرال و هر روز 5 دلار بهتون میده تا بتونید از بهترین مدل ها استفاده کنید
✅
Opus 5 | Fable 5 | GLM 5.3 | Kimi K3 | Qwen 3.8 max | Grok 4.5 | Deepseek V4 Flash
✅
✨
مراحل دریافت:
1️⃣
ابتدا در
این سرور دیسکورد
جوین بشید
2️⃣
حالا در
این سایت
با اکانت گیتهاب ثبت نام کنید
3️⃣
حالا سایت رو به اکانت دیسکورد خود متصل کنید
تمام حالا برید
از این بخش
کلید بگیرید و استفاده کنید ، همچنین به بخش پروفایل برید و 5 دلار امروز رو دریافت کنید
🎉
📌
Base URL :
https://tokengate-cqt9ivzs.manus.space/v1
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7523" target="_blank">📅 16:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7522">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دو سایت عالی برای گرفتن دامنه رایگان یک‌ساله
🎁
با این دو سایت می‌تونید کاملاً رایگان دامنه بگیرید، فقط کافیه مراحل زیر رو دنبال کنید
👇
━━━━━━━━━━━━━━━━━━━━
سایت اول (ساده و سریع)
✅
🔺
دامنه‌های قابل دریافت:
de5.net
–
cc.cd
–
bot.cd
–
bbroot.com
–
ddns.ge
–
l.cd
–
ccwu.cc
📝
مراحل:
1.
وارد لینک ثبت‌نام بشید
2. یک اکانت بسازید
3. تا ۳ دامنه رایگان می‌تونید دریافت کنید
🎉
━━━━━━━━━━━━━━━━━━━━
سایت دوم (کمی زمان‌بر )
⚙️
🔺
دامنه‌های قابل دریافت:
indevs.in
–
sryze.cc
–
ryzedns.org
–
nx.kg
–
ryzn.pro
📝
مراحل به ترتیب:
1️⃣
وارد سایت بشید
و با اکانت گیت‌هاب (GitHub) لاگین کنید
⚠️
نکته مهم:
اکانت گیت‌هاب شما باید حداقل ۱ ماه از تاریخ ساختش گذشته باشه
2️⃣
بعد از ورود، یک کد QR نمایش داده میشه
اپ Google Authenticator رو باز کنید و این QR رو اسکن کنید
3️⃣
کدی که اپ بهتون میده رو داخل سایت وارد کنید
4️⃣
به این بخش برید
و روی گزینه Repo Star بزنید و برید به ریپازیتوری گیت‌هاب اونها
⭐️
بدید
5️⃣
در آخر روی گزینه Verify کلیک کنید
🎉
تبریک! حالا می‌تونید از هر ۵ دامنه، یکی رو انتخاب و دریافت کنید (در مجموع ۵ دامنه رایگان)
━━━━━━━━━━━━━━━━━━━━
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7521">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plZQY0IeU37IPDpS9N76WL_s2OodHt47Ua4wE3C9m9kTFVi1Ey89vHcDD4-MtdWSSUo1E8sTHGV7jD_yXr-aGYxUO4_yjrEU8NhuF_Wq2qv7lM4Xzri105QyQoiZLd6lMShhBiJAX0kfX3Vhe78LIRu2_MAJuhZ-G2DsHK_VYLSZ8E0ZGEed2i8oEyE1aDQDYXfmZrRObcrd9TJQ-1yzkKKM-0xKNAfKz6BtOCaKUv3BmzqOR58ZEl4TMfabZk-RV6DfIZ9KxGznOqXuOH0RCo5hRNG-qCnoFOKp9gRtj-_jVrWWsOMlPL720dzOGEsuRuOg5FBUYr9dVVo0is88qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون توکن رایگان هر روز تو xkiro
🔥
مدل‌های
Qwen
،
DeepSeek
و
Grok
4.6
رو بدون نیاز به کارت بانکی امتحان کن
😤
برو
x
kiro.com
،
ثبت‌نام
کن، پلن
رایگان
رو انتخاب کن و کلید
API
بساز
🔻
هم می‌تونی مستقیم از
API
استفاده کنی، هم بعد از ثبت‌نام با اکانت
تلگرامت
احراز هویت
کنی و 5
دلار
اعتبار هدیه بگیری
🎁
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7519" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7518">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJh-TdYtCLU750aIUo2q6f_QOl8QxUM7PvVkSG1oPZugFzF2ruoAorhjFe0GHdRFWhj2czH6YHe1dS1RyZzE9x47k9XDo4pC1w0hVjSx2iaNBXEIN1pImykf0IAh4Gom4iAMVV7lVrdBD1kgbaXzKVfr5HUu9juGr2Tn9_OUn2QqWkmVyelgTdWaaLpHnb3-A-8whxxWI9TanwyF1EGJM1Kw3WehylsxygyA0I6mD0pWWpdteT5w0CSB4oH8gVpwFntSmxEOVFyAhutjCFLgDhTbI3lIeQ6G95pSSQAYpAoGpyLzvlfEWD30QWDR5ZTTafTJZnZps2y7Mma6kNlX9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به برترین مدل های هوش منصوعی
💥
🆓
Kimi K3 | Qwen 3.8 max |  Gemini 3.7 flash | Sonnet 5 | GPT 5.6 Terra | Deepseek V4 Pro 0813 | Deepseek V4 Flash 0713 | Gemini 3 pro image
✅
با این سایت میتونید به کلی مدل قدیمی و جدید دسترسی پیدا کنید این سایت هر روز به شما 100k کریدیت میده
✅
📌
Base URL:
https://api.anyapi.ai/v1
🔗
لینک ثبت نام
🔗
لینک گرفتن کلید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7517">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مدل قدرتمند
Qwen 3.8
با ۲۷ میلیارد پارامتر الان رایگان روی پلتفرم آزمایشی هتزنر در دسترسه
☑️
اگه اکانت
هتزنر
دارید، فقط
API
رو بردارید و به هر ابزاری که با
OpenAI
سازگاره وصل کنید دیگه لازم نیست پول بدید
🆓
مستندات کامل اینجاست
➡️
experiments.hetzner.com/docs/inference
اگه کسی بلده چطور راحت‌تر اکانت بسازه یا ترفندی داره، لطفاً اینجا بگه تا همه بتونن استفاده کنن
🤝
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7517" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7514">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/At2w6SgUQCaLCQlWlDBM5nFoNh2B9N8qSnGNkSNFCBrsqPxF3AAx1CkZDzZ4k6HL6DTzd6CBbNQexod9jDCSJyKc4cyMwAZxAGdBNKyPj_jQeuAfD7rCAwon8NOHaS0gvnZH4n8qxaKwjVCpWOQZ6n7PTxTjQzXL7VKN5OaqLc-x2LKhXTSHyBn9zOm-4sBAtj-Y2Khq8C8ejRGE_cozd_DBbtOo1rh9AN0F_UseWS9o9yNq8VYXezoYW2lmZ6i9dDD9Hf8wrbjOzK5RFj_MLqBV1H2-g_bMj-KVRsB0qI9vcoz6N57kx14-D6dpfjFykX5qCzd9wEyzcnrrQzxxaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2gvcgvKanqpN-ULEZVKud3d0TXvFVWiYr8FPEVPPzr_rNnMpAatSDybze36D285Q8V3dS9BaJ_3TepfS1W2obZdgv0irBuEYIUu42gGn1TjCWuhhUuOllZfZlmQo0A-Wd5XtukN0mtNczIpouaYWij3z6StAYOZBFDDcwUL2gY-MLixKiGeIl_PbXPvYbqhUEvHC0uq66Js8C5IuR-EI228cPtFzFyxbfFo4cjVelEKTNlFSkHujlTx1iy97fKJx0j8gyCVS0kmC9E1eDb225hZqlwGzzk21Y-Y715olHhtc1a4avfzoE2wmQl83tr9fMvgVrGz_SyqvddMgLuJpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت دامنه رایگان مادام‌العمر
💥
🆓
با این سایت یک ساب دامنه روی دامنه‌ی
kdns.fr
رو به صورت دائمی و رایگان دریافت میکنید همچنين میتونید اون رو به کلودفلر اضافه کنید
✅
✨
مراحل دریافت:
1️⃣
وارد
این سایت
بشید و ثبت نام کنید
2️⃣
به بخش
My Domains
برید
3️⃣
روی Order a domain بزنید و دامنه خودتون رو بگیرید
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=Tqyj0Yl8EM_a6XXsVWVYsfGssnrn9FFgmpPlgiz03XHLq-1a3o8_a9F7DdF-WFTw-pfw2MBn8XTFfoCL9aysnnd1gEiKXdg6xpqXEC_qRZoHzh0_rvjsDKEze-HhzNkTm07tqWK-LftDAomVKWJOxiDvJjwWaHBIB3Rg4xT9mkX2CpGdd0KimHmkLPp4o0k0lsG7x_beNzoobu6fPKTDsVrt7jJjoVA_zsWDRH13NM15cFC-1AVHrIKCtc_3Y5znW3snA2a_ADB3eJ7bxKT1m9u_atfHoKE8hCDBBjcBgMaX4fmX0VMQo5ZYibjwCP7ncJQicSUd6_9q_8qS29s6pYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=Tqyj0Yl8EM_a6XXsVWVYsfGssnrn9FFgmpPlgiz03XHLq-1a3o8_a9F7DdF-WFTw-pfw2MBn8XTFfoCL9aysnnd1gEiKXdg6xpqXEC_qRZoHzh0_rvjsDKEze-HhzNkTm07tqWK-LftDAomVKWJOxiDvJjwWaHBIB3Rg4xT9mkX2CpGdd0KimHmkLPp4o0k0lsG7x_beNzoobu6fPKTDsVrt7jJjoVA_zsWDRH13NM15cFC-1AVHrIKCtc_3Y5znW3snA2a_ADB3eJ7bxKT1m9u_atfHoKE8hCDBBjcBgMaX4fmX0VMQo5ZYibjwCP7ncJQicSUd6_9q_8qS29s6pYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
📱
وایب‌کدینگ حالا رو گوشیته!
ابزار HAPI اومده که به‌جای جایگزین کردن ایجنت‌های کدنویسی، همون‌هایی که روی سیستمت داری رو مستقیم از موبایل کنترل می‌کنی
🔥
سازگار با Claude Code، Codex، Cursor Agent، Grok Build، OpenCode و چندتای دیگه
✅
🎙
کنترل با دستور صوتی، بدون نیاز به تایپ
📂
دسترسی به ترمینال، چک فایل‌ها و اعمال تغییرات — همه از گوشی
💻
سشنی که روی کامپیوتر شروع کردی رو بدون قطعی و از صفر شروع کردن، رو موبایل ادامه بده
🔔
تایید هر درخواست هوش مصنوعی فقط با یه تپ، حتی وقتی پشت سیستم نیستی
🤖
حتی از تلگرام هم قابل کنترله
نکته‌ی جالب: HAPI کاملاً local-first و متن‌بازه (AGPL-3.0) — یعنی داده‌هات روی سیستم خودت می‌مونه و به سرور خارجی آپلود نمیشه.
✨
🔗
لینک سایت برای دسترسی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7512" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7511">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الان سه تا مدل قوی رو می‌تونید کاملاً رایگان تست کنید
🆓
برید سایت زیر ثبت نام کنید و به راحتی از مدل های زیر استفاده کنید
✅
✔️
مدل‌ها:
•
z-ai/glm-5.3-free
• dots-studio/dots3-note-prev
• deepseek/deepseek-v4-flash-free
🧾
Link
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7511" target="_blank">📅 09:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7509">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تلگرام برای دریافت پسوند دامنه .gram درخواست داده است
🉐
اگر این درخواست از سوی ICANN تأیید شود، بیش از یک میلیارد کاربر تلگرام می‌توانند دامنه سطح دوم اختصاصی خود را داشته باشند
💎
مثلاً
@durov
می‌تواند durov.gram و
@monk
می‌تواند monk.gram را ثبت کند
☑️
علاوه بر این، کاربران فقط با نوشتن یک
پرامپت ساده،
وب‌سایت‌های تعاملی خود را مستقیماً روی زیرساخت تلگرام راه‌اندازی خواهند کرد
🤯
🚀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7509" target="_blank">📅 22:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7508">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0OO9QPou4OT9_enZIxFqNT4KBH6xnvdUqJnDhi7LFemiitdAq4zMmDu7o9UlSY2hSwgzDc0H5TcwBsSyVZHzGnAOYv7z5rtp4C79wM7Lpz3k4VxU-1WOm0cxL5L8R0-mGZSgeH_YmSFoeIe-RvICJHausfIE7TyIzR6DatXcjXGEX_aEvAyomv01hNWj_mPB-Sl1GhbZq8O7eEypUkX5vHpUBrZ46ftis02ZKJ-GSUfGrpV0XJK9dg7tPsdF7MIiB41zPSaB4Vm3X3GW6y2VWcfUzVFDGNiPpWn0GkOIOpg-OnCw0c_nSWdtPpMGjupJoGYqqoi59CBpvdionAtug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلود کد ابزار قدرتمند طراحی گرفت
🎨
تیم Anthropic به عامل هوشمند خود قابلیت جدیدی برای طراحی رابط کاربری وب‌سایت‌ها و اپلیکیشن‌های موبایل داده است. کافی‌ست دستور /design را وارد کنید و تغییرات موردنظرتان را توضیح دهید.
🔥
سیستم به‌صورت خودکار کدبیس موجود را می‌خواند، خودش را با سبک طراحی فعلی تطبیق می‌دهد و پیش‌نویس‌های متعددی را در قالب طرح (artboard) تولید می‌کند که می‌توانید به‌صورت آرتیفکت به‌اشتراک بگذارید  (The Decoder) . کافی‌ست طرح موردعلاقه‌تان را انتخاب و ویرایش کنید، سپس آن را وارد فاز کدنویسی کنید.
✨
این ویژگی هم‌اکنون به‌صورت پیش‌نمایش اولیه در دسترس است  (The Decoder) ؛ برای امتحان کردنش کافی‌ست دستور claude update را اجرا کنید.
✅
🔗
لینک دیدن جزئیات
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7508" target="_blank">📅 20:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7506">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تست کردن مدل‌های هوش مصنوعی
🚀
حتماً براتون این سوال پیش اومده که مدل هوش مصنوعی‌ای که از یک سایت دریافت می‌کنید، چقدر به مدل واقعی نزدیکه؟
🧐
آیا واقعاً همون مدلی رو که ادعا می‌شه دریافت می‌کنید، یا یک نسخه‌ی ضعیف‌تر و متفاوت؟
👀
✨
توی این پست، ۲ سایت معتبر رو بهتون معرفی می‌کنیم که باهاشون می‌تونید مدل رو تست کنید و خودتون نتیجه رو بسنجید
🔗
لینک سایت اول
🔗
لینک سایت دوم
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7506" target="_blank">📅 18:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7505">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q25XmwL0SZtT7KBPNZqAocHCIBlYdyGuW0BA5JDubHk7OCH9N-2OmCj-gMFeXBuElwqTFZAiqWFVsqiXZ90UoeIFzn7eZrDhFPd_XTcrxDMUBUupFRJcYrXJYafdxCcsPoyo9LaTAVMLQ4i-vR7qgUM1cpZYSEmhdYOqnDJUN5mD_D7GC6dQTBS0auMgT_i9SYRrCQRFpKrEVrOhhJSkLvtgP54pwn0szdL438qHLLnkn25UPPXqq8FVNvSaUTb8mZy3LywmnhlPOWhjGRHFuCUup1vLSWovayTvIOoYqVa8xXd__gfrR1-_DuSD_U5OyzsXnDsGUZ0M6KVe49QF5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL :
https://api.b.ai/v1
📌
Model ID :
deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7505" target="_blank">📅 16:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7504">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aww2s4ZGuZCpiV-TTDodsnLI5n8-C3MC2nuAoaBj0ETAcTKLPyIh9x5rSKHzHE_G8vbD1xifdFP7IBc5s9xNjZnN8xjjig9nvrj_Uo_uQwc2YqRFiorQp3-jWXCNy4LbkI5beA2-B7cADDJMrXZohXBlevuXrbp2J2RPEeyvn0YH_FZGpipR9ZNiJwzzHrSxE7kQn4vit3WA7pk18c216MCb0rjOdTT8iJDuls0UwrTml6dkX65crns3WQRGGahVhkA9MLAqbadGl40GPac5WGFbUb1vzHrBGjtwKnIHDUwRn9IgtX3Gl9Xl5YAneunSd3JyvTjj9loGYSoIpUrfDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.2 الان روی OpenRouter رایگانه
💥
🆓
هوش مصنوعی GLM 5.2 یک مدل Reasoning قدرتمند برای برنامه‌نویسی، AI Agent ها و اتوماسیون پیچیده‌ست. نسخه رایگانش در اینجا با 128k Context عرضه شده و از طریق مرورگر یا API سازگار با OpenAI در دسترسه.
✅
❗️
از مدل z-ai/glm-5.2:free استفاده کنید — بدون پسوند :free نسخه پولی اجرا می‌شه.
⚠️
محدودیت اکانت رایگان حدود ۵۰ درخواست در روزه
🔗
لینک دسترسی
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/ArchiveTell/7504" target="_blank">📅 13:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7503">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هدیه ویژه برای شما
🎁
3 هزار دلار کریدیت رایگان در این کلید قرار داره ، شما میتونید همین الان کلید رو در هرجایی دوست دارید استفاده کنید
💵
🆓
🔺
Api keys:
sk-IXNxrDiaLV2vNxU73TC0Y4zSW1uPrXj0a24SxG8LbD4TYkfp
🔺
Base URL:
https://tabitoken.com/v1
🔺
Model ID: claude-opus-5
ری اکشن فراموش نشه
❤️
توی کامنتای پست چندتا کلید دیگه هم گذاشتم واستون
✅
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7503" target="_blank">📅 11:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7502">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ss2rz_MXJ6Gasn07A2FdYDguAYj6X73tfYAKD_NmzF3Rift0QGYBoVdbCf4cSNYW1ifDBAtN-Q5eOgdsKsSexFO29S7jsCJlGJABkuDmxRoqHKkaaMGW2S3hUvDy3I6Zw-UgNU-pxXP3bwvtytyGUlnpGXLDUadELr5eAHVZoKQDnlXWZBhK9lkeVVG4tg7WyVEdqY6LU7g7AQCxpRlE_mmmsaUf6wfd8gFYhdk7CcWbHgFbsxKfsKZbF7x9keuG-1VxYeoW0or4QUWHtHn5vjxf0iBIOxUTtzBxx0V7rSSL3fqgm0SZ_q-r52fASvL2vM9z0RZp3IaXxy2hUCFb7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4 Pro 0813 و Qwen 3.8 max به صورت رایگان
💥
🆓
این دو مدل در این سایت به مدت محدود به صورت کاملا رایگان و فقط از طریق API در دسترس هستن
✅
📌
Base URL :
https://api.tokenrouter.com/v1
📌
Model ID :
deepseek/deepseek-v4-pro-0813-free
|
qwen/qwen3.8-max-free
⭕️
محدودیت ایی در میزان استفاده وجود نداره اما به دلیل شلوغی بسیار زیاد سایت مدل ها کند هستن،  پس باید در تایم خلوت استفاده کرد
🔗
لینک دسترسی
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7502" target="_blank">📅 10:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7500">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=DrTygcHZt56gbhsYl2Bbl27eQE4evBDQjkcD4WeU9Cw_7T00VD5WNgItsqpAAsbbo2FhVLwaHe_EcX_ykiuQu3L-SQgaS2Q5yh6u0IC4cxi4BdOuFHiKcUQo-zT3GWL9ZsK9DaBUxTm903MpVP7PPIGXqW_CdhR-pwKctYGevtjmsH1bgkRUU0bFuxf1wjo4vJd05FLDVuC8RpghVqNjHW5i702SSmHo3B0VcQjl_qMZX6WxOjOwcrqx-YeoNZBUO9qoAy78orLo04wDRkoQAYUisDFaYfPCKSzdczENdsogrQOwWrLOzldLE578oykYKjpCol6j1SXUJ1vpTwwORw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=DrTygcHZt56gbhsYl2Bbl27eQE4evBDQjkcD4WeU9Cw_7T00VD5WNgItsqpAAsbbo2FhVLwaHe_EcX_ykiuQu3L-SQgaS2Q5yh6u0IC4cxi4BdOuFHiKcUQo-zT3GWL9ZsK9DaBUxTm903MpVP7PPIGXqW_CdhR-pwKctYGevtjmsH1bgkRUU0bFuxf1wjo4vJd05FLDVuC8RpghVqNjHW5i702SSmHo3B0VcQjl_qMZX6WxOjOwcrqx-YeoNZBUO9qoAy78orLo04wDRkoQAYUisDFaYfPCKSzdczENdsogrQOwWrLOzldLE578oykYKjpCol6j1SXUJ1vpTwwORw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎧
این اپ کنترل موزیک رو مستقیم به تسک‌بار ویندوز میاره
ما FluentFlyout رو پیدا کردیم — اپلیکیشن رایگان و متن‌بازی که پنل کنترل موزیک رو دقیقاً روی Taskbar ویندوز ۱۱ نصب می‌کنه. کاور آلبوم، Play/Pause، Seek، تعویض ترک، Repeat و Shuffle، همه یک کلیک اونورترن.
🎶
با Spotify کامل کار می‌کنه
💻
با Windows Media Player کامل کار می‌کنه
🖥
با مرورگرهای Chromium و Firefox هم کار می‌کنه (بدون Shuffle/Repeat)
🎬
با VLC هم کار می‌کنه (ممکنه Plugin لازم داشته باشه)
⌨️
با هر پلیری که از SMTC ویندوز پشتیبانی کنه سازگاره
سبک، حدود ۵۰ تا ۲۰۰ مگابایت RAM مصرف می‌کنه و عملاً مصرف CPU نداره.
✅
🔗
لینک سایت برای دسترسی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7500" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7499">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj401FDEmbmG-pr4o0kRIdDWLLObKkI-bz47Z1vEE20Do2yMRcXyXjSG9G_-e2nzGEu0AohhyQ1OCfxr0Bt5d4fmcbcc2txzhT6ff1a9D2nVYR1v6tB4yiar62IEeRTiuQfwkJJAZ6dEcwl2gnTPaUOM9CAG2ZYAsTOfp8Cpb2r8rdM1mXPedIcOJkovTQfuyxpqmxz7yt3dpQC0XYNjJsJwgSmlV1os7UbOL3hO9KxSuUOaAS55wbVQepA5nw7SHE7UxemYT4DhXyNg5uhBOl70sA5RoJUg1VhNzQ7im9Av4wP4WlNK3QWi2nucsw_KhnBBejHtIyrLT-K7stHe1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
این ابزار خط‌فرمان، یوتیوب رو مستقیم توی ترمینال میاره
ما ytsurf رو پیدا کردیم — یک CLI رایگان و متن‌باز که ویدیوهای یوتیوب رو تمیز و بدون حواس‌پرتی مستقیم توی Terminal پخش می‌کنه.
✅
👥
قابلیت تماشای مشترک با Syncplay
🎶
پخش و دانلود فقط صدا (Audio-only)
📥
دانلود ویدیو یا صوت با یک دستور
📌
انتخاب تعاملی Format و Quality هنگام پخش یا دانلود
📃
تاریخچه پخش با امکان تماشای سریع مجدد
📂
تنظیم مسیر دلخواه برای دانلودها
🔄
بررسی خودکار آپدیت برای نصب‌های Manual
📺
پشتیبانی از Subscription کانال و Feed شخصی‌سازی‌شده
⚙️
نیاز به چند Dependency داره: yt-dlp، mpv، fzf، jq، curl، ffmpeg، chafa. روی Arch (AUR)، Homebrew و NixOS هم قابل نصبه.
🔗
لینک پروژه گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7499" target="_blank">📅 22:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7498">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=ttXyS9IvEfs-23B8xmDjQ6Hgp-gzJRLPb1jc3RUY0LJZ0MxskypkauOVdOIk5CZn1NlnPm8xoVBf1KBywTA66up0K0AnJ8fgZCKNDzthAp-t6tyMoWJ8EPLy2phT1-XK6vL-ggVtQBGDRnodLvAx7Do5PngagmvnFPFsD3iZV44mKhUkhmX9zqYjdxUh9qsSNKTkLz5-6iO2ktllq8cqmNWZ-YGgeGs5HGcHQJBGEvt9vHcI_NJVbzv7Hvqv9xI8uo3X0KnjOsJaVRDFjl2bkgVT0N6qIkDu1GX8eIKHrj-CdgNgcdDXvhRmifvVj_rea3RoDEdWWQ-u9kza5to4yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=ttXyS9IvEfs-23B8xmDjQ6Hgp-gzJRLPb1jc3RUY0LJZ0MxskypkauOVdOIk5CZn1NlnPm8xoVBf1KBywTA66up0K0AnJ8fgZCKNDzthAp-t6tyMoWJ8EPLy2phT1-XK6vL-ggVtQBGDRnodLvAx7Do5PngagmvnFPFsD3iZV44mKhUkhmX9zqYjdxUh9qsSNKTkLz5-6iO2ktllq8cqmNWZ-YGgeGs5HGcHQJBGEvt9vHcI_NJVbzv7Hvqv9xI8uo3X0KnjOsJaVRDFjl2bkgVT0N6qIkDu1GX8eIKHrj-CdgNgcdDXvhRmifvVj_rea3RoDEdWWQ-u9kza5to4yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پرامپت هر ریپازیتوری رو به یک نقشه سه‌بعدی تعاملی تبدیل می‌کنه
🚀
بده به Claude تا یک شمای ایزومتریک از پروژ با Dependency ها، مسیر داده‌ها، و توضیحات کامل بگیری
💥
📐
معماری رو مثل یک شهر سه‌بعدی روی Grid می‌سازه
🏢
هر بخش از Infrastructure = یک ساختمان با شکل متفاوت
↔
مسیر Control و Data رو دقیق دنبال می‌کنه
📄
به فایل‌های واقعی Reference می‌ده
✍️
پرامپت:
Analyze [لینک ریپو] at latest main. Create an isometric system map with legend and explainer panel. Show infrastructure as varied 3D buildings on a grid, with dependencies and payloads tracing real control/data paths. Cite files.
✈️
@ArchiveTell
|
#PROMPT</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7498" target="_blank">📅 22:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7497">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vkw6w8HGpGpezvWheN1vYzg3TpKUo_-jSJ_ocGpVt_Dng2KXZUi5GHLW3O0tBk8atV_awuvCsQmK1KVmFHsuhgTnZlXFoW8jqhGqVTJPEXs-J-033xtTo30CA79R5t5QxyYfkRt0EstZoBkMUWpQZmGblNTbQTu51zycJfLnCB_tRUeyavnskRWGLPYHAFyD9t81WMj88pi-3xOg7XxueHi7AJiPj6Tlt7kdzMJ_JXMgM8bl8UivyInX3zVdIEOOVcT04APAj80KO0Tmj4KRCKhPWbphfOuyU6OsaDLAIim6c-hhXbYc2lF48D6QWm8Mfccjj6W4-biqua-FCmVyDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧹
این ابزار متن‌باز، ردپای AI رو از فایل‌های شما پاک می‌کنه
ما watermarks-remover رو پیدا کردیم — یک Agent Skill به‌همراه یک سرویس رایگان که Watermark و اطلاعات پنهان تولیدشده توسط مدل‌های AI رو از فایل‌های مختلف حذف می‌کنه.
✅
📄
ده‌ها فرمت رو پوشش می‌ده:
PNG، JPEG، SVG، PDF، DOCX، ODT، HTML، Markdown
🔡
کاراکترهای مخفی Unicode و ردپای متنی AI رو پاک می‌کنه
🖼
متادیتای C2PA/EXIF/XMP رو از فایل‌ها می‌زداید
⚙️
کاملاً متن‌باز و رایگان، با پشتیبانی از Claude، Gemini/SynthID، OpenAI و مدل‌های Open-Source
🔗
لینک پروژه گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7497" target="_blank">📅 19:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7496">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfB_rxGdawb-JJcJrI05mLEnzTPu1arIfC6vXjAqHVcMSPYZeCc5FWXWppi732eRxw5wpa2NdiQ_iCHqzfiL5KV-o42pVj0LfzmTMz2P4cd1Cw67GiQNNJKqyKXx0KgwkGZcRSIAsWrISQs_qN47L3v5mi9tW0cRjfePTSHquBx8KJnKakZ9TMRSNWJqkWUN9sqWIrylwDjXoibJyNEXT8R95CM58lOJDT6WGu4guoXWyTY7m7GyJFkLv7xUUwc-VspuTiARGkyrGK6H-sQPVgvRFRC6G4fBcjdOvzkiX7IicnZjBdnbaTgtcSYYNlYFuUGXYk4RXJeY6pqUcuDekQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به برترین مدل های جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Grok 4.6 | Kimi k3 | Qwen 3.8 Max | Deepseek V4 Flash | GPT image 2 | Seedance 2.5
✅
این سایت بهتون 5 دلار به مدت 7 روز میده تا بتونید از این مدل ها استفاده کنید
💵
یکی از بزرگترین فرق های این سایت اینه که مصرف مدل ها به شدت پایینه و کریدیت خیلی کمی رو کم میکنه
✅
📌
Base URL :
https://heyroute.ai/v1
🔗
لینک ثبت‌نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7496" target="_blank">📅 17:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7495">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=N2dCeLpus4FhnAz1i3bIfx5l-caCVGZkOYGP8CXU3TWx4u7eVYKKABsESJvq3fwFUwwPp9S31nY2DuUBgPoeFYC3R645yHVCBbMZb8DAaPLhnMCZRVomuQNVOxbYRtMF2MVsln_VJvT6pREIGxjTUfoLlhulqn4-2jkF1TBjlSEF4W22Nv8IstdKhsbnslwKiTDL_Av9XCCBq01H0x7Wbdq1S52lNCa4LTMtM6MpFPjHZaPer8M1UTdjHXa2V2apS-Ua9q9cq_CitTl8TvG4i-s7dQ9qcS05moslwLRBDnSWk1wLOlZDUb9yl2FjzZWzEXGvz9--_XxgzThC3cpR5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=N2dCeLpus4FhnAz1i3bIfx5l-caCVGZkOYGP8CXU3TWx4u7eVYKKABsESJvq3fwFUwwPp9S31nY2DuUBgPoeFYC3R645yHVCBbMZb8DAaPLhnMCZRVomuQNVOxbYRtMF2MVsln_VJvT6pREIGxjTUfoLlhulqn4-2jkF1TBjlSEF4W22Nv8IstdKhsbnslwKiTDL_Av9XCCBq01H0x7Wbdq1S52lNCa4LTMtM6MpFPjHZaPer8M1UTdjHXa2V2apS-Ua9q9cq_CitTl8TvG4i-s7dQ9qcS05moslwLRBDnSWk1wLOlZDUb9yl2FjzZWzEXGvz9--_XxgzThC3cpR5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پرامپت، کل معماری پروژه‌ت رو نقشه‌برداری می‌کنه
🚀
پرامپت رو بده به Claude، بذار کل Repository رو بخونه، دو تا خروجی حرفه‌ای تحویل بگیر:
⚡
کل کدبیس رو تحلیل می‌کنه
🔗
ارتباط بین فایل‌ها و کامپوننت‌ها رو کشف می‌کنه
🗺
معماری رو به‌صورت دیاگرام تعاملی می‌سازه
🧭
مسیر کامل هر Flow رو ترسیم می‌کنه
💬
برای هر Component یک Tooltip توضیحی می‌سازه
📤
خروجی:
🖥
فایل HTML مستقل
دیاگرام تعاملی با Node و Connection، پنل Flow کنار صفحه، کلیک روی هر Flow → Highlight مسیر کامل، طراحی تمیز و Responsive
🧬
فایل JSON برای AI Agent ها
ساختار: { nodes, edges, flows: [{ steps }] }
مخصوص Agent هایی که باید معماری پروژه رو بفهمن
✍️
پرامپت:
Analyze my entire code repository thoroughly.
Generate TWO ready-to-use deliverables:
1. A single self-contained HTML file containing:
• An interactive architecture diagram (nodes + connections)
• A flow panel on the right
• When a flow is clicked, highlight the complete path
• Tooltips for each component
• A clean, professional, and responsive design
2. A JSON with the structure:
"{nodes, edges, flows: [{steps}]}"
The JSON should be specifically designed for AI agents to understand and navigate the project architecture.
✈️
@ArchiveTell
|
#PROMPT</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7495" target="_blank">📅 15:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7494">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eP6gKKsaSWF-yBgMQvbvM6pIqLCiJWHMsmjJa0F3jq0EWS2niCYyV8EWYIgh-rE9qXZMJG4L_spBKcSyKSu3fody9lccPUh-oOAqVe1HoM5_0qJ6dSfmAEerx8qiUGiAUpobSb49Ch9TKwu-IbOLDUSiZMV6g-tYJtE93UYVKt96B-4NNyAeE_36JIpDWs9stg-lgSOh7PGEllsMHOUShh-VPUKhcfm377KvOJ-V6sViITwipSmDxWQh0j8e6Z_R1Xqa5bY4O4_8zSS25fXI0ZEKWWOcNWTCseifZfzywFe0jX4Ibior7tqRM09EAMq1J2PqLnCspsXgwvtT6SOv3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی رو به یک ایجنت هوش مصنوعی تبدیل کنید!
🚀
دیپ‌سیک با معرفی DeepSeek Harness یک محیط جدید برای ساخت و اجرای AI Agent ها راه‌اندازی کرده؛ پروژه‌ای که خیلی سریع مورد توجه جامعه اوپن‌سورس قرار گرفته.
🔥
💡
ایده اصلی Harness چیه؟
تقریباً هر چیزی می‌تونه به‌عنوان یک Plugin وارد سیستم بشه؛ از مدل‌های هوش مصنوعی و Sessionها گرفته تا Skillها، Sandboxها، چرخه‌های اجرای Agent و حتی رابط کاربری.
⚙️
معماری Harness بر پایه‌ی Cordis طراحی شده و این امکان رو می‌ده که کامپوننت‌های مختلف حتی در زمان اجرای Agent هم تغییر کنن.
💥
چیزی که Harness رو جذاب کرده اینه که محدود به یک مدل یا ساختار خاص نیست؛ می‌تونید اجزای مختلف رو با هم ترکیب کنید و Agent موردنیازتون رو بسازید.
🧩
حتی جامعه‌ی توسعه‌دهندگان هم دست به کار شده و هزاران Skill آماده برای Harness ساخته شده که می‌تونید ازشون استفاده کنید.
📌
خلاصه اینکه DeepSeek داره یک رویکرد متفاوت برای ساخت AI Agentهای ماژولار و قابل توسعه ارائه می‌ده؛ چیزی که می‌تونه برای دنیای کدنویسی و Agentها خیلی مهم باشه.
🔗
لینک گیتهاب پروژه
🔗
لینک سایت پروژه
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7494" target="_blank">📅 13:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7493">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIFvpmgEDeZSWx7xOnM4La014J5rb1JRtyL-FzPrf-pbji6cR6ZcZKwlma3hlkaq0r7eyNTJthUNLbLIoGINC0Sz8fUjpAXpp1le1xnx8d7QyOJyC-7l5e8v-VDCvnBLZu8jZ7QSSn9WFBuRkyx3706jdMedA-fBNQtwIYcSwGpP6MQQU6Utwkgiqmw3pRA6g9wo-LnlYVVTmcMTZJ0x3fKk2vJgOw3p86xfWh-87kCuqesXty9qNwedwEVYrLgklPOjBJmUKBlRt61NroSUY6Za0oboRTpYxv7T3vOOD4eUjgkK82fC0jVmaNfeYDPCBJopkV5umguQdRo_Ywvi1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست طلایی سرویس‌های رایگان برای برنامه‌نویس‌ها
🖥
سایت
free-for.dev
یه لیست
کامل و مرتب
از سرویس‌های
ابری
و
ابزارهایی‌ست
که پلن
رایگان
واقعی دارن (
نه فقط تریال چندروزه
)
🆓
از
دامنه
و
هاست رایگان
گرفته تا
دیتابیس
،
CI/CD
،
مانیتورینگ
،
ایمیل
،
ذخیره‌سازی
و
خیلی چیزای
دیگه
🔸
اگه دنبال
ابزار رایگان
برای
پروژه شخصی
یا
استارتاپت
می‌گردی، حتماً یه سر بهش بزن
💻
⭐️
Link
⭐️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7493" target="_blank">📅 12:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7492">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09dd417185.mp4?token=r-ak8soCDpWqxMjG9LOx9Cj1DCZ5buyuSBj7FEdyFgkZ9iMX6A_wh5rwzK2H2cZxL6ppUDVQ2cR2sLqS_hkCugxu--QCopB_w7dm0C4k0WAS8ZaGXXED5-8TduL2zyEHbcnxehdoTQgPZv0nwP26XCJYkYeGj3I5bYXCMoUHA32uhGLQ6meZt4zz8SZmb2netxRPZp2SKc9EAntR6fHB3EN87WfRklSTdyISzr9HKZEmQEpoeYAgboQKA01pum3cQPLuoFjOYMd5sh16HrEunHsDmOmMd46KkWw-79bJ7rG7KEsgcacukm77_Jndh9JsFmzX7eeNkTUbXIFnI0yUiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09dd417185.mp4?token=r-ak8soCDpWqxMjG9LOx9Cj1DCZ5buyuSBj7FEdyFgkZ9iMX6A_wh5rwzK2H2cZxL6ppUDVQ2cR2sLqS_hkCugxu--QCopB_w7dm0C4k0WAS8ZaGXXED5-8TduL2zyEHbcnxehdoTQgPZv0nwP26XCJYkYeGj3I5bYXCMoUHA32uhGLQ6meZt4zz8SZmb2netxRPZp2SKc9EAntR6fHB3EN87WfRklSTdyISzr9HKZEmQEpoeYAgboQKA01pum3cQPLuoFjOYMd5sh16HrEunHsDmOmMd46KkWw-79bJ7rG7KEsgcacukm77_Jndh9JsFmzX7eeNkTUbXIFnI0yUiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📝
♊️
گوگل هر ریپازیتوری رو به مستندات تعاملی تبدیل می‌کنه
گوگل ابزار جدیدی به نام CodeWiki معرفی کرده که با بررسی خودکار کدبیس، در چند دقیقه یک مستندات کامل و قابل‌فهم از پروژه می‌سازه.
🚀
🔺
ساخت خودکار دیاگرام و نقشه پروژه
🔺
توضیح بخش‌های مختلف کد و نحوه عملکردشون
🔺
تولید راهنما و آموزش مرحله‌به‌مرحله
🔺
تحلیل معماری و ارتباط بین وابستگی‌ها
🔺
ساخت یک چت‌بات آشنا با کل ریپازیتوری برای پاسخ به سوالات مربوط به کد
یعنی به‌جای ساعت‌ها گشتن بین فایل‌ها و کدها، می‌تونی پروژه رو خیلی سریع‌تر درک کنی.
👀
📌
این ابزار رو از دست نده!
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7492" target="_blank">📅 12:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7491">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQIz7soiAQm17rmAkrJ85hWRTwUQx5HJjCcllGxxD_a4RtZq36dgTjfwJ1TPRYGX8IyJU-Airp1pUjJpC7Dwv1higgmDReyCpHm1jAPCOz09JFiR57Z-umrAirz7scstlu0w3eHeZv5nYIWUI58-Qb_X6pS3t26PTzIbTYNkZ1xXf43GCRWGjYP1nvVAXwGo5ayXqzl1EafldxC-Dw0F4sMfSS6oSJAUTfc2FPEZ1CoAdf8tgos0Xed3o0lsgx17dNuLbL2mPHS0wmY1XZ8ULr2ri_W_2IvAR_TpI1djfCdrOuBHNZWw7JxiZlmRha7GT6rQC90HOf99LgDas8riow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">TorrentSearch
♻️
اپلیکیشن متن‌باز اندروید برای جستجوی همزمان تورنت از چندین منبع
📱
با
TorrentSearch
می‌تونی
خیلی سریع
از کلی
سایت
و
پرووایدر
مختلف جستجو کنی، نتایج رو فیلتر و مرتب کنی و مستقیم مگنت لینک یا فایل تورنت رو بگیری
⏬
امکانات اصلی
💭
جستجوی همزمان از چندین
پرووایدر
(قابل روشن/خاموش کردن جداگانه)
🎁
فیلتر بر اساس
دسته‌بندی
(فیلم، سریال، انیمه، بازی، کتاب و ...)
📁
نمایش تدریجی
نتایج
+
مرتب‌سازی
بر اساس سیدر، سایز، تاریخ و ...
🪣
جزئیات کامل هر
تورنت
+ صفحه جزئیات داخل خود
اپ
ℹ️
ذخیره
بوک‌مارک
+ خروجی/ورودی گرفتن
🔖
حالت
Safe Mode
برای مخفی کردن محتوای
NSFW
🔞
پشتیبانی از
Jackett
/
Prowlarr
(
Torznab
)
🦾
طراحی مدرن
Material 3
و
دارک مود
🎨
⬇️
دانلود از گیت‌هاب یا F-Droid / IzzyOnDroid
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7491" target="_blank">📅 09:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7490">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⚡
پرامپت‌نویسی تغییر کرده؛ این ترفندهای قدیمی رو دور بریزید
بزرگ‌ترین دلیل جواب‌های پرت و توهمات هوش مصنوعی فقط یک چیزه:
وقتی جزئیات بهش ندید، جاهای خالی رو با حدس و گمان پر می‌کنه.
❌
ترفندهایی که دیگه منسوخ شدن:
•
نقش‌دادن‌های کلیشه‌ای:
نوشتن جملاتی مثل «تو یک متخصص ارشد با ۲۰ سال سابقه‌ای...» تاثیری در دقت نداره. مدل به فکت و داده نیاز داره، نه عنوان شغلی تخیلی.
•
تکیه به
Temperature = 0
:
صفر کردن دما جلوی اشتباه رو نمی‌گیره؛ فقط باعث می‌شه مدل خطایش رو با لحنی کاملاً جدی و بدون تغییر تکرار کنه.
•
پرامپت‌های ۳ صفحه‌ای برای تسک‌های عادی:
طومار نوشتن برای کارهای ساده، تمرکز مدل رو به‌هم می‌ریزه و احتمال نادیده گرفتن دستور اصلی رو بالا می‌بره.
✅
فرمول ۴ مرحله‌ای برای گرفتن بهترین خروجی:
۱. هدف دقیق (نه کلی‌گویی)
❌
نگو:
«این قرارداد رو بررسی کن.»
✅
بگو:
«این پیش‌نویس رو بخون و فقط بندهایی که بار مالی اضافه برای خریدار ایجاد می‌کنن رو پیدا کن.»
۲. بافتار و مخاطب (Context)
«مخاطب فردی بدون دانش حقوقیه؛ توضیحات رو کاملاً روان، ساده و بدون اصطلاحات پیچیده بنویس.»
۳. بستن راه حدس و توهم (خیلی مهم)
«اگر پاسخ یا عددی توی متن نیست، به هیچ وجه حدس نزن و صراحتاً بنویس: "اطلاعات در متن موجود نیست".»
۴. قالب مشخص برای خروجی
«پاسخ نهایی رو فقط در قالب یک جدول ۳ ستونه بده: [شماره بند | ریسک موجود | متن پیشنهادی جایگزین].»
💡
اصل ماجرا:
هوش مصنوعی ذهن‌خوان نیست. هرچقدر دامنه حدس‌زدن مدل رو محدودتر کنید، خروجی دقیق‌تر و کاربردی‌تری تحویل می‌گیرید.
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7490" target="_blank">📅 21:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7488">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGBHmTwpsn4MnHfcn8m38he_G4iBfMoAEKzFs9N621_IrAgU9iZhjA9Hu6I9Y9Uzr-eYekrd9LuWE7BaPm9GYkXrIND92VRYmWM-5Tdp3VQaCUM0_3fpiH5An5uFuci29Vh6tC73iSpUlY-2U88syrkFs7ReTT5UtFUOIpO2v-JHKhjNxkLTBz01F5NTVW_zSz8D_ZwYUxxqMlRXVK3pHJ1md5iS9aduFYwA0H5sSU50T5sNJRcUlvIExycKUYxjrxsu7m12lelUltwjJ5N5AtytubE91t3KWyJj2jwx8rjr7GbMauiAh8W6FqX98OgJ17J1Kt9fMy_IRQ-DifAPkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به برترین مدل های هوش منصوعی به صورت کاملا رایگان
💥
🆓
Sonnet 5 | GPT 5.6 Terra | Agnes 2.5 | Mimo 2.5 | Gpt image 2 | Nano banana 2
✅
📌
Base URL :
https://ai.furry.vg/v1
حتما در بخش انتخاب گروه ، گروه Free رو انتخاب کنید
‼️
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7488" target="_blank">📅 19:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7487">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPSKTf6ZPMo9ZRC1XMTVyKU6H5LWgq4asujV_0BN4nuGJBr-G8h7dICQpUQQL3A6o5EewFAeRXnRoHnExXbwbe6BkYeifuiETI1nzpcOYgw5IOrnWEg4X4upPIKsx02UwfiGz-jMyITwDj4zDwqIl7YJlMtHEMtImPZ4OcecYT8K9Gowg85LuqckOXNSUH1DCnu1Oe1weh_KiXFgtv-0OdmGMh5gk5e65XG2UjdRQphsFS79fWD8qtRJxLVy-Cb9oCvtD0vwZbN8g_j0ZoKpKFzTdwTeUD1YcRwwgUq8_y7_q1VagU3MoCvFp1pn6PDWLDPE3raMYjvqqy_T3VBZkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل Qwen 3.8
💥
🆓
با سایت Runinfra تا 48 ساعت آینده میتونید به API مدل Qwen 3.8 دسترسی رایگان داشته باشید
✅
📌
Base URL :
https://api.runinfra.ai/v1
📌
Model ID :
qwen3-8-27b
به دلیل شلوغی سایت ممکن است پاسخ مدل کند باشد
‼️
🔗
لینک دریافت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7487" target="_blank">📅 17:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7485">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jvro_KQwjoWKXrnc4jm0SGge7fvRAuDw-LjQxxL0I_2PHeF6f13k-6-rMcyOCO1e_DxwHkWORj6cmiedo-v02Rwp2ItsyOLtDOzRB-2Fdmg86u4400MIcXj2AAaVRxdN4XEeLW_uXQp_hKyT-ZsJe_8ytuoDhAvChmFWqnOUR1WunPmOrqdF9-jqtaXeEI_Md-S-G-D_REb--8-9BYbDXSfLhohZNX8ZBBAodb9I5_r6EfVM32ZyBhyCcPktMJpgen85NTkG47CXY6zJeOz4blYi_yhnF10LQgYaeCtJ2rmpDXmzBHaLuDc9LnpQ_szjFJZmvrCXL_qCR9O5mK8z1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های هوش منصوعی محبوب
💥
🆓
Qwen 3.8 max | Deepseek V4 Flash | Deepseek V4 Pro
✅
📌
Base URL :
https://api.orcarouter.ai/v1
🔗
لینک ثبت نام
🔗
لینک دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7485" target="_blank">📅 15:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7484">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxUoQ18boKDhE3YRMskVcNcao-d_ryOwrb0vlRKbZbgc01VsW9y-vpqr-yPxAMyGHmjlp2R5aPXIgGB6iIKX2bAEqY1VXTmW9jENYwj-jZ7KB9Pux3leb2SZIFGyMjacG59MUc1AOXYoCHNDYmi3M1Y6OweiIS5x1YMIrN7WZdMpZuR8IKboX4g-p9p53sh12htSlwJEZcM0_AOWbgehCl7ycWtJICFEniudak-0HU_VUxtVDyoLuM-siBqSYIstw5skLFGD8BUr3RI4ZIZExT-uGVe3EMJM7p44McNlZWMCTAcYV488dl0dgX5VdAgV0f9fkOXGbAW1X98TmyM37w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون توکن برای استفاده از GLM
💥
🆓
به مدت 5 روز هروز 3 میلیون توکن برای GLM 5.3 و 2 میلیون توکن برای GLM 5 Turbo برای کاربران جدید در اپیکیشن Zcode
✨
مراحل دریافت :
1️⃣
وارد سایت
z.ai
بشید و با اکانت جدید ثبت نام کنید
2️⃣
برنامه Zcode رو دانلود کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/ArchiveTell/7484" target="_blank">📅 12:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7483">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">هدیه ویژه برای شما
🎁
100 هزار دلار کریدیت رایگان در این کلید قرار داره ، شما میتونید همین الان کلید رو در هرجایی دوست دارید استفاده کنید
💵
🆓
🔺
Api keys:
sk-bY9B0parF18s5v1wasRyzRZsVLzICaSVfZNVEMrqG2Rlt7dH
🔺
Base URL:
https://ai.venlacy.com/v1
🔺
Model ID:
glm-5.2
به دلیل شلوغی ممکن است پاسخ ها کمی کند باشه
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7483" target="_blank">📅 17:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7482">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvLV0urgzwVhmyWHRG_Uq-YlUjxc-9LV4yJPEf2p3mVo2sXqWHutHd5_xyki7UxRLyCVpYDKwaXJUce0wmz5-gASnvdCsjOZoometAHDGFkh3JzLrb1swg30PWWFXy2IUnuYO_c49eo4nf-EPmKTT5i66sRNiEb2rgN5Bn1zxZuTsCA-Z1q_cFZaJWOxP9f6BM4Pc-xxru-xLhY2cdP4AjiGRscpWuuqe1aD_m5lf_N3bpi7aGwU6Ns9g092V_VYptJIzahh3YX_b4Lck_K4-Xuj2eEWHmcGEepXmvgaAh02sKVfbSNhNhRL0zDB9GwqnVFrwFkVwdp5y0aTnttGrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.3 رونمایی شد
🚀
نسخه جدید GLM با نتایج بسیار قدرتمند در بنچمارک‌ها عرضه شده و در چندین بخش از رقبا جلو زده است.
🔥
در مقایسه با مدل‌هایی مثل Kimi K3، DeepSeek V4 Pro، Qwen 3.8 Max، Opus 4.8 و GPT-5.6 Sol، GLM-5.3 در بخش‌های زیادی عملکرد بسیار رقابتی و حتی برتری دارد.
⚡️
🔗
دیدن اطلاعات بیشتر
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/ArchiveTell/7482" target="_blank">📅 23:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7481">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acg9WVXOSuxmdDoRDIfuec_ihO2-R0NtkA3FiF3W-CFs4BR-LwRaJXpOiETEysuZGkDo03gevDjUxMLlxpm4e2_4ghCphNlXGBUISJiPFWg6or_ihpgZAsd6R1ifS4O4ZFM7nmjf5KdScmq6CrWnUrh9bG8b0kuPSnlP6tS038AfYjCz9zeL4VkXX2uE1R4RSvr1-l3gIGFPooYRZQg1i6HxUHH3-WSqnluuiZrJZPauwhbNzuAX8bsc3bJcFna_5Vuuy2cc5wtkE8tAPafK_UWy4ZP8QI58ykUH1scnqjTcv8Stb3_QpjQvs8I9SSND9NhvW-zieK6kl4mE6ks7Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان: امروز از ساعت 12:30 تا 20:30 به…</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/ArchiveTell/7481" target="_blank">📅 15:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7480">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این لینک وارد شید
✅
Base url: https://tabitoken.com/v1  قابل استفاده در Vega Agent
✅
🎁
با هر رفرال شما 20 دلار و…</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7480" target="_blank">📅 14:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7479">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPUh3HjJYpHJNl0-JRn62-f-0Jk2Ff_6vZm8iipXUYjAz0eKejamhQXpN5fDkPM8Cmr9pJxLt9yqF_iCnJuDvpvi87RavJ9_bpURA0FC0HuwyTWcI2LNSWXsWxWCPD7NROzCb8rom7-PVi7qtufkF-FlxkDt2--COe1d-n4k3vR93YIVqlCJRnh3Qrd8rIrQzsd3sDDJ-VlKYULBKOMIxLBd9vtAtVkWLyXRDYZto6h_r9k_6r7rnLaWFkpj4snUvZwwYjKCH40c3GACewTqFZCbHi2ywdDwV4hno01AJP4V1GrGNUMgpRg_wckjgxxE6dudgfezOV8iz4iUMKlFgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ تست رایگان مدل ‌Seedance 2.5
⁩
💥
🆓
‏اگر دوست داری ویدیوهای سینماییِ ۱۰ ثانیه‌ای با کیفیت ‌480p⁩ بسازی، پلتفرم ‌JXP⁩ این امکان رو به صورت یک‌بار مصرف برای هر حساب کاربری گذاشته.
🎬
✨
‏مراحل ساخت:
‏‌
1️⃣
وارد سایت
jxp.com
شو و ثبت‌نام کن.
‏‌
2️⃣
به این
بخش
برو
.
‏‌
3️⃣
متن یا تصویر دلخواهت رو وارد کن.
‏‌
4️⃣
دکمهٔ Generate Video رو بزن.
‏برای این تست اصلاً نیازی به کارت بانکی نداری و کاملاً رایگانه.
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/ArchiveTell/7479" target="_blank">📅 13:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7478">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پرامپت تولید شعر بی نقص پارسی!
از پرامپت زیر استفاده کنین تا ai براتون شعر هایی در حد شعر های حافظ و سعدی بسرایه:
تو یک استاد مسلّم عروض و ادبیات فارسی هستی. در سرودن شعر، اولویت مطلق با صحتِ
دقیق وزن عروضی است. پیش از نوشتن هر بیت، آن را در ذهن تقطیع کن تا مطمئن شوی
واژه‌ها (حتی کلمات غیرفارسی) دقیقاً و ریاضی‌وار در جایگاه درستِ وزنی
نشسته‌اند. خروجی نهایی نباید حتی یک مورد سکته، لکنت یا ایراد وزنی داشته باشد و
باید کاملاً روان و موسیقایی باشد. حالا یک شعر شاهکار کوتاه و روان درباره مناظره یک قناری و دایناسور بنویس
.
﻿
تست کنین، به همراه مدل ai استفاده شده شعرهاتونو کامنت کنین، بهترین شعرو که لایک بیشتری بگیره بش جایزه میدیم
🎉
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7478" target="_blank">📅 22:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7477">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">Gemini 3.7 is out now
😍
از اینجا میتونین رایگان تست کنین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/ArchiveTell/7477" target="_blank">📅 21:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7476">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcNaXlV-iW9SjecL_DpgJp8Ch2NpDT4cRw4UnlZU4PsbIlQh3o7LEKIAUSmuEWUCA0pwSVSvdajlFKiSZ5VMaePHXijnA0VJsx6dwRoucbce9XOg6WeUYKajFOeMq3fEHyd6vLa-nhZ8m_jVkd09KhVi87gVmwnX1-Tie2-FlwMzcO54h-7yWoK51mwdFRY4T5H_abcMu4xsFCbKbbkSJyFfQyDtpzK-Hek3OUIHtRDJxg0hiczt-uK0UFzvJvcKQy-JRhbUwpHzNHaToUPy5PBWSSm819Df_urnJr1twWAmQCqHPd6MRfYuFC956hv2-L4y0kKeEey9ZS3wrwokdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
CiteSeerX گنج رایگان مقاله‌ها
یک موتور جست‌وجوی تخصصی برای مقالات کامپیوتر و علوم اطلاعات که فقط به جست‌وجو محدود نمی‌شه.
👀
🔺
میلیون‌ها مقاله + جست‌وجوی متن کامل
🔺
پیدا کردن منابع و مقالات مرتبط از طریق شبکه استنادها
🔺
اطلاعات نویسندگان و تحلیل تأثیرگذاری
🔺
کاملاً رایگان، بدون ثبت‌نام و با دانلود مستقیم PDF
🎯
برای پیدا کردن سریع منابع علمی خیلی کاربردیه.
🔗
ورود به CiteSeerX
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/ArchiveTell/7476" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7475">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">20 دلار برای دسترسی به مدل‌های هوش مصنوعی GPT مانند
:
💥
🆓
GPT 5.6 Sol | GPT 5.6 Luna | GPT image 2
✅
وارد سایت شده و ثبت نام کنید سپس یک کادر میاد برای جوین شدن در چنل و غیره ، کافیه فقط روی دکمه ها کلیک کنید و پس از ورود به صفحه بک بزنید صفحه قبل ، سپس روی Claim کلیک کن
✅
Base url:
https://apimaster.ai/v1
قابل استفاده در
Vega Agent
✅
🔗
لینک ثبت‌نام در سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7475" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7474">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این لینک وارد شید
✅
Base url: https://tabitoken.com/v1  قابل استفاده در Vega Agent
✅
🎁
با هر رفرال شما 20 دلار و…</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7474" target="_blank">📅 17:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7473">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdGo0a6DCDLUEbgGwOmxV5lqaANOUMlyNAdIur761PYSEWluLSFt3fyE1dmWRxJLIL7eiG0GYp66_1z4fBn7a_o6HxNBULu2VVpzMFZ4gEutkH85HXHO_Go6Kx60CL8MVS9RTWWmllUmGvT3lX_rGWRv6tKPPukjNpf5NAZWTOpVxcwaTDV3xC2aGvBo6ph92cY6E8oItYxJvyybcaIT5Ge3HpzQ-UnPcVIzTVKM_wCPWAPmm7BjCd-dxmwgWJOWrXWNMuCTZV5deGVcosK39mvMs04bPGo0smCcml4MAh3lTysWUC35V82jjCIQhlrBpUiKFCPnnYZBgKjuq-nkdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4 Pro 0813 وارد رقابت شد
💥
مدل جدید DeepSeek با قدرتی در سطح Kimi K3، GLM 5.2، GPT 5.6 Sol و Fable 5 معرفی شد.
🚀
🔺
سه سطح Thinking: کم، زیاد و حداکثری
🔺
عملکرد بهتر در تحلیل و برنامه‌نویسی
🔺
اجرای خودکار وظایف و ساخت گزارش
🔺
پشتیبانی Native از OpenAI Responses API
🔺
اتصال یک‌کلیکی به Codex
🔗
تستش کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/ArchiveTell/7473" target="_blank">📅 17:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7472">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFXGvRld1BoTWKx-ifw5OAM8PAP7r_CRKrfwrSgp6fQttIUcA0Gd90lPe0iHvn8eyC1PdN__TwREtpVyLVE1gGpvtjoHOhqQUYJCo4NFQLavTH58IcOv9tFOmd4uz4z9DjVamPqFk1BjG-TZJYlXvp_8QvWoU2jNlDtIOnBvBpJ-Dyr6egYeAtAd2ADkYmvb0LYKg0WlNc5d6IGrmqTAGIawUvhv5MEfrbz3cSSIjW_-wZJsTAcWpUBMypzPjesFitvQkQ84AnIBqTE7ePr4psWhr86o64efhjMxwSCxyV3hJi3v1g2-2oQBcvupu91iFpd_m1SiZrsjDV_W59giQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های هوش مصنوعی محبوب
💥
🆓
با این سایت
روزانه
300 کریدیت رایگان دریافت کنید و از مدل های هوش منصوعی زیر برای کدنویسی بهرمند بشید
✅
Sonnet 5 | GPT 5.6 Terra | GPT 5.6 Luna |Gemini 3.6 flash | Gemini 3.1 pro | Haiku 4.5
✅
🔗
لینک ثبت‌نام
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7472" target="_blank">📅 15:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7471">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPdlsoGDAWKx7tLAtHAh8LIotAPEKf8KmD7kHKe-0PKFSgY5IgujIX45hNn3iaBHzWUtHYKxNuVdH6GKEMkdElgj3rN7yB2jNnw9DSRekrbJU0KyqAEfGLP51TLqbR1UQSAUE2K8vYgUESOnm5uzZepGpOs3t95OIxc-yyNSEoOA-rUnEq8UOOCbD98n2dbkFD0b_iq5udZ7VXXBmdk3QGnxDJ9a5JKM61N4c8vRcGGiyx5uidCFEEF7MZGuxm19NgVZ4ixhZvldsQTSs_iwwDZHQU8YDDLnaQQrPh_rx7l1cPaO5wsI_S90EZd1jRfgptMUn2uoyrTpXASuhv-3XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کریپتو‌مارک مخفی Claude حذف شد!
🥸
هوش مصنوعی Claude روی متن‌های تولیدی خودش یک نشان نامرئی می‌ذاره؛ چیزی که با چشم دیده نمی‌شه، اما در الگوی انتخاب کلمات پنهانه و می‌تونه برای تشخیص متن Claude استفاده بشه.
🧑‍💻
حالا چند کدنویس ابزاری ساختن که این الگوهای مخفی رو در متن تغییر می‌ده.
📥
فقط متن رو وارد می‌کنی و نسخه‌ی جدیدش رو تحویل می‌گیری.
🔗
استفاده از ابزار
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/ArchiveTell/7471" target="_blank">📅 12:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7470">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUg0dQykaZLUKA2aZREH40W4p5xlYVGq0sGVbRYJQRdeUvc2HNrjhj5UelN835WSK_bvPgHx-ldZQ34YTa75xR93ok1DkfhJeP_10Dj4noqgYqNCW_GCAEiBLIjA0uIWnuGh9SCWD-hs38jr5XgwlVAyg_hTz9yEENpIaYvnT0Mradv8D7FhutMa1Ts6Bx7RG8PhibRhl5AZrbf8gPCTP97_tlw-Tp2rAk4ouJuNC_NaTEyk7ExPGymJxseB_jPfeHvcm_nY3aQgT312HB4mam_-OxHS98_Qizi5I6ndFO4Pkc67Xa92MRofoVSiJpmf8cMMry7DPCDYNrGQ9ckeDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
Grok 4.6 همین هفته میاد  قرار بود ۷ آگوست منتشر بشه، اما انتشارش عقب افتاد
😅
🧠
طبق گفته ایلان ماسک، Grok 4.6 حدود ۱.۵ تریلیون پارامتر داره و قراره در آموزش SFT و RL پیشرفت چشمگیری داشته باشه.
🔥
اما بخش جذاب‌تر:  چند هفته بعد، Grok 4.7 با حدود ۲.۱ تریلیون…</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7470" target="_blank">📅 23:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7469">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">https://t.me/ArchiveTell/7053</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7469" target="_blank">📅 17:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7467">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5YOqQFilmpvsbllGveK7QBVReHFQgftsc_Fxt3jgmqjDNUBVrXHy8B7WtOnpY9hPUTtrGAHlA9kMSWcAzXqrpUx-k_AkuhgyebPwpq11F08pqjlYNY_ueqRHrapZMablPKXfzeT4P8gIKv__1DUAX_CsTv0Yj-2YEFjZP31Qh0anlFf0P1tVaZXWs7bn42L2R6StuIIGjaCQOTTD7deK05nSmt1Zq9bPJUzdjsO7_8HA_GUIUncrSZ_8na6Vbn7udGXXilHnm1ZYj4t2Ce6S5udiBi9lfifrzoACsEZ_OEyABdqhxbLHW4jwJ9JFwrTJNVffz7eKR1pPYxiQSX45A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
Grok 4.6 همین هفته میاد
قرار بود ۷ آگوست منتشر بشه، اما انتشارش عقب افتاد
😅
🧠
طبق گفته ایلان ماسک، Grok 4.6 حدود
۱.۵ تریلیون پارامتر
داره و قراره در آموزش
SFT و RL
پیشرفت چشمگیری داشته باشه.
🔥
اما بخش جذاب‌تر:
چند هفته بعد،
Grok 4.7
با حدود
۲.۱ تریلیون پارامتر
میاد؛ قوی‌تر و بهینه‌تر، ولی کمی کندتر.
✨
👀
باید دید xAI این بار چه چیزی رو رو می‌کنه!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/ArchiveTell/7467" target="_blank">📅 15:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7465">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🎙
LivDub | ترجمه و دوبله زنده با هوش مصنوعی
با
LivDub
می‌تونی ویدیوهای خارجی رو
هم‌زمان ترجمه و دوبله
کنی؛ بدون اینکه مدام به زیرنویس نگاه کنی
🤯
✨
قابلیت‌ها:
🔺
ترجمه و دوبله لحظه‌ای ویدیوها
🔺
استفاده از
Gemini Live
برای ترجمه صوتی
🔺
پشتیبانی از
۷۸+ زبان
🔺
مناسب یوتیوب، دوره‌ها، مصاحبه و لایو
🔺
پشتیبانی از مرورگرهای Chromium روی اندروید
⚙️
روش استفاده:
مرورگر سازگار رو نصب کن → افزونه LivDub رو نصب کن → Gemini API Key رو وارد کن → ویدیوی خارجی رو پخش کن
🎧
🖥
مرورگرهای پیشنهادی اندروید:
Cromite • Helium • Ultimatum • Quetta • Yandex
🔗
افزونه کروم
🔗
سایت LivDub
🔗
گرفتن کلید جمنای
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7465" target="_blank">📅 13:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7464">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNQf2pDLFiIE1CV3kw2YFT5KOJ_yFwYF_wwX2YTu58vrmlipFZ-YohAZ3a3x2Yr0pUjeYqsEOc4BCeiGpSbolPog4CroPf55Zq1BNI0nTg57M3MpZ-IBoIlEUHxaGAmQHWv_IKB37ZpB0UZTDmgxCdtzT1xnt2Cv8luftjSC8GNSevZSb1V1kP8fr9FzhgZ8RfeXWGzyU72Xet-t_ezP8AD-a7cgSzHTNC0qp_bSVi-V3VQ2wJ2F7au9sfyIjI3cCRYGyY4VGkibyWvf6hmmpjcYrHSSHfHylGtas5Puwf8XJhOFgKxH0Mk-WLveQayjVdZSqG4xDfgGWOLdL5I41g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
FLUX 3 Video رایگان شد
؛Black Forest Labs برای مدت محدود، FLUX 3 Video رو توی Playground خودش رایگان کرده
🔥
⏰
فرصت استفاده رایگان تا دوشنبه ۱۷ آگوست، ساعت 10:30 به وقت تهران
قراره در ادامه قابلیت‌هایی مثل 4K، ادیت ویدیو و استفاده از تصویر/ویدیو به‌عنوان رفرنس هم اضافه بشه.
⚡️
✨
🔗
لینک استفاده
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7464" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7463">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آیپی تمیز
✨
188.212.97.3
94.182.177.92
185.50.39.15
103.25.85.84
176.120.17.44
45.146.240.17
45.146.240.70
77.237.246.20
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7463" target="_blank">📅 09:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7460">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSYsFKuB_lYKj4ZyAF59xIEWKLkOWiL21puMzkuegslZE7A1iZ8Ged1NspL5ZV9ps-s30CVUhiIMoqAvcyZviVYjDlHJd5XFILi0VtH4Wpy9zeHwmAjOoQXfAgNYz3K-no5Xy0rO6K5ydm9iewvR306Bq8JHOpjpGZsba8XbkHBRKUoGoRED7xqSz5aLOqBrw9GgHzLbUzkTV6eXzpP9mCnSHGt6WARzC7EfrKfqXv2_3R0l-yD1LnuUMhyyapmjeXs_3cKfjJDl8xk8MC6TqcsTm2sV3rI9G8nzHP4Pl4Cn0lRHM-kukSLg516fePer2oagluSALRGnCh-CNKJa7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از 1000 پرامپت کاربردی برای هوش مصنوعی!
🚀
یه سایت که مجموعه‌ای از بهترین پرامپت‌ها رو یکجا جمع کرده؛ از درس و برنامه‌نویسی گرفته تا طراحی و Excel
⚡️
✨
یه جور جعبه‌ابزار کامل برای کار با هوش مصنوعی
🧰
🔥
🔗
لینک سایت
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/ArchiveTell/7460" target="_blank">📅 16:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7459">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ssxai0ASt-1YAvRijY4b3U0S62KBnFuJBJ9C3pVCPgLVsjmCpSdCY-N_xgC3_SdV7vN34sy8HF6ie0JxAlttuY3r6haXNVCkErslou0CIVA4Y_qV-2_plDdto1G82xgy3t_CQryhzZioX0OtK0gaCTjYvfDgSwirI79jpaBhV5Bs00JzQYH72cebIyUflWM4QFdVpzR0HSvqsAWdpPLZ9syKymE65UI7QQIPHZVgjs0s_tq2WF-86lDFCIzpnkNKGq1kuYDsp7uckXADFWQchHeLJCbP5rvvxLkXvwGxxUAmwiQjWULzfh7D13frbZBJFjK7FMjWxcADsMkjArgvuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤔
گوگل قید Gemini 3.5 Pro رو زد؟
گزارش‌ها می‌گن گوگل عرضه‌ی
Gemini 3.5 Pro
رو متوقف کرده تا مستقیماً روی
Gemini 4.0
تمرکز کنه.
🚀
گفته می‌شه مشکلات عملکردی و سخت‌گیری‌های امنیتی در مرحله‌ی تست، دلیل این تصمیم بوده.
🛡
حالا رقابت جدی‌تر می‌شه؛
Gemini 4.0
می‌تونه از ChatGPT و Claude جلو بزنه؟
🤔
🔥
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/ArchiveTell/7459" target="_blank">📅 13:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7458">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این لینک وارد شید
✅
Base url: https://tabitoken.com/v1  قابل استفاده در Vega Agent
✅
🎁
با هر رفرال شما 20 دلار و…</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/ArchiveTell/7458" target="_blank">📅 11:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7457">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPY2Z28xquVhXXKuTm6jp2dAX0C11VS1yZgcsG3UOaNd3c0s5Larjkpdt3-F8MTfVWYdCdJCeFIlAqSmJjPR83LrGqE2CwCs7FO_I45K_azrKdErOcYueRhDbECjho4KP2eoXqYt081q3aFU675Q93eHiSayZh0LGJ_AcvHcyDLrKn6-LiuSTsb0uuROxvc-H6Gw8SUingcSE_3e20fvQTPeC_969bqZb5ObGlK4E_bnXBpF6CFQi8YabxnOjZHHGpYN41bAYX_tL9uOguxN8btZXO2j5zv0ccH7OrXvno_KGWP-t2ifp8OVZFH6LJltCZENlGp2kSkZWJYtntF7rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">40 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
✨
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدیمی لازم نیست )
داشته باشید و از طریق این
لینک
وارد شید
✔
🎁
با هر رفرال شما
20 دلار
و شخص دریافت کننده
40 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/ArchiveTell/7457" target="_blank">📅 11:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7455">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyaPyXfYl9eHHQj2dxL7zQKqWcPrUHChfOQ3e_ALk9HY3x4e-JDxpSleIBeHqbDJ_zbagxeS4ylr5fsn6rierJ1hF0HLK-vPWJHsopwMSPCKaxV6pPX_Fbrse_PdxuhRz6XtZje8OuBRm_0AX_vKERCai4yJnIYcFPzwNCvs8wfQP3c6nG6J1efVvSA2E4fgKkkuwcojJltARMbSCgu_jeMQosXmDl0Q9psXjlk-XY7M10rPjRNw750gPIOsAFjyHbq7wJf_2-HXYBZOYCAmCAml4RoD_mBSgsM0S0LqAefHPLlucdeuMT40fg0eJkpO2TWXRwaA8pzwvLyKIdVfAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منبع بزرگ یافتن سایت های API رایگان
💥
🆓
💵
با پوینت های این سایت میتونید کلید های API خریداری کنید و یا کلید API خودتون رو به فروش بزارید ، همچنین میتونید Redeem Code برای انواع سایت ها خریداری کنید و کریدیت دریافت کنید
🔍
همچنین این سایت منبع بزرگی برای یافتن سایت های API رایگان هست
🎁
موقع ورود مقداری پوینت دریافت میکنید همچنين هر روز میتونید از بخش Daily check-in ده تا پوینت دریافت کنید
⚠️
🚨
نکته:
حتما با فیلترشکن وارد شید
🔗
لینک ثبت نام
🔗
بخش خرید و فروش کلید
🔗
بخش خرید Redeem Code
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/ArchiveTell/7455" target="_blank">📅 22:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7454">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAIWEh3qcRe9UMSxZtWWWscloaVf7rsmAbUp4JVhQSR7xCUWthj53A6A1GQM90Ujyn3J7tSGC1bT3fVIQ3pSDYAv_J9YwF8zbRPPDd5GySwRkXtNT5BMds3sQ1RNuYhmgMDvVjHF7Ii-kTWJhDfcK0wE_GsfUJ-4mBfKssU1nuxgAz-kpamHGfT1lzoAvDaC6s0hOyMWxri-au4zR1KgE_ZUGqJFNCcuawl-wenA1ZoV4q1YjSKQINN24XnaAcYKm0ADO5yxY0MYkeoQRK703q3O8_Uvicieo7LFmM4sqtUTVs6QIBiBtUeKVU3lurkSp6RYDrRu15LitbFxGaRYvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های هوش منصوعی قدرتمند
🚀
🆓
Opus 4.8 | GPT 5.6 sol
✅
وارد
این سایت
بشید و ثبت نام کنید
سپس به
این بخش
برید روی Upgrade کلیک کنید و پلن Enterprise رو انتخاب کنید و روی Start Trial بزنید تمام حالا به
این بخش
برید و در صفحه چت یه چیزی بنویسید و Let's Go رو بزنید
✅
پیشنهاد میشه که اپیکیشن Postman IDE رو دانلود کنید
‼️
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/ArchiveTell/7454" target="_blank">📅 20:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7453">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBwo6-frjGjSgX3F_oU-AfoOXlaILbAryVT1wbkZSHf9UeJv7eXrSCC18bp2mGuxd_B8PotMN9tPJUi-PFsUzAbVdBJzdraHHNepgUqCg9mgC3B92lilxkD9tQBEQv-pjNqYfeQrukEVC0FpzyZNRsMb02guVnsRxpqSXDxHpjL9Od0CWcVEAwT0I4JZHs1Er5gx6JanUAKiebweX4V2bOC2rUjZeGiIBjEAVjwyyyheYsrrENf4OXVviPm8kr0JKtk3kAH1DQqU4TPo5PGmcwGprUqXdovpSmRP_GSvNIRGSFJoLuHEewVSWXt-2IKILlCJ2twtQs3a6Gwl1fgUCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدیه ویژه برای شما
🎁
3 میلیون کریدیت رایگان در این کلید قرار داره ، شما میتونید همین الان کلید رو در هرجایی دوست دارید استفاده کنید
💵
🆓
🔺
Api keys:
dxai-sk-5feecf996d141afae9e16f8bc072d49a692312d7452a4043fd055c37aba2c8a9
🔺
Base URL:
https://airdropdxns.my.id/v1
🔺
Model ID:
grok-4.5
|
qwen3.8-max
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/ArchiveTell/7453" target="_blank">📅 12:53 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
