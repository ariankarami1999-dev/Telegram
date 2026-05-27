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
<img src="https://cdn4.telesco.pe/file/ANBPQI3NpKaHMoTuHF3b3QXmfnev-66ZrvmKGFfkJuXOTrvRTHHbMNUIM9O3tUq0vSRj1sZqwvgS9Pac8KV7zAe2OOG2OOw9aI8DJSDZoGTDzDhQP0UiebIPb1ehfET260qoPzn_NsbPikbe7HwNCb6SDwoYTpUvmbmEyyqELZb3ycCHThKHOniIi-8oQB3l3IAfMlHGwlo6H5HD4qf-64YnRda2aJzoDpuV7HtGaoeCVhrge7IB2YpwDaRZtOnmjvK8Mxrg3c29vap-baRStuN-QmKjPsMMqUV6ITi9sg_Tph1g51Ea9jXvDt_gHLkM_pUqVpcYbOoo5EqQ16nZUw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 8.59K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 23:32:33</div>
<hr>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گوگل پلی رفع فیلتر شده..</div>
<div class="tg-footer">👁️ 147 · <a href="https://t.me/archivetell/5635" target="_blank">📅 23:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ربات جدید تبدیل لینک به فایل
@url_uploder_nrbot
@ArchiveTell</div>
<div class="tg-footer">👁️ 213 · <a href="https://t.me/archivetell/5634" target="_blank">📅 23:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12fb4063f0.mp4?token=CMkZ8flfpzilHY6XkC_dzBR13tpa-SOnunTeTO36qD2kTSQVVW8kjwupnTxU5X37oF6K1N2p5CkyrT_N5ZMK_ELYbQ28lROCPpt5Rvk0zYojgu_I-1tir7baQ03x0t5zpIEqUhFRFZcQ31A5k48MyXDLJoS_52FkROTcVZpPaz5JgTb9dSWOpZC1w0ohxa0IHlXLZ7jkL71zjxWjFEVJYTS02tCQ59I-KhJ76xwXonE9mA3MYJHPYTVCfkuHDfh7HLrWSR7XM3nVvqj6xrJyOqItBYUDdj-5IGJiEij0rnMjtRLeO7k8H3DmZ8NHH8U80cctUfwOAzN0nfj-5oQf7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12fb4063f0.mp4?token=CMkZ8flfpzilHY6XkC_dzBR13tpa-SOnunTeTO36qD2kTSQVVW8kjwupnTxU5X37oF6K1N2p5CkyrT_N5ZMK_ELYbQ28lROCPpt5Rvk0zYojgu_I-1tir7baQ03x0t5zpIEqUhFRFZcQ31A5k48MyXDLJoS_52FkROTcVZpPaz5JgTb9dSWOpZC1w0ohxa0IHlXLZ7jkL71zjxWjFEVJYTS02tCQ59I-KhJ76xwXonE9mA3MYJHPYTVCfkuHDfh7HLrWSR7XM3nVvqj6xrJyOqItBYUDdj-5IGJiEij0rnMjtRLeO7k8H3DmZ8NHH8U80cctUfwOAzN0nfj-5oQf7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک مجموعه برتر از انیمیشن‌های رابط کاربری وب برای طراحان رابط کاربری که تمایلی به صرف زمان در ایجاد انیمیشن‌ها از پایه ندارند
https://transitions.dev/
این مجموعه شامل انیمیشن‌های آماده‌ای برای کارت‌ها، منوها، فهرست‌ها و کلیدهای تغییر وضعیت می‌باشد.
امکان بررسی مستقیم انیمیشن‌ها در وب‌سایت پیش از بهره‌برداری فراهم است.
ادغام در پروژه‌های فرانت‌اند واقعی به سادگی امکان‌پذیر است.
پشتیبانی از ادغام به عنوان یک قابلیت برای عوامل هوش مصنوعی ارائه می‌گردد.
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/archivetell/5633" target="_blank">📅 22:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/121da40c06.mp4?token=m1Cpflt1wiPRKXjYdWkN_AvnhWEalQ_fszKFgnOiZ6CoKY_-Iv3tu-IUgiQyjaVvxdAjyISJYq6NAeDxTQOGmRGlGff0tMH4vu8x00Ty4lDgKBHlYqjD1yMlR_vJ_fv6q6pRfrvmXrs7RjiDNmOxtrwlTKkKJT5yFIStbckvqNoKtZ1i1B2MRPhkZ-G0fp4uou3y0nO_A8GXakUrqp4ZDTYRP7rIecdvWuk56B7Fwe74OojsqYvFp5eVz8qCdfHXLDznkVBri1FOQClwTj6b7N5m62gh_0uIOowAPd8j2hetZHYi9SWG5xBrsfPJ6X_cRxfvvlGu4-82UnDsR5U01g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/121da40c06.mp4?token=m1Cpflt1wiPRKXjYdWkN_AvnhWEalQ_fszKFgnOiZ6CoKY_-Iv3tu-IUgiQyjaVvxdAjyISJYq6NAeDxTQOGmRGlGff0tMH4vu8x00Ty4lDgKBHlYqjD1yMlR_vJ_fv6q6pRfrvmXrs7RjiDNmOxtrwlTKkKJT5yFIStbckvqNoKtZ1i1B2MRPhkZ-G0fp4uou3y0nO_A8GXakUrqp4ZDTYRP7rIecdvWuk56B7Fwe74OojsqYvFp5eVz8qCdfHXLDznkVBri1FOQClwTj6b7N5m62gh_0uIOowAPd8j2hetZHYi9SWG5xBrsfPJ6X_cRxfvvlGu4-82UnDsR5U01g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎹
سونو را دور می‌اندازیم — ElevenLabs نسخه Music V2 را عرضه کرده است. توسعه‌دهندگان این را بزرگ‌ترین به‌روزرسانی شبکه عصبی موسیقی تا به امروز می‌نامند.
https://elevenlabs.io/music
🕤
تولید ووکال، ابزارها و آرنجمنت‌ها در همه ژانرها به طور قابل توجهی قدرتمندتر شده است.
🕤
سبک آهنگ را می‌توان در حین پخش تغییر داد.
🕤
هر بخش از آهنگ به طور جداگانه ویرایش می‌شود — ثانیه مورد نظر را انتخاب کرده و فقط آن را بازتولید می‌کنید.
🕤
پشتیبانی از رفرنس‌ها: می‌توانید صدا، متن، ژانر یا پرامپت معمولی بارگذاری کنید.
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/archivetell/5632" target="_blank">📅 22:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کانفیگ پرسرعت
ایپی استاتیک کره شمالی
جهت سفارش پی‌وی
🐱</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/5631" target="_blank">📅 20:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شما می‌توانید Llama 4، Qwen3، Gemma 4 را اجرا کنید — همه رایگان، همه خصوصی، روی لپ‌تاپ خودتان.
🖥️
⚡
این همان Ollama است.
🔗
ollama.com
این یک ابزار رایگان است که به شما اجازه می‌دهد مدل‌های قدرتمند هوش مصنوعی متن‌باز را به صورت محلی اجرا کنید — بدون نیاز به اینترنت، بدون هزینه API، بدون خروج داده‌ها از دستگاه شما.
فقط دانلود کنید، یک مدل بکشید و شروع به گفتگو کنید.
چرا مردم واقعاً از آن استفاده می‌کنند:
→ بدون هزینه‌های ابری
→ کاملاً خصوصی — داده‌های شما هرگز از دستگاهتان خارج نمی‌شود
→ به صورت آفلاین کار می‌کند
→ مدل‌هایی مانند DeepSeek-R1، Llama 4، Qwen3، Gemma 4 را اجرا می‌کند
نسخه ۲۰۲۶ اکنون شامل یک رابط کاربری دسکتاپ داخلی، شتاب‌دهی Apple Silicon از طریق MLX، و پشتیبانی ابری برای مدل‌های بزرگ‌تر است — همه در یک رابط کاربری تمیز.
اگر برای اشتراک‌های هوش مصنوعی هزینه می‌پردازید و هیچ کار حساسی با داده‌هایتان انجام نمی‌دهید... Ollama ارزش ۱۰ دقیقه وقت شما را دارد.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/5630" target="_blank">📅 20:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🎁
دریافت یک سال اشتراک پرمیوم RoboForm (رایگان)
---
رفقا سلام!
✋
یه آفر فوق‌العاده و محدود داریم. پسورد منیجرِ معروف، امن و پرطرفدار
RoboForm
، به کاربراش
۱۲ ماه اشتراک پرمیوم کاملاً رایگان
(به ارزش حدود ۳۰ دلار) میده.
اگر هنوز از یه ابزار مدیریت پسورد خوب برای ذخیره امنِ رمزها، قابلیت اتوفیل (Autofill) و همگام‌سازی بین گوشی و لپ‌تاپ استفاده نمی‌کنید، الان بهترین فرصته.
💻
مراحل دریافت اشتراک:
۱. وارد لینکِ آفر در پایین پست بشید.
۲. ایمیل خودتون رو وارد کنید و روی دکمه
Redeem Offer
کلیک کنید.
۳. مراحل ثبت‌نام و فعال‌سازی اکانت رو انجام بدید.
✅
تمام! اشتراک یک‌ساله پرمیوم به صورت خودکار روی اکانتتون فعال میشه.
⚠️
نکات مهم این آفر:
-
💳
بدون نیاز به کردیت کارت:
برای فعال‌سازی اصلاً نیازی به وارد کردن اطلاعات پرداخت یا کارت بانکی نیست.
-
🆕
کاربران جدید:
این آفر فقط برای اکانت‌ها و کاربرانی هست که تا حالا پرمیوم نبودن.
-
⏳
مهلت استفاده:
فقط تا
۳۱ می ۲۰۲۶
(۱۱ خرداد ۱۴۰۵) فرصت دارید این آفر رو دریافت کنید.
🔗
لینک دریافت آفر ویژه روبوفروم:
🌐
https://www.roboform.com/lp?frm=offer-ga
📌
#آفر
#رایگان
#RoboForm
#پسورد_منیجر
#امنیت
#پرمیوم
#کاربردی
#تخفیف
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/5629" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">600 گیگ کانفیگ مستقیم متصل همه نتا
اهدایی یکی از ممبرای عزیز
❤️
vless://22768339-9096-48aa-9109-ff28141145b9@roz2r.skystreamgame.com:8443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=QHkXBS2ENHV0khgY9VBYi8_9bpfqnUYDcfQN4cW5Qg0&security=reality&sid=4326&sni=roz2r.skystreamgame.com&type=tcp#Aqa.rza
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/5628" target="_blank">📅 19:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">kiro.dev
یک ابزار کدنویسی هوش مصنوعی از AWS که فقط کد نمی‌نویسد.
این ابزار کل پروژه شما را از صفر برنامه‌ریزی، طراحی و می‌سازد.
⚡
Free trial with 500 credits
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/5627" target="_blank">📅 19:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آیپی تمیز کلودفلر، تست شده روی ایرانسل 104.16.81.122 104.16.81.43 104.16.81.86 104.16.81.12 104.16.81.24 104.16.81.125 104.16.81.40 104.16.81.133 104.16.81.68 104.16.81.101 104.16.81.23 104.16.81.155 104.16.81.112 104.16.81.106 104.16.81.67 104.16.81.82 104.16.81.157…</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/5625" target="_blank">📅 18:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">Defyx VPN  رایتل سرعت بالا  https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/5624" target="_blank">📅 18:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آیپی تمیز کلودفلر، تست شده روی ایرانسل
104.16.81.122
104.16.81.43
104.16.81.86
104.16.81.12
104.16.81.24
104.16.81.125
104.16.81.40
104.16.81.133
104.16.81.68
104.16.81.101
104.16.81.23
104.16.81.155
104.16.81.112
104.16.81.106
104.16.81.67
104.16.81.82
104.16.81.157
104.16.81.6
104.16.81.1
104.16.81.110
104.16.81.72
104.16.81.10
104.16.81.16
104.16.81.126
104.16.81.75
104.16.81.53
104.16.81.134
104.16.81.119
104.16.81.156
104.16.81.2
104.16.81.91
104.16.81.45
104.16.81.21
104.16.81.77
104.16.81.73
104.16.81.66
104.16.81.19
104.16.81.32
104.16.81.88
104.16.81.132
104.16.81.74
104.16.81.8
104.16.81.18
104.16.81.121
104.16.81.48
104.16.81.145
104.16.81.51
104.16.81.13
104.16.81.104
104.16.81.80
104.16.81.42
104.16.81.144
104.16.81.111
104.16.81.105
104.16.81.118
104.16.81.117
104.16.81.26
104.16.81.78
104.16.81.159
104.16.81.57
104.16.81.25
104.16.81.60
104.16.81.54
104.16.81.149
104.16.81.136
104.16.81.97
104.16.81.38
104.16.81.90
104.16.81.137
104.16.81.140
104.16.81.59
104.16.81.22
104.16.81.41
104.16.81.150
104.16.81.64
104.16.81.31
104.16.81.33
104.16.81.61
104.16.81.76
104.16.81.69
104.16.81.46
104.16.81.49
104.16.81.35
104.16.81.50
104.16.81.79
104.16.81.34
104.16.81.93
104.16.81.102
104.16.81.129
104.16.81.71
104.16.81.115
104.16.81.92
104.16.81.5
104.16.81.99
104.16.81.84
104.16.81.130
104.16.81.128
104.16.81.47
104.16.81.36
104.16.81.96
104.16.81.9
104.16.81.37
104.16.81.4
104.16.81.124
104.16.81.58
104.16.81.52
104.16.81.55
104.16.81.113
104.16.81.44
104.16.81.65
104.16.81.138
104.16.81.95
104.16.81.29
104.16.81.135
104.16.81.56
104.16.81.108
104.16.81.103</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/5623" target="_blank">📅 18:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
مدل بعدی Grok از xAI ممکن است ظرف ۲ تا ۳ هفته آینده عرضه شود
👀
⚡
گزارش‌ها حاکی از آن است که مدل جدید ممکن است از مدل پایه بسیار بزرگ‌تر ۱.۵ تریلیون پارامتری V9-Medium استفاده کند که جهش عظیمی نسبت به معماری ۰.۵ تریلیون پارامتری V8-Small در Grok 4.3 است.
جزئیات جالب دیگر:
گفته می‌شود داده‌های کدنویسی Cursor برای آموزش اضافی استفاده می‌شود.
Grok5؟
👀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/5622" target="_blank">📅 18:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">#اختصاصی
🌐
دامنه‌های رایگان برای هر پروژه‌ای
https://github.com/DigitalPlatDev/FreeDomain
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/5621" target="_blank">📅 18:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbhU-NQ1BvMlTp90Bb-WruJk61MTXMIihvDMHUfggEsiOlkUwAUCQ-tpW91PqPqFsNAx1P0W2419dMouxlZRAZuYDh1zqSct62fvW0MvorVfe3yyT4Jk-APLBb1_1cY0EXa7NQqiKwnNfytB3vFgu-FOBDv4fWPhZw03yXl_Uc0cnOk5l4-kLrywNXjF32AtS7KNv-lzkILGfsVm_enkNliq_8ztwBjbL__BHRyP8W13oRzS1p7U2FTJM4wIw8ijKGFyxqDC12msq9o-yDyUiOO4KcRmzo1bD22WZsDlak1N5VTQG2TvCU1QKTZoJQk-1fHzfIs8BUqcitrg5ET1mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Defyx VPN  رایتل سرعت بالا  https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/5620" target="_blank">📅 17:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">Defyx VPN
رایتل سرعت بالا
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/archivetell/5619" target="_blank">📅 17:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5618">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">configs.txt</div>
  <div class="tg-doc-extra">195.4 KB</div>
