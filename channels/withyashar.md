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
<img src="https://cdn4.telesco.pe/file/XrPGZKWlPGPPA68Zo9HES1nnocbOefdvbfxUyQ81aOlyNYl3SoXtMCYwLpNa0CF4DW3PJJeE265Ag-vWB3hmBTlk9kWPbUqyzzPF7BjuR5KNWe2lf4GHSDOa2rBHDAmtr09yMQBzFyYWAaasRyNb5g3MgEaMdbE90-pUs63k1zyGVV9jwFoTL4vUtPWkwS385CX7inLUPJzSVocc7x0A30DgSvImUP1enRClkFWVDVjg-T09SCPpo4NE2dRF9w2IEYNrL8hRhkN7budGflDj5EeC0wETJajcO0fvpH74jzpYji106Qj9zcccqluAxoUl-dXWRQYMja8UiCj7WRHmcw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 423K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 13:47:57</div>
<hr>

<div class="tg-post" id="msg-19436">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">روبیو: ایران توسط روحانیون تندرو اداره می‌شود «اگر آنها پولشان را صرف مردم و اقتصادشان می‌کردند، امروز ایران احتمالاً ثروتمندترین کشور منطقه بود.» عراقچی می‌گوید سیاست آنها چشم در برابر چشم است. سیاست ترامپ سر در برابر چشم است.  اگر وضعیت با ایران به همین…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/withyashar/19436" target="_blank">📅 12:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19435">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">قیمت قراردادهای آتی گاز در اروپا به ۶۴ یورو نزدیک شده و از بالاترین سطح خود در زمان جنگ در منطقه هم فراتر رفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/withyashar/19435" target="_blank">📅 12:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19434">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">هم اکنون آژیر حمله پهپادی/موشکی در بحرین
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/19434" target="_blank">📅 12:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19433">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">روزنامه maariv : شهردار رمت گن در اسرائیل دستور بازگشایی پناهگاه‌های شهری را صادر کرد:
«احتمال شلیک موشک از سوی ایران در پایان هفته افزایش یافته است.»
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/19433" target="_blank">📅 12:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19432">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یک اسکادران جنگنده پنهانکار F-35 با عبور از اقیانوس، توسط دو سوختستان استقبال و کمی دیگر در انگلستان به فرود میآیند. یکی از آنها، احتمالا به علت نقص فنی یا برای نشان دادن خود به جهان و تمرین ، آلارم فرود اضطراری روشن کرده است. @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/19432" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19430">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35bc0c2eb1.mp4?token=ZzixWHlLVFnMmh0N2diz-0YapDn_f0i7P_hk6AGo5LmLI03WNXMBXbpGSmlr7iEoNXcVN531-ZHrC0avW_SYJ3Ri4yOhlgreH9WK5ol7vbspT45nBb90tVrNpWqhATB-X_0Ny-VWsdBO3Yal1kUSSSF0gcYFRIE5tGZpZHAUKhf1GMB8d9_y_MAO4L4YlaDX7Pzm9A7RuF64x33cZk0Kuj8rYldQyCIQTiWUeYvYac1AcBsNXJQcXB7wQ4hkt3nzeATiJqfxQXHE-3w_gRFp1N8QHP1IinqOPEY8GI0oh_DJa2heT0Nd3615fc1UBBHnLzviXJLYpTDTHYx1Dw0zDasrvh7wTM4wB6UXN6S5lZ2yw31YE5LnZSxoWCxIcygGIvnQfrAscPUrZXlQu0G_228O-5fy3CXLCuHq_P-_j3VZ1jzFtBDx9ewyOF8LwLsp8uXt9ELV1_sPSrQk2MpwRMKOHvgbIDdtLhIyema0GEgjsOsYhoWQ8IHsdx7AWWbo8uDa-W4h_OyL4Z3MFGgBuQmUYe7y0dLswX-CvjE4q1HX6GpgTk11y6BGn62KEfdv5_7YNbj4g0Fmvbl4B_3cflczQIGlWq4HqtNX5QyX11hmwzYoGjx3gYUG-v0KKpe5YlOIhUNQ5auSTADH4rXEwoZzClwQPPziuG-HbX-u8fI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35bc0c2eb1.mp4?token=ZzixWHlLVFnMmh0N2diz-0YapDn_f0i7P_hk6AGo5LmLI03WNXMBXbpGSmlr7iEoNXcVN531-ZHrC0avW_SYJ3Ri4yOhlgreH9WK5ol7vbspT45nBb90tVrNpWqhATB-X_0Ny-VWsdBO3Yal1kUSSSF0gcYFRIE5tGZpZHAUKhf1GMB8d9_y_MAO4L4YlaDX7Pzm9A7RuF64x33cZk0Kuj8rYldQyCIQTiWUeYvYac1AcBsNXJQcXB7wQ4hkt3nzeATiJqfxQXHE-3w_gRFp1N8QHP1IinqOPEY8GI0oh_DJa2heT0Nd3615fc1UBBHnLzviXJLYpTDTHYx1Dw0zDasrvh7wTM4wB6UXN6S5lZ2yw31YE5LnZSxoWCxIcygGIvnQfrAscPUrZXlQu0G_228O-5fy3CXLCuHq_P-_j3VZ1jzFtBDx9ewyOF8LwLsp8uXt9ELV1_sPSrQk2MpwRMKOHvgbIDdtLhIyema0GEgjsOsYhoWQ8IHsdx7AWWbo8uDa-W4h_OyL4Z3MFGgBuQmUYe7y0dLswX-CvjE4q1HX6GpgTk11y6BGn62KEfdv5_7YNbj4g0Fmvbl4B_3cflczQIGlWq4HqtNX5QyX11hmwzYoGjx3gYUG-v0KKpe5YlOIhUNQ5auSTADH4rXEwoZzClwQPPziuG-HbX-u8fI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روبیو: ایران توسط روحانیون تندرو اداره می‌شود
«اگر آنها پولشان را صرف مردم و اقتصادشان می‌کردند، امروز ایران احتمالاً ثروتمندترین کشور منطقه بود.»
عراقچی می‌گوید سیاست آنها چشم در برابر چشم است. سیاست ترامپ سر در برابر چشم است.
اگر وضعیت با ایران به همین منوال ادامه یابد، آن‌ها بهای سنگینی خواهند پرداخت.
@WarRoom</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/19430" target="_blank">📅 12:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19429">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وزارت خارجه آمریکا برای سومین بار پیام هشدار صادر کرد:
تنش در خاورمیانه بالا است، خطر تشدید ناگهانی وجود دارد.شهروندان آمریکایی احتیاط بیشتری داشته باشن
@WarRoom</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/19429" target="_blank">📅 12:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19428">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a1de54c5.mp4?token=JYjGVJJ3h7SErqAltTpiQ1C6A5rXLffPeyHmCpU3ChxRH6FzO-txpHo6UbYhjZp1Jq1HzRWk9HTrSWn_pu4k-0TzWtoiGS-cqOWOkQfWBxl5zue0nW5RpQTSFytMk4sBj2jCRNi85BwwdNBPBldvNzkmZSv6-BuAS7J8cWF_SmcZiV67OVzq5Zuz5liAPfhZuohbJTviVebz-pwPvo13yXF_FcUSGWIs2hipYqIEVdB0gS0oOdtVcHeVe4TB6HrZpzQWBMu5mX-GRv0Ibtw8FWy0pm_UwC5P03KW53svRC23a4a_AJHguyrCz2pGsft0wMetE92T3ed3WbvqFuC4yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a1de54c5.mp4?token=JYjGVJJ3h7SErqAltTpiQ1C6A5rXLffPeyHmCpU3ChxRH6FzO-txpHo6UbYhjZp1Jq1HzRWk9HTrSWn_pu4k-0TzWtoiGS-cqOWOkQfWBxl5zue0nW5RpQTSFytMk4sBj2jCRNi85BwwdNBPBldvNzkmZSv6-BuAS7J8cWF_SmcZiV67OVzq5Zuz5liAPfhZuohbJTviVebz-pwPvo13yXF_FcUSGWIs2hipYqIEVdB0gS0oOdtVcHeVe4TB6HrZpzQWBMu5mX-GRv0Ibtw8FWy0pm_UwC5P03KW53svRC23a4a_AJHguyrCz2pGsft0wMetE92T3ed3WbvqFuC4yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله صبح امروز به منطقه دوم دریایی ولایت نیروی دریایی ارتش در جاسک ، جنوب شرقی ایران
@WarRoom</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/19428" target="_blank">📅 12:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19427">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">صداوسیما:دقایقی پیش صدای چند انفجار در کنارک شنیده شد
@WarRoom</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/19427" target="_blank">📅 11:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19426">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏رویترز: آمریکا در حال اعزام نیروهای تقویتی به خاورمیانه است
‏خبرگزاری رویترز گزارش داد پس از تهدیدهای گروه تروریستی حوثی جمهوری اسلامی، آمریکا در حال اعزام نیروهای نظامی تقویتی به خاورمیانه و گسترش گزینه‌های نظامی خود در منطقه است.
@WarRoom</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/19426" target="_blank">📅 11:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19425">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وزیر امور خارجه آمریکا، روبیو : ایران در حال حاضر آمادگی لازم برای انعقاد توافقی با ما را ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/19425" target="_blank">📅 11:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19424">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3405b1189d.mp4?token=S4SxAHBR9ByhM8UqLEfL632NOhTmhbUJPFjS5JL9yoSa6kwXPpDLtCeserNnChRTd2sCEXUSFekhIibH09xd-T36fyA_8OXlMuUFHD3ajik8TCj4jU4p4cCRBteHdcoTJW8H9-EnHArw-5cBjev1y7QeztA5bo0AevCR7JIGL_VmrkgYdpDfUdjq9Up04LUPJI-zc5ZI8WmZC90aXkpLgn4XcWLB3U3kZlB-IWzwDtxVflqTUZk-lgJG8edlKvPWuE8qFI7PR8oDKpm5QJ6gWJa4YvhMVRvsSuyFsla_udQAz5zT9LK6YYtfLelnkEL5plhwP5-n39-gtCM5dMq7xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3405b1189d.mp4?token=S4SxAHBR9ByhM8UqLEfL632NOhTmhbUJPFjS5JL9yoSa6kwXPpDLtCeserNnChRTd2sCEXUSFekhIibH09xd-T36fyA_8OXlMuUFHD3ajik8TCj4jU4p4cCRBteHdcoTJW8H9-EnHArw-5cBjev1y7QeztA5bo0AevCR7JIGL_VmrkgYdpDfUdjq9Up04LUPJI-zc5ZI8WmZC90aXkpLgn4XcWLB3U3kZlB-IWzwDtxVflqTUZk-lgJG8edlKvPWuE8qFI7PR8oDKpm5QJ6gWJa4YvhMVRvsSuyFsla_udQAz5zT9LK6YYtfLelnkEL5plhwP5-n39-gtCM5dMq7xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب ۲ موشک با صدای مهیب از خرم آباد لرستان  @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/19424" target="_blank">📅 11:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19423">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نفت ۹۸$
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/19423" target="_blank">📅 11:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19422">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گزارش انفجار ‌در ‌قطر
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/19422" target="_blank">📅 11:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19421">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Urk-pRYPeRI6aFtLShKHlMDq-pvzUV0Rcq4yIy6h2nbIhnLjtAJc9-tAtItD37VfLRwy7hSWStfxXK08aJqYc16VLuEZlXuYTxjY3NUzr9_-VYzQSJdBSDDKyPf3NQvBvjTXLOdTYniF1KQNTaP_xorLsbJ4cSXhqzdNFKaj-W06TdGKYYsmwFKlSBqya4pp0eT0MLgaHFFVlvW1oYekgqRYjCbe5EE63CkVmjlkm_DeOb1vcdpmBCDWPPaNy2IrFPcsNR74P9IXm114M4v-y3976ACp5sbhKAw6EARmkbIN6_nkwcuIt2cJzxBNNFaMxH2NnHwEpwPBl1xBUo4IXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب ۲ موشک با صدای مهیب از خرم آباد لرستان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/19421" target="_blank">📅 11:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19420">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">معاون امنیتی استاندار بوشهر: شهر دشتی سه بار مورد حمله آمریکا قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/19420" target="_blank">📅 10:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19418">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آلارم اتاق جنگ : فردا شب از نزدیکی منطقه های حساس نظامی ، تونل و پل های مهم که مسیر عبور تجهیزات نظامی هستند عبور نکنید !
⚠️
⚠️
⚠️
@WarRoom
یاشار : فردا شب ویسکی و آبجو میکس
🤒
⚔️</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/19418" target="_blank">📅 10:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19417">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3Aq7sb7HCDCAcUxFjOKYQpqeQ9RcV4QRto14RHJQkfBNAqcD5znuyKOfqA449rKqz70XCMHSYUiVAqgUx6WcT-WZ2Ry93Vl8zXXX4tGBE_wEPZgzZ0pdbVYQGPKHh6KZT3lX8r8AOXSFCty4AOLQvGJd3ud498Gg1CSKpba6zE0yO5_yb1J1xHKpn_zb9-5TCIRArpt1gEt7HkkPbAK2jl9N07VJ8En-hdLqyqFiWTUfyaoZcmyY_ccwxlr_D0a_LIHsIepimEiRxWonxptq-b5vU0Lt5By_VONMOuoq7_KQvrzNXIbDCZi0-fBewSP1iP1RZYwgEoVuvR4RcAezA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همانطور که در پست اینستاگرام (اتاق جنگ دروازههای جهنم) نشان دادم، هواپیماهایی که دیشب از آمریکا حرکت کرده بودند همکنون روی اروپا و نزدیک به خاورمیانه هستند.
فعالیت هواپیماهای ترابری نظامی C-17 و C-5M نیروی هوایی ایالات متحده در مسیر بین اروپا و خاورمیانه، به سطحی افزایش یافته که مدت‌هاست مشابه آن مشاهده نشده است.
منتظر یک جنگ تمام عیار باشید. دروازهها باز شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/19417" target="_blank">📅 10:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19415">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBxqh6ss5aqCj0zBRSvqyCfUoZ8_M98wKvP37jmvQA3zwNBQn6xMnDhnLfHKu-hhDHShLJwlaoVUdrWXqgzwZOyKGOgACh6FMDi69w0o48fbvM4t2ky-jLOzx7j1oa9FGP_7m-aEXxrxyasCJDC13FEMz3QaKnJAx8Rup-S6MjlFAvPSa4lEIrYzD-pcF7FA8i1YO7Kl8N1fz9MMXrozvZpwsHGh4NB7dzvNQMy9qwUvf84Tsy1Rd7rgi2m8HFTImhgsPXvKtgL9sxkUBZC_MQlsD59Br2VBekQtMQ3_MzFOhEdf2IRcmTMuw-aJCabrm20gglDBHqCtXXZ7vwkOAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه امروز صبح خواهران دوقلو رومینا رحیمی و  ترانه رحیمی اعدام شدن
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/19415" target="_blank">📅 10:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19414">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOudGEW5NhF47akn5c5I7J_CgeMd0eA6U6tsFR1_rkdg58Goz-07lpXqDiA1hxlA_YNUDPL2o1xdnbbB1THIWLNWfRmwSFpUHL8_GxYNYSDhpC9LP-newa_gf5wT2N1fbs1Hj-_Q6SNYHsAC4tZOxf6q9qXlp3p5YOCux0W1dUS6uductrulSe4Qnm8G1W-2JUyQ3zDsDASPN0Kc4fvbugIlKIYgKdn-K6HIHj6tB7paO--fv21RBG4_99E5Wj8RmVeK6COoPxOcIphYcnmpIjgCIdgNuz5ssgDhmSPB7mjhV2mVHn73e4hxmL8R82_XGQkMgrKjHW-mMWiuEM36Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج جدید موشکی سپاه : هم اکنون پرتاب دو موشک از خمین
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/19414" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19413">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7LTyAvUJR0c8VwuA3JzXaa6GKj8G-P9pjoXva8R-jlaMrok0fn00dOY-h1j8vvT8w8sMHsR1fXE0XsgGMr3wQ2y4Ma_xRYxCQJekFyWC6w1jfEL75c2mwoNQzItYfuvUy_zzE1SgI7ca4obQtbbbcyoU42_1raCpizI9bravMpgbIboTpi3MYI-_5_1-m_szzL-euAg-tCe7u1rRnNoK48ZRBUHhmuTXb9ob1MyfwBUm2_O8-Y2VF9DdrQ1i1mR5sT6fmFf8QF2vomcyrU79bio8uD9DjNGSJLu37ALTHjSSb-kjQ3z6HMG0peu4dZATrmwni-3FU5BhTXB6_riBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏مجله معروف ایتالیایی "اسپرسو" با نشر مقاله اخیر خود، اذعان داشت:
‏دیگر نمیشود به محمدرضا شاه پهلوی گفت «آخرین شاه ایران»
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/19413" target="_blank">📅 10:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19412">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بامداد امروز، در پی حمله آمریکا، نقطه‌ای در شهرستان کیار هدف حمله هوایی قرار گرفت.
عبدالعلی ارژنگ معاون سیاسی، امنیتی و اجتماعی استاندار چهارمحال و بختیاری با تأیید این خبر اظهار کرد: این حمله در ساعات اولیه بامداد امروز رخ داده و دستگاه‌های مسئول بلافاصله در محل حاضر شده و اقدامات لازم برای بررسی ابعاد حادثه و ارزیابی خسارات احتمالی را آغاز کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/19412" target="_blank">📅 10:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19411">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رئیس جمهور ترامپ در مورد ایران: من آن را یک درگیری می‌نامم. ما با جمهوری اسلامی ایران درگیری داریم. آنها آنقدر ضربه می‌خورند تا معامله کنند، اما من می‌گویم که آنها آماده معامله نیستند. آنها آماهده نیستند چون بعد زیرش میزنند. اما خیلی زود آماده خواهند شد. @WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/19411" target="_blank">📅 10:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19410">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کنگره آمریکا نسخه خود از قانون بودجه امنیت ملی سال مالی 2027 (NDAA) را تصویب کرد که شامل بندهایی برای افزایش همکاری‌های امنیتی بین ایالات متحده و اسرائیل است.
این بودجه، بیش از 750 میلیون دلار را به برنامه‌های همکاری‌های امنیتی بین دو کشور اختصاص می‌دهد، که حدود 65 میلیون دلار بیشتر از سال گذشته است، و همچنین شامل طرح‌هایی برای گسترش همکاری‌ها در زمینه فناوری‌های امنیتی می‌باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/19410" target="_blank">📅 10:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19409">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a1f97fe0f.mp4?token=QKccXNU8-BzdgROwyipA2Rp0zlXa_bgSGVrEJadkGjvO7muM-Nk_WlQkUBaTds_qRG6Rr2Ij2NV2DH-K0uLOKmowT35reDdRiJVK7ev7sEjcOI3KTCA2yYiWovxuCMXr0GpTq0aNUmLjrdf7zw12fQRFEK9l6mxiLcYowE-DmsZlUVthjrgfcGv_gY8-c_0iFmXbnCuEMwjTClOutrV7_lstpZYnhjVI_piCVrr0VpU8NjL7kMoKeSqCkpnfB6Q3XWAMsGNj5STRCXkfc_jA59dS5JDmgwqzvYRoHUK2f5Z2kRX_nzSc62yQIpc74IM5RubEpi7vyqSRjG6_bD_4PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a1f97fe0f.mp4?token=QKccXNU8-BzdgROwyipA2Rp0zlXa_bgSGVrEJadkGjvO7muM-Nk_WlQkUBaTds_qRG6Rr2Ij2NV2DH-K0uLOKmowT35reDdRiJVK7ev7sEjcOI3KTCA2yYiWovxuCMXr0GpTq0aNUmLjrdf7zw12fQRFEK9l6mxiLcYowE-DmsZlUVthjrgfcGv_gY8-c_0iFmXbnCuEMwjTClOutrV7_lstpZYnhjVI_piCVrr0VpU8NjL7kMoKeSqCkpnfB6Q3XWAMsGNj5STRCXkfc_jA59dS5JDmgwqzvYRoHUK2f5Z2kRX_nzSc62yQIpc74IM5RubEpi7vyqSRjG6_bD_4PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب یه دلقکی اینجوری پشت ترامپ ادا شو درمیآورد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/19409" target="_blank">📅 09:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19408">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LI69FbJPycI64bZurgoDCS4QJ7KVR-4nfnBRgh9KNaYWqwJQ4Yh6iZfodN6SDMe2jQipT_rr-mR8k2yRZDtL7Z8D595z-XY3dgf9dK0oYkfdWr1BT7bB-pbrxQEemMbWTAOtAaHp69xfLTTZjvEJQ3uCXY7HCA4FwnmxG-KhesYiFASRyxZscfxM1FJIoKp3zIx9v7d2LokcOfa5cqahm7CrfHidrOhdj6EhLCHT1sWqcFBqbXBee6MmRBmzhAI6CmQiUzB-fDtrM05gTNSUlJvw1qveJyw7CCiaB_ob1rkdKlwyPpHrIq8acNojeSs2_nzSoVbwReJmsqL_rg3dAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏گزارش‌ها حاکی از آن است که بامداد امروز دو شناور جستجو و نجات دریایی «ناجی ۱۵» و «ناجی ۱۶» در حمله نیروی دریایی آمریکا هدف قرار گرفته و آسیب‌های سنگینی دیده‌اند. بر اساس گزارش‌های اولیه، احتمال غرق شدن هر دو شناور وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/19408" target="_blank">📅 09:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19407">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PuGxwEf30Qbf68dTrp1N53C0oQBFBmzk5uAun_HnTc2Yfg3uGUV0Xesp4UjhsTa-hdtcpnj_7grKxOh-DxuNXGo1LlqzDbnA5z_hVo2qmhwllh9zNOcihvWkvRRmFSjaSwFCx_36MlIyKV3r2cELTE2PxG71KOWwGvX2tHQFtvhTnJQnOMT1AjM5YB0pzjBqg3gOugQFI_F_iiANm_JkJ_M1Nn5z0eGxmMXFHz1Wm1r4XGcGzipdi18M02eLUqPI1nEJiqifWbNeMkgbTpOQ996-bK3I8p3HdWewsDShvck9wU2f23K07IrArL8D6ngM-abYAQoy-QyoOxToPT0kAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان، با توجه به سوالات شما، حضور رادان ساعاتی قبل از حمله در شلمچه تایید شده است. ولی این که آیا هدف ترور بوده و کشته شده یا نه، هنوز مشخص نیست. در لحظه که خبری به دستم برسد، شما را در جریان خواهم قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/19407" target="_blank">📅 09:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19406">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">لیست نهایی شهر هایی که دیشب مورد حملات آمریکا قرار گرفته‌اند
💥
شلمچه
💥
سیریک
💥
رامشیر
💥
بندرعباس
💥
بندر جاسک
💥
بوشهر
💥
اهواز
💥
بندر ماهشهر
💥
اندیمشک
💥
اسلام آباد غرب
💥
ابهر
💥
کرمانشاه
دوازدهمین شب و کشیده شدن حملات به غرب کشور
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/19406" target="_blank">📅 08:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19405">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گروه حوثی‌های یمن امروز پنج‌شنبه اعلام کردند دو نفتکش متعلق به عربستان سعودی را که در حال عبور از دریای سرخ بودند، با موشک و پهپاد هدف قرار داده‌اند. ساعاتی بعد، عربستان نیز اصابت پرتابه به یکی از این کشتی‌ها را تایید کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/19405" target="_blank">📅 08:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19404">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گزارش CNN: یک مامور سازمان اطلاعاتی از تیم امنیتی معاون رئیس‌جمهور، جی-دی ونس، به دلیل افشای اطلاعات به رسانه‌ها، از سمت خود معلق شد.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19404" target="_blank">📅 08:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19402">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88a54a3c2c.mp4?token=N92_RDZfkrLXp_5FPxa0W9SeGl-TEvn6COrjX1vuXvLrCgcZ4UzLvilV1PS9x-GdVwTR6KYJCGArp5UE-TJv4xJUw3vG3te6FDfIJFYnQKLMqvzNmPGjdnmWgFzWmI4KnqfpZbr6KPtvxgDjy-elMK4K4PtF0DV8lJ3uXH1bzAPPtBZWoDK6_H_rppzsN2-X_t7oFz6qo_TNysZefAE5kKhLuZue-zxXPmU5KTePXiJvSAXZbc_uNwDEXh_AeRINwg00Yn_1b9ESmHfIGZgOeNAunRy5J06F-WIyH6PqPOdIV3GtiJHxuOQP_AUWxO3puEhlEKlAj-wb8iM5Qti8fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88a54a3c2c.mp4?token=N92_RDZfkrLXp_5FPxa0W9SeGl-TEvn6COrjX1vuXvLrCgcZ4UzLvilV1PS9x-GdVwTR6KYJCGArp5UE-TJv4xJUw3vG3te6FDfIJFYnQKLMqvzNmPGjdnmWgFzWmI4KnqfpZbr6KPtvxgDjy-elMK4K4PtF0DV8lJ3uXH1bzAPPtBZWoDK6_H_rppzsN2-X_t7oFz6qo_TNysZefAE5kKhLuZue-zxXPmU5KTePXiJvSAXZbc_uNwDEXh_AeRINwg00Yn_1b9ESmHfIGZgOeNAunRy5J06F-WIyH6PqPOdIV3GtiJHxuOQP_AUWxO3puEhlEKlAj-wb8iM5Qti8fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برج راداری گذرگاه مرزی شلمچه
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19402" target="_blank">📅 07:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19401">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKBcukiXtvK9aASzUlJjkAXlj5VdfEPlWgr6V0oGYxQGPXu-bH63-JKR-maUGl4WiT8w55wm3QLtaAO6amsiPuqvwb3zo4gV47ERFrDiVh6OSeaVf98wQwbLgLesGA9M8aInxsM_ob2MXp42iohrABLYsApDiykpWyyT_Z-oEGA6LfJ8Ar94RZB4lx5eZPaOOvB1yyUJXFcXyiOr6mDQMUswb_4Knn6MGHGYuEmMJI846YX7BtyTnSZQVzmp7Pv7THxyQLXVUIRFdWeB3ltc28f2jzifTCWLtvbYwcFuJudnRsKIeZt3IUruzsPu68HEyNhyO9p5bDhPWTJE-AqV3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: بمب‌افکن دوربرد بی ۱ آمریکا مواضع سپاه پاسداران را هدف قرار داد
‏اکسیوس به نقل از مقام‌های آمریکایی گزارش داد یک بمب‌افکن بی ۱ نیروی هوایی آمریکا روز سه‌شنبه با پرواز از پایگاهی در بریتانیا، اهدافی متعلق به گروه تروریستی سپاه پاسداران در ایران را بمباران کرده است. این نخستین استفاده آمریکا از بی ۱ از زمان ازسرگیری درگیری‌ها در ۱۲ روز گذشته است. این بمب‌افکن فراصوت توان حمل ۲۴ بمب ۹۰۰ کیلوگرمی یا ده‌ها موشک کروز را دارد و از بیشترین ظرفیت حمل مهمات در میان بمب‌افکن‌های آمریکایی برخوردار است. مقام‌های آمریکایی و اسرائیلی می‌گویند هم‌زمان با تقویت حضور نظامی آمریکا در منطقه، پرزیدنت ترامپ در حال بررسی آغاز دوباره عملیات گسترده علیه رژیم تروریستی جمهوری اسلامی طی روزهای آینده است.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19401" target="_blank">📅 07:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19400">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">معاون استانداری خوزستان:
در حمله موشکی آمریکا به گذرگاه مرزی شلمچه تاکنون دو نفر شهید و ۱۱ نفر مجروح شده‌اند
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19400" target="_blank">📅 07:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19399">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bf35d9766.mp4?token=awFuw-m-VoTFqvri0TkYqvBPFjUQmdGvnuGGcAEG6UzeHiwO0XzA1qpZI2K3zRfrvjhF_FprGd9ZYLuBojE1AhuSoYnPYkJuS-y9LWvNMRBhHTEHxvYj9I4dN3Efr1qWwYcdBGQfmSCwckmJxxEwZOiVNf5RawVcauVR_Cg3P5PhacY_DE-QquQy_G7StmuVwtfN1CafW4B6jISlEoHPeS-8_uyBmPcnZa6_IZRbVyp6oWg-2ErrRT_m7Mu7ddH5rG5lMnnfwKkT7dDFIp8jPHOTms66E7ejS4Z7R5TAqtDjrBlmJpI2L4wANHG_saCbLs1MyOSN7SUNubuVUtwYpIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bf35d9766.mp4?token=awFuw-m-VoTFqvri0TkYqvBPFjUQmdGvnuGGcAEG6UzeHiwO0XzA1qpZI2K3zRfrvjhF_FprGd9ZYLuBojE1AhuSoYnPYkJuS-y9LWvNMRBhHTEHxvYj9I4dN3Efr1qWwYcdBGQfmSCwckmJxxEwZOiVNf5RawVcauVR_Cg3P5PhacY_DE-QquQy_G7StmuVwtfN1CafW4B6jISlEoHPeS-8_uyBmPcnZa6_IZRbVyp6oWg-2ErrRT_m7Mu7ddH5rG5lMnnfwKkT7dDFIp8jPHOTms66E7ejS4Z7R5TAqtDjrBlmJpI2L4wANHG_saCbLs1MyOSN7SUNubuVUtwYpIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۱۰:۳۰ شب به وقت شرق آمریکا (۶ صبح به وقت تهران) در ۲۲ ژوئیه، برای دوازدهمین شب پیاپی، دور دیگری از حملات علیه ایران را به پایان رساندند.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19399" target="_blank">📅 07:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19398">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حمله رژیم به کویت و اردن
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19398" target="_blank">📅 03:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19397">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19397" target="_blank">📅 02:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19396">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromrebel1</strong></div>
<div class="tg-text">ما رفتیم پشت بوی با یه فلاکس پر چای و سیگار
🤣</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19396" target="_blank">📅 02:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19395">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e59327e2a3.mp4?token=T6aesOg4bRl_80asm6cbNzNPmsW4bE8q3hkVnVS4MTfsHcBrOFXLkIll3n6EUQ7DG6dZXcBVqrP0TtLrcpl_qKnWHNJn0BPwXzM34Y0YurtKQZax93Be67j0kRvNjlrFjR0pwF7DttCl3IAzQxIgco4lg5_h1gR7ostPAz3txxeDk6wSKpa242uQDJ3Ug-VQY2FJy7yhkTN49IOq5h-CExzb9Z7GZQJl0zC6S7boSVp55BE6aC-T6OalpIFoY66F-82TCq52qgQt_Sgqx7fZxoCsYEoyCQ7_5b6w0kowId6aHkESnmu7hy4jfjZQseNJVKkU2NqWPU-1tZR2Oy3iYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e59327e2a3.mp4?token=T6aesOg4bRl_80asm6cbNzNPmsW4bE8q3hkVnVS4MTfsHcBrOFXLkIll3n6EUQ7DG6dZXcBVqrP0TtLrcpl_qKnWHNJn0BPwXzM34Y0YurtKQZax93Be67j0kRvNjlrFjR0pwF7DttCl3IAzQxIgco4lg5_h1gR7ostPAz3txxeDk6wSKpa242uQDJ3Ug-VQY2FJy7yhkTN49IOq5h-CExzb9Z7GZQJl0zC6S7boSVp55BE6aC-T6OalpIFoY66F-82TCq52qgQt_Sgqx7fZxoCsYEoyCQ7_5b6w0kowId6aHkESnmu7hy4jfjZQseNJVKkU2NqWPU-1tZR2Oy3iYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان لانچرها خف کرده در تونل آزاد راه اراک خرم آباد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19395" target="_blank">📅 02:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19394">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19394" target="_blank">📅 02:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19393">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7qD51calnFDJUtpx2FUFVMDLCjSDFBV_FrTlMKqMkGzhkuInKXyZwZsCDxQUWDYMYikYb_YgTtn7AuFegLyIJkAXnzUj_funo6V0glEnWqNTLq9yaLhT3JOiuxHf80sXdIyDZiFL5fel-LTkOdv1GAixsyj2GqH1gCApg3lsQUZSuJITD0-ZVmkI-4cq8KBaEqwLKXH3-Ttts3DydEc1LCcpQvjHEOkQcsevLexs-ZGwmSptxvDS3o26LdMXdjp5T7T2VpK1dhv6mmLZvTz_vq8R2OYRsokrV6GUUIb-6yGs13h7sSOGx42RJzCsAeQHsgdyglOFhZAGJzjsn39CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌های امشب مبنی بر حملات ایالات متحده به ایران تا این لحظه در مکان‌های زیر منتشر شده است:
💥
پایگاه دریایی زیارت سیریک،
💥
سیریک، استان هرمزگان
💥
رامشیر، استان خوزستان
💥
اهواز، استان خوزستان
💥
بوشهر
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19393" target="_blank">📅 02:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19392">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ادعای وال استریت ژورنال:
ارتش آمریکا در حال اعزام نیرو های عملیات ویژه، پزشک، سلاح و مهمات به خاورمیانه می‌باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19392" target="_blank">📅 02:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19391">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فرماندار شهر بوشهر در ایران: یک نیروگاه برق روز چهارشنبه در نزدیکی نیروگاه هسته‌ای بوشهر، در جنوب این کشور، مورد اصابت موشک قرار گرفت.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19391" target="_blank">📅 02:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19390">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گزارش انفجار بوشهر جدید
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19390" target="_blank">📅 01:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19389">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مجلس نمایندگان آمریکا بودجه 95 میلیارد دلاری تامین هزینه جنگ با ایران را با 216 رای موافق و 214 رای مخالف ، تصویب کرد.
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/19389" target="_blank">📅 01:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19388">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سنتکام: امروز ساعت 5:30 بعد از ظهر به وقت شرق آمریکا، نیروهای آمریکایی با دستور فرمانده کل، حملات بیشتری رو علیه اهداف نظامی ایران آغاز کردن.  این عملیات با هدف تضعیف بیشتر توانایی ایران در تهدید ملوانان غیرنظامی و کشتی‌های تجاری در حال عبور از آب‌های منطقه‌ای…</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19388" target="_blank">📅 01:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19387">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سنتکام: امروز ساعت 5:30 بعد از ظهر به وقت شرق آمریکا، نیروهای آمریکایی با دستور فرمانده کل، حملات بیشتری رو علیه اهداف نظامی ایران آغاز کردن.
این عملیات با هدف تضعیف بیشتر توانایی ایران در تهدید ملوانان غیرنظامی و کشتی‌های تجاری در حال عبور از آب‌های منطقه‌ای انجام میشه.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19387" target="_blank">📅 01:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19386">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سندی محکم از قرار دادن لانچر کنار اتوبان و یک شرکت دارویی که مردم را  سپر انسانی و در خطر قرار میدهد تا در صورت حمله بگویند که آمریکا شرکتهای داروسازی و مردم را هدف قرار میدهد ، همچنین امروز هم یک ویدیو از هدف قرار گرفتن یک لانچر با پوشش استتار شده قرار دادم…</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19386" target="_blank">📅 01:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19385">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نفطه زنی لانچر با پوشش کاه و یونجه در اتوبان قم به کاشان @WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19385" target="_blank">📅 01:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19384">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سندی محکم از قرار دادن لانچر کنار اتوبان و یک شرکت دارویی که مردم را  سپر انسانی و در خطر قرار میدهد تا در صورت حمله بگویند که آمریکا شرکتهای داروسازی و مردم را هدف قرار میدهد ، همچنین امروز هم یک ویدیو از هدف قرار گرفتن یک لانچر با پوشش استتار شده قرار دادم که شاهد عینی لانچر را به وضوح دیده بود ولی هدف حمله بعضی افراد قرار گرفتم اکنون این ویدیو سند و محکم است که رژیم این کار را از کنار اتوبانها هم انجام میدهد.
این پست را به تمامی زبانها در همه جا منتشر کنید تا به دست جامعه جهانی برسد.
https://www.instagram.com/reel/DbHEPESRguI/?igsh=ZWJjcW5qdTU0b2xv</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19384" target="_blank">📅 01:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19382">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گزارش انفجار بوشهررررر
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19382" target="_blank">📅 00:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19381">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سازمان دریانوردی بریتانیا:
دقایقی پیش یک نفتکش عربستان در نزدیکی این کشور مورد اصابت یک موشک قرار گرفت و آتش سوزی گسترده ای نفتکش را در بر گرفته است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/19381" target="_blank">📅 00:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19380">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گزارش انفجار رامشیر خوزستان
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/19380" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19379">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گزارش انفجار دزفول
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19379" target="_blank">📅 00:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19378">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پاسگاه سیریک رو زدند
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/19378" target="_blank">📅 00:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19377">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAW3pKEhm5l4GNl4isCTaPxh56K0woeq8qFTWDJRsQ441SM1bN7lEcBxUiEoUPh1nD-g_vlIgGpQJN_xMrWNcCZHm7H15ZFtxqk0QK6WXArIpmLWDZadG6rTU6jcF3V-gT4iXPm8Hz1QkpuN9zwF0jzTEOtxxER_FnriV-ATj8N50fN45R9sGMFqqA29bT8z-gocNoUfH-Tx6_Tyk5h9SbPKu7sVoujECvwLHOQm_ML-_oY_5lVtqAjdUPu77kf23OnqMdku4jXRGPnYOJ01dffudiO6CaTIJ-4yQY9tp7yomsukhJMUuDlqFZAbGoXP_ko-00pA59xsTAzpoxIKrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحنه ای که امشب مردم ایران منتظرند روی فلایت رادار ببینند.
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/19377" target="_blank">📅 00:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19376">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">صداوسیما: دقایقی پیش؛ شنیده شدن صدای انفجار در بخش بمانی شهرستان سیریک
همچنین دقایق پیش صدای چند انفجار در اطراف روستای زیارت شهرستان سیریک شنیده شد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/19376" target="_blank">📅 00:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19375">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گزارش انفجار رامشیر خوزستان
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19375" target="_blank">📅 00:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19374">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پرواز جنگنده تبریز
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/19374" target="_blank">📅 00:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19373">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دو انفجار اهواز
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/19373" target="_blank">📅 00:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19372">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گزارش صدای انفجار بندر ماهشهر
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/19372" target="_blank">📅 00:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19371">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شروع شدددددد
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/19371" target="_blank">📅 00:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19370">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گزارش صدای انفجار اهواز
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/19370" target="_blank">📅 00:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19369">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">از شهر موشکی مخوف یزد موشک پرتاب شد
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/19369" target="_blank">📅 00:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19368">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اسرائیل با ارسال یک پیام به هزاران نیروی پلیس خود آماده باش داد:
"با توجه به نگرانی از وخامت اوضاع امنیتی، تمام پلیس‌ها باید در دسترس و آماده برای هر سناریویی باشند، به طوری که تجهیزات شخصی آن‌ها در دسترس و آماده استفاده در صورت نیاز باشد."
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/19368" target="_blank">📅 23:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19367">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حقیقت یاب سنتکام: ایران تنگه هرمز را کنترل نمی‌کند. این مسیر آبی بین‌المللی علیرغم تهدیدها و حملات سپاه پاسداران باز است. کشتی‌های تجاری همچنان با پشتیبانی نظامی ایالات متحده از تنگه عبور می‌کنند. از اوایل ماه مه، نیروهای آمریکایی به عبور بیش از ۹۰۰ کشتی از تنگه کمک کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19367" target="_blank">📅 23:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19366">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00cad83b45.mp4?token=iqvs5chkITacgCFRrxhEsbJf7hUKvo78ZnMdWolEza-s75Gvy62t1r6aMp_tRRBNxBDg8MYKHCb126Ek30PYQROBLHMy8D0IqcxQaPwp8JesOFanIrkpGhOEAevBVb0uhpcalaFog1FFiUwWn92NvlnilshzspcRz9LgFy9T_Rwh0xF_JYDZFDBbqgo4ran10KCQNXkdEPO68ZVYyHE_svMgg_mJDX90YCVDkk-H78loBVjCSItUjcJt2Qxf9mmbTmKb-XuybsqoARbVXZleh50zDdZ7Xi5C0Dj7_jSHDnvEohshSqxV09IbLR9fSDrhMQw4BzWogtDwXqcqDHoVgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00cad83b45.mp4?token=iqvs5chkITacgCFRrxhEsbJf7hUKvo78ZnMdWolEza-s75Gvy62t1r6aMp_tRRBNxBDg8MYKHCb126Ek30PYQROBLHMy8D0IqcxQaPwp8JesOFanIrkpGhOEAevBVb0uhpcalaFog1FFiUwWn92NvlnilshzspcRz9LgFy9T_Rwh0xF_JYDZFDBbqgo4ran10KCQNXkdEPO68ZVYyHE_svMgg_mJDX90YCVDkk-H78loBVjCSItUjcJt2Qxf9mmbTmKb-XuybsqoARbVXZleh50zDdZ7Xi5C0Dj7_jSHDnvEohshSqxV09IbLR9fSDrhMQw4BzWogtDwXqcqDHoVgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور ترامپ در مورد ایران:
من آن را یک درگیری می‌نامم. ما با جمهوری اسلامی ایران درگیری داریم.
آنها آنقدر ضربه می‌خورند تا معامله کنند، اما من می‌گویم که آنها آماده معامله نیستند.
آنها آماهده نیستند چون بعد زیرش میزنند. اما خیلی زود آماده خواهند شد.
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/19366" target="_blank">📅 23:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19365">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">روزنامه سان : بریتانیا کارکنان سفارت خود در تهران را از ایران خارج کرده است
؛ اما نکته مهم این است که فعلاً گزارش‌ها از
تخلیه کارکنان دیپلماتیک (staff withdrawal)
صحبت می‌کنند، نه اینکه ساختمان سفارت تخلیه یا بسته شده باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19365" target="_blank">📅 23:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19364">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کانال ۱۲ اسرائیل: بریتانیا در پی وخامت اوضاع، در حال تخلیه شهروندانش از ایرانه.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19364" target="_blank">📅 23:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19363">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/243d08a582.mp4?token=ByUfhN2qEqANTj26jNERvyya3PCU4Gh5dEVK4djAEeJO8IlySYq0RFHr1xwpcEWvvV3LWN3ieEBAIPeNG8pkyGqauDAtRiHVfqVaWxl_bn6X6oZZGVwP50vHudbmC1JH1CRVxlm_oaRWvU9UE37z_7sikXp06_7bFFqAm6eBPEOVbwQwUuGd_HgDTdUdpfnTLaTDfaawk5YhjLtQj6_ooJmMLRxuRX260QDOYokqAWAVEZtdRRonLYi9ocKS9ixS0kx94Zk9EIwbaBtZoeAaY-n55sg2ZW0OJxlUCoHAOugSXo_KcjCwVLNkuMhpr53JnOYz1fxPLAV9nmmXBvbIZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/243d08a582.mp4?token=ByUfhN2qEqANTj26jNERvyya3PCU4Gh5dEVK4djAEeJO8IlySYq0RFHr1xwpcEWvvV3LWN3ieEBAIPeNG8pkyGqauDAtRiHVfqVaWxl_bn6X6oZZGVwP50vHudbmC1JH1CRVxlm_oaRWvU9UE37z_7sikXp06_7bFFqAm6eBPEOVbwQwUuGd_HgDTdUdpfnTLaTDfaawk5YhjLtQj6_ooJmMLRxuRX260QDOYokqAWAVEZtdRRonLYi9ocKS9ixS0kx94Zk9EIwbaBtZoeAaY-n55sg2ZW0OJxlUCoHAOugSXo_KcjCwVLNkuMhpr53JnOYz1fxPLAV9nmmXBvbIZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما به تنگه‌ها نیازی نداریم. ما به هیچ چیز دیگری نیاز نداریم.
ما به تنگه هرمز نیازی نداریم , ما این کار را می‌کنیم ,چون باید انجامش دهیم.
ما نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19363" target="_blank">📅 23:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19362">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/273ed05dc7.mp4?token=lH8Vcvy0Rl3LaOaGXHIUs9y5Zzx21YapCBTX8iMJxxjbz7rJnG3_dBxdt4PUzQH9foBBWY8DKqQzAlzx88l43i_ZzKwYS6zQIllYL36jaszLnnB24_J-RFyDyNqcbQlye02uquHORShRz6aZFRju04PqvRvz8F5S5eJcDpuzRs1cVawo_x4SU7qtrTTs4ir0EeK18Xpy7OyfBhwhUtWUIn7I7ZEvsLAIuSAUFfM7rvzzs2fpwPCKf5d-zCJnQJBQGYN_A5ynM8_R2a4DLJJ_wiU_cgOLNdHNdPik3iv1vxDbHUEGZZApwXosG-n_HCW0cMCxdDV5Mfktd7qPeSJ7OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/273ed05dc7.mp4?token=lH8Vcvy0Rl3LaOaGXHIUs9y5Zzx21YapCBTX8iMJxxjbz7rJnG3_dBxdt4PUzQH9foBBWY8DKqQzAlzx88l43i_ZzKwYS6zQIllYL36jaszLnnB24_J-RFyDyNqcbQlye02uquHORShRz6aZFRju04PqvRvz8F5S5eJcDpuzRs1cVawo_x4SU7qtrTTs4ir0EeK18Xpy7OyfBhwhUtWUIn7I7ZEvsLAIuSAUFfM7rvzzs2fpwPCKf5d-zCJnQJBQGYN_A5ynM8_R2a4DLJJ_wiU_cgOLNdHNdPik3iv1vxDbHUEGZZApwXosG-n_HCW0cMCxdDV5Mfktd7qPeSJ7OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیستم دفاع هوایی مخوف c-ram در کنسولگری ایالات متحده در اربیل عراق فعال شد. @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19362" target="_blank">📅 23:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19361">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : دروازه های جهنم   پیشبینی خودتون رو برام کامنت کنید کارای اداریش رو هم انجام بدید  https://www.instagram.com/reel/DbGvd4YRk8m/?igsh=cTlmeHd6bGVvYnM4</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19361" target="_blank">📅 22:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19360">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سیستم دفاع هوایی مخوف c-ram در کنسولگری ایالات متحده در اربیل عراق فعال شد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19360" target="_blank">📅 22:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19359">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">به گزارش خبرگزاری رویترز پهپادهای رژیم ایران تاسیسات سازمان سیا را در منطقه مورد هدف قرار دادن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19359" target="_blank">📅 22:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19358">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">۶ انفجار پهپادی اربیل عراق
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19358" target="_blank">📅 22:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19357">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs3Up50kkOQ_U1j9vwecvw1iMLkD4IMtzgVcGfgWZBCkiusG7IcwXlL9myZflKTl350yy0w9uwjpy-t8n0hQLKXCWHk39rTPMWtSs4gaauvdsF5QgHJBQHA3m5vYCAumL0O62k2D5YavLMTc0owV6yZHdfO-RQXTzejGyASmwC4sxMv8szMDA1tuu7uFj6i9dF5RD8FartPi2zcQt2iULxRDpdvlNVAHQfKjhi8vBfmtRfZlnqe996P7I90xKHX6sYfmH0pDvtqQXCGzQKA9U1Aho6gL0crDE5sIcOtND4Nm5eK_xKCL8GyobNMTs0d8rcJ9PPc2r7AmTWNORx4-zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : دروازه های جهنم
پیشبینی خودتون رو برام کامنت کنید کارای اداریش رو هم انجام بدید
https://www.instagram.com/reel/DbGvd4YRk8m/?igsh=cTlmeHd6bGVvYnM4</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19357" target="_blank">📅 22:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19356">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سیریک صدای توافق میاد
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19356" target="_blank">📅 22:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19355">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19355" target="_blank">📅 21:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19354">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سناتور در‌ جلسه سنا
:
مردم دیگر نمی‌دانند کدام روایت درباره جنگ را باور کنند؛ چون یک بار گفته می‌شود جنگ تمام شده و بار دیگر گفته می‌شود تمام نشده است. یک بار گفته می‌شود ظرف دو هفته اتفاقی می‌افتد و بعد می‌گویند نه، این‌طور نیست. یک بار می‌گویند دیگر موشکی نداریم و بار دیگر می‌گویند هنوز موشک داریم.
همین سردرگمی باعث شده بسیاری از مردم گیج، نگران و تحت فشار باشند و این جنگ را به‌شدت نامحبوب بدانند. چون تصمیم‌هایی را که رئیس‌جمهور می‌گیرد درک نمی‌کنند و با آن تصمیم‌ها موافق نیستند
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/19354" target="_blank">📅 21:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19353">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سد مجید گشاد زن
فرمانده هوافضا تروریستی سپاه:
به پل ها و نیروگاههای ما تعرض شود خاموشی برق متحدان و میزبانان کودک کشان قطعی است.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19353" target="_blank">📅 21:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19352">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بیانیه فرماندهی نیروی دریایی تروریست سپاه(همون چرکه):
ورودی و خروجی تنگه هرمز مشخص و در کنترل قطعی ماست. مسیرهای جایگزین ، نا ایمن و خطرناک است اخطار می دهیم استفاده نشود که تبعات سنگین و غیر قابل جبرانی خواهد داشت
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19352" target="_blank">📅 21:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19351">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">صدای انفجار‌ در کویت
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19351" target="_blank">📅 21:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19350">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5jikkeNd3bjJkDyQfnCJncSHXdsIa5GD51LBJIitQEvQLurhR4qFfIewfLuvy5DEJJspioAWs9yr_RN0wO8N-QbVClTJh5tTuIpMc_stIm-ElGvsAOWMd6Mvk7fEcJsLZhR1fSVQ-f1BtowGR0k0C2PCFtGdvtSMo3xL3bsy7vkRSkh9Wf2v0tnb2cGBVe1J5IvzCS3FRMx8Hu3-oaAFI_6QXTpaoBDrW2yByevg5bD8jJ5emKcg218eVA_mfJP7IG2q3XnjEIxu_9nmv4tBEzE4O2V0MDR4MuFjhILRdVuRNY8XoW5eUMufw-F0xgUt5XCLLgyB4AjkbAHREBz0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبری که ترامپ بازنشرکرد
:
به سنتکام دستور داد شده دروازه‌های جهنم را به ایران باز کنن بعد از کشته شدن نیروهای آمریکایی
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/19350" target="_blank">📅 21:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19349">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19349" target="_blank">📅 21:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19348">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">موج حمله موشکی جدید رژیم
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19348" target="_blank">📅 21:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19347">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خبرگزاری کان: اسرائیل از سوی ایالات متحده آمریکا مطلع شده است که این کشور قصد دارد حملات خود به ایران را تشدید کند و در روزهای آینده، و برای اولین بار در این تشدید، حملاتی را با استفاده از بمب‌افکن‌های سنگین علیه ایران انجام دهد
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19347" target="_blank">📅 20:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19346">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlJmfll3V3nCvhzK9nlTwJOBNqL26W3yaq0DbO3hPM8oNLnHAfHLbQ6ZhhaedCaaT56EaYwMYt4mG2hQl-DOpfs5UNRIBK39z04L9Xt_7SV4eHf-4tMr1KueFyJfghCRPu8vA--iXWRFXZenofmw3h-6YlsY_cmu1-4Q1uDCBRfBy5cTzmHHS61op9FlXqRZR0832MTXMxm5lvY_OBw1N_6yD4oCJ8IHhMBsesamBthG6elmBbSYNVclXHiMd9HuNL43dP6H9043laIQoD0fFa8Rn-fp_VoegfpALG1F5zDs7hbh_JlFhyn8MyFop1xIv0DYPGwQ_34NVKe-CichEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‎سنتکام:نیروهای ایالات متحده که محاصره دریایی علیه ایران را در دریای عرب اجرا می‌کنند، طبق اعلام سنتکام (فرماندهی مرکزی ایالات متحده) تا تاریخ ۲۲ ژوئیه، ۹ فروند کشتی تجاری را تغییر مسیر داده و ۱ فروند را از کار انداخته‌اند. ناو یواس‌اس مایکل مورفی (DDG 112) عملیات را زیر نظر دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19346" target="_blank">📅 20:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19345">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19345" target="_blank">📅 20:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19344">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حمله موشکی پهپادی رژیم به اربیل عراق
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19344" target="_blank">📅 20:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19343">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">علی‌رغم هشدارهای ایران ،بلغارستان اجازه استقرار هواپیماهای آمریکایی در خاک خود را می‌دهد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19343" target="_blank">📅 20:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19342">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d436f581ea.mp4?token=NvFVuiRk6E_jK8pJL8ewUQmk2qJXpmqSUi_WFnGz3Tij3gYliL7MBb_W3Z4IgqQVmuCLYaehNs2R2XkqKYTfeu_aEK-CFbNdrikEQCNYi1H7ryiuZNIS2Ba6UTdOu5_YjeRoPGWbRbpY0ff-T8QRhxjjPo_9C-mziDi0ZCUNtDFx9pjGqv18qAXMDkckFHbGdVdwiGAd1hj8BT6CEKB-RM6InWPqbW48p9KLSGH3C2FOMREd8GZ1RtR2kY7o4qvSPN2XV08zIA8hcDrfb6uq9nYgYIdZMl-bXBStsXTBDALsMsTIHMLwH3PIVDbjUVI6shqKWS8wQ5FJD1pg7dzeFz7IovYnwCDBms9KeQVVVzy-zpdlEZfFf64HUg1Nte0ZgznW928-ckGKWbeaIFakK1CRyRPY2hxW-gfTXbLOk_YbLbMdhrrpFKI5322aVKqzbetSqKjI7S2Av6BGzoXgJQUV0j1xMMPUkIs7NXfpWlsF_1C6wIeYz0kHWYejolKAIkpYdbW-U5gSCPL1wJCd8zJK1bx3NmCpwuPJ9sjoyV5dGu_nX8bMMTWflgUsnOIx7OkXEs9WYQKj1-EmbWajhbuvGspph3ZVrVoOwKpmGGsEhTf6QmHLUENly8gPHtWkqcrymKabhV7Uy_tHxmfZ44LC00Ln5bxUZ0cFG9oiTIU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d436f581ea.mp4?token=NvFVuiRk6E_jK8pJL8ewUQmk2qJXpmqSUi_WFnGz3Tij3gYliL7MBb_W3Z4IgqQVmuCLYaehNs2R2XkqKYTfeu_aEK-CFbNdrikEQCNYi1H7ryiuZNIS2Ba6UTdOu5_YjeRoPGWbRbpY0ff-T8QRhxjjPo_9C-mziDi0ZCUNtDFx9pjGqv18qAXMDkckFHbGdVdwiGAd1hj8BT6CEKB-RM6InWPqbW48p9KLSGH3C2FOMREd8GZ1RtR2kY7o4qvSPN2XV08zIA8hcDrfb6uq9nYgYIdZMl-bXBStsXTBDALsMsTIHMLwH3PIVDbjUVI6shqKWS8wQ5FJD1pg7dzeFz7IovYnwCDBms9KeQVVVzy-zpdlEZfFf64HUg1Nte0ZgznW928-ckGKWbeaIFakK1CRyRPY2hxW-gfTXbLOk_YbLbMdhrrpFKI5322aVKqzbetSqKjI7S2Av6BGzoXgJQUV0j1xMMPUkIs7NXfpWlsF_1C6wIeYz0kHWYejolKAIkpYdbW-U5gSCPL1wJCd8zJK1bx3NmCpwuPJ9sjoyV5dGu_nX8bMMTWflgUsnOIx7OkXEs9WYQKj1-EmbWajhbuvGspph3ZVrVoOwKpmGGsEhTf6QmHLUENly8gPHtWkqcrymKabhV7Uy_tHxmfZ44LC00Ln5bxUZ0cFG9oiTIU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو در پیامی به مناسبت نهم آو گفت اسرائیل طی سه سال گذشته با حفظ وحدت داخلی از بحران عبور کرده و به جای جنگ داخلی، در برابر دشمنان متحد شده است. او تأکید کرد که این کشور با وجود ادامه چالش‌ها به دستاوردهای مهمی رسیده و مأموریت هنوز به پایان نرسیده است. وی اعلام کرد برای تقویت وحدت داخلی، در پی تشکیل یک دولت ملی فراگیر و باثبات خواهد بود که امنیت و آینده اسرائیل را تضمین کند و افزود اختلافات انتخاباتی نباید مانع حفظ انسجام جامعه شود. او همچنین با اشاره به تجربه‌های اخیر گفت مردم اسرائیل در لحظات سخت نشان داده‌اند که بیش از آنچه تصور می‌شود متحد هستند
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19342" target="_blank">📅 20:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19341">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ارتش آمریکا در حال انجام عملیات تخلیه تمام هواپیماهای سوخت رسان و ترابری خود از قطر می‌باشد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19341" target="_blank">📅 20:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19340">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کانال ۱۴ : سپاه پاسداران ایران، ایالات متحده را به حمله تروریستی «به سبک یازده سپتامبر» تهدید می‌کند.
خبرگزاری تسنیم وابسته به دولت گزارش می‌دهد که سپاه پاسداران هشدار داده است: «اگر جنگ ادامه یابد، ما عملیات پشیمان‌کننده‌ای انجام خواهیم داد که منجر به عزای ملی در آمریکا خواهد شد.»
آخرین باری که ایالات متحده برای یک حمله عزای ملی اعلام کرد، یازده سپتامبر بود.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19340" target="_blank">📅 20:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19339">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">منابع جمهوری اسلامی : رژیم ایران معتقده مهلت‌های آتش‌بس چیزی جز فرصت‌هایی برای تجدید قوا، سازماندهی نیروها و بازگشت دوباره به جنگ نیست و نمیخواد در چنین چرخه‌ای گرفتار بشه.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19339" target="_blank">📅 19:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19338">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خبرگزاری رویترز: شرکت هواپیمایی کی‌ال‌ام هلند اعلام کرد تعلیق پروازهای به کشورهای خلیج فارس را تا ۶ سپتامبر تمدید خواهد کرد.
این اقدام به دلیل وضعیت بحرانی در غرب آسیا اتخاذ شده است
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19338" target="_blank">📅 19:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19337">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اکسیوس
:
شرط اصلی ترامپ برای برقراری آتش‌بس این است که ایران حملات علیه کشتی‌ها را متوقف کند و تنگه هرمز را دوباره برای کشتیرانی باز کند
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19337" target="_blank">📅 19:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19336">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رسانه های عبری : آمادگی در اسرائیل ، احتمال درگیری با ایران در آخر هفته @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19336" target="_blank">📅 18:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19335">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خبرنگار الجزیره:ایران ایده آتش بس موقت با آمریکا را رد کرد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19335" target="_blank">📅 18:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19334">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رسانه های عبری : آمادگی در اسرائیل ، احتمال درگیری با ایران در آخر هفته
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19334" target="_blank">📅 18:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19333">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJzmuPadFzxf0s7cUP5DgHiboMjgsu3YjmmYABy_MM8aArvMc2wI3YhynEMdwUyIyybOQfMDbGsOYW-x97UcQO8_wnEn4RfeOMpi-ZsiYg7IkgtlgnvdBATUlacAkewmev1Piqgpv5HOF0BElWTqldt57_2uJHJRNZh_m637BGKwaz7X0ihrC-8Ki7D-9nc8uAYOFmZWWWsaVg_n3wl49KBLMWgCHCfxDjm9l6c0XL0uDHVXQy9-PLBqx4fFj0hPnu6Ws8OgnD8dO0y3qGLoErsgkxsJX8BVbI0DJYYJ9VUcou1fYIEYf5GSR8OsNSkulkurJ11xyB8g8mjUXOR0VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از خوشحالی عرزشی ها از مرگ سرباز آمریکایی در هنگام خنثی سازی خدا به کمر آنها ضربه ای زد و جان دو نفر سپاهی را به همان شکل گرفت سردار احمد احمدی و سرهنگ دوم پاسدار مصطفی جمشیدیان از نیروهای واحد تخریب لشکر ۸ زرهی نجف اشرف، در هنگام چک و خنثی سازی کشته شدند
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19333" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19332">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gfze95sk5k2A5MDQRKbBhOrZryCfHhH-_zYcSu7R1EcnhHhEpfl46Du9ss6dzJAIOC1SzXgk6fd5DnhnPcQ55cK3gulLRxC87Q0cZMluUV6BVzSMDBsuNsp_ae_njusxG9VEAPoCCeAoN_VRtYXbOktzD1EZkYRtUaZ-nopu4r9nE02VrcID7hJ0xMvJeopQfmGVoovMJJaWUK7ygKMLrkQX7MKKje8TftL1nmSw-_fgpN9f0jsl1IFd539OSSeLIyHzhr5CJ37HVW_JKZICwfCICRjt_cF54xOfIss04p4qAqHjNusUHO7x0JhaIDryBg0obitfxNWoXFlyH4kB0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک اسکادران جنگنده پنهانکار F-35 با عبور از اقیانوس، توسط دو سوختستان استقبال و کمی دیگر در انگلستان به فرود میآیند. یکی از آنها، احتمالا به علت نقص فنی یا برای نشان دادن خود به جهان و تمرین ، آلارم فرود اضطراری روشن کرده است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19332" target="_blank">📅 18:08 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
