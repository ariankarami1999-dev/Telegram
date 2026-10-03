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
<img src="https://cdn1.telesco.pe/file/J-k30NQq2igtmc5N-XPWwloqHI1sJiH_WrDoUSiQUC9pZI3KfHYtcNuKbstpUBvYLb15PyKDrQAOATGrRUV_FOWiGv6NzDx8zjNfcL73P3d3bVKyGxUjF6TNccR-xKXpADIz7rJlgJedKKPwebz6Stv-tLs-6sLVvIIyVFrPA5Avgr4LGYGioJvt3i6MPLBGroPQrfiHAgKyhSqHVtMfzsgvm1dtOQNNi0czCNxmhH_a5GA9jiS8rujWnKR_b8JzDJLw0WigiY3ULf-jQLGITm9JVCWfkcJXgckV01MgsEKVySr0vVZlCIe-kmMX8j-L8LvZU3ANvVtCLxMrnfXdQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 95.7K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 12:49:04</div>
<hr>

<div class="tg-post" id="msg-2638">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LmFXx4kICFC6pO5nz5Ck0rnGjmHWWP2gxjm8USRSmRC4rhbRZwO7mZGDyMnp44ui2i6l-zmfyNjtJds5eqoguO0N1RJXhFjuCU0CSmgBPkI1BLchxs7N0UH5yRpGXlwdE29LbbaWMljur80Bfjmz8cpfcg67EEOXGvnDOIG5AoGrVOYjDxrT7foFrArlUusShS5-Yl4P8OdB5JuLxG2XxjcXxiWFocX3UEO3rfmqUaY1ZPtQ2XAfiunS_bBYhVzWlGYLklxzWgcP1LDDYORwpPq3_tnxLg-JP47l1rv8qVncEgMAl9B-8zEBh8cSPJKkbb2mXhyle6fvlil5Vb_s9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپل از نسخه iOS ۱۸.۱ قابلیتی گذاشته که اگه آیفون ۷۲ ساعت آنلاک نشه، خودش ری‌استارت میشه. این کار باعث میشه اطلاعات گوشی دوباره وارد حالت محافظت‌شده‌تری بشه و ابزارهای فورنزیک مثل GrayKey سخت‌تر بتونن قفل گوشی رو باز کنن.
حالا شرکت Magnet Forensics که سازنده GrayKey هست، ظاهراً راهی پیدا کرده که قبل از این ری‌استارت خودکار، گوشی رو در همون وضعیت نگه داره تا مأموران بتونن فرصت بیشتری برای استخراج اطلاعات داشته باشن. این قابلیت با نام GrayKey Preserve و همچنین Evidence Preservation Mode معرفی شده. البته فعلاً این موضوع بر اساس یک ویدیوی تبلیغاتی لو رفته از شرکت مطرح شده و جزئیات فنی روش منتشر نشده. در واقع جنگ بین اپل و ابزارهای بازکردن قفل گوشی همچنان ادامه داره.
ناگفته نمونه مأموران توی ایران برای باز کردن قفل گوشی بازداشت‌شده‌ها، نیازی به GrayKey و این ابزارها ندارن؛ زور و تهدید راه ساده‌تر و دم‌دست‌تریه واسشون!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2637">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پروژه Nexora یک پنل برای مدیریت چندسروری VPN هست، که تا ۲۵ کاربر و ۱ نود رو بدون نیاز به لایسنس و با تمام امکانات پنل در اختیارتون میذاره و میتونه برای مصارف شخصی یا گروه دوستان یا خانواده قابل استفاده باشه.
نکسورا مدیریت کاربران، نودها، اشتراک‌ها و پروتکل‌ها رو از داخل یک پنل انجام میده و از پروتکل‌هایی مثل VLESS با REALITY، XHTTP و Encryption، VMess، Trojan، Shadowsocks، Hysteria2، TUIC، AnyTLS، Naive، ShadowTLS، Snell، Mieru، MTProxy و SSH پشتیبانی می‌کنه؛ در کنارش پروتکل‌های کلاسیک VPN مثل OpenVPN، OpenConnect و WireGuard هم قابل استفاده هستن.
از قابلیت‌های دیگه Nexora میشه به تانل بین نودها، پشتیبانی از CDN و چند آدرس برای هر نود، همگام‌سازی بدون نیاز به ری‌استارت، Rule-set برای مدیریت ترافیک، مسدودسازی تورنت، محدودیت دستگاه بر اساس HWID و انجام عملیات گروهی روی کاربران اشاره کرد.
برای مدیریت و نگهداری پنل هم امکاناتی مثل احراز هویت دوعاملی، بکاپ رمزنگاری‌شده، بروزرسانی خودکار و Webhook در نظر گرفته شده، امکان مهاجرت از پنل‌هایی مثل S-UI، 3X-UI، X-UI، Marzban، PasarGuard، Hiddify، Marzneshin و Remnawave رو داره و از زبان‌های انگلیسی، فارسی، روسی و چینی پشتیبانی می‌کنه.
👉
github.com/nexora-vpn/panel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2635">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AG8F9V5GNsMI-KO0YVD2UsYX7Rthv_ISEm2KPLDhOsG1kPVy6DiCY_ThKiE7XuLuU0yk9bsnFqKEZSwXABh-qeBlTGu0aBjFT5j2vkXmKs5T6tqAlxcrij8Pa7_9dCajgTEoIZ2zWlQAlQrwmboLRbJOEOJU9fTrdEFmUG5SFeMnDdFSTMbrRsFxnGxWeM39sFRKR_-GvL9l9YOvcLH3CvkUQZjhQZwh6V65VQfenbahAOdWcGx36ovNnRkOw8kG3-uHkxLwesdQEmqCzh0FbJJV9EOENkQ9tMGdTG40C-DmOq0wMYwmAQw8Y4ErdXoXyL_np6uFA_sbT3x1q4j1xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب رسمی مایکروسافت در ایکس با بیش از ۱۳ میلیون دنبال‌کننده هک شد و مهاجما از اون برای تبلیغ یک رمزارز جعلی با نام $Clippy استفاده کردن.
هنوز مشخص نیست چطور به حساب دسترسی پیدا کردن و تحقیقات ادامه داره. مایکروسافت هم اعلام کرده هیچ ارتباطی با این رمزارز نداره و پیگیر اقدامات قانونیه.
©
theverge
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g3UkWrQpsO9ZFJsA5FLCMopwYuW3N5IfNvq-K7rIktyB1s1vMSiwfgzw4a3_uI_WXqEI8_a1XZ5tLPUuAq5BPXbd-RXa-ofBYAPEYuNGh3UWzNF0u6-XtP2T99nt02QyLL7NU4lEuxpVscEZZH3O91HCINAnSipGFVh54WZN_RVaPacxAhpKSf783xlxSfVzMd3j4W1b4-e6Fc4mKbskiUkZerIGmfuXHyvCyaZ7h5BqhddYT162AH4ZNPGTCF6OnhWO5o025Y52-YbNEHAxTs7tDq780ZIme0EiQDiy9n-_C_tITV6ycExgntEjS69m_qsb8f8NhEhefTkaFXigwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dZbXjDegUoCkEt5ctaKksR-f6EGt32UJQbdBwgDFcdh1Nm0vU7lxqMWd8G3UJDWcMXKDz84P42ooymjLWrR6esXghuu9JnOhi0dhu6NNnXQAZ7Vh0gv_NX9sMJNeSWFOhdIPoP1Qv4NKyH-wLj0OQFi2LMJwtqjJ7GB85GHYYVo_Q2HMyKX7Qjg6bIN02gfpnIY26rOY89cOXDcAO3MYndVpcb5LDmtdqRH_sYjmDuY000hl6hAkeRarRKofQm-7rGvREEkeDwqnrNnc3d3xVVswjmnIJ-nV2xLtB_wFjRWuHIRig48vUN-OZmpLvcOuexsNmnw9aCQLqlVJYBykCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه از TeamViewer استفاده می‌کنین، چند آسیب‌پذیری امنیتی با شدت بالا پیدا شده که در بعضی شرایط می‌تونه به مهاجم اجازه دسترسی غیرمجاز و حتی اجرای کد روی سیستم رو بده، که مهمترین مورد CVE-2026-92370 با امتیاز ۸.۸ هست.
فعلاً TeamViewer گفته شواهدی از سوءاستفاده فعال یا انتشار کد اکسپلویت عمومی برای این آسیب‌پذیری‌ها ندیده، اما در نسخه ۱۵.۸۲ این مشکلات رو برطرف کردن و لازمه آپدیت کنید.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GiH_mF8vfYh9h0xb26JBghonPOi7Vbqq7uJJhGuzx5vmmr-zWxdIxaaTt6WOE5Ktxz6-vCZcoZuZrhClaY85RN8JLdRMiIX-AyJARoEQEaP0n_VewLXmStqu9EDMj-zhnl0pXze8geqMmO1JCB1oze7pQT3_vvMl_s55vQRz3w_LFxj6FvKGfMjK9W-WYjdZR_mLNp9h_bnku8AcuRziDg5F0CNiJ_yHK1YbkxDJOVYaWLWizuQG9RB7VMpgYnJABftfIxlUoo5JpW0rvIEHtmCHScoVQFLPKTTdMAFkuPq6CzSS_-FLHybw6bHksKvghlXfftylyzUsbXPkE_1Vlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ج.ا در سال ۲۰۲۶ رسیده به راهکار ماه‌های پایانی حکومت قذافی در برخورد با مخالفان: قطع سراسری برق!
©
ArminSoleimany
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2631">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SaCJCCzBEmRswHUo5JWQL5GsEYl_ebQDFOjCnDQfU-MmMEtBZWSZbNRj3004Deg9yTl9V6CBKk9NKHpDwxtVUQUa41tuYbg0Bmidl4VhTW2LpdXAEXs6YoybdBvV6PZION-OwLT0BL9PqUH6efOIaA9yzuZ1HwA5fHR23gwGb-7uOFBY5wxczubxoRIyvLxYXB9IAdsQXpSJ1VvmNakL2pHBkuPvnW4a9HTTcwB4z1oqgQBC7LLQhyTEqxVb28Zlntg4MSep-EdmLlVwdcuIIbx_IOC-GVPdsRfOtKaSpxw5-ZdpI84H0MUX2a2nyHd7cFgHi_h9-oa8yhXBhwHEXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتیجه این و اون خبر چند وقت پیش در مورد تغییر شرایط استفاده letsencrypt می‌شه گواهی ریشه داخلی و پایان بازی. از مسائل فنی اجرایی صرف نظر کنیم، بحث‌های مهمی باقی است: «حریم شخصی» و «امنیت».
در کشوری که با مداخله در پیامک احراز هویت ۲ مرحله‌ای حساب کاربری مردم رو تصاحب می‌کنند و پاسخگویی هم در نبود قانون و ضمانت اجرایی نیست، امکان جعل گواهی برای شنود به خصوص برای موارد بدون SSL pin هست.
©
Hamed
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W6TL_Bn--Ir9_tRgLX-q8tE3WaIfiEOVM2w5UDMd_s5KxzHxlNagFMzwvoleMAggZ45Mudr2VyU6m5zOj_E7_SlZJVJiEyT4zQ15tiOzPhJl2eoA0cM_6-U-bBCG9tJOsWInK44AhRs66tpg8q4s08dtWKSzYg7u2DYK7qty5Q4U1wdJvBl5v5ernGD2r-XfUBszzaGnfcUDv_lBp_AWKpneGYo5Wp8GhNq69GMeKNCmgbzstSKsn3eURNjn_51X5rygpjg0rqCOv-dYxRatuw0qLlnYcJdr6HcxgGLHv9Agw0CPOSEXXoItz0gUVwGP2CQ2h1BOm9OjsNis-Dwqvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهکارشون برای مدیریت قیمت تتر چی بود؟
نمودار قیمت رو غیرفعال کردن!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2629">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کاربران در چند روز اخیر قطعی، ایران‌اکسس شدن و اختلال مضاعفی رو در اینترنت تلفن‌همراه و ثابت گزارش کردن و میگن آشغال‌نت چندروزه که شدیدا اسهال گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VvYIYjGQru-RXflmqhnnUXY32fTf_V2ULBy8XabkKSSzwvlDzDGRzs-01lmahIwXUZHpxcHN7hdQU-aeW4a7azPQ9zB4LoFt7yddHSbihywV0xoO9h2CPsbhUFly2q_x4D_pMpJhAlZgs1a3SY8j2kpDxbESJBB4NlefKm_1RdseogMdgoYZ_yIujB0pHSOFZh0Oio2UP5RIhXNvQSWFHwb2q8tphathB7iXRZvn3fc9WiLlGchwimgr3NJ1g1i8sAQuqeZ4OdUhhwKh0OP0Yf7qtxuhPgIWBGXa__pEgzXaRtR-08nPQbtuLJLNLx_HuGJNA5oPz5Oy7z68vcoCCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Group-IB، یک بدافزار ویندوزی به اسم HEAVYGRAM شناسایی شده که از تلگرام بعنوان کانال ارتباطی و کنترل (C2) استفاده می‌کنه. این بدافزار از پاییز ۲۰۲۳ برای هدف گرفتن روزنامه‌نگارها، مخالفان و منتقدان جمهوری اسلامی استفاده شده و می‌تونه از راه دور روی سیستم قربانی دستور اجرا کنه، فایل و اطلاعات بدزده و حتی از صفحه‌نمایش اسکرین‌شات بگیره.
نکته جالبش اینه که مهاجم به‌جای سرور C2 معمولی، از بات‌ها، اکانت‌ها و گروه‌های تلگرام برای کنترل بدافزار و خارج کردن اطلاعات استفاده می‌کنه. Group-IB در گزارشش ۲۹ نمونه جدید از این بدافزار و ابزارهای مرتبطش پیدا کرده و با اطمینان متوسط این فعالیت رو به گروه حنظله نسبت داده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2627">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اتفاقات امروز و تصمیمات هوشمندانه‌ای که برای مدیریت اقتصادی کشور گرفته میشه، کله هممون رو خراب کرده احتمالا.
ساتوشی می‌تونست وایت‌پیپر بیت‌کوین رو خیلی کوتاه‌تر بنویسه: دست به دست هم دهیم و دستگاه چاپ پول رو در
ماتحت
بانک‌های مرکزی فرو کنیم.
حالا تقاضا رو سرکوب کن، حساب‌هارو ببند یا سلطان فلان و بیسار رو اعدام کن، این باتلاقیه که خودتون درست کردید، توش دست و پا می‌زنید و ازش خلاصی نیست. این وسط، عمر ما هم رفت سر ایدئولوژی شما.
©
GrizzlyBTCloverr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2626">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YoIUnf6n5SlGXxYX9JbrTvLytOYH7-0dqFIcoHuRXMnl4LjYkqYqTLFveQ3i8Ze4vVswzkWLlWNAyBjaEWPukeLAZI0BsKxXP1vEvAixR12ocEn_c6ezIu5LxJhJaCN1S4RXsCUtcGwigcunmZ1KK_qJOjhbpqX6MMWQYX3FFKtbB1uTuZx4lBAX_L_op-oUhW_unPPY0bleGaGBKXxNoOIPhbOV4BsqGmCJpKg7LvS5R6mMF5uhxURSLiFbjeqO1OncqmvlaTaEA3c91UaRo9gF_ep2I8nVZ7VguCkMFctyz9pQ9E5S-KCTZEqdeZGBIiHl_-oOGNI7UY4cFcfGhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از دیوار چنین پیامکی گرفتین، ازش بی‌تفاوت رد نشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rewxSWKfgaXro4tI43fgYCCG-4RwYEER48l6dpLk4M_y1NVNTc-Ixn0ZyqrPND0ml7F_536af7DoT6x4bmWQ-U-IF2VumcKyQCHrAB0h9Ox3Aoswd1l01DPefD_IG4B3vWh-iV4lWJTb1mij7Zd4VEMB6f45Vszt_JGFykGTz-t4adOJkFbADhIsaB14iBWSb77xgECe47bCEgfSIvjpVC3OLiqG2sse8KU7aSBGLresmNGXWbK3EZJBCGJvFbYslTCRmXzmGvNPUI1eMpoUovBD-Nt0orL7Xaawlwz4XjTp-4dGx6y4b-JlbOYsNzGWXD8ZaLeD97oHKvtVN7cUWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرامه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2623">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مجموعه‌ای در حدود ۷۵۰ هزار رکورد از اطلاعات مرتبط با کاربران صرافی ارز دیجیتال والکس مربوط به سال‌های ۱۳۹۷ تا ۱۴۰۱، در فهرست فروشندگان بانک‌های اطلاعاتی غیرمجاز مشاهده شده.
این داده‌ها شامل اطلاعات هویتی مانند نام، نام خانوادگی، شماره ملی، تاریخ تولد، شماره تلفن، آدرس، ایمیل، اطلاعات مرتبط با احراز هویت و همچنین اطلاعات مالی از جمله شماره کارت بانکی، شماره شبا، اطلاعات صاحب حساب، آدرس و موجودی کیف‌پول‌های رمزارزی و سایر اطلاعات مرتبط با کاربران است.
افشای این اطلاعات می‌تواند زمینه‌ساز فیشینگ هدفمند، کلاهبرداری مالی، مهندسی اجتماعی و سوءاستفاده از اطلاعات هویتی و بانکی کاربران شود. به کاربران توصیه می‌شود در صورت فعال بودن کارت، برای تعویض آن اقدام کنند، نسبت به تماس‌ها، پیام‌ها و لینک‌های مشکوک هوشیار باشند و از ارائه اطلاعات شخصی خود به افراد ناشناس خودداری کنند.
©
leakfarsi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ccwjmBcATps2LCVcdlNeWMZQTVsNWz1QDriOKyTO8QTjg0zRNhHN50MQvCwl5uoCLwJiRHFqKrq51VpiEmsOHeJcEs6A4ltIpGO3StOpHOSRkd8UFHzO1bIXvZatxImOa4rHaJITUxVidRYSHMWH6FOcF4OllPaZcmIvlazO8R4nZu1bz0Z1of-xpw1tAQ03PYBlGwxIDTtnkwauLFJojMq7PJbjn9LdzcuxY8R5TG2fPOJf8P6d63lljO3h1ak6IoG3cdjFVrphBM-e2fXO7T3KWo_9IwwyUIdAokOM99n1skiZ-28PsCNpboHOER8JF7DAa49ScHWFChCjH0M32A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر قطع‌ارتباطات گفته "فراگیری استارلینک میخ آخر را بر تابوت حکمرانی فضای مجازی می‌کوبد".
۸۸ روز اینترنت رو قطع کردین و نگران حکمرانی فضای مجازی هستین؟ بابت ده‌ها هزار خونی که ریخته شد، باید منتظر کوبیدن میخ آخر بر تابوت ج.ا باشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lLbZ5YdEXCoaoeNkWjZTbVSHsfFODn2fXcn44QZ0SavcuNsz8U4GYDpZmCnCpgVKpMtSWIDd9Gn1pWzf6qsfcoIXuzHKW4N8ZHcEkcHeirjRTiW2gsh_GmZ3iDlWeBpnsjGOSW-UTtQDkuJpD0SUOROK9YNES31usmQGScjSDEDHxnCc8ITC9qmQyuxCyI02sYnTjPCr7ILS-3kPCZzV_gVoU6Rnm6qO-nRWXzOr9pUjooMHECudRpG1BDCaFX59Ei4zJNNYS5ulz1x8Kn4wSeqd3HzdJ86A5Wel5IDO8R1XVPsGQ_MqtXhEnmv6PSqfkvgVF4pDsRyV8nbNLKrZeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی با ابلاغ یک بخشنامه‌ی رسمی، ارائه‌ی هرگونه تسهیلات بانکی برای خرید طلا، ارز و انواع رمزارز را بطور کامل ممنوع اعلام کرد.
این بخشنامه بر ممنوعیت مطلق پرداخت تسهیلات، چه بصورت مستقیم و چه غیرمستقیم، تأکید کرده و مقررات یادشده شامل پرداخت وام از طریق شعب بانکی یا بسترهای دیجیتال برای خرید طلا، ارزهای خارجی نظیر دلار، رمزارزها و همچنین فعالیت در سکوهای مبادلاتی مرتبط با دارایی‌های دیجیتال می‌شود. /تسنیم
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QSiNqppYVM06vzL_BIQioy9BdZ799QYB8G1hlKWkBSKu3GDf-0KCbsrqbVYuK5TZmpNusbunI_hj0OE6Lg2x1BixuUPCNsDPW-ya-tZ_0Ae7zjZbKCOkhGYinNFLOJkX98-ghGHs6JdnbhZmlhXA-5kDVuOLQI4EuLEFSt5kPya5DR8lw8_L2QTMprLV5beEji474hjcTaoiB2v_Htz6T-_h8g1udTNwCdLnwyNnNbgrLWGhqsxtNQzZYnI7-knxFr-719F-wIHQEOGEt93weFxYvpjAMHDlblauaIvxJTDc7_fv1JacipyCMPJjOKoVYSDr6bXTWVlN-efIP6NW8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت تتر به تازگی اعلام کرد "به مسدودسازی نزدیک به ۵۵۰ میلیون دلار دارایی مرتبط با بانک مرکزی جمهوری اسلامی و شبکه‌های تحریم‌شده کمک کرده".
الانم با عبور دلار از ۲۵۵ هزار تومان، صرافی‌های رمزارز (با دستور مراجع) معاملات تتر رو از ساعت ۲۱ تا ۹ صبح روز بعد متوقف کردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2619">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">هم خبر تحریم ساخت ایمیل برای ایرانی‌ها توسط گوگل قدیمیه، هم خبر مسدود کردن ۶۰ اکانت مرتبط با صداوسیما توسط گوگل.
فعلاً اون لجنی که توشیم هیچ تغییر جدیدی نکرده
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NvuU7PQ117se-zbb5GelJUeVSfN5U4TqnSwJVimk71UwM5gujnWSMY1QgGbPvl3HAwdG4U1EskUJldOePRf2h2bYh4vBWbH0aQTpuhcD4BO8AKg_bfEKdcbntpGJbeKoClvsRca-9XR2fzfv37N10MEWiRDjva75sYwYckYvhme9wqrfUE3tdhJE75b9PSrJI3nvkFaIipq0N2-HZx3_S3BDOk3m9jx0u6_mN6RrapvIH0tcc3GVdcmR6M5mC0171ZlqIMVpC0EGcsfPPVhPcbaHLW6gv5GlUvJF1W4iqFCSpC6fncWufBqmr93XzVFeIAYXev1ml5EqE4TSouNG1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ sushTun یک کلاینت متن‌باز و رایگان برای هسته ایکس‌ری هست، که از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard پشتیبانی می‌کنه و تمام ترافیک سیستم رو از طریق تانل ایکس‌ری عبور میده.
یکی از بخش‌های کاربردی این‌برنامه که برای ویندوز، لینوکس و مک ارائه شده، مسیریابی هوشمنده؛ تا بتونین مشخص کنین ترافیک ایران، روسیه، چین، تبلیغات و دامنه‌ها یا IPهای دلخواه از تانل عبور نکنن. امکان تنظیم DNS، فرگمنت برای TLS، Multiplexing و چند قابلیت دیگه هم وجود داره. حالت کم‌مصرف هم اجازه میده ترافیک‌های پس‌زمینه سیستم مثل Telemetry و آپدیت‌ها مستقیماً به اینترنت وصل بشن و از پروکسی عبور نکنن.
👉
github.com/soroushdeimi/sushTun/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b98WmZBxBOjVVgMeKIxmmJ4Ij1Sl7KeH_ABz69OQElsMHtJm77bS7CMbnMlzxSU4HosKaiiIkioPjR0fGBlh2ACiIcgiBM_NRkJGI4vGdnVM6Gk3a_HoKNy_c_g4NDDVXZHkEhk3p2w5tRDbjNY9fwUw2WMJMrWzlZnKu8kmVPhlpBGCu3uk53jphQU_6QeVoEHR5h1tfptQRcLnIOGhW4r2KBb6s6z2v98rjrIlRJu-ONhZ57Cj3kV6U9RuyzdB2G5fOv5gp6YWh9tApfLcQFVim-7f4ZXDG_Yn0GR5RURiy7ll5Y5OmG2brx_xdI1KHLztmvAhmj94IFqZ1GFx1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت Satelite یک اپ پروکسی متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که می‌تونه بین هسته‌‌های sing-box، Xray و mihomo سوییچ کنه.
از وارد کردن انواع سابسکریپشن و کانفیگ گرفته، تا Rule-based Routing، پراکسی‌چین، DNS هوشمند، System Proxy و TUN رو پوشش میده و یکی از قابلیت‌های جالبش، حالت Multi-Core هست که اجازه میده چند هسته همزمان کنار هم کار کنن؛ مثلاً سینگ‌باکس هسته اصلی باشه و بعضی پروتکل‌ها رو به ایکس‌ری یا mihomo بسپره.
انتخاب هوشمند نودها، تست تأخیر و IP خروجی، مدیریت DNS و Hosts، تشخیص اتوماتیک پروسه‌ها و اجرای دائمی در System Tray هم از دیگر امکاناتشه.
👉
github.com/zn0wii/satelite-proxy/releases
💡
github.com/zn0wii/satelite-one/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dCIRRe01GozR3fyGWrBS_OOAH356JyEQ2RWWBRR0kMg0_dx0jt233alPh70pzNcMidSZtg5Y-b3uGsGatzJA3DBblVgGZVQP2pCYIMARv9Vp2Gs7Dn7v6pTV8EvXdmdOqsWB1Tlgt_57fO0VhyYoVy8vFhmR-XVd7TqGl8A7DF_1XPzkekaot7q6H2bZGf6M-9aEhziE-fYLSajaDk81NCqjalaJexDodB0rGxHvrodY_w3l93G43AUTse-xmfrz8_dRop40x6JUz2crnsT029kwUMaHOGN4bzPzT8GvkSFETNnM6-IqQLDx4yArRYAedHRwee5EYSR218pAvcIl1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی فقط دسترسی به شبکه‌های اجتماعی را محدود نمی‌کند؛ محتوای حساب‌های شخصی را هم زیر کنترل می‌برد.
شماری از کاربران با انتشار پرچم حکومت نوشته‌اند که درباره فعالیت‌های «غیرمجاز» توجیه شده و تعهد داده‌اند در چارچوب قوانین جمهوری اسلامی فعالیت کنند. پیش‌تر، انتشار لوگوی پلیس فتا در صفحات اینفلوئنسرها و کسب‌وکارها نشانه توقیف یا محدودسازی آن‌ها بود. حالا انتشار این تعهدنامه‌ها، نگرانی از تبدیل حساب‌های شخصی به محل نمایش اطاعت را بیشتر می‌کند؛ جایی که مخاطب نمی‌داند آنچه می‌خواند، انتخاب صاحب حساب است یا حاصل فشار بر او.
©
filterbaan
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">معاون سازمان تنظیم مقررات و ارتباطات رادیویی گفته "حجم‌خوری نداریم و بخشی از ابهامات و برداشت‌های کاربران درباره نحوه محاسبه میزان مصرف ترافیک اینترنت، به وضعیت ثبت اطلاعات محتوای داخلی در سامانه تعرفه ترجیحی مربوط می‌شود".
خلاصه: حجم خوری ندارن، ولی باقی چیزارو قول نمیدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JfahR7E70u43YlkV5RlmJHSQLVrg0XTkWZZa4WqMg9Hv-n1qUgCQb95In9y2MNZ0qriegG7sevOWUnbmEQIKHeZcY0fknuwzwhGgKoHYL96OLmPn8YIIm9c57Pn5j2YVZsH1M5xxh1q9CXMv2cWwZvmt9xk7A-18c43Q2Jxan5eYiw0mHjE7jwZTlywfK_eESxZLnhOqOhf4_DKynZ_NW7hKYboejLpjFH-GnYhUYJ8VTowwptLqaX-Y_74p0X9DTl_A8tujgW7cH1tru3Psi2FXKQyIL_oyN7MDny31NYGDAXUCgt6vB0nLuRHThbvwa8BTwA4LDNR2uW-ZuKFiYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Qrator Radar، شبکه همراه اول با شناسه AS197207 در ساعت ۱۳ روز ۲۹ شهریور، بطور ناگهانی ۱۹۰ پیشوند شبکه رو اعلام کرد که باعث ایجاد ۱۰٬۸۶۵ تداخل مسیریابی با ۱٬۵۲۴ شبکه در ۱۰۰ کشور شد.
این رخداد که بعنوان BGP Hijack ثبت شده، در ۲ مرحله اتفاق افتاد؛ مرحله اول حدود ۸ دقیقه و مرحله دوم حدود ۱۵ دقیقه طول کشید و حداکثر انتشار اون به ۱۰۰ درصد رسید.
وقوع BGP Hijack میتونه باعث قطع دسترسی، انحراف ترافیک، اختلال گسترده و در بعضی شرایط شنود یا دستکاری ارتباطات بشه!
البته در این‌مورد مشخص نیست که بصورت عمدی بوده، یا خطای فنی ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بانک مرکزی نصب «گواهی ریشه داخلی» روی دستگاه مشتریان را یکی از راه‌های ادامه خدمات بانکی مطرح کرده است!
اما مسئله فقط رفع هشدار اینترنت‌بانک نیست؛ اگر این اعتماد در سطح کل دستگاه ایجاد شود، می‌تواند فراتر از سایت بانک اثر بگذارد و در شرایط مشخص، زمینه رهگیری ارتباطات رمزگذاری‌شده را فراهم کند.
مرورگر زمانی گواهی یک سایت را معتبر می‌داند که زنجیره آن به یک مرجع ریشه مورد اعتماد برسد. اگر کاربر یک ریشه داخلی را به سیستم‌عامل اضافه کند، دستگاه ممکن است گواهی‌های دیگری را هم که همان مرجع صادر کرده معتبر بشناسد.
خطر زمانی ایجاد می‌شود که آن مرجع برای یک سایت گواهی جعلی صادر کند و مهاجم نیز بتواند در مسیر ترافیک قرار بگیرد. در چنین شرایطی، مرورگر می‌تواند بدون هشدار معمول به واسطه اعتماد کند و حمله «مرد میانی» امکان رمزگشایی ارتباط را فراهم کند.
نصب گواهی ریشه به‌تنهایی به معنای شنود نیست؛ مسئله اصلی دامنه اختیاری است که به آن مرجع داده می‌شود.
البته راه کم‌خطرتر وجود دارد؛ اپ بانک می‌تواند فقط برای سرویس‌ها و دامنه‌های خودش به یک مرجع داخلی اعتماد کند، بدون تغییر فهرست اعتماد کل دستگاه.
پرسش اصلی طرح بانک مرکزی همین است: برای حل اختلال خدمات بانکی، چرا باید اعتماد یک مرجع تازه احتمالا به ارتباطات خارج از بانک هم گسترش پیدا کند؟
©
raaznet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RT6oIdlB9S3oiK_wHnZQ13s9QAPeqab-2H5tqfp_-VwQDJsi5tRmQTpt0KYOJg-e7SY6PZFYV2Wx9-zQLZVi9U3b-oEDU1jfV49NNdloU2RdeOgjoHzpTBauRzQU38RMxg8CKEZTi7A2TgYOWh23mVEzEMUBabD-sWVXTYdT4kdaJQiuI-UQs9J7dShnhJFFmxSlwDlNnNf1RUadr0bgQSt_i2oMCYNWEGMMk_wBUfNq6ilqLBD5TM-1hNTkybsY7-9iM_M_mQNshkESsqx8PnsMmLOEBjZgAxOF4lcKUdkLLjSaVKW2WDlj3UxNGikuNZnqF2N6AmN7NDFlz0798w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراقب این نوع هک باشید!
یه صفحه جعلی شبیه Cloudflare میگه برای تأیید ربات نبودن، Win + R رو باز کن و Ctrl + V بزن.
چون شبیه تأییدیه‌های معمول کلودفلره، ممکنه طبق عادت انجامش بدید، اما در واقع دارید یه دستور مخرب رو اجرا می‌کنید.
©
milad_joodi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QWk1IBWt2HDpO_4j0Ltm4rhf8N55ej15ccfQmj27hXIep2oISI4gozq7GRgBoVXyIGXlwelSrIfNn_kV0TI7atFokJ-jA9m36uUocywk4nqUBY6af7UYKHaek0X8nb3Co6Th88wQz8ShhHXrwMZ8cTNc51OqoOD82RIeJG7ns8UJyL7RJxyrG2LLsxTkxIagYFW_aRPvgcVtWqZ_xLvAHE_lU6bphnPBd3E8Dr-iXkreL6kqPgf4itXrLF5ZFbykiG9FN1MRN8ZU6VBd-_hetf-SWtd7iGmvdRRdutH1SeG9A8Ge6arO0PEYYQQxJT8eKqAX-JVfBEndSPbNX055YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زپتون یه موتور شبکه‌ی جدید، متن‌باز و بدون وابستگیه که با Zig نوشته شده و برای کار با رابط‌های TUN طراحی شده. ایده‌اش اینه که ترافیکی رو که سیستم‌عامل وارد TUN می‌کنه، مدیریت کنه و اون رو به ارتباط‌های TCP، UDP و ICMP تبدیل کنه؛ بعد هم ترافیک رو مستقیم یا از طریق SOCKS5 در اختیار برنامه‌ی دیگه‌ای قرار بده.
پروژه Zeptun امکاناتی مثل پشتیبانی همزمان از IPv4 و IPv6، NAT، مدیریت DNS، مسیریابی خودکار، فوروارد ICMP و پردازش چندصفی TUN رو داره و برای Linux، Android، Windows، macOS، iOS و FreeBSD ساخته شده. طبق بنچمارکی که روی یک رانر گیت‌هاب گرفته شده، زپتون عملکرد بهتری نسبت به Sing-box، Hev و Tun2socks داشته.
این مدل هسته‌های مستقل، می‌تونه برای پروژه‌هایی که نمیخوان تمام شبکه و TUN خودشون رو به هسته‌هایی مثل سینگ‌باکس وابسته کنن جالب باشه؛ مخصوصاً با توجه به اینکه استفاده و توزیع کدهای پروژه‌های دیگه می‌تونه الزامات لایسنس و کپی‌رایت خودش رو برای توسعه‌دهندگان داشته باشه.
👉
github.com/Noisemux/zeptun
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iZXfKyxs47I2F0UOB71RpGu2q0Cd_LZPykFHmwnY-GpwFqStToiVJ6_88btNHUK7Id6NXxfk9H6du_upvF-ZIbIR60MK56gny0lf0kKcWr2mYnkjzBXMt6tNbCkv0aBnIQBtn7R8rVPzGnIslmzT_LKz4d0VHj6LCb5KFS-aCZjWs8VnF-Hu9QPTjhsN5Xjmd_lIJ9d8AYOahc128FVjWfjNoRtHacXC77IHt3UIcLmmJPhZ_E-0Fbo4DtmmQ-__y9HHsO8vEN4RC_Qv7CnxmplHPmJ1aQ3WN5_Rgww62l2FFuVpWgRff3wbVAHoX8KEkw3FYTNJTa0ZX325Arveyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای، چه گوگولی
😄
فرمودن "مجلس بدلیل پایین بودن کیفیت دسترسی، با افزایش قیمت اینترنت مخالفه و انتظار داریم وزیر ارتباطات از حقوق مردم و افزایش سرعت و کیفیت اینترنت دفاع کنه".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MWmmIW3bezknyqzYM0HUk9SPMf8XUGmRrMGmiEmV-sx6NCWFMRuQyGoXziG484OMSxqqsGKgfVvZgdtcdUzN1p7QYSOB-gUV0_evutyoGwhCXAo5I4xzMb86oSGaLVNCgSuoxzGa9mn8T1qChAiO7RiQG5-CpfbjVGOyg9FLKvV2cntptCgHxk9k19tYookf2s5Ysr2HyMFpRlIlNG3tw93jAf61nphvQfg8iheCZNs2xAn-3fNn7IK4UtNqJleN6MIjaBrcBfrQqj5lFQWcgQSy5GXK43HhN02V5VY-jyqVTSvYhzqltzYP3hayD7hto2ZklFGvBgb1aWef0WOCsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت Google Flow Helper برای اجرا از طریق افزونه مرورگر Tampermonkey ساخته شده و کمک می‌کنه محدودیت‌های دسترسی به Google Flow برای کاربران ایرانی دور زده بشه.
این اسکریپت درخواست‌های داخلی Google Flow رو زیر نظر می‌گیره و وقتی به پاسخ مربوط به تنظیمات و محدودیت‌های سرویس میرسه، یه فلگ مشخص رو پیدا می‌کنه و مقدارش رو از false به true تغییر میده. بعد پاسخ اصلاح‌شده رو به خود رابط Flow تحویل میده؛ در نتیجه فرانت‌اند تصور می‌کنه اون قابلیت برای کاربر فعال شده و محدودیت مربوطه رو اعمال نمی‌کنه.
این ابزار VPN یا فیلترشکن نیست و خودش محدودیت شبکه یا فیلترینگ اینترنت ایران رو دور نمیزنه. آدرس
flow.google.com
باید از اینترنت شما قابل دسترس باشه. این اسکریپت بیشتر برای مرحله بعده؛ یعنی وقتی به Google Flow دسترسی دارید اما خود سرویس بخاطر محدودیت منطقه‌ای یا تنظیمات سمت کلاینت اجازه استفاده از سرویس رو نمیده.
👉
github.com/maanimeisam/Google-Flow-Helper
💡
telegra.ph/Google-Flow-Helper-09-20
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WGUcfB8T3FFhJzWY3qDwYn9afrPWmLZ2SmQhkUsnsWbuddHFd4tlffQJcOTkbQkQZNuFkDeUfv6nW6NBt26uS64Xc1AkwJc--1sT7DO_Ti0tWzEcV0s6_dQY928W2eY-K54LYKGE01kb2L5Mv2Yo_ziG_4O__A7Iv9dL85eYTp7itsL2zMZpdy1f7qA6A8m0bmkSGroRDyMAKdfImhzxKQw4Ac_PSZBXZ9E9YQ--PqFWAlhubXYNbHt2EfhTIRayLqEN4_ZqcRm15YR5vjGV9DVhwKc5LHDxf0aq_i7R7zrP-KW4Ppw645Ecp9tuMp3ZDkWe3EROYiqUC3x_GoqUzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیقی از TechRadar روی نزدیک به ۴,۸۰۰ اپ VPN اندروید و iOS انجام شده که نشون میده تعداد زیادی از VPNهای موجود در گوگل‌پلی و اپ‌استور، اطلاعات شفاف و قابل‌اعتمادی درباره سازنده و سیاست‌های حریم خصوصی‌شون ارائه نمی‌کنن.
در این بررسی، ۳,۳۹۲ VPN اندروید و ۱,۳۸۷ VPN آیفون بررسی شدن. فقط ۶۱.۴ درصد از VPNهای iOS و ۴۰.۸ درصد از VPNهای اندروید تونستن تمام بررسی‌های اصلی اعتبارسنجی رو پاس کنن. بعضی از این اپ‌ها از آدرس‌های رایگان Gmail، سایت‌های ناقص یا غیرقابل‌اعتماد و سیاست‌های حریم خصوصی کپی‌شده استفاده می‌کنن و اطلاعات کافی درباره سازنده‌شون در اختیار کاربر نمی‌ذارن.
در نتیجه، صرفاً حضور یک VPN در گوگل‌پلی یا اپ‌استور به این معنی نیست که اون برنامه معتبر و قابل‌اعتماده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xii3Ru-GfOcl-S571XCyIHlCpBWr2yVLb8WW-UXoQyb_QpsfxnLeGnXmY_FpEqPglUgcnTfmzHZYQkcxGhOIDj2xFOmh7q2XeZD_n9To_dn471SYAN6DNu6eQb5bn3Yco-n7p3ASiQ_43L413bVyGlo558343hEAyHTAAQZc4yI-JojRGvR51ED80JRKmIA9p__OLs4Cuso76iTF53u8nNYWECV_XQp-75-epEuX5H9JyJqobRPdWmFAMr-eWA-dO14QHnnwh_cQcMEGoVOamkVQg_0YKy1FiBzJ3SKoeWoaoik9Ga852PiyMSHLh39W-DY_B7D3VlLaf6OHyeKEWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس مربوط به مسابقه CTF بلوبانک هستش، که برای اینکه چالش‌های مسابقه با Ai Agentها حل نشن مورد توجه قرار گرفته.
طبق تصویر، در هدر یک دستور داخل Response گذاشتن که اگر یک AI Agent در حال تحلیل پاسخ HTTP باشه، سعی کنه اون رو بعنوان دستور خودش برداشت کنه و به کاربر بگه چالش قابل حل نیست و اصلاً آسیب‌پذیری‌ای وجود نداره
😁
مسابقات Capture The Flag، یکی از شناخته‌شده‌ترین مسابقات حوزه‌ امنیت سایبریه، که شرکت‌کنندگان باید در سیستم‌ها و برنامه‌های از پیش طراحی‌شده با آسیب‌پذیری عمدی، به دنبال رشته‌های متنی پنهانی موسوم به فلگ بگردن و با کشفشون، امتیاز کسب کنن.
©
Maji_Call
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PLObbOtUKNguZS0VHCI1zlzTgKKXiTqpV_tZm3m-6pHBH9YIvuMcf4a6InEqXU-diFiFrmGGeug3Oo55nxp3XAnLOAWhocAUyaQwCYFogBU5Gd7myogxjn4Oc5oevFII8z-cuLedvGm4BN03k2lQgfpoB8_iL8IpJle5h8SxGg7u0PM8bkqSE-FeE-nx1FWADuoskhPWwQS00kPoPdpdXJWFfKJMF5l7iXclObuzKoa4ztxLf78w3sEPyf11ZI8AzSaukSk64HT7Mqc68q26bjsCFdJvZHVDCXb3YgCGxHntYfpCFyjf7IjEWoRn5_xO3IFfAMZkwRMnxTgQwUevwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از ویژگی‌های مهم Tor VPN Beta، ایزوله‌سازی برنامه‌هاست و هر اپلیکیشن IP خروجی مجزایی دریافت می‌کند، تا امکان ردیابی رفتار کاربر بین برنامه‌های مختلف سلب شود.
👉
play.google.com/store/apps/details?id=org.torproject.vpn
©
PasKoocheh
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mVwqgx10dLiKHwhm2s5xuBrfVCP6aOFsEppCE-OAwU1Di1Cz7P573tcFA9-hv9fwQSJu2ZDkoSZfMZaODHK5FzvIGBtz2rg2EDX6MXHvhDTAJgMtrPebgDUhBoEnMGa6eVtUCJX1lGqj0gexOgATcrS2etOokYfYT5RWS71ju1TeZmSdPhUJc03nCKXG51SI9tAHF7rvFxZgkd69SRdeL-VBd6yJ5glIs93BBEtpATUrt0Qy0OcqklO8njUEznlM7i2Y0gqbh0sAB-RrGVf6SaKYilkR5-643WFweWioC92xloeWh9e1vMxUh3eG__RyybJbOqhHBPsAvATs1tIVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپی میکنید حداقل اسمش رو تغییر بدید :)
تصویر مربوط به نسخه وب ایتا هست.
©
Ralireza11
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ایران در جدیدترین گزارش اسپیدتست نه در رتبه‌بندی اینترنت موبایل و نه اینترنت ثابت حضور ندارد.
تا ماه گذشته، ایران فقط از رتبه‌بندی اینترنت موبایل حذف شده بود و در بخش اینترنت ثابت با رتبه ۱۴۰ جهان قرار داشت؛ اما حالا در گزارش جدید، رتبه ایران در هر دو بخش حذف شده است.
©
itiransite
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BC9oZ_Tk3YxtJGl0NfDN3rlPX3IkDRjevxgrJvDGYAFcTzl6rzwhkyAPvTwOItkzRoMcKIHeB67JaQQrXfWHq91reX0PFsgSbvef0iBq0sB_QTTnh79tR1ZkI66dkFk1VfWvVeUR2b3XNLR0oh8kPuBDrYJRT5yc8-c2-bSJo-1XZW5xvmtfX3Pc_xifrjoj9GOoetWSmC-f20_y6fsepf-GMRX4SKBREHXK95We9BM6yoYbtnOssKEq7KyRBNcEbc184liD6UT-H9wSTNt2rw4LKIBKOVENgbkaxyC3otPQ3VcPCigHWgaNo1LcQVUAHmzEaI4nzGDJLCCGuY2LmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LBZlLnNfHhoJHIJTo6YBs_aNlhyaslaWf9HVLtrNuzp047KplK0bc-5rAg63RICCFSlS4lwY0p8P-558iN5n-ZwPUS-zbPoQjrFVqDjKEKnSAu02tJjmo8HyThF9KhNVr37BiVK5ALE9fYRox_WabHgymD-yvfutxdlJWzkVsF0krwodifgSkuCMppvwJCnxHbSRqldSxpV7iz9XaeXXKFUiMgVZwyamq5Ftdo75zSRaIzay_lGL32AP1y_4Q6x1fvh4AMV4rWmCvd0L9Tsabe2tKOL4uDxKI7UdbJoSPYsXDXcC_0KenfA_2IoivEFZVQAlJFM7YwebIIEdHBwNKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی خبرها
دیدم
که ساکنان روستایی در منطقه فتح‌پور هند، در اعتراض به کیفیت پایین و ناپایدار اینترنت و خدمات تماس تلفنی در منطقه، یکی از کارکنان شرکت مخابراتی رو به یک دکل 5G بستن.
امیدوارم برای وزارت قطع‌ارتباطات پندآموز باشه!
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gWQQPodvbDhXdrmp2mgERo3jiV3h_wVqZB0vBmucmvFtpOJDymPW1EQC5UTE39juol7ub_FJctwGgragI3f20Mdos0N55ulrzUSN9l68B0EClX7-GehXhIPQqJDqngG_rxqgiz8Tk2OgP8MCalFUvEPJ2GGM_ZEiCkWPWV-_6vyHSL07SdVBaiPXCdKJC9LTnic8lFI5nVK2mqUpmVw9r1vYxFnLkB_1jWZPomm2thma9XWz090c2tN6fIFhWOXDkdqkxPNU0ZLyvZfxU__EjSbUEJ6SXO7MOt0bNyNNAqaPmGJC6SWJWXj3EZaqvUBdgROWqII_OGEDx_naayv0AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m80k6IA-9yYbUn_4v7l_aRH7gAOdmaRiLZKjKNUreFYLfG_1Y_m2SGkfKuydvv12ABH5_b38JzqCuzS5MhFLgjC6_5bN9kO1RBW_1ZFO8jxJg6AP7HrAQb2vhP5Y8B-LiAth9Zt6yL1kodAFRKgQZcKGvYF6jOzGr4dUb1YuKEf1L7oXs_SzkVBjjuP_Y7DDKJ9mUQNoB6m4AYqFh0j24n7BszCyyYkx60mqknIoSI53jENHaDcrBEF7oMC6ZxU5WuDPTqU44RjQu7LMsIozsdCvrl2b2WU1m4L4RXgc1BTAIgh7kMBHb2rWh1gtdBFXBTiZs9IJo-Gg6gLF99WfQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether منتشر شده و این بار Tor هم بهش اضافه کردن. حالا می‌تونین از تور بصورت اتصال مستقیم، اتصال Tor از طریق وارپ و حالت معکوس استفاده کنین. پل‌های Tor هم بصورت خودکار از BridgeDB گرفته میشن و Aether می‌تونه پل‌هایی مثل Snowflake و WebTunnel رو امتحان کنه.
یه قابلیت جالب دیگه MASQUE-in-MASQUE هست، که در واقع دو لایه‌ی مسک رو پشت سرهم برقرار می‌کنه. این حالت باعث میشه برای خروجی، رنج آی‌پی متفاوتی نسبت به یک اتصال MASQUE معمولی داشته باشین و توی این حالت دیگه آیپی ایران رو از کلودفلر نمی‌گیرین و رفتار اتصال تا حدی شبیه متد Gool میشه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZR7BoNuaGOIvOYPsge6aVW-53jDbC-LNSoQfYnVJudnDm9sZIn33sLvsjpN-jBcugUnPbc1owrzJlS7XKnlcTaogeWbxf02dobLw8dRw0yij4qVDSQuickFiMSd1jym0BQuoe_VyUBHNvQv5-AS0J8kfvGN_Ff1svDyF8ibS-dI99ADm97j6Oetgfmqkbp7YVgFxD5hek3Odz_ESpU9Djvhc0YQocG2NafqiALVJxhQBTcqTdrGo0NEhJT7nBDbBfWf8r-m22F2KA5iZjderYWqZYpmT-TVbBEvV5TgbBIKKx5NXIs09bGUxHJXHa2UPTJdrLxkiiNUXe6GTo_AS_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک، شرکت سازنده Claude، در گزارش تازه‌ای درباره سوءاستفاده از مدل‌های هوش مصنوعی، چندین عملیات مرتبط با ایران را بررسی کرده است. در این گزارش، ۴ عملیات مستقیماً به جمهوری اسلامی نسبت داده شده و مواردی هم به سازمان مجاهدین خلق و یک عملیات فیشینگ علیه کاربران ایرانی مربوط بوده است.
در یکی از موارد، یک مجموعه مرتبط با جمهوری اسلامی طی یک سال اطلاعات ۶٬۳۸۸ ایرانی را جمع‌آوری و پروفایل کرده و برای این کار ۱۵۵٬۲۱۶ توییت را تحلیل کرده است. در عملیاتی دیگر، بیش از ۵۰۰ کانال برای جمع‌آوری اطلاعات افراد داخل ایران بررسی و ۵۱٬۹۴۴ پیام برای ساخت پروفایل‌های روان‌شناختی تحلیل شده است.
استفاده از کلاود به تولید محتوای تبلیغاتی محدود نبوده و از آن برای جعل هویت، پروفایل‌سازی، توسعه ابزارهای نظارتی و حتی ساخت بدافزار و ابزارهای فیشینگ استفاده شده است.
©
RaazNet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hZSysgGYj6uSjV3PJ3Hz7mt-I728EYTOZK8Ziw56eGMxd03WCoPYx7NCBy8g6e_rcJ_uXO9bGgSkQInB7LZpUdMzFdi6LXm4hsw3xALNaev6Cwe3na_bX6VBHfHDONd1oD4rbKB1iWte-cNi8s5oGagqoLV6MXCEqagYg4GOpRC8ZjpAMV9pj4n7fHuoZGLRfdqrDPTWERF0-vtwFSuEdFLuHK1a8bwmp2l0WWP5wMxyRWwQnoyM8P0tgTYqlr_Co8bllBixaCM6X2aFwOUXdI6Mkl7-7jY0O3Y4YspLal8lXAqJJ_e78CsDn2T4o0YGTUAiEVfROnr4Qu8GJU7Hqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون علمی رئیس‌جمهور گفته "۸۳ درصد رتبه‌های برتر کنکور در ایران مانده‌اند. این موضوع نشان می‌دهد بخش قابل توجهی از استعدادهای برتر کشور در داخل فعالیت می‌کنند".
البته نگفته ۸۸ روز اینترنت رو قطع کردیم، هزاران نفر رو در خیابون کشتیم و خیلی از همون‌هایی که کشته یا سرکوب شدن، از استعدادهای برتر همین کشور بودن.
نگفته راه خروج از کشور رو برای خیلی‌ها سخت‌تر و پرهزینه‌تر کردیم، عوارض خروج گذاشتیم، ارزش ریال رو در برابر دلار به پایین‌ترین سطح ممکن رسوندیم و انقدر محدودیت‌های مختلف ایجاد کردیم که بخش قابل توجهی از آدم‌ها اصلاً امکان رفتن پیدا نکنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sKV-WFfFPU9Zo9KHO24P0Fnp7AJrdXtCWq48ubTh0xWFl8Wj135NMkfM6KHuSfsApuvr2TAxdKN4govuQr7DQoN4WW5Wg-NG7DpKvE-cPwcm4WBuhD40Cd9C8QibgaKr1jHkqatFPwNUhIPoB9qdi8xhLjGiexFvXz0DG2KAHZOj7t2odFEjmway3ZlGz2X68qlAgs5ENTgpg8yofvFp3qx6akrVQoG8e-A-cNFWYBDAqw3OouDCfwcOinbuocZtsvvNnRG6BXZsZOhXpnZAMfbTOgnq2YKCfqsMIfjcdKQT2EuOlIh5EL43F2tI5EXpq5CJASmgVzyUzbcTzZV4TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتابیسی که ادعا میشه مربوط به کاربران فیلترشکن JumpJump هست، توی یکی از فروم‌های دارک‌وب منتشر شده. منتشرکننده با شناسه leakhunter ادعا کرده این مجموعه فقط شامل اطلاعات معمول کاربران نیست و اطلاعات شخصی و نسبتاً حساسی مثل اطلاعات پرداخت، اطلاعات کارت‌های بانکی، تراکنش‌ها، موجودی، لاگ فعالیت کاربران و اطلاعات دستگاه‌ها رو هم شامل میشه.
البته فعلاً نمی‌شه صرفاً بر اساس ادعای منتشرکننده با اطمینان گفت تمام این اطلاعات واقعاً متعلق به کاربران JumpJump بوده یا اینکه کل دیتابیس ادعاشده صحت داره، اما درصورت صحت‌سنجی، همین اطلاعات نشون میده جامپ‌جامپ ظاهراً اطلاعات شخصی و جزئیات مختلفی از کاربرانش رو نگهداری می‌کرده، که این نشت می‌تونه برای کاربران دردسرساز بشه.
اسم JumpJump قبلاً چندین بار در گزارش‌ها بعنوان یک اپ ناامن و مشکوک مطرح شده بود. بنابراین اگر از این فیلترشکن استفاده می‌کنید یا قبلاً استفاده کردید، بهتره موضوع رو جدی بگیرید و حواستون به امنیت اطلاعات خودتون و افرادی که باهاشون در ارتباطین باشه.
©
hamedvpns
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fYrLlnUN67iAgkn9nxcv-LIQ-jZSZoWNcpT5ILtSs92_oHGNMRfNGU1EoeKsQ2Gqrt9AHAbcxkCaP0Zgerfdcs602eWuNvAiidlH7OimjDeykUZeBVVb54T-oqx6Dpt_s4wXGpkRc6XcQsy4pq8PksbfCyf0GhsU8VfM1PLtMAJ6H1HX-oNfm-iLPSJSRVfV80-QR--4aad8_M-Lr4VVKhAa63_FsQSDgn7aNy7ustHlMNYN52jo2bszq43betTyorUgLYQI3sFSIDA5sac6LOuMwNXL2NXt8MyfbZx_qBCYL7PA7uLynuuwflgp3M8T-VNYrCJLRyVhTw-fMzmpMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lxYc_4cWOkSuYNTFRtLQToVfOev-OnoX3iyVM89ZMMrm1PpGhiqEHP6lL-5gT4x3njjsTZ2BOv6gB5WbzjzIZiGOykJkTrj0TQL9VmVRGNwShVnsY2hkccC1DsXf4AjjnE_8k2P2eHfUV1nG1O6nuMB2lfof9XGMs4S_l245ATUeNTv5l01v6jnNc4eLACXJ_9O8nThMp1WQG7hHMzVoy_71SZ3Ge3GgkGGT1B7LcAfWEX7ECJiVkrbqc07ObKDcJ6XnPQdhEXRNfTe4i1wZtTWcyJZJuhzYNZBCYXNkRtRk9cgnac88xEUV80E8J6UdpZSVTWtOtsDYhCRDIEKsAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از مدت‌ها وقفه، بالاخره فیلترشکن Oblivion به مسیر توسعه برگشت.
در این نسخه که برای اندروید منتشر شده، هسته برنامه از وارپ‌پلاس به Aether سوییچ کرده، تا امکان اتصال و دورزدن فیلترینگ از طریق متدهای وارپ، گول، مسک و سایفون فراهم بشه.
👉
play.google.com/store/apps/details?id=org.bepass.oblivion
💡
github.com/bepass-org/oblivion/releases/latest
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VUsgoTg5dbMd5yiDUyxGIs7l-xmf2_N9imUEAl-3koREdlJYZY9sZ16DL697E0WPGuJOlIRk2N_XaMRMoMw6IxCjjGoQggvwww3pavaI_RWufN5f5jZEQzresNHEx8IL8atZWSZ34xhlDOKNLD_0D-GA9UgpAyDvv9bxipMH2EdNGW1M-4w8AtbqfsVkL-surxX4egBRI0l4PMLfjN4Tc294Iz5T8RpqKZjJoAA1L2ToQQyU-q2xkZ3cp-62t41UBe8d7vabQnRLQcGT87MaZO1Rqp3dkuIuidDVf0Q_XufNXH6vcwllU42ucwJALgAIlN47PA_7JbWkrOMi2-MZJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل یک آسیب‌پذیری روز صفر با شناسه CVE-2026-85046 را در موتور V8 کروم تأیید کرده و هشدار داده که هکرها از آن در حملات واقعی سوءاستفاده می‌کنند.
این نقص ممکن است با هدایت کاربر به یک صفحه آلوده فعال شود و مهاجمان را قادر به اجرای کد مخرب، سرقت اطلاعات یا از کار انداختن مرورگر کند.
لازم است پس از به‌روزرسانی، مرورگر را حتماً دوباره راه‌اندازی کنید.
/فیلتربان
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VKbzRQYqs7q0P4pqobzKXxLzGOGsXyWC-kN8i-uAce9MFBCmFUG46DyFLEjvkGDxueFDWhqqk8RaLH0BwN81NVGF5w_P2n0LEtrUP8lXSaEFFUuBFqb8IatFkof2qkB7ep-QdT9gyqQcOzNo-SViw3kPgqv08hOLCqcGi94qTP01AfU-_Vpy9f5sDiVnWalqdjmiQ4TcETArZ5YvUifV6BeW5XpB19JY3Twxx6ocR0bcmY7gQAn5pGt7TvkZkN5Q43pD8TLQ2L3CqrFqFCgADT39RUTIFAurFp2Do9u96VhzO62-AUY7PMNq05QhUR6OCinxyBISNayoLzdC7x1Vcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیفیکس اعلام کرده که این فیلترشکن توسط تیم امنیت
پس‌کوچه
مورد ممیزی امنیتی قرار گرفته و تیم توسعه درحال بررسی نتایج و کار روی چندین بروزرسانی کوچک و بزرگه، تا در کنار حفظ عملکرد و تجربه کاربری، کیفیت و امنیت برنامه رو بیشتر بهبود بده.
این تیم گفته ممیزی‌های مستقل و همکاری بین تیم‌های امنیت و توسعه، یکی از بهترین راه‌ها برای ساختن نرم‌افزارهای امن‌تر و قابل‌اعتمادتره. هدف این فرآیند، شناسایی و برطرف کردن مشکلات پیش از سوءاستفاده احتمالیه و انتشار خبر این ممیزی هم بخشی از شفافیتی محسوب میشه که به‌گفته دیفیکس، کاربرانش در چین، روسیه، ایران و ... که با فیلترینگ دست‌وپنجه نرم می‌کنن، باید ازش مطلع باشن.
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PXg8MqjfzaZ-jL0eT5twhkxlVMPLLnyqM852-4EDblPTt0AFTEPY_B1geI12wdJJNs801noI06xCPXY6o_gHpAKTvKl56pC14I6GCVThKdBLBVSF7UT_UP0wKTdJNy3-D_6tlNBq6TCf28VfELiPrXUrhjkYfV4L2AzrzbH9FDhaaqcQ3lh9qnhveHE6JbUuQWXRg8IHJHNy5Wjyf_fmmfi2ALYGFowbYx8IY1tCea6qmDcy41d8WFwzAB6VnfONpnvBRZHBXhSOJg6kSUMSQ3JVB-YYE2hq0I8GvFKkpWwxW62I1LlSfiO8zSjUExBH9qAPBECULN910GjxwFRbpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qRTnvPAKBkTxKwn3X6Gr0dcw6gxGlvE5f_YznP3lnufi-qMAzpxOFPIZfXHCwqxwDSxF8RcquhrRSv7ZvJgKrOJu2TN4Xt8BcTqwMg7Sr4Qfaoa-8baen3W0y7YhiVikF5JhcODSJt58SqYhXoRt5yttedtrNStFeoIGg_C2kjexW3XYFlP9y4ZcuXvipDAcTlaIfks73Cq4Tcc4xFjR431lo7pYMOt6FTTNSKkCexg9u-bYzPCenlEG3i9ycsUgI6bq8woHsNk3qU7GAeHNxfl_1jM_dhGDwNmbgK9Rde5T30aW--TyTdoRWryLy4E4PKU_GnF1JgM7IjiW1_w49Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سم جدید
😃
☠️
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p7sbAR9tlp6psBu_P-QmSltrGyHudlxc-FQxT0FRv7f0Ct9LrCzE9pE7CQGX8Xy45rP7rKTVc8odbjRAaiOaUg_izlwp_ZAky0Up_umusnj_LkHB1n0jBaRfZHtzKV03DuH3yUHj4pBUP1fzzNdnbV9d-T1pIFmtNOempu51eimWlV9lwNRUVHMxkBI-so524dwM5PEyMS6BpFVBZVzAv8iHQBaRFjUqJ_g2wzKTlbxd_9uCxCCd8uMBRpWZrETFRIa-KOR-bqAurnn8vQN68s3kORybxQXwwTeheJ6dIspYRUzvoFs5Ds8U5_3OgGlswKqLboEjFurASJsnowzAyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات معتقده "قیمت
#ملانت
به اندازه سایر کالاها گرون نشده" و احتمالا باید بیشتر از این دستشون رو توی جیب ملت فرو کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dEKc5hDO5G9v8_9IxYfAkaQi_shqB4pHHSZ9Paeed_nJVZnbrY6IH4a1iB_Ube26KJxq1oF12XP8VlkoR9DewDGIg7pJGNZjbFhyjMvqBsgTKYRlZjzwWDqakoFAkiHrPNZcTVh0kP7ACPnJ3ih0JS8G5B6HmmuUEwlwCLAhPrBp8ggl9Mx1MFMQElgTUvzmvtWbvv4MR1xkuef__ZXoepJLZpJX_Wkk_gD0F6V9zResOXxlGPYVq9_NBAb2IYAKxhuk3kX83JcD0AM-WD59-6cPMxOolqkaJfbrqr9Hop8X05fIRtWe1UYHe1fwtWwhdHh4uQSXY4bv-eQqupcizA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واحد امنیت تیم پس‌کوچه در ماه‌های اخیر حرکت حمایتی قشنگی‌رو شروع کرده و اپ‌های VPN متن‌باز (که در ایران مورد استقبال قرار گرفتن) رو تحت ممیزی امنیتی قرار میده.
طبق آماری که دارم گزارش این ممیزی‌ها تا الان بصورت محرمانه برای ۷ فرد یا تیم توسعه فرستاده شده. اکثر این اپ‌ها درحال کار روی بروزرسانی‌های جدیدشون هستن و بیشتر از نصفشون آپدیت‌های کوچک و بزرگ داشتن.
این‌قضیه تقریبا برای توسعه‌دهنده‌ها و جامعه‌ی هدف برد-برد هست. اون فیلترشکن‌هایی هم که نسبت به مشکلات گزارش‌شده بی‌اعتنا باشن، به مرور از چرخه اطلاع‌رسانی و توصیه به افراد کنار گذاشته میشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NHakiXxCQUSAGVCi6SSXzWMNmkXcpkszceZ_aORA-K-OoyUV32LjAMOsyD4jBw_w8gKgKg0z0yUbCcHhuMh_FrM9xc0LA_0Re3NR3z0f7ML5u1tGbSQolOQ3tfu5j7y4iqEhZ6XgS1cxSLoafsH9lUNO6IrqVjt3y4MwISuGKyUCx5w3DPw2OYqknmkfR4cqoHeMVNA_FiJAASSAJ1_Ponm70LB2pzo87BbOXkJ6b-80MmQyW0wWNWIwjuW7D-MEQRDsVMdr2-iraL_Wg7Y7Gje9Rv74BLwPRyvAV6_sJ1BWfNQUbZKFQ4rLjxuoAPLq8TJkG4ckmn6rqnaUb2AtCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c2I8rZ_o3cExWTNUFf9X-B3EJT3umwRDB1qI0n0pnbQi65HQX9C6oFakIU9eScsSHvvoolNJJuj1OTUVjngDMUUMU86ox9XkVKl_RpUyAvipzuFsA77XHGm9PrNwjIDf8WKUXiyoI0Wtd_dnTeq2pnI8ho_On1nCEXatsc9MiwNXuIUs2E43jxsmDjDEUBHfXLxL4rN_FlpM5mCokwimDARYOQmbl-VskUbrcZ52KrylG-tyOoMFngHCLjF41V2gapUtDuNWXtjryMn11X0bsBING5fMPicv0FzpfcYMBoKMKY6aG008i4VkpVQzHcQKvjggxC7uQQ7m181UjfasJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZuDOVlH2uoVnctZcG85iCNsUMOjc4WUikQ8w3hcah2l2RaF1AVaj_Uggb4FPVbKy2F8o6Akoqhtw4RhnoTff2CniaZQjzyMgTnRe3qVCjJiOgw-S18PNhTu_eXfaOP9L5LLzlQRloqpub8yXFQTXOV6h0I8W52tP93fuRzHWoPmM3wuZmKVHo0-0BsGyVB6jShIHJRzSV_l7dp0dM3cEywNWAPq0EYm72QzwgjtQe6IfXHY0DIYa-AgpocXrhPdVwjaW7Vzxoxccy4u-sVEIJa-okgs5YlN90zoWqdZEZwBBzwvLCGyYuvhkQqCCkb9q76zJVByyQIe5JrqFmkw-UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسپین یه ابزار رایگان و متن‌باز برای ویندوز، مک، لینوکس و رزبری‌پای هست، که دستگاهتون رو به یک هات‌اسپات مجهز به VPN تبدیل می‌کنه تا بتونین فیلترشکن رو با همه دستگاه‌های خونه به اشتراک بذارین.
کافیه لینک VLESS، VMess، Trojan، Shadowsocks یا Hysteria2 خودتون رو وارد کنید، تا ترافیک دستگاه‌هایی که به Wifi کاسپین وصل میشن، از تانل Xray رد بشه؛ بدون اینکه لازم باشه روی تک‌تک دستگاه‌ها VPN یا پروکسی نصب کنین. درضمن اگه تانل قطع بشه، کاسپین دسترسی اینترنت دستگاه‌های متصل رو قطع می‌کنه.
👉
github.com/Iman/caspian/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ibX9yC_AXbZ9vovF2hjksU1irE-98_PbaE9HFMQ-u5rePlrZvNyxQG_vbSqQl9pbGzo340P_wfQi4c8ih5bSxatFO9gECXRC1G0_gh9n_RRpODo-iXvuTXLlpTtji9hjMZN0NIUyQPAbI7h6r3USD5Tc4dUm_xoavjIfeVLBSZfCfeEbtJxVjnH352bG_UMcsBRZwOEAMviG6A1TGB6dvQp8r32Q9_thh0pmWS09ssseOr9YjvD6h9pPFj39n2Z-6havkXmpWGHnTLwXO0-J5glEPY50eleBD7tm6WZR8_pcq0J7ap_fMzFV03TmVzebBpnzTIMZEqqVTXNiJ1P04Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Misga یک پیامک‌خوان متن‌باز و رایگان برای اندروید هست، که به شما اجازه میده پیامک‌های اسپم، تبلیغاتی و کلاهبرداری رو بصورت دلخواه فیلتر و مدیریت کنین.
این برنامه چند فیلتر داخلی برای اسپم‌ها و کلاهبرداری‌های رایج داره که می‌تونید نگهشون دارید، تغییر بدید یا کلاً حذف کنید و فیلترهای خودتون رو از صفر بسازید. با Filter Studio هم می‌تونید با Regex یا متن ساده، قانون‌های جدید تعریف کنین و حتی از هوش مصنوعی برای ساخت الگوی فیلتر کمک بگیرین.
👉
github.com/mirarr-app/Misga/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kOWd1rRabyzQbDJB5sRqX0l9YAlOoaLoyPs8x8ZxNWwHuHCFOb3ar3iaJ20nt9D264FHbjGfrFEZubJcnuvpv2aoP_A0gCQTvzxdbksFhnPkxYcUBBxx5jvqXI5-UZYqO1hHWNuCy1pW8O6LKjWqOnajf8p7GZau3Rf85GDm-zIBHX2dKirsZ21ODwgOHGWmC5IwEX5TynIcbb9b6DcipzWvoC3gQJgoah4gmNHEhTqRPd6yuIoLI5zLUf8e9jtndP5cVQT61Jeht_3YF2TizSB_d-w-lxT83D95NTkWsK2ly-aCifDFWrnB_IBsu6E9_9Dw8KQ0-Y5sMnpEkEGlEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند آسیب‌پذیری بحرانی در RouterOS پیدا شده که بعضی از اونها در قالب زنجیره‌ای به اسم MikroTrick در حملات واقعی هم مورد سوءاستفاده قرار گرفتن و می‌تونن در شرایطی دسترسی کامل به روتر بدن.
از طرفی Shadowserver در اسکن اخیرش بیش از ۱۲۲ هزار MikroTik با SSH باز روی اینترنت پیدا کرده که حدود ۳ هزار موردش مربوط به ایرانه. این عدد لزوماً به معنی آسیب‌پذیر بودن همه این دستگاه‌ها نیست، ولی نشون میده تعداد قابل‌توجهی از روترها مستقیماً از اینترنت قابل دسترسیه.
اگه MikroTik دارید، حتماً RouterOS رو هرچه سریع‌تر آپدیت کنید و بعدش لاگ‌ها، یوزرها، Scriptها و سرویس‌های ناشناس رو بررسی کنین. SSH و WebFig هم بهتره مستقیماً روی اینترنت باز نباشن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nOSIlTUtD31ixUZ2I7VYt8HRevN3bvNeb5O76TvQrC4LY_jCciLja8iVGwxyQm8XjC5ljpAIleU8vLyTHrfA-ZycaO25mN3e_IusvpRslWa12Jn5jFvrwVv-m9SJUchSwlEZouS3AX9_zDivNij5ijxX9wSSGcKKhgaEWijk3zRxZUMzz12TIIMfSkNYWKPswRz3t7_P86nXrMWma6lhG4vMj3k0kbykUw0gSNiMoEDybCxdZHEt4n-NXJibkoCBU-OQguknYhOUdfMloFXYNhPW9xiqqVjUfWZ5QnybvXgiHvWId2NY738nbczSmtF0ad66VYOXwo6qiMA4VhKxMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه یکی از زیردامنه‌های gov[.]ir به افراد دارای مدرک فوق‌دیپلم یا پایین‌تر اجازه ورود نمیده و حتما باید لیسانس داشته باشین
😁
©
SePeHr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ucm5-vJebRSYxr9pzjfb1m-Y8WAuve_Cy1fpHGeI-UlLBTRv3Fw-e3UUYBOLHL_zmcGMgYYRTQIPcJicd2G-UjM6eZ02LtWh3zoNyz74g3a6Bowrq0gKqJDzAQPRtsqblBXNcAyx_GGegqEPBeLH8vTai8Lv-oW3H75cA3BSDmwM3itPT_CX453euIeP87A1tOjIVCEx2Ad7Ec30fOPZJG7Il2OEyEoz9TwnG-V7V7zBBuR0eA38XLDUxX2IIMq9VuFKfWM3ZUJPXdSGQlBn31XBdB1f0LGh1Gg6XUA0sxNS-nx7IBbprKBp2kjaVYWJqkKuPh8e7Xmbx-pssIMe-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن متن‌باز و رایگان دیفیکس اطلاع‌رسانی کرده که امکان تغییر زبان رو در گزینه Diagnostics & Experiments مربوط به بخش "ترجیحات" این‌برنامه قرار داده و حالا کاربرانی که به چینی، روسی و فارسی صحبت می‌کنن، می‌تونن DefyxVPN رو به زبان مورد نظرشون تغییر بدن.
البته این‌بروزرسانی بصورت آزمایشی از طریق گیت‌هاب در دسترسه و بزودی از طریق استور هم در دسترس قرار می‌گیره.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ایسنا خبر داده که
#قوه_عاقله
بخشنامه مربوط به "ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها" رو لغو کرد.
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حکومت در حال تهیه لیست IP کاربران و در قدم اول مشتریان دیتاسنترها است.
در این طرح شماره موبایل + شماره ملی + آیپی به هم وصل می‌شوند و بدون ثبت آیپی در سامانه شاهکار، دسترسی به اینترنت ممکن نیست!
نقض حریم خصوصی کاربران و حق ناشناس ماندن در اینترنت با قدرت در حال اجراست.
©
souzangar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iFdRV0_W0cVBInRMjuz4Q1aQ7pE5sXZEOJVMMmF4RzN1_pYRitzVdyKTK4b4JW1OMlYdABvgHJ5hJ1yvf8R9fpB4Smx773k8b0PvZdBZDVv467t0LXnZq0EE0v0CIqWUaE0-zT2hXyGPIc5ocZGV8R7nicu92pUeR5SiuwcTD8m59POfZZz2jmN0H40h4E6CiRbdPdm7LiSXAvOgeYVa_dezhrOOi6is8Gi1lt0Bf_W5mIH962mC7fALfwsMQaP37g3wA0ZCMHN1XJjy_siiIP2O32nwziUr7-Ag1Swk2w3AAMQz2x7FRD9020_NSz1tW5QXp8JBGLM9fQS_Mo0Ohg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether با تمرکز روی بهبود سرعت و عملکرد منتشر شده و مهمترین تغییر، فیکس شدن مشکل سرعت MASQUE روی HTTP/2 هست، که حالا با اصلاح پنجره Flow Control، مسیر ارسال، فریم‌بندی پکت‌ها و MTU داخلی، باید در شرایط مختلف عملکرد بهتری داشته باشه.
از طرف دیگه، محدودیتی که بخاطر بافر دریافت TCP در Netstack روی همه ترنسپورت‌ها وجود داشت برطرف شده و این بافر حالا بزرگتره. ضمن اینکه می‌تونین مقدار بافر دریافت و ارسال رو بصورت دستی تنظیم کنین. البته برای WARP-in-WARP چندین دستور جدید هم اضافه شده، که اجازه میده اندپوینت‌های مختلف رو بصورت دستی مشخص کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/giSuUDIZko8ObtLgQKlvO4W0XJNmB4ztXbkDfMfyBurWWnFVYv4O8THaPvVJWFgCcOgTJNLSjrWTqnL9Or38k9Lkx6bFfO_XmzFZi1nSGyg800OjZ4AwHJd_zRUxVxPqxvjp5TjWXpXGGGta07f3VnygUZ2tBflzpMViAiSkQfzXlP7cdN_Fd1RHt9yez56EOhI5LnOOcmJX_1mSZpfyf7kyQfS0CEELmNRQnoy4uk4-Van7DVNHbtBu994iyLSKh03qwBPO1VE2xmtwxbfJWhgm2ir2X99CXBqVagnTkh5l8OmQ_33inw4wA0HLph8MHwwkwCV_9EkYWukQAufMFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rp7yLFTdG4HRR7K0vBfJjNa_TaV2qcV2Q_HUdTTdNV7PZnjpV9457FOcLFY7rCZBQfADBhNksEeLZDU_WciXpcd3CsX_kzC3Zcg1j4OwQJOWKZLnKKgzRRWjNVqSfMUopkQgN1w-8sdPSVsEm6DnGrS9Du-F1XKbUGsgF-Psnwk_sophyNFCc5_9gHRRwRRPxfNS-skf0487und-j3guwcMGssCaQfNNWLTNfdkwEjQWCmtXmxcW8IE3sbLuY9cDrMBYK0RX_7dsvem0r5qok9wV2iBMghuP2BG5I9U8UdA-Cb_yjHo91uzPuIPemRZqInZ7HCaOLzdZKBhTw6eYRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه باگ توی واتس‌اپ اندروید پیدا شده که روی بعضی گوشی‌ها می‌تونه اجازه بده بدون باز کردن قفل گوشی، به گالری و عکس‌های شخصی دسترسی پیدا بشه. این کار نه هک پیچیده‌ای میخواد و نه دانش فنی؛ فقط فرد باید گوشی رو در اختیار داشته باشه.
ماجرا از طریق تماس ویدیویی واتس‌اپ و گزینه‌های Meta AI انجام میشه و روی گوشی‌هایی مثل Pixel 6 Pro و Oppo K13 جواب داده، اما مثلاً Galaxy S25 Ultra جلوی این دسترسی رو می‌گیره.
©
notebookcheck
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">معاون سیاسی دفتر رئیس‌جمهور گفته "پزشکیان معتقده دوره محدودیت و فیلترینگ گذشته و اینترنت طبقاتی و فروش فیلترشکن به هیچ وجه قابل قبول نیست".
حالا حدس بزنین رئیس‌جمهور و رئیس شورای عالی فضای مجازی کیه؟
جواب درسته؛ مسعود پزشکیان
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ddsn2bWlzAoIn2vfK7t26sVm_40hX4VcNnH8DOkEvR6wYnX9aAJUrpRoX6i8to5rR48vEmqoilWno9wcklaXLrw6Set4pugckHGV2S5PYrMqKKip-b7bYFgI6AWwO2D8PcXN5wVgcGych4AiIio7EMuga3_1LU_wqfLPYKe653gyD8f81dlwpryNeDSzSA4B6-Y5JXp53BLvAvTV6mOCE3Os2dt2EcPUkLNt4hZ7HZP9fhmwGD3as49PSJ3MybzoGTTCW3A5NSo9Kp_YPLreLa6kDk_oYH32X2dOUEU4ktsOuxL7VNBPG1jvNWy_Ou7YqR9FXYw-Zr1iL0X9zrztlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Echoes یه ابزار متن‌باز و رایگان برای کارهای شبکه و توسعه هست، که چندین ابزار کاربردی رو یکجا در اختیارمون میذاره. از جمله امکاناتش میشه به پینگ، اسکن پورت، اتصال SSH به سرورها، بررسی اطلاعات DNS، WHOIS و IP/GeoIP، ارسال درخواست‌های HTTP و مدیریت DNSهای کلودفلر اشاره کرد. همچنین امکان بررسی وضعیت سرورها از نقاط مختلف دنیا و مانیتور کردن آپ‌تایم اونهارو داره.
👉
github.com/SinaXhpm/Echoes/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kmLwbXyN_TSl72s_72LwiitWtejmV3bm1BFkdQ0mII3tI1Ht4JFljzajDmLB0KpswO9G6kj7vGa0O0D6A5psysg6JWxKkAtg1injklvnJXFy_Mi9cAcQFhfQ24_5Y3Ch1MkRMT0PD-F2_9uadNYDmWIBoS6Rxd0cwM0rXrt2KrhAmIEGU-OiBlUnQwgBtSuXUCLx1vNcgpOLyDu5Tf7kmj1S7aE8nof_qghGd4In8Awgnnfy34BD5wI8WP4fch39WxBxJAL7SpFUHzX-7ZqNc1tFRELxMEXkeWUtcmhV_wOAfu_9n-obNQ6JxNzXRzjuIMaGl2RTo4YitRsoWTC-5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بانک مهر ایران!
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sTrzju3gqwsfCTkclxEQ1kt6HfIoJYJKV_e8o1h0RDtg5Dui8Z2PSsfxRwH0iNm36BxDWv7tgW8YFLVAK2J80IpI_JTD3LeWLfew3pqxW_0ZJ5_MuhTrYQcNuz0namV43gzrD_tl2mghxFPNruyGSLATEPhNo3lGoX0Y6gIhRMyfTdQgshsWu3Z9WLZ8B5dJhRsiqb3nCFvqvdyWiUePcJW7rILP3DWuSB3tVIhqzX01QHvRjLKbsgUa896K2BeaTbFGhAk_wAUcnM0dULMAjRjvr4pr6EpIb_siiOCVP1U5xysK8VGFoV62C5m0hXEu0yiGTFipfuu5KZQLvq9qPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که بانک مسکن داره، ستودنیه!
کاربران پیش از نصب نسخه اپلیکیشن همراه بانک لازم است، ابتدا هش نسخه دانلود شده از سایت بانک یا سایر منابع را با استفاده از الگوریتم استاندارد MD5 به یکی از طرق معمول محاسبه نموده و مقدار بدست آمده را با هش زیر، مقایسه و در صورت یکسان بودن مقادیر از اصالت و یکپارچگی نسخه دانلود شده، اطمینان حاصل و سپس نسبت به نصب نسخه اقدام نمایند.
©
alirazzazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q4pgqCw32i9X4X-aCcGBT2wX_xOLmzfZm96G8y4qotxe_kR23tpMC4MBreKGT88AWkUHUO6PLEEpTrOAn6pPSOWnDOcV0vz8UqtS3L0lHnVF360gkyOW5CAb6bUyUKAbGrzi9YsrFin4JiMlHj1DKzFzMiRBylp6ZcAdX_CCeXvziY9Lc0zXvCxNhLu4ytyIgaNIXlfOOPS6n0llLmcaKP2whOmUd1sOcIvY49dJw-gjWScz4yr3ikiq9s-RqyKcDk8bp5TSPQ-B-75WxDikpwAWpbYLnQYtJz-jtWgXwSaLOyBUIp5YBByI8zQ46FhCSv6rC9p3HPnROiSBMhPCpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دستور پیگیری فوری
#ترافیک‌خواری
اپراتورها به کجا رسید؟
چندبرابر پول اینترنت میدیم، چندبرابر هزینه VPN میشه؛ تهشم آشغال‌نت تحویل می‌گیریم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t_puZC2MqRPCT8YCXMdiIUAzEvib48XSoFXVkAe3EvxkWA1OriWp5PdWX2FdJns37jBHBDFoXVLDndiHLVPBQPzXM7eMs0evBhEhYxMKQErUC7pHz0RjrIdGD11eYPxUegK89RS4i_i5JYa2romYXfChQ5klpNkFnr_xjaNTNnVaVR5ocumDpM5TqtK3SvNmpd7k3r7UozZRW1PqX88nL-NyAREkat-0fh-yewvaIjV4nA_nHFDOJotpWWRI1zN4sqiizNGJ2gFXIeSuiAeg72ZIdWjTv0uA9VCAdyrAtSMVDTeDKHgGhMYIM92NOdSA-eXzKTCaSSRvZrlZ7gsvfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پانتگنوس یه ابزار متن‌باز و رایگانه که برای پژوهش و بررسی‌های امنیتی روی فایل‌های کانفیگ VPN و پروکسی ساخته شده. این ابزار بصورت خط فرمان و نسخه تحت وب در دسترسه و می‌تونه فایل‌های رمزنگاری‌شده با فرمت‌های اختصاصی بعضی کلاینت‌های اندروید و دسکتاپ رو بررسی و اطلاعات قابل خوندن مثل مشخصات سرور و تنظیمات کانفیگ رو از داخلشون استخراج کنه.
ابزار Pantegnos از فرمت‌های مختلفی مثل SlipNet، HTTP Injector، DarkTunnel، NapsternetV، NetMod و Happ Proxy پشتیبانی می‌کنه و برای تحلیل و بررسی کانفیگ‌هایی که توسط بعضی کانال‌ها و منابع مشکوک منتشر میشن، می‌تونه مفید باشه.
👉
github.com/FrontierTM/Pantegnos/releases
💡
frontiertm.github.io/Pantegnos
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QUCicbOtzcrEtgr6oRV6ypdPcB_0TbMCWlYVnsZZp_sWybMCNsSiAEzrJW9gI2ht8cxPI0FMK_drO44LGl1KEAlPITDs6zs-6NDCyn3xGBlmy_QHvjl783OuFcA8WsGUJ1Q_Vt9I3qi_nNMVRX94zAC6_tXfOOvgQzu-LrDeJzxqUKHAuYVYMtTeWCRQLQMS4CNN8gGba9jxd398A3YqTOKtAwna0VE5egp6CAZQ5WA0nzKlEDVdCIPdXI16gGKEcltiXn3iOo3Em-D4zhlde634IqVWgJ7Wz_PYG9ONGZ2OZze4xAx03iaN6OIxIrJACDjwrt3eAETdIkNAPS89Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپیس‌ایکس می‌خواد Starlink Mobile رو به یک رقیب جدی برای اپراتورهای موبایل تبدیل کنه. این شرکت در گزارش مالی جدیدش اعلام کرده قصد داره سرویس اتصال مستقیم گوشی به ماهواره رو گسترش بده و در کنار شبکه ماهواره‌ای، از زیرساخت‌های زمینی هم برای ارائه خدمات موبایل استفاده کنه.
©
satellitetoday
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/seYqsNwjDXDc13WKoZPXD5aAcwl16TiCSMPBg4Aev0fHPpKxJJRd5QDZcXyiPsGz-0xeFuB8Klsrvc8PP237125JZpv9CB46rIjBoB0v7KM4bE074XMjAuYM0Wzdkrzhp0_7YVVKP4FtOXT3pr_PH21HOFSNPibO_02Qol0XB85NxaO87mKcnxN6sTu2w3tzprWe_oUEaL9kiNQobY_FyTPoYMQLPKH4F1E5gyFzQ3UuCG1yixU6EFYTbePFg4RJXK0sZa5xygFoxY01IWdzVGJmm4WHcMdSp389EbBugO45HeEmMyGt78iLnMpQ7ijYHdSoQ-Z8gA9d9TegA9ot6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WDV9ozTLKcIeFTwqmLql5PII4xreE70TYItZQLlS-gtIk8jkhQBZ5yl0ax2CeVM_m-jGOX93V1tGgM4c52d0ClUFI0AHdg-86WM4loGBdj8j0z8qQpM8qyXB-_kGyN_H2R6uz_eeYigDG2aMNaXDb5HTOU8QxeWDme-OXJGoPtn6rBUJwbNF9nRG_zui9KPqTU8ymaISxlMEMBfK4tvTraR11oHfUVqxba3MlS1XB2FZ3iWqyytz5IOA1HtpNL4VB20llAao_-pdgBhZMX4ZLnjjUKM7fJb7XiDDkFPJLIgs2U9__9z6nwDqQs8sFsamRidqM2Y5zLtH6jZplj0pLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام داره روی یک نوع WEB Proxy جدید کار می‌کنه که ترافیک معمول MTProxy رو از طریق یک WebView داخلی و روی HTTPS یا WebSocket منتقل می‌کنه. در سمت سرور هم این ارتباط‌ها دوباره از هم جدا میشن و هرکدوم به یک MTProxy معمولی وصل میشن.
این روش به سیستم‌عامل خاصی وابسته نیست و نکته جالب اینه که دامنه این WEB Proxy مثل یه سایت HTTPS معمولی دیده میشه و فقط درخواست‌هایی که اطلاعات مخصوص پروکسی رو داشته باشن، صفحه واسط (Bridge Page) مربوط به پروکسی رو دریافت می‌کنن.
👉
github.com/telegramdesktop/tproxy-server
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QBHVTzvZp5WOlN9rFJS2Ly1vNuU2pLbfQIncq98k0rZleJuuikLsFwu5e1OSYknuZ9jgHbMFuOpDvLHLWqqArd7ENCNI3hMoCRKZ5o8fEB6n2EArFQB1s-2GGWpsD6WYT3A6gn6MJSqrl4vssJUiSqrR9STRYKmzQvNWKR5ax7ta3cZTWyhO1DRZTmkV7dtXt8wZcAElnoSwFBj1q4tdjm80yz7bTi_1ny5xi_zYpxRGX8lcto9YMr_-NvtqbfB2FfVh-dVBuQj7gLw32rX-LPLIONPPpIHU38_y-zhHGVDiDmL8_rDFgMnqqA1jA_BHw5R56knmNE4S2mg60bWegg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدهای نسخه دسکتاپ از تلگرام نشانه‌هایی از یک پروکسی آزمایشی جدید با نام WEB مشاهده کردن، که از WebView و ارتباطات مبتنی بر HTTPS/WebSocket استفاده می‌کنه. این قابلیت هنوز در حال توسعه هست و مشخص نیست نسخه نهایی اون دقیقاً با چه معماری و مشخصاتی منتشر بشه.
©
telelakel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oCHQ6syW-C_TIFltN5eR5_L2zeW7cZrHZBb_SDN07NKOwS5PvbxaiLasuWybaDyoGb4OBwQjmqvX8Od129AoOtjfkTBy5baq6s3G5YpM_9Vi7EXt7G3A-p8D6eAnE_O_MpPiznNPSh7G3dQ9pZ53VvhmnbYAudJL8GNvXpbdghop87r6ZaR2cEQQiT_uCBaD7GsejaU_GdSL0vQuxTZZnH1Z06S_1rqQ3_qjZYLmf8HWuSw0nY36a_ztr6p4FkmGyXmi80RLxngKpTQvwxXPYkN5EUsMNSQHDiinIHkhveQ0anT_JRg-HZ1xgGdOYovUlMNwxIrp2IdOSDst8MkYQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا با همکاری سازمان ETSI یک استاندارد امنیتی جدید برای VPNها با نام EN 304 620 معرفی کرده که در چارچوب قانون Cyber Resilience Act قرار می‌گیره. بر اساس این استاندارد، VPNهایی که در بازار اروپا عرضه میشن باید حداقل استانداردهای مشخصی در زمینه رمزنگاری، احراز هویت، مدیریت کلیدها و مقابله با آسیب‌پذیری‌های امنیتی داشته باشن و این موارد هم قابل بررسی و ممیزی باشه.
البته این مقررات به معنی ممنوعیت VPN یا محدود کردن دسترسی به اونها نیست؛ هدفشون اینه که VPNهای ناامن و بی‌کیفیت از بازار کنار گذاشته بشن و سطح امنیت سرویس‌های موجود بالاتر بره.
شرکت‌هایی مثل NordVPN، Surfshark، Cisco، Google، Palo Alto Networks و Airbus هم در تدوین این الزامات مشارکت داشتن. از طرف دیگه، ارائه‌دهندگان VPN باید آسیب‌پذیری‌های جدی و فعال رو سریع‌تر گزارش و برطرف کنن.
در نهایت، اتحادیه اروپا میخواد حداقل سطح امنیت محصولات دیجیتال، از جمله VPNهارو در بازار خودش بالا ببره و اجرای کامل الزامات این قانون تا پایان ۲۰۲۷ دنبال میشه.
©
techradar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wa_Pvwt7eutjrm3tFUha8Ae73pQO4XPGOirVlLTzKA6VEnuOJVqJrVv2qTYjcxBmreexx_GNrM_XdCi9eTI_RM1EpoAKtKRCXPsFmdwtMRDhn-pqvWcBXqfBklPLSm51WEE4n9O8mGy8kfNta202xbLNnuOc62EM91MqzoWwNK3y0n6-4avKI10pbzjq25lNkxFKyUaEd6dS0FMouurWNBKNyfX3QzmFMxvBLwX6e_vntsJywe-ef1woxkSNSo4uB6W38JtL4V8gcqmnfyKW6uGNFzUxTJ71NynJt5vxgrP4KXMqT2HXu6JW-2HevJw6EcFNGtBg8jtnxTwT-4OyrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم پس‌کوچه با بررسی نسخه اندروید فیلترشکن Line VPN که تا الان بیش از یک میلیون بار از گوگل‌پلی دانلود شده، ۶ ایراد امنیتی مهم در بخش‌های مختلف اون پیدا کرده، که در سطح بالا ارزیابی میشن.
مشکل اصلی و مشترک در تمام این موارد یک چیزه، که اپلیکیشن در چند نقطه حساس نمی‌تونه با اطمینان تشخیص بده آیا اطلاعاتی که دریافت می‌کنه واقعاً از سرور مورد اعتماد اومدن یا نه، و آیا هویتی که برای اتصال استفاده می‌کنه فقط در اختیار یک کاربر مجاز قرار داره یا خیر.
پس‌کوچه این وی‌پی‌ان رو بیش از اینکه سپر باشه، به ریسک امنیتی تشبیه کرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YBh1lhZaJUsu05X75R2x1H8NZtJwWFzUQ7AwniTj3zG_AUewmzJB-pYbMG1LPlAwx4bykO3s7sRHgfOd7NTAve5zWOoJaetGCgm2aaRNeut5mwHkTdSZHiNWCGEDiFJar-WJF5LRkUXagC7HPPktK0C8CYphrln326swYMjeS-gMtOvm1KGm_mk0pmRbYHQef2r_leGkyNYkUD7lDh1PbDI5cvcUvQ4M6jbxhUizXBgiVK1SsAFzg8Gr_JGQfDV23UTl7hPk6akjeMDgNTSl-S9p9K-go5xRCj0DqPva5OnA9Ok6r-jD4RYmcXGYdfGquK8fO_RZiGFhLSWGEpXBEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ایرانسل و همراه‌اول فکر کنم یه بسته رو به چند نفر میفروشن.
©
ali__m___i
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ظاهراً پلتفرم شنوتو، میزبان هزاران پادکست ایرانی، توسط کارگروه تعیین مصادیق مجرمانه فیلتر شده است. طبق قانون شش نفر از اعضای این کارگروه ۱۲ نفره از طرف دولت هستند. دولتی که در «ستادش» اعلام کرد دیگر هیچ پلتفرمی بدون تأیید رئیس‌جمهور فیلتر نمی‌شود!
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T2YHhBJs_bPV2ThsLAvULwUeil1SuvW8rETxYXGvYd6vsZMDskYfjstG6UGTVy-p91DwCUolwzrxBCpCA7c5lnhLzQtbou31-Mg96dPBfM17CPzMuWhA9ZmCKjSs5XS-dzIf_M_06tYf1-OIcIbNCowWlxHDearcuanWxJEDX1Wrn_HvPHrzbg1kQ9cgxRziWhHwYw9gbkq2M4cBqquAQkcJdenO9dUKRgNr30ZOcp0Lc3MSMyTWXBfnK7-Y_RZxqW92XSnjUmUJT2bw1E3OVXggOj2mu45U6tmgL24luNT9crZEP6IaqHn5S9VykuKOKNWnwONYPEdawp7fSocyOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران شرکت امنیتی Socket شبکه‌ای متشکل از ۷۳۷ افزونه رایگان VPN رو در فروشگاه Chrome شناسایی کردن که عمدتاً کاربران روسی‌زبان رو هدف قرار می‌دادن. این افزونه‌ها در مجموع ۷۵٬۴۸۶ بار نصب شده بودن و ۲۷۴ مورد از اونها با جعل نام و هویت ۶۶ سرویس معتبر از جمله Proton VPN، NordVPN، Surfshark، ExpressVPN، CyberGhost، Windscribe، TunnelBear و Cloudflare
1.1.1.1
منتشر شده بودن.
بخش عمده افزونه‌ها پس از اتصال، تمام ترافیک مرورگر رو از طریق سرورهای SOCKS5 تحت کنترل یک زیرساخت ناشناس عبور می‌دادن. در نتیجه، گردانندگان این زیرساخت می‌تونستن مقصدهای بازدیدشده، IP کاربر، اطلاعات SNI و داده‌هایی رو که بدون رمزنگاری HTTPS ارسال میشن مشاهده کنن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d2RtGlLa-faa3wmjLVo640r2RnuKP-_VCbELwacSaH_UFvIUXMGnyYZUx5XZfUNGDUvyY4hxJ2pk-kUTV6Ow9RIJ_CECDeTqXQ-zWBbiOC4IXDzWhk1N9ZyTowacEJUrgDK6b95GQt06YTDkp_CZWmER97rlhaTXFrvzf7t9622TxdAPtuvbGMmGh-VCL9GYpO_8gRQvzrYtzCQGd_d5rmUjizfPw9SMTyzaUIhF5lNlKRZIThJUsV-ydKjVVkM7McrAKuLROzJszEhAVPjNYRXym2Nj9ZaPDadm05BeELXkHZdbGfS9otJAh01EmVAiLHvkRCjwiMHoO87YYe2d7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteVPN یک VPN متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که بر پایه‌ی هسته‌ی Mihomo ساخته شده.
این برنامه با پشتیبانی از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard، امکان اتصال از طریق سابسکریپشن یا اضافه‌کردن دستی سرورها رو فراهم می‌کنه.
👉
github.com/WhiteDNS/WhiteVPN/releases
💡
github.com/WhiteDNS/WhiteVPN-Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">قوه عاقله برای بار نمیدونم چندم دامنه
workers.dev
مربوط به کلودفلر رو فیلتر کرد و مشخص نیست بازم از فیلتر دربیاد یا نه. بهرحال "در سر عقل باید"، اما 404 مشاهده شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اینترنت همین الانش هم طبقاتیه، چون هزینه بسته‌های اینترنت رو اونقدر بالا بردن که دیگه خریدشون در حد توانمون نیست!
©
Kiyas
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اینترنت ایران باید به لیست شکنجه‌های تاریخ بشر اضافه بشه ...
©
thepanue
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=bhvSU3cBnV_R5ACHNfXO8LirKeFFOrc8kC4c7lcEIjUUntnzC7rMm7ZU8qwBT2Hda_3DDzncRjMskRbj8Kf4SEFczTtI6u5Mb0zPOqnd3tb7YrQTKWjuf4FOUGBeblDM28tNI7XPjsCjXsPFnRd1BDYygC7F7IWkZDF0MVlEW1hL3bU7oJAtTu-Bpgnw7rxrnooTHaMuI2bX6yYrgPfBVCjkzpHMihmq3InESVZZB2nzohJp3EIbEXL312LLtD84gaQDv0IY8ygXk4PVx1u8J_N4MFbdt9bdFBxjI7BEUz_gP99gXSeqlRK9Ygae0uAMdzPHkMRL4rs_k1Lzd74DdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=bhvSU3cBnV_R5ACHNfXO8LirKeFFOrc8kC4c7lcEIjUUntnzC7rMm7ZU8qwBT2Hda_3DDzncRjMskRbj8Kf4SEFczTtI6u5Mb0zPOqnd3tb7YrQTKWjuf4FOUGBeblDM28tNI7XPjsCjXsPFnRd1BDYygC7F7IWkZDF0MVlEW1hL3bU7oJAtTu-Bpgnw7rxrnooTHaMuI2bX6yYrgPfBVCjkzpHMihmq3InESVZZB2nzohJp3EIbEXL312LLtD84gaQDv0IY8ygXk4PVx1u8J_N4MFbdt9bdFBxjI7BEUz_gP99gXSeqlRK9Ygae0uAMdzPHkMRL4rs_k1Lzd74DdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ممد ساخته. یکی از محمدها، که نمیشناسمش و قرار نیست بدونیم کدوم یکیشونه؛ ولی باهاش کلی خندیدم
😂
©
Mohammad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hoEukt_KzbSFVoTYbjQPfRkYJaFdqt7tZZQmZt9mzhuyaDK1ZNkL0QeAsC5_15vG3pVaCmKIjEpgphOt5VhjRm4iCSo6o1BkKOS5NeXUIXWqNBD0km9s7HvhFlSRPgc6qOoDFu1z9lsxXS7W0HJn_miM_Fexdn70igJNtLBK3UvEYV1zcjJpkphtFLqwzFo4lCAFBHRB1A2FzWdJEIOkV3f5jSn5zUBB268p3KqXPZuSgfkw4Ey7tZphGjS6agr7Cu5W8zEAkQYJb4tCnwx-r2K2sOoQ2EDYgF23NWasRsFkIqEyjNCZ9M7FwAsK4693dnnEivBBEfkc_WyUqnxqfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکثر آنتی‌ویروس‌ها (از درپیت تا لاکچری) سایت بانک ملی رو فلگ کردن، چون سرتیفیکیتش منقضی شده!
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fRxhl13kh60xnAGOK-zXEM_EJNTkA87KtI0lKh3evJSOQZ_pdLOMXdisc42KWoT946CGc6Tvj0OzTfJEaHO0KVvB-XY785Zwsey0r6hs5Izo3eTiDLxNKVgGzyjhqluzgxcF8WEJmEsSlTyopgKLgJnpiWdY6azuZCDer32Gxw_-C-L1lJnUn9WN1Zz7eZZzQ22y-39C01lQipvKxHmA2ua80iz0Cyp2bo6TRxD47vRtLDuF-RloRnBTarJrQpOXE9xCx3etnWPhISkpCsSZHZ3ii132dhILQr2ZrIIYxWr03IS6Czxm7-r2Hn5nJBxxNiFlO2wxMuI0wtB0jd-OGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات مخابرات گفته دستورالعمل جدیدی برای محدودیت VPN روی اینترنت ثابت ابلاغ نشده و ممکنه از مشکلات فنی شبکه یا نحوه عملکرد خود فیلترشکن‌ها باشه!
🤡
در رابطه با اینکه اختلال‌های اینترنت وضعیتی فاجعه‌بار دارن که جای صحبت نیست؛ فقط اگر بدون دستورالعمل دارن گند میزنن، یعنی دیگه خیلی کاسه داغ‌تر از آشن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ohrLGirsAzwMGcn_wPp4Rha1LhGh2XrTuF-gP2JN2ugS_5Q793lMLcAMHYEt4z9GDbrwaD_cdOWG7OJLqjU4ZxG-zKeerTNGhQHzdXEeCBRJyxbdWYnklp7cvFGD8lMQeFtv_poiViNMGzRptkKVMIQoTiMg-urzBTAl0AHSs5TGPY9GtbaGt3nx2c42w0vaadWbopF9NLX8hBlpSa2JqFD4NkPh3Z8yJNISyKiE1dppCYWpOIfMsWR3Jv3AaX0_-Ps7xxehTTqZCIKoBDQWqdent62_CzpQ8spF2CpyvfzA3guvKmZOFldOkqRqd_2BKm9VwEW93J29i7fp6dnezg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qzgo2KBCQZf8opp4bZa2KzE8hku1L1JNeKeZ1MXw7YbSKL42jqRVI77OXBP9Bbx6ISD-CcKLQ_PC23w-3r2EBHH4vTzSua1jxP7E43_Nho6f4grAOI34tXcX9KLyferIdXXsnyhoqVN27t69q6-RCJ5cT31r6Tqbxb2cQHhr5ZZ9DtLFj5iEbgvU3mGrMq8e0j97oHzTxMFKRh5OVtMA_yxmJthA_Q-E1E3JihDlnFqfA8caY77OkcG95RW4b8DXumiY9dX5iimdg2i8XdSoJ411Qs5qaS1_Dz-1B9HLVIqQuE19RIVbxOtK5o6j6jDj8qpapR2srbGf28FXi9AvBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LtLnXf2P10ECdweATDxcwsBmit5OHt2ku_rg43ntA1x4K801noTxbUCdmDOPowgIxGuIMiEBPVgPxKd3AVs0t8iP1LL4TBO4GdFQgAYWWH0R9_Ou_47joQ2vFM5dVActNl_pPcGEUCDctyNGGfTGFLDIaJp2rWnnN4-QuysPMX7NF29unm3x5nmV0X0qOwvh4Bt_98YlYJv9VDf6wjDwNHz0Rc5LWvcIgSey88w4z3dxLVtkkCn8iWdhsNO0MoffIhubtXMmjWuVQKKQkeuNL7UbU8XPdTD0KqpHyXXRSKBAE2cvwnOJ002sgP3kGfcyySGjeTUHeujn5ISdI_9QKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RcEuD-AJo0CP2V2IoIynlomanqWeyD7MmAqk-90X7epKzNpXmc3gFROAGOd5PqrRQzHyq-yU6JqxzxOeSOSN9YtOL2jetsYQ4z4rkgFxmP_tNS2H4wRsTqNKg8HLExraOCwNZdva9dP9JZT_Mbl7KYSFFAlQzm1n-m7pXULkVOuVAa-LRsFQcFCZ0B4gt4D6CuuLKNquBnWortORVPSQmxirGOkog2IJHlGzJErgPLf31xfF7wQIoT_9VQSde06lsr8i7xFqcATuX-JuqAkTMXxdrXmO8ji_Dv03Nwf_9bSZJHCEgb1dTjxl1HFn8MRg-rv8uSJ3k6fcAo7S0Muqgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه عده‌ای از عناصر فرصت‌طلب سودجو عنوان می‌کنن اینترنت قوی و زیبای ما گران شده است. برای شفاف سازی میگم بسته‌ای که شش ماه پیش خریدم 1,348,000 تومان، الان شده 3,870,000 تومان. قیمت فقط ۳ برابر شده، گران نشده.
بنده هم با ارائه سند میگم اینترنت گران نشده، فقط ۳ برابر شده!
©
mrweb24
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ji7megcP5MuCpkCECaT8NSlAqrzfQmQne0bq6Cs3VmEzjvOhTXwYEnF5s-3MTWPfh_EgHbSbb6dulM33mwQARLk41TNUn-umGPc2aQdRY5dDQtmu5pVwoNv-slbyrvGpoxhGbevQco9CbYUGqG6t8MzQcjhcEQrocM7KUtEK8HXJRfUGCB9d1quKEgA1H7P5ymtB5FUsOBRKWZX8AColXjpM2pVOFgi6RpWEyO_jFRNXhIoHLfDIMnIEZh2hGALYKvemSLcWREGi8SBLE0zfM6isNNku40UCzYtmp9enmOptUEJ_SwHj8UvjGghCH3sPevm0ftCFS2iFznnEgyaGfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mpIK0zLZuNSTcX0Z1b4moeusBy2rOFJunK0-6BUzTcBCyrLGIFmLer3WAAPWdSUDpM7HW5Zz-1LTcf4bIqFO7NIfwcuOhVoN1fIojnlYVx8gQvf1N9XvGuIeOWXRUjFSxZKjKx2lC6toVgp9gObZUeHZeUT9drjzdaDet4rlYnEcS8tbWI2Ly5HOu2h5NtWkFVkIfXPDgIDfUrhvsaS9QQuDvorAYF5d6vt76RLs1_OWUIWI1rtOr_4DIz2nWukJdHWVxJU8EdLT3m1AV1VAR4uUsxxhC3NTrJ88PfQZrtF3bawS4NgCLYHqv7EsAFjeoEPEUXo9j9YRocGlavSWYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">چند پورت مهم مانند پورت ٢٢ از سمت زیرساخت بر روی آیپی‌های ایران به سمت شبکه بین‌الملل محدود شده است.
همچنین شواهد و بررسی‌ها نشان می‌دهند که ارتباطات زیرساخت برای ایجاد یک قطعی گسترده در حالت آماده‌باش می‌باشد.
©
manageit
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V-AJZwYDZXP3HMRHDV8F8-C14YjkWBd82Q17UoMC9hp9HMRxdEjlGBJ1DpB9xk3cL6K0PwZNHMZX0Z6WxI7sOU-JXumYxWRiAZr0HnsAu5WyYzU8nQ-367txXjPPBwKYLR8ML8_FvhspIOhTP-Tjeoo2fC3GcfUP8aAE-CwGHovuIDOwkSfSLpaclDC98Rd_13DfyRRZ1kpwqTzlly4aqEmRLBingQgKIqJ8pOtxa8NtDwLf6OezTJ33OPBKHGqap5Xkl93J_jb9YxQ-DDTFwSbBPgLvUNUVjys9_x3v21lGYLh-OfCYBs3bdEDnGm53DX6xrnE27fCWPFQ8xGZYIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">چرا کسی از این موضوع که "سیمکارتایی که استفاده نمیکنی رو واگذار میکنن، در حالی که طرف با اون خط اکانت تلگرام داره و چتاشو شخص جدید میتونه بخونه" چیزی نمیگه؟
©
shara77miaa
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F-RIAcGQf6Hv21L209iV6HcObHDq_0ioniow9v8CojGFZbaLR1M4kVxi7Jdd3GCpmgznN9abApjzjmK3ijw_pBwdM-VfBazRVZPHAucPXGFJ2US9tfzvTbiFDdcNww2brxgnK1TRda_p24U328AUAi-o6_2uqoYdt0TXF70EzNyzQvCD9k4rF2aM7Rv4IIKX6jL-UqNr0IG9hl9PZvImjlx_-h90A29EKoWpNgQdS5dcEy1MpznU0Xt3wfiTelxUlUJCKaFejOYZVhVRLEtKmyBoVUi0WoJ-xESq3szZV3fk8u3829ChHpm512LrYmCmpQD2rs7WHKuavcv0-lMtzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZjMj-uunqsdurQa7d_jiLyW0kn4YMbAOjyEAogLWfd--MV6it2g6uIytDExjzgF5kIVX4sfUFUclkQ7cIVL4B2qqP5UNLSY8_CkozCt9mtMGVzBq5xd5Zg-etMB5DZz9qCpuyOJlv-9yBD4e0EKFb--lJHk53NbbFxUEje7nEKpb2PstnXIwWId7GpMGyHb8EvQpYCOaOSz0M1oadd8NiuyEMAVRN6uUUr1QiafRauZMHgZgbhig1kbaWlwiJiNu8SrnNM9S_D3JMGNj2n4--62DNSS1y7M8oyYZUcsOIcWj2a9KBYzp_Qu-kYLXSrTgjZS7Mf-Y5timwypguoCJ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی و با چه مجوزی تصمیم گرفت ضریب بسته‌های اینترنت بین‌الملل رو بدون اطلاع‌رسانی تغییر بده؟
قبلاً ۵ گیگ اینترنت میخریدیم = ۱۰ گیگ داخلی بود! و فقط پول ۵ گیگ رو میدادیم. الان پول ۱۰ گیگ رو می‌گیرن!!! فقط نصف اینترنت بین‌الملل میتونی استفاده کنی! بی سر و صدا دزدی میکنن با عوض کردن مدل درامدی!
غرامت قطعی‌های ماه‌ها اینترنت هم هنوز پرداخت نشده. این دزدی سازمان‌یافته‌ست که با حمایت وزارت پست و تلگراف اجرایی شده !
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lu4A6qhJm94Cd0v2HE8o4oAdEwHbUc50J1qmrQnRG1JFstsdfjSwtqF077OW9P5DCHB18s6zFp39Fsio5TWTgF1gKvFlM_NVQRHqQCvNWCMNt-OeusJx1gMNRR-NYFVNY21o6H6dk9_YzMokhpoIQI8v4XdnxOh3fUfu_aF2TDoFjdH7IkTghHvEgFD7P0JSEnh1ZyhkMpQ0dnIwcGBFjZTdrtmSG-MwHQm_QJFt4Hvvuips_iOF5G8yMiUcEgHq63b9pgf69njAnvP17_WmYIIZFpRvHGstJLYybw--l1sUycZXjVA1IO0Yy96fNaNLMr5BdIOdJWESQpPjwNhEfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aerial یه رادیوی متن‌باز و رایگان برای اندروید هست، که باهاش می‌تونین بدون نیاز به ثبت‌نام یا استفاده از فیلترشکن، به ایستگاه‌های رادیویی مختلف گوش کنین.
👉
github.com/shapeshed/aerial/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eyIbi_bzdcA0QavGWciOgBWnAxsf-HzVOG4xGUako-rQtYPtFiBltoZHR8DNmkCFZHzYlePzl_UILTiH00XnmF0cGSAle_yt1ZnTxvjXvomREr_4sYOrmzQO6y_FAFKSeSRmkCY8d417R15pdN2r7kn4q-37-7fVWVoqUJP1lk-ezwrtxSHEzM291LA3zxyqQZC_pTNx4F3Kf014VJvYPC88sjSeLeugvwn5FrrjA00Em_IqRdXO9NIbBpD_b_-_o-wHiO8rnLMcEJKHY1Jo7_DtMWWs8o8XHNizx5YVmust1cVI2wvquvgpqj_yPeVtCrbvdnF8RueHguzxESvj9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XgxzolGVhgfIoOeo1m39oh5-8bEOsCLn0Ac-JbzW0puNUQwXQ1aZBsdxcbs8vbIogT6vMf24maix7Ty3e7xeLo6irWW-hRxq0t-2CKlDs8xwUC-ZhFR2y_xNv0oIsIxBNu86Fy2DbMRs4Tk0fYHQbR5-OV9sUtMytI5pl8eR10LrgYgkVx0Ke_-JgKDCvbZp81ixK-4cabKHx0TCSrogJew7RkQMvfgH2BK1rCGqHFlPiiEJ4VHcdWTcJ8grRapc28r3TOAMN7p_DMADS_OwSZ9h2jf5lLxUJKTzFWcPFAXzJyThhwsCWilHxZpG__dO2oMMjPq03gcqpCmqwySFGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از راه‌ها مخفی‌کردن صورت مسئله، اینه که چندهفته پیام خطا نمایش بدی!
©
AmirMahdi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
