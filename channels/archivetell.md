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
<img src="https://cdn4.telesco.pe/file/j-jloKkIzf5CYxN8DFoobwPzHjZmaqqM6ILGmCWCp7kVgiCCmdonbVGrwi0eNPYiF9z-7ZFtEJQ8jjxJQllC_Adh-mskusdC7Hhu-naTgIOFT77VSvM9NFuuAt94lTccYn65NoVBXxWf7s6pRjz75ATyBEpYJ46zGRNq5GlSCuZsUEWm_wFyMsmjRQThBuFag8VHwCkU4YDdmuv9VYvyOe7UBa9cmCobtlYGl6Ht_gVSli-ZYqeCaOrXS25dmGlofzTpz4KeFOWInajwp_iwcN98CqmRww99T3pnR5GkGK7a-I9dyBPF9qF617pIXpZpvBE1cPNoNJw9tXXTo81_nA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.81K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐https://www.youtube.com/@ArchiveTelll</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 04:26:11</div>
<hr>

<div class="tg-post" id="msg-7012">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brCDitUlFnWbI48o64G9tmmOUuiTaKFCxQUq1ePUSD-PNRoa5ApmB8Zg82ZL3R-EjdF3Y8E3UKMEmyBAYx6CXsZR9u62FHKzV7ziW-5lHsbKqj_yYM68QoaPF23etdjAtZlTNwW_OltG-g-cLVkPBsHZ9PRSB5l7_6gCz7WNtMZWuCjjiREVH0xkctzSJB01T2MxQcPhKHywYqPARSm90hbOyX1lHV6AI_-HxmeavC6YnxbhKh7Lnwvg4o0pIWKvXmWe39Cve9KJTakp564ZtUxY4o_erf4c9yGd6mkkjLxfGe8bPMKSilr5otkldy5TzUx4zQhgFTyw-UX0oXv9_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دریافت اکانت ۳ ماهه رایگان Avira VPN (نسخه Prime) (
تست نشده
)
یه فرصت عالی برای دریافت اشتراک ۹۰ روزه و کاملاً رایگان فیلترشکن قدرتمند آویرا، بدون دردسر و خیلی سریع!
✨
مراحل دریافت اشتراک:
🔸
مرحله اول: وارد
لینک کمپین
آویرا بشید و با یه ایمیل (واقعی یا موقت/فیک) ثبت‌نام کنید.
🔸
مرحله دوم: ایمیلتون رو تایید (Verify) کنید و یه پسورد برای اکانتتون بسازید.
🔸
مرحله سوم: وارد داشبورد بشید؛ تو بخش وضعیت اشتراک (Subscription Status) می‌بینید که اکانت ۳ ماهه شما آماده استفاده‌ست!
📥
لینک دانلود اپلیکیشن از گوگل‌پلی
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 486 · <a href="https://t.me/ArchiveTell/7012" target="_blank">📅 02:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7011">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ai2lahxcxs41Be8b49etOupwstm9bo9v6KnboB5Fl2nNUMHiev504QnwkPqznfhwOAzVXprBjxnzwgvxKnCCm-RI9rFgj_2d8vp-IdrtjMizm9PAiUO182weEYHZKii2UPuwnwLKbPWBh83DhodXBmzRhsYabItHwXsZPkvigccAGRylnzYKiXqK6DGgEaD-ey3T0wsbtoq0zwhcg-3lgN55_oWtD4TViUMqhc51V4O79nQTihUlH_nd-NTWI5uNDH8SZLK1iIlG-pWT1AWx0cg_PCqu0fvZi8FP6aIeDYXfa-w3poteFsWfR2CTJ4FAUN2_DoKdivI5jq2v9Ugeog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار از زندان DeepSeek
👇
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 577 · <a href="https://t.me/ArchiveTell/7011" target="_blank">📅 01:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7010">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🛡
آموزش ساخت کانفیگ Bepass (متد یوسف قبادی) روی Nekobox  این روش کاملاً با پنل‌هایی مثل نهان یا BPB متفاوت است و با استفاده از Worker کلودفلر و پلاگین اختصاصی Bepass روی نکوباکس کار می‌کند تا نتیجه متفاوتی برای دور زدن فیلترینگ به شما بدهد.
🛠
مراحل راه‌اندازی…</div>
<div class="tg-footer">👁️ 676 · <a href="https://t.me/ArchiveTell/7010" target="_blank">📅 01:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7009">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🖥
نسخه گرافیکی ویندوز فیلترشکن Aether منتشر شد (آپدیت v0.3.0)  اگه یادتون باشه قبلاً ابزار خفن Aether رو معرفی کردیم که بدون نیاز به خرید سرور، فیلترینگ رو دور می‌زد اما محیطش متنی (ترمینالی) بود. حالا ابزار Aether-GUI اومده تا همون قدرت رو با یک رابط کاربری…</div>
<div class="tg-footer">👁️ 735 · <a href="https://t.me/ArchiveTell/7009" target="_blank">📅 01:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7008">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🖥
نسخه گرافیکی ویندوز فیلترشکن Aether منتشر شد (آپدیت v0.3.0)
اگه یادتون باشه قبلاً ابزار خفن Aether رو معرفی کردیم که بدون نیاز به خرید سرور، فیلترینگ رو دور می‌زد اما محیطش متنی (ترمینالی) بود. حالا ابزار
Aether-GUI
اومده تا همون قدرت رو با یک رابط کاربری تر و تمیز و فقط با یک کلیک در اختیارتون بذاره!
✨
امکانات برنامه و تغییرات این آپدیت:
🔸
خداحافظی با ترمینال:
دیگه نیازی به دستور زدن نیست؛ یه دکمه Connect می‌زنید و تمام تنظیمات و اسکن‌ها تو پس‌زمینه خودکار انجام می‌شه.
🔸
ارتقا به هسته جدید (v1.1.1):
مشکل اتصال فیک کاملاً حل شده؛ پروکسی SOCKS5 فقط زمانی فعال می‌شه که تونل واقعاً تست شده و ترافیک رو عبور بده.
🔸
ریکانکت هوشمند و اتصال سریع:
برنامه آخرین مسیر سالم رو یادش می‌مونه تا دفعه بعد بدون اسکنِ کامل، درجا وصل بشید. اگه اتصال هم قطع بشه، خودش خودکار ریکانکت می‌کنه.
🔸
فوق‌العاده سبک:
مشکل مصرف پردازنده برطرف شده و مصرف CPU برنامه وقتی مینیمایز (تو بک‌گراند) باشه تقریباً صفره!
🔸
پنل پیشرفته:
می‌تونید پروتکل‌ها (مثل MASQUE یا gool) و نوع اسکنر رو خیلی راحت با رابط گرافیکی تغییر بدید.
این نسخه در حال حاضر برای
ویندوز
(فایل‌های نصبی exe. و msi.) آماده شده است.
📥
دانلود فایل نصبی (از بخش Releases)
🔗
صفحه اصلی پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 685 · <a href="https://t.me/ArchiveTell/7008" target="_blank">📅 01:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7007">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHmnhidmHkr-qz5wAizJQYSGKiqZoxr9IF-_kCDN8quo16-zH0Jpxv09TN19omPi1iJcWAozr-NSKAGBuxfGIQEMMgnLsEDMDQCyapQyq4Z68Vq3KHRIu7jCDnaOxTy9tyRzZ2h4Z2CHkd-sZUN4HFHodNrqv_K6Wy-364pOUQUA21zyWjcg9-7Z0yzYn8DWsgB0j0ugTOSzYeMJtpQCIWBk7yM_0NRRQDpIp5s0pep7zuJPpUKtaKg2swF984AaVvLWuMnAFoivO1gkidX9EhLZpMQ_OmIes9AMGRRg1XHWrcP9QK-BcGLWWGs7bb3buuLBnnJP8Mq_57fj0cVQhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید و خفن Aether (نسخه 1.1.1) منتشر شد!  تو این نسخه کلی از باگ‌ها برطرف شده و امکانات جدیدی اضافه شده که اتصال رو خیلی پایدارتر و راحت‌تر می‌کنه.
✨
تغییرات مهم این آپدیت در یک نگاه:
🔸
خداحافظی با اتصال فیک: مشکل وصل شدن ظاهری برطرف شد. پروکسی SOCKS5…</div>
<div class="tg-footer">👁️ 618 · <a href="https://t.me/ArchiveTell/7007" target="_blank">📅 01:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7006">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🌐
پروژه Aether: ابزار ضدسانسور بدون نیاز به سرور و دامنه  پروژه متن‌باز Aether یک کلاینت شبکه‌سازی برای عبور از فیلترینگ‌های شدید (مبتنی بر DPI) است. ویژگی کلیدی این ابزار، یافتن خودکار مسیرهای ارتباطی است که شما را از خرید و پیکربندی سرور مجازی (VPS) بی‌نیاز…</div>
<div class="tg-footer">👁️ 875 · <a href="https://t.me/ArchiveTell/7006" target="_blank">📅 23:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7004">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🛡
آموزش ساخت کانفیگ Bepass (متد یوسف قبادی) روی Nekobox
این روش کاملاً با پنل‌هایی مثل نهان یا BPB متفاوت است و با استفاده از Worker کلودفلر و پلاگین اختصاصی Bepass روی نکوباکس کار می‌کند تا نتیجه متفاوتی برای دور زدن فیلترینگ به شما بدهد.
🛠
مراحل راه‌اندازی در چند قدم ساده:
🔸
۱. نصب پلاگین: ابتدا پلاگین Bepass را دانلود کرده و داخل برنامه Nekobox (نسخه ۱.۳.۴ به بالا) فعال کنید.
🔸
۲. ساخت ورکر: فایل Worker را دانلود کرده و یک ورکر جدید در Cloudflare بسازید و کدها را داخلش آپلود کنید.
🔸
۳. تنظیم آدرس: به انتهای لینک ورکری که ساختید، عبارت /dns-query را اضافه کنید.
(مثال: https://name.workers.dev/dns-query)
🔸
۴. ساخت کانفیگ نهایی: لینک به‌دست‌آمده را داخل «فایل خام» که در این لینک (Rentry) قرار دارد، جایگذاری کنید.
🎁
راهکار سریع‌تر (کانفیگ آماده):
اگر زمان یا حوصله ساخت کانفیگ را ندارید، می‌توانید مستقیماً از کانفیگ‌های آماده‌ای که در همان لینک Rentry
قرار داده شده استفاده کنید (فقط فراموش نکنید که حتماً باید پلاگین را روی نکوباکس نصب داشته باشید).
با تشکر از یوسف قبادی عزیز
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 909 · <a href="https://t.me/ArchiveTell/7004" target="_blank">📅 23:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7002">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAJQQaVp_MDZQkzD4iw2PBVtEWl3xgyqMwyxSi91z77jNRni3ZFt-LC1qIVlVYDlj9GY1_eDx9g9b0NR4wi9KGF8ty276xhGntvnkU7uRiZVoqKpVBAqPrQ8FHuXMqklGo5zwAthp_55YGXiZfaSOVYu3gw0hTm9sKWI7NkwMcfNMG7HoyEbTuiOFvGkLSytjrSc4y0uPsv2ApHFVROfLkEdt1J5HsG8nf82QC51NrVhSWqUj_XX6SoR6Ld8ILQIQSx8vasgLaLgmrC4eWwioT2pxcrjyaur_l8M1a5cKvfg0HPgxwVr3Rv6bfAjh6H_9TrNlNjhRMOTI_Bz8wmWDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
معرفی Consensus؛ موتور جستجوی هوش مصنوعی برای تحقیقات علمی!
اگر دانشجو، پژوهشگر یا حتی یک فرد کنجکاو هستید، Consensus یک موتور جستجوی مبتنی بر هوش مصنوعی است که پاسخ سوالات شما را مستقیماً از دل مقالات و منابع معتبر علمی پیدا می‌کند.
✨
ویژگی‌های این ابزار در یک نگاه:
🔸
دسترسی به پایگاه داده عظیم:
جستجوی هوشمند در بین بیش از ۲۰۰ میلیون مقاله و سند علمی معتبر.
🔸
پاسخ‌های مستند و واقعی:
ارائه جواب‌های کاملاً مبتنی بر فکت و شواهد علمی (به دور از اطلاعات زرد و نامعتبر اینترنتی).
🔸
استخراج هوشمندانه:
پیدا کردن مرتبط‌ترین تحقیقات و استخراج نکات کلیدی آن‌ها در چند ثانیه.
🔸
کاربرد همه‌جانبه:
یک دستیار عالی برای نوشتن پایان‌نامه، مقاله‌نویسی، یافتن جدیدترین دستاوردهای پزشکی و تحقیقات شخصی.
🔗
آدرس سایت:
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 935 · <a href="https://t.me/ArchiveTell/7002" target="_blank">📅 23:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-7000">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHjfhUEmp0fj_3XfDjDPYb6PluKMYCAEhvZ6VZ0mWZeJspsUnWCCxbHK077oenR0q2oEy0u4tsYOW4S0P3T0e68GgjaWLk2Z649xtLlMmIrLrhqTie-yGqVUHvNmZflVZQCC8vfz42lBIvx6SDY-OFNj1lyyYlQxDlha5Smgq6Ip_pmycVJMEF2uTZfip1zZXCBDfGeVweGoxxFfwaJOYylSjf5JO7eRnsOdjoNuMR441fR-JLfXacs9wmIAq8s2ZSGZpXwN9ATDydz8A96Pj5mqT2r96Rwpv5Z3vAcIu_yy6twhI_54RqpcXpoougNtnvrr0Y13oHGfXQPRBu38kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📦
Universal Installer؛ همه‌کاره‌ترین نصاب برنامه‌های اندروید!
اگر زیاد برنامه‌ها را خارج از گوگل‌پلی دانلود می‌کنید یا با فایل‌های چندتکه سروکار دارید، این ابزار متن‌باز جایگزین بی‌نظیری برای نصاب پیش‌فرض گوشی شماست.
✨
ویژگی‌های اصلی در یک نگاه:
🔸
نصب هر نوع فرمتی:
پشتیبانی کامل از APK, APKS, XAPK (همراه با OBB) و APKM.
🔸
نصب خاموش و گروهی:
نصب و حذف بدون نیاز به تایید مکرر (نیازمند Root یا Shizuku).
🔸
جعل هویت (Spoofing):
گول زدن سیستم برای اینکه فکر کند برنامه از گوگل‌پلی نصب شده است.
🔸
شخصی‌سازی نصب:
امکان داون‌گرید کردن نسخه‌ها و دور زدن محدودیت‌های SDK.
🔸
سد امنیتی:
اسکن خودکار فایل‌های نصبی توسط VirusTotal.
🔸
انتقال محلی (LAN Sync):
اشتراک‌گذاری و نصب راحت فایل‌ها بین دستگاه‌ها از طریق Wi-Fi.
🔸
طراحی و پشتیبانی:
رابط کاربری مدرن (Material 3)، بدون تبلیغات + نسخه مخصوص Android TV.
📥
سایت رسمی جهت دانلود (گیت‌هاب، گوگل‌پلی و F-Droid)
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/ArchiveTell/7000" target="_blank">📅 20:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6997">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuiHGaq9y9bThU7EjYl9l2Zg3CIwAolc09v24qHUEf6jKn5Ano0JM0kqUQWg_lAvVW7e8FHIhCcrjUlwIEXnMqZpOllmu_-3LPLtxm98DGsWdEDu1fNyGoZ5XV6SUIl3jYfMxBvWfxMCpmf7L3UF1sLcPWAWZUaemGNb7wmtVDCiSTL5FKypfhvMWjXNQblGuh_s0hDPjoVBNR9v0fvzG-fju45FhdHNKgjLrpMpy5vhWdBrv4o9tTV4Z_fFwlcXWBB81fp0nAVFhnIhyl0zaLwrTjqkGVVZE--KTo4gNDPeL3iv45-jEuyx7R628uCrkR0lrUX29zn4CD-jXSIbcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fP07lb43hJ_NiZujOgOv_Pl0FzF-Dj1ZS5pdmaYcUgFzI9mpZOqCur8cEOMZOKHF6cYMra7CMmB2LBah5_TIBsRbgvOicflSareRafeV53HRc9ExGUzK4dQHyD4NlLB13uhMNP6haIQ73zIbcc3j91gU0etsbdGvvvvNFG0F0kILcsoPXsLUhEyV9kNDuXMuvzQJFn08JUY6O1YKpD968P0bxYQyVUjCcr8IAfrEeZYY9is5zEuhT2ds3jlw_V0BkdP84j8yJjGZl6OkxbVvvxO3bTEhMynEF-jPygyBPap3IogsyMBFg36bLTgNlTvkpqZM9GUZfUfI9tzRlhunrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
گوگل برای ۲۵ سالگی Google Images سورپرایزهای بزرگی
معرفی
کرد.
🔹
تولید تصویر با مدل Nano Banana 2 Lite داخل Google Images
🔹
طراحی جدید و مدرن صفحه اصلی
🔹
گالری شخصی‌سازی‌شده شبیه Pinterest که با توجه به سلیقه کاربر تغییر می‌کند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/ArchiveTell/6997" target="_blank">📅 18:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6996">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioGVoTnNN6EXXsFMxnMG49moq6sQydFW8WzBtK7NEVtFgfom3dC6l3KCvfjh6T2Fc6TIl3fAMLqK3kx0D-e2kM8gt6nZwCUJmF6SZk9vm0Pwo5CNFqEgGdxH1_wiQExWg4dWvAiqShN0VIdFW1jUpJgAYJYN7dyxwb4vTD2XT0_gtyZqsNVzd7ZUATbRaejE30acHKdS9-2x3kAxwnrzZUzZS6A8leW8wpEv44mcO2yxOe8wjYqLzvgKrqTXeX1E6uZE_Bcqxz0HasUOFF0Le5TDVAMGPUw2CsWwoNiRjzpo3BUZilMgCdI3Jaya2Jw-pbr5O60DLUCxLBDSy-9WUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثه آب خوردن  کلا ۱۰ ثانیه هم طول نکشید
😐
ولی وصل نشد رو ایرانسل برام
😐
😂
😂</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/6996" target="_blank">📅 17:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6995">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byxOiK3o_k-bwYoXWtMiU1YAUaVjTFt3hi2Da9i9M0Zn_CDKjyHdksheEE0ukKgU2uA75x7R2vr4WJ75kViBFnLwb7I_6qJMJ8nU5ZmTVXAb4H7BOet1ZF8-GmvIuHrGi11mGJt2zpxchyWigyZpq1DIJqc1qaRqZCapb3dUwD4BrAYB_dAJnu8XEEwN_13vEOc4iY8PwoaMKmfPHeo9vgcqC_lpLCygFPQBEgZYowSloTVd8UBYQ1pSc7dbBFJzZi2ycA14az-2iEaOOoUdDfNRwG6Y1LxO_Cvcqe4y2A99R-tp0yxE6erQzBkkouc1tnsMAVWzPMKa51YFNJUNYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
پروژه Aether: ابزار ضدسانسور بدون نیاز به سرور و دامنه  پروژه متن‌باز Aether یک کلاینت شبکه‌سازی برای عبور از فیلترینگ‌های شدید (مبتنی بر DPI) است. ویژگی کلیدی این ابزار، یافتن خودکار مسیرهای ارتباطی است که شما را از خرید و پیکربندی سرور مجازی (VPS) بی‌نیاز…</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/ArchiveTell/6995" target="_blank">📅 17:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6994">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🌐
پروژه Aether: ابزار ضدسانسور بدون نیاز به سرور و دامنه
پروژه متن‌باز Aether یک کلاینت شبکه‌سازی برای عبور از فیلترینگ‌های شدید (مبتنی بر DPI) است. ویژگی کلیدی این ابزار، یافتن خودکار مسیرهای ارتباطی است که شما را از خرید و پیکربندی سرور مجازی (VPS) بی‌نیاز می‌کند.
✨
ویژگی‌های کلیدی:
🔸
بدون نیاز به سرور شخصی:
سیستم به صورت خودکار سرورها و مسیرهای سالم (Endpoints) را پیدا کرده و متصل می‌شود.
🔸
پنهان‌سازی ترافیک (MASQUE):
ترافیک شما در بستر HTTP/3 و HTTP/2 کپسوله می‌شود تا کاملاً شبیه به وب‌گردی عادی (HTTPS) به نظر برسد و مسدود نشود.
🔸
امنیت مضاعف (gool):
علاوه بر پروتکل WireGuard، از حالت وایرگارد تودرتو (Nested) برای ایجاد یک لایه رمزنگاری اضافه پشتیبانی می‌کند.
🔸
کراس‌پلتفرم:
دارای نسخه‌های آماده برای ویندوز، مک، لینوکس و اندروید.
📱
نصب سریع در اندروید (از طریق Termux):
برای نصب خودکار، کد زیر را در محیط Termux کپی و اجرا کنید:
curl -fsSL https://raw.githubusercontent.com/CluvexStudio/aether/main/aether.sh -o aether.sh && chmod +x aether.sh && ./aether.sh install
پس از اتمام نصب، کلمه
aether
را تایپ کنید تا برنامه اجرا شود.
ابزار پس از اتصال، یک پروکسی SOCKS5 (به عنوان مثال روی لوکال‌هاست و پورت
1819
) در اختیار شما قرار می‌دهد که می‌توانید آن را در تلگرام، V2ray، Nekobox یا تنظیمات سیستم وارد کنید.
📥
لینک گیت‌هاب (جهت دانلود نسخه ویندوز، لینوکس و مک)
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/6994" target="_blank">📅 17:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6992">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQzcuVp664cZvbQfDwZoPL2x2BOmlrYaVuUffjX5CybtMgvsb49VfY7tmHGEeTN4dEl582fzOC9f1vXltrNIv3v1BnL34Ph1E9txI37ijg4OgMHGjzAojDZ5_6rD0cB00ZrzDn3_CVvRjdkHC20FSiG8oHubjEknU1n9VmlrrhG5rXb0PRH9dktu0lyA6men9_lHOnSnXFc6Ks4crVLgiklwZ4COCoiVSa-yUhfJb78i8LU5Zpn_5oyanBrBzM951AuxgzLXc2WP_AhKZ11Q1e93jfV-4JOjWeM-U8YZ7FEVFAhziKQytJlV35CKwedJgld9YjWLjKDFBJSBxyCupA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☁️
اشتراک یک‌ساله و رایگان MultCloud (ارزش ۴۰ دلار)  مولت‌کلود (MultCloud) ابزاری بی‌نظیر برای مدیریت یکپارچه تمام فضاهای ابری (گوگل درایو، وان‌درایو، تلگرام، دراپ‌باکس و ۳۰ سرویس دیگر) در یک پنل است. با این ابزار می‌توانید فایل‌ها را بدون نیاز به دانلود و…</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/ArchiveTell/6992" target="_blank">📅 16:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6991">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVTGieYzJ8g23uGsl8g2UxdE5Mku6VakxY0iVbZK3jBDu4UYPbrwObmSsAI_4X5Sdm9l1Q53aEHezSjhMPccUsHsJFudLzKSLQ26tBE1EF6aKya82fC16BEYZq_pr9MCYQLSBVSD3XIk_iXUQXZlS41wFFEOH2_bp9BmZ7hgfGDDKsv34-Ld5zlgXLlTMVFc2I0rMXOC13bEO4lXNXAWVuY1L1qL3fnrBy2b9Y-_Zd7EBdMmkLlqKlOvmsg0U7lJf0tLa21gKvuSoADZxTADvEyz1U9z2qRuhdl8t7lHv-rGzlrn4NGPaxV2EIeWk1rL05pV3471K07kjjuOBidQ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☁️
اشتراک یک‌ساله و رایگان MultCloud (ارزش ۴۰ دلار)
مولت‌کلود (MultCloud) ابزاری بی‌نظیر برای مدیریت یکپارچه تمام فضاهای ابری (گوگل درایو، وان‌درایو، تلگرام، دراپ‌باکس و ۳۰ سرویس دیگر) در یک پنل است. با این ابزار می‌توانید فایل‌ها را
بدون نیاز به دانلود و مصرف حجم اینترنت
، مستقیماً بین فضاهای ابری مختلف منتقل، سینک یا بکاپ‌گیری کنید!
🎁
نحوه دریافت اکانت پرمیوم ۱ ساله:
🔸
وارد لینک زیر شوید و یک حساب جدید بسازید.
🔸
در پنل کاربری، از منوی بالا روی آیکون کلید (
🔑
) کلیک کنید.
🔸
کد پروموی زیر را برای فعال‌سازی وارد کنید:
BAAYK667N5K3K0N6
🔗
ورود به سایت
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/ArchiveTell/6991" target="_blank">📅 16:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6990">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5760952ca.mp4?token=SE14gqB5qi_i8KRD1sj3JFh3aCoFNclu_Y2cfxqFQsC5VYRmQChSPy7m1jlPqwiAMUeuifKH25g0pxYcKtJjluwE2o4XUpGSZLrm8Bvjwv8tlnhZC7ko8J42rOsEwW6r-fAum3II1RhB3BVg7v2etE8sYCet5LJ1yotpOTWXdBQ3n9W9ap_X5izxHZVHCcKPLsvURUiScEDswh1Fl2SJUetZca_E__LPpZSpMoUzNABxz_bfx5GvTXfHq9gAbB9bzoWLvgOrsJXPeaF8JBqwWdpFkZ8lAa7Adjssuv53pzGuL2r4_zuy5Shv4uTeWZV3YL6xZsCyIRhmfcR1LF7JvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5760952ca.mp4?token=SE14gqB5qi_i8KRD1sj3JFh3aCoFNclu_Y2cfxqFQsC5VYRmQChSPy7m1jlPqwiAMUeuifKH25g0pxYcKtJjluwE2o4XUpGSZLrm8Bvjwv8tlnhZC7ko8J42rOsEwW6r-fAum3II1RhB3BVg7v2etE8sYCet5LJ1yotpOTWXdBQ3n9W9ap_X5izxHZVHCcKPLsvURUiScEDswh1Fl2SJUetZca_E__LPpZSpMoUzNABxz_bfx5GvTXfHq9gAbB9bzoWLvgOrsJXPeaF8JBqwWdpFkZ8lAa7Adjssuv53pzGuL2r4_zuy5Shv4uTeWZV3YL6xZsCyIRhmfcR1LF7JvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
نتفلیکس شخصیت رو تو چند دقیقه بساز!
با Reiverr همه فیلم‌ها و سریال‌هات رو یکجا و مرتب داشته باش:
✨
امکانات:
🔸
جست‌وجوی هوشمند با پوستر، تریلر، امتیاز و توضیحات
🔸
ادامه تماشا از همون ‌جایی که متوقف شدی
🔸
پیشنهادهای شخصی برای وقتی نمیدونی چی ببینی
🔸
رابط کاربری مناسب برای تلویزیون
🔸
اتصال به تورنت‌ها و سایر منابع دانلود
🔸
نصب روی کامپیوتر یا سرور شخصی تنها با یک دستور
📥
دانلود از گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/6990" target="_blank">📅 12:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6988">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👱‍♂️
پروژه Ponytail
برنامه‌نویس ارشد تنبل برای هوش مصنوعی شما!
✨
ویژگی‌ها:
🔹
جلوگیری از پیچیده‌نویسی (Over-engineering) توسط هوش مصنوعی
🔹
کاهش حجم کدها تا ۹۴٪ و صرفه‌جویی ۲۰٪ در هزینه‌ها
🔹
افزایش ۲۷٪ سرعت انجام وظایف، همراه با حفظ امنیت کد
🔹
اولویت دادن به کدهای موجود و کتابخانه‌های بومی، به‌جای تولید کدهای اضافی
🔹
سازگار با بیش از ۲۰ دستیار هوش مصنوعی، از جمله Cursor، Copilot و Claude Code
📥
گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6988" target="_blank">📅 12:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6986">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏
🤖
پروژه Hermes Agent (نسخه اندروید)
🔥
پیشرفته‌ترین ایجنت هوش مصنوعی خودآموز (Self-improving)!
✨
امکانات:
🔸
پشتیبانی از انواع مدل‌ها (OpenAI، OpenRouter و مدل‌های Local)
🔸
اتصال مستقیم و مدیریت از طریق تلگرام، دیسکورد، واتس‌اپ و اسلک
🔸
حافظه بلندمدت، یادگیری…</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/6986" target="_blank">📅 10:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6985">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqYwabHaDriXo2kC5BfIBwkrQrAszgOHeEwYFXZMKdkqoPfOXPR3v1zBLbJFgwElv7V11pMe3o-4UZjdNhuThYzjfkUJjmpWZX339H5vbX4xIdT3wqDD5UShUS1sNJOzcRb_inJ83ZtFFK9HsgmQgR5bVQt5L3CwAkOgiyGdzg13GZDuq2euzaSoAs1lTMyRq2yfKFk-vj8edSfzLIwyDYjjGMrEN5ZU6BH1mqms8ze65nouq5SL4S5OwSNoR4QCQAEC3de9kzArxLFISdQW4uGTixydThRmZkO-l-cNNlcEv0brrME1_zb7_-_l-JGpZO_MCW8r8yi19Wt1oGqiTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🤖
پروژه Hermes Agent
(نسخه اندروید)
🔥
پیشرفته‌ترین ایجنت هوش مصنوعی خودآموز (Self-improving)!
✨
امکانات:
🔸
پشتیبانی از انواع مدل‌ها (OpenAI، OpenRouter و مدل‌های Local)
🔸
اتصال مستقیم و مدیریت از طریق تلگرام، دیسکورد، واتس‌اپ و اسلک
🔸
حافظه بلندمدت، یادگیری خودکار و ساخت مهارت‌های جدید
🔸
اتوماسیون و زمان‌بندی وظایف (Cron) فقط با زبان طبیعی
🔸
دارای اپلیکیشن بومی اندروید برای اجرای مدل‌های آفلاین (Gemma و Qwen)
📥
دسترسی و نصب:
GitHub
,
F-Droid
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6985" target="_blank">📅 10:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6984">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqJro0_sfllMWX13QbPqD1oaZKh9yRKdkGo7IbMiCWiDVRki1l7GqceQvZihC9Sn23vcIvMewWDQjtnlCoADivrF91CJpCpF8Q7kSrCsP-RN5h2vEztN3ZeG8rAOzBqbTa6CLl6eAlM21hKQC8vKLyLjg3LuoHa6ZEsfw6_v3o7sJMiZ6UVXLTRm7BPF0qf_Lg3ZG-r7EYMZRLG36PV2EB2dmCxetspnS65OQPNeIVA6mvsnrefBGY7BrDIBqUON9XoCGxgMmcQUBSj7sVW5ssVaCogMIM7HraNzmPp5BFjOmZDVFRy25XlI9icQCnxZEGU28R4NW1UTsBBVvfQQmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💎
Google Gemini API
دریافت رایگان توکن‌های هوش مصنوعی گوگل!
✨
امکانات:
🔸
دسترسی به مدل‌های Gemini 2.5 Flash، Flash-Lite و Pro
🔸
بدون نیاز به کارت اعتباری یا اشتراک
🔸
ساخت کلید API رایگان در چند دقیقه
🔸
توسعه اپلیکیشن با جدیدترین مدل‌های گوگل
📥
دریافت
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/6984" target="_blank">📅 10:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6983">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ro6Ei6psXCoYtjQuLOdfbAR9bKfvxGq8sY7R2E-1gpvXKS_qersFXJzbXsl8Vcu5jLAKv_a8fdIcWcvJK3fPhMCwD4xsDkY9bY19i18aIWsXB5p1FJLvRcv3GHnZ53dTLJYdEOHsI0Aw9XwLSvjRpS_4z-nTenHy49M4sa9gTEUQrQDnGgDcx39pAE2Fmdar-quSdFpIUNhr2tjpUHzwn8YFwwS1lSHuwwfQRMHdJt8cqBNbjD3q602kl6zjIIqDNzuLVi7WG7NnrEHfo0wOCsImOLLkqkg7SozDO1DH9fL4rvTFT47Es1FADiUP7uCoK8umkFasCPCCRMxVHRdXJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
هفته توسعه OpenAI
شرکت در رویداد و دریافت ۱۰۰ دلار اعتبار رایگان Codex!
❓
نحوه دریافت و جزئیات:
🔸
ثبت‌نام و ارسال درخواست شرکت در رویداد از طریق پلتفرم Devpost
🔸
مراجعه به تب منابع (Resources) در صفحه رویداد
🔸
کلیک روی گزینه "درخواست 100 دلار اعتبار Codex" و ثبت آن
🔸
مهلت ثبت‌نام:
تا ۱۸ جولای ۲۰۲۶
🔗
ثبت‌نام
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/6983" target="_blank">📅 08:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6981">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏
🛡
مرورگر Cromite (کرومایت)؛ جانشین قدرتمند Bromite  (جایگزین کروم)  اگر از طرفداران مرورگر محبوب اما متوقف‌شده‌ی Bromite بودید، Cromite دقیقاً همان چیزی است که نیاز دارید! این مرورگر یک نسخه سفارشی (فورک) از کرومیوم و بر پایه برومایت است که با تمرکز شدید…</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/6981" target="_blank">📅 02:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6980">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏
🛡
مرورگر Cromite (کرومایت)؛ جانشین قدرتمند Bromite
(جایگزین کروم)
اگر از طرفداران مرورگر محبوب اما متوقف‌شده‌ی Bromite بودید،
Cromite
دقیقاً همان چیزی است که نیاز دارید! این مرورگر یک نسخه سفارشی (فورک) از کرومیوم و بر پایه برومایت است که با تمرکز شدید روی
حریم خصوصی
و
حذف تبلیغات مزاحم
توسعه داده شده است.
✨
ویژگی‌های برجسته کرومایت:
*
🔸
ضدتبلیغ داخلی (Ad-blocker):
مسدودسازی خودکار تبلیغات و ردیاب‌ها بدون نیاز به نصب هیچ افزونه اضافی.
*
🔸
پشتیبانی از افزونه‌ها:
امکان نصب و اجرای اکستنشن‌ها (Extensions) در حالت توسعه‌دهنده (Developer Mode).
*
🔸
حریم خصوصی حداکثری:
محدود کردن و غیرفعال‌سازی ویژگی‌هایی از کرومیوم که برای ردیابی عادات وب‌گردی کاربران استفاده می‌شوند (قطع ارتباطات اضافه با گوگل).
*
🔸
مقابله با انگشت‌نگاری (Anti-Fingerprinting):
جلوگیری از شناسایی و ردیابی دستگاه شما توسط سایت‌های مختلف.
*
🔸
آپدیت خودکار:
دارای سیستم آپدیت داخلی در اندروید (همچنین پشتیبانی از مخزن رسمی F-Droid).
*
🔸
پشتیبانی گسترده:
قابل نصب روی اندروید (نسخه ۱۰ به بالا)، ویندوز و لینوکس (۶۴ بیتی).
🧪
نکته امنیتی:
این مرورگر برای استفاده روزمره و وب‌گردیِ امن و بدون ردیابی عالی است؛ اما خود توسعه‌دهنده صادقانه تاکید کرده که برای خبرنگاران یا افراد تحت محدودیت‌ها و سانسورهای شدید، همچنان استفاده از نسخه دسکتاپ
Tor Browser
پیشنهاد می‌شود.
🔗
[سورس پروژه و دانلود در گیت‌هاب]
🔗
[لینک مخزن F-Droid]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/6980" target="_blank">📅 02:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6979">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">net.yukh.xui_81000@ArchiveTell.apk</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/ArchiveTell/6979" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">‏
📱
3X-UI Manager  مدیریت حرفه‌ای پنل 3x-ui در اندروید!
✨
امکانات:
🔸
کنترل چند پنل همزمان
🔸
ساخت کلاینت و لینک ساب
🔸
نمایش زنده منابع (فقط نسخه +3.3.0)
📥
دانلود: F-Droid و GitHub و Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/6979" target="_blank">📅 02:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6978">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏
⚡️
پنل نهان (Nahan Panel)
ساخت و مدیریت فوق‌حرفه‌ای پروکسی (VLESS/Trojan) روی کلودفلر!
بدون نیاز به خرید سرور و درگیری با ترمینال، یک شبکه کامل و ضدفیلتر بسازید.
✨
امکانات برجسته سیستم:
🔸
نصب تک‌کلیکی:
راه‌اندازی خودکار Worker و دیتابیس D1 فقط با دادن یک API Token.
🔸
مدیریت آی‌پی و شبکه:
اسکنر داخلی برای آی‌پی تمیز (Clean IP)، آی‌پی پشتیبان (Relay) و مبدل پیشرفته NAT64.
🔸
مسیریابی هوشمند:
جداسازی ترافیک سایت‌های داخلی (GeoIP/GeoSite) برای اتصال بدون مشکل.
🔸
ضدفیلترینگ پیشرفته:
جعل اثرانگشت ترافیک (TLS Signature Chrome) و تنظیم دی‌ان‌اس اختصاصی (DoH).
🔸
ساب حرفه‌ای:
دامنه اختصاصی لینک ساب، مخفی‌سازی با تغییر User-Agent و نمایش حجم/تاریخ انقضای فیک برای گمراه کردن فیلترینگ.
🔸
امنیت بالا:
دکمه توقف اضطراری (Kill Switch)، مسیر ورود مخفی به پنل و استفاده از پورت‌های امن.
🔸
مدیریت همه‌جانبه:
اتصال به ربات تلگرام اختصاصی (فقط برای آیدی ادمین) و مدیریت همزمان چند پنل (Master/Slave) از طریق API.
🔸
نگهداری آسان:
آپدیت خودکار مستقیم از مخزن گیت‌هاب و بکاپ‌گیری/بازگردانی سریع با فایل JSON.
✅
تا به حال مسدودی روی این پنل گزارش نشده است.
🔗
اجرای مستقیم نصب‌کننده (وب)
🔗
سورس پروژه و پروکسی در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6978" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6975">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nw2zX5M2e8tVmDjppqJdXaMt9W41ZYDcljaybR9OxSaXGv65c2EfKPkA6WwRQv-uK3UGhNVjE5IrHrXlAS4jIDSagdM3X8PNgyqliV2rWsfdHLsZxlDnYMpnxAFAurQkZGxjjKSapypYXp8gNC5LQ_Vexr2NqfpvLOtGgqHercJC7E7NvlWJA7B4kwO7o0tzfA_PfoKFc4uPiOLN1RUkfilgqKLenxijK1QYGISVUPBvtYjXSKfxy18_M83UOsjx7KmwEvdIg35BaymxKTlDSadWvNac6cHzZ--MtHpulJ-FaOSWaF_Ln0wPCm4oTOYUfrVAoQQPThc-djTxzZGOog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
تلگرام دیگر برای اجرای ربات به سرور نیاز ندارد
❗️
با قابلیت جدید و فوق‌العاده
Serverless Bots
، از این پس می‌توانید کدهای ربات خود را مستقیماً روی زیرساخت خود تلگرام اجرا کنید.
✨
ویژگی‌های این قابلیت:
🔥
پشتیبانی از JavaScript:
کدنویسی مستقیم و سریع.
🔥
دیتابیس SQLite:
مدیریت داده‌ها درون خود اکوسیستم تلگرام.
🔥
میزبانی بومی:
اجرا مستقیماً توسط سرورهای تلگرام.
🔥
کاملاً رایگان (فعلاً):
صفر شدن هزینه‌های هاستینگ.
🧪
نکته: این یعنی ساخت و اجرای ربات‌های کوچک و متوسط، از این به بعد بدون هیچ‌گونه دردسرِ خرید و مدیریت سرور امکان‌پذیر است
🟠
⛓
منبع
👉
🔤
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6975" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6974">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏
📱
3X-UI Manager  مدیریت حرفه‌ای پنل 3x-ui در اندروید!
✨
امکانات:
🔸
کنترل چند پنل همزمان
🔸
ساخت کلاینت و لینک ساب
🔸
نمایش زنده منابع (فقط نسخه +3.3.0)
📥
دانلود: F-Droid و GitHub و Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6974" target="_blank">📅 22:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6972">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3Bw64-TC8HlOlZ9tY6k4No3eCnj8tQTANZ9qlkbMEvzlmRMi6lmrWo1dbsbZ-y8qytrPkVm_iEUbb5Bd3NaxpzSMGxSc6lEHYaX4OMuRuzFBTM6-MATkO_Hp_DqZloFVD0ZTlvTlF_hS6qFqrVRAcVuAR0oYktzV7-BDB_yR5xfxYFRLIO83MKHJZGL7Y50mJVruHQp3PnVFah2b02gC9F4DTkFkSA8tcemVjzRVF5nzuQ8wTMQKSAN6Bh3PJAkhSvdGPggQGlp66u99ci5jt__-qS-8ECaETqHlUFKnoSPbPcu4LvTZUQJcGEmVLO7SRKxWmvegxlyOUr0WXp4nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
3X-UI Manager
مدیریت حرفه‌ای پنل 3x-ui در اندروید!
✨
امکانات:
🔸
کنترل چند پنل همزمان
🔸
ساخت کلاینت و لینک ساب
🔸
نمایش زنده منابع
(فقط نسخه +3.3.0)
📥
دانلود:
F-Droid
و
GitHub
و
Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/ArchiveTell/6972" target="_blank">📅 22:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6971">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_cdLnJ0n2tYcxifHz4UHNBsx3MVLz4KOglOG1UXjqbiWYm92J414uEQZAXsGODHIIsN199fIAS5QC1qcMSfQ1hOtZCi0lvSgtHjKCEt1HFvypiNPpUvJt-f-29bAuiiQnL4aOtfjtUXO-yyl5TWNaxg1drNfqZJ_FgwvaLUwEvuB8BWVpPHsw-u8Lzt8g586AVpFdw3KO0hgNcqBVUuUCgQPwQpGjBZuk-t1gA8OhZC5Umvk2ZDVAPG8dDOawCWcLwq24JVczpCXTt_dMtJvUBYjkCFMTybwOLNtYc80mmrzTebfWPGSVB_xyUpRLihfz5Mgg_Ks2FfIJMfEgPSWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
Droid-ify
یک کلاینت (رابط کاربری) مدرن، روان و فوق‌العاده زیبا برای مخزن بزرگ F-Droid!
اگر از سرعت پایین و ظاهر قدیمی کلاینت رسمی خسته شده‌اید، این اپلیکیشن جایگزین متن‌باز (Open-Source) دقیقاً همان چیزی است که نیاز دارید.
✨
ویژگی‌ها:
⚡️
سرعت بی‌نظیر:
همگام‌سازی (Sync) و لود شدن لیست برنامه‌ها در عرض چند ثانیه (بسیار سریع‌تر از نسخه رسمی).
🎨
طراحی مدرن:
رابط کاربری چشم‌نواز، روان و منطبق بر زبان طراحی Material You.
⚙️
نصب و آپدیت خودکار (بی‌صدا):
پشتیبانی کامل از ابزار Shizuku، دسترسی روت و Session برای آپدیت برنامه‌ها در پس‌زمینه بدون نیاز به تایید دستی.
📦
مدیریت آسان مخازن:
قابلیت اضافه کردن و فعال‌سازی مخازن جانبی محبوب (مثل IzzyOnDroid) تنها با روشن کردن یک سوییچ.
🧪
نکته:
این برنامه در واقع یک پوسته سریع‌تر و بهینه‌تر روی همان دیتابیس امن F-Droid است و امنیت شما را به هیچ‌وجه به خطر نمی‌اندازد. اگر از برنامه‌های اوپن‌سورس استفاده می‌کنید، نصب Droid-ify یکی از واجبات است!
📥
دانلود از GitHub
و F-Droid
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/6971" target="_blank">📅 21:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6967">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PyZVGCeX4tMxZxfFBTHhc8bYICsxYzk14qDjuDRlM5g3dWDt5lenwkGmqDBlUc6vKnvUkxOYNW1JWvYIxzg1d3IZh8DzmzWG03Fa-di1uh3duBhj0-amUgnti9WuSAVlp2G3XuG0bIQ381Mc-_emaA1e6s-cbbWFxAjVN6xr0AxYlkVz8_ojuYV-2vCcPgmtXYr-5BJRZ074HGzn5cHvMvGfxi2cCBWu2mwKco-A4bp2woIIc7Xn1VimBTm7SwMHrwxzcb7br7Z9GjZ437uAPp5JWx81czC0jqNW7QhAork_Yudlwc1-ZH7oQBk6F1toTVHLJlyTbL2UweDu-v_JUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bknwjtejq5SOliHTKeIJXw58eEi4U27qRYufATgeQv5lKRDIqdE644qR00hnBOOm-a-pD2Vw46gxMU5zqWC2xTlZw1JhLeBJ6KDf7XejeJOe3t_aEvMJUGHrPbNBhFZZjFvnaiQZ_icGbdbNl7ysXhs27j1V0bNkrHMGQVuXOzx_RC1Lb0wVzW32KA_00TQdDHBjOM9S1xplhYg_nZ9v8EOA03F-g19-6FNHfQ02GRvkCREhKSXGwOsshYiYxOTC2Ob-KsmkvN4ADrBjgtCkhzy0GdePJfEX6IxnkOlUPX_3YyeHEFLpmOewl0XiqSJ_i22WQd77whv-kMnAhfDbrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xkry-9_75Nb0N39al2ULIhqIGBJevx2sbpKJHgxnihqb_9SAoVkGbZE9ziRpW2wOZVjdVJSB3xBGXKBHDmx0VChYTHEavMrOHh9JZ5ho5qkYocyMl_MJYnuF_7RlPgjBzq2ImMavtnBIWlqwe_MzAv1ZWAGJryCXP6Sz_BccmaZaCA4oPAcg8keyvkCilM90oz-4y0CCcWLenBV_4DbqmGyvcB5lCsU5LnqZ6Y6PV_1IQ-hHmQdgVHIwYFN5SDxTUGeIf5Xu0PTPL1RBthN2rixLjg7u4JEKOMLha0wpvnn1B9Q3eS2-yDhE7pPUlm8NdJVSeUXDB4yGfXuk0titOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XaUte3tpdpVvv_i7EvlsqF2MnnSH21rxShHBtwq-042kgRiqQXC1QRuaMvgcTbbccslYtEGt6AqqVqe7WcxJjGKuA1S7AC3KPfJSwlE6Hxc_VRt7V3_m2s-Zz1knFO36Oq1YpCuGrNL57LHgVsAvnk_WFOPrZz6FTH1PaBmjafKYmcXOczn2mXnFQONjBBvcr-o7YsHUH5go7kKsc-kvkCqyzLpJjKUsICWpp_ILaloi0gEBfXIuLHT2nJ7uSd5W6XWeJlbyxiCHC0p2LyceuubQ8Ck4Q7JA3HOO2pxET94wKtAr8rKP5CxhGHSi96OhgbO8x6PSIO0srJJsQkZSHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🚀
آپدیت بزرگ تلگرام با ویژگی‌های بی‌نظیر منتشر شد!
تلگرام به‌تازگی یک به‌روزرسانی عظیم دریافت کرده که قابلیت‌های کاملاً جدیدی را به این پیام‌رسان اضافه می‌کند.
✨
ویژگی‌های این آپدیت:
🌐
بخش «انجمن‌ها» (Communities):
فضایی جدید و یکپارچه برای تجمیع کانال‌ها، چت‌ها و ربات‌ها در یک مکان واحد.
📝
ویرایشگر پیشرفته پیام‌ها:
ادیتور متن تلگرام دگرگون شده و اکنون از ابزارهایی مانند
جداول
،
چک‌لیست‌ها
و
عنوان‌بندی (Headings)
پشتیبانی می‌کند.
🤖
تولید محتوا با هوش مصنوعی:
از این پس هوش مصنوعی می‌تواند مستقیماً بر اساس درخواست شما، پست‌های آماده و کامل ایجاد کند.
🕵️‍♂️
پیام‌های خصوصی مخفی:
ربات‌ها قابلیتی پیدا کرده‌اند که می‌توانند پیام‌های خصوصی ارسال کنند؛ به‌طوری که این پیام‌ها حتی از دید مدیران چت نیز کاملاً پنهان می‌ماند.
🧪
نکته:
این به‌روزرسانی به‌صورت تدریجی در حال انتشار است، بنابراین ممکن است این ویژگی‌های جدید هنوز برای همه کاربران فعال نشده باشد و دسترسی به آن‌ها کمی زمان ببرد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6967" target="_blank">📅 19:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6966">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndNwAN7IUSeC05KlXrojtyNB4i35KL905DnonfaGQS9i6wAurvUiyk-SMArN4u68Ye1AvxDWa2EIg3BEvSRC2RzipKLgOA8rwAKiS3I7xFOVmliJyXEsc24B4G89Qaawdn70aw-c_BPKDTpuwpFbi2miXQVKGG9cmiOgO1_u65KDiP2jvQepb3KdgfRj5_7ep3gKpdB4QsyYQE3PO9nfmZVW0zCimud2UK4h-xY6MdnC6L4RL5QRrwF6IYJ_DOIhVWhfSO2n9ehJl0FahKKBbfwy855kSpt65Wgwxup8JNEqpTcEnPnxXAiixF0mSopSfnmR2nYxdxD_TwfwDgLxSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
Acode
یک IDE تمام‌عیار و ویرایشگر کد بسیار پیشرفته (Open-Source) برای اندروید! با این اپلیکیشن می‌توانید پروژه‌های برنامه‌نویسی خود را با امکاناتی در سطح دسکتاپ، مستقیماً روی موبایل یا تبلت مدیریت و توسعه دهید.
✨
ویژگی‌ها:
🎨
پشتیبانی وسیع:
رنگ‌بندی سینتکس برای
+۱۰۰ زبان
و پیش‌نمایش زنده (Live Preview) وب.
🛠
ابزارهای حرفه‌ای:
اتصال مستقیم به
GitHub
، مدیریت سرور با
FTP/SFTP
و کنسول داخلی JS.
⚡️
قدرت و سرعت:
اجرای روان فایل‌های سنگین (بیش از ۵۰,۰۰۰ خط کد!) و پشتیبانی از کلیدهای میانبر کیبورد.
🧩
شخصی‌سازی عالی:
سیستم پلاگین‌پذیر (دارای افزونه‌های هوش‌مصنوعی)، سازگاری کامل با تبلت و
منوی فارسی
.
🧪
نکته:
این برنامه با مجوز MIT منتشر شده و دارای قابلیت بازیابی فایل‌ها (File Recovery) برای جلوگیری از پاک شدن ناگهانی اطلاعات است. (اجرای آخرین نسخه نیازمند اندروید ۸.۰ به بالا می‌باشد).
📥
دانلود از Google Play ،
F-Droid
و GitHub
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️
⭐️
Cyru55</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/6966" target="_blank">📅 17:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6965">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLss4m9lIb0xOtN25mMYlipJfk3fl7QiRN1jxjJKEuZsgsrCU3R-EgOUCoKhqko6PgWHLwbr06OZ_mI08v3xZzkAGaNTfvPdtipeRawgohhrlIraJrkeeONF-xpUBLXRv8KtPpnm67l8pHpK0RRtr92vJ-9EGlibK60TfoLEsj0Hn_PuOmBHfngdES0c9WNxFP8UPg5I2wfwLUGR0FRM5cTorZn-rnsArMgbH3xgA9fLXHLlG1Tx_aX4iT-VS_0gsyOSrHbzZQ3czsl4FIpJZE42Zjgft_SqCRiq8l6rud-RohxeixTMCWi0-FSL8XozqBKTdx-lg2s74Y2iTOEAYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
وقتی هوش مصنوعی علیه هوش مصنوعی رقابت می‌کند!
در یکی از آزمایش‌های جالب روی مدل‌های
Sol
و
Terra
، رفتارهای غیرمنتظره‌ای مشاهده شد.
🔹
کارتل قیمتی
مدل
Terra
پیشنهاد داد قیمت‌ها را با هماهنگی افزایش دهند، اما
Sol
پس از پذیرفتن پیشنهاد، آن را گزارش کرد و حتی خواستار حذف Terra شد.
🔹
اتهام به رقیب
مدل
Terra
در مرحله‌ای دیگر، برای حذف
Sol
او را به تقلب متهم کرد.
🔹
رقابت بر سر درآمد
مدل
Terra
با کاهش جزئی قیمت‌ها نسبت به
Sol
، مشتریان بیشتری جذب کرد و درآمد بالاتری به دست آورد.
📌
این آزمایش نشان می‌دهد که مدل‌های هوش مصنوعی در سناریوهای رقابتی، گاهی رفتارهایی شبیه رقابت‌های دنیای واقعی از خود نشان می‌دهند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/6965" target="_blank">📅 17:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6964">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚀
مدل بی‌نظیر GLM 5.2 به نرم‌افزار Trae اضافه شده؛ کاملاً رایگان و نامحدود!
اگر اهل کدنویسی و دنیای هوش مصنوعی هستید، احتمالاً با
Trae
آشنایی دارید؛ یه ابزار و دستیار فوق‌العاده هوشمند (Coding Agent) که کارش راحت کردن زندگی برنامه‌نویس‌هاست. حالا خبر جدید و جذاب اینه که مدل پرقدرت
GLM 5.2
به این پلتفرم اضافه شده و می‌تونید کاملاً رایگان و بدون محدودیت ازش استفاده کنید.
🤓
من خودم هنوز این مدل جدید رو فرصت نکردم تست کنم ولی Trae کلاً سیاستش اینه که مدل‌های خوب رو رایگان ارائه میده، اما قبلاً یه
صف انتظار طولانی و رو‌مخی
داشت که آدم رو کلافه می‌کرد. نمیدونم واسه این مدل جدید هم همون بساط صف برقرار باشه یا نه!
🌐
لینک سایتش:
🔗
https://work.trae.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/6964" target="_blank">📅 17:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6963">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏
🎙
Voicetypr
ابزار متن‌باز و قدرتمند برای تبدیل گفتار به متن به کمک هوش مصنوعی. جایگزینی عالی برای تایپ صوتی که در پس‌زمینه سیستم‌عامل اجرا شده و همه‌جا در دسترس شماست!
✨
ویژگی‌ها:
*
🔸
تایپ سراسری (System-wide):
با فشردن یک کلید میانبر، در هر نرم‌افزاری (ادیتور کد، تلگرام، مرورگر و...) صحبت کنید تا متن بلافاصله همان‌جا تایپ شود.
*
🔸
آفلاین و امن:
پردازش کامل صدا روی سیستم خودتان (Local) به کمک مدل‌های Whisper بدون نیاز به اینترنت (پشتیبانی از +۹۹ زبان از جمله فارسی).
*
🔸
سبک و فوق‌سریع:
توسعه‌یافته با زبان Rust و فریم‌ورک Tauri با پشتیبانی کامل از پردازشگر گرافیکی (GPU در ویندوز و Metal در مک).
*
🔸
ویرایش هوشمند متن:
قابلیت اتصال به API مدل‌هایی مثل Groq یا Gemini برای اصلاح لحن، یا تبدیل صحبت‌های پراکنده به ایمیل رسمی و کامیت.
🧪
نکته:
این برنامه برای ویندوز و مک در دسترس است. در اولین اجرا، به حدود ۳ تا ۴ گیگابایت فضای خالی برای دانلود مدل پردازش محلی نیاز دارید و پس از آن کاملاً مستقل کار می‌کند (برای لغو سریع فرآیند ضبط، کافیست دوبار کلید
Esc
را بزنید).
📥
دانلود از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/6963" target="_blank">📅 16:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6962">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUadx7KDTcvUQiGQeGD4AK1S1o0ttjZ5go9dFYHILWhlIwbv6mPZ0RcniEAEVgDgwYD71PgPnchDaXmG1_yyzmryWZv-UfnUsn28Ww70_5D_1BIBqrcARJpMQFPJT2LE8C2IVIoijAeq4RGLfeTip9DGiASnma20y0Ly4SA_-IX3Ex3Os5qJNt7O3QIYloVVZvhcN7r7fv62sPR4eBxufQWjYv-yYePATBYr3d7Ev9oU7hlOEtRaaTuqcoMXqJ8iGbTj0xCafqXl1h0K7_pJrt7nmkysfUgGNkN4GEXgLGc7Ft2zEAlaxZ3593xYqaUsQFKjqRc4WT1EDi9Ve0U9rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
TelegramOS
پلتفرمی یکپارچه که تلگرام را به یک سیستم‌عامل کامل برای کسب‌وکار شما تبدیل می‌کند؛ تمام ابزارهای مدیریت، پشتیبانی و توسعه در یک داشبورد جامع!
✨
ویژگی‌ها:
🔸
مدیریت متمرکز تیمی:
کنترل همزمان چند اکانت، صندوق پیام مشترک (Shared Inbox) و مدیریت سطح دسترسی اعضا.
🔸
اتوماسیون و CRM:
ساخت سناریوهای کاری (Workflows)، سیستم پاسخگویی خودکار و مدیریت پیشرفته ارتباط با مشتریان.
🔸
آنالیتیکس و مارکتینگ:
ارائه گزارش‌های دقیق از عملکرد، تحلیل کمپین‌ها و دسترسی به مارکت‌پلیس داخلی.
🧪
نکته:
این پلتفرم بهترین گزینه برای تیم‌های پشتیبانی، فروش و بازاریابی است که می‌خواهند تلگرام را به قطب اصلی و خودکار فعالیت‌های تجاری خود تبدیل کنند.
🔗
وب‌سایت رسمی TelegramOS
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/6962" target="_blank">📅 16:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6961">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0feee0c240.mp4?token=YIvmwuIRfykqHRk92-wI3bBsHL-lPjLQelbcJyi7WthjjhsMNaeD3IJ1HIuIGX6KWxTbLkdyq8F7SKvYqCKiVUNPM058mXF3zfQ8JT7Fk_ROQ-MHVhnF6EaIRVN0auxGIX-cVtp49Q-JRgw4ff3FN_mQSbmG96zR-F9EjiYUCds3lwWX0FrCElVAlmYGx4uz5-qTPjlnNZWx7MfxIUWZEpzX_21gkpdDpC1DW0f0jyGqC62b5lK5Yg_5FLZsrsPNe9jf0s5POtsYoSt3_KujT7BfiIz5udzYYNI3SZJ23HScAEDSEwBkrxd_07crxW4oMqTk4gPiXfCD5Pkmq-vsmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0feee0c240.mp4?token=YIvmwuIRfykqHRk92-wI3bBsHL-lPjLQelbcJyi7WthjjhsMNaeD3IJ1HIuIGX6KWxTbLkdyq8F7SKvYqCKiVUNPM058mXF3zfQ8JT7Fk_ROQ-MHVhnF6EaIRVN0auxGIX-cVtp49Q-JRgw4ff3FN_mQSbmG96zR-F9EjiYUCds3lwWX0FrCElVAlmYGx4uz5-qTPjlnNZWx7MfxIUWZEpzX_21gkpdDpC1DW0f0jyGqC62b5lK5Yg_5FLZsrsPNe9jf0s5POtsYoSt3_KujT7BfiIz5udzYYNI3SZJ23HScAEDSEwBkrxd_07crxW4oMqTk4gPiXfCD5Pkmq-vsmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
با یک کلیک، طراحی هر وب‌سایتی را کپی کنید!
یک ابزار فوق‌العاده به نام Ditto می‌تواند در چند ثانیه، سیستم طراحی هر وب‌سایت را استخراج کند.
✨
امکانات Ditto:
🔍
فقط کافی است لینک سایت را وارد کنید؛ Ditto آن را تحلیل کرده و نسخه‌ای بسیار دقیق از سبک طراحی‌اش را آماده می‌کند.
🎨
تمام توکن‌های طراحی را به‌صورت خودکار استخراج می‌کند؛ از جمله رنگ‌ها، فونت‌ها، اندازه‌ها، فاصله‌ها، سایه‌ها، گریدها و سایر جزئیات بصری.
📄
یک فایل
DESIGN.md
تولید می‌کند که می‌توانید مستقیماً در Claude، ChatGPT، Cursor، v0 و سایر ابزارهای هوش مصنوعی استفاده کنید.
✨
بدون نیاز به کار دستی، ساختار و سبک طراحی سایت را بازسازی می‌کند.
🔄
حتی می‌توانید سبک چند سایت را با هم ترکیب کنید؛ مثلاً رنگ‌بندی و انیمیشن‌های یک سایت را با تایپوگرافی سایت دیگری ادغام کنید.
👀
نتیجه را بلافاصله پس از تولید مشاهده و در صورت نیاز ویرایش کنید.
📦
امکان خروجی گرفتن برای Figma، کامپوننت‌های React، تنظیمات Tailwind، Storybook، WordPress/Elementor و متغیرهای CSS را نیز دارد.
https://www.ditto.site/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/6961" target="_blank">📅 14:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6960">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">موتور جستجوی مبتنی بر شبکه DHT بیت‌تورنت، که امکان جستجو و یافتن منابع تورنت و لینک‌های مگنتی رو فراهم میکنه
☠
http://cilimo.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/6960" target="_blank">📅 14:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6959">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPtd4n2pIHKnKfF0aA3TMrr92i-NtrgSO6u0gykUiDDVy5o2zIdRs3pJD6i4ayrOSdZc8X7mu46MV7cfI-9FM4ajtvAE9S4DTgnIwwRCOC13NpPMnXHl0HJdJeOWpc-OeuEGBSDWA18X0LLaWVVC1t-W1t-i4BQibCLJpLNU2OJXAXNRmiZI6m24TasKAdcAbDmcVbVs3tqb0gnDdrdGak4DX0KZqtg2kDbT2haUxqWPY02h78DqaaN7G6IS4Dzho-0RKSG9d-bwk05eAIFyqbcSYvBdc-DbDUu5enPbQMCC5UYqlZ6FxDJQ77Acu-TI6iypuen1sHzALvDz2xbFRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🌐
Magnitude Browser Agent
دستیار هوش مصنوعی قدرتمندی که با استفاده از بینایی ماشین (Vision AI) به شما اجازه می‌دهد مرورگر وب را فقط با دستورات متنی ساده کنترل و اتوماتیک کنید!
✨
ویژگی‌ها:
*
👁
معماری بینایی‌محور: برخلاف ابزارهای قدیمی که به کدهای سایت (DOM) وابسته‌اند، این ابزار صفحه وب را مثل یک انسان می‌بیند و با مختصات پیکسلی کار می‌کند.
*
🖱
تعامل و اتوماسیون کامل: کلیک، تایپ، و جابه‌جایی المان‌ها (Drag & Drop) در پیچیده‌ترین سایت‌ها.
*
📊
استخراج هوشمند دیتا: توانایی خواندن و استخراج داده‌های ساختاریافته (بر اساس Zod Schema) مستقیماً از روی ظاهر سایت.
*
✅
تست‌رانر داخلی: ابزاری فوق‌العاده برای تست خودکار وب‌اپلیکیشن‌ها با بررسی و تأییدیه بصری (Visual Assertions).
🧪
نکته: این پروژه در بنچمارک WebVoyager امتیاز خیره‌کننده ۹۴٪ را کسب کرده است. برای بهترین عملکرد، به یک مدل بینایی قدرتمند مثل Claude 3.5 Sonnet یا Qwen-2.5VL 72B نیاز دارید. نصب اولیه به سادگی با دستور npx create-magnitude-app در ترمینال انجام می‌شود.
📥
دانلود از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6959" target="_blank">📅 12:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6958">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNfnPbp3yXIv46lF-SrFwLbLpT7XwNzRvBrgSmngGKOvwk42VQp74R3oKBEQDTiPcFYli1TUzKJ5x-iG5rJNmcmEhSxjOahvbw3tapExBz4gHv6gU3FLZlX0Fj_I7PIZyuKcV9Z_4ZXwSMHfmFkxXbN6hIOxnpvozAsVgfWUm8EZ8YnGaoZlRMiV2RYXSYG0Xx9Dljl513GRHAwQfPowrUosrhurCqzYpEHYXTkl6cxT_4bhZvtQiDCs2bcHupxaVcKlUyZqIa0RhELw_BqsslvrQo8O5be2MH_uFBk1ga1UyMJx8sRlwdY2ApOrNBY6Sab0TUKgW4wBHDSgux2daQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار چندمنظوره رایگان برای ویرایش صدا، عکس و ویدیو
سرویس
Magic Hour
مجموعه‌ای از ابزارها و فناوری‌های هوش مصنوعی کاربردی را برای انجام هر نوع وظیفه‌ای گرد هم آورده است:
🔹
تولید تصاویر، حذف پس‌زمینه و افزایش کیفیت تصاویر؛
🔹
ویرایشگر دیپ‌فیک با قابلیت
جایگزینی افراد در ویدیو
؛
🔹
بازسازی عکس‌های سیاه و سفید + جایگزینی افراد در تصویر؛
🔹
مجموعه‌ای از ابزارها برای کار با موسیقی و فایل‌های صوتی؛
🔹
تولیدکننده زیرنویس.
🌐
magichour.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/6958" target="_blank">📅 11:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6957">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">۱۰۰ گیگ کانفیگ اهدایی
🔥
vless://63dc39fe-3bc3-4267-8bf1-4069b47baa18@194.110.172.150:443?encryption=none&fp=chrome&pbk=3sRLbKljY5s7LCik-w9MqgenayhgHgLV0v9lmFGQ9TQ&security=reality&sid=3094219d2cfd2b3d&sni=www.samsung.com&type=tcp#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/ArchiveTell/6957" target="_blank">📅 11:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6956">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏
🤖
3xui-telegram-bot
ربات قدرتمند و متن‌باز تلگرام برای فروش خودکار سرویس VPN، با اتصال مستقیم به پنل 3X-UI. با این ابزار تمام فرآیندهای فروش، تمدید و مدیریت اکانت‌ها بدون نیاز به دخالت دستی ادمین انجام می‌شود!
✨
ویژگی‌ها:
🛍
فروش خودکار سرویس با حجم دلخواه، شارژ کیف پول (کارت‌به‌کارت) و پشتیبانی از چند سرور (Inbound)
🎁
مجهز به سیستم ساخت کد تخفیف، ارائه تست رایگان و زیرمجموعه‌گیری (Referral)
💻
دارای ابزار اختصاصی خط‌فرمان (vpn-bot) برای نصب سریع یک‌خطی، بکاپ‌گیری و آپدیت
🔐
اتصال کاملاً امن به پنل صرفاً از طریق API Token (بدون نیاز به یوزرنیم و پسورد پنل)
🧪
نکته:
مدیریت کامل ربات اعم از تغییر قیمت‌ها، تایید یا رد پرداخت‌ها، و مشاهده آمار، مستقیماً از طریق دستورات داخل تلگرام توسط ادمین انجام می‌شود. همچنین برای سرورهای ایران، امکان تنظیم پروکسی SOCKS5 نیز تعبیه شده است.
📥
دانلود و آموزش نصب در گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/6956" target="_blank">📅 11:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6954">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRlsInlFkVl8vzAYD00MFtD1aq8tchcLKcITv5kSZs-0Wpm4WQ6HIbZ_YFZcSBh6yBokd36KQXb_Px-xzLNV4Q87niz92iBhyG1l8VhhGOv3WcjTP04i6DTEIWoNgjChvnLIqY_A4k3qZxXtXZAxs3EAoVrMYWlaN_dPfkQ_qQvAa7otPrcyDmBu_vWCaFuapUyRwNWMX2h0hXE2EM4fcd7IraOxWQAAJ_xBOnWCM3uvx1OjC-axP-J5kIUXHCwkfRS8bNkc3nvJGJAL0Q4S9GGd0pONKxXfdbZZweVwJoTJFRrVC5l5FnEW7elAG7r-9McGU6FDMptaEzysK0h58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🌐
BrowserOS & BrowserClaw
دو مرورگر متن‌باز؛ یکی برای شما، یکی برای هوش مصنوعی!
✨
ویژگی‌ها:
‏
🤖
BrowserClaw:
اتصال کلاینت‌های AI (مثل Cursor) برای انجام خودکار کارها روی اکانت‌های واقعی شما.
‏
🧑‍💻
BrowserOS:
مرورگر امن با دستیار AI داخلی و پشتیبانی از مدل‌های لوکال (Ollama).
🎥
ضبط ویدیویی تمام اقدامات هوش مصنوعی برای بازبینی.
🧪
نکته:
هوش مصنوعی در تب‌های کاملاً ایزوله کار می‌کند و هیچ تداخلی با وب‌گردی شما ندارد.
📥
دانلود از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/6954" target="_blank">📅 10:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6953">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏
🚨
حذف ناگهانی دامنه
t.me
از DNS جهانی!
دامنه
t.me
(هسته اصلی زیرساخت لینک‌های تلگرام) به طور ناگهانی از سیستم DNS جهانی ناپدید شد! رجیستریِ پسوند
.me
وضعیت این دامنه را روی
serverHold
قرار داده که باعث شده هیچ‌کدام از لینک‌های تلگرامی در سراسر جهان در مرورگرها باز نشوند.
✨
جزئیات ماجرا:
*
📱
اپلیکیشن‌های موبایل و دسکتاپ تلگرام همچنان بدون مشکل کار می‌کنند و این قطعی صرفاً مربوط به لینک‌های وب (آدرس کانال‌ها، گروه‌ها و ربات‌ها) است.
*
💎
ضربه سنگین به اکوسیستم کریپتویی تلگرام و مختل شدن دسترسی کاربران به کیف‌پول داخلی (Wallet) و مینی‌اپ‌های مرتبط با شبکه TON.
*
🌐
دامنه موازی
telegram.me
همچنان فعال است؛ این یعنی محدودیت منحصراً روی آدرس کوتاه
t.me
اعمال شده و کل زون دامنه‌ها مشکلی ندارد.
🧪
نکته:
با اینکه اعتبار این دامنه تا سال ۲۰۳۵ تمدید شده، اما رجیستری کشور مونته‌نگرو (صاحب دامنه‌های .me) بدون هیچ اخطار قبلی آن را از دسترس خارج کرده است (پاول دورف در پلتفرم X مستقیماً از آن‌ها خواسته مشکل را حل کنند). این اتفاق زنگ خطری جدی برای شرکت‌هایی است که زیرساخت حیاتی خدماتشان را روی دامنه‌های ملی بنا کرده‌اند!
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/6953" target="_blank">📅 10:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6952">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fgw86OjJmsO1eL-DR87VEDq1R0SOvahITijLHpZtKc7_Kp9wVh51bYOIG4yMh3m8U-0NftoOyloEUK5-F22x2hcvtw1NgHJmnJsvtLly60ym7Gkh6oIDfbVWAm7jSiueVscnwiFvtsK50vnCl_oUYl0MjXMKCAphIqqNFMYktR1tDHCrVWZ79lZOki_HQTYdf5iHioLVlwX_H-hc2G8w0l2h7AkHFaCCRI2VQfxu2s4jhQAiLYjQPt5r2M_mV44kIeeEbR5a-az34-bEutZ8dkT8Vadbv0aM8lDUdJE1YVJDqD0_AMu9ovwKZJG-4tJoQRTXn1vZpl9qnab4TG-6jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛ Google AI Studio حالا به GitHub وصل
میشه
🔥
با قابلیت جدید Import from GitHub میتونید ریپازیتوری‌های خودتون رو مستقیم وارد Google AI Studio کنید و با کمک Gemini روی کدهای موجود کار کنید.
✨
امکانات جدید:
•
📂
وارد کردن پروژه از GitHub
•
🤖
سازگارسازی خودکار کد برای اجرا
•
✏️
ویرایش و ادامه توسعه پروژه
•
👀
پیش‌نمایش و Deploy سریع‌تر
⚠️
فعلاً اتصال یک‌طرفه است و تغییرات به GitHub برنمی‌گرده؛ اما همگام‌سازی کامل در حال توسعه است.
https://aistudio.google.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/6952" target="_blank">📅 09:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6951">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSJDYrikGkIv9vvt71uonQ-hFLmvAQMHJ6MNzsUyWi4voH7boF39U_ZoVWjLOixpwxNh5Ie7O1fXjhSokub1blb7xMVfiNlj-2sacr4P87a-VJj_SLZZkL76l1qc_oFx2Zr-GktYYcPDNa3WWs528VTFOYesCldsvBcg51WjTHH9lTZvmTf-zdHv8WydW_rL0N4RUA-Yup5ywey42AMo-Pg_vNlT2BJ_DvsbMtR8H5Np467JWd7mJM8wqq88kfo45VN2P9PSJsTZXTUVGah3pBvT-uykHDURwRexlQzBZbZvqiKwKoD9RKrmpEjliXKXWgSMYwNXb1CR527fTEeNxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📝
بیش از ۳۹۰۰ پرامپت آماده در ۱۶ دسته‌بندی مختلف، از جمله:
• تولید محتوا و نویسندگی
• برنامه‌نویسی
• بازاریابی
• طراحی و تولید تصویر
• آموزش، کسب‌وکار و...
https://xueprompt.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/6951" target="_blank">📅 08:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6950">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184a52dda.mp4?token=T_hItQ3O7YDA2qkKNW7XMD0lv2fZys8NBW6KbBvsfHSIAYgLNLGrwzkHKl4knKaK1fkupJ7aX7H6j831RXG11MAdy9BhxmRpMWb_V8h4eDU5zz1FnAB1y5EmnpRgEqz6zrOhgSMJvVbYVKV4QK92DDDeIdaawiA6wmbdY16OQ1uUEQBFDoZd5J9GeymCkA57lDJDORiPdYTZRfRfThDOvZX20byr-U5l0XY7P181B8oOXtdIzT-dHM5m8uWqbyHoiLaCVarm3LcJkhHuINZAuCDCqLF3NikDnUyuuaANgZUpw3X8RzrmAIfNIO8q6819EcSeR5_hveflBmaRfs-Wfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184a52dda.mp4?token=T_hItQ3O7YDA2qkKNW7XMD0lv2fZys8NBW6KbBvsfHSIAYgLNLGrwzkHKl4knKaK1fkupJ7aX7H6j831RXG11MAdy9BhxmRpMWb_V8h4eDU5zz1FnAB1y5EmnpRgEqz6zrOhgSMJvVbYVKV4QK92DDDeIdaawiA6wmbdY16OQ1uUEQBFDoZd5J9GeymCkA57lDJDORiPdYTZRfRfThDOvZX20byr-U5l0XY7P181B8oOXtdIzT-dHM5m8uWqbyHoiLaCVarm3LcJkhHuINZAuCDCqLF3NikDnUyuuaANgZUpw3X8RzrmAIfNIO8q6819EcSeR5_hveflBmaRfs-Wfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧰
۳۰۰+ ابزار رایگان، فقط در یک سایت!
📄
ویرایش، ادغام و فشرده‌سازی PDF
🎬
برش و ادغام ویدئو
✍️
ابزارهای متن و نگارش
💻
ابزارهای کاربردی برنامه‌نویسی
🔑
ساخت QR Code، رمز عبور و داده‌های تصادفی
💰
ابزارهای مالی و محاسباتی
https://footrue.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6950" target="_blank">📅 08:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6949">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">📶
دسترسی به لیست سرورهای عمومی VPN
مجموعه‌ای از کانفیگ‌های
V2Ray
،
Trojan
و
Outline
VPN
که سرورهای جدید و سالم به‌صورت مداوم به لیست آن اضافه می‌شوند
🤔
🔗
نیازی به کپی تک‌تک سرورها نیست؛ فقط
Subscription Link
مشخص‌شده را کپی کرده و مستقیم داخل کلاینت خود وارد کنید.
V2Nodes
🌟
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6949" target="_blank">📅 01:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6947">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">برای احتیاط ام شده برنامه های ضروری رو آپدیت کنین که خیره
🌑
Slipnet
📂
WhiteDns
📂
Resolver
📂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6947" target="_blank">📅 01:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6946">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSyqAKaoXfO83PX5I7eIQ4yjiL9FhgSML18BUzpP2VfjJUUb7pqinBe_A2x04HUQZuvr57JL4fBhEIjcmGRSXss0s00PC4SG9YD9H8gwALMKsHSd5e0dkZVEeuaeb6RqgIdNh-9_xUYNEUgcOb4jDTQzThhisEXR_d_iMTkrsEDrqg5CtzHEWJ9N27shU2bq5C1Tq_L9seBZXqu76cMIN9K55EIKtV8q0KXteX4srm-YRnzup69EzNGSEnpWzXcrlpqW-QfnytSUcdFG-ft-R9nHm1dMnT8whfhBQ6ZORcJpPjEDE-xdEqsl9g1wIo5WKL3BwJYHEZu38URO6f-j1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🖼
Image-to-Text OCR
ابزار تحت وب و متن‌باز ساده و کاربردی برای استخراج سریع متن از داخل تصاویر به کمک تکنولوژی OCR (ایده‌آل برای تبدیل عکسِ اسناد و نوشته‌ها به متن دیجیتال قابل ویرایش).
✨
ویژگی‌ها:
🔸
استخراج دقیق و سریع متن از هر نوع تصویر
🔸
توسعه‌یافته بر پایه تکنولوژی‌های مدرن Vue و Nuxt3 و TypeScript
🔸
رابط کاربری تحت وب، بسیار سبک و بدون نیاز به نصب نرم‌افزارهای سنگین
🔸
کاملاً متن‌باز (Open-Source) با لایسنس AGPL-3.0
🧪
نکته:
برای راه‌اندازی این پروژه روی سیستم خودتان (لوکال)، پس از کلون کردن ریپازیتوری کافیست دستور pnpm dev را اجرا کنید تا برنامه روی پورت 3000 در دسترس قرار گیرد (بیلد نهایی نیز با pnpm build در پوشه dist ساخته می‌شود).
📥
دانلود سورس‌کد از گیت‌هاب
⭐️
حمایت از پروژه: ستاره (Star) در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/6946" target="_blank">📅 23:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6945">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏
🤖
آموزش کامل و به‌روز راه‌اندازی NipoVPN
این ابزار با پنهان‌سازی ترافیک واقعی داخل درخواست‌های جعلی (Decoy/Fake HTTP requests)، به‌راحتی از سد فیلترینگ پیشرفته عبور می‌کند.
⚙️
۱. نصب روی سرور (VPS)
به سرور اوبونتو یا لینوکسی خود متصل شده و نسخه جدید را نصب کنید:
Bash
wget https://github.com/MortezaBashsiz/nipovpn/releases/latest/download/nipovpn.deb
sudo apt install ./nipovpn.deb
📂
۲. ایجاد مسیر لاگ‌ها
Bash
sudo mkdir -p /var/log/nipovpn/
sudo touch /var/log/nipovpn/nipovpn.log
📝
۳. ویرایش فایل کانفیگ
فایل
/etc/nipovpn/config.yaml
را با ویرایشگر باز کرده و مقادیر زیر را به دقت تنظیم کنید:
tlsEnable:
برای امنیت حداکثری این گزینه را روی
true
نگه دارید و پورت را
443
تنظیم کنید. (امکان استفاده از پورت 80 و HTTP معمولی هم وجود دارد).
fakeUrls:
چند سایت معتبر و بدون فیلتر (مثل
google.com
) اضافه کنید.
token:
یک رمز امن و طولانی (حداقل ۳۲ کاراکتر) برای ارتباط کلاینت و سرور بسازید.
🚀
۴. تنظیم فایروال و استارت سرویس
ابتدا پورت انتخابی (مثلاً 443) را در فایروال باز کنید:
Bash
sudo ufw allow 443/tcp
سپس سرویس را فعال و ری‌استارت کنید (بعد از هر تغییر در کانفیگ، ری‌استارت الزامی است):
Bash
sudo systemctl enable nipovpn-server.service
sudo systemctl restart nipovpn-server.service
جهت بررسی لحظه‌ای لاگ‌ها و اطمینان از اجرای بدون خطا:
Bash
tail -f /var/log/nipovpn/nipovpn.log
📱
۵. تنظیمات کلاینت (گوشی)
کلاینت رسمی
NipoVPN Android
(در گیت‌هاب) یا اپلیکیشن
سیمرغ (SIMORGH)
را نصب کرده و اطلاعات آی‌پی سرور، پورت (443)، توکن و آدرس جعلی (Fake URL) را دقیقاً مطابق سرور وارد کنید. کلاینت اندروید بسیار بهینه است.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6945" target="_blank">📅 22:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6943">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏
🚀
SulgX Panel
پنل مدیریت اشتراک VLESS فوق‌سبک و شخصی، ساخته شده تماماً با پایتون (FastAPI و SQLite).
✨
ویژگی‌ها:
🛡
مدیریت کامل کانفیگ‌های VLESS (WS+TLS) با پشتیبانی از Fragment و SNI اختصاصی
📊
مانیتورینگ زنده مصرف ترافیک، محدودیت حجم و زمان انقضا برای هر کاربر
☁️
بهینه‌سازی شده برای استقرار (Deploy) رایگان و ساده روی پلتفرم‌هایی مثل Render و Railway
🤖
دارای ربات تلگرام هوشمند دو زبانه و سیستم ضد-خواب (Anti-Sleep) سرور
🧪
نکته:
این پنل کاملاً رایگان و اوپن‌سورس است و به راحتی از طریق فورک گیت‌هاب و Dockerfile قابل راه‌اندازی است.
📥
دانلود از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6943" target="_blank">📅 18:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6942">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">archive-scanner_v1.0.4.apk</div>
  <div class="tg-doc-extra">10.4 MB</div>
</div>
<a href="https://t.me/ArchiveTell/6942" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اسکنر آیپی تمیز کلودفلر آخرین اپدیت
دوستانی که نسخه قبلی رو داشتن هم میتونن از تو برنامه آپدیت کنن هم با این فایل
سرعت اسکن خیلی بالایی داره، دقتش بالاست و ui کاملا ساده و سریعی داره
🔎
Findings:
❌
Detection: 0
⚠️
Suspicion: 0
✅
Not detected: 67
• File name:
archive-scanner_v1.0.4.apk
• File format:
Android
• File size:
10.43 MB
•
VirusTotal link
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/6942" target="_blank">📅 17:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6939">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fv94z4EwzjaiTkGjh_wFVE9Sbeg1OPk0P2Xo8vZ2NMTRx0iNvsWBtp8IvR2wVWGk0dYOyHg9ruGnLAGDjlQ0iZ90KohUw2d_UtvpyRPtuvvv7-QlfDxjuiIcCQ2-UUSJ09cmZWtzDy64QeO351CaWJzOjGc3bI7jUe1YzQDPYNGZzr42NSfQ9c4q2CKIMk0AUDxpCoLKaZFtaev_mv3EaHnf_z1P5_38Hx6k3U1tv4ZtX-tqk61GLPdJAX-I2DiOM6as-xuDeYm3KurscZBsXl69MfO-a50tKmbQXRXTNheKIJkzrEYkZM7eITpUaH7yMeCee06_KSjdmnrupf-Nmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n8NGz5sy3JUov7s6upGjcmLcOsnbGVeclhj5b3Zdhv3RiUg5qPUmOVBHHNIFXDvtZq2zetVYuznJJ31d5zzFBuBeAglqYBp8jNu89Gf6v5KmUj-2UkfnRcuUNywYZlqDYd2JIC1KUUQboQjeh4I7PDSS0_6lcmbTVmuxOfQORepO7BGak_WFNxzGNtr-k4WP5GkDYQk-TBNaL3GFlBP9NJczh8dmhfD7FGivWidpKBIjFpqsp12jPsq2mu_RnqORt48WwoRHJPsPVgQstkYnmMR-LazINyWxn71Btbs0XUSZVe8d8GG4zj_2jGZ0eJxroLvj0zO6xG2ujGyQ5DkdnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oBuG0-q1x_U6wqRjAuF-BAuG6pem96qmPTAN0trItntYNf9tKeRVzbhwml6TvG8FIoj8VjIkCB4r-S9rPOQVbZw5XVqzXO1pLZGJ1we-MEVKkGgQnJ8capo5WZrMrFr3SDv2UMV8_0I_BssNIC-NZA9iY9m0hQer0C_pT_ypof74mW5MzlqDGeXB7D7VCtOGISCmpZhRvmYOuHPfEXtXMAiAWUd-LnwjMHxCqTDEJBZSE018H3FxTcHknM0X9gmepf6224PMFEDl_ru2wSD-TuhrqTMsL-XeIoVBJkPnmDvTzGdhNhXN0yk_Onu2AblVtjhvg8b7GW5muy3svvYNRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
؛Archive Scanner v1.0.3 منتشر شد!  جدیدترین نسخه‌ی Archive Scanner با بهبودهای مهم در دقت، سرعت و امکانات منتشر شده است.
✨
تغییرات مهم:
⚡️
اصلاح کامل تست سرعت دانلود (اندازه‌گیری دقیق‌تر و عبور از فیلترینگ SNI)
📤
اضافه شدن تست سرعت آپلود برای هر IP
🤖
ساخت…</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6939" target="_blank">📅 17:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6938">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">📱
؛NipoVPN Android کلاینت رسمی اندروید برای پروژه NipoVPN؛ یک ابزار پروکسی و ضدسانسور قدرتمند که ترافیک واقعی HTTP/S شما را در دلِ درخواست‌های جعلی (Fake HTTP Requests) پنهان می‌کند.
✨
امکانات:
🧩
توسعه مدرن: برنامه‌نویسی شده به‌صورت کامل با زبان Kotlin و…</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6938" target="_blank">📅 16:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6936">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نت من ترکید
ی اعلام وضعیت کنین</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6936" target="_blank">📅 15:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6935">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏
🔥
ChatGPT Work
اوپن‌آی با معرفی قابلیت انقلابی Work، آینده هوش مصنوعی را تغییر داد. این سیستم دیگر فقط یک چت‌بات ساده نیست، بلکه یک دستیار هوشمند (Agent) است که کارهای پیچیده و چندمرحله‌ای شما را از صفر تا صد، به‌صورت خودکار انجام می‌دهد.
✨
ویژگی‌ها:
🧠
تکیه بر موتور GPT-5.6 و Codex:
ترکیبی بی‌نظیر برای اجرای کارهای سنگین تحلیلی، برنامه‌نویسی و چیدن خروجی‌ها.
📄
خروجی‌های زنده و واقعی:
ساخت مستقیم ابزارهای کاربردی مانند شیت‌های اکسل، اسلایدهای آماده ارائه، اسناد و حتی وب‌سایت‌های تعاملی.
⏰
اتوماسیون و زمان‌بندی:
هندل کردن خودکار وظایف تکراری در زمان‌های مشخص (مثل چک کردن روزانه قیمت‌ها یا خلاصه‌سازی پیام‌های تیم).
🖥
کنترل مستقیم دسکتاپ (Computer Use):
قابلیت تعامل با سیستم دقیقاً مثل یک انسان؛ کلیک کردن، تایپ و جابه‌جایی فایل‌ها برای انجام کارهای پیچیده.
🧪
نکته:
امنیت این سیستم کاملاً تحت کنترل شماست. دسترسی‌ها را خودتان تنظیم می‌کنید و برای اقدامات حساس، سیستم حتماً از شما تاییدیه (Approval) می‌گیرد.
🔗
وب‌سایت رسمی OpenAI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6935" target="_blank">📅 14:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6934">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMRr0rCEU9677QuheeH1rIQp3Oxl9DTfdj_ag-MIK8UnDUJb6Mb_9vd38gn21tY43hfXxy7sRu9WNOF7jBFF8lglH4Rd_RvMOEyf9Ra65sUtxRYbQqgb41oRb7kpUge6FmFodGAoA4-fvR3v5FJ4nTcBtVMLsGIg8-t41fcj3JzYpMd_iz6c-dKFg-0c_jQVI_mO0HWoLVI2FXOEb19NO3yVZIpAHxG79quDw1hbC9ENbb_zDzT9-ylFa_Jw6jnOlVkZSEBOb_YxSA1E8RGoTKljFIZUFXyEKysekPePp3R_ETmcdA1maMu4Jy0Ex431sX9yUyYdDTA0dxPIUK8kWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🕵️
3D Investigation Board
یک برد کارآگاهیِ تعاملی و سه‌بعدی (مبتنی بر GPT-5.6 و Fable 5) که به شما اجازه می‌دهد اطلاعات و سرنخ‌ها را دقیقاً مثل فیلم‌های پلیسی روی یک بورد مجازی مدیریت و تحلیل کنید.
✨
ویژگی‌ها:
📸
امکان اضافه‌کردن انواع شواهد، اسناد، یادداشت‌ها و عکس‌ها روی برد
🧵
اتصال بصری سرنخ‌ها به یکدیگر با نخ‌های سه‌بعدی و فیزیک واقع‌گرایانه
🧠
کشف هوشمند ارتباطات پنهان بین داده‌ها به کمک تحلیلگر هوش مصنوعی
🧪
کاربردها:
این ابزار خلاقانه، نه‌تنها برای حل پرونده‌ها و معماها، بلکه برای داستان‌نویسی، ایده‌پردازی و برنامه‌ریزی پروژه‌های پیچیده فوق‌العاده کاربردی است.
🔗
مشاهده ویدیو و آموزش کامل در X
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6934" target="_blank">📅 13:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6933">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYBAaewRoJm2KYZrodwKPKxK6sPHuPiozp6m_nrrcYmOwJEjMivMp2z9VvKd_QK4NTq_ovbSkgihnmUDUat0I40KEvxj1dsUNEnBxPjdGNNu3wLTMj3I9MqgMKdgE8ibp6ifkQVT9tXgqc3BU6VtgxkFv0Ewohe99HlBov8f2J7sWrdDEljCtWCFD9XSfVObLO1k_cRDgULl22NoQduLYtsVkl7a8vxRJyS1OnNVwm9NvrxsRzs_vLd0S2pP1zPpTJ4wFeB-LZIMKCI2Orn6FpIdkPtmkLsmyRNcCtJGQCJrr3WWmf5dQ-yIfBdV-xB2ascfAaO8TsKrS7EkLq3ozA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🤖
OMG-Agent
کلاینت دسکتاپ متن‌بازی که به هوش مصنوعی اجازه می‌دهد گوشی اندرویدی شما را فقط با دستور متنی کنترل کند! (مثلاً: «تلگرام را باز کن و به
⚡
Bachelor پیام بده»).
✨
ویژگی‌ها:
🧠
پشتیبانی از مدل‌های هوش مصنوعی موبایل (مثل AutoGLM) و APIهای OpenAI
📱
اجرای خودکار دستورات با تحلیل لحظه‌ای صفحه گوشی (از طریق ADB)
💻
سازگار با گوشی‌های فیزیکی اندروید و شبیه‌سازها (Emulators)
🧪
نکته:
پیش‌نیاز این ابزار، نصب ADB، کیبورد ADB و فعال‌سازی USB Debugging روی گوشی است.
📥
دانلود و راه‌اندازی از گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/6933" target="_blank">📅 13:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6932">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏
🚀
۴۰۰۰ دلار کردیت رایگان API
هدیه‌ای ویژه برای برنامه‌نویس‌ها! دسترسی سریع به قدرتمندترین مدل‌های هوش مصنوعی دنیا برای پیشبرد پروژه‌های کدنویسی شما.
✨
ویژگی‌ها:
🧠
پشتیبانی از مدل‌های برتر جهان (GLM 5.2 ،Qwen 3.7 ،Deepseek 4 Pro ،Minimax M3 و Kimi k2.6)
📧
ثبت‌نام سریع و کاملاً بی‌دردسر با هر نوع ایمیل
💻
سازگاری کامل با انواع کلاینت‌ها
🧪
نکته:
مصرف کردیت در این سرویس‌ها با ضرایب بالایی محاسبه می‌شود؛ پس حتماً در استفاده از توکن‌هایتان دقت و مدیریت لازم را داشته باشید.
🔗
لینک ثبت‌نام
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/6932" target="_blank">📅 13:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6931">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNd245u3nV8aKfmjO3qcu3tlh-NsQ8C7iYUYQL7gKg-Uo9-3Mb6k7pHF4VSFLF0xuhfIVmMs5Eips76MhIllu_eRPOAkAzQDePBvOYgFJe8I0fhLb4Pn2cBsYBR7e6biBJvQnN3XHQHLwGERx5cF93MA2M3eoAaAdERmg_TUEDCTPhOi7MGkWR5eoNo-Pc90EbyxU5yXDKEJ6_f79vl8ivU6pCrHoP4Up2Lqovtv8weBTykeeWkYZWie9rS_CdqjLvWbv8SXd6MkTNfyxnHZjnlA1oqbYu-uDfeLKWGavElZ1z04pdhcWQi0vCcdxWsimwJCgRNwc8u28i5tlPIUwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⭕️
Colibri
پروژه قدرتمند و متن‌بازی که با C خالص نوشته شده و اجازه می‌دهد مدل‌های عظیم هوش مصنوعی را تنها با اختصاص ۳٪ از حجم کل مدل به رم (RAM) اجرا کنید!
✨
ویژگی‌ها:
🔸
اجرای کامل تنها با یک فایل C (حاوی ۲۴۰۰ خط کد)
🔸
کاملاً مستقل از پایتون، کتابخانه‌های جانبی و کارت گرافیک (GPU)
🔸
ساخت API لوکال سازگار با OpenAI (تنها با دستور coli serve)
🔸
اجرای مدل سنگین 744B (که در حالت عادی ۷۳۰ گیگابایت رم می‌خواهد) تنها با ۲۵ گیگابایت رم!
🧪
نکته:
برای کاربران ویندوز، استفاده از WSL2 پیشنهاد می‌شود. به عنوان مثال، لود یک مدل ۳۷۰ گیگابایتی تنها ۳۰ ثانیه زمان و ۹.۹ گیگابایت رم نیاز دارد (البته به دلیل عدم استفاده از گرافیک، سرعت پردازش حدود ۱ توکن بر ثانیه خواهد بود).
📥
دانلود از گیت‌هاب
⭐️
حمایت از پروژه: ستاره (Star) در گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/6931" target="_blank">📅 12:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6930">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">📈
؛
Vibe-Trading
دستیار هوش مصنوعی شخصی و متن‌باز برای ترید و تحلیل بازار. کافیست ایده‌هایتان را به زبان ساده بنویسید تا خودش برایتان استراتژی معاملاتی بنویسد و بک‌تست بگیرد!
✨
ویژگی‌ها:
🧠
تبدیل مستقیم پرامپت‌های متنی به کد استراتژی، تحلیل بازار و دریافت بک‌تست‌های دقیق
🐝
تشکیل تیم‌های مجازی هوش مصنوعی (ایجنت‌های ریسک، کریپتو و کوانت) برای مشورت و بررسی همه‌جانبه ایده‌های شما
👥
سیستم جالب Shadow Account: ژورنال معاملاتتان را آپلود کنید تا هوش مصنوعی خطاهای احساسی و رفتاری شما را در ترید پیدا کند
📊
پشتیبانی یکپارچه از بازارهای جهانی (کریپتو، سهام و فارکس) با دریافت خودکار دیتا
🧪
نکته:
این ابزار با پایتون توسعه داده شده و به‌راحتی به API مدل‌های مختلف (از جمله Groq ،DeepSeek و OpenAI) متصل می‌شود. برای دیپلوی روی سرور شخصی یا اجرای لوکال فوق‌العاده است.
📥
دانلود و نصب از گیت‌هاب (PyPI / Docker)
⭐️
حمایت از پروژه: ستاره (Star) در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/6930" target="_blank">📅 12:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6929">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏
🐋
Orca
محیط توسعه و هماهنگ‌کننده (Orchestrator) فوق‌العاده قدرتمند برای مدیریت همزمان چندین ایجنت هوش مصنوعی برنامه‌نویس. یک دستیار همه‌چیزتمام برای توسعه‌دهندگان!
✨
ویژگی‌ها:
🤖
اجرای همزمان ایجنت‌های مختلف (مثل Claude، Codex و Grok) روی یک پرامپت و مقایسه خروجی‌ها
📱
دارای اپلیکیشن موبایل (iOS و اندروید) برای کنترل و هدایت ایجنت‌ها از راه دور
🎨
مرورگر توکار (Design Mode) برای انتخاب المان‌های سایت و ارسال مستقیم HTML/CSS آن به هوش مصنوعی
🔗
اتصال بی‌نقص به گیت‌هاب، پشتیبانی از محیط‌های ریموت (SSH) و ترمینال‌های قدرتمند داخلی
🧪
نکته:
این نرم‌افزار متن‌باز است و تقریباً از هر ایجنت مبتنی بر CLI (مثل Cursor ،Copilot و OpenCode) پشتیبانی می‌کند. کلاینت دسکتاپ آن برای ویندوز، مک و لینوکس کاملاً رایگان در دسترس است.
📥
دانلود از گیت‌هاب (بخش Releases) یا سایت رسمی (onOrca.dev)
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/6929" target="_blank">📅 11:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6928">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sG1ECdETtVsHqmRrhTa1A5Z2p_4-HJL-rDu1gmMWGsDUFKdyJKpAn8mN05beXUi1VknAYu7D_o1wZ5m25EsGSVHIlc-kjaYVS2P3vP35h7xzUd2Ia_UBRA_ikc2OlLAt6-wzCSnKKb_V1U0g1Z7lJlObPSa0a0aP29sAi5ViN4GuCeZh7XFSijkVPxZTCkyTG-Bnqj-zpRPCyLnjkP86Ah3Sk8jcDfLyUiruiNHhdVEhOhYHjweKreOk_ShPHX3DIL2TsLUeA-oabfEZAerSlQ2R10s8EnYIsf3ERXebQGRG97Dd5Sjp0SecVUhbHyNTUxobegPgqzxw70sN-1h62g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
هر عکسی رو به پرامپت تبدیل کن!
؛Convly AI Image-to-Prompt تصویرت رو تحلیل می‌کنه و در چند ثانیه یک پرامپت کامل و قابل ویرایش تحویلت میده.
✨
مناسب برای:
• پیدا کردن پرامپت یک AI Art
• بازسازی استایل عکس‌ها
• استفاده در Midjourney، Stable Diffusion و سایر مدل‌های تولید تصویر
✅
بدون ثبت‌نام
✅
بدون واترمارک
🪙
رایگان
https://convly.ai/image-to-prompt/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/6928" target="_blank">📅 11:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6927">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGtg9gG4NcdzU93ikhwnMUu11OTXWzyjeFtcMD9fjKA1DvHtiLU5GSai37t3jOpPNntVWhULkyCmWC2szerphNMqCPVpX-InhNP3FGmBnnZ1mzk2lBkMkJFVyvO4AfnSj82HSv4d9Xfyd5T3vcN9AVaYDH33M5rwaNgPRddZERiWHWI1hrQR8I_ihrIFzm9PwWXtIMkvcaWNlZ0wIuZIwDV759ij8K3nqnMwSPoRQyjBhaEIKPQpPv5BFqNVR4xBWwMTcQGjGrxKW0ZxwGxioD5kUzODk6VV4ZlJW-Kq4PR11icLFILqmwNnJB4qUsz8l90Hh9Y8Xl32NkQGpvl_yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
بازی خودت را با هوش مصنوعی، در چند دقیقه بساز!
فقط ایده‌ات را بنویس؛ هوش مصنوعی بقیه کارها را انجام می‌دهد.
✨
بدون کدنویسی
🌐
اجرا مستقیم در مرورگر
🎯
آماده برای بازی و اشتراک‌گذاری با دوستان
https://codewisp.ai/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/6927" target="_blank">📅 09:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6925">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzU_-rWhHa0tEbkWhmkUnQOVwf0aeXulgHQQOEaQTQAahfMwnWTjZHYSJIw2td_FkiRuPyTOdSc0uD6bWtvJ3vXUq5wn0IfBZO7oqRF6-RJWHK9sT5GZOiiRzA_TO-EFamfzGXY0cwbA99y5CKVNjNXYukYkg4l4F5uWKAbB9bbco6zu_aIFqjBLJhSPb35z5N9HF45Q0i9KgditiqapgSJsCLrV-yokBkrDgsrpcGoOLcz6ZojneAcX8bPmfHUjvUyKqrIrPj15YOQ0rH9IP5HuiI4xd4jHxyga9wzh9qH5PUVrQOQ3IxM-VAOwgIX8X5z_IVkZn1LSbddnzTMuRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧩
؛
Hermes Browser Extension
افزونه‌ای حرفه‌ای برای مرورگرهای مبتنی بر کرومیوم که وب‌گردی شما را با رعایت سخت‌گیرانه حریم خصوصی، مستقیماً به محیط هوش مصنوعی Hermes Agent متصل می‌کند.
✨
ویژگی‌ها:
🧠
اتصال یکپارچه به هسته Hermes (محیط لوکال، کلاد یا ریموت)
📄
استخراج هوشمند و ایمن متن صفحات و تب‌های باز برای هوش مصنوعی
🎙
پشتیبانی از دستورات صوتی و رندر حرفه‌ای Markdown
🛡
امنیت حداکثری بدون نیاز به دسترسیِ تاریخچه و کوکی‌ها
🧪
نکته:
افزونه در فاز آلفا است؛ برای استفاده باید فایل‌های نسخه ریلیز را دانلود و به‌صورت دستی (Unpacked) در مرورگر لود کنید. پیش‌نیاز اصلی، نصب بودن خود Hermes Agent است.
📥
دانلود از گیت‌هاب (بخش Releases)
⭐️
حمایت از پروژه: ستاره (Star) در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/6925" target="_blank">📅 08:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6924">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🌐
؛
Omni Browser
مرورگر اندرویدی امن و فوق‌حرفه‌ای (مبتنی بر موتور فایرفاکس) با تمرکز شدید بر حریم خصوصی.
✨
ویژگی‌ها:
🛡
مسدودساز تبلیغات (uBlock) و گاوصندوق بیومتریک فایل‌ها
🧩
پشتیبانی مستقیم از نصب افزونه‌های فایرفاکس
🎬
شکارچی خودکار لینک‌های ویدیو + پلیر اختصاصی
🛠
مترجم ۱۰۰٪ آفلاین و ابزارهای حرفه‌ای دولوپرها (کنسول زنده JS)
🧪
نکته:
برنامه در فاز آزمایشی است؛ فعلاً به عنوان مرورگر اصلی استفاده نکنید و از اطلاعات مهم بکاپ بگیرید.
📥
دانلود از گیت‌هاب (بخش Releases)
⭐️
حمایت از پروژه: ستاره (Star) در گیت‌هاب
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/6924" target="_blank">📅 08:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6923">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKpeq-pv0Se29sbxPSpvKZtoHf4GSrAbJSZ17Afbl56pxWjYmhv4vG2y91yF4b-L_oMqt_dFhkEAVY2bSvKrTH50RoMDrRWXlxFre-zDN_Nx5RDfvFt7b-buvGi4eCVF9izJDaOilHFAjPmHKgSr-Hz0I_3K0cEJev3j-hIif0WrqOU2bg7Bv7R1PXgb7XvmC6FkH-fuorwXg0KTipD5XQXznI3hT06JpEcg351zsQkwMo4tYyR1nCDD-lXSSC1WHLQfHISx72kwMzaOZgdPuOsIZUE1zmbYtDeeJCc1ArTugC5l99AvvIxzNwlroSSY7pxstNsk_PcGN9N7hInSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/6923" target="_blank">📅 08:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6922">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">Telegram-X-0.28.10.1791-armeabi-v7a.apk</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6922" target="_blank">📅 01:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6920">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTelegram X APKs & Build Info</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Telegram-X-0.28.10.1791-arm64-v8a.apk</div>
  <div class="tg-doc-extra">58.4 MB</div>
</div>
<a href="https://t.me/ArchiveTell/6920" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Version
:
0.28.10.1791-arm64-v8a
Changes from 1785
:
4ac597ca...5c907d8b
#arm64
#beta
#apk
(
MD5
,
SHA-1
,
SHA-256
)</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6920" target="_blank">📅 01:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6919">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚀
آپدیت بزرگ بات منتشر شد: هوشمندتر و سریع‌تر
تغییرات کلیدی برای مدیریت یکپارچه کانفیگ‌ها و عبور از محدودیت‌های دسترسی:
✨
ویژگی‌های جدید:
•
📱
مینی‌اپ اختصاصی:
دسترسی سریع و رابط کاربری مدرن برای مدیریت آسان‌تر.
•
🔗
بخش ترکیب (Merger):
ادغام تمامی کانفیگ‌های Render و Railway در یک ساب‌اسکریپشن واحد (نیازمند توکن Cloudflare).
•
📡
بخش رله (Relay):
اتصال دامنه Render به Cloudflare Workers جهت رفع فیلترینگ بدون نیاز به خرید دامنه پولی.
🛡
نکته فنی (مصرف Cloudflare):
این روش بهینه‌ترین حالت ممکن است؛ با سقف ۱۰۰ هزار درخواست رایگان روزانه، نگران محدودیت نباشید. مصرف فقط در زمان اتصال/قطع صورت می‌گیرد.
⚠️
توجه:
به دلیل ترافیک بالای انتشار، ممکن است در ساعات اولیه با کندی جزئی مواجه شوید که به مرور برطرف خواهد شد.
🤖
شروع استفاده:
@REN_WZA_BOT
@REN_WZA2_BOT
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6919" target="_blank">📅 00:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6918">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0t6Vx9ZLK6lAuZgXilr6GaJqUPX9kL4Cpec0KGddz59rJ4cVQE6JrtBwja-0ourdFSmH9l4gUvb2Ok4LjtH9Ta0y0_YRCVzfHA9e5TVG1udZAYwD2hZnyR9oPVS0LFE0VjvRGC9QydJxdEcjb908E1Vb1V8u1lUtp-A0fJ6RPT9yWOkapWmPE9rgYeJKdEd2G94qvAfK1HrJJOkKFupcaPSkriSkSjYfms93p61Ox5Edgq1G8ruoxh40Ahtrdo8hmnEIGiwJphBYDMnGNpU_nyTJf0FZnTbbutsj7Pg5vEC6O37b8NkG6jIL66de3DznirewuCL9Jd7kv_EeIfHSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به Claude Fable 5 دوباره تمدید شد، شرکت Anthropic این مدل را تا 19 جولای در اشتراک معمولی در دسترس قرار می‌دهد.
محدودیت‌ها همانند قبل هستند: 50 درصد از میزان استفاده هفتگی. پس از یک هفته، Fable 5 به سیستم پرداخت بر اساس توکن از طریق API منتقل خواهد شد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6918" target="_blank">📅 22:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6916">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E6jLk0R9xwGtwy1n2NkvlgZ3lE1zHWgzay7BmNSYSQuib7GoX2MWgsO-2LK7l3R0xEUlYPrinDiYrumIUDyumpPfvyNqtAxGGrFdtSyS6NuQyTFtkBsKlxAB2xpHKbFvuMg91wsAed5AFFu_03iceugLQz632ULMFsEjf2qlFZxqBxlqXJZdgKtqj3rvqgLkNqZkQODy3iJYuBz7i-ncKiFTkBqQZjbBmBT7YULc9OFlKeaX6zoArruK_7swX5pqfvO9RAqpZ0vkGK1s8eXq8fKje8y4FU_LAsIjZGtU-vwLnS9eI5b6L00ecBkwt1KygvSdixBJvW0IZpZymyrGmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jcg6kh9DgYM1hPEujyioTz2EEPtcA5uvVhorfArs8kfabgFGii0YQmr9KhG2aAs7js26bMauXypxz8WDCA0Aycbl0dhULjHlTrj9qJD1MOhQv_k27D4BOVavDuAeyyq20Gy__ameVQvSOj2BWX8z1YZWwdesejSJPi7wxtjRgfSzAHI9O4XWksc6UW1VlYO2QhcSJFCFKQLyKp2Zq5AYzJvr2k_CIXtQ9Bf043DsNGYGzloPDwyuqs8prGZqGNF4LTncZ6oUMyCkflFsAWaVRh1jRCod9vifYYyPItAhuYX9sq3NaXuCLAhtE8nYtpZOzZs_c-LwagHPBbqK_VkosA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">؛PCLink راهکاری سریع و سبک برای دسترسی از راه دور به رایانه، بدون تنظیمات پیچیده
🖥
• دسترسی کامل به فایل‌ها، اپلیکیشن‌ها، کیبورد و ماوس
• خاموش، روشن و ری‌استارت کردن سیستم از طریق گوشی
• اتصال آنی با اسکن QR Code
• پشتیبانی از Windows و Linux
🔗
لینک مخزن گیت‌هاب پروژه
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6916" target="_blank">📅 21:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6915">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اپلیکیشن اندروید NipoVPN توی گوگل‌پلی   https://play.google.com/store/apps/details?id=net.sudoer.nipo</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6915" target="_blank">📅 20:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6914">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMorteza Bashsiz مرتضی باشسیز</strong></div>
<div class="tg-text">اپلیکیشن اندروید NipoVPN توی گوگل‌پلی
https://play.google.com/store/apps/details?id=net.sudoer.nipo</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/6914" target="_blank">📅 20:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6913">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@ArchiveTell.json</div>
  <div class="tg-doc-extra">2.4 KB</div>
</div>
<a href="https://t.me/ArchiveTell/6913" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ warp
فقط سامانتل
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6913" target="_blank">📅 19:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6912">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پروکسی تلگرام
🔥
https://proxybolt.link/
| سایت
@mtpro_xyz_bot
| ربات
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6912" target="_blank">📅 19:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6911">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">⏱
؛
tg-username-clock
یک اسکریپت ساده و جذاب برای شخصی‌سازی پروفایل تلگرام که نام خانوادگی (Last Name) حساب کاربری شما را به‌صورت خودکار و هر یک دقیقه، با زمانِ دقیقِ فعلی به‌روزرسانی می‌کند.
✨
امکانات:
*
⏱
نمایش زنده زمان: تبدیل نام کاربری شما به یک ساعتِ زنده برای مخاطبان.
*
⚙️
به‌روزرسانی خودکار: اجرای اسکریپت در پس‌زمینه و آپدیتِ اتوماتیکِ هر دقیقه‌ای.
*
🚀
سبک و کاربردی: پیاده‌سازی سریع بدون درگیری‌های پیچیده نرم‌افزاری.
📥
دریافت اسکریپت و دسترسی به منبع پروژه.
⚠️
احتیاط یادتون نره!
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6911" target="_blank">📅 18:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6910">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔐
؛
OfflinePW
یک پسورد منیجر اندرویدیِ فوق‌امن، سبک و کاملاً آفلاین است که از یک دولوپر ایرانی (Cyru55
❤️
) که با الگوریتم‌های نظامی و معماری «دانش صفر» توسعه یافته است.
✨
امکانات:
🚫
آفلاینِ مطلق:
بدون نیاز به هیچ‌گونه دسترسی (Permission) در سیستم‌عامل.
🪚
امنیت TwoFish-256:
قدرتمندتر و ایمن‌تر از استانداردهای رایج AES.
⛏️
ضد Brute-force:
خنثی‌سازی حملات با استفاده از PBKDF2.
📸
حریم خصوصی:
مسدودسازی خودکار اسکرین‌شات و ضبط از صفحه.
⚡️
حجم مینی‌مال:
تنها ۴ مگابایت با رابط کاربری ساده و پوشه‌بندی شده.
🔪
پشتیبانی وسیع:
سازگاری کامل از اندروید ۴.۰ تا نسخه‌های جدید.
🔒
مدل Trust No One (به هیچ‌کس اعتماد نکن)
هیچ‌کدام از پسوردها یا کلیدهای رمزنگاری شما در سیستم ذخیره نمی‌شوند. تنها کلیدِ دسترسی به داده‌ها، رمزی است که منحصراً در ذهن شما قرار دارد.
📥
دانلود فایل نصب (APK) از بخش Releases گیت‌هاب.
⭐️
در صورت رضایت، با Star دادن از پروژه حمایت کنید.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/6910" target="_blank">📅 17:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6909">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiE3e13k17hYxhKZPZ82gZP501ojsZ2GfyIs-WYzRcBphpoAMUptQ9ccttKo41gx743uf2HUZ3Tn_OhclmHqxymewoti9hcJdGvq6x4aZyaEi-RMA1iotly39h5byasK3VGZp0mxZ8FqrW-Eejot1yvtNv5snaH7kUKjRfxMrfmb0yD2eT5IwkqIydcUfJ37Vkq0CGEercoyKO2AzhglwAOZ18S1TQ-qmWpSDah4MzqwUI3tcAuTokfCne-sLybPxywOKCLjPx0JaB7hfoa_UT7Lsw7bwnhi3g9xt0ArJM576PH2PNFl3zteaPf8T3TpqL1HwTCGZ4MiRfZ8USj0rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌍
؛
OSINT Intelligence Dashboard
داشبورد متن‌باز و کاملاً رایگان برای رصد بلادرنگ رویدادهای امنیتی جهان؛ یک تحلیل‌گر شخصی و جایگزینی قدرتمند برای پلتفرم‌های گران‌قیمتی مثل بلومبرگ ترمینال.
✨
امکانات:
*
📡
رصد جامع:
مانیتورینگ ۲۷ فید اطلاعاتی (پروازهای نظامی، تشعشعات و درگیری‌ها) روی کره سه‌بعدی.
*
🤖
تحلیل هوشمند:
اتصال به مدل‌هایی مثل GPT و Claude برای دریافت لحظه‌ای گزارش‌های امنیتی.
*
📱
مدیریت آسان:
کنترل کامل و دریافت هشدارهای چندسطحی (FLASH تا ROUTINE) از طریق بات تلگرام و دیسکورد.
🔒
اجرای ۱۰۰٪ لوکال
این سیستم کاملاً آفلاین و فاقد هرگونه تله‌متری (Telemetry) است و تمام پردازش‌ها منحصراً روی سیستم شما انجام می‌شود.
📥
دریافت سورس‌کد (با بیش از ۱۰ هزار Star) از گیت‌هاب.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/6909" target="_blank">📅 16:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6907">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🗑
حذف کامل برنامه‌ها و فایل‌های اضافی مک با Uninstally
وقتی برنامه‌ای رو در macOS به سطل زباله منتقل می‌کنید، کلی فایل کش، لاگ و تنظیمات پنهان روی سیستم باقی می‌مونه. این ابزار بومی (Native) و اوپن‌سورس تمام این ردپاها رو برای همیشه پاک می‌کنه.
🔥
ویژگی‌های مهم:
🖱
ادغام با Finder:
امکان حذف سریع برنامه‌ها فقط با یک کلیک‌راست (بدون نیاز به باز کردن خود ابزار).
📦
پشتیبانی از Homebrew:
شناسایی، مدیریت و حذف پکیج‌ها (Casks و Formulae).
🧹
اسکنر فایل‌های یتیم:
پیدا کردن و پاک کردن فایل‌های جا مانده از برنامه‌هایی که قبلاً به صورت دستی پاک کردید.
🔒
کاملاً آفلاین:
بدون جمع‌آوری دیتا (Analytics) و بدون نیاز به ساخت اکانت.
🔗
لینک مخزن گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/6907" target="_blank">📅 16:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6906">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🌍
سناریوی جدید AI 2040: Plan A
تیم پژوهشی گزارش معروف AI 2027، سناریوی آینده‌پژوهانه جدیدی را منتشر کرده که مسیر توسعه هوش مصنوعی را در صورت همکاری قدرت‌های جهانی (آمریکا و چین) بررسی می‌کند. بر اساس این سناریو، تا سال ۲۰۳۵ حدود ۸۵٪ کارهای اقتصادی به AI واگذار خواهد شد.
🔥
مهم‌ترین نکات این سناریو:
🤝
توقف رقابت AGI:
توافق آمریکا و چین بر سر کاهش سرعت توسعه، افزایش شفافیت و نظارت‌های سخت‌گیرانه بین‌المللی.
🛡
تمرکز روی ایمنی:
متوقف شدن توسعه مدل‌های پیشرفته، صرفاً تا زمان انجام ارزیابی‌های جامع امنیتی.
💰
درآمد پایه همگانی (UBI):
رشد اقتصادی بی‌سابقه از ۲۰۳۲ و پرداخت یارانه‌های سالانه به شهروندان جهت جبران بیکاری ناشی از اتوماسیون.
🚀
شتاب علمی چشمگیر:
رسیدن AI به سطح برترین متخصصان تا ۲۰۳۵ و افزایش ۱۰ تا ۱۰۰۰ برابری سرعت پیشرفت علمی از ۲۰۳۷.
⚠️
نکته:
این گزارش صرفاً یک سناریوی تحلیلی و آینده‌پژوهانه است و پیش‌بینی قطعی محسوب نمی‌شود.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/6906" target="_blank">📅 16:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6905">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بنازم
🔥
🔥
🎁
گیووی اکانت‌های مادام‌العمر Proton VPN!  اکانت رسمی پروتون اعلام کرده که اگر امروز تیم ملی سوئیس بازی رو ببره، اشتراک‌های بسیار نایاب و رایگان مادام‌العمر (Lifetime) هدیه میده!
🔥
جزئیات:  *
🇨🇭
شرط قرعه‌کشی: پیروزی سوئیس در مسابقه امروز مقابل آرژانتین.…</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/6905" target="_blank">📅 16:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6904">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بنازم
🔥
🔥
🎁
گیووی اکانت‌های مادام‌العمر Proton VPN!
اکانت رسمی پروتون اعلام کرده که اگر امروز تیم ملی سوئیس بازی رو ببره، اشتراک‌های بسیار نایاب و رایگان مادام‌العمر (Lifetime) هدیه میده!
🔥
جزئیات:
*
🇨🇭
شرط قرعه‌کشی: پیروزی سوئیس در مسابقه امروز مقابل آرژانتین.
*
💎
جایزه: پلن Lifetime پروتون (اشتراکی که در حالت عادی اصلاً فروخته نمیشه و ارزش بسیار بالایی داره).
🔗
[لینک توییت رسمی پروتون]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6904" target="_blank">📅 16:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6903">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4FtNOHPpR_N07a7Z3Z8zL2UczsWMHebSOCZFUeWpW5VZaX5qhguHcglO_EzoIcrhAmUkLcCOTCIIfxoFGGPW0mDwTx5iEePcbbu41LGg6wQScYLpe8NGMCKs4ZYo2C9O9stI1zXvKB4K9NWlTEX8SBXdR9vUrqJVGHbRMsvi7QJJnTdlogV1ecWkcv6O6wmeGbVrps231r2ROO2-VQOQa_FEeI35_NTXBj46uWg_5qHQae1DOuUIw4trKS5qN-aIBTeHuKEbdhGXRRNGkYprxiv4N8vhEViJhccomnTFe5ZQmz0Y3jo-HY5usR7YvpUakToBYw5CZij8pMv4-LIRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
AIText Detection for X
⁩تشخیص متن تولید شده توسط هوش مصنوعی!
🔍
✨
‏‌این افزونه با هدف شناسایی و تحلیل محتوای تولید شده توسط هوش مصنوعی در توییتر طراحی شده که با یکپارچه‌سازی آسان با فید توییتر، امکان تحلیل توییت‌هایی که کاربران میخونن رو فراهم میکنه.
https://www.tweetdetective.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/6903" target="_blank">📅 15:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6902">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWqnm40nKfNJIhICa-yLmlvBEue7-HECE_vxLR71Laaagjf6dQ88JSnSNTYuIQCA-hVA59py-c548pGNc7zbeakB3tnooPWtxD0_MSFfwwe42DSeKClUUUzGPDjHqmv2qQ9vHOV4XyDV5DlB5jndUZfIuk6oYhfRTIRpYVDbBQZ_W-Gx1UYEQfGDxP-4C6Eth1lZIlo-tI3WYTXLxiTxVQv89Ecd6jz5VBhLMo90Azdj9ii6HlqOnZxyzRf9kUu4HKzCgGRFkp0kSooZvrTY7FqqL8XATqniPepl5dXS_2rWd6z92vZQImjZI6Ky_CX6-ldV1xKu2R1lArvdlsqKsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
معرفی ‌Gitea⁩؛ جایگزینِ سبک و قدرتمندِ ‌GitHub⁩ برای میزبانیِ شخصی!
🛠
‏با ‌Gitea⁩ می‌توانید در عرض چند دقیقه، سرویسِ گیتِ اختصاصی خودتان را راه‌اندازی کنید. این پلتفرم با وجودِ سادگی، بسیار منعطف است و اجازه می‌دهد به راحتی پروژه‌هایتان را از ‌GitHub⁩ یا ‌Bitbucket⁩ به محیطِ امنِ خودتان منتقل کنید.
‏
✨
ویژگی‌ها:
‏‌
🔹
فوق‌العاده سبک: یک باینریِ واحد که حتی روی سخت‌افزارهای محدود هم کار می‌کند.
‏‌
🔹
سازگاری کامل: پشتیبانی از ‌GitHub Actions⁩ برای اتوماسیونِ حرفه‌ای.
‏‌
🔹
نصبِ سریع: راه‌اندازیِ بی‌دردسر از طریق ‌Docker⁩ و پشتیبانی از دیتابیس‌های مختلف.
🔹
همه‌کاره: شاملِ مدیریتِ تسک‌ها، ویکی، رجیستریِ پکیج و ابزارهای ‌CI/CD⁩.
لینک گیت هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/6902" target="_blank">📅 14:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6901">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Se7QmnOWhsxyD1Zrw9SvbptX9NJjTvvmMnq8RgkytdQ52TvS8A4jAzUwZI-sn2g-OxSwQ4rt0_NytJfIXQmnPMXRIInUz8HcaLPFrqwZDa2vclHb7GNIodLy1DB9Rr2w1FUcuhBiZYXz6q7Flr_iJsCVmV1BroRsOWKmXND7AzcizjaHrhwNXKD8fLlNVd3CXO_IaU7N08VCNGswu0APwuwFUo3gys21LIuVEgS90xpqV8ybOpUGsxdYcW8gy4zcj1dnPUNUoZE-QU5cSgbYdMW2rloQ0TQMlTya8ardJjCM8gWQ8vuF3mgaRUhdAMPs3cnpjrQtzfDBu46c44exzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📁
فایل منیجر قدرتمند Fast File Explorer؛ جایگزین قاتل برای Windows Explorer!
اگر از کندی سرچ فایل‌ها در ویندوز خسته شده‌اید، این ابزار سریع‌ترین روش برای پیدا کردن فایل‌هاست.
🔥
ویژگی‌های مهم:
🔍
سرعت استثنایی:
سرچ فوق‌سریع که فایل‌ها را در چند ثانیه پیدا می‌کند (بسیار سریع‌تر از جستجوی پیش‌فرض ویندوز).
🌐
امکانات شبکه و امنیت:
اتصال مستقیم به سرورهای ریموت و بررسی سلامت داده‌ها با هش‌های MD5 و SHA.
👁
پیش‌نمایش در لحظه:
نمایش محتوای فایل‌ها و داکیومنت‌ها مستقیماً داخل رابط کاربری برنامه، بدون نیاز به باز کردن آن‌ها.
🖥
چندپلتفرمی:
کاملاً رایگان و قابل اجرا روی ویندوز، لینوکس و مک.
🔗
[
لینک دانلود
]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/6901" target="_blank">📅 13:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6900">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یه توضیحی که مدت‌ها تو دلم مونده بود
راستش قصد نداشتم وارد حاشیه بشم، ولی بعضی چیزها وقتی گفته نشن، فقط آدم رو اذیت می‌کنن. حس کردم بهتره تجربه‌ی خودم رو بگم تا بقیه هم در جریان باشن.
ادمین
نتلیفای
و
زئوس
در واقع دوست ما بود...
زمانی که هنوز کانالی نداشت، عضو کانال ما بود. ادمینش بود. از کارهاش حمایت کردیم، پروژه‌هاش رو معرفی کردیم، کانفیگ در اختیارش گذاشتیم و هر جا تونستیم کمکش کردیم. حتی وقتی کانال خودش رو راه انداخت، پست‌هاش رو تو همین کانال فوروارد می‌کرد و طبیعتاً بخشی از ممبرها هم به سمت کانالش رفتن. بابت زحمتی که برای پروژه‌هاش کشید همیشه براش احترام قائل بودم.
اما چیزی که ناراحتم کرد، این بود که این حمایت هیچ‌وقت دوطرفه نبود.
- برای راحت‌تر شدن کار کاربران، با کمک یک دولوپر اپلیکیشن نتلیفای رو ساختیم، اما حتی حاضر نشد نصبش کنه و از همون اول گفت «اپ به چه درد می‌خوره؟» در حالی که هدف فقط ساده‌تر شدن استفاده برای کاربرها بود.
- بعداً یکی از دوستان، یک فورک تمیز و کامل از کانفیگ‌جنریتورش منتشر کرد. درخواست شد داخل کانالش معرفی کنه، اما قبول نکرد. در نهایت خودم اون پروژه رو توی کانال معرفی کردم.
- خودم هم چند بار پروژه‌ش رو فورک کردم و قابلیت‌هایی بهش اضافه کردم و تو توضیحات ازش قدردانی کردم اما برخوردش بیشتر تمسخر و بی‌اهمیتی بود. در حالی که پروژه
Open Source
بود. اگر قرار نیست کسی مشارکت کنه، خب می‌شد پروژه رو کلوزسورس نگه داشت.
- آخرین مورد هم مربوط به اسکنر IP بود. برای معرفی پروژه بهش پیام دادم، اما انقدر برخوردش سرد و آزاردهنده بود که واقعاً حالم گرفته شد. یه بار گفت «مطلب مرتبط نیست»، یه بار گفت «تبلیغ نمی‌کنم». در حالی که این ابزار به نظرم برای جامعه کاربری مفید بود و صرفاً برای کمک به اکوسیستم ساخته شده بود، نه تبلیغات شخصی.
چیزی که برام عجیبه اینه که از همه انتظار حمایت برای مطرح شدن پنل و پروژه‌هاش وجود داره، اما وقتی نوبت به حمایت از دیگران می‌رسه، اون نگاه دیده نمی‌شه.
این متن برای تخریب کسی نیست؛ فقط تجربه شخصی من از همکاری و حمایتیه که انتظار داشتم متقابل باشه، اما نبود...</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/6900" target="_blank">📅 13:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6892">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PywYI_n-HwmXJkmlhQaKbQTSwyBLihw7qsG5Z6RuqRH6vAD3NpaN-Xu_rAlUR6YSeg4XjoeJhWRR0sEd5ZbULmhT1wf3f0qLGQ00Nobz-x3Zf6vu0nAA5iFh6fFxCSBdtoib0QshVDgIpzlv-mZSRIjo2s0UfVbsbalNB6HdDCpL46OKo6HFSCeAVP3IYgFk-__gg-aAX9pWqHKjlRfkvg0-211pj3xRH-jKXsmKgByAZ75G67jBwHw5ie8BuJeXhm0NqfWiLGnggdu6WE8YaUNSRAARi-Q3kV70vuTI5kMgWZ2ZF1eNa7oYisG5VvyuYozEwo1inJHRFML2-_d5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zc9Gw9OY5bFCbJk6K3ussU4Aq-LDEZRZ1QoFQwiJp-suw0geD5v4ZmyW3Jn-aSpRYPZsUeeRIXuKlCoByNxCy_N2iiu3wO03dfruR2w9NBTnVKlhMlE_-EjyydgOmMwIMCMy3UA1NUFLKtx8vzYD1Qwyapk9Lzu_LiMCMQTniH2wgCUKS1pXFnxIOVKW69G4uhpTLEAnEfx-MSgTi_YsyTDS0-70ZSfGOD5SIXxeI_K7b02n3nBRtkePis8dtftJA0CID9uE6JFZGI65LO5tdiUBShjsAie2-6UPqY5qom7MPc3iDrN1rj6nPuTVgwPeVdsvkNRdyFpSOEY7IjrXOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SARuEESVpDI3NXowVjl0bJMBqoNB2hhrVnETDFM6h-GoKFlUQoW991lPEv9763S_IOlJ9xNz_riPXuwFVhOqnGbQ0uR2P_M74jLDtQM0xFfiGbxRa-zEHL-iTk2rw7d0XSXQgatgmSmlBNfgWwrEo8bnvGCr7p85xwb1Ck8VC3uaxIQ1T7n8cpkiKi497vbYpnFMYOfITU5i7G2nypI9MyZY2o7AM7ZNU2XUsyngGRyqF_LQZc1MLSpnmare3IWXB97EUISSw8fEzLdAtMkqkeHj-yv9kEhEoOnJh0InPPMfDyiZ9txPgGGdFWS7h6WD_vN96b41xpaBRQQIpaHBoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LxvmQhrnZP2GeyeQSuuN5B2nBE9N84TnwjiuhMvecux9qLbnS6orjsj6PsrdsSnLbEkfX9vn03lI2LVAl9w7RA7TqITTH3Mo4pE32Hq2hNfSXavE8OygVKb1u4jwbsbgrMC4Dpfxp1IMKJv5GdovEF5KShb-ML7KIg3W5fptTMwJjmSiYdQC8syM4jgnIWYU40MfGKNYsZUPBeUwekKju7ma4M-ZliA7-etXCjq-R1tN_z1t_RN7pbezuS9a47wCo6d3cv2ml5kgVJ1KkPk1-veYmqrr-U-rd0WBLqDbMUVcAk2F-Pmn41UFeO18XBF4-eZJTrpeGCvbFS_fyOGKcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/6892" target="_blank">📅 13:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6887">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سایت‌های Torrent برای دانلود مدل‌های LLM
1.
https://ckpt.cc/
2.
https://huggingbay.xyz/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/6887" target="_blank">📅 12:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6886">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏
🚀
معرفی ‌VoiceTypr⁩؛ تایپ صوتیِ هوشمند و کاملاً آفلاین!
🎙
✨
( از زبان فارسی پشتیبانی میکنه )
‏این ابزارِ فوق‌العاده دقیقاً مثل یک دستیارِ شخصی روی سیستم‌عاملِ شما عمل می‌کنه، کافیه دکمه‌ی میانبر رو بزنید و شروع به صحبت کنید تا متن‌تون دقیقاً همون‌جایی که نشانگرِ موس هست، ظاهر بشه.
‏
🔥
ویژگی‌ها:
🔹
حریم خصوصی مطلق: پردازش‌ها کاملاً آفلاین انجام می‌شه و هیچ داده‌ای از سیستم شما خارج نمی‌شه.
‏‌
🔹
سرعتِ بی‌نظیر: به لطفِ بهینه‌سازی‌های سخت‌افزاری، حتی روی سیستم‌های معمولی هم مثل برق و باد کار می‌کنه.
🔹
‏ پشتیبانی گسترده: بیش از ۹۹ زبانِ مختلف رو پوشش می‌ده تا هیچ محدودیتی نداشته باشید.( شامل زبان فارسی)
🔹
‏ یکپارچگی عالی: قابلیتِ درجِ مستقیمِ متن در هر نرم‌افزاری که باهاش کار می‌کنید.
گیت هاب پروژه
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6886" target="_blank">📅 11:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6885">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🛡️
؛ungoogled-chromium؛ کرومیوم بدون وابستگی‌های گوگل
اگر به دنبال یک مرورگر سریع، سبک و نزدیک به تجربه اصلی Chromium هستید اما نمی‌خواهید ارتباطات غیرضروری با سرویس‌های گوگل داشته باشید، ungoogled-chromium یکی از گزینه‌های جذاب است.
✨
ویژگی‌های مهم:
🔹
حذف وابستگی‌ها و سرویس‌های اختصاصی گوگل
🔹
کاهش درخواست‌های پس‌زمینه به دامنه‌های گوگل
🔹
حذف کدهای مربوط به سرویس‌های گوگل
🔹
تمرکز بیشتر روی حریم خصوصی، شفافیت و کنترل کاربر
🔹
حفظ ظاهر و تجربه نزدیک به Chromium اصلی
🔹
امکان شخصی‌سازی بیشتر با فلگ‌ها و تنظیمات اضافی
این پروژه در واقع همان Chromium است، اما با تغییراتی برای کسانی که می‌خواهند کنترل بیشتری روی مرورگر خود داشته باشند.
📌
مناسب برای:
✅
کاربران علاقه‌مند به حریم خصوصی
✅
کسانی که مرورگر سبک و بدون سرویس‌های اضافی می‌خواهند
✅
کاربران لینوکس، ویندوز و macOS که دنبال جایگزین Chromium هستند
🔗
پروژه متن‌باز
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6885" target="_blank">📅 11:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6884">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚀
؛Archive Scanner v1.0.3 منتشر شد!  جدیدترین نسخه‌ی Archive Scanner با بهبودهای مهم در دقت، سرعت و امکانات منتشر شده است.
✨
تغییرات مهم:
⚡️
اصلاح کامل تست سرعت دانلود (اندازه‌گیری دقیق‌تر و عبور از فیلترینگ SNI)
📤
اضافه شدن تست سرعت آپلود برای هر IP
🤖
ساخت…</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6884" target="_blank">📅 11:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6883">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ایپی تمیز کلودفلر
مخابرات
104.19.2.34
104.18.135.100
172.67.80.2
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6883" target="_blank">📅 11:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6881">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">شاید من ی مدتی دور باشم
بقیه دوستان هستند
حالم این روزا، حال خوبی نیست
💔
مثل حال عقاب بی‌پرواز</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6881" target="_blank">📅 00:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6880">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✅
آموزش کامل SillyTavern + اتصال API شخصی + استفاده از شخصیت‌های آماده سلام رفقا!
👋
اگر API شخصی داری (مثل OpenRouter، OpenAI، Groq، DeepSeek یا هر سرویس OpenAI-Compatible)، با SillyTavern می‌تونی از شخصیت‌های آماده استفاده کنی و تجربه‌ای بسیار حرفه‌ای‌تر…</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6880" target="_blank">📅 23:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6879">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
آموزش کامل SillyTavern + اتصال API شخصی + استفاده از شخصیت‌های آماده
سلام رفقا!
👋
اگر API شخصی داری (مثل OpenRouter، OpenAI، Groq، DeepSeek یا هر سرویس OpenAI-Compatible)، با
SillyTavern
می‌تونی از شخصیت‌های آماده استفاده کنی و تجربه‌ای بسیار حرفه‌ای‌تر از بسیاری از سرویس‌های چت هوش مصنوعی داشته باشی.
🚀
۱) نصب SillyTavern
۱.
آخرین نسخه
Node.js LTS
را نصب کنید.
۲.
آخرین نسخه SillyTavern را از صفحه Releases دریافت کنید:
https://github.com/SillyTavern/SillyTavern/releases
۳.
فایل را استخراج کنید.
۴.
فایل
Start.bat
را اجرا کنید.
۵.
مرورگر به‌صورت خودکار باز می‌شود. اگر نشد، این آدرس را باز کنید:
http://localhost:8000
👤
۲) دانلود شخصیت‌های آماده
یکی از بهترین منابع کارت شخصیت:
https://chub.ai
می‌توانید عباراتی مثل این‌ها را جستجو کنید:
girlfriend
romance
friend
assistant
waifu
anime
fantasy
کارت دلخواه را دانلود کنید.
کارت‌های شخصیت شامل اطلاعاتی مثل شخصیت، پیام آغازین، نمونه مکالمه و تنظیمات نقش‌آفرینی هستند.
📥
۳) وارد کردن کارت به SillyTavern
وارد بخش
Characters
شوید.
روی
Import Character
کلیک کنید.
فایل PNG یا JSON کارت را انتخاب کنید.
یا فایل را مستقیماً داخل برنامه Drag & Drop کنید.
🔌
۴) اتصال API شخصی
از منوی
API Connections
وارد تنظیمات شوید.
تنظیمات:
API Type
Chat Completion
Source
OpenAI Compatible
سپس اطلاعات API خود را وارد کنید.
نمونه Base URL:
OpenRouter
https://openrouter.ai/api/v1
OpenAI
https://api.openai.com/v1
Groq
https://api.groq.com/openai/v1
DeepSeek
https://api.deepseek.com/v1
سپس:
API Key
مدل (Model)
را وارد کرده و روی
Connect
بزنید.
اگر اتصال سبز شد، همه چیز آماده است.
💬
۵) شروع گفتگو
شخصیت موردنظر را انتخاب کنید و گفتگو را آغاز کنید.
کیفیت پاسخ‌ها بیشتر به
مدل هوش مصنوعی
و
کیفیت کارت شخصیت
بستگی دارد، نه خود SillyTavern.
⚙️
تنظیمات پیشنهادی
Temperature:
0.8 - 1.0
Context Size:
تا جای ممکن بیشتر (در صورت پشتیبانی مدل)
Streaming:
روشن
System Prompt:
متناسب با کاربرد خود تنظیم کنید.
💡
نکات
✅
از کارت‌های با دانلود و امتیاز بالا استفاده کنید.
✅
هر API سازگار با استاندارد
OpenAI-Compatible
معمولاً در SillyTavern قابل استفاده است.
✅
مدل‌های مختلف رفتار متفاوتی دارند؛ چند مدل را امتحان کنید تا بهترین نتیجه را بگیرید.(ممکنه یه مدل اصن جواب نده!)
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6879" target="_blank">📅 23:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6878">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✨
وگا — دستیار هوش مصنوعی تلگرام
قدرتمندترین ربات هوش مصنوعی فارسی، برای پیوی، گروه و کانال شما!
🚀
━━━━━━━━━━━━━━
🧠
مدل‌های هوش مصنوعی
از بین قوی‌ترین مدل‌های دنیا، مدل دلخواهت رو برای چت انتخاب کن:
-
🧠
Claude Opus 4.8
-
🔮
Claude Sonnet 4.6
-
🐋
Deepseek 4 Pro
-
🐉
Qwen 3.6
-
💎
GLM 5.2
-
🍃
Gemma 4
-
🦙
Llama 4
-
🚀
GPT-4
-
🧬
Minimax M3
-
🐬
Mimo 2.5
━━━━━━━━━━━━━━
📢
فعال‌سازی در کانال شما
وگا رو زیر پست‌های کانالت فعال کن! کافیه ربات در کانال و گپ متصل به آن ادمین بشه تا زیر هر پست، کامنتی کوتاه و جذاب بذاره — دقیقاً مثل کانال آرشیو تل.
🔍
جستجوی زندهٔ وب
پاسخ‌های به‌روز و دقیق، برگرفته از جدیدترین منابع اینترنتی.
🔗
خواندن لینک‌ها و مخازن گیت‌هاب
لینک بفرست تا محتوای صفحه رو بخونه؛ ریپازیتوری‌های GitHub رو هم مستقیم آنالیز می‌کنه.
📦
👁
تحلیل عکس، ویدیو و PDF
عکس، ویدیو، فایل PDF و فایل صوتی رو می‌بینه، می‌شنوه و به‌طور کامل تحلیل می‌کنه.
━━━━━━━━━━━━━━
📰
اخبار روز
گزیده‌ای از تازه‌ترین اخبار در سه دسته: سیاسی ,  ورزشی , تکنولوژی — با به‌روزرسانی 5 ساعته.
🧮
حل سوالات درسی و علمی
سوال درسی یا علمیت رو به‌صورت متن یا عکس بفرست وگا با استفاده از به‌روزترین منابع، پاسخی کوتاه، دقیق و کامل می‌ده.
❄️
قیمت لحظه‌ای ارز و طلا
قیمت زنده رو در لحظه با نمایش اخرین تغییرات در روز بگیر
━━━━━━━━━━━━━━
📚
وگا ویکی
دستیاری هوشمند برای پرسش‌وپاسخ: سوال‌های عمومی رو خودش جواب می‌ده و برای موضوعات دانشنامه‌ای مقالهٔ مرتبط از ویکی‌پدیای فارسی رو پیدا و بررسی می‌کنه و بر اساس اون پاسخ می‌ده و لینک مقاله رو هم می‌پذیره.
👨‍💻
وگا کد
ابزاری حرفه‌ای برای کدنویسی، مجهز به مدل‌های GLM 5.2، Deepseek 4 Pro و Minimax M3.
همچنین:
🎨
ساخت عکس
🎙
ویس‌چت
🔤
تبدیل صدا به متن و برعکس
🌐
ترجمه به هر زبان
━━━━━━━━━━━━━━
📢
@ArchiveTell
-
@VegaEnter</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6878" target="_blank">📅 22:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6876">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1PIWogAJDiMDCEpWVDVKiFfv5OkhbjjeeowtslILWEtql016YrZBOS3Anbj3ya_GQPZmYNtJmBzmwssai8apo91yjjoYuzQktbLW8Y8u8J2d1qUgu-e8EzMHlYYr984FKWa01uQL8EtUUGTUMJMGoY6fuG_1RDs7RBaJitc0RVMruOnutFlLVVTUMAEDMody9A5dtxfaC41q1-L5qYHqptZxZZi1mKK-mdRNzvw-loUkPbFV4brpEmJdYg-i3H0JlFS-6nmTTBP2No2K5A9ATIlvwIKRVgvEGFhg0EkrUGXpJPcrPA15UT1PJolc0Q8Q3WGtpoMP7VO0FYL48nVcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a77ed13056.mp4?token=Fnpx0I9IeL-iBiYxjuwtExHuKt6a82LaKtoyh32AF6WRg5n-BrLjJSEEtgywLJMI3t41N53puuwzE-20dGmQ6XhHRjMBulGVB6MMUM1x0hCpUj39KlS4t6aPKiUx8-C5IBteE5HZVU71-sycVXdPMOysAMy1k-w1P6zHN_RwD7l1RaY2zRhD2Yi6Wn-lYxVIV6kuPGYKjTE6e2tidlNYBc9xZ6-YWAjVquXiylAh8TMZMSpAH10Q2WP66FHa4XhW2reayW32cDm2T7RFMmLtdschjuJ_QytFvACuEIAVmBbfM4HIMOSTF7UCdwGJG1Su7C4OwhLlsak-JtfhV95RBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a77ed13056.mp4?token=Fnpx0I9IeL-iBiYxjuwtExHuKt6a82LaKtoyh32AF6WRg5n-BrLjJSEEtgywLJMI3t41N53puuwzE-20dGmQ6XhHRjMBulGVB6MMUM1x0hCpUj39KlS4t6aPKiUx8-C5IBteE5HZVU71-sycVXdPMOysAMy1k-w1P6zHN_RwD7l1RaY2zRhD2Yi6Wn-lYxVIV6kuPGYKjTE6e2tidlNYBc9xZ6-YWAjVquXiylAh8TMZMSpAH10Q2WP66FHa4XhW2reayW32cDm2T7RFMmLtdschjuJ_QytFvACuEIAVmBbfM4HIMOSTF7UCdwGJG1Su7C4OwhLlsak-JtfhV95RBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
معرفی Hugging Bay؛ دنیای مدل‌های هوش مصنوعی، یک‌جا کنار هم!
🏴‍☠️
✨
دنبال یه مدل AI خاص برای پروژه‌ات هستی ولی بین صدها مخزن و لینک مختلف گم میشی؟ پیدا کردن بهترین LLM، مدل ویدیویی یا حتی Agent مناسب واقعاً می‌تونه وقت‌گیر باشه.
؛Hugging Bay مثل یه Torrent Tracker برای دنیای هوش مصنوعیه که انواع مدل‌های اوپن سورس و حتی مدل‌های منتشرشده رو یکجا جمع کرده. جذاب‌ترین بخشش هم جستجوی هوشمنده؛ فقط نیازت رو به زبان طبیعی بنویس تا بهترین مدل رو بهت پیشنهاد بده.
🔥
ویژگی‌ها:
1️⃣
جستجوی هوشمند: پیدا کردن مدل‌ها با زبان طبیعی مثل «بهترین Embedding Model برای RAG».
2️⃣
آرشیو کامل: دسترسی به LLMها، مدل های ویدئو و صدا و AI Agents در یک مکان.
3️⃣
؛Semantic Re-ranking: نتایج جستجو بر اساس مفهوم و کیفیت، نه فقط کلمات کلیدی.
4️⃣
مناسب توسعه‌دهنده‌ها: پیدا کردن سریع مدل مناسب برای پروژه‌های تجاری یا شخصی.
5️⃣
؛Open-Source Friendly: مرجع جذاب برای کشف و دانلود مدل‌های متن‌باز.
🔗
https://huggingbay.xyz/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6876" target="_blank">📅 21:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6875">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌐
کامپیوترت رو به یک هات‌اسپات حرفه‌ای تبدیل کن!
با MyPublicWiFi می‌تونی لپ‌تاپ یا کامپیوتر ویندوزی‌ات رو به یک Wi-Fi Hotspot تبدیل کنی و اینترنت رو با موبایل، لپ‌تاپ و سایر دستگاه‌ها به اشتراک بذاری.
✨
ویژگی‌ها:
🌍
اشتراک‌گذاری اینترنت از طریق Wi-Fi، LAN، VPN، مودم USB و...
🔓
اشتراک‌گذاری اتصال VPN با دستگاه‌های متصل
👥
نمایش و مدیریت دستگاه‌های متصل
🛡️
امنیت با رمزنگاری WPA2 و فایروال داخلی
🚫
مسدودسازی سایت‌ها، سرویس‌ها و برنامه‌های خاص
📶
مدیریت پهنای باند، فیلتر تبلیغات و جلوگیری از Torrent
🏨
ساخت صفحه ورود (Captive Portal) مانند هتل‌ها و کافی‌شاپ‌ها
⚡
اجرای خودکار هات‌اسپات پس از روشن شدن ویندوز
💡
یک ابزار رایگان، سبک و کاربردی برای خانه، محل کار، دانشگاه و سفر.
🔗
دانلود:
https://mypublicwifi.com
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6875" target="_blank">📅 20:48 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
