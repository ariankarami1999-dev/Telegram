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
<img src="https://cdn4.telesco.pe/file/Uq2P7yqrbh__jOzt-ndwWLWjF9Zlu94hTsHp3oDaDl4nLIJA6_IyVweLcBQu8s78gN2T7qTa5q1YS5m_39V00bsyDVQO6Mcb5dFUCJZ3GGU5cY4APi7scDhCEdPZMVx3J-do8IXwhopqQg3wyalRPpOw9O5YD8kRrX_zHrfzCgpWAbEehI3GDwAXhYEi4VR1SXvfYLmxIJ1BHlZplc8CfQy-rF1Z4V3_XvHunjhjYy_7eWovMf_ok3Gurm1Qn0-NuwPvg_arfEpBWIz5mEpB4VKqvr720W9UlLgJrqTNhMkLaF-N7AB7bHtPl0SXy0RfkJ3_k04AvSuB3mVAny_-EQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 20:25:50</div>
<hr>

<div class="tg-post" id="msg-437740">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da32a150af.mp4?token=qYr1p0zdR5eGO4y-bSRIw2Qf1ywGBq2nn32OgVSdje7VBxHSVXhHlps07HC3kVGzwbyo8duWErur_DLaZrA1HEC61NnucP56hcLoCdAnH3SZzY26ztFkqEHzXth6AlFwGMlsaQswtfzBPr7oD2-bGJlCzpt7RXKkJSSam19RpBFLQssBoh21V2JYDKLguGuau3pY8NBbWHVwmJhY2z3P5Lp6TDY__0Fdyz5yMhfMwyk4zCa_YtkzyrPd0LGXa21wuI8lvpnsuzofS6G9jXcddEvd1FcoJwRRrk1bbXiMGhA2kvYn-BjjVrL-s-nbMR7kHYgYJU-9o01vbe0ehdUmUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da32a150af.mp4?token=qYr1p0zdR5eGO4y-bSRIw2Qf1ywGBq2nn32OgVSdje7VBxHSVXhHlps07HC3kVGzwbyo8duWErur_DLaZrA1HEC61NnucP56hcLoCdAnH3SZzY26ztFkqEHzXth6AlFwGMlsaQswtfzBPr7oD2-bGJlCzpt7RXKkJSSam19RpBFLQssBoh21V2JYDKLguGuau3pY8NBbWHVwmJhY2z3P5Lp6TDY__0Fdyz5yMhfMwyk4zCa_YtkzyrPd0LGXa21wuI8lvpnsuzofS6G9jXcddEvd1FcoJwRRrk1bbXiMGhA2kvYn-BjjVrL-s-nbMR7kHYgYJU-9o01vbe0ehdUmUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انتظامی: من از تعداد، پراکندگی و تنوع قدرت‌مان [تا قبل از جنگ] اطلاعی نداشتم؛ حجم بازدارندگی توان موشکی ما بسیار بالاست.  @Farsna</div>
<div class="tg-footer">👁️ 481 · <a href="https://t.me/farsna/437740" target="_blank">📅 20:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437738">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hC6SB8cqBrfsxF6VmOOyUC-mQ8R8ckqSqKCBtj7sp-p9VaVE93zHJ8PKzSEbUeCqWft2N-6f4BpEOD75eSnNMFsINkykBIJpsk16UwQR6YGhV5CVF3gepaFmZqJ-FUN0xi5br0GtMJQtya4cgXHNfLyxTcxwCA7icAUDNGI5T6PCkehTBhLRGUMg2NGPrxCs_8mMsv9S82PMR-PVIKuNXs52hRlXVE9FJ6WpxE_zHMFAWUCafI7zDQemsdTWLGrtv4tgcbMv_lLckYwVL5GIF9E56GpXv3USJhe4-U-3jnlyrfXYL2an37L6nfeBUmuIKLBMpJQ1fP56ChypxziWdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ راهکار برای کم‌کردن رقم قبض برق
🔹
معاون وزیر نیرو: مشترکانی که حداقل ۱۰ درصد از سال گذشته کمتر برق مصرف کنند، تا ۳۰ درصد در قبض برق تشویق می‌شوند.
🔹
همچنین مشترکان خانگی که نیروگاه ۵ کیلوواتی خورشیدی احداث کنند ۲۰ درصد از قبض آنها کمتر می‌شود و اگر تجهیزات ذخیره‌سازی هم نصب کنند، ۳۰ تخفیف می‌گیرند.
@Farsna
_
Link</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/farsna/437738" target="_blank">📅 20:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437737">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f4a3d2c7.mp4?token=MV6Yx4_uGBbcQK3LDewA5hsdhhQvYwBLPXeRwVRhAC1Dzc515XxS6dYGsmDIpTGZz2-d8LPfX3ohbWAlpH3FKT_trulNNOjT8bSrmHoWav5nzjXUHSxaR9iW4QXRCvdpOHnDyzzPYi8OgsgikDhm1TFAXD53BoxIIhji3rP3YUiKs6EAM2dJveejc67m4yl0pXQOc0jF5AccEkQJ6k7mInoBcJ9C65T22jPQ2oCZULUGyPT3VcwrQygGWBjw2h-dnsgo3J2YKPH-Yhzk7rSNBiOZhcTv8QHPwSqWNlKUSaOUdRwl6APUFiAABR64OUEjBZK39rKGNrdV2G4-5kMS8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f4a3d2c7.mp4?token=MV6Yx4_uGBbcQK3LDewA5hsdhhQvYwBLPXeRwVRhAC1Dzc515XxS6dYGsmDIpTGZz2-d8LPfX3ohbWAlpH3FKT_trulNNOjT8bSrmHoWav5nzjXUHSxaR9iW4QXRCvdpOHnDyzzPYi8OgsgikDhm1TFAXD53BoxIIhji3rP3YUiKs6EAM2dJveejc67m4yl0pXQOc0jF5AccEkQJ6k7mInoBcJ9C65T22jPQ2oCZULUGyPT3VcwrQygGWBjw2h-dnsgo3J2YKPH-Yhzk7rSNBiOZhcTv8QHPwSqWNlKUSaOUdRwl6APUFiAABR64OUEjBZK39rKGNrdV2G4-5kMS8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
اسپرسو با حسین انتظامی  گفت‌و‌گو با حسین انتظامی، معاون وزیر ارشاد، را هم‌اکنون در سایت، ایتا، روبیکا و تلگرام فارس ببینید. @Farsna</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/farsna/437737" target="_blank">📅 20:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437736">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vetPdFzszyNiUg-xmfJI1Q6AfSxCNusMPNBfqtk5TF1U29x-lHepnFQL1YDOxtYg06zbA7iPJlPz8-6lvfhXTV1tInuqGfIxg-b-59TVysKHYi9Sd3YyboKKzBHt-VPkx3q39kWK68oyxtSO2UfWxNBEi5r3eMmFybpxGGTahOZXdRkXMe0rQy7FjPjoe8FcJpKfg-5XqKkEtlZujcdF2NPKmXJ67e4tJgtu5lqhenuyTG1njhJkgMaVMbnBcsIUMQ4miGGpOKu55w5N3amhySOrhOUsHIJv62jZjZUGa-OgqocK_j0oHepjhOnXEakKJdXTPS4hh0MXqqQep3Ke1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلاکت یک فرماندهٔ صهیونیست در حملهٔ پهپادی حزب‌الله
🔹
رسانه‌های صهیونیستی: در جریان حملهٔ پهپادی حزب الله به جنوب لبنان، یک خلبان جنگندهٔ نیروی هوایی اسرائیل که فرماندهٔ سابق در این رژیم بوده کشته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/farsna/437736" target="_blank">📅 20:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437735">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb10eda20a.mp4?token=Rp2hzR0OXsxfMyyYBwwZ3z-q0tl9FqJlkQQLtxDTcGLFPuc_Ce9OdraCh-u5SriBQcYBzItmwYY1qSKvdRcwePFy5c32g_kMUQ1JoqP0zEYd8E7007IjOjZPsG0kokW_8cXebzWk80K5PzF2wGbpruAA06-S1vQjmucxUcPR4BJMvdDVu8s8FdrUEe15S_tqakBdlsS6Crqc-FqOTU0selNKMP5-qIrT19KR4GLt9cGzyCJFOvZyfio56xoeFOmlXGV1oGK_cPYeASM0VwhKYPqELDU9zpNPInytmic4P4nzBhUKd3EzUsQDygLAjmPcw6bAZthPkVNL2Nw4utLLkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb10eda20a.mp4?token=Rp2hzR0OXsxfMyyYBwwZ3z-q0tl9FqJlkQQLtxDTcGLFPuc_Ce9OdraCh-u5SriBQcYBzItmwYY1qSKvdRcwePFy5c32g_kMUQ1JoqP0zEYd8E7007IjOjZPsG0kokW_8cXebzWk80K5PzF2wGbpruAA06-S1vQjmucxUcPR4BJMvdDVu8s8FdrUEe15S_tqakBdlsS6Crqc-FqOTU0selNKMP5-qIrT19KR4GLt9cGzyCJFOvZyfio56xoeFOmlXGV1oGK_cPYeASM0VwhKYPqELDU9zpNPInytmic4P4nzBhUKd3EzUsQDygLAjmPcw6bAZthPkVNL2Nw4utLLkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان خودرویی اردبیلی‌ها به مناسبت سالروز فتح خرمشهر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/farsna/437735" target="_blank">📅 20:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437734">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: این حق مردم لبنان است که به خیابان‌ها بیایند و دولت را ساقط کنند
🔹
این حق مسلم ملت است که به نشانهٔ اعتراض به خیابان‌ها بیایند و دولت را در مواجهه با پروژه آمریکایی-اسرائیلی که نهادهای ما را هدف قرار داده است، ساقط کنند.
🔹
ما از بزرگ‌ترین…</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/farsna/437734" target="_blank">📅 19:58 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437732">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: هدف دشمن از این همه کشتار و ویرانی، به زانودرآوردن ماست؛ اما ما هرگز به زانو در نخواهیم آمد
🔹
ما در میدان نبرد باقی خواهیم ماند و سربلند از این جنگ خارج خواهیم شد.
🔹
خانه‌ها را بازسازی خواهیم کرد، مردم ما به دیار خود بازخواهند گشت، دشمن…</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/farsna/437732" target="_blank">📅 19:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437731">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: در حال حاضر هیچ‌گونه حاکمیت سیاسی در لبنان وجود ندارد و کشور زیر سایهٔ قیمومیت آمریکا قرار گرفته است
🔹
مذاکرات مستقیم با اسرائیل مردود است و این اقدام، یک امتیاز و دستاورد خالص برای «اسرائیل» است.
🔹
مذاکرات مستقیم را رها کنید، آنچه را…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/farsna/437731" target="_blank">📅 19:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437730">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: پهپادهای مقاومت به تعقیب سربازان صهیونیست ادامه خواهند داد
🔹
اگر تصویربرداری پهپادها نبود، طرف «اسرائیلی» هرگز به این خسارت‌ها اعتراف نمی‌کرد.
🔹
رویدادهای جاری در جنوب لبنان، آغاز زوال و نابودی «اسرائیل» است. @Farsna</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/farsna/437730" target="_blank">📅 19:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437729">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSRi7PuwkVD3lZmBcedLPVeuiTVKPsF_q5xD3l7L4dB_gtkxJCMLROPEKDSw2hPbuKNfaHybfy-AeJiuyb1RwVtjNvzDrZ1B9ndamGKRt5KxvWyTxNXTAljDrS1vxzEeLwEqtKLaQpIXFDhehPuctfZURkwsIuXU01XZW9feLSmjhY8547YyMlLE4Z0m8fOzxLgUvjEKrlgCQgDE-5lB5OVZCsE09zxLHF769_EN18SE9ePa4lBjqqkkEVctP-7rDmdMKZXg80KTUqKqgR3ku1qKS08ac6-dNJXKh4GYtwEEcJ5waarIeaGiPVXJZ31BTUpro2Uu-gwqFbxqgJ-eyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تابستان داغ در جایگاه‌های سوخت آمریکا
🔹
گزبادی، تارنمای آنلاین قیمت سوخت در آمریکا پیش‌بینی کرده امسال آمریکایی‌ها گران‌ترین قیمت تابستانه بنزین در سال‌های اخیر را تجربه خواهند کرد.
🔹
رئیس این تارنما می‌گوید به‌خاطر بسته‌ماندن تنگه هرمز، میانگین قیمت بنزین به رکورد ۴.۸۰ دلار در هر گالن خواهد رسید.
🔹
متوسط قیمت بنزین امروز در کم‌تر از یک‌ماه‌مانده به تابستان، به ۴.۵۱ دلار در هر گالن رسیده.
🔸
بنزین ارزان، یکی از وعده‌هایذانتخاباتی پرتکرار ترامپ بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/farsna/437729" target="_blank">📅 19:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437728">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: اگر دولت لبنان از تامین و حفظ حاکمیت کشور عاجز است، پس باید کنار برود. @Farsna</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/farsna/437728" target="_blank">📅 19:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437727">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: سلاح تا زمانی که دولت لبنان بتواند به وظایف و تکالیف خود عمل کند، در دستان ما باقی خواهد ماند
🔹
خلع سلاح مقاومت، به معنای سلب قدرت دفاعی لبنان و زمینه‌سازی برای نابودی آن است و این چیزی است که ما هرگز نمی‌توانیم بپذیریم.
🔹
ما خواهان توقف…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/farsna/437727" target="_blank">📅 19:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437726">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: دولت لبنان به ما می‌گوید یاری‌مان کنید تا شما را خلع سلاح کنیم، تا پس از آن «اسرائیل» وارد شود، شما را به قتل برساند و ملتتان را آواره کند! @Farsna</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/farsna/437726" target="_blank">📅 19:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437725">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‌‌
🔴
دبیرکل حزب‌الله: مقاومت از سرزمین و شرف خود دفاع خواهد کرد و با هرکسی که در برابر ما بایستد، همان‌گونه برخورد خواهیم کرد که با «اسرائیل» روبه‌رو می‌شویم. @Farsna</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/farsna/437725" target="_blank">📅 19:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437724">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‌ ‌
🔴
دبیرکل حزب‌الله: تحریم‌های آمریکا هرگز ما را تضعیف نخواهد کرد؛ اگر آمریکا بیش از این خوی وحشی‌گری به خود بگیرد، دیگر چیزی برایش در لبنان باقی نخواهد ماند. @Farsna</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/farsna/437724" target="_blank">📅 19:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437723">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: از دولت لبنان می‌خواهم که از تصمیم خود مبنی بر انحصار سلاح در دست دولت عقب‌نشینی کند تا بتواند در کنار ملت خود بماند.
🔹
ما از دولت لبنان نمی‌خواهیم که به مقابله با پروژهٔ آمریکایی-اسرائیلی برخیزد، اما دولت نباید در برابر ملت خود بایستد.…</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/farsna/437723" target="_blank">📅 19:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437722">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gm9YDYMf8EEkqfsv9rpZsGlh8Pv2uCCfp6i8mavf_Bxk2ibWQXSRmzorLNI41NCVWS5yieaCZIOGiDsk1zS-3RZYsjheNSm7URAV4cEW-wrHLG3daCR66jRoMXLVWm5GC6v8kjcJW55URKsmtT9T-SDxhQiqMfDTClCHZzwFCtIAJ0vwhBUEboPW9mzZTCfLVDL4Bx1CMwVn-Twjl1sobZk0fXJP_AzDjeJkUa6qK7KEnn0EwE4cnA68v48KvXm2dMwjx_4nE5DR_QcFO6RDV3QpxNMIfLCQTJE98_H1yUhhfb3eWmCAwHnNNsXYYrexIeeZSKSdpNj4G_6hzKWG1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۴ کشور اسلامی افتتاح سفارت سومالی‌لند در قدس اشغالی را محکوم کردند
🔹
وزرای خارجه مصر، عربستان، قطر، اردن، ترکیه، پاکستان، اندونزی، جیبوتی، سومالی، عمان، سودان، یمن، لبنان و موریتانی شدیدا اقدام غیرقانونی و مردود منطقه جدایی‌طلب «سومالی‌لند» در افتتاح سفارت در شهر قدس اشغالی را محکوم کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/farsna/437722" target="_blank">📅 19:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437721">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: از دولت لبنان می‌خواهم که از تصمیم خود مبنی بر انحصار سلاح در دست دولت عقب‌نشینی کند تا بتواند در کنار ملت خود بماند.
🔹
ما از دولت لبنان نمی‌خواهیم که به مقابله با پروژهٔ آمریکایی-اسرائیلی برخیزد، اما دولت نباید در برابر ملت خود بایستد.
@Farsna</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/farsna/437721" target="_blank">📅 19:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437720">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdtvX03dtC4-ry05l-zN0yvBc_ImF3J8egiN16Mbjq272Og9dYBuv_V5Wt9-RuxVWmJ8hSgl-b9mfcdXYmLyC33WkdVNNrwDxwhC5NXW5Az6ckX3LsO7R2NTsgp2xtrx4TGnuwOrLhH77Fw1mQ0HW_xjd-yubFCk4TkNfD4BplbTWsS5K5mFO0-J5Q5gnXptnLLs2HmyPuo87-wdwEGO0sQGmy8McAMmqK37ot2brUPvfod-R60W3sGC-fwpbYGqkuQEC-a-Wqn0IVf-aUIjlz_D9n-hJ478gg9fohrgrbmou8ulEgdBRdjmhM6P-FRCWt2hQ_3D5NhbbPvJ0aNonA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
اسپرسو با حسین انتظامی
گفت‌و‌گو با حسین انتظامی، معاون وزیر ارشاد، را هم‌اکنون در
سایت
،
ایتا،
روبیکا
و
تلگرام
فارس ببینید.
@Farsna</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/farsna/437720" target="_blank">📅 19:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437719">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پیامک انتخاباتی جنجالی در مجلس؛ وعدۀ خانه در ازای رأی به نایب‌رئیسی
🔹
در آستانه برگزاری انتخابات سال سوم هیأت‌رئیسه مجلس شورای اسلامی، انتشار یک پیامک انتخاباتی از سوی یکی از نامزدهای نایب‌رئیسی مجلس، حاشیه‌ساز شد.
🔹
امیرحسین ثابتی، نماینده مردم تهران در مجلس، با انتشار تصویری از پیامک علیرضا منادی، نماینده تبریز و از نامزدهای نایب‌رئیسی مجلس، به محتوای آن اعتراض کرد.
🔹
براساس متن منتشرشده، منادی در پیامکی خطاب به نمایندگان مجلس وعده داده است که در صورت انتخاب به‌عنوان نایب‌رئیس مجلس، موضوع تأمین مسکن نمایندگان دوره دوازدهم را پیگیری کرده و آنان را صاحب خانه خواهد کرد.
🔹
علیرضا منادی یکی از ۷ نامزد انتخابات نایب‌رئیسی مجلس در انتخابات فرداست؛ انتخاباتی که همزمان با برگزاری رأی‌گیری برای ترکیب جدید هیأت‌رئیسه در سال سوم مجلس دوازدهم برگزار می‌شود.
🔹
انتشار این پیامک واکنش‌هایی را در میان برخی نمایندگان به دنبال داشته است. علاوه بر ثابتی، چند نماینده دیگر نیز در فضای مجازی نسبت به این اقدام انتقاد کرده‌اند.
🔹
همچنین دو نماینده مجلس در گفت‌وگو با خبرنگار پارلمانی فارس اعلام کردند که در گروه‌های مجازی نمایندگان، فضای انتقادی تندی علیه این پیامک شکل گرفته و برخی نمایندگان نسبت به طرح چنین وعده‌هایی در رقابت‌های داخلی مجلس انتقاد کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/farsna/437719" target="_blank">📅 19:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437716">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1Kv88hwi_M-tfV6cy1GNAm-efIXYlzyEK6aeQJNumwLKT9EupU3HCVOQnV-ju2IY4Jq4GXW0U8_5gxuOQ0vHCE5XRZXX7p4R2WGCc5xMMsplFoKLg7vfQstgne8S91z1HUqrdbTw5A7N2BE4pXyD3uto7lHMT6HYumz5OFX7zTP6Z-6eyZfdpHC90Nc6nWy8o7hoJkQDFC9meQi7YD-CEsKqCsrDhxcNOcQYt8JC_Jv4JzlqQig2DT_qNF6hftYn4bFri5ox3plXhdcRPaA-fSjg5bC0fcx27UDduPOCjwCq6-yJ34dAwCKZpoHqY5j-rWZAOJxnzA5OPCqe_125g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست ایران و عمان در مورد تنگۀ هرمز
🔹
‏معاون بین‌الملل وزارت خارجه: نشست مبسوطی میان هیئت‌های عمانی و ایرانی برای بررسی مجموعه‌ای از اصول حاکم بر عبور شناورها در تنگه هرمز با رعایت امنیت و حاکمیت ملی دولت‌های ساحلی این‌ تنگه و در پرتو قواعد قابل اعمال حقوق بین‌الملل برگزار شد.
@Farsna
- Link</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/farsna/437716" target="_blank">📅 18:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437715">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXbZpRRXX9zII7SsnDaRMmpGYtK6kUm66qfmpmQMd6iTRXEGJCuSD80WNVRXgqg--4Deaxw3ygvTJriRZKdjNUkbFeR_T2b1i6gjnGnN9TyUDBEUDwqmNqzTC9MenPPnoHZwFVI9pvwgdViwvMaD-JhJCxmbGTmZ9YhqNeU8qo37MxL7TUkS8rBOEBZAXg7V6cjR9wam5s5ryw4k1SgopxKvsuC8hKhYKlmE7KTCWNv3MYMWIcP3b4tFk8-gYAnpgVqvcSged2PyViLxmVlbJgTsxkFTKN_Qn-giRHVjno1ofcE45xWkyCdnSnYRflxwCy7koZBs_MdLoG6M2egR_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو: با ترامپ به توافق رسیدیم که تهدید هسته‌ای ایران باید از بین برود
🔹
از بین‌بردن تهدید هسته‌ای ایران یعنی از بین‌بردن سایت‌های غنی‌سازی اورانیوم و خارج‌کردن اورانیوم غنی‌شده از ایران.
@Farsna</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/437715" target="_blank">📅 18:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437714">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9Wr0LD1kYMGsnhljsYfhED5-yDn7fP_62iyJpjAMhNIRJNkuabnVewaa2KwlN_CTcYiDCIlKeGxRr_CtT3hyuIFXLN4c7wC_KeGbaYCrePAqrsXu5PTGYxZBKqyv1Tnx5ctZElI9W75-R9GHlXw0lzSZATTea2ST6b3wf4RkYn4nH-J69WRaf2raETAp63xAypwqEp5KgI6zIByJuCpi3Rxl6aCZSBd8CYzlZxe40M_dz8twuGttr8hlnXPTkJ0UA84i6VZJviAB2jQ-c19aq_-SdUq5YSsTzcvNo4IEyPi34kez8funEGp9NzxRdXXCmLt9_eqUBrF-DJW57i_Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس قوه‌قضائیه: خرمشهر‌های پیش‌رو را فتح خواهیم کرد
🔹
وحدت ملی در همۀ ساحات و عرصه‌ها، یک اصل اساسی و ضرورت گریزناپذیر است.
🔹
رمز پیروزی ما در عملیات بیت‌‎المقدس در خردادماه سال ۱۳۶۱، «استقامت» و «حضور مردم در صحنه» بود؛ امروز هم با همین ۲ شاخصه و مؤلفه، خرمشهر‌های پیش‌رو را فتح خواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/farsna/437714" target="_blank">📅 18:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437713">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-text">مدیریت تنگه هرمز با یا بدون عمان؟
🔹
محمد امینی‌رعیا، مدیر اندیشکده اقتصاد مقاومتی: وزارت امور خارجه به دنبال مذاکره با عمان برای رسیدن به یک طرح تفکیک دریایی است اما این رویکرد با چالش‌هایی همراه است از جمله اینکه عمان ممکن است با ایران همراهی نکند و منافع ایران محقق نشود.
@Farseconomy</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/437713" target="_blank">📅 18:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437706">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LTuV5dnpSeb6-tYzB46p18yumE4LiycM0OJ_XXc7jEDclwG8QyVrWIqb7OG9ERKIrSF2phu_8pDVORohJgPOnDMlgzxaAibhBTkLimRGGvuzVVkOi0f96cGchrSKRTliv8UE4aXVTZgXntab5b8CK_kwdz7egjovBTlwN74VZyuOPDmVUpoQdOS1BTx-SpTnpuM4PWGQeB1-PyJG_J3xaM4LaxLs6Jl74vnIpZNItew5G5KV95_GyrdZ_RvHJU9N4TOdg2B4PlVLJpVSui34Xoic_dn-GRxnCGVe-_vNZ7kNaYSqucoovTEsPqhXIRb9FeROmxvMtCaJLsM9bYbHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hyqwFJmGYcQGQ0YzOapy3IJXuFIEc93ECCnXdhXZEn2F4FZhMM3480ZA23EseWVj4-O2JYO4YOlDmtPn11-6wrfbYX3c4ZMJAr4N9EsLY77kzMf42rGpbu5VDZs5h9CYsQFdFQZc7mg4u8Xq25WI6bxm97FVUw1Sr_5Gwzfl1M7NCm4dvT9Mb0dLUaIvPVXgd45clLuezGoyPJQ57EvytO-pkQCNPQC-K5n8is7sChvm9aGukxLSTfMLWtfiQqPuYmnBkTqx1Q9aZvtt-g1dzhcRdU60EKL4yW52XzirU2kAorrgywh4-Ly_RXZkdJXvcUNqY8qyhLwou_gOi2sc4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NnS59H02sKD1WWONcILZ3xdrTKiNJjMMWj2yHsXH2NPO0wxSKKVvO8hJ183_LsIafb7CYy78xnclSGkzgW6v4uHyqq__tL3TQMB_uzPq8RqjBzui4wYc-PCEb0iaraMJP1kh7WGs4n7iesglm5_unLJxeCYVgeRKSvLOwo_eL4ATiFyZgQIiRWSDqXz2HwH-ji8iGYUjCGHC8kWSUvWhfVA3uLxjGZWzg7MjRxpgLWcwTIUZUevLlqjiCnGvF0JolG3TWV4L0mXig_8f6XH8b2_KoU1gGAt9PXX7s3GwkQPHCESOH6kcNqqtRAblHrLXp6G6qH8No7TanRNzB6eScQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h1K1k1cUnCLKM1I5zcA9fQOr2I_8I8vstg_bteQx7KV6zM_NiRhQ9ntSIDU3B6eAKYcZZQlXObTV3ORFBZ5rKNmD9pkeY7US1bMq9PswAHbjdOPBSTt0sPpklsL9d91SccrmEJHlq99m5BG99_t_KkFhjtmjvVcbJo7_qQ6KBruZJYGKy0JkUT1QkeFvoC7XD5hi10t1nRWwtsEmNGYVO6MhO5EwzbruHh9AgX-L8LWiR19z559Ocst18rYutGyfsQk7PwTvRhJPF3EJhZsqym01GgJ6hweRZgQCwao-IHXa2Qye_PLB7p3SAkUVqx5YjI5LLk2gYFA8X3q2rbqEJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lRb-N14RmiSXQ2CPnF-8fuk9iufaLwlv2qj9ioPHzsU7WsbYNe98fCunn55UZxvPOUj4Xv8oCA0f5w7eTFkgN4jEhdZszyT9X_V7v1maFRGL4SQllHUtouNt_jD-m9q0fSKVZSJjJj5Yg0XgaQ0t-OAkTaEQPBe0O0zJwwsjmd6q3strCIRjW_ZVXmx9k_yrbav4OFEvCR6XY2yn1gmRk6U2ptqsQavC77YKfJS8vveSM_F1ZjHiqKO65baYm0MwKYYioBKPuyISuZy5FHdvcJ9zhI8ZLPpYQDXR1UXaj4PPiYWE4rsLs4MJI39GMpfw60YAEyxSkAt4vneQLEad4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/slp3aNiT_KONzZyJypx358SEzEJofC6wRNaJJR5iWTVhorTdtNAw9HNr2vXOO77gc8AxlTElxplqnDmj4Tr-cL005awGxw-wRFH0mfak-vheO33_GSUZJ-na1Jcp56T4aS8U-Nz6sx4v1iHzZcZAgDzeZmrK8IrnGAarRe3dbYmEGJ6IH9QpJQSxKOKA3vI2-8FomqvqSk-XiXaNPU4DXa__msy5-EmtT0_SwaDVeOMR-nVPwFeantq3Wk3FAkELqXvhx_-SeeWkwjtVTv58h5ZeweG3dy-jP7jjehvFqTH1vsH_A3AzMcpJh_03WboI3FBXG5FmQf-6vvme18EKLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eaq6RnvkMytamyKb0zL0PDlp25-PV9o88Rfsgx4BwdnodVAvwHV0UwG3NL_gbdcPt9Lacp_pjXXtGqPXxvfAOhgfg2jO4rYlz3yVepAqz02gBrZVuXfJkSqDkhjl2qsIHx_vlmeIAr6RoaDf8PfDFukXxIb80mxIL0-1HWt6GJ6WhcEw5isx9QJhste8KZ-ak9hr4CbSa6OcFk0Z5U6O_Z3czKPthLLDkMrH4C0athvEXUj9HTmtnfeYqerpTR00P1Vh0X-j2f0nlWLdOeEEA101McCe7800qxAqruMnG3W_CD7t99jSkP4iMzQ_f-WWMsJ0HsLJfWvKOvL9l0f2hQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگداشت شهدای جنگ تحمیلی رمضان و سالگرد شهدای اقتدار ایران
عکس:
هادی هیربدوش
@Farsna</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/farsna/437706" target="_blank">📅 18:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437705">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PF1uPUAKl388Jp03WRgbnGDUeZc2SQPyAVyK_hHFcsBkDuEX19xpeu8oqs7qD7t-PlpPOEEzr0SEtvoQlLsZSV7yIc2o_9bhLDA6cQlIjSflObE5OcmlMgJ31An5AZvfuZP3bv-uzXq5cegvWRPlbUT0b-khK49EvSIHyYbvJRQm6wBvIp485mW7mFQ_lfBeCkiI8MgFlV-q36hirWu3VMGl09IIPHlEmFQdFxqMck3NgA0ZuXkAbDeNVhQX_1ulNaPPvtL_PnHla2XJHdwYRi-dHcguKeL2zxEDnA2vHxFRXsjSA6Aiw9p9Vz5y3q6efxOSQXMbQC3upNUtYbWT0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گام بلند بانک رفاه کارگران برای حمایت از شرکت‌های دانش‌بنیان
🔹
با هدف حمایت از شرکت‌های دانش‌بنیان و زیست‌بوم فناوری کشور، بانک رفاه کارگران و بنیاد ایران پیشرفته تفاهم‌نامه همکاری امضاء کردند. این تفاهم‌نامه به امضای دکتر مخبر مشاور و دستیار مقام معظم رهبری و دکتر للـه‌گانی مدیرعامل بانک رفاه رسید.
🔹
دکتر مخبر طی سخنانی در این مراسم با قدردانی از وزیر تعاون، کار و رفاه اجتماعی، سازمان تامین اجتماعی و بانک رفاه کارگران، توجه به احیای شرکت‌های دانش‌بنیان را یک تکلیف ملی دانست و گفت: حمایت از این سرمایه‌های علمی و اقتصادی کشور یک ضرورت انکارناپذیر است و باید با تمام توان از این ظرفیت‌ها صیانت کنیم.
🔹
مشاور و دستیار مقام معظم رهبری  در تشریح اهداف این تفاهم‌نامه گفت: نخستین هدف، تسهیل در تأمین نقدینگی شرکت‌های نوپای دانش‌بنیان برای نمونه‌سازی و دستیابی به محصول نهایی است تا ریسک‌های اولیه کسب‌وکار کاهش یابد و این شرکت‌ها از طریق مشاوره‌های مدیریت مالی و آموزشی به بلوغ اقتصادی برسند.
🔹
مدیرعامل بانک رفاه کارگران نیز طی سخنانی در این مراسم هدف از امضای این تفاهم‌نامه را حمایت از شرکت‌های دانش‌بنیان و زیست‌بوم فناوری کشور اعلام کرد و گفت: بانک رفاه از طریق این تفاهم‌نامه انواع خدمات بانکی و بانکداری الکترونیک به ویژه تامین مالی (ارزی و ریالی) را به این شرکت‌ها ارائه می‌کند. تسریع و تسهیل در ارائه این خدمات ازجمله ضرورت‌های اجرایی تفاهم‌نامه است.
🔹
دکتر للـه‌گانی حمایت از اشتغالزایی به‌ویژه اشتغال فناورمحور را ازجمله رویکردهای اصلی فعالیت‌های بانک رفاه کارگران به عنوان بانک زیرمجموعه وزارت تعاون، کار و رفاه اجتماعی و سازمان تامین اجتماعی عنوان کرد و گفت: تمامی خدمات، محصولات و ابزارهای این بانک با محوریت حمایت از تولید ملی و واحدهای تولیدی طراحی و ارائه می‌شوند و بدون شک شرکت‌های دانش‌بنیان در اولویت حمایت‌های بانک قرار دارند. محصولات این شرکت‌ها نقش تعیین‌کننده‌ای در افزایش تاب‌آوری اجتماعی دارند و بانک به سهم خود از توسعه فعالیت‌های آنان پشتیبانی می‌کند.
@bankrefahkargaran
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/farsna/437705" target="_blank">📅 18:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437704">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgtuzJ62c9tDozA3K7QAmXtwHrSEbMYzvcXz92Sf3lVIMEHTiF3v6b3oDQBW0XNZLDkZV8ZRynrzXyvuVcZn1w8-SjRMFAoTWCEEZxM0I83irpI6M90gdO0ETMWwxZmIDCXOfZ4sla8oUd-B-SIdlXIaGTQ68ZGDcrfuMQyt_tHjxg0d1QuGkUdVKZRW9PkryNyh5xfwLcjlbOmDm6zN6PyXXhst78D-aBBcxPh4tJXfLJaACa3waN3u5WwUrmX6RepjucHcrayjUX_VpVcVk1eOXotieGEr9ZvbVlILvW52Wb-xB6BE4CjgLiy7Iv2Bf2FuSXhCtar7NuGLgbuZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
وزیر راه و شهرسازی: کاهش ۸۰ همت ناترازی بانک مسکن دستمریزاد دارد/ قدردانی ویژه از اقدام جهادی بانک مسکن در حمایت از آسیب‌دیدگان جنگ رمضان/ تأکید بر تسریع در افزایش سرمایه و اجرای طرح مسکن استیجاری
◀️
«دکتر فرزانه صادق» وزیر راه و شهرسازی در همایش مدیران ارشد بانک مسکن از اقدامات جهادی مدیران و کارکنان این بانک در حمایت به موقع و سریع از آسیب‌دیدگان جنگ تحمیلی سوم و پرداخت سه روزه وام ودیعه مسکن قدردانی کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/farsna/437704" target="_blank">📅 18:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437703">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/farsna/437703" target="_blank">📅 18:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437702">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-45.pdf</div>
  <div class="tg-doc-extra">3.1 MB</div>
