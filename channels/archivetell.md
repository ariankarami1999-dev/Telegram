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
<img src="https://cdn4.telesco.pe/file/lOF3BSwz8I9baI4UoP0WVaJq0XxJ_HXFrVLeVBciXP6CN-Hak0AT8_PYyBhZjAKTyUXXMxr7T-Ikj0jxupnCTqVLhpDyZt_qlMNQI6_yirxclhVp3ugDI9CarwFscFvSkLoIQ9EA6Fi3Gt196Cxozsg33x9aY-JflcdTu8jxz8-npRlcV1S-ZSJb8wVQxhgWugZoHP_yHiDZcRMNuv4vjBqKzJWdW92SSZmpcxT7d9J0NGxbt6e5Bdf0lq2GfS9efiT6jGFAKnBsJ4qnOuYbDtrpwxBm2po5OUc7btnGIVQFME-VelAeVL_DQUwwgiTHKXZh5mgkfJ7T3l1WXIXUqw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 02:44:05</div>
<hr>

<div class="tg-post" id="msg-7500">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=CYc3lxWjsVGuGUSHtyKZ8Yq7FT-5jRVWYx71CFtb-s1O4l6wlC6vxs4NvRAFACMJ6IBu5DNBM1WoGl-TZEr5whFJ4g6mG2yl0zpQPe-2BOUPkxaaBW8_0dlkj2jhFsGaGyfN69qOpaCGaYrqpp0nJ5ZofvPzNdr776NFArkc8QrlfiVSpANHOZ23RhQ2Qt-ZuoyJqIluZcE2X6y8Oda3MU1-2Y4wPAk3yk-N135wNgjvbquptafSnR578JdJGJwrMN-k5HEnOQew2WCMbuM7RAZocFsl1yXTR-2qGwy414d8V9aA-OVtGHJ_U9LLn0c-Iiq26ibormGFagOeHkPE6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=CYc3lxWjsVGuGUSHtyKZ8Yq7FT-5jRVWYx71CFtb-s1O4l6wlC6vxs4NvRAFACMJ6IBu5DNBM1WoGl-TZEr5whFJ4g6mG2yl0zpQPe-2BOUPkxaaBW8_0dlkj2jhFsGaGyfN69qOpaCGaYrqpp0nJ5ZofvPzNdr776NFArkc8QrlfiVSpANHOZ23RhQ2Qt-ZuoyJqIluZcE2X6y8Oda3MU1-2Y4wPAk3yk-N135wNgjvbquptafSnR578JdJGJwrMN-k5HEnOQew2WCMbuM7RAZocFsl1yXTR-2qGwy414d8V9aA-OVtGHJ_U9LLn0c-Iiq26ibormGFagOeHkPE6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 602 · <a href="https://t.me/ArchiveTell/7500" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7499">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYc1sdOPGfqn_fOQ144SUjF-sSJ543N6PCd1viVUguXwl0IXJW9J2mCi_0oJLFZNGiNHUliOFnpS3ZKXreq2P3QF0MTDR6YvPN7kUIKFiKGdyTe60qebQmI2DwvAtnCiJD2vOtT3Meb1CGyov0F4Xd6J4DsSuhF0h9EtFOCz3uli6xmtYul61oRjAGrWoC6c6OCJrsPGjwEYRnq9UpobdY1FHmXGL78156GslfF5g45voaNkWQ4gvZx9yjKdV4AY6INHwxfa4kpp6OW38gi2jDr6OcZSzqz8IIW6zUi1kCEW5EL7ukwB8nV_qQ2p2CLkQctoQDWeUWtGxiw_ozGn6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 892 · <a href="https://t.me/ArchiveTell/7499" target="_blank">📅 22:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7498">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=er562Yf069vNXmZMXKzRpLFsrqcdgG1dF5_4Csu1WzACKxs1R7o4uABrY8kZojmJdpF5xKnFmt4SYqtD6SkFIjKPAJhKxzJeAPWbfsQGpwFhu546wTVH2I7Xa6kJp2MJ-TN3xj2fqdoxkxfMnfH8SglWAsj4Lc6eIlXiJjT6gI5mt0jozOCzy5biLUsNInOTqI4DrUEPQoWlS14ct5tAJ4ZSrsbTv3glWrsqqtZO-NMxwLnwLnhHUq6YsB7UpElggXKsR3C_DH4r74rK6diVeIZD1X3MAhdi4fhf7DYVBwr_IFNaqHOsnrG98azlLBMqukVmPZiw6wq4qtFhetdSmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=er562Yf069vNXmZMXKzRpLFsrqcdgG1dF5_4Csu1WzACKxs1R7o4uABrY8kZojmJdpF5xKnFmt4SYqtD6SkFIjKPAJhKxzJeAPWbfsQGpwFhu546wTVH2I7Xa6kJp2MJ-TN3xj2fqdoxkxfMnfH8SglWAsj4Lc6eIlXiJjT6gI5mt0jozOCzy5biLUsNInOTqI4DrUEPQoWlS14ct5tAJ4ZSrsbTv3glWrsqqtZO-NMxwLnwLnhHUq6YsB7UpElggXKsR3C_DH4r74rK6diVeIZD1X3MAhdi4fhf7DYVBwr_IFNaqHOsnrG98azlLBMqukVmPZiw6wq4qtFhetdSmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 958 · <a href="https://t.me/ArchiveTell/7498" target="_blank">📅 22:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7497">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dC0yCdi5xSh_YW7H3GwxIhWm1Qq4iSo-MMOf0yE-rNUgAzYHLlp8kvDIb8DCK5IGCpq6ARNMWOOTAWYATGBFCTd6W1YoQcNm9-Lt6FufA5T-bUrlil1Egj_A5M12gjdqYMVXmn6dtw0EnJjgigH4kyqZirr30nYVRVQJeYQRRG7IEO3wZIfZ6lxlkrWKDe6K-Nqkn2hBTJL_0HkITLUJwMuh6PfY_qSafpigObNCBooe8W_PAD2rlYMUB-KZtxzS53E8fzPGjEIEFxOCWKXfGFLTxJ9Mf5Rk-Fnr2lhGZxPU_Vrpzh-8PKVZKCqGMoOGGntEIqlNheJ008vgwMPeEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/ArchiveTell/7497" target="_blank">📅 19:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7496">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syhZr6fG6W4PDR6KKanBK4fc0z6et4Iv7HRXVLKlxYU33-6FSYI7HZFuyo2j_LXSxxnTrie7LwXFEhC1eHI9Y2GOzFYJUC3ZSB48ankMVWUX3qexjoO81Hs9svJJH5OHjqk95zt5EqjTaxmYG4XKKGm7unEcEQRXh4-TobwNjC76QzVdtSmWEP_swQuqZYmPRl_cixTmLSrLjdXAAGuFS1PIR6V2OcBvJhN3yxsPDHoLouhUdMk8WmYTg8ArLref6TmZwLDc_hng0YEg2G0gqcy-cyaluJ6JT-U8oCT_peGKRE3zOi3MgtlzWkGZzn94NPGybE24f-vQPDqOkC-FuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/ArchiveTell/7496" target="_blank">📅 17:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7495">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=TwS4xKsF34AgfeIaTQ1GmtayEAfuCO9PuGD4bj7r5J-a-5H9ie5I_X2-mIzMY4_kZrj4M4k6JSEf3KnQjHp3Psi203EmCu57vEkh-jCtQuM98CNVRl5NVzO7RqI-yx5R-RVuUg9pNQrng96139OE5QOKmxLsdv7wJ3hsenCOs_BiDO5yFLZboHG_qGvY42O5tf6H6Kzj1AIKKWAITNZ8LluKGiDCYKBLaVmp6NpS_DVQCK8cNu2k7PwwLGjN84KqgM6KqhDfusRQkjGluc0Nsx314fBMBsU1UUPDPZXLtXBOQO6hFwBy1h9bF3xI2AIs3CfrEsAADsFpA6Mbl9Q9bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=TwS4xKsF34AgfeIaTQ1GmtayEAfuCO9PuGD4bj7r5J-a-5H9ie5I_X2-mIzMY4_kZrj4M4k6JSEf3KnQjHp3Psi203EmCu57vEkh-jCtQuM98CNVRl5NVzO7RqI-yx5R-RVuUg9pNQrng96139OE5QOKmxLsdv7wJ3hsenCOs_BiDO5yFLZboHG_qGvY42O5tf6H6Kzj1AIKKWAITNZ8LluKGiDCYKBLaVmp6NpS_DVQCK8cNu2k7PwwLGjN84KqgM6KqhDfusRQkjGluc0Nsx314fBMBsU1UUPDPZXLtXBOQO6hFwBy1h9bF3xI2AIs3CfrEsAADsFpA6Mbl9Q9bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/ArchiveTell/7495" target="_blank">📅 15:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7494">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBna8ybnROmp6WM5FscD-npfdtGG_YxOPdRQQgkvNnOBf4DlvStwe432BiquumqT9bhx8kiz6Pz70v38AiJI8f2M4IOhWHp9RmVdCHk_hiAQ2RbjAotmiVn0MGhQiN2wiAlgEDlwXxic-6_Tvqkc1ekQB8vDrg2QfmwWZ5HsKWQBRyHHmTG-BLrY1qjqSX1jL4JwsH5GkxRX5m1py8PWXMMxkjXLeRb3gsQEy8jT0L1teN29bgmKrj6qD669xvgpoHo_KKIUMTWh7mSuizp_f29kFtjCDps69G-dYLeVwV37tsghKjTVadyjQcnltOcKrqgbW6RWTRdoIMYBH1X0bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/7494" target="_blank">📅 13:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7493">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngEi8-r4IQ-MJNOmguZ1OFFaNFSWqqPI6jHsz_O9jQO81VPLWnOB7DqV81pExRIYu9eYjIrqJRP6vKPyuiCEdvkb5l0hqzhXfNGYdU20YwjTGo2h7NUCoPcsW1TJWKUsEkKfsYQ77F7D92PWRaUEc4I3Hdz5SZpho3q6G99JKBR1bX-pgDTugO6xXJUVIDGrz3rXuBx_l55WUcLIQx37afenKhJ_eJNZjREaD_uZ1GKLtcIpt4OTtfquWmSOP3Je6SYinlEINAgYjHCSZM0ou_QLsr3NEunZdzMEXMe4qe9wuOQfYIdUkG8Z7gyZYTaVyy4VtX1WaCH_n2IHIbSqMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7493" target="_blank">📅 12:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7492">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09dd417185.mp4?token=n6EbBeI2HiBEnqXzv6EMzUEag3cX-QpXvL8d35CiY0CajTWCmjAYtcCnPzv-SAfPwkHnXuMoopqfGDHuavC58wQQ2EknLogwG1fAkB-f7dpZOBs8mWfq35lLhk6o3ii1q-xMl5IiZmp27VR_XNWIWtxFS6F1ti6SY4dtR_cpqsyLhQ1ZEG5tryRZrzjwgYjao5mrFNauNDAhYD4uCp7rHRjdCUdlSpGuHnzv2q4TQx8kSKcuu5kVFlV4fNS5WE5dRA-dzYupoYIM6V5_6L5CvmF-2Skcdr_itRyuRDR3AUG8UThK-vDymA-Q4d2HZyldQHPfToKq0F3oqCxURzTQcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09dd417185.mp4?token=n6EbBeI2HiBEnqXzv6EMzUEag3cX-QpXvL8d35CiY0CajTWCmjAYtcCnPzv-SAfPwkHnXuMoopqfGDHuavC58wQQ2EknLogwG1fAkB-f7dpZOBs8mWfq35lLhk6o3ii1q-xMl5IiZmp27VR_XNWIWtxFS6F1ti6SY4dtR_cpqsyLhQ1ZEG5tryRZrzjwgYjao5mrFNauNDAhYD4uCp7rHRjdCUdlSpGuHnzv2q4TQx8kSKcuu5kVFlV4fNS5WE5dRA-dzYupoYIM6V5_6L5CvmF-2Skcdr_itRyuRDR3AUG8UThK-vDymA-Q4d2HZyldQHPfToKq0F3oqCxURzTQcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/7492" target="_blank">📅 12:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7491">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oy0kr_3w4_XWWuuxJUhEIkG_SDHA4noh7Dn3Rj-Al_C5F3VNJ54C4ULQ7Cdc8yctF1MKatHazAzl9Z-y1F16f9lAA_4_44DIB6PpYMgI3KmSk_Llj4Xx3gpFtjzkMqDnY-5ELcznKNyXJi45dAJ50PAX78jG_QDrmQk_ohNdV_Cn3KPUhR9dvBUFOzkKL8Hn-1IyLi9NrNpwy3QsHL65Y7w0NXMq0MhHQ5WIxIhqNEkzhtdvnsyROJdPgu7xrdqMLot2_gH1OZTQHkrg6Sd9CNxjXph4KtHDPmVnvG0Sa2JR-ooQDFUwHs3irAK73qqftUKKtGsjDGq_pa5Y7zYOIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7491" target="_blank">📅 09:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7490">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7490" target="_blank">📅 21:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7488">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cn5BfcIXWnBWxblREqAJtBlEWk2KRdXhmXV6mZ9Ypp9BkzANygpstNmt0wE5sP0uAgKN-8CbrZA67GUQHn6S_Dx-vgZLAz3MyvaG11JbE_XsHgQZBQSNdsA-0dK0Ro8005V6PR8hmy9KaOma2UcBMmrVawLc1ArG-1id8IPi6h8UeqN9cmhc0cQNQbhlwrVSHZAsPOGaCFwWJjtk-ozrf0iyLzoYRKm21Scv_R99Wliy4wWHBVRBhRli8Bc-nPDFD_eR-4v7PsjDv5VLCfOqqSF2_lW42QGuRueDrD_XvvES2xQ7q8L5v5Z-Vl3HP3VK2oxVXCCIPhknUoiKK4r22g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7488" target="_blank">📅 19:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7487">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljvWF8MPSaHgGzFCRDru211UMHfMPgcUY2Ks9ZvLYz6GUMUMaY5XN4yxlNPa7oFr3L08_zwq5JQtTfhmkE9C5KsbKmotIYXtKPAOJPSjVftDLZZ2XFAIOHgY1NssUqE-Cho2Pz8VN5YfOk6Q6c5Gz5ashEcWWUK5klYJ2D2x-tmlBAEpsAo7xhxd-z1uNkNwMG07J_3moc-LqG7d72N9D-5bT-AVnlraecFuZAOZ7fTXWjDork8RSckwkXSOSAYFsN8iKe9i4shIG6O3mptiQQJnrufue9218BMkWoN2cJ5zjdBzinnyGVMqRRuypNyqPMmJSl-4BSwI3-CuUS1lTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7487" target="_blank">📅 17:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7485">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzJ898bCczIrxV-d_QqPTfAqmjExCn5NHnMqq0sk4-mm9qekT8MoT5l2zJYtjFRpbMrsD7dl1-IS0xSY0IywwOtmMBPcqMYL0wnyAFkNT8uBNYI63np9FqZv_q2E4XWrKAMpszeeofmpmgbZ1JrAmodvxEBM2fjtZ1YLiDWoR52pmCMjt-Tr-yeFsOnx0BODf88h-cD2sUXpbPqUV0Fpe9qVSLp74iyVW3o4orswUoUyYdAxpSSftHiu9GURMFuJfrtSVORS7qV9qa_9E1m7a6FeQoI31RYMpMy6WVNe-o4JTE0vpWlsOaoNZrh9KsfBdjW7CoeNVk1L7P8qZffLdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7485" target="_blank">📅 15:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7484">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZ_4lu7i3T_xQA5MLbL2y3DNPcLAn6AkYCvb9mQz08Le762XMTns9loSDRtSEo4LK-C08NaSr4PabJCUVHnYwm_3RIf2IT-NKYlYT1SrPw-tiaeULDg4wprtyHfMbMYpHtSlP7ImDU6hhZp1xYmf7vP0EnxUTIWTnIMGDnsumlAZ_RCc0MBktbbWVSNQSG_qdVnkAQrNqVNYbKTZGMhYN9Q1MBkSd9LYRqKgeL8uZDWb4Wh_1y3ivS1TpCDTU1eJxn7ulaIK51rWJk9lGD8KLS3OSdfw9j-ftdpSzpFjZmBQ-VDZX89ZCwb2fPYcE3xq7EbCKfAZhAHmV_JH_WOGAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7484" target="_blank">📅 12:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7483">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7483" target="_blank">📅 17:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7482">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDeFNOt3Rw_50Kn1IkGi7nJ8YT58iuRIaffBsJgnsJhIoMazTBLduJfl2sLmIZlqx3VfNLe3QZPcJK5Q4BFj5HYCSZAgARWT3hbREfFHolmgT98694VXw-LkzpXnDeH7lBHo9505W2CsIa2aJYZfgvnow-6cefVNdTm8rP5gw-KVcPEU6qkIKB9LLFQE4ZPT_DKYydDi2o6BC4hHoz1BeYGT4tzDooMFvoW1TYbCoFs5GFQV2iJj4Hl1EhaIA_TshUHh5zL28brkaZurjsDGS324-urOEEIoo1NUlUb6BYHzU5vf2zZ8Yg4FH4ukQlQ7omdwI3bVHDbk5MfR8b7K2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7482" target="_blank">📅 23:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7481">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qd67I4bhpugRJwkMIEtiS-fa8-FggjTIBas052deagA-aJOHpppFp7kX468yxvatR1knpXdlp3AB8_wl0ikahLhj0YRnyiSYvwxfG53LOm70e72vE6g2NcuQAUXm8TCkw-crzrcwKGF1CV0xCghTSLKUpTjnCk0jkvVVocAe9eedCwfYr5gXi5jbO-9xbshw34h-dK1ECXo1S-41HxDqPtAWt5quqyDa-CCKDh5eQxPBZxsEZ0tlzTVfiSl44OX1-skNAbndAOCjK2mIJgapXhW0bLYU6x0VckgDRqkIpbDIM46EV4aXfzaCKdaJho1-hpQhfHFtmadxs3evfhzU8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان: امروز از ساعت 12:30 تا 20:30 به…</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7481" target="_blank">📅 15:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7480">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7480" target="_blank">📅 14:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7479">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L39n67SkSGIWWseq-2WaFL9IAwC5THS4dddaiFI-Io_-hgr-LJpSQQ_OclhYwHwjBP6jFcKuSBKyNCcg6xgGWvUvMvn8oMW5-agXTknHjq-Tts_JaU0RQkXEkvEteiGkrbm4hNjCTrEYlkY-IDW5VemHBa3mjuZumIZTPvqIhDHZDDXAze8lZ42DwLj6dWgmlvHDSxBtMguWtgXIETHqohcT98JD6n9z0s8pXyIJ2QomDAydo1Lt_lktMVgfKNohsje6zYGdZ4WJ7eTm2YoT1GvWrdM6XmpbBVV-hyYYfx_OIJBWuxZqqgcXKYWg0ZUu30xLBM7LAsO9oiLFHatPqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7479" target="_blank">📅 13:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7478">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7478" target="_blank">📅 22:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7477">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">Gemini 3.7 is out now
😍
از اینجا میتونین رایگان تست کنین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7477" target="_blank">📅 21:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7476">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ad_F_m2qrCC_bW6NfUUM_TJ1zW-v9GoVMocAxKGaBuJot90veIV0yY7P0n5GTHpuW6YS59Na_LajVn9IHOgT-oGBLylCFHdocZ26sb6aE9gSqhNrhdVwvDw7aEpzZSydi1KUXIwvJrxvKuXs-J7RrNgjhAO9_JgL4I_9JYhFGcRFqSyMIhtFK3bfVR32JM_8uiSE-Cj8Yk8p-8i96qrNjHm5XY8FTyeowqAwlBhD4JmuAidKAog1ITehjaHRsbN32hg0QkeRZgO_Eb9VatTXRcdd-P0IsEoZS5U8tj3Fy8YhPc_-p9jQNBGH9h6x-XEqvWnmVOicmRwTEPViVYc0OA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/ArchiveTell/7476" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7475">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7475" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7474">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7474" target="_blank">📅 17:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7473">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kH8cxfF1wSM8j-xH0cyLZ--FbomqyGdXsj00nYIx-XvxNHjCqmZDxANZglGBLS5lExLWNQUCdYf40bTp_kF3SAkiqDrTwSx0hSkdftyaZ5iTuljFkGGwFtuyeljNbCNv_zcVqnI9KHOigPmHEQsT4SWaRyA2zpuIg_ppKbZowDMQDFFCWXJdozWiZIW3BhW2tGhpzXkauTYasiq-yz0oxhY7pJyZVDll-UKYwUGchsIuJ1OdekvotR_P-XylJ4vlPxt9r1wJWTaIdJo9q4U-jXUwWYCJLRrIWCLCr3xcoPCAYhhN3Ng08Q3-hvfy7EMvjQgcdl28nlr2jpq_kuKsCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7473" target="_blank">📅 17:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7472">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBsIcdNFCxKgQ4LTIBzX-gbIIVWD-Yw2z_lyC7DmAfQh3Gh9-9U_tQpn1U_kaNsI2m9U7PX2Ye4mge_tVU3QwA-wmCWcLPXI-t87mdHZGVFsQr3nQNn5mZBhcAbSK_PaT6h8jiulV4RrVNJadO0K-gHU40kE6YuxHZMdH00-tePylFDA-DAvO05aREVA1xX5xwdR5siXrncs7UmYC61xvJoN6YFMt1C8M52DQrHIcnh35OzjCeNH7CeIYH1DR_KlagJOABrrt1Kb6l4XABk6twOzxToMXf_4xdz40w0wDwpgy3JjvBFIXeC8vREnC2zMFjO8dIYE8D32qVPQF3CLdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7472" target="_blank">📅 15:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7471">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lENZUPb4_gZSktNmtZCfHsf7Xj_n4eEhs5uQTmayPBhzJf3gwtYCDmR-tDQDy5ccEYVS-qSqFLpyVbnIl3FVibkGMN7fpApcSbxyZ4fZGHv2tAPY9aCyUPNdi6assHznRSJ2d4k7bYe_xosk6t-hILKfkQrDLLLEil4TfsmRZz2VmVSITbvGFD1C1qyokoiqOMbjXPkaaOF3RjAjalcIC0eIqkVTp7tajbiibYSu4ME4Z1hVFm-2af73dNwhpjUQZqiLoaSJi7aQEWkOEU9h7Z9zuoxMe6DB9sJULfnvKZM6A8dVig6rq_3yq5eBfw1dZUf8RdFvtpaH3RRMKj2CnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7471" target="_blank">📅 12:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7470">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSmO9RE7ZzDvVeurrVYRbI_SISLMovZ0dI2Q7mt05Xt_hz2cHYbs3AKyzlsOUD-6fFee1r2BaZYMr9ZRsBnku7PZq4EVbGKm3dnLyyzJZSUgcXVHWW5jrjUpXvMwauZ64EMgiMuhVazMOSCKeWdJ0yJmtZ3flrLBENMxI0RIjCIngARxMe-CewteOy_UBGkR4_Ib9WxRBrHU4rJzT3SkstfmnUVu4RgZ4uTkmH2YfeUlPL2SU3jVUr50o5pQjsW4HHrGjBBXBqcGRsYjBAqvyEY6CGfXC4E1M3AOSrMr_UU-m8zUHonEQwD3rf4gecIUkc93lO1CbP7ZRspWcRw6ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
Grok 4.6 همین هفته میاد  قرار بود ۷ آگوست منتشر بشه، اما انتشارش عقب افتاد
😅
🧠
طبق گفته ایلان ماسک، Grok 4.6 حدود ۱.۵ تریلیون پارامتر داره و قراره در آموزش SFT و RL پیشرفت چشمگیری داشته باشه.
🔥
اما بخش جذاب‌تر:  چند هفته بعد، Grok 4.7 با حدود ۲.۱ تریلیون…</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7470" target="_blank">📅 23:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7469">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">https://t.me/ArchiveTell/7053</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7469" target="_blank">📅 17:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7467">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/An0QwqD9Cgv1dQKuj4udPgxXMz7Yf3sdtO0nPTXmMdOqJwWIKEShHrvdZoSGCXe7ZKw1N9RrcwaV_lNSyiPLKZViMenfkB9btdidfpKAl3z-SlQigVLwd4MhOPJAhnYck1WHQ_CRnq0bN8Y1Lpey6iDZFxDskzf8g-OZ4flSOrLulKBF6Tz_3a7mICqDgQIw8fVUr26fYHcu40-xc5pNrdIpAYb9VLbg5BDeb6c4K50PZwGLLNeP6PE1AYgKkMjGzo5czVgXtkJFH_G-_aftUH0Uu4w-zv4fXNKt075IAbAOq8lgnD1jiO2-u78Qw83ftZSLCdPBiaGlmLiLjjvW5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7467" target="_blank">📅 15:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7465">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7465" target="_blank">📅 13:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7464">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvoQbqSZxFiZLf-6jKzFVTCjOM1uXyiQX3epipmwpJAIcpef_r6Wvn-4pwxF10PDMXvE3GveC2spqyjcwJ_qOnu314HN-9mebTi3L-G_ASIOnuC-1T7n2VcUlCGmYUKnJVl_E-kbgAfSY4cf8jhSrSHRxJTRvEWQrZw5yDuvgoIrpsrBqJ74Grv2UygwF38wWTmABGPWqbgKPMT-kCcs7V0wRyPrBj5u9FS1NTJ5vHU9N5ZVnQclzpRR6GcDwwUuNinL7DW9SnuiXvV_4mBWc8I4XX2d1cFla9AXGTE_WOozXxibqxXkD-1J_7PvRW1grFVH1xxo-br23ZYNTJWtng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7464" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7463">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7463" target="_blank">📅 09:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7460">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9Mj2kCPJBPbPmYvSi8x1yDUgSVhMCwQKiAZmwyYSJHZytoLgF4l2JQ_UskrgE8ptHUATdFDa2W9f2mosRapl5aZimKxfR1VsVDzbB2ycW7deXfZnaQUYebtJjNjY8yk4_Z7oXM11a9-Uc3BE3NgedehstySyNJxMrKwfGep-Hmfzbt3P1eo6HoPNXma5nOuZ7y4powHEOymDFEygD1AZ-gz38aFOUy8KMPjTuo2In3KBHCA2MK1xxNNhaI-Osags-jnMo2btwVKtYsdHwd-0Qq89PE8G0BkRKcEknjFHTLLqST5mNgxegbfitSbkQoQn2ekswmr4atOR2vZ64WbeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7460" target="_blank">📅 16:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7459">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emV_EZuoHwfWACrcmzuwynyN7v-jfBqMN7mRv5aQl3Php8fn2c4ZdSSIMdH7atyKTZ9jkUyKivOM9cJt_19WEJxUCdCWYCgZ6-1TdIAQczVq55B1p8caVfUZdBPkSzLz5Fz8oRe1KhDGzJlAaHRhpMPPwvcjQa4djvGe4nG46L1LT52JrXe9zFjnrfuMrYxTNPDew9iw0GfVMSfuuRrE54kQESasLop8KGmEWIST9UlSVK39EEuwZNTcBDQhiW4hRZHXrvhd-fKmVjLTkrx3jcHEfbcGZSXJuKtW--LcjowxZ_4JylcYOHwnNDTJdKBgVr08nv6yQ6DgsgaVTxErTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7459" target="_blank">📅 13:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7458">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7458" target="_blank">📅 11:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7457">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_3J3yJTj0ULqHRvzRnfBiSJNevExmJNHNPceWWdtDxsoK_ufirS1-8vsw192F2l24jnAhuMU720eVsrkDJKHc9CJcwRLCnudFsHpEIonOvUClXVWr3a4peQnxYMsYeMb0fiiTJWhpesXZE_JLggFLmu7ckMtrnVE7deV1I_63tj4PO1pIPTm54BI_17pewn4Td699sdPmfreZNDRGRr4Ew07Fv-7b_7q-IXLXMnHemu1nTjm7R8cSDxLZteU8fAoZ7HviaUn2w3ed2YYqqj2kPe0NgSs7JCmxr6yaTCrypfx-FULa510vRFvsRhy4Xr6NJfKMI27pLDqz0Da92gEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7457" target="_blank">📅 11:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7455">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnthEDEcYC4xPUQsCaLN7wbtZ-xLT-VuJFNlbqR1BhLeqOKrwYvaOLUN9XIM2Mfltt5S2A0pRqD9KQLlXbpwcmtcyEJhwLu54atAz0mM6ftxzDdlvHOWqf8tbZZiQXiJf5SoC_Q7NCPm_0ue3aDYZEi5Y2gnMupmBCLbWhgqDeuveHzHBv-LTEW4v9geC3YRR_HSMwaZZbTh5fX9sobCXB-rjov8lUoy2KPM5aKt6Fi3MDWF0HB7IaswH3I-h33NG2BYllxl3rPTHmh-vI8uyRIX3DEf7SCKDB7kAedS7tV4Y7hRvvL-geAH7KmcV5KGKdm4t0Cq2irCQ77SNv1fQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/ArchiveTell/7455" target="_blank">📅 22:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7454">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tI0E1YVF-sjG16DpuOmTrL8AGi21S4CR689Jey4ru4IIBTT2yljydk1mSrXdljysOQ-yDK1pcTjy1HAyHnnEihJL4Z-FYEJ8AiLW1HHCAxgjfruC5E9Inf4-24YECBYDGwiCKMRMOzthH3V5t4X6wji-lBdFgkE0865uBKkwbqmYL6loWvRPMi0pFg3dA84yIZbkTeN_6ofmgOCuvkyjC_8mVdPjSWnesNlLwi13_QLimlN_aQZyZpyXGtIGUIPOqBCItBhShkaOEhNtzRnYEQDACjluGLiJya_h9A24H-BqG1AuWILAfHH8hAUGFgAvKw0R52kOIORVS1s0dYy7JA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7454" target="_blank">📅 20:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7453">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOuBeJUagguaZcbN5Zl5uYlu-sCKuqdouH-B7lYAzaawVQGYNObh0LFHxEp0ZxXTVgB_07QvKewg-0hheZ-_GIvignxSZmTRv0ccXlQd5RHkcBU9Jy73xtC70Sl8Fl1miUPYZzaX6pGldNkseAKU4r6INt50b_eq6GPR70jaDJRlTHYLVJsrdZ_Vxg1ntDLbrl5VLJskIizGheqddyEfXdw_FQQ9YDYrbE9Ch-fYdLBdUSwO3-XN35Kps62Uo113Hz_9w_itSKFdcfvJcN4_nAVlfM9ghPBU967y1triG4W4QAIySb4T8dOBeX7jWzG7WfQMPLqt6Y1FTvaxVLz-dQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7453" target="_blank">📅 12:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7452">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">جزوه ساز پرومکس
❤️‍🔥
از این بعد لازم نیس سر کلاس چیزی بنویسی، فق کافیه فایل صوتی کلاسو بدی اینجا و  با کیفیت ترین جزوه ممکن رو تحویل بگیری!
📝
https://github.com/faithsaly5-stack/Study-Note-Maker
تست کنین نظرتونو بگین
❤️
⚡️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/ArchiveTell/7452" target="_blank">📅 22:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7450">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پایان دورانِ عذاب‌آور جزوه‌نویسی دستی!
✍️
یه متد خفن طراحی کردم که می‌تونه ساعت‌ها ویس و فایل صوتی رو به یه جزوه‌ی تمیز، مرتب و آماده‌ی خوندن (Study Note) تبدیل کنه.
✍️
فرض کن ۲۰ تا فایل صوتی داری (مثلاً ۱۲ ساعت ویسِ کلاس یا ویدیوی یوتیوب) که نه وقت می‌کنی همه‌شو گوش بدی، نه می‌تونی کلمه‌به‌کلمه بنویسی. با این روش،
بدون اینکه حتی یک نکته از قلم بیفته
، کل اون ۱۲ ساعت تبدیل میشه به یه جزوه‌ی شسته‌رفته!
🤩
فرقی نمی‌کنه دانشجو باشی و درگیر حجم سنگین درس‌های ارشد، یا دانش‌آموزی که وقت سرخاروندن نداره؛ این ترفند کلاً سیستم درس خوندنت رو عوض می‌کنه. کافیه صدای استاد رو سر کلاس ضبط کنی، بقیه‌ش با این متد!
🎙
دارم یکم دیگه روش کار می‌کنم که حسابی کامل بشه. اگه پایه‌اید و می‌خواید امشب تو کانال بذارمش، پست رو لایک کنید تا انرژی بگیرم.
☺️
✈️
ArchiveTell | S</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/ArchiveTell/7450" target="_blank">📅 18:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7449">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwAER4TRc4tBPJqqLqiJPple9oOfpr_gVAac-M-dWsBtrQErb9x1n6LgvBQOQkn-u-b-QKZ3L0Jp-d-lkgxjWq7T7cHDbHhinXarpsvXv2-NvAEss91If5VQ6PAjKZrdxLpVG7UmrFxU4OcblJrMgCAWzMqVh02NCKb1PxhM2icipmx9C0x1vcGz-YmPvMAtAFenSXMkY03rTRMJF9Gny3N4FLVse6W_7pvQ2X9jWHh5Y_ppeKF-R-q1YeQIuyFQVDWaiBySzZk6R6vCDr9wYcf9Og1DAiWh2g3cmwaCwV1B2CS14SHwKF_ZX627LA2KSu3m27weOKDdQ_UZOh0ZYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://tabitoken.com/v1
قابل استفاده در
Vega Agent
✅
🎁
با هر رفرال شما
20 دلار
و شخص دریافت کننده
120 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/ArchiveTell/7449" target="_blank">📅 18:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7448">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOViOuYO-ZTMs2qTpAHnuUUIsQb8FJKCD0vI8aa56f6iKo-wa5so3iXqdgpGUZU6wmD_qlN6ZQBbvjHCsl_nZHDUjP0UYe7zlz1ttA6KQ77vQCSkXQNsH8WcHb8E3y0qDA3zS66-LuXFdFbMID1v2DNzFVS__fNXMloMIJX3U_UlsLkaj290DGxclK5amzqIvZy37iyQwLJMPwj4QLrufqYjv5oziGO1ZxliAWlhOemCa5ts8NcAtqaR_E6hZXvTkPq1bq7DTK6WS6FZoN9m9n723gqNvdMwLoxeTox_fILuRK2f1kzuxkKVmjZUY-TPwcOtAibZfz0zj7lWFpzW_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20
دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
GPT 5.6 sol | Mimo 2.5 pro | GLM 5.2 | Gemini 3.5 flash | Deepseek V4 Falsh | MiniMax M3
✅
برای فعال‌سازی فقط کافیه یک Gmail یا outlook داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://fapi.leileihog.top/v1
قابل استفاده در
Vega Agent
✅
🎁
با هر رفرال شما
10 دلار
و شخص دریافت کننده
20 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/ArchiveTell/7448" target="_blank">📅 18:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7447">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dU07k7zTI6a6xlKTsFLDeXJ4jB1MNFPlCSf3XVZBq2VSxM5x7rsJbQlS1VFay0CnIX3RTqYJ3mCDTnJdbvG-93s1qvtiA_-uw9U8hZf4i5Saew-x8kC_lBBWv82fm-btaSmQvy3Zz1hRKkze0Y5ExMHH-lP_TITA9XXZV4EfBKs22RAGMPAHGWUncl9oc8Gpvx1qSu2ytAYuWYg3tqs4AteC5XYEWU-kBGiYUb4rb4xshDlFoZbaYGYYzsVcETbkwZv_moa22o054rgt4j_meXEXpbUYM5sAjLcFH0IsS7XBwsAgYXMaIGVT6mYNnPWfrwK_dWSYhdKLPuzhCn2X4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10 هزار کریدیت برای دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
GPT 5.6 sol | Opus 4.8 | Deepseek V4 Flash | Kimi k3 | GLM 5.2 | Sonnet 5 | Grok 4.3 | MiniMax M3 | Gpt image 2 | Seedance 2.0 fast
✅
قابل استفاده در
Vega Agent
✅
Base URL:
https://www.getunikey.ai/v1
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/ArchiveTell/7447" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7446">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8QfciBH1t0WN8rz-y20cAXsh5PCWRwJH6fbhclelLgC2JewJ4KsdKAPuJlQBpNJY2x_GZevwct36m2iBLK9PeGJN5J0O77aHEA5RTT9LTOKx1-Z9VhzZHBpftOJjC-4AAkAdX-J29U292bp--cREU3bmQpOzs0WIvoxAwyMjwbJG4pKBk-UK5zwwY9U8JmdRonIoa99wN4HYHL87_Zx82WRuscIw0FSXrmK_QrfZm-Ae6UQmhz8uEG9azwrrzsz-EXeHxuYU9c3HM6-7eBh0CingegeGcJ8jMqAdQVCnvtGCAN97mcwWvqN684e0ENNrll5QykZogKDtZzWUDybNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان نامحدود به برترین مدل ها برای چت کردن
⚡️
🆓
با این سایت میتونید به 35 مدل هوش مصنوعی به صورت رایگان دسترسی پیدا کنید از جمله :
🚀
GPT 5.6 Terra pro | Grok 4.5 | Deepseek 4 pro | MiniMax M3 | Gemini 3.6
✅
🚨
توجه برخی مدل ها مانند GPT 5.6 از کریدیت شما کم میکنند ، این سایت هر ماه 3057 کریدیت به شما میدهد
💵
😎
🔗
لینک ثبت نام
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/ArchiveTell/7446" target="_blank">📅 13:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7445">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">💥
🍌
نانو بنانا پرو نابود شد!
کمپانی xAI مدل Imagine Image 2.0 را معرفی کرد که با قابلیت‌های خیره‌کننده، اینترنت را منفجر کرده است:
🚀
🎯
پیروی دقیق از پرامپت بدون افت کیفیت
✂️
ویرایش دقیق و حذف پس‌زمینه پیچیده با حفظ شفافیت
🔗
پشتیبانی از ۵ رفرنس به صورت همزمان
✍️
رندر بی‌نقص متن روی تصاویر
📈
آپدیت و اسکیل عالی تصاویر
این مدل قدرتمند هم‌اکنون در Grok در دسترس است!
🔥
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/ArchiveTell/7445" target="_blank">📅 20:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7444">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=X8If5wKGV-iAElW_508UlvfDH7fVUjWzpvpkq1Lme5SpQDDsKD6mYTOn9bTt9csJncXj7R-zOB47UIicrA0oZmwXj_f0M43-6C7iI_3BpHSC-lgwpjy6LujdkBYZQeuBjAtBWniiyNdeoLOcHCH9fXKZsjKscuMbrkACr0vW01QYy5-5C6nKVmyqnfGlieLUhLwwHNPPo_LqDDH9JbZrqWiLbIdWaryh1b-SDcA7GRBSiV7Roo7emK6DSm1hiivhjeGTZDCtSfy-5KYgKJ_qiDGJXjRiHcgRi4dIwZ1bRtiYK8wAJgUgzlHIld1AcJERX-EB8S0mk_JCwcBdWbawHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=X8If5wKGV-iAElW_508UlvfDH7fVUjWzpvpkq1Lme5SpQDDsKD6mYTOn9bTt9csJncXj7R-zOB47UIicrA0oZmwXj_f0M43-6C7iI_3BpHSC-lgwpjy6LujdkBYZQeuBjAtBWniiyNdeoLOcHCH9fXKZsjKscuMbrkACr0vW01QYy5-5C6nKVmyqnfGlieLUhLwwHNPPo_LqDDH9JbZrqWiLbIdWaryh1b-SDcA7GRBSiV7Roo7emK6DSm1hiivhjeGTZDCtSfy-5KYgKJ_qiDGJXjRiHcgRi4dIwZ1bRtiYK8wAJgUgzlHIld1AcJERX-EB8S0mk_JCwcBdWbawHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهندسی معکوس پروژه‌های گیت‌هاب با GitReverse
◀
☁️
بچه‌ها اگه یه پروژه خفن تو گیت‌هاب دیدید و خواستید دقیقاً همون رو با هوش مصنوعی (مثل Cursor یا Claude) از صفر کدنویسی کنید،
gitreverse
خوراکتونه!
🔺
چیکار می‌کنه؟
لینک پروژه رو بهش می‌دید، اونم کل فایل‌ها و ساختارش رو آنالیز می‌کنه و یه «پرامپت» جامع بهتون می‌ده. حالا کافیه این پرامپت رو به AI بدید تا کل پروژه رو براتون دوباره خلق کنه!
🔺
ویژگی‌ها:
پشتیبانی از مدل‌های مثل Grok-3، Gemini-2.5-Pro و GPT-5.4.
🐱
دانلود سورس‌کد از گیت‌هاب
🌐
سایت رسمی (نسخه آماده استفاده)
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/ArchiveTell/7444" target="_blank">📅 18:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7443">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فرار از زندان برای مدل های Sonnet 4.6 و Haiku 4.5
⚡️
💥
📣
🚨
حتما با اکانت فیک تست کنید
برای دریافت کلیک کنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7443" target="_blank">📅 17:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7442">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فرار از زندان قسمت 3 رو بزاریم؟
تو این قسمت Sonnet 4.6 و Haiku 4.5 از زندان فرار میکنن
😁</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/ArchiveTell/7442" target="_blank">📅 16:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7441">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfhm4OgXPtMyEvqpAkszt-YEwrHTZapq-yMwgDEKQNeKlxsojvdBAHhelnZ-79SEe0xCa9ZVTsWEbsbrJuXdK83Bn_Qg37YyX26Hki9UsMTK-600D4qg8imr6KxO66l1p4UK34S5BOmb8r84-SJA32gUZjAevdQ23s7R8Po9L_KVoBaiO_0Ntzl27K2TSUncCQD_o9tMxEYOnqmB01f81Ol1dIhHzrAaiSRQHSptIJRzR_lH7M3xH2emjpDQYMcMBFlepzSHU_fDmMpO1HLybMiEb2KmP-NZRjGlIbv2tVumGY7jfI-60itPbMzyHgITPZBP43YFaeZ_mgg-XnDffg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
با این سایت میتونید 5 دلار اعتبار رایگان برای بهترین مدل ها دریافت کنید همچنین این سایت 3 مدل کاملا رایگان بهتون میده
💵
😎
Kimi K3 | Deepseek 4 Flash | Mimo 2.5
✅
Base URL:
https://tokenharbor.ai/v1
قابل استفاده در
Vega Agent
✅
با جیمیل وارد شید سپس لینک ارسال شده به جیمیل رو باز کنید و 5 دلار رو دریافت کنید همچنین تیک Free models enabled رو بزنید
✅
🔗
لینک ثبت‌نام
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/ArchiveTell/7441" target="_blank">📅 14:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7440">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">فرار از زندان برای مدل های Gemini 3.5 و GLM 5.2
⚡️
💥
📣
🚨
حتما با اکانت فیک تست کنید
برای دریافت کلیک کنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/ArchiveTell/7440" target="_blank">📅 22:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7439">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">شرمنده دوستان
😢
بالا باشین
تا چندی بعد فرار از زندان flash و glm رو میذاریم
❤️‍🔥
بدون رفرال
🥹</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/ArchiveTell/7439" target="_blank">📅 22:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7432">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=X8fm3nMtvIolviNuu8vjrH12Sjhe4_H1TtiTINvGzTf6XXou3hg-H29-BypSuq1pFX-gsjAqe8qJ6Fo0XUzPWu-TSWa3N7qZG_X4ekAHmmV6W8JtIVZ89ClQPm5QWX-gjCUUc_t54JMV0BX1e5r1fh5AmJ5Cfy74dGkioADMYUulRTQyNSJuXTDH0k-JAwbH3XQtcavyc0O0YNDISuS3iyAJ2o55lJDOia1dB78na8PJD3jv2QFKJASjGRXjamYYlC9Bi6QGUlrcAWeMmcXvpUajnP0HXakobD1qRSY_tQT98O9aMnEjePGS2FvcfxKIq4JB2O_tMsVPa-0SG_Xm3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cccad37b4f.mp4?token=X8fm3nMtvIolviNuu8vjrH12Sjhe4_H1TtiTINvGzTf6XXou3hg-H29-BypSuq1pFX-gsjAqe8qJ6Fo0XUzPWu-TSWa3N7qZG_X4ekAHmmV6W8JtIVZ89ClQPm5QWX-gjCUUc_t54JMV0BX1e5r1fh5AmJ5Cfy74dGkioADMYUulRTQyNSJuXTDH0k-JAwbH3XQtcavyc0O0YNDISuS3iyAJ2o55lJDOia1dB78na8PJD3jv2QFKJASjGRXjamYYlC9Bi6QGUlrcAWeMmcXvpUajnP0HXakobD1qRSY_tQT98O9aMnEjePGS2FvcfxKIq4JB2O_tMsVPa-0SG_Xm3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمدید فرصت ساخت ویدیوی رایگان با Gemini
♊️
🆓
بچه‌ها گوگل مهلت استفاده از ابزار خفن ویدیوساز Gemini Omni رو تمدید کرد!
جزئیات:
حالا تا
۱۱ آگوست ۲۰۲۶
فرصت دارید که
۱۰ تا ویدیو
رو کاملاً رایگان بسازید (قبلاً تا ۴ آگوست بود).
❓
چطوری؟
تو اپلیکیشن یا نسخه وب جمینای، برید تو منوی ابزارها (Tools) و گزینه «Create video» رو انتخاب کنید.
جا نمونید، برید تستش کنید ببینید چطوره!
😳
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/ArchiveTell/7432" target="_blank">📅 19:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7431">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjeVfHly3WHR4d_fzxiarLqnYuUVpLCbhPoTHJ6TbBHVf1UsAR6Z3VaKGxt0n5dvTaUHtVL9nzDVqb3LsI-FbEZV7SBOTc40cmZXK8jqYfrdWQChtQnze5_Na9LIJkcgJJ5tjqXw-x7xvRqD2IuLJ8Nyc8j0dil47_rivmJyRIFGa8vRirTr3C-tLFOUVUe5hSchkLbEN8gkcJBuXT1XSIEcG5KyAKUyFxmxciSCpd-c1SHOK3E9mOfE6gFVFAw6on0iltM9pp40NP5xpOyJuV4E-0LqVMbf4Cc5OiDq1qaZJ-6lkqv-IP70RA2KbXQyxGyXrZXjAT7M9QX0lb1YnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن خفن و متن‌باز بدنسازی با openGym
💪
💪
اگه از اشتراک‌های پولی و تبلیغات اپ‌های ورزشی خسته شدید،
openGym
یه جایگزین رایگان و کاملاً شخصیه که دیتای شما رو تو سرورهای غریبه ذخیره نمی‌کنه!
📌
چرا باید نصبش کنید؟
💠
دیتابیس کامل:
بیش از ۱۳۰۰ حرکت ورزشی با انیمیشن آموزشی.
🗺️
نقشه عضلانی:
روی تصویر بدن نشون می‌ده این هفته کدوم عضلات رو بیشتر درگیر کردید.
✴️
پیشرفت هوشمند:
خودش حساب می‌کنه جلسه بعد باید چه وزنه‌ای بزنید.
👾
بدون نیاز به پسورد:
ورود امن با اثر انگشت یا چهره (Passkey).
📜
انتقال دیتا:
می‌تونید تاریخچه تمریناتتون رو از برنامه‌های Strong ،Hevy یا FitNotes بیارید اینجا.
✅
صفحه همیشه روشن:
موقع تمرین صفحه گوشی خاموش نمی‌شه تا راحت رکوردها رو ثبت کنید.
💡
نصب:
می‌تونید فایل APK رو دانلود و کاملاً
آفلاین
روی اندروید نصب کنید، یا با Docker روی سرور خودتون بالا بیارید تا بین همه دستگاه‌هاتون سینک بشه.
☁️
دانلود APK و آموزش نصب از گیت‌هاب
🌐
نسخه دموی آنلاین (برای تست محیط برنامه)
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/ArchiveTell/7431" target="_blank">📅 19:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7430">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecNs0NfZC3_kLaMRTec-4tIpbLo2jcZHwX4Tu4s8qVfx1PquFUlPMLcAHYB051O3G-y-EPFdwAZGzMoh1dVeLF0wAZiD5Igv6XxRKcXalXoekmpEvy6mTbchVY5gWADyTi7VahekBT8yFVI7HmW2Yg5Jh8gJeO2GyaUZKjftLR20b0i7CalIMDHzeKRkwdsgXd3cfyBDgXIxFMHkLE3T3qtIbo9V95vQcVWROdLLrPb8Rp1rO8JecRWxAXZW3YSEjJqJVe9EGkKNjmL4PxM8lth3d7pX7El6iQNICO9ez1pd88qBkoXer6rcL2v8pTt8K9SXo-lbNGsf-POAvqOuLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😺
چت متنی داخل ChatGPT نامحدود و رایگان شد.
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7430" target="_blank">📅 18:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7429">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnIPtbw9OQbDljgvY_St8X9R89cI_t_bbJtc_NZjaHDjJvxTdFH7QeNqgKJ7DcxNUnfQZ57MLXZKd8HgKz5RskvoZraJZifmZ2qUrscBIicSc7lGFpC5238RhJuV6LdLiShvigZQsQswaeYiiHccWu2hxlfMmp2x71bIMyhYgZzphLbiuOwTtETOd606IFbUMqLnFijO2bTeJWAt55Rj62teWb0dq4Nn6Ez5l2bKBpybZ4zDrmZio3-_LOGfN8Zp50tBYUE24TVDKNcjj3ZMAi9dipGqkv_mELgUzcEGNJHu7RbJF7lGRDcDCYfiWQmX6omKgOcovPR-ZoRwLa6kIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
🆓
دسترسی رایگان 14 روزه به GPT 5.6 sol و Claude Sonnet 5
​سایت و ادیتور Zed اشتراک ۱۴ روزه Pro خودش رو به همراه ۲۰ دلار اعتبار رایگان ارائه میده که به ۱۶ مدل برتر هوش مصنوعی مخصوص کدنویسی دسترسی دارین.
💵
😎
​
📌
مراحل دریافت:
1️⃣
وارد این
سایت
بشید و پلن پرو رو پیدا کنید و تیک Free trial رو بزنید
2️⃣
استارت رو بزنید و با اکانت گیتهاب ( قدمت حداقل 30 روز ) لاگین کنید
3️⃣
از داشبورد برنامه Zed رو دانلود کنید ( برای اندروید در دسترس نیست ) و تمام!
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7429" target="_blank">📅 15:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7428">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8f426714.mp4?token=tUEbBJNvjgb_9_JepwM4tht_RPQAdlpC3-Q-dWOV6phffFj_C0tcBgRI2G0hZ_b5ziDOC3MwNXi_6EgIRskV6rdktU5zCSqfbrPyMPEzuDh3jFqAtfo--BGsHXe-rLY7O-d0B26lmmqnk-ehwoUdsLkvi3x4gTwCQfc-XWYuSd-D1d-Jc_4MDevD9ewgr_JHkSJUxsyA4TN6ELcS7-_dSrHQ5pJKwe6YzN8-LMit96tRfuWBDVJ11P5D-KZuu0FAYnSG3O0of7VVcqAq22jRGFQok3IOC_fyAaadQystThJplgezgbeppIgVI_tEdyNk3Y_ruLZFK_k_bZUO63Z7vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8f426714.mp4?token=tUEbBJNvjgb_9_JepwM4tht_RPQAdlpC3-Q-dWOV6phffFj_C0tcBgRI2G0hZ_b5ziDOC3MwNXi_6EgIRskV6rdktU5zCSqfbrPyMPEzuDh3jFqAtfo--BGsHXe-rLY7O-d0B26lmmqnk-ehwoUdsLkvi3x4gTwCQfc-XWYuSd-D1d-Jc_4MDevD9ewgr_JHkSJUxsyA4TN6ELcS7-_dSrHQ5pJKwe6YzN8-LMit96tRfuWBDVJ11P5D-KZuu0FAYnSG3O0of7VVcqAq22jRGFQok3IOC_fyAaadQystThJplgezgbeppIgVI_tEdyNk3Y_ruLZFK_k_bZUO63Z7vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چت‌جی‌پی‌تی رسماً تبدیل به فتوشاپ شد!
🖌️
⚡
ادوبی یه پلاگین جدید منتشر کرده که ۷۵ تا از ابزارهای حرفه‌ای خودش مثل Photoshop، Premiere، Lightroom، Illustrator، Acrobat و InDesign رو مستقیم میاره داخل ChatGPT.
😺
🔥
کافیه توی تنظیمات چت‌جی‌پی‌تی پلاگین Adobe رو فعال کنید و با نوشتن Adobe@ توی چت، از تمام این ابزارها استفاده کنید.
✅
این قابلیت از امروز برای تمام کاربران در سراسر جهان فعال شده!
🌐
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/ArchiveTell/7428" target="_blank">📅 12:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7426">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFAWjza97MxMNdR_HEG5_p-TpQeLKHZEjgcQOm35YUGcTgkI2cYAZnPhq3AnwecPraLTXA0OAtxRxrrnzP7euVN7Xvo1ZTVNqlZI12fwHVSk7cIMqq5V3CYmKnw7AbcVdDAFy68dc0JU5Jg3TTFL1sP0UgylzFNL80lWUYmgaHN2iCqdfpSb0PehAhmZ5dxfJ8ZaOTQL7WJMMCf0LhRvptdZlXTXFRenyyIwDXhyLln0Vjm3G91j7Xly75j26xhYhLLdmChvvEhE8INs6EOk9zwWiGusWJ6n5JQWsnzFjaB6wtzxoN5l_mR1mr3-jrIhCXnTbu9Kd_7YzYc7j8wUAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک ساز خفن گوگل
🆓
🎵
🩵
با این سایت میتونین با یه پرامپت موزیک و موزیک ویدئو های خفن بسازین و منتشر کنین.
با لینک زیر ثبت نام کنید و ۵۰۰ کردیت رایگان دریافت کنین:
🔗
FlowMusic
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/ArchiveTell/7426" target="_blank">📅 00:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7424">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghRQx79Mn_iNe48lF6J68g79SXIQQbxR-J7FTSSGcETXEPIJR2VTjkXzM2Yppdg_CCdrgxxKzIg7WReIQ5g8HibXuT64LDEeL1pL6hSg6z6SD5M0rq3X2wQZLaWwBZU5nvvH4pv2RxMZCYtw17IfliP5mVtMiXKlIoOdZj6GWsx8zR0uhuCwtwSUoXTsewZ_la4Jbp4rYJUbL-Cf0cnVEeOhoi0iNILXoFTkyjJZ0SYLC46yJcPqkSCWIeFTzbO5SXHFqBP9GyxF8z8tYa2OodiJ_LqHvM9SdvM1xaM096AjqP5lDKFEBFPIOyCx5jo7rkP5lS2LtFlS-3_VWPS4Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1500 کریدیت برای دسترسی رایگان به برترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.5 | Sonnet 5 | Gemini 3.5 | Haiku 4.5 | Gemini 3.1 flash lite | Nano banana pro | Nano banana 2 | Nano banana 2 lite | Gemini Omni flash
✅
1500 کریدیت برابر با 15 دلار برای 7 روز
💵
🗓
برای دیدن آموزش کلیک کنید
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/ArchiveTell/7424" target="_blank">📅 18:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7423">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFlKR1j7drDEsE15sbnyG-bJYUJ3buspuHKyZgYD1mNMthiiSKfZ80m8JVYmOURAgF0YCcb-VauSKmch2SAgn4kKwQygVnQaafXwb6LXfAlCGPu0xQA0Hbt3ErUpNHlb3qvu3aGjoSIZ0w0g25qMv-WaKA_co5glqjvVxcytQMMci3m9bxEz7GwecdANych3T4eKpQ8V0oiokJVqE1NY9aHDghiaI6rXxRQpX0I9MTvGurAKEeNIQ2CitAYIPI91yDsCqMRSuUYyko7JAyvauQjcbN0U0zaT49aXZLgdSpwsYS5jccsizUrrGOnpo3E6YQJGCrFfKwDdQutqhTEWHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به Kimi K3 و Qwen 3.8 Max
❤️‍🔥
🆓
بدون نیاز به کارت اعتباری کافیه وارد
app.clusy.io
بشید، با ایمیل ثبت‌نام کنید و توی پروژه جدید مدل مورد نظرتون رو انتخاب و استفاده کنید.
😎
⭕️
فقط ۲ روز از این فرصت باقی مونده! به دلیل ترافیک بالا ممکن هست سرعت سایت کمی کند باشه
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7423" target="_blank">📅 15:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7422">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXZJcgou97UlXH7HY1VZf1YFS8m7xtIMlc3N-NfrNp2xdU7cC85PRvgljv1Td74Bj1fFe17GcGGjF9uDdYuvzSGE_6nTw9IqNF9Zy6xXzSeObuvV1zTdNcY0eFTffSf7OXqEuE-ggIbIZW96MXi4Xuy0MX-PItCJGx-1UIOY_xd8rbtN4O7B-HhLOsrdn1w5SU22iLgTEpdzn2e49VLb74GfmnqUEnmX8sISd09S4fSlOIEt4fuaMTOJeuQLRyZQPF1kRXGk2l0ARs8028zggxjd1m7k_Uc_C4NiFFEsJxav0McVDoDGMDibwB7BJLeVsT77QLRaWta8W_UwcX_j9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان:
امروز از ساعت 12:30 تا 20:30 به وقت ایران
⭕️
🛠️
مراحل راه‌اندازی سریع:
1️⃣
وارد
سایت
شده و با اکانت Google ورود کنید.
2️⃣
به بخش Account رفته و اکانت خودتون رو از طریق تلگرام فعال (Verify) کنید.
3️⃣
به بخش API Keys برید، یک کلید جدید بسازید و اون رو کپی کنید.
4️⃣
برنامه OpenCode (یا محیط دلخواهتون) رو باز کرده و اطلاعات زیر رو تنظیم کنید:
🔺
Base URL:
https://api.aigate.shop/v1
🔺
Model:
muse-spark-1.2
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7422" target="_blank">📅 13:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7421">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4Xe1EbUrVFbP5mhvVyr4btKD_RslEAa0t5HNKvTDI-chHUKfdqmJMraTjMWEgJJuTjKS6WPEC2-bsubFYI4Ub7WKH_a1gEFD9x_15CdqEIDeovqF6IMZcQCLgYGEgB8YcH4f8BkeXMch_2_T37i--uYGSMmlBKgrSL4hkWdzGVoOdVmjDWxMmfzdxVBwTA8yqK2BVaFJGU-C2c7p5DZRbNj_DwJZILXpWwjXF-vBiT2nnCmmFjH_z2pQ3FUExDQeBnbIxCwSrJx1dUbZv77ZYjEMqSWQouIHBw2onwdzw4s7vV0CFzKu5lx4SLIwqowSJBUWklVXD-XVv51e4l7Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ‌سیک V4 Flash
به‌صورت
نامحدود
و
رایگان
تا
پایان
سال
6️⃣
2️⃣
0️⃣
2️⃣
به آدرس
cnb.cool
مراجعه کنید
➡️
هر
ریپازیتوری
که خواستین را باز کنید
➡️
عبارت
@codebuddy
را تایپ کنید
➡️
حالت
Work for me
را فعال کنید
➡️
تسک
مورد نظر را وارد کرده و اجرا کنید
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/ArchiveTell/7421" target="_blank">📅 13:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7420">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اگر دنبال کانفیگ میگردید و حال و حوصله گشتن ندارید یه بات پیدا کردم خوراک خودتون
😆
میتونید با رفرال جمع کردن ، گردونه چرخوندن و دیلی چک سابتون رو شارژ کنید
⚡️
🤖
@survpnbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7420" target="_blank">📅 12:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7418">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNHxzK8rff2yBKqBApTDeh0Y2MBD1UOvwKV7gIEfEhnoVUbDaZWe3qYLpbcw9G_9f5cyAyPk2lpWpq75GkngtfrId9OAAop1izTZpqkv9biuSNE9234mJnRjNw1dKFAmT80QmGz9xAqdMdEwIRZRm6BaOty9RBvv906fF_NaRZMSogDc-fs-sQQhOLnyBO1deXuBX3s6mf5VVzT90YOmZu7WlBy6GUzKr6vHJd9ubNzlNfWo_2N8Io5Ikz_pHCgdvZm0pMxBf624Xe9apdhTvSHH_cnyV8O8foS4DvGLsJLpRHohzcBJIi1OfeTMAK2jQaVTyChG0IWF6Qy9UUFWAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کامنت یه کاربر زیر پست تلگرام در ایکس:
من آدرس مخفیگاه پاول دروف رو می‌خوام
😕
💯
اکانت رسمی تلگرام:
مخفیگاه رو که نمی‌دونم ولی من رو می‌تونی تو خونه پیش مامانت پیدا کنی!
🙈
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/ArchiveTell/7418" target="_blank">📅 00:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7417">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIgA4_I2EANtSQZVeWV1nN0UGMsiLAyIkwqPL2iUWzt64n8ja_n2XcQEp3lKu7zQ8ZPyO2608TDzAH6H0yc8x-iNF0QH3FlItLgG5I67CG597icGt5i-egx47-retT6tih29AEDDAMQYHr3o0ZFq96v6ij8KC1w23-wO7adlwcGCJW2ZZz2Sw1tJnBZsKTruD1AX2e3H2e5HU13KjKI2T2Uy76sSPKVmHu5oj3XY2TVI2Nj1XcTySWzOiNwibpRM1WsKR_wyXIETggC7IWQlmY9Uma3Ds8og4Y8Jd2Rh4Vnld4DjdvSNJ-i2FNK94BcKy9BX3Uxc_w21JSo-vPPBKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف فوری واترمارک تصاویر و ویدیوهای Gemini
🚀
🔥
دیگه نگران علامت روی عکس و ویدیوهای جمینای نباش؛ با این ابزار رایگان خیلی راحت حذفش کن
❌
😎
✨
ویژگی‌های کلیدی :
1️⃣
100% لوکال و حفظ کامل حریم خصوصی (بدون ارسال به سرور)
📶
💯
2️⃣
پشتیبانی از عکس و ویدیو با کیفیت های 720p و 1080p
🎞
3️⃣
کاملاً رایگان، سریع و بدون نیاز به نصب
🆓
⛓
لینک سایت
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/ArchiveTell/7417" target="_blank">📅 21:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7416">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJE6QkjMfFLkMLwGuFXL2AYQYfe48_43ZP9pbDWkY1tVgMzyJ7Sq74KCa4r3KDANVkuIZtD535LKf7c6apS0SkyBqnS9EpIkg9mu2_FpxgFVLiSWEUx5M3bG_kTs-AIjx9AgLetKySuYWDAAv3HrHjOpl1rOapypdBovi3Lhk2NbEbH4p6-5g6CjUF6GTj6kZvMrEsPv9gQ_ZpdJSpJ7G1s6-XL-0eofXnmGp106XXPVWv7czfhR-bw26LdY92M2dwQEJ6_FJ5cvSh__j-T9aPvQsz-AVg3PO3PveIRHLxrggxzfYQK3GDA6hAkJYRpCswtMNLnJmYJnYnlwLjq_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت رایگان ویدیو با مدل قدرتمند Seedance 2.5
🎬
🆓
خبر خوب برای علاقه‌مندان به هوش مصنوعی! سایت
Dola
مدل Seedance 2.5 رو به خودش اضافه کرده و حالا می‌تونید هر روز به‌صورت رایگان با این مدل ویدیوهای جذاب بسازید و لذت ببرید.
🍸
🎉
✨
ویژگی‌ها:
🔺
تولید ویدیو به صورت روزانه و رایگان
🔺
کیفیت و قدرت بالا در خلق ویدیو
🔺
استفاده آسان و آنلاین
🔗
لینک سایت
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7416" target="_blank">📅 20:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7415">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uON54inYW5oeTyauSTCyMIuY_LqErNjg4JwVLKIyeHw5V_7lFGcATSE5k8ddSywaUJuYqYd3qaAZLsH9ghx3jofmCYFhJm7vFcq2PJizQUSbt52-5mSH2iUYZ2CcmLZzR7SM6MQicekQ5kUqXzJlDsBIQaSPLR5rVp5rtQ3g04K3Ww_swg2JAgr2RmlXpqY4-yRSg9ArjFRKXJijrkgfvmk-7hRh0GCTfSmUv-Ucd9BHQML9ZgJNfvAAsc3-evyF8e42xVIhaaFzu-tpmQfmL9jt9VSoMSAkXgK0SQpORDTl8bIS2WfhRW9A21_HWXyEaqoRu3kg-NFs7vmBKsRyDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
گنجینه API‌ های رایگان هوش مصنوعی
🆓
یک مرجع کامل برای پیدا کردن API‌ های رایگان مدل‌های زبانی (LLM) بدون جستجوی طولانی
🔍
✨
🗂️
1️⃣
freellm.net
بیش از 424 مدل رایگان از +30 ارائه‌دهنده با اطلاعات کامل شامل محدودیت‌ها
📉
📊
2️⃣
freellm.sh
لیستی ساده و سریع از سرویس‌های رایگان با نمایش وضعیت و محدودیت هر API
⚡️
🚀
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7415" target="_blank">📅 18:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7414">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSF1XDv9IgI_n7sSviTiR4wnRlh53OrpoBNg0kHOVimFEs8RbIfdjH9z7QS9_4i9LTiUK-DozQUBczu-bP_o0W7iKgTpvy--68IW8Iv5auiB1KVypgWlK9F7jOYQlCQ4QbFyMGRvAfOgHF-xCOy8oxVQ1L1JeTLjRLrQeiLgtFU2HIrGOGJYmJ_irTvfzUkflsOInMkUYRr6fmGnamce6qCKhASMAb3YfD3PDnKV7IAtjoGdjszTddz7QbD0afe4hJFxUqI8b2WzqUX2jHkLKZYsiyTrUspsE06Ccn1dh9IQLkHbs-vRe6_UMnrXwI1jd-ILwi08rS4PLbhlYgtQFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمینای اسپارک (Gemini Spark)؛ دستیار هوشمند و همیشه‌فعال گوگل
♊️
🔍
بچه‌ها گوگل با «جمینای اسپارک» رسماً داره هوش مصنوعی رو از یه چت‌بات ساده به یه «ایجنت عمل‌گرا» تبدیل می‌کنه! این دستیار کارهای روزمره و گردش‌های کاری شما رو به صورت خودکار پیش می‌بره.
✨
قابلیت‌های خفن اسپارک:
📄
اجرای ساختاریافته:
اهداف شما رو در قالب وظیفه (Task)، زمان‌بندی (Schedule) و مهارت (Skill) دسته‌بندی و اجرا می‌کنه (پشتیبانی از اجرای همزمان ۱۵ وظیفه).
🌐
وب‌گردی خودکار:
می‌تونه کنترل کروم رو به دست بگیره و پروسه‌هایی مثل جستجو تو سایت‌ها یا رزرو رو کاملاً خودش انجام بده!
😨
مدیریت ورک‌اسپیس:
خوندن و ویرایش فایل‌های Docs و Sheets، زمان‌بندی تقویم و مدیریت کامل ایمیل‌ها.
💻
کنترل مک از گوشی:
اگه اپلیکیشن جمینای روی مک نصب باشه، می‌تونید از راه دور (با گوشی) فایل‌های سیستمتون رو بررسی کنید.
🤒
شرایط و محدودیت‌های نسخه بتا:
❤️
فقط برای مشترکین پولی (Google AI Pro و Ultra) با اکانت شخصی (بالای ۱۸ سال) فعاله.
🔛
ویژگی Keep Activity اکانت باید روشن باشه.
❗️
فعلاً از زبان فارسی پشتیبانی نمی‌کنه و تو بعضی مناطق (مثل اروپا و بریتانیا) در دسترس نیست.
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7414" target="_blank">📅 17:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7413">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBf8Njz0MvYx8UNQMOnjhZSMhtVW26mn4AY7Hbd1oqYC4IK7QV-zPSNhKIFmOaR0UM6EDWN6vYZdi8buWWspHb_oQn4_OYT680wkewu7teY64rqMZVoIenLMsO7YlVndUR7Tu-pGM19c7VFtf_iM7PmGdZZYDkkkRmxb0tpeAPNS7zTxO5teBy1VKl2R3ibEWchDt4lJtg-wEx9qiDlAnLJyff74aN99dd3-Un531tiMxz0w0EPA_VKmx1ekDUovn7M03yDqPhkapXH7DL2WtVe1IS5EbapZZPqLgMWT68AAxA7ddZs80-zgTNO81NxPYEG-lrhAkOrNYhNbTsDZNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌اندازی سرور اسپیدتست شخصی با OpenSpeedTest
🚀
🌐
〰️
بچه‌ها اگه سرور/VPS دارید، ادمین شبکه هستید، یا کلاً می‌خواد سرعت واقعی کانفیگ‌ها و سرورهای خودتون رو بدون وابستگی به سایت‌های عمومی تست کنید، ابزار
OpenSpeedTest
دقیقاً همون چیزیه که دنبالشید!
🚀
این پروژه یه ابزار متن‌باز و بی‌نهایت سبکه (حجم اسکریپتش کمتر از ۸ کیلوبایته!) که با جاوا اسکریپت خالص و HTML5 نوشته شده و بدون نیاز به هیچ دیتابیس یا فریم‌ورک سنگینی، سرعت آپلود، دانلود و پینگ رو اندازه می‌گیره.
📶
👩‍💻
👩‍💻
✨
چرا این ابزار خیلی خفنه؟
🔺
اجرا روی همه دستگاه‌ها
✅
🔺
نصب بی‌دردسر
✅
🔺
تست فشار (Stress Test)
🔤
🔺
بدون ردگیری
🔞
💡
کاربردش کجاست؟
برای تست سرعت واقعی ارتباط بین دو تا سرور، عیب‌یابی کندی شبکه وای‌فای خونه (LAN)، یا تست کردن افت سرعت موقع استفاده از تانل‌ها و پروکسی‌ها.
📌
👩‍💻
لینک مخزن گیت‌هاب و آموزش نصب
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7413" target="_blank">📅 16:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7412">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔥
یه
پلاگین
به اسم
oh-my-hermes
برای
Hermes Agent
معرفی شده
🏥
این
پلاگین
سعی کرده چند
قابلیت
مختلف رو توی یک جا جمع کنه تا نیاز به نصب چندین
پلاگین
جداگانه
کمتر
بشه
✅
😍
از جمله امکاناتش می‌شه به اینا اشاره کرد:
✔️
هماهنگی کدنویسی و مهارت‌های codemode
✔️
سیستم مصاحبه هدف و پرامپتینگ برای برنامه‌ریزی و مهندسی حلقه (ulw-plan، ulw-goal و Loop Engineering)
✔️
معماری حافظه پیشرفته (شامل Dreaming، Pruning و مدیریت کانتکست)
✔️
سیستم حافظه لایه‌ای (بلندمدت و لایه‌های L0 تا L3)
✔️
متخصص‌های دامنه‌ای و قابلیت‌های تحقیقاتی
⚡️
تنظیمات آماده‌ای هم برای استفاده
سبک و سنگین
داره که می‌شه فیچرها رو
روشن
و
خاموش
کرد
GitHub
🐙
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7412" target="_blank">📅 14:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7411">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4JuVXwLJEWvyAjmyUMUG58F2Vga8zRJcsFm921_FvGjVSOzLL4nCdvAjPzkl3z22UG_EIP3qjYQ6_fFo2be4Ays-3HDR_eBTj80zC71DhvW1ULSU5R5AIl38faSX6MqO1zVAA5aOFqlt1Jfhx5lHoqFsRKMPakWP4Zlo1rnARaYNxpD9f6blLYnTIXR0rBpr9Apa-eSw30iT4lEu2pmpZ6CXZw1OKWODQDtT15PKlkiZ1LTp-_brt-25KdIV_sy2242nOdL-Hos1JTb3vltu20quYx0332XRkBNGmZ-ElwI0HidxXmsPwFfKbHHecd18ZMJ2pdzIQS4jVtCkCzSBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱ میلیارد توکن رایگان  تا ۱۲ آگوست
🚀
🆓
پلتفرم
InferX
یک کمپین محدود راه‌اندازی کرده و تا
۱۲ آگوست
امکان استفاده
رایگان
از برخی
مدل‌های هوش مصنوعی
را فراهم کرده است
💥
از جمله مدل‌های این طرح:
😐
DeepSeek V4 Flash
😐
Gemma 4 31B IT FP8
😐
Qwen 3.6 35B A3B FP8
و چند مدل دیگر
😍
طبق پنل سرویس، برخی از این مدل‌ها با هزینه
صفر دلار ($0)
برای ورودی و خروجی قابل استفاده هستند و می‌توانید آن‌ها را از طریق
API
سازگار با
OpenAI
در ابزارهایی مانند
OpenWebUI
،
OpenCode
،
KiloCode
،
Dify
،
Hermes Agent
و سایر پروژه‌ها به کار بگیرید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7411" target="_blank">📅 12:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7410">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEDg4BdV-t2BexiQi0PCV1ZAelJ00LeKMW7xBSuhcSBli4mTmCrhKw01B0Sf7IBYRRy8Ea-IaEXsmH_ivyTyBy7kSORpS3V89ZIQBBaL29hBYC801ya1czOHSdz_P68HuyuoPEJLo2iks11TAYzPFJbMNwMqaj3LnexyQiA-OpvWdqYcHhGmf565lie5IYjauh8h5cfSd5Hu55pQ-aOmtF8g48SqAf_wBy6IwrgGpUnhvNfyFLweQxjbaA5wAiggz7W3Q_Tc0skiisiyblllCyWZMU_euyNxZlENzHRn_ZG-g6mxrSKDfrkEln9plFsRbxAwTBwOdz-r0BjPtSJhKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی CloudSSH؛ ترمینال قدرتمند Web SSH بر بستر کلادفلر
🎶
📱
پروژه متن‌باز
CloudSSH
یه ابزار Serverless و فوق‌العاده برای اتصال و مدیریت مستقیم سرورها از طریق مرورگره. این پروژه با استفاده از TCP Sockets در Cloudflare Workers، یه تجربه کم‌تاخیر و سریع از اتصال SSH رو ارائه می‌ده!
✨
خلاصه‌ای از ویژگی‌های جذاب:
🔒
کاملاً مستقل و امن:
پیاده‌سازی خالص SSH 2.0 با TypeScript (بدون نیاز به کتابخونه واسط) همراه با رمزنگاری اطلاعاتِ اتصال در مرورگر.
👆
رابط کاربری حرفه‌ای:
ترمینال سریع بر پایه (xterm.js + WebGL) با پشتیبانی از تب‌های همزمان (Multi-tab) و تم‌های متنوع.
📁
مدیریت فایل (SFTP):
رابط گرافیکی کامل برای آپلود، دانلود و مدیریت فایل‌ها با کشیدن و رها کردن (Drag & Drop).
☁️
همگام‌سازی ابری:
پشتیبانی از ورود با اکانت گیت‌هاب (OAuth) برای ذخیره امن کانفیگ سرورها.
🤷‍♂️
دستیار هوش مصنوعی:
پشتیبانی از API مدل‌های OpenAI برای کمک به تحلیل لاگ‌ها و اجرای دستورات لینوکسی (مثل Docker و systemctl).
🐙
لینک مخزن پروژه در گیت‌هاب
🌐
نسخه دموی آنلاین
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7410" target="_blank">📅 12:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7408">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ی پست ناب بریم
🔥
🔥</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7408" target="_blank">📅 11:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7407">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e45lQB2Q-7WUdQhyfvWXogyg5IXqOlN3yTUaO4CiNw3LvujQ280lqk-gToxpoB9rX23hUtX78r3hcDi2svIjNynnCng7pxKpFE63FVuciHQCn2VXwT8awLP4U8zUKXu0v-Yy4vquFacGfsR8nBXzFJ1fwMOP3eaN637dPJoOgv5ehW-naeKO9HVB_xJbYyfJmo-pjovpO0LacAIelBXvMUMMMF1mBSx7yfEANifK_hEkHsbrbF_E3WsyRUxSiP5AE6wrym1H8aUrc4VzlVZ3x33g7OsJtFO8TKSCMzA59QIK8N0b0fBPN4aqP_1IZAB4L5Yak-zpbXMztNosafLHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#fun
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7407" target="_blank">📅 11:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7406">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7406" target="_blank">📅 02:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7405">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=Tcr1lo_z_xlRmRVaz3KXKYeQzyLVHko9MYNBUOGJ-gT_ho6MtVh0NasROThRpD4T946iIV6IYbEV5_2Hq0p3qf0WCyGqfVE25MTV7j-n1eqAw2A_KhqNGXrDq5HmClnGMSswcAxztsuzb7zlyXVuAmaVIlEI5m3l3sXWOBxQFG2cFzl0bbk_cFhJk-UZlvpSGHmVw2Vz1rH_9yTZiZ6SVCrGTAhlhCKd28CnTT9ATCtwvmmLdVVboHURxY7tqWwrw7IiZ-jidOlKmR7NQphZRMPcfXgkpFlCU138-6tBc02q9OGW7TFCl9qI8KNnDQh_rargKgw3KKVI1f2KmHH0rTSlKM-6e4OqP-JOm7-x0AhiuIF9B6V5_50D863peYdMP6eDCU-AckpKJtbNw-nqmbq_i10EPoUB728g9TBzOEPogCIoCzPhlunmBp-3IIdoqIeGXKEhBoVN7M-EU8i8u3TfGooQK4e9y6xy00hdjXRNGnXq23q4PlfRV02gcoHquNCmX4_vAVFRBhe3tn3lNd-oKIOOpGV41U9mgJmZq1ZzhilVfvsm2ST4N2ABZ5PZHzLEOzjJ9n1AxG3OFbOr2U9OkLg6dxI1rQzMmEKtFIXSIifKlVRi9HmXVw_yyXrwGZicVeBegWq5SIBphr97mdNJao76S6fhCN5IsCg1Etw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=Tcr1lo_z_xlRmRVaz3KXKYeQzyLVHko9MYNBUOGJ-gT_ho6MtVh0NasROThRpD4T946iIV6IYbEV5_2Hq0p3qf0WCyGqfVE25MTV7j-n1eqAw2A_KhqNGXrDq5HmClnGMSswcAxztsuzb7zlyXVuAmaVIlEI5m3l3sXWOBxQFG2cFzl0bbk_cFhJk-UZlvpSGHmVw2Vz1rH_9yTZiZ6SVCrGTAhlhCKd28CnTT9ATCtwvmmLdVVboHURxY7tqWwrw7IiZ-jidOlKmR7NQphZRMPcfXgkpFlCU138-6tBc02q9OGW7TFCl9qI8KNnDQh_rargKgw3KKVI1f2KmHH0rTSlKM-6e4OqP-JOm7-x0AhiuIF9B6V5_50D863peYdMP6eDCU-AckpKJtbNw-nqmbq_i10EPoUB728g9TBzOEPogCIoCzPhlunmBp-3IIdoqIeGXKEhBoVN7M-EU8i8u3TfGooQK4e9y6xy00hdjXRNGnXq23q4PlfRV02gcoHquNCmX4_vAVFRBhe3tn3lNd-oKIOOpGV41U9mgJmZq1ZzhilVfvsm2ST4N2ABZ5PZHzLEOzjJ9n1AxG3OFbOr2U9OkLg6dxI1rQzMmEKtFIXSIifKlVRi9HmXVw_yyXrwGZicVeBegWq5SIBphr97mdNJao76S6fhCN5IsCg1Etw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/ArchiveTell/7405" target="_blank">📅 02:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7404">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAmBHwF7e0EhhoGcmpWrwFwi48bpkICRfxrVCGaL7SThj5v1_2hhItl4KDOvjx_nAhblbagBUGxmCv-ipRR3qPX2Z9ZunEP6y6-gVcsGjg_sgaCUyqd10lQqL56PvCF6tblEOXOdKJZVJ36cJKcmiNbdVGcBxxnqB7TTQlCjjkEIUNuoh7Om-BbDrk0RfJsLTAE1rPItRAvuDCY4n_P4A2p0V9oWvCWcHpVEaf43n_rqzjKE2rmExuKrVY-SGEYb61h3c0FWDPqWesjB6ePJtPoraCA91UodUPg7F-6bR2vxNO3pbjIRtyunu3xYmUGwADFO7OIV_NITVbzCEbPXmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎁
500 دلار اعتبار رایگان API برای شما!
‏همین حالا کلید اختصاصی را دریافت کنید و از مدل‌های Opus 5 و Opus 4.8 لذت ببرید:
🚀
Api keys:
sk-2UddB27hnFA1z2LKWKnq6BQaffBLe86FU0htxAHm0Q9n5vjW
Base url:
https://agentrouter.org
Model:
claude-opus-5
|
claude-opus-4-8
✨
کلاینت های مجاز :
🔺
‌Claude Code⁩ | ‌VS Code⁩ | ‌OpenCode⁩ | ‌Hermes⁩ Agent | Qwen Code | Kilo Code | Cline | Roo Code | Open Claw
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7404" target="_blank">📅 01:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7401">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">📥
پترنی ها آپدیت جدید داده
۲ ساعت پیش
چنج‌لاگشو ننوشته
https://github.com/patterniha/v2rayNG/releases/tag/2.3.2-P10
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/ArchiveTell/7401" target="_blank">📅 01:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7399">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSrs4lxST2ipW6AD1H4zoGFtlTHaBw5p93tDpVJt6oN-xtA7EhQsEeJocL7WLl3kflEOlzt352inqVLQHx2ea3IPSiLs5edOJEsv9EedmI-a6WcEufLc5FVz8Yk2q11PVU5paAAMK6jBeU4g21bGAQ_DeuWoNPh9zUxWJroQkpokNMlKBr32vyZYwMcsIKKy3eGEoWvjlUd1JLZoxAhoiW2g2lnwi7NoViApFDTD8HfcjkAPsVmK19aGOJCQ2UoqLLLX1g6PZzSsAlD-FlQYDKFOFVjTfgZSeUGr5-9N34yoE_4tWdp-6esxSCJWv7w4kGKoD37TDiLs1y_F9V-SKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولت کلادفلر خودتون رو رزرو کنید
‼️
تنها کار باید برید یوزنیم بدید و به اکانتتون وصلش کنید
⏺
کلادفلر یه سرویس پرداخت و کیف پول برای ایجنت‌های AI معرفی کرده که بتونن خودشون API و محتوا بخرن. با سقف هزینه و محدودیت‌هایی که شما تعیین می‌کنید.
cloudflare.pay
❤
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7399" target="_blank">📅 00:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7398">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آموزش تبدیل کردن صفحه چت سایت Qwen به API
🚀
اگر در موبایل هستید از
Kiwi Browser
استفاده کنید
‼️
✨
آموزش اجرا :
وارد سایت
chat.qwen.ai
بشید و یک حساب بسازید
در سیستم کلید F12 رو بزنید تا Developer mode واستون باز بشه
در اندروید از سه نقطه بالا سمت راست از منو گزینه Developer tools رو بزنید
وارد تب Application بشید و گزینه Local Storage رو پیدا کنید حالا کنار این گزینه یه مثلث هست بزنید روش و سایت qwen رو انتخاب کنید
یک جدول باز میشه و آخراش یه متغیر هست به نام Token اون فیلد روبروش کپی کنید یا توی کنسول این دستور رو بزنید خودکار کپی میشه
copy(localStorage.getItem('token'))
اینی که کپی کردید در اصل api keys هست ، ممکنه بعد چند روز منقضی بشه و دوباره باید بگیرید ، تمام حالا میتونید توی هر جایی که دوست دارید استفاده کنید
Base url:
https://qwen.aikit.club/v1
Model
:
qwen3.8-max
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7398" target="_blank">📅 20:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7397">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsUG3bdUuj5ZBz4QxvKBor1MoVTZ2JD_Zz7qGszklN8QVMI27DiovmVeoqUN7_DR-4UiNXT7Vi0W01mF00AjORCrHJbc2lYRNUqfmWEvBNTNS4hiWJjuX5kw0kbqEXsXeGnFfIP5p1qaV93vOKL-ZZ8e1kz7KCmDqtmQC6UPSJ1skV8BvuSAnIKMUr0OpUqbf87Uwr3oYUqIRQXTKQvhglcvnCKSp-KIjCCT0LETfdpDskv252Tbm3-WhhjZ1-78epNHr2UStrloyp0Kq6zadFKHZMCgS8WUYap2wzYBhYbttjuAZHUJMznN8Nk5IbtYsJacgK_SDlT8_GzyG8eQKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩
‏وارد سایت ‌
Cline⁩
بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند
این سایت
‏حالا توی ترمینال، ‌Cline CLI⁩ رو نصب کنید:
‌npm i -g cline⁩
‏با دستور ‌
cline⁩
اجرا و لاگین کنید و لذت ببرید!
💻
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7397" target="_blank">📅 18:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7394">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یه پست تند و تیز داریم
🔥
Base url: https://www.fastaitoken.com/v1  Api keys: sk-1acd2bba8f138537e2f5405f983933dcbe1c16042abe5ba2621fcbf8a1fed471  Model: claude-opus-5 Model: claude-fable-5  دسترسی نامحدود به مدت نیم ساعت تا یک ساعت
⏳
فاتحش خونده شد
✅
🔵
…</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7394" target="_blank">📅 16:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7393">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یه پست تند و تیز داریم
🔥
Base url:
https://www.fastaitoken.com/v1
Api keys: sk-1acd2bba8f138537e2f5405f983933dcbe1c16042abe5ba2621fcbf8a1fed471
Model: claude-opus-5
Model: claude-fable-5
دسترسی نامحدود به مدت نیم ساعت تا یک ساعت
⏳
فاتحش خونده شد
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7393" target="_blank">📅 16:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7392">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro
همچنین دارای چند مدل رایگان
:
GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3
به
این سایت
برید یک حساب بسازید و با تلگرام وریفای کنید و لذت ببرید
✨
قابل استفاده در
Vega Agent
✅
📍
Base url:
https://anymodel.org/v1
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7392" target="_blank">📅 16:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7391">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wws_D4zgOEaPGKm-MXSsKWEBX8LLD43qMOcR9TIAmnRjQQ3Yl4icXgP2ymHq7L7E0pS6yJ_URv8AScFTVNKaVS1_zFvYfNAPHIfoTw3boZ8zE3CasSpoWkHKPhDtDXXZeWQ8ltHHSPha5uzW0pjbw0Ms7UPQo-Cgu2jeOBOxP_UPohpP269GzIjqcUMSkbKIKV4TKEqrOAb1ynN9QqCF5-x8PsgekxNKCBGvgx9A09A0mtRLlXDRWWaYie6DVlUSnbiaVU3TaSb_DGjasGcJAKAa5DlAb7YrtUPcBcx4pqh-ClnaKiKhULjlFHj_WrQEtnt6iJY0gW2V_Zt700YgFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏100 کریدیت روزانه برای حرفه‌ای‌ترین مدل‌های ساخت عکس و ویدیو!
🎨
🎥
‏بدون دردسر و کاملاً رایگان؛ فقط کافیه وارد سایت بشی و با کلیک روی پروفایل بالا سمت راست، اکانت خودت رو بسازی و از قابلیت‌های بی‌نظیرش استفاده کنی.
📧
✨
🔗
‌
https://www.creen.ai
⁩
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7391" target="_blank">📅 14:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7389">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-FVc60FYGe6K9Cj1RRbOG58q63M3X8hf5jiDboahTCz1AVlUYtdzXi-iQ1iJZqpf4TYPn2c9PPBCmpqvGzg6x3EBH6Y6cnJK1NPhPVLGCCtQvHPQFaJW2b2fQLlSVmCXmj-QdBUMsJDFc5HAOOShkcQNKPvUoK6PgGrFeLu0nOMV5E7t-_e88zuaoBsGxBP1wzC3-SifADHx2Sdl2XFrw5OnD87F0PeaCg2-qtyoWUD38Wg4GBrbanCGqvQXOhuY5OqgAbXs64ssDNOn5MR4a8IENf4zjwDtzM09JZ5Gn6WicIYre0LDKb6vb8JpoXtaaNWQs_nQj2SIH_KbtKPIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دسترسی رایگان به Canva Business
🔥
از طریق
لینک دعوت
به تیم، وارد شوید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7389" target="_blank">📅 12:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7388">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آیپی تمیز کلودفلر
92.53.191.134
66.225.252.96
104.18.14.224
104.25.247.228
104.17.2.54
176.124.223.242
104.16.122.178
188.244.122.16
104.20.14.15
185.148.104.192
104.24.152.74
104.18.2.152
104.27.24.70
154.211.8.196
104.17.88.93
74.49.214.92
195.85.23.208
172.67.114.81
92.53.188.13
104.18.198.203
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7388" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7387">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwkHrPQWbru9byCudN3U6Yse4Vag0kJPqIecfaEYrMgjPKSy009nnMhUBKZ2uKVWMNxSIAKs7B8rz6XR_962h9tqxjHTsQmMXqgH8tB_vyxO3K6B-Yyi9oBeKKV4Ws5p3cCLPGNqMvu0Wu4_HWB2eS8QKPtygQWowg1Era2Yq0IL1mQdyk_o8rua5Ta_foO1SkKkZ95jJXFsORi_Gpq6xv-B6oaoaTWePyCUoVv7k9ZlRmqpRGlaC2mRIbJtBBzWobTLI0gg8iYWfGjN-_u4JNp3z5MWA5F3vbFuuPquAS927LlAd7K-r0M38eFIx69fU1onw6wGp-KX3M_wMRi4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
تولید محتوای بصری بدون محدودیت!
‏دیگر نگران محدودیت‌های اعتباری یا کارت‌های بانکی نباشید. با این ابزار قدرتمند، می‌توانید بی‌نهایت عکس باکیفیت و ویدیوهای ۵ ثانیه‌ای جذاب خلق کنید.
🎨
‏
🔺
تولید نامحدود ویدیوهای ۵ ثانیه‌ای
‏
🔺
خروجی عکس با کیفیت بالا
‏
🔺
بدون نیاز به کارت بانکی و پرداخت
‏
🔺
رابط کاربری ساده و بدون محدودیت‌
🔗
https://zsky.ai/create
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7387" target="_blank">📅 21:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7386">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بسیار عالی
ظاهرا سرورم دیگه پینگ نمیده
بوی خوبی نمیاد</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7386" target="_blank">📅 19:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7385">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0t9yJu0abKS2sS2ht8XwO2K_S45rbmmro6cauXSVPQ2--Upgb9Gb-pCFIMjH0-2B9webQEMHi_9LgOrLiX0MLIj2TWw4dtETUXGpp7N_DdvMyagmKMq2eAvrvnwSjOtqOgy_Qk0TouB4O4IhK-WVY-9Tc-FOuB9bdk1PYEGKWFReI3lUdFADjrk0Dsop7CJIEdr6xPN_hcNSCYOelO-ukoa1uzSZGcLbeiARVA28X4b9khUXkT-NWFEpRDo_VYl8Xck0E6EdlZc6YjrfVsijvluSnf2RYN40ygL3dHf_kUjmW434mq_h_o86aNAxdPm0Tk89GzDf2cAMYq56U6kUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
200 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Fable 5 | GPT 5.6 sol | Opus 5 | Sonnet 5 | Deepseek 4 flash 0731 | Grok 4.5 | GLM 5.2
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://seekai.cc/v1
قابل استفاده در
Vega Agent
☑️
از این
بخش
هر روز 20 دلار بگیرید
☑️
🎁
با هر رفرال شما
20 دلار
و شخص دریافت کننده
200 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7385" target="_blank">📅 18:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7384">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TI3yNvkkq9QM0_7rK_kByEbUHdlqP4hKdlVBNTQ4Q9TL9B4P4tZnEScnlH9idYc5A1gTzOa67iP5HuCsBMYkQwXbw8eyo3hS0eJQkyARhD0q4FQofSVXChkTynP9H79Na7i4WTcUexziVHtIiktImd8osJYo53u906JZIud_Rgo9RasreDkEKAi5TCcePFlvPP7P6ZFNlgpdth0k9mTrLdk4JNN-T-Yfy8CZx6lvmx3SW1k0xXQvGpwjqXQZuF4OyFt0BEEAcxFvDp-EwtPMH8N6HY1b_wOAokiQ6-mQ34DFm6JSAxf6jzAqDyY2yKYBC4MphQ2qJk5XUG7Lj39G7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
دانلود و پخش آنلاین موسیقی با فرمت FLAC
🔗
http://1music.cc/
😀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7384" target="_blank">📅 18:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7381">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دوستان اپلود کی ضعیفه رو ایرانسل بهم پیام بده پیوی
اگه حوصله تست دارین پیام بدین</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7381" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7380">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLmZd2sYy5N-zNCYkHPwmTUw8BjoAdL8CQrHfIf6qbKcBEWCFuOfE-NXAbj5OgotvOXlNDplb0HXLI7K8WAmhwvMblk9NqoHX1ri9wgnkdhtKHyBccpyvLCD1msCOvRofrxtZSzUPyKemUFuHHdL1lVfeXmnEwM86Qqw6mlUpDj2B9WeovwUiE2zx-fz7-c0KmJdNqRyz3RaiX_uzhEozrFQbOSMS3utre0hW3gZkE6xUmb09RSG_Qu3wiAlr12lPVaaCtiH3u3SXxFhcKIBF_a6cbGQsRotDGit16YuCdJwvrl_LA-bw90UPU4zEboZFsq8pYUC5kUfXHslx4o6xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی رایگان به مدل قدرتمند ‌Qwen 3.8 max
🚀
‏اگر برای پروژه‌هایتان به یک ‌API⁩ پرسرعت و رایگان نیاز دارید، همین حالا دست‌به‌کار شوید:
‏
1⃣
در این
سایت
با جیمیل ثبت‌نام کنید
2⃣
‏ از این
بخش
با اکانت تلگرام وریفای کنید
3⃣
‏ دریافت ‌API Key⁩s
📍
‌Base URL⁩:
https://api.aigate.shop/v1
‏
⚠️
توجه:
این دسترسی فقط تا ساعت ۲۱:۳۰ امروز فعال است.
⏳
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7380" target="_blank">📅 17:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7379">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgqApkyutoK2fjpAk-kWUNtvFoZsdNB-sydjhJdcommffqgAxAjAClq02SS3Q1l8iO-hDbQPnzdelviC9rp6X7f_mo2WpfCEsKbcr6AFX0LwbWrs2lGMHnQjfVBK72exyKNyyvSm8_Sb3BLh8xO4xBzVbaG2dsbzo6wPwGgpEssg7I0L0r0dxwi1Q1-xxO5N3YejKfmQUQSOL8eFJR6EldIJLNcIf-CSYmmNXOpqfmrdztR-v8TxI30-zpBrfAyYKlgosOl7JvLcVafMo5LL2PzqHe5Lv70zn2crGf-s7BcDVzIQzGZ1N4-P3Zz_AT-Lj6fmGbbju1L6PBG7phZ-GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
30 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Fable 5 | GPT 5.6 sol | Opus 4.8 | Sonnet 5 | Gemini 3.1 pro | Grok 4 | Nano banana 2
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب ( قدمت حداقل 14 روز ) داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://routllm.pro/v1
قابل استفاده در
Vega Agent
☑️
🎁
با هر رفرال شما
5 دلار
و شخص دریافت کننده
30 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7379" target="_blank">📅 16:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7378">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=e0psG8oQF-weUJN-OEnE5VzC05nroF7PPqE2WCcsR3WS7XSGgrzRPITXKFphjm6fTbiR4rRlb-UHZuOD9DP0QBhIjglO7ivMxdE4P15pLWOGTC-gXU48GVxSs9t0at0iZcqi4VRY5smtLUSH0YQDIBGUUQ9LPdLR5ciuqAU3BrWcbKS6_PEzp0SzaJSCZljWAaHg7OJwE5MdpwfaiRPGX05eNKybSDclx2yE8MID3AbNgdZgQXv50rzQYxvyqfjKbjvoMRriJCtvk7Gk8cPr8z1zhoiJk9IywbEswqkfCUPIg8sBlSQMAP7pE3CBiT2ud0Hhc8QuaTPK7YzFOVLkUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=e0psG8oQF-weUJN-OEnE5VzC05nroF7PPqE2WCcsR3WS7XSGgrzRPITXKFphjm6fTbiR4rRlb-UHZuOD9DP0QBhIjglO7ivMxdE4P15pLWOGTC-gXU48GVxSs9t0at0iZcqi4VRY5smtLUSH0YQDIBGUUQ9LPdLR5ciuqAU3BrWcbKS6_PEzp0SzaJSCZljWAaHg7OJwE5MdpwfaiRPGX05eNKybSDclx2yE8MID3AbNgdZgQXv50rzQYxvyqfjKbjvoMRriJCtvk7Gk8cPr8z1zhoiJk9IywbEswqkfCUPIg8sBlSQMAP7pE3CBiT2ud0Hhc8QuaTPK7YzFOVLkUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
تبدیل هوشمند وب‌سایت به پرامپتِ حرفه‌ای!
🚀
‏دیگه لازم نیست با کپی کردنِ تبلیغات و بخش‌های اضافیِ سایت، وقتِ هوش مصنوعی رو بگیری. این افزونه، محتوای هر صفحه رو به یک متنِ تمیز و استانداردِ ‌Markdown⁩ تبدیل می‌کنه تا دقیق‌ترین پاسخ‌ها رو از ‌ChatGPT⁩، ‌Claude⁩ و ‌Gemini⁩ بگیری.
⚡️
‏
🔹
حذفِ آنیِ تبلیغات و المان‌های غیرضروری
‏
🔹
تبدیلِ ساختاریافته به فرمتِ ‌Markdown⁩
‏
🔹
سازگاریِ کامل با تمامیِ مدل‌های هوش مصنوعی
‏
🔹
افزایشِ چشمگیرِ دقت و کیفیتِ تحلیلِ داده‌ها
🔗
GitHub
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7378" target="_blank">📅 15:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7372">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">NekoBoxPlus-1.4.2-83-arm64-v8a.apk</div>
  <div class="tg-doc-extra">42.2 MB</div>
