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
<img src="https://cdn4.telesco.pe/file/fldyJwPOM5x17hiZWuEO6bH7Wq8f60iZcvc01qljUUbhex_jc_galL05S73ryRqoHxT7bGScSDtOYwttEXmiWO_-Kb82fZB1thcxRkn3Q904gzMShbMrpP_WgOVBJT-828PH716NZ9YZgDLdF2dqPaHFPjn9ffMyE4RuCaf8QY4FxOOYGRPjpyfpwuBJCbepgO4VC4RyMI4_o0XCpcx43ukyLPA36uFJHyqvH1Q8hyjFylwZ3BQn2piKf0-lGYrW4JBtrYlWD4uUEVI0KStxKv-zDJbdEV_OsOU7Xlw-4Jn9ob8u_GrU8Ci4tB1R260yF4-XfaQAf1qNMQU7hwKVxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 22:35:21</div>
<hr>

<div class="tg-post" id="msg-451729">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔸
لطفاً در خصوص پرداخت معوقات بازنشستگان تأمین اجتماعی پیگیری لازم را انجام دهید. با توجه به وعده‌های پرداخت معوقات در ماه‌های گذشته و عدم تحقق آن، سطح نارضایتی بین این قشر زحمت‌کش به حد اعلا رسیده است. امید است با پیگیری از مسئولین مربوطه، مرهمی بر درد این عزیزان باشد.
🔹
نیروهای شرکتی ظفر کویر دامغان و کومش کار از تأخیرهای مکرر در پرداخت حقوق، بلاتکلیفی معوقات و نبود قراردادهای شفاف و قانونی گلایه‌مند هستند. این کارکنان با وجود نقش مهم خود در حفظ و پایداری شبکه مخابراتی، انتظار دارند حقوق قانونی‌شان به‌موقع پرداخت شود و امنیت شغلی آنان مورد احترام قرار گیرد.
🔸
لطفاً قیمت فیش‌های حج را پیگیری کنید. حدود یک ماه است که پیگیر هستم. حتی با یکی از فروشندگان به نظر می‌رسید به توافق رسیده بودیم اما قیمت‌ها هر روز به شکل عجیبی افزایش می‌یابد و آن شخص هم از فروش با قیمت توافق‌شده منصرف شد. قیمت‌ها از حدود دو ماه پیش حدود ۱۷۵ میلیون تومان بوده که حالا به ۳۰۰ میلیون تومان رسیده است.
🔹
بهمن‌ماه سال گذشته برای پیش‌خرید کامیون ثبت‌نام کردیم. قیمت ثبت‌نام ۴.۸ میلیارد تومان بود اما در زمان تحویل، قیمت را به ۸.۱ میلیون تومان افزایش دادند. وقتی برای اعتراض به افزایش قیمت مراجعه کردیم با ما برخورد نامناسبی شدیم.
🔸
اینجانب ۱۴ سال است متقاضی مسکن مهر شهر پردیس، فاز ۸ پروژه شمس راه ماهان، بلوک ۳۷۰.۱.۱ هستم. پروژه توسط شرکت مادرتخصصی عمران پردیس اجرا می‌شود. پس از ۱۴ سال، تمام وجه را کامل پرداخت کرده‌ام، سند ۵ برگی و سند خرید عرصه را هم در دست دارم، اما هنوز هیچ خانه‌ای تحویل نگرفته‌ام و هیچ مقام مسئولی پاسخگو نیست.
🔹
بنده ساکن منطقه ۱۰ شهرداری تهران، خیابان گلستانی، کوچه صباغ‌زاده هستم. مدت چندین ماه است از تلفن ثابت محرومم. بارها با شرکت مخابرات منطقه تماس گرفته‌ام اما متأسفانه هیچ اقدامی انجام نشده است. با این حال، ماهانه هزینه آبونمان از حسابم کسر می‌شود. لطفاً در این مورد اقدام لازم را انجام دهید.
🔸
لطفا عدم واریز وجه کالابرگ برای کسبه را پیگیری کنید. خیلی از فروشگاه‌ها کالابرگ را غیرفعال کردند، ما هم به زور ادامه می‌دهیم.
🔹
هیچ کدام از سهمیه‌های سوخت اسنپ و تپسی اصلا نه پرداخت شده نه محاسبه نشده است.
🔸
علی‌رغم درست شدن بیشتر موارد سامانه بانک ملی (بام)، ولی سامانه درخواست تسهیلات غیرفعال است. این درحالی است که مردم سرمایه خود را چندین ماه است در این حساب‌ها گذاشتند تا معدل حساب خورده و وام دریافت کنند. لطفاً صدای ما را به گوش مسئولین بانک ملی و بانک مرکزی برسانید.
🔹
خواهشمندیم درباره موضوع خاموشی‌های طولانی‌مدت برق در گلستان صالحیه، بخش بهارستان شهرستان رباط کریم خبررسانی کنید. مشکل بزرگ این است که آب شهرستان بدون پمپ برق تأمین نمی‌شود. هر روز در این گرما زجر می‌کشیم.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/farsna/451729" target="_blank">📅 22:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451728">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4iJHQnpNYpUQUq7Myvco7QIeuFlWUXCJHge6HKhkfsGdF11diTmFV7isf8JdeQU_hblm_QKedT8a_hy3Mvc2TQDu0urTzGEF54QTJid34XNYbxVAe3avACE2C33Je7VIKFD9Zuq_99Nwz0HerAztlzjvf9_JYY4Oo0bUNNjxcdOqF27BKIrIqsZgqWVzMsxXuEjeVyzXQWdziRqbCpM9uJcN8C33CezfMkSm-vwyCGvhRYiUmdphx4tZ7B7gZyu-luy5DYD69IzzvWFZ4xgH3IHeZQpqjsWcdol2GSwrBAznTX3IbKDTBVCWfbENT72sf6MxObE1qrdbM7Te8mrCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ: جولانی مایل است با حزب‌الله مقابله کند
🔹
او مدت‌هاست دارد با حزب‌الله می‌جنگد. فکر می‌کنم کار بسیار مؤثری باشد، بنابراین موضوعی است که من دارم به آن فکر می‌کنم. @Farsna</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/farsna/451728" target="_blank">📅 22:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451727">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSoO2F8nDwDG5yKFiJHxWuhmTbIY9YyCe6wjr_stIqOMol9cjz4bpXcwyHLyD0t88vFmxO3LgDv4F1crP5UZQZGHy4PX6IzH8XeXNSWOi7CmjOHdhYPHvnsw61dsLFwx0Hs47LGhSshjaSmEt-4NZLVI3lB8LxFTznAp3QGCnPCet2nbyA3R3XX7HM52JYa_6qQO9tRHb6Jd3v3Xiae4h7kNSbydCX7MxEHpY7CCikQqBXH24SYvPRXfJNcOYlx6zBWERzywskdejStmAkkUcVmN0ag48tvdAhl1RZHKRiD6nU3S_DAIlsR1M_Oc9BNRYXI_tYpQQSv8ROYaxNx4aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ این بود پاسخ مهمان‌نوازی ایران از کویتی‌ها؟
🔹
سال ۱۹۹۰ و پس از حمله صدام حسین به کویت، شماری از مردم این کشور به ایران پناه آوردند. ایران که تازه از جنگ تحمیلی خارج شده بود، با وجود همه سختی‌ها، از آوارگان کویتی در شهرهای مختلف میزبانی کرد.
🔹
ایران همان…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/451727" target="_blank">📅 22:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451726">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgWlU7KVBx1WB4Zpvg86HoqIzGrLp2-_XxwuJgvRmdUl7Yseiyp__iqpY9-ddE9PCYs9ZIsXhNfdW91BjqrNk-WBgg-OqTG5CQTSkhEzps-ow-YDyBOPXjHZJR7sbwRcFJFeJrfhHGFDjd6Ic3zQFs9NovlhsqtXDIkBkCPDrQwGaPngSq0NfPOEkUUopNsWDcCqSJUWezy7h5uQnNmvf1wQm9ulYygS2kPIS78r5GVbp2VR8ND_fL8EZzhkVlxFW2LadY_Xe3uFyQcTTb7PulMW-4rx5CDaY6DYGU3X4AKVDjXXXwIj-R3bbX6pM0iLfuNcgJgdTeS0hLlmGQOXZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صید ۹ مدال توسط شناگران ایران از آب‌های تایلند
🔹
تیم ملی شنای ایران در دوازدهمین دوره مسابقات قهرمانی رده‌های سنی آسیا به میزبانی بانکوک تایلند موفق به کسب ۹ مدال شد.
🔹
۲ مدال طلای ایران توسط محمدمهدی غلامی در ماده ۱۰۰ متر پروانه و علیرضا عرب در ماده ۵۰ متر قورباغه به دست آمد.
🔹
تیم ۱۰۰×۴ متر آزاد با ترکیب کیارام کیانی، امیرعلی ثابتی، محمدمهدی غلامی و دانیال جهانگیری و تیم ۱۰۰×۴ متر مختلط تیمی با ترکیب پارسا شهشهانی، علیرضا عرب، محمدمهدی غلامی و دانیال جهانگیری، هر ۲ به مدال نقره دست یافتند.
🔹
۵ مدال برنز شنا نیز توسط دانیال جهانگیری در مواد ۲۰۰ متر آزاد و ۱۰۰ متر آزاد، پارسا شهشهانی در ۲۰۰ متر کرال پشت، امیرعلی ثابتی در ۵۰ متر آزاد و ماده ۱۰۰×۴ متر آزاد تیمی با ترکیب کیارام کیانی، محمدمهدی غلامی، امیرعلی ثابتی و دانیال جهانگیری کسب شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/farsna/451726" target="_blank">📅 22:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451725">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36ff5728bb.mp4?token=fcHvY3y9G_vv0Q_Bz1yoBqjokxphF2NCD9o7Fkxak7VBR03IqPiBMQTUmzRZcL-MhFVBbXTynnmyFHTGVk0zWjx6AjTumIkDOyX9i3w_YXeAUBQgj41K3PThepd85agxNUoB7a5cVEMKeqCDWXtJ7A2RZrSmV3GkdMEfFAJiEr-8Xo-Q47fuXfUf-rZRLeD5t9U34czzuh355ILwc1lMPl-QQiWkjTY0J0omYvChRhrOvspLPrrUZQuN3eE7fgI0X7WRkVxtNCbceEb4bUwYFdis9SrLU2rlfFk3-4bKjf9l4ng7fcZmnOeYXCxrPjbVLclg_unqOYjWfzraeJHb2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36ff5728bb.mp4?token=fcHvY3y9G_vv0Q_Bz1yoBqjokxphF2NCD9o7Fkxak7VBR03IqPiBMQTUmzRZcL-MhFVBbXTynnmyFHTGVk0zWjx6AjTumIkDOyX9i3w_YXeAUBQgj41K3PThepd85agxNUoB7a5cVEMKeqCDWXtJ7A2RZrSmV3GkdMEfFAJiEr-8Xo-Q47fuXfUf-rZRLeD5t9U34czzuh355ILwc1lMPl-QQiWkjTY0J0omYvChRhrOvspLPrrUZQuN3eE7fgI0X7WRkVxtNCbceEb4bUwYFdis9SrLU2rlfFk3-4bKjf9l4ng7fcZmnOeYXCxrPjbVLclg_unqOYjWfzraeJHb2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشت‌پرده فراخوان جعلی «محاکمه رئیس‌جمهور و اعضای شعام»
🔹
در روزهای اخیر، فراخوانی با عنوان «فراخوان ملت مبعوث برای محاکمه رئیس‌جمهور و اعضای شعام» در فضای مجازی در حال انتشار است.
🔹
تحلیل دقیق روندها و شواهد متقن نشان می‌دهد که این جریان، یک سناریوی هدایت‌شده…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/451725" target="_blank">📅 22:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451724">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e86268f86.mp4?token=V-NmYIolbHUdlPWUG_NKyTpuhvLbDl2PMRJCWCOuYvGjf_wuvlsCQM9UNvLO_ff_-3eRt0HAI1SCVGjcBcRRmv-J4z7m9bDWqzLWKtEcconaG_vlooIc54S6l-LFPWhU8ZPrQWaI73GkfDMw61DqbGyu-5h8rSTodmm4_edGWtmAh7rtPO1m15cG8Hun-THqMeeh1T8xvT1VORwP90_en2a_j9siLYHTqk7lEcp7qjKTgMAcBMClFUzhYZIWazB00AHgo95P1FS2lk9tKF0eVCozI4Fx1yoihaFaBfzRUHUwQo7nUgWJ_eL0kOlcOQibMBzhLQuwJkEB4J_tZnJdXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e86268f86.mp4?token=V-NmYIolbHUdlPWUG_NKyTpuhvLbDl2PMRJCWCOuYvGjf_wuvlsCQM9UNvLO_ff_-3eRt0HAI1SCVGjcBcRRmv-J4z7m9bDWqzLWKtEcconaG_vlooIc54S6l-LFPWhU8ZPrQWaI73GkfDMw61DqbGyu-5h8rSTodmm4_edGWtmAh7rtPO1m15cG8Hun-THqMeeh1T8xvT1VORwP90_en2a_j9siLYHTqk7lEcp7qjKTgMAcBMClFUzhYZIWazB00AHgo95P1FS2lk9tKF0eVCozI4Fx1yoihaFaBfzRUHUwQo7nUgWJ_eL0kOlcOQibMBzhLQuwJkEB4J_tZnJdXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان‌های لبریز از جمعیت، پشتیبان قدرت نظامی ایران
🔹
صحنه‌هایی از حضور پرشور مردم در ایستگاه ۱۴۲ تجمعات  مردمی.
@Farsna</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/451724" target="_blank">📅 22:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451723">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">شبکه ۱۴ اسرائیل از اصابت به سفارت این رژیم در منامه خبر داد و مدعی شد که این خبر قطعی نیست و «این حادثه در دست بررسی است».
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/451723" target="_blank">📅 22:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451722">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‌
🔴
منابع عراقی: درپی حملات پهپادی و موشکی امشب، آمبولانس‌ها و خودروهای امدادی وارد کنسولگری آمریکا و فرودگاه اربیل شدند. @Farsna</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/451722" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451721">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4c8036bc3.mp4?token=DAvknYKpoz581IBadAvZeDDHDrYJM_fFHkmQpXtIg8vwKt8IvcrJtDrZXpeylPTZU6LsXbUy_PMWDztxd47BBMlWLSErY00_CfHp2VpuWc9jQhPCq_TOSynnlU6bhEhVppt6IBEzKXZ12ncWBLcgM134IJRPpBm9JCY6y6VOKy08B9eR2_NbN5-HX48cfmkqzud2Sp_Yh4bKLoA90P2fpCZI6Z8kGWmMeGxBLbVIKZJtWO25Ijn_8KFvkVVFzlzsyHR5h2ErT11w2CWkyxQOfEJFniRJYRV6QOgUwb0LgE8dwJyytTU63aBwXrox4ldx1hzT13MoQrzOa4lUZD2ALQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4c8036bc3.mp4?token=DAvknYKpoz581IBadAvZeDDHDrYJM_fFHkmQpXtIg8vwKt8IvcrJtDrZXpeylPTZU6LsXbUy_PMWDztxd47BBMlWLSErY00_CfHp2VpuWc9jQhPCq_TOSynnlU6bhEhVppt6IBEzKXZ12ncWBLcgM134IJRPpBm9JCY6y6VOKy08B9eR2_NbN5-HX48cfmkqzud2Sp_Yh4bKLoA90P2fpCZI6Z8kGWmMeGxBLbVIKZJtWO25Ijn_8KFvkVVFzlzsyHR5h2ErT11w2CWkyxQOfEJFniRJYRV6QOgUwb0LgE8dwJyytTU63aBwXrox4ldx1hzT13MoQrzOa4lUZD2ALQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفحص ۶۲ قطعهٔ دیگر از پیکر شهدای مدرسهٔ میناب؛ ماکان هنوز مفقود‌الاثر است
🔹
فرماندار میناب: درپی عملیات تفحص در مدرسهٔ میناب در چند هفتهٔ گذشته، ۶۲ قطعه از پیکر شهدای دانش‌آموز کشف شد که پس‌از آزمایش‌های ژنتیکی مشخص شد که این قطعات متعلق به ۳۲ دانش‌آموز است.…</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/451721" target="_blank">📅 21:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451720">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌
🔴
منابع عربی: صدای انفجارها از نیم ساعت پیش در اربیل قطع نشده و چند موج موشکی مقر تروریست‌های ضد ایران را مورد هدف قرار داده است. @Farsna</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/451720" target="_blank">📅 21:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451719">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-zyoUi6O_eh0d78riL4NTT7ck4J0V4_yvmtu-chbCyqw06m4r8NOdstfHNCQ2UUmfyEPnR75oTfXFN7T4IknQlm5iAuYwmoQzNHBgPxXK6p7T1z48Z9X5AExiHofHdfhJ_dcO8dSjCuuhbGw1atlhSg3eVoriyG1jwk9QLYq_YW5KOZm1Y6sTdtJBWYrA57HXJkkWajdYiAW1uAb2YPgvS9euy9z5PlJ3Q_iorFl8PfMl3pmp_9mdyFPhIoPts96sCcdApWfvIN3925jQvGrVwvyJCkHgs8-G_5bm5UJup5FwTPxFKc2DoMbbF2J0Ni5yFwlomcKkMSObLkOOnqcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بذرپاش: برنت را می‌شود با بلوف تکان داد اما هرمز را نه
🔹
واشنگتن در بازار کاغذی قمار می‌کند ولی تهران «ریسک عبور» را در بازار واقعی قیمت‌گذاری می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/451719" target="_blank">📅 21:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451718">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0add65574.mp4?token=bePzL6WD1Eo54GiULFBvMj5kc40APiRuXzbxbX9ojgNq9drDRjoHF8MSpoaVjzn5hV5prx-Ifl03dtuwt7aAacqISSVUjRJQhQbLU6jF9haRUspvdiGxPmWTpaD3mBXPaaqTyTOLipjzI5LMiYZILpMC_6nXRJec4k8C2XNm9IaKiyEYlYa4ZViOJbaSY3wzQ30HcSiJaRE7lZMT-kLdNn1t8IV-bjoFhySzwr0IyjyPXt_Me_lxQJ8-JRoN4T3DqU3b5YMvTxHUeC-qXVVDpoAFq9A7Cej8teFEf7AfUsiwZYhdRYAsFk65yS6OIebyD-cSN3kBK1oU4ZcvYFl_sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0add65574.mp4?token=bePzL6WD1Eo54GiULFBvMj5kc40APiRuXzbxbX9ojgNq9drDRjoHF8MSpoaVjzn5hV5prx-Ifl03dtuwt7aAacqISSVUjRJQhQbLU6jF9haRUspvdiGxPmWTpaD3mBXPaaqTyTOLipjzI5LMiYZILpMC_6nXRJec4k8C2XNm9IaKiyEYlYa4ZViOJbaSY3wzQ30HcSiJaRE7lZMT-kLdNn1t8IV-bjoFhySzwr0IyjyPXt_Me_lxQJ8-JRoN4T3DqU3b5YMvTxHUeC-qXVVDpoAFq9A7Cej8teFEf7AfUsiwZYhdRYAsFk65yS6OIebyD-cSN3kBK1oU4ZcvYFl_sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خوش‌چشم، کارشناس مسائل استراتژیک: نقد‌هایمان را «مشفقانه» بگوییم؛ باید از شخصیت «عراقچی» و «قالیباف» حفاظت کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/451718" target="_blank">📅 21:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451717">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/154a846214.mp4?token=I8KKsQyFqXWrSN_6bnwNffeI_w8EOuHaM9DmFb3KI4JTPO4OXvp-Jtz3ASBEYtrX_gxv_uAnfPTeRr4PzgUvgPB69lM9DpPKszL1KC6ImzuvIPtu23ROBNIt-JR0sI-qZuAjG2AiOacbbaRLHJuywB1_U77VttMACANXSpLFb7d7o3--I-V1ZNDSAufSoUlyeuCvH2xCdwj2gJCoeVgXPSHzyJC1Emjlmn6cHR76iLobwMvAtGZJg-bSmsvVDXk5lbwYtJIhL7L5-wjTolRzaas7t5pd7jZ6ZbfmkK2muuAvAY2GSFregQXpWfNq0skSfpCp2mg5R3qtBgCpPCJiIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/154a846214.mp4?token=I8KKsQyFqXWrSN_6bnwNffeI_w8EOuHaM9DmFb3KI4JTPO4OXvp-Jtz3ASBEYtrX_gxv_uAnfPTeRr4PzgUvgPB69lM9DpPKszL1KC6ImzuvIPtu23ROBNIt-JR0sI-qZuAjG2AiOacbbaRLHJuywB1_U77VttMACANXSpLFb7d7o3--I-V1ZNDSAufSoUlyeuCvH2xCdwj2gJCoeVgXPSHzyJC1Emjlmn6cHR76iLobwMvAtGZJg-bSmsvVDXk5lbwYtJIhL7L5-wjTolRzaas7t5pd7jZ6ZbfmkK2muuAvAY2GSFregQXpWfNq0skSfpCp2mg5R3qtBgCpPCJiIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسئول ستاد مرکزی اربعین: تا به امروز نزدیک یک میلیون و ۲۵۰ هزار نفر برای زیارت اربعین در سامانۀ سماح ثبت‌نام کرده‌اند
🔹
برخی مردم به‌دلیل حضور در اجتماعات خیابان برای حضور در اربعین تردید داشتند که با پیام رهبر انقلاب مشخص شد حضور در اربعین هم بخشی از میدان است.
@Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/451717" target="_blank">📅 21:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451716">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e655d9a666.mp4?token=eVa71qGQCD4nYUaXbw9IkQ-FJToLY024efGx-5-zw_jpX1xRN7EsTv68OMKDlB8CDR1hwBna8iOI5mChAFUeLUsK3ZD4kVzeGUhWVwZ7hwhvbxUM-SqsgWJvYnByeLaEHbCrR4TIbaSAyy2s60UOi4QdGtrhcfUK0WzxJnUn7DNz8EdlU40fTt4OwGJjCDsivyV-YcZNjre5eywVMG0Oz4KgXR8zCUZw3FNS5Q3VNIJwqJkRajOOw_2k7YVmFfOlHPBe-MibedfJ41KNKcLQ_j0vZXaaxw9L0rTGkJkhqy1cXJH-ER8387Y3_amZwep-tK_bzrz0ZOvZimjLwjUOdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e655d9a666.mp4?token=eVa71qGQCD4nYUaXbw9IkQ-FJToLY024efGx-5-zw_jpX1xRN7EsTv68OMKDlB8CDR1hwBna8iOI5mChAFUeLUsK3ZD4kVzeGUhWVwZ7hwhvbxUM-SqsgWJvYnByeLaEHbCrR4TIbaSAyy2s60UOi4QdGtrhcfUK0WzxJnUn7DNz8EdlU40fTt4OwGJjCDsivyV-YcZNjre5eywVMG0Oz4KgXR8zCUZw3FNS5Q3VNIJwqJkRajOOw_2k7YVmFfOlHPBe-MibedfJ41KNKcLQ_j0vZXaaxw9L0rTGkJkhqy1cXJH-ER8387Y3_amZwep-tK_bzrz0ZOvZimjLwjUOdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انتقام قطعی است
@Farsna</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/451716" target="_blank">📅 21:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451715">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🎥
لحظۀ اصابت موشک به مقر ترویست‌ها در اربیل  @Farsna</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/451715" target="_blank">📅 21:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451714">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc36988cef.mp4?token=ZqVXsEUi8qtAeoI0FivW3xyvNtoWE6lAVMsh4_RtbY4AD0k3yoKqJALX9C6U4NXxkYJms8CvLq-odyjIQPYZGWxN91FszwbgkEhUrmgwTvazj6bmt0gSZ51TnpKyzNq9gewnaCEZ_LCUmwZKGNe4IbxBKYGB-nLCQsdFfQmsLAFCb1G1c2bx_v0ITYvGnQSeOrKu76QH7MoRfTwOfXzSZWo3y3hg4mblK223RAjII1JV0VouoQs3K4eWkOUh508kRGIyM572Ud51vq2reL5uW1WaInq9uyFNwof2iIW44ws8E6gY00qRJj6WqLBFUFUctKrE25rqSHZh2kTbDC6GRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc36988cef.mp4?token=ZqVXsEUi8qtAeoI0FivW3xyvNtoWE6lAVMsh4_RtbY4AD0k3yoKqJALX9C6U4NXxkYJms8CvLq-odyjIQPYZGWxN91FszwbgkEhUrmgwTvazj6bmt0gSZ51TnpKyzNq9gewnaCEZ_LCUmwZKGNe4IbxBKYGB-nLCQsdFfQmsLAFCb1G1c2bx_v0ITYvGnQSeOrKu76QH7MoRfTwOfXzSZWo3y3hg4mblK223RAjII1JV0VouoQs3K4eWkOUh508kRGIyM572Ud51vq2reL5uW1WaInq9uyFNwof2iIW44ws8E6gY00qRJj6WqLBFUFUctKrE25rqSHZh2kTbDC6GRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
منابع خبری از شنیده‌شدن صدای انفجار در نزدیکی کنسولگری آمریکا در اربیل خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/451714" target="_blank">📅 21:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451713">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0fpa_rLA1ggZvBl0Y4xNdykVxaBnc4Lwed6hoSOg-1BJgVPFjVz0WKlV1_qMIgcV_YR9taAPlXK6NyMi6CU3tVpCY1pjl1qGXrs1YxRbDA1Go9sXH7an3KYYAjPRnCDIXQ2Zco4LXNa0ekKOpXo2XUlPCZtNaVr8FlDKK8KBZlc3KiJf59Mh6pM4F05xA6MmLSJlvIvJ56xKe93A_ye8sZiwXWmFYjz7IQ-VFESrMFiGdHHTR2UGa6g5qznpktK0jZ4i5YMX2DwddBtecCTUUYwBdy35Vx1rFHaxiSsiJ51719HPf5a3cjs9FEgXONPk_5Ykm8OZYArvPIdbD3teA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
۱.۵ میلیارد دلار سوخت‌رسان آمریکایی در تیررس ایران
🔹
حملات هوایی ایران به پایگاه‌های آمریکا در منطقه باعث کوچ زیرساخت نظامی این کشور به اسرائیل شد.
🔹
تصاویر ماهواره‌ای نشان می‌دهد، حداقل ۲۴ هواپیمای سوخت‌رسان آمریکایی در فرودگاه رامون ایلات اسرائیل پارک شده‌است.
🔸
ایران در طول جنگ ۱۲ روزه و ۴۰ روزه بارها منطقه ایلات را هدف حمله قرار داده است.
🔹
هر سوخت‌رسان آمریکایی ۶۵ میلیون دلار ارزش دارد و تنها یک باند فرودگاه رامون ۱.۵ میلیارد دلار تجهیزات در خود جای داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/451713" target="_blank">📅 21:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451712">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دلیل پلمب چند کافه‌ در تهران چیست؟
🔹
درپی انتشار تصاویر و خبر پلمب چند کافه در مرکز شهر تهران شایعاتی با موضوع برخورد مرتبط با امنیت اخلاقی در مورد این کافه‌ها منتشر شد.
🔹
کافه‌های مورد اشاره هم با عدم اظهارنظر در مورد علت پلمب خود به شایعات پیرامون این موضوع دامن زدند.
🔹
باتوجه به اخبار موثق دریافتی تمام کافه‌های مورد اشاره به‌دلیل مشکلات صنفی پلمب شده‌اند و پلمب آن‌ها هیچ ارتباطی با مسائل مربوط به امنیت اخلاقی ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/451712" target="_blank">📅 21:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451711">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3319cb340.mp4?token=mOrN7LEUUBKFAWwGtgv2nrZ013fbYcZV0zS7AUDf5MnDYcP7IGHRt99CiFeVNwsDDm5Hp5MGYKW4Z3ortiox5VZIQ7KIGy0RKCAyzdtknpk9rMi2Z9xSadOffCkPmJWxA2dFzrPB1uMkhQIEjcTYa6PHuAebRctsg1A2tc4SM1Vyj57k63TbEgCBasa8Cc-nw_pL8qxom0o3NmjWAvKfnBX-NFdTqJH2Oq6Be7o2XUeHG6eHHX9-uyEN2T4GEb7uRbwg0XvHrIDV82xM3aSqdfM9InCEiXDiL6vrj_LABq2fLslXLDoUYmUEMxcqLJJ-P_odeWiwn47tYKWmL8Cviw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3319cb340.mp4?token=mOrN7LEUUBKFAWwGtgv2nrZ013fbYcZV0zS7AUDf5MnDYcP7IGHRt99CiFeVNwsDDm5Hp5MGYKW4Z3ortiox5VZIQ7KIGy0RKCAyzdtknpk9rMi2Z9xSadOffCkPmJWxA2dFzrPB1uMkhQIEjcTYa6PHuAebRctsg1A2tc4SM1Vyj57k63TbEgCBasa8Cc-nw_pL8qxom0o3NmjWAvKfnBX-NFdTqJH2Oq6Be7o2XUeHG6eHHX9-uyEN2T4GEb7uRbwg0XvHrIDV82xM3aSqdfM9InCEiXDiL6vrj_LABq2fLslXLDoUYmUEMxcqLJJ-P_odeWiwn47tYKWmL8Cviw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بازرسی کل کشور: اگر براساس گزارش مردم، فسادی کشف شود، به افرادی که گزارش را ارائه داده‌اند پاداش پرداخت می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/451711" target="_blank">📅 21:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451710">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‌
🔴
منابع عربی: لحظاتی پس‌از به‌صدا درآمدن آژیرها، یک موشک‌ به نقطه‌ای در پایتخت بحرین اصابت کرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/451710" target="_blank">📅 21:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451709">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64f3a480fb.mp4?token=HE3Tkl3vADmZPEbRSTGpQR8rCGJ39GLMVef-_0dK2sALyhENvtArKe8_mXCddFPIlQ1TygWChWtBapC2KjLZHYQmOMh0CodwkTz2jshSDT_fen3VG3NOKutFlldbs-uOXWCGJXNlu-ouWZ2_8h8xh7txXT-3o2JCnUk49wQ6MrP3vsCbtR93MjpbU6Qg2dHrRPI4CU90EKhNx41uwbmv29Vdxvuj1wxeTQNv7WovUv_KopVA3jLkY_Wu57-0vC705f5RL6zfx5PqEywPB-hqxJtfT127BQ0NudAfBibfimIti3HQxQ4gdsFDVwcHNDRe5QK59Rhi6dqcXvzjJqwl9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64f3a480fb.mp4?token=HE3Tkl3vADmZPEbRSTGpQR8rCGJ39GLMVef-_0dK2sALyhENvtArKe8_mXCddFPIlQ1TygWChWtBapC2KjLZHYQmOMh0CodwkTz2jshSDT_fen3VG3NOKutFlldbs-uOXWCGJXNlu-ouWZ2_8h8xh7txXT-3o2JCnUk49wQ6MrP3vsCbtR93MjpbU6Qg2dHrRPI4CU90EKhNx41uwbmv29Vdxvuj1wxeTQNv7WovUv_KopVA3jLkY_Wu57-0vC705f5RL6zfx5PqEywPB-hqxJtfT127BQ0NudAfBibfimIti3HQxQ4gdsFDVwcHNDRe5QK59Rhi6dqcXvzjJqwl9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چشم دنیا باز است
@Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/451709" target="_blank">📅 21:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451708">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eeb7e452a.mp4?token=TlvoX0NBvOla2ci4ozXWDg2hfqwayMU_-QnUp4JVYH0aTEZSL-MIjr6gClO1IS6roVB9eYdaeZzbYVmrJQP66Bal-giiQv9zgfrUoUzfeEhkOqqB2rB56XcPTynOkqayYv0rZtp6WF2uebn8JrHj0fJpW6aeV_mwRHbus4rlwm6cWkTScRPTIJofImDOvAqeJbD0l4IuG4jz5r4Fv0_Vh_6UXKKHN29NTy7G9IWMhc7Grp_F_Z-ILwCWSgutHtWV-qQmePKQNJ6prURcQpJlTYTO96pb9PMR2q_dksfFy1wlGbMd8xysCLAr2K8db2LGvjfDxOSnmqCpqunhkFqP8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eeb7e452a.mp4?token=TlvoX0NBvOla2ci4ozXWDg2hfqwayMU_-QnUp4JVYH0aTEZSL-MIjr6gClO1IS6roVB9eYdaeZzbYVmrJQP66Bal-giiQv9zgfrUoUzfeEhkOqqB2rB56XcPTynOkqayYv0rZtp6WF2uebn8JrHj0fJpW6aeV_mwRHbus4rlwm6cWkTScRPTIJofImDOvAqeJbD0l4IuG4jz5r4Fv0_Vh_6UXKKHN29NTy7G9IWMhc7Grp_F_Z-ILwCWSgutHtWV-qQmePKQNJ6prURcQpJlTYTO96pb9PMR2q_dksfFy1wlGbMd8xysCLAr2K8db2LGvjfDxOSnmqCpqunhkFqP8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس کمیتهٔ حمایت از جمعیت: برای ۵۰ درصد خانواده‌هایی که فرزند سوم آن‌ها متولد شده، زمین تخصیص یافته و می‌توانند ساخت‌وساز را آغاز کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/451708" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451707">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cb3c27fad.mp4?token=f4XpojBIVhlE8ZWUlA0GNRcmiODGUm80WvGWplIX5Ce1M95zuNptrvvy44twZPxVVVRsFDzqiyaiOhKuE_VGxCwVvkw-cXvesAFsW5dECCkh1zpglQzoqcE1pBun3dI4qrt4oNIHr_2gsdE5Y9vR-zRxUL8s8weH23GNFrVD7V4dWpAzqaU0UBbzxesZ90t-VFwMSxfSzR9RxrO1qxgfJOTY0UdZ_nHyDPdJKL73bhRoQLxZwYD-KG8PU1bD_MuWpdELEBoW_jmYotaXLYsBFX5NuS5kaijaQNLLZmnv_3P9o6PRNDkfRxvkChlYfHBNa9O9XUfdo7Mi5eP4WlzJSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cb3c27fad.mp4?token=f4XpojBIVhlE8ZWUlA0GNRcmiODGUm80WvGWplIX5Ce1M95zuNptrvvy44twZPxVVVRsFDzqiyaiOhKuE_VGxCwVvkw-cXvesAFsW5dECCkh1zpglQzoqcE1pBun3dI4qrt4oNIHr_2gsdE5Y9vR-zRxUL8s8weH23GNFrVD7V4dWpAzqaU0UBbzxesZ90t-VFwMSxfSzR9RxrO1qxgfJOTY0UdZ_nHyDPdJKL73bhRoQLxZwYD-KG8PU1bD_MuWpdELEBoW_jmYotaXLYsBFX5NuS5kaijaQNLLZmnv_3P9o6PRNDkfRxvkChlYfHBNa9O9XUfdo7Mi5eP4WlzJSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع خبری عربی از شنیده‌شدن صدای چند انفجار در بحرین خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/451707" target="_blank">📅 21:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451706">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در اربیل عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/451706" target="_blank">📅 21:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451705">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uufVX5YTurHK0-_XiZpaYKHLd9zWjc_peUNEmN-ngDBKIn9W7arG6AxX_Ftkoq8UJaAkJs-JDm4cjuVrJGwmR0jJVC-J8thuTyWFaA6tN3K5ZZzOdMe5i0X7tYd4bh0vqDmkNroc91NMbEOYaBTnTqfpfqFt8c8VD6H4RQkvM_75tevATBteATHsBvAK9OuiRs5W3G84SP3wCNUpABUKwY6KNYuTIj4dmpsuR3F_rXNwDK4bCfBmYAsKDU8RRJxKWYaIG568TaQAKwbwV8hMnr93P0rM6AOxYjlnxzFm26BdXT7mtC-zv_f9k54aohG8OiTvadCNMS93VfWg_JMnYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش: اجازۀ نزدیک‌شدن دشمن به مرزهای کشور را نمی‌دهیم
🔹
از زمان جنگ ۱۲ روزه برای احتمال حملۀ زمینی دشمن همواره آمادگی داشته‌ایم.
🔹
اگر جنگ به روی زمین کشیده شود، نبرد چشم در چشم خواهد شد و به دلیل ناآشنایی دشمن با جغرافیای منطقه آسیب‌پذیری آن‌ها به شدت افزایش خواهد یافت.
🔹
اقدامات نیروهای مسلح به شکلی است که نیروهای مهاجم زمینی حتی توان نزدیک‌شدن به مرزهای کشور را پیدا نخواهند کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/451705" target="_blank">📅 21:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451704">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
منابع خبری عربی از شنیده‌شدن صدای چند انفجار در بحرین خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/451704" target="_blank">📅 21:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451703">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3033cae9c.mp4?token=GJjKng2LbqTwJkxxZbCno1Pf9idmV0hKjUQND9UookbFOnqKG_7W6J0-iioirnnweofMQlxPP0lljrJ7HnIw11Dy8LcMhDDcO1lPAhIjwTE_dCZZdgV6cgxsENChvq9bI-JUa4Zyfk7_CuHC9H216lI7BT5Lzpln84Upse1HGdQz73a9iu_RzbMbf-JHgURYJsSJBRckGRElnLD5LeFv4FN-I7APINVUFPORvzEklpZWVJCLVMRLJqDtbiK_GkDlU3UtIuY_N3DCN0lR5GNqoLdvoa47JtGUrmOUUw4y35eEczUHq7rR9pePfxi5hK2SeI8Yp7rmmeB7QFTx3shayw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3033cae9c.mp4?token=GJjKng2LbqTwJkxxZbCno1Pf9idmV0hKjUQND9UookbFOnqKG_7W6J0-iioirnnweofMQlxPP0lljrJ7HnIw11Dy8LcMhDDcO1lPAhIjwTE_dCZZdgV6cgxsENChvq9bI-JUa4Zyfk7_CuHC9H216lI7BT5Lzpln84Upse1HGdQz73a9iu_RzbMbf-JHgURYJsSJBRckGRElnLD5LeFv4FN-I7APINVUFPORvzEklpZWVJCLVMRLJqDtbiK_GkDlU3UtIuY_N3DCN0lR5GNqoLdvoa47JtGUrmOUUw4y35eEczUHq7rR9pePfxi5hK2SeI8Yp7rmmeB7QFTx3shayw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به عشق مردم جنوب؛ شما چند درجه دمای کولرتان را بالا می‌برید؟
@Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/451703" target="_blank">📅 21:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451702">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/451702" target="_blank">📅 20:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451701">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89fca517c3.mp4?token=p4GtVEQZ3MLTUZDAOq8RST0GcUxrGIeSMKHZn7I10maQ0NI9NkeDkGKG2zrH3wUeTdG5LuKgPpiUCQ_3IdKuWZPCq-0ofW46A1Gog-jJIWYraiPhZHXORzWjSUGYbSidLZVAPX-_zCU7cuFXfaLJtuFlimLxgRvpqDI9lolhciGOmot3gqHMS-BOwTM4rf_ujxLn6OZ6iKDaxTkDI7tOXWZMas14Xekd1l-nkvCCwIM_DIA-M-pwQVaWtfQ0ff70E4jwHmetV3c1NBY3RHcPnQvU_KHZGJaOR96WF2NkGyFWWMR34Gp9PEznLth-yGv25kxkl5h3O6TWifysJ7Z72g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89fca517c3.mp4?token=p4GtVEQZ3MLTUZDAOq8RST0GcUxrGIeSMKHZn7I10maQ0NI9NkeDkGKG2zrH3wUeTdG5LuKgPpiUCQ_3IdKuWZPCq-0ofW46A1Gog-jJIWYraiPhZHXORzWjSUGYbSidLZVAPX-_zCU7cuFXfaLJtuFlimLxgRvpqDI9lolhciGOmot3gqHMS-BOwTM4rf_ujxLn6OZ6iKDaxTkDI7tOXWZMas14Xekd1l-nkvCCwIM_DIA-M-pwQVaWtfQ0ff70E4jwHmetV3c1NBY3RHcPnQvU_KHZGJaOR96WF2NkGyFWWMR34Gp9PEznLth-yGv25kxkl5h3O6TWifysJ7Z72g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایرانی به هیچ‌کس باج نمی‌دهد
@Farsna</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/451701" target="_blank">📅 20:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451700">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/791ad163fa.mp4?token=KKROFz8Bq49gOd65kF8Tm-xVMTZdrpbQ1WMrRKQT-M6hREj0uAG_OQuVWg19SNKf68mvzJm1Y2k-Qmp4zNXMy7X7M_MqXjUrDTfLKhtDFAXf0UeOTjCkbslUsLRmsZN0Rdnrqy13NZquEH0BYKhOZyf6L8zCQ_7CaBxK5VJiNUUL-ZsJwpG9Dt3F92XvhGJgGPc69vD7O-ytoLQWi2yC0QG-Ii25VBq_pa3vUwV0qfKH_adhhY6xyOz7pdL2bAzoP4_vP6tlmF4M3c2JL1gqCjOVniiX6qOYrJOLvmvLTapwsiO5LURN7boGqAR6Lvdpd_HOHXwedWbOrY5csXoXug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/791ad163fa.mp4?token=KKROFz8Bq49gOd65kF8Tm-xVMTZdrpbQ1WMrRKQT-M6hREj0uAG_OQuVWg19SNKf68mvzJm1Y2k-Qmp4zNXMy7X7M_MqXjUrDTfLKhtDFAXf0UeOTjCkbslUsLRmsZN0Rdnrqy13NZquEH0BYKhOZyf6L8zCQ_7CaBxK5VJiNUUL-ZsJwpG9Dt3F92XvhGJgGPc69vD7O-ytoLQWi2yC0QG-Ii25VBq_pa3vUwV0qfKH_adhhY6xyOz7pdL2bAzoP4_vP6tlmF4M3c2JL1gqCjOVniiX6qOYrJOLvmvLTapwsiO5LURN7boGqAR6Lvdpd_HOHXwedWbOrY5csXoXug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افشای جزئیات جنایت آمریکا در میناب توسط اسکای‌نیوز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/451700" target="_blank">📅 20:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451695">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kwlgf8IR3UaVRY4wtjAgBLTx6oLp3XSuRNxz4qAhjG8kydsYwtxnWS1VLeLoqQ71LDnCdSST4hvE_fiKSmZgcFL6ZRelDtdqOtKeKiwrYlaODnXlBL3B5e68q4kWBmGgnzWx7QtMvQz9NQv_f9GBXPTa4Dhy1XsgW45arAe2I40ChweAnUsp1b-lH0ZhWo2WvJbONADe6e2-5q7LFynY_aKlF-4uEcRed2iH_48dUxM-ePcVi9io94EzqygdXt0VzDvqaeHo5k0HDHUxXy0H0YPJ-kqlwNgvMQf2GD6uJ4Obr0qRQ20c2TdpKDk08K-ImMjJD_MNuOKams2U-mgVJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kiA3wecLYuo400qb3ePeotlgWG3uHwayLnkQhj8Qt-7LcJXl3LJC3tXQGzA14k33KouvRP01pbrOBkND9Pi504Wupa7ynTCl4IppMel3aq_tCS_nb_-FWkbMLA7nGjS10N7oVO4RcN2UHVoeGBC-xHg3x8vzTwwku-gqPyzrNStyZL83Whb0s0nHfg3yBe7ZNuSK2ANX-TxJzeV10pJqx8Q6UJ4RL6LUQtEOYouKGMr89xWKVroLv6TYdZ7RmvbZWCPq4qvKjELGBCAeJS2onBUl8tqV2GSnAUIsCfecy1CM8dIZzWtzpkDrwe7vWQO2u3mXJUPZf37GZeehQjnnVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tkS4Hl9ArEB24VG3fL32HVtTD1f--LSV63W8-v0k8eqFQtKN7bVQOjJ3doDW6C6Be5JAR-pSjcExuRssOj3phzp7qOERrR1fziDacXMhUxEt21EjO2D_gcostwNJaOlgABRNrOKssOiNuzgkC89HrEJqGMsPXGjOmdaGyW6g-zevgv7gcziwAzGYjfp5YdK9eRYpaF178qOIFUnc9e2Y3LZ6P6mYUswaGBreq7rAWrb3JKQnzYXatF6LPm_5JmPM_fmvHKGmo_vm346GiEFalzp3pGGInSQTjXJ84tgjqo_eZiTbM3-0dZCSA83382jnB5XjiFm160lf3b9qMW5TdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q4euraWf0amNQtadapspaa8FutralY7qxJGUKaTzSlhF3lDv1q2np-dRCZZrxS4JjiPDUH9Wvx_KywDLX3xs_P8uHzNlJs0KuYU6Y4wFdLRuiOe7SsnGk_G-XvACqvAAf0elUwFMTW964REconNsxRDzMaRPfqM-oqF2xS4NQs2JMCxG7jTsTrFkQeJsXuzPM1Svf9zAY7Pw_Lzc1pftFhzLVJCozp-8u1OfVaECYPxW8IaiEvV5U9SrrDU7nl54cMsWI4AV6rhFRsiAstss3LJ1ZQiA2e6vgYH48qiauuJtxk6H-OzLb_JhYn9wtZjTGaiNNTN5jApNjSvjvee2og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o3I4bJ_KiBXSH1NJifT6nF42DprYPHbklOuVc2a9OpGQ4nNaVK_5W7vvcL6DQqqhmDDKSMU2LM7sS7c9SaeOInIptSQmHyDEPMCEkgqcELs_zXInd8bESPxer9g_6J_sS1uzg62gqkFfsaFexa4mUX1bq4YpXPt5GV9qhZVGdKbT45_lRIVYLt_TmsEyI07Xpx4jMKSyv8vIi9n796dInbxKbNpmXXiWPuno1UVw7wBHn2RoDdds4YrIwyPNV92LUr6rvt19P5nZKhOf3Qi1RG_KAlD20PcLsoDg4if1uAk93Eu3e1KjhI5B7n4DQSMXB4s1yJ42nlybZxrsUzL7zw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید خبرنگاران از سازمان فناوری اطلاعات ایران
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/451695" target="_blank">📅 20:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451694">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">زمین‌لرزه ۳.۳ ریشتری تازه‌آباد کرمانشاه را لرزاند
🔹
زمین‌لرزه‌ای به بزرگی ۳.۳ ریشتر شامگاه سه‌شنبه ۳۰ تیرماه، حوالی تازه‌آباد در استان کرمانشاه را لرزاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/451694" target="_blank">📅 20:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451693">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">همسویی وزیر خارجه جدید انگلیس با آمریکا علیه ایران
🔹
اد میلیباند که به تازگی از سوی نخست‌وزیر جدید انگلیس به عنوان وزیر خارجه معرفی شده گفته که لندن بایستی در بازگشایی تنگه هرمز سهم خودش را ایفا کند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/451693" target="_blank">📅 20:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451692">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d4308a98f.mp4?token=c05Nm-rwlwJyrkby82uvWO3z_NFlloq1KIhz0CI-TSdK2Atuxso-4Jm9pI7kMeC96-n-WobAvNK-pAaGfbu6C6gSGAVLLCVTN4G2kDbsbH1pP283xHBdqlMllUzCzkJVcx5lG-XnwECoBLx3Cke2S8jbS9gjOH4_6Xg0kBaigCQLN4mQI06XF97JpYISl6_aRF6ty4cKUIGKo1jfY8fJmQ1d4faMDBXx2aTy9vaJFMQ56290Wb09NF1UVnGtoaDew8HfDNjQqypjgjJae3pZKNHaijBvXcZRDSNqmakq9sULuLKYHUSl4C8boNGBDpA2k-_WxHx4aAZnDZHsM7HIUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d4308a98f.mp4?token=c05Nm-rwlwJyrkby82uvWO3z_NFlloq1KIhz0CI-TSdK2Atuxso-4Jm9pI7kMeC96-n-WobAvNK-pAaGfbu6C6gSGAVLLCVTN4G2kDbsbH1pP283xHBdqlMllUzCzkJVcx5lG-XnwECoBLx3Cke2S8jbS9gjOH4_6Xg0kBaigCQLN4mQI06XF97JpYISl6_aRF6ty4cKUIGKo1jfY8fJmQ1d4faMDBXx2aTy9vaJFMQ56290Wb09NF1UVnGtoaDew8HfDNjQqypjgjJae3pZKNHaijBvXcZRDSNqmakq9sULuLKYHUSl4C8boNGBDpA2k-_WxHx4aAZnDZHsM7HIUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رگبار موشک‌های سپاه و ارتش، پایگاه‌های دشمن را فلج کرد
@Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/451692" target="_blank">📅 20:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451691">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51426b3189.mp4?token=ebwNoS5uyKlu2ebugpiwc8-OFXe0vIFz-lehicIG94RlGObDCOK84FIoZMzIAYm6rHS7GewFgb9HZrNMRucOzkpx1L9XWphy1WPQzB5MEs5TthzYfV1MW5rjjeXIqXKgYLgZWF9t2VPYigV5gpDSmEEox6Hwx6Qwu1JyqNu49AMoYCG3Z40B1NbK0VckidAyVpr6mQU5EzmIdufSBrDDtKcCpChmb8O3u979rx3dALLxTiF8J4ZVxwzo9MsdCoutbDbotpylnvefaAPkuyw90NskitFTHKpcaBluKCf-2H7YuOsvLFAfuc16sea8lAYFUFmMkfV9q-evF9qP3TimVUuqOfsjuDbN89idFumRMIL19uUbfhNl3fAhshgOFrWTHW9YFFCV0OvANS7eEP-fd3kTaw_vc49fxb47UeBJRhHmWuBdtc23_ftIt4eKYQZJcGyh6EdIzq6ySjmn2kW_oPqX--_erW_1vBKkDF1gaTLxbGCLyzKUtXz1W6Xl4rLFVacFXR_RR3-FRXkuaT2qKnNkeEQNJRrhCaDiVBMr-DVj_xaKq-1gEql3ROTCRJwWQxXplMsHZvQtHJWWA5SZ6UK2UwhaTBTMgeByMxhwvTOcnFYfcxxiBZm0Q46GiqonwvE9xWrWMd8sxsCsVm29eU5046b3YEyeoxr8TSW60MY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51426b3189.mp4?token=ebwNoS5uyKlu2ebugpiwc8-OFXe0vIFz-lehicIG94RlGObDCOK84FIoZMzIAYm6rHS7GewFgb9HZrNMRucOzkpx1L9XWphy1WPQzB5MEs5TthzYfV1MW5rjjeXIqXKgYLgZWF9t2VPYigV5gpDSmEEox6Hwx6Qwu1JyqNu49AMoYCG3Z40B1NbK0VckidAyVpr6mQU5EzmIdufSBrDDtKcCpChmb8O3u979rx3dALLxTiF8J4ZVxwzo9MsdCoutbDbotpylnvefaAPkuyw90NskitFTHKpcaBluKCf-2H7YuOsvLFAfuc16sea8lAYFUFmMkfV9q-evF9qP3TimVUuqOfsjuDbN89idFumRMIL19uUbfhNl3fAhshgOFrWTHW9YFFCV0OvANS7eEP-fd3kTaw_vc49fxb47UeBJRhHmWuBdtc23_ftIt4eKYQZJcGyh6EdIzq6ySjmn2kW_oPqX--_erW_1vBKkDF1gaTLxbGCLyzKUtXz1W6Xl4rLFVacFXR_RR3-FRXkuaT2qKnNkeEQNJRrhCaDiVBMr-DVj_xaKq-1gEql3ROTCRJwWQxXplMsHZvQtHJWWA5SZ6UK2UwhaTBTMgeByMxhwvTOcnFYfcxxiBZm0Q46GiqonwvE9xWrWMd8sxsCsVm29eU5046b3YEyeoxr8TSW60MY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک سلام جایمان بده آقاجان
@Farspolitics</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/451691" target="_blank">📅 20:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451690">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEubNunfsvE0y6tZCCLzrBztdG6M6atHw1QkNtq6JZlRbSLsCq6cd8zYV3SqqeYKEO4EdaPXChodVdlZRHyJjcFZWCHmeA8RRCamDtsIl-DDq4e0AhtDEH2F8JSsFk2caXI4XUu4YuWTzxbRoPxxJIWj6jQB_eOrOoiEmYul6kXyf3aCxNrGUDiQKiZv6wm0KQc-HcTxfl3K9q4TteRu0vCQc-kFS9Z0ro09V6wFw6qwRptgs_C2oCny99N4XJyFBxqlWtnnuMmjhq2-MId6Ja7p1v60oK-oryBsbqAl_iKk-dktwlXPQ8nivGG6eSkfbtKA4gF6NeuDpdTukO3trQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام یک پهپاد انتحاری متجاوز در آذربایجان‌شرقی توسط ارتش
🔹
روابط عمومی ارتش: ساعت ۱۸:۳۰ امروز یک پهپاد انتحاری دشمن متجاوز با رهگیری و شلیک موفق سامانه‌های پدافند ارتش، در آسمان استان آذربایجان‌شرقی مورد اصابت قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/451690" target="_blank">📅 20:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451689">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اعمال محدودیت مقطعی در مسیر هراز
🔹
پلیس‌راه مازندران: به‌دلیل عملیات احداث روشنایی، تونل‌های ۲، ۴ و ۵ و تونل سپاسد در محور هراز از ۱ تا ۲۰ مرداد، در روزهای یک‌شنبه، دوشنبه و سه‌شنبه هر هفته از ساعت ۲۱ تا ساعت ۵ صبح روز بعد با محدودیت تردد مواجه خواهند بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/451689" target="_blank">📅 20:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451688">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRtgG9Xtte6zEKBynfvYO3sbEuwO2XrYYAFpX-R4lME5nJyifxWXwI4oaKDyG7qwhkYvZwlBNQ7f7EO2uFvyR6dv7OsAgajkFXggHEEAKFe4I1t42aIb5_UpR4xYJkj2usDXlEevLqtCtcnH7H2WAO5HE5wJPQiaeuDlAitbkBYm8LkL-NQWeoYvK2PmHSaIrAO5PnG85fZfyHK0LnwLzCQL_-wjfToMfz56Ce4qmu_Kq-evfMTm6V_nuO-DppQijUtLbpVm4nQVf-u4Lez2wLiSU3n__rI9PdB5DQuM7njOH_7OVDI4oggu_RhVHcIJW8YMxcZgzQtUffFQX1qdrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برق ۴۸۳ ادارۀ پرمصرف در مشهد قطع شد
🔹
شرکت توزیع نیروی برق مشهد: درپی عدم رعایت الگوی مصرف، برق ۴۸۳ اداره در سطح شهر مشهد را قطع کردیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/451688" target="_blank">📅 20:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451687">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdK8DvdUmbNTVlL4YQXb4UNzoLDZJy7FltkGaU_veqCoZdNrhlbdthZn00Xf7zLnC0QZkPvuk7mm_nDUiffWobXitmpxTaD2FTGcoW6WkDhA5MzR8LRtBE7vNYl-faRV0H6wGBa-v2MF1WB3rAGo0qErQOrygkwMTzFfiaBSQMjKwu7aQDQzENAt7ZYiqCTdRCanADDNSnxP0SXH22xxtuvrXVl7X7f1GswjOIQEaWUx_qWbVknMSpW8Jv6J1mTOn5wPoj1bk4VUNg0v98nglmNg9kOYwicWwVefIu4DeRXntzuD9eDHhEOPl829GgE92jvfbO6kCQRGRLWJ3o7A6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراض عراقچی به همتای فرانسوی
🔹
وزیر خارجه امروز در گفت‌وگوی تلفنی با همتای فرانسوی ضمن اعتراض به اقدامات نامتعارف و مغایر با موازین دیپلماتیک ۲ دیپلمات‌ فرانسوی در تهران، این رفتارها را غیرقابل قبول خواند و گفت: رعایت قوانین و مقررات کشور پذیرنده و پایبندی به اصول و هنجارهای شناخته‌ شده دیپلماتیک، لازمۀ تداوم فعالیت نمایندگی‌های خارجی است.
🔹
عراقچی خواستار جلوگیری از تکرار چنین اقداماتی و انجام تدابیر لازم از سوی دولت فرانسه شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/451687" target="_blank">📅 20:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451681">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mf_PFDHDRLiyFb57UozQHCvXcMf0Yy3zNKtsFaI47rCpf8L4llJsZ7uG16VAyBBaIojJHJ5Ob_TjIDOsHt-qKi0eh7EdqVc8YOcLSdHKL5NpOgMYSuZJRCX72g1EACSlR6WaqeGpCf_82nJDUYUEv52yzhw3qBpA8RcZ6gO7scSTFuQq-JgzG5dNvgcmgHCgU-jmkhEBddZkR0FGTBgsi5XM4zcjxSkNcstkCcuH6Q62vpSdABXzpazQsyLKDMnH59pOVWe6EH5isv8WG1AZsCwy6C-ewoLtzmaeCR4gZ2IuCVXAw4Hl0Jc9nec8jbc7ekRe4P8VpS1wWsdfFq1YfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gvdF_KH-Mz26IiKgfsXfgYWOFTWuPEaid20Fy0YInGiuYol9wub_BQ8Um97-5UR4dhT53i95Ve2nCrloBUjRvvugdgqtqfMh2yfwkPKLI5E0dkXobCWrEjjPLclIdxWOv9anAbRl3iLmZGNnbiXSaKX03m9ocvp2j_1g4F1ePoOLx_pnmZMGDJ4zZCOMhGV7ybD3S7GPnV54oP-0Yx1w5gl6f9QEL-CyOF1se-hBGxkDKJ1tSNBRQ786BreGkKyXc4c2u2qB3LX7nZFkxie_ZuYYoyTh_3fE1IykUttGoXYvq25Q3iQeTsxmoBEwFk7OfV8klo8RoX5QhTxpTjePEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FC0N-k0EkvqHMSfnYLHbsd_4KeFcj6djt-3kkMrGHsAs6piITN1Vvn0Yd7CWXNO2vPLfiNXCO0s_-NYNMPnwoegJdpo0xAFTAKGXEFOxzxhGt4ZLy0FEM4n3V2ccV_lwlKnu080MNwuH-5KHRZVZRvMbhkQ-fv57mP3w2VQhDYVxPzpDSkmtbYDAaVgRI1oKZ_0OrfwWzrfXKVr7FdD1g1oejTfPAWHUjtF5x5xiS1VEy-FtYSWvJNAfg-DitK6miuLsxybtl7UrpmDpryCiRA2UyqnHGzGD7_LFAVf5c2BDYbF02SpgaLl0ZltRq16F1-zqDEI5ll38GRowG4EGQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l6sdLpHrMdBrbt6EwpgVFalpHXFePiJdYX-w6Hg7D97iZ4AIKvpVHUZxw8qOZ8ww_NxNaxs-4hjHp26bBkVdWCyeFZWtwo2Vv3NxUXRh_xlekcQLcGZQ247tjTiCIkwl557gdFauRpyjykArxb8WRMUZM9Rp-ghlMAfZ1k-bfNvduLdGyRI0Pv_MsJtaKkpdp9Yg_xCNVUGjw8zZQnHEZCzb5yI6IEO8pvHUbBnBIXO98OzS2vcwn8cqKLaZ0RSURnFYQCFPFITUhs7Rd2C_wqvASAkRY3wHeTZFsKgAmx6-Dvp8yU8mwEwjuxdth_lnA-4YhI383yJgY2B7U2i3rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQhQVW-8g5uzBqwn4XAebJ0px_6GFzr6Ev1xieXE_oaDanco0VpVNgyBq4ZPGC6LSvzbCUrW1M89P7uZm1v89q8aBhPVPh4oT6J9AXycnnr0w1XQi7s4Qgz8TnS2LRKqr3a5YLojf_IY7wivdgvy7JCe3CAaWAXxcz4-aM3Bk_Pw3p_kfDpSHHC8DvnMTR0TagtZhCHJL6hqi-NirDF5JPCOVqCY524XLy8ae9DhvsROEFlK9l4qzdZArEAFt-sAqJd5LWionVkw1citSTPxfk1fNrBBSaiOB_UhpGZiESdtJoyRLHeSWi9rOTO9nAbF6kmwlUJTMVMK3RbR_SiCmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kC15FuczJ9IFvD7EHaddKT40Zc3O4jfkN3MgpMJBLUJpzV9X-Lw9KRwa64Gh1F-BCTSZGGPwGChYQtXUxj1P9nUqrQXqRK88UQ2shDFufOYikzW6ZpzRz5CVUK_516rIBCZqePhpmMZBIe8rEXio58f-D7zvgQQDrXr3y6ce9XSMEpv3RIwWRn14-7wkIDPld9GuEcSSUOHppn09wMGkWg61JuKhPGKmNWwg0SpOQNULxDaNbyZ3pc-Qwiv04n4kRbxVkubvR1zFRBBQ3AcCJwVU2s7dvigYPe3jRIlaUpYW8yd7C41h7tOuLG6rmGarbfD1up9yoAbvcxc5Utzs2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
محرم‌شهر در میدان آزادی تهران
عکس:
عرفان باقری
@Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/451681" target="_blank">📅 20:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451679">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31f09280e.mp4?token=LHHeGJAlmRDCYn9Gy7IyH5NseU7ywTxSbzOSDSNJHXe2G0CdWIfCU1zVfib2UaQau9LydkRjmppfUXE5GY1RpyX1uBWMANioOtHnQln40esJ07RNdKl_GiYtW2hCaCKiYLfDXKTydWtYhro5L2KBpVk3IPWWyJT4rXu5RcccsCHPjrZlTVc5Po5lVCuOpT35H1AfYLaivlD13LpFdXyQeDSI3k5ApwpeI9Vrq3r_RIXueH2yQy_pBbFuEDIYkEZWL9oHeAhv0E9tSXXdU93j44LAR1lrT_iQWs9q6DBBpq1buzhLmmaxVWIt6YEDosUFK5XaTGSTlPsRMVaG0PiXVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31f09280e.mp4?token=LHHeGJAlmRDCYn9Gy7IyH5NseU7ywTxSbzOSDSNJHXe2G0CdWIfCU1zVfib2UaQau9LydkRjmppfUXE5GY1RpyX1uBWMANioOtHnQln40esJ07RNdKl_GiYtW2hCaCKiYLfDXKTydWtYhro5L2KBpVk3IPWWyJT4rXu5RcccsCHPjrZlTVc5Po5lVCuOpT35H1AfYLaivlD13LpFdXyQeDSI3k5ApwpeI9Vrq3r_RIXueH2yQy_pBbFuEDIYkEZWL9oHeAhv0E9tSXXdU93j44LAR1lrT_iQWs9q6DBBpq1buzhLmmaxVWIt6YEDosUFK5XaTGSTlPsRMVaG0PiXVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز راهپیمایی اربعین عاشقان حضرت اباعبدالله الحسین(ع) در منطقهٔ عین‌دو اهواز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/451679" target="_blank">📅 20:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451678">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc84283f2.mp4?token=gBriNh56UgaraP-6OpUGNtDrx-AT_g0A1HfpJWjMpIKBdwgUGjVaM-9ETvs-43YC5vtF5sbwWaEtodGQrmcMR9BzQ85m9IEbSANpndVF33FzPm10ZAWnnsidahIlRPfuUKJAlRLfID5ZvZCaLRCNIDJ-ryDGk08mlfVll9UYbvvk5kGwOhFKjGafkDFKThXpirNgj5-pQahA5ClnqIdfqO397xN1nDOfQQk7tY7QFUWNYLkBSBFOGmjJifbKtMsFtrI4dPtFqGya6SDISdtVIzORiapwY19gWB-frBq7v6O9AxaUM0JRqqrzFH0ve89a7AopQAbL8iCJEJNABtadiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc84283f2.mp4?token=gBriNh56UgaraP-6OpUGNtDrx-AT_g0A1HfpJWjMpIKBdwgUGjVaM-9ETvs-43YC5vtF5sbwWaEtodGQrmcMR9BzQ85m9IEbSANpndVF33FzPm10ZAWnnsidahIlRPfuUKJAlRLfID5ZvZCaLRCNIDJ-ryDGk08mlfVll9UYbvvk5kGwOhFKjGafkDFKThXpirNgj5-pQahA5ClnqIdfqO397xN1nDOfQQk7tY7QFUWNYLkBSBFOGmjJifbKtMsFtrI4dPtFqGya6SDISdtVIzORiapwY19gWB-frBq7v6O9AxaUM0JRqqrzFH0ve89a7AopQAbL8iCJEJNABtadiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس بنیاد مسکن: ۴۰۷ شهر و روستا در جنگ صدمه دیدند
🔹
۲۳ همت خسارت در بخش ساختمان و ۱۱ همت خسارت هم در بخش کالا و خدمات داشته‌ایم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/451678" target="_blank">📅 20:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451677">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oc-kFj4OFC4zw7edjS4m-U6HdLNkTcktBY2Gkxdv6mdRhSt1Vosx7RXUEHSNIr1DJpQPCPI4z67JxrnNh0LQCI0NMrYzJgB3yAqZX8AYo5bOfEYaGqpUBPqR17CRD8D6u5TPy9NrJJ4JDowRRK6d3Ecd0pgRmBuWwbgia2NZQ96VauqnQX9RkLgGniqZvTnh__XRGjogo7cbTFwndfh8QEuijoGE8u7DtTJJHbEcnSnfAM6CXqusr8U4kg3E4tYUzBrRUZFBapGmfeFozfMWW8Zlg2RVmn7pRkqNdWTStmbMBiuNKaglqq27tP6bCxxKtlJAIJIsAFst-KjKUP_FYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به بلغارستان هشدار داد
🔹
سخنگوی وزارت خارجه در واکنش به گزارش‌ها دربارۀ بررسی درخواست آمریکا برای استقرار هواپیماهای نظامی این کشور در پایگاه هوایی «بزمر» بلغارستان گفت: «هرگونه همکاری در حملات علیه ایران، از منظر حقوق بین‌الملل به‌منزلۀ همدستی در تجاوز و جنایت جنگی خواهد بود.
🔹
در اختیار قرار دادن قلمرو یک کشور برای انجام اقدام نظامی علیه کشور ثالث، طبق قطعنامۀ ۳۳۱۴ مجمع عمومی سازمان ملل، از مصادیق عمل تجاوز محسوب می‌شود.
🔹
ایران در دفاع از منافع و امنیت ملی خود در برابر هر شرارت و تعرضی تردید نمی‌کند و قطعا هر طرفی که به هر نحوی در ارتکاب تجاوز نظامی علیه ایران مشارکت کند، باید مسئولیت تبعات آن را پذیرا باشد.»
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/451677" target="_blank">📅 19:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451676">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
منابع پزشکی در غزه: از بامداد امروز ۱۳ نفر در اثر حملات دشمن صهیونی به شهادت رسیده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/451676" target="_blank">📅 19:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451675">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbe7077341.mp4?token=KGxS_0aMBzud39ISBUY1dQi_-73nj1NpNPibfuDqpnlKwcTrm4C0eJw0YK0TSO_146REqZT1_j67b6bJLPdHcsgqsTQakkW1ns1cNYmATdgxauWnPrLAutXB-pInC5Fd5H6eYIa2EQFW4jMkQ3cf_FaK51yIuHcX0LbUEKJX-mKUILPbfcT6nE7I1xw2nr4aVkh8OQ-AMrzu8K1sxmrRs_nksf1Dtco72i2ofLdhJjR4Qbii7KLHPXJBHKpiKmgYLajPkByLgRzEyv-W_nYaIJpXBWZdpqAdrl_BaD7wvi0fi_0uh_xRDrjIu5cBvZVzkAFmL5jU5N_a6DJW5JzBCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbe7077341.mp4?token=KGxS_0aMBzud39ISBUY1dQi_-73nj1NpNPibfuDqpnlKwcTrm4C0eJw0YK0TSO_146REqZT1_j67b6bJLPdHcsgqsTQakkW1ns1cNYmATdgxauWnPrLAutXB-pInC5Fd5H6eYIa2EQFW4jMkQ3cf_FaK51yIuHcX0LbUEKJX-mKUILPbfcT6nE7I1xw2nr4aVkh8OQ-AMrzu8K1sxmrRs_nksf1Dtco72i2ofLdhJjR4Qbii7KLHPXJBHKpiKmgYLajPkByLgRzEyv-W_nYaIJpXBWZdpqAdrl_BaD7wvi0fi_0uh_xRDrjIu5cBvZVzkAFmL5jU5N_a6DJW5JzBCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ارتباط ما با رهبر عزیز روزبه‌روز درحال افزایش است تا بتوانیم با رهنمودهای ایشان مشکلاتمان را حل کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/451675" target="_blank">📅 19:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451674">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c33d92d4d.mp4?token=p5GufM9pGbnhoWME8FyppZZEwh7nIozpsU3Exxp4bV_39P86cQMnofySOismCvnfW2aPj3DlzsvXh9LwUIu-xPBbXSKjODHMGqPB_JrFba4UfKuLo9LNtZAHOcVvCi2HIhMGb-oFF1nh_mzCQnJrYhuIrqLRWijdj66LOVd8NZs8QAbBV2PMackbQzjB3S0Rr7oRsHe5L3z_1aju0lAFHrN1pW_B213ubxxxwheeQjRNYebBJm8lIJf1oBFIFk1bLxRCVYqnBxDt5_PXXzhV0ytqk6q8PayhBKGyu1qGJ3wBzK04QX2Cmb4FOQgVX-cuCiU-pb6Un55Rgt2rGQcLUHGHZlHgs4BO8fZVKV850R_nd1m1ejrnHtC_3HRkx1EVoubRcil3gV7XqmSVG_aGF27RPUFytk1bA9futL5B-jHPKrTb_9GClqeoSZSzBq1d8Gy7Tz8j9LBJCg5AKigBraCY8GkPKHmyCFGaJnmjkmLSkM3OsnK5qzszljxmZ31p1KMIn27Obh3RsAyU1-5N2uOrDUQqIL9KaUN1vHLlK_16xTELVvk0xYSMIs-8VCvQkKVknZ07BfRz9lLR3qAV3k8MLUbBRJXjMGmJhpW65CUS0PkIolwaeHQ-q9Jl3ACua3LpG-cAEpUv5jtTw5df3oLkYKb_yQ5auDQAqQK7b2I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c33d92d4d.mp4?token=p5GufM9pGbnhoWME8FyppZZEwh7nIozpsU3Exxp4bV_39P86cQMnofySOismCvnfW2aPj3DlzsvXh9LwUIu-xPBbXSKjODHMGqPB_JrFba4UfKuLo9LNtZAHOcVvCi2HIhMGb-oFF1nh_mzCQnJrYhuIrqLRWijdj66LOVd8NZs8QAbBV2PMackbQzjB3S0Rr7oRsHe5L3z_1aju0lAFHrN1pW_B213ubxxxwheeQjRNYebBJm8lIJf1oBFIFk1bLxRCVYqnBxDt5_PXXzhV0ytqk6q8PayhBKGyu1qGJ3wBzK04QX2Cmb4FOQgVX-cuCiU-pb6Un55Rgt2rGQcLUHGHZlHgs4BO8fZVKV850R_nd1m1ejrnHtC_3HRkx1EVoubRcil3gV7XqmSVG_aGF27RPUFytk1bA9futL5B-jHPKrTb_9GClqeoSZSzBq1d8Gy7Tz8j9LBJCg5AKigBraCY8GkPKHmyCFGaJnmjkmLSkM3OsnK5qzszljxmZ31p1KMIn27Obh3RsAyU1-5N2uOrDUQqIL9KaUN1vHLlK_16xTELVvk0xYSMIs-8VCvQkKVknZ07BfRz9lLR3qAV3k8MLUbBRJXjMGmJhpW65CUS0PkIolwaeHQ-q9Jl3ACua3LpG-cAEpUv5jtTw5df3oLkYKb_yQ5auDQAqQK7b2I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اربعین امسال با یاد رهبر شهید پرشورتر خواهد بود
@Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/451674" target="_blank">📅 19:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451673">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1THMtTAgYXq-mN36Mzu_qsyqtikGWzt14vi_UExtxq0ZpyAf6thGQ4aUYjZ_ivrljoL1TsPUzHWQ7m2HXT11l5KB8mY18afMmaspFgE8Ytgt9iW4BS4AwJEb3lksbvz6j0r-5iqMV8Vdd2tW2W7yFeDUDg1aUZwBunr8F9yQUuRqLxA07wnmsqm54d49NduOAp2TkNZw4P8SHfhQf2Whh_XzmGEeKZGFFwBM8vQqwEMx-B7rgPp8Kexfx6l1xmoB77AMX7tyQE_oDC1imMihncISmsCNsWo3L-Uj5jpCbK1VXgUyS6uAoQE-CENU0LUjKVbz97MYrwB7dNr3mCAsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چگونه یک کارخانه می‌تواند روح هویت یک ملت را در کوره هایش بازتعریف کند؟
🟥
کیمیای آگاهی در کوره های فولاد مبارکه
🔘
در چند فرسنگی اصفهان، جایی که افق با غبار درخشان صنعت گره می‌خورد، سازه‌ای عظیم نه تنها به تولید فولاد، که به بازتولید معنا مشغول است. در نگاه نخست، مجتمع فولاد مبارکه شاید تنها مجموعه‌ای از سوله‌های غول‌آسا و خطوطِ بی ‌پایانِ تولید به نظر برسد؛ اما در پس این کالبد خشن، پرسشی بنیادین در جریان است؛ آیا مرز میان ماده و معنا در کوره‌های ذوب از میان رفته است؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/451673" target="_blank">📅 19:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451672">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRnAnJdo37io9BVf8Kvq59qLF54fnxqPO6MUUpxcM0hAFcILciPga4_Ud5ZKym5hi--_8pJiuxySXGu9D7ibQhEHhRyLX9MEyUyYKp9RJOoXzgIKwaJiIO2Kk-emv1zkFd5kQLKqfiIrglqrYy-GlBJxHuSsvW_E6-bVHFocNk_x_j7t0XPXsWnpJGOXZX4c6qiq9ZhlIYGi25oiG5A2XJmML18GBdA7w9R-SQAo4_4ab4uePs24iZV0cnCjvOMhieLpmWIlS5NEVylJtydgBSX2fOlhwXAVPzx3oGLTzMUtTp4wWmb8kJJ2Dyoc7xSZMfrdzP5UxsnD-Ypr0z5DLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
ضرورت ترویج فرهنگ ایثار و شهادت
🔹️
دکتر اسماعیل للـه‎گانی، مدیرعامل بانک رفاه کارگران در راستای تکریم مقام شامخ شهدا، با حضور در منزل یکی از شهدای والامقام جنگ رمضان، از خانواده این شهید گران‌قدر تجلیل به‌عمل آورد.
🔹️
دکتر للـه‎گانی طی سخنانی در این دیدار اظهار داشت: همواره خود را مدیون ایثارگری شهدا می‌دانیم و تلاش ما در بانک رفاه این است که در مسیر خدمت به خلق، با تکیه بر آرمان‌های بلند نظام مقدس جمهوری اسلامی و فرهنگ ایثار، گام‌های موثری برداریم.
🔹️
مدیرعامل بانک رفاه کارگران تصریح کرد: دیدار با خانواده شهدا برای ما توفیقی الهی است تا با بازخوانی رشادت‌های این عزیزان، در مسیر خدمت‌رسانی به مردم و میهن اسلامی با روحیه‌ای مضاعف گام برداریم.
🔹️
در پایان این دیدار، دکتر للـه‎گانی با اهدای لوح تقدیر، از صبر و استقامت خانواده این شهید گران‌قدر تجلیل به عمل آورد.
🔹️
مدیرعامل بانک رفاه کارگران و هیئت همراه در ادامه با حضور بر مزار این شهید والامقام در گلزار شهدای شهرستان پردیس، با قرائت فاتحه و نثار شاخه گل بار دیگر با آرمان‌های شهدا تجدید بیعت کردند.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/451672" target="_blank">📅 19:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451671">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/451671" target="_blank">📅 19:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451670">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc1730f80.mp4?token=iUMRb6FQ3kQiJ1kkxFvivVi9TyRt8WGxa8r-_XFOOG9o4lyHytUvOqKHJ_SqOvGeWtnmQZrnZ9-qoUWRllvYij3n2Y5WAD-WEVyCRHbB_4_x3YntTOjWvfos7syLkgGA6Ga7Ur9I9FlrKOlV5t1Dc4k1QYM280d8JAFdYsK1DFkVmd1vBuWwjOqZkZyCR-7E-EcfzUA_8A565jMyup5eOhMjAH5rHkaHxerJTEGKm47SZi10vY-xg9S21VPsldQY5-FBu3ikscXG0Lpem_mEvYi7F3qsVKnY0Cv3rEfG4A1F5BrpQ1yrd3aZuQ2B3DrgIrRdWtrBc0NcmLSkcYBKKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc1730f80.mp4?token=iUMRb6FQ3kQiJ1kkxFvivVi9TyRt8WGxa8r-_XFOOG9o4lyHytUvOqKHJ_SqOvGeWtnmQZrnZ9-qoUWRllvYij3n2Y5WAD-WEVyCRHbB_4_x3YntTOjWvfos7syLkgGA6Ga7Ur9I9FlrKOlV5t1Dc4k1QYM280d8JAFdYsK1DFkVmd1vBuWwjOqZkZyCR-7E-EcfzUA_8A565jMyup5eOhMjAH5rHkaHxerJTEGKm47SZi10vY-xg9S21VPsldQY5-FBu3ikscXG0Lpem_mEvYi7F3qsVKnY0Cv3rEfG4A1F5BrpQ1yrd3aZuQ2B3DrgIrRdWtrBc0NcmLSkcYBKKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر جهاد: هیج مشکلی در حوزهٔ تامین امنیت غذایی و کالاهای اساسی نداریم
@Farsna</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/451670" target="_blank">📅 19:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451669">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfdd5935a9.mp4?token=QPk9GT8gUi2vPpPU7qibbmdPKTLXg4yfjpast8-J2d63FzcBMNh35BTNw8DVZvOPKXfbMQ7OglhKeoAJUG428Hglfq2dPsjOrWoru6NeE4shLDXA1yzHXM2nXFQHy9EvoOCGYyPK2kwciSv80d24Ti9uPPSUlKHOw_x3A0iJxGgIpn_-leMFC61CH5T5M6EytyQ2kmSAuG15Koz4phigztEhps41HQOvTYgzhasW8FlZh8-t4ICFRaKGnbkL_ypjJ4rzXDoclT8WCZJxD-06xGIlQRKyQOntp9L6xJc8_EAy3mt3YmOgFhH_hYWarqwxxRJT3oW9UWj8vrfE1nYJuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfdd5935a9.mp4?token=QPk9GT8gUi2vPpPU7qibbmdPKTLXg4yfjpast8-J2d63FzcBMNh35BTNw8DVZvOPKXfbMQ7OglhKeoAJUG428Hglfq2dPsjOrWoru6NeE4shLDXA1yzHXM2nXFQHy9EvoOCGYyPK2kwciSv80d24Ti9uPPSUlKHOw_x3A0iJxGgIpn_-leMFC61CH5T5M6EytyQ2kmSAuG15Koz4phigztEhps41HQOvTYgzhasW8FlZh8-t4ICFRaKGnbkL_ypjJ4rzXDoclT8WCZJxD-06xGIlQRKyQOntp9L6xJc8_EAy3mt3YmOgFhH_hYWarqwxxRJT3oW9UWj8vrfE1nYJuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از خسارت به پایگاه آمریکایی Tower ۲۲
🔸
پایگاه نظامی Tower ۲۲ متعلق به ارتش آمریکا در شمال‌شرق اردن، در نزدیکی مرز سوریه که اخیرا زیر ضرب موشک‌های ایران قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/451669" target="_blank">📅 19:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451664">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/epYrcpdv4Wb6_u5Earlno1AGglMySQLFw0c_vr5mmab95rlRVag4VUJLIjSBoflNV3oBmVEoaYLbctTf2bn48uRplBkrSEt2VJajsP5qDMIelBY2BuTPg5Rjw4WOevV04iIJyhuZOrCRZlBqbDBDojK3rTNTpOuJciku2sL2qL4PYegc0IXpDmIeq6bQ99-UWPAHITmevG5E-aBarId2H_b9LQJ1ZDHkpXq_OjnK1uGN0EoahoAZCVzh70UuYEFu15P-5VXGx9hwJ1vu7v2ldTeRzFK6WPspFTAA4heMdHQBqywNUwnHFiKO0_kAIBUlEZJ3H3mPHrq_viSkqsk8Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eabAdHgIert0njTucxQGJ1xUpv2WtovO4TuABtWmJ0R_GqV5JlptU_f4bm3UEaJtzZ01jqggNrHK2H-IereBAp1mZOXWvsh5aKAHpe4lysKta_7UbuRZTniRpJNZ3p0z4w8xSt48PBDAAELmOdElwcT55eoMBNrqGk2JhlWyS_SYgoF-UB9BDlvuX5kJ5W4CidCYvpnIibeyBD4UeqcqxqGn8gsKUxTX8AbAkTWgM3FHRYPIzkH_ckzHhVz-RjrVSjK5Sf8Sdl3UB1pmFIeZqsK3UkTNE0TzWzS8rYYMlT13qXVDGcgl_8LNTE0w7LxC0I4robbu-i4An6OoCLAXrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNVLXTdQMxIUF1eXP9MZSSBNyEl0qy_VB3hCEa02adwCcFFeH3b4Bdr8AqE_WMKXYY-2Ph90PVqabhspxGDpNS26cY1ytaL__PEhNA_qc06cPIX3GmdWFoEmryi5mG1JYYyG_34ZoCq0aIknS3BF7GLJ3J42hcorK-hrZI_Dm1DEoj3PX4UvpCOZTWgvVpfZkfekVZLqi1RIqqEcz8po4SnPCLxCIbJIvjCjuHdlTNIYjjxq-YxfQp_iLVFZUGURBLkYJQxb1EIcBuexkpMR_UOxbMbvDyByXKMCifGke_g_WSYVlXMWScn6WSaLDQvh-7W4m1VO_ILm9bBkptNN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rv5V-um5xN0FJqHi2VBoqi1QJrUVTrGs2Jkr1wU1yk5pegljv9K10KBI4tneWj5CawPh9rEMcRwZtV9y4sASrdoFvfKsY0fhhRGWC4104w0rQ-D6d8lTNBqChkD9hvv-wnRw5SC4EIblP91kUSizN0Xc389EMiHIUXfF-22RT6twn01W-jIcnH943h8v1e2mxwwxt_Pv7KYzfyQM_pzqZCsYRQNu1X1vClOBDezdyz_RJkRFsWHZwAfFcleaWdEKMLQJWGLKT1vhM3wg3XX0HWTmiRmDLROVH7BrQCVweW2tflh-3zddwmi0vdWegzpmF6iBtCZhkx7pxFa1zswgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xg4gonE-YDEd-iebWs1oCu6pOXE606BB2kqkp6rNw7Oc89Z6srPPjNdndRD2LwPMKP9W0s9Xsa_pAU_qLyhLhlDmiPsPRAMO-vwwY7SZ5opvIynYi1n_hGS6tJ_wnZblPOZuEK452MWV4783CemFQXAA8pw836l54z9wlzv5sw6azTdT6VTpLx46KrOSn7DghuelVDepvRDgFnK6U1c6ByaGwuaLoTmLpSmi4owXqrHHe_2gR1xaqOI-npKtQGVGVDMkZ4qqSRIvl1KUJhH_6KcOGul2_dBdVG3hjqVN3IbWMPx-zmMj4k-rcY3Tm25FQ5BmpgwRsgYiAY6CUNC14A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گرامیداشت روز ملی صنعت و معدن
عکس:
هادی هیربدوش
@Farsna</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/451664" target="_blank">📅 19:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451663">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f2d573af0.mp4?token=SGQB1sGLzVZYpSda19IZFkcptggoiakUQarCvKrulLbpTDpKQM0s-UZddcaq7013MYCqBafcGhWbvNMeZCGf6oMF1RaKm46ar_0expDqPocRv436QPOhaUMbeUE6dzWfp86Nm45eXIBjz9eGzf_Vfn3F9iEgry0MvtkbCftN8iWDLM8AiWHscEjL6voC9SSQprkhOb-efXFXSPpaXiStQ_T-wbt4i4OBGQeCyZAz62Ka1uWgdY6QrsQiIzmm9QVhvAja0Ybfm9agDiO67srjm_lu4phuaDPe3AVdcJIf-aHjqVlCUbdVsbXra98z2wJWD_6lj9YEMZJ6Quypb_G59Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f2d573af0.mp4?token=SGQB1sGLzVZYpSda19IZFkcptggoiakUQarCvKrulLbpTDpKQM0s-UZddcaq7013MYCqBafcGhWbvNMeZCGf6oMF1RaKm46ar_0expDqPocRv436QPOhaUMbeUE6dzWfp86Nm45eXIBjz9eGzf_Vfn3F9iEgry0MvtkbCftN8iWDLM8AiWHscEjL6voC9SSQprkhOb-efXFXSPpaXiStQ_T-wbt4i4OBGQeCyZAz62Ka1uWgdY6QrsQiIzmm9QVhvAja0Ybfm9agDiO67srjm_lu4phuaDPe3AVdcJIf-aHjqVlCUbdVsbXra98z2wJWD_6lj9YEMZJ6Quypb_G59Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ تهدیدهایش را دوباره تکرار کرد
🔹
رئیس‌جمهور آمریکا: ما ۱۰۰ درصد به سایت هسته‌ای جدید ایران حمله خواهیم کرد.
🔹
آن‌ها دارند تلاش می‌کنند یک سایت دیگر را بازسازی کنند. ما به همان سایت ضربه خواهیم زد.
🔹
هر سایتی که حتی فکر برنامه‌های هسته‌ای در آن به سرشان…</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/451663" target="_blank">📅 19:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451662">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/913265ae74.mp4?token=eq2pL_aMDfnJUCaD5JJnZcY97nz7uq8Lf809OgQp2SqhwhRQVS4iLR11zzDpLf_0vUVD1sqQw3ENObez5KErCf6RAin3IrFza1fpzjBEtxLON1EOoNItej9pN12JWukmc_6Fq4GIHFbHV1m34S1WqRcli2LlMw7QvowAFmsqiA78N5AAU6NF8ihR4V6QSL-eDeqzcubUKjkhRZedIw6YAiZfi6Qk-OqcYQEnkbpehP0LJx54UVyQu87ciXK3_Fu4mcfzTX9CWzqspNZHAfOtQOcIg9Iy16uPaLKYIK9bneUDbjskKE59ObFh01rF5E_CQsRXS00J1L4NIJyC55cRtkpSSkHGJadjMU5Cih7n9TcZ_00oaxhJbyXMygfyjEH59c8222n5ZLw46vR-V2ZR0KlDTKaXxkms8sp8368KwEYqX4XcyUNOfcBnjb0G-LurzHPhgoIoUIrjcO0WnIHWLsFysP5f8zBk8DNnzW57GIXv84ewt8euzz7_pgSSJVZBXURM0Se9t9QEx8UYApfgNkwr2DynAVcvP5cWf88UlpeCUBCbYn5eY5905sow2LUt_Y2S__IHRar0OvwaASZy2gbW8G4ySd2xSctqF6C3zeqajU8Ut-aWmOkj8Qjcx5HIt11zBH6g-TiDDP3gH7GpR4UxGrtUh2mAPd9LSQ-TeLc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/913265ae74.mp4?token=eq2pL_aMDfnJUCaD5JJnZcY97nz7uq8Lf809OgQp2SqhwhRQVS4iLR11zzDpLf_0vUVD1sqQw3ENObez5KErCf6RAin3IrFza1fpzjBEtxLON1EOoNItej9pN12JWukmc_6Fq4GIHFbHV1m34S1WqRcli2LlMw7QvowAFmsqiA78N5AAU6NF8ihR4V6QSL-eDeqzcubUKjkhRZedIw6YAiZfi6Qk-OqcYQEnkbpehP0LJx54UVyQu87ciXK3_Fu4mcfzTX9CWzqspNZHAfOtQOcIg9Iy16uPaLKYIK9bneUDbjskKE59ObFh01rF5E_CQsRXS00J1L4NIJyC55cRtkpSSkHGJadjMU5Cih7n9TcZ_00oaxhJbyXMygfyjEH59c8222n5ZLw46vR-V2ZR0KlDTKaXxkms8sp8368KwEYqX4XcyUNOfcBnjb0G-LurzHPhgoIoUIrjcO0WnIHWLsFysP5f8zBk8DNnzW57GIXv84ewt8euzz7_pgSSJVZBXURM0Se9t9QEx8UYApfgNkwr2DynAVcvP5cWf88UlpeCUBCbYn5eY5905sow2LUt_Y2S__IHRar0OvwaASZy2gbW8G4ySd2xSctqF6C3zeqajU8Ut-aWmOkj8Qjcx5HIt11zBH6g-TiDDP3gH7GpR4UxGrtUh2mAPd9LSQ-TeLc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
تصاویر ماهواره‌ای از انهدام مرکز اسکان نیروهای ارتش تروریستی آمریکا در پایگاه ملک فیصل اردن در اثر عملیات موشکی ایران  @Farsna</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/451662" target="_blank">📅 19:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451661">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnOH_HXPDTXsfkKi6Ue8oTIWEhPrBh2yNP1XvbuoglZw-C7IdUk0YGXfGYSL0qpgvEQ97fLmUtnFN3Ds9srcyQVzRXzGEhhxF_90MsL2CvL-g7T0a5V5NP9GvA31kgFbWYLdraX1fr97hHnW5yP4hIzoSITV16rJczt8NN_Qydz_AN9evG_owhvJ1I_5TM_jV8exFItCBJI6RY90SRIuh_8s6o7Y44F2uqfumsxtL4Rjt2uIqHMVLviVGhUNR1x0U3HqjlPU2O2Ehsstyk-IGqBEjbVUd6wF8kUmG3ASyyNQBpv7S6V4FgXPVD7pbbY0yy3681EKpzaZ_9x_mfW0mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیلی: دوگانه «جنگ‌طلب و صلح‌طلب» تله تضعیف امنیت ملی است
🔹
وزیر ارشاد دولت سیزدهم: هرگونه تلاش برای تقلیل فضای سیاسی به دوگانه «جنگ‌طلب» و «صلح‌طلب» نه با واقعیت‌های امنیتی جمهوری اسلامی ایران سازگار است و نه با مبانی علوم راهبردی.
🔹
به اعتقاد من، القای این گزاره که هرگونه ایستادگی در برابر زیاده‌خواهی دشمن به معنای جنگ‌طلبی است، نوعی عملیات شناختی برای حذف گزینه مقاومت عزتمندانه از محاسبات افکار عمومی محسوب می‌شود.
🔹
جمهوری اسلامی ایران هرگز آغازگر جنگ نبوده است، اما دفاع از منافع و امنیت ملی را وظیفه خود می‌داند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/451661" target="_blank">📅 19:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451660">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4b70551d5.mp4?token=PuazLs307bHVjUKsSysKhgHiwhTM1qVW0R0xxOpghR23F6YY7fdGXxeh8MOW6NIG6iScIHrWfQCN8KSf50GHNCPhGFmnD5vlO20-sin6IcBW9_TUz-0EqmuAC8EecPXHPKIIx9MsMnj8jjoI5KHQIZDBdeYvXFAD2T0qdrBNxZuEao7yFKsKk9199P9H44tzTjrpRzgGbFfMt8Zsoz6t9g5Nl1Tkk2QxcvelW0BH0Jz8KW8g1sj0-n5t_CajmOvKLEyY-OJCwZmjqFWkX89duEwIsGZydaj5I3YUYZoQsVgEy4NH8kleWQNPR3eBA3qA7xTbLDPvIQqOyWitA3iOLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4b70551d5.mp4?token=PuazLs307bHVjUKsSysKhgHiwhTM1qVW0R0xxOpghR23F6YY7fdGXxeh8MOW6NIG6iScIHrWfQCN8KSf50GHNCPhGFmnD5vlO20-sin6IcBW9_TUz-0EqmuAC8EecPXHPKIIx9MsMnj8jjoI5KHQIZDBdeYvXFAD2T0qdrBNxZuEao7yFKsKk9199P9H44tzTjrpRzgGbFfMt8Zsoz6t9g5Nl1Tkk2QxcvelW0BH0Jz8KW8g1sj0-n5t_CajmOvKLEyY-OJCwZmjqFWkX89duEwIsGZydaj5I3YUYZoQsVgEy4NH8kleWQNPR3eBA3qA7xTbLDPvIQqOyWitA3iOLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای اسرائیل درباره انتقال هزاران سانتریفیوژ ایران به اعماق کوه کلنگ
🔹
روزنامه وال‌استریت ژورنال گزارش داد که دستگاه اطلاعاتی اسرائیل ارزیابی کرده که ایران هزاران سانتریفیوژ غنی‌سازی اورانیوم را به کوه کلنگ منتقل کرده که هدف قرار دادن این تجهیزات در حملات…</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/451660" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451658">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/133652fe64.mp4?token=tPmvIeqQzZMXbbZ2IbdSVSI__BxhJfAksRoaK-dGXsNv3UHOnhPmvYIByveHcRu8_mLKdxtjJ8zbTnvIawsG_r0f0z-CklTJmXbqv_pgXSgrEKs8kDKkS3ZtahwnR9sOgqtTfaZIkhWM-t-eZ-Cruv4pE_SOF5mNKHDPeW1LTbKYEJoa_9S5jChdNT2vZslW-DA8X85Zg3MUus1_0wiQVfnZTjVU7b-Sl3LuFv_b6UwCEja6AYSJ9MNWf4v8rF_3UQbmVW2ltbp_XykSejWCNTzAJn-M9AIerDmobEgtOu7z3QwHIbpYfduOfze98b-qmlGtPHBmeN5QftN8GkZ1ujbiQFSRgnODXaAN3H-OI0m0r73LRuZ_tpggDgPPHzzmE-y8nRY3thrDU9MTyWLgGEQfaSZju5dCIjpJJadMxnzQu2EIo089InF_UcZpfO8JMV6pAKLFSRWGFuUOcJ7dQvOpjHx2YNskYwm4RTMu8cOSIMK4X-SKuragJD0i2St9_ZyzcJZ4c35HSlAIrsaPiS5uokwCo_Dx8PvVWZe1OBIvlymG-HxZfSVINEqIHlF977CP7yKy5euOS4yfAGX6PvY4bPmOPHj9zoobTctL4PIgQpym6LNrqYV_gN8m3l2vtnwDap4PX2VUjPQHB5SZCm3kBQhETy0C4RDjosjOpsU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/133652fe64.mp4?token=tPmvIeqQzZMXbbZ2IbdSVSI__BxhJfAksRoaK-dGXsNv3UHOnhPmvYIByveHcRu8_mLKdxtjJ8zbTnvIawsG_r0f0z-CklTJmXbqv_pgXSgrEKs8kDKkS3ZtahwnR9sOgqtTfaZIkhWM-t-eZ-Cruv4pE_SOF5mNKHDPeW1LTbKYEJoa_9S5jChdNT2vZslW-DA8X85Zg3MUus1_0wiQVfnZTjVU7b-Sl3LuFv_b6UwCEja6AYSJ9MNWf4v8rF_3UQbmVW2ltbp_XykSejWCNTzAJn-M9AIerDmobEgtOu7z3QwHIbpYfduOfze98b-qmlGtPHBmeN5QftN8GkZ1ujbiQFSRgnODXaAN3H-OI0m0r73LRuZ_tpggDgPPHzzmE-y8nRY3thrDU9MTyWLgGEQfaSZju5dCIjpJJadMxnzQu2EIo089InF_UcZpfO8JMV6pAKLFSRWGFuUOcJ7dQvOpjHx2YNskYwm4RTMu8cOSIMK4X-SKuragJD0i2St9_ZyzcJZ4c35HSlAIrsaPiS5uokwCo_Dx8PvVWZe1OBIvlymG-HxZfSVINEqIHlF977CP7yKy5euOS4yfAGX6PvY4bPmOPHj9zoobTctL4PIgQpym6LNrqYV_gN8m3l2vtnwDap4PX2VUjPQHB5SZCm3kBQhETy0C4RDjosjOpsU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نیویورک‌تایمز: در حملات چندبارهٔ ایران به پایگاه هوایی موفق اردن دست‌کم ۲۴ نیروی نظامی آمریکایی مجروح‌ شده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/451658" target="_blank">📅 19:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451657">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAE5Uq69NflospUrDyDneFNr-IKtau32MPpwhznpYkZUoYcuCpazdCr9S_xeGNzX1GDfWfkxUyorO37z30B87j-CoKkq9hu3DHQ2dxVylMTzcftEZqcfsvkKPGcK7df01MkKUboPdgyLvN5l1H036naG5LFj3ljs3_SV80OqumcjPv0kmAZfjUyqi6rXsH4ifkICNQD4LHIG7erbeYMJxaXvehViq1UdNTmsqKpAneYyJRdi4PPM7jmC9i5bsD10-vphCfHZSnKgBcmJupR1B-lkt18uPjzhCZtJZXr2TamQWPU9ZEo-Rx27ZmY85yUR3dK4obRGIw14rle3Ku7mzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نیرو: ۴ استان جنوبی درگیر جنگ از قطعی برق معاف می‌شوند
🔹
استان‌های سیستان‌وبلوچستان، هرمزگان، بوشهر و خوزستان اخیراً درگیر جنگ با دشمنان صهیونیستی و آمریکایی شده‌اند؛ مردم سایر نقاط ایران با صرفه‌جویی در مصرف برق، این هدیه را به هم‌وطنان خود در این مناطق می‌دهند تا این ۴استان از اعمال خاموشی معاف شوند.
🔹
بساط خاموشی‌ها تا نیمۀ شهریور برای همیشه جمع می‌شود؛ این وعده تنها مختص به مقطع کنونی نیست، بلکه برنامه‌ریزی‌ها به‌نحوی انجام شده که با اقدامات کلان مجلس و پیگیری تعهدات در وزارت نیرو، اقتصاد برق اصلاح شده و صنعت برق بتواند روی پای خود بایستد، بدون آنکه فشاری به مردم وارد شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/451657" target="_blank">📅 19:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451652">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iu66idIitPNiEOl9J2zSTUPccTWGQUmhpxckUs35xxiH-lS3FV69W81bgyO5nn5ua05ZWXjoODuDVBAQcmVG6XZhp6nUv2Od2riJDkEf42Ervwqfu7hVj-aqp3iMoFg4pI9dpM0skYRaWt0aQFAS7ZssY5ilMMa_yP9y52idzxBaSkOpzpm_ni4ym6X3-tGabTwYlcrFjImijzkzu1m_5QOdUEmioAId1sAjmuY2YT3QRIt4Xaygezmqus9adL8Bes1ZKR9oPMm7Sd1JDKDNMaSSdIEUK_6WBnpXGKKTCO60jpmwAl00MN_VLHoLF7L_i4KJ2G8Mcd0CjIKit973ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NgCOTThkhWjeR3wOaChMOYp6XYf5QSoJoa871wKob9HzDuzO7Pw7nEAMmcfDO_Y60MulT7tEglZqkSnqFPZit6AtsQCRDys2KC7_vxFj_4H-v1y0cmfz0jwXJ6HAsspE6AOTeiLzR7hbg2mxRuYXRUYTh3kTO62LLOKocfCuKZ92l-0IUBgftg-yVBYCgrubD1sHdCyfvbGl9xDvSSNmfErRYmycqtvdoddnANv4xFc0Wn2GbMEwz7GQLJOxsqv89LGmdHdhX9fjs73KbvNpNEQr5_7qMapwY3CRFEuElSWnfqfAE1SQ74hvLGWK4JV8_bM3pQTsXvbC_Cul0G8aPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NwWR58PG7QVetXSSFopLp2lDMdjOPCJcn-CvUffWUVeZF1aYwBXFwNj0VpHknkQsWzEeigDCHGDb7bX1Mo79fghmJ9c7VssqwNpgHzveUP2YL5vHd4b69Ud2Ald5GBA7IaMqhes2cbice-kbBYj7pz1e2u1GNCqnOu2I46-YuFOwyaAMpl6lWiNw98kOzRsZzzRDsgIWn65g1dGfe1xbJOdqe09j9dae-9T3NMj62q1iThGbT0H4hBTevr8wC_whCtAKGjm9lPSXbyCkR5-jBHoQbCqk31gHsANrB0s9O-DsGWDaX0XPWSVpJttfk9UjgbjVo421-KjurghJ_-0CYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SLodbSZ_mUbc-jwePqhWIWlRoFgaE5EQqLeCGf1KdgzHsvHUXhudacyVo26xfvQa1Zj0YXJoA7AzP5NfK95u15Ofivb1RafLvL_EUwPES4pjmChqEyPo02iE-THkIHpS8bP0NV9jCbG7AfvmuZboSSzczBke5nq1XMtubg4UugCfRkG7nk_9yd0LRxlmBVsULGstawEP_mv7fWorqSdd6Ox133FRQeKPGoYHbSWejNVesLnuT1KqASio52fA5EOGTV57IRDnqmX4M5-56O3c0m-h9yGB-VrGXDyQW0RwoqoBAu-K79MxgZKZB7XN2-SJRvIcT-KhNmzbpxuCWEyJTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kaPMU_fMwy17aNsOUfyQup4xo9IbYQ1xkQpaxPruDsGAqqscMc_5QWaIoAHjUpo7DWSzb3SWrR9KnlRfZH5CURP6W-lpwXIaYFGKHYtNyVqxQiCRZtGFijoNGt76ccLvZ4Hfb7GTgNJKEdXu_MpajrrjiohNezu3piXFTqENuIuHlVvxQCDe_r-1029Rdto1cFdSLNVYTcAtT3kz0GkYv3_XYnnSZk2-32o0TkOfNUBtthxFw4YJXAoD62B0pGEjACKIPSd6ujnZs2q6jlp2hXDiLyzs8PubzKDMT_LUyk6bHdLykiFHCQymZKxeirfZ6AERn-jR_bzPxsiWA-k2xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
با کوله‌ای از خاطرات جنگ راهی کربلا شد
🔸
سفر اربعینی سیدرضا مفاخری، جانباز ۲۵ درصد دفاع مقدس، از کرج با دوچرخه آغاز شد.
عکاس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/451652" target="_blank">📅 18:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451651">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-OWRIuY_H3iuxpIbo9QLeUoNlGQIFyBsDcmScLFl4CUQ0VP2d_g0LdlNuZshp1wIlJ_vZxeRR2pgDGjWG6SebrrHkoaP_PxvqAY2E4BfxRwq0p324Upf-WETK_sjdQRn8rw53pl9Dd1K3GYct9BnhtX6NOLPnBmlSvmHYWrmLruZi6IrxZ51it2uI-WwJOmgl_ReY4CbT8fWXVBgGUJcu0sqiFuiyasRvkPVzrw2tdOorKJGK4bYayC1d00m7Ysbfw7-JAtzKwmizEP6ZZKGKXcPx_kK5wCu633vt8XM8ZmNhpuGQJIPyh_saxbrky6WCJBZ_eohmHNbeO4VkT3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنش در تنگۀ هرمز بارگیری نفت بصره به هند را متوقف کرد
🔹
رویترز: به‌دلیل تشدید حملات به کشتی‌ها در تنگۀ هرمز و افزایش ریسک‌های امنیتی غیرقابل‌پیش‌بینی، شرکت دولتی نفت هند بارگیری محموله ۲ میلیون بشکه‌ای نفت عراق از پایانه بصره را لغو کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/451651" target="_blank">📅 18:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451650">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac4ebd229e.mp4?token=b36L4QIOCwqwi8rdu8QaJ6X7tlVSC1k7OvrWipJQJRC3sytN-APe9bGfnH-j5bzk0bbf1B55cOVaxwmihNLYvvmDa9yH5CZ2Lz6VduhKW78rfJBqz4jog30Wg04rlhScNaluBDi93NIMw5dES-QOyf6MNs3bSrAD3Lz3bFSqik3Rc0UqHlxcr_bMGCvXKK41TUM84AmN4rVYJcft-wmaZizhVCtTUv4kegSK3diIhqGcr74SmtE7-_Os-UIupkuo5mu-0xxtrHTUHQxtN9vGL6UYbBwH0nNRZcMgdgBPmfsW2zKzlCj5qXtAtYn_tnCEGnQcdBfiSAkCoNA2C1bPpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac4ebd229e.mp4?token=b36L4QIOCwqwi8rdu8QaJ6X7tlVSC1k7OvrWipJQJRC3sytN-APe9bGfnH-j5bzk0bbf1B55cOVaxwmihNLYvvmDa9yH5CZ2Lz6VduhKW78rfJBqz4jog30Wg04rlhScNaluBDi93NIMw5dES-QOyf6MNs3bSrAD3Lz3bFSqik3Rc0UqHlxcr_bMGCvXKK41TUM84AmN4rVYJcft-wmaZizhVCtTUv4kegSK3diIhqGcr74SmtE7-_Os-UIupkuo5mu-0xxtrHTUHQxtN9vGL6UYbBwH0nNRZcMgdgBPmfsW2zKzlCj5qXtAtYn_tnCEGnQcdBfiSAkCoNA2C1bPpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نسلی که برای نوکریِ اباعبدالله(ع) قد می‌کشد
@Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/451650" target="_blank">📅 18:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451649">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnqR7WbofCEgRa92Pu-k-WeT7FaNchI2eeFrjwMd3KIna-nC8DDgn4C5z0rJP99oJo0P_3RKfsVVqryGwXdH5XDNCgZk9bQ_71Qr5xWl9Y2zbHAoFxeOhQgMJCVhtC7yYZSH22r0BA85AAI-mFyr5AnZsB18EB_20lcwWJgKj5H5nZV1HkO2lEHpyVG7vqcXeDJ0fRHi7k0QGJo6hErwYoJTzO6I5n_VPDs8wG48UPbE0BvYUFt0e4rkARDbjfiD8sGfZssWmxPArBxFVBArM4ZqbS4Gqgui6WMvFJyuhh1Hq8neW9lMXx1wILjDbmJxvbdIY2XUwSQmqE3uc1tVcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
به قعر خلیج فارس فرو خواهید رفت
@Farsna</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/451649" target="_blank">📅 18:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451648">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S73Rje-B7C2GvXWZ-qV9DV1ZSM1BYCGmeVQFCsFpt9JXG4BmJ8iOtxXkzDf9rF29-uDPVnVz_nqhRyq90jPDZWWUhdHZN9MGF-yPyNxNiB2MewNVvShadgxkl00RpDcJu7_P36LTlmZzUeuNjZfScga0VBL9zQ5-1vJOnLHXK13OWtF3c2aJnPpS3CqTW-QGy-nmudqz4ofz7XoEYvhLWfx5TCP-UTdFlxYUPbNJwDDqI0R39wXEqk61o15sDD1BBItbXGM8n11ynoeyAAK9i7fcdSl3vKQwro3SQetbm9I4BqeU796n2uUNri6Gq3V7yNdh0qAadFoCRQznRO9IBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع عربی: ۲ نفتکش حامل نفت عربستان، درپی محاصرۀ دریایی اعمال‌شده از سوی یمن، مسیر خود را در دریای سرخ تغییر داده‌اند و به‌سمت کانال سوئز بازگشته‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/451648" target="_blank">📅 18:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451647">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DycHMpp1ASsXdN5kZ4SGH1VUr6ywV2HPedAnfY5pGreHzKN8wUGVVUKZnEqs1vYmcLoXzj4dVh9v7WME10ienOVhZrkw7P64dEr-wr-67fHpdlxvfvLUIUVVaiMX0lgaqCbR2gHr3rfSRRcjylYWexka6VvTYQsuZrRq1g2lk8OUbETg4_wbEWMgnb2i6_FdfU7CA5WcrxmnhpCbVhcYCpKduVW8uwLHOnonYI7bjR6FYX72rpyLcozm9z1E2HaiBk1evfyfeusbG25-PwWGB0d-Go-MbBLsFrxq_1VnNp72dr2rxoV6hv8MV2iLAd3T9WeL_8Q3EimjqqA1dtMCmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخستین معاملۀ پساب در بورس انرژی
🔹
بورس انرژی ایران: با عرضۀ ۲۰۰ هزار مترمکعب پساب تصفیه‌خانه آبفای تهران، ۳۰ هزار مترمکعب از حجم عرضه‌شده برای اولین‌بار مورد معامله قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/451647" target="_blank">📅 18:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451645">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۹۹.pdf</div>
  <div class="tg-doc-extra">3.1 MB</div>
