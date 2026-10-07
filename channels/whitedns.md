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
<img src="https://cdn4.telesco.pe/file/nAYZeSbIrEqOtyGFAO_BC4fYrArhAYFu75DQuDmWnpgOjLEqc19h8Yo4n2NRQegBnDp4kthy48-Dy9ozq-s-okcF-k1x0chh571sFqsGGk7f8fx7joreZ9zZ3IgBI_DMaF5__nn9z1OEFYlMCQFL2L2bqK2gW9yOVCZ5FOnmzliy3B9mX6H0PMsEGC92cJkMToV6zHSjF69gLUjv1niJULU9pbUNCsWUkH5CSOP5DV0qlmu66o2bJ0ZR213qrYdcioNh-Ww-ziVUoVMQ4q8HDS-35_O4P-3hSePoYlTRePAJfv7CK2E9-saGpNn8oqjO9OvC4I5evDaoXKtn841SAA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 107K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 20:36:45</div>
<hr>

<div class="tg-post" id="msg-1924">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔥
آپدیت مهم WhiteDNS
فایروال جدید، ترافیک DNS بالاتر از حدود ۶ کوئری در ثانیه را محدود می‌کند و همین موضوع باعث قطع شدن بسیاری از تونل‌ها شده است.
برای اتصال پایدارتر، برنامه را به آخرین نسخه آپدیت کنید
👇
📱
دانلود نسخه اندروید 1.6.4
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.4
💻
دانلود نسخه دسکتاپ 1.2.4
https://github.com/WhiteDNS/WhiteDNS-Desktop/releases/tag/desktop-v1.2.4
⭐️
تغییرات و تنظیمات پیشنهادی
🔹
محدودیت نرخ ارسال کوئری
در تنظیمات پروفایل CottenDNS، گزینه Query Rate Limit را روی ۳ کوئری در ثانیه قرار دهید. ممکن است سرعت کمی کاهش پیدا کند، اما اتصال پایدارتر خواهد بود.
اگر با اضافه کردن Resolverهای بیشتر سرعت بهتر شد، گزینه Rate Limit Counts را روی Per Resolver قرار دهید.
🔹
تصادفی‌سازی زمان ارسال کوئری‌ها
گزینه Timing Mask را روی Light یا Strong تنظیم کنید تا زمان ارسال کوئری‌ها تصادفی شود و ترافیک شما ریتم ثابت و قابل تشخیص نداشته باشد.
🔹
تعویض خودکار دامنه
اگر دامنه سرور مسدود شود، برنامه به‌صورت خودکار به یکی از دامنه‌های جایگزین دریافت‌شده از سرور سوییچ می‌کند؛ بدون نیاز به ساخت پروفایل جدید.
🔹
اتصال پایدارتر
پاسخ‌های جعلی Domain Does Not Exist یا NXDOMAIN که فایروال ایجاد می‌کند، دیگر باعث حذف Resolverهای سالم هنگام برقراری اتصال نمی‌شوند.
👀
محدودیت نرخ ارسال کوئری و تصادفی‌سازی زمان ارسال به‌صورت پیش‌فرض خاموش‌اند. برای استفاده از آن‌ها، تنظیمات بالا را فعال کنید.
🖥
برای مدیران سرور
ابتدا نسخه سرور CottenDNS را به آخرین نسخه آپدیت کنید:
https://github.com/WhiteDNS/CottenDNS/releases/latest
• برای استفاده از Domain Rotation، دامنه‌های جایگزین را در ADVERTISE_DOMAINS قرار دهید
• مقدار ZONE_NS را روی Nameserverهای خود تنظیم کنید تا سرور به کوئری‌های نوع NS مانند یک DNS Server عادی پاسخ دهد</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/whitedns/1924" target="_blank">📅 14:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1923">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مادر بزرگ ۷۰ساله من برای اینکه بتونه با بچش ۱۰دقیقه در روز صحبت کنه VPN استفاده کردن باید یاد بگیره.
باید استرس بکشه که الان قطع میشه، همراه خوبه یا سامانتل، باید بدونه سابسکرسپشن چیه، سرور چیه و ۱۰تا روش امتحان کنه تا به گوش من برسونه که 《مامان VPN من بازم قطع شده》
😭
لعنت بهتون که به دل کوچیک و بزرگ حسرت گذاشتید.
ببخشید یکم شخصیش کردم و میدونم این وضعیت دردسر هممونه و نه فقط من. شاید این در مقابل دردسر خیلی ها حتی چیزی هم نباشه.
خیلی از این متد ها مناسب افراد مسن تر با دانش کم نیست. تا جایی که میتونید هواشون رو داشته باشید
🥲</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/whitedns/1923" target="_blank">📅 13:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1921">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-GUI_0.8.0_x64-setup.exe</div>
  <div class="tg-doc-extra">19.1 MB</div>
</div>
<a href="https://t.me/whitedns/1921" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/whitedns/1921" target="_blank">📅 13:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1920">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zl2xrleKhPFJU8vCGW6PBgpybUFBwWMbSvzqUza02Tl4eYrgCYSAyHKbUzttxI67pbWoNyyGoqIh3a1-bUrJSvfx5kNpwyuccOTxPVFTNegbYDi8IIMvjAwbR0mOZbsCM-2AiPvbKmtBKYr6vmk0YWzwYONLrUzU4l80t9Ga2xaYmG0BzJx1n8NdLO_qeHs8TTdZcG8ULeWY6w9hlnRaL6POsqi1LFcEQh_usoaNIR6eBZPbidBhrbUZT5NEM6vgSExpOUQQLMhfZNSNp7vdmotLE6uUpa6FzszhtZMZXRvcfOCxtzpTnURz1VNg90fAbw-Nvs4kdOHmS_qeqaqZ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه 0.8.0 از Aether-GUI منتشر شد
👋
- آپدیت هسته‌ی Aether به آخرین نسخه
- اضافه شدن شبکه‌های Psiphon و Tor
- اضافه شدن MASQUE-in-MASQUE
- افزوده شدن HTTP proxy، upstream proxy و exit-country
🐱
دانلود از گیتهاب:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.8.0</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/whitedns/1920" target="_blank">📅 13:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1918">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/lgSDvP1cTMYErKHu0xSDHMJDCS7aZnteuceynInIw0uMkFK0y2yMOFvy7ZwhRhd-5AIw6TDYk6WSaYMvyARjUVXGNXN27Fg2dsICDpMGtvXwQ-0c6dvDCOycKPEjWrpfPOQwvlK0Jf3y2yLAbB_0LN_BbHPi2atr8yX71530MGxvfYg-VfyL1cwHfr5zaD_oTQsyv3wj8Z9mdAtvd7e8m54MhJEj89ADzE-ZwbbIH4ifo8wr-MEZP5OyfYryWx44iIkqbzmfOBUKvog214oG4HhKRPZN3i1ue2qCZnlH4CH7B0vD4iTv1M097CN7_U4pJDFd5RSbnSbqtZGtP3MHPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/Tg-dgZs2VMcdfES7q3SRQpXhUxkj1qA9KRd0ZM_2hqjYgb2RWg77KOCbGoUo8h9k0QdooirgKcRHv7wEyH_rQjKJ0Pvv8Omro12zjsitzOLbKXHPiCVp0FgInqVIqvnWZGrD4sU5xYO1b4yK81Z3aYUfNJmpceUceGs0a-e5weMvEPz9-yvPDYalMx-81-hwef5fhBHooLMrdKIIDpdNoXPWRXxvyuTkjf9iXUpk2EKvBab_UUX_TtfbJWWrwIYsJv8tmADxSwvxh9gOQoKnyevnYjcWB-sAkOtODtpT7VLvJr_04TzkdHMe_YKasDrOU31AIXgZRg3L-5GfqoVV6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان
🙋‍♂️
در نرم افزار
whiteaesther
اگر برای اتصال مستقیم با aether مشکل دارید، این احتمال وجود دارد که دستگاه شما به هر دلیلی روی اپراتور کنونی نمی‌تواند هویت WARP/MASQUE ثبت کند
📡
برای حل این مشکل برید routes  و اولی را روی تور  یا سایفون و دومی را روی aether بگذارید و دکمه اتصال را بزنید
⚡️
. صبر کنید تا سبز شود
✅
حالا شما هویت masque خودتان را دارید و می‌توانید از aether به تنهایی یا ترکیبی استفاده کنید
🚀
@whitedns</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/whitedns/1918" target="_blank">📅 13:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1917">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YseVohwmGFvDdl2ZJpFrEwZAuM9Or0ClIlA1IzMKsM4t7t7O5kOfJLFrne0xXrXa_hJraE7HItdDk96MFdCnMKwP4kcxhYLpArBiSOglHuXUU8N1IPyJv-q14m6Lxw4jcyMTF7DMkjhqnAxdKAQdXCz1LQjryQsC-43JC7oZF72e2yOEp-ueH8U01X7jq_ur7i9-LuPoMRkQb4qg91TwnoleW5zAq9Up3eUVN3LMZmt42WPBrInuNDw5_zz1g9ObdH4C43LdVrrW2_yd3QxT7t4ViWeEz5sfF37M_EyWFc44-Omo5eYUOWB4CwZU6RERBoyPRotOr_f0O0c0xLKKzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
اگر WARP محدود شد، چطور از WhiteAesther استفاده کنیم؟
⚠️
طبق گزارش‌های دریافتی، ارتباط UDP با IPهای کلودفلر روی همراه اول محدود شده است. احتمال گسترش این محدودیت به اپراتورهای دیگر وجود دارد، اما هنوز نمی‌توان آن را قطعی دانست.
این محدودیت می‌تواند اتصال
WireGuard و MASQUE H3
را مختل کند؛ با این حال، WhiteAesther مسیرهای دیگری هم دارد.
۱️⃣ ابتدا حالت خودکار را امتحان کنید
در تنظیمات برنامه:
🔹
Traffic → Coverage:
گزینهٔ «کل دستگاه»
🔹
Routes → Carrier:
گزینهٔ «خودکار»
در نسخه‌های دارای این قابلیت، برنامه مسیرهای Aether، Psiphon و Tor را بررسی می‌کند.
⚠️
اولین اتصال روی شبکهٔ محدود ممکن است چند دقیقه( تا پنج دقیقه ) زمان ببرد.
⚠️
۲️⃣ برای اتصال مستقیم، MASQUE H2 را امتحان کنید
از مسیر زیر پروتکل را تغییر دهید:
🔹
Routes → Advanced → Preferred transport → MASQUE H2
H2 روی
TCP
کار می‌کند؛ بنابراین بسته‌شدن UDP به‌تنهایی آن را از کار نمی‌اندازد. البته اگر مسیر TCP هم فیلتر باشد، اتصال برقرار نمی‌شود.
۳️⃣ امکان استفاده از IPv6 را حفظ کنید
🔹
Traffic → Addresses → IPv4 + IPv6
اگر IPv6 روی اینترنت شما قابل‌دسترسی باشد، ممکن است مسیر اتصال باقی مانده باشد. انتخاب این گزینه داخل برنامه، به‌تنهایی روی خط فاقد IPv6 دسترسی ایجاد نمی‌کند.
۴️⃣ تکه‌تکه‌کردن دست‌دهی TLS را امتحان کنید
🔹
Traffic → Advanced → Split the TLS handshake → روشن
این گزینه ممکن است در برابر بعضی روش‌های فیلترینگ کمک کند، اما مسدودشدن کامل IP یا TCP را برطرف نمی‌کند.
۵️⃣ اگر اتصال مستقیم جواب نداد، حامل را تغییر دهید
در
Routes → Carrier
حالت دستی را انتخاب کرده و
Psiphon
را امتحان کنید. گزینهٔ دیگر،
Tor با پل خصوصی obfs4
است؛ معمولاً کندتر است و ترافیک UDP را حمل نمی‌کند.
نام و محل گزینه‌ها ممکن است در نسخه‌های مختلف متفاوت باشد.
⚠️
هیچ‌کدام از این روش‌ها اتصال را تضمین نمی‌کند. بسته‌شدن WARP لزوماً به معنی ازکارافتادن کل WhiteAesther نیست؛ نتیجه به مسیرهای باز روی اینترنت شما بستگی دارد.
تشکر ویژه از
@patt_channel_x
@whitedns</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/whitedns/1917" target="_blank">📅 09:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1916">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">پروتوکل UDP هم به طور کامل روی ip های کلودفلر بسته شد (فعلا فقط روی فایروال همراه اول)
در نتیجه امکان اتصال به warp از طریق پروتوکل wireguard و یا masque-h3 دیگر امکان پذیر نمیباشد.
برای پروتوکل masque-h2 نیز، امکان استفاده از ECH از سمت خود کلودفلر بسته است، بنابراین در حال حاضر فقط با استفاده از IPv6 میتوان از این پروتوکل استفاده کرد.
روشهای جدیدی که بزودی منتشر خواهد شد امکان اتصال کانکشنهای TCP را به کلودفلر فراهم میکنند، در نتیجه، میتوان از آنها برای masque-h2، کانفیگهای ورکر، cdn و به طور کلی تمام اتصالات TCP روی کلودفلر استفاده کرد.
حمایت فراموش نشه
🙏</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/whitedns/1916" target="_blank">📅 09:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1915">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">PattNG v2.3.10-P59
منتشر شد.
امکانات اضافه شده
:
۱. مقادیر متد فرگمنت+فینگرپرینت اکنون به صورت آپشن تو خود اپ اضافه شده، بنابراین برای اجرای متد فرگمنت+فینگرپرینت کافیست:
address:
188.114.97.6
(or any clean ip)
finalMask: tlshello-0-len
fingerprint: unsafe
cipherSuites: semi-python
را انتخاب کنید، و دیگر نیاز به کپی پیست ندارید.
برای اجرای این متد روی کانفیگ‌های اتر نیز کافیست:
finalMask: tlshello-0-len
fingerprint: semi-python
را قرار دهید.
۲. اکنون امکان chain کردن کانفیگ‌های psiphon/tor/warp با هر کانفیگ دلخواهی به صورت
دو طرفه
برقرار شده.
به طور مثال برای chain کردن سایفون با یک کانفیگ دلخواه ابتدا باید یک کانفیگ psiphon-only بسازید و سپس از قسمت Add Proxy chain میتوانید آن را با هر کانفیگ دلخواهی به صورت
دو طرفه
chain کنید.
همچنان برای chain کردن سایفون با خود warp باید از همان منوی aether اقدام کنید (warp -> psiphon/psiphon -> warp)
۳. با توجه به فیلتر شدن دامنه دریافت کلید وارپ، اکنون میتوانید از طریق متد فرگمنت+فینگرپرینت (finalMask+semi-python) و یا حتی ech این محدودیت را دور بزنید و بدون نیاز به فیلترشکن مجزا کلید وارپ را دریافت کنید.
۴. به طور مشابه با توجه به فیلتر شدن دامنه masque-h2, اکنون میتوانید از طریق متد فرگمنت+فینگرپرینت (finalMask+semi-python) این محدودیت را دور بزنید و به پروتکل masque-h2 نیز متصل شوید.
امیدوارم حمایت فراموش نشه
🙏</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/whitedns/1915" target="_blank">📅 04:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1914">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pYvPjsdnZI8uo5ZxioR5sScs1weYvmoBRARS6ZXsm6Naj891V5gWAmxKgZnQWqQ0wiuoOKhKWbE0v9SByXJdJv133WBBFLvErMNRIqPo4HIRdLX03uHapJcR0T_tSlBrN24wU3u7d0QZjkTcSpOxOW112-uNkdEfOI0ec1EohWvnVFyUT8mHqtbElLLXZt1RD_O-oI56p6C9LGOg_PiQy5isnn13QJSEIslk_8EzWimilcU4bLuXdTHoeaNiCdMwViLjWwh1k5NiUYcYYbjiMOzJG7NkIMv7Dlvy1M-ZvdQq4WDz9C9igv2jb4gOXGMI-D04EUl0zWlw09bE_REN2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity
https://github.com/MatinSenPai/Gemini-Config-Checker
" دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید:
https://t.me/MatinSenPaii/2881
"
کانفیگ‌های رایگان زیاد هست، ولی کدومشون واقعا Gemini و AI Studio رو برای جیمیل خودت باز می‌کنه؟
این ابزار هر کانفیگ رو همون‌طوری تست می‌کنه که یه آدم استفاده می‌کنه: با حساب Google واقعی خودت، توی مرورگر خودت، از مسیری که واقعاً ازش وصل می‌شی. چون Google ریجن رو فقط برای حساب واردشده و بعد از لود شدن صفحه تعیین می‌کنه، تست‌های ساده‌ی «پینگ و API» همیشه همه‌چیز رو سالم نشون می‌دن و دروغ می‌گن.
🔹
دو حالت ساده و پیشرفته برای انواع شرایط
• ساده: کانفیگ‌های خودت یا لیست کانفیگ‌های رایگان (لینک، ساب، base64) مستقیم و بدون زنجیره تست می‌شن
• پیشرفته: کانفیگ‌های رایگان از پشت کانفیگ پایه‌ی خودت تست می‌شن (تو ← کانفیگ پایه ← کانفیگ رایگان ← Google)
🔹
تست واقعی ریجن
• ورود با حساب Google کاملاً لوکال، با Chrome / Edge / Brave خودت؛ نشست فقط داخل حافظه‌ی برنامه می‌مونه، چیزی جایی ارسال نمی‌شه
• AI Studio و Gemini جدا بررسی می‌شن و می‌تونی انتخاب کنی «سالم» یعنی کدوم‌ها
• اول اتصال سنجیده می‌شه تا کانفیگ‌های مرده زود حذف بشن، بعد فقط بقیه به مرورگر می‌رسن
🔹
پروفایل ضد فیلتر
• Finalmask (fragment)، Fingerprint، ALPN، Cipher suites و IP تمیز
• مقدارها رو از خود کانفیگ یا لینک می‌خونه؛ کپی‌پیست کن و تمام
🔹
خروجی
• «کپی با Chain»: کانفیگ کامل و مستقل، آماده‌ی PattN / v2rayN و Xray استاندارد
• خروجی لینک، JSON، و ذخیره در فایل
• انتخاب کانفیگ‌ها، مرتب‌سازی بر اساس تأخیر، و چک‌کردن دوباره
🔹
همه‌جا اجرا می‌شه
• ویندوز، مک، لینوکس: اپ دسکتاپ و نسخه‌ی وب (برای سرور)
• اندروید (APK): فقط تست اتصال؛ اندروید اجازه نمی‌ده برنامه مرورگر رو کنترل کنه، پس بررسی ریجن واقعی رو روی کامپیوتر انجام بده
• رابط فارسی با تم تیره و روشن
• متن‌باز، با موتور Xray-core داخل خود برنامه
این پروژه، به لطف این پروژه‌ها و آدم‌ها ساخته شد (حتما اگر دوست داشتید استار بدید):
• patterniha: PattN / PattNG و مقدارهای ضد فیلتر (Finalmask)
• 0xRadikal/Free-v2ray-Configs: لیست‌های کانفیگ رایگان
• bia-pain-bache/BPB-Worker-Panel
📥
دانلود و راهنمای کامل (فارسی و انگلیسی):
https://github.com/MatinSenPai/Gemini-Config-Checker
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/whitedns/1914" target="_blank">📅 01:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1913">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👆
این کانفیگ ها را هم برای amneziawg روی آپ whitevpn امتحان کنید
یکی از دوستان خوب زحمت کشیدند این کانفیگ ها را بازنویسی کردند
❤️</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/whitedns/1913" target="_blank">📅 19:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1908">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wg-mx-free-5.conf</div>
  <div class="tg-doc-extra">1.5 KB</div>