</div>
<a href="https://t.me/farsna/437702" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-44.pdf</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/farsna/437702" target="_blank">📅 18:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437701">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxRBHV7ARMb3OVVknogE33lhSptOJO8qB4M4wLiOSP6zzTOMdTsvNyTTiL_9iFXMBBzRmiljkL-BTdq0HT3cRGr3rTdihvkcL8lNFbsaYG1YH51c4krt2cWmZ9apI-49zxU4WvftopQlLsYwTWVU8El4TI6xg_AyGnimeHeFel18ELFIe5GflBnSoVXJTwkLWdFW9nDw-Rvhy-j1cDoohV0Wo2pTwD8KSyw5xUWD1bVPlxPqn_3wRfHmb37kcaLCDUPhLohcILn21tQkmZ_7apkTNBC1NPRosqNWhiss3m43Cy4ei-4FKzM6YsU9EgPpgGa_61mHuqmhGJqeVUqhMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرکت مردمی جان‌فدا وارد فاز تازه‌ای می‌شود
🔹
جان‌فدا کاروانی‌ست که در تاریخ حرکت کرده و هر نام جدید که به آن می‌پیوندد، قطره‌ای است که به  رود خروشان اراده ملت مسلمان ایران می‌پیوندد تا سد تحقیرها و تهدیدهای تاریخی این خاک را بشکافد و دشمن را در سیل ایمان و توکل خویش، غرق کند.
🔹
برای شرکت در بخش‌های تخصصی جانفدا و فراگیری آموزش‌های جدید همین الان به سایت زیر مراجعه کنید.
form.janfadaa.ir/login
@Farsna</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/farsna/437701" target="_blank">📅 17:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437700">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a14b750f68.mp4?token=joZg-Q7Gx6hKHRN6CBOIFnbrZM-_39Flq54rdo5HOz2Eyiason-UFUcAGksq02oWKLAXdcokwBVsDpPto4QkO4AYXK29fyFKkeb7onYGQZp-PtRS56_-HmmS3pGuPJFSn-oKp6sq7k0ZTLAAKBbmTYFDgVGhG90XeW8XBD-fO2O5Z_kvI2GSG6yZOd8ixPY6ZrwoqglyH31gSYgIByNwFBacH3UBdPxJqB-BBLjzi2mnDmSc9-_VJw4h-yvVsnV7yUcUFv1Ya3pKV4kgLodZBAgwZHMLB9DXX-TDemArWCH5MxVI3i5L9QzNO1mhbZn6rQDi5vHJKPe3ieg7eeQVxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a14b750f68.mp4?token=joZg-Q7Gx6hKHRN6CBOIFnbrZM-_39Flq54rdo5HOz2Eyiason-UFUcAGksq02oWKLAXdcokwBVsDpPto4QkO4AYXK29fyFKkeb7onYGQZp-PtRS56_-HmmS3pGuPJFSn-oKp6sq7k0ZTLAAKBbmTYFDgVGhG90XeW8XBD-fO2O5Z_kvI2GSG6yZOd8ixPY6ZrwoqglyH31gSYgIByNwFBacH3UBdPxJqB-BBLjzi2mnDmSc9-_VJw4h-yvVsnV7yUcUFv1Ya3pKV4kgLodZBAgwZHMLB9DXX-TDemArWCH5MxVI3i5L9QzNO1mhbZn6rQDi5vHJKPe3ieg7eeQVxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکار یک نظامی صهیونیست توسط پهپاد حزب‌الله
@Farsna</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/farsna/437700" target="_blank">📅 17:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437699">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سرلشکر رضایی: پشت صبر راهبردی ایران خشم انقلابی ملت است
🔹
امروز ترامپ و ارتش آمریکا در یک بن‌بست کامل قرار دارند و اگر وارد جنگ شوند، در برابر آنها دالانی تاریک و بی‌انتها قرار خواهد گرفت؛ دالانی که از تنگۀ هرمز آغاز می‌شود، به خلیج فارس، دریای عمان، تنگه…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/437699" target="_blank">📅 17:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437698">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VB98bEDiZ_vtQ_o3OGhzJPCjZ3hFlTEv71QV-moL5_PceDfRXO0P680ZEwM9f62bOQjgAcwvQXzSR7bSO702yfwUC2Xc6l1-BJLFyoJ4qCmCIR0Q53NC-hdbbahEEnORTIoZvq9BOmJE2e40deza1OugIfostdVGfPLV2XcWFlpl4wAwtlj5th3Ejiq2IpDZNQ4Us5NMjsBcVmDEEHuS8WnQCKSJyutNsCwBgFe0Kjdk4UBq_NbEX33ahExBH1I2Gp8OrKUtfspCfcx_8oRD97VgCphrcu15_-GoulkaIqXpE3AnWNQH06hqKlVv3N1xynQHc3hN2kX7zQ3iejYqJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر رضایی: پشت صبر راهبردی ایران خشم انقلابی ملت است
🔹
امروز ترامپ و ارتش آمریکا در یک بن‌بست کامل قرار دارند و اگر وارد جنگ شوند، در برابر آنها دالانی تاریک و بی‌انتها قرار خواهد گرفت؛ دالانی که از تنگۀ هرمز آغاز می‌شود، به خلیج فارس، دریای عمان، تنگه باب‌المندب و اقیانوس هند امتداد می‌یابد و جنگی بسیار گسترده را رقم خواهد زد.
🔹
تنگۀ هرمز برای تجارت آزاد بسته نیست، بلکه برای لشکرکشی و ایجاد جنگ در منطقه بسته است و مدیریت فعلی نیروی دریایی سپاه موجب شده کشتی‌های کشورهای مختلف پس از شناسایی و ثبت، با امنیت از این مسیر عبور کنند.
🔹
در صورت هرگونه اقدام نظامی علیه تنگۀ هرمز و تلاش برای ورود به خلیج فارس، جمهوری اسلامی پاسخی سخت، دردناک و بی‌نظیر خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/437698" target="_blank">📅 17:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437692">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IYr-Rdn2dqOHV65cVvvxMr1o1_II_T9uPVcuqJdrz5xLMywY7NGNd9EuSA-WNwrRrtwEG3sFPGdCn5PK03VX9jScnWz7TfkZguubBr3rDghiKEi6SzfefWKnBiFRut26WOtXa2gpuyd_4cAt-O-XEaZ8XG7AedKUzv3JsE8Tq2VIaRySb9iKqLLQrw35VFi1uBU5SyalF5POvf5FHxZ_Kq8FG2gZ7DQnsXujzb2qnsIWpHeBZCKg5n6wlJ-9mF7KLXpTM6bxXRsyH930902a-gFLfpkst7-zAByBbLcNED2O6sKFSVC1fK8WQ-9EdaFu44ABTff05ObW0R2cDC0SIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYf0rTzK59hh70C0fhMvo0uXz4fpNtD2GDvgId2j7tfUUF4aa3og6EA0urKkRdMPXimfdj17Th61p67gq_UT9aYbpz5k4bwABviL1bXxrxROIrfEVk5Htzymzi8l8mbPta2cgUtqHbP4R5pxQIopwEk0TOm-WmJsPvKfKdvWFG5LCrVmtXhKyrQevzz3aUTcX-ILiiov41BelWUGD8sV6sQWelpWtttDv4klLt6k4VdoejUv3IhgmVWnAot9v5EqkrH17BecB3g4tYxx4CE19zn8Q_KgoHlE3WB09uBGs-lArBR9CxTnZrW8KuN4JL-Nf66VUQJ0IrJhoT1T2HsZNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vUGjNhLd9-aZyQyHgL-0UFnb-9fZsKh6HmDOXkYQLoclKQArbPaoxsDxF_EsbpkWekfe_QZzWB2SPnEvtllvDgSFScZ-78GjoEoga3Nhw-iDVEPrqBrvZEjUJdv8RV0NTRUjXrDdBA_UboqWPDG8oRAKYIzT9ITkkDQcWrJugMGy5LVlC1oV11dva4jtzBSsswUHzlr1LtPHFNZ2fIoc4WmR9swwgi9Q5jqNqS9lBOhN2HSBlrUlGZTaFsXCZBe4fH4itTwGw0AXgCImvA4cWuoo6U8UQluDXuCwgkIycNRdiKOcnMqv99GS3Eh2MeqiCiVKvMTrNFxRIe1qjIvQ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SFX3bLkZS6lfAK4iHw2Uh4dgEMsysnxm-q63TaHckY89a-93Nf2dsemxXzWPy7JFNThTNu4vd6dzobv-VnI-NdkT9H32i-yZd5zxaRgMkrrf3ozw82LTiyWE21-EJlVxnk4USpv57pg3wpz05gxVjgzcUKJzg7ysZ6hl1VV3U7dB3esWOvLjzXPPvWfj1QEWcqZKi-7ALcI16v0BiUa1_5qTDXqR7X_Nwnrj1glAKa9JQ4o0iTz-blwKllLvpahHMMQ4ezBRawqRrVcND1EoBl24zW0pumoEKiHz1MHX8TZz7YiOS9ze2GLRZ5Z5Vwc6IBkzJ75z-nm55VknZB6xuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nIPUjdSMVnlvpxFIqT2OQAwk6lmc3MtLIVK6ejkr1qE4dtu_xJY3-5qIa4dwiUCu8e6BWVKklJiSxtxLDSlW69UZEq3oheEr9W5dDxM5zrM8k3KRdg0D1px5YkLwrSWhJbRXU3yh5hrOf1b1nkpRYX4u_RSg2v7-wvw81ylhK9XmvwFXUNXqGZJgplKJnlhbNPiKNxCZ1GZ-n8gjRmcZ9UViG3mc9HpBGe1eJxQifvitJLCo0PpxW17dIrG-1vK-7EXP4S7TzDCkujOi0sOMgIwIwaUyCAznsVCrZH2tN-jBunR1XIEusZyjN-j4pS12-icYjon1r3qf4-aTUK-FqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hG159aJowdyLRBm74RbagRiUxHbiuwnJW2eJ1frmRgXUE8Rx1JiN6NxJEHDNhFW4u5GDGnihnmFwFcu6Wljqsncf_V8x3RlFOuOhHLnIfN4vcGd8oPztMW2CT6fmoRBS4XXUGsVXohhpKkUuB5JrmQlcTCXZK-Dkba4qMc3ElAPzyKkOUTyCh0rr0D0ME0LLeD1-AF1Orhb5C9LA9O4-GAFeGoMWlLh6c3_jKMNCeWAHMQdJUbxTWqVfskkcbcGbA7XzkckQLSWb3gAZajbOQbWyr9_9UDwgxks_uJa4mVm0q-xuCAlrtH1mZncFivEup0DKVAD3zPApZKPPJg6MNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از تمرینات امروز ملی‌پوشان فوتبال ایران
@Sportfars</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/437692" target="_blank">📅 17:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437690">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دادستان تهران: ۱۳ نفر در پرونده‌های مربوط به تراستی‌ها و رفع تعهدات ارزی بازداشت شدند.‌
@Farsna</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/437690" target="_blank">📅 17:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437689">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441854eb14.mp4?token=Nxj_5A6ZIKactjbGMtE7qCGzaXh20_gKuPT7LQttQ17an3kMHX19Njr2t_Ct61XAf8sfIUbICt4PdAr-3WGcHXEuNNNQ1XNhNo_oWfoaL0hadN2O5G-N-9vXxpSU06w8kibQLo_9pjJzuKQOB9rKBAtjHHRRXuNiX6--WzOA4xYFzrip-BCfaUknZVQ7xRtoLhFHrCVct6D--f3TTcHJjOrb4ag8p-IZKb11Al35GWDpa9EwkxmVERe565vnl2y1Rb9Bus2Ts7i_1hNUS6M8NhsHYystBHa0jkFPSWQ7OZbS65RepXqiTlsHZM4pcWmNxNhOfJ3xltqEJ6a35N6q_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441854eb14.mp4?token=Nxj_5A6ZIKactjbGMtE7qCGzaXh20_gKuPT7LQttQ17an3kMHX19Njr2t_Ct61XAf8sfIUbICt4PdAr-3WGcHXEuNNNQ1XNhNo_oWfoaL0hadN2O5G-N-9vXxpSU06w8kibQLo_9pjJzuKQOB9rKBAtjHHRRXuNiX6--WzOA4xYFzrip-BCfaUknZVQ7xRtoLhFHrCVct6D--f3TTcHJjOrb4ag8p-IZKb11Al35GWDpa9EwkxmVERe565vnl2y1Rb9Bus2Ts7i_1hNUS6M8NhsHYystBHa0jkFPSWQ7OZbS65RepXqiTlsHZM4pcWmNxNhOfJ3xltqEJ6a35N6q_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور سرلشکر عبداللهی، فرمانده قرارگاه خاتم‌الانبیاء، در مراسم شهدای جنگ رمضان  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/437689" target="_blank">📅 16:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437687">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/662d4ee6ff.mp4?token=DGIpfrMvPnIzCQOr6A6DscLqV8Xx6XLDhu2Qxz642RyKu-sCDGRuOK9Y4e0Z3iSblyHygzCRtaK5-TX3ZIJKs1Cz3NYWX_9C35xtbhjbIkifbzJOd9ORkqG9-suO-l1l1K-ZrS9zJPbWiSfUWnc9Sxbejg3aG9u54RMjG66qTd_YxMnOJ8BT6NE4ierbvFt7f7ryu52LkpOUjZrbZDhEVhc0XOXLi0f_NtPBP69MBokRmfuL4wSg53fzGaQCtPyzaMr0DpErU_Mi4Q2p96Sa3mboKotfYw9BLxPPvqzSMIpcBgXSHfrw4_18j0w0xiNag7uHZWQVGyqIffYJPCq3ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/662d4ee6ff.mp4?token=DGIpfrMvPnIzCQOr6A6DscLqV8Xx6XLDhu2Qxz642RyKu-sCDGRuOK9Y4e0Z3iSblyHygzCRtaK5-TX3ZIJKs1Cz3NYWX_9C35xtbhjbIkifbzJOd9ORkqG9-suO-l1l1K-ZrS9zJPbWiSfUWnc9Sxbejg3aG9u54RMjG66qTd_YxMnOJ8BT6NE4ierbvFt7f7ryu52LkpOUjZrbZDhEVhc0XOXLi0f_NtPBP69MBokRmfuL4wSg53fzGaQCtPyzaMr0DpErU_Mi4Q2p96Sa3mboKotfYw9BLxPPvqzSMIpcBgXSHfrw4_18j0w0xiNag7uHZWQVGyqIffYJPCq3ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فعال اصلاح‌طلب: مردم پاسخ غایبان روزهای سخت را خواهند داد
🔹
باقری، دبیرکل حزب اصلاح‌طلب عهد ایران: در این بزنگاه که کشور در معرض خطر و آسیب قرار دارد، پیوستن به دریای زلال ملی شاید کم پیش بیاید.
🔹
فرزندان این کشور نیز نیاز به این معرکه داشتند که دین خود…</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/437687" target="_blank">📅 16:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437686">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651ceb7ed5.mp4?token=A7gyhs2eSgXl08cDk4limCdzTVM1-V-xBo1Xd4Ua-ool023EOfbPj2BGFlhK5iIz_MP2PJ8W7vDD3kRIIOMhSdxxqodQeibViP159qHXcC99PMQaJCaUpf_oLmpqlPz6n_O_-f_l9hBMI8IHBl7y6Id2t5ii4TouYFaP1RKBLenFCszmIhCoCz5KOsZpKoNpPOYDnS6iqW1G2LJVUMm4HTWy9A3bX88LcoWYv4YEvK8TZCpLjB08v0eymLMb2qeawPnwu8dexseP8XN1cJy0Y9IEqe54LmrI0Bog1EwOd-K1SfoBSxj7aMulSBRTJNThuzU3e7PD4Fq0Aue7G99uZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651ceb7ed5.mp4?token=A7gyhs2eSgXl08cDk4limCdzTVM1-V-xBo1Xd4Ua-ool023EOfbPj2BGFlhK5iIz_MP2PJ8W7vDD3kRIIOMhSdxxqodQeibViP159qHXcC99PMQaJCaUpf_oLmpqlPz6n_O_-f_l9hBMI8IHBl7y6Id2t5ii4TouYFaP1RKBLenFCszmIhCoCz5KOsZpKoNpPOYDnS6iqW1G2LJVUMm4HTWy9A3bX88LcoWYv4YEvK8TZCpLjB08v0eymLMb2qeawPnwu8dexseP8XN1cJy0Y9IEqe54LmrI0Bog1EwOd-K1SfoBSxj7aMulSBRTJNThuzU3e7PD4Fq0Aue7G99uZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیداشدن لاشۀ پهپاد ساقط‌شده در هرمزگان
@Farsna</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farsna/437686" target="_blank">📅 16:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437685">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21abf1a966.mp4?token=E1svFiEzwc6wi_iv0xyqm97JgGNE6jZbN2nBbsJ57IFnN86pdObg3L_HEHGXJWw0mPbRuXbC6Ds6H_JKcVjePEJL57JTyrnD2xeP23mrtvbHQeXE08EC9Wo2b7VuO7VIDkeEgXHT_z0jovEXKmNXiP2AmIlJwMPtb0YnstC-KcuzXFRqPDaLywYF1mF9Wf8PwsGKILx83fgLf-vAWLXc_Mhq6Q9TlIQzXuIHdh0_2p1qrm654_S996II8eB4RhPl3SxvM2J693QfeqidofpZcFigsy5OZ5wF3Rth1wBjCI68NAXarZV9jhwKbpCxtcOYNS1PFn4x8A4nACb327qsqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21abf1a966.mp4?token=E1svFiEzwc6wi_iv0xyqm97JgGNE6jZbN2nBbsJ57IFnN86pdObg3L_HEHGXJWw0mPbRuXbC6Ds6H_JKcVjePEJL57JTyrnD2xeP23mrtvbHQeXE08EC9Wo2b7VuO7VIDkeEgXHT_z0jovEXKmNXiP2AmIlJwMPtb0YnstC-KcuzXFRqPDaLywYF1mF9Wf8PwsGKILx83fgLf-vAWLXc_Mhq6Q9TlIQzXuIHdh0_2p1qrm654_S996II8eB4RhPl3SxvM2J693QfeqidofpZcFigsy5OZ5wF3Rth1wBjCI68NAXarZV9jhwKbpCxtcOYNS1PFn4x8A4nACb327qsqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور سرلشکر عبداللهی، فرمانده قرارگاه خاتم‌الانبیاء، در مراسم شهدای جنگ رمضان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/437685" target="_blank">📅 16:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437684">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44112af52a.mp4?token=YnB7JTBLwGMA0UIRXDh14tF1jp6mjxgyI_9JPes0P1gD8DNTV29Nbo6HD5tYio3cQIRJ16eHnYL8nNKOCxoDEr5q29BMQdqH7k6B6iy53w5Eahkx15-9i-OuRdERKF-CnT04tiHFAVYPHniVKdcx13Uera-zgxZ6An5wThCshyYjLjDcYfWinJBPKl0YJlorsyZ6uBLfndtDSub73gVYCUi7c-MgVtqhjAL0JcWFcgLYmQYzUUCpHps3zdjIs1YFjBJQQaR1bW7TFu-9cRR7xRMLGCxE1j58CUd5V8OKpQOkmNw8KHLv3dEMtV8rnTMePndtk2UkDzUcG8Q70erJ-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44112af52a.mp4?token=YnB7JTBLwGMA0UIRXDh14tF1jp6mjxgyI_9JPes0P1gD8DNTV29Nbo6HD5tYio3cQIRJ16eHnYL8nNKOCxoDEr5q29BMQdqH7k6B6iy53w5Eahkx15-9i-OuRdERKF-CnT04tiHFAVYPHniVKdcx13Uera-zgxZ6An5wThCshyYjLjDcYfWinJBPKl0YJlorsyZ6uBLfndtDSub73gVYCUi7c-MgVtqhjAL0JcWFcgLYmQYzUUCpHps3zdjIs1YFjBJQQaR1bW7TFu-9cRR7xRMLGCxE1j58CUd5V8OKpQOkmNw8KHLv3dEMtV8rnTMePndtk2UkDzUcG8Q70erJ-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: کشور برای واردات بنزین هزینۀ بالایی می‌پردازد
🔹
با مصرف بهینه می‌توانیم این هزینه‌ها را تقلیل دهیم تا روی سطح رفاه مردم تاثیر منفی نگذارد.
@Farsna</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/437684" target="_blank">📅 16:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437683">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‌ عبور ۲۵ کشتی از تنگهٔ هرمز در شبانه‌روز گذشته
🔹
نیروی دریایی سپاه: در شبانه‌روز گذشته ۲۵ کشتی اعم از نفتکش، کانتینربر و سایر کشتی‌های تجاری پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگهٔ هرمز عبور کردند. @Farsna</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/437683" target="_blank">📅 15:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437681">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSADXVLLrf3PWDlREucLXirvURLofWBSeMaQRggR_d0JVD44DSjTrn8ACZ5iFxPC8P7kI0GS5NeNKn4qKFbYYYWcikYggMra_MMYPBPJUeWZ9PpgNB4rmtGpZffT-VaBQZ1GrN2MJ-6TkhfbrWngvETSLwQoW2r4-dpE4vHerQdRp6zt-2_dfFC3pDULN_IpU1LHzFcMUfOSKiG5jTtQdsCLWXJZECj0nWunL_PE5pyuEZvyEPnSIvcJviwQvwmGuAhEg_2JMAgn8wB0NFF9qq8EECoOGtyxQ3xE_kQ1rGOOZpPnYjqHqUtAHJou1MX8AigF0EXIErabK5gtMw1cKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: موضوعاتی مثل «خاتمهٔ جنگ در تمام جبهه‌ها، وضعیت تنگهٔ هرمز و خاتمهٔ راهزنی دریایی آمریکا» همچنان محل بحث است. @Farsna</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/437681" target="_blank">📅 15:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437674">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vS2JVVP5IMFHLyARtyaFkX_OaCOkDH4D-_phGgeDp6eepY2sMnDWy2NeyI2JrJLMrY4apIoQ2Hf4VN_r--3PqmqPtbcWuzAjN0Bs36JwHCPOcafmpvyxClNywR3THxzM5BJXfvOag4YUviMNUF2RvGWmPM0lAEyWtrVX3DoWgKrwB3qTIT2sdL62Z4HdMY6svHv8LRungWWj_3_jz_Q-wlSc6ct-Hk-uXxulM4-iA_ZpSj9Eqrg0Ak2bmQJU3RxuI12rPQd9AnQGsW6dkjbCwQQ4c2HafcIVwoCjlB4aN3XbweW3TUnkyYGGKCbAYScS9qjnMWjA518lkmi9s12UjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vS500TaB-EeZjOLm5476QATMfa0p93msd_73QdMjSp87hVSAe-V7xFjNS91Alo7oZb3Egy0oP8kfR7si2ZUyTahdlbVfims_2Kgg4fDr-BSJ1ENxNk12907bL9KDGoBGrMuI4lXSNJUk5Jjyl3t5jG3LYhv4izB07hbfO8MpQ4CNruMcT_DfU1QGQGZX-3DfpFVyIWtwimF7e3reFDPPSQ5yOeOSidi_s1rlcTIm-ryjYs6XAlC14HUKV9pCixY821W04qUC7omyZblg2wQAaMwe5Pf2KLNpVpg-5hjZo6xA30Wu5zEZzkTs1r07sgSEIIC08pSet83kdNOF-7735w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bQvvN4PErVeetJP0soTStSnTMB4VwYxH1ErEfPRuA4i9qqj7bzt8YUcBZjeRFhRxZdGiWx06WLNnoKeV2uoLC7WzIQ-kzDnvg0TBsFf3F5lkFe1UFGu9Bx5NHniF0-xSj-gKdffa5GO-iBUFIzWMTl6YUY8aliRkmnR6i6ou5bA4Q-eCMLTPDFEtK1D8nCFjw5RidntIaOnRR5XjUhmUwVNhjJFvDSBKHLmThO_WITUWgboYzKNp7Tbo06ZYNco0laS12HLaHb7giwfy1JElaYoXYZMFRPbsrM-1FeZveD-Ky0lzz7PlOBGUNjyZ3WMsMrd4bXtD73moOoVNyNP-XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phwGqgrpNUuZ6LEFQYXEI6yXmjo6nW3Q_MOYDqDcHduqGEV4oLnSJphIqR6qw-o2j5Cb0hiYYKrF30DACSsXcGwB6tQISVCaq4pJOu_K8Hi8J04dy_E-eNiKXmJoc7iAfkCD3Zs78TXpnMYMVE52L55-4Tufsi2HCcaXPA2_l6sQNgqpMtdUoYNRFwFh121RmxUxMOLtYDhWQiVkYuK46KJpOJ1eSzRreDuXnUAHtwgcCtKV5czMy4BwFstKBQtGUXTjsz-Rk51dj_w496_JnyObbvJVtlCyPG2u3jM5B_ClchPGOG22IkDNsMMM2vm-7dQx8IWsSNUHVB9fT_kbmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nn_q-NhWstsGe0LSBCu9-pr1DpzJXT_a4oQlvtcb9uO2uugyLq1N6_3At5q59Gw2bbOp4lj9GBcrvpde2AVaHTeC3PQ_hG95kQQF8yqQ4i3lJem3F9WvIidzc90Vtw0-TBAX8VkCyh35rFG6gZ-r2-WH8XbHpkW5_ysJNLT1O4oJ-bOUVVFejVe0l42Zgorc0JG2pzlCu5TU7UR5Vp2Zr8Od8VR9Fc0yrge9JHdUaH9laHrTfzDzvwBsqn0jol5eUkyPx5j8ppn_IkpRj7Iok0G2MBDnpV4-YAtyy_LjUnwSR_Yy41G1wtjifVqRTbWNbjE1ZpCfQwiutmLJyEwE-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k1LwzAZWGtIGk4hlPqgGM7N4xj5md7-QMDjK5Uov9VLXLTYWYumk7h6sEBDRRCov-0bLJFCWns0P-SMpeUkJF5at7ZdJoyMtDS00nCSotQrhZ73DeUIWdSmB9dScvPMd-2psV2vOUOXFLvYobRfkvAlo2s5no_BMH3Q9OgsWHDduQxr4T_a8nhRPkncHbLxJnBqqw7pLbGJba0QEFZkAb2w6xwcSJESGUJ_mvEyTYFAVN7gfIskYkMYtOOPPCXMSZtFgWaNtvgVAfMAw9Wynezo8owb39C2yitMAqHfPuLHtLyH_qVDBW57cM5WWCxcuJxVq5tKfPOfGzcCo_vaq3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/npZed6zfiOdytI54KmC3IAsbVgtzn694Bwk6kNkkzva7Ai0JR5QeGp8BVEjeKALrbCEoG83H4diXklZiGn6X0gYQqw0WtBEwlvQ-rH7HOrHZ0E0PwsgN8cSiZxLZZfYjR-TCtrbik8A0bPBeTVoXEy5iKtny4ftSQi3cf0i0VLBYcdE7DAP7qd78LDpKYz96L62eC2gmtVHhG3mv8oIPNb8NeeXNEMmqInfHvACt8dc3P6EX2_vfQjL2mLhQ6geVyxTS7ffMkCO43GGVZMHH6jXKuZatygF-TBWcv-XwWSfQg9pfkjliWDf19xtB6LcdRvvs-yfW2-ynSgpmu_X7Kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مسابقهٔ تیراندازی شمال‌شرق کشور در بجنورد
عکس:
رضا خبازان
@Farsna</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/437674" target="_blank">📅 15:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437673">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f0f6b8fc.mp4?token=RiSwLp8vlEej8OaXB_alYJ3rDWoukTAjol0V4X4ZMIHhritgCtsJzdXMyFtIBYk_tgPONdhU-xn0vH4Rmi3P0oYfpBXc0PI5NhduVWAunqx_vP9C22GmqjYC62xFGwCQx2X5COMbC4ZD3WO8h2h-HSyT3Blm2D0ffGaBiv-XLbZIz5bJqUusiBUH0K6KOmdYfuy9ASpsnj5eTU-5oga-ZhDcSoD43f01HWKVDKZKAC7bAdxsfqohYUJpJBQyi9_nKqPx_6twPZNQrkoYyyMIgcPhFFvJZLkJTm4HNHiT0p1jQ8zS6y6gSM_nCiGLHuWEmbydNrSCfMhWub8w2dVM6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f0f6b8fc.mp4?token=RiSwLp8vlEej8OaXB_alYJ3rDWoukTAjol0V4X4ZMIHhritgCtsJzdXMyFtIBYk_tgPONdhU-xn0vH4Rmi3P0oYfpBXc0PI5NhduVWAunqx_vP9C22GmqjYC62xFGwCQx2X5COMbC4ZD3WO8h2h-HSyT3Blm2D0ffGaBiv-XLbZIz5bJqUusiBUH0K6KOmdYfuy9ASpsnj5eTU-5oga-ZhDcSoD43f01HWKVDKZKAC7bAdxsfqohYUJpJBQyi9_nKqPx_6twPZNQrkoYyyMIgcPhFFvJZLkJTm4HNHiT0p1jQ8zS6y6gSM_nCiGLHuWEmbydNrSCfMhWub8w2dVM6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درخواست مهمان انگلیسی اینترنشنال برای کشتار ایرانی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/437673" target="_blank">📅 15:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437672">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">انهدام دو هستۀ تروریستی در استان فارس
🔹
اطلاعات سپاه استان فارس: ۱۵ نفر از اعضای شبکۀ آموزش دیده که در اغتشاشات گذشته نیز فعال بودند دستگیر شدند. این افراد در قالب ۲ هسته سازمان یافته و در ارتباط با گروهک نوپدید تروریستی فعالیت داشتند و در ایام جنگ رمضان با حمایت از رژیم صهیونیستی نقشۀ توطئه و ترور جمعی از شهروندان را طراحی کرده بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/437672" target="_blank">📅 15:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437671">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f04163d6.mp4?token=N8luvIdIpGiDVipgbMDS3yEjNOzcNPim9K5_9RAX_-wVX9xQEAwTXczOP1o4musYhFKsFvZXbuH8gmZKh78jSIztWEJzqQtslkILQKGjUQoTJ7gNkojcHAkrU8sWcJ-iwdOrEZ69IZ7hx4-0_dn7MpyyRFuvGxUv7TbvsmjgyvVssyVeaa35dUJuL09jafzRID3Q5R683ZU-kYeCMJ3pPRDqGNzEkmAUxQlN2aB6zNjKRtxjHKpXKbz7O218YwvRvmG36VLHNwtFkGxvX9fW0fdhpVE0prVAeUTiI8rI4Ev9HMEta7WIXjQ4gPodMI3Z2RFX5IArib3ZhX6iEJX94g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f04163d6.mp4?token=N8luvIdIpGiDVipgbMDS3yEjNOzcNPim9K5_9RAX_-wVX9xQEAwTXczOP1o4musYhFKsFvZXbuH8gmZKh78jSIztWEJzqQtslkILQKGjUQoTJ7gNkojcHAkrU8sWcJ-iwdOrEZ69IZ7hx4-0_dn7MpyyRFuvGxUv7TbvsmjgyvVssyVeaa35dUJuL09jafzRID3Q5R683ZU-kYeCMJ3pPRDqGNzEkmAUxQlN2aB6zNjKRtxjHKpXKbz7O218YwvRvmG36VLHNwtFkGxvX9fW0fdhpVE0prVAeUTiI8rI4Ev9HMEta7WIXjQ4gPodMI3Z2RFX5IArib3ZhX6iEJX94g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو: برق مشترکانی که با دولت برای مصرف بهینه همکاری نکنند، قطع خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/437671" target="_blank">📅 15:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437670">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUImi_Ak6XVQ_jAuqMIs_SxyxCliRqqloI2t_vQDfl17oj3jmVXSdgXz_WWOlL4ZIWBUlcHqFnS7uIGaf7IwWW_4h3Ii7RhW4Eq5hXTFK1fWkhFRk9uN9aSn1jZlZx_DkjBjsvLncOB4Ab907xcqp6EbjsW6J6pwMuSv9Mqkr8AdbVoMJg4TksHaYQK92LW1f_nDYmSMAifFy1vRnP1rFj3vjbKD-jfCtXm2WBxK8M5ZzeLay-iTxcRBw15qtl_DwcRqEmVkk3sASRgMpgs32OKE5_1KCJSv2zLpUiseEBzLxscR6TyIkcXgHwiemaqbAOxkV3VTIHEdqjqtCyJUKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: هیچ مسئولی حق اظهارنظر شخصی دربارۀ بنزین ندارد
🔹
اگر مدیران دولت از این دستور تخطی کنند با آنها برخورد می‌شود، زیرا ابتدا باید نظرات کارشناسی بررسی و سپس جمع‌بندی نهایی با در نظر گرفتن همۀ جوانب امر حاصل شود.
🔹
لذا مسئولان تا پیش از آن حق ندارند اظهارنظر شخصی کنند، چرا که نباید در جامعه التهاب یا نگرانی ایجاد شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/437670" target="_blank">📅 15:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437669">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تداوم بازداشت ۴۱ عالم شیعی در زندان‌های بحرین
🔹
جمعیت وفاق ملی اسلامی بحرین: از زمان قطع ارتباط با ۴۱ عالم شیعی بازداشت‌شده بیش از ۷۲ ساعت می‌گذرد؛ امری که نشانگر ادامه جنگ سیستماتیک علیه شیعیان در بحرین است.
🔹
رژیم بحرین همچنین ۱۰ شهروند را در پرونده‌های…</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/437669" target="_blank">📅 14:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437668">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT8v7J5FKbJYtHpr4m3cByCcTCaNrmgE_mRus0W4NcldlsM52FgLQpQ_7vIY8jFzz0bhT9I5QK7pbNKtU4nJybS4X_Jktc2auZPrNSVCjNMv-Xjxjw7qJQKMyarj_asimmfTsY5JG742jV9ml4Bxl3iTkRpwfUkTI5UuhIayKifTRgeJ5MwrgjXRou3-zGIba8Ox_fMskxH39INiNYQky682kseIPBy54goj203B8EkY9ky00C81THYh1QtDqU9hNIehq1m5vQ_4pEqShwkmZF5WcRsKtuqOIEXqJBiFOm7zmIVLUTZ0xTp8UVMJy42ieoIo7uH-_J0wtFvcYMheWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران نسخهٔ فوتبال عربستان را پیچید
🔹
عربستان در عرض ۳ سال بیش از ۳ میلیارد دلار در فوتبال هزینه کرده تا پرخرج‌ترین لیگ آسیا شناخته شود.
🔹
پیش از این گزارش‌هایی در زمینهٔ کاهش بودجهٔ جذب بازیکنان خارجی سرشناس در لیگ عربستان به‌دلیل عدم سودهی و ضرر ۴ باشگاه بزرگ سعودی مطرح بود.
🔹
حالا نشریهٔ اکیپ خبر می‌دهد که به‌دلیل بحران ژئوپلیتیک مرتبط با جنگ ایران بودجه‌های اختصاص‌یافته به فوتبال در عربستان سعودی به‌طور قابل‌توجهی کاهش خواهد یافت.
🔹
رسانهٔ فرانسوی نوشت: اگر فوتبالیستی تا این لحظه نتوانسته با انتقال به لیگ عربستان پول هنگفتی به جیب بزند دیگر این امکان مهیا نیست؛ چون بخش بزرگ از این پول‌ها باید به مسائل امنیتی کشور اختصاص یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/437668" target="_blank">📅 14:58 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437667">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06dfe7d947.mp4?token=ANtIZqmcFyakbe0DS770Git-vyLNvEVT_Lg5tHCucikdFwa-7XwO75WkYqbbmUpw3fGMg7OrZ8CzCiUJctvKqTch5iNb2KngsLcoHuwGOgz5_Eibydx568y6sO9rMnfTIDCctM3q6pbV6oUme_6fh5kpywlLNMlGAGPj1ghz_qA36kNRvol6mrUf5rbwdXC3kUWrvEFDV2qYfYpUE4Te_re4Ier77M1X_4Qq8U0yN_4roWrT21oa7pYJ_grpbVNNl9Ndw_iK0s0VhKB8jYvVCV-gDoP1GsdRBLIGFXzNoV9V6euR0bpm9fk5-ZwG7kHWQJDZsqgBQ1O0Yxa9E0K5WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06dfe7d947.mp4?token=ANtIZqmcFyakbe0DS770Git-vyLNvEVT_Lg5tHCucikdFwa-7XwO75WkYqbbmUpw3fGMg7OrZ8CzCiUJctvKqTch5iNb2KngsLcoHuwGOgz5_Eibydx568y6sO9rMnfTIDCctM3q6pbV6oUme_6fh5kpywlLNMlGAGPj1ghz_qA36kNRvol6mrUf5rbwdXC3kUWrvEFDV2qYfYpUE4Te_re4Ier77M1X_4Qq8U0yN_4roWrT21oa7pYJ_grpbVNNl9Ndw_iK0s0VhKB8jYvVCV-gDoP1GsdRBLIGFXzNoV9V6euR0bpm9fk5-ZwG7kHWQJDZsqgBQ1O0Yxa9E0K5WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌اکنون؛ آخرین وضعیت تردد کشتی‌ها از تنگهٔ هرمز
@Farsna</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/437667" target="_blank">📅 14:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437665">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qvslXMBwcIYV7VUihk0_khpHMVa6xOBtCiQd8DRvb-vgwKYiGuW9rL2v0C9bMiFBkjB1hKQGLBhIQna-Zq_Bq_ZYOxzG8Y1YHyYGvVU3oTu6dpcK-liFKJ3GLi3oKsidl8pR_Zb4b8V3G70uw8KWBwr1kIBv7nNmgkmBRu2IjPP1Yqv4Mes-Co5lFVLurIsBqVjJczI8VFY2mCIuQyYsQpuey5gjHbFU7OhOkyRQLnKk9oc4gkg9fzTuBGS8uUZ6gBsx3mbeIS0SPEu3kn2rssCRCL8opD9gvb6_be4egzHEXaoLC8TZnBhJ4MxYB5b_O5ElE7mbh4nTeSPTPLHRHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EZkLws7E0mIakiRoyVwVRs1w36X9sXIkn_6MOA2l2a3hWgDbE0KYGumrl5_nuKTVAk0rWdZaKJkNyFhV_zs1SbjLwFki1fhKr9g0N0FT0bOsjjfXLaLuyZHOxnUb2GnN0az5_Qjq2beZ-P8R96gyrFQpBVHDdngdI5JkMP15HjBhn4KsbVkWMXh84P2Hx3mbvF74tAHbknVJz_2wlFyNI6wLlWrtD3Nh9-Gzs9kEr6JcNOmF5wBLoeXRrFm-GBI9UJEgD_rSdS6F_NVJb6qs4HRD2r0SdNkHelDgLGqldAnXCBtYla4FvudsjdELWQtD82W9k2zUPhb8_gi_97Od6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاربران خارجی: جنگ ایران نشان داد آمریکا بزرگ‌ترین حامی تروریسم است
🔹
مایک جانسون،‌ رئیس مجلس نمایندگان آمریکا در پستی در ایکس ایران را «بزرگترین حامی تروریسم دولتی در جهان» توصیف کرده بود،‌ ادعایی که با واکنش تند کاربران خارجی رو به رو شده است.
🔹
کاربران شبکه اجتماعی ایکس با اشاره به ترور شخصیت های علمی و نظامی ایران از سوی آمریکا و هدف قرار گرفتن دبستان دخترانه میناب توسط جنگنده های آمریکایی، با رد ادعای جانسون آمریکا را بزرگترین حامی تروریسم بین الملل توصیف کردند.
🔗
اظهارات کاربران در این باره را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/437665" target="_blank">📅 14:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437663">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2-73GK6mkTGG5sykHdcnZfNQsSFKQMV_2XynuoWW7wcTIJ2Uqj4FWvGEJ_F8_CxmRHxs9uw4hENwpJ4CvSDfav80s7ecoXjG4h4uhFX-Vm2fJViQtOIjBjXPSl7AmkHHvAAl034tS3MUrRjnW3ooEdlrnE8rpoY9JW_wA96FZaM2gSKuXn55IdWIiKmQnkAlfanQtOq78S7hShvE-tDT2FuQA-s909gGg8Y48JMc9RvZLXqHvSw8NAqe68z8I-rR90JNyYLE8GVWXwg9PdSHxgikJkdV5reiY5bV2ok8_HXseL5uoffou4geAHaNr8auD1SWZqskzLy9O7bGLMEmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حاجی‌موسایی: برای شادی دل مردم سخت تلاش کردم و مدال طلا را به شهدای مظلوم میناب تقدیم می‌کنم.  @Farsna</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/437663" target="_blank">📅 14:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437662">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/719dc5b594.mp4?token=JenCPynVlwuuVYGJq4T6sX028DyFsf1hvEyzATq4gbbLcC5Mt_GmVGwysmATzNLcrFUpFruYy9FUiAJ-JpWZe7CEaj8Dcr8PeC921jAXp62kQzzxQqqUlRJkbVAd6XQ4Zr9M0u2vTV2pqCbYlUPdcfdr-YtWyC4mlQhUx8G_ZcsYjWdHO31ah8HO7vxoP0DlFIlJoAlTw2dIxMCfjHptmhsa6KqCZxrrDOMOs-qBA-Hw_Nz4JCGfeZ53qWQ9g0IFYJ21dkGqXpNIEUk3eNBKRhujIMpoI3ncLnPMWLqifKZIhEiNYsOy72tNDYfFNSfUH7rLbLBJB_glfd_0TZAsTIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/719dc5b594.mp4?token=JenCPynVlwuuVYGJq4T6sX028DyFsf1hvEyzATq4gbbLcC5Mt_GmVGwysmATzNLcrFUpFruYy9FUiAJ-JpWZe7CEaj8Dcr8PeC921jAXp62kQzzxQqqUlRJkbVAd6XQ4Zr9M0u2vTV2pqCbYlUPdcfdr-YtWyC4mlQhUx8G_ZcsYjWdHO31ah8HO7vxoP0DlFIlJoAlTw2dIxMCfjHptmhsa6KqCZxrrDOMOs-qBA-Hw_Nz4JCGfeZ53qWQ9g0IFYJ21dkGqXpNIEUk3eNBKRhujIMpoI3ncLnPMWLqifKZIhEiNYsOy72tNDYfFNSfUH7rLbLBJB_glfd_0TZAsTIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
نشست پزشکیان با مدیران صداوسیما  @Farsna</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/437662" target="_blank">📅 14:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437655">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MkEKWmUcdjbjFN3eNmUAaa7evbwghQaHED1Sq0-E3Ti1oui1GAjeIQ42QBAG3gbPnBpmFdYJ09UR3X6vufc2UfD3Qq2EfqgncJQ5YhKUIxMJrwgYXjyo_bO_cDAyPl_8pjuPKRNsrJOnCA2kjhdkC6i6WKrxCEMIh1OHv9w_Z2V1rZUc6MLl4zxvojlH-J7PeBkEOwsUcaL_PRuImfrndbU9XQglD-VwwxQic5ACyghg2Qpg936dAbDTZLvLb4FsdOaEWGSdGh42HlvtoGBrDLBH28HyNgzQKPXokGcf65iOT4DCBYhSUqYo57YthKnisPzD6ZYt5JezeWi2vdIhew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JmhlbQaEaRJ602UKdR2F0MoCnQyRYtVU3EIxzGL28LBoEKDSa4hBMlUH5VnfgcHM24U11kNCe4mFINXV66y9sMcsI-Ce9I9tQttvBZEjYIeJ4bQZt5i9ahg5Wh0QQTDzOYvNIvczgAK8BNhq78BOCu8s3ukzdPHRKu1YsErCLPFpy58EcixWlwb4k3m0dhYFaPMk0iLuVE0UZl8eZZPVyrWUanOsklcV9vEWEjaxv5KBBIey1Yv83uy6UWJy8C4quY8tZWJ-23C-QWGVoa-T8-o8CmoCHLn3DBy6GYenqDCwqKBMnhdacIAhs5snDgVIglJiMkiW8OfU1zhdbrLFNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AZK9EQYnCmoaXo2uAHXeXjmMbXSCgFcHs_d0QEwBM-44NvzDfVnoJ6YfU5otN0R0R4oJQUs0SQxxIpsvzXYeFtrtqc7-AqrmbhH7Y0o5XUGdX9az1xPC9nRsgMYbNNvQxD15lUp2Kph_i85AZ-ww2h_X03rInwa2JAsiyvkqsi0ta2DVLpUeQqfG9s9UV9vjLOrzIDi9MUHKTkrL6qMiSBnJzSQV6GqxGC3ZV7mY_LSRi_1-lr3yOpygJ7QrvQaqVKjaoUeRQ11fkOCTbcVQLuDNKwZ99tpHa-NvklDs1RGvmFvi0ZKrk3BCxcSQjBQw_arEeR-yy8OAaFKvKjdW2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_kuzd2iB2Ki41B8FXUy9g7OjNGGTVjBD9cTINYh1tWZG8HOcjj_8Ro9quNG6OnZGjScyJWx3kL06nyWS1nRmSHghLo2bmnsVzELu42uPdLTF_M0ilsOLNB6vitySn94yQjTcozChy1HIx_uoXpAoyGSZVPSK63Bp-mc1ZLN03nisW60X-xK7TQD5Pw1guB3nWTaAjhG817UE7gJB7PRA7nnlrQXMjj6zJauYkG3cUW2IhbGEkSLbNkmJmkNGXcU2NmMxYfBPf4guVo1CvBMc1NDaVrEtW1bQw2EVpXTV6wxmNcRYUInVxG-uHQNTSKES3pxNbUjgc0LsZ9WtG0Ivw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MuhznwlL99cnIz4eYtne5E9YwEfNfii6oOKPilhOt_bVhDteQ0wt20fZrskrLICe2ycjDc8fp78qbxKyDYXh4NYPCnbf2-zEAeX62-778KIXFgH0ylDmmrd3vCH4ZjDKBYFP8uGVeyqt_tMa_oWYlsVxJiB7lH_VIx14H5T_XcjT9Nm-fhGOs8OonfZWld6o4cnzKd2zu8YLWHqMe1kVEK76L8m1xeUblnGz8BCbGGn7xe4xv9S0OPVDronNtBcW8ur6Y07ZiocHSSlBo8-vF5NXCqwECzt16SI88Lt47-mjHwGvXRre7gKSfXDxmdl41Ax4SCd3HpPsAJVsnM5PXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E-udEcpq0Tu9CANJMcnAYjj9rm-GJlD_xxRKM0NHZWOzOlLm9UNKygv70i_pqIPfD_iuSzG_XTnbCvoCUUozqszkowgENNkfr_EORVeLuqvzr6yEID5RFFQDZi5UjUjaYTxmE4GAyw6vwzMNjFE8wG1MA5gEiWq8AX4c7MCYRN5PS0jE33OS6u5-TI6saVShaVKsbXSeacyQ7NFSKSzUxnkjGN8ew0oC3tZiE-UG8JfSwP9Y8Ff7E7Pxs4P6-PARcCRRTZa_K7Y_GPXbQ0-8LxA-dU0D2aMSaXBK2ZBC4nn1u6WRF1SjpzDia3o1193fmL35siaWZOgtXbe2Z6KizQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pdnvUJXia4U6lFtTkXPdzElzrYvxDB8Dn8w1aG8z00ZmHPvRkK0gVxVHdWoTL3l1o1eoOR6HaRRa55aCgml6wj8QiSRIfDhchm-EBRm6vg8j1uwcUfr-ror-Ca4StYrM8VhyZZh8ktNIXDmd0I3yfgghPuiob3Uz6ohOKGxnI2ZQCpzBRZPXUVOBZ7oZMMp1rn5M1hMZCIOWtqfU8MKqbegAeROg6OTcWiQ10nWicmvg_3Oiole_QIfdEY6vjHM1dVJiGVnY1mMhyzLBLQj7qShWZD55zg9jJbjiuYnSJouhVxSc9wiLc0yV1wv6Ys3LwnbOFp84MsUwabk2xF980g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: دشمنان این سرزمین راهی جز شکست و خواری نخواهند داشت
🔹
کسانی که بی‌شرمانه چشم انتظارند آمریکا و رژیم صهیونیستی بتوانند به کشور ما آسیب بزنند و تجزیه و نابودی ایران را دنبال می‌کنند، باید در برابر وجدان ملت پاسخگو باشند. جنایت علیه مردم بی‌گناه و کشتار…</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/437655" target="_blank">📅 14:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437654">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTs66IKUIDpI7F-moMnhnA0QyG4_nRk68qqmeNi1Ic9IabeNYyg_VrfyfUM25lfIurLM-tZ-VwArGXFLhkfz42znoHP6V7aYNV_8V_5ZEOoY_cw-ROEaEvu7kFjYxVx_K6gAf75CSTJ9IkBuTDTZLSBCr4bxnEtZk46VDbnsiPkReaXfFNFw0ty6LoM09tFJdBMOmklP-Izl1TVfW-GuQE84Pta_PW8WE5jkp9b5xDWVF0W8al0WjlAOdL00CW8UremSzuugGVk-hDYdyFYzk3oVw1QPY5Nhhan9WYT2W35jhcJ4RYw3i-QeUkbLvuuwNzzg9AlQP0_PPGiRuDQPiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
اهدای مدال طلای ناهید کیانی و پخش سرود ایران  @Farsna</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/437654" target="_blank">📅 13:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437653">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXiLCgkCzwiQKZi2OnP546A4YSugFoBKjJNFVw-xn2UdN1Aq6KGMrDH6w21hePe_63VacmomxV_cZ5ay8zq0jQHwQxbtv0SZyqZP31pJF_UrJkKuoxAYm3iu_jj4Qsy44DqYy8DrrnEvkx1Cca9Kvu19WyFahwZIpjRcZUhunbAAy_T6977-woo3v7by1aCEd3o6PWrVHaKcdUsXuO_f-aLNzTHNEQGcu_fw3dm9YyyTvhQBt3KC7_847MBmc2VzOds6L0AOb2Ob9m7mNBY47pJpPSjqeemo-H1dpPA7laXeZFmsry1gAhOZ-cASt8SSMVIqZogMZK3Y-XRklfzjbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الزام ادارات تهران به نصب تجهیزات کاهندهٔ مصرف آب
🔹
سخنگوی آبفای تهران: براساس مصوبهٔ مراجع ذی‌صلاح، تمامی دستگاه‌های اجرایی ملزم به نصب ادوات کاهنده و رعایت الگوی مصرف هستند.
🔹
عملکرد ادارات از طریق قبض آب و بازدیدهای سرزدهٔ سازمان بازرسی کل استان ارزیابی خواهد شد.
🔹
کنترل نشتی‌ها، عدم استفاده از آب شرب برای آبیاری و شست‌وشو، و خاموشی آب‌نماها از الزامات قطعی ادارات است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/farsna/437653" target="_blank">📅 13:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437652">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSK-E4i6t9K1gE0f-qYAMENjZrxHksXM4QL-ObRvN9kldKCXN5cbk_KtjQVFanFyx3-AhS91Ar38Zncc0R6vJAGiSvmP6NX-aOBv2M7iwlDKMoWhtUSnIWI_3SFf_aHWw0gtoBeELdheATyXkE2Fxeek8tMeAkbYr_73u4GwUljRJngr7SdB3WmjJRTc5z8S856OVpozEGPJGWeXFi9NTS8Luy2EK46YXgdtpb7f1nkmZpTed7Sc5vT_deavfvqPttPERriocRwHkwoiAWQtS63dnPCcGGE68osUAtwKgTe0YQlurnb_QphJr9CMwW-FsyIOgCqCgENicYhWUbgKlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: هلال‌احمر می‌تواند حلقۀ اتصال سلایق مختلف اجتماعی باشد
🔹
رئیس‌جمهور در نشست تخصصی با مدیران جمعیت هلال‌احمر: ممکن است برخی از افراد و گروه‌های اجتماعی به‌دلایل مختلف تمایل کمتری به همکاری با بعضی نهادها داشته باشند، اما هلال‌احمر به واسطه ماهیت مردمی، رویکرد امدادی و جایگاه مورد اعتماد خود، می‌تواند زمینه جذب و مشارکت طیف‌های گسترده‌تری از جامعه را فراهم کند.
🔹
باید به‌صورت شفاف مشخص شود که هلال‌احمر چه سهم و ظرفیتی در مواجهه با مسائل و آسیب‌های اجتماعی و محلی دارد و تا چه میزان می‌تواند در فرآیند حل این مسائل نقش‌آفرینی کند.
🔹
مبنای هر برنامه‌ریزی باید بر پایه پاسخ به این سه پرسش کلیدی باشد که «در محلات با چه مسائل و چالش‌هایی مواجه هستیم؟»، «کدام بخش از این مسائل در حوزه مأموریت و توان هلال‌احمر قرار می‌گیرد؟» و «چه میزان از این ظرفیت بالفعل قابل تحقق و پوشش است؟».
🔹
جمعیت هلال‌احمر به‌دلیل جایگاه اجتماعی و ماهیت فراگیر خود، باید از ظرفیت نیروها و سلایق متنوع فکری و اجتماعی برای توسعه مشارکت عمومی استفاده کند.
@Farsna</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/437652" target="_blank">📅 13:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437651">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‌ اسامی نامزدهای انتخابات هیئت‌رئیسۀ مجلس
🔹
اخبار واصله از جلسات غیررسمی نمایندگان مجلس حاکی از رقابت نزدیک گروه‌های سیاسی برای تصاحب کرسی‌های ریاست، نایب‌رئیسی، دبیران و ناظران هیئت‌رئیسۀ مجلس دارد.
🔗
اسامی نامزدها را اینجا بخوانید  @Farsna</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/437651" target="_blank">📅 13:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437650">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‌
🔴
فرمانده قرارگاه مرکزی خاتم‌الانبیا: به دشمنان هشدار می‌دهیم که برنامه‌ها و راهبردهای رهبر انقلاب برای مدیریت خلیج فارس و تنگه هرمز، آینده منطقه و نظم جدید منطقه‌ای و جهانی را در سایه راهبرد «ایران قوی» تضمین می‌کند، که بیگانگان هیچ جایگاهی در آن ندارند.…</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/437650" target="_blank">📅 13:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437649">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پیام فرمانده قرارگاه مرکزی خاتم الانبیا(ص) به‌مناسبت گرامیداشت شهدای جنگ رمضان
🔹
حمد و سپاس خدای قادر متعال را که به ملت ایران شرافت، کرامت و عظمت بخشید تا در حساس‌ترین مقطع از تاریخ نوین بشریت، تحت لوای اسلام عزیز و آموزه‌های انقلابی، با مقاومت و ایستادگی…</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/437649" target="_blank">📅 13:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437648">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پیام فرمانده قرارگاه مرکزی خاتم الانبیا(ص) به‌مناسبت گرامیداشت شهدای جنگ رمضان
🔹
حمد و سپاس خدای قادر متعال را که به ملت ایران شرافت، کرامت و عظمت بخشید تا در حساس‌ترین مقطع از تاریخ نوین بشریت، تحت لوای اسلام عزیز و آموزه‌های انقلابی، با مقاومت و ایستادگی در برابر تجاوز دشمنان در جنگ تحمیلی امریکایی صهیونی، یکی از شگفت‌انگیزترین رخدادهای تاریخی را رقم زند و مقدمات هندسه جدید قدرت جهانی با محوریت ایران اسلامی را فراهم آورد.
🔹
این مقاومت و پیروزی بزرگ نشان داد که باور و توکل ملت بر قدرت الهی و تکیه آن به توانمندی‌های بومی، بر هر سلاح مادی غلبه می‌کند و مسیر پیشرفت و اقتدار راهبردی به سمت قله‌های رفیع عزت و افتخار جهانی در عرصه‌های مختلف را هموار می‌سازد.
🔹
اینک در میانه دفاع مقدس سوم برابر دشمن، که کشور نیازمند هوشیاری و هوشمندی مضاعف است؛ تکریم یاد و خاطره شهیدان اقتدار ایران اسلامی، چون شهیدان همیشه جاوید وطن " علی شمخانی، سید عبدالرحیم موسوی، محمد پاکپور، عزیز نصیرزاده، علیرضا تنگسیری، ابوالقاسم بابائیان و....الهام‌بخش ایستادگی و پایداری ایرانیان بر حقوق حقه و منافع ملی خود است و همگان را به ادامه راه پر فروغ شهدا و تبعیت از خلف صالح امامین انقلاب اسلامی، مقام معظم رهبری وفرماندهی کل قوا حضرت آیت الله سید مجتبی خامنه‌ای (مد ظله العالی) ، فرا می‌خواند.
🔹
در این مراسم شکوهمند که بر تداوم مقاومت و پایداری و هوشیاری و هوشمندی برابر دشمن امریکایی صهیونی تأکید دارد، با تأسی از رهبر عزیزمان، “ایران اسلامی با شکر عملی نعمت، منطقه خلیج فارس را ایمن خواهد کرد و بساط سوءاستفاده‌های دشمن را از این آبراه برخواهد چید.” و “آسایش و پیشرفت را به نفع همه ملت‌های منطقه رقم خواهد زد.
@Farsna</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/437648" target="_blank">📅 13:34 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437647">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYlOvaCIq7JPtopy-xKUdbnIRfQ1CIW22BZD4_zoWOew42RhPRGUHdwnWESTdQnsTRoOTd6IPzyHzoh5DTrAULgQygrKXW07R_Xst4UMpBDNEHj8MJWFP5RIeqqTSktHANT54_kQoJm4kG40oMOdXD1KVlCci70rA3iKvSaxav7NOygVuTNQ2YAV98fZ7A5HGsKaRNR791rny3830UQaeCNUdNIFIRLHsr9TzoPzfRPVaRuw0Cv-p3KFhHZvUCh7U7GSbnVC6JQWcNE1sPNj1xRfh1jySWntQ3-0kOkW5KQAtWpuj216DFGzNxL23SqAxA_8nWnLBUW8G-R24fOIRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رسانه‌های آمریکایی: فرد مهاجم کشته شده است
🔹
رسانه‌های آمریکایی به نقل از سرویس مخفی آمریکا، از مرگ فرد تیرانداز در اطراف کاخ سفید، براثر جراحات وارده خبر دادند.
🔹
هویت این فرد هنوز نامعلوم است.   @Farsna</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/437647" target="_blank">📅 13:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437645">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‌ احتمال دبۀ آمریکا در یکی از بندهای توافق اولیه؛ ایران بر مواضع خود ایستاده است
🔹
درحالی که مذاکرات به‌سمت توافق اولیه پیش می‌رود، منابع آگاه از احتمال بازگشت آمریکا به رویۀ قبلی و تخطی از یکی از بندهای مورد توافق اولیه خبر می‌دهند. این چندمین‌بار است که…</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/437645" target="_blank">📅 12:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437643">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bb3b7b57f.mp4?token=A9ZgF7MMuLjT1Z53Cjw0FSEG5cURppHvRTpqlDUkM7qYG4hP6qr9CQPt8m39Wajy2IcEf8ko1dYXLEIpcIdVRcvqdcj7G_PjOHbHlTrtPFdOtLWyc9lo32ByHpYi9xvyds_fVgBYAHm0h3whbVXzW6BdJ82F18z_8StzFbKkkPKxLN7qfvEyxpOIsAAjL8BGkdsp1xaja9R5H_ZT2mPWgRW1ITQ3PNNA3ZFjPb4Z7TWfBObs-lqSBexHwGX44X1at2k0c7m6NfUxGGwrLJTm_3SQvJCt3F5nDFuGex6vjd3U9DF8mkQPTtGGp2-FiXiEhykPT_1YALBsAfxRd49Alg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bb3b7b57f.mp4?token=A9ZgF7MMuLjT1Z53Cjw0FSEG5cURppHvRTpqlDUkM7qYG4hP6qr9CQPt8m39Wajy2IcEf8ko1dYXLEIpcIdVRcvqdcj7G_PjOHbHlTrtPFdOtLWyc9lo32ByHpYi9xvyds_fVgBYAHm0h3whbVXzW6BdJ82F18z_8StzFbKkkPKxLN7qfvEyxpOIsAAjL8BGkdsp1xaja9R5H_ZT2mPWgRW1ITQ3PNNA3ZFjPb4Z7TWfBObs-lqSBexHwGX44X1at2k0c7m6NfUxGGwrLJTm_3SQvJCt3F5nDFuGex6vjd3U9DF8mkQPTtGGp2-FiXiEhykPT_1YALBsAfxRd49Alg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دور افتخار ناهید کیانی با پرچم ایران  @Farsna</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/437643" target="_blank">📅 12:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437642">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ymx6s6F10_1X3t8LN5F00Upajhq4kUB4jWSKe9GQ7tgR-mKWqWXRrTHmZcFI6nYl8WPFrh0dgU3aGvm2n_hF7YLNtAWG89vF75biE2DKfkNAsiv5gwZ0LaOmrYAzfqkuvJZFAhDCGBXqYTQWNqb6Xofg9XoCxmXAT5-7qAc4ozlR-lApxlUcCbVzsYe0iO1ojeV6TA9nG45qUe9upjUKEYBW64IOGe4TqdQNpqskUq8lmoN95DWB3Qs8qjOgG9giVe5qC2MCDvx-SuOLqn6Bx3J82Z3dyfLMnimKFQUA6LgXI7_77BU-gbbJ4jsZ1X4oVfB177tY7g0y_-6ER3ZssQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احیای هپکو میراث ماندگار شهید رئیسی
🔹
مدیرعامل هپکو: شهید رئیسی در ۲ مقطع حساس، نقش تعیین‌کننده‌ای در نجات هپکو از رکود و بحران‌های کارگری ایفا کرد. اول زمانی که رئیس قوهٔ‌قضائیه بود، با پیگیری مستمر، در سال ۱۳۹۹ زمینهٔ انتقال سهام شرکت به سازمان تأمین اجتماعی را فراهم کرد و از سال ۱۴۰۰ چرخ تولید دوباره به حرکت درآمد.
🔹
دومین کمک سرنوشت‌ساز شهید رئیسی در تیرماه ۱۴۰۱ و در بازدید از هپکو بود که دستورات صریحی برای حمایت همه‌جانبه از مجموعه صادر کردند تا شرکت بتواند از آن دورهٔ دشوار عبور کند.
🔹
همزمان با پیگیری‌های شهید رئیسی بیش از ۵۰۰ نفر نیروی جوان و متخصص جذب هپکو شدند و امروز هپکو یکی از بهترین و بزرگترین صنایع کشور است که در توسعۀ ملی نقشی مؤثر دارد.
🔹
پس از اقدامات شهید رئیسی،‌ صدها دستگاه ماشین‌آلات راه‌سازی، معدنی، صنعتی و سفارشی تولید و نام هپکو در پروژه‌های عمرانی و معدنی کشور بار دیگر احیا شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/437642" target="_blank">📅 12:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437641">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌ رویترز به‌نقل از یک منبع ارشد ایرانی: ایران تحویل ذخایر اورانیوم خود را نپذیرفته و موضوع هسته‌ای بخشی از توافق اولیه نیست.  @Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/437641" target="_blank">📅 11:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437640">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvW6gM4dVfHYS7LAfDZHPRznwkQryqDazmF2yc3XlJu1S7v6IaSUNXWH_4Z-0pICsfAMQZp8_dRW7ADa0KSzelp4z1HtPtN-GZyqwEIX6jqmSMGyYDBgJNeNx6D4RnPKzcsQnqvWG95ITYM-DN3VcKKRc3HRIGS_6yhBeOU86fOsZSxR4jmaUJUNTbRyU8jcr-LaAcSgyt6J2clX6-ifFoUgTLCN6xmVNu6j_x0YppVz8Blojk0B-9HYT2Sf-dGNN-DIawC1gqgD0t8Eg4D6biQ92L42sNO7Qf9gwQlMxwWNm458CsxCNgcEANculNg0aw1zazI9OSyHJ1HQ1g_J9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهره‌وری نیروگاه‌های حرارتی ۴ درصد افزایش می‌یابد
🔹
معاون سازمان بهره‌وری: راندمان و بهره‌وری آب و برق افزایش پیدا خواهد کرد، به‌طوری ‌که بهره‌وری در نیروگاه‌های حرارتی از میانگین ۳۹.۸ به ۴۴ درصد افزایش می‌یابد، همچنین باید بهره‌وری نیروگاه‌های جدید حداقل ۵۵ درصد باشد.
🔹
قرار است در برنامه هفتم میزان تلفات برق در شبکه انتقال به زیر ۱۰ درصد برسد و تلفات شبکه آب‌رسانی سالانه ۵ درصد کاهش پیدا کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/437640" target="_blank">📅 11:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437633">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oAwMt89J9_5ojRLhmBhVUix1MyZsKtvRr3cJEhuCvpy7vdzR-Aml-DtGtxlHQTQM624kHw6_xg_jg1DNVP3TahXyya_Adp4Oi-S-l40_wCY-0YRTafzy-jqRS6q75iTihYCnWjB0uyikoCjykI6sHFfMB4gFqMKMrIfgVVvAwOIgEILs8VV9vBFy-lyWgkaI_dbAZq7UdhBC0oksitpjJMS1BEoO8Wa5gL6HFvKuc7XkH-wwbE9RoWhcLBjHrYICj_1bDCZyybhrgvm7RigQAG58PeybZyt-CKNXl8BaYOvfkNe4ytSbSJzwMqBw3NDG5939YBJEcrMNL9z5qkW_6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HDk382UZaTq1w8703PXE2mKDNs_2ZXgsoxFFVO91Ti99AloMrmS7tGQhEvz0181D8NC80ymw0ATaLLyKQQUEH406pcxbjwH4MYO45pRtJqBdCtyYI3PLnpgnc13PMyJq6GXqvLGBCEWwUm-HqolC_aAvydcNajKyWfqBLX60WTPEBGUi-SgRHDrPcaaRqiXmOfdaRqZHe2Mu7X4cqFBO10SkPU_ybPPqca-FXzJsJo1fpI01_5QFulYl65TvimS17cVSjQzP8KZAds8_Dlcv2ctArWyx6q97rVdM8m7Ao4FWGE61hU3ttT4DuM2a_crh6Sp_nxOlvLMMd_bHR1GMpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jASwg4s9j4OfX8ZkN5Xtxn_12AF3nZNhFs8fzBzpU7JAG3WxDc7JnTrePjiSfVUtkLvtCzJTBJYrENvvHBDJEiovsAuDYMU18lhyIU7sX1lTFieg9yK09076fNOu6PsNdDPaZ9CxfmzqIPHvHE1m1B64sI0_gHZlrCpGZLsD__xj9lqxLITun8kK244ABjoujhBzn_7riNlmqUDFRRHqDybd_CQeNXmyDjAoCrY8P-6kx5kMhNbrgNNyxxnVMVWklinIQ29JXcKKJQQS7DmSly5FxhptAK-LsINQkDL39akk4JCa7-R3BKSLjWAApkWdI4pKMWbGH_9n-n2XSUzG_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PeWVyomyLSz1Dx04If6AyKZxj8-FfgCBBsHQ-t8zRDCmqoSVl0uXQk7QoMgJviIBBK99Gye7S_VGViY5_FgdBEwXd73Z5tIjG6taW9tbacXbOj1gmDOa43n69QBWrLLDRotEMDSbI8WwpjXwsDpvMX6YEwiyqVyhGEbF0bTqUKFz94GUTSA0Y_chLJy6MYtDUWxkf5QYU2MpUNJldMMIo_ed08sf6T7LshGFFbIxvIMi3tCkbyF_Izy2tT6HDIXomsEDkJA0c5Xv8NaFln6NoU_Dd2f-cxKsVJ5YN6ygaPVslR1vIhAJA_6rDdyzMAJQa4ZMpVqmxSLOwq53XREOEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jYZeUzk4Bt6teikPCYguUCnrPdLbgc3sZhIuZyQkUQuF7ygyqyhKgxm8VLz0Zbd7OkCZIpLg0koMZInrFPZgKEzbUKwFkY0l1ruamipd47vRX6dzbc6jrW2AwccXAjeRYYqkHrsccrtJ29lzRrF58CSosb6Ubur3Wkjr8Q3_ua183k7LMDr3xGR72xMwYtMIGIf31TEvC-ftYjzX2ooEeE9JeLti0m7Fe3mZyscFV2Pqr6TowESf4nqTI65EKqXpP04wt--UVsR8LiiV_DBMXK2mOIh5R6i5pN_TjvapZN8algXa7-TGX3BDp-6qovZhGkjRg_CNspuZQZ6EjOGMQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AfW7IWKBftP3uzgjyeSouiHbBdD3xWASKu-F1dlNP4fE7RWoXHrDf4nZgp7sjndZfCvpFFEEJuKFOR4uv1QcjyJfUOH2u1lE1UZyeW0EFl6U0iuQBs2azM2N0XKdGLz5tzUkQzmSn2dzGNKOLuFJjINuUCjF7nIFLwsorztKAOz90nnI5EPpbLEClUNRrkNXEe9o0LS8sXUWg1kZ1_91ABWF_JMck8eAqmJRRSzyegnLmnvXo256wT0IkzhiGMn-bfBqxRXf-LlKDY4FnJrUxQ3m4kCJ92R6cfmgMsf-8WiLTzgPsuR1o4zBFeYfGylLLB7J1_hUXU16EP8WM9rgBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWFJLyl7crw2vGaaK0VjGBDCtazYjg26qhC-tsmo1kFXJP_7t4RlY2BL0LqVYFDLguv3BdHrUgZm7iTyygHXlWFNiY5I9DJ8r-DqMhDVhcC8BzyYT5P7-oKeZJvVq2IFjVO22ytRdIwsA5EF1rMdaMbfiIFHk-mziVfQavzNSE5QyPIcN-f2pdK_rmxQODroc4xWj5Jib4JJtyHkUAiSohPK20pbY9NUCA-waaqUuDVFkFf53oPEvCZxazgsD_NPyAVQVUcFFRj_JKz3NcLdAPJWNPND0HCBLhp7AAJj13hNeHJ2mdQ0cHWi6bfYrV8cO5C3CXdMFCyaY2Ox4H8l6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین سنتی عزاداری مسلمیه در حرم عبدالعظیم الحسنی (ع)
عکس:
احمد بلباسی
@Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/437633" target="_blank">📅 11:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437632">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌ پیش‌نویس توافق فاقد هرگونه تعهد هسته‌ای ایران است
🔹
برخی رسانه‌ها و مقامات آمریکایی مدعی شده‌اند که «ایران در توافق احتمالی با واشنگتن متعهد به کاهش ذخایر هسته‌ای، خروج تجهیزات یا تعطیلی تأسیسات خود شده است». اما بررسی پیش‌نویس نهایی توافق نشان می‌دهد این…</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/437632" target="_blank">📅 11:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437631">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f0108625.mp4?token=NiLIM3DVUKHVuOUOu4LXgMTNrWPoValLNXAsUxqM-GGFtLMC1TM7p_sec0z4FbtYuzDyfTBIjUf2WdE-rbw5_JItzYG5m31WAAB2Os2BmwzaqebKMnpiwGgOym5e60Z6YpkKc1W5hDkFmQyJXZYTo-c90jbOnEa0LTlXFBpw5dYnegg-S4-ib27rYA4nFU31cfIW-M-Vcs3Ee_XKFDDANfOzagSFG53lyz_D08WsPdS2d0llKDizOFdpoXRLN8_YDXHSAtPs9CRBm-y7ixM0pL4TE4G6I7ulD63biVDYJFVaCjH09bJOUlM-kmEzxdq8_YIbgJ7ShOZdSIx2tIQS3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f0108625.mp4?token=NiLIM3DVUKHVuOUOu4LXgMTNrWPoValLNXAsUxqM-GGFtLMC1TM7p_sec0z4FbtYuzDyfTBIjUf2WdE-rbw5_JItzYG5m31WAAB2Os2BmwzaqebKMnpiwGgOym5e60Z6YpkKc1W5hDkFmQyJXZYTo-c90jbOnEa0LTlXFBpw5dYnegg-S4-ib27rYA4nFU31cfIW-M-Vcs3Ee_XKFDDANfOzagSFG53lyz_D08WsPdS2d0llKDizOFdpoXRLN8_YDXHSAtPs9CRBm-y7ixM0pL4TE4G6I7ulD63biVDYJFVaCjH09bJOUlM-kmEzxdq8_YIbgJ7ShOZdSIx2tIQS3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فعال اصلاح‌طلب: اعتراف می‌کنم در نقد به دکترین دفاعی رهبر شهید اشتباه کردیم
🔹
علی باقری، دبیرکل حزب عهد ایران در گفت‌وگو با فارس: رهبر شهید، معمار بازسازی قدرت ایران در جهان بود.
🔹
عملکرد ایران در جنگ‌های اخیر و مقابله با قدرت‌های بزرگ نظامی، نتیجه دکترین…</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/437631" target="_blank">📅 11:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437630">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f142fb35.mp4?token=f0f4PNXCUPo7nOJgpkX-bsmJ6wKOHyhaZ4d0kCS0MvA1ui3kbnADEc8Ar-OPuTK7jkos2QNerQgyZfj6q0q4RRp0pW2Dx-oy7w8bF1TFK53-PynOOxelJJhgU4pznt_wZZtjx89ZR5AJ70dpgh33mT3O8mz4fwNAbBR8XmY2oA0sSrQK0Qk5L5WnVQsg2fH3-i4fnC1tG63FCUTi9HEBF1fhbKkpRGc_7JP8fdR4xw5GnkIZrdypUfs6o33B6hLlxT5fl57Z8A9ShmgOlYNBeFgfJ_sOfLqyTcBnhhuU54sXWHVbGSycytuGbNMAXGQXL9kdauK60dK5wvm34xNvHTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f142fb35.mp4?token=f0f4PNXCUPo7nOJgpkX-bsmJ6wKOHyhaZ4d0kCS0MvA1ui3kbnADEc8Ar-OPuTK7jkos2QNerQgyZfj6q0q4RRp0pW2Dx-oy7w8bF1TFK53-PynOOxelJJhgU4pznt_wZZtjx89ZR5AJ70dpgh33mT3O8mz4fwNAbBR8XmY2oA0sSrQK0Qk5L5WnVQsg2fH3-i4fnC1tG63FCUTi9HEBF1fhbKkpRGc_7JP8fdR4xw5GnkIZrdypUfs6o33B6hLlxT5fl57Z8A9ShmgOlYNBeFgfJ_sOfLqyTcBnhhuU54sXWHVbGSycytuGbNMAXGQXL9kdauK60dK5wvm34xNvHTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ناهید کیانی طلا گرفت
🥇
ناهید کیانی در دیدار فینال تکواندو قهرمانی آسیا وزن -۵۷ کیلوگرم، با برتری ۲ بر صفر مقابل حریف ازبکستانی خود قهرمان شد  @Farsna</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/437630" target="_blank">📅 11:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437629">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/255a86faa8.mp4?token=Ns2tqNTYT6wxLze2qHkE0hKd98Ib-eybgZ_F4Q3DjapTwoy_tWbZO1O8k_zHIRSbZJJD-cWTfAaJ6K0q-89EgOtH98fxRLLhFCnn9NwwS1BU5-UWo6zD5iGJEbCOSzxigvIcKj1c-yVmwKDh69rAlnJbPw5MU6YxRCazrM3ks4ln-N0v6yQSPPpIO0mFmkvKQ5dW87choxtTxGamJLOd5VL1dKlsD24j8nzxMr3zOnyEJpkuysGElcvjmqG7upeDyKcW-VJlPgfA_BMBAIeNFj2z7Jhe5X-q9xBw8ivCiLJf2r6d6clPKpmGpVAZTqpp0LuI8pFH0eN6QwRRD4hGKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/255a86faa8.mp4?token=Ns2tqNTYT6wxLze2qHkE0hKd98Ib-eybgZ_F4Q3DjapTwoy_tWbZO1O8k_zHIRSbZJJD-cWTfAaJ6K0q-89EgOtH98fxRLLhFCnn9NwwS1BU5-UWo6zD5iGJEbCOSzxigvIcKj1c-yVmwKDh69rAlnJbPw5MU6YxRCazrM3ks4ln-N0v6yQSPPpIO0mFmkvKQ5dW87choxtTxGamJLOd5VL1dKlsD24j8nzxMr3zOnyEJpkuysGElcvjmqG7upeDyKcW-VJlPgfA_BMBAIeNFj2z7Jhe5X-q9xBw8ivCiLJf2r6d6clPKpmGpVAZTqpp0LuI8pFH0eN6QwRRD4hGKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ناهید کیانی طلا گرفت
🥇
ناهید کیانی در دیدار فینال تکواندو قهرمانی آسیا وزن -۵۷ کیلوگرم، با برتری ۲ بر صفر مقابل حریف ازبکستانی خود قهرمان شد
@Farsna</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/437629" target="_blank">📅 11:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437628">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugo0OuvFXI3FwEw8qulEei93_zFlvmluF9huWegmQOLvqU9lh0QyfwJVyOQEkS8ED8lbs1XDtQQeV_XkBUZOm6HvKbgOWqOtBGAVbWyyf5FFPfzkzivhZfaaKksmNBLf-7F8EgXL8shasmYeBEpOpABbfllLy4qXQ2ZKLB9WecHH6PDwQ0j70ZfsfZOUp3_PJ02CJLZL4_tYYyEk5dKET1N8mTV0qZBUvJrcHjPy7CATZvSrKFxa2HQ1Xm4wHnr1hNtGJEiolHeBhxINHkn1kuZuFVx2bkRZCtGewTBtcJTBFwtYGHFeImbjrQcz-6vf0Bz7rA4nIs-abvDppnnn-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رئیس‌جمهور: رهبر شهید انقلاب هیچ‌گاه با مذاکرۀ عزتمندانه مخالف نبودند
🔹
در مواردی، کلیپ‌هایی از بیانات رهبر شهید انقلاب دربارۀ مذاکره به‌گونه‌ای بازنشر می‌شود که گویا نظام به‌صورت مطلق مخالف هرگونه مذاکره بوده است.
🔹
در حالی که رهبر شهید هیچ‌گاه با مذاکره…</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/437628" target="_blank">📅 11:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437627">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پزشکیان: دشمنان این سرزمین راهی جز شکست و خواری نخواهند داشت
🔹
کسانی که بی‌شرمانه چشم انتظارند آمریکا و رژیم صهیونیستی بتوانند به کشور ما آسیب بزنند و تجزیه و نابودی ایران را دنبال می‌کنند، باید در برابر وجدان ملت پاسخگو باشند. جنایت علیه مردم بی‌گناه و کشتار…</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/437627" target="_blank">📅 10:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437626">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKsp-33YQZacTM6tuWPlWp0hXEdTWVnQGNVQR8kbQugllHSo2zVGXjNgQPlxbbj74WqCfgcbFAm2BWR-DHdU3SHEuNg-e0h31Gwo55CuX-U1jICfWHYaYM-LRlvUndnhbAMGHupS6OarX0xnc82Y7v9SB8_1PJzikXfg3x4rhMpKPCNMwy3YawNxRNbSOYbqmmWjLYQa5KPpylZpmPYPP9lHn1vG4ynjKWU1NWn3OSKh9q-iWSCR8SH8e7R7FU_oKWlxUbPlsUm3q1_8rx7-6aLscq-9Vja9k-3ETBvGDLlSRY5WN8SMmH2cht6fiffNEWqe26XYvEw7GQS0Wlcbxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: از حضور و همراهی مردم قدردانی می‌کنم
🔹
از صمیم قلب از مردمی که با وجود همۀ گلایه‌ها، سختی‌ها و مشکلات، بیش از ۸۰ شب در صحنه حضور داشتند، قدردانی می‌کنم.
🔹
همچنین از همۀ نهادها و نیروهای امدادی، انتظامی، سپاه، بسیج، ارتش و مجموعه‌هایی که در این مدت…</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/437626" target="_blank">📅 10:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437625">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcGY9MpvvkWUlafSLf6lCp4nVp2HNo2zb6gTKZUah7cvQ7TMrvsoI9jVDhe13ox1_hJGJ_R_97ofRI_0oxEWsVRVHpwIpU2fsLHi3ryKdBYzK-a09goby5BEGB6v0MTJIXWIURBGVd-tQsjwzQqTjmh2nXCQ5lxuXtDp_9bJHwJ2-uXY3F_IIf-AorzHaF1wYHMlgWe0zRqs7v1nflZTgSJ9CsPjHoIrDtlrAt6bZMRlKk54QaCWJLE3uHOAre_sYNyJzisG7tPC507qrLnccmIPYFTStkBDpeW8lrXw4R7hJHMRBG7SgzAzquWvyVR-U4CdOFCy9QKfErVDGx-WwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: نسبت به مشکلات مردم احساس مسئولیت جدی دارم
🔹
بنده نسبت به مشکلات اقتصادی و معیشتی مردم، به‌ویژه آسیب‌هایی که در پی شرایط جنگی تشدید شده، احساس مسئولیت جدی دارم و با تمام توان در حال تلاش برای کاهش فشارها بر مردم هستم.
🔹
باید شرایطی فراهم شود که فشارهای…</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/437625" target="_blank">📅 10:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437624">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvN_gGMD--yhAAwsrFEENA24goJY4hg5R3c55VKqkNMYEzAEAT99ezRpzajtq6VB_O_CCzU7X4TJZesfGDPZB9526Iaad_SD7bEeYe78KhcdyybsgGwZI6O8tILAzI6RQJ5ovMAdFtT_LShimrWygLQAfeZMyc_CkkOMNj9SXx2RNntoYco7XZnOnLoU8__8kf1EV1ZSzLnr23J90uYMUOGyb9fI3fszoSn-D4_rKrjrw5N7TUTYuozJ7rB25GpuxJFM6QB0x5rdK2gL918VOj1uRnSU7IeDLaExZx7gTDv_oKfjvKpmQCD_WIWtFizIVM1X-8FmFBC4-REan9Qkzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور: دلسوزان کشور به‌جای نقد وارد میدان شوند
🔹
همۀ دلسوزان کشور به‌جای ایستادن در حاشیه و صرفاً نقد کردن، وارد میدان عمل شوند و در حل مسائل کشور مشارکت کنند
🔹
امروز بیش از هر زمان دیگری به هم‌افزایی، همراهی و همکاری ملی نیاز داریم و همه باید دست‌به‌دست…</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/437624" target="_blank">📅 10:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437623">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSnxHxw8S4Ti2ocUsDLj9UDXOt6BbpdVIUq9aZe7cLaXxUYR3RpFOHj42RTldTBGqbj0KNPziSAvk6cHOCApm8fCZva3b5GW57fzxxtMRFzwjQ5bLiK7S9EsBVnTwmXN4fzpKM1LSpTOKWh28Cu_hAblW3j_yMYKFwhM4yQ0fAqc4wQD0y-E816w5EbfNsybqA0KcghoBSuGvquOvgDpazxUB8TjQHl5gbAoyS3PDPOCOKkRWYMWuWhNTmIMv-xnP0F5cGUVYvIgBFcPyZHhi43S4gTXQzBOpZ8yfudHncj86h5d76Qp-wNv6rY-OhEWlek_7op48VZS15U2Ry1n8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: هیچ تصمیمی بدون اذن رهبری گرفته نخواهد شد
🔹
رئیس‌جمهور در نشست با مدیران سازمان صداوسیما: هیچ تصمیمی خارج از چارچوب شورای‌عالی امنیت ملی و بدون هماهنگی و اذن مقام معظم رهبری اتخاذ نخواهد شد.
🔹
هنگامی که تصمیمی در حوزۀ دیپلماسی اتخاذ می‌شود، همۀ دستگاه‌ها،…</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/437623" target="_blank">📅 10:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437622">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c28vTsQz7aTs7kzWD_MGcYutS2lBjcwgMENV18a--q5AOJBQMNigagegjzaJ-zD5NodzvEWrUsMSY9YQgnzzbWoNeMkH7W06AuWr2iSk9IiTxSKeCOzAPG7r7SqJ0zdl8kZi30SpWF23L_AOUoBLt89hbNhfZRID575iX26LbiYFjdU9ULBonlCMeu9YBO3P_5kqeLdKvZh1JbFUzuAkBR3o-l8SbP3Ou0BilRhXGwzL1pfksLIofzhBN3zatZaM2dJzNstmquQL3Vbqz4uuK332ftJPRU3iGwiFoIWSKAFTykjErnB0OYX_iANeYW1LmXOlipfIRrOZHaWVt8JZFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: هیچ تصمیمی بدون اذن رهبری گرفته نخواهد شد
🔹
رئیس‌جمهور در نشست با مدیران سازمان صداوسیما: هیچ تصمیمی خارج از چارچوب شورای‌عالی امنیت ملی و بدون هماهنگی و اذن مقام معظم رهبری اتخاذ نخواهد شد.
🔹
هنگامی که تصمیمی در حوزۀ دیپلماسی اتخاذ می‌شود، همۀ دستگاه‌ها، تریبون‌ها و جریان‌ها باید از آن حمایت کنند تا صدایی واحد و منسجم از ایران به جهان مخابره شود.
🔹
امروز صداوسیما باید منادی وحدت و انسجام ملی باشد. اگر همه باهم، در چارچوب منویات رهبر معظم انقلاب حرکت کنیم و انسجام ملی را حفظ نماییم، دشمنان هرگز به اهداف خود علیه کشور دست نخواهند یافت.
🔹
نمی‌توان هر فرد یا جریانی صرفاً بر مبنای سلیقۀ شخصی خود، نسخه‌ای متفاوت برای کشور ارائه دهد؛ چراکه ادارۀ کشور مستلزم تصمیم واحد و تبعیت جمعی است.
🔹
حل بسیاری از مسائل کشور بدون حضور و مشارکت مردم امکان‌پذیر نیست. این امر مستلزم آن است که با سعه‌صدر و نگاه باز، همه اقشار جامعه دیده شوند.
🔹
اگر بتوانیم مساجد را به جایگاه واقعی و تاریخی خود بازگردانیم و به پایگاه حل مسائل اجتماعی و مردمی تبدیل کنیم، بسیاری از مشکلات کشور با اتکای به ظرفیت مردم قابل حل خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/437622" target="_blank">📅 10:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437621">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‌ «مستثنی شدن» رژیم صهیونیستی در توافق با ایران صحت ندارد
🔹
روزنامۀ نیویورک تایمز مدعی شده که ترامپ رژیم اسرائیل را از تعهدات توافق با ایران «مستثنی» کرده است.
🔹
این درحالی است که بررسی متن نهایی‌شده توافق احتمالی نشان می‌دهد که این ادعا فاقد وجاهت است. براساس…</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/437621" target="_blank">📅 10:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437620">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a569e2ef.mp4?token=D89sZGdsgA5eWExt9c-Jlfxo6aj8DcLx2hVAbLx1HOMkFDOYFieBy40sbwhC9HgSg28IfD4wBVzrMUQJoIy99QDkztQ9Vi_QoZpv6ZHqUfbDHMRV_Zn4GbYO76bSU5f8vU0-aBlbdqZuZhm5rpYXgyLsiB-omm_Rcl_gDAXLKmhasqGqtA3GWqBCN0oZfIOTCZSol3p8L-PE6ehOkyXeeALuGHrpcxLwuh9G8FmvYAHg-R9z1NKbcXRiYftR6DoU9WhbWi-IcHPCnuNZxR8MDCo_--cQsyDY1Y_upvsSE-Mmd1zkWcIPPR8e-krqQ04Fwd_1XV9QD5_9UDg07-Zw6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a569e2ef.mp4?token=D89sZGdsgA5eWExt9c-Jlfxo6aj8DcLx2hVAbLx1HOMkFDOYFieBy40sbwhC9HgSg28IfD4wBVzrMUQJoIy99QDkztQ9Vi_QoZpv6ZHqUfbDHMRV_Zn4GbYO76bSU5f8vU0-aBlbdqZuZhm5rpYXgyLsiB-omm_Rcl_gDAXLKmhasqGqtA3GWqBCN0oZfIOTCZSol3p8L-PE6ehOkyXeeALuGHrpcxLwuh9G8FmvYAHg-R9z1NKbcXRiYftR6DoU9WhbWi-IcHPCnuNZxR8MDCo_--cQsyDY1Y_upvsSE-Mmd1zkWcIPPR8e-krqQ04Fwd_1XV9QD5_9UDg07-Zw6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمله انتحاری به قطار پاکستانی
🔹
پلیس پاکستان اعلام کرد که پس‌از انفجار ناشی از حملهٔ انتحاری با خودرو به یک خط راه‌آهن در کویته، حداقل ۲۰ نفر زخمی شدند.
🔹
برخی رسانه‌های محلی، این حمله را به «تروریست‌های مرتبط با هند» نسبت دادند و گزارش کردند که آن‌ها «با…</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farsna/437620" target="_blank">📅 10:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437619">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‌
🔴
قالیباف: مجاهدان رشیدی چون شهید احمد کاظمی و شهید علی صیاد شیرازی که غیرممکن‌ها را ممکن کردند و به ما آموختند که هیچ دژخیمی را یارای ایستادن مقابل سربازان عاشق و مؤمن ایران نیست و مجاهدی که برنامه‌ریزی، توکل و شجاعت را مشق کند، دست یاری خداوند رحمان را…</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/437619" target="_blank">📅 10:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437618">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🖼
قالیباف: هیچ دژخیمی را یارای ایستادن مقابل سربازان مؤمن ایران نیست
🔹
رئیس‌مجلس در پیامی به‌مناسبت سالروز آزادسازی خرمشهر: هیچ دژخیمی را یارای ایستادن مقابل سربازان عاشق و مؤمن ایران نیست و مجاهدی که برنامه‌ریزی، توکل و شجاعت را مشق کند، دست یاری خداوند رحمان…</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/437618" target="_blank">📅 10:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437617">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SD2SfGkxUoegvPndhv-iSyKW92Flm0T__72kCB4YrOPMEYWN9ZA1yW_m4unv3S00pDvvbBtPxKMs1BUeh9480vV20zdkJA1kREtE-EpjLuAstmNCnoNu1lWpr9Jv2cVbXrID_vj5cHyBF8H2NicxuRoW71nzozr5C6dOReU2xhAQy4MoWL9my96BHvqsUunuqqwdJ5gzEPKSc94nEa9EU0dffQ_VRclZtKUUACxn8LDFk8oylrLE0fbZw5RhiHYXRIPo4eZYuz1PkDXtOUvaO6szSejvbWguZZIZDbaGW2sr5_zC1D8qB9rvniQQRPy0hc6Puy4kGf9GUkJxcBV-Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: هیچ دژخیمی را یارای ایستادن مقابل سربازان مؤمن ایران نیست
🔹
رئیس‌مجلس در پیامی به‌مناسبت سالروز آزادسازی خرمشهر: هیچ دژخیمی را یارای ایستادن مقابل سربازان عاشق و مؤمن ایران نیست و مجاهدی که برنامه‌ریزی، توکل و شجاعت را مشق کند، دست یاری خداوند رحمان را بر شانه خواهد داشت و انسداد را نخواهد پذیرفت.
🔹
به‌طور قطع سوم خرداد آغازی بر دلاوری‌های بی‌بدیل رزمندگان ایرانی است، رزمندگانی که به فرمودۀ قائد امت، حضرت آیت‌الله العظمی شهید سیدعلی حسینی خامنه‌ای خرمشهرها در پیش دارند و خداوند متعال، راه شکست را بر آنان بسته است.
🔹
رزمندگانی که به دنیا آموختند افتخار و عزت نصیب ملتی می‌شود که ایمان، اراده، غیرت و شجاعت را در کنار تخصص و تلاش داشته باشد و چنین ملتی هیچ‌گاه طعم تلخ شکست را نخواهد چشید.
@Farsna</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/437617" target="_blank">📅 10:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437615">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ff508d240.mp4?token=XEV-w5vAomaO5oKFNOo09ecyvxe0kwPCIensn6oa3BmKhDatBvvVxL2PGeD0Kb3-iQwm_TbZd9VPRO8PfTG3ug_jHUALyI_zo4fyyTEEOYRphIOOZr-fft_VNBmR96gZDoWNii8zfG5PDHTiDjqKhTYnvNOKj0bRQuzeNuSc2d5MTTnXK7DeJZVgYirMkyMFmi87Wb1HRS3nr7z-3-mIWmHdlgrrMoY5csgbP-6Y7q2Z7mJgLwEUmYQz-aTQBlKO8kUK-L1dOglLk6w6J3J6ODP4hr9Sj4NeBOu_OlTO8jzMe7bcrV6PLsegD56lhDfxPHCX8SxF7ku_JKkgnHG2Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ff508d240.mp4?token=XEV-w5vAomaO5oKFNOo09ecyvxe0kwPCIensn6oa3BmKhDatBvvVxL2PGeD0Kb3-iQwm_TbZd9VPRO8PfTG3ug_jHUALyI_zo4fyyTEEOYRphIOOZr-fft_VNBmR96gZDoWNii8zfG5PDHTiDjqKhTYnvNOKj0bRQuzeNuSc2d5MTTnXK7DeJZVgYirMkyMFmi87Wb1HRS3nr7z-3-mIWmHdlgrrMoY5csgbP-6Y7q2Z7mJgLwEUmYQz-aTQBlKO8kUK-L1dOglLk6w6J3J6ODP4hr9Sj4NeBOu_OlTO8jzMe7bcrV6PLsegD56lhDfxPHCX8SxF7ku_JKkgnHG2Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمله انتحاری به قطار پاکستانی
🔹
پلیس پاکستان اعلام کرد که پس‌از انفجار ناشی از حملهٔ انتحاری با خودرو به یک خط راه‌آهن در کویته، حداقل ۲۰ نفر زخمی شدند.
🔹
برخی رسانه‌های محلی، این حمله را به «تروریست‌های مرتبط با هند» نسبت دادند و گزارش کردند که آن‌ها «با هدف‌قراردادن غیرنظامیان بی‌گناه در کویته از طریق یک حملهٔ انتحاری با خودرو به یک قطار مسافربری، وحشی‌گری خود را به‌نمایش گذاشتند».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/437615" target="_blank">📅 10:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437614">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">۷ نماینده کاندید نایب‌‌رئیسی مجلس شدند
🔹
علی نیکزاد، نماینده اردبیل
🔹
عبدالرضا مصری، نماینده کرمانشاه
🔹
حسینعلی حاجی‌دلیگانی، نماینده شاهین‌شهر
🔹
حمیدرضا حاجی‌بابایی، نماینده همدان
🔹
رضا جباری، نماینده مسجدسلیمان
🔹
علیرضا منادی، نماینده تبریز
🔹
پیمان فلسفی، نماینده…</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/437614" target="_blank">📅 09:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437613">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‌ ‌ادعای ترامپ دربارهٔ بازگشت تنگهٔ هرمز به حالت قبل واقعیت ندارد
🔹
به‌گزارش فارس؛ برخلاف ادعای لحظات قبل دونالد ترامپ در شبکهٔ اجتماعی «تروث سوشال» مبنی بر بازگشت تنگهٔ هرمز به وضعیت پیشین و آماده‌سازی برای امضای توافق‌نامه، پیگیری‌های خبرنگار فارس نشان می‌دهد…</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/437613" target="_blank">📅 09:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437612">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWVRzPREOzQyNPBnODDS9xBJH3Xhz5mZmZVLaCOfjD7op-C0fE6Bk68kDLZStliLg3jHphdw3iendZBOKDOVsy4xj2_J-J_H7aAI2NwD8xbPrBL6-AodTOTf9pNOTbfpBX2fOJaUSCSIVzpL2oUYzTHr2K-jN2v6juSZf9Ri9ZdyMBbRmXmB_pKN_4oWh2v6GwGI_H28ueCwjID6BZ0sQco4No6yiFm2NR3zrQGImvJsD-BtigZUgOn2fh8aMzEpKxuUSORppJYHi9dpAFB_wUuu6BQT7KKr00wW3yXV1pneSQ_K9ajhBUKvKkwj3NgG_LFKma0dWFCZ5OB820TK7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پیام مشاور رهبر انقلاب به‌مناسبت سالروز آزادسازی خرمشهر و تناسب این اتفاق بزرگ با رخدادهای اخیر ایران و جهان
@Farsna</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/437612" target="_blank">📅 09:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437611">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIZGMvnF4jQV1xoDszGNntuFMUJQSlhpckJ7_vltCf03BUIEjUqbl0qGkrcKt5R-z-WjKZUjryGzwQbR79hxYiOcbyb_gkUkQQ0jcFy-hCj0w6DhQofmP2i_v_4yiejdXNcbAYrXmayIy3vZnulJQija8FY4KpSOjysbpWIrylcxLsK7HWvy-KMukqAb10bOMoAz_A-_JYaIuMO2lEuFxeeZyRro_ntsd2Clf0ELWkVNsWJzoZOShAT7YqR6Z_6ObE_7PySZA-HvJ1ksjVtCqNvrBd0JjY6iodXKfEVZUFfyDbaH57s9uYo-nAZ5b2OO5ObmO25o21jF8FPgzZ_R-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فرمانده کل سپاه به‌مناسبت سوم خرداد
🔹
سوم خرداد، روز ملی مقاومت، ایثار و پیروزی، یادآور حماسه ماندگار آزادسازی خرمشهر پس از ۵۷۸ روز اشغال است؛ روزی که فرزندان غیور و غیرتمند این مرزوبوم با ندای «ما می‌توانیم» خرمشهر را از لوث وجود پلید ارتش بعثی صدام پاکسازی و کلام امام کبیر انقلاب حضرت روح الله(ره) مبنی بر اینکه «خرمشهر را خدا آزاد کرد»، طنین افکن و اراده الهی، وحدت و اقتدار ملی برابر استکبار جهانی در یک رخداد شگفت انگیز به منصه ظهور رسید.
🔹
امروز نیز ملت مبعوث شده ایران با گذشت ۴۴ سال از حماسه تاریخی آزادسازی خرمشهر و پیروزی در عملیات بیت المقدس، در سومین جنگ تحمیلی – که با حمله تروریستی دشمن صهیونی‑آمریکایی و شهادت مظلومانه قائد عظیم‌الشأن انقلاب و جمعی از فرماندهان نیروهای مسلح و دانش‌آموزان میناب رقم خورد – بار دیگر سربلند بیرون آمده است، و دشمن زبون پس از ۴۰ روز مقاومت  کوبنده و پاسخ قاطعانه و ویرانگر نیروهای مسلح، با ذلت درخواست آتش‌بس کرد و اینک نظاره‌گر خروش ایرانیان در خونخواهی رهبر شهید انقلاب اسلامی است.
🔹
فرماندهی کل سپاه پاسداران انقلاب اسلامی، ضمن گرامیداشت یاد امام راحل (ره)، امام شهید آیت‌الله خامنه‌ای (قدس سره)، و شهیدان گرانقدر دفاع مقدس و شهدای اقتدار ایران اسلامی و جنگ تحمیلی رمضان، و تبریک این روز خجسته به محضر مقام معظم رهبری و فرماندهی کل قوا حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای (مدظله‌العالی) و آحاد ملت شریف، قهرمان و انقلابی ایران، نکات راهبردی زیر را اعلام می‌دارد:
🔹
۱: جنگ تحمیلی سوم، جنگی ترکیبی بود اما پاسخ قاطع، کوبنده و درس آموز سپاه مقتدر مردمی و نیروهای مسلح به پشتوانه حضور حماسی مردم در صحنه، دشمن را در دسترسی به اهداف ناکام و آمال و آرزوهای او را بر باد داد و ترفندهای  اهریمنیش را خنثی کرد.
🔹
۲: عبرت خرمشهر، اتکا به قدرت درون و بازدارندگی فعال است. پیشرفت‌های هسته‌ای، موشکی، دفاعی و تهاجمی ایران، دشمنان انقلاب و میهن اسلامی را را به محاسبه مجدد واداشته است.
🔹
۳: بزرگترین سرمایه راهبردی کشور، حضور مصمم و پرشور مردم در همه صحنه‌ها است که سدی محکم و خلل ناپذیر در برابر نفوذ و توطئه دشمن است.
🔹
۴: نیروهای مسلح مقتدر کشور در بالاترین سطح آمادگی و بازدارندگی فعال در همه ابعاد "موشکی، هوایی، دریایی، زمینی، فضایی و سایبری" قرار دارند؛ بر این اساس بدیهی است هرگونه تعرض مجدد دشمن، پاسخی ویرانگر و جهنمی در ابعاد منطقه‌ای و فرامنطقه‌ای در پی خواهد داشت.
🔹
۵: فتح خرمشهر، الگویی ماندگار برای پیروزی در خرمشهرهای پیش رو و آزادی قدس شریف و نابودی رژیم پلید صهیونیستی توسط محور مقاومت و مجاهدان جهان اسلام است.
🔹
در پایان، با تجدید میثاق با آرمان‌های بلند امامین انقلاب و شهدای گرانقدر انقلاب اسلامی و دفاع مقدس اول، دوم و سوم  و اعلام بیعت مجدد و اطاعت از منویات و فرامین رهبر معظم انقلاب و فرماندهی کل قوا، تاکید می‌کنیم:
🔹
بی‌تردید ملت بزرگ و فهیم ایران در فضای مذاکره برای پایان جنگ، با حفظ و تعمیق وحدت و بصیرت، و رصد مواضع و رفتارهای دشمن حیله‌گر و عهد شکن نقشه‌های او را خنثی و نقش بر آب خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/437611" target="_blank">📅 08:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437610">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDVpIKqjLgUqEGBDDIgCLbXsmAZVPB0xghjJtUbcTD78N2sqaXcYO1BnGcbQBqkCM6B6atc3ejWRY8iMqRUDQwEJBDuqsSM-c29IjcuBhgMzlnC5xfiwJcv3m538jDW9Kn6vyIRTOkN9TXSEvgwsca1LME8zCm1UNOf85ZaWaBaj4pLffSyh_NdGUBmEx7SDV_r2hoIedA309Ln0qBScl-o0NhcQTZkyu7GLvXNAoSKurdiPpIAA27t4A_KKOdVZls_dcrV_dGCevzQBCEbT-6wEXvXZ0XblrZboX6T6HBQIf7PSXgjkptwxVrIVwebntpk0w5fPQokFeGwSfHW2Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عامل ارسال اطلاعات مراکز تولید صنایع دفاعی به دشمن اعدام شد
🔹
مجتبی کیان فرزند محمدقلی، از عناصر همکار دشمن که در طول جنگ رمضان اقدام به ارسال اطلاعات مرتبط با واحدهای صنایع دفاعی کشور به دشمن می‌کرد، پس از تشکیل پرونده و رسیدگی قضایی در دادگستری استان البرز،  بامداد امروز اعدام شد.
🔹
نامبرده در طول جنگ رمضان پیام‌های متعددی را به شبکه‌های معاند وابسته به دشمن صهیونیستی‌آمریکایی ارسال می‌کرد که از جملۀ آن‌ها، مختصات و اطلاعات محل واحدهای تولید قطعات مرتبط با صنایع دفاعی کشور بود.
🔹
محکوم‌علیه در شرایط جنگی، در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده».
🔹
مجتبی کیان در اعترافات خود عنوان داشته: «پس از ارسال پیام به شبکه ماهواره‌ای، شماره‌ای را به من معرفی کردند تا اطلاعات را ارسال کنم و من نیز اطلاعات را از آن طریق ارسال کردم.»
🔹
بررسی فنی پیام‌های رد و بدل‌شده میان محکوم‌علیه و عناصر دشمن نشان می‌دهد ۳ روز پس از ارسال اطلاعات، محل مورد اشاره هدف حمله دشمن قرار گرفته و به‌صورت کامل تخریب شده است.
🔹
پس از ارتباط‌گیری مجتبی کیان با شبکه رسانه‌ای معاند، نامبرده بلافاصله شناسایی و دستگیر شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/437610" target="_blank">📅 08:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437609">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwILAKum3DyD7vRpkKmLWmNZOffkz8v0e4xxd1X606yZxUFmNB2zb3OqWbbXuKW4KbCUThPxQVX-qS5Cqi0A80BR9LLlRS5ocR7ohNgL2efIyc8HcOJ0mkSRUjwaDFBzu1f8ufgyP-dNfRBGmod11eegitT47v1niF__FjKLEMF-2tQBJwpNjwtTlvYsRF-Vd7lBSGKvao9bvf-tWX-PZFJKIFiwDYNWAy4uAF0ofd1DjKwTH4jbSoKh2st8tfd1ydYtiXXmdHATq5io0a23X9GxY4pN6aRuBmbhKYrSK3WAcS8Ro3pBXujBFCViR4MeofP_y53SH8DtLMHPeTHSpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: خرمشهر امروز ایران، خلیج‌فارس و تنگۀ هرمز است
🔹
ملت ما امروز هم‌چنان مردم رزم ندیده اما دلیر خرمشهرند که روزها در مقابل ارتش متجاوز ایستادند تا قدرت مردم ایران را به رخ جهانیان بکشند.
🔹
مقاومت، ایثار و دفع تجاوز، ریشه در فرهنگ این سرزمین دارد.
@Farsna</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/437609" target="_blank">📅 08:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437608">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nshl3T-vkhlCZyMbugCGc1UNS2GMgdpGYkNim-3U6rNADKKInhC79aqentLnI-WOllz4sBJ6EFIWguucqGqeIGmpS1CstPoOGKTdGWmcOP0VBWCePYjrQ0BMJCxxDOGEhomOLwTZM0w6uQdccHeRn_J-VxP8MgExBabUDb3vW55E7_8aTEu79NnpUU-xyCy2qX02e4mnhudaI79fy5232poZ8w-MoCTcQiy_AtVA1tigs6f3OeSYoRACsNfY7mF7TvKyKG19jH0rsWyvgY6vtQRBVb3WF4NlF3toPZWzKJXGLM-8GhHXLymDvIAcy4rst3PwmFGTHNnmb6kvV-gbpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عارف: با همان ایستادگی حماسۀ خرمشهر، دربرابر دشمنان پیروز می‌شویم
🔹
معاون اول رئیس‌جمهور: حماسۀ آزادی خرمشهر آموخت با مقاومت و اتکا به توان داخلی می‌توان از بحران‌ها عبور کرد.
🔹
امروز نیز در میدان دیپلماسی، دفاع و سازندگی، با همان ایستادگی مقتدرانه و تبعیت از فرامین رهبری دشمنان را به تسلیم در برابر ارادۀ ملت وادار کرده، تحریم‌ها را شکسته و بر دشمنان وحشی خود پیروز می‌شویم.
@Farsna</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/437608" target="_blank">📅 07:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437607">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-TH1GTrzRT1XmNHJcR5nGUJm5-CPC8KMhGnSWIZyz2F3E_Jl1UVAYH1N0Ol9UUGZqQy3VI_GkwTe-OWjy6LFXCgE4gdYaJ3nnB6gRSQwjfNq2CWGyPlYWhkcC_r61krHGp6M79OuPYFRFg09ARnlr5fnfrKNja5Oc5nnkLNoXphwerkf1ZWVkVcpj_9jiKnGon9_y8l98pdmajotMST5oNvTDXCYFPvJUqJvX9SZyj63cShMePTk745wAdgkQ755rqGcl00Qxq6qpxadLXhGyKvfFl0qlMdM5H1cguqBpxu2JXqBK37YmvELwpv3tfkqX_KO74YRrbjilXoiiSpQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران با دور زدن آمریکا سوژۀ اول جام‌جهانی شد
🔹
بعد از اعلام مهدی تاج برای انتقال کمپ تیم‌ملی ایران از آمریکا به مکزیک با موافقت فیفا، این خبر امروز در رسانه‌های معتبر جهان به سوژۀ اول جام‌جهانی و بمب خبری تبدیل شد.
🔸
خبرگزاری AP این اقدام ایران را دور زدن مشکلات عدم صدور آمریکا توصیف کرد و نوشت: ایران با انتقال کمپ خود به مکزیک مشکلات عدم صدور ویزا و تعلل دولت آمریکا ٢٠ روز به آغاز جام‌جهانی را خنثی کرد تا راهی مکزیک شود و تنها در بازی‌ها در آمریکا باشد.
🔸
نیویورک تایمز نوشت: ایران با موافقت فیفا کمپ خود را از آمریکا به مکزیک منتقل کرد تا با کمترین مشکل تمریناتش را انجام دهند و در آخرین روزها با دریافت ویزا در جام جهانی شرکت کند.
🔸
شبکۀ تی‌آر‌تی ترکیه این اقدام فدراسیون ایران را نوعی ترفند برای به حداقل رساندن کارشکنی آمریکا در زمینۀ عدم صدور ویزا توصیف کرد و نوشت: ایران با انتقال کمپ خود با مکزیک مشکلات عدم صدور ویزا و بلاتکلیفی را حل کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/437607" target="_blank">📅 07:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437606">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7LWloLk1wIOAFRlP0Qz69_10jSK9yJ-1_BSH5nBweJbo67Q7MbYv51xrkBqj8EH8S5wajjJWBOKYgftIkRzyQBq8kpsrmfqFfxilxFyLGV1QJjyLGCI1NfBNg2NruBszKvZ4VRXFgVnB5BoYcaMgDmy4y4niwjyL3AWEWX3KzhvxPrz5r0RguXXQpTuhvCR7HbtYtiLZjDzCOTrEEZznQYLnzP6iz7iAkqYSJqpXvv6tfGQvsRanrHO-b-01h38BAlaqlpg-6YUfrhzcEgUF9GAWImAhS1Tk8ui059VNhQBlG9HWbpO-qadm6zR-iUuJodUIJ3PgSV29YPUkpKnmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژۀ تازۀ واشنگتن برای خلع سلاح لایه‌به‌لایۀ لبنان
🔹
لبنان این روزها در کانون یک بازی پیچیدۀ قدرت قرار دارد؛ بازی‌ای که آمریکا با سلاح تحریم آن را بازطراحی می‌کند. از افسران ارتش تا معاونان ارشد نبیه‌بری، همه در تیررس واشنگتن هستند.
🔹
اما هدف نهایی از این پروژۀ امنیتی-سیاسی تازۀ واشنگتن چیست؟
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/437606" target="_blank">📅 07:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437605">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Df3wc9mAKBbvm10lWYtFogLpjtknDNAgzhcAcZXAqxeXx1zjh6s_l_w4N7OsYvnu5dChtIuT6ymotgqLYtjBbosXxUl3Kb0-67YJ7f2V-C90Iz6t9ZPXEFuOO6ktFzsWNE_TodR-Lmk9hoCDw-_pR3jGv5JToJo3Ajl00uSoSGPLoNz7atYs4M9cebAT37bIBhyl6Mk6Qr7jr_0xvFv0UgJgZG98zcUzX-eSRltbPgDxNicCdzTvAPi38QYQVgDIlTyGqRh8AtWDk5GlAjWQHNbysjRZfsEz5pUJUuk1qL7aczDJ7ft0mzaQZUH_h9UV7JLPyX-pPBA0z6B5phXTEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
معاون وزیر خارجه: ایران منطق صلح‌طلبی همراه با قدرت، دیپلماسی همراه با عزت، و دفاع قاطع از استقلال کشور را دنبال می‌کند
🔹
غریب‌آبادی: ‏۳ خرداد، سالروز آزادسازی خرمشهر، یادآور حقیقتی ماندگار در تاریخ ایران است؛ حقیقتی که با اصول بنیادین منشور ملل متحد نیز پیوند دارد: ملتی که قربانی تجاوز و اشغال شود، از حق ذاتی دفاع مشروع برای صیانت از سرزمین، استقلال و کرامت خود برخوردار است.
🔹
خرمشهر نماد پیروزی ارادۀ ملی بر تجاوزی بود که با محاسبات قدرت‌های حامی متجاوز آغاز شد، اما در برابر ایمان، ایستادگی و خوداتکایی ملت بزرگ ایران شکست خورد.
🔹
امروز نیز ایران همان منطق را دنبال می‌کند: صلح‌طلبی همراه با قدرت، دیپلماسی همراه با عزت، و دفاع قاطع از تمامیت ارضی، استقلال و حقوق مردم و کشور عزیزمان ایران.
@Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/437605" target="_blank">📅 06:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437604">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdRHQinkD8hsarjqdpH0HcoBN7_suSAVXv9Lc2nSXVMDJDikXw80BfO_yuL8NA8SopFWaCbSYwnomsPCA1o0csCH22hErQ_-uF_vM-HCupPxlUIgyLEVJb4mdV9dUmjC3CtUdo4792ivqjAJhrFtDbVd90YrM1zTFPgSy9Sc9HcsLAUolSApp9-i_phSgVfy8FlzLDJellzwlLqxtn0ptMKgFiOHafZdqSlA4Lz7fjDUYeDZP8Sf1d1TfJalEHMJBzBGQ0JalQWEQHBFvDRhRIu_2725Z7sI7jWpOHc1Kw3JehE4hVtHouh1ytQMBY0sFE3EF3kw-xng9174-TaR3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهم بیمۀ کارفرمایان، و محل حقوق بازنشستگان تغییر می‌کند؟
🔹
وزارت اقتصاد و وزارت کار به دنبال تصویب لایحه‌ای در دولت با عنوان «لایحۀ ایجاد نظام جدید تامین‌اجتماعی» هستند که بر اساس آن حق بیمۀ سهم کارفرما از ۲۳ درصد به ۷ درصد کاهش می‌یابد.
🔹
طبق این لایحه سهم حق بیمۀ‌پرداختی کارفرما و بیمه شده برابر و در مجموع ۱۴ درصد خواهد بود و ۱۶ درصد مابقی از محل درآمدهای مالیاتی تامین خواهد شد.
🔹
همچنین کلیۀ منابع حاصل در خزانه‌داری کل کشور جمع شده و حقوق بازنشستگان از خزانه‌داری پرداخت خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/437604" target="_blank">📅 06:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437603">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rx5kzuOZ0uH86ONTkwgD7ynyz29boOHOV0J2NCVOAUOzziWX0U8y7f25cPsdiW_RpYvUHdtWaK4dVtsmuenJnCmPb-Bsmz2pt8svULpIqq2sAgWuZ4I-l7mbCoZ9JU0v3XwSys0cHPi65-yTuIOfIAz2KxFDJpd2XALTSVRNOSe9kcUqFaaaQPKx2Pra1rAD2bOZOnabGDWZPtxnKAc3KCC1cFNNPFmyJZ7BskOK8bVzcKWSfSbTASRrH1LTDtBOz9q7o3I8SVwHrCubZUEs-FO1JUG9vL1xdD2q9ocD2S0wor6J1vYUBRNQvqi2Gimx53zl3r7OD4wMTKQMGsAKdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رسانه‌های آمریکایی: فرد مهاجم کشته شده است
🔹
رسانه‌های آمریکایی به نقل از سرویس مخفی آمریکا، از مرگ فرد تیرانداز در اطراف کاخ سفید، براثر جراحات وارده خبر دادند.
🔹
هویت این فرد هنوز نامعلوم است.   @Farsna</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/437603" target="_blank">📅 06:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437599">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a0ddcf87.mp4?token=TkOlxl9LcQG4KGCXVRi0yPBMPsKepLZkuB7p6pNNli7cRI5Sd12rZ3DSYOnSGLbAHu_xCaBiRexDYuYbSqLY4_trt6kGqzMqJr8dw_5DgHYH7uIa1M1EhOvXbn5yDV-KzeoDTBUsIgHC66GSO14mgv0RZWKGnKsKWhi3fvp-ejjsThqqlEgZ5jZcBChLytL_ZXYd9l0SbbcFFkZqcl-7JbHMR9YXP_Mg65Rkq35oOMHpGF3nS52h3vS8n2XVDiARXsCyeJslB911mQOYjAJrgKCEhobUkUz9e-onWKBzrxCHLz3sYdZlm8L2vts23-GWDi1JI_ujUSrNTtUYuKTV_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a0ddcf87.mp4?token=TkOlxl9LcQG4KGCXVRi0yPBMPsKepLZkuB7p6pNNli7cRI5Sd12rZ3DSYOnSGLbAHu_xCaBiRexDYuYbSqLY4_trt6kGqzMqJr8dw_5DgHYH7uIa1M1EhOvXbn5yDV-KzeoDTBUsIgHC66GSO14mgv0RZWKGnKsKWhi3fvp-ejjsThqqlEgZ5jZcBChLytL_ZXYd9l0SbbcFFkZqcl-7JbHMR9YXP_Mg65Rkq35oOMHpGF3nS52h3vS8n2XVDiARXsCyeJslB911mQOYjAJrgKCEhobUkUz9e-onWKBzrxCHLz3sYdZlm8L2vts23-GWDi1JI_ujUSrNTtUYuKTV_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روسیه با موشک‌های اورشنیک انتقام کشتار دانشجویان را گرفت
🔹
ارتش روسیه بامداد امروز یکشنبه، حمله‌ای گسترده با موشک و پهپاد به کی‌یف پایتخت اوکراین و مناطق اطراف آن انجام داد.
🔹
نیروی هوایی اوکراین نیز اعلام کرد که حمله ترکیبی شامل موشک‌های بالستیک و پهپاد بوده و برخی از پرتابه‌ها توسط پدافند هوایی رهگیری شده‌اند. منابع اوکراینی از استفاده روسیه از موشک «اورشنیک» (موشک بالستیک میان‌برد جدید) در این عملیات خبر داده‌اند.
🔹
این حمله گسترده موشکی و پهپادی پس از آن انجام می‌شود که وزارت شرایط اضطراری روسیه شامگاه شنبه اعلام کرد شمار قربانیان حمله اوکراین به خوابگاه دانشجویی شهر استاروبیلسک در اقلیم خودمختار لوهانسک به ۲۱ کشته افزایش یافته است.
🔹
ولادیمیر پوتین رئیس‌جمهور روسیه نیز روز جمعه اعلام کرده بود که به وزارت دفاع این کشور دستور داده است تا پاسخ این حمله را بدهد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/437599" target="_blank">📅 06:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437594">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKLPSoZGt6Xxvlpb-pJ9oa-v2Fp_oYSMehdwCodeA8aDgPTG0ueNkBmcgVmoevJsDil_bWSNA6tlZiwUCCIkT0oY3BUBdc3sJjqgB9rxMLlUEZW6j7Y-0xPrc0XdwYIKHk5_h2vJ2HmSsVK5SytPRnZfU0vtrHhPU1drxUC6s45GooKCuoij_428X-hLQrk5uLHBhlCSJ35iN13bM2AOdpdkxfAYFmzQ2jNWF76fVGEsNPvmq26Ayq7o06zstflgfhVSScat0yEiqneo1iDlayjA9wyBP4B0ennPaUv8QMrMufof2m46qkERJzFphU6Z89ZMZQhLXACJi30aioPn2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرضۀ جدید شاهین در میان معوقات ۴ ساله
🔹
سایپا در حالی دور جدید عرضۀ شاهین را آغاز می‌کند که هزاران متقاضی این خودرو، از چهار سال پیش تاکنون در صف خرید هستند.
🔹
معاون فروش سایپا دی‌ماه سال گذشته گفته بود، از مجموع ۴۴۰ هزار دستگاه شاهین تعهدشده طی سال‌های ۱۴۰۱ و ۱۴۰۲، ۴۲ هزار دستگاه باقی مانده که ۱۲ هزار آن «معوق» است و تمامی این معوقات تا پایان شهریور ۱۴۰۵ تحویل می‌شود.
🔹
با این وجود، حتی در صورت تحقق کامل این وعده و تحویل خودروهای معوق، همچنان ۳۰ هزار دستگاه شاهین از تعهدات باقی می‌ماند که متقاضیان آن همچنان در صف انتظار تحویل قرار دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/437594" target="_blank">📅 05:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437593">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2hxH46AiOyAN2HwmJ0deMT5C6TJZO1RFehE0dz4ilh-svnZAAnH5QdupNk19mVBl24hpkxd3ucsuNhxVvdE6tsFaCppKD-J4y1jQViaGukoMqSrNZ4-DXmhYjkQ9ZRc-LxiAZeGw-IOvYHBkCFF_-2Q2jaBDzJlY7YXeo-vRkyADgI7XtYnkL7EyXsRRW9FMeHC0f3SZnCSiPqOvR4FhG4iCED1mPzGbkRBJFXcWEoX6q_s1x8miNYeg4aFgsV5E_JC6Fm_CdgJrTI-4tiR3WlH-gTPn-_O_HhxteASx8yDotccuMVWEKaN7jO2xpzt2lXlBgTVhTlsQZv1-oy2Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاس اولی‌ها تا ۱۰ تیر برای پیش‌ثبت‌نام فرصت دارند
🔹
آموزش‌وپرورش تهران: پیش‌ثبت‌نام دانش‌آموزان ورودی پایۀ اول ابتدایی برای سال تحصیلی جدید آغاز شده و تا ۱۰ تیرماه ادامه خواهد داشت.
🔹
پیش ثبت‌نام از سامانۀ
my.medu.ir
انجام می‌شود.
🔸
اما شروط و مدارک لازم برای پیش‌ ثبت‌نام کلاس اولی‌ها چیست؟
اینجا بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/437593" target="_blank">📅 04:59 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
