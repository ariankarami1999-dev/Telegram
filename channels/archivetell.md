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
<img src="https://cdn4.telesco.pe/file/HRo4bMBXEjoUwCtuZ51D-oGo9HJkBU1SYIb-E8upqxFRik31C3a_DkgfIOIwzjtW6KFnb3MldYKf3dSYvwaelU1fHSsOJN85roEuyQYionjeLOYovCB7UqP9yq3pd3F4uTOfSRetzhbldy6iZfk0Ct5e8VhoysQtxJKE9A3Yx_0_1UQDkexr0pJdmvdPmfovheuosoHhrkBD_e3sj1ETWABSnVSwLbyYiPLq3Ym4qEVppWm2D9spk5NBYvX_pyz9UPjqdqK577asRhoUpj9Uw1coXoqrSSfiUI7eRAGWjq9d-jmdPx46l-5kfLMFWAkN-UY86XTtO4v-Wx6-kbOpdQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 19:05:43</div>
<hr>

<div class="tg-post" id="msg-7353">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sstYRxVnFvwxr6Ih7awyPwOj_aPfrOPJE3V19eaWJ9Y-1zWV97T1dwtHCP1oOGnm72tBZ-NkrCZNGnPBqvQ2BaphFRhpYNLJz-3eCVesY9Ink3dcRI26DQoO9AuHb4VxzsMNC3fYtQvlBwTmp3X7u-wVyr1uVS2-J9G0S7oBM6dvqfK_96QgGKYuQij1z8LZ5CUbnSiOVbVIsDjAvbiZg7C8ICnAPk882mbr0jjbb9LazmCYoJcIgpgVLFJUMkirnHvpTugFzPz_fWslXOJhIUDWdcm6UOQCippxpiIR-PX1WeQAuQgN3YRCIjCBQ1nP95XJKQLmNvdjTykvO8yqfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییر خودکار و مداوم IP در لینوکس با IP Changer
🔄
🛡️
اگه برای کارهایی مثل تست نفوذ، دور زدن محدودیت‌ها یا وب‌اسکریپینگ (Web Scraping) نیاز دارید که آی‌پی شما به‌صورت خودکار و مداوم عوض بشه، پروژه متن‌باز
ip-changer
ابزار فوق‌العاده کاربردی و ساده‌ای برای لینوکسه.
✨
ویژگی‌های این ابزار:
🔹
تغییر خودکار آی‌پی:
تو بازه‌های زمانی که خودتون براش مشخص می‌کنید، IP سیستم رو از طریق شبکه امن Tor تغییر می‌ده (Rotate می‌کنه).
🔹
سازگاری بالا:
روی اکثر توزیع‌های معروف لینوکس (مثل کالی لینوکس، اوبونتو، آرچ، دبیان، فدورا و پاروت) به‌خوبی کار می‌کنه.
🔹
دو حالت اجرا:
می‌تونید بدون نصب و فقط با اجرای اسکریپت ازش استفاده کنید، یا اینکه با نصبش (توسط فایل setup) اون رو تبدیل به یه سرویس پس‌زمینه کنید تا همیشه فعال باشه.
⚠️
نکات مهم:
* برای اجرای این اسکریپت باید پکیج‌های
tor
،
curl
،
xxd
و
fq
روی سیستم نصب باشن.
* از اونجایی که ترافیک از شبکه Tor عبور می‌کنه، ممکنه سرعت اینترنت کمی افت کنه و بعضی سایت‌ها آی‌پی‌های خروجی تور رو مسدود کرده باشن.
📌
لینک مخزن گیت‌هاب و آموزش نصب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 179 · <a href="https://t.me/ArchiveTell/7353" target="_blank">📅 19:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7352">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIv5Z1M7sp0GlacpmOHsKUa7ltfjAPeIaz9ZWGVp7dC_DV6kGM0tqNOTG3IJH64Tk3u2fXAi2H5RqjXoCWRuXuDNu0seVjKeDMmshaNhpvjz-y8LU0so9E4NnUXZkq34npWdqxa4_-hb5SRnjqJNTXLPyIeifGWP4hR9ptLaR_XwXqGoqXmgq8lLeR2JEnvgXKBB78BBq_A7X_sGDCLFF7AMLrQ7xn_d0RpLznsmuK5bt_tLljXppuvM3LfCGelGxAFZE1wh5U7hf5wIG7u1IPxWno80Rj0oeI45vliqKIXTnJwPurszulFpntcZfQ9oshoX4LHBY49cyta_ekO01A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Deepseek 4 flash تا 12 آگوست رایگان شد
🚀
میتوانید کلید مدل رو از این
سایت
دریافت کنید تا
12
آگوست بدونه هیچ محدودیتی قابل استفاده هست
⚡️
قابل استفاده در
Vega Agent
☑️
Base url:
https://model.inferx.net/endpoints/v1
Model :
deepseek-v4-flash
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 696 · <a href="https://t.me/ArchiveTell/7352" target="_blank">📅 17:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7351">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFGuvuuFfbTuSAagIMidSKTkClXXqS9gmE9jdNaIcbQ-Apg0aJgA-dX4xlxUQhonUnMBURmKSApHc2y2V13dyNhDqmSVjTNXx6UrIOygga9sHYD8l_bJi0ZZ735L-x03fWMc8Aa0RIVgcTiJAKy6XdNDx3bKa1jKxO1Fxbus2hrdnLIFUcBFse-GGH9Y2cVyaihPQ_2agOxwZG_-EE8Sc7eCYQVaV5aEaS55pYxxfiI3jXO4R2QNOu-V1ugK9al34L4lgYYdeMqKzZ8ASpBITOunXxawC-JHb8b_9m_FjexllReQJNGkYzcD3w73Fkm0ccm3x6YMKOIK04_ffpLchg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان
Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این
لینک
وارد شید و سپس لینک ربات تلگرامی ایی که میده رو استارت بزنید برای وریفای
✅
5
دلار اعتبار برای مدل های پولی
☑️
قابل استفاده در
Vega Agent
☑️
روزانه
5
میلیون توکن رایگان
☑️
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/ArchiveTell/7351" target="_blank">📅 15:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7350">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ArchiveTel
pinned «
بالاخره ایجنت هوش مصنوعی خودمون رو برای اندروید ساختیم!
🤖
📱
بچه‌ها، یه مدت بود داشتیم روی یه ابزار خفن کار می‌کردیم و حالا Vega Agent رو به‌صورت اوپن‌سورس منتشر کردیم! این برنامه یه دستیار هوشمند و همه‌کاره است که با معماری Local-first طراحیش کردیم (یعنی هیچ…
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7350" target="_blank">📅 14:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7349">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWkHLTonDUhXL4i1_vKLzVpWmKFgw-FWO9KTFc7h0vznFu95p4A8v8ejdXlOjpe_VzJFn9jxJhgWVtA42hdbh2vSng3_Ki_IGOEcY35F4um6bQWuhOXwwFRdYe1A6zishfRPz43Ebau-bB_XFLaHM3vGo1O0Oj2WUfwKOagyBAb6rTUa3zhO-Br12jAhvG7ETFrhYgSxfNwmjwGoSfcYqR8N9snaRZnDlvMjOw_WzAL5_cnk8I62bj2b4Zcx3r9fxYwQGdWN2hb_qgfeanp7MK4LsLbcm5oZv-Oy4k_AiHcciJ8smzTHCP9JQYb2tjMUGbrVrjLucol7FLMNjOfClA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 8000 اعتبار برای ساخت تصویر و ویدیو
🚀
دارای تمامی مدل ها
☑️
دیدن آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/ArchiveTell/7349" target="_blank">📅 13:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7348">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚀
50 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان  Sonnet 5 | Mimo v2.5 Pro | Nemotron Uitra 3 | Minimax m3 | Gemini 3.6 flash | Deepseek 4 flash | Sonnet 4.6 | Haiku 4.5   برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این لینک وارد شید
✅
…</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/ArchiveTell/7348" target="_blank">📅 13:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7347">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6wCDBsDdsduBclY1B7AbMrvGNIwXqECqCVm32bbJvPKAZ_dh6acVrcfnqEX7_zHc5o19JAYkzhjnEdQ9IkU_wf3UdSsN7SKT2eFvc5EzfvRZRMWVTW4WEUuA9HOSTDJqsuLZU4ZXWXxZLjtwW6NjkHKpgBJuKRTdgsCH8xeyYECczc90sQ8h_3m0OiN3ho-6O0XWnJ8QbSha7WAVCKWLb3CAYG9eUrBC-kpOC3nP0lWYIvUH_OR_On384KmXBcSwKZt9uR8UhYT7YUsY1R_xSRKQbpDfqzOAMi6UY_S3ewSQhcpAbphWYVhCy4k0XKkqHZi4bTX0HZNAyAHKnd1Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
50 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Sonnet 5 | Mimo v2.5 Pro | Nemotron Uitra 3 | Minimax m3 | Gemini 3.6 flash | Deepseek 4 flash | Sonnet 4.6 | Haiku 4.5
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این
لینک
وارد شید
✅
قابل استفاده در
Vega Agent
☑️
روزانه بین
5
تا
50
دلار اعتبار هدیه
☑️
🎁
با هر رفرال شما
10 دلار
و شخص دریافت کننده
50 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/7347" target="_blank">📅 12:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7346">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4Y7iVCF-bdKtbIYpb5CWD-RH4YG6GoVRGfPblVGqYIEjpPJRQO7FRIb-VgizKONzId3QBpNwQ74oxVTnkSwB79HI1gl5J0jEXykojCKMAHXQejgOIgwN03sBscGF8IEeiEVrAhwSMJmoC5JXD3SFFRrAUIN__0aggM5nVML8twn_okZI5IqoQ0_N2jkQD8ybDjK7RNYRuKu_hETTKd1Io9M-_c-o67dYK_AS07wePddnIMd4mN2xS2Sa9_nZsCo6ZNOlZU7K0bRhV95BkGqw1vwPrtQdL1SoIMZy4WsCvHefxI35SOiBHIX_82AVqt_NvKpgMH33o-ibK0mQq0qZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 1200 اعتبار برای ساخت تصویر و ویدیو
🚀
دارای تمامی مدل ها
☑️
دیدن آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7346" target="_blank">📅 10:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7344">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T8UWIsOLta8OZnQGt4IFZxMwYG_huVzRv5xVqydgm7nAa7771S2g26E1lvb78qn8kKpf81exLkuP4aiYzUgywYahcflaC20AYFEnqR_Qyb3dTDxP2Vi1Sv5sehwgIfzNITgmE8-U5QUT7lpdjirw7PgnDraUEjxBwHPlRWJp4n4M40ycuE8bE35orL0MMjyWAmM47uTNf49mMOKVfveX438bBtNwTr5m2Mxo356SxS_D1CH9KfHLq7jbcpgtsDmCjOVnMNwTjeL-c1-j_YxFob7sWJGo_wYLCpfrvfZUjkPjpWRfGwThIlmwFYU1aEJJPZjJcpYscFfmQERrRFNrdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s8CTLtc0dAHCrZOmt1khnfzYnCVd90_bara6x6YJsTb8Y6zFE2z6oja9fpwj12fMTxf2-6odMx9Js9Lf26VcmHGtE8QBmiREj5HrqIS-XzOMgEMYDc9ozXM30bVuf6-AfDuobHhw5ZI1TyXTWTYABLCYif8SHrGA38L9-Xpsg0ClrNEnATAOCZ2ewDujuXaT7o1vD5VWzqaWFettKw6t7lM8kkkPn8EAMH7j1OWxxHTC7wW32NLjo8DWd-clGnVzRHmEUm_Fo6zrMLsC2eai_FaktubQ3KfOz_0gYzdJnn1qBEiIPXA9sgL04DhjwuLJgnaXIIQTyNjH5nQuO2DWiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7344" target="_blank">📅 23:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7343">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7343" target="_blank">📅 23:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7338">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YfglSlmCltnX3BPMbtZO08qolJSvbEoKN0Gvv3rSzHDkQLhjswB4OSOVeljzcGIRaUXfqUqoLwGSWusrCWpQK2AXF3gnTQHA4ue6kc_7YA7MwSof7ZxaWy-x5UUWJ35fI6J3wk1v7Zx7kWBONW_cinzM-uCGzDYiqu7XR4AFm2E3xdzfOlljc1m0hu0-0P8w1tizC9MnkeHtUCrSy9rg07BrYIBX1GeVJ5Rn9OtCIRvJTn4cbExoXJF6qni5NyN4sKxI1d-g_wMoVaLyd_Zd2XY3T_c4GyvGlrCLji2SKyb0tKjCx9AbHgfoHcscBerQNZabwSLJjUfRH9fi7u97JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A3QaTV5Pm4mENlZ2szH7d0_J62wKvI-aK7Sd4dRqfc0_XMBz97PVEWz5AhKS48Rb7EaCrvG_V11peG21ojOonWgh--LqfNTGo7V9Zk5hkmfhbHmnSGCI_XPHSO8_FqOjXbo0bOFaQolx6SKCPxphhUbLwQ1nDVMh0MrUJ17v0LmaD5EEFSMSIhD8KLAKhsmWiAug1bn6-F3ozyoOcp1LXjR_lZwegkpSzlFgNxCaFG6NdDgu7wHmCKR-dGPaLUag48y0TiWS9prbhGWAapiW_hPPFpmcoDCTC0liPfCpM4pbFHwBZuUWQM1kzRMI6zLqLDMSOsTuDFSShx-z3voOmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FnRJ44556-ACj26tBqo2UJPEP3GLJrHHWNmTsGZXnUnCQDT3VCO2T7Xi4-e_EFp9FTEMcaXSRurjPOGX5L2-fUj4NNdYC7UrT--OFiLkFg4KOs8pMfLxaSoRoU3vZz-GcfoMcE2XGz7-Z8JTHlGBF5TgTpuGtt1t_PY2_c9QEypZvYGYuPwLHlkMsDgqMvJ54oxM9oflB3P9U-3uzdYWTkPQFQNEsz5H6NfofRh4f_LaCAIdBNO6IltDhazz0zyjmuGMxqCJlHjFjmj44kQNU5X6kWWi-5M-vn2xcuZAxviLoT6jNX56ZdVW0vxk7m6CpFlCjdiGAPOpiKrZypf35w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tylnsMmedifMWwCdJsFQCXiXBdgNdHuFb10d0YdeJWQHUMwc1CJ3_EBYlF-3voU2TUr7ilnAOoqVisj0kIRhDnQTKSv2z-m5oS6dFWHq5iT6aRPs39CRWYBSeMwgp5UdgaEdmBzMe6bGBafIcPPHmfCz6s5WjHhLTwLRQlUoHjefTXi91WKAB2YGxSaRH1p5eVjmOFSf0bHN2ymLl3Ycw0aJNiMQ63gpJ-i1xq3lX1KW1CBcE9arp3UBoMETlE3et6Bs9fUjFX0hNi3-leneks_AqLzdFyOGOYobLN7o3KDoeMgefEYzPOaK8Tm64mqMS4gl4AxrLsc6S0KfC6qhtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gdS9oB3EZ6YItqywCJ2xe85-6FNIticw3ocDXczfju3Dbb_19m69_RP93QFgieXrpPKHeDcD6liEUOpr00zDPSk20hYGkxCmihIpbYlMv6IHP0Sn9lsDcSb0PWZ6GhbV1CRt9EWK-A3d2A6djYkjcPqxHfdkyku2OAzIGzAnzjmdx0JscwiIVKyLVCD4i1yK3oI9nUJYeP3Q8fpk4w0pYjA-yoLX8t530AOmvSa5HwK316_REuD7xH5Al1f8gL1o9AIbfjQSEFtHiIhyL_BJIGYlUgVk6N9uvagL5WTiiZN91osImB5N-Q0_t4JBqMnXBWfYc680JVtJ5aNQmMTFvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7338" target="_blank">📅 21:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7337">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-text">بالاخره ایجنت هوش مصنوعی خودمون رو برای اندروید ساختیم!
🤖
📱
بچه‌ها، یه مدت بود داشتیم روی یه ابزار خفن کار می‌کردیم و حالا
Vega Agent
رو به‌صورت اوپن‌سورس منتشر کردیم! این برنامه یه دستیار هوشمند و همه‌کاره است که با معماری Local-first طراحیش کردیم (یعنی هیچ سرور واسطی این وسط نیست) و مستقیماً با کلید API شخصی خودتون (BYOK) کار می‌کنه.
✨
چه کارهایی براتون انجام می‌ده؟
🔹
پشتیبانی از همه مدل‌های معروف:
از OpenAI، Claude و Gemini گرفته تا OpenRouter و حتی سرویس‌های لوکال مثل Ollama.
🔹
مدیریت مستقیم فایل‌ها:
بهش دسترسی بدید تا فایل متنی بسازه، کدها رو ویرایش کنه، PDFها رو بخونه یا فایل‌های زیپ رو استخراج کنه.
🔹
۳ حالت اجرای هوشمند:
برای اینکه کنترل کامل روی تغییرات داشته باشید، می‌تونید روی حالت‌های خودکار (Automatic)، برنامه‌ریزی (Planning) یا تأیید مرحله‌ای (Accepting) تنظیمش کنید.
🔹
مرور و جستجو در وب:
خودش تو اینترنت سرچ می‌کنه و محتوای سایت‌ها رو برای تحقیق و استخراج اطلاعات می‌خونه.
🔹
امنیت بالا:
کلیدهای API رو با الگوریتم AES-256-GCM رمزنگاری کردیم و کاملاً امن روی خود گوشی ذخیره می‌شن.
📥
فایل نصب (APK) و سورس‌کدش رو تو گیت‌هاب قرار دادم. نصب کنید، تستش کنید و اگه خوشتون اومد حتماً با دادن ستاره (
⭐
) به مخزن ازمون حمایت کنید!
📌
لینک دانلود آخرین نسخه از گیت‌هاب
@VegaEnter
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7337" target="_blank">📅 21:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7334">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بالا باشین بچه ها عمو وگاس قاقالیلی اورده</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7334" target="_blank">📅 21:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7333">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بالا باشین بچه ها
عمو وگاس قاقالیلی اورده</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7333" target="_blank">📅 21:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7331">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwPBwhnY1UyiOXh6_i1Cwwe25-drZgiwztJ7nlAk-D7XdMdjt-_tTZXdtmCAkzkrOUU3YDtY80IIuQnMuQAAbSGNWJW2OrziYKSC995gjTiCbt5kAgNz2DhYb-HRrNs6jxWpdDbbHOLp2yFZuUBiz8JKpmIalb_mdKwvfRz_-Vqr8QqBxqf_ka_ZRrnKOfBuUBUvnMpQxHqNT2H1Q5_4dM63deMFCI5mpPZWU_6QPzzgDdGwhGc1l8nQX6X84ZhfoBl1mgvbOz6hBny-mmZkUsdcBEmSxnfGvxsLnEE2bPMH6CmRzVUHBh4X9W98dHSahcj0N039tvnNeh-u1tH97A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت ویدیوهای حرفه‌ای با هوش مصنوعی، اونم رایگان!
🎬
✨
بچه‌ها با وب‌سایت
Dola
می‌تونید روزانه ۴ تا ۶ ویدیو باکیفیت رو با مدل قدرتمند
Seedance 2
تولید کنید. علاوه بر ویدیو، این سایت ابزارهای چت و ساخت عکس هم در اختیارتون می‌ذاره.
🎨
✨
ویژگی‌های کاربردی:
🔹
تولید ویدیوهای حداکثر ۱۰ ثانیه‌ای.
🔹
امکان دریافت خروجی در ابعاد و سایزهای مختلف.
🔹
کیفیت تصویر بسیار بالا به کمک مدل Seedance 2.
🔹
دارای ابزار ساخت عکس‌های خلاقانه و چت‌بات هوشمند.
🔹
سهمیه رایگان تولید ۴ الی ۶ ویدیو در هر روز.
⚠️
نکته مهم:
برای باز کردن و استفاده از این سایت، حتماً باید از VPN با
لوکیشن اروپا
استفاده کنید.
🔗
ورود به سایت Dola
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7331" target="_blank">📅 17:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7330">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYgc1EcWT0JmOProbtBxT6b_rqqVxN2DFxCl6xHLsNbHvTRhCTDt_LqtScvTd9bghZFsMxKq6TqWIx967X1EYgGwE1NJnuR3giadgUVj7ZMXqCbGcAh2dxCNLCrVzu2QHgLb943heBTeqrsErbxSXGJCuzKoa3BPekn325l6MI_39HL3a1fe2yrAjVJkiP96OCQwBO7Onlf4FnLyMEJDkUox-e1C5hFa8iAvJ1rF6yVl3HeBlB600H6FWT9YmSLAIbDXyvwWpkM5KJXqYTvE9TxqVMvTFy8zDW5Raj1giz7LfxIkvpf-CBYc20v7lo09uNUVeY27ch18sNRwpcLaXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Türkiye'deki İnternet Kesintisini Aşmak İçin Güncel Yöntemler
🇹🇷
🛡
Herkese merhaba, Türkiye'de yaşanan son ağ kısıtlamaları ve internet kesintilerini atlatmak için şu an çalışan en etkili yöntemler şunlar:
🔹
IP Spoofing (IP Yanıltma):
Şu anda IP Spoofing yöntemleri filtreleri aşmada sorunsuz çalışıyor. Xray/v2ray yapılandırmalarınızda paket parçalama veya IP yanıltma tekniklerini kullanabilirsiniz.
🔹
DNS Yöntemleri:
Bazı ağlarda özel DNS ayarları veya DNS Tünelleme (DNS Tunneling) yöntemlerinin de erişim sağlamada işe yaradığı görülüyor, mutlaka test edin.
Lütfen bu bilgiyi internete erişimi olmayan veya sorun yaşayan arkadaşlarınızla paylaşın!
✌️
#İnternetKesintisi
#Türkiye
#ErişimEngeli
#VPN
#Turkey
#InternetShutdown
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7330" target="_blank">📅 15:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7329">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ابزار تحت وب «بهینه‌ساز کانفیگ» برای عبور از اختلالات کلادفلر
🛠
🚀
بچه‌ها یادتونه تو پست‌های قبلی آموزش دادیم که چطور با اضافه کردن finalMask و cipherSuites تو اپلیکیشن PattNG مشکل آپلود رو حل کنید؟  حالا برای اینکه نیازی نباشه دونه‌دونه کانفیگ‌ها رو دستی ویرایش…</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7329" target="_blank">📅 14:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7328">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZ1zdGYdA5yX2JfucU7RX8mIt3N6XmtXA7ykB9YdcIOhXeJ5UgWDHsurHjdE9ECll1xub68FWY5XM2VbD5pTMGNWVplwlUDc0Mpd-EpXKSsNKdnDkuwNx_-BR4mYrPNbBgOxQstDCRM8gJCeEmF9fs6SofpGqykG8DxPTlhy18cnu1OR7RM211kc9-gTktQ7JURcHiKXFmlDYKOT-WhWk2c6jfTVbXNHNGKAkqX3iuYL4owW7wJ9r1H5LgWw2I9XTGxNRH_wFdslN9blPv62GfRmQYMdKj-wufshR2UdwHSg4EXNGXe-xRhatrLGML3EL-fTEihGQMNnrzqbPsXpNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی به هوش مصنوعی‌های فوق‌سریع و قدرتمند در یک پلتفرم!
🚀
‏با این سرویس، تمام مدل‌های برتر دنیا رو یکجا در اختیار داشته باش. همین الان شروع کن و از قابلیت‌های هوشمندش لذت ببر.
⚡️
‏
✨
ویژگی‌های کلیدی:
‏
🔹
دسترسی به مدل‌های پیشرفته (‌Opus⁩, ‌GPT⁩, ‌Gemini⁩, ‌Sonnet)⁩
‏
🔹
مجهز به سیستم ‌Agent⁩ برای انجام کارهای پیچیده
‏
🔹
۲۵ درخواست رایگان برای شروع
‏
🔹
۱۵۰۰ کریدیت اختصاصی برای استفاده از سایر امکانات
🔗
https://app.clickup.com/login
‏
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7328" target="_blank">📅 12:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7327">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رفع اختلال آپلود کلادفلر
🚀
۱. نصب اپ PattNG: github.com/patterniha/v2rayNG/releases  ۲. ویرایش کانفیگ (
✏️
)  ۳. فیلد Address: یک عدد آیپی تمیز کلودفلر  ۴. کادر finalMask: {"tcp":[{"type":"fragment","settings":{"packets":"tlshello","lengths":["5","94","1"]…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7327" target="_blank">📅 11:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7324">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nHKTy6ZXCw4g4YlPjmQ0JzG7DcXNUkIjxW4b7EweOjcLAt2QRh60QFdJMg6XDao9R8BRR6IR6b6oDMMNvI-qcmkEuwhTB07gbYg-iln0ePQiq_mgRUjTgpSAs433z1Cj5VPbFMbTlcG-Wow6LXvWajt2ukFgjU6NOC5VPs0CDn_NcuSAB9KVgUTypTC-ZKcsnly1qpnJanDnk_db2wE0S79MPa0pBEWUE01KIdPNJGFy5RhfxXASyIUFsfndrbMYMeTNQxyNoezBFl-LuruGUa1eHHVj71ga1naCsGJhF5Ne8WlUSsH2aF4zjTj9tIsTC_kDGfmGHszDJ4--cZAWtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W5vV4QRaQek5ceTRGp5ngd4IjrhSVSIAe3zIcbiNAzeJbNL2VJg6jYrZqJ8YrEdCyDAbNbQjU_YWEjrBoU2XoBtqflN9boWAW9M4rfSgc2jmzI5zwb0EvogkY46r2gEYlwIc-HHfE0EAQjuZ-qZRiqVXgwJvQ6N9aAPtfnVpBl7CSlxAcIZATjHdCM_qhqHZfTY2FzGxpF_kLQrJWQbvHblcOamWL8EpkTPoCkTnZ68ul3CzsOdEIDzNyhIc0vuUWY0IF88vYJg3lt-9NfHmh95Eq2N-SVrWujFbEqCEbLFBqoQap0mB5wC1qEBZBiK_ig0tu0fzLwuztnEhIxZyVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/emVTbvxKWa_p0nqltXSbnt5NzKzwDHzmGEpsx3HQVqV35hrKK2gDYIk2dxA8-RmGTWyQrlDB856C4JKpYNx3t9AGQ0MBhUqa1lsXBXtTme3snlCchxWfWQNSZjyPeUFkZZUrusWArWMNquCOsCxISfOzMRewCJFx6tlUHJelOlHBDB7bgbTNg5zKlCrSmBx83LAMCYUosZPTBOXBhQ5vFhhqOPs79HClStjMJSCcPfjQWDLSBTUpmNJwPKmVJDrP0BwQT6ND0lzm628ggkASyqhXBz1UusnSA2EWtFiGXWqHHQCG1RvXWxwFqYE2ZeJUqyPtOhJl0bjGAQ_IjY4Law.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفع اختلال آپلود کلادفلر
🚀
۱. نصب اپ PattNG:
github.com/patterniha/v2rayNG/releases
۲. ویرایش کانفیگ (
✏️
)
۳. فیلد
Address
: یک عدد آیپی تمیز کلودفلر
۴. کادر
finalMask
:
{"tcp":[{"type":"fragment","settings":{"packets":"tlshello","lengths":["5","94","1"],"delays":["0"],"maxSplit":"0"}},{"type":"fragment","settings":{"packets":"1-1","lengths":["109","1"],"delays":["1"],"maxSplit":"355"}}]}
۵. فیلد
Fingerprint
:
unsafe
۶. کادر
cipherSuites
:
TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
۷. ذخیره کنید
✔️
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7324" target="_blank">📅 01:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7323">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">PattNG_2.2.6-P2-fdroid_universal.@ArchiveTell.apk</div>
  <div class="tg-doc-extra">68.9 MB</div>
</div>
<a href="https://t.me/ArchiveTell/7323" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دانلود نسخه یونیورسال PattNG (نسخه v2.2.6-P2)
🚀
📱
بچه‌ها فایل APK این نسخه (Universal F-Droid) روی تمام گوشی‌ها و معماری‌ها به‌راحتی نصب می‌شه.
🔹
پست مرتبط در تلگرام:
🔗
مشاهده فایل و جزئیات بیشتر در تلگرام
💡
*دم توسعه‌دهنده‌اش گرم، واقعاً خیلی زحمت کشیده! اگه دستتون بازه، با زدن استار (Star) توی تلگرام یا گیت‌هاب ازش حمایت کنید کارهای خفن‌تر تحویلمون بده
😁
⭐
*
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7323" target="_blank">📅 01:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7321">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آپدیت جدید کانفیگ‌های Serverless منتشر شد (ورژن ۴۶)
🚀
بچه‌ها، کانفیگ‌های بدون‌سرور (Serverless) به نسخه ۴۶ آپدیت شدن و روی نت‌هایی که اخیراً از کار افتاده بودن، دوباره فعال و متصل شدن!
✌️
این آپدیت شامل دو نسخه low_delay (تاخیر کم) و high_delay (تاخیر بالا)…</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7321" target="_blank">📅 01:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7320">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فردا شاید ی سورپرایز یا دو تا سورپرایز بزرگ داشته باشیم
🫠
❤️‍🔥
(البته از ۱۲ گذاشته ساعت)</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7320" target="_blank">📅 00:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7319">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مقایسه سرور ها و خرید سرور مناسب و اقتصادی
جهت راه اندازی کانفیگ
https://t.me/archivetell/5282
https://t.me/archivetell/5308
https://t.me/archivetell/5309
https://t.me/archivetell/5310</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7319" target="_blank">📅 00:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7318">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7iFZGnh3VMRahUewLAbi4Gj0nF35lzUvWwUGefGlEOAr4WPzD-UPVAFFn-G_HixPPKX1N2uLv53gzWkCz31cDNkg3c3CH1RY2XU7A7JN_EpW4j6c8cPXqXtgXxhNKKV07w5osIXgTvOVwAYglqdafTqQBYCJwgy4sZT8LH2K1mxuL7OGTJB8EyaNWa-l9ziq0UgZwWr1FvynJFNuqMOvAIxh6lru-3v6nXnmMgNHs3PIdaQTnHXeoD8-DV1n2AzCgws7nZ-ddPNO9X8TATUgMz-vWxW1wBkwIZeScJku3yGIRcb-LUxvnikoRfOBItnftx0EXmyWrvwZMNrWpAfuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش شدید قیمت API مدل‌های GPT-5.6 شرکت OpenAI
💸
📉
شرکت OpenAI هزینه‌ی استفاده از API مدل‌های سری GPT-5.6 رو به شکل چشم‌گیری کاهش داده؛ اونم به لطف بهینه‌سازی کدهای سرور توسط خود هوش مصنوعی (مدل Sol)!
🤯
✨
خلاصه تغییرات قیمت‌ها:
🔹
مدل Luna (اقتصادی):
۸۰٪ کاهش قیمت! (ورودی: ۰.۲۰ دلار / خروجی: ۱.۲۰ دلار به ازای هر میلیون توکن).
🔹
مدل Terra (متعادل):
۲۰٪ کاهش قیمت! (ورودی: ۲ دلار / خروجی: ۱۲ دلار به ازای هر میلیون توکن).
🔹
مدل Sol (پرچمدار):
قیمت ثابت موند، اما حالت جدید
Fast Mode
بهش اضافه شد (۲.۵ برابر سرعت بیشتر اما با دو برابر هزینه).
🔹
راز این ارزانی:
مدل هوشمند Sol، خودش کدهای هسته‌ی سیستم رو بازنویسی و بهینه کرده که نتیجه‌اش کاهش ۲۰ درصدی هزینه‌های سرور و افزایش ۱۵ درصدی سرعت تولید توکن بوده!
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7318" target="_blank">📅 21:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7317">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcO5BDw-WldX2RNSlPu6SjLklb-UNPaegvm0A7BUeO5Zn8z6m6WNAXT7bIO_fadMGIqpeTPVi1ggBkLZxnIqaj22QzitUsfnLFnwy8B9D1sETtjdtNa0uqC2x4_zLnRG2xXWJlVZg2A2CQEupetzep_qBOACath_uSWHXS97QYjNrkNP_N9A_7-HwZX03ODJcQOsXIp282nYuzQ9Zr9e6IvX6c3sjJUAcI0UbCxN_aBQjBvdVjZX814_jnmKywHRY4NDLrGeQU69jlmwPRRUIWbqfa8aIoDLOrpl0Aj5DdMN5kAGlU_lEChzPJ44x4THrqQ92PIWtF7DSjBJBHqkFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت ۱ ساله Pro سایت
Beautiful.ai
(رایگان)
🚀
🎨
بچه‌ها این سایت یه ابزار عالی بر پایه هوش مصنوعی برای ساخت اسلاید و ارائه‌های حرفه‌ایه؛ فقط کافیه موضوع رو بهش بدید تا خودش کارها رو انجام بده!
✨
نحوه دریافت اشتراک آموزشی (EDU):
🔹
مرحله اول:
با فیلترشکن وارد
صفحه
بشید و روی
Claim EDU Offer
کلیک کنید.
🔹
ایمیل دانشجویی:
ثبت‌نام رو با یک ایمیل
.edu
انجام بدید (می‌تونید از سایت‌های ایمیل موقت مثل
tempmail.id.vn
کمک بگیرید).
🔹
اطلاعات دانشگاه:
برای اسم و لینک سایت دانشگاه، از یه هوش مصنوعی بخواید اطلاعات فیک و رندوم بهتون بده (سایت گیر نمی‌ده و قبول می‌کنه).
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7317" target="_blank">📅 20:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7316">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jewCFM9QeKIMH5l5ZTESd2intQU7r23yF5MROb983XyH8kMTZxwlXoMrHp26YCPepnguNVwFw42SIxRQG3t6aOOwBK_o1JeMxRCiNnYbVitYMN9LATfzvlWtk9-CLL9N8OLcMltahY9XUt6tb0imN93pM0dHrH3SJbFCWDAgaKEiyiRjI4Vwsqgai4F6YA-ZJbl11d2uMW31dHDHABsj9vNZuwMXV7hXr24iDYcxvxJHrQYG6A8lEWvlpii2B1OgCa1dPZaDiD0o20E1AdoV4eLGgaZY_Vbc3DXlmHhhcEINfKKB-W-vZsGG-x12pb8ivLiYN0YbihdfTviHBilYCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی ابزار PDFx؛ ادغام و تفکیک هوشمند فایل‌های PDF
📄
✨
پروژه متن‌باز PDFx یه راهکار خلاقانه برای مدیریت اسناده: ترکیب چندین فایل در یک فایل، اما با حفظ قابلیت جداسازی!
✨
خلاصه ویژگی‌ها:
🔹
ادغام و تفکیک:
چند PDF و عکس رو یکپارچه می‌کنه. این فایل تو برنامه‌های عادی پشت‌سرهم نمایش داده می‌شه، اما تو برنامه PDFx دوباره به اسناد مجزا تفکیک می‌شه!
🔹
کاربری آسان:
مدیریت فایل‌ها فقط با کشیدن و رها کردن (Drag & Drop).
🔹
دسترسی:
دارای نسخه وب و دسکتاپ (ویندوز، مک، لینوکس).
🔹
دستیار هوش مصنوعی:
پشتیبانی از مدل‌های OpenAI، Anthropic و گوگل (با API Key کاربر).
📌
[
لینک مخزن پروژه در گیت‌هاب
]
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7316" target="_blank">📅 18:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7315">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یه پروژه جدید ساختم برای 3xui دارا که خیلی بکار میاد
دیگه لازم نیس آیپی های تمیز رو دستی اضافه کنین پنل
یه ربات تلگرام هس که به پنلتون وصل میشه، بهش چن تا کانال آیپی تمیز میدین، خودش خودکار آیپی های تمیز رو از چنلا برمی‌داره اضافه میکنه به ساب پنل برای تمام یوزرا بالا بیاد.
سورسشو شب میزارم.
تمام.
🔵
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7315" target="_blank">📅 14:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7312">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZLI3j-VBZZsUOhlkYf_43JiKTXjUB4HrcP4EThj865FEJIyeMQVw0uFNehU9A-RJWvMNuv_l1DKdwQSUYx15dqql4-elE1d6caktzzQAxMA9RovHrw6Vfeqi4QCLBLsPCuAbnpZPwV-jXWziZUeMaZ-Ht3O2Z7CcY4scrnoQjtvmC9wIwjXK7v2TMkP_lkJb-K4TMAbc7cjyq1kSH-2QyjhK2fyVvYBQpfLqQ_l3seGKiLCCVmNjbnv0TU1lNv2WQvDPgtvy-2z_yTyAe1XvA2R2MpW3e5GU5qnMRJ9bIK2X3B6y-wqIkz42XguPHHnSeHUOaaRc7mrW2NvKm30oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید پنل 3x-ui (نسخه v3.6.0) منتشر شد!
🚀
🔥
نسخه جدید با تمرکز روی امنیت، پایداری و رابط کاربری بهتر منتشر شد.
✨
خلاصه‌ی مهم‌ترین تغییرات:
🔹
ارتقای هسته (xray-core v26.7.28):
(نکته مهم)
ساختار
finalmask
تغییر کرده؛ اگر قبلاً از این قابلیت استفاده می‌کردید باید پروفایل‌ها رو از نو بسازید.
🔹
امنیت بالاتر:
بسته شدن دسترسی آزاد به فایل
openapi.json
، امن‌تر شدن توکنِ نودها و مسدود شدن دیفالتِ آی‌پی‌های لوکال.
🔹
لینک‌های سابسکریپشن:
تشخیص خودکار نوع کلاینت (User-Agent) و قابلیت جذاب چک کردن وضعیت آنلاینِ کاربر مستقیم از لینک ساب (با اضافه کردن
format=info?
).
🔹
داشبورد مدرن‌تر:
بازطراحی کامل صفحه اول پنل با گراف‌های تمیزتر برای مشاهده زنده مصرف سرور و کانکشن‌ها.
🔹
پایداری دیتابیس:
اضافه شدن قابلیت بکاپ‌گیری زنده از دیتابیس (بدون نیاز به خاموش کردن پنل) و رفع باگ‌های ترافیک.
📌
نصب و آپدیت با همون کامند همیشگیه، اما
حتماً قبلش از دیتابیس بکاپ بگیرید!
#3x_ui
#ثنایی
#پنل
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7312" target="_blank">📅 12:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7311">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1-nUTRpKrWBvIp2g857kCDYlsSfmpeADO5krCHH1XVBgwMH-etpzrHP8fUDQO0oyE5qY8sPbvCn5Va4w1USddybDd5C6sksOmZ64eelvikGdmwlVjGB__vzkHn_Af-MqyrX2sAB7AOPQ7hLS3-0jznfh42pP9hRL_uBZLremab9KHGSbV5frUinNm8bmCU5NEvgHJN2cSE5xUlMylqKg6sVk9yInMeeI_bpUwkcE0Vt9IFAFgr7TL4rzsVh7nRfnTwRH6vvOqF15Q0d862NDMLO76fR4Yk0TxUOtUQVnL9TDMJ2iYga7c5NGb9DyyeCupP8faYf19xift_UlhWjjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشتراک ۱ ساله ChatGPT Pro رایگان برای دانشگاهیان
🎓
🎁
بچه‌ها می‌دونم این طرح به خاطر تحریم‌ها و نیاز به کردیت‌کارت و مقطع‌تحصیلی بالا به درد خیلیامون نمی‌خوره، اما اگه دوست یا استادی خارج از کشور دارید حتماً براش بفرستید تا استفاده کنه!
🔹
مخاطب:
اساتید هیئت علمی و محققان پسادکترا (Postdoc).
🔹
شرط اصلی:
داشتن حداقل یک مقاله در ۳ سال اخیر (در سایت‌هایی مثل arXiv).
🔹
تایید هویت:
نیاز به ایمیل آکادمیک (بدون VPN) + کردیت‌کارت (بدون کسر هزینه).
🔹
مزایا:
یک سال اکانت Pro با حفظ حریم خصوصی + ۴ دعوت‌نامه رایگان برای همکاران همون دانشگاه.
📌
لینک ثبت‌نام در سایت OpenAI
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7311" target="_blank">📅 10:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7310">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbZuCtqCkq6sXcwlAccSejLJIvXbcfeK_wLk5pDaGmpqgp-fJNjQzhJsFRfqGlclTYxpoN72fAqUJVXdm8ftDg-Xv8tVLog15V5iXHOYO3GZNg0T_Xhg99ciUEHuBQAPvZKZFCw4tkJuyU1qqk671FJXu2YpABJ63QW9oB5zoEttxIbJITqR8rdaTBsDWQEM0FtbFndEkp2Vjmh1YXBc_hS1YW7XNbK8A8S643Var2tgt12riQEJOXt3d8GEPzvx98C5fuOnFOObtrdsKocVpulwDi91RgeXdgvK816UXQUPGh38iRLAkbbFWjhiU0ME9PmTtxugY6Ni_oyEI5MaVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از Grok Voice Think Fast 2.0؛ شاهکار صوتی جدید ایلان ماسک
🎙
🚀
شرکت هوش مصنوعی ایلان ماسک (SpaceXAI) به تازگی از جدیدترین و هوشمندترین مدل صوتی خودش پرده‌برداری کرد. این مدل مستقیماً برای پردازش سریع «صوت به صوت» (Speech-to-Speech) طراحی شده است!
✨
نکات کلیدی:
🔹
قدرتمندترین نسخه: به گفته سازندگان، این هوشمندترین و قوی‌ترین مدل صوتی است که تا حالا توسط این شرکت توسعه داده شده.
🔹
پردازش مستقیم (Speech-to-Speech): ارتباط صوتی کاملاً بی‌درنگ، که باعث درک بهتر لحن انسان و کاهش شدید تأخیر در پاسخگویی می‌شه.
🔹
رقیب تازه‌نفس: کاربران به شدت منتظر مقایسه‌ی عملکرد و سرعت این مدل با نسخه جدید gpt-live از شرکت OpenAI هستند.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7310" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7309">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تغییر ظاهر لینک سابسکریپشن 3x-ui (پنل ثنایی)
🎨
✨
پروژه
MiTemplateSub-XUI
یه کالکشن عالی از قالب‌های مدرن برای صفحه اشتراک کاربرهاست:
🔹
تنوع بالا:
بیش از ۳۰ تم مختلف (سایبرپانک، مینیمال، شیشه‌ای و...).
🔹
پشتیبانی از فارسی:
کاملاً راست‌چین (RTL) همراه با دارک/لایت مود.
🔹
جذاب و پویا:
نمایش انیمیشنی مصرف ترافیک و چیپ‌های پروتکل.
🔹
مدیریت راحت:
تغییر و نصب سریع تم‌ها فقط با یک دستور (از طریق اسکریپت اختصاصی).
📌
[
لینک پروژه در گیت‌هاب
]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7309" target="_blank">📅 23:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7308">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tyerw15m0YDEi7QOELTITIIlRGRczDsNmb4S6BDfofmrObDF998-qBFkNjEAyPGHwmhc-G3An6HDixxEVGxDUSF5EroawG_VUlEz1QJr4yhJZIoppmMU3ExKaEobSpnXqepnK_p08Spbb2asb_48Ra9FrtoCR8YOx8JPpVwrRIiuyb-FU7TH7QnOzR771WBJf4XVSk8w3NTio-u-JatdtrxPY_j5eglwByDGFbU6L0siIrlxZBItiR1hiCRIvVf506x0YKdcguH9bvlNkMOvkRpc5IQmNZ7sL47yv27M_8wMP1JAKE3xf9AnxHNhL6Hvn-734_xhlQUR84MqME854A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ابزار ‌Onlook⁩: انقلابی در طراحی و کدنویسی!
🤯
‏اگر طراح یا توسعه‌دهنده هستید، ‌Onlook⁩ دقیقاً همان چیزی است که به آن نیاز دارید. این ابزار مثل یک دستیار هوشمند، فاصله بین «طرح» و «کد» را از بین می‌برد.
🛠️
‌‏
✨
قابلیت‌های مهم:
‏
🔹
ساخت خودکار:
تولید پروتوتایپ‌های حرفه‌ای همراه با کد تمیز.
‏
🔹
تعامل دوطرفه:
امکان اکسپورت به ادیتورهای کد یا محیط ‌Figma⁩.
‏
🔹
سرعت بالا:
صرفه‌جویی چشمگیر در زمانِ طراحی و فرآیندِ درکِ کد.
‏
🔹
رایگان:
دسترسی به تمام قابلیت‌ها بدون هزینه.
📌
[
لینک پروژه در گیت‌هاب
]
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7308" target="_blank">📅 22:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7307">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPGEPxIXQgQUiOnxprn-Ge3eSHKvKc67sNwMvX01YdW9EiziHGMOPXEYskQcsTmEYnXvLOmd9T3YMv48srN53DNJMABk5t_oy6VgmiRiYnUHD4JXhNkmaq38OEGDFyx269uKrmrbqKHqv-P-W6V4Kkge8dWpgYPVqctqU3EOyelZzSrISOGYiESVxoL0QrTeydEj5SCFahT5E1RFaFf65HHfZ2jBDcuzxEqgONh-r51vF63PbbnUZz74enwJm2HAaj6IAXzpmAevn6Zz7FCoTEOWXNvqwmmYuQC2VSYLPK983Sli08PlzRrl-M76WBcedXiuTHm23itEhg2cqETcUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
گنجینه‌ای از هوش مصنوعی در دستان شما!
🚀
‏اگر به دنبال پروژه‌های آماده و کاربردی هوش مصنوعی هستید، این لیستِ طلایی شامل بیش از ۵۰۰ پروژه متن‌باز در گیت‌هاب، دقیقاً همان چیزی است که نیاز دارید. از چت‌بات‌های تخصصی تا ابزارهای پیشرفته‌ی ترید خودکار؛ همه چیز در دسترس شماست.
✨
‏ویژگی‌های این مجموعه:
‏
🔹
دسترسی کامل به سورس‌کد تمامی پروژه‌ها
‏
🔹
تنوع بی‌نظیر در حوزه‌های مختلف (از بیزنس تا مالی)
‏
🔹
مناسب برای یادگیری، توسعه و شخصی‌سازی
‏
🔹
پروژه‌های تست‌شده و آماده‌ی اجرا
🔗
‏
همین حالا از این مخزنِ ارزشمند استفاده کنید و سطح پروژه‌های خود را ارتقا دهید
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7307" target="_blank">📅 20:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7306">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDQK1PaZYA913TNwgghltLnAH1QB2QFtsiQoDN1lXIQs5r0de-hNI0YUyiKv2nDJzWAVqnse8QBSaNno7vVVfLzskXSQHfhRlGVXdnjVc61KwrAepo-qeRmY2qK5l85rm5vm5sLidJ-kmyvUlg2QfaN_X2RJsUvyeGU5jM_el8D12OmXBv_EWOln1PKLUtorvmJOkTAad3uthD6k6VumtoVGOFqUk6uS-X6CNx-ttZJHFas10tIcuJNDBiqcXGhxvO_FmBslHO49mAN_nKHIOrhT8aCaK1_IKAF4-jg64gG2k7XzYfzyCKKogLStLMz4_-d4ZWXP8up1kJYcagLdZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت تلگرام پس از صدور حکم بازداشت بین المللی روسیه علیه پاول دوروف
😁
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7306" target="_blank">📅 20:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7305">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCNflluyhErlLEURZw__CAct33xIYxr751795wCs-hAAqiSzcnXl55_ot6SsdB3UNFUqa_ZNSVyqDzXllE21LpCpRkuEd9GMh8hoMXEXj2ZPBaqOVsVp21A61kIM1oS2bjkAJecF4aMDotL0cZRLtCID9bEkbWhFPxLL0osmLmH-iWHT5Fw3qAFOfbL5oldxe5r1qhWUP02x8LJeIJCcRorefAgB3sSFQb_RTCzgSS4ymilJZ2Uzci4U2ZefrF7qVjo1TfybYDh3_noyY8g7XxS0DTTcbGnKm1eq14rYjWPcDtW19b0gIa3jK3zZwwjim2jSvozV_d_EApQqPMICaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
😂
https://t.me/ArchiveTell/7300</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7305" target="_blank">📅 18:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7304">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6kRkjRmTm6DcMGMXNFrBiWOV3Kf3yQcgnyX_2nCY0Iucce6-jDcqX8qrCcrZLZWf-CThduf5vJBWCwfRN0dRbhFz_Vu_qsoVVgShamQHUYtbTW8XNTe3KSqj_9Fij6nYwFO4SCz8qg1c4a2N17hvxbyq1qjAaYHvkZDH041sLxnmKckRxD_qOt49QCDEEeq38ECBJZhvKxxvNw0uG-AEq1l80V-o7YxR4xhqkX1Pq4GogBlaNSpU8P0I9aRqjCuuPY2jq36Yaie7So8AEftBk9ce2SfZjyejQg3f8Nh1IUEojw1_VdI0nAIFVqFKRCoifP2MZa0-JPK9ElwXim1Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏‌APK Converter⁩؛ پلی میانِ وب و اندروید!
📱
🌐
‏این ابزارِ آنلاین، پروژه‌های وب، فایل‌های ‌HTML⁩ یا بسته‌های ‌ZIP⁩ شما را مستقیماً به فایل‌های نصبی ‌APK⁩ یا ‌AAB⁩ تبدیل می‌کند.
🛠️
‏
✅
ویژگی‌های کلیدی:
‏
⚙️
تنظیماتِ اختصاصیِ اپلیکیشن و آیکون
‏
🔑
مدیریتِ حرفه‌ایِ امضای دیجیتال (‌Signing)⁩
‏
📋
نظارت بر لاگ‌های ساخت و مدیریتِ تسک‌ها
🔗
https://gentsergame.com
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7304" target="_blank">📅 18:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7303">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dc52KgKi-eEeCwBeLO_ReMsCk5q6rPAy6ZJXfWp3_EG4aVXq107JJAeP-o7hTh12G64uIj-NKINawIT2KwxYZ8IeZUQU-o98Ma50bmCs2Zbc7C3lofhrYHEaS8e0VLU8doy77zBIdnNSLpOBU1QBybvBnUyWKI3xbGvk8wd2VLZpbV0OqVYzzSUEnDAmLLzaLWhhRGt2IN6_ZnlYt4Qi_q4JBDffdp1n0hzWNx73hicoX0EVXExQV83U9SAObRdDt-tMiMFAtlbGRLig-uZ5gs2XDLwz5CpB4DbKcS1rzYU7fTqXD4Dk0dcNHwpXQEEk7I2lJa_sS-ZksGpOgJcIwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
انقلاب در کدنویسی با ‌JCode⁩: سریع‌تر، هوشمندتر و قدرتمندتر از همیشه!
💻
‏اگر فکر می‌کردید ‌Claude Code⁩ سریع است، ‌JCode⁩ با سرعتی ۲۴۵ برابر بیشتر، استانداردهای جدیدی را تعریف کرده است. این ابزار نه فقط یک دستیار، بلکه یک «تیمِ کامل» در سیستم شماست!
🐝
✨
‏ویژگی‌های کلیدی ‌JCode⁩:
‏
🔹
سرعتِ خیره‌کننده: ۲۴۵ برابر سریع‌تر از رقبا با بهینه‌سازی فوق‌العاده.
‏
🔹
مصرفِ ناچیز: هر سشن تنها ۲۸ مگابایت از رم شما را اشغال می‌کند.
‏
🔹
معماریِ کندویی: ایجنت‌ها با هم همکاری می‌کنند، وظایف را تقسیم کرده و کد یکدیگر را بازبینی می‌کنند.
‏
🔹
حافظهٔ هوشمند: با حافظه سراسری، هیچ خط کدی در سشن‌های مختلف فراموش نمی‌شود.
‏
🔹
سازگاریِ کامل: پشتیبانی از تمامی ‌API⁩های بزرگ (‌OpenAI⁩, ‌Claude⁩, ‌Gemini⁩, ‌GitHub⁩ و...) و مدل‌های محلی (‌Ollama)⁩.
‏
🔹
خود-اصلاح‌گر: قابلیتِ عیب‌یابی، بازنویسی و رساندنِ کد به کمال.
‏
🔹
تجسمِ پروژه: تولیدِ نمودارهای درختی برای درکِ عمیقِ ساختارِ پروژه.
‏
🔹
مهاجرتِ آسان: امکانِ وارد کردنِ سشن‌ها از ‌Cursor⁩، ‌Claude Code⁩ و غیره.
‏
🔗
دسترسی به ابزار
‏
📂
مشاهده سورس‌کد
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7303" target="_blank">📅 16:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7302">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZ3S8RFPeIi_RNHzwTJZhm4iEmXEj-T9Wtj7yxE6Smp1B46hlyprYOUoitCU58vsmfQWQOUfqm64pBOeCf7IilClc6LA5f7qVpt3jcs1GCV2WMzNuYf_in2pedDLUXxkJ1h13_jbsNebm-ZY8rE4JUf2IQqQi4qMsl3V1UogAeTG1rWQpo-x8EMZN5wulZrLLVpEMo9bVKYJGQis2XVTrEgjNGRyb4MUMwONfVG_JFc6yyydgRrC3ayl7UEdNcMS9Y7dYtQE0oZbpAoJEx00rd6WijmAZ6cR0Wek-MJ2o5Wo9uxWdeihZ1rcqUGB1UWBmHI-4EvbSB4JNo9p94OX4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
70 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Opus 5 | Opus 4.8 | Sonnet 5
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدیمی لازم نیست )
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
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7302" target="_blank">📅 12:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7300">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kf1C0f10TkyAdFNoRKhNhvl14Mwt_EZ3k8r7_Ng6eYSpNkLSbSoMKlkwPwd0_7KFZTIAWXZDct8hD_8rP80_LPZDjWVdYDxrgRBxMbpZ7XKMKEL7fnrMptmzdaTXhLTttQEfaKKq0MVpXmg8YAcsyM7XLZ0r2u4RxeEL74AJrc2Ym8jXtUUCvcgLL4Jl8pkgBysOjz8DlQsa3XQzWi7_dTuLOPXSy6HP7sL5jJ2G9dG185taPaW09Re4JSQgcdaweD4aR5E6LsyU_oN8fGNEUPrD46LQpBXUileWYqGq34Ng9DrhP_xaG9Z8hawe5Ri7M5C5lgXVxbKGTCdn2sYOvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتهام جدید و عجیب علیه پاول دورف؛ حبس ابد به خاطر ربات دوست‌یابی!
⚖️
🚨
یه خبر عجیب تو رسانه‌ها و کانال‌های روسی داره دست‌به‌دست می‌شه! ادعا شده کمیته تحقیقات روسیه (СК) پاول دورف رو به خاطر عدم حذف ربات معروف «Daivinik / Leo» (یک ربات دوست‌یابی تلگرامی با بیش از ۱۳ میلیون کاربر) متهم کرده و شایعه شده ممکنه سر همین ماجرا با مجازات سنگین یا حتی حبس ابد روبه‌رو بشه!
🤯
✨
ماجرا از چه قراره؟
طبق ادعای بازپرس‌های روس، سرویس‌های اطلاعاتی اوکراین با ساختن اکانت‌ها و پروفایل‌های فیکِ دخترانه تو این ربات، در حال فریب دادن و جذب نوجوانان و جوانان برای انجام فعالیت‌های تروریستی و خرابکارانه هستن.
اتهام اصلی دورف اینه که چرا با وجود این مسائل و هشدارها، این ربات رو از روی سرورهای تلگرام مسدود و حذف نکرده است.
با این وضعیت و اتهامات امنیتی به این سنگینی، به نظر می‌رسه فشارها روی تلگرام دوباره بالا گرفته و فعلاً نباید منتظر کوتاه اومدن دولت‌ها در برابر پاول دورف باشیم.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7300" target="_blank">📅 10:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7299">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Dockerfile</div>
  <div class="tg-doc-extra">35 B</div>
</div>
<a href="https://t.me/ArchiveTell/7299" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
آموزش ساخت پنل ثنایی بدون خرید سرور (کاملا رایگان!)  با این آموزش می‌تونید بدون نیاز به خرید سرور (VPS) و دامنه‌ی شخصی، فیلترشکن فوق‌العاده سریع و اختصاصی خودتون رو بالا بیارید.
📂
پیشنیاز: فایل Dockerfile ضمیمه‌شده به همین پست رو دانلود کنید.
🔹
مرحله ۱:…</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7299" target="_blank">📅 10:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7298">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">📌
آموزش ساخت پنل ثنایی بدون خرید سرور (کاملا رایگان!
)
با این آموزش می‌تونید بدون نیاز به خرید سرور (VPS) و دامنه‌ی شخصی، فیلترشکن فوق‌العاده سریع و اختصاصی خودتون رو بالا بیارید.
📂
پیشنیاز:
فایل
Dockerfile
ضمیمه‌شده به همین پست رو دانلود کنید.
🔹
مرحله ۱: آپلود فایل تو گیت‌هاب
۱. وارد سایت
GitHub
بشید و یک مخزن (Repository) جدید بسازید.
۲. اسم مخزن رو
railway-3xui
بذارید و تیک
Add a README file
رو حتماً بزنید و دکمه
Create repository
رو بزنید.
۳. تو صفحه مخزن، دکمه
Add file
➔
Upload files
رو بزنید.
۴. فایل
Dockerfile
(همین فایلی که پست کردم) رو بکشید و آپلود کنید و در نهایت دکمه
Commit changes
رو بزنید.
🔹
مرحله ۲: نصب روی Railway
۱. وارد
Railway.app
بشید (با اکانت گیت‌هاب لاگین کنید).
۲. روی
New Project
➔
Deploy from GitHub repo
کلیک کنید و مخزن
railway-3xui
رو انتخاب کنید.
🔹
مرحله ۳: حفظ اطلاعات پنل (Volume)
(اگه این مرحله رو نرید، با ری‌استارت سرور، اطلاعات اکانت‌ها پاک میشه)
۱. تو صفحه اصلی پروژه تو ریلوی، دکمه‌های
Ctrl + K
(تو گوشی روی آیکون همبرگر) رو بزنید.
۲. عبارت
Create Volume
رو سرچ و انتخاب کنید و به سرویس متصلش کنید.
۳. در کادر
Mount Path
دقیقاً این عبارت رو وارد کنید:
/etc/x-ui/
🔹
مرحله ۴: تنظیم پورت و شبکه
الف) آدرس ورود به پنل:
۱. روی سرویستون کلیک کنید ➔ برید تب
Variables
➔ دکمه
New Variable
رو بزنید.
۲. کادر بالا
PORT
و کادر پایین
2053
رو بنویسید و Add کنید.
۳. برید تب
Settings
➔ بخش
Public Networking
➔ روی
Generate Domain
بزنید. (این آدرس پنل شماست).
ب) مسیر ترافیک فیلترشکن:
۱. تو همون تب
Settings
بیاید پایین‌تر به بخش
TCP Proxies
.
۲. روی
Add TCP Proxy
بزنید و پورت
8080
رو بدید.
۳. یک آدرس TCP (مثل archivetell
.proxy.rlwy.net
) و یک پورت ۵ رقمی (مثل
14841
) بهتون میده؛
یادداشتشون کنید.
🔹
مرحله ۵: ساخت کانفیگ تو پنل 3x-ui
۱. لینک آدرس پنل (مرحله ۴ الف) رو تو مرورگر باز کنید.
۲. با نام‌کاربری
admin
و رمز
admin
وارد بشید.
(بعداً از Panel Settings رمزش رو عوض کنید)
.
۳. برید بخش
Inbounds
➔ دکمه
Add Inbound
رو بزنید و این مقادیر رو ست کنید:
@ArchiveTell
Protocol:
vless
|
Port:
8080
Network:
xhttp
|
Path:
/assets
|
xPaddingBytes:
5-70
Security:
reality
|
Target :
www.samsung.com:443
|
SNI:
www.samsung.com
دکمه
Get New Keys
رو بزنید تا کلیدها ساخته بشن و در نهایت
Add
کنید.
🔹
مرحله ۶: اصلاح و آماده‌سازی لینک نهایی
۱. تو پنل روی
QR Code
کانفیگ کلیک کرده و لینک
vless://
رو کپی کنید.
۲. لینک رو تو نوت‌پد گوشی یا سیستم کپی کنید و این دو قسمت رو جایگزین کنید:
آدرس بعد از
@
➔ آدرس TCP ریلوی (مثلاًarchivetell
.proxy.rlwy.net
)
پورت
:8080
➔ پورت ۵ رقمی ریلوی (مثلاً
:14841
)
تمومه! لینک اصلاح‌شده رو تو نرم‌افزارهای V2Ray بزارین و متصل بشید.
🚀
‎
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7298" target="_blank">📅 10:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7297">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">آپدیت جدید کانفیگ‌های Serverless منتشر شد (ورژن ۴۶)
🚀
بچه‌ها، کانفیگ‌های بدون‌سرور (Serverless) به نسخه ۴۶ آپدیت شدن و روی نت‌هایی که اخیراً از کار افتاده بودن، دوباره فعال و متصل شدن!
✌️
این آپدیت شامل دو نسخه low_delay (تاخیر کم) و high_delay (تاخیر بالا)…</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7297" target="_blank">📅 00:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7296">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9SkoA-6Fu1LJ-bo3WKMf1b_UwftPWVcBTpciGj22W-mnLzDc2Q7wotaFkGA6M8V7o3KWOTMYIDrWEn0yktxxUe0JTTt8l94om8bu5HpyaP3RU6nGGQZPOVZaTwrVWv_oAq75Fc3KyZXyQoG1ZG8qpbeoVXfG0jxl-IyFe5DyiRanvMKl84yPHmIQgvJV_udWpyc2HNrNUCvoFwsl2UFdSrZe6UAkoVcpQtLnoE5sQjFK5L_GVGr2xZDpa2AFbfTI36UAQ9sOb7_R4L-ka4bKNY5LOBfNbnDD0I-c2qEv-Eebbi40i4aaf1tINo_Y3WhLXzXhjyXe6Pm5rd_jMCNlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
تبدیل گوشی Android به وب‌کم با VCamdroid
‏
‏با
VCamdroid
می‌توانید دوربین گوشی Android را از طریق USB یا Wi-Fi به وب‌کم مجازی Windows تبدیل کنید؛ مناسب تماس تصویری، استریم و استفاده‌ی دوباره از گوشی‌های قدیمی.
🚀
‏
‏
✨
قابلیت‌های مهم:
‌‏
🔹
اتصال خودکار از طریق USB و ADB
‏
🔹
اتصال بی‌سیم با Wi-Fi و اسکن QR Code
‏
🔹
سازگار با Zoom، OBS، Discord و Teams
‏
🔹
اتصال هم‌زمان چند گوشی و جابه‌جایی سریع بین دوربین‌ها
‏
🔹
کنترل دوربین جلو و عقب، وضوح تصویر، فلش و تنظیمات رنگ
‏
🔹
پشتیبانی از Windows 10/11 و Android 7.0 به بالا
‏
‏
⚠️
نکته‌ی مهم:
‏
‏برای اتصال USB باید
USB Debugging
فعال باشد. عملکرد برنامه نیز ممکن است بسته به مدل گوشی، کابل و سخت‌افزار دستگاه متفاوت باشد.
‏
‏
📌
دانلود و مشاهده در گیت‌هاب رسمی پروژه
‏
‎
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7296" target="_blank">📅 00:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7295">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8RzQ7wpht3icgVa50IP5AKWw1rGUvLhoM8A4sRMP27o9IcGNXxto8QPMC7a081aEzl4mIJ-zJbcI1R_tl-EVNvLOi2tp51ElJB4_9Pf5XkToOAOZ2OWeQ4VLMtisDFUuZS13KqQcSU2Vb3rnC4pAwECUFYT2ZffboHKyZhtgULiZSkogdzBbQkYI1kSEBS40-y615Cma_MkIKO9xOOskDPs2pDb6JZpxmvkAFpcDqnBFR4HaCwxM-0Q-V7ohvO5Yotoo4lDCFCSsydkCpkBL4lgb6D9eRsMkAtbn_q8VOFDil2cHXGM-kozfNiq05dXaVXGcZAc28US0YkPpZrU_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎬
Shotcut؛ ویرایشگر رایگان و متن‌باز ویدئو برای کامپیوتر
‏
‏
Shotcut
یک نرم‌افزار حرفه‌ای و کاملاً رایگان برای تدوین ویدئو است که روی Windows، macOS و Linux اجرا می‌شود و از طیف گسترده‌ای از فرمت‌ها پشتیبانی می‌کند. نسخه‌ی جدید
26.6
نیز با تمرکز بر قابلیت‌های HDR منتشر شده است.
🚀
‏
‏
✨
قابلیت‌های مهم:
‏
‏
🔹
پشتیبانی از ویدئوهای 4K و 8K، HDR10 و HLG
‏
🔹
ویرایش مستقیم فایل‌ها بدون نیاز به Import یا تبدیل اولیه
‏
🔹
تایم‌لاین چندلایه با پشتیبانی از رزولوشن و نرخ فریم متفاوت
‏
🔹
ضبط صفحه‌نمایش، وب‌کم، میکروفون و استریم‌های شبکه
‏
🔹
ابزارهای اصلاح رنگ، Chroma Key، Motion Tracking و Stabilization
‏
🔹
پشتیبانی از زیرنویس، تبدیل گفتار به متن و Text-to-Speech
‏
🔹
قابلیت Proxy Editing برای تدوین روان‌تر روی سیستم‌های ضعیف
‏
🔹
نسخه‌ی Portable و بدون نیاز به نصب
‏
‏
⚡️
نکته‌ی مهم:
‏
‏Shotcut بدون تبلیغات، اشتراک ماهانه یا محدودیت خروجی ارائه می‌شود و به لطف FFmpeg از صدها فرمت صوتی و تصویری پشتیبانی می‌کند.
‏
‏
📌
دانلود از وب‌سایت رسمی Shotcut
‏
‎
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7295" target="_blank">📅 22:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7294">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBRsY_AN2mF-w-O3k8Cr0w1OshDLorHNXqmhb_s3L0DtBDTCy6EmpXsXsCs8vlWz7gnXGwHmCiYCx3nqV1vKbypSvMP5HTbLHUlLTwb_NhxTS7CXdGHlCa-CLOb6-PHqAZToSdEXge4nEh8ziAc0NGF1hQ_CkKEQyD7qpmRmnkJxJbZwRqcg9WTC_T2W4kbHqifPCBC3R1Xl9w2FrGD1_yzWuMc2ihsP0t7CHH6oTqEHx1-qE94k0V6KYuZJ3OtCNljuklAH5DWNWUEWMgxGppDuLtCBGwW_OVO2yeLzTjSL-uIUD7pnRKAeiQtC7huUYXDFk6_n_XqEaycl3Upwfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏‌CocoLoop⁩؛ هابِ هوشمند و امن برای کشف و نصب اسکیل های ‌AI⁩.
🚀
‏
✨
ویژگی‌های کلیدی:
‏
🔍
جستجوی سریع و دقیقِ مهارت‌های ‌Agent⁩
‏
🛡️
بررسی امنیتِ ابزارها قبل از استفاده
‏
👥
جامعه‌ی فعالِ توسعه‌دهندگان و کاربران
‏
🔥
دسترسی به ترندترین و کاربردی‌ترین قابلیت‌ها
🔗
http://hub.cocoloop.cn
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7294" target="_blank">📅 22:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7293">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb979dcf62.mp4?token=aaAweC57SdyzmMO4F94-FRhjaNnmS0BbNT4XthI_IVYzWNNkI5yi9Ie94Rr3sEWXb5JFFStv1-meFkaMhVXAFfkkUJQZWaPfUzfhjWVYbPFg2Y-vIXm0nlJmahoIRgc_wIU19eoIAoO0SpTqoD7Y5sXc9GZMIGBGm3JV_MrnBsza6ozKouyOBtemi9XnkQIGBoGZ4NU5is__F0RFqa8zRE3E1LnfgMArFIbczsSPe1j71kv3DBa6NmKiJhGBRqvnCXABbbxyYSkoE3IY1GMdJ26NA02pNEA5tOtdWI3KufIFnrKRMG4sAKl4UBIfK4t3ImB6G07SUOFtYvJ4aWnvuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb979dcf62.mp4?token=aaAweC57SdyzmMO4F94-FRhjaNnmS0BbNT4XthI_IVYzWNNkI5yi9Ie94Rr3sEWXb5JFFStv1-meFkaMhVXAFfkkUJQZWaPfUzfhjWVYbPFg2Y-vIXm0nlJmahoIRgc_wIU19eoIAoO0SpTqoD7Y5sXc9GZMIGBGm3JV_MrnBsza6ozKouyOBtemi9XnkQIGBoGZ4NU5is__F0RFqa8zRE3E1LnfgMArFIbczsSPe1j71kv3DBa6NmKiJhGBRqvnCXABbbxyYSkoE3IY1GMdJ26NA02pNEA5tOtdWI3KufIFnrKRMG4sAKl4UBIfK4t3ImB6G07SUOFtYvJ4aWnvuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
ابزار ‌PromptCard⁩؛ کلیدِ رمزگشایی از دنیای تصاویر!
🔑
🎨
‏با این افزونه‌ی کروم، هر عکسی که می‌بینید تبدیل به یک پرامپت مهندسی‌شده می‌شه تا بتونید دقیقاً همون سبک رو در هر هوش مصنوعی بازسازی کنید.
⚡️
‏
🛠
قابلیت‌ها:
‏
🖼
آنالیز هوشمندِ تصاویر
‏
📝
استخراجِ دقیقِ دستوراتِ متنی
🔗
دانلود افزونه
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7293" target="_blank">📅 21:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7291">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آپدیت 1.0.4 کلاینت UAC-SNI-Spoofer</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7291" target="_blank">📅 18:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7290">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldHdB4hJmV8Xs8UwJlau80cBWZYBMu71Wcr2xukCdWzKB6kBiheDPlLeRhvvi20vwlPPRVFPv3PMHHLY5KSpuDaefEjNIpN2GNku3p758jST7A3hJSDrIbBO4gl_4gPNOTc9ntaO7dIeu9Nf9Tw_mX-qahdnEp74Jr41ANkyHnhh1bPCU_LLQ7FRNIjYoE9l_6Vf8wI40HjZJIny0Kg4WQBGLtPGKDB22XfcMfaUNBITtnYCzVG4zCEX2HOeHPiD31sln2s5NiQ5oOoKbu7ZRZqKBKNGkQa3cuOXAsUEdfXHhUu2YRalGbeT3rPMxS-acRajxKUxWNhlx9DNkowEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان  ایجنت روتر (سرویس API چینی) امروز علاوه بر Opus 4.8، مدل‌های GPT 5.6 Sol و Kimi K3 رو هم اضافه کرد
🔥
برای فعال‌سازی فقط کافیه یک اکانت گیت‌هاب قدیمی داشته باشید و از طریق این لینک وارد شید
✅
🎁
با…</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7290" target="_blank">📅 17:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7289">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgMdjBy0tP7kZP6Jpvc4tXKPsJO2guSd7xCgEjPTzT3vt-0xKLekxvFnICe0vXrI_ga43HoTABUbS-pMiEw82XqLRqmj1r5_7Yhqt0pSysuU9WBwr7Ufw0XUsdPqTXXpypLxdxAo1_s3s6kW0AzbJ6UxwworTykj69PUwDXn4XcXUGc68wzsI136aNWT25tL03jTYRZLSXT_6rstRNb-4Sv8ek1Nu4ENS34bCTnfmwCbxjmairz-SAPtjwG3ttgHW0mtkJlZiwM7Of-g1ilCcTZzWc299j2yKUMS8qBjnoc2t2EOYEGKXp8owaq0WTblBRTtSt0XT306pMl36pB9cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💸
جایگزین‌های رایگان و بدون اشتراک برای ابزارهای محبوب
‏
‏سایت
NoSubscription
مجموعه‌ای از نرم‌افزارهای رایگان، متن‌باز و قابل‌خرید با پرداخت یک‌باره را گردآوری کرده تا برای سرویس‌های اشتراکی، جایگزین مناسب پیدا کنید.
🛠
‏
‏
✨
چه چیزهایی پیدا می‌کنید؟
‏
‏
🔹
جایگزین ابزارهایی مثل Photoshop، Microsoft 365، Chrome، Premiere Pro و Zapier
‏
🔹
دسته‌بندی‌های هوش مصنوعی، طراحی، برنامه‌نویسی، بهره‌وری، صدا و ویدئو
‏
🔹
فیلتر براساس سیستم‌عامل، قیمت و مجوز متن‌باز
‏
🔹
ابزارهایی مثل
ONLYOFFICE، DaVinci Resolve، Brave، LocalSend و n8n
‏
🔹
جست‌وجوی سریع و بدون نیاز به ساخت حساب کاربری
‏
‏
⚠️
نکته‌ی مهم:
‏
‏همه‌ی ابزارهای این مجموعه کاملاً رایگان نیستند؛ برخی رایگان یا متن‌بازند و بعضی با پرداخت یک‌باره یا مدل Freemium ارائه می‌شوند.
‏
‏
📌
مشاهده‌ی کتابخانه NoSubscription
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7289" target="_blank">📅 17:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7288">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏
🛡
Aether؛ کلاینت متن‌باز برای عبور از فیلترینگ شدید ‏نسخه‌ی جدید Aether 1.2.2 با استفاده از شبکه‌ی Cloudflare WARP و روش‌های پیشرفته‌ی مبهم‌سازی، برای اتصال پایدارتر در شبکه‌های محدود و مقابله با DPI طراحی شده است.  ‏
✨
قابلیت‌های مهم: ‏
🔹
تحلیل وضعیت شبکه…</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7288" target="_blank">📅 17:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7287">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQinLR6PFSv64zVJOlfk-BYemmAluJBBzNmRVzWYW5VdcyV604l24sSTTaIl6f-LIhRKfkWhwBueJuok-dUAZzO3r2WRJ6KGLzOd0DQ3eLFQ-VHW4oTM_ZLM8SzVBfgket6pQbHDMrIjlsShyuPTLTfR6SZLsONnYFIhU203WUYioJ66DXnQszaJgVMODAWkHDWTd8HpBWRmxNG9V-N83I49hj3-ffaXeCGKqrbhxdNG1WJZTZqLoUdvYtmJyYcPDWLDu-l8cuPDWr9xcN1oZFcRQSuRd0FwWz1DAuxZ1edgMJsovprR90o_UmCF6i6SnqDW9RLhdcQnJ82KyvHXVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🛡
Aether؛ کلاینت متن‌باز برای عبور از فیلترینگ شدید
‏نسخه‌ی جدید
Aether 1.2.2
با استفاده از شبکه‌ی
Cloudflare WARP
و روش‌های پیشرفته‌ی مبهم‌سازی، برای اتصال پایدارتر در شبکه‌های محدود و مقابله با DPI طراحی شده است.
‏
✨
قابلیت‌های مهم:
‏
🔹
تحلیل وضعیت شبکه و انتخاب خودکار بهترین روش اتصال با
Smart Mode
‏
🔹
مبهم‌سازی ضد DPI با
Noize
، TLS Fragmentation و ECH
‏
🔹
انتخاب خودکار سریع‌ترین نقطه‌ی اتصال WARP
‏
🔹
اشتراک‌گذاری اتصال با لپ‌تاپ و گوشی از طریق
SOCKS5 / HTTP
‏
🔹
پشتیبانی از
Split Tunneling
و حالت Proxy
‏
🔹
کاهش مصرف CPU و رفع مشکلات اتصال، قطع و تغییر پروتکل
‏
🔹
حذف آپدیت درون‌برنامه‌ای؛ دریافت نسخه‌ها فقط از گیت‌هاب رسمی
‏
🔹
بررسی امنیتی کد و رفع آسیب‌پذیری‌های مهم
‏
⚡️
نسخه‌ی
1.2.2
بدون حذف نسخه‌ی
1.2.1
نصب می‌شود و تنظیمات قبلی حفظ خواهند شد.
‏
📌
دانلود و مخزن رسمی پروژه
‏
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7287" target="_blank">📅 16:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7286">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🟠
❌
اوپراتور های تلفن همراه به اینترنت بین الملل ضریب ۲.۷ دادن یعنی مردم اگه ۱ گیگ اینترنت مصرف کنن اونا ۲.۷ گیگ ازشون کم میکنن و اینطوری بسته های اینترنت فورا تموم میشه و مجبور میشید زود به زود اینترنت بخرید...
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7286" target="_blank">📅 15:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7285">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">ظاهرا رو بیشتر اپراتورها فرگمنت رو کلا بستن، البته باز بررسی کاملتری انجام خواهم داد.
در حال حاضر برای دسترسی به اینستاگرام و یوتویوب به طور مستقیم و با حداکثر سرعت میتونید از MitM-DomainFronting استفاده کنید (فقط نسخه وب).
* اگر از قبل از طریق فایل certificate_generator.bat سرتیفیکیت گرفتید، سرتیفیکیت شما بعد از ۳ ماه منقضی میشه و احتمالا الان نیاز دارید که سرتیفیکیت جدید ایجاد و اضافه کنید (در نسخه جدید جنریتور این مورد اصلاح شده و دیگه سرتیفیکیت منقضی نمیشه)
https://github.com/patterniha/MITM-DomainFronting</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7285" target="_blank">📅 15:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7284">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gG48F1rXIOxmaNoLj5RJqhVH6IKLZU6g_DnNkLzYBz0yAoGmEpa1qrYGc88GDnSmJJWo-vJufVlq0CEchVSNy_nj24dMK0aI7c6z5rFDlMv5YvThIBql-TYtVaAbVH-4FyJNTfNWTGRAOJxIGuR9OTcVo8gjN4rQ4ob7Udh7iRoyHfMa7CSTyBqrfDg-TLpEKddRaGqsCglf7g4iqAAxRTav9mm1rQgt3Ok54ibV-1zpqLuiTmBGJnept3sVt6LCpN40NefgkobOr9nxmTylbxKu25EiNFq1ughL2y7bbX3kxKytTkP9cjUmczOCKzC4ePqvZdcX5diRmeUNTAXiQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لو رفتن اطلاعات جدید از Anthropic؛ مدل Fable 5.1 در راه است!
💣
🔮
طبق جدیدترین شایعات و لیک‌های منتشرشده، شرکت Anthropic توسعه مدل جدید
Fable 5.1
رو به‌طور کامل تو محیط داخلی خودش تموم کرده و احتمالاً تا ماه آگوست (همین ماه آینده) معرفیش می‌کنه!
🔥
✨
نکات کلیدی این شایعه:
🔹
زمان عرضه:
احتمالاً بلافاصله بعد از رونمایی احتمالی GPT-6 منتشر می‌شه تا رقابت سنگین‌تر بشه.
🔹
قیمت‌گذاری:
ادعا شده قیمتش هم‌سطح Fable 5 باقی می‌مونه و افزایشی نداره (هرچند همچنان قیمت اکانت‌ها و API برای تست‌های کوتاه و چندتا ریکوئست ساده، سنگین و گرونه!).
🔹
وضعیت رسمی:
انتروپیک هنوز هیچ اطلاعیه رسمی منتشر نکرده، اما منابع آگاه می‌گن مدل کاملاً آماده‌ی انتشاره.
باید دید تو این مسابقه‌ی نفس‌گیر مدل‌های جدید، نسخه ۵.۱ قراره چه ارتقایی تو قدرت کدنویسی و استدلال داشته باشه.
#هوش_مصنوعی
#Claude
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7284" target="_blank">📅 15:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7283">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pem5N4ToJ9QNe4ruXj6mpg3q4ebqyluQWADcfAvf7Khka_bpeXoQXEZnflOvaUTcqn4Ss1WbY_KKv1e0o7xEDfX2Nnf9OCw0M95ZJ9pJ6TBmP-jR0-4CCfmvECHyK11Pc9BVshqLtmXtO2Z3Dj2UEoSvQO4DAFGtjetQNart0qe4viNBETyFKkhp_AsqOKuCCUtXFCSui6girG_ZzleKqQPI-tZ4_WX4pao0WGzw7Oypcr9gOlVgTxO7E9aua2-FWXnE9IbilhnDyOqD4uCj_dqRzf0hxcD4L_eSvv2IK3pdEDC-onq1dLTVa_krv0qbaa5P5Rpmd5oSxLtjMuchyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
فعال‌سازی پلن Professional برای پلتفرم Figma برا طراحی رابط کاربری وب سایت و برنامه اندرویدی با مدل های زیر :
GPT 5.6 | Opus 4.8 | Sonnet 4.6 | Gemini 3.6 flash | Gemini 3.1 pro
برای دیدن آموزش کلیک کنید
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7283" target="_blank">📅 14:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7282">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTgmiD07fHeegArEK4scbD4_GO64SMHRRB2KgMW3QJXGgfv2CRslM1LdsOkoNmyMyrMsxrL7HWVHemmCndGdHJqZmMzZCqKerZc6lP1uBd8ftQ3Pes_Dd1Aep1vbVlIyQ3ej3oBBabTRpUzOWtsnbmBXHK6cirXig7t83xPBoczY-QWTzVR5K1mQmhLlTSkh1XmToY_Q8qBTPrXxWvpGhlHTyajsGq8pusAzoWUIJNAkJ3g_dheqR1ghb6x3eI0Gz3DdyFzSLrJ9iwg2It5O0FaRPyMMnG-21w-8YU-dkeiA9N7zGRWW2JV42KH00iXbwaJCfhonF-bDCo9UTcseNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید کانفیگ‌های Serverless منتشر شد (ورژن ۴۶)
🚀
بچه‌ها، کانفیگ‌های بدون‌سرور (Serverless) به نسخه ۴۶ آپدیت شدن و روی نت‌هایی که اخیراً از کار افتاده بودن، دوباره فعال و متصل شدن!
✌️
این آپدیت شامل دو نسخه
low_delay
(تاخیر کم) و
high_delay
(تاخیر بالا) هست که با توجه به وضعیت اینترنتتون می‌تونید ازشون استفاده کنید.
⚠️
پیش‌نیازهای مهم برای اجرای این نسخه:
🔹
کلاینت شما باید دارای هسته
Xray-core نسخه 26.6.27
یا بالاتر باشه.
🔹
در اندروید، حتماً از
v2rayNG نسخه 2.2.6
یا جدیدتر استفاده کنید.
🔄
نحوه آپدیت:
اگه از قبل سابسکریپشن رو داخل برنامه‌تون دارید، فقط کافیه ساب‌لینک خودتون رو آپدیت (Update Subscription) کنید تا کانفیگ‌های جدید (نسخه ۴۶) جایگزین بشن. حتماً نکات استفاده داخل گیت‌هاب پروژه رو هم مطالعه کنید.
🔗
لینک سابسکریپشن (برای وارد کردن در برنامه):
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️
❤️‍🔥
@patt_channel_x</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7282" target="_blank">📅 14:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7281">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">چند دقیقه دیگه قراره یه آموزش بفرستیم دوباره از همون متد باحالا هست
😁
❤️</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7281" target="_blank">📅 14:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7280">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">چند دقیقه دیگه قراره یه آموزش بفرستیم دوباره از همون متد باحالا هست
😁
❤️</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7280" target="_blank">📅 14:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7278">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBWv5aKzfUn9m4AD8fxUo3qqIOTqeRw9AL9BoUyi7rTg1vu_-aE1Ta0RpztbNyBsL2kEG4mq4Wauq7Q67y1Q7-7gz2JCZKP8oIc-rZCENUcCOY5nxNRLDVbl7FkzuCwIFOX-nTNUGB6c3zvW-N_awaFHRb0JWX0rMKl0himq-59MtxD_6xnuBYqQVdOOWc3hSutcXyqJqnZFuL2ttZSJ7ZweT_Bz2dLww_1-9-lj3SI9ZEDAQ2hIQvRgOJMtL-JF-moVE-pOs4OZc6o_Tj4y9XCGlmsbaPXbanvZ5yHglo35-DEX2qhTXCqZeNvODyr5v7m-b4SQKso56EKtTr41dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی ۱۴ روزه به غول‌های هوش مصنوعی!
🚀
💎
‏با پلتفرم ‌Lumosel⁩، قدرتِ مدل‌های تراز اول دنیا رو در اختیار بگیر. این فرصت طلایی رو از دست نده:
‏
🔥
مدل‌های در دسترس:
Fable 5⁩ | Opus 5⁩ & ‌4.8⁩ | ‌Sonnet 5⁩ | ‌GPT 5.6 Sol⁩ | Kimi k3
🛠
چطور فعالش کنی؟
‏۱.
از طریق این لینک ثبت‌نام کن.
‏۲. برای وریفای، لینک ربات تلگرامی رو کپی‌کن و استارت بزن و در کانالِ تعیین‌شده عضو شو.
‏۳. دوباره به ربات برگرد و با لینک استارت رو بزن تا پلن ۱۴ روزه برات فعال بشه!
‏
💰
مزایای پلن:
‏هر ۴ ساعت ۱۰ دلار اعتبار و ۴۰ دلار در هفته برای استفاده از ‌API⁩.
‏
💡
نکته مهم:
‏برای استفاده از این ‌API⁩ در ایجنت‌هایی مثل ‌Claude Code⁩ بری ، و از یک فیلترشکن باکیفیت استفاده کن تا مشکلی در اتصال نداشته باشی.
‏
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7278" target="_blank">📅 22:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7277">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">به به
🔥
🙊
دیگه جای عسسسله لامصب عسسل باید بگیم لوموسسسله لامصب لوموسسسسل
پایین کامنت بذارین پستای وگاس لوموسله لامصب
جعبه شرودینگر وگاس ببینیم از توش چی در میاد
تا دقایقی دیگر
👇
Clock is ticking
🫣
🔥
🎲
🪄
🕦</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7277" target="_blank">📅 21:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7276">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏دسترسی رایگان به هوش مصنوعی‌های قدرتمند!
🚀
‏می‌خوای با مدل‌های پیشرفته‌ای مثل ‌GPT-5.4 mini ، ‌DeepSeek V4 Pro⁩ و ‌GLM 5.2⁩  کار کنی؟ همین حالا این فرصت رو از دست نده:  ‏۱. در ‌Boltch⁩ ثبت‌نام کن. ‏۲. کلید ‌API⁩ خودت رو از اینجا بساز.  ‏
⚙️
تنظیمات اتصال:…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7276" target="_blank">📅 20:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7275">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8W9CdCvdI5D5sRmNn4LbpqxrUnqpXXzotEXiWvexZl8IuAKW-T9gPavqD8VZZMtdpjXXASGjHEcZhkUGClbFWqJTZWXmEiaecJIMEvr15PUoa6g34mEtTOBLfXGSzUr1Xxcy_8YyDMFyIwrDA5OBliEp6lic9k3ROFqJaNKuibVBKx1uA2RDLB3UOlPRJXms_chvC9p_a2ghA0cbAZGHx5nWqZQM6S3vIEI7uyhTTtVM5nXF22PcrpIdB89ssDg872czj4doSL5bTjZMPk3xjAnCiK9CCzrd9iAFuXnKeRN0JPfsU_dOybEPMu0hROKuJHdF1TIIqXdy8CoEb420g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی رایگان به هوش مصنوعی‌های قدرتمند!
🚀
‏می‌خوای با مدل‌های پیشرفته‌ای مثل ‌GPT-5.4 mini ، ‌DeepSeek V4 Pro⁩ و ‌GLM 5.2⁩
کار کنی؟ همین حالا این فرصت رو از دست نده:
‏۱. در ‌
Boltch⁩
ثبت‌نام کن.
‏۲. کلید ‌
API⁩
خودت رو از اینجا بساز.
‏
⚙️
تنظیمات اتصال:
• ‌Base URL⁩:
https://api.boltch.cloud/v1
‏لیست مدل‌های رایگان در دسترس:
🔹
free:glm-5.2
🔹
free:gpt-5.4-mini
🔹
free:deepseek-v4-pro
🔹
free:kimi-k2.7-code
🔹
free:minimax-m3
🔹
free:qwen-3.8-max
و چندین مدل حرفه‌ای دیگر!
☑️
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7275" target="_blank">📅 20:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7274">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دوستان گلم
❤️‍🔥
این پایین تو کامنتا اعلام کنین که چه چیزایی بیشتر علاقه دارین
بیشتر ازون پستا بذاریم
البته برای همه سلیقه ها پست میذاریم ولی بسته به نظر شما سعی میکنین بیشتر اون سمتی مانور بدیم
ایشالا امشب یا فرداشب ی سورپرایز خفن دیگه داریم</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7274" target="_blank">📅 20:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7273">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHN3I7SuOop-I-dsuK_zlQI00d2A5a_DGOl8krKBBwg2pEkhGTpWRpAm5BSFolG1hmXuu7dcw2w1ZJGh-iJxkOyPDuRMbZCgvX0m2NRMrdu34P42L6WFWh4ilw7YJKZdW-tlsvQkesMJhEg2UXUGbFf5J3X__0IiIWBPoFNbbA-tXO-IbT3sMsz--spJd2MGfCbY12DWJ5xPXjhU5Ydcm_ltSH-TqmU1imFbLE8zAQ2vmTagMzwmJP4JLmufQMNlvG9Ei6J1SosHBw3GPY-66DjU14xyQx-ENIWRC7RCKteWxTh9sQpgrSeMt9mOAy8pX3MgwV22Qnrt2B5LxqfOuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
یه اصلاحیه کوچیک درباره پست متین و بازار سیاه APIها
بچه‌ها متین تو کانالش یه پست درباره بازار غیررسمی فروش توکن‌های هوش مصنوعی گذاشته بود. کلیت حرفش درباره سوءاستفاده واسطه‌های چینی از اکانت‌های فری‌تریال و بات‌های ناامن کاملاً دقیقه، اما یه برداشت اشتباه کوچیک توش وجود داره که بهتره شفاف بشه.
متین نوشته بود که از این شبکه‌ها و پروکسی‌ها «برای به سرقت رفتن اطلاعات مهم استفاده می‌شه»، اما تو مقاله اصلی (نوشته Simon Willison) اصلاً چنین چیزی مطرح نشده!
sometimes through stolen credit cards or chargeback attacks.
یعنی این واسطه‌ها برای تأمین هزینه‌های خودشون،
از «کارت‌های اعتباری سرقتی»
استفاده می‌کنن.
هیچ کجای این متن حرفی از دزدیدن اطلاعات شخصی یا دیتای مهم کاربران زده نشده.
https://simonwillison.net/2026/Jul/26/relay-market/#atom-everything
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7273" target="_blank">📅 13:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7272">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLKAAekcx5qq1VoQHCKDa89WMqOQvO85bvFgaTZ6rO1WxD2hO3C0MkHhO_uBjsPIpp6NukrPCCpJ-tp6OeAhnOFeT74sH_6XVph-U2VsnKeZM_5QQxiufhdwazMp-F5wq5hKPcF_Q3cxUfkOzFhWomlvZVyfE7oI0oJJjlAwFoD0eRQuCtyVcLbUm1ZDpmKP473S4IyH7qSsBjx1K5ywpV9Uu5l1PxmolQIvR8iFyatLGEuvjiyg4md2veDyE3b6CgYkCbSV-MIOwKYn-HTMorE9W7suwumoXFxYYXyGs8irYo-tMu4Iaez7v7MvzYfToQ-87BiXMkppaY6bsTyYPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سورس‌کدهای کامل دوره پایتون (PY4E)
🐍
🎓
بچه‌ها اگه دنبال یادگیری پایتون هستید یا دوره معروف «پایتون برای همه» (Python for Everybody) رو می‌گذرونید، این ریپازیتوری دقیقاً همون چیزیه که نیاز دارید!
دکتر چارلز سورانس (csev) تمام سورس‌کدها، فایل‌های تمرین و متریال‌های آموزشی این دوره (نسخه پایتون ۳) رو به‌صورت کاملاً رایگان تو این مخزن قرار داده.
✨
ویژگی‌های کلیدی:
🔹
دسترسی به کدها: تمام کدهای استفاده شده تو کتاب و ویدیوهای آموزشی در پوشه
code3
قرار دارن.
🔹
متریال کامل: شامل فایل‌های تمرین، تصاویر و جزوه‌های مرتبط با دوره.
🔹
امکان اجرای محلی: داکیومنت کامل برای راه‌اندازی یه پلتفرم آموزشی با Tsugi (برای اساتیدی که می‌خوان این دوره رو روی سرور لوکال تدریس کنن).
📌
[لینک مخزن گیت‌هاب پروژه (py4e)]
#آموزش_پایتون
#Python
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7272" target="_blank">📅 11:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7271">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IP7ZVeXx2ld-NvhH17-z8LIn9DfDZqBaja-aY6G7HNh1tc4EHimtxplB9YYcECGajqhfcXD_FaEck09dYHDsohswZYStzrjotCi1fzJEnCU454NBYOY7mUww5hsr2x9pFQSWfHW1VJ8bcmUzYpoFq7TcUe41ba2owncjVnivpP9tZWC6voXb2ROL52izUahYmiYvVKmBwnQ8IjWh0s9mpgd6-sj7Mw0S0qRM0hV95Q1q4OxhndMlWrcX5WLek4HX4CGiupHRlkdW-Uq1lZIl25XajsHc24-Nzs3RhcXi17Q1K2_TJn5AOwWaRpVvtCsPITWwRzumM7-kOa2ZaX94Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار PeekVault؛ ماشین زمان و کاوشگر آرشیو شبکه‌های اجتماعی
⏳
🔍
بچه‌ها حتماً براتون پیش اومده که بخواید یه پست پاک‌شده تو اینستاگرام (یا توییتر و ردیت) رو ببینید، یا برای کارهای تحقیقاتی (OSINT) نیاز به بررسی تاریخچه یه پیج داشته باشید. سایت PeekVault یه ابزار به‌شدت کاربردیه که مستقیماً به دیتابیس عظیم Wayback Machine وصل می‌شه و آرشیو پیج‌های پابلیک رو تو چند ثانیه براتون می‌کشه بیرون!
🤩
✨
ویژگی‌های کلیدی:
🔹
بازیابی پست‌های پاک‌شده:
بررسی و پیدا کردن پست‌ها و پروفایل‌های عمومی اینستاگرام که الان در دسترس نیستن.
🔹
پشتیبانی از پلتفرم‌های مختلف:
علاوه بر اینستاگرام، ابزارهای اختصاصی برای کاوش توییتر (X) و ردیت (Reddit) هم داره.
🔹
خروجی حرفه‌ای داده‌ها:
قابلیت دانلود لاگ‌ها و نتایج جستجو با فرمت‌های HTML، CSV و JSON (عالی برای محقق‌ها).
🔹
بدون دردسر و لاگین:
فقط کافیه یوزرنیم یا لینک پست رو بهش بدید؛ کاملاً مستقل عمل می‌کنه و نیازی به اکانت شبکه‌های اجتماعی نداره.
🔗
لینک وب‌سایت
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7271" target="_blank">📅 00:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7268">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCP-G6UVkLacrhqxva61GaGGHE1gOE8ACgr7K3rmjJQ3eRh2mxZN9J5iULQaQqmSw2D2QhckgLFU_G5nWnLpI4KRi6fNG4Mw02qhozBTxITh05oGmDDs6KUfxj5BEV1P5feUF7D9eMdPcAbfHmMQpMGSe-zJKdT9SdnBJr4rlYCZn9PUIagGaBmPO5NeQ0gSjjuMWVeWo85AZgoEiUB08ClpiAyqTBozz0c7wVk_jJHJXTOAI1Hgc7gl995EBcVzNOBEJhnLpTizBTG3BN4LkcIrmqk9OWYbVx315P3SSzx75hLbkkB38PNj7YZ6O-Ur5Z99zORy-kO3-_sS09ZI2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرورگر Lightpanda؛ جایگزین خفن کروم
🐼
🚀
بچه‌ها اگه برای اتوماسیون و Web Scraping از Headless Chrome خسته شدید، Lightpanda رو تست کنید! این مرورگر با زبان Zig از صفر نوشته شده، نه فورک کرومه نه وب‌کیت، و به‌شدت سبکه.
🤩
✨
ویژگی‌های کلیدی:
🔹
سرعت بالا: ۱۶ برابر مصرف رم کمتر و ۹ برابر سریع‌تر از کروم
🔹
موتور V8: پشتیبانی کامل از جاوا اسکریپت و سایت‌های مدرن (SPA)
🔹
حالت Agent: تبدیل Prompt به اسکریپت اجرایی (بدون نیاز به توکن)
🔹
سازگاری با MCP: اتصال بومی به مدل‌هایی مثل کلود، جمنای و OpenAI
⚡️
اجرای سریع با داکر (سرور CDP روی پورت 9222):
docker run -d --name lightpanda -p 127.0.0.1:9222:9222 lightpanda/browser:nightly
📌
[لینک مخزن گیت‌هاب پروژه]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7268" target="_blank">📅 20:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7267">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">config</div>
  <div class="tg-doc-extra">2.8 KB</div>
</div>
<a href="https://t.me/ArchiveTell/7267" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ المان کی دلش میخاد؟
😁</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7267" target="_blank">📅 16:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7265">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آموزش گرفتن اشتراک X20 max claude به صورت رایگان با اون متد باحالا که دوست دارید
😁
❤️
توجه داشته باشید که حتما باید روی اکانت فیک بزنید و در کل باید بدونید که بن داره
🚫
به مدت محدود قابل استفاده هست همین، حالا ها شاید متده بپره سریع برید بزنید
⚡
برای دیدن…</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7265" target="_blank">📅 15:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7264">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kyhryo2wQKjbcikO1PEob7t6KD7eqeVrTpnml8J4tYuDSkg7l8b1DkgjIKSaOBev3nMCdMwk963EKFq6Hs5x9LxHtZAro6EYDKOPsgBYnQYZzDQWK0V9AqiHRnrHPeyPN9orsidVN2Cl4APAzgljRdHY1NNRoOUrbIP5w1_IpQitgWUBAEGbjVDDDAzUnDZ0zsFlp250m7lP3DicOswDQpJRtG1Uem2GhSG82yUNKsWipqa704CpHWXgB7jL-TTbN3ulKpgcfnyoF2CSO4jcP9YES7WpomZiuEAS_NpZSIMnQs2iI5mYt0aGRJH6AFODVhbxj4Xjzg4ef1YGxvbeuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن اشتراک X20 max claude به صورت رایگان با اون متد باحالا که دوست دارید
😁
❤️
توجه داشته باشید که حتما باید روی اکانت فیک بزنید و در کل باید بدونید که بن داره
🚫
به مدت محدود قابل استفاده هست همین، حالا ها شاید متده بپره سریع برید بزنید
⚡
برای دیدن…</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7264" target="_blank">📅 15:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7263">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">من نمیدونم کامیونیتی تلگرام چرا انقد دشمنی زیاده
همه سنگ میندازن تو مسیر هم
از حسادته از فکر اشتباهه از چیه
فرض کنین ی کیک بزرگه
به همتون میرسه
انقد دیس نکنین همو
وگاس میاد پست میذاره
بنده خدا داره کامنتا رو جواب میده پست ناب میذاره. تازه و درست حسابی، اونوقت یکی میاد حرف بد میزنه. هممون همینیم داریم تلاش میکنیم کیفیت رو بالا ببریم. احمدرضا من وگاس، اس و بقیه دوستان
خدایی بده این کارا
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7263" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7261">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آموزش گرفتن اشتراک X20 max claude به صورت رایگان با اون متد باحالا که دوست دارید
😁
❤️
توجه داشته باشید که حتما باید روی اکانت فیک بزنید و در کل باید بدونید که بن داره
🚫
به مدت محدود قابل استفاده هست همین، حالا ها شاید متده بپره سریع برید بزنید
⚡
برای دیدن…</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7261" target="_blank">📅 13:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7260">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWX_EXNLDe02KhlsM1G96CFLfcvy942HvmlSOcJtU5rMuW0YDlpW3Hd2EL7z2aUBm3vAfJn1R3oS3QuQulUdCShHJibXdCrJxDolJHCv9qYDulK6ZKPx05mto1KyuOPt8wP9ukv5-HaUbKk3uflxnYc_mTl28KhgJ1O3u-0TemKoGYcNWwbcgi75M42qjV4iavfNmxQ6HU8hD6gnbGzkti49OKIFEp-toATa6KdqGLgULWOk_IPlwy1450H52kVR4o-pih5FATKNLRHBsGPcn_ZsPYlV-QphocjAZJW_lqC0X-8sjYdrS5GxKMQCrwPfSKD7K4_kJduOE1tki5Ki4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش
گرفتن اشتراک X20 max claude به صورت رایگان با اون متد باحالا که دوست دارید
😁
❤️
توجه داشته باشید که حتما باید روی اکانت فیک بزنید و در کل باید بدونید که بن داره
🚫
به مدت محدود قابل استفاده هست همین، حالا ها شاید متده بپره سریع برید بزنید
⚡
برای دیدن آموزش کلیک کنید
✅
متد به طور کامل بسته شد
❌
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/ArchiveTell/7260" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7259">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ی هول ریز بدین بریم 10 کا
❤️‍🔥
🔥
Fable 5 Opus 5</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7259" target="_blank">📅 13:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7258">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔥
6 ماه اشتراک رایگان از Claude برای برنامه‌نویس‌ها و فعالای اوپن‌سورس!
🤯
شرکت Anthropic یه برنامه حمایتی فوق‌العاده برای کسایی که تو پروژه‌های اوپن‌سورس (Open Source) مشارکت دارن راه انداخته. پاداشش چیه؟ ۶ ماه اشتراک رایگان Claude Max 20x!
🚀
❓
چطوری این آفر رو بگیریم؟
اگه دولوپر هستید، پروژه‌ای دارید یا تو کامیونیتی‌های اوپن‌سورس کدی زدید و مشارکتی داشتید، اصلاً این فرصت رو از دست ندید.
کافیه از طریق لینک زیر فرم درخواست رو پر کنید. (نکته: ممکنه بررسی ایمیل‌ها زمان‌بر باشه یا حتی لازم باشه بعد از چند وقت دوباره درخواست بدید، ولی در نهایت تایید می‌کنن و به شدت ارزشش رو داره).
🔗
لینک ثبت‌نام و اپلای:
https://claude.com/contact-sales/claude-for-oss
حتماً بفرستید برای دوستان برنامه‌نویس‌تون تا اونا هم استفاده کنن!
🔵
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7258" target="_blank">📅 13:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7257">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ی هول ریز بدین بریم 10 کا
❤️‍🔥
🔥
Fable 5 Opus 5</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7257" target="_blank">📅 13:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7256">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ی هول ریز بدین بریم 10 کا
❤️‍🔥
🔥
Fable 5 Opus 5</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7256" target="_blank">📅 13:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7255">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdUGPDa1WhxacrxOMAM3B94ZozA81u8U9RSGQ4tarOYdckBkKm3wCUUHmrWPvkdYaPdvkCSFmNIuufPZZR9E5vhrcYON_ziI7DmUgUP5PxdbWKbQy1KptplnivnAchaIRqHPvg_mCt_WTFPXUpX37f7EnVK9FxZH4mz3arrB8x7I-AnuYKDTC8p_OTmdmMcaQzPvlOxhSWOeTQsylFwNGFpwPyDClS5-9pGYj-eJ0vzCJdQRkeW_dgujKz1XYUWMpJT3aMqrbSCTU_1XTpumUSLGEyousuDJxXCtbb-peklCaX9NwFwEHclSWE0LgkZ_BEjpphtrCORSbF0EHj5g7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ی هول ریز بدین بریم 10 کا
❤️‍🔥
🔥
Fable 5
Opus 5</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7255" target="_blank">📅 13:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7254">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ثبت دامنه با قیمت پایه در Alibaba Cloud (از ۰.۱ دلار)
🌐
سرویس ابری Alibaba Cloud یک فرصت ویژه برای کاربران جدید فراهم کرده است که امکان ثبت دامنه با هزینه اولیه بسیار پایین را می‌دهد. این طرح می‌تواند برای راه‌اندازی پروژه‌های جدید و کاهش هزینه‌های اولیه…</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7254" target="_blank">📅 12:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7253">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ثبت دامنه با قیمت پایه در Alibaba Cloud (از ۰.۱ دلار)
🌐
سرویس ابری Alibaba Cloud یک فرصت ویژه برای کاربران جدید فراهم کرده است که امکان ثبت دامنه با هزینه اولیه بسیار پایین را می‌دهد. این طرح می‌تواند برای راه‌اندازی پروژه‌های جدید و کاهش هزینه‌های اولیه مناسب باشد.
✨
جزئیات تعرفه‌ها:
🔹
دامنه‌های ۱۰ سنت:
ثبت پسوندهای
.xyz
،
.shop
،
.store
،
.online
،
.icu
و
.fun
تنها با ۰.۱ دلار (۱۰ سنت) برای سال اول.
🔹
تعرفه ویژه دات‌کام:
ثبت دامنه
com.
با قیمت ۵.۹۹ دلار برای سال اول. (این تعرفه نیازمند ثبت حداقل ۳ ساله است و قیمت سال‌های بعد برای تمدید، ۱۲.۹۹ دلار خواهد بود).
📌
شرایط استفاده:
▪️
این تخفیفات صرفاً برای
حساب‌های کاربری جدید
قابل اعمال هستند.
▪️
هر کاربر تنها مجاز به ثبت
یک دامنه
با این تعرفه‌های ویژه (برای سال اول) است.
▪️
قیمت‌های ذکر شده مربوط به سال اول است و هزینه تمدید در سال‌های آینده به قیمت عادی بازمی‌گردد.
🔗
[صفحه ثبت دامنه در Alibaba Cloud]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/ArchiveTell/7253" target="_blank">📅 12:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7251">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9-pCb4OhVaWDF6tJYZLoHaC45IbHTfn3_-Fg5pFW2b7dBfKB9QWT6hpaKN0IeGGvVym_dPQRfvroSY1HJbJ1DmueR8a7XAXk0v3yNOBhbnl243AqumTBaGU9ve3aWNUKCyqwpo1jHtOnxGDyQTiUk8sWYRDS8jRVSG2s1C1LXawyY1Kb-hP34701Cyu5NIdWZlTnsyXFlNWuLN10VN2wLzhm0i-oBb5WAJ0pmUpMvJmVQya5DEgpw3A4TU2gYevVPpDSs1xe7kE-EH7RuQw4i1ycATZAsOsk4WK0yNxNSEWgRvyqAiyhQIZKk34puBIj1L3SpT4De5urzR1X1fszQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پادشاهی Kimi-K3 در توسعه وب
👑
🚀
تو رده‌بندی جدید WebDev AI، مدل kimi-k3 با درخشش بی‌نظیر تو کدهای فرانت‌اند و دقتِ بالای رندر 3D، غول‌های Anthropic و OpenAI رو کنار زد و قاطعانه رتبه اول رو فتح کرد!
🤩
✨
۴ مدل برتر جدول:
1. kimi-k3 (Moonshot)
🥇
2. claude-fable-5 (Anthropic)
🥈
3. gpt-5.6-sol-xhigh (OpenAI)
🥉
4. glm-5.2 (max) (متن‌باز -
Z.ai
)
🔥
🌐
Link
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7251" target="_blank">📅 03:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7249">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">۳ تتویی که همیشه برای آینده بهت انگیزه میده:
Don't stop:
یعنی متوقف نشو و به مسیر موفقیت ادامه بده.
Round || :
یعنی اگه بار اول شکست خوردی، جا نزن، پاشو و برای بار دوم ادامه بده.
Oh yes daddy:
یعنی پدرم تاج سرم، هر وقت خواستی جا بزنی، یاد زحمات پدرت بیفت.
🔵
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7249" target="_blank">📅 01:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7248">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbFblHukrbTEWieUsZVD_j69-L7O4JTO1os6AcbM80XVVgQegqst9kiBftGirPIhYEPieU9iIAdwBPgDaXHc5TobdvxiySJ-tP_DvRszuWql6MzWKZi_7v5l0Tx37a9j9GRBxuUXfRt_0-YZ4cOpUcyz1dFt2wSlO22VA-1bBvNjhhibpBt-8-sTZwrBjzCC21SkR2opEaTYpEdlOko_nqg4EACsEvcsr1fNc2X1BxuWbcwoFicP-7J85tyhpbwP5hmsXTVpWuspNDJ1YJakV3S-tphC_aJZGeHHPfeKOBCjBx2r-KW78ViZ4QM5sZfRlOk1FmyuSSVWxpeCUYJ-xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار BackPack؛ انجین قدرتمند تانل معکوس
🎒
🚀
یک راهکار حرفه‌ای (توسعه‌یافته با زبان Go) برای برقراری ارتباط پایدار بین سرور ایران و خارج. BackPack با شبیه‌سازی اثرانگشت مرورگرها و رمزنگاری پیشرفته (حالت Stealth)، ترافیک شما را از دید سیستم‌های فیلترینگ (DPI) کاملاً پنهان می‌کند.
✨
امکانات کلیدی:
🔹
پشتیبانی جامع از پروتکل‌های TCP, UDP, WS, KCP
🔹
حالت مخفیانه (Stealth) برای عبور امن از سد فیلترینگ
🔹
لغو هوشمند تنظیمات مخرب جهت جلوگیری از قطعی (Auto-Rollback)
🔹
مانیتورینگ زنده و مدیریت یکپارچه از طریق ربات تلگرام
⚡️
دستور نصب سریع:
bash <(curl -fsSL https://raw.githubusercontent.com/AminMGMT/BackPack/main/install.sh)
📌
[لینک مخزن گیت‌هاب پروژه]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7248" target="_blank">📅 23:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7247">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دور زدن هوشمند فیلترینگ ویندوز با تفکیک اپراتور
⚡️
🛡
نسخه 1.0.3 ابزار UAC-SNI-Spoofer منتشر شد. این کلاینت ویندوزی با ترکیب هسته Xray و متد SNI Spoofing، کانفیگ‌های همراه اول (mci) و ایرانسل (irancell) را کاملاً ایزوله می‌کند تا بدون ایجاد تداخل، بالاترین…</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7247" target="_blank">📅 23:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7245">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsplf2Yw6OiaIjBZ4gQ9x8FHnA6PzbbI0rKRAiQk8xgM8W8Xl_cwtONEV4pz3S2lPZNn8Fyi0GwuttVgy0Mt5kfuETOCoCC1F2srtuDgLimw6piSwEpoq6N2CyTnErF4BaNHnviTl23Q9_wgpFphDdJm7Dw3_FyEVR8jU1rUzqonzaTTxiA627XgNinkPrNmQH_RPafvPM4YPgd1vLRzC6_Qun7BvkPQiN5SlPwOT5cmteM1alJtcJ5dTTCf8vuc02mqnXXjeEh2_2SZXPVdOrhMubgPUYkonaMhahfR32OgauviMdKD7nhrC-NPkuYRHwl-dvDYVYpammabEv9Zaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یچی خفن پیدا کردم که دست خطتون رو تبدیل میکنه به فونت
😁
🔥
ی هول بدین فقط نزدیک 10K بشیم مژدگونی رو بدم
❤️‍🔥
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7245" target="_blank">📅 16:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7243">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یچی خفن پیدا کردم که دست خطتون رو تبدیل میکنه به فونت
😁
🔥
ی هول بدین فقط نزدیک 10K بشیم
مژدگونی رو بدم
❤️‍🔥
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7243" target="_blank">📅 15:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7242">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMqbg47rkFzca-ehHQJ4tYqdgyErBcYJaBK65xlvRSEc0tpJSJmPjH7qtMM8OaWXemvjfTnG_MLOQJ2hP8k7xZafURSm3YgthVOLrAhozDqNKBnPLBrybrFNhaanPoThh7ZkdG4l_qjddsmvHqesXuUvFdD7UEwKgz_qPNV4WXii1t-0kMXe3PEKE9Q-Sl5bL121CApBN-EvmuafrgTSA8BfA6a8XP2LczC4etw05qxim8bMnCTDlInt7Z5Z_XcR9hYnoK-ARfQHABsMOSDi_NrQeU6v1CvvxkSFWQapyDswVe_PGCq-0ycaKjQS2v4bqf5JARvQz-fcaaoOyQ8oVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت L×Box؛ چاقوی سوئیسیِ دور زدن سانسور
📱
🚀
این کلاینت اوپن‌سورسِ اندرویدی روی فورکِ اختصاصی sing-box سوار شده و خفن‌ترین پروتکل‌ها رو به‌صورت نیتیو براتون اجرا می‌کنه. تازه می‌تونید با یه کلیک، اشتراک WARP کلادفلر رو مستقیماً روی دستگاهتون بسازید و وصل بشید.
✨
ویژگی‌های کلیدی:
🔹
کلکسیون پروتکل‌ها: اجرای VLESS، Hysteria2، AmneziaWG و XHTTP
🔹
مسیریابی هوشمند: اعمال قوانین متفاوت بر اساس شبکه‌های وای‌فایِ دستگاهتون
🔹
زنجیره‌سازی سرورها: متصل کردن پروکسی‌ها به هم واسه افزایش حریم خصوصی
🔹
توزیع بار: پخش کردن ترافیک بین چند سرور واسه پایداری بهتر
🔹
ضد فیلترینگ: مجهز به DPI Bypass و مانیتورینگ زنده برنامه‌ها
📌
[مخزن گیت‌هاب پروژه]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7242" target="_blank">📅 11:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7241">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ایپی تمیز مخابرات  104.19.207.128 162.159.193.250 104.17.92.34 104.17.88.3 104.19.136.8 173.245.49.80 172.65.48.177 104.16.61.8 172.64.188.55 104.16.37.8
🔵
@ArchiveTell | 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7241" target="_blank">📅 11:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7240">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sY2nJzXv5gm5hp5T6uXgMrUWcW6kTWNsb3kqQisz2pXVO6WxnydiQY6pae7UCInlTuLbqjh2UbC6I-5cImILqS5EPEMx7TETIBZZ6WBE6AGNRkFvnkrkI5IuB21D1H6d7E8tg1io8A6VK50zBr-OW2KDDfqcMcTDvZH6H_9RcS7M5cNBFkoxh7u-8G-aYkdH5KYIrFdzQQKE5zSxDKQbFiWWc6xXU_v-hkIBnm84pZ3kPErkE2ZGj5i_WqPPefJvqjG86uGSBsXCnsqWTwof7dXT3nxwDs1EqNydLIrEghf5cDVxz6WT-6m0C6aLocnrS1Yb84-pg0HHUxjk6GR0pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
اشتراک ۱ ساله رایگان Hidely VPN Premium
📱
آموزش و نحوه فعال‌سازی:
1️⃣
ابتدا برنامه Hidely VPN را از گوگل‌پلی دانلود و نصب کنید.
2️⃣
یک حساب کاربری  جدید ایجاد کنید.
3️⃣
وارد بخش My Profile شده و روی گزینه Redeem Code کلیک کنید.
4️⃣
کد زیر را وارد کرده و تایید کنید:
HIDELY-VPN
📌
نکات مهم:
* این کد برای هر دستگاه یک‌بار قابل فعال‌سازی است.
* اگر مبخواید کد رو روی اکانت‌ها یا جیمیل‌های دیگه هم فعال کنید، میتونید از شبیه‌ساز استفاده کنید.
📥
دانلود برنامه از گوگل پلی:
📎
Hidely VPN
🔷
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7240" target="_blank">📅 09:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7239">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvRt7iDZQQtRVUjS8XWc8C2dNpf9ZheCQ9a20hTbbQ9X4C0dEW-QT_Eg96F4GyPbOUWb-7RAc3fUQs7MD1VcIzFGuahMH04bBAMODEVC1njpX6lBu7r83uzRBP4GQisf9JyB5OJ-JWgwMNSfct5DQ36WSecXjsuaSrFAkWjnaPYebKNSb2j8RaS9fhH6ElbCOpJx4yYVa2aXrRjMv6eKWOI8qTYAe2Jdi2FhNmlcmWK6g-GoNy7uqeODhVYAbytpl-_lxYQ3KuTYZS7K6X-bK9GVNSsfn4GjwpOQTF7erbrUO0HqSJ2avUvcCKfm2xQ4D2FlrT86M-C3CzAGi7c33w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
آموزش ساخت Proxy شخصی با Nova Proxy
اگه دنبال یه
پروکسی شخصی
و ساده هستید،
Nova Proxy
این امکان رو میده که با استفاده از
Cloudflare Worker
برای خودتون یه
پروکسی
بسازید، بدون اینکه نیاز به
خرید سرور جدا
داشته باشید
✅
⚙️
مراحل نصب:
⭐
اول وارد سایت
Cloudflare
بشید و یه
اکانت
بسازید
👤
➖
➖
➖
➖
➖
⭐
برید به صفحه نصب
Nova Proxy
novaproxy.online/install
➖
➖
➖
➖
➖
⭐
گزینه گرفتن
Token
رو بزنید، داخل صفحه باز شده به صورت خودکار  برای شما پر شده و فقط کافیه تا انتها روی Continue to summary بزنین روی Create Token بزنین و کپی کنید
⭐
نکته : توکن رو یه بار بیشتر نشون نمیده پس حتما دفعه اول کپی کنید
➖
➖
➖
➖
➖
⭐
توکن
گرفته‌شده رو داخل
Nova
وارد کنید و روی
Create my nova
Panel
کلیک کنید
➖
➖
➖
➖
➖
⭐
حدود
30
ثانیه صبر کنید تا
Worker
و تنظیمات لازم
خودکار
ساخته بشه
🫥
➖
➖
➖
➖
➖
بعد از اینکه Worker به صورت کامل نصب شد یک پسورد از شما میخواد بسازید که زمانی خواستید لاگین کنید از پسورد خودتون استفاده کنید و در نهایت یک ساب لینک اختصاصی بهتون میده  که میتونید داخل کلاینت‌هایی مثل v2rayNG، Hiddify و Clash استفاده کنید
⛓️‍💥
➖
➖
➖
➖
➖
برای ip های تمیز هم از لیست پایین میتونین استفاده کنید
⭐
185.235.243.19
chatgpt.com
grok.com
chess.com
openai.com
npmjs.com
➖
➖
➖
➖
➖
➖
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/ArchiveTell/7239" target="_blank">📅 02:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7238">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjrB4TeTvq1gj_06FeiyeO354uVo-FmMOllGv2cOk0ZzXgnwqjHRajcafyyP3X_4KPP8-moVxE4Pc9SP-VFnCgyuWgfQrKcwiesBuapieZrnk_jH7aDeJcjRLGtC1aiA0GH9OWkM5mN-08eumTx8Y2rxuQkk8Vu5q3bOPda1M__KOaBiDuKco-wqwNUYZDsrBZNMljJhZp5UExrv3A24dGxrBVyPJ06wUjJ-ZLUJyjVyDquS71CnHyuRDZ9eLxuLmJlCaMYrkmeB0BRGHTX6wembV7S0qBRoeJhQ35ewwnqTEr-vn9nvafHRD9SAaEWRSEG-_yKifik3jjv373QOsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
قرعه‌کشی ویژه: اکانت یک‌ماهه نتفلیکس رایگان!
🎬
🍿
رفقا، یه فرصت عالی براتون داریم! قراره بین شما عزیزان قرعه‌کشی کنیم و جایزه‌ش هم یک اکانت یک‌ماهه نتفلیکس برای برنده خوش‌شانسه
🤩
👇
چطور تو قرعه‌کشی شرکت کنیم؟ خیلی ساده‌ست:
🔹
کانال ما رو به دوستانتون معرفی کنید (ارسال پست‌ها یا لینک کانال برای حتی
یک نفر
از دوستان، یا داخل گروه‌ها و چنل‌ها کافیه).
🔹
از پیامی که فرستادید یه اسکرین‌شات بگیرید.
🔹
اسکرین‌شات رو
تو بخش کامنت‌های همین پست
بفرستید.
⏳
مهلت شرکت:
فقط تا فردا عصر، ساعت ۱۸
پس همین الان دست به کار بشید و شانستون رو برای یک ماه تماشای رایگان فیلم و سریال امتحان کنید
🚀
منتظر اسکرین‌شات‌هاتون زیر همین پست هستیم!
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7238" target="_blank">📅 00:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7237">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEOKkE_KI0mEvBeYtUhLnB6Sck42DKVnbQwEpGKzAB51r6pctAwD8dzMzEXl6s1n4SLXn0EvLDcAALq9ODXtT4q997jBfKYeubwI1hTkrSoRfR7axh7bh9hvlR_cqbORkpxrqoLoby638Zx5AavjIdsi8IBgaR8kYYQs66jU4xXYeRMBpWSv2ci_9IrMQpzltof0dsxe0pGwqM5yeJV8UwTURuCdKItgly6G79Kn86HT7dxnHw3nJAMlfQrC6vepdhDr23ghQFsdy3YcYGCLLTUCdyUwKt-fJvWXneuHIuo1gecGHGhc2ADtgOIfgpm2ICNYREKJK5zmB9xjnp0Ecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی رسمی مدل Claude Opus 5 توسط Anthropic
🤖
✨
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7237" target="_blank">📅 00:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7235">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ابزار Text Surgeon؛ ویرایش نقطه‌ای متن‌های طولانی با هوش مصنوعی
✂️
🤖
وقتی از AI می‌خوایم فقط یه بخش از یه مقاله یا متن طولانی رو ویرایش کنه، معمولاً کل محتوا رو از اول تولید می‌کنه که هم کلی توکن هدر می‌ده و هم ممکنه ساختار اصلی رو بهم بریزه
🤦‍♂️
پروژه اوپن‌سورس Text Surgeon دقیقاً برای حل همین چالش توسعه داده شده! به جای بازنویسی کامل، هوش مصنوعی فقط کلمات اول و آخر بخش موردنظر رو مشخص می‌کنه و این ابزار دقیقاً همون قسمت رو روی سیستم شما جراحی و جایگزین می‌کنه؛ بدون اینکه بقیه متن دست بخوره
💡
✨
ویژگی‌های کلیدی:
🔹
جایگزینی دقیق:
ویرایش هوشمند از طریق تشخیص ابتدا و انتها، نشانه‌گذاری یا کلمات خاص.
🔹
رابط کاربری وب:
محیط سبک و کاربرپسند با پشتیبانی کامل از زبان فارسی (RTL).
🔹
حفظ یکپارچگی فایل:
بک‌آپ‌گیری خودکار قبل از تغییرات و حفظ پاراگراف‌بندی و ساختار اصلی.
🔹
کاهش هزینه‌ها:
جلوگیری از هدررفت توکن‌ها و زمان برای پردازش‌های اضافی.
🔗
https://github.com/faithsaly5-stack/TextSurgeon
🔵
@ArchiveTell
| S
😎</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7235" target="_blank">📅 23:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7234">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEX1ADNjVEi0VsySI6Yr4KFKRYCEpwvvoGH_T_MVH2lzHIKNUVXyRSca06lcakiSSiQMfbI3JhO9DMTbssRoCgONlUALCEe6pGD1vIxQdRKlzvcX2Afi41gBb9e6VQpeyXN4oX5BLRZuOf240Q-z1aS0o_z_xGrw35R-UNhQIUOQLP-VRAPp5mp8JN4zAJCsbh-qAbGeGIPPAB5K_eERqjlz2-V6WWRB98JRuvLXuU0RGtDe1Yt7rEUk3L4b5IGmOrzX7ne8sPzujpgkBYrJ3FhG_qeUlEXBucDNCz1oNlmcUgR0CIYZehoaaIovmneTEWv1ksN01qw8EOcHSZ0vpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
ایجنت روتر
(سرویس API چینی) امروز علاوه بر
Opus 4.8
، مدل‌های
GPT 5.6 Sol
و
Kimi K3
رو هم اضافه کرد
🔥
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
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7234" target="_blank">📅 22:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7233">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ساعت 22 یه سرویس API که قبلا گذاشته بودیم و عالی هم بود که امده طی یه حرکت بهترین مدل هارو اضافه کرده
⚡️
قراره دوباره واستون بزاریم و توضیح کامل بدیم ، آماده باشید
❤️
🔥</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7233" target="_blank">📅 21:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7231">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M9YC4h9UanOJkqQVaJQoh6YNW6Gd5E99H0GoPKGs4C5qvvx3FMsvi6Pi71z8Jm-FFIr_hkh1W6IF1rqEluVJ1hz2FBI-m7XD8SxzBnsHPXODgEcsBEsz9r7YXffy-J8RQvrocXfj8hWFUDu2RCa7WkH7jLBazOMmRhlnZiB4gpncYXASlH1fdBGQ6Nn_WOeVyrDOThsV5ns50g8Zco_uEIIPXMDEL3ZTqmen0a6YDjbUwfHSTYDldLDijLLm7ImJ1nNebugBxpHKC_ThSF5RJBPiMk0qbCdaXPacw0QT2K3y8FV8meI4t0LB8AWd2ZvKaPNa9_nmC1P6_6Px-Cp4hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H3mxbV16IXreUQw-thxnxIPRYJ2WJQispPn9BXY1NWvMpAu0NaGBiImtUyQK9S5CA8STc1Io3u00ygRsIA3o8XqTpX-9VKXPdGAL1mTgCFGEVEDaw4zNFbce3eOW8nqkMorfBRmP_Kkv6zPxxtbI8niSbQwwpIP6neDhHpXkRd1Jng_FJlYXMRKvgjacZEDqZwPlwV5Uu-WTaXgRtrJeoRj3gOx5RrLdNxP0MVvfqZ_bKXkFERKl4RMQz-ebqjur6GGWzRkT7exmaw0QoZwDc-6D87QKB6vtRgBGznbqzk1wFFR0i-aRiPj8Y2DrIBCLDTQPj3ucDQG_B4yvliNXzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مدل Opus 5؛ پادشاه جدید بنچمارک‌های هوش مصنوعی
👑
🤖
آنتروپیک با Opus 5 استانداردهای جدیدی رو تعریف کرده و تو اکثر تسک‌های پیچیده ایجنتی، رقیب اصلیش یعنی GPT-5.6 Sol رو کنار زده
🚀
✨
نتایج کلیدی:
🔹
حل مسئله پیشرفته:
ثبت امتیاز خیره‌کننده ۳۰.۲٪ در بنچمارک سخت ARC-AGI-3 (در برابر ۷.۸٪ رقیب).
🔹
کنترل سیستم:
برتری قاطع تو کار با ترمینال و کنترل کامپیوتر (OSWorld 2.0).
🔹
کدنویسی:
با وجود عملکرد عالی، تو تسک DeepSWE هنوز GPT-5.6 Sol جلوتره.
🔹
تسک‌های تخصصی:
صدرنشین قاطع تو اتوماسیون اداری و زیست‌شناسی.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7231" target="_blank">📅 21:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7230">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">AVAST SECURITYLINE VPN
Key:
➤ 74P4QK-XB9VLJ-5ELJSA
➤ HBWVBW-KDN972-5ELJZS
➤ SRXCCS-UHW892-5ELJ2N
➤ WNDWU4-V6UZM2-5ELJ46
➤ FTAK74-MSPQV2-5ELJ9A
➤ P7FEHV-BJLHQJ-5ELJ46
➤ B96RQ6-V3U92J-5ELJF2
➤ XARGEJ-PJEMT2-5ELJG6
➤ GLM4WH-2P8LVJ-5ELJV6
➤ 9N5G6D-RWXRB2-5ELJRS
➤ QQSAEB-WCL49J-5ELJQA
➤ VCYZRS-WBM4QJ-5ELJBJ
➤ CSCZ4T-KGZCXJ-5ELJXW
➤ YUEXJ5-REHZJ2-5ELJTS
➤ UG95CM-NUFVMJ-5ELJG2
Plan: Premium
Device : 100
Android
|
IOS
|
Windows
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7230" target="_blank">📅 20:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7228">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUgWHNxmGJDVy9yHLYyFgQsCPQ2ZrJdON11Ob_y2liApWlfniDd86lmyV2_5H0ramdM0ZK7ROA2E3wPuNDeK88QC6zS-FbKuuzR8LqSMXPWlu8aRQ88SJ4vW3k5sAh5HM3oeVbJ5ejKI-PkIf8xweqE2KjqJpNNL5PDIllfZRSwkOiscgkK-e-F2IVTwy0VNbW9pfBe1iXTansOTDxsZGNaFosUl4b7xELo-T5PhUX_oPQ-9WQLRCmUkEcykVAD3_xQ_T2Q37o0Vyio1Xhh_lWVYQLY4eWSPfErD0Zdfhd1-m9yWBswWV99jX7sdOQGlyWxevgUu3Tp_ZddqstqH4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت Zapret KVN؛ غول پروتکل‌ها با هسته sing-box
📱
🔥
(زبان روسی فقط)
بچه‌ها یه سورپرایز اختصاصی براتون آوردم که برای اولین بار فقط تو چنل ما می‌بینیدش!
🤩
ایشالا چند روز دیگه تو چنل مسلم!
برنامه Zapret KVN اومده با استفاده از هسته به‌شدت قدرتمندِ sing-box-extended، خیال همه‌مون رو راحت کنه. این ابزار اندرویدی خفن، تمام پروتکل‌های مدرن و سنگین بازار رو یک‌جا و با بالاترین سرعت ممکن روی دستگاهتون اجرا می‌کنه.
✨
ویژگی‌های کلیدی:
🔹
هسته سفارشی: طراحی‌شده بر پایه نسخه توسعه‌یافته sing-box-extended
🔹
کلکسیون پروتکل‌ها: اجرای روان VLESS، Trojan، Hysteria2 و TUIC
🔹
وایرگارد و وارپ: پشتیبانی بی‌نقص از پروتکل‌های WireGuard و AmneziaWG
🔹
مخفی‌سازی امن: دور زدن متدهای شناسایی بدون نیاز به روت
⚠️
نکته مهم: این ابزار فقط روی نسخه‌های اندروید ۸ به بالا نصب می‌شه.
📌
[مخزن گیت‌هاب پروژه]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7228" target="_blank">📅 18:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7227">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دیدین یه متن طولانی دارین، میخایین یه قسمتش رو ویرایش کنین، به ai میدین از اول بازنویسی میکنه؟؟ بعد کلا جاهایی هم که درست بودن میزنه خراب میکنه؟؟
آره ایجنت ها اینو انجام میدن. ولی agent خوب که مدل قوی پشتیبانی کنه رایگان باشه نداریم فعلا.
من اومدم یه کاری کردم که با همین چت بات های رایگان موجود بتونین مثلا یه داکیومنت ۱۰۰ صفحه ای رو ویرایش کنین، بدون اینکه بقیه جاهاش رو خراب کنین.
اسمشو گذاشتم جراح متن. چون متن رو جراحی میکنه.
شب منتشر میشه
❤️
🔵
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7227" target="_blank">📅 18:11 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
