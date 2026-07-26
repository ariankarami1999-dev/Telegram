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
<img src="https://cdn4.telesco.pe/file/QaZrj4j7IHBWdnWc5zb17TD0_5x83v10LU0ZZ37IEEyCllzE1OPW36p5tmyuUFRnK_GjktDpjCExQiDouwLiAzT71RbCXAYblhsUvSu-CJOeW2hV5Qlz3vyOZbmQz4AUtSYrtdgBkCq7fJgcPHeyzo0xflgVSN2R4SOpjyfTWHeQr8VXZTFYgPBp0Y4r8CR_Wnf2ZRUXyM-5G7XhA7mFp6y7GFEskWlUtrE9KVdjNzXjTB5X2VbVSVgZ1Jyck7h0Vnq-bKGktv3x0SLqiBx60OT9GJyBcf9e0FMvjqHmzXUHjB4d8tMgfvzfpyO46uOAvYfST9__z-0uALpVz387RQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 428K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 11:00:43</div>
<hr>

<div class="tg-post" id="msg-19715">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCnoEbbwuvXAE5ysbkN40RR3G4aZT_h8tbobqeVQ3O5BlJNqDIIY1uPL_9QQtEC0qZZtUUubsZs69uRJ_aFFlwYHTwq3sukLIEdO3IZSpXrKDkwwZ4EHwNLsOGyTgNAW-ePonbUaMg6npBBFvOXCSxu_3B0RprS-WyS8JO560WJ5zVLn7_iUY-MJGKFZixag0fhP-5Ia9FHQOVjS0XJ_8wFt-i15Oer7XamLYIBMnF5f8Vp6hCJAOWxBeBz8DM6jf_TpwuJXYTp0XT3eWkF8AyTnahbhhg2-7qc0ubKUtkTLzhmisG3tQIZEsTe5r4l9MklEZCXAbCL6-0qypAbWUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون حداقل ۱۷ فروند هواپیمای ترابری نظامی آمریکا از نوع C-17 و C-5M و سوخترسان در حال رفت و آمد به خاورمیانه هستند
@WarRoom
دیروز خبر فیکی مبنی بر پایان نقل و انتقالات پل هوایی آمریکا پخش شده بود !</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/withyashar/19715" target="_blank">📅 10:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19714">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">امروز چهارم مرداد؛ سالروز درگذشت رضاشاه کبیر پدر ایران نوین
@WarRoom</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/withyashar/19714" target="_blank">📅 09:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19713">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">صدا و سیما :
‏ سناریوهای احتمالیِ آمریکا در مقابل ایران
سخنگوی ارتش
: یکی از راهبردهای آمریکا خروج از جنگ است البته اگر اسرائیلی‌ها اجازه بدهند.
سناریوی دوم
اینکه تحت فشار اسرائیلی ها عملیات هوایی گسترده انجام دهد. یا انجام عملیات زمینی.
‎
@WarRoom</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/withyashar/19713" target="_blank">📅 09:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19712">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">به گزارش سی‌بی‌اس نیوز، مذاکرات عمان و ایران برای بازگشایی تنگه هرمز پیشرفت‌های مثبتی داشته، هرچند رسیدن به توافق نهایی نیازمند زمان است. همزمان با سفر روز جمعه مقامات عمانی به تهران، آمریکا نیز برای جلوگیری از اختلال در این روند حساس دیپلماتیک، بمباران‌های ۱۳ روزه خود را عمداً متوقف کرد؛ موضوعی که کاخ سفید و سنتکام حاضر به اظهارنظر درباره آن نشدند.
@WarRoom</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/19712" target="_blank">📅 09:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19711">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شبکه کان اعلام کرد که اسرائیل امروز تمدید وضعیت اضطراری را تا ۱۱ آگوست (۲۰ مرداد) به دلیل اوضاع در ایران و لبنان تصویب کرد. همچنین در مورد سفر نتانیاهو به آمریکا گفت: نتانیاهو فردا به واشنگتن سفر خواهد کرد و روز سه‌شنبه باترامپ درباره موضوع ایران گفتگو خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/19711" target="_blank">📅 09:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19710">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شان پارنل، سخنگوی ارشد پنتاگون در بیانیه‌ای به سی‌ان‌ان گفت: «ارتش آمریکا قدرتمندترین ارتش جهان است و هر آنچه را که برای اجرای عملیات در زمان و مکان مورد نظر رئیس‌جمهور نیاز دارد، در اختیار دارد.»
«ما عملیات‌های موفقیت‌آمیز متعددی را در سراسر فرماندهی‌های رزمی اجرا کرده‌ایم، در حالی که اطمینان حاصل می‌کنیم ارتش ایالات متحده دارای زرادخانه‌ای عمیق از توانمندی‌ها برای محافظت از مردم و منافع ما است.»
@WarRoom
part5 final cnn</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/19710" target="_blank">📅 09:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19709">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بر اساس گفته چندین منبع‌ به سی ان ان، افراد کمی در حلقه نزدیکان ترامپ یا در داخل پنتاگون بر این باور بودند که گزینه‌های رئیس‌جمهور برای تشدید تنش، نتایج مورد نظر او را به همراه خواهد داشت.
پیش از آغاز جنگ، کین و سایر رهبران نظامی به ترامپ هشدار داده بودند که یک کمپین نظامی طولانی‌مدت می‌تواند بر ذخایر تسلیحاتی آمریکا تأثیر بگذارد(استراحت بین حملات لازمه برای پر کردن ذخایر)
@WarRoom
part4</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/19709" target="_blank">📅 09:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19708">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">به گفته یک منبع آگاه، تا بعدازظهر جمعه، دولت ترامپ هنوز در حال بررسی این موضوع بود که تشدید احتمالی تنش چگونه خواهد بود. این منبع گفت که کشورهای حاشیه خلیج فارس در گفتگوهای اخیر خود با مقامات دولت خواستار خویشتن‌داری شده‌اند، اما اذعان کرده‌اند که ایالات متحده توانمندی‌های منحصربه‌فردی دارد که در صورت تمایل می‌تواند از آن‌ها برای تشدید درگیری استفاده کند.
@WarRoom
part3</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/19708" target="_blank">📅 09:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19707">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">استیون چونگ، مدیر ارتباطات کاخ سفید، در بیانیه‌ای گفت:
«با توجه به ترکیب تحریم‌های موفقی که اقتصاد ایران را فلج کرده و ۱۳ روز پیاپی حمله به اهداف نظامی در پاسخ به تجاوزات مکرر آن‌ها، عاقلانه است که ایران برای رسیدن به یک توافق مذاکره‌شده تلاش کند. در غیر این صورت، آن‌ها می‌دانند چه اتفاقی خواهد افتاد.»
@WarRoom
part2</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/19707" target="_blank">📅 09:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19706">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یک منبع آگاه و یک مقام آمریکایی به سی‌ان‌ان گفتند که جی‌دی ونس، معاون رئیس‌جمهور، و ژنرال دن کین، رئیس ستاد مشترک ارتش، هر دو در جریان نشست روز جمعه در کاخ سفید و در حالی که رئیس‌جمهور دونالد ترامپ در حال بررسی این احتمال بود، نسبت به تشدید جنگ در ایران ابراز نگرانی کردند.
@WarRoom
part1</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/19706" target="_blank">📅 09:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19705">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ به LCI : توقف موقت حملات به معنای عقب‌نشینی نیست, برای انجام حمله گسترده علیه ایران آمادگی کامل داریم!
@WarRoom</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/19705" target="_blank">📅 09:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19704">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وزارت امور خارجه: گفتگوهای ایران و عمان درباره تنگه هرمز که در تهران برگزار شد، سازنده و مفید بود.
@WarRoom</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/19704" target="_blank">📅 08:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19703">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2743288b5.mp4?token=PXmFXVudkdvdIWIGLEytlNhIccnFoh7ebUu-SePaqBHpTjX5LmFoRA5nqRRoYE1j4O0OJ3ThMX7Bokaf9bLqbKGJDX5i_m0ZlhDQcIJDqGPZfG3IIRJEMdN6iuSah5T9DRW5yiWUsoKS_xJcGgh-jsdquJSRGkswPPaYhf7eC67KkxysRYPbP1lEMb5dJSHbLMQeaUTSQvTa5GyzHj5B_WiGZdbPnekxn79kJ9VoeFUYcBoJZ49UrUyDVcHc6lx0tsnLHHETZF7nWWmL_nHnAHjKXb6zkXC1M4NMAT42egjAO_ah73c0oW4aitv82Fl5TsClASGGs9-QyoKMMlKvnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2743288b5.mp4?token=PXmFXVudkdvdIWIGLEytlNhIccnFoh7ebUu-SePaqBHpTjX5LmFoRA5nqRRoYE1j4O0OJ3ThMX7Bokaf9bLqbKGJDX5i_m0ZlhDQcIJDqGPZfG3IIRJEMdN6iuSah5T9DRW5yiWUsoKS_xJcGgh-jsdquJSRGkswPPaYhf7eC67KkxysRYPbP1lEMb5dJSHbLMQeaUTSQvTa5GyzHj5B_WiGZdbPnekxn79kJ9VoeFUYcBoJZ49UrUyDVcHc6lx0tsnLHHETZF7nWWmL_nHnAHjKXb6zkXC1M4NMAT42egjAO_ah73c0oW4aitv82Fl5TsClASGGs9-QyoKMMlKvnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محاصره دریایی ایالات متحده علیه ایران همچنان به طور کامل برقرار است. از ۲۵ ژوئیه، سنتکام ۱۲ کشتی تجاری را که سعی در عبور از محاصره داشتند، تغییر مسیر داده، ۲ کشتی را که رعایت نکرده بودند، غیرفعال کرده و ۲ کشتی دیگر را برای اطمینان از رعایت کامل محاصره، سوار بر آنها کرده است.
اوایل امروز، نیروهای آمریکایی عملیات تأیید ورود به کشتی M/T Charminar با پرچم کومور را در دریای عرب تکمیل کردند و این نفتکش اکنون به سفر خود ادامه می‌دهد.
نیروهای سنتکام، M/T Lavine با پرچم موزامبیک را در ۲۴ ژوئیه در خلیج عمان غیرفعال کردند، پس از آنکه خدمه چندین بار تلاش کردند محاصره را نقض کنند و هشدارهای مکرر را نادیده گرفتند. این کشتی دیگر به سمت ایران در حال حرکت نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/19703" target="_blank">📅 03:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19702">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یک پهپاد در نزدیکی منزل ایتمار بن گویر، وزیر امنیت ملی اسرائیل، سقوط کرده است ، جزئیات در حال بررسی است.
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/19702" target="_blank">📅 23:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19701">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دریای قزوین
😁</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/19701" target="_blank">📅 23:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19700">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وزارت امور خارجه ایران:
ما محکوم می‌کنیم اقدام دولت اوکراین مبنی بر حمله به یک کشتی تجاری ایرانی در دریای قزوين«خزر»که امروز صبح رخ داد. این حمله منجر به انفجار کشتی و شهادت یکی از ملوانان و زخمی شدن ملوان دیگری شد.
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/19700" target="_blank">📅 23:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19699">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کانال ۱۴ : ترامپ دستور توقف تمام حملات به ایران را صادر کرد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/19699" target="_blank">📅 22:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19698">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">کانال 12 : بنیامین نتانیاهو تصمیم دارد در نشستی در کاخ سفید، اطلاعاتی درباره پیشرفت برنامه هسته‌ای ایران را در اختیار ترامپ قرار دهد
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/19698" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19697">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">زلنسکی : ما دریافتیم که ماهواره‌های روسی به تهران در حمله به مناطق خاورمیانه کمک می‌کنن
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/19697" target="_blank">📅 22:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19696">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خبرگزاری وای‌نت : قطر و عمان ،رژیم تهران را تحت فشار گذاشتند تا سازش کند و از یک عملیات تقریبا قطعی و بزرگ آمریکا جلوگیری کند
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/19696" target="_blank">📅 21:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19695">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ممد باقر : حملات ما به اهداف آمریکایی در منطقه، تا زمان تسلیم کامل دشمن و به عنوان انتقام خون کودکان بی‌گناه در میناب، لامرد و سایر مناطق، ادامه خواهد داشت
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/19695" target="_blank">📅 21:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19694">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🥛
امشب دوغ  میزنمااااااا</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/19694" target="_blank">📅 21:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19693">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ , تلفنی به یک خبرنگار از شبکه فرانسوی LCI:
اگر از ایران ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/19693" target="_blank">📅 21:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19692">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ : آمریکا «آماده حمله گسترده» به ایران است (کانال ۱۴)
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19692" target="_blank">📅 21:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19691">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19691" target="_blank">📅 21:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19690">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سخنگوی سپاه: در طی ۱۵ روز نبرد، نیروهای مسلح ایران ۱۱ فروند جنگنده و بالگرد آمریکایی را در پایگاه‌های منطقه و روی زمین منهدم کردند؛  شامل یک F-15، یک P-8، یک C-17، هشت هواپیمای سوخت‌رسان و ۱۷ پهپاد شناسایی و عملیاتی.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19690" target="_blank">📅 21:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19689">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ایلان ماسک: در سیاست زیاده‌روی کردم!
بهتر بود به جای دخالت در امور اجرایی واشنگتن، تمام تمرکز خودم را روی مدیریت شرکت‌هایم می‌گذاشتم.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19689" target="_blank">📅 21:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19688">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">رادیو و تلویزیون اسرائیل:
در حال حاضر بیش از 90 هواپیمای سوخت رسان آمریکایی در اسرائیل مستقر شدند، موشک های رهگیر پدافند به صورت گسترده در حال ورود به اسرائیل می‌باشد، هواپیماهای ترابری آمریکایی بدون وقفه وارد اسرائیل می‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19688" target="_blank">📅 21:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19687">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">شبکه
I24News:اسرائیل برای یک حمله گسترده از سوی آمریکا در پایان این هفته آماده‌سازی می‌کرد، اما این حمله اتفاق نیفتاد. تخمین‌ها نشان می‌دهد که آتش‌بس فعلی موقتی است و هدف آن فراهم کردن زمینه برای گسترش دامنه عملیات نظامی در آینده است.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19687" target="_blank">📅 21:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19686">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19686" target="_blank">📅 21:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19685">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXcLZKpXegyD9m662fXUdxgekGyMixyoBNutlf8Cqvt_yZY08UK8xnucYIPSOogBrYIAU3ANAEVveWhgvE5LE47yXzu1B3_ZWdYyFEzcGfAIZJ6gzHxqIHDAmbIdsWUGo4JTIv_6xL9jPv5RWjVlAGgOKvQueP09dEuX0C3OvObooPdbtqlvl3ilXeMtyRHO6u6adCWXlva6LPLQGKKmcXVzcBuAlrEYa2EafOhEtWI3rNqzYkvsPVOECGl4hfaziASQQSe4bMQSbjemDU6nevtxMfTMyfQ3REpb1tYq_pP15xc635Q_RTwytn9UWGHMO2CPFPZInTv3tmoLphGnTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقال مجروحان آمریکایی از اردن و کویت با هواپیمای C-17 گلوبمستر به بیمارستان نظامی آلمان؛ مقصد نهایی مرکز پزشکی لنداشتول
بر اساس گزارش‌های منتشرشده، شماری از نیروهای نظامی آمریکایی که در جریان حملات اخیر در منطقه خاورمیانه زخمی شده بودند، پس از دریافت مراقبت‌های اولیه در پایگاه‌های منطقه‌ای، با هواپیمای ترابری ـ پزشکی
C-17 Globemaster III
نیروی هوایی آمریکا برای ادامه درمان به آلمان منتقل شدند. مقصد این انتقال،
مرکز پزشکی منطقه‌ای لنداشتول (Landstuhl Regional Medical Center)
در ایالت راینلاند-فالتس آلمان بوده است؛ بیمارستانی که سال‌هاست به‌عنوان مهم‌ترین مرکز درمانی ارتش آمریکا در خارج از خاک این کشور برای پذیرش مجروحان جنگی فعالیت می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19685" target="_blank">📅 20:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19684">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19684" target="_blank">📅 20:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19683">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromَ</strong></div>
<div class="tg-text">یاشار جان سلام خسته نباشی اول از همه مرسی از زحماتی که میکشی ، من المان زندگی میکنم بعد ما رفتیم بیمارستان ارتش مخصوص کسایی که زیر نظر بیمش هستن فامیلمون عمل لازم بود قبولش نکردن گفتن تو حالت اماده باش هستیم پرسیدیم برا چی بخواطر جنگ خاورمیانه گفتن اره  هرچی خواستیم ازش جزئیات بیشتری بگیریم گفتن محرمانه هست هیچ جوابی بهمون ندادن</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19683" target="_blank">📅 20:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19682">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نیویورک پست: ایران در هفته‌های اخیر دفاع خودشو به‌شدت تقویت کرده و برای سناریو حمله زمینی آماده شده
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19682" target="_blank">📅 20:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19681">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19681" target="_blank">📅 20:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19680">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دو شرکت زیرمجموعه لوفت‌هانزا آلمان پروازهای تل‌آویو را تا سه‌شنبه لغو کردند
این تصمیم در پی ادامه نگرانی‌های امنیتی و ارزیابی وضعیت منطقه اتخاذ شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19680" target="_blank">📅 20:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19676">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سفارت آلمان و فرانسه رسما شایعه تخلیه کارکنان خود را تکذیب کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19676" target="_blank">📅 20:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19674">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19674" target="_blank">📅 20:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19673">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19673" target="_blank">📅 20:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19672">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19672" target="_blank">📅 20:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19671">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZ0f2p-Et3FqiaerXiYhqCdvlwHy9Uf0pvZfgUdijAUbBIYNeJz4q3yD1MJuFhYy8MDYsK_FV0Emsj7poLksfmnrFFdrN_8pW7pZ2qfpOxmxCxJ9n54K9RC7Hc0NWp4fcAJA35P8TAeepzct_6VmFm7WJ6DW5R13E-cvecfli4ULhMrmzfEJf9rjGzvlMdo0UUIgtNwVJdVhcs0Trr0KyXDd39vc9zYehFsngY3M8l_d2EmXDulDzpt9W3OlJIeHNRd7r35H0PfFStuft3tHicEjVMKw6-TOSaA4L_pRkszk__Uzvn871PUlFxvHE9DyKmoHm2JinlKtBPhy9B-nUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ریزه کاری هایی داره ولی خیلی سخت بود تا این بشه ، سلیقه داداش رو که قبول دارید
😎</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19671" target="_blank">📅 19:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19670">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19670" target="_blank">📅 19:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19669">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حمله به یک نفتکش در نزدیکی عربستان
سازمان عملیات تجارت دریایی انگلیس از اصابت یک پرتابه به نفتکشی در ۷۰ مایلی ساحل الشقیق عربستان خبر داد.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19669" target="_blank">📅 19:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19668">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaW8oBf3qW5xL01QIZgRjgx9xhB0ZD0SukMjyQ_DjyoOv1mBSpUOEY1F1WZIRZmm0nFGW74-iVZQYv7xMjKEWjYVEUSQBjYlAqkWHdiky2GKn7aWhynMWLI2z5s28ROJrcBnXfN_AscgFd7H_dLGX3gefyE3RgLu-juY1eJ17p1Z5K46O15QfVgPIg4ACtesswzXPfxioxxTxKlOYwPKVDZRu7G5FiGTm1p900Iqkn5bPFqJiCvHS9x0DL3yB8rkMGEtrM6cLfWpLxhRhuFj5kqHJ3FY4bykXRU-_x5S4n0KZBgh_JI30uGohIvD1tO_mX5kKSs3Ci39DI5WDDZx3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏یک هواپیمای آواکس E-3 Sentry در فرودگاه جده فرود آمد
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19668" target="_blank">📅 19:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19667">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGa3zbCSD19xBcKLGokabV6fZrP5g9FgXQjQ7Rb0DnFp2-diTMSf0Oe5D6N4iixTq54n2_qgNXlnjXW8Y7SIheL8kt94N5JFXUBxP6Ao7UuM_HDGERsVliwqWHPy9B79-Ka3DyY6iFgYbcZMQushpYDHXUJl0_dATlq1Zbo_qmlxhQZLfkUCkfjr_h-NOq2fQ-W00cdmgC3xE2K_UztUWD61v4F8xnkDmpsWUoSJP5BLzT8oLS0PfKPzWM7oYffDKJRFi6fkd8DJkuBVJczub_eW7jyfOLG57iT7XOVsXEtwQxhjSvYvMcaAXL41hB7sCEmGw7nGxn3biDYM4wsfYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶ سوخترسان هم اکنون در آسمان اردن
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19667" target="_blank">📅 18:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19666">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اکسیوس با رد خبر رسانه‌های عبری:
آمریکایی‌ها دیروز برای یک عملیات گسترده‌تر علیه ایران آماده نشده بودند، بلکه برای حمله‌ای با همان حجم و ابعاد حملاتی آماده شده بودند که در دو هفته گذشته هر شب انجام شده بود
.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19666" target="_blank">📅 18:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19665">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">به گزارش کانال ۱۲: آماده‌باش در سطح بالا در اسرائیل برقرار است؛ آنها منتظر تصمیم ترامپ در مورد آینده رویارویی با ایران هستند, همچنین شرکت‌های هواپیمایی خارجی لغو پروازهای خود به مقصد و از مبدأ اسرائیل را آغاز کردند
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19665" target="_blank">📅 18:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19664">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وای نت : ترامپ قرار بود دیشب یک حمله بسیار گسترده به ایران انجام بده ولی وسط کار نظرش عوض شد و تصمیم گرفت فعلا به ایران فرصت بده تا مسیر دیپلماتیک جواب بده!
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19664" target="_blank">📅 18:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19663">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏وزارت حمل‌ونقل قطر اعلام کرد از روز ۲۶ ژوئیه، تردد تمامی کشتی‌ها و شناورهای دریایی به طور کامل از سر گرفته می‌شود. با اجرای این تصمیم، همه محدودیت‌های اعمال شده بر فعالیت‌های دریایی لغو شده و عبور و مرور در آب‌های قطر به وضعیت عادی بازمی‌گردد.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19663" target="_blank">📅 17:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19662">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تلگراف : یک مقام ایرانی ناشناس، بریتانیا را تهدید کرد و هشدار داد که در صورت مشارکت این کشور در جنگ به همراه آمریکا، مقر نخست‌وزیر هدف قرار خواهد گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19662" target="_blank">📅 17:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19661">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وال استریت ژورنال: موشک‌های خیبرشکن ایرانی با ترکیبی از مسیر‌های پروازی، مانور‌ها و سرعت‌ها، سامانه‌های پدافند هوایی را گیج می‌کنند
این موشک‌ها بسیار ارزان‌تر از رهگیرهایی هستند که برای انهدام آن‌ها استفاده می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19661" target="_blank">📅 17:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19660">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اکسیوس: طرحی جدید میانجی‌ها به امریکا و ایران ارائه شده که شامل رفع محاصره بنادر ایران، بازگشایی تنگه هرمز و پیشنهاد دریافت «عوارض تأمین امنیت» توسط تهران از کشتی‌های عبوری است @WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19660" target="_blank">📅 17:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19659">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOnBUMId2uFIZvvPMPee384K5CQua4w-Y_evuYEFisOwL8Loz1_tHEtRRfa6w9szmVJliU6MTjDJ5b7nrCgFPMvAu2XLyTs9gMiISQPuclGa2-7aD5aZMllStvaNDOdGZOeZZVeQO9Yll5DrYiiwS2T9akQtAnjq0fxmywkAf35aJnV2bfbz3ScKvy3I36G23AEEqMqTjAInurN2CPOS1cE5bZb9_yKR9oxJFgH80mcc92CYK-kyO9S_34Q9VwK7lyF7B-ShdUvSGKI4pT7YXp4pPpCm5MMhfr5J2TK1VdJIBiLh3Xm-lFRY6kroUc__WK96OeHSPqC8COediCwepw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسال سنگین تجهیزات و مهمات به اردن فقط در همین لحظه ۴ هواپیما C17 در‌ مسیر رفت و برگشت ! نشان میده آمریکا در حال کشیدن کامل کمان «فول دراو» است
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19659" target="_blank">📅 16:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19658">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ورودی جدید
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19658" target="_blank">📅 16:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19657">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromH</strong></div>
<div class="tg-text">الان جدی جدی آمریکا قبول کرده ایران فقط تنگه رو باز کنه و پولم بگیره؟؟</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19657" target="_blank">📅 16:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19656">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اکسیوس: طرحی جدید میانجی‌ها به امریکا و ایران ارائه شده که شامل رفع محاصره بنادر ایران، بازگشایی تنگه هرمز و پیشنهاد دریافت «عوارض تأمین امنیت» توسط تهران از کشتی‌های عبوری است
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19656" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19655">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9083629166.mp4?token=kNVAbp-L9NXph_lxDaEUuhlHhYP2A6UQECfHb2xxvFX_T-q5lgIjZNZCWMPKZ5niiBknZX_s5Bspjr6pgGb8iuweSYrk7HT4N_jYfBI7SIGz1InHIWw4cDTTA6RUZAGqI-qmWxsY0fT33TiRy8dCvUSff9ccB4OBbuZYVhdyID2hrgTeXqgVVhekZu7sTEEXgXFVO99Kcxs-s2mtNsEcihqoLGBh1v9SmIzCQN1mj4HKNqdsk23G_OWcpHOiVLxAJJN1ykIt4X6pIA7-x9PKHlz07EnCQrDrjPt7wTZ_Ifc_1HYN8ihTXLp56Rky56L1-mFplbTf5ngPns-IVSXVylbySWth0uy4tbj3DDYimYGseYUU0RvEPoIvm06s9u1wlqtZPWOTbv0Leb5V9q9MGd8WdoDKasS8AhTETdUYAcHAPQOZmlgFoee6rCl7H25CbNaEiRYDrtQDoSueTm71_LXY7hi7_1K9uW23ANfBHqhvPnDJQjmY3vn0aNb-Q4uWx36MbTuzP-e2pdZYUbv2J_Nuv0DPoMysdFYeOjPzuQ6PsxrxGiXNi2itEU0cATM7dbjtobPO_E1aPJXQPWCuRHuBaKKCfUh6tx-GZeqU_c-NVLfh1XYDvgWqjdYssvKXQ5htnvk9MP7U9y24B17XvI2zaG8b0AT_nsP2qoGQUJE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9083629166.mp4?token=kNVAbp-L9NXph_lxDaEUuhlHhYP2A6UQECfHb2xxvFX_T-q5lgIjZNZCWMPKZ5niiBknZX_s5Bspjr6pgGb8iuweSYrk7HT4N_jYfBI7SIGz1InHIWw4cDTTA6RUZAGqI-qmWxsY0fT33TiRy8dCvUSff9ccB4OBbuZYVhdyID2hrgTeXqgVVhekZu7sTEEXgXFVO99Kcxs-s2mtNsEcihqoLGBh1v9SmIzCQN1mj4HKNqdsk23G_OWcpHOiVLxAJJN1ykIt4X6pIA7-x9PKHlz07EnCQrDrjPt7wTZ_Ifc_1HYN8ihTXLp56Rky56L1-mFplbTf5ngPns-IVSXVylbySWth0uy4tbj3DDYimYGseYUU0RvEPoIvm06s9u1wlqtZPWOTbv0Leb5V9q9MGd8WdoDKasS8AhTETdUYAcHAPQOZmlgFoee6rCl7H25CbNaEiRYDrtQDoSueTm71_LXY7hi7_1K9uW23ANfBHqhvPnDJQjmY3vn0aNb-Q4uWx36MbTuzP-e2pdZYUbv2J_Nuv0DPoMysdFYeOjPzuQ6PsxrxGiXNi2itEU0cATM7dbjtobPO_E1aPJXQPWCuRHuBaKKCfUh6tx-GZeqU_c-NVLfh1XYDvgWqjdYssvKXQ5htnvk9MP7U9y24B17XvI2zaG8b0AT_nsP2qoGQUJE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرچی‌ میشکنی‌ بشکن ، ولی دل مارو نشکن
@WarRoom
💃🏼
🕺🏻</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19655" target="_blank">📅 15:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19654">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نیویرک پست : آمریکا در حال بررسی طرحی برای تصرف اورانیوم غنی‌شده از تاسیسات هسته‌ای ایران است. این طرح به اعزام هزاران نیروی زمینی، خنثی‌سازی تله‌های انفجاری و استقرار یک نیروی دفاعی بزرگ در اطراف سایت‌ها نیاز دارد. سپس یک تیم کوچک از نیروهای ویژه عملیات اصلی تصرف را انجام می‌دهد. این مأموریت بسیار خطرناک و از نظر لجستیکی پیچیده توصیف شده است. گفته شده ارتش ایران تا حد زیادی تضعیف شده، اما هنوز از نظر تجهیزات از نیروهایی که مادورو را محافظت می‌کردند پیشرفته‌تر است. این طرح فعلاً در حد بررسی است و تصمیم نهایی درباره اجرای آن اعلام نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19654" target="_blank">📅 15:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19653">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">صداوسیما: اهالی جاسک اسلحه‌ به‌ دست منتظر آمدن نیروهای آمریکایی هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19653" target="_blank">📅 15:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19652">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ: نتانیاهو در 48 ساعت آینده به آمریکا سفر خواهد کرد و در کاخ سفید دیدار خواهیم داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19652" target="_blank">📅 15:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19651">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تلگراف : جمهوری اسلامی از شبکه‌های قاچاق مهاجران در کانال مانش برای انتقال برخی افراد مرتبط با نهادهای اطلاعاتی به بریتانیا استفاده کرده است.
مقام‌های بریتانیایی چند نفر مشکوک را هنگام ورود با قایق‌های کوچک شناسایی و متوقف کرده‌اند. برای ردیابی این افراد از پهپادها و برج‌های نظارتی مجهز به هوش مصنوعی استفاده شده است. بخشی از این شبکه‌ها با سپاه پاسداران و به‌ویژه واحد ۷۰۰ نیروی قدس در ارتباط بوده‌اند. یک مقام ایرانی گفته «افراد انقلابی» در لندن مستقر شده‌اند و مسیرهای قاچاق را از موشک‌ها مؤثرتر دانسته است.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19651" target="_blank">📅 15:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19650">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">زلنسکی : ما با حملات دوربرد در دریای خزر  از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی به نتایج بسیار قوی دست یافتیم.
از این نتایج متشکریم! افتخار برای اوکراین!
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19650" target="_blank">📅 14:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19649">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">حمله عربستان به مأرب و الجوف در یمن
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19649" target="_blank">📅 13:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19648">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وای نت به نقل از مقامات اسرائیلی: بعد از آزادسازی تمامی گروگان ها، دست اسرائیل برای انجام حذف هدفمند در غزه زیاد شده و اینکار با شتاب بیشتری انجام خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19648" target="_blank">📅 13:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19647">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الجزیره : چراغ سبز عراقچی به شروع مذاکرات
عراقچی: پس از بروز تنش‌هایی در هرمزگان، در جریان مذاکرات سوئیس، تصمیم گرفتیم یک خط ارتباط مستقیم ایجاد کنیم تا از بروز سوءتفاهم‌ها جلوگیری شود.
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/19647" target="_blank">📅 13:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19646">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرده است که گزارشی درباره وقوع یک حادثه میان یک نفتکش و نیروهای نظامی مهاجم در خلیج عمان دریافت کرده است @WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19646" target="_blank">📅 12:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19645">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1fWLU2EDeEz-bMSbpPzrkj0r5zMdekQak7WwDW8KDgLrDG4PBkOU4DGln7Kc-unsfM-AnO05GgzFUnuQNlyQ6nWBO79uOcJU-BmbJbu4J5Vc9umFWU52BZ73JIfqJoIZNa0HAQikfWy4BiVLQ77HGuBcAQ8nfZhrJG-Bfsuwb2HcH8QOknD-WkLzkykLupf-9qt9Q8ckeuTJRojTwLyiTAU2DxjuxqsFqpKCCgXYLbqVkgflcpUL8bc5L-5y0Au7ct7wMD5crLVlgaJZ24E3BvMfsmgHFJrxQunAhHZTl_JsrbzZP27F2AZqK8NbEEdAQ5js5jv191BZBkhezlQqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرده است که گزارشی درباره وقوع یک حادثه میان یک نفتکش و نیروهای نظامی مهاجم در
خلیج عمان
دریافت کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19645" target="_blank">📅 12:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19644">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19644" target="_blank">📅 12:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19643">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIPIUt3tSgKp2ZfcAIoiMjOTyFPE6siLDNR8k_CZ1CyGpWFKqiRd0_-FvNWxj3Wp1RIZhnEhtnFBAyRXp_j59VPfgZ2w0ZB-qhyYFsP4IA_uISb1LsW5YhHDWrsBQ-kiJhVNr39TFys8rIKflcpSur3L4kIOOB_1qELGpooEnHu7MIYRcUyPooGgc-NQRrkHANHEnxgi1xmGwIknhKpK3_bJaO9hYBUeNJ5q5CGD2__nAaRCWs-8HbxBzOZFALMCTjs1vV9S6B0XuLD01vMILnzv7QTnreKwSdAH-mILzLyliGlXSI4j-8aSBbLVcq9ag1ZMGb9WJWYpdf9omR6vnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین لحظه برای اولین بار‌ آشکارا یک هواپیمای
C-17 Globemaster III
یکی از مهم‌ترین هواپیماهای ترابری راهبردی نیروی هوایی آمریکا و ستون فقرات جنگ با توانایی حمل ۷۷ تن بار در حال انتقال  تجهیزات/مهمات احتمال زیاد برای کرد ها در اربیل عراق است
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19643" target="_blank">📅 12:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19642">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فاکس نیوز: جی دی ونس امروز در جلسه شورای امنیت ملی در کاخ سفید شرکت نکرد
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19642" target="_blank">📅 10:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19641">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سی‌ان‌ان: پس از ۱۳ شب پیاپی ، روز جمعه هیچ خبری از حمله به ایران از سوی سنتکام منتشر نشد
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19641" target="_blank">📅 09:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19640">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7weGvzfEoWOVGadmM60yJ9F6qEJlogX00HrOIj7Uxz2n3u34am1prJJec-X2xRlE8i3XX-stBF47ogEuAKHE0N3lAxyNlf0zSNAlZIOkPOodmXSOdDvjalIf6nQk2hQLg4cWj5YMMeUkXdm_OAGMNr7HHCGYGBdmbK3Qdw57LgBeC0hxmAHJn2OCZaypi9Lqh3NJoDSx45COHOdmXhl-gjswIvURPyLwlZXZGKK6CtqZddFwi9bBBfJw55K6kI5aiPmezdRi6uUqNO1qPJJi9HIORme4iqcYu-42gdiijdIYQ8uCROF00qesCh2hvDGVIRKuMMC_-NyeWWAFqf73Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : عکس باراک راوید خبرنگار ارشد آکسیوس به همراه تیم این خبرگزاری در مراسم شام کاخ سفید که بخش بزرگی از اخبار این جنگ را پوشش میدن و ما رو سرویس کردند ، دیشب اصلی ها نبودند که حمله رو پوشش بدهند ، در جنگ آمریکا و اسرائیل با ایران، رسانه‌ها فقط نقش اطلاع‌رسانی نداشتند، بلکه به یکی از میدان‌های اصلی نبرد تبدیل شدند. انتشار سریع اخبار، تصاویر، عملیات روانی، روایت‌سازی، جنگ اطلاعاتی و تلاش برای تأثیرگذاری بر افکار عمومی، همگی بخشی از این نبرد بودند. در چنین جنگی، گاهی یک خبر یا روایت می‌تواند به اندازه یک حمله نظامی بر روند تحولات اثر بگذارد
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/19640" target="_blank">📅 09:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19638">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5168a521.mp4?token=UQnMjgKBOGbF3iKn3HyFEhYw1u3WOnnri1yJWJx8WX2Tbpo1pOUF5Wij7pzrFlhj-FCEl6yON2AcfvdUrWozFNaa2BzPL1qEUCFR_ekUurtRG5qRmAciDKp2mSJz6sjwxlrvdHYqwWARHzRayP_idyBjtZHVD3ASpSzEkIZTQBxRSKzwDzkKx57bYDxaq_ugoVkkEtIqdULvb-crt4iRuxZ_Pn1C-6xMscCtYl5_4iCfxFN2DR-hk2blJZMy3vCuBmxnA68wgzAxEbFUjbdWw_-VC-I7feCqgvehJYomTi5qogZnF34Dggy__h5y3mUlBGMao1-UggwWsoQdkWghDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5168a521.mp4?token=UQnMjgKBOGbF3iKn3HyFEhYw1u3WOnnri1yJWJx8WX2Tbpo1pOUF5Wij7pzrFlhj-FCEl6yON2AcfvdUrWozFNaa2BzPL1qEUCFR_ekUurtRG5qRmAciDKp2mSJz6sjwxlrvdHYqwWARHzRayP_idyBjtZHVD3ASpSzEkIZTQBxRSKzwDzkKx57bYDxaq_ugoVkkEtIqdULvb-crt4iRuxZ_Pn1C-6xMscCtYl5_4iCfxFN2DR-hk2blJZMy3vCuBmxnA68wgzAxEbFUjbdWw_-VC-I7feCqgvehJYomTi5qogZnF34Dggy__h5y3mUlBGMao1-UggwWsoQdkWghDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه تیراندازی در ضیافت شام رئیس‌جمهور ترامپ در کاخ سفید @withyashar</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19638" target="_blank">📅 09:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19637">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کلش ریپورت : فرماندهی مرکزی آمریکا امشب هیچ حمله‌ای علیه ایران انجام نداد؛ احتمالاً به‌دلیل برگزاری شام انجمن خبرنگاران کاخ سفید و سخنرانی ترامپ در این مراسم.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19637" target="_blank">📅 09:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19636">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ در مراسم شام انجمن خبرنگاران کاخ سفید (WHCA):
«برای مثال، در دوران دولت من، آن رژیم(خامنه ای اول)که زمانی همه از آن می‌ترسیدند و بی‌وقفه به آمریکا حمله می‌کرد، سرنگون شده است. رهبران سابقش برکنار شده‌اند و حالا توسط یک دیکتاتور گِی (خامنه ای دوم) اداره می‌شود و با اختلافات داخلی دست‌وپنجه نرم می‌کند. اما من به نوبه خودم برای باری وایس در CBS News بهترین‌ها را آرزو می‌کنم.»
﻿
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/19636" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19635">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92de2ca506.mp4?token=v47TrU2u5Yu3e-PCQF29w9QyRmkqdavT4fqWy-Ja_DymO_DMvNsJMNdhsT25fgZ80qEbXAEOhyZGlVIhIl7Ioe_1JXVXSGYKjudk1Vq7cSeHbykESdacCN5jHLPqbPBg_O4rYfMptV9Xfdsr_d_tT-e9OJeds2MTJo_ohD0f4mCP46kAs7zPXpc_E_h0gLk3uEDja7rxaCM-LO90aC9dVOGOivmduzL41RHRGJ47HX1V7xDJgF2uemywtIsUjtsCHRtC7HN8kHjqYO1_TS0EVVPtdmYQXbVBLckyEaD3p-SX95ShRNZ4uddOJtUNTZpFRpy_MISgvSnDH9vyDQsc6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92de2ca506.mp4?token=v47TrU2u5Yu3e-PCQF29w9QyRmkqdavT4fqWy-Ja_DymO_DMvNsJMNdhsT25fgZ80qEbXAEOhyZGlVIhIl7Ioe_1JXVXSGYKjudk1Vq7cSeHbykESdacCN5jHLPqbPBg_O4rYfMptV9Xfdsr_d_tT-e9OJeds2MTJo_ohD0f4mCP46kAs7zPXpc_E_h0gLk3uEDja7rxaCM-LO90aC9dVOGOivmduzL41RHRGJ47HX1V7xDJgF2uemywtIsUjtsCHRtC7HN8kHjqYO1_TS0EVVPtdmYQXbVBLckyEaD3p-SX95ShRNZ4uddOJtUNTZpFRpy_MISgvSnDH9vyDQsc6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به روزنامه‌نگاران:
وقتی من بروم، همه شما ورشکسته خواهید شد. مدل کسب‌وکارتان تمام می‌شود.
وقتی من نباشم، شما ورشکسته خواهید شد. کسی برای گزارش دادن وجود نخواهد داشت.
هیچ‌کس به دیگری اهمیت نمی‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/19635" target="_blank">📅 08:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19634">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">از شاهزاده سلطان عربستان هم سوخترسان داره بلند میشه… @WarRoom
🚨</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/19634" target="_blank">📅 04:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19633">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zp-hYVjlnfWTYq47L9qLNRGvhQxbAWsaTG1_3lXnRESMVwqpeS1yVr66lXKIKWRS0Y8_DVL3kj3Vulsy6JxQO2ByW0GkGOGK2uWIEi0BDgOg4_ywk8D6-SxJDiYuT7VtqVl2tzvOYg6BeUN4ToUKBLbFRKFJ0K_Z6QbyGrB6IiYdLe3IgA8si4WgD18sms3ywLoTPnqE3caMYWZYc1alwybYt7jrJDizHY59fk-niBukOAOryUT7AGCbL1qyyru_5EAHNTORG31zdBPoVobBXGfabo6959EUc-fv7WkAQSA81dTjlnNncAaZ94gccRwWSCuqkKkP2L83wqbgpWfC5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعالیت دو هواپیما چند منظوره بوئینگ پی-۸ پوسایدون
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/19633" target="_blank">📅 04:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19632">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ششمین سوخترسان رو بانده پروازه در  اسرائیل @WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/19632" target="_blank">📅 03:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19631">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وال استریت ژورنال: ترامپ به برخی از نزدیکانش گفته است که معتقد است
از طریق یک بمباران تهاجمی و جهنمی، جمهوری اسلامی را در هم بشکند.
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/19631" target="_blank">📅 03:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19630">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پنجمین سوخترسان از اسرائیل بلند شد @WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/19630" target="_blank">📅 03:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19629">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نیویورک تایمز : نشست چگونگی حمله به ایران با حضور ترامپ داره انجام میشه و شروع شده
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/19629" target="_blank">📅 03:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19628">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">با فاصله بلند شدن ۴ رمی هم داره تیک آف میکنه  @WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/19628" target="_blank">📅 03:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19627">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اوه اوه هواپیما جاسوسی ریوت جوینت هم از خانیا یونان داره بلند میشه ! @WarRoom
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19627" target="_blank">📅 02:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19626">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19626" target="_blank">📅 02:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19625">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQv8qsEYVFqHFPfjze9aNkHVFrZBKZRatvUvWlXhDbGa0DaI1gTwz6ZzYZGtTvT78oTB-aSBjA7oCt-IxDrXG1jhCGek8tg30FJBgRvxfO5HMOJ2dpUDCqaCIqDsH93IYApDvIXsIv9Fbvo3wrF7hw9Y1LYk6xveoCLjlVkyc-vy88RWQPO5SM7vz0mgANixo5QwFObaNazUtfquuPQnzlooqWX_L4gW4DDYV9P4oObmgQAkBeN8LbKHLvxh3Khm4bsAwK5--eDX8wokM8zqVimzSI-NIRtwcdm5SKtuEQU1LEmLjLI8MQEQJKOdIUx_UV9ZtBd9bgdGrjIusEPYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه هواپیما جاسوسی ریوت جوینت هم از خانیا یونان داره بلند میشه !
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19625" target="_blank">📅 02:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19624">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkY9muygMgC0IIeJULcaILv4SvycVVpbjy40TFcYizYki0mHqt60dUonTAiL8TsMzAeuNfInRmHRdJuAFvts13VnYaoaabONI0Fji927Uq8GiMQxcLEDNARu3tl6_UbrlYTcOfhR5ZJiugrHCD8WGYi4JgcIQHqFl-zkRwv3LSEonvLbH2qg9WD7yCPJtFw6MU1qZ9-PDvlpudN9PNvsN2o-wpPW03a8Jg0FktUwR9MM_9StNcgB6I9yOlWadqbZfBqiQi-vF8Deu5pzA0DTJFDl4ZtygF1WPPQRuqpZmaeDs34_eIkSrtVVH1_LeMXQoeuVRMLxv7v-2Bbpwu2QLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از شاهزاده سلطان عربستان هم سوخترسان داره بلند میشه…
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19624" target="_blank">📅 02:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19623">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هاآرتص
: تل آویو می‌خواهد تهران را به حمله پیش‌دستانه علیه اسرائیل سوق دهند و در نتیجه برای پاسخ اسرائیل، مشروعیت بین‌المللی فراهم شود.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/19623" target="_blank">📅 02:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19622">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxdDjImWTw2GBCJtX0l_7zDPhZPqm-E1fpgWj7cLCipChE3rN0e3bswuUKO_s9FxLhBEQ4w94BsJgXkuIyf25OO5vwvg2QI73w5Lfo2FZ7hFOIsLUkmQ0FWa1ZSXkoUj7R14IqNpprEusDN3VkNolYBE9I_6URYrqnt_BHanoweGYihBS-rgsXpQ8VJSLp_vAZi4nMGXY3A3y8dEHGmeb19wh_Di2-WPvbyl6s786Miz4MdYDJwpTIppA0w_5IQtNZfLVWogYzPvfiXB9FwXw-WWe_abV9aTwD32T8ikmYKnE6BuKd1STHfoPhXx_p0j8RQHyKKo5Yd0vOtaKG409A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با فاصله بلند شدن ۴ رمی هم داره تیک آف میکنه
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19622" target="_blank">📅 02:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19621">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">۴ سوخترسان دارن از اسرائیل بلند میشن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19621" target="_blank">📅 02:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19620">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اتاق جنگ با یاشار : حدود ۱۵ دقیقه دیگه میشه زمان حمله دیشب
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/19620" target="_blank">📅 01:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19619">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خبرنگار کاخ سفید: سنتکام گزارش داده بود بعضی اوقات ما به ایران حمله نمی‌کردیم ولی میدیدیم که کلی موشک در آسمان به طرف ایران میره، بعد می‌فهمیدیم که کویت و بحرین و عربستان و … در حال حمله به ایران بودن ولی به طور رسمی اعلام نمی‌کردن
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/19619" target="_blank">📅 01:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19618">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آسوشیتدپرس : ارتش آمریکا یک کشتی تجاری را در دریای عمان توقیف کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19618" target="_blank">📅 01:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19617">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19617" target="_blank">📅 01:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19616">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کلیسای جامع ملی واشنگتن اعلام کرد مراسم یادبود سناتور لیندزی گراهام در ۲۸ ژوئیه(۶مرداد) برگزار می‌شود. این مراسم با حضور خانواده، دوستان، همکاران سیاسی و رهبران ملی برای بزرگداشت زندگی و چند دهه خدمت عمومی او برگزار خواهد شد. دونالد ترامپ نیز در این مراسم…</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19616" target="_blank">📅 01:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19615">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19615" target="_blank">📅 01:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19614">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">علی عراقی ریدم تو سرت به تو نمیرسه از چنل بدزدی ، فقط برای ایرانی‌ها آزاده
⚠️</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/19614" target="_blank">📅 01:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19613">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19613" target="_blank">📅 01:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19612">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkLAOXURRxwyVdijZx6xo5zvoR0E4wz7IaFzMip85rshHHWajXT-R1cLkGLLeWXUXwpFjmk3WLS-I_QWudyuyS5TyK_3i4taUh1sLIVMMbWQquGOuOUFa3yjpGwj3r1kZBCBVbbwszeOd6PjY70dJAUULeBvOoLVVjw_MJ51H1fBHqGLCEGy0nJA99IyZSyGCCyCk06osR1A3uEamYHbBXzf1PVNIyU8PzaAMlfRtciBj20aG7WkRN9JTzy11aCruxJWm72QPWY0J1i_PR3uGCN0qBVi0vFp3sAVImJvmiVgBJte3YRud7xN-w7p6vEWtg2LlEpCQWU3kqqPJsoNfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیریک الان
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19612" target="_blank">📅 01:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19611">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">@WarRoom
کارمند</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19611" target="_blank">📅 00:52 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