</div>
<a href="https://t.me/whitedns/1908" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/whitedns/1908" target="_blank">📅 19:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1907">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دوستان عزیز:
به جز خود سرورهای whitevpn , الان ۶ موتور اضافه شده است که هر کدوم روی یک نوع اپراتور و یا منطقه کار میده
شما باید خودتون موردی که الان کار میده را پیدا کنید .
فیلترینگ مثل سالهای گذشته یک الگوی ثابت نداره و نمیشه یک نوع خاص از فیلترشکن را به شما داد که روی همه چیز کار کنه
ارادتمند
تیم وایت
❤️</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/whitedns/1907" target="_blank">📅 19:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1906">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitevpn3.10.2026.conf</div>
  <div class="tg-doc-extra">2.8 KB</div>
</div>
<a href="https://t.me/whitedns/1906" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/whitedns/1906" target="_blank">📅 19:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1905">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wg-MX-FREE-13.conf</div>
  <div class="tg-doc-extra">340 B</div>
</div>
<a href="https://t.me/whitedns/1905" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/whitedns/1905" target="_blank">📅 19:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1904">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wg-MX-FREE-5.conf</div>
  <div class="tg-doc-extra">342 B</div>
</div>
<a href="https://t.me/whitedns/1904" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/whitedns/1904" target="_blank">📅 19:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1903">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-poll">
<h4>📊 دوستانلطف کنید اول این فایل ها را ذخیره کنید بعد از قسمت پروفابل - افزودن- amneziaWG  -وارد کردن فایل پیکربندی این فایل را وارد کنید و امتحان کنید که ایا وصل میشید یا نه</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/whitedns/1903" target="_blank">📅 19:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1902">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-poll">
<h4>📊 کدام پروتکل(های) زیر روی شبکه شما کار میکند ؟</h4>
<ul>
<li>✓ سایفون</li>
<li>✓ تور</li>
<li>✓ Ssh</li>
<li>✓ امنزیا amnezia wg v3</li>
<li>✓ IKEV2</li>
<li>✓ سرورهای عمومی whitevpn</li>
<li>✓ سرورهای اختصاصی whitevpn</li>
<li>✓ اتر whiteaesther</li>
</ul>
</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/whitedns/1902" target="_blank">📅 15:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1901">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/bbBzjoCLITBll25sG8F4cJT7X1GFlvIJIid71tjnbjw_9t6wNajxQFMqa8y-8CeSPbX78WJfPgVveGdtn3JpqTJfVJ0hlT93Iw26YQBK_C_7u-as0v8d1NjXel3nm0cnbxZGvOOzQZhBwNLnwO6RH6Rb7N8mv28WZ5ZmHCemRoB-g6etdD3obu8QXA08-168w1vO0rARxRasl0f2KM4cHLORAwTTU0zM1Y_40HUg_LgfmIZko_Vv_p399Bngw8ATQyXLecXlx7YnHJOBAIKW8rbOfZCofDmsEqafsLzSYZxUw_6mTDJ-Q6Vs0RaW48WeGeisUoRlye3bgSKgigKDnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای دسترسی به امکانات جدید نسخهٔ آزمایشی WhiteVPN 1.7.0-beta.1 میتونید با مراجعه به تب "پروفایل" - "افزودن" آنها را مشاهده کنید
@whitevpn</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/whitedns/1901" target="_blank">📅 14:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1898">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.7.0-beta.1-universal.apk</div>
  <div class="tg-doc-extra">203.4 MB</div>
</div>
<a href="https://t.me/whitedns/1898" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🧪
نسخهٔ آزمایشی WhiteVPN 1.7.0-beta.1 منتشر شد!</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/whitedns/1898" target="_blank">📅 14:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1897">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fTxnkzjpL-SFZEko-slCINx_wI3CWP6X7ZBmF81m2PMNIw2r8LEhGXZAMMCjDZC-Am-WNvtVTY9UoXxe-Ud_c1hscGscikSXgEa7fyZ_-Rrkp8P0fdleJGxLBX11HIaBuwqd9eVKOmtLlNlAl_ihzTZ43PisAhVkwEajHVoZEEUEr2j8mEbhQSsNPlURUXxgSW_oXK-v0o8b6bca7uvoHJGwJc04EEipCAKE0OyjiSyqaECPbeLvL2tMyq4F1MX6fdWWPSN9vwYsnujX9mgIZElWleWlnWCq58OYpBR2O0H97zq93GmStEQHu7duYB-4S5sYpTXwe1aPP7bINnugww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧪
نسخهٔ آزمایشی WhiteVPN 1.7.0-beta.1 منتشر شد!
⚠️
🔥
در این نسخه، شش موتور اتصال در دسترس هستند:
Psiphon، Tor، SSH، DNS Tunnels، IKEv2 و AmneziaWG
✨
تغییرات اصلی:
• صفحهٔ یکپارچهٔ «پروفایل‌ها» برای مدیریت اشتراک‌ها و اتصال‌ها
• واردکردن کانفیگ AmneziaWG از فایل یا لینک
vpn://
• انتخاب کشور سایفون از فهرست
• هماهنگ‌سازی فرم‌های فارسی و انگلیسی و اصلاح نمایش گذرواژه‌های طولانی
• بهبود پایداری اتصال و قطع سایفون و نمایش ترافیک
⚠️
این نسخه
آزمایشی
است؛ بررسی کامل همهٔ موتورها روی دستگاه‌های مختلف هنوز ادامه دارد. برخی موتورها به سرور و کانفیگ سازگار نیاز دارند. نسخهٔ پایدار
1.6.10
همچنان در دسترس است.
⚠️
📥
دانلود نسخهٔ آزمایشی
اگر مشکلی دیدید، همراه با نام موتور، مدل گوشی و نسخهٔ اندروید گزارش کنید.
@whitedns</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/whitedns/1897" target="_blank">📅 14:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1896">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sns4fPjucQC-kmM7HLF_VwiO4EvphRY9wAmujE6ary4ADxed5oNbAd47weJbHmeZvWIyPZmlqSbl8elzlZIzOezEVmNKCjlWQi9RjYlniRbJBw7AiGXKBDQPm5Xg-dWhlzp1TddNjLP1OkIGesV9EqkAATq3SfSAwXBO56_1lfHj-rZZHR-LzJDyVR8Zxb-CbCefmwDs3WILPCxYsNpR1EjeXYsnaSAiuCbVozOmnWg62IhGg89esCQ5VooRXAQWCONFoPL3ClDUG1LxhnbKJUvawOlgC8TqZM-QpS2bZ7LpNCjZeVXUDa96f0SvrjU33XxZZF1QhcW_WXdcltOiaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
عزیزانی که با WhiteAether سخت وصل میشن یا مدام قطع و وصل دارید، این روش رو حتماً تست کنید.
به‌دلیل اختلالات شبکه، ممکنه Endpoint انتخاب‌شده مرتب قطع بشه و Fallback به‌صورت خودکار Endpoint دیگه‌ای رو انتخاب کنه؛ همین سوییچ‌ها می‌تونه باعث کندی و ناپایداری اتصال بشه.
🛠
برای رفع این موضوع :
1️⃣
وارد بخش Routes بشید و از پایین صفحه وارد Endpoint بشید.
2️⃣
اسکن Endpoint رو انجام بدید.
3️⃣
بهترین Endpoint از نظر Ping رو انتخاب کنید و روی اون بزنید تا Pin بشه.
4️⃣
گزینه Fallback رو خاموش کنید.
🚀
حالا دوباره Connect کنید و نتیجه رو تست کنید.
چند نفر با همین تغییر مشکلشون برطرف شده؛ ممکنه برای شما هم در شرایط فعلی شبکه بهتر جواب بده.
@whitedns</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/whitedns/1896" target="_blank">📅 19:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1895">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/dcDNlOmnO8JKWCwCnvizuc6x9IVkdV8sFY3UOJ47xlxonH7roN6Ap9WWuLYWgi3Z5B_AXTMFpGt7lUdirOcopWec0e6cS98Az0UUJyK4jGRg-pbpTgLipC1WkH47GmnZy-WKc4qfR_GK3W-710LcQiqNOmnwN-t7ca09uSexUWJwWzwv41T_6evv5_xbq6k_KLbF0W9nUcbJeYksh6jQD26Ck4frYRC47GbDUlQLa7QInOWhe7LyyZMgs8y6QsYKKb0qXJBQiwGSC7cezn0CLyT_v54H0E2L30oxLPFS4YbaanRu2sihmD_ZlnGGZLu_wRRqChEZX1LvEkunHwVJFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری (مستر دی ان اس )
⚠️
⚠️
whitedns app config bot/ masterdns config   :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/whitedns/1895" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1894">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJnX7CM-szuOH-VA-bHXb4IxYQTK9Z0qsAfu9M2HY6XqQmbJCjp2jxs-U-Ofz4QnSMPhyLBjGU5YK61suImEVP6LVqRusZhj1mOMTXjOkjGeMwSiSGvoqeNrIrVnzcDfmVXXu_OkQCwl1iRLpEeq5pjswBPd_W4eP7xIuhmlDO-INBYG00YGvn1ojP0rz7CNDRIybBiSPlO3Ahw2nDSPfTsx1fiwJRBvhFt7ZuUJWFjP-CXWeBvsXa-PBGEr9P5YGFKMCNq_c2CmVp8g-sFebVXQl5AWdXXZFf3MGX6M2QtyYkq7kbALkRbwgZ7XYn3CrKpZbhncUGuynRW0-GFvlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به جای توضیح دادن «اون دکمه رو می‌گم»، روش کلیک کن
👀
اگه با Codex یا Claude Code رابط کاربری می‌سازین، احتمالا پیش اومده نصف پرامپتتون صرف توضیح دادن این بشه که دقیقا کدوم قسمت صفحه باید تغییر کنه
😅
ابزار Agentation یه نوار ابزار به پروژه اضافه می‌کنه؛ روی المان موردنظر کلیک می‌کنین و می‌نویسین چه تغییری می‌خواین.
مثلا:
«فاصله این دکمه از عنوان، ۱۶ پیکسل باشه و توی حالت loading عرضش تغییر نکنه.»
⭐️
نکته کاربردیش اینه که بازخورد رو همراه selector و اطلاعات المان به agent می‌رسونه. می‌تونین خروجی Markdown رو کپی کنین یا با تنظیم MCP، کامنت‌ها رو مستقیم در اختیار agent بذارین.
برای Claude Code یه skill راه‌اندازی هم داره:
npx skills add benjitaylor/agentation
بعد داخل Claude Code دستور /agentation رو اجرا می‌کنین.
فعلا به React 18+ و مرورگر دسکتاپ نیاز داره و بهتره فقط توی محیط توسعه فعال باشه. تغییر کد رو agent انجام می‌ده؛ نتیجه رو هم همچنان باید بررسی کنین.
برای رفت‌وبرگشت‌های ریز طراحی، ایده کاربردی‌ایه
🔥
معرفی و دمو
·
راهنمای نصب</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/whitedns/1894" target="_blank">📅 17:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1893">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommmahdi_sz</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTkGACTRcCLVGhI2NsPq8wSgDgBw8iKyvlm6b2LHf5zutEpDWhHpaVec0vu3qjx565B36ScVUwxBqdtd96KK1qcYR5bEmNRxBzHhFZxItMHgq7R7brlgOlphX3ad38cswkbNJJUrfH1PrciNrdQoWstj82-R3RuBMJsW1Osz75AuEsQbW5zehn89uJ4J5rBN9iau4NcPWcOUgINzWSw4yRPFkANSViByRL4pFbJ6csrZQWKxxLlTqnpVqWI-HDXsqMK-1ZcbdQmy5KHkcWAC_9Mubt96QC4mLk4NBA1KzXEpcqpgtLugIW_YBgX-ISLM2N8s1eO-1WVNMDjJ6T7gwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ArasClient | کلاینت قدرتمند اندروید
یک کلاینت مدرن و متن‌باز برای مدیریت کانفیگ‌ها، Subscriptionها و اتصال‌های مختلف، با امکانات پیشرفته برای تست و مدیریت سرورها.
➿
➿
➿
➿
➿
➿
➿
➿
➿
⚡️
Smart Connect
تست هم‌زمان کانفیگ‌ها و مرتب‌سازی بر اساس Latency برای پیدا کردن سریع‌تر گزینه مناسب.
📡
Subscription Management
مدیریت چند Subscription، بروزرسانی کانفیگ‌ها، نمایش حجم مصرفی و زمان باقی‌مانده و امکانات بیشتر برای مدیریت سرورها.
.arasc
فرمت اختصاصی ArasClient برای Import / Export و اشتراک‌گذاری کانفیگ‌ها با حالت Protected.
🔐
Per-App & Routing
پشتیبانی از Per-App، Routing، Proxy Chain و Policy Group در بخش‌های پشتیبانی‌شده.
🔥
پروتکل‌های پشتیبانی‌شده
VLESS • VMess • Trojan
Shadowsocks • Hysteria • Hysteria2
WireGuard • AnyTLS • AmneziaWG
MASQUE • Mieru • SOCKS • HTTP
➿
➿
➿
➿
➿
➿
➿
➿
➿
🌐
Aether / WARP
پشتیبانی از پروفایل‌های Aether و قابلیت‌هایی مثل:
• WireGuard / MASQUE
• ECH و Fragmentation
• Endpoint Scanner
• WARP Key
• Psiphon و Tor
📊
امکانات بیشتر
• تست و مرتب‌سازی جهانی کانفیگ‌ها
• نمایش اطلاعات اتصال و مصرف ترافیک
• تشخیص کشور سرور بر اساس IP
• Backup & Restore
• Dark / Light Theme
• Logcat و ابزارهای عیب‌یابی
• تنظیمات پیشرفته Core و شبکه
➿
➿
➿
➿
➿
➿
➿
➿
➿
😎
Open Source • Android
👩‍💻
GitHub:
https://github.com/ArasTey/ArasClient
🖼️
Telegram :
https://t.me/imArasTey
📥
Releases:
https://github.com/ArasTey/ArasClient/releases</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/whitedns/1893" target="_blank">📅 17:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1892">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مشکل ربات
@WhiteDNS_installer_bot
حل شد
با این ربات میتتونید ازطریق تلگرام روی سرور خودتون MasterDNS نصب و سرور خدتون رو مدیریت کنید.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/whitedns/1892" target="_blank">📅 09:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1891">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thkB-QvVV6dbFbyKSG41ETp-XuIKzd1B6bHyZ2UCgce36neP_tXhVkOW7ejUKYtule1BaDELFcwsyNW0MXagToDEzCQwUR0OvctVRTkjAZdIsKDa4670kLI4fweYvR6p7JmVsbto8V7njzHnuL8xXwlGopWBvtSy-ZxHgcbadbP6bp_6oJyMmRuOJ9kxFouyZ58Hw5Hu8v6SyrhfP5W1ueLIfHh6mMQnP6bRYDSuNYU_IGYCbIGbZKYk_XYpfpNJEevVUe04sA5-LCdXro2fHzV-OBN2j7Rdlro16k-MkZcHZSlSitQrmLi-HJQ8eukOLbZhgvXqu3zbjK8xd9BLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍓
آموزش جدید رسید!
🥹
✨
اسکن آیپی تمیز با WhiteDNS Scanner و استفاده ازش توی کانفیگ
🔥
💗
از نصب اپ تا تست نهایی، همه‌چیز مرحله‌به‌مرحله توی ویدیو هست
🎀
🎬
ببینینش:
https://youtu.be/GDo6p_z3CAw
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/whitedns/1891" target="_blank">📅 19:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1889">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دوست عزیز :
خرید ، فروش ، درخواست خرید ، آگهی فروش هر چیزی که توش پول رد و بدل بشه ممنوعه
🚫
بلافاصله بن میشید</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/whitedns/1889" target="_blank">📅 15:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1888">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/whitedns/1888" target="_blank">📅 13:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1887">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/whitedns/1887" target="_blank">📅 13:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1886">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/whitedns/1886" target="_blank">📅 13:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1883">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">بعد از ماه‌ها که برای کلاینتم آپدیتی ندادم این مدت روش کار کردم و کاملا بهینه و بهبود یافته. UI/UX  کاملا بازنویسی شده با متریال گوگل. و خیلی فیچر های شخصی سازی داره بخش "رابط کاربری" از تمام هسته های حال حاضر پشتیبانی می‌کنه راحت میتونید کانفیگ هاشو اد کنید،…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/whitedns/1883" target="_blank">📅 13:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1882">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Blue Knight Panel WispByte.rar</div>
  <div class="tg-doc-extra">1.3 MB</div>