</div>
<a href="https://t.me/ArchiveTell/7372" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📦
پروفایل پشتیبان NekoBox+
با توجه به
شرایط فعلی
،
اختلالات پیش‌آمده و قطعی بسیاری از کانفیگ‌ها و VPNها،
با این روش می‌توانید به
مجموعه‌ای
از
کانفیگ‌ها
با
پروتکل‌های
مختلف دسترسی داشته باشید و در صورت
قطعی
، گزینه‌های دیگری برای
اتصال
در اختیار داشته باشید
☑️
🔹
روش استفاده:
1️⃣
ابتدا برنامه
NekoBox+
را نصب کنید
2️⃣
فایل
JSON
را دانلود کرده و
Save
کنید
3️⃣
وارد
NekoBox+
شوید و از منوی
☰
به مسیر
Tools → Backup → Import File
بروید
4️⃣
فایل
JSON
را انتخاب کنید
✅
تمام
.
تنظیمات
و
پروفایل‌ها
به‌صورت
خودکار
به برنامه اضافه می‌شوند و می‌توانید از
کانفیگ‌های
موجود استفاده کنید
📌
این پروفایل شامل ۱۴۰ اشتراک و گروه با کانفیگ‌های متنوع است
🛫
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/ArchiveTell/7372" target="_blank">📅 12:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7371">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f8d804f72.mp4?token=drKkTstVBHjHE-QklhjD8joVnvqHyo9Qmki11t9ZJh1dP6xOLnDByRPIRL9T23hfPJVNxiTbptUYGu-chg8ohR2fvADaTcXXR8eP3Fcfgd-I0RKuU35VEjEhP8QmH48M43ExFrfZy5ReJhjHkuhnsPoHeft96fgewAEhFSGpbHbI8a9ht9epYuoS3fjsx3rI_Ei2FgIJuO0Nsreh3zoMA2rcr6K_QGlxb-FntpY5I1Q5ZSZV3hVDnnM8mdEO4VpqCN_Ng1r26SPbImmZnVNLx6WHciBrU47rah-TJ7ZnDwlekO0pqqnctV_BxP6qRXrRTrPMf5WB4fbJVI5571eAcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f8d804f72.mp4?token=drKkTstVBHjHE-QklhjD8joVnvqHyo9Qmki11t9ZJh1dP6xOLnDByRPIRL9T23hfPJVNxiTbptUYGu-chg8ohR2fvADaTcXXR8eP3Fcfgd-I0RKuU35VEjEhP8QmH48M43ExFrfZy5ReJhjHkuhnsPoHeft96fgewAEhFSGpbHbI8a9ht9epYuoS3fjsx3rI_Ei2FgIJuO0Nsreh3zoMA2rcr6K_QGlxb-FntpY5I1Q5ZSZV3hVDnnM8mdEO4VpqCN_Ng1r26SPbImmZnVNLx6WHciBrU47rah-TJ7ZnDwlekO0pqqnctV_BxP6qRXrRTrPMf5WB4fbJVI5571eAcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
کپی‌برداری از پروژه‌های گیت‌هاب با قدرت هوش مصنوعی!
🚀
‏تا حالا شده بخوای یه پروژه خفن رو از گیت‌هاب درک کنی یا مشابهش رو بسازی، ولی غرق در پیچیدگی کدها بشی؟ این ابزار جدید، کل ساختار مخزن رو به یک «پروپوزالِ اجرایی» تبدیل می‌کنه تا بتونی با کمک هوش مصنوعی، اون رو بازسازی یا تحلیل کنی.
🤖
💡
‏
🔹
آنالیز هوشمند:
بررسی دقیق ساختار و معماری کلی پروژه.
‏
🔹
مهندسی معکوس:
استخراج منطق اصلی و اجزای حیاتی کد.
‏
🔹
تولید پرامپت دقیق:
ساخت دستورالعمل‌های گام‌به‌گام برای بازتولید عملکرد پروژه.
‏
🔹
شتاب‌دهنده توسعه:
ایده‌آل برای یادگیری سریع، پروتوتایپینگ و درک پروژه‌های سنگین.
🔗
https://www.gitreverse.com
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7371" target="_blank">📅 12:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7370">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ربات تکه‌تکه کردن و آپلود فایل‌های حجیم در تلگرام (بدون دیتابیس!)
🤖
📦
یه سورس
ربات تلگرامی
فوق‌العاده جالب و خلاقانه براتون آوردم که روی بستر کلادفلر ورکرز (Cloudflare Workers) اجرا می‌شه و وظیفه‌اش اینه که فایل‌های حجیم رو از طریق لینک مستقیم بگیره، به پارت‌های کوچیک‌تر تقسیم کنه و بفرسته تو چت تلگرام!
✨
ویژگی شاهکار این سورس:
این ربات کاملاً Stateless (بدون حالت) طراحی شده؛ یعنی برای کار کردن به
هیچ دیتابیس، KV یا فضای ذخیره‌سازی ابری
نیاز نداره!
🤯
شاید بپرسید پس چطوری می‌فهمه تا کجای فایل رو آپلود کرده؟ ربات خیلی هوشمندانه تمام اطلاعات (مثل آفست بایت‌های آپلودشده) رو توی خود متن پیام‌ها و دکمه‌های شیشه‌ای تلگرام (مقدار
callback_data
) ذخیره می‌کنه و از خود تلگرام به عنوان دیتابیسش استفاده می‌کنه!
🔹
قابلیت‌های اصلی:
*   تقسیم خودکار فایل‌ها به پارت‌های ۴۸ مگابایتی (برای رد کردن محدودیت ۵۰ مگابایتی آپلود ربات‌های تلگرام).
*   امکان ادامه فرآیند آپلود در صورت خطا یا قطعی (کافیه دوباره روی دکمه همون پارت کلیک کنید تا فقط همون تیکه دوباره دانلود و آپلود بشه).
*   بدون نیاز به سرور یا هاست (قابل اجرای کاملاً رایگان روی کلادفلر ورکرز).
*   اعتبارسنجی خودکار لینک و حجم فایل در هر بار کلیک کاربر.
سورس
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7370" target="_blank">📅 11:54 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
