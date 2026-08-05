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
<img src="https://cdn4.telesco.pe/file/tqyhFWbbFealMpAGLaPtF0jGNDZNsBE08JFt1MLrt2JZh9TOdfEUCeya_PEQwv28cEkVymAVgkQcohZ-Gm6poGs0pBzJemw6KM1_AlLF98WFeZrwPvBk744aguV6q4_Li7jhZiDO9mGHCSZ0mr1FUMc8JRrp4pBDcvEksQO1GLiM1UWvYhlh4d8WHZx82krFEW6yPMrsKUGMYXnw7hF5sQQtv91-csJsLalvVWuQtCAE6pd_roKiiW2sLL1C7JdcLvzWEQ3LyTF5sd4u3HKm0ju8Kr9hPO0quwkI7ESi1jwt-qaEIxZx_0Zglsd_AajL2Z7H3Gg5vfovpV0HI92F2w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 21:31:18</div>
<hr>

<div class="tg-post" id="msg-19717">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">غریب‌آبادی:   موضوع دریافت هزینه توسط ایران در تنگه هرمز بستگی به تصمیم مقامات عالی نظام و رفتار آمریکا دارد.</div>
<div class="tg-footer">👁️ 463 · <a href="https://t.me/SBoxxx/19717" target="_blank">📅 21:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19716">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">غریب‌آبادی:
موضوع دریافت هزینه توسط ایران در تنگه هرمز بستگی به تصمیم مقامات عالی نظام و رفتار آمریکا دارد.</div>
<div class="tg-footer">👁️ 494 · <a href="https://t.me/SBoxxx/19716" target="_blank">📅 21:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19715">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فوری | معاون وزیر امور خارجه ایران: پیام‌هایی از ایالات متحده دریافت کرده‌ایم که نشان می‌دهد این کشور آماده است تا به تعهدات خود بازگردد.</div>
<div class="tg-footer">👁️ 494 · <a href="https://t.me/SBoxxx/19715" target="_blank">📅 21:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19714">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فوری | معاون وزیر امور خارجه ایران: پیام‌هایی از ایالات متحده دریافت کرده‌ایم که نشان می‌دهد این کشور آماده است تا به تعهدات خود بازگردد.</div>
<div class="tg-footer">👁️ 868 · <a href="https://t.me/SBoxxx/19714" target="_blank">📅 21:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19713">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رائفی‌پور:   ایران به اردن حمله کرد و ۶ جنگنده اف ۳۵ را نابود کرد چون قرار بود به مراسم اربعین و مواکب حمله کنند</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/SBoxxx/19713" target="_blank">📅 20:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19712">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رائفی‌پور:
ایران به اردن حمله کرد و ۶ جنگنده اف ۳۵ را نابود کرد چون قرار بود به مراسم اربعین و مواکب حمله کنند</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/SBoxxx/19712" target="_blank">📅 20:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19711">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">منابع عربی گزارش حمله موشکی به بحرین را منتشر کردند - خبرگزاری مهر.</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SBoxxx/19711" target="_blank">📅 19:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19710">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">منابع عربی گزارش حمله موشکی به بحرین را منتشر کردند - خبرگزاری مهر.</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SBoxxx/19710" target="_blank">📅 19:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19709">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این تحلیل درست 4 روز پس از پایان جنگ 40-روزه ارائه شد و همچنان بر اعتبار آن افزوده می شود و خواهیم دید روزی می رسد که تنگه هرمز را فقط خودمان استفاده خواهیم کرد.  از همه کریدورها که محروم ماندیم و سهممان .... های باقر شد این هم از تنگه هرمز!</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/19709" target="_blank">📅 19:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19708">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvVOqspF4iN3HYim7us_DM9r3yTEYO_mj21eezJ8SO7d7AXKO_sMyOZ2P90Ump_-4KuT390ICRMxT5OTZm-fAZDoheSSWxdBlPZDdDUUl0NO4j-r0wWVrGOiheW9cb8e-L4NB1Mpp2C-qL9Ycfwau-K8bK1_bQsrXm4CPZvuf1l_05s9ZLb15StTj-ey2fePmU2sPqacf0PDhhWK75vQ1hwRK2HUAfwCOt0e1o1F8GOhbO-haF_NPYYoN5tZP9Njs2zfRMcB916Po349Pezw-ITFNDmAURQOhMJhOQWbxxQwBv5i5RxOO-GZgLFaI91C9Mth750s0Bw_crtk6XwJLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
طرح جدید اسراییل برای ساخت
پایگاه‌های نظامی در جنوب لبنان
روزنامه هاآرتص گزارش داد که رژیم صهیونیستی حدود ۲۳۰ کیلومتر مربع از خاک لبنان را همچنان در اشغال دارد و قصد دارد بر روی ویرانه‌های روستاهای تخریب‌شده، پایگاه‌های نظامی جدید احداث کند.</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/19708" target="_blank">📅 18:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19707">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/19707" target="_blank">📅 18:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19706">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">طبق وب‌سایت وزارت خزانه‌داری ایالات متحده، ایالات متحده تحریم‌های مرتبط با ایران را لغو کرده است.  منبع: رویترز</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/19706" target="_blank">📅 18:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19705">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فوری | یک مقام ارشد ایرانی به الجزیره گفت: هرگونه بستن یا باز کردن تنگه هرمز به اقدامات واشنگتن بستگی دارد.</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SBoxxx/19705" target="_blank">📅 18:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19704">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">طبق وب‌سایت وزارت خزانه‌داری ایالات متحده، ایالات متحده تحریم‌های مرتبط با ایران را لغو کرده است.
منبع: رویترز</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SBoxxx/19704" target="_blank">📅 17:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19703">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">منابع فلسطینی گزارش می‌دهند که حماس، واحدهای سازمانی، فعالیت‌های مخفیانه و عملیات امنیت سایبری خود را به ترکیه منتقل می‌کند، در حالی که قطر به میزبانی رهبری این سازمان و فعالیت‌های عمومی آن ادامه خواهد داد.
— روزنامه جروزالم پست</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SBoxxx/19703" target="_blank">📅 17:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19702">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پیش‌نویس قانون ترکیه برای حمایت از خلع سلاح و بازگشت به زندگی عادی اعضای سازمان پ.ک.ک
ائتلاف حاکم ترکیه، روز چهارشنبه، یک پیش‌نویس قانون را به پارلمان ارائه کرد که هدف آن پیشبرد روند صلح با حزب کارگران کردستان (پ.ک.ک.) است. این قانون شامل حمایت‌های قانونی برای بسیاری از اعضای سابق این سازمان و تعلیق مجازات‌های زندان برای برخی از افرادی است که به عضویت در پ.ک.ک. متهم شده‌اند.
این قانون‌گذاری، که انتظار می‌رود در اواخر این هفته توسط پارلمان تصویب شود، به دنبال پایان دادن به درگیری‌های دهه‌ها طولانی با تسهیل بازگشت هزاران نفر از اعضای سابق پ.ک.ک. است که در حال حاضر در شمال عراق مستقر هستند.
بر اساس این قانون پیشنهادی، سازمان اطلاعاتی MIT ترکیه مسئول بررسی و تأیید خلع سلاح این گروه خواهد بود، در حالی که یک کمیته متشکل از معاون رئیس‌جمهور، چندین وزیر و رئیس MIT، بر روند تسلیم و تحویل سلاح‌ها نظارت خواهد کرد.</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/19702" target="_blank">📅 16:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19701">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مقامات آمریکایی تأیید کردند که هرگونه توافق احتمالی با ایران، به طور قطعی تضمین خواهد کرد که تهران کنترل مسیر کشتیرانی تنگه هرمز را به دست نخواهد گرفت.</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SBoxxx/19701" target="_blank">📅 16:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19700">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">کونستانتینوس فلوروس، رئیس ستاد سابق ارتش یونان:  هر کسی که پا به خاک یونان بگذارد، ابتدا سوزانده خواهد شد، و سپس ما از او می‌پرسیم که کیست.  این تنها واکنش مناسب به تهدیداتی مانند: "ما یک شب سر می‌رسیم" یا "ما به جزایر شما قدم خواهیم گذاشت" است.  منبع: Proto…</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/19700" target="_blank">📅 16:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19699">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmyBbCxihbqmePaa9xYZ5DsFIfMkx1rVEbXl96tvgecZTa9PHl-g7vLbTf2-QulUC5DwIB6fGbCh_qtrz9odm2UTgKDr9rtciXrQSrO0KzgaNNJGdYn_ohHGSemrIxAmH0sj8udAUXJAx2kvgtnMcMq38xPCpEjJYA9dkgCkmuJD1IgQ1CZPvHvEycOeE3qiWofm4BkgCq6O4oyReaszb5tUvIoyTukGR9EA7DuB59ic-Nz2AExBV9BcnBpCiIJ2JKZMGtNUYC7pCJRmpmxfWaWtJmJusNZOM7z1QCHqe2oVFVPq_IhwwC35BhkItta6-a53GvnfOwg7vkWXYiF45w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنش‌های میان ترکیه با یونان دارد دوباره داغ می شود….</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SBoxxx/19699" target="_blank">📅 16:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19698">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYZPZKKLzeLhWgvcl3hnCqGUtEv91zw7u8ujxhENWGlxVZeY8VvR0Tjc26KQHPpBBoNULeOyhm06ymK5gu5ejLpvAnh18tx2U2TjIW-avdoLyItbifpdY34EClZK4U0phRt5gnN8WYtxtlyMhOoWVhaIuTodXwi-65_4LPJ4G1jfKia0I4YehxwhwAxhalaExltqe5tZnlVXwqFRooCtr7VYyRvHwqiGcx4E8_WuOsvl1JRV7IREacFMm-F19j55rcd_MYTFnfvJ0PvnQSeYj0HkMXkleqBtrb0Nsv_7k2WZSY3vE550RhCLOzXxIfEpylpg1GwVavj4-G8lE1At0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این فیلم را ببینید!  در حالی که همه هنرمندان و تماشاگران (از جمله بهروز وثوقی افسانه ای) به صورت ایستاده سرود میهنی «ای ایران» را همخوانی می‌کنند، «نون میم» با آن چهره و ریخت هیستریک ش  مثل بزهای کوهی به در و دیوار خیره شده و گویی در سالن تئاتر دنبال یونجه…</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/19698" target="_blank">📅 16:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19697">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یک مقام ارشد خلیج فارس گفت که احتمال اینکه آمریکا و ایران تا روز جمعه به یک توافق موقت برسند، ۵۰ درصد است، اگرچه هنوز گروه‌های تندرو کلیدی ایران موافقت خود را اعلام نکرده‌اند.
— سی‌ان‌ان</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/19697" target="_blank">📅 16:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19696">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یک جا آرام می شود، 13 جای دیگر جنگ می شود</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SBoxxx/19696" target="_blank">📅 16:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19695">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شب های خواهرمیانه !</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/19695" target="_blank">📅 16:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19694">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نیروهای دفاعی اسرائیل (IDF) یک هشدار "فوری" برای تخلیه ساکنان روستای المنصوری در جنوب لبنان صادر کرده است، این اقدام قبل از حملات هوایی انجام شده است.
ارتش اسرائیل:
«حزب‌الله توافق آتش‌بس را نقض کرده است و ارتش با قاطعیت علیه آن اقدام خواهد کرد.»</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/19694" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19693">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ارتش اسرائیل برای حمله ای سنگین به جنوب لبنان آماده می شود.</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/19693" target="_blank">📅 16:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19692">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حادثه دریایی جدید در دریای سرخ</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SBoxxx/19692" target="_blank">📅 15:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19691">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">422.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/19691" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 19</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SBoxxx/19691" target="_blank">📅 15:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19690">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 19</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19690" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 19
چهارشنبه 5 آگوست 2026</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SBoxxx/19690" target="_blank">📅 14:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19689">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ژاپن در حال بررسی ادغام سیستم‌های هوش مصنوعی ساخت آمریکا، از جمله سیستم هوشمند Maven شرکت Palantir و Lattice شرکت Anduril، در نیروهای دفاعی خود است تا فرآیند تصمیم‌گیری نظامی را تسریع کرده و همکاری با نیروهای آمریکا را بهبود بخشد.  برای کاهش وابستگی به فناوری‌های…</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SBoxxx/19689" target="_blank">📅 14:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19688">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmMKmqhwp134hK89Tpgywj3j6tU9TlQ60ps3e_oct52SrDiqg8_cQengurMgkFqHH1IAyebm_bI8KY6xFQ_IwoIpPmB1JTyFubXihqtjonM34FlMv1MWvf-rBe3ljzRhmDcJzySVpdre6H2cuZVLMS-o-jY8io8T_x9bi7JeHIj6VVoRbSHbRDQR4CltPB-PJuZnsh5bfD4hEMgFZ1MLzcBYMfiR5kaiXfBwTu-mRre--7JaKD2Hnq5fIs50ndNfQNr2_M1vi-eMxxKZ8WiYJ6QeuqZ1d64GkzY80q0Z-Dd-I46aLBVnv3RiQcmDe7-V2yprb8OeTacGa41vn01eDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوشش ژاپن در تقویت توان دفاعی  ژاپن با تأکید وزیر دفاع خود، شینجیرو کویزومی، بر لزوم تقویت و تحول توان نظامی این کشور با «حسی بی‌سابقه از فوریت و بحران» اصرار می‌ورزد. گزارش سالانه سفید دفاعی ژاپن، منتشرشده در ۴ اوت ۲۰۲۶، بار دیگر بر تهدیدات فزاینده چین، کره…</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SBoxxx/19688" target="_blank">📅 14:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19687">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گزارش صداوسیما درباره مذاکرات بر سر بازگشایی تنگه هرمز:  "توافق احتمالی ایران و عمان درباره ترتیبات عبور شناورها از تنگه هرمز هیچ ارتباطی با باز شدن فوری این تنگه ندارد؛ باز شدن تنگه هرمز منوط به تغییر رفتار و تصحیح تخلفات آمریکا است و در صورت ادامه تخلفات…</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/19687" target="_blank">📅 12:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19686">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">صداوسیما  به نقل از یک منبع مطلع:  توافق احتمالی ایران و عمان در باره ترتیبات عبور شناورها از تنگه هرمز هیچ ارتباطی با باز شدن فوری این تنگه ندارد</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/19686" target="_blank">📅 12:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19685">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترور ناموفق ترامپ!</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/19685" target="_blank">📅 12:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19684">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">صداوسیما  به نقل از یک منبع مطلع:
توافق احتمالی ایران و عمان در باره ترتیبات عبور شناورها از تنگه هرمز هیچ ارتباطی با باز شدن فوری این تنگه ندارد</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/19684" target="_blank">📅 12:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19683">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfGdhSbuAVA6_mvR3uV90E82Nk2Jj0kRmrvllT6JypB1n0VgEK-kQy62ZUbR3_QnaThqa-5axNoPQJ8APOBDDdS37l6lz7efumIj3mIv89sgfvS3RblWBkDe-PDNkeeG6h2Z40kyXYX8HR0MTjXuyRuctLttjygAvcI4UV2fJmraEHw7BaruUBdY8xhan5p1oGdtlfapHd54UTe9-x-YCsJdYY6_Ft_KKeHGPdoaM2KqR-jK8b1v0VO8cbOWKwZMXqz5NFyMEaUXoHgDxSyrE06YbUoF0q95BA8vQlvpoeFEwweEjZ0PmkW5zNt8AqB_4NaJod7X9zbLdbLqR5dp9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح پایینی قرار دارد و ادامه جو ریسک پذیری پیش بینی می کند.
(شخصاً با توجه به اینکه:
— عمده رشد امروز در سشن آسیا روی داده
— پس فردا گزارش NFP داریم
— اعتمادی به توافق ایران و آمریکا ندارم
اینجا خریدار نیستم و پله ای می فروشم)</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/19683" target="_blank">📅 11:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19682">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حوثی‌ها مدعی هستند که با موشک‌های بالستیک، تانکر نفتی سعودی به نام «وفا» را در دریای سرخ شمالی، در نزدیکی ساحل ینبع مورد هدف قرار داده‌اند و ادعا می‌کنند که اصابت مستقیم رخ داده است.
این هشتمین تانکر نفتی سعودی است که از زمان آغاز محاصره دریایی در تاریخ ۲۲ جولای، مورد هدف قرار گرفته است، و حوثی‌ها مدعی هستند که ۲۹ تانکر سعودی دیگر را نیز مجبور به بازگشت در دریای سرخ و دریای عرب کرده‌اند.</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/19682" target="_blank">📅 11:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19681">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLibokS_gXVvFgwM-YLROsX8ZE_Au8U_d1zAiFgLHuiWST9zmTaYeQTMc4PxCgG3FOQL3q99j_Q1P35iiOvQiYMl1QVV4wgTIEY89SQzdpVcdpPEbKDrmOmuFaSpTCnEeZNce2L7X94XIaE4UnuEj4ac-GzPP7qiAjsWPycOqVQexdxOiAhnBOlkd34XIlEA70BRJb2gnM_BAGC-e0hExFPAkVaTsUyXfxt-bwaOCuIYWjgL-Fqvt6iAxS5zI4PeiH7nDXer4JVcTFHpelh0MmLxw0M-pTWZ-fjjWxLQWdGROmC6GPmKoVh1SXsxq6kLEfCYUlPzljw30hFgTnrEKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید جدید ایران برای قدرت هوایی آمریکا
خرید موشک‌های شانه‌پرتاب چینی توسط ایران و پیامدهای آن برای عملیات‌های آمریکا
چین در حال ارسال ۳۰۰ تا ۴۰۰ دستگاه موشک دفاع هوایی شانه‌پرتاب (MANPADS) از نوع QW-12 و FN-16 به ایران است. این معامله که ارزش آن ۶۰ تا ۷۰ میلیون دلار برآورد می‌شود، قرار است طی هفته‌های آینده از طریق پاکستان و به صورت هوایی یا زمینی تحویل ایران گردد. این موشک‌ها، با هدایت مادون‌قرمز، قادرند پهپادها، بالگردها و جت‌های آمریکایی را که در ارتفاعات پایین پرواز می‌کنند، تهدید کنند.
هدف اصلی ایران از این خرید، بازسازی دفاع هوایی کوتاه‌برد پس از پنج ماه حملات مکرر آمریکا و اسرائیل است. این حملات، آسیب‌پذیری‌های زیرساخت‌های نظامی ثابت ایران را آشکار کرد. موشک‌های جدید، به ایران اجازه می‌دهند تیم‌های سیار و پراکنده‌ای را در اطراف سایت‌های استراتژیک مستقر کند که امضاهای راداری بسیار کمی دارند و شناسایی و نابودی آن‌ها دشوار است.
از نظر فنی، QW-12 با سر جنگی ۱٫۴۲ کیلوگرمی و برد ۰٫۵ تا ۶ کیلوگرم قادر است اهدافی را در ارتفاع ۱۰ متر تا ۴ کیلومتر درگیر کند. جستجوگر مادون‌قرمز آن می‌تواند جت‌ها را در فاصله بیش از ۹ کیلومتر تشخیص دهد و احتمال نابودی در شلیک اول آن بیش از ۸۰٪ است. FN-16 نیز برای درگیری کوتاه‌برد با پهپادها، بالگردها و هواپیماهای کم‌ارتفاع طراحی شده است.
این معامله، علاوه بر توافق قبلی ایران با روسیه برای خرید ۵۰۰ پرتابگر وربا و ۲۵۰۰ موشک به ارزش ۵۹۱ میلیون دلار (تحویل تا ۲۰۲۹)، توان دفاعی ایران را به‌طور چشمگیری افزایش می‌دهد. چین و پاکستان این گزارش را تکذیب کرده‌اند، اما دونالد ترامپ اعلام کرد که چنین ارسال‌هایی مغایرت مستقیم با قول شی جین‌پینگ دارد.
آمریکا در حال حاضر با کمبود پهپادها مواجه است. از آغاز عملیات در ایران، ۳۰ فروند MQ-9 Reaper سرنگون شده‌اند. با در نظر گرفتن خسارات جنگ یمن، آمریکا یک‌سوم از ناوگان ۱۳۵ فروندی خود را از دست داده است. خط تولید Reaper در ۲۰۲۵ متوقف شده و هر فروند ۵۶ میلیون دلار قیمت دارد، بنابراین جایگزینی آن دشوار است.
این موشک های دوش پرتاب نمی‌توانند هواپیماهای بلندپرواز را تهدید کنند، اما پهپادها و بالگردهای آمریکایی را در ارتفاعات پایین در معرض خطر قرار می‌دهند. برای مثال، در آوریل ۲۰۲۶، یک موشک دوش پرتاب ایرانی به یک بالگرد HH-60W آمریکایی اصابت کرد. همچنین، یک A-10 و یک F/A-18 در ماموریت‌های کم‌ارتفاع آسیب دیدند.
این موشک‌ها، به دلیل سیار بودن و عدم نیاز به رادار، قادرند حمله‌های غافلگیرانه انجام دهند. آمریکا برای انجام ماموریت‌های ISR (اطلاعات، نظارت، شناسایی) و جستجوی نجات رزمی (CSAR) مجبور است در ارتفاعات پایین پرواز کند، که این امر آن‌ها را در معرض تهدید قرار می‌دهد.
در نتیجه، ایران با استفاده از این موشک‌ها می‌تواند هزینه‌های جنگ فرسایشی را برای آمریکا در ارتفاعات پایین افزایش دهد. اگرچه آمریکا آسمان ایران را کنترل می‌کند، اما ایران می‌تواند با تیم‌های پراکنده موشکی پدافندی، عملیات‌های آمریکایی را پیچیده و پرهزینه‌تر کند.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/19681" target="_blank">📅 08:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19680">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">به عنوان بخشی از این توافق که بین کشورهای ساحلی ایران و عمان در حال مذاکره است، ترافیک ورودی از طریق یک مسیر شمالی واقع در آب‌های سرزمینی ایران وارد تنگه هرمز خواهد شد.
ترافیک خروجی از آب‌های عمان «با هماهنگی با ایران» (یعنی با مجوز صریح از نیروی دریایی سپاه پاسداران انقلاب اسلامی) خارج خواهد شد.
این توافق موقت به مدت ۶۰ روز طول خواهد کشید، در طی آن هیچ عوارض یا هزینه‌های دریایی دریافت نخواهد شد. در عرض ۳۰ روز، هر دو طرف تلاش می‌کنند مین‌ها را از مسیر میانی تنگه هرمز پاکسازی کنند و به یک حل و فصل دائمی نهایی دست یابند.</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/19680" target="_blank">📅 08:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19679">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دونالد ترامپ
:
ضربه واقعی هنوز در راه است و امیدواریم مجبور به استفاده از آن نشویم.
آنها دوست ندارند این را بپذیرند، اما می‌دانید، کمی نگران‌کننده است. شما به مردم می‌گویید که ما مذاکرات خوبی داریم، و بعد کسی از ایران می‌آید و می‌گوید: "ما ملاقات نکرده‌ایم." این یک دروغ است. آنها می‌خواهند معامله کنند
سوال: اگر ایران دوباره عقب‌نشینی کند، آیا این پایان کار است؟
ترامپ: خب، اگر آنها دوباره عقب‌نشینی کنند، ضربه بسیار بسیار سختی خواهند خورد.
تنگه خیلی زود باز خواهد شد، یا خیلی محکم به آنها ضربه زده خواهد شد و تنگه باز خواهد شد. آنها با من تماس گرفتند و خیلی مودبانه گفتند: "لطفا، می‌توانیم صحبت کنیم؟"
سوال: چه زمانی می‌گویید دیگر بس است؟ و آیا راهی برای بازگشت ایران وجود دارد؟
ترامپ: من وقت زیادی دارم
ما کنترل کامل تنگه هرمز را در دست داریم.
روز خیلی خوبی بود. ایرانی‌ها دوست ندارند این را بگویند. آنها همیشه ادعا می‌کنند که ما در مورد آن بحث نکردیم. اما مردم فهمیده‌اند که این درست نیست.
اگر تنگه هرمز باز شود و به هر حال تا حدی باز است.
قیمت بنزین به ۲.۵۰ دلار در هر گالن کاهش می‌یابد.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/19679" target="_blank">📅 07:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19678">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ:
گفت‌وگوهای بسیار خوبی با ایران داریم.
تنگه هرمز به‌زودی باز خواهد شد یا ایران هدف ضربه‌ای فوق‌العاده سنگین قرار می‌گیرد</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/19678" target="_blank">📅 07:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19677">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpABx9ad5vuPvhnNf6UXeK5yipc9WrcpFbgqZNi4K-oGVol0Gpo7MIrFh8Iyo3QiidgnlET1b54ICMsLdvswqGoOq0aiCXYqnpraJdsTkUpl0Pocd-1dwOacwuphBWg0xP6wjyJ_VMS2d-vTshZZDH6oUoyKJlvqoP3OmNDbStUcymhnO2RHVs1TjqAEPvT1Rj00rYeEBqzVRw9xLrJymq8jQqbhyS7tvUSL1pe-CGsKZw3bKw3OxIIl5EYPGlaD0VvTHbnAfjo8NfnEZX0Rh_vvtkRV07Bcg3vIdgZ7RfoMLdH997pQJ6LELc_nWqybxSHKtaPhzY3l-u56Vzy9pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژاپن پس از آنکه کشتی‌های جنگی چینی، به همراه یک کشتی روسی، در داخل منطقه‌ای که توکیو آن را منطقه اقتصادی انحصاری (EEZ) خود در نزدیکی جزیره اوکینوتوری می‌نامد، رزمایشی با گلوله‌های جنگی انجام دادند، به چین اعتراض کرد.  ژاپن اعلام کرد که این رزمایش طبق قوانین…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/19677" target="_blank">📅 07:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19676">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ارتش ایالات متحده تقریباً ۸۰ درصد از پیشرفته‌ترین موشک‌های رهگیر THAAD خود را مصرف کرده است
سی‌ان‌ان</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/19676" target="_blank">📅 04:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19675">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شب های خواهرمیانه !</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19675" target="_blank">📅 03:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19674">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حملات هوایی عربستان به صنعا</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/19674" target="_blank">📅 03:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19673">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترور ناموفق ترامپ!</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19673" target="_blank">📅 02:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19672">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حملات هوایی عربستان به صنعا</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/19672" target="_blank">📅 02:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19671">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سنتکام
:
مسیر جنوبی از تنگه هرمز همچنان برای تمام کشتی‌های تجاری که به دنبال عبور از این آبراه بین‌المللی هستند، آزاد و باز است.
در طول سه ماه گذشته، نیروهای ایالات متحده به بیش از ۱,۰۰۰ کشتی در عبور موفقیت‌آمیز از تنگه، علی‌رغم تهاجم بی‌دلیل ایران، کمک کرده‌اند و این عبورها امروز نیز ادامه دارند.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19671" target="_blank">📅 02:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19670">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWsquV7o9QGdJsI3jAvlsktypIMRk2Lfp50rgD_7fe36QPDZqzhfUkPUyedBNlnSn9UpBJLWq13Bka7v4CY3iQQpiPDoiodUFZfgig3ReHxiXjsp1adO622uXiiJIGr2dQIqFelvvclWjh_RU66LU6hAA73RihsMcgScxA_NDsDLcdUrC3sq6GtRxb3gaCMVTCAsuBl4rJ88cZic2fLBOfqXBcipgRptDLuneKnBQFlMeHD5PAcw2Mdwl3RCmM-6wXFy_pr35h56Ku7ZMbB9RbwmXW4vCUWqtcYYRQxzIjI39OwAuVF6hu6JfWFhBEBRvJfla7nUzQy2r_QmddI3YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگه های مهم دریایی جهان و میزان نفت عبوری از آنها
ابتدا تنگه مالاکا و سپس هرمز.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19670" target="_blank">📅 01:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19669">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">روبیو، وزیر امور خارجه آمریکا: پیشرفت‌هایی در مذاکرات با ایران حاصل شده، اما هنوز توافق نهایی وجود ندارد.  روبیو گفت: «ما در مذاکراتی بین عمان و ایران در مورد بازگشایی تنگه هرمز برای تردد کشتی‌های تجاری شرکت داریم» و افزود: «امیدواریم این اتفاق به زودی رخ…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19669" target="_blank">📅 01:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19668">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xaw4WInpz1QNsabszVpTIkZ94X3PgXHoAExkyeyoqWLR-yQenr62lO_ydM3Da3_sph9fsT6azOD9VsHn9e_m2s4ZdKyRp0q0cXHOZo29-1HUl0ckkvD9S3A-WUiVi2cBmKoi_qyW6Z94ca52OT7-FCpOcTuSlW02lEvitEBk-ZNgyvoBgFV1Oa2R7SP3ewFrdakRCmmMMIe0h8yHVL-NZMFn-Q2zWUQ0WpmqtSKnBzIGVQs5z8GYTvHnkFsX6lKBv652K-YpQ5OEUQYG1VWkrqBp4iQuMx7taRsymIg4smkJ7XGShELDIn8HLJlVqPPn8g64QNKGExaJfC79tKoYqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح بالایی است. پس از رشد مناسبی که طلا از کف دیروز داشته، توصیه می شود امروز با احتیاط برخورد بشود و بالای 4090 اگر برود قطعاً محدوده فروش است.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19668" target="_blank">📅 01:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19667">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IN9L3xOOlA5I_K3wK0TeL3w-hTKZcvdjcSdus2SklPdsmFfE3b4foMtdX7yjW54p4DTZAK5W1_aZmT-SjjyeX3q3V2sGcmh0jGG91K9VCDrAKdB6VguHli2VTMfMws2WMjYiTeQN-QuHRJCBfVcMGg4JXgq4wySJFqLKEgiYKOO8_r-qbZ1axgYClUToOQ8ESFB8U3NDcuI0_0rq2e167vGvkvjps7JlUq7gx6hastcwCj8XrDnzRpSAWeCw-76kc325BsNIQLxT4MACak7EjEyu-UzwF3u9iEiGRCK6DiHtO1NjsyYdbtweyU787zEOFGxzCG6Y7xqdcxlXORbVXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
احیای بخش تولید آمریکا شتاب می‌گیرد  شاخص ISM تولید آمریکا در ژوئیه به ۵۵.۶ رسید و رشد همزمان تولید، سفارش‌های جدید، اشتغال و صادرات نشان داد که بخش صنعت پس از سال‌ها ضعف وارد مسیر احیا شده است. با وجود این بهبود، فشار هزینه‌های تولید، اختلالات زنجیره تأمین…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/19667" target="_blank">📅 00:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19666">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ایران در حال بررسی طرحی برای بازگشایی تنگه هرمز از طریق ایجاد یک صندوق داوطلبانه است که توسط کشورهای خلیج فارس و کشورهای اروپایی که به این مسیر وابسته هستند، تأمین مالی می‌شود.  به جای اعمال عوارض رسمی، این صندوق هزینه‌های ناوبری، حفاظت از محیط زیست و خدمات…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19666" target="_blank">📅 23:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19665">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ایران در حال بررسی طرحی برای بازگشایی تنگه هرمز از طریق ایجاد یک صندوق داوطلبانه است که توسط کشورهای خلیج فارس و کشورهای اروپایی که به این مسیر وابسته هستند، تأمین مالی می‌شود.
به جای اعمال عوارض رسمی، این صندوق هزینه‌های ناوبری، حفاظت از محیط زیست و خدمات جستجو و نجات را پوشش خواهد داد، مشابه مدل موجود در تنگه مالاکا.
این پیشنهاد که به گفته منابع از عمان حمایت می‌شود، می‌تواند یک راهکار قانونی فراهم کند، زیرا قوانین بین‌المللی اجازه دریافت عوارض عبور اجباری در گلوگاه‌های کلیدی کشتیرانی را نمی‌دهند.
منبع: تلگراف</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19665" target="_blank">📅 23:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19664">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENRD2KwtWh8Y4zqVDlTiIKgl4sbLETKbMKm3sHzw4X8cWXBIcPIPDrzfqZcFDX6kcqgDIuBTryKe_9sx5jlleewRmexAMnEPGDWLKwKHwHArpdqtJ2jUJRtWzOvCFlTPueHNh-45Zj-NE1uSj0Bv5nwK5PcqZTIdYPz6_fgP8vsuPQC1GuAFG8q3-ma5Qlppbo88saQbSjBYyOWRvIfQR4pjW_DDia7x6bSwQ_0xGK9dc6mJDrHkS9fnqCiGz9jrxiiOOIlxj6oDgLMeNuGTfINHXp5CmiHjet_vWvTo2JCTo0t0EVTXKGtFypS1STAnmxc9XPD63byUCiyMwAhYrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏳
سوپر اپلیکیشن بله بعنوان اولین لژیونر اپ های داخلی وارد اپ استور شد</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19664" target="_blank">📅 22:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19663">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ایران سیگنال داده است که مایل به بازگشایی تنگه هرمز است، اما در عین حال حق دریافت هزینه‌های عبور، تضمین‌های امنیتی در برابر حملات آینده، پایان محاصره دریایی ایالات متحده و تخفیف تحریم‌های نفتی ایالات متحده را مطالبه می‌کند.  منبع: WSJ</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19663" target="_blank">📅 22:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19662">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ایران سیگنال داده است که مایل به بازگشایی تنگه هرمز است، اما در عین حال حق دریافت هزینه‌های عبور، تضمین‌های امنیتی در برابر حملات آینده، پایان محاصره دریایی ایالات متحده و تخفیف تحریم‌های نفتی ایالات متحده را مطالبه می‌کند.  منبع: WSJ</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/19662" target="_blank">📅 21:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19661">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">روبیو، وزیر امور خارجه آمریکا: پیشرفت‌هایی در مذاکرات با ایران حاصل شده، اما هنوز توافق نهایی وجود ندارد.  روبیو گفت: «ما در مذاکراتی بین عمان و ایران در مورد بازگشایی تنگه هرمز برای تردد کشتی‌های تجاری شرکت داریم» و افزود: «امیدواریم این اتفاق به زودی رخ…</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/19661" target="_blank">📅 21:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19660">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19660" target="_blank">📅 21:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19659">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سبحان الله!</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19659" target="_blank">📅 20:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19658">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_LI-Yw9OiOkDzvS1xk14KCwXhp3RVKCSDCu9HtXPb9B1qFsaQ8tdRNvm7L7QoShVWyr5_NyiuVUzWiRytgxdqaKYpWpNDZvUrQ6T_ze5dfO0aKC7gvM-Yj9fURy_PD5ltnqQQTxiQshJ2hKaTf8HZaNgpX2o2Rgk84e2KsJS4-EZAaBXFsQL90shFxuSsKokw1RZM8wYTOqugt35Ey5yo4-TtK675gAaj7oqxysYrsnOo1tLskZ_dqKR37k0izXU58UOQ1q_JMZ6zJiruWn6nhl5tAf-5r1s2uuaqwp4SSrxtIT5V2GiKPWmQeRU-y0kzDjABR2yeqU4gSOeCJzNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  محسن رضایی: منتظر نفت ۱۵۰ دلاری طی روزهای آینده باشید.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19658" target="_blank">📅 20:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19657">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">روبیو، وزیر امور خارجه آمریکا: پیشرفت‌هایی در مذاکرات با ایران حاصل شده، اما هنوز توافق نهایی وجود ندارد.
روبیو گفت: «ما در مذاکراتی بین عمان و ایران در مورد بازگشایی تنگه هرمز برای تردد کشتی‌های تجاری شرکت داریم» و افزود: «امیدواریم این اتفاق به زودی رخ دهد.»</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19657" target="_blank">📅 20:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19656">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ایران در حال بررسی اجازه دادن به کشورهای اروپایی برای خنثی‌سازی مین‌ها در تنگه هرمز است، امتیازی که می‌تواند بخشی از یک توافق برای عادی‌سازی حمل‌ونقل دریایی در این مسیر و تسهیل مذاکرات صلح با ایالات متحده باشد.
ایران بارها به‌طور علنی اعلام کرده است که اجازه نخواهد داد کشورهای خارجی در تلاش‌های خنثی‌سازی مین در این مرکز حیاتی حمل‌ونقل نفت و گاز طبیعی مایع‌شده مشارکت کنند. با این حال، طبق گفته دیپلمات‌هایی که با این وضعیت آشنا هستند و به شرط ناشناس بودن درباره مسائل حساس صحبت کردند، تهران در جلسات خصوصی در هفته‌های اخیر موضع خود را تعدیل کرده است.
وزارت خارجه ایران بلافاصله به درخواستی برای اظهار نظر پاسخ نداد.|</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19656" target="_blank">📅 19:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19655">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">غرق شدن کشتی هندی در ساحل یمن  به‌گزارش برخی منابع یک کشتی هندی در فاصله ۱۳ مایلی جنوب حدیده، توسط نیروهای انصارالله مورد حمله قرار گرفته است. این حمله با استفاده از یک قایق انتحاری انجام شد و در نتیجه، کشتی غرق شد.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19655" target="_blank">📅 18:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19654">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حتی وقتی کشتی طوری ش نمی‌شود، هندی ها تلفات می‌دهند</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19654" target="_blank">📅 18:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19653">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">العربیه : تا ساعات آینده بیانیه بازگشایی تنگه هرمز، رفع محاصره و از سر گیری مذاکرات اعلام می‌شود</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19653" target="_blank">📅 18:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19652">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">323.7 KB</div>
</div>
<a href="https://t.me/SBoxxx/19652" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 18</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19652" target="_blank">📅 16:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19651">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 18</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19651" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 18
سه شنبه 4 آگوست 2026</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19651" target="_blank">📅 15:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19650">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گروه حوثی‌های یمن اعلام کرده‌اند که یک حمله دقیق با استفاده از پهپاد علیه یک "هدف حساس" در فرودگاه نجران در عربستان سعودی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19650" target="_blank">📅 14:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19648">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hZpPViQHeAJ6Gpt7p5tYqBu2g_cfdu46D_V2VS9Yx-TnrQNcuuUd2o_Ncm0TBbj963-vKj2XSIGm0WftxOaSQMs1S2GymtVHTkVugahpVGCdxb-mS-Xwqz5yEAP0D3U5YLRgDuQIHYHA_jupyk-n022cDBgX6p9syGVPhlN6cnEoS-eDWoTgNND9VmSgsM7QKJbSqjOWsfKwfeHJ2dlBeJ8aLIVV7GaR6K61MrvTlmcv_nLIf85RS-PRfkWgUWWMn09i0ZKyy5qIKTClNeNCvyl2YVK2snX1gcuyRnIItVqQ-dhdrDrG480S0EONgkjMhzdjvytigJS1Z8k2DQnM5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s4z9mnpofGm_zcynXn0aRz4IzEZ9gY0pgy9VYrZXy_geSJ80LTStDrH5wvaOPW4yVzVnBH_XYCZnRWYNhp-27dHOy4yOQ5evT4hoD6mi5H1kkOffYOwC_8o3jZJ6lQ1noYUAGsLHJiGbJGNm3bN-hSEEcdLyJh_gt2ySsPNKiVeaRuO1GCgWyN6s9tGhuWLOaf8Og7AnleYliARc-G4yOKKeFVabIVMhMOMgHx94sr89biNI8B-IurM8K4nMelnZEKHmHzwe7JtMrPfC9KUAm9V3vJ3rOb__Dmh3z5dwiAAgCjQASr2-a-bbsalctk8ju9721oO5bvCKUZ9lVfenqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بهره‌برداری از آسیب‌پذیری‌های داخلی آمریکا
محاسبات ایران تا حد زیادی انتخابات میان‌دوره‌ای آمریکا را نیز در نظر گرفته است. تهران بر این باور است که دونالد ترامپ، رئیس‌جمهور آمریکا، در شرایط افزایش قیمت سوخت و کاهش حمایت عمومی، تمایل چندانی به ادامه دادن یک جنگ نامحدود ندارد.
این درگیری شش‌ماهه تاکنون به کشته شدن ۱۸ نظامی آمریکایی از ماه فوریه منجر شده و فشار نمایندگان جمهوری‌خواه در کنگره برای ارائه یک راهبرد روشن جهت خروج از جنگ را افزایش داده است</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19648" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19647">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHk3UIdnewRel_x-FLIAF9oS0z224qC8vXCl78kAc_KxxxYgvhK9kQO_iIlw9k5qb5yR4pCiI-_qUaPHLUpttpCJ-EJIyJe5PpBxEJSipVV7RlG6-dtf-kLRQu4ZbdD1jNGHSbo9qnrdNiDxqjIxyIRp7_InWGocFrjDi6iBcJN3rchR6wMy6KRO50Z1eRHf1mFlEY7LcNUkqJp69H_9Q_ZpJHgL012CN241DFzcAYCu-2MkaAk8-6F03-cQQkN4Z2mMIReRdnG-w81xO4lswqY0jLp52hAO23SldR2ZepfHxtc1w-8CyyH9GA9Q0Izz3MFgvvra6BAxBhpsk0lGSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادداشتی به قلم « احمد کوچاک»
ایران روی اخلال اقتصادی برای وادار کردن آمریکا به امتیازدهی حساب باز کرده است
ایران در حال اجرای یک راهبرد فرسایشی حساب‌شده در سراسر خاورمیانه است و با استفاده از مسیرهای کشتیرانی جهانی و زیرساخت‌های انرژی به‌عنوان ابزار فشار، تلاش می‌کند اراده واشنگتن را فرسوده کند. تهران بر این باور است که افزایش هزینه‌های اقتصادی در نهایت آمریکا را به دادن امتیازاتی درباره کنترل تنگه هرمز وادار خواهد کرد.
تهران در حال اجرای یک کارزار فرسایشی حساب‌شده علیه ایالات متحده است و کریدورهای تجاری و شبکه‌های انرژی خاورمیانه را به نقاط اصلی اعمال فشار تبدیل کرده است. این راهبرد از رویارویی مستقیم نظامی پرهیز می‌کند و در عوض بر افزایش هزینه‌های اقتصادی و لجستیکی ادامه این تقابل متمرکز است.
رهبران ایران بر این باورند که می‌توانند واشنگتن را پشت سر بگذارند؛ به این معنا که هزینه حفاظت از کشتیرانی بین‌المللی برای آمریکا و متحدانش را آن‌قدر افزایش دهند که در نهایت پذیرش خواسته‌های دیپلماتیک تهران برای واشنگتن کم‌هزینه‌تر از ادامه وضعیت موجود باشد.
گسترش نقشه تهدید
عملیات ایران دیگر به تنگه هرمز محدود نمانده و میزان تحمل آمریکا در برابر اختلال در چندین گلوگاه دریایی را هم‌زمان آزمایش می‌کند. اکنون تهدیدها دریای سرخ، تنگه باب‌المندب و زیرساخت‌های انرژی عربستان سعودی را نیز دربر گرفته‌اند.
این پراکندگی جغرافیایی، نیروهای دریایی بین‌المللی را وادار می‌کند مأموریت‌های اسکورت و حفاظت دفاعی بیشتری انجام دهند؛ اقدامی که منابع غرب را فرسوده می‌کند، بدون آنکه الزاماً توازن نظامی منطقه را تغییر دهد.
مایکل نایتس از مؤسسه واشنگتن می‌گوید:
«ایران از همان ابتدا تلاش کرده است با گسترش گزینه‌های تشدید تنش خود، آمریکا را در این زمینه پشت سر بگذارد؛ به‌گونه‌ای که همیشه بتواند هر هفته چیز جدیدی ارائه کند: جغرافیای جدید، نوع جدیدی از سلاح یا نوع جدیدی از هدف.»
بهره‌برداری از آسیب‌پذیری‌های داخلی آمریکا
محاسبات ایران تا حد زیادی انتخابات میان‌دوره‌ای آمریکا را نیز در نظر گرفته است. تهران بر این باور است که دونالد ترامپ، رئیس‌جمهور آمریکا، در شرایط افزایش قیمت سوخت و کاهش حمایت عمومی، تمایل چندانی به ادامه دادن یک جنگ نامحدود ندارد.
این درگیری شش‌ماهه تاکنون به کشته شدن ۱۸ نظامی آمریکایی از ماه فوریه منجر شده و فشار نمایندگان جمهوری‌خواه در کنگره برای ارائه یک راهبرد روشن جهت خروج از جنگ را افزایش داده است.
چرخش به سمت دیپلماسی
واشنگتن در حال حاضر برخی عملیات تهاجمی برنامه‌ریزی‌شده خود را متوقف کرده و به دنبال امکان آغاز مذاکرات با میانجیگری عمان است. این تغییر رویکرد پس از رایزنی‌های فوری با متحدان منطقه‌ای، به‌ویژه عربستان سعودی، صورت گرفته است؛ متحدانی که خواستار کاهش تنش برای حفاظت از دارایی‌های آسیب‌پذیر انرژی در خلیج فارس شده‌اند.
دولت آمریکا در این توقف تاکتیکی، دولت اسرائیل را نیز به شکل محسوسی در حاشیه قرار داده و ثبات در خلیج فارس را در اولویت قرار داده است.
با وجود گشایش دیپلماتیک، اختلاف اصلی بر سر تنگه هرمز همچنان حل‌نشده باقی مانده است. آمریکا خواستار آن است که این آبراه به‌عنوان یک مسیر بین‌المللی باز باقی بماند، در حالی که ایران بر حاکمیت مدیریتی خود و حق دریافت عوارض عبور تأکید دارد. اما تهران حاضر نیست از موضع ضعف وارد مذاکره شود و با استفاده از تهدید به گسترش اختلال اقتصادی تلاش می‌کند برای خود اهرم فشار ایجاد کند.
ری تاکیه، مشاور پیشین وزارت خارجه آمریکا، می‌گوید:
«اگر قرار باشد مذاکره‌ای انجام شود، ایران شرایط آن را تعیین خواهد کرد.»
در نهایت، رویارویی کنونی بیش از آنکه صرفاً یک تقابل نظامی باشد، آزمونی برای تاب‌آوری نهادی دو طرف است. ایران بر این باور است که ساختار داخلی آن می‌تواند تحریم‌های طولانی‌مدت را برای مدت بیشتری تحمل کند تا ائتلاف تحت رهبری آمریکا بتواند نوسان دائمی در تجارت جهانی و بازارهای انرژی را تحمل کند.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/19647" target="_blank">📅 13:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19646">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گزارش‌ها از شنیده شدن صدای انفجاری در شهر صنعتی شمس‌آباد، واقع در جنوب تهران، خبر می‌دهند.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/19646" target="_blank">📅 13:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19645">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKazjUYkIyPF5e4olYwGnwfNrajfq6A9h5WTj5g4ZUGvx1PklqTjAPcJ9i_WFBK9TZL_sPfhhoBumqtvo2LK5mpq_nnbVqUkM9_6R2oSs7FxZZhHxKfi6LmZ12Jr4Xb5lEF4oiU_Oq97to00QuvUGANQOibIoOgaJ43M54W36azaF1qRVT2uV_-OVbsjHTzN4U8EW6Vw7tIntvPGH7boSkGhrnZULkFlh3eQnxe7NXLOSzgQ-1OPVIScxrsKeQC73rc-BQnysGeahBNPZsNy3BHhLxuf-nfEhZ6qgfG5FqKkVMxSoMKzvzDpuLGzZOUkdcXxwzZS-CJ_sitH5_M6Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در حال احیای صنعت آمریکا است و این مسئله در گزارش درخشان دیروز PMI کارخانه ای آمریکا بازتاب یافت.  یادداشتی در این خصوص منتشر خواهدشد.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19645" target="_blank">📅 13:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19644">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNipGhVIvRt7kE0ummdU3Mgxclweoy7767-daTE1TAMcY9jAelCEJzEZ26aNBEoWwDT62HDZy5OjWx2mZK1_MLrazJzuHYWNrKinn9M67tDkTKRpYMlEbaf9RH1m3-FQZr1xiHaxcT34Aps7uqWFH1rLheB0rmaPaPUQwu3kQUlVSWG-IaeDh3tjvJPqQl-6ukFXIiMRom4UR8PnfGsRy1jRCI3ZDyKv8JMF6xf8ZBUx9fcswgYMXqU49N7tzD-9MgYidSJidse7ta9v_E8VdC2LmMnrSFjTWSmVZZUApSf6SsK0dmqqR9qd-tLnlRx9jUBN6KiAdJNmaixdSaUKMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Geomarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19644" target="_blank">📅 11:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19643">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhTNWYBc_YqVCL8Elsx12gTVWCoGfLEPhkpcYN4Z-NNlpkD-Lapul_cipntPQJgrKx7ARf-9uWqqOKnUnlM-S4KnN6qiBLZO9gtq6JyefsUSsXFbwMcyy2AnxiqfdxOuUqG6Ba9gc3Va4EZq-I2q-juiJvsXn-5RUcyp_RAJ2I3X-p30BjrNk0h9ZCmX_bQvHS878Hc99QdQ6KYPzRCJlJMXHgYG0aTxjMVTWauqndBzwBVS4s5VWtklqIUhFlBIiDH9wTaua9hfKeNh77QlV12m-97V59-t5Rg2IWvCFjmfjHdlqFR0ybmjEFQXWiM8xd5jxrbQktGiI9vIH36xzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح بالایی است. پس از رشد مناسبی که طلا از کف دیروز داشته، توصیه می شود امروز با احتیاط برخورد بشود و بالای 4090 اگر برود قطعاً محدوده فروش است.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19643" target="_blank">📅 11:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19642">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svgUr5kqHSZ1BgG-nvnYnR1phqOsM2Z1KS1jqRcphQ3rkLFYNUSOQuKu7fNgkej-owUVv27sWcc48h8-Vt7LZRlw4UwSSDPmfk0KUhEGsO40yf4utEWMlfFxKbROBTpiSsPuXixgpsXI2QPLysF4RI7gsn5-ip5NnOjcnuof_am13uV8nt2dqh1x0D3oOpOv9dhKNPbVsqfxt3ejywZ_cOqSF8KskxqJ09C29F23U9_zbcARIj9NEICgdDQr78cuGaJyQTBLIDfvWY1rJjJL_q4wnPdjv9naub1JAp9XiR-QnuDb31hnGzdmizpv5q6zvtaCUjAZPLxE9y5JdWjP8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
آیا بخش تولیدی اقتصاد آمریکا در دوران ترامپ احیا شده است؟   داده‌های اخیر PMI نشان از رونق و رشد چشمگیر بخش تولیدی آمریکا در اوایل ۲۰۲۶ دارد که می‌تواند ناشی از سیاست‌های حمایتی و استراتژیک دولت ترامپ باشد.  با این حال، این بهبود به دلیل کاهش اشتغال و تغییر…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19642" target="_blank">📅 10:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19641">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ایران و عمان به توافقی نزدیک شده‌اند تا پس از ماه‌ها اختلال، مجدداً تردد کشتی‌ها را از تنگه هرمز از سر بگیرند.
مهم‌ترین مسئله مورد اختلاف این است که این توافق پیشنهادی می‌تواند به ایران نفوذ بیشتری بر این آبراه بدهد.
مقامات ایرانی می‌گویند که کشتی‌هایی که وارد خلیج فارس می‌شوند، از یک مسیر نزدیک به ایران عبور خواهند کرد و هزینه‌ای را پرداخت می‌کنند که بین ایران و عمان تقسیم می‌شود. در مقابل، مقامات آمریکایی این ادعا را رد می‌کنند و می‌گویند که ایران هیچ اختیاری برای دریافت هزینه یا کنترل تردد نخواهد داشت.
منبع: نیویورک تایمز</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/19641" target="_blank">📅 10:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19640">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oE1ZJHP28g4xd2xSxuq2M3DG2Y9DnesP200y9youmwBa9q4HVFaI3N38kEri8K03JtfzQlKOTSuc2vYJq_hGqUJbaitd9XKgV4Y0Hn2G_kz1--PqiaUoGGa8qD-185ZTCmUS3Bg8WQ0sQPAvRahFym01D5MD7l9sYK6LpI7eSrg6OUJED0l4SZycSGm7itlF4v9FUKKcwn2B0et4jG3r5kFPqJjWOWrFJNXuNUHSzre21PVTJx-gXdgrrjnsq3dxlxiCSL9jQw1uTdTqH2RbN6_qqTNvhB0Sh7RBAkUYlqq4RAfkGJYjYEF3um8YUYfTKzYu86HAhm-qKzHuJCx8xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار پایینی قرار دارد و پیش بینی می شود که طلا رشد مناسبی (دستکم در حد 400 پیپ) را تجربه کند.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19640" target="_blank">📅 00:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19639">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">#USOIL — H2  محسن رضایی: منتظر نفت ۱۵۰ دلاری طی روزهای آینده باشید.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/19639" target="_blank">📅 00:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19638">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISnA7F1s94A2-5ZLLHN-4n8FjW5MdcAO1e7JtkSRMShHUHmln8zxE8SW5cuhHIsHE3fhPAKn7po2aKvpZYPDVo8ZHLeCgsFKUCihzrxHwDtWcCSu4Hn1rJMeqzYofM4TS5QrMnvnKpbX7lxPAkJhkyMKZtg3JWHmwrsfxS-9-liq3X6KMDryPwvYRVvDVoy7NENLx5xmKVQRPiTCEtwSU_uWLPlY5QgsrJMj7vE48q4P3ehR4lg833iAY2oYhfPFRPeBcmrYta6Ix_ii4VEq3dVC_DLV4pp8dDasXzNBxiu4tqPcILK3-2DqWySU_Uwx7u7_5MZXKiv5tSmgTxz0Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  به نظر تارگت 2 را می شود دستکم 120 درنظر گرفت.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/19638" target="_blank">📅 00:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19637">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یک منبع آگاه به خبرگزاری رویترز:
ایران در 24 ساعت گذشته حداقل 3 پهپاد به سمت کشتی‌ها در هرمز شلیک کرده است.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/19637" target="_blank">📅 23:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19636">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">در حال حاضر خورشیدگرفتگی روی نداده اما ماه کنار مریخ است.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/19636" target="_blank">📅 23:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19635">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ژنرال محسن رضایی:
در حال حاضر، هیچ آتش‌بسی وجود ندارد. اما تمام عملیات‌های ما هدف مشخصی دارند.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19635" target="_blank">📅 23:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19634">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">برنامه داریم اسم جزیره قشم را بگذاریم آمریکا و آن را محاصره کنیم.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19634" target="_blank">📅 22:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19633">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏ژنرال  محسن رضایی:   اگر محاصره دریایی ادامه پیدا کند حتما برای ناوهای دشمن خطرات جدی به وجود خواهد آمد.  ‏درصورت عدم تغییر رفتار در آمریکا، نیروهای مسلح ایران هم دست روی دست نمی‌گذارند تا محاصره دریایی ایران ادامه یابد. ‎</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19633" target="_blank">📅 22:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19632">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏
ژنرال
محسن رضایی:
اگر محاصره دریایی ادامه پیدا کند حتما برای ناوهای دشمن خطرات جدی به وجود خواهد آمد.
‏درصورت عدم تغییر رفتار در آمریکا، نیروهای مسلح ایران هم دست روی دست نمی‌گذارند تا محاصره دریایی ایران ادامه یابد.
‎</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/19632" target="_blank">📅 22:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19631">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ژنرال محسن رضایی:
آمریکا در طراحی چهارم خود علیه ایران تلاش دارد از داخل شورش‌هایی انجام دهند
کشورهای دیگر را هم می‌خواهند وارد جنگ با ایران کنند!</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19631" target="_blank">📅 22:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19630">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">توضیحاتی درباره روند تکامل صنعت دفاعی اوکراین و پیآمدهای خطرناک درگیری با این کشور برای ایران  #ژئوپولیتیک   لینک مقاله مرتبط</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19630" target="_blank">📅 22:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19629">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اظهارات ترامپ درباره عوارض عبوری از تنگه هرمز:  من اجازه نخواهم داد که ایران این عوارض را دریافت کند.  اگر کسی قرار است این عوارض را دریافت کند، ما این کار را خواهیم کرد.  ما کنترل کامل را در اختیار داریم.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19629" target="_blank">📅 22:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19628">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دونالد ترامپ در مورد چمن:
چمن مثل انسان‌هاست. آن هم زندگی دارد.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19628" target="_blank">📅 21:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19627">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اظهارات ترامپ درباره عوارض عبوری از تنگه هرمز:
من اجازه نخواهم داد که ایران این عوارض را دریافت کند.
اگر کسی قرار است این عوارض را دریافت کند، ما این کار را خواهیم کرد.
ما کنترل کامل را در اختیار داریم.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19627" target="_blank">📅 21:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19626">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">منظور کله زرد از «این» چیست؟! وقتی مذاکره ای صورت نمیگیرد</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19626" target="_blank">📅 21:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19625">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ درباره ایران: این آخرین شانس آنها برای امضای یک سند خوب است.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19625" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19624">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ درباره ایران:
این آخرین شانس آنها برای امضای یک سند خوب است.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19624" target="_blank">📅 21:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19623">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سوئیس: ما در ارتباط با ایران و ایالات متحده در مورد مذاکرات احتمالی هستیم -
خبرگزاری تسنیم</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19623" target="_blank">📅 21:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19622">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCp2CEOSgz3-cMYY7cLtv4NL56d5Jj8KAsyhNe8NedNvmXq10Qv-OCMik9FDGMLZNVIrUUbS6JbSSEjPdUz2nNp9w9Gl3C-WlZskJVjZD_78ascQon5T00mRu1ofSCcHmDtOpp4RwlQHYGLLwSycyttH97h2gDxn24y3BGeGiDDscH19GGwwUz_6SbkUxfzX0Cj37ebkjAMmjMdHEM06wu8aGP7yJkLEekD6LiQbTRdZNOQVYCtAhudAFuZjF2kru9ILCM_3yLNn0XNdPLL5aLU1D8lh0n3GCtsb3PhA80NeX7zwO82iXaoBmDSzYnxSMxgQnGGOzbGWj9O6ace8cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:   رهبران ایران به طرز باورنکردنی‌ای ریاکار هستند! آن‌ها درخواست ملاقات می‌کنند، برخی می‌گویند "تمنا می‌کنند"، مذاکرات آغاز می‌شود، و جلسات بیشتری در آینده نزدیک برنامه‌ریزی شده است، و در عین حال، به صراحت و با افتخار اعلام می‌کنند که هیچ بحثی در جریان…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/19622" target="_blank">📅 20:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19621">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ:
رهبران ایران به طرز باورنکردنی‌ای ریاکار هستند! آن‌ها درخواست ملاقات می‌کنند، برخی می‌گویند "تمنا می‌کنند"، مذاکرات آغاز می‌شود، و جلسات بیشتری در آینده نزدیک برنامه‌ریزی شده است، و در عین حال، به صراحت و با افتخار اعلام می‌کنند که هیچ بحثی در جریان نیست، هیچ موضوعی مورد گفتگو قرار نمی‌گیرد، و آن‌ها فقط با "عمان" در ارتباط هستند.
سپس، آن‌ها به سخنان همیشگی خود ادامه می‌دهند و ادعا می‌کنند که تنگه هرمز به طور کامل توسط آن‌ها کنترل خواهد شد، در حالی که در حال حاضر، این تنگه به طور کامل تحت کنترل نیروی دریایی ایالات متحده و "محاصره" ما، یا همانطور که برخی می‌گویند، "دیوار فولادی ایالات متحده" است.
هیچ چیز به ایران نمی‌رسد، مگر اینکه ما بخواهیم، و هیچ چیز نخواهد رسید، مگر اینکه یک توافق حاصل شود، یا ایران به طور کامل تسلیم شود. چه ایران این را بپذیرد یا نه، در واقع، ما در حال بررسی راه حلی برای مشکلی هستیم که آن‌ها برای دهه‌ها ایجاد کرده‌اند.
این موضوع بسیار ساده است: ایران هرگز سلاح هسته‌ای نخواهد داشت!</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19621" target="_blank">📅 19:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19620">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پاکستان وجود هر گونه مذاکره ای میان ایران و آمریکا را رد کرد.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19620" target="_blank">📅 18:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19619">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تصویر نگران‌کننده بازار کار ایران.
بر اساس تازه‌ترین نتایج طرح آمارگیری نیروی کار مرکز آمار ایران، اقتصاد کشور در بهار امسال حدود
۴۵۰ هزار شغل
را از دست داده است. همچنین
۶۲۹ هزار فرصت شغلی در بخش صنعت
حذف شده و شمار قابل‌توجهی به جمعیت بیکاران افزوده شده‌اند؛ آماری که از تشدید بحران در بازار کار حکایت دارد.
﻿
همچنین مرکز افکارسنجی دانشجویان ایران (وابسته به جهاد دانشگاهی) اعلام کرده است که
معیشت بیش از ۳۲ میلیون ایرانی
به‌صورت مستقیم یا غیرمستقیم به پایداری اینترنت وابسته است؛ موضوعی که اهمیت دسترسی پایدار به اینترنت را در اقتصاد و اشتغال کشور نشان می‌دهد</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19619" target="_blank">📅 18:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19618">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نتانیاهو:
ما باید روابط خود را با متحدان بیشتری تقویت کنیم.
به همین دلیل است که من سرمایه‌گذاری زیادی در رابطه خود با هند انجام می‌دهم، با دوستم نارندرا، که یکی از بزرگترین دوستان ماست.
برخی می‌گویند اسرائیل منزوی است. اما حمایت‌هایی که اسرائیل – و من شخصاً – در هند دریافت می‌کنم، واقعاً شگفت‌انگیز است.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/19618" target="_blank">📅 18:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19617">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نتانیاهو:
اکثریت قاطع مردم ایران، اسرائیل را تحسین می‌کنند.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/19617" target="_blank">📅 18:27 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