</div>
<a href="https://t.me/archivetell/5618" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دوستان میتونین با Hiddify روی سرور های رایگانش وصل بشید یا از گیت هاب بگردین دنبال ساب بندازین داخلش
👋
**میتونین داخل Github هم بگردین ساب های مختلف و وارد اپ کنین و تست بگیرید
👍
لینک دانلود داخلی Hiddify
👋
💀
@archivetell</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/archivetell/5618" target="_blank">📅 16:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5617">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHNXIogQ-RwYhmGHIO3Owr8kZkE4Cbg2iUYghEsKeM9-IqEwQFAtDWoIWbH7B2M_h2YEZcnJWdagkX65Ke6bxpdQFLj-7khlaMBoRETvsYfbRFwqxiF2DlxnKnjlKGw91bJXuz54bGzLSaY2ogt7ZZ4ex6hC9qOs5xfD8JlnoaRaWQrUz2zxS7xElYvfdXplN_eLtf5M3wt2ea1bnQ36Pc-LxmzsXJxodXHty2TcV_V9J9UqQIJib2JWsWFy5ZMDOEgrbYq_2b-Vgze4xN73HkSx7BOACbMPlX7TzAH-KMk6WG3hWifG4ZS9cIITwzoSmFuiGLW9PhbdneDa51IfvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان میتونین با Hiddify روی سرور های رایگانش وصل بشید یا از گیت هاب بگردین دنبال ساب بندازین داخلش
👋
**میتونین داخل Github هم بگردین ساب های مختلف و وارد اپ کنین و تست بگیرید
👍
لینک دانلود داخلی Hiddify
👋
💀
@archivetell</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/archivetell/5617" target="_blank">📅 16:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مقایسه سرور ها و خرید سرور مناسب و اقتصادی
جهت راه اندازی کانفیگ
https://t.me/archivetell/5282
https://t.me/archivetell/5308
https://t.me/archivetell/5309
https://t.me/archivetell/5310</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/archivetell/5616" target="_blank">📅 15:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2g9VQZ3kZuMPhZPIrFMs0tmpiHZQ9g-HHuq677PeH0FxEUQeO--Ry-lOMWWeVrgHPLC1yYKO-wVg2KmrzEzw4UZKmWlXs6CtIokyusRq94RCYbjmKVlxEnGLEVsH5RlJpQHGAVca3ROY-WB7QDEVyAbqCrpMdI2743CcoJKv8gEwLpYkpOvwIZNiiZUTxHcbY6eEZm5kyQnpa3mNXq6SRzO4S9NXajyBXcKxdbDMZVoWjRw2qNsXbiXYWGGvJ0W4vTEyGC3PQs3Ofwc17bi9RholKLA1NAVDUFECLpydiHSiRQjlZis3mj_xfYmPYYhtdSisocbMQoaqjqK3eBavg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">162.159.192.1
162.159.193.3
162.159.195.1
برای وارپ وایرگارد با این آیپی وصل شدم.
پینگ می ده، لوکیش ایران می زنه
😂
ولی تلگرامم الا بالاس دارم باهاش پیام می دم.</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/archivetell/5615" target="_blank">📅 13:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">در کل این اپلیکیشن D-Tools خیلی خوبه ولی حیف توسعه داده نمی شه، وگرنه یه اسکنر Google CDN و Cloudflare CDN و Fastly CDN می‌آورد خیلی خوب می شد.</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/archivetell/5613" target="_blank">📅 13:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">در کل این اپلیکیشن D-Tools خیلی خوبه ولی حیف توسعه داده نمی شه، وگرنه یه اسکنر Google CDN و Cloudflare CDN و Fastly CDN می‌آورد خیلی خوب می شد.</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/archivetell/5612" target="_blank">📅 13:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNR_habm1QWntQKkU2-EnmdnFUI6qCwPhrAuhXVTXIx0pS3WgmhHO1hPdvvc4scC3rA5w8awIKu8ty31yJiOIKZbS68gIEXH94mjDqmCKjXDziSxFfT5viPPi9OLzvrDocUlDUct2QLk7TqvuSFaPuFV-opYIfQ7YGYT5FdFXzEJNWj5FTCbQe0SEYw_ahnWalfzb9cjLO7PseN9kVz9Hh986RgktJoSxPG7skw9XOGn5OrpYPs9Puq-yogAVC98k59Vm3UR6NZr2Xbq7rM8NOxNknTuEZRdgVe4uNA6O0wDmP9eUvji_ccHVJ6rIY6IxY5FqVFe3Y3GrR9qCdbIFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ساختن وارپ به این نیاز نیستا.  کانتریبیوتر v2ray، یک ریپو داره به اسم D-Tools. اپلیکیشن از پلی استور حذف شده ولی توی اینترنت پیدا می شه به شکل xapk. بدون سرور مجازی براتون کانفیگ warp می سازه.  {   "local_address": [     "172.16.0.2/32",     "2606:47…</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/archivetell/5611" target="_blank">📅 13:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">D-Tools_0.0.6_apkcombo.com.xapk</div>
  <div class="tg-doc-extra">31.7 MB</div>
