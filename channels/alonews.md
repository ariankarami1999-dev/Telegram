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
<img src="https://cdn4.telesco.pe/file/gXs83xBQpDXPTAqlZDYhWUt60pjHZsJ3-lP-AfDUV1sLWUUTvi5S4xI3MSzmiWmhQx-QDjROtaqChyKSYV55Q37UjIPUfneFozFeX2dYBT26v8cu03LTgnz-8GVCsOmh4x1sKrbAkaiodE9QFDiJGvYYzu8_-z-Dtsngohpf4rAWyM432soQhKaie7WoWGmHxJnJ7cM8kJV2WTyX7DcT7PsPGbZWWjPEqWacLjQwJsH9AF5A_ETaqDDKDAUFZ4eU_6rDNAVhga1E3vmRyQ3Uw2dLqBsgXAgTAdbKn8MZmqG00PuSxKozVhlZT0tlkasbU-hu2pNwimt6meE948vQ8A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 920K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 13:13:50</div>
<hr>

<div class="tg-post" id="msg-133427">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سپاه پاسداران: ما در عملیات امروز از موشک‌های بالستیک مدل قدر، عماد، خیبرشکن، فاتح ۱۱۰ و ذوالفقار استفاده کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/133427" target="_blank">📅 13:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133426">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا:
سطح تهدید دریایی در تنگه هرمز همچنان در بالاترین درجه خطر، یعنی «شدید»، طبقه‌بندی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/133426" target="_blank">📅 12:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133425">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
وزارت حمل و نقل قطر از مالکان و کاربران کشتی‌های دریایی خواست تا اطلاع ثانوی، موقتاً دریانوردی و فعالیت‌های دریایی خود را متوقف کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/133425" target="_blank">📅 12:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133424">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: نتانیاهو در حال بررسی امکان سفر به مراسم تشییع جنازه لیندسی گراهام است.
🔴
در صورتی که این سفر انجام شود، به احتمال زیاد با ترامپ نیز دیدار خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/133424" target="_blank">📅 12:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133422">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
احتمال تحویل ۶ فروند اف-۳۵ ترکیه تا پایان ۲۰۲۶
🔴
آمریکا ۶ فروند F-35A را که پیش از تعلیق مشارکت ترکیه برای این کشور ساخته شده بود، همچنان در انبار نگهداری می‌کند. با پیشرفت مذاکرات واشنگتن-آنکارا برای بازگشت ترکیه به این برنامه، احتمال تحویل این جنگنده‌ها تا پیش از پایان سال ۲۰۲۶ افزایش یافته است.
🔴
ترکیه در سال ۲۰۰۲ با سرمایه‌گذاری ۱.۴ میلیارد دلاری به برنامه F-35 پیوست و قصد خرید ۱۳۰ فروند داشت، اما پس از خرید اس-۴۰۰ از روسیه در سال ۲۰۱۹، مشارکتش در این برنامه به حالت تعلیق درآمد. هیچ مقام رسمی هنوز زمان‌بندی دقیق تحویل را تأیید نکرده است.
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/133422" target="_blank">📅 12:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133421">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سخنگوی دولت عراق: هیچ پایگاه خارجی در عراق وجود ندارد، بلکه مشاوران بین‌المللی در خاک ما حضور دارند که به درخواست دولت است
🔴
خروج آن‌ها هم شامل تحویل پایگاه‌های متعلق به هیچ طرف بین‌المللی‌ای نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/133421" target="_blank">📅 12:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133420">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
امارات: «تهدیدهای موشکی که صبح امروز شناسایی شدند، خارج از مرزهای امارات متحده عربی بوده‌اند.»
🔴
در این بیانیه آمده است: «اوضاع همچنان باثبات است و سامانه‌های ملی در بالاترین سطح آمادگی قرار دارند.»
🔴
پیش‌تر در روز یکشنبه، سازمان ملی مدیریت بحران، حوادث و بلایای امارات (NCEMA) اعلام کرده بود: «سامانه‌های پدافند هوایی هم‌اکنون در حال مقابله با یک تهدید موشکی هستند. لطفاً در محل امن بمانید و هشدارها و به‌روزرسانی‌های منتشرشده در وب‌سایت‌های رسمی را دنبال کنید.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/133420" target="_blank">📅 12:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133419">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
خبرگزاری مهر :  شبکه ارتباطی تو کرمان بر اثر حمله آمریکا دچار اختلال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/133419" target="_blank">📅 12:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133418">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
دیوان امیر قطر: پیکر حمد بن خلیفه آل ثانی پس از اقامه نماز در گورستان لوسیل به خاک سپرده می‌شود.
🔴
از امروز چهار روز عزای عمومی در سراسر قطر اعلام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/133418" target="_blank">📅 12:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133417">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
وزارت بازرگانی آمریکا با ارتقای جایگاه امارات، محدودیت‌های صادرات تجهیزات نظامی، فناوری‌های پیشرفته و صنایع فضایی به این کشور را کاهش داد.
🔴
واشنگتن این تصمیم را قدردانی از همکاری‌های ابوظبی، از جمله در جنگ علیه ایران، عنوان کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/133417" target="_blank">📅 12:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133416">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
فرودگاه سیرجان بعد از چهار ماه تعطیلی دوباره باز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/133416" target="_blank">📅 12:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133415">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
کانالای ایتا: گراهام رو ترور بیولوژیکی کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/133415" target="_blank">📅 12:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133414">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجارهای کنترل‌شده در تبریز به‌دلیل پاکسازی منطقه از مواد منفجره
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/133414" target="_blank">📅 12:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133413">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
خبرگزاری رسمی عمان به نقل از یک منبع امنیتی اعلام کرد: چندین نقطه در استان مسندم هدف حملات پهپادی قرار گرفته است.
🔴
استان مسندم، یک منطقه کوهستانی عمان است که بر تنگه هرمز اشراف دارد و با امارات هم‌مرز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/133413" target="_blank">📅 12:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133412">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وزارت دفاع روسیه اعلام کرد سامانه‌های پدافند هوایی این کشور طی شب گذشته ۳۴۹ پهپاد اوکراینی را بر فراز مناطق مختلف روسیه رهگیری و منهدم کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/133412" target="_blank">📅 11:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133411">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
تصاویر حملات موشکی هوافضای سپاه به پایگاه‌های آمریکا در منطقه منتشر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/133411" target="_blank">📅 11:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133410">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وزارت خارجه هند: در حمله به کشتی کانتینری «جیافاس گلکسی» (GFS Galaxy)  ۱۰ نفر از ۱۱ تبعه هندی حاضر در این کشتی نجات یافته‌اند، اما یک نفر همچنان مفقود است
🔴
سفارت ما در عمان اوضاع را از نزدیک زیر نظر دارد و در عملیات جستوجو و نجات در حال انجام، با مقامات عمانی هماهنگی فعالانه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/133410" target="_blank">📅 11:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133409">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_QR99rBxbqwDNIFVSNJcD5d0J396jmRRdOJcp_pePeEnt_C2WjAYJhRwiMMJtf2VjNOKcQs7Uik5SdyUg5f_lQh9_ATyG0UjdJc2dnodMEH1TlyWo6T-xDmgPKraSMJXzpDJBfhVZNJnN5m_X7NZkMykXJINAFZ6UP1t3W7sNYAxA7iBjJOC5wZQlxlQ0a3A1LXuujhpKFQV5V-5DK-5PjXQd2jFTxxqxvzQU7D8H6NczwrUPS_mykn1QH77aYF8YzikDAF3C5zXa6Am0H8HS6-J4dg6T2Lgp-a8s-oIa5GMWQ46XIaYMw26cEwvhS3D277vcjdBfrr71SVpxda0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: گراهام اولیش بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/133409" target="_blank">📅 11:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133408">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
شریعتمداری: اکنون باید به زیرساخت های اسرائیل حمله کنیم
🔴
باید علاوه بر بحرین و کویت به امارات نیز یورش ببریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/133408" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133407">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFzEWq7LW700rAmQ3fw0PyIisjA5Cz9JiV9EkigVNkwHpExF_VZRn15_bNOwPG9crMb-n3V1M4rmftXovGfFYXWD1Lhqb9zQ7x3g-YBP09gfog-TxyfT5dOsm3crdKdo5FRql0QbFf0g8Sijrmag96_4eeONw2KrEkbvrC7F_DA3lY77Flx3O9LZj1HkrFByLyYtm_lLjC5NOvsvMIFTi00qf54kfsfBbD5VjEYwD9n9z2r92jDRZN3PoaeAFNXQKdxK6VJlgbx1lhQfe5BZxYa3-iAvSIDubVpV4GaCopSn9tFB5hCV-S47SWGByzLxev01w1Fh-7IlRuFrbaDsLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش کنایه‌آمیز مرندی به مرگ گراهام: حیف شد؛ کاش قبل‌از رفتن به جهنم قیمت فردای نفت را می‌دید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/133407" target="_blank">📅 11:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133406">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLWIfygnCaDjazlmSEpzKkniDFEMGt1umPlnWUR3gpdMYu6rlQ3ZDETlraVHqZ4pNQDT_2j2LNIEv2gGpmL7CQ4vC142HEvaPJwPrCXhBB0BjVIBCOxUu6fbi1XG2KuTsQK5QZyqcBpex4KDO0UMy1KY0Hx_hZn_5_K3v4x3Ga7tR9hBQMfN2gYA6EStfRB_sw8Q8G847j4LwPY6Rrg_ke-42t7aedlVFH8gIisuj2Zn7yna2WnwIkFew8RBtFfwkbhjdx6PmUi_McR7V-O8kjaGh_Wihwm7lk-E47jr45hOtprZzKSXlZ9CBVyEB_vCIu5bmD1WO4QZxCmUJ90h_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان سعودی با محکومیت شدید حملات ایران به کویت، بحرین، قطر، امارات، عمان و اردن، تهران را به نقض قوانین بین‌المللی، تضعیف امنیت منطقه و تهدید آزادی کشتیرانی متهم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/133406" target="_blank">📅 11:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133405">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
مقاومت عراق: سلاح ما قابل معامله نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/133405" target="_blank">📅 11:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133404">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd35346900.mp4?token=N2LqiwAK8DMb_l-lYA_z4plhh-9MbI8Md8_vV2bMN8q25OMFCWL6DSIuAHOUY5Pvkj_m9NPSsAks4Vy0sz_cCG4Qi94VqTPJZdHwHHNTBjzAicjb3yVeInoUYEztellbSLhsz4Yay7bS0oWohhHtiIo6LTUzUxmxpd-_nGQcF7C01dIUzFBcT1AI0R3-IapjCo2nnYwVxvMn77ED3A2LXtgS_Bkuj7iP_SXcW-Q5i6UR548hxtb3kX7YcgX10gnabxP526hBLv_w0FNDE79EDVmsl7oCooo7r0djY24qFOzKCophZqr8I3OTYBVLffsMZoedqsH0q69aaMBJZajwTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd35346900.mp4?token=N2LqiwAK8DMb_l-lYA_z4plhh-9MbI8Md8_vV2bMN8q25OMFCWL6DSIuAHOUY5Pvkj_m9NPSsAks4Vy0sz_cCG4Qi94VqTPJZdHwHHNTBjzAicjb3yVeInoUYEztellbSLhsz4Yay7bS0oWohhHtiIo6LTUzUxmxpd-_nGQcF7C01dIUzFBcT1AI0R3-IapjCo2nnYwVxvMn77ED3A2LXtgS_Bkuj7iP_SXcW-Q5i6UR548hxtb3kX7YcgX10gnabxP526hBLv_w0FNDE79EDVmsl7oCooo7r0djY24qFOzKCophZqr8I3OTYBVLffsMZoedqsH0q69aaMBJZajwTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه اعلام مرگ لیندسی گراهام در شبکه CNN: "خبری به سی‌ان‌ان رسیده است، خبری که هیچ‌کس انتظار شنیدن آن را نداشت… لیندسی گراهام درگذشته است."
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/133404" target="_blank">📅 11:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133403">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zvcy5cu8Vsexumfm327a5XGZR6E6tAwBCsyjihQNSJ_2cP4R6d_RP4yY8DOtHkOEokkYxCwF9Lu054YA9GWixU7gKwNZCu7TwUfqhYZIOETb_CU-9LCV69U0b44N9qzS7bDeXzd8Szc_ozEqklbHwKmFAs5ihr3krNWH5bbKIiknH2AxH86J0L7LDavTK03UGmcPEvZbEF0vMDdGtHgeMs84QdboFUgz-Z8Y1gwmS4n6nSK6zvIKu5NZRQsUb4ibliZKZVBvtw67QTAcnqST3_bDpQ2RgoNLjAyqLosnL6Dgw69KFws9-bJo-HQoGzIeBEBlmM7uicRTFP4CcC3EZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو: اسرائیل و آمریکا دوستی بزرگتر از گراهام نداشتند
🔴
نتانیاهو با ابراز اندوه عمیق، سناتور لیندزی گراهام را دوستی عزیز برای خود و اسرائیل خواند و گفت در آخرین دیدارشان به او گفته است: «ما دوستی بهتر از لیندزی نداریم.» او گراهام را کسی دانست که امنیت اسرائیل و آمریکا را جدایی‌ناپذیر می‌دانست و تأکید کرد اسرائیل یکی از بزرگترین دوستانش، آمریکا یک میهن‌پرست بزرگ، و خودش یک دوست عزیز را از دست داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/133403" target="_blank">📅 11:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133402">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
یک منبع امنیتی اعلام کرد «چندین نقطه در استان مسندم عمان هدف حملات پهپادی قرار گرفته است.»
🔴
استان مسندم، یک منطقه کوهستانی عمان است که بر تنگه هرمز اشراف دارد و با امارات متحده عربی هم‌مرز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/133402" target="_blank">📅 11:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133401">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080aef9062.mp4?token=e7dfwcbeb_Y8qTyYDV110D6b7wDshw6VEVkXtT4WNC7vxL_hHoyMezqnq2nTFVck6kN1_Iso_xlISW8a-Q0-UoIwrb3x8-Bz87fXBk17nDc95EDsD15ETn2cwFswDUwmTl9PJ159kENmSYPGOkGA9FlDgd4zVouH8eQXxewTJ-tUtPEW1rUU5c-jp9oOVdp2NGHBBE_Wd6BAGc61quzuZPR4IjhxZcEjB8vG1aQIW2UstQMnFWYmqSARSUIUsey1NZUjhlxvoosmYi6mWMYQIzZJK_vG2lfpSPZU4UBElqiUJA9Z5Uk3HQumiXFkt_se2WotZ5lnUGKvo0I1xx0Mwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080aef9062.mp4?token=e7dfwcbeb_Y8qTyYDV110D6b7wDshw6VEVkXtT4WNC7vxL_hHoyMezqnq2nTFVck6kN1_Iso_xlISW8a-Q0-UoIwrb3x8-Bz87fXBk17nDc95EDsD15ETn2cwFswDUwmTl9PJ159kENmSYPGOkGA9FlDgd4zVouH8eQXxewTJ-tUtPEW1rUU5c-jp9oOVdp2NGHBBE_Wd6BAGc61quzuZPR4IjhxZcEjB8vG1aQIW2UstQMnFWYmqSARSUIUsey1NZUjhlxvoosmYi6mWMYQIzZJK_vG2lfpSPZU4UBElqiUJA9Z5Uk3HQumiXFkt_se2WotZ5lnUGKvo0I1xx0Mwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدا سیما : «به درک واصل شدن لیندسی گراهام را به ملت ایران شادباش می گویم»
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/133401" target="_blank">📅 11:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133400">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lj1YFv_sA5jhHBYi4_02e_Dq7O6pcMSV_c9Jb84PopwBKkBI_lysU2uOnKYsHrmAjqb2OZc6LlPigsTvVRzY1fJbDrxJ2r-oS_JdOBfVq5Onf-BoVKMtthpKLJMqxdK25eWquO8JpknFd97FM5kfyGlTjJLcWp3jgz_CGI13bGFlU3IQ7fadciK6nFQYFHUKeqNSaMzyr4UxsKoW0GdALMr5pMLG4mTRQsjSbdGjPl0G6Xw8Q-Mfuo6LeWCEW150buqKZv9dB3_iWZvKXF0rfDWxVFElh49-17F1LLHXn1SGL6recKnAqTn3SedXuBwf6NP7FQt5KAvBZ5KHwEyRAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لورا لومر خبرنگار نزدیک به ترامپ با بازنشر تصویر توییت سناتور گراهام که اشاره به حذف فیزیکی وی توسط سپاه پاسداران داشت خواستار تحقیقات در مورد مرگ ناگهانی این سناتور جمهوری خواه شد.
🔴
لومر نوشته سناتور گراهام چند روز در منطقه جنگی روسیه و اوکراین حضور داشته و کمتر از یک روز پس از بازگشت از سفر به آمریکا، خبر مرگ وی اعلام شده و احتمال مسمومیت (ترور بایولوژیک) باید بررسی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/133400" target="_blank">📅 10:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133399">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALWU_7ABQA3XuSeIS6hJ_qfi5cVsGDb5baBxGeeqPKuYFVj9bKzsYHkvgIRS4WSOq6NCS4dxCLhXgqoyMO72aCnBC-mHUqDdQC7nR5_X20htMZUi9_SCsd6Taplt7qBCpvir0fZmZBE2l5ShSA7XuxoPSfpTYEPF2CvE-Ua7mMLuJ9gGMCxwwzq5Lf7Yk8oUO8K353l8G67g47ZfFMibBwxqhhqPAundRs05kafo2G5gUDzn-KXuuLfAvQEmdwQQEmrh_NFGaUWwC8Yh18-LY1EMH6yZaezAR-yrCJKD-NQUE2UTOlxKewSZue_ArOOLNxBMKTaCzcvcbB2ytqGbPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: سناتور لیندسی گراهام، یکی از بزرگترین افراد و سناتورهایی که تا به حال شناخته‌ام، درگذشت! او همیشه در حال کار بود و یک میهن‌پرست واقعی آمریکایی بود.
🔴
جای خالی لیندسی بسیار احساس خواهد شد!!! جزئیات و ترتیبات بعدی. خیلی غم‌انگیز است! رئیس جمهور دونالد جی. ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133399" target="_blank">📅 10:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133398">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
منابع خبری از شنیده‌شدن صدای انفجارهای شدید در نزدیکی فرودگاه بحرین خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/133398" target="_blank">📅 10:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133397">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07524e3d2.mp4?token=vEGKcFta4J5jXwWALS00Z8NGC9ST7QSdURtZmc_sAkzQeE_kDcLm4e2RwWCVDQu-9wnrpBDlMjeGaohz0AoXl3IhxcW3t1eD08jfeLr66LDci2YeSMkx-6L-LQ3Tgz6WoHKVmafpwRj4POww-olNHzrzqur8dgzAjKY0RjAhbXtdQGpANE0jp-UHJIZXsd7oXv8XcO-p4t6-t2sHnBb2Ra8Lg_0maK1vkxeGFL14JhgGWHn3Md-EH9HLwRJ9zkIypUXMltP3AybfzILxRIkNuR-7dQ3wkVAbU9Cf5A4JHp31maIKgEIPjQU2vx0wp0iC5cVm0MZ_4hKqZYPa9-nyjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07524e3d2.mp4?token=vEGKcFta4J5jXwWALS00Z8NGC9ST7QSdURtZmc_sAkzQeE_kDcLm4e2RwWCVDQu-9wnrpBDlMjeGaohz0AoXl3IhxcW3t1eD08jfeLr66LDci2YeSMkx-6L-LQ3Tgz6WoHKVmafpwRj4POww-olNHzrzqur8dgzAjKY0RjAhbXtdQGpANE0jp-UHJIZXsd7oXv8XcO-p4t6-t2sHnBb2Ra8Lg_0maK1vkxeGFL14JhgGWHn3Md-EH9HLwRJ9zkIypUXMltP3AybfzILxRIkNuR-7dQ3wkVAbU9Cf5A4JHp31maIKgEIPjQU2vx0wp0iC5cVm0MZ_4hKqZYPa9-nyjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور لیندسی گراهام در حالی ساعاتی قبل از دنیا رفت که دو روز قبل در اوکراین با زلنسکی، رئیس جمهور اوکراین دیدار کرده بود. او همچنین قرار بود تحریم‌های جدیدی را علیه روسیه به تصویب برساند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/133397" target="_blank">📅 10:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133396">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
بمباران توپخانه‌ای نیروهای دفاعی اسرائیل  علیه شهر کفر تبنیت، واقع در جنوب شرقی شهر نابتيه، لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/133396" target="_blank">📅 10:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133395">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEiMvKWIGpraMo2uz_Y9t5ENlLKd9L2JPbCiFBUarSEUoV4Xo51hxKllBLkjN2cBxxR1IvmSaqeNlRJ2muaGVZGwqzfZKk9A7w9r4XYkDqoMjcX5vxgvU1T810Xt1Rjd0kBofmYT7lVDrwMEDPZ-ERULwoyeB7SM7MulEfya6o5A0fDMAoBjljvRsuW7fKV-PeXCbyv7ZrNCZmohHRTCbcuTJgCv0iqkjebZu_mLT1aQRJUa7NVaC7ZJOJVCaI_0iJmL4GfoerFVRSbov3EP4LDjGrrzNXObuoOoPHfz6uXZjtgXKnwwUgtK587cLUPsUZrbo-bTIrpMnmyoyDLDUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بنت، نخست‌وزیر اسبق رژیم اسرائیل: قلبم از شنیدن خبر مرگ دوستم شکست؛ اسرائیل یکی از بزرگترین دوستانش را از دست داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/133395" target="_blank">📅 10:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133394">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
هم اکنون وضعیت در بحرین عادی است. به احتمال زیاد، پهپادها در خارج از فضای هوایی بحرین توسط هواپیماهای بحرینی و آمریکایی رهگیری شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/133394" target="_blank">📅 10:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133393">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpdZZRmGUPF07v-nWWlFTRZAvTsdOGH7vbse9q4dXECJzmMXFsmt4WN_2j78Vk4AfD2xy7rxb0w9dnoeIiVQ9XyvEjHGGchtho1TdX7Cjoe6Lc3RHZlbo_I_kIT_ib-WTFoAFaYxs2psNjFZCwYdkDGxE2NmRd70Xch6tkJaASQZxVrXtEQeZrQbazhLtYsfocU6vKWgixrqLYkqbAEC2bHg5UDNqM066JJk0SPLhrHAEHOeMv6wc_mT58mQ0VUgNvwB7GQM6nVF7MQOXkhdDlLlN9isLPkCjgrZNkLLdC-hiCNXR2u5L_ElbZaZtVJ8M4b5ArHv_4EU1K8aPB1MwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت کشور قطر اعلام کرد که سه نفر، از جمله یک کودک، بر اثر برخورد بقایای رهگیری موشک‌ها و پهپادهای ایرانی ، مجروح شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/133393" target="_blank">📅 10:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133392">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وال‌استریت ژورنال به نقل از مقام‌های آمریکایی گزارش داد اطلاعات اسرائیل نسبت به احتمال وجود طرحی از سوی ایران برای ترور دونالد ترامپ هشدار داده بود.
🔴
با این حال، این مقام‌ها تأکید کرده‌اند که تهدید ادعایی در ارزیابی آمریکا «کاملاً معتبر» تلقی نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/133392" target="_blank">📅 10:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133391">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAvPg8_Rak1Bj1bC4Qox6cFCrOjGQs42ADY7H_n3b_oY0eqk8_iU-sdzXEgWPh0h9XAsLzSluG4tOpm_ih4LQXDk5GMci6MoUIzfD5q5C_sL9RM_oAyBfRhvbkdfkr17ODHi0PH5lnHhvObk6r0USAPXr-W4YJBoAq6_sRvU0SY2nZWk0_T5xog80iaFZTMQK66tuMwuyu0XsGlp_IEYkHnyQ40g7OP0ZMM3OA3_k0CBQDY2yjw-aMH9RW_qLauKyWXTGrU0GMCxMAjGps2ZJnMpRnoB4_nlYhkkx6NBnBuV9admN-cUUvHhMz4dClj1c69rtdGHDX7QP07_lv83jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بن‌گویر، وزیر تندروی اسرائیلی: اسرائیل یکی از بزرگترین دوستانش را از دست داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/133391" target="_blank">📅 10:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133390">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
برخی رسانه‌ها از شنیده شدن صدای انفجار در کویت و بحرین خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/133390" target="_blank">📅 10:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133389">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوری / مرگ ناگهانی سناتور جمهوری خواه
🔴
دفتر لیندسی گراهام، سناتور جمهوری‌خواه و جنگ‌طلب آمریکایی اعلام کرد که او بر اثر یک «بیماری ناگهانی» مُرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/133389" target="_blank">📅 10:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133388">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
استانداری کرمان: هدف قرار گرفتن یک دکل ارتباطی در ارتفاعات جنوب استان در حمله آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/133388" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133387">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpodBFVtdKcyk6fkzg_dgxH4Be5LB1TFvQLoc-guigSzUcfzCGNXUQw4VFM0xKE5fnzxtZZxyA2_b44PQAwjcfya1PE0JgmBSUy_B4PPo1chZHMzwTfTgqQJ-5xyhmgSupWFTO3X9h4ETh2bO5nM_Mw1ht75i_GSC_eEg6yrqQnKsYffFX3WjGXJ1zzfD24cFuPuOg5nFfxxeoxAPvjJvBzLz4hCrUclYX9Skl7eqV7Cxd35xtGce_NMLEh8u8J3JpUVBMzAa9wx1owxZRWepLhkNK2T_JXkfwjC6CEu5DaRRFPRZn-u9IV2TPKR_S90WQgtQ8i8X-KdYDFYvOo-UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اردن مدعی شد: سه موشک ایرانی بدون برجا گذاشتن خسارت جانی در کشور سقوط کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/133387" target="_blank">📅 10:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133386">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری/ وزارت کشور بحرین از فعال شدن آژیر های خطر در این کشور خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/133386" target="_blank">📅 10:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133385">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7e8ac85b.mp4?token=pJnx-y0f3mL0ip5RExcGv4p8_1gVWkpSF0aY1XQFnogdToLBGF1-D3eY1aSBmnDXbhK67gxQms6BisjVzKGBOUUXLEa_tQG6Lm1-4ovqWGROA3qN4fyHaUuhUOKuab5Sg2rI8Luw-CLGeFPEb0-BJoBhJrSEtGSfToF-uHxg7thP_bdM_YnjyszRlOo5_QjGORe6ortIpi5Kj5eqHszfz2MDELwPWpaGQrOywYZTnz7cKNYOzUncV-6Iy36d0_GzuDtt7u78UK3nJvbZGJ8bmSsNXBwnJDCYCiYvt-2Xz50Ta7_FgJQU-o44Le1PQ_KmY1YsVgsOJQ_iBtjKgbfuuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7e8ac85b.mp4?token=pJnx-y0f3mL0ip5RExcGv4p8_1gVWkpSF0aY1XQFnogdToLBGF1-D3eY1aSBmnDXbhK67gxQms6BisjVzKGBOUUXLEa_tQG6Lm1-4ovqWGROA3qN4fyHaUuhUOKuab5Sg2rI8Luw-CLGeFPEb0-BJoBhJrSEtGSfToF-uHxg7thP_bdM_YnjyszRlOo5_QjGORe6ortIpi5Kj5eqHszfz2MDELwPWpaGQrOywYZTnz7cKNYOzUncV-6Iy36d0_GzuDtt7u78UK3nJvbZGJ8bmSsNXBwnJDCYCiYvt-2Xz50Ta7_FgJQU-o44Le1PQ_KmY1YsVgsOJQ_iBtjKgbfuuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور لیندسی سناتور گراهام، مصاحبه با فاکس نیوز در سال ۲۰۱۸ میلادی:
🔴
«قصد دارم آزمایش DNA بدهم ... احتمالاً در نتیجه تست ایرانی باشم و این وحشتناک است!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/133385" target="_blank">📅 10:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133384">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
خبرگزاری عمان: یک منبع امنیتی اعلام کرد که مناطق واقع در استان مسندم کشور عمان، مورد حمله پهپادها قرار گرفته است.
🔴
دولت عمان این حمله را محکوم کرد و اعلام کرد که تمام اقدامات لازم را برای حفاظت از کشور و ساکنان آن انجام می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/133384" target="_blank">📅 09:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133383">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
شیخ حمد بن خلیفه آل ثانی، حاکم سابق قطر، در سن 74 سالگی به دلیل مشکلات قلبی(احتمالا ترس از صدای موشک های ایران) درگذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/133383" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133382">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRJx8xJdTibMRsmJIZguQmmi-iNz6xawbefwjn5Nao8gPkYTlmf2-MKVes58bK6XEsAEOEE3JPNH7P1pD4rcA6gcm4F-_KvmK1Rnd3t-2HPQx8C7zrlPcOYUN7Zv03rMM3W55THPE3x-b7gneOvHcN961N2cHlDW9NRAuxv580rvXwf4IM_6Rkl998jKgTAsU5RG58_tbblUK9Pc4MME8yTJbpPfd8AvfTOrmHBKEOWPsEpDtVy_8zxmTVz7umz2DsKnXWQp9M_T9PcIk-CboiTWq721uU4r95S6X1uDz123HmbAJIPuXJTh7cf32fbv2SdVF48Ldtm-KuPlaoGCIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / مرگ ناگهانی سناتور جمهوری خواه
🔴
دفتر لیندسی گراهام، سناتور جمهوری‌خواه و جنگ‌طلب آمریکایی اعلام کرد که او بر اثر یک «بیماری ناگهانی» مُرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/133382" target="_blank">📅 09:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133381">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFjsqenhNw2MVxdUN7WhuMjve7LiSyrjeQiNHqLOa7DWKIrVgq45twaKa1x1nTzlmtblypnI5Uco3NpDZEABybGpKlylapKJji2Anvoo9grOQGBUvI7peQjMUTSJfda3NSkQK3M-1VkbVRsl1bqgUzAlhSTL-bDSRLpEqYCmFb11Zi_e0F4kO2P365EFvv_O-Tmv7DT_tDKexiiVmB7hIi7LnXDKI4cxY4NcYWEWxciQsgDUpQCabTarcROKkbnFvvUAw2v1pSMAdrUz1zcekP2KC6v44Tjn6hXUkhKB-LrnSPnc2R7qXLC7_Lb6HnKocbDPHERPSM4ZSha22ilcnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: تنگه هرمز را با قدرت گرفته‌ایم و با قدرت حفظ خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/133381" target="_blank">📅 09:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133380">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
تلاش سه کشتی برای عبور از تنگه هرمز؛ اصابت به دو فروند
🔴
طبق تصاویر ماهواره ای شب گذشته سه کشتی بزرگ قصد عبور از تنگه هرمز را داشتند که ایران دو فروند را هدف قرار داد. یکی از آنها از کار افتاده و سرنوشت دومی همچنان نامعلوم است.
🔴
سومین کشتی تحت اسکورت نیروی دریایی ایالات متحده آمریکا موفق به عبور شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/133380" target="_blank">📅 09:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133379">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
فوری / سازمان عملیات تجارت دریایی انگلیس اعلام کرد گزارشی درباره وقوع یک حادثه دریایی در فاصله ۹ مایل دریایی در شرق سواحل عمان دریافت کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/133379" target="_blank">📅 09:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133378">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
اهداف حملات امروز ایران:
🔴
پایگاه امیر حسین در اردن
🔴
پایگاه هوایی العدید در قطر
🔴
بندر شیخ در کویت
🔴
پایگاه دریایی پنجم آمریکا و منطقه الجفیر در بحرین
🔴
بندر الدقم در عمان و مخازن سوخت ارتش آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/133378" target="_blank">📅 09:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133377">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hC3RYMKqdjZb8Obb31H9cxJuiOxIpQ5OA02oEsTAeXps0kWzrQFGqEkxpVosjCPMpq6Qh2Opv0E3Sd-EH5y-lJpJktGXlGrMSlFWDUjytn9cTBjtidiITO_OCu4XZJ7h8L5z8AqJ0Q4jwjHEPk_A5wTdDlOYlwFqQbiZCuT-D_Ki2DQa0BjTK2wy_K6Ueo_RDHWwpwIor35lnt6llk-Gu7DYX8SxO73KO58hKI6yMur1axLoLeojUX3PGxQUME14ZPxEfYOo7kJ_C539oqT_l5FMunPufRX9EixDgj4HJlFPkRLPFvKuMYc0GSD64BRJzAwQkcijGF7N4PqlZS04xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر هدفی که در نزدیکی شهرستان خنداب استان مرکزی مورد اصابت پرتابه امریکایی‌ها قرار گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/133377" target="_blank">📅 09:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133376">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
امروز؛ آغاز امتحانات نهایی دانش آموزان یازدهم و دوازدهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/133376" target="_blank">📅 09:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133375">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fR9swTCZt02SqdIIHhl5_FsXGhQq0Sg9Uf-aFnStf2BhYysO_4iJyt5R3gc0__56xANEduPHyiriITc8CG6K-PClsAjL22rhF9XV100DrO3b2KwqJpvxZZu5aWSoxr9t_EdJIRGuu3lvoxUpNKgWkGYcD6QZlBLY86a1sohEZR-ub_w3ei-DzbDaurcjoFX2ZSnzVSdcDbyR77mSBfzHA6hoIwsqVqEpfFuzlkYang-AnSVfcTWj5GdCHihB41vMgcsM_ZvEo4_E_VJkNv1CmffosHtEOLD327pbN6yYmo6wFbJbpTTtlFkKSv_hRkL2H3kIvuciB0EWRX6eEYe0MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / سازمان عملیات تجارت دریایی انگلیس اعلام کرد گزارشی درباره وقوع یک حادثه دریایی در فاصله ۹ مایل دریایی در شرق سواحل عمان دریافت کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/133375" target="_blank">📅 09:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133374">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqXRklZ0j24xffHw8-2xkWTu0aOjJGCwa_xtlGBc889xyYHbqiihps5ZiWxU14YVz_V4LPd-tSf4H-QtET_5NcEN9DDXtk1svkvbPmPTFZyH8-GtHXHxN6t6hVW2ujxk-i2ChmQD7C29C0eWHRE8jQ-xmrgm8QiJPunsirPOQRzAifYJ4TNMK96STT16WK3W-psIfjMxOeWOy777sfEfqjutlx4gE6FWUAqTYvzfGg2bFS-xCr2jh8ocKtGpTphCD4SrWn_NiNfKyd1Ryjxl71UdgWRXH8dPsr5aqdtlijncxGNDOrkwvX0pbqVQ6tZNVuXoC2AoRmRkNYoXUXS-Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستاد ارتش کویت اعلام کرد پدافند هوایی و نیروهای نظامی این کشور در این لحظه در حال رهگیری و مقابله با اهداف متخاصم و بیگانه در حریم هوایی کویت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/133374" target="_blank">📅 09:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133373">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6496896d1b.mp4?token=ABtlvm5qckj5HQr__r_xBLVuyqXclwWxbwT8LAypIjNUfgj7VG8U1Hjt0wxNvi6Xa0q8dVsvlFtlUVj9xd2XvwQ1_XY1lmK9RLid-ywAtSGJ3cVmOyK2fKfHrInsvnzsCsDRxkZmdxOqxxYVuo0debMGbi_bUagXBaISvTBAAW6zKdj1B_4b2-TUMgKgwG2EuXvfiSwGbZjomBdOMp7Hi4EWv2krx2upuCL7KBXYAX2h7dqDLG-zVRnbHPno7Gs2GEtUQgX61TS3jNHkbm3Ay94nz-A9io3TdNzR7u-7oMJ6zLZI913bRs6hHjr8XcuRr2qae3ku7emRcv84cvHjoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6496896d1b.mp4?token=ABtlvm5qckj5HQr__r_xBLVuyqXclwWxbwT8LAypIjNUfgj7VG8U1Hjt0wxNvi6Xa0q8dVsvlFtlUVj9xd2XvwQ1_XY1lmK9RLid-ywAtSGJ3cVmOyK2fKfHrInsvnzsCsDRxkZmdxOqxxYVuo0debMGbi_bUagXBaISvTBAAW6zKdj1B_4b2-TUMgKgwG2EuXvfiSwGbZjomBdOMp7Hi4EWv2krx2upuCL7KBXYAX2h7dqDLG-zVRnbHPno7Gs2GEtUQgX61TS3jNHkbm3Ay94nz-A9io3TdNzR7u-7oMJ6zLZI913bRs6hHjr8XcuRr2qae3ku7emRcv84cvHjoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / وزیر دفاع اسرائیل از عملیات مستقل قریب‌الوقوع علیه ایران خبر داد
🔴
یسرائیل کاتز، وزیر دفاع اسرائیل اعلام کرد به دستور او و نتانیاهو، اسرائیل به زودی یک عملیات مستقل علیه ایران انجام خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/133373" target="_blank">📅 09:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133372">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDEgZKn3tAbZrWcxYOk0uhvPPBAuz9q3tf5lrQgky8UDT1Jej7i64eJwN9keTPJad8Rx9nKn-8kAkcOdkjHeghPrRuIspCXCHVOk4XyIZUi1F3xpelqGoRa4Lk8-VGc--1XN60n7VlPFvs0JK0_65E3Cgm3_XWaBvuGctYCD3DhiFqO9eEjlf5FlAEytO-8xkJGmIp1KYeYhwdR4EXE9KLJD_NyHgjUv_FPvf6ZFiMg8PM6J_l0mVAhY3IhHKUiKh5FEhx0XKOBmgjt0yPUkmyz30Px4r5QyZqIky0F8Hf_ud4TuhdePQRuP13wUE84-m31JBFv55daVGTAz8b4tbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت پروازها در آسمان منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/133372" target="_blank">📅 09:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133371">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
استانداری لرستان: صبح امروز یکشنبه شهر ویسیان از توابع شهرستان چگنی دوبار مورد حمله هوایی آمریکا قرار گرفت
🔴
این حمله تلفات جانی نداشته‌است و هم‌اکنون شرایط عادی می‌باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/133371" target="_blank">📅 09:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133370">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
این دور از حملات ایران بندر دقم عمان نیز هدف قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/133370" target="_blank">📅 09:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133369">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
شهر هایی که تا کنون مورد حمله ارتش آمریکا قرار گرفته اند
🔴
بندرعباس
🔴
سیریک
🔴
کنگان
🔴
بندر دیر
🔴
عسلویه
🔴
چابهار
🔴
کنارک
🔴
بوشهر
🔴
ماهشهر
🔴
مثل حملات اخیر، تمرکز آمریکا به جنوب و خط ساحلی ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/alonews/133369" target="_blank">📅 04:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133368">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
انفجار در ماهشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/alonews/133368" target="_blank">📅 04:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133367">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
کان نیوز:
عمان به آمریکا اطلاع داده است که ایران پیشنهادات مربوط به تنگه هرمز را رد کرده است.
🔴
در پاسخ، واشنگتن تصمیم گرفته است که محاصره دریایی و عملیات نظامی علیه ایران را از سر بگیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/133367" target="_blank">📅 04:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133366">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFH_iqE7BWEcbnZhHXa6_1d0qe9ACIfFfTWL3LVwMmGwydlZ1xTqaBd8gnWjDc1VLq7b-p707_hq0Fw_VbWm1btF7DjDGH0Eov0HGI-cNH4ncoWByk98n0q38BDYCu3NQs-U8ZgEmdtSQ6BbwA09YJBUnH3ZDWMXFpoH-yKkcEoYckmpSoxZJ3u9q0mYUqgMlWILiripj7Yd3F8A1TNXlxG6sp-zvYXQZlExwLt7YISAj7d5diyysZHil3EuZficRWq_ZCdKD5LISxHy3ZJyG3i1e2amUPtR8919Fx848tA5K-kxet_DZyLB8OVQiyZmCDANhpL7pSjSVgOHo0ZoXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شلیک موشک های آمریکایی از کویت به سمت ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/alonews/133366" target="_blank">📅 04:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133365">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
حمله آمریکا به پایگاه هوایی بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/alonews/133365" target="_blank">📅 04:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133364">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
فوری/انفجار مجدد در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/alonews/133364" target="_blank">📅 04:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133363">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
گزارش رسانه های عربی:
هواپیماهای نظامی آمریکایی به طور مداوم به سمت ایران پرواز می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/alonews/133363" target="_blank">📅 03:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133362">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
یه کشتی میزنید، ۲۰۰تا نقطه بمبارون میشه!
🔴
هرطور فکر میکنم عقلانی نیست و حماقته
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/alonews/133362" target="_blank">📅 03:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133361">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
انفجار در جاسک
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/alonews/133361" target="_blank">📅 03:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133360">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
چند انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/133360" target="_blank">📅 03:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133359">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tT2NJMr3djprMDXb2sfSEv3D45jYKZEIDfHhMtNXWvIhPl3kJffTNfMlrti0MsrqAKoVilRM92B9WdGhhPId5MlM2opSy6kHGogqjYIXhNKltAB7G2h2-SmRUgAFnAbkXNy9EeAWHxWeA672HLtuSibntMW8nzDyRT0v26TOl-lePzzCAfJCZxGQG6pd0CNk_VRzmuO8j267FHryxVZWjZBjq5zFjxe_1S0Oxs_3ltgqRUO_K4sPXFyrDYfGOMJBvTediu8HJUpeI3vmF22DsD6aR3ydUpkTpfRjPbmUXWlcxmJWYrkPGsvieVB70ZKmjG4dhm_bEE6LNnO3a7KUYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: الله اکبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/alonews/133359" target="_blank">📅 03:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133358">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فوری/گزارشات از حمله ایران به یک کشتی دیگر در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/alonews/133358" target="_blank">📅 03:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133357">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ee80a6069.mp4?token=SJv5y1NtFDqpKWyjZ_W0KdXhu_8YxISSmA_IgOEwlK9zdr-ExdnNqSVbOg2kEG0PqxlB0XVID-hjXPs8lxIBedeXQLQWEfu1BG8mE0HQmNwnP4kEssSwhEuDaDDeGflsDPXS6Hezmg1Vyhe5mbYsKTi6sDY1vfpBh9lo_8uCHiSkwhljAKqjmNkyWxHqc92ubAV4s8CyIg05LkIWnCZL7N3hOjULI9-B2OnrreIZ-PywF5yX82pmmLlfueHop8W71htAO_3xez95QWTn6dTmNwcpjoHZ5gc1cKvywzpUNaO5Gbv6Z5jhQkS-Gso57I9lBKvEB0gLvqcnbPdkTHoToQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ee80a6069.mp4?token=SJv5y1NtFDqpKWyjZ_W0KdXhu_8YxISSmA_IgOEwlK9zdr-ExdnNqSVbOg2kEG0PqxlB0XVID-hjXPs8lxIBedeXQLQWEfu1BG8mE0HQmNwnP4kEssSwhEuDaDDeGflsDPXS6Hezmg1Vyhe5mbYsKTi6sDY1vfpBh9lo_8uCHiSkwhljAKqjmNkyWxHqc92ubAV4s8CyIg05LkIWnCZL7N3hOjULI9-B2OnrreIZ-PywF5yX82pmmLlfueHop8W71htAO_3xez95QWTn6dTmNwcpjoHZ5gc1cKvywzpUNaO5Gbv6Z5jhQkS-Gso57I9lBKvEB0gLvqcnbPdkTHoToQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/دیده شدن پهباد در آسمان تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/alonews/133357" target="_blank">📅 03:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133356">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری/پدافند ماهشهر فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/133356" target="_blank">📅 03:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133354">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">💢
فوووووری/پرواز جنگنده بر فراز تهران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/alonews/133354" target="_blank">📅 03:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133353">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
انفجار در عسلویه
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/alonews/133353" target="_blank">📅 03:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133352">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فوری/پرواز جنگنده در قزوین به سوی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/alonews/133352" target="_blank">📅 03:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133351">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران:
اگر وضعیت کنونی توسط میانجی‌ها مهار و کنترل نشود، تنگه هرمز می‌تواند به نقطه آغاز یک جنگ جدید تبدیل شود.
🔴
به نظر می‌رسد ایران پس از پایان مراسم تشییع، دیگر از آن محدودیت‌ها عبور کرده و اکنون بر مبنای آمادگی برای همه سناریوهای احتمالی عمل می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/133351" target="_blank">📅 03:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133350">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
انفجار در کنارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/alonews/133350" target="_blank">📅 03:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133349">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3lFwlikIFzcWyjp7EkGXpZjRDVKYvz3aF-02_iiVwEO3D6mtO9NaSXCiN548er6gF70-g2knF5MhFzANutetuaN8-lDj5FUAiZpsi-O98PknGbKxBtB_HHT9GaJa3OApB6hyU49TKt1ORYxm6uXCM1SawXCqB7ZW-KwO_nWFhRKtg4QLbsKCrb81OYCTPp8HXpWoEXiTS2y4AduQwZsyLW4xFZUqe21dMINnXHh7ITd5XRqbajpzg1sPvhFIt9PZnQ0m2Lp0qKa2cyBhv13v-SqnlPIofbTVuEyVRSqgYEI1QKQ02vKP5moX988dQlBew8-o_4xrK4KxQsjrl4-Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/هگست،
وزیر جنگ آمریکا :
- ایران انتخاب بدی کرد، حالا باید تاوانش رو بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/alonews/133349" target="_blank">📅 03:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133348">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/133348" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133346">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aX0TCnfLvZ_NQFnhIBMsEzAyLqXGpEQ6q6PKPbhmkBzroNDHI9waRZt6v4v14988gYWQduaYJp3K2a2eBfM7bifJf8G7bFNlEbMoToDnYEsnWQ9BZJLnNpanNh0L3gNEfiGoOusE167AtxDjHtUROE6Ca8KSxSjS91ceXyCiPswOLGnoY8_eNHBIc0SDaUsYi9zVsBiOTahYjp11j4zpbph_D5Z3fOAiHIhL96W-kdTHqKsqLRStH1KEtYcIYV10_Q3X78pPHy74GZLQ6_r25xjunsTYo4Sib31KX7K7nX9GSvCdh1O6M4mPRq1Gb2PD2GkyhiLbK3L6OBcVRDY4rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: ساعت ۷:۱۵ بعد از ظهر امروز به وقت شرق آمریکا، نیروهای فرماندهی مرکزی ایالات متحده پس از حمله آشکار نیروهای سپاه پاسداران انقلاب اسلامی به کشتی کانتینری M/V GFS Galaxy با پرچم قبرس که در حال عبور از تنگه هرمز بود، دور سوم حملات خود را در این هفته علیه ایران آغاز کردند. یک خدمه غیرنظامی مفقود شده و کشتی به دلیل آتش‌سوزی در داخل و خسارت قابل توجه به موتورخانه قادر به ادامه سفر نیست.
🔴
پس از آنکه ایران به خاطر حملات قبلی به کشتی‌های تجاری مسئول شناخته شد، اما دوباره شکست خورد، فرصت دیگری برای نشان دادن پایبندی به یادداشت تفاهم به ایران داده شد.
🔴
در پاسخ، ایالات متحده با ادامه تضعیف توانایی ایران در حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه عبور می‌کنند، هزینه سنگینی را تحمیل می‌کند. این حملات به دستور فرمانده کل قوا انجام می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/alonews/133346" target="_blank">📅 03:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133345">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned «
🔴
این چنلو حتما داشته باشید زمان جنگم پروکسی هاش همیشه وصل بود  @proxynab
»</div>
<div class="tg-footer"><a href="https://t.me/alonews/133345" target="_blank">📅 03:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133344">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوری/بر اساس گزارشات، ستاد فرماندهی نیروی انتظامی اهواز، هدف یک حمله هوایی قرار گرفته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/alonews/133344" target="_blank">📅 03:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133343">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">انگار نتا یکم ضعیف شدن  اینارو داشته باشید تا در صورت قطعی متصل بمانید
✅
پروکسی |  پروکسی | پروکسی پروکسی |  پروکسی | پروکسی پروکسی |  پروکسی | پروکسی پروکسی |  پروکسی | پروکسی</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/133343" target="_blank">📅 03:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133342">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انگار نتا یکم ضعیف شدن
اینارو داشته باشید تا در صورت قطعی متصل بمانید
✅
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/133342" target="_blank">📅 03:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133341">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37792480c.mp4?token=UgVaL44xJkb0YQo8ozhQJX3W04VCTnkpYEzmKCFK2AIp5wEdtVEXMmTz811_xmRDXgyl-OKInOWI-hoSOfbsT-DE2RQNCEl6P6_thZizKrdiM_kbvjUY7SLm6IKZ7tLnoY0BZckQZeTFmnElZQ5oFZ7OQiNZUqOEjm0pQ_ejFkCqGofe9G-cCXNH9Wje2ZffNh4fTJoh5P8OGVIq8tX3LgN1yZ0IbOHPI3AcOE41WfBU5jv8nXrCjMsAsR6hcn29gvtnuGWo4cGAS8aebofflfexW918JNC_KLpjn-WdLsFyNjdSqiISQ5kqffZeEM5Jzhy3Yyj4SZGB58QPn6SBnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37792480c.mp4?token=UgVaL44xJkb0YQo8ozhQJX3W04VCTnkpYEzmKCFK2AIp5wEdtVEXMmTz811_xmRDXgyl-OKInOWI-hoSOfbsT-DE2RQNCEl6P6_thZizKrdiM_kbvjUY7SLm6IKZ7tLnoY0BZckQZeTFmnElZQ5oFZ7OQiNZUqOEjm0pQ_ejFkCqGofe9G-cCXNH9Wje2ZffNh4fTJoh5P8OGVIq8tX3LgN1yZ0IbOHPI3AcOE41WfBU5jv8nXrCjMsAsR6hcn29gvtnuGWo4cGAS8aebofflfexW918JNC_KLpjn-WdLsFyNjdSqiISQ5kqffZeEM5Jzhy3Yyj4SZGB58QPn6SBnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جوری که دانش آموزا صبح باید برن حوزه امتحانی:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/133341" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133340">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
انفجارهای پی در پی در جنوب کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/133340" target="_blank">📅 03:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133339">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">💢
فوووووری/پرواز جنگنده بر فراز تهران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/133339" target="_blank">📅 03:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133338">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فووری/سی بی اس: حملات به تهران هم‌میرسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/alonews/133338" target="_blank">📅 03:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133337">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
فوری/انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/alonews/133337" target="_blank">📅 03:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133336">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAyaTo68tCRBZ-vctKBiodBZX4eYr_E2UFWahrmjui0Vd8kbcdE2sHqmthcft_Ppp4o9ADU2jqI_kIhecbKw6wlaqb5x5pHXyYntZtHkaMnecLUaOKhkLnlNvx5BTgWsJn9gGtRwx-tSU12y4CkUZnAMRTJaZvoeQaIfu_yjYevLS0PITdXmgmUA1jVom59IUyhwL4YgSPjyMziwB09kwJUQm3RmBlWk-6ow6zXH6hWfHYtU6XeYdVPk6PU_hFpQ5sTx2oNBnrbGn8NmHE7KnHgcG3mDG2wf0ll1JoBCDhF241vpqjX_O3oMdz4QfDRpiJMOptXCXwbfAgiLwRmnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/انفجار شدید در بندر دیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/alonews/133336" target="_blank">📅 03:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133335">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
فوری/انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/133335" target="_blank">📅 02:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133334">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری/انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/alonews/133334" target="_blank">📅 02:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133333">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
فوری/حملات به تمام خط ساحلی جنوب
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/133333" target="_blank">📅 02:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133332">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36c2812772.mp4?token=nhitgfpzgas-nJis5fULk_eFny1bUa_XUFFfc6rQwO90NU6qgHWkQBueT_twI0E9WGvJeRK7svC5V5N8kNmNRsqIQA5XkY4y3LhkF6SfmDLFe2adWWoQ6_Ldn9vcupOuHHGkM8oBwfI4d8Csc6MrGvq0mzEGoeYbIHEB2kouIXroTkwGCMOb8A2RWf1ykcHBNluZGIuJLnSeXichNBENceJHRvDGkn6rpx2oo_sg3pA2IVvyDbOaYpTWbtawvn__3ziOlr7Xt-BqZlyAf5tS5_qF7eCzHiUxKRd5t99dBbYnA0c1ngGa11Uybh3EvIwKsRQ1ap0_Ngwo9hMZyLt7sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36c2812772.mp4?token=nhitgfpzgas-nJis5fULk_eFny1bUa_XUFFfc6rQwO90NU6qgHWkQBueT_twI0E9WGvJeRK7svC5V5N8kNmNRsqIQA5XkY4y3LhkF6SfmDLFe2adWWoQ6_Ldn9vcupOuHHGkM8oBwfI4d8Csc6MrGvq0mzEGoeYbIHEB2kouIXroTkwGCMOb8A2RWf1ykcHBNluZGIuJLnSeXichNBENceJHRvDGkn6rpx2oo_sg3pA2IVvyDbOaYpTWbtawvn__3ziOlr7Xt-BqZlyAf5tS5_qF7eCzHiUxKRd5t99dBbYnA0c1ngGa11Uybh3EvIwKsRQ1ap0_Ngwo9hMZyLt7sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/آسمان بحرین، دقایقی قبل/ظاهراً مبداحملات به جنوب کشور بحرین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/133332" target="_blank">📅 02:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133331">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری/گزارشاتی از شنیده شدن صدای انفجار در دیر و کنگان شنیده شده است/احتمالا اسکله دیر مورد حمله قرار گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/133331" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133330">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
فوری/گزارشاتی از شنیده شدن صدای انفجار در عسلویه و بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/alonews/133330" target="_blank">📅 02:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133329">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
فوری/العربیه :
هم اکنون تماس وزارت خارجه پاکستان با دو طرف برای کاهش تنش در منطقه در حال انجام است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/133329" target="_blank">📅 02:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133328">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
فوری/اولین تصویر از موشک باران تنگه هرمز
مشاهده فوری</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/133328" target="_blank">📅 02:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133327">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
تابناک مدعی شد: گزارشات تایید نشده از حضور تکاوران ویژه دریایی سپاه  "S.N.S.F" به صورت تیم های غواص مین ریز  و قایق های تندرو در تنگه هرمز مخابره میشود.
🔴
این تکاوران از یگان های نخبه دریایی ایران مستقر در مناطق دریایی سپاه در خلیج فارس هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/133327" target="_blank">📅 02:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133326">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9lP7YmL0dh83dWEDq7hFyL_H2iahCPAUtjFqIEERtYJX6HMV1psKRKBa_csTGkpHccgkjfkdV3wZr6Tse6hDYMVTqP2Jp9glUuDy-YjnAC2kBMbcPERUs8l0vUiTqTj7e5GQfBL9WMgORKCJDPAQeQcT-wLSc2ZRGt8f_2Yd0YeFT_8g-gmpLE7i0EyuREea4ajDLJFWRxw5V79WB5phB2dEstb0ZrhBZsd0lcGm6vb4dap9Ut9bniWo3-a2gWCF552Tae_qvBo9LM2-Vpet_MgTzRxD4trAlNaa9YpOlWlc1MzPXRRc3xRh6spDfoUbtyA89FtJ30qTrBahUkUJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال 14 اسرائیل :
مذاکرات به بن‌بست خورد؛ ایران یه پیام جدید برای ترامپ فرستاد و گفت: از این لحظه تنگه هرمز رسماً بسته‌ست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/133326" target="_blank">📅 02:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133325">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">💢
فوووووووری/پرواز جنگنده‌های آمریکایی در مرز ایران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/133325" target="_blank">📅 02:18 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
