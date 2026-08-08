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
<img src="https://cdn4.telesco.pe/file/J8IxcF3Zwm8Ojarnvm1ae3xWLf7VlzbJI4GjVPXIa7HQTnX_Neqzi-e81tS4mjBc0z7tcdd5KWI8qHe_IBjqQWn9CSmKHjvXIWcDBqW0tyjI4hdrmk2KWTc5jhmZL9yOoqaszYK6lk30l8LhAAfPdaOXEbb7EhslnxsENDBxKf2STBT80Ic_WMggLwe6Tw6JR0-fHvlHNSuqefa22gDa2tcDJby0SYBfSx5f5SLHRcRVHsjq3NOWn2bfoULKGBsaWdlKPPyLBBoHl5lb-bZ1RBNHe0givbeMe4LLABBrr7ybd7n7W7dDy4SJ94nmc73du9d5YfNzRO7EJxmnta6iYQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 17:34:53</div>
<hr>

<div class="tg-post" id="msg-679450">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
۵ تا ۱۰ هزار کشنده وارداتی پشت مرز ترکیه بلاتکلیف ماندند
،عضو کمیسیون عمران مجلس:
🔹
حدود ۵ تا ۱۰ هزار کشنده با مجوز کلی دولت قبل برای نوسازی ناوگان وارد شده‌اند، اما به‌دلیل نداشتن ثبت سفارش در مرز ترکیه متوقف و در آستانه مصادره هستند.
🔹
وی خواستار تصمیم فوری دولت برای ترخیص این خودروها شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/akhbarefori/679450" target="_blank">📅 17:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679449">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ls_TJVeRyIXWfLL660zh3RusNTxCfgYu1_W0f9wRiJfaCPLCCQB2rNhNButZqiYllOX3I0J-B79BMghO5vU5SHvkrIneddPjqrA1YAjLOvBTvzcLYduFpzhEHSykd39bg1zb2hbu0PjxY7NPb_dLp_2iJmO2erugqwyPSkdkmnsv5B0G6CoWre_l5t288OAMnWdD3ki4ciGH78fH60muHt_5bQ6F7l1xuCKz8y3wZWPM8NAHeV5ZlgALtqgd6YuUGyhiATPACgp6JC48yzb4aG8d26ADEVOCU7x7WbHoOzNyYUHDPWqh8btleKNkXYmEhpwXSnRBCYGaDWMNbxwb7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعلام کشته شدن رئیس ستاد مشترک مزدوران سعودی در مأرب یمن
🔹
وزارت دفاع دولت مزدور و سرسپرده عدن از کشته شدن صغیر بن عزیز رئیس ستاد مشترک مزدوران سعودی در حملات موشکی دقیق اخیر نیروهای مسلح یمن به اردوگاه مزدوران خبر داد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/akhbarefori/679449" target="_blank">📅 17:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679448">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b0cc564f9.mp4?token=gDTCVOwnKoly03m5fMmzKseuuPsh06CIeD2xsG4zaoELbgJSuR980hXZwDKzFWQpBbPIN-pBPyiXhIYRtA_8K3BoGBulAfv4kC7PNm7kStvYfTfSq96jSxDyraxhdl3ALzhyALi9Mn2QjNsAomQKJmoGfGdGkyyTBn-u05f4c04LxGIsn7-Y1QfvEywlRTpHLhBdcDed3emqQAw9BCM_55093hREfYd0MqDck2Ajo74Bsm3kZldI4twuVywr45hNFSpvbQZPysvU83GcZf7_b2aaBs8TbphyLOb94Jdqkx-un2v8aFcd7y4P17AoKedYElH3_xkSQ9lr9MF84C0eqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b0cc564f9.mp4?token=gDTCVOwnKoly03m5fMmzKseuuPsh06CIeD2xsG4zaoELbgJSuR980hXZwDKzFWQpBbPIN-pBPyiXhIYRtA_8K3BoGBulAfv4kC7PNm7kStvYfTfSq96jSxDyraxhdl3ALzhyALi9Mn2QjNsAomQKJmoGfGdGkyyTBn-u05f4c04LxGIsn7-Y1QfvEywlRTpHLhBdcDed3emqQAw9BCM_55093hREfYd0MqDck2Ajo74Bsm3kZldI4twuVywr45hNFSpvbQZPysvU83GcZf7_b2aaBs8TbphyLOb94Jdqkx-un2v8aFcd7y4P17AoKedYElH3_xkSQ9lr9MF84C0eqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمرین سخت جراحی با بادکنک
🔹
جراح با دقتی بالا، بادکنک را بدون ترکاندن بخیه می‌زند؛ تمرینی برای تقویت مهارت‌های ظریف جراحی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/akhbarefori/679448" target="_blank">📅 17:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679447">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
سرنوشت تجمعات شبانه بعد از ماه صفر چیست؟
قائم مقام سازمان تبلیغات:
🔹
ادعای تعطیلی تجمعات بعد از ماه صفر صحت ندارد؛ همه ساعت‌مان را با ولی‌فقیه تنظیم‌ کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/679447" target="_blank">📅 17:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679446">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Asy0_ymxvMkFfzpDNrIKKgi73OHSBc_f5Lky5ow_jgzdWQqR38zhgFCSw_6azxS62ZSMDx7yNwQ1sBQwLTShL42_zTHBzLE2_uXcdRQh_Yit5tvPEhTNd9E2ZwEC59jDIdKZ282bMbLU85eKB3MIbjQAQPyrgkDy6uwTyNnzLd_Mm1PJqvernGH9lAE3eHHz4xNWsnZaxogiweD76YC4V7cSXo7st_PIqcUWU9ASWek2e09-lXx_x4SO3VdRBDXsnt-VGv7T3JKi_CDELvscfg-xOyE2_N3rP1iHX--KaYgNyArHxog9ZYlXOMrQM9HJ2sNit0XaH41VYP87cr0BMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: تا آمریکا رفتارش را تصحیح نکند، تنگه هرمز باز نخواهد شد
🔹
شورای عالی امنیت ملی هرگز کوتاه نخواهد آمد؛ چه در جنگ و چه در مذاکره.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/679446" target="_blank">📅 17:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679445">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwRw903s-4B5s1047biwyFSybGZHku-vwE4eQxXgfsEnWGQFRQ1ebg-qjHGQFhv_PNMdbiq5sVmOzYp88NY0sGQI6wLOVvuS9vlEw8z_OXyxusTJvFh3M4orBxabPA3I_kxGSv5E47pOTWfqEZEbKrVoU3zpe0Q1EfIU8F6KAgNGCHbV0UfDOP9zZa_tApclBPYNjQVn8MilVhr8AX_GwZjq0k5A0YkGCRphEgYPj-JAY9ze-ZVQoZmCZk6f6CP6bxq9wWXn6K_RDuZmvgaxcf7lnRRobznlnsZm56jRIvalo5P7WnQQ4wMG2XkBkV_J0AW9LPWzjcg5lXvXO2wB4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واضح‌ترین تصاویر خورشید، یک راز ۱۵۰ ساله را آشکار کرد
🔹
تصاویر جدید از سطح خورشید، برای نخستین‌بار هزاران گرداب کوچک را نشان داده‌اند؛ پدیده‌ای که دانشمندان حدود ۱۵۰ سال پیش آن را پیش‌بینی کرده بودند.
🔹
این کشف می‌تواند به شناخت بهتر انفجارها و فعالیت‌های خورشیدی کمک کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/679445" target="_blank">📅 17:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679444">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| نَبض تهران |</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ju1i9J7w5DEe49eT8D2i9IQA-U50JXL5J3bdOqrKvOoGvcQukvdnOBjkPQJRY5Eru5-4Uf694fZsr_6t5ea43DvmkhLrrdnbaMsyAodiH-YX5m871a7VOncnCIP0aM3OSmwR8BDj3jzebGzjuMKUxVPOT17kSWbbEjfAvULLSj8Qe4cEeprb7z0CaMaBgZV9namIAsCVdTXkSRkPsofqBh08Odd9GgpRnww7buQV0OtUemDN1Ku5fs_s0qsicdMf8ZB95SPvmEBGbiMg6CGJs0gMscgUVR6GgZfOaMrPXrTFakqa40L2AEB8RoT7EEQJkpYtornapxu5MtOQas9sHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عامل افزایش قبوض برخی مشترکان، عبور از الگوی مصرف در تابستان است/ افزایش تعرفه نداشتیم
🔸
مدیرکل دفتر مدیریت انرژی و برنامه‌ریزی امور مشتریان شرکت توانیر با تشریح دلایل افزایش محسوس قبض برق برخی مشترکان در روزهای اخیر اعلام کرد: در شرایط عادی، برای مشترکانی که الگوی مصرف را رعایت کرده‌اند، افزایش نرخ برق نسبت به سال گذشته افزایش محسوسی نداشته و آنچه موجب افزایش چشمگیر مبلغ قبض شده، عبور از الگوی مصرف است.
🔗
‌
مشروح خبر
🆔
@tavanironline
🆔️
@tvedc</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/679444" target="_blank">📅 17:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679443">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNeG3EWKBSUjSy7mpz9c_C5ul-XjA1WMrj0SrvaE8AVFgqJfs1Td8RetUDmGZPlX7dkxdzKT1zL5GN8v3SXhc0-PrT3iHoVnzvPpoJkExTFnK85DxrkWEkodRlvcFaOhhi_qOP9O2fOlzdJcQnuTEbINddBufwVz4DGorJD5azgLlhhcGDaRVwDHEyKlf9eZ-i5LKGLfmRy1s1hvDOtIRUZDm9WsMcNkqV3e4M3vr4tvu8tDpAuALzVufz6FDFB6Xx4y5PbkNyGpmFi-BXofT3P-FDLTjTgH5byCy89OGcf-4hIMpC6RtJOvQyYE4JTTHsemFq0Qdbh1N1qf0pgj5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از قتل «حمیدرضا رجب‌زاده» چه می‌دانیم؟
🔹
جست‌وجو در میان پست‌های منتشرشده در توییتر نشان می‌دهد، حداقل از روز ۸ مرداد اکانت‌هایی مربوط به جریان هوادار رضا پهلوی و سلطنت‌طلبان، از انجام قتل یک مداح خبر داده و از مقتول نام برده بودند. ماجرا چیست؟
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3236375</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/679443" target="_blank">📅 16:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679442">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
حملات مجدد ارتش یمن به اردوگاههای مزدوران سعودی در «مأرب»
🔹
شبکه خبری العربیه به نقل از دولت وابسته به عربستان سعودی در یمن خبر داد این حملات، با چند موشک و پهپاد انجام شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/679442" target="_blank">📅 16:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679441">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toP8epTuIvmxp_41KkOLcFji2nD6BuoLhZxSDOP0ZsoMUOkYkJIeLKCYOI3JqHugOqhXrGMunuavTYl05pbNqfXO_xAxrcDuY8Fomy89sraF8ss5rZ_c2LAyRzvC06ZaP115IXdkoMZ4t4kQME1NGqdIGFRGb6cr1fst2D_dst1NIOkztNVbRL2_jcTlS9LTzRy5-YC0-nWmlYyLp9-qrPbxR2nH0_weJC_ugrpQ7Z5jMjTq_l9qYpi3qgz72AgKFL4YGOmhzglBxX1-Ox68AV-Vq3hC7GkS2B3rMBPmGmEFD702Bk6xsCg9b6H_300OnoxhP5_XBCm5i5HpUmdv5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله به یک کشتی در سواحل عمان
سازمان عملیات تجارت دریایی انگلیس:
🔹
یک کشتی در ۱۸ مایلی خصب عمان هدف یک پرتابه قرار گرفته و این حمله باعث آتش‌سوزی در داخل کشتی شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/679441" target="_blank">📅 16:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679440">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7815beadc2.mp4?token=n7L5OOu81nkytbxBki6kB_UMMl017YqxVqyGYlkiLnN3HQrIPM7TyPCM18bGnW3nlJGpoZ7qHbSX0PcJkO1Ohhcd7U-wQmXoqfQTeNp5tCZPL-5UFvAt74FjVfm4AhZxgyK77mVhei8zHrI8Rptvh4o9-k2NPN3cK7fZoiKX87qV04sywGiYHRk5fN-pnTzmmayUkIdpS9xxVYzY_5L9aFImahjzHEXyqQ7hQUbLsWU1ygqoH05ZBJ4Ap-qXNGGWvT9kPR-0k2PXnZVrTinDB3bTi7L2pSDIBJFZnLGbbACuAjJNOM64lP9JSIREdNb-4Z62_Xo1kLpaoO9yERSNFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7815beadc2.mp4?token=n7L5OOu81nkytbxBki6kB_UMMl017YqxVqyGYlkiLnN3HQrIPM7TyPCM18bGnW3nlJGpoZ7qHbSX0PcJkO1Ohhcd7U-wQmXoqfQTeNp5tCZPL-5UFvAt74FjVfm4AhZxgyK77mVhei8zHrI8Rptvh4o9-k2NPN3cK7fZoiKX87qV04sywGiYHRk5fN-pnTzmmayUkIdpS9xxVYzY_5L9aFImahjzHEXyqQ7hQUbLsWU1ygqoH05ZBJ4Ap-qXNGGWvT9kPR-0k2PXnZVrTinDB3bTi7L2pSDIBJFZnLGbbACuAjJNOM64lP9JSIREdNb-4Z62_Xo1kLpaoO9yERSNFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور بعضی از خرید‌های ساده به‌جای این که پولدار نشون‌مون بده، تبدیل به یک سقوط مالی میشه؟
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/679440" target="_blank">📅 16:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679439">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
پزشکیان: ممکن است کسی بگوید قبلا چیز دیگری می‌گفتید، چرا این‌گونه شد؟ خب، حمله کردند
🔹
کارخانه‌هایی که مورد حمله واقع شدند، نیروهایی که بیکار شدند و خسارت‌هایی که وارد شده است، وقتی کنار هم قرار می‌گیرد، ابعاد مسئله مشخص می‌شود. بعد ممکن است کسی بیاید و بگوید شما قبلا چیز دیگری میگفتید، چرا این‌گونه شد؟ خب، حمله کردند و این اتفاق افتاد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/679439" target="_blank">📅 16:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679438">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
تصاویری از عرشۀ کشتی متخلف که توسط نیروی دریایی سپاه پاسداران متوقف شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/679438" target="_blank">📅 16:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679437">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
پزشکیان: آنها طبق تفاهم‌نامه، می‌بایست بر اساس دستورالعمل‌هایی که جمهوری اسلامی با کشور عمان با هم می‌نویسند، عمل کنند، عمل نکردند و ما هم پاسخ دادیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/679437" target="_blank">📅 16:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679436">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/956bb4711e.mp4?token=akrBWN4vYoAXF6_uQZ5-B7T4IIGVgObh3lNCJMR_eAJZcdFoQ4t78HUfRvCLtrwWku0sG1yaUrdGfvpiablx39g5P-OcUOvRkVV65cVOd6VAhPd-JjrLsfjlQVlQIgxRLwKL5rGngjJQ1v1oF-jnpQOZMEHQs8mW90m0f34IO45r5e27VtE9YCgmbwbrxkyt9ZDUk0uS_CznK7si9xof0sPCGs2Q2DYrZAhNx_Pi4lNuenmb_Zz24M_hrxtk_ReQwmzgk6OAnPiysXzBGg1s6tnHoSY0ni38ttHtBMCFenKVdkC82za6QkGdMFu9oTSNkSFiNGThQ_Gn9cUV8UxReg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/956bb4711e.mp4?token=akrBWN4vYoAXF6_uQZ5-B7T4IIGVgObh3lNCJMR_eAJZcdFoQ4t78HUfRvCLtrwWku0sG1yaUrdGfvpiablx39g5P-OcUOvRkVV65cVOd6VAhPd-JjrLsfjlQVlQIgxRLwKL5rGngjJQ1v1oF-jnpQOZMEHQs8mW90m0f34IO45r5e27VtE9YCgmbwbrxkyt9ZDUk0uS_CznK7si9xof0sPCGs2Q2DYrZAhNx_Pi4lNuenmb_Zz24M_hrxtk_ReQwmzgk6OAnPiysXzBGg1s6tnHoSY0ni38ttHtBMCFenKVdkC82za6QkGdMFu9oTSNkSFiNGThQ_Gn9cUV8UxReg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جان بولتون: پوتین احساس می‌کند ترامپ در جنگ با ایران ضعیف و ترسیده شده است،روسیه آماده حمله به ناتو است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/679436" target="_blank">📅 16:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679435">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ترکیه عبور کشتی‌ها به دریای سیاه را محدود می‌کند
بلومبرگ به نقل از منابع آگاه:
🔹
ترکیه در پی افزایش حملات پهپادی، عبور کشتی‌های تجاری از تنگه داردانل به دریای سیاه را محدود کرده است؛ اقدامی که همزمان با اختلال در عرضه نفت و کاهش تردد از تنگه هرمز می‌تواند مشکلات بیشتری برای تجارت جهانی ایجاد کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/679435" target="_blank">📅 16:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679434">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
پزشکیان: رهبری هر تصمیمی بگیرد، ما تا آخر ایستاده‌ایم  رئیس‌جمهور:
🔹
تصمیم درباره جنگ با فرماندهان و رهبری است و دولت وظیفه تأمین تدارکات را دارد.
🔹
هر تصمیمی ایشان بگیرد، ما تا آخر ایستاده‌ایم و از جنگیدن و ماندن نمی‌ترسیم و تا پای جان ایستاده‌ایم.
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/679434" target="_blank">📅 16:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679433">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
پزشکیان: رهبری هر تصمیمی بگیرد، ما تا آخر ایستاده‌ایم
رئیس‌جمهور:
🔹
تصمیم درباره جنگ با فرماندهان و رهبری است و دولت وظیفه تأمین تدارکات را دارد.
🔹
هر تصمیمی ایشان بگیرد، ما تا آخر ایستاده‌ایم و از جنگیدن و ماندن نمی‌ترسیم و تا پای جان ایستاده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/679433" target="_blank">📅 16:09 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679432">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
اعلام کشته شدن رئیس ستاد مشترک مزدوران سعودی در مأرب یمن
🔹
وزارت دفاع دولت مزدور و سرسپرده عدن از کشته شدن صغیر بن عزیز رئیس ستاد مشترک مزدوران سعودی در حملات موشکی دقیق اخیر نیروهای مسلح یمن به اردوگاه مزدوران خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/679432" target="_blank">📅 16:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679431">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
پزشکیان: کافی بود هر کدام از این‌ها ساز مخالف بزنند و عده‌ای را در کشور در مقابل این اقدامات قرار دهند. همین حرف‌هایی که امروز درباره سختی‌ها و گرانی‌ها گفته می‌شود، می‌توانست بزرگ‌نمایی شود و مردم را به اعتراض وادار کند؛ اما همراهی و همدلی این جریان‌ها…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/679431" target="_blank">📅 16:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679430">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
پزشکیان درباره آینده قیمت بنزین: هرگونه تصمیم مهم اقتصادی و اصلاحی باید با اطلاع‌رسانی و همراهی مردم انجام شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/679430" target="_blank">📅 16:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679429">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
جهانگیر: خرازی به دادگاه ویژه روحانیت احضار شد  سخنگوی قوه قضائیه:
🔹
با توجه به روحانی‌بودن باقر خرازی، پرونده او در صلاحیت دادگاه ویژه روحانیت است و اقدامات قانونی برای تعقیب کیفری وی آغاز شده است.
🔹
خرازی امروز به این دادگاه احضار شده و جزئیات پرونده پس…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/679429" target="_blank">📅 16:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679428">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
پزشکیان: ما تصمیم گرفتیم اینترنت باز شود/ دستگاه‌های امنیتی تهدیداتی را در این رابطه ملاحظه می‌کنند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/679428" target="_blank">📅 16:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679427">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
پزشکیان: راه ما را بسته‌اند. ما کالا را ارزان می‌آوردیم و از مسیرهای راحت وارد می‌کردیم، اما اکنون باید مسیرهای مختلف را طی کنیم و از راه‌های گوناگون کالا را وارد کشور کنیم و به این سادگی نمی‌توان این کالاها را وارد کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/679427" target="_blank">📅 15:52 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679426">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
پزشکیان: دغدغه و نگرانی من، معیشت مردم است  رئیس جمهور:
🔹
واقعاً این دغدغه، دغدغه‌ای به‌حق است و اگر ما نتوانیم مشکلات معیشت مردم و سلامت مردم را حل کنیم، بقیه کارها نتیجه‌ای نخواهد داشت.
🔹
حتی پیش از جنگ نیز همین بحث را داشتیم و تمام تلاش خود را به کار…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/679426" target="_blank">📅 15:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679425">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
پزشکیان: در حال حاضر کمک خبرنگاران برای ایجاد وحدت و انسجام بسیار مهم است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/679425" target="_blank">📅 15:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679424">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5yXy82pbnajFBRD5q95fhh9sWJcusHBboFMueo1G_Zarjq6jaJCx7qrRMYZmpcqncyoSNnNdHUlbda3wvDLxmRlbYGZgI-4M2li4gzCVadWbWj21hXbaPnCuSygHv6M7gK-mnJMH5a2wz1Xa8rnw0uV7de2yJ5TqGmNzx3TjmsWLvUts8GAcm_ClhINpE3IA5ZN8uG-pHFjaDYTakblvIkerdIihqAlp8JrcgQS-QgaEJiYT1xK-T1JeRF-1loHVDvyfg4B7S9QDLmxyxHlnRg2JFaGsFklUZdt3888sTtthTs3_7jPxgEO0vVtZ5gP0mdm9R9zmyXCnWNmgZ2djg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهم بودجه نظامی جهان از GDP
اوکراین با تخصیص ۴۰ درصد از تولید ناخالص داخلی خود به بودجه نظامی، در صدر رده‌بندی جهانی قرار دارد و پس از آن الجزائر با حدود ۹ درصد و رژیم صهیونیستی با حدود ۸ درصد در رتبه‌های بعدی ایستاده‌اند.
ایران نیز با تخصیص ۲.۱ درصد از GDP به بودجه نظامی، سهمی مشابه اسپانیا دارد و پایین‌تر از کشورهایی چون بریتانیا، آلمان و هند  قرار گرفته است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/679424" target="_blank">📅 15:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679423">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/679423" target="_blank">📅 15:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679422">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5L2wjPhxi-zS5fQpid6o9PkeW98HFTMJ0ogAA5jM7UYMVT_YIRTy8zGSk20A7yXDhln9lzQU45x7XiBl3BTqRyFo1S4ROTmWZRxsg4d789B0-N6yP9dNoyKFhwYTA0hFNgLFFl5Bv_iSZnPDAIdph-vSPX4tGRKDw9vQ09vTTf2wfsN3onbSRzW89qeNGJC_GcNqx4X2KpvyMb5NpkK36L5zWnDRG1k0DOWaV4WXAZ-4JnJHSqjxsk1vbPhsQLXLAFVk-hdydDrmKvQUWkqvZWBfwf3SsvuIeG8u0FmMkxEh8I4ARvHDSABFu3ejWQEnTeXkAf5-NNLpIJI-IBr0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشای الگوی عملیاتی شب رسانه‌های زرد علیه بانک مرکزی
🔹
صیانت از مرجعیت و ثبات نهاد بانک مرکزی، خط قرمز نظام پولی و اعتباری کشور است. هرگونه هجمه به ارکان این نهاد نه صرفاً نقد عملکردی، بلکه تلاش برای مخدوش‌سازی اعتماد عمومی و اختلال در ثبات اقتصادی تلقی می‌شود.
🔹
جریان‌سازی‌های اخیر در برخی رسانه‌های زرد، از یک الگوی تکراری و مهندسی‌شده پیروی می‌کند. تکنیک اصلی این جریان، مهندسی اخبار و جعل پیوندهای غیرواقعی با هدف وارونه‌نمایی عملکرد نهاد بانک مرکزی و گمراهی افکار عمومی است.
🔹
تحلیل تاکتیک‌های به‌کاررفته در این گزارش‌ها، هویت ذینفعان این عملیات را برای رسانه ها کاملاً شفاف ساخته است.
🔹
بانک مرکزی جمهوری اسلامی ایران، فارغ از حاشیه‌سازی‌های هدفمند، بر تداوم مأموریت‌های استراتژیک خود متمرکز است. استراتژی این نهاد در مواجهه با این‌گونه عملیات‌های روانی، بی‌اعتنایی به حواشی زرد و تمرکز بر دستاوردهای عملیاتی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/679422" target="_blank">📅 15:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679421">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
برگزاری دیدار سرخابی‌ها در ورزشگاه شهدای شهر قدس
🔹
دیدارهای استقلال و پرسپولیس در فصل جدید لیگ برتر در ورزشگاه شهر قدس انجام خواهند شد؛ بدین ترتیب به احتمال فراوان این دیدارها با حضور تماشاگران انجام می‌شوند.
🔹
دیدارهای لیگ برتر فصل آینده از جمعه ۲۳ مرداد آغاز می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/679421" target="_blank">📅 15:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679420">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ماهنشان؛ جایی که کوه‌ها رنگی‌اند و لک‌لک‌ها بر فراز قلعه‌ها زندگی می‌کنند
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/679420" target="_blank">📅 15:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679419">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPwkY_gv_oOBugN55srksGZ7SALg3ozigCPhAjQxrFuLmiUOD4cayjRpNcmwPVGZCW7t_9_lrk4wiA76EkNZNmg2FkLHqu1cVb6sauoBaJW9gNyIzvQ5lY1AUi0vjrse9CnybheFMz0UBRUo0USQVQAuMiPZyiw0PngH0N6ULbo78WfBmZDhWkYW6l0iN396WI1oGiHsZNOZ_gGm8hNzDdLErbNqmyRlTNn1Bhc-n_Y3MdoO68u70-BdGIgqBKmkMPHrT2R6dCMDOQBKljTS-qm1dNDwrwP-fQrRcPLXVejV0N14VaI67XbHA_txJJaa7v7ogdcffR4_wrVj8kIZCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سایه‌های نامرئی در آسمان تنگه هرمز | ترامپ سری تازه اسرار یوفوها را منتشر کرد | چرا همه پرونده‌ها در زمان مذاکرات با ایران منتشر می‌شود؟
🔹
انتشار پنجمین مرحله از اسناد طبقه‌بندی‌شده دولت ایالات متحده درباره «پدیده‌های هوایی ناشناس»، بار دیگر توجه افکار عمومی و محافل امنیتی جهان را به معمای حل‌نشده اشیای پرنده ناشناس جلب کرده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3236311</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/679419" target="_blank">📅 15:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679418">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رژیم صهیونیستی به خاک سوریه مجدد تجاوز کرد.
🔹
نتانیاهو خواستار افزایش ۱۴ میلیارد دلاری بودجه نظامی اسرائیل شد.
🔹
رئیس هیئت فوتبال تهران: ورزشگاه آزادی و تختی تا پایان سال به بازی‌های لیگ نمی‌رسند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/679418" target="_blank">📅 15:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679417">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896ee6a0a0.mp4?token=e10AKv2NUqexs5EB-RTi5O_-iYtbGZSEl-gEwTEaerXJ0XT2sy6hv53D13w4wAQRVfYP_H7gXYezNCSY7ERe_Iu-qkpe75JlXuZE4I4Yt69MnJAzYgDOrPXAMn88StCZ4KFg4Zfgb5sBBm1Eu3jL7nJ9lazTQa74WDtGqXWiFaEmpiYpFAnupt_JKgaiPCb1eRty56sS9q6fzyPkgxu_Qmb18_N8G6ML92xUSlF-GuNNVVBEZKtdkntemO1asNopzOyT6nHwCEGbeSkXkoJ3rqUJGOV5gU8258KX-JNiaZUr_z93SgJn_sVj4g3vNhS4FLl7JR3-hfC0V1enL3DBkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896ee6a0a0.mp4?token=e10AKv2NUqexs5EB-RTi5O_-iYtbGZSEl-gEwTEaerXJ0XT2sy6hv53D13w4wAQRVfYP_H7gXYezNCSY7ERe_Iu-qkpe75JlXuZE4I4Yt69MnJAzYgDOrPXAMn88StCZ4KFg4Zfgb5sBBm1Eu3jL7nJ9lazTQa74WDtGqXWiFaEmpiYpFAnupt_JKgaiPCb1eRty56sS9q6fzyPkgxu_Qmb18_N8G6ML92xUSlF-GuNNVVBEZKtdkntemO1asNopzOyT6nHwCEGbeSkXkoJ3rqUJGOV5gU8258KX-JNiaZUr_z93SgJn_sVj4g3vNhS4FLl7JR3-hfC0V1enL3DBkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف زلنسکی: موشک‌های آمریکا به پایان رسیده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/679417" target="_blank">📅 15:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679416">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1797f66576.mp4?token=jEJ9NVY_h-uJwStMRypXS9ZrKIhERs4l5gBlV5XTg2ULjOl_7SyS3UCMuZXt_c9dYBOWaevh7NSExOAMlCGteCGIUksvC7Q7cQcsuEW4XlTHWLyY6KakgPMyrjo6FZvtbzQLRKet6XPUUoSQqGg-xkLaxz3YHOkD1a4o2HKmjJVUL4GD6ShzTLwykV9HBS9ox4MmOP5NyfLZOaO_tAzRNFQ8tlRGefkQzkTj3CTVzoL99hJ_5q115q2hgfi9VAdvyL3sOjJu7OTSfreE_FxRK94UkDHa0LvCTU7j_UoB8e7XnyH5hHGVPhgTLJ5w2QqudBe-p9r-RtcvuAttKKst2W6CGVX0kaU0g2ixud81Mo4Q0ap6LsJh3UvzTLHKiRsEEpbgoZaYg1aa6hNSgBxy7btbl04gp7p5Lo0K3pbKyI3tCbkVfTqnzfRLujJ7z81bEOIP0UeaB_1ylTcu1rOlug0zCX9gphKi-RLdSbcMou5moZaWcVqfNfuJcojwMfWnSr_bSbXv_PBja-OXVw-A73O-xaxx4FpGcN0rp7d6Mswvou2eqOssVWF6dY0eClRdHFlidg-qYFMa_3SbEQfV3HIT2fm36yf-uqIJvrbW4_yEjF0MrboWx79W0392MzmSHQXFUBqtpKfg1QtG4eS2JEQpxifI1YWM7E6S7Cp2mxE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1797f66576.mp4?token=jEJ9NVY_h-uJwStMRypXS9ZrKIhERs4l5gBlV5XTg2ULjOl_7SyS3UCMuZXt_c9dYBOWaevh7NSExOAMlCGteCGIUksvC7Q7cQcsuEW4XlTHWLyY6KakgPMyrjo6FZvtbzQLRKet6XPUUoSQqGg-xkLaxz3YHOkD1a4o2HKmjJVUL4GD6ShzTLwykV9HBS9ox4MmOP5NyfLZOaO_tAzRNFQ8tlRGefkQzkTj3CTVzoL99hJ_5q115q2hgfi9VAdvyL3sOjJu7OTSfreE_FxRK94UkDHa0LvCTU7j_UoB8e7XnyH5hHGVPhgTLJ5w2QqudBe-p9r-RtcvuAttKKst2W6CGVX0kaU0g2ixud81Mo4Q0ap6LsJh3UvzTLHKiRsEEpbgoZaYg1aa6hNSgBxy7btbl04gp7p5Lo0K3pbKyI3tCbkVfTqnzfRLujJ7z81bEOIP0UeaB_1ylTcu1rOlug0zCX9gphKi-RLdSbcMou5moZaWcVqfNfuJcojwMfWnSr_bSbXv_PBja-OXVw-A73O-xaxx4FpGcN0rp7d6Mswvou2eqOssVWF6dY0eClRdHFlidg-qYFMa_3SbEQfV3HIT2fm36yf-uqIJvrbW4_yEjF0MrboWx79W0392MzmSHQXFUBqtpKfg1QtG4eS2JEQpxifI1YWM7E6S7Cp2mxE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
عملیات ویژه آغاز شد
✨
وقتی یک دختر کنجکاو تصمیم می‌گیرد از خانه خودش شروع کند، یک مأموریت بزرگ شکل می‌گیرد؛ مأموریتی برای حفظ برق پایدار، کمک به خانواده و همراهی با همسایه‌ها.
💙
⚡
این فقط یک انیمیشن نیست؛ داستانی از مسئولیت‌پذیری، همدلی و نقش هر کدام از ما در مدیریت مصرف انرژی است.
🌍
💡
🆔️
@tehran_roshan
#تهران_روشن</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/679416" target="_blank">📅 15:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679415">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kq9aaOPP4ShnVtiTd1dPLhtL17y3RMI_MnLioBHc1NauYU762CN-YkI1UH0laWib64aTqHkq3EGt2WCD894-gCT9ENXJrx5e2BAvVTM1COZruOsrdYDLyD-ncI4SHQAuA1PGF4cfuydf5qNAAj-AX9ifQeuvtG6CmbV81mSiK1vJBvTe6leO-uuPoUb4GO7KV53z3nzZjyRfqxgTqbNBl60W3XVGZrzDnFigjxJGlt-5IGtO3CtW4b_bsxoZFFH7Ax0dD-D9VLjN97QJh17r8agGPe2gcNW2XkSvZrHE3lD99MERsXOMzZbWnR78Q0pw5vTCFRS9TQipFvm29XEP1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خط مقدم نابرابر روایت‌ها؛
مصائب دفاع از حریم افکار عمومی
🔹
امیر نیک‌رویان روزنامه‌نگار در
یادداشتی
برای روز خبرنگار با اشاره به شرایط نابرابر رقابت خبرنگاران ایرانی با رسانه‌های جهانی و مشکلات معیشتی، امنیتی و آزار سایبری نوشت:
تجلیل از این فداکاری با پیام‌های رسمی و اهدای شاخه‌گل محقق نمی‌شود نمی‌توان در روز بحران از خبرنگار انتظار داشت دوشادوش مدافعان کشور از حریم افکار عمومی دفاع کند، اما بدیهی‌ترین حقوقش را نادیده گرفت. قدردانی واقعی از روزنامه‌نگار، تضمین امنیت شغلی، دسترسی پایدار و بدون اختلال به اینترنت و پلتفرم‌های ارتباطی، پرهیز از امنیتی‌کردن فعالیت حرفه‌ای خبرنگاران، به‌رسمیت‌شناختن استقلال حرفه‌ای و حمایت در برابر قلدری‌های سایبری است. این موارد امتیاز ویژه نیستند، بلکه بخش جدایی‌ناپذیر زیرساخت دفاع از منافع ملی‌اند.
کشوری که می‌خواهد صدای روایتش در میان انبوه روایت‌های جنگ گم نشود، باید پیش از هر چیز، حافظ جان، نان و شأن کسانی باشد که این روایت‌ها را می‌بینند، می‌سنجند و ثبت می‌کنند. کشوری که خبرنگارانش را در روزهای دشوار تنها نمی‌گذارد، اجازه نمی‌دهد دیگران به‌تنهایی روایت و تاریخش را بنویسند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/679415" target="_blank">📅 15:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679414">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/804a675aa2.mp4?token=spexuRHma4UM8qpHnzOC-LBxGwfA-oG9YFUIbr4yTztnugOQtSB72Tw6Lj9krFT6xhIxY22WfuhqPouVa12vL0ZDlBicO97XMzWw5tfGb_iHy3mLBwnvpHgB_hrnjyO7kzPfT1vJ_2ydgk75wSCC8TqH5K3jEw16cejHB8poOrJOKfwEDIUD7LMWvJK5M8EIQjeu4CTMHT-WH7t4YYAKFWuiXwn7Xc3nXjEi_68fRi_-HegGGs-C1X4rjkRDkRuPwjCi1M1VrEtDioc0AWS90oVU_elrHYjjAQQHvBpx8cPWIRM9AgCkIcunEe-0jAZibbTIRc43OkWreYCrqJh6OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/804a675aa2.mp4?token=spexuRHma4UM8qpHnzOC-LBxGwfA-oG9YFUIbr4yTztnugOQtSB72Tw6Lj9krFT6xhIxY22WfuhqPouVa12vL0ZDlBicO97XMzWw5tfGb_iHy3mLBwnvpHgB_hrnjyO7kzPfT1vJ_2ydgk75wSCC8TqH5K3jEw16cejHB8poOrJOKfwEDIUD7LMWvJK5M8EIQjeu4CTMHT-WH7t4YYAKFWuiXwn7Xc3nXjEi_68fRi_-HegGGs-C1X4rjkRDkRuPwjCi1M1VrEtDioc0AWS90oVU_elrHYjjAQQHvBpx8cPWIRM9AgCkIcunEe-0jAZibbTIRc43OkWreYCrqJh6OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس جمهور: اگر صنوف و تولیدکنندگان همکاری نمی‌‌کردند وضع خیلی بدتر از این می‌شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/679414" target="_blank">📅 15:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679413">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cf602bc46.mp4?token=mubPjpyW1RVgIcL1YOxk9OAI4UqrvBJfn7WmnHCw72nGMEqkAXhJ0Sh95TB1fSTot5oCOMZOor-f3Cv_sqlNmiK64SRlKaU5EY5iQAwODkai0HvGiapofQ3Lh_ImCgxSjaQcClJopv1rsiUWE2vJ5J5OzRaSbQqF65PShiSzWv9o312UfSUKatkh9broSs3iNlD85I_XOrekv1JKidrTXsvJSjHlx065uEvYPWs03JnOqH_3XVwERVcE040u6BjZ3DZo8QETIZP0vfnZUodgavyoSvLvciYd4-74_25B0PgDGNBB1rXlcdloqnUGJPHAqRMtCfioT3_A-dWwUenSAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cf602bc46.mp4?token=mubPjpyW1RVgIcL1YOxk9OAI4UqrvBJfn7WmnHCw72nGMEqkAXhJ0Sh95TB1fSTot5oCOMZOor-f3Cv_sqlNmiK64SRlKaU5EY5iQAwODkai0HvGiapofQ3Lh_ImCgxSjaQcClJopv1rsiUWE2vJ5J5OzRaSbQqF65PShiSzWv9o312UfSUKatkh9broSs3iNlD85I_XOrekv1JKidrTXsvJSjHlx065uEvYPWs03JnOqH_3XVwERVcE040u6BjZ3DZo8QETIZP0vfnZUodgavyoSvLvciYd4-74_25B0PgDGNBB1rXlcdloqnUGJPHAqRMtCfioT3_A-dWwUenSAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوخی حاج‌قاسم در عملیات آزادسازی بوکمال
/
داری با من مصاحبه‌ می‌کنی؟! شیطنت می‌کنی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/679413" target="_blank">📅 14:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679411">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39b695a029.mp4?token=t8gQmPFygzOHlqdYjyFcMfxtjIe19y5ofZrRqHNV996iQrVaro0PteiVqI2MgQhOJB98KHHTJMyecVBHdXIltlI4Nv0IeCrwQHIWZZomxLnQkd28rkL2VgujMgEaO3euY0V63L34xbNbJYQlqABJxKezDD28WTSBU-zvnq5gnEDm6rbukwzpyf6fn2yCcQKdpLO118Q2ZYUr1zh9YvJJZVAJ8LfN2gfqTeu7njn56Iq3QOU468Ehc3iqr83MOGigxrmjeAGrFO2bMaPccj8jewMlz0931o-gQjJ-xdKHdoWOddOq7e81i1OrtF4jQ9x2U6SZ20GHwIgypF4ZuCEtEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39b695a029.mp4?token=t8gQmPFygzOHlqdYjyFcMfxtjIe19y5ofZrRqHNV996iQrVaro0PteiVqI2MgQhOJB98KHHTJMyecVBHdXIltlI4Nv0IeCrwQHIWZZomxLnQkd28rkL2VgujMgEaO3euY0V63L34xbNbJYQlqABJxKezDD28WTSBU-zvnq5gnEDm6rbukwzpyf6fn2yCcQKdpLO118Q2ZYUr1zh9YvJJZVAJ8LfN2gfqTeu7njn56Iq3QOU468Ehc3iqr83MOGigxrmjeAGrFO2bMaPccj8jewMlz0931o-gQjJ-xdKHdoWOddOq7e81i1OrtF4jQ9x2U6SZ20GHwIgypF4ZuCEtEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: آمریکایی‌ها از بند تفاهم‌نامه درباره تنگه هرمز تخلف کردند، ما هم پاسخ‌شان را دادیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/679411" target="_blank">📅 14:52 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679410">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
عراقچی: مذاکرات با عمان برای مسیر موقت در تنگه هرمز نزدیک به نتیجه است، اما این به‌معنای بازگشایی نیست؛ بازگشایی منوط به جبران نقض تفاهم‌نامه توسط آمریکاست
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/679410" target="_blank">📅 14:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679409">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
عراقچی: مذاکرات با عمان برای مسیر موقت در تنگه هرمز نزدیک به نتیجه است، اما این به‌معنای بازگشایی نیست؛ بازگشایی منوط به جبران نقض تفاهم‌نامه توسط آمریکاست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/679409" target="_blank">📅 14:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679408">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4c4876d09.mp4?token=esDh0eALwuLx6J0R0odzPMvULKHNPOdULq1-h6c3lGzTnn6hPdTVc0AfDNU1XLhYwL2SF06wtFJvFcvg0ZVaZWgMbUK0LRvc7DUamaFKzVDSZvF5iBXpLzLp2NJ_rUAr722hcAfJr22ua8UIrnCc28Xf_5dFEwFBBNO5c8oOxpByW_HQotcjG9fH09Aen3-G738vTv2MzYC7xbqx8qx8KXm6z-bZaH9cE4XLJH_rwKag8Fd8uHDymsfjKe5yZ8LT-8IzwN1pFz1NlaITKYAgOWcodaM-jv8lqVL5m6pqf5rp_evOyWjHAhDuEx9nNlsaeuAfpd_drWl6wEhJsAvmrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4c4876d09.mp4?token=esDh0eALwuLx6J0R0odzPMvULKHNPOdULq1-h6c3lGzTnn6hPdTVc0AfDNU1XLhYwL2SF06wtFJvFcvg0ZVaZWgMbUK0LRvc7DUamaFKzVDSZvF5iBXpLzLp2NJ_rUAr722hcAfJr22ua8UIrnCc28Xf_5dFEwFBBNO5c8oOxpByW_HQotcjG9fH09Aen3-G738vTv2MzYC7xbqx8qx8KXm6z-bZaH9cE4XLJH_rwKag8Fd8uHDymsfjKe5yZ8LT-8IzwN1pFz1NlaITKYAgOWcodaM-jv8lqVL5m6pqf5rp_evOyWjHAhDuEx9nNlsaeuAfpd_drWl6wEhJsAvmrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: آمریکا نمی‌خواهد جمهوری اسلامی باشد ولی گفتگوها او را وادار به همراهی کرد؛ چرا دستاوردها را خراب می‌کنیم  رئیس‌جمهور در نشست خبری:
🔹
آمریکا استعمارگر و جنایتکار است و نمی‌خواهد جمهوری اسلامی باشد در این شکی نیست ولی همین گفتگوها او را وادار کرد…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/679408" target="_blank">📅 14:41 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679407">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
پزشکیان: آمریکا نمی‌خواهد جمهوری اسلامی باشد ولی گفتگوها او را وادار به همراهی کرد؛ چرا دستاوردها را خراب می‌کنیم
رئیس‌جمهور در نشست خبری:
🔹
آمریکا استعمارگر و جنایتکار است و نمی‌خواهد جمهوری اسلامی باشد در این شکی نیست ولی همین گفتگوها او را وادار کرد که همراهی بکند؛ چرا خودمان را ضعیف می‌کنیم و دستاوردها را خراب می‌کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/679407" target="_blank">📅 14:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679406">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d15af7df8.mp4?token=QQi93HQWzSoYuI35SUTCvGKj6LK9vvo2BAbLi9zcoh4NevrsxHKxl5dVeMngQ4hyn6BJYdcHHreCjnv_7vJ5OCVFEONi7qXJHCAP11BlhKNXYE61I6et5vE4RoQziprFfW7Bv9pofokzJXZHGKy3f86gweclSmHBcPGc6xegUym6boF5u07rRIz-Ta1Kj2wxeFh1OXNvihC8VC_irlZofcR6gz56kNczoo_p_9uaDNwxoa7WgC6Zwy2SWi4T1SaBgY3TOUt1Lu6rqfDMXO6iuTSGbmEYd_RVa5fNlTtpXT1PfT80YCk0Uadk5L5Yr8ix8j5IJFfYpRvG3o_OrIKvhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d15af7df8.mp4?token=QQi93HQWzSoYuI35SUTCvGKj6LK9vvo2BAbLi9zcoh4NevrsxHKxl5dVeMngQ4hyn6BJYdcHHreCjnv_7vJ5OCVFEONi7qXJHCAP11BlhKNXYE61I6et5vE4RoQziprFfW7Bv9pofokzJXZHGKy3f86gweclSmHBcPGc6xegUym6boF5u07rRIz-Ta1Kj2wxeFh1OXNvihC8VC_irlZofcR6gz56kNczoo_p_9uaDNwxoa7WgC6Zwy2SWi4T1SaBgY3TOUt1Lu6rqfDMXO6iuTSGbmEYd_RVa5fNlTtpXT1PfT80YCk0Uadk5L5Yr8ix8j5IJFfYpRvG3o_OrIKvhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز
تغییر ادبیات رسمی سفارت‌های ایران در توییتر برای روزهای پرتنش/
تلویزیون اینترنتی مدار
این برنامه را در یوتیوب ببینید
👇
https://youtu.be/WQ8SA-5rZMU
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/679406" target="_blank">📅 14:34 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679405">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38519590a5.mp4?token=b_dlf06Gm8wWN7eQVyAGcRmrhgacYyIV6519LEEcHyPBvIicdQJArohryXyFSNRMmcRsXSfIkb8_DnGpa_H4EjJvE6rqd7iMsLtXS0pKv94Vi8A8ygMLgak5RDlcc36S3V-qJ9G3FMVWP5P0SYP2L165t-LVQruigmWvfA9cGIiIgITo9CO-mLg0uZiyyqVAODmkZbqUKkX7lRWCP2aCnNAjEO2uV_ezzXXkD7wa5XsPcWCGOE3oPvX4E00Ld6-EixYIuDOIkyfaF_Q48rD81IzRBQxPDz7ksT-jS5I5rX8ZtBMVyb-2BdB1u8HOQB4VVKW0DZsrsi_c0gmRj-Lnmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38519590a5.mp4?token=b_dlf06Gm8wWN7eQVyAGcRmrhgacYyIV6519LEEcHyPBvIicdQJArohryXyFSNRMmcRsXSfIkb8_DnGpa_H4EjJvE6rqd7iMsLtXS0pKv94Vi8A8ygMLgak5RDlcc36S3V-qJ9G3FMVWP5P0SYP2L165t-LVQruigmWvfA9cGIiIgITo9CO-mLg0uZiyyqVAODmkZbqUKkX7lRWCP2aCnNAjEO2uV_ezzXXkD7wa5XsPcWCGOE3oPvX4E00Ld6-EixYIuDOIkyfaF_Q48rD81IzRBQxPDz7ksT-jS5I5rX8ZtBMVyb-2BdB1u8HOQB4VVKW0DZsrsi_c0gmRj-Lnmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای اولین بار در جهان؛ درمان موفقیت‌آمیز ناهنجاری پاهای زرافه با آتل‌های سفارشی طراحی‌شده توسط متخصص ایرانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/679405" target="_blank">📅 14:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679404">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/akhbarefori/679404" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
روضه‌خوانی تاسوعای امسال شهید حمیدرضا رجب‌زاده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/679404" target="_blank">📅 14:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679403">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IK_O-8Ub0i7tIPGSeG_kl3fdJ6vnkXEgJoYMelRHPoqaEuB0A3P8LsI2qDjJJ3ns0mnGunDVRjxhbTluPKr5aTkvbm9WHQF91ys5k73Z6IVWqnHfIGDGAjbtuWSsc0ZJ23N7EECE4gX2vDXudhXixs2UhYrWICk_8f9AF4Qqg8BG64YmauLdHcjVStz8GSq0-CXXttNsKOLZB2znXsn-1kD0ImQ3xGd-NjxZgHelj65bHS9nlhmjX_Qkv_0opLfE6ykjaLXRrdN7zAD4GhF0wqUUed9IpNeUCSux5avNBOI1MuRfAe9NA-3Y8diRxoweFLO-i1KbRDzJdFxLQC6GMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تأیید یک مورد ربایش و قتل؛ تحقیقات برای شناسایی عاملان آغاز شد  یک منبع آگاه با تأیید ربایش و قتل حمیدرضا رجب‌زاده:
🔹
او چند روز پیش ناپدید شده و پس از آن ویدئویی از لحظه قتل برای خانواده‌اش ارسال شده است.
🔹
تحقیقات پلیسی و قضایی برای شناسایی و دستگیری عاملان…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/679403" target="_blank">📅 14:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679402">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dygV9_wzDVrtOef9ELcKnaSOUjQkP2X3u_MO4sZm0-t-tBeKyrvfzNhW3-fsgXUZAXxfT5bDnhBdj8LvhbuLMNNotsbN2KzUDEVw08Sar84lfrMeni57McEGjMLMgtxIO1kjemQfE8bhMP3jQHS4LMjVA2jkSo7R8JcXHtyQA7mpL9a8uOz2WGzsCiPPMXKSsU-RtfZHu3A8LnHooNZtroXOUm-oJ7_Qe8_knlViuoxGnGojMvE86Q3oXCs9vaetjH3XgwzUcpbyXSdg3QHxME8CadmnUZjK2RNd7fkj_UVdkUypVTxL4LPywNVncOp21F5TVHMr-4yn9tJqXi4jug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«خورخه مسی»، پدر لیونل مسی درگذشت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/679402" target="_blank">📅 14:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679401">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌وپنجم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای هادی عباسی که در سانحه تصادف به همراه همکارش روح از جسم دو نفر به طور همزمان جدا شده و با هم به گفتگو می‌پردازند و جناب عباسی متوجه جایگاه برزخی خوب همکار به خاطر کمک به ایتام در زندگی دنیایی او می‌شود و در ادامه به خاطر شیون و ناله خانواده در بیمارستان روح ایشان آزرده می‌شود اما با دعای برادر در حرم امام رضا (ع) آرام و مورد شفاعت حضرت قرار می‌گیرند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: هادی عباسی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/679401" target="_blank">📅 14:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679400">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
حمله به کشتی اماراتی در تنگه هرمز
خبرگزاری امارات:
🔹
امروز یک کشتی متعلق به شرکت «ادنوک» هنگام عبور از تنگه هرمز با یک موشک هدف قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/679400" target="_blank">📅 14:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679396">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O3d7n3lSgYkGbNayB6Ngugy6_MxKy4vF1ee8Xgg3sMOBxyitw306zyZJevu6_d_N_7tqBL72_IqNm3mnyza1EOod3av9KY74-2wQW5Ktm6QcAQtCg_Tyxbgfwx86uun_t9szgZRJIkQBqYgoKr3ftwB-ayng5cu0iJQLkzpHdRNlJZypCDudb6a9niUbVLbrBIz_tuZZyVGKt9l5l4APlZxOdJ030vpoJuS-JX8V4ArbTQw6AhFGq_3NLlAAuUmBF-ziUj-M-JvbJJsCja5Y1UQIrI9LPN2ha84Wy56a_bDgoHA8rlvCPRFTQ_r9n-e-jFiicBs-d3ztS7mq5MLgGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NyRKhLgB2duMnRLuDAi6MBA60EZPnBSZB8P-NXxMRyvE20eu2RwmbEUNWiisoYYiH6Tlu0hOh_ecOxIVWAmLv0l83bJIvVTY-mpSQmwm90QV-eDW33g81EvgUoN2a9z3KxcVeJv_4wgCH_WSS_mPGihoz_RMX3oH9ttjl_rmJowYMHWbABscIQX5TDsBVmTsIio-4qvcI6BZ3CJZfyQ95gN9oYWZQrvonvtcMWonlZWGDe6zLIiS0xMPJD_GNQEzPcixvNgYMeIGU3nNqMlq-Cv-OZf6cp0KsU8JMkXT8PnbN61-TNwCG3VPDRRxGdtfKyLOw5LNwS4D_IH4lU6CFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_JWKhd_xH50Lx9PRQqVwKO7EGIo6Eq8sJZ-nXhdXnWwXUB2Dg8QHWfW_gzN1OZiFwFbrVV3lIM8gtJ1GtncQ94FbShGuz-JEEpooP3tvvtY7kTTIUfWbtfT9ubyVB0fFygbY4n29iBG3HlfpGmhzvE3c147O1Ft5lQN1GAEEVKdQs9oXJCQqmDO9HkxeuJLBiG1ZNFY50bjYI9ksSH0TQ_dxkqm7NmNm2A5aMsv-JH_exMlL_YqPWYLKJGxxfjdTuMV164g4qWFlQvnwcrbSp-s_dX6trzZroIOZw6C1Jzu68xq5brwkegyR7uRrkGfTCv6C-cUXQdujM8f-AbS3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WLTpVgUfsJUkVlvTprMXxGSeEIhp364RdKWqWOAm-0dHDvmNyASlAVCQMFfkeUElOf1_ef-FdRxQ3CGfulckKRJUmVx7Co5aLDA4K8nnHilnudHiJltEEyx3qCIu8ZVeru1SM3rnq7EXIyy_PkZcX8mvpfJidFeSVC2z9kW0KOyv8KJc93nzn0HlUQyrV5P7PplaeSUIAXeKBDbzRlYXAahpkqzTbp7u9FsqH914dXUveWn3q0Wnfu8FppRDFkIZ4kma8jgDIj1DhCIio2h4MjIgOJRauHWPZ3WWOOD_M0m0TFFO__3ZFKw9GAWDTQTogHBfireRRfbgrOI2n9Fs3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هر کفشی مناسب کدوم شلواره؟ #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/679396" target="_blank">📅 14:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679395">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
روزنامه
رای‌الیوم: ذخایر موشک‌های رهگیر پاتریوت کشورهای خلیج فارس به‌شدت کاهش یافته؛ عربستان ۸۶ درصد موشک‌های پاتریوت خود را در ۳۸ روز جنگ مصرف کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/679395" target="_blank">📅 14:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679394">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc9dc6e948.mp4?token=dWIejNbZ5LzCzTj72GTqvn9brDLso-9b74fkpResXEr4hHr56zjDO8EAjDFksKkmQUJjDMrKdtPPprrCpXBaYzFFvPTFZ1kgLh6haILtwwFSOYtena3ALebqBZiOYVAdrfmVCmJ6bo6QzrATMjd-pZUkOqgJ_Gz29nnY3Dw8MDNO2AzdxjeUTFYdJkE_ihlGmIbwHLIIPoi5BoSXx5zTt4zqy1ZzEK1GKv23x1hHyZUAsGLolstCxMM9PTFQoIXBAcDKJLPHrPbzHSd69BY9moRXdRd33-5c3ykaVdhV4Mb8f4LT1HMpmrau02URiaafVGZq4TASMUz7f6Wt-xPE6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc9dc6e948.mp4?token=dWIejNbZ5LzCzTj72GTqvn9brDLso-9b74fkpResXEr4hHr56zjDO8EAjDFksKkmQUJjDMrKdtPPprrCpXBaYzFFvPTFZ1kgLh6haILtwwFSOYtena3ALebqBZiOYVAdrfmVCmJ6bo6QzrATMjd-pZUkOqgJ_Gz29nnY3Dw8MDNO2AzdxjeUTFYdJkE_ihlGmIbwHLIIPoi5BoSXx5zTt4zqy1ZzEK1GKv23x1hHyZUAsGLolstCxMM9PTFQoIXBAcDKJLPHrPbzHSd69BY9moRXdRd33-5c3ykaVdhV4Mb8f4LT1HMpmrau02URiaafVGZq4TASMUz7f6Wt-xPE6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد دو دنیا؛ تپه‌های شنی نامیبیا که در اقیانوس اطلس غرق می‌شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/679394" target="_blank">📅 13:56 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679393">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaVv92PeR0Cc2PLHm1BR8F5tZt-F0_yLCYpz2Y0GTf1rfoUbdZjpBgsuwph4k_ea0s2Hi7vJzyybD03GziphxUEDdgZJSc4AtbnTVSHnn9iF1t8Sp1QRjpJ-3rWO1IRUVjlX9VNwsBK3hoy1BLDfkyMxD40WrLqNfZ0qYXJway4vcv5NC_LdcUNdNy6uE-98XP5F46znQAbF1wpDqM9Ty6oSJatBRwQJrUyyi9-Uvgxf-iylFMGDd5IG1dd8uaDz4eOqnY4zIPSLKAoxazDCotbdnyXciZOC1Ddr_d9MfMLFyctFrfb7T7cMLCNOhE1SygJUTOJnfJo0pwYEz12Hhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۷ مرداد ۱۴۰۵؛ ساعت ۱۳:۳۵
🔹
دلار که در روزهای اخیر با تکیه بر اخبار مثبت سیاسی و کاهش تنش‌ها مسیر نزولی را طی می‌کند، امروز هم کاهشی بود.
🔹
اسکناس آمریکایی با کاهش قیمت نسبت به پنجشنبه، به ۱۸۷ هزار تومان رسید./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/679393" target="_blank">📅 13:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679392">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8409ef1a14.mp4?token=lCWJfVSx5jNY-PwwGxQrCVcytYJMiP2U44krZvg-bP1FVrs-Y88Tx3EFIu4mEl8lhOAPiZFlwdXtzsAPKFx3BGtaK48aiC4qZ7okitqGGnM62ynn1taY_u4lBV8kRvpABfA4Hb7I_EftWieFjKw9WB67LZchAGyZXKEv_T3cqk8Eqx4QepIG6GCiL6mzTI1fMgFfYKJGcSbT23Y7UhmKD5UboCQUwi7gNE7NjIWtgbltZBp_L_dydiWgfl29o9JSGuxjtJQzG4i--seN3cv6qv-7cm6UGRdcF_iZ97zb0-7XS1fDvKRM8vl7IoXZtZc6bVpTcPKvQcxhYTAMs0hM4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8409ef1a14.mp4?token=lCWJfVSx5jNY-PwwGxQrCVcytYJMiP2U44krZvg-bP1FVrs-Y88Tx3EFIu4mEl8lhOAPiZFlwdXtzsAPKFx3BGtaK48aiC4qZ7okitqGGnM62ynn1taY_u4lBV8kRvpABfA4Hb7I_EftWieFjKw9WB67LZchAGyZXKEv_T3cqk8Eqx4QepIG6GCiL6mzTI1fMgFfYKJGcSbT23Y7UhmKD5UboCQUwi7gNE7NjIWtgbltZBp_L_dydiWgfl29o9JSGuxjtJQzG4i--seN3cv6qv-7cm6UGRdcF_iZ97zb0-7XS1fDvKRM8vl7IoXZtZc6bVpTcPKvQcxhYTAMs0hM4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقام پیشین وزارت خارجه آمریکا؛ دیگر حرف از کنترل تنگه هرمز نیست؛ ایران تمام خلیج فارس را کنترل می‌کند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/679392" target="_blank">📅 13:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679391">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سخنگوی سپاه: بازگشایی تنگه هرمز منوط به پذیرش شروط ایران از سوی آمریکا است
🔹
معاون وزیر نیرو: ناترازی برق ۳۰ درصد کاهش یافت؛ محدودیت صنایع به‌زودی رفع می‌شود.
🔹
ارتش روسیه از تصرف شهرک ایوانوفکا خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/679391" target="_blank">📅 13:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679390">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMzl_575vf0ehh1mCBhYZEEz5f_uYQnj1guzFsS1XKp_nGBJH5M_fFlu2nXDc0wtwN5CWjQPDKSqMPxjO6GYVzvDF-GkllTLBR2tB1AE2GNFqe-z2SBPS8pevPxigO_SGJb_wFbiKS-wUtlmpuT1WBn9VDNHTgOIsn_S-Smd2Dr7rIIniRT7ssCbj8nxss_7s_ALfwYxlLulNE87iId4dcqsnZPObpXNkQxDW0Ygmm1M9UFKKh-jFKfB6r2HlS0YJKSQbHK9NCpsix7-ISNtbMsQ-veNvmwIPXhxDRvhCkbtzaBf6qWnTQt0D4dbfoLpAzmGvglSlfz4z4VekUbcaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩺
ثبت‌نام طرح ویژه آزمایش رایگان در منزل
بدون نیاز به مراجعه حضوری، آزمایش و چکاپ خود را در منزل انجام دهید.
نمونه‌گیری در محل شما انجام می‌شود؛ راحت، سریع و بدون اتلاف وقت.
⚠️
ظرفیت پذیرش محدود است و با تکمیل ظرفیت، ثبت‌نام متوقف خواهد شد.
👇
برای ثبت‌نام، روی لینک زیر کلیک کنید:
https://drsna.ir/r1</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/679390" target="_blank">📅 13:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679389">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7aeeab2332.mp4?token=FNIKQnBeIVJ95mvnKeG1t5W0t2Ok0m9lcGJPw_nJIXE14W51YzERSiuAedLzstfhUwh_U_RSSTRsR11cSoXHPk0HOMhQmHrt9-IhgScXfZrZbr7ENeks9pUoWG0I76vkEIDJIOin1DbbVeJkRwZecEUZciVS9qOg1gVGNoTTPQ0x5HSEi9wyrykLh9x7AFnwfYKDNmk-pLFdag41ljBHS7gfiF39dWW-GlUaUkatcol7epojW-5yBTJrjZD_w7_UgvxHI7JRcuFq_y7yBkt-ftwSnvQDnZTiEEB2sos36ZHS8in6Beof9D0133t-pCPS7itrDsLbzbk3YgCj0P3PMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7aeeab2332.mp4?token=FNIKQnBeIVJ95mvnKeG1t5W0t2Ok0m9lcGJPw_nJIXE14W51YzERSiuAedLzstfhUwh_U_RSSTRsR11cSoXHPk0HOMhQmHrt9-IhgScXfZrZbr7ENeks9pUoWG0I76vkEIDJIOin1DbbVeJkRwZecEUZciVS9qOg1gVGNoTTPQ0x5HSEi9wyrykLh9x7AFnwfYKDNmk-pLFdag41ljBHS7gfiF39dWW-GlUaUkatcol7epojW-5yBTJrjZD_w7_UgvxHI7JRcuFq_y7yBkt-ftwSnvQDnZTiEEB2sos36ZHS8in6Beof9D0133t-pCPS7itrDsLbzbk3YgCj0P3PMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه انفجار مهیب جایگاه CNG در صحنه از دوربین مداربسته
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/679389" target="_blank">📅 13:34 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679388">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f3ec6e44.mp4?token=RP4NyRNwV4Nn7mu5fiDG6lDsQkr4IskccQ4PaRMFib6PQRRhCeNSb0zsVdgqr0cOoxmmaZr5P8HvvY6oYGw0Pv7TSX2Zqq8Y0sOAVvrwsL-vtJGfJEyojzHDmV2d8wqHAzdZRehQd3J3jDfEIEFuXoi2c0nDToYLBVjxVFS2lvzwqmTnnhiAuu6H59_szFA3iUIy2IcMlKQGGMy7YCSg1SZymvwvO7flXnxQghdq9GmE_WjSvMwDy3Em563bXzw1MedxGUvJjFN01o1wennBxjClHV-PUIPUQjnadPFTObXwkp1ZyYLdNcdZn8hvCAAfP6XLxmOgwEJpDJ7FDA7_Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f3ec6e44.mp4?token=RP4NyRNwV4Nn7mu5fiDG6lDsQkr4IskccQ4PaRMFib6PQRRhCeNSb0zsVdgqr0cOoxmmaZr5P8HvvY6oYGw0Pv7TSX2Zqq8Y0sOAVvrwsL-vtJGfJEyojzHDmV2d8wqHAzdZRehQd3J3jDfEIEFuXoi2c0nDToYLBVjxVFS2lvzwqmTnnhiAuu6H59_szFA3iUIy2IcMlKQGGMy7YCSg1SZymvwvO7flXnxQghdq9GmE_WjSvMwDy3Em563bXzw1MedxGUvJjFN01o1wennBxjClHV-PUIPUQjnadPFTObXwkp1ZyYLdNcdZn8hvCAAfP6XLxmOgwEJpDJ7FDA7_Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پوتین: رئیس‌جمهور پیشین فرانسه درباره آمریکایی‌ها گفت «بی‌فرهنگ هستند
پوتین:
🔹
یک‌بار از ژاک شیراک، رئیس‌جمهور پیشین فرانسه، پرسیدم: چرا رهبری آمریکا این‌قدر تهاجمی است و در بعضی موارد تا این حد کوته‌بینانه رفتار می‌کند؟
او به زبان روسی به من پاسخ داد: چون آنها آدم‌های بی‌فرهنگی هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/679388" target="_blank">📅 13:34 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679387">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWHvpgxzycjWCQ-wx8asmx2eI_rv10YUkArZCljjD6f-sfq0m-JDinyuwpD51TCdXzkv-Zq4V-EvHCyEpP8uWvnwOYauAFfd0J-uuXmUTlZXmDnO91OsYvHx_egTJN_tR99ZTcO7w6bE3ZqTu_IV57Lo3zG2OBF0pIsQvPm9B3PtRNv3uU4VX3fmi5YDjbpU0wsX_CSSYr4Rb6LWCGfuk7vzIclaLP-5LNDpYv9xaqP77JhXCg_AYRQFocR8a9E3QTO_lClnmzMZXA_NOhI4bJASUs6KqLnme9fkO7pTKKDrYLVVKFwJQ5NXm9IbNrQ6N9j0dfCZIx0eV4BrI7gSAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرمایه‌گذاری در صندوق سیمان، آری یا خیر؟
🔹
تحلیل‌ها نشان می‌دهد ترکیب رشد زیرساختی و درآمدهای ارزی صادراتی، صنعت سیمان را به ابزاری برای پوشش ریسک تورم تبدیل کرده است.
🔹
با نقدشوندگی بالا و ارزش‌گذاری دوره‌ای، این صندوق‌ها فرصتی استراتژیک برای بهینه‌سازی پرتفوی شما هستند.
🔹
شما چقدر به وزن‌دهی سیمان در سبد دارایی‌تان فکر کرده‌اید؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/679387" target="_blank">📅 13:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679386">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b72f7ffdf7.mp4?token=HR-rLjwSiJ7x9Id5CLclAjrHIWCcOBfBUyUWA3GyZu4R38WkoFCgtMnxtcgiUP7zWGIZUpGGjoiAzLfFCBeqlx7eUybM_34uU9ds_xiUgAjIO8lX4xDpsXjmZXSccdXNnOfaH7TrbTq-NfzFlFx5h0fopWR6IF2s2GtnuE_tXUsI_FgSsCy_iQdzcqv-ZzUszsQ_0-ckvq1xxeTsrPJTWrq4lDn3d3Pme-Vs6SwWP8vt4BCdvogNXxAtenVpTs2QfHEuyIlGN-B3ZBWa1r4RuALgRYFcTJQxi1809Yt2sXB0inQvFtVQ0IgCb416xlpqmlIu4f6XP9I9abv_JDF1uUF0LroPnqn690Oc8pwR-GzvK8bORpLGiiG9UmWMza0RQBIsDe-7l9gotdV3vUxWct9SfqirRGsI2peV0ZGIf9tBuQSQhQSEZYxg-jo5BbUYGJuK2E_qKKGGvmxJzsGCCGylaWgisSKt8MIEiMBMthHW5cC6zD_dn7G5Wje7mv7uN8eC11FgpqHlX98dO0oO3M2yDYpDiOFFcz7JJTMcxPUjINwbqnW7J-iKS3Zvdgztf0eoWEvlO-efn_KAVVU6UtN8FNPRcdsOZRxeqJtqFJ4zO2x0UpVKVd06ZUeCtzd0kw-ktZxLXOjHptvDbukHKqKxqWqTvN-Xm_0LT-nzme0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b72f7ffdf7.mp4?token=HR-rLjwSiJ7x9Id5CLclAjrHIWCcOBfBUyUWA3GyZu4R38WkoFCgtMnxtcgiUP7zWGIZUpGGjoiAzLfFCBeqlx7eUybM_34uU9ds_xiUgAjIO8lX4xDpsXjmZXSccdXNnOfaH7TrbTq-NfzFlFx5h0fopWR6IF2s2GtnuE_tXUsI_FgSsCy_iQdzcqv-ZzUszsQ_0-ckvq1xxeTsrPJTWrq4lDn3d3Pme-Vs6SwWP8vt4BCdvogNXxAtenVpTs2QfHEuyIlGN-B3ZBWa1r4RuALgRYFcTJQxi1809Yt2sXB0inQvFtVQ0IgCb416xlpqmlIu4f6XP9I9abv_JDF1uUF0LroPnqn690Oc8pwR-GzvK8bORpLGiiG9UmWMza0RQBIsDe-7l9gotdV3vUxWct9SfqirRGsI2peV0ZGIf9tBuQSQhQSEZYxg-jo5BbUYGJuK2E_qKKGGvmxJzsGCCGylaWgisSKt8MIEiMBMthHW5cC6zD_dn7G5Wje7mv7uN8eC11FgpqHlX98dO0oO3M2yDYpDiOFFcz7JJTMcxPUjINwbqnW7J-iKS3Zvdgztf0eoWEvlO-efn_KAVVU6UtN8FNPRcdsOZRxeqJtqFJ4zO2x0UpVKVd06ZUeCtzd0kw-ktZxLXOjHptvDbukHKqKxqWqTvN-Xm_0LT-nzme0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پوتین پیام‌رسان بین ایران و اسرائیل
علی صدری‌‎نیا دستیار رسانه‌ای - فرهنگی شهید لاریجانی در «فرهیختگان گپ»:
🔹
اگر خاطرتان باشد پوتین مصاحبه کرد و گفت که نتانیاهو گفته ایران حمله پیش‌دستانه نکند، اسرائیل هم حمله پیش‌دستانه نخواهد کرد. این مساله را آقای لاریجانی به صورت جدی پیگیری کردند؛ چون ما با رژیم صهیونیستی گفت‌وگویی نداریم قرار شد به احترام آقای پوتین این موضوع پیگیری شود.
🔹
آقای لاریجانی یک مسیر دو ماهه را پیگیری کردند [که پاسخ از طریق پوتین ارسال شود] و در نهایت به نقطه‌ای رسید که می‌شد پایان این مرحله از جنگ را اعلام کرد و از مرحله نه جنگ نه صلح عبور کرد اما ماجرای دی‌ماه رقم خورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/679386" target="_blank">📅 13:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679385">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddf08bc391.mp4?token=FgqICuO6OueR6fbzF7ywBVWja5bvMZSA-VuuEooi_zxehhTpp8AEpRiwu0lKyUKC1c8pv3simSvhliFYHmMU6pZ-1SKSEi7KCus1HVzXhLfDXc99yY1Rco28OFTNrJyTCWDFBodz18zzKLv80N2dctLQ7qdBg7I3Wo2s-k8kOFDpLleNWih-nlvAme9_jhIoc7HNp62fY8sYPYV0z3dddBWnmLHSjMQIjlyVdp4yE510TBN0ltx4qnQLheRhGwJgC0KyyXCZpc4GWJ7z2zlerZXfeBQ9e3HjiFwuHQpL6NEVUEr5d3pXodHuPzrRkrLAxzLX8Cd4Kxp38ESZd8L87g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddf08bc391.mp4?token=FgqICuO6OueR6fbzF7ywBVWja5bvMZSA-VuuEooi_zxehhTpp8AEpRiwu0lKyUKC1c8pv3simSvhliFYHmMU6pZ-1SKSEi7KCus1HVzXhLfDXc99yY1Rco28OFTNrJyTCWDFBodz18zzKLv80N2dctLQ7qdBg7I3Wo2s-k8kOFDpLleNWih-nlvAme9_jhIoc7HNp62fY8sYPYV0z3dddBWnmLHSjMQIjlyVdp4yE510TBN0ltx4qnQLheRhGwJgC0KyyXCZpc4GWJ7z2zlerZXfeBQ9e3HjiFwuHQpL6NEVUEr5d3pXodHuPzrRkrLAxzLX8Cd4Kxp38ESZd8L87g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار برای اولین بار؛ تصاویری از رهبر معظم انقلاب سید مجتبی خامنه‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/679385" target="_blank">📅 13:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679384">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
قوه قضاییه: رأی بدوی پرونده کرسنت زنگنه صادر شده و پرونده برای بررسی در مرحله تجدیدنظر قرار دارد.
🔹
بازی‌های لیگ برتر فوتبال با تماشاگر برگزار می‌شود.
🔹
یمن: محاصره هوایی عربستان ۲۴ میلیون مسافر را در ۱۰ سال محروم کرد.
🔹
ثبت‌نام آزمون ارشد علوم پزشکی از امروز آغاز شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/679384" target="_blank">📅 13:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679383">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
وکیل ترامپ در پرونده حق‌السکوت، وزیر دادگستری شد!
🔹
سنای آمریکا پس از چهار ماه و چهار روز از برکناری وزیر دادگستری، با ۵۰ رأی موافق و ۴۹ رأی مخالف تاد بلانش را به عنوان وزیر دادگستری و دادستان کل تأیید کرد.
🔹
بلانش پیش‌تر وکیل ترامپ و از اعضای تیم حقوقی او در پرونده پرداخت حق‌السکوت به «استورمی دنیلز» بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/679383" target="_blank">📅 13:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679382">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ویدیویی پربازدید در شبکه های اجتماعی؛ اینجا یکی از پارک های تهران است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/679382" target="_blank">📅 13:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679381">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_Md5s-FVZMV7lNUTnOeINRDo996ytq1kR53vL_iUzYhPY94eaEQvuzaj72ANDNXep9UrXsVw9BfDOUdzj1NnoWatfMYyErYPQoBgUE0DU0HP5hDtLBUBpcgWuEjQvCL0GgTCVC0jF8bMHciAzgSNaB9srGEqj9ee5mUCLI0xJyfSI9Oi0Zlwihe0QhOqjzDO2Gw8Ok-A5I2Nm5M__ve8LPIl1buZZnRqyFxI-WiCiNTpbE0yLpYvkYuBHUWDl3EoHvNmrCrBVhUiILWVRe64Oa-O7O4F22ZILQN0E4uAFXWhlE9W_K07Bc12NbyZGTJ2Al0Lh8m7J6M-99I5e0_rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز خبرنگار را به تمام همکاران رسانه‌ای تبریک می‌گوییم
@Fori_Graphi</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/679381" target="_blank">📅 13:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679379">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c515b0cb32.mp4?token=ViLPcV8fAaJm3lUq4pb_6FV0R8-aCmvXaY5f5gKe1vtXejn5jYDGCV70erfKvHZsGs4jlftIDhaqa6lwieNo6prMhmcO144LnqbH-zX9hwd2XOgFzqrIEZqto6qsmQCwilfiDumWDvj9X7TRMNR11A1uA1fMhGPlfryfLyP9zQtdSpFxZMtLAVB2kMbIlFBR7rmNgpq3MH5lRdeU9Or_iO4FgikhPc6YGNif2b4LLxErS2UFVE_H1n1cfLScWgaZokIIWhu_ciScaRkU1OuB9dQ5BUs9YXu7OMPAnz74WNO8JLViUyerMpYKu154ubTkpjQgg_tPMJSmoeic5YD49mB4T-ZMISHS-RYsNRURH7Bw_XR7xZPWovhcAErxOk7kZPrTuUSqZ84n9wQXNcjm-KTCQCPGscJec3thpOnNYz4SDUo5-zgxwPTOCtGNAYnKzxnqdLbtlLJBl9KqFUbIspufALiWqYfjAdVfDeVzKaRZJPzQSycG6qydOe3aynxh3HKDdzvGHUtwi7gM5TjtonSR7khVFYOqe3v3SOQuNAJgYEYg0RQ8ebqKISeZ2lbTFoQyCOWBBzmbE50AJ7LaeZEw3B7gv90pG9A3xnBAX8jE7ms_TO-N_G8Gaiv-a7zM-ABTTm88lFm_fjKNJau_VjcQ4oVfWg2wsSaClaSSRA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c515b0cb32.mp4?token=ViLPcV8fAaJm3lUq4pb_6FV0R8-aCmvXaY5f5gKe1vtXejn5jYDGCV70erfKvHZsGs4jlftIDhaqa6lwieNo6prMhmcO144LnqbH-zX9hwd2XOgFzqrIEZqto6qsmQCwilfiDumWDvj9X7TRMNR11A1uA1fMhGPlfryfLyP9zQtdSpFxZMtLAVB2kMbIlFBR7rmNgpq3MH5lRdeU9Or_iO4FgikhPc6YGNif2b4LLxErS2UFVE_H1n1cfLScWgaZokIIWhu_ciScaRkU1OuB9dQ5BUs9YXu7OMPAnz74WNO8JLViUyerMpYKu154ubTkpjQgg_tPMJSmoeic5YD49mB4T-ZMISHS-RYsNRURH7Bw_XR7xZPWovhcAErxOk7kZPrTuUSqZ84n9wQXNcjm-KTCQCPGscJec3thpOnNYz4SDUo5-zgxwPTOCtGNAYnKzxnqdLbtlLJBl9KqFUbIspufALiWqYfjAdVfDeVzKaRZJPzQSycG6qydOe3aynxh3HKDdzvGHUtwi7gM5TjtonSR7khVFYOqe3v3SOQuNAJgYEYg0RQ8ebqKISeZ2lbTFoQyCOWBBzmbE50AJ7LaeZEw3B7gv90pG9A3xnBAX8jE7ms_TO-N_G8Gaiv-a7zM-ABTTm88lFm_fjKNJau_VjcQ4oVfWg2wsSaClaSSRA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاید باور نکنید اما تعریف انسان‌ها از عشق، اطلاعات زیادی در مورد شخصیت‌شون میده #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/679379" target="_blank">📅 13:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679378">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
مشاوره تخصصی اتاق تهران برای موفقیت در تجارت بین‌الملل
معاونت امور بین‌الملل و توسعه تجارت اتاق تهران با ارائه مشاوره تخصصی مالی و بانکی بین‌الملل، به فعالان اقتصادی در کاهش ریسک‌های ارزی و اعتباری و تسهیل تجارت خارجی کمک می‌کند.
👈🏻
88725269| واتساپ: 09102669714 |
service.tccim.ir/intl</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/679378" target="_blank">📅 13:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679376">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbPnz4HOO82gbp0QKrsruZzGaKG41bo0VoT63n8OiPkHb5HZQ5c-0chI10nsmQwgvqMjVafLtIJ4zdU2wAOdvCQuAkD6t-PShWBHD0x5tr5qufcmvGGxG84-eSYsXzqt6Ib5-5bOjFEgWqEBkiUDZFTAm-y3f2s_yWrmp4dawX1x8y0Gp9dBpr_ZXWmafs2D_rbzQlotzXs92yESq-51Jf0ILCq19PksJw2IOLEEiDDj7H6uIUEfIU4AmVv2F4oIVCuXV3FGxjC9cvkWWsv9KCliY1TeaVmH4B4FnzqYROCitM7246153WIDH69hvT4xhHCiE3pK9MuiOjyWS0Tq3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جوراب‌ شهباز شریف در مراسم امضا توافق‌ مکه مورد توجه کاربران فضای مجازی قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/679376" target="_blank">📅 12:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679372">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a90971fa.mp4?token=Bph58mKM6a5MvXlN6u5dSFCfK9BasnAf5z68XJZ4rpbIgg2etEHIUhGnLFc37vEj-zL1u2acioxIBTlrT7kS9hgSWY3KRqfJMLSlIPQmybIla67npq1Dra9COypyOXfI0Jp7qMLkp6GyuHM1iWvYAIjzULRjhuUvwOVT1GSGJtHohAmOi6jmHukYclPteG-rHUHcsphB1rVJr2SeR806ntQq3yFHWrsqVRk1SHajQrKdJ7auhkgPorq9sMf9dEvvoAyl1b1aUTfsAohe8h_qf4rdh9XC5orhgFlKTMVlsBRIw8ghVmosVvohprUNPvjkyvm5J6K653SaS93I9dCYcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a90971fa.mp4?token=Bph58mKM6a5MvXlN6u5dSFCfK9BasnAf5z68XJZ4rpbIgg2etEHIUhGnLFc37vEj-zL1u2acioxIBTlrT7kS9hgSWY3KRqfJMLSlIPQmybIla67npq1Dra9COypyOXfI0Jp7qMLkp6GyuHM1iWvYAIjzULRjhuUvwOVT1GSGJtHohAmOi6jmHukYclPteG-rHUHcsphB1rVJr2SeR806ntQq3yFHWrsqVRk1SHajQrKdJ7auhkgPorq9sMf9dEvvoAyl1b1aUTfsAohe8h_qf4rdh9XC5orhgFlKTMVlsBRIw8ghVmosVvohprUNPvjkyvm5J6K653SaS93I9dCYcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دلقکی به نام ترامپ!
🔹
لاولی ایسلامیک ریپابلیک آو ایران؛
جمهوری اسلامی ایرانِ دوست داشتنی(عزیز)
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/679372" target="_blank">📅 12:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679371">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41e57c7fea.mp4?token=e3umGpbEpnSaUluBIoR4xS4Cjvxr9AdfhPwVLXiefzTjYeusGuv6AFpUKjie9iDWCCGUMf4SqYEkWwz25z9ADdllzYIMUx66AuBYx8mPwqYjl32HppNXbzVxXp363RGEkUlDZMJylb9ZpYStAOLNDfFutMtJsf4RQf3u5xRu4KrzQqDbvMcaIeqJm__UEH6TCPjCb9C5t5GM5YJyWrMubxXtqCUTMCGsqB3gXl2XIpvGYOzRIuJcM5oZdC99fr5kdpyOYoGNBXq9TmhnLbnZIRmZyrBN3l2gEDA3NxTnj7M-Gr5gDu7IxCSnGqFrVrIEAkdxcqSfzJl3W3SRVyDQ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41e57c7fea.mp4?token=e3umGpbEpnSaUluBIoR4xS4Cjvxr9AdfhPwVLXiefzTjYeusGuv6AFpUKjie9iDWCCGUMf4SqYEkWwz25z9ADdllzYIMUx66AuBYx8mPwqYjl32HppNXbzVxXp363RGEkUlDZMJylb9ZpYStAOLNDfFutMtJsf4RQf3u5xRu4KrzQqDbvMcaIeqJm__UEH6TCPjCb9C5t5GM5YJyWrMubxXtqCUTMCGsqB3gXl2XIpvGYOzRIuJcM5oZdC99fr5kdpyOYoGNBXq9TmhnLbnZIRmZyrBN3l2gEDA3NxTnj7M-Gr5gDu7IxCSnGqFrVrIEAkdxcqSfzJl3W3SRVyDQ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسب از صاحبش در برابر حمله گاو محافظت کرد
🔹
این اسب هنگام پلاک‌کوبی گوساله تازه‌متولدشده توسط صاحبش، در برابر هجوم گاو ماده از او محافظت کرد.
🔹
اسب‌ها نیز تقریباً دید ۳۶۰ درجه دارند و امکان غافلگیر کردنشان بسیار کم است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/679371" target="_blank">📅 12:34 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679369">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a621cebc7.mp4?token=M7FuL8wUeO9f3OLXLRo9emwIxDHnjDx5_vruwJBuufykVO-f7E2-cdv1t3XKcGtHruMjlvNelyCKWlZx5cYHRW3jNCa17vTEzf1i7TNUmm2m8kNnb8e5y4z-YiSu10bs07MzpXwz41hspOnCGYwooscCzyDsxWrtcmIQJ4mxm6vmlWtraprQTalLBMg7r26sv0wNwP_lhcm7VnxgFZYE0M_FsHBcT2rQsJIc7xyyJjYL2Pqb30CBzLsOGHTsxicHjLvGxei9WToMK_0BiLfuxm-82jFLOSSbMEWnVPBLNlWQOrpxGhbpR_IPLgdNVNMBSMFJrFMpxCPL_kMczQ6P2r5Tso6KjqDsK7mNbvmQCSzQXL5s_bEpTMFaeMubcjI3ynhYGYmXCTJzSLa8-kfvfytX-3BWeV5llsopwiP_bScQ6CorJPSpgdA0ZF1aOS1VVNdHS3htrCu1e_MOG2bYctWY2ekh0dQaHu8w2dV3bPA3fFPKrf0D4HeTjA76d0OoSL6s9jGhiUozHUodLS9Rxdllmrqt4VgKi6AB9iHZvOUgX9Io1kUtEeohTZMcg4Ytr69iP29wVVGtXhlq_jvMBSKrATbJvixvEYRGoeVSCc940cc7XMaqmUZi4nf__b5nMtkzD6XPfgqV5VdR-mva69iL6au2nXPNW0Y5P33vyAE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a621cebc7.mp4?token=M7FuL8wUeO9f3OLXLRo9emwIxDHnjDx5_vruwJBuufykVO-f7E2-cdv1t3XKcGtHruMjlvNelyCKWlZx5cYHRW3jNCa17vTEzf1i7TNUmm2m8kNnb8e5y4z-YiSu10bs07MzpXwz41hspOnCGYwooscCzyDsxWrtcmIQJ4mxm6vmlWtraprQTalLBMg7r26sv0wNwP_lhcm7VnxgFZYE0M_FsHBcT2rQsJIc7xyyJjYL2Pqb30CBzLsOGHTsxicHjLvGxei9WToMK_0BiLfuxm-82jFLOSSbMEWnVPBLNlWQOrpxGhbpR_IPLgdNVNMBSMFJrFMpxCPL_kMczQ6P2r5Tso6KjqDsK7mNbvmQCSzQXL5s_bEpTMFaeMubcjI3ynhYGYmXCTJzSLa8-kfvfytX-3BWeV5llsopwiP_bScQ6CorJPSpgdA0ZF1aOS1VVNdHS3htrCu1e_MOG2bYctWY2ekh0dQaHu8w2dV3bPA3fFPKrf0D4HeTjA76d0OoSL6s9jGhiUozHUodLS9Rxdllmrqt4VgKi6AB9iHZvOUgX9Io1kUtEeohTZMcg4Ytr69iP29wVVGtXhlq_jvMBSKrATbJvixvEYRGoeVSCc940cc7XMaqmUZi4nf__b5nMtkzD6XPfgqV5VdR-mva69iL6au2nXPNW0Y5P33vyAE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بخشی از بگومگوی ناصر هادیان و فواد ایزدی درباره رای‌گیری در شعام درباره تفاهمنامه
فواد ایزدی:
🔹
آمریکایی‌ها تهدیدات سردار حاجی زاده را باور نکردند؛ ایران بعد از جنگ ۱۲ روزه به آن تهدیدها عمل نکرد!
🔹
ترامپ ما را مسخره می‌کرد.
🔹
اعضای شورای عالی امنیت ملی روی مقاله ظریف اجماع کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/679369" target="_blank">📅 12:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679368">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdKECiiaINzfu_iZl1SFozPHh1XSHa_D2nevjvcuYcK4SB-RPWuYX37QgDo5tEa-Pqr9cETF6Jdm2B8HhM7BqHMEQSfibKsW6UpsXc07lqRlmRMilrWsFHoG4qxqpPX1Az-gOptvTp78nuogZ5lTGHvu5kbYJhFOtdUBtHq8UZfEIZzD5N80tcbuRAezJ31FyNmNTRfBC7VkDJ-sGbdZxJFypfkr93w91H9RnTN8s-fgkVhII-8XskYFGDlYlKvmaLfShBhnRz7sIYivklBjPkwbtDaGM_UsHR8y1COcE3TUCnEU1HmIOmkIWJDtWzpZ9IMZnVPGXmr4cVArRcvcrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیمی از بیکاران با کمک خانواده دوام آوردند
🔹
طبق نظرسنجی‌ها نیمی از بیکارشده‌ها با کمک خانواده از دوره بیکاری عبور کردند، نه بیمه و پس‌انداز.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/679368" target="_blank">📅 12:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679367">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwyHzUvrL0uja_XeaDzY3azs8dzkBq2bKYAqtCVmLgrv05FpL97gBK5KoezL0q_wVASAB6780vp8SnwL0X9ius5S29KGWFHfXRPLKC4Afcynz0WVoF8GBzlIoTZne-BvS5n5TDOVSlotDXLtY9l0ZPhNJ4wkavNYuhRPX5ywcs8Y715jduxHG4Z1eTUYnUuKjnsW2NYrm34FRMGs78Tevz3vzQzzxwVxHHkrc07R5_zbgPchkM5dr45q5_NM9Ktrdfg9-g1H6f_D45ST0tkuZinF4-X_WpWMjUDeQ0Ykzeg2Icm1WFzB7bQMtHa8GRQvFrFydSb2rHsdj1RNPeIVnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلای ۱۸ عیار از ۱۹ میلیون گذشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/679367" target="_blank">📅 12:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679366">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbUJbMvYNgdC_g1bhWUqRcBNrHHdDo6kynUrCYNY4E_g15atOPb_FDaPQDTCl8A7pmc-jdKrEJI2Ncze2LqAKFisEKeauxp93i2wffAikaRw3pvADPxpmJ0MOaB7L3vK4YwYJUYqdKr17xvR_585K224Yva2e3CioWvFlTCzPhHc8_2K16gxD9QXhsec_SP5LjW5tWk7Q7aLT8JNP5fjr-Wb-ToCPUcGDZUdEMzAflT-RN-DmCvuGttmqZLyS9f3jDsSr80UI0t7anqsh7wR-ZCOxzzxCer2LNmuEPw8A7F6FGWeAHY2_71gi24QvcAgjI7-tiO0i9G4Kl92qF4RRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدام کشورها بیشترین آب شیرین جهان را دارند؟
🔹
برزیل با ۱۳.۲ درصد از آب شیرین تجدیدپذیر جهان در رتبه نخست قرار دارد و پس از آن روسیه با ۱۰.۱ درصد، کانادا با ۶.۷ درصد و آمریکا با ۶.۶ درصد قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/679366" target="_blank">📅 12:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679362">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a11bc8749.mp4?token=qjGMQbOpEX07y9cUfNMA9e_hGcIIuVVfGT7QMy3myqR9TAyStEk31tmeKrqCFN0uDi9d58zdJOQzwIarqUf5GmLlvjluokOxlwyur_4StvVATdLWPPY7Z3re-r_-FkQKPV33eJmGkWoNswGeNhApziz_N06VydjqT-YiVgDOlAG18ERp-1AuSGxxM8lZ2yMkCQEs7zjw8PqxiLoSaeYj66UJaVl1XAFYGeMma-mk1ghbWOKh_-MDq50GebkKBwHvmYE8hRjFkDYZvrUfRjJSkHAQUCmpc8-JfjHuwaAJ5mWe1x2EviKTtPXJcO2kdkWSD8B4jEgmwYCNpGnc2gdeXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a11bc8749.mp4?token=qjGMQbOpEX07y9cUfNMA9e_hGcIIuVVfGT7QMy3myqR9TAyStEk31tmeKrqCFN0uDi9d58zdJOQzwIarqUf5GmLlvjluokOxlwyur_4StvVATdLWPPY7Z3re-r_-FkQKPV33eJmGkWoNswGeNhApziz_N06VydjqT-YiVgDOlAG18ERp-1AuSGxxM8lZ2yMkCQEs7zjw8PqxiLoSaeYj66UJaVl1XAFYGeMma-mk1ghbWOKh_-MDq50GebkKBwHvmYE8hRjFkDYZvrUfRjJSkHAQUCmpc8-JfjHuwaAJ5mWe1x2EviKTtPXJcO2kdkWSD8B4jEgmwYCNpGnc2gdeXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری جالب از برخورد صاعقه به ساختمان مرکز تجارت جهانی اسپیرز در نیویورک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/679362" target="_blank">📅 11:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679361">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49688f542c.mp4?token=PO9NWYqZtYL1YTJyiiEPFKko9q20Qd23RiQV-EXaDyil347nrap7uUQ7rNFm148QnUbYunDhHsbRmt929pb9s_qg2f9vr1u8IEpBdbS34NFt3XPduwqZbUYePMCZVkxL4-os7RF4Aai2octMihjUzUFxtawp6Yk2dz2HZMwbHD-XSM9xWATXZV2ZCqfgzUIsXXCco5_cpcMJQ6DSSlgT4qiEF2CHhWt4SIiFGmAthEZg4FNq89s_wZTW6aogtyGVF6CodxFo-slq5zaKH-n_I9fArUB1_pcReJoHCmyNMbzEPREpH8wr5wCCHWC1Q9QQKyxUliJ915ojGe9T_UpZmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49688f542c.mp4?token=PO9NWYqZtYL1YTJyiiEPFKko9q20Qd23RiQV-EXaDyil347nrap7uUQ7rNFm148QnUbYunDhHsbRmt929pb9s_qg2f9vr1u8IEpBdbS34NFt3XPduwqZbUYePMCZVkxL4-os7RF4Aai2octMihjUzUFxtawp6Yk2dz2HZMwbHD-XSM9xWATXZV2ZCqfgzUIsXXCco5_cpcMJQ6DSSlgT4qiEF2CHhWt4SIiFGmAthEZg4FNq89s_wZTW6aogtyGVF6CodxFo-slq5zaKH-n_I9fArUB1_pcReJoHCmyNMbzEPREpH8wr5wCCHWC1Q9QQKyxUliJ915ojGe9T_UpZmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش امام جمعه اردبیل به سخنان باقر خرازی  آیت‌الله سید حسن عاملی:
🔹
از دستگاه قضایی سوالی داریم شخصی خبر دروغ به رهبری بسته و دفتر رهبری با صراحت آن را انکار کرده است آیا این جرم است یا خیر؟ قطعاً جرم بسیار بزرگی است چون علاوه بر ضربه به جایگاه رهبری هزینه…</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/679361" target="_blank">📅 11:39 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679359">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fbc4940d.mp4?token=u73i-ipTsaHk11iCcz1x9A1Yk5b97x_eND4i9iavao9HUApcDtDNeeU8v-2aWHVN6dsWdoBnACLrVFjJbNoFoWDcr0TghUFcUVrIjgOUrYbgnn6GPWgqkzzvF-ZR43EhJKoldxTfiir0Oy9rxA0zjKvjeUsUBhmP6heI_Wd7K5koWcUniPfnzD-cb68Wm91sS6dQJm-atFXOf9K6ND-CQ4BfjivX63_kGwQKk6F9y-1ntEAGRUtRPhRmKCVr42DLjIuQpWzagzGCX9XF1e0F7zVJdfg1qXI_7_4kM8KxMmeXiqflS276B3cOk_KoRT_8FFbtuNbcllzqmCYf5eKy4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fbc4940d.mp4?token=u73i-ipTsaHk11iCcz1x9A1Yk5b97x_eND4i9iavao9HUApcDtDNeeU8v-2aWHVN6dsWdoBnACLrVFjJbNoFoWDcr0TghUFcUVrIjgOUrYbgnn6GPWgqkzzvF-ZR43EhJKoldxTfiir0Oy9rxA0zjKvjeUsUBhmP6heI_Wd7K5koWcUniPfnzD-cb68Wm91sS6dQJm-atFXOf9K6ND-CQ4BfjivX63_kGwQKk6F9y-1ntEAGRUtRPhRmKCVr42DLjIuQpWzagzGCX9XF1e0F7zVJdfg1qXI_7_4kM8KxMmeXiqflS276B3cOk_KoRT_8FFbtuNbcllzqmCYf5eKy4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ورود زوار اربعین به کشور ۴ روز بعد از اربعین؛ ساعت ۹:۳۰ - مرز مهران
#چشم_به_راهیم
#۲۸_صفر
#شهادت_امام_رضا
#سازمان_راهداری_و_حمل‌ونقل_جاده‌ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/679359" target="_blank">📅 11:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679357">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-CvpbOZ0CpjBEDqrcHtC7F0LG7wmEdJnqR-h6Ypgbn5hE1f_5QnBgRx1Mzz0-gDLtcZVONsriYEgwwN-_26k8uWLOIOGbok1rdfb1Q4j35bboWq7QsUMQyVg2ImYW9U-hPxkXQ_fNGUcOpm-MYTb3XgDS0G6VHVly54PgDPrmCKltjFCxIgtaHkleLEcZh5gU7D59zlFfL1iXhV1GFnKZzogmbN21ZPXk1iySyTZX1so5bnXhGmucys0bawQAesKHLlcZRg8Z22awjoF_mted0VQRncfPGeCaFqVyQM5I7uxZYgxQuBTCe19GiyRMJ86Ia_oqzsSliHPhEdY6dfrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیاین باهم شربت خشک که ترند این‌ روزهاست رو درست کنیم  موادلازم:
🔹
پودر شکر، یا پودر قند و یا پودر نبات یک لیوان
🔹
تخم‌شربتی و خاکشیر یک قاشق‌غذاخوری
🔹
زعفران
🔹
آبلیمو یک قاشق‌چای‌خوری
🔹
گلاب یک قاشق‌چای‌خوری #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/679357" target="_blank">📅 11:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679356">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06460460cd.mp4?token=kqZTiypvPhRTOaLBtWY7FYsbIuRLVdPiBFWYGHaYZ6zwwv6ynthWbQTf42UDW-n_eN3Wuy3lk1Q6CM-au5Pm89l6aId_bhIicBcEYUlPbqI38T-HjGLpIBSLxA7c8zcxziOljvy4VV5iyCnEchcv5-Ri1yqG_ftuXDRY-1wbCit1uoN-PkMRjNhaQXcSPqLbun3eUAmW9HvPh1RolIDCik3Mx9q9KmpidKZW_pPVuSAddob2K4Fg_u970OeCxmbWzYx-DHR-o-KrX6Ot7gFPIZSMx44_mwvSddiBUL62A0hahWt8JJLFafFhkIvb5SPBEGlPFIDb8wK5pYtPFikR6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06460460cd.mp4?token=kqZTiypvPhRTOaLBtWY7FYsbIuRLVdPiBFWYGHaYZ6zwwv6ynthWbQTf42UDW-n_eN3Wuy3lk1Q6CM-au5Pm89l6aId_bhIicBcEYUlPbqI38T-HjGLpIBSLxA7c8zcxziOljvy4VV5iyCnEchcv5-Ri1yqG_ftuXDRY-1wbCit1uoN-PkMRjNhaQXcSPqLbun3eUAmW9HvPh1RolIDCik3Mx9q9KmpidKZW_pPVuSAddob2K4Fg_u970OeCxmbWzYx-DHR-o-KrX6Ot7gFPIZSMx44_mwvSddiBUL62A0hahWt8JJLFafFhkIvb5SPBEGlPFIDb8wK5pYtPFikR6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چگونه مانیتور ICU را بخوانیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/679356" target="_blank">📅 11:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679355">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25f1224bf2.mp4?token=tG8sqbXFkUf6MMr2muvj5S6ZXoHX3zoBsYHzPOtUgKUgU7H5Bp2td76oew3ues_ABrVvIjrZmo_tGDw5nagRNxfOKoy6y4LFsBKpvlrPlFCnpA0luNsLut1rte8Wv4MgVdpiY93XDP9sMO_J_BcNM8l49o7B-Zd_MuLdvQmfuRn5DVjsoqUnJ5ROeG64MNUE1dIwOSJAG719VXFAyoKdVQEQNJlIU8gUZ8MEjnexxwbELM_QjpEOaTW7VIbH2WteuelUDCGreLktPzZNwVpNI3nb9A0XBauBVeXMls_JIFBJwFZGKcWDvHCare8xo15FkrfNhRRTRJyzBLldEGXZFk48Hyb4MDxCv4xMHP3nDb3fTe43QVL3HCLPxX2rOzFRGHakVA3Rk9UVpx0-dlz_8MQQeabHILkeeiFFG0LcoKydrFBz7r5iWkhJVieckwQ8Dk38iOct7vRjUO9kjY5Ntxv1ZOcyuIjryfejTU06k0siRW0VdVLinfzsV3RrIesViT5wMEFq6SdrGM0MXqtHNBQiDUyMOE25HMa5r1qXE7iOE1B450AW_PXSvqvoGDcp8zEweCmRZfGgOr_Pt_QeL8Ow95sOuL1UGxv8DAFNQnfPUGgWebgdWf08kJc3NCDr-hJSI9Zn-F4GiHVn9seQd2MmHl6gSY1YLOY0ADGWg_c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25f1224bf2.mp4?token=tG8sqbXFkUf6MMr2muvj5S6ZXoHX3zoBsYHzPOtUgKUgU7H5Bp2td76oew3ues_ABrVvIjrZmo_tGDw5nagRNxfOKoy6y4LFsBKpvlrPlFCnpA0luNsLut1rte8Wv4MgVdpiY93XDP9sMO_J_BcNM8l49o7B-Zd_MuLdvQmfuRn5DVjsoqUnJ5ROeG64MNUE1dIwOSJAG719VXFAyoKdVQEQNJlIU8gUZ8MEjnexxwbELM_QjpEOaTW7VIbH2WteuelUDCGreLktPzZNwVpNI3nb9A0XBauBVeXMls_JIFBJwFZGKcWDvHCare8xo15FkrfNhRRTRJyzBLldEGXZFk48Hyb4MDxCv4xMHP3nDb3fTe43QVL3HCLPxX2rOzFRGHakVA3Rk9UVpx0-dlz_8MQQeabHILkeeiFFG0LcoKydrFBz7r5iWkhJVieckwQ8Dk38iOct7vRjUO9kjY5Ntxv1ZOcyuIjryfejTU06k0siRW0VdVLinfzsV3RrIesViT5wMEFq6SdrGM0MXqtHNBQiDUyMOE25HMa5r1qXE7iOE1B450AW_PXSvqvoGDcp8zEweCmRZfGgOr_Pt_QeL8Ow95sOuL1UGxv8DAFNQnfPUGgWebgdWf08kJc3NCDr-hJSI9Zn-F4GiHVn9seQd2MmHl6gSY1YLOY0ADGWg_c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قوه‌قضاییه: ساعدی‌نیا اجازه کافه‌داری ندارد
🔹
بر اساس حکم بدوی، صادق ساعدی‌نیا از فعالیت در حوزه کافه‌داری محروم شده و دستور پلمپ تمامی شعب کافه‌های او همچنان برقرار است. بر اساس اعلام مرجع مربوط، در صورت فعالیت مجدد واحدهای متخلف پلمپ و جریمه خواهند شد.…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/679355" target="_blank">📅 11:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679353">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyxJXOrN7NTMy3aCKSe640nBat-pE5UZhsWPuYouMREKhCFTUSOLGkiBWoXjesRsC7yKGeG5ANOVJ4GCHyHX3OF33ecLASa1EYLuRzVO87GDYCxT54X9flOt-gIiAp04YEkrAQTXSGdVrDKPKTOekVHVoqEms8lj-8TRCUvqvg7pvJ2J0or2__u6asnb9IVSFvBqBjO83XMwgiosoCaJCZGgclnWd_emRqwOVdYY1du_0B0zmMC100XKXnvJnfmXkt9Zw9r_UPTNwCqemWOYjXtSjhlv3ugc7Cp4BN9MVEDrbF2zPMG_tu-ffZvyPvEQLBiBfL5ErjMEGIiyAkNU3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تأیید یک مورد ربایش و قتل؛ تحقیقات برای شناسایی عاملان آغاز شد
یک منبع آگاه با تأیید ربایش و قتل حمیدرضا رجب‌زاده:
🔹
او چند روز پیش ناپدید شده و پس از آن ویدئویی از لحظه قتل برای خانواده‌اش ارسال شده است.
🔹
تحقیقات پلیسی و قضایی برای شناسایی و دستگیری عاملان ادامه دارد./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/679353" target="_blank">📅 10:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679352">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
آتش‌سوزی یک کشتی دیگر در تنگه هرمز
🔹
پایش‌های ماهواره‌ای از آتش‌سوزی احتمالی یک نفتکش در مسیر جنوبی تنگه هرمز خبر می‌دهد؛ شناور اطفای حریق «ادنوک ای‌آر۰۱» به محل حادثه اعزام شده است./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/679352" target="_blank">📅 10:43 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679351">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
دریاچهٔ ارومیه جان گرفت
شرکت آب منطقه‌ای آذربایجان‌شرقی:
🔹
حجم آب ورودی به دریاچهٔ ارومیه از ۴.۵ میلیارد مترمکعب در سال آبی جاری عبور کرد؛ این میزان، بالاتر از حقابهٔ تعیین‌شده برای دریاچه بوده و بیانگر بهبود شرایط آبی این پهنه نسبت به سال‌های گذشته است.
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/679351" target="_blank">📅 10:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679348">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LDPuWJQ70JSlCafaRofke-aTATsG5jYI1ivaQcLZv7DGvn1GTYsxoifH4kImXgtLQ6z2lvrdRlzkhIwg7xpZ_F1WGH-_h_qlb8ro8cDNSxHO6nGeyCQwEe2wuGCtqdrjMerqsBMRaSr-cNEPKeWCXAFk65vzGQ2n2z1Qc1DdCeDzqeF3cLyfpcatz6V_remiYzGz3VEHOeqxMXdJdWZ1mCfGhGtya2TMJNXZ3PR0S-eTDB-_OMKi3gi4NXJ9tY6TuQTKQQ87kpoeqvrYxZXo2jCLzaBJkVSx7lsgNsroS-wa-PKd64HwxJwDaKzbAygfN9jkHF4ZCqFKx-R6xEXtyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iPJhCx1UK-Qn5IchVolLfxZEkVmSBQup8tl7Ko0gG_LlrAs0x3LYBdDbokvtMxiZCjSRT1KzKHhJbjPcPvbwyH9KWdONIsyBul_LTcYwMzrzpRVSQO6W6pF3IV5YYlAOmzeMCrrQC7xFtYbXdZO7sdfd6c_XeMp86yyZXADfl1vhF48Mb6-gbzRnQXSOPFHpKXnkirVvvTtRpig0DjvqkAq4JSA1uU0q6h67eLgKxSUolzvE_H9TIBeXRyeRU6Tgk5yi0IrtlHmKmHwGJKep8nvBcmrPGS3oMjh_mQY20zrCq2xD8y4uvM0PuzRj4xs68nz-XukcM0DgegDoOo4ZCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B0bPOdDkSBy9IcBa2jEvw6XXSOyJkeUXBdC9Vwfxet0v_ZZYGEMoScEo7R6B0NK8G-jav3RNaNoePx32hYTMa_2KavwDRRUVlyWAoJUC823LiqCHzAkqgnkCRNgYHloPMk_Q4X9zFRKMGlDqnfAJ1l3ujrC8gNWD9ih1EEif9uuPjEZNzYhTZ0Pn04C4q6GKBOp2Ko__TIfM8--zkB3vu14wTPw1hJ8JUniwHkzPK422ejXk_5QZtGgUqaSL0PpTs429emeG0zg-BT2Vq-9ZCrbI6O0VKCkmqAYtaYpJkT1N65n-aim-y5ZPZdKNDFsyLUF8Ch6krzksKty6edoGoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دفترچه‌ای برای گوشه‌ لپ‌تاپ!
🔹
یک طراحی ساده اما هوشمندانه؛ دفترچه‌ای با برش زاویه‌دار که دقیقاً کنار لپ‌تاپ قرار می‌گیرد، بدون اینکه مزاحم کیبورد و موس شود.
🔹
گاهی یک تغییر کوچک در طراحی، می‌تواند یک وسیله معمولی را بسیار کاربردی‌تر کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/679348" target="_blank">📅 10:34 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679345">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3sUCX8b7ZInyP8wuCIfPwhOkAYGrZ_aoPNR4SpbNf055HiiWR0baoNaPsMY5E6NsU_c9uNKeF3l5SsjpHB_QrlUZuRSG715ImOvab0okjueqgd11Kgvl7jTHBtuoHOcpZlx4Qtg1z80ySZG1PBQ5zjtwqFiax61P-kXjXw5wbsvkPbJJP8KsQM33x3CdTSwMX6HI_3dXLHRSqCIs1h7VyuRGcpDay_yGq8-RK4_hdiRUjSRR3c6sMe-AhEnQoRZ0E9mCrcP-NbSPWOQs_o9noMLURPy__gfcAIgBG27Tq0lUXP2HNtWb4JnS6q2-frd8nhTSxWJ0Ho6BDIlrJuAcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دلایل پارگی رگ خونی در چشم؛ چه موقع باید به پزشک مراجعه کنیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/679345" target="_blank">📅 10:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679342">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
رئیس فیفا دست به دامن سگ زرد شد  بن جیکوبز، خبرنگار انگلیسی:
🔹
جیانی اینفانتینو قرار است با مقامات ارشد دولت ترامپ دیدار کند.
🔹
او به دنبال جلب حمایت برای ادامه فعالیت خود در فیفا است.
🔹
اینفانتینو در حالی که فشارهای فزاینده برای استعفای او شدت گرفته، با فدراسیون‌ها…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/679342" target="_blank">📅 10:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679340">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obeFvs7ozIcS2wFBXQyjMTjfUmVRUGiIwDfAEsteP9xu7J04Ab4WQkqKN3BXfeCltoidgY8QBhhnsRsQpPGGt9SdBdFOttoL2UifZmCBAInWfrR1ERY7oGKeHJ_Hlo9CJSxh0oZ2-lxjPqDVyoElBFc9PMLIVEcoN12NmnLGURYb6EmTKshNAhihkXn-KVK3EkWnbwD2n0fheQhcjQS8rr8ktUdg-gcHGkQr0AxwLZaFETyjsPPQIq1h8SX6gy5vId7-lrZff3KUVMdVFcq5V3WoJ2yqWdlPCcFjf4TZP4919l1G56GX7-TbfqETHdGrOoNxQ6R1Sb-yQvn8l9iFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۱ سناتور آمریکایی برای توقف جنگ علیه ایران قطعنامه ارائه کردند
🔹
۱۱ سناتور دموکرات آمریکایی با ارائه قطعنامه‌ای در کنگره، خواستار خروج نیروهای مسلح این کشور از هرگونه عملیات نظامی علیه ایران شدند.
🔹
«جان آمریکایی‌ها از دست رفته است. قیمت بنزین و کودهای شیمیایی به‌شدت افزایش یافته و ذخایر تسلیحاتی ارتش ما تحلیل رفته است» این اظهارات سناتور آمریکایی جان هیکنلوپر در پیامی در ایکس است. او در ادامه نوشت «به این جنگ پایان دهید. همین حالا».
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/679340" target="_blank">📅 10:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679339">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea6ad6f88.mp4?token=QmGFOchddXOV6kYNw1N2QDYNpPAsGGnirePmBrAPC6lFN_eFrci1zjZr-KcKnqbzIYTKPxW0y1bQ2KOQofTLrztCUldAgsgwwTaBokSQjLivi3_38WL-xU5qrItMCqBBDmte5Oqy73RuSAFN86eZJasvGo_1G3W-iiHyd5P0LBl3hHvYHqC3-Mh6sibSba0YVJvb_T13pIDisJM5aEBQ4YFY1vm72YJIeJyA-v6kRVdO6PCLc8imcn3IE9DSmLJXpH3onQPc6ZuirLe0twvO34iPQVbxq1VCIHECfNqJ5eU_d1EAkXYlXh4DZ36QocHaav_nZn9CWfstZvRHFcApIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea6ad6f88.mp4?token=QmGFOchddXOV6kYNw1N2QDYNpPAsGGnirePmBrAPC6lFN_eFrci1zjZr-KcKnqbzIYTKPxW0y1bQ2KOQofTLrztCUldAgsgwwTaBokSQjLivi3_38WL-xU5qrItMCqBBDmte5Oqy73RuSAFN86eZJasvGo_1G3W-iiHyd5P0LBl3hHvYHqC3-Mh6sibSba0YVJvb_T13pIDisJM5aEBQ4YFY1vm72YJIeJyA-v6kRVdO6PCLc8imcn3IE9DSmLJXpH3onQPc6ZuirLe0twvO34iPQVbxq1VCIHECfNqJ5eU_d1EAkXYlXh4DZ36QocHaav_nZn9CWfstZvRHFcApIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موجودات عجیب و غریب خلیج فارس
🔹
لیسه دریایی
🔹
عروس دریایی دکمه‌ای یا چشم زخمی
🔹
عروس دریایی مهتابی
🔹
حلزون تی
🔹
شقایق دریایی
🔹
خرگوش دریایی
🔹
طوطیای دریایی یا خارپشت دریایی
🔹
پاتریک
🔹
خرگوش دریایی سیاه سم بنفش
🔹
ماهی گلخورک یا اشلمبو که از قدیمترین موجودات دنیاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/679339" target="_blank">📅 10:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679338">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn6N4qlCvDnIOEOWzcedXohXJ2m5OeYU86c4RJO3fUbjH1aenfqSAnf18hHZgDEN_S2zxXCpQfdulqaXDYZkXgeqyZIzzvaQat7GjcbYe9Q_TNk1Rt9s9QsN8_WMdk_p5ohhHZkhqWAQAaIJmJxMQvcDjHRvU1ssKw9VGCQmwjB7_x3Gf1vSFVf0BvkDBBoNy8_TS8DXss6mlFd8vFoXO8BVFVI0balNzV5Y6p7TpJOlB_bhyMKTRm9sb2cWZ7pDQ65wg3Cd0tfrtttLzd4ZMGuZqvd-MxMkznTUaWsO27QkNReJWMgUfLSqy06r6GE9kphjvoi6TbA_29midEOC2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕌
فروش ویژه فرش سجاده آریا | طرح ویژه دهه پایانی صفر
⏳
این شرایط ویژه فقط تا سالروز شهادت امام رضا (ع) برقرار است.
🔥
فرش ۷۰۰ شانه بخرید، با قیمت ۴۴۰ شانه پرداخت کنید.
✅
۲۰ تا ۶۰٪ تخفیف
✅
خرید مستقیم از کارخانه
✅
فروش اقساطی
✅
ضمانت ۱۵ ساله
اگر به دنبال فرش سجاده‌ای با کیفیت واقعی و قیمت اقتصادی هستید، همین الان تماس بگیرید
📣
درخواست قیمت و کاتالوگ فرش سجاده تماس یا ارسال عدد  1 از طریق
👇
شماره: 09128044740
آی دی:
@Farshsajadeharia
💫
💫
فرش سجاده آریا
💫
💫
https://t.me/aryiacarpet</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/679338" target="_blank">📅 10:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679336">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
صدها نفر مثل علی خامنه‌ای در این راه جان و آبرو خواهند داد
رهبر شهید در ۱۳۷۹/۰۴/۱۹:
🔹
مسئولیت رهبری حفظ نظام و انقلاب است... رهبری یک عنوان و یک شخصیت و یک حقیقت برگرفته از ایمان و محبت و عشق و عاطفه مردم و یک آبروست.
🔹
صدها نفر مثل علی خامنه‌ای در راه این حقیقت جان و آبرویشان را می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/679336" target="_blank">📅 09:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679334">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddzTFu3UCgZxjDpNvwiYA7cQ_HUWtsrsKyecGRA_pv98aAwue_e1Ko95zlAkLiaJKFGOVUKvAYhC2Nl81BBgvyn6apirwIjhBePpIYQUM26gyzYnXcW68EqpWlEz3wWFi9JwtQNs1kb3Wxj3ssIQSkWhZBVsNTzAy6jNYFXscm054mOYJSgKegSHvzfvKbKzGPlLGT5pquHaFeT2npLo09Mt8d0lsPHo8tq5gIyvsHGGNFgLck_tICsZ6rp8OVpNdIStDEUNmRM-w7hrsZCM9Dkk1-kpomRSfDm4QxahTKTdUNMepBwXooo5fOi-M8LX7aS5Lumewp_4ZPc5VSA15g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگاری شغل سختی است چون باید طوری از مشکل بگویی که امید زنده‌تر شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/679334" target="_blank">📅 09:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679327">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/peHYY5ioPMPUl0t-WbnRqtUn4DBvYhH0-aG0gJ8nXawQcJbfcaCucSqkxTnFcAxFy187839c_n6ktBz8WQe1eFovd6iVnfzKgrAbJ6GhATI-pmJTf9Og6QJijssYLqf7lN1_eQRPtlePp9kjbAiUzt3JRry1BWNcGZUmSps-AiqXt15whzTEgKWbevsXnhKAL1xftTY5-rz2LKWQdCdBhvcNiPerPr8HFnXG8OmJTAtf0JxEWtbum6ImhtUthcPBAo0bqzxS_wA2jpZt7Y9fBndCk_trpW8g-ZYCZfCY-4bSyjBuSaBOAAFiq13ZlSAYUDEwrX7CbZQCrmsACKdQlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک کامیون با راننده ۸ ساله در محور شاهین شهر کاشان توقیف شد./مهر
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/679327" target="_blank">📅 09:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679321">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
پیش‌فروش ساختمان فقط با سند رسمی معتبر امکان‌پذیر است
دادگستری اصفهان:
🔹
مهم‌ترین نکته این است که مردم بدانند قرارداد پیش‌فروش ساختمان باید حتماً به‌صورت رسمی تنظیم شود و خریداران نباید به قراردادهای عادی اکتفا کنند.
🔹
پیش از معامله، حتماً مدارک و صلاحیت قانونی پیش‌فروشنده بررسی شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/679321" target="_blank">📅 08:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679320">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98c7c72b59.mp4?token=h89ImvuTn6Y0kqZJ4Dj-1mBKGxI0K5-siTA2iURopuixqyAY0D8_ZmY4FqqVoOMUclP_cLHdLob2x4eu8dHJegeVxH8HTUFxR3O0Pwrpd5xb8ZncbwPkJ5W0yHWjYugnJhkWOVleVPgRLPYdS2hWpGLPIN5WO9hf6sIEgOv0ZCSiaEXJn3rXrh0LbQJcJ578RtlDbyTNgECHMt3FnZuPbvR6YAYszYks3YZ3qrnNmaDOFvyXYFU7lQptxMY2FtIhHNeOkAHBdG_pLzUblq00njuuAEtHVaCCKaaQMfM00u7BR3rq8zjFr4Keiv1ESJiq60I_cXNrm5SL6lMXX1phbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98c7c72b59.mp4?token=h89ImvuTn6Y0kqZJ4Dj-1mBKGxI0K5-siTA2iURopuixqyAY0D8_ZmY4FqqVoOMUclP_cLHdLob2x4eu8dHJegeVxH8HTUFxR3O0Pwrpd5xb8ZncbwPkJ5W0yHWjYugnJhkWOVleVPgRLPYdS2hWpGLPIN5WO9hf6sIEgOv0ZCSiaEXJn3rXrh0LbQJcJ578RtlDbyTNgECHMt3FnZuPbvR6YAYszYks3YZ3qrnNmaDOFvyXYFU7lQptxMY2FtIhHNeOkAHBdG_pLzUblq00njuuAEtHVaCCKaaQMfM00u7BR3rq8zjFr4Keiv1ESJiq60I_cXNrm5SL6lMXX1phbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سانسورچی‌ها ناتوان از پنهان‌کردن ضربات کوبندهٔ ایران بر ارتش آمریکا
🔹
وقتی قدرت نظامی ایران و ضربات کوبندهٔ رزمندگان جان‌برکف ارتش و سپاه بر پیکرهٔ ارتش آمریکا آنقدر خسارت‌بار است که با وجود سانسورهای گسترده هم نمی‌شود پنهانش کرد. ‌
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/679320" target="_blank">📅 08:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679319">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54ace74ac9.mp4?token=ZfYGih6-ZR3kHpcTbohNRL5vZUpyqdy2yMxctq4lGMWHdsPdNxUOy1EYRQ1KmHgGEFTT6JmeyJ9gAwY5nyqdA5FbGAt8QayIR7S1J7QDbv2L97B6zk3LLhCD5Le35d-TMoGBze4j1yle-gaekyGYLtDRP9NRP7_rAYtU9ZfEvuV-uuTQILL6UsjYfmsw-LqGa_Z3YA7bwD08u0sD2vVzgMyQi1G5IgQKjF40_du9LbYp1u9iZoKh8h1ApAP6WMnl2lVRR29jk8_TUuKjdlYAvul7oQXtPpL8MQvL2qRTjcwKUXqm-QgvNW89F3Vf76k_dkoeMBsc0K0kAeM7FMt_syOb60562_BY_ifTH_MeHHlM0_A35q4Fc7Qltk8hb9JEfj5pDE6tW1AryA598nvkNKimXfn6UbeBOjUtxnJrZ3nZtyOiVq90YrNnXctsHByWMDy1dI1IOXYhbDTV3nHN7WguCIrYx7w_qD4oMeijdxtlkaq3LCAtprGK7G73xBbgaXz2fJTuTw-Bm1YrG8zAzRjQlp0PuidIvZAU6Z0dxTpqkTuqfkRgf7SLxusYCi-TN3_gEvUUK9lnPFJ8l3RPNZzUPHB_2D2Y52BvHwU9GBr_zc5LhXVkiASPm7SbU2-dv_p6_uXlYysBp_kvh0IovPat0uCSLa0IkdMI1j06_eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54ace74ac9.mp4?token=ZfYGih6-ZR3kHpcTbohNRL5vZUpyqdy2yMxctq4lGMWHdsPdNxUOy1EYRQ1KmHgGEFTT6JmeyJ9gAwY5nyqdA5FbGAt8QayIR7S1J7QDbv2L97B6zk3LLhCD5Le35d-TMoGBze4j1yle-gaekyGYLtDRP9NRP7_rAYtU9ZfEvuV-uuTQILL6UsjYfmsw-LqGa_Z3YA7bwD08u0sD2vVzgMyQi1G5IgQKjF40_du9LbYp1u9iZoKh8h1ApAP6WMnl2lVRR29jk8_TUuKjdlYAvul7oQXtPpL8MQvL2qRTjcwKUXqm-QgvNW89F3Vf76k_dkoeMBsc0K0kAeM7FMt_syOb60562_BY_ifTH_MeHHlM0_A35q4Fc7Qltk8hb9JEfj5pDE6tW1AryA598nvkNKimXfn6UbeBOjUtxnJrZ3nZtyOiVq90YrNnXctsHByWMDy1dI1IOXYhbDTV3nHN7WguCIrYx7w_qD4oMeijdxtlkaq3LCAtprGK7G73xBbgaXz2fJTuTw-Bm1YrG8zAzRjQlp0PuidIvZAU6Z0dxTpqkTuqfkRgf7SLxusYCi-TN3_gEvUUK9lnPFJ8l3RPNZzUPHB_2D2Y52BvHwU9GBr_zc5LhXVkiASPm7SbU2-dv_p6_uXlYysBp_kvh0IovPat0uCSLa0IkdMI1j06_eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیام رزمندگان نیروی زمینی سپاه مستقر در جزایر خلیج‌فارس به مردم همیشه در صحنه ایران اسلامی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/679319" target="_blank">📅 08:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679317">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ادعای ای‌بی‌سی به نقل از مقامات آمریکایی: توافق ایران و عمان ۶۰ روزه خواهد بود و در این مدت برای توافق بلندمدت، گشایش کامل تنگه هرمز و ادامه مذاکرات هسته‌ای تلاش می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/679317" target="_blank">📅 08:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679311">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dac9b82c54.mp4?token=bAZa0s1bttd_UgF9O0xKhpTfaml8BOhwW0GzBVH3nKkkT9P-8xmndw2RoETnc63TuWsLd1ezCKZDB0YdcWDVb6YrDFcM7VLmzFaGgZglGDx1_pSh-h89uVE0e3jYibaLhg4eAG2BVEloxcPv-7K-l5TxzTdmltKwVZ0uDsJ2VWakTiMkzmQ4xCjnoTXcimDOWCOLsHa7OF-ahuygi4MoCrtk41KwW43hJWQdo9Qu5nfPlUANErMxBYU6iAlySnQzkHYM5ghFjPcrVFf8jftPWfeWtEskWR93GrZza8w3KemdjeLmT5skhDhUMyxzuZvztsdqkTEHo5be3DI-v_jiOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dac9b82c54.mp4?token=bAZa0s1bttd_UgF9O0xKhpTfaml8BOhwW0GzBVH3nKkkT9P-8xmndw2RoETnc63TuWsLd1ezCKZDB0YdcWDVb6YrDFcM7VLmzFaGgZglGDx1_pSh-h89uVE0e3jYibaLhg4eAG2BVEloxcPv-7K-l5TxzTdmltKwVZ0uDsJ2VWakTiMkzmQ4xCjnoTXcimDOWCOLsHa7OF-ahuygi4MoCrtk41KwW43hJWQdo9Qu5nfPlUANErMxBYU6iAlySnQzkHYM5ghFjPcrVFf8jftPWfeWtEskWR93GrZza8w3KemdjeLmT5skhDhUMyxzuZvztsdqkTEHo5be3DI-v_jiOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ تمرین فیزیوتراپی مفید که به رفع و اصلاح قوز پشتی کمر شما کمک میکنه #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/679311" target="_blank">📅 08:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679309">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
یمن نفت عربستان را زمین زد
کپلر:
🔹
پس از اعلام محاصره باب‌المندب، صادرات نفت عربستان از بیش از ۴ میلیون بشکه در روز به کمتر از یک میلیون بشکه کاهش یافته است.
🔹
بارگیری نفت از ینبع نیز متوقف شده و صادرات به آمریکا برای نخستین‌بار در ۴۰ سال گذشته به صفر رسیده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/679309" target="_blank">📅 07:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679300">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZZbk6kjnZJn8SvTxpceIMH_PIW9LWgcG-TZDTalojZj6sqQa1Qdq2PBhz5KcV0RQjyl6YXacvoMy8RyJJzZuwLR-jt5Lo3C-cxXaYzjbvI29-byF8S7C2YB1AHC3MwBl6JLwSQeOBmDGlEJxVI4kLHmIs7IhY50SfuwU65pWQnbwQOkbYfAJNZ0N4bQv4UnT6J3uQNZsCTvxXtWO6m1vFB8M4yx3vc_m2nlqrRdBFNyIlJ9dAz9FGk9nOkSrKxUHygNHhBXTzYAYhRRYb-UgCy2ejX1AG9MpUW8zL9SR9O_N9CunCbOdltydLmbZZ88chQdrG8M2cmJyuGk43DA7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۱۷ مرداد ماه
۲۴ صفر ‌۱۴۴۸
۸ آگوست ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/679300" target="_blank">📅 07:28 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
