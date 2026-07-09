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
<img src="https://cdn4.telesco.pe/file/qRS-uAkzLeqVWn50OxhChxm-wHS6G6XWyB9bIZKZAHeLP03JKx-bm3B2CBBjCOuHv13uOO39Kya2DeGEy9QprTUHHTQ7ck2Wef4AK9Z-oGbL8u7k34kSuASUGNUhu1AQ-nWBuNjPhubPQRr-YhfVLPryQsZSCHXgxYT12kh9GA3X_Iuo0jJdWr_aGh_HcJbbBd67zhOPPttWi8d76HRNSWbtDREJy8-lXNYznHXAx6eZdkWUWApogTHg-5VyVZuiUBY502wrR1H8XWfrieFCKUDVqTtYjERZttBjiPFcWSUkfVqR936iI054xBuWmDdCRU_xve6Eob99BvFw13mjSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 924K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 20:42:49</div>
<hr>

<div class="tg-post" id="msg-132883">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
فارس: برخی منابع خبری  مدعی شدند سوخت‌رسان‌های اماراتی در حملات بامداد چهارشنبه آمریکا به بنادر ایرانی کمک کرده‌اند/این هواپیماها توسط امارات متحده عربی اداره می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/alonews/132883" target="_blank">📅 20:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132882">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
روسیه و چین در نشست شورای سازمان بین‌المللی دریانوردی، سند پیشنهادی امارات درباره تنگه هرمز را رد کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/alonews/132882" target="_blank">📅 20:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132881">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
فوری / حازم قاسم سخنگوی حماس در غزه ترور شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/132881" target="_blank">📅 20:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132880">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mA8EejL3zq_iVx2xwXW7Q2Gw2rZ0ZEdD5Kysi4f8y-2Ppx4SzWfwVuVwbPCv6h6YMedMeun4ZQdg4gMSdIIvUHLi1AP9GOKltcTQtEmLXhrn6UJeOJqJJwlEmVfTwD6B2XD1wy3W8qVfzUbWi1A4k_ZLcxTrGtsUdUFp7HVxpRRIkF4k70KTOcf_4_3KXIel2aVlZDUKpDCj5phKXfFeW0rB4KN5UmoHrwlYRZu7D8_dXyA2tJ7m0NATTR69930aR2M8thb4r3TbU_cgyQqvyeDSZONQmh6gaqdEdmjjWvyR8nlEtKEnzkaulY44If2gC2hZ9wzrI0cD5X1249Rvpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون جنوب لبنان هدف حمله شدید قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/132880" target="_blank">📅 20:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132879">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: ضمیمه محرمانه توافق اسرائیل و لبنان، به تل‌آویو اجازه آزادی عمل علیه تهدیدات در داخل «خط زرد» را می‌دهد
🔴
این ضمیمه بنا به درخواست دولت لبنان، محرمانه مانده
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/132879" target="_blank">📅 20:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132878">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
فوری / حازم قاسم سخنگوی حماس در غزه ترور شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/132878" target="_blank">📅 20:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132877">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
رویترز: گزینه‌های ترامپ در برابر ایران «محدود و بد» است
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/132877" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132876">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه، از مقامات ارشد بیش از 60 کشور دعوت کرده است تا هفته آینده در جلسه‌ای شرکت کنند که موضوع آن، به گفته دولت ترامپ، احیای تروریسم افراطی فرا ملی است. این موضوع، به ویژه، به گروه «آنتيفا» مربوط می‌شود، طبق گزارش واشنگتن پست.
🔴
این طرح، نگرانی‌هایی را در میان مقامات آمریکایی، متحدان اروپایی و کارشناسان تروریسم برانگیخته است. بسیاری از آن‌ها معتقدند که «آنتيفا» یک جنبش غیرمتمرکز است و نه یک سازمان تروریستی خارجی، و بنابراین، تهدید جدی بین‌المللی محسوب نمی‌شود.
🔴
سباستین گورکا، مشاور ضدتروریسم کاخ سفید، در مورد این موضوع بحث کرده است که آیا می‌توان از برچسب "سازمان تروریستی خارجی" برای هدف قرار دادن افرادی که ارتباطی با «آنتيفا» دارند، استفاده کرد. این اقدام، به گفته مقامات، می‌تواند ابزارهای تحقیقاتی بیشتری مانند نظارت را فراهم کند. برخی از مقامات دولت هشدار داده‌اند که ایجاد چنین رویه‌ای ممکن است در آینده توسط دولت‌های بعدی علیه فعالان محافظه‌کار مورد استفاده قرار گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/132876" target="_blank">📅 20:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132875">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
تکذیب انفجار در زنجان
🔴
منشأ دود آتش‌سوزی سوله بازیافت بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/132875" target="_blank">📅 20:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132874">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
مدیرعامل راه‌آهن: با تلاش مهندسان شرکت راه‌آهن در کمتر از ۱۳ ساعت پس از حمله دشمن آمریکایی به خط راه‌آهن مشهد؛ یکی از خطوط بازسازی شد و به چرخه خدمات‌دهی بازگشت.
🔴
خط دوم نیز تا ساعاتی دیگر بازسازی خواهد شد.
🔴
هم‌اکنون تردد قطارها در خط بازسازی شده از سر گرفته شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/132874" target="_blank">📅 20:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132873">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
روسیه: رقیق‌سازی اورانیوم در خاک ایران یک گزینه کاملا عملی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/132873" target="_blank">📅 19:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132872">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPr6qMAhi_YbFi9EIF_885lcfC0EZIOPKEeHD8san6wqpDThVyn5P0y67rKOeRBJbI7TmDKfU7O-sHIG0QenzkuAZmQ6pawfO9Xsp6lgbchJTtOxoX5aH-5AnBe9dKFJ95-O3g0fYSoISb0QjPI_cwK-8lhFoi0jvACv1qSrcDmQnsXVtGRA5-rqG0P9nUr8iXBgjBOBb6vuPLNxrA2QqvMxIAXvvN2K-UNQm27-odog0pl7ZF2YWGxjzHXq4idI_sVKSdVtgUXTASe5YiN0y3HJQ3mDARU2lr_UTsT-CZRtiXGfU6Db2InoVFdiZ8jRKOEH5j2_gEiCu-UFi0GXHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: چگونه «سلاح طلایی» ایران در تنگه هرمز به اولویتی بزرگتر از برنامه هسته‌ای آن که مدت‌ها مورد مناقشه بوده تبدیل شد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/132872" target="_blank">📅 19:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132871">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از منابع: قطر و پاکستان در تلاش هستند تا آمریکا و ایران را مجدداً به میز مذاکرات بازگردانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/132871" target="_blank">📅 19:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132870">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
نتانیاهو: جنگ هنوز به پایان نرسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/132870" target="_blank">📅 19:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132869">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ندف ایال: منابع ارشد اسرائیلی معتقد هستند که جنگ دوباره در مقیاس کامل آغاز نخواهد شد، اما تنش کنونی ادامه پیدا می‌کند
🔴
آن‌ها هشدار می‌دهند که رفتار تهران بسیار غیر قابل پیش‌بینی شده
🔴
اسرائیلی‌ها می‌گفتند تفاهم‌نامه، مزیتی به ایران می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/132869" target="_blank">📅 19:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132868">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/568e3cc6bd.mp4?token=ObXbT6qX6-JHYoGI0fp9Ytd4aL00YRRDwqLEWXBjRn454IuV6DXCWn1W95rF1rpKf5fwOBgUvjs6MhXx6ooVHWW3BXYrlPlPJJcJfA80fzX6nPQkgEQAq4jaSDoV9oZwUFGWb8-m1eJ1dC0disMfocFEx4wSFHJkRnX5wNxGAUndDVkQz2RUddwDRgctQzW_WjbSmQN5E66Fi4T3n2-CdWUhW5lCH9gCe3tzuzNlvKVFSCto7ifIg5UD7BOBekt5noxXh_fjzXaIZPTeJrKiqXvFQwadR00CSY_oqwbP_rTLy1fmXegE_rj_jVks51F3daQB2x_8S--zKek34T8Y0LMKzlRdnpdxmfxyb3sPMVu7nWSNIVWik3uMg8x-DOubsjMbSdVxYOYSXY3c1ghzB0XTnEcdmQWWqRol9uvotBKgVefTRqbb-EKLzoNSZjST7unmY0asjz7t2aDBjvQ2vik4qtKhXxC46gyYtfWUmGByTkg3aMwGUidZUgv9FokLA9gTYVb3bf_fjap6BD8EK9RiDO0IpDKTn2I7lU5EHp9QOxNobOl3IC99QnSRgWYUz-nX2xRDnGVAmy1oVa1h1sMLrpcPstVo83BC2fiMZDj1JenpaQ7WeepFzPljcaoGmzeGtTvzW21DyRrGOmcU92QPkfl5xbv5yNGkxMTlcWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/568e3cc6bd.mp4?token=ObXbT6qX6-JHYoGI0fp9Ytd4aL00YRRDwqLEWXBjRn454IuV6DXCWn1W95rF1rpKf5fwOBgUvjs6MhXx6ooVHWW3BXYrlPlPJJcJfA80fzX6nPQkgEQAq4jaSDoV9oZwUFGWb8-m1eJ1dC0disMfocFEx4wSFHJkRnX5wNxGAUndDVkQz2RUddwDRgctQzW_WjbSmQN5E66Fi4T3n2-CdWUhW5lCH9gCe3tzuzNlvKVFSCto7ifIg5UD7BOBekt5noxXh_fjzXaIZPTeJrKiqXvFQwadR00CSY_oqwbP_rTLy1fmXegE_rj_jVks51F3daQB2x_8S--zKek34T8Y0LMKzlRdnpdxmfxyb3sPMVu7nWSNIVWik3uMg8x-DOubsjMbSdVxYOYSXY3c1ghzB0XTnEcdmQWWqRol9uvotBKgVefTRqbb-EKLzoNSZjST7unmY0asjz7t2aDBjvQ2vik4qtKhXxC46gyYtfWUmGByTkg3aMwGUidZUgv9FokLA9gTYVb3bf_fjap6BD8EK9RiDO0IpDKTn2I7lU5EHp9QOxNobOl3IC99QnSRgWYUz-nX2xRDnGVAmy1oVa1h1sMLrpcPstVo83BC2fiMZDj1JenpaQ7WeepFzPljcaoGmzeGtTvzW21DyRrGOmcU92QPkfl5xbv5yNGkxMTlcWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: من تصمیم گرفته‌ام که در طول ده سال آینده، 350 میلیارد شکل به بودجه دفاعی اضافه کنم. بخش بزرگی از این مبلغ به نیروی هوایی اختصاص خواهد یافت.
🔴
در راستای این تلاش، ما همچنین یک صنعت گسترده تولید مهمات، با استفاده از فناوری‌های اسرائیلی، ایجاد خواهیم کرد. این سلاح‌ها متعلق به خود ما خواهند بود و وابستگی ما به خرید از خارج را کاهش خواهند داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/132868" target="_blank">📅 19:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132867">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
نتانیاهو: جنگ هنوز به پایان نرسیده است. در کنار چالش‌های قدیمی، چالش‌های جدیدی نیز در حال ظهور هستند. محورهای قدیمی در حال فروپاشی هستند و محورهای جدیدی در حال شکل‌گیری‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/132867" target="_blank">📅 19:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132866">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
نتانیاهو: «حفظ برتری هوایی ما، یکی از ارکان اصلی امنیت ملی ما و کلیدی برای حفظ ثبات در خاورمیانه است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/132866" target="_blank">📅 19:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132865">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
قیمت نفت و گاز در معاملات امروز کاهش یافت. نفت برنت با افت ۰.۹۴ درصدی به ۷۷.۲۹ دلار، نفت WTI با کاهش ۱.۱۳ درصدی به ۷۲.۶۹ دلار و گاز طبیعی نیز با افت ۳.۵۲ درصدی به ۳.۰۹۹ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/132865" target="_blank">📅 19:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132864">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
بلومبرگ با استناد به داده‌های کشتیرانی: ایران در ۲۴ ساعت گذشته برای تخلیه نفتکش‌های حامل ۱۱ میلیون بشکه نفت خام عجله داشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/132864" target="_blank">📅 19:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132863">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
شورای همکاری خلیج فارس: حملات ایران به کشتیرانی در تنگه هرمز، امنیت انرژی و تجارت جهانی را تهدید می‌کند
🔴
ما از شورای امنیت می‌خواهیم که موضع قاطعی برای تضمین آزادی دریانوردی در تنگه هرمز اتخاذ کند.
🔴
ما ایران را مسئول این حملات می‌دانیم و از آن می‌خواهیم که فوراً و بدون قید و شرط تمام اقدامات خصمانه خود را متوقف کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/132863" target="_blank">📅 19:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132862">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
نتانیاهو : برای هر سناریویی آماده‌ایم
🔴
یه چیز رو هم خوب می‌دونیم؛ اینکه باید همیشه آماده و قوی باشیم
🔴
قبل از هر چیز، خودمون رو تغییر دادیم  جسارت به خرج دادیم
🔴
پیش‌قدم شدیم و حمله کردیم، ثابت کردیم دست بلند نیروی هوایی اسرائیل به هر جایی می‌رسه
🔴
از یمن تا ایران، وقتی هم از دست بلند اسرائیل حرف می‌زنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/132862" target="_blank">📅 19:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132861">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
کاتز: آماده‌ دور سوم درگیری با ایران هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/132861" target="_blank">📅 19:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132860">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
خبرگزاری تسنیم: بیشتر از ۱۰ میلیون نفر در مراسم تشییع در عراق شرکت کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/132860" target="_blank">📅 19:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132859">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
منابع دولتی پاکستان به خبرگزاری آناتولی گفتند که پاکستان و قطر تماس‌های جدیدی با آمریکا و ایران برقرار کرده‌اند تا دو طرف حملات نظامی بیشتر را متوقف کرده و «طبق توافق» به مذاکرات بازگردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/132859" target="_blank">📅 18:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132858">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
نتانیاهو: اگر ما اقدام نمی‌کردیم، ایران به سلاح هسته‌ای دست پیدا می‌کرد و جنگ هنوز تمام نشده است؛ چالش‌های جدیدی پیش روی ما در حال ظهور است.
🔴
ایران ضربه سختی خورده است و سیاست ما روشن است: ایران چه با توافق و چه بدون آن، سلاح هسته‌ای نخواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/132858" target="_blank">📅 18:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132857">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
اولیانوف: هیچ عوارضی برای عبور کشتی‌های روسیه از تنگه هرمز پرداخت نمی‌شود
🔴
میخائیل اولیانوف، نماینده دائم روسیه در سازمان‌های بین‌المللی مستقر در وین، گمانه‌زنی‌ها پیرامون پرداخت عوارض عبور از تنگه هرمز توسط کشتی‌های روسی را رد کرد.
🔴
اولیانوف تأکید کرد که هیچ‌گونه هزینه‌ای از سوی کشتی‌های روسیه برای تردد از تنگه هرمز به ایران پرداخت نمی‌شود.
🔴
وی در پاسخ به سؤالی درباره وضعیت کشتی‌هایی که با پرچم کشورهای دیگر از این مسیر عبور می‌کنند، اظهار داشت که ارزیابی دقیق درباره اینکه آیا ایران از آن‌ها عوارض دریافت می‌کند یا خیر، دشوار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/132857" target="_blank">📅 18:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132856">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
عراقچی به فرمانده ارتش پاکستان: ایران قاطعانه مقابل هرگونه ماجراجویی آمریکا می‌ایستد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/132856" target="_blank">📅 18:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132855">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/718137081a.mp4?token=c8gqhEuQvwBttPR2QgILyO46NcWhyyyZpI5tT86i5jMyxCmmGBtJD4KjSco7YHC1oZadF_OvUJnW4JAS39BpiqBBRSXJHqlcZ8q7UefHaJHv1Uq2X6MZ3lAt2Ek1Yir1VvVFKKwOIeJ2W0FX2N4190oxIsL8ubXs2tJVB3IqdLRNdLxLnkP_SIGop5evY2TUC9mXTHFyRU3qlMZ7bHxoRE9kc3_tUi5BR_FpntBUS6PQf4fz9T_SI1J0VsRv-DElOwFmZRaGm6dInrWHNxmRs6TQhPYlpP69_9XnQg-UQqrfzf4cOqKCJKoslf6jkBvbnr9zZVO53BeJvA9FQkLl7IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/718137081a.mp4?token=c8gqhEuQvwBttPR2QgILyO46NcWhyyyZpI5tT86i5jMyxCmmGBtJD4KjSco7YHC1oZadF_OvUJnW4JAS39BpiqBBRSXJHqlcZ8q7UefHaJHv1Uq2X6MZ3lAt2Ek1Yir1VvVFKKwOIeJ2W0FX2N4190oxIsL8ubXs2tJVB3IqdLRNdLxLnkP_SIGop5evY2TUC9mXTHFyRU3qlMZ7bHxoRE9kc3_tUi5BR_FpntBUS6PQf4fz9T_SI1J0VsRv-DElOwFmZRaGm6dInrWHNxmRs6TQhPYlpP69_9XnQg-UQqrfzf4cOqKCJKoslf6jkBvbnr9zZVO53BeJvA9FQkLl7IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بیرون کشیدن ۸۵ میلیون دلار حاصل از فساد عدنان الجميلی معاون پیشین وزیر نفت در امور پالایش عراق از زیر زمین!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/132855" target="_blank">📅 18:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132854">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
مصر در آستانه هسته‌ای شدن
🔴
روس‌اتم اعلام کرد نخستین واحد نیروگاه هسته‌ای «الضبعه» مصر در ۲۰۲۸ وارد مدار می‌شود و سوخت اولیه نیز از ۲۰۲۷ تحویل خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/132854" target="_blank">📅 18:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132853">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
فرانسه، سوریه را به عنوان یک مسیر جایگزین احتمالی برای انتقال نفت خلیج فارس در نظر دارد، به گونه‌ای که این مسیر بتواند تنگه هرمز را دور بزند، این در حالی است که تنش‌های بین ایالات متحده و ایران در این آبراه دوباره افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/132853" target="_blank">📅 18:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132852">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMKJNG_i1jxQfdSSWsi72exG10xBKqp45g1hkyeYBxpWLepJR9eHAfdSQpa5tfaf91oWg6_E5WWEFMGTBSA3jye5eFyqH3dD0gjoYbanf2SKILie4OweB33COeIzRFVkD2u1OSt-7L5fZvzXEzH8yJ1ik6X8NR5dmoAKhIagSdsLKVOHLB-FqOwDoPFTfesHML88sy5Zgu7qnDF5PFxzia0nOvD3ujvh9S787eRoz7Bzfqm2fmDJxZz4EJViNaGiDWP9ZN0IOObRRlF9oyJV8IWUuFrM8B7RiP9jqBN9lI4toUg4UKiwgaiIykmTM02hrRsjetbqXoAfFBvLBf1gXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین وضعیت قیمت نفت
🔴
نفت تگزاس: ۷۲.۶۹ دلار
🔴
نفت برنت (معیار قیمت جهانی نفت): ۷۷.۲۹ دلار
🔴
نفت امارات: ۷۲.۴۰ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/132852" target="_blank">📅 18:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132851">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qu31kJTCOwkgSjO2EfmuiRHixKNZ8ntrXChihx61uUs0e-TAOKygHOMd86ATSIu5Zf58ASBihr92YPmAYnOFqb2h91lQrvhUDxl9Pd7tb_FFHz6IpZCBil50kUgLSpUNscnRvlI3SCPS9cGY72ildm9zOPh17fJNPLBaLD8-xSzeOGkUPvpPWqAvnr8Qrddm38XUjK7hmxlfbLS36LSDJQ0Ti7vjd0ad9vLQ2NGLVC8JTH6xpRfbdMs9Vs8wIDH1xRnJH2cywE8hpOMB4JHPWD70htr99BbE8QBQgoG3IYMnmbuuIz8vnqaE6ySnN1kgDKDzKaQv4Xn-CmVLC9zpxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ضرغامی: در صورت تداوم تجاوزات، به کشورهای خلیج فارس اعلام کنید درب چاه‌های نفت خود را ببندند وگرنه آن‌ها را به آتش خواهید کشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/132851" target="_blank">📅 18:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132850">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
بلومبرگ : قطر موقتاً برنامه‌های خود برای افزایش تولید گاز طبیعی مایع در مجتمع رأس لفان را متوقف کرده
🔴
این تصمیم پس از هدف قرار گرفتن یک کشتی حامل گاز ال‌ان‌جی قطر در تنگه هرمز اتخاذ شد
🔴
کاهش عملیات‌ها، تعداد نفتکش‌ها و کشتی‌های حامل گاز ورودی به این مجتمع
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/132850" target="_blank">📅 18:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132849">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ov1nx-OZMfaUjfZBsSBZdM6L-T8ov6l7mMw6VqkehjTa3eGQxgZfl27ZGvMYLb1uwM3XSZG5aVYPk0AckZKEXYg7Mdl18iz225jBuJ8Z7d71pdRXE1pEuQeUcELXDw_s4qbWJ0wZnEHYkOcLvrX2cgTrs2hPoooTpvZWIgn7nuNviJ0s_33HvODF4h3mWwPYMA7STJUGKzRVrusvwSnK5wh0eNkXrF-DpV7BSg2sYlrz6zca5pxIPjvxOnL9bmnXXfJrXK6NxpMzv6M0GQE89lehmVUdjxBDV13O32b0IkrRwxjqjOoS3kSwsBrFWt-JiQ8V1Rv0fNqkJ3NlRytf9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇬
در اقدامی عجیب و برگ‌ریزون؛ دولت مصر ورود لیونل مسی و خانواده‌اش رو به خاک این کشور ممنوع اعلام کرده
@AloSport</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/132849" target="_blank">📅 18:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132848">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
عمان: از اعمال عوارض برای کشتی‌هایی که از تنگه هرمز عبور می‌کنند، حمایت نمی‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/132848" target="_blank">📅 17:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132847">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
مقام‌های اسرائیلی به i24NEWS: برآورد فعلی این است که ایران تمایلی به کشاندن اسرائیل به این درگیری ندارد و به همین دلیل، احتمالاً حمله‌ای علیه ما انجام نخواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/132847" target="_blank">📅 17:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132846">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc73b26ab0.mp4?token=NM3v0A99wNq0cN52Zk8VWfWPNpUgLKBL4CjP-gtHN898JM40wx5oepakf_OeJf0bbgHuPwzKEoLYMcVC_P7DdzlKmFPEGKqql-gaPFQQVxJWiGo8aWFMr6PtRHVlNeQncS-8p3DuEDxrp7YWM7PwUr4PdGLuWYb90n8hL2pH2lck_sX_E5JNuehHtTbmG8LeO0xZ0FfGWL6fw06y_n4e3wM74U50ighx6kMY9ynrP5jWA0X92lcTLdsYMb97IK6ltAqEWyz7nMZImzgbtGzjxfrkpOqZMxnHW__5UwD5rWv97HKlCzNr9jKbb6A5QV_Ahv9wSbaQFkB-yjdpfhfoNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc73b26ab0.mp4?token=NM3v0A99wNq0cN52Zk8VWfWPNpUgLKBL4CjP-gtHN898JM40wx5oepakf_OeJf0bbgHuPwzKEoLYMcVC_P7DdzlKmFPEGKqql-gaPFQQVxJWiGo8aWFMr6PtRHVlNeQncS-8p3DuEDxrp7YWM7PwUr4PdGLuWYb90n8hL2pH2lck_sX_E5JNuehHtTbmG8LeO0xZ0FfGWL6fw06y_n4e3wM74U50ighx6kMY9ynrP5jWA0X92lcTLdsYMb97IK6ltAqEWyz7nMZImzgbtGzjxfrkpOqZMxnHW__5UwD5rWv97HKlCzNr9jKbb6A5QV_Ahv9wSbaQFkB-yjdpfhfoNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار «انتقام، انتقام» در مراسم تشییع، امروز در مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/132846" target="_blank">📅 17:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132845">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/920bba89e2.mp4?token=Em49hQ_hDhS0AbpgsdcNBDXpk-sE6y9tIiteEyBvttaGmAnv8qCjWltjiK7Lk5R3l_WCr2kxn0rqxv5FrkRtQ1B8qjl_-8MxFXjf03G0RTci0xbN36oUI2wa_I3n3Sw22GHrBH46hx1zC6ZWz6-qwuPzInPFauRGKebISkpAoW6VtfqUBGejuKfxz_Fc-WTvX9msPI-Ilgn3AZopuryySxkUZt5lUqllAH_KVpYJ6d0PrPp7K9srxB7YM9migHPBPF1dyI6DslJjvVV_kTscObw4zBxxcFGHf-QnGQU5zlPMuGJUdRkrLFgXTpwAChouP_gjZ_5erUNTnd7KnaF9sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/920bba89e2.mp4?token=Em49hQ_hDhS0AbpgsdcNBDXpk-sE6y9tIiteEyBvttaGmAnv8qCjWltjiK7Lk5R3l_WCr2kxn0rqxv5FrkRtQ1B8qjl_-8MxFXjf03G0RTci0xbN36oUI2wa_I3n3Sw22GHrBH46hx1zC6ZWz6-qwuPzInPFauRGKebISkpAoW6VtfqUBGejuKfxz_Fc-WTvX9msPI-Ilgn3AZopuryySxkUZt5lUqllAH_KVpYJ6d0PrPp7K9srxB7YM9migHPBPF1dyI6DslJjvVV_kTscObw4zBxxcFGHf-QnGQU5zlPMuGJUdRkrLFgXTpwAChouP_gjZ_5erUNTnd7KnaF9sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هیچوقت قدیمی نمیشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/132845" target="_blank">📅 17:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132844">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
منابع دولتی پاکستان به خبرگزاری آناتولی گفتند که
پاکستان و قطر تماس‌های جدیدی با آمریکا و ایران برقرار کرده‌اند تا دو طرف حملات نظامی بیشتر را متوقف کرده و «طبق توافق» به مذاکرات بازگردند.
🔴
یکی از منابع نزدیک به روند میانجی‌گری گفت:
«پاکستان، همراه با قطر، با واشنگتن و تهران در تماس است تا دو طرف را متقاعد کند که خصومت‌ها را پایان دهند و طبق توافق به مذاکرات بازگردند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/132844" target="_blank">📅 17:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132843">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54633b65fd.mp4?token=ZclJ85zl3mzhyWMStUNW_uhPB8OeBnwN7JkBcI203-dJwBt6hxOIGUpmzJLR4r8T8omddY9_J3hzh8l3UX-g8REfLJdf0DDM3c_g4K0Wl6aAiuWQSad5DuBLGxbj-WhF0iE9bA4t6fIrg44DFPvEnirL1-dDKDKGHbHmmDuXfGl0sUsCP-PnXPMEIuGTpJfsuI_V0Tn0-uSOYTRUNweUrvZTgIE6BxaTTCnaCEZox4jUBfmhDh_VpqUlS6iCVFhHuXMdqvGyvj9aksr0xaftCO7vDAZWEC-OdY7dFsE4FBkU3_8sQxcV8V3MvNLzcaNvhicAjvsWwGgbC1gabk-wsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54633b65fd.mp4?token=ZclJ85zl3mzhyWMStUNW_uhPB8OeBnwN7JkBcI203-dJwBt6hxOIGUpmzJLR4r8T8omddY9_J3hzh8l3UX-g8REfLJdf0DDM3c_g4K0Wl6aAiuWQSad5DuBLGxbj-WhF0iE9bA4t6fIrg44DFPvEnirL1-dDKDKGHbHmmDuXfGl0sUsCP-PnXPMEIuGTpJfsuI_V0Tn0-uSOYTRUNweUrvZTgIE6BxaTTCnaCEZox4jUBfmhDh_VpqUlS6iCVFhHuXMdqvGyvj9aksr0xaftCO7vDAZWEC-OdY7dFsE4FBkU3_8sQxcV8V3MvNLzcaNvhicAjvsWwGgbC1gabk-wsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری گنده گوز شبکه سه:
به همه مقدسات قسم من اگه بتونم، خودم میرم ترامپ رو ترور میکنم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/132843" target="_blank">📅 17:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132842">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
تانکر ترکرز گزارش داد:
احتمال از سرگیری محاصره دریایی ایران توسط ایالات متحده بسیار زیاد است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/132842" target="_blank">📅 17:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132841">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
منابع پاکستانی:
میانجیگران برای جلوگیری از حملات بیشتر، تماس‌های جدیدی با آمریکا و ایران برقرار کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/132841" target="_blank">📅 17:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132840">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIgHwe7YUEJIHLVfM6MfJu4dvxLY6zBuJRWRFWNDltzCo-1qr5lxscn8dOKCGegj6S9npJrvLVsScXa-K32asURt5juzy-rPQviQkI0OWW0LqgJQw1HPPF34r9uIic7IeeRuMMJfRP7rvv3VNq-RMkY9op-E1Xr4WJhxhLbucrSLmwZvnPDNrnXE-c1k58W4YyaPea4Y72LQ6SZtIh9tqExnXzNATEI5LqtfUFVtypBKdgH7CR1CTVAbbimpy2cvkvNFKeIkEDLtLgu7fKuvnLPvd37-VLAyuyoe5U8-ljh19ZVokOukDqze3Av_vT70YtVHjWZomdyQuXaYx8nQeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار عبدالهی: بزودی قاتلان آقا یعنی ترامپ و نتانیاهو رو میکشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/alonews/132840" target="_blank">📅 17:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132839">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سپاه پاسداران: مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی الازرق اردن با ۱۰ فروند موشک بالستیک در هم کوبیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/132839" target="_blank">📅 16:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132838">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693aef909c.mp4?token=d9YZkq_m4MQB1sUO2lzZ2YFFQE-o-BVkpGw9FUssuMD89jzbULj0jSCaGBu6u2lBXXuGuTD8k78qg4eSHabwrxTiSU4VgopdQ1onw685KDQODvPhi44nJI0HOcO11bL0En1QG0GEfn2x3oQ1jQbDx5G1T0AKHGJGnymcVfOYkZ9vTvIhDXrTSZNn1mY91I3pIEuDC7aJLa0y0x64mXSrKpwLNxOvlj3-8wMuuSigQm2We7FVlVDrwf2jjAvYDfJ-yatI0B0XlAJuopTWuvMNcdL4duikPDkiOG5JxmCuOI2L8QHdURDkkhiQI9OVLNeORE3qJlsy8rzOL009Lzf_ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693aef909c.mp4?token=d9YZkq_m4MQB1sUO2lzZ2YFFQE-o-BVkpGw9FUssuMD89jzbULj0jSCaGBu6u2lBXXuGuTD8k78qg4eSHabwrxTiSU4VgopdQ1onw685KDQODvPhi44nJI0HOcO11bL0En1QG0GEfn2x3oQ1jQbDx5G1T0AKHGJGnymcVfOYkZ9vTvIhDXrTSZNn1mY91I3pIEuDC7aJLa0y0x64mXSrKpwLNxOvlj3-8wMuuSigQm2We7FVlVDrwf2jjAvYDfJ-yatI0B0XlAJuopTWuvMNcdL4duikPDkiOG5JxmCuOI2L8QHdURDkkhiQI9OVLNeORE3qJlsy8rzOL009Lzf_ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/132838" target="_blank">📅 16:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132837">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ابوالفظل بازگان: موشک‌های تاماهاک حدود ۲ساعت طول کشید تا به بیت برسن و چون ارتفاع پایین بود همه میدیدنش اما کسی بیسیم نزد که حداقل آقا رو ببریم زیر زمین
🔴
حتی ماهواره‌های روسیه هم دیدنش اما چیزی به ما نگفتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/132837" target="_blank">📅 16:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132836">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/763cc26dcd.mp4?token=WySulxYQN7yLazOmI2y7qoocUIkJTR-U0ajZc_oGFRmvICuZ6bBRKYD3jSqPFaI_9cvQHx6JV_i-uBG_QwcmlaXDdeJKl7WlaMq-P66PXyCVTJl6S7rjhgnC5W83XLwyiLGQjwQ3ICGDqATK-9N3h78wanDkpwVRcV1u_BAtAi2ntCd1rnpJvgFZ6_fSVnbNwVjRzR0Cn0D0wuB1_CHcC2vM5YuAlr_sQJcwDPx5vynAcOTOKS-ESj_47Bbv5arnRfLOIUholO8gWbXdNkMrNA3M-sZnp9-0zoVwVVDwI9OyrbQHd2hR_diPEZKKnxuyCKtoGHgwarRfkOjHuDpfWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/763cc26dcd.mp4?token=WySulxYQN7yLazOmI2y7qoocUIkJTR-U0ajZc_oGFRmvICuZ6bBRKYD3jSqPFaI_9cvQHx6JV_i-uBG_QwcmlaXDdeJKl7WlaMq-P66PXyCVTJl6S7rjhgnC5W83XLwyiLGQjwQ3ICGDqATK-9N3h78wanDkpwVRcV1u_BAtAi2ntCd1rnpJvgFZ6_fSVnbNwVjRzR0Cn0D0wuB1_CHcC2vM5YuAlr_sQJcwDPx5vynAcOTOKS-ESj_47Bbv5arnRfLOIUholO8gWbXdNkMrNA3M-sZnp9-0zoVwVVDwI9OyrbQHd2hR_diPEZKKnxuyCKtoGHgwarRfkOjHuDpfWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
احمدی نژاد : بابا داره بهتون فحش میده،یه مرد بین شما پیدا نمیشه پاشه حداقل بگه خودتی؟!
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/132836" target="_blank">📅 16:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132835">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfuFoRNVx792deIpSuUCI01S80w5xMp6OHUEUsFbMfT3J-xyr_WzcNN-dNRaS1O267PB6edB2zRjpxn0DsZfY_xSaLLhhfiohpN1rqhIgYPj7Vf4lE5jYPHE9tNU1RuA3PFmP9--uRlcw4wXmGDgpVCAHtdf1L8XTR5_owZU7KEX-MiBlWI1qX3J9f6U4LpU54Awqbyn2_c8xL6n2MjWETsrKZnRyg8Vlw5kfSoG5ZKrETnalw91_g47azHHtHC29dRifOufWOfjhecftR1Q7Gu3id8mQG6MYqcBE367UUPoBz3TPmtuKHa2X211ylaagCjJ7pna4Y4NOZKjbLymyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کنایه سخنگوی فارسی‌ ارتش اسرائیل به ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/132835" target="_blank">📅 16:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132834">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22231a0a4.mp4?token=sM8EdH2FM10Cs8pZhASR5Ntj-OCaCt2N7ggiAZBI2bTwnuZ3VP2HsK3fQIQfV_hFggiO799Sd6HfKAzAft2Tg8khYy5fQeb_UmewgAFQ-lG6-QgyMRnT7Rlon6M4ekY8bGKBcmQwPANvhEKAC2g__j-Xbw2G3Dg6fumZ5qkG3C5KJqu0buuW6Mfux1RUJ4nxXjR5H_VAsYzTAQ8Chfa_gtyfoHFWYKpvsaCDgEdmnqpAFe72pCuxG1iO4vYc2Po3uDFe95UQ0JF4rbkwTNjD6D99HtbnumPe5aa3irj6R2xz-jinBX5RgquokdJg5jIigpN_vItEvsVQOoL4wEiqyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22231a0a4.mp4?token=sM8EdH2FM10Cs8pZhASR5Ntj-OCaCt2N7ggiAZBI2bTwnuZ3VP2HsK3fQIQfV_hFggiO799Sd6HfKAzAft2Tg8khYy5fQeb_UmewgAFQ-lG6-QgyMRnT7Rlon6M4ekY8bGKBcmQwPANvhEKAC2g__j-Xbw2G3Dg6fumZ5qkG3C5KJqu0buuW6Mfux1RUJ4nxXjR5H_VAsYzTAQ8Chfa_gtyfoHFWYKpvsaCDgEdmnqpAFe72pCuxG1iO4vYc2Po3uDFe95UQ0JF4rbkwTNjD6D99HtbnumPe5aa3irj6R2xz-jinBX5RgquokdJg5jIigpN_vItEvsVQOoL4wEiqyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قدرتنمایی
نیروی هوایی ارتش تو مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/132834" target="_blank">📅 16:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132833">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">روزی مردی مغرور، سنگی بزرگ را برداشت و کنار چاه آب ده ایستاد. مردم پرسیدند: «چه می‌کنی؟»
با خنده گفت: «می‌خواهم کاری کنم که همه از من یاد کنند.»
و سنگ را در چاه انداخت.
آب چاه بند آمد و زندگی مردم سخت شد. سال‌ها بعد، صدها مرد دانا آمدند؛ طناب آوردند، ابزار ساختند و هزار راه آزمودند، اما هیچ‌کس نتوانست سنگ را بیرون بکشد.
پیرمردی گفت:
«یک نادان، سنگ را در یک لحظه انداخت؛ هزار عاقل، که گرفتار بیرون آوردنش هستند.»
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/132833" target="_blank">📅 16:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132832">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423eb34be5.mp4?token=PEB-TYjeveGjtT2PEvoHvRK1Roz22q1GWQTMZhsyDRIiD8Wh1BvjRfVzRr86cK5eeCuBCCqSClLISDdzCSo_HWogxa2iQVbZUGpGMWqNr04aI7xlbxS3ul-rWCsE_gSJwyz3VspNpW5dNOGOOkp4fLy_2d7DSjlrutydWHPXq57ONcgD4vjxaPc-wZbLyspMfLPAZ1U1qdYcIJkxVCsy-XC-Vr02VpYVXeNR_8dMBfnKChwIensN3EJkhxsHDtgijuUEvsdkBGUiUE7qkrl0tPa3YV4oLpeCfWKnh9QoJdRdaaK4TLBCB80S9ieDZCZlHH5DQ3W3oC1YqzdMQ_iYDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423eb34be5.mp4?token=PEB-TYjeveGjtT2PEvoHvRK1Roz22q1GWQTMZhsyDRIiD8Wh1BvjRfVzRr86cK5eeCuBCCqSClLISDdzCSo_HWogxa2iQVbZUGpGMWqNr04aI7xlbxS3ul-rWCsE_gSJwyz3VspNpW5dNOGOOkp4fLy_2d7DSjlrutydWHPXq57ONcgD4vjxaPc-wZbLyspMfLPAZ1U1qdYcIJkxVCsy-XC-Vr02VpYVXeNR_8dMBfnKChwIensN3EJkhxsHDtgijuUEvsdkBGUiUE7qkrl0tPa3YV4oLpeCfWKnh9QoJdRdaaK4TLBCB80S9ieDZCZlHH5DQ3W3oC1YqzdMQ_iYDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: حمله به ایران مانند برداشتن سرطان از بدن شماست.
🔴
اگر سرطان را از بین نبرید، خواهید مرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/132832" target="_blank">📅 16:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132831">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
خلاصه وضعیت فعلی از علائم شوگون سالاری هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/132831" target="_blank">📅 16:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132830">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a8caad7c68.mp4?token=NaKNMW46uvyFKPPx72fOKD66pNwqjeKEE64MkW0zhwN47wsorL4e2-O0e_xBRCURmZrCMH4XMXO3qNG7AqvhpYToZpI_Hjdh37fz_jLnivgPz-8GPg5k1Z6T1Hq3I-jHOJrerpzdyIy3UkHlsuQ37QlUU7loQ_CuEL1KxFmYFLdaRwhKJwjCIaU8IqGSv9J2hxBakF2IAYre2B5cpk4LBaUoot6VrBbraFhFBiMCb0hBWFbu3NYFkQUywWnkdBam8Ds4hy4OiNneHYiBLE6m4rxKJxmD-giodOyLDNrXZDw41VSpFZo3xcrIMD8ucf5qPNB88HsEKZ2cPnZUKUudqw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a8caad7c68.mp4?token=NaKNMW46uvyFKPPx72fOKD66pNwqjeKEE64MkW0zhwN47wsorL4e2-O0e_xBRCURmZrCMH4XMXO3qNG7AqvhpYToZpI_Hjdh37fz_jLnivgPz-8GPg5k1Z6T1Hq3I-jHOJrerpzdyIy3UkHlsuQ37QlUU7loQ_CuEL1KxFmYFLdaRwhKJwjCIaU8IqGSv9J2hxBakF2IAYre2B5cpk4LBaUoot6VrBbraFhFBiMCb0hBWFbu3NYFkQUywWnkdBam8Ds4hy4OiNneHYiBLE6m4rxKJxmD-giodOyLDNrXZDw41VSpFZo3xcrIMD8ucf5qPNB88HsEKZ2cPnZUKUudqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
علی مطهری، نایب رئیس سابق مجلس شورای اسلامی ایران، ۲۴ مه ۲۰۲۲ (۴ اردیبهشت ۱۴۰۱):
🔴
وقتی که برای اولین بار وارد فعالیت‌های هسته‌ای شدیم، هدف ما ساخت بمب هسته‌ای بود.
🔴
اگر می‌توانستیم آن را مخفی نگه داریم و بمب را آزمایش کنیم، موضوع تمام می‌شد.
🔴
از آنجا که قبلاً شروع کرده بودیم، باید تا انتها پیش می‌رفتیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/132830" target="_blank">📅 16:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132829">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
بمب اتم اگه بازدارندگی داشت که مسکو الان زیر موشک نبود! ۳۰سال پول مفت رفت تو صنعت اتمی و آخرش با دوتا بمب نابود شد و چند نسل هم سوخت و کشور وارد چرخه بحران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/132829" target="_blank">📅 16:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132828">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f696affe3.mp4?token=CBWU-0gKXw9bTfdhyO9eUd4QDcOwIJsiRd0me79N9xGJShSta4xB8kbGO_T4h7gxf_v4yheQRvx9fuYklaCAPDXPRdpe2hjB9Ggtb_wVLSzGFE8Szce_m9NYWpk1JLXtQe5cLZbvUIExlp4H29j_ny_XKdvfn5ElQoxUi7o58-slfZyEBc4RTnS5P7NMMW8UoefxQ9OicCRJChhZWE6gG9EkLFW4MjMBQO3sFJDo3OjUeiiyTBUcyXPZ2G3klrfS5tI72rOnyL-oTaED_r1XSKps-zVhJUdCWaS0NvICka6XbDH7zoarY3v7qZsmoD-wUfMG6k9tV4aZ7fl6L209-JQwTPt3VVmddqa4fUpGVoq8CLqUZopmOt0QEN7VCca39GpkwS-NKCfFQFktsL1hXvSh7MgLUrqSx3yEz1FRmE55NfB0O7ZFqNxHW1rrNCEyW0v-5_FeQAJDNpDrMrp5TgozTNvdGNB13Eu6I6IJZBsv88hSZ4AIBXichWYD2JQSiwCJE6dJ_HDyQkpj86gamLTpqffYT5cEKARHVex_7yJ6HGY6g5xMik1SU5-wZxdT-yHdXPq-hdB8qd9lK83fXCNUdmqzrDbdMmOKkj8i2JAePNztyY6bdThZHSY5CAFY0s8H85hfu4Jc53aCrnLkNbterYf2HENpXE8SDDiMarw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f696affe3.mp4?token=CBWU-0gKXw9bTfdhyO9eUd4QDcOwIJsiRd0me79N9xGJShSta4xB8kbGO_T4h7gxf_v4yheQRvx9fuYklaCAPDXPRdpe2hjB9Ggtb_wVLSzGFE8Szce_m9NYWpk1JLXtQe5cLZbvUIExlp4H29j_ny_XKdvfn5ElQoxUi7o58-slfZyEBc4RTnS5P7NMMW8UoefxQ9OicCRJChhZWE6gG9EkLFW4MjMBQO3sFJDo3OjUeiiyTBUcyXPZ2G3klrfS5tI72rOnyL-oTaED_r1XSKps-zVhJUdCWaS0NvICka6XbDH7zoarY3v7qZsmoD-wUfMG6k9tV4aZ7fl6L209-JQwTPt3VVmddqa4fUpGVoq8CLqUZopmOt0QEN7VCca39GpkwS-NKCfFQFktsL1hXvSh7MgLUrqSx3yEz1FRmE55NfB0O7ZFqNxHW1rrNCEyW0v-5_FeQAJDNpDrMrp5TgozTNvdGNB13Eu6I6IJZBsv88hSZ4AIBXichWYD2JQSiwCJE6dJ_HDyQkpj86gamLTpqffYT5cEKARHVex_7yJ6HGY6g5xMik1SU5-wZxdT-yHdXPq-hdB8qd9lK83fXCNUdmqzrDbdMmOKkj8i2JAePNztyY6bdThZHSY5CAFY0s8H85hfu4Jc53aCrnLkNbterYf2HENpXE8SDDiMarw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طاهری، مداح :
الان من شنیدم که ترامپ اومده ترکیه، همین بیخِ گوش ما، الان بهترین وقته؛
🔴
یه آدم با خایه و جیگر دار میخوایم که نماینده همه شیعیان بشه و  بره انتقام همه‌ی مارو بگیره از ترامپ بگیره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/132828" target="_blank">📅 16:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132827">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7b657271.mp4?token=Q5YuzMTMmdEAnXafUDHH6pgB8Ro9aqeawPyTQxaP5WxqrfrGhvMKDVurQ0EWdJPOkxrp9GIIVM4crC70sRxuTDE4-GXibVjDpbiA9O1dqk-Q5y6vOcgkmAbBkPhw1ru0yEdW1Lpgt0lvw1siUi8l3z5kTnMk95yfRB41FiRB0bmiPxTY3AZvAKoMmAm5jWdi7zdJbnK_YDEQ_5mRe1jBDjkCHanPFtnOedkHs1gOKLaMyPdpD1K-6TFlSkElmUIHBJwiqdJDDsEAREGjdRLlbCpXD6keHcu5WgodiOAqPTW1bOb2jp2x3fOOxQiSfGuxZE77rgpZQ-tmAwFcqL-gMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7b657271.mp4?token=Q5YuzMTMmdEAnXafUDHH6pgB8Ro9aqeawPyTQxaP5WxqrfrGhvMKDVurQ0EWdJPOkxrp9GIIVM4crC70sRxuTDE4-GXibVjDpbiA9O1dqk-Q5y6vOcgkmAbBkPhw1ru0yEdW1Lpgt0lvw1siUi8l3z5kTnMk95yfRB41FiRB0bmiPxTY3AZvAKoMmAm5jWdi7zdJbnK_YDEQ_5mRe1jBDjkCHanPFtnOedkHs1gOKLaMyPdpD1K-6TFlSkElmUIHBJwiqdJDDsEAREGjdRLlbCpXD6keHcu5WgodiOAqPTW1bOb2jp2x3fOOxQiSfGuxZE77rgpZQ-tmAwFcqL-gMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از مراسم تشییع در مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/132827" target="_blank">📅 16:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132826">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
خبرنگار حوادث: تو تبریز دو تا پسر نوجوان ۱۴ ساله توی بازی کالاف دیوتی باهم رقابت میکردن که این بازی تبدیل به کل کل میشه و بیرون باهم قرار دعوا میزارن و اونجا یکیشون اون یکی رو با چاقو به قتل میرسونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/132826" target="_blank">📅 16:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132825">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
واشنگتن: چین در حال خرید دانه‌های سویا از آمریکا است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/132825" target="_blank">📅 15:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132824">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e0d425be.mp4?token=AnThp3jhL0YxrhtVrVoojoGw7ZlC1dfj2BrmQc1QUcQgPH-qnPR1U5F4-Y_J8KxDfu8e2nhPG-kSraJSMJsnoR1f3FeHZTNoUYKrNZbXDduUyQeNj-nmqGHqYa73FiavU-w6UFwOyAelYdthvLqHUVLOMkzHDhwQelTYQ9gDTcoYIIkheknLwOzLsbv7twb08F3BfZRJEio0xEt3bRpKzL7T5p-kpRsc8cfiHXrbjI8TE9OVZKn1XS9M49XJorRIiJH4sLR1uu2Ox462bB7LRagSigKDuaaccp48NDLRxX20M-Z7WKN8NYEmRAcFtSs-SPqAc-BDcYVGwuoG3_c9nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e0d425be.mp4?token=AnThp3jhL0YxrhtVrVoojoGw7ZlC1dfj2BrmQc1QUcQgPH-qnPR1U5F4-Y_J8KxDfu8e2nhPG-kSraJSMJsnoR1f3FeHZTNoUYKrNZbXDduUyQeNj-nmqGHqYa73FiavU-w6UFwOyAelYdthvLqHUVLOMkzHDhwQelTYQ9gDTcoYIIkheknLwOzLsbv7twb08F3BfZRJEio0xEt3bRpKzL7T5p-kpRsc8cfiHXrbjI8TE9OVZKn1XS9M49XJorRIiJH4sLR1uu2Ox462bB7LRagSigKDuaaccp48NDLRxX20M-Z7WKN8NYEmRAcFtSs-SPqAc-BDcYVGwuoG3_c9nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو:
شما باید ائتلاف‌های جدیدی ایجاد کنید و روابط جدیدی را توسعه دهید، و من همین کار را در حال حاضر با هند انجام می‌دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/132824" target="_blank">📅 15:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132823">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در پایگاه آمریکایی «ویکتوریا»
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/132823" target="_blank">📅 15:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132822">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از فرماندهی مرکزی آمریکا (سنتکام): طی دو روز گذشته، بیش از ۱۷۰ هدف نظامی ایران را در جریان حملات هوایی مورد هدف قرار داده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/132822" target="_blank">📅 15:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132821">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCGZVq_xPAvXFTvgcOTrIHfaNlIw64y1wQlM3pr-sV4jaWtnReMn930BSuQhyAgE42QU250g4GyT-Y0Htn6Xjge15wf1mXucUTbnpWaS_uRflfrRjCjmgYt3aBzhedZLbvf8zpDS2dAHiTENqCPEfmFeTIvBpKBxR8h0M28bbGgA_89nzJZv-_ypn652r1jwli-6h4kuoixPjY4cPHDfUgi7lJlALHZe8ZGjsimHaoYnXS7JjwDOFg_q4ziSgpAf4OSpgmBvBQMUSfsbwi1JtDXsrbx8E2Yex_XkaFSpz0EJLLgNn3-VpTqFn3umpKW0T-GETaODUH7yZQHgJOSfPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
7 سوخت رسان آمریکایی بر فراز آب های ایرا
ن
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/132821" target="_blank">📅 15:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132820">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وزیر امور خارجه بریتانیا: ایران باید از ادعای خود مبنی بر کنترل مسیرهای حمل‌ونقل دست بکشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/132820" target="_blank">📅 15:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132819">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
فرودگاه اسرائیل بسته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/132819" target="_blank">📅 15:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132818">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vbj_A3M9S_ZOFsxQd_qpOtIEgEQV6A3oevGyCWn6T05LLx0fv0gBYEHQ_gIJ-x2zXd1waBq8_t35Q4XB7aWJY7Pi5GtR-l1MIByxptSi_IZg_glU9q17pHD82XyiiDLrSR2iZjAi--BrYc1afApfKqzai9w4I7d1m_GTB2EBTu0MKbvcP5MqMc3uMWjYjqyypiFFY9cyZKQrpSsANpq8DLsBQVI-4TbVI1aFvOh4EL94gHN9IbTfvnMX3e6ox9WZAEzgR2-thTXQkWXa_QyiW6oiSL9_kiG29mUbcpxOmd9cad2bBvYltjaQMq44qx0NTY4ldIhD06Wu1bgfw6actA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منتسب به پهپاد شناسایی در آسمان زاهدان سيستان و بلوچستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/132818" target="_blank">📅 15:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132817">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
به گفته برخی منابع چند هزار نیروی رزمی و تکاور ارتش و سپاه هم اکنون در نوار مرزی غرب کشور با شمال عراق مستقر شده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/132817" target="_blank">📅 15:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132816">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPLp21AdOekmt0wmakgfK9Do3CLrDQQvGV3gS_tujIAdvYhlq1EGn715qoJ7GNSikKm-6k2045QCSX7npDWO39t_9lLUFX1uOJQtyQ5fDZ2xAIHFzBtluGq8zUT9-1kqcfDtFA0hd7LhwLQmB6M_ml9QbEobFizEsO1V4a0x_RK6UIzoGPXH2vPbCS2-TMhdrEucftEQ1s_-P0EkKedFFeL_U6s5fIHVo5XjiKHHWOZwPOWkDtrks_copY6PUkpZ5_shYpAAFozIGep3QHc7v8PyiphKr1ielG5MWpQ6VP-z_Ps6Yb19vrXzBPEQHl47ssDELYqBw-Lz3ys-EM_38g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سپاه: در حمله سنگین آمریکا به استان خوزستان، سه نفر از نیروهای سپاه پاسداران به اسامی ستوان دوم پاسدار حسین عموری، سروان پاسدار سعید توکلی‌زاده و بسیجی محسن نجاتی کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/132816" target="_blank">📅 15:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132814">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9bc31d407.mp4?token=MWaN93jPMi2J8YtXZ6QruCV4shwayGOYpahqEuELBQ9mpbvtFBRUDt-hGqfUNqDbl2TPhEoWFyaUmJxqoFJM_6rI_igw9kEPQbgmzGCYTzG2mXOO5xCNFLnfausg3O0boVhUzPLaBFN9EUC4y8odH4iEgxtpv65-4X7ftwHGr6LfmgyviS5zMaUYOMAxkIS9N-Hy4OYMcm3x7UuynnX5i1rDcRQrL9_rrDU4c4a2zQomhc2omxL4EEnVavNuk2wgfIphfec5V5lW9yGgUPAsWiN7PCp_SNXXF3tCEXAMISVeyfFnEPwffjWs2P9iDloGBL9egHHqdQABuFfUG1av2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9bc31d407.mp4?token=MWaN93jPMi2J8YtXZ6QruCV4shwayGOYpahqEuELBQ9mpbvtFBRUDt-hGqfUNqDbl2TPhEoWFyaUmJxqoFJM_6rI_igw9kEPQbgmzGCYTzG2mXOO5xCNFLnfausg3O0boVhUzPLaBFN9EUC4y8odH4iEgxtpv65-4X7ftwHGr6LfmgyviS5zMaUYOMAxkIS9N-Hy4OYMcm3x7UuynnX5i1rDcRQrL9_rrDU4c4a2zQomhc2omxL4EEnVavNuk2wgfIphfec5V5lW9yGgUPAsWiN7PCp_SNXXF3tCEXAMISVeyfFnEPwffjWs2P9iDloGBL9egHHqdQABuFfUG1av2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیکوس دندیاس، وزیر دفاع یونان، گفته است که این کشور "تمام تلاش خود را" خواهد کرد تا از فروش جنگنده‌های اف-35 توسط آمریکا به ترکیه جلوگیری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/132814" target="_blank">📅 15:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132813">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3ad1cdad7.mp4?token=sTVFO6wDZ2fvwfG8nCgVSolHjZ1avJQeGvgho2TmvYwaxpCPYGa-UHlvy3YgQRaBjYF9P2eUSnB_pYKiFiGjYWQXJ388upoWRXHfottc9r4Q07MF7CdqayhVtqlzd4Yo8lLjr2Ae_4P8ObRx5WH1O5tPShAF9BbY4O-rqbl-miwfw2urYZfDcXdmWczMtUJhGowUm2uhlcKwXdJ7k5cKjWp_jy_KLIVBLN8oNNImVN1tM-OMCqDW4KlkM-ExSLZgZIA27F7cc6gk-MDD74G8fIDEV3-vAKPlqtEKYZtVcVPFSLLmvKjaLFE_zUeNw9R9JrOUv6_ks5MTFEmqP0-gdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3ad1cdad7.mp4?token=sTVFO6wDZ2fvwfG8nCgVSolHjZ1avJQeGvgho2TmvYwaxpCPYGa-UHlvy3YgQRaBjYF9P2eUSnB_pYKiFiGjYWQXJ388upoWRXHfottc9r4Q07MF7CdqayhVtqlzd4Yo8lLjr2Ae_4P8ObRx5WH1O5tPShAF9BbY4O-rqbl-miwfw2urYZfDcXdmWczMtUJhGowUm2uhlcKwXdJ7k5cKjWp_jy_KLIVBLN8oNNImVN1tM-OMCqDW4KlkM-ExSLZgZIA27F7cc6gk-MDD74G8fIDEV3-vAKPlqtEKYZtVcVPFSLLmvKjaLFE_zUeNw9R9JrOUv6_ks5MTFEmqP0-gdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک جنگنده F-16 آمریکایی پس از دریافت هشدار مبنی بر احتمال آتش‌سوزی، مجبور به فرود اضطراری در یونان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/132813" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132812">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJocCRPtgoM_g4haPjda36Nk4qVWb-7X-er3OMrphxULTVbThwEUwIzRAepxQgAKXpbVBJmkheIca0QcSvreWzgXt53hAsSw7hrZnPIa1xOqbAVfDNxByTlY6yOwg_E4KTwkGlbu7c_lRUZRHPvjWzaQph3iK7vywU3_dRAltBuYRCl2OFPmLNOqIBdOQONHg-e_RJIRP8T64-CyPx8WORBl7O6L7T_89LbKZlclscmw4-a7ue_ISvZOI3VTe8LiALOW5FEDW46wh3M0U8fE-GUL0vDYYdYebu0_eHth7nOFWgYymS0XQZJxqBwyrUmth32RGXZxTWaQ3eqEZk3H9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیانیه سپاه: ماجراجویی ارتش آمریکا و مداخله در تعیین مسیر تردد روند بازگشایی را با اخلال جدی مواجه می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/132812" target="_blank">📅 15:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132811">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
مهر: شیراز امروز مورد حمله قرار نگرفته و  عکسا فیکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/132811" target="_blank">📅 15:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132810">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
قطر: حملات ایران را به شدت محکوم می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/132810" target="_blank">📅 15:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132809">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
اردن، حمله‌های مجدد و شدید ایران علیه بحرین و کویت را محکوم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/132809" target="_blank">📅 15:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132808">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
دو موشک دیگه از ایران به سمت اردن شلیک شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/132808" target="_blank">📅 15:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132807">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkaVLJTT-re3ARmr7HkVeXK2qqN6A6JgvxitBg5CI6LsMYPz1HZ21q2ibOOQfIzWeBS8I1IKw-XfSLecPIxar3DpfPo13IooO4WbQHkyfBoCZfsMUA_OzEPUUrdebYJK0FY7ogfX0ey7RctmybYQVLi8RVDcDyLw5zbNNNATfV8pjynF51rooZrjciO_HML9f9gsUHAkVi295-Z4-bHeuXyHQWH6u0Eaa_AVgjt47FGatd9XqY59OA1szNJ-GylOaeFYOw748NM0h8eC1RFoGJg0v1stGbNvfiGDdNb9QnSeaP6D2e97yX0vRKrBPH3edht4BRdLyIsKqNdjzAWMnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گشت زنی جنگنده اف ۵ نیروی هوایی در مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/132807" target="_blank">📅 15:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132804">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FTaEVwcF3Wh0-wHb0mRe1PKVRHPN-a0wPKTAxOI3TOX6aNjakH1qP8tHrNvUI8-XHyMDqZdn0PzXNv9US70r2keXW91IZW_pAmHZqg9P7M96wXLcG78tVzWkzPDynDEj716B7PZUsjDOxtpzDy1Vn_j1GdjPwOx32VqLy6ZdT5OtV7ul8UWMT9xZhqzEIpv_iYxonzkPW6hb_kqnjbMhqhnY8ZZoiShqmk8mNaDKGOphZWlR0ExK0nrjZWNl7qAe1RpJvnf-WkSQ0yD1Yhr0mlPcz4BDAqMaTjUJFkVTbV-q3D-tZgUXXjsrCjvxIH7LBYv-jh2SdrSO68QJsDVYMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WlIttarHFBYpoNr5glMtFsqk6QZS7qAwK_zpDkiMX2viQWEZCBaNvCIPbgL8rNv3ELsf9FSu0NhBXlSgvUylfHl-g7J52pFxzpewDsJygHfbjZtw0uIKZjh04ODvg2Bqb6-PulqJAGqbSzmEQpjwaJaHsAbwPmeVr5HbW3ykiYyMFFOodQh2eRRfGsnC0z6Mt-iU_zWEo0mLH9YeMs23J7Vk3NH1E1EJdAPJnk40B4MD62EL5O8I-48Dvffrfxt5uBIwq1cxBPfywhakzyOPIlzs0RCwSY4xnUBKbWD0Q_8wyW0HUCf7DdAaoVhuG5_F12BtQ-kty-_PbuPy343aRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
شرکت هواپیماسازی متحد روسیه (UAC) محموله‌ای جدید از جنگنده‌های چندمنظوره Su-30SM2 و هواپیماهای بمب‌افکن جنگنده Su-34 را به نیروی هوایی و پدافند هوایی روسیه (VKS) تحویل داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/132804" target="_blank">📅 15:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132803">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4BibQ6kTD5GQ4vmKYVp1VJrPZvUUmFjdcbukpnD53NluQhqKYe1g4tx6tJXDvLMO_DwpLfMyZVbnUveaZeXFii100hYCT_jHUvMXDT4LZStO0O2aFFMjQxO84zRe9saTYsGGogFMB8N566Kk46u6dgdiAkQUePjvnP-_XgDUHCPIPY460ujYZF5cvm1A7tHDm6FlQIXLjUPdtgOoBl9105IM-E4NMKcP1172x5yqKRrS16chf5NWR4Spkm37A-BCltzUA1QRhm2tu5TfXtGKaYDfulvzN8AmlbQpel-X-bkNzyUspdRrJQbhxTmBLXAORyU5_fhCnTsrxzjmRWwgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ داره بصورت زنده از تنگه هرمز گزارش تهیه میکنه برای صدا و سیما
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/132803" target="_blank">📅 15:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132802">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فوری/ آژیر ها مجدد در اردن فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/132802" target="_blank">📅 15:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132801">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2e74886f.mp4?token=LnLrX3A9WzqsROEHoBxUEjXbOyOHJyfJ0QBaCLQrcihl6sG4sKwK7_I2poY6XWCgfRjeDLK_ZYxuTxxgH1Cc0-xNcEZiT6TZwdpgG1pEUVvnTVcMWIWmF3qCCHxucdZgSf-3JoUE9dEjahN6tbkYdKUz9oXNswQj4af-rXNfxEdHKdw_uEgscv8IUGOlJ3XifPBX8qFbbA8Z3WWpPYlL-jczTc63HD9quVzjhs5jEWq8DzzZevWfMj6SBe12zOeMVCJSY0k0d8MFc8JNfXxRFuVE6YZ8hVjSn1mpux6yGLpgCxXnGIEnkRXT5WW-D1KJgrhDCsGctVgqwebm7UFwPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2e74886f.mp4?token=LnLrX3A9WzqsROEHoBxUEjXbOyOHJyfJ0QBaCLQrcihl6sG4sKwK7_I2poY6XWCgfRjeDLK_ZYxuTxxgH1Cc0-xNcEZiT6TZwdpgG1pEUVvnTVcMWIWmF3qCCHxucdZgSf-3JoUE9dEjahN6tbkYdKUz9oXNswQj4af-rXNfxEdHKdw_uEgscv8IUGOlJ3XifPBX8qFbbA8Z3WWpPYlL-jczTc63HD9quVzjhs5jEWq8DzzZevWfMj6SBe12zOeMVCJSY0k0d8MFc8JNfXxRFuVE6YZ8hVjSn1mpux6yGLpgCxXnGIEnkRXT5WW-D1KJgrhDCsGctVgqwebm7UFwPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / هم اکنون وقوع آتش سوزی در اسکله عسلویه
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/132801" target="_blank">📅 15:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132800">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
مجددا صدای انفجار در کرمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/132800" target="_blank">📅 15:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132799">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
حریم هوایی سوریه بسته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/132799" target="_blank">📅 15:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132798">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
نیروی هوایی اسرائیل: وضعیت حالت آماده‌باش در سراسر اسرائیل اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/132798" target="_blank">📅 15:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132797">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
سازمان ملل در پی تنش ها بین ایران و آمریکا هشدار داد و ابراز نگرانی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/132797" target="_blank">📅 15:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132796">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در کرمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/132796" target="_blank">📅 14:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132795">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
توقف دریانوردی در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/132795" target="_blank">📅 14:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132794">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار های عظیم در اربیل اقلیم کردستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/132794" target="_blank">📅 14:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132793">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
نیروهای مسلح پادشاهی اردن: ما 8 موشک را که از ايران به سمت پادشاهی اردن شلیک شده بود، رهگیری کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/132793" target="_blank">📅 14:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132791">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d7aAAcmoZa0aXZdNSt7mssMm89eL78N7tkzxRJnqTlrqNOFSZZYNOw1C8Q1nPsBqp7OSMda3rVwH0vj7MxRtYaCYE0E9v1plfKXP8XW62Dz0RLX2QStpmo14NT7UwomP57pRptqsFkWeNXuJESFIMXHDXfugi64NO0NkH-W7KLfyjsGxW5BWp4PGD-bRtq_T6SQRwmrJaMiJXl9X8cv0sLOxE6kpLpAQP_G6CO6C72WbljJ34OteGsrAh6te_MFOyl7m_qC9cyUrJM_J4X-KCPPekAJoeNlyqE1dByUJNYdyN3VpFxOr51MzqX9oL9sQUv_M8fochwCsZOOm1gUKUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uazd9YT_ip0gXck3scldtBlWX_A3yxsHhKkCXT1C7GexNEK7CitR9KppxvssHblyCQEFVsewObaefxjNKkvyxDN4p9kK4SIkuQ74suO2eCwl0DwzyBVVA9ADKV9gt-ur7cS3ZEfojQWjI6jx6HcQLsfhkWXLgGYUa_ONoPx5ZxbLPE180SmQqhfac2fNuaN96ZKCPv51U0XrYgVgoKeDsFP8dkfMxHkx5X0-CciP2atXPBHraiisbEPYjWtc15QV1JDFF5254_Xja8aIaAs-flIS-4vko30aWHKkaksu7kofOJa1QB3tQy7kOIRYFylIqLwxZ14Pc_Z6NlGvMX13xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از حملات آمریکا به عسلویه
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/132791" target="_blank">📅 14:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132790">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
عربستان: حملات به کویت و بحرین رو با شدیدترین لحن محکوم میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/132790" target="_blank">📅 14:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132789">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
صدای آژیرها در پایگاه ویکتوریا، نزدیک فرودگاه بین‌المللی بغداد، شنیده میشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/132789" target="_blank">📅 14:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132788">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293667c56d.mp4?token=C6lJwO0fGWnh8G8SKV-MaPnMfJ2ki2OzUNzh-J7UmTHAhPpsW8dpGZbM899GcHYa5AZznJ2-z_chZUpgavKseKgMREiRB-E7L8COeP96DPrmz-O_QCGZDsLfjP9jGcsqmYtiJWbncxed7oX5hjmoDkr5HwRnoybBci31QVa0OWaBDYNCIuIPg406sIlJ6nGzg6x3oYLm7ctHa1T5sQh_O8EMY6JrFXkAgxsyoRXxORztfL6N8UYvn6PAGfcFXrb8jWSRBlmqXD87HgDm2vTm_-AVIV8ozX82L-x8iiZYOQPaq32Wt80EveR9fheo4KxDJfhjpJF8-yUiYqry5Vg_7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293667c56d.mp4?token=C6lJwO0fGWnh8G8SKV-MaPnMfJ2ki2OzUNzh-J7UmTHAhPpsW8dpGZbM899GcHYa5AZznJ2-z_chZUpgavKseKgMREiRB-E7L8COeP96DPrmz-O_QCGZDsLfjP9jGcsqmYtiJWbncxed7oX5hjmoDkr5HwRnoybBci31QVa0OWaBDYNCIuIPg406sIlJ6nGzg6x3oYLm7ctHa1T5sQh_O8EMY6JrFXkAgxsyoRXxORztfL6N8UYvn6PAGfcFXrb8jWSRBlmqXD87HgDm2vTm_-AVIV8ozX82L-x8iiZYOQPaq32Wt80EveR9fheo4KxDJfhjpJF8-yUiYqry5Vg_7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک ایرانی در آسمان اردن در حال حرکت به سمت اهداف خود
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/132788" target="_blank">📅 14:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132787">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
گزارش‌ها حاکی از آن است که حملات هوایی اخیر ایالات متحده به اسکله تجاری و ماهیگیری در منطقه سیریک، در جنوب ایران، منجر به کشته شدن ۳ صیاد و زخمی شدن ۱۵ نفر دیگر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/132787" target="_blank">📅 14:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132786">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
پرواز گسترده جنگنده های نیروی هوایی ارتش بر فراز مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/132786" target="_blank">📅 14:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132785">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
دولت اردن : موشک‌های ایرانی رو رهگیری کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/132785" target="_blank">📅 14:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132784">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
گزارش های تایید نشده مبنی بر برخورد موشک و پهباد به سپاه ثارالله کرمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/132784" target="_blank">📅 14:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132783">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
خبرگزاری رسمی اردن اعلام کرد که آژیرهای هشدار پس از شلیک موشک‌هایی از ایران به سمت این کشور، فعال شدند.
🔴
این خبرگزاری همچنین افزود که نیروهای مسلح اردن در حالت آماده‌باش کامل قرار دارند و برای مقابله با هرگونه تهدیدی که امنیت اردن را هدف قرار دهد، آماده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/132783" target="_blank">📅 14:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132782">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
منابع عراقی: آژیرهای خطر در پایگاه آمریکایی «حریر» در استان اربیل در شمال عراق به صدا درآمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/132782" target="_blank">📅 14:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132781">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gt041_4lprsbmn3OMO3pq-2zA2DUsI8dGzS6kJzyyjDdR9fkKdeZYV_6-spKbQldsGK8vT5JV9ONHzamsgBqwxb1VDuFsRFUM3mYWeQMCq64otf4LJL3bf3KRg2YFQB8iKylaHI7T6wEmZQQkzcrLs0nqJraLgEiMwtIVDbMvg3blG-WKDhXQBP5A-kGg9IzTW5qUdO0bcBL3vUeM-UVf8vwVML-blG25iGIFTWzsLVSYl9sl_i3kcWocspSnwpy0JRx9FaiHrcJlZnLL8membU1YkbJrcSceELXDYH1AWXRdccEiNzc7cVrsaUBhmAacZE3k64kkE7nLKEftMd2Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار وال استریت ژورنال: علیرغم صحبت‌های دونالد ترامپ مبنی بر پایان مذاکرات، این احتمال وجود دارد که به زودی به آنها بازگردیم.
🔴
پویایی اساسی، بیش از هر چیز دیگری، تمایل به عدم تشدید تنش است. و من گمان می‌کنم که این موضوع در واشنگتن شدیدتر از تهران احساس می‌شود، هرچند که در هر دو مورد صادق است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/132781" target="_blank">📅 14:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132780">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رسانه‌های اردنی: یک موشک مستقیماً به یک مجتمع صنعتی در شرق اردن اصابت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/132780" target="_blank">📅 14:39 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
