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
<img src="https://cdn4.telesco.pe/file/rcoA2gZhZ88SlLdbouj5XH1fC7fDbaMaYNxzR5yXbfRLjY1EoWZR0mIBZCyPsrKxLB59OselWa4VFNJy882CAzALMfFtxm79tzPpEwthq4SxpyaYkVtVjr3QSbYdZKPLYTHQz54Ysfz-V2kQldj2EuN6P74ZfcfKHkB-B6mIaXO33OtypBKfgLHJFuxTSgyyLHROfTD4G0PoE_KFciey22cEBfqX3IM3K85lGnoP0G2XHHj9hxJCkuMa6OH68pUP67FlT8KAozvbjCw6dysMMCeAASMpB5xzItu2HAt7i3f8cvZycKK_mumS0-uTULXcx4Jz5P9exP7GWnOpyiOCQQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 03:54:12</div>
<hr>

<div class="tg-post" id="msg-7607">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTirexNet(TirexNet SUPPORT |)</strong></div>
<div class="tg-text">«
🦖
TIREXNET SELF
اکانت تلگرامت رو همون‌طور که می‌خوای مدیریت کن.
⚡
🎮
یک پنل شیشه‌ای برای مدیریت، شخصی‌سازی و خودکارسازی اکانت تلگرام
👤
پروفایل و بیو |
⏰
ساعت و فونت
🛡
بلاک و سکوت |
🔒
امنیت و AutoSave
🟢
آنلاین و Action |
⚡
ریاکشن خودکار
🤖
منشی و پاسخ خودکار |
📢
تبچی و تایمر
📋
ابزارهای کاربردی |
🧠
هوش مصنوعی
﻿
«
✨
همه‌چی یک‌جا؛ ساده، سریع، حرفه‌ای.»
🤖
ربات:
@TIREXNET_SELF_bot
📢
کانال:
@TIREXNET
💡
پشتیبانی و ثبت پیشنهادات :
@HRMP1386
»</div>
<div class="tg-footer">👁️ 802 · <a href="https://t.me/ArchiveTell/7607" target="_blank">📅 22:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7606">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 885 · <a href="https://t.me/ArchiveTell/7606" target="_blank">📅 22:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoYtTVf4FoCSR66_1Ak5mjuzD7zy25d-pbel1-ZqesXEPsjsIFeNsghly_xZN0cPS4KU4RubSdQCxFMQFKb_qiXZYsrWDtybv02UxYgJLS6r5MlxNoYd_NYFif9S7u_K6_ZwRpNP9WibAzEwSSn90Ua_y7oL-Y_5JwW-re2u2VMsygXFUksaKGSdM7_jebXR05e7ilSxNeijEQbshr8TmmmSzT5zpR6WgL2VOVPTQwedmc_S3unyGRfxeRwSLQgwzZQPsKmrsL3A6trN-omcUIwWDZcSUmygVjeecXWS7ZLhncceyIt6Uy3m2SJU8y2Np31LwDuiiJPE5uANpsrAHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل Gemini 3.8 Flash در برخی موارد از Opus 5 پیشی گرفت - با قیمت 0.75 دلار برای هر میلیون توکن
شرکت گوگل، سومین مدل Flash را در عرض شش هفته منتشر کرد. Gemini 3.8 Flash برای برنامه‌نویسی، کار با ابزارها و سیستم‌های عامل مستقل طراحی شده است.
بر اساس تست‌های گوگل، نتایج به این صورت است:
⚡️
Terminal-bench 2.1: 89.4%
در مقابل 89.1% برای Opus 5
⚡️
Finance Agent v2: 61.4%
در مقابل 58.6% برای Opus 5 و 53.8% برای GPT‑5.6 Sol
⚡️
HLE-Verified: 54.9%
در مقابل 54.4% برای Opus 5
⚡️
پردازش ویدیوهای طولانی: 87.8%
در مقابل 75.4% برای Opus 5
اما این مدل در همه زمینه‌ها از مدل‌های پیشرو پیشی نگرفته است:
⚡️
DeepSWE v1.1: 71%
در مقابل 74% برای Opus 5
⚡️
Terminal-bench 4.0: 19.1%
در مقابل 51.8%
⚡️
OSWorld 2.0: 59%
در مقابل 75.4%
به عبارت دیگر، این مدل "جایگزین Opus" نیست، بلکه یک مدل سریع و ارزان است که در برخی وظایف به مدل‌های پیشرو نزدیک شده است، اما در کارهای پیچیده و تست‌های جامع سیستم عامل، عملکرد ضعیف‌تری دارد.
قیمت این مدل تا پایان سال 2026 ثابت باقی می‌ماند: 0.75 دلار برای هر میلیون توکن ورودی و 3.75 دلار برای هر میلیون توکن خروجی. پس از آن، قیمت دو برابر خواهد شد.
همزمان، گوگل مدل Gemini 3.8 Flash Cyber را برای جستجو و رفع آسیب‌پذیری‌ها معرفی کرد. این مدل در CWE-Bench امتیاز 47.2% را کسب کرد، در حالی که مدل پیشرو امتیاز 47.8% را کسب کرده است. دسترسی عمومی به این مدل وجود ندارد: نسخه Cyber فقط به متخصصان امنیت تأیید شده از طریق برنامه Fairwind ارائه می‌شود.
در حال حاضر، این نتایج توسط خود گوگل ارائه شده است. هنوز هیچ تست مستقل از این مدل جدید انجام نشده است.
⚡️
جزئیات بیشتر:
Google
⚡️
بنچمارکش داخل سایت
https://artificialanalysis.ai/models
اومده
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7604">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoQPNI--aaa808SXdaRoRR7R3mMndTbcyTIs_JobiDcbPPjfrWdvdqeTzJpkhn6zzXrM21vih8zvccN_d0A-i0qFU6ahiAVAFTcxAL1FaFaMd4qyxZ4IbM32k0zM2OtF7-8T5J4qGlukJ_1NMT8orMl9vOqFUrDKgO0eWcDj0IxKt_p8Z4jIbvRKRwomhnDvTHbcTbmyPdOf61hnz6-Ganb4oV1DBfaGgIxtz5TQG_4HgvxS1HpR5wgU7_hEowRwpFa4JdjW9_9jxRFS5B45Kaz49Sm7fDP-LBSbC9G6JAc9RAseCBa4WIHKtoG8XI79Gp8RL8lzYFzQ0yiD6Dkd8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBOif0M9BOc3xvMRCxKzas0eLr2hsNg4ZbWdDow3ayZyZk8HT4c1M4Z3t1dOPwYps3IVSDBXfY5YEq8F9l0Of6GRuzBoSl-bEU1Sq4_ri4BATrV0SOHuGgc-S4ILdzYNY1gocOZ2pzOgt6d8xKjX8AdL1dA2xmLAi80etsaP-qsdG8Wj92bda0dH__sPKpWChbcoaz4F0vgS2WrrFdPgVU5nqQ2TFjGIdzosW-VnKsK5R1uXBnW9hi6mvPQEWoOlVMI1c39l6wE_HpNCOdmFDjJGYRmVaKuaAfKlYLjfSdB85Bcx848fADXq7pwp_rrJydwBABzwpBrxnw8QebW8EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTeCOF-Zw5M9-aNpfBqJJuRaRg__pgFmI-y7M6o9qOsx4EGxb2t9B5xOETj4pqOm_PfhfJP92E_4vN7SN2S_WX4U0EeFI8rajfpdbhSg8Nt30NfCvuw1MkQ_McJtn51fUgtjdu7nanNYXkDOqkA3LdqIrogT_NTImt8mLyzYwBIzuG4CsfpyydnqTjQwvmVcvl800F6bu6CXRlFJNpXstg4ff271MJsjnILLGqjmTqeqQ_KYBFuwzuJyQBRQBidF_vM8aZDmA2pMZ7DprfithI7woy80ghBXnH70RFdgJtqMkJBtAbNyIGeqsT3aIu9pAVBP3Io7INMBBpLRYpnySw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ریپوی ArasClient پابلیک شد!
بالاخره سورس کامل کلاینت روی گیت‌هاب عمومی شد
✅
🔗
گیت‌هاب:
github.com/ArasTey/ArasClient
📥
دانلود مستقیم:
github.com/ArasTey/ArasClient/releases
فایل arm64-v8a برای اکثر گوشی‌ها
✅
فایل universal برای بقیه دستگاه‌ها
⭐️
اگه خوشتون اومد یه Star یادتون نره — برای ادامه مسیر خیلی انگیزه میده
❤️
━━━━━━━━━━━━━━━
چرا ArasClient؟
چون کار چند تا اپ رو یکجا می‌کنه:
⚡️
اسمارت کانکت
یه دکمه: همه سرورها همزمان پینگ می‌گیرن و سریع‌ترین وصل می‌شه
🔃
سورت سراسری
بعد از هر تست، سریع‌ترین کانفیگ از هر سابی بالای لیست قرار می‌گیره
🔓
فرمت اختصاصی .arasc
ک
انفیگ‌هات رو تو یه فایل رمزنگاری‌شده امن ذخیره و به اشتراک بذار
حالت Protected: طرف فقط می‌تونه وصل شه و پینگ بگیره — نه آدرس، نه URI، نه اشتراک‌گذاری مجدد
📊
اطلاعات ساب
حجم مصرفی، حجم کل و زمان باقی‌مونده ساب مستقیم از لینک ساب خونده می‌شه و بالای کانفیگ‌ها نمایش داده می‌شه
📣
اعلانات ساب
پیام‌های سازنده ساب خودکار نمایش داده می‌شه
🏳️
پرچم کشور
کنار هر کانفیگ پرچم کشور سرورش (از روی IP واقعی سرور تشخیص داده می‌شه)
📊
آمار اتصال
تایم اتصال، آپلود و دانلود لحظه‌ای + آمار کلی در تنظیمات
🛡️
همه پروتکل‌ها
VLESS • VMess • Trojan • Shadowsocks • Hysteria2 • WireGuard و…
💎
پر-اپ پروکسی، روتینگ کامل، بکاپ و رستور، تم روشن و تاریک
━━━━━━━━━━━━━━━
🔒
ویژگی‌ای که هیچ کلاینتی نداره:
کانفیگ‌هات رو با پسورد به دوستات بده — اونا فقط می‌تونن وصل شن و پینگ بگیرن. نه می‌تونن آدرس سرور رو ببینن، نه کپی کنن، نه برای کسی بفرستن. مخصوص فروشنده‌ها و ادمین‌ها
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmKfk_G-vPoZKLFDNushz4KhbspM-DhybiszR4RJdCxPByXyJF795gZ3XEmQjluz8OLdq59RU4fFZqtcNYJudXRNWOsdgMPH8E5RNWYXt_MGZRHwLLVV84XbfQXAkiezGqJCcrczdUNiynVXRWV86H7gP-p5FUIkJY1UyfEqN_RHEkwmNZ6XBdiGDTIJp4Z5Lu-VLJhAHpz3llUZM2U3P1L5xV4TT43Fxg_cTQkGT8KmaK5QI-OVKaI2dF2qyJ6o7Jj7rDQzCpF28dmaRGtKydI1EUiu_GeDzaRfYbQmUpb7t8Gvq21oMYZCxjjQ89qrjwG4XA09erHFDXd-w0GTcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧑‍🎓
✨
OpenMAIC — کلاس درس تعاملی با هوش مصنوعی
هوش مصنوعی داره تبدیل به یه دانشگاه آنلاین کامل میشه!
OpenMAIC
یه پلتفرم متن‌باز برای ساخت دوره‌های آموزشی تعاملیه — شبیه NotebookLM، ولی با کلاس درس مجازی واقعی
📚
📤
چیکار کن؟
یه موضوع، فایل PDF، اسلاید، صوت یا ویدیو آپلود کن، سیستم خودکار می‌سازه:
✍️
ساختار منطقی دوره + اسلایدهای آماده
🔤
آزمون، تمرین و سیستم تصحیح خودکار
🔬
شبیه‌سازی، مینی‌گیم و مدل‌های سه‌بعدی
👨‍🏫
معلم‌ها و همکلاسی‌های هوش مصنوعی برای بحث گروهی
🎙
سخنرانی صداگذاری‌شده + تخته‌ی هوشمند با نمودار تعاملی
📦
خروجی:
فایل
.pptx
یا
.html
قابل ویرایش
🔌
سازگار با:
ChatGPT، Claude، Gemini، DeepSeek و مدل‌های محلی (لوکال) هم پشتیبانی میشه
⭐️
۲۰.۷ هزار ستاره روی گیت‌هاب
— پروژه‌ی فعال و پرطرفدار
🔗
لینک سایت
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6q9qpQoZvei58VN15FFUi3vRi6qkz_0Lqv8gx0LL14f-ScascrXZVKi8DZZtbE1q3rHErnLoPqkEROSzMc9ymMWdiBI5xMiIg7bODn844-lSBP0akBLcoadIMltymrA5c96Gwep31pbgf0AcTmP_XrwBILZ49uPriAhRl6hTxCZJcsL6X-jlTZvG5Quvyy1exldJLQjblNC9mPdzkUNZ0ER8Wt_1OAUjR2CnrpS0-R2_yCY9kDLtkWDlnkfEy_t5HTH78qSP4G1NgBYmGTAL41cg04JJG2wT4OKknn14zkPIq9aQjcI5XsjdB21yjQlzfvkwmgcGNR3mjqKLphg7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
✨
۵ ویدیوی رایگان روزانه با MiniMax H3 Max — بدون ثبت‌نام!
با این سایت میتونی این مدل ساخت ویدیو رو به صورت رایگان امتحان کنید
🔥
✨
ویژگی های کلیدی :
🔺
روزی ۵ بار تولید ویدیو، کاملاً رایگان
🔺
هر کلیپ ۵ ثانیه، کیفیت 768p
🔺
صدای طبیعی همزمان‌شده
🔺
متن و عکس به ویدیو
🔺
فریم اول و آخر بده، مدل حرکت وسطش رو بسازه
🔺
نسبت تصویر: 16:9 | 9:16 | 1:1 و...
بدون نیاز به اکانت برای ۵ تای رایگان روزانه — با لاگین هم ۵ تای دیگه اضافه می‌گیری (تا ۱۵ ثانیه‌ای)
💡
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mi8sOnLKuQYVSE2ICuVuRys-YPzVYgCD_KJKZloG9KKbI5eq1O0IPtClBix6kiXjLajTfoyKg1ToVAAR6a4UJVCAwVGmvS_pTGmQU3a18xb5UbvZq0_QLDdO7OFADtixBIOCVbxVaEjgItF1mZwaEnRxYjORc296b8p4vBgPDHGhth_E4pML5DMraqLIc6kNjPw4OizH17j0nDmzO88WQIVc5fZIhKzs47N-53LA1j-y72LScCw-AAIKqBK0fkfrgEo1tTC6cw_G9kazAcVzdvj9vpCVUYnRRaffsT6_g1ylSth_2VEvqR1BEh-lFMG8Nny27yXAkIltIFWwWfVcSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔧
✨
دانلود کامل گفتگوهای Claude با یک کلیک!
معرفی
Discussion Downloader
— یک اکستنشن ساده و سبک برای Chrome که گفتگوهاتو با
claude.ai
به فرمت
Markdown
ذخیره می‌کنه
📝
📥
چیکار می‌کنه؟
کل گفتگو رو استخراج می‌کنه — همراه با:
👤
مشخص بودن نویسنده هر پیام
🖥
بلوک‌های کد سالم و دست‌نخورده
✍️
لیست‌ها و جدول‌ها با فرمت درست
🏷
هدر YAML با متادیتا (عنوان، لینک، مدل، تاریخ)
⚙️
چطور کار می‌کنه؟
برخلاف روش‌های معمولی، داده‌ها رو مستقیم از API داخلی
claude.ai
می‌گیره، نه از روی صفحه! چون توی گفتگوهای طولانی پیام‌های قدیمی از DOM حذف میشن و روش‌های عادی نتیجه‌ی ناقص میدن
🎯
🔒
حریم خصوصی در اولویت:
✅
فقط دسترسی
activeTab
و
scripting
✅
بدون آنالیتیکس، بدون تله‌متری
✅
هیچ داده‌ای از مرورگرت خارج نمیشه
✅
رایگان و اوپن سورس
⚠️
محدودیت‌ها:
🔺
فقط شاخه‌ی فعال گفتگو صادر میشه
🔺
آرتیفکت‌ها و بخش thinking صادر نمیشن
🔺
رابط کاربری فقط روسیه
🔺
نصب دستی (unpacked) — توی Chrome Web Store نیست
🔗
لینک مخزن در گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEPfnEV0_u_Vvut9Y8FXQR2SC0nEPCN9PWL1ppHl13hEQodnFaCBvaPCge_d7vTsPFTVVmKg6bXbY5K0SXevsqoTVQPCjaVZSG3GUBGr2UaVZ800TE37xC83SjQCyxJ6mpFkrZ7oJDbV423gk-HDrfviVx7m170Q3swev_plHTJIz0QcIWyJSbDnC-GsdK5TrswA7fNzSxIVI9cXYvyZcYdfpOw2OF-niJ6gX66SGlytxvLfrKidLaY2V7xXz3SOmyBnRvfJUCu7pvjQsmNsD6bZ1vpHrbVBrdqwGRlPXV-AOnqQRvLZq4TgS5zOLJ6lts94riBgozbvleSYwWj3VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦆
✨
حریم خصوصیتو با هوش مصنوعی معامله نکن!
با
Duck.ai
بدون ثبت‌نام، بدون اکانت، بدون هیچ دردسری به قدرتمندترین ابزارهای هوش مصنوعی دسترسی داری
💥
🆓
💬
چت و وب‌سرچ با GPT 5.6 Luna
🎨
ساخت عکس با GPT Image 2
🔊
ویس چت با هوش مصنوعی
سؤال بپرس، جستجو کن، تحقیق کن، عکس بساز —  همه‌چیز رایگان و خصوصی، بدون اینکه ردی از هویتت جایی بمونه
🥸
🔒
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdBbU9li3fgjluibWH5kskVpGSi_2Jl-k4VSZSd0FZcgbs2sSbVuGB4W31_4XsvKw9nwXZRoB4yqtEYQa8zFXyZqSNd-XdKIq-RIx3ZftinRBN-xSiqbzE5cd_mL5f2vfwx9xrRGRsyeHimk9H4yzizlLISv5zQ3cl6QXlU25rIEslyT4RT6xVfE7mWDQKqVcU6-nyQP9nLX3h9C1N7IaNCK0GnBca-rZfQQ5HzwnRxKkfykyFRXz-kon0sGbq4-uJmEMIq-z4R50iDMC_CnVSUWYBB8E6nVt0OkSQjM60FZRrIpVHxYhgUYPGuStfjCLl4w91O7NF5uwTirG1sOwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Hy4 Preview: رقیب جدید GLM-5.3 و Kimi K3
شرکت تنسنت، مدل جدیدی از خانواده Hy را منتشر کرده است که قبلاً با نام Hunyuan شناخته می‌شد. این بار، برخلاف روال قبلی، مدل به صورت عمومی منتشر شده است، وزن‌های آن در دسترس قرار گرفته و به سرویس‌های محبوب اضافه شده است.
اطلاعات کلیدی:
🟢
770 میلیارد پارامتر، با 49 میلیارد پارامتر فعال به صورت همزمان
🟢
ظرفیت پردازش متن: 1 میلیون توکن
🟢
حداکثر طول پاسخ: 64 هزار توکن
تمرکز اصلی این مدل بر روی وظایف پیچیده و طولانی است: کار با کدهای بزرگ، تحلیل چندین سند، نمونه‌سازی بازی‌ها و تحقیقات علمی و غیره.
در یک آزمایش کور، شرکت تنسنت 203 وظیفه مهندسی را به 163 متخصص ارائه داد. نتایج به این صورت بود:
1. Hy4 Preview – 2.99 ( از 4 )
2. Kimi K3 – 2.94
3. GLM-5.3 – 2.92
این مدل در تست‌های منتشر شده نشان می‌دهد یکی از قوی‌ترین مدل‌های متن‌باز موجود است.
نکته جالب دیگر این است که این مدل به طور جزئی در فرآیند توسعه خود نیز نقش داشته است. این مدل نقاط ضعف در عملکرد خود را شناسایی کرده، پیشنهادهای بهینه‌سازی ارائه داده، آزمایش‌ها را انجام داده و به افزایش 31.8 درصدی سرعت پردازش کمک کرده است.
نحوه تست:
>
WorkBuddy
– به صورت رایگان در دو هفته اول پس از انتشار
>
CodeBuddy
– دوره رایگان دو هفته‌ای، با تمرکز بیشتر بر روی کد
>
OpenCode Go
– مدل به اشتراک اضافه شده است
>
Hugging Face
و
GitHub
– وزن‌های مدل برای اجرای محلی در دسترس هستند
برخی مشکلات شناخته شده وجود دارد: مدل گاهی اوقات بیش از حد طول می‌کشد و نتایج نهایی را دوباره بررسی می‌کند. به همین دلیل، این مدل در حال حاضر یک نسخه آزمایشی است و نه نسخه نهایی Hy4.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdgxiUY6rBgxR7MY1vVEk4f769MKP76CnZPZTaqJIQh15n-GHqpENSNaIvK8s-QkQtXanXIqIQP8bCx4nVNZP4XChyg0eDlceSp6bNCqgZtOEu-52ngPzmiPyRKXdvIlejtoqzJ_Q3GziFwp7v_6r5kVn82TydV7mRVEyMXTxf1CdcUdn2CJN-K5IwgI0OreCNOvqv1B37gOGN1iCZufpZFRXAtS5cur7Skst4xtWreKcdUQB2LTc8-_v-2YNSD3zmOXninJckOsKY8WHEKO62nPxajxabxn7ejTQRRLzTysaPzmna0IKeS6dRlGuxEuuWd7eOec7iEVMuMbUUwqMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تبدیل PDFهای قطور فارسی به متن تمیز برای هوش مصنوعی!
نرم‌افزار ویندوزی و رایگان
PDF2MD Studio
. با این ابزار، PDFهای ۱۰۰۰ صفحه‌ای رو به متن استاندارد مارک‌داون تبدیل کنید.
فقط در ۳ قدم ساده:
1️⃣
تبدیل هوشمند:
PDF رو بکشید تو برنامه تا به عکس‌های سبک و باکیفیت تبدیل بشه.
2️⃣
استخراج متن:
عکس‌ها رو تو Google Drive آپلود و با Google Docs باز کنید (بهترین OCR رایگان فارسی).
3️⃣
تمیزکاری نهایی:
متن خامِ گوگل رو دوباره بندازید تو برنامه. نرم‌افزار تمام خطوط و نیم‌فاصله‌ها رو مرتب می‌کنه و یک فایل فوق‌العاده تمیز میده!
حالا این متن رو بدید به AI تا براتون خلاصه کنه یا تست امتحانی بسازه!
😍
🤔
پردازش امن روی سیستم شما
🤔
بدون نیاز به اشتراک پولی
🤔
اصلاح خودکار باگ‌های تایپوگرافی
دانلود رایگان از گیت‌هاب
(ستاره
⭐️
یادتون نره):
🔗
دانلود نرم‌افزار PDF2MD Studio
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXFkoLHOr9cx3_9ZC65cntUUMgh83vZD8OR8cwFWmY2WRz612_CQUKC4FsIR2O4URWkmhovmvQSFC9k9dl2xC6rt5D-bZJPCv0evmfTDO4KzN8MPO3Jhyu1XQ6WmJRc_-CBCK4HR4mmcpj-h6WM3rXhzOep4LC_ATh-3e3Wdix1HnyLgKS6rfLrwtbSd2XIu3Dq270fTSf6fwhZ4mK3YM-ONS2A_PnMKaAIJhlRPegnwXjnuVZU5mrCyWb6n2KYE1hVfIkGazZ4K0y4hHesN7wWS6J5Fb5u5dEsvLytuwSq-Q7bGzffr9LUG-O800LhDYOXYipDz0kUIZI6FISjDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100
د
لار برای دسترسی به API بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدمت یکساله )
داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
25 دلار
و شخص دریافت کننده
100
دلار
دریافت می‌کند!
همچنین 20 دلار پاداش روزانه
🎉
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtyCU9XBGVVHDLG4Z_Ni-PPIQuQlsRHDsADBZE6jQb-SdxCCqip1U9H_5fuk62R39KIOr7-6LBaZw5mle8BKHT5IpkaZ7_RVTYOYZhXNa6vPZBUi8Tys-gpLDaJ7Jj9sfbOUO6h9m8XJs4_S-AMQoaVlGXsJ23k_e0r4DzXA_3pnNXmOX6J6Tqjbs-Z9GS_AULIGQ72TtP-dh-KNTJDomkTn1lVdBex5C_9gwfFXXw6AZj3K7EDeM14Rl9RfPAGQCUCMhIXKqgl3IapLfiGkls-0iMc7hOjrkdhjzoDLEwHIUEaDXXZjbBq3_JvMvBF9nDLUQmrlZ-04j6ANdKXSWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت 10000 کریدیت رایگان سایت Genspark
💥
🆓
با این روش میتونید داخل این سایت برای مدل های زیر و دها مدل قدرتمند دیگر 10K کریدیت ۱ ماهه معادل ۲۵ دلار دریافت کنید
💵
😎
Opus 5 | Fable 5 | GPT 5.6 Sol | GLM 5.3 | Kimi k3 | Grok 4.6 | Deepseek V4 | Nano banana 2 | Seedance 2.5 | GPT image 2 | Gemini 3.1 flash TTS
✅
❗️
نکات مهم :
چت متنی در این سایت نامحدود هست ، محیط وب سایت یک محیط دارای Agent هست ، همچنین می‌توانید از این سایت API بگیرید ، همچنین این سایت یک نسخه cli هم داره
برای دیدن آموزش کلیک کنید
✅
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5a4r2QTO5K7L-gpvGoJwhz3TGZ8fEDNrV4W4gfpcoBhESxPjUjHDU6z21W1ldSD54us9Bu3uhxMn511ZvLp-uyVtjfl3LQ7O2UfeGLYbikfATiR2-dFhlch3JbWpP_sUxAWbWtK1khz7ULIUFmgP_-c1oCjTAjd22P5otxr1j3KvM6_MiQJiAC3HpUE__NtgFOuAY38rn7X61w2exlYS8F7jNPfmKgLrey7yiy337S6_aD9qWlqOSWuq60UodsVnK_9zYO-e-i7dNfTsNLYfTfUFXEZ66veel3GMrGiCLoXwydjcIc9CRy3ao3SRJbBW7ul_S9jNt0n_aabSYqhYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
ساخت تصویر با هوش مصنوعی؛ رایگان و بدون ثبت‌نام!
🔺
بدونه اکانت و کارت بانکی
🔺
بدونه کردیت و واترمارک
🔺
بدونه هیچگونه سانسور
🔺
تا رزولوشن 1024×1024
🔺
چندین سایز تصویر
🚀
فقط وارد سایت شو، پرامپتت رو بنویس، فرمت رو انتخاب کن و تصویر رو دانلود کن
⚠️
مدل دقیق استفاده‌شده مشخص نیست و محدودیت رسمی روزانه هم اعلام نشده؛ ممکنه در ترافیک بالا با صف یا محدودیت مواجه بشی.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=mZlxKmgmKVygeAH4JM9kV_eQhFrpn7bkZwLzlv1zMsYXGtbUARdtXbMWCz0ZHxQ5aDZhSqFJ3ejmtXAtKOVP47_M-1CTZE0pCtVoG9j-cEDKKACPdcY9eqfjois0xfFNubkgOxTKw9g7SvWdPsbVqorf8xqQGfJR4b3DfObtBR4L-Td9ReVPYdTZAtT_a9JtfjIexVJfVR3xDHEMd6Y_04rV9FA-JhiZaT169itGZbCwbMsCB0xzer8BSV5v9CApS2ZG7vZNCAOIV_MHMEJQg58exle6uolK25LoAycQJXhsEJp1s-EmD0Bv6nXQQrujZkPj1huS-zF9ZkBSnWmMrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=mZlxKmgmKVygeAH4JM9kV_eQhFrpn7bkZwLzlv1zMsYXGtbUARdtXbMWCz0ZHxQ5aDZhSqFJ3ejmtXAtKOVP47_M-1CTZE0pCtVoG9j-cEDKKACPdcY9eqfjois0xfFNubkgOxTKw9g7SvWdPsbVqorf8xqQGfJR4b3DfObtBR4L-Td9ReVPYdTZAtT_a9JtfjIexVJfVR3xDHEMd6Y_04rV9FA-JhiZaT169itGZbCwbMsCB0xzer8BSV5v9CApS2ZG7vZNCAOIV_MHMEJQg58exle6uolK25LoAycQJXhsEJp1s-EmD0Bv6nXQQrujZkPj1huS-zF9ZkBSnWmMrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدها ابزار متن‌باز و رایگان، همه توی یه جا
💥
🆓
سرویس NoSignups یه دایرکتوریِ از جایگزین‌های متن‌باز و رایگان ابزارایی مثل فتوشاپ، کپ‌کات و فیگما رو جمع کرده — همشون هم به‌صورت آنلاین توی مرورگر کار می‌کنن.
✅
🔺
بدون ثبت‌نام، بدون نیاز به کارت بانکی
🔺
توی کاتالوگ، ابزار برای برنامه‌نویسی، کار با متن، عکس، ویدیو، موزیک و خیلی موارد دیگه هست
🔺
همه‌ی ابزارا کاملاً رایگانن
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHmo7SFt5I2H_FW3J11HL2531IZtZoA7uShyM6nOcLKhfdqcOxT4S0gGVzG9MxxtFXYD2b2LNU02WW87YqxZj9WTbmlPwxby_41gxHT0tU42eqlhBzwWaRsBCCC2NIP_I5NrSXiS4FAtFx9-wtrVlIVigDwrUsRLGwtToMOVDnH5uRgzXo4lPPrZCwtLZ0ZX4QIoYC9lhQDvZvgYv_jayyiTZSKDfyNTLimW68xzacHTQ7zzACeXV7l7aU0cFx1mrtSk4k8VTFJScjeS0sg4ptrbmqNorrHKdryCHc6Mrr2fRiB_YYNPLBGKokUA68dpOANVS-t-AU416DK7U_Vd2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجموعه رایگان ابزارهای تشخیص محتوای جعلی و تولیدشده با AI
🔍
سایت
forensics.media
یه سری ابزار مرورگرمحور برای بررسی عکس، صوت و فایله که کاملاً روی دستگاه خودت اجرا می‌شه — هیچی آپلود نمی‌شه
🛡
✨
چیزایی که می‌تونی باهاش چک کنی:
📷
تصویر:
تشخیص ادیت و اسپلایس (ELA)، متادیتای عکس (مکان، دستگاه، تاریخ)، تشخیص تولیدشده با GAN یا دیفیوژن (Midjourney، Stable Diffusion)، واترمارک نامرئی، SynthID گوگل، کلون/کپی‌-مووِ بخشی از عکس، و متن مخفی داخل پیکسل‌ها
🎧
صوت:
اسپکتروگرام، تشخیص موزیک ساخته‌شده با AI، فینگرپرینت صوتی، ENF (برای فهمیدن منطقه ضبط از روی هوم برق شهری)، و تاریخچه‌ی فشرده‌سازی
📁
فایل:
هش SHA-256 برای اثبات دست‌نخوردگی فایل
⚠️
نکته‌ی مهم:
هر کدوم از این ابزارا فقط یه سیگنال جدا رو می‌سنجن، پس هیچ‌کدوم به‌تنهایی حکم قطعی نیست. برای اطمینان واقعی باید چند سیگنال رو کنار هم دید
🔗
لینک وبسایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=qsvPPf4P2uWCFdIq6X9lA1xGZ7vu_9R_P52gYb_Uh6f33nFtaQQ_jZazZqvsCxFIbZX6ZOODAUeMdx1jutpiUOetifD3wXv78iaCjnB2j5o49sv3ICF-RIeFVcGRmd8e0p_BmxalM_6ccNKvSWPhS4yeB2xfm4zDjJTGSAEEhqRn2hswkfBbWKlNezEUUK1BCmwj5gTnxUBOEFwowy0f4OHoUGmWm9lSlzjNf8D9eoUSodhx5qKHT5FgyNLYeqXE-Dudr-vUUXXXK4klSQb1nY2HpfY5sUbiBKCH3NX6uv_3ma-2UCTxPPeujQSZtWt_EGUtupLqx41JXxPfzhLtFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=qsvPPf4P2uWCFdIq6X9lA1xGZ7vu_9R_P52gYb_Uh6f33nFtaQQ_jZazZqvsCxFIbZX6ZOODAUeMdx1jutpiUOetifD3wXv78iaCjnB2j5o49sv3ICF-RIeFVcGRmd8e0p_BmxalM_6ccNKvSWPhS4yeB2xfm4zDjJTGSAEEhqRn2hswkfBbWKlNezEUUK1BCmwj5gTnxUBOEFwowy0f4OHoUGmWm9lSlzjNf8D9eoUSodhx5qKHT5FgyNLYeqXE-Dudr-vUUXXXK4klSQb1nY2HpfY5sUbiBKCH3NX6uv_3ma-2UCTxPPeujQSZtWt_EGUtupLqx41JXxPfzhLtFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوی ترین ابزار افزایش کیفیت ویدیو رایگان
💥
🆓
🎬
هیچی نصب نمی‌کنی — فقط فایلو بنداز توی مرورگر
✨
خروجی با کیفیت 2K یا 4K، هر کدوم بخوای
🔍
جزئیات ریز هم تمیز و شفاف پردازش می‌شن
🎁
کاملاً رایگان — نه واترمارک، نه حتی ثبت‌نام
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI4RJuYoJol8afKBu35T7HP1P_kX4PXhqTibWcf_EtdJH2Wz_TV2mEnrWNT4KNPLl472MXWeWdtcvfIfwFEd5_jEAa8N_PfSqZOJj3eC35QaT91uN_8LlqMWLdIviw1Itz4vcPhOua7Mmlyh_69EZP4ECtoens-L12JeGgFyabbskKKtkOHxqA43q9jD4mAtDLSOJ5c6OD0YwVbYVv57Vd5zFRbKSL7uW_6b2tqkjvl343DJMFXkkBy2sPvWNLjBTFJ5NUHa4t51x_H7niZZc8gIs4mxuzD_Tus7sYa09ymWp8sMlF9gc3ruZnFlGfCr17GO1QCxaF6RG_KPvYfwJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به API مدل های رایگان
💥
🆓
مدل MiniMax M3 و چند مدل دیگه از طریق Ollama Cloud به‌صورت رایگان قابل استفاده‌ان ( با محدودیت روزانه و هفتگی
⌛
)
1️⃣
وارد سایت
Ollama
بشو و اکانت کلود بساز
2️⃣
با گوگل یا جی‌سوییت لاگین کن
3️⃣
از داشبورد اکانتت یک API Key بساز
4️⃣
کلید رو به 9Router یا هر سرویس مشابه دیگه اضافه کن
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEmnc7AzDaosmy0OWp6UElTKGnGoWGXeDQKNDvEQ5zv3qDrU5Qtd9_8w3CZu-49kLsVADqlshbLrp4A_aHSyXqidcQjvIlFgLvHW2_ByJL85c1l96gi7rS1CrQ1Y-qEsAYxJ0moT35QPTC7xxhmQet5Tt__4-QrxwqctwwomZHCUk6i6-4wnHkMUNv3FXuwogfaHKgweprJKU-ky-ajYzNjHsP6GyRZZf4e3mUyLdZhjTWZSkzYKUwOpAtXjEm6um607F5gxLTW_IdesFjBRt1lsEFeASwW97zD0Ef8bujjDzM-FmEPvWJg2AaeuI6gnIbGuwoE-g4gnwttaPDMIeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aKpK25lDON-J40TlJMc2kWpGWNCkKH5gUm9Yqge-UitkZPN6EHOlfFCXzUVhOLl4Tc8njU1UhelCGdCiEgTsoKqv1CbzWDZ9qjkw3bUAvZ6_ZZvz-AXq8qGldoR-3xVb9xuwuo3gQMhbEA1ydFHGTwbuyI4RzQ21KdhAIqyh0Kghj4OHjbDPwLeStquACLTr_Ui_ZWC43RAKiMHaRoZi-hOv8Hx-uRfHwBhGGJhjacnOpY--BGdUKbaGyOSRnFm1jK_4zmUdxJmZoVtroCJHfS-t-3oOnQFRJ-kySPrBd5JBk5ElCsaOvxHdmkCH_dPYmG08Yme2CbAwinjza2vwfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lk-dh_kzLQ0OhfD1asZZHNU59JWjWXCEEFyh2p3jaEJFHNG8h4abomkX-a-YhVtb5Q0cyf3kwX_raxssL0CZHr6IClqevrxZtbspn_K70is5iM8kDZ9-ZVoYqNidx6MDHGR8TX5GP8ALd9DsuQMJZSYMM29qv043l1ExFTQ6Q-1-n6G7Z_hf3yBTsuhf0BFOZ2JkO8kwsXWyLUsMy8g-auxZjxLln7tz3oPjKsWTRXhk1qru94P0HHVDpRVZxFwFELmvnf7O0XIcjITVBo7zdaIr3EgRmmPaXe0eHwyoD9VDXA9V43IyZceP4rB_6yL9mddwNpeblPIjK8KZuHtWRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DXLqt_1BjJFx_S0CsVDweehZ_AC9thqKiVPnDp0HNf_-5GKsm7xh2z0GX9TSNKs4SQ75WthbveZe9TqLvKK1_P9HyYI1n7NU1dvslvGx4sqkmmSDXqRXoGLUgGrba4-4bxitL4rCjdnZE8jNxczjyLDr3_9U65hR0fcV9W37YWYDo1W2bNdOUf-jS-xpz3r2SephCAGg4RjYOzYGwoOOPD4FPQhh4GsXoltWxD6_b_qMFvLW-bD_teXwJpq2hSM8rv61Mx57yli-bsX575xWhYrSK-xzUjPrDPlMqJq80mVRiO0fftJHx1RrigR7PKa7SYmoMCDP8-XtbIbMP3KC7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rp0VTiM0UG_AFjdHhOXAcgS74J7F2Ixj-ZeYSDi3x0MWA2L6l7kNltM8VyfMcd9DwbyhwU5AT0IcI4jf0qKQRr9Rt_0EwR0V0eLfah-wYTTwlaAGxR0eziQfnmQfCMyS980XU3_1VvCu_zpq_UwwEhf-B50NmJdLjqohOxCFbX7_at0mGtdN9IFqeAg3VYI9wNfVPjyNcfUGLYdK23mAEjzIjVJ8ds_hQ6-XtspGsjrOd_XGKtofQbg8hmptcrCPE5b8bdrDOLwTl-QMdnSI9DOLaZ4I3pvQ3hwRW6kSrt6m64AyyqWGUoc5NBUTpikV0_0U_wziEndUyeB9-OGODg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDDQFvT6tDg7lOyGdLXZnPMgLmyQxjv-bQ3T_aPgkeOJqYsQoBJkUoQmi95tK96udsYRwPDrs3uwuaMvCSBLck8oMYeX15Da-51oivUMDnghMHWFkfpfCo_zoHKhWA43oKh0tsxK2owfCjAnGybiwBaI9thWQdN6x4b0xowUW-2bDNFJSMYqXKPZHT21nYDqGghcStJxpwmI416xHMp4qzzHtli3LgdfCzyzgcqMzrGF4WY8aZFQn1afVoc_AJxnTVYME0knIszmsw6en4k8bb9tmlmtOrllWjnJbn4saPFMdDvwTMK5KjJPXFbcou8ALZ90LpCDSHo6gCp1Av5-yQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SP3UtmJBd5wR7hEf2jf5jfgEe-DtseOT9Jse5-Ew7TQH_LtM39q21_BgBMoKgQDevZDwBK6-7PXXmyv7X0Cy2ytGRE7g-sSYeDoppzi741p1X010HQX2wM9clQX4rmcQwiLFW3Ub1h_anrU8KQN06AeP6d7zi59aRD1WkbmcE4XpVtr8jPPOpcHEreFQ_pVFhvnq3lAIgkfXR6GIFo-QfnUD6ieTZmJ7ZBH1FMN7v83qUNPfY1fcIlC36a3V1-0QjAhxwTss-aFMbvycUvqhiPxDCPu-NN98Auz1iK-ee7uurjcFJe-DYgtsgHx5QdBLcNFSMDCkE0M7w1CEzNExkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZVqpAtyUYCUI1SaWUoLnwBv-yHJktu7ejXRIQ2-aPViUTsuc3BrNMSCvoRoarmFdK4cwsg6UBfkdl8sohYLYcwmLweZKWfphOe8E8eiEenP15D9O4pT3-0VfeCpd5-RckjV_Y-6e1i76AxMlAN-Kp0r-YQi3d9iOpWPPKAOe1bA2-SvlZ-v-a1YTieO-8UAKk_-V0yVt77rYjQnbZQvdxrcq_RCZMy_4BxP4QFJbM91ddM6ubn36LKJm_A-NkQc1NzBtK22cyBDejr4Q6hQnvFo3wuP0gXpYtnw4DGHTx2PEHwaNMENKAoGDnSJwu6095adtrwSQyMubDRYDyFtLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoXovXr4l2ckNuJOPR-8UTuA49ruIuIoEAo7n3hbkqlbCsVZdZVEEkstsPcJDHj_xFuGuFNIRgQDwm2Myg14udRRZ0zmnqUAvddG_f2wEYbJCoe4-C-Gi_WVrBBjfJy-doyyDIiTLiz7ou6KzajngSNli5SpNKKK8f8iQHMiOKKDaATD0KI_TmPFlexF73mGr02R3RslmgWYJ7kjel3d7T1Hvpn0xYEiBrro32qkFYs5bWLGbBNH_mMuWd_uA-0vxYGkFj350ZpmfhX7CD_uXVG-Fa-lAgg_eyF_mHk2AvKHLPT0fD6EpD824w1LnvDTayK7Vy0V5xh4i2ITxWhZXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTPy1ksp5X9RoYCr00KfM5GC_WIGTbv0nU5C8JwHN1euVtEWofr6xWGUi3ANyMF1R9CjP-0NIK1Qf1FGFC_EPH5p8chm8eFMa7Mc7ZxQ20MCfvbMZ1xN0Cr_WPklAgkcwv_xL958iigm6pZosR5sflfv8rvNuWBMH1g8ezPMb9lhevFBbJ7uWbMqHSS8nbI_r86at7OZSeIHlby5WQpnyQhjV2mu-j3FhyHOSxCqLrhtX4qk0XxaQxfyC-4CMOIa-Ygeyb_WwFhJZLZ2buqUGc5UYyKWoMC0HI-cQqkzLg9rimP3FgTow2oLHqeujQ_NHTXhIOd7oXhgJ_ddAg8mrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJNJp__1ftO51skckS25tJvjyOpA4CL-YVLQYKHF6d2Qspj6WpDw8-T42Lz1Z2JUf0n4sZaL31NXBaynkiRkzeiB6wdzKzxO4GYAnzgzkbyzg4Twd91X3NOs9-IjjNYPG_TCnVb5bKJpZV6bLhvxdDo51nzub3pEQfz5WMSOTrG_-1sFEyRp27OVUNPiEJ5JPWEiCtt1QbEGDFWBI3hmPGrznXK1WI9KKZECeD9yvHhIIqShwTya458ErIItM_9D4onaPGaG1lDdU4o0r7213co5alyEW2ThEY_1Xze_wF3ehnH9LfE_cp9SqGyYVjZSGrPoR-rr7Hh8tj0PJOVbfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7556">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBZcwCkVm4ykE0mUYtKj_vHR8yHNz24J9Pt8FAlz25aRYi2YLmjJgAKuSJqPBJKn0IJviRAwfRrGMM-kXnDSWIHBYETqwpRR-3r0M1ikJ6hsQx6N-7ACEe3NAZID-UnD3PD2ZT39_Xb7cE3JWgPsGoZjho2o5JwZaAWgoftnzgHhl58MhiitSj3QHqTvoUelEh0XdzGyJjTXpEsWubcyeIzm1J7-5QcU1BmGfU99xCPrvtbqfw2FSMOxHoTgLk6rTD-HLIcA3ePSaT-LGnVqIiz4M2qGfXnKISFn6NUwASBEl_UXEavMpQmxnzxT9XTAxDg2I0geY3TmIF1dwXlJEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=GUWBoz5fKgm-U4Y96YLfXT0YaHV25Fw9zOT9dnoWhJ_pWdAj8I0hc8WRGiUQO9_8IXNCzsdTZ-IYHNphYqOKM_XfGmb4E8cIQPaa3zb8vVqeqeVIv2x6CNrJPWk-k02RSmyBV-wZzu0afkAEURUW7HiPOPoOGbbgVWpcw9uEBTKgzTg5jg7TagAiUQjRN1JdA0o0zVnQWi_l5LGjtolmA6NNbB8pZoKmuD2mtZv8EF1Up90ZVVxOy3ctJJnXw0Xt_AZQcJ_ZfNqOSwy3_4a1xzCAK570DZVkP-iEcjwi7fbeXKsxk73cL0vWuYSsns-kdSVGp2rWH92Nlp1gyTza2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=GUWBoz5fKgm-U4Y96YLfXT0YaHV25Fw9zOT9dnoWhJ_pWdAj8I0hc8WRGiUQO9_8IXNCzsdTZ-IYHNphYqOKM_XfGmb4E8cIQPaa3zb8vVqeqeVIv2x6CNrJPWk-k02RSmyBV-wZzu0afkAEURUW7HiPOPoOGbbgVWpcw9uEBTKgzTg5jg7TagAiUQjRN1JdA0o0zVnQWi_l5LGjtolmA6NNbB8pZoKmuD2mtZv8EF1Up90ZVVxOy3ctJJnXw0Xt_AZQcJ_ZfNqOSwy3_4a1xzCAK570DZVkP-iEcjwi7fbeXKsxk73cL0vWuYSsns-kdSVGp2rWH92Nlp1gyTza2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=QUk1VLk6ryxvDUc9GElm_6SKGNQynQZcstoffUlvgds_dEow06tgbDOqFo1vOD1m08leU9u7fg92Fg1LPXVyLsUARnF07xj_yiTuoJIZGPYefDKWPIDZjz96sNre2ErtOHN_6p2Sv4CWUvxcenz7myBKPPk3rkdlnef8VlsDd_2SCEY4O41mcsi_-LzuT8_twiIlZH2iEOgySvr8Q3rUD_GIJr1UQno1YoJEIeED8QMHrjrtJsJ7C3W6XlFwnwTmsGoEMFIWVc0M54Wy-w2blmOLZ2sj8ThTXjqTTfTbQTW3EU-yYHVRD-GjOqmrlh837abGjF08-ygK23jtzgGatg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=QUk1VLk6ryxvDUc9GElm_6SKGNQynQZcstoffUlvgds_dEow06tgbDOqFo1vOD1m08leU9u7fg92Fg1LPXVyLsUARnF07xj_yiTuoJIZGPYefDKWPIDZjz96sNre2ErtOHN_6p2Sv4CWUvxcenz7myBKPPk3rkdlnef8VlsDd_2SCEY4O41mcsi_-LzuT8_twiIlZH2iEOgySvr8Q3rUD_GIJr1UQno1YoJEIeED8QMHrjrtJsJ7C3W6XlFwnwTmsGoEMFIWVc0M54Wy-w2blmOLZ2sj8ThTXjqTTfTbQTW3EU-yYHVRD-GjOqmrlh837abGjF08-ygK23jtzgGatg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت خروجی 0x Alpha و fable 5 در یک نگاه
👀
تو کل سطح اینترنت واقعا اتفاق های خیره کننده ای با این مدل رقم خورده
🔥
➡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7548">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-Unjl7b7os7J_q1FllOfs0FXfauFZzzAk3_ulTKf-vZFkE9Bbu085QakepkF9aYAmM3LK0WLmzj7E2OyoK_agkrG9m1JZ4JlZ8AdyoiGF4ppkfTw395at8xOceCcFElVBjuc6UzSzLRDm6TDPRwhc5eiT4nJf4KToGFUFckHd3DgCh2QRiRJwiBuykjjl7qZlJA4__KXdEvz04A3vUjKSamCbUdIyI-NiLTMJEcvdkwe1YVPy0P2i4AuOIv-5l-iVqCypVyvSX55nlTUfZUzeOGTrHB6JkfPOryPfgI9yOZ72_ouKjZrhxtmS6ZL_R8jwdqHAYXuFC0uKtIY9C4zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7548" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7547">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srOwkKPGMWDXPfpoQ6k0MADE03eb55bKjCR32nIPEtw_JS3GKYxyQyxGQCzQm2VIYCGOmyMl5fG7xwMlHBH3i8rf5X1_QFaNvWLs0pwiLKYmNjQ7n98vp20Yk9aX4c_Er9WGUHEt2J3o53ZbLb1hdZ275JhxUMfesLRPwNKgGp7hiXi4XPJN0hG3prO3jZ2TKsCgioRqb-AoZUU5uyyAo_mwOweBCugjcDBEr2N0417IrTekxWpUGRlJRHGTU8zx4C70xq1TFCU3mzt0HfHyj-PNq61zx73oPm9qwMpQR5hc08rBqAMNiInpSt0cnjBgOPxcaTr_jHuO2Vz6GMqQ7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6Cry_4i0NyNaNXLEJASjDmvwe0GQZ44eSxap0CecN_NpavUZj8xpyJVX63_9SqUHqtJS4pfP7X_ojFsGAyAUEZ1-ypNuU-6CKf5SYR55dctiK9Qbn_fsKmxFrqc8R6k5_9Ba0W2GzWBkfMqYoJh1nVY39x14Xs5x9-37vzDys1SW_DkHwmPbx9oyvIJneHhmJLaLUveQwXhEy3qPbj3s2L53f81fHVMJ-jh2_-kvl6FdYxx50TJS21vXR3IC0Iyi-mfU2Ztik6QclE5B6M1Hkg8tL_DAIehKddCRVQu-p6Nz6R78qqM1KlwWy28RBfUUuqkCcGrtOAWcP-9Oa8xhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7544" target="_blank">📅 21:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7543">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به
هرمس
اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7542" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7541">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7541" target="_blank">📅 19:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7540">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=N_3kLazQMATWx5AWFK9A4xE5va1rFra8S-koGxyPtfRNlPsfPdZM9EdeexVQU8VAGXEhds5nJB3Fo_rKBAeqfISOR_MAcpMgCyt7osH8hZ8jbmf__v1ieU6TyI0oORpgY44KBFgGaWqbfhH5JV6X8qBoYCx3EEcielZDMfexmCL_556f3ePUZg3Y-mU7lkNLVDpS4ENmRbhJvmkogVKLcHZpsM7rvqAMXARM658La_etq0rGBRfCjD-HpChmowUOssYhg0AGrW9lsRnkvF71gxCkafHvVNz4V1ajHqFskVLlaVAgE-W7xDK5E8hFvvZjG4oCxc_BsMMnTna8eakNSxVBAFHz57Qh4TlGJ0ZOMA2l7Hjn-m3Ks0oz_Jk07noHS3IREbeAwutOaJOFjjG8rGXB-OGTNBO8dRNSab-8VXionfYHD0RXbJzkORvro5_kAxHsQodmG8JRrtMvLks7HxLZiDnVIYYzLsKAvbd75WB2COSBfC45Y98s37vmYexJN3oerVJoUpG1-91BPvaVsieqOOIDAc8QLPGQUi81rcCLdC-u508RMiVqe3_j6l1fGHZw44Piws3b2IShWOd2nhrP67q8bGJ_vlqFMa2gk58ASRKdqr_Ub558oMzv09thVBoiFViYf7r60YS37HOWhmXKLdA5IsQniSOdCSfsxvI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=N_3kLazQMATWx5AWFK9A4xE5va1rFra8S-koGxyPtfRNlPsfPdZM9EdeexVQU8VAGXEhds5nJB3Fo_rKBAeqfISOR_MAcpMgCyt7osH8hZ8jbmf__v1ieU6TyI0oORpgY44KBFgGaWqbfhH5JV6X8qBoYCx3EEcielZDMfexmCL_556f3ePUZg3Y-mU7lkNLVDpS4ENmRbhJvmkogVKLcHZpsM7rvqAMXARM658La_etq0rGBRfCjD-HpChmowUOssYhg0AGrW9lsRnkvF71gxCkafHvVNz4V1ajHqFskVLlaVAgE-W7xDK5E8hFvvZjG4oCxc_BsMMnTna8eakNSxVBAFHz57Qh4TlGJ0ZOMA2l7Hjn-m3Ks0oz_Jk07noHS3IREbeAwutOaJOFjjG8rGXB-OGTNBO8dRNSab-8VXionfYHD0RXbJzkORvro5_kAxHsQodmG8JRrtMvLks7HxLZiDnVIYYzLsKAvbd75WB2COSBfC45Y98s37vmYexJN3oerVJoUpG1-91BPvaVsieqOOIDAc8QLPGQUi81rcCLdC-u508RMiVqe3_j6l1fGHZw44Piws3b2IShWOd2nhrP67q8bGJ_vlqFMa2gk58ASRKdqr_Ub558oMzv09thVBoiFViYf7r60YS37HOWhmXKLdA5IsQniSOdCSfsxvI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7540" target="_blank">📅 19:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7539">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcb7V5bqNtELQ7ShU7KI-LcyP7yl7szjcpZI_uGOW_PIT7pw5XM6mAYaPdnwYaZTdOGkQwEGun_I2EXIk63ZOxBuuqC2WvUasx0PUL8AFuBBsDxPbo9GPsVsTWUUHyZFHlFYVKEeuP8WGvU9gYQJx-0ryL4C7DDsIvToqiG9CG3YfT2NA1rOeoUkvPp4wYDoEW29RUgVaW0qt9PLEwz0BljP4iMhLL6qfIUtP9TTvNs2nuoK8g2HOTedjim90lH8DydZ5NfTJI--AZUERor907G5mWsce7L1jLtI2Zd-TCOdC3rUcXg1zZArpdnfoj5xhFEH_FjBVsNV08mFA_FAdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7539" target="_blank">📅 18:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7538">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2QWnU0tXLeyhsuKhpDKcpopkeSNbmk5GUGgDsiBW-DnHJmBCB1B3-v6ZkRu_ld-zRJY5mYxOAceIV7OPf_-IAjmwAVldE4soe4ol0-DfEuiVUNiD2t9AGhPs8PZzU5xuhpsW1jqODRJT_i-LkwdtSkEwRiff9riCmebTlwLcUFtYCaDtsR0Jz6pKRnhmlmxC_oK76B6ZkLWNEd2Y7QopeIJExLcX5iWN8qLAXHhRROsBW_fN-O5cahhWbaJs3Q6soJZGvG-5fhmkikGnrg9HsWScwshTV9vrNE8gZfeCq84Nyt7OjX1JECQG0M5_wq8SHQscGkhsotsVcx0yb22lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7538" target="_blank">📅 16:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7537">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zm7_mnSFIY_vt-n2bfYnE8BilybBvRoJqMi-UI4kHhYP9Ny4ewphYgPuAW-phjPWDnPEWByyLpoSlczZFPBVHflUbt-CbJ8tTKcy_jIgA_X6jui-otYYnzhpYoHEuhyCMr4AalQQiNmmK_37mAWXzOAswxzNojU1vOQvPPiCE18UPAEgsiy_cdCJt0RbJflovabN38j_fV8AFDEuw3w2apJ5fVnDeZfZtTJU2A5lAliJsfyIndSVBB6_bENKZhWpvgc-HoYV5m2PX4nL5UlMQ-8roC6VQuXPWqMY6x73LG1zd_VJTY9O0wc6PBEw8s66vzZUhukLOlatrsUuCRcD7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7537" target="_blank">📅 15:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7536">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Av4ly-MbWSigssttf7kTPiGveIhKt9ZwZoh5w96e5esYMBb0_uIHn8Y9CN7dhv9ewuKbrpJvFS4_LvaUz1zJRtWz-_wDZDKJC-uVLVloUNp-AQS_m2QoftDZtYtX9c9u7MIUWPcefUSIKgEQcryDVAmZt7le1aM0aaOtg8TcsZtSw4hPbhM057G3XXQpqsKVKWQvuFTKjwnK4-WllxOcdBNB2c2RDcatwn29UCQZQxQLjkPgPLACAqT6aj9F_zHq-Mue3STEDJxKeQ_lgDEFpAO-RXyfmYpQwWpbFo3zoLA63I4Ko4vQ5VALCztg6SDQJzNf_T_R830-2VKaRjsJbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7536" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7535">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bA2mkhKxw3Vdu-Fp8bESr2sGBQ8PSrWtJEdLBbdaOjsSLG4OtkQZVaLqvUKuLqfk1acXPb-Nj1b60jxC173QXBX9N220YdDjuZHC2d_QEeBMXK1UYly2AQiey1CEndis9tAetvxhzQCROHPyIAfbhpz3K3ahAX-ZZexXZkdHedLoEe8o502q1Mc-FhLrku09Vgnr8P2U4DlLEakB9uyaoc6QtzzzQmCII8RaEv7XMIeAFBCD0OUyf6zrntP1-OdIX4o8anVUpjWk4b2bbBvXNuyOEhgOr41bM2C9T1IP4VLHpwVqDvX1o7xTxlPBXQbyxyoyKium5rizjWZ5ifzzcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7535" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7534">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7534" target="_blank">📅 00:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7533">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASdbhgQe1aieXyws8XrCcPPHjRcuHXR5uePs3MySORlVOMvP8QybTrbro2HurezYKPYbMuROj3kZwW8_A6Zz65nIlXm6u_Lv67Zr49b2Uj_evMlx6nc59fHA3IzT_c3k51c3L62V7X1qrlpTqYRgjFuiGJvCCqCNUFqQbeehxyzEdeo_iMcJwNdQ9PV8OMpLyZH1odkY6gd05nqnMZ6lGFQr5GZQocH41NPd6x8azD4EH0V8b6FnmZX_yiYdlAQE66ZtpzSgMhD6MITjH6zKgIZT1mSkY3yDPLsbXNj8M2kaA_IIt1pMlMn2N-mx5Dv1j2o4jOhxP6a_SI8pNfGr3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=HgKYT_BGHk0Y7nryfyOICU5O1YuGQoif-sjy5od4tnm4W4bCpwJcZItJZacIYK_jz83bwlMSwoleDczdEMBJLWqPVhXX4lUdB1yfKxp83XJI4XN2lEsV03DnvEB5O6sscMqCpxGnnzZKRMYwizGtUk26ZgTEabKJDhSaMPyAcN3JGb0pBYOBXRWXvpt1TLnYEzJ5ycCR8iNlcPN8JsKFr_1zZrLmOMeTs-sE8HkyVf-52M2edjRwJIm7WcrnTkS0uA92S-whPBrIyAiZG1pxaA8NG3nU4nA2ldb43JCDHBl7otjwgTM9vfnvLqtbKcwXTGK2Nz4TSFj10ZbNP0WaIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=HgKYT_BGHk0Y7nryfyOICU5O1YuGQoif-sjy5od4tnm4W4bCpwJcZItJZacIYK_jz83bwlMSwoleDczdEMBJLWqPVhXX4lUdB1yfKxp83XJI4XN2lEsV03DnvEB5O6sscMqCpxGnnzZKRMYwizGtUk26ZgTEabKJDhSaMPyAcN3JGb0pBYOBXRWXvpt1TLnYEzJ5ycCR8iNlcPN8JsKFr_1zZrLmOMeTs-sE8HkyVf-52M2edjRwJIm7WcrnTkS0uA92S-whPBrIyAiZG1pxaA8NG3nU4nA2ldb43JCDHBl7otjwgTM9vfnvLqtbKcwXTGK2Nz4TSFj10ZbNP0WaIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsDrtvtOwhiLwpm8YBpkYEmO_29ZN-VzN6mMyT_b9FofaN7LnR9Ay2eEv1f-C7sVAO2vX1Q5hHUTfcY4H9dfscdmEjFF9Vvo02TtB5OOTDQMTPPMu3d0CeheU8rAatOW8JkAjCVQsuCqI5t-XAjXfG3QVA3g2biIVPYCHnLWT1yXCAw23Q79YA62WKvYwbmYNU9Sg1KkifgS62SJaTes8Y7aMXXaCegAfGOmyI7b6nsSIgfwsTFYePyxHxNOBmjh_oHiRjAGyBD2x37rU8z3tq0paekPAo9XPF99SXpnT0h8Ro8BGaVAHfVBezBkT3wcu37hqKyz3DwSguaNsliKwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7530" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7529">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdExpO7eUm-LMRpnMhim2YyyUrbxcgsr85E8TFt-Te2fofpGXbPQATvlnJbjQbgta1OOuWIQrhchA_4ux4xMrcs_XjMSH440YplS_7itqBqOraRd8NrMjQmJJ4Te_q3vx9kPg3ZtABLNH9v-LQiJKKD9QDt3FtrIAeuy-bzGtoIo3ZITsmdKHWKi7wnbdTUn-BdnhoyaX0XgXqzja7HFth-_O42JHlqnnI1-txlrh6h0jlIcKf5DZlFFQEVCtvWIbfpGzbl9gZ_Yc39rpWiSL42eSQA5xe8mT73COX75Rgxae3ZZOLuPD7Zbj_e2C5ugKRAnx542eSTCeTph0CvROQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngBdvYb5CzmHIBiM7J8YlkeD5CTcl2HLbl5vgxEoSh4ZZd44feDKciRCCjdl6hdOi8sfCSgUflTXFmGCZHJRrddZLCSqiWQN_itdVkK9oaEF5cMBYZir7p6JCmINlLh0IAKjXaIaRmAZxVRCJCizmAIjgceT5KUBUeCgo6pieM8kYK8GCZvPZC-LRfE6BZe-Js4shRn_-MAjzpNZIBDH1KrtOCGY6UhQv4MjWIPaaWtKGjfDndyj70YFo8QZc7ADNo5ASks2A-Wx7PMQ4T_ptNt57gDy1rY4pUFsS9bZIluQXHbtdFlbK65jkeMcACl8mK4T7Q_9Sa1mINQsuvj5oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7525">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BC5Ub3gnWzH-yG1lhOjXoi7so4L71RAL9dxbcbalELmgB8l5_LvcA0dAvIByK5Q_BcxbiqaXcvs_Pmh5SpBvi4KK5apYgFUS5S6V69JfVD0-hisRil_84atgl7RhaHODHYsQ2SK86hc4NAkL4zcNs_aemrFxlu0j27vB5O_bcg1eN3wfXUp1uCmBcQRVhDis7bF74yht52yDB5fzd1gv_mdMJWyHsRuV0cNaV6DdfrlFh7pHjtNncGZouZTTgPobANrCYxjw-Oze87nQoZc-4sIIOrrKtL5F_s_oYGzrjhYhHiBM4s1hxriv2qG40q2ZePEp3WgV3k753RF06LlgAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7525" target="_blank">📅 20:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7524">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7524" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7523">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLSjRqsFV-hLwWsbL8u8j962h4VXKhh_KazRgSAkWfHQUd3aSWbYTn9WpBgQEK37Ty7A2p3NeAqkYouaGd31uv1ZtWxadlOUHAqdPPp00NVq9xESMkAyBfLFeXZPBcN4fVBIma8jGU6ZNtStm7FWTKeHqSt9m8oauX8yvwmuk1huhcpd600NdfDQhuXqaJ5m_m9JGbmlClQoWXPkZhvH0uLRrCacyc9tkoh9PTOBlBkau1Mg_msbTk2Rz23RY9SvWEPIhhQcUyp9gLy5f_IMDC-bXz-1v5eTpvFcwk-XQ2RZ2g7py4hss02647U9RXsKg7vNuSXxYg9Qziian9tbiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7523" target="_blank">📅 16:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7522">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7521">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3xkekHNVcRBx9EXcH-mQtsXED7uZ7Lq8WpHxV2IUjiB-ZkbyLG5A3EoE_fyTk6yV71kIWuKawhcgBA7GUKEHTnKfuDINeG5f4R6qNlgVc8DGOQurJax4EhyCnHsaUyrWWwJQ7nz05A1Nrz4zRwKdO0Z1yZVHVeViYqGlCgeca0zMGf861aRZ8axQyp5VROZHaDQllwNQ0nxQZ8rEVnBMqSKI1JutgyDcSGGh2CRmVblwm8BbB9qbehYeRkEKDb1nvBgG8N5dlHvzsKs3X7SL8N38IJTSzdHxWFlO44_JVW2ZN-5kZ4gdQcxWoIKVDHaKd9yn8azLsmLfiZ_u16naA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/ArchiveTell/7519" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7518">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZsKy4qgcybNCP5XoK0qoK9fF-kdVfL2XKML9nNTUwYqbaHHhd-WBGS3vvn_zKGJPkei0ts9ZELjGhUglBOK5BEHrwcmNgtsAA2kDm0eZzx5yUTzG_dL82A6FKYmL1N-7iLSLaL2A4hcUbgKfh0pszgWfVoS3wNgDYvAYNZrjOWfHZTD-IcDV-sVvgjdXhlrIK6cdV48kgxjeFdsxE8xoGTL5leaDJuxpOVbnlwCZBzCxAm3uMFo1ptimT3jI1inG_E3DyHYiLqm_-DxwTjj8ecAYpe99SGL8ikaSsjxsr0JzQ0YDAZDrGmtC9sW4-G1r1S8E1k8iMLDpZopBJUElA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7517">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7517" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7514">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqVrVLWls41gUfVabKcktygTkwCt-UqLKP7g4hYHpgDHZy1bdfwIScyeP401nrm6mMVwy7quxF91yWPVW5e5l8F5SLgpmCS-PoiP9TG5YxYqLcrwUNl64rXH-MYDVjChSJ9yy9QeecqkPunL-I6WPl-L07qaLvR7KDXlUZ4VRWPP_HJvvGEFhNIIx1EflmVuxa377_96DMfnziUhW4Syh78H222ADnbwwKJKr5Ge8wCNDox2S2IoeX4M0xzPWv1GJdCwlwd0VtnGP-9gEb4xX8MFkAmrqAeOK4J73iEi-KfXZIMUdqUiIhrgmL_IlUHhohGeBwaZHemDIteuNDpn7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xzlb0SDCawsGMkqpRgqY1lsbXU9hQdByTLl7scAfG5Onx3W7dHSNZrFLfK16zB587DSyjNTm6OgWFFndsc4-te1S90HMtHmX2akAbrwOpnZFEqwVGcYTTEoBglvoh7A52_YmPBLs7I2RIbcuIqiZ4C8NWR8tSVfbBn7dEVeYe_NnATGh5l97ThsgCjnscaPtugTJZ6SRqIW3BFZBAEyr_6FEZGrTVdFdYcXAnvriTjuT86Jo19vZdmvBxvAHqM-Q1gYSwMMd8IGFIgV_p6-GOlEcS73EnDEKq9hCakfvL_BUBwLj6LbGV8l82KFfB7-qyKmxg6BJC1JL9L0V1jiH7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=GRUPZVt7yvv5abGitv7nK6sX1BP2XPlzWyQ6xWryVleklUqCLvUVTeR-uyUheYwE1-EFHhxO9_2_2d6mVjren3VwpWthh7n_AvnUidzj8tPkKMyhCFjTbXW4VZNw353bk0EacS2gUbcGbI0uOVH00xKr88Wc2sWAEwg8t_cYxPiJDslZs8gjghvVgq4Cv85-tXYY3lxelKhMH8NU2Y5Oalv08oxA1UNT964t1C01lr0oON2_83q-9uuJFcRE-ZAjjdQ0dcs8ZyyJd9WyLgbHZs7MKUBxy341b7WWp9OaRuCVW_-qEnPhJeKDs6OmIA5uGj8nW4C5sCoWja1WfbrjC4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=GRUPZVt7yvv5abGitv7nK6sX1BP2XPlzWyQ6xWryVleklUqCLvUVTeR-uyUheYwE1-EFHhxO9_2_2d6mVjren3VwpWthh7n_AvnUidzj8tPkKMyhCFjTbXW4VZNw353bk0EacS2gUbcGbI0uOVH00xKr88Wc2sWAEwg8t_cYxPiJDslZs8gjghvVgq4Cv85-tXYY3lxelKhMH8NU2Y5Oalv08oxA1UNT964t1C01lr0oON2_83q-9uuJFcRE-ZAjjdQ0dcs8ZyyJd9WyLgbHZs7MKUBxy341b7WWp9OaRuCVW_-qEnPhJeKDs6OmIA5uGj8nW4C5sCoWja1WfbrjC4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7512" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7511">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/ArchiveTell/7511" target="_blank">📅 09:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7509">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/ArchiveTell/7509" target="_blank">📅 22:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7508">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfyCzedLf_5YgMieusWwE4elDsJeb-5QOCLjJvMj4pjEEQWPjvTMda77fYSUcXXm52xxjF64z9tWQCeYkztcLYkmmyom-ilAdMheoYrOL0mNNB1WgZmR4xYvKq0EBdf7R0g6mjv-5pixTE5F27T4Gq3gyY_arnQVxK2E8ghhLN7auDPuUU1L9c3OnW3n9feGKJL_PzJSkM74sch3u8yGt4odbW0iPj75quQN8SVwGKUOV1026hir4Oxn7zESdZO99mLmI8krkQEl2NWmPb8zRlFxRS1yk83ABKisXZ3lb63vQihAD-jvjmfb5GQ_6QQhSoKDHns6oVrnLfwFlLJ4cA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/ArchiveTell/7508" target="_blank">📅 20:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7506">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7506" target="_blank">📅 18:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7505">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWZjodbVmj8sFMeM4Bsmu5A7wt4VYGFVIfcpLO5EOfIWiZj2eyIPlZaN2Z83Zp6m2Sux8XP7MRyxG3vz9vsPWHI8lpZH-jHntMlRTLaphc56e3gnKYkv6pqjisnnh7eefaMbuqiNJdR7U7zlrEI1TJiaZI8DMfZ_-04PjZMlgfMBypYdXlmg69rGR6O6urmJLQGEt1VipmQQLYpDcDWp2w0JqhH0NcsD4nqtGTDnlruKleHcytrYFreLiWd08G7yXHoHMDhVc0D84pmo2YQNT1feHt93LLt5hZ4ZXAgNWST4iZoGizzF5H-tpYjhqLrjwLFPSpNQ8MB-7O7LNEm20w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7505" target="_blank">📅 16:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7504">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkQKx-1nz3AbaiSh4YkLJJXtd2fygli7gLOY5g9ynLmtqXI_m7jEzwLYzx6-nj47NiLpcK0BaPy1vLLdQZUuq-9TZT50zXGB6tbWYrht-eO-2D1No9XfNYj7ThTBNNA1Olkbd0-VCV7u2tkMf_k-0zs8RtRScfR1ZKdRJgw088O4zXTWFrtR1UYO0jK1Nx5u6_DjZEwOz7M1IKyPOhIoAe_TbOzRXO2UFzawpULuYwj4oV7H9iVxOpz9JS-eGFwllUYnFiCf1cT5Tz8QPmAFmGURhhX73xQvlTU7UqfkQ03pg67REVux80T7UqLmH0j1kWruhGSexVA_5J7A1WgdlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/ArchiveTell/7504" target="_blank">📅 13:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7503">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7503" target="_blank">📅 11:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7502">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hem-MgGyiEyDj6lo5vV6ficxtT9KuLONuMsiQPhEmy7RF8rB0xB3QFWTIIAASS2kLU176kSBCSYGg7JMkz78gHbRs4gxC9uR2-uLEaU9UPL78sBmZXF6ZoaoRuqBZ-S3lnYYM8F3QpwS9e5By9ipfcQTr-1qGaeNuPKsxNJ_zXAvYXg8QiznhZOebaPRWZvak-82GAW7slxsoZRS5bIGTLiQ6ieafFg1Ca0mxZrMB-2pkIIJJDAmPw3WJlxuaqh4GhgCsBa_xYXOwYQuMPdnscd6vwnn4PJMkPizoq9_S_AopE5F3nlzJ8h3gUd_my-wYbuucMzsbnqLXTYyPcc3Qg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7502" target="_blank">📅 10:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7500">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=WnrCyAoDDMkynjJbpmdlJVlB-f2HqkQBAuB5zcUdnJxeZ5_L1vWvAS6DmPru-S1wBdXb9wxdhJwsCsTonwOgSflcVkIi8YCqmTCBjcjRS0aR-nXgZ2l4S17Swz7UAysKsvar8jauGyWl7pgqjPcFesn-U4I7iHQEqX9yufQF4krz0JR_pXs60D1ZpW_OvaLumVz3aMBqQmmIKN9AVvf-PLxt8_tR9iqUI5xne1oP0XLYt0Or8EP2UhN4umBVUCH3dB16vMYYww0LPidMaYBZKUR7saIqI7BumPzuzY7iN3tr8425A4WXqoy9ITKbRkxxyrK2IByHdLgV9ZUGa8yxdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=WnrCyAoDDMkynjJbpmdlJVlB-f2HqkQBAuB5zcUdnJxeZ5_L1vWvAS6DmPru-S1wBdXb9wxdhJwsCsTonwOgSflcVkIi8YCqmTCBjcjRS0aR-nXgZ2l4S17Swz7UAysKsvar8jauGyWl7pgqjPcFesn-U4I7iHQEqX9yufQF4krz0JR_pXs60D1ZpW_OvaLumVz3aMBqQmmIKN9AVvf-PLxt8_tR9iqUI5xne1oP0XLYt0Or8EP2UhN4umBVUCH3dB16vMYYww0LPidMaYBZKUR7saIqI7BumPzuzY7iN3tr8425A4WXqoy9ITKbRkxxyrK2IByHdLgV9ZUGa8yxdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7500" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7499">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaiEuMSbZoagYPuNqvEY-lqitwm8LBgFqUsvZWuDgalRFG-COZDPh64Qzw25Mvi4PO5nGc1Lg2RBgEqi6JOU93OXOOPfVVSFG7bjD-ZCSVP4HbtK4ZtX2FjQ15YXv1Wp8rNwZTuBQq_Gw8yuLnUXeaHBPpb1nPolco1Lbow5lvfqf6wvyZtYmk8XoR-vuQsRFgJQ7N_aZaGnBoiTTeYyM6coMGYWrZYpUmnpCiz_nnOOECaOdfC-NC2HqXtRxxtFEiLxEzbbcRLH39alDhxn56rPOBjB8jI4s7QfG_SgXVKUJYRforA8Zvbcp2WTFnGMNdKlcs9EhTIueoSvK19vJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7499" target="_blank">📅 22:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7498">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=AuVYcwvlx15ik0syKkleP9qRyE3jA5GBbTtXtJ4IXSMQ6T9fePnHifEkLCCSZ6181C9SZ-0ktDGs0fkjxtCW8_OvHqQ1vdWYpIyx4zWtFo4KSyI44zREdkBUKq6yXONZg7CrUJv0ogHVIgzJSvccf031_39dPmCzw-tkb6rOgyUozfpMnCBEAKT5Hd499BtSPxPU6uXvHQGJ_VSmt1pxTC30uzn3z7o-RMrNxAqnjDLZOZl3JCAPbB7TinySvgJur8tgFy191W2gs2qLB6tGLarTQfNX0VtNSV6EwrvpO72YyjKA_EcDhxQFE7aEr1rURkTaM5p-Lq6Dao_AQlgrUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=AuVYcwvlx15ik0syKkleP9qRyE3jA5GBbTtXtJ4IXSMQ6T9fePnHifEkLCCSZ6181C9SZ-0ktDGs0fkjxtCW8_OvHqQ1vdWYpIyx4zWtFo4KSyI44zREdkBUKq6yXONZg7CrUJv0ogHVIgzJSvccf031_39dPmCzw-tkb6rOgyUozfpMnCBEAKT5Hd499BtSPxPU6uXvHQGJ_VSmt1pxTC30uzn3z7o-RMrNxAqnjDLZOZl3JCAPbB7TinySvgJur8tgFy191W2gs2qLB6tGLarTQfNX0VtNSV6EwrvpO72YyjKA_EcDhxQFE7aEr1rURkTaM5p-Lq6Dao_AQlgrUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7498" target="_blank">📅 22:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7497">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hs_56qnR02xZ_kg47SGAc1QAN4MxW-Rkc_G29S9BU3M0uQjpIFki_Zguv4qXP6ciN2a5G1GsLW-uBwPmxTglsn6P_sy5M3zFw5cfcgUbG_e-PtUzkA07Hpr96p7ZQmcMfBFToLwtknr1SQ6d-R15FJqxYnFfJhZx2U7fn0qQhqo60YL9bjh3T-4krSmBPQdKnNDPrZNWcrEKEA2_ZbYZs39qVasV4GlSL72dSpp8vbbfGlVovytNJbFZKyzBKR0OcielRECYayHS3zQEL47EfNCexTlvXZyJvBTFr3LnLBmtenrSotu-ud8XWVJZPhBJsa8_LfXgmLrBJiybIfXtBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7497" target="_blank">📅 19:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7496">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umPMVsz_SHPbwRwgT8jz1vZbHsUvlSmpCqVxD2bxV6IetnbAKa8ktVBsl2gLquF_6U1jKQFZbbVgElMV4XdJCm_i0ANtz0Vo09LpbFnxNWAF1qRv32zdXu6zb_DA-0Nz-bBug37YwIWA3-y1phBzdPVb1x7ph7VQZP7FLLxvJaO1-KevmyBjb_hRYGxRbKF63f5FdVUA6Jt6zsItsEBCK7L37Ic2XuOAETcGBEqXINELeaOovmi2B1If_R0UWqNnsAXeFBAs2iIwtZIS_JwIPqxGf01yKoSmp0XMoKy4NF7Xlv5Uc6MYV800E3KtW1pYO6SC8vaq1_hOSFyUO3hkuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7496" target="_blank">📅 17:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7495">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=ijgxho1oRAYqGw1zI6EE5yztVOvz-41u6stasmnRhsXV4QwW0oz726j9U1Xt9X3EXUIVHGdHS8vwYZu7fgn6YcuPx7u-dnhWPepjmPHc29Xjw4lP8FepacaJ4ZeHM9msBDZaAhtb13540Va8A2j-cG9uXcCU02QgkCsXzhhhYR-QI6wNKOaLQmhtCo3a3iceht-lczjQZEl-9ElN4XK2KQ2hj1YZcj6Nd9XLl2UvMSu4Q9WtimhRzKVERmoB0oJ5ME6WYTjPyjBxjZE2eMR6_FomI4cR-_mQmtHh1LQ1z7zKjdfNNFLlPzN3GDLd4wDvZneeS455pD4nra9ur2sNTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=ijgxho1oRAYqGw1zI6EE5yztVOvz-41u6stasmnRhsXV4QwW0oz726j9U1Xt9X3EXUIVHGdHS8vwYZu7fgn6YcuPx7u-dnhWPepjmPHc29Xjw4lP8FepacaJ4ZeHM9msBDZaAhtb13540Va8A2j-cG9uXcCU02QgkCsXzhhhYR-QI6wNKOaLQmhtCo3a3iceht-lczjQZEl-9ElN4XK2KQ2hj1YZcj6Nd9XLl2UvMSu4Q9WtimhRzKVERmoB0oJ5ME6WYTjPyjBxjZE2eMR6_FomI4cR-_mQmtHh1LQ1z7zKjdfNNFLlPzN3GDLd4wDvZneeS455pD4nra9ur2sNTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7495" target="_blank">📅 15:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7494">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrENaGrPOgd2MAlW4uzVQkEKbcaE_IRmmVaODxJLIPn2BICA_b1wTU1OET70F9TYhBWIq2addcE1ALpiYyaPuTvp8qCUkLcteXkgB-ccgdp6kP9sITsBxkb0lvxyuhGD6EPnU7DoDAdTqhKwyjtWyNEEOaM-POWn2OaHg35L18cbCvyjQNk-yvBhgPZGptf4dgcMhWd3ch3dwio2dcg_h3Y1Xkac1PAYz5SPohJqrCAltxpz7hyXzJ1FW0JhCfiN62CkTLGAIlu42vwCooF6kq_N3go_ecaXx1EfQfSjGfkIemaR8J41mQ11oDAxRLfzUVrqmHThT6pBtFn3UMl4-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7494" target="_blank">📅 13:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7493">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTay4TZdVBvrB7HJZoYwiU6YwBcpDNXcVtVHyVC9WNJHquwBuvobEVjsfAJe-2vyZQbT-MwwcQr0zTyt5LsMcfZ0V8WuEZ-uaJxgqQirugEHCC2T8xB63n1j3ML3fNMjPya5ITodBtMFlQOjZL-EevPil0pcVAfYe_kPrS3JkucXUQgKxi_nvzdLLsgFAQxZwRMqvh0gfZYcj17XGRs1Bzv0ZQP4G-hc-iFz5rQSgotVnHEVfhaWrM8jhouGrYuNDtLDHDtFWDB0EczS3Y1aj4bj7s9UPu70g3nxIcNw4sMVAlIGJfe0rx5vol1plg1ZugDxFP5Hpl1JPMH4DmA3qw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7493" target="_blank">📅 12:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7492">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09dd417185.mp4?token=NxVbnsU18mL75oXIJMQBUAS67Zjt-d6wKcq-VLKBljqRaQHheqnB3AlEIeeWTx5ezzhGRRnWLnCZ5h7KuuOyum8dHLZxmCnMUeSeFrj897K8Yh5fJKVASFeLSRWSf25eg5zpxQ3m4SctK64dR270N003l2eZVh-EayNMcef-HGzmFcob5yxE2OP4d_QntGnmriwNLwfDCTOt2UZ9Y6AGkwgTCDaDQK8A9UfSXuU8WrnkK0AmK-_gn9TZ14IoL_t05wWNvGnXrzHbb3ETgpJFxiQXbr23DwIHBzgBFuyq9w4bSgKB5UQh41lOI9gL17oSeoaD7aCJ5KzEw9xcwaGVwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09dd417185.mp4?token=NxVbnsU18mL75oXIJMQBUAS67Zjt-d6wKcq-VLKBljqRaQHheqnB3AlEIeeWTx5ezzhGRRnWLnCZ5h7KuuOyum8dHLZxmCnMUeSeFrj897K8Yh5fJKVASFeLSRWSf25eg5zpxQ3m4SctK64dR270N003l2eZVh-EayNMcef-HGzmFcob5yxE2OP4d_QntGnmriwNLwfDCTOt2UZ9Y6AGkwgTCDaDQK8A9UfSXuU8WrnkK0AmK-_gn9TZ14IoL_t05wWNvGnXrzHbb3ETgpJFxiQXbr23DwIHBzgBFuyq9w4bSgKB5UQh41lOI9gL17oSeoaD7aCJ5KzEw9xcwaGVwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7492" target="_blank">📅 12:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7491">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMWRpPOws6ikswg4yg67arPUNY9g_3fjOvhm9NjQc-A1LZVB4vYmyZlJpPo_FnElkBp1JwBK-5ecx3PBqIE-6P_ZuOZ2R_5mGPW4TNh_YX1ut0B39s6r1RljsuyT5b3mELPWWHrPFtwGf9QCIlpqs0zPbJtVvot9gGCCRffHb_Iz0PueisnU4IrMZBD6NKPIBW2mAirQ-wiVTff8L1FiBDHJLiNcESHLDHtjhyuAv1QcO_-T-CyGXr6dFFGhPXJuJJ7w4sy_bIHVA-h8m9SLo4jVkE8f0Y7HDsOQ8t42nH7aEfTyypLwJPWoeMHyE-V1IgazIW0fhDMvYh-C19mekQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7491" target="_blank">📅 09:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7490">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7490" target="_blank">📅 21:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7488">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9PkVmCA5j1RE9u99A7K2Um5x4Z40lLHVEeDWeWpl6Q9Q0CLYatM5UAezOJjiP-gy-zePKgu2NV6pp2J8UJMYrZm6V-awpwIJw5b1YvMBITS1hfoo0CWWKn0MlvZqkIhuigdRrHfKEO5IPEPspwzwGnhitQqJR9kIwh1z4SZYLDOMILRte_V74JMD6Qizptfd-vRbxZsYsAGqy1lSTU4BeiPpnpjiXTpTlypH_RWji-eP-8A0OwoTrVO0_lptbZCTyY-_YRqJVsg4dnbE6yoKZs3bgzAOsYe10lN-6nE5aXaNQjBO9GTHcOmh_VURkWOwGEp_gBbWsdv_ak-Oz1uHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7488" target="_blank">📅 19:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7487">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZobqXF-SVtOZERizkDwwWCsvyXVa44wQskETbsre4mxfgFZODF7MDpM_xAXUvPkw--d7VIdKKJazfvipoLfss1rotV4zKXNEdvqtAjvSuoJ0LM69TqhZFNFT8RZMVunvWoeAUTnNGGNy5B36sY_dRHTyNyFqEHr8sW4NeEQ_5aitksuSjg1TAvSH8Mw8ILis5OcWEqT4jzcZoBJ2R0VSPeFZ1NrsIis_6myvDWwmb4JcsgKc5b3TrsenONwdJGVKU9dOmu-drWWACSRixUNg_HO8Bz4faRN9DNfszaC4ksQrDQg2l3hCHsB51wNKSFcCBtIRKglDyyyh5OCeBYI1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7487" target="_blank">📅 17:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7485">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HomhAvb5co99vbU22HlE3TmgE310J7OoLXnRBgom-2nseYQbhbqysfrOmhYrIgi4A1vDhvRCZk18kwHCyWit8uIZEcjIh-e01E7V0TGebatLM5DLBSs-zClL6Y-2IO_0EYm9Vrr-lIR7lF-GXOC3giYQS-2CDT8JQSXoNvjz0YvaAUJ-obcoTAqEC7MjCLS9S_O0TTlYDDTZJY4jBJ1MwBIBe5RhiEAeiwAlvg6pUqx7rtuaEKZguoLvy_T158neMioqSKe38FHZetYyimwprKxG4AGSfWy9oZrFOGaU3bWub0pfpbH5Gvxvj22KS-pzIlaq0NIIHYvhwWC8J09Czw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7485" target="_blank">📅 15:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7484">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuKkiJeFOu3FpkcfU4q27WO_1vxvdeXGH0AjX3TH14RCxc-1IW3sz75oqumSatNhA03nHBeofC77zEaDQw7L364lgPFvBKyEbOaqW-fjDPnMssrREVPE6mEcEnA79Azl-iuObROhAfkhanovk7Lw_1F6caR3Xg_Tu28yUWKY2rEuhy_RDbjgoOUDBFQ9aCzTqhndj6RidWdbztwD3jjsgnEviRiGHIulfRFa8TrcELs9J9U6j0AUO8FMwmMIXTWM2Alld3xP6tTZwf3iFbpYrKwbL2c6n5uwO_g1uhQ42ApOOyL2BdX5vLqAynq_sqLZRB_egCijDNEcy2c426mQAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/ArchiveTell/7484" target="_blank">📅 12:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7483">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/ArchiveTell/7483" target="_blank">📅 17:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7482">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6BCg3Ud_BkzF378oLAqoDSsnnmmC6R-bkw3BjfWqQC6B_19L688ENECznyWOtGWj4USZntFFx8_un3gPG8nT3VfCbk8JQk7d3KKtvADHsPRMpuPPD-KSplnAxKOKh0jDa2WokcBFhGBwakSeXRukkhy7h4OS7MAG8Dm0h2w7dFlEliYUQTrNa2edys6LaMCllNo99ZOt8dcSe-NiyQImbar7KPlMy0nY031BqcHiZfZ26O9vdQajI3j0BpVcPDE_dfCTxyllGVwdOvffcDyrJo8ooMqNf-rXtSe_9dgnxD56pGaqDrKebbfXbKou48tJmjor0mrpgz78tCvwdhRag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/ArchiveTell/7482" target="_blank">📅 23:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7481">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUJzZ3qXx0Nj0s-YM7KGEwemSYNbPNeTr266gMc4U9AzEkRLwQw8Q-d7ZKFVBwlqVwxLTU41rgH0eLOKuGSQyLCaz7dmyOsUAgeIMo6b3lr9jJseVRlf0qlRu3dJW8jRJxFyrvEgUL77pTDx3ItadHI3eiGIxOrfpfTjhHZ7ljrUQkHv9tAwA1EhntSya5kiip8H8Dfl0LcaWxULvTBndX0OMcqgvQ3XadOmk2UjKOPjgFrv96-H9s20Kc_WU2Z1GJih7ZwymMVj7c9AljcTpXm4fhr1A5v5LO3WuYquHzj-AyONqQV4PpJH6dWlTZEhKtSg7g6YLH1As1ks29cedA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان: امروز از ساعت 12:30 تا 20:30 به…</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/ArchiveTell/7481" target="_blank">📅 15:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7480">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7480" target="_blank">📅 14:15 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
