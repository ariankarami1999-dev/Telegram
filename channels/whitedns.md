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
<img src="https://cdn4.telesco.pe/file/doUp3H7mJKthIghGPblu8DFM4kWjwG8l12FQmZtCCDGaMWYYv2-5bRDzAjw0viZKdq7zfBnABGnTiiD5A7OgsEnf45WuNF5SUWDWgq8JRv6lJqAGWVFCLKvwfUkbyG6SlQrjDN4WWFRcbHYGrq87TF26ANI-bokWN7ZpWYrregN3kcE_qkfyyHGTf3Wzygu9urRpHrX63f5ernqscaBfENlW4JqHrDy8Ye3MbwQh_w5_EJgDdR6jSCgdMFzLB14nUoked4HCXsJTWWt8A_RqeNLcWtHvU0qwVgIsNwevGkTvUnqc-c7au-v3z1lhTqCPB4AfRvkbKePLxcEV4q7huQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 107K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 20:15:07</div>
<hr>

<div class="tg-post" id="msg-1132">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">White DNS
pinned «
وضعیت اینترنت چطوره ؟
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1132" target="_blank">📅 10:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1131">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-poll">
<h4>📊 وضعیت اینترنت چطوره ؟</h4>
<ul>
<li>✓ فرقی نکرده</li>
<li>✓ مختل شده تا حدی</li>
<li>✓ به شدت دچار اختلال شده</li>
</ul>
</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/whitedns/1131" target="_blank">📅 10:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1130">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1130" target="_blank">📅 10:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1129">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsTC6I44q40XBvu2q29n8XZLI6piFERlooR0l1yFIeKfSMJ52pSeMNmGYzuhs3grQQTdje_faItOCmULmbm08oeyPWps-wpja-12u-uNJeuMuxPsODCRD2Vm24yTl_pq8DbdO0naYaDn6dKl4nVF6yOPE6HHRMd_yAcxfk5pT9ILcHBtfupvMfYJb441q1MY78_pU0sIPIovUlc_BszAcKE8ZO_Uz6dqYzJiPttkTwC2_zL7tS5mxubuBIF62cohY8GkxN2oChh5SIZeRPgAiIO2sJn3u0TBwwGbREKbaGd6m9myOTcGEL1VaVYpGg2YBXgKLfOIDPUfBmxum2Gn_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/whitedns/1129" target="_blank">📅 17:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1127">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1127" target="_blank">📅 14:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1126">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/KThDCLMz73eyNY_nPcteeaufboOTp0qv1cb958LTwG-DMM5EYs4VHmSQmxaXNVInCOmmCQH93CXvBhWwOB3FeeNDYrWlJ_e9cyEsAqkjmZYkC-Amr7MTYSGzeu943OaBl8_JFuJVMDH5STEOlax2zJT60Xqo_EwS8_cVQRjciCxQ6MmNMw8tYOmlGSZHXml1DVcskbcbdfPE3q1V8Z6w-2a9Sqrv1UjkxuzcubUqIE2eeVjQZYmg8xdyc04FicIJcS6Xup1fZ848PhlgsPVOeKbxq2rHrARUS9Iyd5lV_hpDfcfFfQKGk_NkrBzYqx5MSkK1D7Wge0mlJ-fBf-rZ-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/whitedns/1126" target="_blank">📅 13:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1125">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🌎
آموزش کامل WhiteDNS Desktop براز مان قطعی اینترنت
لینک مشاهده ویدیو
https://www.youtube.com/watch?v=Mc--GlKw2wg</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/whitedns/1124" target="_blank">📅 05:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1123">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/whitedns/1123" target="_blank">📅 02:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1122">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/whitedns/1122" target="_blank">📅 02:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1120">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge
https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/whitedns/1120" target="_blank">📅 10:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1119">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🛡
معرفی CoreForge برای iOS فیلترشکن ساده و قدرتمند مخصوص آیفون  دوستان عزیز،  اپلیکیشن CoreForge برای iOS آماده تست عمومی شده و می‌تونید از طریق TestFlight نصبش کنید.
📥
نصب CoreForge از TestFlight: https://testflight.apple.com/join/u1vfEHur   CoreForge برای…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/whitedns/1119" target="_blank">📅 10:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1118">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/whitedns/1118" target="_blank">📅 10:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1117">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♨️
معرفی ربات جدید WhiteDNS برای راه‌اندازی و مدیریت سرور شخصی MasterDNS
♨️
ربات جدید WhiteDNS آماده استفاده است.
👉
@WhiteDNS_installer_bot   این ربات به شما کمک می‌کند بدون نیاز به درگیر شدن با مراحل پیچیده نصب، سرور شخصی MasterDNS خودتان را روی VPS راه‌اندازی…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/whitedns/1117" target="_blank">📅 06:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1116">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNKFZvJI29mpqopUodIieSLfE0zklU8R238rEQJCh2rbebbAMSshTZcHR1jGudny_BGXviOxwFsMeM-Ud9G6twmsBUQbY1n9GHn5euCTsS1Y4SGMTvfJhuYNKJeKmKrYNYAJ60b5s-__LDtOCNRUJvcn8f_GVQdhCcgx-qT_6rCtuIpnimaJQsE6EGFptoFijgcFvcopHeEspL5ybSUy4EqFn7BdbSOJZACM--z6-f-81tDTsJD_hxXkWEsRMdMTWo-_ODQ_Un8dPusUwWehWKewDSmQtww5wUe-o0SzvCkJbcdjnbt2E7r4QmAG1QYycAj0gX6bYnI1oatvNdZ3Jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/whitedns/1116" target="_blank">📅 06:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1115">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/whitedns/1115" target="_blank">📅 10:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1114">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/whitedns/1114" target="_blank">📅 04:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1113">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/C3vwoLIZZbYHPJaopbJvOvzxROz4jlCGu9gaVduUPZulW-wu5OcB1Y-iKr-NKsk7JMfsH4D14i7TiYznRu065DwpGSYGNmM06tz74p4a3SNh6mG_LLqDWIlEo7ZRu_f1RpjtHoZTS594C4tJ9qQ-YJxCDwcSccX9CqTWT95exh-xbr7jfc9WVU0tezFleCjUnrkpWCR7-iINfQEH_536f8xYmZY5wM3A4OnOlcXxX0WtbOCnwZOpZY_XbmVMXlUWzrJPEk1tjVxUapln82aMArr2aZNyDvJCaIka8G7PAszAAgbL85vna_u-jY9-FF7UHo9CsJP_Yi_YV52C6jLtPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/whitedns/1113" target="_blank">📅 20:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1110">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/whitedns/1110" target="_blank">📅 19:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1109">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سلام
❤️
توی این آموزش، تمام بخش‌های برنامه V2Ray را از مبتدی تا حرفه‌ای به‌صورت کامل بررسی کردیم؛ از اضافه کردن کانفیگ و Subscription گرفته تا تنظیمات پیشرفته، Routing، آپدیت برنامه و حالت‌های مختلف Tunnel.
🇺🇦
لینک آموزش در یوتیوب:
https://youtu.be/i1-XenoSalk?si=5jbQK3BrGAe4ctsu
اگر موضوع یا نرم‌افزار دیگری هست که دوست دارید آموزش کاملش را ببینید، داخل کامنت‌های یوتیوب یا گروه تلگرام پیشنهاد بدید تا برای آن هم آموزش تهیه کنیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/whitedns/1109" target="_blank">📅 18:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1108">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/whitedns/1108" target="_blank">📅 04:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1106">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy
فیلترشکن قوی و پرسرعت برای تلگرام
https://www.youtube.com/watch?v=pyvB6VSPhwg
@WhiteDNS</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/whitedns/1106" target="_blank">📅 19:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1105">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/whitedns/1105" target="_blank">📅 16:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1102">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">↗️
تعداد کانکشن های موفق WhiteDNS VPN در ۲ هفته به ۱۰۰هزار رسیده
.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/whitedns/1102" target="_blank">📅 15:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1101">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5xrMhkl-gitL2JvVZd3_OK7WlVKlxtCwW8G6LJTzyaSHnaKB_3DEH3Sw0PCPJAcKEFmdFm46Gp2vKjCyxaektVyVZMcg_yQP3i3afe7gWMPoKOrHEDT8Jflep4t-aju7yS7HsJkhUoyLJg-p1nCuKk174vxCc5Kttc_8jQ8eGYjmUowawCfQugLQ9DFn_HN8Vj3s5gpriOIMkJT6fWBBpFetoAxHwD8B65qwAMZ1F3Lw4EQ73C5oOwB5HYC1pYN23dgVLEedUeNwiK8hb19WkYhN8s10Av-wVOb6kpMI-F1msOSR_Vi6aAX0jLsf0_ZZigvKu-UH-1AQobe5lPxZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📇
دوستانی که امکان اسکن ندارند، می‌توانند از تاپیک «IP تمیز» در گروه استفاده کنند. دوستان دیگر IPهای تمیز را آنجا به اشتراک گذاشته‌اند و می‌توانید از همان‌ها استفاده کنید.
لینک گروه
https://t.me/+-Uc2AHI2d8Q2MzA0
آموزش استفاده از IP سفید
https://youtu.be/N5hKuWXp37w?t=1092&si=mdL0Q8Q9H039IAiL</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/whitedns/1101" target="_blank">📅 08:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1100">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=mbW4DTcpESZxZ_H7aTcIULRuKIkGBRsPa5JTqL911sjUlRNWI0U8Xqr1HbBwwdkuazLzvAXSdQ22GSOBqvNYKvSFjCj84m_6bVFPnL3kMUAdg-fKVj6PMSLZASJwNYZG0W_47kDDgmpDQBwJfpy5llUUz0cA0OQf8OXRYcwzPAmSCBvxE1C2p6LMHqKsO8yAhsUlDD0Z61ruYaC-ad1h8p12GeS8i00SUUBOFh9UXSbvA2jzP7pZgXLTv3Wr9QAt8FbmbtqqFjGsBW0lGpyOnd4k1cKKkhoW4e1ZS7g4VpvOn0PZ-5iUHz5AJJb35oUYDPLs4pKfZHoftVxUgOAqbYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=mbW4DTcpESZxZ_H7aTcIULRuKIkGBRsPa5JTqL911sjUlRNWI0U8Xqr1HbBwwdkuazLzvAXSdQ22GSOBqvNYKvSFjCj84m_6bVFPnL3kMUAdg-fKVj6PMSLZASJwNYZG0W_47kDDgmpDQBwJfpy5llUUz0cA0OQf8OXRYcwzPAmSCBvxE1C2p6LMHqKsO8yAhsUlDD0Z61ruYaC-ad1h8p12GeS8i00SUUBOFh9UXSbvA2jzP7pZgXLTv3Wr9QAt8FbmbtqqFjGsBW0lGpyOnd4k1cKKkhoW4e1ZS7g4VpvOn0PZ-5iUHz5AJJb35oUYDPLs4pKfZHoftVxUgOAqbYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">https://www.youtube.com/watch?v=Z069VNFAgAc
ایجاد بی‌نهایت آدرس ایمیل با یک دامنه روی کلودفلر
📧
آیا می‌دانستید می‌توانید با استفاده از قابلیت Email Routing در ، بی‌نهایت ایمیل شخصی‌سازی‌شده برای دامنه خود بسازید و همه آن‌ها را در یک صندوق دریافت مدیریت کنید؟
در این ویدیو، نحوه راه‌اندازی این سیستم کاربردی را یاد می‌گیرید که برای مدیریت بهتر ایمیل‌ها و جلوگیری از اسپم عالی است.
@whitedns</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/whitedns/1100" target="_blank">📅 17:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1099">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/whitedns/1099" target="_blank">📅 15:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1098">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/whitedns/1098" target="_blank">📅 11:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1097">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/whitedns/1097" target="_blank">📅 14:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1096">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtNHTBol0BUD6kFfYaTNmvNwHZDles4oAWkR-_vwjAnk5q5ZROu0ysLsBB8-15Kl-ZTkZQbxPfPIvYTjwDNZkKgaWfMIqUVm-n5ASuMDwy_xsYxF2HfAar3JaTabzpza2Tt5utP3AwYj616CuogKHJQfvUS9W83DEaPFHiCFM-9H1zhPQOD9prCwR0iqSSTB9anBJiho2iDFO-1l-LcknILExO8CnD8dVqnK2YGUyG5N_eqyeoFP-Y5ZqX8bVeoeEjibGlwHUjms_TqLHkctRa--hvHf5AH8TUFbfSJxmfPqZS9gpkLCXU0pYkzyGHHDAVQMjR2lTLW1Rv_jK-_ifg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/whitedns/1096" target="_blank">📅 10:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1095">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/whitedns/1095" target="_blank">📅 05:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1094">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/whitedns/1094" target="_blank">📅 05:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1093">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/whitedns/1093" target="_blank">📅 05:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1088">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS Desktop  منتشر شد
👆
👆
👆
👆</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/whitedns/1088" target="_blank">📅 11:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1082">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta6-linux-amd64.deb</div>
  <div class="tg-doc-extra">19.1 MB</div>
