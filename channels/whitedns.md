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
<img src="https://cdn5.telesco.pe/file/IfnOB_5UEtQmwDEoaOgKvpge8AJrkx9oACIUGt4qTGvQVQYR0JYhQP4_nYRpMkhzTvWVIZ7DO6V40_XpiJnQV9b7nRTcOLRohHcJeOrR2ZV7QiAgRD30_dT7fawdTxPZTveojngBt2EyEAkClgbRZGyTQNHsKXxx5dgt5_TsC9R3HYBBbRDKoxLBLws6yOhmboTgtcwRgbZv6QbaYqPfY9uYz__2PMuLGiA94XzmGR9RzJLDoc7Sv56CJpZSisJEKc7bOK62ZDGf0hvgpFqeB6bW849zpSKraLeZ3fIVkJUbHgqCIvh-J58vH1CMhaae3JilD6R-E4iz0UU_Z82Vbg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 108K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 10:37:33</div>
<hr>

<div class="tg-post" id="msg-1561">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/L6T-vOEz6Ge1csj39i2O5JyqgYaETHaEsz2qdH31Zpk0eQh_LSGUAxZ_hNgr8_fvKONKrWK-AvOInP_MuU1EnzrBVxhtzxdpLlRirBh2wWrJcphJPMJK8wg9mDdNp4gE4_nnxymedXOJ8tij1XHdC32O-_zLdlTntkmFszeo6lQL-4_4AlTe1P9EUlEhGhVcykkZzZS10qVyOUg5PQwCcU2fh3-BOYMMT1Fl4NIpaJwfDAaeFIveBLKHbVdAxjWLU9ncmH13Ppl245ZLx_pBLk_x7a5XpQqYsCqGwStzpjVO2KIYTK2GwsyMGfH2x2WWwHXYqvBsOWXgKIB8odDN3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :
ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.
پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است همیشه کامل یا دقیق نباشند. این ربات به اینترنت زنده دسترسی ندارد، جایگزین پشتیبانی انسانی نیست و اگر اطلاعات کافی نداشته باشد قادر به پاسخگویی نیست. لطفاً اطلاعات حساس یا شخصی خود را برای ربات ارسال نکنید.
برای مدیریت بهتر منابع و کنترل هزینه‌ها، محدودیت استفاده از ربات به شکل زیر تنظیم شده است:
- هر کاربر می‌تواند در هر ۵ دقیقه حداکثر ۳ سؤال بپرسد.
🕒
- سقف استفاده روزانه برای هر کاربر ۵۰ سؤال است.
📊
- در صورت رسیدن به محدودیت، ربات زمان تقریبی انتظار را نمایش می‌دهد.
⏳
- دستور /search و سایر دستورات عمومی شامل این محدودیت نیستند.
🚫
- محدودیت‌ها پس از راه‌اندازی مجدد ربات نیز حفظ می‌شوند.
🔄
این تغییر باعث پایداری بیشتر ربات و دسترسی منصفانه‌تر برای همه کاربران می‌شود. سپاس از همراهی شما
🌱
لازم به ذکر است در صورت سواستفاده این محدودیت بیشتر خواهد شد - پس خواهشمندیم با استفاده درست جلوی به ادامه این خدمات کمک کنید
لینک ربات :
@WhiteDnsResponder_bot
🔗
@whitedns</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/whitedns/1561" target="_blank">📅 18:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1560">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fODO7FlU4-uxrBFO9ZdeDHU_id-0kZnPwn3Hgyv3NP18Rq-8Lkzupm8t-JwR2CZNTKIZKWJgmqb8JSKOKjNrC7nefR3fFpJbKRLkawDffNk4_VmGn4yU45-JvKDrSI4xgZo-6p_9xQlr2jnULte7A8wREpm6GwRyaGGVuoDuJXzCNj_93xvlRiw_k1UsMuaK3pCzBCk-ncR7zJ_gOKyr9wTprkK51dP3ekvwhgUPZL1w462iLwE_QpV962bn3QeAJ198hGBT5X0Q_Jh8vvs6O4yJ9Rm5-0essc0rZvEZQI4K14PvJBsV8TgGfCShby-mmn6orEiiwnwpo_VV_1pNUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteVPN Desktop v1.0.18
زنجیره کردن اتصال (Connection Chaining)
از این نسخه می‌توانید ترافیک را قبل از رسیدن به اینترنت از دو سرور رد کنید.
اتصالی که در صفحهٔ وی‌پی‌ان انتخاب کرده‌اید هاپ اول می‌شود، و سروری که در تنظیمات به‌عنوان هاپ دوم انتخاب می‌کنید جایی است که ترافیک از آن خارج می‌شود.
چطور فعالش کنم؟ تنظیمات ← زنجیره کردن اتصال ← هاپ دوم
پیش‌فرض روی «خاموش — یک هاپ» است و اگر دست نزنید، همه چیز دقیقاً مثل قبل کار می‌کند.
چند نکته که خودِ برنامه رعایت می‌کند:
▪️
سرور هاپ دوم از فهرست هاپ اول حذف می‌شود، تا هر دو سرِ زنجیره یک ماشین نباشند و بی‌دلیل هزینهٔ دو هاپ را ندهید.
▪️
اگر هاپ دوم WireGuard یا Hysteria2 (یا هر پروتکل روی QUIC) باشد، فقط سرورهایی به‌عنوان هاپ اول پیشنهاد می‌شوند که بتوانند UDP را حمل کنند. زنجیره‌ای که هاپ اولش فقط TCP باشد ساخته می‌شود و وصل هم می‌شود، ولی هیچ ترافیکی رد نمی‌کند.
▪️
حالت Automatic همچنان کار می‌کند. اگر هاپ اول قطع شود، خودِ گروه جایگزینش می‌کند و نیازی به اتصال دوباره نیست.
▪️
اگر سروری که به‌عنوان هاپ دوم انتخاب کرده‌اید بعد از به‌روزرسانی اشتراک حذف شود، همان‌جا در تنظیمات به شما گفته می‌شود — نه وقتی که دارید وصل می‌شوید.
⚠️
توجه: دو هاپ طبیعتاً کندتر از یکی است، چون هر سرور باید ترافیک سرور بعدی را هم حمل کند. اگر سرعت برایتان مهم‌تر از لایهٔ اضافه است، همان یک هاپ را نگه دارید.
دانلود: ویندوز (x64 / ARM64) · مک (Intel / Apple Silicon) · لینوکس (deb / rpm / AppImage / tar.gz)
github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
@whitedns</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/whitedns/1560" target="_blank">📅 16:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1558">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/bJKUlFdrEfjZjj_wk1zrM5Mr74tNq74SNoP30nB9GkVfstZfe9WskDMINhrRlFn8pByc873D1c-t-aaiDNdMA9b7_j2So1AeWX4OKdDLyGeOKw1NUMZNirSzWqykBrW5RoNwXS8W8yXmWvufGa2HiraoEvBL5M8NvjIJXCNTw1NfH2k_avglomMTbaI0k0H5DZCOgJbsjKPRjf4hnPp9FJMh2CyMnUmxmtGbPLWSwMFykTsiN9L3HGj2I9g7gP9G-CXt6vFd1NFapHZJ5AgGLcrBP9kWP8dF4KuZS7VNYKdOpAdRLc3AJNsdjXyKhMD-b-_Q8aRRkg2LvKudnpi8jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteAesther Android ورژن جدید
🔥
🔥
🔥
🔥
🔥
نسخه ۱.۲.۱ — رفع سه مشکل اتصال
این نسخه قابلیت بزرگ جدیدی نداره؛ سه تا مشکل رو رفع می‌کنه که باعث می‌شد اپ روی خیلی از گوشی‌ها اصلاً وصل نشه. اگه ۱.۲.۰ داری حتماً آپدیت کن.
🛠
چی رفع شد
1
.پروتکل های wireguard و warp in warp برای خیلی از دوستان اصلاً وصل نمی‌شدن
توی ۱.۲.۰ «ثبت‌نام مشترک بین پروتکل‌ها» رو به‌عنوان یک بهبود اعلام کردیم. اون کار اشتباه بود: وقتی MASQUE هویت رو ثبت می‌کرد، کلید WireGuard روی سرور Cloudflare پاک می‌شد. بعدش هیچ اندپوینتی جواب نمی‌داد و اپ می‌گفت شبکه بسته‌ست — در حالی که مشکل از هویت بود، نه از شبکه.
حالا هر پروتکل هویت خودش رو داره. اگه از ۱.۲.۰ آپدیت کنی حسابت از دست نمی‌ره.
⚠️
در عوض، اون کاهش سه‌برابری احتمال rate limit هم برگشت. اگه زیاد نصب و حذف می‌کنی، حتماً از
Settings ← Identity & access
یک بار بکاپ هویت بگیر.
۲
. عوض کردن پروتکل وسط اتصال، همه‌چیز رو خراب می‌کرد
اگه بدون قطع کردن اتصال پروتکل رو عوض می‌کردی، جستجوی اندپوینت از داخل همون تونل قبلی رد می‌شد — یعنی هزاران درخواست دقیقاً به جایی می‌رفت که قرار بود جایگزینش کنه. نتیجه: هیچی وصل نمی‌شد.
۳
. گیر کردن روی پروتکلی که شبکه‌ات بسته
پیش‌فرض قبلی H3 بود که روی UDP کار می‌کنه. اگه شبکه UDP رو بسته بود تلاش اول شکست می‌خورد و اپ دوباره همون رو امتحان می‌کرد. تا نوبت MASQUE H2 برسه چهار دقیقه و نیم گذشته بود، و عملاً هیچ‌کس این‌قدر صبر نمی‌کنه.
✨
چی جدیده
حالت Automatic — از
Routes ← Manual ← Protocol
گزینه اول حالا Automatic هست و پیش‌فرض هم شده. خودش سریع امتحان می‌کنه ببینه شبکه‌ات چی رو اجازه می‌ده، از H2 شروع می‌کنه (چون TCP روی پورت ۴۴۳ هست و شبیه HTTPS معمولی دیده می‌شه)، و هرچی جواب داد رو یادش می‌مونه تا دفعه بعد از همون شروع کنه.
روی نصب تازه: ۱۴ ثانیه تا اتصال، جایی که قبلاً چند دقیقه طول می‌کشید.
گزارش خطای واقعی — قبلاً اگه جستجو نتیجه نمی‌داد فقط می‌نوشت «اندپوینتی پیدا نشد». حالا می‌گه چرا: بسته‌ها از گوشی خارج شدن و جوابی نیومد (مشکل از شبکه‌ست)، یا اصلاً خارج نشدن (مشکل از مسیریابی خود گوشیه). لاگ خود موتور تونل هم از این نسخه داخل
Settings ← Diagnostics
هست — اگه مشکلی خوردی همون گزارش رو بفرست.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/whitedns/1558" target="_blank">📅 14:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1557">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/hg8MVKMeXyhY1bpAEUytDfx3wr2D_ujm4IO_NIFNIxOBcAlS7r5TREn30KC2D49Cl6P00SFlQxaAb--BxdWLPUIwrrDoeoII-sOCYxwl8V98iFE0Q8M6OIU4A3vNyJlt09bYszeb-9-TEUet2shN3Vhe7pJ6QhKk278itZ_LBiKvRJveve98hMXir84WUik2uDx69LwlZpuHgrr9uNhL_cRmAFVFvn7NNvTOz7Coh8tkZ8l9QFoKcmvSBzB5BB6qNQA_2IImVgixvX-uyTEsglb6KHM9Es6sjh7yiNxADaZq74kfQdAHomOpLS4IDELfzePJTGW9ZyhHZvuzaRg37Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/whitedns/1557" target="_blank">📅 14:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1556">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/UtWWT0g8msBRYCQC58bxNs_66LdxWCEYl_bJtTcqO-Z36MT9EJdtJF8P-_SYSYtR-QKcVhjvSZKoKGXxeRN87z7tsjW-vQb_OR1s0xvB768SgEwMcibnGv4cjNJm6A20YCNqlqpCB7rP72Astw3wDp9XDn1OQ4EJ8Z8pw3MnRi1a0olDCv--dMGxGov9pgiUfE8x83u4asQgv_p95URA-f0hr7Rb5kh5LOwmMmwYqJ7E_ApakomirT0sQCNurlcIWS-hzClhYpewuXxMcjkF4mJEnIHmkykxo_foYzro5yqbPLcw9xn5udoZKVcsD5aotXIAR6ZNYb9zxJ-JJ1xJ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی آزاد و امن به اینترنت با WhiteVPN (نسخه موبایل و دسکتاپ)
اگر به دنبال یک کلاینت یکپارچه، سبک و حرفه‌ای هستید، WhiteVPN با رابط کاربری مدرن در دسترس شماست!
⚙️
قدرت گرفته از هسته Mihomo:
این برنامه بر پایه هسته قدرتمند Mihomo (مشابه کلش و متا) توسعه یافته است که بالاترین سطح پایداری و سرعت را در دور زدن محدودیت‌ها برای شما فراهم می‌کند.
⚠️
توجه مهم:
این اپلیکیشن کاملاً سورس‌باز (Open-Source) است و در Google Play یا App Store منتشر نشده است. تنها منبع رسمی برای دانلود، مخزن گیت‌هاب پروژه است.
✨
ویژگی‌های کلیدی:
🔹
پشتیبانی همزمان از ویندوز، مک، لینوکس و اندروید
🔹
رابط کاربری ساده و اتصال تنها با یک کلیک
🔹
سیستم پراکسی جامع و تونلینگ کل سیستم (System-wide)
🔹
مدیریت پیشرفته سرورها و پایداری بالا در اتصالات
━━━━━━━━━━━━━━━━━━━━
📥
دانلود مستقیم آخرین نسخه از گیت‌هاب (رسمی):
📱
نسخه اندروید (Mobile):
🔗
https://github.com/WhiteDNS/WhiteVPN/releases/latest
💻
نسخه دسکتاپ (Windows / macOS / Linux):
🔗
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
برای دانلود، وارد لینک‌های بالا شده و از بخش "Assets" فایل متناسب با دستگاه خود (فایل apk برای اندروید و فایل‌های نصب برای ویندوز/مک) را دانلود کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/whitedns/1556" target="_blank">📅 14:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1555">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDyU_Fa0E3utecrfAjjlPtwToirB6mvvRoiVdSfQN8xam4eDeu3p6krpnyHJVjHS76RcLj5B4k9jGa40FXSjFII_Ne4AqHp0CKlmKeNATqUs0YevXd4P0ZvzQJhS9VtJ-ErpbiC7zEp7QVMNr-HXqsfXNIiVRofqpGTnGPDITsqItcKy24ymIX_i1ESDfu7LKfcMYegQeA5xEQO5W-q0Nc13u_5SwcvHZnQsMxRYmk1BfEu3oQ08BWc70XQLslTpOJKsVbRJsiKxL4QsbruNHa2mItGpHgHyrEhAptNuypH69ThugdaCRQeNsG6VDkjJLD57rfEuhZeU6itL3SEG3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
WhiteDNS
مسیری که قبل از روزهای قطعی اینترنت شروع شد
تیم WhiteDNS از مدت‌ها قبل از قطعی‌ها و محدودیت‌های گسترده اینترنت فعالیت می‌کرد. از همان ابتدا تلاش کردیم ابزارها، سرویس‌ها و آموزش‌هایی بسازیم که رایگان و در دسترس همه باشند.
در این مدت افراد زیادی به این جمع پیوستند؛ بعضی ماندند و بعضی مسیرشان جدا شد، اما چیزی که ما را کنار هم آورد همچنان پابرجاست:
حرکتی جمعی برای دسترسی آزادتر به اینترنت.
تیم WhiteDNS تا امروز کاملاً مستقل و بدون هیچ منبع درآمدی اداره شده و تمام هزینه‌ها را خودمان پرداخت کرده‌ایم. با این حال، این مسیر را ادامه می‌دهیم و همچنان ابزارها و سرویس‌های رایگان بیشتری را با کمک همین جامعه خواهیم ساخت.
حالا تنها مسیر درآمدی ما کانال یوتیوب WhiteDNS است. اگر می‌خواهید از این حرکت حمایت کنید، کانال را سابسکرایب کنید و ویدیوها را ببینید. همین همراهی کمک می‌کند WhiteDNS مستقل، فعال و جامعه‌محور باقی بماند.
📺
https://www.youtube.com/@WhiteDNS
ممنون که بخشی از این مسیر هستید
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/whitedns/1555" target="_blank">📅 10:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1553">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">WhiteAesther V1.2.0    دو پروتکل جدید، رفع مشکل قطعی، و مسیریابی اپ به اپ  از این آپدیت سه تا قابلیت جدید اضافه شده و سه تا مشکل قدیمی رفع شده. همه‌شون رو اینجا خلاصه کردم.
✅
چی اضافه شد  ۱. دو پروتکل جدید: WireGuard و WARP in WARP  تا الان فقط MASQUE (روی…</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/whitedns/1553" target="_blank">📅 09:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1552">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keaOLXhnqBp9-4DAX--t5zYL-vf9XrBtd7Q2VzumJhh2BPaMZVxnjBjwWyBxrIrfZG3j3GgH6pYP_7r76iOv1V9GGenR8iHnbP8JArTYTOG7GlUCCvbK2067MFZHgFpdlP6X3q8qMIR49y05xOxWBZGJoVtwZsZJlYORl4ZNTlEu_DDlccWHUxXYaEeeQFaiNtAhEcI9Uokph98ygAMif-wczfjbn7hQSS2x4KroLvev7uMMF5mIqbRVg6dSiW1-kDqfOcF9gSdXibejnTv2u0GFOc4R48gl4mDToDBNgqj-Ddob55vl0jhpHeXUO7qk7Y2sMeQQTHV2H3OoCBUJtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همه دوستان عزیز
✍️
از دیروز گزارش های زیادی روی WhiteVPN روی گوشی های قدیمی گرفتیم که بهمون گفتید نصب نمیشه، یا نصب میشه ولی میزنید روی اتصال، اررور میگیرید.
ما سعی کردیم توی ورژن ۱.۶.۱ که از لینک زیر میتونید دانلود کنید این مورد رو حل کنیم.
حالا گوشی های اندروید قدیمی‌تر هم میتونن بدون دردسر وصل بشن.
همچنین مشکل کانکشن هایی که camouflage داشتند هم توی این ورژن حل شده.
تغییر دیگه،ای نداشتیم  جز این دو مورد.
دانلود آخرین نسخه
https://github.com/WhiteDNS/WhiteVPN/releases/latest
با تشکر
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/whitedns/1552" target="_blank">📅 06:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1550">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CDmOT24s56_Ay2cVlosEyLEJMcl9N8OVOKimskz-1mRWvUg89ngrQ1R9fwxxzpnXCQ9nZC0HJjI4Bj0qnlYEQg3BGEtRRzlBllY16kWcvSlaynYtsRB9l_RQhvPgXbvB_1pqTzXuj47pLCra7NzU9GH49RJ4ua7RqZPia_13J_JXapWCR9_MBjvxzBjgkZsnnuSZPeJ8BsiRFp7Otmocg0pw14jGiNPvx3thUP2mteOvK_G-aLR549HuzGvVXrVVaAyRbBxQmpucHb49w9oV1e6kk7yOuHvVwYTveBHaV_a26IWGcY7qnsA_8pr85yq0iiUa3B_6VGUkvikHoLQHMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gnY4pYNGacH6eZK01crxVRG5zvwJ54bR0yUGL0EVOXWcFgpFZTbzRBMIxe_JoD4cjZV0DLGpYbYN8LpMGTS0hSb-lzU7g6iD1S-0mHWOYER4KO-tAP-Hqo6ggFGKcS9PifVffF47CROLVPJjkg8Jgwm6E5-or5B1xxaIDLiquRFCUVA0pvjrP-oawdDkTlg9iM_fbLZmOaM2jFgY07uSxAkGeAJRC7XG1tfRxwB5alPwWAj_iUWn_aaJeJBQ0kExCRfrqyf9j93Wsakm4j9z0UEe14gxHgi49F7Z0lKAvF2-XayQNNez_9nfHaZyD-YM9QVIZg076SOHLiZPfy59IQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان عزیز
لینک ساب رو باید بعد از کلیک کردن روی دکمه Raw مشابه به عکسی که گذاشتیم کپی کنید.
لینک
صحیح WhiteDNS Sub
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/whitedns/1550" target="_blank">📅 05:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1548">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCore Forge</strong></div>
<div class="tg-text">🚀
CoreForge Build آپدیت جدید منتشر شد
https://testflight.apple.com/join/DRkT6zny
این نسخه یکی از بزرگ‌ترین آپدیت‌های CoreForge تا امروز محسوب میشه.
از Build 90 تا Build 100 طی حدود ۲۰ روز:
• 214 Commit
• بیش از 411 فایل تغییر کرده
• بیش از 86,000 خط کد جدید اضافه شده
• چند Engine و Protocol جدید از پایه اضافه شده
• بخش بزرگی از سیستم Connection، Routing، Failover و Config Management بازطراحی شده
###
🧩
پروتکل‌ها و Engineهای جدید
🔹
OpenVPN
* پشتیبانی مستقیم از فایل‌های .ovpn
* UDP و TCP
* AES-GCM / AEAD
* AES-CBC برای بعضی سرویس‌های قدیمی‌تر
* TLS-Crypt
* Multi-Remote / Multi-Address
* Username / Password
* Client Certificate
* OpenVPN Subscription
* پشتیبانی بهتر از ProtonVPN، VPNGate، SoftEther و کانفیگ‌های مشابه
🔹
Tailscale
* اتصال مستقیم به Tailnet
* انتخاب Exit Node
* MagicDNS
* مدیریت Account داخل CoreForge
* امکان اتصال به Exit Node حتی بدون انتخاب Config معمولی
🔹
Cloudflare WARP / MASQUE
* WARP به‌عنوان یک Outbound واقعی
* MASQUE روی HTTP/2 و HTTP/3
* امکان استفاده داخل Chain
* WARP Endpoint Scanner برای پیدا کردن Endpoint بهتر
* تست Endpoint با handshake واقعی MASQUE، نه فقط TCP Ping
🔹
mKCP
* پشتیبانی از mKCP مربوط به Xray
* همه Header Typeهای اصلی
* قابل استفاده با VLESS و Trojan
🔹
ECH
Encrypted ClientHello حالا به صورت واقعی داخل CoreForge اجرا میشه و برای بعضی Transportها از جمله Hysteria2 هم اضافه شده.
###
⚡
Load Balancer و Failover
Load Balancer فقط اسم نیست و حالا Connectionها واقعاً بین Nodeهای انتخاب‌شده مدیریت میشن.
همچنین:
* Config فعال داخل برنامه نمایش داده میشه
* Exit IP بعد از تغییر Node آپدیت میشه
* Dead Server Detection سریع‌تر شده
* Backup Node از قبل آماده نگه داشته میشه
* اگر Config فعلی از کار بیفته، CoreForge می‌تونه بدون Disconnect کامل به Backup منتقل بشه
* Backup Pool بعد از Failover دوباره پر میشه
###
🌐
Routing
سیستم Routing هم تغییر زیادی کرده:
* Routing Profile شبیه Shadowrocket
* Rule Actions
* Iran Direct Preset
* Iran 2026 Rules
* category-ir
* Import کردن Routing Rules از فایل
* Fragment به‌عنوان Routing Target
###
📂
Configs و Subscriptionها
مدیریت Configها تقریباً کامل بازطراحی شده:
* Swipe برای Ping / Edit / Share / Delete
* Drag & Drop برای مرتب کردن Sectionها
* Groupهای Local
* Bulk Actions
* forge:// Chain Links
* Tap-to-Ping-and-Connect
* Import QR Code از داخل عکس
* Subscription Folder
* Rename / Reorder / Export
* Auto Update جداگانه برای هر Subscription
* Plan Status
* تقویم شمسی
مشکل فایل‌های OpenVPN بزرگ هم برطرف شده؛ برای مثال اگر یک فایل شامل ده‌ها یا صدها Profile باشه، دیگه همه‌ی اون‌ها به‌عنوان یک Config خراب Import نمیشن و Profileها جدا میشن.
###
🔧
Fixهای مهم
در این نسخه تعداد زیادی Bug مهم هم برطرف شده، از جمله:
* Crash روی تعداد زیاد Config
* مشکل Import بعضی لینک‌های VMessAEAD
* مشکل gRPC پشت Cloudflare
* مشکل XHTTP که Connect می‌شد ولی Traffic عبور نمی‌کرد
* مشکل REALITY و extra
* اصلاح UUIDهای VLESS
* Lag شدید Config List
* Writeهای اضافی Keychain
* آپدیت نشدن Connection Details بعد از Failover
* UDP برای VMess، Shadowsocks و SOCKS
* UDP Associate برای Trojan
* gRPC MultiMode
* pinnedPeerCertSha256
* PattNG Fragment / Cipher Suite / Unsafe Fingerprint
###
📱
iPad و UI
* پشتیبانی بهتر از Stage Manager
* Split View
* Resizable Window
* تغییرات Liquid Glass
* اصلاح Light Mode
* بهبود Tab Bar و Headerها
---
⚠️
نکته مهم درباره Build
این نسخه تغییرات خیلی زیادی داشته و طبیعتاً
۱۰۰٪ تضمین نمی‌کنیم که تمام قابلیت‌های جدید روی تمام Serverها، ISPها و Configها بدون مشکل کار کنند.
بعضی قابلیت‌ها هنوز در مرحله‌ی تست واقعی توسط کاربران هستن و ممکنه روی یک Server عالی کار کنن ولی روی Server یا Network دیگه Fail بشن.
به‌خصوص قابلیت‌های جدیدی مثل:
Tailscale / WARP / OpenVPN / ECH / Chainهای پیچیده / بعضی حالت‌های VLESS و REALITY
هنوز نیاز به تست گسترده روی Serverها و اینترنت‌های مختلف دارن.
پس اگر چیزی Connect نشد یا Connect شد ولی Traffic نداشت، حتماً گزارش کنید و در صورت امکان Config، Log و نوع اینترنت رو هم بفرستید.
Build بیشتر از اینکه «نسخه نهایی بدون باگ» باشه، یک جهش بزرگ برای CoreForge ـه و Feedback شما مستقیم روی Fixهای نسخه‌های بعدی تأثیر می‌ذاره.
🛠️
CoreForge Build
⚒️</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/whitedns/1548" target="_blank">📅 15:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1545">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/XbPdI5riCiQ3zad9sxtT1lqVcKYNm6pOEiLxe2d-6V9j3Ydsnc-4-QUH5mdkx6BXic9hzDj_NzGHp2ZtfuQWAcGc-2-5b517MdYeZhsgnKVQx823lnrwx5kcohjC951U2rNxn4yUJ9WX1d4N3UEugNA5hirrrBTeUB0Z1TbGD3h0vCTGrRWHUSUWYqhIjEF1aM8M_2clgCHOnHHP-Uwn8c2qFtO1kKgEAxausZsXTe4CKD_W4IZo3aan3tpokFiXUv01YfIr3AP-ri9Dthg4ktHj1h5gekX6PiHzEBIo80wxrBgqPrgHdRpgfQfhzQkfV6d5IanKEIKSqzYs2UsKIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther
V1.2.0
دو پروتکل جدید، رفع مشکل قطعی، و مسیریابی اپ به اپ
از این آپدیت سه تا قابلیت جدید اضافه شده و سه تا مشکل قدیمی رفع شده. همه‌شون رو اینجا خلاصه کردم.
✅
چی اضافه شد
۱. دو پروتکل جدید: WireGuard و WARP in WARP
تا الان فقط MASQUE (روی H3 یا H2) داشتیم. حالا از Routes ← Manual ← Protocol می‌تونی این دو تا رو هم انتخاب کنی:
▫️
WireGuard —
سریع‌تره، ولی روی UDP کار می‌کنه
▫️
WARP in WARP —
یک تونل داخل تونل دیگه، کندتر ولی شناسایی‌ش سخت‌تره
⚠️
هر دوی این‌ها UDP هستن. اگه شبکه‌ات UDP رو کامل بسته باشه (مثل همراه اول این چند وقت اخیر) اصلاً وصل نمی‌شن — اونجا MASQUE H2 که روی TCP کار می‌کنه انتخاب درسته.
۲. بکاپ هویت — راه‌حل قطعی مشکل «چند بار نصب کردم دیگه وصل نمی‌شه»
دلیل اون مشکل این بود که هر نصب، یک هویت تازه از Cloudflare می‌گرفت، و بعد از چند بار ثبت‌نام از یک آی‌پی، دیگه هویت جدید نمی‌داد. حالا می‌تونی هویتت رو قبل از حذف اپ ذخیره کنی و بعد از نصب مجدد برگردونی.
۳. Split tunnel — انتخاب اینکه کدوم اپ‌ها از تونل رد بشن
از Traffic ← Apps: همه اپ‌ها، فقط چندتا اپ خاص، یا همه به‌جز چندتا اپ خاص (مثلاً بانک یا اپ‌های داخلی).
🛠
چی رفع شد
▫️
ثبت‌نام مشترک بین پروتکل‌ها — امتحان کردن هر سه پروتکل قبلاً ۳ بار ثبت‌نام می‌خرید. حالا یکی مشترکه.
▫️
WireGuard و WARP in WARP دیگه روی "trying" گیر نمی‌کنن — از تا ۹ دقیقه بی‌نتیجه، به معمولاً چند ثانیه.
▫️
باگ ساب عوض‌شده که نودهای قدیمی رو نشون می‌داد — درست شد.
📌
آموزش: Split tunnel
۱) Traffic ← Apps
۲) یکی از سه حالت: All apps / Only these apps / All except these
۳) با سرچ اپ‌های موردنظر رو پیدا کن و سوییچشون رو بزن
برای بانک یا اپ داخلی: All except these بزن و همون یکی دو تا رو انتخاب کن.
📌
آموزش: بکاپ هویت
Settings ← Identity & access → Save a backup (قبل از حذف اپ) / Restore from a backup (بعد از نصب مجدد)
⚠️
این فایل مثل رمز عبوره، رمزگذاری نشده — جایی نگهش دار که رمز عبور نگه می‌داری.
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
@whitedns</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/whitedns/1545" target="_blank">📅 12:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1535">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/No8tLDI3hnlR2SqPU0PhSLVYYlphykifQy-jKRTD6BuVGw-Ngo6NhscfRfZoXxmVHdKgKB7oOIH7QpDsMmXSbitd-apMGtZRBqdklloKhxB5LktZzq6-TSszk1QPshGoCadyH6ptqiKEq29OL34vceQC82ax-h9mjreLHVz4n6y3XWduI7SdMQdOzQ2vPfgjAFwoulCzfdn82Ei2cki9vFKNgL5pbihk87VKI0oyw6XWBoIQZKx1mc-oCCydyhqaTBc3ZIx_lGQ7XpaAV1JLWP7BXQarGzX8bbfYnGV-EVMnpGt5DdND9hEFK9GVV94M585cp6lNzdigepMTBMDPCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteVPN v1.6.0 منتشر شد
🚀
یکی از بزرگ‌ترین به‌روزرسانی‌های WhiteVPN آماده است؛ با امکاناتی که اتصال‌ها را قدرتمندتر، انعطاف‌پذیرتر و قابل‌کنترل‌تر می‌کند:
📺
پشتیبانی کامل از Android TV
🔗
زنجیره کردن دو اتصال برای امنیت و انعطاف بیشتر
🛡
پشتیبانی از
AmneziaWG v3
و تنظیمات پیشرفته WireGuard
📥
وارد کردن مستقیم لینک‌های
Hysteria2
و
WireGuard
⚡
تست اتصال‌ها از تمام سابسکریپشن‌ها
🌐
بهبود سازگاری، پایداری و رابط فارسی
اگر از WhiteVPN استفاده می‌کنید، همین حالا به نسخه
۱.۶.۰
به‌روزرسانی کنید.
این نسخه با کمک بازخوردهای شما ساخته شده است. اگر مشکلی دیدید یا پیشنهادی داشتید، حتماً در گروه با ما در میان بگذارید.
🤍
WhiteVPN v1.6.0 — دو مسیر، یک اتصال قدرتمندتر.
📥
Github Release
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.0</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/whitedns/1535" target="_blank">📅 09:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1534">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">از این به بعد کانفیگ های بیشتری داخل ساب ما خواهد بود.
هر ۳۰ دقیقه بیشتر از ۲۲۰هزار کانفیگ جدید تست میشن و خروجی اونها بین ۲۰۰۰ تا ۳۰۰۰ کانفیگ با کیفیت و سریع خواهد بود.
تعداد کانفیگ های حاضر: ۳۳۵۳
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/whitedns/1534" target="_blank">📅 07:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1531">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">https://github.com/iampedii/whitedns-sub
لینک ساب برای استفاده در برنامه های white</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/whitedns/1531" target="_blank">📅 18:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1528">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👆
whiteAesther  android V1.1.0
در این نسخه از اپ اندروید شما میتونید با  قرار دادن یک کانفیگ ای پی خودتون را ثابت کنید و احتمالا خیلی از مشکلات مربوط به Gemini , Chatgpt و بقیه هوش مصنوعی ها و وبسایت هایی که روی لوکیشن حساس هستند  حل خواهد شد
نکته  خیلی مهم برای نسخه اندروید :
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
بسته به نوع کانکشن و موارد دیگر ممکن هست 1-5 دقیفه بار اول طول بکشه که شما موفق به اتصال بشید . ولی در دفعات بعدی این موضوع خیلی سریع خواد بود .</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/whitedns/1528" target="_blank">📅 17:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1527">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">WhiteAesther
android V1.1.0
🔥
🔥
🔥
🔥
🔥
🔥
قابلیت Exit Chain
از این نسخه می‌تونی بعد از تونل، یک ایستگاه دوم اضافه کنی.
یعنی چی؟ تا الان ترافیک تو از سرورهای Cloudflare بیرون می‌رفت و سایت‌ها آی‌پی Cloudflare رو می‌دیدن. حالا می‌تونی سرور شخصی خودت (یا سابسکریپشنی که داری) رو آخر مسیر بذاری، و سایت‌ها آی‌پی اون سرور رو ببینن.
مسیر ترافیک این شکلی می‌شه:
گوشی ← تونل رمزنگاری‌شده ← سرور خودت ← اینترنت
به چه دردی می‌خوره؟
▫️
سایت‌هایی که آی‌پی‌های Cloudflare رو بلاک کردن (بانک‌ها، بعضی سرویس‌های خارجی، بعضی بازی‌ها)
▫️
وقتی به آی‌پی یک کشور مشخص احتیاج داری
▫️
و مهم‌تر از همه: اگه شبکه‌ات اصلاً تونل رو بلاک کرده، می‌تونی تونل رو دور بزنی و مستقیم از سرور خودت استفاده کنی
پروتکل‌های پشتیبانی‌شده: vless vmess trojan shadowsocks hysteria2 و بقیه — چه لینک سابسکریپشن، چه کانفیگ تکی که دستی می‌چسبونی.
📌
آموزش — ۵ قدم
۱) اپ رو به نسخه ۱.۱.۰ آپدیت کن.
۲) برو به تب Routes ← گزینه Exit chain.
۳) کلید Exit chain رو روشن کن.
۴) توی کادر Add a subscription لینک سابسکریپشنت رو بذار و Add رو بزن. اگه فقط چند کانفیگ تکی داری، از Paste nodes by hand استفاده کن — هر کانفیگ توی یک خط.
۵) برگرد به Home و وصل شو. تمام.
⚠️
سه نکته که حتماً باید بدونی
۱. لیست سرورها فقط بعد از وصل شدن میاد
قبل از اتصال قسمت Nodes خالیه و این ایراد نیست. سابسکریپشن تو از داخل تونل دانلود می‌شه تا شبکه‌ات نفهمه داری چی می‌گیری. پس اول وصل شو، بعد برگرد به Routes ← Exit chain تا لیست سرورها رو با پینگ‌شون ببینی.
انتخاب سرور قطع و وصل نمی‌خواد — روی همون اتصال جابه‌جا می‌شه.
۲. گزینه Dial nodes through the tunnel
پیش‌فرض روشنه و بهتره روشن بمونه: شبکه/اپراتور تو هیچ‌وقت آدرس سرورت رو نمی‌بینه، و سرورت هم آدرس واقعی تو رو نمی‌بینه.
🔸
ولی اگه اپ اصلاً وصل نمی‌شه یا خیلی طول می‌کشه، این گزینه رو خاموش کن. اون‌وقت WhiteAesther تونل رو کامل رد می‌کنه و مستقیم به سرور خودت وصل می‌شه — دقیقاً برای شبکه‌هایی مثل همراه اول که تونل رو می‌بندن، همین حالت جواب می‌ده و خیلی سریع‌تر هم وصل می‌شه.
۳. Coverage باید روی Whole device باشه
توی تب Traffic. اگه روی Proxy only باشه، Exit chain کار نمی‌کنه و اپ بهت تذکر می‌ده.
💾
حجم اپ بیشتر شده
از حدود ۸ مگابایت رسیده به ۴۷ تا ۵۷ مگابایت. دلیلش موتور جدیدیه که این قابلیت رو اجرا می‌کنه. اگه Exit chain رو روشن نکنی، اپ دقیقاً مثل قبل کار می‌کنه.
▫️
arm64-v8a — تقریباً همه گوشی‌های ۲۰۱۷ به بعد. از این شروع کن
▫️
armeabi-v7a — گوشی‌های قدیمی‌تر و اقتصادی
▫️
universal — اگه مطمئن نیستی (حجمش سه برابره)
⬇️
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
اگه مشکلی خوردی، از Settings ← Diagnostics گزارش بگیر و بفرست — از این نسخه لاگ موتور Exit chain هم داخلشه.
@whitedns</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/whitedns/1527" target="_blank">📅 17:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1526">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">📺
خبر خوب برای کاربرهای Android TV
در ورژن بعدی WhiteVPN پشتیبانی کامل از Android TV اضافه شده. تا فردا نسخه جدید اپ اندروید هم ریلیز میکنیم
❤️</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/whitedns/1526" target="_blank">📅 17:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1525">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👆
whiteAesther V1.5.2 desktop
در این نسخه از اپ دسکتاپ شما میتونید با  قرار دادن یک کانفیگ ای پی خودتون را ثابت کنید و احتمالا خیلی از مشکلات مربوط به Gemini , Chatgpt و بقیه هوش مصنوعی ها و وبسایت هایی که روی لوکیشن حساس هستند  حل خواهد شد</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/whitedns/1525" target="_blank">📅 16:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1524">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">whiteAesther
V1.5.2 desktop
🔥
🔥
🔥
🔥
🔥
🔥
🔗
قابلیت جدید: Exit chain (زنجیره‌ی خروج)
🔥
🔥
🔥
تا حالا وقتی وصل می‌شدید، ترافیک‌تان امن و رمزنگاری‌شده بود — ولی آدرسی که سایت‌ها می‌دیدند همچنان نزدیک خودتان بود. این ایراد ما نبود: WARP کلادفلر عمداً کشور شما را عوض نمی‌کند، از نزدیک‌ترین نقطه خارج می‌شود و همان‌جا را هم geolocate می‌کند. برای همین خیلی‌ها بعد از اتصال موفق، باز هم به سرویس‌های خارجی دسترسی نداشتند.
Exit chain یک هاپ دوم اضافه می‌کند. ترافیک اول از تونل رد می‌شود، بعد از داخل تونل به نود خودتان می‌رسد و از آنجا وارد اینترنت می‌شود. آدرسی که سایت‌ها می‌بینند، آدرس نود شماست.
دو نکته‌ی مهم در طراحی:
▫️
نود از داخل تونل شماره‌گیری می‌شود — یعنی شبکه‌ی محلی شما فقط یک اتصال عادی به کلادفلر می‌بیند، نه آدرس نود و نه SNI آن.
▫️
به همین دلیل، نودی که از ایران فیلتر شده باز هم کار می‌کند — چون از شبکه‌ی کلادفلر به آن وصل می‌شویم، نه از اینجا.
━━━━━━━━━━━━━━
📘
آموزش
۱. بالای پنجره روی Advanced بزنید، از منوی سمت چپ Exit chain را انتخاب کنید.
۲. دو کلید را روشن کنید:
• Route through a second hop — خود قابلیت
• Dial nodes through the tunnel — پیش‌فرض روشن است، همین‌طور بگذاریدش
۳. نودتان را اضافه کنید، به یکی از دو روش:
• Subscriptions — لینک ساب را بگذارید و Add بزنید (خودش به‌روز می‌ماند)
• Configs pasted by hand — کانفیگ‌ها را خطی یکی paste کنید و Apply بزنید
vless · vmess · trojan · ss · hysteria2 · tuic همه مستقیم پشتیبانی می‌شوند؛ لازم نیست چیزی را تبدیل کنید.
۴. پایین صفحه در بخش Nodes نودها ظاهر می‌شوند با پینگ واقعی‌شان از پشت تونل. با Test هر کدام را بسنجید و با Use یکی را انتخاب کنید.
۵. بالا سمت راست Save profile را بزنید تا دفعه‌ی بعد هم فعال باشد.
━━━━━━━━━━━━━━
⚙️
کدام حالت را انتخاب کنم؟
• Whole machine — کاری لازم نیست، پروکسی سیستم خودکار روی زنجیره تنظیم می‌شود. برای اکثر کاربران همین درست است.
• This app only — مرورگر یا برنامه‌تان را روی آدرسی که در همان کارت نوشته شده تنظیم کنید (معمولاً
127.0.0.1:1820
).
برای اطمینان، کارت What websites see در صفحه‌ی اصلی آدرس واقعی خروجی‌تان را نشان می‌دهد. اگر برچسب Through your node را دید، زنجیره برقرار است.
@whitedns
https://github.com/WhiteDNS/WhiteAesther</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/whitedns/1524" target="_blank">📅 16:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1523">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YTK50A2lilq_lMj6gcwTl1hgsfjeaxxdqknhq5OqN-Kex5JEfxgxPt8-N98IQfs_dSNqOkqwKqRsfB4FwclhxojlZG8Q7DTbqmbZXCBM8GFsOc7SD3UiRs-y6OPjvrtULuZERE13Tpk5kl6seH7igpmmiloW2RC5OfHMquxTj0HKOqXycP36xrn_uokcsvllEb37UXDRxBvv60BeuqjO8zBzUWFDfdbQki0zhx1DRAbWX6ULGsPYjRJywOOfvZ3czyuNKyA32dPXxtqP_3e5GMHMt9kDB9BqtWJV3ubTcM7bBsad6cMlQweeX0Qck8dBcixaL_uF3nltlwM6JcfQ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/whitedns/1523" target="_blank">📅 16:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1522">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/lDxc-k8a4HzgrDkCWX0bmWeleVMosyfU5Fb4jbQAi4hLH6PSlRLRDI4LPW3d3xWsdf0BBOh5qQTCsPBD4DsnZsR5RICsHCQhaZr2skrHH301ICmPUnNYt-R4pgdAHPRdQPx3YVxnMjh3yj31_kdjo1C02Ogn86GiPjyaykGjTtfK4mKQsiXGUq0PPu8CPlgFPnkR3AnT1kLH9YfMV3Cnr1ltLwDzKEee6LackY63jVFOcs2J9sSgC_RC9B-ToL8vyUUqqWESXrNlNoh6MFCeNJ1s5hWKnj_TiBHpspKNTtMoBNY0nn_lb5LABn-ZWCYiG2H3ZLw6Q__Md4aRBxSd5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی آزاد و امن به اینترنت با WhiteVPN (نسخه موبایل و دسکتاپ)
اگر به دنبال یک کلاینت یکپارچه، سبک و حرفه‌ای هستید، WhiteVPN با رابط کاربری مدرن در دسترس شماست!
⚙️
قدرت گرفته از هسته Mihomo:
این برنامه بر پایه هسته قدرتمند Mihomo (مشابه کلش و متا) توسعه یافته است که بالاترین سطح پایداری و سرعت را در دور زدن محدودیت‌ها برای شما فراهم می‌کند.
⚠️
توجه مهم:
این اپلیکیشن کاملاً سورس‌باز (Open-Source) است و در Google Play یا App Store منتشر نشده است. تنها منبع رسمی برای دانلود، مخزن گیت‌هاب پروژه است.
✨
ویژگی‌های کلیدی:
🔹
پشتیبانی همزمان از ویندوز، مک، لینوکس و اندروید
🔹
رابط کاربری ساده و اتصال تنها با یک کلیک
🔹
سیستم پراکسی جامع و تونلینگ کل سیستم (System-wide)
🔹
مدیریت پیشرفته سرورها و پایداری بالا در اتصالات
━━━━━━━━━━━━━━━━━━━━
📥
دانلود مستقیم آخرین نسخه از گیت‌هاب (رسمی):
📱
نسخه اندروید (Mobile):
🔗
https://github.com/WhiteDNS/WhiteVPN/releases/latest
💻
نسخه دسکتاپ (Windows / macOS / Linux):
🔗
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
برای دانلود، وارد لینک‌های بالا شده و از بخش "Assets" فایل متناسب با دستگاه خود (فایل apk برای اندروید و فایل‌های نصب برای ویندوز/مک) را دانلود کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/whitedns/1522" target="_blank">📅 16:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1521">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lF8lKkUEM1TV31Il80BMJKF1uoposVWXHpuGXfj6PZ55tBBRDyPOcwuYB1hGkzq9P6Ro_xj-hM_tN9LzH7Y8-bGqnLRW6Iei9W8U8hVeMOFey92N3xc8aQmVJC0HbLVP9Rt2imwcVLh9rEqWHKb9lBtGSBrYjDHZCIseFnMZhpMScWsi59gjAg5m5nq7LaQvrqTgwuKIfdJm5OA-cQ8GcJhyOPe83G1GU9ejLUrAwLxQ3nIQ35s1WcsOXzid8O19b6a6OAinpUq7Kwiymf1Kh6dBGvnGszDKVscYDbnR5o2GcRt30K8rdQDS5Snd87hDhZlJQ1V_qb_i2Rk8E8_4_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏯️
آموزش کامل اپلیکیشن WhiteAesther
📍
تماشا در یوتیوب
https://youtu.be/cRfqxbDY1Dg</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/whitedns/1521" target="_blank">📅 18:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1518">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نسخه جدید WhiteVPN v1.5.0  توی این نسخه سعی کردیم پیدا کردن یک اتصال خوب و سریع خیلی راحت‌تر بشه. اول همهٔ اتصال‌ها بررسی می‌شن و بعد، اگر دوست داشته باشید، می‌تونید سرعت هرکدوم رو جداگانه تست کنید.   حالا می‌تونید زمان، تعداد و حجم تست‌ها رو هم خودتون تنظیم…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/whitedns/1518" target="_blank">📅 14:41 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1517">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂🍓)</strong></div>
<div class="tg-text">آموزش نصب پنل رایگان StanNg روی Railway
بدون VPS و بدون هزینه کانفیگ V2Ray بگیر
🔥
از صفر تا صد کامل توضیح دادم، مناسب تازه‌کارها هم هست.
لینک ویدیو:
https://youtu.be/sdiGXCDsDvQ
سوالی داشتی بپرس
👇</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/whitedns/1517" target="_blank">📅 11:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1515">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🌎
نسخه جدید WhiteVPN v1.5.0
👆
تغییر های این ورژن کاملا روی فیدبک های شما بوده، و به نظرم از لحاظ تجربه کاربری تغییر خیلی خوبی داشتیم.
😆
ممنون از فیدبک هایی که به ما میدید.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/whitedns/1515" target="_blank">📅 08:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1510">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/whitedns/1510" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">WhiteVPN V1.5.0</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/whitedns/1510" target="_blank">📅 08:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1509">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RS95MLhucjHQse6JekBDhrLMywPRTs26CK2VmNPCexzy8gOgLPmowZHmJSw7M5Frti0sj4M9B1Sm4f2OYQhDZh465OPW8TYfxYAwdSch1QXAjWQTHGCinIiCgtoWRsdbpSwAGzdNKBLoqgX4nkDxa5e_KnnKN1lkOIO2QsIRuUe516NXU96hXB_pHNYvbgGCpkwpIEWAq-_No39YdyksREdbsmLD0HurqpL9eqaMFBVW2qF6FKNBJWpTbw3O_nF8GQWItv2PNpfO26xHIvFm1O6wu1871CUJ8K6hx77kR6EWqXPxpvBg5GKpJCwMnwogQ_e57GtuT_uA1wMP3hD_wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید WhiteVPN v1.5.0
توی این نسخه سعی کردیم پیدا کردن یک اتصال خوب و سریع خیلی راحت‌تر بشه. اول همهٔ اتصال‌ها بررسی می‌شن و بعد، اگر دوست داشته باشید، می‌تونید سرعت هرکدوم رو جداگانه تست کنید.
حالا می‌تونید زمان، تعداد و حجم تست‌ها رو هم خودتون تنظیم کنید تا هم کمتر منتظر بمونید و هم مصرف اینترنت دست خودتون باشه. ظاهر و بخش‌های مختلف برنامه هم مرتب‌تر شدن تا انتخاب اتصال، عوض کردن سابسکریپشن و پیدا کردن تنظیمات راحت‌تر باشه.
⚡️
تست اتصال‌ها سریع‌تر، دقیق‌تر و مطمئن‌تر شده.
⚡️
برای گرفتن نتیجهٔ بهتر، تست تأخیر حالا از سرویس پایدار گوگل استفاده می‌کنه.
⚡️
تعداد اتصال‌های هم‌زمان، زمان انتظار و حجم تست سرعت قابل تنظیمه.
⚡️
تست سرعت دیگه خودکار انجام نمی‌شه و فقط برای اتصال‌هایی که خودتون بخواید اجرا می‌شه.
⚡️
تست تأخیر و سرعت از هم جدا شدن تا خطا و تداخل کمتری پیش بیاد.
⚡️
می‌تونید چند کشور و چند نوع اتصال رو هم‌زمان برای تست انتخاب کنید.
⚡️
انتخاب و مدیریت سابسکریپشن‌ها راحت‌تر شده و از صفحهٔ اصلی هم قابل تغییره.
⚡️
صفحهٔ تنظیمات، تونل تفکیکی، اطلاعات اتصال و چیدمان فارسی مرتب‌تر و ساده‌تر شده.
دانلود آخرین نسخه از گیت‌هاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/whitedns/1509" target="_blank">📅 08:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1508">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نسخه جدید WhiteVPN v1.5.0
توی این نسخه سعی کردیم پیدا کردن یک اتصال خوب و سریع خیلی راحت‌تر بشه. اول همهٔ اتصال‌ها بررسی می‌شن و بعد، اگر دوست داشته باشید، می‌تونید سرعت هرکدوم رو جداگانه تست کنید.
حالا می‌تونید زمان، تعداد و حجم تست‌ها رو هم خودتون تنظیم کنید تا هم کمتر منتظر بمونید و هم مصرف اینترنت دست خودتون باشه. ظاهر و بخش‌های مختلف برنامه هم مرتب‌تر شدن تا انتخاب اتصال، عوض کردن سابسکریپشن و پیدا کردن تنظیمات راحت‌تر باشه.
⚡️
تست اتصال‌ها سریع‌تر، دقیق‌تر و مطمئن‌تر شده.
⚡️
برای گرفتن نتیجهٔ بهتر، تست تأخیر حالا از سرویس پایدار گوگل استفاده می‌کنه.
⚡️
تعداد اتصال‌های هم‌زمان، زمان انتظار و حجم تست سرعت قابل تنظیمه.
⚡️
تست سرعت دیگه خودکار انجام نمی‌شه و فقط برای اتصال‌هایی که خودتون بخواید اجرا می‌شه.
⚡️
تست تأخیر و سرعت از هم جدا شدن تا خطا و تداخل کمتری پیش بیاد.
⚡️
می‌تونید چند کشور و چند نوع اتصال رو هم‌زمان برای تست انتخاب کنید.
⚡️
انتخاب و مدیریت سابسکریپشن‌ها راحت‌تر شده و از صفحهٔ اصلی هم قابل تغییره.
⚡️
صفحهٔ تنظیمات، تونل تفکیکی، اطلاعات اتصال و چیدمان فارسی مرتب‌تر و ساده‌تر شده.
دانلود آخرین نسخه از گیت‌هاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/whitedns/1508" target="_blank">📅 08:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1507">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دوستان عزیز سلام
اپ CoreForge از تیم WhiteDNS ظرفیت جدید اضافه کرده برای کاربران IOS
https://testflight.apple.com/join/3htm1Whc
آموزش استفاده
https://youtu.be/filwdiPKN90?si=O-hvgeNw43t4BUmR
@WhiteDNS</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/whitedns/1507" target="_blank">📅 01:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1506">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">💬
لینک ساب تیم WhiteDNS
https://github.com/iampedii/whitedns-sub</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/whitedns/1506" target="_blank">📅 01:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1504">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سلام دوستان :
❤️
اینقدر درخواست برای IP ثابت برنامه های  whiteAesther و whitevpn اومده که دیدیم بهتر هست ، یک پست براتون بگذارم
در حال حاضر  این امکان توی آخرین ورژن های این دو برنامه وجود ندارد
با اعضای تیم داریم روش کار میکنیم و امیدواریم طی روزهای آینده به دستتون برسونیم ، یکم به ما وقت بدید و صبور باشید.
ببخشید که انجام درخواست های شما گاهی طول می‌کشه، چون ما هم مثل تک تک شما درگیر کار و زندگی و مسائل خودمون هستیم و گاهی وقت کم میاریم
ولی مطمئن باشید ما همه پیام های شما را می‌خونیم و تا جایی که بتونیم ترتیب اثر می‌دیم ،
ارادتمند و کوچیک تک تک شما عزیزان دل
ویسپر</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/whitedns/1504" target="_blank">📅 16:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1502">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⚠️
موقت
به نظر میاد که دامنه
workers.dev
کلادفلر رفع فیلتر شده است</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/whitedns/1502" target="_blank">📅 19:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1501">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/bbCHPwlsRbjWp6plroULcEkK8hwiaCYr6VTSaRPOO6vy42KfTj1hgUdI4_PlGXTOQLtdha2BOvTt45DqzKCyjoa4JHeyGlzvkyiLUKan3BjrIgT3LdZqroIjS1CwUhbv-sR5tG3hUMwxNsYTVv7iZk_g6OdJ0JLq1fCnDVzC-FyywvBiuyDYuVEi1a-Xj28wSh12xswCQSthcVNzNx3sf1pr3F_Dor6Bp7VBkc3ouSCmBf5pJCoHF2Ghqjtrhl3nl866avJiR1soHmoksaJcjCyLiKXTqUNqna_ki7tp_0saLM7hGsZ1ALwjpEMaGRljtfYSorhgJjiZM4YsbByH5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
چرا موقع ورود به Gemini با ارور ۴۰۳ مواجه می‌شویم و چطور حلش کنیم؟
خیلی از کاربران هنگام باز کردن
gemini.google.com
با خطای معروف زیر روبه‌رو می‌شوند:
403. That’s an error. Your client does not have permission to get URL / from this server.
🔍
دلیل این ارور چیست؟
سرویس‌های هوش مصنوعی مثل Gemini دسترسی کاربران برخی مناطق را به دلیل محدودیت‌های منطقه‌ای و حقوقی مسدود (Geo-block) می‌کنند. اما اگر از ابزارهای تغییر آی‌پی استفاده می‌کنید و باز هم این ارور را می‌بینید، علت معمولاً یکی از موارد زیر است:
1️⃣
نشت موقعیت (DNS یا WebRTC Leak):
با اینکه کانکشن شما وصل است، مرورگر از طریق درخواست‌های DNS یا قابلیت WebRTC، آی‌پی واقعی شما را لو می‌دهد.
2️⃣
شناسایی آی‌پی دیتاسنتر (Datacenter IP):
گوگل بازه‌های زیادی از سرورهای عمومی و تجاری را شناسایی کرده و مستقیماً مسدود می‌کند.
3️⃣
کش و کوکی‌های ذخیره‌شده:
مرورگر موقعیت قبلی شما را در کوکی‌ها نگه داشته است.
🛠
راهکارهای سریع برای رفع مشکل:
🔹
تست نشت آی‌پی (Leak Test):
ابتدا وارد سایتی مثل
ipleak.net
یا
browserleaks.com/ip
شوید و مطمئن شوید در بخش‌های WebRTC و DNS هیچ نشانی از آی‌پی واقعی یا DNS داخلی وجود ندارد.
🔹
استفاده از حالت ناشناس (Incognito):
یک پنجره Incognito / Private باز کنید یا کش و کوکی‌های مربوط به دامنه‌های
google.com
را پاک کنید.
🔹
فعال‌سازی حالت TUN Mode / روتینگ کامل:
مطمئن شوید کلاینت شما تمام ترافیک و به خصوص درخواست‌های DNS را هدایت می‌کند و ترافیک دامنه‌های گوگل به صورت Direct رد نمی‌شود.
🔹
تغییر نود یا کشور سرور:
اگر آی‌پی سرور فعلی توسط گوگل فلگ شده باشد، با جابه‌جایی نود یا تغییر لوکیشن معمولاً دسترسی بلافاصله باز می‌شود.
💡
اشتراک‌گذاری برای دوستانی که با دسترسی به جمینای مشکل دارند.
@whitedns</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/whitedns/1501" target="_blank">📅 15:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1496">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/rjhZwRMd-aa5r6S9Q48e-dmtYecuy-GeWlNvbYH0KwAencexhqm9ghwXA2plA7rxw2-I5UuPgpZpY7dVajOAxp-jjLymfP2v9xYg1Ud4Br2-U1b-nZnE1y_dvbEtPUyNqN3KhN8JRzwTVduvr2Sb8K3KjjeVtxfka4qebpwNK4Yi5Kg2mvGHUhCipnpWy34I2gTXjralYGnSn3yAnMB0PDMmt48F0FV6EoswgkX5qXTBCfAuZ-cZJ_1qWRJcg6hYFP7l7EHNR2ieeWtoOPNmc0txist7DJ9ev9ApIy3hz1yFjzYZV0g_JLuhzK5oozv3QYNseBBieFxM9062sIRSEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/whitedns/1496" target="_blank">📅 07:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1495">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/o8EZwrlHUDXonfktMIvvzt1gV1PJBZ2O_aiFbIWDYCmUeRcsbHB_XfMFO7EnJrcvDlWJppQ8XY3N2hFo9H71k15mHN9B1-cizIGaN9ZFUSX48ZAAgFdbW6aLpmUx3dNAcwE49j4MUN5yLTwLIIx4cPGcDzuxqy8erGBn5H_hOv-4UI-ab5s55UyeP2W_UToN_VO6yXRTmyyPDKHULdo8VSIanTd37NG4XF-RpBL8tQwdan02UPtKKFvJGN8-B8nu4Gy47fqvCv-_fjs5wPaF9zWisC2bilM_L3p1k23gMq6c3WqIjjYkCLTJBw0SFzST2Kt0gs8EW6nZtevKOXenFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی آزاد و امن به اینترنت با WhiteVPN (نسخه موبایل و دسکتاپ)
اگر به دنبال یک کلاینت یکپارچه، سبک و حرفه‌ای هستید، WhiteVPN با رابط کاربری مدرن در دسترس شماست!
⚙️
قدرت گرفته از هسته Mihomo:
این برنامه بر پایه هسته قدرتمند Mihomo (مشابه کلش و متا) توسعه یافته است که بالاترین سطح پایداری و سرعت را در دور زدن محدودیت‌ها برای شما فراهم می‌کند.
⚠️
توجه مهم:
این اپلیکیشن کاملاً سورس‌باز (Open-Source) است و در Google Play یا App Store منتشر نشده است. تنها منبع رسمی برای دانلود، مخزن گیت‌هاب پروژه است.
✨
ویژگی‌های کلیدی:
🔹
پشتیبانی همزمان از ویندوز، مک، لینوکس و اندروید
🔹
رابط کاربری ساده و اتصال تنها با یک کلیک
🔹
سیستم پراکسی جامع و تونلینگ کل سیستم (System-wide)
🔹
مدیریت پیشرفته سرورها و پایداری بالا در اتصالات
━━━━━━━━━━━━━━━━━━━━
📥
دانلود مستقیم آخرین نسخه از گیت‌هاب (رسمی):
📱
نسخه اندروید (Mobile):
🔗
https://github.com/WhiteDNS/WhiteVPN/releases/latest
💻
نسخه دسکتاپ (Windows / macOS / Linux):
🔗
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
برای دانلود، وارد لینک‌های بالا شده و از بخش "Assets" فایل متناسب با دستگاه خود (فایل apk برای اندروید و فایل‌های نصب برای ویندوز/مک) را دانلود کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/whitedns/1495" target="_blank">📅 07:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1493">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tgnAUZiPjXqYEMHO1epq2c8BRmc2hoacUVys7M8w50c5k2wTBTFkbzBL5LFMyLYIKWJhLINOEcCNvbnqJWW4PtoZqYSCyjzyMCs4Bb7wh4wxOfC5mO1kz81cKhFxz8F8qOD7ZUNkEBfprJ6GAy_fcYKJBxOrRUotZAo45r_0BX3ckez3qc9Le-mZ0PXNMwrMVTv8Zc72LTmUGQe-B8oiqki82VJk1XdPXxojPd3s7u0JXK-jkkKC9dlbYGlPOShvrzW2x8wSHhpI_F6LPxNaaaDhfrxNRyPm-jw5xNymSaqVQ4eaIngdeL3rSuqt34hbEXoVkohFsqDXbvdn8mwKJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام :
برای حل این مشکل توی ورژن دسکتاپ و مبایل whitevpn لطفا ساب زیر را دستی وارد کنید
اگر به هر دلیلی ساب برای شما اپدیت نمیشه اول یک فیلترشکن روشن کنید که ساب را بتونید بگیرید و اپدیت کنید بعد استفاده کنید
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
@whitedns</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/whitedns/1493" target="_blank">📅 05:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1491">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
تمام
#نکات
واسه مشکل فیلتر شدن worker رو داخل این پست میگم:
👽
💻
طبق آموزش هایی که قبلا دادم با اپلیکیشن pattng و همچنین v2rayn در ویندوز میتونید مشکل فیلترشدن ورکر رو حل کنید و کانفیگ های -1 رو مجدد متصل کنید.
آموزش مروبطه:
👇
https://t.me/xsfilterrnet/3642
📱
داخل ios هم طبق تنظیمات یه ip تمیز پیدا کنید داخل کلاینت incy یا hiddify بزنید و فرگمنت رو روشن کنید متصل میشه.
یه روش دیگه بعد از بالا اومدن پنل استفاده از کانفیگ های فرگمنت برای bpb هست که با مقادیر low (1-1) رو متصل کنید
🔥
🔗
در مورد لینک ساب های raw هم به گفته خود bpb:
بچه‌ها اگر ساب Raw و کانفیگ TLS استفاده میکنید از این روش در v2rayNG/pattngاستفاده کنید، معلوم نیست تا کی کار کنه، اگر پایدار بود پنلو تغییر میدم.
این رو دو جا وارد کنید:
https://8.8.8.8/dns-query
۱. قسمت Remote DNS تنظیمات برنامه.
۲. ویرایش کانفیگ قسمت echConfigList.
با Mux خاموش
یه نکته دیگه از بچها اینترنت آزاد که جواب داده:
با ECH و استفاده از آدرس udp://1.1.1.1 میتونید فیلترینگ
pages.dev
و
workers.dev
رو دور بزنید.
💓
نکته ای هم که متین سنپای گفته:(همراه با ابزار جدید)
https://t.me/MatinSenPaii/4960
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/whitedns/1491" target="_blank">📅 22:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1489">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vM_MxcH8Pznd2pmS3egY7IpF5AxsRipdxjTX6V-Ndep_WFmO-XLPUbu7mjosdFLlUwoIf0E0Ds7AJtWxGNM5QvHu9F57jreE7P3IRJTwWdn2msLHAVGUD8YBS--kInn2ULPvZvN4OP_VvD00GWHneOVtvBogEa6nc4sY6LTUZWuWOdfAqf_uqQUBBr5qInStbdZhMDHZR1XOb91DDAsn-Db1KC6N7ELBBKz4liTMDQV0TvQxz0Kknwd_v3pRdACGfwwk5dGSeP_Bw1TV40olQBbpmrepzlhXyflXwfUj79GHmbzUFEK1bbOQiAPLdtxkv-ALiU6B6JoLQwQ_leLX_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
چطوری فیلتر شدن BPB و Workers رو دور بزنید؟   میتونید با رفتن به منو تنطیمات، فعال کردن گزینه Amnezia Noise فیلترینگ ورکر رو دور بزنید و به کانفیگ های ساب BPB Warp Pro و باقی Wireguard ها وصل بشید.  این مشابه گزینه فرگمنت هست برای Warp pro و Wireguard داخل…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/whitedns/1489" target="_blank">📅 21:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1488">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtO1-9puYHD1wjrbsJez0gcv860jiKvj8O-5bO33cTjSAY_JPkZi-53xu1wX5UWpkIOQHH3cgyimKyAMbXc1AmC7r9NFkw_T0ah4mLwC5W4-xsu1lWO9vNhkqHUJRLtdPyNf_op5cRY_8xLZ5QG2aZBtZ0I3LrR2VLuwDW17VwX_wKM9dIyxVxK3PswFQDif4I7Yrl_Pd1CRyW8YCpAKBg-TnUH4QIj3lZhICfCsDTX2YSJZSWQDsYJuYDoU8hFTeplES3N0EucjJRCiCENGtcjnMNXC3kfKfbvK-5QEl11EySX9Kwp-9s5QYOPBhenPS6uaeE_8AcU6wT8axzFF3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
چطوری فیلتر شدن BPB و Workers رو دور بزنید؟
میتونید با رفتن به منو تنطیمات، فعال کردن گزینه Amnezia Noise فیلترینگ ورکر رو دور بزنید و به کانفیگ های ساب BPB Warp Pro و باقی Wireguard ها وصل بشید.
این مشابه گزینه فرگمنت هست برای Warp pro و Wireguard داخل اپ WhiteVPN
لینک ساب Mihomo رو داخل WhiteVPN وارد کنید.</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/whitedns/1488" target="_blank">📅 20:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1487">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=F0Bw1QHC82cU3F-KnOCPAnhCrzpgdlHYEO_hA-k-W5eQjkkWEK0J-bh5Gj9hvxaJbxLvZZJh53uJTiDJ3I_857w_Se5W-dMlqqSpVBNWjGFotgE44Jgmz3wX-AefGIgqyRk27vrJd1hyr2bEim7lFSlGMLhpfE7RRMNtZAXuqCDlKMYB1fonFVCaFAHFx25r6MxC16_qFVgXcrGkKesNtBw5Gw6hiiUnNn0vh6ScP1zJSNbH8H9-cLg46lcYsoMEwIbVEngvB_xcSfmpYlpdvGNLNrWVfPIUr9ZS_dvmbWKZnc09NsTb-WYhjpdtU3DK_zwSaRFawJa0tGDZADE3hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=F0Bw1QHC82cU3F-KnOCPAnhCrzpgdlHYEO_hA-k-W5eQjkkWEK0J-bh5Gj9hvxaJbxLvZZJh53uJTiDJ3I_857w_Se5W-dMlqqSpVBNWjGFotgE44Jgmz3wX-AefGIgqyRk27vrJd1hyr2bEim7lFSlGMLhpfE7RRMNtZAXuqCDlKMYB1fonFVCaFAHFx25r6MxC16_qFVgXcrGkKesNtBw5Gw6hiiUnNn0vh6ScP1zJSNbH8H9-cLg46lcYsoMEwIbVEngvB_xcSfmpYlpdvGNLNrWVfPIUr9ZS_dvmbWKZnc09NsTb-WYhjpdtU3DK_zwSaRFawJa0tGDZADE3hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
دوستانی که فقط با فشار دادن دکمه کانکت براتون وصل نمیشه یا سرعت کمی دارید، از این روش میتونید تست سرعت بگیرید و بهترین کانفیگ بسته به اینترنت خودتون وصل بشید.
توجه کنید، هر تست سرعت ۱مگابایت از حجم شما استفاده خواهد کرد.</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/whitedns/1487" target="_blank">📅 19:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1486">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🌎
انتشار نسخه WhiteVPN 1.4.0</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/whitedns/1486" target="_blank">📅 19:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1481">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.4.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/whitedns/1481" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/whitedns/1481" target="_blank">📅 19:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1480">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7FcY3as_xshEdR9fhYsh6i62QJOiYwSdc1Z8j_xTkNGfEsk4CcP_slX2rrq_dLjJEMwqhpy5iUPtwuNX6JF9mN5PGkiX210F5xOz60zKFCuN18ED0EQGmE68nBBtdLf6aPYiilhHq-AoUvFlz7loW7x0oEBDTYcc3047G-HHYrCknhHN860pIsSi4qaNtpbubgwNMemxtp5i9rvb1mCjJdjfcM1vNJKF5EeYIpefkKZtfQtRv__Sn35vJLCUdptZ55YF_bjrkcMi2ozzFWsT9JJ_-YfkDeUPn_kLJZfr7DiYGcSkevOwilPtuAsCVadVACl0Sv-gJeovPrREClqQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
انتشار نسخه WhiteVPN 1.4.0
• ظاهر جدید و مدرن اپ
• بهبود اتصال بعد از قطع شدن
• حل مشکل VPN Mode & Proxy Mode
• بهبود تست اتصال. حالا میتونید کشور رو فیلتر کنید و بعد تست کنید. تست هم به دو مرحه real delay و تست سرعت  تقسیم شده.
🌎
دانلود آخرین نسخه از گیتهاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/whitedns/1480" target="_blank">📅 19:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1478">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Kpz7WTGauU6mKVJkY8FYzf6APQiE9iI_kHK-1I2lS0DcCjOXEl-8hc193UMhPwMU4LGsRHdlS0KI8CihpPSGiw2dQFVXbPmDTVbQtIA1CFbi5Z9bvQvXFDpVOf8b6JYsKJ4Ng3LFw7Rc2n23hUIAPauyBMmughHlNdyQD-MlkMkVnnmyndezL7ze1ufjw5kVEUfR-xC0QUED8laEQ4jPvOseoskoGq2iEfRFrAr0Vec_5-Kcwb-ho4b_wmNzXGZAQvZBP1slbasHBin3STufHD6vag_MSL2g3zk7JQYpnjz697o35kvKul6mq2r26B8ub9MSFpbqNp_59H3Ky34iFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
وایت‌استر  —
نسخه‌ی دسکتاپ بتا
WhiteAesther Desktop V1.3.1
یه کلاینت رایگان و متن‌باز برای عبور از فیلترینگ، ساخته‌شده روی هسته‌ی Aether (همون هسته‌ای که تو اپ اندرویدش هم استفاده می‌شه). برای ویندوز، مک و لینوکس؛ کاملاً رایگان و بدون نیاز به کانفیگ دستی.
✨
امکانات:
🔎
جست‌وجوی خودکار مسیر — به‌جای اینکه شما دنبال کانفیگ سالم بگردید، خود برنامه بهترین دروازه رو پیدا می‌کنه (با MASQUE H2/H3، WireGuard و WARP-in-WARP)
📊
نمودار سرعت و تأخیر زنده — تست سرعت واقعی داخل خود برنامه + نمودار پینگ لحظه‌ای
🖥
دو حالت اتصال — «فقط این برنامه» (پراکسی محلی) یا «کل سیستم» (همه‌ی اپ‌ها از تونل رد بشن)
🛡
کلید قطع اضطراری — اگه تونل قطع بشه، ترافیک رمزنشده لو نمی‌ره
🔍
جست‌وجوی تنظیمات با Ctrl+K — هر تنظیمی رو در چند ثانیه پیدا کنید
🧩
چندپلتفرمه — ویندوز، مک (اینتل و اپل‌سیلیکون) و لینوکس، هم x86_64 هم arm64
📖
متن‌باز، برای همیشه — کد کامل زیر مجوز AGPL-3.0 روی گیت‌هاب
⚙️
نحوه‌ی استفاده:
1️⃣
از لینک زیر، نسخه‌ی مخصوص سیستم‌عاملتون رو دانلود کنید
2️⃣
نصب کنید و برنامه رو باز کنید
3️⃣
دکمه‌ی Connect رو بزنید و چند لحظه صبر کنید تا مسیر سالم پیدا بشه
4️⃣
اگه خواستید کل سیستم از تونل رد بشه، پایین صفحه گزینه‌ی «Whole machine» رو بزنید
5️⃣
برای تنظیمات پیشرفته (پروتکل، DNS، حالت جست‌وجو…) روی Advanced بزنید یا Ctrl+K رو بزنید و اسم تنظیم موردنظرتون رو تایپ کنید
📥
دانلود:
github.com/WhiteDNS/WhiteAesther/releases/latest
💬
نکته: چون برنامه امضای اپل/مایکروسافت نداره، ممکنه هنگام باز کردن هشدار «ناشر ناشناس» ببینید؛ کافیه روی فایل راست‌کلیک کنید و Open رو بزنید (تو مک هم از System Settings اجازه‌ی اجرا بدید).
#وایتاستر
#ضدفیلتر
#متنباز
نکته مهم :
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
گزینه whole machine همان system proxy هست - این گزینه فقط اپلیکیشن هایی مثل گوگل کروم که امکان ان را دارند پراکسی میکند - برای همین ممکن هست بعضی از اپ های شما پراکسی نشود
تلاش خواهیم کرد در روزهای اینده امکان TUN را اضافه کنیم
@whitedns</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/whitedns/1478" target="_blank">📅 18:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1477">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دوستان عزیز سلام
مثل اینکه آدرس های ورکر کلادفلر فیلتر شدن. و آدرس ساب اپلیکیشن ما داخل ورکر ها هستش. تا آپدیت بعدی، میتونید ساب مارو از لینک زیر وارد اپ WhiteVPN بکنید
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/whitedns/1477" target="_blank">📅 16:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1476">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/f57h_KrHp7_TQeAuWxjKVLHU7e0hgThhKZi4H5U8WWN2D8hxpi5gLBUcS7HJ0xo1yKL3HmekjvMd6qh23sZP7hIPqntAB8-TaTCSYj9ZKIP59dgMBG6gBNMVrentUprVXt04-DhwkPS30_2VUjqcqpwKYjA0-jZt1SoDIhGEw_8fxzp8_GbD7mmEHofnRAiAK5vwZpNICGt8ATZo2JO_Mv4Q-7KmKhf36wNzELDQbwJknKutlC2KiB8mWGUHRHHx4TmVpHG3ek9e1FAf1tBdC1d9DtcsJVyx2CDrMtk2qCKV40RGnjHIfFzAbX7GDRE6ZNRcq9Zo_waSvU3KqIECMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther V1.0.2
دوستان سلام :
ما روی هسته Aether که حاصل زحمت دوست عزیزمون
CluvexStudio
هست یک کلاینت**
آزمایشی ورژن بتا
** درست کردیم . که اگر دوست دارید تست کنید و لطف کنید فیدبک بدید.
پیشاپیش ممنونیم
❤️
❤️
❤️
اموزش :
📖
**راهنمای WhiteAesther**
**۱ — نصب**
فایل **arm64-v8a** رو بگیر (تقریباً همه گوشی‌های ۲۰۱۷ به بعد).
مطمئن نیستی؟ **universal** همه‌جا کار می‌کنه، فقط حجمش بیشتره.
**۲ — سه تا نکته اول**
▪️
**Traffic** → گزینه Coverage روی **Whole device** باشه
⚠️
حالت Proxy only خودش هیچی رو رد نمی‌کنه! به‌نظر می‌رسه وصل شده ولی عملاً هیچ ترافیکی از تونل نمی‌ره.
▪️
**Routes** → پروفایل روی **Adaptive**
▪️
**Settings** → اجازه اجرا در پس‌زمینه رو بده، وگرنه با خاموش شدن صفحه قطع می‌شه
**۳ — اگه وصل نشد، به این ترتیب امتحان کن**
**قدم ۱ — پروتکل**
Routes → Advanced → Preferred transport → **MASQUE over HTTP/2**
📌
روی **همراه اول** مدتیه QUIC (یعنی UDP) کاملاً بسته شده. یعنی H3 اصلاً وصل نمی‌شه و فقط H2 جواب می‌ده.
از نسخه ۱.۰.۲ اپ خودش این کار رو می‌کنه.
**قدم ۲ — تیکه‌تیکه کردن TLS**
⭐️
Traffic → Advanced → **Split the TLS handshake** → روشن
فیلترینگ معمولاً فقط تیکه اول بسته رو می‌خونه تا ببینه کجا وصل می‌شی. وقتی تیکه‌تیکه بفرستی، نمی‌تونه بخونه.
اگه با H2 وصل می‌شی ولی کنده، **حتماً اینو امتحان کن**.
**قدم ۳ — پروفایل**
Routes → Profile → **Strict network**
(برای شبکه‌هایی که خیلی چیزها رو می‌بندن)
**قدم ۴ — خاموش کردن IPv6**
Traffic → Addresses → **IPv4 only**
روی خیلی از شبکه‌های موبایل ایران IPv6 نیمه‌کاره‌ست.
**قدم ۵ — مبهم‌سازی**
Traffic → Advanced → Obfuscation → **Aggressive**
💡
اگه قدم ۲ مشکلت رو حل کرد، **Off** رو هم تست کن — شاید پدینگ اضافه فقط داشته سرعتت رو می‌گرفته.
**قدم ۶ — اند‌پوینت دستی**
Routes → Endpoint → Specific address → دکمه **Find endpoints**
⚠️
گزینه Fall back automatically رو روشن نگه دار.
**۴ — گزارش مشکل**
Settings → Diagnostics & logs
۱. Detail level روی **Verbose**
۲. دوباره سعی کن وصل بشی
۳. برگرد و **Send** رو بزن
قبل از ارسال دقیقاً متنی که فرستاده می‌شه رو می‌بینی، و IP‌ها پیش‌فرض مخفی می‌شن. هیچی بدون اجازه‌ات از گوشیت بیرون نمی‌ره.
**نکته:** اون خط خاکستری کوچیک زیر متن بزرگ توی صفحه اصلی، پیغام خود موتوره. برای فهمیدن مشکل همیشه اول اونو بخون.
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.0.3
@whitedns</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/whitedns/1476" target="_blank">📅 13:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1474">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/vWdZYPgiFOw3O8c0mEMU5MYeDxI-5TDXc8b52ghriiVx2uVk-YqIpTMr1CUx80jVkFPnpBXC9-fInROn_Cd2VZOYucUW1KEwB0ojI2AG7udIZMgiuwWvmkDQovxkbK1GMTJAQnGJzYJhet2xOLra4_YG9_yC3cr8H-L5geE-eLovQaXd3TRQSEFRyfqic4Xck3XAkGwxSzlPW35lTrrd9Olm7rNn3ZCkiRA8ZtFxmne8-fK8XNuonFrqi_Ags8fRf1Hqn6pxJVaS1KTCPEHyPONoEK3Agbo5SPvIFWGi4UkAhcBhsbTmVc_ABEbLfwxf4Z1X2HLbEWPOn9fWNR0p3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتشار WhiteDNS Clean IP Finder 1.3.7
نسخه جدید WhiteDNS Clean IP Finder با تمرکز روی افزایش سرعت پیدا کردن DNS Resolverهای سالم در Desktop و Android منتشر شد.
⚡️
مهم‌ترین تغییرات:
• اجرای همزمان تست‌های DNS Transport و TXT Passthrough برای کاهش Timeout
• اجرای Parallel بررسی‌های NXDOMAIN Hijack
• اضافه شدن Fast Scan با حفظ بررسی‌های اصلی A Record، Recursion، EDNS و TXT Tunnel
• حفظ Full Scan به‌عنوان حالت پیش‌فرض برای بررسی کامل
• بهبود دریافت و Cache اطلاعات Reference DNS
• اضافه شدن UDP/53 Only و TCP/53 Only در Android
• گزارش دقیق‌تر DNS Poisoning، Injection و Hijack
• بروزرسانی دیتابیس Iran & Global ASN شامل IPv4 و IPv6
💻
پشتیبانی از Windows، Linux، macOS و Termux
📱
نسخه Android شامل APKهای مختلف، Universal APK
✅
برای آپدیت نیازی به تغییر تنظیمات قبلی نیست.
📥
دانلود WhiteDNS Clean IP Finder 1.3.7:
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3.7
⚡️
WhiteDNS Clean IP Finder — اسکن سریع‌تر، تشخیص دقیق‌تر و دیتابیس به‌روزتر
@whitedns</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/whitedns/1474" target="_blank">📅 02:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1473">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JD7WgBDvadRt_kO_hqjdjaAPDLnsG-EwIR5AQjY9Cc9B6omHV2cEFV_5i0Cse-Qim6dsa2aIk4wNOks8_0Y_5nmxMx9q_IxjvDLs0Qbqb8AJ1mnpaatmg07QE_tcZAy-GfSjRqmQBAz0bsqeslFWnDD-Q0UaJy2B56aaYW-OTiUTyj4pRDks3LKKhLV2yDMfPFPNZhyDhbQealvJI0NilcotJOCGwQ8mEfVm343c8OxXC1XFq6lFGpNSBEFsj7PpOh57t4zmjNja4UQGTHSvpwAMZvaiJr6jo_dZ_eKkS4q0_t5Udrp3RXcx6ONpgFVVtT-KY3pAo4PmZLDgTamiCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏯️
آموزش ساخت کانفیگ V2Ray با سرور رایگان!   توی این آموزش با استفاده از Wasmer یه سرور رایگان می‌سازیم و در نهایت بدون نیاز به خرید سرور، ۳ تا کانفیگ V2Ray برای مصرف شخصی دریافت می‌کنیم.
⚡️
⏯️
تماشا در یوتیوب  https://youtu.be/EAjOhvuMw8Q</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/whitedns/1473" target="_blank">📅 21:53 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1472">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⏯️
آموزش ساخت کانفیگ V2Ray با سرور رایگان!
توی این آموزش با استفاده از Wasmer یه سرور رایگان می‌سازیم و در نهایت بدون نیاز به خرید سرور، ۳ تا کانفیگ V2Ray برای مصرف شخصی دریافت می‌کنیم.
⚡️
⏯️
تماشا در یوتیوب
https://youtu.be/EAjOhvuMw8Q</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/whitedns/1472" target="_blank">📅 21:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1471">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/KOxHjJ5dCzzh0d0tmory6apdWYujLXzwXOaCg_nqtUi3TfXZ93ITxvWdsGEs7KN6ttkHR_RnoqfP0qp2PpqkZVYQrKFXKgPanr6xhxdwJaa8Ux_4M7joTgU8sXM4km_hBJRSiQdNgRX56eD4SAOU3oPUMQ-pJ0wzCwRH68PTRhUqAhm4rwLewapg_-bEjysa8nSv1FEOFYJIf26QSPCMynLzUc_AD7joXNlU5jKyEF1cr6uwtwfefCkTXhgj4DJbT5ZKQiH8a3f-XD9fyMRbJTuH1CtFU9M-3E6YrtxPzDZLTFF6c0b7SywD1rYAn8ZU5yW2XAzQY93RjMXavWLyrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرایط عادی :
•
دانلود آخرین ورژن WhiteVPN اندروید
•   دانلود آخرین ورژن WhiteVPN دستکتاپ
شرایط قطعی اینترنت :
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین ورژن WhiteDNS دسکتاپ
•
دانلود آخرین نسخه CoreForge برای آیفون
@whitedns</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/whitedns/1471" target="_blank">📅 18:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1470">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromUAC Sni Spoofer(Behrooz)</strong></div>
<div class="tg-text">🛡
نسخه‌ی 2.0.1 اپلیکیشن UAC SNI Spoofer برای اندروید منتشر شد
در نسخه‌ی 2.0.1 تمرکز اصلی روی این بوده که برنامه در شبکه‌ها، اپراتورها و مناطق مختلف، مسیرهای سالم‌تر و سریع‌تر رو پیدا کنه و در صورت افت کیفیت یا از دست رفتن مسیر فعلی، بتونه مسیر مناسب‌تری رو جایگزین کنه.
⚡️
یکی از مهم‌ترین قابلیت‌های این نسخه، تلاش برای زنده‌کردن کانفیگ‌هایی هست که در حالت عادی دیگه قابل استفاده نیستن.
🔹
اگر کانفیگی دارید که IP سرورش روی اپراتور یا شبکه شما بلاک شده
🔹
مطمئن هستید کانفیگ سالمه ولی در برنامه‌هایی مثل v2rayNG متصل نمی‌شه
🔹
کانفیگ فقط روی یک اپراتور خاص کار می‌کنه و روی اپراتورهای دیگه از دسترس خارج شده
🔹
کانفیگ قبلاً کار می‌کرده ولی به‌دلیل تغییر محدودیت‌های شبکه دیگه متصل نمی‌شه
UAC SNI Spoofer می‌تونه با بررسی ترکیب‌های مختلف مسیر، DNS، Edge، Fragment، MTU و سایر پارامترهای اتصال، برای پیدا کردن یک مسیر قابل استفاده تلاش کنه.
در تست‌های انجام‌شده، برنامه تونسته بخش بسیار زیادی از کانفیگ‌های سالم ولی محدودشده رو دوباره قابل استفاده کنه و در بعضی شرایط میزان موفقیت تا حدود 98٪ هم رسیده.
البته نتیجه نهایی به نوع فیلترینگ، اپراتور، منطقه، وضعیت سرور و کیفیت اینترنت شما بستگی داره.
تغییرات نسخه 2.0.1:
🔹
برنامه برای هر شبکه یک اثرانگشت جداگانه ایجاد می‌کنه و تنظیمات موفق همون شبکه رو ذخیره می‌کنه تا دفعات بعد سریع‌تر به مسیر مناسب برسه.
🔹
بخش Route Speed Test حالا می‌تونه ترکیب‌های مختلف Edge، DNS، Fragment و MTU رو بررسی کنه و بهترین مسیر فقط براساس Ping انتخاب نمی‌شه.
🔹
مسیرها در چند مرحله از نظر اتصال، سرعت، پایداری، نوسان و میزان موفقیت بررسی می‌شن و بهترین نتایج بالای لیست قرار می‌گیرن.
🔹
امکان توقف Route Speed Test و ادامه‌دادن اون در زمان دیگه اضافه شده.
🔹
می‌تونید هر زمان که خواستید مسیرهای سالم پیدا شده رو به مرحله بعد بفرستید و لازم نیست منتظر پایان کامل تست بمونید.
🔹
برای هر کانفیگ و هر شبکه، یک مسیر اصلی و یک مسیر پشتیبان ذخیره می‌شه تا اتصال سریع‌تر انجام بشه.
🔹
اگر شبکه تغییر کنه یا کیفیت مسیر فعلی افت کنه، برنامه می‌تونه سراغ مسیر پشتیبان بره و برای بازیابی اتصال تلاش کنه.
🔹
سرویس‌های مختلف DNS مثل Cloudflare، Google، Quad9، AdGuard و OpenDNS در دسترس هستند و همراه مسیرهای مختلف قابل تست هستن.
🔹
بخش Config Maker دارای دو حالت Quick Scan و Deep Adaptive Test شده؛ یکی برای بررسی سریع و دیگری برای تست دقیق‌تر و گسترده‌تر مسیرها.
🔹
امکان وارد کردن کانفیگ از متن، Clipboard، فایل و Subscription Link وجود داره.
🔹
لینک‌های جدید بدون حذف نتایج قبلی به لیست اضافه می‌شن و کانفیگ‌های تکراری به‌صورت خودکار حذف می‌شن.
🔹
کانفیگ‌های VLESS، VMess و Trojan پشتیبانی می‌شن و مشخصات اصلی کانفیگ تا جای ممکن بدون تغییر باقی می‌مونه.
🔹
برای برنامه‌های گوشی سه حالت Routing در دسترسه: عبور همه برنامه‌ها از VPN، خارج‌کردن برنامه‌های انتخابی از VPN یا استفاده از VPN فقط برای برنامه‌های انتخابی.
🔹
حالت Tunnel و پروکسی محلی SOCKS در دسترس هست و تنظیماتی مثل Fragment، FinalMask، MTU، Mux، Keepalive و کنترل QUIC هم قابل تغییر هستن.
🔹
Ping، میزان دانلود و آپلود، کشور، IP خروجی و اطلاعات فنی اتصال به‌صورت زنده نمایش داده می‌شن.
🔹
بعد از اضافه‌کردن برنامه به Quick Settings اندروید، می‌تونید بدون بازکردن برنامه VPN رو مستقیماً روشن یا خاموش کنید.
⚠️
نکته مهم:
محدودیت‌های فیلترینگ در هر منطقه، اپراتور و حتی در زمان‌های مختلف می‌تونه متفاوت باشه. به همین دلیل ممکنه کانفیگ داخلی برنامه برای بعضی کاربران متصل نشه یا روی بعضی شبکه‌ها کیفیت متفاوتی داشته باشه.
در حال بررسی مسیرها و محدودیت‌های شبکه‌های مختلف هستم تا روش‌های بیشتری شناسایی بشن و برنامه بتونه در مناطق و اپراتورهای بیشتری محدودیت‌ها رو دور بزنه.
همچنین حتماً مطمئن بشید اینترنت اصلی شما سرعت دانلود و آپلود قابل قبولی داره. VPN نمی‌تونه ضعف شدید یا ناپایداری اینترنت پایه رو جبران کنه و کیفیت اتصال نهایی به کیفیت شبکه شما هم وابسته است.
━━━━━━━━━━━━━━━━━━
📥
دریافت نسخه 2.0.1:
https://github.com/Floxu1/UAC-SNI-Spoofer-Android/releases/tag/2.0.1
💻
گیت‌هاب پروژه:
https://github.com/Floxu1/UAC-SNI-Spoofer-Android/tree/main
جهت حمایت از من اگر دوست داشتین وارد لینک رفرال من در NotHolidaySeasonBot بشین
❤️
:
https://t.me/NotHolidaySeasonBot/app?startapp=tr_aFLKAgxVq8ezM310c0sS
📢
کانال:
t.me/UacSniSpoofer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/whitedns/1470" target="_blank">📅 15:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1468">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/DAvpGe4N1-zjm5kJXCjPYmKsk8F6r0EeCY0n_X09c2xZyW6apczgJ4wMo3LhoRI-I1qZniF7Yhd0wJudYdLfG_4rK_0g70kAciuso1AFpK8oAclft3_eswnD9omgjfgwXpESn99bZ5q5wid0Ou3WDtimT5Z87rtA4qkWE9BNj321hRnQrs6rHxspz6wWmvInfnru19Ups-LJPE7ccFIhb5JRqBuBKRdz2SNEAZsghsTYDKtLF7vGaDNnvtkvDlw1Qds7eBvhYdKGvaQ5BaFJm0RCZOu-F2DJiWcrrsM5qnyQJt8RMwGGWAeIn-8Fxtze9Q7V8yjjFP51uK_4im1Jxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :
ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.
پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است همیشه کامل یا دقیق نباشند. این ربات به اینترنت زنده دسترسی ندارد، جایگزین پشتیبانی انسانی نیست و اگر اطلاعات کافی نداشته باشد قادر به پاسخگویی نیست. لطفاً اطلاعات حساس یا شخصی خود را برای ربات ارسال نکنید.
برای مدیریت بهتر منابع و کنترل هزینه‌ها، محدودیت استفاده از ربات به شکل زیر تنظیم شده است:
- هر کاربر می‌تواند در هر ۵ دقیقه حداکثر ۳ سؤال بپرسد.
🕒
- سقف استفاده روزانه برای هر کاربر ۵۰ سؤال است.
📊
- در صورت رسیدن به محدودیت، ربات زمان تقریبی انتظار را نمایش می‌دهد.
⏳
- دستور /search و سایر دستورات عمومی شامل این محدودیت نیستند.
🚫
- محدودیت‌ها پس از راه‌اندازی مجدد ربات نیز حفظ می‌شوند.
🔄
این تغییر باعث پایداری بیشتر ربات و دسترسی منصفانه‌تر برای همه کاربران می‌شود. سپاس از همراهی شما
🌱
لازم به ذکر است در صورت سواستفاده این محدودیت بیشتر خواهد شد - پس خواهشمندیم با استفاده درست جلوی به ادامه این خدمات کمک کنید
لینک ربات :
@WhiteDnsResponder_bot
🔗
@whitedns</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/whitedns/1468" target="_blank">📅 11:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1467">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YN9vPo7j7cMf_0if5_HNhxWAE_je051b3uMKQgpIKXkU1_d1o2-MEnewKMxmuWwB6kgOFavYtc7Nn6Lzs_nEvKpa4gwAh_-V61uwj179trTX18_0VxJG8liRjw6XweJSxOU8uAk3KHULpUZXjBNg4Ll2_RuerqKR_Csi2Qzwqym6eM3aJ4yrvtpm3WqcVuTNqb4eZ64g0gGldNdqNaOtvJIaP-0Ag0_rNC7LqqWuALW6dTRnsJGYqFSJasJBRILR9sbh-pydqa3TRWY2MMZtgxoh_O6rJtXZO6FOP8FFXRwn2KrPuWHzlhaB5jdAeLOb4niPn1pM4vlwWhoiqiPFdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Coming soon............
WhithAester desktop
😍</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/whitedns/1467" target="_blank">📅 09:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1466">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🌎
پروژه WhiteVPN رو اوپن‌سورس کردیم و در گیتهاب میتونید بهش دسترسی داشته باشید.   https://github.com/WhiteDNS/WhiteVPN  همراه با پابلیک شدن پروژه، نسخه ۱.۳.۱ هم ریلیز کردیم
⛏
در این نسخه امکان • آپدیت اتوماتیک اپ  بعد از یک ورژن جدید • امکان routing برای…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/whitedns/1466" target="_blank">📅 09:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1464">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🌎
انتشار نسخه ۱.۳.۱ اپلیکیشن WhiteVPN
پست قبلی پاک شد. یک آپدیت کوچیک داشتیم به ورژن ۱.۳.۱
😆
از این به بعد آپدیت هارو اتوماتیک از داخل اپ میتونید بگرید</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/whitedns/1464" target="_blank">📅 08:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1459">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.3.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/whitedns/1459" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/whitedns/1459" target="_blank">📅 08:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1458">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTsiufHakrUnyf8iVZNDe9hGAJpKeU8NCX1j6zmxcLrVFsWtc5Myj2kSIzmsA7Mdf7Qg3SxwufG5poAX57Uri0ssoZum2SjVFEzJd-ObqUADpuSSIdJjjzNIdeQ75MoiKSxnUsl0FGG2fCxB56QVFtjl_nHQRzlH5u4kJ3nrFRGLqTlljOiUjMgZrxun7RiTPBvaBDjQynIGw1XwnIWolCnkLYPch_FFozKtVzDRnTMBA4ptpqMZqp6owbZnTOilY6-mgW7VYx3NczBOCR464YeqCqFnCtCO8eqlNWYgaqOO98EYXlYgm_E8nq0BhKTyAyZ4PUv4Pov1PmneQWDK5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
پروژه WhiteVPN رو اوپن‌سورس کردیم و در گیتهاب میتونید بهش دسترسی داشته باشید.
https://github.com/WhiteDNS/WhiteVPN
همراه با پابلیک شدن پروژه، نسخه ۱.
۳
.
۱
هم ریلیز کردیم
⛏
در این نسخه امکان
• آپدیت اتوماتیک اپ  بعد از یک ورژن جدید
• امکان routing برای سایت ها و آی‌پی های ایرانی به تنظیمات اضافه شده تا دیگه نیاز نباشه اتصال رو برای سایت های داخلی قطع کنید.
• اشتراک گذاری WhiteVPN در شبکه اضافه شده.
• حالا میتونید اپ پروکسی اپ در داخل اپ های دیگه مثل سایفون استفاده کنید.
• تست سرعت به سابسکریپشن اضافه شده
دانلود نسخه جدید از گیت‌هاب
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.3.1</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/whitedns/1458" target="_blank">📅 08:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1449">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/A1viLVGPE-mp_gD7VXBopOUzfuPMFuDmWZZEgjzRaJYzTPI7FXrq_g5Z1CLtWqCsxL2BQx9z7La5fdOg0KtZp3HVCQQRRJ4NoSpPlVRaVVxiclUnaYwHBSFcCtKy7Up_JkRnm1dObxIYntKDg0nkqFtkVvmb0iPO7WEtgh9C1E36W7G3u8ORVXPRg7zZ6571vp-gvWLtjwCWcpU7qRx0wfN7bk6JpASCiGEb7SCnSAsBUEHnYTMWf2Sp3hqUf__FlLfzArSJ2gVpRIKtHXghR63W3ZPaD4gN-hlVolJGkuGLzz1BHo-IJcPX5ss4OzXLh9ylrHi4A9kh73is2G-7Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther V1.0.2
دوستان سلام :
ما روی هسته Aether که حاصل زحمت دوست عزیزمون
CluvexStudio
هست یک کلاینت**
آزمایشی ورژن بتا
** درست کردیم . که اگر دوست دارید تست کنید و لطف کنید فیدبک بدید.
پیشاپیش ممنونیم
❤️
❤️
❤️
اموزش :
📖
**راهنمای WhiteAesther**
**۱ — نصب**
فایل **arm64-v8a** رو بگیر (تقریباً همه گوشی‌های ۲۰۱۷ به بعد).
مطمئن نیستی؟ **universal** همه‌جا کار می‌کنه، فقط حجمش بیشتره.
**۲ — سه تا نکته اول**
▪️
**Traffic** → گزینه Coverage روی **Whole device** باشه
⚠️
حالت Proxy only خودش هیچی رو رد نمی‌کنه! به‌نظر می‌رسه وصل شده ولی عملاً هیچ ترافیکی از تونل نمی‌ره.
▪️
**Routes** → پروفایل روی **Adaptive**
▪️
**Settings** → اجازه اجرا در پس‌زمینه رو بده، وگرنه با خاموش شدن صفحه قطع می‌شه
**۳ — اگه وصل نشد، به این ترتیب امتحان کن**
**قدم ۱ — پروتکل**
Routes → Advanced → Preferred transport → **MASQUE over HTTP/2**
📌
روی **همراه اول** مدتیه QUIC (یعنی UDP) کاملاً بسته شده. یعنی H3 اصلاً وصل نمی‌شه و فقط H2 جواب می‌ده.
از نسخه ۱.۰.۲ اپ خودش این کار رو می‌کنه.
**قدم ۲ — تیکه‌تیکه کردن TLS**
⭐️
Traffic → Advanced → **Split the TLS handshake** → روشن
فیلترینگ معمولاً فقط تیکه اول بسته رو می‌خونه تا ببینه کجا وصل می‌شی. وقتی تیکه‌تیکه بفرستی، نمی‌تونه بخونه.
اگه با H2 وصل می‌شی ولی کنده، **حتماً اینو امتحان کن**.
**قدم ۳ — پروفایل**
Routes → Profile → **Strict network**
(برای شبکه‌هایی که خیلی چیزها رو می‌بندن)
**قدم ۴ — خاموش کردن IPv6**
Traffic → Addresses → **IPv4 only**
روی خیلی از شبکه‌های موبایل ایران IPv6 نیمه‌کاره‌ست.
**قدم ۵ — مبهم‌سازی**
Traffic → Advanced → Obfuscation → **Aggressive**
💡
اگه قدم ۲ مشکلت رو حل کرد، **Off** رو هم تست کن — شاید پدینگ اضافه فقط داشته سرعتت رو می‌گرفته.
**قدم ۶ — اند‌پوینت دستی**
Routes → Endpoint → Specific address → دکمه **Find endpoints**
⚠️
گزینه Fall back automatically رو روشن نگه دار.
**۴ — گزارش مشکل**
Settings → Diagnostics & logs
۱. Detail level روی **Verbose**
۲. دوباره سعی کن وصل بشی
۳. برگرد و **Send** رو بزن
قبل از ارسال دقیقاً متنی که فرستاده می‌شه رو می‌بینی، و IP‌ها پیش‌فرض مخفی می‌شن. هیچی بدون اجازه‌ات از گوشیت بیرون نمی‌ره.
**نکته:** اون خط خاکستری کوچیک زیر متن بزرگ توی صفحه اصلی، پیغام خود موتوره. برای فهمیدن مشکل همیشه اول اونو بخون.
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.0.3
@whitedns</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/whitedns/1449" target="_blank">📅 11:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1448">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">دوستان عزیز،
در حال حاضر تنها مسیر درآمدزایی و تأمین هزینه‌های تیم WhiteDNS، کانال یوتیوب ماست.
❤️
برای حمایت از ادامه فعالیت‌ها و توسعه سرویس‌ها، می‌تونید کانال ما رو سابسکرایب کنید و ویدیوها رو تماشا کنید. همین حمایت ساده، کمک بزرگی به ادامه مسیر ما می‌کنه.
🔗
https://www.youtube.com/@WhiteDNS
ممنون از همراهی همیشگی شما
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/whitedns/1448" target="_blank">📅 11:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1447">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1zoN5Gm9juhIwA_zGqy_4RqCApk1RTm23DzC9IXOrYA8Z2Vqt_vKZW21QOHE9Z2OzEnIqMA1qrWnY8WWGEw0EXKEK2ZdDRAvPR-r_Oi4jdzaOOekmB3mnlvZr2xPaT7WajvmgSaQy1F_tucyDNkXznKT-1sKqWdkpBXG5h4rtF7Ja4Zkkf8yTYp_kdC0bJhWG-Sk1FgziQcvMrf_RSXQ_xRgvFxnMm83qcaBdfr_T0qyq6hEGZNLf_9KQcC7STbQPevSJ9vEeYlfVzuEAi4sIfYzMU5zjIP6rRe7uwSxHVNwsOJWMrZTDZAmHoNzz3pmTHzHe1gBlPxR9DK73P6Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
دانلود آخرین ورژن WhiteVPN اندروید
•   دانلود آخرین ورژن WhiteVPN دستکتاپ
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین نسخه CoreForge برای آیفون</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/whitedns/1447" target="_blank">📅 09:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1446">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🌎
سلام خدمت همه دوستان عزیز
در آخرین آپدیت سرویس ساسبکریپشن WhiteVPN ما مشکل کشور هارو حل کردیم.
حالا اگر از اپ اندروید یا دسکتاپ کشوری رو انتخاب کنید، کانکشن به کشور درست وصل خواهد شد.
⛏
دانلود آخرین ورژن WhiteVPN اندروید
⛏
دانلود آخرین ورژن WhiteVPN دستکتاپ
اگر اپ رو دارید، اول ساب خودتون رو رفرش کنید.
اگر مشکلی دیدید، حتما با ما به اشتراک بگذارید.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/whitedns/1446" target="_blank">📅 09:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1444">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">موقت
⚠️
هشدار مهم برای همه اعضا
⚠️
⚠️
⚠️
⚠️
دوستان عزیز،
بارها گفتیم:
به هیچ‌کس—چه ناشناس، چه آشنا—برای فیلترشکن، VPN، کانفیگ و… پول ندهید.
دلیل اینکه ما اینجا شبانه‌روز وقت می‌گذاریم همین است که شما
بی‌نیاز از پرداخت پول
باشید و گرفتار افراد سودجو نشوید.
اگر بدون پرسیدن از ادمین‌ها رفتید پول دادید و طرف کلاهبردار از آب درآمد، بعدش پیام می‌دید که «چی کار کنم؟» واقعاً ما در این مرحله کاری از دست‌مان برنمی‌آید.
چرا قبلش نپرسیدید؟
ادمین‌ها ۲۴/۷ پاسخگو هستند.
ما نمی‌توانیم در تک‌تک چت‌های خصوصی شما مراقب‌تان باشیم. لطفاً قبل از هر پرداختی، یک پیام ساده بدهید و سؤال کنید.
کلاهبردار پیام داده 1000 گیگ فیلترشکن BPB - به مرغ پخته بگی خندش میگیره
پول را واریز کرده - اونم در کسری از ثانیه بلاکش کرده -
حتما با تگ کردن ادمین ها افرادی که تبلیغ فروش VPN میکنندیا در خصوصی به شما پیشنهاد میدهند را گزارش دهید
این مکان با کمک و همراهی همه فقط میتونه امن و سالم باقی بمونه
ارادت</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1444" target="_blank">📅 07:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1443">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">Whitevpn dekstop v1.0.16
🍎
🐧
راهنمای استفاده روی مک و لینوکس
حالت TUN فعلاً فقط روی ویندوز کار می‌کند. روی مک و لینوکس دو حالت دیگر هست که برای اکثر کارها کافی‌اند.
━━━━━━━━━━━━━━━
🖥
روی مک — ساده‌ترین حالت
تنظیمات ← اتصال ← «پراکسی سیستم» را انتخاب کنید و وصل شوید. تمام.
مک تنظیم پراکسی را در سطح سیستم اعمال می‌کند، پس تقریباً همهٔ برنامه‌ها (سافاری، کروم، فایرفاکس و بیشتر اپ‌ها) خودکار از تونل رد می‌شوند.
━━━━━━━━━━━━━━━
🐧
روی لینوکس — یک نکتهٔ مهم
«پراکسی سیستم» روی لینوکس تنظیمات گنوم و KDE را عوض می‌کند. ولی این یک ترجیح است، نه اجبار: برنامه‌هایی که این تنظیم را می‌خوانند رد می‌شوند، و برنامه‌هایی که نمی‌خوانند نه.
معمولاً کار می‌کند: کروم، کرومیوم، فایرفاکس
معمولاً کار نمی‌کند: تلگرام دسکتاپ، ابزارهای ترمینال
برای آن‌هایی که کار نمی‌کنند، سراغ بخش بعدی بروید.
━━━━━━━━━━━━━━━
🎯
وصل کردن یک برنامهٔ خاص (روی هر دو سیستم)
اگر می‌خواهید فقط یک برنامه از تونل رد شود — یا برنامه‌ای پراکسی سیستم را نادیده می‌گیرد — این راه مطمئن‌ترین است.
آدرس پراکسی، بعد از وصل شدن، در صفحهٔ اصلی نشان داده می‌شود. روی آن کلیک کنید تا کپی شود. معمولاً:
127.0.0.1:2080
این آدرس هم SOCKS5 و هم HTTP را می‌پذیرد.
📱
تلگرام دسکتاپ
Settings ← Advanced ← Connection type ← Use custom proxy
نوع: SOCKS5 — آدرس:
127.0.0.1
— پورت: 2080
🦊
فایرفاکس
Settings ← Network Settings ← Manual proxy configuration
SOCKS Host:
127.0.0.1
— Port: 2080 — گزینهٔ SOCKS v5
⌨️
ترمینال (curl، git، npm و…)
این‌ها هیچ‌وقت از تنظیمات گرافیکی پیروی نمی‌کنند و باید دستی بهشان گفت:
export http_proxy=
http://127.0.0.1:2080
export https_proxy=
http://127.0.0.1:2080
(فقط برای همان پنجرهٔ ترمینال اعمال می‌شود)
━━━━━━━━━━━━━━━
💡
اگر نمی‌خواهید کل سیستم پراکسی شود
تنظیمات ← اتصال ← «فقط پراکسی» را انتخاب کنید. در این حالت هیچ چیزی روی سیستم شما تغییر نمی‌کند و فقط همان برنامه‌هایی که خودتان تنظیم کرده‌اید از تونل رد می‌شوند.
━━━━━━━━━━━━━━━
📥
دانلود:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.16</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/whitedns/1443" target="_blank">📅 16:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1440">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">Whitevpn desktop V1.0.15 ( linux 24+)
🐧
راهنمای نصب روی اوبونتو ۲۴ و بالاتر
بعضی از دوستان روی اوبونتو ۲۴ به بالا موقع نصب با خطای dependency روبه‌رو شده‌اند. مشکل از برنامه نیست — فقط باید فایل درست را دانلود کنید.
━━━━━━━━━━━━━━━
📌
اول ببینید نسخه‌تان چند است
در ترمینال بزنید:
lsb_release -a
یا از مسیر Settings ← About نگاه کنید.
━━━━━━━━━━━━━━━
✅
اوبونتو ۲۴.۰۴ و بالاتر (شامل ۲۵ و ۲۶)
فایلی را دانلود کنید که در اسمش webkit41 دارد:
WhiteVPN-Desktop-1.0.15-linux-amd64-webkit41.deb
و نصبش کنید:
sudo apt install ./WhiteVPN-Desktop-1.0.15-linux-amd64-webkit41.deb
⚠️
حتماً ./ را قبل از اسم فایل بگذارید، وگرنه apt دنبال آن در اینترنت می‌گردد.
━━━━━━━━━━━━━━━
✅
اوبونتو ۲۲.۰۴ و دبیان ۱۲
فایل بدون webkit41:
WhiteVPN-Desktop-1.0.15-linux-amd64.deb
sudo apt install ./WhiteVPN-Desktop-1.0.15-linux-amd64.deb
━━━━━━━━━━━━━━━
🎯
ساده‌ترین راه: AppImage
اگر نمی‌خواهید درگیر نصب و وابستگی شوید، فایل AppImage را بگیرید. اصلاً نصب نمی‌خواهد و به هیچ کتابخانه‌ای روی سیستم شما وابسته نیست:
WhiteVPN-Desktop-1.0.15-linux-amd64-webkit41.AppImage
بعد از دانلود، اجازهٔ اجرا بدهید و اجرا کنید:
chmod +x WhiteVPN-Desktop-1.0.15-linux-amd64-webkit41.AppImage
./WhiteVPN-Desktop-1.0.15-linux-amd64-webkit41.AppImage
(این فایل برای اوبونتو ۲۴ به بالا است)
━━━━━━━━━━━━━━━
💡
چرا دو تا فایل هست؟
اوبونتو در نسخهٔ ۲۴ کتابخانه‌ای که برنامه‌های گرافیکی از آن استفاده می‌کنند را عوض کرد. یک فایل واحد نمی‌تواند هر دو را پوشش دهد، برای همین دو نسخه می‌سازیم. فایل webkit41 مال نسخه‌های جدید است.
📥
دانلود همهٔ فایل‌ها:
github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/whitedns/1440" target="_blank">📅 13:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1438">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔵
WhiteVPN Desktop — نسخه ۱.۰.۱۵
🐧
رفع یک اشکال مهم روی لینوکس
روی لینوکس، بستن پنجره باعث می‌شد برنامه ناپدید شود اما در پس‌زمینه اجرا بماند — بدون هیچ آیکونی برای برگرداندنش. تنها راه بستنش، kill کردن از ترمینال بود.
دلیلش این بود: برنامه فرض می‌کرد آیکون نوار وظیفه ساخته شده، در حالی که خیلی از محیط‌های دسکتاپ (از جمله گنوم بدون افزونهٔ AppIndicator) اصلاً چنین آیکونی نشان نمی‌دهند.
حالا برنامه واقعاً بررسی می‌کند که آیا آیکونی نمایش داده می‌شود یا نه. اگر نه، بستن پنجره یعنی بستن برنامه.
📡
اشتراک اتصال روی شبکهٔ محلی
حالا می‌توانید اتصال این دستگاه را با دستگاه‌های دیگر روی همان شبکه به اشتراک بگذارید — گوشی، تلویزیون، یا هر چیزی که روی همان وای‌فای یا هات‌اسپات است.
تنظیمات ← اتصال ← «اشتراک روی شبکهٔ محلی» را روشن کنید. بعد از اتصال، آدرسی که در صفحهٔ اصلی نشان داده می‌شود را در دستگاه دیگر وارد کنید.
⚠️
توجه کنید: هر کسی که روی آن شبکه باشد می‌تواند از این اتصال استفاده کند و از کسی رمز پرسیده نمی‌شود. این را برای هات‌اسپات خودتان یا شبکهٔ خانگی روشن کنید، نه روی وای‌فای عمومی.
📤
خروجی گرفتن دسته‌جمعی از کانفیگ‌ها
اگر کانفیگ‌های خودتان را وارد اپ می‌کنید و تستشان می‌گیرید، حالا می‌توانید آن‌هایی که تست را پاس کرده‌اند یکجا خروجی بگیرید — به‌جای اینکه یکی‌یکی share بزنید.
تست بگیرید ← موارد سالم را انتخاب کنید ← «خروجی انتخاب‌شده‌ها»
خروجی را می‌توانید کپی کنید یا در یک فایل ذخیره کنید تا به گوشی یا تلویزیون منتقل کنید. حالت Base64 هم موجود است، چون بعضی کلاینت‌ها همان را می‌پذیرند.
━━━━━━━━━━━━━━━
⚠️
اگر نسخهٔ ۱.۰.۱۴ نسخهٔ مک (Intel) را دانلود کرده‌اید
فایل آن نسخه ناقص ساخته شده بود و احتمالاً درست کار نمی‌کند. لطفاً نسخهٔ جدید را دانلود کنید.
📥
دانلود:
github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/whitedns/1438" target="_blank">📅 12:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1437">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-poll">
<h4>📊 با whitevpn desktop وصل هستید ؟</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/whitedns/1437" target="_blank">📅 11:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1436">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دوستان، یه توضیح مهم درباره پروژه X4G که توی ویدیوی بالا معرفی کردیم:
بعد از انتشار ویدیو متوجه شدیم که به نظر می‌رسه بخش قابل توجهی از پروژه X4G از پروژه RVG گرفته شده، بدون اینکه اعتبار مناسبی به سازنده اصلی داده شده باشه.
🔗
پروژه اصلی
(لطفا برای حمایت استار بدید)
https://github.com/arvin341az-glitch/RVG
✍️
برای اینکه از سمت WhiteDNS حق و اعتبار سازنده اصلی تا جای ممکن رعایت بشه، این کارها رو انجام می‌دیم:
- اسم RVG رو به عنوان ویدیو اضافه می‌کنیم.
- توضیح مربوط به این موضوع رو در کامنت‌های ویدیو پین می‌کنیم.
- لینک گیت‌هاب داخل توضیحات ویدیو رو به ریپوی اصلی RVG تغییر می‌دیم.
این جور اتفاق‌ها متأسفانه توی دنیای Open Source پیش میاد. ما قبل از ساخت ویدیو با هیچ‌کدوم از توسعه‌دهنده‌های این پروژه‌ها در ارتباط نبودیم و طبیعتاً تشخیص اینکه یک پروژه از پروژه دیگه کپی شده، همیشه از قبل ممکن نیست.
ممنون از دوستانی که این موضوع رو به ما اطلاع دادن.
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/whitedns/1436" target="_blank">📅 03:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1433">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⏯️
آموزش ساخت فیلترشکن رایگان X4G + پنل شخصی  این پنل تقریبا شبیه به سرویس BPB هستش اما روی بستر سرویس Railway اجرا میشه و سرعت و امنیت بسیار خوبی داره.
🔗
تماشا در یوتیوب https://youtu.be/8G7xioYZqPQ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/whitedns/1433" target="_blank">📅 20:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1432">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=Hai-diclxbMeyX7jPGnSXXP2lOYyWbaTsow269eZc-DbuqJud18WCYFUUr1eUdyZfGoMBjLRG-ighMFghQo5R7U3e_sdOjSRXoPWHv8Wpc79__CxwcCuAzKS4ffqwadMy_bqB_5sNDqeSCdVDGV6zTeTyh6hx7P15Wrm-JHyxD0z15aO3mpdseqHVZkWNivMCnECLqTrFSn8foPhgWQYbYNGI0e89zKnIqdQda-pUBya7j5FtIy3Ny_L14mOy2lKOnv_R_R7dVdOvljguTRvoWlAkeMyOCadpVcMNjlFb_zK-aXVT7iuiIwnpT3-jWNpwhU5TF6F39kYyouerUUQUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=Hai-diclxbMeyX7jPGnSXXP2lOYyWbaTsow269eZc-DbuqJud18WCYFUUr1eUdyZfGoMBjLRG-ighMFghQo5R7U3e_sdOjSRXoPWHv8Wpc79__CxwcCuAzKS4ffqwadMy_bqB_5sNDqeSCdVDGV6zTeTyh6hx7P15Wrm-JHyxD0z15aO3mpdseqHVZkWNivMCnECLqTrFSn8foPhgWQYbYNGI0e89zKnIqdQda-pUBya7j5FtIy3Ny_L14mOy2lKOnv_R_R7dVdOvljguTRvoWlAkeMyOCadpVcMNjlFb_zK-aXVT7iuiIwnpT3-jWNpwhU5TF6F39kYyouerUUQUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش ساخت فیلترشکن رایگان X4G + پنل شخصی
این پنل تقریبا شبیه به سرویس BPB هستش اما روی بستر سرویس Railway اجرا میشه و سرعت و امنیت بسیار خوبی داره.
🔗
تماشا در یوتیوب
https://youtu.be/8G7xioYZqPQ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/whitedns/1432" target="_blank">📅 19:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1431">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مهم
⚠️
WhiteVpn Desktop
دوستانی که میپرسند اگر ما کانفیگ های ساب خود whitedns را تست میگیریم و بهترین را پیدا میکنیم . چطور ذخیره کنیم که همیشه داشته باشیم . ؟
شما با این روشی که من توی ویدیو نشون میدم میتونید راحت این کارو بکنید. , و همیشه اون کانفیگ را دارید
یادتون باشه که توی subscription باید حتما manual را انتخاب کنید تا ببینید
🔥
@whitedns</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/whitedns/1431" target="_blank">📅 16:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1430">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">White DNS
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1430" target="_blank">📅 12:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1428">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">White DNS
pinned «
دوستان عزیز،  در حال حاضر تنها مسیر درآمدزایی و تأمین هزینه‌های تیم WhiteDNS، کانال یوتیوب ماست.
❤️
برای حمایت از ادامه فعالیت‌ها و توسعه سرویس‌ها، می‌تونید کانال ما رو سابسکرایب کنید و ویدیوها رو تماشا کنید. همین حمایت ساده، کمک بزرگی به ادامه مسیر ما می‌کنه.…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1428" target="_blank">📅 12:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1427">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">دوستان عزیز،
در حال حاضر تنها مسیر درآمدزایی و تأمین هزینه‌های تیم WhiteDNS، کانال یوتیوب ماست.
❤️
برای حمایت از ادامه فعالیت‌ها و توسعه سرویس‌ها، می‌تونید کانال ما رو سابسکرایب کنید و ویدیوها رو تماشا کنید. همین حمایت ساده، کمک بزرگی به ادامه مسیر ما می‌کنه.
🔗
https://www.youtube.com/@WhiteDNS
ممنون از همراهی همیشگی شما
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/whitedns/1427" target="_blank">📅 12:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1426">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(Dᵢₐₙₐ🍓)</strong></div>
<div class="tg-text">📚
آموزش اسکن Resolver و استفاده در WhiteDNS (cottendns)
اگه دنبال یه Resolver مناسب و پایدار برای راه‌اندازی WhiteDNS هستی، توی این آموزش قدم‌به‌قدم نحوه اسکن و پیدا کردن IPهای مناسب با Clean IP Finder و استفاده از اون‌ها در CottonDNS رو توضیح دادیم.
⚡️
🔍
کاربردها:
• اسکن و پیدا کردن ریزالور های مناسب
• بررسی پایداری و سرعت Resolverها
• استفاده در WhiteDNS
• بهبود کیفیت و پایداری اتصال
📥
دانلود ابزارها:
🔹
Clean IP Finder v1.3.6
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/1.3.6
🔹
WhiteDNS v1.6.0
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚡️
ابزارها رو دانلود کن و طبق آموزش پیش برو.
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/whitedns/1426" target="_blank">📅 08:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1424">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔵
WhiteVPN Desktop — نسخه ۱.۰.۱۴
🔧
رفع اشکال آیکون نوار وظیفه (taskbar)
در نسخه‌های اخیر، منوی راست‌کلیک روی آیکون کار نمی‌کرد و امکان بستن برنامه از آنجا وجود نداشت — تنها راه، Task Manager بود.
مشکل از حلقه‌ای بود که پیام‌های آیکون را می‌خواند و روی رشتهٔ (thread) اشتباهی اجرا می‌شد.
اگر نسخهٔ ۱.۰.۱۲ یا ۱.۰.۱۳ را نصب کرده‌اید، این به‌روزرسانی را حتما داشته باشید
📥
دانلود:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.14
@whitedns</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/whitedns/1424" target="_blank">📅 10:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1423">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/NP5ddzBIQhaf92I9827gYjHDkeAOG-MIc-qsnlEVypJevuvr48UD2HOu4sWL4Q5PQZwFtsO9G_k3TNLh2iI19hGzgReC1gw_Iihp6V2ximJsqFTu_eOdL1r9C4hm5bAJcqf9UCTfwYRc6a29p8wlQHRR66ibBXry8XvZWpfQQOguUJVrzxS8RWuiC2mMTldFVkgKLllPbWK_DXXaXB7viu9DLnJkkxkjT1pNj90gRmNCAOCWnTh-do6w3_0CcB81EnRSALHBLbP3ruZf_AqfipSw4nteyuoVCmtz--bEXCaw0awycDd64Xofp0iAvsn_f1HFRCzGdXkgPPZwZhRscw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
WhiteVPN Desktop — نسخه ۱.۰.۱۳
Stable
🎯
حالت «فقط پراکسی» اضافه شد
تا حالا دو حالت بیشتر نبود و هر دو کل سیستم را از تونل رد می‌کردند. حالا سه حالت دارید:
• پراکسی سیستم — کل دستگاه (مثل قبل)
• فقط پراکسی — هیچ‌چیز روی سیستم شما تغییر نمی‌کند
• تونل TUN — کل دستگاه، حتی برنامه‌هایی که پراکسی را نادیده می‌گیرند
در حالت «فقط پراکسی» برنامه فقط گوش می‌دهد و شما خودتان تصمیم می‌گیرید چه چیزی از تونل رد شود. مثلاً فقط تلگرام، یا فقط یک افزونهٔ مرورگر — بقیهٔ سیستم دست‌نخورده و با سرعت عادی.
📌
چطور استفاده کنید
۱. تنظیمات ← اتصال ← «فقط پراکسی» را انتخاب کنید
۲. وصل شوید
۳. روی آدرس پراکسی در صفحهٔ اصلی کلیک کنید تا کپی شود
۴. همان را در تنظیمات پراکسی تلگرام وارد کنید
هم SOCKS5 و هم HTTP روی همان یک پورت کار می‌کند.
🔒
پورت دیگر عوض نمی‌شود
در این حالت پورت ثابت می‌ماند و خودتان می‌توانید تغییرش دهید. اگر برنامهٔ دیگری آن را گرفته باشد، همان موقع به شما می‌گوید — نه اینکه بی‌سروصدا پورت دیگری بگیرد و تنظیمات تلگرام شما یک روز بی‌دلیل از کار بیفتد.
━━━━━━━━━━━━━━━
⚠️
نکته برای کاربران فعلی
سوییچ TUN در تنظیمات جای خود را به یک منوی انتخابی داده. اگر قبلاً TUN را خاموش داشتید، روی «پراکسی سیستم» قرار می‌گیرید — یعنی دقیقاً همان رفتار قبلی. تا وقتی خودتان چیزی را عوض نکنید، هیچ فرقی نمی‌کند.
📥
دانلود:
github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/whitedns/1423" target="_blank">📅 19:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1422">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔵
WhiteVPN Desktop —نسخه 1.0.12
*stable *
🔋
از نسخه ۱.۰.۴ تا حالا تغییرات زیادی انجام  شده.
━━━━━━━━━━━━━━━
🔓
اشتراک‌هایی که باز نمی‌شدند، حالا باز می‌شوند
مهم‌ترین تغییر همین است. روی بعضی شبکه‌ها، اشتراک اصلاً دریافت نمی‌شد و خطای مبهمی دربارهٔ TLS می‌داد.
دلیلش این بود: نام سایت در اولین بستهٔ ارتباط بدون رمز فرستاده می‌شود. فیلترینگ همان یک بسته را می‌خواند و ارتباط را قطع می‌کند — قبل از اینکه اصلاً چیزی رد و بدل شود.
حالا آن اولین بسته به قطعه‌های کوچک شکسته می‌شود، طوری که هیچ قطعه‌ای نام کامل را در خود ندارد. سرور همان چیزی را دریافت می‌کند که همیشه، ولی دیگر چیزی برای تطبیق باقی نمی‌ماند.
این کار فقط وقتی انجام می‌شود که مسیر عادی شکست بخورد، پس روی شبکهٔ سالم هیچ کندی‌ای ندارید.
🔄
اشتراک‌ها خودشان به‌روز می‌شوند
اگر اشتراکی روی شبکهٔ شما باز نشود، فقط وصل شوید — اپ خودش آن را از داخل تونل دوباره می‌گیرد.
🔐
گزینه برای اشتراک‌هایی که گواهی‌شان تأیید نمی‌شود
روی بعضی شبکه‌ها چیزی وسط راه گواهی خودش را جای گواهی سرور می‌دهد. برای این حالت گزینهٔ «دریافت بدون بررسی گواهی» اضافه شده — فقط برای همان یک اشتراک، و فقط وقتی نشان داده می‌شود که واقعاً به کار بیاید.
⚠️
توضیحش را حتماً بخوانید: نشانی اشتراک کلید حساب شماست.
━━━━━━━━━━━━━━━
🔔
اطلاع از نسخه‌های جدید
اپ خودش بررسی می‌کند که نسخهٔ تازه‌تری منتشر شده یا نه و به شما اطلاع می‌دهد. دیگر لازم نیست دستی سر بزنید.
━━━━━━━━━━━━━━━
⚙️
تنظیماتی که حالا واقعاً کار می‌کنند
چند تنظیم بودند که ذخیره می‌شدند ولی هیچ اثری نداشتند. همه درست شدند:
• Split Tunneling —
اپلیکیشنی که کنار می‌گذاشتید واقعاً از تونل خارج می‌شود
• بررسی سلامت TLS — اتصالی که در آن دخالت شده باشد رد می‌شود
• نویز اتصال (Amnezia) — روی اتصال‌های WireGuard اعمال می‌شود
• پراکسی سیستم روی لینوکس — روی GNOME و KDE تنظیم می‌شود
━━━━━━━━━━━━━━━
🛡
حریم خصوصی و امنیت
• نشانی اشتراک دیگر در پیام خطا نمایش داده نمی‌شود. قبلاً اگر از صفحهٔ خطا اسکرین‌شات می‌گرفتید، کلید حسابتان هم در آن بود.
• روی ویندوز دیگر دسترسی Administrator نمی‌خواهد، مگر برای حالت تونل.
━━━━━━━━━━━━━━━
🐞
رفع اشکال
• پنجرهٔ مشکی PowerShell که هنگام اتصال در حالت TUN باز و بسته می‌شد
• نشتی DNS در حالت TUN
• در نصب تازه، لیست سرورها خالی نمایش داده می‌شد
• گزینهٔ پاک کردن اطلاعات برنامه و بازگشت به حالت اولیه در تنظیمات
• پیام‌های خطا حالا می‌گویند دقیقاً چه کاری باید بکنید
━━━━━━━━━━━━━━━
📥
دانلود برای ویندوز، مک و لینوکس:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.12
@whitedns</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/whitedns/1422" target="_blank">📅 14:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1420">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=mwK3pV3yJc6ZnipJZgUAUt_54RPnYKBmj4HM7cSbhkNYDXS-EfHXR8qqjM-3eSNTbftEj5lxX63bGZBvL2m5o0ilf7UbZPN4Na24wwkxxFgAVoJAGLzy1Ib0DtKH_LKNDAP-0OjE2F6Qq47tDmTqxXvIiZdBpMBwyPpSGAWiXPy-ug3CZ7TSORE24KN-oVltOBInEkkjjxippPUss2gXtMIZAxKE3xXFafTNzPQWpZFWJLEEO0vTc9hiKweahFYFxaM_IskUi4yNzxuJ_S0j82HzjjatAYrGnLOjOz0zzLIgcU2vYaMjMFHMCGTKgQcz4Sr2LLc_FGrESWQUNrrIwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=mwK3pV3yJc6ZnipJZgUAUt_54RPnYKBmj4HM7cSbhkNYDXS-EfHXR8qqjM-3eSNTbftEj5lxX63bGZBvL2m5o0ilf7UbZPN4Na24wwkxxFgAVoJAGLzy1Ib0DtKH_LKNDAP-0OjE2F6Qq47tDmTqxXvIiZdBpMBwyPpSGAWiXPy-ug3CZ7TSORE24KN-oVltOBInEkkjjxippPUss2gXtMIZAxKE3xXFafTNzPQWpZFWJLEEO0vTc9hiKweahFYFxaM_IskUi4yNzxuJ_S0j82HzjjatAYrGnLOjOz0zzLIgcU2vYaMjMFHMCGTKgQcz4Sr2LLc_FGrESWQUNrrIwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش فیلترشکن رایگان و امن با استفاده از متد های MITM و Serverless
مشاهده در یوتیوب
https://youtu.be/VYfQePhgEUU</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/whitedns/1420" target="_blank">📅 11:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1419">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔒
WhiteVPN Desktop نسخهٔ ۱.۰.۴ منتشر شد
🚀
۱. رفع نشتی DNS در حالت تونل — مهم‌ترین تغییر این نسخه
🔒
در نسخه‌های قبلی، وقتی روی حالت
TUN
وصل می‌شدید، خودِ ترافیک از تونل عبور می‌کرد — ولی درخواست‌های
DNS
از تونل بیرون می‌رفتند و مستقیم به مودم یا سرویس‌دهندهٔ اینترنت شما می‌رسیدند.
🌐
یعنی محتوای ارتباط شما محافظت می‌شد، اما
فهرست سایت‌هایی که باز می‌کردید برای ISP قابل دیدن بود
.
👀
علت پیدا و برطرف شد. حالت پراکسی هیچ‌وقت این مشکل را نداشت.
✅
⚠️
اگر از حالت TUN استفاده می‌کنید، حتماً بروزرسانی کنید.
🔄
۲. صفحهٔ Servers
🖥
•
انتخاب همه
اضافه شد
✅
•
کپی به کانفیگ‌های من
— یک سرور از ساب را به لیست خودتان کپی کنید و بعد آزادانه ویرایشش کنید
✏️
•
مخفی کردن
— سرورهایی را که نمی‌خواهید از لیست و از مسیر اتصال کنار بگذارید. بعد از بروزرسانی ساب هم مخفی می‌مانند، و هر وقت خواستید برمی‌گردانید
👻
• رفع به‌هم‌ریختگی ستون عملیات
🛠
⬇️
دانلود برای ویندوز، مک و لینوکس:
💻
🍎
🐧
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.4
@whitevpn
📲</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/whitedns/1419" target="_blank">📅 05:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1418">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=KEJ22TOWub8vD2CcSBS9DJqVuh3UCwWFhW5hAiSPzqT87hB6by5LN_87duQ6KbXvKurHf_O8IFr1XYgJkrs_MuzBunUB1qn4RnLotzSTMJ6lNMsF14JynDVVvndj6GUe62vE0SvupRVergrRoVUG2IWTsZqIIRJQz4--DK-VNi6umwxneh0CrpwHuuIX-0ApJyGUiuFeCUA_GPCVNfaju4jh1QZ6dozH_uhchv3OrkuSePPHAxNLIL_Cp1DFP040w06AKAMrirtr86zoix_VhMsrtqjYQCjuX9FMJH6wFOX58SwoxTgo846nM7RexE6TXGVBdXHKNK7g3i9m3cDBIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=KEJ22TOWub8vD2CcSBS9DJqVuh3UCwWFhW5hAiSPzqT87hB6by5LN_87duQ6KbXvKurHf_O8IFr1XYgJkrs_MuzBunUB1qn4RnLotzSTMJ6lNMsF14JynDVVvndj6GUe62vE0SvupRVergrRoVUG2IWTsZqIIRJQz4--DK-VNi6umwxneh0CrpwHuuIX-0ApJyGUiuFeCUA_GPCVNfaju4jh1QZ6dozH_uhchv3OrkuSePPHAxNLIL_Cp1DFP040w06AKAMrirtr86zoix_VhMsrtqjYQCjuX9FMJH6wFOX58SwoxTgo846nM7RexE6TXGVBdXHKNK7g3i9m3cDBIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش فیلترشکن رایگان و امن با استفاده از متد های MITM و Serverless
مشاهده در یوتیوب
https://youtu.be/VYfQePhgEUU</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/whitedns/1418" target="_blank">📅 01:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1416">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚀
WhiteVPN Desktop نسخهٔ ۱.۰.۳ منتشر شد
۱. اتصال خودکار از پایه بازنویسی شد
✅
حالا دقیقاً مثل نسخهٔ اندروید کار می‌کند: اپ دیگر خودش نودها را یکی‌یکی امتحان نمی‌کند، بلکه انتخاب را به موتور می‌سپارد تا از بین صدها نود، بهترینِ در دسترس را بردارد — و اگر نودی از کار افتاد، خودش روی نود دیگر می‌رود.
نتیجه: اتصال در چند ثانیه
⚡️
، و خطای «could not connect» که خیلی‌ها می‌گرفتند برطرف شد.
۲. رفع مشکل حالت تونل (TUN)
🛠
مشکلی که باعث می‌شد روی بعضی سیستم‌ها کانفیگ در حالت پراکسی وصل شود ولی در حالت تونل نه، پیدا و برطرف شد. کسانی هم که IPv6 سیستمشان را غیرفعال کرده‌اند دیگر با خطا مواجه نمی‌شوند.
۳. حذف و ویرایش کانفیگ در صفحهٔ Servers
✏️
کانفیگ‌هایی که خودتان اضافه کرده‌اید حالا قابل ویرایش و حذف هستند. برای اصلاح یک کانفیگ دیگر لازم نیست همه را پاک کنید و از اول وارد کنید.
۴. پیام‌های خطای واضح‌تر
📢
اگر اتصالی برقرار نشد، اپ دلیل واقعی را نشان می‌دهد نه فقط «ناموفق» — هم برای شما روشن‌تر است، هم گزارش مشکل را خیلی راحت‌تر می‌کند.
⬇️
دانلود برای ویندوز، مک و لینوکس:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.3
@whitedns</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/whitedns/1416" target="_blank">📅 19:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1415">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tnCR8-dNC_ySupPQaXoI-Fy6uN-Ca-LWbmIR2PL1XvahCFb6RgqTyu18nGowAVo6UPnS9ymgtNOL0kwh1GhDfXWA0FSM_CDKOmnb30NEojqzW9N4Avt2DuTiWKLdetZA56KO0iPhINERiL-3lcDn-m_K1Sp8UbFHv-vphTZora82XS2hfflQsuS9uS5HlxrWtGLwEKKrSZeJM4rdB6yMrBKAfjnpjkEH68xjBDuxCLzl52uk3l2IZEVgA9Dfw2xHIsOFxNOAythUu3c2xNSXeOKOJLeAEU8iIe5gKAMOnn8Jou-AkMaH7dLQ9ohLKV3oBS8UVl7iYLKvo9wqveXUvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteVPN
Desktop
نسخه 1.0.2 منتشر شد
🎉
مهم‌ترین تغییر: حالا هر نوع لینک اشتراکی را می‌شناسد
🔓
تا نسخهٔ قبل فقط لینک‌های اشتراک معمولی (vless، vmess، trojan و…) اضافه می‌شدند. اگر پنل شما خروجی Clash یا sing-box یا Xray می‌داد، برنامه خطا می‌داد
❌
از این نسخه این‌ها همه کار می‌کنند
✅
:
- لینک‌های اشتراک معمولی و base64
- کانفیگ Clash / mihomo (چه YAML چه JSON)
- کانفیگ sing-box
- کانفیگ Xray و v2rayN
- و حالت base64 هر کدام از این‌ها
فرقی نمی‌کند پنل شما کدام قالب را بدهد
📝
. سرورها مثل همیشه در صفحهٔ Servers می‌آیند و می‌توانید پینگ و سرعتشان را بگیرید
📶
، مرتب کنید و یکی را انتخاب کنید
🚀
.
دانلود:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.2
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/whitedns/1415" target="_blank">📅 15:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1414">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🌎
نسخه‌ی دسکتاپ WhiteDns منتشر شد!
📤</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/whitedns/1414" target="_blank">📅 11:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1413">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚀
معرفی اپلیکیشن WhiteDNS Desktop
کلاینت قدرتمند تونلینگ DNS برای کامپیوتر
اگر به‌دنبال ابزاری حرفه‌ای برای تونلینگ DNS، مدیریت پروکسی و عبور از محدودیت‌های شبکه هستید،
WhiteDNS Desktop
یکی از کامل‌ترین گزینه‌های در دسترس است.
این اپلیکیشن یک کلاینت محلی DNS Tunneling را روی سیستم شما اجرا می‌کند و در کنار آن، امکانات پیشرفته‌ای برای مدیریت پروکسی سیستم در اختیارتان قرار می‌دهد.
✨
ویژگی‌ها و امکانات کلیدی
🔹
پشتیبانی کراس‌پلتفرم
قابل اجرا روی Windows، macOS و Linux
🔹
پشتیبانی از موتورهای مختلف
امکان انتخاب بین موتورهای:
• CottenDNS
• MasterDNS
• StormDNS
🔹
پروکسی محلی کامل
دارای پروکسی‌های محلی SOCKS5 و HTTP، همراه با قابلیت تنظیم خودکار پروکسی سیستم
پس از قطع اتصال نیز تنظیمات پروکسی سیستم به‌صورت خودکار به حالت قبلی بازگردانده می‌شوند.
🔹
مدیریت پیشرفته پروفایل‌ها
امکان ساخت و مدیریت:
• پروفایل‌های اتصال چنددامنه‌ای
• پروفایل‌های Resolver
• Import و Export تنظیمات
• تهیه بکاپ از پروفایل‌ها
🔹
پری‌ست‌های آماده
تنظیمات از پیش آماده‌شده برای شرایط مختلف شبکه:
⚡️
Speed
— برای دستیابی به بیشترین سرعت
🛡
Survival
— برای پایداری بیشتر در شبکه‌های محدود
🔒
TCP Survival
— برای اتصال پایدارتر با استفاده از TCP
🔹
مانیتورینگ زنده
نمایش لحظه‌ای:
• وضعیت اتصال
• آمار ترافیک مصرفی
• اطلاعات نشست
• لاگ‌ها و رویدادهای برنامه
⚠️
هشدار امنیتی بسیار مهم
نسخه‌های رسمی WhiteDNS Desktop فقط از طریق ریپازیتوری رسمی پروژه در GitHub منتشر می‌شوند.
برای حفظ امنیت سیستم خود، برنامه را از سایت‌ها، مارکت‌ها، کانال‌ها یا منابع متفرقه دانلود نکنید.
📥
دانلود آخرین نسخه از GitHub رسمی:
https://github.com/WhiteDNS/WhiteDNS-Desktop/releases/tag/desktop-v1.2.0
📢
عضویت در کانال رسمی تلگرام پروژه:
https://t.me/whitedns
🤍
WhiteDNS Desktop</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/whitedns/1413" target="_blank">📅 11:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1412">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🌎
نسخه‌ی دسکتاپ WhiteVPN منتشر شد!
📤</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/whitedns/1412" target="_blank">📅 09:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1410">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XV_qSHdtb9OseH-_IFCImnOOh56GViZaOPaYDQ27How-l2d8HUphl2agZ_g_urIjzUbz_PPvwCviSEWOwpDVDyfWufVnikTYmBlHp13CYD4sPBhDL1lB0dYdAN6o0MhnOuuzax4ZM9WaO-dVKSFMzsQpzyVSS_q-9xPkrrGifEXgn6dbsURKTwJrqRGiY2hhbb-VgnmzlZT-h0H8gQvKZZpNwxoEsLdmk4h20HAXW0qqQNbtaBdk2spasVYB5YCrAKEdCZ9mGVvEp7VJOBfja5kz7mygErAXNgGhMlNDnFnP2SUCF4L4qcMBoHHP6xWW68ip3snrsrmAvN9AVG6ZLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
نسخه‌ی دسکتاپ WhiteVPN منتشر شد!
اگر می‌خواهید روی کامپیوتر بدون درگیری با تنظیمات پیچیده به VPN وصل شوید، WhiteVPN Desktop برای شما ساخته شده است.
💻
قابل استفاده روی:
• ویندوز
• مک، هم Apple Silicon و هم Intel
• لینوکس با بسته‌های AppImage، DEB و RPM
⚡️
اتصال ساده و سریع
• اتصال با اشتراک آماده WhiteVPN
• اضافه‌کردن اشتراک شخصی
• انتخاب خودکار بهترین سرور
• انتخاب دستی کشور، نوع اتصال یا سرور دلخواه
• نمایش IP و کشور واقعی اتصال
• بررسی خودکار سلامت اتصال و جایگزینی سرور خراب
📥
واردکردن کانفیگ شخصی
• پشتیبانی از VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard
• امکان واردکردن یک یا چند کانفیگ به‌صورت هم‌زمان
• فقط کانفیگ را کپی کنید و Ctrl+V یا در مک Cmd+V بزنید
• کانفیگ‌های شخصی در بخش Manual و بالای لیست قرار می‌گیرند
🚀
تست کامل سرورها
• بررسی سالم بودن سرور
• تست پینگ واقعی
• تست سرعت دانلود
• مرتب‌سازی بر اساس کشور، پینگ، سرعت و نوع کانفیگ
• تست‌ها بدون قطع‌کردن اتصال فعلی انجام می‌شوند
🛡
تنظیمات حرفه‌ای، با ظاهر ساده
• حالت Proxy برای ویندوز، مک و لینوکس
• حالت TUN برای اتصال کامل ویندوز
• تنظیم DNS و حریم خصوصی DNS
• Split Tunneling برای مدیریت مسیر برنامه‌ها
• تنظیم IP Fronting به‌صورت خودکار یا دستی
• مشاهده گزارش‌ها برای پیدا کردن سریع مشکلات اتصال
🧰
ابزارهای کاربردی
• White IP Generator: ساخت کانفیگ با White IP و اضافه‌کردن مستقیم به برنامه
• Validator: بررسی تعداد زیادی IP یا آدرس و ذخیره نتیجه‌ها
• Full Backup: پشتیبان‌گیری کامل از تنظیمات، اشتراک‌ها و کانفیگ‌ها و بازیابی آن‌ها
🌍
رابط کاربری کامل فارسی و انگلیسی
• نمایش صحیح راست‌به‌چپ
• فونت فارسی Vazir
• محیط ساده و مدرن
• ادامه اتصال در System Tray حتی بعد از بستن پنجره
📌
چند نکته درباره نسخه اول
• حالت TUN فعلاً فقط روی ویندوز فعال است
• در لینوکس ممکن است لازم باشد Proxy سیستم را دستی تنظیم کنید
• برنامه هنوز امضای دیجیتال ندارد؛ بنابراین ویندوز یا مک ممکن است هنگام اجرای اول هشدار نمایش دهد
🔓
WhiteVPN Desktop متن‌باز است و تحت مجوز GPL-3.0 منتشر می‌شود.
⬇️
دانلود آخرین نسخه:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
اگر برنامه برایتان مفید بود، لینک آن را برای دوستانتان هم بفرستید
❤️</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/whitedns/1410" target="_blank">📅 09:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1409">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سرور های فعال WhiteDNS داشته باشید برای تست و زمان قطعی (کلیک کنید روش کپی میشه)
کلاینت اندروید و IOS از CottenDNS پشتیبانی میکنن و به زودی کلاینت ویندوز هم آماده میشه
Server #1 thx to LordofCinder
♥️
Location: Turkey
🇹🇷
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HufCfh7cgdGh4IHRvIExvcmRvZkNpbmRlciIsInNlcnZlciI6eyJkb21haW4iOiJ2LmFzaGVudGFqaXIuc2JzLCBjLmFzaGVudGFqaXIuc2l0ZSIsImVuY3J5cHRpb25fa2V5IjoiZTU1NGI4ZmI4ZGU4Mjc4ZDJmMTFlODcwNDA0NDI2OWEiLCJlbmNyeXB0aW9uX21ldGhvZCI6M319fQ
Server #2 thx to Bamdad
♥️
Location: Germany
🇩🇪
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HqfCfh6ogdGh4IHRvIEJhbWRhZCIsInNlcnZlciI6eyJkb21haW4iOiJjLmJhbWFrLnh5eiIsImVuY3J5cHRpb25fa2V5IjoiMmRkZWI5ZGYyYzJiYTRkMyIsImVuY3J5cHRpb25fbWV0aG9kIjozfX19
Server #3 thx to Araskhatare
♥️
Location: France
🇫🇷
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-Hq_Cfh7cgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6InBhcmlzLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiI1MjViNjkwYjU4ZmU0MTI0IiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0
Server #4 thx to Araskhatare
♥️
Location: France
🇫🇷
2
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-Hq_Cfh7cgMiB0aHggdG8gQXJhc2toYXRhcmUiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiYS5hcmFzLmRwZG5zLm9yZyIsImVuY3J5cHRpb25fa2V5IjoiNzFkM2MwOWYyYmY1NmVkYSIsImVuY3J5cHRpb25fbWV0aG9kIjozfX19
Server #5 thx to Coreforge
♥️
Location: Turkey
🇹🇷
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh7nwn4e3ICAgdGh4IHRvIENvcmVmb3JnZSIsInNlcnZlciI6eyJkb21haW4iOiJ2LmFub255bW91cy5vYnNlcnZlciIsImVuY3J5cHRpb25fa2V5IjoiYjI3NTAzOTE5OWIxYzhjOSIsImVuY3J5cHRpb25fbWV0aG9kIjozfX19
Server #6 thx to Araskhatare
♥️
Location: USA
🇺🇸
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh7rwn4e4IDIgICB0aHggdG8gQXJhc2toYXRhcmUiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidXNhLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiI5MzY5NjVjZWYzOWQzMmE5N2JlMWEzZDA4YzhiZmM5MyIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
آموزش استفاده از برنامه اندروید
👇
https://www.youtube.com/watch?v=tz8cj7HzHVI
آموزش استفاده از برنامه ios
👇
https://www.youtube.com/watch?v=filwdiPKN90
آموزش استفاده از برنامه ویندوز
👇
https://youtu.be/Mc--GlKw2wg
@whitedns</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/whitedns/1409" target="_blank">📅 04:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1407">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/3ae84e81b7.mp4?token=K4n90Psr_OVSktkpllGfnXWyPHuH15dvOeiCKziOZsoRN3xEoHGSswbmhqDaIBw0gV0AmC0Yp7RRPyx1ZnMH4AcuAAKTbpkjG7EEgmMJDbDXaDRVHYndFd-qW2ep31ItnN7KMF3iH-NOPrHZu5_7G8MfoVENOFe8YN37vq9Y--Dat9HndkZ4kunEUvr_1Tg4Y1K8iC3BqGvvhlXz0NuEZ77bsbnUIwsRgM-7S2enMj4lzDmYvmeY8mKCS9uYgJMQssKh5QYYfze1qiovvjCApjexzVSZEqFvWpxZemvMRk48Axh8JbV4oC7Y1XfP5Z6hHZYbv6ONbCGGUn6wNZoeDA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/3ae84e81b7.mp4?token=K4n90Psr_OVSktkpllGfnXWyPHuH15dvOeiCKziOZsoRN3xEoHGSswbmhqDaIBw0gV0AmC0Yp7RRPyx1ZnMH4AcuAAKTbpkjG7EEgmMJDbDXaDRVHYndFd-qW2ep31ItnN7KMF3iH-NOPrHZu5_7G8MfoVENOFe8YN37vq9Y--Dat9HndkZ4kunEUvr_1Tg4Y1K8iC3BqGvvhlXz0NuEZ77bsbnUIwsRgM-7S2enMj4lzDmYvmeY8mKCS9uYgJMQssKh5QYYfze1qiovvjCApjexzVSZEqFvWpxZemvMRk48Axh8JbV4oC7Y1XfP5Z6hHZYbv6ONbCGGUn6wNZoeDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
🔥
نسخه دسکتاپ
whitevpn
اماده شده است و به زودی بعد از طی مراحل آزمایش منتشر خواهد شد
@whitedns</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/whitedns/1407" target="_blank">📅 19:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1403">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
پترنیها یه اپلیکیشن مشابه v2rayng زده که به نظرم از خود v2 هم بهتره چرا؟
هسته بروز که توسط خود پترنیها داخل اپ قرار گرفته و بروز بودنش حتی از v2 هم زودتره(بیشتر آپدیت هسته v2rayng از سمت پترنیها بوده)
رابطه کاربری روان تری داره.
مهم ترین نکته اش اینه با قابلیتی که واسه
#فرگمنت
اضافه کرده شما دیگه محدودیت آپلود داخل کانفیگ هاتون ندارید(بیشتر کلودفلره) ولی بعَی سرور شخصی ها هم مشکل آپلود دارن که طبق تنظیمات پترنیها اکی میشه
🔥
دانلود اپ از گیتهاب:
💓
https://github.com/patterniha/v2rayNG/releases
تنظیمات مربوطه به آپلود:
📝
https://t.me/patt_channel_x/94?single
💡
دوستانی که پترنیها رو نمیشناسن:پتنریها خالق sni spoof و شیر و خورشید و همچنین کلی از کارای بزرگتری بوده و داشته از جمله خود v2ryang و...
@xsfilterrnet
👑
@patt_channel_x
✅</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/whitedns/1403" target="_blank">📅 15:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1402">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚀
آپدیت WhiteVPN 1.2.0
✍️
تمرکز این نسخه فقط روی اتصال  سریع‌تر و پایدارتر بوده است.  امکانات و بهبودهای جدید: •  شروع اتصال سریع‌تر •  انتخاب هوشمند بهترین سرور •  جابه‌جایی خودکار در صورت اختلال سرور •  کاهش خطا و نیاز به چندبار زدن دکمه اتصال •  بهبود Real…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/whitedns/1402" target="_blank">📅 15:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1401">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(Dᵢₐₙₐ🍓)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS_Setup_Servers.md</div>
  <div class="tg-doc-extra">3.8 KB</div>
