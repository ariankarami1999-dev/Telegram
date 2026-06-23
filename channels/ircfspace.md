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
<img src="https://cdn1.telesco.pe/file/S5Hb7Ew16ROw-imJSa4jt8j7CcokpuMf4AmU0q_GkJnT85CMcEVsA-XRmkZx2QMGyQH3VIy_0jc8HVXulvxNeGAr5wIjZqn6De63S8ScNB9kGEThl8S04HfanPuZrAq0CozDpu1ckoR8pXfolvGCM08TQ9HQWgsnCpYyVlDHI6aM1_CQ4X08NW3Rn2u99JGmdJiml8k4zfqhCsKt9FPl2Eo_ZdyFlSehmO-o4ZhzF2d79MfxsBko7lKPRcCsk6ltnQE1taQy1sNNcgJYYZHwqzr5094i5gKC53eFPxZd052Y5fpkoh7a6vWuF9Ey3a776zJPVe8I19zAYx9QRWT58Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 98.9K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 22:53:04</div>
<hr>

<div class="tg-post" id="msg-2459">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FUQK5O4sKrlHZowwb2lAMw_jopTmL4udR6nxgkAxElq0fH5OhyfWN-ALhrKdH7n05EESSCoPYQ7lK80LaS7zSYXdACB7o2GuQnXGfv-ncuPuxlrcrS0W3gqbxWgx1e6BiyxMCdAyc16sqtCyES9ykAjUNvI5AGYXs_ntA4z-Lzk_XYjXbxIgCzoD8EdW01k9f2bdVeSyTYapvlO0D7wmSE4XOCRWy2FKJRJyL7CGHGgLccEMN3MA352b5ojs_7-6X8dAH_psPhsDIvv2e7pZBgTzrxf99xZszV_p69V7rv5cUcWnLO8SBRajTKXIDWnFE_qGkC17AO2a6QOfE594SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیسیون اقتصادی مجلس طی نشستی با ستار هاشمی، وزیر ارتباطات و فناوری اطلاعات، از عملکرد این وزارتخانه در دوران جنگ تقدیر کرد. /دیجیاتو
بابت تقدیر یه کاسه دادن دست وزیر قطع‌ارتباطات؛ اما بابت ۸۸ روز
ریدن
به اینترنت باید یه لگن بهش تقدیم میشد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/ircfspace/2459" target="_blank">📅 20:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2458">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خدمات‌دهی دست‌کم ۸ بانک کشور با اختلال مواجه شده. شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، حملات سایبری را تایید کرد و نوشت "شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است". /iranintl
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2458" target="_blank">📅 16:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2456">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اختلال خدمات بانک ملی بعد از چندروز نه‌تنها برطرف نشده، بلکه این اختلال فقط محدود به همین بانک نمیشه و خیلی‌هارو گرفتار کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/ircfspace/2456" target="_blank">📅 13:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2455">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">جنگ شد، اینترنت رو بستن، تنگه رو بستن، آتش‌بس شد، توافق کردن، تنگه رو باز کردن، اینترنت رو بصورت تدریجی برگردوندن، گشایش شد، مسابقات جام جهانی سر رسید یا هر نمایش و کوفت دیگه‌ای؛ ۸۸ روز قطع سراسری اینترنت، سرکوب، اعدام، زندان، شکنجه و کشتار ده‌ها هزار نفر معترض دی‌ماه رو به فراموشی نمی‌سپریم.
خون‌هایی که روی این خاک ریخته شد و نسلی که هزینه آزادی رو با جون خودش پرداخت، از حافظه ما حذف نمیشن. بین ما و شما دریایی از خون فاصله هست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2455" target="_blank">📅 09:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2454">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rkhF15vAASHci_Cvk8itxy9dazXjSG_I9JE7dv1UzEdETpQ8bjX-NrTyIu14-VUdBOzNNQzHrc9pPm972xJVV6G4saJdiqnNzRjneMl1E4ogzyTCmACrQ1rSaj6woidtCBE8BlIpCqG9oMULJ_5Hg55QeHx516SwifXZy3Iga8IrLKiuV3Fo6KLBtb_Hp02awYFwOubAGNMeUqYBTvT36qBtTe-7bKS-h49QGMwuUe6JJG1XR024LFfYJlvgD7YbqxTgWzs6IVFoSSLNijChx8fYpfdd9QbZODQyOrMyUkg7e10JszMZ9vbmky8JAFH-m9DxzwE8AznRgpx2BkMjDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل V2X یک ابزار مدیریت اشتراک سبک و متن‌باز برای VLESS روی WebSocket + TLS هست، که به شما اجازه میده با دیپلوی پروژه روی سرویس‌هایی مثل Render، Railway یا DockFly، برای خودتون و خانوادتون اشتراک اختصاصی با قابلیت بروزرسانی خودکار ایجاد کنین.
این پنل امکاناتی مثل مدیریت کاربران و کانفیگ‌ها، تعیین حجم و تاریخ انقضا، نمایش آمار مصرف، مدیریت IPها، اسکنر داخلی و ارسال گزارش و هشدار به تلگرام رو در اختیار شما قرار میده.
👉
github.com/SulgX/SulgX-Panel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2454" target="_blank">📅 09:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2453">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aL1aKJptCWbPYSPgJsjw5qOwHWYf-OQiA6qR-RaXQwb9fl3ue_LVK4-8Rx4Rqg-bQKaAcKqdWhnkECgOCbyDrstzO-k0vYlfiDMqDGQNou4Kv90xDUyWyjW_gainw1NUCn1iDBsEawwiMILZjJhDtRlRJQcedHPFHNrKv9av-IfkJfS4LubSwOqrAgd7YLhy2iyxUgoSuSs1QOGr4BNXb8FjYSezC5wSXUeuGq6QhUcMYZKAsBa-eoD7v1HxS0lnx0g6wvzDSDLd-1rdxij6BtNUltQe9Jm4e2hLrd4BHvgPgbOAVHHIYb_dmlf_3U1uVhyEzc6kSuPE69TH63USfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از کاربران ایرانی به نام MrArrow دو مشکل مرتبط با فرگمنت در v2rayNG رو برطرف کرده، که از نسخه ۲.۲.۵ به بعد این اپ اندروید در دسترس هستن.
این کاربر توضیح داده که "چون تو شرایط فعلی اینترنت ایران Fragment نوع
tlshello
روی خیلی از اپراتورها دیگه مثل قبل جواب نمیده و بین حالت‌های مختلف،
1-1
معمولاً عملکرد بهتری داره و حتی با مقادیر پایین Length و Interval هم میتونه از فیلترینگ مبتنی بر SNI عبور کنه، یه سری مشکل در برنامه وجود داشت".
مشکل اول این بود که با وجود اینکه هسته Xray از Fragment نوع
1-1
پشتیبانی می‌کرد، اصلاً گزینه‌ای برای انتخابش توی رابط کاربری v2rayNG وجود نداشت. مشکل دوم هم این بود که v2rayNG عملاً فقط
tlshello
رو استفاده می‌کرد. یعنی حتی اگر توی تنظیمات نوع دیگه‌ای از Fragment انتخاب میکردی، موقع اجرای کانفیگ دوباره مقدارش به
tlshello
تغییر می‌کرد و انتخاب کاربر نادیده گرفته میشد.
👉
github.com/2dust/v2rayNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2453" target="_blank">📅 09:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2452">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YxqkJtTRaV00Vw1Aa7TrUyxmD_fM9KmXhfYqAKnPjwuITFastg3Bg4_7FvtHTOOPCRL_VMklzm2bYMA0j-Bs29pFvPNeOFgE_-jwam-y8d1ay7SNL_Fh7E-603-CdIj3uR7533hkVTlvc2EL_AQ7E3vzDzj_DegW0Vy8Ixbvia2TvDV1HjOOZ4l54c4gir0Cnhn_eIZGXUoG1wjjSa6sWrzdX-HJdQNbBfahDq5U7ThKn2-p54m6w9RgNyu9s3D42zF66q95KI5nG8yp0Qj8qCKihg2TLDOqkqvGL0PsleJzrBSBLLRv22EjFyDB9gyggm2GD-rAe-cUKOHcDYBG0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکت اندروید F-Droid (که کاربران میتونن بدون وابستگی به گوگل‌پلی، اپلیکیشن‌های آزاد و متن‌باز رو ازش دریافت و نصب کنن) هشدار داده که گوگل قراره از سپتامبر ۲۰۲۶ قوانین جدیدی رو روی اندروید اعمال کنه.
طبق این ادعا، توسعه‌دهندگان برای اینکه برنامه‌هاشون روی دستگاه‌های اندرویدی قابل نصب باشه باید در گوگل ثبت‌نام کنن، هزینه بپردازن، مدارک هویتی ارائه بدن و اطلاعات مربوط به برنامه‌ها در اختیار گوگل قرار بگیره.
منتقدان میگن این تغییر میتونه نصب برنامه‌های مستقل، پروژه‌های متن‌باز، نرم‌افزارهای شخصی و حتی برنامه‌هایی که خارج از گوگل‌پلی منتشر میشن رو با محدودیت جدی روبرو کنه. به همین دلیل F-Droid و برخی فعالان حوزه آزادی نرم‌افزار معتقدن اندروید بتدریج از یک پلتفرم باز فاصله میگیره و کنترل بیشتری روی اینکه چه نرم‌افزاری روی گوشی کاربران نصب بشه، در اختیار گوگل قرار میگیره. به همین خاطر کمپینی با عنوان Keep Android Open راه افتاده تا کاربران و توسعه‌دهندگان نسبت به این تغییرات آگاه بشن و به اون اعتراض کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2452" target="_blank">📅 08:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2451">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کاربران میگن "ظاهرا" دسترسی دیتاسنترهای داخلی به اینترنت داره برقرار میشه. فکر کنم هنوز از اون زمانبندی که نامسئولان قطع‌ارتباطات گفته بودن "بازگشت اینترنت درحال تکمیل شدنه" چند دقیقه باقیمونده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/ircfspace/2451" target="_blank">📅 08:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2450">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g6_Uyxv3zubOV_86-FTbS4aPnBEfltPEAJDG4vgUcVhJCQjZ3LlFqHDyVuVqBB3d12ZuO62r-oDKMOMgrxjW8Dlx6sIDxZOr7P3btyzXP0D4B7nrBUIkZ-cMjOOWottfGZcF7w_P83u-7_nUnIpa9Lpd9LC7n9A1l8w_tGjACTtY8TZ1AGnXVnmjttPZFauj9idF28aQVrKa5jKITOy0akKdw4xpwfgDC2Lh1Nh-c8-srA9WB1Yu8N8EbB2hz2pCH_yfTcomvBwick1RPlgtL2sd2ypo52pZHayhXEb1XFVcQAVhr9c2547q2vfsarhqXPODMkrR8RWHcAMQoQ-t1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما تنگه را مفت ندادیم، زندگی یک ملت را مفت دادیم. سال‌هاست حرص و ناکارآمدی‌تان را «سیاست‌گذاری» نامیدید، ماشین قراضه را ده برابر فروختید و گفتید حمایت از تولیدملی، اینترنت را خفه کردید و گفتید «مدیریت»، فقر را گردن تحریم انداختید در حالی که رانت و انحصار رگ‌های مردم را بریده بود. جوانی را به مهاجرت، کسب‌وکار را به «تاب‌آوری»، آینده را به سکوت فروختید. اگر چیزی واقعاً مفت رفته، نه تنگه هرمز، نه یک وجب خاک؛ عمر مردم، آرزوهایشان و فردای سوخته‌شان بوده. این صورت‌حساب واقعی است.
©
rassssoo
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/ircfspace/2450" target="_blank">📅 08:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2449">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">این اختلال GPS بخصوص در مناطق مرکزی شهر تهران برای چیست؟
داداش طرف اومد نقطه زنی کرد و رفت و تمام شد. الان GPS رو مختل کردید که چی بشه؟ ملت اونجا سرگردون و گم بشن؟
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/ircfspace/2449" target="_blank">📅 08:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2448">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C26SFmugHYLNVPxpNrYRsAN4X1xCx6XV0gOeI8mPIL2qQ8ff6Hgvu6XnNN-TwrnSghUF12JYlQ-vHNqYS09IP8oqmEhIf4THz1rWgNFbNFFnrfZFGQn0qKfXFIAR9JpsI08odPFDx2GO5kiNRxlc74raeKjb_4vcgfhrFDPqnHCgJmQg7Nxssqc7rs0zzbMqYhfqS1UmQ1MQMu5wCLijt9ipZ_wzlFi7OmQ77DsBQe8Y-Fhs_VV3coKKrzbqsyrdvfqAKmFB0i56LqHvvbSUmeVxZz1w8n9tZpGa8YBBZUidDMfihK3a0xvNArw9dl15CkbmBBquAgwgud_duotRJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه CandyTunnel یک ابزار متن‌باز و رایگان برای ایجاد تانل روی سرورهای لینوکسی هست، که با استفاده از تکنیک‌هایی مثل تغییر و پنهان‌سازی آدرس IP، رمزنگاری ترافیک، بازیابی بسته‌های ازدست‌رفته و روش‌های مختلف عبور از فیلترینگ، تلاش می‌کنه ارتباط کاربران رو شبیه ترافیک عادی شبکه جلوه بده.
این ابزار از پروتکل‌های انتقال مختلفی مثل UDP، ICMP، Proto58، TCP، QUIC، IPIP و GRE پشتیبانی می‌کنه.
👉
github.com/AmiRCandy/CandyTunnel/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/ircfspace/2448" target="_blank">📅 08:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2447">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cD8aS7uOOJGbLO33_kYUH9EnmThrox3PszMqVU94v3RMKI-7IIG5zc6yNnB1Ech6gPvZrlpFvAeUJtVwTlqJVDFO83geUtRJgzsLzx7UA1sFCHllE9dqTPRV92RmfBI6vT38gO4nW0z09B2evWRWBLVvwOTif6Bky-QmOq-Mv8xhNKflK-cdwCwzhpn-1Wl05gOX0BnqjZSa54ab0g-Up8r_1nllHdYzQ1cGSJ8fe97nUA-kJqwQIOqisgBk53--FKOOwS_YrT3ISDZyC6LJ1i9h9e_zaFaklqQi1ZyAQbiU165DOOV9qggnKBcFcqURWjnw_DGPeyecYcxx4natUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار Config Converter یک وب‌اپلیکیشن متن‌باز هست، که ۳ ابزار پرکاربرد مبدل V2Ray، مبدل WireGuard و مبدل Clash/Sing-box رو در یک محیط یکپارچه گردآوری کرده.
این ابزار امکان دریافت مستقیم کانفیگ‌ها از لینک‌های سابسکریپشن رو فراهم می‌کنه و ورودی‌های Raw، Base64 و JSON رو با تشخیص خودکار فرمت، پشتیبانی کرده. همینطور کاربران میتونن بصورت گروهی آی‌پی، دامنه یا پورت تمامی کانفیگ‌هارو ویرایش بزنن.
👉
darknessshade.github.io/Config-Converter
💡
github.com/DarknessShade/Config-Converter
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/ircfspace/2447" target="_blank">📅 08:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2446">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/biy4xvTnGSEG_mky7zsYnoQdeGEesas9Uu_A3Hq2dEIGoeZWWZUX5f_HBs8I_eO-isf-KQutZZC_Rs9jQ-sTHVT_BrWnnVoeCETm-ZNzG2TapOp5pLt6rMYfzFOlc2FJe15Yfrpz1vQPvCLcbpI-27XkmSAcZmYmMnJGK9Dlj_yx_OojDRb1JaYZ_Tpu66t8KELSWE4nMU1z6YOsJ777ATRT63-Oo1c2_Drt3Y5dOqX-logEPYyuVKgF0_i8TG5PrGR5VYsLNjlr3tRysWDmDrPcZWVzOe_px8DunEuS9RPrwF-aFh4hUeyXW8gZ2I0JET0RXRJbRbnecpLrZy_mOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان بازرسی کل کشور از توقف اینترنت پرو خبر داده و گفته اپراتورها اقدام به ثبت‌نام گروه‌هایی از جمله وکلا، مدیران و اعضای هیئت‌مدیره شرکت‌ها برای دریافت اینترنت با شرایط ویژه کرده بودند. در اجرای این طرح، هماهنگی‌های لازم با رگولاتوری و وزارت ارتباطات به‌طور کامل انجام نشده یا در برخی موارد محل اختلاف بوده. بنابراین مقرر شده از ادامه اجرای بخش‌های دارای اشکال جلوگیری بشه و مبالغ اضافی دریافت‌شده از مردم رو بهشون برگردونن. /فارس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2446" target="_blank">📅 18:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2445">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kgsStB5fYZ9KTl4jI5DG-f5xBfTYbmcf609Qgog0q3gGllafd7s-CkKOeb02aNv_qnEXaHJV9BetcWfJh6A_7Fyhw9m5M7FQW6JGMHHet5waDlsAcqIBOdafTPmr4kfzIDCjWRMSJ9Ifn8wS0JnUzIgNMwpiV6vus-mHxzPULtWJkARQidTZz4CZtpXZlEEd7gGiIhS9IE9Ur8v93eJJVmObQSxd6EyMosPt7hb6XBUDGr2upcdBglsCjOiQcNTSNC6o5717MRF6_fMVVPsMpfC4SO9qLSm8asuLtp46V1MauC4RZfE6l2NpYt7u63qNnszS9o-kjFccfp20lOqktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه NipoVPN یه ابزار پروکسی سبک و قدرتمنده که درخواست‌های واقعی HTTP رو بین ترافیک عادی وب مخفی می‌کنه. این پروژه با معماری Agent-Server کار می‌کنه؛ یعنی برای استفاده ازش، اول باید هسته رو روی یه سرور راه‌اندازی کنین و بعد کلاینت‌ها به اون وصل بشن. در حال حاضر هم کلاینت رسمی اندرویدش به‌صورت متن‌باز و رایگان منتشر شده.
👉
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/ircfspace/2445" target="_blank">📅 08:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2444">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M47zySNL88DxET-beed_kF8sDnb4X3Pin0F1oD9Diko6vtqNXe09RJZ3DfmQ8JuS3UbvSaxJ8w7rd5P6T8RqlkUGJJROD5dPAE9OhRZMtfWnfb99mC3VnMhhIpshZZ_Q1Ej1oPmrexsL0YY5SRXshpd0Cqi6ydleB55hsuDDacarIbjWbmKbiQCebS6MdGgH3do12gWWsih02CzX4e7FoSeKg0afDV39jNxxdaEpkzP-FGrZrKhMCgBcGxnGI6AyGJiQrSMs1GaUcIMDP3nuE71M-kPrurIFiNmkC2JcgT8Wq9edO7outsXUoMiWc3MRLTYtyRdHGfVumY84BJ09tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ InviZible Pro در بروزرسانی‌های اخیر نسخه بتا، با اضافه کردن Tor Snowflake و پشتیبانی از پل‌های DNSTT، قابلیت‌های ضد سانسور خودش رو برای عبور از محدودیت‌های اینترنت گسترش داده ...
👉
github.com/Gedsh/InviZible/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2444" target="_blank">📅 08:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2443">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پاول دورف، مدیرعامل تلگرام در واکنش به محدودسازی استفاده از شبکه‌های اجتماعی برای افراد زیر ۱۶ سال در بریتانیا گفته: این ممنوعیت فقط اونهارو بیشتر در معرض خطر قرار میده و کودکان به استفاده از VPNها روی میارن، که در نتیجه به محتوای غیرقانونی و به‌مراتب خطرناک‌تری دسترسی پیدا می‌کنن. برای مثال هم به استفاده بالای فیلترشکن در روسیه و ایران اشاره کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2443" target="_blank">📅 08:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2442">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">از میان ۴ بانکی که اختلال برایشان پیش آمده، ۳ بانک در بستر ایران‌اکسس فعالیت می‌کنند و دسترسی مستقیم به اینترنت ندارند. یعنی هیچ ارتباطی بین آن اختلال‌ها و وصل شدن اینترنت نیست.
©
emirhussein_rz
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2442" target="_blank">📅 08:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2441">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DKp8j1Bihh_CMQe4kmYfZ-be1Yu0_kYPDbV6uvYBbj_XjqBcA_HXC_ey9JiYuTsLVL_EMG1nho5jrQkLp5sod7MpJCTVchA7fgQNyrUInoCs-iUlpVJzLwXonwIYBFeHDP2QgHJGEMnKwrZff7ItXzX3WUEMWz78gMLeLkW_phrYVnj9VlpmEfewERUQ2xeD4d9tR0STZiGTSsBhgmG7_yyWf_5l-Tfrwh0DZG9c1lVykM7cNRQPLywfZHBGRH3cKRA2mnvMzImzMxNxP5KPBsymI8NH8PxKunsJkqFeNVdfYJiYkUohRo6Nqs1s7Y83wnChbTnGIAa3CmEyTr8vKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویروس زارع‌پور به هندوستان رسید؟
دولت هند اعلام کرد که دسترسی به تلگرام رو در هند تا اول تیر مسدود کرده، چون از این پلتفرم برای کلاهبرداری از داوطلبان شرکت‌کننده در آزمون ورودی پزشکی استفاده شده. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2441" target="_blank">📅 08:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2440">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o3Iwoan4OMjDb0kONA564WPbeoU-LZIBB3DD8DWyrVSA_NFrl0z0_TIj1lakA3jlTbSEAxuyb9ZJ8tXiVK_ne1Numa2BNXOJJDyrYjF4KhFZSC9W5nJq1vWDZmQ035BG3ifqMggrEImR6Q3fZB0vwl1VERFOImAJp2jWuGE4NEKLKdw1NN2LMmgqOK4QeW1nRxfzJUsuuedUftqvYLMeJs8-wfZ-HNIJJGEp-18ZPPMmaBYnDqWglW4IJGmKdoCOzkkhj92VTkYW4j7lQlmuCENXA7yba5u5SVUHx628OPYdZ2KSHUYFa3UfrC1Z7FZrXi3z1hpKrj9LNnyFuap4QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ سیمرغ یک کلاینت VPN متن‌باز و رایگان برای اندروید هست، که با پشتیبانی از کانفیگ‌های XRAY، پروفایل‌های NipoVPN و موتور اختصاصی MSP، تلاش می‌کنه بهترین مسیر اتصال رو با کمترین پیچیدگی در اختیار کاربر قرار بده.
اسکن هوشمند آیپی، انتخاب خودکار کانفیگ سالم، پشتیبانی از کانفیگ‌های ServerLess، پروکسی محلی، ذخیره IPهای تمیز، بررسی سلامت کانفیگ‌ها و ... از جمله امکانات این برنامه هستند.
👉
github.com/rezakhosh78/SIMORGH/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2440" target="_blank">📅 20:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2439">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">با وجود ادعای رفع مشکل قطعی و اختلال در خدمات ۴ بانک بزرگ دولتی، این اختلال‌ها برای سومین روز متوالی ادامه دارد. نیما اکبرپور، کارشناس فناوری، معتقد است طولانی شدن روند بازیابی، نشان‌دهنده ناکارآمدی سامانه‌های پشتیبان است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2439" target="_blank">📅 19:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2438">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/672c6641f0.mp4?token=tSQkRzBqjUbZ8zRAve6NKJJI53Y5tMoDv198H1D7EQq-2DK0Hn3qVh-1mYsV6aUCmnGRG-ulloIBwMRgspgYysWCQTVIACXZST6BgTEjF174fc-DdSJQaFbn8xpngG35KgW4UKsUAui7L7vogxhyD25FIaVHw_EV-YJjUUdMXucvtgrECgM1P8DiVocGSjzy5Ecr-2j61BCeTl9moPeyJ6JroiNNftAZ-durDlLhHnqW1862WljkvSYfOt_GeJvVUdKznZY_VMmXMypf0pshyrZNvfSACtYh_QBwTSSr55NbV4d4x1GDA6loMw6T6VaQZaoZnuCfvIIoUn6IkO5H1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/672c6641f0.mp4?token=tSQkRzBqjUbZ8zRAve6NKJJI53Y5tMoDv198H1D7EQq-2DK0Hn3qVh-1mYsV6aUCmnGRG-ulloIBwMRgspgYysWCQTVIACXZST6BgTEjF174fc-DdSJQaFbn8xpngG35KgW4UKsUAui7L7vogxhyD25FIaVHw_EV-YJjUUdMXucvtgrECgM1P8DiVocGSjzy5Ecr-2j61BCeTl9moPeyJ6JroiNNftAZ-durDlLhHnqW1862WljkvSYfOt_GeJvVUdKznZY_VMmXMypf0pshyrZNvfSACtYh_QBwTSSr55NbV4d4x1GDA6loMw6T6VaQZaoZnuCfvIIoUn6IkO5H1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانفینگ
😄
©
miladiels
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2438" target="_blank">📅 19:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2437">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">در پی تجمع مخالفان توافق ایران و آمریکا، خبرهایی از اختلال در
#ملانت
و پیامرسان‌های رانتی منتشر شد. خواهشاً اینترانت ملی رو قطع نکنین؛ عده‌ای اگر مدت کوتاهی از پروپاگاندا و خوراک تبلیغاتی حکومت محروم بشن، ممکنه ناخواسته شروع کنن به فکر کردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/ircfspace/2437" target="_blank">📅 08:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2436">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فاجعه یعنی اینکه اول حمله سایبری رو تکذیب کردن، اما بعدش بصورت رسمی تایید شد. الانم نشت اطلاعات مشتریان رو تکذیب کردن، احتمالا چون قبلا هرچی بوده و نبوده پابلیک شده!
شورای هماهنگی بانک‌های دولتی، اعلام کرد: به پیرو اختلال پیش‌آمده در سامانه‌های ۴ بانک ملی، تجارت، صادرات و توسعه صادرات، تیم‌های فنی بلافاصله پس از شناسایی نشانه‌های غیرعادی، اقدامات پیشگیرانه و حفاظتی لازم را برای صیانت از داده‌های مشتریان و زیرساخت‌های بانکی کشور به اجرا گذاشتند. بررسی‌ها نشان می‌دهد حمله سایبری محدود به چهار بانک بوده و هیچ نشت اطلاعاتی رخ نداده است./ انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/ircfspace/2436" target="_blank">📅 23:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2435">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ایرانسل و همراه‌اول با گذاشتن ضریب روی بسته‌های بین‌الملل قشنگ
عَنِ
دزدی رو در آوردن. گِل بگیرن در اون وزارت ارتباطات و سازمان حمایت از مصرف‌کننده رو، که دزدی اینقدر راحت و علنی شده. البته چیز دیگه‌ای هم نباید انتظار داشت، یه مشت دزد دور هم جمع شدین!
©
Mohsen_935
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/ircfspace/2435" target="_blank">📅 17:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2434">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MyQUff_nWJquOld_TODlwmjmw1CyUessC9W57eaifIqRaHHT5JsIvXYiDIoRKUKtzbTLwUbOkbMryzEJpNkqFQHzCopGpHwUPjQ6obxcMhH5TL_ja7aQo86WpPNsz_5V4_9p6GE5YcqAE930JcGCF_fw35IC2D2ha6BC6Xin76SYfAXtaVLHZVc1ItjsmAGnt9Yx88RzOjJPiw4-EOyaWtR7cdQEV_pahIjLsEozgH7wVqkhNnvbPgOQlaw7asuXW0xlG7OQYcGLcVTYGwcQfJtPdu28TxcU4h28QxgGrWOG8QyndhJ4EdiRgpvXPm9tHoUEyih-MDkr4-4hWFF_yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به دنبال بروز مشکل در ارائه خدمات بانک‌های ملی، صادرات، تجارت و توسعه صادرات از صبح امروز، پیگیری‌ها نشان می‌دهد عامل اختلال بروز مشکلات زیرساختی در شرکت ملی خدمات انفورماتیک بوده و ارتباطی با حمله سایبری ندارد.
البته تاکنون زمان دقیقی برای رفع کامل اختلال اعلام نشده است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/ircfspace/2434" target="_blank">📅 17:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2433">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BV7hzsHFkHXK1E7HMCd8wOaNjzK6aGMT58j9fiZjCO0OSD4v2MFIHsLpp9S7Yarp90ZBjlV4Or4SvAfe0L0evwPvM0doFmTia073vy0_iKcbUaUeQsmWtnjdMvZC62Q5nHzWpkW-2564U3cXZ60CkDcrg6kNjY0KOtzMsa_vmDUbenRaKUYNGTQNWv9N-VsoPkbcTrcxeXpWz6WiooNRgSmBGgfjyU3uYSm0obSEunuPD49pjTh5NNfdGq1lMYAhQZLWA0TPtxCT4WFtLB46pkTOUe-Gnsl9JMd4sqe_RtbD3paXd8qb37vX2OOUyF6NLYmYGOWYjn-Xq7WuP2b11g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اعلام کرد پس از دریافت گزارشی درباره فعالیت ده‌ها کانال یوتیوب مرتبط با اشخاص و نهادهای تحریم‌شده ایرانی، علیه برخی از حساب‌های ناقض سیاست‌های خود اقدام اجرایی انجام داده است. این شرکت جزئیاتی درباره تعداد کانال‌های مشمول این اقدام یا نوع محدودیت اعمال‌شده منتشر نکرده است. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2433" target="_blank">📅 17:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2432">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P3Ky6BI877pjCHh6VPAOczyZ3xGRrf5x1VIqWgDpN1s0_BSAzL7X6tg3EuNhK00d3JIQgHOEYUjZqe25XzaDLemx12sbOtptaZvXmKNnVUAIMEcT0sQaCjLAf6vyY4_2XsIvhUPw4UKCaRNR7VqRpFu9xEGflyQ9oounp6R1yPvdVP_Wkq3B1AzX1yP1lrKen9s4Yg_t4NQXsuBBeyBVPUgGgHkfm90eutxOIY8e5UpmcMgknehxTPQGMFgS3Kn8OLcpr1wvDoQ41zUF37IwhiBZlFB5P0Rf8gj3S4MclfHRzIG0PWTrHc1IsVR93O5TxCkQgW2FnniWcBWqKxxJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستار هاشمی، وزیر قطع‌ارتباطات اعلام کرد پیش از بازگشایی اینترنت حجم ترافیک استارلینک با کل ترافیک اینترنت کشور برابری می‌کرد. او همچنین طرح وایت‌لیست اینترنت را برای جمعیت ۹۰ میلیونی ایران غیرعملی و غیرقابل اجرا دانست و گفت به آنکه ایده‌اش را مطرح کرده بود گفتم ماستت را بخور. /یورونیوز
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/ircfspace/2432" target="_blank">📅 08:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2430">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ea-DB7CwiXcz0K86tg2fUzpjJ54c00iWt7yerPaGw1YxYb73LXEg_FhAtkmJ_P4eLrahB7TiI0dngzITHlaEY4stI95u8l31wStnVconjo6GbFUiWaxrAwq2MW9H_vKmKdfP2rZFYt7iDIHrwZ4yw5sSLHxuQjjdLFTsFNqDE3P2eZiDWUnhruE_BM8GU-Lk2icfZPmawJcVZks9gCyNKR2XAarzhA_DcXZuT4gyymP-PDUxde5V8XOZ65xFhupFOtQLipdY7eM3L-w9hkRwOlrF5xJz6SWMgxVtj7P1xVjHioJ9kOlflXErPrp8x40ydz6HJ_QJHqZV1z1Psh73nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌دنبال توافق‌نامه‌ای که در اردیبهشت میان شرکت ارتباطات زیرساخت ایران و آذربایجان برای توسعه ترانزیت داده و زیرساخت ارتباطی به امضا رسید، بخشی از داده‌های ترافیک اینترنت ایران به اپراتور Delta Telecom در آذربایجان منتقل شد.
داده‌های موجود نشان می‌دهد که آذربایجان در مدتی کوتاه از رده چهل‌وچهارم مصرف ChatGPT در جهان به رده سوم رسیده، که انتقال ترافیک اینترنت ایران از مسیر یک اپراتور آذربایجانی این اتفاق را رقم زده است. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/ircfspace/2430" target="_blank">📅 07:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2429">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور گفته "نگرانی برای قطع اینترنت وجود نداره و اینترنت قطع نمیشه".
از اونجایی که دولت کلاً هیچ‌کاره هست، نگرانیم بیشتر شد!
😒
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/ircfspace/2429" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2428">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e0av0o-M6YNwE9BVL5xsB5VXUHTKepAWVFMxJbRuaTmLlkOmk2DeppVJtW8R_NW1FyGw9C1d52bxTo7onW8xZjmqKv-0r23x_Jzpo9vlGzQqGG3KclV3dxlIn8XSGtbbBTfbHYv4NBacggkwDOujyxjo5z3A83JIYhxAl95vFZHKzSxNFJZlhUCvarNKAn9MBbYd6QtqjzK3IkeAbTHxpNgmdVzKJZHDFZV5F79dKyAH8ybqYgde3FwLcrR3aUdiVJayPiiFxY_bcdBSFv2KaDD3EtVdOF_p-8lYprlcQWhXqX9FPou7dv6Iej_7K5RM0aL_xscJXy7fR3Ms8kPYiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آپدیت جدید از فیلترشکن متن‌باز و رایگان pyWarp که برای ویندوز، لینوکس و مک ارائه شده، ۹ مسیر اتصال به وارپ (با انتخاب گزینه Auto در Protocol) چک میشه و در نهایت اگر اتصال امکان‌پذیر باشه، بهترین رو انتخاب میکنه.
👉
github.com/saeedmasoudie/pywarp/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/ircfspace/2428" target="_blank">📅 08:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2427">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">هنوز موشک‌ها توی آسمونن و به زمین اصابت نکردن، پهنای باند رو کاهش دادن و گزارش کاربران از کندی اینترنت و افزایش اختلال‌ها حکایت داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/ircfspace/2427" target="_blank">📅 23:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2426">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بعد از ۸۸ روز قطع سراسری اینترنت و برگشتن دسترسی‌ها، هنوز اوضاع اینترنت به قبل از دی‌ماه برنگشته که دوباره دارن واسه همدیگه خط و نشون می‌کشن. انگار باید خودمون رو برای یه قطع سراسری دیگه آماده کنیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/ircfspace/2426" target="_blank">📅 20:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2425">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rj9IHW6PCTyxSJD8jl8W27dt6_uJHlIwAE4uC0ZYsi1CQwxLYuWY7ReSnZHxVxdqaV14UShwEZHuVBz7UxGQYGqZGaJkcVNq_ppCJd1dCytJ7G8rfoAzJUhgf57BUAD9Mdifvmtd2z__8eDNCqt2SJbz_x3k_mBj43EXI3ptSSBiGqFNq0nTj8483E_RfzVgAuUkBPVgxlazQCaOJt0JMDEOMOjIhYI_0V6oVOKYt4fjim7ih79Pd0ZUSiTUJyM_eZOX6QgK9sElAhEwqKA6pUtJ9U0c-UNtBukEXrRwbpkk0ug4iSn5WhJRFVXhD-4HUihpJgC2ROsSwqCFe6GBUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه
#نهان
یک راهکار متن‌باز مبتنی بر Workers کلودفلر هست، که امکان راه‌اندازی کانفیگ رایگان Vless و Trojan رو بدون نیاز به سرور مجازی فراهم می‌کنه. این اسکریپت از داشبورد مدیریتی، امکان پشتیبانی از چند کاربر، ربات تلگرام، قابلیت مخفی‌سازی ترافیک و قابلیت تغییر آیپی تمیز از داخل پنل برخورداره.
👉
github.com/itsyebekhe/nahan/blob/main/README_FA.md
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/ircfspace/2425" target="_blank">📅 08:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2424">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BuTfgR6zhfdgIVdG5okzpHWkeGMqocDgFpsoiM96f7p4Vo4hiccSUl8J8QFCCo1Xu4OSRGaxuUaZAojY57FXn3ypw8RZ9leGYdXNcE4ynuOPkkfIU4zL_k7OVfHeVHWdQjT_uQpRo4fQwk4JyFQXGco6GsY5hFBlGz2-VJ5f7UZZD9uxcUlB9PrQs8qAo9PAuHYIC7NYjRecKtfnEumy-JUGMQTaUjFIX29vMJVzR8_KSZWS_e6ys3ePKm7r67AzbbecYakuYJuYyqImfhQyiJSU-dM5QnqzBljxQVGNeZ_2iJvkgn5UZ7ajuJltZkdb32v7XU9GR6yZIviQEYoVFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه موضوع حادتر از دستکاری DNSها هستش و هر روز ابعاد جدیدی ازش کشف میشه، هرچند سرقت ترافیک تعبیر درستیه. همینقدر بگم که این مساله اصلا درایت/اراده‌ی زیرساخت برای کمک به کاربران یا چیزی مثل تحریم‌شکن نیست بلکه بخشی از پروژه‌ی وایت‌لیسته، با هدف قطع مجدد اینترنت در آینده‌.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/ircfspace/2424" target="_blank">📅 07:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2423">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q2X2DSRLmlUCw3XMK_ySM_iqCwoFATba1QFcmgvWayS2zej6-U9UMLznpgmmByjjjCcC8KCYnMAYAZdXour-V0qH3X4_CoImiprmySPtm2qnnTPxuko9IcgeWuaJ7TRgy8PKz2WIRyWLPDTjfcGCVUniPNbz_eUQvC4vaguIwY2s5P2CBGhM52kHvvTgQznLaf6CP1BY8NRUiJ0-TSJ4CqrXKys6shWqzD9qX-tgEnWh9kTWWcp55LTNaCr_X6tCRH0n6Gr7OCZ263OEWKM7_W8ZmH-D4PdlZjwJYAabpJhAzCGI4oG6Vt7PIwLT8z_tOwvzq9LdUPpOHPe9hqKmMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ GenyConnect یک کلاینت متن‌باز و رایگان برای شبکه‌های خصوصی و ارتباطات رمزنگاری‌شده هست، که با تمرکز بر کارایی، حفظ حریم خصوصی و مدیریت دقیق ترافیک شبکه طراحی شده و ضمن پشتیبانی از هسته ایکس‌ری، برای اندروید، ویندوز، لینوکس و مک در دسترسه.
👉
github.com/genyleap/GenyConnect/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/ircfspace/2423" target="_blank">📅 19:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2422">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/im_Yi9xsJN0jfN0ErWwMkZQHc3BH7p-diBqeY9X3_nFufDrkBA4SeBL87mG8dhG12JJI69hXHglbYvFdP8vs0hEtdHeZ4nFKRnn8g_6ioql2MzLyw27dc71AvEJd-Mx_MJS9fQFp-8Hp42Cn3DeOmE0ZTVAEROCLKHwMMMX-Syjz2WjNxT32hPVbIt9iQ_eEDL03uYuPHbjfDAicsUQIUxXWk88uNnxIcVAbhDrWQVUonoFHwU0urE5dhErAAGPD0fLUMuGu41bEsYswuifpYLPk_1n_gw9syrIGAKeSssmfgE7XoK2eH1QtU-wkM33g9qp6r_06iy6L_LIMdpAULg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه آیفون از فیلترشکن
#شیروخورشید
با نام AzadiTunnel در اپ‌استور منتشر شد.
👉
apps.apple.com/ca/app/azaditunnel/id6776486891
💡
github.com/polamgh/AzadiTunnel/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/ircfspace/2422" target="_blank">📅 18:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2421">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FRcVpnTgEWVh9BVYH63DYZ2qbC9PSTniLFbGlr9uZ-Ev9IP9oEQBfTZM1d8_lUtsCpLA82HKBM3FkVj3J15Bt2LWdw4GXMZr6ohnb-06vn1GzB4dufvhIWToX06w4sPR239BRTKmU3M1yrRE9zU23JaxmYmBID3wgYMu_Y0D7B698pSvhgN_13ZEZnmFP47UrBFk7uFsyqbLi8KbBwQfVuM1A1sAa9IKPRB638xFbkyQEIyX_McFlGDYMQltG2ltgA4MuzGAXTaCmxGTAtkmlDHebvR4vvjTaG1xELY6W63IpCOEuug5R6wDxTyLlSt-dppHGvIe4cQxLXjG0G0KRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آپدیت جدید از فیلترشکن
#دیفیکس
که برای اندروید، آیفون و ویندوز روی استورها در دسترسه، قابلیت Health Monitor به بخش ترجیحات اضافه شده. این قابلیت بصورت دوره‌ای وضعیت اتصال رو بررسی می‌کنه و اگر کانفیگ فعلی از دسترس خارج بشه یا کیفیت مناسبی نداشته باشه، برای اتصال به یک کانفیگ جدید تلاش می‌کنه.
اینطور که تیم توسعه‌ش گفتن این ویژگی از قبل در هسته برنامه وجود داشته، اما به‌دلیل اختلال‌های شدید و ناپایداری اینترنت در ایران، گاهی قطعی‌های موقت شبکه رو به اشتباه به‌عنوان خرابی کانفیگ تشخیص می‌داد و باعث میشد اتصال کاربران پس از مدت‌ها تلاش، مدام قطع و وصل بشه. الان استفاده ازش اختیاری شده و میشه فقط درصورت نیاز فعالش کرد.
👉
defyxvpn.com/download
💡
t.me/PersianGithubMirror/5927
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/ircfspace/2421" target="_blank">📅 23:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2420">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مرکز ملی فضای مجازی اعتراف کرده که "از منظر فنی، قطع یا محدودسازی دسترسی عمومی به اینترنت، به‌تنهایی مانع اجرای عملیات سایبری پیشرفته از سوی بازیگران دارای توان تخصصی، زیرساخت مستقل و سطح دسترسی بالا نمی‌شود. این دسته از بازیگران، با بهره‌گیری از مسیرهای ارتباطی اختصاصی، لینک‌های مستقل و زیرساخت‌های غیرمتعارف، قابلیت تداوم عملیات خود را حفظ می‌کنند".
این مرکز اضافه کرده "به‌عنوان نمونه، حملات مشاهده‌شده علیه برخی سامانه‌های بانکی نشان داد که محدودیت دسترسی عمومی، لزوماً به معنای انسداد کامل مسیرهای نفوذ به زیرساخت‌های حساس نیست. بر اساس بررسی‌های فنی و ارزیابی‌های عملیاتی انجام‌شده، تأکید می‌شود که اقدام قطع یا محدودسازی دسترسی عمومی به اینترنت در شکل اجرایی اخیر، تأثیر معناداری بر خنثی‌سازی حملات سایبری پیشرفته نداشته است".
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/ircfspace/2420" target="_blank">📅 23:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2419">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دسترسی به چند سرویس تحریمی مثل اسپاتیفای، گراک، کلاد و ... ربطی به آتش‌بس، توافق و رفع تحریم‌ها نداره و مربوط میشه به دستکاری شبکه توسط فیلترچی و عبور ترافیک از شبکه آذربایجان!
©
DigiHubAI
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/ircfspace/2419" target="_blank">📅 22:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2418">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">محققان امنیت سایبری یک آسیب‌پذیری در Visual Studio Code کشف کرده‌اند که به مهاجمان امکان می‌دهد توکن احراز هویت گیت‌هاب (GitHub OAuth token) کاربران را به سرقت ببرند. تنها با کلیک روی یک لینک، مهاجم می‌تواند توکنی را بدزدد که دسترسی کامل به تمام مخازن کد کاربر، از جمله مخازن خصوصی، را فراهم می‌کند. این آسیب‌پذیری از طریق سوءاستفاده از مکانیزم انتقال پیام میان پنجره اصلی VS Code و نماهای وب عمل می‌کند و به مهاجم اجازه می‌دهد افزونه‌های مخرب نصب کرده و توکن OAuth ارسال‌شده به سرویس
GitHub.dev
را استخراج نماید.
این حمله همچنین از قابلیتی به نام «افزونه‌های محلی فضای کاری» در VS Code بهره می‌برد که نصب افزونه را بدون نمایش هیچ هشدار اعتماد اضافی ممکن می‌سازد و بدین ترتیب بررسی اعتماد ناشر را دور می‌زند. گفتنی است این آسیب‌پذیری در دوم ژوئن ۲۰۲۶ به گیت‌هاب گزارش شد و تنها یک ساعت پس از آن جزئیاتش به‌صورت عمومی منتشر گردید. مایکروسافت این آسیب‌پذیری را تأیید کرده و اعلام نموده در حال توسعه یک وصله امنیتی (fix) است، همچنین تصریح کرد که این مشکل نسخه دسکتاپ VS Code را تحت تأثیر قرار نمی‌دهد.
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/ircfspace/2418" target="_blank">📅 22:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2417">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ipdjRBrnq-XKe-ipDmzvcMr-sS2UrlX9L_AojERkwS7CZTj2oi8huROVDmdfVLiEEFfDNwWIrLLfsU9lj8reT2RR49M4UYi4AnTzklw1A54XcNRRtGa4C5qpOWY7lXgOv7OUz8LfQ6u288KTzU_qmUmUg2EwE_uEqU5rlUKhr6-6rjn2RGLgPctAbgrOFx8scj0pShLduszpETELVuWOkRgTz3oY6bWWfrNBIxHJyKCx8XUlwIMYiKjD56X820ZJBTd1qqjqhysjF8mUUnEdv3dxvV0unhe3SnfvJTtoGkKe0rrH6_97tTuxVK4CX2hW51y0VBxDeyFtJFl73u0bgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر RKh CFS یک ابزار رایگان و متن‌باز برای پیدا کردن آیپی‌های تمیز کلودفلر هست، که از IP تکی و CIDR پشتیبانی می‌کنه و در نهایت نتایج رو بصورت رتبه‌بندی‌شده برمیگردونه.
👉
github.com/rezakhosh78/RKh-CF-Scanner/releases/tag/v0.1.4
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/ircfspace/2417" target="_blank">📅 08:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2416">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">صرافی‌های دیجیتال نوبیتکس، بیت‌پین، رمزینکس و والکس به دلیل دور زدن تحریم‌ها و انتقال ثروت به خارج از کشور، توسط وزارت خزانه‌داری آمریکا در فهرست تحریم‌ها قرار گرفتند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/ircfspace/2416" target="_blank">📅 08:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2415">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بامداد امروز سیگنال تمام اپراتورهای تلفن همراه و همچنین تمام سرویس‌دهندگان اینترنت خانگی بصورت همزمان در شیراز و چند شهر دیگر استان فارس، همچنین شهرهای خط ساحلی جنوب کشور در حدود ساعت ۲ صبح به مدت تقریباً ۲۰ دقیقه “کاملاً قطع” شد. به عبارت دیگر هیچ دستگاه تلفن همراهی آنتن نداشت، هیچ وای‌فایی متصل نبود و هیچ امکانی برای ارتباط حتی با شماره‌های اضطراری میسر نبود.
قطع برنامه‌ریزی شده جهت یک اقدام امنیتی، تست زیرساخت، حمله گسترده سایبری یا مسائل مرتبط به جنگ الکترونیک؛ مشخص نیست در آن ۲۰ دقیقه چه رخ داد!
©
iliahashemicom
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/ircfspace/2415" target="_blank">📅 08:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2414">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TSoMdKTOXDSn1hseh5qVgEM7KMSqWbsXsBPf7jutICyc8Tjzmf3BDUsn9QojTsaQT5gDgO5txQRD0Nv6sVtaSOIO5BO1amcjfbNAtFjfi7jZHgz_A84ej9PCHQtAGGK61vPut6MKVT6jWoyc8WR_h6r_fXRlSTMLBPj6fDmbPsFuo7sjrunQ93Sob2FNVnSQF29kDtmQ9WWJdwY9RpG5ozNQHRE-bTmmDJCWdXOvNLMlnHhnLUfhi9ACkd_2j2vkOLhrhxzgFv6bMayxwyjBLQSDp-FMmKOtc8UwhG2nr6IZevykHWFpChmYFB7R7GYclch8Og576gpx1YO_bax_tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در نسخه ۳ از اپ متن‌باز و رایگان OnionHop که برای ویندوز، لینوکس و مک منتشر شده، موتور اتصال برنامه کاملاً بازنویسی شده و با قابلیت Smart Connect می‌تونه بصورت هوشمند بهترین روش اتصال رو با توجه به شرایط شبکه و میزان فیلترینگ انتخاب کنه.
این فیلترشکن از روش‌های مختلف دور زدن سانسور مثل Obfs4، Snowflake، WebTunnel، Conjure، Meek و DNSTT پشتیبانی می‌کنه و یه اسکنر داخلی هم داره که میتونه Bridgeهای سالم و قابل دسترس رو پیدا کنه.
👉
github.com/center2055/OnionHop/releases
💡
t.me/PersianGithubMirror/5793
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/ircfspace/2414" target="_blank">📅 08:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2413">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EtgHakM2hc2xa_Re62liEQk-9pF7w8TSNVaFgkofvM2ycUiYo6jNJgE8c02dYxhjopslfR9blYUNg4aYaWFw_Zc7bXI-l9JZCHIg4MAO7sCpdd5-q7zLa4PmoMXhZ_DrGw8R1W8q8yZkRNQ8yA6wErKWYJ7AydX-tWHDDThnDbxtAsnVT-DOF969PDJsNX3HNdaN4kSqZHeFrsZd3qUrquVKXl2MFsG_98N41h94GXPqPlsN8eBNY_i1XCiVK_qIWD39Sp_53bP6bWBOP77NDSLOt0eQrxIV6Hj73xskkeym9Q1l0N951lZY1JuL8PiUi9gvnd2FfTtOq1fIP3XkUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظرسنجی جاب‌ویژن درباره تاثیر جنگ (و البته بحران قطع سراسری اینترنت) بر کارجویان نشون میده ۵۲ درصد از پاسخ‌دهندگان اعلام کردن که شغل خودشون رو از دست دادن و حالا به‌ دنبال یافتن فرصت شغلی جدید هستن. این آمار همچنین میگه نیمی از اونها برای تامین هزینه‌های ضروری با مشکل جدی مواجهن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2413" target="_blank">📅 07:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2412">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بر اساس گزارش‌های دریافتی، اینترنت بین‌الملل در برخی دیتاسنترهای کشور مجدداً برقرار شده است.
با این حال همزمان محدودیت روی بسیاری از تانل‌ها و پروتکل‌های ارتباطی ادامه دارد و بخش قابل توجهی از این روش‌ها از دسترس خارج شده یا با اختلال و ناپایداری شدید مواجه شده‌اند. ارتباط از خارج به داخل کشور نیز همچنان با اختلال همراه است و بسیاری از سرویس‌ها و مسیرهای وابسته هنوز به‌طور کامل در دسترس قرار نگرفته‌اند.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/ircfspace/2412" target="_blank">📅 07:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2411">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گروه Void Verge در تازه‌ترین
#گزارش
خود اعلام کرده: از زمانی که اینترنت ایران دوباره توسط دولت بازگشایی شده، تغییرات گسترده‌ای در شبکه داخلی کشور درحال انجام است. پس از هفته‌ها قطعی و محدودیت، تقریباً تمام روش‌هایی که در آن دوره مورد استفاده قرار می‌گرفتند مستندسازی شده و به دست نهادهای مسئول رسیده‌اند. سیستم فیلترینگ خود را برای مرحله بعدی اختلال‌ها و قطعی‌ها آماده می‌کند و روش‌هایی مانند DNS Tunneling، MITM و Domain Fronting به احتمال زیاد در قطعی‌های آینده دیگر کارایی گذشته را نخواهند داشت.
علاوه بر این، نهادهای مسئول فیلترینگ اقدامات گسترده‌ای برای ایجاد ارائه‌دهندگان واسط انجام داده‌اند؛ سرویس‌هایی که خدمات خارجی را با محدودیت‌های شدید در اختیار کاربران ایرانی قرار می‌دهند یا وب‌سایت‌های ضروری را که امکان استفاده از روش‌های قبلی را ندارند، از طریق NAT در دسترس قرار می‌دهند. در چنین شرایطی، انتشار عمومی و علنی روش‌ها نتیجه‌ای جز آسان‌تر کردن کار نهادهای فیلترینگ ندارد. این سازوکارها باید دور از توجه، به‌صورت کلوزسورس و کم‌سروصدا فعالیت کنند.
در همین حال، مافیای اینترنت در ایران بیش از گذشته قدرت گرفته است؛ مافیایی متشکل از افرادی با دسترسی به «اینترنت سفید»، برخی ISPها و مراکز داده که از طریق سازوکارهایی مانند سرویس‌های پروکسی و سرورهای اختصاصی مجهز به NAT، اینترنت نامحدود را با قیمت‌هایی در حد صدها میلیون تومان به فروشندگان VPN عرضه می‌کنند. این مافیا آن‌قدر قدرتمند شده که توانسته بر سیاست‌گذاری‌ها نیز اثر بگذارد و حتی در شرایط بحرانی و دوران جنگی هفته‌های گذشته، به حفظ هرچه بیشتر محدودیت‌های اینترنتی کمک کند تا منافع اقتصادی خود را حفظ و افزایش دهد.
برخی شرکت‌های ساده میزبانی وب در ایران تنها طی دو ماه قطعی اینترنت، به فروشندگان بزرگ VPN با درآمدهای بسیار بالا تبدیل شده‌اند. ما در هفته‌های آینده به جمع‌آوری و انتشار اطلاعات و داده‌های لازم ادامه خواهیم داد. اگر این روند ادامه پیدا کند، هدف بعدی باید مقابله با مافیای اینترنت در ایران باشد. امیدواریم این روزهای سخت برای همه ایرانیان به پایان برسد. آسیبی که از سوی دشمنان داخلی و افرادی که زیر سایه جنگ از مردم سوءاستفاده می‌کنند به جامعه وارد می‌شود، گاهی از خود جنگ نیز دردناک‌تر است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/ircfspace/2411" target="_blank">📅 07:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2410">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وضعیت قطع اینترنت طوری شده که همدستان فیلترچی که روزی روزگاری با هم عکس یادگاری میگرفتن هم به شکایت رسیدن.
یک سیستم فاسد همیشه به سمت فساد بیشتر میل میکنه؛ در ادبیات فنی بهش میگن فیدبک مثبت. یعنی سیستم هی فساد خودش رو تشدید میکنه و در این مسیر بیشتر و بیشتر از آگاهی تهی میشه.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/ircfspace/2410" target="_blank">📅 19:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2409">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L8QSkbWBaR86c7_qH7CB4HYBTSRph8G2AdgJYnJutvtkEYBofQijhvZSFaUsYEcqOodJF5ljZzLwQkE22UCwXN02OnJj5WAlTDWwaLvTWtwnXwH2dLSoaH7zA6bEU5xdmakmexc-Oa6AFROzdKPIzanl_ynYQWTv0a_lUV2R9YHhqqPreb_3TRkrsd06F0GZ6P2r2EM86tF6iEAGEswNGRIngtIP2fipM4ZA1cCOOBEjqBcBbe7egj3AXwQb8XcSpyKRc3-30eL2IHB_6mYPkFgfC-Qp5Iao_VpCR5vUbV7l4v3GNw6AWbCeWy4U90RCgnfhHWqrk9oMgwe8rw4y6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صالح اسکندری، عضو مؤسس و عضو شورای مرکزی شریان، در خبرگزاری فارس کمپینی با عنوان «گزینه قطع داوطلبانه دسترسی به اینترنت بین‌الملل را فعال کنید» راه‌اندازی کرده است. این کمپین طی پنج روز گذشته تنها حدود ۳۴۰ حامی جذب کرده است.
در حالی که میلیون‌ها ایرانی برای کار، آموزش و ارتباطات به اینترنت جهانی وابسته‌اند، ترویج ایده قطع اینترنت بین‌الملل بیشتر از آنکه همسو با نیاز مردم باشد، نشان‌دهنده فاصله طراحان چنین طرح‌هایی با واقعیت زندگی شهروندان است.
©
alirezaer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/ircfspace/2409" target="_blank">📅 19:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2408">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oAk-udOTHvH-jomh-Rf1C-AGbRB3JGnVRIO_6Rf35vBFgdiPIqOLXGHcq80IVKkB1HqMfDSUvuWaMREW2J35DBB8JHYFZOfF0op8_L4-MEZugM_1oA6zHbWcRPIm69zBt1wG5cKT21-n-2DndeHBefS2I4UptCWdz7QmjVUg8OZ6n3Q3ovvBEg3uHu0rS9OS-ZWtOlFwAUsUXB17oDAGwAgsRCwYa-ZQR4YRH5ZMT5MkDu5RWYigkaICJJmiGTSwRbC4ifdEMBAm9jGNJsdjxskGiAltRcF2jnlLegtud_NIWsVsUCOWelktNLMLWj532yRDV89g7eQMmnBtRHMvCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ SenPai Scanner یک ابزار متن‌باز برای پیدا کردن IPهای مناسب کلودفلر در ویندوز، لینوکس و مک هست، که با تست عمیق از بین هزاران آیپی مربوط به محدوده‌های رسمی، اون‌هایی رو پیدا می‌کنه که هم پایدارتر هستن و هم کمترین تأخیر و مشکل ارتباطی رو دارن؛ تا بشه در کانفیگ‌های واقعی ازشون استفاده کرد.
👉
github.com/MatinSenPai/SenPaiScanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2408" target="_blank">📅 12:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2407">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dVVN6_7K6R54wxYe27lV6nvC9gCtj7hsZ_OtKhUjSSdio9kE1nPGifG0Z1juq6muMnyww_6cg64IVha4luUxczk0XXkQvAochQwrXnmwzQJUqJCdfjGNSkb25Mcbrho41wnHKhWO46QAAcUqBkX92bH4SPrFlf4OA_cTf6f-H6ryJI_hbEK6Hh6BoMaPXH3zjHwXZrDY1-9uGVTLGfF6vhUdiDYv0JyR_q68D-4E13SBZtOVqlT0xSLU-15jAC0YxMCjDbEtm7TwaEM1XJWrXKpsUq-FXLWGjOAYwzpVDwFWfU6Z0IqQ1pO5PdqKHxl-Kq_yLwa0zHH3EGLrZJaFaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ SpoofGUI یک نسخه گرافیکی برای SNI-Spoofing در ویندوز هست، که از هسته‌های Xray و Sing-box برای مدیریت ترافیک خروجی استفاده می‌کنه. این ابزار در اصل برای اجرای یک مکانیزم محلی SNI Spoofing طراحی شده که به کمک اون می‌تونه مسیر ارتباطی بعضی از درخواست‌هارو به شکل کنترل‌شده دستکاری کنه.
در این برنامه کاربر می‌تونه فرآیند SNI Spoofing رو فعال یا متوقف کنه و وضعیت اتصال‌هارو به صورت زنده ببینه. همچنین امکان مدیریت چندین پروفایل مختلف برای Spoofing وجود داره، که در هرکدوم میشه تنظیماتی مثل آدرس و پورت اتصال، IP مقصد و حتی SNI جعلی رو تعریف کرد و در نهایت بین اون‌ها سوییچ کرد.
👉
github.com/ZethRise/SpoofGUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2407" target="_blank">📅 12:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2406">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FbUF09sxbVrN4pWrEmTUERuR5Ce4k7Uxs5cGnzQOwp25Ye1GIWmU_C9aMWMedPJQTi1kckiul4sqDadG9S86epWhHGUcmS08uCdh7HOOP0y1Q9iGYgmAhXs290jZ7a2vBxh0Z50IK9MH00MmOkcTQgRLrVsB9FGYcdoNUKyEW8j9Gp1SvFafDobrQdAX-2oHs8smjQc90kofE7UamsOkM9NBtgOYa22utwflEOWnV8XCnvSaUKLM3lqZcGzYvsH1Qoljnf9yPRLfNhMXmXfgVnF_A0SlGLAhW3fx6w1HYapG5wTd48CrnVmmpWRHs5Fksv5Qf4_dDZ0XRa_jR81Q5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر CrimsonCF یک وب‌اپ برای اسکن سریع IPهای کلودفلر هست، که آیپی‌هارو با L4 TCP Handshake روی لوکال تست می‌کنه و خروجی‌های آماده برای Xray, sing-box, Clash میسازه ...
👉
github.com/amir0zx/CrimsonCF/blob/main/README.fa.md
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/ircfspace/2406" target="_blank">📅 12:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2405">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IipndyvCCjv7DDrM-CNDg7VHglgO4Xq8mznHBMNmGVjBUO0jir6AW_iwiOVkSYWVQETfbGR9ExtSrc12CiaT1BNyjWrAzzk7rgiWYgWjMe5HMgyk0JUavEzhw8jJ5nlbWODxID9WwDyXRBTpNE_EAxmRi-w6-xfZsdNRn_mioSdzDdswDpJmwRXg-55p3cp6EFRe6Ma2mMzBMmyWlCW7rZZeAyhCrrtAr7ci1hfvpTvVw-oohwCB3PDPnuQFZTTQTfvpnNvS7lmdibBlMDrI6oNeqRES6mCe1j5bMq4uzNukuEbwijMU4wq2cu7uOPGhz7Fqbt_JjxHm3b4kJ0FQzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتماد به نفس اگه اپلیکیشن بود
©
mansheyeh
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/ircfspace/2405" target="_blank">📅 10:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2404">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اینترنت صرفا برای توقف روزشمار نت‌بلاکس وصل شده، یا هدفتون برقراری ارتباط بوده؟
چون با هرکی صحبت می‌کنم تقریبا ارتباط پایدار نداره ...
©
ArashNalchegar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/ircfspace/2404" target="_blank">📅 19:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2403">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اینترنت در ایران آزاد و عادی نشده. بیشتر مسیرهای خارجی یا بسته‌اند یا نیمه‌بازند. فقط بعضی مقاصد و مسیرهای خاص اجازه عبور دارند. همین باعث شده فیلترشکن‌های معمولی خوب کار نکنند.
در این میون بعضی از افرادی که دامنه‌ها و مسیرهای سفیدشده دارند، دسترسی می‌فروشند. نتیجه‌اش هم شده اینترنت نابرابر، رانتی و پر از راه‌حل‌های موقت. انگار که درب ساختمون رو کمی باز گذاشته باشن که هوا بیاد، اما اجازه ندن کسی ازش رد بشه.
برای همینه که گوشیتون ممکنه نشون بده که اینترنت دارید، حتی شاید اولش سایت یا اپ مورد نظر رو باز کنه یا بهش واکنش نشون بده، اما در عمل از اینترنت خبری نیست.
©
nimaclick
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/ircfspace/2403" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2402">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تقریبا اکثر IPهای خارجی خاکستری هستند، یعنی در هر کانکشن شما مجاز هستید حداکثر ۶ پکت به سمت سرور خارجی بفرستید؛ این محدودیت به شدت سختگیرانه است و تقریبا هیچ سرویسی نمیتواند با این محدودیت کار کند. به طور مثال برای کانکشن‌های Https صرفا میتوان یک ریسپانس ساده Http را دریافت کرد و  شما حتی نمی‌توانید درخواست دیگری بفرستید.
برای بعضی از IPهای خارجی خاکستری مثل IPهای CDNها و ...، SNIهای محدودی سفید شده، یعنی اگر شما یک درخواست TLS با یک SNI سفید به یک IP خاکستری ارسال کنید، آن کانکشن سفید میشود و می‌توانید به صورت نامحدود پکت ارسال کنید! به طور مثال با اینکه الان تمام IPهای کلودفلر خاکستری هستند، ولی اگر شما یک درخواست با SNI سفیدی مثل
www.speedtest.net
ارسال کنید، کانکشن سفید شده و محدودیت ۶ پکت برداشته میشود.
در حال حاضر SNIهای سفید به صورت وایت‌لیست بسیار محدود هستند. با وجود میلیون‌ها وبسایت میتوان گفت عملا اینترنت همچنان قطع است و صرفا دسترسی به سرویسهای خاصی امکان پذیر است. حکومت برای بهبود کیفیت اینترنت مجبور است بسیاری از دامنه‌ها را بدون بررسی دقیق به لیست وایت‌لیست اضافه کند؛ به طور مثال الان تمام دامنه‌هایی که در لیست نیم‌بها ثبت شده‌اند همگی سفید هستند. نکته‌ی قابل تامل این است که اکثر این دامنه‌ها را فیلترشکن فروشها ثبت کرده‌اند (زیرا قبلا شما می‌توانستید صرفا با بالا آوردن یک وبسایت فیک و ثبت درخواست، دامنه خود را در لیست نیم‌بها ثبت کنید). بنابراین فیلترشکن فروش هایی که دامنه‌شان را در لیست نیم‌بها ثبت کرده‌اند حالا دارند سود خوبی به جیب می‌زنند.
این سیاست‌های بستن و وایت‌لیست کردن اینترنت موجب رانت و فساد زیادی شده و شک نکنید که خشم خدا را در بر خواهد داشت.
تکنیک SNI Spoofing باعث میشود که یک SNI فیک توسط فایروال دیده شود و کانکشن سفید شود و محدودیت ۶ پکت ارسال برداشته شود. روش اولی که منتشر شد اکنون در بسیاری از نت‌ها بسته شده (یعنی فایروال SNI اصلی را می‌بیند)، ولی طبق گزارشات همچنان بر روی ایرانسل و بسیاری از مناطق حاشیه‌ای برقرار است. روش دیگری که آن را Plan B نامیده‌ام، دیروز (با تشکر از دوستانی که نکات فنی خوبی را متذکر شدند و باعث جرقه ایده جدید شدند) با موفقیت تست شد، ولی به ۳ دلیل فعلا قصد انتشار ندارم؛ اول اینکه بسیاری از فیلترشکن‌های رایگان اکنون وصل میشوند (به طور مثال سایفون به راحتی با فستلی وصل میشود)، دوم اینکه همانطور که گفتم روش اول همچنان بر روی ایرانسل و بسیاری از مناطق فعال است، و سوم اینکه بسیاری از سرویس‌ها مثل اینستاگرام، واتس‌اپ، یوتیوب و ... به طور مستقیم با MITM در دسترس هستند.
©
patterniha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2402" target="_blank">📅 19:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2401">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اینترنت در یکی از بحرانی‌ترین وضعیت‌های خود قرار دارد!
اکنون وضعیت اینترنت در کشور به یکی از عجیب‌ترین و ناپایدارترین حالت‌های خود رسیده است. در حالی که بخشی از اینترنت بین‌الملل برای کاربران خانگی و شخصی برقرار شده، اینترنت دیتاسنترها که بخش اصلی زیرساخت کشور و میزبان بسیاری از سرویس‌ها هستند همچنان با اختلال و قطعی گسترده مواجه است. همزمان بسیاری از VPNها از کار افتاده‌اند و شرایط اتصال نسبت به زمانی که اینترنت کاملاً ملی شده بود، برای بخش زیادی از کاربران حتی دشوارتر و بی‌ثبات‌تر شده است.
کاهش شدید پهنای باند و افت محسوس کیفیت اتصال باعث شده دسترسی به سرویس‌های خارجی و حتی داخلی با اختلال و کندی همراه باشد. از سوی دیگر، گزارش‌هایی از بروز مشکل در گواهی SSL برخی سایت‌های مهم و حتی سرویس‌های دولتی منتشر شده؛ موضوعی که می‌تواند امنیت اطلاعات کاربران را تحت تأثیر قرار دهد. همان‌طور که قطع اینترنت فوری انجام شد، وصل شدن آن هم می‌تواند فوری باشد؛ اما فعلاً روند بازگشت به‌شکل قطره‌چکانی پیش می‌رود و همچنان بخش زیادی از کاربران و سرویس‌ها درگیر محدودیت‌ها هستند.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/ircfspace/2401" target="_blank">📅 19:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2400">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">توی یک لحظه دسترسی مردم رو قطع میکنن، بعد میخوان به همون فیلترنت سابق برگردونن میگن این روند تدریجیه!
مشت‌مشت خاک بر سرتون.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/ircfspace/2400" target="_blank">📅 15:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2399">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RI4DeQHyzyEi6s-hR5gACaw-w4mWGCanp-tIr8uVgk0_CrmSgjQ7b4OpNMG0jDsp51pvvdCy4KcPPJaYPeiS0f7GPDJ94yMKNBfGPYUx4M9SZLKoFIBZg_vfid0GBumpLvJTaK5Toi0_kaFYTDYG245erLoxETDb1nsE640hWH1bASHuEnss3ORgG7FIPkKKvoVMG9APE5tggBQmSIF923URNC-rQCwC2ixZjWk8vsgbXHB4GoIoD401mllvXCBFY8K9ZqqFgrsP1txX6AUpGxlkENsaRFpOYEDgDIXHCoINBXqf1KNSySjuUjpszDypQN7rck6AG9lfDCTiUe6mZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جدیدترین بروزرسانی از فیلترشکن رایگان و متن‌باز
#دیفیکس
فرایند دریافت کانفیگ از API بهبود داده شده، متد CDN Fronting رو به‌همراه اسکنر داخلی به بخش روش‌های اتصال اضطراری در قسمت ترجیحات اضافه کردن و همچنین روی بهبود عملکرد، افزایش پایداری و رفع چندین مشکل گزارش‌شده در نسخه‌های اندروید، آیفون و ویندوز تمرکز داشتن.
👉
defyxvpn.com/download
💡
t.me/PersianGithubMirror/5676
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/ircfspace/2399" target="_blank">📅 10:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2398">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ej4jiPP3zL5O3IDTLYNKV6n5TZLxGD1YDV_pLD34am3CaPtSYE66FA5Aqw32DICj2EKv3eTeUGAYKM6DteqycKtWDLPZxqTQE1LWfos72ML_0XaIaGa1yi_77NbjzGASMXaXd7fiqka1NhULhEt14kdhpCnB5Z6VWIVIrlCPkpQRmZe6OUkC-d_0C_uC1T9E0u_zZFNAy_KW6Viddy7TVQ-BpXpGfvb2xN1rqTwFtRgXypPSXRoJPv8pbrib1KUwjuP4BhZG5O71kTSLAXlWt5RIp3a4dcklpDRXn2ItBdEzCZHfceUhAGHshm4TZq6pIcUo3aVy_idoQ5hSpJioiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در بروزرسانی جدید از کلاینت NexaTunnel امکان پشتیبانی از کانفیگ‌‌های Xray در کنار Stormdns, SSH over VPN, WhiteDNS برای iOS فراهم شده.
👉
apps.apple.com/us/app/nexatunnel/id6766783641
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/ircfspace/2398" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2397">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رئیس کمیسیون تحول، نوآوری و بهره‌وری اتاق بازرگانی تهران گفت: خسارتی که کسب و کار‌ها و به‌ویژه فعالان حوزه اقتصاد دیجیتال در این مدت متحمل شدند، اصلا قابل جبران نیست. /ایلنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/ircfspace/2397" target="_blank">📅 19:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2396">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این اینترنتی که وصل شده داره نمی‌اینترنته ...
©
okhtapoos80
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/ircfspace/2396" target="_blank">📅 19:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2395">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jXouXv9-oc91OORkEvleIlU5BOCIbUc2m6lAggxcdvO05idYyHoW_a8cHV-XlQTw46OZMH7wsPSu5zhRV0N9rhl50xGGt6QLIiK_-TYZ42yWvYJ-FZQFkQ3DPH1ZqURKnw7lZRqCSrBYeHMx5E4FWhAExbNZAMK352WxwSjWWQ5_2nNpqv9s3Im0U7FYYwboUxNmRmPEzWMJ2CHzIjrB22hVI3NtqdS_PjZEe2F1-bTnh6rJl8EpCvwCkCyS-HHd1pGJx8dJGB05jQ8ysvRwdsD1mI2vhPW9N2Sdb82R-OdkC1u_Op6_tx1GLGEdSf8HvOZIDHYjDXvcyaEC5ZWGxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمانی که اینترنت در ایران قطع بود و تیم رسول جلیلی موفق به مسدودسازی Signature وارپ شد، اپ رسمی کلودفلر بروزرسانی جدیدی داد که حتی رابط کاربریشم تغییر کرد. آپدیت جدید این برنامه الان روی بعضی از سرویس‌دهنده‌ها داره کار میکنه، هرچند امیدی نیست که در محدودیت‌های شدید بعدی دووم بیاره.
برنامه‌هایی مثل Oblivion که بر پایه وارپ کار میکنن هم تا زمانی‌که هسته‌های وارپ‌پلاس یا وی‌وارپ بروزرسانی نشن، کار خاصی ازشون برنمیاد.
👉
one.one.one.one
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/ircfspace/2395" target="_blank">📅 08:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2394">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بعد از وصل فیلترنت یا همون اختلال‌نت، اکثر VPNهای متن‌باز و رایگان دارن به روند آپدیت‌های منظم خودشون برمیگردن. تجربه قطع کامل اینترنت در ایران احتمالا به ابتکار عمل بعضیاشون کمک کنه، تا بتونن در شرایط سخت بعدی کمک بیشتری انجام بدن. به مرور سعی می‌کنم بروزرسانی‌های جدیدشون رو اطلاع‌رسانی کنم.
👉
t.me/PersianGithubMirror
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/ircfspace/2394" target="_blank">📅 08:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2393">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دسترسی به اپ‌استور و گوگل‌پلی روی خیلی از سرویس‌دهنده‌های اینترنت باز شده. احتمالا خیلی‌هاتون دیگه حتی حوصله وب‌گردی رو نداشته باشین، ولی توصیه می‌کنم وقت بذارین و حتما برنامه‌ها و دیوایس‌هاتون رو بروزرسانی کنین. حتی سایت‌هایی که دارین (از جمله مواردی که با وردپرس بالا اومدن) نیاز به آپدیت‌های فوری دارن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/ircfspace/2393" target="_blank">📅 08:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2392">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بعد از ۸۸ روز قطعی کامل اینترنت، جمهوری اسلامی اینترنت رو وصل کرد. فقط یه مشکل ریز داره: فیلترینگ انقدر لایه‌لایه و سنگین شده که عملا فیلترنت ۲x پلاس رو باز کردن، نه اینترنت رو، و همین فیلترنت پراختلال رو به اسم بازگشت اینترنت دارن به عنوان دستاورد دولت تبلیغ می‌کنن.
بماند که جمهوری اسلامی میگه اینترنت به وضعیت قبل از دی ماه برگشته، ولی ترافیک شبکه حدود ۴۰-۵۰ درصد کمتر از  قبل از کشتار دی هست.
©
AManafii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/ircfspace/2392" target="_blank">📅 08:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2390">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">عدد ۸۸ برای چینی‌ها نماد خوش‌شانسیه، برای موزیسین‌ها نماد پیانو، برای فیلم‌بازها نماد سفر در زمان…
ولی برای ایرانی‌ها، یادآور اعتراضات سراسری سال ۸۸ بود و حالا ۸۸ روز قطع سراسری اینترنت و خاموشی‌ دیجیتال!
جمهوری اسلامی اصلاح‌پذیر نیست و بین اونها و ما دریایی از خون فاصله هست.
از فرصت استفاده کنین و دیوایس‌ها و برنامه‌هایی که دارین رو بروزرسانی کنین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/ircfspace/2390" target="_blank">📅 21:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2389">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uf4xBF4aCrIS1813PXtIH7-d6mKdFPZx0Tge61kQJUeUAVxoWedvVVYq1YyWHz-6KmjCsgZexWh3KifMZKLVVqGO_0VoCl3QvYoMH4fZv4xlTMdE3mYtcjJEh4E9YvQ8VqYhzJ2W5OqlLu8q_135ACzKLsHHSbowWrh2hT2gaiZkod3O623epkl71w1WU_m8oqw3l2CtC-zr6XByCh5JywmASaJ6OqfQ1NoXNTJNFectC4lGbEvkCxXgb5lvwEO4n4WogoG4a349sQ3cMoSz2L4rxL1SRXdnPL_WlHnyPrXkO_VFC_wBCTwZOvWbrDNVXAuGmt_HwqTLS0MjcZO82g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس تایید کرده که میزان دسترسی به اینترنت در ایران افزایش قابل توجهی پیدا کرده و به ۸۶ درصد رسیده؛ هرچند فیلترینگ به قوت خودش باقیه ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/ircfspace/2389" target="_blank">📅 21:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2388">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VrjzTx3C_IaL6yFWcFtT0I11yRJBe0tx62xQCasLOUH8lU1OskAKCVTgLXqYJR5kkNxFOjZCYmE509WlivhyB5jsG8RqUE9ii30Wbkg4MI6xauuF7vEsNnARcQrwVYaWqtqDmfbfkQMx2nFhl-HKWuHOgP1LiAOFNgJrEf_CWMM73FZbpq79IfpGsghAmWu8kZ5wVF8qMKkTpPzNWSBJoNv6x6LeDKyIPJ_RJg8S5R7os4Z3-Ez9BGpZDw1ZF_4qANFhaTTmoHgFDRWaRLlfoSlh-SU4xT-5sJuMNY1-GHwNVRG7SRdWh3HoHGCaNej_IvxfsL9Lftph2GTuqGwAzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای اینکه از وضعیت این روزهای اتصال نسبی اینترنت در ایران آگاه شوید، لطفاً نگاهی به این نمودار زمانی جامع بیندازید. ایران هنوز راه درازی در پیش دارد تا به همان سطحی از ترافیک بازگردد که قبل از ۸ ژانویه داشت.
©
nimaclick, DougMadory
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/ircfspace/2388" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2387">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CKia_CzNHd5ruh73qMRaPI6-Qucd4VubCl0FViBzX3Bzgse6MFhl98Hn1BR8tysgrrzl1IM7u8OVH2vgF0bJDcx1nz5if1JfgBXVIWEbKkxV6OThmvwBXQaueLdVQ3mYpMsDdBS3gD7ImUGeo_x0k82fH444MigMlDOlBXwfSLufTxHChUW4GR_eISV8hsnXzmex_uGwAc_66X4Jav9ktPjsSjQLMHH78_QqsIBEO38I-pVe8BcCboz6WGS9ANjHgyxT2FOXvxh0fJJOLlhxZ9msVwgzUCUbV7eKHdXtr64Qwg8HYsx8Lkcw9Fe-CgQyypRZdwq93WBTHdqV0-9IEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه‌ای از تلگرام اندروید که از طریق سایت APKPure منتشر شده، ظاهراً یک نسخه دستکاری‌شده و آلوده بوده و محقق‌ها متوجه شدن APK مربوط به نسخه ۱۲.۶.۵ امضای دیجیتال متفاوتی نسبت به نسخه رسمی تلگرام داره، که داخل اون کدی با نام DataCollector قرار داده شده و میتونه پیام‌ها، مخاطبین، فایل‌های رسانه‌ای، موقعیت مکانی و اطلاعات دیگر کاربر رو جمع‌آوری کنه. گفتن این نسخه به سرور مشکوکی در هنگ‌کنگ متصل می‌شده و داده‌ها رو به یکسری API ارسال می‌کرده!
©
vpnreviews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/ircfspace/2387" target="_blank">📅 17:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2386">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بازگشت اینترنت به وضعیت قبل از دی ۱۴۰۴ را با ذوق و شوق تیتر زده‌اند، انگار فتح‌الفتوح کرده‌اند.
کدام اینترنت؟ همان اینترنت ناقصی که UDP و QUIC و IPv6 رویش عملاً بسته بود؟ همان اینترنتی که نصف سرویس‌های مدرن دنیا باهاش درست کار نمی‌کرد؟ همان اینترنتی که برای هر کار ساده باید ده جور VPN و تونل و کلک می‌زدی؟
اسم این چیزی که شما تحویل مردم دادید «اینترنت» نیست؛ این یک شبکه دستکاری‌شده، محدود و مهندسی‌شده ا‌ست که هر روز بخشی از استانداردهای جهانی‌اش را قطع کرده‌اید. بعد تازه اگر همین شورای جدید واقعاً قدرت تصمیم‌گیری داشته باشد و فردا یک نهاد دیگر همه چیز را دوباره برنگرداند!
این‌همه خسارت به زندگی و کار مردم زدید، حالا برگشت به وضعیت نیمه‌خراب قبلی را هم دارید مثل دستاورد ملی قالب می‌کنید.
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/ircfspace/2386" target="_blank">📅 17:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2385">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VrJtXvBsdAQTa1dw9W_aF8rK-aI9AxEjARoHuGxNXwK6d5PtRZS3M4fNT8ATq22dnUi9kYCkqHGYsxs3INc88wREqzoCt3uZ0GBLzY8jyA7X15-kJpE9TKRvzpmpuTFUG_WquHidFR5y10PDnamQeozXPamSaOLKgX3vuki8jI7sFdoqzTpj2Dz8B_9ZLrHyysJVOXvTW_Y94jJl3faS85yYVsuqxPLGV9JTcVYOQyDEbnCoqa5OfwKIYCmffFWdx-oPlM2Piv4areOz6Wc9IWun-KADlEzaAY1ucEeAPbOr3aPgtUslziO8OjGLO7-W4HpYYYJBVBfUj4KVX8GITg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ فردی که در دیوان عدالت اداری نسبت به اتصال اینترنت بین‌الملل دست به شکایت زده‌اند، کامیار ثقفی، رضا تقی‌پور، رسول جلیلی و محمدحسن انتظاری بوده‌اند. /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/ircfspace/2385" target="_blank">📅 17:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2384">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d-s6fBlFX4Ah27wrKvOWN2b4whCPuT-ql2wbut-qIdnRTaIKMbjNDXQ1L7AIOrD-em8pK180vAtiHwXy4cYjDFN8VlF_sytolvt121GYAnCOfa0HMldG2SJiFgyzNQ4bbPxljQHiEH3xkJall7Qq-YDqx4NicQGJhJRRtEjd-a4JmeOjPzeUdKriVTbERlobu12rlKJzSSOX_PdHKx9WCdbXoHGzGVoNxzXK9irjpfV6ugHLrBNkKYMRA-1JTp3cRDqb_GO_8bc9bA32Iv3ufLv7z9MVmuMDm9CCl8AU_7nmTZNndCqZWYsZv2ihUXW_c56BJxfRM4XdH0OJtAl2-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: داده‌های زنده نشان می‌دهند که در روز هشتاد و هشتم از قطع سراسری اینترنت در ایران، اتصال تا حدی درحال بازگشت است. البته هنوز مشخص نیست که این بازگشت اتصال پایدار خواهد ماند، یا خیر.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/ircfspace/2384" target="_blank">📅 17:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2383">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دیوان عدالت اداری به مصوبه تشکیل ستاد ویژه ساماندهی و راهبری فضای مجازی کشور ایراد گرفته و گفته مصوبات و تصمیماتشون تا زمان رسیدگی به شکایات، قابل ترتیب‌اثر نیست.
فعلا اون نمایشی که پزشکیان و هاشمی واسه وصل فیلترنت اجرا کردن به دیوار خورد و شرایط روی ملانت باقی می‌مونه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/ircfspace/2383" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2382">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S66gp4imYaiXOfMvpWaA4PRq5aexKrR1PhTqPuHkh3ySY7jUfjJ-V6rQEjqDEOojuyY7v609DgbNarFe8PtS4s6fxVIMC3yWXbeKFP78JVA2-CDV_qRpFv9yjlDJI_NRzNtE2l22IXr5xwcv-ZRl3MFsR0Uo0OBn5u442kzXJm7DQag4x7uayHJF6IFh_xqB5NonY6NIqdiOaFZ-BdMiVoi_hla-QTDuTBRaHLyTlnlkNJplUQXMGL0IC7p3hHYVPNf0jRrQuS3vgfqnPSjc1h2c5ul6mOgECTSTvBu4Yri8surBWBNjAgsTZ_UiJMNhuWsKuqjj38fsVJ3a4eypdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها نوشتن که مسعود پزشکیان مصوبه بازگشایی اینترنت رو امضا کرده و بعد از ۸۷ روز، بزودی فرایند اتصال مردم به شرایط پیش از کشتار دی‌ماه برمیگرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/ircfspace/2382" target="_blank">📅 23:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2381">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g5MfBTIKIlCDdF2MrJsI_XjYvmtIs9omdq5xsweD1G-Rtp6QemnEyh2BwfgVaBCj7W7hrYcMUMTA5qp_5xhQj5Ne6eHTcNr9FJETNrMJZt1uWvqqbAzMz2ZLW1iKbhQvoL6CGxYYHcHwH5f3wbIdlF__mys1qknytiuqZNLZbiCtIDKnaP3z3I1OXXKwK5uL1ytXajwOTrlrQETyFk4-YTZVLRjDLzPjqLkHZmOxc8RT6YOCCDom9a3o0G2ZBVdkl_EUcVJjAa6fmRKx9R52v_4176BAdC-BPxep5yx2XnXZJvMQPOjduyldGe2l0RVi0TEWgkrekBn5NMB2Og8LWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: اکنون هشتاد و هفتمین روز متوالی قطع سراسری اینترنت در ایران است؛ محدودیتی که بیش از ۲۰۶۴ ساعت ادامه داشته. این اقدام هرگونه شفافیت درباره اعدام‌ها را از بین برده و به شرایط غیرانسانی و بلاتکلیفی روزمره‌ای که منتقدان زندانی، مخالفان و حتی گردشگران بازداشت‌شده با آن روبه‌رو هستند، دامن زده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2381" target="_blank">📅 11:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2380">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aIegb2vBgLIFoo-ZCX9vLG-j40yhQwLR8LeqRPmVQVRSlYxa1ww7YQCetcU6gToKp4iNLsZISbfJ6bVW7xWrKpU7mkDENoCR-k2veEwyoODuF9rO93cTna8CDGAoVRsdlfHZtBg4ts9L2wKiVHUFUtQ1do4qu0ApKNBeeHkVKsDmMZe8ldhUUNnk20pdwKtAu9ySJGiSe9WXu2b_ZgSjXKCekxnIpMSHt9mrRgMDplNF-eIVs0hio8c_7MkvDjqOxBNZp22v_OttdbKilB1aPUnZEvZ5MXi70oGCBg1HIdGXUGGQh6hWDN77Xv-g2HFwgovuMmT0L__kNSqOiwg1qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی آپدیت جدید از اپ متن‌باز و رایگان
#شیروخورشید
کار خاصی نیاز نیست بکنید! حالت اتصال رو روی CDN FRONTING بذارید، اگر قبلا آی‌پی و SNI ست کرده بودین، پاک کنین؛ بعد روی اتصال بزنین و برای مدتی صبر کنید تا نرم‌افزار خودش آی‌پی تمیز پیدا کنه و وصلتون کنه!
👉
github.com/shirokhorshid/shirokhorshid-android/releases/latest
💡
t.me/PersianGithubMirror/5515
©
yebekhe
آیا این برنامه امنه؟ قبلا
اینجا
توضیح دادم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/ircfspace/2380" target="_blank">📅 17:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2378">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مامانم دچار آلزایمره، از وقتی اینترنت قطع شده و نتونستیم ویدیوکال کنیم، فراموش کرده من ایران نیستم، فکر می‌کنه باهاش قهرم و نمیرم دیدنش.
©
MaryamA89323145
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/ircfspace/2378" target="_blank">📅 08:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2377">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AaafEeyY6UJSDvxVF5Q2xmMBrTyERqrQtkzWFXnfXEMqF8h7bryaZnVcsIwKur2h_y0kW0Br3xVPoFgI51gfg3VruhMBgP49n_JzALnNeymffNnSnGits2m5XhxBCdXyYgOQFLv6f_wbWr5_obYzsh0-KL-Oibl44osz49GFqQNz2lPJvolm7tQyMg2_cAMF_bb2gTjAD3Y7k9C9jqLABWkb7YYKbmRQQCes8--gruD3J0ICrfT-S9ViEpnHXunGckC_2H9jQryrdifkLndHRrUryN9gjBchpy-iqF-vi2ICTJ2K1cFCAMV0UXKCy1GnH4KpEWkAlgQHjkXweA972w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع سراسری اینترنت در ایران به روز ۸۶م رسیده و همزمان توجه رسانه‌های جریان اصلی به این موضوع داره کمتر میشه. انگار دنیا معمولاً به رنج و فاجعه‌های طولانی عادت می‌کنه؛ مخصوصاً وقتی قربانی‌ها صدایی برای دیده شدن نداشته باشن.
Iran’s nationwide internet shutdown has now reached its 86th day, while mainstream media attention to the issue continues to fade. It seems the world gradually gets used to prolonged suffering and ongoing disasters — especially when the victims have no voice powerful enough to keep themselves visible.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/ircfspace/2377" target="_blank">📅 08:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2376">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a874f4f669.mp4?token=UxvukH3rwptcp7KqwyUG0ne3peRuPKf0rP2Km8vgFWbi3zKdbUT9lxNWQ0fGlV_AwPf43QeeWtsSaw67LkZztlE1J2MVQ0ReF9tLr1lU8kROmPErxCPUONJJ1xybM3pu_ew6SVM2AVZrJWGZdoI8TCtFMohfHC1Eylkrw6ylD-BxLIwVfSiBb-R9nO1RiyoVhXfLLer0DqQrv1-Fl5OSQfWnyRL_efZy33NR4-7bSRHm7Via9cgiiw3L00iGloMk89Z7PVOHNmiIOOJSO3ooDC7kk1eJaw26coTT79lavrSK9GfGmT8V32Dd9EnMJHs2Ug5RlzW3D_BpUF3XA88w8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a874f4f669.mp4?token=UxvukH3rwptcp7KqwyUG0ne3peRuPKf0rP2Km8vgFWbi3zKdbUT9lxNWQ0fGlV_AwPf43QeeWtsSaw67LkZztlE1J2MVQ0ReF9tLr1lU8kROmPErxCPUONJJ1xybM3pu_ew6SVM2AVZrJWGZdoI8TCtFMohfHC1Eylkrw6ylD-BxLIwVfSiBb-R9nO1RiyoVhXfLLer0DqQrv1-Fl5OSQfWnyRL_efZy33NR4-7bSRHm7Via9cgiiw3L00iGloMk89Z7PVOHNmiIOOJSO3ooDC7kk1eJaw26coTT79lavrSK9GfGmT8V32Dd9EnMJHs2Ug5RlzW3D_BpUF3XA88w8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازم خداروشكر كه الحمدالله، وگرنه والا به خدا
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2376" target="_blank">📅 08:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2375">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رئیس کمیسیون تولید سازمان نظام صنفی رایانه‌ای استان تهران با انتقاد از تداوم محدودیت اینترنت گفت: پیام‌رسان‌ها و پلتفرم‌های داخلی هنوز نتوانسته‌اند نیاز کسب‌وکارها را تامین کنند و مشکلات فنی و محدودیت‌های ارتباطی همچنان پابرجاست.
حسین ریاضی اضافه کرد: راه‌اندازی اینترنت پرو و اینترنت ویژه برای برخی گروه‌ها، نشان می‌دهد که خود سیاست‌گذاران هم پذیرفته‌اند محدودیت‌های فعلی، فعالیت شرکت‌ها و کسب‌وکارها را مختل کرده است.
او با اشاره به آثار طولانی‌مدت اختلال اینترنت بر فضای کسب‌وکار افزود: ماه‌هاست درباره آسیب‌های ناشی از محدودیت اینترنت صحبت می‌شود اما هنوز مشکل به شکل اساسی حل نشده است. در عین حال، ایجاد این محدودیت برای اینترنت باعث حساسیت و نارضایتی گسترده در جامعه شده و بسیاری این وضعیت را تبعیض‌آمیز می‌دانند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2375" target="_blank">📅 08:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2374">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cyNcCQ6sZcq7-yw0A7tCHKjdWacpG8h7x-ynT0wT9AmLwCAxjbBh6UGV5fEdeOjP0X_FRqvUbBx9Yfqx__E5D2Ayzg_6ZOJ8uIoHQ4UVlfEC0sKGEGrKhAyNS_TONnAJk_v1-Uxk3bOeOKugFpL7i2SGZnnhBb2LfZsEkaW4go-T5-aZ67b3EJNfPxLDkQkrCdyoWT2F0VRpd6h1Y5yzN-OcLUj7J309PPBtoplQHNwcrGQHbUvF53vY1qMrJCiBe0fpILahkp4vKLiA28G9aNkZ5--vafQBRmQOtc9pLV2J-9Mh-QOMfLak9d7GdxwrPWw7ZGF3eQVur12S-Q55VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸۵ روز از قطع سراسری اینترنت در ایران گذشت!
قطع اینترنت در ایران، یک پروژه چندوجهی است. قطع شده تا بین "هواداران پهلوی" و "پهلوی" فاصله ایجاد شود و همزمان عده‌ای بتوانند روایت جعلی بسازند.
صدبار دیگر ایران بمباران شود، نظام با بمباران تغییر نمی‌کند؛ چیزی که جمهوری اسلامی را ساقط می‌کند، آن مردمی هستند که شعار دادند "این آخرین نبرده، پهلوی برمی‌گرده" ...
با تمام دشمنی‌ها، سرنوشت محتوم ایران محقق خواهد شد.
©
AmirHadiAnvari
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2374" target="_blank">📅 08:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2373">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tkIsm6BXPxEio4GzaINvzQYwrClbeuefPeNtUiQGkPVx2XJ9NdXdSMcluUHeKY0_IR_ESI77ZEfHkebScqEbhOKtx2qwM9Aw7BlG482DEugT-ccINvNbtnZNcBwb-BhQWsT-fkcuRL18zy32pJY1HlwbIHzlblM2ZxwxmJzLrpnI2X5bAqZT_sy-L70ERpKN3Y6fecivtrmtDTZF0cKa-Sul-FgwwSER72cOgjxXA6pbwc5H-Ji0SJ8QYbb0Lb3imzZj-5oEpMndFTMljSEr5XbVdPvBMFkg1qA2T_2REGKdBqxoxGL4LfOTO6TQAOdX1Q53lpHF5Xl9eYHF011J1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طی یک عملیات بین‌المللی، سرویس VPN موسوم به First VPN که توسط مجرمان سایبری، گروه‌های باج‌افزاری و هکرها استفاده میشد، از کار افتاده. در این عملیات بیش از ۳۳ سرور توقیف شده، دامنه‌ها و سرویس‌های Onion بسته شدن و یک مظنون در اوکراین هم بازجویی شده.
مقامات میگن این VPN در تقریباً تمام پرونده‌های بزرگ سایبری یوروپل دیده شده بود و برخلاف ادعای بدون لاگ بودن، نیروهای امنیتی به دیتابیس و اطلاعات کاربرانش دسترسی پیدا کردن و هزاران کاربر شناسایی شدن.
©
eurojust
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2373" target="_blank">📅 08:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2372">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جمعی از سازمان‌های مردم‌نهاد و فعالان حوزه حقوق کودک، با انتشار بیانیه‌ای نسبت به تداوم محدودسازی و طبقاتی‌سازی اینترنت در ایران هشدار دادند و آن را عاملی در تشدید نابرابری آموزشی و اجتماعی، به‌ویژه برای کودکان و نوجوانان دانستند.
در این بیانیه که به امضای ۱۹ نهاد رسیده، تاکید شده دسترسی آزاد و برابر به اینترنت، بخشی از حقوق بنیادین شهروندان، به‌ویژه در حوزه آموزش، دسترسی به اطلاعات و رشد فردی است. این بیانیه، با اشاره به تعهدات بین‌المللی ایران از جمله پیمان‌نامه حقوق کودک، محدودسازی اینترنت را در تضاد با این تعهدات دانسته و همچنین با اشاره به نقش اینترنت در آموزش و معیشت خانوارها، تاکید می‌کند که اختلال در دسترسی بر شرایط اقتصادی و امنیت روانی خانواده‌ها نیز اثرگذار است.
©
hra_news
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2372" target="_blank">📅 19:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2371">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W7618RUQeaYLYCa4nLMSYxKmBLxIZKZK_UOyzy39h7ColtplfLwjw4WABhL6d8dC0BnLk-WGZn6PiJ799k5aAx12_gUhtqBA0Yg-QmRaEZyY3onVKg6vVw2DyXxstyZfh-rdGTKSspqqpANjBQjQZ_JnhKBjG814M_0DIXwndK-cI1SoiTC710wr4MDYnIyhLmzIQ8jMgq7nhD0Vp97xiGClbWfA5qyr0H6D99iPyj6jzYPxUxab2HXRIdKtWRUQHSPCfqU7xL34qWsmDyRmYQEBWmt4CqW1ytArKGxW63xsOEs9BvFOlSWm3nyKVLtmGwvKWcs331vL-9TKoFPIKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران با ورود به روز هشتاد و چهارم، از ۲ هزار ساعت عبور کرد. هر ساعتی که می‌گذرد، شکاف‌های اجتماعی و اقتصادی عمیق‌تر می‌شوند؛ به‌طوری‌که هرگونه ارتباط با دنیای خارج به جایگاه، تبعیت و امتیاز وابسته شده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2371" target="_blank">📅 19:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2370">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خیلی راحت آمارسازی میکنن و میگن ۹۰ درصد مردم با قطع اینترنت مشکلی ندارن؛ به همون راحتی که احتمالا قراره تعداد ثبت‌نامی‌های سامانه
#جانفدا
از کل جمعیت ایران بیشتر بشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/ircfspace/2370" target="_blank">📅 20:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2369">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کسانی که قبلاً کانفیگ می‌خریدن، الان ترجیح میدن دیگه نخرن، دلیلش هم تکراری شدن خبرهاست. دنبال کردن مجازی دیگه اون‌قدر براشون ارزش نداره که بخوان بابت هر گیگش خدا تومن پول بدن.
از اون طرف، کسایی هم که سیم‌کارت پرو گرفتن، خیلی‌هاشون توی کسب‌وکار خودشون موندن. چون درسته اونها اینترنت دارن، ولی دیگه کسی نیست که بخواد تبلیغشون رو بخونه. تقریبا اون چرخه‌ای که باید بین محتوا، دیده شدن و فروش می‌چرخید، به بن بست خورده و کل سیستم رو از کار انداخته.
©
NR2OH
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/ircfspace/2369" target="_blank">📅 20:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2368">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MkAIEIRd6AdeeKpcpWKw6f04tA3SIL7DHKPR2FxT8Ml2QNvKmGO2C1WwFamnXX8eYhLBjUoNHZ0C44PiLprnnM0LreksuOvSmCWl28ENRh3Dv2Tn91rUb2QjdD2rMOfQNQJgTvwv3DDHxKFd736azEh9aaF6rsYG9BOVg5XQWUJy6lUR0WcVK5ArIW9P-uHEEE5tI6FFu6OppI2GeCMh8_FSnJQg6Eg3YfdYd03kRIfCxp3pdPr0noYSE-SjFM95s72JaoyH-ZjvVooWW6TYvzOsRtOKhWXQBMXx8FvtSubBrvjxyJOl8yUjQ-6UgkKZwV7Oz8_rfvfr8V48ipjtMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا فرزانگان، اقتصاددان حوزه خاورمیانه در دانشگاه فیلیپس ماربورگ آلمان، گفته است حدود ۱۰ میلیون شغل در ایران به‌طور مستقیم یا غیرمستقیم به اقتصاد دیجیتال وابسته هستند.
او به وال‌استریت ژورنال گفته محدودیت گسترده اینترنت باعث کاهش بهره‌وری، تضعیف اعتماد کسب‌وکارها و افزایش نابرابری می‌شود؛ زیرا در چنین شرایطی تنها کاربران ثروتمندتر یا افرادی که به ارتباطات بهتر دسترسی دارند، می‌توانند اتصال پایدار و قابل اتکا داشته باشند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2368" target="_blank">📅 20:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2367">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bAtUh1oXO7UTFcVGNzAX1QWqWVUmjbwGNMToDqrCkpGsqwRu3iB84_AKNXOtdnDjsaPnRUlmjNg-fVcH7T0ypzy8UcGLOqJWOJ4AmqMohB5hutR3CBWowcxnzvgTExLlrre-AwriGOER38BmK9Atr4lc7TW_yTmNryTrCF7LAJRW2Y7t1v2uCSaUS2gRNdwW5cS_W0GTlmCYcWacE_XSsIxPg8mhWknLLHsn2JGhcq8_7oB2C1_18KCjAmQs__16znocMJI-EZ3Dd_P5bQvgn8p30w8C81SkXqAy25t-z5fWISbj_2fYcqQ4hvTG-6lUOp6miYUo07rN-_GCRTrZfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زارع‌پور، وزیر قطع‌ارتباطات دولت قبل گفته "جمع‌بندی رئیسی این بود که اینترنت به خاطر هیچ‌چیز نباید قطع بشه"، ولی یادش رفته که رئیسی با ۶ کلاس سواد حتی جمع و تفریقشم افتضاح بود.
جهت یادآوری واسه
#قوه_عاقله
، اینستاگرام و واتس‌اپ توی دولت سیزدهم فیلتر شدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2367" target="_blank">📅 20:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2366">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یزدی‌خواه، نماینده طویله مجلس گفته "در شرایط فعلی تصمیمی برای بازگشایی اینترنت جهانی وجود ندارد" و "با قطع اینترنت، کسب‌وکارهای مردم از جهت ارتباطات بانکی، خرید و فروش و بسیاری از سایت‌ها همچنان در حال خدمت‌رسانی هستند و مردم مشکل عمده‌ای ندارند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2366" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2365">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FudTqUiZPt_wrcucvrKv1S9HFb-fQVL0gmpMCb-v85fhMf_IJJ68qhI753IESamewoX-3NaOLWB1QlV62xvqJ3OZ3fKsIU1L6PiD_JA8tLQ7jQAJc4ZmoNjC24iDiiIW_djVZH4Ek3JoRIQCz2zi9wsR8d0kUrCtIfpNB7VAvKq9oalwO2gz8HrbfBvBfxQYf_DVBA1V59NTXAdZCUdPLRhg_EZloiVRNmWq_coCNXrdy70Maql26galVgumLSgSY4abuhMHr8oB13AhnFsYApjm-I9u_uMlqPKjBhWo68iPDnZ7a7uaJYTNEzrgIjFF49kdCQqGWtEnfvOMW6sVsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه عاقله در همراهی با سایر قوا، قطع سراسری اینترنت در ایران رو به روز هشتاد و سوم کشوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2365" target="_blank">📅 08:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2364">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گیت‌هاب گفته دستگاه یکی از کارمنداش از طریق یک افزونه آلوده VS Code هک شده و مهاجم تونسته به تعدادی از ریپازیتوری‌های داخلی خود GitHub دسترسی پیدا کنه و اطلاعاتشون رو خارج کنه.
فعلاً میگن شواهدی از دسترسی به ریپوهای کاربران یا داده‌های مشتری‌ها پیدا نکردن و موضوع فقط مربوط به ریپوهای داخلی خود گیت‌هابه. البته دارن لاگ‌ها و میزان دسترسی مهاجم رو بررسی می‌کنن و گفتن بعد از کامل شدن تحقیقات، گزارش کامل منتشر میشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2364" target="_blank">📅 08:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2363">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عضو هیأت رئیسه مجلس: تصمیمات مربوط به اتصال اینترنت فقط با امضای رئیس‌جمهور انجام می‌شود؛ تشکیل ستادها نمایشی است.
این هم خبری دیگر درباره اینکه مسعود پزشکیان نه‌تنها مخالف قطع اینترنت نیست، بلکه در ساختار سرکوب و محدودسازی اینترنت کاملاً همراه و همسو با حاکمیت عمل می‌کند؛ تمام نمایش‌های رسانه‌ای درباره «بی‌اختیاری دولت» فقط برای فریب افکار عمومی بود.
©
alirezaer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2363" target="_blank">📅 08:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2362">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jgS46Cv4oCx6HWyxnyZVcvDh6mwrkAfHEXrLSnGDJ0s7X7WicsCucuSPEoxcxoJqZRzuj3V4-EQa0PeDOnE-zkNUt_lT6fFKxWEOfYF7kNFsY5g6ooIHJ6NJZBUqkWJfc2hzJLeOY1ClYtRrzU08jvFoLBem5Y93lknsnYEIQMEf6xCF6Zb4V4DMkL1R6-kLdKjVbC1CrnH9cbGp1OZA22qye57bJ9y-h1_L_MrBQ43ztYvF-0SMIAxi_osF-hbqTAykK8XrzSPdHz0dBS16AyJCr8Oh6oaP3pcTlYFLDCkYpFkQaqHx3yfR7b4HqHpZebyPKyeV5genpGamNyBXGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار نشون میده در ۳ ماه گذشته یک پاکسازی طبقاتی دیجیتال در ایران رخ داده. در این مدت سهم اندروید از ترافیک اینترنت ۲۵٪ افت و آیفون ۱۸۰٪ رشد داشته. این به معنی خروج میلیون‌ها کاربر طبقه متوسط و پایین از فضای آنلاینه. اونی که آیفون داره (احتمالا) از پس هزینه کانفیگ یا اینترنت پرو برمیاد، اونی که نداره، اونقدر دغدغه مالی مختلف داره که عطای اینترنت رو به لقاش می‌بخشه.
©
arashzd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2362" target="_blank">📅 08:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2361">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EKtZ9kn047cM9cjn5j0JuypNU5V4RcnsHbisgp_dV8JpzLpzQ1foaIO96i8dTzf7wfwxRkEWtQ_EZGiejJl6g-j6_yWKdOp9Y8yWf6pqJCMdXzNcir5SIBvwrw27O2rLchi00hAqs2RJPgJ2xj1MKHD7MaYEf-WQ0iI_kK5Cn7BuHcODJ1Rt1fRgSV7jWcCDOvOMzi4LKKqElGSkJGu0pJj8FLeL1ghdytgQB5l1aDcsOYSHdDUbeY6PwJqHKzumGFqP3PG2rNFaPnEimFqYbZARX_n0rFwmMLwOSVhq105vRtdxugBiZ7LGpQrgMPAr-SAp73Qz8ZAXodfBtkKEcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتاد و دومین روز از قطع سراسری اینترنت!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2361" target="_blank">📅 09:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2360">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">قطع اینترنت به خاطر تأمین امنیت، یک دروغ بزرگ است
گفته شده قطع اینترنت به خاطر تأمین امنیت زیرساختی، نرم‌افزاری و سخت‌افزاری است تا کمتر مورد حمله‌های سایبری قرار بگیریم، در حالی که این یک دروغ بزرگ است. حمله‌های سایبری و ناامنی زیرساخت هیچ ارتباطی به قطع اینترنت ندارد. متخصصان به این‌گونه دلیل‌تراشی‌ها پوزخند می‌زنند. البته نه به این معنا که زیرساخت مخابراتی ما یا زیرساخت شبکه ملی اطلاعات ما در حال حاضر امن است؛ نه، ناامنی وجود دارد، اما قطع اینترنت کمکی به تأمین امنیت زیرساخت نمی‌کند، بلکه لطمه بسیار جدی‌تری هم به امنیت زیرساخت می‌زند.
در همین مدت دو ماه و نیم گذشته ده‌ها آپدیت امنیتی برای باگ‌های «زیرو دی» یا اصطلاحاً باگ‌های روز صفر داده شده است. این‌ها باگ‌هایی هستند که می‌توانند دسترسی بسیار بالایی برای هکرها ایجاد کنند؛ روی گوشی‌های مردم، روی مودم‌ها، روی شبکه‌های صنعتی داخلی. این‌ها هیچ‌کدام آپدیت‌ها را نگرفته‌اند. آپدیت‌های ضروری‌ای که حتی یک روز به تعویق انداختنشان گاهی باعث ایجاد ناامنی می‌شود، الان بیشتر از دو ماه و نیم است که دریافت نشده‌اند و ما با یک بمب ساعتی در ناامنی زیرساخت شبکه کشور مواجهیم.
من فکر می‌کنم وقتی بحث امنیت مطرح می‌شود، بیشتر از اینکه منظور امنیت شبکه و زیرساخت باشد، منظورشان کنترل افکار عمومی و جریان آزاد اطلاعات است. اگر با این چارچوب امنیت را فهم کنیم، بنظر می‌رسد حق با این آقایان است؛ قطع اینترنت قطعاً باعث جلوگیری از جریان آزاد اطلاعات می‌شود. دلیل اینترنت پرو هم اتفاقاً همین است. اینترنت پرو نهایتاً شاید به یک یا دو میلیون نفر ارائه شود. یک یا دو میلیون نفر با ۵۰ یا ۶۰ میلیون کاربر فعال ایرانی خیلی متفاوت است و باعث می‌شود جلوی جریان آزاد اطلاعات گرفته شود و در واقع کنترل افکار عمومی و کنترل جامعه راحت‌تر شود.
چطور اینستاگرام یک پلتفرم آمریکایی است و ممکن است لوکیشن و اطلاعات مردم را در اختیار مثلاً نهادهای امنیتی آمریکا بگذارد، اما سیستم‌عامل اندروید که متعلق به گوگل است، نمی‌تواند چنین کاری کند؟ اساساً منطقی که مطرح شده، پر از اشکال است. وقتی شما اینترنت را قطع می‌کنید، عملاً یعنی تمام زیرساخت‌های رشد و توسعه یک جامعه را متوقف می‌کنید. به یک معنا، ما با این مسیر داریم گام‌به‌گام به عصر حجری نزدیک می‌شویم که در آن از فناوری اثری نبوده.
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2360" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2359">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">امروز هشتاد و یکمین روزیه که اینترنت ایران بصورت سراسری قطع شده، ولی پروپاگاندای حکومت بدون لگ داره کار می‌کنه.
امروز هشتاد و یکمین روزیه که جمهوری اسلامی داره
#روز_ارتباطات
رو با قطع اینترنت جشن می‌گیره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/ircfspace/2359" target="_blank">📅 08:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2358">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RE6xdXsHi00KPQPv0aQXyunc8W5VsTDza1V34a1pqJwLl7uTK_1jRbHJkFn7FFHZLWY5IKYF5J5u1o2VHWyfzwBLS1y_qjY30qLKJmzTbEK5_zV1YXeNq8FoHbgUJF7wpcWLSB2nqWAAa7UM5F0LR-L1m7lKThXpwYQvcXwAz0keoFj0E7x-hf7alxl7iLqNXaWuu9nHTwSPLz9NkkO8LITfOPhOYD-elOrW-yF3z14tSeHMi9mjB3x-B1Y5u5iZqW6rVZGe4mFwCvC9razPu_FHtXuBJoHe1io5MNs8ceq44BlPClWbGblIFztpLAtj-hhHn_6h-XJL-zXR8ZkJAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در بروزرسانی جدید از اپ Network Checker برای اندروید، ویندوز و لینوکس، قابلیت اسکنر آیپی Akamai (جهت استفاده در اپ
#شیروخورشید
) اضافه شده.
👉
github.com/mirarr-app/network-checker/releases/latest
💡
t.me/PersianGithubMirror/5227
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/ircfspace/2358" target="_blank">📅 08:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2357">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Af4F2MV3IhzEiG1oHRl24G0j6XVRffxcj1a4Chz9e9-PhPOtE3SKZVX_3uCi7X63ETc17XiqXOJRPjqA2qO-cyhu7GgPFhE01sX1xgE07WyQFVUOcxdcdYAEtrXJtQzQHsQ10wASj3vUxfAjrgoOoSw--SEVu1WudhDaVhxACvGHb8iQK0LKptcHptsuzfHeAsIj2sT9qWQPJ4W6N4LLGx5yBa4VpP6irWj0MOKgkir5N8tKZn1ygGeY1pyadHBJFsK6j-0c-iMu5KFRsw57cncPqCNeSspG9hPJNeMv4IBu8UQMdSQYUwdEVWSyCQwMEjFtmdcQ7ti_nbjQJL6hdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ NexaTunnel یک کلاینت رایگان برای مدیریت تانل‌های StormDNS در iOS هست، که به شما اجازه میده کانفیگ‌های مختلف رو وارد و مدیریت کنین، وضعیت اتصال و ترافیک رو بصورت زنده ببینین، DNS Resolverها رو تست کنین و خیلی راحت بین پروفایل‌های مختلف سوییچ کنین.
این برنامه با رابط کاربری ساده طراحی شده تا بتونین وضعیت تانل، سرعت دانلود و آپلود، پینگ، IP عمومی و سلامت اتصال رو بطور لحظه‌ای بررسی کنین و مدیریت بهتری روی اتصال‌هاتون داشته باشین.
👉
apps.apple.com/us/app/nexatunnel/id6766783641
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2357" target="_blank">📅 08:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2355">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">توصیه اکید من اینه که برای وصل شدن به اینترنت سعی نکنید از سرویسهای ایرانی (خصوصا سرویسهای متصل به نهادهای امنیتی) که شمارو قبلا احراز هویت هم کردن، سو استفاده کنید.
به هیچ وجه حتی برای امتحان کردن هم ارزش ریسک کردن نداره. و به هیچ وجه هم روشهای مربوطه رو معرفی یا پروموت نکنید! اگر کردید بهتره همین الان پاکش کنید. از سر دلسوزی میگم، بچه‌هایی که از چندسال پیش در ایکس فعال بودن میدونن دارم در مورد چی حرف میزنم.
©
aleskxyz
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2355" target="_blank">📅 20:07 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
