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
<img src="https://cdn4.telesco.pe/file/uOjE-jBvy0SBNKaCgzMCLwWI1S5i3llXovSkYAoRpq2UYvKJ4CzDBbLhkxxB9la7gjyjE7eO-1Vzma93lNGjiRau2JGiTg5b9O2scYlRu9029JH2D7QRLZzrRL8qH5arV6LjHRXvZhDhNnpoAsoGSVUdxCpDX0BKU2LkOIZOYi1gfYBJAyLXQi69Is-oluJJ2Vo4y8kmgb9OH09_Jo2ENL1iT07JjYwW3m6ZfdwaIcno2B-oFOobsXReM9FyDg-IOBBDldmGG6iavVs3EPwbc0TPsC-kf07dM9ZnRCILma0ybP0oaI_pQnHl4jDK0AYy8qp3KaF7W7W2NEsCqUGRMw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 22:24:13</div>
<hr>

<div class="tg-post" id="msg-683769">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKc7wBRhB3jVDX8pwRwlKxfObD8UJoCJBjB9S01gVNQ8mu2Z84GeFNeIniBdQLjWETIS9ipcQEBMMpCPRo6KlqiPqiY_7Xebr9x7xyNKQ5CtnL93J7OUQEhMrUovULOi-uPKhURnvwKISRAROR_WzdP7ssuRhuuuJI5HnHth92FJ6W3ujJht66yxLcGc_T6wuYdV0W97pLHQCXWXA01ESn1_uC-0FwuNXi9vHKEsTZZiEqgcHGtIWgeLsMU-e3ow6RHSk2CgTE5yvoDxUYQ1x9hbgcCToSsIbdZXyr4gsMM-em_Y_O9TmHgksOZW7KxvquBRQL40ZViLIM1CV1v_tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گاردین: انتخابات میان‌دوره‌ای آمریکا در سال ۲۰۲۶؛ اقناع، انکار و لفاظی
🔹
ترامپ در آستانه انتخابات، در جنگ ایران «گیر افتاده» است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8 · <a href="https://t.me/akhbarefori/683769" target="_blank">📅 22:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683768">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e6de6f328.mp4?token=n-Ol5B86rP2_SVHTNGjfzbp1ZKKHETt7MyUoNEEtj-FVjcaYk9nSv-tBgeHUhk-3pQuo8rRcZbcLYc32kdMmtVyLL5zF2IPSu3Npc6ZElDdNyT4MphAudgtHiRV8MCJLWWZYUI3ENA1HdmP8VpJKGOqKgFqteez3tuahrWwieLxXSUSBgEP4_BHVaKsbEGmZLG8C9N0arf2vKQ5-R0GGVR00jPFaS_2q66ZS4ZpCkY8jaVW41kL2cMWJKfLE6JXa8p5oDgS_5ChVgkdW4ryJggUvPf9GcjpXALYU1YIWLh6Sgy1CiFjcm9dEOI2sFLNQ1hqJUSnJvEotFLMzIRBAUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e6de6f328.mp4?token=n-Ol5B86rP2_SVHTNGjfzbp1ZKKHETt7MyUoNEEtj-FVjcaYk9nSv-tBgeHUhk-3pQuo8rRcZbcLYc32kdMmtVyLL5zF2IPSu3Npc6ZElDdNyT4MphAudgtHiRV8MCJLWWZYUI3ENA1HdmP8VpJKGOqKgFqteez3tuahrWwieLxXSUSBgEP4_BHVaKsbEGmZLG8C9N0arf2vKQ5-R0GGVR00jPFaS_2q66ZS4ZpCkY8jaVW41kL2cMWJKfLE6JXa8p5oDgS_5ChVgkdW4ryJggUvPf9GcjpXALYU1YIWLh6Sgy1CiFjcm9dEOI2sFLNQ1hqJUSnJvEotFLMzIRBAUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار نماینده حزب‌الله در پارلمان لبنان با عراقچی
🔹
حسن فضل الله از نمایندگان ارشد فراکسیون وفاداری به مقاومت در پارلمان لبنان عصر امروز یکشنبه با سید عباس عراقچی وزیر امور خارجه دیدار و ‌‌گفتگو کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/akhbarefori/683768" target="_blank">📅 22:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683767">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ee2ZN5h_0Tza7OzlR6K9JjmurmdDqW8HVNZrQgtUxoywhXpg5aGV9_9fv0dvw4Pu-er3FEgl6gqdtT6lUFESU3F71dD61PxoMlOSucuIt9ZqJpkdRubJSx1xO1xUk9mZ1k3_6KLETPOBx_DN3YEMvhg8WheSB7fk_h9lEisUByzj-GPG0aOBFBFcV_-CMzpOy7fg41WxQzW9ezMkPtV3XmP5iO_2H4W4LQ4aqXkH0jTa0QFoWfM_U2E_zM7o9XA4ZGqNdxmMopsWvGYKfFBidRu2VS_1U8Zgt5FqoWKbqIVvp0BZA2DBn-QTau555d2fALbOvI7gUWpbdj_yMmxhXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار: آیا تعرفه‌های کانادا هزینه‌ها را برای خانواده‌های آمریکایی افزایش خواهد داد؟
🔹
ترامپ: بایدن این آشفتگی را ایجاد کرد. بالاترین تورم
🔹
خبرنگار: تورم وقتی بایدن رفت ۳٪ بود. حالا ۳.۴٪ است
🔹
ترامپ: جو بایدن
🔹
خبرنگار: بایدن ۵۷۰ روز پیش رفته
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/akhbarefori/683767" target="_blank">📅 22:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683766">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
با مفسد مماشات نکنید
🔹
فارغ از تمام هیاهوهای این روزها و جنگی که دامن کشورمان را گرفته، یک حقیقت را نباید فراموش کنیم. روزهای پیش‌رو، فقط به آرایش نظامی نیاز ندارند، اقتصاد کشور نیز محتاج یک بازطراحی عمیق، فوری و شجاعانه است.
🔹
امروز دیگر وقت بخشنامه‌های بی‌اثر، وعده‌های تکراری و برخوردهای نمایشی نیست.
🔹
یک جهاد واقعی و ویژه اقتصادی لازم است، جهادی که مردم نه در تیترها، که در سفره، بازار، شغل و زندگی روزمره‌شان آن را لمس کنند.
🔹
باید با مفسدان اقتصادی بی‌اغماض برخورد کرد با دانه‌درشت‌هایی که سال‌ها از رانت و خلأهای نظارتی بهره برده‌اند، با محتکران و قاچاقچیان، با گران‌فروشان و اخلالگران بازار، با کسانی که ارز، منابع عمومی و اعتماد مردم را ابزار ثروت‌اندوزی خود کرده‌اند.
🔹
عدالت، اگر قرار است عدالت باشد، نباید پشت هیچ میز و عنوانی متوقف شود.
🔹
باید با مسئولانی هم که گاه با یک تصمیم نادرست، یک بخشنامه عجولانه یا یک سیاست غیرکارشناسی، معادلات یک بازار را برهم می‌زنند و هزینه آن را به میلیون‌ها نفر تحمیل می‌کنند، برخوردی جدی و مسئولانه صورت بگیرد.
🔹
مسئولیت فقط اختیار تصمیم نیست، پاسخگویی در برابر تبعات آن نیز هست.
🔹
در روزهای بحران، فساد اقتصادی دیگر صرفاً یک تخلف نیست، می‌تواند زخمی بر پیکر امنیت ملی باشد.
🔹
مردم نباید احساس کنند که در میدان بحران، تنها مانده‌اند و عده‌ای در سایه همان بحران، ثروتمندتر می‌شوند.
🔹
اگر از مردم صبر می‌خواهیم، باید هم‌زمان با مفسد، رانت‌خوار، فرصت‌طلب و تصمیم‌گیرِ بی‌مسئولیت برخوردی ببینند که صدایش در جامعه شنیده شود.
🔹
امروز کشور به یک جهاد اقتصادی واقعی نیاز دارد. جهادی برای حفظ ارزش پول، امنیت بازار، اعتماد مردم و عدالت.
#سرمقاله
@Tv_Fori</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/akhbarefori/683766" target="_blank">📅 22:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683765">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b3afca9dc.mp4?token=tnTAtsBhYzM-GODBq3KC6PR2AuQlpR6Rhq_N-KJvvC1V_RJArG4RsiNM7jWaxd0YouH0cQJ6uqfhkGBl6t3df0scCLwns3ohbJF_W9zzLkBllLpKhAOB2cLtXyMa4sDkTP9rUKOg4lvM5cKktxBnv3gQRq60yt7DFBf5-Ep0mUhqrTe8gnlLQiX_3DVKf4hbcHxLBY7X9SbJ0jSFwKMoHfB06i0J-Eg7oBKeJ9yyMgIn-uGFcpB0nMNvNUTnG7CQReM651m0aiKyYvAGGAL2l98dCscFeAI4qtl9PZSNFAUexjDtVUWVq-5q2dBUKrA95GKqI4Jcj-D1QwwQPpQm-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b3afca9dc.mp4?token=tnTAtsBhYzM-GODBq3KC6PR2AuQlpR6Rhq_N-KJvvC1V_RJArG4RsiNM7jWaxd0YouH0cQJ6uqfhkGBl6t3df0scCLwns3ohbJF_W9zzLkBllLpKhAOB2cLtXyMa4sDkTP9rUKOg4lvM5cKktxBnv3gQRq60yt7DFBf5-Ep0mUhqrTe8gnlLQiX_3DVKf4hbcHxLBY7X9SbJ0jSFwKMoHfB06i0J-Eg7oBKeJ9yyMgIn-uGFcpB0nMNvNUTnG7CQReM651m0aiKyYvAGGAL2l98dCscFeAI4qtl9PZSNFAUexjDtVUWVq-5q2dBUKrA95GKqI4Jcj-D1QwwQPpQm-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شادی پس از گل ربات فوتبالیست به سبک رونالدو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/akhbarefori/683765" target="_blank">📅 22:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683764">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
دویچه‌وله: جنگ‌های ایران و اوکراین ممکن است به یک جنگ جهانی تبدیل شود
ادعای دویچه‌وله:
🔹
جنگ روسیه علیه اوکراین و درگیری آمریکا و ایران به طور فزاینده‌ای به هم گره خورده‌اند. از پهپادهای ایرانی در اوکراین گرفته تا حمایت اوکراین از کشورهای حاشیه خلیج فارس، مرزهای بین این درگیری‌ها در حال کمرنگ شدن است.
🔹
اگرچه ممکن است این دو درگیری به خودی خود خاموش شوند، اما هیچ راه خروج آشکاری برای هیچ‌یک از طرف‌های درگیر وجود ندارد.
🔹
در همین حال، هر روز احتمال اشتباه محاسباتی یا تشدید تنش وجود دارد. ادامه همزمان این‌جنگ‌ها شاید جنگی جهانی را رقم بزند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/akhbarefori/683764" target="_blank">📅 22:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683763">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cbc2ff0e9.mp4?token=WXmpjkqnD7gfyZ3uZlt0HOiAT6u9uYPe5sRW7CmmJol5Cg39e_GyTBx3o_hCM6_nwnpyEcjc9Rs-yi4g2kmt37T8HxcdFf1Z4YbNtVigflGSJRGAcsuVgS-f49wA_ThcdUN6VFVIJ-jNw_f-9uYo8MvCDNLpYpfYFLTTxREn2XdDduR9OVWzBaTgIcpMWVLoK8MBrpXzFll-AtTL13GmGNbAc3ZOrwDwKHrZmdaATl7JySn0AtPRtpXRrwbBhmfIZYG2R-OZ-RV2eUM9B0V2AnRX7YPDKi2TsZxNSkJbfAY-q4tyo__vuk2YthcqLAk8dJGyequq9oEP2fmCsrgGNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cbc2ff0e9.mp4?token=WXmpjkqnD7gfyZ3uZlt0HOiAT6u9uYPe5sRW7CmmJol5Cg39e_GyTBx3o_hCM6_nwnpyEcjc9Rs-yi4g2kmt37T8HxcdFf1Z4YbNtVigflGSJRGAcsuVgS-f49wA_ThcdUN6VFVIJ-jNw_f-9uYo8MvCDNLpYpfYFLTTxREn2XdDduR9OVWzBaTgIcpMWVLoK8MBrpXzFll-AtTL13GmGNbAc3ZOrwDwKHrZmdaATl7JySn0AtPRtpXRrwbBhmfIZYG2R-OZ-RV2eUM9B0V2AnRX7YPDKi2TsZxNSkJbfAY-q4tyo__vuk2YthcqLAk8dJGyequq9oEP2fmCsrgGNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در زمین گلف جان باخت
🔹
یک بعدازظهر آرام در زمین گلف؛ چند قدم، یک نوشیدنی و اتفاقی که ناگهان همه‌چیز را به هم می‌ریزد. اما ترسناک‌ترین بخش ماجرا، لحظه‌ای است که ....
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/akhbarefori/683763" target="_blank">📅 22:07 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683762">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzCmCb-DvTmg0ax4mY__Z9N5jNaTahrcNf1wxUjj7mViwqQFRGOAKfAmCmg9ocZeTEtfBd_3YlY1xDRwHkNlN1V-EsytN8ghAAx6uwjwiqJrerFSn_Ly0aaUymzft3SmHem4TVTq8BMFeZAnov9dk4nNhGyeaZKynXKTJZ9jbdjxYolUoDBjd2fgR7Rlbv6r7TNsFH6pSa81WT8QByjk4TrCLPHSvpqSI4e5iT09CFr74EO7NPYVgJUldNX7d3p7pL7NcItXbCoedf0pgv4rx6oH58Z9ivw4C-KrJgFjjiAn8uME0bzxgCBj6TkOM1Ytm1m8uiXFQn6GI_4N11lNIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نعمت، امتحانی برای انسان است؛ نه دلیلی برای غفلت
🔹
امام علی(ع) در نهج‌البلاغه یادآوری می‌کند که انسان باید نعمت‌های خدا را بشناسد و در برابر آن‌ها دچار غفلت و عصیان نشود؛ چرا که هر نعمتی می‌تواند آزمونی برای شکرگزاری و بندگی باشد. #نهج_البلاغه_بخوانیم
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/akhbarefori/683762" target="_blank">📅 22:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683761">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuMtPEMhjG_pIsZ8qqUSsCrm2POxeJ1nTwH4zrVsbdSZ7pKJe7o9PAV8qn9lFbtAhHFyeIl9JA12lPlDEUvy1BicBmJmbRojrjaJmSLCd2VQWYaN3FC8zTowTfkpN0V0LH_EsmGxERkTjKXcKabrXe2k2A5iUWG2F7I_3XB5uui97dGqMxRmrkdiRSzjWECX86fKRkABhoJk9fKV-lmT8GJ1MzpQ1TlIYE98V13VMHt7F6aZuEkCdn4qGOXHsX4A20B9JUds6r9tB1HKA71TgZun5ALtOOSSZxe0TRUSwSiROw5k9dkyh_-CdBM80_GO6HYB_uDEvQimnzF2iCtMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول لیگ برتر پس از پایان روز اول از هفته سوم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/akhbarefori/683761" target="_blank">📅 22:02 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683760">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f548c60e11.mp4?token=Tw30NcCCwR7IUEOAGWux2k9KQrLrfZrV5_To4fXSwMSc5fr_3tNB5eureMJrOqX4kHFz4RLYaLez4lgOVx01Xe6h9epRpIBG8kodKY6IjdU9loxkycVKIUTs-4DxBUI6BB_24lLII22hF1mRaQCoKbUTiLRy-3r7XK-1-hH-t0OJV06lvWm5NF21Sjmrvh8skdTCjsxQCAwTK5H8mhowqdLjGg8HNM4NLS_Xd6Hi1cc3zwHsq2e_GYcXL-eOdpflyEy3BtWXpUZblX7hv4nAqcztYhrGhvEDU4yzm2bg35U_-fbN4XqJrEAckThl4Ee4NFn5KD_8XL0MHEBVTxUbiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f548c60e11.mp4?token=Tw30NcCCwR7IUEOAGWux2k9KQrLrfZrV5_To4fXSwMSc5fr_3tNB5eureMJrOqX4kHFz4RLYaLez4lgOVx01Xe6h9epRpIBG8kodKY6IjdU9loxkycVKIUTs-4DxBUI6BB_24lLII22hF1mRaQCoKbUTiLRy-3r7XK-1-hH-t0OJV06lvWm5NF21Sjmrvh8skdTCjsxQCAwTK5H8mhowqdLjGg8HNM4NLS_Xd6Hi1cc3zwHsq2e_GYcXL-eOdpflyEy3BtWXpUZblX7hv4nAqcztYhrGhvEDU4yzm2bg35U_-fbN4XqJrEAckThl4Ee4NFn5KD_8XL0MHEBVTxUbiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحقیر کانادا توسط وزیر حمل‌ونقل آمریکا
🔹
این کشوری است که ارتش ندارد... نرخ مرگِ خودخواسته در آن به رکوردی بی‌سابقه رسیده است.
🔹
اینکه فکر کنند می‌توانند وارد جنگ با دونالد ترامپ شوند و واقعاً در جنگ با آمریکا پیروز شوند، از نظر من کاملاً احمقانه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/683760" target="_blank">📅 21:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683759">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzdIbKHrwqSW45oLmx87PnGKnjwHJIwG3u10110yGZ_PNNcADRHkjj14Xdt8sB2_xK_oVj9etJ2GeziY1zLKyJDQFCQ4u-BaJXmeF0O-cjGROiAphpBetZ2ivyy_peV_GP5OmR85o2KwKz-F7tZotWfGZ5cHg5-I2A5iE5-kBisYyPgdsGOifrMRww59O5vlQY9OmOBYeWmD-2GaLdO6-GDzy0KW8K0jplIDJnDZTMJOZLAPBlrIcLIKdmokhytZBW8XRbwZt3lHifJRlgKBU9xrzeBq0hNCHa3fjCqrys85x9fSYFdF9dh3uGr2QojnIjO3BIAWiIBeLAwRyN3h5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت یک صهیونیست: دیروز با یک ایرانی برخورد کردم که او مرا در آغوش گرفت و از من و کشورم تشکر کرد که کشورش را بمباران کردیم
🔹
این‌ها احمق‌ترین و ذلیل‌ترین مردم جهان هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/683759" target="_blank">📅 21:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683758">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c314e76d17.mp4?token=knL9Mw2zfaKcGxRpEkeC823RWYFjdhHUBwWRSRjiLU2z6o50LCJECXSjqwD4K7jxSPbNCcflzH_yrdZNKGAuGiD46qlE56R93V6TYlyhHWzJfj96xqTAOnWoBN7Oc3Fu_RDjh1RlYrKagoLLIOAtuPdMZvsZ1pyiPe5rcg462MRvGwex5-PtJdzItV8TJzOj9neM0khXKL1R0wObj1WfPlk0kN0u18iCaJ_QysyZ2X24IDVPZM2LFs7i6WhEDFN3IQS4NcThD0M4sKg-PxgiKSzJO3nbaEFUrNrWJQjqLYrjpZXaCAwe85uW8gnrxp6Qd7z6ZyXQBG7ons8Gvtn6Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c314e76d17.mp4?token=knL9Mw2zfaKcGxRpEkeC823RWYFjdhHUBwWRSRjiLU2z6o50LCJECXSjqwD4K7jxSPbNCcflzH_yrdZNKGAuGiD46qlE56R93V6TYlyhHWzJfj96xqTAOnWoBN7Oc3Fu_RDjh1RlYrKagoLLIOAtuPdMZvsZ1pyiPe5rcg462MRvGwex5-PtJdzItV8TJzOj9neM0khXKL1R0wObj1WfPlk0kN0u18iCaJ_QysyZ2X24IDVPZM2LFs7i6WhEDFN3IQS4NcThD0M4sKg-PxgiKSzJO3nbaEFUrNrWJQjqLYrjpZXaCAwe85uW8gnrxp6Qd7z6ZyXQBG7ons8Gvtn6Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای قطع کالابرگ به خاطر سکونت در خارج از کشور ‌چه بود؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/683758" target="_blank">📅 21:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683757">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
جزئیات پاداش ۵ میلیاردی ارتش برای کشتن یا اسارت نیروهای آمریکایی   سرتیپ اکرمی‌نیا، سخنگوی ارتش:
🔹
هر فردی از نیروهای مسلح یا  مردم عزیزمان که دارای سلاح شکاری مجاز هستند، در صورت تجاوز زمینی نیروهای آمریکایی به خاک کشورمان، متجاوزان را به هلاکت برسانند…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/683757" target="_blank">📅 21:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683756">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
اتفاق غیرمنتظره؛ ۹۵ درصد اوراق بدهی دولت فروش رفت
🔹
در آخرین حراج اوراق بدهی دولتی ۹۵ درصد از ۶۲ هزار میلیارد تومان اوراق عرضه‌شده به فروش رسید.
🔹
اتفاق مهم‌تر اما اضافه‌شدن ردیف «معامله‌گران اولیه» و ثبت نرخ بازده آنها در چارچوب قرارداد بود. به نظر می‌رسد دولت با این سازوکار توانسته جذابیت خرید اوراق را برای خریداران بزرگ افزایش دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/683756" target="_blank">📅 21:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683755">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfIGBa5FvQZBHbaHZI9n0O4WXGiPSp_r_76g_yDCOMhFGfJnPq05KLNv64GNzeX_8j78qK7ePi4adsI6-syuTE5mLL-AaKrPfJ1sPXFEdELE7md85P1YfJIBipNIe9FCgU_O15TmRHSnViCzGv7xA7vPhUVBzhvITFQmamlWS35vCHvZTwxQtHlJh8m-D4GM28mrAci504IRl_-aLoZP_M7LfSLUPDYWFNykuU0fuajUjsi18XI3AU1u0go32fHRQKNTMdcLCa8heHkdPYA33z7vdLMeaWZ6KatA7VPfSCzZObJ5d9kVeKNXP3tmmjCeiWbvZVO6vplSH-QKhXbsMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه‌نگار کانادایی: شما به یک پدوفیل اعتماد نمی‌کنید که از بچه‌هاتون مراقبت کنه ولی اعتماد می‌کنید آمریکا رو اداره کنه؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/683755" target="_blank">📅 21:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683754">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ژنرال آمریکایی: باید با ۱۵ پایگاه نظامی خود در خاورمیانه خداحافظی کنیم
مک‌کافر، ژنرال بازنشستۀ آمریکا:
🔹
به نظر من ارتش آمریکا دسترسی به ۱۵ پایگاه نظامی خود در خلیج فارس را برای همیشه از دست داده‌ است.
🔹
چند روز پیش نیز واشنگتن‌پست به نقل از منابع آگاه خبر داده بود که پنتاگون به‌دنبال کاهش حضور نظامی در خلیج فارس پس‌از جنگ است و دلیل آن حجم بالای خسارت‌های واردشده از طرف ایران است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/683754" target="_blank">📅 21:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683753">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKlJz-YjaqY_AII4OeZ0jw9fY_FZvOHY7RQXmzJMfOQln65cNLTLuiS4xekBd1_C1aBU4jbZ9FaWzLB7-pdqtzhEzTbtN2_sL2eCJi6xm98CKh2YQJ2LGdO4kYzr_YIUCNCEH8vojG7vYX4qvRmhq6xAclIEWyiR-5zh4c3SVAt-k7UvNer1TgJs76AebrcrtYAUy0yzsWx6nQs0xN5GD3II4MztxqSMHSGPCcBSW0FNkPSdUN0UxO7IRGgVYnfLh-EucK9aU6GFzJAo2IAdXx6tvA1q9UZ5zCE4J8I1lFO3fjkLU1iiIoHBf9ahM-LXnacl8TydkBBDkUSheV2oIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری قدیمی از محسن رضایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/683753" target="_blank">📅 21:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683752">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/859c55ee57.mp4?token=GwgSRd8xYCVdJXHLtBwRKZBkK0LkTVF_5s_Oiuv0w7jcim9vm4GL4EkkZoxsKqQfjEIhetpWq3d49FSuZy46Dc6pvwqh2gouJgu9KeqctFDSZRjNrZQbw9rh7WLC2Uat30a1Q4DhQDp9BVookH6ISuUxXzZiqqSPrc16HfFOg0cBcS57u7CEdBLVjniiIk_O68703lOJlMAQyCtn0g6S5Pzg0VKY0ojPA-QqJ5fBS4EkstFRC2hiKhKA7_Ft7d7XbO7wMkHncLPZB6Tx5IXV3lL6gdZKXltHjVnfKlqi6MNaygz8uS-w77Nx1k-quw1zK71iIAyRJEbprICIBeu5lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/859c55ee57.mp4?token=GwgSRd8xYCVdJXHLtBwRKZBkK0LkTVF_5s_Oiuv0w7jcim9vm4GL4EkkZoxsKqQfjEIhetpWq3d49FSuZy46Dc6pvwqh2gouJgu9KeqctFDSZRjNrZQbw9rh7WLC2Uat30a1Q4DhQDp9BVookH6ISuUxXzZiqqSPrc16HfFOg0cBcS57u7CEdBLVjniiIk_O68703lOJlMAQyCtn0g6S5Pzg0VKY0ojPA-QqJ5fBS4EkstFRC2hiKhKA7_Ft7d7XbO7wMkHncLPZB6Tx5IXV3lL6gdZKXltHjVnfKlqi6MNaygz8uS-w77Nx1k-quw1zK71iIAyRJEbprICIBeu5lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«تروریستِ اره‌برقی‌به‌دست» به سزای اعمالش رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/683752" target="_blank">📅 21:37 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683751">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc49270824.mp4?token=sgh1puHztDdkmeZP43KRxenbXTGBboAW0PEq-R9h6HHROqE2OGckyVxLOY0kDtHu2sAdrYjmiSgaY3NyBj-zfXyzDRZfpAO4toJ3yQVaTjWdEbVW6O_aCf6RKeFwfZ0ycPS0cfbYCdezcEgteVUuiqx9rogvNWpoSM0j3FUfqD9m9Umu6MknVAkmszwhPoTFYfO8zbHBZbQLQlGF6ngaTFYBRFzerQ2HJdAd2Ys7xaGdJZG0aTwRq-X8gn0t0vS6roP64GF4DweIICPVv46HqxsNXxmBl-A5LX1BTh_-JtYeG3XS2u0ztYD6xFa3M8Bj5eJ3OOjeaDzpjm4fDfSAfKsyNAHnxYCejE_coIPxnYzHMYCD8buEgTNL4Y7Z6SGdI2vsLKBKbI1QmmZJbMCt2E9GJdy2z71ALMiSE7w0WgvLeT38Y6M00GDM6oSu2xxTFoQ5bfyfKfRIwI5VO4S2261uJJKIBV8sen35-mOhuwqnLvXfDuHRzQRoZVNrbrwE_xyvTbG7KT_Jjy2dRVBnVxIDFaFPdEPoK4NtggwF695Qb7QFvr6IguzJ18bSEqikk3Q41rUumIsgq3NItE_FxTSdvZM_cRGtLiRYUdsv9ByLtQ4R9PnveGGM97RHnHFS_4s9qRAtJR17rjlikkupop8xMLyxeC95Jixbt3wc8qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc49270824.mp4?token=sgh1puHztDdkmeZP43KRxenbXTGBboAW0PEq-R9h6HHROqE2OGckyVxLOY0kDtHu2sAdrYjmiSgaY3NyBj-zfXyzDRZfpAO4toJ3yQVaTjWdEbVW6O_aCf6RKeFwfZ0ycPS0cfbYCdezcEgteVUuiqx9rogvNWpoSM0j3FUfqD9m9Umu6MknVAkmszwhPoTFYfO8zbHBZbQLQlGF6ngaTFYBRFzerQ2HJdAd2Ys7xaGdJZG0aTwRq-X8gn0t0vS6roP64GF4DweIICPVv46HqxsNXxmBl-A5LX1BTh_-JtYeG3XS2u0ztYD6xFa3M8Bj5eJ3OOjeaDzpjm4fDfSAfKsyNAHnxYCejE_coIPxnYzHMYCD8buEgTNL4Y7Z6SGdI2vsLKBKbI1QmmZJbMCt2E9GJdy2z71ALMiSE7w0WgvLeT38Y6M00GDM6oSu2xxTFoQ5bfyfKfRIwI5VO4S2261uJJKIBV8sen35-mOhuwqnLvXfDuHRzQRoZVNrbrwE_xyvTbG7KT_Jjy2dRVBnVxIDFaFPdEPoK4NtggwF695Qb7QFvr6IguzJ18bSEqikk3Q41rUumIsgq3NItE_FxTSdvZM_cRGtLiRYUdsv9ByLtQ4R9PnveGGM97RHnHFS_4s9qRAtJR17rjlikkupop8xMLyxeC95Jixbt3wc8qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به داد هم برسیم!
🔹
گاهی فاصله‌ بین «یک مشکل موقت» و «یک فاجعه‌ واقعی»، فقط چند میلیون تومان است...
🔹
اما اگر یک محله تصمیم بگیرد نگذارد هیچ خانواده‌ای تنها بماند، چه اتفاقی می‌افتد؟
🔹
شاید چیزی که قرار است ببینید، فقط درباره پول نباشد...
🔹
حتماً این ویدئو را ببینید.
#چرخ_زندگی
@Tv_Fori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/683751" target="_blank">📅 21:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683750">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
رئیس مجلس نمایندگان آمریکا به فاکس‌نیوز: به زودی وارد مرحله جدیدی از جنگ با ایران می‌شویم و به تلاش برای پایان دادن به آن ادامه خواهیم داد
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/683750" target="_blank">📅 21:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683749">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQivj5fegw8l6vwdDJ4rDWiGTsN_DA9Tq-iBcO-L58rpKH3uOCBX_-AN7DwGIXpYULznVLaHl1bTCVdaqIbveOUJWjiCHJ9YS4ZdGo4abvEjWx0xlJYKPWCLOp9BMo5x59RLA6Vjvkf2zbrz5RJLpfFK9VrfNSFtnQRmeFF6GV4AilzDXlN9xEAovGmEQPeNbRoFH5GMwoVGciPEgc3q4xdzVYJBqGqzeImOAwP9QMiyPiJtcv3no_qINaFmavJYyzmZYcv8yAV4jE8eS76fsiuXHD-4vx6QsDVrfwvuYTMxH62T7k15PG003a6jkzQgkcEV8GHgJbh3dFQ10mCMog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل دوم استقلال به سپاهان توسط قلی زاده
🔹
استقلال ۲ _ ۰ سپاهان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/683749" target="_blank">📅 21:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683748">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
رسانه هندی: آمریکا ۱۵ پایگاه مهم در خلیج‌فارس را از دست داد
تایمز آو ایندیا:
🔹
یک ژنرال چهارستاره بازنشسته ارتش آمریکا اعتراف کرده که جنگ با ایران ضربه‌ای جدی به حضور نظامی واشنگتن در خلیج‌فارس وارد کرده است.
🔹
به گفته بری مک‌کافری، آمریکا دسترسی به ۱۵ پایگاه منطقه‌ای را از دست داده و پنتاگون در حال بررسی انتقال بخشی از نیروها به غرب، از جمله عربستان، اردن و اسرائیل است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/683748" target="_blank">📅 21:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683747">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
رئیس مجلس نمایندگان آمریکا به فاکس‌نیوز: به زودی وارد مرحله جدیدی از جنگ با ایران می‌شویم و به تلاش برای پایان دادن به آن ادامه خواهیم داد
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/683747" target="_blank">📅 21:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683746">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
صدای مهیب صاعقه‌ها در جریان یک طوفان تندری شدید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/683746" target="_blank">📅 21:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683745">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
آتلانتیک: از این پس، ایران قدرت برتر غرب آسیاست
🔹
نشریه آمریکایی با اشاره به شکست آمریکا و رژیم صهیونیستی در حملات به ایران گزارش داد که از این پس قدرت برتر و مسلط در غرب آسیا نه آمریکا و نه صهیونیست‌ها، بلکه ایران خواهد بود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/683745" target="_blank">📅 21:21 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683744">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kw_-ntlsZQ467Ev2k2bVhlTztr0m5xA7sy67YB51xml7bmUBfs9FH73vgWbK9wpH6xUF2OWCaPOyVCfrHZIyCQBM4HAiR4BPBE5oMJwLJPWizvYvb6fiVP-gSPbokhvEinQH2MdgJSTTZ6YKJzZiXj39z6aavTwwz2dPMaZx2gEWKbTfAE9hi0NJGTkChZ9jPndDHHvHxYD-lECkpnQePpYJUhunVbxGLPDtYyPPnef-srmFsJo9O_kbTJ95YB_XA_zK6mIl0N1qRctbn1XfetAqgpIGZDDh5hIUV0g_QSjMleTnlT_pbYC9_f53wc8vOfH4AvB-9v_fZS7qO9tytQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلاهای پشتوانه صندوق رز ترنج کجا نگه‌داری می‌شود؟
🟢
طلای پشتوانه صندوق طلای رز ترنج در انبارهای مورد تأیید بورس کالا نگهداری می‌شود. پیش از ورود طلا به انبار، اصالت آن تحت نظارت بورس کالا بررسی و تایید می‌شود.
🟢
صندوق رز ترنج نیز دارایی خود را در همین گواهی‌های با پشتوانه سرمایه‌گذاری می‌کند و تنها در چارچوب مقررات امکان فروش واحدهای سرمایه‌گذاری را تا سقف تعیین شده دارد.
🟢
بنابراین هر واحد صندوق رز ترنج، متکی به دارایی واقعی، ثبت‌شده و قابل رهگیری در سازوکار رسمی بازار سرمایه است؛ بدون اینکه سرمایه‌گذار دغدغه‌ای بابت تشخیص اصالت، نگهداری یا امنیت فیزیکی طلا داشته باشد.
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/683744" target="_blank">📅 21:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683743">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
وزیر نیرو: اگر روندها مثل همیشه باشد، همین هفته خاموشی ها تمام می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/683743" target="_blank">📅 21:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683742">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6b3ab7f19.mp4?token=vyQ0vvo8N4YyVyw-KHdyCUuZg0zpcogbeOi9uDz949b6j0zFi54sCof4yAsgzr-Y_2NsheqAfJlN5RJpB5AAVaykkVeJsKHaud5-ig3o2HnYaA7N7vRNEI9BZwkQDSfJ5zz_wgRVDEll86FKPkmqOFkIkUxk8R_jGy-Px3X3FYwl0OFhxDjfCZVxzL-fLucOmNo2K3Klk8-oGu1Qav20zbsQtTuCRLtLyWdV3AkHJD31LPzDAj1jhZFOTRNHqsIxITj1ROD5D8OgxUPXi-HXPy8pz8-4fVshTWTf7cqqRThJOOskRYVDGZz7wZAztE4hB4Ov2QRdV-024Fi4323uqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6b3ab7f19.mp4?token=vyQ0vvo8N4YyVyw-KHdyCUuZg0zpcogbeOi9uDz949b6j0zFi54sCof4yAsgzr-Y_2NsheqAfJlN5RJpB5AAVaykkVeJsKHaud5-ig3o2HnYaA7N7vRNEI9BZwkQDSfJ5zz_wgRVDEll86FKPkmqOFkIkUxk8R_jGy-Px3X3FYwl0OFhxDjfCZVxzL-fLucOmNo2K3Klk8-oGu1Qav20zbsQtTuCRLtLyWdV3AkHJD31LPzDAj1jhZFOTRNHqsIxITj1ROD5D8OgxUPXi-HXPy8pz8-4fVshTWTf7cqqRThJOOskRYVDGZz7wZAztE4hB4Ov2QRdV-024Fi4323uqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بوگاتی و C SEED از تلویزیون ۵۰۰ هزار دلاری Bugatti N1 رونمایی کردند؛ تبدیل به MicroLED ۱۳۷ اینچی تنها در ۴۵ ثانیه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/683742" target="_blank">📅 21:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683741">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f081bdae0.mp4?token=ZfVVxiO55FAczbnblMzirPakeWrZ5nEk9JIZFAnIfHngdhMDFr1z156i1lxzuaYdKGRdMSAT4eeq_P4pD3IztE_hHIJj-cHlT2dVnPEKE_KClcQvqD1t-OXPMWklkTdxp1KbIqCGFnRufz9BJWSYBidTUEuBRksS7793Dq40x1BFdI_qFTVpUWVhfk2Rbij453yptYY_S2r8NHTOBbUEYVRuQEqxkB4BHLpuXjNezAMDPgFU6OnQZsRN0Gxo2fQjefu0rm_l3XXJe5a4o9VlcYiKxAAeMBnnbb4I_i5bx82Dn74C7MLx-jOSDodv_FvLHf6FNe8SSgIKY9vC6j_kgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f081bdae0.mp4?token=ZfVVxiO55FAczbnblMzirPakeWrZ5nEk9JIZFAnIfHngdhMDFr1z156i1lxzuaYdKGRdMSAT4eeq_P4pD3IztE_hHIJj-cHlT2dVnPEKE_KClcQvqD1t-OXPMWklkTdxp1KbIqCGFnRufz9BJWSYBidTUEuBRksS7793Dq40x1BFdI_qFTVpUWVhfk2Rbij453yptYY_S2r8NHTOBbUEYVRuQEqxkB4BHLpuXjNezAMDPgFU6OnQZsRN0Gxo2fQjefu0rm_l3XXJe5a4o9VlcYiKxAAeMBnnbb4I_i5bx82Dn74C7MLx-jOSDodv_FvLHf6FNe8SSgIKY9vC6j_kgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس بانک مرکزی: صبح تا شب داریم تامین ارز می‌کنیم و سیاست پولی اعمال می‌کنیم؛ به جوسازی‌هایی که درست می‌کنند خیلی توجه نکنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/683741" target="_blank">📅 21:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683740">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
شرایط نه جنگ، نه صلح به نفع کشور نیست / نباید از مذاکره دوری کنیم و هر جا منافع ملی ما اقتضا کند، باید مذاکره کنیم
رضا سپهوند، سخنگوی کمیسیون انرژی در
#گفتگو
با خبرفوری:
🔹
شرایط نه جنگ نه صلح به هیچ‌وجه به نفع کشور نیست و به اقتصاد و زیرساخت‌های انرژی ما آسیب می‌زند و بر مردم فشار وارد می‌کند.
🔹
باید کشور را از این وضعیت خارج کنیم. ادامه محاصره دریایی آمریکا صادرات نفت ما را مختل کرده و درآمدهای ارزی ما را تقریباً از بین برده است.
🔹
همان‌طور که ما در مقابل آمریکا خوب جنگیدیم، می‌توانیم خوب هم مذاکره کنیم. نباید از مذاکره دوری کنیم و هر جا منافع ملی ما اقتضا کند، باید مذاکره کنیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/683740" target="_blank">📅 21:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683735">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kf2bZIxEIgi5jg4a_nes_TB6N-YKJcOwgR7aLMX3XRCFF2LIW446rNkG3YYQdxOFPlNHJt1Fvtegy8ZthiN9lqMDT8syOc-rIKcs7Y4AgURTpFpJJdt4gF8AH0Kh01gGEe0OXbFskvmZ5s_ORj4kK1Vpuc2T3cdC-xp7DFT4Jf2UPPDAKwBR4vAW99TrVpr_JrM4k-CeBwugUKhFOe8tGrvg5m9zKF1Lz5ZncBgfhE5l7kEZSBCZCB1cwDEdMIv0ZoIo_uIoQmoC1I2VvNH1y8S3FReeizJZ5O2lv4J7wKVHiSK7gcY4hU9tFFV0gWiYrM6zW7Q1uGAxlQIIP_ssZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZMBMM9xRK9NXFrD_RoG-CGAb8axP0gnGHEO7cXWa3Dv7SSAhMF9y89QnZimyEAWNJFOkLUcuK9F6m3n7FgCl5puY4g5HSb7iSGrPlafQnTTg59x4N4RC4tCrOjY73n0VWrnXdei2eROtE3J5Ia74dBmpAbUP2nPsmNU2sJ_UPxel-vCCADW4WEN__9wYwCVGfs9gs_Bf_4BiW4USPevk2rorvlTVIiL41693wTMRp50RxU5Dc4AmHib29wQnwlUz6icp_jpXZLpz2sc1lhOBJgcEpriqlQ1i54SoWZcwxsy101Qk9zdUZ-fJ74s2CRoqNpMsXhpzseY7cBq38j8wDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D1DRiJDLz2Wzn77N_iB8awFpEQpMhBt5dU2tpSkhh2uIA9Q3DQ33ibA_OQav577BnAljU5hdJLBd7DyIhT78QioONkkIIraugaHUbShzboz469Q_z0PHb6uNzpBZ50kXxH98Thxc3MV6Wfq03NFvH3XjS5q-YMYPHkVSBILzvh9pdOizY_ACuN2PcxsLypsrkzXugUWKUQuVhJF1kTnbdWY2CgJGd_EiGx_2eFkNEPapkf0FgBjqykavGJOdGUpw8IIWKVfWvuK1w06LjwR59BJO_VncigIx7Klm497yjGWj6-cWcnrVtnpkFirHQ9w6ko1IdiQ-HejdYDKGtnAtRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GrnkSgiA4vJEgWmHWUs1U2XkLALA_vVr7sh_17fYKfZDn7SmmM7uEsxYnYkMnPwp5pjJPWvXAL5pNJ1AtXQe2iBx4I4UAjyqt48D4c17gV24eXsQVuEdZOsWWizHjEiiKDgpjvldb9cQPen9w4EecQpW8SSG1h28R11X0TBhPdCzWhYBlCK6SL1dKIL4rLREjTSU8-xwMypHWqHIEo946LHiP1FC2kzjsU51bV3bhtCRHmuzTUUGoiv-kPY8Giys_SZ-izqyI55CrXKFuNSbGGSqrxxTjv8BZM4GlMSnhdZMa0NkRuiMB3zL0JySgDY8CN4dDeLyIrzb-t1WJt4cog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3yQ093IGKjUY-iRtsuVKNq87_3fRLS_6ijbZ3f2E9TzNylh53gW1mAVQeTjRl3m9RF9msGFemyqnDP6oUSKk4EaO7kS5C0AFHr7O_w90NSUpv8K9AY3NNpjjQG4037mSBHCByF_yIA8tKzzCrLp6bERTZAFVocNmvZV4Ix2n_UKDUiKLTx8dKDq9ScBdkkDBUCH0NjZE3Ah4e61PJMtkbViupGHSh4B5P0EMzUgw_7YEDmlljBiTKT2xO3dc9Vt1PNU6G0UJTE_rnr0QTa7QdiIwPhcZah1Y0GblZhQ_wkBy2ttzUOAqyh1Plx4GMzx9stCkfqmDyXXrCMTpDCsbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تفاوت پرامپت بد، خوب و عالی فقط در چند جمله خلاصه می‌شه که می‌تونه خروجی شما رو متحول کنه
#هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/683735" target="_blank">📅 21:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683734">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
بلومبرگ: یمن نه‌تنها مسیر صادرات نفت عربستان از دریای سرخ را مختل کرده، بلکه مسیر جایگزین ریاض از بندر ینبع را نیز با مشکل مواجه کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/683734" target="_blank">📅 20:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683733">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74d1f2107.mp4?token=B9JKf4OtElV8fGxG6Cf-AJ8XUjBxo54c8dLmirSZEHeK9H7JI7JqvW1bFk1AChTjirS8ooFhd0nxzIQ8jvnBbG6vWSZ53_Ott-AoXBBbYiX_WyQS7TKzuj3cLBew2VjqhkpiBPikKGryiOJojMPzzNTZtjfGoi23cFqSQK2KqSbQHqyYlG4OcvLaKF1Sw2oHzL1lutASXkM7SQr5hCj5O20ysXGkvXdLjfbkCJyJ50nNKcU-tyurOIyUHUzBRrVXRBZ6EFFIXE_ouGGoTL1nWvzy5XhAbw34-smDcosgVdsg090uE2erGFVSh7nqO6E0zjyzf_NYdPzwZpOtFOV8Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74d1f2107.mp4?token=B9JKf4OtElV8fGxG6Cf-AJ8XUjBxo54c8dLmirSZEHeK9H7JI7JqvW1bFk1AChTjirS8ooFhd0nxzIQ8jvnBbG6vWSZ53_Ott-AoXBBbYiX_WyQS7TKzuj3cLBew2VjqhkpiBPikKGryiOJojMPzzNTZtjfGoi23cFqSQK2KqSbQHqyYlG4OcvLaKF1Sw2oHzL1lutASXkM7SQr5hCj5O20ysXGkvXdLjfbkCJyJ50nNKcU-tyurOIyUHUzBRrVXRBZ6EFFIXE_ouGGoTL1nWvzy5XhAbw34-smDcosgVdsg090uE2erGFVSh7nqO6E0zjyzf_NYdPzwZpOtFOV8Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوال خبرنگار صداوسیما از وزرا: تا به حال توسط رئیس‌جمهور ویزیت شدید؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/683733" target="_blank">📅 20:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683732">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29c8219b57.mp4?token=uAzyADdj3p6C1kcpzkqi5KSXwaiFlHGug3xhW2HpuOcL10D2WXyyJitQmSFxPAqppS9veQ0xShZu7ZCuWerRXYqbnz4-Q2oqUUIVXkACoGQSKdXM9HlnfAb1Er30-suyc0OZRJymbKZ7e0ZVPw5zi8fBVIajFweIWm686uZeN_UQWSGfSDBhoyXUYAFOVxI3TGI7Kfz-kn_rZe4oVgAb5VhywI5oT__cMd3ney4T9dgE87ld5BxoFI4lc9OzYtPvIiep-iqIZuXQH6nJRAl6zXFpshx-ElpJPjNLGQuR64OnfHKOXT7tJ8XWoUoMtq9b-WNwyiMCNreYtciHFkRj0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29c8219b57.mp4?token=uAzyADdj3p6C1kcpzkqi5KSXwaiFlHGug3xhW2HpuOcL10D2WXyyJitQmSFxPAqppS9veQ0xShZu7ZCuWerRXYqbnz4-Q2oqUUIVXkACoGQSKdXM9HlnfAb1Er30-suyc0OZRJymbKZ7e0ZVPw5zi8fBVIajFweIWm686uZeN_UQWSGfSDBhoyXUYAFOVxI3TGI7Kfz-kn_rZe4oVgAb5VhywI5oT__cMd3ney4T9dgE87ld5BxoFI4lc9OzYtPvIiep-iqIZuXQH6nJRAl6zXFpshx-ElpJPjNLGQuR64OnfHKOXT7tJ8XWoUoMtq9b-WNwyiMCNreYtciHFkRj0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان انرژی اتمی: شیوه‌های نوین درمان را در کشور برای استفادۀ همۀ مردم گسترش خواهیم داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/683732" target="_blank">📅 20:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683731">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
نشریه نزدیک به کنگره آمریکا ادعاها درباره تنگه هرمز را رد کرد
🔹
نشریه هیل روز یکشنبه ادعای دونالد ترامپ و برخی رسانه‌ها درباره عبور گسترده نفت‌کش‌ها از تنگه هرمز را به چالش کشید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/683731" target="_blank">📅 20:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683730">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad4a466bf4.mp4?token=JAV5LHg7q7WHivRcK_q8OeqGfArh20flmJZWZjsJcdM_C73JWBQWQT8la_TnlRKHIEpWi_ww6wcchrVuVWvo9CCDxuHKZnC97dFxAwzhJOTIAzaV23HW0-3w9q62sv-BIQ86icrKw0Sl1LAyK45-GviAY0dvog75xt2nbJ13MkF8UFttpDAVPMsbYL4-A2CUrWcAff-bgKyGFJK-1N3MN8UROyqhE26uyl55MGOfoCQJM5WLLC4C_QMDB32uaJzsG8n9cZRjOFxKjUC8oDEDXcOhRrGVrhJZQAkJsqp6GfsBHd-Nm6FNE-ghKMLJb-M6qd9znuWc6ECi6mSEdzZH-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad4a466bf4.mp4?token=JAV5LHg7q7WHivRcK_q8OeqGfArh20flmJZWZjsJcdM_C73JWBQWQT8la_TnlRKHIEpWi_ww6wcchrVuVWvo9CCDxuHKZnC97dFxAwzhJOTIAzaV23HW0-3w9q62sv-BIQ86icrKw0Sl1LAyK45-GviAY0dvog75xt2nbJ13MkF8UFttpDAVPMsbYL4-A2CUrWcAff-bgKyGFJK-1N3MN8UROyqhE26uyl55MGOfoCQJM5WLLC4C_QMDB32uaJzsG8n9cZRjOFxKjUC8oDEDXcOhRrGVrhJZQAkJsqp6GfsBHd-Nm6FNE-ghKMLJb-M6qd9znuWc6ECi6mSEdzZH-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در منطقه صنعتی در بیت داگان در سرزمین‌های اشغالی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/683730" target="_blank">📅 20:37 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683729">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFBm6VzN6nX0WrG7DtFm8ttlTu8Fnm_ATZ--M4sbgHEc9eYwWZDoawCIAKOx3YNoFwz0efFMqD9ictAVYPwzcK_mhd_VomtX0Z6zq_w6_BCgRLHhny0MFn4degdC1rfSgvGDVHK-rRBD7MiERwHVCjZ1raSrpuY1IzHEX3njwquDb-7dzCz5RhC0ejgOT3cRPWOyLK7mZNwhe2BDuj7uW4Sl8Y1cMPIl45IJsptgIdfCTZ2fO0_94U_wMGnvYasXv2ec8kQaYi2k7tVdksPJW49Qdr16x_7xOOrnazQSQKb5Ksp-RxIsHm8XvelFdLVXjuiE4nue2Sav9LoKbtAy8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دلار ۲۰۰ هزار تومانی و طلای ۲۲ میلیونی | تبدیل سرمایه مردم به کاه | از رهن خانه تا پس‌انداز خانوار؛ تورم چگونه دارایی مردم را می‌بلعد؟ | امروز چقدر فقیرتر شدیم؟
🔹
این گزارش باید از قیمت کنونی طلا، سکه و ارز آغاز شود اما نکته درست همینجاست؛ اینکه این قیمت‌ها در زمان نوشته شدن همین گزارش کوتاه تا زمان خوانده شدن احتمالی آن تغییر کرده است. چیزی که در این میان برای ما مردم عصبانی ثابت مانده یک گزاره تلخ است؛ تبدیل سرمایه مردم به کاه!
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3239874</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/683729" target="_blank">📅 20:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683728">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
معاریو: احتمال درگیری اسرائیل و ترکیه وجود دارد؛ شمال قبرس می‌تواند به میدان رویارویی دو طرف تبدیل شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/683728" target="_blank">📅 20:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683727">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwSIXIiODb1M4ghjJSNvi-vQ62N2Rkt1Z9c-21oFfAw7Z54MnbHgfTB3xFH_7D6gIwSdAIG4xftaA6dl0dLqkd-ehhLFDG-85g7t6MOOIOjC308rNil7rn2Y5DQyA68XTSuHM-XqZ8gdMTkco68aEN0HNaSeJsOWh4IHs61mSp1IJauUFtoRYbZdULeKLNBUbjgKdKJ4xjQaOcAj7sxxSZsypcrUAOLLaBlb4t7qB_2gFOVWXfzhb0nwSBryCHCpXrpkiYtavJ4UBlyVDQ6kuxSlhB7vH1MnHj5CBUU1prFZf2nxw4deWOEho1PD9kwuppnBvjln_OR-PMthT9V7Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درد دارو
🔹
گرانی دارو در سال ۱۴۰۵ وارد مرحله تازه‌ای شده و این‌بار دامنه افزایش قیمت، داروهای عمومی و پرمصرف را نیز دربر گرفته است؛ اقلامی که تا پیش از این بخش محدودی از هزینه‌های خانوار را به خود اختصاص می‌دادند. طبق اعلام سازمان غذا و دارو، میانگین افزایش رسمی قیمت دارو در سال جاری حدود ۴۸ درصد بوده و در برخی اقلام به ۶۰ درصد رسیده است. با این حال، بررسی قیمت تعدادی از داروهای پرمصرف نشان می‌دهد رشد واقعی قیمت در برخی موارد به بیش از ۱۰۰ درصد رسیده است. این شکاف قابل‌توجه میان افزایش رسمی و قیمت‌های بازار، هزینه‌های درمان را برای خانوارها سنگین‌تر کرده و دارو را به یکی از اقلام فزاینده سبد معیشت تبدیل کرده است.
🔹
هشتصدوچهل‌ویکمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/683727" target="_blank">📅 20:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683726">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a42126f5e.mp4?token=nnt2wSAYHq0skjmokd1OMgISkj7774CgZ4ZG33THIYP5ESLJN1z04xcnI9bUyVebCkOyaFFz5WC7F0ZeGsLjKJlTU4R1VxDa7HSj-p-qvAgbm0alCJGOdQt617uaM2QIPWEoPE0JK3-EFO6zb2ZyM2VgNATIq3iFm-1yAqHhb81p5haBs2xWwm2gZ43kYcebHCZhnJAlfFT50Z-xCRJDC3qU_KxbItapYgAn3osLi_ejnqHYuJkSyfRXRN7GSB5ZAfy2EtUGPvDBqvAlznSaOfmVfdfPAB7Jm5ZZgPtsFkdqep4L9b-bAC_fRclPtaNopAGNzgAr6L0GNBUHCOzS1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a42126f5e.mp4?token=nnt2wSAYHq0skjmokd1OMgISkj7774CgZ4ZG33THIYP5ESLJN1z04xcnI9bUyVebCkOyaFFz5WC7F0ZeGsLjKJlTU4R1VxDa7HSj-p-qvAgbm0alCJGOdQt617uaM2QIPWEoPE0JK3-EFO6zb2ZyM2VgNATIq3iFm-1yAqHhb81p5haBs2xWwm2gZ43kYcebHCZhnJAlfFT50Z-xCRJDC3qU_KxbItapYgAn3osLi_ejnqHYuJkSyfRXRN7GSB5ZAfy2EtUGPvDBqvAlznSaOfmVfdfPAB7Jm5ZZgPtsFkdqep4L9b-bAC_fRclPtaNopAGNzgAr6L0GNBUHCOzS1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلیلی با فریاد یا امام رضا طلا گرفت
🔹
سینا خلیلی در وزن ۷۰ کیلوگرم رقابت‌های کشتی آزاد جوانان قهرمانی جهان، در دیدار پایانی مقابل کرمیوف از آذربایجان با نتیجه ۷ بر ۳ به پیروزی رسید و صاحب مدال طلای جهان شد.
🔹
این کشتی‌گیر پس از کسب مدال طلا نام امام رضا(ع) را فریاد زد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/683726" target="_blank">📅 20:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683725">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0bb69875.mp4?token=so7knFLJiCfuoIUNNjasVy8T5GMoCDsa3WCwkncZfT5tKt_YYq-4eF28JzjUuuazEqV-2g75qe1tv10S32GG0J3b7RVhIN_5nKdU75EOycccMNbvad8PAwKScrdTO5ZMfLawjR__LzJkvnQx3wn6HhOJiuIqNRNbTJ-x1osxs3dH9apfemoA3dUyR3MkWSw748Xu3x_pAJ75IVjCzvKEMbXWbq_0i4NAB-jYOirhPNraa7Je0yyK5K9XZLdtzg0WKsETqI_EW6nC3Er7LKLd0BQwCxzEDjbg_tPtg4YCZwkOo1hlDl1WKdYZIvjkKeFAQuQ3l-kkmSYmn6zIi7rUNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0bb69875.mp4?token=so7knFLJiCfuoIUNNjasVy8T5GMoCDsa3WCwkncZfT5tKt_YYq-4eF28JzjUuuazEqV-2g75qe1tv10S32GG0J3b7RVhIN_5nKdU75EOycccMNbvad8PAwKScrdTO5ZMfLawjR__LzJkvnQx3wn6HhOJiuIqNRNbTJ-x1osxs3dH9apfemoA3dUyR3MkWSw748Xu3x_pAJ75IVjCzvKEMbXWbq_0i4NAB-jYOirhPNraa7Je0yyK5K9XZLdtzg0WKsETqI_EW6nC3Er7LKLd0BQwCxzEDjbg_tPtg4YCZwkOo1hlDl1WKdYZIvjkKeFAQuQ3l-kkmSYmn6zIi7rUNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نایب‌رئیس مجلس: ما در قانون گفتیم که بازنشستگان باید ۹۰ درصد حقوق شاغلین را دریافت کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/683725" target="_blank">📅 20:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683724">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون امنیت: جهاد اقتصادی باید بازتعریف شود
عباس مقتدایی،نایب رئیس اول کمیسیون امنیت ملی و سیاست خارجی مجلس در
#گفتگو
با خبرفوری:
🔹
قیام اقتصادی ملت برای حراست از فضای کسب‌وکار، تولید و عرصه خلق ثروت، یک ضرورت عینی است. همچنین می‌بایست مقامات دولتی، نهادهای قانون‌گذاری و همه بخش‌هایی که می‌توانند، در این زمینه ایفای نقش کنند.
🔹
در این مقطع زمانی، جهاد اقتصادی باید بازتعریف شود تا معیشت خانوارها را دگرگون سازد و  از مرحله بیان به مرحله عملیات برسد و زمان‌بندی آن محقق شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/683724" target="_blank">📅 20:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683723">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dW7wm1hmhZyT33OJrtVNq5FUncOc_WvvFNrvvQ7nDhlYi8DlYly7wA-ai5ZbhjohKDACZ8FrvY1dM_5734gBL8FwNA4RXYi_PxYsh6KmwAvt3B-xE8UiGqdbKYsf9zRQ3zrdWOcmkgLLJ945tmL3K-vR7YE3SXHIURyoW2JUl3XBJpZUCRalDMzYUa3S0cbk-kM1gd88aSCfJS-_VAwNgfkauHXWXM-oiXdEH4Ts_tMKskvAdktK3Mr56ArWQImboxCl4R-xG4stxZSomxNxrgHYyaPSKvT3btufeL_SFCJqV5dCbgXZ_Tmw0KEuduwdXY4qkd4E7xhzk1rUBfkqig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جلسه اضطراری نتانیاهو برای مقابله با بادبادک‌های غزه
🔹
دفتر نخست‌وزیر رژیم صهیونیستی از برگزاری نشست فوری با حضور نتانیاهو و وزیر جنگ این رژیم برای بررسی تهدیدهای ناشی از پرتاب بادبادک‌ها و بالون‌های آتش‌زا از نوار غزه خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/683723" target="_blank">📅 20:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683722">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">02 Ane Manaee (1403-07-19) Marghade Sheikh Sadoogh</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/683722" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه دوم
حجت‌الاسلام امینی‌خواه:
🔹
روانشناسی باور؛ تقابل عمیق بین مؤمن و کافر [01:45]
🔹
دسیسه‌های شیطانی: شانتاژ و تخریب مسیر ایمان [02:55]
🔹
قرآن، کتاب زندگی یا کتاب مراسم؟ [08:00]
🔹
تماشاچیان عاشورا؛ بازیگرانی خاموش [19:00]
🔹
حضرت حمزه و درس‌های بزرگی از غیرت و تعصبِ به‌جا [25:28]
🔹
وقتی پیامبر (صل‌الله‌علیه‌وآله) کوتاه آمد ولی امیرالمؤمنین(علیه‌السلام) کوتاه نیامد... [26:45]
🔹
تکرار تاریخ؛ از سکوت مرگبار جامعه تا فریاد‌های رسای حضرت زهرا (سلام‌الله‌علیها) [36:50]
🔹
۱۲ قرن تنهایی و مراقبت از دشمن؛ روضه‌ای که با زندگی سید حسن نصرالله دوباره خوانده شد [44:56]
🔹
چقدر باید ظلم کنند تا بیدار شویم؟ [51:50]
🔹
پاسخی از جنس شعر، کرامت رضوی در کلام صائب تبریزی  [55:20]
🔹
رهبر معظم انقلاب؛ دلی که با یقین می‌تپد [59:58]
🔹
توبه جناب حر؛ امید در تاریک‌ترین لحظات [01:017:00]
🔹
معجزه‌ای از کربلا؛ بدن سالم جناب حر پس از قرن‌ها [01:23:43]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/683722" target="_blank">📅 20:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683721">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c153e7d278.mp4?token=v3vpsmKog4KHtv93eTDkQ78WAzZVOSX0JYB2A2DSLRu-szAHZ4TdcaVrN5ZlFS3hGzj9e-3SwJSuCTcSJ_Nc6S6McUSMos7ZLP0lb-I_4EsSRYqmvaQHgGNOiqf4db62D2uwpCfWaKeKUASg9i9Tvwx0Spw0SD1pdk96TH0HSx2LCZa7HwtACYnhWgiVRA8PK2cBRgO2EuTbOgWoNacHNKG2JoFBY5zBYjIjcfiN-HYA7mZ2UTFISPoS8bj149LcHgY9L1IjNkWZDatLSGS5207ICyO8UHrjRRMVdtleSoQLAdWQ_c-w7uNFYPfjoQ5qlT4SlJN9oatE01lv-K77IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c153e7d278.mp4?token=v3vpsmKog4KHtv93eTDkQ78WAzZVOSX0JYB2A2DSLRu-szAHZ4TdcaVrN5ZlFS3hGzj9e-3SwJSuCTcSJ_Nc6S6McUSMos7ZLP0lb-I_4EsSRYqmvaQHgGNOiqf4db62D2uwpCfWaKeKUASg9i9Tvwx0Spw0SD1pdk96TH0HSx2LCZa7HwtACYnhWgiVRA8PK2cBRgO2EuTbOgWoNacHNKG2JoFBY5zBYjIjcfiN-HYA7mZ2UTFISPoS8bj149LcHgY9L1IjNkWZDatLSGS5207ICyO8UHrjRRMVdtleSoQLAdWQ_c-w7uNFYPfjoQ5qlT4SlJN9oatE01lv-K77IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با چند ترفند ساده، اتوی بخارت‌ رو مثل روز اول تمیز و آماده استفاده نگه دار! #ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/683721" target="_blank">📅 20:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683720">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
رئیس سازمان بهینه‌سازی: ۴ روز بعد از آغاز جنگ، جلسۀ دولت تشکیل شد، آقای عراقچی در جلسه گفت ممکن است دشمن اینجا را بزند، رئیس‌جهور گفت به درک که می‌زند. من جلسات را تعطیل کنم از ترس اینکه او می‌زند؟ خُب بزند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/683720" target="_blank">📅 20:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683719">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2781b49bbf.mp4?token=MtyhS_tjR2ED2Y_ee9Zy6tfZ5ct7S_1msayDeTMm08YQwmt3F9ktpStmStCUmzClYm5Et36gFoOSuBkPQZFhJD4RmRJVPXU-KW_hojR3lvV-xkiuF_J7mKgn9vo1w3nTA-zvS5QFqstJLwl1FZm_45i2Pwcna3BCGq7-ZR98wlOiQGg_Np1ZKYBKHeldEzgfdkO484sbKJ_F8_6Vzw_4a_8dwMVK1z2PMfywy9GnEG7O7mZTjB-mL0FW4SRnSXrmp74k5ZT8zsBiDOsxQObyRYCC0ZM-q2hxK2UkPrCGiX3bZDb68tvEAncu09BLg9dlNwGmF2L695uXtepdVqS0Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2781b49bbf.mp4?token=MtyhS_tjR2ED2Y_ee9Zy6tfZ5ct7S_1msayDeTMm08YQwmt3F9ktpStmStCUmzClYm5Et36gFoOSuBkPQZFhJD4RmRJVPXU-KW_hojR3lvV-xkiuF_J7mKgn9vo1w3nTA-zvS5QFqstJLwl1FZm_45i2Pwcna3BCGq7-ZR98wlOiQGg_Np1ZKYBKHeldEzgfdkO484sbKJ_F8_6Vzw_4a_8dwMVK1z2PMfywy9GnEG7O7mZTjB-mL0FW4SRnSXrmp74k5ZT8zsBiDOsxQObyRYCC0ZM-q2hxK2UkPrCGiX3bZDb68tvEAncu09BLg9dlNwGmF2L695uXtepdVqS0Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقاب اصفهانی: بخشی از مصرف بالای بنزین به خاطر کیفیت خودرو است  رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی:
🔹
با اینکه کیفیت برخی تجهیزات پایین است اما تغییر رفتار، زودتر از اصلاح تجهیزات و اقدامات دیگر قابل انجام است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/683719" target="_blank">📅 19:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683718">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f08c8d12a6.mp4?token=MclD0lcZNoLJ-YDHfTGoL91OOS3Mb_UVRQmTynUPeNuDi9mLxXRGDarJg7ffiJuoBhM4m7aPpWNF2WbVIC3nwckui6LUg5VGisInzXue6ZPuI3JjzdgqMVC4e5a14oqVMUI0PDzHPMvMTgCXs9-DQSufXZnSefD4FIDTWHFAVhY5fY_emeCCjMVJTIYa2GKIHjErg6bnzOW1Cv8Npo4ctWVZmwoH4LA5gpoMBkxThokfy7L9wg4rpoQiBiB3W-iW5ZeGREDh1E75UbiAun55ZTnmDuaBiwEpSnYjDKF8Q2pEfm5ZJlJp4JVIrLqENalJKRPWcc-HHR15YR9to7NLlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f08c8d12a6.mp4?token=MclD0lcZNoLJ-YDHfTGoL91OOS3Mb_UVRQmTynUPeNuDi9mLxXRGDarJg7ffiJuoBhM4m7aPpWNF2WbVIC3nwckui6LUg5VGisInzXue6ZPuI3JjzdgqMVC4e5a14oqVMUI0PDzHPMvMTgCXs9-DQSufXZnSefD4FIDTWHFAVhY5fY_emeCCjMVJTIYa2GKIHjErg6bnzOW1Cv8Npo4ctWVZmwoH4LA5gpoMBkxThokfy7L9wg4rpoQiBiB3W-iW5ZeGREDh1E75UbiAun55ZTnmDuaBiwEpSnYjDKF8Q2pEfm5ZJlJp4JVIrLqENalJKRPWcc-HHR15YR9to7NLlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان بهینه‌سازی: در ایام جنگ به رئیس‌جمهور گفتم حاضرید باهم برویم پای لانچر؟ او گفت برویم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/683718" target="_blank">📅 19:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683717">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7cb82fdaa.mp4?token=E5Syvsrgu0fOBg3hM5x5VdmuUCdZFJrC_t-JkkBwMlsp18Xp92DtK3ruk2lsV0jf0rngy3QUIzfzxva84KSCb7C7lZlhVEEZQw_9MFy920zffi4JAS14c_Bk6kTNcIX_hQOK0pIUOvLEVgXIXXerJ5KFjsSYIBKJVab3RRPUCupIACxyeZ6-K5H1jQ3sm8SAprjUxHM4o7jtCcz3ApqCNfR4UbtgHsC9Q08yZUyNeL-M1Z8AZoKp7w66xMFLjgRv8wBWueVw8zKP7gKdXeL6E4ifUn5gFGk1L62ca021vxAEiPpZbk3NbTiO_RVuy-bQxEHQNtbSejffeFD9ZdLLVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7cb82fdaa.mp4?token=E5Syvsrgu0fOBg3hM5x5VdmuUCdZFJrC_t-JkkBwMlsp18Xp92DtK3ruk2lsV0jf0rngy3QUIzfzxva84KSCb7C7lZlhVEEZQw_9MFy920zffi4JAS14c_Bk6kTNcIX_hQOK0pIUOvLEVgXIXXerJ5KFjsSYIBKJVab3RRPUCupIACxyeZ6-K5H1jQ3sm8SAprjUxHM4o7jtCcz3ApqCNfR4UbtgHsC9Q08yZUyNeL-M1Z8AZoKp7w66xMFLjgRv8wBWueVw8zKP7gKdXeL6E4ifUn5gFGk1L62ca021vxAEiPpZbk3NbTiO_RVuy-bQxEHQNtbSejffeFD9ZdLLVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان بهینه‌سازی: به رئیس‌جمهور گفتم باید کارهایی کنیم که در کوتاه‌مدت فحش بخوریم اما در بلندمدت از ما تشکر شود
🔹
آقای پزشکیان به من گفتند حتما این‌کار را بکن زیرا ما باید مسائل را حل کنیم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/683717" target="_blank">📅 19:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683716">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96dbefcd54.mp4?token=EyzWCJmvuZLL5BrDuG6_BZOgeiOdJtvg7Z7KQkT44-ius0ctibhFYsGLnS8qXb6nc1VzhTGQOu9a83_LxJbNtWKpn4MwLHCj2JfJvJhS2HuRfU-cTuDf5YbtFf2ZiHyI49fYRkP9BpF7otlE90_exvm2P0xPkEI2FYv0HiJJ7n6UiqyzgQc1YAFH2vV2gjYAzvAP86vDKr8234Qz_K7hQApFJqWABeTfXUEBEX_xUFw0f8u7LjLtxtNklwaxYSkZ5jeyIlpwniTobce287iHjJOM7YfiBAq-qtcrX0CtApK9VkkP30bClqs9rAbybRGHB1dg73S1UiMYW5T1ZlQZRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96dbefcd54.mp4?token=EyzWCJmvuZLL5BrDuG6_BZOgeiOdJtvg7Z7KQkT44-ius0ctibhFYsGLnS8qXb6nc1VzhTGQOu9a83_LxJbNtWKpn4MwLHCj2JfJvJhS2HuRfU-cTuDf5YbtFf2ZiHyI49fYRkP9BpF7otlE90_exvm2P0xPkEI2FYv0HiJJ7n6UiqyzgQc1YAFH2vV2gjYAzvAP86vDKr8234Qz_K7hQApFJqWABeTfXUEBEX_xUFw0f8u7LjLtxtNklwaxYSkZ5jeyIlpwniTobce287iHjJOM7YfiBAq-qtcrX0CtApK9VkkP30bClqs9rAbybRGHB1dg73S1UiMYW5T1ZlQZRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان بهینه‌سازی: به رئیس‌جمهور گفتم باید کارهایی کنیم که در کوتاه‌مدت فحش بخوریم اما در بلندمدت از ما تشکر شود
🔹
آقای پزشکیان به من گفتند حتما این‌کار را بکن زیرا ما باید مسائل را حل کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/683716" target="_blank">📅 19:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683715">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534e133ebb.mp4?token=GsQbQiH1G1GQp04bL2Rykj_skGCwXf50GnFKF3see7a4KfNfPPt3uklNuB-09J4dLWDx7HZOxrw25SYNo9nwmLuBCMqDb8pKt7zOYpUJTZvDuonWUZEzCWr7YZS7bXOgdJkWi9gu5_ruS64REpn_HAL0C7B8O3qPPfvQksTWEUezA6e2u03ECARmCS4H7pIRupyghp-ZdTe-d3_SJHEAPX8dOwR3MedNiLdSSZmJWeB2QN7rpuuGUu5bpIArnD1X0mB_HIYCJbAEzLfRxAv3rJk1ulTJzZA_AauW5Qy2fgJ41C2aDyv8QltXgWyI5xfDmpaGrR0cxUw_UoiuJ9Pv6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534e133ebb.mp4?token=GsQbQiH1G1GQp04bL2Rykj_skGCwXf50GnFKF3see7a4KfNfPPt3uklNuB-09J4dLWDx7HZOxrw25SYNo9nwmLuBCMqDb8pKt7zOYpUJTZvDuonWUZEzCWr7YZS7bXOgdJkWi9gu5_ruS64REpn_HAL0C7B8O3qPPfvQksTWEUezA6e2u03ECARmCS4H7pIRupyghp-ZdTe-d3_SJHEAPX8dOwR3MedNiLdSSZmJWeB2QN7rpuuGUu5bpIArnD1X0mB_HIYCJbAEzLfRxAv3rJk1ulTJzZA_AauW5Qy2fgJ41C2aDyv8QltXgWyI5xfDmpaGrR0cxUw_UoiuJ9Pv6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد ضدصهیونیستی در آرژانتین، معترضان پایان «نسل‌کشی» رژیم اشغالگر در غزه را خواستار شدند
🔹
صدها تن از شهروندان آرژانتینی با برگزاری راهپیمایی گسترده، سیاست‌های جنایتکارانه رژیم صهیونیستی در نوار غزه را به‌شدت محکوم کرده و توقف فوری ماشین کشتار این رژیم را فریاد زدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/683715" target="_blank">📅 19:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683714">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
پزشکیان: صرفه‌جویی مصرف بنزین باید از دولتی‌ها شروع شود
رئیس‌جمهور در جلسه هیئت دولت:
🔹
برنامه‌ریزی کنید که چگونه می‌شود ماشین‌های دولتی و مصرف دستگاه‌های دولتی را کاهش داد و میزان ترددهای ماشین‌ها را پایین آورد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/683714" target="_blank">📅 19:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683713">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12fbb21d0.mp4?token=LN90fthTBiSW3gbcrLr2cXD4mBskgR6qdP-kYtD7W3kQVBH7BAw5OMmhnEF9vOTeJRdxBLVK4CyEaHVaECUSRYnEljGK1jJi21o_HKnzSe1uobH1HPgorPHXoNx9QlUPZ2tuqeDwAda9J9U3ZzJGQUFWfb1LW4z0S5VQ7yyjfgwoRWhF8JXviTQ1UgCpSerb5YmeEA2zx7YqJskNVQ2jKjmq1j0nsYSw6Cd2i7cOE0-dyhxbUBtEZdJ5jG3rZE7QJrrssUPV9M8nyO4J78UaVRvMX0VRp72FVV8K3ruD0DxEBQm8dxr88jmG7rvwrK4l6TpUCV-y0pvtCo3qthYjnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12fbb21d0.mp4?token=LN90fthTBiSW3gbcrLr2cXD4mBskgR6qdP-kYtD7W3kQVBH7BAw5OMmhnEF9vOTeJRdxBLVK4CyEaHVaECUSRYnEljGK1jJi21o_HKnzSe1uobH1HPgorPHXoNx9QlUPZ2tuqeDwAda9J9U3ZzJGQUFWfb1LW4z0S5VQ7yyjfgwoRWhF8JXviTQ1UgCpSerb5YmeEA2zx7YqJskNVQ2jKjmq1j0nsYSw6Cd2i7cOE0-dyhxbUBtEZdJ5jG3rZE7QJrrssUPV9M8nyO4J78UaVRvMX0VRp72FVV8K3ruD0DxEBQm8dxr88jmG7rvwrK4l6TpUCV-y0pvtCo3qthYjnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول استقلال به سپاهان توسط یاسر آسانی   استقلال ۱ _ ۰ سپاهان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/683713" target="_blank">📅 19:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683712">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
رسانه صهیونیستی: همه جای جهان اسرائیلی‌ها را کودک‌کش می‌خوانند
🔹
کانال ۱۴ تلویزیون اسرائیل اعتراف کرد، حتی در دور افتاده ترین نقاط هم صهیونیست‌ها را کودک‌کش لقب می دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/683712" target="_blank">📅 19:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683711">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhGaOTgg72hVrf6USvnVQR2JdrFr4b5QxQMcYAGdOleeVExtpfDBx2ey7ZgINg_WnFYRoxInlbSq30j3Ap5qVWuVdmYY0kcP-JtqxmMj08QT-RaNHh2mrVJh49G1IMA6LHeztAx3179Q56VGAP-FQZsFGhRC9-XjhYnunA7E-6LBY2v3yRwo0lEveSP6V70QyDbATbjrk-vPJ1wwFRzxeqo4aWD4xIkUtd63TnYuGuMmXOgeXvcoDpZmZhxZBG_cofrUKaNmcqBqfOZX2EoyN9cGA3yuWCh0Xi2gL08yzPqOX-Msl6nZKBmJYRpfiAuyzkAS0hjRjmaGqHJu_GAFtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گسترش فرصت‌های سرمایه‌گذاری در وال‌گلد؛ نقره به میدان آمد!
💎
تنوع، کلید موفقیت در بازارهای مالی است. پلتفرم «وال‌گلد» در گام جدید خود این امکان را فراهم کرده است تا کاربران بتوانند در کنار طلا، روی «نقره» هم سرمایه‌گذاری کنند.
🔸
روند یک سال اخیر نشان می‌دهد نقره بازدهی‌های چشمگیری در بازار سرمایه داشته است.
🔸
با این امکان جدید، سرمایه‌گذاران می‌توانند با ترکیب طلا و نقره، یک سبد مطمئن‌تر، کلاسیک و پربازده بسازند.
ورود به بازار جذاب نقره
ورود به بازار جذاب نقره</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/683711" target="_blank">📅 19:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683709">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96b95162d0.mp4?token=PwvRP6hIMyjPXbrFd8IcwyMhI58MLgbPrD0KTDUORDBrKz1TwxUQYB8EmxYTuQXSZoHMCI05aTbwZ0KO5kPUanVWM6T1XDszhly0wkyWBlVhlAgO8SwtoYniveKlvCQnXvb7Pn5TkpQXj8P64FfSxfYhcnzAitugi9N6_zh8yWe85Ag7vduQg_sbNERG0rMo1ui_cG-hWNA_lsSdDCdrRjs5LPfuKiLtVjj66jMtjbCvXnmKaVUS8wcaWk3AX2IN6lk7kJBr4NdC2PtpCPsPKl6GnCuw22t_CndD22xvbUac5OBECQxaEjjKvBkcSaSLEpGHddL-QkkMGDSqKuw_WUX-h6osgBjor7ZkysoXBwtvQZ8ezG2xg76bdmSv-Yyda9jxUtxYAxUD8bw_MeQW8LRF2c69FZOSXGOqJffh94msIb-nMrgDdfvnoFtReYCTKFy7pj_mOxHs3nQ80RQaVDHhJ00fqGlbBgVsoGLG50-k0QoWDBuLf3ORFJtGAFSYqdSkKd4MYGm_8sqovTatKHhMThLNmAxmtDJmomD27jW_RoRn2jZNk9f1Pr86qzcy1R-kUg0uPZoiOexxP2N0G9gavIzTvDybsM6lhJuAIlvr0l7kP3p1tmvnmJSFAeRLN_8xZDaJiugsrBUn8w2HxO2FOQFwRyBBsn_rHYccRuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96b95162d0.mp4?token=PwvRP6hIMyjPXbrFd8IcwyMhI58MLgbPrD0KTDUORDBrKz1TwxUQYB8EmxYTuQXSZoHMCI05aTbwZ0KO5kPUanVWM6T1XDszhly0wkyWBlVhlAgO8SwtoYniveKlvCQnXvb7Pn5TkpQXj8P64FfSxfYhcnzAitugi9N6_zh8yWe85Ag7vduQg_sbNERG0rMo1ui_cG-hWNA_lsSdDCdrRjs5LPfuKiLtVjj66jMtjbCvXnmKaVUS8wcaWk3AX2IN6lk7kJBr4NdC2PtpCPsPKl6GnCuw22t_CndD22xvbUac5OBECQxaEjjKvBkcSaSLEpGHddL-QkkMGDSqKuw_WUX-h6osgBjor7ZkysoXBwtvQZ8ezG2xg76bdmSv-Yyda9jxUtxYAxUD8bw_MeQW8LRF2c69FZOSXGOqJffh94msIb-nMrgDdfvnoFtReYCTKFy7pj_mOxHs3nQ80RQaVDHhJ00fqGlbBgVsoGLG50-k0QoWDBuLf3ORFJtGAFSYqdSkKd4MYGm_8sqovTatKHhMThLNmAxmtDJmomD27jW_RoRn2jZNk9f1Pr86qzcy1R-kUg0uPZoiOexxP2N0G9gavIzTvDybsM6lhJuAIlvr0l7kP3p1tmvnmJSFAeRLN_8xZDaJiugsrBUn8w2HxO2FOQFwRyBBsn_rHYccRuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول استقلال به سپاهان توسط یاسر آسانی
استقلال ۱ _ ۰ سپاهان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/683709" target="_blank">📅 19:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683708">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سرپرست وزارت دفاع: یافته‌های فراوان اطلاعاتی و فناورانه‌ای از دشمن به دست آوردیم
🔹
کمیسیون امور داخلی مجلس: اعتبار گذرنامه افراد بالای ۱۵ سال ۱۰ ساله و زیر ۱۵ سال ۷ ساله می‌شود.
🔹
وزارت دفاع عراق: ۹ مهر تاریخ نهایی خروج نیروهای بیگانه از عراق است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/683708" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683707">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
خبرهایی درباره انفجار در حلب سوریه
🔹
منابع خبری از انفجار در حلب خبر دادند، ولی هنوز جزئیاتی درباره علت انفجار منتشر نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/683707" target="_blank">📅 19:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683706">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc966282fc.mp4?token=vCJ0FoRjEyDZZXMG9V22gNIpPMgsT0MJ0xSec4jo4tm7zauu5IO-Nhi22jyXx25LBuw6Ebm9cXv0NLNNyt1a_Q6hXruf0WlSw47ZLvNJ0Ds22U5pLijOyTaQw9dU0jOskfRT26kY3HooEiy7thd_CZdzfwb9c7ozjugF-jzYBU1Cphx4ICRHicH4SQ27TDFvSjHBMliwu54TQEVNe1KT9HnRt3ijETv91si24SVUZ203At7v7Q5JaG0F0KAcsb4VP61IawIvqw9v9pS_Vo60jaA-8J724ly-w5A6nOgqwlMz_Ue2dhyAkfGYKqSaHjiH6EmrGyJkcNI_W6lUHigWZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc966282fc.mp4?token=vCJ0FoRjEyDZZXMG9V22gNIpPMgsT0MJ0xSec4jo4tm7zauu5IO-Nhi22jyXx25LBuw6Ebm9cXv0NLNNyt1a_Q6hXruf0WlSw47ZLvNJ0Ds22U5pLijOyTaQw9dU0jOskfRT26kY3HooEiy7thd_CZdzfwb9c7ozjugF-jzYBU1Cphx4ICRHicH4SQ27TDFvSjHBMliwu54TQEVNe1KT9HnRt3ijETv91si24SVUZ203At7v7Q5JaG0F0KAcsb4VP61IawIvqw9v9pS_Vo60jaA-8J724ly-w5A6nOgqwlMz_Ue2dhyAkfGYKqSaHjiH6EmrGyJkcNI_W6lUHigWZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش زیبا روی خورشید
🔹
این ساختار حلقه‌ای تاج خورشیدی، یک مسیر مغناطیسی است که پلاسمای فوق‌داغ پس از یک شراره خورشیدی از طریق آن به سطح خورشید بازمی‌گردد.
🔹
ثبت این ساختارهای ظریف و رشته‌ای در هیدروژن آلفا با این میزان پایداری بسیار نادر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/683706" target="_blank">📅 19:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683705">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a398e28d40.mp4?token=AaD_fulNOvey57FaryfS4HjUMygBd20zNidkAtkg4r79SIWjYoUrqA7FWcX7CpSAth6yOYNokjjXzxsDmX3JIaimsUTIzbGoYuytgGWk3aXtH9MsmW18dcn-BUzmLw66Y9jkOqsk-KascJbWDVWzQAjJ0m6red9-3FykxZzeBwGNh7qx8WeZRsNfaXC-Q1YR0gXBJ2YOCI67pJFJ1lB9jgwVZPtxYh_GSOobIQM3Mpo_eBzAFTVmlgs_M5O0bhphsPpe-M1ZT_9WiPRNwNKYuqaTxOXxYvX5fFTrHLFGf_oD1yGbe0FNu9HMptDZCyPPpImqBF8Ez9ZEKWlk_n8OVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a398e28d40.mp4?token=AaD_fulNOvey57FaryfS4HjUMygBd20zNidkAtkg4r79SIWjYoUrqA7FWcX7CpSAth6yOYNokjjXzxsDmX3JIaimsUTIzbGoYuytgGWk3aXtH9MsmW18dcn-BUzmLw66Y9jkOqsk-KascJbWDVWzQAjJ0m6red9-3FykxZzeBwGNh7qx8WeZRsNfaXC-Q1YR0gXBJ2YOCI67pJFJ1lB9jgwVZPtxYh_GSOobIQM3Mpo_eBzAFTVmlgs_M5O0bhphsPpe-M1ZT_9WiPRNwNKYuqaTxOXxYvX5fFTrHLFGf_oD1yGbe0FNu9HMptDZCyPPpImqBF8Ez9ZEKWlk_n8OVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام پناهیان: کسانی که در مسئله علی‌الاصول دل رهبر انقلاب را خون کردند امروز همچنان از بخش‌هایی از توافقنامه دفاع می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/683705" target="_blank">📅 19:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683704">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس مرکز امور زنان و خانواده وزارت کشور: محققان می‌گویند غلظت ماری‌جوانای مصرفی در ایران بالاتر از جاهای دیگر است
پروین داد اندیش، مشاور وزیر و رییس مرکز امور زنان و خانواده وزارت کشور در
#گفتگو
با خبرفوری:
🔹
درباره زنان بی‌خانمان نگاه سلیقه‌ای است و می‌خواهند مسئله را پاک کنند، اما تاجایی که می‌دانم اگر به آقای پزشکیان مهلت بدهند، رویکردشان این است که با مسائل کارشناسانه برخورد می‌کنند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/683704" target="_blank">📅 19:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683703">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
قشقایی: ماده ۳ طرح اقدام راهبردی تأمین امنیت و پیشرفت تنگه هرمز به تصویب رسید  سخنگوی کمیسیون امنیت ملی:
🔹
بر اساس این ماده، در قبال خدماتی از جمله خدمات دریانوردی، محیط‌زیستی، سوخت‌رسانی در شرایط خاص، بیمه‌ای، ایمنی و سایر خدماتی که ارائه می‌دهیم، هزینه…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/683703" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683701">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a928736d65.mp4?token=QnZiBW4hsZduHY_lTnCFIUYJqdLrXK6cdczU7p_7aAer66lscugsMbtBBu3shimUGXdhIPBtzMFnEYaJL0TzZpssiniU6Lc2zC0WZ3rYCuBpCF13o7c7Plk3y7jk3J7Yp3isMIHpL5QELdZmA4EI3AwZQkzEAaoHiHOms1Ow-2ld0uUnjsvy5ZjX4e2vftwIS2e7uhYe00adCXVOeEZ5sFSlx8mMj_MFzNEO0GVjY9XqVe8APo0UPPP2A1PL5C1q469i49ZnNAmvic3mXOoOHhYZbHXOdmX4Ftl6F_pWdJM_dN3oth70hRvq-A6zt4AbydcwR2wvPKpDafcha_kf1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a928736d65.mp4?token=QnZiBW4hsZduHY_lTnCFIUYJqdLrXK6cdczU7p_7aAer66lscugsMbtBBu3shimUGXdhIPBtzMFnEYaJL0TzZpssiniU6Lc2zC0WZ3rYCuBpCF13o7c7Plk3y7jk3J7Yp3isMIHpL5QELdZmA4EI3AwZQkzEAaoHiHOms1Ow-2ld0uUnjsvy5ZjX4e2vftwIS2e7uhYe00adCXVOeEZ5sFSlx8mMj_MFzNEO0GVjY9XqVe8APo0UPPP2A1PL5C1q469i49ZnNAmvic3mXOoOHhYZbHXOdmX4Ftl6F_pWdJM_dN3oth70hRvq-A6zt4AbydcwR2wvPKpDafcha_kf1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات انسان‌نمای چینی رکورد پرش ارتفاع را شکست
🔹
ربات انسان‌نمای شرکت X-Humanoid در دومین دوره بازی‌های جهانی ربات‌های انسان‌نما در پکن، با پرش ۲.۸۸ متری رکورد این مسابقات و رکورد ۲.۴۵ متری پرش ارتفاع ایستاده انسان‌ها را که خاویر سوتومایور در سال ۱۹۹۳ ثبت کرده بود، شکست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/683701" target="_blank">📅 18:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683700">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
سردار ابن‌الرضا: برخی بمب‌ها اختصاصاً برای استفاده علیه ایران ساخته شده بود
سرپرست وزارت دفاع:
🔹
دشمن در «جنگ تحمیلی سوم» با استفاده از ابزارهای سایبری، نظامی، نیروهای نیابتی و عناصر ضدانقلاب وارد میدان شد و برخی سلاح‌ها و بمب‌ها برای نخستین بار و به‌صورت اختصاصی علیه ایران به‌کار گرفته شدند.
🔹
وی این جنگ را نخستین جنگ موشکی و پهپادی گسترده، دارای بالاترین حجم عملیات هوایی و یکی از پیچیده‌ترین عملیات‌های نامتقارن دانست که در نهایت با شکست دشمن همراه شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/683700" target="_blank">📅 18:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683699">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6af592104d.mp4?token=Z-M-CunCKyS_I9pwrju3hd71R77PJDBdGa-D1ZDWbEuR_DVQqwEua8omqGa_Q9a5MVPzT02n3O1nFShkRwXIENDAaLvddgxjjFTcNGuf5br879rGFjNdCZifYcHTU5tBFXdOwCjkFAVzZbxu9t3jbQEsbb0g41JNGt6L74G-p-r3VIe3LLKjfY9WBoj5UXdhcF0bev6u5E4lBTQuXBS4Q-NNElNtMR-Das9rbyQ0hIYzQD2TvtR5JE-3RI_u4bK_1KYgXhZBODJyI1OFXV9pPzWYo1sVHmswjGbCy8jZCNz0dDgjgCPL5QXfInUgpe9mhB-3AvVYELqOKegKjVI1Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6af592104d.mp4?token=Z-M-CunCKyS_I9pwrju3hd71R77PJDBdGa-D1ZDWbEuR_DVQqwEua8omqGa_Q9a5MVPzT02n3O1nFShkRwXIENDAaLvddgxjjFTcNGuf5br879rGFjNdCZifYcHTU5tBFXdOwCjkFAVzZbxu9t3jbQEsbb0g41JNGt6L74G-p-r3VIe3LLKjfY9WBoj5UXdhcF0bev6u5E4lBTQuXBS4Q-NNElNtMR-Das9rbyQ0hIYzQD2TvtR5JE-3RI_u4bK_1KYgXhZBODJyI1OFXV9pPzWYo1sVHmswjGbCy8jZCNz0dDgjgCPL5QXfInUgpe9mhB-3AvVYELqOKegKjVI1Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادهای اوکراینی به مرکز لجستیک بزرگ نزدیک سن پترزبورگ در روسیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/683699" target="_blank">📅 18:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683698">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی: دریافت هزینه خدمات از کشتی‌های عبوری از تنگه هرمز تصویب شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/683698" target="_blank">📅 18:37 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683697">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37f4a95602.mp4?token=kAlMj2tsqBZu_6C-0Pei4sih5aSGNN82lXPWBcoIBVb7YH1KKYotAep57V30GO02NcyEgazVUa5eujQ_hmaTSs7WrKqp8M7cxPRDfSFFFPdhVmANut9Ov19GHfomZc8ys4aZaj6Eaa5SBO5Fkvv3Hwvj6Yl3HWEqT8SVlUOSACi08nLHX5QuhsZruIVl3Eei4WmaQq2q0nnXAq0LS9kJH8lBzV4wSXEFLj9YaBoIP_DfJaDIsSBtHHpaeJ0V09atspFmK66SAozuqpwzEvdOMIb_D21JvCX-cOP-FFf9nZ1MJi1BEZHg5USPsFFrs8NN9soYoYMPe9kUy39mOzaSUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37f4a95602.mp4?token=kAlMj2tsqBZu_6C-0Pei4sih5aSGNN82lXPWBcoIBVb7YH1KKYotAep57V30GO02NcyEgazVUa5eujQ_hmaTSs7WrKqp8M7cxPRDfSFFFPdhVmANut9Ov19GHfomZc8ys4aZaj6Eaa5SBO5Fkvv3Hwvj6Yl3HWEqT8SVlUOSACi08nLHX5QuhsZruIVl3Eei4WmaQq2q0nnXAq0LS9kJH8lBzV4wSXEFLj9YaBoIP_DfJaDIsSBtHHpaeJ0V09atspFmK66SAozuqpwzEvdOMIb_D21JvCX-cOP-FFf9nZ1MJi1BEZHg5USPsFFrs8NN9soYoYMPe9kUy39mOzaSUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احیای مراتع خشک تانزانیا با گودال‌های هلالی
🔹
پنج سال پیش، در مراتع خشک آروشا در تانزانیا گودال‌های هلالی برای مهار روان‌آب و هدایت رطوبت به خاک ایجاد شد؛ روشی که با کاهش سرعت آب و فرسایش، به رشد دوباره پوشش گیاهی و احیای زمین کمک کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/683697" target="_blank">📅 18:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683696">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی: دریافت هزینه خدمات از کشتی‌های عبوری از تنگه هرمز تصویب شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/683696" target="_blank">📅 18:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683695">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0f10383f9.mp4?token=vokg-3BjgoiZykdbqJPECGa9u4Xs_Pj3VruHxiWiVnUAGxveiiz8ecfVAvWlOkVpjmK9-Y-DFU-a_tDuXXhvrvw6I_LJ4vrEKp4mljpHx0fDvw-UKc1Qirjq3rcAEkKedhcY3LnTVemDNwWslbW-HHiRaooLxlYi9kTKZRz1icp7Lqc83I7LShAzN0oMI9NigqeEqj0BHd5N7_GyjsraFhNaQdti7SaWGD11EO01E9fQmaR0g8-ve6ceYFPr-dIqnTlM1xPv6xRhbgB26idYqMHciStAcDgnPL03K-DO-jsVzBG6QNHuTUATkKa6C3VgrD9QCNnYDOwjoOPRC8aoLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0f10383f9.mp4?token=vokg-3BjgoiZykdbqJPECGa9u4Xs_Pj3VruHxiWiVnUAGxveiiz8ecfVAvWlOkVpjmK9-Y-DFU-a_tDuXXhvrvw6I_LJ4vrEKp4mljpHx0fDvw-UKc1Qirjq3rcAEkKedhcY3LnTVemDNwWslbW-HHiRaooLxlYi9kTKZRz1icp7Lqc83I7LShAzN0oMI9NigqeEqj0BHd5N7_GyjsraFhNaQdti7SaWGD11EO01E9fQmaR0g8-ve6ceYFPr-dIqnTlM1xPv6xRhbgB26idYqMHciStAcDgnPL03K-DO-jsVzBG6QNHuTUATkKa6C3VgrD9QCNnYDOwjoOPRC8aoLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین طرح هواپیمای مسافربری ۸۰۰ نفره را رونمایی کرد
🔹
این هواپیمای بال‌تک‌سوار با عرضی ۱.۶ برابر بمب‌افکن B-2، ظرفیت حمل بیش از ۸۰۰ مسافر را خواهد داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/683695" target="_blank">📅 18:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683694">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoojtCqzS_tW4Ob2OSothNByRBOYYdENXLI3vZnSykBaJpuJCGSzop3Jx6l12mGitt8RURhMqdc-cxKo2Zh1_gkUQyvlPXCjW-SD_jectfe-ucSlqcdcgQYq8EuYiVLoWfzF_Zepz5IRLO5OVvTdgVzTwvkSm2tV4tCLHeUfOET-zlzvfOjGc-PzfjeQBeAsODS9ELIW5Ru4U43TqiE6eDRT-DnakGL0YC9yI1hgj9FFkTuyQLoEWGXVxrUpWkf5dqE8ztdOiJPuGL5QNsaQCE9xOWobgMx5ccmh3znhYOrku_Y5hdRukNEdk0C3j8BtmiQ-tKD_CgxGZhLFN20eBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در انتخاب پزشک، کدام عامل برای شما مهم‌تر است؟
🔹
در این نظرسنجی حدود ۲۶ هزار نفر شرکت کردند که سهم روبیکا ۵۳، بله ۲۹ و تلگرام ۱۸ درصد بوده است.
🔹
حدود ۷۳ درصد از شرکت‌کنندگان، تخصص پزشک را مهم‌ترین عامل در انتخاب پزشک دانسته‌اند و ۱۱ درصد نیز توصیه دوستان و خانواده را در رتبه بعدی قرار داده‌اند.
🔹
این یعنی در انتخاب پزشک،
اعتماد به توانمندی
نقش شرط اولیه را دارد و عوامل دیگر بیشتر تعیین می‌کنند که از بین پزشکانی که قابل اعتماد به نظر می‌رسند، کدام‌یک انتخاب شود.
@amarfact</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/683694" target="_blank">📅 18:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683693">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erkZ0mLJBsUrQOsP0J_7RCwckM6nvN6pYSE-IrWoH1YpW37Rfi7PyJQMxZCSQu4eJ94_xS2PzQZ3_g52pRbP4dCuzAuIyykci5JwCMj5TWf0koasOUUtVA7-wspRVF6sXpQbIZiBJ3Y-JPb8FhhV3usapkdMpJo_WCaa3C52xkmiw0_7E6IRFqdJL45eJfutS-ksxUT_LCkdhpw0Gj5iZ9LuYAuHAqPWOjkNd4nGf6e_U8TJ38qYDjeSq7rtWcry4w6juT4DhY7n5gFxK1SQKRBSfCLXx7IeBpsUKDaox8R5LTF7emePxSkHc8roBDLX17zfQNIduH9LXC84yjzSsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فایننشال‌تایمز: جنگ با ایران آسیب‌پذیری حضور نظامی آمریکا در غرب آسیا را نشان داد
فایننشال‌تایمز:
🔹
پایگاه‌های عظیم نظامی آمریکا نزدیک به چهار دهه ستون فقرات حضور این کشور در غرب آسیا بودند، اما شش ماه جنگ با ایران میزان آسیب‌پذیری این ساختار را آشکار کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/683693" target="_blank">📅 18:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683692">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02b1d573bc.mp4?token=TxAS8qScDj_0OzYfwKtlYTTj0heDRLBfUBWdCXffALj0cKKUAlUfH7Tq2SFcYolEOvVEcwIX-CwB_Mb5-dfLILZKuGMVoQ8RfY5e9gzN08NBfNsKn7v8v0-8ItBkM3yr0eJa2kbv5CxSQYHwW2bSxxKczTnsF_ZjnfJtGT-iutKhT23N7JtbSFTccSPOsbkX5S-Mnx073lkY7sZiHsWVmA3IT4AKz6iTrftkydbgby0azJXXxxPbOjY2vx-a9rQSrBvpxgjtNIkfQnBWeBucY24F0fcF9GnfN96xdhjzvSgJ8FslBKZHSTdYBzHkj1RqqeK69ByD1PmoDVQ6xt3iYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02b1d573bc.mp4?token=TxAS8qScDj_0OzYfwKtlYTTj0heDRLBfUBWdCXffALj0cKKUAlUfH7Tq2SFcYolEOvVEcwIX-CwB_Mb5-dfLILZKuGMVoQ8RfY5e9gzN08NBfNsKn7v8v0-8ItBkM3yr0eJa2kbv5CxSQYHwW2bSxxKczTnsF_ZjnfJtGT-iutKhT23N7JtbSFTccSPOsbkX5S-Mnx073lkY7sZiHsWVmA3IT4AKz6iTrftkydbgby0azJXXxxPbOjY2vx-a9rQSrBvpxgjtNIkfQnBWeBucY24F0fcF9GnfN96xdhjzvSgJ8FslBKZHSTdYBzHkj1RqqeK69ByD1PmoDVQ6xt3iYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۲۶ جمله کاربردی زبان انگلیسی که مطمئنا به کارتون میاد #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/683692" target="_blank">📅 18:07 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683689">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzRlfJND5wTuVrhBcyUtU0Eflaop2WTVgBvZzVCyAqovvbOgfwAEIrzwyYiNhgWTOTh0P4HbiYrc-rK609-0aaLBP_jm9Mm5z4uAHKznWmR6jgIzMTyl6WZo8fN5ZmnvEbE-xuxjUse54GkssPR_m0ZtNAyeCkEep2aSVPX2p_SbslrHbjZbBydMIhgAXBEIWMk70M5Q_88Lzl1umHcPoowSNfb1crjYdaggo19p4E7ePObymoVyIXRFjjiXICHZMcyubdI1EsjB9jkz0oPh1r_Fzo9QPuGoxV-wnwYS-3Hz7MLrS-QawB0_0PO9iZD0Vh6ziSfPyxMZ0eCh8hekTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
دوره آموزش طراحی طلا و جواهر با Rhino و Matrix
+ گواهینامه قابل ترجمه از سازمان جهاد دانشگاهی صنعتی شریف
🔹
برخی سرفصل‌ها:
📌
آموزش پروژه‌محور طراحی طلا و جواهر
📌
مدل‌سازی سه‌بعدی با Rhino و Matrix
📌
طراحی انگشتر، گوشواره و آویز
📌
اصول سنگ‌گذاری و ضخامت‌دهی
📌
آماده‌سازی فایل برای پرینت سه‌بعدی
⏱️
مدت دوره:
۴۰ ساعت
🎯
سطح:
مقدماتی | همراه با منتورینگ اختصاصی
✅
بدون نیاز به پیش‌زمینه
اطلاعات بیشتر و ثبت نام
👇
https://t.me/+FN40rMsbFhoyZjU0</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/683689" target="_blank">📅 18:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683688">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaI5TcnVI2dCisFRDQPVKRCV1N9rV78WES-D_LE0zJU0p0SSDaLLVbNpNPgGMI5lY3cmb_o_KacK6SEZpTDf7A2z_Jt7CWdxpRoieK7kaInscGgl6J_EvvfbvaunLl6DuFhByPVmsZQ4GVKZwgpS8_dmjCSBJGx1o1_FCdugnxci7nuHwn2ZvtdOpGWmw0I9wy-D29lneYlXTozLr9bEGpi3Dy9CnY5Xc2dWhXBhlq_Kan8VZts01TQaZFxSenFlBBLJolxNmfLA3oXvg2wF85sWbnfluG9EqVEutt7Ncigjo6df7t_wG49KA1kNlxeVabVK1JywZ083CUXnvq7yeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: فشار اقتصادی علیه ایران مثل بومرنگ به صورت آمریکا می‌خورد
🔹
واردات گوشت یخ‌زده برای کنترل قیمت گوشت؟ باشه، شاید جواب بدهد.
🔹
اما برای اوراق قرضه چه نقشه‌ای دارید؟ می‌خواهید بازدهی یخ‌زده وارد کنید؟
🔹
برای مسکن، خریداران یخ‌زده وارد می‌کنید؟
🔹
برای چاره‌اندیشی دستمزدها، فیش‌های حقوقی یخ‌زده صادر کنید؟
🔹
یک سیاست خارجی یخ‌زده و بدون ابتکار، اقتصادی یخ‌زده و راکد به بار می‌آورد.
🔹
تنها چیزی که هنوز در حرکت است؟ بومرنگ ایران که به صورت خودتان برمی‌گردد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/683688" target="_blank">📅 17:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683687">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87707f32c3.mp4?token=kpDAaQeJF3Ez2m4SCZqKyK9HVsF6EhgpH4sdm77TQ6oYhVbJbOzXZRfGpbsLB6nRHxd0TKxHhbotdX092YAbP3wDLdAyiG3UdxmEtFoOOhqF3GL5O4YgEV3i120Ja9RtYGQB8MUTpR5UaPrWgmQQwhWcMudAPClTMgNRdcayqA4Ut59E87xw1T0l7vmQ7qgxwpaHL4rMXiKCVJJYkM6RLe636BMU6Meu-Lm8PVdqvRCbAMlM3oerQn_lULEPxfRzH-Rnh6pL3w1FxAbNsuMot6fpGvX5ra3Bz0zLuTZIMjb3vwrk2411jaF9xKt1IApEfcYVXFv9tSVG-VEvF259DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87707f32c3.mp4?token=kpDAaQeJF3Ez2m4SCZqKyK9HVsF6EhgpH4sdm77TQ6oYhVbJbOzXZRfGpbsLB6nRHxd0TKxHhbotdX092YAbP3wDLdAyiG3UdxmEtFoOOhqF3GL5O4YgEV3i120Ja9RtYGQB8MUTpR5UaPrWgmQQwhWcMudAPClTMgNRdcayqA4Ut59E87xw1T0l7vmQ7qgxwpaHL4rMXiKCVJJYkM6RLe636BMU6Meu-Lm8PVdqvRCbAMlM3oerQn_lULEPxfRzH-Rnh6pL3w1FxAbNsuMot6fpGvX5ra3Bz0zLuTZIMjb3vwrk2411jaF9xKt1IApEfcYVXFv9tSVG-VEvF259DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای تلخ سقوط یک خانواده در هند
🔹
یک جوان ۱۸ ساله در هند به‌دلیل اختلاف با پدرش بر سر پرداخت اقساط آیفون قصد داشت از بالای دره خودکشی کند.
🔹
مردم با وعده خرید آیفون ۱۵ پرو او را منصرف کردند، اما هنگام نزدیک شدن پدر، هر دو به دره سقوط کردند و مادر خانواده نیز پس از مشاهده این صحنه به پایین پرید؛ در نهایت هر سه جان باختند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/683687" target="_blank">📅 17:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683686">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
رئیس سازمان نظام دامپزشکی: همه پت‌شاپ‌ها در کشور غیرقانونی هستند
رئیس سازمان نظام دامپزشکی:
🔹
پت‌شاپ‌ها در کشور به‌صورت غیرقانونی فعالیت می‌کنند. آن‌ها اجازۀ فروش دارو و مکمل‌ها را ندارند.
🔹
درحال حاضر اتحادیۀ گل‌فروشان، آرایشگران و بعضاً اتاق اصناف برای راه اندازی پت شاپ‌ها مجوز می‌دهد، درحالی‌که طبق قانون سازمان نظام دامپزشکی مسئول صدور مجوز است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/683686" target="_blank">📅 17:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683685">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db946df252.mp4?token=PYUE6QlwZW8WWtBjSfHqAEo-R3xQSUDdrSQ-4n6DWv8V63PVzg0ThBLOTkrPq4A6PUfjFIipSHuo-U6WLMUcza0XeQzCWr8D2N9tM5_xOcmYP_4ktNO4VbJIAMQqto9-TtIcGe0be0AKbarFGvp4u23vo4X26E-cScDF2Zv-VGrbXZ7eUy46LaKxQaQET8uwhSHN3iFdaEZjpEAnW-ltq3ml1tw8DcqZ-qPW_DudbRja-w66lDJ7FuDRws9_ZsUBfs7fBuj_HSk-2BsNki4EFhGCO-GTGdp1aw7GxHH2V36xqfR6fUi_va8gHsc35v0-1QboCRKAyJC76Ram34wEiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db946df252.mp4?token=PYUE6QlwZW8WWtBjSfHqAEo-R3xQSUDdrSQ-4n6DWv8V63PVzg0ThBLOTkrPq4A6PUfjFIipSHuo-U6WLMUcza0XeQzCWr8D2N9tM5_xOcmYP_4ktNO4VbJIAMQqto9-TtIcGe0be0AKbarFGvp4u23vo4X26E-cScDF2Zv-VGrbXZ7eUy46LaKxQaQET8uwhSHN3iFdaEZjpEAnW-ltq3ml1tw8DcqZ-qPW_DudbRja-w66lDJ7FuDRws9_ZsUBfs7fBuj_HSk-2BsNki4EFhGCO-GTGdp1aw7GxHH2V36xqfR6fUi_va8gHsc35v0-1QboCRKAyJC76Ram34wEiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، کارشناس حوزۀ مقاومت: رزمندگان حزب‌الله در علی‌الطاهر در شرایط عاشورایی هستند/ اگر به شکل هدفمند به نیروهای اسرائیل در خاک لبنان حملۀ موشکی شود، فشار زیادی به اسرائیل وارد می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/683685" target="_blank">📅 17:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683684">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dd18bba1f.mp4?token=GhiMRRK8TTXC19uNmr9DXBgV7vY8NHbwp1AQfVf1U4HiGF8BJQCZCqbrr8oq6LqX1cZqVBzb_aa9apU0ww_692wlo7bbgiUqUbPIZSovoYEulUiw-5jAakq0HBOszcwUnYiHB_9V3cDdDuaUcWUZBHvxdZCiYmelRJ5XFJsi7EPS5xVyE_kfmRqWjLzGzXeuC7qilpEdLzMGeX02BWkmrT5BPR-A6X_0DZCsNtoYj8S8cKBqVvzmub6NTB9GH8smV38Kf_DuvlE_65S4Z9kqu_KnnTy110qLT7nPu6QHv8NVEeECcixqbCj7v015qKsmYG3z0r5brZAwHXGPjo75WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dd18bba1f.mp4?token=GhiMRRK8TTXC19uNmr9DXBgV7vY8NHbwp1AQfVf1U4HiGF8BJQCZCqbrr8oq6LqX1cZqVBzb_aa9apU0ww_692wlo7bbgiUqUbPIZSovoYEulUiw-5jAakq0HBOszcwUnYiHB_9V3cDdDuaUcWUZBHvxdZCiYmelRJ5XFJsi7EPS5xVyE_kfmRqWjLzGzXeuC7qilpEdLzMGeX02BWkmrT5BPR-A6X_0DZCsNtoYj8S8cKBqVvzmub6NTB9GH8smV38Kf_DuvlE_65S4Z9kqu_KnnTy110qLT7nPu6QHv8NVEeECcixqbCj7v015qKsmYG3z0r5brZAwHXGPjo75WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان شدید چند هواپیما را در ایتالیا جابه‌جا کرد
🔹
وزش باد شدید در شهر فورلی ایتالیا چندین هواپیما را جابه‌جا کرد؛ سرعت تندبادها به ۱۲۰ کیلومتر بر ساعت رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/683684" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683683">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
عاصم منیر در راه تهران  اسماعیل بقائی سخنگوی وزارت امور خارجه:
🔹
فرمانده ارتش پاکستان برای تقویت همکاری‌های دوجانبه و رایزنی درباره امنیت منطقه دوشنبه به ایران می‌آید.
🔹
منابع العربیه ادعا کردند: فرمانده ارتش پاکستان، پیام‌های آمریکایی را در جریان سفر خود…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/683683" target="_blank">📅 17:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683682">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2576646bde.mp4?token=lOqml2QihMxyAfBJJTsRDsADXB-9gJhi4D4mjuzIqb645UPpjIVKVnBJh2ukpU9lew_PU35m1KQvhSi0CgXaJWwYxQYmr1_l2lf6H_oKN94TmIuJP7JmwSPnfaQluo2G-JmchU0qtlEJmeYhi2yXTnYMRyaHFh0tvShZECYQyEVtdDwd_FKL4pk36ZkUIu-rsv0W-8W6yKq6-xMbinLoa5wtKWHOZLyygg1kGSSzOPQKjkebra9vgdc-4dgK_2xRn6aK1oYYWzPBE3XPyNqs6mARMHwkHf-M_9CD91KoRBdiHkUUFVBHBWJy9sA7cru1ybHDiMsHpjtb3NjY8bcLHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2576646bde.mp4?token=lOqml2QihMxyAfBJJTsRDsADXB-9gJhi4D4mjuzIqb645UPpjIVKVnBJh2ukpU9lew_PU35m1KQvhSi0CgXaJWwYxQYmr1_l2lf6H_oKN94TmIuJP7JmwSPnfaQluo2G-JmchU0qtlEJmeYhi2yXTnYMRyaHFh0tvShZECYQyEVtdDwd_FKL4pk36ZkUIu-rsv0W-8W6yKq6-xMbinLoa5wtKWHOZLyygg1kGSSzOPQKjkebra9vgdc-4dgK_2xRn6aK1oYYWzPBE3XPyNqs6mARMHwkHf-M_9CD91KoRBdiHkUUFVBHBWJy9sA7cru1ybHDiMsHpjtb3NjY8bcLHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات‌های انسان‌نما در پکن قدم برداشتن را تمرین کردند
🔹
در افتتاحیه دومین دوره بازی‌های جهانی ربات‌های انسان‌نما در پکن، ربات‌های کوچک دوپا با گام‌های لرزان و زمین‌خوردن‌های پیاپی، تلاش کردند مهارت راه‌رفتن و حفظ تعادل را تمرین کنند.
🔹
این ربات‌ها برای حرکت و حفظ تعادل، بارها به کمک نیاز داشتند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/683682" target="_blank">📅 17:28 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683681">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e9d4a30cf.mp4?token=gSuvgS21YXDP3mEYHDClkiwKp_t7y7bS-aRmzr2XzuOGFAtMSOXWRKEsaooM9ZNOpY7JCSh5u7W7y0rNXSWIZN6zc5d0wmwd4y9eKxxgd2xeRFdq7fDuIT7kvNPP3lGBPFVMLyM5oX5UhkCWwNG4NKvS5BRB6TPM0A6iT63ob2qwKJVHcaex2oSA-VfPDjWWXh5hXvGy9h0QU702p1o4jhydZkCg3E2GRMmIMWkj26NoGsTzK25bX3m6w4Mje5bH2fiEfNqTo8eiDzuDov3MpcS8Gf7BhAv5p-78P4EGXvsU1ydsFYHoLbYpXlRK0JNls0ZlRlk62C_294qDTg4ahw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e9d4a30cf.mp4?token=gSuvgS21YXDP3mEYHDClkiwKp_t7y7bS-aRmzr2XzuOGFAtMSOXWRKEsaooM9ZNOpY7JCSh5u7W7y0rNXSWIZN6zc5d0wmwd4y9eKxxgd2xeRFdq7fDuIT7kvNPP3lGBPFVMLyM5oX5UhkCWwNG4NKvS5BRB6TPM0A6iT63ob2qwKJVHcaex2oSA-VfPDjWWXh5hXvGy9h0QU702p1o4jhydZkCg3E2GRMmIMWkj26NoGsTzK25bX3m6w4Mje5bH2fiEfNqTo8eiDzuDov3MpcS8Gf7BhAv5p-78P4EGXvsU1ydsFYHoLbYpXlRK0JNls0ZlRlk62C_294qDTg4ahw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ چرخ زندگی
🔹
روایت شما از ایده‌هایی که در خانه جان گرفتند؛ تلاش‌هایی امیدبخش برای رونق اقتصاد خانواده و ساختن فردایی بهتر.
🔸
یک پیام صوتی حداکثر ۳۰ ثانیه‌ای شامل نام، شهر، نحوه شروع و نتیجه کسب‌وکارتان، به‌همراه عکس کسب‌وکار برای ما ارسال کنید. روایت‌های برتر فرصت معرفی و تبلیغ در خبرفوری و کانال‌های زیرمجموعه را خواهند داشت
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/683681" target="_blank">📅 17:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683680">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/513dfe4113.mp4?token=qEFIUqgUvdUHntICA-lt_534ZEWTmBIo9UIQ5xka9tqgzH7kvSfJUSWpZGm-YpN1SIKEEn5Ie0na4VJ0JWEr8bQPYBR6B8Iw5-UbgiZa3pP_qXdIOWP9LHa0aqvFPTI0E3d0kIzj3pAxFBKqa2oIYLFm7RnaXlMQutQHPWCoLkEhxzvuHqy-Fg1hrQ8hQHpxf11ffV9HVDNXgZG7kNbmfCszLqYsawm1m4MD-0VWPIjNnPwmaGujnXWMHBZFvbyaB03ZQtag3Ct3XBYGgK24vZpjnY8UMk-cyLoxTZia3WtPQZrAYL_OKGeRRPe70DlDTSQgEdzZLoKASJ6e2OTHprW2vqDNufgqKQnIuNLjqC8TQ01kJhM1V22MxghZTXrXr5TDpSlQIqipFjwvw-6kWXnqyObOVWhxI8SA5plk0VRtQOJ5s_rBdOOsjO4AFLmH4JWJRCVG1EFNnyjWh8AOm8cByvagz8iBw6Sy6kPHjCPVQAhk757zFy5LGN9yriWouEgjeE9pmB2YJJFEXrvv_eDvL_XcE5PusU-EPBTxaCu-7MKIIl9sl6QUyl76zLRgrtqlEqvObq_2LFV4SUiAO8XtNGc-wSsbZHQEn-v6vVvPibV6Nk-Kfsnmh1t61Eet6Uxxtzu3r_cQoloy8lecG39bRJUa8WSkCdwwQu-dffQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/513dfe4113.mp4?token=qEFIUqgUvdUHntICA-lt_534ZEWTmBIo9UIQ5xka9tqgzH7kvSfJUSWpZGm-YpN1SIKEEn5Ie0na4VJ0JWEr8bQPYBR6B8Iw5-UbgiZa3pP_qXdIOWP9LHa0aqvFPTI0E3d0kIzj3pAxFBKqa2oIYLFm7RnaXlMQutQHPWCoLkEhxzvuHqy-Fg1hrQ8hQHpxf11ffV9HVDNXgZG7kNbmfCszLqYsawm1m4MD-0VWPIjNnPwmaGujnXWMHBZFvbyaB03ZQtag3Ct3XBYGgK24vZpjnY8UMk-cyLoxTZia3WtPQZrAYL_OKGeRRPe70DlDTSQgEdzZLoKASJ6e2OTHprW2vqDNufgqKQnIuNLjqC8TQ01kJhM1V22MxghZTXrXr5TDpSlQIqipFjwvw-6kWXnqyObOVWhxI8SA5plk0VRtQOJ5s_rBdOOsjO4AFLmH4JWJRCVG1EFNnyjWh8AOm8cByvagz8iBw6Sy6kPHjCPVQAhk757zFy5LGN9yriWouEgjeE9pmB2YJJFEXrvv_eDvL_XcE5PusU-EPBTxaCu-7MKIIl9sl6QUyl76zLRgrtqlEqvObq_2LFV4SUiAO8XtNGc-wSsbZHQEn-v6vVvPibV6Nk-Kfsnmh1t61Eet6Uxxtzu3r_cQoloy8lecG39bRJUa8WSkCdwwQu-dffQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گریه آیت‌الله آملی لاریجانی زمان نام بردن از برادر شهیدش، دکتر علی لاریجانی
رئیس مجمع تشخیص مصلحت نظام:
🔹
از برادر عزیز و شهیدم، دکتر علی لاریجانی یاد کنم که شخصیت واقعاً ممتازی بود؛ دلسوخته نظام بود، در برابر جفاها صبور بود، تجربه‌های اجرایی مهمی در وزارت ارشاد و صداوسیما داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/683680" target="_blank">📅 17:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683679">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9acc6d6680.mp4?token=YRm0sXzjYciWB_3_-ef9pJcSepQptCr77I7hKVr2hiv-CxrUvV-HaCIoLkCnPmPswjLZ8sx8093l6Vur580UeEckkuL7STZ7ojGkjkRLz0weMTz4NMPkfBO-oh0rNbXVsUHTStmJ3oOg5dgb5CU4H13U8gtIRhjBE8xe_kKz48zOeA2IZBfej94Nh8pl5YyrhNbxQd2xeFtSAEBMdORUtEAy_aEMA7UU944mDOkd3Oy62I7XX-i7ve7xfhp5OEItf-IhfLx5ZO6czcFpzSEszV2Cy6PnTQLXCS5f7IXZLzwoimYuLal5-mAUYq2Oe7i6231dKSBz_hbuDbWL1tl58yn52NU7csrm5kTESkzV8__MX5XP5Py55fo-4ShbFBtTEfa8-sKxpR83UKUwI_q-ir2G-epRMz4RBEnBcVhHtHwyMlVTuxDvix4UgQL3VmEaHQb72ZGQtSS0AEYHt4_Hj_Jd1aczLQxNyPt_xykOykSdx28Ut5LWRsSCKCNXB16Ye5XqTTVaoHHM4_LlbNBcfQ1OP5jG3enX90O6RqlIsjLnwNaC_x2Kgjk9X1gf7VXPMt8PLqMy1adyRDQIu8UXtcN52owa0sTRoVnYE423QG2u1j_ze9elEeT5pr-nKd3Zm-tWuDzsQqYjbwlx1vyhZfQeAd7FyfGdS310LoaSIaU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9acc6d6680.mp4?token=YRm0sXzjYciWB_3_-ef9pJcSepQptCr77I7hKVr2hiv-CxrUvV-HaCIoLkCnPmPswjLZ8sx8093l6Vur580UeEckkuL7STZ7ojGkjkRLz0weMTz4NMPkfBO-oh0rNbXVsUHTStmJ3oOg5dgb5CU4H13U8gtIRhjBE8xe_kKz48zOeA2IZBfej94Nh8pl5YyrhNbxQd2xeFtSAEBMdORUtEAy_aEMA7UU944mDOkd3Oy62I7XX-i7ve7xfhp5OEItf-IhfLx5ZO6czcFpzSEszV2Cy6PnTQLXCS5f7IXZLzwoimYuLal5-mAUYq2Oe7i6231dKSBz_hbuDbWL1tl58yn52NU7csrm5kTESkzV8__MX5XP5Py55fo-4ShbFBtTEfa8-sKxpR83UKUwI_q-ir2G-epRMz4RBEnBcVhHtHwyMlVTuxDvix4UgQL3VmEaHQb72ZGQtSS0AEYHt4_Hj_Jd1aczLQxNyPt_xykOykSdx28Ut5LWRsSCKCNXB16Ye5XqTTVaoHHM4_LlbNBcfQ1OP5jG3enX90O6RqlIsjLnwNaC_x2Kgjk9X1gf7VXPMt8PLqMy1adyRDQIu8UXtcN52owa0sTRoVnYE423QG2u1j_ze9elEeT5pr-nKd3Zm-tWuDzsQqYjbwlx1vyhZfQeAd7FyfGdS310LoaSIaU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سونامی استعفاء در پلیس رژیم صهیونیستی
🔹
در ادامه بحران‌های داخلی در ساختار امنیتی رژیم صهیونیستی، گزارش‌ها از وقوع موج بی‌سابقه استعفاء در میان فرماندهان ارشد پلیس این رژیم حکایت دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/683679" target="_blank">📅 17:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683678">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgERqAtcUSi1gKJ4gIDoXqAu-DuBdGbmg14SL123ufn3ks0AniU7bgK6hRcIrmUFl7u4ADzL4xMWJo439S5HRVh1HpmDx6uzIEQFLcL-_h-ErUSCHB-bNfkIlnft8iP6frRkXow9cVH4pvXEzWwqLLElQJZLCLG7_H62hzrZJAsakI6uKy5pc3xvdq-qV3T_2RnJQunMkadISkayGvc1eArID8NgKMVc61UT3g9sstdsBJBOeAzik9oLFiwEM6ltRY_mZ7fNN0wEAQM_S35vgPEftdG68IUj4YkgP6Ec4xE6u6ulvKzq3qeKdRffKtbddAE5bLHe4AdElOAzKK4J-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دفاعی از جنس تناقض؛ چرا پرونده پژمان جمشیدی همچنان خبرساز است؟ | مامک جمشیدی چه می‌گوید و چه چیز را نمی‌گوید؟ | کسی که شهرت دارد می‌تواند «عشق و حال» کند!؟
🔹
در ماه‌های اخیر، پرونده حقوقی پژمان جمشیدی، بازیگر سرشناس سینما و فوتبالیست سابق، از یک پرونده قضایی عادی به یک میدان نبرد فرهنگی و اجتماعی تبدیل شده است.
گزارش میثم اسماعیلی دراین‌باره را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3239817</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/683678" target="_blank">📅 17:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683677">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ebc59613b.mp4?token=IFXZow_c-7AfgeEg5jKsQEJspjv9jkRGAqA6upslCcbT19V9XkG47ADu4Ds3qOZy3d8v3Xz4BVnz2b-fIa83miKQmPwjiPz7sLN91-uM2zPrwiUIpe7vgK62HkEh7G2A2SS8zJce9b6_reufrdloQ6chW46q3vYnv8pQgjhNNGvfFqnzlFTImShS2z7u5a70y4EW2C2XaRn3ea3eFT0wrD32D78ZFvmHY9XvnYco0K-JOhjRvkBOLJXR_MJBgAxNSAdsuqnCVoeKMdKC0xOQmB9HfmD1J3rj1dptqq1CNu-CJCFsG9-KXWdVbKEHxwf64nZKK3JgW5sL1R230l1dbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ebc59613b.mp4?token=IFXZow_c-7AfgeEg5jKsQEJspjv9jkRGAqA6upslCcbT19V9XkG47ADu4Ds3qOZy3d8v3Xz4BVnz2b-fIa83miKQmPwjiPz7sLN91-uM2zPrwiUIpe7vgK62HkEh7G2A2SS8zJce9b6_reufrdloQ6chW46q3vYnv8pQgjhNNGvfFqnzlFTImShS2z7u5a70y4EW2C2XaRn3ea3eFT0wrD32D78ZFvmHY9XvnYco0K-JOhjRvkBOLJXR_MJBgAxNSAdsuqnCVoeKMdKC0xOQmB9HfmD1J3rj1dptqq1CNu-CJCFsG9-KXWdVbKEHxwf64nZKK3JgW5sL1R230l1dbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سالروز ازدواج حضرت خاتم‌الانبیاء و ام‌المومنین؛ خدیجه‌کبری‌"صلوات‌الله‌علیهما"
خجسته باد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/683677" target="_blank">📅 16:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683676">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پلیس فتا تهران از شکار هکرهای تلگرام و اینستاگرام بعد از نقض حریم خصوصی ۳۵ شهروند تهرانی خبر داد.
🔹
سوریه: گفت‌وگو با اسرائیل درباره توافق امنیتی به‌زودی از سر گرفته می‌شود.
🔹
میدل ایست آی: ده‌ها پایگاه اروپایی از عملیات آمریکا علیه ایران در جنگ ۴۰ روزه، پشتیبانی کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/683676" target="_blank">📅 16:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683675">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8-X_t6UsYPTZt58Szbc--ktmpTw-BEhABZjYcRsAh9SEiAdrtiwjN0vvceD8N8W2FYvBQ58ch3MixwJ_B-w7-YTEdRO5FTeVaWNUoSM5gHe6mmRHHU9Gki6S39TNNkR2mfz9alyYTltBxc1FLZJtbIWWfZpIj2wStVaUdsYQ89xU4BE8wfbJKwPT11H8e2LqLiqY_7EVGENJ9uDud47FrpK3pDeSa3SSmlMX9cAAGKqwQZBiMo1LVL5WOLt1wdyEiR8gVvy-2BakAyW1BCBAWPPAGL1TwIESLlO7GULWb6TZmRJ8Rpup6Z5g96_M4-3eUdMBHlQU8F6BTIp25dSfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای داشتن موهای پرپشت و بدون ریزش، باید چند نکته را رعایت کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/683675" target="_blank">📅 16:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683674">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f578783ddf.mp4?token=NPzdO8t7WxP742FrJm87Uyv-t2onUcLnWKZwkOIbi1WUZek7nipC6F5R9fd_zv8IsvC-IztN0IAQs3UorISYjISO-zg_2EyJxb6bLjY7Qi91yZok9eY2xOBSbOmQ5Y9eEukxaZEb2XRcPlHXnxgn3V04o7QHb-t6nQ5FJewVIwdi8nMeu1lDe-r5yMFQvpIW3PZqP34LMjeqgiZ6f3sfKf_QOLa0HdmrzrOEzZyiDgY0eD59At-wV5CQ4clCsQk6ppbvApW92AFhngnbT8BPjGZMhgFZ1sKnOH0et2wUZpXr2fDEa3niagDllduKlQZ2AMLoZy3NiYpUD6ZyhQ1o3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f578783ddf.mp4?token=NPzdO8t7WxP742FrJm87Uyv-t2onUcLnWKZwkOIbi1WUZek7nipC6F5R9fd_zv8IsvC-IztN0IAQs3UorISYjISO-zg_2EyJxb6bLjY7Qi91yZok9eY2xOBSbOmQ5Y9eEukxaZEb2XRcPlHXnxgn3V04o7QHb-t6nQ5FJewVIwdi8nMeu1lDe-r5yMFQvpIW3PZqP34LMjeqgiZ6f3sfKf_QOLa0HdmrzrOEzZyiDgY0eD59At-wV5CQ4clCsQk6ppbvApW92AFhngnbT8BPjGZMhgFZ1sKnOH0et2wUZpXr2fDEa3niagDllduKlQZ2AMLoZy3NiYpUD6ZyhQ1o3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعبیر تند اندیشمند سرشناس آمریکایی از ترامپ
پروفسور جفری ساکس:
🔹
سیستم سیاسی آمریکا فاسد و ساختارش فروپاشیده است؛ «یک خودشیفته خبیث» قدرت آغاز جنگ را در دست دارد!
🔹
دونالد ترامپ رسماً و به شکلی بسیار جدی دچار بیماری و اختلال روانی است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/683674" target="_blank">📅 16:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683673">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
جرائم بیمه شخص ثالث از ۲ تا ۱۳ شهریور بخشیده می‌شود
🔹
جرائم وسایل نقلیه فاقد بیمه شخص ثالث از ۲ تا پایان ۱۳ شهریور ۱۴۰۵ به مناسبت هفته دولت و هفته وحدت، به‌طور کامل بخشوده می‌شود.
🔹
این بخشودگی فقط برای خرید بیمه‌نامه شخص ثالث یک‌ساله اعمال خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/683673" target="_blank">📅 16:41 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683672">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZFN3dgqsp8gl-dlQsa0h7E1tE0-trVVqzqVL-eDN6qvtQo3pG9cyBPMq54FH_LrTkOBiuC1xlxs_gFPvAYuQnPldUshOdwpNWb0MACp8u1fCA9XmaKFt-dOo_LZ_IU9Xxa5TjS4r0OPQhcBGLynX6BYsPMYLeiJAJM6zTFbDFo4jAeq3Le7jdE1ebCIDmB2zx-acco5Fw11YWxSaDYA3OVaEC3DFcBSCtfZojHHAlRyzssQH3Hfcm3Q4Gknik7c0wXfqrPI4WDejik-9EPvX6IE3z3P4GWvLHcS2pMRCQpLs1OnsWD68zCSjYbUgNrftqsC_fJoTpCuVggOGIWxGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش سخنگوی سپاه‌ به جنگ اقتصادی ترامپ
؛
برای هر اقدام خصمانه آمریکا سناریو داریم
سردار محبی:
🔹
رئیس‌جمهور آمریکا می‌گوید دستور جنگ اقتصادی را صادر و شدیدترین جنگ اقتصادی علیه ایران را شروع کردیم. این اعتراف ضمنی به شکست مفتضحانه دشمن در عرصه نظامی است.
🔹
اگر در عرصه نظامی پیروز می‌شدید، لازم نبود جنگ اقتصادی را آغاز کنید. مگر جنگ اقتصادی تازگی دارد؟ ۴۷ سال است جنگ اقتصادی می‌کنید و همه ارکان اقتصادی ما را تحریم کرده‌اید. کار فعلی دشمن فقط ادراک‌سازی و ایجاد باور برای مردم است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/683672" target="_blank">📅 16:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683671">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
حمله پهپادی یمن به مواضع مزدوران سعودی
🔹
برخی منابع خبری گزارش دادند که نیروهای مسلح یمن در تازه‌ترین عملیات تهاجمی خود، مواضع و تجهیزات مزدوران وابسته به رژیم سعودی را با استفاده از پهپادهای تهاجمی در استان الضالع هدف قرار دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/683671" target="_blank">📅 16:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683670">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26b72c5b22.mp4?token=UBBISplgumnkMs7LUXvcN7fduQoGT6WnbssGv5ZY1YJdbIuwum4eTlAeaW5SdOGTkIs1sQSufdo2LB3KNEVaVVvUNeeqKMmYbrS0OWZCyuuD9sJjejBMV8zx1mi75rfCGEVNbBtmNiZwjKNgDipspl-gWfqcdkjvjQHKpfeTi4iFbZI7YC19j9jvn2kItnBdj6X0LWKzr0ejk6H0UIFgJE8Di2nMTKVU8s-iTvCY36EBI3mkUDJvnWK8ofx2_U1SG0_C3hHgdmxYzEQOVgdHzb5Fq8j-3wo10laSuHn7eew6NLJsok6yJY-Gye79avtzpDLEnuPGQKgPk8YkxumOjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26b72c5b22.mp4?token=UBBISplgumnkMs7LUXvcN7fduQoGT6WnbssGv5ZY1YJdbIuwum4eTlAeaW5SdOGTkIs1sQSufdo2LB3KNEVaVVvUNeeqKMmYbrS0OWZCyuuD9sJjejBMV8zx1mi75rfCGEVNbBtmNiZwjKNgDipspl-gWfqcdkjvjQHKpfeTi4iFbZI7YC19j9jvn2kItnBdj6X0LWKzr0ejk6H0UIFgJE8Di2nMTKVU8s-iTvCY36EBI3mkUDJvnWK8ofx2_U1SG0_C3hHgdmxYzEQOVgdHzb5Fq8j-3wo10laSuHn7eew6NLJsok6yJY-Gye79avtzpDLEnuPGQKgPk8YkxumOjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر کنجکاو هستید بدانید سوپاپ زودپز چطور کار می‌کند این ویدیو را ببینید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/683670" target="_blank">📅 16:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683668">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2358d2fbe1.mp4?token=nIRB5QywmghbL3BZcYDHNh9i2VasNRkbs0s4aDoiC7M0mhJGKlZIW33f1g1OqNtw6fwGhPL8B7_pvHQfddHPY6dqowsGE0PPmhseR4HD5SKvki5Pj74b0hvuElmbiOejNrMeuAA3iWYdj4ak6go7t-XDK4yekmFIkIFlfbYja8vJLwJA5X0RJdOfDRD0CQUoIRQua6H0ZH29_FZBAqqfAMFVKlVl0WGaKl02Za9Oyz99n5NTeuT1U6tP88j_PTIASkpYkC7caAdYwm1wZPYBoCJSkd7kOAp0LRGouC3fbSBKl8WvGetFvI-xzNWx95LcVZxjc1LWwwdiUb9rwBQ-VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2358d2fbe1.mp4?token=nIRB5QywmghbL3BZcYDHNh9i2VasNRkbs0s4aDoiC7M0mhJGKlZIW33f1g1OqNtw6fwGhPL8B7_pvHQfddHPY6dqowsGE0PPmhseR4HD5SKvki5Pj74b0hvuElmbiOejNrMeuAA3iWYdj4ak6go7t-XDK4yekmFIkIFlfbYja8vJLwJA5X0RJdOfDRD0CQUoIRQua6H0ZH29_FZBAqqfAMFVKlVl0WGaKl02Za9Oyz99n5NTeuT1U6tP88j_PTIASkpYkC7caAdYwm1wZPYBoCJSkd7kOAp0LRGouC3fbSBKl8WvGetFvI-xzNWx95LcVZxjc1LWwwdiUb9rwBQ-VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسئول کانادایی: توافق با آمریکا دوام نمی‌آورد
🔹
پس از شکست ماه‌ها مذاکرات کانادا و آمریکا و توسل واشنگتن به جنگ تعرفه‌ای، نخست‌وزیر استان بریتیش کلمبیا در کانادا دیوید اِبی گفت: «نمی‌توان به ترامپ اعتماد کرد.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/683668" target="_blank">📅 16:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683667">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/259fa82692.mp4?token=FJhBmuFee0noUMJuK8n5LxfuyWQ8zkCEIgi2_Aafn6xqcT8jQm8pkC2KUTdznFDqy3Kx5aUi3oCBKsXk3wVviI2yS_wUdQN5_2e1_JdqJyL1pAh0bWa5rrW2Ew3K8GRkE0dYgkkqM01oV8VHQX0RgaVljjfWD1-MLb8aigW52VwPZoKPDRP_CYl_TANubBUssRwtZBoXF09qgKdDNLYM01V6nNMVn0zxv8sOsU1zpzNOyhQuOEWhPh01V4SkWrKawVdTnsbPQGkLBVl_uZo5FFIXYnPIY73OCPSya5cPXOHzSWe5VTXqpQ-UDjxHQtk3zBB0JPX0HLoHZH1CmSPnuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/259fa82692.mp4?token=FJhBmuFee0noUMJuK8n5LxfuyWQ8zkCEIgi2_Aafn6xqcT8jQm8pkC2KUTdznFDqy3Kx5aUi3oCBKsXk3wVviI2yS_wUdQN5_2e1_JdqJyL1pAh0bWa5rrW2Ew3K8GRkE0dYgkkqM01oV8VHQX0RgaVljjfWD1-MLb8aigW52VwPZoKPDRP_CYl_TANubBUssRwtZBoXF09qgKdDNLYM01V6nNMVn0zxv8sOsU1zpzNOyhQuOEWhPh01V4SkWrKawVdTnsbPQGkLBVl_uZo5FFIXYnPIY73OCPSya5cPXOHzSWe5VTXqpQ-UDjxHQtk3zBB0JPX0HLoHZH1CmSPnuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قبل از خرید و سرما‌یه‌گذاری روی ملک، حتما این سه سوال رو‌ از مالک بپرس تا سرت کلاه نره #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/683667" target="_blank">📅 16:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683666">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی فیلیمو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cae100903.mp4?token=iQ8q8rGE8pAPSHpHclEifHPCDaj1tNRRCNTs1k0azMplCA1_Nnxg3Pe6bUa6uoyJnDinBx3pMTx22Rv1_zyOLTUu65Penj9AGZ15bwrnAXCbE04D3_e5gRGXK-KOsAYceY7xXv-daiW3i5PL3Kqd0ug3wdTnlOlFmc5IlsmnEUIXafmPW6WMFg6LDCdcEin_g_KsZjSOLiyUP-r0mxy35x8jcBdMAUNHliMwSlMDsoiWrHMyqyCSIGXm1r7U1wiIoKhXuhAPK4UPH3YS0sx8AqP5HgoabwNQ98EX9FvKDp-ByIVUbHYKX_gVpkDxSm4YdriJNBKEWOxgdByDiwm58YZX-iU4QSlOXWO4s_aWGFKOQUsRtbeMzr1M6nkbpS4iTvEffOpnLitE6n-qkaT-R5NpExIHxzDfZugtKR7WxAFUWOY-E8etwwNQ8DArBS9z1kpQhIwjnSCfuctymo6CrqoK1yrCqRDT0i3EPcsGO7zXMvcodK7QH1Hnhl0xfcPQW6zIsJ5aMkUubOWwrr4-vvqzDK7Q8e66DleNFLIcPVGoOwrBdvqRu8iInkUOZiKXxBa6df7yXZPXiiJdgZvIEamLTHOKbMed9XfPtWOFxhQlF1GDfKyDvY5-bRq_EGGPfDMLE0xoZZJqUju_8wRF6nEQT-y0PGCZTU852AvWzU8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cae100903.mp4?token=iQ8q8rGE8pAPSHpHclEifHPCDaj1tNRRCNTs1k0azMplCA1_Nnxg3Pe6bUa6uoyJnDinBx3pMTx22Rv1_zyOLTUu65Penj9AGZ15bwrnAXCbE04D3_e5gRGXK-KOsAYceY7xXv-daiW3i5PL3Kqd0ug3wdTnlOlFmc5IlsmnEUIXafmPW6WMFg6LDCdcEin_g_KsZjSOLiyUP-r0mxy35x8jcBdMAUNHliMwSlMDsoiWrHMyqyCSIGXm1r7U1wiIoKhXuhAPK4UPH3YS0sx8AqP5HgoabwNQ98EX9FvKDp-ByIVUbHYKX_gVpkDxSm4YdriJNBKEWOxgdByDiwm58YZX-iU4QSlOXWO4s_aWGFKOQUsRtbeMzr1M6nkbpS4iTvEffOpnLitE6n-qkaT-R5NpExIHxzDfZugtKR7WxAFUWOY-E8etwwNQ8DArBS9z1kpQhIwjnSCfuctymo6CrqoK1yrCqRDT0i3EPcsGO7zXMvcodK7QH1Hnhl0xfcPQW6zIsJ5aMkUubOWwrr4-vvqzDK7Q8e66DleNFLIcPVGoOwrBdvqRu8iInkUOZiKXxBa6df7yXZPXiiJdgZvIEamLTHOKbMed9XfPtWOFxhQlF1GDfKyDvY5-bRq_EGGPfDMLE0xoZZJqUju_8wRF6nEQT-y0PGCZTU852AvWzU8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#
فیلیمو
رو نصب کن
😍
۱۰ دقیقه تماشا کن
🍿
سفر استانبول ببر
✈️
فقط تا ۲۰ شهریور فرصت داری جزو برنده‌های ۱۰ سفر استانبول و ۱۰ سفر باتومی باشی؛ اونم با امکان سفر با هم‌سفرت و دریافت ۵۰۰ دلار وجه نقد!
💰
⛱️
r.filimo.com/Tsummer1405
@filimo</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/683666" target="_blank">📅 16:02 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683665">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8e1AiH4rPm9Gov2POrSD72JDX3unHwnkB1LQw5MklLos2NHbqmvlRtV4A4aI8JR8OADSivSUTfpyiWEAB0Nkc0Fz_AVreaRo92VL7D_9TVbh6X5xrZKzUNHgUrSt8WjTB7GDTKuy369TFmNRHx87fyF70YIMnq217YEnASEFhXITxJYodCbgoRgCKOZ_GEXmWzvib7Yh9B6agiQIuRTJ6cH5ICBTv6mbHmOj_Rrx_wfqF6VnQkGmjnY-TVmShFlfqIZi0Kqkpn9U2-Q4OAq6z5yaNN4R0a-jFmvTaPtSFYIpJwZ1_YwKtLl10oj4xt4HIURGC8cO3Ka7FG2Ouvamw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
روایت ناقص و غیرمنصفانه رسانه ملی از بیمه سینا
🔰
هلدینگ مالی و سرمایه‌گذاری سینا با انتقاد از نحوه طرح برخی مطالب درباره بیمه سینا در یک برنامه تلویزیونی، تأکید کرد: ارزیابی عملکرد یک شرکت بیمه باید بر مبنای صورت‌های مالی، اطلاعات رسمی منتشرشده در سامانه
#کدال
و شاخص‌های تخصصی صنعت بیمه انجام شود.
بر اساس گزارش منتشر شده در سامانه کدال،
#بيمه_سینا
در سه‌ماهه نخست سال ۱۴۰۵ حدود ۶۷۰ میلیارد تومان سود شناسایی کرده است.
📎
مشاهده خبر
🔘
روابط عمومی هلدینگ مالی و سرمایه‌گذاری سینا
🔘
🌐
سایت
📱
بله
📲
ایتا
📲
تلگرام</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/683665" target="_blank">📅 16:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683664">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93519f61b6.mp4?token=f8GQz1rd0paw5QEjXUYJDQrzixTzE3EYHeBUXkJcFCybrgzsxdbGNbbdV9GtJ1Tj3_TCx6C_Gvsvli-a9wHsx15OhtiY65MH_wEGLB5fdiLwUj7twKuyWML07aCDzM8iD6XQf8XDVjIFG_WAfEPHMRFklrA2ykfepM0uGnSvKeO0B6Cm9iqn-r-c1CP2TUHWaXcSKk0xHCO79hvFj2KjgHfzlWofxgZJtK18W-0Ps3nZkzSikKRSNZzP8euxflSvAJ4A9l43m6LGOzFe-p_EnRAndfrpqEFYsvxiHp_FBOxYi7weonwkRvSL_V3qVaci6eQo8-hLH-Blt7cQhnb-_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93519f61b6.mp4?token=f8GQz1rd0paw5QEjXUYJDQrzixTzE3EYHeBUXkJcFCybrgzsxdbGNbbdV9GtJ1Tj3_TCx6C_Gvsvli-a9wHsx15OhtiY65MH_wEGLB5fdiLwUj7twKuyWML07aCDzM8iD6XQf8XDVjIFG_WAfEPHMRFklrA2ykfepM0uGnSvKeO0B6Cm9iqn-r-c1CP2TUHWaXcSKk0xHCO79hvFj2KjgHfzlWofxgZJtK18W-0Ps3nZkzSikKRSNZzP8euxflSvAJ4A9l43m6LGOzFe-p_EnRAndfrpqEFYsvxiHp_FBOxYi7weonwkRvSL_V3qVaci6eQo8-hLH-Blt7cQhnb-_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیلوستر استالون در ۸۰ سالگی همچنان بدون بدلکار فیلم بازی می‌کند
🔹
پشت‌صحنه فیلم جدید سیلوستر استالون نشان می‌دهد این بازیگر ۸۰ ساله همچنان برخی صحنه‌ها را بدون استفاده از بدلکار اجرا می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/683664" target="_blank">📅 15:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683663">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
از این پس برای پرداخت مهریه بیشتر از ۱۴ سکه فقط ملائت زوج ملاک است
🔹
با رای نمایندگان مجلس شورای اسلامی هرگاه مهریه در زمان وقوع عقد تا ۱۴ سکه تمام بهار آزادی یا معادل آن باشد وصول آن مشمول مقررات ماده (۳) این قانون است؛ چنانچه مهریه بیشتر از این میزان…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/683663" target="_blank">📅 15:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683662">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff65586258.mp4?token=fBRZs7Jg3uvbuy_wicqmp7rC2c-oTIa_3wdmwMSbhTvb0cO07DLVszC9NV2x8GqguPgkZITlEqqxgOy1x6H1NxRC0xX4EuoVAc6c9BHWWz_evrYCkGuGkcHSMfEM0IZ33_92legYmynOI7SUBEc-aEC1ksKv5L8TBqRWZ-YpHonjzUVVa0PxYLRxLIYjJVyeZOgvjoIf5MNnZXwfDjHs1fkVdON0whreuhc9p1t-7D8syHzUTodjhaXWcvVfA2ZxEbiHIlYRI_hNucF_BcxzaXfB8gOnJTvHfjoluPVwB7v4d0BMBlLnz1oH4K6979W7I93di4IpijWuPlilUuAfKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff65586258.mp4?token=fBRZs7Jg3uvbuy_wicqmp7rC2c-oTIa_3wdmwMSbhTvb0cO07DLVszC9NV2x8GqguPgkZITlEqqxgOy1x6H1NxRC0xX4EuoVAc6c9BHWWz_evrYCkGuGkcHSMfEM0IZ33_92legYmynOI7SUBEc-aEC1ksKv5L8TBqRWZ-YpHonjzUVVa0PxYLRxLIYjJVyeZOgvjoIf5MNnZXwfDjHs1fkVdON0whreuhc9p1t-7D8syHzUTodjhaXWcvVfA2ZxEbiHIlYRI_hNucF_BcxzaXfB8gOnJTvHfjoluPVwB7v4d0BMBlLnz1oH4K6979W7I93di4IpijWuPlilUuAfKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دست از خیال‌پردازی برای تنگه هرمز بر نمی‌دارد
🔹
رئیس‌جمهور آمریکا بار دیگر با انتشار تصویری از خلیج فارس «تنگه هرمز» را «قلمرو جدید آمریکا» نام نهاد.
🔹
این توصیف طی روزهای گذشته موجب تمسخر و انتقادات زیادی در محافل آمریکایی شده است.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/683662" target="_blank">📅 15:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683661">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: تولید روزانه ۳۰ رهگیر ۵ هزار دلاری برای مقابله با پهپادهای ایرانی در امارات
🔹
طبق این ادعا، یک شرکت آمریکایی در امارات روزانه ۳۰ رهگیر پهپادی با قیمت حدود ۵ هزار دلار تولید می‌کند؛ این رهگیرها بر اساس طراحی اوکراینی ساخته شده‌اند و فرزندان دونالد ترامپ از سرمایه‌گذاران این شرکت هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/683661" target="_blank">📅 15:39 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
