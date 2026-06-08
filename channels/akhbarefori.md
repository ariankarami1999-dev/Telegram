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
<img src="https://cdn4.telesco.pe/file/SnJb7UlggJViluTN9Vr-LAUnH7tKgyqnXSSsyEJxKlWbLfo4UvSxevUFfunxaIzm1_K2WpPqxk2BshIy8rQj4RH1PpPmuuUKLXR-jY8jvSPQ2Qhzov6ZJv48zxZDHvA8x-C2-m-Nuq5z3B84AyKtxM-1rBMyRtncM1RpQVTppH3YlQQb9rjCbHa5Pvm6CilDfqlSbU98FOE3i0ZNhUfVMzD6K7iBWOx2M-1EUjM-Le2YoW5JSqhpL5PFISh8oBUWLjHN_GHS7MDBQcdHFcELk8IzY9UpqT9PZqXu2Qt5czM5OFZkpG8Anv2MN45N2Yn-P-Syge9KnnADGeHTUBnw7A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.24M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 14:56:10</div>
<hr>

<div class="tg-post" id="msg-657359">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3jhc7uOWB2T90HTnCcev0Mb5WNU7oiX2Ghg1gFeLEgk2BJRDkz1cwwz3b_7QXna6paId_Bn4B-P3RTUMHSrcPkr9LnI56EQ2CVmslE_XK7bM4XrmO2VKUZfYjnRQJFZMipfqN_vtGU9t4300fgfmCrabzBo77pMGebk4qo-LsXhGNb7Z1Kz4tauMhoKbLwJ23SzVtdDMk5g5KG7HfzcOcrqJxNRcMG5OhhK6MjyKTXv8_vU4qCrZ1O-4sjf8tAM3bkAVvVyb0PfuLj8Vj-_nxpKbYm1CBtBz5M6b1e6ZT1Z2WKWMi6la9KGwC6oF2BsEUtmQx9ujBpXZBZg_wiG2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر فدراسیون فوتبال
🔹
۳ روز مانده تا شروع جام‌جهانی ۲۰۲۶
#جام_جهانی_۲۰۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/akhbarefori/657359" target="_blank">📅 14:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657358">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
اسرائیل هیوم به نقل از منابع ادعا کرد: رژیم صهیونیستی و آمریکا پیامی را به ایران مبنی بر این امر انتقال داده‌اند که اگر ایران مجدداً حمله نکند، حملات بیشتری علیه ایران صورت نخواهد گرفت
/ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/akhbarefori/657358" target="_blank">📅 14:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657357">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خبرفوری
pinned «
♦️
قرارگاه خاتم‌الانبیا: عملیات متوقف شد؛ در صورت تداوم تجاوز پاسخ شدیدتری می‌دهیم  قرارگاه مرکزی حضرت خاتم‌الانبیا(ص):
🔹
در پی تجاوزات رژیم صهیونیستی در جنوب لبنان و ضاحیه، نیروهای مسلح جمهوری اسلامی ایران در حمایت از مردم لبنان پاسخی دردناک به این رژیم داده‌اند.…
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/657357" target="_blank">📅 14:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657356">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
قرارگاه خاتم‌الانبیا: عملیات متوقف شد؛ در صورت تداوم تجاوز پاسخ شدیدتری می‌دهیم
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص):
🔹
در پی تجاوزات رژیم صهیونیستی در جنوب لبنان و ضاحیه، نیروهای مسلح جمهوری اسلامی ایران در حمایت از مردم لبنان پاسخی دردناک به این رژیم داده‌اند.
🔹
عملیات نیروهای مسلح متوقف شده است، اما در صورت ادامه تجاوزات، از جمله در جنوب لبنان، پاسخ‌هایی بسیار شدیدتر و کوبنده‌تر داده خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/657356" target="_blank">📅 14:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657355">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7c1768271.mp4?token=PizbC7t1tkFSNl-vI4MLXWBb5Z9oYRBdFr07UBY6628lDdHn56tPweygz7GTP6RVbI79xD9PE-sU0sHJvvlbpVujaUEj1hb21R73P6BTNJdcRkH03A-q8DVCkpkr76ICvSu6mGioBRrUb8jJFEx0tfjJpH9gGnIjqK6vlc2UgCX-Ys7QK2GIiF4k3ZmaRYoYfGbBuDnRPLQdrbFuENA3_GLmj02qSjMmobGGc4HFU11DWvftkQOXGcSvp7fMxe100IUpCrMC-kISY_TdlXlI8oHDIk6GZ0C1wNiV6gveb1FrMy6ZkDGU-k9CS5S_zOAVJuFQDBfIog21s0bavyqVGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7c1768271.mp4?token=PizbC7t1tkFSNl-vI4MLXWBb5Z9oYRBdFr07UBY6628lDdHn56tPweygz7GTP6RVbI79xD9PE-sU0sHJvvlbpVujaUEj1hb21R73P6BTNJdcRkH03A-q8DVCkpkr76ICvSu6mGioBRrUb8jJFEx0tfjJpH9gGnIjqK6vlc2UgCX-Ys7QK2GIiF4k3ZmaRYoYfGbBuDnRPLQdrbFuENA3_GLmj02qSjMmobGGc4HFU11DWvftkQOXGcSvp7fMxe100IUpCrMC-kISY_TdlXlI8oHDIk6GZ0C1wNiV6gveb1FrMy6ZkDGU-k9CS5S_zOAVJuFQDBfIog21s0bavyqVGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیچ شناوری بدون اجازهٔ ایران حق عبور از تنگهٔ هرمز را ندارد
شناور سرفرماندهی نیروی دریایی سپاه:
🔹
به تمامی شناورها اعلام می‌شود، ورود هرگونه شناور کشورهای متخاصم به تنگهٔ هرمز ممنوع است و در صورت مشاهده بی‌درنگ مورد هدف قرار می‌گیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/657355" target="_blank">📅 14:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657354">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
پلیس: انتشار و بازنشر اخبار، تصاویر و ویدئوهای کذب یا تحریف‌شده در فضای مجازی ممنوع بوده و شهروندان باید اخبار را فقط از منابع رسمی دریافت کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/657354" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657353">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ادعای اسرائیل درباره بازداشت «جاسوس ایران»
پلیس و شین‌بت رژیم صهیونیستی:
🔹
فردی را که برای ایران در اسرائیل جاسوسی می‌کرده بازداشت کرده‌اند.
🔹
به گزارش تایمز اسرائیل، مظنون مردی حدود ۳۰ ساله است که گفته می‌شود حدود پنج ماه با یک مأمور ایرانی به‌صورت آنلاین در ارتباط بوده و در ازای دریافت پول، برخی مأموریت‌های امنیتی را پذیرفته است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/657353" target="_blank">📅 14:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657352">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-RAIIq0oR9T6mNatuflcUtA19uph9GMZFVaSn6oeaRjxd8Q5HdM7qF0SAxDzUUed1RtvAg41_a9oQjDNFJJlwsA29nMsSKun72m48DvBOj8e3IOfX9tkc4bEV9ORcwRy8p70q93wmgSjA7yd7At25qnjsOwyfL3yqMf_tf0COfIMu1kCE4JRYvyXYVPPtkrOd3ckdcCYHCq7pjMKUMYe_NaBZAna_J-CSWxfcp-XMxV9emkrbVlZdRUNcP2cwZNTnklg3E9GY49AOHLIubg9q2sDOom9H_cNsy8Hgb5rBeeaupCYPb9Dj9BFOF8HyR6v7uvxtR8ds4Yxbhcn9AoNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا اینترنت قطع می شود؟
🔹
حالا که جنگ مجددا شروع شده ممکن است اینترنت بین الملل دوباره قطع شود. ممکن است بانیان ارتباطات آنلاین و مسئولان امنیتی کشور استدلال کنند که ممکن است قطعی اینترنت به نفع کشور بوده و ارتباط جاسوس ها و ماموران امنیتی اسرائیل و آمریکا را مختل کند و جلوی ارسال فیلم و مدرک به رسانه های دشمن را بگیرد.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3221470</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/657352" target="_blank">📅 14:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657351">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f5954bc90.mp4?token=mO35-7hDcl61AqI8b3Vl30dBxPfXf0pp3ZbKN6KCJrWACry0vHYZm7D_QMhiTgfvjBPH4e4T8un5Vl1b9l2_seuZI0HH7I0c8yfuwyrpWS-QWGLdRkZ7L96-8JB_i9sS46NlCKq0Q8RtPy-ppHQ8nkdZNjMfkF8zhIhFO9K-N1qQUlftR8ItqlSwirACFicJTVRHiePCDz2AzXgIjE1o1NeE7j5C7THuuQFW2QtoXC6JVbRls5uWE0E9jhTs900M97sKEog7x0elgUpLCGABg6cu9bMEtncgGEgnANAW5V_vmHVoMFb5EMemtPRmHBAa0h0KRIGJL7T-E8jjAKYghoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f5954bc90.mp4?token=mO35-7hDcl61AqI8b3Vl30dBxPfXf0pp3ZbKN6KCJrWACry0vHYZm7D_QMhiTgfvjBPH4e4T8un5Vl1b9l2_seuZI0HH7I0c8yfuwyrpWS-QWGLdRkZ7L96-8JB_i9sS46NlCKq0Q8RtPy-ppHQ8nkdZNjMfkF8zhIhFO9K-N1qQUlftR8ItqlSwirACFicJTVRHiePCDz2AzXgIjE1o1NeE7j5C7THuuQFW2QtoXC6JVbRls5uWE0E9jhTs900M97sKEog7x0elgUpLCGABg6cu9bMEtncgGEgnANAW5V_vmHVoMFb5EMemtPRmHBAa0h0KRIGJL7T-E8jjAKYghoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحلیلگر الجزیره: ایران بی‌توجه به واکنش آمریکا پاسخ قاطعی به قمار اسرائیل در بیروت داد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/657351" target="_blank">📅 14:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657350">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ادعای گروسی: ایران باید به تعهدات خود پایبند باشد
🔹
رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی: ایران باید به تعهدات خود عمل کند و از فعالیت‌های غیرقانونی خودداری کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/657350" target="_blank">📅 14:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657349">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhkUegO5xSArJZJM09kwJWZgHY1exjRM6zVuTT_3408LTeA5Sz9byHqTPNdUC_iCV4_Kq0BXEIZ1JovINOzkUByBpA0S1JuaPZ8wuwWMAJlgG2xygnVv1QRAmHQSN52A1V8Ir_kBY0d_VBYkP5qyI9GgSYJLaEHnVfrA54iTnrLltbA0UmsiA35nv5mVBO6MXEB7KPbfyVe2mAwqG5MnHUxvfrDoDATLD5xrkw5VchdPwdSdp6cfTKrpZO440G_IteqaRzBu6n07zjfR4GK6waS-EAy2xLCPAkE_rbji_14vbK7ENM-pexI5EaJP2Ou4bxki5_8XFv-ZifVGLijxmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمین‌لرزه‌ای به بزرگی ۴ ریشتر در عمق ۱۰ کیلومتری زمین، مهرانِ ایلام را لرزاند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/657349" target="_blank">📅 14:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657348">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سفیر سابق ایران در امارات: آمریکا وارد درگیری با ایران نمی‌شود
محمدرضا فیاض، سفیر سابق ایران در امارات در
#گفتگو
با خبرفوری:
🔹
شواهد نشان می‌دهد که دولت امارات در یک مجموعه‌ای قرار گرفته که شاید خودش راضی نباشد اما مجبور است که با دیگران هم‌صدایی و مشارکت کند.
🔹
آمریکایی‌ها امارات را تسخیر کردند و پایگاه‌ها متعلق به آمریکا است و باید دید آمریکایی‌ها چه شیطنتی خواهند کرد. ورود آمریکا به جنگ اسرائیل و ایران به مصلحتش نیست و این کار را نمی‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/657348" target="_blank">📅 14:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657347">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWGxpquioKStFX6o-_R2i5nXJcwdIlHFdHBQotmw82jf3lXZcmPqqkSGy-oVQohdaTbHZI-tG-dAHLqHjAbD5IpIuQMpy0QKAYMk4x4CypBThUinrKHhvaJdRk922iGIhWTBvsBzX0JqeSgEUoVKMaiknyxEpjmWQZVsXDMX65J7z1LqBYGlKfDmLOw8jNqXT938qFzPgyWp0YGf6TsWjl80d9OR7lBI3RQsalNRiK8966G1Gs7Q1kSpOBcT4iiyA_3hD3_2VtFHlGrpnoRI2iunzRwDGOZjcbSdg55DBGcELrWDOoH0RCiv3IWypQQ-TYzmsPLJD2kecXSEyoBSoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت سفارت ایران در ارمنستان بعد از حملات ایران
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/657347" target="_blank">📅 14:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657346">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnXW140TfwX1euEOdqrrRq3qrNJeQb0dnjUdpYPQGIVIe_Y3yp6vbElH4bqMuaiERWp0WJEaF80YLT2Wcb8F5PwsB6qJrsmqPHd0PH0cLboQcPpgIQKDZ0NCYZhM1X3e-nry1gIwfZC_M2RQb4nw0BZxNUuwQqwbQrTosDUhSqRV-kEub53NNOD-pyVPNslPmgtqF7X7sukB2dtglWcz7eg8qh-8ysbfhEwFz17GBT3Z-KVud8lv07zYov2rMcRciWplUeP-3YrinwzK7YcwWHl6kz5Ry0cPwvKFOb5ePyiO72tK4fNNaZ5VkWjVKZcrNLjmKdR6TuZqkb9acppmQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری که شبکه CNN از ریزش سنگین بازارهای سهام شرق آسیا (کره، ژاپن، هنگ‌کنگ) به دلیل آغاز دوباره درگیری‌ها میان ایران و اسرائیل منتشر کرده است!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/657346" target="_blank">📅 14:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657345">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cefSN9gkv8x22Rjeih07JxlXKST27BOJneeFu_4hypgSt3QklxGbVPVUh7qXcfw3jZCdHEa3vB1i8pQuJmqvyWuaN46deVg7su1tCPQIgoSQCYYQwiRfUHL-Gs47uda28RSFyVv0TET12l7QvH-SzNmRZFsgELofaG3QIc3wk318CZAa6uRbw9Azj1ol1jzF7gnKvT7kk1PhiNXHCTuZTfufLvDhru43d_HWjermtEiJPaWuQOD8aMUyybM7euA3WbxUoDATjccVjXukUDFN4IyoeoMtXLzCo41Cj5jg9l7sMxjYiS33X0lQvMO2EMuvp_ALd_YwZjjTuD95cN4dEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: اسرائیل و ایران باید فوراً درگیری را متوقف کنند #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/657345" target="_blank">📅 14:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657344">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
پدافند یزد فعال شد
🔹
ظهر دوشنبه سامانه پدافند هوایی در استان یزد برای مقابله با اهداف متخاصم دشمن فعال شد./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/657344" target="_blank">📅 14:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657343">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
جروزالم‌پست: ایران سه سلاح هسته‌ای دارد!
روزنامه صهیونیستی جروزالم‌پست ادعا کرد:
🔹
ایران در عمل از دو «سلاح هسته‌ای» غیرقابل انکار استفاده می‌کند و جنگ کنونی غرب با تهران، بر سر خلع سلاح از این دو سلاح است، نه بمب اتم.
🔹
اولی توانایی ایران در بستن تنگه هرمز (عبورگاه ۲۰ درصد نفت جهان) است که قیمت نفت را ۴۵ درصد و بنزین آمریکا را ۴ دلاری کرده است.
🔹
«سلاح دوم» نیز موقعیت جغرافیایی ایران در قلب اوراسیا و کریدورهای حیاتی چین و روسیه است که برتری دریایی آمریکا را دور می‌زند.
🔹
بمب اتم تنها «سومین سلاح» و بی‌اهمیت‌ترین آنهاست. /خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/657343" target="_blank">📅 14:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657342">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
انهدام ۴ هسته تروریستی در جنوب شرق کشور؛ ۱۹ نفر دستگیر و ۵ نفر هلاک شدند
وزارت اطلاعات:
🔹
در چند عملیات در جنوب شرق کشور، ۴ هسته عملیاتی گروهک‌های تروریستی–تکفیری منهدم شد که در نتیجه آن ۱۹ تروریست بازداشت و ۵ نفر از عوامل این گروهک‌ها هلاک شدند. در جریان این عملیات‌ها یک سرباز گمنام امام زمان(عج) نیز بر اثر انفجار انتحاری به شهادت رسید و یک نفر دیگر مجروح شد.
🔹
در این عملیات‌ها مقادیر زیادی سلاح، تجهیزات انفجاری و بیش از ۲۰ سازه انفجاری کشف و ضبط شد و عناصر بازداشت‌شده قصد انجام عملیات‌های انفجاری، ترور و ایجاد ناامنی در کشور را داشتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/657342" target="_blank">📅 14:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657341">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
کابینه رژیم صهیونیستی امشب تشکیل جلسه می‌دهد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/657341" target="_blank">📅 13:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657340">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: اسرائیل و ایران باید فوراً درگیری را متوقف کنند #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/657340" target="_blank">📅 13:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657339">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
اروپا تحریم‌های جدیدی علیه ایران اعمال می‌کند
🔹
اتحادیه اروپا در اقدامی خصمانه علیه جمهوری اسلامی ایران، برای  نخستین بار با ادعای نقض آزادی ناوبری دریایی، تحریم‌هایی علیه ایران اعمال خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/657339" target="_blank">📅 13:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657338">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69212ac3a2.mp4?token=Zg6k94XIbObl3djF-MGZt-bUvCYpodn4w_bW8DTERGKpUAOsrQ_kaffvI9AYpic7yd2tnsDIeXyVGMWlVGIqWN2I1VV5nv_E15LqkOMKGHJxFLTUAVJV5eMQVRtD9s-zwSFcRqbMyAfpDG774kiQAuQOe_XLSL9Boe1CR6DYcp3uWv6n15SVvfESWmEsQybUA8L_E3s0-3dqEBm-NKfxknTbksAS77DIQb-kUia83ldxZ1g67Wt3EDPJFhKJsUOmMGgk63FObbClTAt1RelIAkWVfzusyjFWSjZXV4IbpsHq0Q7JslcmTlLsMMXQCpRfTE4UPUY3olU9B7XOzaelHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69212ac3a2.mp4?token=Zg6k94XIbObl3djF-MGZt-bUvCYpodn4w_bW8DTERGKpUAOsrQ_kaffvI9AYpic7yd2tnsDIeXyVGMWlVGIqWN2I1VV5nv_E15LqkOMKGHJxFLTUAVJV5eMQVRtD9s-zwSFcRqbMyAfpDG774kiQAuQOe_XLSL9Boe1CR6DYcp3uWv6n15SVvfESWmEsQybUA8L_E3s0-3dqEBm-NKfxknTbksAS77DIQb-kUia83ldxZ1g67Wt3EDPJFhKJsUOmMGgk63FObbClTAt1RelIAkWVfzusyjFWSjZXV4IbpsHq0Q7JslcmTlLsMMXQCpRfTE4UPUY3olU9B7XOzaelHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک کشتی هندی در دریای عرب دچار آتش‌سوزی شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/657338" target="_blank">📅 13:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657337">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e62e35608.mp4?token=smR-j6_aCUZcc1QY8AQx03S3U6Kwu7V-b9ntfwomj_u3Ge0ALSYqnF8tdj102zJPnpUGQl1AB_Iql-dfA2pXFuwta0r5VIyWOrbS4anQ04ZDBSAkAYtLtu0hXaj_sbLaNAUIyJvbdxKWWXZKzxaAn0honBZTQIvPNd4_bje3f2WI2nN9FWb3msuHojgGHMczIVDEMXPZlNFxIXr3r0wQ-aZooK0YfJDAlgvPehvMgjVp-CyElxtqfpyoAzbblOG6WE_9IcwAqpG-P2WH5suhc6UyNvUJniNa7fsjWGSjYOWD6jHdYmAnDP9KXT9hHAEaHeUndUdookVvKnvI0c2QiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e62e35608.mp4?token=smR-j6_aCUZcc1QY8AQx03S3U6Kwu7V-b9ntfwomj_u3Ge0ALSYqnF8tdj102zJPnpUGQl1AB_Iql-dfA2pXFuwta0r5VIyWOrbS4anQ04ZDBSAkAYtLtu0hXaj_sbLaNAUIyJvbdxKWWXZKzxaAn0honBZTQIvPNd4_bje3f2WI2nN9FWb3msuHojgGHMczIVDEMXPZlNFxIXr3r0wQ-aZooK0YfJDAlgvPehvMgjVp-CyElxtqfpyoAzbblOG6WE_9IcwAqpG-P2WH5suhc6UyNvUJniNa7fsjWGSjYOWD6jHdYmAnDP9KXT9hHAEaHeUndUdookVvKnvI0c2QiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع زلزله ۷.۸ ریشتری در فیلیپین
🔹
زمین لرزه ای به بزرگی ۷.۸ ریشتر جنوب فیلیپین را لرزاند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/657337" target="_blank">📅 13:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657336">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e513ad5e.mp4?token=dOu26qHdsCB8r2i7zhsvfp1Ap5o5qXl-asl2QYWLt75GXIqu5x-jNQMhYjD6P5KOmKDpLeHz1_REnsmL3KOpsWZD_6EXTfl4xEs0aqFaJrKSFNy8GeabpLHibXugSwqxrlSoUglhAhujT6OeAbfC2Xmk3m9XjPTgiPAA1_LPtHlE0jSAGHo8O_tR0OXgChi3-5Y9c_C9faLIx8J0GVIAzF1C48YyhPlvClyCQ0gbmF4xPjOg_zXwtm3LdoV95AcJIwKnQWZNGieu-fq9Kqgz-UzL3gRjzC6eWdQtJqGjw854C0Y8bPi7I8HQ4BSKs7goD2IKfght5bOz7y9CXtEwyTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e513ad5e.mp4?token=dOu26qHdsCB8r2i7zhsvfp1Ap5o5qXl-asl2QYWLt75GXIqu5x-jNQMhYjD6P5KOmKDpLeHz1_REnsmL3KOpsWZD_6EXTfl4xEs0aqFaJrKSFNy8GeabpLHibXugSwqxrlSoUglhAhujT6OeAbfC2Xmk3m9XjPTgiPAA1_LPtHlE0jSAGHo8O_tR0OXgChi3-5Y9c_C9faLIx8J0GVIAzF1C48YyhPlvClyCQ0gbmF4xPjOg_zXwtm3LdoV95AcJIwKnQWZNGieu-fq9Kqgz-UzL3gRjzC6eWdQtJqGjw854C0Y8bPi7I8HQ4BSKs7goD2IKfght5bOz7y9CXtEwyTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا زور کنگره در جنگ ایران به ترامپ نمی‌رسد؟
🔹
کنگره برای ترامپ در جنگ با ایران محدودیت گذاشت اما ترامپ می‌تواند همین محدودیت را وتو کند!
🔹
نکته قابل توجه اینجاست که کنگره می‌تواند جلوی رئیس‌جمهور آمریکا را بگیرد اما با یک شرط مهم ... چه شرطی در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/657336" target="_blank">📅 13:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657335">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
اجرای متناسب‌سازی حقوق بازنشستگان در سه مرحله
عضو کمیسیون اجتماعی مجلس:
🔹
متناسب‌سازی حقوق بازنشستگان تأمین اجتماعی در سه مرحله و در چارچوب برنامه هفتم توسعه اجرا می‌شود و هدف آن رساندن مستمری‌ها به ۹۰ درصد حداقل دستمزد زمان برقراری است.
🔹
حقوق حداقل‌بگیران ۶۰ درصد و سایر سطوح ۴۵ درصد به‌همراه مبلغ ثابت افزایش یافته و تأمین منابع پایدار برای پرداخت‌ها نیازمند همکاری دولت و مجلس است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/657335" target="_blank">📅 13:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657334">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpBFD24VsSVhmkUQamrYTJYTz54EQaENxXSd3QD90vB3tGeuSN07dQHtZivNg05jo5wfFtoO-xWbrc86O2UyCA6lco6MOdi8jQmW-RsR4vuzQGUpUU36k15mBV_zdrC5G12UhNc_oNSLce9on18q5KLFYL1si6JRGaBOEOq2qoqn06PEDzT5f5MH9Bnh4iYCNbiEobOuHGQrbUMx-f2MgONTnXSy6NJSYnrKe8TRicnjmM9nsRF0MSqMF2hkB9nydDnUkBgDd8ZNsGc7bRWIsVF1PV-7k04YDaiYBSr-VlOQv2ArgovD6jLN6RkrIXVNNMaOq5nDtX3iIB7fKBUEFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی: تا لحظهٔ پشیمانی دشمن سکوت نخواهیم کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/657334" target="_blank">📅 13:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657326">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ioPgNlCtearyBg-4raqXj1tLgov-HY7wkTdA8xi1uyy-SbdQwE_157c3nm6-iK7i8EE-3EZiU2i5HTeI53elXQ7PT3ID_2RJHEeRnjJBUhnox_DLdoat2ZclIh8iAobbob4vy0eRJniHABYQyX-cJkMsVd2BLZQNp3ppiI9XtWhNyU8QhQTlAXmAbaTnXnY_5P8QhI50EKcXdNSHJU7DyynCApawAti3Dx_36YC_CTdkqXw15Zfii6K_O5i6CrZuTr1MB5H80waoN5HF3JinSL3MAQONmZvSs6zP12opc_uZnaIR-AtTL9bE2sHJK2ck_ft1PknuZuIT6cmIVhUJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o7MdCoZ2-GxuZ6mwaptpSlahuzkYBHXFGBrUcN3YtU3xaZCgL3uEVwRjR15eK8Txi_AOuXOagoQxG_dVy4gjitt10SAXSmP8XgxKv_ZGHCc2SYkCX6mVn7A_HThklc9Q-zd5o1hVXxjIq3NY68uVbosXWr6e3jDw2xkCQufHZmc0uOGBYV-SLxZghFxD5jNe1FtaBltS9EBMno8ShaNQ-N9rdHMEQWXteF8mn8-mmJXqWMTrfdQIEPzHLD08neLvS4XI6nwqlLJcCqVyrP1H0LBuOLb7e4s0lvXlmYDWHWKvqIW9TLSrQK6hofrUS8Iz_JJ0jT3NyhV8OAzlCLII7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i-EravKZxoWK2wUSj-Vsl6M1s3REHKo_cxQU5UWOVsW-8auDOH-GWCRdXNbXfs989J5kUBXPpO45DjdRzy_NJHT5nvebkbL7uluxa1IutTVF2sVLbNmeVi7smLOpZaNHmoVMg17uwRT82OfA0g5fT8BhNmIq9usK861fqJyZiqX0anyksQ7wGVIWewVy4MIYm2RQP8dpt2IlnPUOtMm2BdVdPHlzO0dYRQT93Gmn-ol08NEEn_--GXNtqKJjo9QoMsswD06eL0d2KL43lGgwREKeaRDUsqymn2GGYqsmtOywZEwVe-1wHVk7LMUAsKEbwypys8AMcu6uNLsIzAQl4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QvWgrRtlHqpB3UmE7nRsHifx7HTdC87LYT72F311prgQmaNJC3MI2G961BydaCrq6dtgMWLry1cYgoAOECcxOF5IGisQQTHnnQv7WFauSI3itKdgav2HephAbFfU6BDk2DnQswva5NLq5yS-Ajetfmqik68QDjfsIiJtpmGxliEdsOulAhuAZiynswPNxBkDwCO2qeUrB0G0mPFlj8EInbIri1tYC4vhVDAdv9PpM7z6zzbujXaZDFtI6RsnRt00It5nz-qOmzn15soH9Z4RU1vaV3f66dzFCn7QE2geAdy6KtqyMlmrijSl5SC0PKfILUiuPow_X54mvqj5Ab21fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B8Koxaf7vH666goAPVZbGz8rNoYJ_5hCZgl332gGQudB6ZMbP2fbMT_iHu5gV25dEKAjokeqFQHNQY4xm-uQwJ_R4J9hx7r0F5oBgu_xOO4CIpzy5V8_otweFDFdWMWrBxL2npxS3GwaVjqPozjibyepXGzWFk62Vy2167ulJfnYOO5WQanDSkdoaJpCK60lR7_EjscPpf2HOZiMakQDC7-d8pAes54o0Pnf21yrfnQ8cBgZh1_WWQoaQxC88z58v8vHBAMMHmWwTLCFUYlHtO122pp-QgWWIbl5yKcwL2PxqOdoGm-HXTq0SaoTJXSIlpTvEOilQgErz_M050jqgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JT7w9ew69e0-Z3dLzocFL8j2O0qIXE60ptr7DFv9n_vX05_utxHJUZ065uLU-Ab4JunN7fY-fxoeONsIZ9Az5hpJcVBau5P6spOHMVygf2rbnhgLEg4zo_lyTfjyS1aseRgMDj70er1ZiGYKAYKd6fVjWwxtYwyKP__lrg4DVwRGlxGCelyvkksDh_oglDzRMTwvbVX6t11vjb3-xpZLp6PvxxSjpNA7dX8Ggp4tS8uCVWUpbdYlIcgp_dZwNmdmQ4MOA_PLb1vU7__DEpgcVTQryWeqZjHcFXjfJg38zOYHklVoJS4EKm4xnbnoNJPp07bT7P3Jpca4GsoXRwAlPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F-BIcFPTO-FpWcIn2osXscThAo0haZtSd56Bfr7ecAB0wOc5Wb8oSdpyYAn-WIfc60h372fgizhkBMXo797PMOu22x3naLzcSBdUOaKCYfSQKHbzw8uNorYBhSY_92WvNqo300KbcWpc1wpqMHa8Wu__BSl-Y2coRcfcC7SH1gzT4QilZfwlB3tj2ac_zY-AgLi8CUkofsa1e6uoN4UQWsx_Z0TLq9XA97vFlPBoK3TPIEpdWakcDD2JlR4ZJ58-3Y6tvviGrilhfz2qaxu46K8eDLyka1j7VIom09mSjHa8IEK4d0zbf8KhXky0w_Vsit17gRjv5yVfnpiv6U0ZMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rf_GrJEfWOxv7vD-PekO6ZSs4dbrmz8pxtn4U8Kk5kst_VhQ2XxKfqzLwT2Ye6WeTvrfzvqSMWsNVMJT7afIPuzMC7D5Y1Lw-6Krmsi4kdH0UJ2gcbftXLRsVXx-s3OVBpAv6G7YLiYhRkfJ411acAVsRtuhmjiAF3uWPtQPxA7XDLRR1wX3hW8N6tBqjI4EsqwA2gfp3D4CqwD-qltYuDE6YJs4j9nHBcTKmeFjSXdFT0_P1YrX_-iQWwzCgt-VUkx4R0NMXTqkeWoCAsi0BzSfDd3l8tM-lhE9ObX9_L2L6TWuoS94KLmo8cEd7zRW4i-dE4aXNoYJAHeAko-IFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آماده‌سازی حرم حضرت اباالفضل (ع) در آستانه محرم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/657326" target="_blank">📅 13:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657325">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
اولین واکنش چین به آغاز درگیری دوباره ایران و اسرائیل
لین جیان، سخنگوی وزارت خارجه چین:
🔹
پکن به شدت از وضعیت فعلی نگران است. از سرگیری خصومت‌ها به نفع هیچ یک از طرفین نیست.
🔹
چین امیدوار است که طرف‌های مربوطه به تعهدات آتش‌بس خود پایبند بوده، شتاب مذاکرات را حفظ کرده، متعهد به حل و فصل اختلافات از طریق کانال‌های سیاسی و دیپلماتیک باقی بمانند.
🔹
آنها باید شرایط لازم را برای بازگرداندن صلح و آرامش به خاورمیانه و منطقه خلیج‌فارس فراهم کنند. /خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/657325" target="_blank">📅 13:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657324">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
رژیم اسرائیل ضاحیه جنوبی بیروت را تهدید کرد
رادیو ارتش رژیم صهیونیستی به نقل از منابع آگاه:
🔹
در صورت فراهم شدن شرایط برای هدف قرار دادن رهبران حزب الله، این رژیم در حمله به ضاحیه جنوبی بیروت تردید نخواهد کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/657324" target="_blank">📅 13:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657323">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
یک کشتی هندی در دریای عرب دچار آتش‌سوزی شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/657323" target="_blank">📅 13:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657322">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
شبکه ۱۲ رژیم صهیونیستی: از دیشب تاکنون، ایران بین ۲۲ تا ۲۴ موشک و انصارالله دو موشک به سمت اسرائیل شلیک کرده‌اند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/657322" target="_blank">📅 13:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657321">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d2ec5f1.mp4?token=qJ-YCYOCoI6iLF_TUg-phPl239Poi2hRr99Xe_6lGiduf278Mslde1tu1K4CUFWxJf-z6myyiJRv2j6lj_b7aHBIjV0mTTg7H5xeldCNElz1tjDdKbDJ7ICk3f034Rgtph5S41Bybe7nUBnslWkalsjsvI2s_rv1dYFaNmRib2u_vERG3uuETNxcd85c9gM7PrEJRRCOyN3N0wbheM0agxdnBadXoPbZSiVTvVrouw6oZHl9FiiR_NaF5EW6KvUxTF-euGrcyzVB8Xw-VHH-HZznkkUdODJzJ3Uaz5_ncXrpLQy6iZujJFiFERKkd-SqiEDWYJ1UE5SRC-PgsFrOnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d2ec5f1.mp4?token=qJ-YCYOCoI6iLF_TUg-phPl239Poi2hRr99Xe_6lGiduf278Mslde1tu1K4CUFWxJf-z6myyiJRv2j6lj_b7aHBIjV0mTTg7H5xeldCNElz1tjDdKbDJ7ICk3f034Rgtph5S41Bybe7nUBnslWkalsjsvI2s_rv1dYFaNmRib2u_vERG3uuETNxcd85c9gM7PrEJRRCOyN3N0wbheM0agxdnBadXoPbZSiVTvVrouw6oZHl9FiiR_NaF5EW6KvUxTF-euGrcyzVB8Xw-VHH-HZznkkUdODJzJ3Uaz5_ncXrpLQy6iZujJFiFERKkd-SqiEDWYJ1UE5SRC-PgsFrOnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی قرارگاه خاتم‌الانبیا: دشمن ضربات سنگینی دریافت کرد
سخنگوی قرارگاه مرکزی حضرت خاتم‌الانبیا:
🔹
نیروهای مسلح ایران شامل سپاه و ارتش با آمادگی دفاعی و هجومی بالا، به وعده‌های خود عمل کرده و در موج جدید حملات، اهداف مهم و حساس در سرزمین‌های اشغالی را مورد هدف قرار داده‌اند.
🔹
ایران و جبهه مقاومت در برابر هر تهدیدی ایستادگی می‌کنند و در صورت ادامه تجاوز، پاسخ شدیدتری به آمریکا و رژیم صهیونیستی داده خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/657321" target="_blank">📅 13:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657320">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
نامه ویژه پاکستان به رهبر انقلاب تحویل عراقچی شد /تسنیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/657320" target="_blank">📅 13:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657319">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
منبع نظامی: ایران برای جنگ طولانی آماده است
یک منبع نظامی:
🔹
ایران برای جنگ طولانی‌مدت با رژیم صهیونیستی و ضربه به منافع آمریکا آماده شده و تمهیدات لازم برای این موضوع در نظر گرفته شده است.
🔹
تصور محدود کردن پاسخ ایران با «تنش کنترل‌شده» اشتباه است و تهران سطح تنبیه اسرائیل را افزایش خواهد داد؛ آمریکا نمی‌تواند از مسئولیت اقدامات اسرائیل شانه خالی کند و در این زمینه هزینه خواهد داد./ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/657319" target="_blank">📅 13:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657318">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
نماینده روسیه در آژانس اتمی میخائیل اولیانوف از آغاز نشست شورای حکام آژانس خبر داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/657318" target="_blank">📅 13:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657317">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
انهدام پهپاد دشمن در غرب تهران
🔹
پیگیری‌ها نشان می‌دهد پیش از ظهر امروز دوشنبه یک پهپاد متخاصم در غرب تهران توسط رینگ پدافندی پایتخت رهگیری و منهدم شد./ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/657317" target="_blank">📅 13:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657316">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGaMMBX-UFCVin9gBA7wLmhaPbOGRMu3eVheKC9pxryDS_Agz-vjfsU7leYqwKyWdYzNX9OBpkP8GZ82budMYA1Ipf0pOuzoNlk2sa-pKa1EAxE3aPXw7oXJQ8awfmBexgEROI-HMD4_krvl4cWJUcgzqx39WnmxCtD9lNRMRFSjwRXahQlDliTX7gd8wx0Y--1cjwUrD6gZ1CIGzUOD_Gol0MGHQwrB-ojsNuU1xRNKNJ4Eqrf_yesDj-aFP_CNiiJx1FGCMyfbtoOyulTfqqnv9UKggutm3q62dYmzzjAETP7Yo7Z2qBb0u-0QWaVl_k56OprZwNLxdrmbVQkgSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ישראל תתמודד עם מכות קשות והרסניות יותר אם תרחיב את התקפותיה ויחלו התקפות הרסניות נגד המשטר הציוני ותומכיו.اسرائیل در صورت گسترش حملات خود با ضربات کوبنده تر و پشیمان کننده روبرو و حملات ویرانگر علیه رژیم صهیونیستی آغاز خواهد شد.
‎
#WillPayThePrice
‎
#هزینه_خواهید_داد
توییتر خبرفوری را دنبال کنید
👇🏻
https://x.com/Akhbare_Fori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/657316" target="_blank">📅 13:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657315">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
سرپرست وزارت دفاع: پشتیبانی از نیروهای مسلح با قدرت ادامه دارد
سردار ابن الرضا:
🔹
رژیم کودک‌کش صهیونیست امروز بیش از هر زمان دیگری به افول و فروپاشی نزدیک شده است.
🔹
تا زمان تنبیه متجاوز، لحظه‌ای از مسیر دفاع از منافع و امنیت کشور عقب نخواهیم نشست و تمامی ظرفیت‌های دفاعی و پشتیبانی در خدمت نیروهای مسلح قرار دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/657315" target="_blank">📅 13:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657314">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_hj5q__wlrMrXQ4LjQ2GCycqWrLbLhFQv-4XAqX2Vbu0KNnHc1GcLICF8QGIAPgLoUWOw7TPv7Rfu8z1AtAC_hxXlXq5OVhDY69DLSLDwCDuWxDmcd6SFyz5pAu0ajRc1Or85SBmQ9xyLO1LVtJbV4SO9RHg1LttggE8jR0ZQiE8k2Wiu_In2XYp-QyjR8ZrY9kWUKM7L0LHjn7hwnR0ntOjfcCTsOc4eldCH_EO3kwk6tle81Gio2XIN3sq4LvN27M44hKHnppsYB6UCBFoacrFzB7atlBwUQRB6bELH7Sw0zjWHwRUAsVJSS7lEkWneySm2eBFY3OscG4JtMiag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای
ترامپ قمارباز: اسرائیل و ایران باید فوراً درگیری را متوقف کنند
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/657314" target="_blank">📅 13:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657313">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfwanIjQ9Sd89Bx-AtSqBKCrBzmJw0CH6EuynwFpyXtYGfQIhcR4ciaXNQA3w1-yBIbx21dFvRNUa7AdNYSipPpEBfhfLRnVb5MTuisr6tYsIeZMJhsqlqEx1BS76xTsEi48ZTIMOCX3CR-Thazs9ryVva2nnW0vwGCGo7rl8PQL0DhhKqRloT31qdeyx_w9ffwRE9s8brn7faO3Ov_Imvc3PLdP3427J0r0lX2zO-a7KOcTjX1qINFrdVSg-MFU8nFziFysLW0zV_AP-FQipGL4Sfxxz4EIwZYgllH0rA-5o8WDEt6aj8DmmlRtLmOtIUrdCCeNH8wq0LM4P7JA7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس مجمع تشخیص مصلحت نظام: تهران فصل تازه‌ای از سیاست دفاعی خود را گشود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/657313" target="_blank">📅 13:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657312">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
هشدار دادستانی کل کشور درباره انتشار تصاویر محل اصابت پرتابه‌های دشمن؛ با متخلفان برخورد قاطع قانونی صورت می‌گیرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/657312" target="_blank">📅 13:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657311">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
منبع ارشد امنیتی ایران به المیادین: معادله زیرساخت در مقابل زیرساخت تنها شامل اشغالگر نمی شود و همه باید به جدیت ما پی ببرند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/657311" target="_blank">📅 13:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657310">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGeXoJkOz3XqzA_OmmL-AGjB0S6dCjWbHFMnwPVF5elO0RaTfjpzC06mcs9tL3wnF5H8vi0jwWfvPGBSNWGRt_swACBK-GlIDjdeoxC-pD737ZzJEqSkIelqZTVw54GYUOOxACueSkbV0-t2aHFDJv7-2j_9yO2TKeDKwViaURsrPJltI8BFfys_mNPugKcHg8J0HYUJovkkJPSzZNWfUHJAwumcJQqF0N7wrSt5GlPkdO_F-JcX1LB8jIDIBx21PaFpRUn8uhCLH5whtinnMV1oBMIv0Cz-S7AMsDAFp9jTRNTuKTcyp5ccjIGPBXGKLT3bahLbq7eoPmbfdxqx_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکورد ارزش معاملات خرد بازار سرمایه شکسته شد
🔹
در حال حاضر ارزش معاملات خرد به بیش از 35 همت رسید که بالاترین رکورد ریالی ارزش معاملات خرد در تاریخ بورس است. /خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/657310" target="_blank">📅 13:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657309">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ایران در حملات خود به اسرائیل از چه موشک‌هایی استفاده کرد؟
یک منبع آگاه نظامی:
🔹
ایران در حملات شب گذشته به شمال اراضی اشغالی از موشک‌های نسل آخر خیبرشکن استفاده کرده است.
🔹
سرعت این نوع موشک‌های بالستیک در هنگام شیرجه به حدود ۹ ماخ می‌رسد که انهدام آن توسط سامانه‌های گران‌قیمتی همچون تاد و پیکان بسیار دشوار است./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/657309" target="_blank">📅 13:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657308">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJMsOQ0aqoYpuAPt4EwBlCCBjBI8CjnExPmnCH7wZcqkz9FVZe2BM1lmgDoWr8KLrCwBnn4jPld1TKLYlp8Y4Ai1DqPLr13frVrZc2iktFvDUIbyttBt8TPmx4WYIv9cSa71jHPZP4AhIG9xI5ZIGWe4TL1gyY83qVhlaX-2fxQlNWJkd7wSA4JHzT46MBBc9E-wlua666haUL07ESN-LmyOWS1L0tMenbvvSyJw4ovSzzLXVhplobFf5rYoIkS_XXyjJYqirsLOJFLv7w540EuMaI8yLaGfo8Dj0JRGZWBomapxJoZHBmvZH6M-6nqjAUmM5B7rUqi92Ze2wx12cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس منتشر شده در برخی کانال‌ها به عنوان انفجار در تهران مربوط به ابتدای جنگ رمضان است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/657308" target="_blank">📅 12:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657307">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYD87MD__5T_JR2aCvEjt85UKx_SPdzvrcPmY8jY-lyHfClB7FZGG31ls7QQdTsFTCmVhdD_fBkCmHy4HZkGi8L88pg4UVOtqvrYqBicFX7d79T_2RIiaeywVduM3iPR4qzezEwl0V1OIa_p7lEsmHRTZN71iwCV7vZxiXsXPdHz8ZdPHdFj8WPnhLLvOlwKHppOjjjZdZyxtmLUpyj8zZCOxN1kLnhf8A_nhN7Gqb5888zWeQl9S8nwEyz6C4T1aT-vkQT-B8IcVzGvFeSg4efcs-2VPO9G01wy2nuRq3Psro3oUYn4jBpiQzIC0_swcxOI9zVbl1EhpjYIfDFCQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویدئویی از لحظه حمله‌ور شدن الهه و شهربانو منصوریان به اتاق ریاست فدراسیون ووشو و شکستن دوربین مداربسته
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/657307" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657306">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
هشدار دادستانی کل کشور درباره انتشار تصاویر محل اصابت پرتابه‌های دشمن؛ با متخلفان برخورد قاطع قانونی صورت می‌گیرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/657306" target="_blank">📅 12:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657296">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXixfP5_XVMElxYCYsQT5fUr4Bm-2CA-sRU2OUjUrd-T-nQ3rpn8HbwmKKC0szlhXXgM1EiqlkTM_vlHqu5Lo07QEh8fM82RvLPe-knkEZk74Cx5a-4VRssM9vu2C66KxYw3XaGIm1zWd2rucxxpf3MvZNq7s2L1VsQyZSQLIyOcaU8II8qeKF5-0VlmlywIODP9ERQLAvrVgqfhGKmMc_3QhBWABGEkcphV3UKLjIinFVvd0feTc7Zji6qpdXolcuAXkGrmmHafVmRo-qjsc1mh0FVI5cBIMFQEaCNejHbDypnPT-yI002EmHAoPxsY_CQXYeSbl0IOVWNmgHphEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NStMAv_OtX7CifNBV6r7zFudJq_oGeMr9gObh4tYP5FAWSPFZctGSxXECTWvYdLZTgWjP4VcjTfNmDLX8dOulFHJQ3Mkb0YzKJDw7lMKoADdaPf4TjD2cgRNeRhbOUYjm6fTDBj6bQCqJHWza9Eaxhc67WZO-1VtpXcSgnUMVbkORcIxhe5easeh6boO8ZicjDsYyIakcF8aVNQk8ytUTKBAMqZ19P7Bcpnpv0JA5wS9hKN1bmzUZyq74WMAAv-6W7JdjQxyjSm3iOLupCDj6oFIrPLBDRSL1JOLz902N5Qff3oSqHWlmqhgdXRWDBTYT7pVo-5kUWdR4pojt8SN7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hUFpAm08mZFhjkV1V_NrorHkJlxkS-lbWsWWQm-DBdeFH4Tucu1QO4REf2AtHQ_SnlK-9KfBn8qkIB7v6SWG33ljAhPHlY2-3VCrkIo3oXt2EWZBDdcfO3EUwPpUeAKS0TgDc-uXvzUmsntakMGNGhd0w0eC9xNWGdV55PPZ-z7Fjm81Mc4pvZ2NIj8gb4Q39yZwwr0WFRlLSz7wqoZDynpC4CoJq8CD9uwuQuMxPcmeGTNze90MHK_w7AfEme0OST1PagOVR8llugNe7gasyaNvtHwP562LzDUsZ2xaT53y8w21vg1R6HREznPi5JKdiytkiEgHkk2PEXX75xNNPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cPQZWDKc0AsXU2pNjzOUuBni00laJgba_Ag0_OHbc5RfwrZF3jORxKpz7dvrVP52rqxJ2Hb7P5eGCyhYshbGec3TPhY1KmQg_K8w9S_1klbyGI7Cdw1CfO0lMoTGjEy9htZJzOzwJrU6U3tXs1dzy1PUDimtLnxeW9sKRo1YxxiHkZHNaRxDb-HkrK-PfppIRX1k1o8p8G6ZwtQKTEJffYNe1s-7t0UbXknVUcEvEGw7tKE1yINlYfdNZFhfoD-LTZks1bNQ8iH4s25dJmozMW3nQWD-bNvfPuozGdaJkj6BJAEuCfDyKgOa4qOIDOnNo8bJkt6jyoXd64ZRdCM3OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WaLPi9MviO-jWfAf9_PFxy7SDbpVSIYGETMgSKJxDQ5TwjejbX8tdZ3D75WICGasrd_7X4a-1n2VLCaPAvyOywxCwl2yiq904r7BsFtCU7oril741E9YjhMki9NlhmhcjXmjtOeaG6-8YqoARvNliklWw2Iqw1C1O8-SfO-Z-VNdVKbMse96jMzOdJNWHCuGwUeUbwsHjPbCxopjescZTNROlQrulBBz_nE7FZXFtJ4I171NNdzfAJPkGcXA4fT1278kHSzYPBjEz4TqgKzqQ7kH5R3b8TEyJ4ptPX7iQ814c53VjJ75qwNxr3UZ_SNJdXL5UQNUWdXcxq88usSndg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZaCPeIA-XM42mSTJNgWIxA2HUhXT5SwCNXBrs7kBBeYbp1RRVeV5ouf5OTxRn4YSSOpyiAYO9-hvyiDeGPNJHjT-Xqy-Dlh8VwzgnCDICOWv8ZrnHboxVDen8q9GZhhj5YsQXfjNak-zVbDI6hfE3qrobY3ZSY7XsV59HrskfTKRvSR8KOc_8u_ckCXlu8Zt2o2S7G4xnt9S-L_mWo4zR0EbODNzYKHkLuL0UCKFo8VLUmcj07A_YiEYkP7IyPtH1gquESg0vlu3soXWjf-m4Vu3ZsRPgoCqnTA4bhlbY_HwOLwBFPJCNZOIPxjmVib3Ae6q6M8p8NUTBPSwIQlYzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dSU4HdvrFWU-lXNtJ3-uJJDh2SiZ10JkVKE_JyaKFj29w0oOog81pDQPs_U3_DMEsVVeayD__kbCojhDJYy9Pu3SgxyhKxv43bqJsXblH138tCeUMfYb8RdqdCl6DnvcBiHu0Vd7a-_ybTkPBc5BNdpG5b6Mjze6JWcfXnW_4fKiIkTtXc7RWfo29u5YWYE8efF4c0TJUDEdZXL-mY0GKTSjSeCo8LCTgJYBBOEtiMlfJ-Ne4_vhPJzBa3A0tpIwosqLBNW5t6W7lyTsQ7HAyFhsEwdVNYzVsA4Jk-E-ruvx-BkASJrS0iuFtyb9dfbk_AbKvpnIuQlwQC9X-wHWMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BMUP4It2fdKo_wUTRHJXOgydxbiQ7eJdas7p4wOVIQvSdSdqElIN7xofTUnOfEEVEptqucPB8qFtCKxhk7usyBVKUkEOJyr7GGsz97aD2M-s-Vujw2yS14cjY7EyD9HddoYcqm9j5pgb6g82AIKwMmbR6hZIRRRA7pwCaG3_Qajstipqiz7SwL_kKwFZExwDHQ7eMyE4fnIr_R22N5jJMHv2Kjd0Q1nxD3j2SVpIi2hIkOUnogjFOmbp4eVWkxBcwQ-dFgNs8lLnZAeqLxDETWPk68UaDwoGzWvJAmjwePXshXGPcU_M5bFbod0r3hsV8HuKVIKpcmzYSIl48am0Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OkGLHsEPeryyt66K7PH_39IAVFFGpufDUoPpRPn59Tmeqg6MPsF6uE5bxMCKo6yh7UsnH1UAEvxzoRwvPsRIuD8Ydk435XbzKG0aTds1ZlP7OFcW6AK09_-zcrmR7riFFfXiSXxvB9YrGGHPQLqJHvHqMvFj5_NQxXPVg5TOVsySdUZXLRbeKif89xsmHZSTezPOzL-iO9DyHkdb7zS7QenWI7AAucGKPr0Gq1x5whJR8nSOxwPMaO0xaogdNdZ71tuGPLJUmEGZC50amZSOK3Q8rFtWyAqSTWmXBZEqIXyaYLeXrqLmxJJ1WybnfOqvP9tf-QjB3SCAWvmEjEihZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V8KeLscyQYwM5tfCWHSBnK9Wb6O2w602zciqoa8KZzQ3IkwJLuFiS5tUXdUlXZuWwnKrby_W54TQCugpy4XCe-KTIx4g4Acm3nVh5t7Zj9XWx3Z2Gg-m8rL8q5UGiLfF7dBi0k1uBgJ72rFfjaTf0pLSn1E1TcdR_N98AzZMjA2f_MTY1x0gXa7_qC1fhfuiS3chjhw_2RQBu9sMlVPq671HfmdxlUgxJ6tRUfi6zcsklTnmBFmk4jNbfkL6gT4jCB0RbLUhAjbWwAIfd55zmZ6tGq8dfIiZsiDu-k-udgZL3Ol0mVJZ49F_W1w2TOJ53IMTaXIHd-I9CTQN0jjs9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دیشب از مخاطبین ویراستی خواستیم یک پیام برای سید مجید موسوی و اپراتورهایی که پشت لانچر نشستند و قلب تل‌آویو را هدف قرار دادند بنویسند
🔹
خداحافظ‌تون باشه ما که تو این اتش بس لعنتی.. جون‌مون به لبمون رسید الان چشم  بچه های میناب و رهبر  و مردم شهید چشم‌شون…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/657296" target="_blank">📅 12:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657295">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMsMJj0odYErsrdHOzXW1xmpUD-TscsRLTUpy6NzQyZ6bettOCJsH8Dt7j9E2QNKalPnuG7Gntn6xHj5dD260L9INaAGQ7v9vj7RgilLVOkC4cKIjgZJyickF2ihJS6BWzBB6Ijz4tPdJ2zaAIxAW_EfrZ0CFsguceicmVD0uvwD9XeVAKms2D3AbNBZ9cWyppi-7jiGAwKL0xhGhKhxisWWIOlN5IBdQjrzDTcHzDAUG2c54wB7MQytCxpLJKZSQr1swF5OYul3aAApp4sKWBBb05x1yYS0k0JP0_SuwktRfKmEFnZJJ5S4cGdkiVSOYixKmAd4ij-V4PdwSbjEzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گرین گرینوالد، نویسنده و روزنامه نگار آمریکایی: برای ترامپ متاسفم
🔹
وقتی مجبور است فریاد بزند: نتانیاهو رئیس من نیست
🔹
ترامپ در ۱۸ آوریل اعلام کرد که اسرائیل را از بمباران لبنان منع کرده، اما آنها به او خندیدند و روز بعد بمباران کردند.
🔹
ترامپ می‌خواهد با ایران به توافق برسد، اما از خشم لابی اسرائیل وحشت‌زده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/657295" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657294">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
عملیات موشکی حزب‌الله علیه نظامیان رژیم صهیونیستی
🔹
حزب‌الله لبنان اعلام کرد که تجمع خودروها و تجمع نظامیان رژیم صهیونیستی را رد شهرک «بیت یاحون» با تعدادی موشک هدف قرار داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/657294" target="_blank">📅 12:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657293">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHO608U3JHxSPIUVyE14g-EB11b-JjSO95xGeqTEqhqblF5CQ-uvdxeW2pg6crZG1YaZg0SRkRiIjb8frBMT4p2kq3K--6pRkGxl7vyCFjdLH-5bDvaTGXzdgUhB2lTlWHSJ2TzZqr5-foxseWTluUA2vaqGn-S1Uup5vZWhpNcUdf_ktf7j8QRidlLlcPruJaICLBF0MzjZA9Fu3wzL2NvN5HjeBHY_rlb9ZSJJ6NvOKE7gIoxW_GBvXkBV3jmP0nFsuIhep0DXx0afEeKipa3KBAlNtCqKlADnxxwpaweGrQ0Dqs2GADNQatQSLde3mmPN9PTGsvwaq-bJ7kcpvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابراهیم رضایی: قوی‌تر از ۹ اسفند آماده پاسخ هستیم
🔹
سخنگوی کمیسیون امنیت ملی مجلس: قوی‌تر از ۹ اسفند آماده پاسخ هستیم و تا لحظه پشیمانی و تغییر محاسبات ذهنی و ادراکی دشمن سکوت نخواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/657293" target="_blank">📅 12:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657292">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c6693569.mp4?token=jfq5zm-t_CTYKqY8et0kOfW4FJniM_mGT4ZNr5kTvZipAyYtjDZT3F2DbDm90c2IPmSQOgXZpdUpyiGbIFfVUh-CDn5yx7m3BRSRbI8OqzXStwB97oCLFyxVHa_gWoybH-u4UGn0S_DtmMzjuBBE-Xzo835dPl9saDVx8HV-XaSy4zn9u0UjRqy4lf74sjwuXMfQjgjfmno0BjMLwsrDKZweT1twA8Vkmnby04cfmQ1GodJjgA8wnVBmEA9JSTBxmntqXGvbI7qf1tm4_-o1r9b5FrRadaloGmN35THp0lOvhIxOc5iVGZzsDPm3fkFNdA0oZg5DRHBGVea13XQ-EBdAD9RZcGE2YCBx0JC01qNq8gy2nBT2VxIZFr1lLLuNSSVX1zIWMALKNeBryHIWd5Cv0W_iZVcrHg7Rbx5I9yTq4TCbgY0p_CWBt12nxOwwH2ni71db4yFDMa2ncTo1Rg_JuTq78nK0IowDO9l5IqsYe-XFwqPOginociayA7glYLtLi_kH-_ryAJyOo4Rk-IHRwedD8OOfvhGaAv6OA3xqagD0i9umm7utx0cFVkzsKsDptxyiMQS3fKks3BTzjqsz2dCG1PfviFDkElHcznITeShO0p6S8CKcuaZrOrqR8tn_ENwkE8ahKyRhmkrGK6NuabRHltH42HTxkoP2_do" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c6693569.mp4?token=jfq5zm-t_CTYKqY8et0kOfW4FJniM_mGT4ZNr5kTvZipAyYtjDZT3F2DbDm90c2IPmSQOgXZpdUpyiGbIFfVUh-CDn5yx7m3BRSRbI8OqzXStwB97oCLFyxVHa_gWoybH-u4UGn0S_DtmMzjuBBE-Xzo835dPl9saDVx8HV-XaSy4zn9u0UjRqy4lf74sjwuXMfQjgjfmno0BjMLwsrDKZweT1twA8Vkmnby04cfmQ1GodJjgA8wnVBmEA9JSTBxmntqXGvbI7qf1tm4_-o1r9b5FrRadaloGmN35THp0lOvhIxOc5iVGZzsDPm3fkFNdA0oZg5DRHBGVea13XQ-EBdAD9RZcGE2YCBx0JC01qNq8gy2nBT2VxIZFr1lLLuNSSVX1zIWMALKNeBryHIWd5Cv0W_iZVcrHg7Rbx5I9yTq4TCbgY0p_CWBt12nxOwwH2ni71db4yFDMa2ncTo1Rg_JuTq78nK0IowDO9l5IqsYe-XFwqPOginociayA7glYLtLi_kH-_ryAJyOo4Rk-IHRwedD8OOfvhGaAv6OA3xqagD0i9umm7utx0cFVkzsKsDptxyiMQS3fKks3BTzjqsz2dCG1PfviFDkElHcznITeShO0p6S8CKcuaZrOrqR8tn_ENwkE8ahKyRhmkrGK6NuabRHltH42HTxkoP2_do" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔰
واکنش یک نماینده مجلس به ادعای ثابتی: به مردم مبعوث شده ظلم نکنیم/ در مذاکرات اسلام‌آباد حتی یک اپسیلون از خطوط قرمز عدول نشد
🔻
محسن فتحی عضو کمیسیون اجتماعی مجلس:
🔹
اگر فردی خود را ولایت‌مدار می‌داند باید به گونه‌ای رفتار کند که در ذهن مردم این تصور ایجاد نشود که میان مسئولان نظام درباره جنگ و مذاکره، دودستگی وجود دارد.
🔹
ما معتقد هستیم که رهبر معظم انقلاب آنقدر مسلط و مشرف به قضایا هستند که تصمیمات را به درستی می‌گیرند.
🔹
در اسلام‌آباد دیدیم که تیم مذاکره‌کننده ما به ریاست آقای دکتر قالیباف حتی یک اپسیلون از خطوط قرمز عدول نکردند.
🔹
کوچک‌ترین خدشه به انسجام ملی، ظلم در حق مردمی است که بیش از ۹۰ شب ایستادگی، پایمردی و تعهد خود را به نظام، انقلاب و رهبری نشان داده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/657292" target="_blank">📅 12:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657291">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29baaf2910.mp4?token=IUkOMNvcKncurPlC9AU-QtQSdvG-DLONl_fNiaNwc98UfA-JoC28Y8eF5KstrYGzBzci95Koz_DZHs58azmiNyal8Ze2a2GH93PnpiE7SxEH-hk_6-op0f0SaT5ED3M1O7VjGL1OP7jX8p9xE4VNI5YaI-8jNTLQNwwm0w4j9WqTzeopPfMXMAaNPC7sCAujeqx4cnhrzOb-_xt1Z4rXY9JktErziljmONyITaJVK1iOHN-IYxovP94fMZHX1qv0BueYrJfHo_LYkmTSvqEoA4CyYnDXOXsn-dnWUg79ah7ODUyIi_uJ-aRkH7XgEbALOIIpjKtkXiUC3FCKFj0C8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29baaf2910.mp4?token=IUkOMNvcKncurPlC9AU-QtQSdvG-DLONl_fNiaNwc98UfA-JoC28Y8eF5KstrYGzBzci95Koz_DZHs58azmiNyal8Ze2a2GH93PnpiE7SxEH-hk_6-op0f0SaT5ED3M1O7VjGL1OP7jX8p9xE4VNI5YaI-8jNTLQNwwm0w4j9WqTzeopPfMXMAaNPC7sCAujeqx4cnhrzOb-_xt1Z4rXY9JktErziljmONyITaJVK1iOHN-IYxovP94fMZHX1qv0BueYrJfHo_LYkmTSvqEoA4CyYnDXOXsn-dnWUg79ah7ODUyIi_uJ-aRkH7XgEbALOIIpjKtkXiUC3FCKFj0C8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویر ادعایی فدراسیون وشوو از آثار حمله خواهران منصوریان به دفتر رئیس فدراسیون  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/657291" target="_blank">📅 12:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657287">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KDogSNYUZIxrSXzCdd8lPFDwMGmtp4SsgryIXncAODzrwPARHtdXg2mjwT8zLvzA2UrpOI4VGES83JnfdTZR6wxxEQHY2PuDW2AVLh2ZzgNEwsAZgbWQ1nF5-PWancZmDdKZvQFC9x_1QVMoP5Vnx9D9Yh-YnLk722PmceF4Q9NstDdJwhPanrSe7QtGf5LdsjQmEPiSf1rqO3zXBfCsA-FaitIpaMErL9GQldCRaIiKj79gIWpnpdef329GCQGiQVQLsZgICtNj8_kJdV1FjRjM-ISwxspO0KNJRHmOvWpR8hcB3woCgDG1tO53mhPXjQzhFI3EwkkRjGAyix3-Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BjXGmhDCK6jWwejOfpuZ4fHXTn4CdisK8by7CdYvoX3lCZcNcxejVIGtEFSNQs7BhHBkSDHi5bmtkoD7f18x7PnmDCyx7ZH_9AyRxnUbUGUmDg4INjj7jbzCcCKnlR8H-NbcurCcsDE0jTr_uMu868Zih-b1PVj0p2Vob43MNPueM6V0pZVyBFkO4aOMvwerKCWey5QJEpUbUsWiHZyT8mnpH_kwAO256d3GY2u8nYuK--1dh9SHagQo4qmZ27UjBLCIRkGeDYqBmqD6PhKBCDkGdH5MFEJIhAY2STAMPa8jIzwNCXOdA7XuPFLRw7SNj8FQ8EKyodUYZLPdP--j_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVOtzF91e22bv_PHzngwruARBZVNGVIIxy4IbPqPTMgfF1hpT74DhM1aa1wthiEOqvCU1RmcOhNtG4-g35Gngpc_P683P6q1rBUTSXaTNh7Gp8fUScdnDSX4XfLyqQBr5cP8e0KAHSHzDp_sb9dEuHf38rqcPbMrwNAXu-l63fpHgSfq_gkjiezFEBvSfMOkm7e0PSAfUz38_jcGrraifVIH-LZXxmoFtTN8kGmKwhqrey_SbiaJWWH5DmAYH4yhlT0FgpIjrDi-WY0btEtAfwCXD20A2TeO2T0670oPsjbjAInJbe88O7zO3Lel5UIHHjKxh4S2YztgpvXffb0hiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ld3CTuWJCoWTJHzFftLdO-TPho4b7Oz9bikIzIFmjGOexWQfT3BWpqer5uEv00Ow1YvuoOKg75ls2TTrwSJokCwOQ7xQFua-1s_QDSIBI0Ge73hso9g1r7mYNT3txfPZQhRyeJ3DsWOqwRJM8urQ0KZvnptK6A7KZ_yKugcID-TWh8W6x81p10Dnj9IJsy2VyI292MNg3qgi7x0iSPugPVJAFNUxR6HdQBlJAH0gUoAlyvCuIhP5_VY2PdqjzbKD3xy6Fc7mUY246_OUNhkJOTSGaNWqFuGrrlQSVCTAyN4P4ZtVctcOQIri56_MDB8rQoQ9QDAzj2K_hJ0zzziTiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر ادعایی فدراسیون وشوو از آثار حمله خواهران منصوریان به دفتر رئیس فدراسیون
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/657287" target="_blank">📅 12:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657286">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
رکورد ارزش معاملات خرد بازار سرمایه شکسته شد
🔹
در حال حاضر ارزش معاملات خرد به بیش از 35 همت رسید که بالاترین رکورد ریالی ارزش معاملات خرد در تاریخ بورس است. /خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/657286" target="_blank">📅 12:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657285">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3e68add6f.mov?token=XLQ6UiRlVATXUcTtwYl9VAZgjCJVQJGZZDet9wcAs5oibMGCsTvmaTAhy-BV1J38QatfOMeY_HGmMPfnXOr_A1UiK749LbwZvUPgcnfcjfPnvWbAUiI76ie53J66VIlAPhvj-TFkTo4bnD7kZEJsTUodsKdZ7CgTXHx_SAgf1UT25ouIwRPFq4jorYNKPD6MzXfe-EewRoq3D1DVQPNBwyxYru4mlB8uE8nn5U3LOPyg21vjW9itR391IILT5X1XKmLkovPLkpPFXE1_gG011czRWU3WQqcD0w_1prY9yq2mcyao46f9rzIWTlf2Uls-Sy-h22YsiR-oKxNFoUsFZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3e68add6f.mov?token=XLQ6UiRlVATXUcTtwYl9VAZgjCJVQJGZZDet9wcAs5oibMGCsTvmaTAhy-BV1J38QatfOMeY_HGmMPfnXOr_A1UiK749LbwZvUPgcnfcjfPnvWbAUiI76ie53J66VIlAPhvj-TFkTo4bnD7kZEJsTUodsKdZ7CgTXHx_SAgf1UT25ouIwRPFq4jorYNKPD6MzXfe-EewRoq3D1DVQPNBwyxYru4mlB8uE8nn5U3LOPyg21vjW9itR391IILT5X1XKmLkovPLkpPFXE1_gG011czRWU3WQqcD0w_1prY9yq2mcyao46f9rzIWTlf2Uls-Sy-h22YsiR-oKxNFoUsFZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استفاده از پارکینگ‌های زیرسطحی برای پناهگاه
سخنگوی شهرداری تهران:
🔹
پارکینگ‌های زیرسطحی برای استفاده به عنوان پناهگاه آماده می‌شوند.
🔹
مجموعه اقداماتی برای ایجاد استانداردهای لازم در این زمینه در حال انجام است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/657285" target="_blank">📅 12:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657284">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
فعالیت عادی شعب بانکی ادامه دارد
🔹
در صورت تغییر در ساعت کار بانک‌ها در روزهای آینده، شورای هماهنگی بانک‌ها اطلاع‌رسانی لازم را انجام خواهد داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/657284" target="_blank">📅 12:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657283">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28106fa10c.mp4?token=hyG096VU_t3bt2wmXcXot7GvD-wCukz3HuMDjH9sTO_xYowlbiY79aXTMA45tkkfdPuyQbSuKt5gRCmiB0Mp8m4_ylAm1kAn8g2j2V7G-u4ALrMCpHoOOrNsZuBHUla0CM4GNyi56SpOa-hMLBYm2G--nDjWwsHls9Q9G5rXUMc1XFPS6183meCPqlM_7kw9GDs4TvOk07qZOF_jxAFjf7IW1hDwqNnLRaQZO7lnbHEEFoGkHgqOd2c8Z0FMaSjgx_hXQVcjMPuVkyipNv8KsTuIe9fMptFipjNXXIYeT8GzkRmuXOMh96eVhS-lHDwLsl7ewQAG1ihLiozTDXBgGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28106fa10c.mp4?token=hyG096VU_t3bt2wmXcXot7GvD-wCukz3HuMDjH9sTO_xYowlbiY79aXTMA45tkkfdPuyQbSuKt5gRCmiB0Mp8m4_ylAm1kAn8g2j2V7G-u4ALrMCpHoOOrNsZuBHUla0CM4GNyi56SpOa-hMLBYm2G--nDjWwsHls9Q9G5rXUMc1XFPS6183meCPqlM_7kw9GDs4TvOk07qZOF_jxAFjf7IW1hDwqNnLRaQZO7lnbHEEFoGkHgqOd2c8Z0FMaSjgx_hXQVcjMPuVkyipNv8KsTuIe9fMptFipjNXXIYeT8GzkRmuXOMh96eVhS-lHDwLsl7ewQAG1ihLiozTDXBgGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۶ زخمی براثر حمله مسلحانه در ایستگاه پن در نیویورک
🔹
براثر حمله مسلحانه یک فرد در ایستگاه راه آهن پن در نیویورک، ۶ نفر زخمی شدند.
🔹
فرد مسلح، دستگیر شده اما انگیزه او از این اقدام هنوز نامشخص است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/657283" target="_blank">📅 12:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657282">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
تهدید گروه مقاومت عراق به بازگشت به جنگ با اشغالگران
🔹
گردانهای سیدالشهداء عراق به رژیم صهیونیستی در خصوص عواقب حمله به جمهوری اسلامی ایران هشدار داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/657282" target="_blank">📅 12:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657281">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
حمله جدید یمن به سرزمین‌های اشغالی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/657281" target="_blank">📅 12:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657280">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpaTOqu8driS5N1JFKB1W_5bxDeCjU2rOzyGQ7d9DtOPZ3cREqeSqnRX3SFPF7DdCA2qPWxJAylcjmLLlIYfftJ1q5cFIsxeHYjtEOBOSUknoqGbRAr-_rOE9OLXF09C0zeXPnMEqn_LZrdykGB3u0PCZlXHY-Y2xcUyThyYm-2tQkyGg_SHjPX84peBkZJQYkvlJtoh9UyY4eYA8AKENH0NWDPi7rYNMJJVP-5hU1rDTW5YcS7jfNF-EYdUV2gWS3SqWdGOVVf8AIDKimhzqGF1NWCPZ7H8UR6p3BoIxlcDl4mPW_JWMB_w_-SEeJmFPP4uDxLFftrql9Q9vMw0MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اطلاعات سپاه: اطلاعات میدانی از ضربات دیشب به سرزمین‌های اشغالی نشان دهنده موفقیت ۱۰۰ از ۱۰۰ است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/657280" target="_blank">📅 12:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657279">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
عکس‌گرفتن از محل‌های بمباران و انتشار آن، بی‌احتیاطی ساده نیست؛ کمک مستقیم به دشمن است
🔹
در چهارمین جنگ هم هنوز این رفتار خطرناک را ترک نکرده‌ایم: خودمان با دست خودمان کشورمان را بی‌دفاع، بی‌نظم و بی‌حفاظ نشان می‌دهیم.
🔹
هیچ کشور عاقلی در میانه جنگ، اطلاعات میدانی، حجم خسارت، موقعیت اصابت و نقاط ضعف خود را برای دشمن منتشر نمی‌کند.
🔹
دشمن فقط با موشک و پهپاد نمی‌جنگد؛ با عکس‌ها، ویدئوها و اطلاعاتی هم که ما بی‌محابا پخش می‌کنیم، هدف بعدی را دقیق‌تر می‌سازد.
🔹
لطفاً عکس نگیرید. منتشر نکنید. بازنشر نکنید.
🔹
در جنگ، سکوت میدانی بخشی از دفاع ملی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/657279" target="_blank">📅 12:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657278">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
کوثری: به احتمال زیاد تنگه باب المندب در مرحله بعد بسته می‌شود
اسماعیل کوثری، عضو کمیسیون امنیت مجلس در
#گفتگو
با خبرفوری:
🔹
دریای سرخ را فعلا انصار یمن اعلام رسمی کردد که به کنترل رسمی در آورده که اگر شناورهای رژیم اشغالگر بخواهد تردد داشته باشد، برخورد و کنترل می‌کند. در مرحله بعدی به احتمال زیاد بحث (بستن) باب المندب هم پیش می‌آید.
🔹
ما باید جواب باصلابتی را به رژیم اشغالگر قدس بدهیم تا بدانند که آتش بس را نمی‌توانند نقض کنند و یا خودشان تعریف  کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/657278" target="_blank">📅 12:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657277">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrEhuHDvDWMBY395x9z4-wpysy8zeTJLrPwhwJAnxUqeEpZfLgAK9XTR1Z2XFh6ywpmYWgFsItU1QZbZQ9-0Tv40fiF8MKYXUycwmYENa9pPAKjSfwxF0bovc5CmCJgrkdmNXo1D1l7C64TzsVaPuT0c3Xk2K59ONxN3JpMhxFa9K9IAdFYek7wEpkqKFxd9qN00JsVWUVn-YDa1eLeGKIVqHx70ymrogyZCMYpBBBK9d6e3jNjl7lI_8ybMlvmx0eVByuRgzSC_0bQhebydNUY22vxbTLxWoPcBkTambJ8GrD5Zr2bJ4UkH9bMD4qng1Ko644rSqMRVKWIqS21crQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاوره و تسهیل گری در فرایند اخذ وام های بانکی
نیاز به وام دارید اما در میان انبوه بخشنامه‌ها و فرآیندهای اداری سردرگم شده‌اید؟
کافی‌نت آراد با جواز کسب رسمی، اینجاست تا مسیر دریافت وام‌های معتبر بانکی را برایتان هموار کند.
✅
خدمات ما:
• انجام مراحل اداری و پرداخت وام در کمتر از ۷۲ ساعت
• مشاوره و بررسی شرایط شما برای انتخاب بهترین وام بانکی
• ثبت‌نام آنلاین دقیق و بدون نقص در طرح‌های تسهیلاتی
• آماده‌سازی و تنظیم مدارک مورد نیاز
• پیگیری روند درخواست تا دریافت پاسخ نهایی بانک
📎
برای شروع، پرسشنامه اولیه ما را از طریق لینک زیر تکمیل کنید تا کارشناسان در اسرع وقت با شما تماس بگیرند:
https://survey.porsline.ir/s/CwzLVsEN
https://survey.porsline.ir/s/CwzLVsEN
https://survey.porsline.ir/s/CwzLVsEN
کافی‌نت آراد؛ پیشگام در تسهیل امور بانکی شما
🏦</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/657277" target="_blank">📅 11:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657276">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
شهرداری تهران: با توجه به شرایط موجود در کشور، استفاده از مترو و اتوبوس در هماهنگی با شورای شهر تهران همچنان رایگان خواهد بود.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/657276" target="_blank">📅 11:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657275">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس اورژانس تهران: هیچ مصدومی تا به الان نداشتیم
محمد اسماعیل توکلی، رییس اورژانس استان تهران در
#گفتگو
با خبرفوری:
🔹
در پی حملات اخیر، الحمدلله تا به الان هیچ مصدومی در استان تهران نداشتیم.
🔹
همین الان دو حادثه انفجار داریم که درحال بررسی هستیم که اگر موردی باشد به رسانه‌ها اعلام می‌کنیم.
🔹
حجم تماس‌ها با اورژانس به نسبت روزهای عادی افزایشی نداشته و کل ظرفیت ناوگان به همراه بخش خصوصی در کنار مردم برای خدمت هستند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/657275" target="_blank">📅 11:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657274">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
لغو تمامی پروازهای فرودگاه شیراز تا ساعت ۲۰ امشب
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/657274" target="_blank">📅 11:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657273">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در غرب تهران
🔹
هنوز محل دقیق و منشا این انفجار مشخص نیست.
🔹
همزمان پدافند هوایی در برخی نقاط تهران نیز فعال شد.
🔹
اخبار تکمیلی متعاقبا اعلام می‌شود.  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/657273" target="_blank">📅 11:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657272">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">📷
تصاویری عجیب از کاخ سفید؛ آماده سازی کاخ سفید برای برگزاری مسابقات UFC
🔹
قرار است کاخ سفید روز ۲۴ خرداد میزبان شش مسابقه UFC در قالب برنامه «آزادی ۲۵٠» باشد؛ رویدادی که همزمان با تولد ۸۰ سالگی ترامپ برگزار می‌شود و برای آن سکویی بزرگ در محوطه کاخ سفید ساخته…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/657272" target="_blank">📅 11:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657271">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
دولت عراق اعلام کرد؛ حریم هوایی این کشور به مدت ۷۲ ساعت به روی تمامی پروازها بسته خواهد شد| ایلنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/657271" target="_blank">📅 11:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657270">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در غرب تهران
🔹
هنوز محل دقیق و منشا این انفجار مشخص نیست.
🔹
همزمان پدافند هوایی در برخی نقاط تهران نیز فعال شد.
🔹
اخبار تکمیلی متعاقبا اعلام می‌شود.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/657270" target="_blank">📅 11:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657269">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
یک پیام برای سید مجید موسوی و اپراتورهایی که امشب پشت لانچر نشستند و قلب تل‌آویو را هدف قرار دادند بنویسید
👇🏻
🔹
پاسخ‌های شما در خبرفوری منتشر می‌شود و به دست سربازان گمنام امام زمان خواهد رسید  ویراستی خبرفوری را دنبال کنید https://virasty.com/r/BWcv</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/657269" target="_blank">📅 11:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657268">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آمادگی ۵ هزار آتش‌نشان برای حملات احتمالی به تهران
قدرت‌الله محمدی، مدیرعامل سازمان آتش نشانی و خدمات ایمنی شهر تهران در
#گفتگو
با خبرفوری:
🔹
در پی حمله‌ای که بامداد امروز به کشور انجام شد هیچ اصابتی در شهر تهران تا این لحظه نداشتیم.
🔹
آمادگی ۵ هزار آتش‌نشان برای حملات احتمالی به تهران
🔹
شهروندان در صورت وقوع حادثه، از تجمع در محل خودداری کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/657268" target="_blank">📅 11:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657267">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
یک منبع آگاه: در صورت خطای مجدد، زیرساخت نفت و گاز منطقه هدف قرار می‌گیرد
یک منبع آگاه نظامی:
🔹
در صورت ادامهٔ حملات به زیرساخت‌های انرژی، کلیه تاسیسات نفت و گاز مرتبط اسرائیل، آمریکا و هم‌پیمانانشان از جمله تاسیسات انرژی منطقه‌ای هدف نیروهای مسلح ایران است./فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/657267" target="_blank">📅 11:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657266">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: هیچ مذاکره‌ای دربارهٔ ذخیرهٔ اورانیوم ایران انجام نشده و اخباری که دربارهٔ آن منتشر می‌شود صرفاً گمانه‌زنی رسانه‌هاست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/657266" target="_blank">📅 11:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657265">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73b0f77de3.mp4?token=minj3jB55Yr9e1Ctv3rH296QQden-lXbS1r53lFaLMvv_Ezeq05kQ29cc0lcFo_aib7u67UE2NarcjY1b2XTqeXCfXN7EBZEg4ZEOpba5S_U4F5dJzG0hphlZoKDRgoJTQeOcKqETYcQI_YIDdEf7lFn73WNHIWkbfSRWMCqRQQacpiC8n37VPbyTWYcUa7zUkD6MRWDUuTymr6Ur4ZBTe4UF2ot8MNxjTUFrpcEzwzfyeKI9vsmYFMXkhN8_2nB77rWQohixR9DMJ50VA0WwDOkABLg9pvBpyld-y0WQ_BYJ667l81gqc3wGi6u3hZ3WAyss2IfA1iBAbg5wPbOBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73b0f77de3.mp4?token=minj3jB55Yr9e1Ctv3rH296QQden-lXbS1r53lFaLMvv_Ezeq05kQ29cc0lcFo_aib7u67UE2NarcjY1b2XTqeXCfXN7EBZEg4ZEOpba5S_U4F5dJzG0hphlZoKDRgoJTQeOcKqETYcQI_YIDdEf7lFn73WNHIWkbfSRWMCqRQQacpiC8n37VPbyTWYcUa7zUkD6MRWDUuTymr6Ur4ZBTe4UF2ot8MNxjTUFrpcEzwzfyeKI9vsmYFMXkhN8_2nB77rWQohixR9DMJ50VA0WwDOkABLg9pvBpyld-y0WQ_BYJ667l81gqc3wGi6u3hZ3WAyss2IfA1iBAbg5wPbOBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ادعای مصادره اموال ایران جنگ رسانه‌ای است
🔹
بقایی ادعای واگذاری اموال بلوکه‌شده ایران به کشورهای منطقه را بخشی از جنگ رسانه‌ای و تبلیغاتی طرف‌های مقابل دانست و تأکید کرد که این دارایی‌ها از محورهای اصلی مذاکرات جاری است و ایران در این…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/657265" target="_blank">📅 11:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657264">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfaAxm6QCzEpzqpYb-VGuXTXfUaxuEoLdFXZducr0RITWEok07iVIrVZ8C-XvOvhT-xtDseFyWb4R6T4GnXeaeuH2kZuK5bPltL9KnD2_Knv3cVjK0zVnzER8cQA6c_aFz1KOwkUeAE_3FNb80lLO4j4L9ZdNcbLfY1370-ZmUyP1iriS34XvRPaEk9-SUeS57x3N-RxuDo-uN1h387t5C1pXR1Zd5CEJKmK4PcUMfxyGCtugneecZEMXGvIJmtGQ4Adrkrv1L4nrkVjWP7m753vi7eGMiv2-UTISvgkqUgj1PzD-x2sQqFSQibpIB_txs7q6Tj3SXJrNIyFHGdiPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفیر آمریکا در تل‌آویو قایم شد!
🔹
سفیر آمریکا در اسرائیل با تشدید جنگ ایران در پناهگاهی در اسرائیل پنهان شد.
🔹
مایک هاکبی، با به صدا درآمدن هشدارهای موشکی در بخش‌هایی از اسرائیل، به‌روزرسانی‌هایی را از یک پناهگاه به اشتراک گذاشت و وضعیت پرتنش را توصیف کرد.
🔹
هاکبی در ایکس نوشت: با شنیدن صدای غرش‌های بلند در بالای سر، امیدوارم رهگیری باشد.
🔹
او در ادامه لفاظی‌های خود نوشت که  روز دیگری که ما تحت تهدید یک رژیم دیوانه ایران زندگی می‌کنیم. /خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/657264" target="_blank">📅 11:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657263">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8df649b271.mp4?token=NWLUZH7cUw2D7THbx8Zu3nXzjYxDOMkJ1AosiEHIx-u9zlgjFU6C0ucOqNmbDKkiCt8HRnr7x7G7HI3UwnEB4lkKhSvqdnyOtuemp2YytFrYnH6LH0aiM9ziUXSTnvgRnDzZ4lx4vSQXun7ogqotF5ln6uCJlLhVxYB-6RNnrBBoxEI9zw28TRXDYoBRlaWmHPYIzM2EFVRDK49jRaid95syhDAHvnpKzUPSSAgeEjNO_Fd6WHNRbzGLZE5At7bQJFCHyNS3I54EXQ_HHirVbLjcVK58U97yyY5ab17opp_2aS9cJ_5HZzIMvmSuDzbzgZulTJ6xhmiB6rDnGb2tNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8df649b271.mp4?token=NWLUZH7cUw2D7THbx8Zu3nXzjYxDOMkJ1AosiEHIx-u9zlgjFU6C0ucOqNmbDKkiCt8HRnr7x7G7HI3UwnEB4lkKhSvqdnyOtuemp2YytFrYnH6LH0aiM9ziUXSTnvgRnDzZ4lx4vSQXun7ogqotF5ln6uCJlLhVxYB-6RNnrBBoxEI9zw28TRXDYoBRlaWmHPYIzM2EFVRDK49jRaid95syhDAHvnpKzUPSSAgeEjNO_Fd6WHNRbzGLZE5At7bQJFCHyNS3I54EXQ_HHirVbLjcVK58U97yyY5ab17opp_2aS9cJ_5HZzIMvmSuDzbzgZulTJ6xhmiB6rDnGb2tNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر پاسخ به تجاوز دشمن آمریکایی‌صهیونی به یکی از صنایع پتروشیمی علیه صنایع مشابه در حیفا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/657263" target="_blank">📅 11:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657262">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
فرودگاه‌های شرق کشور فعال است
مجید اخوان سخنگوی سازمان هواپیمایی کشوری در
#گفتگو
با خبرفوری:
🔹
فرودگاه‌های فضای غرب کشور، فرودگاه مهرآباد و فرودگاه امام خمینی طبق آنچه که در شب گذشته صادر کردیم، بسته شده است.
🔹
تا زمانی که ایمنی و امنیت پروازها به خطر نیفتد، این وضعیت حکمفرما است و از آنجا به بعد باز خواهد شد.
🔹
فرودگاه شرق کشور مانند مشهد فعال است و می‌توانند پروازهای مناطق شرقی کشور را انجام بدهند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/657262" target="_blank">📅 11:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657261">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: گروسی همچنان رویکرد نامناسبش اصرار دارد
🔹
در صورت صدور قطعنامه در شورای حکام آژانس انرژی اتمی، به آن پاسخ مناسب خواهیم داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/657261" target="_blank">📅 11:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657260">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1s5glk0LTNA5rX_e-W9xc_7B3tSHL13JDy2FbQwYCfvLeJIeVMjqgJ7YaqIH02ceHD7jRXM7yqKlddqIbT0ue2iy6Q8BIp317Fwcfyf-SZVn9HsfczW0SGev7dsJECK6DSOYWchXLXASersv3S46HC-lHItrECTpxeWPrx0f4bdZi1erLJw55NKv55lwxMS53ewi7BYUwpsG3KNurvfVAZuh-LiOkFEjScsSZlPamjblCIB48qS7lgYuuRBnsXECLeCQ-TnhM2xINGOTcKGcmnOHbCD0r6yJqzdcP9tThMsv5knhvHRVff2kIFahECIVJQyyfwWXzhBsAJ3PL8xWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبی که ماه کامل شد
🔹
پس از نقض آتش‌بس از سوی رژیم صهیونی در لبنان و حملات این رژیم به جنوب بیروت، جمهوری اسلامی ایران با حملات موشکی به سرزمین‌های اشغالی پاسخ این حملات را داد.
پیام روشن این اقدام، نمایش اقتدار و یکپارچگی محور مقاومت و تأکید بر پیوند و اتحاد استوار میان ایران و لبنان است؛ از شب گذشته نیز گروه‌های مقاومت در لبنان و یمن هم سرزمین‌های اشغالی را هدف قرار دادند.
🔹
ویژه‌نامه جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/657260" target="_blank">📅 11:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657259">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a208e31b9.mp4?token=BVtMP67Q-35QszbH8A4pkhY1VBZL2gT9Kg8OGq9roK_Mvm8RpB4gJgnzItj337Ukp6M9zmOtHTP8oJaJSlC67Lv45lYRzvX2LXgLb8-eSuDWHvboOW-CCvJuMkxuuHiG5brso3I_7o_FoYq1zFhBc3cZEvAKKkMYg_HikYIqLq6sGg7h7MxW0-fXGhFNVpjpfFvnuilZNTgzbYw97kTqDjRw0apF2Lj4BlqLQuKCKTLBtgKheLHZiJJbHRyceIbnG-E13oB-NSyRIsG1q8PI7ranvnz7ILCnKNcJhwe4znf-2DZQ2eMUP__y7SFWuFcFDHnkeHzmSEXtoZDb8fepAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a208e31b9.mp4?token=BVtMP67Q-35QszbH8A4pkhY1VBZL2gT9Kg8OGq9roK_Mvm8RpB4gJgnzItj337Ukp6M9zmOtHTP8oJaJSlC67Lv45lYRzvX2LXgLb8-eSuDWHvboOW-CCvJuMkxuuHiG5brso3I_7o_FoYq1zFhBc3cZEvAKKkMYg_HikYIqLq6sGg7h7MxW0-fXGhFNVpjpfFvnuilZNTgzbYw97kTqDjRw0apF2Lj4BlqLQuKCKTLBtgKheLHZiJJbHRyceIbnG-E13oB-NSyRIsG1q8PI7ranvnz7ILCnKNcJhwe4znf-2DZQ2eMUP__y7SFWuFcFDHnkeHzmSEXtoZDb8fepAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود شی جین‌پینگ به کره شمالی
🔹
«شی جین‌پینگ» رئیس جمهوری خلق چین با ورود به پیونگ یانگ، دیدار رسمی خود از کره شمالی را آغاز کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/657259" target="_blank">📅 11:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657258">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ae81cdbee.mp4?token=gYY1AQU-BS40Pl-A-dD--jj6HoPQVQqS56KB8SY3V1Kqr4XzSeZAjJmLTHRh0JnnGK7PKoLS6UK01-HVPcTSqh1fLlLadnT8jlobZnfS6FdxClCWORnB9Jq8got5TWyzSN3ZUGR0SB4hIS9x2HCx8fm-0ihgiuM2xHUqfE7EVzKUlXeJLFFksZjU0lpD_trY4k9sieY8Wivzn_oIYtVzMqRZBQjkkx0HGAB05z5sSGwEPhUkk_SgtA28eMOgiXRU_VdgpMC2NSBrjZegxF3JFFFYp2pMpY8ZUdJo39mLsLGSTXx5CdIP0kmrnP6PlgRjFF-1tx0VkbaYvVJTNFdfSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ae81cdbee.mp4?token=gYY1AQU-BS40Pl-A-dD--jj6HoPQVQqS56KB8SY3V1Kqr4XzSeZAjJmLTHRh0JnnGK7PKoLS6UK01-HVPcTSqh1fLlLadnT8jlobZnfS6FdxClCWORnB9Jq8got5TWyzSN3ZUGR0SB4hIS9x2HCx8fm-0ihgiuM2xHUqfE7EVzKUlXeJLFFksZjU0lpD_trY4k9sieY8Wivzn_oIYtVzMqRZBQjkkx0HGAB05z5sSGwEPhUkk_SgtA28eMOgiXRU_VdgpMC2NSBrjZegxF3JFFFYp2pMpY8ZUdJo39mLsLGSTXx5CdIP0kmrnP6PlgRjFF-1tx0VkbaYvVJTNFdfSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: آتش‌بس به‌طور مستمر و مکرر توسط طرف‌های مقابل نقض شده است
🔹
ما هر وقت لازم بدانیم برای دفاع از امنیت کشور اقدام خواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/657258" target="_blank">📅 10:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657257">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: تاکنون تبادل پیام ما با آمریکایی‌ها در فضای بی‌اعتمادی بوده و اتفاقات شبانه‌روز گذشته به این بی‌اعتمادی دامن خواهد زد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/657257" target="_blank">📅 10:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657256">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
هشدار کارشناسان: ChatGPT کاربران را به وب‌سایت‌های کلاهبرداری هدایت می‌کند
🔹
در گزارش امنیتی جدیدی گفته شده که کلاهبرداران با تزریق آدرس وب‌سایت‌های جعلی به منابع یادگیری هوش مصنوعی، نتایج جستجوی ChatGPT را دستکاری کرده‌اند. به گفته آنها، وقتی کاربران برای دریافت پیشنهاد خرید از این هوش مصنوعی سؤال می‌پرسند، لینک سایت‌های کلاهبرداری به آنها نمایش داده می‌شود که در نهایت منجر به سرقت پول و اطلاعات بانکی خریداران خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/657256" target="_blank">📅 10:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657255">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de88f8ba46.mp4?token=cSZ26FVNZ2tnfzaTpOBq1gGMd9D1HWTNeMKpB4wSHjIHAJf7ivxWF0Ftf3TiDtlx-n8_JV2kW0gc1KeoA1YN46Xrw2wj4DPSgvLA3ln5tU_02t-7ZmJJWlGGLNKy9AH8QnzbebzKqoLg5xWC54kjG1ujQoilQ_sgED6Ij5VsdjPBvbeDZuJ7ifw9gctLb5ntD1sqvjE1IcKqy8AYfrBhIfz5XXkBIAOiF39wzhtvIWuPbnFD0CCNwbLdi4aLMta0iDpVvN_8OY_LyxHRpst-tNmkKFqM4a8dTBKbEKiMvlg2UM1SNJfI0rC3Vj_6JY83MIsLpHxnd1sw4C9tO-yn6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de88f8ba46.mp4?token=cSZ26FVNZ2tnfzaTpOBq1gGMd9D1HWTNeMKpB4wSHjIHAJf7ivxWF0Ftf3TiDtlx-n8_JV2kW0gc1KeoA1YN46Xrw2wj4DPSgvLA3ln5tU_02t-7ZmJJWlGGLNKy9AH8QnzbebzKqoLg5xWC54kjG1ujQoilQ_sgED6Ij5VsdjPBvbeDZuJ7ifw9gctLb5ntD1sqvjE1IcKqy8AYfrBhIfz5XXkBIAOiF39wzhtvIWuPbnFD0CCNwbLdi4aLMta0iDpVvN_8OY_LyxHRpst-tNmkKFqM4a8dTBKbEKiMvlg2UM1SNJfI0rC3Vj_6JY83MIsLpHxnd1sw4C9tO-yn6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: تاکنون تبادل پیام ما با آمریکایی‌ها در فضای بی‌اعتمادی بوده و اتفاقات شبانه‌روز گذشته به این بی‌اعتمادی دامن خواهد زد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/657255" target="_blank">📅 10:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657254">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
شبکه ۸ اسرائیل: از دیشب تاکنون ۲۰ موشک به سمت اسرائیل شلیک شده است
🔹
در اثر اصابت موشک‌های ایرانی به تل آویو شماری زخمی شدند./ جماران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/657254" target="_blank">📅 10:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657253">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54da5e3d02.mp4?token=Xx1osZ8qvjBxnNsHf32IaFpxMw1RKxO_bIyx4xQuXaJjYip_hU5fak50eVbhKcDRyR8MLnDmb1d4Pk0WKHBjgl3vGdWQcDFjOmsneSprfJRW-m56ofTbSstgu0ceUGZJjhHebPnqBCWnzzL-fyCtoajHaSBwpEl1dEj0FVGf9-ZC95zbgUD3mOX1oVchVbBFokCGby9XQ576aNnCQm0Bs_nHF2HZGYhFCQdbUJI-CISyeMY9GN-I_igqUbeilc826f6CpPfNxyicYuDLaHfxZkU6ejNLTcyPn4w_qCgNX-UhWJKsbOVkcmn4h3DUBZus7rKOEn7z4SMfA26D-CSKFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54da5e3d02.mp4?token=Xx1osZ8qvjBxnNsHf32IaFpxMw1RKxO_bIyx4xQuXaJjYip_hU5fak50eVbhKcDRyR8MLnDmb1d4Pk0WKHBjgl3vGdWQcDFjOmsneSprfJRW-m56ofTbSstgu0ceUGZJjhHebPnqBCWnzzL-fyCtoajHaSBwpEl1dEj0FVGf9-ZC95zbgUD3mOX1oVchVbBFokCGby9XQ576aNnCQm0Bs_nHF2HZGYhFCQdbUJI-CISyeMY9GN-I_igqUbeilc826f6CpPfNxyicYuDLaHfxZkU6ejNLTcyPn4w_qCgNX-UhWJKsbOVkcmn4h3DUBZus7rKOEn7z4SMfA26D-CSKFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی دیده‌نشده از پدر موشکی ایران و سردار موسوی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/657253" target="_blank">📅 10:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657252">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhEEoMB0XcYgB83I52Mi6Sq3V8C3cDKi8yLH3hmmhrjZXcO0-qvDSOvxD3lcCqJ-VHCsLMEtI9MWDcBPKG7dQvsy-VsBare4aAEK93hkyuhFht_1rJSY25tIzxcYoznMcy4SURWQA8pdTeIolg2FSZGgmrfgJlQ_CQCrwki8JnE47tznPg9Rq8-Gol7zVHtHujtbJN3ew9R0-JmCFWJoTLjIEI5oWf1lhH-bOZWupMjCLKgTChLJT_sCTAu1nmu9AYHvXw4Hcj5gyhl6tjmeF1fwDAcu804HFLrmYUsWOU82Q5WGx1bhs6jXiz4Jwol_mYBlgvMfu9iLB9eqcDXOHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایلان ماسک: جالب است بدانید اسم تنگه هرمز از اهورامزدا، خدای آیین زرتشتی، گرفته شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/657252" target="_blank">📅 10:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657251">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/089e0036d0.mp4?token=bThzX-64eBcWb7SpnQewCB3MD8Dfv5O6-i34j3gwMkGHl3b5Nwf3NHu9x9WvdhbDRmxNOd8ccs-NaoUVZxYQTOq3lQKL1Ckrzmd2ps0fHExOakfrSNulPMbqlMGMpLgEtcpmkblhjuteV40HIxY-KM2Z79zbu7LzkV4MuYujM-wEljnGcq6jI81EkMXDVRV2B9DdiyZvjzCfUd05t9FykJCPtmIdUEQfqKSPTKgWn2D7k5IiCE1c2SoHCtWJ9LrFjh50idFN-HhcU7WATFRj2HcL0vTMDk4iFmoiMRedXrIFFt-GM_98o3tNwz6gW2Fl5ikgmYXw3dzzhkzogkZTPrSVHgI09sZG-ByHIPXxD4BGm6e0ZWwU_uEyFXjz8XBxco2rj3ACyhH1XXLVpBwaqQeUWJ9GckStyGLDkrPVVBvrT_XeAOltpcKTYpeMzuML5XDzkRbHPHSEzSkXvcyasRDEKRQoPhGCzuKoTPc6bPZRn77ajsO2NoMrSl3sKPDLJDgVBlWgOpVKTnmrz3ZNLxZZAK6Gf2vpsYpN55NRUMQ_Xzm4bIe4RLvpiyB7Iu40gQNwafGIoE8IBmhHB12RJlzBMwSid_84ouJyl5SJaEVuA56UTk9IcCsOma9f7HqVoXj3HiLg7Za24I3ihamUQ0WZidQ2PaxIPDN2v2HVTeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/089e0036d0.mp4?token=bThzX-64eBcWb7SpnQewCB3MD8Dfv5O6-i34j3gwMkGHl3b5Nwf3NHu9x9WvdhbDRmxNOd8ccs-NaoUVZxYQTOq3lQKL1Ckrzmd2ps0fHExOakfrSNulPMbqlMGMpLgEtcpmkblhjuteV40HIxY-KM2Z79zbu7LzkV4MuYujM-wEljnGcq6jI81EkMXDVRV2B9DdiyZvjzCfUd05t9FykJCPtmIdUEQfqKSPTKgWn2D7k5IiCE1c2SoHCtWJ9LrFjh50idFN-HhcU7WATFRj2HcL0vTMDk4iFmoiMRedXrIFFt-GM_98o3tNwz6gW2Fl5ikgmYXw3dzzhkzogkZTPrSVHgI09sZG-ByHIPXxD4BGm6e0ZWwU_uEyFXjz8XBxco2rj3ACyhH1XXLVpBwaqQeUWJ9GckStyGLDkrPVVBvrT_XeAOltpcKTYpeMzuML5XDzkRbHPHSEzSkXvcyasRDEKRQoPhGCzuKoTPc6bPZRn77ajsO2NoMrSl3sKPDLJDgVBlWgOpVKTnmrz3ZNLxZZAK6Gf2vpsYpN55NRUMQ_Xzm4bIe4RLvpiyB7Iu40gQNwafGIoE8IBmhHB12RJlzBMwSid_84ouJyl5SJaEVuA56UTk9IcCsOma9f7HqVoXj3HiLg7Za24I3ihamUQ0WZidQ2PaxIPDN2v2HVTeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir
رویان
📍
۳۰۰ متر زمین
۳۰۰ متر بنا
تعداد خواب ۴
مجتمع خصوصی
سند تکبرگ و مجوز ساخت
نوساز و کلید نخورده
🔻
برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/657251" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657250">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtK3ZIJ3eLMAvYZr8kqM36mTB-uaGEzOJbaB7rvSBsI3WVvQ9TedbrwMwGxhQx2JIg7Hu9jsxM8RyGXzt7U1Jss71HHSTPIPq35Prh2WvswMIghntGwBVGxmi2jfxfIYyqbBAxAhaSx8jw82_QpIdnyinDPqSnG58h8PndVhwiuCzqtxsFTa2ntBD_LZYEKPamqeKcJg3Vd94-ta7UOoU3Mh7Ewxh6zd6ipnp3zc-xpAk2uX3nyNy_p-Q8jVBYo55FvBZthja-yF7MlTbdf-zCpWUF3NHDHoDoTTljppMlSxFv10adwJwDVANAxdNm8h6Mgs74yttkZ4KhXKssM5TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دست‌نوشته شهید موسوی در خصوص عاقبت رژیم صهیونیستی
شهید سپهبد عبدالرحیم موسوی:
🔹
رژیم صهیونیستی در باتلاق زوال دست و پا می‌زند امنیت خود را در ناامنی دیگران تعریف کرده است.
🔹
به اینجا آمده تا با انتقال ناامنی، امنیت خود را بالا ببرد. دود این اقدام به چشم آنهایی می‌رود که مجبور به پذیرش او شده‌اند.
🔹
روزی پشیمان می‌شوند که امیدواریم دیر نشده باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/657250" target="_blank">📅 10:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657249">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
روابط‌عمومی سازمان هواپیمایی ایران: تمام فرودگاه‌های غرب کشور تا اطلاع ثانوی بسته شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/657249" target="_blank">📅 10:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657248">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
رژیم صهیونیستی مدعی شناسایی یک شبکه جاسوسی در قلب سرزمین‌های اشغالی شد  سایت عربی وای نت:
🔹
اسرائیل یک شبکه جاسوسی مرتبط با ایران را در «بیت یام»، در مرکز سرزمین‌های اشغالی را شناسایی کرده است.
🔹
در این گزارش آمده است که این شبکه جاسوسی اطلاعات حساس  را در…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/657248" target="_blank">📅 10:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657247">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
فرماندار قروه کردستان: صداهای بامدادی ناشی از فعالیت سامانه‌های پدافندی بود
🔹
صداهای شنیده شده ناشی از فعالیت سامانه‌های پدافندی بوده است و شرایط در شهرستان کاملاً عادی است و هیچ‌گونه تهدید یا خطری متوجه شهروندان نیست.
🔹
مردم به شایعات و اخبار غیررسمی توجه نکنند و اخبار و اطلاعات را تنها از منابع رسمی و معتبر پیگیری کنند./مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/657247" target="_blank">📅 10:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657246">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38b6bd8447.mp4?token=GZ4SbBWpYQ8jmbOqpuMD9uUUkpNyuDMUfQyFqK7pQ9yPgneQ6YmDLLYIqUaGFtM7z_6dycuyurY2i0Uq9mhrZiFYIGGrOZ-6Nt28fQzG6cEeby8UXD7j0Gt0pUhpOq77XaJIeXEy5dOIX0Hn5SFr5K3EA__JO2ItfuqwuWqb01WYw8sLwHrUzrWAXucjIvAOPKaAcddCqdL8sodwxkn9-SbuQTR36DgQ06mj_KyQV6jG0ceKduT6_0dqdsQr6r9E973MrQPBW7GW5-GPAemiN4fvurMGaSUStLUeVqJ7XG_Z3X513iraG_veHaIY2_I2xL14jDRy_oGvJWiRM2P5LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38b6bd8447.mp4?token=GZ4SbBWpYQ8jmbOqpuMD9uUUkpNyuDMUfQyFqK7pQ9yPgneQ6YmDLLYIqUaGFtM7z_6dycuyurY2i0Uq9mhrZiFYIGGrOZ-6Nt28fQzG6cEeby8UXD7j0Gt0pUhpOq77XaJIeXEy5dOIX0Hn5SFr5K3EA__JO2ItfuqwuWqb01WYw8sLwHrUzrWAXucjIvAOPKaAcddCqdL8sodwxkn9-SbuQTR36DgQ06mj_KyQV6jG0ceKduT6_0dqdsQr6r9E973MrQPBW7GW5-GPAemiN4fvurMGaSUStLUeVqJ7XG_Z3X513iraG_veHaIY2_I2xL14jDRy_oGvJWiRM2P5LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرگردانی مسافران در فرودگاه بن گوریون
🔹
هواپیماها در حال تخلیه مسافران در فرودگاه به دلیل ترس از موشک‌های ایرانی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/657246" target="_blank">📅 10:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657244">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb76c2010f.mp4?token=tDHAtnKM2V6uLFg8fsoWmACdsRkbXwoPJJP4eSp7UU5GGcnTPTuNoRh2MW-MzcTt-ZoVCMCgB8fLEj-C3DLab2VS6EsXjJAgb7RVWRs9BhupHDrcqoC3Vrj_pF6MJFRqI7HtS_6tJIzJiIHeGtsrQAWeISUHilk77yRnsk6kapyaJPBPEr-6mg1HxXL0g5jfYqb1TZSKI9GCd5iJVO2nuM-nwSlECxziUwNo0ePQMkQEOFzIYN_9mcou7uFHAsL4KazRfhvrXAhlPF0XcvP6aUuMfVHabLyMHiB73lo214iHubbej8CBLjP1aHD4-SbuWpAF5Rqk3E6tKvK0orQ-lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb76c2010f.mp4?token=tDHAtnKM2V6uLFg8fsoWmACdsRkbXwoPJJP4eSp7UU5GGcnTPTuNoRh2MW-MzcTt-ZoVCMCgB8fLEj-C3DLab2VS6EsXjJAgb7RVWRs9BhupHDrcqoC3Vrj_pF6MJFRqI7HtS_6tJIzJiIHeGtsrQAWeISUHilk77yRnsk6kapyaJPBPEr-6mg1HxXL0g5jfYqb1TZSKI9GCd5iJVO2nuM-nwSlECxziUwNo0ePQMkQEOFzIYN_9mcou7uFHAsL4KazRfhvrXAhlPF0XcvP6aUuMfVHabLyMHiB73lo214iHubbej8CBLjP1aHD4-SbuWpAF5Rqk3E6tKvK0orQ-lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار فاکس‌نیوز: صدای انفجار در تل‌آویو شنیده شد
تری یینگست:
🔹
”همین الان صدای انفجارهای دور از تل آویو شنیده شد... احتمالاً از رهگیری‌هایی می‌آید که در حال انجام است یا با رهگیری دیگری که همین الان در همانجا در حال انجام است، برخورد می‌کند، زیرا ایرانی‌ها به حملات خود علیه اسرائیل ادامه می‌دهند."
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/657244" target="_blank">📅 10:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657243">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
اصابت موشک ایرانی در کریات در شمال سرزمین‌های اشغالی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/657243" target="_blank">📅 10:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657242">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3BOISlSxdXYitnfhCPapg_eXBI9BOxTg0W8iksi2yS3IOVtlFxKxkDSIR66F8lZ5HsciYvWWIjndCof_EY8iWtaJPAf-6fUscmz6eezSoijcu3WOkHSxqBcNyIkuTLPVxNDLLdKYQsUf_GyieygJQLxpk5ldEMVy_7--m-XzbGlfb2pdELc6HnJ6NncT4kxNlsw7rclUYzidnfwSoPmbigq_pKyILbluUJ3oKK_Jh5ZyWneMv_ppCwJPVMgNgLBEqZDkJAnIuqErUGV32yzuOJc1O-1r0OinqQoKaz9W7T6XJfECdDv68q8n8GEHqIdETIDKonC2ezeUCjwfeib4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصويرى از موشك هاى ايرانى به سمت اسرائيل
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/657242" target="_blank">📅 10:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657241">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
شلیک ۶ موشک از ایران به سرزمین‌های اشغالی
🔹
منابع خبری رژیم صهیونیستی از شلیک ۶ موشک از ایران به سرزمین‌های اشغالی خبر دادند.
🔹
منابع مذکور اعلام کردند ۲ موشک به شمال فلسطین اشغالی و ۴ موشک به تل‌آویو و مرکز فلسطین اشغالی شلیک شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/657241" target="_blank">📅 10:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657240">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
الجزیره: جبهه داخلی اسرائیل: همزمان با شلیک موج جدیدی از شلیک موشک‌های ایرانی، از شهرک‌نشینان خواسته شده است به پناهگاه‌ها بروند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/657240" target="_blank">📅 10:12 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
