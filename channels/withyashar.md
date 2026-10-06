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
<img src="https://cdn4.telesco.pe/file/FY4jGW5iipWAZgJWAhlJPdRrvHjPPbvD858TKvnr9P8BFTJczgAAXu8bbZG7c7YT8pN16ChsEnWY3OpI9tqmrZv-PGBGODVaqtREc0i1aUHuqSGPXqokRpBAoxoWi0oEeq4VmK4Bez-frwRoT2FsHNURNo_oMSO5JOTBlhc-grpXHRD76joFs9TsrCmgF6Se2gl3YkQ1qTgSzGsMDNdOpIsXpRGYesCG9eglFboQnmMTcKySrDodyR0dDYh1no7tTU2x4Rv9ztg1OrwFTpvanV4vDOa2krr_O3XhArhpawvuE3P5iDRPanH1cMoNDoWKyNcaLasIHGY-nJiZZgs1yw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 489K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 17:18:01</div>
<hr>

<div class="tg-post" id="msg-25021">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SX-7C4-JiBT9sDYCvXyn6KsGcNdC_qgQv5-37f8FwSfFR2k5EzS3gZ053bMe-WKGDt4ykscabJmfzyiUxuEvlYEPKuLrQL4-ukKIGAWsGh1R_7F6qKazLvHZdwfCyFy5d59rhfaMbby5TrXOYJv_cx4rLbP-g4vY7rXkPf_OyXgLaug07RKx2A97OFlb0nQtsm1KKH-73yOmC9rZeswW_zDP5-ztHiwPk0XP8_9Gw99IKMWYbZxwK3L7wI_X5A7go-66TsUtP50wvH4Rc9HR6TnQET6_vA8CmX-q6RLDKApREjozgrfbhOL118YX2RjzBbamJ0ptqKV9IGpEpdo75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارت ایران روز فلج مغزی رو به ترامپ تبریک گفت
@WarRoom
البته باید به موشتبی این رو تبریک میگفت</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/withyashar/25021" target="_blank">📅 16:39 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25020">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سفارت بریتانیا در ریاض برای شهروندان خود هشدار امنیتی داد
سفارت بریتانیا در عربستان سعودی با صدور اطلاعیه‌ای از اتباع خود در این کشور خواست با توجه به شرایط فعلی، ضمن حفظ هوشیاری کامل، پروتکل‌های ایمنی را رعایت کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/withyashar/25020" target="_blank">📅 16:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25019">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پلیس بریتانیا یک مظنون دیگر را در پرونده پایگاه هوایی فیرفورد بازداشت کرد.
پلیس ضدتروریسم بریتانیا اعلام کرد یک
مرد ۲۲ ساله بریتانیایی
در وست‌مینستر لندن به ظن
آماده‌سازی برای انجام اقدامات تروریستی
در ارتباط با پرونده مرتبط با پایگاه هوایی
RAF Fairford
بازداشت شده است. در جریان این عملیات، یک ملک در وست‌مینستر نیز مورد بازرسی قرار گرفت. این فرد
هفتمین بازداشت
در این پرونده محسوب می‌شود؛ تحقیقات درباره طرح احتمالی مرتبط با پایگاه فیرفورد همچنان ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/withyashar/25019" target="_blank">📅 16:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25018">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BlvRDhrc1gbhKReCaQb2qVLcI6HAXV4L-fKFW3P3BoZQiJxiEnfxzcyTpTZM9kxbGgTCgHk-w9ZeuIv4nStTdwLVnElYBw6pv_TQ8kw7WlbvXhicwwooR89oqiG0nml3M6zZgoPu1LgEmXldNHFKXetFS7230C0eSvyrv-XT4gZyXB8QKK1hswLftimMXWMabE8YN0la_KJyn3Hzm3t6-G8jAumRDsR9AvaNh2s_TChWEnBrOyF-8U-MJydqeeG0oMxhc4W7UP4m2bAqKndh6xNbpInkE3QZblrkQkqyyGmaGHLdq3aO18UjPS8xFdF9U8cyXUUpmavDDLopa6cGGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقت یاب
سنتکام گزارش سقوط بالگرد آمریکایی در دریای سرخ را تکذیب کرد.
فرماندهی مرکزی آمریکا اعلام کرد گزارش‌های منتشرشده در
رسانه‌های دولتی ایران
درباره سقوط یک بالگرد
MH-60R نیروی دریایی آمریکا
پس از اعلام وضعیت اضطراری، صحت ندارد و
تمام هواگردها و نیروهای نظامی آمریکا در سراسر خاورمیانه سالم و در دسترس هستند.
این تکذیب پس از آن منتشر شد که بالگردی با همین مدل، دوشنبه شب هنگام پرواز در نزدیکی
ینبع عربستان
وضعیت اضطراری اعلام کرد و سپس از سامانه‌های ردیابی عمومی ناپدید شد. دلیل وضعیت اضطراری همچنان اعلام نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/withyashar/25018" target="_blank">📅 16:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25017">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دادستان‌های بریتانیا سه ایرانی را به جاسوسی برای جمهوری اسلامی متهم کردند.
مصطفی سپهوند ۴۱ ساله، فرهاد جوادی‌منش ۴۶ ساله و شاپور قلعه‌علی‌خانی نوری ۵۷ ساله
متهم‌اند بین
اوت ۲۰۲۴ تا مارس ۲۰۲۵
فعالیت‌های روزنامه‌نگاران ایران اینترنشنال را زیر نظر گرفته و برای
تدارک حمله خشونت‌آمیز
علیه دست‌کم دو روزنامه‌نگار، از آنها عکس و فیلم تهیه کرده‌اند. دادستان پرونده گفت هدف،
تلافی انتقاد از جمهوری اسلامی و ایجاد ارعاب
بوده است. هر سه نفر اتهامات را رد کرده‌اند؛ سپهوند مدعی است تحت فشار و تهدید عمل کرده و دو متهم دیگر می‌گویند از ارتباط اقداماتشان با سرویس اطلاعاتی ایران بی‌خبر بوده‌اند. دادگاه در
وولویچ کراون لندن
برگزار شده و رسیدگی به پرونده حدود
شش هفته
ادامه خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/withyashar/25017" target="_blank">📅 16:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25016">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhCm4Jj9UOM9GFRuYDl6X4twEd2wsSJFcOFKyLbDf7vQrpqwjuxm19VWjQzverOHcfNTkYCDp378tovY5mMJtSI-kYP5cbjsZTxWE74v67RxsPnh3Yg3sHRCL9jDMp-aUknhnHPpHExEeSkUFjSXrU3hoMNSWDo5Z3-N38vT4E60IF_IS5JkIAi3U73o9JzOC-9VH1d9GSyTMgK5NhPwUxtAUlgDhbM8lwpWiBFgbxAt6A0RQe3vNs0dwv6_WKyIpVT9DFP0Z_I8N7SHoUF6yuapLCu63-Q5rOdJeeTai2bQ6ZkXlYOMdqXvjOG_vzgqlZdzqJQiZvaCuj_S611Mrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب یک دستگاه آبگرمکن گازوئیلی از بهبهان خوزستان
@WarRoom</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/25016" target="_blank">📅 15:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25015">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28d6cd9fcc.mp4?token=ddOPtvGjxHwWJnRuiPbzgyvg3eTmMSlpiTq1IOrklqAEH-DBWxAwKJllApQ4FGNUvUxDSVPXO6Jmmz7OgXUERUPBi71k0crjV1axa3u-7AOxDbogkGMeSEmypip6IWpGWUrKqTKPEy1IytkZ16gycWUa1vk-YEpbtjeB_gEGvRGRavLLKGMGprjhsaoiOPk-fui46TtGZePOzgjX8Md4PRGpAZCxQv1JOYkiMuq4Lsg1hbO2lvAkeedoC3EiV2WuPq1rk1nGjAmv5X9mAYoUMiJgv5UeigILEYoepPALf9RnNyu0ZTows5RjzXuWSPr407exM5BOVHvQt0wBrupXXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28d6cd9fcc.mp4?token=ddOPtvGjxHwWJnRuiPbzgyvg3eTmMSlpiTq1IOrklqAEH-DBWxAwKJllApQ4FGNUvUxDSVPXO6Jmmz7OgXUERUPBi71k0crjV1axa3u-7AOxDbogkGMeSEmypip6IWpGWUrKqTKPEy1IytkZ16gycWUa1vk-YEpbtjeB_gEGvRGRavLLKGMGprjhsaoiOPk-fui46TtGZePOzgjX8Md4PRGpAZCxQv1JOYkiMuq4Lsg1hbO2lvAkeedoC3EiV2WuPq1rk1nGjAmv5X9mAYoUMiJgv5UeigILEYoepPALf9RnNyu0ZTows5RjzXuWSPr407exM5BOVHvQt0wBrupXXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از ۱۰۰ موتورسوار که از حضور مسلملنان و صدای مسجد در منطقه کلافه شده بودند در روبروی مسجد آنها و در حال عبادتشان گرد هم آمدند تا موسیقی گروه «ای‌سی/دی‌سی» را با صدای بلند برای آن‌ها پخش کنند!
@WarRoom</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/25015" target="_blank">📅 15:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25014">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سخنگوی وزارت امور خارجه قطر : تماس ها و بازدیدها در تلاش برای پیشرفت در مذاکرات بین واشنگتن و تهران ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/25014" target="_blank">📅 15:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25013">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رویترز:
پالایشگاه‌های نفت چین، حجم خرید خود از نفت خام عراق را افزایش داده‌اند تا کمبود عرضه نفت ایران از طریق تنگه هرمز را جبران کنند. بر این اساس، حداقل ۱۲ میلیون بشکه نفت خام عراق و قطر خریداری شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/25013" target="_blank">📅 15:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25012">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b6a1530a7.mp4?token=UnU9oMqis7CdRKEs9xi5UbdCeWZJS9A7SMidVR9jJ2-e21fgpoyE74qTkFA_b0nDFbJ_oHmMpHv_aABWvb_U8jtFZD0qx1pVQLdxoiRMB_0h4Ao7116jUX64tvrJSsyFEMz_v1racWxb07-iFQBG5gGvFXYZHTmvtiPIVNeTgkTPzeCfuGH_wDa7-U0FlZF8oqGuHG17-sH_g6G3nZcKvdk6e9CtBAXNiQdC7zsSlBNHeMg_YInZS4mWe4qe1ftT0ueqn8kV05q7_S0yUNvqiFEPZSS7Sp9ypVanWFyDqgnje-ojHIKVqnHBnbRRh8pEyjIuz7ncNi_YrlRhAKXfHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b6a1530a7.mp4?token=UnU9oMqis7CdRKEs9xi5UbdCeWZJS9A7SMidVR9jJ2-e21fgpoyE74qTkFA_b0nDFbJ_oHmMpHv_aABWvb_U8jtFZD0qx1pVQLdxoiRMB_0h4Ao7116jUX64tvrJSsyFEMz_v1racWxb07-iFQBG5gGvFXYZHTmvtiPIVNeTgkTPzeCfuGH_wDa7-U0FlZF8oqGuHG17-sH_g6G3nZcKvdk6e9CtBAXNiQdC7zsSlBNHeMg_YInZS4mWe4qe1ftT0ueqn8kV05q7_S0yUNvqiFEPZSS7Sp9ypVanWFyDqgnje-ojHIKVqnHBnbRRh8pEyjIuz7ncNi_YrlRhAKXfHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای خبرنگار وال‌ استریت‌‌ ژورنال: سرویس مخفی آمریکا CIA یک لیست از ۵ الی ۱٠ نفر مسئولان ایرانی را به اسرائیل داده که این افراد را نباید ترور کرد چون قصد دارند در آینده، حکومت را به دست بگیرند تا ایران کشوری نرمال شود!!️
@WarRoom
یاشار: این ادعا فقط در همین ویدیو بیان شده و در وال استریت ژورنال یا رسانه دیگری منتشر نشده است</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/25012" target="_blank">📅 14:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25011">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">منابع هندی اعلام کردند یک
کشتی تجاری با پرچم پاناما
امروز،
۶ اکتبر, ۱۴ مهر
هنگام عبور از نزدیکی تنگه هرمز و سواحل عمان هدف یک
پرتابه ناشناس
قرار گرفته و
۱۱ خدمه هندی زخمی شده‌اند
. تاکنون هویت عامل حمله به‌طور رسمی اعلام نشده ولی این حمله به سپاه نسبت داده میشود.
@WarRoom</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/25011" target="_blank">📅 14:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25010">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">عملیات کاگ‌ب برای ایجاد اختلاف میان شاه و آمریکا:
بر اساس اسناد
آرشیو میتروخین
و
اسناد رسمی وزارت خارجه آمریکا (FRUS)
، بخش «سرویس A» کاگ‌ب که مسئول عملیات فریب و اطلاعات نادرست بود،
نامه‌ای جعلی به نام جان فاستر دالس، وزیر خارجه آمریکا، خطاب به سفیر آمریکا در تهران جعل کرد
؛ نامه به‌گونه‌ای تنظیم شده بود که توانایی شاه را تحقیرآمیز جلوه دهد و این تصور را ایجاد کند که
آمریکا در حال بررسی کنار گذاشتن یا سرنگونی شاه است
. کاگ‌ب نامه را مستقیماً به شاه نداد؛ مأموران شوروی
نسخه‌هایی از آن را میان نمایندگان بانفوذ مجلس و سردبیران مطبوعات ایران پخش کردند
تا نامه از طریق محافل سیاسی به شاه برسد؛ طبق پرونده کاگ‌ب، این نقشه موفق شد و
شاه نامه را واقعی تصور کرد و دستور داد نسخه‌ای از آن برای سفارت آمریکا ارسال و درباره آن توضیح خواسته شود
. سفارت آمریکا اعلام کرد نامه جعلی است، اما طبق گزارش کاگ‌ب،
تکذیب آمریکا نیز در میان برخی محافل ایرانی و حتی شاه باور نشد
و محتوای تحقیرآمیز منتسب به دالس به موضوع گفت‌وگوهای پنهانی در میان نخبگان ایران تبدیل شد.
هدف اصلی عملیات، ضربه زدن به اعتماد شاه به آمریکا و تشدید شکاف میان تهران و واشنگتن بود.
@WarRoom</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/25010" target="_blank">📅 14:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25009">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تلاش شنیده نشده نافرجام کاگ‌ب برای ترور شاه در تهران:
بر اساس اطلاعات
آرشیو میتروخین
، یک مأمور مخفی کاگ‌ب یک
فولکس‌واگن بیتل مملو از مواد منفجره
را در مسیر حرکت محمدرضا شاه به سمت
مجلس شورای ملی
پارک کرد. طبق روایت منتشرشده، این عملیات به دستور کاگ‌ب و با تأیید
نیکیتا خروشچف
انجام شده بود. هنگامی که کاروان شاه از کنار خودرو عبور کرد، مأمور کاگ‌ب با
کنترل از راه دور
اقدام به انفجار بمب کرد، اما
چاشنی عمل نکرد و انفجار رخ نداد
؛ در نتیجه شاه از این سوءقصد جان سالم به در برد. این گزارش در کتاب
«آرشیو میتروخین ۲: کاگ‌ب و جهان»
نوشته کریستوفر اندرو و واسیلی میتروخین آمده است. آرشیو میتروخین شامل یادداشت‌ها و رونوشت‌هایی است که یک آرشیویست ارشد کاگ‌ب از پرونده‌های محرمانه این سازمان تهیه کرده بود و اکنون در
مرکز آرشیو چرچیل دانشگاه کمبریج
نگهداری می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/25009" target="_blank">📅 14:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25008">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اتاق جنگ با یاشار | حقیقت‌یاب: ماجرای موسوم به «طاعون روسی» پس از مرگ یک پژوهشگر ۲۸ ساله در مؤسسه تحقیقات ضدطاعون در ایرکوتسک روسیه مطرح شد؛ اما آزمایش‌های رسمی تاکنون ابتلای او به طاعون را تأیید نکرده‌اند و علت مرگ، ذات‌الریه با منشأ نامشخص اعلام شده است.…</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/25008" target="_blank">📅 13:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25007">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WciHhsDC8Z3NIM-cJfaT6ptQ-vghfUDo3APkGKdw3L4dYxH5Yw-BCHcUh5e28OP6DXN--ZFf09TI1PtBhuuPv3ROtEssdvlaWpQLlAtz8ouitr0WOXX3USoiPXs5yKI3D-UN-zli39wQkNzlY7Ffnox5FmThDe7PMvPHfoIk5YZ8LTz1lDoFWM2gYJbe8QOoqJESn0yibvld9Jh1wOYJww5bm-bGoAf3JNvBMfZbWTAXhwNMKX-zqBKlWuDNCkrz_qSfiWMXcVrP82U6O5jm2DFPR74vojvqdaC8RqpZSFRot247zw6OpJON4SCpT2AKML5GmzVI4FLO3tnR5TYfrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران اعلام کرد در واکنش به اقدامات آمریکا علیه نفتکش‌ها و شناورهای ایرانی، نیروی هوافضای سپاه با موشک‌های بالستیک به دو ناوشکن آمریکایی  DDG119 - USS Delbert D. Black و  DDG53 - USS John Paul Jones  حمله کرده است. سپاه مدعی شده این دو ناوشکن که به…</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/25007" target="_blank">📅 13:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25006">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/230bdf5772.mp4?token=G6B9esnM1IVQocNDTKTyJ0DfMDD_Fot97wGZ5Cwsd-uy7dg7Jup9KDlClOxcDXUDFrspRPg6B1DsxWTCHHe4VneSRVXjV6toEpaY9qxtEqgiqS-OmS6hvCVb_NbTha4NP25p2VrfQXHpO81yjVJloj2p2DV8rFQgUnekLoA37IYj8OzfrlelfRhOlVwBHEG1nEPZqdWZFdCGC0_13qCocDYc1zAQSVfwDwAMkhV7ItC-dHU0wcwjJFm6YTPiEotXqjYMxeTB-k8S4ae9AjuNscmHiBXY0g0fXqSqcwBj4I4vhuwtNQlq01LXcHyqVEbg6LEkg0_nvVCcyb9njI3CzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/230bdf5772.mp4?token=G6B9esnM1IVQocNDTKTyJ0DfMDD_Fot97wGZ5Cwsd-uy7dg7Jup9KDlClOxcDXUDFrspRPg6B1DsxWTCHHe4VneSRVXjV6toEpaY9qxtEqgiqS-OmS6hvCVb_NbTha4NP25p2VrfQXHpO81yjVJloj2p2DV8rFQgUnekLoA37IYj8OzfrlelfRhOlVwBHEG1nEPZqdWZFdCGC0_13qCocDYc1zAQSVfwDwAMkhV7ItC-dHU0wcwjJFm6YTPiEotXqjYMxeTB-k8S4ae9AjuNscmHiBXY0g0fXqSqcwBj4I4vhuwtNQlq01LXcHyqVEbg6LEkg0_nvVCcyb9njI3CzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو: «معجزه‌ای که امروز جهان شاهد آن است این است که حتی بعضی از کسانی که ما را محکوم می‌کنند، در دل خود می‌گویند: «وای، ادامه بدهید، ادامه بدهید!» چون خودشان چنین قدرتی ندارند.»
@WarRoom</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/25006" target="_blank">📅 12:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25005">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d6a47346f.mp4?token=BA7gok026wLXJTldqznB_9tQ69e_dMdMq7sb-J05VstWosYHIYf7YAKAuzBF261MHGWsVRKBb-6xcsBWQh5F0E0N23UnK0vKa96pI0kpl8JHtyOXT6-Lxwj3AdSmhfg9zn0H0iBIbbvKwy99xeF4m-lmGlNh4htz1Q0JL7VDvx-y52YgqUtEoGIYQqTNCOrmq3nns8jc_lZgZJZ47LPsaSXrIECCM-iKhiTmhHXnn7CZrlRmm2AgMfyBKjchEC8k2ykScsw8RyW4PR08n9g9A5aCjZ-DJFNjKgZno29XIwnBsmeYJ16Su288tTAaEQP2HDENS2yC9af7MZsIsBjf4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d6a47346f.mp4?token=BA7gok026wLXJTldqznB_9tQ69e_dMdMq7sb-J05VstWosYHIYf7YAKAuzBF261MHGWsVRKBb-6xcsBWQh5F0E0N23UnK0vKa96pI0kpl8JHtyOXT6-Lxwj3AdSmhfg9zn0H0iBIbbvKwy99xeF4m-lmGlNh4htz1Q0JL7VDvx-y52YgqUtEoGIYQqTNCOrmq3nns8jc_lZgZJZ47LPsaSXrIECCM-iKhiTmhHXnn7CZrlRmm2AgMfyBKjchEC8k2ykScsw8RyW4PR08n9g9A5aCjZ-DJFNjKgZno29XIwnBsmeYJ16Su288tTAaEQP2HDENS2yC9af7MZsIsBjf4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو: «در دنیای غرب امروز، در جوامع دموکراتیک، آنها هم انتخاب دیگری ندارند؛ اما نمی‌جنگند. ما هم انتخاب دیگری نداریم، اما
می‌جنگیم
.»
@WarRoom</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/25005" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25004">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نتانیاهو در اکس: «ما ایران را عقب راندیم؛ مأموریت را هم به پایان خواهیم رساند.»
@WarRoom</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/25004" target="_blank">📅 12:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25003">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">استیضاح عراقچی در سامانه مجلس ثبت شد
@WarRoom</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/25003" target="_blank">📅 12:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25002">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وزیر کشور رژیم جمهوری اسلامی , اسکندر مؤمنی برای شرکت در مذاکراتی وارد دوحه قطر شد هم زمان ۶ سوخترسان و جنگنده های آمریکای با تمرکز بر تنگه هرمز در حال اسکورت کشتی ها از مسیر جنوبی تنگه هستند @WarRoom</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/25002" target="_blank">📅 12:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25001">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">شبکه ۱۲ اسرائیل : همام الهمامی، کمک‌خلبان عمانی در بازجویی جدید گفته است او قصد داشت هواپیما را طبق روال عادی برای فرود هدایت کند و در ثانیه‌های پایانی، زمانی که دیگر امکان رهگیری وجود نداشته باشد، هواپیما را به ساختمان ترمینال فرودگاه بنگوریون بکوبد.
@WarRoom</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/25001" target="_blank">📅 11:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25000">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8573ef2225.mp4?token=Jlz1DeBREEfEKbrVMSDLrfOnQnGaZEjwhCQmoqvcz-QsMLbwtcai9HR3_2JtcgphKqpnznNL8h5cQcS5li6_gsAOP-C35RLbpzPRvKZ4qbRTXgDmUIxZ7FTHMly5__4tZdIzo4ZMHHXsF86881y1gOJQ2FPu1p-rNiGFV_2-OEMbus-KMza9ZkuYiVp8HuWKbeb2qR-TLTeDSTJpSaiI-z4Wtd1PXcGVKJu-ilIcI8550zlQpUyXpPbmHbAclghA_u0PBR06OvLkdUqh9wO8FYkDDRQhS_rR5Wx-dqm45aFuhMKdeyL84ti69TLCSShhpx83zceer5n1JCMiSn9APg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8573ef2225.mp4?token=Jlz1DeBREEfEKbrVMSDLrfOnQnGaZEjwhCQmoqvcz-QsMLbwtcai9HR3_2JtcgphKqpnznNL8h5cQcS5li6_gsAOP-C35RLbpzPRvKZ4qbRTXgDmUIxZ7FTHMly5__4tZdIzo4ZMHHXsF86881y1gOJQ2FPu1p-rNiGFV_2-OEMbus-KMza9ZkuYiVp8HuWKbeb2qR-TLTeDSTJpSaiI-z4Wtd1PXcGVKJu-ilIcI8550zlQpUyXpPbmHbAclghA_u0PBR06OvLkdUqh9wO8FYkDDRQhS_rR5Wx-dqm45aFuhMKdeyL84ti69TLCSShhpx83zceer5n1JCMiSn9APg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏سخنگوی ارتش اسرائیل: یک تونل به طول یک‌ونیم کیلومتر را در شمال نوار غزه منهدم کردیم. عملیات برای نابودی زیرساخت‌های زیرزمینی در این منطقه ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/25000" target="_blank">📅 11:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24999">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏اداره فدرال حفاظت از قانون اساسی آلمان : تلاش جمهوری اسلامی برای دستیابی به فناوری آلمانی مورد استفاده در ساخت موشک و سامانه‌های پرتاب افزایش یافته است. حکومت ایران برای بازسازی زرادخانه و تاسیسات آسیب‌دیده خود به دنبال فناوری‌های غربی است.
@WarRoom</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/24999" target="_blank">📅 11:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24998">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwdxvjAxyApbQZ0M4S5WCh_u0wBYF7NM_8V3xwwy4zyWWgHvtpjCBSCXTj60KrnUINKKIncMnwa5NdEAjKRzLX_uCThXmrrF2OdSuIClVvyRndHIsOKSpTdaKycPxrqK73T6KbVqB8zv35qvQkDeY_m_fEwaYh3hczD32VDoxr6OFylW5K79l9Q5FmhTk3-r1NydmG6PNisJ-2vzH4d8fcA9_U6IuBsql_ixavleshuC1hkbhhC-SgFGZnxw6AL_47Kt5oQicvakhRKD9ixltLtpFdLSI3kusP9_FM8gFCVOdsrgACQ2B9ZLBa9HkL93B-dhZlL4MB9-T2W3wriTwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت آموزش و پرورش ترکیه تو جلد کتاب درسی جدید خودش، تمام مناطق شمالی و شمال‌غربی ایران رو، جزو نقشه‌ی "دنیای ترک" قرار داده.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/24998" target="_blank">📅 11:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24997">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بلومبرگ: دست‌کم
۵۰ نفتکش حامل نفت ایران
همچنان در نزدیکی سواحل ایران متوقف مانده‌اند و تعدادی نفتکش خالی نیز در نقاط مختلف اقیانوس هند و اطراف سریلانکا منتظر هستند و به سمت بنادر ایران حرکت نمی‌کنند. دست‌کم ۱۱ نفتکش حامل محموله در شرق جزیره خارک لنگر انداخته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/24997" target="_blank">📅 11:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24996">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24996" target="_blank">📅 05:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24995">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24995" target="_blank">📅 05:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24994">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3258eb63.mp4?token=rEsQcknV2u-6UOToqNCKUWdPayi697b2zynHyjbI6Ta0blblRmguLP7RCwUSwtZuDuk0lptss3qLz_9mlE04rO6kIk6ACIjw8XdMky1Y2zk8gib-_ZQgmvhQLnZqaeRLY2eQVMDdMdKwdHYvOXeUb7r6r-XCzhkH8k2KQ2epW9prBCbklVvuzJjIYBSUqx2g69n88Sn48Hiw4ttPCmJGDMn6uwewV-MR66sLtdV04tLuR7xq5Q7NF4wAo1W7bPWylY0asj_hb-V4OycCMuNWdb7Um-DrOB45EZbTFhYHhw9JgnlY16oq_qRaOAwTUsfLUfFzMtL_5jIprpj_LXx3gGy5rJmcNkhZHFT3fZwF5G4BF2yuwWR3QPxzoLgqPeyGM-m73s3k7uzs7HcQasgkGd7rKRiPeD5nL_ZKVN7ag1AZTTRYxlLo5yAS0cxUrwgLzf1IEBZJs04VG9jq9ufTjVVkausUsN3KVawOjfV8k96etSlZc9QYNLqZKMecFyHquDAvRwvqAa4vASQZm6wcaevcki0STiIIG5liMin0iEdGaVOmxKuJjG_Y19EHhkQdf-tiUiswhafGSkJcxV2wi4mSc8AWhtT4tEKI7Rhd_eQDQhY9WjeGaCqKCJba5mjPNIMJ7vkZ6-8Jy9imYRlQZkP4gK9fci52icvIBoiwL7Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3258eb63.mp4?token=rEsQcknV2u-6UOToqNCKUWdPayi697b2zynHyjbI6Ta0blblRmguLP7RCwUSwtZuDuk0lptss3qLz_9mlE04rO6kIk6ACIjw8XdMky1Y2zk8gib-_ZQgmvhQLnZqaeRLY2eQVMDdMdKwdHYvOXeUb7r6r-XCzhkH8k2KQ2epW9prBCbklVvuzJjIYBSUqx2g69n88Sn48Hiw4ttPCmJGDMn6uwewV-MR66sLtdV04tLuR7xq5Q7NF4wAo1W7bPWylY0asj_hb-V4OycCMuNWdb7Um-DrOB45EZbTFhYHhw9JgnlY16oq_qRaOAwTUsfLUfFzMtL_5jIprpj_LXx3gGy5rJmcNkhZHFT3fZwF5G4BF2yuwWR3QPxzoLgqPeyGM-m73s3k7uzs7HcQasgkGd7rKRiPeD5nL_ZKVN7ag1AZTTRYxlLo5yAS0cxUrwgLzf1IEBZJs04VG9jq9ufTjVVkausUsN3KVawOjfV8k96etSlZc9QYNLqZKMecFyHquDAvRwvqAa4vASQZm6wcaevcki0STiIIG5liMin0iEdGaVOmxKuJjG_Y19EHhkQdf-tiUiswhafGSkJcxV2wi4mSc8AWhtT4tEKI7Rhd_eQDQhY9WjeGaCqKCJba5mjPNIMJ7vkZ6-8Jy9imYRlQZkP4gK9fci52icvIBoiwL7Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رقص و قر تمام کننده ترامپ
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24994" target="_blank">📅 05:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24993">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ca302cfb.mp4?token=hfv5JC4w-h-1Dcp_agWrELaQ-j0SiV72NxEmpOR7Tg-W97cBWRrqKtdX0d70eHiMJixoLV4FVl5eUEHpfZ0Pn0QTUVTOBNMnnIwgCjK1p-T5zcCQ2SkL1wwuS_IVynyIBZ3eHd1VB_4g1iQ5gxhhFzkZOllK8F2Pwi3DArT6YSJFR7WG6144RhRLQDNjVQ144QV4bvgBBHnoOjnFi5f_mRRjXc_CqV7WbVIFznyXFOIGiv4ZG6EfcNB5N0KMTG3n4dmuF04ZBHe5m4UyH2EW8mb-Dr1iS26ICOonCnjrhBJBALE5hO1SeH7Fqqz9NHzC6CDZAooQQsDPbs7ya30t-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ca302cfb.mp4?token=hfv5JC4w-h-1Dcp_agWrELaQ-j0SiV72NxEmpOR7Tg-W97cBWRrqKtdX0d70eHiMJixoLV4FVl5eUEHpfZ0Pn0QTUVTOBNMnnIwgCjK1p-T5zcCQ2SkL1wwuS_IVynyIBZ3eHd1VB_4g1iQ5gxhhFzkZOllK8F2Pwi3DArT6YSJFR7WG6144RhRLQDNjVQ144QV4bvgBBHnoOjnFi5f_mRRjXc_CqV7WbVIFznyXFOIGiv4ZG6EfcNB5N0KMTG3n4dmuF04ZBHe5m4UyH2EW8mb-Dr1iS26ICOonCnjrhBJBALE5hO1SeH7Fqqz9NHzC6CDZAooQQsDPbs7ya30t-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ: «فقط یادتان باشد، من دارم می‌دوم، باشه؟حقیقتأ به تمام معنا، واقعاً دارم می‌دوم.»
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24993" target="_blank">📅 05:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24992">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571e103bc9.mp4?token=HNmrYhQFWV_EoeaJDdkjGRC0Nf9kAsT2hoVPF4qkCCfWtVXiAUVNv0PQw8UKg7PGCpPAKrlDR7y9LgFhB88NeMTr5MJIB2OQiM-WIuoGyZAvk7VqXJTiYKXWVk4ptqmKlIDIE5O6U7ywZbp4AgJWAgAAlUQvZ9pt0p--trIx_56aFsKR2NL_3f1r7zv9eOIp712wwiPXjSU-JOpfR6p4r53M_3bnQOR1DYmdu3EhsOj8G-T67mbRlt_v9kECjqTG56TqHk6yPU4uf6bZR0MVCzx6rqeLFs48iCTpivTb-ko4ScTHZDXQDzVJIXooVG_7MK0WchyYYk1RgiZP39TDNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571e103bc9.mp4?token=HNmrYhQFWV_EoeaJDdkjGRC0Nf9kAsT2hoVPF4qkCCfWtVXiAUVNv0PQw8UKg7PGCpPAKrlDR7y9LgFhB88NeMTr5MJIB2OQiM-WIuoGyZAvk7VqXJTiYKXWVk4ptqmKlIDIE5O6U7ywZbp4AgJWAgAAlUQvZ9pt0p--trIx_56aFsKR2NL_3f1r7zv9eOIp712wwiPXjSU-JOpfR6p4r53M_3bnQOR1DYmdu3EhsOj8G-T67mbRlt_v9kECjqTG56TqHk6yPU4uf6bZR0MVCzx6rqeLFs48iCTpivTb-ko4ScTHZDXQDzVJIXooVG_7MK0WchyYYk1RgiZP39TDNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره احتمال حمله هسته‌ای ایران به یک شهر آمریکا: «میخواهید بگذارید این کار را بکنند؛ بگذارید لس‌آنجلس را از بین ببرند، بگذارید سن‌دیگو را از بین ببرند؟؛
این
گرانی بهای بسیار کوچکی است که باید پرداخت شود.
»
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24992" target="_blank">📅 05:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24991">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گزارش چند صدای انفجار بندر عباس ۱۰ دقیقه پیش
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24991" target="_blank">📅 05:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24990">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871cf2b90c.mp4?token=SIxMGc736hh_aIBRxy_oD3laHDc56-xjp6wR0Z5FAQ7oi8kHqgQ-UKG4wpDjkBgeZitylPw8os6kYymQXTCOGnKJ7sehH1uej8NKjHkOeL3gBzIENKpeQEQZCwZ42QkK5kwsxzOnvpRHP__M4jcKMNzBIARfhi8Qq16ACNRE3kzOlzTix7RXngtIuno0Vd3tHHqh65n2fECO2ti81coVZFaLkHU2S4w-GKnXMj2_3w6c0Sw8qYCT7gu4PhmKiIiBJ77bnaN4m51cjR_v9jx2P8gzUUCeTS-kvLQLNbQ60_MJmd-4e109gaVI9yLIAmtcovXv21Ziw8x88RscW4Gp-IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871cf2b90c.mp4?token=SIxMGc736hh_aIBRxy_oD3laHDc56-xjp6wR0Z5FAQ7oi8kHqgQ-UKG4wpDjkBgeZitylPw8os6kYymQXTCOGnKJ7sehH1uej8NKjHkOeL3gBzIENKpeQEQZCwZ42QkK5kwsxzOnvpRHP__M4jcKMNzBIARfhi8Qq16ACNRE3kzOlzTix7RXngtIuno0Vd3tHHqh65n2fECO2ti81coVZFaLkHU2S4w-GKnXMj2_3w6c0Sw8qYCT7gu4PhmKiIiBJ77bnaN4m51cjR_v9jx2P8gzUUCeTS-kvLQLNbQ60_MJmd-4e109gaVI9yLIAmtcovXv21Ziw8x88RscW4Gp-IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره عبور کشتی‌های آمریکا از تنگه هرمز: «کار نیرودریای ما حرف نداره ، نفت از قبل هم بیشتر از تنگه عبور میکنه ، هر از گاهی آنها یک موشک کوچک شلیک می‌کنند. ما هم می‌گوییم «بینگ» و موشک را می‌زنیم و نابودش می‌کنیم. به شما می‌گویم، خیلی خفن است! موشک می‌آید، موشک می‌آید، موشک دیگر نیست. تمام. و کشتی‌ها هم به حرکت خودشان ادامه می‌دهند.»
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24990" target="_blank">📅 05:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24989">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دونالد ترامپ: «آنها شیاد هستند. دروغ می‌گویند. ما کاری جز پایین آوردن قیمت‌ها انجام نداده‌ایم و وقتی جنگ با ایران تمام شود، که خیلی زود خواهد بود، قیمت نفت به‌شدت سقوط خواهد کرد.آنها نمی‌توانند سلاح هسته‌ای داشته باشند، چون دیوانه‌اند. این کاری بود که رئیس‌جمهورهای دیگر یا کشورهای دیگر باید سال‌ها پیش انجام می‌دادند. ما همیشه مجبوریم کارهای سخت و کثیف را انجام دهیم، در حالی که این کار باید سال‌ها پیش انجام می‌شد. این وضعیت ۵۱ سال ادامه داشته است؛ زورگوی خاورمیانه دیگر چیزی ندارند همه چیزشان نابود شده است و تنها چیزی که دارد ، تورم ۳۱۰ درصدی است، کار را زود تمام میکنم احتمالا بعد از انتخابات میان دوره‌ای
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24989" target="_blank">📅 04:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24988">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9b95796cd.mp4?token=lX-TjJ4YRMNLlOFIAzS9S4LIWIxrXBN9clVG7kblrcEW6Gb7rJn_9mPQgGQuKv2MKooO2Lsr-aJeABQICDeEeRgKQpyi7VY7UVS7Om9yYDuFbK28Kyb5LeTYCX_nSbp5KeN8WL3JPPnWHyQHxFTYwdJVsRGQZenzUYlLy90amucg-LIm7HojrIEyUt_2vTyAhvoXDPY251u2KzMq6fHjMbkpwmwKt6ORzPCYXAQw7mxIbpSA4_rHpssoSRQ9lbzxzPhLSny9joKlFw3XEu_LF8cekTn2EzpXDsV9246vdy-p1CM-nGDGnlI7QdN6WbkrQrfbwHX5M2gFm0sEJk7-R4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9b95796cd.mp4?token=lX-TjJ4YRMNLlOFIAzS9S4LIWIxrXBN9clVG7kblrcEW6Gb7rJn_9mPQgGQuKv2MKooO2Lsr-aJeABQICDeEeRgKQpyi7VY7UVS7Om9yYDuFbK28Kyb5LeTYCX_nSbp5KeN8WL3JPPnWHyQHxFTYwdJVsRGQZenzUYlLy90amucg-LIm7HojrIEyUt_2vTyAhvoXDPY251u2KzMq6fHjMbkpwmwKt6ORzPCYXAQw7mxIbpSA4_rHpssoSRQ9lbzxzPhLSny9joKlFw3XEu_LF8cekTn2EzpXDsV9246vdy-p1CM-nGDGnlI7QdN6WbkrQrfbwHX5M2gFm0sEJk7-R4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ: راستی، ما داریم به ایران در کونی میزنیم ، اینو که می‌دونید، مگه نه؟
این ماجرا، به هر شکلی، به پایان خواهد رسید. خیلی زود تمام می‌شود و قیمت‌هایتان به‌شدت پایین خواهد آمد
ما خاورمیانه ، اسرائیل و جهان را نجات میدهیم, آنها هیچوقت سلاح هسته‌ای نخواهند داشت
@WarRoon</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24988" target="_blank">📅 04:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24987">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پزشکیان گزینه جدید وزارت دفاع را معرفی کرد.
مسعود پزشکیان،
مهرداد اخلاقی کتابچی
، از مدیران باسابقه صنایع موشکی و هوافضای وزارت دفاع را برای تصدی وزارت دفاع به مجلس معرفی کرد. او سابقه ریاست سازمان صنایع هوافضای وزارت دفاع و گروه صنعتی شهید باقری را دارد و نامش در فهرست تحریم‌های مرتبط با برنامه موشکی ایران نیز بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24987" target="_blank">📅 01:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24986">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">فرمانده سنتکام، دریاسالار برد کوپر: «ارتش آمریکا همچنان با تمرکز کامل بر این مأموریت فعالیت می‌کند و علیه هر کشتی که تلاش کند محاصره را دور بزند،
سریعاً اقدام خواهد کرد.
نیروهای ما آموزش‌دیده، حرفه‌ای و مرگبار هستند.» به تمامی دریانوردان توصیه شده هنگام تردد در
دریای عمان و مسیرهای منتهی به تنگه هرمز
، اطلاعیه‌های دریایی را پیگیری کنند و در صورت نیاز از طریق کانال ۱۶ ارتباط «کشتی به کشتی» با نیروهای دریایی آمریکا تماس بگیرند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24986" target="_blank">📅 00:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24985">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0rfEvo8OxF0rqUiFXLLF5F67JziapP4YYK08yka3RRvnkHa-nTy8jeSSUsioqeA9GbR126tfWhTt89M7zq103GyAIpycTPNw3Aea2sSBFbEkMD9b0WTOSUylgNbyrHrtYi7ALs260dydDiYv1U1zRl3OK_iza_0zRxavbmxbwmbdOSq8NnLAqknBcf9S9NugkC0SiaM2Pd2dHjzMug0oXv329WveJ6lueZI3v2v6VTdHfPS2-tD-MT4BxgwzH3rKDe73UgQ8e7Dld9WEONlKDwjF2xh77QFiTj5yUocHeEO7tAqxntZJSALnNVP_3Ef1b8IvM4MX4S-HnhYcyeFOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام اعلام کرد نیروهای آمریکایی روز دوشنبه
صدوسی‌امین کشتی تجاری
را که قصد ورود یا خروج از بنادر ایران داشت، در چارچوب محاصره دریایی ایران، وادار به تغییر مسیر کردند. از زمان ازسرگیری محاصره در
۲۳ تیرماه
، نیروهای آمریکایی مدعی‌اند
۱۳۰ کشتی
را تغییر مسیر داده و
۳ کشتی
را که حاضر به تبعیت نبوده‌اند، از کار انداخته‌اند. همچنین به بیش از
۷۰ کشتی بشردوستانه
اجازه عبور داده شده است. سنتکام همچنین مدعی است طی ۱۲ هفته گذشته،
۱۳ کشتی تجاری
را که متهم به نقض محاصره یا فعالیت در شبکه چند میلیارد دلاری سایه سپاه پاسداران بوده‌اند، منهدم کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24985" target="_blank">📅 00:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24984">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کانال 14 اسرائیل
: لحظاتی پیش نتانیاهو با روبیو، وزیر خارجه آمریکا یک تماس تلفنی اضطراری و ویژه برقرار کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24984" target="_blank">📅 00:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24983">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c54e4b572e.mp4?token=Uzol0rfGuchVl8_Pj5EUnImY9TezMjaaHNJgQeOmysoLwAgwAvlsoEQMPG6YIwjc1iWNWCFDrw1ZI4-nGaZbib_qxclrOQ1Fadrm7gNi-zDn0mEjOFH0BBy0khGqt14CFkiYUVZHkiwhakQzHqL17DG17HyFWsawspU-wAVbiv2L0-5hwLYUJ1LLfH8yCeynMy_-3CsZjg_OdLVZ5_5b7nuDHsa55B-foguSICd6e0HzlrbxlCufq9daHuljPs24YC9kpeO8HY0f34vk8FbEl8LQAscMy_Gf8zlabmQQ1r6yylDnUcKVSFwjExompnwZv-_p6EqOWfMfigRra8Sqkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c54e4b572e.mp4?token=Uzol0rfGuchVl8_Pj5EUnImY9TezMjaaHNJgQeOmysoLwAgwAvlsoEQMPG6YIwjc1iWNWCFDrw1ZI4-nGaZbib_qxclrOQ1Fadrm7gNi-zDn0mEjOFH0BBy0khGqt14CFkiYUVZHkiwhakQzHqL17DG17HyFWsawspU-wAVbiv2L0-5hwLYUJ1LLfH8yCeynMy_-3CsZjg_OdLVZ5_5b7nuDHsa55B-foguSICd6e0HzlrbxlCufq9daHuljPs24YC9kpeO8HY0f34vk8FbEl8LQAscMy_Gf8zlabmQQ1r6yylDnUcKVSFwjExompnwZv-_p6EqOWfMfigRra8Sqkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی‌های ترامپ: «این جمعیت از معمول بیشتره یا چی؟ دارم جذاب سکسی می‌شم؟ چه خبره اینجا؟ اینجا واقعاً آدم‌های زیادی هستند.»
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24983" target="_blank">📅 23:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24982">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dd3fb47f0.mp4?token=hluEDrz5r2p1bn-FPsz-BDzJH3KHQ41SnLCMi9azIGYBcCu0QFilEx8n0963U5PUYvtDXTB1qi5X8YlpIqcBr5Iterevhx2KtcQ7MLR7eWuYh9_EoVnYHqT6XbYpHevQ_Psi4_MYF5_CRUGs1t_BljoCSqTY8IlO-e0ImSCC4YZ8EF53enwOCjuoPFNFr-hpJ5-o1XPQYbDX_Hw37Qdcnuf0uHeizkgfj9p96yqscCAgKSxNpngAY7QD2heBROc4CRcq52lSarC4CAVqhL9I7HcKeMAYHUOGDrJOoVwhz0I5wk3vUlzvF_8PgxoIuTKfTpDgtNWjGzD92JIF5HSDoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dd3fb47f0.mp4?token=hluEDrz5r2p1bn-FPsz-BDzJH3KHQ41SnLCMi9azIGYBcCu0QFilEx8n0963U5PUYvtDXTB1qi5X8YlpIqcBr5Iterevhx2KtcQ7MLR7eWuYh9_EoVnYHqT6XbYpHevQ_Psi4_MYF5_CRUGs1t_BljoCSqTY8IlO-e0ImSCC4YZ8EF53enwOCjuoPFNFr-hpJ5-o1XPQYbDX_Hw37Qdcnuf0uHeizkgfj9p96yqscCAgKSxNpngAY7QD2heBROc4CRcq52lSarC4CAVqhL9I7HcKeMAYHUOGDrJOoVwhz0I5wk3vUlzvF_8PgxoIuTKfTpDgtNWjGzD92JIF5HSDoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لوکاس فاکس، خبرنگار فاکس‌نیوز: «درباره فلای‌دبی، آیا فکر می‌کنید ایران مسئول این حمله تروریستی بوده است؟»
ترامپ: «بله، شخصاً همین‌طور فکر می‌کنم.»
با این حال، بازرسان هنوز در حال بررسی هستند تا مشخص شود مظنون با
ایران یا یک طرف خارجی دیگر
ارتباط داشته است یا خیر.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24982" target="_blank">📅 23:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24981">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b58bc0dae.mp4?token=utcFrjzSeJv6REC-lR51K_dovMfWAYPJorJFWCbJ2viTZKD4YkM9xyimu1J1U0DcFF9dMsl-LteUomRxmf0aMdJW-n7G8skp5MnOdPKVwKJr-w7mFEXdDtIpa7FZUic-NXldSzS06EbEcgEiICBHckGuaI6Cwf2xk5hqx5Ew3yKBKqx0OxPqPUF56pz9Wuyc3HJbAUmI46xnseQ7NfBZHluSTeVdVUhFDTJmi-bte2VUEd-3SSBuTg-r6S5IyeSsUUuqgk0IP7JwRAJPwT5sR8cdjBpkraMSQgWCOBdqKLKEnKktMIEFrnlceZnvKgBK125LJZxKMbJVEkNKbofcIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b58bc0dae.mp4?token=utcFrjzSeJv6REC-lR51K_dovMfWAYPJorJFWCbJ2viTZKD4YkM9xyimu1J1U0DcFF9dMsl-LteUomRxmf0aMdJW-n7G8skp5MnOdPKVwKJr-w7mFEXdDtIpa7FZUic-NXldSzS06EbEcgEiICBHckGuaI6Cwf2xk5hqx5Ew3yKBKqx0OxPqPUF56pz9Wuyc3HJbAUmI46xnseQ7NfBZHluSTeVdVUhFDTJmi-bte2VUEd-3SSBuTg-r6S5IyeSsUUuqgk0IP7JwRAJPwT5sR8cdjBpkraMSQgWCOBdqKLKEnKktMIEFrnlceZnvKgBK125LJZxKMbJVEkNKbofcIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : فکر می‌کنی احتمال داره که ایران پهپادهای نظامی خودشو به بریتانیا انتقال داده باشه ؟
ترامپ: من نمیتونم راجبش به شما چیزی بگم.
اما اگه اونا اینکار رو کرده باشن، عواقب خیلی سنگینی رو متحمل میشن.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24981" target="_blank">📅 23:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24980">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خبرنگار فاکس نیوز: در کاخ سفید، رئیس‌جمهور ترامپ به من گفت که معتقد است ایران مسئول حمله تروریستی به هواپیمای فلای‌دبی است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24980" target="_blank">📅 23:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24979">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e53e579ac.mp4?token=e7bexvwxnUgGuMPc0KFV1idGhO-IrOpvOrPYLD_OVga-QtyHtvNA1fIwPKwZ5UOYPbgG7kZh9vHMIL-3AGV3o7Pbvr3zwkVAWYo52IBFmfYxCHP8vpJ74pAnmj3t28rDEnJT34ZJWeaDcDY_NjBogMCWcSbcNf4hpxUdVlxObpGWeZFbAZjVRXS5D3yoN55fYZWeU-27XeiIjK1JLw93Wx2aQ2Z-Vxn_BUK8Imy-zgXBMBjDzbvJdaqvXEwkl7SLhnkDN9LeKJNXFdMsi-lAGBs3DCdVukgNvzd-uJGdMxzy0hOjLVGIEchsl-2j7rXg94tKsLpYPk-TL_IcxyQ-R41WHRs0jAz9Oxa6o6i2DVriv_ro70TceTy_6zT-3JB2lY6FbD2qV3yfXxC7OAtNxi18jslTw1hOXIc5APA3olmTLdv0NEb__d3HDqjYZTASKCkz4YZyHDLFqeOWojUou8aWsLN2kpp7pBK7QJLapar6DowsKWS01H5ooApHHxxFPERQdSpTVbz0yvqRy4ixMKoZKENFIenXU844Ys_5zBeHDS1UteAoM98e2xu6unmlkLkCiu-6T5afUJulh75EZTzKvDSMLPimG4QRDlCwwpto943qQbkaXseWm_RZBnTBpbhwnmkRmooY3_tM5xqhknITH_T77tInMW1W77FvLkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e53e579ac.mp4?token=e7bexvwxnUgGuMPc0KFV1idGhO-IrOpvOrPYLD_OVga-QtyHtvNA1fIwPKwZ5UOYPbgG7kZh9vHMIL-3AGV3o7Pbvr3zwkVAWYo52IBFmfYxCHP8vpJ74pAnmj3t28rDEnJT34ZJWeaDcDY_NjBogMCWcSbcNf4hpxUdVlxObpGWeZFbAZjVRXS5D3yoN55fYZWeU-27XeiIjK1JLw93Wx2aQ2Z-Vxn_BUK8Imy-zgXBMBjDzbvJdaqvXEwkl7SLhnkDN9LeKJNXFdMsi-lAGBs3DCdVukgNvzd-uJGdMxzy0hOjLVGIEchsl-2j7rXg94tKsLpYPk-TL_IcxyQ-R41WHRs0jAz9Oxa6o6i2DVriv_ro70TceTy_6zT-3JB2lY6FbD2qV3yfXxC7OAtNxi18jslTw1hOXIc5APA3olmTLdv0NEb__d3HDqjYZTASKCkz4YZyHDLFqeOWojUou8aWsLN2kpp7pBK7QJLapar6DowsKWS01H5ooApHHxxFPERQdSpTVbz0yvqRy4ixMKoZKENFIenXU844Ys_5zBeHDS1UteAoM98e2xu6unmlkLkCiu-6T5afUJulh75EZTzKvDSMLPimG4QRDlCwwpto943qQbkaXseWm_RZBnTBpbhwnmkRmooY3_tM5xqhknITH_T77tInMW1W77FvLkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: «آیا نگران شیوع بیماری در روسیه هستید؟»
ترامپ: «بله، هستم.
شیوع ذات‌الریه، اگر بخواهید این‌طور صدایش کنید.
این بیماری چیزی بود که قبلاً می‌توانستیم آن را کنترل کنیم. اما به‌نوعی این میکروب‌ها قوی‌تر و باهوش‌تر شده‌اند. آنها مثل یک ارتش هستند. میکروب‌ها واقعاً نسبت به گذشته قوی‌تر شده‌اند و چیزهایی که قبلاً برای درمان ذات‌الریه مؤثر بودند، دیگر به همان اندازه مؤثر نیستند.»
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24979" target="_blank">📅 23:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24978">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c5518a59.mp4?token=ieYMoTa5wEQypqkq5OmpbNALmnZQ1auKbBsDYGyvD6ql8XhFwFROIt5h5oVcUMDssMyC9mD7DjMjS1stbT9j982tPz_8pn5TkB4AJur6TMWj-QXEwAjvSU9iIrc9hUN6gf-cFWrTz0rVl7vX2XcWjR87oZ7A89VSIOamJFDltAaW-3HuabLAq6xpB6LeZA1ZRtgtg98hnL5hyyw7eKVeegSxNK-xk2-n7LqtSfHumkhr_Ys8LRqnki2ogeUraL9U0hSOcQx_KHhiE-ceK7SX2Ehn3upDwd5ITJ7stplRtsD3RC00AhmJ7lfsONxlwnyGG1OXNvHQYa0I-wniG1HlBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c5518a59.mp4?token=ieYMoTa5wEQypqkq5OmpbNALmnZQ1auKbBsDYGyvD6ql8XhFwFROIt5h5oVcUMDssMyC9mD7DjMjS1stbT9j982tPz_8pn5TkB4AJur6TMWj-QXEwAjvSU9iIrc9hUN6gf-cFWrTz0rVl7vX2XcWjR87oZ7A89VSIOamJFDltAaW-3HuabLAq6xpB6LeZA1ZRtgtg98hnL5hyyw7eKVeegSxNK-xk2-n7LqtSfHumkhr_Ys8LRqnki2ogeUraL9U0hSOcQx_KHhiE-ceK7SX2Ehn3upDwd5ITJ7stplRtsD3RC00AhmJ7lfsONxlwnyGG1OXNvHQYa0I-wniG1HlBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : «چه تهدیدی باعث شد هواپیماهای آمریکایی را از بریتانیا خارج کنید؟»
ترامپ: «ما به این نتیجه رسیدیم که ممکن است تهدیدی وجود داشته باشد و چرا باید آنها را آنجا نگه می‌داشتم؟ انتقال آنها هزینه بسیار کمی دارد. ما افرادی را که این تهدید را مطرح کرده‌اند می‌شناسیم و آنها
با ایران مرتبط هستند
.»
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24978" target="_blank">📅 23:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24977">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4307e8a523.mp4?token=SsUdPy6OckLApZ6CZmqRHPQMSnEq_uDDeaQnbW0mTrN5MTG1G7JeMM2JKvhWUVIvKLbqYcA2fzu_zHOaaPrUFn2_pFEKF9PD_eAFyGGDUvJw2uPBBXIwu-uWOy3kxniy4Ozhe9Uy8VFh3a041WF5i-lOq7NKNTlii0oTSyOSKymn2PrpwNbzmawdD7-gMsZDD9lY15qCl2-kADEj0d7spUV9KDaH4ZFqwkQ_q5Fes5vYrXptxPBcib6yJz3yxvdQIQLhdyt3uzdfwamOIdThah2CR87pOo6WY00gwP0TchwE3MvQiouRow7FR0GOityWUYCJ4SVQwjo9SkoKizcM9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4307e8a523.mp4?token=SsUdPy6OckLApZ6CZmqRHPQMSnEq_uDDeaQnbW0mTrN5MTG1G7JeMM2JKvhWUVIvKLbqYcA2fzu_zHOaaPrUFn2_pFEKF9PD_eAFyGGDUvJw2uPBBXIwu-uWOy3kxniy4Ozhe9Uy8VFh3a041WF5i-lOq7NKNTlii0oTSyOSKymn2PrpwNbzmawdD7-gMsZDD9lY15qCl2-kADEj0d7spUV9KDaH4ZFqwkQ_q5Fes5vYrXptxPBcib6yJz3yxvdQIQLhdyt3uzdfwamOIdThah2CR87pOo6WY00gwP0TchwE3MvQiouRow7FR0GOityWUYCJ4SVQwjo9SkoKizcM9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: «نظر شما درباره ضدحمله و عملیات تهاجمی عربستان و یمن علیه حوثی‌ها چیست؟»
ترامپ: «همه‌چیز درست خواهد شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24977" target="_blank">📅 22:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24976">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e845f43990.mp4?token=ZpaVFvjqeGHnJ2vA9mTAt4KfX7OmhMRLhWcyqQcgxz4__8n_B4cTgAIGsnXjNEyTKek3keOXRwZDuQOo_27WqJz9w2F_Seho6x5v7gJrFUrkhJv3Izkw_oiI_Z8bHHfsDq4oY6S4xMKzV0Bd89dSytntk4rR08m9pEYS8AesW1yha50px6z6Mh5yleFDiYb3DBLYI9ha7em-mR9W3JFouIE9AdQInPNhjt9z3CfXjUfHyyRBzYMcJo-5A8EjnZ53hiIFV1Rr_Ql3ARCrBoauPJgptaKHtDqJwZh16QGAauhqA211M9AxW1yG-k476xOWC4C3Lzf_Uukvg6GV9nYF3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e845f43990.mp4?token=ZpaVFvjqeGHnJ2vA9mTAt4KfX7OmhMRLhWcyqQcgxz4__8n_B4cTgAIGsnXjNEyTKek3keOXRwZDuQOo_27WqJz9w2F_Seho6x5v7gJrFUrkhJv3Izkw_oiI_Z8bHHfsDq4oY6S4xMKzV0Bd89dSytntk4rR08m9pEYS8AesW1yha50px6z6Mh5yleFDiYb3DBLYI9ha7em-mR9W3JFouIE9AdQInPNhjt9z3CfXjUfHyyRBzYMcJo-5A8EjnZ53hiIFV1Rr_Ql3ARCrBoauPJgptaKHtDqJwZh16QGAauhqA211M9AxW1yG-k476xOWC4C3Lzf_Uukvg6GV9nYF3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره پالایشگاه‌های نفت روسیه: «مشکل، کمبود پالایشگاه‌هاست.
حجم بسیار زیادی نفت از تنگه هرمز خارج می‌شود.
به‌دلیل جنگ، با کمبود پالایشگاه مواجه هستیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24976" target="_blank">📅 22:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24975">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آسوشیتدپرس: آمریکا در حال گسترش بررسی درباره تسلیحات فضایی است و کارشناسان هشدار داده‌اند که نبود مقررات روشن درباره سلاح‌های متعارف در فضا می‌تواند به رقابت نظامی جدید میان قدرت‌های بزرگ منجر شود.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24975" target="_blank">📅 22:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24974">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پیمان مکه فعال شد
وزارت امور خارجه پاکستان: پاکستان، پادشاهی عربستان سعودی و ترکیه توافق کردند که نیروهای نظامی و قابلیت‌های مورد توافق را فراهم کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24974" target="_blank">📅 21:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24973">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ای۲۴نیرز تصاویر جدید و جزئیات جدیدی درباره خلبان مهاجم: او چندین بار در گذشته به اسرائیل سفر کرده بود و قصد انجام این حمله را از ماه ژوئیه برنامه‌ریزی کرده بود. در امارات متحده عربی، مقامات در حال تحقیق درباره کارمندانی هستند که به این خلبان اجازه ورود به "فلای دبی" را داده‌اند. همچنین، بررسی می‌شود که آیا او یک هدف جایگزین را در صورت شکست طرح اصلی در نظر گرفته بود یا خیر، که احتمالاً یک پایگاه نظامی آمریکایی در اردن بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24973" target="_blank">📅 21:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24972">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پزشکیان: هربار بازرسان آژانس به ایران آمده‌اند، مراکز هسته‌ای و دانشمندان ما شناسایی و پس از آن این مراکز بمباران و دانشمندان ما ترور شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24972" target="_blank">📅 20:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24971">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پزشکیان: مشکل ما با آمریکا این است که هر بار به میز مذاکره می‌آییم، بلافاصله جنگ به ما تحمیل می‌شود @WarRoom
🤣</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24971" target="_blank">📅 20:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24970">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYAIBCD9ngXnpm0UugA0N8jKCN_Q_rY7rRjSbF1qLW1bgJ0O-F__wn-aJbDJcFDDxPsePxIKhZQWhwd5VPpKU4evwnxNmmFQsO6cvHv1bbd8RzZSjCiQkgX7qyqnNM4n2fB7358LMFoVE21JzBA8_R6DANrq6zHzqJF8zB6JSMVe5hS1kTIa5-nBreHXp4SnZZlVu_OFiLuUSemh5BStx--Sh890Lq9G7RSL3yiCx7qQCYxi7BhxWD5eGw6Uh1SQZq3HEFCaTAY_uWLH2Z700zEYNf4kySGOYR784ZyMr1H6CC0EOjcYVn1HvnpG14PhVxA_SwntrtnrqZqBo79IVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر امور خارجه ترکیه، حاکان فیدان، وزیر دفاع ترکیه، یاشار گولر، و رئیس ستاد مشترک نیروهای مسلح، سرلشگر سلجوق بایراکتاراوغلو، در ریاض با همتایان پاکستانی و سعودی خود دیدار کردند تا در جلسه کمیته سیاسی، دفاعی و استراتژیک شرکت کنند. این کمیته بر اساس توافق مکه برای همکاری‌های دفاعی تشکیل شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24970" target="_blank">📅 20:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24969">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پزشکیان: مشکل ما با آمریکا این است که هر بار به میز مذاکره می‌آییم، بلافاصله جنگ به ما تحمیل می‌شود
@WarRoom
🤣</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24969" target="_blank">📅 20:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24968">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MoKByFNN67wTOHkIntRp-8sY1vZKVfKDGp9gLhGUkA0imMC8jMpkvGsdhRphSCxUnlrSvwBAhRVguKhdfUFdg5Y1__d4LAk4wkMLDRnF_qlKjg0BCQ-rkQpa42CUXuk2e0Ap5u6aVfAJCeEjKGRf_4vk_4HT-OEn0QGeqBFj5tQ6lyPAJ8ZHwbHI87nanlXk666tuK26-C9Ez6wdc5g95P8GrpTc97eNOuVbO9Tx4m_0TG2KoQlk2EzvjkNQTBpQOm9uEMLRS8bw5z7GWKBAUjbOw6MO2rWcdiBSgWbmwqeW0dVIiQ_vBAG4esYduPvj741fFizrl5P7J55Jx0-EgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : آنچه باعث افزایش قیمت بنزین می‌شود، دیگر تنگه هرمز نیست، چون اکنون تعداد بی‌سابقه‌ای بشکه نفت تقریباً به‌صورت روزانه از آن خارج می‌شود، بلکه این کلمه است: «پالایشگاه‌ها»؛ جایی که پالایشگاه‌های روسیه توسط اوکراین منفجر می‌شوند و پالایشگاه‌های ما در ایالت‌های آبی، مانند کالیفرنیا، توسط دموکرات‌ها تعطیل می‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24968" target="_blank">📅 20:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24967">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اسرائیل هیوم: آمریکا محدودیت‌های عملیاتی پیشین برای فعالیت نیروی هوایی اسرائیل در حریم هوایی عراق را لغو کرده و به اسرائیل چراغ سبز برای حمله به گروه‌های مسلح مورد حمایت ایران در عراق داده است.
این گزارش به نقل از منابع ناشناس منتشر شده و تاکنون از سوی آمریکا، اسرائیل یا عراق به‌طور رسمی تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24967" target="_blank">📅 19:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24966">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca7496737.mp4?token=Viss_vr63Q7K6vs2C1lPVtU6BRyyywsd35d0VYPLGm0CwULeIemUWn1VtozXLgx8CNOUBBJQbUCEPy3Ond7h6w_5G8labM2oMXU8jzJ9ZmkVBbBK7dMdJevKcSzXomaV3-H2h2NX2T_zxVVGHToJnsJAHZlW5c1kEYF4KCRMvsJPulWxKnHl8FyQCHhzdhca5kvecw6p4f6IbMpfRbJYPAwEDd8EXWq8fgIl8A6PH4KWFi3JWR7sYOo2M8QbO2QGGwcvy-TcS6sW9QWt4HBRvrODq8P5CVi1iTahTK0x5f3_e6rTSlrS3NE_SNegfSm_BEDm9J04bS73R2lMrvWrMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca7496737.mp4?token=Viss_vr63Q7K6vs2C1lPVtU6BRyyywsd35d0VYPLGm0CwULeIemUWn1VtozXLgx8CNOUBBJQbUCEPy3Ond7h6w_5G8labM2oMXU8jzJ9ZmkVBbBK7dMdJevKcSzXomaV3-H2h2NX2T_zxVVGHToJnsJAHZlW5c1kEYF4KCRMvsJPulWxKnHl8FyQCHhzdhca5kvecw6p4f6IbMpfRbJYPAwEDd8EXWq8fgIl8A6PH4KWFi3JWR7sYOo2M8QbO2QGGwcvy-TcS6sW9QWt4HBRvrODq8P5CVi1iTahTK0x5f3_e6rTSlrS3NE_SNegfSm_BEDm9J04bS73R2lMrvWrMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سناتور جمهوری‌خواه ریک اسکات:
من هم از قیمت‌های بالای بنزین خوشم نمی‌آید، اما نمی‌خواهم با یک سلاح هسته‌ای کشته شوم.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24966" target="_blank">📅 19:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24965">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گزارش رویترز می‌گوید پاکستان پیش از آغاز عملیات صبح امروز،
تجهیزات نظامی، سامانه‌های پدافندی، توپخانه سبک، پهپاد و تجهیزات ضدپهپاد
به عدن فرستاده و
مشاوران نظامی پاکستانی
نیز در محل حضور دارند. اما رویترز تأکید کرده که متحدان عربستان قرار نیست مستقیماً در عملیات رزمی زمینی شرکت کنند. همچنین
پهپادهای ترکیه‌ای
که عربستان قبلاً خریداری کرده، در عملیات به کار گرفته شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24965" target="_blank">📅 19:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24964">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نتانیاهو : ما مأموریت را تکمیل خواهیم کرد. می‌خواهم بدانید‌که ما هر روز آن را تکمیل می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24964" target="_blank">📅 19:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24963">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f364dd49e8.mp4?token=BcAgUmzb6Bq_Uc8v0ksh8-kHiKS9POdyVVRmn4jdjvNyyv5LMJjDV5-AyymYUtsYY9sjFSyDZHd1aizWczV7GmNiOtU-_x813eiW27bcb6PBJ0Kd2yTcN00_75UcFyxtXGGKeb4ebjYKCCPCwkSWvt6MZMeZWHcPfTbcJFisculOtnVjowFqpGYorYoT5EQk8ZDsTBvZuriIYB74708J-JlWcFH20nkqZhKnBmfx6kTAImWKDH9zT6WOf7voSRYRjnqSVwReN7eUHuLsV9nRxr_bhLwJjaM3K3kBGF0uVVZESrLsgyOcZUp0gDNjXBdxdFWA9yuttF4-S4LKoCGEqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f364dd49e8.mp4?token=BcAgUmzb6Bq_Uc8v0ksh8-kHiKS9POdyVVRmn4jdjvNyyv5LMJjDV5-AyymYUtsYY9sjFSyDZHd1aizWczV7GmNiOtU-_x813eiW27bcb6PBJ0Kd2yTcN00_75UcFyxtXGGKeb4ebjYKCCPCwkSWvt6MZMeZWHcPfTbcJFisculOtnVjowFqpGYorYoT5EQk8ZDsTBvZuriIYB74708J-JlWcFH20nkqZhKnBmfx6kTAImWKDH9zT6WOf7voSRYRjnqSVwReN7eUHuLsV9nRxr_bhLwJjaM3K3kBGF0uVVZESrLsgyOcZUp0gDNjXBdxdFWA9yuttF4-S4LKoCGEqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسحاق هرتزوگ، رئیس‌جمهور اسرائیل: «رئیس‌جمهور ترامپ درباره تهدیدی که از سوی تهران وجود دارد،
حق دارد
. ما با یک
امپراتوری شیطانی
روبه‌رو هستیم که می‌خواهد جهان را به‌شدت افراطی کند، جهان آزاد را به تصرف خود درآورد و تا اروپا و ایالات متحده پیش برود.»این موضوع فقط نگرانی اسرائیل نیست و
تمام منطقه همین احساس را دارد
؛ چه آن را علناً بیان کنند و چه پشت درهای بسته.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24963" target="_blank">📅 18:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24962">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3B5VQqDfWsa89u_wp8zaX-3xPx5Zoeo_YZgrLyCLCJdIwyCjbhDpPh0LH8I1P_93XaNOSzbE8XJHJbfdi6v3eUh1cGU4B-fNtXApbKtuBY2lZlrtuLGQcdWfa9y8YQdXMC1h0ePUY17TtvLQHdMhQijnktbwqL4QAkCPw_ng7NBOyBWUKGs__plWhfh1OqjCj71xcn47FMxIHhAnbYSO17-FRLE163wZFtd7zflnOrqN0M72Zuk6Fxw4xPRMcCXpbEdmneJwjOqKF-jzPXLP0c2d4Z_3zreyboytZUauTKa09i85N2nZRjwCTwVZ7B1_R94Rp052GXb294G9z-NzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشور رژیم جمهوری اسلامی , اسکندر مؤمنی برای شرکت در مذاکراتی وارد دوحه قطر شد هم زمان ۶ سوخترسان و جنگنده های آمریکای با تمرکز بر تنگه هرمز در حال اسکورت کشتی ها از مسیر جنوبی تنگه هستند
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24962" target="_blank">📅 18:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24961">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adeQqHH4R8dF1Im5Z6XJQADjY_lD74614Soiofx12UTNDtT2rT-Gy_B6qscNE17oubHP6Hf8ENVMhLIPne3NLW9aCdX9Lh5F90mnCVGwzEzmI9SRp7RE1QMiTXXstzV0ljsCeLX039b_W9uW6VGT19ZahjTDBPWyZFKi-pBF0G9P4fB5pcmfwXm99RSWk15lwAqr_lAkDpdLQ6HOl4oyNgfDvQy4MVPWj1sD9ZKauckzTvGFWmridLPcVKNOs1x-AmTa8z9xJgSMygl8URpyvm4M_KI49j3sw8D6K3XHV52UeQi2ind4jkaxTV2Q5zJwWEzB9zIkeCn_902_98qSpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی درباره وقوع حادثه‌ای در تنگه هرمز دریافت کرده است. یک منبع موثق گزارش داده است که یک نفت‌کش حامل نفت خام، در ناحیه‌ای بالاتر از خط آب‌خور، مورد اصابت یک پرتابه ناشناس قرار گرفته است.
مقامات در حال بررسی موضوع هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24961" target="_blank">📅 18:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24960">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اتاق جنگ با یاشار | حقیقت‌یاب:
آیا آمریکا و استارلینک می‌توانند بدون همکاری حتی یک اپراتور یا نهاد ایرانی، اینترنت را مستقیم به گوشی مردم ایران برسانند؟
فناوری «Direct-to-Cell» برای همین نوع اتصال طراحی شده و گوشی معمولی می‌تواند بدون دیش و دستگاه اضافی مستقیماً با ماهواره ارتباط برقرار کند؛ ماهواره عملاً مانند
دکل موبایل در فضا
عمل می‌کند. در مدل فعلی، استارلینک عمدتاً از فرکانس و شبکه اپراتورهای شریک استفاده می‌کند، اما در سناریوی ایران می‌توان از
یک اپراتور خارجی یا معماری مستقل ماهواره‌ای
استفاده کرد؛ بنابراین همراه اول، ایرانسل و رایتل الزاماً نباید همکاری کنند. در این حالت می‌توان برای کاربران
eSIM
( آسان ولی نیازمند گوشی مدل بالا)
یا سیم‌کارت فیزیکی(
سخت در توزیع ، ولی راحت تر) صادر کرد، اما سیم‌کارت به‌تنهایی کافی نیست و باید شبکه ماهواره‌ای، احراز هویت و فرکانس موردنیاز از سمت استارلینک و اپراتور شریک خارجی فراهم شود که این هم میتوانند . از نظر گوشی، سرویس‌های ماهواره‌ای اپراتورها در برخی کشورها از
iPhone 13 به بالا
پشتیبانی می‌کنند(قابلیت‌های ماهواره‌ای اختصاصی اپل از
iPhone 14 به بعد
وجود دارد این دو سرویس با یکدیگر یکی نیستند) اما سؤال مهم‌تر این است که آیا حکومت ایران می‌تواند چنین ارتباطی را قطع کند؟
قطع دکل‌ها و شبکه اپراتورهای داخلی، ارتباط مستقیم گوشی با ماهواره را قطع نمی‌کند
؛ ولی هیچ تضمینی وجود ندارد که دولت نتواند با
پارازیت و اختلال رادیویی روی فرکانس مربوطه
یا روش‌های فنی دیگر ارتباط را مختل کند. بنابراین «کاملاً مستقل از زیرساخت ایران» از نظر فنی ممکن است، اما «غیرقابل اختلال توسط حکومت ایران» نیست.
اگر تصمیم و زیرساخت لازم آماده باشد، راه‌اندازی محدود می‌تواند در مقیاس چند هفته تا چند ماه تصورپذیر باشد، اما ایجاد اینترنت موبایلی گسترده برای میلیون‌ها نفر به زمان و ظرفیت بیشتری نیاز دارد و اگر در انتظار این سرویس هستید بهتر است گوشی با قابلیت eSIM هم آماده داشته
باشید
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24960" target="_blank">📅 17:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24959">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اتاق جنگ با یاشار | حقیقت‌یاب: ماجرای موسوم به «طاعون روسی» پس از مرگ یک پژوهشگر ۲۸ ساله در مؤسسه تحقیقات ضدطاعون در ایرکوتسک روسیه مطرح شد؛ اما
آزمایش‌های رسمی تاکنون ابتلای او به طاعون را تأیید نکرده‌اند
و علت مرگ، ذات‌الریه با منشأ نامشخص اعلام شده است. گزارش‌هایی درباره شکستن لوله حاوی باکتری یرسینیا پستیس منتشر شد، اما مقام‌های روسیه می‌گویند
هیچ حادثه آزمایشگاهی و ارتباطی میان مرگ او و عوامل بیماری‌زای محل کارش پیدا نشده است.
حدود ۲۰۰ نفر تحت مراقبت قرار گرفتند و در میان افراد بررسی‌شده
دو مورد کووید و دو مورد راینوویروس
شناسایی شده، اما مورد جدیدی از طاعون گزارش نشده است. کشورهای همسایه از جمله قزاقستان، تاجیکستان، ازبکستان و قرقیزستان
کنترل‌های بهداشتی مرزی را افزایش داده‌اند، اما مرزها بسته نشده‌اند.
کارشناسان نیز می‌گویند فعلاً هیچ شواهدی از شیوع طاعون ریوی یا یک بیماری جدید مشابه کرونا وجود ندارد.
طاعون ریوی در صورت تأیید بیماری جدی و بدون درمان می‌تواند مرگبار باشد، اما با تشخیص سریع و آنتی‌بیوتیک قابل درمان است.
بنابراین ادعای «طاعون مهندسی‌شده روسی» یا یک همه‌گیری جدید در حال حاضر
فاقد شواهد معتبر است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24959" target="_blank">📅 17:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24958">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c88d29dc5.mp4?token=fkrT5hXS_U4l6UIGarXqYOFwo0DPSKVM7Thok2y3mjV9KV_2GrRZDgoCfBvUtDTdWMK5UBqt2mn-AmeYyEbk5tUcWkKd0ch1GYACxy7QOqtooKKb5wjr5Y0DXwRTVARSxTM8MDBAI1dD44Up9NALVMm0SE4heXMpd22C_oa5ub3ou_nwV79UwSj0Tbhjo11KJHNn1uTPZL1325kSCgy8KBUFAA4R3VlIMwNP4Yv0e4n_2AYnLvin_s0wh_1w0T0ag_PkMIhpiSfA_7dr9JFb22tVGvp8nuFcUen7yFYVUIpQjBmki-QcPXN_ahX2mVQQa3N27P5G-G2GRDSIkabjcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c88d29dc5.mp4?token=fkrT5hXS_U4l6UIGarXqYOFwo0DPSKVM7Thok2y3mjV9KV_2GrRZDgoCfBvUtDTdWMK5UBqt2mn-AmeYyEbk5tUcWkKd0ch1GYACxy7QOqtooKKb5wjr5Y0DXwRTVARSxTM8MDBAI1dD44Up9NALVMm0SE4heXMpd22C_oa5ub3ou_nwV79UwSj0Tbhjo11KJHNn1uTPZL1325kSCgy8KBUFAA4R3VlIMwNP4Yv0e4n_2AYnLvin_s0wh_1w0T0ag_PkMIhpiSfA_7dr9JFb22tVGvp8nuFcUen7yFYVUIpQjBmki-QcPXN_ahX2mVQQa3N27P5G-G2GRDSIkabjcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز:
نیروهای دولت یمن با پشتیبانی عربستان مدعی
تصرف منطقه راهبردی ذوباب و مواضع کلیدی مشرف بر تنگه باب‌المندب
شده‌اند. طبق گزارش‌ها،
فرودگاه ذوباب
نیز به کنترل این نیروها درآمده و مسیرهای تدارکاتی منتهی به باب‌المندب قطع شده است. درگیری‌ها همچنان در اطراف برخی مواضع نظامی ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24958" target="_blank">📅 17:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24957">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رویترز:
بانک HSBC میانگین قیمت طلا را برای سال‌های آینده کاهش داد؛ پیش‌بینی ۲۰۲۶ از
۴۵۶۰ به ۴۴۹۰ دلار
و پیش‌بینی ۲۰۲۷ از
۴۹۲۵ به ۴۸۲۵ دلار
در هر اونس کاهش یافته است. با این حال، HSBC همچنان چشم‌انداز بلندمدت طلا را مثبت می‌داند و معتقد است اگر قیمت به محدوده
۴۰۰۰ دلار یا پایین‌تر
برسد، احتمال افزایش خرید توسط بانک‌های مرکزی وجود دارد که می‌تواند از قیمت حمایت کند. در کوتاه‌مدت،
افزایش بازده اوراق آمریکا، دلار قوی و رشد قیمت نفت
همچنان از عوامل فشار بر طلا هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24957" target="_blank">📅 17:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24956">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/990c4f7388.mp4?token=eGIsQ1qhbsQgPkhhKwmTJ8r2_XeWeQom5THgGEGuV-lttCHhvzQKNosd0DJCzlmvNe6mnWYBO4QzvrbrBh5t2TY3grLp2PC77duEu7gy40x_HNyg-UxZ1ORPfon-DUTukETjNeJuaffwfztZAwR4Am19CjCgC5ny5hxmBrWgXJEP4B2ytXzNBVoxCaa6loXBdn-1MAa2PkREEQouMA-E9Xx13Kiip42yFNefAb7ymxjVPGNQGVq2LnKOiysgOlMoCtwNDXJN9JLXhItkjlnEpSu81xFA4nps6UQo7ME9TXwEg_dl9WzewRcsj4rbNwpvYf2VRvrw3wca9vjdgys7Woi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/990c4f7388.mp4?token=eGIsQ1qhbsQgPkhhKwmTJ8r2_XeWeQom5THgGEGuV-lttCHhvzQKNosd0DJCzlmvNe6mnWYBO4QzvrbrBh5t2TY3grLp2PC77duEu7gy40x_HNyg-UxZ1ORPfon-DUTukETjNeJuaffwfztZAwR4Am19CjCgC5ny5hxmBrWgXJEP4B2ytXzNBVoxCaa6loXBdn-1MAa2PkREEQouMA-E9Xx13Kiip42yFNefAb7ymxjVPGNQGVq2LnKOiysgOlMoCtwNDXJN9JLXhItkjlnEpSu81xFA4nps6UQo7ME9TXwEg_dl9WzewRcsj4rbNwpvYf2VRvrw3wca9vjdgys7Woi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو تأیید کرد
بمب‌افکن‌های آمریکایی بلافاصله پس از طرح تروریستی، پایگاه ویرفورد را ترک کردند، اما این جابه‌جایی را «غیرعادی» ندانست: «چرخش‌های منظمی وجود دارد… من مستقیماً این موضوع را به جابه‌جایی انجام‌شده مرتبط نمی‌کنم. دیدن چنین چرخش‌هایی غیرعادی نیست.» تمام بمب‌افکن‌های آمریکایی مستقر در این پایگاه به پایگاه‌های اصلی خود در آمریکا بازگشته‌اند. هر ۶ مظنون این پرونده نیز آزاد شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24956" target="_blank">📅 17:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24955">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e32f588d98.mp4?token=Syg2nBIO12F-JHx5q_9fJRCt_IymeveE_g49vJHHLA0R_ij8XWBF1sIxzKQ9jzyCouTGQQ7knm9SNmK-E7JAyEwqt78mEz6JHfVbyiy3_L4bhwKnxXi5FpXyLyg8SNQkKhNtbc8ibe_rwjKgArtEZYkuVdHXG49s0vTrQ-3tCYb4OB49_L8yHRPXyiKzor2N_KInJzZDB2KMqdyPPOEtb4rUU2gPoXPWvrGBpqWrrbYYfQMB79OuaxnfChVtEaDc9qo5pSlGptgQrMisEUYTh2ENuNOoo3lUmArtr-MEGUQCLKuDVK8c_6d0w5KP2DLCd4KpXQhr7ONY4KGEDveaKyIK5zevGBGpECZEqhTsRHme0Mr2N87jBkdWplFn_WLBGv-vZpuyaBMRnpuGOFax_o2A5z3NoXusknplgbht7qDrDSTx6nDFJac7qj6TFmuVTQBlXvm0vLZB1qsCbDxr2Nz9QliBcCPk_lcgrO9ly6yaC9munMvsvlERcG7ZPBb34_sUFh4zmNh4woeC4fBTsbvmjFrm9ja2SDl_U_oHbB0BOVVSnHzB_3TztbmhH68bpP4RtBLfm_GNuxS7AN9R3ucjte40eWSzbPATDYXSvdkW0kiCDmuk8Dl3yj-kCwu8VmRhBDdQA_xC07nCOwVpsHrRzUiup_dLJaavyYNhhhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e32f588d98.mp4?token=Syg2nBIO12F-JHx5q_9fJRCt_IymeveE_g49vJHHLA0R_ij8XWBF1sIxzKQ9jzyCouTGQQ7knm9SNmK-E7JAyEwqt78mEz6JHfVbyiy3_L4bhwKnxXi5FpXyLyg8SNQkKhNtbc8ibe_rwjKgArtEZYkuVdHXG49s0vTrQ-3tCYb4OB49_L8yHRPXyiKzor2N_KInJzZDB2KMqdyPPOEtb4rUU2gPoXPWvrGBpqWrrbYYfQMB79OuaxnfChVtEaDc9qo5pSlGptgQrMisEUYTh2ENuNOoo3lUmArtr-MEGUQCLKuDVK8c_6d0w5KP2DLCd4KpXQhr7ONY4KGEDveaKyIK5zevGBGpECZEqhTsRHme0Mr2N87jBkdWplFn_WLBGv-vZpuyaBMRnpuGOFax_o2A5z3NoXusknplgbht7qDrDSTx6nDFJac7qj6TFmuVTQBlXvm0vLZB1qsCbDxr2Nz9QliBcCPk_lcgrO9ly6yaC9munMvsvlERcG7ZPBb34_sUFh4zmNh4woeC4fBTsbvmjFrm9ja2SDl_U_oHbB0BOVVSnHzB_3TztbmhH68bpP4RtBLfm_GNuxS7AN9R3ucjte40eWSzbPATDYXSvdkW0kiCDmuk8Dl3yj-kCwu8VmRhBDdQA_xC07nCOwVpsHrRzUiup_dLJaavyYNhhhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل: «رهبران جهان به من می‌گویند: تو از دل جهنم ۷ اکتبر برخاستی، افراطی‌های اسلام‌گرا را شکست دادی و به بشریت امید دادی که می‌توان نیروهای تاریکی را شکست داد.
سپس بسیاری از آنها اضافه می‌کنند: ای کاش جوانانی مثل اینها در میان ما هم رشد می‌کردند.»
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24955" target="_blank">📅 15:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24954">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f2091a813.mp4?token=hQnPaNb6JDILKGQi5S6y50Sy2h53QEg7X-47QDeopOdRuA9BV8G1QNx6_2r82dlaFeHT4I5unLbE4HCup5R_FoY3prgqdi_l6UdA4r5Me1A4KrRUkzcRXyny3aDl3psJnfVp63s6Fuj_UPJMj9MBL3wFk_-0DKYhlhF7fLI50Qil6zNOg1EetckGqU3dVOppGjotJAbcASvuXlUgnGNMWIUqv4iv-wDUu7kDghq7mCUw5JXbCzUDKhdWAbXyZcCtfcFX0YZVZ6zv0DZwiNoivi5ImyVV_NVwEX8rCSNEQt-vrIYmms30A84N-8L-q_zmaF2R5ul-4FEiq827lPK21g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f2091a813.mp4?token=hQnPaNb6JDILKGQi5S6y50Sy2h53QEg7X-47QDeopOdRuA9BV8G1QNx6_2r82dlaFeHT4I5unLbE4HCup5R_FoY3prgqdi_l6UdA4r5Me1A4KrRUkzcRXyny3aDl3psJnfVp63s6Fuj_UPJMj9MBL3wFk_-0DKYhlhF7fLI50Qil6zNOg1EetckGqU3dVOppGjotJAbcASvuXlUgnGNMWIUqv4iv-wDUu7kDghq7mCUw5JXbCzUDKhdWAbXyZcCtfcFX0YZVZ6zv0DZwiNoivi5ImyVV_NVwEX8rCSNEQt-vrIYmms30A84N-8L-q_zmaF2R5ul-4FEiq827lPK21g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در مراسم گرانیداشت ۷ اکتبر : اسرائیل اجازه نمیده جمهوری اسلامی موجودیت این کشور رو تهدید کنه. رژیم تهران ضعیف‌تر از هر زمان دیگه‌ای از زمان تأسیسشه، برای بقای خودش می‌جنگه و در نهایت از بین خواهد رفت. @WarRoom
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24954" target="_blank">📅 15:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24953">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نتانیاهو در مراسم گرانیداشت ۷ اکتبر : اسرائیل اجازه نمیده جمهوری اسلامی موجودیت این کشور رو تهدید کنه. رژیم تهران ضعیف‌تر از هر زمان دیگه‌ای از زمان تأسیسشه، برای بقای خودش می‌جنگه و در نهایت از بین خواهد رفت.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24953" target="_blank">📅 14:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24952">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9qAGrnJd3u76eX7351h-i_NHCTg3YO3uWBu4hFB0WZwvVacTw2GZG-QP0YHMm8ZVKUMIVlQt8xvOvnZEi_RrVZnp-X-Gjaw8kovHHyanaUtknkAnFDb7L84o7UEQw2aMNEo3qTNFBZWy_ywj5RSpkzBbW3fJfL_b-diM8F9MPc7uXF55p7dfG9My6HzoON-MKP0Eh48fgh5V66xN_EeCa8wbZrHoK0roReOiKj-tvypKdhOuClNKCS186UrjaLe1JJltFdufw6-vXbVfCl7yQMkHrZMhNcqAJZxvl4_LE3_YTwAbsif6dBatvGRSZKYVfZCqPWzyfM5RLYZ6XYCHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم میهن بکش هر جوری که میتونی نا امید نشو … چیزی‌نمونده
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/24952" target="_blank">📅 14:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24951">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سازمان دریایی بریتانیا :  گزارش می‌دهد که ایران یک نفتکش را که قصد داشت خلیج فارس را از طریق مسیر عمانی تنگه هرمز ترک کند، مجبور به بازگشت کرد و نفتکش از دستورالعمل‌های سپاه پیروی کرد
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24951" target="_blank">📅 14:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24950">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pw7b-SM7CmdlOuRvWphvLBoEsn2xRgzVJsSyhHrvGt2dwV8ehya5eDAULMRk9i2C6sLtGIk-fKtXjVelaFfGDpYt_IL-BHSH03I_wlmOGPOLDZOxun6Mxs1-di7tNiBn7zWc3xKPUJNfagVMxbb7Wh1UMLThn3Ls6bzZwswradzmilMuQYG1gzGL_43wta2vHWBFb1QLQDdHs-w8pXqYUfnHfZQrCc6TcAs9gNXA6XFAiB79fhu4Dxy4lN5LR584_mA7w0IUvcnDcXtpco0EV7GDTCxmel0q__fiV6vkpsxrqlakSuk9XuczjTabmvsVWvVaKqslQpfX-7CTD81YOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گشت‌وگذار یک دانشجوی عراقی با خودروی آمریکایی دوج چارجر در همدان، در حالی که تصویر تروریستها؛ علی خامنه‌ای، قاسم سلیمانی و ابومهدی المهندس (جمال جعفر محمدعلی آل‌ابراهیم، معاون پیشین حشدالشعبی عراق) روی بدنه آن نقش بسته است. @WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24950" target="_blank">📅 13:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24949">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دایرک جای ، کامنت جای درد و دل و جای سوالی های  بی مورد و آموزش کامپیوتر یا پشتیبانی اینترنت شما نیست ! برای آخرین بار میگم ۹ ماه شد چرا ملت نمیفهمند ؟ مسیج پشت هم ندین در هم و جا بجا میاد !  فقط در‌یک پیغام ،الان این دو نفر‌هی دارن پیغام میدن یکی قبض برق…</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24949" target="_blank">📅 13:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24948">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ogk5sXLIejIN2WyRljWzU0qYBUmN9r8ngcMw6iIkL1ujEdPR6x10IVx_SNeW8B_bEmsiYSf2REYwQmn44VA9yokDsE0K2yoLbV4owjxRbRJ9QEaTMBF7zns3i_El4sCUdsCBGnDAzxFUjCJHj1JgnNhkmxDugoMj5fB0CEoLAa-DjAPUuHJc4Ts8zpoWLK3ZMLEau405ncvt7umZ1WUppGEPgQNkHo9mBcPdDMq3xH_ro66nz538cYOrXraW2z8OdTbT1v5AUN3EIPMDkDQUM-dwp5LwS45i0L6wK9GGxssSK4vjP6eU0t14XYngDx5XVXyXDjJpbs-CbSyMYqTqRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دایرک جای ، کامنت جای درد و دل و جای سوالی های  بی مورد و آموزش کامپیوتر یا پشتیبانی اینترنت شما نیست ! برای آخرین بار میگم ۹ ماه شد چرا ملت نمیفهمند ؟ مسیج پشت هم ندین در هم و جا بجا میاد !  فقط در‌یک پیغام ،الان این دو نفر‌هی دارن پیغام میدن یکی قبض برق داده و اون هو میگه من کجام ، اخه یک بگه به تو چه ، چرا حالیشون نمیشه من نمیدونم !!!! من مشاور نیستم چیزی باشه برای همه میگم دایرکت جواب‌ نمیدم</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24948" target="_blank">📅 13:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24947">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سردار حسین رحیمی، رئیس پلیس امنیت اقتصادی فراجا، در همایش سکوهای اینترنتی هشدار داد سایت‌ها و کانال‌های داخلی نباید قیمت‌های غیرواقعی ارز را که از سوی برخی کانال‌های خارج از کشور منتشر می‌شود، بازنشر کنند. رحیمی گفت انتشار این قیمت‌ها می‌تواند به التهاب بازار…</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24947" target="_blank">📅 12:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24946">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سردار حسین رحیمی، رئیس پلیس امنیت اقتصادی فراجا، در همایش سکوهای اینترنتی هشدار داد سایت‌ها و کانال‌های داخلی نباید قیمت‌های غیرواقعی ارز را که از سوی برخی کانال‌های خارج از کشور منتشر می‌شود، بازنشر کنند. رحیمی گفت انتشار این قیمت‌ها می‌تواند به التهاب بازار دامن بزند و به مردم، مصرف‌کنندگان و کسبه فشار وارد کند و تأکید کرد پلیس با انتشار و بازنشر قیمت‌های غیرواقعی ارز برخورد خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24946" target="_blank">📅 12:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24945">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24945" target="_blank">📅 12:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24944">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">الجزیره به نقل از محمد الشرقاوی، استاد حل‌وفصل منازعات بین‌المللی، گزارش داد که با توجه به مواضع اخیر دونالد ترامپ و مقام‌های جمهوری اسلامی، احتمال روی‌آوردن آمریکا به گزینه نظامی افزایش یافته است. الشرقاوی پیش‌بینی کرده است که
ترامپ ممکن است از هفته پایانی مهر تا نیمه آبان، همزمان با انتخابات کنگره آمریکا، حمله‌ای غافلگیرکننده به ایران انجام دهد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24944" target="_blank">📅 12:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24943">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">در پی فعالیت نیروهای ارتش اسرائیل برای نابودی تونل ها و مخفیگاه های دشمن در ساعات آینده، احتمال شنیده شدن صدای انفجار و لرزش در مناطق غرب گلیل، مرکز گلیل علیا، دره الحوله، رشته‌کوه رِمام و احتمالاً در شمال جولان وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24943" target="_blank">📅 12:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24942">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKQY64VOMKKDxbMIPxcHZFRc0ibL92kHAM6WmK2dZJKiVbZt30ThfPSEW5uODOLRVZ0sXRn6v68KM3oivYxKCOaJWTRJQ3csSEwenrJHAYS9sL5R5a2YcC10FIskqxipYwKkCZGWyDQPcGJeYCDCOpFDv2w2kkMOCVgem15Vs3t_Gxub8mUEsva1rBKP6Wb6MupiczuJ_yJOWiAoo9uZr7EfelLWFZrzlLRTPNuAwcPBsGt35ONJ-VYu8630RCxzNqTT-sfPVCSQnPs1u0UnuPohFmd6x6mn_td2h9hTujd84Qohnhu7GvbIDaNQ3H0yw7ts8Y1LZO2l9eyEfjO56w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانون حقوق بشر ایران اعلام کرد
علیرضا سپاهی و علیرضا رئیسی
، از متهمان پرونده «میدان علیخانی» اصفهان، بامداد امروز دوشنبه ۱۳ مهر ۱۴۰۵ در زندان دستگرد اصفهان، همزمان با اذان صبح، حکمشان اجرا شد.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/24942" target="_blank">📅 11:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24941">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ای۲۴نیوز : دولت ضداسرائیلی اسپانیا سقوط کرد ، نخست‌وزیر اسپانیا، سانچس، از برگزاری انتخابات زودهنگام در تاریخ ۲۹ نوامبر خبر داد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24941" target="_blank">📅 11:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24940">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خودروی متعلق به دفتر نخست‌وزیری اسرائیل در یک تلاش برای ترور هدف تیراندازی قرار گرفت و مورد اصابت گلوله قرار گرفت. بر اساس اطلاعات موجود، به نظر می‌رسد هدف مهاجمان پسر آقای دومرانی (از مقامات دفتر نخست‌وزیری اسرائیل) بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24940" target="_blank">📅 11:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24936">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eWN-1B4toWBrx_UyeQ1fhqQW10nu0_FwhQoclLnopxURnyInJbUj2lQQEkNXVYevUrA1ukKDoD5qRP3WOBsla7NmUhjmCS-k31kSJQEGG2WwaJ6Si9q62-BFye7-XdXRvxHMcqYtHVKWkfRsE5S2_1Qg1S_gFlXoG0anhtCt82x4XRYPNyGHz6s5lVyVnni2QTuBZ07P5MR1FrFdcSGm3jfxKYT4hlSq4Pizgh5JBr3LpSRy9xPdjeiYb-QpopTl_yRxgxC2w5kzxWg04896hAq-Hez_o4y1JhcbyCPE_fEUp8H3Gt76v_M-IG6RGFXXQmAFby5NTI5xYzbSDuKyYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RokDo4LKlXrrVpa0hF7ZqIMXYeK_HZMlGtlwvYPkQiNsWj01TsuIXrrinrTamfoarhKJSGWv0aBieZpxp5i-yOgwIiol-DlQAjIQBJwCfJgFqu2dbi3kRvKgaOR6DbPiy98CkjFR-wGAX_HLy5OREB1WeMftBf9mR8z3LAGf5ftFr_R0u1Oeji2dSqkhkmXCKg1HFICMPqm8RN8TnMrRyTsheTq6X8_NwX3gHL00yIACk6TiZVAPNJD_t-9BCfRs5INSZPqNx8Pg-nADW47OsN09W1zEmBttUFyvE27vEJO0y2Z7BR9yycWskcT3IEpaAG4h9BIN7TsUMCHz8dNfmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tU4IGpTqXElDvEIs4BYRNwEGAGwemgSSitzz1NqBJKCahpDx8MP0ATnapTgsaBqDL78wtH8QJW73G_QiZ3udTrI-hxV3MZZ6DhsBo2ms6HqZwNqmTJtWwXKOgTGpJ2cOQOKyP-hFLiLFNm2QPM3ar9RmZXp112cqzwkFnNvhd0GhSuriaGnCHE7_yhNvSWNQIrJ11dzJlXi9uEHkWJNzDSg7uP6QnhzIqtmkdtmlzGyH9mhb6xfBi6nkz_xtjpt6X87T5qC3a-M3PBIVYTb9M6EqrubGx90Jxa61JACe_sj4DbKr_tLZ8knmCFOQthy7TS0rKCFMFYRobZ6lSOyVyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/568831ae66.mp4?token=F89SwTvRfkaH4-jC9gbrkdDzjal0NZ3NyaSwUerjCYt3BIFG6tAdQmJFbTgOPNsSjFq7mX0vF35ITirHpWkMet_ou3bi0q6oTwBjt1BKiKlnrXN8qgBbhNt-AIaRB-vchwiOugBfvdT0MzkwYeAYQmRVXhw3mhw4rQ9fTraxtYn6ish4_CiKLC_QnkLj861-CasCSntJ3RcEWIklt1zRLly8kpBH9US4AK51w9h58vWhdZ93aCvZhBqkk5jc_RwEqMdNwf74z4lVFJeEjto1J4uOqvrcT2RYZyNpDZ_wJ8yafuHamh8TxMfTOwolb2_VM4CqbQpJ_3ccyURv5_N-uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/568831ae66.mp4?token=F89SwTvRfkaH4-jC9gbrkdDzjal0NZ3NyaSwUerjCYt3BIFG6tAdQmJFbTgOPNsSjFq7mX0vF35ITirHpWkMet_ou3bi0q6oTwBjt1BKiKlnrXN8qgBbhNt-AIaRB-vchwiOugBfvdT0MzkwYeAYQmRVXhw3mhw4rQ9fTraxtYn6ish4_CiKLC_QnkLj861-CasCSntJ3RcEWIklt1zRLly8kpBH9US4AK51w9h58vWhdZ93aCvZhBqkk5jc_RwEqMdNwf74z4lVFJeEjto1J4uOqvrcT2RYZyNpDZ_wJ8yafuHamh8TxMfTOwolb2_VM4CqbQpJ_3ccyURv5_N-uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس سیستان‌وبلوچستان: افراد مسلح به گشت انتظامی پاسگاه نوکجو در محور بمپور–ایرانشهر حمله کردند. در این حمله دو مأمور انتظامی کشته شدند. جزئیات بیشتری درباره مهاجمان و هویت گروه مسئول هنوز اعلام نشده است.  @WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24936" target="_blank">📅 11:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24935">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هواپیمایی جمهوری اسلامی ایران :  پس از رفع محدودیت‌های عراق برای انجام پروازهای نجف، نخستین پرواز ایران‌ایر در مسیر تهران-نجف ساعت ۸:۱۵ صبح امروز از فرودگاه امام انجام شد ولی پرواز ماهان‌ایر‌ مسدود خواهد ماند
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24935" target="_blank">📅 10:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24934">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d83bdd494.mp4?token=RhOkhj8v6Q78gN3Xt-4luDfK2OAsFfJLwND6sHnS7ufDBvJIGqrowu4ozpGSIdXt_j3GrlHQYmEC8Z1DdmYLiiqTPK82lRgsX4FVQH3xO9-Q5Ri0wm_mrs5sAjAMEtgtxLnNUnFa8nEtkx-UF62Nt169y4KI6g2JRYY4iM8XWnR_45CqEtejLtpdOwJyDioi16F8AMC59ojl5TJSxZ5K3FYdvjBfAQ0EYRj6zyGM1IrOO5oW0MbRFKBbDkIVkxIkf5LhXgoQESbTLhEcuf66v6-XzfmGT_ULpurwI7YUGSwQUZ9bBurq0W8r00GhF2gwi4XZa5XIFlHxKAMPYTS6kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d83bdd494.mp4?token=RhOkhj8v6Q78gN3Xt-4luDfK2OAsFfJLwND6sHnS7ufDBvJIGqrowu4ozpGSIdXt_j3GrlHQYmEC8Z1DdmYLiiqTPK82lRgsX4FVQH3xO9-Q5Ri0wm_mrs5sAjAMEtgtxLnNUnFa8nEtkx-UF62Nt169y4KI6g2JRYY4iM8XWnR_45CqEtejLtpdOwJyDioi16F8AMC59ojl5TJSxZ5K3FYdvjBfAQ0EYRj6zyGM1IrOO5oW0MbRFKBbDkIVkxIkf5LhXgoQESbTLhEcuf66v6-XzfmGT_ULpurwI7YUGSwQUZ9bBurq0W8r00GhF2gwi4XZa5XIFlHxKAMPYTS6kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدئویی که امروز کانال های روسی منتشر کردند یک تیم پدافند هوایی متحرک روسیه با موشک دوش‌پرتاب 9K38 ایگلا / SA-18 سامانه‌ای فروسرخ برای مقابله با اهداف کم‌ارتفاع—به یک پهپاد اوکراینی شلیک می‌کند. بنا بر ادعا، پهپاد پیش از برخورد با تأسیسات ذخیره‌سازی نفت سرنگون شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24934" target="_blank">📅 10:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24933">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">احراز هویت تصویری کاربران حقیقی ایرانی الزامی شد
مرکز ثبت دامنه‌های اینترنتی ‎.ir و دات ایران:احراز هویت تصویری سطح ۲ برای کاربران حقیقی ایرانی الزامی شده و ارائه خدمات تنها به کاربرانی که این مرحله را تکمیل کنند، انجام می‌شود
تکمیل‌ نکردن این فرایند، موجب محدودیت در دریافت خدمات خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24933" target="_blank">📅 10:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24932">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گزارشهایی از شروع اعتصاب در بازار تهران
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24932" target="_blank">📅 10:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24931">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fExZlD1zR4Qk4bm1eE6vpMJxuLI3T1CQX0PcEfrUrcA91HBHftyMrVBZmW_nd6lYsJ7q5SbrAd4wh5e1_3sjds1f8xXh4dd0zguZMWK6jWtBRfyBYMo-BvhoZeDIneq6N0UrboQG6pjCHTuo1pRSMu6kWSEu1-HJht0gFIu4gdr7PRmDIaokto23gc0kSXN1JXaXR48BRgryOrySgJPfgug-EEIjYhBqb0eEi1YkYuiLueVQWgOcxhOa9HNrXg8YOtD_S30vstm5rU0JrsIbcno4c8YWzUpR6eeHsGDTO15MJUzVzf-1o9YOOuT74jy1h1TrTe3mHiI454zQUpTWXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو انفجار پشت کوه صفه اصفهان ، شبهای جنگ اونجارو زیاد زدن،ولی به نظر من رژیم داره تونل‌های مسدود شده رو باز‌ میکنه( رنگ عکس‌رو کمی‌تغییر دادم ستون دود معلوم باشه مال همین الان هست)
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24931" target="_blank">📅 10:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24930">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNNECpGZd4E2KVEf11bIohJvWAKk-lc6y2UQf8s6qPxexoNODT34o_uPOTFFRP9lQC7gwbENUBuPeVN4zSusDsDUQWpTJcjw5AcNyGjH-e8RYmAmt4ccXNHQjgCvuUs02NqcAf3VTNgEGP5GadsBzEUdKwB-bHmGFfNyuYSjd60hwcBxHn-dph0NVuGBZm-Cjk2fdJx97En-b-477MX-9jqWlitlBboOHFJETq1A1NSXuzl-Mddrl0_t0waIUX5n5XXgPVFxT10P0AVAt2b7dNZv-ZKq__cApO8nHA296p8CxHh8RofTl2vUsDj0YXVTg8GOKpOFMG4_A4x-m_ikhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصفهان
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24930" target="_blank">📅 10:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24929">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پلیس سیستان‌وبلوچستان:
افراد مسلح به
گشت انتظامی پاسگاه نوکجو در محور بمپور–ایرانشهر
حمله کردند. در این حمله
دو مأمور انتظامی کشته شدند
. جزئیات بیشتری درباره مهاجمان و هویت گروه مسئول هنوز اعلام نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24929" target="_blank">📅 10:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24928">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آی۲۴نیوز:
یک توریست آمریکایی در نزدیکی
ساختمان‌های دولتی اسرائیل در اورشلیم
پس از اعلام اینکه قصد انجام یک حمله تروریستی دارد، بازداشت شد. نیروهای امنیتی پس از دریافت اظهارات او، وی را دستگیر و تحقیقات درباره انگیزه و احتمال وجود تهدید واقعی را آغاز کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24928" target="_blank">📅 10:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24927">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نیروهای دولتی یمن : عملیات‌های دقیق علیه مواضع شبه‌نظامیان حوثی در محورها و جبهه‌های صعدة، الجوف، تعز و ساحل انجام شد.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/24927" target="_blank">📅 07:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24926">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نتانیاهو، نخست‌وزیر اسرائیل: حوزه دریایی عملاً به یک میدان نبرد بین‌المللی تبدیل شده و ما این را در تنگه هرمز و باب‌المندب می‌بینیم. دشمنان ما می‌خواهند فضای دریایی اسرائیل در مدیترانه، بنادر و تردد دریایی‌مان را تهدید کنند، اما ما اجازه این کار را نخواهیم…</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/24926" target="_blank">📅 07:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24925">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آکسیوس: آمریکا
۱۲ فروند بمب‌افکن بی-۱
مستقر در این پایگاه را طی آخر هفته به پایگاه‌های اصلی خود در خاک آمریکا منتقل کرد. پنتاگون با تأیید این جابه‌جایی اعلام کرد که تمام بمب‌افکن‌های ویرفورد به آمریکا بازگشته‌اند، اما همچنان برای انجام حملات دوربرد آماده هستند و بمب‌افکن‌های بی-۱، بی-۲ و بی-۵۲ می‌توانند از خاک آمریکا عملیات انجام دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/24925" target="_blank">📅 07:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24924">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvHjDKP8t3PKlRRN6H-Z1n9DAE8GtVxxck308l8Mu4zmSx0DadKiRdhmYoz8dpxI6pRZfW3YQtC9vCGkatTbzDhNcLPKPcY4a4VlU8ERQgPl2LzmKHh_vb_1PZc6iezHmDt4LF-DCoeagPc2isxDxqfvOryH0FkoQfw-_kAd4CgtdREUNaOd3gwlDyQu4ZGYsNVGNTziVh7fwoA-ExruGv1MYYTDZGlMIGR2mR6J5XrZxJzTzliay2RNszIy52TNMTf7F2RkpUez1qlSYLjrFjAR3nrAf1poN9E2ftZXXF6yahOAWd_XQmwi1th3LRmb9fg8u3S4rjaC2qbw6G4pUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتیوب تتلو
:
امروز دادستان و رئیس کل دادگستری با امیر تتلو صحبت کردند و به گفته او، این گفت‌وگو مثبت بوده است. او همچنین به بخشی از آهنگ «من و خدا» اشاره کرد که تتلو در آن می‌گوید «همین روزا دیگه باید بیاید استقبالم» و ابراز امیدواری کرد فردا خبرهای خوبی درباره وضعیت او منتشر شود و ممکنه که آزاد شود
@RapFA
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/24924" target="_blank">📅 00:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24923">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وال‌استریت ژورنال به نقل از یک مقام ارشد آمریکایی:
آمریکا از طرحی مرتبط با ایران برای
حمله به بمب‌افکن‌های آمریکایی و کشتن نیروهای نظامی در پایگاه ویرفورد بریتانیا
اطلاع داشت. به گفته این مقام، سپاه پاسداران
شهروندان بریتانیایی را برای اجرای یک طرح چندمرحله‌ای
استخدام کرده بود که هدف آن حمله به هواپیماهای آمریکایی و نیروهای مستقر در پایگاه بود. در این طرح قرار بود با ایجاد یک
انحراف در نزدیکی پایگاه
، زمینه حمله فراهم شود.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/24923" target="_blank">📅 23:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24922">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4ILqyi3qPSOmp1nowj3NblkdHCuy37NUg8nQBqd4Vdgfd7QJ-ESx6erQIOVELr2tzDK5Pzku1fROgj8UQC-HWzDBsHpxdI--28qcPFUJ-GZRlL7COe-ujlvuCz-2BbRdO7QdJueuKveMwwAGKEOmt64YSiJXmOvxMdCC2mvItYHEQOoQZTg3piirNrvWJ0986I1BUz8KmW6c_gRncDHg6eAys6IzNyZ03YkDzLu2f3Y5c38mb2-vlkYnsBKsf0s_ZgTN49EcST-jqK24_SBamoiQgoRZb3I02SSUx-qC0wW-PkBiiigWV3q3rpW7A1dz3feoEf0caj-ElHYd5SVhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس ختم خواهر عراقچی
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/24922" target="_blank">📅 23:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24921">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/24921" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24919">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmBupiVMsMVK8N_ImyYkREuzbPNxAYIUu5mnFOwZUExZWfdRmNEL8Km8IDhC8uvGlOd8c9g4E6YiOOUQBRZ8WJTE9dquVR7IPmNKFC9wTs4WBTJiT2RH2hwkgzfuc2d-H8bpZV5k5aYPyHgD5bhsb3W5aaFhVc2zBiD4HdJjROQK1EHeSOQFID_jOeUhBr0ywqRSryPwgmbK2vK6ZMGG2T9bgjom6JfO0SsHMjB9iVhFCx4xZaUjaGQATjLOJNh3S7ZlJHoQAAWNFg1mMQuPIqKoz5y5tfCID2Cv9G_vtsBsHay0_r6X2D6Wyo0R8aaWAvEftGtMdlzQtrZxwwIRLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ۱۲ فروند بمب‌افکن راهبردی B-1B Lancer نیروی هوایی آمریکا، پایگاه هوایی سلطنتی فیرفورد در انگلستان را ترک کرده‌اند تا به خاک اصلی ایالات متحده بازگردند. @WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/24919" target="_blank">📅 23:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24918">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تصاویر خبرنگاران از پرواز چندین بمب‌افکن راهبردی بی-۱ لنسر آمریکا از پایگاه نیروی هوایی سلطنتی فیرفورد در بریتانیا منتشر شده است. @WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/24918" target="_blank">📅 22:55 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