</div>
<a href="https://t.me/whitedns/1882" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/whitedns/1882" target="_blank">📅 20:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1881">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0_YDo-lvZaCc09KgTkYNlzMkL4kGapHOJK8A3mp5UehqJwpqG2JdXpv5iDULT6ak4Xh6V8UlLSpr-YsKc4Lvc3FT9XMzKIsOWnX2964RrcmJRY_sJ5lwxuhbXM7iUh1oYDujNHlhAks15JpUxB70h0-rRX88ZFfS-oh6QODkPITdUKH_HKxRDhAjXlL-GOz6Wi8jqvUuptIlhC09L-p2UxUPTyGi6s6z4zzKuhbjMKcE3n4NUu1wO9GDG1yk2XWtNaV2EdLg5e5Vk3iEc3OdwsytFlJh1k4w91ET5AcR5idL1qVuuMDiYuP7CG8Dlqr7UtLKzfXgA6LYGQuxTLctQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎀
بچه‌هااا یه آموزش خفن و کاربردی جدید دارم براتون!
🥹
💗
می‌خواین هاست رایگان بسازین و ازش کانفیگ V2Ray رایگان بگیرین؟
👀
✨
توی این ویدیو با Blue Knight Panel همه‌چیز رو از صفر باهم ساختیم و آخرش هم کانفیگ رو تست کردیم
😍
🔥
اگه این چیزا برات جالبه، حتماً یه سر به ویدیو بزن؛ قول میدم ارزش دیدن داره
🫶🏻
🎬
ویدیوی جدید رو ببین:
https://youtu.be/TmHM_yBPOUU
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/whitedns/1881" target="_blank">📅 20:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1880">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">💬
تعدادی سرور اختصاصی جدید اضافه شد!
دوستان عزیز، برای استفاده از سرورهای جدید، لطفاً از مسیر زیر سابسکریپشن اختصاصی رو تازه‌سازی کنید:
✨
بخش سابسکریپشن
✨
سابسکریپشن اختصاصی
✨
دکمهٔ تازه‌سازی
🔄
فکر می‌کنیم ظرفیت فعلی برای همهٔ کاربران کافی باشه، ولی اگر نیاز به ظرفیت بیشتری باشه، حتماً سرورهای بیشتری اضافه می‌کنیم.
آی‌پی‌های این سرورها اختصاصی هستن و انتظار داریم باهاشون بتونید به‌راحتی به شبکه‌های اجتماعی و تمام ابزارهای هوش مصنوعی دسترسی داشته باشید
❤️</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/whitedns/1880" target="_blank">📅 11:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1879">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-poll">
<h4>📊 الان با چی وصلین ؟</h4>
<ul>
<li>✓ whitevpn</li>
<li>✓ whiteaesther</li>
</ul>
</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/whitedns/1879" target="_blank">📅 11:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1878">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚀
۵۰ سرور اختصاصی اضافه شد!
دوستان عزیز، لطفاً تست کنید و نتیجه رو به من بگید. موقع فرستادن نتیجه، اسم اپراتورتون رو هم بنویسید تا بهتر بتونیم وضعیت اتصال رو بررسی کنیم
🙏</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/whitedns/1878" target="_blank">📅 07:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1877">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🌎
سرور IPهای اختصاصی ری‌استارت شدن
🔭
برای دریافت آخرین تغییرات، برید به:
سابسکریپشن ← سرور اختصاصی ← دکمه تازه‌سازی
بعد از به‌روزرسانی، دوباره وصل بشید.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/whitedns/1877" target="_blank">📅 03:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1875">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⚠️
دوستانی که از نرم افزار whiteasther استفاده میکنند و مشکل ورود به وبسایت ها و یا سرویس های  تحریمی دارند
:
🔥
با یک سری تغییرات که روی سرور exit chain  یا همان زنجیره خروج  دادیم . احتمالا مشکل خیلی از دوستان حل خواهد شد
🛠
برای این منظور کارهای زیر را انجام دهید :
1. وارد ربات
@WhiteDnsChainbot
شوید و کانفیگ(های) مورد نظر خود را انتخاب و دریافت کنید
📥
2.در تنظیمات اپ whiteaesther به مسیرها-زنجیره خروج و در نسخه دسکتاپ به قسمت پیشرفته - زنجیره خروج  بروید و ادرس ساب خودتون را وارد کنید
⚙️
3.کانکت شوید
🚀
موفق باشید
🙏
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/whitedns/1875" target="_blank">📅 17:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1874">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">محدودیت آپلود
۶
پکت رو دوباره دارن اعمال میکنن.
از چند روز پیش برخی سرورهای شخصی دچار این محدودیت شدن.
از دیشب وبسوکتِ (alpn/1.1) کلودفلر هم برای برخی دامنه ها مثل
workers.dev
.* دچار همین محدودیت ۶ پکت شده.
در نتیجه کانفیگ‌های ورکر کلودفلر به صورت عادی در دسترس نیستند.
با ech ,
fragment+fingerprint
و چندین روش دیگه میشه این محدودیت رو بر روی کلودفلر دور زد.
فعلا تغییری در وضعیت warp هم مشاهده نشده.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/whitedns/1874" target="_blank">📅 13:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1873">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">💬
با از کار افتادن سرویس های BPB فشار بیشتری روی سرور های اختصاصی هستش (شاید براتون کار کنه و شاید درست بشه).
ما سعی میکنیم کیفیت سرویس های عمومی رو بیشتر مدیریت کنیم و از شما هم میخوام اگر مایل هستید به ما کمک کنید.
❤️
تنها راه کمک به ما سرویس Patreon هستش و فقط برای ساکنین خارج از ایران قابل دسترسی هستش.
🗺
امروز به ما ماهی ۲۲دلار بهمون کمک میشه اما ماه ها بوده که هزینه های ما بیشتر از ۱۰برابر این هستشو همش از هزینه شخصی پرداخت شده و تا جایی که بتونیم ادامه میدیم.
https://www.patreon.com/cw/WhiteDNS
یک سرور آمریکا
🇺🇲
جدید اضافه کردیم و سرور هایی که براتون کار نمیکرد رو حذف کردیم.
برای دسترسی به سرور جدید، به بخش سابسکریپشن برید و ساب اختصاصی رو بروزرسانس کنید.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/whitedns/1873" target="_blank">📅 13:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1872">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👀
یه تغییر آزمایشی روی
سرورهای اختصاصی
دادیم
فعلاً تعداد سرورها به
۴ سرور
در این کشورها کاهش پیدا کرده:
🇺🇸
آمریکا |
🇸🇬
سنگاپور |
🇫🇮
فنلاند |
🇩🇪
آلمان
آی‌پی این سرورها
هر ۲۴ ساعت یک‌بار تغییر می‌کنه
تا احتمال فیلتر شدن کمتر بشه.
قبل از تست، حتماً اشتراک رو به‌روزرسانی کنید:
بخش اشتراک‌ها → اشتراک اختصاصی → گزینه «تازه سازی»
بعد از به‌روزرسانی، سرورها رو تست کنید و نتیجه رو بهمون بگید
🙌</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/whitedns/1872" target="_blank">📅 06:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1870">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دوستان سلام :
ما برای کانفیگ whitedns ربات داریم
@MasterDnsManager_bot
این کانفیگ ها یک روزه هست ، با حجم محدود
⚠️
به درد افرادی میخوره که هیچی براشون کار نمیده و با یک سرعت خیلی خیلی پایین فقط می‌خوان یک وبسایت چک کنند و یا تلگرام اخبار بخوانند و یا پیام متنی بدهند
این روش سرعتش در بهترین حالت ممکن شاید به ۵۰۰ کیلوبایت برسه
عده ای از دوستان درخواست میفرستند که برای روز مبادا می‌خوایم ، که درخواست رد میشه ، توضیح دادیم که دوستان دلخور نشن
ارادتمند
تیم وایت</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/whitedns/1870" target="_blank">📅 14:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1869">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/DOW1BaQGYdoLNZScBhTqRmuyP7Qu_9x3y4E-oSrtP5QfXkjhOU_0_tQ8WEVB2EAwYBe8Nl1k5n7fnGnlVYT-4X1a4jf1YvcYv54pvPpfOM7qyxCdBB3Obqxtu6Dj213mBgYwSbLDE6MLwthLNHZvRPwsc73Y9mMM8oL0U4pHbqPJluHCthtd7menjtLsHCXcSIFZdZIfUlKJKgoFv7ZWeFSfPuhESYYnIEiZYV1gUO0ysm6l__zUsO6GaQfus5v926R-nM3Fhd_sUsSEcS6y9oZV89zUyDtaTDosYEf5bg-hds1pcuJlWJPd3Onu1h2DjzouQdZoIJK_hHTmAplODg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
اطلاعیه پایان فعالیت ربات
@WhiteDnsResponder_bot
کاربران و همراهان عزیز،
به اطلاع می‌رسانیم که فعالیت این ربات و خدمات مرتبط با آن از امروز به‌طور کامل متوقف می‌شود و پس از این، هیچ‌گونه سرویس، پاسخ‌گویی یا پشتیبانی از طریق این ربات ارائه نخواهد شد.
از اعتماد، همراهی و بازخوردهای ارزشمند شما در تمام این مدت صمیمانه سپاسگزاریم. حضور شما نقش مهمی در مسیر فعالیت این پروژه داشت.
با آرزوی بهترین‌ها برای همه شما
🌹
تیم WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/whitedns/1869" target="_blank">📅 19:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1868">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مهم "
⚠️
⚠️
⚠️
📢
راهنمای تست اتصال WhiteVPN نسخه 1.6.10
لاگ‌های ارسال‌شده از چند دستگاه، نسخهٔ مختلف اندروید، وای‌فای و اینترنت همراه بررسی شدند. در بسیاری از موارد، کاربران فقط چند ثانیه بعد از زدن دکمهٔ اتصال، آن را دستی قطع کرده‌اند؛ درحالی‌که برنامه هنوز مشغول بررسی سرورها بوده است.
در نسخهٔ 1.6.10 برنامه ابتدا سرورهای اختصاصی را آزمایش می‌کند و اگر آن‌ها پاسخ ندهند، سراغ مسیرهای جایگزین می‌رود. این فرایند در شرایط فعلی اینترنت ایران ممکن است
تا دو یا سه دقیقه
طول بکشد.
لطفاً برای تست دقیق، مراحل زیر را به‌ترتیب انجام دهید:
مطمئن شوید نسخهٔ نصب‌شده
WhiteVPN 1.6.10 (85)
است.
وارد تنظیمات برنامه شوید و گزینهٔ
تعمیر اتصال / Repair connection
را اجرا کنید.
بخش
Split Tunneling
را موقتاً خاموش کنید.
در بخش انتخاب موقعیت، گزینهٔ
Automatic / خودکار
را انتخاب کنید.
اگر امکان انتخاب سابسکریپشن دارید، فعلاً
سابسکریپشن عمومی WhiteDNS
را انتخاب کنید.
دکمهٔ اتصال را بزنید و تا
سه دقیقه کامل
برنامه را قطع نکنید.
هنگام اتصال، بین وای‌فای و اینترنت همراه جابه‌جا نشوید و برنامه را از Recent Apps نبندید.
اگر پیام «متصل» نمایش داده شد، حداقل ۳۰ ثانیه صبر کنید و سپس موارد زیر را آزمایش کنید:
بازکردن یک سایت در مرورگر
ارسال یک پیام در تلگرام
بازکردن یک سایت خارجی دیگر
⚠️
اگر برنامه متصل شد ولی اینترنت یا تلگرام کار نکرد:
لطفاً اتصال را بلافاصله قطع نکنید. در همان وضعیت متصل:
اگر برنامه «متصل» شد ولی اینترنت کار نکرد، اتصال را قطع نکنید. در همان وضعیت، از همان گزینه‌ای که قبلاً برای
کپی و ارسال گزارش اتصال
استفاده کرده‌اید، لاگ را کپی و برای ما ارسال کنید. سپس نوع اینترنت، نام اپراتور، مدل گوشی، نسخهٔ اندروید و اینکه سابسکریپشن خصوصی یا عمومی انتخاب شده را بنویسید.
آیا هیچ سایتی باز نمی‌شود یا فقط تلگرام مشکل دارد؟
آیا حالت Always-on VPN یا «مسدودکردن اتصال بدون VPN» فعال است؟
اتصال با سابسکریپشن خصوصی انجام شده یا عمومی؟
اگر برنامه بیشتر از سه دقیقه روی «در حال اتصال» ماند، باز هم ابتدا گزارش را کپی کنید و سپس اتصال را قطع کنید. گزارش‌هایی که بعد از قطع اتصال گرفته می‌شوند ممکن است بخشی از اطلاعات اصلی خطا را نداشته باشند.
بررسی‌های فعلی نشان می‌دهد تعدادی از مسیرهای اختصاصی
AnyTLS
داخل ایران پاسخ پایدار ندارند. در چند آزمایش، سرورهای اختصاصی شکست خورده‌اند ولی برنامه پس از انتقال به سابسکریپشن عمومی با موفقیت متصل شده است. به همین دلیل تا زمان اصلاح مسیرهای اختصاصی، استفاده از
سابسکریپشن عمومی
پیشنهاد می‌شود.
همچنین اگر از نسخهٔ 1.6.9 استفاده می‌کنید و برنامه «متصل» نشان می‌دهد ولی دیتا ردوبدل نمی‌شود، حتماً به نسخهٔ
1.6.10
به‌روزرسانی کنید. نسخهٔ 1.6.9 در بعضی شرایط ممکن بود اتصال ناموفق را به‌اشتباه متصل نمایش دهد.
از ارسال گزارش‌های دقیق شما ممنونیم. این گزارش‌ها مستقیماً برای شناسایی اپراتورها و مسیرهای مسدودشده استفاده می‌شوند.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/whitedns/1868" target="_blank">📅 14:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1866">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⚠️
🔥
تعدادی از دوستان به خاطر فیلترینگ شدید توی منطقه ای که زندگی میکنند توی نسخه 1.6.9 دچار مشکل شده بودند .
کانکشن برقرار میشد ولی ترافیک نداشتند .توی نسخه 1.6.10 این مشکل به طور کامل رفع شده است و احتمالا خیلی از کاربران مثل نسخه های گذشته به راحتی متصل خواهند شد
دوستان تا ما مشکل سرورهای اختصاصی را حل کنیم فعلا از سرورهای عمومی استفاده کنید
⚠️
دوستان چنانچه هنوز برای اتصال مشکل دارید لطفا با نگه داشتن انگشتتون روی دکمه اتصال لاگ برنامه را کپی و برای ایدی ادمین که توی بایو هست بفرستید
ارادتمند
تیم وایت</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/whitedns/1866" target="_blank">📅 11:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1863">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">38.9 MB</div>
</div>
<a href="https://t.me/whitedns/1863" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/whitedns/1863" target="_blank">📅 11:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1862">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/eJb83XQ89QwlvKyZc60M_YytRSCvhNBDXN195uc2F3h-yWsDPrlajpjpfhqCpzoMyHEEdmuT87MpDqACYbmF3jVXnmgs3VYTuSMadpsBq-dTuEB9UMzW4x188WLhmXXOMUTruC5O3TNkScmRvLc9zhaNbFVM-Huj_zxFZpc1Px8iS_E8DgrBkkWKa1zcZr1AhVy1oLtq5dhude6alF6Oy_wTW7CWdHw8IybknfOKKyXOXouC-9eeImyWz_Df1e4ZOJeBuHugYt37lMnSU0LK8FrdvLkh4jMorQmOoeCb5yoX2U5IO1pBHsnxSdXrqTjqPdpo72oYNDW3NekaGEealA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید WhiteVPN منتشر شد (نسخه 1.6.10)
در این نسخه، مشکل نمایش وضعیت «متصل» در شرایطی که ترافیک در شبکه‌های دارای فیلترینگ شدید از تونل عبور نمی‌کرد، به‌طور کامل برطرف شده است.
تغییرات و بهبودهای این نسخه:
تأیید واقعی اتصال:
وضعیت اتصال تنها پس از تأیید نهایی دسترسی به اینترنت آزاد و پایدار ثبت می‌شود.
سوئیچ خودکار هوشمند:
در صورتی که سرور تنها پراکسی محلی ایجاد کند اما دسترسی واقعی به اینترنت نداشته باشد، برنامه بدون وقفه به سرور پایدار بعدی سوئیچ می‌کند.
بازیابی خودکار اتصال:
بررسی‌های ناموفق مداوم پس از اتصال، مستقیماً وارد چرخه بازیابی و اتصال مجدد خودکار می‌شوند.
ثبات سیستم امنیتی:
حفظ و پایداری رفتارهای قبلی در بازیابی آفلاین و مدیریت خطاهای گواهی (Certificate).
افزایش امنیت اشتراک:
الزام و اعتبارسنجی دقیق لینک‌های اشتراک خصوصی در بیلد‌های رسمی برنامه.
📥
هم‌اکنون می‌توانید نسخه 1.6.10 را دانلود یا به‌روزرسانی کنید.
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🆔
@Whitedns</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/whitedns/1862" target="_blank">📅 11:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1860">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ZNIZUHDhVjYejMlmFVgbZk8Dcvul5wt20ZgHejr_dutXsL8rnJioRbHYmIGQPEeiNl5cx-KAMW_LTDOVss9scr7HDw6N_moXln2jtDcdwcnHFQ_JsTrsWbTxXP0Q2BdFdlmE8-0pqGFmIAhp1twzayzgpj_wlpI7aGkVPn5aoT30tqPbgN9wwkh0pFs4-hggAY88V5khInPfxqTbmUYWrZM80ktMpPP4F9SijpShvzDnUd52GkW7TFxw2PWi9AJ36NZYilbo0NKnPQpBH9KU3P0x5iiywWkajCZxMQUlongTZkikge_03A89BD6PH_6OQRfCxZ_JzLoS5USMZWDSHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات پاسحگو
💬
Support Bot:
@WhiteDnsResponder_bot
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری
⚠️
⚠️
whitedns app config bot  :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/whitedns/1860" target="_blank">📅 18:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1855">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteAestherMobile-1.10.0-universal.apk</div>
  <div class="tg-doc-extra">134.8 MB</div>
