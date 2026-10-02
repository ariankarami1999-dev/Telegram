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
<img src="https://cdn1.telesco.pe/file/nH-tqYKKMcRwPcEk4ndra9ZxDPmNuSaN8scUIoIDDbR3_5D6df29T8sgmTbnglAY3rnKHzavQAhWeQnovWuM27EbPMY8lB5pUL6yeGygtBj2_NvMiJHyGuk5sJqmGDKljsgEHoxxmN7PSc4AXSxnmLMpzObmUkTRGoXQC7Bv1JWtJ_-eWcaHnKngHpQ2IToVvRpQF7WQUxZcpLtMPkzqitI_ZAGaoj-rM1ox6UkHhaP1eKAhb3Kfjo0_DUGnm8M84WCSN2q94-o9CW2sB6kHvde5PpW7xCIAKH286yptJ1BZ88YZeYwq-bjGH_RvDe_aUGLpauaBdyQV0m95GtoWZw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)ارتباط با من:https://linktr.ee/matinsenpai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 23:31:10</div>
<hr>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tFstmDj0rdeG3a8qaNQE_pSXGaW6pmGewKswS7Mw77mpZj_QEpRLQGUuo6oc2FQg_kogaP1tx3Dcd0wa73o8JvEx1HXbrr5Wk_KhN1dMij0b0u6MbQG2lS8ry9d86pIZUBPgH9oKBsTY0SQ65cVFBg7P0TtrC32NUqdgSxQ3naP1ml_pb1oUpiZ2M5FZTKZQNPRHU5bo0CJM60fMTK-09rlvSLsMmYpxoUMNwbTRqmBgtf5ICIqsGTqWxAJII1KkW5MwqyiK8JIxQGpthMCoggj8ztf_VfqvAEmZ7X8aVRDfD50jEsJD2p0JUwP79yolK8d1V8UqThts5yJLZkISNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA  من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/MatinSenPaii/5481" target="_blank">📅 18:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XWNwWpST1YIRvuqPE3yC9Z_9qnEhJoxcygZIV5GESC4-11hoekarBpAWHrc559RAz5HZ3VPKP2OpKzQ0l97mzyrZ5gUbOE3XCy8gOvTX8qHzOuiA9NSy2PXI4snE7WXI9mMlMssbEWMtHv3WJrDuXfBork8zBKxjuuvj73rx-8eHKsTBWFst_k9ji97p4s7ZuONZ7goeMHSZFFmt5g2qyz6bSWy1l1lTPPKN-IfVKAlsqIgQSCvnQ6pQl7CZETkP38UTmXGQSzOUCjctQ1L0bdOy5-HL00hKoU5uUwOk78pdbhoYv56DHFjrakwNXTl7Tw5T_bg5PqQjfQ2jfTyMQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qFVK8L-xFytmdEhYjtDAFojy7qGd4pKXc6ZxE2Qi8YeJq7gem50f-hHD3tiharqoXfS1JukIHDXBEJtZoGvUtOILg8PbzObIAHnbvVETQqttPk9OE3Pr1iNByESVjb1U8U-fA4ZFiTrkrpgtbWCnM3TACSgObkaLbXLFC_HM2Z5rhSwhCIZdSXdATuECXgfv8db-ZEFDnl8kOG2mAhnqf9MHBF4YHLcznjk3I56TRLWu5UsDE1_pSevVtjE8m3DOZJDkvkDO--RxsVIQxfCLrkqnv5vDccfO36U-NVEuhwaWP5zie2jZjOTa1Y_PAbAI7fNmffF-RtyHeyMY_jgzew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/MatinSenPaii/5479" target="_blank">📅 18:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZhOJbTdk83cEpIuoFAEyF-SW5YsOYSIqDE46-97kJlGQyY8IyB6DDxTcf6zKnu8aqWTSrNGBlxHMIczdxVCXRC9r3WS8JgQwprnQ7ipvaMDPD3DgEsiwosKyZ7Rw-Gc5ev_UxH9iltfwm8p3XCklYy6IBiZ_UFFNJ3mvGTY1jS2UpoW6axAFcDxIwZ_HYEFUJUtS23XCjp9OG8JzvvSKi2-bnVv9iMisaE7t8B5G796dybi3w4_YVUe398M-5iDsNwQC-JwgxrtbHCzi1rnjbo15bJZIlTyp2vTL0vQ73uEV6n3kG06HffeHW1-RffsPwNPj0yQCRKba1Ft8DMkxJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA
من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد دادم چه شکلی ازشون استفاده کنید و حتی با اینترنت ملی هم بتونید دانلودش کنید.
امیدوارم که مفید باشه واستون
❤️
دانلود Ollama:
https://ollama.com/download
📹
تماشا در یوتوب:
https://youtu.be/EAF-hMPUMYc</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/MatinSenPaii/5478" target="_blank">📅 18:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/MatinSenPaii/5477" target="_blank">📅 17:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akN3pz-z6yGbIJzWTPZJHVUKDLBm2hSQFVwTD5hQLa2sPi4VLMkijeCpOjGbrs20Y6bfB_efXDMuc9dhM1v7hanOCOnNKkHDSPimiEYfabG--zOp4oIA1UM-CAIpetskzcN7Ci38U89WrVLVw5m0R66xCP3uMT5Zna9e__bBGnfTnAGK5BMF9qvb4TMh9Z1VQexq6APuF6zDEQtKJRqHOxFrL4TTGiEiu6_2QqLRomEm-pNebyEQGozsRe9edcbZZbejLp1ce_GWItYUge_ytEvorXZhhorq46kn9FKZqIWwUkVsDbE-shXiEGUDgTRmt6dnQ-ia6D7xyX0XrptfBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/MatinSenPaii/5476" target="_blank">📅 16:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">در کنار بلاک/فیلتر شدن دامین دریافت کلید وارپ، اومدن sni مسک (Masque) فعلا فقط h2 رو بلاک کردن :))</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/MatinSenPaii/5475" target="_blank">📅 13:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/5474" target="_blank">📅 10:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">چطور فاصله‌ی بین Hermes و دستیارهای اختصاصی Dots و Grok رو پر کنیم؟
یکی از کاربرا توی یه راهنمای کاربردی از اکوسیستم هرمس توی ردیت، بررسی کرده که چطور می‌شه بدون نیاز به پلتفرم‌های بسته(مثل grok bot و dots و muse و...)، قابلیت‌های پیشرفته Dots و بات‌های گروک رو توی ستاپ Hermes پیاده کرد. راهکارهاش شامل لایه‌ی مسئولیت‌های موندگار (persistent responsibilities)، سیستم دیده‌بان پرواکتیو (Scout) برای وب و دیتا، مدیریت وضعیت تسک‌ها با SQLite، و تعیین سیاست‌های دسترسی قبل از اجرای ابزارهاست.
که البته خیلی از ۱۱-۱۲ تا قابلیتی که گفته همین الانش هم هست، صرفا دسترسی باید راحتتر بشه توی UX خود هرمس و به نظرم کم کم به اون سمت هم میره
👍
پستش رو توی ردیت بخونید، بد نیست:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/5473" target="_blank">📅 09:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مهار دزدی و Distillation Attack مدل‌ها توسط OpenAI
شرکت OpenAI اعلام کرد یه کمپین گسترده و سازمان‌یافته برای استخراج و تقطیر (یا همون Distillation خودمون) قابلیت‌های استدلالی مدل‌های پیشرفته خودش رو متوقف کرده. گویا مهاجم‌ها با کوئری‌های پیچیده در صدد کپی‌برداری غیرمجاز از متدولوژی استدلال منطقی مدل‌ها بودن. اوپن‌ای‌آی دفاعیات و سپرهای نظارتی جدیدی رو برای شناسایی و خنثی‌سازی تریک‌های Adversarial Distillation مستقر کرده.
(ببخشید برادران چینی. راههای جدیدی پیدا کنید
😭
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/5472" target="_blank">📅 01:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5471" target="_blank">📅 23:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آرنا توی این ویدئو، قدرت Gemini-4 Argon رو بیشتر توی زمینه‌ی 3D و قدرت پیاده‌سازی گیم‌ها و محیط‌های مختلف بررسی کرده
که خب کامل نیست و باید توی تسک‌های ایجنتیک و کدنویسی و بکند و... ببینیم
انگار که کلا قدرتش کمی پایینتر از GPT 6 sol هست که خب، ازم بپذیرید که قابل قبول نیست برای گوگل، اونم بعد از اینهمه غیبت کبری
توی دیزاینایی که نشون میده، قدرت Sonnet 5.5 هم می‌بینید
😂
خداست این مدل
https://www.youtube.com/watch?v=h5EL5zThKaI</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5470" target="_blank">📅 23:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tMsxgZBHl48Eg_FuqKtRvD3XEKCfyil18o5LElEkNqDw6oG1J0YzbXd7mdq-5zDWfGHfAvhh279bZtAPpnk3tJJvF6cGHXcyAIdhQCtjrlnIj1sHBGP20FoConZqp5hpt2r_dJ8WC0vgfxTdDindsBr1sy-qc7iabgaNlSa_TToi6cTHg7Bc43o0Urvywqm8bfgbw4kJmmjIS98TimIVi1jT5J1QCZGqIxxwZN5wvVuAGxZCpCqudhiNP_CrmUgZyMJqQFe4Qawdt4w-dX2puklvp1vGSm3kV5vcxyeZWXWgjlPWKW7EJmctqtZscXH7IZl1Ik7mKaQKy9vG3cKu-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)
1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا
https://github.com/patterniha/PattNG/releases
)
یا نرم‌افزار PattN(برای ویندوز از اینجا
https://github.com/patterniha/PattN/releases
)
دانلود کنید.
2- کانفیگ V2ray خودتون که با Worker کلودفلر ساختید(آموزش ساخت کانفیگ رایگانش اینجاست:
https://youtu.be/iAbYpjXyLpY
) رو وارد اپلیکیشن(PattNG یا PattN) کنید
3- توی اپلیکیشن اندروید، روی مداد سمت راست کانفیگ و توی اپلیکیشن ویندوز، دوبار روی کانفیگِ وارد شده کلیک کنید تا پنجره‌ی تغییر تنظیماتش باز بشه
4- توی بخش Finalmask raw json، این مقدار رو وارد کنید:
{"tcp": [{"type": "fragment", "settings": {"packets": "tlshello", "lengths": ["0", "104", "1"], "delays": ["0"], "maxSplit": "0"}},{"type": "fragment", "settings": {"packets": "1-1", "lengths": ["114", "1"], "delays": ["1"], "maxSplit": "11"}}]}
5- توی بخش Fingerprint، مقدار رو روی
Unsafe
تنظیم کنید.
6- مقدار Alpn رو روی http/1.1 تنظیم کنید
7- توی بخش Cipher Suits، این مقدار رو کپی پیست کنید:
TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
8- کانفیگ رو ذخیره کنید و پینگ بگیرید. دقت کنید تمام موارد رو انجام بدید. آیپی تمیز
188.114.97.6
عموما کار می‌کنه. اگر کار نکرد، از اسکنر
https://github.com/MatinSenPai/SenPaiScanner/releases
که هم نسخه اندروید داره هم ویندوز و مک و لینوکس، استفاده کنید و آیپی تمیز پیدا کنید.
مقادیر ممکنه عوض بشن، مقادیر جدید رو می‌ذارم خدمتتون.
موفق باشید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5469" target="_blank">📅 21:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILjrPx8Lq9tp9QONJw4ln-RgDchEkH1oUpWOLV_a3k-rhXFDr6wknqHUyeNypbwF9gV4caDNQMawBQaMYKBlCa2vOiCHWsVXhOJidvFHw2acnzH8FjM-CK7Hlt5uvnZFbmAzWZN6RmoQWYnyEtoFwOYI2PkK0lvH2ewVY0COhrqD0x_y9hkj6_dpN68o7BmVf0_mrW5tKk0k6zcHWTculWpVVZbfiDjvquBjFzmGJWz8_IEuWO8gTood0wcPAh716WfXj_pRhm8QqlZhJm1Ip3D_RzhhCVhhVTgcY-7N5T3Hz-88iZuHyeUQ9TWFvcFxRRt8Ttc1q_cOi6ouafZi0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل Airbnb: ایجنت‌های هوش مصنوعی به سیستم‌عامل اختصاصی نیاز دارن
برایان چسکی، مدیرعامل Airbnb، توی گفتگوی جدیدش تأکید کرده که
پارادایم اپلیکیشن‌های فعلی پاسخگوی نیاز ایجنت‌های خودمختار نیست و دنیای هوش مصنوعی نیازمند سیستم‌عاملی مستقل و AI-Native هست تا هماهنگی بین ایجنت‌ها و خدمات به شکلی پایدار صورت بگیره.
خب مشتی یه کاری بکن. ما هم میدونیم
😂
طرح نیاز که خیلی وقته شده
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5468" target="_blank">📅 20:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بزرگترین مزیتی که ایجنت‌های شرکتی(Muse, Grokbot و Dots) دارن اینه که با مدل خود کمپانی یکپارچه هستن
برای هرمس، یه کم چون دستمون توی انتخاب مدل بازه ممکنه گاهی اوقات گیج بزنه یا دو نفر با کار یکسان، تجربه‌ی متفاوتی داشته باشن
اما همچنان هرمس رو ترجیحش میدم</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5467" target="_blank">📅 19:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">قراره با هم یه اپلیکیشن تمرین زبان با روش Shadowing بسازیم.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5466" target="_blank">📅 18:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qYdcSJwVxlq4oztH8rPdoMKr0NkuWh0wUFpTa2ieq_wjBxt0nzKvuDGxNrkslCToynm2O2noOnQfuodkjMMAdJuojIUCorRZWZgNxJhP5WDDPyGADJAppOP2Aaa6tPsQl756kXJNTvUvFLwEeJ5Y59_onCassMr6s_JpdJ9BX3zUtUxJyb2QaCjbGJS8D9UXOXHSppuwvdkVNZMkYccvugGqsKwkIwb8PXeg5uSmq-I4JmiXG9uSymUTi15Hp64mxxQcIufzZE6QmpW0xMjAqwK4auvbY5-GaNV-RZUdpROJ_sD6axDr7cyeGNbGbmu_HYE90QAV4uif1dPsO-C6Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ردیت فیدهای RSS را متوقف و دسترسی عمومی به API را مسدود می‌کند
ردیت اعلام کرد که به دلیل اسکرپ گسترده داده‌ها توسط بات‌های هوش مصنوعی، پشتیبانی از تمامی فیدهای RSS را از ۱۳ نوامبر به پایان می‌رساند. این شرکت همچنین تاریخ توقف کامل دسترسی به API عمومی را مارس ۲۰۲۷ تعیین کرده است. این تصمیم در شرایطی گرفته می‌شود که فروش داده‌های کاربران به غول‌های هوش مصنوعی به بخش پرسودی از درآمدهای ردیت تبدیل شده و این پلتفرم دسترسی رایگان را کاملا محدود می‌کند.
که خبر بدیه برای ما
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/5465" target="_blank">📅 18:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">امروز زیاد ازش استفاده کردم
گفتم یه توضیحی راجبش بدم</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/5464" target="_blank">📅 18:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یکی از قابلیت‌های بامزه‌ی یوتوب، Hide user from channel هست
این شکلی که وقتی کسی کامنت دری‌وری می‌ذاره، زمانی که هاید میشه، هنوز می‌تونه کامنت بذاره، اما کامنت‌هاش رو فقط خودش می‌بینه
نه من می‌بینم
نه بقیه
اصلا هم متوجه نمیشه که هاید شده
😂</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/5463" target="_blank">📅 18:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J6ve7HBwRbfkWuXupeTXdwr8XjMmKLTyrOKJJI5ZI-6CZWsB1NS7ABhhiVbnV580ZgvguHFS8OevkbalLxc4eBpu-HIO_FvTC3gfmAS-7JMURuclrh7h8zE2VjBedq3dRd0mbiSHx747LTPoVEZb9th4kaAjNy4z5dSTEz6D6wDqL94BcMdRy-zf8QNWrHEkeFZH1GxJU3q5kVArxKpmE_6VsxIiSdFvY2Y3DfdJ16ZaSt0Gi4F_GNzLlMAae2Xh02H9yx1wzZqMuEDaGoxyvsjcxrb2e3lXqH4niFDBsDslM0V_cByScuPL3WNfiyLiN-ExHZZ5nKtV3zWPh3dZ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/5462" target="_blank">📅 18:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fIaiXJAyJZfK7FRkM6HI9KK7sflRpR_TKA3fC4v4hc31dzEwh7GEXtXv6ZBY0QoN_eT7qbyUZJiPBGHKVarox8h06UemfSOEj4AamNAoLj1TqK77ZBgtEZP2jGQKH1Bbf7ey-nhoZmIJ6YazPeJ7X5oK3-zjQSBj8YNCtA4mA6KnCv420q_2kTHF9aSIb-GZlcKSmgY9q1nKQCxhGHk3eOCoTP9dPQr1xSuqC_w0a_tboV_mgTdme-gJ1KSaIl2T3UHgkLBdBSnLpC8bb3cGs7vbSe4L6hwJ4TJiKAKggodamcz0yQcbaOuEpj7zXkwT0HmCep4bkOAAsxXcfQRw8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Decisions API توسط OpenAI برای اتوماسیون فوق‌سریع تصمیم‌گیری در ایجنت‌ها
سم آلتمن از عرضه قابلیت جدیدی به نام Decisions API خبر داد که ساختاری مشابه مدل سریع Jev از استارتاپ TypeSafe دارد. این رابط برنامه‌نویسی به توسعه‌دهندگان اجازه می‌دهد مجموعه‌ای مشخص از گزینه‌ها را به مدل Luna بدهند تا با سرعت بسیار بالا و هزینه بسیار ناچیز، به صورت احتمالی بهترین تصمیم یا اکشن را انتخاب کند. این رویکرد به ویژه برای کنترل ازدحام ایجنت‌ها و اتوماسیون لحظه‌ای نرم‌افزارها کاربرد دارد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5461" target="_blank">📅 17:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s9SUHzVxItN6Y5HtuoC2Jc2ujht7uSutt_MSTN_9xiqGlIlR-cWOlaBU1R1DiLX8zeUA4Gde3vT-aFJzQBOTBWOPtkVPGLkNrEtIQnU3IXQB1l7PU7ePZSf5kSinjPwga5ueu95nqQvZlZWNswjL4CuhDGeRg77jSGaZhgXSln4a6I5goxm8KF2z1WppIcZgm51BGLC2pvBw_cidBmxQVCZLi2e066bIi1ASg7YslkdI8IBXOelu3R17SghAa7UWuwusnS4PHN0obMc5Ah_VULIpjyCYHRp7egYrlz_SbHe15OLxJa0VvQdfhwwczzUofoxLjuoy32XEsvy29YvXyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به قول Theo، چرا واقعا OpenAI هنوز داره از GPT-5.6 Sol استفاده میکنه توی چتش:))
نه تنها 6 sol اومد، بلکه 6.1 sol رو هم دادن و چت هنوز روی 5.6 گیر کرده
اولین باریه همچین چیزی رو میبینم حقیقتا بین کمپانیا</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5460" target="_blank">📅 14:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jeAswI76VUE8BZsEELqKPgdsnQsOxjHs42pIo8SjnSRUdjPGFY-ywyrgiMrt2JqrDa75JhPO-E1eHCx4KPAmiOU08-K14VRLXTfKh3KP62XDOVBqHGl8SxvyqGbHFgxNrTlicxSJsYFkWTi_R_EJ0gVpQ1F1wgDueoa1AdPEyyLhVUBHv5sGvzsWfQwPG0KvBpLu13UBBslvraaRKSQ3Noy92ZrHucH3Q_2TfmWgW7YMCDbh4JIyn2AzB5T7S6vHE_6qx7w5oDTeutQw89ALLCpBgewZqkmcmBJqAuMgvxn9eiCQiWBuBCXX5Ku3y8aing4tAaJvDxkXyhOXU65pAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله ما نسل Z هستیم
😂</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5459" target="_blank">📅 12:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k-0PAwTpofDbGE656yhnYq1PE57tTlM27xqre2PKGBiFottezdR8ddj9PRChKj6LOVDme5muliDYAbJM3cdeRhi-OJjZPTX4i0_I25Mdf36PHhl6kuoJ7gjeNtZPwzttyAH18QF57qCgkvzb8cNbEQDdnnaxzaTkkAGZUL68U81LSqdc8rN8lAiyihrPGNI5oE9hLM0kMHAejpFiAwVIBVuvrEUn7vCa03UFz2JpbC7G_TqDTEOU1raQkMU7v2ZSeTrNor_enGHU5UlItF-AJh-j1ADCGQEpyHRJjShppdPBSDO1U8mIp3ek7lyqPXG6AoqE2runV0RS7O9CIMMMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate
توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب:
https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5458" target="_blank">📅 12:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شدیدا حس میکنم مدلهای چینی اوایل که اومدن غول بودن، بعد از عرضه یهو ضعیف شدن
مثلا هممون به Ox Alpha دسترسی داشتیم، بعدش که glm 5.3 flash معرفی شد اصلا اون هوش رو نداشت.
یا من به Qwen 3.8 preview دسترسی داشتم و خارق‌العاده بود. سرچ کنید توی چنل نوشتم از تجربیاتم. اما الان Qwen 3.8 max وقتی ریلیز شد هم از مدلهای Frontier خیلی عقبت‌تره هم توی بنچمارک و هم توی عمل</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5457" target="_blank">📅 11:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nZtNghpgQiH42VyhFNIrw_YEwZ52VkidU8rEptsFT89qKrbcaG3N10G8FQQqfnt8Bm5tsGiRsNJ1RwKC-weLmcPfHHmf8FkO-5fV1XYAXyAy-ONL0tDxmdqKv9ds8sLyIPouXcrhGUe_qjYiUnPDRwp8x4bGqwQmpgAu0apBd1Qb1v2MC-cbwWXtBEyKpmEhTp058LeICHKfi0VKmh5MOZfaiU-aMX_gRhFBwOf0J5rjjOVABlAT2pEEMmpzodBNKBarKRPobZR_ro_D0vf54txgKS6KGDPy9t4QxQcWL_r-4RrYYjI8khxqCM3_SPKzHdNfXV4Dx9dClzYPP6bumA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم به نوبه‌ی خودش عالیه
Hallucination یعنی توهم زدن ai
که این یعنی جمنای 4 به ندرت از خودش یه چیزی رو در میاره</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5456" target="_blank">📅 08:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کلا هر مدلی که میاد
این قضیه‌ی Benchmaxxing پیش میاد
نگران نباشید
میگن توی کدنویسی اونقدر هم خوب نیست انگار و باید منتظر موند و دید تا فردا پس‌فردا که شایعات و تست‌ها به کجا می‌بره ما رو</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5455" target="_blank">📅 07:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rQVGxr2y0jSAOlwHSeu-MbhwzZJtSvR6Y95kqtPbdu-LHhYHDvtvNSzf9v8oO_fReEwr0sk9yjlJm0YKbp9zYkkaHdB54ylaw-eHDaokXNYXT9rwhvc5cRSOyfHWeEeP9k-7aNMaN7dOY5YcHKdSdvSyrJR94tgttc74DD1XZlO7JTpNK9I0YyWyVE_xUzTm5eadSHT-0fDfT1WDAzvaA6cjH6DhLVD3JQ5lRmipU9acnQ83bumiwhvd2fQq4_gL1h5qD4fXtliCZo8VpzdV6N5cTXX9a5ovt2sLoYx37o5ESvJa_ObZozFWu7Jzr7wOcGCuxP4tx9DU7MGIBZj-VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/THy5ADHb1_ZcbUi_2PZbHOabq0RhU4DeHtja9lwrXlHEbdpZ5sCbssl0EkXXqWQwGCiUijz0p3ycaWDUUbu5wGsrvpLvDkz9H7Gh0ouLDDcDGG6fD9VSrdLd5F9ZQ5_FIYSngswbZRb9ppX0kaT7P1cGOJ5peFhwS7VQ3Y09vNeV7Z9b43vC9cQz-VTCFTHpK4B2UlygxQK4CqjwnWawqasQzVRjY6aJ6zd39ZXbK1eXuH0FTrdYuoVWK-wbWrbAr9h-ZXE9ysTsD6KRENix72I5Xu9M8ThINLqLjSwMwsZ7W7kYZNr8UTBJkIbQJj0OofyjmbgdHE8Ent9L-pLMkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q7BpARCsn-iN68M7QINKxjBnzjQWq4msg-GYAEX9lrKDfiKsDy77tJH2RWdTpBnW7WBjcJdyYHjvQGHBKCp0Lmi2yIXSHSK9ahSCB8Jr2HuN4Hwe-g1zGRiWuYZtG9nPrAVFSmlhvp7QOxgT4vOJ0P9Hu4pIDoB0I3fVpEm5o7N3_445PIaP1wEBbw8KDEFTuRrY1ruFm60TVyySONI1MwiKwXgOhVFhdMef59E62VvVTmUmSLAj543Sj_zkioOZGuMYaSaplDoEIXNYeZIDQID-RYdOG5pphGlM9DdzYGI6GHyaAzN7zvGUdU7RVfoAk-gFbvaObD0kgqAYJxFS2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u1Q9qJ1AQtKoSCrPahnkOca4EsFu9_6Y7QwOhMe4Z4-h8B9WHxM8xY0ammotSbLKD3h3AbR3skQIMiFEg1kKyLdTxcegr4Eo1sRfn_wM0uFdlBn6uo1e0WAn_w8e8fU_ZkB3kNb-ebo_bw0zWRJC8AYcqRXeL1Q19GNJkGG-dm69mekBCbG6NOOgTd7aIlkjrVeIhQeNyLYem4szrPtUJKI_dhhfqBWfMNxRplZT48lr8x7Ss_kKVwhW9oAt4FsuB4kOzYXrWVAQluzaASwDENUKXXCI-sI1BDHY6CXTgV2fmfc_gnMO_u8VWOyoy4ohrZJM-VZFoL6eR9oMorRLww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری  گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5451" target="_blank">📅 01:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=c-J1MgHGA5zuA1Y1fqTXRbOv9EFzJpgHMxiGREy-F2Mervbk5_8M06AgIj6mEvZWKT40BpVW3CcLc9n8q3OyC2XSyemI_GoAlKc9E2R9F-TgyKaM2OIpmB09QGyaoGjwWvlEIpMPtpC-1o7V7lsWH12ipH94x1FAhLINgno5py-7vSRb_y6N6W4GvdcrM1Hzz0-yFuKEGwF368_S2pl_YlydhnrCWQQZf5XgbD8O0hyNNZPTLgy-8TCHTF39Oudcz62Pz59Un5Z45wiMBpKWgMekViFYC_8-X30Lrc_qHnVPu3mWe-FhGsfEJft_LjHZRWoYGBArp7vAEBMXJ9G-Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=c-J1MgHGA5zuA1Y1fqTXRbOv9EFzJpgHMxiGREy-F2Mervbk5_8M06AgIj6mEvZWKT40BpVW3CcLc9n8q3OyC2XSyemI_GoAlKc9E2R9F-TgyKaM2OIpmB09QGyaoGjwWvlEIpMPtpC-1o7V7lsWH12ipH94x1FAhLINgno5py-7vSRb_y6N6W4GvdcrM1Hzz0-yFuKEGwF368_S2pl_YlydhnrCWQQZf5XgbD8O0hyNNZPTLgy-8TCHTF39Oudcz62Pz59Un5Z45wiMBpKWgMekViFYC_8-X30Lrc_qHnVPu3mWe-FhGsfEJft_LjHZRWoYGBArp7vAEBMXJ9G-Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5450" target="_blank">📅 01:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XAz9cdAxCXVxlYO73d6cAtWVrSS4BJLGMuFmXe0FXoim-8eC1ydQRWMBylYkFYxkvE2_2aMgyzbvXvYcuJri3k2xsn81OLQLum5rwRH3-K1CguolDNNxTBd30qLhlYmpp_0zjCuJ70OxeaX03elAMoLgGKE-FGPoAa0qwVF_3tagcGJX_YtXARW1lMTMPqNdX_4FxciY6VLHThG1X96puUyDnYMZAV_ds2RZtBH41hcy-jFa3H0emCOCDR5EvFQIRc74-CEiuDp50kGB70pd5nzHo4TMcNQ7D31w1pgmVxZDxFYon7K0ns3K9H1HSjvnE22-8Dbh6I3M1Hl4utgANg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری
گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای اکثر مدلا) تولید می‌کنه و توی بنچمارک‌های مهندسی نرم‌افزار (امتیاز ۷۷.۹٪ در DeepSWE v1.1) و امنیت سایبری پیشتاز شده که به زودی می‌ذارمش. آرگون با هدف کارهای سنگین کدنویسی، تحلیل دیتابیس‌های حجیم و کشف خودکار آسیب‌پذیری‌های امنیتی طراحی شده.
هزینه‌اش برای دوره معرفی، قیمت خیره‌کننده‌ی
2$/10$
و بعد از اون،
4$/20$
اعلام شده. با 0.1$(بعدش 0.2$) برای هر یک میلیون Cache ورودی
دقیقا هم‌قیمت با Opus 5.5
باید فردا ببرمش زیر تست ببینم گوگل واقعا پرقدرت برگشت یا هایپ الکیه:)
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5449" target="_blank">📅 01:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بیدار شید بیدار شید
جمنای 4 اومدد</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5448" target="_blank">📅 00:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e3w_RawvUIyFUKhYwF_9jTEldY-hyTVQXZ7NaEKN1phDXsf5FrE-rYq8-QC7VVsPGs4U9JcA-pWxlIbPGsIdtdlXjix11e6gHlmP66OJjgMYu-ks7tAYQlM5vW_bKQiwo5gttNKuABhSxdxB9qvpge6ijvg5Lf19iKSZ1j0vUAr0KVdPdpu4B-FCRT6_Ch4xCgEF9kQrpH7ESHjDrttMCU2a9HEfSgXDWCbApO0kmM_SfZ9ogkUDxkvBjYBPB8BtS_10oe7Ql9YM5VRz0rQLsNMG5VsOjCpBp_1Ipv5-CegnINaGkuEMLCv-Wjr1S1AnHRFfflayHPIR1aWJ0d4XWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش هزینه‌های هوش‌مصنوعی با Auto Router در Cloudflare
کلودفلر قابلیت جدید Auto Router رو به سرویس AI Gateway اضافه کرده. این سیستم توی لبه شبکه (Edge) پیچیدگی هر درخواست رو می‌سنجه و به‌صورت خودکار بهینه‌ترین مدل رو انتخاب می‌کنه؛ یعنی برای پرامپت‌های ساده مدل‌های سبک و ارزون‌تر رو صدا می‌زنه و فقط کارهای پیچیده رو به مدل‌های گرون می‌سپاره تا بدون افت کیفیت، هزینه‌های پردازش به‌شدت کم بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5447" target="_blank">📅 23:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">من معتقدم با مدلهای رایگان، مدلهای چینی و ابزارهای رایگان هم میشه به خوبی کد نوشت و ابزار ساخت
و به زودی برای اثباتش، یه سری کار انجام میدم
چون میبینم دور و اطرافم کسایی رو که هیچ کاری نمی‌کنن، تلاشی نمی‌کنن، به بهونه‌ی اینکه من اشتراک Claude یا GPT plus ندارم و...
و این کارو انجام خواهم داد که شاید انگیزه‌ای بشه، و شاید ترغیب بشن یه سری افراد که شروع کنن ایده‌هاشون رو بسازن</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5446" target="_blank">📅 21:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ویژگی‌ای که Dots و Cues و Grok Bot دارن نسبت به هرمس اینه که اومدن قابلیت‌ها رو محدود کردن!
بله درست شنیدین
همین محدود کردن قابلیت‌ها خودش فیچر خوبی بوده(برای اکثر مردم و برای مارکتینگ خودشون) و باعث شده کارهایی که میشه باهاش انجام داد ساده‌تر به نظر بیاد و سرراست تر بشه. از اون طرف، چون با LLM خودشون سازگاری صد درصد داره، به 99 درصد ارورهای مدل‌ها و api و... بر نمی‌خورید. VPS هم که نیاز ندارید دیگه
اونور قضیه، هرمس به شما "کنترل" و "هزینه صفر(روی لوکال)" میده که اون هم ارزشمنده برای قشر عظیمی</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5445" target="_blank">📅 16:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بچه‌ها ما قراره استریم داشته باشیم راجب دانشگاه و انتخاب رشته
اگر سؤالی دارید، می‌تونید به ایمیل matinsdungeon@gmail.com سؤالتون رو بفرستید با Subject استریم
روی استریم می‌خونیم سؤالاتتون و جواب می‌دیم با مهمونای گل</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5444" target="_blank">📅 14:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kJUKM38VS1ENiB1gfLquV46k1EUBO9jKETG2LlKK9SQPtMIO2t-Oy9bazJ5vwRjl5c6lT8wMuYblifBvJvtD3oDj-j2DIvMg35GfeDGBh_HPhnW5_4ZbCfSdQXEHDR4qUzS980Yxyh2fvgyhAXzW2jgPInFHOGZyv5HysA0Ph_aKjIeNI-LiKGJo3eyD-ra3s0zQ4bwUWoOyjVbj0Fbs1DdgvCfLxQcmOHFjv5c-hvlYXWESiAf5kNtnziwvXw0lkr_AAgxxA0qFSGwaOwBcKF3cOIzE0Wy285h8bnRhoPS9CEOGxsYK4hewzMENwCFjdqLLYqvm3L7OaE5yjxV3FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری رسمی OpenAI با پلتفرم Hermes
در اعلامیه‌ای جدید، همکاری رسمی OpenAI با اکوسیستم ایجنت هوشمند Hermes(Nous Research) تأیید شده است تا قابلیت‌های مدل‌های جدید و ابزارهای کدکس به شکلی منسجم‌تر در اختیار کاربران و توسعه‌دهندگان این پلتفرم قرار گیرد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5443" target="_blank">📅 14:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بچه‌ها پدی 2500 دلار کردیت OpenAI داره که میخواد باهاش یه اپ بنویسه به انتخاب شما
رأی من زمین بازی سیستم دیزاینه
😂
❤️</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/5442" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5441">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-poll">
<h4>📊 کدوم ایده رو با هم بسازیم؟</h4>
<ul>
<li>✓ تمرین انگلیسی با Shadowing</li>
<li>✓ زمین بازی سیستم‌دیزاین</li>
<li>✓ تبدیل کانال تلگرام به وب‌سایت</li>
<li>✓ ایده‌ی خودت رو بگو💡</li>
</ul>
</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/5441" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ykfuh-cB8yq32rg5t_VetWlMd5jJnLyI_BhZ_MHgAYSYVBf8YXa4iqwYiWIKoUPqmZEb7woVm1FakdcPZmscGkdS_17dWWYwnN_jmzblbIKbla3O6I9M_6QDej08Pr91sG0zA-SNCj_BxLNKT6vCrq4VMtAJosr7O7BaE4k_KzXgI9IN0QLRgv3amZSqDMCgnTdvxmRCahqT8F89jqPdTVTMuCIZZPAbQehM0Zxdmcgj2WuOVCI8_NpCewTRD-uDioW8YUyNaxPQmBm15bpwQz4Trcp9Y6BdnhoaRRH6LwQhpdddHxUg0VESDR7Tc9IJSzbUiak5d2Gb_CD_10EPXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FbooZkZmaJwyNlWODpWAH17U8fyN7CyCzKgVbwxXRyEPyiuNpgCY8h6mwlvPW0lTEXgpV_r3pwLzEVBjExBljAInGjY6__9zP2vuFf6X_oxrseXdHXY576zdg3e_-0s50Vch2JCvZoOrOKzURVkJhw95E8l5jGof4T9eju9OoBEDwxIeCjQutSH-HTfgxIrZNpZuTpFeNgATKWAX5DAyRLRMxMgstZfhyjPgdMOjDYsqGlqd79Du3qNh3pV1bQSZZ0qB7jD1tCGzh9wLreagcMveFPr-qxinGOV0cWn4OeDzptHIX_EPQ_Wrn4JMrDlg4d7lG9I-08tW46NnDmt4OQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قبلا برای این کار شاید 20 دقیقه زمان می‌ذاشتیم.
پیشرفت ai واقعا عالیه</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5439" target="_blank">📅 14:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5437">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pEK8IuSoH7VrhY3lGYHPZgzCEy6XR-GVblyDejn0gWm0MGLLk4zD5WxCQr0pSihF_yCC_jMK-eEMIiHBhfSKp6C9qqeQ7b4LD7mUCUUZkId1mBZj7BwFnirrORDT88pz9klA3Gx-EdbQ7WwArZeqZXYry2kVC0ZRJPg44e_saLaj7aT2eDTgLYyM4C2CmIwUQECR7mh3BITAIPIM-9Eb8zpTspcbWA29m3hJIhY6T9ILtcwmGiC4wr1fHkoTOnhmXU-I4vSBLw-pzDTt8jnPWtHzAA-Jn7sn5ZN64O4tkMtThr9xFx4Fh-tBngdrWksQ8GhmsFjwZX-SbgMma_56jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s6HfgDYu1LUYCgBRtmuSAzsyzJAaEkZsMeSm7fB8ziuzw8O40X_yBMk-5Z4SoYNP0DO8jZ3oFlCe24Yr_2W219J4ZgA_O0IuFIZno76wDs-FnMZJOY7rBY4_xhw1KVmP4k3E-Z-ddLipwAoDb-G-JOJt_RJ0aN5lHarP3dqKb6O19B4UG7WX8UHXWR9Meb3HHsX-ZFWcnVRZ8ReAm7JZjbSgUucjij5gmvc2vB4Q12__ViyQdC1z98GQi1s6hOwJxQbTq5-LGuh86qCWls2hIeaMD6yzCNOHwTmeqFbebQXKNCBzOT8KpceA5Ng6XMhttXFqZ3RysLp_H_n33qYVdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز Manus پلتفرم Cues رو رونمایی کرد
چند ساعت بعدش، OpenAI از Dots
و طراحی بصری ساب ایجنت‌های بامزشون خیلی شبیه هم دیگه‌ست
😂
نمیدونم چه توطئه‌ای در کاره</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5437" target="_blank">📅 12:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گویا همه روی GPT 6.1 Sol مصرف توکن کمتر + قدرت بیشتر تجربه کردن</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5436" target="_blank">📅 11:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">عرضه نسخه ابری OpenAI Codex در رویداد DevDay
اوپن‌ای‌آی بالاخره بعد از شیشصد سال که رقیبش آنتروپیک این قابلیت رو آورده بود، توی رویداد DevDay بالاخره مدل Codex رو به فضای ابری آورد تا توسعه‌دهنده‌ها محدود به اجرای محلی روی سیستم خودشون نباشن و بتونن از راه دور با گوشی یا هر دستگاه دیگه‌ای ازش استفاده کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5435" target="_blank">📅 10:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=NMCsJFcbpWpI7KpHvCoZ_hB1ln7YSqVSXg54e9hvNpnVHzmr47nuIUkp6YIjOIznwDtaTOj0BSKtbVJtfQNDv0fTHCB4Y9pCqatTQmm7DyGvoSJ64V82mM5o2m6h9hwDj6QLurZ0jag6CqR1ZPhXwZXPyZcSbxy3dcNnWnxDuSTxbB63rTy3TZbUfWR2lyQg-xeujO-oXoJi44GNTXsxWBUXgwrWKOm-UzbJexVUqDlSLzLPnuMr0aq8i_hTZhsjSRwmf2kGAurRukATKQ1Km1pYc-LVnyLiOme3BTgdgbg1jx2swgBgyt5zsDudvJ5OJ-GS-zb0NoKTkDNuswyMtA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=NMCsJFcbpWpI7KpHvCoZ_hB1ln7YSqVSXg54e9hvNpnVHzmr47nuIUkp6YIjOIznwDtaTOj0BSKtbVJtfQNDv0fTHCB4Y9pCqatTQmm7DyGvoSJ64V82mM5o2m6h9hwDj6QLurZ0jag6CqR1ZPhXwZXPyZcSbxy3dcNnWnxDuSTxbB63rTy3TZbUfWR2lyQg-xeujO-oXoJi44GNTXsxWBUXgwrWKOm-UzbJexVUqDlSLzLPnuMr0aq8i_hTZhsjSRwmf2kGAurRukATKQ1Km1pYc-LVnyLiOme3BTgdgbg1jx2swgBgyt5zsDudvJ5OJ-GS-zb0NoKTkDNuswyMtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5434" target="_blank">📅 08:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حس می‌کنم یه رقابت خیلی سخت بین سرعت ریلیز مدلهای جدید AI و بالا رفتن قیمت دلار شکل گرفته</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5433" target="_blank">📅 08:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5432" target="_blank">📅 00:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مدل Ember-1 از Fireworks: کارایی Kimi K3 با 40% توکن کمتر
تیم تحقیقاتی Fireworks مدل استدلالی Ember-1 رو بر پایه‌ی Kimi K3 منتشر کرد. تمرکز اصلی روی حل مشکل بزرگ مدل‌های reasoning بوده: تکرار بیش‌ازحد مسیر فکر توی خروجی که گاهی بخش اعظم هزینه‌ی توکن‌ها رو می‌بلعید.
چیزی که من خودمم توی ویدئوی کلاد رایگان، سر اون بازی سه بعدی تجربه‌اش کردم و واقعا افتضاح بود. مدل توی thinking خودش گیر میکرد ده‌ها دقیقه.
امبر با بیش از ۵۰ آزمایش و ۲۰۰ ارزیابی جوری آموزش دیده که شاخه‌های غیرضروری استدلال رو حذف کنه و بدون افت کیفیت و دقت کدنویسی، همون نتایج بنچمارک‌ها رو با حدود ۴۰ درصد توکن کمتر تحویل بده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5431" target="_blank">📅 00:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5430" target="_blank">📅 22:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن
به اسم Dots
تقریبا شبیه Muse، یا Grok Bot
https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5429" target="_blank">📅 22:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5428">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CDzPXy0YwhnvnGPRbJKB-TSAtxqcsvlWXvRwF7SirKxcINq-CARwmZnrEZuwmF7RxbC8L6jWBUQlH54_oi4SQZC6j3zwXFGWuXff1qOffmGv3zq3Pc_DEFd3s-h1hMxt-D5OEhIC9-H6I8dBqYvNKWLNTlgPmPirywSRD-COnjv6ESq1hqSuO5k18D8Uu3mEVUFBrbipWNbiC5KHkzsTt0pnFPLT45JYMFMUU4HeFsP8ok9URjrB0T4wC77ZmBwS_THVqD34DDBDys8ZwY1iMhGOMFnLYwGevsSooH8qAN9CnAhCt1Fc0a6Axcd13VBD7WUq9OvLC9PcPpzDp1Y21Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی خندیدم
توییتر OpenAI کلی گفته بود که امروز به مناسبت Dev Day قراره یه چیز خیلیییی خفن بیاد.
کلی توییت زده بودن
هایپ کرده بودن
حالا حدس بزنین چی دادن؟
GPT 6.1 Sol
😂
😂
😂</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5428" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EGtXlB6lQseza5P3c2j7ju9hj5Kcj9dqQMOH--3j7WZ0Ub7dv4wuR3RivcGd2ij9lqGoot-sKLbaznehnWbTTmha4XIdOxhtRLoNB5iTOBusgNebVDY_UOLfcnrDUPLojWPokiHdNszZQGPejLiaX1vmmSDivLarhR2ltS2lYyWV9HVeo2-l0jCHK2Dc_5EgMq4349EyGbhbp4qKFAbQtVgcijzBCHx1cmV-dVx533MCeNh1Om4zrbrGyf8x-R2_lYiVjHzkcXwWgdXKJiLuDoR0CkN8ikZlIJHuvQ_IsGGi507SeD7mQjru9d4QgcriHVFMhBKxRV0s1Pb-0EXtfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aH_p4Xk4IoNefcKL86GiA9lGQrF9D8pppA3s9MpeYI1fE465h-TyDNeFmEGcf0lj7cC8LRcQSGcZol0qfB9BLH37UK1SO2RpH_6E7ANwQFzZTevNsHPqPZ4uT27vw5XjCzkKqVfLuMI0XFcmeaQcn2ijeVmvwaCsTimxxIfSWCuPfJ9Q49ErJFlJbjD1cpKzhdDROLvOId51WrsuDnqp_1_mPDII1Cp3wHBf39XMClzY8-cCsb9YraH7Rkmxx_niUsroCnssQ7goie0miPEc7IklUJYHwW7Ob5ChC2HQI7HLx7DQIBZoIR_iElep_DogdLsViZsVJy81SYn1TRa6dQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کلی ارتقاش دادم از دیروز که الان داره با یه مدل خیلی ارزون، کارایی انجام میده که Astra نتونسته بود. یه پنل تحت وب نوشتم براش که اینونتوری رو ببینم، یه مدل سوپروایزر براش گذاشتم که بالای سر پلنر باشه و تصمیماتش رو هدایت کنه، بهش حمله کردن و دفاع کردن مقابل…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5426" target="_blank">📅 19:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uDN11s4rHepLaajkFs1qEuzU2EytxSv-Zv33ovIkfNwv5V_viq9q2Lvw-WDX4KOOFi-KyouzoUq5FUbcGCIqCtDmaPnq76BHX4VJEMBE9hDqtpWAw-yj8OI6Ndf3YKksVNaGDqe7EWhNCptI0aqgNU9liRE5L4REC39Nc-qqNrJhW0Fi3DlfdrdNvaPYjPneSHQquSmPLsZM3sYJKuQ7LOH9PzO8eMDhKeVdjgpwvckmWrjHWJy6KF58PwZ15bbv53OCvkKVcxrRSSEGzqFoIuOaO5lQ4sgj8A4WaZi4YAnyD6rB7k1B7TwJ7fmzA4BIeuJ2kZbowMYVZ0JZHq9IRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستیار جدید ماریسا مایر فقط از روی عکس‌های گوشیت می‌فهمه کی هستی
ماریسا مایر، مدیرعامل سابق یاهو، بعد از راند ۸ میلیون دلاریِ seed بالاخره Dazzle رو معرفی کرد:
یه دستیار AI که برخلاف Muse و Instinct، نه خبرنامه‌ات رو می‌خونه نه تقویمت رو؛ کل context از Camera Roll می‌آد. از روی عکس‌ها می‌فهمه چی دوست داری، آخرین سفرت کجا بوده و بچه‌هات به چی علاقه‌مندن.
مثلاً از عکس‌های خود مایر فهمیده خانواده‌اش escape room دوست دارن و چند جایی که نمی‌شناخته پیشنهاد داده
😂
😂
کمی ترسناکه حقیقتا
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5425" target="_blank">📅 18:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ایده بیزنس: یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال" قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط بعدش از…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5424" target="_blank">📅 17:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ایده بیزنس:
یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال"
قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار
هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط
بعدش از سودت برای تبلیغات توی کل شهر استفاده کن و دوباره پول در بیار
سرمایه‌ات که رفت بالا و بالاتر و مردم اعتماد کردن، یهو پول رو بردار و دفترات رو هم جمع کن و فرار کن، همه چیز رو هم بنداز گردن بانک مرکزی و فرار کن د برو که رفتیم</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5423" target="_blank">📅 17:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">در مورد آزمون تورینگ و مقاله‌ی Computing Machinery and Intelligence سرچ کنید و بخونید. جالبه. با اینکه انتقادهای بسیاری بهش وارده که دوست دارم یه روز بشینیم با هم صحبت کنیم راجبش
و دقیقا پرسشیه که اوایل سریال West world مطرح میشه.
"If you can't say I'm human or robot, does it even matter anymore to ask this?"</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5422" target="_blank">📅 15:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یه جورایی حس مور مور میده ویدئو
از شدت پیشرفت علم کامپیوتر، اینترنت، ai و...</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5421" target="_blank">📅 14:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=QRtyywuRN327mHPVZ3FuN_Tg2z7HZAxGkkFRVZe8wx65AIiNTtLz7ioTpXHJ7Wk_d4X6qqHQCg5YmfoApwJ1bkYmI-OmXTnaD8C5qUKPzJeNJzpo7MRK3jUxwR-YZnsX-YaTyyMdKw64XKmhN4o56_N6OUOigZMs9RUWKJa9pE4CrX89Gjo3xfXL5q6kZ55wTiaXQFRVuddoRzghaHj-nUdXdzUsaac_D_0L19xUX_MqGL-Rgw_4UL327xKcD18HWyLDRi7Rsl3YGTp0GpDUrhiPJPrdthnNAjvaYvAXMXrO_SVfvt0tDnE6XgYCqaAcwGDz_O_N3QG1xj-lu0hhGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=QRtyywuRN327mHPVZ3FuN_Tg2z7HZAxGkkFRVZe8wx65AIiNTtLz7ioTpXHJ7Wk_d4X6qqHQCg5YmfoApwJ1bkYmI-OmXTnaD8C5qUKPzJeNJzpo7MRK3jUxwR-YZnsX-YaTyyMdKw64XKmhN4o56_N6OUOigZMs9RUWKJa9pE4CrX89Gjo3xfXL5q6kZ55wTiaXQFRVuddoRzghaHj-nUdXdzUsaac_D_0L19xUX_MqGL-Rgw_4UL327xKcD18HWyLDRi7Rsl3YGTp0GpDUrhiPJPrdthnNAjvaYvAXMXrO_SVfvt0tDnE6XgYCqaAcwGDz_O_N3QG1xj-lu0hhGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«کلاد ساننت 5.5 این رو ساخت. فقط با کد»
این داداشمون
این ویدئو رو توییت کرده و اینطور گفته
ویدئو در مورد پرسشیه که آلن تورینگ، پدر علوم کامپیوتر مدرن و هوش مصنوعی چهار سال قبل از مرگش مطرح کرد:
- آیا ماشین‌ها می‌تونن «فکر» کنن؟
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5420" target="_blank">📅 13:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3a3bcc7a3f.mp4?token=cxRKc3aaJuVrzPz5AByXAk5fAPi5P2IElrc7hT4avTD_C6lrxvPvCEQ1vYxWm44TtkCt7KTUtHN7tpvkQ_6YfuEmP9H0zBsa8XmiWDPY1REDCBBlgDptvzfHGz7dwOo3a549W8pe6VBgFlk9c0OsYs1HBu3PAZP1lV03om0wvBbST4YBwDw0t_CATo1V-8eXaKfuMBjXY0Vt2cgHESrEj7uVhv0MBLhNz114ZgoT6TRjb7-O26xJNJBUtqER2tOdCoCTDAOmFgRZAFxXddnRtfvZv3PoAZ_8hPn4-5CD8aLgocnmvf-hhnf6AexAJzrtHPU7gb5OopaMusylBLV8cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3a3bcc7a3f.mp4?token=cxRKc3aaJuVrzPz5AByXAk5fAPi5P2IElrc7hT4avTD_C6lrxvPvCEQ1vYxWm44TtkCt7KTUtHN7tpvkQ_6YfuEmP9H0zBsa8XmiWDPY1REDCBBlgDptvzfHGz7dwOo3a549W8pe6VBgFlk9c0OsYs1HBu3PAZP1lV03om0wvBbST4YBwDw0t_CATo1V-8eXaKfuMBjXY0Vt2cgHESrEj7uVhv0MBLhNz114ZgoT6TRjb7-O26xJNJBUtqER2tOdCoCTDAOmFgRZAFxXddnRtfvZv3PoAZ_8hPn4-5CD8aLgocnmvf-hhnf6AexAJzrtHPU7gb5OopaMusylBLV8cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل Claude sonnet ۵.۵ توی بنچمارک Terminal-Bench 4.0 نمره‌ی ۷۰.۶٪ گرفت.
بعد این پرامپت معروف بهش داده شد:
«یه کد به HTML بنویس که یه انیمیشن دوبعدی از یه پلیکان سوار دوچرخه رو با گرافیک SVG نمایش بده. نیازی به تست اضافی نیست.»
توی حالت xhigh: یه SVG سالم توی ۴۱ ثانیه، به قیمت ۰.۰۵۷ دلار.
اما توی حالت max: تمام ۱۲۸ هزار توکن خروجی کاملا خرجِ فکر کردن شد، ۱.۲۸ دلار سوخت، و SVG‌ای هم در نیومد.
گاهی سطح Effort/Reasoning بیشتر، فقط یعنی «شکست» با هزینه‌ی بیشتر.
پس الکی درجه‌ی Effort رو بالا نذارید. برای مدلهایی مثل sonnet، همون High-medium کافیه واقعا
🔗
‌
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5419" target="_blank">📅 12:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iELL1UM9-klr_WTEhjzYhuPW_ktxfESbPgV6PK7o7Q6d64AIdRID5RQfLLEUh27rTrVtiqZ2aJmyqy8gBxCzrHPvknF3fklm--wGRGwwpRIocL2afWcS2q62rfI6Fh7ZxHtvYMmDzj61b7_gEVJVYct743AGRvFFlIYBsAmvj_PgHabsEcUTloDF1KEHTK60V-h2WW6G_WM7-U2rpV1fA9dDJoWqkiXP_DzH5USyqYonRnHHWk6Mu7Mo5C-x-eM07kjEJgxf59sPrFRWa0Jq0XneIWWDazZOcmNIIc_PlOnlsdOwyfMz4t5smMCyEkuAxPg0mu0XREfStKVrdieTrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LMRXLHrZsHNLkN2rLC2gV96PNV4uLZCWY48TgozlYxlvM2jZRI_6wx4a9x6T7TravogDpADrhicpOtZvjHfTJJzSmcI4FDM-TzfBAuMTGOdtByHZOg3U8RqxaaeY63FUCVbyTIdcBYVSJn5CLrQ9F6O2MGJimJD2mCUntajRHaVf2eAnZbRVqpaFB7t2XRmXU1Po09s_vYrWf2xhjm3Z3kQx-j6eJwSLDHaQq3QbrhyauZU_r9GHbiMS2ZWTK2adY4zoKh1pXg6_BKRNxdLui4gsaZnRnQPbdEwN3x5YshRA7LHQV9Deaqldidogc2OizFyPrKAissljSPM3zbWchg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با این نسخه از WhiteVPN می‌تونید مشکل فیلترینگ ورکر رو دور بزنید</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5417" target="_blank">📅 10:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5414">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">38.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5414" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5414" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/n1eEdjlrjSkbpiJlmKiyiL5O16udsxKzPjZF1_6pFxYD7ycO6daZufEE76y2ZxTMGXL4uf5R9bMH-XhRVmGx7Nqhv1jfTHWQla7HCsaVPw1krRkl4MqKE087lLHV-8-PA794THlrE5M94CQHU43acZUvgFeWNdwE8wYYcj8lc2TLlkybgiW0NcSP5xiOkAFOz-1x_TODPeeLjSTCzBr7BYogpV3iXz-pdlUeVusMobc67aSQDyIJEdq0reKIJm6mqwksILThJab0wxVAll9TgS8JqzOR3MzEeg5Z9ystqLobh9XQnWOqBWbqBsYtObPaKTyM0NzPlPYNTSXT196Vrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/5413" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S6akznsBAqFI2Y9hp2Z1rbrwsj6DZVn7_RLaD9lBr-MUwrft7nek0dg5quFwe0f-jg1e3eMwehPE4lwhzkPOM6HFqYjApWfcvRajs1ry_LsmjdAHB9Ywh-pQZZr0pt4-q92j2Rg1tgWdTP6PK-MZX7a1iwfHHU-mUbhhbK5VKYnfJWOUmGwAJp5HTB42zkNbT6ExZ4CFE9rDsnKknnU9k6y-iRbR8byvV3Vptj6ENGoHbMDbZlSXrNe9HbOa-4vSyg6x85U3zJdDKmMGimZspOWcp5lCrAC4g2GAurQYiBQdOsEj7dAJ7dXM6l4dcagrrgGFrZ-dtpNuy-BRT78mNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10
اسکیل برتر OpenCode
جامعه کاربری OpenCode فهرستی از ۱۰ ریپوی برتر Skillها برای ایجنت‌های کدنویسی جمع کردن که شامل پکیج‌های اتوماسیون تست، دیباگ خودکار و سینک شدن با دیتابیس که کار روزمره دولوپرها رو خیلی سریع‌تر و روون‌تر می‌کنه.
(حواستون به SuperPowers باشه که خیلی توکن می‌بره)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/5412" target="_blank">📅 07:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">Matin SenPai
pinned «
اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید: https://youtu.be/dQKfkXnThCE  به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5411" target="_blank">📅 03:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/feF6DMht6YuKKKTfkf9C0kNL9vsoT36ViSSs32bPYD4Wou44b0xu_zbxLFG8ywTOCIqtenHH3IhBBADr7rCFnhQFEzYNW8VJJfhMAW1XkcHmlgGwRSq_KMf958JOKSmD0OjQHhuxYbspmlhILBVXmG8Fi8bDNcMQTN63xD1IG0HIQ4fyAZLKIBIc_EiMg7CDKEeAC3FRnQymcP-8WojtWbhHilA_wEM8QA2EGwmtCz1fyIs3v4U3zLCRfUCsuJRdH9CX1ZzqJo7iqESfyOXx1DAOOydGBIFesQxNTRDwDW-H5rxXlL4q3xqTxdgH1hjAr9GUMPJzlIXG-yDbv9ibHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5410" target="_blank">📅 03:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p1CElHNU0tb0IrJ1_pJzGKljvw7JdORJUk6-Pmwpu-CXZNTGM4v6wiVBq2LrMqv-FyY4rrIZrU1uZEhqqYrEA1HgjBOfNye541NJ6VTeEy8LpnWnxyj1vWgfT1UurhvfRUnv_1_gXvr_GLpV0eZXxeIT98QSsFD9BH2KbmxtS8pp7Y3tK-LVI959dkg8bD2g3ZJR-nRxTyDzg712E2LNqttKdB0c7qsOndxpJXjPMjB4JBGUilGNBFxdrrbOjE6DbkUTNLLCV5ofE14kDjxJ_msyShwt12El9ub4_EzkD819dq6TqTf3hUJItcaXMlXZ_fneaqdYx2nhXNvpOIIgPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5409" target="_blank">📅 00:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">هرمس خوبیش اینه که سمجه. اگر از ترکیب هرمس + مدل رایگان(مثل mimo) استفاده کنید، واقعا غصه‌ی توکن سوزی یا انجام کارهای سختتون رو ندارید</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5408" target="_blank">📅 23:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مدل Claude Sonnet 5.5 معرفی شد. هم قیمت با GPT-6 Sol، اما به شدت قدرتمندتر! نزدیک به Opus 5.5  • $2/M input • $10/M output • $0.20/M cache reads 1M context + 128K max output
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5407" target="_blank">📅 23:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LV5ZdCKqhx7hn2aX0qLP4vtw0geeycLl6imvw1zO0ywyikMe7qvS3JWVnQaDygi7xzEMOo2-YfwZKywlPS9BZjQ0Wv0BzoUV4Gbt3_fRm6pUWdervAIeUxOaPTlyJs1f3PnCvQPSxFueWZg2eNAX_IAW0LsEBg8CNJtFWjFNF_TVNScJHHKi7pLLi3ud60uzPbRmY4HgtVehqOFJZ8WrTFOfaYaElyHaofKbZCZyiq0AP4kfsybgkylddJMs60Gwq8W7PjC_2vkwm-iLRspbHhvx2ISU9i8jBP0xkF6nlWxIGRagSFEtj6TvNu6HH73MgVF_AuiJC7f--N3by9oT4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cTcdHplwTEFPaIY2f8hfaQa1XspmZCXCPniXUb2YncLZMcELZNrJB-BM-343_37uSGz4vAnzWaWLBneFnqBoaRqgoHOJSlPh4W5_4Y6YchGXaXWQNrk_Tur1jBd6e49sM9K8ipb83NdjJhB7QPKhqqaKU8M1y7C-xBMoB_klGms_pqPq10h3-br1LNVEVTVDksZNkAIAQV0IcLUNWziiC4csyF1HQzctBhxOtBq_HViKzylD63ji7hGaL9gS8CT4kaLFPTOr1pI37Er_thRS8Y7rwYbIwQv_CdNHWJPWd1nHqwk06u5mk3o4gTnKtTgSfTJKQXO6qUTpHQn3N8023Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5405" target="_blank">📅 22:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5  از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.  هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید. https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5404" target="_blank">📅 21:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82410567b8.mp4?token=A-9m7tqli-tdqcpXCIQvkAS484nqo4JaWnpfxd5IZl_WtRktpvKf-T7H5YLtRo3ZD1nNpnDq-FmiecRCmgF2KvF9WDUo7dBr8clC8V5IrwxPrjMd80RHbGbRxLYGoSY2AII9z6FhZ-ng9g1DHSqZyq33LR00CpOYwlEkBVnXFCg7qP68LDBKYi-JPJS4aFHYlzI9i3IbDFBOJwkRNgk_ejDjecJuiVksKjSp-PB7AHK9hKh6htlzdH4c1wJKm4USjNRgYvQlTUBFwtUc9bcgsYZL5mkHwcaYa8z3cnsWoSxyQgQaaVnHdurHzMnBhD7zbfLDoB0vl_RKd02VJE-KaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82410567b8.mp4?token=A-9m7tqli-tdqcpXCIQvkAS484nqo4JaWnpfxd5IZl_WtRktpvKf-T7H5YLtRo3ZD1nNpnDq-FmiecRCmgF2KvF9WDUo7dBr8clC8V5IrwxPrjMd80RHbGbRxLYGoSY2AII9z6FhZ-ng9g1DHSqZyq33LR00CpOYwlEkBVnXFCg7qP68LDBKYi-JPJS4aFHYlzI9i3IbDFBOJwkRNgk_ejDjecJuiVksKjSp-PB7AHK9hKh6htlzdH4c1wJKm4USjNRgYvQlTUBFwtUc9bcgsYZL5mkHwcaYa8z3cnsWoSxyQgQaaVnHdurHzMnBhD7zbfLDoB0vl_RKd02VJE-KaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5
از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.
هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید.
https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5403" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید:
https://youtu.be/dQKfkXnThCE
به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5402" target="_blank">📅 19:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bjyF8mNX-GggPY22ZnWRs1xrncEv1PRdX-OF-FhtMcXK55WaWp58LoWV-JO-K7TsgkPHMFHZJykufiOiKXWbaeEVH_gjNc4_7v7zqjNKiFrf4NmRKlBNtNaOREEjHr_D1D9eGB2KNra42IqAA8IOmvKS8sBmvJDhDsSl6nwEO4B5w6yjujGNXcXA1xs0-Idifg8NZnvhHRuEFa95x9G_cu3xyVb-ghmqQTbRpX98cO18VYEJbkQxBO61T9vRBJUhovPdZs1E6bti-Jv3s9J2sgVDb4euRu2ipnBtHa8cj_WX84cDv3To2Wb5PEXWOqaQ2daZEH4bjrvRbj2EUtD-qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظه‌ی Hermes: از
MEMORY.md
متنی تا گراف دانش
نویسنده این پست ردیت گفته بودش که مثل خیلی‌ها به دیوار
MEMORY.md
دو هزار و دویست کاراکتری خورده بود (۹۹٪ پر و مدام درگیر نوشته‌های کهنه‌ی توی کانتکست). پس برای همین تصمیم گرفت plugin مربوط به ارائه‌دهنده‌ی حافظه‌ی Hindsight رو توی یه کانتینر Docker جدا راه بندازه؛ بعد از کلی تنظیمات مختلف، اولین اجرا و تجمیع گراف تموم شد.
که این باعث میشه:
1- دیگه محدودیت
Memory.md
رو نداشته باشیم
2- سرعت خوندن از حافظه وحشتناک بالا بره
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5401" target="_blank">📅 19:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LE2juCpbGsnEK6K6SScyiJqWZIRYq8TZAZawVr6uN41v3KspHnBP1ZlC4FYZJr85yhwOHEj27faHOGuL7On-fMvUqvrETjLzpzwm6LambygxF-vc81VsxB68oT6cWS36oVmZfGDK6YbeSL-Xat8batZrZM-EYrvdwmrnmAFrVdek38F2npVt7XDQtiicY7Rlp5_N7SAsDRmFoGssBMK_TN5qnRjY_GNeJ3PYObaHZ_6LjEvYdXg93sE_jlzhLpjbFlBE4G--D2iTzoLWL9Doml52Sd6KEcf4Z1DG-L36075FDpQD2poxnDUnXRoFceznNuKP4kEnCfAUbYmVeJI9Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر کنم گوگل چند صد میلیارد توکن از نسخه 4.6 ساننت و اوپوس خریده برای Antigravity و نمیدونه باید باهاش چیکار کنه
😂
مشتی 5.5 اومد 6 هم به زودی میاد ولمون کن دیگه</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5400" target="_blank">📅 18:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pcdQ_E-yDcDWwAAZ1IgBxyaTKJrcDOpIiy1K4UnaxO994sqI2suiZP8y7DTLH82fMAvt3NhlcokbcQdErVlijvI8NumNPw8yc5DCRUqwuWK-Wl8d37cd683Beh01uGZgt3i44I7zhPDS__Vz3K4qQ4fAFlb4pLTvdAhcJkzrdfV5xPApcK6at9JymAT_FzQEG492w5yE40xbMIqIvOHKPnUxTZ-8ojBYpUmhBX7uZ9F20RjOlbYyeo_oRhB3S0EPEAxhsp0koHVIQpK8YYfHMu4xvjybDWBO_lF9hujI_RRSWLD45o6y1m-u_Te7TVt_Lfohp-TOxOv5z-jgyVmKhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی ساخت نرم‌افزار رو آسون کرد، دیده شدن رو سخت‌تر
قبل از AI برای ساختن به توسعه‌دهنده نیاز بود؛ حالا آدم‌های بیشتری همون چیز رو راحت می‌سازن. ولی تعداد کسایی که حاضرن پول بدن، یهو چند برابر نشده. نتیجه: وقتی ساختن برای همه ارزون می‌شه، مزیت واقعی از ساختن می‌ره سمت توزیع، ایده و شناخت مشتری.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5399" target="_blank">📅 17:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FcIwyBIR24uocaihiFliiKwzZSSJhT7r4qga8kSV-9G2oVFiUSTDN4Pyhp978Q4GvlyygQ46SRc1EX1fUm-fDEGoyPE_l95Hq9TrLZWJPFegJZV19hs3KdVhMUo4TYBMrAv5VqbzuekvniKqancP6ESabb-xVsdE7xgt1tw-fLE8urukRgS25gvXzbxs10mP0vyqxiVB8ed4Dh7M6kOqOwWkWg6LrSWnWsPoBEH0fcb3THWo8Y3_nOpT5XQyyjsP-xkAaTX6Zy_Vmrnt_nWu9cc1hqlpSNPeGzvjC1SQHlrT6PidSZsrBOF_SPhF-_RvE_UMty6w0kzuDfyxLmHlrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JD9Kjjhc81M1VXN4px-NSTC6qzGreFDU5bbC9AD99wCuDJld49k8b0Rnev2iu8nLQ2EY2R5NmQzaVP2zyzzi2SBhDQIXzzPPjIBAAJqpvH4IZdlvK4A7Aw5n2-AtCitf2Gi4LNcHe72y1lE7T9oz6ZiJNYuM1b6qBMZlSqgGpuZWmaG7buRljyaj6brV6_1o0VlmYkZ4WbYqfFq5dNqa2t7OvN3nk06eJT--vHjLgO2vdSiBbkdTELj_phSNUt64ZoNoiLmFJmSYAYG38N4zeH-5hfX4J5xnsnTu6erH6FuRoQUsEx2Zi7snfOVKndXh_7yp_Q6UCkGRC62uF2KPlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این فتوشاپ اوپن سورس که مسخره‌اش کردن یه دوره، سازندش اومد توی ردیت درآمدشو از دونیت‌هاش گذاشت و گفت محصولم خیلی پرطرفدار شده
😂
لینک این فتوشاپ اوپن سورس که اسمش Photon هست:
https://tenzen.studio/photon
لینک پست ردیت:
https://www.reddit.com/r/SaaS/comments/1wsac6d/i_replaced_adobe_photoshop_with_a_free_better/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5397" target="_blank">📅 17:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست
با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5396" target="_blank">📅 16:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/MatinSenPaii/5395" target="_blank">📅 16:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J6iyI7lkqiqKOAQS2QqyVaQ-SL6EbXk7LOnxj_iZaue-td4xDKwrSo8GqRKJWntD7l6Ha_0TpCrDSmQtyB5wynvkYPQq6bH8IwdHm-RcZElBBQSYopNeOsAL6jn8KEnSi3ppmhCSswQ34CkvPquEhMch5nGPHxJp4vsfmHUaLxK0tyZP90RsZMbW55qMngqJvowndED8xFEOfgYOz8SaP7WknZC09hRnCJrYq9yc8YgqH88p7kw0KwtJDLsHNwmI77h2fnLAv1NxUvXoVjd6ws_zhuc0ED7-wQftdhVsl-E2v75UVchvU_rad8tTC85Uj-nr96Ac8v8A3CglwlSxhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5394" target="_blank">📅 15:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O18GOsuMBfPtSr7slBW9xPSSLkgY5NiYDDrDaEvsA-qOLQoT1zxJoX9OZkzKI4C39wnD3mYeQiJJ1nsewY60XMRZnIsgW6Sd7O5MLwj4JcAkIcnpWax3EySn86zqeFxk0CEiLYACmJLt9UdQnSVkA0dhMudch1ycAjBgQZCpLZ4j9UZodyDsvUHC1qWjUEq0oXp7Bg7LN712jqGTVEz2uoelPpc2Knz2E1OVAlge__qjxK4iPH9zTysAjpesc1JkTAO_rVB1Rk--JugPQKwH_Cw61kegE54TrtrGslH5E7hcQfoRlXsdqhZxSN9aM7LEAqYwsLkw2ZUZS5GGj6n3Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک خسته‌کننده نمی‌خواید؟ بشینید جنگ مدلها رو ببینید
🤣
سایت TinyAIArena یه صفحه‌ی ۸×۸ هست که چهار مدل توش دارن واقعی با هم می‌جنگن؛ نه یه جدول امتیاز خشک و خالی. روی هر مچ کلیک کنی می‌تونی تماشاشون کنی و ببینی بالاخره کدوم‌شون باهوش‌تره. کل پروژه هم روی GitHub عمومیه. البته این صرفا سرگرمیه و جدی نیست، اما همچنان برای دیدن اینکه مدل‌ها توی یه محیط محدود چیکار می‌کنن بامزست.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5393" target="_blank">📅 07:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">قضیه‌ی «انسان در حلقه» خودش داره از دور خارج میشه
مارگارت مچل و همکاراش توی یه مقاله استدلال می‌کنن که راه‌حل «انسان رو نگه داریم وسط کار» توی عصر AI، اون‌قدرها هم ساده نیست:
هم طراحی فعلی ایجنت‌ها نظارت مؤثر رو سخت می‌کنه، هم استفاده‌ی طولانی مدت از همین ابزارها، توانایی‌های شناختی خودِ ناظر انسانی رو هم کم‌کم از کار می‌اندازه. پیشنهادشون اینه که نیازهای ناظر رو به‌اندازه‌ی توانایی خودِ ایجنت جدی بگیریم؛ تا هم توی طراحی محصول و هم قضاوت انتقادی تمرین کنه، و هم توی سازمان‌ها با پروتکل‌هایی که اثر اتوماسیون رو جبران کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5392" target="_blank">📅 23:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">بعد از ماه‌ها که برای کلاینتم آپدیتی ندادم این مدت روش کار کردم و کاملا بهینه و بهبود یافته. UI/UX  کاملا بازنویسی شده با متریال گوگل. و خیلی فیچر های شخصی سازی داره بخش "رابط کاربری" از تمام هسته های حال حاضر پشتیبانی می‌کنه راحت میتونید کانفیگ هاشو اد کنید،…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5391" target="_blank">📅 23:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سندباکس‌های ابری Docker برای ایجنت‌های کدنویسی
داکر سرویس Cloud Sandboxes رو منتشر کرده: محیط‌های اجرای امن و میزبانی‌شده روی زیرساخت خودش، با ایزوله‌سازی microVM توی سطح سخت‌افزار. با یه دستور میشه سندباکس رو بین لپ‌تاپ و سرور جابه‌جا کنیم طوری که فایل‌سیستمش هم منتقل بشه؛ یعنی کار رو محلی شروع کنیم و قبل از خاموش کردن لپ‌تاپ بسپاریمش به کلود. هدف، ایجنت‌هاییه که ساعت‌ها کار می‌کنن و می‌خوایم چندتاشون موازی پیش برن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5390" target="_blank">📅 22:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5389" target="_blank">📅 16:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcBVJJbYHYishNNOshlIUd36k3FginwRmuvKF6yQH64xy6gfrzNY41MgEOxdoLXn7VMDAZbw9UO-tSXrYJs_fg3-m6kVE3kxjUFzyci-WN83aRry9rgB2jraDVfMdR2QYHFaLanUlHppSieCH-sjYgVO7MNdYZJhrTcOT5QsAJBqOmwJ8rvhTYdMI2-fGwgI4y2QsjkxDBwqeJieGywqXg6tTzIzPiO3mWdr5lI4Trz_5J2GKk5M9Ug2qP0YDEZUcuuU1u0YevdpyYvheVI6ozwJpX6aZt5RWE2OnTYkuc-_R2jwPWQJTthik9VNv6-2pFB6Z0FNtR20LjIhC18-EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر بلاگش رو از WordPress کوچ داد به EmDash
کلودفلر جزئیات کوچ دادن بلاگ اصلی‌ش از WordPress به EmDash — سیستم مدیریت محتوای متن‌بازی که خودش داخلی ساخته — رو منتشر کرده. EmDash با TypeScript نوشته شده، روی Worker خود کلودفلر اجرا می‌شه و تا ۷۰۰۰ درخواست در ثانیه تست شده، در حالی که بلاگ معمولا ۷۵ درخواست در ثانیه داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5388" target="_blank">📅 15:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f8jpTrQRocJ3nMZtVRnljWd7tFiKvxgW1BCaGmtPqucF-kqbTW0tDo-zoArLzovtmewgqTcJZjzjcplEtMaf2q-kMK7e758QpqWZAsz4u8onpR25bFOj9lkiST8sSEfQAsW862uRfosaqMnAGkguqiiSek0tp62sa_e11rr4aHYbFE-1KA_4hxzJLupRBX2Ik_qV9ZnWLTvDCb3n1KS5KJnG-WXmxhzLNYeGEUC1HyY75bj3w4KM-zpw_P5wxA6rpBDQXmGSl3cTDkhhDAJSz5i5Niy1dkh7D_5ny0PF2yJM7fGTGfqa11r0R2femta0-0I3CeDf0DZ79blG-fxiOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا حس می‌کنیم هر مدل جدیدی که میاد، انقدر از مدل‌های قدیمی قدرتمندتره؟
باید بگم که این بیشتر از منطقی بودن، «کلک» شرکت‌هاست برای مارکتینگ
اگه یادتون باشه، 2 هفته پیش همه‌ی این بنچمارک‌ها(خصوصا سه بعدی) جوری از GPT Astra تعریف می‌کردن و چیزای خفن می‌ساختن که انگار خدای همه‌ی مدل‌هاست.
بعد که Claude Opus 5.5 اومد، خروجی‌هاش رو جوری نشون دادن انگار اون مقابلش پیامبره.
حالا این قضیه برای هر دوی اونا در مورد Gemini 4 Pro داره تکرار می‌شه
به این کار اکانت‌های بنچمارک و Ai Enthusiast ، قضیه‌ی Strawman Fallacy می‌گن. یعنی مغالطه‌ی آدمکِ پوشالی
توی فلسفه، Strawman fallacy یعنی از رقیب قدرتمندت، یه فرض پوشالی بسازی جلوی مخاطب، شکستش بدی، و بعد خودت رو پیروز جلوه بدی
هم خود کمپانی‌ها، هزینه می‌کنن که اکانت‌های توییتری/ردیتی این کار رو انجام بدن؛ هم خود آدما خیلی وقتا این کارو سر هایپ و ... انجام می‌دن.
چه شکلی انجام می‌شه؟
1- مدل رقیب با پرامپت ساده یا بد تست می‌شه، ولی مدل خودشون با پرامپت بهینه‌شده.
2- قابلیت‌های رقیب مثل reasoning، ابزارها یا context بلند خاموش می‌شه.
3- هایپرپارامترهای رقیب به درستی تنظیم نمی‌شه ولی مال خودشون با دقت tune می‌شه.
این شکلیه که می‌گم هیچوقت به بنچمارک‌های این شکلی توییتری، نمی‌شه اعتماد کرد.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5387" target="_blank">📅 14:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rm3LtUQpC99krdRN5HzcQAwzOKK6cISclKZvkh5jcGzwj1G6yjs-XCbnxA1b90_8ebGxxU3fTl6EAIrYieT5oGgsErY-htF9vaq5btENt0yCW2pdwyELGWMCUpWCh9NwM4WhB3xGFCSYLcr9jBg1326xPfh3vQy7kfBXe3kvlRk6kyB8kdvzgObpw56lJiWL513djfdUNpZPJ1nqgIz7bqh2LhSSls6HYjlgyAaxlqNAYftfBjFmEeSqPX4KviawtfXXumwGo6zuBCkoKdPAb_I9oineUETDjIhC6arI4v-gz54RF-70acF3h5DfeWns7BkIkvgJ9XhmHSHBIZ475w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ هزار دیتابیس Supabase داده‌های مردم رو لو داده
پژوهش شرکت UpGuard نشون داده حدود ۱۶ هزار دیتابیس میزبانی‌شده روی Supabase بخشی از داده‌های شخصی‌شون رو عمومی کرده: اسم، آدرس، شماره تلفن و گاهی پسورد و توکن.
و بین اینها دیتابیس یه کنسولگری دولتی توی فرانسه هست، پلاک هزاران خودروی یه پارکینگ، و دیتابیسی که برای دریافت رمز یک‌بارمصرف کلاهبرداری استفاده می‌شده. Supabase که امسال به ارزش ۱۰ میلیارد دلار رسیده می‌گه پروژه‌ها پیش‌فرض امنن و امنیت یه مسئولیت مشترکه.
بخشی از ماجرا هم کدهای Vibe Code شده هستن که بدون پیکربندی درست، داده‌های کاربر رو  لو دادن(شبیه یه بنده خدایی که یه بار پروژه اوپن سورس گذاشته بود با به به و چه چه و بعد دیدیم apiهاش توی کد فلاترش هاردکد شده. (طرف مخالف سرسخت ai بود و میگفت به کد ai نمیشه اعتماد کرد)).
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5386" target="_blank">📅 11:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=PVuxeQsDDEaD5isT0D5IYRmLiCbFyZsYoEV3ugGJQ526WnZZ6taKfir65VfhRd0UgpQHLCrLCGZzoauJNgmK4AkNS5zm3UQOx5pXBS4REn0q7CYVZixjWaJemnaXpOWDrH9DYlGbec5OJtQtr0uTrnetWKCx922IY3Ax_VTAfIEm5HmjIZQLsJfhHZMkgAPFlGCnuirk7DXi8XSLtD3TLlndt7fEs__LBjQ2eXs__MRwhDJFCkmYySDfl7VUApi-r6mkc37-G47bXmRWoQIbC6aWlXr8NlKljALGWRTqvDoewZIaoe_0GW0u4bppgG5H1qIalxTsOIg_rIrSAc5nWLeIsKhUwtYrYYAD3Hn9OzKuBXmybbrbVkYMFVdPujX5b_lMaV3nHzk3FDhxZMIoFUQc1cpzxKjPa2GthAjOYcu_c4EdMRkO9PYq8bAIQJa1_xC853-ARMWv74SBTFkQmreWvnOXuZlArj8C4gHbMojM_IPGF12ZRLIS0Rt0u549WZ5NDdUK4df7xlBTrhy_0gwonmDwNQyJY149lHec2CRTsmr6zoZQfr3CzZ26kh-iRbTFp8h7FCjetcD1rlIk5_WBXh9usUSyWdKtJ2mdMAdSBCKH7Uk7apGaHG_-9M5PZxKJj-IcbLuLV2f3d2XYEOj3g1JTv8_VhGCFBlEt1KU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=PVuxeQsDDEaD5isT0D5IYRmLiCbFyZsYoEV3ugGJQ526WnZZ6taKfir65VfhRd0UgpQHLCrLCGZzoauJNgmK4AkNS5zm3UQOx5pXBS4REn0q7CYVZixjWaJemnaXpOWDrH9DYlGbec5OJtQtr0uTrnetWKCx922IY3Ax_VTAfIEm5HmjIZQLsJfhHZMkgAPFlGCnuirk7DXi8XSLtD3TLlndt7fEs__LBjQ2eXs__MRwhDJFCkmYySDfl7VUApi-r6mkc37-G47bXmRWoQIbC6aWlXr8NlKljALGWRTqvDoewZIaoe_0GW0u4bppgG5H1qIalxTsOIg_rIrSAc5nWLeIsKhUwtYrYYAD3Hn9OzKuBXmybbrbVkYMFVdPujX5b_lMaV3nHzk3FDhxZMIoFUQc1cpzxKjPa2GthAjOYcu_c4EdMRkO9PYq8bAIQJa1_xC853-ARMWv74SBTFkQmreWvnOXuZlArj8C4gHbMojM_IPGF12ZRLIS0Rt0u549WZ5NDdUK4df7xlBTrhy_0gwonmDwNQyJY149lHec2CRTsmr6zoZQfr3CzZ26kh-iRbTFp8h7FCjetcD1rlIk5_WBXh9usUSyWdKtJ2mdMAdSBCKH7Uk7apGaHG_-9M5PZxKJj-IcbLuLV2f3d2XYEOj3g1JTv8_VhGCFBlEt1KU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه. - عاااااشقش شدممم. با کدوم ابزار ساختیش؟ + الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5385" target="_blank">📅 09:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cgZLHcrRH053g8h7NESXrjRV1aeCgsqcxBNfPrwU388k_YGvDJMorWoKzF8OfWUFlp-4r7oewxpvn-NH9oBD9XwmuPFDpUILd5nh5YoxsEuKP9LAe34EqWUObJXIuB1d0BoQOuEQLxlLNB6LGVSSR_BK6aLGXHqukaj96_ITzLZe5a2G19LQiX6iglpwVSshTVMGxq8_PkUp2CfKFpAYElNb2W_MHkpyZPL0OUnxndi6Z4iIAMumOD-cSIeW9rr36Paziyq7T-nUGOShvAZbq-hVflHmm2-VbVaXFIHVxzthFnSJYfQLMY5xgMdi5LMR4L4EL0qxbNl-emX6maQfGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه.
- عاااااشقش شدممم. با کدوم ابزار ساختیش؟
+ الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5384" target="_blank">📅 09:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3r4ZQJK2LREBWZABbu6RO9WsCbmw_2mbBpecSn2Pt9JYeQ9psYAQi9f7E4RQaNYRsDOzjNhwbyG0sJDG-xPQqtQa7NPmX6FQK3c56d-I0vb6oHYa796kxpkWgOghPev1lBASGfN3NzsnIuurOxvjKZU4bo5h4msx0YHImKCNsdvm03rMNuioSue_B7WvWaQCEWz-ju7ThlumdXQ4pr7wq4fC2g62J_5_keTaGCXrLRBxHEn6HOLehhoqiiiX0_kmHHQEHADjmhvmC_5hneXN6qM7HleOoDG7FMk6MhimWOpfZQIDVLbeuu6J--8TMoLDYw3qb8Ur1HXNp5Zx1kwAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولایا (Ollaya)؛ مثل Ollama ولی برای مدل‌های تصمیم‌گیری
خود Ollama، اپلیکیشنیه برای اجرای مدل‌های Open Weight روی سیستم خودتون. حالا Ollaya، همون Decision Models که Jev ساخته رو می‌خواد لوکال و متن‌باز اجرا کنه: سوال تایپ‌شده از هر متن یا JSON میدی و جواب کالیبره‌شده رو توی چند میلی‌ثانیه می‌گیری. جواب از یه پاس روبه‌جلو میاد، نه از تولید توکن‌به‌توکن: حدود ۸ تا ۱۰ میلی‌ثانیه برای ۵ تا سؤال روی RTX 4090، در برابر ۲۳۶ تا ۲۷۶ میلی‌ثانیه‌ی API عمومی Jev. با API سازگار با TypeSafe کار می‌کنه، پس SDK رسمیش بدون تغییر وصل می‌شه و مدل‌ها هم همونطور که گفتم، open-weight هستن.
اما یه بحثی که وجود داره، API خود Jev انقدر ارزونه که فعلا من با اینهمه کار باهاش 5 دلارمو هنوز تموم نکردم. لوکال اجرا کردن لایا هم خوبه اما شاید بهترین گزینه نباشه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5383" target="_blank">📅 07:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wk0zJpyrieXi1__6RZUezSG95n3QqFXAPHeqgkjGAqoLjIPLHaMbpzm3DZn6RZpPrpzJhyfbtLYW8-h63PbtX4wqCOGdmRaw_HREV6ykrC3o0VBXBKtG6WB2foaT1MWMe-pbGQXT3cGe_N33YqkgQdyykLrItLmj2rLxDlnD1dPkGzLQKTldfzirJQhW2bAb7zaCSvPecmfq2B_iO3nNWX-v8-gZlcb90Ka_p1j0jRRVMDznWj_YV-ptshOywJC3h9sZhRZ6UhGHn5FipkJ1OqYgkOnS1c80gE056IkZ5O0vtvKNMLEz0MJAC1x720VTuI_U5Z8CcQwOvQEY7zpTfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک هست دوستان.
گوگل یهو ایران رو تحریم نکرد. سالهاست ما تحریمیم
گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده
این خبر هم اشتباهه
می‌تونید ایمیل بسازید همین الان با گوشیتون و نگران نباشید</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/MatinSenPaii/5382" target="_blank">📅 00:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تانل با دو سه تا یوزر و سرور قوی هر 40 ثانیه یه بار ریست میشه
معلوم نیست دارن چیکار میکنن
کلودفلر هم اکثرا کار نمیکنه واسم آیپیا با نت همراه. فیبر وضعیتش بهتره</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5381" target="_blank">📅 00:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وضعیت اینترنت خیلی افتضاح شده
هم نت هم VPNهای تانل</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5380" target="_blank">📅 00:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpUWa1ZtivyOJxqZHbXKDtFYfgnr6d5Y4B_QqrTp7gctUKfCFSy6ATy218z096J3AfNi_JqeAB5eu55Z0OfDgc8mWKi6LhfxKq-aCSbxVmGmi4Ps3cE05VcAn1CZP5ShSqKcU3d-aTTWaPouqF1bSXy8Q6wHxA70jCdbRcT22bCddEcGi5YQRBukEJ7c_rxepqfd1BxfvOZOPVh2FSDIbnOvqWl41Rs-iQsKzi1J94LBQBzNK72nGy_CN3aaUVYSr8R5aPrBcgTkgAOtFrznrhq1QnmLmnXhQUNIX8pB3OmvwWdeZ9pEWaAb7t4UiLiF0rzYVaKroRfpuCpjkJLagQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رابطی رو که توصیف می‌کنید، ایجنت براتون می‌سازتش
گیت‌هاب توی اپ Copilot یه قابلیت به اسم canvases گذاشته: به زبان ساده توصیف می‌کنی چه رابطی می‌خوای و ایجنت یه سطح زنده برات می‌سازه که هم خودت می‌تونی استفاده‌اش کنی و آپدیتش کنی، هم خود ایجنت. هدفش اینه که وقت کمتری رو صرف تطبیق‌دادن با ابزارها بکنی و بیشتر کارت رو پیش ببری.
این کارا فایده نداره گیتهاب جان. پلن‌هات گرون و به درد نخورن
برو این دام بر مرغی دگر نِه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5379" target="_blank">📅 00:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AM0vB441cKEL1Iw4NIaSiekbQEs7Ayx98cOw6DB8Y4cZo_tPK9AILwNcgvRgJpCWnxQTOe542xrm9GTtoQuq1u1Xwgyu5PbpKtJzZ1sAjHSlOtW52PLx_n5uAbzofmiyJ_WGxPq1RbuEN1GeHHKmHH8-bi5fsTvWs3QlctYYjDBx4jlnVqyrDvyo1OWaU2RYe5-GjTX2k4qA5xKXBGO4QqQbLbiTB9TfmV6IBSzn9BsD3rudCRPw1YycUoTQn2sLvKI7eF9-IA-1pj9RM2ELFJNOUGEl_unokxDmY2ZiH3c0zHBwvPsuIDCQ0-D9AudLI40vpqK-Tls6JRv-AUjxmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">(باید برم ببینم کپچا فارمش چطوری کار میکنه)</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5378" target="_blank">📅 23:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/htLcS5gf3uoRtoh2Vp3AD5veb8LoU7EFry8iTn9VUtOP0HscVtnKa2q3mAGMLWAcIP7FC84XmSBA0rXTFH5QOZNDTPWiEQax1H9_iDUPKmnQ-e9deMeyt7hZwy8ogm_R3eM13Pg16K_rPNM0tOAvY7n0f7Mo4IuVmIT5N1W-mCg0GFxKoL9eo11gZowzDhMzAWsDCBmQkOhK3LtGH5InP5aa7qJzxgZsvhjy8OJDYaE_2fPMZog1xT99xWMTlNAhXLJZpGgWJAlhatDg1cHEPuaGdNbsUmM0HnJ9qxXfLEGCka4kOt5apv_tY1l4o-wQmzRRvj-YaQ4xG5bYuO0qMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر سایتی رو برای ایجنت‌ها به API تبدیل کن، بدون Browser Automation
💪
یکی از توسعه‌دهنده‌ها توی ساب ردیت هرمس ابزاری به اسم
agent-data.dev
معرفی کرده که ایده‌ی جالبی پشتشه.
حرف اصلیش اینه که برای خیلی از کارهای تکراری وب، مثل چک کردن قیمت پرواز هر روز صبح، دنبال کردن آگهی‌های شغلی جدید یا سرچ توی یوتیوب، browser automation رابط مناسبی نیست. ایجنت باید سایت رو باز کنه، بفهمه چی روی صفحه‌ست، هی کلیک و اسکرول و اسکرین‌شات بگیره، و هر بار که لازم شد کل این چرخه رو از اول تکرار کنه. وقتی کار در اصل «این سایت رو با این پارامترها سرچ کن و نتیجه رو بده» هست، خیلی منطقی‌تره ایجنت یه API call بزنه و JSON ساختاریافته بگیره.
حالا این agent-data چیکار می‌کنه؟
1- یه کاتالوگ از APIهای آماده برای سایت‌هایی مثل X، Reddit، Zillow و کلی سایت دیگه داره
2- اگه API مورد نظرت نبود، URL رو می‌دی و توضیح می‌دی چه دیتا یا عملیاتی می‌خوای؛ خودش API رو می‌سازه و نگهداری می‌کنه
3- از طریق HTTP، MCP یا CLI قابل استفاده‌ست، پس برای ایجنت شبیه یه tool call معمولی می‌شه
نکات فنی:
😟
به‌جای HTML selector، endpointها رو روی همون network requestهایی می‌سازه که خود سایت برای لود دیتا استفاده می‌کنه؛ برای همین با تغییر layout کمتر می‌شکنه
📱
خود APIها مرتب تست می‌شن و خرابی‌ها خودکار شناسایی و برای تعمیر صف می‌شن
💰
زیرساخت proxy و CAPTCHA رو خودش هندل می‌کنه(باید برم ببینم کپچا فارمش چطوری کار میکنه)
سازنده‌ش گفته قراره نشون بده این روش در مقایسه با browser automation چقدر سریع‌تر، قابل‌اعتمادتر و از نظر مصرف توکن بهینه‌تره.
🔗
وبسایتش:
agent-data.dev
📌
ردیت
اصلی پست
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5377" target="_blank">📅 22:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این ویدیوی موشن‌گرافیک رو با مدل Opus 5.5 برای یکی از دوستان ساختم. و باید بگم با ۲ خط پرامپت و یه ویدیوی مرجع برای گرفتن اطلاعات و متن ویدیو عالی عمل کرد. عالی  حدود ۴۰ دقیقه زمان برد و دقیق ۲ خط پرامپت با چندتا فایل فونت.
✍️
Saeiid</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5376" target="_blank">📅 21:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=m4cED0GDMUP_j3pC1SI1ZJD7lNyFUHMvlDc03GFg6xERvOD08TpgHSGbdmpaULddK-4flUK4P-_0273X9zRODxsZdWK4QXDXvkK7ORjbA1AgTwZye7tuzBdiw3LFNrXijGcU3kyMxz2-xqYg8xpvl-ZboByzqQh0AKnE72xlVUeO1n6fvuIUhGfHWC7qjnrh760JaFph2kW3dq27_6lo2rOu9lsprsr5xzrYiPFIVhNQxnpq4rqbWXA33c_i9xMnODRCOpFoAwq8r5tPRHNY8Pr5w1p5qLy6JkwFh5pY_yE_eNuaYqJyJdEZn29I3-igLA1R30gMfGmdCQ2RXTFIFw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=m4cED0GDMUP_j3pC1SI1ZJD7lNyFUHMvlDc03GFg6xERvOD08TpgHSGbdmpaULddK-4flUK4P-_0273X9zRODxsZdWK4QXDXvkK7ORjbA1AgTwZye7tuzBdiw3LFNrXijGcU3kyMxz2-xqYg8xpvl-ZboByzqQh0AKnE72xlVUeO1n6fvuIUhGfHWC7qjnrh760JaFph2kW3dq27_6lo2rOu9lsprsr5xzrYiPFIVhNQxnpq4rqbWXA33c_i9xMnODRCOpFoAwq8r5tPRHNY8Pr5w1p5qLy6JkwFh5pY_yE_eNuaYqJyJdEZn29I3-igLA1R30gMfGmdCQ2RXTFIFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5375" target="_blank">📅 20:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FqECmgQyIOQLYHLXXLObbu_L9-1yyrPayegzlFAKaZ5jCN8H1GzULINLO5Bm_xOp9IOQu09LHm50lCfmSZVOA9lFYRrAEM9U4iFCLIV45pDqgFVNrYN6SjO1Ol6LcKidC1FpSH56BSuFvKsJmFT3h2vAyMsM_FvyV6UAwKTVLj2LNyeFJC4jhhcaOLKK28w7rleuopCkXWfA_oTPy7XizZ52CX5tkUvDcw0w7nwzfoSPxmBaNHHlBUYWaV9mRrOU4rUffJsuFkHHVDlhbNSz5LPBkZ139__AyxKVk7EE1oD17W-hEQn2YGyKZcxGJ6Jhjsp7W2p_HW_eRctDuaMzNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RxAu38x0xxySsEwp_5vgb2BFIOqOhm69OTaUZLlkj856Ccf0ZziNCSfeHh4U0PdkDpGnHjvcAGmOb_vXSF0ZtCEvTA-4SQNm-DZ5_3tarMvCVje4NEhqAtNzC7oDn6C0xuNxJDueXi7g_nYJ1rLAc3wyht1efQq2F3HO7V_6zWweEayNdgcwYz2LInk79TYFTGvNOpdpUulTCAOzdBcAY4wL_16ByIet29h5KxTq4AUXHmJRS-3A4tCHU9la5nxjdntsX0pFmwartDLsNwocJaCY40cLfNgMvCAvv1N5jMFZFb6x9GljCeCbZdLD1fueARwvnnJBVlJ4z4NSAmLkBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hFMNNVk2XdJffr1OJ10GDXqdO5k6sEbgKURo7EC4CuGpkGh-Qc2e_-aDKXjR10YummCX013cduax2uePXter6ZUsGQuJohyMIothGGzVOB4SqGhbvtqveerXptNTkptqCtsHy_TXbPSBYNeCwGj6OH-hSuOAhHzr753hfumwxXc5t6KhVJDhk9sVQ5pWO8BIb3765Vh7uPW8gxUZmb_KjyM_b1x6c4kDuZ7Ohm9cL7bwSHlSvM1btosR8zgyATO1lWCDk51Q9fTQ4pFcURz5NLhoZY4vtWCsd3lY018ePGoVzSXGZid1dPH9UHmQVMXAge45z8xx27kAm5tsOmw3bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PsokpisQuLyWfhrjJcCxUqgI42gWGFvviTZ9PmTYY7SO14NEEMo2i0_mcacWWxFmJhwvaL9bdqZT5LUEr2htJYMqqClWKncqiYQtAuGugI8GK-nbiDTg6d6IfQS_qWn1spomB6vS1D_stU3qb-KmbzbF70CWUL1eC5nvstWBtX8NwqCnTHkDz_67NKSrtMhJHCMrbTzLk2SR8uxKL-4-XXLqA9RlWms-inY_RUkFi6AHUIohyTQE2Yb_tjvICGAVlTzHG2Tu11Peb8-M67MBIZr0Ltm-cWgabtj_NTL0o9fCGTd2RHSekSfqVzKivTlf457aJY2hJzj7qGppCMkz4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اروین از توییتر
یه سایت بهم معرفی کرد شبیه به Mpay، اما بیشتر برای بیزنس‌ها یا کسایی که تراکنش نسبتا بالا دارن؛ با قابلیت برداشت مستقیم از کارت و کارت‌های تبلیغاتی برای کارهای حساس مثل تبلیغات گوگل ادز یا تراکنش‌های سنگین و گرون
از اینجا می‌تونید ثبت نام کنید:
https://finup.io/?code=MATINSENPAI
لینک، رفرال هست. اگر دوست نداشتید میتونید کد آخرش رو پاک کنید. برای شما سود یا ضرری نداره
نقاط قوت:
1- برای ساخت کارت، MasterCard داره به جای Visa(شانس قبول شدن آفرهای رایگان معمولا بیشتره)
2- قابلیت برداشت ازش وجود داره به ولت کریپتو(هنوز تست نکردم که KYC می‌خواد یا نه اما توی مستنداتش چیزی ننوشته بود که احراز می‌خواد یا...)
3- آدرس BIN آمریکا داره
4- از ارزهای مختلف برای واریز پشتیبانی میکنه برخلاف mpay که فقط تتر داشت
5- دو نوع کارت بیزنس و تبلیغاتی(هزینه‌شون یکیه) که کارت Advertising شانس پذیرش بالایی برای کارهایی مثل تبلیغات Adsense گوگل و تیک‌تاک و متا و... داره
6- کارمزد رایگان روی برداشت و تراکنش کارت‌ها
نقاط ضعف:
1- هزینه اولیه ساخت کارت 10 دلار هستش
2- برای KYC شرایط ثابتی نداره اما توی تراست‌پایلت نمره‌ی خوبی داره
3- حداقل هزینه واریز به خود کارت(نه ولت)، 50 دلاره
و اروین گفتش زمان واریز مراقب باشید از صرافی‌هایی که امریکا تحریم کرده نزنید. ترجیحا بریزید توی تراست ولتی، جایی و بعد بزنید به ولت این سایت
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5371" target="_blank">📅 19:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=ik_6wffYPWaU67CYG_ALEEJlAyPSgCpZRFTkPjeOs1U_3Y-Vp4zVC-Mfto8uTYhb6NpK-hDvXM0Xv2iPqItcdENeeJ4DqCO3MTmHWJt556ZWTguzloHyomuG_nCkDvCYoJwF5rtXo9vDMYuowLdis8t4T-5Tk9lvlfz-W-x1NYtyrZ0Rol-QCu4VmKHAOJnOEVYXhUZbUk1sWQmthgbAp7YVnz-SWwe0RM4WBx2w6-knjKrmOr6LK5T7kZi5PzbW7fXJtHeak7eHPc78TwFMIQKGuDxX8tOhJQNgHaCL6YPXBjFZhaqDwucgCmDfxjsaE2cm1yl6umZT9x50lzCZx1CdqsLrkMZQmzUdlDbCuQDOnx9gko7lHWZd4qtuQnJZlAB6HIdNPef_EXxqkuhMYbHVgf4YUgoO16mbCy8nATphm2R2QgIdQbVe12rdHHsC4R2D5N5PY1v93rSj7zKzyTVFkoWivbOWNCrRGqQbTjNg7FWx9GwEhFb_RceAWM9UddAxt0VEezU8gelX-na0I6naOHGpAt3vq_liqMX6Rf3CG3ifc6b-DW9zc51cYTMB-lXxnfKpwqAkmkx_OeOuCQPxjAzIupXLqwKPzdLBKbwgVMlcSkfXCTc0hOmwEmjThUNhqj4PDVeMdQ6B8LUJWQuzkwwIXtylKeol2BElREI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=ik_6wffYPWaU67CYG_ALEEJlAyPSgCpZRFTkPjeOs1U_3Y-Vp4zVC-Mfto8uTYhb6NpK-hDvXM0Xv2iPqItcdENeeJ4DqCO3MTmHWJt556ZWTguzloHyomuG_nCkDvCYoJwF5rtXo9vDMYuowLdis8t4T-5Tk9lvlfz-W-x1NYtyrZ0Rol-QCu4VmKHAOJnOEVYXhUZbUk1sWQmthgbAp7YVnz-SWwe0RM4WBx2w6-knjKrmOr6LK5T7kZi5PzbW7fXJtHeak7eHPc78TwFMIQKGuDxX8tOhJQNgHaCL6YPXBjFZhaqDwucgCmDfxjsaE2cm1yl6umZT9x50lzCZx1CdqsLrkMZQmzUdlDbCuQDOnx9gko7lHWZd4qtuQnJZlAB6HIdNPef_EXxqkuhMYbHVgf4YUgoO16mbCy8nATphm2R2QgIdQbVe12rdHHsC4R2D5N5PY1v93rSj7zKzyTVFkoWivbOWNCrRGqQbTjNg7FWx9GwEhFb_RceAWM9UddAxt0VEezU8gelX-na0I6naOHGpAt3vq_liqMX6Rf3CG3ifc6b-DW9zc51cYTMB-lXxnfKpwqAkmkx_OeOuCQPxjAzIupXLqwKPzdLBKbwgVMlcSkfXCTc0hOmwEmjThUNhqj4PDVeMdQ6B8LUJWQuzkwwIXtylKeol2BElREI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم یه ویدئوی جدید از مقایسه‌ی این مدلی که فکر می‌کنن Gemini 4 هست با GPT 5.6 Astra توی یه انیمیشن ساده(هرچند بنچمارک‌های این شکلی اعتباری بهشون نیست کلا ولی خیلی وقتا درست از آب در اومده این مقایسه‌ها توی قدرت دیزاین و درک سه بعدی)</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5370" target="_blank">📅 18:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=CLekLP3fsKtvqGE0jaA5LKyWo_NwxsMuwtq70OjDx53398sb_soW_Ho_MmeYijfWBZNhBMAFIDtN-_9OSPSl51TsOOr24JqGPntVNK0y5Ag7oFGwAd-zdSlEWrELyomMJFSOWcgb180GHFKwLpAplcGxWsh7IYWsOGxnSEcHg0iyQ_NrH_i1NUcMkkHMwPETCqXDgIy4YFlRiynkmiCz-rSrqNfqj3GbFuq8MWB4tRNNw6pBq0BsIvYLWOR-Fy1TwE6N1kDzEiovwKC_zMZZ-m5DMIE9zuZPg_jXjLstWV8NbG6nCYbmuI28Hn8pQ-imV2TbJ-l52BlNDNKsz2mSMw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=CLekLP3fsKtvqGE0jaA5LKyWo_NwxsMuwtq70OjDx53398sb_soW_Ho_MmeYijfWBZNhBMAFIDtN-_9OSPSl51TsOOr24JqGPntVNK0y5Ag7oFGwAd-zdSlEWrELyomMJFSOWcgb180GHFKwLpAplcGxWsh7IYWsOGxnSEcHg0iyQ_NrH_i1NUcMkkHMwPETCqXDgIy4YFlRiynkmiCz-rSrqNfqj3GbFuq8MWB4tRNNw6pBq0BsIvYLWOR-Fy1TwE6N1kDzEiovwKC_zMZZ-m5DMIE9zuZPg_jXjLstWV8NbG6nCYbmuI28Hn8pQ-imV2TbJ-l52BlNDNKsz2mSMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5367" target="_blank">📅 18:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5366" target="_blank">📅 17:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تیم Tokio نسخه‌ی ۰.۹ فریم‌ورک Topcoat (یه فریم‌ورک فول استک برای Rust) رو منتشر کرده که می‌خواد ساختن اپ وب با Rust رو به اندازه‌ی Ruby on Rails راحت کنه.
توی این نسخه ری‌اکتیوی سمت کلاینت جدی‌تر شده: توی macro مربوط به view سیگنال‌ها و عبارت‌های تایپ‌چک‌شده می‌نویسید که به جاوااسکریپت ترنسپایل می‌شن و توی مرورگر اجرا می‌شن، ولی بقیه‌ی رندر و منطق می‌مونه سمت سرور. نکته‌ی جالب‌تر اینکه نویسنده میگه راست بهترین زبان general-purpose برای دنیای توسعه‌ی مبتنی بر AI هست، چون قراردادهای مشخص به مدل کمک می‌کنه با توکن و خطای کمتری کار کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5365" target="_blank">📅 17:03 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