</div>
<a href="https://t.me/whitedns/1401" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
آموزش نصب DNS اختصاصی برای WhiteDNS
آموزش کامل و
قدم‌به‌قدم
نصب و راه‌اندازی:
🟢
CottenDNS
🔵
StormDNS
🟣
MasterDNS
از تنظیم دامنه در Cloudflare تا نصب DNS و دریافت
Encryption Key
🔐
📚
آموزش به‌صورت متنی آماده شده و
لینک آموزش ویدیویی
هم داخل پست قرار گرفته.
🎥
📥
فایل آموزش رو دانلود کن و برای روز مبادا نگهش دار!
🚀
@WhiteDNS
·:¨༺
@BlueKnight_Net
༻:</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/whitedns/1401" target="_blank">📅 16:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1398">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/whitedns/1398" target="_blank">📅 12:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1397">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc0b81933.mp4?token=PgqmW1m9mSsoJnJ_WVN_N2g_eRP3p7wdqZoZt-gtDQR0Iu6Zj-U17v7Hz5Bp3MzcKENTHrAdITU7uLn1wMGE3vvj1IcJ2dawJyJxYSZ5cPXA0bRKS05cGGG1JeFMDLwrToiRg8qy-FzxRf9iFNOlUiLmbUWMhVXC8GR-RKAU91tV2pAj9jPdQPEJz7HihK4EFBXZ2QC_bXsKhscUaNTWpbrWDMJbFeHsnhl3NRTMOuzHSLHpUJ_w4iLSCyLlXjM3t2JYQzhxZzrdWjHc5vMNB1UKgJqEeIV8CQxYKGjUFNMfj_EyeiNhISV8-Bb1zWgxOIhs-VAIuxjNmXlzf5peiigXkQ3YLykEF3X9TVuC4QdyaEOWCFI0yD8ej7DGkhZT9jze8LrK6aRkuClukSNXUHqF8M0jtzM6qL7rHClym5mPLJqgaSq5ZKI3v-neK9FzayQOZcwsZXMPcwOXNJML_cLxqZOzEpqgPhlV2Ixwj1VcVfOq3AghaSdPMPgTXsQOAM7LyRhstvwB67rJlqMntxx19TvMDWp4aQbA9aiAnjtsBlnxWt0_LB_x6y7L62mHQ3JM46hlGqI5VPnV4tIR_OKnVLkuPxboJ52T7vxpYCxIO40ADbte5PECnxEzVLxoakmS0mUelCaHbMoXUSe96Gbs7DYNhnNwf_lWQHSMRBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc0b81933.mp4?token=PgqmW1m9mSsoJnJ_WVN_N2g_eRP3p7wdqZoZt-gtDQR0Iu6Zj-U17v7Hz5Bp3MzcKENTHrAdITU7uLn1wMGE3vvj1IcJ2dawJyJxYSZ5cPXA0bRKS05cGGG1JeFMDLwrToiRg8qy-FzxRf9iFNOlUiLmbUWMhVXC8GR-RKAU91tV2pAj9jPdQPEJz7HihK4EFBXZ2QC_bXsKhscUaNTWpbrWDMJbFeHsnhl3NRTMOuzHSLHpUJ_w4iLSCyLlXjM3t2JYQzhxZzrdWjHc5vMNB1UKgJqEeIV8CQxYKGjUFNMfj_EyeiNhISV8-Bb1zWgxOIhs-VAIuxjNmXlzf5peiigXkQ3YLykEF3X9TVuC4QdyaEOWCFI0yD8ej7DGkhZT9jze8LrK6aRkuClukSNXUHqF8M0jtzM6qL7rHClym5mPLJqgaSq5ZKI3v-neK9FzayQOZcwsZXMPcwOXNJML_cLxqZOzEpqgPhlV2Ixwj1VcVfOq3AghaSdPMPgTXsQOAM7LyRhstvwB67rJlqMntxx19TvMDWp4aQbA9aiAnjtsBlnxWt0_LB_x6y7L62mHQ3JM46hlGqI5VPnV4tIR_OKnVLkuPxboJ52T7vxpYCxIO40ADbte5PECnxEzVLxoakmS0mUelCaHbMoXUSe96Gbs7DYNhnNwf_lWQHSMRBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش دریافت دامنه رایگان و نامحدود
دیگه لازم نیست برای کانفیگ های شخصیتون دامنه بخرید.
https://youtu.be/Tiods_aCJX8
@WhiteDNS</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/whitedns/1397" target="_blank">📅 11:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1395">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دوستان عزیز،
در حال حاضر تنها مسیر درآمدزایی و تأمین هزینه‌های تیم WhiteDNS، کانال یوتیوب ماست.
❤️
برای حمایت از ادامه فعالیت‌ها و توسعه سرویس‌ها، می‌تونید کانال ما رو سابسکرایب کنید و ویدیوها رو تماشا کنید. همین حمایت ساده، کمک بزرگی به ادامه مسیر ما می‌کنه.
🔗
https://www.youtube.com/@WhiteDNS
ممنون از همراهی همیشگی شما
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/whitedns/1395" target="_blank">📅 10:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1394">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⛏
۲ نکته برای بهبود سرعت WhiteVPN
۱. بعد از اتصال روی دکم
ه اتصال مجدد
کلیک کنید تا به سرور جدید وصل بشید.
۲. همچنین میتونید به صورت دستی تمام سرور هارو پینگ بگیرید و به بهترین سور به انتخاب خودتون وصل بشید.
آموزش تصویری</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/whitedns/1394" target="_blank">📅 08:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1393">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚀
آپدیت WhiteVPN 1.2.0
✍️
لطفا تست کنید و نتیجه رو با ما به اشتراک بگذارید.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/whitedns/1393" target="_blank">📅 07:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1388">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.6 MB</div>
</div>
<a href="https://t.me/whitedns/1388" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/whitedns/1388" target="_blank">📅 07:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1387">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf_cY2A_duclm1dOqdO56VFGnXFX9yU5Z90mekEqBds6RydUubxEO8xONr_djj4uCUbFvwXxEVw8qvDa9dZ_ix7-hglCKGAAMPoNu1nD3rreazHhC8AuChMHFnAgxf3KeFmDXP3FZ4R56wXbE6i7wINbqH6N6bBIR-z3Uk0V9aZs3rGWB8k7wPmTfS6d1TesO2Bfz2G-Q6VqQw5Nbmo39-QGyybmQpdJ6R3z8e2lv8taXsCvPmZ6wacH_FcNPCdHuyxM7NiCKul-7rsJvGgGLMAnCvIGnM_MRT1J2BXaDAEY7x9dWHtZPh_80Ipgiv95pEA8GOcTdOVQ6Nmw-QZViQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت WhiteVPN 1.2.0
✍️
تمرکز این نسخه فقط روی اتصال
سریع‌تر و پایدارتر بوده است.
امکانات و بهبودهای جدید:
•  شروع اتصال سریع‌تر
•  انتخاب هوشمند بهترین سرور
•  جابه‌جایی خودکار در صورت اختلال سرور
•  کاهش خطا و نیاز به چندبار زدن دکمه اتصال
•  بهبود Real Delay Test
•  رفع مشکل متوقف‌شدن اتصال در مرحله شروع
هیچ تنظیم خاصی لازم نیست؛ فقط برنامه را به‌روزرسانی کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/whitedns/1387" target="_blank">📅 07:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1386">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⛏
اگر در اتصال به WhiteVPN مشکل خوردید مراحل زیر را اجرا کنید
۱. به صفحه تنظیات برید
۲. از گرینه حریم خصوصی DNS گرینه DOH را انتخاب کنید
۳. مقدار زیر را جاگزین کنید
https://doh.whitedns.workers.dev/dns-query</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/whitedns/1386" target="_blank">📅 17:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1378">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZ1dYu2t-oXrwXtSc1BIm4llN5jiQxUQTP-Wy90T0v4AhB_HHuS_fQcnY91v6AU3_4s4qLSu_Frp9kGy-1ELDjKot-3rFOovrD23eqDeOPUU6Ub8ZRXqOip1NLBb6XGlVRXX-J-NTln1Gvb-j3dE2D9EdEpbmDDg-9bMol7mJA3fVfnSdlf5RZ4gtA6k23SjGEvddrHnVL7PY-E3Y5SDNlJ9V8skS9C028YyucAs8_isqUSQGzFDhL1v4q_QONMTnUuTiUYLsLs69uR4Lv8WsCLQW4W1LNYj2W-E6lFci9XCxq9IwwO85Hcr9OqDyxB1dFvJRdWxtC1bdRkT34zAbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">➖
➖
➖
➖
➖
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
دانلود آخرین نسخه برای  ویندوز
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
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/whitedns/1378" target="_blank">📅 11:25 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