</div>
<a href="https://t.me/whitedns/1855" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/whitedns/1855" target="_blank">📅 11:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1854">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/OfoPsrxtGhpX40qCIRKghll5E1NFUnQDx2G1RGXdYNhOBabALSJxVkSgoIeH7EtdQI2XTgminu18ZVHSdYdhvWjdoLed_7EEtR7H-mhgIEBADY6lTRUvMDgIQDzIUatpHkkJP_aB6OKB_ZPqzyHo9y2ZglmELgS8LWCBZ_Wa-8It-5QWBVAUH4ub77BFDUchL7Xpfs0Mjk7DEELwH2m1JWEeflbnB9y6q3vmHXziFbF5uvw0UJUTxSEAjQS6Qi1rTnDnvjrUspQzAEDlrBjmd6PxOuQFMsUDo_9E3BYlBWnBz166kjHKkYkF-0r0oIm7C8XkHNygGKZJ_yii_gmWQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Whiteaesther mobile v 1.10.0
حالت خودکار حالا جست‌وجوی مسیر را ادامه می‌دهد و مسیر موفق هر شبکه را به خاطر می‌سپارد
🧠
پایداری اتصال بهتر شده و سرعت دانلود و آپلود در اعلان برنامه دیده می‌شود.
📶
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.10.0
@whitedns</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/whitedns/1854" target="_blank">📅 11:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1852">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-poll">
<h4>📊 الان با چی وصل هستید ؟</h4>
<ul>
<li>✓ اخرین نسخه whitevpn</li>
<li>✓ اخرین نسخه whiteaesther</li>
<li>✓ اخرین نسخه whitedns/coreforge</li>
<li>✓ هیچ کدام</li>
</ul>
</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/whitedns/1852" target="_blank">📅 18:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1851">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آمار اتصال ها داره برمیگرده به حالت عادی
❤️</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/whitedns/1851" target="_blank">📅 13:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1850">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✨
آپدیت WhiteVPN 1.6.9 منتشر شد
❓
بعد از دریافت و بررسی گزارش‌های زیادی که درباره مشکل اتصال برامون فرستادید، چند تغییر توی برنامه انجام دادیم. امیدواریم این تغییرها اتصال رو برای همه‌تون بهتر و پایدارتر کنه.  لطفاً WhiteVPN رو از داخل خود برنامه آپدیت کنید.…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/whitedns/1850" target="_blank">📅 12:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1848">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dika6PTCBSEtMoOFWWXW24bsAofIQaN6AHcnwMuG48Ug-3jfnwQdHWw51THYBirg9rpKb0Tj3qTQ3EfbUKOaVxwOZ-wdIo5d4LE0L9agNHJFBXr58gvV3hLrhxXAcFjHPw5jF2gu_tzPQpCmjfB1WgOtlcl2h1cZauTquPeYBfKX8F-19hECIzuFtkKEu0Do4bXamMaY9y79IZQI3VBD1r5NJWxhAqpRfw1QRh9YtxbyjRp6_7hieurXp7-NoIFO9UX95tXlDJTNmiYYeO3EdxzCfZAn7e-Zt6T3fCFqg2G6VlDS3wHoEso35P4ZjVIQfmesyET7F6vNrZosVOI9SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
آپدیت WhiteVPN 1.6.9 منتشر شد
❓
بعد از دریافت و بررسی گزارش‌های زیادی که درباره مشکل اتصال برامون فرستادید، چند تغییر توی برنامه انجام دادیم. امیدواریم این تغییرها اتصال رو برای همه‌تون بهتر و پایدارتر کنه.
لطفاً WhiteVPN رو از داخل خود برنامه آپدیت کنید. نسخه جدید رو می‌تونید از صفحه GitHub ما هم دانلود کنید:
🛡
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.9
💬
بعد از نصب نسخه جدید، اگر هنوز مشکلی داشتید لطفاً بهمون خبر بدید. گزارش‌هاتون کمک می‌کنه مشکل‌های باقی‌مونده رو دقیق‌تر پیدا کنیم.
ممنون که با گزارش‌هاتون کمکمون می‌کنید
🤍</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/whitedns/1848" target="_blank">📅 12:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1847">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Qo7yYCnPugHgUXLNAeQG356D9B3WvMwfQjVfxEKSLXZfhCBeA4XNhiHCDxV6apDPANxYAfMAzQF13-Kw9IphhuPLSS2FZMvkrPPRS43RTlTstA56DOfbZq09xbx38Ydby3EUiHfezuaAlBMVtPrRwSt3GPLOtkeMK0SLXuMoJ5odD07Ea24_QxZ57FunksjgVkFop8psQtj2HEX8HUc4kuIk2oZo73sVs0zHbDI3D7uIWPVN9ii-kYGIjGB2C6_R4RWvxktpUlgA7RcJTQu5yee75-1MYNE28dDJa1hGiQFVafvU9Szu2pIj0_11SttZZC7E7O9-YX6DOXTOPdHyMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧪
نسخهٔ آزمایشی whiteaesther desktop 1.9.7 pre-release
⚡️
اتصال باید خیلی سریع‌تر شود
کلادفلر در همان جواب ثبت‌نام، آدرس دقیقی را که به دستگاه شما داده اعلام می‌کند. موتور آن را می‌خواند، ذخیره می‌کرد، و بعد نادیده می‌گرفت — و به‌جایش حدود ۲۵۰۰ آدرس را یکی‌یکی امتحان می‌کرد تا یکی جواب بدهد.
🔑
و مشکل «دیگر نمی‌توانم ثبت‌نام کنم»
اگر تا حالا پیش آمده که بعد از چند بار نصب مجدد یا اتصال ناموفق، برنامه اصلاً نتوانسته شناسه بگیرد — این همان بود.
ثبت‌نام همان لحظه‌ای که سرور جواب می‌داد خرج می‌شد، ولی تا چند مرحله بعد روی دیسک ذخیره نمی‌شد. اگر وسطش چیزی قطع می‌شد، ثبت‌نام رفته بود ولی شمرده شده بود. و چون سهمیهٔ کلادفلر روی آی‌پی است، همین می‌توانست گوشی روی همان وای‌فای را هم از کار بیندازد.
حالا اول ذخیره می‌شود، بعد بقیهٔ کارها.
🛡
و یک حالت خراب که دیگر ممکن نیست
قبلاً اگر با وایرگارد وصل بودید و MASQUE را امتحان می‌کردید، هیچ‌کدام دیگر کار نمی‌کرد. ساختار جدید طوری است که این وضعیت اصلاً قابل ساختن نیست.
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.7
⚠️
نسخهٔ آزمایشی است — در فهرست به‌عنوان آخرین نسخه نشان داده نمی‌شود و برنامه خودکار پیشنهادش نمی‌دهد.
شناسهٔ فعلی‌تان خودش منتقل می‌شود؛ کاری لازم نیست بکنید و چیزی پاک نمی‌شود.
💬
اگر اتصال سریع‌تر نشد، یا هر چیز عجیبی دیدید، بگویید.
@whitedns</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/whitedns/1847" target="_blank">📅 12:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1845">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/a-X1vsF-jVtavKGnw8P4cwPjNU17WeKDbgWHCaCfqTfMlmGK-RJJH5YH9BAqJxbWlmV13bHwFz6tfqsqDB3Rrb4RYR3mECWu9vLfzD4O8EQwFega-RqiTSNhU6eQrEWJ1ZVi0wDFTRIX5erDbDDI0HAA3a4pOYnS6wM834rZ8dyvEc8JQqYeKNC0zR75J2YqtbN2TWvqTgGGc0EzBR2d0rnoAchxubMfmQg3Tcob8F7zAxR0VqNN_zCy2Cmga-hCuK8EmSHVWLn23ukZ1NPF2Mkv7nHF-o9OgTNi0fwV_RWv7Av0M6UBlhHNaJjnCeCmlm8vssCdjtWu8b_0Eb4NXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/XPcjABeleOxg7v7tVuCC4JXvzAWdIlAwerObEJRLd9iMI4rrsapKb8Dgb-D58FzDT7R3szyDE7P27nEIvD4nQmq12wgdv9P4FUahY7YStw5B8nPZlDfvHpP20vdh2QeYKxmiGW2F1jehD2AvC25EEH6128IZvZTBMa5CJnHJPCNvTUR925T2sOyvD0mKS5UbhHdX4DR0K3QH97tatvEfgNdP0ybdNyNUU3trU9slno0BXIw3FvxQ0u--rQnYBP7ZMqVwL5s_ts5PRy-i04HQOwilkzGDp7UAiyzp_MUuRRsjzJZ4WHMpbkhkQMLRt47XjeHe4aH-K_Nhbwmnc4Xlkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
⚠️
یک امکانی که توی اخرین نسخه ازمایشی whiteaesther موبایل و دسکتاپ تقویت و بهینه سازی شد - امکان ست کردن dns بود که تقریبا هیچ کس بهش توجه نکرد جز یک گروه خیلی کوچک به نام گیمرهای عزیز
😁
😃
از این امکان استفاده کنید حتما خیلی از مشکلات شما را حل میکنه
🤓
لیست dns های عمومی :
۱. DNSهای عمومی و معمولی
Google
8.8.8.8
8.8.4.4
Cloudflare
1.1.1.1
1.0.0.1
Yandex
77.88.8.8
77.88.8.1
Quad9
9.9.9.9
149.112.112.112
OpenDNS
208.67.222.222
208.67.220.220
AdGuard Unfiltered
94.140.14.140
94.140.14.141
Control D
76.76.2.0
76.76.10.0
DNS.WATCH
84.200.69.80
84.200.70.40
DNS.SB
185.222.222.222
45.11.45.11
AliDNS
223.5.5.5
223.6.6.6
DNSPod
119.29.29.29
—
Hurricane Electric
74.82.42.42
—
Comodo Secure DNS
8.26.56.26
8.20.247.20
Neustar UltraDNS
156.154.70.1
156.154.71.1
LibreDNS
88.198.92.222
—
360 Secure DNS
101.226.4.6
218.30.118.6
OneDNS
117.50.10.10
52.80.52.52
Quad9 Unfiltered
9.9.9.10
149.112.112.10
DNS4EU Unfiltered
86.54.11.100
86.54.11.200
۲. DNSهای امنیتی، ضدتبلیغات و خانوادگی
Yandex Family
77.88.8.7
77.88.8.3
Cloudflare Security
1.1.1.2
1.0.0.2
Cloudflare Family
1.1.1.3
1.0.0.3
AdGuard Default
94.140.14.14
94.140.15.15
AdGuard Family
94.140.14.15
94.140.15.16
OpenDNS FamilyShield
208.67.222.123
208.67.220.123
CleanBrowsing Security
185.228.168.9
185.228.169.9
CleanBrowsing Adult
185.228.168.10
185.228.169.11
CleanBrowsing Family
185.228.168.168
185.228.169.168
Control D Malware
76.76.2.1
76.76.10.1
Control D Ads
76.76.2.2
76.76.10.2
Control D Family
76.76.2.4
76.76.10.4
DNS4EU Protective
86.54.11.1
86.54.11.201
۳. DNSهای رمزگذاری‌شده (DoH و DoT)
Google
https://dns.google/dns-query
Cloudflare
https://cloudflare-dns.com/dns-query
Quad9
https://dns.quad9.net/dns-query
AdGuard
https://dns.adguard-dns.com/dns-query
Control D
https://freedns.controld.com/p0
NextDNS
https://dns.nextdns.io
Mullvad
https://dns.mullvad.net/dns-query
DNS.SB
https://doh.dns.sb/dns-query
AliDNS
https://dns.alidns.com/dns-query
DNSPod
https://dns.pub/dns-query
OpenDNS
https://doh.opendns.com/dns-query</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/whitedns/1845" target="_blank">📅 11:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1844">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">💬
کاربران WhiteVPN روی اندروید
اگر اخیراً داخل برنامه با مشکل اتصال یا اختلال مواجه شدید، لطفاً برای کمک به تست و بررسی مشکل این مراحل رو انجام بدید:
1. ابتدا گوشی رو یک‌بار
Restart
کنید.
2. وارد تنظیمات گوشی بشید و برای WhiteVPN گزینه
Force Stop / توقف اجباری
رو بزنید.
3. سپس
Clear Data / پاک کردن داده‌های برنامه
رو انجام بدید.
4. برنامه رو دوباره باز کنید و اتصال رو تست کنید.
در اکثر موارد بعد از انجام این مراحل مشکل برطرف میشه.
اگر بعد از انجام این مراحل همچنان مشکل داشتید، لطفاً نتیجه رو به ما گزارش بدید تا بتونیم دقیق‌تر بررسی کنیم.
ممنون که با تست و گزارش‌هاتون به بهتر شدن WhiteVPN کمک می‌کنید
🤍</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/whitedns/1844" target="_blank">📅 09:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1843">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/c0-q8h5qbkdWlXNb5rDLbAeCcDUDnrntqFFb1awryQCW24IozhK1QPJABaRJuMAMSxAsbiTl0JQM-Vi2HEpckDvAEsKo4Ir0LU60Fmbo17d_dREhHWGsJfVOhgWp6t-L-t3u1wlztoxlb5renMgoVo2abWv4Kk-1O1Js24U2hc1FjxlRkoimaL4hcEBkQrLx7ijFGLF2nSyvaqd7qAxJHc5fYyKlLJcVAwmrHxfPPz9TjrZU97I-eZ8ZnW-wL5eBjVYnSuduW_46Zd1_xBhkf3kN2RTGZafrZG_wGy2Y2DyO6m45O5e2SrOsrpFtcfAFquaIUUtii9LncU9cI7wxmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ازمایشی whitevpn desktop1.0.23 pre-release
🧪
این نسخه آزمایشی است، نه انتشار رسمی. برنامه خودش آن را پیشنهاد نمی‌دهد. اگر نسخه پایدار می‌خواهید، روی ۱.۰.۲۲ بمانید.
چه چیزی تازه است:
- فایل نصبی
.msi
برای ویندوز — نصب در Program Files، میانبر منوی Start، و حذف از تنظیمات ویندوز. نسخه zip هم هست.
📦
- گزینه «همه سرورها» — اگر چند سابسکریپشن دارید، از میان سرورهای همه آن‌ها انتخاب می‌کند.
🌐
- پروکسی سیستم و حالت تونل حالا در منوی آیکون کنار ساعت هستند.
⏰
بیشتر از همه به تست فایل نصبی نیاز داریم، چون اولین بار است ساخته می‌شود. اگر ۱.۰.۲۲ را دارید، این را رویش نصب کنید و ببینید درست جایگزین می‌شود.
اگر مشکلی دیدید گزارش بدهید — اگر بتوانید محتوای صفحه Logs را هم بفرستید کمک بزرگی است.
📝
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.23-rc1
@whitedns</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/whitedns/1843" target="_blank">📅 06:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1839">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-poll">
<h4>📊 خیلی از دوستان میگن الان یکی دو روزه اختلال شدید دارند و برنامه های white براشون کار نمیکنه . شما چطور؟</h4>
<ul>
<li>✓ هیچی کار نمیکنه</li>
<li>✓ همه کار میکنند</li>
<li>✓ فقط whitevpn کار میکنه</li>
<li>✓ فقط whiteaesther کار میکنه</li>
</ul>
</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/whitedns/1839" target="_blank">📅 15:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1838">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pKfkmHxgYfhAnTQdwnf4kXYcXUSsa5EHTN4BpyaMfL_VRqnRKXUWlRrbA5vFcH5W9M3bFz-u-FOQYSDbNHchE9KE8EMCGJF_7sOC6TL6zbrO-2bRMm57MewYOS-KmB3MrhHGUmngnqe1FfF8LzbeP-lIiV7RERqk_OdvwgELL8kDCLTeOo2E-7qFOlPH-EqK2PCE_ROf5qkL5UHo6sojv4Hk0lfuhz8ZAyCzp5avEG_4yBYNmZHvBRV97MFyScPsXAOaHtCWXP5HA2ugQ1_bBZcrzntz0ROnEva3M_9OIyqkDLIWRE3SnYgrZHRgAUr5_wnonwh0KhMcMsZt_YMu-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteAesther mobile V1.9.4
pre-release
الان DNS inside the tunnel روی همه حالت ها اعمال میشود - قبلا این امکان فقط برای حالت proxy بود.
🌐
چی درست شد
▫️
فیلد «DNS inside the tunnel» بالاخره کار می‌کند.
✅
تا حالا هر چی وارد می‌کردید نادیده گرفته می‌شد و همیشه از
1.1.1.1
استفاده می‌شد. اگه با سایت‌های تست DNS چک کرده بودید و جواب عوض نمی‌شد، دلیلش همین بود.
اگه خالی بگذارید مثل قبل
1.1.1.1
می‌ماند. در حالت chain اعمال نمی‌شود، چون آنجا نام‌ها رمزگذاری‌شده و از سمت خروجی پرسیده می‌شوند.
🔒
و بهینه سازی موتور و routing , ......................
نصب:
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.9.4
@whitedns</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/whitedns/1838" target="_blank">📅 15:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1837">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/CVv9ZSttQ5etbqMoDaIGtBbzWE2583aedoZcm4Sm2MxzZo7Q9OTMp0lDjCLlogTrdYdSsoBniJ0Z3kHgSSvjQEyuqm_F6bMZeHKYnwwabpeAELF7k8zQsRsM-xshvi_6GlFhaWVqU7qnwwA1T7oitQ4T3mSBOeOddfatduVSn-nZJXLsiJJSvBVzNxlu2ql1txFreJCW5ssj38dvmFH-WJnHawqQ2LUkrTV_FR7uPHxhQ2ZZYVQXn5kLWiQ-Y2_QdNj6kLw66bCo-BdImXook12EgF2SK8t6zQ_MHmZhXRYECSV5avk36XHZU4y43SdwlDmq7MNDJ4N5VbkG_tjDsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخهٔ آزمایشی whiteaesther desktop 1.9.5  — رفع باگ پورت و یک سری بهینه‌سازی روی موتور و .........
🚀
اگر بعد از هر بار اتصال، پورت پراکسی محلی عوض می‌شد و تنظیماتتان به هم می‌ریخت، این نسخه همان را درست می‌کند.
✅
پورت دوباره ۱۸۱۹ می‌ماند — هر کریری که وصل شود.
🔒
این باگ از نسخهٔ ۱.۹.۲ به بعد دیده می‌شد، از وقتی دکمهٔ اتصال شروع کرد خودش راه خروج را پیدا کند و سایفون یا تور بیشتر برنده می‌شدند.
🕵️‍♂️
📥
github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.5
⚠️
نسخهٔ آزمایشی است — در فهرست دانلودها به‌عنوان آخرین نسخه نشان داده نمی‌شود و برنامه خودکار پیشنهادش نمی‌دهد. با همین لینک بگیریدش.
اگر پورت باز هم جابه‌جا شد، حتماً بگویید.
📢
@whitedns</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/whitedns/1837" target="_blank">📅 14:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1836">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🎮
معرفی اپلیکیشن WhiteGame | پینگ و آنالیز سرورهای گیمینگ در یک بستر
🚀
برنامه WhiteGame یک ابزار کارآمد آنالیز و ارزیابی کیفیت اتصال گیمینگ (Network Pr MA) برای سیستم‌عامل اندروید است (که به‌زودی برای سایر پلتفرم‌ها نیز منتشر می‌شود)
📱
. این برنامه به‌طور…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/whitedns/1836" target="_blank">📅 09:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1835">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twU0nlEz64cRdWJH-wTA2KHJN6GugYkzDjt1tfVgNyphfEwMGMrTNglPb0NQvqMf6HdUV7WQ-7qs-SBx6-oIakXs3fSsnniV9GVVSxDa79oLr0weFilNlmKZSezWaHXolWZkhYUvkWME6cmiY3-fnxX8r1KMAGBGx8Vwh1NU02l98AF-3Az-aDFqSk8AV8Px19jaYtbaXYvUyOTr5fdWySDL3j9XdI7dthds16yCZ0Lp3rYaspB5iqtIoHYnSJeTO-2tq3T9ba_z-WVuNhd66zuZnZCrLAG9Uzk-je5KWssBJr7Z0H15ULEgfkPTMxRoyHoqQ8uM7yMWNgSv-B8JXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
معرفی اپلیکیشن WhiteGame | پینگ و آنالیز سرورهای گیمینگ در یک بستر
🚀
برنامه
WhiteGame
یک ابزار کارآمد آنالیز و ارزیابی کیفیت اتصال گیمینگ (Network Pr MA) برای سیستم‌عامل اندروید است (که به‌زودی برای سایر پلتفرم‌ها نیز منتشر می‌شود)
📱
. این برنامه به‌طور ویژه برای بهینه‌سازی پینگ، سنجش کیفیت اتصال (QoS) و رفع چالش‌ها و محدودیت‌های ارتباط با سرورهای بازی طراحی شده است.
📊
این ابزار با شبیه‌سازی پروپ‌های شبکه‌ای و سنجش شاخص‌های کلیدی و نوسانات پکت‌ها تحت وب، به گیمرها این امکان را می‌دهد که وضعیت زیرساخت اتصال خود را پیش از ورود به بازی ارزیابی کنند. جای دارد گفته شود که تمرکز ما روی
UDP
است، همچنین قابلیت
Test Real Path
در اپلیکیشن، پینگ واقعی و دقیق شما را در زمان Matchmaking و InGame نمایش می‌دهد .
🔐
پروتکل‌های پشتیبانی‌شده:
Warp | WireGuard | Amnezia | Xray
✨
ویژگی‌های برجسته:
• Packet Loss Injector
• Jitter Plus
• Gaming DNS Spy
• Optimizer Warp و WireGuard
⚙️
علاوه بر این، ابزارهایی برای ساخت و مدیریت کانفیگ در اختیار شماست؛ با استفاده از بخش Generation برنامه، تنها کافی است Public Key سرور خود را قرار دهید تا خروجی موردنظر به‌صورت خودکار تولید شود .
📉
همچنین در مرحله تست آزمایشی (Beta)، حدود ۳۰۰ نفر از کاربران با استفاده از ترکیب Warp و پنل BpB توانستند میزان Packet Loss خود را در شرایط ناپایدار کنونی به نزدیک ۰٪ برسانند.
🤝
امیدواریم با بازخوردها و پیشنهادات شما، این پروژه را روزبه‌روز بهبود ببخشیم.
https://github.com/TaJirax/WhiteGame
@Whitedns</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/whitedns/1835" target="_blank">📅 06:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1834">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/oCu_GJYK4vxk7kjFq3QqJAUj9mes-EZmU3d7C8RxovnKvlQUuTcdFMngx0YOtkLzhnYiP4Kj9RbpIB6X_cFJpGGpapj1qJeBmSY4FqUZECuFtFyp-wOIsAAEot8ONt64B2MGPObNZ_mtd9-UcwAj3XO-We0e3GLIYM-v493SMGPd8uPO-f1KPWgGNUVChMy3KdSAIDOeyc5EHt19XM7XXAg5fMxA-PTDOYclREy3_JAeCQoG0DOAWivWLmpqDZWGkdz99MyXB2jm9u8m-u5UewDAe4IieMLe2Zgk8vCyTcZf7Or0qNCPYrt80MvyMKay9NIDab5BiBySgUWbvaPHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا در گروه whitedns عضو بشید
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/whitedns/1834" target="_blank">📅 20:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1833">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/lvaujl-X22ukFD5hAojcFrPAI5P3JGY1QUtCEsKI3KhNVfKhoN7sn3bj-hzEZPbaLLMsS0UBYv0An6vZlQNxy5wIoXiTn43BffoOB6ECjEpxH7YKRGMf0jehMw7u_9h31kr17IQiOHQ6-JhE3zPEQr7lKrpLEytN3hhBtJNXlerAKQqoyARB57tTeD3GM8wUgvdW28gHu9Bp46iKQa_VbGLkmtNFyWckH94dNdBjnhDfUGuIXHdQDj6ATCGCWBTndqHIi1cqFHunJ_ZRSyf8GGhTBL0XJqT8C8wPMR83iEKWrjeUOWt6edfuy02BVjSUBnKB34nbosX_uTjlLc7BHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات پاسحگو
💬
Support Bot:
@WhiteDnsResponder_bot
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری
⚠️
⚠️
whitedns app config bot  :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/whitedns/1833" target="_blank">📅 17:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1830">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Blue Knight Panel (Orihost).rar</div>
  <div class="tg-doc-extra">1.3 MB</div>