</div>
<a href="https://t.me/archivetell/5610" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اینم فایل اپلیکیشنش.
😊
@archivetell</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/archivetell/5610" target="_blank">📅 13:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gv4v0gm2JmbOKrsX7Eq24e-OAY4dqzJaZsLgr8d8bjQMoICL-IzFy186N73zduxre246kieY0psjUUeCsTlktrA2U_gkKBay4Lrl6glfj62z0yCgdUEWiJC7WNzUnxnrmrQnA77tevVWOdzYz3HVj430oXYmOHTBatHZaWJF50xA7NrJVhIpzXtgwkjESQiCaeyJqzFTUoLnynQzjXZJXnTPDWpy6_QIS4-864oAQp8n40HEnmQvtrB1V6G8S6rEYa3dmm9RVBpqftRc-Ld97inKZJAGAzIQTGggY0953fvpHa0KszaN2uXAZfBoPtjfcgPO3fAYfPmfEp1FneUJCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش ساخت کانفیگ وارپ (نیاز به سرور مجازی )  با استفاده از الگوهای زیر، کانفیگ اختصاصی خودتون رو بسازید :  کانفیگ‌های خام:  warp://licence@ip:port/?ifp=40-80&ifps=50-100&ifpd=2-4&ifpm=m4  warp://licences@ip:port/?ifp=30-60&ifps=50-100&ifpd=3-6&ifpm=m6 برای…</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/archivetell/5608" target="_blank">📅 13:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🌐
بات تست رایگان بدون رفرال (خرید نزنید)
@Cheap_v2ray_bot</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/5607" target="_blank">📅 13:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آموزش ساخت کانفیگ وارپ (نیاز به سرور مجازی )
با استفاده از الگوهای زیر، کانفیگ اختصاصی خودتون رو بسازید :
کانفیگ‌های خام:
warp://licence@ip:port/?ifp=40-80&ifps=50-100&ifpd=2-4&ifpm=m4
warp://licences@ip:port/?ifp=30-60&ifps=50-100&ifpd=3-6&ifpm=m6
برای استخراج لایسنس، آی‌پی و پورت مورد نیاز، اسکریپت زیر رو اجرا و مقادیر رو در الگو جایگذاری کنید:
اسکریپت استخراج:
bash <(curl -fsSL https://raw.githubusercontent.com/Ptechgithub/warp/main/endip/install.sh)
☑️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/archivetell/5606" target="_blank">📅 12:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">همراه اول
Windscribe UDP 443 Censorship On Dallas BBQ
@ArchiveTell</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/archivetell/5605" target="_blank">📅 12:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کسایی که سرور دارن.
اینباند:
Vless+xhttp+tls+Cloudflare clean ip
بزنین با آی‌پی تمیز کلادفلیر
عالی وصله‌
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/archivetell/5604" target="_blank">📅 12:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">همراه اول
Windscribe UDP 443 Censorship On Atlanta Peachtree
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/archivetell/5603" target="_blank">📅 12:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">و اینکه، نرم افزار Karing گزینه وارپش کار می کنه و پینگ داره و کار می‌کنه.
😊
@archivetell</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/archivetell/5602" target="_blank">📅 12:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">واقعا باورم نمی شه مردم چقدر می تونن عقده ای بشن.
📘
مگه ما فروشنده ها چیکارتون کردیم؟
😭
طرف با کانفیگ رایگان بعد ۹۰ روز وصل شده زنگ می زنه مسخره کنه. چه رویی دارین خدایی.
حالا من به وصل شدنشون می گم وصل، طرف فقط می تونه با کانفیگش پینگ بگیره
🤡
😊
@archivetell</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/archivetell/5601" target="_blank">📅 12:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">لینک داخلی
Am tunnle
(pro)
Am tunnle
(lite)
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/archivetell/5600" target="_blank">📅 11:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">AM TUNNEL
سرور ۱۶ fast dns روی ایرانسل و همراه اول سرعتش خیلی بالاست
https://play.google.com/store/apps/details?id=app.vpn.amtunnelpro
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/archivetell/5598" target="_blank">📅 11:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXwKI9uxebU8aYpLhkylmGS-iccfkslQrfCic-MWmZINp_Fspp0DoGn60_VoZIEQl8qtpp0IlHp4GvpGoavptsUD7dxdh20kGOfLBce3gS24ZLFSqNSfXmjewH1a8Axbvdee6Yd77bmmJ2s36zvW3Jb9f3TPUJ726XEnKGNMCRv4VhI_ipPtDOexcxCAK4-l4lVInc4JpGI6G592iJx3f6OHsu8A3iUpSohPxVP3skHVqBsFlWVuft52qnBihxmq1tK9hg0vgFaHdeoHPGIeNwNI0b-BoABZ9FiRFP1lS4zYvT7DaHaPRl32SFyup2UyIk1FYA1sHZaCOlxkJ8Ao7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Optimize-Windows
اسکریپت‌های بهینه‌سازی و ساده‌سازی نصب ویندوز
https://github.com/ShivamXD6/Optimize-Windows
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/5597" target="_blank">📅 10:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c6MADIUkfXkU-wgy0ziYyQuCoSxZmqjDhNaHdNZ4jwO5W9GqKGgwukgxdKOqLa9nIadyMtKR6vp__1bvxgvK_2ifoSh7vhouo5lLbEZHvlDJNBMYGiKLJ5QYLHSYkLFFXlmWRxajjmbRoBycxahKpbkXaYIymTuXL9v49BenxAuGfI0ytAEzHyV6b0ebERtJ3DGzDfpRiLISdxqxF6SRihJZp-gqnoGY0CCcycVBrN_j3QYIxmbpS6gwoDS4mMhTRrp2uHxRW9kdjgZ6fdawX0ETXwg4wGoMe-eccL5U55pUyAR30P-Ou5fdveejGhSXAQaBxEvKZCv-z_soajmb9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YAi4R6OBKKyFF6OjQAdmk9J2XkUrfBiYzVtjvY4FWjBEOTjZ1fDIG0Zr_xMwTw5MFw5Me-KTqyZXy_6w29RiGLx4cMdYZCLXkVyK0yqCNiZUO0vyCK_lTvsWezNgxoXQg18BBWUcSYIDaAH7aGwivvLGdidXXk6Kb5u0a8TRhTSUjHdvYuzj-uCPegMBwQfqBcaOPMGayCbXnUCLKycsXlVDZfi5DyJKLyCW51sikHfmQ2HANrjti_TQMQngActX8PIdA5rbCDFZP04O1bURf3EsR43EAhWVbOp0KFrjR43F3Xbn3dqcmlYXfmMZRdGdAOnJO5jG2K8MwaOxVc4APQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/esQbtSGPtdUdZ0yhwoMvMBqRrLpsLE-eAovvqJR4vhU-pXjW4DMRQ4DsIo2vqdWyNn2IRve7hYQJ1sCDPUpnuovBK5-VB2DGmU1150UKMH1nq3e_D9_B1wbrOfxuBuqPrcWYRspEaOQYnIAi1DC-J7S_MVedEifda_t3M5J4O7GKOneiL-mQOamu3wcjYJd6TCp24_JkvKu5xs-mt9XtWOyP5AaVDS9HZKnL47dCNcea_cmlgApZprBubj8AlHrkt-eWVvKDlaT-V5h7dOvNPBvekgmGoiAsXtpe5rqrRwN9944Go1hSSQ5nji73AKmBgBQphkbusRTOeJj9IrGxiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L2sBO8oLmFEJdtZHWNNCx5xFBhnpRUL7LBJvjZeDfKQwwZNN4HBfqIIg5W6KKOmn25Kt34m2XSKT2K6tq6jwjOB-5pRUuYPHXPd-4-N-gi-bfSUZuOSerPYegs1Qsg6LLyToIVBZKPqLz15ETSoRqHC7jj4Lc16tMPmz2midjU3ohJA5pj3x1UmaPqyY9BnW3qybw_ELlwtl8mUbVO2MEQsXgqRuY3v7shQ0JsrsUKM7NNSP7iGslcnxYyoXMVIha9RNDXce9Lq8oNR8xfYN3msmG3W3j7rF3kCSezYYDciRuuiWKaaDX1xhozUr_i6J5mZaTC_bsIOWBfvp77UD2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ec6V99WzYsESePl2U0P12ih4fkbu6l7SBp5MxD7Cv9LGsfGsnemJdRgACRwkT6e5yFf_1APnMlD_Xel9EqTQuwOAc5PztprDo4-leOMSgQktuS-Seb3cVzX_7iMD8jOQ72y_U9rKUdFku9ROgbvcjRlKz6fVY1gzcrBTEnQWJVotkcQR5e0pZWvoy30Uq8Ygh4QlkZv8kJfKiH-VfaooMtlNQKfmqqxRzFRI4m13hjDNOxapttJs4yCe14eujfiseYpCYjNKbBxQNjNQStrn0js7gz8hPA6L8AOWs0583uNkaGWWTx1N2EkB6Srw5dAIOKTO6fDP1G95HbAFxSrvRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pyb1HKdsJqiLAhRq8YUEm5jKsdV84AdfxllPZNgQkoChZvvCl2dFnXjLHvrvGL0KKr6HGenqmNd6z7Y9CAWA2o-gVgFI5q3LxvYZwZ0HksMzXz3o8jh4V2wZqJBlmbesV-_EHaeYpnQrVBe4og9fqu-GlVFjm__eBh2pDzGfydrcNMa7FqkD9uf1jSsuA7ZU5y2ZUIYbgR8a03pgIlmtKsV3kURPhwQfLMb0CSllrJluOU2WdwK0QxJsktBtp0c6YhlKw7DMrMhcNrtHxdQAmDWsm9VTrh3iyUmQH1N4DX-RjuTqUlJO-VF6u9EhH1-V7Srm2A7TuXevUUxunqTU6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uc_4i5k9ZsI0NFCk6T7-D-NOQzY3b8AV2AzL7evwzfUoYYCTl771z6aVwT-xKamFkDzkiFIDXNjE2T63IRykomqrU1MdflwiR_RykdXcGIaJsdQMLx7KymkjB3m4g3uVepjwW-25sLEFGV2v_Y4xPaKHXoKFAhbA-D6kVobzpXa9ZbmnTStGaVRfNED12PuWTkCaQJAQ-LzHuACI6ftXD10o8whNsqHRmklB0z4UEHcWO_pYBZJPkesUd9fMQbXMIGmvUeKhpp901xXZEbTgyC4TD0pWw-5KHd22GRDavQQYoBI44NTlpefvuvJQWSi9oYeM4l0W5v_cDe3kDxF9kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ربات دریافت پل تور
@GetBridgesBot
پل webtunnel سامانتل و ایرانسل وصله
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/archivetell/5590" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Invizible_Pro__beta_ver.2.6.9.apk</div>
  <div class="tg-doc-extra">38.1 MB</div>
</div>
<a href="https://t.me/archivetell/5588" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">InviZible Pro beta 2.6.9
* Updated Tor to version 4.9.8.</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/5588" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXz5mNNeFRdCCYA8ump-lxvvYGHMimKQKVlQekB77eMIY-cc0RmNliVQ3KUPt9HtlKsaRkJwFisye-sBrV21c1e4M6RlCiroKhODLB8_2U-HJpTbiQfxjOjXn1k1T-XSF8sdf6oSZBFLLv3LBjnFoJ0fd-6BMp3m-1JpJdE7I3PbbBjeuWLCs7KeKMmgl_93zBgNs3Nk-a8hHoWro0LnEk4-qMkuoWn5uLPrywwEOCAitBHSH63-KbbiQUg7DGKEWiWYbM6qh95fg9Qc_jzB0ogJtSssqeyvAalgDgUoJCJPyjyc0Z2Sm15plGbalQZ8VsS0ABe7KD6tL91gV73rig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش invizible pro به زودی..</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/5587" target="_blank">📅 09:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">MetaMask یا Trust Wallet?
🤔
👇</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/5586" target="_blank">📅 09:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">BD NET VPN
مخابرات، متصل
سرور BCCF 01
@ArchiveTell
https://play.google.com/store/apps/details?id=dastan.prince.bdfreevpn&hl=en-US</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/archivetell/5585" target="_blank">📅 09:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">شیر و خورشید بدون آیپی
مخابرات ، همراه اول و ایرانسل وصله
تنظیمات رو به حالت اولیه برگردون ( کلیر دیتا ) و پروتکل رو بذار رو CDN ، متصل میشی ( کمی صبر نیازه )
﻿
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/archivetell/5584" target="_blank">📅 09:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آیپی تمیز کلودفلر سامانتل
208.103.161.170
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/archivetell/5583" target="_blank">📅 08:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">📱
صد گیگ کانفیگ اوتلاین به همراه شادوساکس بهتون میده
✅
( پروکسی ام میتونین انتخاب کنین )
@OutlineKeysRobot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/archivetell/5582" target="_blank">📅 05:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کلا tor برای وبگردیه فقط، هیچکدوم سرعت خاصی ندارن.  وقتی وصل شدین برین یکم تو این سایت وبگردی کنین
😊
https://tor.taxi/
اونایی که می دونن
🔫
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/archivetell/5578" target="_blank">📅 02:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHey4ydE3ZBBvTx5fIyT4G16iu7gRP1CMjdOQRcOxHcCQv2NGSxw5RwC2KT330PBIy8ivonbETI3KQr4RHxKG477mAHHMmuLx6EuhxYobEK7MBibVDxpVdMVkhEjJ-B-O2z9S6owq4NDBfrEmXpdJjtm7sC-hkDHDfrEeSLIgLszAly9IXEfCFyjyLo1xrGuVGfrfh7XRGrOeKEFz-2uGs4aNfwha7v91vHDSM9WGRVa0c3GCnbivIFjBYe4w4T0ARBX2w_XPEcA84j1_ZCS86xwmSW0EHmRiF2B8Kzv76zo5pXpYFwUaMNvu8orYLA7cgKU20Or9jMvBRz5cE0JIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان کلا از نظر سرعت بخوایم مقایسه کنیم ظاهرا به ترتیب Obfs4/WebTunnel Meek Azure Snowflake اگه اشتباه نکنم</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/archivetell/5577" target="_blank">📅 02:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5576">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">octohide VPN
ایرانسل سرعت عالی
لینک گوگل پلی
از ربات
@octohide_bot
کد ۳ ماهشو بگیرین فعال کنین
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/archivetell/5576" target="_blank">📅 02:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🟢
نسخه جدید Argo VPN (اندروید)
🔺
بخش Network type رو روی Public Network قرار بدید و متصل بشید
اگه ارور داد یکبار برنامه رو ببندید و دوباره وارد بشید
https://dl.toolschi.com/view.php?f=ac33499153243a31.zip
(لینک دانلودداخلی)</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/archivetell/5575" target="_blank">📅 02:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کلا tor برای وبگردیه فقط، هیچکدوم سرعت خاصی ندارن.  وقتی وصل شدین برین یکم تو این سایت وبگردی کنین
😊
https://tor.taxi/
اونایی که می دونن
🔫
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/5574" target="_blank">📅 02:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K70dQGadI28YLguW3RrucG-HhWs1FWtA4RUGqtb96YoJUxDJt6l3ILINXaQKFw3mFdfsHVeS1NIfWqLmpeeJauhtm1-KpZ0dji2NThUCYtgG5BEpDiaPsXvn3eBQkjxov1J6eqL_522Egd5dgaBTdUCMM8uxo9AP6E4gXArFABgy__ZMz6ecAG0zDJCKsmVDswCLDuqadA0wIl0OlmJ0XXDf9xlLD1DMYaK9ylVZrhxZhMjJe5l-nO6QOS8IxbrhWaVakLeYsDRAmwQcBxfXUsUA0VaGFDcfPYg9gZEMSnmYVgq8l_y8LiZc-gdo8iLY-wU6wI6hGQD6i8xsW4Zn5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلا tor برای وبگردیه فقط، هیچکدوم سرعت خاصی ندارن.  وقتی وصل شدین برین یکم تو این سایت وبگردی کنین
😊
https://tor.taxi/
اونایی که می دونن
🔫
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/archivetell/5573" target="_blank">📅 02:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5572">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دوستان کلا از نظر سرعت بخوایم مقایسه کنیم ظاهرا به ترتیب Obfs4/WebTunnel Meek Azure Snowflake اگه اشتباه نکنم</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/archivetell/5572" target="_blank">📅 02:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دوستان کلا از نظر سرعت بخوایم مقایسه کنیم ظاهرا به ترتیب
Obfs4/WebTunnel
Meek Azure
Snowflake
اگه اشتباه نکنم</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/archivetell/5571" target="_blank">📅 00:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5570">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کلاینت های Exclave, SlipNet از ssh پشتیبانی میکنن
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/archivetell/5570" target="_blank">📅 00:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bFwPu58KOc65gGtWRq3IMHfI5xqRREfDPYmOpKTWuKnUdEoFwp64x2nWg6qlDdbGU1b1yKegxuMYIbjSEHp-MupOLWpciCd3P6qU1cWrLSf-d5CLd-bOV9JBGUi9JSKwfnnuAxPHIL2nL343WXAj_NyG-Rty7ghdNqa9l31usd9n8mvmTeB17P8je3dhfMP_PvEf3UODsaSDya1LPSVQdBcJnVs0IsM1isvrh5MxEu10J600AXJTVfacfoZi_yiWwrXIEcIE-MsmvW-QQu-hzESiuo5HkxI08SSv5mmOTXbEkHX84lK7q2E7BlBd1KfJG7pkXRexpcNZb0H-kpJxww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XxY5tvm_J2gH48f6P9P5ZDnoxmxzsogJGVSFWkmpOSGcpChTF6GAEVxSHgPsfPy4cqARm2WXfSP0cMLQ5enA232y9OS8KC2sRCqZCbXrqUqkh_LL3j3BjXJbQFGtUgdMi4-Af9Yi2JBNyXr95mT4uNTDmkISCAmbWtg7YxPkOY3gIZnlMHlANh3KAoC19bXBpZE9ToSF1PQuMrENKpSxQ5ti1c0S3qU7arehYP48ci14OzHxQHwISvp04n_9wi-J5ebQHZdLHSr83_a6dPjSB9qLvH38QoChrpRNtMuGAuxQBhNJ6vkiqMV7ykDdulWZIN4soZLEauRrOrV8fZc7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kKLUj3pHmQEgt2AAtnNJ6DHLUB8smgA3n9_Ap_sPBktE76ER4swQvKHq-4eQud7D4HS4JYsiduB8B8flZHhPexsuHX_sSrLhzRZYuUDnxwH7BBLvM9YasPt-fC2DSbsJkyFxllExXx2mTc-RwKUZE_s5pm1WpjoKjd9M_UR2I0X22WtVstsfZUwaJRyq-vd7N3mmPGCwEpLbcjPuctIZActU9zxa_To6J59tBpUGdqGo8KNZK1m4Q1rhKGqMT_8j5o5e7gp9YBaAC5EIHZPd2auI4LXsLpDo9XT6dTs71NHyb_Hbbmc7GpsOTNf84p9e48hFbPbFjZ3GbbkM1WpQtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aOMU42v5AypTpbJxkYuszg7teeO7rRn1TGZazUSj79DF8YpX9fL9yxEaviqi7azcs2ZRJHhvlrgQG-Uk584LkKbxYpiZ64mCfB_OnW8WAnVjTBmpfHFPJEO-5P1dqy_ZaVD94GuSSFP4JeQK77H2vkpSBVnwgNvhBnqCHeNIIc14mmsc4mRAMUGk6KGLA7lRgTR7oSZ2-sC3d_4F_3BOrGuwlHous-ROSf9AI310vQH8bdICOcd38Xuh67OzpsekzPeQgYHHVlRlSGSLFt471SSkOQrlZGcZNkCYvXIqcShFKzHkCRIxMMDwHLxuRb9haPGrG6oCUJyDldJWJj-QXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aT5DzY-kGqLISmDjfoEJbJwUpSdOqhnjTdEWfIvX38kQEmPpkYTGJAYzQr-3YJpC9Ort8uNEcqCi3hdnfV-ViK1ippXmoPVm7eJLifmi8UReLNxVV7BJ_gYmCACYMNlU1T8p02cu6xUMwAE4dImvYgBPSNgUwxIpnL4iaZeWqj4eh3yN4oLrpXm7DLc8kybGvm67qZBIyuStNKCbug1LX1JWsBZJdLdRvcbDpJHzghpVjBPnOyMLDFGVe4aceL7iFiET8KWXX0o0icms8_afHmMuUGOwDjgl6CvSO_1JmEy4LnbPnu-B0GmWVRI0-3sCjjfOz1sQytqNrEMofcwzyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3WsuSsb4gzka77cJo12UnEityjFvjT0rEnGYVUNOSAC01-Vq-jDc1xFZF9U37n_d7VrvQzjwdnOSIF5lxBbU8Xj8A2pI7XPbYi6z4egmzmsqw-2OhIq6S5fxM8MtxvEWHMNr0K1iCVEJglMkPe1lB_KVLxmmqreS9LS1KZ60aJQyvCTXPUpkuOGM24s7KOaCQ1xE7PDuY0PmhA_wVFDA4L5qmuMpYWRlqzh8EXx7RvW9zFIlGu2qlqGdmCaNZ_5mVVVGnWUjvaGbPnCztLmauJxTia-cJNB8WognQFKvGb3MJQonm3ddAtkwF7oceMfAlRoZwCJxw1UssuSMGF9Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از بالا چپ به راست
اتصال Tor با برنامه اسلیپ نت
پل Obfs4
بقیه هم میتونید تست کنید
Snowflake, Meek Azure
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/archivetell/5564" target="_blank">📅 00:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پاکت هدیه
🎁</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/archivetell/5563" target="_blank">📅 00:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سوپرایز anonvector
❤️
🚀
آپدیت جدید و هوشمند کلاینت SlipNet (نسخه v2.5.5)
---
نسخه جدید اپلیکیشن
SlipNet
منتشر شد. توی این آپدیت، سازنده تمرکز اصلیش رو روی هوشمندسازیِ فرآیند اتصال و تنظیمات DNS گذاشته تا کانکشن‌ها خیلی سریع‌تر و پایدارتر بشن.
✨
مهم‌ترین قابلیت‌های این نسخه:
🔸
تنظیم خودکار شبکه (DNS Auto-Tune):
برنامه حالا می‌تونه به صورت کاملاً هوشمند، پارامترهای حساس مثل
Query Length
و
Rate Limit
رو بر اساس وضعیتِ فعلیِ اینترنت شما (برای کانفیگ‌های DNSTT، NoizDNS و VayDNS) تشخیص بده و موقع اتصال تنظیم کنه.
🔸
انتخاب خودکارِ بهترین دی‌ان‌اس (DNS Pool):
اگه این قابلیت رو از تنظیمات فعال کنید، برنامه قبل از هر اتصال لیست DNSها رو اسکن می‌کنه و ۱۰ تا از سریع‌ترین‌ها (با کمترین پینگ) رو برای کانفیگ شما ست می‌کنه. *(دو حالت اسکن سریع ۱۰ ثانیه‌ای و اسکن دقیق ۱۸ ثانیه‌ای هم داره).*
🔸
اسکنر و مدیریت پیشرفته DNS:
حالا می‌تونید آی‌پی‌های سالمی که اسکن کردید رو در قالب یک گروه یا استخر (Pool) ذخیره کنید و هر زمان که خواستید با یک دکمه فوراً لودشون کنید.
🔸
بهبودهای ظاهری و امنیتی (UI):
- منوی اضافه کردن کانفیگ جمع‌وجورتر شده.
- می‌تونید برای باز کردنِ باندل‌ها و قفل کردنِ پروفایل‌ها، پسوردهای کاملاً مجزا و مستقل تعیین کنید.
---
📥
دریافت آپدیت:
می‌تونید فایل نصبی این نسخه رو مستقیماً از لینک گیت‌هاب زیر (بخش Releases) دانلود و نصب کنید:
🔗
https://github.com/anonvector/SlipNet/releases/tag/v2.5.5
📌
#آپدیت
#SlipNet
#فیلترشکن
#اندروید
#DNS
#تونل
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/archivetell/5562" target="_blank">📅 23:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSlipNet</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SlipNet-v2.5.5-full-release-arm64-v8a.apk</div>
  <div class="tg-doc-extra">25.7 MB</div>
</div>
<a href="https://t.me/archivetell/5554" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🕊
@SlipNet_app</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/5554" target="_blank">📅 23:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSlipNet</strong></div>
<div class="tg-text">v2.5.5 Changelog
🌐
DNS Pool (New)
•
Auto-Scan:
Automatically picks the top 10 lowest-latency resolvers at connect.
•
Verification Toggle:
Faster scans by default (10s timeout); optional full HTTP/SSH verification (18s timeout).
⚡️
DNS Auto-Tune (New)
• Auto-tunes query length and rate limits for DNSTT, NoizDNS, and VayDNS profiles at connect.
🔍
DNS Scanner
• Save working IPs as named pools and load them instantly via a new button.
🎨
UI Improvements
• Replaced the "add-profile" bottom sheet with a compact 3-column grid.
• Moved DNS section above Network in Settings.
• Independently set bundle-decrypt and per-profile lock passwords.
———————
✨
قابلیت‌های اصلی جدید این نسخه:
قابلیت Auto Tune: تشخیص و تنظیم خودکار و هوشمند پارامترهای Query Length و Rate Limit بر اساس وضعیت شبکه.
قابلیت DNS Pool (قابل فعال‌سازی در تنظیمات): اسکن خودکار و سریع لیست DNSها قبل از هر اتصال، و ست کردن بهترین و سریع‌ترین Resolver روی کانفیگ.
بهود رابط کاربری و رفع باگ
دانلود از گیت هاب:
https://github.com/anonvector/SlipNet/releases/tag/v2.5.5
🕊
@SlipNet_app</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/5553" target="_blank">📅 23:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HO_CxE9rFkiMhp8PDhu6F9e432xPwRU6Ee61gg6ZGoPb5wg0ijTvum35ftW9NGawSQu07A30tBdIqYONHGrcDY1STtebvcW6UNR2k3IMRP0S0SAzmU7dI8Bk2W4lSLmsoeXJWBwc0XsQg2bkVI7HjubUTQ9pbrtMxbwS-MprQOFz6ow5eoY-484ep7XpRRXYgdDzkYryTbKiCwQj-RW1q9q0gx-Jt2CuBWTWqId-M7IAJItQzGtLNq6IHByzDT1qvPo_g59N1L9wViCt5YEYNJ6f_omR4mmkPezzg6EM_M1iEby6aV6T21swEFwhJkgWyDMJ-AVNoLeBqVMSfsfJDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله  یکم لایک و انرژی بدین اپ تر و تمیز که رو ایرانسل کانکت میشه یافتم
🙊
🙈
❤️</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/archivetell/5552" target="_blank">📅 23:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5551">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سبحان الله  یکم لایک و انرژی بدین اپ تر و تمیز که رو ایرانسل کانکت میشه یافتم
🙊
🙈
❤️</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/archivetell/5551" target="_blank">📅 23:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سبحان الله
یکم لایک و انرژی بدین
اپ تر و تمیز که رو ایرانسل کانکت میشه یافتم
🙊
🙈
❤️</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/archivetell/5550" target="_blank">📅 23:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نت شخمی نشده؟
کانفیگا پولی هم بد وصله
😐
😂</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/archivetell/5549" target="_blank">📅 23:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ایرانسل پر سرعت وصل
Windscribe UDP 443 Censorship On
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/archivetell/5548" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">همراه اول تست شده
vless://06ef598c-1555-4887-b3f9-08214a2f6792@104.16.7.70:443?encryption=none&host=2026.hhhhh.eu.org&path=%2F222.167.202.31%3A7443&security=tls&sni=2026.hhhhh.eu.org&type=ws#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/archivetell/5547" target="_blank">📅 22:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سامانتل بدون فیلتره اینستا
😁</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/archivetell/5546" target="_blank">📅 22:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سامانتل بدون فیلتره اینستا
😁</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/archivetell/5545" target="_blank">📅 22:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompatterniha</strong></div>
<div class="tg-text">پیامهای تشکر و محبت آمیز زیادی دریافت کردم، ظاهرا به خواست خدا وارد قلب هزاران نفر از مردم شدم، فقط میتونم بگم از همگیتون ممنونم.
البته به نظر من کمک اصلی رو "امین محمودی" کرد، پروژه های mhr و masterDNS بینظیر بودن و باعث شد عده ی زیادی متصل بمونن.
واقعا با یک تلاش دسته‌جمعی درصد قابل توجهی از خرید کانفیگهای گران قیمت بی نیاز بودن، افرادی مثل "aleskxyz" ،
"ناکر" ، "samim"، "Sarto" , "shahab", "گروه وایت dns", "مارک پشم‌فروش"  ، "Break_The_Barriers" , "CyberNigga" , "بیا پایین بچه"و ... کمک شایانی در این قضیه انجام دادن.
عده ی زیادی هم تو بحث آموزش این متدها نقش داشتند، عزیرانی مثل "متین سنپای" که آموزشهای روان و ویدیویی در اختیار عموم قرار میدادن که بدون آن قطعا عده‌ی زیادی نمیتونستند از این متدها استفاده کنند.
همچنین جا داره از RPRX بنیان گذار project-X که توجه ویژه ای به ایرانی ها داشت هم تشکر کنم، واقعا v2ray الان به ابزار اصلی ارتباطات اینترنتی تبدیل شده.
از دوست چینیمون "zhc" هم بسیار سپاسگزارم، با دانش بینظیرش کمک قابل توجه ای به مردم ایران کرد.
واقعا یک تلاش بینظیر دسته جمعی صورت گرفت که نمیشه از همه نام برد، من هم خوشحالم که نقشی در این زمینه داشتم، باز هم از همگیتون ممنونم
❤️
///
هنوز نت به طور کامل باز نشده ولی با متدهایی که در حال حاضر وجود داره باز شدن کوچکترین روزنه ای به معنی باز شدن کل اینترنت خواهد بود.</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/archivetell/5544" target="_blank">📅 22:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">همراه اول bdnet وصل</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/archivetell/5543" target="_blank">📅 21:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHosseini.h</strong></div>
<div class="tg-text">همراه اول bdnet وصل</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/archivetell/5542" target="_blank">📅 21:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑴𝒓 𝑯𝒂𝒎𝒊𝒅༗</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/swsKqXJUvnA3omrpDh0qPvMOQP7bIKe2sWGx1sZSvYlMWo5DO5vrjJzLd2cII6-yO27oDMi3pay_2e3rPIr1iAaITz0tx3kX0Nzxzb407xcioShVvuzAVuiiM7S0oknKDO1x6xKuNOcmJaJlgr7iOHsOmpApuBCxL_vU6O5XY5Fl9lH3y_8PtavbNVAtOEy-yjJnNF1gKFmWLc_p9Q8K68qgkFwuJ8ejSiIP8BKbH102yijs-Pn-ixpPial3wTnP81U6URyuJ99jv6edfs1p6su3sqdtVGInN3F1k7yvWgVLTzJBT3C34ZwohFUoXtHO_Ivc-lP5VVinnwweG-o-Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YpMjyzk4ay4uigIAtuDeEjio2xIBgGdIOVPOebzXZ3wW3k4LMFWjmQearnbKNuSAiJIqbW8aLVD0X1v2fABfftUci3UJnGHO4wrve5t0i_PpeKW2eBKIdj9ojQNOEInsrBRxacVS0Ug7KNAbnCszeLgO0dePXPxP2ERGL0G_idfW5IJZn6epIuatrHf_q8eeD24lG12UUlelZFKGcS78w29jvRqCutw4NIgVoOtj--wgoyBm1TDEY356xkTkfvDRktLbWNIbrEyDAPCGQxH3Z4hXUwVZ2tDg5iTtFcj6YLC-RYw6tkRTFc767l8u9IhhusIq-T9jtcTG6tAtgeazsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این دوتا وصل شدن همراه اول</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/archivetell/5540" target="_blank">📅 21:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">vless://IR_NETLIFY@194.59.183.234:42115?type=ws&encryption=none&path=%2F&host=&security=none#IR-NETLIFY
مستقیم وصل</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/archivetell/5538" target="_blank">📅 20:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">همراه اول کلودفلر وصل
trojan://8r%3C%5B9%27l6hAO%238ZQi@104.18.12.149:40443?allowInsecure=1&host=Koma-YT.PAGeS.Dev&path=%2Ftr&sni=Koma-YT.PAGeS.Dev&type=ws#%F0%9F%87%A8%F0%9F%87%A6%20Canada%20(CA)%20-%20Toronto%20@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/archivetell/5537" target="_blank">📅 20:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آیپی تمیز همراه اول
104.18.12.149
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/archivetell/5536" target="_blank">📅 20:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiliya</strong></div>
<div class="tg-text">اینم یادتون نره بزارید
شاید بدرد کسی بخوره مستقیم هم سایفون وصله</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/5535" target="_blank">📅 20:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiliya</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">PsiphonProSetup_x64.exe</div>
  <div class="tg-doc-extra">76.1 MB</div>
</div>
<a href="https://t.me/archivetell/5534" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/5534" target="_blank">📅 20:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiliya</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oy2hXSsJkQ_E25u9ghY3RVF5rsf3wNyFeQ5YFnSFReOW5bEvVgdGCE_LGNTwfv3iet6H_znLhyPeEr0gf2DWDZeNIJ0N58J-YIIDc9JjITS2hBoDumSLPSZoFMUSXcW3_QxmxZnhGiDuuMHZzadgwS_7BypcFJAp7Vi3cEGASzEWqZxhEUthPyk8GaCHwJUw-rg5DvypAyUbK-jAa0d-6MdtNBimBHnm0p9BXaXDt8_fuIJf9ALL-_90nEU2dbu_-Rx4bYVj_W_Y5tWSCLHeRqDBw0u8fe81Ly3cKRQGKSR856CBckREyJ8D9qEaVXReDPBRU3scP_qmJ8HK3Zv4Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s1rFkVEheauTJ0X15u99He3qRvbQr2teH67_rk0v5ucbfRLt7iTtnANA0RQjA-wrlFCtiXIuJHzVgbI3rOnssgCpKISdNKtR50QT4ZD_mkKNIyiZBsQUMD8Ma55F6CXzglFh4Ute75qV5PQI10zcjr77casgfp_65lvKqdCD3Kl7Ate2p-H-Wm09yD8j-o_xtM1bTR7M08pT5uP3fdLqSCVPSO8cPAAcE_IkGBt1J54gBjj0Isg_Jjzwa62zq42XPxOI-8jx6IT6m76ArU3tQku-9ZD3aYDGkUqW08O3HQiLKRx1GoD_axCNnX1HXx0BpR3DTbQK-YU2DqMuHz33vg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برنامه ی سری تغییرات دادم و تو خود برنامه میشه کانفیگ زد ترکیبی وصل شد و بین مود های
psiphon
v2ray
v2ray+psiphon
جا ب جا شد</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/5532" target="_blank">📅 20:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آیپی تمیز ایرانسل   27.50.48.49 @ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/5531" target="_blank">📅 20:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آیپی تمیز ایرانسل   27.50.48.49 @ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/5530" target="_blank">📅 20:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">https://t.me/proxy?server=191.101.113.153&port=443&secret=ee3ef807f06138530624d5631232bfa592636c6f7564666c6172652e636f6d
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/5529" target="_blank">📅 20:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آیپی تمیز ایرانسل اسکن کردم   واستون میذارم
😁
❤️</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/5528" target="_blank">📅 20:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سیمکارت ها هم وصل شدن</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/5527" target="_blank">📅 20:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">آیپی تمیز ایرانسل اسکن کردم
واستون میذارم
😁
❤️</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/5526" target="_blank">📅 20:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🛡
معرفی ابزار فوق‌العاده Paqctl: عبور از سخت‌ترین فیلترینگ‌ها با دور زدن DPI
---
اگر سرور مجازی (VPS) دارید اما آی‌پی‌تون مدام فیلتر میشه یا سرعتتون به خاطر سیستم‌های تشخیصِ هوشمند (DPI) افت می‌کنه، امروز ابزاری رو بهتون معرفی می‌کنم که قواعد بازی رو عوض کرده:
Paqctl
(بر پایه هسته قدرتمند Paqet).
💡
این ابزار چطور کار می‌کنه؟
روش کار این ابزار با V2ray یا کانفیگ‌های معمولی فرق داره. Paqet ترافیک شما رو از لایه‌های بسیار پایینِ شبکه (Raw Sockets) عبور میده. در واقع پکت‌های اینترنتی رو طوری "دستکاری" می‌کنه (مثلاً فلگ‌های TCP رو تغییر میده یا پکت‌های عمداً خراب می‌سازه) که سیستم فیلترینگ (DPI) گیج میشه، نمی‌تونه تشخیص بده این ترافیکِ پروکسی هست و در نتیجه اجازه عبور میده!
⚙️
دو روش قدرتمند در یک ابزار:
این اسکریپت به شما اجازه میده دو روش مختلف رو روی سرورتون نصب کنید:
۱.
روش Paqet (ساده و پیشنهادی):
از پروتکل KCP روی پکت‌های خام TCP استفاده می‌کنه. شناسایی این روش برای فایروال‌ها بی‌نهایت سخته. خروجی این روش یک پروکسی SOCKS5 روی پورت
1080
سیستم شماست.
۲.
روش GFK (مخصوص سانسور شدید):
از ترکیب پکت‌های "نقض‌شده" (Violated TCP) و تونل QUIC استفاده می‌کنه و در نهایت به یک هسته Xray وصل میشه (پورت
14000
). اگر اینترنتتون به شدت محدوده، این روش معجزه می‌کنه.
---
💻
آموزش نصب سریع (مخصوص لینوکس):
مرحله اول: راه‌اندازی روی سرور (VPS)
وارد سرور لینوکسی خودتون بشید و دستور زیر رو کپی و اجرا کنید (نیاز به دسترسی روت دارید):
curl -fsSL https://raw.githubusercontent.com/SamNet-dev/paqctl/main/paqctl.sh | sudo bash
بعد از نصب، با زدن دستور
sudo paqctl menu
یک منوی جذاب باز میشه که می‌تونید سرویس‌ها رو نصب، استارت یا مدیریت کنید.
برای دریافت اطلاعاتِ اتصال (آی‌پی، پورت و کلیدها) کافیه دستور
sudo paqctl info
رو بزنید.
مرحله دوم: راه‌اندازی روی کلاینت (ویندوز/مک/لینوکس)
ابزار Paqctl فایل‌های کلاینت رو هم در اختیارتون می‌ذاره. کلاینت رو روی سیستم خودتون اجرا می‌کنید و اطلاعاتی که در مرحله قبل گرفتید رو بهش میدید. کلاینت در پس‌زمینه اجرا میشه و به شما یک پورت SOCKS5 میده که می‌تونید اون رو در مرورگر، تلگرام یا برنامه‌هایی مثل v2rayN و NekoBox وارد کنید!
---
🔗
لینک‌های دانلود و گیت‌هاب پروژه:
سورس اصلی پروژه و آموزش‌های دقیق‌تر برای نصب کلاینت ویندوز رو می‌تونید از گیت‌هاب‌های زیر بردارید:
🌐
ابزار مدیریت و نصب آسان (SamNet):
https://github.com/SamNet-dev/paqctl
🌐
هسته اصلی و خام برنامه (hanselime):
https://github.com/hanselime/paqet
⚠️
نکته:
اجرای کلاینت روی ویندوز نیازمند نصب بودن پیش‌نیاز
Npcap
هست که داخل گیت‌هاب کامل توضیح داده شده.
اگر کسی این متدِ Raw Packet رو روی سرورش تست کرد، حتماً از وضعیت پینگ و پایداریش توی کامنت‌ها برامون بنویسه.
👇
📌
#آموزش
#سرور
#فیلترشکن
#VPS
#تونل
#Paqet
#Paqctl
#DPI
#لینوکس
#ویندوز
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/5525" target="_blank">📅 20:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5524">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">همراه اول سورف شارک وصله</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/5524" target="_blank">📅 20:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ایرانسل cdn شیرو خورشید نسخه جدید وصله سرعت عالی
لینک داخلی شیر و خورشید</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/5523" target="_blank">📅 20:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترکیبی سایفون یا شیر و خورشید با v2ray
ایرانسل و همراه اول
trojan://humanity@193.151.152.206:40443?allowInsecure=1&host=www.ignitelimit.com&path=%2Fassignment&sni=www.ignitelimit.com&type=ws#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/5522" target="_blank">📅 20:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سلامتی اونی که امروز گیگ بالا اوتباند گرفته
😔
❤️
🍷</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/5521" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ی اعلام وضعیت بکنین
با چه اینترنتی و با چ اپی وصلین
👇
:</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/5520" target="_blank">📅 19:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚀
آموزش جامع ساخت فیلترشکن شخصی و رایگان با پنل BPB (بدون نیاز به سرور!)
---
امروز می‌خوام یکی از بهترین، پایدارترین و بی‌دردسرترین روش‌ها رو برای داشتن یک VPN دائمی و کاملاً رایگان بهتون آموزش بدم.
توی این روش که به کمک پنل
BPB (Bypass Panel)
انجام میشه، شما نیازی به خرید سرور یا دانش برنامه‌نویسی ندارید. پنل شما مستقیماً روی سرورهای قدرتمند کلودفلر (Cloudflare) سوار میشه.
💡
مزایای این روش:
-
رایگان و دائمی:
اکانت رایگان کلودفلر روزانه حدود
۵ تا ۶ گیگابایت
(۱۰۰ هزار ریکوئست) ترافیک به شما میده که برای استفاده معمولِ ۲ تا ۳ نفر (یوتیوب، اینستاگرام و...) کاملاً کافیه.
-
شارژ روزانه:
این حجم هر شب ساعت ۳:۳۰ بامداد (به وقت ایران) دوباره صفر و شارژ میشه!
-
سرعت و پینگ عالی:
به دلیل استفاده از شبکه‌ی کلودفلر.
---
🛠
مراحل راه‌اندازی (قدم‌به‌قدم):
مرحله اول: ساخت اکانت کلودفلر
۱. وارد سایت کلودفلر (
Cloudflare.com
) بشید و ثبت‌نام کنید.
ترفند: برای اینکه ایمیل اصلی‌تون درگیر نشه و بتونید چندین اکانت بسازید، از سایت‌های ایمیل موقت مثل
atomicmail.io
استفاده کنید.
مرحله دوم: نصب اتوماتیک پنل (BPB Wizard)
برای اینکه درگیر کدهای پیچیده نشید، یک ابزار اتوماتیک به اسم BPB Wizard وجود داره که همه کارها رو براتون انجام میده.
⚠️
دو نکته بسیار مهم قبل از اجرا:
- وی‌پی‌ان (VPN) شما باید کاملاً خاموش باشه.
- آنتی‌ویروس (مثل Windows Defender) و فایروال سیستم رو موقتاً خاموش کنید (چون این برنامه کدها رو از گیت‌هاب دانلود می‌کنه، آنتی‌ویروس بهش گیر میده و می‌بندتش).
💻
اگر ویندوز/مک دارید:
ابزار BPB Wizard رو از لینک انتهای پست دانلود کنید، از حالت فشرده خارج کرده و اجرا کنید. مراحل رو با زدن کلید Enter طی کنید تا پنل نصب بشه.
📱
اگر اندروید/لینوکس دارید:
برنامه
Termux
رو باز کنید و کد زیر رو کپی و پیست کنید:
bash <(curl -fsSL https://raw.githubusercontent.com/bia-pain-bache/BPB-Wizard/main/install.sh)
*(نکته: ترموکس رو به هیچ‌وجه از گوگل‌پلی دانلود نکنید، حتماً از سورس اصلی یعنی F-Droid نصب کنید).*
مرحله سوم: تنظیمات داخل پنل BPB
وقتی مراحل بالا تموم شد، ابزار یه لینک به شما میده که تهش
/panel
داره. واردش بشید، یه پسورد قوی بسازید و لاگین کنید.
⚙️
دو تا تنظیم مهم انجام بدید:
۱. تیک IPv6 رو خاموش کنید تا اتصالتون پایدارتر بشه.
۲. تو بخش Routing Rules، تیک Bypass Iran رو بزنید تا وقتی سایت ایرانی باز می‌کنید، ترافیکتون از فیلترشکن رد نشه و سایت‌های بانکی گیر ندن.
---
📲
چگونه به پنل وصل شویم؟
تو پنل خودتون، برید به بخش Subscriptions و لینک بخش
Normal
رو کپی کنید. حالا بسته به دستگاهتون:
🤖
اندروید:
برنامه
MahsaNG
یا Exclave یا V2rayng رو نصب کنید. لینک رو از کلیپ‌بورد Import کنید، از منوی سه‌نقطه Update Subscription رو بزنید و بعد از پینگ گرفتن، متصل بشید.
💻
ویندوز:
برنامه
GUI.for.SingBox
رو دانلود کنید. حتماً روش کلیک راست کرده و Run as Administrator رو بزنید. از داخل پنلِ BPB، فایل
config.json
رو دانلود کنید و تو این برنامه ایمپورت کنید.
🍎
آیفون (iOS):
از اپ استور برنامه
Streisand
رو دانلود کرده و لینک سابسکریپشن رو داخلش وارد کنید.
---
🔗
جعبه ابزار و لینک‌های مورد نیاز:
🌐
سایت کلودفلر:
dash.cloudflare.com
📧
ساخت ایمیل موقت:
atomicmail.io
⚡️
دانلود ابزار نصب BPB Wizard:
🔗
https://github.com/bia-pain-bache/BPB-Wizard
📥
دانلود کلاینت اندروید (MahsaNG):
🔗
[دریافت از گوگل پلی](
https://play.google.com/store/apps/details?id=com.MahsaNet.MahsaNG
)
📥
دانلود کلاینت ویندوز (GUI SingBox):
🔗
https://github.com/GUI-for-Cores/GUI.for.SingBox
📌
#آموزش_جامع
#کلودفلر
#فیلترشکن
#Cloudflare
#BPB
#ویندوز
#اندروید
#آیفون
#رایگان
#سرور_رایگان
#VPN
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/archivetell/5519" target="_blank">📅 19:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اموزش بچه پایین بیا BPB به زودی گذاشته میشه
راحت شده اسکریپت جدیدش</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/5518" target="_blank">📅 19:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">از همین تریبون از تمام کسانی که ما رو در این مدت متصل نگهداشتن ممنونم
بخصوص از anonvector گل بابت برنامه خفنش
https://t.me/SlipNet_app
و پترنی‌ها و سایر افرادی که پونز شدن روی صندلی فیلترچی
یادمون نمیره زحماتتون
❤️</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/5517" target="_blank">📅 19:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مخابرات
trojan://humanity@104.18.32.47:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#@ArchiveTell</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/5516" target="_blank">📅 19:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بمن گفتن زنان قریش رو در اختیارم میذارن
گفتم نه نت پرو؟ ممنون
🙏
👍</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/5515" target="_blank">📅 19:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">https://t.me/proxy?server=51.120.71.120&port=443&secret=c760667d53b6856ca44431fc93b8fe23
https://t.me/proxy?server=95.181.213.248&port=443&secret=ee8a2802995839c6ce8b8f7b0c3bfe44c67777772e617669746f2e7275</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/5514" target="_blank">📅 19:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمهرداد استاپ</strong></div>
<div class="tg-text">من از سازمان بنیاد ملی بازی های رایانه ای باهام تماس گرفتن و قرار بود نت پرو بدن ولی قبول نکردیم و با هزینه شخصی ادامه دادیم</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/5513" target="_blank">📅 19:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLUFFY</strong></div>
<div class="tg-text">شکن عوضی حالا که نتا وا شده چت جی پی تی و اینارو اورده که مردم بخرن که انقدرم خر نیستن مردم</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/5512" target="_blank">📅 19:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفرهاد</strong></div>
<div class="tg-text">اونهایی که پرو نگرفتین دمتون گرم به خودتون افتخار کنید</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/5511" target="_blank">📅 19:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفرهاد</strong></div>
<div class="tg-text">دقیقا و کانال های یوتوبی که اینترنت پرو تبلیغ می کردند</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/5510" target="_blank">📅 19:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiman</strong></div>
<div class="tg-text">ادمین این شکن بیشرف هم که مردمو تهدید میکرد و اکانتاشونو بن میکرد باید توی گروه ها اعلام کنن که هیچکی‌ ازش خرید نکنه. اینارو یادمون نره که کی توی شرایط سخت سنگ مینداخت جلو پای مردم</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/5509" target="_blank">📅 19:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یه متن کوتاه کامنت کنید در مورد حمید رسایی
😁</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/5508" target="_blank">📅 18:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from✨Orchid$✨</strong></div>
<div class="tg-text">لطفا از عبارت "اینترنت داره به حالت عادی برمیگرده" استفاده نکنید.
ما هیچوقت اینترنت عادی نداشتیم.
در بهترین حالت یه فیلترنت بوده با هزاران محدودیت و مشکل...</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/5507" target="_blank">📅 18:54 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