</div>
<a href="https://t.me/farsna/451645" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۹۸.pdf</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/451645" target="_blank">📅 18:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451644">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RihDzKM01bF3Oo7mZJZZAFhPLGDcRVgsMt4PVikgm3u9jt6H2Dtby2GIXv6swaIcewgCD-4aEEDIg_Ngm4UFKZZOuiLh6tHeplNur7koasSUK4e3SjuK9PPgj9GicCvyH-Vs1K-0RgMTKo7rs05f5W10MqOYeo5p-_xEQWILpMkyJlhRcrlDYEanuJp1yvBX9DKpkphcvIxEy31czAvssejLx-GdvjiYQ8GGpLyIqwNdeESyyc1J2-w9NuB8OaTbBUYFuK6Qfcdqc8QK0szBV7EPhjBFrk1I56urgLPkMq_6A60Nfb9AKt-2MYtiu4APxkzWS857FtruvMUTIpqwQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور اهالی فرهنگ و رسانه در دل جنوب کشور
با حضور چهره‌هایی چون علیرضا دبیر، سعید حدادیان، یامین‌پور، خضریان، حسین پاک، خانعلی‌زاده و جمعی از فعالان فرهنگی، رسانه‌ای و اجتماعی، ویژه‌برنامه‌های در جنوب کشور برگزار شد؛ حضوری برای روایت از همراهی و همدلی با مردمی که این روزها داغدار حملات دشمن هستند.
@Farsna</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/451644" target="_blank">📅 18:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451643">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRC5EFRF6Jck4sneW2KSDL6zzrcGxf9QYDp3ufzz3FqiKDDQ7svHGOZoK14D5gsSfWMZpNfPUMjJUz4tF_Prdk0wEXlZ_Z90UxvcLkN7_aZU0o1gmmoJdRhR97v8JJurrg7gemgb5-E9t-qQDp-v0Aw6ExueaZTzUxhsH_8DGRVBpv-SY4XoneeLCg77wKVSDgYTfjyWSNuNQGHaeXDLX9RuruHw3YXbt-X-wwkcqqapuXeygQtbMFmcSfxyqNjHyT-m0ii6SJFVsigTXH-82UOivkEFJSn0vHMVOxzs-tfJsohhxt3q8DJBIvVJzo8lbeYYjDPRqHy9-iTpkm6lMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
مجامع شرکت ملی صنایع مس ایران؛
🔰
سهامداران «فملی» ۳۱ تیرماه درباره افزایش سرمایه و تقسیم سود تصمیم می‌گیرند
🔻
شرکت ملی صنایع مس ایران (فملی) مجامع عمومی فوق‌العاده و عادی سالیانه خود را روز چهارشنبه ۳۱ تیرماه ۱۴۰۵ در مرکز همایش‌های بین‌المللی صداوسیما برگزار می‌کند.
🔹
در این مجامع سهامداران درباره افزایش سرمایه ۳۷.۱۴ درصدی، تقسیم سود و دیگر دستورهای قانونی تصمیم‌گیری خواهند کرد.
⬅️
افزایش ۳۷.۱۴ درصدی سرمایه در دستور کار مجمع فوق‌العاده
🔹
مجمع عمومی فوق‌العاده شرکت از ساعت ۱۴ برگزار می‌شود. در این نشست، گزارش توجیهی هیئت‌مدیره و اظهارنظر بازرس قانونی درباره افزایش سرمایه ۳۷.۱۴ درصدی شرکت از محل سود انباشته، از مبلغ ۱,۰۵۰,۰۰۰ میلیارد ریال به ۱,۴۴۰,۰۰۰ میلیارد ریال، برای بررسی و تصمیم‌گیری سهامداران ارائه خواهد شد.
◀️
ادامه خبر در مس‌پرس:
https://mespress.ir/x6RM
@mespress_ir</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/451643" target="_blank">📅 18:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451642">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/451642" target="_blank">📅 18:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451641">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8_N-_msim9cJcj0aGEb0JHtEY0yz30Q3zmvDrchOD3GI1tHF1Cl4vQu0eEeuwtUpaGOuif0j3oFGKzef7xO3UpWc4iFX6zRDotdHY-J8RByCilEg0MM527v7MGZTCtDc_q204P5irETLHzIaYvYgQczl3W35fyFqwGzOEPGelY4HHUJrlzZGWOz9zLRRYCcyeCBlVpSswdJ5DjqTPIfwbPhORZZqU3-ZwIMv7cHKQ75ebHCUEu9ikyNfEgicnxyRmpAZcLA35ZBEg371Z0MUDCbSOqpUwP0Guw_Ec-P2MIvKqiQqMf0C2Hf0QWpR0auQ4xKVTUCsbsC8PjI1E7jZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صداهای انفجار در بحرین و کویت خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/451641" target="_blank">📅 18:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451640">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjqfF1SV2ZvsKaSJ_nPRnGG3ISspxLNX7iuVxeyn5WD6F-RMT7zWWUyzUpsI_u5DQT1KakS11_ZWUF1GGaIXgPvGDdlpihGsJM3qNWNnjUrdU-tmqxWNlNZ-5xyLvAhNBFzeRhoZs0QBnpcpRPggx5f4PZj_iYW62LbHRJ1bwvrZrUNrwZlWeaCcWHtHqf6YKXbRxOPbDL32zUinfBH42cdGrgfZRy78QIDXOWoMbRwjmy4dy-UqSbSYJg5hUfRFuYPECml81lW_c84aIPDM6d8_InfZNa3TVwEx6avf0WNkgk-DuXw9qYQWzDN17QC8ndxsK1EJgfTqy9yG_qj_Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«استادِ بی‌تعهد» و فروشگاه اتکا؛ افکار عمومی منتظر ورود مدعی‌العموم
🔹
انتشار یک استوری اینستاگرامی از سوی فردی به نام رحیم زاهدی، که خود را استاد دانشگاه تهران معرفی کرده، واکنش‌های گسترده‌ای را در فضای مجازی و رسانه‌ای به دنبال داشته است.
🔹
زاهدی در این استوری مدعی شد که مادرش به دلیل نداشتن روسری هنگام مراجعه به یکی از فروشگاه‌های اتکا از دریافت خدمات منع شده است. او همچنین ادعا کرد که پس از تماس با معاون وزیر دفاع و رئیس سازمان اتکا، مسئولان مربوطه ضمن عذرخواهی، برای دلجویی از مادرش دعوت به ملاقات کرده‌اند. این ادعا تاکنون از سوی وزارت دفاع یا سازمان اتکا تأیید یا تکذیب نشده و هیچ مقام رسمی درباره جزئیات آن اظهار نظر نکرده است.
🔹
در همین حال، بررسی‌ها نشان می‌دهد زاهدی در صفحه شخصی خود عنوان «مشاور وزیر نیرو» را نیز درج کرده بود؛ موضوعی که روابط عمومی وزارت نیرو آن را رد کرده است. این وزارتخانه در گفت‌وگو با فارس اعلام کرد که وی هیچ‌گونه سمتی در وزارت نیرو ندارد و عنوان یادشده جعلی است. همچنین حراست وزارت نیرو اعلام کرده است که موضوع را از طریق مراجع قانونی پیگیری خواهد کرد. پس از انتشار این واکنش‌ها، زاهدی تمامی عناوین دولتی و دانشگاهی را از صفحه اینستاگرام خود حذف کرده و تنها جمله «عدو شود سبب خیر اگر خدا خواهد» را در معرفی خود باقی گذاشته است.
🔹
این ماجرا دو موضوع متفاوت را پیش روی افکار عمومی قرار داده است که هر یک به‌تنهایی نیازمند شفاف‌سازی و اقدام قانونی است:
🔸
نخست، اصل ادعای مطرح‌شده درباره نحوه برخورد در فروشگاه اتکا که نیازمند پاسخ رسمی از سوی مسئولان مربوطه است. آیا واقعا به واسطه تذکر حجاب باید از فرد متخلف عذرخواهی شود؟
🔸
دوم، استفاده از عناوین و مسئولیت‌های دولتی که در صورت اثبات جعلی بودن، صرفاً یک تخلف فردی نیست. وقتی فردی با القاب جعلی در فضای مجازی ظاهر می‌شود و از آن برای اعمال نفوذ یا تأثیرگذاری بر افکار عمومی استفاده می‌کند، این موضوع جنبه‌ی عمومی پیدا کرده و باید مدعی‌العموم نیز به آن ورود کند. حرکت‌های حساب‌شده‌ای از این دست، اعتماد عمومی به نهادهای رسمی را خدشه‌دار می‌کند و نمی‌توان با آن مماشات کرد.
🔹
این نکته شایان توجه است که اگر این فرد واقعاً دارای مسئولیت دولتی یا دانشگاهی بوده است، مردم حق دارند بدانند چگونه افرادی با این سطح از بی‌تعهدی در جایگاه‌های علمی و اجرایی نفوذ کرده‌اند و خودشان به‌جای حل یک معضل اجتماعی، به عاملی برای ناهنجاری و بازتولید آن تبدیل می‌شوند. استادی که به‌جای روشنگری و ارائه‌ی الگوی درست، با حاشیه‌سازی و القای این پیام که قانون قابل دور زدن است، عملاً به تضعیف فرهنگ حجاب در جامعه دامن می‌زند، شایسته‌ی چنین جایگاهی نیست و باید پاسخگو باشد.
🔹
و اگر عناوین مذکور جعلی بوده است، موضوع از یک تخلف اداری فراتر رفته و مصداق کلاهبرداری و سوءاستفاده از عناوین دولتی محسوب می‌شود. در این صورت، نه تنها حراست وزارت نیرو، بلکه دستگاه قضایی و مدعی‌العموم باید با جدیت وارد شوند و با این پدیده‌ی خطرناک که می‌تواند الگویی برای سایرین شود، برخوردی بازدارنده داشته باشند. اجازه دادن به چنین رفتارهایی، راه را برای سودجویان باز می‌کند و نظام اداری و علمی کشور را بی‌اعتبار می‌سازد.
🔹
گذشته از ابعاد حقوقی این پرونده، آنچه در دل این ماجرا نهفته است، مسئله‌ای اجتماعی و فرهنگی به نام حجاب است. بی‌گمان، موضوع بی حجابی و بدپوششی به یکی از دغدغه‌های جدی و مبتلابه جامعه‌ی امروز ما تبدیل شده و بسیاری از بانوان در این زمینه با چالش یا سردرگمی روبه‌رو هستند. این واقعیت تلخ را نمی‌توان نادیده گرفت.
🔹
در این رابطه توصیه شده است که همه ما نسبت به هموطنانمان مسئولیت داریم و وظیفه داریم با دلسوزی، صبوری و آموزشِ همراه با کرامت، زمینه‌ی اصلاح نگرش‌ها را فراهم کنیم. اما این مسئولیت هرگز به معنای کوتاه آمدن در برابر قانون، مماشات با تخلف، یا باج‌دهی به جریان‌های حاشیه‌ساز نیست. قانون حجاب، قانون قطعی کشور است و هیچ عنوان و جایگاهی مجوز عبور از آن را نمی‌دهد. کسی که خود را استاد یا مسئول معرفی می‌کند، بیش از هر شهروند دیگری مکلف به رعایت قانون و الگوسازی صحیح است.
🔹
اگر فردی به‌جای کمک به ترویج فرهنگ حجاب و اصلاح این آسیب اجتماعی، با القاب جعلی یا سوءاستفاده از جایگاه خود به دنبال ایجاد فضای التهاب‌آمیز و تضعیف قانون باشد، نه تنها به جامعه کمکی نکرده، بلکه به اعتبار نهادهای علمی و اجرایی نیز آسیب جدی وارد کرده است. دستگاه‌های نظارتی و قضایی باید با رویکردی منصفانه و قاطع، هم از حقوق شهروندان صیانت کنند و هم اجازه ندهند قانون با حاشیه‌سازی و اعمال نفوذ تضعیف شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/451640" target="_blank">📅 18:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451639">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a4b05777b.mp4?token=lIYyrmLH4axDHIx3YB-_n0tEJCIRnV6v6o8VkuVC2TluuKFt8peq6EZoAm7KV2E43xsGKmxKO8lR8SaBmkwalngsnBd6rJSHdxZ5auYP5ue3XsiDSGAd5TtuLP8lMIeggB0tMv1aTvEI0a7lRR1OL-RMBZaT2PfrqB7bgGxInsc67HL_AD_siQl8pNuUFZnjeHRoULDBavZjek7MOUEF7rLEjNVyy73qLEiQ5qQGIv882kXkIiKnjk28oWbMOTcGrKvl6J8RGTe4jNJeUhKWydLsZf8YpmRXiPp2K6m73c_t0Ip5ySbPqDYzSQ9u0xpjY3YolQieSCGg-BRXkXZq5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a4b05777b.mp4?token=lIYyrmLH4axDHIx3YB-_n0tEJCIRnV6v6o8VkuVC2TluuKFt8peq6EZoAm7KV2E43xsGKmxKO8lR8SaBmkwalngsnBd6rJSHdxZ5auYP5ue3XsiDSGAd5TtuLP8lMIeggB0tMv1aTvEI0a7lRR1OL-RMBZaT2PfrqB7bgGxInsc67HL_AD_siQl8pNuUFZnjeHRoULDBavZjek7MOUEF7rLEjNVyy73qLEiQ5qQGIv882kXkIiKnjk28oWbMOTcGrKvl6J8RGTe4jNJeUhKWydLsZf8YpmRXiPp2K6m73c_t0Ip5ySbPqDYzSQ9u0xpjY3YolQieSCGg-BRXkXZq5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خط و نشان کودکان ایرانی برای ترامپ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/451639" target="_blank">📅 18:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451637">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌ قالیباف قانون برگزاری جلسات علنی مجلس در شرایط اضطرار را ابلاغ کرد
🔹
طبق این قانون مصوبۀ جلسه علنی ۲۲ تیر مجلس، در مواقع اضطرار و شرایط خاص کشور که بنا به تشخیص هیئت‌رئیسه، حضور نمایندگان و برگزاری جلسات رسمی مجلس از جمله صحن، کمیسیون‌ها و هیئت‌رئیسه در…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451637" target="_blank">📅 17:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451636">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwG_ztzORrHLpSwK3tPK3PnxDLysmYymwGiYbSLt4ZlojSSJgK2iODRDWqEPFBFksSmug7IduwOBavZYbdwgVp4e_9iWrBywUDe9-1Vp63BCCJwMLs0PzdmH4d7fVaESwVaANcPTO_87wYUDqU1OFTwWQ_6N15W2YfHVU1PXK4z2-qu8fUp3_hR3TrIXaej71mgS7sREqHWzQmVcFhj1QqTqxpVAoE7ldz27BhDvb9afSOQmLMQfKAtX5_LUt1Gfp9JZwhrbSF6asEma6P6-jiOuU-H3g8tM0kOgQdwXeF64JVlDbqsDhJ2rbpFc6Lw5bcsKcHek_hyriRpM54JD8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع عربی: ۲ نفتکش حامل نفت عربستان، درپی محاصرۀ دریایی اعمال‌شده از سوی یمن، مسیر خود را در دریای سرخ تغییر داده‌اند و به‌سمت کانال سوئز بازگشته‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/451636" target="_blank">📅 17:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451635">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b9a6787d1.mp4?token=HyPSqARc7PZEy4vdkHhuWZUnYAoP7hiiMgY-lVU0RPCu-FkuxeGPMJkcyG5-X514c-97Mqx2115xGMkDyDSAtVFC3SpzBcZ0mlSuDXTVHMOAvThEk1TVlLY_gKXIIzkNVDdWmyhOPSwQ5xrV1gFM7zDXEq_m1_op3MhZomFv6s9UuwZVbdvdtJ_DANaUGCbdKGB14g3Jte4OlUPnDcd5R-vRHzDBKpTliPoQS8Bs92ktNbftIvDCNPFzm7al8qtid9Kw3gYUi-I9FrkrFtu9YqQeyZ5KL3dni87p_PKA7kFKUrHqd0EHVs46vQ3NKwEWKTjmDcqSbx3RgnnIVn-v1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b9a6787d1.mp4?token=HyPSqARc7PZEy4vdkHhuWZUnYAoP7hiiMgY-lVU0RPCu-FkuxeGPMJkcyG5-X514c-97Mqx2115xGMkDyDSAtVFC3SpzBcZ0mlSuDXTVHMOAvThEk1TVlLY_gKXIIzkNVDdWmyhOPSwQ5xrV1gFM7zDXEq_m1_op3MhZomFv6s9UuwZVbdvdtJ_DANaUGCbdKGB14g3Jte4OlUPnDcd5R-vRHzDBKpTliPoQS8Bs92ktNbftIvDCNPFzm7al8qtid9Kw3gYUi-I9FrkrFtu9YqQeyZ5KL3dni87p_PKA7kFKUrHqd0EHVs46vQ3NKwEWKTjmDcqSbx3RgnnIVn-v1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراق مهیای حضور میلیون‌ها زائر اربعین
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/451635" target="_blank">📅 17:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451634">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/920b3a3802.mp4?token=fikvODHuMz_cl9eKMeeKGpLfFR9Eo7TaEpoj0CnXyZRyLiReJxEhBY5Sz-pLis3Q86EUmPhrZJQRXAbrrRojTg1hIeWEKwompPWLNUc79tBWyiNRoXxLcEXpX-NmpazpzqWwD2qy3GvmlX_FPIyVPKxoupun_ADfx-IpBmPXY2J8YFqz6lumaO0443aMRaxfymxTeBR4BrMbF4EUtz5dIcvahZoGB6mB3Q3D41_qU8NC_UICSI0HqXCIG2DaZDtmf8zZbr7imPlegeI52RKwf9zKVAM-LT9aKN58A1FAyKWXModQzMXSxor3EgY1NmhroIobNMAXmxR5sC8-Z_9AXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/920b3a3802.mp4?token=fikvODHuMz_cl9eKMeeKGpLfFR9Eo7TaEpoj0CnXyZRyLiReJxEhBY5Sz-pLis3Q86EUmPhrZJQRXAbrrRojTg1hIeWEKwompPWLNUc79tBWyiNRoXxLcEXpX-NmpazpzqWwD2qy3GvmlX_FPIyVPKxoupun_ADfx-IpBmPXY2J8YFqz6lumaO0443aMRaxfymxTeBR4BrMbF4EUtz5dIcvahZoGB6mB3Q3D41_qU8NC_UICSI0HqXCIG2DaZDtmf8zZbr7imPlegeI52RKwf9zKVAM-LT9aKN58A1FAyKWXModQzMXSxor3EgY1NmhroIobNMAXmxR5sC8-Z_9AXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دفاع دوبارهٔ رضاپهلوی از حمله به خاک ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/451634" target="_blank">📅 17:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451633">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صداهای انفجار در بحرین و کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/451633" target="_blank">📅 16:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451632">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فرانسه کاردار سفارت ایران را احضار کرد
🔹
وزارت امور خارجهٔ فرانسه از احضار کاردار سفارت ایران در پاریس به این وزارتخانه خبر داد؛ این احضار درپی ادعای بازداشت کارکنان سفارت فرانسه در تهران انجام شده است.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/451632" target="_blank">📅 16:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451631">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1f14ee037.mp4?token=DvpoPbm0x4cEKQWT_XNVGeiKS65panEw2oUcVEiOtxtOqT6urXFqBdn-ACfQFQFmsEH3B7FRHP_aqT8sjdkkUnz_XhKd-NZvl5IzxXpwjfhK9ABroz_KghQ_R4SoClmKDqoUorYDsZwiQT7fZKO2KmDOO9Kkv-8eXLG5vzW6eAZbeZGlQxsRcj1ofMqbYpMbxVi1292bJ2ICSp9d_f9znYHsZUfUjS1PXJN0RZnZqCRA-XurA74jZdgsHsM6KEvfIB7kcnizg-gOQ2RCN3lMkwX92qRqdaRmoRlefsJ8dOOa0dvUQCRd_Np-V2r9Z86Bbv04E02p_FztX68DQ5d1BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1f14ee037.mp4?token=DvpoPbm0x4cEKQWT_XNVGeiKS65panEw2oUcVEiOtxtOqT6urXFqBdn-ACfQFQFmsEH3B7FRHP_aqT8sjdkkUnz_XhKd-NZvl5IzxXpwjfhK9ABroz_KghQ_R4SoClmKDqoUorYDsZwiQT7fZKO2KmDOO9Kkv-8eXLG5vzW6eAZbeZGlQxsRcj1ofMqbYpMbxVi1292bJ2ICSp9d_f9znYHsZUfUjS1PXJN0RZnZqCRA-XurA74jZdgsHsM6KEvfIB7kcnizg-gOQ2RCN3lMkwX92qRqdaRmoRlefsJ8dOOa0dvUQCRd_Np-V2r9Z86Bbv04E02p_FztX68DQ5d1BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امارات چطور وارد دهان شیر شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/451631" target="_blank">📅 16:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451630">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qu6PeZuaWn1xgJsMeV1j2iNhquu_a_gLF8e-ganjsCZCDS2l-gEQVLtfS2sX598MwkLhwqevub-zdT75qgc0VtDIiJsIWOEF5q64WlXk8xe--W0f23E64jHgRqu2oc8B-MF1vaUCn-343UU06dXmNeLbcowbXTJw9Jmww7QTA7VLhWyCK3UmDPxoFsXZszqi_ABNXm9mvT6dg4G0fL-8gUwhzh7YWw69AxLWmJwjHDH2e4nTxX06sbU4B3eg5F0QtBTloShA-9qdqOW2VfevZo-0xHDvDlI8gCOYrwrIfvprsNUDPnDwJhEoKnx25IhKlu_hIFf6r9Ch0bolpXAtcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار جنگنده‌ها و هواپیماهای سوخت‌رسان آمریکا از پایگاه‌های منطقه
🔹
به گزارش شبکهٔ ۱۴ رژیم صهیونیستی، آمریکا در واکنش به حملات گستردهٔ ایران، اقدام به تخلیهٔ پایگاه‌های خود در منطقه و انتقال جنگنده‌ها و هواپیماهای سوخت‌رسان به اراضی اشغالی کرده است.
🔹
همچنین یک تحلیلگر مسائل نظامی و امنیتی در شبکهٔ ۱۴ رژیم اشغالگر، اعلام کرد که آمریکا در حال حاضر قادر به حفاظت از پایگاه‌های خود در منطقه در برابر حملات ایران نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/451630" target="_blank">📅 16:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451629">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBn6V239bPVVgkcZ_vefKsdDEThaNTtKjKJs1v_bO62kzhpk0dVwkBleLlYG41YPFwuvbATQEMY1IQG4DFceivF5ySvkOZmETfXQ0fBVCI8tE71SRlrc-KGA16kdimJX7iOEE7PSeRbyUa4nnws7kK3bHTIwhd0W6z8BuBZVoU9cf2c2sednunk6u8nemI9ThAy1M-VCF1poC1_jnEgBRnE_KxFQsiIs0W5_xo6yiiyInJL2EcGivN7Q7mM4pqRQj18GMrEoAfISfVp6eUu7hAJwAJeL_Nk1EvqguOWabc6fOBYMeVJ3UdKtHJrxUnPMgc-kw_jOCdBnw-UNkB9ruQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت و نان عربستان در حلقهٔ محاصرهٔ یمن
🔹
نیروهای مسلح یمن با اعلام محاصرهٔ دریایی عربستان در تنگهٔ باب‌المندب، مسیر جایگزین صادرات نفت این کشور را هدف قرار دادند.
🔹
عربستان که برای دورزدن تنگهٔ هرمز، بخش عمدهٔ صادرات نفت خود را از طریق خط لولهٔ شرق–غرب و…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/451629" target="_blank">📅 16:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451628">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gt9vF3WTI4I6X0wyJShMx60u8UCmgUBugS0YuDIoH7aSl8HARmwpxlyPwJdRdp_BWhSDKZ1CaCvGVCLlmZvce9F75_XF9PwH30j41arDe3zm_huxB-tQe-MfFvTJTinCIen1yQvkV2VY9cKnjlOxwfDtiSPT6jjirlZ7mj3Ktn0ao_z4BiTAa2ZTfVEUbxolf_7tXgvcJF3OkM-Lv7zcQfHDYeYqk6uOHNkuKEkLXxgh3iv-ZRG3Mby-7Qhq9f7rno8iEqXBSst-oLa0ZYjyoXNzhHE020BMyoi-Ye3R05AfFqqJrKc0PYbh67qGTyAKv4Bch4DJ_NPzrgZ3pLXkug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بهرام گودرزی مدافع ۲۱ سالۀ فصل پیش آلومینیوم با قراردادی ۵ ساله به استقلال پیوست.  @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/451628" target="_blank">📅 16:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451626">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iVaWntrDWdmPqyaV91ZFhvcE8sdV2Z6ym2FtGjkNf9ZRi9Qr890cqde-HeBQ4KO1vgEbp22rRi4E5OdAEJwWb7iJD16l4yj3_SeHEOVFWiI3L8_ITuzJiGLTSK_huxbW0R8nrQqr6qLCY7G2NVyGL1C-CvKvEWbdGbGK1BtfnAh8i0tuMHxiGluscJC6rDFaAqPRjlfuplghA_USUw4BDEh5_ckIC39cQjRuLP-CeKYnF6wWT-iWRrV48wAK3yZBKmRlcmDcRSwGEIYmt92m0CidWizYp8ohN5AzuTrdJqaezOJQJ4XW47ZkQQGptXnAGAyXpD7hQ4ODNczTakJw4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZQyxMOybpdta90uELFmG-sl8XdUG9XyxWio-1cQO7WhBX-w0F0faLVEOgAm-G4apDGuTzlYP8npFiAJwCEvVn0F39gqWCwe2aqLrNBDPeCfMQGHA1fFQF1kki1GhpAGImxFvURVDp0Hs5uwxwiIGnlJIs5PNLwpmSia_yrks9n5RJGtzM8j8NlKl8wfcO0yNj3AWjqa56u58bYyd17AHA1lb7YPYUDSK7U7OxjSOrSZsUpAVRY6pw4GDZo8AVRJp98vrf5JHgU0z_tcF8kaIPhmxeuAJzfTwKT46yNRJTuFGXhTVIl3yLDhbYN-z9E-_oFoTtnNq875RMpH91Al2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نارضایتی اکثر آمریکایی‌ها از عملکرد ترامپ در جنگ ایران
🔹
بر اساس نظرسنجی‌های منتشرشده توسط فاکس نیوز، ۶۹٪ از مردم آمریکا از عملکرد ترامپ در موضوع جنگ با ایران رضایت ندارند.
🔹
در این نظرسنجی که توسط مؤسسهٔ ایپسوس و روزنامهٔ واشنگتن پست در ماه جولای انجام شده است، تنها ۲۹ درصد از مردم آمریکا از عملکرد و نوع مدیریت ترامپ در جنگ ایران رضایت دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/451626" target="_blank">📅 16:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451624">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8gxPS0a_S9NRpLAPJYyjx2yFWwXaXB1KcITaK-4M0vjmkuQ3vxSl5o6GjbECUdoDCBjjzJaIgUr7UitGHnm47sJsZkVtPSTYRdmuObv__p3v1w420Lm6oPv4b-Tbmg9c684NubqbsZuDUuO7cEB_kv-cFi4KFfh8IP0alKR8-kt2QwqMPDFmMNbTtP0kyNT88Mmbgj2qydmt4pVG42JviCb6DzCoPhmjWAIEDF1OiFVLuN9JEO6SzpjFbTprjBurPv37MevIGQ0F_FjxLz0prPHIqYoeTvkS-Hr6JVpMcDgym87_5yJHngFpnS8l7Jlv94ymtX-Yl1VpHh_3YOv4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفحص ۶۲ قطعهٔ دیگر از پیکر شهدای مدرسهٔ میناب؛ ماکان هنوز مفقود‌الاثر است
🔹
فرماندار میناب: درپی عملیات تفحص در مدرسهٔ میناب در چند هفتهٔ گذشته، ۶۲ قطعه از پیکر شهدای دانش‌آموز کشف شد که پس‌از آزمایش‌های ژنتیکی مشخص شد که این قطعات متعلق به ۳۲ دانش‌آموز است.
🔹
رئیس‌ دادگستری هرمزگان اعلام کرد که با وجود انجام عملیات متعدد تفحص در این مدرسه، تاکنون هیچ بخشی از پیکر شهید ماکان نصیری پیدا نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/451624" target="_blank">📅 16:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451621">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-text">منتخبی از پویش‌های پیگیری شده «فارس‌من
»
🔹
شما
گفتید
: به بلاتکلیفی مسکن مهر اسلام‌آباد غرب پایان دهید.
🔸
معاون مسکن و ساختمان اداره‌کل راه و شهرسازی استان کرمانشاه
گفت
: با ورود دادستان و فرماندار یک فرصت نهایی ۴۵ روزه برای اتمام و تحویل پروژه به پیمانکار داده شد که اکنون با گذشت دو هفته از این ضرب‌الاجل و افزایش نیروهای اجرایی، پیش‌بینی می‌شود بخش‌های باقی‌مانده طی یک ماه تا ۴۵ روز آینده تکمیل و واحدها به بهره‌برداری نهایی برسند.
🔹
شما
گفتید
: به وضعیت شیفت و اضافه‌کاری کارکنان آبفای ایلام رسیدگی شود
🔸
مسئول روابط عمومی شرکت آب و فاضلاب استان ایلام
گفت
: تمامی فعالیت‌های عملیاتی به‌صورت شبانه‌روزی و در قالب تیم‌های چندنفره انجام می‌شود و ضمن رعایت دقیق قانون کار در پرداخت اضافه‌کاری، تعطیل‌کاری و شب‌کاری، استراحت قانونی کارکنان و تداوم بی‌وقفه خدمات‌رسانی به مشترکان نیز تضمین شده است. است.
🔹
شما
گفتید
: برای تسریع در تحویل واحدهای مسکن ملی اردبیل اقدام کنید.
🔸
معاون مسکن و ساختمان راه و شهرسازی استان اردبیل
گفت
: از مجموع ۲۷ هزار واحد طرح نهضت ملی مسکن، تاکنون ۱۴۰۰ واحد به متقاضیان تحویل داده شده است.  ۳ هزار واحد دیگر در شهریورماه آماده تحویل است؛ مشروط بر اینکه دستگاه‌های خدمات‌رسان نسبت به تکمیل انشعابات اقدام کنند.
🔹
شما
گفتید
: شهرداری کرمانشاه معابر عمومی را از دست متصرفان آزاد کند.
🔸
شهرداری کرمانشاه
گفت
: با رصد مستمر محلات، به متخلفانِ ساختمانی و سد معبر ابتدا اخطار داده می‌شود و در صورت عدم تمکین، با قاطعیت با سازه‌های غیرقانونی برخورد و تخریب خواهد شد. از شهروندان تقاضا می‌شود هرگونه تخلف و تصرف معابر را برای رسیدگی سریع، از طریق سامانه ۱۳۷ گزارش دهند.
🎉
شما نیز می‌توانید مطالبات‌تان را در سامانه «
فارس من
» ثبت کنید.
@Farsnews_My</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/451621" target="_blank">📅 15:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451620">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3e708a1f5.mp4?token=WMSyF0Ufm0cVTD3K1jbXCSCsG8ljhy_8i8KPABnbwLrgkRfmINzgHYOFZZ5qMPZdRgcsWWdYz9-vgTsJA5v_YFGlEgc4tRUPfG6noKsFFSAQOUJezf0ORM_I1ljdHuWeVDzs8FdoVjolNBOTRs5L2x7TeVa_XKScbNyc7tlxDM9qE-B29YFmUGdZxNgReTHuI_8RYoVJVr1jZ3aCaBKZjFPTCc7tIrIoIlNzPLOuhLXx8_flnSk1KpKhD41dBDRIvlRlUlNiY73Cha830IK0AOqugtY88JmH_a29hjhdxui69iNhN6pevK0HE5rQJGqqyi6U87anK7Dtzfpj4RYS1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3e708a1f5.mp4?token=WMSyF0Ufm0cVTD3K1jbXCSCsG8ljhy_8i8KPABnbwLrgkRfmINzgHYOFZZ5qMPZdRgcsWWdYz9-vgTsJA5v_YFGlEgc4tRUPfG6noKsFFSAQOUJezf0ORM_I1ljdHuWeVDzs8FdoVjolNBOTRs5L2x7TeVa_XKScbNyc7tlxDM9qE-B29YFmUGdZxNgReTHuI_8RYoVJVr1jZ3aCaBKZjFPTCc7tIrIoIlNzPLOuhLXx8_flnSk1KpKhD41dBDRIvlRlUlNiY73Cha830IK0AOqugtY88JmH_a29hjhdxui69iNhN6pevK0HE5rQJGqqyi6U87anK7Dtzfpj4RYS1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تبلیغات «انقلابی» موساد در فیلترشکن‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/451620" target="_blank">📅 15:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451619">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIi4-WwgjGnnbP356YitOObm2LMpUl7jqtonD2saOjdF2ArGIyPBQhSjtLAKbObNcR6dem5HKPDyRm3lL7OK5lusPB7iN3NG0o66TrlPixBg2k63iQKmdUo1Jt4j9lHJJ5MJD-QoiKH5fL0WR4pwsnUFqLZ4TZ3fD-TjwY_5FfPHmGvFyPdwWiD2BiH0rApisTDurNPOdYORWDZX0qyE7Vxa7gpGLMg8xSpGo02wcBZC_eRohXjN5cxQTgZO__g0_E3_I6AnVxcRmXo48LSatdhtkD33kgUgzqomU7LeG5HVVa6edjBwSr0ILODsYpfHMLXqsEikuOfp00ASzIDV8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رژیم صهیونیستی: شهردار نیویورک باید بازداشت شود
🔹
سفیر رژیم صهیونیستی در آمریکا در واکنش به صحبت‌های شهردار نیویورک، دربارۀ احتمال بازداشت نتانیاهو در صورت سفر به این شهر گفت: کسی که باید بازداشت شود نخست‌وزیر ما نیست؛ شما هستید، آقای ممدانی. او همان شهرداری است که کمیسیونرش تلاش کرد با نماینده ایران در سازمان ملل دیدار کند.
🔹
نتانیاهو به نیویورک خواهد آمد و شما هیچ کاری نمی‌توانید برای متوقف کردن او انجام دهید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/451619" target="_blank">📅 15:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451618">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8a3eeac6.mp4?token=DgwflQSrV5Sr6Bqos8kK25QyzBnLJ4xf8kM1JkHPPxIKUHwd2xaoytr1HPr9_6ppbnuQYQiaA8Mwk1sS5ArNzoyc-NnR1JQkEXFR9-GUfxAQ4La2eLn0DpOJLSaHyBwFvAIoD9xng8riSbjpT579jQ-pX-JVR8ERgcn7IaTTvlQtF8szKIKUrzCVgEa0E-Z-NW3Kgg7_7D6bLBGlBZSm4uaGsuPIzyr25AK8HIMZM3vnB4W6B-8eIKdVZgFKWoAUHI-zPfOXeAl1zrIzJs1YcB2Vx1AKu0rhPrJw7kk4Iyk2nMTyFrttX07RevRg8ar0j7GFpJTzvuaTXtQRfAGEoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8a3eeac6.mp4?token=DgwflQSrV5Sr6Bqos8kK25QyzBnLJ4xf8kM1JkHPPxIKUHwd2xaoytr1HPr9_6ppbnuQYQiaA8Mwk1sS5ArNzoyc-NnR1JQkEXFR9-GUfxAQ4La2eLn0DpOJLSaHyBwFvAIoD9xng8riSbjpT579jQ-pX-JVR8ERgcn7IaTTvlQtF8szKIKUrzCVgEa0E-Z-NW3Kgg7_7D6bLBGlBZSm4uaGsuPIzyr25AK8HIMZM3vnB4W6B-8eIKdVZgFKWoAUHI-zPfOXeAl1zrIzJs1YcB2Vx1AKu0rhPrJw7kk4Iyk2nMTyFrttX07RevRg8ar0j7GFpJTzvuaTXtQRfAGEoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آورده‌ای نواده به قربانگاه...
🔹
نمای معنوی و باشکوهی از حضور دختران خردسال در جوار مزار شهید زهرا محمدی گلپایگانی، نوۀ رهبر شهید انقلاب در رواق دارالذکر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/451618" target="_blank">📅 15:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451616">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d75d3fdc03.mp4?token=jbET60bYjTwfYHwQuYDs2WU1nbMdmSDbEzBqPQDQzV7AVlrikCW6og2x4sWCYeWtjiyDSx3S_YjogzUTZZ0sYCaSrvxnxHOEHTFQEGkVxBmO6exGmGq9C_uB4WNksrmS9isZppv5qHN9XrASHtEOQsYmaFWxf7E1uvifP9Xi8B7oRVmQQNrYNHk7CoMiMnSd678OiyjOrDLG3v64FYonEWLuXK6VXnhP5-HiI7Brw7fzA0A5WLpWE_DjES1o_EFFUCB2968g6cIEOAJPb_tyZm6U_mGJdlGfqiImPpg69VPsB5hi4w3fUgY88tMYrnZmfzoF4zlM_B1IJ-QoU_2mlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d75d3fdc03.mp4?token=jbET60bYjTwfYHwQuYDs2WU1nbMdmSDbEzBqPQDQzV7AVlrikCW6og2x4sWCYeWtjiyDSx3S_YjogzUTZZ0sYCaSrvxnxHOEHTFQEGkVxBmO6exGmGq9C_uB4WNksrmS9isZppv5qHN9XrASHtEOQsYmaFWxf7E1uvifP9Xi8B7oRVmQQNrYNHk7CoMiMnSd678OiyjOrDLG3v64FYonEWLuXK6VXnhP5-HiI7Brw7fzA0A5WLpWE_DjES1o_EFFUCB2968g6cIEOAJPb_tyZm6U_mGJdlGfqiImPpg69VPsB5hi4w3fUgY88tMYrnZmfzoF4zlM_B1IJ-QoU_2mlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیاتی از آخرین حملۀ آمریکا به برج مراقبت دریایی چابهار  @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/451616" target="_blank">📅 15:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451615">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eaddca6c2.mp4?token=PFwHLBMOFgVD79t__uQCcOX7se4eIhk7TcrDKPttYZ75JvQSnG1a8Jwqbf6GXsOFvExUo18HRjUSkCT1tly7ThJ-NvCbIxC2lek7nwbRItF-bQd40DAFTJXavNWYI7SdHE9-SvWei3WMHlb0N_C1Txle7b8tqRHutIOn4BAdD3JeYPIsSv5LG_WUl8eaDk7_4VfDAOoTthCXYui958iTBqOBZPI78mXXREgGB_I6llMHYXLX5N5kmS_CwZgXAUWcX2qtW2at70KH0RWaByYJa0uqiTF7bkieh1wU7SXI2Q6xjWsZHSfkme0G6vIrFcg-Lf9GNJbWknIpcJ1u1WB7nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eaddca6c2.mp4?token=PFwHLBMOFgVD79t__uQCcOX7se4eIhk7TcrDKPttYZ75JvQSnG1a8Jwqbf6GXsOFvExUo18HRjUSkCT1tly7ThJ-NvCbIxC2lek7nwbRItF-bQd40DAFTJXavNWYI7SdHE9-SvWei3WMHlb0N_C1Txle7b8tqRHutIOn4BAdD3JeYPIsSv5LG_WUl8eaDk7_4VfDAOoTthCXYui958iTBqOBZPI78mXXREgGB_I6llMHYXLX5N5kmS_CwZgXAUWcX2qtW2at70KH0RWaByYJa0uqiTF7bkieh1wU7SXI2Q6xjWsZHSfkme0G6vIrFcg-Lf9GNJbWknIpcJ1u1WB7nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: اسکلهٔ پشتیبانی سوخت ناوگان آمریکا، محل تجمع پرنده‌های جنگی، مرکز داده‌های اطلاعاتی و یک مرکز سیگنالی و مخابراتی آمریکا درهم کوبیده شد
🔹
روابط‌عمومی سپاه پاسداران انقلاب اسلامی: مردم قهرمان و با ایمان ایران! دریادلان غیور نیروی دریایی سپاه در امتداد…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/451615" target="_blank">📅 15:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451614">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فوت کودک ۳ ساله بر اثر حملهٔ سگ‌های ول‌گرد
🔹
دادگستری کردستان: درپی فوت یک کودک ۳ ساله به‌دلیل حملهٔ سگ‌های ول‌گرد در امروز، ۲ نفر از مدیران شهرداری سندج دستگیر و علیه مسببان این حادثه اعلام جرم شد.
🔹
سایر عوامل دخیل در این حادثه که مرتکب قصور و ترک فعل شده‌اند، شناسایی و با آنها برخورد خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/451614" target="_blank">📅 15:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451613">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad19ca0b5.mp4?token=moafXhRF96IcftfdcEWdnteoaz8hkcNIYZCmFAKgsnHGtjzJU6j2qtUTdSxYC2VCuLFDijEtJm9eM8zpvuavUH1bhnxTi-CCel3HlTCDrteYbGxIZegX8pS4E4vS30B9a4ehLIVkyQ6Yjnh-xxFBQEo57iOyKbSaUuiHvUyEWYFln9YO4x6ZmWNm5UTK0fQswTt4dk-0nvwfAEHBOGrgq8rOivTwv5bEpCjgh0DYvXj-RNjg-KNf37W55GWL9i1aolAmsZdE2gqGfVquVcEgKXdSi-Va7JySyu4-jFUeas3-CjazwCWHQly73XvIkuyzGjvqassrGSeTu0fGWvrzKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad19ca0b5.mp4?token=moafXhRF96IcftfdcEWdnteoaz8hkcNIYZCmFAKgsnHGtjzJU6j2qtUTdSxYC2VCuLFDijEtJm9eM8zpvuavUH1bhnxTi-CCel3HlTCDrteYbGxIZegX8pS4E4vS30B9a4ehLIVkyQ6Yjnh-xxFBQEo57iOyKbSaUuiHvUyEWYFln9YO4x6ZmWNm5UTK0fQswTt4dk-0nvwfAEHBOGrgq8rOivTwv5bEpCjgh0DYvXj-RNjg-KNf37W55GWL9i1aolAmsZdE2gqGfVquVcEgKXdSi-Va7JySyu4-jFUeas3-CjazwCWHQly73XvIkuyzGjvqassrGSeTu0fGWvrzKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ویدیویی از محل منهدم‌شدۀ حضور نظامیان ارتش آمریکا در پایگاه الرکبان اردن
@Farspolitics</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/451613" target="_blank">📅 15:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451612">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILaNge5tPuIqysTb5BBZxQp_9XDtXTsA9BeP5V6I8GdQwXIZM4r3xwy6jgZJ-5IwO2ZzMUl80vq4kaiQ9V_2dF4Z6wz1Kw7kHwsHkeyDqeARon23Zz5R8XXNqKe-anNuEl6vp4pfw8uyLol7oG24T2K9Za4d-1eQ6cc3Xh_PX6-djsybP0IWSBRh4GNWp4YjN9JTvveSdpK9bf3A4mvLftcgnXRRNvKT_o5tPGbrBxHqsjnYXbOMznqA_JdOoQLsSYe9BTfvn9lvp9dtvaBRL6tRZyoF7OOogWxx16TbZOOj1CjhFDTYCorsdh89B06JwF1FfaTQPDCLRebqHKv9IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت رفاه اجتماعی: یارانهٔ تیرماه دهک‌های اول تا سوم واریز شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/451612" target="_blank">📅 15:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451611">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
نیویورک‌تایمز: در حملات چندبارهٔ ایران به پایگاه هوایی موفق اردن دست‌کم ۲۴ نیروی نظامی آمریکایی مجروح‌ شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451611" target="_blank">📅 14:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451610">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaEDRpyhnItcaxii_RpOv5YtUL4lUPXOcJlp7mXC_K_xb9X4WJ03xhRmSHpMwkAFb4ZOoMOMXDapgRTnvMXrO_H3BuSh-zkcy6YIZR2jBRsOHatCmvdErg2Q9z1A-atfH_lj72Sd524fKNVseM1NZ8lt6w5HpjysNZmDOlcKb3ef2vAfK6OYP-iKYN3aYnooTGCwwSP532YfxlO_MhM7f3THQ7PvIUsIU9EUno8G5kY3cDfAIE5kR_LJ5jxxycywvwhh1jJpYIfBS-0SxcwC30OyUMfDcSmKsa2y-pFAgbkWeeJ7cGMWOuIakNTFKQLtEaSh3tR8FW0ElmTnmrjWuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ سردار قاآنی: رژیم صهیونیستی باید بپذیرد که با وجود همۀ جنایت‌‌ها نتوانسته مقاومت را متوقف کند
🔹
پیام سردار قاآنی درپی انتخاب خلیل الحیه به‌عنوان رئیس دفتر سیاسی حماس: عرض تبریک انتخاب دکتر خلیل الحیه به عنوان رئیس دفتر سیاسی حماس، باید این انتخاب را به شخصیت‌های…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/451610" target="_blank">📅 14:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451609">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEzzBWdGcWkq1CDf1JCLkFPGjSQUi2Xn3ydwONZIzDE5uMPuxls445TRzSNotRuhBc0FTwLGbnMLV-14pdZCZ2BqnBIerOq5NUS1MvW8K8ow0cOeaoqK6njMOSpn5QEBsTgHGIM_Kk2aZuB5cWj7Yl2LHE-JCvS1ZmVrMGC5gRoDS7jnQbq16Qn7SnvV6YD4p5g4IbNyAKpQQaivQnAVQ2FSwF_ZqQnyhBabYz1gvOcPbBrAKjOClok88tc8WEAGFfSvezZ6nkec33NjKMPLeWeOIxV_tVKdMG2Bisi1NpoD87bOBXGpU1CZDVMWNkkNpwCk4ZnILPyA2alrSQBpCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسال‌کنندهٔ فیلم پرتاب موشک به شبکهٔ معاند دستگیر شد
🔹
سپاه ابهر: فردی که با فیلم‌برداری از لحظهٔ پرتاب موشک در آسمان و ارسال آن به شبکهٔ معاند «ایران اینترنشنال» اقدام به همکاری با جریان‌های ضدامنیتی کرده بود، توسط سازمان اطلاعات سپاه ابهر زنجان دستگیر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/451609" target="_blank">📅 14:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451608">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f95c26614d.mp4?token=sR3B9uwtMDvzrgpq_jL1kSqo4unJUbii3cHwmSrg7kCyycS3AwgQfiEVYW9p2hGgH2Z7eGCTCIqU8FTZsMDeh_xbYuUThULvmY-OnzwuJN-3p3aJQg0W8EQL5VLlv01JuVewoaK8jMJ1fYZMWNguuOInopaF5onMANd66f2GPBzYIixP2KOBjFiYq8gVOKoMFG8Uskn5exsbh2De7BGgj9nAJLhpIDGWksvyvsy4yyl05tKe-QMQ22aggtPQXbzCNzsvK3M2YsAKHOULl3AFeuMAjXk1wbViq_j0m-CrTqTw96ssw_DiwhQGGlPKAwJmpEpneNPs8LwXZZv8Jv0iWyNJWgbmSmixg9X5KcSArBl40e_RVUlnvhDDTQmNGPTwDdwlW8ahv0asxoPSl71NXer_Aq03j3xmTBQogE5fKOFGCdH9ENiKPbB-rQ18SyZUuz-nHfzuI6M5teqR54C-7TEv4IvoPaVFRAOIJxiJ9_S9UuhdZrpmevO8Vb7uV6iT0nppFF982Pp6lJyg6N98NOgJVM6gZWsPhLio0KH3fxFu49EAJKEATRtWvS8YxjluXeDQts3X0pEShRg7JIJOyf8uIAXRRnIlHT6uxki53wusB2mkSeSOnawD-GJdsfwnmuXNZMuWnPkGvf6PkK9uqYPUT4ldCLUWUSODJrO_BIU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f95c26614d.mp4?token=sR3B9uwtMDvzrgpq_jL1kSqo4unJUbii3cHwmSrg7kCyycS3AwgQfiEVYW9p2hGgH2Z7eGCTCIqU8FTZsMDeh_xbYuUThULvmY-OnzwuJN-3p3aJQg0W8EQL5VLlv01JuVewoaK8jMJ1fYZMWNguuOInopaF5onMANd66f2GPBzYIixP2KOBjFiYq8gVOKoMFG8Uskn5exsbh2De7BGgj9nAJLhpIDGWksvyvsy4yyl05tKe-QMQ22aggtPQXbzCNzsvK3M2YsAKHOULl3AFeuMAjXk1wbViq_j0m-CrTqTw96ssw_DiwhQGGlPKAwJmpEpneNPs8LwXZZv8Jv0iWyNJWgbmSmixg9X5KcSArBl40e_RVUlnvhDDTQmNGPTwDdwlW8ahv0asxoPSl71NXer_Aq03j3xmTBQogE5fKOFGCdH9ENiKPbB-rQ18SyZUuz-nHfzuI6M5teqR54C-7TEv4IvoPaVFRAOIJxiJ9_S9UuhdZrpmevO8Vb7uV6iT0nppFF982Pp6lJyg6N98NOgJVM6gZWsPhLio0KH3fxFu49EAJKEATRtWvS8YxjluXeDQts3X0pEShRg7JIJOyf8uIAXRRnIlHT6uxki53wusB2mkSeSOnawD-GJdsfwnmuXNZMuWnPkGvf6PkK9uqYPUT4ldCLUWUSODJrO_BIU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در ۲۴ ساعت گذشته ۴ پایگاه در بحرین، ۵ پایگاه در کویت و ۲ پایگاه در اردن هدف حملات موشکی و پهپادی نیروهای مسلح کشورمان قرار گرفتند
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/451608" target="_blank">📅 14:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451607">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2f647aef9.mp4?token=JQ9H-tAOFF7Ig6i4mM4-Mgahzmf-qrOimvSYiYRpltFnL1-4weeu5CloV7aioAIEOToQlN5FZIkdlDWrobqJn9P9LBkgqA-k28fD9OFLDVr4SRKPqbODoBtNg0MleIQWmG2Y98JQE_5mAWs6saiw12IzS8-HzUulwZNSJEB6E4CzCH4CJkxuU4_vrGS02TRPkdZ5Z-sDLyqx4IngKaUkpo6VJlrPwpDc6cM0iGseNvTOPe3a8Lf7_VprEkiKw8k1Vokp7NO-UglctpL8UoX23Ry6P9UHajr9iDs4sHO6G2YLvSYAIpfLej3phjXyPF3HCE2kEB3YsQwX32UCd8Nuqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2f647aef9.mp4?token=JQ9H-tAOFF7Ig6i4mM4-Mgahzmf-qrOimvSYiYRpltFnL1-4weeu5CloV7aioAIEOToQlN5FZIkdlDWrobqJn9P9LBkgqA-k28fD9OFLDVr4SRKPqbODoBtNg0MleIQWmG2Y98JQE_5mAWs6saiw12IzS8-HzUulwZNSJEB6E4CzCH4CJkxuU4_vrGS02TRPkdZ5Z-sDLyqx4IngKaUkpo6VJlrPwpDc6cM0iGseNvTOPe3a8Lf7_VprEkiKw8k1Vokp7NO-UglctpL8UoX23Ry6P9UHajr9iDs4sHO6G2YLvSYAIpfLej3phjXyPF3HCE2kEB3YsQwX32UCd8Nuqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برافراشته شدن پرچم ایران در بلندترین ارتفاع خلیج فارس
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/451607" target="_blank">📅 14:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451606">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KI7owN-2aQCv8zOVfS3K8Tc6xtpMyxWM-4UYkU0A8lEPQh6qED7PrHdSn0vgWC8wlCH_E--hud9p6E8KfdyN4yxSwpYgBFHC6LCLMZoAul4n0p0z9ityd9tjsGGxvLVEB41E99eNLZ8IxVd6TzUXlCkE2GqzRJ_nEVCUxmUdb1kkTVd5bFhIZvApnkjD-6DROmAERNCSj79UKQPl2NXMxmx5PYC0GenJsfo-UxyLmXvnuYpN79SubRT7nQ17uAeN5W-GeKEfQ8n4Jg2V5-qk9SxOZgL8bNcqUb5unrU3tGO9sFnt_mfCYzuTgHlT6vRWUauGV6RUwu-2JpsGwsQlVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
منابع عربی: یک پهپاد به پایگاه نظامی آمریکایی حریر در اربیل اصابت کرد.  @Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/451606" target="_blank">📅 14:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451605">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac6945763e.mp4?token=WounplrBSfv_01RZ1MrXsHsIoBJbjeNiUJpdK_91GbsICiP7Q0SDK8dyh-8VTFDTdOzpgOgBs88RgWiuvAKvr6DcYP8btSMLxnYmX8O_D1egH26yBbNJ9H4f64gDxKiH1PBXRenfjp__rDNKwJni6xnJe2hEbR7jTwk6IYvb0E5wyuPhI2G5GPSCzdnSSytPjMc1uIuFqE4cXB7Uz6sZ20NxtUQwkiawaaLO_5MyWkYOTEfOtlGSf3FbTTTQc69oAh1Pbr__QJRq8cbpImCe68f79Qnzlma_otUCVPSMWhS4HzSU9sTWnLJGEq7GB-BaKic4rWKg7OO1snSc4FEm5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac6945763e.mp4?token=WounplrBSfv_01RZ1MrXsHsIoBJbjeNiUJpdK_91GbsICiP7Q0SDK8dyh-8VTFDTdOzpgOgBs88RgWiuvAKvr6DcYP8btSMLxnYmX8O_D1egH26yBbNJ9H4f64gDxKiH1PBXRenfjp__rDNKwJni6xnJe2hEbR7jTwk6IYvb0E5wyuPhI2G5GPSCzdnSSytPjMc1uIuFqE4cXB7Uz6sZ20NxtUQwkiawaaLO_5MyWkYOTEfOtlGSf3FbTTTQc69oAh1Pbr__QJRq8cbpImCe68f79Qnzlma_otUCVPSMWhS4HzSU9sTWnLJGEq7GB-BaKic4rWKg7OO1snSc4FEm5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: به وزیر نیرو گفته‌ام، برق دولت را قطع کنید اما برق صنایع را قطع نکنید  @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/451605" target="_blank">📅 14:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451604">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80e57c20be.mp4?token=ABAc7b6D-U4iBWPjXkRtiZ8G_gYJ9P8lubTdn9I_ZpdHAvovwEKj5HDCbrkjKRL_OuY9Bhc5SkmD6RnFqnVT54Pas4beT-2-uVNfjTvR_RqcQvJg7An6MU4THdJ5Yo8DYoRbiSKnaQ3e-2YUthP2c4QhItlCrmvEjBChoFKNp13hn1eRYm0Ny7PJxc9LBC3XUF6uVMsrJtaXvE3tBvXTUZuZOHvcBBcYZMqG0r82dtDxrIXSW2y2LgxGeM8IbhiFkqOywawVpUvL9Aw7uZYWlAqGxbucN0BDTyaJzTMFPAIPnM511B4uwR9ejk3kuiHcRmvJM9yhVVB_ScGmac_KrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80e57c20be.mp4?token=ABAc7b6D-U4iBWPjXkRtiZ8G_gYJ9P8lubTdn9I_ZpdHAvovwEKj5HDCbrkjKRL_OuY9Bhc5SkmD6RnFqnVT54Pas4beT-2-uVNfjTvR_RqcQvJg7An6MU4THdJ5Yo8DYoRbiSKnaQ3e-2YUthP2c4QhItlCrmvEjBChoFKNp13hn1eRYm0Ny7PJxc9LBC3XUF6uVMsrJtaXvE3tBvXTUZuZOHvcBBcYZMqG0r82dtDxrIXSW2y2LgxGeM8IbhiFkqOywawVpUvL9Aw7uZYWlAqGxbucN0BDTyaJzTMFPAIPnM511B4uwR9ejk3kuiHcRmvJM9yhVVB_ScGmac_KrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: به وزیر نیرو گفته‌ام، برق دولت را قطع کنید اما برق صنایع را قطع نکنید
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/451604" target="_blank">📅 14:34 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