</div>
<a href="https://t.me/whitedns/1830" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/whitedns/1830" target="_blank">📅 02:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1829">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhArLzgmCpJHaetAWg_Lg49VD3aWhTbEUhsMClRICZ83mqkR6u8FIOZpxjloVabCNSsGXWspxPLBxp75U8D2JeRkPPiiv2GLs4-T5e9GAqaByYbs5ujPDUypmvSipMCE-7lou2ljqBzAXUiQxty4mz8vByr3Ey6c25TbpvTBhaphjVOGQOVcohHCteVESA0fZhYjoX7Y3bJFMqNJRVyejqvZVcEazcGJ_HwxIduFTxGjfoMCnhvFUMSkv0OB-FcKU0scLEzPzckn-4coRIZkVlQAYR7VSc1PpRutEq48qKO0EQrKB-IAi5ij8mR5augh_YNZNhoi-eTlb8psoyrDeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍓
بچه‌هااا یه آموزش جدید آپلود کردم
🥹
✨
اگه Gemini خطای 403 میده یا Google Flow براتون باز نمیشه، این ویدیو رو از دست ندین
👀
💗
توی ویدیو از صفر Blue Knight Panel رو می‌سازیم و آخرش با کانفیگ‌هاش Gemini و Google Flow رو تست می‌کنیم
😭
🔥
🎀
تماشای ویدیو:
https://youtu.be/GK2PGDzkbh4</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/whitedns/1829" target="_blank">📅 02:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1823">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteAestherMobile-1.9.3-universal.apk</div>
  <div class="tg-doc-extra">134.8 MB</div>