</div>
<a href="https://t.me/whitedns/1082" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/whitedns/1082" target="_blank">📅 11:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1081">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3ij-nl0pKVkMLcpy7vWQaVuYDx7LpMFVHbubyK_tbeRqfEMqv954pyS6j27vc5SWTzKVVhFYLUJsHwQF6pugI6vKxEZFSJCpOuyMspjKqCGqY_ptXI1AHu_ApIZl8hY4hVZAnxhJSH19fA1dThSXjFQyhpGDOe-WJINYYdcitapxTaXgE-K63-Q1oVKwh4L25EKImlIrRRzwq2gdLM8cICEt-w2WA0e7ogRr5_ubKDk6HWzv5lisOUxC_oMEUZgNXO4pp20s2_Kc91A28gi0q6r96u3-UTL4dg8e8YM9Q-igrJiN501u47qPAfdkvbea6Qp4FcZaN2e29ekHoLM7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/whitedns/1081" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1080">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/whitedns/1080" target="_blank">📅 04:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1079">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fi0XAWG7MCwBqKYI0NSGkNet46lH14BPxALKMytQykaI-YJUeONotVyebkFRR0-BtEzWLOA9Xhp9yTVfbMNpleawtlnK6lZHIG51ezSkSyvtsQcs4NdxfoHpcvTw1hIkQ3dh0Dbqpza88v9-LJlqJxUoPpJfwqV5PL_orCNsKa58bzvc8AKpllsYet-WwbUUvOLO5uOUOcnxpz85Igw0YeyLjmQM3Xgcp34invMcNwijr52vleXTmT4AuOkDNo-HXlVZeYhe4avoTXjLX4B_5VNX3WPCOb_4WSfLY2SGSiaiOVYsYS9qi-2AfdMVhgGfDc-MpFxctwbtIq0Wy00fnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
ورژن جدید WhiteDNS Desktop تقریبا آماده شده
در این ورژن همان وی‌پی‌ان داخل اپ اندروید
برای ویندوز، مک و لینوکس قابل دسترسی خواهد بود.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/whitedns/1079" target="_blank">📅 16:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1077">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚀
اسکنر WhiteDNS  اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن. https://github.com/WhiteDNS/WhiteDNS…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/whitedns/1077" target="_blank">📅 03:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1076">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5-Zsmpxcwsh9qf67kgCtcT9Qc9jnYcH0U_E100vd3eBvJYUF8Rhjn9ERn-HF9VVyccDO0U4DGmpvIE4ayAI6DWOygNdJOsBI0DNSfvwegenQkKXgVW0z9RlCEsq2DIlHjpgr_OBE_Wim14BwuiUwPEnl6TghfTuyl8L8COxEU04kcxHBApcccD6XMHtzvBhQfcC8cM1o4_tDn3kDMhJrNnFlFP_SijOATQoK9SeQawYrEA2Vj0xyajeikMjZ6Buj8cklq_mQosen4HcGWiO37citrtxhdOaY3Yo_Oo5_R1LwyWIhdZeAK8fxkc3LGLBgEb-Qyw_FXfhw_Q1PFKRLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/whitedns/1076" target="_blank">📅 03:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1074">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">White DNS
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1074" target="_blank">📅 17:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1073">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOl7pTPd2P2eA43YRbXnkTROcBBkNNB1T6OiTJsa804E_daP3CrVCu5aSJyP7yTG-0nCD4NDbc3-BhK3Ug0AUat6vjTazu1XNzDq5RPtZQh0Npec2jZcmjnUaxJikhNL4aq6Hfbk4EPGoZ4nRG4--Lu_FmCCW1VBGHpK5Q6Yjw47JxVYQaCIj3pgXO-MoTwX1q3uXlAXs6CHfCBkl1pPrKgyuJaA9T42ntVEDiMcEZnxz27vvnkyPbUusFCsfkv-4HYwMJ2hpA6p5gHPmrgtAupLzs0ZfqsCmA1lpvDB4eUi5deXVwpFw3TSJalkgQWK8zKmskco1Yen-_uq0XU2xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا شد
😎
۷۰۰ اتصال موفق در ۳۰دقیقه گذشته.
ممنون از همه دوستان که کمک ما تست کردند.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/whitedns/1073" target="_blank">📅 16:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1068">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/whitedns/1068" target="_blank">📅 15:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1062">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS VPN 0.0.6 منتشر شد
👆</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/whitedns/1062" target="_blank">📅 13:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1057">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.6-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/whitedns/1057" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/whitedns/1057" target="_blank">📅 12:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1056">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txRqL9wGaZgaukD3zX2M7dXj331Jb-8E-64cjw221ONpSFE3BZdJPASc308nTreeHFBXmq7iMGpXjyEWmeloN5IS4lPPeAdBolGc6LK1l7qr_rX8i2MqzSDihSWg-rFbWSJCfEWFZolXzESRN0yOmMHWrDIaQkGmPXHMl0g8aEdXdzxLf8JxZKIOM7R-GvrdEZA7W60ICaia1APtwKZkwsEnI5te-wR3zE44J72PuJev7EuNeAfHJY6yJIi9No7ZsJOeyBlQXVFHr4VXXCog8a7_Ro6A8aZtdbYf-XeoOjfL2lPYvSKVdQRlNXA1u8jgUJy-Ea_4hps098kcjSy28w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/whitedns/1056" target="_blank">📅 12:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1055">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/whitedns/1055" target="_blank">📅 08:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1054">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/whitedns/1054" target="_blank">📅 13:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1052">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یکی از اولین آدم‌هایی که از این پروژه حمایت کرد،
ویکی‌تجربه
بود. زمانی که اینجا فقط حدود ۱۰۰۰ نفر بودیم.
شاید خودشون هیچ‌وقت ندونن، ولی با به اشتراک گذاشتن پروژه، یکی از کسایی بودن که به ما انگیزه دادن ادامه بدم. بعضی وقتا یه حمایت کوچیک، بیشتر از چیزی که فکر می‌کنیم روی مسیر یه نفر تاثیر می‌ذاره.
خیلی وقته دیگه خبری ازشون نیست. حتی دیدم دامنه سایتشون هم تمدید نشده.
کار درست انجام دادن توی ایران سخته. درست موندن و باوجدان زندگی کردن هم سخت‌تر.
من حتی این عزیز رو از نزدیک نمی‌شناسم و اسم واقعیشون رو هم نمی‌دونم، ولی همیشه قدردان لطفشون بودم.
امیدوارم هرجا هستن، سالم باشن و حال دلشون خوب باشه.
🥲</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/whitedns/1052" target="_blank">📅 16:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1051">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OfEaj7lpm1vh4oezD2f1c5YTBvmqEtlpxXYVcQ2A3o8NJsxBRLGfWQyKRZZBG5Vxx--eZYsfczURf2mxQEFwK3ieCIwD2D6FXbd87rIcxSwbedDNSPJ3GHr3cPs1kleiDNOzEhkLY-hHpnHS8C1V7KobqAQCGKObkIoWVgPuaGkpNXs5Kellt2xayD5LBtlp2E1oK-_9wNXx2ffDCU0KAvdElNZXXpLqOcgTbKLiLWb6kn9zp3Bp3KBd2qIIbZtOkpQCdmEtZa0163eN7pFpcLkCwSQwmj15UTcBaRE1_dLt46FFa77F_LSvwgbckIIFmwKPH20-Cjk30hvTQ8VE0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویکی تجربه یکی از معدود گروه‌هایی بود که بدون هیچ وابستگی و فاند و رانتی، محیطی رو فراهم کرده بود که افراد نظر واقعیشون رو راجب شرکت‌های ایرانی بگن و نظر بدن.
سر همین خیلی از شرکت‌ها می‌گفتن که کامنت‌هایی که راجب ما گذاشتن رو پاک کن وگرنه شکایت می‌کنیم و فلانت می‌کنیم و... یا حتی می‌گفتن بهت پول میدیم، اما قبول نمی‌کرد.
و همینطور یکی از عواملی بودش که باعث شد آموزش‌های من به دست خیلیها برسن، چون همیشه مطالب رو share میکرد و با وجود هزینه‌های سرسام آور سرورهاش و شرایط سخت مالی، توی قطعی نت کنارمون بود.
و آخرین پست کانال تلگرامشون توی
تاریخ ۲۷ مارچ
(۹۰ روز پیش و اواسط جنگ) بود و همه نگران بودیم که نکنه اتفاقی واسه‌ی مالکش افتاده باشه یا دستگیر شده باشه.
و نتونسته دامنه
https://tajrobe.wiki
رو تمدید کنه. امروز دیدم که دامنه‌ی ویکی تجربه توسط ابرناک گرفته شده(احتمالا یکی از شرکت‌هایی که تهدیدش می‌کرد). و در عجبم از اینهمه بی‌شرفی، که میراث شخصی رو که مشخص نیست مرده یا زنده‌ست یا دستگیر شده یا... رو برداشته و اسم تمام اون پلتفرم رو گذاشته انتقام‌گیری.
امیدوارم که حال ویکی تجربه خوب باشه. دامنه و اینها کمترین اهمیت رو داره</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/whitedns/1051" target="_blank">📅 16:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1050">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">↗️
تعداد کانکشن ها موفق WhiteDNS VPN به ۱۰،۰۰۰ کانکشن روزانه رسیده .
✍️
در حال حاظر تمرکز اصلی ما روی اضافه کردن وی‌پی‌ان به نسخه ورژن ویندوز، مک و لینوکس هستش.
✍️
مواردی گزارش DNS Leak توی کانکشن‌ها داشتیم. درحال آماده کردن سیستمی هستیم که علاوه بر تست‌های سرعت، امنیت و پایداری، تست DNS Leak  هم از کانفیگ ها گرفته بشه.
ممنون از همگی
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/whitedns/1050" target="_blank">📅 10:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1049">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-poll">
<h4>📊 به ورژن جدید  WhiteDNS VPN تونستید وصل بشید؟</h4>
<ul>
<li>✓ آره</li>
<li>✓ نه</li>
<li>✓ ویندوز یا IOS استفاده میکنم</li>
</ul>
</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/whitedns/1049" target="_blank">📅 13:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1043">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-armeabi-v7a-release.apk</div>
  <div class="tg-doc-extra">33.1 MB</div>
