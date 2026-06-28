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
<img src="https://cdn4.telesco.pe/file/VnP8xr8Ny-QGA0GhN77_Sw9J7tY65fzCyMcbaReYguqvlv6v2eS0cpF8UU-zcm-Uvv1D4OjsTZy5ZQ0ZqwQgK1VhcRHhoayr045z7oEMSPdjZFieyZCoKUswco_2W7C4CT958u5h-ZqRkiCvAirHEVNNcLDmQMGJIgVgZmCaRcvuMTdruilEarUF6IYGL4aftOlBIgrlBg3kn8CHOjLLl1fDSmGUejK0i1o1bMGRkm3-itWurDYEBDS1ebRf2d_7Nhaz77w21kpQFDERAwwws50qWKM-wLI8yJjIVG6Or5fpKPVOu9dS4Wog0_PJ8P6mjGEKW2txnuYAfP8TSpkIvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 932K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 21:36:53</div>
<hr>

<div class="tg-post" id="msg-130739">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qo7hEY4SmAP2ZFFFSs1367L-qLPYW1eiNBROJFBpvhRrehOjIasSMvGI1V21AFwpCZMKRyp3KFk37reAcdvKdct40oCY6ARShZZwMhXVhxymo13u5JoFaR0KaKIZyWhyBervPI25fwF0ET4-YalTc8lTibTKIxrhJNu-Detb5rvZZGX1F5k_pHa64nztf6Ip3RhJBjqUlGMNUP1mXFz-s5o7_QGF0KUdgYbYSwcgBdnVUYl7czaQdYJxinUHJVWUzmQ_jMZTO7qZzCk79TgUIzqeCIgrlD04X4M-jeGthEhu6i40bVBwGym92omofDwB6tj68pUu3lhuadeBM6cVWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس :
آتش‌بس بین ایران و آمریکا می‌تواند نابود شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/130739" target="_blank">📅 21:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130738">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908ea40def.mp4?token=fdbZZuZJoxc9I2uvMfxAbUFbOG7rD20Hi-YvcBUPhn80lGSGU_Rle7SfayCtryuTDjduzEaiPDk9-Pw591p_PVRVVMhEbpZH0-c7GFrVp_-WcCetb6DTAjswxKMNjbyCAZYy4q1os-ACQFkklw3OeQd-qaX3wh8iVPmlfoPbDNo5qXdH-AR0zWLbJNKgGDoT8i1PaZeSXITYdzhgqkEfKpG4c4zbNyTzNSl10b9Us07q5St9YdHb32eJgDyGCjWuiMAFau56KxxE3sqfTDcUCMeRHPvYGHMpTpdJH5mnnVfhhGYknzPygVosWfrq2jECtJaPi1YM2ncNTyO1mDaNsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908ea40def.mp4?token=fdbZZuZJoxc9I2uvMfxAbUFbOG7rD20Hi-YvcBUPhn80lGSGU_Rle7SfayCtryuTDjduzEaiPDk9-Pw591p_PVRVVMhEbpZH0-c7GFrVp_-WcCetb6DTAjswxKMNjbyCAZYy4q1os-ACQFkklw3OeQd-qaX3wh8iVPmlfoPbDNo5qXdH-AR0zWLbJNKgGDoT8i1PaZeSXITYdzhgqkEfKpG4c4zbNyTzNSl10b9Us07q5St9YdHb32eJgDyGCjWuiMAFau56KxxE3sqfTDcUCMeRHPvYGHMpTpdJH5mnnVfhhGYknzPygVosWfrq2jECtJaPi1YM2ncNTyO1mDaNsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
میساکی باز هم توهین کرد: کسایی که برای خوشحالی گل شجاع کلیپ می‌سازن همون جای خالین
@AloSport</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/130738" target="_blank">📅 21:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130737">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">حذف شدن تو یه مسابقه میتونه طبیعی باشه اما زجرکش شدن قبل حذف یعنی اینبار اسلحه دست خدا بوده
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/130737" target="_blank">📅 21:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130736">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
دنیس راس فرستاده ویژه آمریکا برای خاورمیانه در دولت‌های جورج بوش پدر و بیل کلینتون: ایران در تلاش است «مدیریت» تنگه را به اجرا بگذارد. تنها دستاورد ملموس تفاهم‌نامه، بازگشایی تنگه بود که در ازای آن ما محاصره را لغو کردیم و به ایران اجازه دادیم نفتش را به دلار بفروشد.
🔴
می‌توانیم به تبادل نظامی ضربه در برابر ضربه ادامه دهیم یا محاصره را دوباره برقرار کنیم. گزینه دوم را انتخاب کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/130736" target="_blank">📅 21:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130735">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
منابع دیپلماتیک به روزنامه الجدید لبنان گفتند ایران چارچوب توافق اسرائیل و لبنان را به رسمیت نمی‌شناسد و می‌خواهد اسرائیل را مجبور به عقب‌نشینی کامل کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/130735" target="_blank">📅 21:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130734">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: دولت لبنان از واشنگتن خواست که پیوست امنیتی مخفی را در چارچوب توافق با «اسرائیل» منتشر نکند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/130734" target="_blank">📅 21:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130733">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1janjqzfmAn0ahy2cO31dLXUd6EH0YfTmNhUVgECiyeD0MXWU-bcQ2o4rDsqplfR_hrEVmnLndqSVaG7cCe7qfJ8K9bNbi5maalGz6Vc-ZKznX7WjpLY9WAeINYwT8umb3bJA0rM2N1wcy-T3eVfoN-Kpp_xIVpn11vj9wCx_PMCrSAbe_j1gyMnJScKYhfHiLa9tATy1d9zTzqRriM9kmkQoTsbGhx4tjIKv-6VNZSF52vCu9vU55GA3-zsPm5SoFPJrhjb_hY6s-XfvK0625uIMgro9qpqQ9Uv8Enr-43F9eBV0Ob2JElh5YiU-OEzwXhIt2K-_vBlOrkwx6C8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت کشور قطر اعلام کرد تیم‌های جستجوی دریایی پس از عدم بازگشت یک کشتی در زمان مقرر در این آخر هفته، آن را پیدا کردند و تأیید کردند که یک شهروند قطری پس از اصابت ترکش از «عملیات نظامی» در منطقه کشته شده است
🔴
یک ساکن عرب که در کشتی بود زخمی شده و در وضعیت پایدار به بیمارستان منتقل شده است
🔴
مقامات تحقیقات در مورد این حادثه را آغاز کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/130733" target="_blank">📅 21:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130732">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ایران هر شب حداقل شش پهپاد به سمت کشتی‌های تجاری در تنگه هرمز پرتاب می‌کند که برخی از این پهپادها توسط ارتش آمریکا رهگیری شده‌اند، طبق گزارش i24NEWS.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/130732" target="_blank">📅 21:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130731">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
بلومبرگ: تلاش دولت ترامپ برای لغو دهه‌ها تحریم، به‌عنوان بخشی از توافق برای پایان دادن به جنگ با ایران، شرایط سردرگم‌کننده‌ای برای دولت‌ها، بانک‌ها و سایر شرکت‌ها ایجاد کرده است، زیرا آنها با ترکیبی در حال تغییر از مجوزهای جدید و محدودیت‌های قدیمی دست و پنجه نرم می‌کنند.
🔴
پس از انقلاب ۱۳۵۷، ایران به دلیل برنامه هسته‌ای و حمایت از متحدان منطقه‌ای، به یکی از تحریم‌شده‌ترین کشورهای جهان تبدیل شد. اما کاخ سفید اکنون در حال طراحی یک تغییر موضع شگفت‌انگیز، به‌عنوان بخشی از توافقی گسترده‌تر برای باز کردن تنگه هرمز، کاهش قیمت‌های جهانی انرژی و پایان دادن به جنگ نامحبوب خود است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/130731" target="_blank">📅 20:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130730">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
خبرگزاری فارس: ایران در دوران گذار به نظم جدید جهانی، چاره‌ای جز ساخت بمب اتم نداره تا گزینه نظامی علیه کشور از روی میز برداشته بشه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/130730" target="_blank">📅 20:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130729">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdad75e45.mp4?token=QY6GFZGrrtYne78x-GTwbw070ar899iE80mV4yeZd48gtz9oFSIEd7ZDAhozIrnPmSgdK6I9-K42RPvJ5h61venqsTUpmWh6zDF2Sq0Ty7x1m9OXd4u2MYBjBiF8qMyoTBDZAeu5W4gnfK9bGYX1iCacQh9SOR90rP8YrtagN54XQxpWlft-jJukv40WOUcFtJpL0WlEATUf81uAfl5zRBQf7nojYseRuxoplZiyonNokRdVS3P2lNYuYfRcBeKsSZh6QxzeUTgpal5Kbtvm5ADjUuUSySwkFHSiQioTBvFw9wfyNsYzUIYbeh-WkpzxWwHOVp80M6q56jRP-xK3GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdad75e45.mp4?token=QY6GFZGrrtYne78x-GTwbw070ar899iE80mV4yeZd48gtz9oFSIEd7ZDAhozIrnPmSgdK6I9-K42RPvJ5h61venqsTUpmWh6zDF2Sq0Ty7x1m9OXd4u2MYBjBiF8qMyoTBDZAeu5W4gnfK9bGYX1iCacQh9SOR90rP8YrtagN54XQxpWlft-jJukv40WOUcFtJpL0WlEATUf81uAfl5zRBQf7nojYseRuxoplZiyonNokRdVS3P2lNYuYfRcBeKsSZh6QxzeUTgpal5Kbtvm5ADjUuUSySwkFHSiQioTBvFw9wfyNsYzUIYbeh-WkpzxWwHOVp80M6q56jRP-xK3GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی گسترده هتل «پلازا» در اربیل عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/130729" target="_blank">📅 20:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130728">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
وزارت امور خارجه انگلیس با موضع گیری در خصوص حملات اخیر به بحرین و کویت، خواستار اجرای تفاهمنامه ایران و آمریکا شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/130728" target="_blank">📅 20:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130727">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فوری/ سفیر آمریکا در سازمان ملل:
صبر ترامپ درحال تمام شدن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130727" target="_blank">📅 20:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130726">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
گزارش ها از وقوع درگیری میان ارتش اسرائیل و ساکنان منطقه حوض یرموک در استان درعا سوریه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/130726" target="_blank">📅 20:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130725">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
حمله پهپادی اسرائیل به جنوب لبنان
🔴
منابع خبری از حمله یک پهپاد متعلق به ارتش اسرائیل به اطراف شهرک فرون در شهر بنت‌جبیل در جنوب لبنان خبر دادند.
🔴
جزئیات بیشتری درباره خسارات یا تلفات احتمالی منتشر نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/130725" target="_blank">📅 20:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130724">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
اکسیوس: در جریان مذاکرات هفته گذشته در سوئیس، هیئت آمریکایی به ریاست ونس با ایران توافق کرد یک «خط اضطراری» میان آمریکا و ایران، برای هماهنگی ترافیک در تنگه برقرار شود.
🔴
تا روز شنبه، این «خط اضطراری» هنوز راه‌اندازی نشده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/130724" target="_blank">📅 20:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130723">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
پوتین: روسیه شروع به استفاده از ذخایر سوخت کرده است، اما ذخایر بنزین در سطح سال گذشته باقی مانده‌اند.
🔴
ستاد دولت درباره وضعیت سوخت به‌صورت شبانه‌روزی کار می‌کند
🔴
در پمپ‌بنزین‌ها صف وجود دارد و انواع لازم بنزین همیشه در دسترس نیست
🔴
لازم است پیامدهای حملات کی‌یف به حداقل برسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/130723" target="_blank">📅 20:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130722">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqkGNJL9jdcRYtQss50PXoTA1vn3CGmXg-J5q8wLD1KmAXfgHERdDpLiY7d2SMx_Bvm8mP_9K-Uhpzzedc3pAQDEQ4Mlqvmee87pcuuKE_HPt5oyEXaCgXc1L9qKIpQ6Ir2LVdq9wPuxejL5DiKSq95_LbQDJRXJIsGJWDQMDmplWi7c-Qqh_AbUF_9skIyCLRB0E-lRST9p1JhLL1vk9ibXXEztZ-AEAQVcuB3-8B9Mx_xv6aoewLhDb5N9mbDW0PUR049LixFyIw0YHzAy8eoeVROH9WWPUyChpFsj0665uQaUQldPFGiwSbSlkHB3OewfxCENbuh4wHvR1jkqJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال اعلام کرد مذاکرات هفته جاری در سوئیس به علت درگیری‌های جدید لغو شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130722" target="_blank">📅 20:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130721">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
بلوبانک مجدد قطع شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/130721" target="_blank">📅 20:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130720">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
۸ فروند هواپیمای سوخترسان آمریکایی هم‌اکنون بر فراز خلیج فارس و تنگه هرمز در حال پرواز هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/130720" target="_blank">📅 20:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130719">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d5aba3744.mp4?token=b4HqJzqigmsiwz2HMbBCQ6T2JJaMyI550sPsl3ZuuPNDgd8F8zcD-taF6yxqcwYOqaik2bBnKk_-ZJm1tJ_aLYxB0ENA_2179AQ9e9IxpOl96iMOXuy9e3J74HVkBhrW07WXKAzx4XFbu-EP4h_aKqxBWBts46z7SHzytsADc_ObmlPoK8l9sJeToefuSAe3-6EL1Qe9uuDEoaGAYhGLqvfN1-EHDVO_PNf2lql2rjEVVWHB6-UbPNY0GTvKXGHbODhbh-I4Td8Pemp55KbrhKiJ3HnbtYKicUQHbCY8VMo5gDIsvkQ1CsQxyCWZ7Uh-PD3DNvpZfpADsxj-6fKjRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d5aba3744.mp4?token=b4HqJzqigmsiwz2HMbBCQ6T2JJaMyI550sPsl3ZuuPNDgd8F8zcD-taF6yxqcwYOqaik2bBnKk_-ZJm1tJ_aLYxB0ENA_2179AQ9e9IxpOl96iMOXuy9e3J74HVkBhrW07WXKAzx4XFbu-EP4h_aKqxBWBts46z7SHzytsADc_ObmlPoK8l9sJeToefuSAe3-6EL1Qe9uuDEoaGAYhGLqvfN1-EHDVO_PNf2lql2rjEVVWHB6-UbPNY0GTvKXGHbODhbh-I4Td8Pemp55KbrhKiJ3HnbtYKicUQHbCY8VMo5gDIsvkQ1CsQxyCWZ7Uh-PD3DNvpZfpADsxj-6fKjRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرمربی کره استعفا داد
ساعاتی بعد از حذف تیم ملی کره جنوبی از جام جهانی، هونگ میونگ-بو، سرمربی تیم ملی، با برگزاری نشستی خبری ضمن عذرخواهی از مردم کره، از سمت خود کناره گیری کرد.
@AloSport</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/130719" target="_blank">📅 20:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130718">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/130718" target="_blank">📅 20:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130717">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
وال‌استریت ژورنال به نقل از منابع:
گفتگوهای برنامه‌ریزی‌شده ایران و آمریکا در این هفته، تعلیق شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130717" target="_blank">📅 19:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130716">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADY-o78D0bwJR6gU6c9RDauw-gCJR16g5OdFeG6B9lMz3EN_CCNzRcuTnfBT8IoRZRfO2Sl5vpj4oI5qf5MBB1fNwizaIpYJndpLiy8RbEfP9XrSEprtXmGPnQd9l-noHGy07gVGaaNqDY4muaoBUMTwvhbmGN_lCzqR2efqM2AJgCXykyCSZPZWYpMvrlAxjEQqs5C0RxyDafOIqGz56oScC3AHWd_IsFH3frdRmW8GwifcmeRQcR2kpFYmBIc9dGcLPK6wrSdxuQ8vE7m7LR2hSfXoMIJMoIdZQuXBGzjWEgiRfgZJnHCS2XuoIwGNJyhOd1r4JLhwrVlyPG1gAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو:
هنوز بقایایی از محور ایرانی وجود دارد که باید با آن‌ها برخورد شود، چالش‌های امنیتی سنگینی وجود دارد و همچنین فرصت‌های تاریخی برای صلح در منطقه — در لبنان و جاهای دیگر — وجود دارد.
برای شکست تهدیدها و بهره‌برداری از فرصت‌ها، ابتدا باید در درون خودمان صلح برقرار کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/130716" target="_blank">📅 19:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130715">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntcMLFStfQSqDlv1XNfHOdK8HQXGaMx0gNHNx6N6NyiATyify3r8_QUZLIqM05dR23hiLcKtkoi4saQJ5chbH1GXrhH9knBdGd9aQWQi5qQkxRBahu02KULW60Ia5b_uDB4ntgHI8izfBaYz1LZ8Eok_z-EbEwjjMlUkeZ33331uOXAn4_eKGXRxMsgbcRngI-v_h05SMBoAtaNd5E2lCcDYg5xWvtwXMR_QzljdsEWgIpRezVlSxhlxvGM27PDb5ZAaM8LiTuRqdFyF68w_UGRCVCCgRH81uN8tZhXLVG3L1pkLGdGwm1VzpvKj3-La7kVwZPKcaa3M0kChoCBC9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو:
اسرائیل به یک دولت ملی گسترده نیاز دارد — و این دولتی است که من تشکیل خواهم داد.
در این زمان، پس از سال‌ها آزمایش‌های سخت، مواجهه با دشمنان از خارج و چالش‌های بزرگ داخلی، دولت اسرائیل به دولتی نیاز دارد که اکثریت مردم را حول یک مسیر واضح، مسئولانه و ملی متحد کند.
قصد من تشکیل یک دولت ملی گسترده است، دولتی که بر اساس گسترده‌ترین اجماع ممکن در مسائل مرکزی که آینده ما را برای نسل‌ها تعیین خواهد کرد، تکیه خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130715" target="_blank">📅 19:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130714">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
نتانیاهو:
ما اظهارات ترکیه را نادیده نخواهیم گرفت و آنها را به اطلاع دوستان آمریکایی خود خواهیم رساند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/130714" target="_blank">📅 19:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130713">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
آغاز پروازهای تهران-دبی-تهران از فردا
🔴
مدیرعامل شرکت شهر فرودگاهی امام خمینی از فعال شدن مجدد مسیر هوایی تهران-دبی-تهران و انجام پروازها در این مسیر از فردا (دوشنبه) خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130713" target="_blank">📅 19:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130712">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9z50wv0Ok9IDca0vbja5udnxGaVhaV-HR4KnxVTL4jTudYclDs8jbwsY9HsH8-clyYI38VDnVHSQ8v7xcf7MFJJGr8sKpyAtftzoZbUs3_wOccm0XPlkTMbotn0855B2ve_UJB4BOC8GKvLpb8dhNzd42dNmWb4diIFlYDRzpLyM-VgitDxyftG7MUtLykfNsQNZs9Pd8Tc8bw3aXg7D70U9AjPyagmMrFWidGJNxctWM8rrNMH6gNLSEnJaEXUHezI_CKlXGOi3KxZcxFHwKU6XBNEKJ-awxTAJG0JJe7UyUhP70vw4Vj9CAea4Ffb7Q2XOE52Kr4m4Kwrsm42Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از لاشه یک فروند لانچر منهدم شده دو فروندی کروز ( طلائیه ) سپاه توسط آمریکا.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/130712" target="_blank">📅 19:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130711">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/884efd1550.mp4?token=K7oF19vNPonyVE20qPh_8YOUTH5SO3ZswmS-2nsSJWSn5tdrdb_IcjhJhy86gi6WZfjgtinLCTYs9LYGaZg9Pl6l6m6UfcZxkg_JkRfQOWOH0_4ARfYWf394ihXgWgwelqPt8CCV3lYmaYk4LNDnGzc1Jkl-rJmh87kCQbuT1B6cTYtKj4ZdvzOsvlG0suSXDSDkiwWvm_yS9TxFRgXzA5MyncM729Q470k3QJcgqM8dZg8uJygsFeS2cqVAsgyI-LBmZ_s1JqRN_7Wq5yRczeNZHAT_4QnM32HCievburAo7LGjlc02kxcR7Dg7F3662lj-BMlfrp4XVAypgigXAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/884efd1550.mp4?token=K7oF19vNPonyVE20qPh_8YOUTH5SO3ZswmS-2nsSJWSn5tdrdb_IcjhJhy86gi6WZfjgtinLCTYs9LYGaZg9Pl6l6m6UfcZxkg_JkRfQOWOH0_4ARfYWf394ihXgWgwelqPt8CCV3lYmaYk4LNDnGzc1Jkl-rJmh87kCQbuT1B6cTYtKj4ZdvzOsvlG0suSXDSDkiwWvm_yS9TxFRgXzA5MyncM729Q470k3QJcgqM8dZg8uJygsFeS2cqVAsgyI-LBmZ_s1JqRN_7Wq5yRczeNZHAT_4QnM32HCievburAo7LGjlc02kxcR7Dg7F3662lj-BMlfrp4XVAypgigXAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام فیلمی از یک جنگنده F/A-18E سوپر هورنت نیروی دریایی آمریکا در خدمت اسکادران جنگنده ضربتی ۱۳۱ را منتشر کرده است که از ناو هواپیمابر کلاس نیمیتز USS Abraham Lincoln در دریای عرب برای انجام پرواز برخاسته و همچنین یک F/A-18 سوپر هورنت که روی همان ناو فرود می‌آید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/alonews/130711" target="_blank">📅 18:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130710">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87a537482.mp4?token=pPKol_qlNxDF_fbh9HV4UcSmuRa-xnMjo_9sT4NHUrJiB8lCmW3tPQX8uPCAnRP5ljLyyVBJTB-COCvX7oJpEMDXQD3vldHW7SKNIfbOuYb_z709HQPCTQIJ2sWNmeg9r17wQqL6xDCDYQriC2NbBBUtZcseo144YG3o8TroqNkgVlQZiJzq0YqhKsQiLbqPQbwRKrv6UYy6RWmdX10AQ4-8QMCofibjXR9humuq_EPBwOMI7AN9T6rfdCHslhkwB6uSt3ftdIBghGk57tuvk-lx1FtCRORAU-dqACVbx8mlogoLwNYkwM4v6Wz-MNj1ZLml0xxiNj4k757tc8mK-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87a537482.mp4?token=pPKol_qlNxDF_fbh9HV4UcSmuRa-xnMjo_9sT4NHUrJiB8lCmW3tPQX8uPCAnRP5ljLyyVBJTB-COCvX7oJpEMDXQD3vldHW7SKNIfbOuYb_z709HQPCTQIJ2sWNmeg9r17wQqL6xDCDYQriC2NbBBUtZcseo144YG3o8TroqNkgVlQZiJzq0YqhKsQiLbqPQbwRKrv6UYy6RWmdX10AQ4-8QMCofibjXR9humuq_EPBwOMI7AN9T6rfdCHslhkwB6uSt3ftdIBghGk57tuvk-lx1FtCRORAU-dqACVbx8mlogoLwNYkwM4v6Wz-MNj1ZLml0xxiNj4k757tc8mK-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Newcastel core...
@AloSport</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/130710" target="_blank">📅 18:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130709">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل:
در توافقنامه هیچ جدول زمانی برای خروج وجود ندارد و هیچ چیزی اسرائیل را به آن ملزم نمی‌کند.
🔴
در واقع این یک توافقنامه بسیار خوب است، اما حزب‌الله از این بابت عصبانی شده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/130709" target="_blank">📅 17:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130708">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5affae2222.mp4?token=PUU7o3zfPR_UnDCoieO3M_qtNZsrGnAF3uE-Vv-DoLAAsThd70UzRMKE6BPX-9Mzv23_dZxY9sQFP9NkFeMob5-WsXy1GMa1l7uZ4rRC3-bgXSvsNMCNL8mKmiDhXVlT0H5VGQO-UW5NKjZwdpHqpVkq8FKStvkf3UCEDSsfVfE03hhY9nsCfQ0iRyqwlAr4HSGI6LrNpamHROHkbLi_zA5xSIY4joMzn3lzEwCSjxGl6wKTEYIw20-uBePTRlOtsTnuJBz8aftC8gH6c6buhXtbrExHylyRWvtdF_PplKtjeGC5_t4XF4FyjXMSZw2l8dhtvUt2VEfCCk476OkcQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5affae2222.mp4?token=PUU7o3zfPR_UnDCoieO3M_qtNZsrGnAF3uE-Vv-DoLAAsThd70UzRMKE6BPX-9Mzv23_dZxY9sQFP9NkFeMob5-WsXy1GMa1l7uZ4rRC3-bgXSvsNMCNL8mKmiDhXVlT0H5VGQO-UW5NKjZwdpHqpVkq8FKStvkf3UCEDSsfVfE03hhY9nsCfQ0iRyqwlAr4HSGI6LrNpamHROHkbLi_zA5xSIY4joMzn3lzEwCSjxGl6wKTEYIw20-uBePTRlOtsTnuJBz8aftC8gH6c6buhXtbrExHylyRWvtdF_PplKtjeGC5_t4XF4FyjXMSZw2l8dhtvUt2VEfCCk476OkcQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوشحالی مردم غزه از ناکامی ایران و صعود مصر به مرحله بعد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/130708" target="_blank">📅 17:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130707">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">پیروزی شیرین ملی‌پوشان والیبال مقابل کوبا
ایران ۳ - ۱ کوبا
🇨🇺
۲۲| ۲۱| ۲۵|۲۸
🇮🇷
۲۵|۲۵|۲۰|۳۰
@AloSport</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/130707" target="_blank">📅 17:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130706">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
دادستان مازندران: بی حجابی در سطح استان به بیشترین حد خودش رسیده و دخترا عریان میان بیرون!
🔴
از مسئولین مربوطه درخواست دارم اشد مجازات رو برای دخترانی که خلاف موازین اسلامی رفتار میکنن در نظر بگیرن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/130706" target="_blank">📅 17:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130705">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
نماینده آمریکا در سازمان ملل:
تحرکات ما در صورت لزوم ادامه خواهد یافت تا زیرساخت‌های مورد استفاده ایران برای کنترل هرمز را از بین ببریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/130705" target="_blank">📅 17:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130704">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی مجلس:
ممکن است ترامپ به زودی دامنه جنگ را تشدید کند و تفاهم نامه با ایران را پاره کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/130704" target="_blank">📅 17:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130703">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سفیر آمریکا در سازمان ملل: اگر ایران گمان کند ترامپ در برابر حملات به کشتیرانی و پایگاه‌های ما دست روی دست خواهد گذاشت، در اشتباه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/130703" target="_blank">📅 16:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130702">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ET8iOwctgecFkKNEtJxkPriKxCoVsMOkg2UBAAmSWnskjhfdhMD1v4dRTUAZMXQeUfCJ7NMKYLbnNFGaEc6EM1esIXq_tFXEiQNULoWLidt8R2Fk1rhEGrNdZmB7F3mYBRJcD_m-lFvxWRUtHkAPemO65TbqR3q_KGQ51LAh-c-BQ8mpJaxDHpG0DoU-5R3CsdrzWK9Egt95SwN5ZXBsZ7wvEj_1Nxd5svAcW1hH8GG0dA1ByNyibKpqy6Z-uGGPwOL0hrqmMzxk0yQICMAe73MyZvsvCROQuH0_T-N699zcb_SvpisC0j6rUlJuF6ZVSkV0pszGdZeIAvY3zbt4_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خداداد عزیزی:
قلعه نویی با پارتی بازی و رانت سرمربی شد و این نتیجه افتضاح پیش اومده، سرمربی‌های ایران هنیشه با پول خوری و رانت و رابطه انتخاب میشن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/130702" target="_blank">📅 16:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130701">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی مجلس:
ممکن است ترامپ به زودی دامنه جنگ را تشدید کند و تفاهم نامه با ایران را پاره کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/130701" target="_blank">📅 16:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130700">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
زمان شروع امتحانات پایان ترم دانشجویان دانشگاه تهران از روز پنجشنبه ۱۱ تیرماه به روز شنبه، ۲۰ این ماه موکول شد
🔴
پایان امتحانات پایان ترم دانشجویان دانشگاه تهران نیز از روز یکشنبه ۲۹ تیرماه به روز شنبه سوم مردادماه به تعویق افتاد و همچنین روز دوشنبه پنجم مردادماه  پایان امتحانات دروس عمومی می‌باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/130700" target="_blank">📅 16:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130699">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGinTsMuI1-USDZC2sKR9bOK8m7_DTwtmc2uY6SFKucX5u1_rYQtWUq0yKXa_ZoMzqfqrTcgtVEgB7XFEcSOGNrsay8UWG3snUAPjUQTyPBVGxx-VjAWAe5H6Pg-ZalqemFLzIJXuHxBcUh4PKy2okQz-GJxQBSlaIZVOIS5dbmUH4n_i0e404HTUsfnH5l0mDJ8ap3IEXc-fFB6566Jg6nsHdy0s8NfEr6efi3F1QPeGq7GIzfWt0zF0A6fUNI7RdMmc52XUq9mMk4Jy6zEEFWx1KUw9HC4HeZaFv971c_4zIqldCyeNPc7Oe0t8tgra8WzQlr1BRfFhtLTlMfNUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایالات متحده اولین کشوری است که در یک روز هم میزبان تیم جام جهانی فیفا بوده و هم کشور آن تیم را بمباران کرده است.
🔴
ایران دیروز در سیاتل با مصر بازی کرد و بعداً در همان روز، ایالات متحده به جنوب ایران حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/130699" target="_blank">📅 16:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130698">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqC9OGrdCVGKc4Ztht5259zpjbR_FKui4KuLvcacr0eHZWPumsjKUQ_g-pSeWEnIIUJV4gvoViSXseumVC88Mdh-5NPhfY41XM5ZdXruDM7i6G5ZU56e2jdj9Ru_VRY1wkWeaOWHCnLF4ZMNSJCZa3wxi7BdGlEbpkbOiMKHxV_j14ZTuMLEyV-GDxPz5QOSEOKs8EcVtcyxYhG9-USP8Te_ZvBYusY0jY1OUTfK6G8-DqPySBrkTGWPx-LOQPvfR46cqfkD-iW21GS32QUylxtyEdGXlp2lFVZvFou3JHQTbjDkZX7j_qdM_XwWFMJKCcuU0naayKerOyk-0d5jjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: مسی دیدنی است؛ او تنها بازیکنی است که می‌توانی بگویی بهتر از پله است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/130698" target="_blank">📅 16:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130697">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1_7FkYEeDr7YsYJsxB6a8T9Vczn8_XpKALb6qaHAT5eF9yfNrGn5szSXGrFtVZNqPdgEHYfldrk75X5zUVSO4RUGHMU-a6DP2qEe5K1lrUdcQ5WLSG8_S5twwcdc_JBGKKBrR0e47lUzXsRwMSjARNYYyDFlfLtqT8XjlRwhOB4-jWesJVIxVyKLVsZFUy1beyEDbTLv6SAFdwb5sR-DJUXTdwu2aTyFShA_hGGAkFwVwhEnCMISeOi314Df_3106wI-rn7nwGScC90zpJfiJrERT8Sw5sqqVO3PJov_uRlbmupC-Eiyadclb0O55PwNZc8ELeKrn9_XI268ejaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاتز ، وزیر دفاع اسرائیل:  فرماندهان و سربازان ارتش به طور قاطعانه به عملیات در لبنان ادامه خواهند داد تا تهدیدها را از بین ببرند و برای تضمین امنیت ساکنان شمال تلاش کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/130697" target="_blank">📅 16:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130696">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
فایننشال تایمز: میانجی‌ها در حال انجام گفت‌وگو با ایران و آمریکا هستند تا تنش‌ها را کاهش دهند
🔴
فایننشال تایمز به نقل از یک دیپلمات گزارش داد که میانجی‌ها در حال انجام گفت‌وگو با طرف‌های درگیر [ایران و آمریکا] هستند تا تلاش کنند تنش‌ها را کاهش دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/130696" target="_blank">📅 16:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130695">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
وزیر ارتباطات: اظهاراتی که اختلالات در خدمات بانک‌ها را به اتصال اینترنت بین‌الملل مرتبط می‌دانند، غیر حرفه‌ای محسوب می‌شود/ عمده خدمات حوزه بانکی اصلا در خارج از کشور در دسترس نیستند که با باز شدن اینترنت، برای آن‌ها اتفاقی بیفتد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/130695" target="_blank">📅 16:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130694">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e18ef9d64.mp4?token=CoMkG7P93E1dRvrFmQotiZap7hajlCePxqwoOAWXyF8d9e9yhIQJ785yecTn5XYOW0aEo3VrgA-6QfxPSgLTDUXByG_U5h31-eZ_6FWs8HfvGoKfiCF6rS6NCMSPEgJSz_lymNAY5uVSyE889AfYqSGVvIMuiajObFT0vajyLlWxwkBCs78oNDzOr25erGDuzX4jPiGRQCV9T7VJrchSALmFAXh3CRPAB606ryRL6uUFZ1QOXlMcI4LwriQ6ux_afEDF0BrcvQkr0oWdUi03Tfo2PBezlIRzKRneljFUpWabxDkTpVNg4qGJPM4MvwQIReOaYsKEePeuDjuWZa0a3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e18ef9d64.mp4?token=CoMkG7P93E1dRvrFmQotiZap7hajlCePxqwoOAWXyF8d9e9yhIQJ785yecTn5XYOW0aEo3VrgA-6QfxPSgLTDUXByG_U5h31-eZ_6FWs8HfvGoKfiCF6rS6NCMSPEgJSz_lymNAY5uVSyE889AfYqSGVvIMuiajObFT0vajyLlWxwkBCs78oNDzOr25erGDuzX4jPiGRQCV9T7VJrchSALmFAXh3CRPAB606ryRL6uUFZ1QOXlMcI4LwriQ6ux_afEDF0BrcvQkr0oWdUi03Tfo2PBezlIRzKRneljFUpWabxDkTpVNg4qGJPM4MvwQIReOaYsKEePeuDjuWZa0a3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
39 سال پیش در چنین روزی، رژیم بعث عراق با استفاده از انواع سلاح‌های شیمیایی، مناطقی از سردشت در آذربایجان‌غربی را بمباران کرد
🔴
یکی از غم‌بارترین و تاریک‌ترین صفحات تاریخ معاصر در این روز رقم خورد؛ رویدادی که با وجود فریاد مظلومیت مردم این شهر، از سوی جهان شنیده نشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/130694" target="_blank">📅 16:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130693">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
قیمت هر گرم طلای ۱۸ عیار به ۱۷ میلیون و ۷۱ هزار و ۵۰۰ تومان و سکه امامی به ۱۷۲ میلیون و ۵۰۰ هزار تومان رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/130693" target="_blank">📅 15:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130692">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
انفجار بمب‌های عمل‌نکرده در محدوده فرودگاه شیراز از امروز به مدت یک هفته آغاز شد؛ احتمال شنیدن صدای انفجار وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/130692" target="_blank">📅 15:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130691">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
مقامات بهداشتی فرانسه می‌گویند از ۲۴ ژوئن تاکنون حدود ۱۰۰۰ مرگ اضافی در طول موج گرمای بی‌سابقه‌ای که در غرب اروپا رخ داده، ثبت شده است.
🔴
افراد ۶۵ سال به بالا ۸۵٪ از مرگ‌های اضافی را تشکیل می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/130691" target="_blank">📅 15:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130690">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dr47g5U78KCVPSJ8TBFTtb44rLB2_eEXzAzTczvCYKDXyIDw6XQ6JstYbHXlrJZ8vv1_7AVElzRQgdeOBmirj9whwr0Fx94NjVTHUJZCKdQDd1QHkeHyOoOrhj2PCA8zpW5uV7P_DmZCjq7kPQOCq3JSCMzx8TGJJg50mhi7C0Lp6_JNftZpjnAHjDdnr_JWWicIzZWz2pzAJa__4YPti0LTbHkdkciw-qnqHi-EH4CG17TpFfnjwZGqVLSTygDJDAj8VIs18ndkuG9lwdX9yMvMsr7lE3JRTZuimZoGBmMgRXMWcS9a1fq-hN6w--HOehOL-rEngxKbr4ZHsu9P7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تردد خودروهای پلاک مناطق آزاد کیش و قشم در هرمزگان به‌صورت رسمی آغاز شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/130690" target="_blank">📅 15:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130689">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVR1IsNjzF5Qbkm1nlpisoQiznwf4JeRGidARCGeQqDi5bi3H0kp52WwVApqxSdiHprgikF-Sv6VvgbMU3D80QuNuV9JaxemQbVZUyzwOZjTZb32qq0gA5vOyN2QrUFfDZBx_d13irMrUyMzD7labZflVaQxmYdicYF0AKYRYtquJ1USwyjKG5JaJ0YtbuyHyVqkSL2ajeaV2dUnITgH7Y_bWA_l7F5oCjez4AnfHUDev5ly3fC_6cR7gz4tASB8e8g47xcnk_4KxykOrUIUgzNIdq5GhKLy9uTZMhQ7uhFkwuYeOYCnHQc6bjHsqw-NPTHcklq1-Dc5VFmc9MnsKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تو هر کشور چند روز باید کار کنی تا بتونی بازی GTA ۶ رو بخری؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/130689" target="_blank">📅 15:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130688">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
داعش ساحل فیلمی منتشر کرده است که حمله ۱۷ ژوئن به پایگاه نظامی ایناتس در نیجر را نشان می‌دهد و سلاح‌ها، مهمات، خودروها و تجهیزات نظامی منهدم شده به‌دست آمده را به تصویر می‌کشد.
🔴
این ویدئو همچنین پیامی از یک تروریست داعش خطاب به «برادران در زندان‌های شیعه عراق» دارد که از آن‌ها می‌خواهد در برابر آزمایش‌هایشان استوار بمانند، در حالی که یک شورشی دیگر قول می‌دهد کمپین گروه را از ساحل تا بغداد، مکه و قدس ادامه دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/130688" target="_blank">📅 15:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130687">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
گزارش ها سقوط یک بالگرد متعلق به شرکت آرامکوی عربستان سعودی در رأس تنوره و کشته شدن ۱۴ نفر.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/130687" target="_blank">📅 15:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130685">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed75e27c84.mp4?token=UHHaiiadnxYEAE5qGcy2_EhVkA8WTxXKiNMSbjXeBEqwVzDmMe8dhoXsWypGeJqf-KWBkzfUR0_FYNsqelA7vlJBlUewzZIRzlZtzR88BaiiZVSIqugiK_mD0a2UxGwoF009SwEhRaa2VQpJYwwkJLEAfQxI0JzAhfEYFYQ4VZCxVXaIKWS1Q-PmTxT6UThDmh1_AHUIDGEgziVrrUJ9d2ulBjcCvBAYJl5XpkzrhzBK0FZVwnGd0Eu1NjGNDMoz94tnZomnWmlLxMRGZaj6EP_wCKDAcz12E81iwQ_43Mrn18Z90XzUkpYmnGo5rUGizxVkWS5y6KnYd0cxJYFynzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed75e27c84.mp4?token=UHHaiiadnxYEAE5qGcy2_EhVkA8WTxXKiNMSbjXeBEqwVzDmMe8dhoXsWypGeJqf-KWBkzfUR0_FYNsqelA7vlJBlUewzZIRzlZtzR88BaiiZVSIqugiK_mD0a2UxGwoF009SwEhRaa2VQpJYwwkJLEAfQxI0JzAhfEYFYQ4VZCxVXaIKWS1Q-PmTxT6UThDmh1_AHUIDGEgziVrrUJ9d2ulBjcCvBAYJl5XpkzrhzBK0FZVwnGd0Eu1NjGNDMoz94tnZomnWmlLxMRGZaj6EP_wCKDAcz12E81iwQ_43Mrn18Z90XzUkpYmnGo5rUGizxVkWS5y6KnYd0cxJYFynzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای جستجو و نجات ایالات متحده دیروز مادر و نوزاد نه ماهه‌اش را از یک ساختمان فرو ریخته در ونزوئلا نجات دادند.
🔴
هر دو تنها با جراحات جزئی فرار کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/130685" target="_blank">📅 15:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130684">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
یک کارشناس حوزه آب با اشاره به وضعیت منابع آبی کشور اعلام کرد ۹ استان از جمله خراسان‌ها، کرمان، یزد، اصفهان و سیستان‌وبلوچستان در آستانه تنش شدید آبی قرار دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/130684" target="_blank">📅 15:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130683">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6IRqrQmyD5Exq8Pe2F8E5Sn82rSXkc0JwHAse21745YrkoefE7qGheihmWcoUzRrZvJ-sK2MjcTzShSoIZhA5AaYm6hzQxcRw6pnhzahYYMQhKlLNY96agBjpjCTUl627k2yGotMj5WbDe0UXXo3hoCG4MIO3sbgoapo0HvQf6vembbMhBso8xp8Wzt77XrYAKLtgLt9MJzAmsgD_QJHvQvUNEVVJBMDUTZAsT6_qxo7QrxRqwx6svKtFJC3FvjkF7NW9miyAARY2nz72B9lg9zxbSXXANEQNIiJvhzrvFFLG7Ug4Prrzlef29JO2ph_k4CxAgRMeVt3JB02KN3ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواداران حزب‌الله دیشب تابلوهای «لبنان اول» را در جاده منتهی به فرودگاه بیروت به آتش کشیدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/130683" target="_blank">📅 15:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130682">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
الجزیره به نقل از صدا سیما: امن‌ترین گذرگاه برای کشتی‌هایی که وارد خلیج فارس می‌شوند، جنوب جزیره هرمز و برای کشتی‌هایی که از آن خارج می‌شوند، جنوب جزیره لارک است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/130682" target="_blank">📅 15:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130681">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
شرافت یعنی آقای مرزبان
🔴
خدای ما مردم با خدای طرفداران جمهوری اسلامی فرق داره</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/130681" target="_blank">📅 14:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130680">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
واکنش سخنگوی قوه قضائیه به تهدید رئیس‌جمهور توسط یک مداح: این یک اقدام مجرمانه بوده و قابلیت پیگیری دارد
🔴
دستگاه قضا‌ حتماً به وظیفه قانونی خود عمل خواهد کرد
🔴
شرایط وحدت را حفظ کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130680" target="_blank">📅 14:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130679">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وزارت خارجه قطر: باید از پیامدهای حملات غیرموجه برای منطقه جلوگیری شود و مسیر گفت‌وگو، دیپلماسی و کاهش تنش ادامه یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130679" target="_blank">📅 14:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130678">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
گزارش صداوسیما از جزئیات حملات نظامی بامداد امروز آمریکا به قشم و سیریک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/130678" target="_blank">📅 14:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130677">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3GqtWN8sQnf-prSQrSfnDrLHBDvs9000jBXx8_mLH-Ow6bmZ6kO9Jo_CbkBw2ak5GOzD7Lt5n2LDFmYdieAqj7eg1rqbyOnE7u99JUFpaSmcfzhW3wKo9BxrZMitXa6O0S1aTrxdo5VxAbL7jzvr-0LolHzu8wmARw9bFKOOJLLzVOjp7MFIzwOwKoYBU4F2QPTvgNHWL4VGHYTidha6u5MsPMcsYALvX1CRGQDkSjnGWN_WvmEr-lmPjPh5LVCMz90IGZu6MQWrCh4lh_sj27tPxG4sXJgczRXUf2nNPgPNEo43LgJc9GH60dbExbluJszDhVTVQ4AzgPOfq_GxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی با نخست وزیر عراق دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130677" target="_blank">📅 14:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130676">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
قالیباف و نبیه بری تلفنی گفت‌وگو کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/130676" target="_blank">📅 14:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130675">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
ذرت هم به جملات سیاسی برای جمهوری اسلامی تبدیل شده و حبس داره</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130675" target="_blank">📅 14:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130674">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/c69d8e0a97.webm?token=OuSdwf_Xu4MfDBao87oO6gzqkX1wr2AY5DiJ4bddFZsY99b4wPrs5DZr_gII3SVc8MrFArMDeBt69a0_cjArW8H7yaIzkBhJvcSWGwYzmOmcbxxAus4LKaaS1yYJwDsAyH_tDdj7nsKLpxz3Bpw5HLss0pjzPynETBDnEOIyXezNnjWLYmLumQzW9NXeLpsds8AaRAhPZL37idwEzJvmQOin0oUTEijxRI2_hmQtzJtWxKwvweUS50HLLbbwMjgT6ERRVKWcnp_01V1NFK8EbcY9huI0y25kbCjvDsIx7xDLN-3dIz4YYItJ7I1vy8r2126zmevMbvTWIP1oAppvOA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/c69d8e0a97.webm?token=OuSdwf_Xu4MfDBao87oO6gzqkX1wr2AY5DiJ4bddFZsY99b4wPrs5DZr_gII3SVc8MrFArMDeBt69a0_cjArW8H7yaIzkBhJvcSWGwYzmOmcbxxAus4LKaaS1yYJwDsAyH_tDdj7nsKLpxz3Bpw5HLss0pjzPynETBDnEOIyXezNnjWLYmLumQzW9NXeLpsds8AaRAhPZL37idwEzJvmQOin0oUTEijxRI2_hmQtzJtWxKwvweUS50HLLbbwMjgT6ERRVKWcnp_01V1NFK8EbcY9huI0y25kbCjvDsIx7xDLN-3dIz4YYItJ7I1vy8r2126zmevMbvTWIP1oAppvOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130674" target="_blank">📅 14:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130673">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af98f99e9.mp4?token=CnagZK6BZjuX8hoBeuJro99UXEaQD1OjTjYz3_jhPUhsEgd-_GfZoXZIgt46XVrgWlMAyLwKyHnirGCO34-pYQ3v0_UyAERXC0KTAJBgyFGR6GpZWbgbQByAS0gpmgQCg5m1f7CUWyU46dc-hm4iwjn4yOFSXVRXLrVssR1HxAU3Lrvl4x5kwqI-Jr5oK9wTDCumjbZZr1j9oWvPXbvJjFcopeVFok_VAwaWbAYyobaevaqnZR2Ghj7QavrZLLA1zDBa4VX5RKpxsKZV_xMqdy2TXZVo5EFGZ_DWGxYn9LT407tarw-OAbrQK-gisHgv2AORYjFhJE0RzLgC-fwW1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af98f99e9.mp4?token=CnagZK6BZjuX8hoBeuJro99UXEaQD1OjTjYz3_jhPUhsEgd-_GfZoXZIgt46XVrgWlMAyLwKyHnirGCO34-pYQ3v0_UyAERXC0KTAJBgyFGR6GpZWbgbQByAS0gpmgQCg5m1f7CUWyU46dc-hm4iwjn4yOFSXVRXLrVssR1HxAU3Lrvl4x5kwqI-Jr5oK9wTDCumjbZZr1j9oWvPXbvJjFcopeVFok_VAwaWbAYyobaevaqnZR2Ghj7QavrZLLA1zDBa4VX5RKpxsKZV_xMqdy2TXZVo5EFGZ_DWGxYn9LT407tarw-OAbrQK-gisHgv2AORYjFhJE0RzLgC-fwW1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روزنامه‌نگار لبنانی
:
لبنان را دوباره بزرگ کنیم!
🔴
ترامپ
:
بله، من این کار را خواهم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/130673" target="_blank">📅 14:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130672">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
جماعت الاحرار، گروهی جداشده از تحریک طالبان، مسئولیت حمله به یک مرکز نظامی پاکستانی در کراچی را که دیروز رخ داد و منجر به کشته شدن چهار سرباز و زخمی شدن چندین نفر دیگر شد، بر عهده گرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/130672" target="_blank">📅 14:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130671">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
دو کشته و بیش از ۱۰ زخمی در حمله هوایی نیروهای دفاعی اسرائیل در شرق بیت لحیا، شمال نوار غزه. انتظار می‌رود تعداد کشته‌ها افزایش یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/130671" target="_blank">📅 14:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130670">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
آیت الله مجتبی خامنه‌ای : قوه قضائیه باید تحول قضایی، مبارزه با فساد و اجرای عدالت را به‌صورت عملی محقق کند و جنایات و خسارات جنگ‌های ۱۴۰۴ و ۱۴۰۵ را در محاکم داخلی و بین‌المللی تا مجازات عاملان پیگیری کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/130670" target="_blank">📅 14:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130669">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
قیمت دلار آزاد امروز به ۱۷۱,۱۱۰ تومان رسید...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/130669" target="_blank">📅 14:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130668">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdDyO55fiYojCVWWaFRCblX1VLQqWQkOI7OvkgAhYz9VCoPXvPQVB_XmqFq0EgLbkipEMQlwJOh_pocfE_h0XuLf0mdQ03hzo3Obl8mR4KeZqGBZ4hzJnPxXL865ma3yHp4ZMHh0xkjXyA-YdvprHJSP0v35qoiGKaOpd_E2_XBrOS8qpOxeyRp6w2ST8qMiP9nNYDxdI_zmziAep18Nn9LJ_tOIp_29K60BYrPLD8tIy0KZ8nDCc96ChixgcodveoqgbLg6sraKZhXnf-pPJzSyWGHzxK-ynxQR0mmSvEzDGDL2fEEqd4aQ0Gmxl9ryb-Dfvvh9MKYZJpCUIymesw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسراییل به فارسی : دولت اسرائیل امروز به اتفاق آرا پیشنهاد گیدئون ساعر، وزیر امور خارجه، مبنی بر به رسمیت شناختن نسل‌کشی ارامنه توسط امپراتوری عثمانی را تصویب کرد.
🔴
وزیر امور خارجه ساعر اظهار داشت: «هیچ وقت برای انجام کار درست دیر نیست.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/130668" target="_blank">📅 14:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130667">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❤️
اونقدری که رضا پهلوی به جمهوری اسلامی و طرفدارهاش فشار آورده آمریکا تو جنگ مستقیم نیاورده.</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130667" target="_blank">📅 14:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130666">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
قیمت هر گرم طلای ۱۸ عیار از ۱۷ میلیون تومان عبور کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/130666" target="_blank">📅 14:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130665">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9accf16ca1.mp4?token=VsLO3kJAqakMvWqB37YSnKOsWWqfwpNKMcfN6JPyAsMKBJrcg3sM3LbRDrUSfMgygvCbFB9qIpCpnCws0kDu00rkLwb6p6jORfQ5AEuzR4YKiZobuo-7KEXEJhPGEOA1mHg9ovgB5nw3V0-uePOaNHH3Dm-t4G2qaA3lBE8tuWTGt2wKNzcJUt_vlDf_QeuVneXIsdFIFgAEy_Nw2NsVqQ8I40x8uhHyyICuc47j4dYp7CghTkRR2DQ_AN64DXaS4oi7tbAK91zotMRS27Ucj4FLZEtd7Jq30cAXxlNajsK71z-ksBZxRz6EiKBnj0k_KE4s4GD21wG1OSYTnjKJEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9accf16ca1.mp4?token=VsLO3kJAqakMvWqB37YSnKOsWWqfwpNKMcfN6JPyAsMKBJrcg3sM3LbRDrUSfMgygvCbFB9qIpCpnCws0kDu00rkLwb6p6jORfQ5AEuzR4YKiZobuo-7KEXEJhPGEOA1mHg9ovgB5nw3V0-uePOaNHH3Dm-t4G2qaA3lBE8tuWTGt2wKNzcJUt_vlDf_QeuVneXIsdFIFgAEy_Nw2NsVqQ8I40x8uhHyyICuc47j4dYp7CghTkRR2DQ_AN64DXaS4oi7tbAK91zotMRS27Ucj4FLZEtd7Jq30cAXxlNajsK71z-ksBZxRz6EiKBnj0k_KE4s4GD21wG1OSYTnjKJEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ژاپن پس از زلزله ۶.۱ ریشتری که جزیره هونشو را لرزاند
🔴
گزارش‌های قبلی حاکی از آن بود که ۲۰ نفر در زلزله ۷.۲ ریشتری در چهار استان ژاپن زخمی شده‌اند. لرزش‌ها تا توکیو و اوساکا نیز احساس شدند و سلسله زلزله‌ها همچنان ادامه دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/130665" target="_blank">📅 14:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130664">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
سی‌ان‌ان: نشانه‌های فزاینده‌ای از استفاده از مسیری نزدیک به ساحل عمان وجود دارد
🔴
چندین کشتی تجاری بزرگ از بخش جنوبی تنگه هرمز به سمت بنادر خلیج فارس عبور کردند که نشان می‌دهد کشتی‌های بیشتری مایل به استفاده از مسیری در مجاورت سواحل عمان هستند.
🔴
در میان کشتی‌هایی که روز یکشنبه وارد خلیج فارس شدند، دو نفتکش و دو تانکر گاز مایع وجود داشت و یک کشتی کانتینری نیز از همین مسیر از تنگه عبور کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/130664" target="_blank">📅 14:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130661">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRSCp-eWigst8ZV5PfImzYMqTcEp8Qz2JJQYaB7zYlcya6KjlUebOWtuFIsxSM_5Oqh8XfrnwlNmqo50TMmKsUp5wLKelGBYa6jZn8BaV6j2wX5f9bOWnAA1BOupDN2Azg1AzM7BfmkrnwC_D3wN6LPmR9N29fl2dATP8p-gtsidqE4PPgt8Nj8qKDTr_bFuY24ZL8_q8YSUT1uGWHWLdQPrt6U-_eeTsiyeQuRrtHWOGoRF-T7GmlCrvjiFzkv6hjahRCaDfsNufyojwoniRh27EVWP2bbwa9pRMycdcUC2vdhCXQKw0D0ixbPid1HD7xFr8dLu1b3-vhfwSZiEMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b425c3270.mp4?token=C8wckPrVfE9veCJecnks2A8VJ-TGeFYTeyZWlxoY50SJNIZVKMiQo-Oyr_GgjkVl1zRzn1LTMvvaAFnNcHR8S3Tf4WDbjqjbx7uaSXMffvf6myTh8OrKZG9_CriDSyQ___jeB5jWWt_Z9-RoAXUx5Wgi6Hv3Jx0ppfx6ZuX13f9pAubj3nZI6j8c2Yy6ZiaZBnT3TJ_neozGfo7u_yOgnbKNZ1zDnTbUdLp74juEGcdv1QHWVhc9W0jXAoNGNRrNO3yszCnfZGKpp8m5CT55jkpbUF7RAjgGbAGdyFHc6kgC1mwYt0nNMDPLwMUSwvLLntzq629cWrxE8409PLeSgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b425c3270.mp4?token=C8wckPrVfE9veCJecnks2A8VJ-TGeFYTeyZWlxoY50SJNIZVKMiQo-Oyr_GgjkVl1zRzn1LTMvvaAFnNcHR8S3Tf4WDbjqjbx7uaSXMffvf6myTh8OrKZG9_CriDSyQ___jeB5jWWt_Z9-RoAXUx5Wgi6Hv3Jx0ppfx6ZuX13f9pAubj3nZI6j8c2Yy6ZiaZBnT3TJ_neozGfo7u_yOgnbKNZ1zDnTbUdLp74juEGcdv1QHWVhc9W0jXAoNGNRrNO3yszCnfZGKpp8m5CT55jkpbUF7RAjgGbAGdyFHc6kgC1mwYt0nNMDPLwMUSwvLLntzq629cWrxE8409PLeSgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک خودرو در هولون منفجر شد و مردی را کشت که پلیس می‌گوید او را می‌شناخته و به چندین حادثه جنایی مرتبط با درگیری‌ها در جامعه عربی یافا مرتبط بوده است.
🔴
انفجار تنها چند ساعت پس از انفجار مشابه یک خودرو در یافا رخ داد، جایی که یک مرد کشته شد و پسر جوانش به طور متوسط زخمی شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130661" target="_blank">📅 14:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130660">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgG9Aj3wBBiew120pyLNMzjTT0vKM-THEPK6I0q4vkgamkQgtnLgFjFYJRH6X_7njyiQtG4he_rO6Qm1ekShZ3NuT0jG4iD6_fTTyru95eTuupC_hKQVNi5aOKsl76oVh2mf_mucN7wQpqIBUjyrxNfwOvf4QNLEECORP0mbobuZM-lQGIkKNuVqVyF_FKuWYZgz2ZZLlXEUo2M0JdoSpKaiKShZEHXeWn0yQMX1nDnzM8ZiECjpnp0xy6_Fzy3rmb8crrUfbDqNWzhumAfyJob_BDsQg6CMMZwx2TDJkkLfiTDRcQQS8dE8X7S4UmW-Kddm4da6qzPiN4s0IVNrxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر اسرائیلی، الی کوهن، می‌گوید دولت جدید راست‌گرای اسلوونی به رسمیت شناختن فلسطین را لغو کرده و سفارت خود را به اورشلیم منتقل خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/130660" target="_blank">📅 14:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130659">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/337aefd3c4.mp4?token=vyx4_KN-wXDgQx2EBTpdSUROBNtY5VQBpqfIk9D6wfvy09Blwkk_M-LNLBoBdV3zPol09MnotMQ-P5GX1eZSk4xHB0MH-67CPiE0WR4xdDKG1OF0pNfjoyZH-w-AC8aSGUnoBibr4KDMVkS1nHEh_-1HDyHBLlLD2KnrUrBh5VlWOXQ6ypsngVRvEf1WZTXsq7YO9_qfaquUe9Calrr1TI9sTmROt286X9W_qK3Snw5OSNM-OsR2ntNhNZOB5fEAwIjVISqSoUBY9cM5PKoo7gWatXcPfj9_O7eMc6BjsXeZk13x1CGrXSIZW_LGaD4xxN8sSzhJt-yUt8D0urrk_DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/337aefd3c4.mp4?token=vyx4_KN-wXDgQx2EBTpdSUROBNtY5VQBpqfIk9D6wfvy09Blwkk_M-LNLBoBdV3zPol09MnotMQ-P5GX1eZSk4xHB0MH-67CPiE0WR4xdDKG1OF0pNfjoyZH-w-AC8aSGUnoBibr4KDMVkS1nHEh_-1HDyHBLlLD2KnrUrBh5VlWOXQ6ypsngVRvEf1WZTXsq7YO9_qfaquUe9Calrr1TI9sTmROt286X9W_qK3Snw5OSNM-OsR2ntNhNZOB5fEAwIjVISqSoUBY9cM5PKoo7gWatXcPfj9_O7eMc6BjsXeZk13x1CGrXSIZW_LGaD4xxN8sSzhJt-yUt8D0urrk_DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلزله ونزوئلا؛ تصاویری دردناک از لا گوایرا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/130659" target="_blank">📅 14:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130658">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
اسماعیل کوثری، عضو کمیسیون مجلس : شعار مرگ بر آمریکا عبادته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130658" target="_blank">📅 13:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130657">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8jTrIHGMjfjOmYeip9G_joF_ZE7xPTyYnael3_flAzyM9To93rHL6_DUPH8hwucIyfQPfT1YfQ5uSuA59fmi-KMdEeJykPbsk_4gFus7LC2i0Bxk1IymPeT7jMw2J_wCmjsY6HDONWdfc4zSxKycRiMPbBPF-cAv5GK2mO50ks3Y2LZFKwkaZBGFv3K7UuCDwHM6BOKEPm0Quq-YTEAqQhCxw4UkDC3uxrNN0syESdykQZN7jbw0a6zhBh39WX-LcNWGAiG6OI_CsWWD7Asq58DKaknvvm2B1XhvWXo8WKI211OkPXVVA01-urcO9YXpIrQHcRaVBYHjemHJ4LIrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری پربازدید از  اقامه نماز در رختکن تیم ملی فرانسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/130657" target="_blank">📅 13:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130656">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
شهردار منطقه ۱۰: ساخت اولین پارکینگ پناهگاه تهران در یکی از مناطق پرجمعیت و پرتراکم تهران به اتمام رسید و بزودی بهره‌برداری از آن آغاز می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/130656" target="_blank">📅 13:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130655">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a6b806d95.mp4?token=jMZS9Rkk9MKcoBumvle5CElQ95ig6aYv44SBC_2gPLevRWG_LytqHl2izGy69RuX_DpBNgSDXQBV9IebhNE5ueJVMqxSubLk3PFpl0KckzoX-4ySV5LBeCbl1KI-__dIwidjH1552lE9oWzrPJiDAJJR-GNJJ5vkyFBgfmx58xIOpk_93GxhEtyI5HPb6AbZENo0jrVbSJgDXQkT39TsOo0mBiGjpIpGRJ6v18mVLTkGbaMSJN8hb2vH2J4_BirwB1K2lFK7XaTQPyoIRyaAPQlIP89bbab5YRqXsmZ-25ShMdb7PwOE2jKIzSlHifzuKUx-_Un3Zhm4V8FHEhuQiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a6b806d95.mp4?token=jMZS9Rkk9MKcoBumvle5CElQ95ig6aYv44SBC_2gPLevRWG_LytqHl2izGy69RuX_DpBNgSDXQBV9IebhNE5ueJVMqxSubLk3PFpl0KckzoX-4ySV5LBeCbl1KI-__dIwidjH1552lE9oWzrPJiDAJJR-GNJJ5vkyFBgfmx58xIOpk_93GxhEtyI5HPb6AbZENo0jrVbSJgDXQkT39TsOo0mBiGjpIpGRJ6v18mVLTkGbaMSJN8hb2vH2J4_BirwB1K2lFK7XaTQPyoIRyaAPQlIP89bbab5YRqXsmZ-25ShMdb7PwOE2jKIzSlHifzuKUx-_Un3Zhm4V8FHEhuQiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقوع انفجار در تل آویو
🔴
منابع خبری گزارش دادند یک خودرو در منطقه «حولون» در تل آویو منفجر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/130655" target="_blank">📅 13:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130654">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
الشرق نیوز سعودی به نقل از منبع عراقی: نیرو‌های امنیتی عراق اقدام به بازداشت سیاستمداران مرتبط با پرونده‌های فساد در منطقه سبز کردند
🔴
الحدث به نقل از منابع آگاه: ۱۷ مقام دستگیر شدند؛ از جمله معاون پیشین وزارت نفت عراق و رئیس یک فراکسیون پارلمانی که متشکل از ۱۹ نماینده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130654" target="_blank">📅 13:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130653">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43c16a967.mp4?token=d-1n91v9IYBEf2kzmWVn-QgrDpM5_s-Q-0kiYsLm6ya4Q9DED4Ti5e_7Mv9SBjE4yE7x0oamVWzV6rrJHczPLHP3Cdpu2uuPaWEygUb8vsMq2Mr6sF8jsX3emLOp1ETQcbgIpj0saXnWa2EEuNYj5iAV1yVPM3axkC1V9fkV_geEOdlS4nuKTa0lVgIh2Ihlg_4Il7buQxbC-d8Y9pcIR4jyYdD84tS3d7rMlDUqiARMMLtqPqdpHLpjuzDkbs1VTuoUj07Ds-klYh32w1-YYmKOS8W_hcq4OfT31N0Ybgbzo1W4b6b_vFPzz-GlWUt_adbm-xtsQDvkMnkB42xGOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43c16a967.mp4?token=d-1n91v9IYBEf2kzmWVn-QgrDpM5_s-Q-0kiYsLm6ya4Q9DED4Ti5e_7Mv9SBjE4yE7x0oamVWzV6rrJHczPLHP3Cdpu2uuPaWEygUb8vsMq2Mr6sF8jsX3emLOp1ETQcbgIpj0saXnWa2EEuNYj5iAV1yVPM3axkC1V9fkV_geEOdlS4nuKTa0lVgIh2Ihlg_4Il7buQxbC-d8Y9pcIR4jyYdD84tS3d7rMlDUqiARMMLtqPqdpHLpjuzDkbs1VTuoUj07Ds-klYh32w1-YYmKOS8W_hcq4OfT31N0Ybgbzo1W4b6b_vFPzz-GlWUt_adbm-xtsQDvkMnkB42xGOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عباس عراقچی: هرگونه دخالت و هرگونه تلاش برای اتخاذ ترتیبات جدید یا جداگانه از آنچه ایران در خصوص تنگه هرمز در نظر گرفته است، تنها وضعیت را پیچیده‌تر کرده و بازگشایی تنگه را به تأخیر می‌اندازد و تنش‌ها را افزایش می‌دهد، همان‌طور که در دو شب گذشته شاهد حوادثی در تنگه هرمز بودیم که منجر به افزایش تنش‌ها و درگیری‌ها شد.
🔴
از همه طرف‌ها می‌خواهم در مدیریت تنگه هرمز و ترتیباتی که جمهوری اسلامی ایران برای بازگشایی تنگه اتخاذ کرده است، دخالت نکنند، به یادداشت تفاهم امضا شده پایبند باشند و اجازه ندهند این یادداشت از مسیر خود منحرف شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/130653" target="_blank">📅 13:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130652">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
طبق گزارش روزنامه هاآرتص، سامانه‌های دفاعی اسرائیلی به قطر و عربستان سعودی فروخته شده‌اند؛ با وجود اینکه هیچ‌یک از این دو کشور روابط دیپلماتیک رسمی با اسرائیل ندارند
🔴
اسناد و تصاویر نشان می‌دهند که هواپیماهای سلطنتی قطر به سامانه دفاع موشکی C-MUSIC ساخت شرکت Elbit Systems اسرائیل مجهز شده‌اند؛ سامانه‌ای که برای محافظت از هواپیماها در برابر موشک‌های گرمایاب طراحی شده است.
🔴
همچنین شرکت‌های اسرائیلی در برنامه جنگنده‌های F-15QA قطر نیز مشارکت داشته‌اند و قطعاتی از جمله کلاهخودهای رزمی JHMCS و عینک‌های دید در شب AN/AVS-9 را تأمین کرده‌اند.
🔴
عربستان سعودی نیز از طریق برنامه F-15SA شرکت Boeing تجهیزات مرتبط با اسرائیل دریافت کرده است؛ از جمله صدها کلاهخود JHMCS و عینک‌های دید در شب.
🔴
ارزش فروش کلاهخودها به عربستان سعودی به‌تنهایی حدود ۱۰۰ میلیون دلار برآورد شده است، در حالی که قطر جداگانه ۱۶۰ کلاهخود را در قراردادی به ارزش ۳۵ میلیون دلار خریداری کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/130652" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130651">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f694ed771b.mp4?token=lrgHrVL6yWg3PjlBP4qBfU0yAYGcgqRnkLtdjoi3FziD565atM3gLdb7Fghe507tzjzV6oWrWkXS0jiwrZMS5yoH0YfxwiREUdccRu92iSEAINmrnf5t8YeCOpSAn0hCAV7ZLf6m6uVTjeJlp98JTunrDXtEQQYy2-vj02CQUbO4Jvvk0vHn1LQr6NfZYOhLRtWVHrJeN4l7WqvNCti5R8L2fdzjcSdn3KRiMmgr-BRgVVF1CAeDPmIny3R_ovRaIq9Tbwn9CbXU5XgG_BJ8Bca1PsDbeoU-gc1kibq28woZcFCpQnnxQ9GFielW6nSDJauQ2pYu0v-5JWs7Y-cwBDzRO7PqHnB6LzbLJYCHty-u9OGQCuzxKxIM2hvM2-2YtjHz0Z5q9odeboqtkXqiDGk5T1UvJ4vnpW6ADlwG790QYux3aS5imIb7VjqQAakUBuSu_z-_PhvyLWDeIb7iuuoFmieonzKRd_aiueaFCx7nVMo_iJiuif2aHObJaeNocDzd1ORJ9XPMPR4LSm5nIFOvpfCOXTaa6bmdwKK3tvO3tx0myALy49xxcIZxb7MWWokTTNzURL-XLqEtqiMshDDp3UXHb5cZMMfzuazCE_smSEpeehzrttA_ZWjNBbJ1r7V5WPPzbwkla8aRD5YpLgBMJs2rRdAI7YQEv0ko2Qs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f694ed771b.mp4?token=lrgHrVL6yWg3PjlBP4qBfU0yAYGcgqRnkLtdjoi3FziD565atM3gLdb7Fghe507tzjzV6oWrWkXS0jiwrZMS5yoH0YfxwiREUdccRu92iSEAINmrnf5t8YeCOpSAn0hCAV7ZLf6m6uVTjeJlp98JTunrDXtEQQYy2-vj02CQUbO4Jvvk0vHn1LQr6NfZYOhLRtWVHrJeN4l7WqvNCti5R8L2fdzjcSdn3KRiMmgr-BRgVVF1CAeDPmIny3R_ovRaIq9Tbwn9CbXU5XgG_BJ8Bca1PsDbeoU-gc1kibq28woZcFCpQnnxQ9GFielW6nSDJauQ2pYu0v-5JWs7Y-cwBDzRO7PqHnB6LzbLJYCHty-u9OGQCuzxKxIM2hvM2-2YtjHz0Z5q9odeboqtkXqiDGk5T1UvJ4vnpW6ADlwG790QYux3aS5imIb7VjqQAakUBuSu_z-_PhvyLWDeIb7iuuoFmieonzKRd_aiueaFCx7nVMo_iJiuif2aHObJaeNocDzd1ORJ9XPMPR4LSm5nIFOvpfCOXTaa6bmdwKK3tvO3tx0myALy49xxcIZxb7MWWokTTNzURL-XLqEtqiMshDDp3UXHb5cZMMfzuazCE_smSEpeehzrttA_ZWjNBbJ1r7V5WPPzbwkla8aRD5YpLgBMJs2rRdAI7YQEv0ko2Qs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو، خطاب به ایران : به شما ربطی نداره هیچ جایگاهی اینجا ندارید
🔴
نه شما، نه حزب‌الله ،هیچ نقشی یا حقی در این موضوع ندارید
🔴
اسرائیل و لبنان هم بر سر دو منطقه نزدیک به خط آبی (مرز) که من پیشنهاد داده بودم، به توافق رسیدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/130651" target="_blank">📅 12:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130650">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
نتانیاهو : توافق ما با لبنان ضربه بزرگ به ایرانه
🔴
ما این موضع رو حفظ می‌کنیم تا وقتی که حزب‌الله و بقیه گروه‌ها خلع سلاح بشن و دیگه از سمت لبنان هیچ تهدیدی متوجه اسرائیل نباشه
🔴
ایران سعی داشت ما رو مجبور کنه از جنوب لبنان عقب‌نشینی کنیم
🔴
این خواسته‌ها رو بارها شنیدید و ناراحتی و انتقادشون از توافق، هم از طرف ایران و هم حزب‌الله، رو هم دیدید
🔴
من روی منافع حیاتی اسرائیل ایستادم و با این ایده که بخوان ما رو با زور وادار به عقب‌نشینی کنن، مخالفت کردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/130650" target="_blank">📅 12:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130649">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XA-bX2WklBQzoD8N1fwQE2TuHK4jMD60IQdJOz98bTW3UHJKJaukNmItv0cSgzP9N9hjRCcmwXedTgQD6mtHPMeW_3ftFNgrplXho18xbFBfOqmNohVQIk_huDqDQ6BBBptTaOvKj1akqXTEglTuxKCp65J3bj-4nnuGvQcW6x6hLZgra3853NjGgvc1Q-p_JiO0ZrmegHCGTtl1nlHSSJncjHxfbnIWCf0_Rkch3zfLWiacgnmmZeABaaKDceSKifs-O7olqutCBjBavfegJeOp9rdpIK6mC4DXjwZkl3HO8x99Ha0MPKB1UPv9QapSfW067NlyUl1fOIywY1jlfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ریزش ۱۰۰ هزار واحدی شاخص بورس
🔴
شاخص کل بورس با ریزش ۵۳ هزار واحدی در پایان معاملات امروز به ۵ میلیون و ۰۷۵ هزار واحد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/130649" target="_blank">📅 12:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130648">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
عراقچی: مسئولیت ترتیبات تنگه هرمز با ایران است و هیچ نهاد یا کشور دیگری در این خصوص مسئولیتی ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/130648" target="_blank">📅 12:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130647">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=LZlBcuvEN0VSdyr7z64y3UPDzk6sXFUpYAGG51mvqtnUjWDLL1WR_9nwQAzZw_-t3E2NiQ6sgc24OIEJ2pjdomqRlbfwuUq3SV0Sp4GES2xuQQGBIcs3FxFO2OKVzao7DdQclrkFMOsrsc6dvxZ_DAlyElWzaZONfpuny7jUCvTqlfCCU4nPC8qLtxHKS-YFEP613FVyhQggDyHUENiZfbeRg4HBCLCiboPVBVZu-AAK5lCDzW3Cq_ar3jSwNOgpjJbHOY6wvGUXPF4KeAbK53OQat6CgAZwc6VO2yQnQncxjzAmalxFKbwHcnCyl5bPpjFpfgwqSbMgL5aX_s2ltQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=LZlBcuvEN0VSdyr7z64y3UPDzk6sXFUpYAGG51mvqtnUjWDLL1WR_9nwQAzZw_-t3E2NiQ6sgc24OIEJ2pjdomqRlbfwuUq3SV0Sp4GES2xuQQGBIcs3FxFO2OKVzao7DdQclrkFMOsrsc6dvxZ_DAlyElWzaZONfpuny7jUCvTqlfCCU4nPC8qLtxHKS-YFEP613FVyhQggDyHUENiZfbeRg4HBCLCiboPVBVZu-AAK5lCDzW3Cq_ar3jSwNOgpjJbHOY6wvGUXPF4KeAbK53OQat6CgAZwc6VO2yQnQncxjzAmalxFKbwHcnCyl5bPpjFpfgwqSbMgL5aX_s2ltQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حملات اوکراین به پالایشگاه یاروسلاول در روسیه
‎
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/130647" target="_blank">📅 12:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130646">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
عراقچی: آمریکا موظف به توقف حملات اسرائیل و اجرای آتش‌بس است
🔴
بر اساس بند نخست یادداشت تفاهم، جنگ در تمامی جبهه‌ها از جمله در لبنان باید به طور کامل خاتمه یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/130646" target="_blank">📅 12:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130645">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/487cb1c4d0.mp4?token=RVP9TcxeWwPkMhChgPJzrzJcCy3R31WadWEC2pG6D4fLyNVZaDOoBW3pEPhT_Itmr_Hs7IAXcwbG8eCC3Q0ATPOC0hH11mgc_I6NJeuvbeGVC103uZpml6IxghICZNADvKSryx1PxmP_TlxE7BCdfo3WV8a9-aTr3yEtkdHp2KW1MDxcXsouay6_iqy5eooDDFrOTyjriwt9CZG30lX8RabcXcW9EBS3vAFdMpuFzwXEtoAJnJ5G89tD4dxd5tq23hmbZbTsoGnOH-Sfa0iqZGnYJ3Jg2kT-tAeRk0m5D9lijMw60NApUanUFBUGqmCN8un52BbfC-riSoPgmZ64tbTmhAdohSXaJqQ2ZwUzE6TAYg8lEaID6KfAaNbQKX5OmheOJmV4kyMwsi9OCVlH0iPW1qxrQJBswDZoiyDY_2vT8swP3EwU2YO4VqsD_E8REtW87if6jCFAoBjI4plwYvocxV7Oi_kzmUov0Jw2dvs8YTxbhRrwrfqu3c1ShsNT4UYXvrJ5NKc9JvNGgid2i1TMBUr1Axsk5ojvqwzxbDhen-lgDXh5fmCmzRzQFPVmMI8k529IdUP6d13l5yrOzvS6EtnrfWi8hcGfLfvPN0J8S1DIvO-_XH6gbx7kvVoE9z9sJAQ1HL2KIXCoqJXFFS7u3CC4tX26dJbWHr789DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/487cb1c4d0.mp4?token=RVP9TcxeWwPkMhChgPJzrzJcCy3R31WadWEC2pG6D4fLyNVZaDOoBW3pEPhT_Itmr_Hs7IAXcwbG8eCC3Q0ATPOC0hH11mgc_I6NJeuvbeGVC103uZpml6IxghICZNADvKSryx1PxmP_TlxE7BCdfo3WV8a9-aTr3yEtkdHp2KW1MDxcXsouay6_iqy5eooDDFrOTyjriwt9CZG30lX8RabcXcW9EBS3vAFdMpuFzwXEtoAJnJ5G89tD4dxd5tq23hmbZbTsoGnOH-Sfa0iqZGnYJ3Jg2kT-tAeRk0m5D9lijMw60NApUanUFBUGqmCN8un52BbfC-riSoPgmZ64tbTmhAdohSXaJqQ2ZwUzE6TAYg8lEaID6KfAaNbQKX5OmheOJmV4kyMwsi9OCVlH0iPW1qxrQJBswDZoiyDY_2vT8swP3EwU2YO4VqsD_E8REtW87if6jCFAoBjI4plwYvocxV7Oi_kzmUov0Jw2dvs8YTxbhRrwrfqu3c1ShsNT4UYXvrJ5NKc9JvNGgid2i1TMBUr1Axsk5ojvqwzxbDhen-lgDXh5fmCmzRzQFPVmMI8k529IdUP6d13l5yrOzvS6EtnrfWi8hcGfLfvPN0J8S1DIvO-_XH6gbx7kvVoE9z9sJAQ1HL2KIXCoqJXFFS7u3CC4tX26dJbWHr789DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گرمای شدید در فرانسه باعث بیهوشی راننده اتوبوس و تصادف شد
🔴
در فرانسه، یک راننده اتوبوس به دلیل گرمای شدید هوا هنگام رانندگی دچار بیهوشی شد و در نتیجه این اتفاق، راننده کنترل وسیله نقلیه را از دست داد و حادثه رخ داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/130645" target="_blank">📅 12:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130644">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtB-ZPu3tQk_I3xX7FPjIuyDGqZ_izYXB-fFeJrJ411yWolTouo1dxNAQ5ERqolyGRhdZgSPyNfHEbLW-24t6jtq9fAZEBSWfs2WRhCGniMEYpJ1EAPFuhEMIQ03ax5Z-uJRipH12a3blVSaaatAbuJf1ojj6AgMZMvzaU6SLImfu_cjPlM_lct1yJopeOjsO4KA-kpZqwTHN-YbZVJt_vo4toLEpYFO0c2KrBuGIVTgAyAV2NNf_hte1x4SZEeSgVAXd2k_SgsDJtkDsh33T1UXhrPARmHPb59y6VhyMzz--Q9sQ3nBIMwr3GiEGdU0uLh3Ka9HfhNYLFrblI5FXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/130644" target="_blank">📅 12:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130643">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
قیمت دلار ۱۷۰ هزار و ۵۰۰ تومان شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/130643" target="_blank">📅 12:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130642">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
عراقچی در بغداد :  روابط راهبردی ما بین ایران و عراق به طور ارزشمند ادامه داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/130642" target="_blank">📅 12:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130641">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26a14380ab.mp4?token=vW4x5YRUcKChjxDH113lrgqzfQhmwQgj0JKZUXlP5WYyKMRba4bTJOYpSvyNJMiQtGIGpgyt5vR25KRwxxEOjL-wUIP4iK8UoEcYB9GDcdCgvsZorE74AP3pWWhO3gfJxuhvkW48vzqGb2jf_l042p_pHB5PTFhIt99_mpj4QD77bZTRmvG6pjN6LEzCFcYbA0miLLBg4C-g3eyA2d-gatj8IFpk7LNd2LVwYzlOmBkKH_ASwol5GOQqqKoSQPlbxAPMbnQ0n67L6njJkB0EkQAtdqVW_lKn3HPOlF8nupkaUqtHt5DPf5PLKuTn3MmwbK8wqx87G6yeADdO9NSNJjqNapzLZLljTJXvOo6wIhMv1mrAxDTvkS7DO5sd33c26ekDoGLf5dNkLXfMC92xEhyfjkhXoe8KetDI3qIJ9MTAIrJo88QSwTxdZlLUP2q8MaDXG2s2n463SLEbuIWzcUQs7-iC6rTpDkW887SOYtesmWyPP3OdlsXzjfy5Y0vp_eYzi24O4OI6PkKBPURcZslZ0hIVJRRhUPzHRJFYhYrIrq9ZSJTbJ3A26toBoqUQvoY3Rf4JB4VjYlNHPISi1fTtGRQmtzFRWOMt9CaF4D3DhbTWnJsfZoNgO6olxJ50PMzZdgVVbCCYgtuNS9VyBN6DlGgQ2np3FC1iwr2n5TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26a14380ab.mp4?token=vW4x5YRUcKChjxDH113lrgqzfQhmwQgj0JKZUXlP5WYyKMRba4bTJOYpSvyNJMiQtGIGpgyt5vR25KRwxxEOjL-wUIP4iK8UoEcYB9GDcdCgvsZorE74AP3pWWhO3gfJxuhvkW48vzqGb2jf_l042p_pHB5PTFhIt99_mpj4QD77bZTRmvG6pjN6LEzCFcYbA0miLLBg4C-g3eyA2d-gatj8IFpk7LNd2LVwYzlOmBkKH_ASwol5GOQqqKoSQPlbxAPMbnQ0n67L6njJkB0EkQAtdqVW_lKn3HPOlF8nupkaUqtHt5DPf5PLKuTn3MmwbK8wqx87G6yeADdO9NSNJjqNapzLZLljTJXvOo6wIhMv1mrAxDTvkS7DO5sd33c26ekDoGLf5dNkLXfMC92xEhyfjkhXoe8KetDI3qIJ9MTAIrJo88QSwTxdZlLUP2q8MaDXG2s2n463SLEbuIWzcUQs7-iC6rTpDkW887SOYtesmWyPP3OdlsXzjfy5Y0vp_eYzi24O4OI6PkKBPURcZslZ0hIVJRRhUPzHRJFYhYrIrq9ZSJTbJ3A26toBoqUQvoY3Rf4JB4VjYlNHPISi1fTtGRQmtzFRWOMt9CaF4D3DhbTWnJsfZoNgO6olxJ50PMzZdgVVbCCYgtuNS9VyBN6DlGgQ2np3FC1iwr2n5TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کلیپی از شادی بازیکنای تیم ملی‌ تو هتل که امروز فکر کردن صعودشون قطعی شده اما ۱ دقیقه بعد از این خوشحالی، بخاطر گل دقیقه ۹۶ اتریش به الجزیره صعود کنسل شد...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/130641" target="_blank">📅 12:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130640">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
در پلی مارکت هم‌چنان بر روی صعود تیم ملی ایران شرطبندی می‌کنند
🔴
تیم های اتریش و الجزایر الان تو آمریکا هستن و برای بازی باید به کانادا بروند
طبق آمار احتمال سقوط یک هواپیما ۰.۰۰۰۴ درصده که اگه این اتفاق رخ بده ایران هنوز شانس داره جایگزین یکی از این تیم ها بشود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/130640" target="_blank">📅 12:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130639">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
یک منبع مطلع در گفتگو با ای ۲۴ نیوز مدعی شد:  اهدافی که فرماندهی مرکزی آمریکا دیشب در ایران مورد حمله قرار داد، هم اهداف جدیدی بودند که ایرانی‌ها اخیراً ایجاد کرده‌اند و هم اهدافی که قبلاً مورد حمله قرار نگرفته بودند.
🔴
از جمله زیرساخت‌های ردیابی، سیستم‌های ارتباطی، سایت‌های دفاع هوایی، تأسیسات ذخیره‌سازی پهپادها و توانایی‌های کاشت مین مورد حمله قرار گرفتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/130639" target="_blank">📅 11:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130638">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ریاست جمهوری لبنان: ما حملات ایران به بحرین و کویت را محکوم می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/130638" target="_blank">📅 11:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130637">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
دلار هم اکنون 170,000 تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/130637" target="_blank">📅 11:33 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
