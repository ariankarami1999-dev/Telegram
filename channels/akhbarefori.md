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
<img src="https://cdn4.telesco.pe/file/j_MuSm4VCHnWYJY9oh6ywNqTDEVTm1ZuWZRuM19vddntOUWwPSv48URmqGAMyA7xCzrHIdaIPx_WtKqLxKn8kHnZWg1mthim-TxL-Ipwn4zBjTzsDFp1ZI3OLyW9b8rtuIdJGQHBQMqFQRehbOs9amQu1slc6rWZyUyIwJEzYbRCHPHZsknk_hcSIXlBNqnDV_XD0KlhTWhsGs6adA6V7GuPVfTkZvGDs8xQwNeLG29jJHVxxD5ZHtTByHGvNkn85dmVKcW5UXv3NfiOJe1IwCzVrPhRCbWqZPi7hhY-lPki1fHzn5V-xcy6N-YEmDYaU3Z0kU3IKTz1LXCMG2OSjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.44M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 22:31:47</div>
<hr>

<div class="tg-post" id="msg-686333">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
بلومبرگ: ترامپ عملاً با بی‌اعتنایی جهان روبه‌رو شده است، چین عقب ننشسته، برخی ارتباطات بانکی ایران در امارات ادامه دارد و پروازها و تجارت با چند کشور برقرار مانده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/akhbarefori/686333" target="_blank">📅 22:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686332">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
یک پهپاد آمریکایی در آسمان‌ خمین سرنگون شد
🔹
یک پهپاد MQ9 آمریکایی با سامانه جدید پدافند کشور سرنگون شده است.
#اخبار_مرکزی
در فضای مجازی
👇
@akhbar_markazi</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/akhbarefori/686332" target="_blank">📅 22:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686331">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در اربیل عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/686331" target="_blank">📅 22:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686330">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
یک مراسم عروسی در سیریک هدف ترکش های حمله وحشیانه دشمن آمریکایی قرار گرفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/686330" target="_blank">📅 22:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686329">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
دقایقی پیش حمله دشمن آمریکایی به فرودگاه جیرفت
🔹
اطلاعات تکمیلی منتشر می‌شود  #اخبار_کرمان در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/686329" target="_blank">📅 22:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686328">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
حملهٔ دشمن آمریکایی به منطقه‌ای غیرنظامی در کوهستک
استانداری هرمزگان:
🔹
دشمن آمریکایی در حملهٔ وحشیانه به خاک کشورمان منطقهٔ مسکونی کوهستک را مورد حمله قرار داد.
🔹
اخبار تکمیلی متعاقبا اعلام می‌شود.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/686328" target="_blank">📅 22:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686327">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در اربیل عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/686327" target="_blank">📅 22:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686326">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHY4Pk6oe2XIIxK47omY9ER21yqLVeKx9dgYbkzbZRFVAGCszk8hrrIEOyxwUzjfG65MkzJBXJWS46rWgX0MTlveJyo4zqI_Okc4qUaU2mAAdIjyjT7n7QWw_YJPwIl-muCRe-aSaD_6_Yva6Zy2c-toE1c3XQeuRvDwsyDBUEHHFCEbp-K_2nL9_MPrb7XvO7QgPRVv4h7VU2Ja6LMvObUYeoZoSJIIeFQLl5Gq0tNb8GDOafOFJx_9d3fRY0gfIfyl7PjRKsXbM-OPk-oPGfLEWRvd-xHSg56h7KFls4Z3nTqV5_uPxoSJgOfuJEmf2N_JXsDEOeOnna4Bpnho7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت ایران در غنا در واکنش به حملات مجدد امشب آمریکا: یک ساعت پیش، اشتراک دوباره تمدید شد
🔹
آمریکا همچنان وفادارترین مشتری ما برای چشیدن طعم «تحقیر ساخت ایران» است، البته مشتریان وفادار، پاداش این وفاداری را به صورت ویرانه‌ها تحویل می‌گیرند.
🔹
سفارش به‌صورت هوایی ارسال خواهد شد. انگار بعضی مشتری‌ها فقط ساخته شده‌اند که بها بپردازند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/686326" target="_blank">📅 22:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686325">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07956f8e14.mp4?token=IxdTiELVcG1E9TRzkqCns_mFwPhl3rauhT3EGLxz7MaQkQ0Jsr5n0IjaPLf0WNJMAYHCDFcUezbo65l6Xp2VD8c7NGaNQnAPybAAZzLpH5ldia3N-_r0V97mspKaqypEhXcSr15xoZAwd__-I3jjGOZ-l_eAv64NVyIG-NU-5Rtj_xVLi98EAtHKl-Icy4lceHDZTssYIUE6ZUOo73_yeuiSXvVvAUyVoZWwEnt7TdNYHE0h-MkXntMtKUFLFIttVJM4c_nwWgrftkX4GYvhxB9dm8g5PgNNqfN4Fej5jD5lblZveLpuijEsIVrvuhGsiuKCcAo9Pk_AUeAbTzBN2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07956f8e14.mp4?token=IxdTiELVcG1E9TRzkqCns_mFwPhl3rauhT3EGLxz7MaQkQ0Jsr5n0IjaPLf0WNJMAYHCDFcUezbo65l6Xp2VD8c7NGaNQnAPybAAZzLpH5ldia3N-_r0V97mspKaqypEhXcSr15xoZAwd__-I3jjGOZ-l_eAv64NVyIG-NU-5Rtj_xVLi98EAtHKl-Icy4lceHDZTssYIUE6ZUOo73_yeuiSXvVvAUyVoZWwEnt7TdNYHE0h-MkXntMtKUFLFIttVJM4c_nwWgrftkX4GYvhxB9dm8g5PgNNqfN4Fej5jD5lblZveLpuijEsIVrvuhGsiuKCcAo9Pk_AUeAbTzBN2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری که گفته می‌شود مربوط به پرتاب یک موشک بالستیک از تبریز به سمت پایگاه‌های آمریکایی در پاسخ به تجاوز امشب این رژیم است
./ فرهیختگان
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_sharghi</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/686325" target="_blank">📅 22:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686324">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
علی بازگشا، سخنگوی پرسپولیس در گفتگو با خبرفوری:  بازی خوبی قبل از دربی داشتیم و از نظر روحی و جسمی آماده‌ایم
🔹
خوشحالیم استقلال هم با شرایط خوب به دربی رسیده و امیدوارم شاهد بازی خوبی در اصفهان باشیم.
🔹
درباره داوری صحبت نمی‌کنم، اما نکاتی را به داور منتقل کرده‌ایم و نگرانی‌هایی در فضای هواداری وجود دارد.
🔹
تارتار تیم را هجومی بسته؛ بازیکنان دوندگی بیشتری دارند و تیم از بالای زمین پرس می‌کند.
🔹
نقل‌وانتقالات زیر نظر تارتار بوده و بیفوما با حضور او تبدیل به بازیکن متفاوتی شده است.
🔹
تارتار تحت تأثیر جو فضای مجازی قرار نمی‌گیرد و هر بازیکنی را که بتواند به تیم کمک کند، به ترکیب اضافه می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/686324" target="_blank">📅 22:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686323">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
بقائی سخنگوی وزارت امور خارجه: هشتاد و هفتمین سالگرد آغاز جنگ جهانی دوم، فرصت عبرت‌انگیز از درس‌های تاریخ است؛ عادی‌سازی قانون‌شکنی بزرگترین تهدید برای صلح و امنیت بین‌المللی است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/686323" target="_blank">📅 22:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686322">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6jCYmYqZZUMo24TaJ7LWMKP2mzlYOGWO-A8NiIgyv35oRe9lseMb8vZt10ZoJO8NEuJY6soR7wFWOFwmrmomp6Ff-bc4N-0ev8-5oX0MfqTNHNOIDtTehtsPja3NrZaFKsR3dJQekN7HuVLtNg54B9g5HXeJxx6swX1i6ttH_EQHMAd5Ab8HnrQIz0QoM1vF5Q7n6W0YvsV5jNS4UfumPE94y755GSO7FBSYYzQB59lZMYgX4NMrapJ8vwtOfMNPLmZHGpjRj9VZOISdf_qNQrdFpRnkFf5ObgB1pqpRaJSdSyqLReFQKLWjHzYNquU2bcmAcVAAVR22q1euZ-5Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت ایالات متحده هشدار امنیتی برای شهرهای ابوظبی و دبی صادر کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/686322" target="_blank">📅 22:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686320">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3bee3a53.mp4?token=tsVlP7Fr7vu9Vv0HKg7vt5Iwjak57JauawiMZyIwdeU3UsHjTNPAkqHyh-jO50zuidyG2verR664HDPPdtl5WG8mP_vlxA_CYhHrrxGETnl_-ikW8YKvBucB6dGvU5xx2qdnQyIjlFaAiJ_x8Pdbvb5YUnt2GzPpUWe3BMtNfsLvD12Awb0feLscFc4jYOe0aE-Offp_Nx6xi0js5cDXnL8IqD0kX-DG-lpytaoZOO9By-xqH-zNwOGJ4CZMRP0HS3xVTqdPabcQVZANQNgMVZwbjp5y16acsCgPciy7UpcCy6MU9CN2Szw76e49WkIS0cCq7AX6vLb-Tr2bbnR5Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3bee3a53.mp4?token=tsVlP7Fr7vu9Vv0HKg7vt5Iwjak57JauawiMZyIwdeU3UsHjTNPAkqHyh-jO50zuidyG2verR664HDPPdtl5WG8mP_vlxA_CYhHrrxGETnl_-ikW8YKvBucB6dGvU5xx2qdnQyIjlFaAiJ_x8Pdbvb5YUnt2GzPpUWe3BMtNfsLvD12Awb0feLscFc4jYOe0aE-Offp_Nx6xi0js5cDXnL8IqD0kX-DG-lpytaoZOO9By-xqH-zNwOGJ4CZMRP0HS3xVTqdPabcQVZANQNgMVZwbjp5y16acsCgPciy7UpcCy6MU9CN2Szw76e49WkIS0cCq7AX6vLb-Tr2bbnR5Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه‌ هدف قرار دادن و سرنگون کردن یک هدف متخاصم در آسمان ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/686320" target="_blank">📅 22:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686319">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سخنگوی دولت : نمایشگاه
#الکامپ
بی نظیر است. مهاجرانی: جوانان ایرانی همه محدودیت ها را دور می زنند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/686319" target="_blank">📅 22:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686318">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجار در عسلویه
🔹
فرماندار عسلویه از شنیده‌شدن صدای انفجار در این شهرستان خبر داد.
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/686318" target="_blank">📅 22:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686317">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
عملیات قاطع نیروهای مسلح ایران در پاسخ به دشمن تروریست آمریکایی آغاز شد
🔹
پایگاه‌ها و منافع آمریکا در منطقه زیر ضرب موشکها و پهپادهای ایران قرار می‌گیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/686317" target="_blank">📅 21:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686316">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
شلیک موشک‌های ایرانی به‌سمت مواضع دشمن
🔹
مشاهدات میدانی برخی خبرنگاران از شلیک موشک‌ و پهپادهای ایرانی به‌سمت مواضع دشمن حکایت دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/686316" target="_blank">📅 21:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686315">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
گزافه‌گویی ترامپ در مصاحبه با فاکس‌نیوز: اگر ایران حملات اخیر آمریکا را تلافی کند،‌ دوام نخواهد آورد
🔹
توافق با ایرانی‌ها حتی ارزش کاغذی که روی آن نوشته شده را هم ندارد و ما به آنها فرصت‌های زیادی دادیم. #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/686315" target="_blank">📅 21:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686314">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هر جسارتی تاوانی دارد ...
🔹
آمریکا دوباره با سکان‌دار نابخردش، طمع حمله به ایران کرده، سکوت در برابر زیاده‌خواهی ترامپ نه‌تنها زخم گستاخی او را ترمیم نمی‌کند، بلکه جسارت دشمن را دوچندان می‌کند.
🔹
تجربهٔ تاریخی گواه است که عقب‌نشینی تنها بر طمع متجاوز می‌افزاید. آنکه مرزهای عزتِ ملتی را نادیده گیرد، باید بداند که گریز از تاوانِ اقدام خویش، محال است.
🔹
هجوم به ایران، عبور از خط قرمزی است که بازگشت از آن، به‌سادگی خیال خام متجاوز نیست.
🔹
هر گونه تعرض به حریم این سرزمین، هزینه‌هایی سنگین و جبران‌ناپذیر در پی دارد. هزینه‌هایی که نه‌تنها دامن عاملان، که تمامیتِ نظم منطقه‌ای را درگیر خواهد کرد.
اما پاسخ ایران، هرگز شتاب‌زده و هیجانی نخواهد بود، بلکه با ترازوی عقل و در چارچوب مصالح ملی سنجیده می‌شود.
🔹
جمهوری اسلامی ایران، با درک کامل از نقاط آسیب‌پذیر دشمن، قدرت محاسبه و واکنش متناسب را داراست.
این نه تهدید، که اعلام ظرفیت هوشمندانه‌ای است برای حفظ بازدارندگی. رویکرد ایران، مبتنی بر سنجش دقیق هزینه‌فایده است. تا هر گونه اشتباهِ محاسباتی طرف مقابل، پاسخی متقارن و کوبنده، اما حساب‌شده بیابد.
🔹
عزت ایران، در هیبت واکنشِ به‌هنگام و تدبیرآمیز اوست؛ واکنشی که فارغ از غرورِ کاذب و خشم زودگذر، با ثباتِ راهبردی، پایه‌های هر گونه زیاده‌خواهی را فرو می‌ریزد و به متجاوز می‌آموزد که تعرض به این سرزمین، نه صرفاً یک اشتباه، که فاجعه‌ای بی‌بازگشت است.
تاریخ، شاهد صبر راهبردی ملتی بوده که هرگز بهای عزت خود را نادیده نگرفته است.
#سرمقاله
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/686314" target="_blank">📅 21:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686313">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
دقایقی پیش حمله دشمن آمریکایی به فرودگاه جیرفت
🔹
اطلاعات تکمیلی منتشر می‌شود
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/686313" target="_blank">📅 21:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686312">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
گزافه‌گویی ترامپ در مصاحبه با فاکس‌نیوز: اگر ایران حملات اخیر آمریکا را تلافی کند،‌ دوام نخواهد آورد
🔹
توافق با ایرانی‌ها حتی ارزش کاغذی که روی آن نوشته شده را هم ندارد و ما به آنها فرصت‌های زیادی دادیم.
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/686312" target="_blank">📅 21:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686311">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
حمایت مالی پارک فاوا از شرکت‌های فناور؛ از لیزینگ تا خرید دین
🔹
دکتر مافی، رئیس پارک فاوا، از برنامه این مجموعه برای بازارسازی و توسعه بازار شرکت‌های فناور و دانش‌بنیان حوزه فاوا خبر داد.
🔹
به گفته مافی، با همکاری صندوق‌های پژوهش و فناوری عامل پارک، قراردادها و تفاهم‌نامه‌های منعقدشده در نمایشگاه‌ها از طریق ابزارهایی مانند تسهیلات لیزینگ و خرید دین مورد حمایت مالی قرار می‌گیرند.
🔹
او همچنین اعلام کرد تاکنون به ۱۵۰ واحد فناور خارج از پارک و ۸۰ واحد مستقر در پارک تسهیلات پرداخت شده و برای حمایت از شرکت‌های آسیب‌دیده از شرایط بحرانی نیز تسهیلات سرمایه در گردش ویژه جنگ و بحران اختصاص یافته است.
🔹
مافی ابراز امیدواری کرد با توسعه شبکه‌سازی و بازارسازی، شرکت‌های فاوا از شرایط بحرانی عبور کرده و نقش مؤثرتری در تأمین نیازهای فناورانه کشور ایفا کنند.
▫️
کانال تلگرام فاوا
https://t.me/ICTPark_Newsline
▫️
مشروح خبر
khabarfoori.com/fa/tiny/news-3242044
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/686311" target="_blank">📅 21:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686309">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
در حملات امشب تاکنون کسی آسیب ندیده و زیرساخت‌ها نیز سالم هستند/صداوسیما
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/686309" target="_blank">📅 21:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686308">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی مجلس: عبور از تنگه هرمز، منوط به پرداخت غرامت جنگی شد
🔹
مطابق ماده هفت طرح مدیریت هوشمند تنگه هرمز  تمامی کشورها، سازمان‌ها و اشخاص حقیقی و حقوقی که در دوران جنگ خساراتی به جمهوری اسلامی ایران۷ وارد کرده‌اند، ملزم هستند تا با دولت جمهوری اسلامی ایران بر سر نحوه پرداخت غرامت به توافق برسند.
🔹
بر اساس این مصوبه، در صورتی که این کشورها یا شرکت‌ها نسبت به پرداخت غرامت اقدام نکرده و یا در این زمینه با جمهوری اسلامی ایران به توافق نرسند، مجوز عبور آن‌ها از تنگه هرمز صادر نخواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/686308" target="_blank">📅 21:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686307">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
شنیده شدن دوباره صدای انفجار در بندرعباس و قشم
🔹
در جزیره لاوان هم صدای انفجار شنیده شده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/686307" target="_blank">📅 21:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686305">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L23GAfJp6zsL-dVPq24THIIbSsdQ3zjksEqmVQcifJ4ALgXy01HWm7hyrAVYGEW_UX_VNZhUQWMboFN844y0KB2IIpt01Ep1AgoVE5nFVJfr6iGeF1sbSSJiwHXyAWALTurqcikjRS25d4WeZLgfYDHRB2n5nWGVjZK6XS2M1z1lK9Zz0brEG4P45U4T1P40JRrjshaIEfiWOXd0RRS_8kzq8NtOj-AIST7EwGDHchqrudZCvqVRIJR8cJ4nCtu8WBvjM1_zK-cEzmJ-j9ZUW5jLoJJaA8uNPUbWnlHqdFmfYI6eYG-FR_0Ueq7oyr3Rgqu-OHkJFp7fEGlZvhG5LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z-WjJugHLXCQoUYQZeVCXHVc7B5VCJ4xikL3orCi1HPsRNCwmw7ZdibeU8btI0STnChCfRNu4z_5QM4ZFeIKQIPh0HpB5a7X9wKBCFfxx3n7Rqx6p3KixcdQzZ6_3PQxpjQHKoocR0617FZn7vD9e9eOSl_G2vnngqaKMWaCBnNHOVBfUAgSCbhtkYo-11PImXI8Py2J6hsNlCaTFjR666V6W2RyPmo88c4__U5rn7wu3ILlzDEEzYgvY5P6XE-gLF8BqcZnIpKluM2PevKRYnH--RtvWGrgOptodDV1hXWn0Gn3o9zTnlMjW8-Nr8-yT0tZHpLY9hGXX6edPwC1wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">میزان و کیفیت خواب مناسب در رده‌های سنی مختلف
🔹
بررسی آمارهای سلامت خواب نشان می‌دهد نیاز به خواب با افزایش سن کاهش می‌یابد؛ به طوری که نوزادان به ۱۷ ساعت و سالمندان به ۷ ساعت خواب روزانه نیاز دارند.
🔹
در بخش کیفیت خواب نیز، زنان ۴۰ درصد بیشتر از مردان به بی‌خوابی مزمن مبتلا می‌شوند، در حالی که مردان ۲ برابر بیشتر از زنان دچار آپنه یا وقفه تنفسی در خواب می‌شوند.
🔹
همچنین با گذشت زمان، میزان خواب عمیق در هر دهه حدود ۲ درصد کاهش یافته و در افراد بالای ۶۵ سال، بیداری‌های ناگهانی در طول شب به اوج می‌رسد.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/686305" target="_blank">📅 21:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686304">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
مرشایمر: ادعای کنترل آمریکا بر تنگه هرمز مضحک است
استاد علوم سیاسی دانشگاه شیکاگو:
🔹
کاملاً روشن است که ایرانی‌ها تا حد زیادی کنترل تنگه هرمز را در اختیار دارند.
🔹
پیش از آغاز جنگ، روزانه حدود ۱۳۰ کشتی از تنگه عبور می‌کردند، اما این رقم اکنون به حدود ۸ تا ۱۱ کشتی در روز کاهش یافته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/686304" target="_blank">📅 21:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686303">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01137ebf30.mp4?token=Re_bUBlgkMcks3uj-wdk00zm_XMydXsBcbWo26O-2G02r7vpSXT7qNi2XBIG-aNE16vLoHpN1DR4dsPQVNN7ERtde3NLDgWRw2GasWlNtH42B5H6M6tzgluZX1Kmk2CVfRJux1M8v2ZRXzAn-w6fU-bQKyExYXgsCngC2KRclRKTLMfcXHQPKG5XFA8rUBrRXs5DQf0IB1EYRwTwMX2Ow-ZowLGxwgS8wpd1wiqXfghsXf4fbgfvbCYDWzP0igmcR2hlg0S7a2Q63OoqYGlRqak6MgCqZFkaytdQspYNlHySYkMkFMRkdZaDoFOof_xUIcs81RAfQ7baPlLQuN8WOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01137ebf30.mp4?token=Re_bUBlgkMcks3uj-wdk00zm_XMydXsBcbWo26O-2G02r7vpSXT7qNi2XBIG-aNE16vLoHpN1DR4dsPQVNN7ERtde3NLDgWRw2GasWlNtH42B5H6M6tzgluZX1Kmk2CVfRJux1M8v2ZRXzAn-w6fU-bQKyExYXgsCngC2KRclRKTLMfcXHQPKG5XFA8rUBrRXs5DQf0IB1EYRwTwMX2Ow-ZowLGxwgS8wpd1wiqXfghsXf4fbgfvbCYDWzP0igmcR2hlg0S7a2Q63OoqYGlRqak6MgCqZFkaytdQspYNlHySYkMkFMRkdZaDoFOof_xUIcs81RAfQ7baPlLQuN8WOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمامی حملات امشب آمریکا به جنوب کشور به مناطقی بود که قبلا به آن حمله کرده بود
🔹
در این حملات آسیبی به افراد و زیرساخت‌ها وارد نشده است./ صداوسیما
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/686303" target="_blank">📅 21:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686302">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
آژانس اتمی بار دیگر مدعی «عدم پیشرفت» در برنامه هسته‌ای ایران شد
🔹
در گزارش فصلی جدید آژانس بین‌المللی انرژی اتمی درباره ایران که برای کشورهای عضو ارسال شده و رویترز نیز به آن دست یافته است ادعا شده که هیچ پیشرفتی در پرونده ایران حاصل نشده است.
🔹
در این گزارش ادعا شده که آژانس از زمان حملات آمریکا و اسرائیل در ژوئن ۲۰۲۵ به ذخایر اورانیوم ایران دسترسی لازم برای راستی‌آزمایی نداشت است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/686302" target="_blank">📅 21:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686301">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
فرماندار لنگرود و مدیرکل مدیریت بحران استانداری گیلان وقوع هرگونه انفجار یا اصابت در شهرستان لنگرود را تکذیب کردند
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/686301" target="_blank">📅 21:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686300">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84a2512ead.mp4?token=F89d0lfrTubeItF9hHMIDmbIVB04RDKBSD3JXgFRk2HSPI1CXjKr6kBTGlEZ24bGzmcmcJtU6hXirudtJWwwq--rX2bdAi8jdSiqPbtNTnYCge82Cttv3_u_IkLVcaONaLYk4FhoUertqhRVrrTHZxXLJovSzUHCKxGwuyaAtfUCT4zC4jyVDVBBsXKRYgSi2fzqN3anOcff0CcBxZF7r8LvndNwsHcCt-lC_3_LJoabaFe7q5-CsN4PUA5VT6WQLeVORgbMy8AittNLgjiDNCBoST3r4iRfIO-5TlTNoCbTR7rEQ8a7ZMCh7UaeM3GkwmFw4w27YxpLW2rXn5IaC2tGHtCOkTsfk5kibdwnDwm_hZnwOh3IQ0vcHGolLhcGDL7RX2cXn8ljmusyt4D3ddmvXFV55A6Yn5qhWanpkm0pDqY7QaLQD1aKUfuZ5hy8ap-ldzsa-yIR-PA2A5-v1xh42Ad1QwzWesXpaDQVURj3RpT3HCu8HSAumtEPYk_MEysJ63hy00AVYvt5HFEdkT4zJ4xuQ1w068q14VL3gnu29W8C9pnV1tZkPkZQMlqBoePgz5C50WcelWVzrADUyl_85g5S8zUAdOdr3QooTY6IuzYdMQbwfyzg-1aR-Iw28_TFsHpBSioai7ZswhZtyM-VzX09w4p3leavlv-ilgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84a2512ead.mp4?token=F89d0lfrTubeItF9hHMIDmbIVB04RDKBSD3JXgFRk2HSPI1CXjKr6kBTGlEZ24bGzmcmcJtU6hXirudtJWwwq--rX2bdAi8jdSiqPbtNTnYCge82Cttv3_u_IkLVcaONaLYk4FhoUertqhRVrrTHZxXLJovSzUHCKxGwuyaAtfUCT4zC4jyVDVBBsXKRYgSi2fzqN3anOcff0CcBxZF7r8LvndNwsHcCt-lC_3_LJoabaFe7q5-CsN4PUA5VT6WQLeVORgbMy8AittNLgjiDNCBoST3r4iRfIO-5TlTNoCbTR7rEQ8a7ZMCh7UaeM3GkwmFw4w27YxpLW2rXn5IaC2tGHtCOkTsfk5kibdwnDwm_hZnwOh3IQ0vcHGolLhcGDL7RX2cXn8ljmusyt4D3ddmvXFV55A6Yn5qhWanpkm0pDqY7QaLQD1aKUfuZ5hy8ap-ldzsa-yIR-PA2A5-v1xh42Ad1QwzWesXpaDQVURj3RpT3HCu8HSAumtEPYk_MEysJ63hy00AVYvt5HFEdkT4zJ4xuQ1w068q14VL3gnu29W8C9pnV1tZkPkZQMlqBoePgz5C50WcelWVzrADUyl_85g5S8zUAdOdr3QooTY6IuzYdMQbwfyzg-1aR-Iw28_TFsHpBSioai7ZswhZtyM-VzX09w4p3leavlv-ilgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت یک مداح از حضور رهبر انقلاب در مراسم رهبر شهید ایران در حرم رضوی
حاج عباس حیدرزاده:
🔹
آقای مروی فرمودند حضرت آقا در شب دفن رهبر شهید از ساعت ۱۲ شب تا هفت صبح، در حرم بودند و حتی مسئولان حاضر، پشت سر ایشان نماز خواندند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/686300" target="_blank">📅 21:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686299">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
سخنگوی سپاه پاسداران انقلاب اسلامی: تنبیه سختی در انتظار متجاوزان است، آمریکا از حملات جدید خود پشیمان خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/686299" target="_blank">📅 21:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686297">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
حمله آمریکا به یک کارخانه پودر ماهی در قشم
🔹
در حملات ساعتی پیش ارتش متجاوز آمریکا به سواحل جنوبی ایران یک کارخانه پودر ماهی در قشم، یک اسکله صیادی و دکل اداره‌ی بنادر در سیریک مورد حمله قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/686297" target="_blank">📅 21:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686296">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای ترامپ: این حملات گسترده و قدرتمند هستند و در واکنش به تلاش نافرجام ایرانی‌ها برای کار گذاشتن مین‌های دریایی در تنگه هرمز انجام می‌شوند
🔹
تنگه‌ای که در حال حاضر هیچ مینی در آن وجود ندارد (مین‌ها به‌طور کامل منهدم یا منفجر شده‌اند!).
🔹
همچنین این حملات…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/686296" target="_blank">📅 21:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686295">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
واشنگتن از پاسخ تند و قدرتمند ایران به تجاوزات خود بیمناک است
🔹
شبکه فاکس‌نیوز در گزارشی اعلام کرد  مقامات آمریکایی به دلیل اقدامات تهاجمی اخیر، از واکنش شدید و انتقام‌جویانه ایران در منطقه واهمه دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/686295" target="_blank">📅 21:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686294">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAASfjfmrLzBlv1ouaKupK6S7wbtwzXKTvZVzsR-Iq_knANx8EI95FoRVQXaqKyACKt88-Dp3Vo7mO-i24PWdOERJD7GCiYyJoT07TwQrBhSPwcbIVcvWshIagmb6TdsaWPZu68_oSUDH8IA3Ze-EYVZRRNFCEzImsUaxghLgW5m9kSl9UBvu_LbjPFdsThZAdYpruOrtDxTM6inJt1CsLPXEAZclY7xxAJYKiUEGiP2JSKdQbEV8wrSkp7z11DZ-c7mQJVXC36nAR6oEFq76PIBevULwj7isSHv5Sd7uQfQTb9_swrQPEf1H4-zjnsSIyMtxjGEZ53QrP1Upg82kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی سپاه پاسداران انقلاب اسلامی: تنبیه سختی در انتظار متجاوزان است، آمریکا از حملات جدید خود پشیمان خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/686294" target="_blank">📅 21:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686293">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
به گفته منابع محلی، دقایقی قبل صدای ۶ انفجار در بندر چابهار و کنارک شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/686293" target="_blank">📅 21:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686292">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUDn06-D3AQicOSK84JgLPcg6MXHK8lSAQCbQZ0q4Fq4kyrux5rmRBWQP_hoTWou_pHvF2dXXI5lFM2ACULR72w2kq02vFCX0070r-L1r-kKzRfAWRkuyuOOJEs8URHUQheBxZ2OlEHPstDKe2MrS5VKTwz4L87jNPsbpizCjnYatif5BOnrT6b5QqVk-xW9n_ZTP7XcYrH5g8FyPH6hhxwsXruMGmxs3eRJHpszuQ5yVTsI9pT0lw-eGA1GNiRKtsgLTCNV7QWnVEnffOq7YxTe7HgMzNjsr5YEGaJ1Z3VoFOwYRQBAQP2rMjMO6s60RjJQy5Y-YWky4o53J5anpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: آمریکا در حال انجام حملاتی علیه اهدافی ایرانی در نزدیکی تنگه هرمز است #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/686292" target="_blank">📅 21:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686291">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
یک منبع نظامی: ایران به حملات آمریکا پاسخ چند برابری می‌دهد
🔹
یک منبع ارشد نظامی به تسنیم گفت که نیروهای مسلح ایران به جنایت امشب آمریکایی‌ها در حمله به نقاطی از کشورمان قطعاً پاسخ می‌دهند و این پاسخ چند برابر حملات آنها خواهد بود.
🔹
همچنان که پیشتر نیز هشدار…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/686291" target="_blank">📅 21:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686290">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5136a28d0a.mp4?token=s6cC7inrtlarxRTC-JzuwRdTFzpXBv2ksY0BreTIlzSS_kNj_v00w9GiwOoFgTOcVNXjUuQhfa5Y_whDCNFjjCDc1T8lvUcrRNBtiW9HP5__WgOg8-cv2JO0CW7Ue4xD-aUczrwam1-o9OFkJHvL1fPpImSURLFGs5LOIkpOUqOiV0VJNxPMAoKgCE8BSgoYRztTuKjSR6ctmw_xgN-pQNNoNa8iCXkJAXxOBnEdUgxs0OdzWL1oNLt85hxvPJzQddBZL8SBK_6rNwNXSZYyEYttgRxdtag3LLvrVPAX0zcQZ7vuHm5EvOGP_mwptey0PQ88PjvVz8EHXfC2SPdW8CQpkmrOvbN6Ly8S_Bhe7Kf5Oob6fcyDtJty5lvXRlm--x-dPj8iuu2qfCCbLJAvEn6HqpPepiWmZPU7c5nPwQLXeHIvxo6xGj2JhvpwR2OozLcPCB88x0q4pNavF3uJZ6uvvlo2zdhIs4O0zMYmgZhnFFMhaMpx0K-fXAWYuUKmVzVBnvLkd93LpCOBvprn3-CAWyGbB8fhbBPrboX-HgE-3yfz0RuMqs-b-09F60qdbLRfCjUxLMWHFd3ifq7dHqeex1vW9UIxVTOWdw-VGbWAgNjN0T3DevNCmITB7datrcRBrZV_pBcprYFo26fO16WYPUhZbloNxDdVItc2iuk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5136a28d0a.mp4?token=s6cC7inrtlarxRTC-JzuwRdTFzpXBv2ksY0BreTIlzSS_kNj_v00w9GiwOoFgTOcVNXjUuQhfa5Y_whDCNFjjCDc1T8lvUcrRNBtiW9HP5__WgOg8-cv2JO0CW7Ue4xD-aUczrwam1-o9OFkJHvL1fPpImSURLFGs5LOIkpOUqOiV0VJNxPMAoKgCE8BSgoYRztTuKjSR6ctmw_xgN-pQNNoNa8iCXkJAXxOBnEdUgxs0OdzWL1oNLt85hxvPJzQddBZL8SBK_6rNwNXSZYyEYttgRxdtag3LLvrVPAX0zcQZ7vuHm5EvOGP_mwptey0PQ88PjvVz8EHXfC2SPdW8CQpkmrOvbN6Ly8S_Bhe7Kf5Oob6fcyDtJty5lvXRlm--x-dPj8iuu2qfCCbLJAvEn6HqpPepiWmZPU7c5nPwQLXeHIvxo6xGj2JhvpwR2OozLcPCB88x0q4pNavF3uJZ6uvvlo2zdhIs4O0zMYmgZhnFFMhaMpx0K-fXAWYuUKmVzVBnvLkd93LpCOBvprn3-CAWyGbB8fhbBPrboX-HgE-3yfz0RuMqs-b-09F60qdbLRfCjUxLMWHFd3ifq7dHqeex1vW9UIxVTOWdw-VGbWAgNjN0T3DevNCmITB7datrcRBrZV_pBcprYFo26fO16WYPUhZbloNxDdVItc2iuk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دات‌وان ونچر؛ بازوی سرمایه‌گذاری در حوزه نوآوری و خلاقیت
🔹
در جریان برگزاری نمایشگاه الکامپ، دات‌وان ونچرز به عنوان بازوی سرمایه‌گذاری هلدینگ دات‌وان، برنامه‌های خود را برای حمایت از زیست‌بوم استارتاپی کشور تشریح کرد.
🔹
علیرضا حاج سعید، مدیرعامل دات‌وان ونچرز:
🔹
با توجه به نیازمندی‌هایی که شرکت‌های هلدینگ دات‌وان دارند، در ونچر استودیو توانستیم ۱۱ هسته فناور داشته باشیم. روی ۱۶ تیم سرمایه‌گذاری کنیم که ۶ تا از سرمایه‌گذاری‌ها به بلوغ رسیده و الان واگذار شده به هلدینگ. بقیه هم در پروسه انجام است.
🔹
فردای کشور را فقط ایده نمی‌سازد، حل مسئله می‌سازد. از خودتان سوال کنید که چه مشکلی را حل می‌کنید؟ آن‌وقت ما به عنوان دات‌وان ونچر در کنار شماییم.
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/686290" target="_blank">📅 21:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686289">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مدیر اجرایی نمایشگاه
#الکامپ
: در این نمایشگاه ۱۰ رویداد جانبی برای مخاطبان ارائه شده است .
رضا حیدری: ۳۵۰ شرکت در ۱۴ سالن، آخرین دستاوردهای خود را در
#الکامپ۲۹
به نمایش گذاشته اند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/686289" target="_blank">📅 21:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686287">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
برخی منابع از شلیک موشک‌های ایرانی به سمت پایگاه‌های آمریکایی در منطقه خبر می‌دهند
🔹
این خبر هنوز به صورت رسمی تایید نشده است./ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/686287" target="_blank">📅 20:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686286">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0bbbc3995.mp4?token=v9zIepD_esAHpwan0jtW8ck1J2yBszjSanHRqezt3MJ01qJ1i3rAdjnYUgp_szJgnqpjd9KZzlaJXQep460xCb3WTeUAUjVkEFO9qGUUWVSPJ1drR6N0X8Q4hdBDlwY6P-Z9Xay3eyjgxfzWdkqAQXQHl_YjFn1ZsXPMuSFqBKuyNWvFxM5gfHufNmUs1bkXH6SiXg1pmDbKLQNcH6lDaMv9PyAj0F3HWkRfsqCxQ46TJ168tx_6kGuJUZ5JwwIRyqdE2R1oJXPUCppVb3_47SB1Fgqy3TYI7wB-ZUH-lsTQvTztGAB4NocoC7CR7E5LTCAp2jsVojTY5IXCJUfB3gLlq7WF2_sCwroRiqE-R6ff-Cd4PI_BWKy2Ew3KSvFXN-r51AZ-tnth5rokS7W15nfNO5k19SJmvdVCvYoF410txB2XgkE94mZnJRPPh-dHIrjEg86rnyC7mhLMrzqpG4QJUFRR2RPJF1OLcnwT1PcjwdmvB6K-6i9c_HZC2YNfCJwJaeUdj9jMxsqR9HEI15ivFKs3HobUkHQ8UyNVtmbolWW9fkibJhrrYLLQcug7K2wcUSKo8JEZjZQkH3VRk6atUdDexYzuSSs12ZwA3JBk5CEk_M497khfQHBgemxXmBpEoT0hNm3XR5-o4H1lU7lHjxGhmOA_fiEHo8c2ui8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0bbbc3995.mp4?token=v9zIepD_esAHpwan0jtW8ck1J2yBszjSanHRqezt3MJ01qJ1i3rAdjnYUgp_szJgnqpjd9KZzlaJXQep460xCb3WTeUAUjVkEFO9qGUUWVSPJ1drR6N0X8Q4hdBDlwY6P-Z9Xay3eyjgxfzWdkqAQXQHl_YjFn1ZsXPMuSFqBKuyNWvFxM5gfHufNmUs1bkXH6SiXg1pmDbKLQNcH6lDaMv9PyAj0F3HWkRfsqCxQ46TJ168tx_6kGuJUZ5JwwIRyqdE2R1oJXPUCppVb3_47SB1Fgqy3TYI7wB-ZUH-lsTQvTztGAB4NocoC7CR7E5LTCAp2jsVojTY5IXCJUfB3gLlq7WF2_sCwroRiqE-R6ff-Cd4PI_BWKy2Ew3KSvFXN-r51AZ-tnth5rokS7W15nfNO5k19SJmvdVCvYoF410txB2XgkE94mZnJRPPh-dHIrjEg86rnyC7mhLMrzqpG4QJUFRR2RPJF1OLcnwT1PcjwdmvB6K-6i9c_HZC2YNfCJwJaeUdj9jMxsqR9HEI15ivFKs3HobUkHQ8UyNVtmbolWW9fkibJhrrYLLQcug7K2wcUSKo8JEZjZQkH3VRk6atUdDexYzuSSs12ZwA3JBk5CEk_M497khfQHBgemxXmBpEoT0hNm3XR5-o4H1lU7lHjxGhmOA_fiEHo8c2ui8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در هفت روز جنگ، ۱۵ استان را سرکشی کردم
پورمحمدی در بیست‌ودومین قسمت برنامه ماجرای جنگ۲:
🔹
قبل از رسیدن به هر استان، به آنها خبر نمی‌دادم تا متوجه شوم واقعاً در استان چه خبر است
.
🔹
در همان وسط جنگ، با استاندارها درباره پروژه‌های توسعه‌ای استان برنامه‌ریزی می‌کردیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/686286" target="_blank">📅 20:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686285">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
پرس‌تی‌وی به نقل از مقام‌های آمریکایی: تعداد حملات هوایی که امشب علیه ایران انجام می‌شود، ممکن است به ۱۰۰ حمله برسد/ انتخاب
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/686285" target="_blank">📅 20:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686284">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tf5swBWJIjL8b9Ymynq7SrYPEKXfB8sVFrGV7Nckg3JjKljzLZfXNGv8iKTd3ZzQf5SUK7NxekHp1FOeFeKrAA5JuHpk0NjoJP9Hwa9Is5T3yREU_IpQmbljI67SoS13F72h10Rg0V7WYCLWif0rzBoF5e0kQsL3mtBcJpwyxkhIkCeBWRwGpb0Byc92DiBLjHJDTNSsaFKXkcV338VsoF_Yd-DgrjYmdQs37Pmo-zC1J46rK_Z-13mdH2SaLF9aVl1_CHmtcGM1Zg8EFLabvjazCu2ZTmc9oel9aCk9QFWMK4OI_nH7ROvw-PJO7m_3GW4DtUxP8Xksuz3ESQ6Lvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تنگه هرمز ۲ در راه است؟ / این اقدام دریایی ایران کابوس آمریکا می شود
🔹
لازمه بستن تنگه باب‌المندب این است که ایران دیپلماسی منطقه‌ ای خود را فعال کند. این مساله‌ ای است که رسانه‌ های غربی را نیز ترسانده است. آنها از احتمال فعال شدن سیاست "فشار نظامی به غرب و متحدانش" و همزمان، "فعال شدن دیپلماسی منطقه ای" سخن می گویند.
گزارش خبرفوری درباره برگ‌برنده ایران را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3241998</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/686284" target="_blank">📅 20:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686283">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnYaP7LgTeCW_dmWgr82smjQZUV8jsmHKSSgkCUVLAGT3BzzrHiTYQ2cJ_SSTlIaYcbmjAw0bSaAnAX9p4t9gV9krI_KQZVeKv8jWfvw8b4g_0OOMqc8zQxA6b5Ieky8vnCTJUnkeyh33WLmfSa08W5pAQYX942c5VCOlTERrKgQ0ceZTBLTORhmaKXft795xd9I1xtx1ncBo-6p_pNbrCSeyVslcdV4Bph0BLGbE25QPzSShrtA10SzhU0jDtvwCtp5S4DMFGhYUjdYjFrbUYFwy-XoyJqZAm6ducYVA5O_xZ0JIrRDjzPOJMYXpUve9hA8Vbw2vwFPEDqOIYO2Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعالیت هواپیماهای شناسایی و سوخت‌رسان آمریکا در منطقه
🔹
فعالیت هواپیماهای شناسایی و سوخت‌رسان نیروی هوایی و دریایی آمریکا همچنان در سراسر غرب آسیا ادامه دارد و گزارش‌ها از فعالیت هواپیماهای KC-135، KC-46A و P-8A در نزدیکی خلیج فارس حکایت دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/686283" target="_blank">📅 20:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686282">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار سیستان و بلوچستان(Admin)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d37c6f9286.mp4?token=Nw9-vkqg98-s6Qx9TtPrehZHf-f3s38kP72aPv3RD4eJIrHMQW1rK9H1i_jXil6oiFLCbjUmJprHtMSgarjKIJTyRtvc8NBWqK2JvBIuOsxHVWrF2-RJ-fm9MP57EmzMibG7kM-U3TeH4ig1JlhQCCeNZ7xZ7alr2d2TDEGVZ8Y0af6xyZjrkFiP9oKjJwz3bqVcDVbZySIMMdFos-z3Ivfxgmp5ztjMd9CDfavLigAW12HMJCc6h_gW2E7vCPXkBgsK2LoyLjQOFINuScIRisNpxSASbAOFcFqrvtQTJikKXSnoPjXZPw6SnAq0KP-ojHrFj-qKKszmaNK1mLgU4lzc9KNEZCGv2QTtnfyShLXrjLgBz147hck3Ou9-BA9Pnn-kfUWYZmC4X3NdI0XFHim4UBaSgtj4Zy3VkiSqXNHKwa7s8e8hP-exhciLuGAs8KOz9wEqFTOsRvbInc7GJmvNkWHAS15E6En3ZacPDPwFfI7JSF2nIE-wNMPFYbnRD1QdP_jfzlvr_aHk7hxh0iFSAzOx3TWceQKPMhTjEZDtHid7EVVRa6gbUhoUHV1OmHv4-kYwnCcDFalehxLWQg1oRGrqPnXdyB1R9Sdt2VCEu5QflZAx5ilbL3HLa3naHkLkt5w18HF-6oOU6viZUnYuY4SyXeMRvvBNbYQ2CTY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d37c6f9286.mp4?token=Nw9-vkqg98-s6Qx9TtPrehZHf-f3s38kP72aPv3RD4eJIrHMQW1rK9H1i_jXil6oiFLCbjUmJprHtMSgarjKIJTyRtvc8NBWqK2JvBIuOsxHVWrF2-RJ-fm9MP57EmzMibG7kM-U3TeH4ig1JlhQCCeNZ7xZ7alr2d2TDEGVZ8Y0af6xyZjrkFiP9oKjJwz3bqVcDVbZySIMMdFos-z3Ivfxgmp5ztjMd9CDfavLigAW12HMJCc6h_gW2E7vCPXkBgsK2LoyLjQOFINuScIRisNpxSASbAOFcFqrvtQTJikKXSnoPjXZPw6SnAq0KP-ojHrFj-qKKszmaNK1mLgU4lzc9KNEZCGv2QTtnfyShLXrjLgBz147hck3Ou9-BA9Pnn-kfUWYZmC4X3NdI0XFHim4UBaSgtj4Zy3VkiSqXNHKwa7s8e8hP-exhciLuGAs8KOz9wEqFTOsRvbInc7GJmvNkWHAS15E6En3ZacPDPwFfI7JSF2nIE-wNMPFYbnRD1QdP_jfzlvr_aHk7hxh0iFSAzOx3TWceQKPMhTjEZDtHid7EVVRa6gbUhoUHV1OmHv4-kYwnCcDFalehxLWQg1oRGrqPnXdyB1R9Sdt2VCEu5QflZAx5ilbL3HLa3naHkLkt5w18HF-6oOU6viZUnYuY4SyXeMRvvBNbYQ2CTY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استاندار سیستان و بلوچستان در رابطه با گروگان گیری و نا امنی های ایجاد شده در استان: نظامی که میاد ابرقدرت های جهان رو به زانو در میاره و پوزشون رو به خاک می ماله اینکه بخواهد با چهار نفر سارق و گروگان گیر برخورد کند،تو این زمینه هیچ ناتوانی و ضعفی ندارد
@akhbar_sob</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/686282" target="_blank">📅 20:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686281">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
به گفته منابع محلی، دقایقی قبل صدای ۶ انفجار در بندر چابهار و کنارک شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/686281" target="_blank">📅 20:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686280">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
ادعای اتحادیه اروپا درباره مذاکرات مربوط به تنگه هرمز
مسئول سیاست خارجی اتحادیه اروپا:
🔹
تلاش‌های دیپلماتیک درباره تنگه هرمز «تاکنون هیچ نتیجه‌ای نداشته است».
🔹
برای ما مهم است که هیچ گونه عوارض و هزینه‌ای برای این مسیرهایی که قبلا باز بوده‌اند، وجود نداشته باشد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/686280" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686279">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
فاکس نیوز به نقل از یک مقام آمریکایی: حملات نظامی علیه ایران همچنان ادامه دارد
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/686279" target="_blank">📅 20:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686278">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
گمانه زنی درباره همکاری بحرین و کویت در تجاوز به ایران
🔹
گزارشاتی غیررسمی از شلیک موشک‌های زمین به زمین هیمارس از مبدأ بحرین از سوی منابع عربی منتشر شده است؛ با این حال تاکنون تصاویر مستندی منتشر نشده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/686278" target="_blank">📅 20:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686277">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dr6aUvrKpk-98lziQEHs6pITD0W73ey1mMZUE5FbP_Ik-lpQcukeamYwSfHikSnddUI7AxhRHyTKbMqA8RLNSnWtzksRIYchRCJDyd8ZwnIR7xMc5j2NC34ilgjQw6co0YmUZUEpcWBm8KTiGxwFTgGcPMD_0uqaqWMUuFXW6miyT74xOaTsTO5gbQ7iBtYXYwR3wGX8t4VZ6AUEwz67m6J_-8HpkwabImtHCkoLzlobACgRG1f0YMMEldCaNLLGwAxKwRsBAkWMENwC306ncY2Kmqpi4kqMefpuuVocDTFVoObQ5qBc4OgBMZxvBxRyAa6ypC1etk6o_wHL5gxjFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقتصاد جهانی در سال ۲۰۳۰
🔹
صندوق بین‌المللی پول (IMF) پیش‌بینی می‌کند که تولید ناخالص داخلی جهان (GDP) تا سال ۲۰۳۰ به حدود ۱۵۰ تریلیون دلار خواهد رسید.
🔹
بر اساس این پیش‌بینی، ایالات متحده آمریکا با ۳۷.۷ تریلیون دلار همچنان بزرگ‌ترین اقتصاد جهان باقی می‌ماند و چین نیز با ۲۶ تریلیون دلار در رتبه دوم قرار خواهد گرفت.
@amarfact</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/686277" target="_blank">📅 20:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686276">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
معاون استاندار سیستان و بلوچستان: چهار پرتابه در شهرستان‌های چابهار و کنارک اصابت کرده
است
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/686276" target="_blank">📅 20:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686275">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
آژانس بین‌المللی انرژی اتمی: میزان ذخایر اورانیوم غنی‌شده ایران تغییری نکرده است
شبکه سی‌جی‌تی‌‌ان:
🔹
در گزارش جدید آژانس بین‌المللی انرژی اتمی آمده است که بر اساس  برآورد‌های صورت گرفته، میزان ذخایر اورانیوم غنی‌شده ایران تا ۱۳ ژوئن ۲۰۲۵، تغییری نسبت به گزارش‌های قبلی نداشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/686275" target="_blank">📅 20:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686274">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
برخی منابع از شلیک موشک‌های ایرانی به سمت پایگاه‌های آمریکایی در منطقه خبر می‌دهند
🔹
این خبر هنوز به صورت رسمی تایید نشده است./ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/686274" target="_blank">📅 20:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686273">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owKDPb793jkFHIGVnTVj8-LY34zip_Vmk7heDypWpkaukekVsFC5tLPZDta8ejnBUkyliSaHRKuaOjGR60hMkXdTR2l-BBLM8brEvjatdyNrNrIkJnz3Fx7phPBUPjFN58WVsJG1O0YuRXGR0m6QDxFQieBacKQxXzxmg3ZoDV5pVNeqirk6yU8swnouQtakeGHkFj6lz5dcJ5rToZugYC-KgIPJbPQXTXs660a5EhsIY3SF2WVxEDksXlv4_TuigzdPM2C2TrmiS0B7GWi5hCL164HAYyycPzAgZKJVOr0ynqVP2Xlkxc9oPAsHpBfCaZwBvDTow_ldcTdIk8XOjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسلح مسلط
🔹
قالیباف رئیس مجلس امروز در پیامی ویدئویی با بیان ابنکه دشمن بداند در دوره‌های بعدی جنگ، هم در بُعد کیفی و هم کمی، مسلط‌تر خواهیم بود گفت که نیروهای مسلح از هر فرصتی که به آن‌ها بدهیم برای بازسازی توان خود استفاده می‌کنند و حتی ساعت و لحظه‌ها را هم از دست نمی‌دهند. او افزود که در تنگه هرمز علاوه بر اعمال قدرت نظامی، در عرصه دیپلماسی نیز پیشرفت‌های خوبی انجام شده است.
🔹
هشتصدوچهل‌ونهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/686273" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686272">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
وزیر کار، تعاون و رفاه اجتماعی: معوقات بازنشسته‌ها به ترتیب حروف الفبا در حال واریز است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/686272" target="_blank">📅 20:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686271">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1dca1fd7.mp4?token=MEqIl65-94HZ8r04mQvDlnX7NNmlFw72VzwTm5EwWdK_6WWtC8CjFP5PVyn2R5qjMhm4tR9L0z8_w0nDInrNOJe_9rHrYmeFasAIyy4rPMgfQNNSKHA8dNqYW2DqfB9WoZQEPDXBQ70npxUZx1kwigUDrLzIS5f70Tkvei1pyjdOnv1xx0qwFDkge3qALsd7CQQ0MuXb5d4bwylw_jxEGt-P6U7J4-P-gSnmEsegOhTDw1EjDFBjvZHHHsZWSGGFKsGRM69Ex4oXHiLobR7b9HEToZSt_gSWV8_cgh07X4H7gwNX8h0BUzHjdbAaIHAHekxiTB7YwL6B51hCyVQCE5rasR2cEe4fCEXQvmmp_xUGrVy6unnEFcpZBA1nHofmUnSZRbQxYBpXnQq3jR_YEOHFfqtqbchyM78IvnYEDznF_oGDl_Okub2TopMnZuJlT2Y8t7IDL41RaXVoNpTMRhu-445WIMdJ8NVYrtwRrfhaWtFyrmKQZWeAxpix14hKdnY7B5iUcr05eZwJdGLcWmY7lqNW9N5rGJVct_es4nSWgZ5u-ZRYu2N_D6ywwVZX02xGnZp_y0TNSAgcb7weKsOh6I927ZVW2CTzCf9jA-I2mObYGXSCTPgkbFTYv3Txn8Wg6OozS3GSpAMHWjXjJS4F0sYHlh8JWPQzvNk-pRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1dca1fd7.mp4?token=MEqIl65-94HZ8r04mQvDlnX7NNmlFw72VzwTm5EwWdK_6WWtC8CjFP5PVyn2R5qjMhm4tR9L0z8_w0nDInrNOJe_9rHrYmeFasAIyy4rPMgfQNNSKHA8dNqYW2DqfB9WoZQEPDXBQ70npxUZx1kwigUDrLzIS5f70Tkvei1pyjdOnv1xx0qwFDkge3qALsd7CQQ0MuXb5d4bwylw_jxEGt-P6U7J4-P-gSnmEsegOhTDw1EjDFBjvZHHHsZWSGGFKsGRM69Ex4oXHiLobR7b9HEToZSt_gSWV8_cgh07X4H7gwNX8h0BUzHjdbAaIHAHekxiTB7YwL6B51hCyVQCE5rasR2cEe4fCEXQvmmp_xUGrVy6unnEFcpZBA1nHofmUnSZRbQxYBpXnQq3jR_YEOHFfqtqbchyM78IvnYEDznF_oGDl_Okub2TopMnZuJlT2Y8t7IDL41RaXVoNpTMRhu-445WIMdJ8NVYrtwRrfhaWtFyrmKQZWeAxpix14hKdnY7B5iUcr05eZwJdGLcWmY7lqNW9N5rGJVct_es4nSWgZ5u-ZRYu2N_D6ywwVZX02xGnZp_y0TNSAgcb7weKsOh6I927ZVW2CTzCf9jA-I2mObYGXSCTPgkbFTYv3Txn8Wg6OozS3GSpAMHWjXjJS4F0sYHlh8JWPQzvNk-pRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مصطفی انتظاری هروی، مدیرمسئول خبرفوری در الکامپ ۲۹: مهم‌ترین کار هر رسانه این است که تا چه اندازه بتواند در حل مسائل نقش‌آفرینی کند
🔹
رسانه باید بتواند مسائل و دغدغه‌های مردم را به‌درستی منتقل کند، بهترین پاسخ‌ها را به پرسش‌های آنان بدهد و زمینه‌ای برای ایجاد ارتباط میان مردم با یکدیگر و همچنین مردم با نهادهای تصمیم‌گیر فراهم کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/686271" target="_blank">📅 20:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686270">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXWfbquCg5Fjy1-C49y4ZMEDUQj2bu8gSrxkwXW4f3BmJ3EYnxcMwt8NVgAuBtYf9FC8wb5aNeyFad655QrRNuwezeRXcYLAKGvCkwOnZIOgRvJ2_n1gE7O0AIqD874MBIwYFNyswlIs4oHU8UYmcc8oN0mY2Y7r8na2WaacYZPNAbG_xcotlVAzQgYBM-gfisr2enOYNyp2I_lwYqVZFiW0XIJJz0oh0EotcubChDVoKjWKQr5pb3ITF2M39EreMoIN2gw3ZkZetRiYvRhTRkhgZyFtzcYOrNRxAZ7UH2s4Xr9_2NUC979H3gTPPsAHtCDewMwwxOJNFR3Sa8jnLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دقایقی قبل مردم در کنارک و چابهار صدای چند انفجار شنیدند؛ هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/686270" target="_blank">📅 20:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686269">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbKS6D0ZMvdFQ2ljua4aaWoRKWwdB4-fHjgwBa7apzt5HWtCfrXdTJtQQaUZxN2yfoff2ZIpRZaZF7za9u8X1VIdkd7Bz5pcruX841U-pmBYVRFsC_eb4zFE7G41MlmgLLIopuc2tsyElZcVw70Y0ljOkPZxPdi_PXuP8HsIzJloTiUqwjmcvUySP3h9W0ks8ns1MJfycvFUgB6SBYLqO5ES07CBJTI3hUK4MkdXaVB-9iNsJfXwCB9Z1mmImGoIQKYRbK-TkruoO3SQLmwq0qADqfzJZMn36i936bn3VHE92Ahmi0nTYtf-rkrdKZMB8KnGax9x-rcRcPz9fP0s7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه ارتش تروریستی سنتکام: امروز، ساعت ۱۲ ظهر به وقت شرقی، نیروهای ایالات متحده به اهداف مربوط به سپاه پاسداران انقلاب اسلامی (IRGC) در ایران حمله کردند
🔹
این حملات، در پی تلاش‌های اخیر سپاه پاسداران برای حمله به کشتی‌های تجاری در تنگه هرمز و همچنین به نیروهای نظامی آمریکایی مستقر در این منطقه، صورت گرفته است./ رکنا
جزئیات بیشتر
👇
khabarfoori.com/fa/tiny/news-3242065</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/686269" target="_blank">📅 20:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686268">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlTGkzvoZkyTUwUqe5lby8PKIBVskYrRUUOlX-ERwIXKGPIvNCzF5aiGf2oIZ-1VLxIRkwyDFuQTwLDiupDeU42pqsg3jdlzI4p3K7Q-jrzmymMHzVPbdjDoomONNq5Dyfc3S7RkT0U3OQAPJQW5-GfVSx-bj64NQWN8bRquxTU17Pra9duEomoLrFKFqR5VaVwJIkUNNGo_eTF3FJKMzMPXfrREj44S-eH_sKA9Iu4PNwju2PSUHYU_XQyEKtBpvszLLK-CJSkwMiwcqDq2IZBSMAxptciG1-k8IjinueRxv783Pd0eM95rZD-b1Hrxbud8grH2k7gdyQ-Y2gmdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفت از ۹۳ دلار عبور کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/686268" target="_blank">📅 20:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686267">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
سفارت آمریکا در قطر: به دلیل تنش‌ها در خاورمیانه، محیط امنیتی همچنان پیچیده بوده و احتمال تشدید پیش‌بینی‌نشده وجود دارد
🔹
شهروندان آمریکایی که هم‌اکنون در خاورمیانه به سر می‌برند باید هوشیاری خود را افزایش دهند و از احتمالاتی مانند لغو پروازها، بسته‌شدن…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/686267" target="_blank">📅 20:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686266">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه مشاهیردانش</strong></div>
<div class="tg-text">🎉
بزرگ‌ترین گردهمایی پذیرفته‌شدگان آزمون وکالت؛ غوغای مشاهیردانش در برج میلاد!
🔔
سومین جشن ستارگان وکالت مؤسسه مشاهیر دانش با حضور مدیران کانون‌های وکلا، اساتید برجسته و بیش از ۱۶۰۰ نفر از پذیرفته‌شدگان آزمون وکالت در برج میلاد تهران برگزار شد.
در این مراسم از رتبه‌های برتر و پذیرفته‌شدگان مؤسسه‌ای با بیش از ۳۰۰۰ قبولی سالانه تجلیل شد و سخنرانان بر ضرورت حرکت به سوی مؤسسات حقوقی مدرن، تخصص‌محور و اخلاق‌مدار تأکید کردند.
⭐️
همچنین خبر راه‌اندازی «خیریه مشاهیر» با هدف توسعه فعالیت‌های مسئولیت اجتماعی مؤسسه اعلام شد.
⭐️
سومین جشن ستارگان وکالت، آغاز مسیری تازه برای پذیرفته‌شدگان در حرفه وکالت را به تصویر کشید.
@mashahiredanesh</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/686266" target="_blank">📅 20:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686265">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
سفارت آمریکا در قطر: به دلیل تنش‌ها در خاورمیانه، محیط امنیتی همچنان پیچیده بوده و احتمال تشدید پیش‌بینی‌نشده وجود دارد
🔹
شهروندان آمریکایی که هم‌اکنون در خاورمیانه به سر می‌برند باید هوشیاری خود را افزایش دهند و از احتمالاتی مانند لغو پروازها، بسته‌شدن حریم هوایی و اختلالات سفر آگاه باشند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/686265" target="_blank">📅 20:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686263">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMwanpE3xXuS-HK-1WwYMYfGi-MEcRxOdIAROtuhw0P0p85GxXtkoqYlyhZHF2lVQC8ah2m1MeV3Pi7vRLRwqj146VgmZNPazDGjxZBdYBg-oeejKgYafR_9FnIA-PgnOQfmDdBZ530LW7UIpv3XrxEDVrAkxArMl0oJB8VNPmjqkufQ6C7WEf-HCPtqCZRZ6W-YEp4pvxL9rk9yt37l_u276I8Gj3P_mG86XNlgUXTs1M5T3q9bJeT-ui1JUdNXvObgJ9scShBiqoL0EJrPkUIsptyohSkmWtmgywchJW9bAAlJiQtkFN7Q1UNT-BSuqReYl04KDP3G4wlTEMRPYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دقایقی قبل مردم در کنارک و چابهار صدای چند انفجار شنیدند؛ هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/686263" target="_blank">📅 20:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686262">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
دقایقی قبل مردم در کنارک و چابهار صدای چند انفجار شنیدند؛ هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/686262" target="_blank">📅 20:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686260">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بیست‌ونهمین نمایشگاه بین‌المللی الکامپ، فرصتی برای دیدار، گفت‌وگو و همراهی با تازه‌ترین جریان‌های فناوری و تجارت الکترونیک.
۹ تا ۱۲ شهریور
ساعت ۸ تا۱۶
https://t.me/ElecompOfficialNews</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/686260" target="_blank">📅 20:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686259">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ادعای العربیه درباره حملات آمریکا به برخی مناطق در سواحل جنوبی ایران
🔹
شبکه عربستانی العربیه به نقل از مسئولی آمریکایی اعلام کرد که ارتش تروریستی این کشور حملاتی را به برخی نقاط در بندرعباس انجام داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/686259" target="_blank">📅 19:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686258">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادعای العربیه درباره حملات آمریکا به برخی مناطق در سواحل جنوبی ایران
🔹
شبکه عربستانی العربیه به نقل از مسئولی آمریکایی اعلام کرد که ارتش تروریستی این کشور حملاتی را به برخی نقاط در بندرعباس انجام داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/686258" target="_blank">📅 19:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686256">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3K5FXeJ9ujtyPfTCUlNAutZsMbY_LFfHYqu6B_Zuj48x5qW38DwCrSjoLA_ba6XprvzcFZAZ6YErtyCXRlLJf5HS-n8bJ_bSusMxP8qXYArvbz1SSy3hudzI5gHzAlg3uo4vw45PZCBrEFcHRwVtVrhHF77onLmmJkOD1EBpNB42nOPImDD2lJ3sFLXqZpvK5zljqxgJI9bl-TIIlJ6dbofAxANpmpu6WhsTUU9IMGpMSURfCRfBfXttnxWZ_7MjQ1POlvnzyJMmp3KgUWjYFgQv6_imIiatV92LkgHTlfeSMl_vWObgruQNDGnb3OhO9T8agoX4fcNym5uYiX6Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aHrKJYG6zHBjQ3uCaYXZKXFrqwDK2hGHHE2fdMoySIVEhdIb3bNaBuM78Ch5lRps6xpCNIYiZBtlOHvKcD2bjRB0_ANVt1f1OnyJoF4xxaB63PgKc48pmVOr_KLhjNMHYrNWYOZ2nACmNm_IB2extGogoLPYR2RUbpUDfuzXFMIHPr-6SYxXS7t8KUTHVY7Lg7N0dmNaR4S915Zu2EAlPS5O7u2NZjwZWaL0ZhwnHaY-MaRpK2idtTqPFQkrC4m8kb8z5MwVmwsXPWKT-bV5zuZSagAWh-6ajyDn5rP0JuSr-SjntOJlCl9JVY2Qz7yBsh1A1pS69CMgGhHkJGEXTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شفاف‌سازی «وملل» در خصوص کاهش ۵۲ درصدی زیان خالص
🔹
زیان خالص «وملل» در سال مالی ۱۴۰۴ با کاهشی ۵۲ درصدی از ۳.۰۵۵ میلیارد و ۸۲ میلیون تومان در سال ۱۴۰۳ به ۱.۴۷۵ میلیارد و ۵۲ میلیون تومان کاهش یافته است
🔹
علل اصلی این بهبود عملکرد عبارتند از: شناسایی ۵.۱۵۷ میلیارد تومان درآمد تسهیلات اعطایی ناشی از بازسازی و تسویه دارایی‌های اشخاص مرتبط در تاریخ ۱۴۰۴.۱۲.۲۵، ثبت ۹.۳۵۸ میلیارد و ۵۰۰ میلیون تومان درآمد عملیاتی حاصل از برگشت ذخایر مطالبات مشکوک‌الوصول، عدم نیاز به شناسایی هزینه مطالبات مشکوک‌الوصول در سال ۱۴۰۴ با توجه به ذخیره ۱۲.۳۹۲ میلیارد و ۴۰۰ میلیون تومانی شناسایی شده در سال ۱۴۰۳، و افزایش سایر درآمدهای غیرعملیاتی به ۷۹۲ میلیارد و ۷۰۰ میلیون تومان. همچنین اضافه برداشت از حساب جاری بانک مرکزی جریمه‌ای معادل ۴.۴۲۳ میلیارد و ۶۰۰ میلیون تومان به همراه داشت که تا پایان سال به مبلغ ۲.۳۲۰ میلیارد تومان تسویه گردید و هزینه‌های عمومی و اداری نیز به ۱۶۸ میلیارد و ۳۶۰ میلیون تومان رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/686256" target="_blank">📅 19:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686255">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJSoT4g9_aIU7EBUTu9SqnUU02Y-Nmx8whw__AhlPTb-KizZjes_1Z8ikoXWi51bov514IkKIl9kPUwe3KBdiUKSTnzNkwOePG0nPs_3cgJAUYO3cAQmcN-a8Vqweg55sYDKE2NwHZZZ6Nm8nxUDXyIvTagp5d_Yy4SpI81NNUwmmXF3cqczgB-dr-aBbpK0Dr673-jAWu9jiY8BTEtGJ-7xBvQZoV2V1YwnSXgd-uCtkvsdBZCj1XHl0_yur1C4WlGgvE4vUcwJmUZqnBF_nm2YrIa4nix7IngHy4L3mFNDnXKRGTW30KhJfAh-CUdpqlmY4E3XmSNvqTfTiTPtsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفت از ۹۳ دلار عبور کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/686255" target="_blank">📅 19:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686250">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cA3eCQfqmunwTC6en0itwizeFcLyQtNHhrNphKvnqgy4KXGWhFHv1nU8AjptHtMdYqUC1NJAoModsvpy83TPulp67E5nSxo3NOIeGzKVPyqxR2NF980lhssmVbA6mDzDS6pNZFTABHd_Ojd42ej99Wjjut_XSwSg-CwDW2EnQF40KUap3HC__lYZ4XA1tecKEUGCH3gv14LE6z-5LSlILsvQlDLdnHF5ObLX2cLVedMcJjctvR3w65UdQzX1HBWD1NgbIEpa7rsCQ1FDye3CFaZ8rACZB6TTy8NL_Yqbx5z0Rjpn6CizrQpK9bLPFbN-LRaeujujN5KuEChs_Aophw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پینوکیو ورژن ۲۰۲۶
🔹
ترامپ ۱۱۱ بار دربارهٔ نیروی دریایی ایران دروغ گفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/686250" target="_blank">📅 19:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686240">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qr7cs4rgW6IGIgy36JdX2Pb2wKflkzsB2Sf61AZ5pMnnxSPfX1UJFvaPRo_Mi1IDSGZwlYfrufBJqfjmBy3ZDBgQeCE5zObaD6LOtuoVk_LMFpQ-zBme22pBc-sCadHueZg5O4Jshq2osg_q_QQDBhKXvsIkh18V2PAivlIwx8GJdwR0f0gwXZ0kMZ4O6Lm4-64uJyZ97z26UXK3UU2QKye1NhnqSPm7wFXS0U1gbQY4Ft0sXKcoVYJSzui4v4_EmpVARMbBacB-0tng_XYzPpmHMqbx1f0l0q8ppa70o1TUseyBkHU_8tX8J9DSf4zjdbJuhoZ3KU4Fi-jnl7znSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvJBxIXGwmXONprfbkV3TzlHnAJVkPKW9ETB3g0v3m3ohX21_WW1uxXuzuVBl7iPv6pwbjpiafexS_KOaDsWtvua3dgWPSlPCDBKSRo22clLAt7VWAT_pLl-N7zBZ2bo8d4h4RdYTzyHBa-ygtFwwrRWOlIPh0arWqHJ-YtQ0Z5HagtrN9_VwJoN8Tg_CNIrM0Jisd09vBNKpO5HYaDrx4Saj2pawjxbpn5XGNeDfIEG1FE3XW7TGs3lAm4S4uGfry7z4y67j5W-lzJJGkaD26_KT4nL-wMfn0iSUd7OuvgQ3v1leI-kSh4vn_ReDPI-siaGmPQX0HNWPKw22w5tfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ggyFjwcMpb7cn4nQJcoB-ldogrX9wygU7ZKeIxGPjC9KV5IyyiELKtrqtp-JXNg25-31RGYBNvb2Cuj9mQK0ICnbIwFc0V8Fxn4lGCY53yKqbdsGzAuMPO4jO0xBX7__cWYRjO2KBj_SiKuTTW1TM6UGjNVvj-OFNb6gBkDLu-z-95Mh5NWULMoCM6vYcGwUjtLdKT6ucf6yvKB8y_fnr2a8mEMibZkca08NGsdh7YiY5ABAhNiRaCtU-RfEFBiLKkSGQibjoAKI74otMF5SOnskWnhtkqndISulR5IyGxdqxTXcFv98ViBoO6iJDB8m89H6AJFb2H3kU9dTNbFzLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGYyluGwtUYO_oQkiQPf4x0PWkWCz--WzUim7D0ENgCSVUyzGg5hFj7PAoXxdVgNmxhDUMCtQZm4yQHQ_MFbS4Gb3kAcDZ9omGyV-7DUDwW3Csjqbtih9zikrwC2YAmdYP8Gj_LHUFHr-Wr6vbBcmP7a_t2xq1uCANpnTXvFFrrfbzbm6amqw3mrLkgtyV_5Nj8v6cPb-Tf5pX7P3Oxb4BBeeaDy6PI3NYTpQe4RabvvPh598wke4cMFpNFLHdriN96KlmqX1BQDJyhovey30NPaPjUjpoFvMxa3IEWqMPY6Fk9mgsDkYyo3Cca6SFJjmtQzPe1BeiTSuiK5f7kVyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qoZwNDnPAYd86CAGmwjWGwenc_19gW2osf_HS9DEol0bAA-ZFNIQkVHc_52ucnIUXigjMvfry5Gl25FtWrOo6sx2xD5MWACryPuoR15sF77uJhl8CBaswmRPTGIXbgnOYi03xChjQKKC80p73DWFJ8ViChYqHYSlXW_FjB3q8k9qOekp3JPZxym-MyaRc0ENLnQZ_tMgiNMp9zDvqEosOTdlr_V1NUWvAOqZk92fXVleYTm5Sl_cDGuQ-yvYwYRSjJyP17kfjF1-lFK544CcZXGFqGWaXDpBykT_-KNkCsmiEysOjUgc5VaKa6Pu2PD9pc-HkATdKrj1U09GR5jwJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zpf8zhHXVHtFcYGpCamG_wUv1CvJUpj4IGljAiFpNKGwPkf72F9YIi9UfTaF62npv_FvVsrHtEoXLzN4N4Uy79vKiPqcynQrsQO__r55IFQnsSHfre-_wsQBw1F3S4MIumwkJzW34zF4BPmrxlgvyb_3fLXDeEeyDvTLoG7CPv6NHIpfRThB9bznKIFPgg3_uECyHdwZ7i-6dDmZgh7NlZkfM_VOV-4Kr7llF0pt2cpJHVuGOEgrOhef0EtuqrAoOt3hMDyeX9zzzz-bhiq74xVePzb4fruJiOizShm-hs7-Ivq4EOPyQacbsxhYLSynowNzOE-P7ooB523WHZJHow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gqKLQrlNMTphBziU-WOiRQtadsjMzkRXFiiC1LekWm43D-SR-JZfWOWm4ahqdTpZG358eSMhSehs2CdD0jKI70q36o98c38s7eHQyqlZMIkjB6yGZdDNRYiXuSpVQorXm3dreAg6-fdpl3YlS3aSjEyxsk6Sl35-NbmkfDSgMHhd3TLSj2oCL1nZuv_b63LP03dz4kC2s9K4iqZjOvkOLUWiG2rOFzvdYFXO2jy7F4JZhvHnrO4wYZEim6DfV7Wa1v5cKyoizksMOK_qGEltTO3s-hBKrKmLe4HAXr11p0r2z-zLXRN1QR1ya7S7ZOEjdP2SunUzNGTgRLvTAS04qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FcxslmW-5TaJFTq3xwILtoiXtgHotyAGulH6k-dPnxnGGwNw75kClnvAeI2dDrqI17Y18bLb9CKsm_q7Tf6ZcMFaTX7nL5eMaZMYYC1ZodjnBvT9tqszgCPZiijBGiwPJJpxdPlI-suEdAT3mAyDqXfzgQroS9lgrObS0U2HbA7RAidMLQHWhLeGgONeOWHSGHRzSft5nuSHcen1Vbj5JAHNJYyZVA22-3rUyXunocR8PQfF1Bw7EN8KqwGfNf0yE15LsixxpI4O7VI3yzDFeVBXe6ODXKGpn1d2kKERwA_t2iNe3-MMPZzU8nl49fOXE_f_omqlk8hb2VW_p2HxXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gcdtgzwe7MVXi7BHHKOqVM6IeYEOji4ZhVp2WvxNrgeStZxIBCXAd3vxNli7Gpi9kbwwDXGvsJYPlMv5JQk9vcVO1LXeHBYBrJc8GpVwusyS0kysXT4SiFEIZShjUwawUboPnfTtYkKNITnLijPQRbf7VNkTzc8dAwEe6jAqqzlNyQ0vEbRhpytGoHjHZhLIkGfV3g5PV1wcLIIgRlxw2VpSU5QYOxvxs5_AGjTktT96lxqg7f18byAJYcC9Blqzn-9ic3qv1T-WdmsSA9UH3PgJn9SAi-cH6ZJz6swjjfyb033IFjH79p2HgMA_d_gw4GYtByqzyOt1i_9wBFLl3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h4n1JRTZjHHANFHtiYLrP9mEjOBs5273FWofaVXurVLcC_IlgHo6wxKPCmMG-Do2HfPfkHIqDlRYUpPKsMUmhzwtS4L64A9ueKcL1ZrHoc9xdBur9WtIfmKZ59uPirHbjW3fOyh6hmzz_NT4rOTCODn-qbqXHcZpdzbF4rL20ndz2Anm892E3SqXdor2s_ZGpUICZJ4IpIax8ai7IG72nBGII3_px0F3URusMriLEptVhOKOSz4ooPIUBAsQJLrvJ3GidYNZ0mWqJ5L1xaO8s_fdJqvOxAoCbvsJdJg1X0aMUfQro4m0P5CxljC-wQehnbJz22OYy8Nq9aB7-VX0bQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از غرفه خبرفوری در نمایشگاه الکامپ ۲۹
🔹
بازدیدها از غرفه خبرفوری همچنان ادامه دارد و در روزهای برگزاری بیست‌ونهمین نمایشگاه الکامپ، میزبان شما عزیزان هستیم.
🔹
منتظر دیدار شما هستیم.
🔹
نمایشگاه بین‌المللی تهران | سالن ۶ | غرفه ۳۲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/686240" target="_blank">📅 19:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686239">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQaWLNhNtJasQp4vTRl6LHoFr1Vfo-E6iC3coDSuDHd7LmYxX_npB3udVWkQ7BIyhAeGJFrfSL11MdLmItXuiUrbVdkgtllGKY1y6s6shXPsC3QM19-MXktqPfcbFT963xCjV0H_zpyIIQX9HjKhRYPRAPB6BZXQXWWSjMSS5CYgFcuXxcA632Dcmj-VuQZo7H5FRcwsEFWLQZvV2PRutvR7L9gn4db4qrjVwVjCc1804LR2HB2vwOWYHjuetPkwIx4hC7ZH0MOxTHVxX2qXhSyXsIi1KMwEOVXxGuvgwWlnp40RPJIg3amwZkqZZ6e3-mEjcTIKiALCIG74jRa66Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمپول‌های لاغری؛ مُد جدید این روزها؟ یا بخشی از درمان پزشکی؟
🤔
با زیاد شدن صحبت‌ها حول «کاهش وزن با آمپول‌ لاغری» در شبکه‌های اجتماعی، ممکنه این دارو در نگاه اول شبیه یک موج موقت به نظر برسد. اما در سال‌های اخیر، داروهای حاوی تیرزپاتاید جایگاه جدی‌تری در درمان پزشکی چاقی و برخی اختلالات متابولیک پیدا کرده‌اند.
این مولکول شناخته‌شده به اسم
تیرزپاتاید
؛ ماده مؤثره‌ای است که احتمالاً نام آن را کنار
مانجارو (Mounjaro)
شنیده‌اید. در ایران هم
زیکورپا (ZCorpa)، محصول داروسازی دکتر عبیدی، مشابه مانجارو و حاوی تیرزپاتاید است.
💡
استفاده از آمپول لاغری به معنی کنار گذاشتن تغذیه مناسب، فعالیت بدنی یا مراقبت پزشکی نیست و این درمان‌ها برای همه افراد هم مناسب نیستند. انتخاب درمان و دوز مناسب باید زیر نظر پزشک انجام شود.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/686239" target="_blank">📅 19:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686237">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8t4BYDDe1Q6EExvRM6kOd_tINGTDbhE1tkBHP8RlVIAzEBoGA3OACLbVWjnYtC4sm5q1Vj-H3pxpoAZFnX0PUGby6u4OSaSwebNlTJDNE-u5gTZhKWzOatV1kjauYPufriJWDUZUfRB4fOq9WQfev0kn-B2on1uX7zQ0SlAfWX_XywVt7I0RJSgY2jVeI5yTECHhWf_3yQ3ORM05DGIMUJJnCv0Hb1Vzq8409hbtteWzdaasTls6zNZrVsvPtu3CYMouG6qdm22IvEpHcZMLYaBlHJiE7FNC2TMBJw5OX_U1oisHnN4UkLRZRKJOmJWPmDel0nE6c-tHIyd-SxKkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال و مفسر سیاسی آمریکایی:
لطفا ایران، دیگه بدون هیچ ملاحظه‌ای پیش برو و کوتاه نیا. بساط امپراتوری اپستین رو به هم بریز. تمام دنیا با تو هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/686237" target="_blank">📅 19:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686236">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-KOONiYI-wZqJNY4AnvvqNDH19woCNahcxh9XH7btVgWHqdF2cwDVrACkwSrllPSZ-Sgiy6djnVf5JlnQceYnGDxau7ClHX4jeU61hUiBr58n93RCFnAVINC7kJ8JkCKAKxq4_tHtF8jA8BAvmAOmqiNbUDrnUg2BRREKH2j3vYN7yZ6-Hsd6ohcHsWse-jgXG9mer8gfSr6SMNRQG68_GQWKNKkxrGg-hW8YmJNBdeKIKJhHY3kTPY9weZKxC21mDzE_Wm9u_AaTchmMa7vJ4yZbraSSK1UQubD684BSk9QDtcktBCXQt5AObv6TF5M8XYtM-0vrTxNcmS5Nxjug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کمترین قیمت تتر/دلار در صرافی ایرانی ۲۱۱ هزار تومان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/686236" target="_blank">📅 19:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686234">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر خارجه سوریه: اسرائیل به دنبال تثبیت اشغالگری در سوریه است.
🔹
اسکای نیوز: تلفات سیلاب هیمالیا در مرز نپال و چین به ۱۰۶۶ کشته و ۴۴۶۲ مفقود افزایش یافت.
🔹
اتحادیه اروپا: دیپلماسی در تنگه هرمز تاکنون نتیجه‌‌ای نداشته است.
🔹
درگیری ارتش پاکستان با تجزیه طلبان در ایالت بلوچستان/۲۱ مهاجم و ۶ نیروی امنیتی کشته شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/686234" target="_blank">📅 19:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686233">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCNfdREPHgvqHN_q-5iC22I20iwrKw6OiMbNg4OMJVU5wgC186xJoE6ytI4SR9zwOL5TyMrOgZAGx0_1AFRGXVZoa-ndgkRH94bTaiN-SfsUL4jeH2g9d8nI_LiuBWkBT_YQ94Ttbu4bBISRbl9ZzDCX_3-YmY3jKWwmVanb7bIpv6-h8ZpSHTXTjGK8GeVAwPwCxGduwOwKcZpu3wWcArGH9X1AOWVApOLDBqPFEAPZk84PgEhM5rRicum6KjP2Cl_ORBJMQrx3k16p0zWX4GlUthWOQO3uPHWn0va8S1-cSP4qeFKYg7oKL3u4xCXvf7RZmqAh0MagaXSZ8mjeeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تورم و ننه‌جون
🔹
دست غریبه‌ای در یک جیب، شاهدی در جیب دیگر
🔹
امیر نیک‌رویان روزنامه نگار در یادداشتی برای روزنامه شرق نوشت: تقویم سیاست‌گذاری در این جغرافیا، گویی بر مدار استثنا کوک شده است. «مقطع حساس کنونی» دیگر یک برهه گذرا نیست، بلکه به یکی از طولانی‌ترین و تکراری‌ترین فصول تاریخ معاصر ما بدل شده است. روزی تنش‌های منطقه‌ای است، روز دیگر تحریم و بن‌بست‌های دیپلماتیک. بی‌شک هر یک از این تکانه‌ها وزنه‌ای سنگین بر دوش اقتصادند، اما مسئله از جایی آغاز می‌شود که این شرایط استثنائی در پی تکرار مدام، به وضعیت عادی و توجیهی همیشگی برای ناکارآمدی تبدیل می‌شود. اساسا ساختار دولت برای اداره کشور در دل همین واقعیت‌های سخت شکل می‌گیرد، نه برای مدیریت یک ایران فرضی که در آن خبری از تحریم نیست و بازار ارز چشم‌انتظار اخبار سیاسی نمی‌ماند.
ادامه
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/686233" target="_blank">📅 19:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686232">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
هشدار سفارت آمریکا نسبت به «تشدید تنش‌ها» و لغو پروازها در فلسطین اشغالی
🔹
رسانه‌های اسرائیلی از ارسال پیام هشدارآمیز سفارت آمریکا در قدس اشغالی به تمامی شهروندان آمریکایی حاضر در منطقه خبر دادند.
🔹
این سفارتخانه در ایمیلی رسمی، نسبت به احتمال «تشدید غیرمنتظره تنش‌ها» به اتباع خود هشدار داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/686232" target="_blank">📅 18:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686231">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc022fce85.mp4?token=psV4uQpt2-5bM57sZNCyLuWe0QO7BeDLR3S2L0tr6O3PEaF3qRUI8gZfUimTE7XMD6m06RDmBIf7j-octfw1jxJ3mbQjipL5B-KJR8NsVY1XPCgFICXhKKPTyjQHFq_nnryfe62J5A_4xE-2CUnPrYoCAMfTOydRw5hHbJtkHX6YhaIjATRYxcPLN8a7zupHVeA0EfAY-DSG5Ja80YSxP_dXV-X3FLuJD9dllaDj6WXWqJeYFW1kT6uFQ9-mjWEHQv3iLPJPGrWcQScq7oa1cIhYOmQjSOsQ0Fq8B0836FPwzTi9A4BOxTChd5c8-tBWzhIrtPOyielQFHk40Fa7yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc022fce85.mp4?token=psV4uQpt2-5bM57sZNCyLuWe0QO7BeDLR3S2L0tr6O3PEaF3qRUI8gZfUimTE7XMD6m06RDmBIf7j-octfw1jxJ3mbQjipL5B-KJR8NsVY1XPCgFICXhKKPTyjQHFq_nnryfe62J5A_4xE-2CUnPrYoCAMfTOydRw5hHbJtkHX6YhaIjATRYxcPLN8a7zupHVeA0EfAY-DSG5Ja80YSxP_dXV-X3FLuJD9dllaDj6WXWqJeYFW1kT6uFQ9-mjWEHQv3iLPJPGrWcQScq7oa1cIhYOmQjSOsQ0Fq8B0836FPwzTi9A4BOxTChd5c8-tBWzhIrtPOyielQFHk40Fa7yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشته شدن مقام ارشد بانکی آمریکا در چاقو کشی در نیویورک
🔹
یکی از معاونان بزرگترین بانک آمریکا در حادثه چاقوکشی در میدان تایمز در نیویورک به قتل رسید.
🔹
بانک او آمریکا شرکت خدمات مالی و بانکداری چندملیتی آمریکایی است، که اکنون به‌عنوان بزرگترین بانک  این کشور شناخته می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/686231" target="_blank">📅 18:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686230">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پیشنهاد جدید برای وام ازدواج؛ ۷۰ درصد کالا و ۳۰ درصدنقد
سید نجیب حسینی، عضو کمیسیون بودجه در
#گفتگو
با خبرفوری:
🔹
حدود ۶۰۰ تا ۷۰۰ هزار نفر در صف دریافت وام ازدواج هستند.
🔹
پیشنهاد جدید این است که به‌جای پرداخت کامل پول نقد، با فروشگاه‌ها قرارداد منعقد شود و بخشی از تسهیلات به‌صورت کالا، در جهت حمایت از تولید ملی و هدفمند شدن مصرف وام، در اختیار زوجین قرار بگیرد.
🔹
این طرح می‌تواند به مدیریت نقدینگی در جامعه و کنترل تورم کمک کند و احتمالا به‌صورت ۷۰ درصد کالا و ۳۰ درصد وجه نقد اجرا شود.
🔹
بسیاری از مردم توانایی تامین ضامن را ندارند و حتی برخی افراد برای ضمانت، مبالغی دریافت می‌کنند.
🔹
با توجه به محدودیت منابع در شرایط جنگی، فعلا امکان افزایش مبلغ وام ازدواج وجود ندارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/686230" target="_blank">📅 18:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686229">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/734d98cea5.mp4?token=j_OAF0nt9E1Wj7vUxDu3Yl7W1Z1007LNSZNnsRJw3O3XooNEfTIIykLF0X2NgF3TQNrR688fopOMqQmPK2YHUWHPXqOJ_hDou5pWuCZbS5YypERzYgrGAJdParRhFyb3puDkxyxOsbGA7GWekbQFNW1XOf8byt8wQfY3NXhoHI7HVhcKWtmFUiZgbY1_rlzwncFZ78Q38edxO2RX04TIlUp14bOWa1czGvdbZVx8k1GDuMfuUzTsHxY-7GmkTN2Go9YyB1SSfyWofmMLgm_blTACwo0DqAc27IvEgNJ3Q0GDLnAvYviRK1_GOcdbOgrKtj9NMbaZInfCory_JM4L4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/734d98cea5.mp4?token=j_OAF0nt9E1Wj7vUxDu3Yl7W1Z1007LNSZNnsRJw3O3XooNEfTIIykLF0X2NgF3TQNrR688fopOMqQmPK2YHUWHPXqOJ_hDou5pWuCZbS5YypERzYgrGAJdParRhFyb3puDkxyxOsbGA7GWekbQFNW1XOf8byt8wQfY3NXhoHI7HVhcKWtmFUiZgbY1_rlzwncFZ78Q38edxO2RX04TIlUp14bOWa1czGvdbZVx8k1GDuMfuUzTsHxY-7GmkTN2Go9YyB1SSfyWofmMLgm_blTACwo0DqAc27IvEgNJ3Q0GDLnAvYviRK1_GOcdbOgrKtj9NMbaZInfCory_JM4L4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: به ملت بزرگ ایران اطمینان می‌دهم با عنایات الهی، حضور مردم در صحنه و انسجام مسئولان ذیل رهنمودهای رهبر انقلاب، ایران عزیز از این آزمون بزرگ سربلند بیرون خواهد آمد و افتخار عظیمی برای ایران در تاریخ جهان ثبت خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/686229" target="_blank">📅 18:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686226">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09df224f40.mp4?token=vu5wGxj2PtJBpSzQwDSkPuNbRhb35frGxKhfqmdadE0HXoM1DNmeFoGT1KZK6yJf6uehANH8I7bb8tpvrZJiE0KhUUOtyhr8PbLIpHuyTJUZ1xuNP_-7XEWzuWK4ztklh9_BafABJGkM4hl2gpyO72WbVE0-3PepGpc4oquBmkZSIuOIlc3k9qcd7CpkfIRQL-qbXXyPZIOPCVZi_OkaZgC6IijXQM4dVdkeURIyRRbqh_cLwU37XtnNi5B_27587HJ5SEnx6cVe6jEILtvVtHWAu3qBbzaQ_OxyvQ7XEgT5syumMPmkAw9aOcKPVkZmMqxElmmkiWOjlAxMJXoq5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09df224f40.mp4?token=vu5wGxj2PtJBpSzQwDSkPuNbRhb35frGxKhfqmdadE0HXoM1DNmeFoGT1KZK6yJf6uehANH8I7bb8tpvrZJiE0KhUUOtyhr8PbLIpHuyTJUZ1xuNP_-7XEWzuWK4ztklh9_BafABJGkM4hl2gpyO72WbVE0-3PepGpc4oquBmkZSIuOIlc3k9qcd7CpkfIRQL-qbXXyPZIOPCVZi_OkaZgC6IijXQM4dVdkeURIyRRbqh_cLwU37XtnNi5B_27587HJ5SEnx6cVe6jEILtvVtHWAu3qBbzaQ_OxyvQ7XEgT5syumMPmkAw9aOcKPVkZmMqxElmmkiWOjlAxMJXoq5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: نباید فراموش کرد که همین الان نیز در جنگ هستیم
🔹
پیام رهبر انقلاب، با ذکر جزئیات دقیق، تکلیف همه ما را روشن کردند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/686226" target="_blank">📅 18:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686225">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXyJbmxGfYmNGU3xYN9OapHfISbxKZi4N5BMssVwTnf2qUQWRkpVGXgF5Pq7ZSUOv0NJdVoq53HSMfIhHacaMbR7dCPxPez80YBbOuQ2X8hRi1caCglX70mJ15Bhzn7XXwhhjOtxr8rVwxV-V8Uus5si1MRcBp9d2RRXCdj6ArnOW8CFsKzupxP5OxiJl15sCcII2fvqHqYtX1Boq4-wf7k4igxhIb-yAKFMh2TVvrRk1HuDHpgmAAgLdXwwpzHQGfnbsVEOtKqeqmFwqVAKGRktQPZxb3vKuTNzcptesrAWv66xOeRRfwpHDncO06kDjtqgtp7uobU6glPLJvmQqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایزی‌لایف حامی صعود به قله دماوند
🔹
ایزی‌لایف در ادامه رویکرد مسئولیت اجتماعی خود برای تغییر نگاه به بی‌اختیاری ادرار، از صعود مهرداد شهلایی و تیم کوهنوردی انجمن ام اس به قله دماوند حمایت کرد.
🔹
این صعود در ۳ شهریور انجام شد تا بار دیگر بر یک پیام مهم تأکید شود: بی‌اختیاری ادرار نباید محدودیتی برای یک زندگی فعال باشد.
🔹
ورزش، طبیعت‌گردی، سفر و دنبال کردن تجربه‌های تازه، همچنان می‌تواند بخشی از زندگی افراد باشد؛ حتی زمانی که با بی‌اختیاری ادرار زندگی می‌کنند.
🔹
ایزی‌لایف در کنار تولید محصولات مدیریت بی‌اختیاری ادرار، تلاش می‌کند با فعالیت‌های مسئولیت اجتماعی و افزایش آگاهی، به شکستن تابوی صحبت درباره بی‌اختیاری ادرار و تغییر نگاه جامعه نسبت به این موضوع کمک کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/686225" target="_blank">📅 18:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686224">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dffdbc0af.mp4?token=C2TV9ZO20vWXjfrev2KwUURTGiHbX_az1hzg_qsPRu9yTku7ytwRg34DuXiXNTc3inhTXf1RpTle-GkNnsXQDNNL7bNAOT1A0QkHuuqP-x_S5r0aYcU5ktdx-EVYkAJnBHUDmtnGf1C1CfbrNnBDQM3IoJ38pcmXD8Zyv-KcnrKfevtD0Ai75u3W_K-9idMPYqYbVUOObUndvu2Hv1ozzJtXOgNRFkjDNugW0XQN_zJf22Ic6fxrlFU8Qlzwa6XWWv4LVDLJtuEacKFzmrYvs80lh6Imh_B_8SULXoFBpdGG-4C8z9anz5GLFITBmhRiRmwHIct9wANGH1jl9zwBtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dffdbc0af.mp4?token=C2TV9ZO20vWXjfrev2KwUURTGiHbX_az1hzg_qsPRu9yTku7ytwRg34DuXiXNTc3inhTXf1RpTle-GkNnsXQDNNL7bNAOT1A0QkHuuqP-x_S5r0aYcU5ktdx-EVYkAJnBHUDmtnGf1C1CfbrNnBDQM3IoJ38pcmXD8Zyv-KcnrKfevtD0Ai75u3W_K-9idMPYqYbVUOObUndvu2Hv1ozzJtXOgNRFkjDNugW0XQN_zJf22Ic6fxrlFU8Qlzwa6XWWv4LVDLJtuEacKFzmrYvs80lh6Imh_B_8SULXoFBpdGG-4C8z9anz5GLFITBmhRiRmwHIct9wANGH1jl9zwBtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان برنامه و بودجه: انسداد تنگه هرمز برنامه‌ریزی شهید پاکپور بود
🔹
شهید پاکپور پیش‌بینی کرده بود که جنگ با ترور او شروع می‌شود؛ شهید پاکپور برنامه‌ریزی کرده بود که اگر جنگ آغاز شد و او دستوری صادر نکرد، فرماندهان ۲۰ دقیقه بعد شلیک کنند.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/686224" target="_blank">📅 18:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686223">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b450dc735.mp4?token=UhnfXsePf7afhEkJgTb2lzmLEUxnLRvvDwZGkyu8JYNQWwly6ZMJ52cdINp2QE6LkSjrLHWeQ-wWuQLGRefwSO4_8FedwPQR2pvcaT7pD084kKdoicjqUyZlZwrZd2TZJaiCB8WgJGb_06YZoLizkBBni7SWdxH9O2sW7fH727WALYBsBd794qMuWUUPcZHlPSnY7BM1RcALCdBcGm4kKv5DFTLuOq2zHFPjt6OdJJO8R_0GMNzifVbDgdkFTo_Qn23Y0rjsKxScZJJFa2jAPLxErS5uZUq6J0KGjrHjR1xVMMrnNreQCSCkuGUIwX-hWQLn_yMs00WU_bOQpuMZ9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b450dc735.mp4?token=UhnfXsePf7afhEkJgTb2lzmLEUxnLRvvDwZGkyu8JYNQWwly6ZMJ52cdINp2QE6LkSjrLHWeQ-wWuQLGRefwSO4_8FedwPQR2pvcaT7pD084kKdoicjqUyZlZwrZd2TZJaiCB8WgJGb_06YZoLizkBBni7SWdxH9O2sW7fH727WALYBsBd794qMuWUUPcZHlPSnY7BM1RcALCdBcGm4kKv5DFTLuOq2zHFPjt6OdJJO8R_0GMNzifVbDgdkFTo_Qn23Y0rjsKxScZJJFa2jAPLxErS5uZUq6J0KGjrHjR1xVMMrnNreQCSCkuGUIwX-hWQLn_yMs00WU_bOQpuMZ9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: تا زمانی که تعهدات آمریکا در تفاهم‌نامه اجرایی نشود تنگه باز نخواهد شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/686223" target="_blank">📅 18:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686222">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff0f494e4.mp4?token=pvZ_dElzh0CAVMjW2uCCyYAIXLKoGtZcAF9L79YiiWPslnIkwLbn7ng0iPS_Ma5j07pafnA5Xkgi0G0GICUFK60ezzw-AS5tvSAumTDkTI8YOXaZRa28JxCA7ygZyajqFiwWn2lvF4X5NQDeOiB6qVw959-agJPrgfTuWkoehRGY5NPmxG2FPCdANFsNH3AnYjPHO3YB-TVXb3DP6WdJFJ8R_seZyQOLeHhNAIMGsa1j5ZkIVAIQinfkW4p9bYyFuwDebnZI8d0F66g-Y05kTF5kGjgOsOPTo_Bmxfx6VP_ogYkNJ2ZL9DKq-OoJ_loR6j9JNukTVtVtDkZnkiwzqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff0f494e4.mp4?token=pvZ_dElzh0CAVMjW2uCCyYAIXLKoGtZcAF9L79YiiWPslnIkwLbn7ng0iPS_Ma5j07pafnA5Xkgi0G0GICUFK60ezzw-AS5tvSAumTDkTI8YOXaZRa28JxCA7ygZyajqFiwWn2lvF4X5NQDeOiB6qVw959-agJPrgfTuWkoehRGY5NPmxG2FPCdANFsNH3AnYjPHO3YB-TVXb3DP6WdJFJ8R_seZyQOLeHhNAIMGsa1j5ZkIVAIQinfkW4p9bYyFuwDebnZI8d0F66g-Y05kTF5kGjgOsOPTo_Bmxfx6VP_ogYkNJ2ZL9DKq-OoJ_loR6j9JNukTVtVtDkZnkiwzqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: در آغاز گفت‌وگوها، آمریکا یک متن ۱۵ ماده‌ای در خصوص هسته‌ای، موشکی و محور مقاومت ارسال کرد؛ اما امروز وقتی متن ۱۴ ماده‌ای نهایی را نگاه می‌کنید، می‌بینید دشمن از همه آن‌ها عقب‌نشینی و رئیس‌جمهور آمریکا پای این سند را امضا کرد
🔹
چارچوب مذاکراتی…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/686222" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686221">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
قالیباف: در آغاز گفت‌وگوها، آمریکا یک متن ۱۵ ماده‌ای در خصوص هسته‌ای، موشکی و محور مقاومت ارسال کرد؛ اما امروز وقتی متن ۱۴ ماده‌ای نهایی را نگاه می‌کنید، می‌بینید دشمن از همه آن‌ها عقب‌نشینی و رئیس‌جمهور آمریکا پای این سند را امضا کرد
🔹
چارچوب مذاکراتی را ما تنظیم کردیم و دشمن را وادار کردیم پیروزی‌های میدان را تبدیل به سند سیاسی کنیم.
🔹
اجرای سند به اندازه امضای آن نیز مهم است؛ اما بدانید وقتی سندی امضا نشود، راهی برای اجرای آن نیز نیست.
🔹
با قدرت، منطق‌مان را بر دشمن تحمیل کنیم و هرگز تسلیم نظامی یا سیاسی نخواهیم شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/686221" target="_blank">📅 18:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686220">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65bc99871.mp4?token=MIDKUu6A2AIwoFxX1TT4MdExjXAN6UDcgtSsHtnmcSlbtcml8jIc2DeJsjYFpY9uaba00HBNnNKkrNuMoA9gMEJbmWTG9lelH2MF8vTmjsclRjraRruI2lg0GtY-ZKnpwRY1iFKUIPWsuIn1CObxgCtOW3fJoiAenRsNSFc-ZtJ2yVkihl4i-8ugNvBWdLQBK8h534JAAvdIVSHaZEXOJG3FmJOeAf-uQSatjlTT3DF7VLFBRAAil8QHH_WwaTrAMAHN_JNmX0CqWyPJyyiiffkBVtfu_PQxkQDO6VNKys8J4iwFI6RXmCNlL6QgSuKHt2TJJ9Pqiss9RTxv5bHpiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65bc99871.mp4?token=MIDKUu6A2AIwoFxX1TT4MdExjXAN6UDcgtSsHtnmcSlbtcml8jIc2DeJsjYFpY9uaba00HBNnNKkrNuMoA9gMEJbmWTG9lelH2MF8vTmjsclRjraRruI2lg0GtY-ZKnpwRY1iFKUIPWsuIn1CObxgCtOW3fJoiAenRsNSFc-ZtJ2yVkihl4i-8ugNvBWdLQBK8h534JAAvdIVSHaZEXOJG3FmJOeAf-uQSatjlTT3DF7VLFBRAAil8QHH_WwaTrAMAHN_JNmX0CqWyPJyyiiffkBVtfu_PQxkQDO6VNKys8J4iwFI6RXmCNlL6QgSuKHt2TJJ9Pqiss9RTxv5bHpiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این ۱۵ الگو را یاد بگیر؛ گرامر انگلیسی را فتح کن #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/686220" target="_blank">📅 18:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686218">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e47ef015.mp4?token=PKmb5pN_AmFOxzerZCpuivglYnkLndIFhfDC8CeiqdMMZDdH8UmVollwYpeq8O-NYJ5XwZoky7QY6_MrE6or1SnMaJW_x5AMcKg6FORVxnowYby4IDbAywhD8saKI4O6fejPffBbPvL_a5t6y15cpSvrDivovx5PMhuyr8l9ySHJupLuS8u-87y4vZU4VbEtamGYBORo47mFTIdD2--F5GxPAzRfFfutEcRTszO4nqXkHMsUgm6k4caxULIglzlanpnSTeJEYFaQ8KYY3DuFCTXlA3AcxHI6ETn-gr5skoWjM_C72ED26lE1Ot0ZOEyfK7kOTpxyAsTDL-lVBvhfgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e47ef015.mp4?token=PKmb5pN_AmFOxzerZCpuivglYnkLndIFhfDC8CeiqdMMZDdH8UmVollwYpeq8O-NYJ5XwZoky7QY6_MrE6or1SnMaJW_x5AMcKg6FORVxnowYby4IDbAywhD8saKI4O6fejPffBbPvL_a5t6y15cpSvrDivovx5PMhuyr8l9ySHJupLuS8u-87y4vZU4VbEtamGYBORo47mFTIdD2--F5GxPAzRfFfutEcRTszO4nqXkHMsUgm6k4caxULIglzlanpnSTeJEYFaQ8KYY3DuFCTXlA3AcxHI6ETn-gr5skoWjM_C72ED26lE1Ot0ZOEyfK7kOTpxyAsTDL-lVBvhfgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: دولت و مجلس مصمم به افزایش کالابرگ، مخصوصاً برای دهک‌های ضعیف جامعه هستیم و در اولین فرصت اجرایی می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/686218" target="_blank">📅 18:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686217">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxAFMKlefvzSpf7PUgY4CXVSsY6d7tdBSUjXprJbMxb3RnbgKaGCqfwWaiuf3_YV1uHdAr38SWaclZjnW-cK2hxzeDPZSmKel5VMuMH3adTVQ-pk8RWxvAlnnhDN-I7PIY1HscMCsQK9McxqzZernEVbl8klgoyVdkzyb7Z89qOqkpsEPibaSYMQx75lcCbTvm_EM1SwYIs8vAMwkX78cOI87HWGSXu5QhFOXdmh3M_UHe7mp_u9_qaS_GUYsFaukPnY4uBYA29zLcjGFxHVvcOkh9mCZceE-PcxhbPcS27ziX7TcFkZ3G5by81lwHzjQzBjvH4fzGUhxz-I5UbREQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازار سیاه بلیت دربی داغ شد؛ تا ۷ میلیون تومان!
🔹
با وجود فروش رسمی بلیت دربی استقلال و پرسپولیس، قیمت‌ها در بازار سیاه به ۲ تا ۷ میلیون تومان رسیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/686217" target="_blank">📅 17:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686216">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ec52fc94.mp4?token=MtAlNpi5iRdML5IfQRTTtRO2MZOqGd5wDLr14dF5-r8kUGtBVdN9HB4DHnfHNJQ-hQjHD83BKRtfuG7LWQek5S-mGVfV4es3P_8wmrxlyVRFRa31vFzy-4TCFhyEK78Twm54QbmafG2w3kkjEDYyP7kLWIT2qvwXCSQkcmBDfvaNupuqhbpugEG47Ip3XOgCvzaajSXBxDdRcCYl9uCAImWc_vYWkYbfdxS9Xw7UJRjjYuv19kVg8sDBaVUF0ZhfiyxmJja33ufbWTygAyWCG_Qgs7IUVkn6KnDcxHCJYi9mwtVO73sgOw6NZwGP8OOoA7qhmiE6xcdK8Wp2O1QEJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ec52fc94.mp4?token=MtAlNpi5iRdML5IfQRTTtRO2MZOqGd5wDLr14dF5-r8kUGtBVdN9HB4DHnfHNJQ-hQjHD83BKRtfuG7LWQek5S-mGVfV4es3P_8wmrxlyVRFRa31vFzy-4TCFhyEK78Twm54QbmafG2w3kkjEDYyP7kLWIT2qvwXCSQkcmBDfvaNupuqhbpugEG47Ip3XOgCvzaajSXBxDdRcCYl9uCAImWc_vYWkYbfdxS9Xw7UJRjjYuv19kVg8sDBaVUF0ZhfiyxmJja33ufbWTygAyWCG_Qgs7IUVkn6KnDcxHCJYi9mwtVO73sgOw6NZwGP8OOoA7qhmiE6xcdK8Wp2O1QEJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: اگر محاصره را تشدید کنند، حتماً پاسخ نظامی می‌دهیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/686216" target="_blank">📅 17:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686215">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: ناتو اسلامی را باید ایجاد کنیم
احمد فاطمی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
اشتراکات فرهنگی، دینی، اعتقادی و تاریخی کشورهای اسلامی به اندازه‌ای گسترده است که می‌توان با کنار گذاشتن اختلافات، به یک وحدت و همگرایی منطقه‌ای قوی رسید و زمینه تشکیل یک ناتو اسلامی را برای مقابله با زیاده‌خواهی صهیونیست‌ها و استکبار جهانی فراهم کرد.
🔹
تحقق این وحدت نیازمند آن است که کشورهای اسلامی با تکیه بر منافع مشترک و واقعیات میدانی، از وابستگی به قدرت‌های خارج از منطقه فاصله بگیرند و با تصمیم‌گیری مستقل، مسیر همگرایی و همکاری منطقه‌ای را دنبال کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/686215" target="_blank">📅 17:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686214">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6410ffa96.mp4?token=h1h4FJnMEdWIGZr4I2x_KF9vnsV0SCVvy3m9Ojzgsf8yuhhMXMJNEnuFaITDAXbnmLZmFeHH7Erh0-kXW1v7wJMdDRDsE4Q9dVt4YnLshNoSRLoxvIOsI3NcCFuyfyUIUy5BUwyIinVLzWxwHZ6abcbSNrzjsR3KO09kLRrO3NKN-_YXrOMLkBG2liSeiyjZ20Sjh42RJbX4uOpR10A-pNGmK5bNgyhGk8IIkW0TpGIztR_3v-PgxnXK1bsOCjN4I8ClyZnVorXhZ5EmuM5tNQKcTLTGr5epYH-GyQFF-4jEZFLRPpBDQoFZuKNrZ-1mUUEoy9n4cU8IIW5faTgFFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6410ffa96.mp4?token=h1h4FJnMEdWIGZr4I2x_KF9vnsV0SCVvy3m9Ojzgsf8yuhhMXMJNEnuFaITDAXbnmLZmFeHH7Erh0-kXW1v7wJMdDRDsE4Q9dVt4YnLshNoSRLoxvIOsI3NcCFuyfyUIUy5BUwyIinVLzWxwHZ6abcbSNrzjsR3KO09kLRrO3NKN-_YXrOMLkBG2liSeiyjZ20Sjh42RJbX4uOpR10A-pNGmK5bNgyhGk8IIkW0TpGIztR_3v-PgxnXK1bsOCjN4I8ClyZnVorXhZ5EmuM5tNQKcTLTGr5epYH-GyQFF-4jEZFLRPpBDQoFZuKNrZ-1mUUEoy9n4cU8IIW5faTgFFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: اگر محاصره را تشدید کنند، حتماً پاسخ نظامی می‌دهیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/686214" target="_blank">📅 17:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686213">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما مهم‌ترین دلیل رواج پیدا کردن خریدهای اینترنتی چیست؟</h4>
<ul>
<li>✓ امکان خرید اقساطی</li>
<li>✓ مقایسه آسان‌تر قیمت‌ها و کالاها</li>
<li>✓ تنوع بیشتر محصولات</li>
<li>✓ تخفیف‌های دوره‌ای</li>
<li>✓ صرفه‌جویی در زمان</li>
<li>✓ تحویل آسان درب منزل</li>
<li>✓ سایر موارد</li>
</ul>
</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/686213" target="_blank">📅 17:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686212">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
بازار دارو در ایران ۴۰۰ همتی شد
🔹
بازار تأمین دارو در ایران در سال ۱۴۰۴ به حدود ۴۰۰ هزار میلیارد تومان رسید؛ بازاری که همزمان با رشد تولید داخلی، از مرز ۵ میلیارد دلار عبور کرد.
🔹
تولید داخلی دارو از ۵۱.۴ میلیارد عدد در سال ۱۴۰۳ به ۵۷.۴ میلیارد عدد در سال ۱۴۰۴ رسید.
🔹
رشدی ۱۱.۶ درصدی که نشان‌دهنده افزایش قابل‌توجه حجم تولید در صنعت داروسازی کشور است؛ ارزش دلاری بازار نیز از ۴.۵ میلیارد دلار به حدود ۵ میلیارد دلار افزایش یافت.
🔹
رقمی که از این میان حدود ۸۵۰ میلیون دلار سهم واردات و ۴.۱۵ میلیارد دلار سهم تولید داخل بوده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/686212" target="_blank">📅 17:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686210">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01a80eb3ed.mp4?token=Avbfr1Nl0PT77X6djT5a5_9eTdBKIFf1GzaXkusxACeqFQiGUuwTcWQOcRgQyy55i_jMt4fI1A1QPLeDgl9oOqz_7_feRgSvrATW-IXLxfy-Nw9nnKD4FvrjulcFNM6nSEJ-7EUvlzWc3ZN9Mz41rXpSDc7889IMdC6g7w64vl0VcIHN4q1iGvD5LBmQ2VbIA2-gH9P5ZKluyYJU7ZwE77F_H7EjAKFwsA3_sjqyZzCNslxbeB8VGKKF7k3o3zOtagBQE7O7t1XKtLDyl-UOSbcTySlLdsMtdRZkrTd-VbkCsYQlSRCj5oBA7cCxG3kIJuaMhvEXUPrsYyJOXR0OFXdhLoGpWMiaPlyYIk26qO5BFnHAGgYzIBjFElhiub0tLwmzqLPjlahZb4O0bcXf9iggsOD-0cWRzZCe8uqXlTJOxJnJL1omv8MrEQFIDFAMN5V25rpCttcasr-cJHvAl4sn_1JW-kNQ0R2AJY0X7ilClUiF3yA8Dn6X-G8ji25-4GIqxe1hTkFqhNqBqm8iuvz25fJroq7A4TPZV0nQ9xgX2ORUR65kwSR7KFcooQRDsEfMezUIl4-bpBULc73ueAWJwTev8sBgnMTsa60xAXpa38kKz4C9JWY-PvIlmvWvtAXvG-jBm9pXpTTNQpv2B34n0QiKiXCHOtv6cykC4Wk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01a80eb3ed.mp4?token=Avbfr1Nl0PT77X6djT5a5_9eTdBKIFf1GzaXkusxACeqFQiGUuwTcWQOcRgQyy55i_jMt4fI1A1QPLeDgl9oOqz_7_feRgSvrATW-IXLxfy-Nw9nnKD4FvrjulcFNM6nSEJ-7EUvlzWc3ZN9Mz41rXpSDc7889IMdC6g7w64vl0VcIHN4q1iGvD5LBmQ2VbIA2-gH9P5ZKluyYJU7ZwE77F_H7EjAKFwsA3_sjqyZzCNslxbeB8VGKKF7k3o3zOtagBQE7O7t1XKtLDyl-UOSbcTySlLdsMtdRZkrTd-VbkCsYQlSRCj5oBA7cCxG3kIJuaMhvEXUPrsYyJOXR0OFXdhLoGpWMiaPlyYIk26qO5BFnHAGgYzIBjFElhiub0tLwmzqLPjlahZb4O0bcXf9iggsOD-0cWRzZCe8uqXlTJOxJnJL1omv8MrEQFIDFAMN5V25rpCttcasr-cJHvAl4sn_1JW-kNQ0R2AJY0X7ilClUiF3yA8Dn6X-G8ji25-4GIqxe1hTkFqhNqBqm8iuvz25fJroq7A4TPZV0nQ9xgX2ORUR65kwSR7KFcooQRDsEfMezUIl4-bpBULc73ueAWJwTev8sBgnMTsa60xAXpa38kKz4C9JWY-PvIlmvWvtAXvG-jBm9pXpTTNQpv2B34n0QiKiXCHOtv6cykC4Wk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی پربازدید در فضای مجازی از مراسم افتتاحیه جام‌جهانی بازی‌های محلی در قرقیزستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/686210" target="_blank">📅 17:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686208">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8bf6ee6b0.mp4?token=TdK2-CR3EZZgbi4LcdedEYNutvZddzsOKmwYKX6FkrsJmrc34YX0saCv4L6U0L__kDYaWctbV3WOJ0R2v1CWr6qpM4b3sUxVbM-jopdL2ngrGzd4E8iHfDx9MqrWfzzf-mbUaoAVieDQjWgtZ8BDaEcSpMYfSa7MqSe3uUxLzj-rCXJoFx2aoeLeoxZ1OsMcjcl8Om66tukn5SwypWK3PDN54B6R00NkakC1HN9Thi16k6Y2riqMaBxYoB9EnhQeKMvegKiCp7F6o2h1KMZ1p-lTmwnvnQGkprEPZGWY-6JRky2AydIvShKgrmi_BYDRYWXzXy0dFthm_RgKkGe7qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8bf6ee6b0.mp4?token=TdK2-CR3EZZgbi4LcdedEYNutvZddzsOKmwYKX6FkrsJmrc34YX0saCv4L6U0L__kDYaWctbV3WOJ0R2v1CWr6qpM4b3sUxVbM-jopdL2ngrGzd4E8iHfDx9MqrWfzzf-mbUaoAVieDQjWgtZ8BDaEcSpMYfSa7MqSe3uUxLzj-rCXJoFx2aoeLeoxZ1OsMcjcl8Om66tukn5SwypWK3PDN54B6R00NkakC1HN9Thi16k6Y2riqMaBxYoB9EnhQeKMvegKiCp7F6o2h1KMZ1p-lTmwnvnQGkprEPZGWY-6JRky2AydIvShKgrmi_BYDRYWXzXy0dFthm_RgKkGe7qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: قدرت نظامی ایران در تنگهٔ هرمز حفظ و ارتقا پیدا کرده است
🔹
اعمال مدیریت ایرانی بر تنگه، هیچ منافاتی با قوانین بین‌المللی ندارد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/686208" target="_blank">📅 17:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686207">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIrb6SRpczoZlH235mLsfusOg3ajFwkCB5oBzn75a2VlRYDdTJp_TWcqABdl_ovVNERBp6iTWYZVtZF2WHd4WnBb-X3anOJgztjHO4GDAjauupZUBt3t3byAU6oFeiRn-Si7PIxb5P8vjchxZrxVhEzT7W4t62GA4E3OHIYjPeUO30qhlM8VoLNnfoxkkoVS-_vE9DvezhkgjrLF9pp37buzd_DwnbFF_z4ahM06mGZmS0Lvm9mwFkx8zLFO5HWIsMI-ccjJPK9jd6F1feuK5e3fd2xNkON7AekKe5LHlgxmyWIOu_gs2fXTzHfxdQoFiKfesx33lp-i5b1cDPZ-5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علی کریمی پس از دعوا با هواداران رضا پهلوی، گوشه‌نشین شد
🔹
او پیش از این نسبت به فحاشی سلطنت‌طلبان گلایه کرده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/686207" target="_blank">📅 17:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686206">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3345c0aee0.mp4?token=nTXHDw2b87FuB0kcw3mIL72DI1ms-DEW-Ry-FXYM4EfwMEOo2ZJOnc_ENS6VRjWfXFm7h7mPHY1sJTGhH9zFHyN_VLvWP1bQTbsYuNsFXuOkNzRR-VuopwQpKWaAZxKA2KuUdoQ0o0sxA-MhWx_xoH4G39pJgcOdxkYexMrOl0ufGMPj4ZFUZ0g_i5DQEyKsl92JSG_xqi75FFzYevSjmPZ9T3VfoN_-YM6SnQrcG4Zio9ABAbkA5RmDlEAQoHXiQxM8Bon4xVC3by811HHbSIsm-OUlhXOeSvcw6uJBugfc1LcNkiE9-1iTfV2N9e1l9enc8J_JerNP_-2A9lUZnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3345c0aee0.mp4?token=nTXHDw2b87FuB0kcw3mIL72DI1ms-DEW-Ry-FXYM4EfwMEOo2ZJOnc_ENS6VRjWfXFm7h7mPHY1sJTGhH9zFHyN_VLvWP1bQTbsYuNsFXuOkNzRR-VuopwQpKWaAZxKA2KuUdoQ0o0sxA-MhWx_xoH4G39pJgcOdxkYexMrOl0ufGMPj4ZFUZ0g_i5DQEyKsl92JSG_xqi75FFzYevSjmPZ9T3VfoN_-YM6SnQrcG4Zio9ABAbkA5RmDlEAQoHXiQxM8Bon4xVC3by811HHbSIsm-OUlhXOeSvcw6uJBugfc1LcNkiE9-1iTfV2N9e1l9enc8J_JerNP_-2A9lUZnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: دشمن بداند در دوره‌های بعدی جنگ، هم در بُعد کیفی و هم کمی، مسلط‌تر خواهیم بود
🔹
نیروهای مسلح از هر فرصتی که به آن‌ها بدهیم برای بازسازی توان خود استفاده می‌کنند و حتی ساعت و لحظه‌ها را هم از دست نمی‌دهند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/686206" target="_blank">📅 17:22 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