</div>
<a href="https://t.me/whitedns/1043" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بیلد کامل اندروید SenPai Scanner، با تشکر از
Hidden-Node
عزیز</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/whitedns/1043" target="_blank">📅 02:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1042">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">34.7 MB</div>
</div>
<a href="https://t.me/whitedns/1042" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">به زودی نسخه یونیورسال هم ارسال میکنیم.</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/whitedns/1042" target="_blank">📅 18:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1041">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🛡
چطور آی‌پی اسکن بکنیم؟
یک آموزش براتون ساختیم تا بتونید با اپ SenPaiScanner روی گوشی اندرویدی خودتون آی‌پی های کلادفلر یا رنج های خودتون رو اسکن بکنید.</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/whitedns/1041" target="_blank">📅 18:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1039">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS VPN 0.0.5 منتشر شد
👆</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/whitedns/1039" target="_blank">📅 09:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1034">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.5-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/whitedns/1034" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/whitedns/1034" target="_blank">📅 08:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1033">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhzD28tI9w2MR5HqY45u1ioy4-MPgj4Jp6k8vrUoLiF6jJe-wJszF34FD5SsoLqnFh3R0qKfSPCwOE4z8F_dDUuFUoZtNidlX7g1_6UF4RHE50nMCRYLW6AMniXGKm53SaTIsu3nNjlGTSlqY9iAAO0WA9dmbuY4d-gSSTt5Rq2Fffj8hemX5g99BdPjy1BZUFJ4WNfEz0NzG2Je6dhNQ4drp94MfqtEK9Akf914PnI9bam3o63rZYK1DuQ-uqD7ks-Pz11aCvJDrjQ-WdmjeVzxiEewCAvV6m31Wmen3m_n3SnFoToh3PggIPFWXyPwPCYWkUB0IvP0UzAokHbDjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS VPN 0.0.5 منتشر شد
توی این نسخه چند تغییر مهم داشتیم تا اتصال راحت‌تر، سریع‌تر و قابل‌کنترل‌تر بشه:
• موتور اصلی اپ از XRay به Mihomo تغییر کرده
• تم دارک به اپ اضافه شده
• امکان اضافه کردن تا۵ آی‌پی تمی در بخش IP Fronting
• رفع مشکل «کانکت میشه ولی چیزی لود نمیکنه»
• اتصال سریع‌تر بعد از قطع شدن، با استفاده از کش
• اضافه شدن دکمه Refresh برای گرفتن کانکشن جدید و شاید بهتر
• نمایش سرعت دانلود و آپلود
• نمایش آی‌پی‌ای که در حال حاضر به آن متصل هستید
اگر برای اتصال مشکل دارید، احتمالاً باید برای خودتون آی‌پی تمیز اسکن کنید و داخل بخش IP Fronting قرار بدید.
تیم ما همچنان در حال تست و بهتر کردن اپه تا اتصال پایدارتر و ساده‌تری داشته باشید.
ممنون که همراه WhiteDNS هستید
❤️
@WhiteDNS</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/whitedns/1033" target="_blank">📅 08:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1032">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دوستان
👋
بچه‌های تیم به صورت مداوم در حال اسکن و بررسی IPها هستن تا همیشه بهترین و تمیزترین IPها داخل اپ در دسترس باشه و شما کمتر درگیر اسکن کردن و پیدا کردن کانفیگ مناسب بشید.
هدف ما اینه که تا جای ممکن فقط اپ رو باز کنید، یک دکمه بزنید و متصل بشید.
اگر فکر می‌کنید قابلیت یا امکانی هست که می‌تونه تجربه استفاده از اپ رو بهتر کنه، حتماً زیر همین پست برامون بنویسید. اگر با مسیر و هدف کلی اپ هم‌خوانی داشته باشه، با کمال میل بررسی و به لیست توسعه اضافه می‌کنیم.
ممنون از همراهی همیشگی شما
❤️
@WhiteDNS</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/whitedns/1032" target="_blank">📅 13:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1031">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1031" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1030">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سلام به همه همراهان عزیز،
متاسفانه یکی از اولین اعضای خوب خانواده WhiteDNS که از روزهای اول قطعی اینترنت خالصانه در کنار ما بود، به علت بیماری سرطان از میان ما رفت.
از طرف تیم WhiteDNS، این اتفاق دردناک رو به خانواده، دوستان و همه کسانی که دوستش داشتند تسلیت می‌گیم و آرزوی صبر و شکیبایی داریم.
یاد و خاطره‌اش همیشه در قلب ما می‌مونه.
🖤</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/whitedns/1030" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1029">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود رفقا...
پروژه نهان که قبلا متین معرفی کرد رو محصول داداشم دکی واسه دسترسی رایگان به اینترنت آزاد با روش ورکر رو بلدید دیگه؟
حالا میشه آسون تر حتی واسه کسایی که مبتدی و هیچ ایده ای ندارن هم ساخت با کمک ربات:
@itsyebekhebot
شما وارد ربات میشید ساخت پنل نهان رو میزنید وارد سایت کلودفلر میشید و طبق راهنمای کامل پیش میرید و ظرف دودقیقه حتی کمتر با کمترین اطلاع و دانش از ورکر یا هر چیز سخت دیگه ای فیلترشکن رایگان خودتون رو بسازید به صورت رایگان
❗️
نکته:از بات ایمیل فیک هم داخل کلودفلر میتونید استفاده کنید:
@TempMail_org_bot
هر جا هم گیر کردید بهتره که به من پیم بدید
😆
آموزش ساخت پنل نهان
@yebekhe
👑
@xsparvin
🍷
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/whitedns/1029" target="_blank">📅 13:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1027">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🌎
نسخه جدید WhiteDNS VPN V0.0.4
⛏
در این نسخه • ظاهر اپلیکیشن تغییر کرده  • امکان اضافه کردن آی پی تمیز خودتون اضافه شده تا اگر اسکن میکنید با آی پی های خودتون به کانفیگ ها وصل بشید.  • پرچم کشوری که بهش وصل شدیدرو بهتون نشون میده.  • با کمک یکی از بچه های…</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/whitedns/1027" target="_blank">📅 15:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1022">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/whitedns/1022" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/whitedns/1022" target="_blank">📅 15:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1021">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAg18Km6YT9wbJj3nOwH8Pd-tk2tLScvF45I1jEV0_TgGMmbM-CTft4vGUyBAgs7p5nsP54--AoP5Lla9_9T_jI2NB9YKNg8wDQob2i-FerjKvJNGfG7woB5TKZo77uG7pqrIid-g3uuRQQla3ukPdc-90JfaW_GJR5Ck0tggrh-ObPp0Ai3Qq7fHI3pkAXiafVwxmZTCqYQbV1PUDzZM2MTuHQ5JUJ0DEcEDM-vmoJD8_v6RsjOcT0HjaI12b0eWTNANj3zmvNG4MR8sPhGVYpv6M8IxHPLuNGcLXzhqnOqnIyqZefMSbblnhinkEV7niKJaAWWPefQFP_Aw7pQng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/whitedns/1021" target="_blank">📅 15:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1020">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">34.7 MB</div>
</div>
<a href="https://t.me/whitedns/1020" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/whitedns/1020" target="_blank">📅 14:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1019">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sB80hMF5UfVVAry-qcqd73Go0PgJkg1GHlpHI56SvPiONhGDRnskpu-TqMwrR8pc2N2eaZLD9Nf0D8r-K5CZowzbGW78eGqICKLtpEfVY2ezL5SImc3anq2fDoPsrXA0D2whMdzC-1ZISaHttQZ2B5f-zdzd9O_19K27B9ZdxbVZNS6OgdxFi9KPaTvh6I0ATLc3QJrLeg_ZuF3nUboO3f0Gu7XALpqKTGQeKK7rAL2g_k8NUt8aKdSeeGpirl2ubvWCc67vYrGSrAQ7AFI67kjfwCqFHuz0dle3T4NbHjdpBsWK8kdM89NTxU7eghzLMIkpoNWQ0uqkLO8DoUoASA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از contributerهای پروژه‌ی senpaiscanner، دوست عزیزمون hidden-node، نسخه‌ی اندروید اسکنر رو توسعه دادن. طرز کارکردش دقیقا شبیه به اسکنر دسکتاپه. نصب کنید و یه تست بکنید
👇</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/whitedns/1019" target="_blank">📅 14:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1018">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-BPB-1.2.0.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/whitedns/1018" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌎
آپدیت جدید WhiteDNS BPB V1.2.0
در این نسخه مشکل ورود با Cloudflare برای بعضی کاربران رفع شد.
قبلا بعد از انتخاب WhiteDNS BPB در مرحله برگشت از مرورگر، گاهی برنامه پیام خطا می‌داد که کد ورود آماده نیست.
از این نسخه، برنامه لینک برگشت Cloudflare را نگه می‌دارد و بعد از تمام شدن بررسی قبلی، ورود را درست کامل می‌کند.
✍️
نتیجه:
ورود با Cloudflare پایدارتر شده و احتمال خطای برگشت از مرورگر خیلی کمتر است.
روش استفاده تغییری نکرده است.
@WhiteDNS</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/whitedns/1018" target="_blank">📅 12:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1017">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخدماتی حامد📱</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">آموزش (1).mp4</div>
  <div class="tg-doc-extra">15.1 MB</div>
