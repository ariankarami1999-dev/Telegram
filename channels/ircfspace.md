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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 17:51:23</div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rl5vO-NhqxbMtOBt77jJMrPKdZ7gPhPGqtAW8ks-38xvhhj2SOj2SQ2KLjtT8Yd2obOquVgWWHXBIbyy0l5Yhz0woOoK3xFitsyaTD4Fjx8eoLOiJ2-OhW5GnTr0uMmyXNYkx-ZiIvbraxYsFBSYHLQADWS2wmlKhdiH2oy_cj9oInCy0i5jSyKJMpUlHb8QTDJYrDz1uCssxFQLkhC1Es41xLv5d-bx7yozVpBnoIoK2BijRaNCqJZXrNmRfAd_JjSUFa7xQ31s1wVr-_1bD5EBwdK0WNFdgmYToWwU6MXJvmwY_0l4iolwkyy08ZixDE__J3DAnxDiNz4Fu2WtJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M9pM7HDK2COrKvCKQfG9bagmi67Y80CAyzWaye1_6NJTj1GNUl-00Xyi2GxIWvIE53kT-mEox8-pVerbTWKQWNrsYoGHoAsvKYaAYuq3-8dtLwkWr-24-N40bUKLyYrkM49wx165Ey60BQpoRLKynN758HgbrKYsuv8gC6LvlNzlcJ0CpNRSvG49Lqu2J0ebjPKTuG6NRgXmR5asiMBVitlcx7uIeSsFN7gYpJfLpuHgoEKigIn7Uvfn5cQ4uiZJVZKeB0qpZmDHkpSckEBhm3xhZJEKxqDU_c0O7WL4mVtmMDzjHz7_gzTZT0dPWc85EQ6TLvITFyOeq9H9D7VyQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ry3pA3RoA_J-8bFaCS8KjEGK5VxsOoxzt2ognA9nLlZilJhh7WWmtM-2hAiZJUN4d4AEUfJwA_uXMg_4TuUUKXdT7lbjnl_-FT72lLwTKpD3vksvLOH34nEAyG7C3LHVwn7TJfRZJIM1AsiBPXR5-_wJQTIzTIogcj2MGyU9pURM-NEffRmPMzqwnT7um6dOeKYLblmEdothzO__28pQ6Gr6AfwQT6OIm-BdM7oQqfUg6F4BEv-wPYND1WaXqE8HsWBjhf-U_0ZgwmsLjz5R7L1lbKc1yc06Fr7ZmsQAS3tTQtpUTWXwh_d_URMQP6TPTTOEbiJXp3efHLrHjTXiJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LKSLQnyMvfXiW-JdTcenK57UgzaCFAiUZtKKmEVAaCTfVBtA6O1HuS07UMwrjlYZq8fw5I8hEqFVQto2oH2NkZwso3BNIMmqBrbroWpg3VUXxSwQrWKdHcB5g8tTLPVd5RZEbRadw_wVrLzB1JnZBX8GnzrPMGajOrjun9GlX1lCFW2MdbScPSdCSRe26i4oGMlvW6BGdiaoUk7tZNJAbDuj1MZ55kEPmls5r81jijz_JJfc8Mjzd1tFrkl_cQwYU6NJx9t3h1x6NS-vKcNCYT5pjh_mBJ52WTyrnuFRYxsKadoi5E-Z5qKl6ULaGk_qKmQ93IaYZeITrYM5-N8Kaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JEsjcFFE_g-avvwTooXtzj08cxyNJhY3O81c1YK1jpKqaUzCYvuvL9jgJx-Jo7sehIky0zc-RKGp5ciCMJWrcqSTcKeaQQFX4JjHM_uZGog3fZoKpWajvw4ubomd77IqwBqnAxDC6qco9Ul0S6rx-thYwvICpLCxrQZpm7d6uGA-U3ptQ1fPNjQQ07Etst7GONecKjF-Mmt_g3GiX9kNwaJ72MZoTTpNx10LAX_XoexgVEXHvsSXS7ySLXKgwVLFKYXT87M6HJ_0ezZ2qMdKBHoxZzYhPBgT4CwrH3h0SZtG1mvFhXaacQ-iAbt1LtzVc9dv6t_nCg8fzSItDQ0HWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aNgl3FJd3YFuIyy0VA7XSJXzLANgWTpfksgfWgQtEkTztIXbbpXX48WZ4DKaxMKCDHouZQJjwDvk48qaj2hRhPie2zfUOIIMUD6A_TiWt5J-Vysubjc6SbmwPmfi4uTNmcgI-VA6MBlI5KEKKzcot9CLhnOe8Z5hvTgP0O6I24Y_hrsDqxUyBtfFxHcBUsjiS5plCzhUJQAb7NYxHRLam3ipoT50le6I5Aunvd_faCXR74FJiYCTnJ0gVg3b5UvWe8mQuvh2l_cxUkYnWiVlUwYoxY7dfEbsCXvAMa3NnYQk2_qMTpMwbgTJCgW3km5n-t-rmROYToErLMLIXCa6pA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NR9s230dYHpdnPp3bgpNqGaqze6rN6UjRj5bzM_Enq_uTnzzD1wwbyonRfeJcNWuZ6M_9X4ztTqU4D4SZ9Z370BlBmkwgTAX_A0pXQW7l5LskmlSFh_87YHK_YnYkXau8f8d0Dpm0tEC1jjBGC7ZxEPUKhra9Qabhc25C6CIpFp0axRT48V_-gnnfmJIYWqrHTC_XdKW9pIFC5EL-pQsCCYg4Ja3aAoM4pwGapAO9gA6oI3_zusfrNVCrPkJhFUIg8LtFqukT1ZbeChSAqB0-Cp5C_bGwHOjA17GNIWoahM2weu0gJeTbo82zMM9NSZk97T-ZlsGAdX1-a0UK6sS6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/enbulT1Ya1HqPbG5kHIDXpV5bddmMgXZXdBzOQB2G3VIuELUfqGbkghJbp48vf4gVd3aQhqpZ04nPoHw-KQhwqTgcP-YbjGvjbx2plyHNIMKJ6H2cbzggkx5mCb9DVolQ44v6fWmnJrg7-G8XrLlwKu18fvXhjdVbTLprk1Lwz3qBXJguh-_Kc11vSrH0swzjOOxYsirldMccH8CPRuabIEGjXmOS358tRWfxM-S6OzvuNpl0B7GF0Rez5sXC8raTDveS9pAct4XfSgE1lofEConTo-AdhxXIIUAbj_7yIXJlFdiYzaHPS3nkLxIzx5hvKL9WEOKXSH1Py4qdzAVlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NOSRoSLRkHDxoYeOOo6rxWHVeeJUMa3u999skMeABkyVaDYXJdef9ZaWa22Od_We06WEHZstJxobySlIJcfXPPEobcn-fwzLv-t6DETr-XHoEuWHQrTUPkMGDR7WXsDmNpt0v3HX5q1mLCZkBvKkny1DjOGjJeenmfCfGC8WZEqL_J-khlTFndWKObpQCIBpAhyG-BXRFuaRhwkdUcvujMy7siywh-gb43P-c5aIbfLGFnsYLfhd_AgDHkERDfBHKOlXZFrAO7sL6a-Z0m3Z3c3RQUgDgb1D5Q-PukqnxnozKkEyzqxfQ5xPyFwXTxAjj1fk0aVGv8LHfVFpAZOq2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TSgBiODCnpKeFL21YIs8WIYoEadlLdpQDioHuXNr1wC8j8TtnDShP4Jct1t0wkEJUt9WZAjmBrn0ArOe-Q1FeaGpPAQx20qtkAsmFbKqxMhjioSQanMbOlM_iAenFd7_WP46AL-EWPv3qDsnSur5fFDBuTfmcY5WqfWYykmBBFZQAYtbVj5KW5cfmsLKhAmfAezW49E6StytqEP_qz1afO3b0_1Co2Udc2_xGQX6yPe-mT-URsotWswQFFZi1Pm7kZcetZGRV4Q9cxuwDvWzj897_y6R30V2MjUa34oxH3uNcAFybnf7VQFFhlOOJLOanNgtvS75cBBSaX2eZcrM2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M0VUNzUfdVTlzCtzpJlee1rNwC4W3S4Owyuz9cI-cDIWWhAWQ0S2NWqg74y83HFMSKIFftughSDWdXC5QRNKCdOUX1cvcMmab8Q7mkv4PqjseCtDD1uduyysBtARvjI7-lfgCpLWt3hWROIasFIX4i2VkFT3ilDLbr4gp-bJq9A_ZTL1tFbysgHaPrzROsuhb8SPO39qDt6sTHoNwQMLoeAbjEkM5hwavoyVvjThk4ziG4bKuCw71qxvcEEK1MacT3Dz9VjoD81QK226hNUEz4airNgHQBVwvEPjt6aw0j2MeTlMrdi8XrlpeatqO3RgJoCZ_68YNmrupPCfP0nShQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZzY9tFnGETiUXowEZpMibCeY57S9bxgf20eSciL6VRFC3xz5uBcVmiHrL9C87rRGo7EEiFHn4g_KMXmOYI57_iHblObk4QUcUBwExwTQD4RUIcd9Sh2CdHCSfYYpYjPAFXNeQfk7oN4_6ct6Uu5DyBlrZ-Rmb8YHN1W2fcOuQ5LHcRxijflNeOlYaN-Kj_brnjE183rvC2aq48BRNDl4RQlB4bdajsfe7zUFLVZVBYqIl6R9Oyz7kTS1-75uOZEwBSramtrn69gBViSnQzRu1oMxPSBmpZEfRJp3hx8xxOa5CEPCGjyZwH_tay5E8zZQILchuomX6wga5RXBUehMZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dSnQbOYxcKcWugfWNApsQwSb8MRNn5DKpm5du-hbdpNWzNsRKhD-TjHh6GMWGutZFtmGZgKRCluMRALfuidceohZOFTcd6pXSsPUv7Ecw0g-rnE7ESRR5PpvduZJrGKeVBu6ZipP78JLG8V9g8BmT4_c9MoovO8chyEjEdVyZiVQoAixqQO7h33ET9MfSC_xm9T-6Lf85-6TElIULeCR2tHR4ZTpH7kzQOR4lf8msuYshEZFgyT4uKTM5QKW3HRuNaEO_jWgdGcov-4DREcc1eKY0q-negxijMsIa-carVen3FO_tXG1XEuqMm7zJZgxrc6d4viGzfurRqqmqa5TtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hszyJBxnUtiyMspRsstz3rVwMQE04WExUIgq3F35qBeYtpT6PxS-ZAWXHUKO0raYV4dZVFjV8KKAfcu1n8j475nBaU10Y8O9fPou1w4huuTQE1HzCP_cZA49BF1I2tmJgtJZ1ejvaXJY4tTZisC8D6VvxJnWpk8A7JFAS3JSmwh6XTpyVOV6PZwslthFPQUgXU2PW0Sx5bkJyvib2h05ovgc9NdWlwO1HULw9-FQ0mp8ZMJ4q1HBHZNUIlWghWPe2LhWu8ww6PDALMW1C1g6oieE8KuVEUPPdLOAKT8CCFkkTGqNXbTYCXFDuaq9MP1pwp6h0zPAh-jPQ2JTnDjf3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Op4hDMqsVbJLg4VWaATbOLMx2k5MNQZ1ULMGOs4D4KvJ9zdmhGe6OtqjCUomNciKNhYJSTd0EO7xgnLJqggQeEuAWCvGAZvd0g_aJdzzuZsxGGWTNPVm4L-yYMvumQNHwh6OUquhdYKmcZunM0Jc8x1jzVBWU3eeX2w9mPYLd6SVoUF5liuUYps3GUVyT7__aklPbuan4gDpliFNynOGAZtrz7QqjVrXi-OM-9fLLVMXXi4V_BxfGSiGu1686rXhB4pccnIOgLr_jNTg1UZiv43aXCd024YsZwTZGdAtZPUZhk68CUlP6Z_tE5kg2hQg2mLCrpkEZnvnxKh5Ifb8jw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UjWn9RvKJRvig7qK7JkOfzWlLeJ4uV1O8swPmp4bHijxuxfryDNwC_O-cGIMW4Wz2nzMWzpSeEcTZib2qBC07dEszdv2IBehzCDxnl767yHDiHAHtPH_jH5zE98Ag-JlIvHpGS-jz8kP_uYH_ltJXW57deH16Xyi5D8Ax7Gq7D_lJ2r9WhlAGr5IcXdAm6Ji08pAu6QxBBp6aausdRKp5YIp6xc5GV4r3V-SJaUAg-Vnyljrpez95yXU1q4DZvZK2IB-Al3Ky-OWbIBrJzdKwCJtx5l7FDO0wmsxh8mNt7OEqWqWFAiJgu7A3lmld0vi4jZ42kLSOmtPinNrdjV3Sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OaBV3OcILe1ZX_1kNEkqmtyHKmqzL6OZhURstTXqxcE7cLmDjsUlJBnELrN6SFT4MGecCNYDYbXAR5wgny7FgKfcBgds4JY57aSujHz6c_y1ivC-9ysvyMGjnb1467ygmRmVEnks5v5Pik-HZs3ToCL3Z-qrCYSRadsMLyFYknljq2RyrlnAOSPmA2k0RNrscQPo5f-ceEpnD5Brlibf1ci6LJVCCXzPAwVGZb3n50TJiX1mJeJovZVb-u-Uo17M8Yg2S7m_o4rptoWIrzyoXW3TG70Uth4SfCRU_4_HVwZcxrQQ1c5O9T_9YYkosOoZobKv8kwctLdWmafHZG8sKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yy-g-OOVauo1JFgC2x_6GvpXFwo1odQKE4gjCse0epQ_zy1bLJECIIHd4rdcUcST90nUjjb8GwgNQXhcHJIlOO4qY6M9Sm90J_w6NnJw_XGZsqEt9koPCvWpIVlZ_reJyF_IQY6MXW0cttxF8ecf7x1TceBtKO2eAZV9d5OmWGkgxJlvxOCY7jN-pb10p9YJnunjVNP-Y9LB0BRWYwJhyKClTUHru75qsMUOw3dtyPQQI0CFs_qaiB-zUP2Xan2pC8-zm_0CWhFWt0S5t3_HmOHn35gG3DcF_fbaaCmQnkKVlmBW3BECwQU7nYRaSSPJ-dSRGRDXSHhTZ6_KPkJAMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XxjZVkuU2HHFqLVXGOZL2KZ6BeTWjeH_S-oqusmymIamG_g3kw3q7RH2nE5c5Rvw1bRqRZ4xXnZYW0SCPC9tVe0sQ3boC71EhO5PKF-yiDbmRJbGRHy_lx-8YB75SCQI6_y8lHZbFvHfm5ArG5NssAfY0QwvimbuLDwvqaUNs0ZJkBQKb7qfQ0eXhZJ8s_k8j-avkovcCNNDfTrDKI81WXlaJwMHHqULlR2IxA0q3EdtHCU_4cOacVejNKoz59zWZWrQAlRNQp2M6E-NS0xSYeuYwXigFQoY8yYlIVhTMtgUKQqAbo0vyOZmdzm4ntsgYt06b8rsZ6qMkBSmWVtKoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qx49TPNJ3_SbEhlBmxJG2VbrmsX-WSUycTjEDOYTP9k8CppBoGR4xE0IxdaYPgZZRPfd9SPMNLBE9JPAhOXctWnfV0sqr0nifyXJCw8P4dMkpwlKiktYcYW_Gvgkcu90VOO0BmiG1TRwSjtEYmciDPYjCJcs3Jiuofu9GLyf5_nntkeHtr-QaoTfqhqef2HmhSgRQUiha5_Wkfos6w3oikOjitQ8WeDmPekIh9IGfsqLhJCWbD0FFa8V7OD-sF3H10AY8fcYa71fovODoMB0L1nS4we1IQzDi8BLLLoaVNqaWkyNC_9NpRlMGUVJwrdbODt7jpjaeNfPHlRK1GWwnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZYlmXlBehBM--KL7M0bHSEDD2DAIUihQFnT4sqkrUR6mCrYSJNNLR8DykhHAC_iqfsNfxlie8hmTutKDTtFcpiS53p--uIt3QkaTjXA5AlTi_92OuLrB1A1uVL6Xv3DsXeC-iDgTcQs7Bbo3D5eZJba5l_NVvsmLdBwMSV9dvrly3ASkYVRrlUYtFG4xZdRFREzHQTjqFATq42gnj_5EWjasreSEEAP22_V-A8fNZpRAnOriJHv1xFCo766rNw4wW7Zm5b2IvHh-ZiObNd-zXfZS7M--k839aq35RDFIC0_sz4mqvFbPJJrNzjLr3kjBwsSUJuA6I5ePSZgBLcbMVg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=gR9ZS7j72E6oM5odSZaR3JrwtlMsU13G3uhoMKrew4SWWOjH_NfUp0U15P-8k38_gqcAVPYsHMZD9uGslQE6z-0mzj_xqf-S1Eb2CDEUbYafh2hdDYgCbpJf62bU1G6Z-PgFBiOVlBWxCYTpmYw04tIhUtCfmb4UzlDesnx0aI0IFa3_theTVUvaemhgUMLB2MMfotMatgPE_JoY8rqNYJfU8dKi5Midl5zyZ63i1--pyW_zIcQhIvtz-_EGmIflA9X4kRqDiao3tou2FjpYZKdha0kxinwsE5cEAzEALyMiGnrVAqNJSiy1zlZGVmCwhgryLX_9GCzgvpdZ0Q3uKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=gR9ZS7j72E6oM5odSZaR3JrwtlMsU13G3uhoMKrew4SWWOjH_NfUp0U15P-8k38_gqcAVPYsHMZD9uGslQE6z-0mzj_xqf-S1Eb2CDEUbYafh2hdDYgCbpJf62bU1G6Z-PgFBiOVlBWxCYTpmYw04tIhUtCfmb4UzlDesnx0aI0IFa3_theTVUvaemhgUMLB2MMfotMatgPE_JoY8rqNYJfU8dKi5Midl5zyZ63i1--pyW_zIcQhIvtz-_EGmIflA9X4kRqDiao3tou2FjpYZKdha0kxinwsE5cEAzEALyMiGnrVAqNJSiy1zlZGVmCwhgryLX_9GCzgvpdZ0Q3uKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IV5adbFSqYGLXFS-tGnKqfeZmtqr6yXiwe4VG9BuhHnb4cCRWVyZFptdeoWQaQzoNhwSgoWe12Sqi-z9udJx0k5mmfOSllyF3DK-z48po_jcLS_pVH53ao_abY3Hsnl_RWrazTDMmOWh7C8zEIl16CGQTt4Cgk1cZqMl72pvGBmPf2glpkb6CFfkHLg-yNT_vDr7m3PA55XpuBuh6H3R_LDOqdFk7Fatp6gaqK5mY1QaKGJVFXcZ_EFAm2XEnTJll-IoHGPdkapvr5iqN6Fky6BjbqZNksMHQfKaQSHcNGGrmyLfbjw3nzdaKI1JS5yjPvEgazabe8_hwt3Ui0cl5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NzwRMTdxG5IC-Z0rG0b3pjACyC5J8wqNaQzTms_rDV-LoPnlkfhbNlzryZQO5IkShKKA7yaZYkFDLs0vUxCunAg3gbaLiwmu9eS1vhSuDIzRWmjmQG8WqL2I4cpi-uxIka6fEed39JBgqGLXEfE_eVoqbS0zIvUsee85Kuz3UhfEa455oTTycwuM_pEgNLkGaN33qst4mn2qsSxfV65mPdB4l7gDQ_l4itysfpTm6nzkODXdg7-Di-7SPJR8Tus6q03M_Q6kKvj5vf_mPpiYUXFhgZVK0JzoneptRBo03QOCPamySCtPQ8Kno0tzlq3u_TxZuKjO_FYG9DLn9n1l5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YjQLGwq3MI2mDbr_Xso4JJEpvOjVxbVH98KxSjE5PWVfEiCgDoOjPlGsOcsmTH9GibOm4QpX77NV5hv1mzuXHQs0yj-FuxEl7NjAHYpU-SwHPI6ZRm3Nf6M9IVDSRe0L8RCHBzbo1pA657Xjz7Kvmyf7biGbfO_IkWKvlwkyv-3P7HtEjv_K3tiNbFDyNGBExFDgHSBKpW27_XmJNyAmRthCUfMjBopOPKf4GSDRe3qdC7Uo8Z9_Bqa57gFZhid68RimIIYLpk-3HSq8mq5RVae2TGS31VfyBeRQSmZabTKP01j_NhRTJa1QL23lQYoykjGgSqKFkdyjQDAkTZFCbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VfX2KGBY7OV1n_kgycZAt8xMWdsCTRhWct4SPcb4aSQCHnDdOwtIosCeCSDf4z0tD0nEu066IS7q-unK1n3DbfhFDkfcRVgUdNkmQlYULVYy04dEKQ37MwnLHSwNmIWqqFG0YUrfP8qfRoV_DeykW_ESVP7q8e1fUNhLlrVekQx2P-3FWXS9QAUuSX-fGVfUO4dhvo-wl7TNGeXzqlPhTgxjRGV00Lpn90N4yjtulxTc3DRf6G8-9YQ6MJC_IPsgwQ-5ZpnGkp6Vfr4xWpPVXjlA7oyp1B59rsUo8RU8CJKSUBzaEuYuU9VoTckt8vykTzZIEI58490rkqLCqiUuNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rKIfGDujYJL94ZtcRVTQhlUMvE_oQoEZ4p0l-wA1z8jIu0qghAVo3W9TEyqV5vIIrMeGNM0AkFaPAtZbtADB_LH3pYU48GLMvzPyofYebfKLoGMLXDQ6CmgGk6x4BlGWCWOWyPhpxacWqkqmsI19Q-KYCNEayymB1Km0E7-Jiu0LZdcrnye5vBagGdRh58jQnpqgSudJoq5HZ4C5Ja91XwjJWE-TNdEbmweZL3beg6xFG4TDYlvR6kH9AilUZucHPuV-5Jje3ZphS0b7xgoWRrCmAj_N6xOKFC4SevNbk11RFVNEo8xTbsC_nYR0N7McwfQWH_N-UfDeY0FROSYgWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BmqpzYhzn_u31uC34Ch7Bxd1FE3dlRZqgZ06mO2eX9BaHCWhmhW82QNlfm-1aBPrc0XQqyxLgKplsaSa0VVqcHyD4H_nohk05NtPf3XYBFIQiqbYk5gE27jY69XA7yUjm5Su4WmTU0Xx8FGLzBkDN4027HwFC9HR1CGWGSFBLCEPBakDwJcA_KNWqSu-RAvasgOwyqi8AF5iWeVu_koI6W5Y_W3p702ib0sMLZXrbd8P9pvFUkWJ9vt-EFK47nmKfjhB6cWpt37ZacSh-sprOVjxqlRGB2Xq3BOvMPRdCfHpATT3RX2kiFa4akeLY7w6Mlc8GkerwY4aP5n2jXYp1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n1Mnm_ARXzTPxhG-0MWBovubANttECEgIWKNbwuNdNXlZeaHu4Q-o2Feh7lr5jaOQsW3OAI74PVmiTiNB8xRZKMsUiLy8Grk3XB_EAHwTxO0zi_KFv5pcssPB0Y8Oc6rxWG5954NqIVu-F2XEJ6WLPVtl4vPQjdbycyEAT6SwSxQkPDSuyF5K0l2gwYZl6tOMYvxCc3Up71eSOgrEkYhjDV-c1Cyj0OcueASTYvZYsmY0P2qBAk7JSumuo-utXYZtJbfAPvuqfdjXQd6iWyX8Br7WrHZYdSR0LscqNbtJKj_1fuKlYCy0MYF81Wr7BMLAV4RqVgUOCVo4SU7TVleXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kbcvL36TclqKn1W1LCddQfbTAkEKdr2z2ekqqslaY2JWW5hCuz5NApZrKldsifxkkzNgyT3nr1K1dTIT9Do0BXQBdUbkFFW0DXI2ZC724VP1sGJrvGqaGeqBBLH-v0EROmD0cmZyO0GV1WMQxJRUD-tIj-PkyTgCzioQRM05lexun6ArvUNoFXHg5OxDGiZ1DPcv2WxWKAxM5p8XQxwfp393T9Hv-pYZ-8auDGAKyH98OROnSz0ia6eTQ-W8HkyWmfPSMcWHY-l1UvhtmAGjY-Yla1e02KMeTQcFU4nx1KuE5Z01HjtWsud4z1otRiHR671EDt3ISLCkWDkAgZR_3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uKh4IMJiR7QkBXCKmIZ4f8tvVwk0X9s8r-bs1KdXzCAh0QzlkCfV8OlouLXmAQ0QafoaRIV17msfJqZIaR29GatHJGBNEUYyZ_s6X0JJYINF4snLA33K_ir7SJ_lZ0HYDy5sgNC7WNpQwl1723ho6112KEe0O5xihPujRqGVC-9C853yTc735x3hh2gjR8a4jdWhVOuHtYdcyl-xMdfRsitP133Io8Mw70IM9JlRZKO0nT5EZBdGEtBpq3YflW8DR19s3ksIqJo7sjKePE8BnsydrlYuIaJsYi5FrfIX3W6v10NrFS4c_emFywBl4V7a5g6hKbKkRtToLiiy_xBZPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v2N4U77xNnd8gmRhFDFcj7yGHy39M3-dg8odxB-uRGK_d5R0RO0XI8vs7v_eizB38DKvwYUUe67xdOnMVOrowenbVW8s0yB_8Af57aq-U6bln7vfJLAmMn5qk7YLRd3Duylb0M7yS40cTjHaaaDesmjegx1f4U4gXuX2Nz6SKF4mLv9hV5JOmD-NBB8lLB65uUkCs3BAYuZ6x22x49suF1yjHeHHRM-TYK1wBEdqvzMvZL9ZM7RXrNisQM81lNLSphLn1DWlUBXnujC2Vf5qAclkEpLXBdX5QhkKm9WjtIvQm5c51JSdxJp9SHstKc20ADlYVt7g6OrBKAu2h2N2xQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S1amNTg78xodRzHpvy2CgW866JW_ZwKfs38bShFbCRKnQ15Qqvznk9SCYvRUzDRAUPGw13V3TJTl1IktZrOJLUYxiq9ZyAZJhb59-DJdqXgD9xI3HPEDAxqBXjrhrei-yJKDTRLXNExd_ZOUI1BEGxm5ryceTWC6JyGyjVEFiQlSGe44zB-fGOUElNOpKRlJ__aaRDdfCm_RCgLVZbfC2jVOLZgkG_zooa8EpXyQpLCRdRRfLakWP9sxSZCvKdkhJFOYbwZimuVlahMB0K0j2H-YKZEMzTv39TfgH8xVDQ8JJAFETVMraGlGC9KNB3__W67q8vi9vD_1ziNEPpol_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jQ2CwN0GCKOZhihZBFPxbw52m3uSh0Siu8eM3NiyLsoUka-9gOtxv_cDNudCwlK0CRxPgLRj0dOn0uLaEgd7M4rqrEV3tWpTmKBEu-OJv05Ts31cxUwzxtgSRUP0UcTM6M9Oyz1E5FTnRpJY8mwr_knXbmw_qOSiZrS2-SpsZfzJDh4XICno799PcT3C2fqmyyjJGCK_2ueoIgJC4vSK_OSuZgHA2_fVo6tyuWUlxzRJHIdxqjTzcyBJtihGcfwXGwMm53kTsDIFLgQbkRWWLtrd1Sn6Qx9gtYyfHu63tBgrgtJVoj-tm40_z49rKw1f5N1FYMEaq8NpgB1J7fXUNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gFc_KlPXe7hIjwkA-DbXYiuNdUzsEWXtiFSScrjurTBnAdOE9mYqhVXjMiOTOfZRoQOV0eAh9tOww42r5BVVd4AafAsHtiChh0Kb5ZCEp4__wgIhnFCA1HONF2AsDgsfaNRCcLwmteohqiH20oqhfwkq3rAcBPohm2b9hThIbr3SMwEomM_LmNZ0TgUXYAESRQB_S66LeKIWGITH7fFeki1CJxUh7kunuU7VDnLiMdmPU1EfwhANlB6S9JQe_aWfVwLgw2phFkRltX_TytJ0r8PV5glm41-iYWDIGe-gopc_9jMDBwRNnpVyw2HW6yni7T4XOjVOVDhqQTnu6Jd70Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EZAe4j0rOIqpZqJV8a353RlQagO20b9Lu3jttC1smAs5prmKN8aPaNOArBUVpWGOit1Ck9gQ9_yzvX5lgprher3V6xANsnz4jpaaPBmMxEtBGMGVeBUfk4aSD_2m3Edjg50aOZ0FV22merc6PNJ1Z1mrThTz2O9NmoFmJpeJqq1dscoIcY-u-e5W0xduRNmLM3SE5QNS6W1G3jyoR4EC5tIHgxBj1LfzhoCP07Lt8Jf2DgryOzaV57gV1WCt7crOv2bd8PfHjVaO1P-lgjQX_t54slks7VWEhRWo-GLnjzICewvDWq5kIbJStZrdgxOPqVKw2Lg0kXQl4nyIj7JTog.jpg" alt="photo" loading="lazy"/></div>
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
