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
<img src="https://cdn4.telesco.pe/file/ZzDp9W0ZDLtejLlQiyPBG8RhXlGzCcQ_fletEC4kPUO2-L9y4xL4bBFV22D2AO5OkVAlWfvdEFzCZI7Y3bHmtK3IvxEeM3Ox0rm_nobh7D9u9fVkjI3p81JqE9rH-UhZgNlL-S2VrrJkiVHRCwg9bVWvdyF9F6XawkjLT4F5eCacKOv-tEDRljrqwKiUZhpC4zZd4Zzd3eQ3ec3OU9jySMZ8p2o2Q8ZamazJ0fCiBzeUoVPmBT-XAUTXAPvhXJwxLhJ4piXOxaZdeSsgeGqFcqN4X65NsrFZzg5oS31Z1ImtiLTSNO-szc2MCFJsLSuBGGDEZSbKqVO-jKhZesQmCw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.52M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 22:33:11</div>
<hr>

<div class="tg-post" id="msg-659898">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
انفجارهای کنترل‌شده امشب در بندر جاسک؛ شهروندان نگران نباشند
‌
🔹
طبق کسب اطلاع خبرنگار مهر، امشب از ساعت ۲۱:۰۰ تا ۲۴:۰۰، عملیات کنترل‌شده و برنامه‌ریزی‌شده‌ای در محدوده شهر بندر جاسک انجام می‌شود که طی آن صدای انفجارهایی به گوش خواهد رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13 · <a href="https://t.me/akhbarefori/659898" target="_blank">📅 22:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659897">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFwtM-oQon6SA8w1qYRVEw9UlNGTEGLdI33AmkUjpEKAZoapRsOoxXwX8hDVEwbfHiql9KnJwLM8UPp4RKjRFFcV7TxeUUHjgBaaFo0k38t9qYPMQuCsiEz9KZNqM7FfssQxvIcUcNyLRb-rPn28Q9iuzzoPYePjZKZL_wqqEReqEFx-HqhgiAdFnenpyZDT_NTwDqBWFmwieK3uWYgRnDbFl4dNVk2W_yDnVHGd_ybwS936fRUPuzvASB7bml6kPuT4u-Ug8DeR1gxCP_oA2_OGt7Fmsi0k5a5yDHkVyElW2NmGKGJBBsqyWhQ31ML-eyadKYl4g-6a1psdOGC1Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرهیز از آرزوهای طولانی
🔹
امام می‌فرماید: آرزو اگر از حد بگذرد انسان را به بدعملی می‌کشاند. امیدِ معتدل محرک تلاش و پیشرفت است، اما آرزوهای طولانی انسان را از آخرت غافل می‌کند، او را به استفاده از هر وسیله حتی نادرست وادار می‌سازد. چنانچه در دعای کمیل نیز…</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/akhbarefori/659897" target="_blank">📅 22:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659896">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKGt67Azk76ooRzuOskuAkyJaCRJzcjXMQ3EzhWcyz6VT-k2TrmUyPvPg-enioqvqE0tbArPqVn-kPxGnsvLXkv-t2VT1Gn57P-Sa7g3uJEqqQqBkpOAPB-umOKJBO5hbwVMk_AUWE1r0P6Y2IP0nbCziREt4AIl2YJIj-cWtriyXoojMo3NBuDq6B6M_X5abUdPxqHpOnJopENaWMNSKkubPGyDJnYG_gPBclr2Oz9D4nxA5mxsDacV2AWk7N9Z0VWxSPO9i9a1KKeS3MkL96xWVnqWIhj1gzISd37DvZwO_oQB6Ra3tydgfpD1Z7z4-gKjS0pJQ6NL7EvaK_0StA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ناپدید شدن مرموز جاسوس اسرائیلی | گریز در سایه بمباران اسرائیل | خالد العیدی کیست و چگونه گُریخت؟
🔹
در حالی که جنگنده‌های اسرائیلی حومه جنوبی بیروت را زیر آتش گرفته بودند و ساکنان منطقه با وحشت در حال فرار بودند، مردی از دل این هرج‌ومرج فرصتی برای گریز پیدا کرد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3223272</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/akhbarefori/659896" target="_blank">📅 22:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659895">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e59a6bef4.mp4?token=IzCfeOPrDJCdRyL68IvPYbfEqNhz7K90DjS-h9zOFZ1tN9gA95z5ng58C_r35PjtdzjacAusKCMwi4GDR5ZOOrbl-Dkdwoh760fiYKI8bi35xXdzxIkLD1u-FFlfjiT-bfBQ4OutDPO_KHoJVHNRxKgM0r2oQNJ8wBXQS3DyrVpJqoC5tWApAiK5WSf5GVmOT_rxyBrX17nc4_iMD3ufmfNRCE1ZF0D9uO0K7Le_Xi1jMsrmWQlGVXq_SanfUgqdo9N5hDWtuKJuS8t7MX3iE5dDSAAYlUKRNgrHYkLBTGO4GOGAwQZBc5y8-iLn9yWqpAl6lYSgZrG8tDaQaluit4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e59a6bef4.mp4?token=IzCfeOPrDJCdRyL68IvPYbfEqNhz7K90DjS-h9zOFZ1tN9gA95z5ng58C_r35PjtdzjacAusKCMwi4GDR5ZOOrbl-Dkdwoh760fiYKI8bi35xXdzxIkLD1u-FFlfjiT-bfBQ4OutDPO_KHoJVHNRxKgM0r2oQNJ8wBXQS3DyrVpJqoC5tWApAiK5WSf5GVmOT_rxyBrX17nc4_iMD3ufmfNRCE1ZF0D9uO0K7Le_Xi1jMsrmWQlGVXq_SanfUgqdo9N5hDWtuKJuS8t7MX3iE5dDSAAYlUKRNgrHYkLBTGO4GOGAwQZBc5y8-iLn9yWqpAl6lYSgZrG8tDaQaluit4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازیکن دوازدهم
🔹
بعضی صندلی‌ها هیچوقت خالی نیستند؛به یاد ماکان نصیری شهید جاوید الاثر جنگ رمضان و تمام پسر بچه‌هایی که قرار بود جام جهانی را ببینند اما حالا از جایی دورتر،تماشاگر رویاهایشان هستند
#اخبارفوری_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/akhbarefori/659895" target="_blank">📅 22:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659894">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
بنیامین نتانیاهو: «مواردی پیش می‌آید که من و ترامپ دیدگاه‌های مشترکی نداریم. آدم باید با خرد و تدبیر از منافع امنیتی اسرائیل دفاع کند #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/659894" target="_blank">📅 22:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659893">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
تهدید تازه نتانیاهو؛ «هر زمان لازم باشد اقدام می‌کنیم
🔹
ما تا زمانی که لازم باشد در «مناطق امنیتی» مختلفی که تصرف کرده‌ایم باقی خواهیم ماند تا از کشور محافظت کنیم. #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/659893" target="_blank">📅 22:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659892">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8702b068a.mp4?token=IlUgN_7Zf4b7H1N6xV02p8ts118CNK1d1n2CSoLvJ4r2q_4iSH_d5_TqED2ZoE96res7AQ4iVeuClWLw_K0cXpKYQ2djoPM-d6PeiEupQLAhacA9XWAKbvc06sKKkdoqM_FD9RZwT3IHiVxRyHwV5oWEbwN4vr6W5HJwKWxRv5KWce1K74z0CpIYMZY-BRI3mDtl-nG9tZdwtkb3K1NS1zaN9Hwv1GgeIFud4Buy9xR8PFYKMX8YtR0dxd4gfKA6vzjhujQJGeIOc9Gl7mMAC_C1ltMVDqm5JBod49AFRLX7ZZClbTzSt5ms_ohyeKGdaYjNE8i52ZyxeT4VXhdVfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8702b068a.mp4?token=IlUgN_7Zf4b7H1N6xV02p8ts118CNK1d1n2CSoLvJ4r2q_4iSH_d5_TqED2ZoE96res7AQ4iVeuClWLw_K0cXpKYQ2djoPM-d6PeiEupQLAhacA9XWAKbvc06sKKkdoqM_FD9RZwT3IHiVxRyHwV5oWEbwN4vr6W5HJwKWxRv5KWce1K74z0CpIYMZY-BRI3mDtl-nG9tZdwtkb3K1NS1zaN9Hwv1GgeIFud4Buy9xR8PFYKMX8YtR0dxd4gfKA6vzjhujQJGeIOc9Gl7mMAC_C1ltMVDqm5JBod49AFRLX7ZZClbTzSt5ms_ohyeKGdaYjNE8i52ZyxeT4VXhdVfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مذاکرات بعدی ایران و آمریکا چه زمانی برگزار می‌شود؟
عراقچی:
🔹
قرار است روز جمعه در کشور سوئیس که محل دقیق آن مشخص خواهد شد، یک دیداری بین هیئت‌های دوطرف انجام شود، که در آن روسای هیئت‌های دو طرف ابتدا این یادداشت تفاهم را امضا کنند و پس از آن اولین دور مذاکرات بعدی را داشته باشیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/659892" target="_blank">📅 22:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659891">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5234ca4dd.mp4?token=BUHIRufP4i5g-V1hjB0cZDuwR7ToG2Rfs8wO6Fmj4e54bZRp7NFt3terBvld72y4sMMICYgvhtBQbWEpppIqTqQjITGjFUmAcya1hKcsfKAqeBYUFoKEtZkCfJllWpUUGopavaxV5WbijvwW0NtK8FjWF9KH00fWX-8ZdvKkwg8MXqMm1F7HP90HDjZFrrs6S8yiTqsdwEJeBKEHpOEc1kjMbEQYZLVIj5eOuMW3vDnSXlx9Nm6cTFQEiQ4SlUqHfEVph0L3jMdt8DrFZbyQX_XCtPFcNdLMbAevIfjQ7lQEL7_FanRbhX668yh2GvDvtkRRvQ-PX4Y0OxQYzBWa1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5234ca4dd.mp4?token=BUHIRufP4i5g-V1hjB0cZDuwR7ToG2Rfs8wO6Fmj4e54bZRp7NFt3terBvld72y4sMMICYgvhtBQbWEpppIqTqQjITGjFUmAcya1hKcsfKAqeBYUFoKEtZkCfJllWpUUGopavaxV5WbijvwW0NtK8FjWF9KH00fWX-8ZdvKkwg8MXqMm1F7HP90HDjZFrrs6S8yiTqsdwEJeBKEHpOEc1kjMbEQYZLVIj5eOuMW3vDnSXlx9Nm6cTFQEiQ4SlUqHfEVph0L3jMdt8DrFZbyQX_XCtPFcNdLMbAevIfjQ7lQEL7_FanRbhX668yh2GvDvtkRRvQ-PX4Y0OxQYzBWa1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار فاکس نیوز در اسرائیل: همچنان نیروهای آمریکایی در منطقه باقی خواهند ماند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/659891" target="_blank">📅 21:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659885">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ec236e29.mp4?token=UVDL9ykymGYozK2cGtIXzlaI6nbs0Nh83lEKF3T04vHlwHJMXCnfJxW-TrpdyixvSR5F5kU7-4cRsT-CCuZicPSbrEQQdrfg-Mw_5AxDfPoTkDKGGC1or2JW0UsXovKyR5kxPuYPt_7zyC7BYDE3Xanva-e1zX6WCggcuT6Cofs3xATIzrwcIxmivcz8k0_32DcC01nbCOjG-D9wVnZDL4yPNLwYa6jCb4uhdudMOJljYfYXhX8KfU0a7DswZVT6PDjh6MujYWCH7T1XLBBrCiRGXPsyGeKOV8Z84hm-zsuMvHyh00JZGLhsZiT1FqLHkLQIQ2xyhw03V83YIoLpyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ec236e29.mp4?token=UVDL9ykymGYozK2cGtIXzlaI6nbs0Nh83lEKF3T04vHlwHJMXCnfJxW-TrpdyixvSR5F5kU7-4cRsT-CCuZicPSbrEQQdrfg-Mw_5AxDfPoTkDKGGC1or2JW0UsXovKyR5kxPuYPt_7zyC7BYDE3Xanva-e1zX6WCggcuT6Cofs3xATIzrwcIxmivcz8k0_32DcC01nbCOjG-D9wVnZDL4yPNLwYa6jCb4uhdudMOJljYfYXhX8KfU0a7DswZVT6PDjh6MujYWCH7T1XLBBrCiRGXPsyGeKOV8Z84hm-zsuMvHyh00JZGLhsZiT1FqLHkLQIQ2xyhw03V83YIoLpyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
ویژه شب اول محرم
🥀
شهر را سیاه پوش کنید ؛
صدای محرم در کوچه پس کوچه های شهر می اید…
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/659885" target="_blank">📅 21:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659884">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/351804f828.mp4?token=X-e59mHckg6dMdOZyK6aw0MeL_94FzHcroIjroNY0N_saAsceGEWTJ_3v9OcCQK4qElGd-6NLY2yVyu2IbyL341NSaRc_YqkaA8OHvzl974dn80SLvVGipj6uURGGCYZcWg8FkxD6LXeCVgYuv4dmsTL70dPgLnQ2zklWjQXoLQhoPumIJuTcjEwOX-oj6F3UEsuP1oNYqPfpLHn2ehN0gxNFw4PGgpMuEHUwmXK2bzQrpIwYGXv2jdYkn6oXPGkZCnvSlumCRhl3pUr0wlySoMopHDKAF1Hkbrj4OfNIUAzwj2Kyg6INk184TDCsBFzFTg-zrjso40Z2BTBQgMJFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/351804f828.mp4?token=X-e59mHckg6dMdOZyK6aw0MeL_94FzHcroIjroNY0N_saAsceGEWTJ_3v9OcCQK4qElGd-6NLY2yVyu2IbyL341NSaRc_YqkaA8OHvzl974dn80SLvVGipj6uURGGCYZcWg8FkxD6LXeCVgYuv4dmsTL70dPgLnQ2zklWjQXoLQhoPumIJuTcjEwOX-oj6F3UEsuP1oNYqPfpLHn2ehN0gxNFw4PGgpMuEHUwmXK2bzQrpIwYGXv2jdYkn6oXPGkZCnvSlumCRhl3pUr0wlySoMopHDKAF1Hkbrj4OfNIUAzwj2Kyg6INk184TDCsBFzFTg-zrjso40Z2BTBQgMJFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تهدید تازه نتانیاهو؛ «هر زمان لازم باشد اقدام می‌کنیم
🔹
ما تا زمانی که لازم باشد در «مناطق امنیتی» مختلفی که تصرف کرده‌ایم باقی خواهیم ماند تا از کشور محافظت کنیم.
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/659884" target="_blank">📅 21:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659883">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a83d00b039.mp4?token=q5LtDZ38SlaB_OjWQJMKE4Q87elRw9zGP56gwpfyEO_B-Zs1L0oYj_2IS1d1eyqvoNjJjIgaoyPRerGL3s7pAzZMNCeYdTuzHeCZ6UVvIIVub5QONrP_TAIL3Ch7bvKiG-2Gls3mQreBJ0Tys4KKmAXcpOEr3kU-xp84IBrAZKu4HdUsWfeM2_Jm2ZJBLMDMOgu16uEfTpnNInUnCXMLp2gWvAI7i-B9d9lb2cyXeyjJG94z5hSIhzoGu4i3gnHR7Dr_dBv6Z3gvRwwNx7xGSiyEFDLXTSSO0f973zM16hqGAa1fXqM_l7FHoDm6Eg_Cm4pRU_9XY0MtV44tKBCcPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a83d00b039.mp4?token=q5LtDZ38SlaB_OjWQJMKE4Q87elRw9zGP56gwpfyEO_B-Zs1L0oYj_2IS1d1eyqvoNjJjIgaoyPRerGL3s7pAzZMNCeYdTuzHeCZ6UVvIIVub5QONrP_TAIL3Ch7bvKiG-2Gls3mQreBJ0Tys4KKmAXcpOEr3kU-xp84IBrAZKu4HdUsWfeM2_Jm2ZJBLMDMOgu16uEfTpnNInUnCXMLp2gWvAI7i-B9d9lb2cyXeyjJG94z5hSIhzoGu4i3gnHR7Dr_dBv6Z3gvRwwNx7xGSiyEFDLXTSSO0f973zM16hqGAa1fXqM_l7FHoDm6Eg_Cm4pRU_9XY0MtV44tKBCcPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو باز هم نقش آتش‌بیار معرکه را بازی می‌کند
نتانیاهو کودک‌کش مدعی شد:
🔹
«ماموریت زندگی من مبارزه با برنامه هسته‌ای ایران است.» او همچنین تأکید کرد که «با توافق یا بدون توافق، ایران به سلاح هسته‌ای دست نخواهد یافت.»
🔹
همچنین او ادعا کرد به اقتصاد ایران خسارات عظیمی وارد کرده‌ایم؛ برخی آن را یک تریلیون دلار برآورد می‌کنند.
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/659883" target="_blank">📅 21:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659882">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
پربازدیدترین ویدیوی این روزهای یوتیوب که میلیون ها بار بازدید گرفته در مورد اقتدار ایران
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/659882" target="_blank">📅 21:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659881">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🏆
مروری سریع بر داغ‌ترین حواشی این روزهای جام جهانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/659881" target="_blank">📅 21:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659880">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
سی‌ان‌ان: یک مقام ارشد دولت آمریکا گفت که عمان در جریان مذاکرات با ایران دوپهلو و غیرصادق بوده و عملاً از نقش سنتی خود در میانجی‌گری کنار گذاشته شده است
🔹
ما از کاری که عمانی‌ها انجام دادند بسیار ناراضی بودیم، احساس می‌کردیم که آن‌ها بسیار دوگانه‌ رفتار بودند و تقریباً مثل کارمندان ایرانی‌ها عمل می‌کردند، بنابراین ما آن‌ها را تا حدی از این روند کنار گذاشتیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/659880" target="_blank">📅 21:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659879">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FL8JKl6pZFoRdXlsjJ65vFHKCsaLeWITbNxd6XQg6CVrmUe0JlJxhb5_DbnY2N7oZBmig-QYwK03q5U3tJDSigJhzgfOnihKQWIEWZK329lQU8Lx-TD9v2JbUMHnBd-L9Jr9umVQejdzX6bgMb9ONV7Z311-W-RmkZvwMNRQ7bkRjTBX7YWJCJdnNm5mJw30XUJun8vrl0-0GkvDI7-2v7lkt7SCLBaTr7Z4EPgOetM4a95EoLkQJaY22ZbErhLqo5h4DAj3alsWEdLrb4b-O28_CWUwVaW5W0ZhGMTc4gUfdWJs1tBiOcID9bMML2wouR6rb2JCCdy1IUmiH8fSog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: هدایت‌های رهبر عالیقدر بیشترین نقش را در گنجاندن بندهای صیانت از منافع ملی ایران داشته که قدردان ایشان هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/659879" target="_blank">📅 21:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659878">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPZW0mClo1AxFIhI7Q35URWbyE_R734wzvefSMXi0iH1GcziCpVZcOdaJ8prTRgVZNxhSrBwo7V_MXKjtRtIGc0ch5QxeUIkkQDyLLo0YPYtpe5ToX7I9ULQPOPIIe4W4VuHiCUfMG9nesWJdkGeEmQiLOLqcjsVN8vWXSmXCyXV1AYd9aOcAFfecO5I80Z4HzB7608yDXsKzTiLG4cBaQKmvNvxxeIyqgxPO51tbrx3AuECyrrnA_xKakN-VCyoP6uJFSnG5oMY968EAW6TM6A9dbqRxjTsyY-5nyO-xqbUQNvKe7_aciV2VKA_dqlGbWrHNEc4mlp6UXtlZ52rDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسن‌ترین تیم‌های جام جهانی کدام کشورها هستند؟
🔹
پاناما تنها تیمی است که میانگین سنی بازیکنانش به ۳۰ سال رسیده است.
🔹
ایران نیز در میان باتجربه‌ترین تیم‌های جام جهانی ۲۰۲۶ در رده دوم مسن‌ترین‌ها قرار گرفته است.
🔹
حضور کشورهایی مانند کلمبیا، قطر و برزیل در این فهرست نشان می‌دهد بسیاری از مدعیان، همچنان به ستاره‌های باتجربه خود اعتماد کرده‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/659878" target="_blank">📅 21:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659877">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
اردوغان: توافق ایران و آمریکا راه را برای صلح در جهان باز می‌کند
🔹
رئیس‌جمهور ترکیه با استقبال از توافق میان ایالات متحده و ایران، آن را گشاینده راه صلح در منطقه و جهان دانست و از تلاش‌های پاکستان، قطر و عربستان برای تحقق این توافق قدردانی کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/659877" target="_blank">📅 21:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659875">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
شبکه ۱۳ رژیم صهیونیستی به نقل از برخی منابع: گفت‌وگویی پرتنش میان نتانیاهو و جی‌دی ونس درباره لبنان
‌
🔹
ونس خواستار عقب‌نشینی تدریجی از لبنان شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/659875" target="_blank">📅 21:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659874">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
عضو ناوگان صمود: در زمان بازداشت مورد تجاوز جنسی قرار گرفتم  جولیت لامونت، مستندساز استرالیایی و عضو ناوگان صمود:
🔹
در جریان توقیف و بازداشت توسط ارتش اسرائیل در ماه مه، وقتی دستبند و پابند داشته، داخل یک کانتینر تاریک توسط یک سرباز اسرائیلی مورد تجاوز…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659874" target="_blank">📅 20:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659873">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e0fcd76c0.mp4?token=HFPXDKz7EbQ_RQjy_-asXe0byXTwdutUYLlm9udly4J_8w7lm8C1n-RIuGrummu4T00q-wlRZMdRV2KXPHRBswe103aItMxy1Um1h6uf9-LK06PC8KgpoMKbGRDCU8u5FNVf611WVBoS-N8swz-IEKbPG2sqJ4gCxnxNHG8LXADG3A7gW6ABIsd4J5Ay4mfPYS6srlzniH4H2MIJOsFidjUVeNcsgGjez2-t8okCmnnj5mFiCk1Ed4Of9famlmrecCWjlQWELLlFQC1DO2qeuEHaDI6iDLfae-IUHSS58D3fnwuCQ-Ra0DKhkSQXMa4qx06vlQ7gCETQQxZUvxYwEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e0fcd76c0.mp4?token=HFPXDKz7EbQ_RQjy_-asXe0byXTwdutUYLlm9udly4J_8w7lm8C1n-RIuGrummu4T00q-wlRZMdRV2KXPHRBswe103aItMxy1Um1h6uf9-LK06PC8KgpoMKbGRDCU8u5FNVf611WVBoS-N8swz-IEKbPG2sqJ4gCxnxNHG8LXADG3A7gW6ABIsd4J5Ay4mfPYS6srlzniH4H2MIJOsFidjUVeNcsgGjez2-t8okCmnnj5mFiCk1Ed4Of9famlmrecCWjlQWELLlFQC1DO2qeuEHaDI6iDLfae-IUHSS58D3fnwuCQ-Ra0DKhkSQXMa4qx06vlQ7gCETQQxZUvxYwEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: سعی می‌کنیم از تفاهم ایجاد شده راهگشایی اقتصادی ایجاد کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659873" target="_blank">📅 20:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659872">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
آیت‌الله سیستانی، چهارشنبه را اول محرم اعلام کرد
🔹
دفتر آیت‌الله سیستانی، مرجع عالیقدر شیعیان با صدور اطلاعیه‌ای اعلام کرد روز سه‌شنبه، مکمل ماه ذی‌ الحجه بوده و  بدین ترتیب، روز چهارشنبه، نخستین روز از ماه محرم‌الحرام سال ۱۴۴۸ هجری قمری خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659872" target="_blank">📅 20:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659871">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ادعای
مقامات آمریکایی: آماده کاهش تحریم‌ها علیه ایران هستیم
شبکه cnn به نقل از مقامات ارشد دولت آمریکا:
🔹
آماده انجام گام‌هایی برای آغاز کاهش تحریم‌ها علیه ایران هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659871" target="_blank">📅 20:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659870">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
افزایش کالابرگ دهک‌های پایین تا دو هفته آتی
‌
وزیر امور اقتصادی و دارایی:
🔹
افزایش مبلغ کالابرگ دهک های پایین تحت پوشش کالابرگ در دستور کار قرار دارد و وزارت اقتصاد در حال آماده‌سازی پیشنهاد خود برای ارائه به دولت است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659870" target="_blank">📅 20:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659869">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
نجات از دو موجود وحشتناک با توسل به حضرت رقیه و ....
🔹
00:04:30 فشار مالی مرا از خدا دور کرد
🔹
00:07:50 لحظه نشستن روی کاناپه لحظه ورود به برزخ شد
🔹
00:15:20 رؤیت نوع عذاب غیبت‌کنندگان
🔹
00:21:00 اعمال خوبی که انجام دادنش فایده و ثمره‌ای نداشت
🔹
00:31:40  عذاب وحشتناکی که از جهت بداخلاقی با خانواده ام متحمل شدم
🔹
00:44:20 توسل به حضرت رقیه(س)
🔹
01:06:35 به جا ماندن کبودی سیلی برزخی بر کالبد دنیایی
🔹
قسمت چهاردهم (دخترم)، فصل چهارم
🔹
#تجربه‌گر
: علیرضا غلامی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659869" target="_blank">📅 20:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659868">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
صدراعظم آلمان: توافق ایران و آمریکا باید شامل لبنان نیز شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659868" target="_blank">📅 20:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659867">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حقایقی از تیم ملی ایران که شاید تا به امروز نمی‌دانستید!
🔹
تیم ملی در آستانه اولین دیدار خود در جام جهانی است
🔹
در این ویدیو نکات بسیار جذابی را از تیم ملی خواهید دید که شاید تا به حالا نشنیده باشید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659867" target="_blank">📅 20:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659866">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba82007ab0.mp4?token=oo45OzgVlTTZZ1g7Ovg6hNxonQyx_3VED48CO1TN8NGj9n-ooNRUch2M3ptIVo1hpk3sS-1vQegw1klflNGsBl6QQm3eQ-0_bChwW15iyEpuM-X_jziHpZK0SVsgaznlKWcl_ggT6E16q8Dmwd2kA-JRtxJv25-fSUJF2GZHGuwDaN0dtO3L8ZwjKDVr5ZA0MMsNZ8f7QBaosK_jWDdbcXTWIxbeKThSRdQwzU0T8OFmnc6JtiLHx18VemMkAThwgmlZ6m_0SlhZzOkzwqxfXixhxEG5iF04G1UGvGCWzkdc-PQ87stPEFYJb-zJWH2nIsCjezSGET6onnekWKnfsqj9TtM2mI3JQVp9iBvjiVp8Cu6yzIASO_UJGuP9ayKXeeDltJ5TxgbSWUZuWGLa--YZ7VUCxdcXaednEzRRuMlINp5OeO4pJsPMimD0rXbocsRmIlRA65iAgQv9Ixlw10doRmAGzcSekZTz3xblYxiPzwr4PROJy_tmuJDi3Qsf9XdCgSoE-mEjWlWzjKXyav7duko5VSJ_U5cfgzSQtShZACPeh1but8XkYXsTwdktCcjz8FwnPeZIrDHnzokPKyf7tSBzjCiMttV96TwNaq1hXyTYafWl_halhEAS8rEicVd8KaK-XsWIAVH11hP5fpizWxysq4OASrcVM0flrBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba82007ab0.mp4?token=oo45OzgVlTTZZ1g7Ovg6hNxonQyx_3VED48CO1TN8NGj9n-ooNRUch2M3ptIVo1hpk3sS-1vQegw1klflNGsBl6QQm3eQ-0_bChwW15iyEpuM-X_jziHpZK0SVsgaznlKWcl_ggT6E16q8Dmwd2kA-JRtxJv25-fSUJF2GZHGuwDaN0dtO3L8ZwjKDVr5ZA0MMsNZ8f7QBaosK_jWDdbcXTWIxbeKThSRdQwzU0T8OFmnc6JtiLHx18VemMkAThwgmlZ6m_0SlhZzOkzwqxfXixhxEG5iF04G1UGvGCWzkdc-PQ87stPEFYJb-zJWH2nIsCjezSGET6onnekWKnfsqj9TtM2mI3JQVp9iBvjiVp8Cu6yzIASO_UJGuP9ayKXeeDltJ5TxgbSWUZuWGLa--YZ7VUCxdcXaednEzRRuMlINp5OeO4pJsPMimD0rXbocsRmIlRA65iAgQv9Ixlw10doRmAGzcSekZTz3xblYxiPzwr4PROJy_tmuJDi3Qsf9XdCgSoE-mEjWlWzjKXyav7duko5VSJ_U5cfgzSQtShZACPeh1but8XkYXsTwdktCcjz8FwnPeZIrDHnzokPKyf7tSBzjCiMttV96TwNaq1hXyTYafWl_halhEAS8rEicVd8KaK-XsWIAVH11hP5fpizWxysq4OASrcVM0flrBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لغو تحریم‌ها بستگی به رفتار ایران دارد و فوری نخواهد بود
🔹
خبرنگار:  آقای رئیس جمهور، آیا این توافق شامل لغو زودهنگام تحریم‌ها برای ایران می‌شود؟ این لغو زودهنگام از چه زمانی اجرایی خواهد شد؟
🔹
ترامپ:  نه، اجرایی نمی‌شود. این واقعاً مرتبط با رفتار (ایران)…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659866" target="_blank">📅 20:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659865">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4cb986925.mp4?token=EPgD66i1hdUTGt1fH1fdaO4KbWTnUgCIsIgr9vUoKLou4dMsqCGBouJbcio--LUpMiSVVuEDYzDCzTKC3FrlAVd94ljR19uJ1CoU16bKsvtidZUx7DnFhTyvoFE9qR9wIx0EDPc9Tj2i8L4tcl22vmzozmBWP-F32YVPbDGSTfUaV-Q-6paF6ANSgoXsnPwChN1A04v8uFVai9C5OWQY9cSsPwbTQL-QBz2Mbl_QF5ZRfQRE8kVGFH_aZwT0A5vSAtIdNzdkm7_Z88_oE5djRoUeBuiCIenoe0lxapzYie2-aQHaiTo2FtPwRG0L2ubXe5bYEf0SqtbhPe3u-etM5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4cb986925.mp4?token=EPgD66i1hdUTGt1fH1fdaO4KbWTnUgCIsIgr9vUoKLou4dMsqCGBouJbcio--LUpMiSVVuEDYzDCzTKC3FrlAVd94ljR19uJ1CoU16bKsvtidZUx7DnFhTyvoFE9qR9wIx0EDPc9Tj2i8L4tcl22vmzozmBWP-F32YVPbDGSTfUaV-Q-6paF6ANSgoXsnPwChN1A04v8uFVai9C5OWQY9cSsPwbTQL-QBz2Mbl_QF5ZRfQRE8kVGFH_aZwT0A5vSAtIdNzdkm7_Z88_oE5djRoUeBuiCIenoe0lxapzYie2-aQHaiTo2FtPwRG0L2ubXe5bYEf0SqtbhPe3u-etM5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایرانی‌ها نظارت قوی بر تأسیسات هسته‌ای را پذیرفتند  ترامپ در دیدار با مکرون:
🔹
آنها کاملاً با این موضوع موافقت کردند و با قدرت‌های نظارتی قوی، سلاح هسته‌ای نخواهند داشت، که دلیلش هم همین بود، چون اگر سلاح هسته‌ای داشتند، احتمالاً از آن استفاده می‌کردند.
🔹
و…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659865" target="_blank">📅 20:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659864">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed953f1774.mp4?token=Hi4hdiq20J5KVvfi-9zMOnIiV67WqKc78kTT3o4QXb5jPXHHrQzXwX9LmLYEMRa5ufFzgoda67DSjx-hDhLenBxITvibJPIoQ1sM1jW7STVSxpyw2-nEaPn20jFnS874avjB09oSt0EM-RJDlYhodwCRfveoNMiHztoUnTP6ImuDBycTeZtzfHFAd29dBmzA528uak5W9mBfWZmRnF4eKzqTK2kqutPr_vTYBP535GxfxwbLM6uXlihkEz7jSMr35uBhmQ3nkQXHhIxapQgMWORLkdOXr5nhTNSQbgu8mkeGkjAKMyIBYhM2fC7ByyslrDIaq-nOCuNMNO-9jjXBow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed953f1774.mp4?token=Hi4hdiq20J5KVvfi-9zMOnIiV67WqKc78kTT3o4QXb5jPXHHrQzXwX9LmLYEMRa5ufFzgoda67DSjx-hDhLenBxITvibJPIoQ1sM1jW7STVSxpyw2-nEaPn20jFnS874avjB09oSt0EM-RJDlYhodwCRfveoNMiHztoUnTP6ImuDBycTeZtzfHFAd29dBmzA528uak5W9mBfWZmRnF4eKzqTK2kqutPr_vTYBP535GxfxwbLM6uXlihkEz7jSMr35uBhmQ3nkQXHhIxapQgMWORLkdOXr5nhTNSQbgu8mkeGkjAKMyIBYhM2fC7ByyslrDIaq-nOCuNMNO-9jjXBow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: تنگه هرمز تا حدی باز شده است   ترامپ در دیدار با مکرون:
🔹
تمام توافق امضا شده است، تنگه هرمز از قبل تا حدی باز شده است.
🔹
آنها در حال جستجوی کمی برای یافتن چند مین هستند. کشتی‌ها اکنون شروع به حرکت کرده‌اند. روز جمعه، تنگه کاملاً باز خواهد شد.…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659864" target="_blank">📅 20:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659863">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HD4DUXja9MPDxWSVUuQhcq5ZDhl-yhHWA1ruStERppKcdvK_j7swlSy5t6N6Rjq7ez--RGNJob4p1MJvGfI1vAvPlL3jpz_7TnslnBP3CKco0qoY0ngFfXVV94f25TcLcXRDNGl6mCA2HqsA7esddVdPpgp3Ci1PPKjl5An7xsXkiMDL75Y-zQ9CyK3miUPb8cT8lXV9gIbXNKJMCLRLhgphzaMcSwBieiU8kllAKdbuOVdav6LYjgtluzdgwqzmvNcm-f7VfRza-6a-54rXxOWRWnD1g6k6YxBU_Z69qcIO-TQTi-d-TfvdhfPleKrmiXzga6hWu8DcCyMKAq7T_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورود بازار آنلاین طلا به مقیاس تازه؛ پرمخاطب‌ترین اپلیکیشن خرید و فروش طلا ۲۵ میلیونی شد
📊
بازار آنلاین طلا در ایران طی سال‌های اخیر با رشد قابل‌توجهی همراه بوده و حالا
میلی به‌عنوان یکی از بازیگران این حوزه اعلام کرده که در کمتر از سه سال به ۲۵ میلیون
کاربر رسیده است.
🔸
براساس داده‌های اعلام‌شده از سوی میلی هر کاربر از زمان راه‌اندازی این اپلیکیشن تاکنون
به‌طور میانگین چهار نفر از دوستان یا آشنایان خود را به استفاده از خدمات میلی دعوت کرده است
؛ آماری که می‌تواند نشانه‌ای از افزایش اقبال کاربران به خریدوفروش و پس‌انداز آنلاین طلا باشد.
🔹
میلی در تلاش است تا طلا را وارد زندگی روزمره کاربران کند. برای همین در کنار امکان خریدوفروش و پس‌انداز طلا سرویس‌هایی مانند «خرید قسطی طلا» و «دریافت وام خرید کالا به اعتبار طلا» را نیز به سبد خدمات خود اضافه کرده است. به همین علت تاکنون کاربران زیادی تجربه استفاده از خدمات میلی را با یکدیگر به اشتراک گذاشته‌اند.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659863" target="_blank">📅 20:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659861">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HmXzJyGfFBTRdGL7TA5JGb4AN9JqAYHRc8Uy62WmGCWYxmlEQAaaHYb3Txlba1tfy3_Fx4CxjqXg1NFd6Fu1cAu5JbW4mSHIsjfjplnGRsPGN4xfMY74oz-P-yfHOFvmzYMYfQzA7C18daq1v--208Kh7nXXmeVErKZjEawfVeBfeJT0UVaLOk1QEhws6cYr8TjyVQUcnwyZR2l2-5Lqkblu-jR3bZWtcxAJDkpqCDzJIfLGUrVMwX-rJ-LWwXt0L2Y0weJIui1ec3CAJWV60dnxakgU8L3hR34r6hjEShJcltXEqFqZPHrSPPLmexlQuWM0CytCgxVKTGlU7z4Nfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qH1473XOKiPhwaMlgpVE4M3yGkHUXJXYjUPBx3DUI6XPzd_XzEua8WS9C09IUIIDfmE-q4MHNJXz1tlnCxcDc_fbKQ6aaTSvrkfvnB9Hnn4oVcRkiu8NPF5DUsxGEEQqiWgww2vLdY-nLbZhkg5RzpCZGFhynuB0M17zuK_Cd-5_L3AG5boe9e3P8Dl2BQoPbqt2kwHOjKJlpZ0Q2dRqaeHjcFW7jfrBV6lZukDpyFfZzzmv2Z96KAwK4ZJ5hm53IY9LMAX6qm8sYTx19f4RsCEGfArZdEI-iZOmcRSit57sDkSi54RinvIb0qzkhWy_JRGEoLtK59nLi8sKA8aUsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📚
نام کتاب: حسین از زبان حسین (ع)
🖋
نویسنده: محمد محمدیان
🔹
این کتاب روایتی متفاوت و اثرگذار از زندگی امام حسین(ع) است که حوادث را از زبان خود آن حضرت بازمی‌گوید و از ولادت  تا شهادت را با نثری روان و مستند پیش می‌برد.
🔹
برای کسانی که به دنبال آشنایی عمیق‌تر…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/659861" target="_blank">📅 20:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659860">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0c3dfd0d6.mp4?token=fo8ZvvdhHOHzZCGAzPAPuA1uhbcGSnXD4NyUiyn-AiuPJh6eu64Lx6JxfxGqI7hlJBGNVOr0R_VzQre3tPL1gWGGTPSBWKTa2cwhu8n_jBQLD3O78urWAM-jlbLFv9U6VcpJwbJXBq96lOdiHXYA7JRcc6H9cjWMNj2dmtycp3-xzZL8v9zpQS0IYskU1wIt1FGZIjvlTP6b6TK3TGZ8eYSeSOadNjYx15nKKkqURWr1OmH-S69Zc_oe-HrOnF66raL9km8ty6h6SXsPVkgqXUKP1m7qs8cI3uhzxGy60mszqGpzXgZcto7JrqIUY-guAEIeW8fI5MBnq9XpQstFWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0c3dfd0d6.mp4?token=fo8ZvvdhHOHzZCGAzPAPuA1uhbcGSnXD4NyUiyn-AiuPJh6eu64Lx6JxfxGqI7hlJBGNVOr0R_VzQre3tPL1gWGGTPSBWKTa2cwhu8n_jBQLD3O78urWAM-jlbLFv9U6VcpJwbJXBq96lOdiHXYA7JRcc6H9cjWMNj2dmtycp3-xzZL8v9zpQS0IYskU1wIt1FGZIjvlTP6b6TK3TGZ8eYSeSOadNjYx15nKKkqURWr1OmH-S69Zc_oe-HrOnF66raL9km8ty6h6SXsPVkgqXUKP1m7qs8cI3uhzxGy60mszqGpzXgZcto7JrqIUY-guAEIeW8fI5MBnq9XpQstFWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: شاید بتوانیم در مورد اوکراین کاری انجام دهیم. فکر می‌کنم هم پوتین و هم زلنسکی برای آن آمادگی دارند
🔹
حالا که ایران تمام شده، قرار است روی آن تمرکز کنیم #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/659860" target="_blank">📅 20:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659859">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
متن تفاهم‌نامه با ایران به زودی منتشر می‌شود
🔹
خبرنگار:  متن تفاهم‌نامه چه زمانی منتشر خواهد شد؟
🔹
ترامپ:  فکر می‌کنم خیلی زود. منظورم این است که می‌خواهم منتشر شود. این یک سند قدرتمند است. مثل سند اوباما نیست که فقط یک سند وحشتناک بود #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/659859" target="_blank">📅 19:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659858">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
عضو کمیسیون بهداشت مجلس: افزایش حقوق و متناسب‌سازی، نشانه ایفای تعهدات قانوی تأمین اجتماعی است
🔹
احمد آریایی‌نژاد، عضو کمیسیون بهداشت و نماینده مردم ملایر، با اشاره به افزایش حقوق بازنشستگان و اجرای متناسب‌سازی گفت: این اقدامات نشان‌دهنده ایفای تعهدات سازمان تأمین اجتماعی در قبال بازنشستگان است؛ موضوعی که در شرایط جنگ و بحران اقتصادی اهمیت دوچندانی پیدا می‌کند.
🔹
وی با تأکید بر اینکه متناسب‌سازی گامی در جهت عدالت و حفظ قدرت معیشتی بازنشستگان است، افزود: دولت و مجلس باید برای تأمین منابع پایدار و استمرار این مسیر، حمایت‌های لازم را از تأمین اجتماعی به عمل آورند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659858" target="_blank">📅 19:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659857">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdbba1879c.mp4?token=GzViGW0t00wsnzHtC2k7HC0kgxgPxCyJu3aMRyAzbz--t8v8Ghc14T1h17_i2shV2TN1KNSNoO2vc63DDkjGvVks4JyaeUP3geR6cY17GnHOdqf63xLbZx3NqNhro3vB3LPACzSNL7q2TpG_i7rKo_wlMnn6B2q9IwYgPxJQUXcDUapu2s099ORGu5ghLs8OdnkpT_WVbpA-EfBBfArZlO57S8LMG-Tb3IyJnF_ICK3IJsIs3moK1tR0BzjD5hAh9cn_BzINPYGyp7G1kxqfw8jEqah1nrYPxZDaKG04CoI2Wpq9GMiIeEOkaj2QIeo1rEKdsnOH_kL-uy_yqhC_XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdbba1879c.mp4?token=GzViGW0t00wsnzHtC2k7HC0kgxgPxCyJu3aMRyAzbz--t8v8Ghc14T1h17_i2shV2TN1KNSNoO2vc63DDkjGvVks4JyaeUP3geR6cY17GnHOdqf63xLbZx3NqNhro3vB3LPACzSNL7q2TpG_i7rKo_wlMnn6B2q9IwYgPxJQUXcDUapu2s099ORGu5ghLs8OdnkpT_WVbpA-EfBBfArZlO57S8LMG-Tb3IyJnF_ICK3IJsIs3moK1tR0BzjD5hAh9cn_BzINPYGyp7G1kxqfw8jEqah1nrYPxZDaKG04CoI2Wpq9GMiIeEOkaj2QIeo1rEKdsnOH_kL-uy_yqhC_XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اولین هیجان و اولین قدم یوزهای ایرانی در جام جهانی پیش‌بینی جام تایم از بازی نخست تیم ملی در برابر نیوزلند
🔹
قسمت دوم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/659857" target="_blank">📅 19:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659856">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df1985986c.mp4?token=DAffNYQsow9ra9g8kTcLoJmKAWB60F_HG7G4p5xkC6pPbkyF22PxcO6TRrQpfYxmV9tZ0cdR78aW90njdizgvmyJMGLhx-YowKjGbN2WoYBe_ROTpDf_kPRopqQ7e7NJcpzqadxguxvJaqC7k1HLSNT8S28ZeIshYmOGk7Q4allZWsggkduZgs5Fjcb4KE_kPSGForyCOsI_En7FRjC1FR1W-NkTjCjtpkJDtP1A338AA9R9eV1ZyFrs4NDRIu_YdBWMO3mMzhHHBrtdAY6CQqYZrNKsPt_4hpLW2KgVXuo-HHDWhITdScg8-yW8LbkII9mHfZaAkX23yXiYwMZNDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df1985986c.mp4?token=DAffNYQsow9ra9g8kTcLoJmKAWB60F_HG7G4p5xkC6pPbkyF22PxcO6TRrQpfYxmV9tZ0cdR78aW90njdizgvmyJMGLhx-YowKjGbN2WoYBe_ROTpDf_kPRopqQ7e7NJcpzqadxguxvJaqC7k1HLSNT8S28ZeIshYmOGk7Q4allZWsggkduZgs5Fjcb4KE_kPSGForyCOsI_En7FRjC1FR1W-NkTjCjtpkJDtP1A338AA9R9eV1ZyFrs4NDRIu_YdBWMO3mMzhHHBrtdAY6CQqYZrNKsPt_4hpLW2KgVXuo-HHDWhITdScg8-yW8LbkII9mHfZaAkX23yXiYwMZNDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متن تفاهم‌نامه با ایران به زودی منتشر می‌شود
🔹
خبرنگار:
متن تفاهم‌نامه چه زمانی منتشر خواهد شد؟
🔹
ترامپ:
فکر می‌کنم خیلی زود. منظورم این است که می‌خواهم منتشر شود. این یک سند قدرتمند است. مثل سند اوباما نیست که فقط یک سند وحشتناک بود
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/659856" target="_blank">📅 19:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659855">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e99fa9a3b.mp4?token=a1pKquKEQoac7Q8x6-X16-2eE2c5p_x1HW-QKvkuIyW3cP3GFGUnsRPjpwBux-qcVafU8MaET6w_RYW63emw13jAAcOtTXbyxJBVc8j2ARrc_BPFGBnCS4DgQeBLnIQwiuKEH_KCxQ5AnxpcrUfRUIH5P91FQzb-_q49m9lF2xTFFRzymDCRv8RxRXwaANrCj9p5Gdidrs8nGBAtbhKGhtgMcp5lcqOLPbD3EnW2P_ynWF3_2FpCHEm8IxkFoCnMhp1FyJRZ23Iu67HLjuUngutgEvJ9S1ELjmNkK7WHaO4x2fEU3Lflyqq95WkSNqf6MqIianR6LEqYR5jSV5DOvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e99fa9a3b.mp4?token=a1pKquKEQoac7Q8x6-X16-2eE2c5p_x1HW-QKvkuIyW3cP3GFGUnsRPjpwBux-qcVafU8MaET6w_RYW63emw13jAAcOtTXbyxJBVc8j2ARrc_BPFGBnCS4DgQeBLnIQwiuKEH_KCxQ5AnxpcrUfRUIH5P91FQzb-_q49m9lF2xTFFRzymDCRv8RxRXwaANrCj9p5Gdidrs8nGBAtbhKGhtgMcp5lcqOLPbD3EnW2P_ynWF3_2FpCHEm8IxkFoCnMhp1FyJRZ23Iu67HLjuUngutgEvJ9S1ELjmNkK7WHaO4x2fEU3Lflyqq95WkSNqf6MqIianR6LEqYR5jSV5DOvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای ایران
🔹
در آستانه اولین بازی تیم ملی فوتبال ایران، مخاطبان خبرفوری با ارسال پیام‌های صوتی، به ملی‌پوشان انرژی و انگیزه دادند.
🔹
این ویدیو، بخشی از پیام‌های صوتی مردم برای ملی‌پوشان است؛ صداهایی از جنس امید، عشق و حمایت.
🔸
شما هم با صدای گرمتان انرژی بخش ملی‌پوشان باشید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/659855" target="_blank">📅 19:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659854">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پیراهن شهرم رنگ مشکی داره</div>
  <div class="tg-doc-extra">مداحی آنلاین</div>