</div>
<a href="https://t.me/whitedns/1823" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/whitedns/1823" target="_blank">📅 14:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1822">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Q4iw0G302YQkhfSxMJjEgBuENokrk-k8cB3NcO0B59TATnDYrKpmenFwBHmSEKaiK-SCpyegOKh8aNkqt9YcQc09kG-_21A5qWYZ5_M6TOCEMc0jtq969tELnGyerS_nchgTT26n-IqxNXorIRUcG4OztykucQqh4Ce0jKFEETuYPa7RoUb40MZ8-khjT9ypxNofg2OzwGrVR0yNJ458FLsMghCS3kfCDlJX15_3xp3gg19o1xqrCUh0K-OnXm9wZwjxs_wqdRKzJ-4okcYhis4u-kh9dhdlg4S29hlSNAI3HzIZqVN2yM4gAy96BsUJbX5iyoryP-Mi-s00_8AoHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther
Mobile 1.9.3 — نسخه پایدار
🔥
نسخه پایدار 1.9.3 منتشر شد. برای به‌روزرسانی می‌توانید از قابلیت جدید داخل اپ استفاده کنید یا فایل را مستقیماً روی نسخه فعلی نصب کنید.
برنامه را حذف نکنید تا هویت و تنظیماتتان حفظ شوند.
قابلیت‌های جدید
آپدیت مستقیم از داخل اپ
کارت «نسخه جدید منتشر شده» حالا می‌تواند فایل به‌روزرسانی را دانلود و نصب کند.
این قابلیت فقط زمانی فعال است که:
پوشش اتصال روی «کل دستگاه» باشد.
فایل با همان کلید نسخه نصب‌شده امضا شده باشد.
ابزارک صفحه اصلی
بدون باز کردن برنامه، اتصال را برقرار یا قطع کنید. برای افزودن ابزارک، در Settings دکمه Add را بزنید.
هنگام جست‌وجوی مسیر نیز دکمه قطع اتصال در دسترس خواهد بود.
مشکلات رفع‌شده
مشکل نسخه 1.8.0 که ممکن بود برای یک هویت دو رکورد نگه دارد، برطرف شده است. اگر نصب شما در این وضعیت گیر کرده باشد، با اولین اتصال خودکار اصلاح می‌شود.
جست‌وجوی طولانی finding a working route اکنون محدودیت زمانی دارد. این فرایند قبلاً روی شبکه‌های دشوار ممکن بود تا ۲۷ دقیقه طول بکشد.
هنگام جابه‌جایی بین وای‌فای و دیتای موبایل، تونل تا جای ممکن به شبکه جدید منتقل می‌شود و از ابتدا ساخته نخواهد شد.
اتصال MASQUE in MASQUE اصلاح شده است. اگر روش اول برای هاپ داخلی پاسخ ندهد، روش دوم نیز آزمایش می‌شود.
تمام اصلاح‌های نسخه 1.8.1 نیز در این نسخه قرار دارند.
روش نصب دستی
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.9.3
فایل مناسب معماری گوشی را دانلود کنید.
اگر نمی‌دانید کدام فایل مناسب است، نسخه universal را بگیرید و آن را روی نسخه فعلی نصب کنید.
در صورت مشاهده مشکل، از مسیر Settings ← Diagnostics گزینه Send diagnostics را بزنید و گزارش را ارسال کنید.
⚠️
@whitedns</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/whitedns/1822" target="_blank">📅 14:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1821">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/stCidQ-34vzJyPabXQctkx61g39WinxDCdQe8tTd9RPj8nligJ7uJbJHrAru-yXjpkZ_AEGZsFq2g5KqyxTShynOUKnfYnX5y31Eu7V-HwsFSQeSkJFjLC2Fon2p_H233zbYN8JHIVS9NUA3uJKfazBTjmQKrgXprGZm-dg5eqVsk45qNOD5cbHVIGAFfUXq-wdxO0e48TG_XUbEn5_kABIARXGJd2NScWWCETDIuH8jQbErFZhou4Y0J-aL0XxhSmOJ6iHIeENLNg-Nuk1SCzIj49fHnWMlWizU7CCWUXq9tdyt21iZWvFEPUPg7b67wZy-Q0qILZVHrIbVFgU9Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
;کاتن روتر
چیست؟
کاتن روتر یک ابزار سبک برای مدیریت چند سرویس DNS Tunnel روی یک سرور است.
خیلی ساده بخواهیم بگوییم:
فرض کنید چند سرویس مختلف دارید، اما فقط یک سرور و یک IP در اختیار دارید. CottenRouter درخواست‌ها را دریافت می‌کند و بر اساس دامنه، هر درخواست را به سرویس مربوطه می‌فرستد.
یعنی چند سرویس می‌توانند از یک IP و پورت عمومی ۵۳ استفاده کنند.
⚠️
توجه: CottenRouter خودش VPN یا تونل ایجاد نمی‌کند؛ بلکه سرویس‌های تونلی موجود مانند CottenDNS، MasterDnsVPN، StormDNS و SlipGate را مدیریت و مسیریابی می‌کند.
🔗
لینک پروژه:
https://github.com/TaJirax/CottenRouter
پیش‌نیازها
برای نصب به این موارد نیاز دارید:
یک سرور Linux با IP عمومی
دسترسی SSH و root یا sudo
دامنه یا زیردامنه
سیستم‌عامل پیشنهادی: Ubuntu 20.04 به بالا یا Debian 11 به بالا
روی ویندوز مستقیماً نصب نمی‌شود؛ باید روی سرور Linux نصب شود.
نصب آسان
ابتدا با SSH به سرور وصل شوید:
ssh root@IP-SERVER
سپس دستور زیر را اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
بعد از نصب، پنل مدیریت را باز کنید:
sudo cottenrouter tui
استفاده خیلی ساده
در پنل بازشده:
با کلید Space سرویس موردنظر را انتخاب کنید.
با کلید i نصب هدایت‌شده را شروع کنید.
با کلیدهای Enter یا e دامنه و پورت سرویس را تنظیم کنید.
با کلید s یک سرویس را Restart کنید.
با کلید v اطلاعات اتصال و مسیر رمزها را ببینید.
با کلید x یک سرویس را حذف کنید.
تنظیم دامنه
برای هر سرویس یک زیردامنه جدا بسازید و همه را به IP سرور متصل کنید:
cotten.example.com
→ CottenDNS
master.example.com
→ MasterDnsVPN
storm.example.com
→ StormDNS
feed.example.com
→ thefeed
در پنل، همین دامنه‌ها را برای سرویس‌های مربوطه وارد کنید.
بررسی وضعیت سرویس
برای دیدن وضعیت CottenRouter:
sudo systemctl status cottenrouter
برای بررسی سلامت:
sudo cottenrouter healthz -config /etc/cottenrouter/config.json
برای دیدن لاگ‌ها:
sudo journalctl -u cottenrouter -f
به‌روزرسانی
برای نصب آخرین نسخه، همان دستور نصب را دوباره اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
نصاب تنظیمات قبلی را نگه می‌دارد و در صورت بروز خطا امکان بازگشت خودکار دارد.
📌
برای اطلاعات کامل‌تر، راهنمای فارسی پروژه را ببینید:
https://github.com/TaJirax/CottenRouter/blob/main/README.fa.md
اطلاعات این متن بر اساس راهنمای فعلی مخزن نوشته شده است.
@whitedns</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/whitedns/1821" target="_blank">📅 17:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1820">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/swVW8asgCrpUcdEIcKVXxYsNZKfa3Jna7pIahqsiMiggJw1_vM2UuEHO-zLF0Ts6VuJRKbVKLhccEa-4k8Cz4EE-eFP7F5Yi1e5zs1gHpQd-3k__-0iD0qSRbCXJbMzvf_esptHO-Aw5ZON7ecMaOR8qVktRpNpr2nQIlGGPGwEEF6n4XUqwnv-YZDrx8lUZ07gY1IhcluRs0kLiKYezHcnY2eJgBJmYTpuWBSKZDlEsPwAejqqNOVWUFSsikJtNB6oMX32ER7AhQBNp_Ug2kmitwBE6ou4U3vSoW6lU2DsWm0C41Vx_c45QV5cQxxDzIHY0OimmWeKE4DzZnHIN9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخه
CottenRouter v1.2.13
منتشر شد!
سریع‌تر، پایدارتر و آماده برای ترافیک سنگین
⚡️
• رفع مشکلات نصب
SlipGate
روی سرورهای تازه
• جلوگیری از Down شدن Router هنگام قطع نصب یا SSH
• رفع تداخل Domain و Port بین Backendها
• امنیت بهتر
CottenDNS
و
StormDNS
0
٪ Query Loss
در تست ۵۱۲ کلاینت همزمان
• پردازش بیش از
۲۲K Query/s
• بهبود TUI، خطاها و سیستم Purge
✅
آپدیت مستقیم بدون حذف Routeها، Backendها و تنظیمات قبلی
💻
GitHub
https://github.com/TaJirax/CottenRouter
📋
لیست کامل تغییرات
v1.2.13
https://github.com/TaJirax/CottenRouter/blob/main/docs/releases/v1.2.13.md
@whitedns</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/whitedns/1820" target="_blank">📅 16:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1819">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ksyPcJSe-we4EbT7xhbVPwBlT7jQBHxSDDGUWo-wMt21csZqxc8i07rUEFBYyDcEex5wbZHRnO6j75j-nTa15VyNd5ylu-S2CjU73hKZBk9tEJexSlj8xrmj6BlkX9bSA3VNFZA8iIvMk5zbO9Qf3gSpp2dJhXERea1JQCycJPch8er8X8mMY3mWGLu06e4Jda22GpAfSzgKiI7lbaiqi_Mt-IMXLkDiMcdTosMN0C8c0ZXZemRshVCp1Wgdi1XXrHK1Ow_Czo6QsxfB3rktWyHv-aDjIwVIrOmHfSEo-RRs3wvREfjq1ylo57vVKyXMpG3aglMHDDzDboijKsUm0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whiteaesther moblie pre-release 1.8.1
⚠️
این نسخه برای کاربرانی هست که توی چند روز گذشته اختلال شدید گزارش کردند و نسخه آخر هم مشکل انها را حل نکرد
برخلاف باور غلط عمومی ورژن ها در حال بدتر شدن نیستند بلکه امکانات بیشتری در حال اضافه شدن است - اما به دلیل گستردگی کاربران ما مجبوریم حداکثر بومی سازی را انجام بدهیم که این کار گاها زمان بر خواهد بود .
اگر روی ورژن قبلی مشکلی ندارید فعلا اپدیت نکنید !!!!
⚠️
⚠️
⚠️
دو اصلاح، هر دو روی حساب زنده اندازه‌گیری شده:
MASQUE دیگر دنبال آدرس نمی‌گردد. Cloudflare در هر پاسخ ثبت‌نام آدرس اختصاصی دستگاه را می‌دهد و موتور نادیده‌اش می‌گرفت
ثبت‌نام‌های Cloudflare دیگر دور ریخته نمی‌شوند. هویت بلافاصله پس از ثبت‌نام و پیش از هر کار دیگری ذخیره می‌شود؛ مسیر مستقیم یک بار امتحان می‌شود نه پنج بار؛ و نصبی که enrolment مربوط به MASQUE کلید WireGuard‌
اش را باطل کرده بود، در اولین اتصال خودش را تعمیر می‌کند.
این نسخه به‌صورت خودکار به کسی پیشنهاد نمی‌شود.
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.8.1
@whitedns</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/whitedns/1819" target="_blank">📅 12:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1818">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">😎
دیگه لازم نیست برای آپدیت از اپ خارج بشید.
اپ اتوماتیک ورژن جدید رو دانلود و نصب میکنه.
این به کسایی که اطلاعات فنی هم ندارن کمک میکنه.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/whitedns/1818" target="_blank">📅 11:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1817">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbKn_rCTy5RRkIYXO-gLof6ETDtbzhwx_ygH8Q9SH6sCcvOnByncUu3IxcyHYzfXbXlbpN7lGcuk6M92-S8MRHrfJQ8gFkP2XgOy8Vq7D5yBveQmDrAC8W0tJOnJLmMhYo6iJ25SpL5PlqrJmRmuZhNvYPJ0Zcst-j5Xcj8aZA1CoAGOoU_GUzhOXfZZJoqPu4dR1z9NOeRHO0F3uDqp79uEerNC1kyc1304VyU9ye5rJbA91jfYFR0Nl__QZnCZw8Hq4_Y83OnqDW-_fUoCfkDz_ZyeSXBUJjfd0RLVqg8FjnCfgboXjIAkzdV2yrfj69PEWsRoH_lBSajVylKJyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
انتشار نسخه جدید WhiteVPN 1.6.8
تغییرات نسخه جدید:
🟢
ویجت صفحهٔ اصلی برای اتصال، قطع اتصال و نمایش وضعیت VPN
🟢
به‌روزرسانی از داخل برنامه، با نمایش پیشرفت دانلود، امکان رد کردن یک نسخه و بررسی صحت فایل و امضا پیش از نصب
🟢
اجرای Real Delay Test و تست سرعت در پس‌زمینه و هنگام خاموش بودن صفحه
📱
دانلود از گیتهاب</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/whitedns/1817" target="_blank">📅 11:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1815">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⭐️
چطور API رایگان DeepSeek V4.1 Flash بگیریم؟
توی این ویدیو، قدم‌به‌قدم نشون می‌دم چطور به API این مدل دسترسی رایگان بگیرید؛
اگه با API آشنا نیستید، خیلی ساده یعنی به‌جای اینکه فقط توی سایت با هوش مصنوعی چت کنید، بتونید ازش داخل برنامه‌ها و ابزارهای خودتون استفاده کنید.
چه بخواید ایده‌ای رو تست کنید، چه روی یک پروژهٔ شخصی کار کنید یا تازه کار با API رو یاد بگیرید، این آموزش می‌تونه نقطهٔ شروع خوبی باشه.
📹
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/whitedns/1815" target="_blank">📅 22:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1812">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✍️
موقت
دوستان هم نسخه مبایل و هم دسکتاپ برای کارایی بهتر اول ورژن قدیمی را uninstall کنید و بعد نسخه جدید را نصب کنید
در نسخه ویندوز موقع uninstall کردن حتما گزینه delete app data را بزنید
ممنون</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/whitedns/1812" target="_blank">📅 16:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1811">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/g_SrzWdJ3US2BuKTKQG1GMG_HNmjYzcyHhdDmHoww_SP5UP3Gj5e4pFGzVV8KNQXNRsS7lVQ_AH5fwZ90wg91kncHhPQ-JR5xXYht3BGwjdhfs-uHRCP0h36Zti1iO-EqieZWhhSGef3KyaXu89X0kUBNsZXfmJKZV3Xft32srX7yYeBBCFIA_Rjo5SdPqs4PdJEQck6eNShDiA_2dihtVj8_uR09zMka40O9z_OQWqSwhdITlKzixF9EuDqPLck-2smxzA0y8vbkzUBuEHqDFklIMkkRla4u7cCqcb-EQr_O8lojTtyMO-wzzvV-_TNE549E_UBkFptF2GokgryiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
WhiteAesther Mobile ۱.۸.۰ نسخهٔ پایدار
این نسخه دو کار را با هم می‌آورد: هرچه در نسخهٔ آزمایشی ۱.۷.۰ بود، به‌علاوهٔ یک راه خروج تازه. اگر روی ۱.۶.۱ هستید، هر دو را یک‌جا می‌گیرید.
⚡️
اتصال روی شبکه‌هایی که تا حالا جواب نمی‌دادند
حالت خودکار حالا واقعاً خودکار است. از همان لحظهٔ زدن دکمه، اتر و سایفون و تور را هم‌زمان می‌فرستد و هرکدام زودتر ترافیک را رد کرد همان می‌ماند. تشخیص اینکه کدام مسیر واقعاً کار می‌کند هم دقیق‌تر شده — دیگر یک مسیر سالم را به اشتباه کنار نمی‌گذارد.
این حالت از این نسخه پیش‌فرض روشن است. اگر خودتان قبلاً حاملی انتخاب کرده‌اید، انتخابتان دست‌نخورده می‌ماند.
🧅
ماسک در ماسک — راه تازه
یک پروتکل جدید برای شبکه‌ای که یاد گرفته یک تونل ماسک تنها را بشناسد. دو پرش تودرتو: پرش داخلی از دل بیرونی دست می‌دهد، پس چیزی که شبکه می‌بیند یک تونل است که محتوای مبهم حمل می‌کند، نه الگویی که آموزش دیده دنبالش بگردد.
هم در فهرست پروتکل‌ها هست، هم آخرین چیزی که حالت خودکار امتحان می‌کند — و بخش دوم مهم‌تر است: شبکه‌ای که این برایش ساخته شده همان جایی است که بقیهٔ راه‌ها شکست خورده‌اند، و کسی سراغ تنظیمات پیشرفته نمی‌رود. پس خودکار خودش به آن می‌رسد، بعد از اینکه راه‌های سریع‌تر نوبتشان را گرفتند.
از یک پرش کندتر است و عمداً آخر است. جایی که یک پرش کار می‌کند، چیزی برای شما عوض نمی‌شود.
🧠
موتور اتر ۲.۰
هستهٔ برنامه یک نسخهٔ کامل جلو رفت: سرعت عبور ترافیک روی تونل‌های TCP بیشتر شده، یک لایهٔ تازهٔ دور زدن تشخیص پیش از دست‌دهی اضافه شده، و پایداری تونل‌های تودرتو بهتر شده است.
🌍
کشور خروج روان‌تر
فهرست کشورها بلافاصله به‌روز می‌شود، «بهترین گزینهٔ موجود» همیشه در دسترس است، و اگر کشوری که انتخاب کرده‌اید در دسترس نباشد برنامه صریح می‌گوید به‌جای اینکه بی‌صدا تلاش کند.
🛡
پایدارتر
اتصال مجدد بعد از قطعی، حفظ تنظیمات محافظتی پس از راه‌اندازی دوبارهٔ سیستم، و رفتار دقیق‌تر هنگام جابه‌جایی بین وای‌فای و دیتا.
━━━━━━━━━━
📥
دریافت
برنامه خودش این نسخه را به شما پیشنهاد می‌دهد. اگر می‌خواهید همین حالا بگیرید:
برای تقریباً همهٔ گوشی‌های امروزی:
WhiteAestherMobile-1.8.0-arm64-v8a.apk (۴۵ مگابایت)
اگر نصب نشد، فایل universal را بگیرید — روی هر گوشی کار می‌کند ولی حجمش بیشتر است.
🔗
github.com/WhiteDNS/WhiteAestherMobile/releases/latest
روی نسخهٔ فعلی نصب می‌شود و تنظیماتتان می‌ماند.
#WhiteAesther
#v1_8_0
@whitedns</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/whitedns/1811" target="_blank">📅 16:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1810">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/NemUUsuQMksEr8drn1ZKEie2XKYr6fOFKP8n1y51hqMUXOGPv4M8wxni3cfvYoAiJTjarRtR9Wz9l468I9zyy3L_cyL6g9wn5YPsUf5BP065_whQSOQTjKtDLk0sR30PVEbQPYctVenr6DTydP27dS_cJ-2DxB648i1a4cORbSB_ggv_2VuSHvT7Aph02xolIhOdtqpm6OS6OQFfg3guHZFllsD9ltYenxJRQJzHbwiMlzdFrF5UWcwP88awhfFFivp3gFyQlAXQS3mEj7K0c5ad8TT8xxSdPmcWHOMjcuwyuksF7jJvoPJr8CGQMqU9PXzvgdlY3-4AOokWQRMAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
WhiteAesther Desktop 1.9.4 — نسخهٔ پایدار
بزرگ‌ترین تغییر از زمان ۱.۹.۱، و دقیقاً همان چیزی است که بیشتر کاربرها لازم داشتند.
دیگر لازم نیست بدانید کدام راه کار می‌کند
تا امروز اگر وصل نمی‌شدید، باید می‌رفتید در تنظیمات پیشرفته و بین Aether و سایفون و تور یکی را انتخاب می‌کردید. بیشتر مردم اصلاً نمی‌دانستند این گزینه‌ها وجود دارند و فقط فکر می‌کردند برنامه کار نمی‌کند.
حالا فقط اتصال را بزنید. برنامه هر پنج راه خروج را هم‌زمان امتحان می‌کند و اولی که واقعاً ترافیک حمل کند نگه می‌دارد.
قبلاً یکی‌یکی امتحان می‌شدند: اگر Aether بیرون نمی‌رفت، باید سه دقیقه صبر می‌کردید تا نوبت سایفون برسد. حالا همه با هم شروع می‌شوند و معمولاً چند ثانیه‌ای تمام است.
🆕
یک راه خروج تازه: MASQUE در MASQUE
بعضی شبکه‌ها یاد گرفته‌اند یک تونل MASQUE را بشناسند و ببندند. این حالت دو تونل تودرتو می‌سازد که از داخل هم رد می‌شوند.
لازم نیست انتخابش کنید — جزو همان پنج راهی است که خودکار امتحان می‌شود. روی شبکه‌ای که بقیه بسته‌اند، ممکن است تنها راهی باشد که باز می‌شود.
⚡️
موتور به نسخهٔ ۲ رفت
هستهٔ Aether از ۱.۸ به ۲.۰ ارتقا یافت. محسوس‌ترین اثرش سرعت است: بسته‌های بزرگ‌تر روی MASQUE H2 و دست‌دادن سریع‌تر.
🔒
حالا مطمئن می‌شویم چه کسی جواب می‌دهد
قبلاً برنامه یک مسیر را «کارکن» حساب می‌کرد اگر چیزی از آن برمی‌گشت. ولی روی شبکه‌ای که ترافیک را شنود می‌کند، خودِ شنودکننده هم جواب می‌دهد — یعنی ممکن بود همان مسیری انتخاب شود که در حال خوانده شدن است.
حالا از سایتی که به آن وصل می‌شود می‌خواهد هویتش را با گواهی ثابت کند؛ چیزی که فقط سایت واقعی می‌تواند ارائه دهد.
🐧
و برای کاربران لینوکس
پیام خطای «تونل کامل» دیگر شما را دنبال دکمه‌ای که روی لینوکس وجود ندارد نمی‌فرستد. حالا می‌گوید واقعاً چه کاری از دستتان برمی‌آید.
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases/latest
@whitedns</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/whitedns/1810" target="_blank">📅 16:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1807">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">💬
تقریبا ۵۰۰۰ هزار کاربر فعال از کشور روسیه داریم که روانه دارن از WhiteVPN استفاده میکنند.
اونا هم اندازه ما دردسر فیلتر دارن، اما با توجه به «چراغی که به خانه رواست ...» از ورژن بعدی دسترسی کشور های دیگرو به اپ میبندیم.
• از ورژن بعدی میتونید اپ رو ببندید و پشت صحنه اسکن انجام میشه.
• آپدیت داخلی و اتومیاتیک به اپ اضافه شده
• بکسری تغییرات کوچیک دیگه
💬
اگر مشکلی داشتید که به ما گزارش دادید و ما فیکس نکردیم، لطفا برامون بفرستید.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/whitedns/1807" target="_blank">📅 09:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1805">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">💬
دوستان ما هرشب سرور های اختصاصی رو روی WhiteVPN بروز میکنیم تا از فیلتر شدن سرور ها جلوگیری کنیم.
متاسفانه این‌چند روز سرور سنگاپور رو نداریم ، توی یک شب ۳۰ ترابایت مصرف شد و هزینه زیادی داشت. وقتی خاموشش کردیم، دیگه سرور سنگاپور ارایه نمیداد.
باید دوباره موجود بشه و براتون یکی به زودی میسازیم.
🔒
اگر براتون مستقیم وصل نمیشه، به یک سرور عمومی وصل بشید و اختصاصی رو زنجیر Chain بکنید تا آی‌پی ثابت بگیرید.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/whitedns/1805" target="_blank">📅 02:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1793">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qp1sio4pkv0vVEnVwBL7Eq-mZEecOXax3XOyY-pAnbvh31pF0vD1ps71RjgxCUBOOEHqhA6csT1xeqZUAcrnHfJpNQKGT8Kp_6g8CWqb4nF80pBKE0YopBF3Z0v26kWx2qNhyd6zImSy148c4aAkFPxY3dJ65BzWpBiwwyzKR_ByJBQx2sZhV4JRjYkVMAple-rTcq2HZ26OTPYWMpa5QBo6KE0LBKxE46iCymnFhwr0KkNJD9Q5u22a6RoK2t42ObRvSdPrgWMr1FTb5Yerkx-54jx-XeMv6cqrCJ8vQB5Uo7X3cmanDJMW6oCzx_cAuhlsOt067CMV_dmRlV1HnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
اگر به هر دلیلی نیاز به کانفیگ (cottondns,masterdns,stromdns) برای اپ
WhiteDNS
دارید از ربات زیر میتونید با محدودیت حجم و روزانه کانفیگ بگیرید.
⚠️
این کانفیگ 1 روزه و با حجم 0.5 گیگ هست
در حال حاضر تعداد کانفیگی که میتونیم بدیم خیلی محدود است و فقط با تاییدیه ادمین برای شما ارسال میشه
⛔️
لطفا اگر اشنایی ندارید و کنکجاوید و یا میخواید ازمایش کنید و... درخواست ندید
@MasterDnsManager_bot
WhiteDNSاپلیکیشن
دانلود اندروید
•
دانلود دسکتاپ
@whitedns</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/whitedns/1793" target="_blank">📅 09:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1790">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Zho5beFcB2USN_w_oZmvf7NUDQHEXKVfDxCK1kVKhNTiH6c0nwVFPnhDfQE7kkbf1q1_Ohc8PrO-kV5kD8WzTYQdbWGdn9spL5yDhbSrauzZLmn7mLbUOpxmLUQ5cMncvqxXDra8ZMSJuKIXsKtAHrCoC49V1UMr2Q-I-pMJMr6tfEQbmvKCj3hvNNQPlf81OwAJ455mJf6iTqig7uh69jl5No-YKrRrsVkQ-Qwafn6ma8bMdK6ztlXasDXRNGmcSCxSZsfgBkNHa_YlAWMRstqIglVoVnriMmyvLP2o1tbY1uSPLix3GEEtxlbv5raIT-p-W9Vu2SyqYbVhjfSLGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
🤖
قابلیت جدید : (نسخه ازمایشی )
⚠️
⚠️
⚠️
گفت‌وگو با هوش مصنوعی در ربات
🔥
WhiteDNSResponder V.5
نسخه ازمایشی حتما باگ هایی دارد  و  دچار اشکالاتی خواهد شد که با پشنهادات و کمک شما هر روز بهبود خواهد یافت
👀
از این پس می‌توانید مستقیماً داخل ربات با هوش مصنوعی گفت‌وگو کنید، سؤال بپرسید، متن تولید یا ترجمه کنید و درباره موضوعات مختلف توضیح بگیرید.
این امکان جدید به صورت محدود و با درخواست کاربر فعال میشود.
⚠️
@WhiteDnsResponder_bot
🔐
نحوه درخواست دسترسی
1️⃣
وارد گفت‌وگوی خصوصی ربات شوید.
2️⃣
از منوی ربات گزینه /airequest را انتخاب کنید.
3️⃣
درخواست شما برای مدیر ارسال می‌شود.
4️⃣
پس از تأیید، دسترسی به‌صورت خودکار فعال شده و نتیجه از طریق ربات به شما اعلام می‌شود.
نیازی به پیدا کردن یا ارسال شناسه عددی تلگرام نیست.
🔹
روش استفاده
پس از فعال‌شدن دسترسی، سؤال خود را بعد از دستور /ai بنویسید:
/ai تفاوت DNS و VPN چیست؟
یا:
/ai یک متن رسمی برای درخواست همکاری بنویس
🔹
دستورات کاربردی
/ai سوال شما
شروع یا ادامه گفت‌وگو با هوش مصنوعی
/ainew
پاک‌کردن گفت‌وگوی قبلی و شروع مکالمه‌ای تازه
/aistatus
مشاهده سهمیه روزانه، میزان مصرف و تعداد درخواست‌های باقی‌مانده
📊
محدودیت‌های فعلی
• سهمیه روزانه براساس تأیید مدیر: ۵ یا ۱۰ پیام
• حداکثر ۳ درخواست در هر ۵ دقیقه
• حداکثر ۲۰۰۰ نویسه برای هر پیام
• نگهداری موقت چهار بخش قبلی مکالمه برای ادامه بهتر گفتگو
• قابل استفاده فقط در گفت‌وگوی خصوصی با ربات
• سهمیه روزانه در نیمه‌شب به وقت UTC تمدید می‌شود
🔒
امنیت و حریم خصوصی
• هوش مصنوعی به سرور، فایل‌ها، دستورات سیستمی یا اطلاعات خصوصی تلگرام شما دسترسی ندارد.
• متن مکالمات توسط این قابلیت در پایگاه داده ذخیره نمی‌شود.
• تنها شناسه کاربر، وضعیت دسترسی و میزان مصرف سهمیه ثبت می‌شود.
• لطفاً رمز عبور، اطلاعات بانکی، کلید API یا اطلاعات محرمانه ارسال نکنید.
⚠️
این قابلیت فعلاً به‌صورت محدود و آزمایشی ارائه می‌شود. درخواست‌های تکراری ارسال نخواهند شد و در صورت استفاده نادرست یا ارسال خودکار پیام‌ها، دسترسی کاربر ممکن است غیرفعال شود.
🤍
WhiteDNS — دسترسی ساده‌تر به ابزارهای کاربردی هوش مصنوعی</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/whitedns/1790" target="_blank">📅 15:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1789">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✍️
موقت
اگر روی ویندوز و یا اندروید نسخه قدیمی دارید
⚠️
⚠️
ویندوز :
گزینه reset app data را بزنید و بعد uninstall کنید و جدیدترین نسخه را نصب کنید
اندروید :
حتما ورژن قدیمی را uninstall کنید و ورژن جدید را نصب کنید
@whitedns</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/whitedns/1789" target="_blank">📅 04:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1787">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✍️
موقت
برای جمینای و بقیه هوش مصنوعی ها بر اساس تستی که کردیم روی سایفون و تور راحت باز میشه - اگر تور و سایفون مستقیم وصل نمیشه اول با اتر وصل بشید و بعد خروجی را روی سایفون و یا تور تنظیم کنید.
در ضمن اگر روی یک اپراتور جواب نمیگیرید حتما حداقل یک اپراتور دیگه را هم تست کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/whitedns/1787" target="_blank">📅 19:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1785">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-poll">
<h4>📊 امشب ساعت 8 به وقت ایران لایو بگذاریم جواب سوالات را بدیم ؟</h4>
<ul>
<li>✓ بله😍</li>
<li>✓ خیر😢</li>
</ul>
</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/whitedns/1785" target="_blank">📅 14:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1784">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/eoekw0iPTwHRphwjoMALbM1S8yimJEHWIS0lu8-DhGMccZ9oUnL0RbcXuwRkd7UOHM8-qmZTYPOoNhvRninB4Rwvh1tr9amo16WX7cC5giRKRi-jJlfZZGSbqho8rcrheTg5RNer1ovfbT70SabgVoTYOA6HWsS-NtE-SHj-qNb-lkwDnlBkUENrsNEddoHI5pfJWLGq3PpLFw-iQ-qXH5Vlfkv96eyPy7aVLJDujXfaaTHUIfO2PQiRMyYczEM13aUlS79tucKHjtJJWZtyEG0w_WtgQ9QoSQV5TrTgMXS15TBUEHq7Bi0Z48kZSF0DL10kbsiQ2UUVkQZJFG06DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات پاسحگو
💬
Support Bot:
@WhiteDnsResponder_bot
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری
⚠️
⚠️
whitedns app config bot  :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/whitedns/1784" target="_blank">📅 14:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1778">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cQP5owGeKfN6juYKGGyk3IxONNZJFLAfby2OakHh45bNB11tId5-pXkHJwF-CmUVVfklSzUExjYf11XupnE3ACsHEd381Xym0eZTdAUxx8bhwrrON8zeYD9GITmx4kyp8D2blxgXWOcOnYlpeBH1ko2zLEPjVn3Y9bf5TaIAchKRcEMpk5GPN5OpyJ5FFKajV25e5IBegd17eclVOGPrkC5vOccIyHQ__kwQAAdfxUeeEJDLW-A9Lz1fUchaXW-ixhWPtssrYECn6LI0_TkytNPEJN6vZ4tbGjq4VbHi3FXNriPrzX500gVkNCKIFmsUstPgxruyVt3xyKV2XFaX0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
WhiteAesther mobile 1.6.1 (stable)
دوستانی که منتظر اپدیت بودند الان میتونند اپدیت کنند
⚠️
✨
چه چیزی جدید است؟
🔗
زنجیره کردن دو حامل
حالا می‌توانید دو حامل از بین اتر، سایفون و تور را پشت سر هم وصل کنید، به هر ترتیبی. حامل اول چیزی است که شبکهٔ شما می‌بیند و حامل دوم چیزی است که سایت‌ها می‌بینند.
مسیرها ← حامل ← «خودم انتخاب می‌کنم»
⚡️
سایفون بهتر
سایفون به سرورهای بیشتری دسترسی دارد و زمان بیشتری برای پیدا کردن راه خروج می‌گذارد، پس روی شبکه‌هایی که قبلاً وصل نمی‌شد شانس بیشتری دارد.
🤖
حالت خودکار (آزمایشی)
اگر روشنش کنید، برنامه خودش اتر، سایفون و تور را هم‌زمان امتحان می‌کند و راهی را انتخاب می‌کند که واقعاً اینترنت از آن رد شود. راهی که روی هر شبکه کار کرد را هم یادش می‌ماند و دفعهٔ بعد سریع‌تر وصل می‌شود.
فعلاً پیش‌فرض خاموش است تا بیشتر امتحان شود. برای روشن کردن: مسیرها ← حامل ← «خودکار (آزمایشی)»
🛠
اگر نسخهٔ آزمایشی ۱.۶.۰ را نصب کرده بودید و وصل نمی‌شدید، این نسخه آن مشکل را برطرف می‌کند.
💡
نکته
اگر اتر روی اینترنت شما وصل نشد، سایفون را امتحان کنید:
مسیرها ← حامل ← «خودم انتخاب می‌کنم» ← سایفون
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.6.1
• بیشتر گوشی‌ها: WhiteAestherMobile-1.6.1-arm64-v8a.apk
• اگر مطمئن نیستید: WhiteAestherMobile-1.6.1-universal.apk
روی نسخهٔ فعلی به‌روزرسانی می‌شود و تنظیمات شما می‌ماند.
🐞
اگر مشکلی دیدید: تنظیمات ← تشخیص ← «ارسال برای توسعه‌دهنده»، و بنویسید چه اینترنتی دارید (همراه اول، ایرانسل، وای‌فای خانگی و…).
@whitedns</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/whitedns/1778" target="_blank">📅 14:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1777">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/VkKVp9nsueyO-vdRs5B2qswewUTifx5Sin-cSW3Rhr9u2LMo5jy68l_TsHKZJ8ZOPnMzRsvFVaImg21cKlHZ90wvWITSQZknnNhyL8OTLqNsBqAJvucjLKYasHJ-7-G8JdLUXpfbC9r1ss-4fvYiPlZuZyNKhokZR6vYpMfaoQb4iJ_lOyyivMDiCzdy8cuuWq85R5f34m4m1xEBjilvXndJc9GBnqprPP2jVlI11OfWfT-hhCJ_XWmFxzYpsBkvfuK9c5isVeLWXnKRfE3_adqMQibN1sOc_L5TUZJ0Btlqm7IG14k_qsci1_eepCE8ijKYHVmKrvbisGPcsErc1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther desktop  1.9.1 (stable)
🔥
دوستانی که منتظر اپدیت بودند الان دیگه میتونند اپدیت کنند
⚠️
پنج ایراد درست شد که سه‌تایشان را فقط وقتی می‌دیدید که شبکه سخت می‌شد.
دکمهٔ «یکی که کار می‌کند را پیدا کن» حالا واقعاً می‌گردد
تا امروز، جست‌وجو روی همان گزینهٔ اول می‌ایستاد و می‌گفت وصل شد — حتی وقتی نشده بود. هیچ‌وقت به سایفون، تور و شش ترکیب زنجیره‌ای نمی‌رسید. حالا هر راه را تا آخر امتحان می‌کند، و یکی را فقط وقتی قبول می‌کند که یک درخواست واقعی از آن رد شده و برگشته باشد.
⚠️
یک نشتی در حالت زنجیره‌ای بسته شد
اگر پروتکل را روی WireGuard یا MASQUE H3 گذاشته بودید و بعد سایفون یا تور را جلویش می‌گذاشتید، Aether از کنار آن کریر بیرون می‌رفت — یعنی از همان آدرسی که زنجیره برای پنهان کردنش وجود داشت. حالا پشت هر کریری خودکار روی MASQUE H2 قفل می‌شود.
به هر کریر همان‌قدر وقت داده می‌شود که لازم دارد
جست‌وجو قبلاً هر تلاش را سر ۹۰ ثانیه می‌برید، در حالی که سایفون در اولین اتصال روی شبکهٔ سخت تا ۵ دقیقه وقت می‌خواهد. نتیجه‌اش این بود که روی سخت‌ترین شبکه‌ها — دقیقاً جایی که این دکمه برای آن ساخته شده — هیچ‌وقت جواب نمی‌داد.
و چند چیز کوچک‌تر
• جست‌وجو ساعت نشان می‌دهد و از اول می‌گوید چقدر ممکن است طول بکشد
• سایفون می‌گوید اولین اتصالش روی شبکهٔ سخت چند دقیقه است، تا فکر نکنید هنگ کرده
• عمق جست‌وجو (از turbo تا thorough)
حالا واقعاً رعایت می‌شود
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.1
ویندوز → .exe
مک (اپل سیلیکون) → macos_arm64.dmg
مک (اینتل) → macos_x86_64.dmg
لینوکس → .AppImage یا .deb / .rpm
@whitedns</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/whitedns/1777" target="_blank">📅 14:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1776">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Q26TCT7KtG_uekLNxKo9JEPVwI7aVRDcmOgtyQUIu28KLDkZfsJxNx1g1JTXXMwJGV5VHbmOQc51C-4Ij0WujWmytCupYJHhUEdsqzWXCRSLTGalN1wvy3tdpBTBITJ9YzPwAfSXaMO9-DN2CjQS-k5t-ZMPw2Lhv428bEWJl3lxLWp-J9iqQyo-UEupMvdliuYOOmFQUKmMUaYZGR9CWWTkLcSoEKeiUaDxLdX60kZmAoQmmt4NxCChv280OUxtp9IGGLkCIINNArlVQ_tZBWzxjkAzQj2BQViEi2mI2NlsAQHY2bCQlTNY__DnTScHUTWRXVdh56eF_2q1QaBmSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه پایدار WhiteAesther به‌زودی منتشر می‌شود!
🚀
تجربه‌ای سریع‌تر، امن‌تر و مطمئن‌تر در دسکتاپ و موبایل. منتظر باشید
💚
@whiteaesther</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/whitedns/1776" target="_blank">📅 13:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1772">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/uIcWG4OVefRtlET_S3tmESYAOzaPMNyxU8B-DBPsNAfq4psDxCPQf7vgAxPal3TesWRzCS3Cdu3O47qOgzRP9yWVS4eCnNOCGEyuo4Y1Kayccl02R-VnMLIxOccgmg-7PGuCwRoMWIte3dKrgnKRmlSHmS5nEo6ocKElOo9SBNFnunTaDD1tLdXWikniM_DAzKBOThZ8-9ML-S_dKykrrKqadT49FeogKWZ7-wHHCw3AZMEq5wVF46tKQ_r5RYqfx04O8QTJnJ0PNlABWW1jHkUZhMgv2FyZWM8WZxAvtJ984r7UrWoDdmUZmS8G6xTvfFmc9jdEma_ZQ7DMyRfBJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتیم برای WhiteDNS یه Patreon راه بندازم.
حدود ۷ ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱۰ هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://www.patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/whitedns/1772" target="_blank">📅 16:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1771">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دوستان :
⚠️
⚠️
اگر پست ها را کامل نخوندید . لطفا توی گروه ها پیام ندید . چون کاملا مشخص هست خیلی از دوستان حتی 10 ثانیه هم وقت نگذاشتند . این مدل پیام دادن فقط باعث گمراهی بقیه میشه . لطفا کاملا پست ها را مطالعه کنید .برنامه را کاملا بررسی کنید . تنظیمات متفاوت را انجام دهید وفقط با توجه به روشی که توی پست های بالا گفته شده گزارش کنید
سپاس</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/whitedns/1771" target="_blank">📅 16:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1770">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/NqsFcMMwq_KmYXn7iyHnJ6NHh6KNFqZ9mn0h4yAp11VMOkiN0i3wVbkpP5x7ZXhBoV2ZPkHsdzvj8CevaXzTw43cZiYug2banExrJVlHOlHTAi1-hcbbho04esEDReEcs6Jdbf8CIPbHQ6-daDlyAU6BeqKfMrhosiolWBmhOjTkjPoqjOCJJDDct1IguAwn7Vuu75Z2U9IyT_9fRqjP4WTz6NxKuVfTedrRcnarwp0AXGb_LzfH58YckvnHdiburZ86KPhhmZrb55lVP8RlFFxxUAizY_s075f6nExoyTpGDIAwl91FvyQX2KRWx1TEsHtObrUdA1fa_VhfTywxkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا توی نسخه اندروید هم شما حالت اتوماتیک دارید ، خودش می‌گرده و بهترین حالت را انتخاب می‌کنه و وصل میشه
#WhiteAesther_Mobile_1
.6.0</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/whitedns/1770" target="_blank">📅 15:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1769">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🧪
نسخهٔ آزمایشی WhiteAesther Mobile  1.6.0
حالت خودکار: فقط دکمهٔ اتصال را بزنید
🔥
🔥
🔥
🔥
⚠️
این نسخه آزمایشی است و ممکن است باگ داشته باشد. داخل برنامه اعلان به‌روزرسانی برایش نمی‌آید و فقط از لینک پایین نصب می‌شود.
✨
چه چیزی جدید است؟
دیگر لازم نیست بدانید اتر، سایفون یا تور کدام روی اینترنت شما کار می‌کند. در حالت «خودکار» برنامه خودش اول اتر را امتحان می‌کند و اگر نشد سایفون و تور را، و راهی را انتخاب می‌کند که واقعاً اینترنت از آن رد شود.
راهی را هم که روی هر شبکه کار کرد یادش می‌ماند؛ دفعهٔ بعد روی همان وای‌فای یا همان سیم‌کارت خیلی سریع‌تر وصل می‌شود.
📱
استفاده
برای بیشتر کاربران خودکار از قبل روشن است؛ فقط دکمهٔ اتصال را بزنید.
اگر قبلاً حامل را دستی انتخاب کرده‌اید: تب «مسیرها» ← کارت «حامل» ← «خودکار (پیشنهادی)».
⏳
اولین بار روی یک اینترنت سخت ممکن است چند دقیقه طول بکشد؛ لطفاً صبر کنید. روی صفحه نوشته می‌شود الان کدام راه را امتحان می‌کند.
🐞
اگر مشکلی دیدید: تنظیمات ← تشخیص ← «ارسال برای توسعه‌دهنده»، و بنویسید چه اینترنتی دارید.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.6.0
• بیشتر گوشی‌ها: WhiteAestherMobile-1.6.0-arm64-v8a.apk
• اگر مطمئن نیستید: WhiteAestherMobile-1.6.0-universal.ap
@whitedns</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/whitedns/1769" target="_blank">📅 15:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1768">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/oO2j-ZfgWIrRJul7tAVtaKNPNMv6xqGcBxGt-cyOF9feU0KYRtgcBmAyMQBdGLvQ4BaCH6Pm-HeuzGUWUBXFzC7irs6fFxNkX4DEFkIDKiBT7Dpd9PUmck3tHexj5bnGyjvuuDo0S5pZ15kL4WdVGiqAPwiv9jgSrel0n-zgoJkIXUsmTKOPYfoenifrj_28KrftBss9j2pCud94-1N_a6vUeqHL4Or5VYx2kmpEsl_JLokbr_TgwQCIgQTP1lIKrIVJhP1TAdzkC0F8i-qMUnY6oqw2N7tgpqKO3NXYdDHE9W4JuWX63vvUiFzw6-xV-8f1F-CDdwxaC7k_iQH1jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی نسحه دسکتاپ یک گزینه اتوماتیک ما داریم . که خودش بهترین کانکشن را براتون پیدا میکنه
#
WhiteAesther_desktop_1
.9.0</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/whitedns/1768" target="_blank">📅 14:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1767">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دوستان :
اموزش هایی که ما توی پست های کانال میگذاریم به خدا برای شماست - والا ما خودمون بلدیم !
خواهشا وقت بگذارید مطالعه کنید</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1767" target="_blank">📅 14:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1766">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-poll">
<h4>📊 توی این نسخه ازمایشی whiteaesther مشکل شما برای اتصال و استفاده از هوش مصنوعی حل شد ؟</h4>
<ul>
<li>✓ 😏اتصال اوکی شد ولی هوش مصنوعی کار نمیکنه</li>
<li>✓ ❤️هوش مصنوعی و اتصال اوکی شد</li>
<li>✓ کلا نتونستم وصل بشم😢</li>
</ul>
</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/whitedns/1766" target="_blank">📅 14:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1762">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🧪
نسخهٔ آزمایشی
WhiteAesther mobile 1.5.0
⚠️
⚠️
⚠️
⚠️
این یک نسخهٔ آزمایشی است و ممکن است باگ داشته باشد. برای همین داخل برنامه اعلان به‌روزرسانی برایش نمی‌آید و فقط از لینک پایین نصب می‌شود. اگر به اتصال پایدار نیاز دارید، فعلاً روی نسخهٔ فعلی بمانید.
━━━━━━━━━━
✨
چه چیزی جدید است؟
۱
. زنجیره کردن دو حامل
حالا می‌توانید دو حامل از بین اتر، سایفون و تور را پشت سر هم وصل کنید، به هر ترتیبی که بخواهید. حامل اول چیزی است که شبکهٔ شما (اپراتور) می‌بیند و حامل دوم چیزی است که سایت‌ها و اینترنت می‌بینند.
۲. سایفون بهتر
سایفون حالا به سرورهای بیشتری دسترسی دارد (از جمله سرورهای داوطلبانهٔ Conduit) و زمان بیشتری برای پیدا کردن راه خروج می‌گذارد؛ پس روی شبکه‌هایی که قبلاً وصل نمی‌شد شانس بیشتری دارد.
━━━━━━━━━━
📱
چطور استفاده کنم؟
۱
. به تب «مسیرها» بروید و در صفحهٔ «چطور وصل می‌شود» پایین بیایید تا به کارت «حامل» برسید.
۲. در بخش «اول — چیزی که شبکه شما می‌بیند» حامل اول را انتخاب کنید.
۳. در بخش «بعد — چیزی که اینترنت می‌بیند» حامل دوم را انتخاب کنید. اگر فقط یک حامل می‌خواهید، «هیچ‌چیز دیگر» را بزنید.
۴. با دکمهٔ «ترتیب را جابه‌جا کن» جای دو حامل با یک لمس عوض می‌شود.
۵. «پوشش» باید روی «کل دستگاه» باشد؛ سایفون و تور در حالت «فقط پروکسی» اجرا نمی‌شوند.
۶. به «خانه» برگردید و وصل شوید. آنجا مسیر کامل نوشته می‌شود، مثلاً «متصل از طریق سایفون، بعد اتر»، و وضعیت هر حامل جداگانه نشان داده می‌شود.
━━━━━━━━━━
🔀
کدام ترکیب برای چه کاری؟
🔹
اتر ← سایفون
اتر وصل می‌شود ولی می‌خواهید سایت‌ها آی‌پی خارجی سایفون را ببینند، نه کلودفلر. کشور خروجی را هم می‌توانید در کارت «کشور خروجی» انتخاب کنید.
🔹
اتر ← تور
بیشترین حریم خصوصی، ولی کند.
🔹
سایفون ← اتر
وقتی اتر روی شبکهٔ شما مستقیم وصل نمی‌شود: سایفون راه را باز می‌کند و اتر از داخل آن بیرون می‌رود.
🔹
سایفون ← تور
وقتی تور مستقیم بسته است.
🔹
تور ← اتر / تور ← سایفون
برای شبکه‌هایی که فقط تور (با پل) از آن‌ها بیرون می‌رود. این دو ترکیب کمتر از بقیه آزمایش شده‌اند و نتیجهٔ شما برای ما خیلی ارزشمند است.
اگر یک ترتیب وصل نشد، «ترتیب را جابه‌جا کن» را بزنید و دوباره امتحان کنید. اینکه کدام ترتیب جواب بدهد به شبکهٔ شما بستگی دارد.
━━━━━━━━━━
💡
نکته‌ها
• زنجیره از یک حامل تنها کندتر است. اگر یک حامل به‌تنهایی برایتان کار می‌کند، همان را نگه دارید.
• وقتی اتر حامل دوم است، خودکار از H2 استفاده می‌کند و انتخاب پروتکل اثری ندارد.
• وقتی تور حامل دوم است، اسنوفلیک کار نمی‌کند؛ تور مستقیم، با پل obfs4 یا با پل‌هایی که به شما داده شده وصل می‌شود.
• اولین اتصال سایفون ممکن است چند دقیقه طول بکشد؛ صبر کنید.
• اگر برای سایفون کشوری انتخاب کرده‌اید و وصل نمی‌شود، «بهترین گزینهٔ موجود» را انتخاب کنید.
• اگر در تنظیمات اندروید «VPN همیشه روشن» همراه با «مسدود کردن اتصال‌های بدون VPN» روشن است، ممکن است سایفون و تور وصل نشوند؛ خاموشش کنید.
━━━━━━━━━━
🐞
گزارش باگ
اگر به مشکلی خوردید: تنظیمات ← تشخیص ← «ارسال برای توسعه‌دهنده». لطفاً بنویسید کدام ترکیب را امتحان کردید و روی چه اینترنتی بودید (همراه اول، ایرانسل، وای‌فای خانگی و…).
━━━━━━━━━━
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.5.0
⚠️
در صورت امکان ورژن قبلی را کاملا uninstall کنید و ورژن جدید را نصب کنید تا کاملا بروز شود
⚠️
• بیشتر گوشی‌ها: WhiteAestherMobile-1.5.0-arm64-v8a.apk
• اگر مطمئن نیستید: WhiteAestherMobile-1.5.0-universal.apk
روی نسخهٔ قبلی نصب می‌شود و تنظیماتتان حفظ می‌شود. برای برگشتن به نسخهٔ پایدار (1.4.2) باید اول این نسخه را حذف کنید.
@whitedns</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/whitedns/1762" target="_blank">📅 11:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1761">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🧪
نسخهٔ آزمایشی
WhiteAesther desktop 1.9.0
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
این نسخه «آزمایشی» (Pre-release) است و ممکن است باگ داشته باشد. بنا به درخواست تعداد زیادی از شما، آن را زودتر در اختیارتان می‌گذاریم.
✅
اگر نسخهٔ فعلی برایتان بدون مشکل کار می‌کند، فعلاً نیازی به به‌روزرسانی ندارید.
✨
چه چیزهایی جدید است؟
🔗
زنجیر کردن دو راه خروج
حالا می‌توانید Aether، سایفون و تور را دوتادوتا و به هر ترتیبی پشت هم بگذارید. اولی شما را از شبکهٔ فیلترشده بیرون می‌برد، دومی تعیین می‌کند با چه IP و از چه کشوری دیده شوید.
مثلاً Aether ← سایفون: سرعت Aether برای بیرون رفتن، و کشور خروجِ سایفون.
🔍
دکمهٔ «یکی که کار می‌کند را پیدا کن»
اگر نمی‌دانید روی شبکهٔ شما کدام راه جواب می‌دهد، اپ خودش همه را یکی‌یکی امتحان می‌کند و اولی را که وصل شد نگه می‌دارد.
🟢
سایفون خیلی بهتر وصل می‌شود
خیلی‌ها گفته بودند با اپ خود سایفون وصل می‌شوند ولی با حالت سایفونِ ما نه. علتش را پیدا کردیم: سایفونِ ما نمی‌توانست از پروکسی‌های داوطلبانهٔ خود سایفون (in-proxy) استفاده کند، یعنی همان راهی که در ایران بیشتر از همه جواب می‌دهد. فهرست سرورهایش هم به‌روز نمی‌شد. هر دو مشکل برطرف شد و سایفون حالا برای وصل شدن تا ۵ دقیقه صبر می‌کند (قبلاً ۲ دقیقه بود).
📥
دانلود:
https://github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.0
⚠️
دوستان حتما  delete cache/data را بزنید تا کاملا بروز از برنامه استفاده کنید
⚠️
🪟
ویندوز: WhiteAesther_1.9.0_windows_x86_64.exe
🍎
مک با چیپ M1 و جدیدتر: WhiteAesther_1.9.0_macos_arm64.dmg
🍎
مک اینتل: WhiteAesther_1.9.0_macos_x86_64.dmg
🐧
لینوکس: فایل AppImage یا deb یا rpm (نسخهٔ x86_64 یا arm64)
🐞
اگر به مشکلی خوردید:
دکمهٔ Advanced ← عیب‌یابی ← در بخش «گزارش»، دکمهٔ «ذخیرهٔ گزارش» یا «کپی» را بزنید و برای ما بفرستید. آدرس‌های IP به‌طور پیش‌فرض در گزارش پنهان می‌شوند.
📘
آموزش نسخهٔ 1.9.0
١) کجاست؟
بالای برنامه دکمهٔ Advanced را بزنید ← از منوی کنار، «مسیرها و پروتکل‌ها» ← کارت «راه خروج».
٢) یک راه خروج (مثل قبل)
در ردیف «خروج از این شبکه با» یکی را انتخاب کنید (Aether، سایفون یا تور) و ردیف «و سپس خروج از» را روی «هیچ‌چیز دیگر» بگذارید.
٣) زنجیر کردن دو راه خروج
در ردیف اول چیزی را بزنید که شما را از شبکه بیرون می‌برد، و در ردیف دوم چیزی که می‌خواهید IP و کشورِ خروجتان مالِ آن باشد. زیر این دو ردیف یک کادر دقیقاً می‌گوید این ترکیب چه چیزی به شما می‌دهد و چه چیزی نه.
💾
برای اینکه انتخابتان بعد از بستن برنامه هم بماند، «ذخیرهٔ پروفایل» را بالای صفحه بزنید.
چند ترکیب کاربردی:
• Aether ← سایفون: وقتی Aether وصل می‌شود ولی IP از کشور دیگری می‌خواهید. کشور را از «کشور خروج» انتخاب کنید (فهرست کشورها بعد از اولین اتصال سایفون ظاهر می‌شود).
• سایفون ← Aether: وقتی Aether به‌تنهایی وصل نمی‌شود ولی سایفون می‌شود. خروجتان همچنان نزدیک خودتان است و کشورتان عوض نمی‌شود. شرطش این است که قبلاً حداقل یک بار با خود Aether (بدون زنجیره) وصل شده باشید.
• تور ← سایفون: وقتی نه Aether و نه سایفون به‌تنهایی وصل نمی‌شوند. کندتر است، ولی یک راه دیگر است.
نکته: وقتی تور نفر دوم زنجیره است، از «پل‌ها» استفاده نمی‌کند؛ کارِ بیرون رفتن را نفر اول انجام داده.
نکته: زنجیره‌ای که سایفون یا تور در آن باشد UDP را عبور نمی‌دهد. سایت‌ها و بیشتر برنامه‌ها عادی کار می‌کنند، ولی بعضی تماس‌های صوتی و تصویری یا بازی‌های آنلاین ممکن است کار نکنند.
٤) پیدا کردن خودکار
در همان صفحه، کادر سبز «نمی‌دانید کدام کار می‌کند؟» را پیدا کنید و «یکی که کار می‌کند را پیدا کن» را بزنید.
اپ اول تک‌ها را امتحان می‌کند (Aether، سایفون، تور) و فقط اگر هیچ‌کدام وصل نشد سراغ ترکیب‌ها می‌رود. به هرکدام تا ۹۰ ثانیه فرصت می‌دهد و نتیجهٔ هر تلاش را همان‌جا نشان می‌دهد. هر وقت خواستید، «توقف جستجو» را بزنید.
٥) درباره سایفون
اولین اتصال سایفون ممکن است چند دقیقه طول بکشد، مخصوصاً وقتی از طریق پروکسی‌های داوطلبانه وصل می‌شود. عجله نکنید؛ تا ۵ دقیقه صبر می‌کند.
⚠️
مشکلات شناخته‌شده
• زنجیره‌هایی که به Aether ختم می‌شوند (مثل سایفون ← Aether) ممکن است بعد از چند ثانیه قطع و دوباره وصل شوند (وضعیت reconnecting). روی رفعش کار می‌کنیم.
• ترکیب سایفون ← تور، و قابلیت Kill switch (قطع ترافیک هنگام افتادن تونل) در حالت زنجیره، هنوز کمتر آزمایش شده‌اند.
ممنون که با ما هستید
🤍
گزارش‌های شما مستقیم به بهتر شدن نسخهٔ پایدار کمک می‌کند.
@whitedns</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/whitedns/1761" target="_blank">📅 11:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1759">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">💬
ما قرار داریم روزی ۴ بار سرور های اختصاصی رو عوض کنیم تا همیشه وصل بمونید و سرور ها فیلتر نشن.
✍️
اگر یکدفع دیدید که سرور اختصاصی قطع شد، برید با قسمت ساسکریپشن، بزنید روی ۳نقطه کنار سرور اختصاصی و تازه سازی رو بزنید.   بعدش دوباره وصل بشید.   خود اپ هم…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/whitedns/1759" target="_blank">📅 15:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1758">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/WeI8OaAxK7VAvOGOVJ0ucPxi9OkFWbxhvb36UZHldWpruW7EZ0zE5zP9Ujsej4XGIqNc-IGXKBRe9G9stEDGXwsAAmRVKR41OjCw824EjZbz7wyGtkWLGz5oVwWhYuHmuy1-C5hQHx1zCGa9_uMP8Hei5hY_Efk0ZDuBdn4ornWrDO2DxZrFZd12jPCY6d9YR8zsZUy_uu_RQMUdqqKCjxLO6kXGdHalexqXAuqAZ6chlyraQu06jVZ-68zee78vUH88MU4SkH0nsh4l7ythOV11HYC3pbg1x_OHPbj2I0n_29MRMjDfD9sn_75sZJz46U6TNnapcFjC4YkjCAYDxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخه
WhiteVPN Desktop v1.0.22 منتشر شد
این نسخه چند مشکل مهم را برطرف می‌کند که می‌توانست باعث
عدم اتصال، ذخیره‌نشدن تنظیمات و ناسازگاری برخی کانفیگ‌ها
شود. همچنین از این نسخه،
سرورهای اختصاصی WhiteVPN
هم به نسخه دسکتاپ اضافه شده‌اند.
━━━━━━━━━━━━━━━━━━
در این نسخه چه مواردی اضافه شد و چه باگ هایی رفع شد :
🖥
سرورهای اختصاصی و عمومی، هر دو در دسکتاپ
تا امروز نسخه دسکتاپ فقط از سرورهای عمومی استفاده می‌کرد، در حالی که نسخه موبایل روی سرورهای اختصاصی قرار داشت.
حالا هر دو فهرست داخل برنامه در دسترس هستند و از صفحه
Subscriptions
می‌توانید مشخص کنید از کدام منبع متصل شوید.
نصب‌های جدید به‌صورت پیش‌فرض با
فهرست اختصاصی
شروع می‌شوند.
اگر یکی از فهرست‌ها در دسترس نباشد، برنامه دیگر همان‌جا متوقف نمی‌شود و به‌صورت خودکار منابع دیگر را بررسی می‌کند؛ از جمله:
• فهرست داخلی دیگر
• سابسکریپشن‌های شخصی شما
• کانفیگ‌هایی که دستی وارد کرده‌اید
برنامه همچنین اعلام می‌کند اتصال از کدام منبع انجام شده است. انتخاب اصلی شما تغییر نمی‌کند و در اتصال بعدی دوباره همان منبع امتحان خواهد شد.
━━━━━━━━━━━━━━━━━━
🛠
رفع مشکل «هیچ سروری وصل نمی‌شود»
در نسخه‌های قبلی، اگر روی فهرست داخلی فیلتر
کشور
یا
نوع اتصال
انتخاب می‌کردید و بعد به سابسکریپشن شخصی خودتان می‌رفتید، همان فیلتر روی فهرست جدید هم اعمال می‌شد.
در نتیجه ممکن بود تمام سرورهای شما رد شوند، بدون اینکه مشخص باشد مشکل از کجاست.
حالا هر فهرست تنظیمات و فیلترهای خودش را نگه می‌دارد.
وقتی وارد فهرست دیگری می‌شوید، آن فهرست از حالت
Automatic
شروع می‌شود و وقتی برمی‌گردید، انتخاب قبلی شما همچنان حفظ شده است.
━━━━━━━━━━━━━━━━━━
⚙️
رفع مشکل ذخیره‌نشدن تنظیمات
برخی گزینه‌های صفحه Settings تغییر می‌کردند، اما پس از خروج از صفحه به حالت قبلی برمی‌گشتند.
این مشکل برای گزینه‌هایی مثل:
Amnezia Noise
و
این‌ها مستقیم خارج شوند
برطرف شده است.
حالا تغییرات مثل نسخه موبایل، به‌درستی ذخیره می‌شوند.
━━━━━━━━━━━━━━━━━━
🔗
پشتیبانی بهتر از کانفیگ‌ها
پشتیبانی از موارد زیر اصلاح و کامل‌تر شده است:
anytls
socks
HTTP Proxy
قبلاً کانفیگ‌های anytls ممکن بود اصلاً در فهرست نمایش داده نشوند.
کانفیگ‌های socks و HTTP Proxy هم ذخیره و نمایش داده می‌شدند، اما هنگام اتصال به‌درستی کار نمی‌کردند.
این مشکلات در نسخه جدید برطرف شده‌اند.
━━━━━━━━━━━━━━━━━━
🐧
رفع مشکل آیکون Tray در لینوکس
در برخی نسخه‌های لینوکس، کلیک روی آیکون WhiteVPN کنار ساعت باعث بازگشت پنجره برنامه نمی‌شد.
این مشکل در نسخه 1.0.22 برطرف شده است.
━━━━━━━━━━━━━━━━━━
⚠️
کاربران لینوکس، این بخش را حتماً بخوانید
نام فایل‌های لینوکس تغییر کرده است.
فایل‌های بدون پسوند amd64 و arm64 حالا از
WebKitGTK 4.1
استفاده می‌کنند و مناسب سیستم‌های جدید هستند، از جمله:
• Ubuntu 24.04 و جدیدتر
• Debian 13
• Fedora 40 و جدیدتر
اگر از
Ubuntu 22.04
یا
Debian 12
استفاده می‌کنید، نسخه webkit40 را دانلود کنید:
WhiteVPN-Desktop-1.0.22-linux-amd64-webkit40.deb
در نسخه‌های قبلی، نام‌گذاری فایل‌های Linux بین amd64 و arm64 یکسان نبود و همین موضوع می‌توانست باعث انتخاب فایل اشتباه و خطای Dependency شود.
این نام‌گذاری حالا اصلاح شده است.
✅
برای کاربران Linux با پردازنده Intel/AMD، ساده‌ترین گزینه همچنان
AppImage
است:
WhiteVPN-Desktop-1.0.22-linux-amd64.AppImage
━━━━━━━━━━━━━━━━━━
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
📥
راهنمای سریع انتخاب فایل
🪟
Windows — Intel / AMD
windows-x64
🪟
Windows — ARM / Snapdragon
windows-arm64
🍎
Mac — Apple Silicon / M1 و جدیدتر
macos-arm64
🍎
Mac — Intel
macos-amd64
🐧
Ubuntu 24.04+ / Debian 13
linux-amd64.deb
🐧
Ubuntu 22.04 / Debian 12
linux-amd64-webkit40.deb
🐧
Fedora / RPM-based Linux
linux-amd64.rpm
━━━━━━━━━━━━━━━━━━
📢
@whitedns</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/whitedns/1758" target="_blank">📅 14:05 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
