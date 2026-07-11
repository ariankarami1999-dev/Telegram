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
<img src="https://cdn4.telesco.pe/file/GwcQr_z8mE_mkQtDnw5jWt9L1psO7YQ_0l5xpA6-XLcpH9TSxG0ZGYuaLYaUx8D6s1BqYtLhfOkCf7tn2VaxLkTFDmhPkh3F9AnkdbP2_ilmFdI18Iu9Yr60lc_EwlgPo7NwodIO7pGCAUWG6HLkJTsi-9EuTwQIJT-M__8JOZRwUJwnwyAribB-ps5bzuABfT6_24e_A0d079El9JzntVcfZAofKZY_9pcQv72fwMpJACqEBjIimEcT7Xqhjr-7iwD3UrtgLRfS0Y_PX4ae_EjCpujc1uxk_FIZ5dl8Qm_SO3GxoorpByDO_CooiAAeBqhnOq6Miq-Xxx6HZnpibQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 367K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 19:54:28</div>
<hr>

<div class="tg-post" id="msg-17436">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">هشدار ایروانی به آمریکا درباره تفاهم‌نامه
نماینده ایران در سازمان ملل هشدار داد اگر آمریکا به نقض تعهدات خود ادامه دهد، جمهوری اسلامی ایران دیگر به تفاهم‌نامه با ایالات متحده پایبند نخواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/withyashar/17436" target="_blank">📅 19:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17435">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یک منبع آگاه با رد ادعای آکسیوس به منابع داخلی گفت:
تصمیم‌گیری برای تنگه هرمز فقط توسط ایران و عمان صورت می‌گیرد
حضور قطر برای تصمیم‌گیری نیست
حضور قطر در گفتگوها، در راستای نقش میانجی‌گری آن و نیز تبادل‌نظر ایران با بقیه کشورهای منطقه وفق بند ۵ یادداشت تفاهم است
@withyashar</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/withyashar/17435" target="_blank">📅 19:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17434">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فاکس‌نیوز: تهدید مرگ ایران علیه ترامپ واقعی است، نه نظری
@withyashar</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/withyashar/17434" target="_blank">📅 19:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17432">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ClMZ7k92oKzrmuI8NKZy1w46Fy3lKX1wzAV99w2Q6YgG1GDTiPHk9chSnkAaSrigRuR0jc8WnnMoFsUGCRNr8MH-0DJdjCumo7ZtABqqAf9z6X3RNfrE2EoOSA3VdRi2WHN4zBujamtPj0EN7RmxHqwrwE91wKFEAacAhQWbHxSgkG_6gBO6lYpPV8gwrH5dN13Il14O7tfybLY_DJMVCgu8LfP14HpNz_yXfmJllDdqjwMFQGNEoVWgtpHOa-037NUO1gqfVdec4Ijtw_Ac_21VxI3VumI1dGU43UZ7fSDJV7uRJN8nPrkCMI2Xw5hW5nuBlYIy8WongQRb5l-4TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V6vzS7NYbw_AuFmDaobzbHBgzl3GSu3FsY4AGTg_axoBa_gYIWDgB5gqrqFgYU9rLgkNbbodqabbE2Ht4AN_Ui3T89e7wv6ZwLS1bnJ71j_eWQ91-i0UXitD3IOiDidvyYmL68Hb82eUqcag49bJBEZEvSSsCPuU_ke8zUBtigMPh43WfIv2rJy_2ug6-wXyaZ6NXLHSLTR7r0Z5OHdn4Xt5h2iqeNvLQmfWVJS8NKyrXyTkD48uUY7ZM2q4q43pyS-PKaOfqwL1JZ1aNF2zb4bKrEgXxFdSFcCuOXMTPJ9zOUYrrd53tnAAwHFaIlolDKcnXJM1vzKwtVobg9iq5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همچنان عکس از کرج ارسال میشه…دود از سمت گلشهر یا حصارک مشاهده میشه… علت نامشخص
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/withyashar/17432" target="_blank">📅 19:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17431">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سید عباس عراقچی مدعی شد : ایران تاکنون به تعهدات خود عمل کرده است و تنها راه این است که هر دو طرف به تعهدات خود به صورت متقابل عمل کنند.
اعمال مجدد تحریم‌ها توسط آمریکا، نقض توافق‌نامه است
@withyashar</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/withyashar/17431" target="_blank">📅 18:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17430">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شبکه سی‌بی‌اس به نقل از یک مسئول آمریکایی: «جی‌دی‌ ونس» به عمان سفر نخواهد کرد و روبیو، ویتکاف و کوشنر نیز در مذاکرات آنجا شرکت نخواهند کرد.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/withyashar/17430" target="_blank">📅 18:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17429">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkrQXAi4eSNUVGiAN9vaS3ICEDr3WSUmZsfJBllosttIYaTfJOi1SWVC-fFa3v0lifaJVl530Nu7-ouPMTLTqzAuc4fl50E2CdMH102Y2hWYgJW4sGpKYFGNMyp8vyHzLoeaJZbMxDixYsNOyGUdlxgXFum5nQWSgdr91ITpNcmn6sNG3vIjFnjurQccH9ku56dLryc4mlzrat3h1g1udIqW0T5Pmg0jJVCrJ-3RRSnF12izQOAT8HCR8KGW6kAfJ8hIj6IEkb6CiTIHdCY02D4CAWDKZHBK_pajrqmKnnSQhfNfFnk-J8r0V6TBBZepoUv8yIoNNlZ0IXxja77elA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت رسمی رهپری تصویر جدید از مجتبی خامنه‌ای , منتشر کرد. @withyashar Ai ?!</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/17429" target="_blank">📅 18:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17427">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDkM5rEtYGYQGMcMwaYHt0nEwMNba6f-VRkvutJzQuJls4EpdworL2JXl_WjadkZjvZOiaEYYVOd9JkDGZvRifXAjPJbN2fPN6-gXHfuACBKcMI6qLtRZHBq4WxY_o0sKgbWpFCEenmq-yx2TXY5AQzgLoSABMkAnWKN7Khr4cF2t-TQ_8shIiuttq5DJABb6ca5bTHHkTb3ZgbylagATjbhS5tEc2UAzTZrrNgCjN5STNoiZtcFtAJNQPealIS98WJL3qYheKcAKEcr4iCNokJvTf8NyfQEMR_5wRQR55kW3ioW8EYH-S3mIjIPaBdgRprzihGdBEGpX5vqXj0T4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UBm3thh8XKyDEm2A7XcEbRzy0nr98YSOJz2huy2va4TZJjHPs9ZjjLnvOAnfvTEs-D3olAJFaugsXsiyS9f11_m1W8Gz-a2Bx2hA8EZu-VupRWw0AlTjWbbB8BTkfcA9xKnDvOgbE2F-I9EorWk4HhqtsWElPTo5d-79FlsttBszRNfIA4c168rF04K8xMideAsNK0ruf5xdpHLBPu2RvYaeRNh4Qrz7AWW96JxT5QxoZmIpaM5wvfbn7oWkXz3YUDyfSPbnEE2J9iT-04FTHa5MqwStjp5QuOCFJLQomWCUsrPWgtN-WGrzCoGEtOFEwajoMw-rbWybzSpXHlcOSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کرج این دو عکس ارسال شده الان ولی توضیح بیشتری هنوز ندادند
@withyashar
🚨</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/withyashar/17427" target="_blank">📅 18:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17426">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آکسیوس:  ایران و عمان در حال بررسی بیانیه‌ای هستند که آزادی کشتیرانی در کریدور مرکزی هرمز را تضمین کند
@withyashar</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/withyashar/17426" target="_blank">📅 18:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17425">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اکسیوس: رهبر جمهوری اسلامی در بحبوحه تهدیدهای ترامپ به مرگ، انتقام ترور پدرش را اعلام کرد.
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/17425" target="_blank">📅 17:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17424">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آمریکا: توافق با ایران بدون تحویل اورانیوم غنی‌شده ممکن نیست
شبکه i24NEWS گزارش داد واشنگتن اعلام کرده هیچ توافقی بدون تحویل اورانیوم غنی‌شده ایران ممکن نیست و گزینه نظامی همچنان روی میز است.
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/17424" target="_blank">📅 17:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17423">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fV5w0LeumZLfsHg76IMarhGCwEMKuFolc2hwHMNzee2QAhTKujK5mYcS21-hdWKVcNobyuIaIB0aBAuEV_C9lUyzHQJQORV2Q5VoUqyhWvqevalkSG6tPb8bGOEaf7FxVly9YNCr_8DHtslKrkzUxHmzS2fPjSN7S6VfDU_oW4Nkfs2L_K6hnuMmsXs1-tM5IqjShQPrbplBwefmFI77_FtPVRXLb6m2hMyXmjMroZWL7isS9my4AwsvlHZevlUcrw5TTqnZkHKTWNcxtFHjHLFjcD-VXCf9SD19wnBUJX0gVjNF7iIrWN3BB81Wmhfy_iJsReF3IOtA0txzJysQUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت رسمی رهپری تصویر جدید از مجتبی خامنه‌ای , منتشر کرد.
@withyashar
Ai ?!</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/17423" target="_blank">📅 17:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17422">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تعداد کشته‌های زلزله مرگبار ونزوئلا به 4118 نفر رسید!
@withyashar</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/17422" target="_blank">📅 17:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17421">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سردار ابن‌الرضا سرپرست وزارت دفاع و پشتیبانی نیروهای مسلح:
در اوج جنگ، نه تنها تولیدات دفاعی متوقف نشد بلکه ظرفیت تولید پهپاد سه برابر افزایش یافت.
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/17421" target="_blank">📅 17:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17420">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thS8qggwxt8VPrGOSxHY8qq5Zt4si7kelfesrxpeeb3T_16zFFmLitTiNBgwG-xlQd-Btr98PCPwdMLfgOakiXqXuGrdOKq6qm-KHL4kBusrplhjdVpcdh3RKBnUtQVDcWyvDNPr2XTvbhcWAHnCYcqasR5V9-d3HM5LofjcxPhOpokilA7t7J3PpTMlTSGPZ1jt8ZcTgIMWJkItbrmqvugiM2JlSsBxD8VcrpSvxs2pKNMuCchIXFCO2YSxGryeCmZ_9L8aUx11Q1rnHdhukj2cAe-72SHRHlBDGTaFmZ9C_drvRwws31T4sqwlpNbxDuA0f76A1FZtAfNVkzT5JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگراه بسیج شمال به جنوب
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/17420" target="_blank">📅 16:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17419">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1U8kguqmmZaPlrEVbCD_wyGpuo4lbUXtvIHFhcTSYafyZxPRApeK8LaRWmHgz5CpndCBIuoS9-hLLuA39_2Mc6nfHB-ONR3vHrW5Tftua3bM8ymHqIOKkmtoO2Li1hqTJkVgdylYWyv2naIBGLVCaRL-ZvjCLTmud21CWYtBYKIZfAAegHf9l4d_N7TeNQe5On9-4gWnzeHdE6hE8fA_jNy_bO6pMAqnULlNkFkEHP4WZ7h2Kr4-Y_f7YXzjumzqLdEcUM-Lhe7f73Pjb61tvt1elGuVeW8q0tIOJF_nQsinrEFb0HD2YBM-vhN6dNYYKWoHR1s-aRDtO4JTDo7wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهدی به چشم دیده یک پهپاد منطقه افسریه یک سوله را زده !
کاربران هم تصاویر زیادی ارسال کرده اند
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/17419" target="_blank">📅 16:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17418">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/17418" target="_blank">📅 16:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17417">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دو دیپلمات نروژی که ارتباط نزدیکی با ویتکاف دارند :
ترامپ بعد از دیدن مراسم تشییع خامنه ای عصبانی شده و گفته احساس میکند توسط عده ای دروغگو احاطه شده است
@withyashar</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/17417" target="_blank">📅 16:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17416">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c204b38409.mp4?token=GjTX1Rnwv0REFtFivcZWKkPuQkv9zIj2NcnIkwmG_KFY38FCxt4IF17kSvmII2yFU57s1ASTWuYcKWtGSC41OZcGEkm3kIZ5maerJy7Zi7iBOTP6QdbYc-kKR67uEaAAqNSTQDGKzBGdoykzdcMLzJlSct-Mr5qKYDhvRY9zRKOs-8H2wGcR1adD9AxjXLZGzRPWCKGgOiu6FUhHzD8FayUplNK8nuuhDB-CrhKC7C42u0vIkvlJ_wlaXcscCFolURwokvSk6Ig8RlQPxozTG9EI7r06PhckPamKf2HmluvR5Hes-o6oFsJ1G5saFhceUx8lsAUllpy5srwYDUv0Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c204b38409.mp4?token=GjTX1Rnwv0REFtFivcZWKkPuQkv9zIj2NcnIkwmG_KFY38FCxt4IF17kSvmII2yFU57s1ASTWuYcKWtGSC41OZcGEkm3kIZ5maerJy7Zi7iBOTP6QdbYc-kKR67uEaAAqNSTQDGKzBGdoykzdcMLzJlSct-Mr5qKYDhvRY9zRKOs-8H2wGcR1adD9AxjXLZGzRPWCKGgOiu6FUhHzD8FayUplNK8nuuhDB-CrhKC7C42u0vIkvlJ_wlaXcscCFolURwokvSk6Ig8RlQPxozTG9EI7r06PhckPamKf2HmluvR5Hes-o6oFsJ1G5saFhceUx8lsAUllpy5srwYDUv0Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک بار دیگر، هواپیماهای جنگنده اسرائیل منطقه المانصوری در جنوب لبنان را بمباران کردند.
@withyashar</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/17416" target="_blank">📅 16:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17415">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">معاریو: نتانیاهو فعلاً افزایش فشار بر ایران از طریق تشدید تحریم‌ها را به ورود مستقیم به جنگ ترجیح می‌دهد
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/17415" target="_blank">📅 16:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17414">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نیوزمکس: ترامپ در حال بررسی ازسرگیری محاصره دریایی است , دولت دو ناو هواپیمابر و بیش از ۲٠ کشتی جنگی را به سمت منطقه هدایت کرد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/17414" target="_blank">📅 16:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17413">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">روس اتم: با حملات جدید به ایران، اعزام نیروهای خود را به بوشهر به تعویق انداختیم
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/17413" target="_blank">📅 16:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17412">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">قطعی برق در برخی نقاط تهران، از جمله محدوده ولیعصر، مطهری و قائم‌مقام فراهانی تا بیش از چهار ساعت به طول انجامیده است.
خاموشی‌هایی که از حوالی ساعت ۱۱:۳۰، همزمان با اوج گرمای روز، آغاز شده و هنوز هم ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/17412" target="_blank">📅 16:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17411">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اتاق جنگ با یاشار : این جریان خیلی مشکوکه صدا و سیما داره اینو یهو بولد میکنه مخصوصا این چند روز!  سید علی مصطفوی ، زادهٔ ۲۱ فروردین ۱۳۶۵ (هم سنه منم هست) مشهور به حجت الاسلام والمسلمین سید علی خمینی. وی فرزند سید احمد خمینی و نوه سید روح‌الله خمینی است  از…</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/17411" target="_blank">📅 16:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17409">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpV-u8UfwCT-fVD7UK_qft27lhEFD2XneDESoGp-Z09-QzgHxbMIQnMbEN8hSQXfI2rIgkbLBWXm16E5bv4_m5aogaCCOlDDAbck7r6oi_EooesR24PRSMRf5g_pzqdHE_6sK_tWbhS492ecwSDfLqxMxT1RKbrXNkqdxMkxL6nlbt0TBFW8CuZbKh7gP8EFNxn6mb7JpCzEs79ogE-g0DbhJKwtNeYbxeJllJ7G8eJm7uOnFGUN-vPuZHOSBx_vLZ-_ESc-ZjsAkBMVTy1V6F9DdE01OGyRb7uVYeFh6mz4JAMHkXQdt4D9rcSSjIzE6hMVSNZbqcxJHZRcUtFnfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : این جریان خیلی مشکوکه صدا و سیما داره اینو یهو بولد میکنه مخصوصا این چند روز!
سید علی مصطفوی ، زادهٔ ۲۱ فروردین ۱۳۶۵ (هم سنه منم هست) مشهور به
حجت الاسلام والمسلمین سید علی خمینی
. وی فرزند سید احمد خمینی و نوه سید روح‌الله خمینی است
از این لحاظ او برای من دوباره خیلی مشکوک است که بعد از حمله آمریکا و اسرائیل به بیت ، شروع جنگ و کشتن سران نظام و علی خامنه ای، وی اولین نفر بود که به صدا و سیما آمد و طرح تجمعات شبانه را بنیانگذاری و از همه مردم خواست تا هر شب به میدان‌ها، شهرها و خیابان‌ها بیایند.
فرضیه من این است که اگه مشتبی خامنه ای مرده باشد(که فرض من این است) یا ناتوان باشد این شخص رهبر بعدی یا رهبر کنونی ‌مخفی باشد توجه کنید این یک فرضیه است فقط جهت توجه و زیر نظر داشتن بیشتر و آگاهی شما بیاد شد!
@withyashar</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/17409" target="_blank">📅 16:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17408">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دقایقی پیش دو حمله هوایی اسرائیل به منطقه المنصوری در جنوب لبنان انجام شد
@withyashar</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/17408" target="_blank">📅 15:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17407">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b21d2edb8d.mp4?token=BhKW2xYjIiKWnydm_z36x3TDeC1W-k8fJEXluw_jKivUQcl2Mn2Ef-9C9Dq09FMpcdWSdZv1A2qtlCGexReJktpF4wsqE3GgFAa92nbpYKPeuucb_KcaLQATSGPiDzhPrHBpcOoy89psfdzL9V9AN1YJ6YNh-u6IsJR7XBbf0roA-UkNZKfdeJNGo1Il3P2LH-PZkc8zA8SNnsofQ1cSSDvuymUhCc7G0A43GqxQzW7jeOMVdNc8lZe28-WCGgIVzJmxYQnjICzmcLAa7j9Z66XRtrG2_8MfEwH9uxN-nGktTUYnGB--N23-gqaajnb0W8wBXgBU1oexRxLvVP0eug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b21d2edb8d.mp4?token=BhKW2xYjIiKWnydm_z36x3TDeC1W-k8fJEXluw_jKivUQcl2Mn2Ef-9C9Dq09FMpcdWSdZv1A2qtlCGexReJktpF4wsqE3GgFAa92nbpYKPeuucb_KcaLQATSGPiDzhPrHBpcOoy89psfdzL9V9AN1YJ6YNh-u6IsJR7XBbf0roA-UkNZKfdeJNGo1Il3P2LH-PZkc8zA8SNnsofQ1cSSDvuymUhCc7G0A43GqxQzW7jeOMVdNc8lZe28-WCGgIVzJmxYQnjICzmcLAa7j9Z66XRtrG2_8MfEwH9uxN-nGktTUYnGB--N23-gqaajnb0W8wBXgBU1oexRxLvVP0eug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ اقدام اصلی علیه ایران را بعد از انتخابات کنگره انجام می‌دهد
مجری فاکس نیوز:
رئیس‌جمهور می‌گوید ایران دوباره به میز مذاکره بازگشته است. آیا شما واقعاً معتقدید که ایران با نیتی صادقانه و با حسن نیت به میز مذاکره برگشته است؟
هارلی هیپ‌من، تحلیلگر سیاست خارجی:
قطعاً نه. البته دوست دارم این‌طور باشد. هیچ‌کس خواهان جنگ نیست، اما ایران کنترل تنگه هرمز را رها نخواهد کرد. آنها به اهرم راهبردی‌ای دست یافته‌اند که به‌گمان خودشان، شاید حتی از یک بمب هسته‌ای نیز برایشان ارزشمندتر باشد. همچنین قرار نیست از تسلیحات هسته‌ای خود دست بکشند. بنابراین، آنها به دنبال حل‌وفصل مسالمت‌آمیز این مناقشه نیستند.
احتمالاً این وضعیت تا ماه‌های اکتبر و نوامبر به شکل اقدام و واکنش متقابل ادامه خواهد یافت و پس از آن، ترامپ میداند که در آن مقطع چه اقدامی باید انجام دهد.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17407" target="_blank">📅 14:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17406">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">به گزارش شبکه ان‌دی‌تی‌وی، شرکت رافائل، شرکت دولتی اسرائیلی فعال در زمینه سامانه‌های دفاعی پیشرفته، در حال مذاکره با شرکت‌های دفاعی هندی برای ایجاد یک خط تولید در هند برای موشک‌های رهگیر تامیر است,این موشک‌ها در سیستم دفاع هوایی "گنبد آهنین" مورد استفاده قرار می‌گیرند.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17406" target="_blank">📅 14:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17405">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">الان محدوده زندان اوین و بالای سعادت اباد @withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17405" target="_blank">📅 14:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17404">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مجتبی خامنه‌ای :
عهد می‌بندیم انتقام خون شهدا رو از قاتلانشون بگیریم
این جنایتکاران آرزوی مرگ آرام و در بستر را به گور خواهند برد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17404" target="_blank">📅 14:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17403">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فارس: هیچ مذاکره‌ای تا عقب‌نشینی آمریکا از مواضعش انجام نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17403" target="_blank">📅 13:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17402">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">به دنبال خبر نیویورک تایمز درباره «تغییر هواپیمای ترامپ در بازگشت از ترکیه از ترس ایران»، دولت آمریکا برای خبرنگاران این روزنامه احضاریه صادر کرد
نیویورک تایمز اقدام دولت ترامپ علیه خبرنگارانش را «عملی گستاخانه» خواند و محکوم کرد
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17402" target="_blank">📅 13:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17401">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">https://x.com/yasharrapfa</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17401" target="_blank">📅 13:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17399">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aT_u15ReKQKyHm4r-QMVy54ovnuXFsYO-uPqTu-41UNxT5-uTejqxr71yB1M2Y0GpAc9CjrbBHTJRGcZAzL9WW1eJGekABWVc3rA__oQ5Da58g8kAgN1RU9G7d3MPuJEaXkA26uRhLRu1CB752WvvTGuToF823CA1z0jkPW945fjG4lKSZf9sGPYmIc5oH9eq7eZtJuctpW0a9AV4uT4pz0Dppt8HlJMbqOUmy4wCeYV2wZFucaNK78_BH6twqIldO9WtVxdalDo8pbVOTTmiLE6IRe_C0Rl7uVaUJY2GR9pXs1psT2m3X5ZkC6MhOD4LET2I212ahCzaMXCFVdhuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رژیم کشته شدن دو بسیجی‌در ایست بازرسی مشهد را تایید کرد
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17399" target="_blank">📅 13:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17398">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ای بی سی نیوز به نقل از مقامات آمریکایی:  اگر ایران امروز شنبه اعلام نکند که تنگه هرمز مانند پیش از جنگ باز شده است، آن روز برایشان روز شادی نخواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17398" target="_blank">📅 13:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17397">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ادعای ان‌بی‌سی:
یکی از متحدان جمهوری‌خواه ترامپ به او گفته دوباره به ایران حمله کن، این بار ظرف چند روز به اهداف نظامی خود می‌رسی
@withyashar
😁</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17397" target="_blank">📅 13:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17396">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">طبق برخی شنیده ها غیر رسمی، سردار عظمایی فرمانده نیروی دریایی سپاه به صورت نمایشی برای جلب رضایت آمریکا به دلیل هدف قرار دادن ۵ کشتی متخلف توسط رده های بالاتر توبیخ شده و تذکر گرفته
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17396" target="_blank">📅 13:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17395">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">جشن های ۲۵۰۰ ساله گرونترین میهمانی تاریخ جهان
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17395" target="_blank">📅 12:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17394">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ارسالی : سلام یاشار جان وقتت بخیر من از اصفهان پیام میدم پرسنل بیمارستان الزهرا هستم  امروز همینجور داره هلکوپتر از بالا سر بیمارستان رد میشه قبل جنگ چهل روزه هم همینجوری  هلکوپتر مهمات رد میشد  من حس میکنم یه خبرایی قراره بشه این چند روز
😍
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17394" target="_blank">📅 12:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17393">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گاردین: اروپا در حال بررسی پیشنهاد‌هایی است که ممکن است امکان وضع عوارض بر تردد در تنگه هرمز را در صورتی که اجباری نباشد و مورد حمایت آژانس سازمان ملل متحد قرار گیرد، فراهم آورد!
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17393" target="_blank">📅 12:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17392">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پولیتیکو:  آمریکا انتظار داره جمهوری اسلامی در بیانیه‌ای که قراره امروز منتشر بشه، «به‌طور صریح یا ضمنی» قبول کنه که در حملات اخیر به کشتی‌رانی در تنگه هرمز مرتکب اشتباه شده.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17392" target="_blank">📅 12:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17391">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d85328fee3.mp4?token=jReD_u8lcOtdEudyEwV4219W4WVX-Z6TcXs9M5HoY_uIX5O583v0rQ0boKwcq6ev9WOgFtjchBWOMtKxhvAN9hZQfZVyz4HO4MYRo7zx9ONcTxYL6vIJJxa1BTqvssG2siznJtS3P9rWJKfm5DUaqVj6w9AZuTiaqHILcabLjGdabwwNegZ_0lWdV16Xg-G0b0k6aWhHzYsTtW9wvI0QxYNBqjLzblRbIzVSwXxR7QRirO3ZWjEdlAfZCkSbhs_3OXfRQwxjRL2ykjlxahEkljsEq4CQhAqz9GSuYvFkrN2df05VNoBi_rcqVgnLOKOWc0PS9fRPBBSrcQgI4fF2fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d85328fee3.mp4?token=jReD_u8lcOtdEudyEwV4219W4WVX-Z6TcXs9M5HoY_uIX5O583v0rQ0boKwcq6ev9WOgFtjchBWOMtKxhvAN9hZQfZVyz4HO4MYRo7zx9ONcTxYL6vIJJxa1BTqvssG2siznJtS3P9rWJKfm5DUaqVj6w9AZuTiaqHILcabLjGdabwwNegZ_0lWdV16Xg-G0b0k6aWhHzYsTtW9wvI0QxYNBqjLzblRbIzVSwXxR7QRirO3ZWjEdlAfZCkSbhs_3OXfRQwxjRL2ykjlxahEkljsEq4CQhAqz9GSuYvFkrN2df05VNoBi_rcqVgnLOKOWc0PS9fRPBBSrcQgI4fF2fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان محدوده زندان اوین و بالای سعادت اباد
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17391" target="_blank">📅 12:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17390">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofQo7TCRZt_4Exs6RalCu8gpcS6VHx2mjqwmGiS82sq4PGTCvVhUvrVYZMKSxX-Kz5_YNaNOjL3XAsofq8Ax3VgaaNY6SMqmAnDDob-5LBFCCkAYSKR6ZXaasvrU8w56unJLY14EtXwPQpKcIolYW76bceQxQnlHBftLL2cGoRWww9hWrj_eGsGxNDn0tcn7OzH69MoUF3Dbb1pscWqPxwdAtyg8rYp-WaoA961Kzk_7XsIi9uRJvIpNYzri0ebL5AD7rxsqPQ1UTPPIN8BWTcR75wvHpX1Vz_e2a-_Fl_jhm2c5lUnVDY74mlQJE68mlGEdTEnYWVt_Y9m65fBIbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏وقتی سناریو حضور مجتبی‌ خامنه‌ای تو مصلی ⁧ تهران⁩ با رسوایی شکست خورد؛
‏رفتن سراغ سناریو دوم تو ⁧ مشهد⁩ که آره مرد ماسک و کلاه‌دار تو صف نماز مجتبی خامنه‌ای بوده!
تایید‌ای بر این‌که این شخص دوم ماسکی مرموز در مراسم رهبر تو مشهد هم مجتبی خامنه‌ای نیست؛
‏تو یه لحظه که سمت چپش رو نگاه می‌کنه:
‏۱- ریش سیاه
‏۲-مدل ریش ستاری
‏۳-صورت استخونی
‏۴- گونه بیرون زده
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17390" target="_blank">📅 12:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17389">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وزارت بهداشت ایران : در حملات آمریکا در روزهای ۸ و ۹ جولای، ۱۷ شهروند ایرانی (از جمله یک زن) کشته و ۱۵۱ نفر دیگر زخمی شدند.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17389" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17388">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e930784fd.mp4?token=CYtlUs1ME2M8S82edIzdoHiw4N5iPyHwIdz9biAahQGtbgk3cqHKXgY2K0OHxR3SJkdiszYspMpcFC6B7ZdRD1wKe-PxyZSzgr6c38r3i89vck0Gq9UWSxAinCEDxJEXE56XXxji6z1NOzF2-4UWfx7eieMp6oKIvejua1oemAawvzxA8xRF8S7C4a6cwE9wss-F48vWJc4uRMUJfTcTLt77l4I46gvKRPI25TN_plmY_tvziR3cSLyEp3zWrrO4avgkKaib0RGesxxvgS9-dn6k9kHplK3WL54sWPrG1nRlQWHZ-zVHGRAcprn8zbjEt_9NntfZXCq_F99r-XSQoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e930784fd.mp4?token=CYtlUs1ME2M8S82edIzdoHiw4N5iPyHwIdz9biAahQGtbgk3cqHKXgY2K0OHxR3SJkdiszYspMpcFC6B7ZdRD1wKe-PxyZSzgr6c38r3i89vck0Gq9UWSxAinCEDxJEXE56XXxji6z1NOzF2-4UWfx7eieMp6oKIvejua1oemAawvzxA8xRF8S7C4a6cwE9wss-F48vWJc4uRMUJfTcTLt77l4I46gvKRPI25TN_plmY_tvziR3cSLyEp3zWrrO4avgkKaib0RGesxxvgS9-dn6k9kHplK3WL54sWPrG1nRlQWHZ-zVHGRAcprn8zbjEt_9NntfZXCq_F99r-XSQoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از سری جدید انتشار پنتاگون: پدیده های ناشناس بخش ۴
فیلم گرفته شده توسط یک حسگر مادون قرمز در یک سکوی نظامی ایالات متحده در سال ۲۰۲۰
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17388" target="_blank">📅 11:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17387">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سپاه : عملیات امحای مهمات در شرق تهران تا ساعت ۱۵ ادامه خواهد داشت
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17387" target="_blank">📅 11:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17386">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">منابع به العربیه: واشنگتن از ایران خواسته است تا به صورت کتبی و علنی تعهد دهد که دیگر به نفتکش‌ها حمله نکند.
واشنگتن از طریق واسطه‌ها به ایران هشدار داد که در برابر هرگونه تجاوز به آزادی کشتیرانی سکوت نخواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/17386" target="_blank">📅 11:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17385">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuiMU2zz-Zccp12eUl5n_try5LbC1hZabvBMF_8u6XIkpVzBO4t0XEAjdK5IcORyiF_KfL1idfGuCeS_7w5jn862XCSFE0oMbKUMFzZrxDpVk2h7HfRPFHjRzcxbHR--g3SPlQnw9Z_AjHCX8ieN4DYW_Q49SNLTIZBNIfPPwCHP6NpCG6v7J7adfISmCDoPito-isj79dsNURj8MX1h3MjJFngOORKtqEwhic0DKa_H9D0nuiu9hs_l9tr2hylAT8AE5q2RcWAIuKSKK2Ef3JdscFhLbq-94FiM2QGjz1QWKTLJ3i2D-C5sM0WvD2DoWMBwCo6d2CyEItCkjdTazg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود چیتگر الان
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17385" target="_blank">📅 11:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17384">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">طبق آخرین آپدیت آموزش پرورش و با اعلام صادقی، هیچگونه تغییری در امتحانات شکل نمیگیره و از فردا 21 تیر مطابق برنامه شروع میشه.
@withyashar
(این خبر آخرین خبره و ماله دیروزه و تازه رسانه های‌داخلی قرار‌دادن گویا امروز جلسه ای است ولی فعلا تا اعلام خبر جدید همین خبر آخرین تصمیم ‌است در صورت اعلام خبر جدید به اطلاع شما میرسانم )</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17384" target="_blank">📅 11:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17383">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGMxElQ0z-dhkRlTGXNIefR4HglsrDS8S2D1Ax8SxdyEFl5karhG-tGzXG3DrhLSf0xbJZyROeCtur3DYWdandW7reBXU-4Oc0_ZmYLrjrra2s26FNQaczVaKUvxq31IA40SW4JRzDrsut9DpMFOXXkJxpu8rwxp_NmXQhFwVlmKiVT93g5gnhUZL85j9XxicGERQSSbYLqVlID4XNnu_eRY1RuzHNtaOXtW5AVj4LmVF-XBCGyeNPHMa3ynpXEOs7rTkEOwnFydblJAqeAsJgdEVpY4Q51i-JoDmYroBlluMPWE5k2eIUHTD4bHJXeoAvYLHVuPGrgm47TdNUQ5xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی : به نظر لانچر میاد
دماوند
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17383" target="_blank">📅 10:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17382">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ارسالی : درود یاشار جان وقتت بخیر من عموم لودر داره دیروز بهش گفتن هر چقد خواستی پول میدیم بهت که یه اکیپ لودر ببرن سراب کارخونه پهباد سازی که تو جنگ قبلی زدن ترکوندن رو آوار برداری کنن تا بتونن به تونل هایی که زیر آوار مونده برسن که انباره پهباد که اون قبول کرده از دیروز ساعت ۱۰ ۱۱ شب شروع کردن با ۱۴ تا لودر آوار برداری کنن
@withyashar
😕</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17382" target="_blank">📅 10:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17381">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خبرگزاری معتبر تسنیم
😂
: علت صدای انفجار در منطقه پاکدشت ورامین انهدام مهمات عمل‌نکرده کنترل‌شده است
روابط عمومی سپاه سیدالشهدا استان تهران با صدور اطلاعیه‌ای اعلام کرد: صدای انفجارهای شنیده‌شده در امروز شنبه ۲۰ تیرماه، ناشی از عملیات فنی و کنترل‌شده تیم‌های تخصصی چک و خنثی جهت انهدام مهمات عمل‌نکرده به‌جامانده از تجاوز در منطقه پاکدشت ورامین است؛ این عملیات ایمن‌سازی که تا حدود ساعت ۱۵ ادامه خواهد داشت، احتمال ایجاد چند صدای انفجار دیگر را نیز به همراه دارد و از شهروندان عزیز تقاضا می‌شود ضمن حفظ آرامش خود، به شایعات و اخبار غیررسمی توجه نکنند.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17381" target="_blank">📅 10:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17380">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اتاق جنگ با یاشار : به نظر میاد خودشون دارن ورودی های سایت های موشکی مسدود‌ رو با عجله باز میکنند ! @withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17380" target="_blank">📅 10:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17379">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buRTqvJcWVzP2nQH5YuzWqqgiFbUhLGrNKB6PT2bbPkLOzLgV3qVhFsGWH_6H2Nb8HFNAO_wDN26rrZ3IClGolGdh3gL7GXJ6Gv1vVN59_qFB1nMs5y4-QjoMqYzBXtVkIi1aWzYRwCAx-reQPbIwp-SCAgcC1k84tKbgh0MDr7Xi0N6ZQbJnYn2voKoFEIqvgn3sJZhRcWLh7RqSjGlqtY49sC4qPnppIkkYwkxdVMBEmbJLSM-ein5fmR51AZ9cqSJHoWuCzWQ2p4icjy6Ldhzs69P4pq5lp0AMCHBXgNLWUPiDhSZ6HMH9W6YROmt_5mEpSLiLtitzhMElHB1eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه پاکدشت
🤒
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17379" target="_blank">📅 10:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17378">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شبکه خبری ABC به نقل از یک مسئول آمریکایی : فشار نظامی، دیپلماتیک و اقتصادی مستمر بر ايران وارد است. ما گزینه‌های زیادی در اختیار داریم اگر ایران از تحویل مواد هسته‌ای خود امتناع کند.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17378" target="_blank">📅 10:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17377">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اتاق جنگ با یاشار : به نظر میاد خودشون دارن ورودی های سایت های موشکی مسدود‌ رو با عجله باز میکنند !
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17377" target="_blank">📅 10:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17376">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">صدای انفجار تو قسمت نجف آباد اصفهان شنیده شده
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17376" target="_blank">📅 10:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17374">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">لطفا دایرک بی مورد ندید !!! هنگه ! خبررسانی‌رو کند میکنه ! دایرکت جای نظر و کامنت شما نیست !!!!!</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17374" target="_blank">📅 10:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17373">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer"><a href="https://t.me/withyashar/17373" target="_blank">📅 10:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17372">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فرماندار پاکدشت : صدای انفجار مربوط به عملیات کنترل شده مواد منفجره‌ست
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17372" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17371">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Glbn8k8iJZHigAdwOvhghf4hO_UZhU_oPpe4KzFu4WRBHqGQGh69WJl5El3efzrVyo4edEXEx_5GBcOR2hpCzrjcRPcMDqtMRoTc_3mxzB4NCjVzV2lExcP6YD6ghSj722f_3IU1xInJRfVDAKHzDx5kRfp8K902jCkhaPbP2UPgFoEv0Y9rTK3N5OlNoPe3W1TrdKbMyjgY3Oar6cUGU-PFhJZ79ETvfLEHCPpSi_2p2_CT9qra_mAer9N8YqR8ZGnEcFIsfMefX0h_tGQnJb_NIq_GiHbJz4I2ym0lIp3dmnrxMub33b5HGb2BweH3ESvRu8m5UUeQoLP0mSp3vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17371" target="_blank">📅 09:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17370">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfNUs-qWWggllhV44Qkhm0qmVm5370cmyZ3xmorPuTolBftSjOF4gZEzyMTQbZEYX_-_-W-0RyCd917UuE_-5bq66CdG4_nAOEGbnKbj39u7RdDBEfG2MusSyDoz8YkWyY7pJnwMCWzus95_Xv0QYHEf7Zz3DaDmhTNc8iPgr3q_pxheR1j-11f3OzzGlv8lNz39xVmj3XHcbFsNi2oDquieT6lJvuM1kDrapBap-XrKoRL6nydzNFSce-KVoN5JQYcj2U4fe-jj3NbBcxQ8TjCxSbwQvTt85uTXSiOsJ0Ics1aH1oVsXRdRDoIS5PG6_5EHkSBXW509SDWmhXOisg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار شدید پارچین
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17370" target="_blank">📅 09:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17369">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWus3TPxlz82F9x2Eofin9TqPMa43ok_UeFFJIoLyQV5Dpb7Be4Bs1HfMQ8n47-tcm6iUaod2nUT6mjfYJ3wx0swoccg8j1FK2WzT7jRw3V6O-CZyEX1EfFGCpk1Ln4dWAHYfESl3oN_MQBo8Y_vIBvJ90uIY1y9M6zpqqUcKNx5HMtae18lgTyl5vDCdaWyR32RbxDu9xoVY715CqEeSiyI1LQAwAwFmX9czm3TM2Ynqkam8VvQaN3P8wZAhoc5ns0RY1PjCabOMbHwbCmmiia8cN3ZN3nfu2HxYaPdyo1Otx40w6WuuueIiFhnkDx6dUJhyUDkrQlNfXwaLvcmAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار پارچین
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17369" target="_blank">📅 09:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17367">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhwRixEJDYord7wGuQQJAXRjoCR96Fh3MdR3y9BBVDwjenX3ixsgT-wuIRzkt90FNfm0k5kU_6ezU0WIXE1jwjzoT3q5A3AddaHGSDcV4iVoiPlZtipo2Tl2S1m2wi48HukVZuSgyuM6gxW25S8v6GRGQpONqXQPWHRsmxvH9ori1o9tC1RGgxTdAUa3V972P9mCe9x2F117_OttFJs-XPR_4TarBk9eHtWYwyy-3fK2kYryatAkOOSH7PoGkdZFEG8hujmxuG17uVtHPxL-lHc8dqdjdudltD27OoVXBOg7XJA6bqMQdprTJ9l7pFso4SYAJ6cZ1k6rP71YpdyK_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار پارچین
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17367" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17366">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سایت موشکی پارچین / پاکدشت رو زدن
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17366" target="_blank">📅 09:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17365">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M67aKhuN9qozYe8HoCabjGHl3BwecLBRGYfsxzkQYEultCc27kj_HH_cBd3TIxdrOXkq8JNx5b8_GE5JfdbAx2V9il8HHjfUDFstK9MKVpOqcLmj9fjheqmTAchb_M5utIOXXJKyIFjB7E3ExW_132DceM4tENBKvu73BNkOWxQ1F3cKEPN9tPhioZjhLnfeSymtmFLwjQHDgczqFjR_45tdyU5bKVxGqWV4DewlrLyHAk__4ssVluL8iWRLO7wKM1pO-HDEe21m3TX4ZJ7LpEYl1ZNbvzz8BSkUIIuic1U3UBb7cEa9QuUw0L2UF085eBDZvb3_AdUz89gbWjFQEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی وارد مسقط عمان
شد
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17365" target="_blank">📅 09:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17364">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">صداسیما: ایران به دلیل پایبند نبودن آمریکا به تفاهم اسلام‌آباد، آماده ادامه مذاکرات نیست
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17364" target="_blank">📅 09:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17363">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سی‌ان‌ان: یک مقام آمریکایی اعلام کرد تا زمانی که ایران اجازه عبور آزادانه نفتکش‌ها از تنگه هرمز رو نده، واشینگتن وارد مذاکرات مربوط به تسلیحات هسته‌ای نمیشه
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17363" target="_blank">📅 09:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17362">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T56CYTGPWeYCrAt36EbydwnNl2zrGp7RoEWM3uqRddexrgvu0HAUewqQozQhkaD7Rw573YP-dSeqGKjRJglb_oYcuVHsu2l2C275JVIrCHw4YP-Uv5R6N0m8cFwX9Yg2-oXzQoqKjwJUzFEEmE0dEGvp09bfo6IVz5vBXX9fkWCDv43fPPHT7hZvMuKgEphHp413JKKQ7s7g1ouGw8S2YDryVSAnPUIVwNSnKs3vpBfvHh-8-FAzaOCHs4v4gxNDcWlZK4zvDVwYB1AI19KYiRGbIxHWnCEZjrEESMjKA4o-W4zwuSUHevu8SG0wSQnRbXZGi4g35KS9c5D2DU-JWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ۱۰۰۰ موشک در حالت هدف‌گیری شده به سمت ایران قرار دارند و در صورتی که دولت ایران به تهدید خود مبنی بر ترور رئیس‌جمهور مستقر آمریکا که در این مورد، خودِ من هستم عمل کند، شلیک خواهند شد
دستورات از قبل صادر شده است و ارتش آمریکا آماده، مایل و قادر است، برای یک دوره یک‌ساله که قابل تمدید است، همه مناطق ایران را به طور کامل نابود و منهدم کند
@withyashar</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17362" target="_blank">📅 09:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17361">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">هم اکنون حمله اسرائیل به جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/17361" target="_blank">📅 02:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17360">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سی بی اس : ایران در گفت‌وگوهای محرمانه به مشاوران ترامپ: در هدف قرار دادن کشتی‌ها در تنگه هرمز اشتباه کردیم
به گفته مقام‌های ارشد آمریکایی، مقام‌های ایرانی در گفت‌وگوهای محرمانه به مشاوران دونالد ترامپ اعلام کرده‌اند که هدف قرار دادن کشتی‌های تجاری در تنگه هرمز «اشتباه» بوده و این حملات از سوی یک جریان «خودسر» از تندروها انجام شده که قصد داشته‌اند روند مذاکرات را به شکست بکشانند. همچنین ایران تأکید کرده که مایل است گفت‌وگوها ادامه پیدا کند
@withyashar</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/17360" target="_blank">📅 01:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17358">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">باراک راوید: دولت ترامپ به ایران 24 ساعت فرصت داده تا به‌صورت علنی اعلام کنه که تنگه هرمز بازه و متعهد بشه حملات به کشتی‌های تجاری رو متوقف می‌کنه؛ در غیر این صورت، با پیامدهای بسیار سنگینی روبه‌رو خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/17358" target="_blank">📅 00:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17357">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrjRxOb-_SXhM-7wNSFKn9iDfxmiTGnGhNUAhEGbc3LlATf5_I0s3DK8whjieWk-6cth7XG9Go1gVyNvNmSjZi47Ktgh2Sif0VlXmc_G9IfetEibO7mKNEy8pwz4edJAr2jeSKBlbm-D0hVsoWYsnMyXoi4o2yBVudgRTYHPO2LI8cCdE6lxh9BNXJqam7hdaMaFfohbdMtoNi9E8YXTUyBnxZwERbjMuibP4i6P9PXT7ayMpNKZHEJ_CcjnF6HBDYKdUuzhZ8qqcDi56jbeTqxfVW6wPak0Er4Ccf9pupId0mbV2gA9E-9waUEkU0UbtRjzlXAPJMoZU6GR9uKltQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : من تو جام جهانی طرفدار آرژانتین هستم.
@withyashar</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/17357" target="_blank">📅 00:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17356">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فوری | بر اساس گزارش نشریه "اکسیوس" از مقامات آمریکایی: دولت ترامپ از ایران خواسته است که شنبه‌شب بیانیه‌ای عمومی منتشر کند و در آن اعلام کند که تنگه هرمز باز است.
@withyashar</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/17356" target="_blank">📅 00:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17355">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d3fe5b208.mp4?token=cOXHZRCDLKyMwdRTp3Xp1XSLuaTX-FiCOFNJzzqsTwvRTz73pz9MgZ3in9ko8DAlEumoNs4_-zFan94hE1jporpwUT8LXjbwov-bRVZAnfk11DVAW_Gtp7d7PBc-00MR2StNPvVqi6yOnTM-freCtG4TZAO6ezaXXE8Lxl4Ogxent9clEjZoHd9G8GJuKIfRQg-4ikTnz_IMkJjiirzD2ZKNJjG2PRhKgsf9oXZltiSzWqCy6lJFLc3sM43WeZ9k0slrcX9Vb_japLUGjodKZV08HsvmxcE9wThCMtZcX7-Pylk7kDzNg0c-Z3T1Ez1Slm8s9w4YjbIQYjGcqlSG8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d3fe5b208.mp4?token=cOXHZRCDLKyMwdRTp3Xp1XSLuaTX-FiCOFNJzzqsTwvRTz73pz9MgZ3in9ko8DAlEumoNs4_-zFan94hE1jporpwUT8LXjbwov-bRVZAnfk11DVAW_Gtp7d7PBc-00MR2StNPvVqi6yOnTM-freCtG4TZAO6ezaXXE8Lxl4Ogxent9clEjZoHd9G8GJuKIfRQg-4ikTnz_IMkJjiirzD2ZKNJjG2PRhKgsf9oXZltiSzWqCy6lJFLc3sM43WeZ9k0slrcX9Vb_japLUGjodKZV08HsvmxcE9wThCMtZcX7-Pylk7kDzNg0c-Z3T1Ez1Slm8s9w4YjbIQYjGcqlSG8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام با انتشار این ویدیو نوشت : ملوانان آمریکایی در حال انجام عملیات پرواز شبانه بر روی ناو هواپیمابر یواس‌اس جورج اچ. دبلیو. بوش (سی‌وی‌نی ۷۷) در حالی که این ناو هواپیمابر در آب‌های منطقه‌ای در حال حرکت است.
@withyashar
ناو بوش و لینکلن در نزدیکترین حالت به ایران هستند</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/17355" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17354">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa058f243.mp4?token=ikXTZArsYELTR_0CJRjkuYVPjYt7nI06CSl2Z8xba2RxJp9krzGKAeXfdrqElWHGUVo7FkVOOL8hVb1Fg63IzT5MHf3X0nwyKDVWsp7YFB8YdlcyQ5CSEz3Wgc7C9l9niW4NL7OaSmrNTYCLLfaUJ7YAEy7aatUHwfu7xzcCRCJ1U0IkgMHV__T0rn07Jh2YqNDRBlF8NCkwTyHIueVh6ZZDcQYqaaAFHgyjLyYQCLMHYLAnW1xAvltgNl_Q_d4RnO2AoxPRG7fGkBUJHNVivuw1cGaklpwvY9rgxNCqQx6uSvQNRI-R6c7Juf9fGvN-lHZ2LFv4GiU7p4-l5DDQtYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa058f243.mp4?token=ikXTZArsYELTR_0CJRjkuYVPjYt7nI06CSl2Z8xba2RxJp9krzGKAeXfdrqElWHGUVo7FkVOOL8hVb1Fg63IzT5MHf3X0nwyKDVWsp7YFB8YdlcyQ5CSEz3Wgc7C9l9niW4NL7OaSmrNTYCLLfaUJ7YAEy7aatUHwfu7xzcCRCJ1U0IkgMHV__T0rn07Jh2YqNDRBlF8NCkwTyHIueVh6ZZDcQYqaaAFHgyjLyYQCLMHYLAnW1xAvltgNl_Q_d4RnO2AoxPRG7fGkBUJHNVivuw1cGaklpwvY9rgxNCqQx6uSvQNRI-R6c7Juf9fGvN-lHZ2LFv4GiU7p4-l5DDQtYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا این شکلی شده
💀
از کاباره تا کان پاره
😂
@withyashar</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/17354" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17353">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سازمان بین‌المللی دریانوردی خواستار عدم به رسمیت شناخته شدن حاکمیت ایران بر تنگه هرمز شد و تلاش‌های ایران برای این کار را محکوم کرد
@withyashar</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/17353" target="_blank">📅 00:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17352">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رئیس ستاد مشترک ارتش اسرائیل در سخنرانی خود اعلام کرد:
احتمالا عملیات‌های بزرگی انجام خواهد شد، برنامه‌های جدیدی در حال تدوین هستند، انتظار می‌رود جنگ مهمی در پیش رو باشد، آماده باشید.
@withyashar</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/17352" target="_blank">📅 23:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17351">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وزارت امور خارجه ایران: اعمال تحریم‌های جدید آمریکا علیه افراد و نهادهای ایرانی، نقض آشکار بند ۹ از یادداشت تفاهم است.
@withyashar
😁</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/17351" target="_blank">📅 23:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17350">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">منابع عبری  : هم اکنون تحرکات نیروهای آمریکا در تنگه هرمز
@withyashar</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/17350" target="_blank">📅 23:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17347">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
به اصطلاح “رهبر معظم” در انزوا پنهان شده است در حالی که رژیمش در حال فروپاشی است.
ما این پول‌ها را برای مردم ایران حفظ خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/17347" target="_blank">📅 23:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17346">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خبرگزاری CNN: تصاویر‌ ماهواره‌ای‌ نشون میده که ایران داره تلاش‌ میکنه که تاسیسات هسته‌ایش رو بازسازی‌ کنه.
@withyashar</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/17346" target="_blank">📅 22:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17345">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اسرائیل کاتز
: خلبانان تازه نفس ما منتظر موج بعدی حملات هستند
@withyashar</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/17345" target="_blank">📅 22:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17344">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آتش‌سوزی در نیروگاه تبریز، استانداری آذربایجان شرقی ادعای حمله خارجی به نیروگاه را تکذیب کرد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/17344" target="_blank">📅 22:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17343">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef2410203.mp4?token=NsfxWLUZVPRJSgh0ArfxvXVB3LmJAoSIV-l84ICcQkwp4sxZgcjZ1YpLN66BmqcDfse0dBEvv-ODjfl4VLNXn4A4uMW7oTJzLI7ollsnRF8ZAXzc8aB2NyNdABtrHpV_R5S9ieX_Vlr4BS1vI6BKXSw5TWCUE1ZWyCa0FwyXFAgI5sWSvnFqhOx5LD9UKZl9YLv-pwkKwLnKrPjYRh-MkwD6ur_E2e82PABdXmIiEKctJLAyS8jcdCs2AljUi-m0nxAILhjD8Dw7SJuTrn0al7k7uUH5fE_x15oT7PT5WABQynYfaXUJakVdQp7He3XSqsr0Ry_7S6z2RjIKE_woxIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef2410203.mp4?token=NsfxWLUZVPRJSgh0ArfxvXVB3LmJAoSIV-l84ICcQkwp4sxZgcjZ1YpLN66BmqcDfse0dBEvv-ODjfl4VLNXn4A4uMW7oTJzLI7ollsnRF8ZAXzc8aB2NyNdABtrHpV_R5S9ieX_Vlr4BS1vI6BKXSw5TWCUE1ZWyCa0FwyXFAgI5sWSvnFqhOx5LD9UKZl9YLv-pwkKwLnKrPjYRh-MkwD6ur_E2e82PABdXmIiEKctJLAyS8jcdCs2AljUi-m0nxAILhjD8Dw7SJuTrn0al7k7uUH5fE_x15oT7PT5WABQynYfaXUJakVdQp7He3XSqsr0Ry_7S6z2RjIKE_woxIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انرژی بدید امشب غده سرطانی رو بزنه
@withyashar</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/17343" target="_blank">📅 22:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17342">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">شورای رهبری یمن: از رژیم ایران می‌خواهیم از استفاده از یمن به عنوان میدانی برای درگیری‌های منطقه‌ای دست بردارد و از تشدید رنج مردم یمن جلوگیری کند.
@withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17342" target="_blank">📅 22:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17341">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fshFTWxvyGLiYA8Bs7CoNz3xpjDHvmyjQe2d--DoT7QCljBRqhhBCHtLWYo2AlWd2E0L4b__vlEAkUVFsupTfgUZproArq7H5Xz2jho6NcamFSjsg3YvuEx35lsMV9anUwnM9Nm3UXXbt5TCQJ-FgVGdDPpnTfj7T_eVmG0TI_sGFXo6Gep74SkpifV96LAbgkExyEyCkEwlryQWgcHUU3TaHLTSjw1_6vwhp11iVRgdI-E74SKAswWpOto4Wh0lGVjuCCRk21SUnO7dzr0qwc2V6y1tpCZp26hKqleRHB5NOGDusOnuDe3VCSy8C24TW8NgzaqGGxjF7ltlyY25yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود ، کرج الان مثل اینکه یه چیزی هست که کلی پیغام اومده
@withyashar
به علت تاریکی زیاد نور تصویر رو خودم زیاد کردم</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/17341" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17340">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آخرین فرصت , طبق گفته رئیس اطلاع رسانی آموزش پرورش فردا قراره جلسه بزارن برای تعویق کنکور و نهایی
@withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17340" target="_blank">📅 22:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17339">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کرمانشاه الان  @withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17339" target="_blank">📅 21:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17338">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بند دیگری از قرارداد تفاهم ایران/آمریکا به فنا رفت
وزارت خزانه‌داری آمریکا تحریم‌های جدیدی مرتبط با ایران را اعمال کرد.
@withyashar
یاشار : این تفاهم نامه رو رو دستمال توالت نوشتند !</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/17338" target="_blank">📅 21:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17337">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44bd1cd0af.mp4?token=S9D-k59V22i15H56D_vv8zQsnQMp1MLgivqL03GU35ib9daYqSY7TYScFl_9XDNbb9Tf8v217kdR_jAUuTiNYYfGYWb5pApySHLUjUQw-gJAfQ53x6D4K1_YIr07vHIl42j2VxjxSFsZgGUQiqPnwIZfVEyPjGLTk3apWJPPSFuDR0QpbWGh-KQvL5-dolqA_PWuSHZakbvY6Zl7MLk7bF6hH302LwqVjJIFdhqXJqJFv8sxaCMlyI5-RNFUMoe_eylELc8JBH5pJ6zjc38qYzcTPrMWk1S-r4RREYE9R2JFUDmBZj81pgwnQ4xzRns5fIs2CMD1n81Cy5tzo5qXaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44bd1cd0af.mp4?token=S9D-k59V22i15H56D_vv8zQsnQMp1MLgivqL03GU35ib9daYqSY7TYScFl_9XDNbb9Tf8v217kdR_jAUuTiNYYfGYWb5pApySHLUjUQw-gJAfQ53x6D4K1_YIr07vHIl42j2VxjxSFsZgGUQiqPnwIZfVEyPjGLTk3apWJPPSFuDR0QpbWGh-KQvL5-dolqA_PWuSHZakbvY6Zl7MLk7bF6hH302LwqVjJIFdhqXJqJFv8sxaCMlyI5-RNFUMoe_eylELc8JBH5pJ6zjc38qYzcTPrMWk1S-r4RREYE9R2JFUDmBZj81pgwnQ4xzRns5fIs2CMD1n81Cy5tzo5qXaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کرمانشاه الان
@withyashar</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17337" target="_blank">📅 21:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17336">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حمله کنکوری های کرج به اتاق جنگ
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17336" target="_blank">📅 21:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17335">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJDwMP64S6Z8BZD76fxbswnbdjxEJDXnHEQTNB2y22CKudplWCBMyZL6eiO4wVyQZa5b5feGNbJ2ZBtYuYpZIC6d4AYJe1bNaoKf0N1dtzAfBiaIPBQ5rSxW4_mm8pqf0207UzGi-QncuhjfCa4h0j8lvxNK8zIwcIKOIr4ITznIKIix3mfoUfnoUcpM11IDO-7XGKWZJpDlH9FYgg4ITI1-OCJP2Cj_77AJHhocscSwHSJ7JNeIC2JDKwtcmUyWP3sTpxVw7nq9QEnc5mF5tj-G-lmZLxfJUs1oqqRQi5IYEw1MYl09Otf3j2somIRBjpJtyxDKH-hEMK3Lsb9Emw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرم‌ترین شهرهای جهان تو 24 ساعت اخیر
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17335" target="_blank">📅 21:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17334">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نیویورک تایمز: ایالات متحده و ایران در لبه پرتگاه درگیری نظامی هستند واسطه‌ها تلاش می‌کنند تا دورشان کنند
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17334" target="_blank">📅 21:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17333">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">صندوق بین المللی پول IMF پیش بینی کرد رشد اقتصادی ایران امسال منفی ۵.۴ درصد خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17333" target="_blank">📅 21:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17332">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تایید نشده گزارش زیاد از صدای انفجار کرج
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17332" target="_blank">📅 21:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17331">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17331" target="_blank">📅 21:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17330">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خبرنگار CBS: مقام‌های ایرانی روز شنبه برای گفت‌وگو درباره تنگه هرمز و اختلاف بر سر مسیرهای کشتیرانی که از آب‌های سرزمینی ایران عبور می‌کنند، به عمان سفر خواهند کرد.
میانجی‌های قطری به‌تازگی مشهدِ ایران را ترک کرده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17330" target="_blank">📅 21:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17329">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تصویر ماهواره جدیدی که منتشر شده نشان میدهد ناو هواپیمابر جورج بوش و گروه ناوشکنهایش به فاصله(۲۲۰ کیلومتری)  از چابهار قرار گرفته  حتی نزدیک تر از ناو لینکلن @withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17329" target="_blank">📅 21:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17328">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/470c8df2f2.mp4?token=CxMihpyc7SI2VhXsDaea779DBMTQmkNX-lDW_xqTU1CCcAtMT9-bPFbFBgL2qPNpVGfXlWXUWSFTTeya7Yk2FhbS8HIhf9Yd1HElZw3Atcf2VvAMcXvfah5r4Ed0N8EZVevmZ0KH7ln4pHaK0Rye9BvJVbnu-h4p5iT4aj4QA1daU0y3_rqWUxv6k_77S4mpJ2qgk2E29LjSTQzc2IP6kGoj7UDCsVLS25uxDvdjsRzv_Vc0P1QJAwJaej-EP6q7Wd37_cFI25pkRY9XVgvgi7-fUgd5KCA-J9mzaswvccw91lTNiUT4DWsmVevGcosfqJB0IgsqCNOyxTjst4NYAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/470c8df2f2.mp4?token=CxMihpyc7SI2VhXsDaea779DBMTQmkNX-lDW_xqTU1CCcAtMT9-bPFbFBgL2qPNpVGfXlWXUWSFTTeya7Yk2FhbS8HIhf9Yd1HElZw3Atcf2VvAMcXvfah5r4Ed0N8EZVevmZ0KH7ln4pHaK0Rye9BvJVbnu-h4p5iT4aj4QA1daU0y3_rqWUxv6k_77S4mpJ2qgk2E29LjSTQzc2IP6kGoj7UDCsVLS25uxDvdjsRzv_Vc0P1QJAwJaej-EP6q7Wd37_cFI25pkRY9XVgvgi7-fUgd5KCA-J9mzaswvccw91lTNiUT4DWsmVevGcosfqJB0IgsqCNOyxTjst4NYAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داده های ماهواره‌ای امروز دو اصابت آشکار در باند فرود در فرودگاه بوشهر در ایران را پس از حملات اخیر ایالات متحده نشان می‌دهد.آثار سوختگی نیز در اطراف باند قابل مشاهده است.
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17328" target="_blank">📅 21:12 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