</div>
<a href="https://t.me/whitedns/1017" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آموزش ساخت پنل BPB بوسیله برنامه
WhiteDNS BPB
😎
😎
😎
ارسالی ادمین am
❤️
برنامه نصبی مورد نیاز
👉
سلام برای ساخت پنل به این نکات دقت نمایید قبل از ساخت پنل شما به یک اکانت کلادفلر که تایید شده باشه نیاز دارید.
بعد از انجام آن وارد برنامه white dns bpb بشید به بخش dasburd  برید .
گزینه connect cladflarرا بزنید تا گزینه sing in cladflarنمایش داده بشود روی اون ضربه بزنید تا صفحه مرورگر داخلی گوشی باز بشود در نهایت با زدن گزینه ابی رنگ  در تصویر اکانت ایجاد می گردد .
بعد از اون دو گزینه نمایش داده میشه که شما باید برنامه white dns bpb رو انتخاب کنید سپس به تب bpb deployment برید و گزینه  create  رو بزنید تا پنل ایجاد بشه یک نکته دیگر که مهم هست .
اگر در حالت عادی به ارور برخورد کردید با یک vpn روشن وارد پنل بشید یا نت خودتان رو تغییر بدهید تا به پنل وارد شوید باقی مواردش مانند پنل bpb می باشد .
در صورتی که خواستید می توانید ایپی تمیز برای پنل خودتان قرار بدهید و از آن در کلاینت های خودتان استفاده نمایید.
@whitedns
❤️
اشتراک گذاری یادتون نره
🌈
‌‌
@hamedvpns
☑️
لایک   |   Like
👍
❤️
اشتراک بزارین   |   Share
⭐</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/whitedns/1017" target="_blank">📅 03:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1016">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/whitedns/1016" target="_blank">📅 05:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1015">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/whitedns/1015" target="_blank">📅 04:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1005">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">برای این ساب، ما هر ۳۰ دقیقه بیشتر از ۲۵۰هزار کانفیگ رو بهشون وصل میشیم، تست دسترسی، امنیت و سرعت میگیریم و بهترین هاشون رو تو ساب قرار میدیم. که خروجی بین ۲۰۰ تا ۵۰۰ کانفیگ میشه.
تمام این کانفیگ ها قابلیت این رو دارند که از Cloudflare IP هم براشون استفاده کنید.
بروزرسانی فقط برای این ساب جدید نیست. تمام آدرس های قبلی هم بروز میشن و همین محتوی رو دارند.
اگر ساب براتون اررور میده، احتمالا آدرسش رو فیلتر کردند. اولین بار با وی‌پی‌ان ساب رو وارد کنید.
ممنون</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/whitedns/1005" target="_blank">📅 10:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1004">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دوستان عزیز WhiteDNS
🤍
ساب جدید WhiteDNS برای اپلیکیشن‌های مختلف آماده است.
برای اپ‌های زیر از این لینک استفاده کنید:
💠
ClashMi, Clash Party, FlClash, Karing
https://sub.whitedns.shop/sub/mihomo.yaml
💠
V2Box, V2Ray, WhiteDNS Desktop App ....
https://sub.whitedns.shop/sub/base64.txt
آموزش استفاده از Clash Party را هم می‌توانید از این ویدیو ببینید:
https://www.youtube.com/watch?v=gMFH88yRghg
این ساب شامل حدود ۵۰۰ کانفیگ پرسرعت Cloudflare Proxy شده است که به‌صورت مداوم بررسی و به‌روزرسانی می‌شوند.
پیشنهاد ما این است که اگر از اپ‌های Clash-based مثل Clash Party، FlClash، ClashMi یا Karing استفاده می‌کنید، حتماً لینک Mihomo را اضافه کنید تا بهترین نتیجه را بگیرید.
@WhiteDNS
برای اینترنت آزادتر، پایدارتر و قابل‌استفاده‌تر
🤍</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/whitedns/1004" target="_blank">📅 05:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1003">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/n_8_i9ycNdG9iCeUAjMnqzivLPZi4NMdoQRzUNHBPyu7q18wDd0cF9xKVL7ZS15XvysKGZ4DC26jy1VAcQBvBANTZk99RjsDqA3K56-_4CR_R8Frt3rbIrnFa5p0C_x_JCyT-q9q4wvPoGwaQLzlkcVtXdYuOHZ0398J0CaTTxkntvel-8fN_4TWPAwO0WJn5VVn3J_b3ZIeY7PFo9Wpweuv4AykMN2wAb_PdAynAaucs6rlodX230JWdGrSOKERmvH-7ou7yIqFnXBvmmxEqFUC9OKukD5u-KUmuf3M2llol8JMySNu8ztkmE76AvKgEPTE6C1pBcQLDqcIO9iDQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما با این مدل افراد به نظرتون باید چیکار کنیم ؟</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/whitedns/1003" target="_blank">📅 19:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1002">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آموزش کوتاه استفاده از :   WhiteDns BPB  1.1.0
📱
📡
@whitedns
🔗
✨</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/whitedns/1002" target="_blank">📅 15:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1001">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">White DNS
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1001" target="_blank">📅 14:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1000">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">White DNS
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1000" target="_blank">📅 14:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-999">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/2df17bf874.mp4?token=j1HO3DlwVheiQRxV8ayDfms9GowKtgxDjWJlVXgd7yIKLop-5zkB39LTN2Qe_SPH7MqnJfcvJWApuN7VpXBDRK2lrrVjBxUG34OWheqoTCTZd2OSwIgZN-jZUPUQjV6MU_2IAyN_CiR7shvX4DZV0FXLzVqPXV4awuYIKukSEX8MMVeq4yZacSWRO2rMWnBZo0DdDCfa8IXzpqkalyT5o2toyjQdNk2N-mK17Z8R6VE6SmD4M5_cGXoZ8gWBdMDWB3-9XbLj79jjLTtwWO5-KlQnonAIKrPp51kW0PsDJ2U-IPjcAndWVeoFlO3bShbaF0GoMfp5pDXv0dTu01LXX4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/2df17bf874.mp4?token=j1HO3DlwVheiQRxV8ayDfms9GowKtgxDjWJlVXgd7yIKLop-5zkB39LTN2Qe_SPH7MqnJfcvJWApuN7VpXBDRK2lrrVjBxUG34OWheqoTCTZd2OSwIgZN-jZUPUQjV6MU_2IAyN_CiR7shvX4DZV0FXLzVqPXV4awuYIKukSEX8MMVeq4yZacSWRO2rMWnBZo0DdDCfa8IXzpqkalyT5o2toyjQdNk2N-mK17Z8R6VE6SmD4M5_cGXoZ8gWBdMDWB3-9XbLj79jjLTtwWO5-KlQnonAIKrPp51kW0PsDJ2U-IPjcAndWVeoFlO3bShbaF0GoMfp5pDXv0dTu01LXX4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش کوتاه استفاده از :
WhiteDns BPB  1.1.0
📱
📡
@whitedns
🔗
✨</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/whitedns/999" target="_blank">📅 14:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-997">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">WhiteDNS-BPB-v1.1.0.apk</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/whitedns/997" target="_blank">📅 13:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-996">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-BPB-v1.1.0.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/whitedns/996" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه ۱.۱.۰ اپلیکیشن WhiteDNS BPB
در این نسخه مشکل وارد شدن به
پنل  Cloudflare برای دوستانی که ارور داشتند حل شده.
پست اول هم آپدریت شد به این ورژن. پس اگر اول لود رو دانلود کردید دیگه نگران این ورژن نباشید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/whitedns/996" target="_blank">📅 13:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-995">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دوستان سلام :
تذکر !
مشکلات سخت افزاری و نرم افزاری گوشی شما فقط و و فقط توسط خودتون باید رفع بشه ، چون ما نمی‌تونیم کاری بکنیم ، مطمئن بشید گوشی شما آپدیت هست و مشکلات نرم افزاری و سخت افزاری ندارد
موارد زیر را حتما برای whitedns bpb رعایت کنید
۱.مرورگر دیفالت گوشی را روی فایرفاکس(که پیشنهاد ما هست ) تنظیم کنید و از مرورگرهای ناشناخته گوشی های مخصوصا چینی استفاده نکنید ،چون بسیاری از این مرورگرها مشکلات امنیتی داره و وبسایت های معتبر مثل کلادفلر به درستی اجازه دسترسی به اونها نمیده
۲.فایرفاکس را باز کنید ، توی کلادفلر login کنید ،
نکته : ایمیل شما حتما باید وریفای شده باشد
۳.حالا وارد اپلیکیشن whitedns bpb بشید و شروع به نصب پنل کنید و ادامه ماجرا ....
در صورتی که به خطا برخوردید اپلیکیشن را uninstall کنید و مراحل بالا را از اول انجام بدید
ارادت
تیم whitedns</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/whitedns/995" target="_blank">📅 13:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-994">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-BPB-v1.1.0.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/whitedns/994" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/whitedns/994" target="_blank">📅 12:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-992">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNSv7lV6k2Eh7SMljqZuLOX5ZPpOizDteqn1GxjV9IZqhlTIeoMZFVN_cD4RSn6lR51X7cIk8N6K5Sv0rS6NS1TkaFM0NxuCfCrVl2KQcZUQdIHsLdpOemzHmxmlZE8Fmu1NxX4kyDvl6Rq8I6-DCMD2lYrfHYbTEvpZiI1JYMogyQ8PYjpXOXaKdjN7uwlZi4uJ40tIFyT4gRvvz3CJ3rx0kxiFfadJITCw2nnvvCEFA8XjyXrX7w4N_IzqZLtJA5BzAOYcAM65_7ln5AthWkNbMkGmDjt7w9rKxDVACygq7F41spka_kCldwL-yN5XU33iMr0lP8F3vJlJ-iOlFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/whitedns/992" target="_blank">📅 12:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-991">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">در حال حاضر بیش از ۵ هزار نفر به صورت رایگان از WhiteDNS VPN استفاده می‌کنند و به اینترنت متصل هستند.
شاید این عدد در نگاه اول خیلی بزرگ به نظر نرسد، اما برای ما ارزش فوق‌العاده‌ای دارد. هر کدام از این اتصال‌ها یعنی یک نفر توانسته راحت‌تر و رایگان به اینترنت دسترسی داشته باشد.
از تمام کسانی که در این مسیر کنار ما بودند، تست کردند، باگ گزارش دادند و از پروژه حمایت کردند صمیمانه تشکر می‌کنیم.
❤️
دم همگی گرم</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/whitedns/991" target="_blank">📅 18:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-990">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQwjPG0LcySwu2Tf58DYOsnm9evmEQDxfa5XfU2YZrxZc3k0nmxS9o8P3rlzcANh1QalQ-LDmgTUMlEXfaf-_YBQUiujUejOcSAusgOp4nQgQ-1akuxoF4g-XM5gvDW-NVZg8psqkQmgUxtJggFRf2s7FHVtgD14bTr1q0Au3LFDRIK_MR6fROXQCEJyxf1k67bUoJCASmr9cSjRtWaTS-BNDD_ue-R_exCw6kSDvcodeTTkZM026HDAzCUQWTrsuOVnlXJXoKAOWl3Z8GQCORdZWwp3LpBrLARFB8F5ReuTocZ_WKOpOzEH6c3n9W37luyXm-TWdvetA82bwjldFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
در حال انجام تست‌های نهایی WhiteDNS BPB هستیم.
این همان نسخه‌ای است که در تست‌های اولیه بازخوردهای فوق‌العاده‌ای از کاربران دریافت کرد و برای بسیاری از افراد عملکرد بسیار خوبی داشت.
به دلیل محدودیت‌ها و قوانین Cloudflare، امکان ارائه عمومی این سرویس به شکل ساده و مستقیم برای همه کاربران وجود نداشت. اما حالا با WhiteDNS BPB هر کاربر اندروید می‌تواند تنها با گوشی خودش، پنل اختصاصی خود را راه‌اندازی و استفاده کند.
نگران پیچیدگی راه‌اندازی هم نباشید؛ همه چیز تا جای ممکن ساده شده و آموزش ویدیویی کامل نیز داخل خود اپلیکیشن در دسترس خواهد بود.
منتظر انتشار نسخه عمومی باشید.
🔥</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/whitedns/990" target="_blank">📅 18:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-989">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ما از روز اول قطعی اینترنت فقط شنیدیم
《اینستاگرام لود میشه؟!》یا《اینستاگرام لود نمیشه؟!》 یا 《اینستاگرام لود شد》
🤣
تنها معیار و ملاک سرعت لود اینستاگرام بده
🫠</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/whitedns/989" target="_blank">📅 13:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-984">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.3-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/whitedns/984" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/whitedns/984" target="_blank">📅 09:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-981">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jlge9HpQT2RzXOKvuD0NImnBZ602J0qwq8RwcufeTzMDQtHI30il-t8BmsXw0DUHD6v0WfroCyCuIqvTkxKWBeZnjOyt8K3C29_TMZhKpPEYZRgQngk2wZV_sCztpy5iW3lR_0ctBwmEeaImizhYSWRtuPqimtHuCREhYyliEr2z-sYNeAMyPDli10aZcDXW2A1ZTtZnEzXTqLAeHgJreB1NVSblmy0rAiRli--EWYx0ksKmzZtw9nMaWmA9bll8KiZCXwDdiIS2NLf6VWHFL6POwjLux6WFKiUJsQKI6kJCt6ORXjwPfVotAdSWW-RywmI1TzQ-oistHRziV6OgTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h_J8jtX90k9u--wo_5Ez3ufeTDvJkX92t9NuOV0YtKQUZXVC-nj_xcBh968RuqfFNuhZ7LjdoiQK-4PiYxduxIFH2EwRCsqMAKBK1hNXLlO9ckio9P7NqramD8tBF7t0-ZhlmkKhr6HY4ASF0V9tqBvMz58TAzILYITmUmoPGxbVHjoKgCoWEE9ih5XJNN7WS1FWEW-SXVjbtSmfCZ3uYvrX8RH64KK01GqohDq2YFB84yH_rymHAIqaDPCEDM7PtPQMejGGDjyMsn2QGxfI2H0qCK29MBW1Z4TmCPem3CqnBtOO2oJ-Ys-kQYMfcMEF0pjCKb45fB9j9-7osJFBug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXlQS3NwaxRvd8wd38mEwSLWW9_2jpkD5GLee57_niB5hIS_njlkeZ9K3RDKekA0hCeXDrBwVHcDjn3uc5Rkv5miiLhzdnvab0ojfpbEbMd8DvNs1CU2NOkYk9SCSsBzaFHmh-63MCjqTKbbaTeCCZp1gF5XWv1u3yTAe6B_Vn47ljKwVYdJ8mBTVoarYEfGA37KrXl97TPCFcg3PS0ZBBcTi1PkWKZaHzuDV1YBMBbugNFU5sCwEhclciVtO16wnMjMBj8_7DeKT9qA5ByaGhgoF_EFKw3Ztvokbmm0alj3kbulvxrutpNN7NzobposuQjLOBwGeypZJoOgZ0AYwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎉
نسخه 0.0.3 اپلیکیشن WhiteDNS VPN منتشر شد
در این نسخه چند قابلیت مهم به اپلیکیشن اضافه شده است:
✅
انتخاب لوکیشن برای اتصال
✅
انتخاب اپلیکیشن‌هایی که باید از VPN استفاده کنند. Split Tunneling
برای بهترین عملکرد، پیشنهاد می‌کنیم هنگام اتصال از گزینه Auto استفاده کنید. در این حالت اپلیکیشن به‌صورت هوشمند بهترین لوکیشن را بر اساس شرایط شبکه شما انتخاب می‌کند تا اتصال پایدارتر و سریع‌تری داشته باشید.
از همراهی و بازخوردهای ارزشمند شما ممنونیم
❤️
@WhiteDNS</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/whitedns/981" target="_blank">📅 09:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-980">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">داریم روی یک اپ جدید کار میکنیم به اسم WhiteDNS BPB که پروسه ساخت، مدیریت و وصل شدن به کانفیگ های BPB رو برای شما ها راحت تر می‌کنه
🔥</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/whitedns/980" target="_blank">📅 15:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-979">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-poll">
<h4>📊 آیا به نسخه جدید WhiteDNS VPN وصل شدید؟</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
<li>✓ آیفون/دستکتاپ دارم.</li>
</ul>
</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/whitedns/979" target="_blank">📅 14:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-978">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">لطفا تست کنید، نتیجه اتصال یا شاید تست سرعت خودتون رو برای ما زیر همین پست بفرستید.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/whitedns/978" target="_blank">📅 12:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-973">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.2-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/whitedns/973" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/whitedns/973" target="_blank">📅 12:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-972">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">همچنین در مورد اپلیکیشن WhiteDNS VPN، باید بگوییم که در حال حاضر تمام تمرکز تیم ما روی توسعه و آماده‌سازی این سرویس قرار دارد.
در طول ماه‌های گذشته، با کمک گزارش‌ها، بازخوردها و تست‌های ارزشمند شما، توانسته‌ایم به یک معماری پایدار و مقیاس‌پذیر برای این پروژه دست پیدا کنیم. این تجربه به ما کمک کرده تا نیازهای واقعی کاربران ایرانی را بهتر بشناسیم و راهکارهای مؤثرتری برای آن‌ها طراحی کنیم.
هدف ما تنها ساخت یک VPN دیگر نیست؛ بلکه تلاش می‌کنیم سرویسی را ارائه دهیم که از ابتدا با در نظر گرفتن شرایط اینترنت ایران، پایداری، سادگی استفاده و تجربه کاربری مناسب طراحی شده باشد.
همچنین تمامی سرویس‌های مبتنی بر DNS ما در حال حاضر در وضعیت پایدار و آماده‌به‌کار قرار دارند تا در صورت بروز اختلالات گسترده یا محدودیت‌های اینترنتی، بتوانیم در کوتاه‌ترین زمان ممکن مجدداً این سرویس‌ها را در اختیار کاربران قرار دهیم.
از همراهی، صبوری و حمایت شما سپاسگزاریم.
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/whitedns/972" target="_blank">📅 08:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-971">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سلام خدمت همراهان عزیز
🌹
ساب‌های WhiteDNS شامل باکیفیت‌ترین کانفیگ‌های عمومی هستند که در سطح اینترنت منتشر شده‌اند. تیم ما هر ۳۰ دقیقه یک‌بار بیش از ۲۵۰ هزار کانفیگ را مجدداً بررسی می‌کند، از آن‌ها تست سرعت و پایداری می‌گیرد و در نهایت تنها حدود ۲۰۰ کانفیگ برتر را در اختیار کاربران قرار می‌دهد.
با این حال، لطفاً در نظر داشته باشید که تمامی این کانفیگ‌ها عمومی هستند و توسط WhiteDNS میزبانی نمی‌شوند. ما تلاش می‌کنیم کانفیگ‌های انتخاب‌شده از نظر کیفیت، پایداری و امنیت در بهترین وضعیت ممکن باشند، اما هیچ‌گونه تضمینی در خصوص زیرساخت، عملکرد سرورهای میزبان این کانفیگ‌ها وجود ندارد.
هدف ما ارائه بهترین گزینه‌های عمومی موجود و کمک به دسترسی آزاد به اینترنت برای کاربران است.
با احترام
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/whitedns/971" target="_blank">📅 08:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-970">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دوستان عزیز، ممنون از گزارش هاتون.
لینک ساب که از دسترس خارج شده بود درست شده و میتونید ازش دوباره استفاده کنید.
https://sub.whitedns.one/sub/mihomo.yaml
@WhiteDNS</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/whitedns/970" target="_blank">📅 08:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-969">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kx94ZIxtWgz1eshW8I7jZ8j0BWmW8gchika1JNHw9cSzewiRKp0y9YYJ5SxfmbjfI9S0Iwm_HZgsOaMZgmp2pd5lAhozn1ieI8To08hT3kisVcPE1TWgOgAhxKWQgvwbmqapHQWb3LyGKTcdpOqM4dm6GXc1LB2Dp3UsqvBAGNwppdX12nx0GTMLL0THAItTBZScrVZUCLsAWH4SknwSuzivDdiqzUztBnYhKWjtfXeHFhQZ6OHIbFDvP1c9dAEhBWeeC0jR5iQz7hKJ65CtCaFJ5dyKs_EgkJYI5KDQIw5wJcmyHTKsAHwWfBFkJ8rfQdfxWxTDodRHahpyf4pdDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/whitedns/969" target="_blank">📅 04:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-968">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVmgfnoZI5n014DzGaP9-SyHLHZQKCVt530-5wlEXpf6q7LXFG_rUUlBWii07GLZWMsEbxFuFW0Fqtz_tBLqxV2Hx8H_kacOaXHai1z2Jznbsgf4vzt8yF-Hn6rh1PToeDEnxzLS51f0RSDhEtgs9uOgcze_3V70s0SOyEiWdiEsGEiOVyYSPGPcwC9yi3l2bltV2-NfYUvhIp7MfwGzeX0-u1T-8DehpenXWNiRWDN5mcnyjscAqAgDbn723QfP0MKdejRKCuEW3fjRbj0wUpUsbKo6i_zZ6308cbFtaWrb4d3MtpVdiDJEAn6jJFI26EOL1ApE-IqxwmtQb1MZ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/whitedns/968" target="_blank">📅 13:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-967">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">این دومین نسخه تست همگانی اپلیکیشن WhiteDNS VPN میباشد.
لطفا تجربه، سرعت و مشکلات خودتون رو زیر این پست برای ما بفرستید.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/whitedns/967" target="_blank">📅 13:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-963">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-vpn-arm64-v8a-v.0.0.1.apk</div>
  <div class="tg-doc-extra">30 MB</div>
</div>
<a href="https://t.me/whitedns/963" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
نسخه جدید اپ آماده شده
در این ورژن شاید اتصال شما کمی کندتر انجام شود.
ما در حال تلاش هستیم تا در ورژن های بعدی سرویس بهتری ارایه کنیم.
ممنون
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/whitedns/963" target="_blank">📅 13:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-962">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ما راه حل رو داریم، اپ مناسب رو هم ساختیم. حالا فقط باید باهم تست کنیم تا به نتیجه نهایی برسیم.
به زودی ورژن جدید رو منتشر خواهیم کرد
❤️
ممنون از همراهی شما</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/whitedns/962" target="_blank">📅 09:10 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
