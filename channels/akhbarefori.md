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
<img src="https://cdn4.telesco.pe/file/TmjqJV9Vm65Fbi0qiDGJyqcQ7-p2v6ntmxbg_ICOybzlmVdjrS_IkB7cUo-l7KGc1kifEZjT8QHzjWhsffoof6e1R24m8M6IrQFW0_CwDe5R-ZQBCU9H4BeNh55Upd43kCShBFMbgCmBZHuQpNxve4hx7ST9yzh8rZCjihySMSA0jWTsing9Og8H-145I8EZ5ikmluXfDIlBQBFh841Ubuy7mboGAbogm0MIZBCgqGNNTjw-vfgLvIlj5ijOOvFOb1YAlm4GGuWH2_qYcJJDqxta5XsdlX4mKVk41LGtiwXGRZy9jsLBOHWNCQBtGCt0iYzu_Nc_lKrcm_JdeJmqKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.39M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-05 03:22:42</div>
<hr>

<div class="tg-post" id="msg-684636">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
نفوذ هکرها به ناسا، فدرال رزرو و سنای آمریکا
آمریکا:
🔹
یک عملیات هکری مرتبط با چین به شبکه‌های چندین نهاد حساس، از جمله وزارت دادگستری، ناسا، فدرال رزرو و سنای آمریکا نفوذ کرده است./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/akhbarefori/684636" target="_blank">📅 03:20 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684635">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
نخست وزیر قطر به تهران سفر می کند
🔹
شیخ "محمد بن عبدالرحمن آل ثانی" نخست وزیر وزیر خارجه قطر قرار است به زودی به تهران سفر کند. این سفر احتمالا فردا پنجشنبه و در چارچوب میانجیگری میان ایران و آمریکا صورت می گیرد.
🔹
در چند روز اخیر هم فرمانده ارتش پاکستان…</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/akhbarefori/684635" target="_blank">📅 03:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684634">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
کشورهای گروه عرب سازمان ملل: صلح منطقه‌ای منوط به پایان اشغالگری اسرائیل است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/684634" target="_blank">📅 01:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684633">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
انفجارهای شدید در انبارهای سلاح وابسته به مزدوران سعودی
🔹
منابع یمنی از اصابت موشک‌های ارتش و انصارالله یمن به انبارهای مهمات و مواضع مزدوران سعودی در بندر المخا خبر دادند.
🔹
همزمان انفجارهای شدیدی نیز در شهر الخوخه در جنوب استان الحدیده که تحت اشغال مزدوران…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/684633" target="_blank">📅 01:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684632">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b551e124.mp4?token=V2LDe7gcHHQ_YpWF6Xiv9UPx7pdMyvZ1JQmHRpZhvwF9LQHkjFOmGQKHDD3raYTu94U3iIwIUy3ufyamJ6O-63tUrBmPmlFcaFGWktJDVzWDk7THcw0Za7a7AqKSyxRzfAdmCk3KXLCTlEjdjJ3MsFE8naXrBD76qrg5X4noR1TqpRFes1ajuaRtIMJjPbSQYZuxf6CrA4DthxyHfD9Ow8d0qOhGV7QNjO2-EhglhT2VKdbPUYrYfB1D3D5aFT8ApfJwK6P3JI3B2hotbT1AKgyA2wHZEUyUGJ_6YEAb2MPcPjDIetGGyVFu9EMwrPPriHpt-3iRWc_xIjeZfE08QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b551e124.mp4?token=V2LDe7gcHHQ_YpWF6Xiv9UPx7pdMyvZ1JQmHRpZhvwF9LQHkjFOmGQKHDD3raYTu94U3iIwIUy3ufyamJ6O-63tUrBmPmlFcaFGWktJDVzWDk7THcw0Za7a7AqKSyxRzfAdmCk3KXLCTlEjdjJ3MsFE8naXrBD76qrg5X4noR1TqpRFes1ajuaRtIMJjPbSQYZuxf6CrA4DthxyHfD9Ow8d0qOhGV7QNjO2-EhglhT2VKdbPUYrYfB1D3D5aFT8ApfJwK6P3JI3B2hotbT1AKgyA2wHZEUyUGJ_6YEAb2MPcPjDIetGGyVFu9EMwrPPriHpt-3iRWc_xIjeZfE08QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنان ضدایرانی نخست‌وزیر جنایتکار رژیم صهیونیستی/ نتانیاهو از بررسی گزینه‌های شرورانه علیه ایران با ترامپ خبر داد
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/684632" target="_blank">📅 01:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684631">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
منابع محلی از تکرار حملات تجاوزکارانۀ رژیم صهیونیستی به مناطق مختلفی از جنوب لبنان خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/684631" target="_blank">📅 01:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684630">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
منابع عربی از انفجار در مواضع مزدوران سعودی در المخا درپی حملات یمنی‌ها خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/684630" target="_blank">📅 01:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684628">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ادعای واهی نخست‌وزیر اشغالگر رژیم صهیونیستی: هدف اصلی صهیونیسم بازگشت یهودیان به سرزمین فلسطین بوده است
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/684628" target="_blank">📅 00:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684627">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
بلومبرگ: وزارت دادگستری آمریکا در حال احیای «دادگاه غنائم جنگی» است تا بتواند نفتکش‌های ایران را به‌عنوان غنیمت ارتش مصادره کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/684627" target="_blank">📅 00:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684626">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc05f8a9f.mp4?token=KoRoUlSytD6JDe8Nmv496wHoU-N1T-MMgKGS8xXRbc9tqg8w_UDmiVzNWXUSA7ynEAHzaB91MJrZ8U235030MywtR41apo_MROsCTCGI9HtgLpWXOzJIXwzCqtx62m361PKFMoPOqFvxhAzHbywmPEUIrwltA7v7Ko4uuaR4ujNg5RcxwR_TGQi_wvOgEuyD_bvdYMhlGpme2_od1Ef5M9jNxDzgNz7994o1BsOZ93BZalIndp7CNWLVoecbHH-xfvqZ3CokjRLDySQFXOOo1wdWkn5AewIeYX92a3xTLvKDAQZbfzrBPsSkT8AWYOtX-tWA86HAd942WNwR5i_7og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc05f8a9f.mp4?token=KoRoUlSytD6JDe8Nmv496wHoU-N1T-MMgKGS8xXRbc9tqg8w_UDmiVzNWXUSA7ynEAHzaB91MJrZ8U235030MywtR41apo_MROsCTCGI9HtgLpWXOzJIXwzCqtx62m361PKFMoPOqFvxhAzHbywmPEUIrwltA7v7Ko4uuaR4ujNg5RcxwR_TGQi_wvOgEuyD_bvdYMhlGpme2_od1Ef5M9jNxDzgNz7994o1BsOZ93BZalIndp7CNWLVoecbHH-xfvqZ3CokjRLDySQFXOOo1wdWkn5AewIeYX92a3xTLvKDAQZbfzrBPsSkT8AWYOtX-tWA86HAd942WNwR5i_7og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروهای یمنی یک پهپاد جاسوسی عربستان سعودی را منهدم کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/684626" target="_blank">📅 00:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684625">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
برخی منابع خبری از وقوع حادثه دریایی در تنگه هرمز گزارش می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/684625" target="_blank">📅 00:38 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684624">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNCb7QpsbucscN0DPEm_asuQA2lYPgsj4gFn7LIIUNm2sfa1PZWJIzESDy713A9NHtcQDb1roWNEGcDJyZr6k9MdHJpWegVuGCP3hLzTuasNXicbJ5Y5pQTxJAGcA5CQULC-CAaS66Rsu8TnxJoO9whIZDvvFajYiUuZc7HHIWfGicO5jRxA9gqCzzUlLK5EqOTBlrELYDgeNnrZbNcBB80tJbfuISwPzdBm7N2fNPfUSbKjPfM1xhROxd47id2zFHiWuyoCtLSXeOgg6-zeJbDziu1caS69mvUt28YbJ2lVfvL00gtkEmo5XQkp23e5Y7W_v_jLFwnzMbMKeitrcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برگزاری رویداد «فن‌راوی» هم‌راستا با تقویت روایتگری رسانه‌ای پارک‌های علم و فناوری
🔹
رویداد تخصصی «فن‌راوی» امروز چهارشنبه ۴ شهریورماه، در پارک علم و فناوری خراسان رضوی با حضور مدیران روابط عمومی پارک های علم و فناوری کشور  شروع شد و تا فردا ادامه خواهد داشت.
🔹
معاون فناوری و نوآوری وزارت علوم از فعالیت ۶۰ پارک علم و فناوری، ۲۹۰ مرکز رشد و ۲۳ پردیس فناور در کشور خبر داد و با انتقاد از فعالیت سنتی روابط عمومی پارک‌ها، بر ضرورت اصلاح مسیر اطلاع‌رسانی و حرکت از انتشار اخبار معمولی به سمت روایتگری خلاقانه و اثرگذار تأکید کرد.
🔹
وی یکی از اهداف رویداد تخصصی «فن‌راوی» را ایجاد شبکه روایتگری رسانه‌ای میان پارک‌های علم و فناوری عنوان کرد و خواستار ایجاد ظرفیت‌های مشترک و هم‌افزا در این حوزه شد.
🔹
به گفته معاونت فناوری وزارت علوم هر شرکت فناور می‌تواند روایت‌های متنوعی از اختراع، تولید محصول، برندینگ، شکست و یادگیری داشته باشد.
🔹
رییس پارک علم و فناوری خراسان رضوی نیز روابط عمومی را پل ارتباطی میان سازمان و جامعه دانست و گفت این مجموعه‌ها می‌توانند داده‌های سازمان را به روایت‌های جذاب برای جذب سرمایه‌گذار و جوانان تبدیل کنند.
🔹
هم‌اکنون حدود ۷۰۰ شرکت با ۱۱ هزار نفر نیروی انسانی در زیست‌بوم پارک علم و فناوری خراسان رضوی فعالیت دارند که ۷۰۰ نفر از آنان دارای مدرک دکتری هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/684624" target="_blank">📅 00:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684622">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/850edb2075.mp4?token=ELJcPHREnfJY0qeWWEigGflCWd2rUTTkTJFiiToB-Ag5mIsHsxvvtFqGKtVk_mCRZxiUEeVZSHT4oUs1UE0mvP1Mz5V-hNeI0722WBIu0TFl6UwvhyKwWmAHlbNUBIaQGfgqnjpFPz0ofmFaISmX0CXUXR5i8KAH-eHhBK-WhcXddOJLCBfwKaRH8OEZs-zvarlG1H2cUSV1L3Ysj8SWtmVUEhwI0FxTqdgM22xE8h9YGEj9MUZvj8JCOAn6qxVREN7TcCP4z0KsfB7eToX0pOYbp6-qdEIqXC0VKGCz8NYpASc-Whkc8YHIB5lj6hjycxKaD0bQXg_HTfp7mNb3lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/850edb2075.mp4?token=ELJcPHREnfJY0qeWWEigGflCWd2rUTTkTJFiiToB-Ag5mIsHsxvvtFqGKtVk_mCRZxiUEeVZSHT4oUs1UE0mvP1Mz5V-hNeI0722WBIu0TFl6UwvhyKwWmAHlbNUBIaQGfgqnjpFPz0ofmFaISmX0CXUXR5i8KAH-eHhBK-WhcXddOJLCBfwKaRH8OEZs-zvarlG1H2cUSV1L3Ysj8SWtmVUEhwI0FxTqdgM22xE8h9YGEj9MUZvj8JCOAn6qxVREN7TcCP4z0KsfB7eToX0pOYbp6-qdEIqXC0VKGCz8NYpASc-Whkc8YHIB5lj6hjycxKaD0bQXg_HTfp7mNb3lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله انتحاری با استفاده از پهپادها به مقرهاى تروریست های تجزیه طلب کرد در اربیل را هدف قرار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/684622" target="_blank">📅 00:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684621">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f89fae6b.mp4?token=AxVJonHv66vlrB3J9H_h8l-DW4i4JTv1qodzvDQhXjyd0akdBmsxq3Y8pORNoa3alQr4MgcjQvMvUHbMQdkXyloQUF7C_ygpAsyWvy8DqgDMfQF3Kb0e41qgMnTjPJsR1jkoTy8cWNt82LxaFGk4-ie7gg-vQz5cffTlkMu0HcdhaVGdYaG15HdiX1BQ3FwdzKnV2Gyq_zfP4Mzfo-LuqHMf6BY7yt25R_2_fMNfHOnVT2dpRsEDS1YxBzw53OZr8gK3t86L_Qik7bWDGj2bA8iEoUVJ9Ejam4NTw-0e6hYEMeqhufgisHk4O14dRZDD9_YvqTGkuOMcBZ_6hnULSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f89fae6b.mp4?token=AxVJonHv66vlrB3J9H_h8l-DW4i4JTv1qodzvDQhXjyd0akdBmsxq3Y8pORNoa3alQr4MgcjQvMvUHbMQdkXyloQUF7C_ygpAsyWvy8DqgDMfQF3Kb0e41qgMnTjPJsR1jkoTy8cWNt82LxaFGk4-ie7gg-vQz5cffTlkMu0HcdhaVGdYaG15HdiX1BQ3FwdzKnV2Gyq_zfP4Mzfo-LuqHMf6BY7yt25R_2_fMNfHOnVT2dpRsEDS1YxBzw53OZr8gK3t86L_Qik7bWDGj2bA8iEoUVJ9Ejam4NTw-0e6hYEMeqhufgisHk4O14dRZDD9_YvqTGkuOMcBZ_6hnULSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از خارج کردن نفت به روش کشتی به کشتی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/684621" target="_blank">📅 00:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684619">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2a7V30kKSoyFLo65MwwnP6k7_NTNnbWOSzB5ThviovZ5oiJzcml0jNz2jzk5cz8nGlkkBbZEieiDws8S__cFu12O2AR8nBsa1D_PnVq4uL7vxqatEE70tNrKKyWL76y7rSvAYY-46hi-2XuL-hMDh_OsvE9DfPYmBarAifaiAK-8EBkB4UqbHUDH9hdEi3buxhunc5-IHhbA0BY6iZaSX9_Mf31VQS6VKj910zBlhgytj3ILNsVJWeC2UyusmY-ICr6nFxjQKpD3-SthBLLXBiKV7eES7tTzqCIte_Yl0YhxFQUzPqH074Mlm2OuCzDpW6-6LN0HnL3Yt4hmwNuWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c71bba8f8.mp4?token=oJ1UKHhHmuOwD4N2UVcgBNEXp6pk-ajcNi50_WfOGcTZE598IMlYnSqbS-FfrUiTR6ZTxANJKNzbHGQT_acmZKVnNhZtCTOTW3kB8yLPYAE75ORD6Mcd8XD_vXt2i9qh0OJciPSqpvbVagl2dt8q7i4xq5ticx4o9Ut7bB_wnPd09dmTyaBpsOdQNw6TQEE4v9udPoFklXpjHerTkQhD71BGhyav8NrxWUKhq6pR-tx8XNaOn_hJifb0m_oEiRdNm9BccCVW5oZpnuqzLEr0R0VDLCBSAnHvNh7hyBQFMeiqWzamJgj6uGYIRJBxluYoUTkmIbL0F_G3Et-mQe-tVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c71bba8f8.mp4?token=oJ1UKHhHmuOwD4N2UVcgBNEXp6pk-ajcNi50_WfOGcTZE598IMlYnSqbS-FfrUiTR6ZTxANJKNzbHGQT_acmZKVnNhZtCTOTW3kB8yLPYAE75ORD6Mcd8XD_vXt2i9qh0OJciPSqpvbVagl2dt8q7i4xq5ticx4o9Ut7bB_wnPd09dmTyaBpsOdQNw6TQEE4v9udPoFklXpjHerTkQhD71BGhyav8NrxWUKhq6pR-tx8XNaOn_hJifb0m_oEiRdNm9BccCVW5oZpnuqzLEr0R0VDLCBSAnHvNh7hyBQFMeiqWzamJgj6uGYIRJBxluYoUTkmIbL0F_G3Et-mQe-tVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای انفجار در اربیل عراق
🔹
منابع عراقی از حملات پهپادی به مواضع تروریست‌های تجزیه‌طلب در منطقه سوران در اربیل خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/684619" target="_blank">📅 00:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684618">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3NwesT1dm1BKg2mHNdtPN4gnT0ztI4qx3WEv95KJog0uKOzpigbyb8Kd5dYm_B7wPAshWxtHlO-NKOV_N9_ROIZgc4vWv20XqLBoVvvwnEXqNKnBDxa_pWziv3CMwlC1nrJE7x_-XWBokdQFLyQPNNBusTWqMB6qEBCgqadKeSXdxpe6p6Ed7R66LnxX_dLL6xjLZ58fwXTyqY4DnXawUrCzzMDgQ0461I5_7ZybeX-rJHR4lOn-iZ27JWmr3PkSdaOVPTU5ErR5xoOf48PSg4NwTuolC2AVwchKrKd9ktRZ-BRdHFw5Mj-b0VmbTrgLr3z1N89J-8isKSbB2pVqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هم سرنوشت
🔹
رسانه‌های خارجی امروز اذعان کردند که بر اساس گزارشات، آمریکا با ۱۶ کشور هم‌مرز ایران برای قطع روابط اقتصادی با ایران تماس گرفته که ۸ کشور درخواست آمریکا را دشوار دانستند و ۸ کشور دیگر پاسخ دادند که در حال بررسی این احتمال هستند. این موضوع نشان می‌دهد که فشار اقتصادی مضاعف به ایران بسیاری دیگر از کشورها را نیز تحت فشار قرار می‌دهد.
🔹
هشتصدوچهل‌وچهارمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/684618" target="_blank">📅 00:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684617">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca50a51f47.mp4?token=aGIHXDkxs0_HFNNmOTnE1bRq0RkpAgsLUObLyt2wDVI962JG6aP6WEBk8rCV_u8WCA9RItXivQi1zb3hZUVGyO0HAkoK9CDiN1AIAFzwS7NE_jnd9IuSnShszlcd5-z54sTAfwGXKHzh3yeg_vJasaMp0OxvwrWkTSBbgSWpONF1tRo5RCxLqamwUECmnMZ0MqmDws-UOOWn-9ZBPhkecrq084KbXUcSas0w79D9fo01OBaLPxjWpBGEF6cuCECk29lt81pKWfBDq2vzjowbJ5c1pSiuj2yWPS4B1JqI5HbWkXqG8ispi8dBxC79UZ_FjTyWCVh9zesFX730XCtegA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca50a51f47.mp4?token=aGIHXDkxs0_HFNNmOTnE1bRq0RkpAgsLUObLyt2wDVI962JG6aP6WEBk8rCV_u8WCA9RItXivQi1zb3hZUVGyO0HAkoK9CDiN1AIAFzwS7NE_jnd9IuSnShszlcd5-z54sTAfwGXKHzh3yeg_vJasaMp0OxvwrWkTSBbgSWpONF1tRo5RCxLqamwUECmnMZ0MqmDws-UOOWn-9ZBPhkecrq084KbXUcSas0w79D9fo01OBaLPxjWpBGEF6cuCECk29lt81pKWfBDq2vzjowbJ5c1pSiuj2yWPS4B1JqI5HbWkXqG8ispi8dBxC79UZ_FjTyWCVh9zesFX730XCtegA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
العربیه: صدای دو انفجار در نتیجه حملات موشکی حوثی‌‌ها به بندر المخا شنیده شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/684617" target="_blank">📅 00:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684616">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XACfZQS1ZhRQXD5_ACaYsF-QdlqB4Z6eZ1Zx5JgaOL-r42lA-vxevaM6vAv_Pjzg-SGToJa4sqarwpby8g3waTVdGQ31J2y8LTWOROFswNeDwm7Gq_kncIQ_gwlLL84e0Ng70AdM4M6zd_aIWtLRte5oiHDfByRCyDQ9gw5hN3DdqyZWAb-mWfw2TYMpF0q-wExmnOwyiguFDAFFlHHEIry0NBsiTIeQ5wlSnnPj-vmr0Htnbqxz3k79L1uCVA845AqdH1e3gqauT1-ilsZjFUNTYMLRgBm3kDvMwB0fM0drFZeSd0d45MXzy9AyfFkgEXyGbxMZqyATySVsfAVXIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از آبادان و خرمشهر تا سراسر ایران
طرح تاکسی‌های هوشمند دات‌وان با آغاز فعالیت در آبادان و خرمشهر وارد فاز اجرایی شده است؛ گامی در مسیر توسعه حمل‌ونقل حرفه‌ای، هوشمند و یکپارچه در کشور.
🔹
در چارچوب این برنامه، خرید بیش از ۴۵۰۰ دستگاه خودرو و مشارکت در طرح لیزینگ رانندگان برای توسعه ناوگان پیش‌بینی شده است.
🔹
تهران نیز یکی از مقاصد اصلی توسعه این ناوگان است و هدف‌گذاری برای توسعه ناوگان BYD تا سقف ۱۵۰ هزار دستگاه در تهران، بخش دیگری از برنامه توسعه حمل‌ونقل دات‌وان به شمار می‌رود.
مسیر از البرز آغاز شد و به آبادان و خرمشهر رسید؛
🔹
مقصد، توسعه حمل‌ونقل هوشمند در سراسر ایران.
@AkhbareFori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/684616" target="_blank">📅 00:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684615">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4985526d.mp4?token=Df_gawc2yIzRYBV3MMlrLlqgiOqMCpp6xsio7NlnRDIGw9xY14XF03ETHbd-6es4eaudA8X3maAJyjN4VXkEIOiLVgDoTsMNcyPzuMZTHXRuc4UTTYHgyffNi79rsF-sFR4E6JsS_VOU5ITA76lfv2Kepn3Upj2DXtOSPg9LrnW8k8GVL3q6QzvpYkz6AJWfCv8qfsMacBFA1ZZoDhpGb_MWA8uMQWTbfdKgpWosDMkE-YO7hoZBaRb3O2vOtvrjAuHP-uqBS0spoKa_7dkU_cwxmVcJBzW7wkGyljV92VLMQs4g5MeWk6SxjUqifL1Zo0yCCSIpd_nqwwL_919oBYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4985526d.mp4?token=Df_gawc2yIzRYBV3MMlrLlqgiOqMCpp6xsio7NlnRDIGw9xY14XF03ETHbd-6es4eaudA8X3maAJyjN4VXkEIOiLVgDoTsMNcyPzuMZTHXRuc4UTTYHgyffNi79rsF-sFR4E6JsS_VOU5ITA76lfv2Kepn3Upj2DXtOSPg9LrnW8k8GVL3q6QzvpYkz6AJWfCv8qfsMacBFA1ZZoDhpGb_MWA8uMQWTbfdKgpWosDMkE-YO7hoZBaRb3O2vOtvrjAuHP-uqBS0spoKa_7dkU_cwxmVcJBzW7wkGyljV92VLMQs4g5MeWk6SxjUqifL1Zo0yCCSIpd_nqwwL_919oBYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر فرهنگ: واگذاری نظارت بر پلتفرم‌ها به صداوسیما اشتباه بود و باید زودتر اصلاح شود
🔹
نهاد تولیدکننده، اگر تنظیم‌گر باشد، اختلال ایجاد می‌کند و این کار صداوسیما را زمین‌گیر کرده!
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/684615" target="_blank">📅 00:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684614">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3DMOc_4KuA6h0orScP7aWNktvjNPyIx7PUKjVDYwXy5extjTJ2g2NiHRLEx3-xvdzYcFRD6fvR6zAhDBMc5Q_8Vd9yDdq5TdyjB88h1B9EkZCFdXPkcpQsDeHVsSf_6drn1WFmVkjhGdUX3t7Ury3gLGnDBtnIPrKRUfovyuQvGZBdWyfQ5c0yRkeIE7L4YWwLbzQH7r6aDqqqA9PoNb5wFGkE7XJZ83R6Pl7JPy7YGYEHaOoqY58_1ZQEMd6iAR5P8oK6igfjCCoSrnrbWG6XU70mQBXHPYs59GVyM4jkf11WkuVfyNmj4otdK3ErCRGjYyfJKm-OOqTheZIgo2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/akhbarefori/684614" target="_blank">📅 00:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684613">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhQD7dSsi6qcsd0_5iS-j7fRthOjntNrFN7izV34sqQC726jNYqWj-27VXJsyEzXBvg7S5XUyq8hIP7I54Q9WnMvtX9uRSlBzztlsAcJiWcbn2fZs0D4RAo-HSsgVwG_elr7xOoArYVt_6zlPI9i7VYrspyb-bhB12IrdNYDWcavuAQzBJ7JkuoVrGrttAVMuXlXUdCEomKGbWZ4X3HrPTAW_wSUx0p50dIDLlB7scb5DTyRS_zf0RnsVFICrNq_t561TUueuTLCJSdmHl3vbjwURsGqzlaDS6lf2bfC2CBBCl2SKZ2RDitDNrFFzPOo-5Rie9g-s7GRjKrDM1OmgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عضو دفتر سیاسی انصارالله یمن: دشمن سعودی در کشور ما جای امنی برای مزدوران خود نخواهد یافت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/684613" target="_blank">📅 23:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684612">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b28b62c9.mp4?token=spDVuSMof3WRcL_c1uQp7IHsZPC3nCsYCbhEThjXhZfbgeMYbyOYf7_-WPoaGWpvt8iv6F35eOxoLxa1eZgoIlyrauokg_CInMUWpuL4TJc7N7Kh8aO2l5p163JpWZQEYucmnbfuFMvGJCEpOuEWzNB8e_QMszAuh7WeT6BOefHOkAM1CYvf4kZIGfqrEPiSaSaF34b4vvACSGERtjVBVF4j-bboZ-CoHCZv1-Qn-yT3413Sp_V4u1mlqI0ehcU2VaHrN8jt7X6UQxNTi1l-mCBudHY5G7xFO51rkRnv_ktrk_gXTXbmndXvzoxyxTLXuJDrL_hznz9zTvFFxCC5Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b28b62c9.mp4?token=spDVuSMof3WRcL_c1uQp7IHsZPC3nCsYCbhEThjXhZfbgeMYbyOYf7_-WPoaGWpvt8iv6F35eOxoLxa1eZgoIlyrauokg_CInMUWpuL4TJc7N7Kh8aO2l5p163JpWZQEYucmnbfuFMvGJCEpOuEWzNB8e_QMszAuh7WeT6BOefHOkAM1CYvf4kZIGfqrEPiSaSaF34b4vvACSGERtjVBVF4j-bboZ-CoHCZv1-Qn-yT3413Sp_V4u1mlqI0ehcU2VaHrN8jt7X6UQxNTi1l-mCBudHY5G7xFO51rkRnv_ktrk_gXTXbmndXvzoxyxTLXuJDrL_hznz9zTvFFxCC5Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل وحشتناک نپال
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/684612" target="_blank">📅 23:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684611">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
مروری بر اخبار جنگ و مذاکره در روز گذشته
👇
khabarfoori.com/fa/tiny/news-3240495
🔹
ماجرای دعوای علی کریمی و رضا پهلوی چیست؟ + تصاویر همه استوری‌ها
👇
khabarfoori.com/fa/tiny/news-3240618
🔹
پشت پرده تمام شدن زودهنگام بسته های اینترنتی چیست؟
👇
khabarfoori.com/fa/tiny/news-3240532
🔹
حمله بازیگر سرشناس به پژمان جمشیدی: مافیا او را وارد سینما و تلویزیون کرد/ یک شب به مهمانی رفت و بازیگر شد!
👇
khabarfoori.com/fa/tiny/news-3240738
🔹
حرف‌های جنجالی خانم نخست‌وزیر درباره بدنش |‌ از این قضاوت‌ها خسته شده‌ام
khabarfoori.com/fa/tiny/news-3240674
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/684611" target="_blank">📅 23:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684610">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
حمله موشکی یمن به مواضع ائتلاف سعودی در بندر المخا
🔹
منابع یمنی گزارش دادند که نیروهای مسلح این کشور چندین موشک بالستیک به سمت مواضع ائتلاف سعودی در بندر المخا در استان تعز شلیک کردند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/684610" target="_blank">📅 23:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684609">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
فایننشال تایمز: اگر فشار اقتصادی شکست بخورد آمریکا حمله نظامی می‌کند
ادعای فایننشال تایمز:
🔹
اگر کارزار اقتصادی واشنگتن نتیجه مورد انتظار دولت ترامپ را به همراه نداشته باشد، خطر متفاوتی شکل خواهد گرفت.
🔹
ترامپ ممکن است برای خروج از بن‌بست کنونی و به‌ویژه با نزدیک‌شدن انتخابات میان‌دوره‌ای نوامبر، بار دیگر گزینه تشدید نظامی علیه ایران را بررسی کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/684609" target="_blank">📅 23:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684608">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dL3dIpSJp3QNZrYWAlTkjFTQIoP-478TsGy-whSFT6yd60pCFzoYWUIemfoPw_KreNnFI2IrzRJSB3cZcIkAmhBzuVUeR0QN71WGoWywSj0bz91Ac9jsh06M0JQV9SdFn726gLZSH7AiHhAmm1q1IftCGyddNHhAX5pkQUDLxjuTDe5QbeVh9l-NgGNw6eFI0fcq_6NpC0xNNbj3j2oeJ8heGe8s_K7Wj6-4xYQfuW2mAmcphtB1m-3a98Goc2iFX6wANb1l5cc2ln7L9kQqelTHVB1xMsTd7Qj_bzTi8ukAczsnjRqx69Mc7URAQnPFkXWGzfD6P0zdHNRYtUjJmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: سیاست واشنگتن در قبال ایران به یک نمایش مضحک تمام‌عیار تبدیل شده است
🔹
واشنگتن به بحرین متوسل می‌شود؛ کشوری که عملاً هیچ مبادله اقتصادی معناداری با ایران ندارد، تا ثابت کند «ائتلاف» آن در حال کار است.
🔹
سپس مبادلات ورزشی و دانشگاهی ایران را «متوقف» می‌کند؛ مبادلاتی که سال‌هاست عملاً متوقف و بی‌رمق بوده‌اند.
🔹
تحریم‌شده‌ها را دوباره تحریم می‌کند و خلأ موجود را «ائتلاف» می‌نامد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/684608" target="_blank">📅 23:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684607">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
حمله موشکی یمن به مواضع ائتلاف سعودی در بندر المخا
🔹
منابع یمنی گزارش دادند که نیروهای مسلح این کشور چندین موشک بالستیک به سمت مواضع ائتلاف سعودی در بندر المخا در استان تعز شلیک کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/684607" target="_blank">📅 23:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684606">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d13f8cce4.mp4?token=sztF4hN1xhr2AslFiuCwPHWtiAJuEY4A_p8afwQ0KpvJtFzjoviB5IWioUTxxRyhGpDYd38aHZXdwgPlwvZbbU7UZ6aXG4uB-0w8OYA_waoPrEQwg44yCnl_etUNnUP76R7dcpvJ9S7QAJtlGXG1Z6bLiSPQtU3Tqza7ddPxrKyY7dVaxSvxleAQy0WGadDv3EwNt6XU8nQ2aZohER_f6-1iWXg4Q3HTEP7NEqtlASIg0uPNjTJsHNC1kZMtkDIOG5QZww-pRyJ1vXThqhBggcGOi8QUK36DUJHqT4ALVllSpwbsB6U13obja_CM8kNBljzJLHNZqSIvAxUaSd9OaFNZU1BXz4Hp0Yhw0qRMyICZPEq8oEKBjKBN0Mjh7fJoIPIP5b_lIfqhLynjOHom2eX6TgABl4jiyJA7Cd7LNIIw30Y9HvOeX-NJeoPeEXjVIVh4GpulaZOnjMpMB-DrqOo8oave7UhkM64jIcV9hQ4ADbzwXrM9ZdmHf80hAkip8bUArbDevo8RMdvM_IO4c3gAv9yhJWrmtBY-3PBjh7cDqSp2Sm-E55BMIJOtWKSRxSDmfW57WaoehXVCwNAOYaG4boItFiHE7ZtZmpqVRuwPhLrq8g04hct_kKfqpe2ngOyV0iSwxIOLg0im6vwPl37CREZG5Bbz5qLDvObUXD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d13f8cce4.mp4?token=sztF4hN1xhr2AslFiuCwPHWtiAJuEY4A_p8afwQ0KpvJtFzjoviB5IWioUTxxRyhGpDYd38aHZXdwgPlwvZbbU7UZ6aXG4uB-0w8OYA_waoPrEQwg44yCnl_etUNnUP76R7dcpvJ9S7QAJtlGXG1Z6bLiSPQtU3Tqza7ddPxrKyY7dVaxSvxleAQy0WGadDv3EwNt6XU8nQ2aZohER_f6-1iWXg4Q3HTEP7NEqtlASIg0uPNjTJsHNC1kZMtkDIOG5QZww-pRyJ1vXThqhBggcGOi8QUK36DUJHqT4ALVllSpwbsB6U13obja_CM8kNBljzJLHNZqSIvAxUaSd9OaFNZU1BXz4Hp0Yhw0qRMyICZPEq8oEKBjKBN0Mjh7fJoIPIP5b_lIfqhLynjOHom2eX6TgABl4jiyJA7Cd7LNIIw30Y9HvOeX-NJeoPeEXjVIVh4GpulaZOnjMpMB-DrqOo8oave7UhkM64jIcV9hQ4ADbzwXrM9ZdmHf80hAkip8bUArbDevo8RMdvM_IO4c3gAv9yhJWrmtBY-3PBjh7cDqSp2Sm-E55BMIJOtWKSRxSDmfW57WaoehXVCwNAOYaG4boItFiHE7ZtZmpqVRuwPhLrq8g04hct_kKfqpe2ngOyV0iSwxIOLg0im6vwPl37CREZG5Bbz5qLDvObUXD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوتبال در میانه ویرانه‌های غزه
🔹
کودکان غزه با نصب تیرک‌های چوبی و باقیمانده توپ پاره شده، در میانه ویرانه‌ها و روی شن‌ها فوتبال بازی می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/684606" target="_blank">📅 23:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684605">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eec58bffbc.mp4?token=IlrCrSr0e5_68wlQv6gFDIvH8vfk2qRDFPuWOiwzfl8teLB41iUkRjSkuglekNr5rBnJZexOvD5ubDyphfII6ktnaYmbz-J1NjRhKkog78pdNWC1RMhuxpqQQB6sSkg28WnE7eSwkO9Q0JQddi2c_0PkHkPWscwlnXzFoeUFKrDrl7uZZwgmRbIcyk07KMWfN-nImybPEtCTOF_H5XVKLSKuswDtL6XVFVlkDqa2q6rrzjSM0IWljmdorHV8AL_ZaOZOD5p-b7nvacCKYdWIbFbQkxh_5ld46I3EEibvg1BEPQ8tvxRFlzvysHKKIiWTH0-FLhUUpFV74W-EOv7L9ii3HPuMDRaXEhXs5DPpjT-F3Stc1wzPfK5bTystXgeo5i6vSN4SWDSFPUVBziTMdKDHrnz1UMMdvaKLtIUPi3R77Y5zcxG-XXfrFQh0gwbrzSU-FTiov0-6Gv-pFAO9SrGt2OWEtzABun3JNRjfE2b_myo_3HhOV74woe2ObiBWWzE25Mbn5u0ZgqLOqmIqRrlTIGTfA5bz_3MfB1teB_IM1MLhFKaJJEAanXSAAt_hfinrOoK9GZvBvfxzTb0IJZQbwL1oQ4UKui0kTiyys_zqm5nr0P1ixblAztm9cTN4kbdPuBcM2knyTOcBFvWiDi1e2dReYj91ICr6fBOeHQY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eec58bffbc.mp4?token=IlrCrSr0e5_68wlQv6gFDIvH8vfk2qRDFPuWOiwzfl8teLB41iUkRjSkuglekNr5rBnJZexOvD5ubDyphfII6ktnaYmbz-J1NjRhKkog78pdNWC1RMhuxpqQQB6sSkg28WnE7eSwkO9Q0JQddi2c_0PkHkPWscwlnXzFoeUFKrDrl7uZZwgmRbIcyk07KMWfN-nImybPEtCTOF_H5XVKLSKuswDtL6XVFVlkDqa2q6rrzjSM0IWljmdorHV8AL_ZaOZOD5p-b7nvacCKYdWIbFbQkxh_5ld46I3EEibvg1BEPQ8tvxRFlzvysHKKIiWTH0-FLhUUpFV74W-EOv7L9ii3HPuMDRaXEhXs5DPpjT-F3Stc1wzPfK5bTystXgeo5i6vSN4SWDSFPUVBziTMdKDHrnz1UMMdvaKLtIUPi3R77Y5zcxG-XXfrFQh0gwbrzSU-FTiov0-6Gv-pFAO9SrGt2OWEtzABun3JNRjfE2b_myo_3HhOV74woe2ObiBWWzE25Mbn5u0ZgqLOqmIqRrlTIGTfA5bz_3MfB1teB_IM1MLhFKaJJEAanXSAAt_hfinrOoK9GZvBvfxzTb0IJZQbwL1oQ4UKui0kTiyys_zqm5nr0P1ixblAztm9cTN4kbdPuBcM2knyTOcBFvWiDi1e2dReYj91ICr6fBOeHQY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر جنجالی از گردشگری با ضابطه؛ اینجا خبری از فرش و بساط شخصی نیست
🔹
تصاویری از یک پارک در کانادا؛ نمونه‌ای از گردشگری با رعایت قانون و احترام به طبیعت، بدون فرش، بساط شخصی و مزاحمت برای دیگران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/684605" target="_blank">📅 23:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684604">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
انگلیس با ذخیره‌سازی کنسرو و آب برای جنگ محتمل آماده می‌شود
🔹
بانک مرکزی: تورم مردادماه نسبت به تیرماه یک‌دهم درصد افزایش داشته و به ۳‌.۷ درصد رسیده است
🔹
بلومبرگ: مذاکرات اوکراین به بن‌بست رسیده است
🔹
منابع اماراتی از کاهش ۳۱ درصدی مسافران در فرودگاه دبی خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/684604" target="_blank">📅 23:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684603">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: قیمت داروها در کمتر از دو سال ۸ تا ۹ برابر شد
هاشم خنفری پورجعفری، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
افزایش قیمت داروها در کمتر از دو سال گذشته نگران‌کننده بوده و داروها ۸ تا ۹ برابر افزایش قیمت داشته‌اند.
🔹
هزینه دارو برای کسانی که با بیماری درگیر هستند به یک فشار جدی تبدیل شده و این موضوع یکی از اولویت‌های مجلس در حوزه نظارت و قانون‌گذاری است.
🔹
فشار معیشتی باعث شده خانواده‌ها در هزینه‌های خود اولویت‌بندی کنند.
@TV_Fori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/684603" target="_blank">📅 23:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684602">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
در پی انتشار ویدئوی نقشه ترور پسر رئیس‌جمهور امریکا، شبکه‌های خبری امریکا از جمله سی‌بی‌ان نیوز با انتشار فراخوانی از حامیان ترامپ خواستند برای محافظت از او دعا کنند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/684602" target="_blank">📅 23:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684601">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvdTBJqnrBJjD_vzsyKIwKsyz1VO4txHekMI9QMjOxdSMjRRsrs0tmYdVLcaGGBak4ty7T1yrF3w2UP_N58-37aqRv6ABJowY8EoTg5Z1hXIFQT5rATIk2mPyk3Z8pLv6o2CGrBbUlhlgli0EjvtFd-UB05Oqz00KXbPkqOmIMbJT2SBEmNUDWkG86J1fPLco166dV7U0p671W0TL0Nd_S_QNCOLEq2V_we5ojUvyNYf0AIp7oBOdub_zHHBrkis3MhyDhHOURfGaVYTLMBeLBzWIpgusj2AGcD4ha5shNQq9DcZIijXuWmLeq_kg2gSHtn8eRlu1EqEeMZuXNB06Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه بقائی به آمریکا: آمریکا ناو هواپیمابر یواس‌اس آبراهام لینکلن را برای نمایش قدرت به منطقه اعزام کرد
🔹
پس از ماه‌ها جنگ و بیش از ۲۰۰ روز بدون حتی یک بار پهلوگیری در بندر، این ناو اکنون برای استراحت و تجدید قوای خدمه (R&R) راهی تایلند است.
🔹
ماموریت: نمایش قدرت.
🔹
ماموریت فعلی: نمایش تعطیلات!
🔹
رئیس، خسته‌ام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/684601" target="_blank">📅 23:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684599">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ce508914.mp4?token=XJ9Q10H4gh9ImJR_q--XHffKt3bw7eUx-D7BNc7omdVZS86BZTZg01dlcp_cJJqS0wZ4RDgk5o3NiI9lDxjANrPveisJ6x_zrlMKakABE400n1e7iBM8P50iG4jh4HoCbXA0yjK4OiOkXFaQqUKVMMrLi4HSol3a5CE1n0sPgrlO9xinYD9HAu_OdmFLPad86daW4lIKdG-VX5_G2UZ3St_bNpD0S2kcY1nbCtUBSvtXmcyAoSv07H2HCpqEO1oI_HK6rO3isijVG_-8jNrqQDgTp5JMUeKyF8t4m-39FYr0ysPkjuQI2DXG4LcwuXkxVz5CuESTWEoYOZ8ugsPjHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ce508914.mp4?token=XJ9Q10H4gh9ImJR_q--XHffKt3bw7eUx-D7BNc7omdVZS86BZTZg01dlcp_cJJqS0wZ4RDgk5o3NiI9lDxjANrPveisJ6x_zrlMKakABE400n1e7iBM8P50iG4jh4HoCbXA0yjK4OiOkXFaQqUKVMMrLi4HSol3a5CE1n0sPgrlO9xinYD9HAu_OdmFLPad86daW4lIKdG-VX5_G2UZ3St_bNpD0S2kcY1nbCtUBSvtXmcyAoSv07H2HCpqEO1oI_HK6rO3isijVG_-8jNrqQDgTp5JMUeKyF8t4m-39FYr0ysPkjuQI2DXG4LcwuXkxVz5CuESTWEoYOZ8ugsPjHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
‏
تصاویر عجیب از سیل وحشتناک در منطقه مرزی چین و نپال
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/684599" target="_blank">📅 23:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684598">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a248c8d2f8.mp4?token=liIpdQrWjd0wubi0Ln5scHBumlTzxmlVsCW7qEgJYBaN-0UIcVQg10j9Xbs_bJQ8FKhV4E1URoBfts5SoYjCyvSYQPx0xvfAAd1je-HfKKaijMvh4zKieIgeyf6lZwfJXOUiG90dZuyhPJIgKcHycBV6xbY2RfUmt3aT74BGjtdKY5zNtSGP42MqRp8YilgN6vaz0Nv3ftiCpdy-2n4mR853hvnczaMvIc2hnbtuhgJNWJ2hqEGgjN1wDKfzPpOl-dbkuu1OIIqGR9nVgAY3JyqNCkugTHF8h5uSfLPF8RRJvc4F6ElI_Jdr3QYPAFzL-v4Ni41EAQT6kmf9WAsVVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a248c8d2f8.mp4?token=liIpdQrWjd0wubi0Ln5scHBumlTzxmlVsCW7qEgJYBaN-0UIcVQg10j9Xbs_bJQ8FKhV4E1URoBfts5SoYjCyvSYQPx0xvfAAd1je-HfKKaijMvh4zKieIgeyf6lZwfJXOUiG90dZuyhPJIgKcHycBV6xbY2RfUmt3aT74BGjtdKY5zNtSGP42MqRp8YilgN6vaz0Nv3ftiCpdy-2n4mR853hvnczaMvIc2hnbtuhgJNWJ2hqEGgjN1wDKfzPpOl-dbkuu1OIIqGR9nVgAY3JyqNCkugTHF8h5uSfLPF8RRJvc4F6ElI_Jdr3QYPAFzL-v4Ni41EAQT6kmf9WAsVVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آبادان و خرمشهر لایق بهترین ناوگان حمل‌ونقل هستند، توسعه دات‌وان ۸۰۰ شغل ایجاد می‌کند
🔹
مصطفی خانزادی، مدیرعامل سازمان منطقه آزاد اروند در
#گفتگو
با خبرفوری:
آبادان و خرمشهر با توجه به پیشینه توسعه‌یافتگی و همجواری با عراق، شایسته برخورداری از زیرساخت‌ها و ناوگان حمل‌ونقل مدرن هستند.
🔹
ورود ۱۰۰ تاکسی جدید دات‌وان (وابسته به گروه بابک زنجانی) ۲۵۰ شغل مستقیم ایجاد کرده و با احداث ۷ ایستگاه شارژ برقی، ظرفیت اشتغال‌زایی طرح به ۸۰۰ نفر می‌رسد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/684598" target="_blank">📅 23:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684597">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3456c18c13.mp4?token=Lx4U54KcSwRolrKKLgv2UXvp39QRFEoILbumZf_5mNwKccZbB80klv3-m6Qxm4BNxQ0sPd-D1p11Et45i5cpzYSCPad14EHbpYekey9jN8C733R0k0pT29BWfSoi4CCG8mdJ6QReqH2SX3wi0u6LyQ_FcQhWHJEHtK7Y1b29wa_nC2M_2jBu0Do0QcpXRTJzHGMzZadYj1KTYVtKQQVaVKq-clQf2hm6KdZryolvbAcFaArgvd0yhcyGCa2m_M-cDjLu5Q_rRmd918lg4WbxO9zOzIa49jfoKA2mchdecR3bkfUXc5uC8rR5Am57dZ19M14GK-wF1dGw1v-xm07fLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3456c18c13.mp4?token=Lx4U54KcSwRolrKKLgv2UXvp39QRFEoILbumZf_5mNwKccZbB80klv3-m6Qxm4BNxQ0sPd-D1p11Et45i5cpzYSCPad14EHbpYekey9jN8C733R0k0pT29BWfSoi4CCG8mdJ6QReqH2SX3wi0u6LyQ_FcQhWHJEHtK7Y1b29wa_nC2M_2jBu0Do0QcpXRTJzHGMzZadYj1KTYVtKQQVaVKq-clQf2hm6KdZryolvbAcFaArgvd0yhcyGCa2m_M-cDjLu5Q_rRmd918lg4WbxO9zOzIa49jfoKA2mchdecR3bkfUXc5uC8rR5Am57dZ19M14GK-wF1dGw1v-xm07fLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شهریور، خریدت با اسنپ‌پی BMW داره!
🚘
✨
از ۱ تا ۳۱ شهریور، با هر خرید از اسنپ‌پی، چه آنلاین، حضوری یا از شبکه‌های اجتماعی شانس برنده شدن
BMW 225L
بگیر تازه با انجام ماموریت‌ها می‌تونی شانست رو بیشتر کنی!
🔥
🎁
هر هفته به مدت ۵ هفته، ۵ برنده:
💻
مک‌بوک ایر M4 |
🪙
۵ گرم طلا |
📱
آیفون ۱۷ |
📲
گلکسی S25 FE |
🎮
PS5
با
اسنپ‌پی ۴ قسطه و تخفیف‌دار
خرید کن و شانس‌هات رو بیشتر کن.
😎
💙
https://l.snpy.ir/j5cfo
https://l.snpy.ir/j5cfo
https://l.snpy.ir/j5cfo</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/684597" target="_blank">📅 23:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684596">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4751d89143.mp4?token=XfOg9udSpQFVPfU2DvoO7UdrsZWy2umrVlA3Y3ulMv3Wp8f7KcpFxT-RWVv5t6IS4hylCz9iq8U5z4qGdjK5rP893j22cC7ttOrGHq5MP_7CCqR1KzapBqqlkI0hXPQF-5krOfZqscQ7qsiLOPiBXDZ7j6UJOKrFe7aG_i9tt2r1Nm4dq_jVsqjiRnqkJ5OEJShEJEj4AKSfiDYVqIbGq0kbycoH07Vv3rHLLe-3bQvmEBnbGHmnm141LlW320WFAW366wpRpPnAAj12Bi2rjbQCkvjnPYENi6U2HA55ELjxmukKe28mdP1WAfLSphqBzv4skjswzGY9QHEjsTWapg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4751d89143.mp4?token=XfOg9udSpQFVPfU2DvoO7UdrsZWy2umrVlA3Y3ulMv3Wp8f7KcpFxT-RWVv5t6IS4hylCz9iq8U5z4qGdjK5rP893j22cC7ttOrGHq5MP_7CCqR1KzapBqqlkI0hXPQF-5krOfZqscQ7qsiLOPiBXDZ7j6UJOKrFe7aG_i9tt2r1Nm4dq_jVsqjiRnqkJ5OEJShEJEj4AKSfiDYVqIbGq0kbycoH07Vv3rHLLe-3bQvmEBnbGHmnm141LlW320WFAW366wpRpPnAAj12Bi2rjbQCkvjnPYENi6U2HA55ELjxmukKe28mdP1WAfLSphqBzv4skjswzGY9QHEjsTWapg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فناوری عجیب نیروهای ویژه چین
🔹
نیروهای ویژه چینی از یک «پرنده» برای شناسایی هدف خود استفاده می‌کنند.
🔹
فناوری، جنگ را دگرگون کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/684596" target="_blank">📅 22:51 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684595">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dmy2jfuzpGaoPKe11T8Ergog7nY9x0u8xtyYGWHUpxGaaduh7Nc59ZKkmlxs5IlsXbPYA5A4SqgwvXXupI4K8AXVzEhF_33DBfyRMpWBNYFDOCMsJFCIRsbifWt_LAy_PW0-nXb73WTXPZnvVQBwvBXnvcaEQIedsTKAx-J3nMar-pCOXiVyrf7cdSfApWwGnQQMGjZMHUFORG3tdRGkVfJsXhnSFYZ7pHOcKyQIgMzf3o5KO0NEphzJVMUfeYH2wzfetjNA5u0XlsNKUBJs04C9XxqLInWuvGxt2mOVJ-jpyPv8-hEwkNhOLKJ-f9kjULzHjq0xGBIsoN1wWfLPeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمسخر ترامپ توسط فارین پالیسی: دانلد داک در اقناع افکار عمومی از ترامپ موفق‌تر بود!
نویسنده مقاله با اشاره به نقش شخصیت کارتونی دانلد داک در جهت‌دهی افکار عمومی آمریکایی در جریان جنگ جهانی دوم نوشت:
🔹
ترامپ درس‌های زیادی را باید از دانلد داک پیش از ورود به یک جنگ یاد بگیرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/684595" target="_blank">📅 22:48 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684588">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NnKfQQ9YuBdhpK_Mpm0tZTLO32LzMuJQ0iJN2UVt-PJYQxYdeGVO4bsyBQTDDxzh9mmiYLa-IobJlw3KcTOLVpXlhbtWVKQlQjqxbF2y1NHdU7vwr43Lk3wSChgqA2sN1w4e7hKZmS1xdJ5fidfExaLKTE1rYBq60hqTpgQQctPA222R5VSairXOx6bB_U5Um8XaUhDvfnNVsNrSMPY6e-hC9_xw1SDfVyf0MDbGQTjeQwPBwkLsbFQVvumrWCFX_wkS5RJlpWBBfXl19f_O9tvnowY9idrJ1tUHxTYoozLQSutMnrbKXGeoSUSjBBJZe-xnB-z9bRujyhn5J00-4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AjjdjFt2qxn7iQ4_PLebbfL7TwurR4cbwg50tCnjrQq1_kAL7kwRASPyaCDazCPxt3ZqGuASpKwQp5h8fvGn9-MfuQCDyqddAlpwaYPlIqe-k8r6VjvuYO8qQq1RJWUjjbNQLr2LA8neREznhwCZ9do3gdOyekW5zGvHHL1RpFzn7bptYU_cBIFCynwXBtJFeXE4DNslp9Pu7v8uPh_35-T5n3vbHA4d2Yty5OBXIt6PfR-K6HpUHpOF7DqMKa81x9IkRsN2Jq2wI670-3BZfktBL8bjcJEVpTbi7dALZM7sAZkBthg6y6iPFVrK21twp_sZnVml6YWZjIkrobrMaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kT5pb0a2TbOYJKBjStTOJc0n-XlSDHFYsVb0RGCaIJrVWSaUcu4zXw6v_pHOck6P5Lkz0r_7t78p5lhr9IrEB7SJs0aJN8wbGPC24UDo9lfPnXP8W3WMydD76-pykp1iUZZBnZ2tVlS3ITnYD6omGe5U2HH0COjlBTYsntRnrYnXs_ZNeRfiGAyLasbJatoaLoUa0vBO0RtTgNHyFak60zEtM2cImqZnOTa7QyemgT-X8CQhaPqNG0GIOWueXNAPlLpanKAHesLxPGFxsEyJxjyyqkRvw5vTJCYRgtAlNFp_PqknzT_yWHwWRRewXsLhsUqutizovSFy3vBRy7uJCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tPzPfAAZUGiLpAzLR2syTalM9DAublR7-mWGNWqkOGlJF4P3JKWPmrGkKD0wQCV6pprLx2OlppVRWFDBuFWjFXH5LF_Z0TWA6NQz8T8eaqR0vxPc3c_lM873VrlAEvn0ao99IyZGehKfYDGoi7n3s42-UniO9yAroj19aUxj0jcFsGMAmYz3iydIjDCqF2n6eiTobRcA_IOfCuxOfpV_QFT6FfeabFOhTfPTa8ZcE5PPLSisEC1plhQX-IfKhao3aKf5qGcUak7G2Xd7eD_Tpzvo8H8NkQWBgJi8e7Sb6PqSjNEXtFrwmKsMQGN9qFVMsOqKTKP_eszZbkn6sPVcjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KYZE1NREyw7Avulhav3mTII0_xd3ZTCDboHavkNBZ9wGXXBer_NenIBhji7SK6VYKv5V7f8pGbrIlH--ZMq3HeqojraWOf1MbWw7cRbBtfHMSpAwufv0BP4nncNlA3DUJ5JFy42ogRCcdMPBl1LnyFYRI3rF4vnZBFqW2kshXN1NSNVE2FNWkE0twpbmTvMFerkb0uAtEOdYY-1_Rarj6X_73_byqrbBJ9fKDWERnZ6JgybDj9UiaV_E0xH0eqGf0mE7gT2okmOCi4TOCVgCBGBIb_rLOljztrk8n5u4b_g3LmKO9gyG5AU7p3sBIf1gyhj-RMCdZOkv301h16oyHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E6BWmCvsK1GIbdkfYHGGVDuAVHf9cTRKgjzQkjI9YlzCRbYuZxp3L4_wH9upX6BXBV0-WAg5eGlZ0P4buX4FmTf72Yr4XL3cZ9EbWb_FzuuMGE-0wKD-oEJi7HSd1Q2FZSJLpkT4_UZuvA0a12Gb33XbrVw3-CqvXaVcsuxopWa2MwGTjydnM44I2rFdPtQi5UnJGEmjQoz2lr-1V3lezaE2yjMspTUTU9poz-SZtsOydeLGZSH2oclzYCOymq7V-KjlZsR2j9zhjcxSXTUd2bhtCLxaTGeI414HkSxVYIhnUIrcVCRkJsXkdUrxe1b8zfpiG_d2wjIsiAdiT-xb8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jeBYT6NygS72hZJVkar70CWHHmwPzdASbbsfjSjxm_agYTsR-6B-42OQwS7zZtZokVpuX0LK1pHJon7oqFsFCzuziN6obqa4WBLmjCB4YPu4SWP-WhMepCA_-9A38MH3_tA1yHimQZ20Yh8ODPm_b6YO5uf97si28SiyIU9P2ZR_GzBRPDNjJpKluC0gGMbDtSB_LQVeriKFQAjC7Jl8EHXSzEoejuuiX4Xq9qZK1G7Y0IeZMB_MTyXZMazF4zDU5wzbJcxv2DGpp5Ujmn9L3ktNpNTb4JpSR129qTIERRlWoqktWuQeq1gSa2Fx0ZKHwg1oXdXwjafeVC7IW94TaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت برکتِ حضور
💫
✨
برکتِ هر نذر، به حضور دل‌هایی‌ست که بی‌منت کنار هم می‌ایستند.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با نذر و قربانی و توزیع گوشت قربانی، در مسیر حمایت از خانواده‌های کم برخوردار و خانواده‌های حائز صلاحیت این همراهی را معنا می‌بخشد.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/684588" target="_blank">📅 22:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684587">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86a139c06a.mp4?token=Ee1RtB2UhDJY59Ot3fiRbx5z7HcB5q2e0vaUwYX2ZyDD41lb02Dh8SsFur86Htp8BepJRwCZiL9520wf3_RiikfTHZ3WE0DdxS6WiTigtuKqIVgQcstWbBk-ebLAZeFhdv52dJvOBsMSNSMv91xP0J7YnqJ-wNVFBb4UIiGdYsQSgDEs4d_FOwh7N_o3vn5BTkE1zp_RcQt8BmTA98I-hcJXithuZKrkVG5QnSuB3ca2Od2w4G9rBiPUVyA1p8bATTHWhPOkm-CHZ5g-1okSs9g1pJykE9a8Pm2v4Nqc4C7Qxt--NCyNgyAyug_45n5NwGs6q6OQAyMcWzYWfXq_KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86a139c06a.mp4?token=Ee1RtB2UhDJY59Ot3fiRbx5z7HcB5q2e0vaUwYX2ZyDD41lb02Dh8SsFur86Htp8BepJRwCZiL9520wf3_RiikfTHZ3WE0DdxS6WiTigtuKqIVgQcstWbBk-ebLAZeFhdv52dJvOBsMSNSMv91xP0J7YnqJ-wNVFBb4UIiGdYsQSgDEs4d_FOwh7N_o3vn5BTkE1zp_RcQt8BmTA98I-hcJXithuZKrkVG5QnSuB3ca2Od2w4G9rBiPUVyA1p8bATTHWhPOkm-CHZ5g-1okSs9g1pJykE9a8Pm2v4Nqc4C7Qxt--NCyNgyAyug_45n5NwGs6q6OQAyMcWzYWfXq_KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گفتگوی سخنگوی دولت با بازمانده حمله به مدرسه میناب: همه دنبال انتقام هستیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/684587" target="_blank">📅 22:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684586">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
شوک جنگ ایران به دبی؛ ۸۰ درصد رزروها در یک ماه لغو شد
🔹
بررسی‌ها نشان می‌دهد در تنها ۳۰ روز نخست درگیری‌ها، بیش از ۲۲۶ هزار و ۵۰۰ رزرو اقامت کوتاه‌مدت در دبی لغو شده است. این رقم معادل ۸۰ درصد کل رزروهای ثبت‌شده در این شهر است.
🔹
این در حالی است که فرودگاه بین‌المللی دبی در سال گذشته بیش از ۹۵ میلیون مسافر را جابه‌جا کرده و صنعت گردشگری سهمی بیش از ۱۲ درصدی در اقتصاد امارات داشته است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/684586" target="_blank">📅 22:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684584">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پیشنهاد پاکستان به ایران در سفر عاصم منیر
علی احمدی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
هدف از سفر فرمانده ارتش پاکستان به ایران، پیگیری توافقنامه قبلی ایران و آمریکا و همچنین پیگیری قرارداد نظامی مکه و پیشنهاد عضویت ایران در این قرارداد بود، پاکستان همچنین برای بازگرداندن ایران به میز مذاکره رایزنی کرده است.
🔹
ایران پس از بررسی شرایط درباره عضویت در این قرارداد تصمیم‌گیری خواهد کرد و بازگشت به میز مذاکره نیز منوط به پذیرش شروطی است که قبلاً از سوی تهران تعیین شده است.
@TV_Fori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/684584" target="_blank">📅 22:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684583">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juWG3qC1ii1NNKRGDyy94KU-G0P6pAbFkaZYLwhp0RqLf4VUWun20auoqBx6aiIMy3y3jUAen6v2IrUMJ0MCzJYMHjHs_kS5Lal8dbmhUF96gqiSs2bkc1I1fovOANZXgVghqZXfHPVscXOBWUUqzotblvuQA67pt6LfVvssC3P2phA6kVNNCiIB8iVa6fQUGRs5meSqERE1xk5NvDdS2uZVrY0HAnFVpDrL5RWvnBumyU6uTSb85T4yjmpuu0rJTAOOjVvNp3w8avehyDwHyju6a8d9h326Zo74WvoEW8Z9DF8P8dcDlp3iai2n7YpjQCKqYmWn3ETl0TGo4WVhPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت
سفارت ایران در جواب گزافه گویی ترامپ متوهم: ماموریت انجام شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/684583" target="_blank">📅 22:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684580">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JfPKliZXd-3ZFcIEtyfE3Hz9QChUGBf3iwqIlagpn3ViC7GKv4tVp208ec_TO-BMfSiSBsB2x8MEp58vBBzB-oOW2ZRC7VawEEoLQpeLiOmLTIPMn3s_qJmMz2XBkxnoU0jm083yRX91kD79T5ak7gzUzUGmtBzsCfny6qSSev3ztDC1M7yULefPbZbo9yhr06t3oYHNam0j-zDjdZHLe42HEqiVZmuB1dbpZo7dsQm6DzsnBHcZu0cqAylfjNyv2FRqwA8Y9-Oh3W0KJd-iF3qfUoZ5S7cndRdIryEVA1q7OLDOmr5nKDEi4VcAjbsxecgaR5ASwdnB2wZv6Asv8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L9OZK5bSYVvCeLuS-nF8VOdr4BVUQXHeJWnGKxvYn2LyJqcVCseZECNI2-iEmiRHxnyBCuE_wHM3TU26J38poNPXbP28C3XhyUSPqnk5EsrmVuu1Sf-qpybzi15HBUUN328K4Qlhr4mXwfwU09qPXetL7z0whTFoFy7IZwb4FhU_u14KrthNiM9o_Aj2DQ7kwvyuXwt8xXFLTuz8NgPsP5BNfhZYWjppBcJBqhkM5RORLQ5kyM3RabMRfAfNR9Mzj_5FWM5nrV2QTnwQ6GGraa57-5PVfpCqNLIlnv3lXcWR6zT3d2KdANhyoTKUKyQ4IxarYqH-iu7FTmVFw-IRuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
از رزین تا درآمد؛ سینی‌های دست‌ساز، یک ایده برای کسب‌وکار خانگی
🔹
این بار در #چرخ_زندگی سراغ ساخت سینی‌های رزینی رفتیم؛ محصولاتی کاربردی و دکوراتیو که با طراحی‌های متنوع می‌توانند به یک محصول قابل فروش تبدیل شوند.
🔹
اگر به کارهای هنری و تولید محصولات دست‌ساز…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/684580" target="_blank">📅 22:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684579">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPM355BzcUqNCqWF4izRC3pJMjrnlDRPufJEhWQRFiqSzT7p2MfjQkEoh_m6GqNbBY4NJdRJEl2_qbaYq2_nxOYHmLik959g31YQxtWUhjcv2NZbntT7_6bQLh_4unX8RT0yrr-7gbTlPYNXlSzI-qHWklq4LQeapwPQGm8j3mWi81YzOkUCY_9NKBYkdPV4Aq0BOt2i2GAB9HMmKKYw3-Sv-C7LuAjhHrfHMvZKzF0RdVqCNcl50n4uyBeG6b8y5awRpduiMEvN5TEmxmgbcGqKFKg3SWtbx4ldljjxwLD78pkPYpsQLevCywKXtmyK-ivK1qVeLqFV8XEah-VLfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیشنهاد جالب درباره بازگشایی تنگه هرمز در ازای انتشار کامل پرونده اپستین
توییتر خبرفوری را دنبال کنید
👇🏻
https://x.com/Akhbare_Fori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/684579" target="_blank">📅 22:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684578">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
بقائی: سفر نخست‌وزیر قطر به تهران در چارچوب رایزنی‌های مستمر ایران_قطر برای گسترش روابط دوجانبه و تقویت صلح و امنیت منطقه صورت می‌گیرد
🔹
سخنگوی وزارت امور خارجه از سفر شیخ محمد بن عبدالرحمن بن جاسم آل ثانی، نخست‌وزیر و وزیر امور خارجه قطر، به تهران در روز پنج‌شنبه خبر داد و گفت: این سفر در چارچوب رایزنی‌های مستمر ایران- قطر برای گسترش روابط دوجانبه و تقویت صلح و امنیت منطقه صورت می‌گیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/684578" target="_blank">📅 22:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684577">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f939603214.mp4?token=VX5PAKyCsQBUZ0YjbtcDeT3bgSiFu8DbujmKGI4xPRBfL8GrRHnKPmUI5Lj4cQk1rlkFVyJ_PTlBeRDcbRZisSIpBmSI4uIjWztremnlUvzzsVELbQnI1QEarFC4akOeO_3WuaDWM52ti6ixmxADuZdHk89yUqd_s-VFE43N71DJ64XCRW_lhbj46Ys4ZsUHemWwPUZXkyLAam9YdlZJQrv6Zz3K69DtdELH_4kP2vg_vXxBdbn3uz3k4NI6IbtItqTR2mk34zLIKwZpwDN923cGe5PHPe3W_UdTJQL2CmjcKl7bUDdfkCObJPs9GyV77_MK7e9-W0APRLKKQHz2QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f939603214.mp4?token=VX5PAKyCsQBUZ0YjbtcDeT3bgSiFu8DbujmKGI4xPRBfL8GrRHnKPmUI5Lj4cQk1rlkFVyJ_PTlBeRDcbRZisSIpBmSI4uIjWztremnlUvzzsVELbQnI1QEarFC4akOeO_3WuaDWM52ti6ixmxADuZdHk89yUqd_s-VFE43N71DJ64XCRW_lhbj46Ys4ZsUHemWwPUZXkyLAam9YdlZJQrv6Zz3K69DtdELH_4kP2vg_vXxBdbn3uz3k4NI6IbtItqTR2mk34zLIKwZpwDN923cGe5PHPe3W_UdTJQL2CmjcKl7bUDdfkCObJPs9GyV77_MK7e9-W0APRLKKQHz2QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصلاح صورت و خون روی آینه
🔹
همه‌چیز از یک اصلاح ساده شروع می‌شود؛ یک تیغ، یک آینه اما چند ثانیه بعد در لحظه‌ای که همه‌چیز ترسناک‌تر به نظر می‌رسد، واقعیت خودش را نشان می‌دهد... #کابوس_ترامپ
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/684577" target="_blank">📅 22:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684576">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjRCsRSZqeFrP4sxwnPqUWIvnUKpHxGFV7A16FaZJikW3mktDgo7nZfRGtON6lxx-EkNAvOHZ-CoDd9Dw9OTGqQZha-O-xAjkiAOZWB-Mn3TnZXJ6lkMci3eaVgNGK9HTJKJO3FeCM8J2zs5b5qJnwBjGy9i76k8DGhGMDaR2ULBY06BVSO-b-tEPLnDyrtP2tsQsyigCAxfVIW-1sl_gOpBW6lLWdFYYOyR5vJkEF2zWxVsZEUPFk2N_ayXRIElvJVM3lk1xgXKE8eNt3sp_yiR7kKRMosd3VZc0rYQ9W08RomvuanDmOaMxEUG0x1Vq4Bec2cA1g3RlKTyfDgtsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گاهی چیزی که برای ما شکست به نظر می‌رسد، در حقیقت خیری پنهان در خود دارد
🔹
امام علی(ع) در نهج‌البلاغه می‌فرماید: «بدیِ توشه‌ات، نزد خدا بهتر از خوبیِ خودپسندی است.» شاید آنچه مطابق میل ما پیش نمی‌رود، راهی برای دور شدن از غرور و نزدیک‌تر شدن به خیر واقعی…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/684576" target="_blank">📅 22:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684573">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLXKQxcmHLiO-ah1vrr0g1uRIZaoo_97DYcfCCOgbsA7t6oY5uDAMNDS40J1YoGP7n3m31j9Fj_qiqGqvcMaZygmGiCIGnns2HvNFuBo_Xk7dwtRFlhQeMkkW5Ytduetu-fqYz4cNTWxUSsFf-z3LEVTZH8lI42qThr2jAkl4FGWhDW7cQw38wXA4oYlsROGoAPVi3JWbyrElro8B53QytXe1fShHClHJEtPwnV6iRSp7QGCMq9bga57CMXBNqn5v5KFxETxRdZtvGjwNCtAiSEwYHjd_sual1PxPgBuktqAaZizI0eEsPky5xv-7ChsYrxstV6y1iSY6_cAnoedmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از البرز تا اروند
🔹
دات‌وان تریپ با آغاز رسمی فعالیت ناوگان حمل‌ونقل هوشمند خود در آبادان و خرمشهر، سومین ایستگاه فعالیتش پس از البرز و اصفهان را در جنوب ایران رقم زد؛ حرکتی که در ادامه توسعه این ناوگان در استان‌های مختلف ایران انجام شده و حالا با ورود به آبادان و خرمشهر، دامنه جغرافیایی فعالیت دات‌وان تریپ گسترده‌تر شده است؛ مسیری که می‌تواند نشانه‌ای از تلاش این مجموعه برای شکل‌دهی به یک شبکه حمل‌ونقل هوشمند در مقیاس ملی باشد.
ویژه نامه خبرفوری
@TV_Fori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/684573" target="_blank">📅 21:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684572">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ادعای
وزیر انرژی آمریکا: ما می‌خواهیم از طریق مذاکره و بازرسی‌های آژانس بین‌المللی انرژی اتمی به برنامه هسته‌ای ایران پایان دهیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/684572" target="_blank">📅 21:51 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684570">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8474597568.mp4?token=M2kNhidx-CO-kGy1CJiJKn6KrXoxN0aDFuEBHkh-Eyx2KpmSYbLLMPo6WxuvctX0Tx0uhsYud6kFYRyvwaqB7ySjunUuPkOS-d0YS52Erfj32efAhKPbWOn4pN2y2eVyNI-8R8ouEsHxH8EgO0C1xcp0sPG5tdNZU4p12oOpJeWFZ2ArQyu23zRRzsxPms96h49fPzfx_OMWljft6cAPuyjlKHX8hQZ8vv0biu65AslDSSBZIdjBAjUxsBgRWVqptxMZFwhpqYNR_8AiyIAFGmsSib0C9c7fZFWrN6lX3RCgt-M8y2-I-TA_mVqA507JoQNNjixCFCUljgHtRxUa3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8474597568.mp4?token=M2kNhidx-CO-kGy1CJiJKn6KrXoxN0aDFuEBHkh-Eyx2KpmSYbLLMPo6WxuvctX0Tx0uhsYud6kFYRyvwaqB7ySjunUuPkOS-d0YS52Erfj32efAhKPbWOn4pN2y2eVyNI-8R8ouEsHxH8EgO0C1xcp0sPG5tdNZU4p12oOpJeWFZ2ArQyu23zRRzsxPms96h49fPzfx_OMWljft6cAPuyjlKHX8hQZ8vv0biu65AslDSSBZIdjBAjUxsBgRWVqptxMZFwhpqYNR_8AiyIAFGmsSib0C9c7fZFWrN6lX3RCgt-M8y2-I-TA_mVqA507JoQNNjixCFCUljgHtRxUa3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان انرژی هسته‌ای: ایران به دانش گداخت هسته‌ای برای انرژی پایدار دست پیدا کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/684570" target="_blank">📅 21:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684569">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzxalxI9keBu6qPzxF1RCXPCANroCwdhZBu9Cj8q5RHJDO-kCzWqaxyMnmjvD2PceNIDFdVuCmBYJnKclKudc6xChAFoHR0WHWLCBDzZgX9jSKQwLpB11nm-MbXc5b_0IEctmccXzAUlSgYEMT3O7vE2L-Y-IBINbLBpBb0MGn-ss2HQb_Lw3TM_fkK_o5CC-loYzGpOw4v_4RGtaU8CeVJDbCpcnlCAkSdwoHGkLFFuo8N4_5MrnmzGQEyrHTlfNP4bGopZbljK_GhZGwEBv-FbgLToC_ORTD47HBY0qpZipHnxt6pTylHqu5NNIa_-uU83Q6wkBNEzn-irdMW1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: ما از بیانیه اصولی چین در رد تحریم‌های غیرقانونی علیه ایران استقبال می‌کنیم
🔹
مشارکت استراتژیک جامع ایران و چین ریشه در احترام متقابل، همکاری برد-برد و چشم‌انداز مشترک برای جهانی چندقطبی دارد.
🔹
این رابطه نیازی به اجازه هیچ‌کس ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/684569" target="_blank">📅 21:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684568">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
معاون اجرایی رئیس‌جمهور: توزیع بنزین در کشور عادلانه نیست
قائم‌پناه:
🔹
طبیعی است باید تغییراتی در نرخ حامل‌های انرژی انجام شود اما میزان و زمان آن را باید در گفت‌وگو با دست‌اندرکاران تعیین کرد.
🔹
توزیع بنزین در کشور عادلانه نیست؛ فردی که چندین خودرو دارد از یارانه استفاده می‌کند و افرادی هم که خودرو ندارند از این موضوع بهره نمی‌برند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/684568" target="_blank">📅 21:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684567">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ادعای
جان مرشایمر استاد علوم سیاسی آمریکایی: ایران به امارات پیام داده است با آمریکا همکاری کنید شما را به خاک سیاه می نشانیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/684567" target="_blank">📅 21:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684566">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/684566" target="_blank">📅 21:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684564">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pvn4xV4n9MalpZ_tTZYX38JVCiytyL5HmkKuPR9swNIm1x7XUSGqxIjKibKKTyjbfGzV7cJcb1JXxckoR77m4mECKtMQGH8aky2WYTdGnOT2WBiP7v3em9MFbWcaK8LDgHHaDpbcCJ6u0aCU1urvZQwdQC2BYphZn4JbxwYLuC9fPg9qgWtZDte7klXkRsADtlq_n0vtM0hPRCyKiNUcgUIufSEs9fZZXkiM1ZCPZ7D5UVRdi3T86R0yCWxDZSDlTSQ78eNaUTMDQrN3B0wxeZ99kbkFcas0MMan4X46sQeFSAGiU-Sg37SxbzFbmj_Lyo_8-iuhcBBnjYTY_bhPVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WbC_MADNvU2QvFViQKfsgG2WWPQBZZIrZ1PMFApPymyAQH73JtDkPLImg2P-ujWm556KsaiPkHIgw6uzQltM7fPWpSD2RcBJG5DttovjFWiIK-YH8A1Ds4tr1JcQdOk8aI8dfx2cleSHnKPPY90aLwxFw-E1-10A3n98bVfbg7r4fKwvkjyl4qR0IP3vFTrUsrGtXpy312GkeZBPdLAd90oMXCh3wu0b6xwcIOnlD3lDVT3V67F6K7WnO26sq1ERH8U3z7ayaLSW6J-6UBxxXpmoDjpcppDJEhOvv4LaKJS_gZKPXGxSfu-IaAybR9qC78v9NHyY-90zPWISlHDMNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سفر ۳ هزار کیلومتری با گیوتین؛ بازداشت شهروند معترض آمریکایی در نزدیکی کنگره
🔹
پلیس کنگره آمریکا مردی ۳۵ ساله اهل کالیفرنیا را که یک دستگاه «گیوتین» واقعی را در پشت وانت خود قرار داده و پس از طی کردن سراسر خاک آمریکا، آن را در نزدیکی ساختمان کنگره در واشنگتن پارک کرده بود، بازداشت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/684564" target="_blank">📅 21:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684560">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3sE8Pus2PD5IKElanlshzJ81EcFMhhASsf1nyWfx-uBTUSEX-5ShAnjQKFjh0fkMJCEmIol42E2BABVQbHR3mx9P65j_6Zf0DaVnkw1StWC1i__2LGq311nahA7OVdvlZn3rLfqjIuOe5m4Nox2yxpL5rtUN-GxsBjaCfVSXBTrBeyFSaBgoVd2k3NmoRhCqOc9t77p-OF-7YjE1VZoFVIVq0y0BNlTWE4dN9MfVeansWMPnl1mXiRa9N6G-KzF0d0OYKZKcqYxhEvwKnOQeNEzV_GqZDangFy9-XegAZFvDjZMbKd-PbpcQ_We6Xih6datnuuCZsrqFCbfftvrFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگر ایده‌ای دارید، اما توضیح دادنش به هوش‌مصنوعی با متن سخته با ابزارِ Squig می‌تونید خیلی سریع یک طرح اولیه از ایده‌تون بکشید و همون رو به هوش مصنوعی بدید تا بهتر متوجه منظور شما بشه  #هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/684560" target="_blank">📅 21:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684559">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aee581b45.mp4?token=NemLjInteKP7VMRd7p3A6WFt-MfVjPmrIBV5nM1b-P7fBU_AwMPb7zitk8FwYBMF9gTgEvykE6G4dTnb3cqqVOLdS7SIW2H-4O3gaXn3sSKLKrIYjt5omPzp8p9ieaYDb-qcTfLCl81Bsp5P65vDjenZ6JCfvS5yD5-XjA3UbS8LXjZ3NheiY-tY-buhizndfaOD6ZIxByIgOCH3767fNDAX3lGG1l93M-JDgieINhYSTBYgnCXRfZhYUpzvEWxe6vtnthyVSvQ795mpo30gxYOLKxvhwTTQ8BVfUrYb5wtnl4sP2qfP-3rPPmAAqB9LMseL5tCc1ve-xjrGh_gWpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aee581b45.mp4?token=NemLjInteKP7VMRd7p3A6WFt-MfVjPmrIBV5nM1b-P7fBU_AwMPb7zitk8FwYBMF9gTgEvykE6G4dTnb3cqqVOLdS7SIW2H-4O3gaXn3sSKLKrIYjt5omPzp8p9ieaYDb-qcTfLCl81Bsp5P65vDjenZ6JCfvS5yD5-XjA3UbS8LXjZ3NheiY-tY-buhizndfaOD6ZIxByIgOCH3767fNDAX3lGG1l93M-JDgieINhYSTBYgnCXRfZhYUpzvEWxe6vtnthyVSvQ795mpo30gxYOLKxvhwTTQ8BVfUrYb5wtnl4sP2qfP-3rPPmAAqB9LMseL5tCc1ve-xjrGh_gWpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
تولید و پخش پلاستیک آریا
🚨
🚨
به‌دنبال تأمین‌کننده‌ای مطمئن با قیمت رقابتی هستید؟
پخش پلاستیک آریا، عرضه‌کننده عمده انواع محصولات پلاستیکی، ظروف یکبارمصرف، لوازم بسته‌بندی و اقلام پرمصرف بازار با تنوع بالا.
📍
تهران، خاوران، جاده امام رضا، ورودی فرون‌آباد سوم، مجتمع پلاستیک پایتخت، پلاستیک آریا (کیانی)
📦
فروش و همکاری به‌صورت عمده
🚛
ارسال به سراسر ایران
📞
مشاوره و ثبت سفارش حضوری، تلفنی و آنلاین
☎️
09129628810
☎️
09129680633
☎️
09128063394
📲
جهت مشاهده محصولات و ثبت سفارش
به اپلیکیشن های ذیل مراجعه فرمایید.
لینک کانال روبیکا
👇
🆔
@pakhshariyaa
لینک کانال تلگرام
👇
🆔
https://t.me/pakhshariya1
لینک پیج اینستاگرام
👇
🆔
https://instagram.com/pakhshariyaa/</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/684559" target="_blank">📅 21:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684558">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THMqNsh5FryELkDapnN08Q0s52pyyfhNeLXSt86qIaJu4y_Ghbh1RG5l7u3w7ZITylYRaylNUporHHLgV5zGnVWM_1m3OcXwitMvxzA9xLyVe7cJXLwmUeqJEg5R3ivqHR-YPMGpE7xDZDqAZiRBgHoeTgHtHmOJeZo17RfIc_QPmO_3wT7yArpCSQy1JnqzIj-vKN1EvZP6ddbrdjxClrc9OXXqWB7l8Mh7_LDpa3OG_K0qImdnmuW9vUIOJj2myyCY3tABHsTJiwMKkfCHJ3_ApcL28L9x1LS-5lNUV8JHL0-bA51lPqS9Rf6ZCTYbtDjvXyusZTNZHSoqEbeoRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بخشودگی ۱۰۰٪ جریمه بیمه شخص ثالث!
📢
طبق اعلام بیمه مرکزی،
از ۲ تا ۱۳ شهریور ۱۴۰۵
✅
تمام جرایم دیرکرد وسایل نقلیه فاقد بیمه،
به‌طور کامل بخشیده
می‌شود!
فقط کافیه در این بازه زمانی، بیمه‌تون رو تمدید کنید.
✔️
تا 2میلیون تومان تخفیف با کد
pnsc
👈
تمدید بیمه شخص ثالث
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/684558" target="_blank">📅 21:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684555">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtyPGJEyIP0bG2g7VGv_o5Yf-ZVosEM5rVDyBOqVg6rlv_hwMGdGnGhtaU_yR-zLiNq1fsGOIg_lTPNM2T24uiwDQkbEgp0cHH_LA78DhysMfj3y2ywc7PmBrMZ4BGhvPqL8J9x5xT6okBrpl3xoUcf6f4h0u63wN0c9ONNpbxM79NQPPXvmsplFR7NEtsRzBl8QQvpx0bC_p7pt252vNJOBCW3RhEEtJKxCz86Dv5KMs9hw8jR9ZnldiE7_IbpWvF1PLL485ApEQZsBBU3EPAGxIKh2cDMvtE9_zavvassujmH8fXVqsCSLlf-OKrhgT6F69LLVAKNKIXCH2CRWMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فحش و فحش‌کاری اپوزسیون علیه یک دیگر / علی کریمی "گله" را بهم ریخت!
🔹
همزمان با انتشار استوری جدید علی کریمی، موجی از فحاشی و توهین از سمت سلطنت طلب ها علیه وی به راه افتاده است.
🔹
علی کریمی، اپوزسیون را "گله" و رضا پهلوی را "یک احمق" توصیف کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/684555" target="_blank">📅 20:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684554">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VB690XZpMhR_rrTJ0KRmCep3YaUT_ZfPTdFTVGQhhkuJ3bRjTYB2ZGpzjKTkntqLP9vN2tCtPXr2ULRcjrMoaI772vwFhIW24AO_23rnHExPqTm2xO5AItq9v4oPMdAzBvRDMER_Mb8sRrTGz2sdOZ9EKi2m5ITmholYuOQXFbkNxWEKP8ldI-gveBjm4Pbv9QoTpsx_QyOCqENQPwl2RsKqskm86aJI-AObnLwoT4Ava9CZFoDJJF40psO5yr0uWWtbRtyHtHPrJkX9mRH25l3KIBfe89gNLlOv2t4E5F60flcDLwNAI-YEDErykF2UnQsQGni2VLGdzJII3LAtfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر شهید انقلاب: زندگی و شخصیت بی‌نظیر پیامبر اکرم(ص) برای همه‌ی دوران تاریخ اسلام یک درس و الگوی همیشگی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/684554" target="_blank">📅 20:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684551">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezMgItWX7x2qxX8uqXq0LMJ_W-Up6XfbB8HPUk4-IQIhFpJCzS4A1Rgj7_kssmjZnGJxWGyL-apxA3YP6Npe0R-hTz9tu6f-NBGnNc0OvlIIXNDm6SJvID-0_KBrTNvhWqdkwWU2hkxzGkxmFfGvBy7VIF773m7Dns1ndgv3tcu12sK-W-dDOc7cbKI0F1lvmrfT2EuGlsVGeMntL7rQSgbsMRQxttw2C3qU0jhxZxPztoyYNMSCYR6avqG0JHgqk47F4KXZ2L4WDMtiN2s9rX0sJfUh-rPVI8uhUZoyFSPbDKSvhhj4RHOUoa3DLX_V3tW3os5qISBk5PfpkpIrXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فحش و فحش‌کاری اپوزسیون علیه یک دیگر / علی کریمی "گله" را بهم ریخت!
🔹
همزمان با انتشار استوری جدید علی کریمی، موجی از فحاشی و توهین از سمت سلطنت طلب ها علیه وی به راه افتاده است.
🔹
علی کریمی، اپوزسیون را "گله" و رضا پهلوی را "یک احمق" توصیف کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/684551" target="_blank">📅 20:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684548">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3fTomJ3Vlz_qDjzTSOWKpjtPKa4p6hvgxOqDNzVhdOe3oZbrV2yBxhAUR-1t0CKqJENwsWSGmwyMEl2r62NTe_K-fcuyI-iUdXB15WwlXwP8UH_6tQZWqMwhnWHkxrnAqwox2GLPwYNvVK4Y-T0IBHsJS64zF01Lx9n2cWudPJSCH9Y86kOkGdElj39R3GnwAiYdhep5J0YD3b-L3YvbGMewfntG9Rs9erqt-gZXKJ4Z9NAw7JzIywTxNLJqq8ntaPS_tDBJ4DRlZxvXehdFeIS8AEuTVt4hiH7abl5z38DMBEbKJF5s5jr_sc2ToEV3KP4UENzneLWPYLOFlFCxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صندلی‌های سینما و تئاتر، خالی‌تر شده‌اند؟
🔸
در این نظرسنجی بیش از ۲۴ هزار نفر شرکت کردند که سهم روبیکا ۵۰، بله ۳۰ و تلگرام حدود ۲۰ درصد بوده است.
🔸
بیش از ۳۶ درصد شرکت‌کنندگان، کیفیت پایین آثار و حدود ۲۶ درصد هم رونق شبکه‌های نمایش خانگی را از جمله مهم‌ترین دلایل کاهش استقبال از سالن‌های سینما و تئاتر دانسته‌اند.
🔸
به نظر می‌رسد تغییر رفتار مخاطبان و کاهش جذابیت تجربه سنتی تماشای آثار نمایشی، از مهم‌ترین عوامل کاهش حضور مردم در سالن‌های فرهنگی است.
@amarfact</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/684548" target="_blank">📅 20:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684546">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">05 Ane Manaee (1403-08-10) Marghade Sheikh Sadoogh</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/684546" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه پنجم
حجت‌الاسلام امینی‌خواه:
🔹
دوگانه‌ نور و ظلمت در سوره محمد: سبکی نادر از تقابل ایمان و کفر [03:10]
🔹
از در هم‌‌پیچیدگی دل تا آرامش بال؛ خداوند چگونه تشویش مؤمنان را می‌زداید؟ [06:30]
🔹
همراهی خداوند با سالکان راه حق؛ برداشتن خطاها و بخشش لغزش‌ها [07:40]
🔹
الگوریتم‌ مغفرت الهی؛ کافی است مانع نشویم! [12:40]
🔹
حال خوب؛ وعده الهی برای رهروان مسیر ایمان [16:50]
🔹
حال خوب در راه عشق؛ هر قدمی برای خریدن لبخند محبوب [26:58]
🔹
ادخال سرور واقعی؛ هدایت دل‌ها به آسمان، نه خنده‌های زودگذر [35:30]
🔹
حق، مانای بی‌کم و کاست؛ باطل، میرای پر کم و کاست [59:05]
🔹
ملائکه و بیداری‌های سحری؛ از حاج آقا مرتضی تا مرتضی پاشو! [01:19:00]
🔹
زیارت با هدیه؛ شیخ صدوق به تاجر: صلوات بفرست و دست پر به حرم برو [01:25:00]
🔹
به خاطر یک لحظه دلسوزی بر امام حسین (علیه‌السلام)، تا قیامت در امان ماند [01:28:00]
🔹
امید آخر؛ وقتی کودک شیرخوار به میدان عشق آمد… [01:35:50]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/684546" target="_blank">📅 20:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684544">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bdacdec44.mp4?token=KoMhe7qZk3RHijijr2PXBGM7R7qBNOc9OTaTyWa4kxww49TplEBoq_MTR10xs6QlZ0AwhDvTrl3Ot932tuCgtaZk1MjZxJ081tjqTuqWRsGZ6JeUXxE8x_ljD-1cj4hRU0iMl9gDn22B_1MCw7pfUn2q6fTcknPoqOJF7nSGTUWh-fBCj0r7Mo4zCwCfYtMyP1uhQZPD6HqosVf-By4SpsAylMbW4J0w2sJl-dWhLmxfOSBz8K3w1qS9ZcVJjo1v9-TG2u1cwbkfe8j5zNXGvbOeyJVG2Dl5yQI4ruOtuDjz3nn-_FxU5EX3K7je2TFc9Ms2e0DA8oVblvF6NeLKUrqRxztStFEMOYdrEnRYsblfh_-sJ1gvxTOzU13AijVlpHn3bDXawT7XbhaM7_l6_hmaaEMN4FS5Dw1ZTRFDSx27vklQmtRhNRZTHFaH-wokFeE4cE2eABbrGibqSA1yjRqvDhla6TZLcaB_aZLsH_8ws4V9GPoCCJI38RnYSd7YqQ5boQ7WpCCAmTeDWHL1Et3vbZK4CZyCTjj4L5ju_T5hr91Ql5hUUTOCHoGsU-UHurhG-hEzM300yCQeYcAk09l8-o0dl-1lHosjvE8yo32vQpWaImHKSyD9VKDfyBqV1Gi5p25iygHwV3aewBlZ04MZJtezFCZfYhkl9RmgCVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bdacdec44.mp4?token=KoMhe7qZk3RHijijr2PXBGM7R7qBNOc9OTaTyWa4kxww49TplEBoq_MTR10xs6QlZ0AwhDvTrl3Ot932tuCgtaZk1MjZxJ081tjqTuqWRsGZ6JeUXxE8x_ljD-1cj4hRU0iMl9gDn22B_1MCw7pfUn2q6fTcknPoqOJF7nSGTUWh-fBCj0r7Mo4zCwCfYtMyP1uhQZPD6HqosVf-By4SpsAylMbW4J0w2sJl-dWhLmxfOSBz8K3w1qS9ZcVJjo1v9-TG2u1cwbkfe8j5zNXGvbOeyJVG2Dl5yQI4ruOtuDjz3nn-_FxU5EX3K7je2TFc9Ms2e0DA8oVblvF6NeLKUrqRxztStFEMOYdrEnRYsblfh_-sJ1gvxTOzU13AijVlpHn3bDXawT7XbhaM7_l6_hmaaEMN4FS5Dw1ZTRFDSx27vklQmtRhNRZTHFaH-wokFeE4cE2eABbrGibqSA1yjRqvDhla6TZLcaB_aZLsH_8ws4V9GPoCCJI38RnYSd7YqQ5boQ7WpCCAmTeDWHL1Et3vbZK4CZyCTjj4L5ju_T5hr91Ql5hUUTOCHoGsU-UHurhG-hEzM300yCQeYcAk09l8-o0dl-1lHosjvE8yo32vQpWaImHKSyD9VKDfyBqV1Gi5p25iygHwV3aewBlZ04MZJtezFCZfYhkl9RmgCVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پلیس نپال: سیل مهیب امروز تاکنون ۷۲ کشته داشته است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/684544" target="_blank">📅 20:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684543">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sqv60PxvHOgYkZqrSUJ4onUgpE8EdWdVIczkVGbh8S4rN9pLacx6UmTQmCH2zgOgf2sW7GnjGJ4WFVQqXoAXN6Z3H3ciQWwGxxas2U3DpR81pC7wC7PMbzm-AiPTzHljQhrxLgLH-5HOVj7a1jgTDTHdZ_-TUL2PC4e9oUWkeLOzaW4CZGIayTtmivSETmlu0ozmB_MnEQmPX33YSRwbchB_Yq1P0GAMjj92cD-NhpPCeEFJ6_OHEmLWZWIAEjYVU482FJ-GQAMzD1pCc6FBn4TMK59WW8EsCRZfEHspfBleYmwvwLhuO-pUbbzJW6ODXs267RL0_Pe-3UxNdLEi1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چند ترفند کاربردی که بد نیست بلد باشی #ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/684543" target="_blank">📅 20:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684540">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
قابلیت پولی دیگری از چت‌جی‌پی‌تی که رایگان شد
🔹
چت‌جی‌پی‌تی استفاده از ابزار ارتقایافتهٔ زمان‌بندی وظایف را برای حساب‌های رایگان هم فعال کرد.
🔹
این قابلیت که پیش‌تر فقط در اختیار کاربران پولی بود، به کاربران اجازه می‌دهد درخواست‌هایی را برای اجرا در آینده تنظیم، پیگیری و ویرایش کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/684540" target="_blank">📅 19:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684539">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3AY0mN9o_uzMhmpp_V_eWNq2jU7WyK6AJpWh73wf7VxGy9OLHy8i3gikKu5Qr8nj1auEGEZwknVMxMOtnhlGN3JK2FBqwYFfUa4hC4g18mt4VWR3FbTo1CrsKbHqLnDyXcr9Kd8yNQsCYBPFlMsh4UE-aRd2SRvRE3_DkXYI7LaqPb8kk-k5DnBgPOKDD0F9g2J2oCZoskMQDq0IOgYX0fbIU8CU_wWdUggdSpu2thrDTEmKpJEvqLthvIa_VJ9CXBJREnoPwNwxe6bFpoM8aAFgBcGb8oScnwtdhf2Z7g0KvQAMSSshsaw9udPJEuZMj5UUgdkDhHX0ZuBi37riw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرتاسر آمل در مدار 5G / هدیه ۱۰ گیگابایتی همراه اول برای مشترکان آملی
🔹
همراه اول با تکمیل پروژه ارتقای شبکه، پوشش سراسری 5G را در آمل فراهم کرد.
🔹
این توسعه در قالب کمپین «سرتاسر آمل در مدار 5G» انجام شده است. این کمپین از ابتدای شهریور آغاز شده و تا پایان این ماه ادامه خواهد داشت.
🔹
مشترکان می‌توانند با شماره‌گیری کد دستوری «ستاره ۱۰۰ ستاره ۵۱۱ مربع»، یک بسته هدیه ۱۰ گیگابایتی اینترنت یک‌روزه دریافت کنند.
🔹
در کنار این هدیه، بسته‌های ویژه اینترنت متناسب با ظرفیت و سرعت شبکه 5G نیز ارائه شده که شامل دوره‌های ۱۰ تا ۹۰ روزه، بسته‌های حجیم ۱۰۰، ۱۵۰ و ۲۰۰ گیگابایتی و برخی بسته‌های ساعتی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/684539" target="_blank">📅 19:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684537">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a383a3b317.mp4?token=bN54R-qU9B46cPHSiIPsghZ7R7gMkB13iN8oR1KNLkgAi719EvK6aP-knmoAHB6M2LH-FBLMshGR576tKf9ThsdaMK5sGAgdqsq9ewwEYrWBzZoG-SPt3PytiyWC9VziWI-Ml7ct9SOMSwObWKTzjvHkv2VDqFBztCIZ6JnALftz78tK9SIXDeX4nRQ4b6lt4mHZxhozi2fyf8uFBzC9t5Cm9CZAcmsjUsVjr5eclXai978_ahCHYdSMYot6Yc_qZvmi9hFWRp21I-BAJfk2E5SSV1vdcw3MUN89Lvy8ZfiiFVBvlN5BYP0z5Wu5BhKBsPYcY_fPeJGFHdHyOp_lQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a383a3b317.mp4?token=bN54R-qU9B46cPHSiIPsghZ7R7gMkB13iN8oR1KNLkgAi719EvK6aP-knmoAHB6M2LH-FBLMshGR576tKf9ThsdaMK5sGAgdqsq9ewwEYrWBzZoG-SPt3PytiyWC9VziWI-Ml7ct9SOMSwObWKTzjvHkv2VDqFBztCIZ6JnALftz78tK9SIXDeX4nRQ4b6lt4mHZxhozi2fyf8uFBzC9t5Cm9CZAcmsjUsVjr5eclXai978_ahCHYdSMYot6Yc_qZvmi9hFWRp21I-BAJfk2E5SSV1vdcw3MUN89Lvy8ZfiiFVBvlN5BYP0z5Wu5BhKBsPYcY_fPeJGFHdHyOp_lQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بی‌ارزش‌ترین ویدیو‌هایی که در یوتیوب بازدیدهای میلیونی داشته‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/684537" target="_blank">📅 19:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684534">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2l-boedpTK8qiYZI9PoXjTkXqx-56iemMGyyC37P0-Fw53aIvyGUICzapWtmkA4UF_dykX7gYrU8iQvcSh3v1Eojp8oSg7UVHcXw5E7k3kWxoF7Qfu2DtQ5xCi2dr_kGnN-L7IiCZx8HuA9I5M0EQwmfuxgohjU0eT69oyaZb1uJ1OBfKra67BSRwpNFLV7DpLUJYxiNEwdSBkAKq_3oYlSQ3s2KKv-6Q1UK2hel7LNiP9VzAUraT_s1ZeSgognTyhOBVycCEPpMzdN9pBNXXGet4wsKUXlkovXqsb_xYfkOUlbvxYUhKFFR9HQjenHnA1kpJrUDynt-chYsbaXUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این ویدیو چند شب پیش در تلویزیون پخش شد که بازتاب گسترده‌ای در آمریکا داشته و موجی از نگرانی را در میان نهادهای اطلاعاتی این کشور ایجاد کرده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/684534" target="_blank">📅 19:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684529">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzWkP4xueC5RqAGbwJ1scV-p6Vnse8PhePrkgGjq8fGtvHSdy0vsZ84pgRgHEG5d9loKErieE_vKOh5XjBpDdR7ECyA1r_vgA72ZaaMfqtMPsOHKAT8iV1uhwqkv9C5pmqdhD2MehNEgLwSw-wPgjbewbAx0X6CWWZeC1olFyIQ1RpPY_MMw4yY1Pb6EVhesaU_jo_GzEVdl-V-YeGBSeqWHONGwxWpAUC-4xr_Hwq48l3TMf6El3WWwB1BKVpfB2BcL0iwopvkMRnLRGp29bQEkZn1MdrQUjksDGuxBJm30_XZwkzAvMKhbKvt0QrggliFMpQ_MANd4HYSQzqVt0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امید ملایی قائم‌مقام هلدینگ خبرفوری شد
🔹
با تصمیم هیئت‌مدیره گروه شرکت‌های تبلیغاتی و رسانه‌ای خبرفوری امید ملایی به عنوان قائم‌مقام این هلدینگ منصوب شد.
🔹
این انتصاب در راستای توسعه فعالیت‌های هلدینگ خبرفوری و بهره بردن از دانش و تخصص ایشان در مجموعه صورت گرفته است.
🔹
گفتنی است امید ملایی دانش‌آموخته علوم ارتباطات است و سابقه یک دهه فعالیت رسانه‌ای را در کارنامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/684529" target="_blank">📅 19:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684527">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNWlMwvCplM0PyBz2Z7EZuFY4qVgADe1h4vqrUqtpsM4Mwnm_aEPDYswkMXKXw5P6FjmFJtxzFyaeeW6xCK3gVRS80vRcKZErAdqEVlwhLw5CD2e44F8dM_V8dxQQJtsygXTF-OQscfcQPZxIkoEZ6q1FrK4NLRdIB8Y9FCQISQu7diqyM9l67P-IlGUuzNn7qptGmsUFwL6qO5mfv6TbLnNKGCeU2QZpGPk32IG6l-qotGWEUS3ZrnAW9NQkhs3x7xdBRXwu3C9n9OaALaNdEfGMXL4VM-hep3GAFZeIHCm8TvwJhn6EeZPvZJu5cGT-XusqTG76Vm1Xw_otfhV0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایست بزرگ مقابل کشتی هندی در تنگهٔ هرمز
🔹
یک نفتکش هندی به نام «HAANA» لحظاتی پیش قصد داشت تا از مسیر جنوبی تنگهٔ هرمز موسوم به کریدور عمان عبور کند اما با هشدار داده شده از این کار منصرف شد.
🔹
در ۲۴ ساعت گذشته هیچ ترددی در مسیر جنوبی تنگهٔ هرمز مشاهده نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/684527" target="_blank">📅 19:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684525">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/558b39f2ab.mp4?token=bcIP-Xk2BSq3tFL_5rWhONvEIpojGxigPqXgvm4iyqKTKlYFy1YQCkvj5r1BfHO-Ec9CJYZHmrOR11QggHQjwjyxXOm6jrp9vCBoSH-VfHELofb8t6J4SwTMIkoQwQnwq3qS9gCqZr3gCyHcnIegpivF5O1SOWn1w3ggD0mc6Hc0cHY4QnOBL3Omsj6LtUwCKrdU4xgBwQkp0OLJ5zGnpu-0WrpM3qDzdsHj-XH6Wig3Jq-Wr3os2Gok5nKpaaMse5FfUMdFBG1-yvyaWG4SbY4FcwBY6zMafYmVBGuotu0t3dG8LpoIm-kRKERuAemfucUfyMB5syVTEtho2y_UZSTiW-cS9ve1j6wkLXZ_CF8lg_N_-QWoJnqxEbnfw08qkDCcFr8KfzPs-7HjIGAmbefmIYmk4K8qOqkg0u7hX8jNrENjHjxe_p_G9zyfTCIj2h6jcR-zE8X2nfHnOfjSlOm9D9OVdbT8kvrA5PArqNxWz5QnvU4vx4KI40OkO11uvxZgWLQyI4XEF8CoA86iLRrr0awrDuFjzDca5SzeEW2Z6Xx26jEYmrW7bb1EiUh8Xmy-d9rf9rMmCYZNTCosUXecdFLwqtrKWRUhZTtPIisYg3b0EWsrTkxCkKqXKJBDG_YpUfBH5wAFkHAQ-fFT3c_oXZ4gLoh8KS6837biWVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/558b39f2ab.mp4?token=bcIP-Xk2BSq3tFL_5rWhONvEIpojGxigPqXgvm4iyqKTKlYFy1YQCkvj5r1BfHO-Ec9CJYZHmrOR11QggHQjwjyxXOm6jrp9vCBoSH-VfHELofb8t6J4SwTMIkoQwQnwq3qS9gCqZr3gCyHcnIegpivF5O1SOWn1w3ggD0mc6Hc0cHY4QnOBL3Omsj6LtUwCKrdU4xgBwQkp0OLJ5zGnpu-0WrpM3qDzdsHj-XH6Wig3Jq-Wr3os2Gok5nKpaaMse5FfUMdFBG1-yvyaWG4SbY4FcwBY6zMafYmVBGuotu0t3dG8LpoIm-kRKERuAemfucUfyMB5syVTEtho2y_UZSTiW-cS9ve1j6wkLXZ_CF8lg_N_-QWoJnqxEbnfw08qkDCcFr8KfzPs-7HjIGAmbefmIYmk4K8qOqkg0u7hX8jNrENjHjxe_p_G9zyfTCIj2h6jcR-zE8X2nfHnOfjSlOm9D9OVdbT8kvrA5PArqNxWz5QnvU4vx4KI40OkO11uvxZgWLQyI4XEF8CoA86iLRrr0awrDuFjzDca5SzeEW2Z6Xx26jEYmrW7bb1EiUh8Xmy-d9rf9rMmCYZNTCosUXecdFLwqtrKWRUhZTtPIisYg3b0EWsrTkxCkKqXKJBDG_YpUfBH5wAFkHAQ-fFT3c_oXZ4gLoh8KS6837biWVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در پی انتشار ویدئوی نقشه ترور پسر رئیس‌جمهور امریکا، شبکه‌های خبری امریکا از جمله سی‌بی‌ان نیوز با انتشار فراخوانی از حامیان ترامپ خواستند برای محافظت از او دعا کنند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/684525" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684524">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omqbakB4_e0aAzJ0v6gbvLNIa6cSlIxqRE6lvAN_TWvmY2toOWOQaGqnMSL7nJa94VZGsKi7vz2OtlXCPNhZ2JOzuPYFeQX9KvjuuSN0E7CoNCvkq_xo7RfX7pq-ZlOuRkPe7urOFN9pbLeEQ2LYN7opMOWmKjRygjBaTjtVZH___BG2VCZHB2aphgSAKH7fS__HexS_kym1UQQg9ql1bpAdY481d_Jz7_m-3nn4a1H_aIeItgiAjHynZNjzPz2ExfWDuA3U5eLtq4DmWeQMjFHfCdQDKCD4JIZRYvyet8LiGShrplN0_5f-DR1-FpDR_rOzgDQOt80FTc4V4tlQ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«منافع ملی»؛ معیار انتخاب ایران در اسلام‌آباد
حسین افشین، معاون علمی، فناوری و اقتصاد دانش‌بنیان رئیس‌جمهور، در جمع نخبگان کردستانی با اشاره به تفاهم‌نامه اسلام‌آباد تأکید کرد: دفاع از تصمیم ایران برای امضای این تفاهم‌نامه، دفاع از اعتماد به آمریکا نیست؛ بلکه دفاع از حق ایران برای انتخاب ابزار مناسب در یک مقطع مشخص و در مسیر تأمین منافع ملی است.
به گفته وی، سیاست خارجی زمانی می‌تواند مقتدرانه عمل کند که تصمیم‌ها بر اساس منافع کشور و تشخیص درست از شرایط اتخاذ شوند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/684524" target="_blank">📅 19:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684523">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآجیل و خشکبار برادران حسینی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ed72d204a.mp4?token=gM2xlykdp3Gxzw5glWU1LEsbMEg-ir6L49lxpFz474X4Y0X9XbhK5HLMYZt4I2E039DKjQHatUlVAyTF3Ps4vFViQl-DRAl3eESoeWezyhhwR6qSmjcSGVIauqES5aQC77C-dRU__Pis9DTfqL_l06e8ckUQnWkRznWAADthZCyPDNLaJPayVg38SRAcmArnnqXDwHtQwzt5g6UGDcyI-PkPjWFJM03g4Xutk9YujWSLL0BIrUFuRmvirp8hf8dLH9x59-ZpSVjd04-nS0jlywHB1tqY9McDLCg_cFZ43m2W_5CNRgIgcgihClcNo0h1nB6XKLqvYsB4WnwPtDQapg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ed72d204a.mp4?token=gM2xlykdp3Gxzw5glWU1LEsbMEg-ir6L49lxpFz474X4Y0X9XbhK5HLMYZt4I2E039DKjQHatUlVAyTF3Ps4vFViQl-DRAl3eESoeWezyhhwR6qSmjcSGVIauqES5aQC77C-dRU__Pis9DTfqL_l06e8ckUQnWkRznWAADthZCyPDNLaJPayVg38SRAcmArnnqXDwHtQwzt5g6UGDcyI-PkPjWFJM03g4Xutk9YujWSLL0BIrUFuRmvirp8hf8dLH9x59-ZpSVjd04-nS0jlywHB1tqY9McDLCg_cFZ43m2W_5CNRgIgcgihClcNo0h1nB6XKLqvYsB4WnwPtDQapg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌰
برادران حسینی |
🎉
جشنواره تابستانی
برای مشتریان سایت، این فصل
2️⃣
امتیاز ویژه در نظر گرفته‌ایم:
◀️
با خرید بالای ۳,۰۰۰,۰۰۰ تومان
✓ ارسال رایگان به سراسر ایران
✓ یک هدیه از ما، همراه خرید شما
این دو امتیاز فقط تا پایان جشنواره تابستانی برقرارند.
خرید از سایت
👇
🌐
https://hosseinibrothers.ir
خرید و ارتباط:
hosseinibrothers.ir
t.me/Hosseinibrothers1342
ble.ir/hosseinibrothersnuts
rubika.ir/@hosseinibrothersnuts
instagram.com/hosseinibrothers</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/684523" target="_blank">📅 19:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684521">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qggn5DJ0oCRo_I5PfrQJud2PZ3mfpEGRmwTVkczzuQt-F6_CihMor83RZVCTKr8x_Fy3GPv8gf3jcctH9y3LXuYVKwbRcgyjFc6nAfQlTEREgCUCDhx84k5aJW0zv6sFTbvwXoAMQpIr8sv0CFzRZsUtBQheeFz3LXZCCxb0FQMNUzSRzeA4HBH3qtiu19yfAnBUX0BJv85i7VmgsAM-44bUpJJpI2Nsqfa3euyaLumOZWBQ1-_n69pwC7lEk9VFF8hZvWACfMHjRVBMfE0D0a83R8Vpod3OOuqbXxZxY0Zrg1yVBAaqu8bRwAFOnWqYXDQGW9iVkuXgcHt9eLHmcw.jpg" alt="photo" loading="lazy"/></div>
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
https://khabarfoori.com/</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/684521" target="_blank">📅 18:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684519">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axiGVGEQRiu085-fPpIpMyxjW9IS1IOZN_5rd5vCavSEzPoHllO2RP1Bs_jS_2-IlYQn4-jKB8VFufCSH6GCUbdFIW38pMiMpCvwXbui_b9rfx--nhsC0nbtKSkBgVB7kUNsok1TDhmkFu3hK70ImPwdk7f7oJrf7_AAz2hDpAN3sWGXvaTlNIksfnJzROw0Lsu61k5jLuflHjfO9o2ass4sFzSTrtZUkk-rPJJDSmJ06Bn7hodFLT1ogF76M3LEb7z-rBWYp4jPBGN9zT4yU5B1axHKEyzREVjz_-7jNenltVSUuTNw7LCQFBas-EQt2yU49fkPf_7dkj8VDPi8Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سید نظام الدین موسوی سخنگوی دیوان محاسبات کشور شد
🔹
با حکم سید احمدرضا دستغیب رئیس کل دیوان محاسبات کشور، سید نظام الدین موسوی به عنوان سخنگوی این دیوان منصوب شد.
🔹
موسوی در حال حاضر رئیس هیات چهارم مستشاری دیوان محاسبات است که با حفظ سمت، سخنگویی این دستگاه نظارتی را بر عهده گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/684519" target="_blank">📅 18:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684517">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtdMo_L78YeI87LR9Isg4kUrM0cAAZIDnzWfWLr1NM2xt-MfZ_ulF0oY_I879AuUUnF6ekAPi2XVcC-iAWaWSPjA1UvooBV25Mfvs4WutKzIPMAjsjOh9f-y1cKssASq5lOqX-hN7LdnlL2xTxDIWkAiW4oY6DKNMvdBvV58HE0yEgBdWZ-kc_fm0NwOLDoPStQfkOdjorkc0klWyEU-d5A5F84K1WwcDXD2-jX4-_lJJZb4Dro04jWXwWR7Tf-SpzGiEfxA77PNY_VGRc0hH21o_YIkBtTEV7lzGxfU69_vhqdqCSZAfE5np75MrQ_UFXF4_zRtUOVmpzWLUWIOFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعالیت سامانه بارشی جدید از جمعه؛ هشدار به شالیکاران برای برداشت سریع
یک کارشناس هواشناسی:
🔹
روز جمعه در سواحل دریای خزر همراه با کاهش دما، بارندگی‌های نسبتاً قابل ملاحظه‌ای رخ می‌دهد، بنابراین هشداری برای شالیکاران است تا در برداشت محصول سریع‌تر عمل کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/684517" target="_blank">📅 18:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684516">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f97d7acf26.mp4?token=gbqmm09AKgN5C3lFMGSPFJeRgtarb5onFnrNaYrCgzDsqfJCiBUAMklN-NoUuGHPehbMeFe3AFL2XRqfgLwIKq9wGJAvtvA0LSD3AGhq6ux4CErcyyAwBqpX08xwgEG6Dclr_Fmo0UwfZ7ZoC60WWSv-1yW2IWLM1g3cDKXDN-ttShYNlhQKeWI_HlwkAWsw51xsBYFj4w5Ix3fwMAmh99fctAbLt4w_eg1S6U4sQlPA5DItk0PjnEdVgJ9WU_VySAe2HRzOwKsYqDUU4feW8SvKkqdbADZ6P54qmGmlMBi2HRqLUIVA4IczdvQX__26QR98xOfEKqdmOSjBBNXxGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f97d7acf26.mp4?token=gbqmm09AKgN5C3lFMGSPFJeRgtarb5onFnrNaYrCgzDsqfJCiBUAMklN-NoUuGHPehbMeFe3AFL2XRqfgLwIKq9wGJAvtvA0LSD3AGhq6ux4CErcyyAwBqpX08xwgEG6Dclr_Fmo0UwfZ7ZoC60WWSv-1yW2IWLM1g3cDKXDN-ttShYNlhQKeWI_HlwkAWsw51xsBYFj4w5Ix3fwMAmh99fctAbLt4w_eg1S6U4sQlPA5DItk0PjnEdVgJ9WU_VySAe2HRzOwKsYqDUU4feW8SvKkqdbADZ6P54qmGmlMBi2HRqLUIVA4IczdvQX__26QR98xOfEKqdmOSjBBNXxGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پلیس نپال: سیل مهیب امروز تاکنون ۷۲ کشته داشته است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/684516" target="_blank">📅 18:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684515">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae39d4883a.mp4?token=orbRvTpPZZXR1vtFBEjTqwd52EMsD8sIkGV3BrKNp0_G-d5pZaFWZoFJAOY9MOXK1KXXqCOSr_Vo69Up-0ngx9LdzeHNUSLxXzBoT5cnwDMF8iA3PkvUKHIjsU7646Lf-qeXu9MBRd2DKQb8SS-3UU-o5NeXUR8mL7VR30ScWnBQ1fSK7VAmSPxHN1I6v6Q0PKBNlKTY5zcUel01rVRj7Btm116AXEkdz_ElNl4xK993KOtR4RAxA8CU9xXUmnk9oDewj-ec7xZQwNLKkDKHSAr-8pzQDHV4vduNbehRw7Ip0GNWY9QcBJHDC--RUPXbRozZk08uivKWCWZnTZoYQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae39d4883a.mp4?token=orbRvTpPZZXR1vtFBEjTqwd52EMsD8sIkGV3BrKNp0_G-d5pZaFWZoFJAOY9MOXK1KXXqCOSr_Vo69Up-0ngx9LdzeHNUSLxXzBoT5cnwDMF8iA3PkvUKHIjsU7646Lf-qeXu9MBRd2DKQb8SS-3UU-o5NeXUR8mL7VR30ScWnBQ1fSK7VAmSPxHN1I6v6Q0PKBNlKTY5zcUel01rVRj7Btm116AXEkdz_ElNl4xK993KOtR4RAxA8CU9xXUmnk9oDewj-ec7xZQwNLKkDKHSAr-8pzQDHV4vduNbehRw7Ip0GNWY9QcBJHDC--RUPXbRozZk08uivKWCWZnTZoYQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چگونه یک خودروی الکتریکی می‌تواند برق را به شبکه بازگرداند؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/684515" target="_blank">📅 18:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684513">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRwyP677V95ExIWXFyC7jstkoyIIGOJyYzIFsJNI-eC3DUAtgJ1VkkCbIUGy_-ajSK81FxS9zFG3NreAimVjFBcFXMbqMt2nYvLmGFnyxop-hEq6pt5SSViMm8g5Dp--DNNQjkaMNWKkGN1P-Xf6K_XIaM4UWEL4Y_DZiI5Tc84BODzSEn--vsuFqyY6FI6IQkdkpvJa-JpBMiAluod_AS5CUMbKX27Z0UBuS8BR-_0h7K-8AH7PnQNLrUKhhEA9AmHtsi5EVGSHSXdexZ8hqeNYZPE2Q8qhk62Gf_ZPxkOT1IXwi3Q0tYFwuoOGsYTk3niDGM4pFxo5gCys-GKEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا آمپول‌های کاهش وزن به‌تنهایی کافی نیستند؟
یک نکته در توصیه‌های معتبر جهانی (ازجمله سازمان جهانی بهداشت WHO) بارها تکرار شده است:
آمپول لاغری، بخشی از برنامه مدیریت وزن است؛ نه تمام آن.
آمپول لاغری حاوی مولکول تیرزپاتاید (مونجارو و زیکورپا) باید در کنار تغذیه متعادل و کم‌کالری، فعالیت بدنی منظم و زیر نظر پزشک مصرف شود.
بنابراین، تصویری که گاهی در شبکه‌های اجتماعی می‌بینیم ــ «یک تزریق و تمام!» ــ با رویکرد علمی مدیریت چاقی فاصله دارد.
این اصل درباره داروهای حاوی تیرزپاتاید، یعنی
مانجارو
و
زیکورپا (ZCorpa)
، محصول داروسازی دکتر عبیدی، هم صدق می‌کند.
🔗
منبع:
سازمان جهانی بهداشت؛ راهنمای استفاده از داروهای GLP-1</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/684513" target="_blank">📅 18:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684512">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9dtjm0dxph_A4jYJA5B7aaCYyXIm0reYWTJ1UlxNmxxo9Z3pSuukpxmVYVG1CM2jbEVtKJrkq7UXYOhfPPznusJQsk0IuYuWibkLRmLwnXbJJD_KXHvYTHcUmw00j8qwpHfH0gKxJzY0-ljP34QkMhuoC6crVK3M1e6u3AAzqwWZbVj--Ln_LIQTojcf5bcnyZQb-JpuMUOoEKM8De4ncjLcZB2LOAj0wvrs6Ywi-6tznU4FKWaVEamSv8J0_RTXJ9fRDfxKJ63L2wl4uHOQQLuNxBdw3TbidJMPBJHnuEhKstizvNLDZK9-kXZ92jFqoGC-r3grBLngqp1j6XUtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراخوان عمومی شناسایی ارزیابی _اعتبار بخشی و انتخاب شرکت‌های وارد کننده خودرو در منطقه آزاد سرخس
برای دریافت اطلاعات و ثبت نام در این فراخوان مطابق با شرایط اعلام شده در پیج رسمی سازمان و کانال های اطلاع رسانی به آدرس‌های رسمی تحت عنوان
@SarakhsFreeZone
مراجعه و پس از دریافت اطلاعات به  سایت رسمی مخصوص ثبت نام به آدرس
Plus.khsfz.ir
مراجعه و اقدام به نام نویسی نمایند .
🔗
رسانه مجازی منطقه آزاد تجاری صنعتی سرخس
@SarakhsFreeZone</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/684512" target="_blank">📅 18:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684511">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aba9e1faf.mp4?token=lnuEx5JG09B3WiIBOHsFKbx1OB_THRoJrpzD1hqSLNiqBFPGq3uO006RyFHxeTCi7iyil_z6dJ7sTAL1bTdjbsDjWoZ0G_u3fX8ku2bg0vLouk3mGix7GiDKgDZRZ6qJsn62zmCEyL11oWjtITwSoWdI_2qq3oVzNYmoGZHjGmJ1rtgisNcSlfvBeDuVDAxaR6cZK4c5KeNqNhv7yk4OwP1Bf7zayv0hb2cmAwsP5p2AUyH2pP5xaqdlmbuE7eao48SyCwfu6WpZehoYPV-qtv6XDtvlHbiqDr5fTi0nd4euWyFlsoNtu0neNuhyzszQwavf_kGh5nSfFk5qIl794YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aba9e1faf.mp4?token=lnuEx5JG09B3WiIBOHsFKbx1OB_THRoJrpzD1hqSLNiqBFPGq3uO006RyFHxeTCi7iyil_z6dJ7sTAL1bTdjbsDjWoZ0G_u3fX8ku2bg0vLouk3mGix7GiDKgDZRZ6qJsn62zmCEyL11oWjtITwSoWdI_2qq3oVzNYmoGZHjGmJ1rtgisNcSlfvBeDuVDAxaR6cZK4c5KeNqNhv7yk4OwP1Bf7zayv0hb2cmAwsP5p2AUyH2pP5xaqdlmbuE7eao48SyCwfu6WpZehoYPV-qtv6XDtvlHbiqDr5fTi0nd4euWyFlsoNtu0neNuhyzszQwavf_kGh5nSfFk5qIl794YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
خیلی راحت و جمع‌وجور گرامر اسامی زبان انگلیسی رو مرور کنید #زبان_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/684511" target="_blank">📅 18:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684510">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
سخنگوی سازمان تعزیرات: مردم طلایی را که به صورت دیجیتال می‌خرند، حتماً فیزیکی تحویل بگیرند تا با خالی فروشی و عدم عرضه مواجه نشوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/684510" target="_blank">📅 17:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684509">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
تکذیب شایعات درباره کمبود بنزین/ تولید و توزیع در حداکثر ظرفیت
مدیرعامل شرکت ملی پخش:
🔹
تولید، انتقال و توزیع بنزین در کشور با حداکثر ظرفیت در حال انجام است. مردم نگرانی بابت تامین سوخت نداشته باشند.
🔹
ضرورتی ندارد افراد صرفا به دلیل شایعات به جایگاه‌ها مراجعه کنند و صف‌های کیلومتری تشکیل شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/684509" target="_blank">📅 17:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684507">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8Qt2Ab6Rc2Q-LkoNzpWJa5DBStbJ33BSOgfwQvMVPaZCZGYPQR1sHAwOlojfEtf2JSaIJO3I4wF3kGr0e63jI92e89X15wViTL-KQTLgX1eaDTiUYpt6I6uJVJJFbhgw8yDFBQ8dZEc9sKaJoqsBuQ1vnIhh3SwMjh1sVsdXkYidSKcNAMkN9Kta4IqseO3FFlarmli3oIHR1UprP2Xh10S9HciRXstIHrcEt32odRw9Jha2L3KEDu1DvJ_ZhY2BWVAVJzSHEh66FP-JqhYTLYwpFomey0m0BCCIy9928uHEk1wWZYFk3NeTPQP9x1D5TJoOsjSdtJ-HF-tC3xfgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پای کار «خاک ایران» / ۱۸
🔹
رکورد جدید بانک کشاورزی در تأمین مالی با ابزارهای تعهدی؛ میانگین رشد ۱۴۶ درصدی در سه سال اخیر
🔻
بانک کشاورزی در راستای گذار از بانکداری سنتی به بانکداری نوین و با هدف تأمین مالی مؤثرتر و پایدارتر بخش کشاورزی و افزایش ضریب اثربخشی منابع بانکی، طی سال‌های اخیر توسعه ابزارهای نوین تأمین مالی از جمله ابزارهای تعهدی، اعتباری و دیجیتال و تأمین مالی زنجیره‌ای را در دستور کار قرار داده است؛ رویکردی که با استقبال فعالان اقتصادی همراه شده و به ثبت عملکردی قابل توجه در تأمین مالی زنجیره‌های تولید، به‌ویژه زنجیره‌های مرتبط با امنیت غذایی کشور، انجامیده است.
🔻
حجم تأمین مالی این بانک با ابزارهای تعهدی طی سه سال اخیر با میانگین رشد ۱۴۶ درصدی، در مجموع به ۱۶۲ هزار میلیارد تومان رسیده است. این رقم از ۱۹ هزار میلیارد تومان در سال ۱۴۰۲ به ۴۰ هزار میلیارد تومان در سال ۱۴۰۳ و ۱۰۳ هزار میلیارد تومان در سال ۱۴۰۴ افزایش یافته است.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/684507" target="_blank">📅 17:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684501">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/arqNO8VYmA90OqCnSOUglcM6pbTTXIms9WNwsbu14W3ap3Aw197VHi7EOybE-Rr1Ea-RNjHSVU56ndhpCQP_GZhP0EY_OMe1HX-p12jize-pZ6zMP7KpNjlIK_BBowsRfeswqnYOaJ6PFJVelpb0XcDeSDror1h79rcKzItOTpPBVgCfM3NvZoYQEDax2PKLvnGlvxm6tHkVwMy5PPBk68h3kG0oY69YpVxhc_dn1_2eUgOU3qHrxHgcXlX-KpkBejgbHBrpg51pJpPp5gzNY1b4FnYdM7xzYJcROHH5Aj7dliybeGWKDmxIEobjxPVmzN-YiWp3xzEHQMcIF2uwjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJHp6h6zjZzTX6Bb7eR4qUOFr5Wlu4T207kyifekr8eMl12M1bTyJefTsb5qaSzxRCeI0Wj3kWpfoBRetzOeoxe10s9-tx6eIslNU0kPg3BxHpTV4NyV_OROjwbBgtZKXDaIkbDIZfDxWF_I6w-j2moYQYqF_fN6Dvt1oMIQ5GrIumZjohAlkbqLSQdCfSMmO8g-LnXI3PPbNP6i_l9ayWBw2Hoer8obDitKt5ZLDrl-47f8UHmqsmd8syeGmlbCT_Spbp_Sqts7s4Xrf6IERm4QoAhQP6g08Sqpkrg4drk-wk_85zA4SwN1pDbe1TfDYpj4HfHMDHTiXGiXSFLm_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tfi4G2o-8cd-E-yW4sP_x4tOvnFvUWNc5FkCvI3D1gptllI-1LQcapG1FW6om6NPA2bm9e7P-q5FUk9Tjx6r638tWaDiiGmcjkDNuirOADToeutwsQItonHYpjfhU_FS1hNVUfnvNTYNq14aucosi3jeq0F8AGlOdGw4Dr4mr87CE8wZvRTdqP3asE_L9iZgbU8i1dL5OGA2AfdRrPOIPV1CA0gUePvTbvHHMEJ2My7_MmxCaPz1l1xPa36Y7gDujIev4eXOQs_nNL6tiBC8vWzSOy6eOcswULBKyDUthuCM6PA4kIjMgSVaML--9VpAy1Jh2VH-62oWU0idmDJaHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWIYxs2G2lbGwoIPC_61GfeVChJc6VqQ3MXgyD2eT7FwMLkPd5JWaJ8HfA6TheovagasC2qoTO9Ck4CRJYtQF-bHvR3_39OZhNHywxN0x_OTmIecIk_X133MFefeoWuUP93Vk_UKgOabZWHVqO1yD6QWM6ewGMV8S1jmLQ52yrpciyPoVQY5yJeHWvVRoioKh9ECXmD9gReuI99Y1RyLONIZTqMaGTnZSfrIy30V73PbOZbzcTcqTjp1hLNm4PdMBGwIXAvP7WCa2D9Wr_4VbidMHX4eXs-lCe0D-WdGtHcSEtGGFD95Ub266XZTJEhODQizHf-4uUtbPS2UkTzMgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QJzj12uPxnQqTzTfSmtl1RpL-BMlvov2qfS6QEmYvlsR59Xm8APzm27qOmXKyObLDyUn3CFttYsuGcJVvQVhqg5ZI2mwy8g92MMo1ogLCV4HqxOpmUiOd_67UEOcpmKzcNxib_rRyuMi8DP8-AK4Fh9Tq6igp1uGs5dpbR02UjeN0t_EgLwdyhBKTL5A9SSvep1db6OQQ2FUNVM0nApFWdRMIPpk9a1FmWxCSeykDFe9xwuqDMuSe1jDkaQ8njPLlvY_IhdQoNpszdgN4rMrv3DzFZKl_k-HKGhubymxxVAVJmWTXTJ8A1Xep2VAAsue7_pGo3QmV-iMIwyOTdb9Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rqhaqk85eiVif8_s8kxgkAQf4oIrMkS7q-LWYYBoFlRlUT5wRf05PKOE94j1HVRvvIfyMgpeuqonJ0aAMSkDGCUKEK40iMrI2cSCtwRbiNmsgaa_u4BcRKVeMJvhOKM9_r8rEKhAr5MOIc3gMYd2Y4gWIf1OzDnng_cEN9YNKrWVwS9xuRndJMW2E3HUGNODv9tGLODxEQAAG6bToHSbjfoIKZCWVmYDTEu8-UW_uovt_mRrrtF3GiNC-p9GRggjMsoTUFvC1kHR9b1o7tg0_8FuaANRBsl8BMQ4VUyiCl76wpsYAzZuOgD9Unaqx76dIphHIcTA6x_GupiVQcZ4lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
«بگو چکار کنم» یا «نگرانش نباش، با من»؛ دو جمله متفاوت که حال آدم رو عوض می‌کنه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/684501" target="_blank">📅 17:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684500">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
وزیر ارتباطات: پرونده فیلترینگ باید بسته شود/ استفاده از فیلترشکن‌ها خسارت بزرگی زده
وزیر ارتباطات:
🔹
سیم کارت سفید مصوبه سال ۱۳۹۹ بود، اما در سال ۱۴۰۴ رسانه‌ای شد. استفاده از فیلترشکن‌ها در زیرساخت‌های ما آلودگی ایجاد می‌کنند.
🔹
در جنگ رمضان ترافیک اینترنت داشت به سمت منظومه‌های ماهواره‌ای می‌رفت و اگر به نقطه بی بازگشت برسد بخشی از حکمرانی کشور از دست خواهد رفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/684500" target="_blank">📅 17:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684499">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptW0cKN0VcWzho0oZRNZAQUcGBwpy7F-4_LFqypdAtLWfRluHCGByCYkreNO7NJ-qRU2eQYwSIFjTYQ5sgGnNSpycLypCLpoaitY029yNZA-iM1T8lEAVnL4vtylF9Rl7UyHKEr_4qPxqUBbcRViNBmVrU0koWDJIEG2MiNWjYDgrmxW4Brge88xsQ8k-lVR8FopzSllr-9Lbrp0gst3lAnIfbKv0WT5hGZEY962jZ9KpygntKvn_tSXyjAkYVM15zfdZhIUXAhEOI9Ahy-xHFFjyXtapR98wntrDL4bkvE-ZVCIiH0qwAQQiL49tmMjrM9DUm7IFo4ZRJehbFYkvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدام کشورها سرانه خودرو بالاتر است؟
🔸
کشورهای کوچک و ثروتمند اروپایی، بیشترین تراکم خودرو به ازای جمعیت را به خود اختصاص داده‌اند و کشورهایی مانند سان‌مارینو و موناکو در صدر این رتبه‌بندی ایستاده‌اند.
🔸
در میان قدرت‌های اقتصادی، آمریکا با ۷۶۰، ایتالیا با ۷۴۰، سوئیس با ۷۲۰ و ژاپن با ۵۷۰ خودرو به ازای هر ۱۰۰۰ نفر، بیشترین نرخ مالکیت خودرو را به ثبت رسانده‌اند.
🔸
ایران نیز با ثبت ۲۴۵ خودرو به ازای هر ۱۰۰۰ نفر، رتبه‌ای بالاتر از کشورهایی مانند اندونزی و هند دارد.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/684499" target="_blank">📅 17:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684495">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ادعای ترامپ متوهم: دیشب ۲۰ قایق ایرانی را منهدم کردیم
🔹
ما در ونزوئلا به پیروزی رسیدیم و خیلی زود در ایران نیز به پیروزی بزرگی دست خواهیم یافت.
🔹
رویارویی آمریکا با ایران تابع هیچ جدول زمانی نیست و تا هر زمان که لازم باشد ادامه خواهد یافت. #Devil
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/684495" target="_blank">📅 17:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684494">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ادعای ترامپ متوهم: دیشب ۲۰ قایق ایرانی را منهدم کردیم
🔹
ما در ونزوئلا به پیروزی رسیدیم و خیلی زود در ایران نیز به پیروزی بزرگی دست خواهیم یافت.
🔹
رویارویی آمریکا با ایران تابع هیچ جدول زمانی نیست و تا هر زمان که لازم باشد ادامه خواهد یافت.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/684494" target="_blank">📅 17:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684492">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kq2JUd4CRwcLaGnINCnRt3ktp7P31tBSiq21tofl1zjO1pmk19qimmV0IHSXlnEHLVYkh5i4Ts5uLYM7ZAoBrYEqxNIt9V1AcznZ3IlSqPkYQOwLpBE2SXifuxezrSQdavdWk39wvxm8PW84dP_p7Kp5fPlYCioAWCerQOFPMrWOWY0xQQIRlG26Q2XL_CbXoz9tY4JGng050XvvXWhCWr2Us_bMDb_BFkmyz4DlsnYTXNGU541aFP4ddUknX3ccSlbhsP6U2JXvbl2Umsi373ENeUj-KX6djuJWeyy5l7zaVowVtKfmueEvi0tgS7d8r2fJQYy7YAKEvIAU2fjyWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/963c6ddd65.mp4?token=NV1AgqQBsb6v-u8hygAp_TFcfStV44UwYmJdRhlvndDMwZbKLZ8r93EnIJgypWxgmfLSsOLGk-yhPvig1f-UtkK8puJeFH0zHxkIXkoW22jss6uEDZusLpc4kq8Q6gQG5m6RjEW67TI_MLqA9JTsZSf3Cj85xOJm3k6WMkoa_S1SAmqMnMfpBYCwck9OSaiyi1fZeDeKiNx_5mgeF_ZRXiN-W_4dt-dqvoOdnGLJINsQg-ai9YSfxCYTQnwnnfHa7PLZsa7uWfLs8Ls4Ic25HORR4SNmbUIEGFeuBI89kANLfOeeiF1_eBE2K_LXGFDIc3I0t1E4V1sll9WdvXr-NzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/963c6ddd65.mp4?token=NV1AgqQBsb6v-u8hygAp_TFcfStV44UwYmJdRhlvndDMwZbKLZ8r93EnIJgypWxgmfLSsOLGk-yhPvig1f-UtkK8puJeFH0zHxkIXkoW22jss6uEDZusLpc4kq8Q6gQG5m6RjEW67TI_MLqA9JTsZSf3Cj85xOJm3k6WMkoa_S1SAmqMnMfpBYCwck9OSaiyi1fZeDeKiNx_5mgeF_ZRXiN-W_4dt-dqvoOdnGLJINsQg-ai9YSfxCYTQnwnnfHa7PLZsa7uWfLs8Ls4Ic25HORR4SNmbUIEGFeuBI89kANLfOeeiF1_eBE2K_LXGFDIc3I0t1E4V1sll9WdvXr-NzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل ویرانگر در نپال؛ ۸ کشته تاکنون و مفقود شدن ده‌ها گردشگر
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/684492" target="_blank">📅 16:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684490">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac706e15a.mp4?token=vguQUqS6tz6qUPWiwZSqyJeGBj1EZ_7RkKgAPi3297ahIY-JKkoGcFo7vh3YUSkO3kpR-VWzLAlFBXQHJzvAUwUU7DkXxrDoFyDe7KUCOi61Ht5klq9W949CjJm5Vi8fp8Vni1S06SQZwL1rS9tFcVZoFiZyOGE72yItJy8girgqEbublEBM7BvN1KWKNluOv8tCv-dtymPQAqqcIIxGCkXKOXe3GOfqi7kOZvL0gi-Gw3uj_uYRqIg04mwSDtdihq7GSt9CCQL0ZrFqfUE7SGrLDoQ0Xux3LhjGUbURvuFQBMAvtDcCY6T_tlCx0-VeTT4myefXa-uR7McObtraaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac706e15a.mp4?token=vguQUqS6tz6qUPWiwZSqyJeGBj1EZ_7RkKgAPi3297ahIY-JKkoGcFo7vh3YUSkO3kpR-VWzLAlFBXQHJzvAUwUU7DkXxrDoFyDe7KUCOi61Ht5klq9W949CjJm5Vi8fp8Vni1S06SQZwL1rS9tFcVZoFiZyOGE72yItJy8girgqEbublEBM7BvN1KWKNluOv8tCv-dtymPQAqqcIIxGCkXKOXe3GOfqi7kOZvL0gi-Gw3uj_uYRqIg04mwSDtdihq7GSt9CCQL0ZrFqfUE7SGrLDoQ0Xux3LhjGUbURvuFQBMAvtDcCY6T_tlCx0-VeTT4myefXa-uR7McObtraaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت‌های شما از دلایل تجرد | چرا ازدواج نمی‌کنیم؟
🔹
صدای شما از چالش‌های واقعی زندگی؛ بازتاب موانعی که جوانان را از تصمیم برای ازدواج دور کرده است.
🔸
پیام های صوتی خود را به آیدی زیر ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/684490" target="_blank">📅 16:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684488">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad3ad1d78.mp4?token=jaBkf52riOp-VEgArPpkus-Mjztl0n1L8zfPBXpgiSu_OKCYFj-xfBVj2Cdt6qdPB-Re80IXOaU5HUeivayeI6U-ZUEMl8tMJ-LsC_zIsB4hY_SEAzaAf5KhJ3MbKamwariakxqzxrcAV6t2LUuKY7CDad1S8M2DOJhpGOc7RfWGSynuYg2u-f11hKnYYiKS-ay1-Zd8AFbJ3pCYW8XyjnrPX3YJRUJfCaw6urodGhpMvNPUw8KBj7DU-qGAKA1qbyCLdPsR6oqfJFdxSi3eDC3mmzt55dWBz6aLqETtWaqSQdsI2J2ucp_Eu_2FZTJZvHQcWijXaY5MLBcSpZ9LKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad3ad1d78.mp4?token=jaBkf52riOp-VEgArPpkus-Mjztl0n1L8zfPBXpgiSu_OKCYFj-xfBVj2Cdt6qdPB-Re80IXOaU5HUeivayeI6U-ZUEMl8tMJ-LsC_zIsB4hY_SEAzaAf5KhJ3MbKamwariakxqzxrcAV6t2LUuKY7CDad1S8M2DOJhpGOc7RfWGSynuYg2u-f11hKnYYiKS-ay1-Zd8AFbJ3pCYW8XyjnrPX3YJRUJfCaw6urodGhpMvNPUw8KBj7DU-qGAKA1qbyCLdPsR6oqfJFdxSi3eDC3mmzt55dWBz6aLqETtWaqSQdsI2J2ucp_Eu_2FZTJZvHQcWijXaY5MLBcSpZ9LKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر کنجکاو هستید بدانید ماشین ظرفشویی چطور کار می‌کند این ویدیو را ببینید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/684488" target="_blank">📅 16:48 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684487">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
جشن روز ملی ارس؛ شکوه یک رویداد ملی
🔹
جشن بزرگ روز ملی ارس با حضور پرشور مردم و ارسوندان، خانواده‌های معظم شهدا، مسئولان و فعالان فرهنگی و گردشگری به همت سازمان منطقه آزاد ارس برگزار شد؛ شبی که یاد شهدا، موسیقی، هنر و معرفی ظرفیت‌ های تاریخی و گردشگری ارس در کنار هم قرار گرفت.
🔹
از اجرای چنگیز حبیبیان و گرشا رضایی و رونمایی از آهنگ «ارس» تا تجلیل از خانواده‌های شهدای مرزبانی سال ۱۳۲۰ و شهدای جنگ ‌های ۱۲ و ۴۰ روزه، رونمایی از آثار فرهنگی و گردشگری و پوستر جشنواره ملی عکس ارس و اهدای ۱۵ دستگاه دوچرخه و یک دستگاه خودروی MG5 در قرعه‌کشی میان شرکت کنندگان.
@arasfz
.ir</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/684487" target="_blank">📅 16:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684486">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ترامپ به الجزیره: برای مذاکره با ایران «عجله‌ای ندارم»
ادعای ترامپ:
🔹
هم اقدامات اقتصادی و هم نظامی در مواجه با ایران «موثر» هستند.
🔹
او در پاسخ به سوال خبرنگار الجزیره، افزود که «من هیچ برنامه زمانی ندارم، عجله‌ای ندارم».
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/684486" target="_blank">📅 16:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684485">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2dd13e4d1.mp4?token=ovDlS9IzQwvRk7qP9gWsqM4XpFm9-1bImWYtrgRreioVoMVkbCiFMhIOJntwbg8wI2zTLqw6MDEJKg2MLfdn4FHH0nKu7AOM2KnNF0hbQkuv9p7mH1SxuTGmN1rdCwN2ed4b_yDqP3ymWgcsnkqyKO0vqebGWbEIMtjEI-pzSBAAze7143vMiF-TogeikfP5X0CUI1Pk2Swfs88wQ-v4QBV_sLFYHRSHEuDULgk5V7c-9G0Ygw0ZGYFP6v4SAei71R017KC0clYC_Cv3izZsMQhjPnadS8lsMgBHaa6Q5uOqnqlCdqpucHn4FNpWfoAg1-l8hkdLaim1mA6OuL9bvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2dd13e4d1.mp4?token=ovDlS9IzQwvRk7qP9gWsqM4XpFm9-1bImWYtrgRreioVoMVkbCiFMhIOJntwbg8wI2zTLqw6MDEJKg2MLfdn4FHH0nKu7AOM2KnNF0hbQkuv9p7mH1SxuTGmN1rdCwN2ed4b_yDqP3ymWgcsnkqyKO0vqebGWbEIMtjEI-pzSBAAze7143vMiF-TogeikfP5X0CUI1Pk2Swfs88wQ-v4QBV_sLFYHRSHEuDULgk5V7c-9G0Ygw0ZGYFP6v4SAei71R017KC0clYC_Cv3izZsMQhjPnadS8lsMgBHaa6Q5uOqnqlCdqpucHn4FNpWfoAg1-l8hkdLaim1mA6OuL9bvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: در بدترین وضعیت جنگ اقتصادی هستیم
🔹
ما در بدترین وضعیت جنگ اقتصادی هستیم؛ یعنی جنگ موشکی را همه می‌بینند، اما فشارهای اقتصادی شاید به این راحتی احساس نشود.
🔹
کاری که در چنین فضایی و در چنین جنگی انجام می‌شود واقعا قابل قدردانی است. شاید اگر زمان عادی بود این‌قدر نمی‌توانستیم کار کنیم؛ الآن علی‌رغم اینکه تحت فشاریم و در جنگ هستیم، این دستاوردها قابل قدردانی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/684485" target="_blank">📅 16:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684484">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZ8naRvWy9sDazKksV-VcaQkwXOexCEYsLplIRFq4jpUZEoCPPVthsvRp9QqWf0JNhakYiWYQNgxeAbtm7wbYodUYxf_OLLiCyALyKza_ZWtB4pNLtXCeKeBzsCBQ9tazUarfY4He2HJ8QCPh1H-KKDqZkSRNBoPmbAb-ondVK3P0WJlIwhxsutPDmSfFG5YjG7RUPW_wxreHWJ0k0lwo37tec64x2dPJm5eYFXoJSsa85uh3Zmy4SPefucNAgjpYVs65e-skFCq-qCvz57NcMBEN8WOuHcmFD4VmCW6jiWnmwlltggtc94YY32ElaVmQzB-DyBQRxWYOl69gLBX2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در پی انتشار ویدئوی نقشه ترور پسر رئیس‌جمهور امریکا، شبکه‌های خبری امریکا از جمله سی‌بی‌ان نیوز با انتشار فراخوانی از حامیان ترامپ خواستند برای محافظت از او دعا کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/684484" target="_blank">📅 16:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684483">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be2734fad.mp4?token=PqCEMpQe7GeEZY1gtYktMDnYM6L3tSRXBXUZpNwDBGbqh5gKfREdzRg3NuTPDbpiWP6L8ASTEc2s3hI23s1k3Z96pkwwae8-LnS9Cm91CZnSn-w1nXNU-0MDLhPqSTUYP0GD_mhvmJ3JeLei7ZRKbN7Xo_cfsS7TmyyVOT-UpLCxR52ThyVtTzolNjhToOq9TMKHHzAmopNkU-G8jTEsHguhRrwWSDZ_8cpuZ6NupBAaLHwo22qTO80WJL38t6S6_ZU0qB3mHZGH6fSFBAmW6H0tvDUuO17-I6-4HJcywtxjh-HHMZDy9Sh2R7HBVEpaX8-v-Q7yVkiD-3Z1muZT0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be2734fad.mp4?token=PqCEMpQe7GeEZY1gtYktMDnYM6L3tSRXBXUZpNwDBGbqh5gKfREdzRg3NuTPDbpiWP6L8ASTEc2s3hI23s1k3Z96pkwwae8-LnS9Cm91CZnSn-w1nXNU-0MDLhPqSTUYP0GD_mhvmJ3JeLei7ZRKbN7Xo_cfsS7TmyyVOT-UpLCxR52ThyVtTzolNjhToOq9TMKHHzAmopNkU-G8jTEsHguhRrwWSDZ_8cpuZ6NupBAaLHwo22qTO80WJL38t6S6_ZU0qB3mHZGH6fSFBAmW6H0tvDUuO17-I6-4HJcywtxjh-HHMZDy9Sh2R7HBVEpaX8-v-Q7yVkiD-3Z1muZT0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طلا یا بورس؟ بررسی یک الگوی تکراری که حتی سایه جنگ هم نتوانست آن را تغییر دهد/
تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/684483" target="_blank">📅 16:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684482">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d77a7f9cc8.mp4?token=NuZ87rE76rFfYtiqC-26TUN4x5qZu65Pr_j4h05WgHg0ML3UQHvJcK2ynjBL2q7MDw0w5fCZFqVy2AVrAvUEo8rVWbgFMt9XCEGFLg-8eO70NK2JAIigNF2BTNJWPg_EV_gwcD7bU9FVqBbAqnyTnfSq4Enmq1PGV2PM6SP_hIKIqmY76d_PkslxiSgvwfjMfvCqAS9vGsjQBNuWF3dn2UaQeAIXekjVdpIwsTPfORWelag2985sZ4GS6-0TOsk71bEZIq2KzaFDfNq0dRjDbsOZp_We3tAy_7Hxr7a7xNzyOR7ndDvDeCQZwie5OuQILJIbARIpR-5O2XcJmKeQSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d77a7f9cc8.mp4?token=NuZ87rE76rFfYtiqC-26TUN4x5qZu65Pr_j4h05WgHg0ML3UQHvJcK2ynjBL2q7MDw0w5fCZFqVy2AVrAvUEo8rVWbgFMt9XCEGFLg-8eO70NK2JAIigNF2BTNJWPg_EV_gwcD7bU9FVqBbAqnyTnfSq4Enmq1PGV2PM6SP_hIKIqmY76d_PkslxiSgvwfjMfvCqAS9vGsjQBNuWF3dn2UaQeAIXekjVdpIwsTPfORWelag2985sZ4GS6-0TOsk71bEZIq2KzaFDfNq0dRjDbsOZp_We3tAy_7Hxr7a7xNzyOR7ndDvDeCQZwie5OuQILJIbARIpR-5O2XcJmKeQSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متفاوت‌ترین تبریک تولد
!
🔹
نگار هاشمی بازیکن تیم ملی والیبال ایران در جریان دیدار با عراق، هربار که دوربین او را نشان داد تولد پدرش را تبریک گفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/684482" target="_blank">📅 16:07 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