</div>
<a href="https://t.me/akhbarefori/659854" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎼
پیراهن شهرم
رنگ مشکی داره
آماده‌ی کاره
هر کی عشقی داره
🎙
حسین_طاهری
#زمینه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/659854" target="_blank">📅 19:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659853">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bebc4fb1c.mp4?token=EZLgzO4izghBfyZfnqlcWRDdTblAdxJfSBJ9vUCH7if9NajyaF3w80BVarYxL5rm3pY69nhJn-jPXIRkkXiVfyDW5muzXTMBxHwY-Kk5Qj1pPNa1HVBCJJSt2Jjcoq4u6puyaT7fBBrDir47buMDK4Y_1xJ6USVeyM-YQSiz6BhMdURikPj8RAE4rqihODG4_z2GIKymjY2mka4VJF10ir47xRzSYlRHlKt-B2TrDMA7-ILUgKb5pdu_q-NlpdenF9csZfO4Ubrg6HTYoGuJWTqQj0tehdDFNFl2asWi4sJp1W0nr5j4On_zv0jQtmSg21YVNhELpWeztLUSVMeVoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bebc4fb1c.mp4?token=EZLgzO4izghBfyZfnqlcWRDdTblAdxJfSBJ9vUCH7if9NajyaF3w80BVarYxL5rm3pY69nhJn-jPXIRkkXiVfyDW5muzXTMBxHwY-Kk5Qj1pPNa1HVBCJJSt2Jjcoq4u6puyaT7fBBrDir47buMDK4Y_1xJ6USVeyM-YQSiz6BhMdURikPj8RAE4rqihODG4_z2GIKymjY2mka4VJF10ir47xRzSYlRHlKt-B2TrDMA7-ILUgKb5pdu_q-NlpdenF9csZfO4Ubrg6HTYoGuJWTqQj0tehdDFNFl2asWi4sJp1W0nr5j4On_zv0jQtmSg21YVNhELpWeztLUSVMeVoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باز بوی غم ز کوی محرم رسیده است
دل‌ها به یاد غربتِ مظلوم تپیده است
آغاز ماه ماتمِ سلطان کربلا
بر عاشقانِ حضرتِ ثارالله تسلیت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/659853" target="_blank">📅 19:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659852">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
ترامپ درباره ایران: اتفاقات بسیار خوبی در خاورمیانه رخ خواهد داد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/659852" target="_blank">📅 19:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659851">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piwoKu97DzUuWvmBDX_XUvjTjYSnOzvVx_zD13plhZ4IomrkcUVJejuPW-yQyT9OzUnfG3y5DGBlFA3DFGo4n6Lh9WPXS0re6tqn8D-p38VAWeKks7d34ShzCuh_xgRRiDrC-ixUjQJ_XlreFwQpqADKYN7Bqj58QuwqPmg0l0blz8kaoPFDwOdTQ44sy7nOBoiwjJ3KNE0yG1GIjGitpmagywVS43mzugNv0fvN3YpKApkK7RFtcObmCBl-3Qm3yzcRURLXr700tEan4POS3aIBWu208AjaiBNQhSftaSnUkPlDSx2VRZqrLUDX1iTSH_88nTNNGFm8RPmDQlvRNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحویلِ سال به وقتِ مُحَرّم است؛
حَوّل قلُوبَنا بِبُکاءِ عَلَی الحُسَین ...
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659851" target="_blank">📅 19:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659850">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
نخست وزیر پاکستان: تفاهم آمریکا و ایران پیروزی برای صلح و دیپلماسی است
شهباز شریف:
🔹
توافق آمریکا و ایران پیروزی برای صلح و دیپلماسی است؛ ما روز جمعه میزبان مراسم امضای این توافق در ژنو خواهیم بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659850" target="_blank">📅 19:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659849">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
دیروز تولد قاتل ۱۶۸ کودک معصوم بود
🔹
فرشته هایی که پیکرشان هم پیدا نشد صحبت هایی با قاتلشان دارند...
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659849" target="_blank">📅 19:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659848">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
پیش فروش بلیت‌ قطارهای مسافری تیرماه از روز چهارشنبه
🔹
پیش فروش بلیت‌ قطارهای مسافری برای بازه زمانی ۱ تا ۳۱ تیر (مسیرهای رفت تا تاریخ ۳۱ تیر و مسیرهای برگشت تا تاریخ یکم مرداد ۱۴۰۵) از روز چهارشنبه ۲۷ خرداد آغاز می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659848" target="_blank">📅 19:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659847">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNi6fwGjcygBA96owYOG2Znxzu36atWOFNRTmPWK0vnoV7UfwD3Xjq9kJSQPK8W-cR5LtBzxTqrBZIuVxgAwXiTvOfV0DuajuxhFW1YyVFTKg-6ATxYEcfykc9iqHsdJCNs0pipre212746mlssuq9IcMUSPt04l6X3jvhcbI5uWGmfMnFifxJ6jTPoGIW3SXSnkmfRCVKb7UGOOxLNzSOIiDUsQVJqaMqkKFeaY6p45MjW3T6YpF8e1tTjKaGp9DorjZVhxTSMNzajiJsgxVYoNkqPlCUaOtmmCv2E2cGa8g63ehOo9VsLNRbzy_5mhItMV1lpi-MvyT1mtBx-2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: با مقاومت تاریخی ملت و رشادت نیروهای مسلح، ایران گامی بلند به سوی پیروزی نهایی برداشت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659847" target="_blank">📅 19:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659846">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3953919e97.mp4?token=b2NnEZ7O3VL9-UfFpVaVZ8zFSjWpTukq5XrucuG-tQVj_i9xTM8xwFVx1kHsDYNg89XLw--ZBHIZ2bXXf77PpyKPUc7pFntwjq87Oh-scwB4WRUbhGTYa7xEDLwtxVNDP4Y37Yx20AA7r_Q9b_rmjisRolAvmDD31dh7RLYDvKF07AQ9y5H_-Y4gC5dDxN15DkSQHYJMJpaz5uUcOwWsLV3xksRqsUEzrOCKfAqddl4UEub0GP8N1T3IDcMQW-r4sop564ZL7s_nvw77vA70AVUyFxzpf5-yNebkUyzyas8gpwiWEMYe5Mw5G5eGIDoiVWQl_Vg5u36ydy0Z0Zhb7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3953919e97.mp4?token=b2NnEZ7O3VL9-UfFpVaVZ8zFSjWpTukq5XrucuG-tQVj_i9xTM8xwFVx1kHsDYNg89XLw--ZBHIZ2bXXf77PpyKPUc7pFntwjq87Oh-scwB4WRUbhGTYa7xEDLwtxVNDP4Y37Yx20AA7r_Q9b_rmjisRolAvmDD31dh7RLYDvKF07AQ9y5H_-Y4gC5dDxN15DkSQHYJMJpaz5uUcOwWsLV3xksRqsUEzrOCKfAqddl4UEub0GP8N1T3IDcMQW-r4sop564ZL7s_nvw77vA70AVUyFxzpf5-yNebkUyzyas8gpwiWEMYe5Mw5G5eGIDoiVWQl_Vg5u36ydy0Z0Zhb7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس: ما آمادگی کامل داریم تا کشورهای عضو شورای همکاری خلیج فارس، سرمایه‌گذاری‌های گسترده‌ای در فرآیند بازسازی ایران به عمل آورند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659846" target="_blank">📅 19:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659845">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ed1fbc1e1.mp4?token=syPp_P1ECPTXdnFrUySqzv0lBoZFoX_hk11UE_S4gFCnPhWQCIhUMVYCkyCNCWhN_EwItNpsxlorjmcj8Hs-omnq_nKIYR8jIaLie3ETRFhadQTxSbOAzlzRYPH5fV2ztCIYNdaGZbDUlP4KNyw-ZatJDYsBzu-HCq7bYQ6hunL7R2mi2k3mKrajPctbinCe6_voMbzZ0LtiAEkZiZxrTdvl54ZzHPBEXPVe5F3JUVMif0EvtEO0FHMO4xEVV0ivR_DTuGFY344XSopiXa2Qomw20ApoqDw-FJRvVaQWxrlNp3--cN0a95Mho4Oblfmb5KhfnddRtKK4ZdriJv_f5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ed1fbc1e1.mp4?token=syPp_P1ECPTXdnFrUySqzv0lBoZFoX_hk11UE_S4gFCnPhWQCIhUMVYCkyCNCWhN_EwItNpsxlorjmcj8Hs-omnq_nKIYR8jIaLie3ETRFhadQTxSbOAzlzRYPH5fV2ztCIYNdaGZbDUlP4KNyw-ZatJDYsBzu-HCq7bYQ6hunL7R2mi2k3mKrajPctbinCe6_voMbzZ0LtiAEkZiZxrTdvl54ZzHPBEXPVe5F3JUVMif0EvtEO0FHMO4xEVV0ivR_DTuGFY344XSopiXa2Qomw20ApoqDw-FJRvVaQWxrlNp3--cN0a95Mho4Oblfmb5KhfnddRtKK4ZdriJv_f5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارزش تجهیزات هر لابراتوار سیار به‌طور میانگین به ۱۰ میلیارد تومان می‌رسد
سجاد محمد علی نژاد معاون مالی و اقتصادی شهردار تهران در مراسم رونمایی از لابراتوار سیار خلاقیت و ساخت:
🔹
در اتوبوس‌های رونمایی‌شده نیز مجموع تجهیزات نصب‌شده به ده‌ها میلیارد تومان می‌رسد و با اضافه شدن آزمایشگاه‌های تخصصی‌تر، هزینه تجهیز این واحدهای سیار افزایش خواهد یافت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659845" target="_blank">📅 19:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659844">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
سخنرانی امشب نتانیاهو درباره تفاهم ایران و آمریکا
رسانه‌های عبری:
🔹
نخست‌وزیر رژیم صهیونیستی قرار است امشب در خصوص تحولات اخیر و تفاهم‌نامه حاصل‌شده میان ایران و ایالات متحده آمریکا سخنرانی کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659844" target="_blank">📅 19:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659843">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
من عزاداری تو رو دوست دارم...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659843" target="_blank">📅 19:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659842">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
رئیس کمیسیون اروپا: تحریم های ایران کاهش نخواهد یافت
اورسولا فون در لاین، رئیس کمیسیون اروپا در موضع گیری خصمانه اعلام کرد:
🔹
اتحادیه اروپا بدون تغییرات مشخص در سیاست‌های ایران، تحریم‌های خود را کاهش نخواهد داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659842" target="_blank">📅 19:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659841">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e56e60def.mp4?token=je6pQv9vlRcSBAVEpoZM7bW2IaxRM5nENg3pTbo24iSPfLcbLMP-6lif6wB7RNGKPLtoLHqRu6JMAY_FciZBkVJQZ9udQDCyL3ZE0-DF61f-XicfbF-9geIRxDvi_Eh-dh2mc4Ijalrh7S5nq4npqtcMgfsg3KJJUzyxUyc-ei82jwhVV6HWgfiydir58avB_t0VZn4RT_vma9hkuM9z2R9ft0U1061ApNncxVA6Ae4yMKeoRGE2RMnTxdmVxDhnn-T4XNXN_tGsDUo3-8cP97r8oBh7QCSXvnnkvuiuhtLfrwScpsoyLfFvRowNL-Mt2GTypbfWO2JXRqKvqpsTUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e56e60def.mp4?token=je6pQv9vlRcSBAVEpoZM7bW2IaxRM5nENg3pTbo24iSPfLcbLMP-6lif6wB7RNGKPLtoLHqRu6JMAY_FciZBkVJQZ9udQDCyL3ZE0-DF61f-XicfbF-9geIRxDvi_Eh-dh2mc4Ijalrh7S5nq4npqtcMgfsg3KJJUzyxUyc-ei82jwhVV6HWgfiydir58avB_t0VZn4RT_vma9hkuM9z2R9ft0U1061ApNncxVA6Ae4yMKeoRGE2RMnTxdmVxDhnn-T4XNXN_tGsDUo3-8cP97r8oBh7QCSXvnnkvuiuhtLfrwScpsoyLfFvRowNL-Mt2GTypbfWO2JXRqKvqpsTUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپاد انتحاری اسرائیل به زندان «اصداء» در
غزه
🔹
پهپادهای انتحاری رژیم صهیونیستی در تازه‌ترین اقدام نظامی خود، یکی از ساختمان‌های واقع در زندان «اصداء» در شمال شهر خان یونس را هدف قرار دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659841" target="_blank">📅 19:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659840">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
عراقچی: احتمال امضای تفاهم‌نامه ایران و آمریکا روز جمعه در سوئیس
وزیر امور خارجه:
🔹
احتمالاً روز جمعه در سوئیس دیداری میان رؤسای هیئت‌های مذاکره‌کننده ایران و آمریکا برگزار و تفاهم‌نامه‌ای امضا شود و سپس نخستین دور مذاکرات بعدی انجام گیرد؛ این تفاهم می‌تواند گشایش‌های اقتصادی ایجاد کند، اما اقتصاد کشور نباید به چنین توافقاتی متکی شود.
🔹
عراقچی با اشاره به سابقه بدعهدی‌ها و عدم اجرای توافقات، تأکید کرد روند مذاکرات و اجرای توافق بر اساس بی‌اعتمادی و تجربیات گذشته برنامه‌ریزی می‌شود؛ ایران از مسیر توافق برای ایجاد گشایش اقتصادی استفاده می‌کند، بدون آنکه به آن دل ببندد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659840" target="_blank">📅 18:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659839">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuRu7ZKuU7l7X_ISI69zJ0jXD1vdD1Lkt0dCGYpRkW6_L_zvnA7wYLtwC-jdptXNW7yRoUV5yTGWFYtnfbR03xiOI9KxAuRzIpxKUokL02VJYirljMYZZaeyKzQpMWSIofukPclxLVLOflM9fxxdkX9y_P4x2vxKpGsInKODSTywR_-qR_vgoj1xyAmbuXn0FqF1_L31XBpisLS_HFoar82d5S2kliVtG-kbytWEhpefvlWWJ9SyvTY9D1mBn_OPF9T0rH0Ga27Qj49UJu5xJAFfa6iKbiGYZSRysGrUl7Nu3_MIyDXOPEM1Utxq7CJxcD--nbE7t4eBW-3a1ET4cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659839" target="_blank">📅 18:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659838">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76223f1b49.mp4?token=qC7IEnUV_ikgewB3PjZXotyvmc5rVOi2aZ-_ivfv4acsVhhkjYjFSVYVsH5ji_RtoF_-rNWDmsCv3gP89xZ19MJfnvziGE2ffRehfeK_kXHdPPzMmo7ABmd7RXKQIk4paRt8i3MvDGyx89pY-cVidlHPvWxgjwIQpYtEA5le5NG2YaMSDCXiiEddnE5a-3oX9uAqdgkkBc5-9JluxM_iseOHknN3TEBXTvEk8DLJy1Thx0K3VsEkW_RNneVStu73ZSBjtgEMT-RDGro2yM5YIVI_CjxOi3PxO_mVGkRsB-nUXoqS5r9NyEYQ4A23Cy-UmFdrU5FW0O0oCZC90wdA6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76223f1b49.mp4?token=qC7IEnUV_ikgewB3PjZXotyvmc5rVOi2aZ-_ivfv4acsVhhkjYjFSVYVsH5ji_RtoF_-rNWDmsCv3gP89xZ19MJfnvziGE2ffRehfeK_kXHdPPzMmo7ABmd7RXKQIk4paRt8i3MvDGyx89pY-cVidlHPvWxgjwIQpYtEA5le5NG2YaMSDCXiiEddnE5a-3oX9uAqdgkkBc5-9JluxM_iseOHknN3TEBXTvEk8DLJy1Thx0K3VsEkW_RNneVStu73ZSBjtgEMT-RDGro2yM5YIVI_CjxOi3PxO_mVGkRsB-nUXoqS5r9NyEYQ4A23Cy-UmFdrU5FW0O0oCZC90wdA6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود ترامپ به فرودگاه اویان
🔹
دونالد ترامپ، رئیس جمهور آمریکا وارد فرودگاه اویان محل برگزاری نشست جی۷ شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659838" target="_blank">📅 18:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659837">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
گستاخی رژیم صهیونیستی؛ عملیات‌ها متوقف نشده و تنها کاهش یافته است
ادعای شبکه ۱۲ رژیم صهیونیستی:
🔹
دامنه عملیات‌های ارتش متجاوز صهیونیستی در جنوب لبنان به‌طور قابل‌توجهی کاهش یافته است.
🔹
این تغییر رویکرد نظامی در حالی صورت می‌گیرد که فرماندهان صهیونیستی در انتظار ابلاغ دستورات جدید از سوی سطوح عالی سیاسی این رژیم هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659837" target="_blank">📅 18:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659836">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47c8ee5a78.mp4?token=OEZclFyhfyjYQQ_57a7I5pv3ftJ3S7H3UBkubQ0vU2IxrbosN52ZkBa7bCRiNqFPTgMZfJ-wEta-KNH05fs6AIXUs_cihw_g-yuRsFiBSNFwcEgp37CN1ReyZ5j2GAjkAF4EEb2gVzuDb2Ahm34DEFwUnDLS1A9oOqORyHIEzxs4h7AkHG8Q7O4HoSeDKFC-zum9G5PiHYNbRNg8S2NvTRXTYzQdhb0T4JnXjGZW4dFr6N_IIFg0iwSXWqnPImIIzMzMp9nz8RtdFm7-NXsgfxrOmWffOiXxphdyC4EOflbchEhbzv1-RNbN8PLWRbWi7KrzylWMUmfWwBB_udK0xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47c8ee5a78.mp4?token=OEZclFyhfyjYQQ_57a7I5pv3ftJ3S7H3UBkubQ0vU2IxrbosN52ZkBa7bCRiNqFPTgMZfJ-wEta-KNH05fs6AIXUs_cihw_g-yuRsFiBSNFwcEgp37CN1ReyZ5j2GAjkAF4EEb2gVzuDb2Ahm34DEFwUnDLS1A9oOqORyHIEzxs4h7AkHG8Q7O4HoSeDKFC-zum9G5PiHYNbRNg8S2NvTRXTYzQdhb0T4JnXjGZW4dFr6N_IIFg0iwSXWqnPImIIzMzMp9nz8RtdFm7-NXsgfxrOmWffOiXxphdyC4EOflbchEhbzv1-RNbN8PLWRbWi7KrzylWMUmfWwBB_udK0xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هدف ما این است که دانش‌آموزان در کنار آموزش تئوری، ‌ایده‌های خود را هم به صورت عملی پیاده کنند
سجاد محمد علی نژاد معاون مالی و اقتصادی شهردار تهران در مراسم رونمایی از لابراتوار سیار خلاقیت و ساخت:
🔹
هدف از راه‌اندازی لابراتوارهای سیار خلاقیت و ساخت، فراهم کردن فرصتی برای دانش‌آموزان است تا فراتر از آموزش‌های تئوریک، ایده‌های خود را به مرحله اجرا برسانند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659836" target="_blank">📅 18:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659835">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwO_aEXmzfrtmg5fv5j9mmq30384JmDxhoBWJfao3BfTtHAG2VCN5opzJ1SjBwbNa6wmKfp70Y3UmLPljqLRutXs1iS_RkiqmJpQbKLIqjR4bY6_P2q9REbKTVA1dxc--2BaBWnZ2AGafpVAHpm8y1jzSIG4zpvhDwxMJQ9ozxgJaquoAaGVhRjql_SyWvYusbl-uTGbCh2hNl_1LNuh3MWXpReJFamtkvV90ZkhvF1WdzgohOCS0jsxhFoGerKo-SN5kqnrRc837SfQH4OWm1W8KVODnLpO5tiVR1OLGh9ZjQTyvFAfPXlpvNbUq6fm9bGBWzC2T58VXn5la9Uatg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین سرانه مصرف آب در جهان مربوط به کدام کشورهاست؟
🔹
ترکمنستان و مونته‌نگرو با اختلاف، بیشترین سرانه مصرف آب جهان را دارند.
🔹
حضور چند کشور آسیایی در این فهرست، الگوی مصرف آب در منطقه را برجسته می‌کند.
🔹
ایران با مصرف سرانه بیش از ۳۶ هزار فوت مکعب، در جمع کشورهای پرمصرف قرار گرفته است.
@amarfact</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659835" target="_blank">📅 18:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659834">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2540562b52.mp4?token=cmCx3qYVOFmWpAJkGrWtukubo3GksHgC_3f25ERNmxtAwhwoevibscjWyuc_aqSOUjX3n63Eo9xknmpKtSvd85ztuJyEPS9r0Le8hGCek4DyfxaJrz61Sq3XBRjGRbxFHc_yUB7aNiinXtbskzZMnuqxYoeYvLqy-XUyfWYNip7YTOpFGenePl2Pz7Umh9LOU4fBHN5ccJn5zfBVnXMwQ7xIY48RYYkqS2IoyH_OPr1QdI2FUddsuUAI56SHHa11OD7dVQJWua8oFTf_hFX7FAPO7jxtaQ4ov9wywU1Z2nVfGb1LMSb2pUbcPPxi09M5Tgv3Q9GZMBOio00DJ7OF0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2540562b52.mp4?token=cmCx3qYVOFmWpAJkGrWtukubo3GksHgC_3f25ERNmxtAwhwoevibscjWyuc_aqSOUjX3n63Eo9xknmpKtSvd85ztuJyEPS9r0Le8hGCek4DyfxaJrz61Sq3XBRjGRbxFHc_yUB7aNiinXtbskzZMnuqxYoeYvLqy-XUyfWYNip7YTOpFGenePl2Pz7Umh9LOU4fBHN5ccJn5zfBVnXMwQ7xIY48RYYkqS2IoyH_OPr1QdI2FUddsuUAI56SHHa11OD7dVQJWua8oFTf_hFX7FAPO7jxtaQ4ov9wywU1Z2nVfGb1LMSb2pUbcPPxi09M5Tgv3Q9GZMBOio00DJ7OF0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط بمب افکن توپولوف ۲۲ روسیه
🔹
روزنامه سان از سقوط یک فروند بمب‌افکن دوربرد فرا صوت توپولوف ۲۲ ام ۳ روسیه در مزرعه‌ای در ایرکوتسک خبر داد.
🔹
علت این حادثه هنوز اعلام نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659834" target="_blank">📅 18:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659833">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7b04b313e.mp4?token=ndD9PZlfdDuZ1hEgCqAICfukw0KVl_7yTTaQ1J9L4ll4rx0rm_O-dwA1mIHFo1PdDN07siEipYo6oMyeT7nedRBabjwSCXkXk0HCUun2iitEnqdqDNGzQBq3wO2Ax-TBMFxmvx5CpFcYxlisEXRJCcmYtWTrj3vV8lej6ZHE_tlzO0_r0p-6DfEndRbtUuuaMICCjZMfk3au6WY2g9jHHVJMSIzC_IR-5aZVCPMveGfKDrzpoZSluZlenoVa95JFXVwYtdu97_TVCHli0WR4HB-PLoyOewJ49HyMJ8jWNph93fdoGXMwmbgq05Y8HRbR-NIyZeXNjFQGL3y0h3kC6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7b04b313e.mp4?token=ndD9PZlfdDuZ1hEgCqAICfukw0KVl_7yTTaQ1J9L4ll4rx0rm_O-dwA1mIHFo1PdDN07siEipYo6oMyeT7nedRBabjwSCXkXk0HCUun2iitEnqdqDNGzQBq3wO2Ax-TBMFxmvx5CpFcYxlisEXRJCcmYtWTrj3vV8lej6ZHE_tlzO0_r0p-6DfEndRbtUuuaMICCjZMfk3au6WY2g9jHHVJMSIzC_IR-5aZVCPMveGfKDrzpoZSluZlenoVa95JFXVwYtdu97_TVCHli0WR4HB-PLoyOewJ49HyMJ8jWNph93fdoGXMwmbgq05Y8HRbR-NIyZeXNjFQGL3y0h3kC6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در خیمه حسینیم، خونخواه و جانفداییم...
‌
🔹
نصب کتیبه ایوان طلای صحن آزادی
به مناسبت فرارسیدن ماه محرم
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659833" target="_blank">📅 18:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659832">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDar18uuT2YD0SYe3ofuj3wJLdPyZP2wovngs8N2uQDpDUGtwSTUgBjtljw8u65bj2CdMtatWc577LoRVnIFAzZ_i_pNyb-4W_2vVx73-ZM0Tq_noy199q4IwpzAH_f1mONyfcT_CcDtnD5UZWbmHzx84cbmTJVfucbuoiTTbIOW3uuIfmFC5IFPcQhAsZjnGO0U8_s7N5iFqb6powE6-5MB9uO5pE6gPwq11JGwuNnZJi5lLHbYo3xPi5WgShgf3x8orGfeYLRFOEpa2IJr1aKlcvou9ZCWYJas3FpOXzSx9E2WWEQ_Ql8FCmXzLTFUtmtuq6HhAJRIi4VhtIeCzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری کمتر دیده‌شده از رهبر انقلاب اسلامی حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای
🔹
عکاس: علیرضا فراهانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659832" target="_blank">📅 18:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659831">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
پزشکیان: تیم مذاکره‌کننده به هیچ‌وجه از سیاست‌های تعیین‌شده از سوی رهبری عدول نخواهد کرد
رئیس‌جمهور:
🔹
پیروزی دیپلماتیک اخیر، سند افتخار ملت ایران در برابر زورگویان جهان است.
🔹
سرمایه اجتماعی و همراهی مردم بزرگ‌ترین پشتوانه امنیت و پیشرفت کشور است.
🔹
هرچه انسجام داخلی بیشتر باشد، قدرت دفاع از حقوق ملت در مذاکرات افزایش می‌یابد.
🔹
آینده ایران در گرو هم‌افزایی همه ارکان حاکمیت و بهره‌گیری از ظرفیت‌های مردمی است و هیچ قدرتی نمی‌تواند در برابر ملتی متحد و همدل ایستادگی کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659831" target="_blank">📅 18:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659830">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
گزارش‌ها از وقوع حادثه دریایی در سواحل یمن
🔹
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع یک حادثه امنیتی در آب‌های نزدیک به یمن و هدف قرار گرفتن یک نفتکش خبر داد.
🔹
بر اساس گزارش مرکز عملیات تجارت دریایی بریتانیا، یک قایق کوچک با چهار سرنشین مسلح به این نفتکش نزدیک شده‌اند.
🔹
سرنشینان این قایق در جریان این حادثه، با استفاده از پرتابگر آرپی‌جی به سمت کشتی شلیک کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659830" target="_blank">📅 18:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659829">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
پهپاد اسرائیلی یک خودرو را در جنوب لبنان هدف قرار داد که طی آن راننده خودرو به شهادت رسید
🔹
این نخستین حمله مرگبار اسرائیل به لبنان از زمان اعلام توافق آتش‌بس بین ایران و آمریکاست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659829" target="_blank">📅 18:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659828">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e249466fd7.mp4?token=a8Ii9vllzJxne0DfNhbFc8ouzqlm2l_4UpPzioG2pVfUUoA51vFPTI596rtU9J7t-SzgKoGW2R5K5yFaGslj5t4pEf-7K98uga3bz4YrzDlB4r_NMuzVWA4_R0anIU_4PWhtnmQHH1V6cojdOd14BZZo4TA2Ip6hB73sTCgdus7GCk1sw3nY8FffubVfKHb7QDxJn71mvK_c0P9TtFLpWE0R3pmfAH2cMWhcftYJQPLAdwUwfLii04dyQFHekz6rS2Wi21yE_0znpWZbqLh33p4iMqJl-REdw3Cfpt192kgIC-Q4VcJa85uFKfW9eXfmj28O9zj3oX4_KFgWLWQXYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e249466fd7.mp4?token=a8Ii9vllzJxne0DfNhbFc8ouzqlm2l_4UpPzioG2pVfUUoA51vFPTI596rtU9J7t-SzgKoGW2R5K5yFaGslj5t4pEf-7K98uga3bz4YrzDlB4r_NMuzVWA4_R0anIU_4PWhtnmQHH1V6cojdOd14BZZo4TA2Ip6hB73sTCgdus7GCk1sw3nY8FffubVfKHb7QDxJn71mvK_c0P9TtFLpWE0R3pmfAH2cMWhcftYJQPLAdwUwfLii04dyQFHekz6rS2Wi21yE_0znpWZbqLh33p4iMqJl-REdw3Cfpt192kgIC-Q4VcJa85uFKfW9eXfmj28O9zj3oX4_KFgWLWQXYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا پایان تابستان، تعداد لابراتوارها را به ۱۰ مورد می‌رسانیم
سجاد محمد علی نژاد معاون مالی و اقتصادی شهردار تهران در مراسم رونمایی از لابراتوار سیار خلاقیت و ساخت:
🔹
این لابراتوارهای سیار برای گروه‌های سنی مختلف، از دانش‌آموزان هفت‌ساله تا مقطع دبیرستان، طراحی شده‌اند و با توجه به میزان استقبال و نیاز مناطق مختلف، به‌ویژه در جنوب تهران، خدمات آموزشی و مهارتی خود را گسترش خواهند داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659828" target="_blank">📅 18:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659827">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txuoEBBGh33YN_yVGuvjPBOw-97pTz2_5EV1vRYENk3SXGfcMcCuHAOpfoM7SOf9dUxkjMEIAHUCqvIty9zghGyarhkk9ocusizcsMbqbvkkM4rZelafIRndzrYPAmuc4EaXoHzpZuncRIL5x1EXn5uZPm2gEO7gxE5b66m_GGUjZ-M4_juEJZxMAuR5EIwAZtcYYgwy_uCdFc0tW_HpK7OJObESDEvEErVMpDI6eWaZ8fwmOSFtG8V25MW0Pj6EbDnXkS7D9jtyYm97frp176QkT4dLv8FJIRCvPxCd3gNkSVqLugHy6Ss-VzNUAqHf3L6B0s_YFnikjXyldjSLtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابن مسکویه؛ دانشمندی که در غرب شناخته‌شده‌تر است
🔹
شاید همه ما اسم ابن‌سینا را شنیده باشیم؛ اما کمتر کسی ابن مسکویه را می‌شناسد. فیلسوفی که اندیشه‌هایش درباره اخلاق همچنان تازه است و در تاریخ‌نگاری نیز جزو نخستین تاریخ‌نگارانی است که تاریخ را نه براساس…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659827" target="_blank">📅 18:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659826">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
حمله انتحاری به یکی از پادگان‌های وزارت کشور سوریه
🔹
وزارت کشور سوریه از وقوع یک حمله انتحاری به یکی از پادگان‌های وابسته به این وزارتخانه در استان رقه خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659826" target="_blank">📅 18:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659825">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
شرط‌گذاری جدید معاون ترامپ برای توافق با ایران
ادعای جی‌دی ونس، در گفتگو با شبکه سی‌بی‌اس:
🔹
واشنگتن تنها در صورتی آماده تغییر رویکرد است که ایران تعهد عملی خود را با ایجاد «مکانیسم‌های راستی‌آزمایی» برای کنار گذاشتن کامل برنامه تسلیحات هسته‌ای اثبات کند.
🔹
فرآیند توافق باید «ابتدا با بازرسی‌های دقیق و سپس پایان دادن به برنامه هسته‌ای» آغاز شود. موضوع آزادسازی منابع مالی مسدود شده ایران، تنها پس از طی شدن این مراحل و حصول اطمینان از توقف برنامه هسته‌ای مورد گفتگو قرار خواهد گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659825" target="_blank">📅 18:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659824">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8935d8f26.mp4?token=KJsUPULUt5PbKRGNrBXAlS7R5SCsBlRbCx8oqmkrzmCVpuQYl-Hf6aIKM3ukq0VchEK0fOK7pVupWt6TPRnz_wZugDmndFfM6ofzWpVGNm7SFYFTAI9F-G6T8qcXvPTqkhBmwxkLbdhZEf6rYPPdKONL9lZeccXvoyi2PEsppmgRfUEoIA4ALKHFdBlZu6sliHZ1wPWfvW8mvaQWnYriQ5g1kXYHDdOl2D_pw8olZNIijzx3K6EpPjU1Gy73Y-gPMLhTPyj7kPxwAephcgWcIid42-_8iEP91RoQpB6mz-KDSUft9EJjQ285aDh5YTnqNU8qsDdnHmvZkP1I15gi5KhQnnQml5NrmmFZV1xE7BaTj0sf03o8R-5UoLFt-B6E6KF9zpcd5ztpl6rVLpARMeQSCuIeu8YJqWcQihWHl0M13UX_vB8jL6ag5jCk6AtUMPtwf-hlfwsAzrxuzGNQW_9qKUplB4hC7HFtFLcx7tWIsVKMKO1V6uVp2CN8xhiR407-SaTBfuM8__OFbXOodUt2rGgqIgr3HyQ2ijTdWJf2oIzz74ATPWURzoJ3mzyE7J68Ll9QePYBu4GstLYbGsg1k2H0Xb8WUR1X1LngwyG0yznNFKEioBiLJzuioHjoMAY-M8Aa5w_CHKD51XzDjwfYG8xRmLXca1g1uKs70d8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8935d8f26.mp4?token=KJsUPULUt5PbKRGNrBXAlS7R5SCsBlRbCx8oqmkrzmCVpuQYl-Hf6aIKM3ukq0VchEK0fOK7pVupWt6TPRnz_wZugDmndFfM6ofzWpVGNm7SFYFTAI9F-G6T8qcXvPTqkhBmwxkLbdhZEf6rYPPdKONL9lZeccXvoyi2PEsppmgRfUEoIA4ALKHFdBlZu6sliHZ1wPWfvW8mvaQWnYriQ5g1kXYHDdOl2D_pw8olZNIijzx3K6EpPjU1Gy73Y-gPMLhTPyj7kPxwAephcgWcIid42-_8iEP91RoQpB6mz-KDSUft9EJjQ285aDh5YTnqNU8qsDdnHmvZkP1I15gi5KhQnnQml5NrmmFZV1xE7BaTj0sf03o8R-5UoLFt-B6E6KF9zpcd5ztpl6rVLpARMeQSCuIeu8YJqWcQihWHl0M13UX_vB8jL6ag5jCk6AtUMPtwf-hlfwsAzrxuzGNQW_9qKUplB4hC7HFtFLcx7tWIsVKMKO1V6uVp2CN8xhiR407-SaTBfuM8__OFbXOodUt2rGgqIgr3HyQ2ijTdWJf2oIzz74ATPWURzoJ3mzyE7J68Ll9QePYBu4GstLYbGsg1k2H0Xb8WUR1X1LngwyG0yznNFKEioBiLJzuioHjoMAY-M8Aa5w_CHKD51XzDjwfYG8xRmLXca1g1uKs70d8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمد علی نژاد
:
در لابراتوار سیار خلاقیت و ساخت، ایده‌های مفهومی شرکت‌های دانش‌بنیان نوپا را به محصول صنعتی تبدیل می‌کنیم
سجاد محمد علی نژاد معاون مالی و اقتصادی شهردار تهران در مراسم رونمایی از لابراتوار سیار خلاقیت و ساخت:
🔹
در این مراکز، به کارآفرینان و شرکت‌های نوپای دانش‌بنیان تهران کمک می‌کنیم تا ایده‌های خود را از مرحله مفهومی و نرم‌افزاری به محصول صنعتی تبدیل کنند.
🔹
ضروری است که کودکان، دانش‌آموزان و دانشجویان ما از مهارت‌ها و ظرفیت‌های ویژه برخوردار باشند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/659824" target="_blank">📅 18:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659823">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ارتش آمریکا: محاصره بنادر ایران تا روز جمعه همچنان ادامه دارد
ارتش آمریکا:
🔹
محاصره بنادر ایران همچنان ادامه داشته و در انتظار تکمیل تفاهم‌نامه‌ای که قرار است روز جمعه با ایران حاصل شود.
🔹
ارتش آمریکا همچنین از تمامی کشتی‌هایی که در طول مدت محاصره بنادر ایران آسیب دیده‌اند خواست تا زمان دستورات بعدی، هیچ‌گونه حرکتی نکنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659823" target="_blank">📅 18:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659821">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ادعای ونس از روایت‌های رسانه‌های ایران از تفاهم‌نامه
معاون ترامپ:
🔹
رسانه‌های ایران درباره دستاوردهای ایران صحبت خواهند کرد بدون اینکه بگویند که تهران چه امتیازاتی واگذار کرده است. برای همه ما مهم است که این رویه را اصلاح کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/659821" target="_blank">📅 17:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659820">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ادعای ونس در مورد توافق
🔹
سی‌بی‌اس: ایرانی‌ها می‌گویند که به یک صندوق بازسازی ۳۰۰ میلیارد دلاری دسترسی پیدا خواهند کرد. درست است یا نادرست؟
🔹
جی‌دی ونس: این از آن دست چیزهایی است که آن‌ها می‌توانند به آن دسترسی داشته باشند، به شرطی که به تعهدات خود پایبند باشند./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/659820" target="_blank">📅 17:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659819">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ترامپ وارد ژنو شد
🔹
ترامپ پیش از عزیمت به فرانسه برای شرکت در اجلاس گروه هفت، وارد ژنو شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/659819" target="_blank">📅 17:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659818">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1c6103bc1.mp4?token=INJ-PsTCQfnIy-xe6aVLhdICEPt5iQ6M1D4sW0qJcEloFqD4GZM3Pw3Lux-0wymmC0wanpGxrrT2LvpfYL-O_n0wGPM4_NpTMLm9KxUf2Z_Php6qwOvdE9cDUlYDzg_8TcD2OT-JK4DYvPxU2YVmr5DdhW7KrNlHeCWjkDwYyKhw-dpaguwgZdD-FMC-0YukyIjaBG9WiFSo59YA_Bdfa8L2eBDurL5KQ2pWBuAiG8rmMTjCVr0nYeNTDSvHYl8wBwl3lgnRvC-EEimxlbujV5IWPgY0LfuqK4u7MpO-zduDGSTSR783fXoNmpLkjavG289y-6fqzrUM4uzS1JG53A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1c6103bc1.mp4?token=INJ-PsTCQfnIy-xe6aVLhdICEPt5iQ6M1D4sW0qJcEloFqD4GZM3Pw3Lux-0wymmC0wanpGxrrT2LvpfYL-O_n0wGPM4_NpTMLm9KxUf2Z_Php6qwOvdE9cDUlYDzg_8TcD2OT-JK4DYvPxU2YVmr5DdhW7KrNlHeCWjkDwYyKhw-dpaguwgZdD-FMC-0YukyIjaBG9WiFSo59YA_Bdfa8L2eBDurL5KQ2pWBuAiG8rmMTjCVr0nYeNTDSvHYl8wBwl3lgnRvC-EEimxlbujV5IWPgY0LfuqK4u7MpO-zduDGSTSR783fXoNmpLkjavG289y-6fqzrUM4uzS1JG53A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس پارک علم و فناوری تهران
:
هدف از افتتاح این فب لب‌ها کمک به نخبگانی است که ایده دارند ولی امکانات اجرای ایده خود را ندارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/659818" target="_blank">📅 17:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659817">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
پزشکیان: اگر همۀ مفاد تفاهم‌نامه به‌درستی عملیاتی شود، به‌عنوان سندی افتخارآمیز برای کشور تلقی می‌شود
رئیس جمهور:
🔹
اجرای کامل این تفاهم‌نامه می‌تواند بسیاری از مسائل را برطرف کند و شرایط تازه‌ای را در ایران و منطقه رقم بزند. این تفاهم‌نامه نه‌تنها برای داخل کشور، بلکه برای کل منطقه و نیروهای مقاومت نیز افتخاری بزرگ به شمار می‌رود. جزئیات آن نیز ان‌شاءالله در زمان مناسب ارائه خواهد شد.
🔹
لازم می‌دانم از اعضای تیم مذاکره‌کننده تشکر کنم؛ از آقای قالیباف که زحمات زیادی کشیدند، از آقای عراقچی و همچنین از اعضای شورای‌عالی امنیت ملی و همۀ کسانی که در این مسیر نقش‌آفرینی کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/659817" target="_blank">📅 17:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659810">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JP5sHYoCBttjdqwdLdP-VSfMUbBZoV-IRkqJTPRARR6ncOKS8Qs4UtOSt6xTUnoASa3bIniNbkGhLH8K_68KNAO2OugLZXYlE3U4vMuHaT1PR0bb5wpcRx5wJIhd_6crSGLvKBN6UtAfDSpS87Kygun1JPr8Uv33-BSmw1HcwnQQ4v0kS9axYAN9et-bTwCXE0PbUGLPKp8owznQib9JqPS5EE5zaJvmrWKE0pNH3WvQXoJ2eWcUlManLuzgfM_nHtWPHg4mkt_XcM8jtVV6BdAWmD1I-250050ugBOO1ebvt3W0xLGkjYoBx7qnd7rE3yryuBXPgJh07DHHK5MfIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fddyIW6-gGPqrXJakMnSDjMLZ1Wc4TrTI21hjW6jujbSGBMDmyN1O1OdL3yH4MIxJGut5lXD3p5_azFXThWXnN5V4v_EhHnwwaXMKAibPi-ExZcyrkK7oBgf8TGbPMN-NrXeMG-fZEdIjcruGDA1wcrDYw-KHTsuphxGZOJ8bXSRV8S-slkVbywENxtl1B_8YckBqjQ5EeUQ_FVBFqzOxUMwtuG3ptuGpNxjqxjrR67dq_4QGxdJHjcon3wixnXxdc5lAQuVG-lNueAiK0n0S4-t8ENyNhpEyVwz9OLtCLjXI7zH2XlDth5XHGMqLbsCPiF9cgXOnQr7RTx1JnduxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rgn5m90v7X8jTUT91h6tRM29H1rGlegFvqRMeWLLEKPFOK0jjIpZtfTE9iVtobv6KmoTAJS4Rmz1qz526Z4UU6SGp9BtTWfk0xEcqiw9GQzJ7Mnb__5_KHhEVQjlFnC0NvN6gTVr1oonlDMSFDS7V9jdcJZKslFXffZ5mSd8_TyCc4EwzwM8vQf7Hbo3H_z5uSi29h63Fz1w-5TdeCb1yky73lnK_wdojgeqEqLngP9rClumt59GSIh1DrAi1m6bXYEMunjbJIIIjRMSIAIZNRx87OcpfAogrCApgKH9MUWGMGKYY-n1vqepdwLn7tLUIhZeeJbH3DF2aIk2Kdf_Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EmvtiigU6JJ5AbEJqS7oZ7ZnrEPTLjOQPmZB4fdUGkyFtl2-A06R7SNLaU9OYQ8_xDomiqKXF9IpmKCtwUP5nAzAEvPpoSFLDUUlalK3VEM832a6retdXqvgCDeCJNIk3LAW_9eqSmlIsAjzRPdZwdlspLWTZaoXOWPm02uaG7yPACICv7-OX9bUaMpVm4ygXEqEM_e7LAWBZOW5VpYvYA1Zxo7aciUMm2-weartVHYf5yCeCNd7XkmxHcaWKcFoLTLx7xJixypiQ2__bQDBaElMYeX-l1QuWKyT_qY9ZM7KQ0FwwPHbYBk0tQXcv-HFPPy4TOO6BxFpa8UT0Z8mTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IOCvKtx5GbuuKvfF4cyEZxwNPFy9DPHtF8BIXmX7h4yINgIG41za99NEk4LYLMkeWgrdOjS-TDg2d0P629dTCzXzB6FcuHw2_8Rvx2zFleLUQZPzYosgA4h53BfKvjUnJUx4u243qeM-t3XU6eXHxve5xNO-VDYU8WS0df7R1hpyVMXgKB42NMRyclScRBV8qqqPY8TJKBeBllgPmFUJZ1KBfGKuJ9hZyIcTvqEVhADLnPDq_JH6tDMMJ2a45bArMFNDkpotVD2Qh6joIElfHsmfWrnaePWvuC2JQ3HD-nhSVLkKO8T67pv_0wsvNv9mWnYmCrZVz4bOmPrUGEPCTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2ZbiRMHbb__JUmUboJejH2oGD7EHhcoUvedB09y7vwLpTn1WK_SE6REtBd3PAVkIAnmnXC2iPuCJHJoS844ffjbP9UgASZdZIKfc63b_Q2M0cYIlKr2enlxGWirjxdNh2zTWVHQZ3T0FUz9AduOIXfhIftEyTsZPFvarTm5vMYx6wS0yTacvZVsi0v6gfHeVooVhoSejQclF306ilJoJmQmc0t4P_ZGNBJyXR_cnpNNdNZTXr9kfKjp5edmHw1nvSaIeX-LhcSIg7CvxNfBo8kpWPZ8ng00nuik6UDouUBImDxSM14oR1Lp4affUluXn2deWuDC71GCHWeenYq9Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K_JafVKfu6fSDXVu1yCa0vbhI2YuuY2v2fA9gvd4GlOrPuUKOD0c9p8e11YG7H2hvzVXhKTIicnu_xexLsXkS4hRgjZSVZLSkGld521WlgdUMWkuugrHKzWRDF_tXkeTRt164gG2zDRShPpXTDFmVrDjkvwhz93ZD-QHcaFgHw5yY30A1RRWDrMFDvz7gmMwvxWN-caVj77XHk6hx83naHWgUfF4_izyipvCyw79DrAXztvU462dQnvRk3GUQuBfRNyZYnKN-gxfC4eDFYpzX2RQi6MNVAD-pyp3i4N9W7hgC63UT9JE2ECWF-S_yXiR60HdBHY4AUrZ6DhKxkfo2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تأکید فعالان اقتصاد دیجیتال بر تاب‌آوری، ماندن و حفظ سرمایه انسانی
🔹
در همایش «نقطه تصمیم»، مدیران و فعالان اقتصاد دیجیتال با تأکید بر افزایش عدم قطعیت در فضای کسب‌وکار، «تاب‌آوری سازمانی»، «یادگیری مستمر» و «سیستم‌سازی» را مهم‌ترین راهکارهای عبور از بحران‌ها دانستند.
🔹
سخنرانان همچنین بر لزوم بهره‌گیری از فرصت‌های نهفته در تهدیدها، ارتقای پایداری زیرساخت‌ها و سازگاری با تحولات ناشی از هوش مصنوعی برای حفظ رشد و تداوم فعالیت کسب‌وکارها تأکید کردند.
🔹
حاضران در این پنل، «حفظ سرمایه انسانی» را مهم‌ترین سرمایه شرکت‌ها در شرایط بحرانی عنوان کردند و همراهی کارکنان را عامل اصلی عبور از چالش‌ها دانستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/659810" target="_blank">📅 17:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659809">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrP7QUex1wVGYGCviWdUuqHIOXL5n4-MrewdLRkZhMiotplExhh2lGcAaGbBavnuxXnvzoqh1HpUnqjHPsiIimRSvo5j5Kh0H8SCogSTepwlVuo76I7y7p3YOe-IbQ5SFM4UC8FTjiVE7aVlSy5K3u9GaqZDpQA9QS2w4AwOKBY-_BKNyhsqR4pDri5pHpZK1D4LMZP_aNUCJiVgaIleSXfvIepL4it-Wp71VmZRIkt_dmfhIUd35PIc5hw6VpgFg-nB9oSdpd5I-Misd4znIr-HrOJIBq2kjjPbNGzmhwBizqS41Vg4i9UZdCLx1OC90Tvr9Rr3AyY9noI3pmwpCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری سردار آزمون و آرزوی موفقیت برای تیم‌ ملی ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/659809" target="_blank">📅 17:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659808">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
افزایش سقف وام ودیعه مسکن؛ پرداخت تسهیلات به ۳۸۴ هزار خانوار
مدیرکل دفتر برنامه‌ریزی معاونت مسکن و ساختمان:
🔹
سهمیه تسهیلات ودیعه مسکن از ۲۰۰ به ۳۰۰ هزار میلیارد تومان رسید. سقف این تسهیلات در تهران به ۳۶۵ میلیون تومان رسیده و تاکنون به ۳۸۴ هزار خانوار وام ودیعه پرداخت شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/659808" target="_blank">📅 17:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659807">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/659807" target="_blank">📅 17:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659806">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NU8axL0isyTZFFqEVSyT5tL316UZ7xM6CKmkMmX-AR_QNufyopzt2vIvxVWBO_QECmSqsmqoJO2pfcw_KdUgufCqLTiq9iGdhiVpOe001xSCliXeYmDV6BN3Qrr4Udqer1NZhyk6Mvw-ieaiIlhAQ0ABd4dVFWOxdo3MlNJZi4vmPSjtUAu16Gq-nQwU2qvNpfb4sWlcV0CCvTA1mFGi78agdcLVf-4by-VuaITS5IZVydKgUvFZkkR8hQx0AUggwWCRi37SRL6H7O83fXv8lvIfG4qcbGJWMSHtWtIOugYkczAX17wXkHU4OThTOe8XkP4WZ6Q5QDwbp8T1DqfwwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه Haaretz: ایران به بقا قانع نیست و در پی تبدیل شدن به یک قدرت بزرگ است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/659806" target="_blank">📅 17:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659805">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsuYIDh889BUh3vR9K-EL8sh7TeiaoS4-6BqaLAoij0GG2iyIstgCfkRe_RnHjLLCCGym7AoJ2w3hGDvoxyJJ4JwuTdUoXehy7Iq_8Z0KOhG0CacryYAYTgCfQQLS9nc0LiQlNdyIlixQ0t-Nrjd4M34DNKF6m1qNRtQNU5sSnjOzgdYcjZR7_amuqxrecQdHhqMG-BIn1OHWQVqibSNBy9rkWFU1_EpXsKrEnE4Oou-PD4B17_OVVV0lGoJzJIi2tL8hEUGinlJdcARokoUegf8RjayjnBqAzPFs0i8ZXy_areRYExnzaTCsxg31IZeMTz1AMvQxSOPi3-SsdvAlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعضی تصمیم‌های مهم در تاریخ کشورها نه در میدان نبرد، بلکه در عرصه مسئولیت و تدبیر گرفته می‌شوند
محسن بیگلربیگی نوشت:
🔹
آیت‌الله سید مجتبی حسینی خامنه‌ای در مدت کوتاهی فقدان شماری از نزدیک‌ترین اعضای خانواده خود را تجربه کرد؛ رخدادهایی که برای هر انسانی می‌تواند با اندوه، خشم و احساسات عمیق همراه باشد. با این حال، مسئولیت‌های بزرگ گاهی انسان را در برابر انتخابی دشوار قرار می‌دهد؛ انتخاب میان احساسات شخصی و مصالح عمومی.
🔹
بزرگی رهبران را تنها نباید در تصمیم‌های سخت، بلکه در توانایی آنان برای ترجیح منافع ملی بر ملاحظات فردی جست‌وجو کرد. در چنین شرایطی، آنچه اهمیت می‌یابد حفظ امنیت، ثبات، رفاه مردم و آینده کشور است.
🔹
اگر توافقی با هدف تأمین منافع ملی، کاهش هزینه‌ها و آسیب‌های احتمالی برای مردم و گشودن مسیرهای جدید برای پیشرفت ایران پذیرفته شود، می‌توان آن را نشانه‌ای از تقدم مصالح کشور بر احساسات و ملاحظات شخصی دانست.
🔹
تاریخ نشان داده است که ماندگاری کشورها بیش از هر چیز در گرو تصمیم‌هایی است که با نگاه به آینده و منافع عمومی اتخاذ می‌شوند. شاید مهم‌ترین آزمون یک رهبر نیز همین باشد که در لحظات دشوار، آنچه را برای کشور مفیدتر است بر هر ملاحظه دیگری ترجیح دهد.
🔹
ایران امروز بیش از هر زمان دیگری به همدلی، عقلانیت، تلاش و نگاه رو به آینده نیاز دارد. پاسداشت یاد همه شهیدان این سرزمین نیز زمانی معنا می‌یابد که در مسیر ساختن ایرانی قوی‌تر، آباد و امن‌تر گام برداریم.
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/659805" target="_blank">📅 17:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659804">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
ادعای جی‌دی ونس درباره ایران: ما دیروز به صورت دیجیتالی توافق را امضا کردیم
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/659804" target="_blank">📅 17:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659803">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0df0d20618.mp4?token=aSO7zwVfLFthgdry4i1N62fFSSK43h0QSnb7ZpW33RP1tGg3dZF7T8bBwcrXErz3bqm28WVbRBsRaMFm8VfM_payKG35o0xb1BPPUQdr8uiCHNxp-Wm3HszYrZD6IaXuri6I5ziIUqklzow8JlFnue_WgLRHx0Trmvl1aINZjcjTwIqzBmcYkomD6vZI8cWdbnoqFt_zQsCf3D_m-qZytXWDa5jOx4Fn7HBTV_9J7rL5zl2ES0kcwYMDYb6d1J6H-vQ45o3cZXYHC0HMkO9KpDNR7iBX6fRQSML_G0GJ4g4jj3taDx7or1s7NeNb4exduqUYtwwkphRmC0159xIA4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0df0d20618.mp4?token=aSO7zwVfLFthgdry4i1N62fFSSK43h0QSnb7ZpW33RP1tGg3dZF7T8bBwcrXErz3bqm28WVbRBsRaMFm8VfM_payKG35o0xb1BPPUQdr8uiCHNxp-Wm3HszYrZD6IaXuri6I5ziIUqklzow8JlFnue_WgLRHx0Trmvl1aINZjcjTwIqzBmcYkomD6vZI8cWdbnoqFt_zQsCf3D_m-qZytXWDa5jOx4Fn7HBTV_9J7rL5zl2ES0kcwYMDYb6d1J6H-vQ45o3cZXYHC0HMkO9KpDNR7iBX6fRQSML_G0GJ4g4jj3taDx7or1s7NeNb4exduqUYtwwkphRmC0159xIA4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفند طلایی برای آبیاری گیاهان
🔹
این روش یکی از بهترین راه‌ها برای زمانی است که ۳ تا ۷ روز در خانه نیستید، چون گیاه به اندازه نیازش آب مصرف می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/659803" target="_blank">📅 17:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659802">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cf2518627.mp4?token=TGNWW8aOJ7zQlng_LW975m9sP9QR1qJCoCcaQbvZsVimzLXrSUdH813CFBIeNgB4IW_XWsgLmb2TATUx4ywayy4EZw57g2535AMhCHZyWIqCP_7LEo9LhCW8Q7TSAXRYM4DtWXLDkwVDt3f8N1gOM4SMwote6oOPsiFxpj8SQK2ZEYP545tvPJyGx8FuiDAjwkHvAH6HbZEEuzCG73ylCe76Ddh3FLuFBTXKK8Il2hDOZbft10tpsChznfRwXBn_EU0RwJ-hi8j_A26FVHP-kV7_lkwyJnBS1j_YVg0HMgFlEUDXCkSYTf4Zl6muxFHfkaml4LoA4XFrrNhQ_zimtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cf2518627.mp4?token=TGNWW8aOJ7zQlng_LW975m9sP9QR1qJCoCcaQbvZsVimzLXrSUdH813CFBIeNgB4IW_XWsgLmb2TATUx4ywayy4EZw57g2535AMhCHZyWIqCP_7LEo9LhCW8Q7TSAXRYM4DtWXLDkwVDt3f8N1gOM4SMwote6oOPsiFxpj8SQK2ZEYP545tvPJyGx8FuiDAjwkHvAH6HbZEEuzCG73ylCe76Ddh3FLuFBTXKK8Il2hDOZbft10tpsChznfRwXBn_EU0RwJ-hi8j_A26FVHP-kV7_lkwyJnBS1j_YVg0HMgFlEUDXCkSYTf4Zl6muxFHfkaml4LoA4XFrrNhQ_zimtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمد علی نژاد
:
رویکرد ما این است که در تهران زیرساخت‌های حمایت از شرکت‌های دانش‌بنیان نوپا را توسعه دهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/659802" target="_blank">📅 17:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659801">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vR902UCfqCXHF0eB_psQiWp6fQYMgws-rl3RTc-FFS4DBBZdlwdBqOCMnEM8mBaze7CNs-SeheVBjJ6wSCqQv7ZJhgny5ExcM8gZThQOh3YwfKEA_si06vTHvlKI115OqmWVmg9foazz82u855k731IdT4z0bpWuH2dgRnTXk0tyCUOaEExXIT46VQqzKjSwCMzmaRAJQhCtURQk7l6QC4C15TFkKv6wlIs5LMXCnRP9mFQ02pyBcuCAYjJh1JOetyZBdeDaXlTXcr8CUyO8QCU2X2k0xFKU0qy2yMseXTDllhmoIW_JrRQhwSqEMufrgEv4q-bfUsAn3quIcgYkMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام معنادار نخست‌وزیر اسپانیا درباره جنگ ایران
🔹
پدرو سانچز، نخست وزیر اسپانیا، از مردم خواست که هزینه درگیری مسلحانه آمریکا با ایران را فراموش نکنند.
🔹
به گزارش Ukrinform، او نوشت که «بیش از ۷۴۰۰ کشته، که اکثر آنها غیرنظامی بودند. صدها خانه، مدرسه و بیمارستان ویران شد. افزایش گسترده قیمت‌ها و میلیاردها یورو خسارت، به ویژه در اروپا. اینها پیامدهای درگیری در ایران است.»
🔹
نباید فراموش کنیم که جنگ یک اشتباه است و گفتگو و دیپلماسی تنها راه ممکن هستند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/659801" target="_blank">📅 17:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659800">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lii_OPmSrn3QzlaLiZ-2XTVmdNHQVRPS1tMcYt7E3T2Xjw17YG5w-irrEZBxjaF6w4xpyt3dUR1IOTvn51gWYrsc5o6GzqzfO_lNfg-1JJGgtRtPLH9iDkmg55EF-yLiQdENJABEEREXyhKdvlOS40KJxiwvEAX4RzNUztyzknRhtFHI0hLF_LytXyjQ_S8gr9AuxAUR6uWR_NPB-E9WwM31YgkgzuTEvNCacKXKdAgSjPvagg4f-c9C7eG3qdoqz8jUs8JmbZMjm2zab4NP7lfCNDI_8P_nEbRXzOYEtzQV0RlyNKVN81SZCElupfk-vcpaql1-nXiz1UEvYlw2tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«من ایرانم»؛ نسخه «اوج» برای بازگشت مخاطب به تلویزیون
🔹
«من ایرانم» به جای ساخت تصویراسطوره ای و دست نیافتنی از فرماندهان و چهره‌های رسمی، پیش از آنکه با سمت و مسئولیتی دولتی شان از آنان یاد کنند، آن ها را به عنوان عضوی از یک خانواده به مخاطب شناساند با ترس‌ها، دلبستگی‌ها و انتخاب‌های دشواری که داشتند.
🔹
شهیدی‌فر نیز با همان شیوه آشنای خود، بی‌آنکه بخواهد ستاره برنامه باشد، اجازه داد روایت‌ها شنیده شوند. او به جای آنکه احساسات را هدایت کند، به مهمانان فرصت داد خودشان قصه‌شان را تعریف کنند و همین صداقت، مخاطب را با خود همراه کرد.
🔹
در این میان، نقش سازمان اوج که به تولید چنین برنامه‌هایی میدان می‌دهند نیز قابل انکار نیست؛ سرمایه‌گذاری بر روایت‌های انسانی و پرهیز از شعارزدگی، نشان می‌دهد که گاهی اثرگذاری رسانه نه از مسیر پرخرج‌ترین پروژه‌ها، بلکه از دل انتخاب درست سوژه و اعتماد به قصه‌های واقعی به دست می‌آید./ روزپلاس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/659800" target="_blank">📅 17:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659799">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb22ee8c3d.mp4?token=YQthkX5ooRyfqCy43O7FIjJwx_0kgnMnDGuy9N_1EyJpTrrT9IYmPhSj0N_msn65-l4LQ8atfqKlgwMIq2JCFVurfR6kz1eSqBdD96UzpGvwZvfk6wPVyNdG1x-vzxTn7up5bA2vaJE526UijdMQK4FjgNbJL9LtV_nr_I2nmp3dm71-SYpBR_Awk8Atjs2BEZZyHj1I-U56Hmm5r0R0EbVCUhaIU-jb0UWDOzuqWH_6HiO0klQt4Kiqh0ObjD7V4YXcKLXZLrIZkONipOOyLmRFmv4SldJDccwfqQaWHLul0QJ0qKK4z0bAgTL_VvW8Na7gmgB7SnE6SB3nBlMrRjPK5r94d3DMEFAsj3nDz9DI4as0JOYh5UM2VBZrJ_DMMoLIV3gcr4tEBKmBTAx2XIV4HhVTgItNO1NArDKmXhrdK_CyWXsDEokJWqdNYQ9fa0AsdE_kYrGI9C9kBeOyOlkCUL3FuPbK-Ky-7J7_A5DQlrGxgMl-xePRxQ_4YohNNgbGnzY0_nmbMUrXYOUe5VYFxiru4udo-pg_tffNc-dtoQPJUipsn0p0ip8LpKO1u-e4XarEAbavQggValDpX6B6dF6f5i1VEr45PfYfGJXFY-zv-5FjYVE1BRnzcw14XoJwezwQwS_LXAFPOHXdAJkmmU2VZRT_l39eyzSteNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb22ee8c3d.mp4?token=YQthkX5ooRyfqCy43O7FIjJwx_0kgnMnDGuy9N_1EyJpTrrT9IYmPhSj0N_msn65-l4LQ8atfqKlgwMIq2JCFVurfR6kz1eSqBdD96UzpGvwZvfk6wPVyNdG1x-vzxTn7up5bA2vaJE526UijdMQK4FjgNbJL9LtV_nr_I2nmp3dm71-SYpBR_Awk8Atjs2BEZZyHj1I-U56Hmm5r0R0EbVCUhaIU-jb0UWDOzuqWH_6HiO0klQt4Kiqh0ObjD7V4YXcKLXZLrIZkONipOOyLmRFmv4SldJDccwfqQaWHLul0QJ0qKK4z0bAgTL_VvW8Na7gmgB7SnE6SB3nBlMrRjPK5r94d3DMEFAsj3nDz9DI4as0JOYh5UM2VBZrJ_DMMoLIV3gcr4tEBKmBTAx2XIV4HhVTgItNO1NArDKmXhrdK_CyWXsDEokJWqdNYQ9fa0AsdE_kYrGI9C9kBeOyOlkCUL3FuPbK-Ky-7J7_A5DQlrGxgMl-xePRxQ_4YohNNgbGnzY0_nmbMUrXYOUe5VYFxiru4udo-pg_tffNc-dtoQPJUipsn0p0ip8LpKO1u-e4XarEAbavQggValDpX6B6dF6f5i1VEr45PfYfGJXFY-zv-5FjYVE1BRnzcw14XoJwezwQwS_LXAFPOHXdAJkmmU2VZRT_l39eyzSteNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صفحه رسمی جام‌جهانی ۲۰۲۶ با انتشار ویدیوی مهار پنالتی رونالدو توسط بیرانوند به استقبال دیدار تیم ملی کشورمان با نیوزیلند رفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/659799" target="_blank">📅 17:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659798">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9cfcb123f.mp4?token=iP7hiVJgPZMabAXeIl3yPptBPJyJ4y3LkYhpebekJ_nwVzQHvELFQCHnCk0MdZ-zuc1IhtRbF4SWiac9DK1eFh7KNqbUonMBrZFjbwHr6RXptcM1U-zaI4yQm2lQTFBdtlctriTaDyUpc9iOZk81gR5YTtNXq3YiQMev50_ZP-KsnerSEA5p7AF4rv5mRN5V7_t88lfc4yXYVxUg53lIK51-H-0VZM3ycraI_jLOWak0jbeMdMdKM6MyF1wqME_hcsggzlzpcI8CFKNvHakcKA7bPhU4PdTdqOG0euehOcJc62-potv-ZQ-LKI_rR6yZ9n4E7J72f6ZnwykrX-IsYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9cfcb123f.mp4?token=iP7hiVJgPZMabAXeIl3yPptBPJyJ4y3LkYhpebekJ_nwVzQHvELFQCHnCk0MdZ-zuc1IhtRbF4SWiac9DK1eFh7KNqbUonMBrZFjbwHr6RXptcM1U-zaI4yQm2lQTFBdtlctriTaDyUpc9iOZk81gR5YTtNXq3YiQMev50_ZP-KsnerSEA5p7AF4rv5mRN5V7_t88lfc4yXYVxUg53lIK51-H-0VZM3ycraI_jLOWak0jbeMdMdKM6MyF1wqME_hcsggzlzpcI8CFKNvHakcKA7bPhU4PdTdqOG0euehOcJc62-potv-ZQ-LKI_rR6yZ9n4E7J72f6ZnwykrX-IsYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماکرون: ناو فرانسه می‌تواند ظرف ۲ تا ۳ روز آینده در تنگهٔ هرمز مستقر شود؛ البته با هماهنگی
🔹
ما می‌توانیم از همین فردا یک ناو محافظ و ظرف ۲ تا ۳ روز آینده، ناو شارل دوگل، تجهیزات مین‌روبی و ناوهای محافظ شرکایمان و سایر تجهیزات را در منطقه داشته باشیم. اما تمام این اقدامات تنها در صورتی معنا خواهد داشت که یک توافق بین‌المللی وجود داشته باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/659798" target="_blank">📅 17:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659797">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgUqm1iJoPjFhuwJlg5mZixokpEGhBzNwX41VegoupNr1r6vCWmAvXhPNMKbGb3F2OBUPidpdj20wQzf6RhyIkYSTyFvyHywEnQW3n3QZU9663bIGvRAFGJFQn3A8z5uCnH8B9icWMa2fK-PS_buY9BGrmvyu7vqhJdvOmtyLpoMx33CN__i1h0mjgpRMm6LlS_hyXispbH04UNhNeHk8rQifferO61QScYfbpRX94kRhZOnhM-LYSuWJpjHMfIAwkN90UL71Yo2QemjX_xy0HYt26viEz69Nnf5mH3pPD5Ab2WzLi-u4uZ7CTorXKQ83CfqW-nFSmlWY8VpBGXP7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینفوگرافیک/ روایت نقش‌آفرینی بانک صنعت و معدن در توسعه زیرساخت‌های انرژی
🔹
۴۱ طرح نیروگاهی، ۸ هزار مگاوات ظرفیت و سهم ۱۰ درصدی در تولید برق کشور
🔹
بانک صنعت و معدن با ایفای نقشی مؤثر در تأمین مالی پروژه‌های نیروگاهی کشور، از اجرای ۴۱ طرح در حوزه تولید برق حمایت کرده است؛ طرح‌هایی که با ظرفیت ۸ هزار مگاوات، سهمی ۱۰ درصدی در برق تولیدی کشور داشته و گامی مهم در تقویت امنیت انرژی و توسعه زیرساخت‌های صنعت برق به شمار می‌روند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/659797" target="_blank">📅 16:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659796">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
بحرین برای ۱۲ طرفدار ایران ۱۰ سال حبس برید!
🔹
بحرین ۱۲ نفر را به دلیل حمایت از حملات ایران به ۱۰ سال زندان محکوم کرد
🔹
آناتولی گزارش داد که دادگاه عالی جنایی می‌گوید افراد «مرتکب جرایم حمایت، تشویق و تأیید حملات ایران» در بحرین شده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659796" target="_blank">📅 16:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659795">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda12651f0.mp4?token=CrKz5tI3zyGRpqXAE5rvKGMbXNb2twuvy72rnMF3-6G0e0vonVv_NiHDLvtsFBtZcMbAZUhFIqPfJa9TWgx9DcZCc0zWETS1Tl1hV2x5RydaR8WQ5B3TCzKX-9GyhM_yuuGqQGXqAn2OVstt_EqDLE8c6MGma0MXlqhqsyrbNvZ6rV2q4Ys448tuiy6qd28-RSntC_a9_dobmPQrKQrutdGpFfXVDnqBPYL9F984HpetO1PKbHDPzInS9jvSVk1bQHWUNJ9DzAoqq0dGCFqGbBEfQHku92yAQ-GX5SfpDRZKP4EB9xyK5rFsIRsFg1PwmXLNwxz87W6NatN_EZ6qCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda12651f0.mp4?token=CrKz5tI3zyGRpqXAE5rvKGMbXNb2twuvy72rnMF3-6G0e0vonVv_NiHDLvtsFBtZcMbAZUhFIqPfJa9TWgx9DcZCc0zWETS1Tl1hV2x5RydaR8WQ5B3TCzKX-9GyhM_yuuGqQGXqAn2OVstt_EqDLE8c6MGma0MXlqhqsyrbNvZ6rV2q4Ys448tuiy6qd28-RSntC_a9_dobmPQrKQrutdGpFfXVDnqBPYL9F984HpetO1PKbHDPzInS9jvSVk1bQHWUNJ9DzAoqq0dGCFqGbBEfQHku92yAQ-GX5SfpDRZKP4EB9xyK5rFsIRsFg1PwmXLNwxz87W6NatN_EZ6qCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار برای نخستین‌بار/ آخرین مصاحبه فرمانده شهید گروه موشکی ۱۵ خرداد
🔹
شما آخرین مصاحبه فرمانده شهید «عبدالحمید رهبر» فرمانده گروه موشکی ۱۵ خرداد نیروی زمینی سپاه پاسداران انقلاب اسلامی ایران را می‌بینید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/659795" target="_blank">📅 16:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659794">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
لاپید، نخست‌وزیر اسبق رژیم صهیونیستی: نتانیاهو در آزمون لحظهٔ سرنوشت‌ساز فروپاشید
🔹
اسرائیل شکست سیاسی شدیدتر از شکستی که او در قبال پروندهٔ ایران ثبت کرد، به خود ندیده است. زمان آن رسیده که اعتراف کنیم او دیگر قادر به انجام وظایفش نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/659794" target="_blank">📅 16:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659793">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
کانال ۱۳ رژیم صهیونیستی به نقل از یک مقام ارشد اسرائیلی: این توافقی شوکه‌کننده برای اسرائیل است، هیچ کسی در رأس قدرت نیست که چنین فکر نکند، از نخست‌وزیر گرفته تا رئیس ستاد
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/659793" target="_blank">📅 16:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659792">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba8b3ddeae.mp4?token=EMekqrY7C6n8683Inrsuc9NAI1hn60mkX92qR8omxHIygnXSjZHN23uY3U0_hIQ5XvQ-DmCGi0xhCtWzKlNd0T-LOBYiXyXhQDcTBRhtc00VX-4-wHyuzVuCiKq8av5SfxJHbzi_oYVsuK0SXMDFi0oq8VG5fOHBEg0aPm9J13RekS9xOoFbSEiXp6aJiDv8AgbVIumbkn-XSEaLkLxtvoQm-fWoAWbicG0n4WjySKCxL0j48-R2EbJ7J_ZdG1_tuKX6DnMMrWHBll_3bk3UMTqigcnYgmUjpXuEgArDG-m92j2Bpa57YnxJ_TegIMmSVQM3om81rOgY-tpHHrpFDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba8b3ddeae.mp4?token=EMekqrY7C6n8683Inrsuc9NAI1hn60mkX92qR8omxHIygnXSjZHN23uY3U0_hIQ5XvQ-DmCGi0xhCtWzKlNd0T-LOBYiXyXhQDcTBRhtc00VX-4-wHyuzVuCiKq8av5SfxJHbzi_oYVsuK0SXMDFi0oq8VG5fOHBEg0aPm9J13RekS9xOoFbSEiXp6aJiDv8AgbVIumbkn-XSEaLkLxtvoQm-fWoAWbicG0n4WjySKCxL0j48-R2EbJ7J_ZdG1_tuKX6DnMMrWHBll_3bk3UMTqigcnYgmUjpXuEgArDG-m92j2Bpa57YnxJ_TegIMmSVQM3om81rOgY-tpHHrpFDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه ورود رهبر شهید به مراسم محرم سال گذشته؛ لحظه‌ای که دیگر تکرار نخواهد شد...
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/659792" target="_blank">📅 16:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659791">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8IkodRj2fRktCM2xIoQZIbgzHf0lQItPmckLqcpnZ2_AYKj9ay0aHkb9qwGBfeUvojx3xx9eG6okzbNksjSxUgw8wQ7XHbHA_n54xczCaeWClwjbCuBAu3Iml-JVhvKAPMtMWKy60KLpzEsMulb5vBypzJ7pFBwxQ_ER6OJonPMLgtDhFyQwGCOssP3iCdAcE3s7QVTaxYRFXHkijdou4AA3j3obc5gEJSpfQUHXtEIKBXvBhucYB55HjzycmL5J8W6pIadOLKLX9P1-qAKmVcqiMTuBElOvC2lHJgRRzuKl7aIXD8SsOveTUq7NDxXSMNVdSu8JoqE_ZP1bv0_kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس قوه قضاییه: ملت ایران با تأسی به مکتب حسینی توانست در جنگ تحمیلی سوم متجاوزین را به شکست و هزیمت بکشاند
🔹
اگر در دیپلماسی، عزتمندانه و انقلابی ظاهر شدیم، چون درس‌آموز مکتب عزت حسینیم؛ حسین (ع) همه وجود ماست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/659791" target="_blank">📅 16:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659790">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
رژیم صهیونیستی چند ساختمان را در شهرک عیتا الجبل را منفجر کرد
🔹
منابع لبنانی خبر دادند که ارتش اسرائیل با بمب‌گذاری در چندین ساختمان در شهرک عیتا الجبل، آن را با خاک یکسان کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/659790" target="_blank">📅 16:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659789">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJLnEu79vvoEsM4myciH_6iIn56P09Z18sxPsAKjn5jXOuznLjBao-Sk-dqattr8yQ7lxUzkPgrw12ONUtGKR9pvOqT3f94qHLx0jTeOZbB59Wpfk641y9Ja05FPJIrA3W1BUhoGvvrZwUMEmHod84qG9w0A3ZWVzmTBDwCPe3c4fODzkTvvwg0njsAeIpXOU-HPS9qHnpfzKyw9jmnon5VD2vv2WaBxye74hsk-vy3Kmxowm6dtpBpub_plwFM9SXwXxeLXdpIOKqahyrxBPGmmiRr47m_fZ4cPnJBgvjmywmzVnSwpm_6_eA2gCdX9NhLWP3u8ovtmMjsHWAhj0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: کشتی‌ها شروع به حرکت کرده‌اند، بسیاری از آنها با نفت بارگیری شده‌اند، از تنگه هرمز خارج می‌شوند
🔹
آنها در امتداد «بزرگراه» جنوبی حرکت می‌کنند که کاملاً ایمن، مطمئن و بکر است. مناطق دیگری برای سفر نیز وجود دارد!!!
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/659789" target="_blank">📅 16:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659788">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTqOFVavfHjswvCXPkZhRu0XaKdJa-x80r_YYB6dhDuZXN7aLVehB5auh-A55CFK-su5lERbmjLWh1XiNySC8KI_GkQY3_GsTuU7hdzGLIv-6prqBjEUD1SvQVfGLnjWyKS_RNVqSpHmlhEWLOgniI6k7qVfxX8ZYnuoj0pD_P1_cLo3-Gcb3DsVniIW2sP767ii_3YOs6MvrjhxROIbmkZ8WtaOX4q1817qwg4WSNgKhvGQvDO3AfrgcCTDUSuOz0iPEMo6QMdH7lTQ3lrbTDU63WD3oaEaLmPXhsPtweRiYxAcUhLsONCa5HeM2AsszGBdpMJUbo8aEojUJu3QDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون پزشکیان: ایران از جنگ با دو قدرت اتمی پیروز بیرون آمد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/659788" target="_blank">📅 16:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659787">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ce210dcf0.mp4?token=rzq56C0jXJN8YSjmPoxEZeIn4C_mMl4AJty-2KFjASDOC5qkmcP3FfIfxbfWY6oyUBawELZoPiIdbPFkQY7EIgb9fYGFEqmFgRhejf4pZ6oMhO9IjB93CzmhTrnwGdy3RcVaZrXVZlIPhzvAThAM6sOSE3ejvf7Ja5Bl_eIGkBq-pCCt78CpoUPiWIlPfIDLGvM03mXt8w59PEA67DenkDJMBJfZ2uJrWFHIdRwekVeDUCk6VNTwPotybfBK6DiZgZtiNOUmEsOerNxK-g8Tf8bUTLsJeUHpIfcKuR2F7ILw5jFIBXRqv41Gnz_bI15IY31FnDy-Nk-rlLEtgzmkRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ce210dcf0.mp4?token=rzq56C0jXJN8YSjmPoxEZeIn4C_mMl4AJty-2KFjASDOC5qkmcP3FfIfxbfWY6oyUBawELZoPiIdbPFkQY7EIgb9fYGFEqmFgRhejf4pZ6oMhO9IjB93CzmhTrnwGdy3RcVaZrXVZlIPhzvAThAM6sOSE3ejvf7Ja5Bl_eIGkBq-pCCt78CpoUPiWIlPfIDLGvM03mXt8w59PEA67DenkDJMBJfZ2uJrWFHIdRwekVeDUCk6VNTwPotybfBK6DiZgZtiNOUmEsOerNxK-g8Tf8bUTLsJeUHpIfcKuR2F7ILw5jFIBXRqv41Gnz_bI15IY31FnDy-Nk-rlLEtgzmkRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس درباره ایران: ما اساساً همه کارت‌ها را در اختیار داریم
🔹
اگر ایرانی‌ها تعهدی ندهند، ما مجبور نیستیم چیزی به آن‌ها بدهیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/659787" target="_blank">📅 16:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659786">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10548b8f4.mp4?token=XqBj_RMwK-BjicoeY-CvL8HSD0n0qhpU63YuUtW2pNetOPpzu5KhcItaCJAeL5HOj7sXVyNnLc9h5I0D83ewYqzaa0FhU7nb0e0fAbziId8cJ8pck-JXHkHQO2pCTBAMgE3lAnPnAX5bzllGQeVgFUml-JTVpzrGj8e1uBHsU8w4dS7S8jrdCzxn5T7tZ5aFm33bBGH4M2_D_j0wdl-NjdUoIGPbvXPAl2h2u7kGqQqrFbfB6Waw6Mima5yy2li3t0YKe5QV7V-e8E5Gg4Es21wzsNLjWmvjnADSn4SeCbUf6V9TdpjCCXrKy-zQA1DXESMymX83R3Uf1gc1Zo7s8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10548b8f4.mp4?token=XqBj_RMwK-BjicoeY-CvL8HSD0n0qhpU63YuUtW2pNetOPpzu5KhcItaCJAeL5HOj7sXVyNnLc9h5I0D83ewYqzaa0FhU7nb0e0fAbziId8cJ8pck-JXHkHQO2pCTBAMgE3lAnPnAX5bzllGQeVgFUml-JTVpzrGj8e1uBHsU8w4dS7S8jrdCzxn5T7tZ5aFm33bBGH4M2_D_j0wdl-NjdUoIGPbvXPAl2h2u7kGqQqrFbfB6Waw6Mima5yy2li3t0YKe5QV7V-e8E5Gg4Es21wzsNLjWmvjnADSn4SeCbUf6V9TdpjCCXrKy-zQA1DXESMymX83R3Uf1gc1Zo7s8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس درباره ایران: ما دست دوستی به سوی ایران دراز کرده‌ایم. اگر آن‌ها بخواهند رابطه‌شان با ما را تغییر دهند، ما نیز رابطه‌مان با ایران را تغییر خواهیم داد/ این پیشنهاد است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/659786" target="_blank">📅 16:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659785">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgpiOOYh0zP4J5EN788jLuhvhMJfr5o6e2NIkoiuhiq1Iwi-OdYswFcEOwwEVkzXloNl-eezoFrOVqNDQqxcxPQmW6ypr9w2SzbvTimdizYvOoC6kdoUTzl4f2ca6A4RZWdBNRgjtAsXCIxXHzWIYjf81v9ONmIAawcxjc8BUkZI0cojT-S8mWjeiLpGcztIoFY6ghVbxkFpj63KMi-2LbMmS28DSe42hx1Dls-54c09FD8PDP-r86fPtJVeUY55KmjlZex3ry5z7mxGdDp1YZTAtTkYqF1s-j_lx34hmUOoePzh9ODVZbyypYf4fJ6nxmJ6Lq_holbycYNYqXbizw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر صفحه رسمی جام‌جهانی برای دیدار ایران و نیوزیلند
🔹
این بازی فردا ساعت ۰۴:۳۰ بامداد به وقت تهران برگزار خواهد شد. #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/659785" target="_blank">📅 16:24 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
