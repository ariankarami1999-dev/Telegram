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
<img src="https://cdn4.telesco.pe/file/YvpQwkNQREldzQAtgSwaqaxZ0gsUzOaPoWmu8aVjFhNAhG6jP1scntY2wqig8F7UwjOfkCYu4CWvT_ImlWIy4P0wBIyBEEPSJ7aaTLL4XeWpEkypondiyRLSad2zLp4Ybhab23pmJRNZLf_s17lF7O5xKLepyiBthM-4yI0FqDNNwqVYGR5tdcs1whQNnJiqgdV2PKpxYbJ6oPf02PvGzosiv7RzHoOCJ0Lhjhry5Fu0qBCDXWOm0wX2CyL6SyAY23bK9imliDliotoDSo00Kq1awxipRiTfpGM2xyVqBjUcpPsHK-R2Qj5ILeh4KReqmpm01_7htFFE0bVrFcPJUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.02M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 21:22:03</div>
<hr>

<div class="tg-post" id="msg-149753">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
گروه حوثی (انصارالله) تصاویری از بقایای یک پهپاد "کاریال" ساخت ترکیه را منتشر کرد که توسط عربستان سعودی مورد استفاده قرار می‌گرفت و امروز صبح در آسمان استان حجه سرنگون شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/alonews/149753" target="_blank">📅 21:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149752">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
سخنگوی نیروهای مسلح دولت تحت حمایت عربستان در یمن: در عملیات جدید نیروهای ما علیه مواضع حوثی‌ها در مرکز یمن، چهار کارشناس ارشد ایرانی متخصص در راه‌اندازی و پرتاب پهپاد و موشک در مرکز یمن ترور شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/alonews/149752" target="_blank">📅 21:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149751">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
پزشکیان: بار‌ها می‌گوییم گفت‌و‌گو می‌کنیم، تا نگویند ایران حاضر به گفت‌و‌گو نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/149751" target="_blank">📅 21:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149750">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
تلگراف: پلیس ضدتروریسم بریتانیا در حال بررسی این موضوع است که آیا تهران پشت طرح بمب‌گذاری علیه پایگاه هوایی مورد استفاده آمریکا در جنگ ایران بوده یا نه
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/149750" target="_blank">📅 20:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149749">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5MR2mrMgccog0RhRYnBgRo2_6czp0JW9zO0oat0qRfE0E0cmGsoStj1Bz9bGh_6C9mO2F4TH3Sd9vVqrTM6NnNIONbWMp2Ww875PvTX5p8CZyf-u27y0XzyD_S_7mVPLybSF5WuZ5coQGEam5JgdI6k_r7xq9dg1SSju1nATfdVKUBXhfBS-e_mu_GiahYFMkXTmYAQzcxHLD7Q-j5cWLpK3AhmZVAzsHscAoDe46_iQb1p92ZGEenWikIvPMA0LM1igYTKIveUC0zrS9X7CYnFiaiV5t77doMot1Lso21nPYHYH_Xw7sFRqBnuBgMYfvNiQr3FFtgfDxKnBs9clQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان قبل زدن زنگِ آغاز سال تحصیلی؛ یه استخاره باز کرد که انگار نتیجه خیلی جالب نبود و سَر تکون داد...
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/149749" target="_blank">📅 20:54 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149748">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0be3641b4.mp4?token=GzUYWxlGcsTj03ZRbHlC57rVYZnRAdlVD9rCJN5PcepQt3Dhp0INcoeDUxrHnSmOJlwrzqwGJxA5Q228Rjwx3uvZ7Jy9ksjoomWce_topL_ayS7t7MUnehUWykxCyMzgI_JFYN68JemMUMtQsiiMzH2r1DlzczL1MYdmKHTmsaYtjMhMt3hZDI8YDIKe2VNH5X9Z2Ilz-dvMpYHg_ZnG9edz8lAUyDE03AYyQp0fCTBBZ6zTzHeu9JMU1rNNqrvP0rPIS1PhMudBZXwD3iHdIcNMsjBSa9GixNuQdZO0LKRFiC4wI-isWoL_Zee0ht1R4QPnvEgciq-cWRBLK8FCpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0be3641b4.mp4?token=GzUYWxlGcsTj03ZRbHlC57rVYZnRAdlVD9rCJN5PcepQt3Dhp0INcoeDUxrHnSmOJlwrzqwGJxA5Q228Rjwx3uvZ7Jy9ksjoomWce_topL_ayS7t7MUnehUWykxCyMzgI_JFYN68JemMUMtQsiiMzH2r1DlzczL1MYdmKHTmsaYtjMhMt3hZDI8YDIKe2VNH5X9Z2Ilz-dvMpYHg_ZnG9edz8lAUyDE03AYyQp0fCTBBZ6zTzHeu9JMU1rNNqrvP0rPIS1PhMudBZXwD3iHdIcNMsjBSa9GixNuQdZO0LKRFiC4wI-isWoL_Zee0ht1R4QPnvEgciq-cWRBLK8FCpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بیل گیتس: هوش مصنوعی از انسان باهوش‌تر است
‏
🔴
هوش مصنوعی فقط یک فناوری جدید نیست. این واقعاً یک رویداد تکاملی است.
‏
🔴
ما یک گونه هوشمند خلق کرده‌ایم که در بسیاری از جنبه‌ها، همین حالا از ما باهوش‌تر است و در چند سال آینده، با سطحی که به‌صورت نمایی بهبود می‌یابد، به‌طرز دیوانه‌واری از ما باهوش‌تر خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/149748" target="_blank">📅 20:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149747">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hq4SbwuXaVi590Jx7uDzZ_2F6_KL5KaQeP8O2LzdkTwZlhkVhwI12okOWTDKW-N428PMswMEJlgdR_SFUeVG8NoSh36HLe2ipfK3GM5TdyOtD7qNh8BKiZUpJrwVJTNMya11FZ-6ra-dOh-Iad9sZ7bkrMxJNke6on86YX5phtOyiNtzqiiifdutpfkX8Q5FT0RN9Ey_y5zse7GLxL5c78qQiTWTw3qnhBAD-HwO5XSb7V2rteQrvN-v16JY07_5eTz4mAmrqIuFlrOUSgczkIKrn6pAH3uk30ixAuMJ7z2tPLT7CmLWs6jpNGNxkhG3muKqT5LjbvQJB6oNyS7-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف بنگاهِ فریب‌کاریِ آمریکا می‌گوید ایران کنترلی بر تنگه هرمز ندارد، اما بازار یک اضافه‌بهای (پرمیوم) سنگین روی نفت کشیده است: ۳۵ دلار بالاتر از قبل از تهاجم، و ۵۰ دلار بر اساس قیمت‌های نفت فیزیکی.
🔴
پس یا بازار احمق است که نفت را با این قیمت‌های بالاتر می‌خرد، یا دستگاه روایت‌شویی آمریکا دارد سیاه‌بازی می‌کند.
🔴
برای کسانی که حرف آمریکا را باور دارند، یک دستگاه چاپ دلار رایگان در تنگه هرمز گذاشته‌اند؛ بفرمایید بروید بردارید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/149747" target="_blank">📅 20:36 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149746">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
تریتا پارسی: مداخله دیپلماتیک با رویکرد سنتی چین همخوانی ندارد؛ اما اگر دور سوم و ویرانگرتری از جنگ آمریکا و ایران رخ دهد، شرایط ممکن است تغییر کند.
🔴
اگر شوک‌های اقتصادی جنگ به سطحی برسد که چین دیگر نتواند خود را از پیامدهای آن مصون نگه دارد، پکن ممکن است برای مداخله انگیزه پیدا کند؛ آن هم به شکلی که واشنگتن ترجیح می‌دهد از آن اجتناب کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/149746" target="_blank">📅 20:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149745">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
هم اکنون گزارش های اولیه از وقوع انفجار های متوالی در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/149745" target="_blank">📅 20:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149744">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1bc066b31.mp4?token=JhxPeFdFe2NC2CIaMg8RpSQU_6txiwWbMImztvcPvg0zokte_n5RMDX4mYmBeEmjR31SkAKaQs-ncj0UMVxr6fcDnD-3LWAjlSlPbMDR-mWEmxNEgbV1JAFGe_K-msi_b7TWZlJFVRuAkHko6fQm1TwHFXzpwGoYmiQ7jRmV7ABR0S9UXLqPqLnH-oOLzhBTw0Nqtsr5CItk4f2NMFEJVQ3-DF6ClHK0_ScukC0QrYaiStvhNZMpuRrgYkC4ZyDyZIsNzUvmfWTbKKCBZ5cquaHY2Ac08XjdVndvtpLnlTUpjjDDj8mC5z2_cbREOFUAYrnux_Y3H-et2qGv57akhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1bc066b31.mp4?token=JhxPeFdFe2NC2CIaMg8RpSQU_6txiwWbMImztvcPvg0zokte_n5RMDX4mYmBeEmjR31SkAKaQs-ncj0UMVxr6fcDnD-3LWAjlSlPbMDR-mWEmxNEgbV1JAFGe_K-msi_b7TWZlJFVRuAkHko6fQm1TwHFXzpwGoYmiQ7jRmV7ABR0S9UXLqPqLnH-oOLzhBTw0Nqtsr5CItk4f2NMFEJVQ3-DF6ClHK0_ScukC0QrYaiStvhNZMpuRrgYkC4ZyDyZIsNzUvmfWTbKKCBZ5cquaHY2Ac08XjdVndvtpLnlTUpjjDDj8mC5z2_cbREOFUAYrnux_Y3H-et2qGv57akhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مشاور جلیلی در زمان بایدن و با دلار ۶۰ هزارتومانی: آمریکا ابزار جدیدی برای تحریم ایران ندارد و تحریم به سقفش رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/149744" target="_blank">📅 20:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149743">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
یک مقام آمریکایی به شبکه سی‌بی‌اس:
ما با درخواست ایران برای لغو تحریم‌هایی که پس از ماه ژوئن اعمال شده‌اند، مخالفت کردیم.
🔴
ما می‌خواهیم تعهدات مرتبط با هسته‌ای در پیشنهاد ایران گنجانده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/149743" target="_blank">📅 20:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149742">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
فعالیت‌های قابل توجه هواپیماهای سنگین نیروی هوایی ایالات متحده در استان اربیل، کردستان عراق. به نظر می‌رسد عقب‌نشینی نیروهای آمریکایی در حال انجام است؛ مهلت تعیین‌شده برای عقب‌نشینی، یعنی ۳۰ سپتامبر، تنها سه روز دیگر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/149742" target="_blank">📅 20:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149741">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EI2_vIrtb6R941QV-U93bcXecdIihNPOSTet6X-Ziv_UNJ8HtKul_DAm-XL6t2ubagK3M4YAEHzDgzogOnWoR7EXm7iyWOJzMLxqLkzS_UKEvoN6JU9ZPnSN-AtC73gbmub8OGYqBf69dX-QCADQDO8jw_-DI2ebVGJG9-nyr-akhBE0uqXO3CbISZJP6HvpISVzgUxAdBus2V1kfGkPOyZFJyqIJUFtTQIw_0ifNBRescHk3xIOgsMJiGY0kgA3tQwOq0iIwtZIlQJv29FgdCoQAUGA_8eJrEFMJYfEwhYwV25gPg0xM_HNe9FmPq4y9bl6YaqMF0Xde6JhFNp4Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه تو بلوبانک‌ بیش از ۱۰ میلیارد تومن پول تو حسابتون داشته‌باشید، از این کارتای VIP از جنس استیل بهتون میده
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/149741" target="_blank">📅 20:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149740">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/149740" target="_blank">📅 20:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149739">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سید عباس عراقچی:"جنگ راه حل نیست. این موضوعی است که باید از طریق مذاکره حل شود، و ما در گذشته این کار را انجام داده‌ایم. ما اورانیوم را تا غلظت 60 درصد برای اهداف صلح‌آمیز غنی کرده‌ایم، و این در چارچوب تعهدات ما در پیمان منع گسترش سلاح‌های هسته‌ای (NPT) قرار دارد. ما هیچ‌گاه پیمان NPT را نقض نکرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/149739" target="_blank">📅 19:51 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149738">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f59c715ba.mp4?token=qH8XXFEy91pbNZ6O72kN2Ct_3qoFdmvLsNu2EXMm8jh8mp_NhxUNzOr5mw0giWFFiSdrFkzgh3kZobDxDHpP66Tuf8__-nTCnPb7-BblFq1-DlYABH31JC1Ix7S3BIvoZLdcNib16kiTPQzY-F8r_txMLRUZTAwMFfZhgD9FsLoGumagPFmLd7BsSAYeI2lDPErBC7Tg4heLtj6IHO0J3HgFMB9em5kUQLA8tYA2PiTkBk5PHpCNabLHQn-Yb_VQHXf75dcnKEyEKqJ7DN1CbxPW3jGcY5h0z9-DgZohF7QkSemC8ocFVz6G26npzRilB2rsJey9iqfxEXxabE7hkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f59c715ba.mp4?token=qH8XXFEy91pbNZ6O72kN2Ct_3qoFdmvLsNu2EXMm8jh8mp_NhxUNzOr5mw0giWFFiSdrFkzgh3kZobDxDHpP66Tuf8__-nTCnPb7-BblFq1-DlYABH31JC1Ix7S3BIvoZLdcNib16kiTPQzY-F8r_txMLRUZTAwMFfZhgD9FsLoGumagPFmLd7BsSAYeI2lDPErBC7Tg4heLtj6IHO0J3HgFMB9em5kUQLA8tYA2PiTkBk5PHpCNabLHQn-Yb_VQHXf75dcnKEyEKqJ7DN1CbxPW3jGcY5h0z9-DgZohF7QkSemC8ocFVz6G26npzRilB2rsJey9iqfxEXxabE7hkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری شبکه NBC: «رئیس‌جمهور ایران این هفته گفت که ایران، نقل قول، هرگز به دنبال سلاح‌های هسته‌ای نبوده است، اما ایران اورانیوم را تا غلظت ۶۰ درصد غنی کرده است. این میزان ۲۰ برابر بیشتر از غلظت اورانیوم غنی‌شده‌ای است که برای تولید برق مورد نیاز است. چرا ایران به ذخیره اورانیوم غنی‌شده با غلظت ۶۰ درصد نیاز دارد؟»
🔴
عراقچی:"خب، این سوالی است که ما در طول مذاکراتی که با ایالات متحده داشتیم، به آن پاسخ داده‌ایم. اول از همه، غنی‌سازی تا ۶۰ درصد غیرقانونی نیست. این کار همچنان در چارچوب معاهده منع گسترش سلاح‌های هسته‌ای (NPT) و برنامه صلح‌آمیز ما قرار دارد. ما این کار را برای اهداف خاصی، از جمله اهداف پزشکی، انجام داده‌ایم."
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/149738" target="_blank">📅 19:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149737">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9056ac4f3.mp4?token=Sms6zHDwgBtXNqcMrkGthEccZvCbPu6cWPj8-0mWlD9hTTwq4Uc32r7zkDDqyOZkN13tJ6inJl_HESWWjKYYbBjs9g_jY2LfpiQhc024LqFI0mTL63lFmvXREPm34l8IphdAAjmqRpbJ9FgHs3vxYHCTWTFJOdRYfhSa9T5UCfPw96LsNQOcH61fTvYzv2CXU0GAy5Svpr_LDD0VvbOYI1orUONOVYs22QYBJRwtNvlbqb4bT2Vhvl-Yzvwz7YNScA9anoWwqHR6j0H3gwMZcpbU5KFS5QV_kILxfDLH3Cc6icDTDISm5k8z7E7RCvgiLIZYluyu2CZ9bhMHWw9Vow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9056ac4f3.mp4?token=Sms6zHDwgBtXNqcMrkGthEccZvCbPu6cWPj8-0mWlD9hTTwq4Uc32r7zkDDqyOZkN13tJ6inJl_HESWWjKYYbBjs9g_jY2LfpiQhc024LqFI0mTL63lFmvXREPm34l8IphdAAjmqRpbJ9FgHs3vxYHCTWTFJOdRYfhSa9T5UCfPw96LsNQOcH61fTvYzv2CXU0GAy5Svpr_LDD0VvbOYI1orUONOVYs22QYBJRwtNvlbqb4bT2Vhvl-Yzvwz7YNScA9anoWwqHR6j0H3gwMZcpbU5KFS5QV_kILxfDLH3Cc6icDTDISm5k8z7E7RCvgiLIZYluyu2CZ9bhMHWw9Vow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری: "آیا به پرزیدنت ترامپ، اعتماد دارید؟"
🔴
سید عباس
:
خب، ما به خودمان اعتماد داریم. ما برای دیپلماسی آماده هستیم. و در عین حال، برای جنگ نیز آماده‌ایم."
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/149737" target="_blank">📅 19:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149736">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36b1c0d3e2.mp4?token=ktLPuhKKHyRkcvbbf85EZR9M1Xw334EbxY5DbzYnsDX0i_p2-kslbvpEil-r6bl_iMUpSZScFCXZ5RQRo2Bga6UGw55mir8OcwFLqYq8O07CQ9z70MaI9Z19WwJml-hvnGSFFx_UVXXhb3hVb6FQ5EJqSxd-oP6a2Fu49QZCc8Nw8LRHZFFHq24BAyifVeRJfjR30PNx_p3Da3k8YgjPQ84FQwQ0-YxqjBuffhBoYtGXHyquODI2Z_rfcyr5eZ8NLmW8tumvVXga8cA0PveBNL3rPJAuyF_zCssaNJdlMl7I0_AJrW3VZ8DEl4WHJd-bghld427lNZq8LsGqKP2BcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36b1c0d3e2.mp4?token=ktLPuhKKHyRkcvbbf85EZR9M1Xw334EbxY5DbzYnsDX0i_p2-kslbvpEil-r6bl_iMUpSZScFCXZ5RQRo2Bga6UGw55mir8OcwFLqYq8O07CQ9z70MaI9Z19WwJml-hvnGSFFx_UVXXhb3hVb6FQ5EJqSxd-oP6a2Fu49QZCc8Nw8LRHZFFHq24BAyifVeRJfjR30PNx_p3Da3k8YgjPQ84FQwQ0-YxqjBuffhBoYtGXHyquODI2Z_rfcyr5eZ8NLmW8tumvVXga8cA0PveBNL3rPJAuyF_zCssaNJdlMl7I0_AJrW3VZ8DEl4WHJd-bghld427lNZq8LsGqKP2BcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری: آیا این درست است که ترامپ در حال آماده شدن برای از سرگیری حملات نظامی پس از انتخابات میان دوره ای است؟
🔴
سفیر ایالات متحده در سازمان ملل:  چیزی که می‌توانم بگویم این است که رئیس جمهور همه گزینه‌ها را برای اطمینان از ایمن بودن جهان از تهدید سلطه ایران از طریق سلاح‌های هسته‌ای، باز نگه خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/149736" target="_blank">📅 19:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149735">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3SBPKPI_B93QNhuNn8n3L0mSPQIQTGnuIMtJyKu_UfUq92W-fis84WJkUiJvuFo1Yb3ufvJjq11H_AjHAzIFmnAYDG-m1wrFzxXkIDDb3ySqcubSRkyaRFVGTNEiyFsqFjAiwkvElGIPMbSP9IDgTt1WB78N_1qlgg6jJDvaKIyghI3hGe96jGVowIUBYexKQ2xP16fJZCMB4-sz-Vs_yVYX9QSZKHjzaO_cQrGFJhyDrHYs-pJsT1GwdGxOGnTk4e0e4qGWe-gJR0YXpeLX8W_VxC-MfaU77pEp28iWWuwJPekY8L3EDJR6AfrWMU1n2NZ1KHmTUdlrICzqfa8vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : دیوان عالی ایالات متحده آمریکا هرگز اجازه نمی‌دهد که میزوری یک پیروزی انتخاباتی داشته باشد. آن‌ها به‌طور مداوم، تاکنون سه بار، رأی قضاتی را که به تصمیمات صحیح رسیده بودند، نقض کرده‌اند.
🔴
از فرماندار و از همه مردم بزرگ میزوری که به‌شدت برای عدالت و امنیت انتخابات می‌جنگند، سپاسگزارم. روحیه و عشق فوق‌العاده‌ای به کشور ما.
🔴
من میزوری را به‌طور بزرگ، هر سه بار، بردم و نمی‌توانم بیشتر از این به انجام این کار افتخار کنم. جای فوق‌العاده‌ای — همه شما را دوست دارم!
🔴
پرزیدنت دونالد جی‌. ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/149735" target="_blank">📅 19:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149734">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا درباره ایران:
ایرانی‌ها گفتن در صورت توافق، تنگه هرمز رو باز میکنن. ولی تنگه بازه که.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/149734" target="_blank">📅 19:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149733">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIReDPeYxSo7TL3kKCeiJwPSx1R9pLSlHgcc8c7ouVba3BSH5jhLATx6ixbpR7WTugWZ1WFMxx-uK48q4l7urjCvCpav5H-2wCjHIM0BBP-BuMjUnVByB4qwzbr_zkIeyTt3-7Bf_cBE9zpcj143IHWJCnkAl68AHCSi5u3un3tw8R47tSr26JeKfRpflXcTow8rjdqlTlwCrSCb9iL_k3Ve1wPDaYj9KlspRvet_wuabyF2Nh6GA79GA2NgkUTQYN6HzNJ-DNk7ZjR_-eCIc30LAEiARBLrcL0PlhOzM1vm4V7J7NOEse4qt5HwBvjeMEhXXeyQTGUrDgWlgbEmoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: «همه‌ی شرایط در منطقه» شبیه به «بهمنِ ۱۴۰۴» است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/149733" target="_blank">📅 19:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149732">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
اکسیوس به نقل از یک منبع منطقه‌ای آگاه از مذاکرات غیرمستقیم گفت: میانجی‌های قطری پیشنهاد اولیه ایران را با هر دو طرف در میان گذاشتند و یک پیشنهاد مصالحه نیز به هر دو طرف ارائه کردند تا آن را بررسی کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/149732" target="_blank">📅 19:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149731">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ترامپ: توافقی‌ که ایرانی‌ها می‌خواهند مدنظر من نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/149731" target="_blank">📅 18:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149730">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
اسکات بِسِنت: ما اکنون یک رئیس‌جمهور داریم که چینی‌ها به او احترام می‌گذارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/149730" target="_blank">📅 18:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149729">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2cd8f35d0.mp4?token=fADH2v5cRN8DAdrTrhPBomGIOyF8sa0Isd_A2znuZyhIO4wbWqH4Vua3jz7UE5M9BBuTRyx-O8HAB8Cc6lHqY5Ibk7vnU-LYCXPXobndm1AOuGkUWbKe4Q58WCMFtt653g15Is-OPYLuDogEIo0iLGqwDJn_bjXMPQRLKl485LS3KB2i6wJBzO6YpAEbAx5ncHx1Yz9nN5OB_82v0Rvl5LGllDOmvNgGB2UEY-iceuaAEx3acu2V-ZIg0_Qd7W_Ditr63CrfFEHUct4Ry3R8cKvpUh3paxjvPb-Y5EdawbPLkwHta7EDFzc6bq0X5B1YY-njKMW1j35yzdY6nk6l3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2cd8f35d0.mp4?token=fADH2v5cRN8DAdrTrhPBomGIOyF8sa0Isd_A2znuZyhIO4wbWqH4Vua3jz7UE5M9BBuTRyx-O8HAB8Cc6lHqY5Ibk7vnU-LYCXPXobndm1AOuGkUWbKe4Q58WCMFtt653g15Is-OPYLuDogEIo0iLGqwDJn_bjXMPQRLKl485LS3KB2i6wJBzO6YpAEbAx5ncHx1Yz9nN5OB_82v0Rvl5LGllDOmvNgGB2UEY-iceuaAEx3acu2V-ZIg0_Qd7W_Ditr63CrfFEHUct4Ry3R8cKvpUh3paxjvPb-Y5EdawbPLkwHta7EDFzc6bq0X5B1YY-njKMW1j35yzdY6nk6l3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: ایران تنها دو هفته نفت روی آب برای فروش دارد!
🔴
بعد از آن ایران هیچ چیزی برای تجارت ندارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/149729" target="_blank">📅 18:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149728">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
اکسیوس: منابع گفتند انتظار دارند دور دیگری از گفت‌وگوهای غیرمستقیم میان آمریکا و ایران احتمالاً از روز دوشنبه آغاز شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/149728" target="_blank">📅 18:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149727">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
باراک راوید به نقل از یک مقام آمریکایی مدعی شد که برخلاف ادعاهای خبرگزاری معتبر فارس، در دو روز گذشته هیچ کشتی‌ای آسیب ندیده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/149727" target="_blank">📅 18:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149726">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
اکسیوس:
منابع گفتند انتظار دارند دور دیگری از گفت‌وگوهای غیرمستقیم میان آمریکا و ایران احتمالاً از روز دوشنبه آغاز شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/149726" target="_blank">📅 18:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149725">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚀
کانفیگ v2ray نامحدود | چند کاربره
🦋
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
📍
نامحدود _ PLUS
⚡
:
🇩🇪
🇫🇷
🇮🇹
🇸🇪
🇦🇹
🇦🇿
🇵🇱
🇹🇷
🇺🇦
🇦🇱
🇦🇩
🇫🇮
🇳🇱
🇺🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇲
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
برای اولین بار در ایران
👑
کانفیگ ها بدون تبلیغات هستن
🚫
تمامی لوکیشن ها قابل استفاده در جمنای
✅
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/149725" target="_blank">📅 18:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149724">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqboUD4bDyDregTcDYoJMseXA89wekovvfzfAEmcfaVYxO0R7tfPgq-LLkmrNIxHM_mbE2aqdsDBe-0hFvOKhKPupW82sSVO_FHob0HSsnoGH2jjHZtMEtKKwFYjSuGZH-mOYKCit6koHs34AwHaSm7D5WTz1ouBlklLf3PrL5vQ5JLFZgZLkXGxZ-JmhsrNz5rZ0KcxQrmYoqnSqDR5e1GJvmvFukRbp69RkTin46gbFYAUHhuyfd1xfUp2Ppbu2l6kKWt7JplO24WMLCJtw4tVOWvLTlcdaSGznUkwYbm7gEHmBYwKyKL1AnH9z3RNjAhYHaRhmTViGU1EzpYYAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب آبادی خطاب به بسنت: جهان حیاط خلوت شما نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/149724" target="_blank">📅 18:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149723">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7baea2c31f.mp4?token=chALGb7PdHU3enSEAbNi8gZWlfkAC4hMKftq5qI_LrgHwGID-I6IsM1fM3j1Kb_zAz6D08rIZpco4GpU09Q5sY2zPCvvNPk858Snq9PhkKmok2oeRHsFqPjPB69wwQUIXT70nJGGuF9mZL83R3EEF1GF4Pu-y_bG45GAbSQKghQMaumYYuMB-_w9IK-5wqpwtTHcW4bkTu3fmgf7qnYcAQQkkBRN_oceHe_kFhTyDmZflKq5kIniBG3M8rjvJBsIdrnCf8u8DPkOCn9-Ib8DC04MwIs-zS4Ha0o_E9Qc3YDtVkpFaImuAEuR6n72dTf7gE7gfZeJaFm0ZDd5WI5DbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7baea2c31f.mp4?token=chALGb7PdHU3enSEAbNi8gZWlfkAC4hMKftq5qI_LrgHwGID-I6IsM1fM3j1Kb_zAz6D08rIZpco4GpU09Q5sY2zPCvvNPk858Snq9PhkKmok2oeRHsFqPjPB69wwQUIXT70nJGGuF9mZL83R3EEF1GF4Pu-y_bG45GAbSQKghQMaumYYuMB-_w9IK-5wqpwtTHcW4bkTu3fmgf7qnYcAQQkkBRN_oceHe_kFhTyDmZflKq5kIniBG3M8rjvJBsIdrnCf8u8DPkOCn9-Ib8DC04MwIs-zS4Ha0o_E9Qc3YDtVkpFaImuAEuR6n72dTf7gE7gfZeJaFm0ZDd5WI5DbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی : در حال حاضر، یک طرح بسیار منطقی ارائه شده است. اگر این طرح بدون دلیل رد شود، این اشتباه آن‌ها خواهد بود.
🔴
با وجود اینکه از رئیس‌جمهور ترامپ شنیده‌ایم که این توافق را رد می‌کند، ما همچنان منتظر پاسخ رسمی از طریق واسطه‌ها هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/149723" target="_blank">📅 18:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149722">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40858e6d1d.mp4?token=gHqfE-uLdO7YPLhG3Eh2mW-HYhar-oCJ5N2ph8FZh7FvlOjlFnd4t_ffoTVR1L6L5RXCIx3t0wtpp3cPDsc16H0RqmvtId8Coy89FwKjPYUNGMJzkvFwBazbC22vJxWXwE-wXJip9Lqsk14u2AgQYZ335IKcnYs0YAI7fatdG3vkxehIZ4pCBsvrR9mHCvjrEM8XOOhW4F1zeUlqoKjH2QnuDATf3ot4y9-pyC3vZCMAg0fhJqgmPL6wp42sTje9hA_9OPNRTOK06O6FsQJCqgnsiBpiu2U8psaewtJzGQtBF9h25F0tuLhMQd2hFAxyFPQ8XEGiuxWe-_3QDVVzjqfcr-IRIzWTEb-qrRRNQnN00lkIaTLZmyqyaHDmLJbtGYI5ZG1WPoAzs5TEFzHWPVvxAOw93qz9u0OnT-sfWEQEDgA4n6KHSINSC0s5e89Z3DHK5bgKy_nWs2vKLBpUR5I2BsKobU6UWQZoPr0yQOaW2P9zS4XxLvSGEZWPGqNMv0Ja-z3Io6uK9SyfOO-2ge7-a7Km0OkkQu7p2pu9LJoMZXC2rmUgCcXmWb2dsNngAnYoH-AvF_rtdcfIgEWCmN9qSeGQuxB3yP3f5cDrDLdDCVykka1h1QyLPJ5ofu2tq1azpbO0_AhPUCN8gz5x6VWm_I1WEXqnPdRC78yDPjE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40858e6d1d.mp4?token=gHqfE-uLdO7YPLhG3Eh2mW-HYhar-oCJ5N2ph8FZh7FvlOjlFnd4t_ffoTVR1L6L5RXCIx3t0wtpp3cPDsc16H0RqmvtId8Coy89FwKjPYUNGMJzkvFwBazbC22vJxWXwE-wXJip9Lqsk14u2AgQYZ335IKcnYs0YAI7fatdG3vkxehIZ4pCBsvrR9mHCvjrEM8XOOhW4F1zeUlqoKjH2QnuDATf3ot4y9-pyC3vZCMAg0fhJqgmPL6wp42sTje9hA_9OPNRTOK06O6FsQJCqgnsiBpiu2U8psaewtJzGQtBF9h25F0tuLhMQd2hFAxyFPQ8XEGiuxWe-_3QDVVzjqfcr-IRIzWTEb-qrRRNQnN00lkIaTLZmyqyaHDmLJbtGYI5ZG1WPoAzs5TEFzHWPVvxAOw93qz9u0OnT-sfWEQEDgA4n6KHSINSC0s5e89Z3DHK5bgKy_nWs2vKLBpUR5I2BsKobU6UWQZoPr0yQOaW2P9zS4XxLvSGEZWPGqNMv0Ja-z3Io6uK9SyfOO-2ge7-a7Km0OkkQu7p2pu9LJoMZXC2rmUgCcXmWb2dsNngAnYoH-AvF_rtdcfIgEWCmN9qSeGQuxB3yP3f5cDrDLdDCVykka1h1QyLPJ5ofu2tq1azpbO0_AhPUCN8gz5x6VWm_I1WEXqnPdRC78yDPjE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد حادثه رخ داده در پایگاه هوایی بریتانیایی فیرفورد: دستگیری‌ها در بریتانیا فوق‌العاده بود. همکاری با بریتانیا شگفت‌انگیز بود.
🔴
آن‌ها قصد داشتند آسیب جدی به پایگاه ما وارد کنند، و همکاری با بریتانیایی‌ها به نحو احسن پیش رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/149722" target="_blank">📅 18:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149721">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
بسنت، وزیر خزانه‌داری آمریکا: چین کمک‌های خود به ایران را به میزان قابل توجهی کاهش داده است
🔴
ما اجازه دادیم بیش از یک میلیارد بشکه نفت از تنگه هرمز خارج شود در مقابل صفر بشکه برای ایران.
🔴
انزوای اقتصادی ایران به صورت مرحله‌ای اجرا می‌شود و ارزهای دیجیتال، هوانوردی و حمل‌ونقل دریایی را در بر می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/149721" target="_blank">📅 18:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149720">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: تحریم و انزوای اقتصادی ایران به صورت مرحله‌ای اجرا خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/149720" target="_blank">📅 18:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149719">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
عراقچی: ایران آماده از سرگیری جنگ است، حتی اگر اوضاع به "روز قیامت" ختم شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/149719" target="_blank">📅 18:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149718">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbVnzKnIQnEQaRPoEjrLKrIErbh5WcLley0TVgkKBaawWff2a6mhSS0KSDaYXFVXNkmNXIkm8fzWRCXmoDwNvxSaZ0zdI11Ko8hAX4FFXlI7BPlyCa4CSWtL6zrAktgeas7JHo4qYURXNTsf3fmIFa-pwBmbZerOJh-C9_4id5ovkWD5JVpg81ss4vnbF2SyRoDW_umB4hlWtSdIYVfpUAHLEQIQcWNoB9qJaDspehsdOjkzF9FxuD3UK4c3yeErv_LdWap9QkVieKNGo3Tds6vwmXEOWzR7pGINb3oik5Ufgw9u4ps_QYrlN3wRfLTy4XUPrDtt2uwyfuTa-RkfeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / خبرنگار cbs : یک مقام ایرانی به من گفته است که مذاکرات روز دوشنبه میان ایران و آمریکا لغو شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/149718" target="_blank">📅 18:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149717">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
پروازهای ایران فقط به این ۱۰ کشور همچنان برقراره:
🔴
چین
🔴
روسیه
🔴
ترکیه
🔴
افغانستان
🔴
پاکستان
🔴
ارمنستان
🔴
بلاروس
🔴
تاجیکستان
🔴
ویتنام
🔴
مالزی
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/149717" target="_blank">📅 17:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149716">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
خبرنگار الجزیره به نقل از منابع ایرانی:
مذاکرات با آمریکا ادامه دارد و ایران همچنان منتظر دریافت پاسخ رسمی واشنگتن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/149716" target="_blank">📅 17:54 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149715">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
عراقچی: می‌خواهیم پول‌ها و دارایی‌های ایرانآزاد شوند
🔴
وزیر امور خارجه  در گفت‌وگو با ان بی سی: از خود می‌پرسیم چرا آمریکا پیشنهاد ایران را که می‌تواند شرایط را در خلیج فارس و تنگه هرمز به حالت عادی بازگرداند، رد کرده است.
🔴
اگر آمریکا اقدامات مشخصی انجام دهد، آماده‌ایم تنگه هرمز را بازگشایی کنیم.
🔴
این اقدامات خواسته‌های جدید یا موضوعاتی از ناکجا نیستند؛ بلکه حقوقی هستند که خواستار احترام به آنها هستیم.
🔴
ما خواهان پایان دادن به جنگی هستیم که هشت ماه پیش آغاز شد و می‌خواهیم پول‌ها و دارایی‌های ایران که به‌طور غیرقانونی مسدود شده‌اند، آزاد شوند.
🔴
به انتخابات میان‌دوره‌ای آمریکا اهمیتی نمی‌دهیم؛ آنچه برای ما اهمیت دارد منافع ملی ایران است.
🔴
همان‌قدر که برای مقابله با هرگونه تجاوز، حتی اگر به جنگی ویرانگر منجر شود، آماده‌ایم، برای مذاکره نیز آمادگی داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/149715" target="_blank">📅 17:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149714">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
بلومبرگ: ۳ نفتکش توقیف‌شده از ایران در راه تگزاس هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/149714" target="_blank">📅 17:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149713">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
حملات هوایی سعودی یک برج و ساختمان مخابرات را در استان‌های ذمار و البیضاء یمن هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/149713" target="_blank">📅 17:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149712">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
مقام عراقی: تعلیق پروازها با ایران به رعایت دستورالعمل‌های وزارت خزانه‌داری آمریکا توسط شرکت‌های خدمات زمینی بستگی دارد
🔴
عدم موضع‌گیری علنی دولت در مورد پروازهای ایرانی به دلیل حساسیت موضوع است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149712" target="_blank">📅 17:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149710">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CpzHfq_x5-Q1Q-qsqOVpK9I8lV9IpATPwlAl87itxKFA9f0jp-vAo7dujlcnt8DSkVg2ky8C2kHRgv44IvZdgdIOwvgFmm1ooKs4OsW0GYrhl_WwNal2IwSoLQfiKn5_nXP5bULJ70xXoGonMt3MHv_xe0Rx9iFVE9IC8jxJ9BJMl4fA73Fu2IxqWnZHBBsV09dsrAThKGun4VCreM2htGv9K8g1vZWokkTZJJX33JIXdm7uOIH08-zG27xfQCs5MOHFCn1Hnla5K5KB1DMpuZIGZIbnFDHubtMaVIscooKBRHCYdNA3cY2D3mB6raYF1FRSUEIK1PfKS9zF2Z3tRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NZl4el0uT7vb10o3El3ewmSAqbf7cnquI6sevpLs93SYOEaVhSvAL9ujsJlNeD3zahkf5q9bxE3S5ZCFeqqIU6LUlEqKiVDwFCkdMkM1kg-FTkYnJxyHQHxfssWOHZzC1u8r9RdCIjsRlXQTRtwXjZujTNU5LBW2BesXb8BZIei5XgQtEfbLMGSYPpwcgEFQV0jeLD_CCYNdZXCCmayB0R5e58Z4F8XuTppASCHoIio_oEOGe1SCvgR7QKl8Ns39faaxALhvrNZH0nDhL0hQ3gN-SwmH6DhMuxMkoWELK_mYfyla1hNE6howm774hNGmhFOYSuF45UYX3OnNuJWPGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هواپیماهای تانکر سوخت متعلق به عربستان سعودی و بریتانیا در نزدیکی یمن پرواز می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149710" target="_blank">📅 17:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149709">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bvbbv-T7A6faO2ik4NJPYoJ2-IzCKylxhTW0mflBkgJsboy3PItB2re6U58R5S9pdsCec3uGeNggcYDv4QxKxFMRLmsUe93BKZCPmpaRccnNEGWf2p01D1J1WEkMoGBB1zkluv-bKJpvYDA_iBMbXIm-dQDFckTgTg1U5aXke1xLK3l0sSr89uBo9CoroQIHDvQtV0W64O8IcG0cM0kU1dduW6B32kmnyWp4ATP-t42ld7HLTw6yAXurIVmDs8mBJcVBGdXZW0jmIqcCrAAhEYxRzXB1PoaYH-rGdCtKZhc_lAkkiNnPq0j3SUHZ60n4TtEtNGuUHMOBIRJ948awrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بعد از ماه ها تفحص تو مدرسه میناب یه چسب که روش اسم ماکان نصیرزاده نوشته شده پیدا شد و این آخرین باقی مونده از ماکانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/149709" target="_blank">📅 17:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149708">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011bddf1e3.mp4?token=UK5DMbILef9ABcyP5EqaGsw06GDWZgGWFpElYQBEwlXmTDzXb5mwl7ciPwf35pBkEBzNV_eDVNX9Q0t6uhh3UPk6i7aatFaHEHWWWDYQUafW4VDmMNDgeiVcSE3bdpf1MrQbYebSr8_FG8Jrey0zmNss-JoK1w8C3PgdTirOvNBLOQzRarRaEUCUyug9cVDt232CkcoVAPMtTmQVlRsyyCHN1CL2MWQ-_dEbbsfL9-cglMVoKpJLOcHnr7AXiTlD_sceXEl6VPlOjHFbraU0qFEce0vseEXcHLdIsL7upNgz967kZPHj7ZvjpaDAZetWQ47O6NJtMee3EdN3eVHOoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011bddf1e3.mp4?token=UK5DMbILef9ABcyP5EqaGsw06GDWZgGWFpElYQBEwlXmTDzXb5mwl7ciPwf35pBkEBzNV_eDVNX9Q0t6uhh3UPk6i7aatFaHEHWWWDYQUafW4VDmMNDgeiVcSE3bdpf1MrQbYebSr8_FG8Jrey0zmNss-JoK1w8C3PgdTirOvNBLOQzRarRaEUCUyug9cVDt232CkcoVAPMtTmQVlRsyyCHN1CL2MWQ-_dEbbsfL9-cglMVoKpJLOcHnr7AXiTlD_sceXEl6VPlOjHFbraU0qFEce0vseEXcHLdIsL7upNgz967kZPHj7ZvjpaDAZetWQ47O6NJtMee3EdN3eVHOoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
ما بهترین آمار فقر در تاریخ کشورمان را داریم
🔴
اکنون میزان فقر در آمریکا از هر زمان دیگری در تاریخ این کشور کمتر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/149708" target="_blank">📅 17:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149707">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
پلیس بریتانیا: پنج مرد بازداشت شده‌اند و همچنان در بازداشت هستند و پلیس مبارزه با تروریسم تحقیقات را پس از اعلام وقوع یک حادثه بزرگ در نزدیکی یک پایگاه نیروی هوایی سلطنتی بریتانیا هدایت می‌کند.
🔴
پس از گزارش‌هایی درباره سه خودروی مشکوک، پلیس به محل اعزام شد
🔴
این افراد همچنان در بازداشت هستند.
🔴
85 خانه تخلیه شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/149707" target="_blank">📅 16:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149706">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2380fb253c.mp4?token=L4USCFu7Hg6SYjG6zb5Kb4atr0fdAJ7LnKDdP_CTtjs8ghTlI6bEE-Ogc5KqVdHTSzaroSWFWoZ4c7YQ0RfckV6j84V1tVcImenzPFSZ7is6sgRYAdY3lW_FhJixEf7zRgfOKI-i5ogoELCL-hsJTd-tLpo3Hzk3DnqgPuB-p_tkSgNUJehGoIbNf5KHoOyOa3J00ivRnM2XTpF2uqZ-lprheq6XjykrAgpJqm01Gz2k_qbxEZWmBqTqHRGAEkDeTRpiQxs03jwzxkcsrM-aLUYWsBDg7lSVMm6_bwrwcsOapaancCYPoXJ-PmRMSS65mTUu1axA25KV-4wS_Jv-jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2380fb253c.mp4?token=L4USCFu7Hg6SYjG6zb5Kb4atr0fdAJ7LnKDdP_CTtjs8ghTlI6bEE-Ogc5KqVdHTSzaroSWFWoZ4c7YQ0RfckV6j84V1tVcImenzPFSZ7is6sgRYAdY3lW_FhJixEf7zRgfOKI-i5ogoELCL-hsJTd-tLpo3Hzk3DnqgPuB-p_tkSgNUJehGoIbNf5KHoOyOa3J00ivRnM2XTpF2uqZ-lprheq6XjykrAgpJqm01Gz2k_qbxEZWmBqTqHRGAEkDeTRpiQxs03jwzxkcsrM-aLUYWsBDg7lSVMm6_bwrwcsOapaancCYPoXJ-PmRMSS65mTUu1axA25KV-4wS_Jv-jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دو مدرسه تو تهران؛ دولتی و غیردولتی
یه ویدیو تو فضای مجازی وایرال شده که دو مدرسه رو کنار هم نشون میده. یکی دولتی و یکی غیردولتی. تفاوت فاحششون نشون‌دهنده فاصله طبقاتی تو جامعه‌ست.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/149706" target="_blank">📅 16:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149705">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏
👈
عراقچی: آمریکا در نهایت چاره ای جز پذیرش شروط ۷ گانه ایران نخواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/149705" target="_blank">📅 16:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149704">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMCZLceKzOa_skUlklnEAvezGEV5tppSdyusjcM3o4AJDTIvKaU93JC1l_U5-yUr9xoNG5EBLuAIygsXo00EjEYAFN9HFFC0MDHla9fPjen1X0u8GCORZJNpAYajH8sxD3fh85xT3798EU4KxaLon7Ncx798SNoTAQjehIDSmRek0XcSzSWi1rriTbvR_7bA-nyyL8VR1g7ByKXIHg-DTxiNj_iw1ApUbxBDMzEO5mb83tghSvDFIFIsxZVk_t7vdUbQSxilAWJGug6vcsDSJEzt2J1L7wu6i2H3Sf_Wr4FeQPdII9fIB8kBfoCRwyGZWj5Mf88Z1RW0i0JJDYm7Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از متحدین ائتلاف ایران علیه غرب
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/149704" target="_blank">📅 16:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149703">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c70d8cb102.mp4?token=L7FliKasY9gJTk4ny3ieTSYWoHJ_f3PWfXopjQlasBlO7uGBis5Pp89bfGph1CMRnTWrzqwKO-pw-flnwmNlisMDc2P_HevPXD49bSlpTvaX8Izq4zFnEqIyAQlflJGmVXpiHdaGi91hbgcCnDBMrmMNI6asNCUmUmKgdv5lMZwG_LGf9Cj-COBBYnh9HiD3bk_Ic4-2Iklf8HNAhiDrvde3_SYL6VwwAc689_EYXMo_1H5Tq8jyKAvbpj_a6o7WtBxQXx3en51LT7209vE0oc7C4sPrkabxJivr-Qtecx1oHnEZoV4jELwv_GiI4wDMRi8kh_VIFGJHt-tqSVCj0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c70d8cb102.mp4?token=L7FliKasY9gJTk4ny3ieTSYWoHJ_f3PWfXopjQlasBlO7uGBis5Pp89bfGph1CMRnTWrzqwKO-pw-flnwmNlisMDc2P_HevPXD49bSlpTvaX8Izq4zFnEqIyAQlflJGmVXpiHdaGi91hbgcCnDBMrmMNI6asNCUmUmKgdv5lMZwG_LGf9Cj-COBBYnh9HiD3bk_Ic4-2Iklf8HNAhiDrvde3_SYL6VwwAc689_EYXMo_1H5Tq8jyKAvbpj_a6o7WtBxQXx3en51LT7209vE0oc7C4sPrkabxJivr-Qtecx1oHnEZoV4jELwv_GiI4wDMRi8kh_VIFGJHt-tqSVCj0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
قیمت نفت اکنون پایین‌تر از دوران دولت بایدن است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149703" target="_blank">📅 16:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149702">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c275c1a77.mp4?token=TghLUHKK-thw-V88UL2zsuw7Y07qaqEwo0gUaP7Lp4plGL23qqaijgRk-kqry_BkjZD3iuD90mIwLAmm_9T0ib5JEZmD0hH0Ftbst4bUM7uCvboTEL-jnGLstcWlUkvPyF2YNmF0x0B-loDSfIcYPIqlaQaABlQveGFfq_79JQGjST8vDP6VaO91DGFk-QafiCphWK8E8DjmpSPFgUPisbYlZ10GkUZJCjlXF9b0er8TRfg7wVo9QbgoVgVsyLbo9uvlngvA3NxjbVFzruGlDwMiaKaDRurW4KsehAAvJRW5DJgmhuXmXVl-Q7R3a9xjKHUCNYx9_QUesr1jEVZWzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c275c1a77.mp4?token=TghLUHKK-thw-V88UL2zsuw7Y07qaqEwo0gUaP7Lp4plGL23qqaijgRk-kqry_BkjZD3iuD90mIwLAmm_9T0ib5JEZmD0hH0Ftbst4bUM7uCvboTEL-jnGLstcWlUkvPyF2YNmF0x0B-loDSfIcYPIqlaQaABlQveGFfq_79JQGjST8vDP6VaO91DGFk-QafiCphWK8E8DjmpSPFgUPisbYlZ10GkUZJCjlXF9b0er8TRfg7wVo9QbgoVgVsyLbo9uvlngvA3NxjbVFzruGlDwMiaKaDRurW4KsehAAvJRW5DJgmhuXmXVl-Q7R3a9xjKHUCNYx9_QUesr1jEVZWzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
شب گذشته، رکورد تازه‌ای در انتقال نفت از تنگه هرمز ثبت کردیم؛ حتی بیشتر از میزان نفتی که پیش از آغاز جنگ از این مسیر عبور می‌دادیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/149702" target="_blank">📅 16:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149701">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a495b9a3cc.mp4?token=fGXNba4QZk2H6y-k3nuYW4fCAfdeQWaivTxIhhpK5B5j6kPAv4LnP74qv4bCKjWBluFmXqk6TBa_OFeRkJsiPQxUftGptg_VLuds1ELQBK_LdFp8kOCKQ4N52FbyxMXNvOQ57d5oBG-KTgx_pw7_ecKh9Hhrp3_tDe81s4Ev3o_-Q3bckpGpHdbOIiXj6RC47o9PF6rhCpNGrCozUG_L2qpFwe00-r6FxMaZ2jroiA9PnE1kMjr7XBrBE7GdrpKSsiX9vCZy0BYpCWZRcUL8dNKdtc6nf7ieVp4vKwtbstz_2omLXC1GK8mOXjA1YyVHs7ZwQgyLA4hA8XKHx1sjew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a495b9a3cc.mp4?token=fGXNba4QZk2H6y-k3nuYW4fCAfdeQWaivTxIhhpK5B5j6kPAv4LnP74qv4bCKjWBluFmXqk6TBa_OFeRkJsiPQxUftGptg_VLuds1ELQBK_LdFp8kOCKQ4N52FbyxMXNvOQ57d5oBG-KTgx_pw7_ecKh9Hhrp3_tDe81s4Ev3o_-Q3bckpGpHdbOIiXj6RC47o9PF6rhCpNGrCozUG_L2qpFwe00-r6FxMaZ2jroiA9PnE1kMjr7XBrBE7GdrpKSsiX9vCZy0BYpCWZRcUL8dNKdtc6nf7ieVp4vKwtbstz_2omLXC1GK8mOXjA1YyVHs7ZwQgyLA4hA8XKHx1sjew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
به محض اینکه ایران تسلیم شود، به محض اینکه جنگ به پایان برسد، که این اتفاق به زودی خواهد افتاد، قیمت نفت به شدت کاهش خواهد یافت.
قیمت نفت به طور چشمگیری کاهش خواهد یافت و تمام قیمت‌ها پایین خواهند آمد، اما قیمت مواد غذایی به میزان قابل توجهی از زمان ریاست جمهوری بایدن کاهش یافته است. تقریباً تمام قیمت‌ها به میزان زیادی کاهش یافته‌اند.
ما حجم بسیار زیادی از نفت را خارج می‌کنیم؛ شب گذشته، ما حجم بی‌سابقه‌ای از نفت را از تنگه هرمز خارج کردیم، بیشتر از زمانی که قبل از جنگ این کار را انجام می‌دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/149701" target="_blank">📅 16:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149700">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tqMsLAudRUn9b1bEriXZAzQ2gGuDP8AMmnnoQW_oaAXGYOhGPGBXrwkiSZy_FZJmtmACgcIWwi7pISYLveiNkf6f9cpJSvPpo-tSlMP5-_TUfYe54fliStXW4rQnBWrz_voaxRXFZbtkI8r72p8Wy_LZoeSv7wsX2GwxVdfzh_qncoMd2fnWAGRU7PC2-QAkJBCTlTrVOfTi_VkDz-My7_e7MmTXIZV-uBE4PBaNgWEeao_p-euMiI4KRaNh-H_XET5mZaEXfcvnPnNp4vEyP3thoBOTKHYqXaURPQGBIMUn8JSdDm-6pnbJlMFKXkVk7Fqpn-tr7GGN8P3OIhARwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاطمه معتمدآریا بازیگر هم به ایران بازگشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149700" target="_blank">📅 16:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149699">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdZiH0ENmW_VNp9lUj5BYY_J3w4SlqAWOeRr9G8IqNV98wCswaO5hbzycyZ59m4VIhwxlHLx34qvmzEowkmGkWnvR7lv3tF2fUML1yEtLFXcYnCjS75SrFemHUZnw-2o8DgN0998Bu6XV3pcmDByNsymMnNn95ZY2iVU_OYm4dYCzDB3Pm2ga-FVyBW10g5-Hr5HFnlu2DLswajZenMlJugOQpwCp_86ShZBvsdyjaEWvXR_0s4xVIlpesVqxhcXuHoRTe_Stp7GA3MBbtuj2PfgBuvR27lw5v7A9mLBBsANPrg_L_CpliRScLoCWO-ncOvEeP16tN_gF0KGNvegIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: هیچ‌وقت در تاریخ آمریکا این‌قدر افراد شاغل نداشته‌ایم
!
🔴
همین حالا افراد بیشتری در آمریکا مشغول به کار هستند تا در هر مقطع دیگری از تاریخ کشورمان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/149699" target="_blank">📅 16:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149698">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjzuVFmv4CX0EyAjvDF0DAZaZ8-0Uw6xbZmcJ3NJldv3Nqc82s2syQfwYOo91sD87LTuyGd1AAMKMvPRr3iBVT31l31YmuNtkQF_ZpCloPMQ0DMCnZ832XmSPR9kiaa4iEtpKijY1Cr2InReeeL3PEMfLNRIklrkw5TxpTR7bOdIjpHAh0WxARh5221h2keD1C0TdSHcff8EQJbqkcs6rVa5D5ECoFoari8lrBzLSZLOHCk8ruCt5TudI8Hl99lD_h7EuH-9uKDvifHUkxFo-k_6kBT0yQvYeimZFqGrraiFFUIWLDqTRpzRUVX1SiQZocr3AMNfl95LtX0bURfHZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
قیمت بیت‌کوین به ۲۰ میلیارد تومان رسید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149698" target="_blank">📅 15:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149697">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2OG4RqCnEqPms4WZRAOIYkcUlrP15vXKIpquRXjvfqdZB4uvekJ5xqpa5OPj_qMGr2MXkDpulJ9ZgMxAXWFtz6zb2Vj2rrbKRbZXNYCqMh1TI6zWRxE0hy__h_ZqVJ91jTFASfrkJy7BPA72_MRQZ4EkhyJAlspz4jabeb4tYyj0BFA891Nd9kMGXJlxgRAnMRGS53CdvVMHpUnDqJgyz1bgC3F6numH6FaZiG0Y2QWrDaqzood9BgSCErkIPPP4jHUSiOMOO0RdlWtjAKgu3TB4Alw9mYxkroanXFpbbiF9MHunGHtlHiiabId3_p59pli3qLXPYry_XrYPh0Spg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای ثابتی هم پرونده قضایی تشکیل شده و احتمالا بزودی اونم محکوم میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149697" target="_blank">📅 15:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149696">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
طبق گزارش برخی از رسانه های خارجی؛
آمریکا قصد داره با فشار آوردن روی کشورهای پاکستان
🇵🇰
؛ افغانستان
🇦🇫
؛ عراق
🇮🇶
؛ ترکمنستان
🇹🇲
؛ آذربایجان
🇦🇿
و ترکیه
🇹🇷
مرزهای زمینی ایران رو هم محدود کنه و محاصره زمینی هم به محاصره دریایی اضافه بشه.
چون الان ایران با وارد کردن کالا از مرزهای زمینی تونسته دووم بیاره و اگه مرزهای زمینی هم بسته بشه؛ عملا هیچی دیگه وارد نمیشه و به یک زندان بزرگ تبدیل میشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149696" target="_blank">📅 15:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149695">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-qF8v4MYsyvhO6MsP_3Vq6omq9Icuh8hZjHjRwgOHJMEnNtRGQeefUexQgXvHfWsmfRb9HtXgCWvWkeSYnqON5tQcPBhTW_dnsnTc0y_DyNjtr9T1qlOdszzaBN1jToQ92Hl8R3JvmjQb7haK_TP9o-LunfotXpX_3Kreey5kZXx1_CCTMMEb-c9x7C-2Cu8tveQaqvmzh-dsn5QGiPxKnQ-BJ-5ByV__0ZSLfusZKW2IuZGOAGFqNVVxKoO4DJ-VsU11dS6KREzJMiTeC-rJgDPjyvj9-FtCSef093E7B4jhlF3-cwpWE5gPGGIaLsXj_GAxuVdGW3upNKfKiEVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی بخاطر شکایت قالیباف و چندتا موضوع دیگه تو سال 1402، به 10ماه حبس محکوم شد  #عروس_زندان
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149695" target="_blank">📅 15:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149694">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlBGM6qUkVRDLm4eSgmViEHReaEH_2N8Bs9nCSMKfEXxeHOT_RL00qa51FsGRmODKHO6kx80mRKFRdxSooz8m7B1wv615dYnPQ9i_DEKp4zN6hPcThtdSOdC7X2kOUqVCbrfeHQcQrq3U6Cbk3da9bmHhVydBQtvrBeixcIegcHcVSL0Q3HP6Ayxb7nKR5wQW_z2MHzjWmGx3SasivO39UgG0wWYiN8cK1UcBuPdEa1ZwI1YopSX60Xg3nXhHjEjfc4rR5eWHmUmLpjMv6VLaG9YmMnd0fgh-3NXRy6zGyMCGnPISHCCDosgoJeHnhOmBcTmWYyfbcpGyK91xq9xzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کامنت وایرال شده از مرضیه حسینی، خبرنگار ایران اینترنشنال در کنگره آمریکا.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/149694" target="_blank">📅 15:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149693">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
فارس: شب گذشته ۷ کشتی و شب پیش از آن ۱۲ کشتی هدف قرار گرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149693" target="_blank">📅 15:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149691">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mABN5yPoX-izWVXWWiNK8IzhaB7lhIfLguY6WnM3Ey08mjk1x4_Drx5AYy0ghk1B_siuglolbFaGqT5zR5OLU_avW5TyZYmHq0kKo1ULz28zSIs8n5Dg2hjvhshRQ7s4IMaqOSlkeSqYCgfiR7s4rQZyWcz5qAr0H0EDzOc7L28kk06WU-S43dDscKg0iPN1QHniW5JP4nH-NSsxmf89XuPemcOR8aSCj7vd_NwalgxJdEUR8qpz3Y0gaYCHY9OYtK7M0th6YdQ7XIOWtjKrYYKRgnpuCD2f8K42umNnlcJu2kYU9fZ421xBQ79gpQKxVdexqdMDvxxVa6XRnnDYQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777e744fd9.mp4?token=bZ1xH85KtBk-qkJDaOeGah6gP5vSmwabs9huphWdIh5mtmiNybRiz7pDOTtKguKIe9k-w7sth5gO_4wWPCFR_aL_oEHBImT0oxteW4PN07S1EleLoNy7kvDa9KgAqYI7dyMwbQX3Hb_uQJzMho8j6AgbUdIgtANSbpTamykwN7SaMh0BD9QS11kV9t0PNl88a_b0k5RJ-ezxiHu1sdNccaEj51aiWKS4M04DRixP4syzpW3aL_bPH9i7FceaeCT7hF7HXltop6ham1vUqu5AFFEpmCfsN7qBUjidd65i4gZzJaZ2r8ruD4BBM0deOBidsnKsg3jN3VYoDIRuKfL3XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777e744fd9.mp4?token=bZ1xH85KtBk-qkJDaOeGah6gP5vSmwabs9huphWdIh5mtmiNybRiz7pDOTtKguKIe9k-w7sth5gO_4wWPCFR_aL_oEHBImT0oxteW4PN07S1EleLoNy7kvDa9KgAqYI7dyMwbQX3Hb_uQJzMho8j6AgbUdIgtANSbpTamykwN7SaMh0BD9QS11kV9t0PNl88a_b0k5RJ-ezxiHu1sdNccaEj51aiWKS4M04DRixP4syzpW3aL_bPH9i7FceaeCT7hF7HXltop6ham1vUqu5AFFEpmCfsN7qBUjidd65i4gZzJaZ2r8ruD4BBM0deOBidsnKsg3jN3VYoDIRuKfL3XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خنثی‌سازی مواد منفجره در نزدیکی پایگاه هوایی فیر‌فورد بریتانیا
🔴
نیروهای امنیتی بریتانیا در حال تلاش برای خنثی‌سازی مواد منفجره در نزدیکی پایگاه هوایی فیر‌فورد هستند.
🔴
در تصاویر، یک ربات کوچک خنثی‌کننده بمب در نزدیکی چند کامیون دیده می‌شود که احتمالاً حامل مواد منفجره بوده‌اند و به سمت پایگاه هوایی در حرکت بودند.
پایگاه فیر‌فورد محل استقرار بمب‌افکن‌های آمریکایی بی‌۱بی و بی‌۵۲اچ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/149691" target="_blank">📅 15:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149690">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">فکت  فرودگاه نجف رو جمهوری اسلامی ساخته ولی الان هواپیماهای خودش نمیتونن برن اونجا.  [@AloTweet]</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149690" target="_blank">📅 15:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149689">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
رئیس دانشگاه تهران: در جنگ اخیر ۲ استاد و ۵ دانشجو را از دست دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149689" target="_blank">📅 14:53 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149688">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
سپاه: شکار دومین زهپاد [زیرسطحی] ارتش آمریکا در تنگهٔ هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/149688" target="_blank">📅 14:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149687">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJ7bolTD5oBuCu_rk2nEYEK6qa5Jg1BR-IcXrmssqwSF-BthY5OZF8pAPJcvycBB5guKx4jAp9pROyYhVhmhKIOXmzvb2aKIeezNMANDqTemslpU8a3j9Inufci2pVBW1-lB6QoWtAQkQhF56qyT1A0jGQTwwmG3joMzZBDaKZ4pMGF3JtCfFg1JRd4_Ody7bdw9d8C1nAJFgUuUyxo6Xc29y2rMQMLYGWsdvnJD5WZi306rLNJZvb1BQgLWcAKe70MugpU9tJheQPIaAF9xYl-4eUD80iU053D3UbAAaumaUycNbS6a7HRU1VWjRz4qzyDTlxeyCFviAZNYrz8-4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساعاتی قبل، پرواز ۴ هواپیمای مسافربری ایرانی به مقصد ترکیه
🔴
مطابق گزارشات، باوجود توقف پروازها در مسیرهایی مثل عراق و امارات، مسافران ایرانی می‌توانند با هواپیما راهی استانبول ترکیه، اسلام‌آباد پاکستان، کابل افغانستان، پکن چین،‌ دوشنبه تاجیکستان، ایروان ارمنستان و مسکو روسیه شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/149687" target="_blank">📅 14:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149686">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
رویترز: بوئینگ یک نقص نرم‌افزاری را که پیش‌تر افشا نشده بود، در هواپیماهای ۷۳۷ مکس شناسایی کرده
🔴
بر اساس این مشکل نرم‌افزاری، ممکن است خلبانان هنگام فرود، به هدایت خودکار پرواز دسترسی نداشته باشند
🔴
هنوز مشخص نیست چه تعداد هواپیما با این نقص در حال فعالیت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149686" target="_blank">📅 14:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149685">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
فارس به نقل از  یک منبع آگاه نزدیک به تیم مذاکره‌کننده: پیشنهاد اخیر ایران [به آمریکا] دربرگیرندهٔ مجموعه‌ای از اقدامات متقابل و مرحله‌بندی‌شده است و ایران مواضع و ملاحظات خود را به‌صورت روشن به طرف‌های مقابل منتقل کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149685" target="_blank">📅 14:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149684">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
نقدعلی نماینده مجلس: مهدکودکم حضوری شد، چرا مجلس حضوری نمیشه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149684" target="_blank">📅 14:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149683">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BO8SnO57ofXVxmd7dcNKXA2j64_JPw9QCjb3RhRlOq8yUu_7J_4n3kagP_59i6uXCjFBjWMi42V7LOb5QHCYgrUedOAr64mhVgo4dWz3aNLHm0SZO-hXkQr66KqwJqbaxS0eGrO7dqY6l8uqJ5FgOna6aLvUJas9v2mCYL8jXUd1qzK5HNTyvF2vdjuP5sZf494ANAc6wPrcPOcls7wFmfozG2lhPmHC4OmVQD3o4u7SPKojFahgCeAiFN31kqritbJifMlJ17KYEYFQGzgBdC8rzSytz_2balSa4Up2foyLhXhaSvlwTXuVRASsDST_am4GPo7oDaU1c-lLvntPfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همزمان با حملات هوایی سعودی که به کشته شدن و زخمی شدن حدود 50 نفر منجر شد، یک هواپیمای سوخت‌رسان بریتانیایی بر فراز دریای سرخ برای پشتیبانی از هواپیماهای سعودی فعالیت می‌کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/149683" target="_blank">📅 14:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149682">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ugaim_Vw8TDIV1xlCXBuTLVErH0-Hy3oSEbAO8tTiWEXk1QXHhFJMHkwRGRGBC3yprwu39pUcjvUbDdo1LKbLbZ_NaVuDsdUeUO6TXjrAMukh1xNMpnHsqQV2O4bIeyWtdGpd8V5aJGIv-LSGm39heepIDitEYQKZp6pelgMOKXwEYwNH_aDfhtacyNl1N8Chg9Gr4GbPRvn9OHrRD9E7Hmu0tKrOA4aiQkej5WjkbnWm89IK7G-eBFXTTWtcaZXXyjDs02djeaCXbMk82rJetvRvEyw5rYGfRvY-b5AtJN0Lrw5-DMisYrGPme8smCjMxyLMUQpeYCiGp4n-kFpZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سپاه: شکار دومین زهپاد [زیرسطحی] ارتش آمریکا در تنگهٔ هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/149682" target="_blank">📅 14:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149681">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
وزیر انرژی امریکا : روزانه حدود 13 میلیون بشکه نفت از تنگه هرمز عبور می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149681" target="_blank">📅 14:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149680">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmtnrTMAzrAfEUymVtATLB1DLJLMco8RQfDbjbtg_ZjLwxvauXiyo71jKFR83v_ocuumL2LBZ_Klx1J_AWknlyL0JdoWGxAOotKB-32Bpy8_HNyvqaO98JnLKVju_8-QsivSF1mb_fshM_xD-X8BQmAMSGzAM3FDQxC4BeOe7ZNnnH49xINWpn1AytuAgLNKTG-bU34-1_IIV-Rqg1fh9VgknjrbRtSA3FNlsG8AKoFiYmej5xk0ZQcbn6fTA5xXLzH2M0dfQDtaMZpB7dSyPmgKT9ThTB12hHReAhOjsVQ71WtAfBlc9qRAlhPMhk9GfEPop3xL2QMIRA6j1arQrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نامه میلی گلد به محسن رضایی: بانک مرکزی یک تن طلایمان را نمی دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/149680" target="_blank">📅 13:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149679">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
بی‌بی‌سی: در پی اعلام «حادثه بزرگ» در نزدیکی پایگاه هوایی سلطنتی فیرفورد (RAF Fairford)، پایگاهی در بریتانیا که میزبان نیروی هوایی آمریکا است، چند مرد بر اساس «قانون مواد منفجره» بازداشت شدند.
🔴
هم‌زمان با بررسی چند خودرو توسط متخصصان خنثی‌سازی بمب ارتش،…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149679" target="_blank">📅 13:51 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149678">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
امیر حاتمی فرمانده ارتش: جنگ هنوز به پایان نرسیده است و ما باید برای وارد کردن ضربات قوی به دشمن آماده باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/149678" target="_blank">📅 13:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149677">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/099d500c99.mp4?token=tOwJsgBSd4akysPc77gYr5asnUqkAsr4auOPu5axus6MreXu4el8RTwfcYwrv-KNv5hYC1mc2aLUMxS--FFA4ue0S452FMh6Ob_fWtEZnoHIWJbnNAHT65LqKBkCGFOzo89Ldtpzeq_5JZIMfOOOz_86ItR1O5HXTuGsbILf82NQ-cUXFTD0Evw8G5gGT1zVkMkcCSvXPirakghu9i4L_bLUMdToxp1MjHeoXxSG-NYRznZMN2fm0Sc78-dafIlZ1F2QaJ8ZWDlmIuRe4YgTfJzDDLZIm3phpvQsrm3efIc8TX2ZmCLH_5ok5lToJkIL599yZdflgix2Fdwsd8L0lLa8AlaVnhzac4X1lsljwJI1qI5NKI7djCQTiZXUcDYkLvN3cC6hbAGOYULSyZG6X7g0aRuRMQpuk7_LfYIBeeZjd4TBoONI9U7TzjeOMb_0PRobEy4XghjLpVNLu3_N7KDS9PbBpBW-EmDyi0rUYuqrau81ACbbCCh0cCMBUeRzwwr1sHGoeqQqVtx0o7QPUNZ4tlOKibq8vmrzjCV9LGIVftjRUHGhafidYGdPNgmt795p8n-KHN13okDbCj8Gbx_UzVXal_8MlCLst6LuJd3ykP2DSgMLTpaO56sBf02wUHZ2rqqJ0KbSlV0RWsrJXRH-_24K1gJu79Gp65S00y0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/099d500c99.mp4?token=tOwJsgBSd4akysPc77gYr5asnUqkAsr4auOPu5axus6MreXu4el8RTwfcYwrv-KNv5hYC1mc2aLUMxS--FFA4ue0S452FMh6Ob_fWtEZnoHIWJbnNAHT65LqKBkCGFOzo89Ldtpzeq_5JZIMfOOOz_86ItR1O5HXTuGsbILf82NQ-cUXFTD0Evw8G5gGT1zVkMkcCSvXPirakghu9i4L_bLUMdToxp1MjHeoXxSG-NYRznZMN2fm0Sc78-dafIlZ1F2QaJ8ZWDlmIuRe4YgTfJzDDLZIm3phpvQsrm3efIc8TX2ZmCLH_5ok5lToJkIL599yZdflgix2Fdwsd8L0lLa8AlaVnhzac4X1lsljwJI1qI5NKI7djCQTiZXUcDYkLvN3cC6hbAGOYULSyZG6X7g0aRuRMQpuk7_LfYIBeeZjd4TBoONI9U7TzjeOMb_0PRobEy4XghjLpVNLu3_N7KDS9PbBpBW-EmDyi0rUYuqrau81ACbbCCh0cCMBUeRzwwr1sHGoeqQqVtx0o7QPUNZ4tlOKibq8vmrzjCV9LGIVftjRUHGhafidYGdPNgmt795p8n-KHN13okDbCj8Gbx_UzVXal_8MlCLst6LuJd3ykP2DSgMLTpaO56sBf02wUHZ2rqqJ0KbSlV0RWsrJXRH-_24K1gJu79Gp65S00y0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظات اولیه حمله سعودی که بازار تعز در تقاطع الماوية را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149677" target="_blank">📅 13:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149675">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DXTMNKpQyWIzNlf5oBL72gIBhbjzIN-4akl4NnMhP9hDs88ZyH9h5BZsEOftdF1qCzdh1CRf1VFGsvNdZJgmy7XoqlnOTg-anNQvlLkPB4dPA7EIdZAX6OUQD6OKWdTHfSzyKWUhziCbYwnqNQrPM1ZZ9oS5RRr1fPXyvXXbVSM3Pa-ldgNVUnZJE3oPHa_69s6Pyy76cyzF950I7kJ3UFh3jq_n62RUAHXlVSw52UkIYQ_GgwGAI5ahnocAMVLf4sh9K4o2Kq8SuKUkDcLk3TxiX4LLJjzUdr-pS4dDUubzbOQttliW59KGyJtUPp3NHryyU1ZivDoUODIUlY3Aaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Af2dmPtR3xs7k2ZuN1mkn-7-UdkgA8yoRb_MsmUWC9pKoSW70SAZoMnTpPNz7IZGtZ2bFcsc9lQMlSP4zMNmUR9oJOTRw9qr1nSZINYEt_Bg5vl0lGtnK9qT9DviRQEkydqA8yoBugxfIfCxn3pAlLqoRsPjUB7Gj0uwWPI-9coE7s_57gPiEHZoBjvDa1MsT50ke2yiwBMti7OJ3GLHsHYVO_hqEVtvP2G47PuO8xxrh13u_FlO3uHFkQ7h6xJQTNf0QM-WEeoppgBoOS1A0J5t551KoeYyk_96Z9QskK89PQmCKN6BRM6jx2QTJRhLoqAL5Q9Z-z2Ml2ADzq2_RQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله‌ای هوایی گسترده از سوی نیروی هوایی عربستان سعودی، زیرساخت‌های مدنی را در استان تعز در یمن هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149675" target="_blank">📅 13:36 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149674">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
نیروهای هوایی عربستان سعودی با سلسله‌ای از حملات، فروشگاه‌های تجاری در منطقه "المؤسسة الاقتصادية اليمنية" در تقاطع "ماویه" در منطقه "التعزیه" از استان تعز را هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149674" target="_blank">📅 13:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149673">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
حاجی‌بابایی، نماینده مجلس: ایران باید با قدرت [مسیر] انرژی را بر روی همه ببندد؛ یا همه یا هیچکس
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/149673" target="_blank">📅 13:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149672">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841e48be90.mp4?token=obszE5lK-Ai4HqgH81OfHeBXFc_Smu_cibCTKUOegqaqh5RSAglkeBgnwnetWVXj33GosigvWS2eq8cmax71Kg2BhGRT56EZO_18Dz_65iRd5cPXbuI7-Pmm3KOyt9vvGGL3hccRER_5kFks26UAAtlRNQQ--udtlFh9C_cwhjBVcYR-4BTgD4Y8__830hOUWHhi9EV6zaWw1mdBEORS86lOWZltpACsPEek-9n7fKNJXHea9Voofnq9t3cMBAomO0ljNo_U82ddL5UhVuZKXTz5nFzSSKsNbGu_wpYuZMjqynLcSDZ0Hnto9MqeYHsa1teofmaaQG2qN_5popzy1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841e48be90.mp4?token=obszE5lK-Ai4HqgH81OfHeBXFc_Smu_cibCTKUOegqaqh5RSAglkeBgnwnetWVXj33GosigvWS2eq8cmax71Kg2BhGRT56EZO_18Dz_65iRd5cPXbuI7-Pmm3KOyt9vvGGL3hccRER_5kFks26UAAtlRNQQ--udtlFh9C_cwhjBVcYR-4BTgD4Y8__830hOUWHhi9EV6zaWw1mdBEORS86lOWZltpACsPEek-9n7fKNJXHea9Voofnq9t3cMBAomO0ljNo_U82ddL5UhVuZKXTz5nFzSSKsNbGu_wpYuZMjqynLcSDZ0Hnto9MqeYHsa1teofmaaQG2qN_5popzy1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر بیشتری از حملات هوایی عربستان سعودی که استان تعز در یمن را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149672" target="_blank">📅 13:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149671">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
پزشکیان: چیزایی که تو سازمان ملل گفتم کار من نبود، خدا بر زبانم جاری کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/149671" target="_blank">📅 13:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149670">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
نیروهای دفاعی افغانستان اعلام کردند که 28 نفر پس از عبور از پاکستان به شرق افغانستان کشته شده‌اند و افزودند که بیشتر این افراد، اعضای سابق نیروهای امنیتی افغانستان بوده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149670" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149669">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8e72d805d.mp4?token=EFO6YOzE899OqYG9WwbCmMJWTd1yY9JY4Cyk5DZl78D_FGg37zaOQjsdic9fMXDwW0BI9TIKKLT_AX_PDjoYHWs9AGr0XFXcYXFPiBQ0o7uYOzzR7wX3V-biBYQ50DBnJmRpuezatOiyhyC5y9fVqHXCIyk8HTZmZVCn2pqEzdZfmja1W_nkryRNiHaOZGr6MFytn35bpDIJ86NSeqtcDfqSZUGL8yjbj0_O1yOtJSfrv0eXbQ-aSZzAZWhrZZtd1tZLRLU8Zdh9_2qb0C4GWY1C9_J_WRNMlsLiMhCsSREE1GCsiYLtcia0B3j1O2t8IJI2ttVImaFnLz8QvAN39g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8e72d805d.mp4?token=EFO6YOzE899OqYG9WwbCmMJWTd1yY9JY4Cyk5DZl78D_FGg37zaOQjsdic9fMXDwW0BI9TIKKLT_AX_PDjoYHWs9AGr0XFXcYXFPiBQ0o7uYOzzR7wX3V-biBYQ50DBnJmRpuezatOiyhyC5y9fVqHXCIyk8HTZmZVCn2pqEzdZfmja1W_nkryRNiHaOZGr6MFytn35bpDIJ86NSeqtcDfqSZUGL8yjbj0_O1yOtJSfrv0eXbQ-aSZzAZWhrZZtd1tZLRLU8Zdh9_2qb0C4GWY1C9_J_WRNMlsLiMhCsSREE1GCsiYLtcia0B3j1O2t8IJI2ttVImaFnLz8QvAN39g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) اعلام کرد که در حملات جداگانه در نوار غزه، دو عضو حماس را کشته است
🔴
در نصیرات، «ابراهیم فوزی اسماعیل محسن» که به گفته ارتش اسرائیل فرمانده یک دسته از یگان نخبه حماس بوده، کشته شد.
🔴
در حمله‌ای جداگانه در خان‌یونس نیز «محمد کامل سلیمان محسن»، از اعضای شاخه نظامی حماس، کشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149669" target="_blank">📅 12:53 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149668">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
عباس عبدی به یک سال حبس محکوم شد؛ توقف دوماهه فعالیت روزنامه اعتماد
🔴
خبرگزاری فارس گزارش داده عباس عبدی به یک سال حبس تعزیری محکوم شده و دادگاه همچنین حکم به توقف دوماهه فعالیت و انتشار روزنامه «اعتماد» داده است.
🔴
براساس این گزارش، متهمان نسبت به رأی صادرشده فرجام‌خواهی کرده‌اند و پرونده برای بررسی به دیوان عالی کشور ارسال شده است.
🔴
بنابراین این احکام هنوز قطعی نشده‌اند و نتیجه نهایی به رأی دیوان عالی کشور بستگی دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149668" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149667">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/439e435273.mp4?token=t5oAgNsO4Nc5o_1xORQt2dr6K0ydDTA2fGIQHKZmIax8bvwFQN-5qTwQ0u31QiO6g4DG0x4NJEd2xYU6sjdkHYxjblKn34Xrv-IvxqVCa6iFgTAP3oMHXZdvLlGZ1_U7B9D7Zqo1xM7zXk-Z66FdWpSz8UL_aCmBn0TGw68vop6PSVFTzXV5aMtFwbu1eXUpglQEloRJk8oxRU18OaU57b476DSu-DtanmsxFNZowDOcmZnnDzJNp7wECpfIqu_o5bqULB_4aW59IDBUWPJxx1stcWCPV34eJVlxZ7iB7FNxVn3zwVHCTl0d-d4fYzhlG56O__5-D3Qp3X518R0OXjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/439e435273.mp4?token=t5oAgNsO4Nc5o_1xORQt2dr6K0ydDTA2fGIQHKZmIax8bvwFQN-5qTwQ0u31QiO6g4DG0x4NJEd2xYU6sjdkHYxjblKn34Xrv-IvxqVCa6iFgTAP3oMHXZdvLlGZ1_U7B9D7Zqo1xM7zXk-Z66FdWpSz8UL_aCmBn0TGw68vop6PSVFTzXV5aMtFwbu1eXUpglQEloRJk8oxRU18OaU57b476DSu-DtanmsxFNZowDOcmZnnDzJNp7wECpfIqu_o5bqULB_4aW59IDBUWPJxx1stcWCPV34eJVlxZ7iB7FNxVn3zwVHCTl0d-d4fYzhlG56O__5-D3Qp3X518R0OXjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیک موتوری؛ شغل دانشجوی ممتاز دانشگاه امیر کبیر تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149667" target="_blank">📅 12:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149665">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c69bc7a57.mp4?token=B4aUoMqxm90YTIYuBMFnLHev3OwtHwRk7DizJ67B20uMXdzp_YIhd-W3Ep-8biShKxhvXIfKPuDwL0w1t4vcg1L9srVA03-QfejBcocYsjTu8Gq0fVH0muUgD4cDsHk9txE7TSf-zxkab4HW7RfB6Wv4TnHJIm0DbLjroLTT1oENnxW5IrwUGLMurFyvetpdglTdWvCo5AcL8pf9v5sbwHuiMorjiEOd7ZoHMEvX5FKNYmx4imXv1TyewjOHJ4GQUveE0Xntk0CCH4WOk0skphWYFkdA4v73G_dZrf-MuzCsArfA84qOt02HPlBFfCl8fdyjeFGBNDUKnw8Xzppg1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c69bc7a57.mp4?token=B4aUoMqxm90YTIYuBMFnLHev3OwtHwRk7DizJ67B20uMXdzp_YIhd-W3Ep-8biShKxhvXIfKPuDwL0w1t4vcg1L9srVA03-QfejBcocYsjTu8Gq0fVH0muUgD4cDsHk9txE7TSf-zxkab4HW7RfB6Wv4TnHJIm0DbLjroLTT1oENnxW5IrwUGLMurFyvetpdglTdWvCo5AcL8pf9v5sbwHuiMorjiEOd7ZoHMEvX5FKNYmx4imXv1TyewjOHJ4GQUveE0Xntk0CCH4WOk0skphWYFkdA4v73G_dZrf-MuzCsArfA84qOt02HPlBFfCl8fdyjeFGBNDUKnw8Xzppg1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) اعلام کرد که حزب‌الله بامداد یک پهپاد انفجاری را به سمت نیروهای اسرائیلی مستقر در منطقه امنیتی جنوب لبنان پرتاب کرده است. در این حمله کسی زخمی نشده است
🔴
در واکنش، ارتش اسرائیل از انجام حملات هوایی علیه اهداف حزب‌الله در چند منطقه از جنوب لبنان خبر داد؛ از جمله مواضعی که به گفته اسرائیل برای پرتاب پهپادهای انفجاری و موشک‌های ضدزره علیه نیروهای این کشور استفاده می‌شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149665" target="_blank">📅 12:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149664">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5V2pHuTuzCcLeAX6UMcabOGG_oj_CrkbWmjQB45i_fkfLPi7O78V5vkFBq1lrgrGJMUmjy4cX0nXbnhnpCFcOq078h4EBTO8xzdjDNv_bnu7IFnUTH4KY9BvtgJ81ImT4w-NbP69vZm8WCaSr5iMDT12Z43DrvJGyT3Btji7VUZu1_fZho8dKfdT-ddmfLjXJiQjYQDtIDOC-ZjyjySNLq4qQ2QhGNgSF_V3qg3piFqrg9mrLSRsyiLjQkiXJgNw0kQFMO-hn7Oj84XIqaHRt-GO2sZKUtbifwdhVdyfRxcFl0UnR1gnKAyxP6siRSJUXZhoLukaa0gUk_US6ilug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله‌های هوایی عربستان سعودی، چندین منطقه از استان تعز در یمن را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149664" target="_blank">📅 12:30 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149663">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
رسایی بخاطر شکایت قالیباف و چندتا موضوع دیگه تو سال 1402، به 10ماه حبس محکوم شد  #عروس_زندان
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149663" target="_blank">📅 12:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149662">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
مدیرعامل شرکت ملی نفت ایران:
بر اساس اطلاعات به‌دست‌آمده، اسرائیل و آمریکا برای ضربه زدن به تاسیسات نفتی برنامه‌ریزی کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149662" target="_blank">📅 12:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149661">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
کارولین لیویت سخنگوی سابق کاخ سفید:
گاهی فکر می‌کنم ترامپ شاید بیشتر از مردان به حرف زنان گوش می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149661" target="_blank">📅 12:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149660">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
برخورد قطار با یک عابر پیاده در ساری جان مردی ۳۵ ساله را گرفت؛ علت حادثه هنوز اعلام نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149660" target="_blank">📅 12:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149659">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری / گزارش‌ها حاکی از آن است که پایگاه RAF Fairford در بریتانیا به سطح FPCON Delta، بالاترین سطح حفاظت نیروهای نظامی آمریکا، منتقل شده است.
🔴
این اقدام همزمان با حادثه‌ای امنیتی در ولفورد و بازداشت چند نفر به ظن جرایم مرتبط با مواد منفجره انجام شده است.…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/149659" target="_blank">📅 11:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149658">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdZc48rBgZKhvs2L9Oksg0VUK7E3gFwPuWLBnB5kR1_vX5daARoPCR1Z_XsajrvKM7hiN_BiB88M6cMJplX7GdK5dZdZ4lTlCmlVH7nQeWV2A9u2jEwDsQNI5Hz9jUuxUWiJTUKgsxqsHRWCzwcZU3sfyFqMKySeu678cjjxDh4aLS10P8Jn2Dt4nRlQHjC28G3xNJDaQ40QVM3gbKvULFwtDcbWV0j2aG8UNVtQcez5hdbysq02AQnoeI6rc0yWHfbvAfVNRJxda9exLsiDkcU6ur2TRux6kj7ZqMVwuiXivKqL-E2o23hszcX0Mvh0ROtRWfKc2uKEziMo4toSZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی بخاطر شکایت قالیباف و چندتا موضوع دیگه تو سال 1402، به 10ماه حبس محکوم شد
#عروس_زندان
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/149658" target="_blank">📅 11:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149657">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44476a7f42.mp4?token=jnShu4vI7xXSl1u1KJj8bZO6f_7MdI5iyDLI7kmkUNAAJpQ9EvT3yzapYsh1nrP63DYslJ6iOWi3E_ROlmfthIZz8M64YlJwNg193sbRghMM_3ttAnRCi1F7oemlbUgmdGLrK-kuehG2fDXbaqM2yE2CGuQRsqzg-v91e2o9hf16oukUBHduvA2ihf29YVq_VGsWG5W2aJvfc0svSbjSlfFiS6ehj_8wSeDPIH9CKYPpCAHCor7NWV7RcHj1Un8CrnHgpoAKcRyYAqJJqAK8O13jt0Su6vA2B7ONej0R4Sr02DK5M7PiE8IrckKkgG4fcqlYQzFl3jxhP8b0FlpgoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44476a7f42.mp4?token=jnShu4vI7xXSl1u1KJj8bZO6f_7MdI5iyDLI7kmkUNAAJpQ9EvT3yzapYsh1nrP63DYslJ6iOWi3E_ROlmfthIZz8M64YlJwNg193sbRghMM_3ttAnRCi1F7oemlbUgmdGLrK-kuehG2fDXbaqM2yE2CGuQRsqzg-v91e2o9hf16oukUBHduvA2ihf29YVq_VGsWG5W2aJvfc0svSbjSlfFiS6ehj_8wSeDPIH9CKYPpCAHCor7NWV7RcHj1Un8CrnHgpoAKcRyYAqJJqAK8O13jt0Su6vA2B7ONej0R4Sr02DK5M7PiE8IrckKkgG4fcqlYQzFl3jxhP8b0FlpgoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر دوربین مداربسته از سرقت موبایل یک خانم در پیاده رو
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149657" target="_blank">📅 11:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149656">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b665c32a7b.mp4?token=TiVXCT4oi8Fkq1XnxCCwocCbyEfEXByrF1OzEhk18pCk9RpfPVr3Xdb_fgSTEEyQqJW7JvRs0VEOUr7sbUtaTu7yMgvF72SEwQKx4Q2cGUQpoETfnR7KHp-XOIRfB0KLQpNxmIKHLdgEM3C68QspZZdKPXZV9j_3JOgtHn5xlIjaO01DYk2b_QxkEqiDW2VHy4xoycu0QyBV65F0uWsISim2VvPAsjsb_-H52VP4UZSMrD7JfNz7_cyphDTPt0QM5iItP63aACLMntlb_e3kOFnRlEwKfOmCuAo5w-feYrnCT1qH4ifyzZBEOIVNU3rPW7zDuizSj4zJy1JoU4F38w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b665c32a7b.mp4?token=TiVXCT4oi8Fkq1XnxCCwocCbyEfEXByrF1OzEhk18pCk9RpfPVr3Xdb_fgSTEEyQqJW7JvRs0VEOUr7sbUtaTu7yMgvF72SEwQKx4Q2cGUQpoETfnR7KHp-XOIRfB0KLQpNxmIKHLdgEM3C68QspZZdKPXZV9j_3JOgtHn5xlIjaO01DYk2b_QxkEqiDW2VHy4xoycu0QyBV65F0uWsISim2VvPAsjsb_-H52VP4UZSMrD7JfNz7_cyphDTPt0QM5iItP63aACLMntlb_e3kOFnRlEwKfOmCuAo5w-feYrnCT1qH4ifyzZBEOIVNU3rPW7zDuizSj4zJy1JoU4F38w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که انصارالله یمن طی چند روز گذشته، یک مخزن ذخیره‌سازی نفت را در ینبع عربستان هدف قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149656" target="_blank">📅 11:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149655">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
نخست‌وزیر اسلوونی: تغییر حکومت در ایران برای صلح پایدار ضروری است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149655" target="_blank">📅 11:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149653">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-2vw4RqTwi7hSOD5YXRckRwjnnps3b2qAAtQSmKeYLjspHaCJzgMRUOMaHOO0mPa686FDJfguU_TjWCgd_K8wjC4MeaP_bab-2ha8niMX3AfJO2-TpDr-A0aGR15rznEpxUAUIlcZgEVGmFcRLX7WcvBwsIzOsWVoX8crib7BtPot1fwWvwik8bxB9zHRYzLmrh0TZaEbcfu6cY_gY8h7Rz-VgilJFnMUbcLiO7Eru29XWIVrAjOyLR_oPTCtCkWllG4_qV1FMGzY8L7cldboBFnOK6WczvRDjssH--LQw1qsm7Yj9yqZ99vCGTVX5QnqvoBWDNtnhjnP33pmKhSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f40191a121.mp4?token=N0U4Uv07ZEQalS5soU4Jtj7e2IMnlnwD6amr9rM5veju4g0h5i_wUe8BE_4Qv9N56aHfYzMBrvcj4jk8EpIKCzG-W5KYOBOXYp3Lh_F2GshyweMc9E79LFib1CH4RuCkhTB7OBLwpPONflgLvo42sVyLRgXnO8zz2q7CBR8UhLkdlQCNnymz7ZEQNm_5yEVgXMFoba-o6-QR9WJILdPv3JECpZvMHac6wPlmqgkb0Wyqm9azfP5Lj77O0LznUuNKz1fzC8DtsSNQZkFOg72P9faV1e2Bbox6ka_5Xff13rWUFvmhsF-SFmwdbhdMn0Lo2t3vTRTdu573MSDyHdNF8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f40191a121.mp4?token=N0U4Uv07ZEQalS5soU4Jtj7e2IMnlnwD6amr9rM5veju4g0h5i_wUe8BE_4Qv9N56aHfYzMBrvcj4jk8EpIKCzG-W5KYOBOXYp3Lh_F2GshyweMc9E79LFib1CH4RuCkhTB7OBLwpPONflgLvo42sVyLRgXnO8zz2q7CBR8UhLkdlQCNnymz7ZEQNm_5yEVgXMFoba-o6-QR9WJILdPv3JECpZvMHac6wPlmqgkb0Wyqm9azfP5Lj77O0LznUuNKz1fzC8DtsSNQZkFOg72P9faV1e2Bbox6ka_5Xff13rWUFvmhsF-SFmwdbhdMn0Lo2t3vTRTdu573MSDyHdNF8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دو سال پیش تو چنین روزی حسن نصرالله با 80تن بمب سنگرشکن ترور شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149653" target="_blank">📅 11:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149652">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnpfhqSldZlhbFrDUnFAzJ-DtQVgAfLKxjjyggu5N40eOVmjajmZ7YA9Agew1tOzYVhD-v_OmVX35fqsl2k1IaOxrtgIOb2OKj0yulaGjHaXShxTTW0iREDsbxlXaTqPvpUJ7-zHu1a1UPvTzV2j3yvyufP53CUTNn_wUJOAtwaT2E0LBQOAo5S1ahlMZ-OYz_ncSQstv0jhmcdZ-g6MPijC-rEa_yhtKjInZqFdP3L8Ki8tR15wBDDRzsvcvcoHAKd4S3nzcwq0T_ihArPilcyqmMq1kFt-goI0aVj5cBxGUEeM_h3SOVK-fV277uj3-wVuaFznaROTpo2kO158WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / گزارش‌ها حاکی از آن است که پایگاه RAF Fairford در بریتانیا به سطح FPCON Delta، بالاترین سطح حفاظت نیروهای نظامی آمریکا، منتقل شده است.
🔴
این اقدام همزمان با حادثه‌ای امنیتی در ولفورد و بازداشت چند نفر به ظن جرایم مرتبط با مواد منفجره انجام شده است. چند ملک تخلیه شده و تیم خنثی‌سازی مواد منفجره در حال بررسی خودروهاست.
🔴
سخنگوی نیروی هوایی آمریکا اعلام کرده نیروهای پایگاه در حالت آماده‌باش و هوشیاری بالا قرار دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149652" target="_blank">📅 11:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149651">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VO8E3171TfnYlnNKAFArlJJ0Qw8vV9nVgkdwole_wLupIgK4U3ClhtBO9nBKOrSiyhsmfkdoIcKaCoWKefBCQGoCYtW7lhfo6Sq8UupayeaLKNIO_3cCFu2ZauwuZTw079U1dNw9eCkqhscq7vZG47JLcdDfBA0UQCK9iNgMvQGWs9C9TaDkpEojS84efPBh3_WxAZauUlyz521QCDYou7BE0hPBAYwd-1zOeZrtH4cNok8o5s4bAc-X8oi5HmVbsYX9yWOMeWpiBHfdQ576tdSrfKwFA6tXqwTg5czepgLnudOnPJNeTBdDMNyuKHyXdbHvO7crBEMbOyqEdByIlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی رغم پایان فصل تابستان، قطعی برق برنامه ریزی شده در استان خوزستان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149651" target="_blank">📅 11:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149650">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5BEfmsQaZk-04ZfF3g3nwuheVsgeQxzHqCqaNhuGKvAqwJ881lcb6e6V6ysAxpCWEZMW_C9acUAaFUFRB9wuUOjVLQ1M9WCGitXFg4naxygJbopjnL4LI6dyeBZVCjN56lROwAejgJOvVzaUfJvDzq_ZIu-Jwupe5lhcMxCCmU0TiJGrhW91Dlw0Lk07H4ftHR0dbJxCnwYpRqx_KwGXXPKQIxNuFPIdD8GNKu7WS4fBbuy3mkgn1iBHC2pJD4wLvaSaQnd2Hti77aHGisRZai7xKzPvGYcifjlLdzrcv1CIxRfcvQDm7j9-TKvAae67q5fUDnLtCySbTdSLezg1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گوگل تولید ویدیوهای ۱۰۸۰p با هوش مصنوعی را برای همه کاربران فعال کرد
🔴
گوگل امکان تولید ویدیو با وضوح ۱۰۸۰p را در Google Vids برای دارندگان حساب‌های عادی و Google Workspace فراهم کرد. این قابلیت با استفاده از مدل Gemini Omni ۱.۱ Flash، امکان ساخت ویدیو از روی متن، عکس، صدا یا کلیپ‌های موجود را فراهم می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149650" target="_blank">📅 11:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149649">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/BsPyAYfpZYTgqYrOY8nLtRZiTKon32ugajlN4HbPddusQj44OSU-mKM11UMBIBxBSCFi0YlkmW-3nBWyBCoKhTZz0MCKW0RCSfwm0JD0fIYvDXcZEkGxq1fSraEKXT6AVRcEHuz0npnGuyxhpolWo14j4PfL8BP9Zq90QQy6J0JuVtkr6PFScnf9P4DhD2amaMR4mt_9bZdVdiUJ0AzeyqgB-p06ghrW1IRdLL3zspYMAoc2_oUvOBuU1DNsLnJwiazvLQEZhCRy5lmRAix-RBYbWHfp88Yqco0HKsnJpuw-83e4RvGXR2Q-2OwhAjVSNeB4pPaccoPy7CFqVRU-QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه عبری والا: ارتش اسرائیل در آستانه عید یهودی سوکوت (سُکّوت)، سطح آماده‌باش خود را در کرانه باختری افزایش داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/149649" target="_blank">📅 10:54 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
