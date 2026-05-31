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
<img src="https://cdn4.telesco.pe/file/laAKNE_p4yaKYZSjCUOmJ3eHF5zWKTmnHslrGdPDpQPly5ytgmbGh-R3V_l5asTXjesJgvV6b7MxJkPcCTvbnHx3BqZlInrJWTQdRbop1DzY0GYT_fzWTpgfYPRROQBaVs9FiVEcf0xlV7G-9xOX3SvZ-fP4prt-MrKmho5pZ2xBv2rP3y7vGMccBLSn_e4nmJf7mBcPbGg3fNdxE_jyedu4Xqc6ooKIYPmkN9KQSBmZX9scyf0lKMnQuEJhMRmC9X0baoi499Z2zfqI4jKmlX72Q9Y-sjgVLcmo_xL_FdaTu-3_WPE6RFKqAo1EBvRkNDpAnXpY73oQlMhvHeGIFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.08M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 02:21:55</div>
<hr>

<div class="tg-post" id="msg-655127">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b32ef18ff5.mp4?token=lRqC5cEXgSg7OtHDulJNmV8gSRGUkZvGOG2S5mOmKWrB5KSqju8V5rPLSOJQ9puvUigXWklc2n3t3tawSxSnS6xIg0z0gal71ahPqltzu3kz5dCx5QQoRbwmcSto4F7yMD16QLq-Kg5LRKBfFlv5Vua-crz7vm8R4rt7WLD0G_O20yGDUly418w6OswFR-5kB9us9CYO_BHdFJ5MWHRnu6BXQAEEY9DI0FJjveUyvsgxr2ylx6XbCkvVANSk4vexyRDxjoftfvi6Ed-Pq3k3ukTohFTkBaJvtz801nv059_1uLo9gxPxyqoNBJmEyRElaT-nc0IYe1mKAGO1d2Fo6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b32ef18ff5.mp4?token=lRqC5cEXgSg7OtHDulJNmV8gSRGUkZvGOG2S5mOmKWrB5KSqju8V5rPLSOJQ9puvUigXWklc2n3t3tawSxSnS6xIg0z0gal71ahPqltzu3kz5dCx5QQoRbwmcSto4F7yMD16QLq-Kg5LRKBfFlv5Vua-crz7vm8R4rt7WLD0G_O20yGDUly418w6OswFR-5kB9us9CYO_BHdFJ5MWHRnu6BXQAEEY9DI0FJjveUyvsgxr2ylx6XbCkvVANSk4vexyRDxjoftfvi6Ed-Pq3k3ukTohFTkBaJvtz801nv059_1uLo9gxPxyqoNBJmEyRElaT-nc0IYe1mKAGO1d2Fo6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#آراپیس
( آرسکا )
💊
کپسول مفاصل آرسکا
🔸️
غضروف ساز
🔸️
ضد درد زانو
🔸️
آرتروز گردن
🔸️
ضد دیسک کمر
🔸️
درد سیاتیک و ورم مفاصل
🔸️
کمک به درمان بیماری های مفاصل
🔸️
تنگی کانال نخاع
برای اطلاعات بیشتر عضو شید
👇
👇
‌
https://t.me/+U65oequC0vhwZpKY
‌
ثبت سفارش ارسال عدد ۱ به شماره تلفن
09146342317</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/655127" target="_blank">📅 00:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655126">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvrZ0uBk-QMle3bXnrm7rskz8Zl1TloIsZGAekY8XckvEZu_-997cNcwwf68o1J8keMWd6Qqe_N8ax_owA_YARTZYFytGYjKXD-3OExqR7IgWGb373p9kSYgzbS2fgPf54sr4h_RKLtiYsaQ7epDMNMAUEb6C-0Oku4TigWDpZCF_-TxIzEXGnZQS_hKtJbYJumHx-LXI_EFBZ_-YudDMACTO8hujl31OrgxhI6-vvvE756Nx08NLTPV4Frbg9IpDsARo81jcwf8UyCGmhBTOESMgQ0MVspfnGYQsoCCkbkXqUnOmEWCDNK4gcHWjvogCf2XGPpBgotrBPjyImPuHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/akhbarefori/655126" target="_blank">📅 23:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655125">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار شدید در اربیل عراق
🔹
منابع خبری از شنیده شدن صدای چند انفجار در حومه استان اربیل در اقلیم کردستان عراق خبر دادند.
🔹
المیادین: مقر گروهک تجزیه طلب «کومله» در اربیل هدف حمله قرار گرفت
.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/655125" target="_blank">📅 23:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655124">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLuFNjdi47EC7X6eaM8z4q_4-YqWyRHANLVJyMwVnjiSnsDFQSSddFAYb4lSzhe2DnY6mgLsEtsQDCACV0NMfXnn2q7ikvbEPRsztbOfnvGqS9mX0Mg5FC89dYVewRoEIYrXUAcVZ9irZi2Ew4w7Exugg6rbFDXsiTZ6qWOZqvx3zq-b3MeIK9f8E4Pe1UPjv2F6-OpCnF6QzOZRIMy8OvdI9BdHWQO8pnQOFt_lA9E4OLGZ7fi8r23fsI4rA-yxRNvKEWnfACTfvfcuTBMNlJhSR1m1lj7sGqy8YuTR54cM1mf-FxSXvLAu8iwQyDcsUHHsn7F0eSiC77ZdXW696g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
با یک بار ورزش در هفته هم می‌توانید لاغر شوید
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/655124" target="_blank">📅 23:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655123">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/889980ef31.mp4?token=i_E89N3wQ2mL3BWqbnDfDMTwwpYRm_jQNSKvnYtDj9MWdBHTJctJAg6tv1NtABYBxZs9-gAy1pjA-Q4FIePJC7ogekY7r0wDICyalHzwDuYB7tP-FbCgYAwzPwMEAIfjSKRBYM-8MwI0etLwBrf3OF02-pzCi8sWjpY2tMEPm9au4OfYK6ZuhG80616wP0D9BC39infqpLJI6JNat45GFFlwCxZVhzwq1XZkQlJdEKnoQzWyHF4sdCurKByMnkW209s0BYG9TDb82jra148KH36l7_Fx_TSthagp-ZnlaAPl29prYACFRlmsq4a7Ui5h4_tC09Iquml6ufx3pZa56g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/889980ef31.mp4?token=i_E89N3wQ2mL3BWqbnDfDMTwwpYRm_jQNSKvnYtDj9MWdBHTJctJAg6tv1NtABYBxZs9-gAy1pjA-Q4FIePJC7ogekY7r0wDICyalHzwDuYB7tP-FbCgYAwzPwMEAIfjSKRBYM-8MwI0etLwBrf3OF02-pzCi8sWjpY2tMEPm9au4OfYK6ZuhG80616wP0D9BC39infqpLJI6JNat45GFFlwCxZVhzwq1XZkQlJdEKnoQzWyHF4sdCurKByMnkW209s0BYG9TDb82jra148KH36l7_Fx_TSthagp-ZnlaAPl29prYACFRlmsq4a7Ui5h4_tC09Iquml6ufx3pZa56g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با رشد سرویس‌های اعتباری در ایران و افزایش تمایل کاربران به خرید قسطی، انتخاب پلتفرم مناسب اهمیت بیشتری پیدا کرده است.
توی این ویدیو، پلتفرم‌های فعال این حوزه را بررسی کردیم تا ببینیم هر سرویس اعتبار را با چه شرایطی ارائه می‌کند و کاربر در نهایت چه مبلغی پرداخت می‌کند.
هدف این ویدئو، کمک به انتخابی آگاهانه‌تر، شفاف‌تر و کم‌هزینه‌تر در خرید اعتباری است.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/655123" target="_blank">📅 23:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655122">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Va1FZbJYTorSTad2pRgzBTXMhGdAO58PNi3Tnx7vz0LpwnwhshgjKSV49wtZ6Mgem-_FcitgLyvOiQosncZSKNKR-xSfti0Op7-uj7CXFkHouCObc8a7s4L0zvcLFJshrJSj1cYn0SUItHSTmfbffR7MKYYBYWXzjtsLj4GZji0qaLwz-jIecsZyJIP8JjsYllPrZJn15We0euZ6XVRhfrSFg78v4_zisPv94ksn8jkcAT_xD0wJ3sLB1LL9N3KJrrTED4Ci8ngNBaSg-gF1AffEUgoPhcooOLNjDcn0QSliBxXt63wecNN7k-68sNJeMqK8trV3mQIw-NbGjlyCVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رژیم صهیونیستی قلعه بوفور را تصرف کرد | قلعه‌ای بر فراز جنگ | اهمیت استراتژیک بوفور چیست؟
🔹
امروز نیروهای نظامی رژیم صهیونیستی کنترل قلعه بوفور در جنوب لبنان را به دست گرفتند که این اقدام نشان‌دهنده عمیق‌ترین پیشروی آنها در خاک لبنان در بیش از ۲۶ سال گذشته است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3219361</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/655122" target="_blank">📅 23:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655121">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pzlz7qKhKdHbFkVBBuIkwJooUPQjxgACjjBc-9LRAcPrJY3JNoEGuHbG3-cvkXvYg4_PaT7L7CT7MMv9H0-TZLRYqZpGMCGBoYGL9ctyd_vUFy0xmdnIE3K-Qwg5MwHWCqLglhArx10q8atjVRUeBbpXeiz5zGKRY6MkI2seIk7WoAVAhyUQi9nBASXOrXnQxLCZxS0Qa9p_zh6eYlDGZ9FLQiS95Ust7-kRjU0Jw0MxBtgXQ6-790Pk0baf_IiJiU_7LrKu1UUwZ7tCOMLB8SDB0QdQSdhM0kxzQ8NNYfheTeKskX9wi1Yxw6-vfZHEJKBqYZlP3KeBF1LRIrhCCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخست‌وزیر دانمارک: جواب ترامپ را واضح دادیم!
مته فردریکسن:
🔹
رئیس‌جمهور آمریکا درباره تمایل خود در مورد گرینلند بسیار صریح بود.
🔹
تمامیت ارضی ما باید محترم شمرده شود.
🔹
معتقدم که اروپا باید کاملا مسلح شود و کاملا بتواند از خود دفاع کند.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/655121" target="_blank">📅 23:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655120">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromایران روشن</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90222c673.mp4?token=hRZh2jW2LiZc8l9g5Xq9npCCktkmRqjJ-As4V2Pd3n1mP6JuWrZGriHKx0XyzEDJR_AI3e1r_wMqqdfAxN5YxFjOOonux8zsr2DtCSvZ97_uPAFvS9QY9cYQ2t8Tko8zqxBddOM1CtIHnlyk0ekb5PjHSt27ryBJn9B-ezCNiB2vH5JaDo-PjsygkitvtlR99ANqQjqZqI0iNr0q6tK3yTcWPF3kg-Z9xiOqOlAWly8cjMLAejOl9H4WjhejLSLWG9Cb8urVYAHcGuh62r6BjkbDjb7mRVJiV2q2IDenR2EtBiMdX4w_VlDSfZMN6fo9EnJmFA7kcTZP1VQ-0ttwHEJuYB-SwemQn_32JlkgFJCqx9MAK6EVIYPFM9TmBFid3h4a_1ID8fUgWDu-ofism5Yw0Li4tBm2D4PWml49pIoyWYSlUiUHBjXS0Vs8GElJ5nYHRMH3L1e24D1t1oaAj4szQi7BOjd92RjbEp0OkeS5UunP_2rIjVai7tekff5gfC4zC0AmFV8g4R4vK5ozz_grdn75ES6Bl0mQLBh47QEBt_C8uJUI82BgadAlSiC9BHb3viUI4lWWhR9S7SKxNgBKHJu_HRoZGpB6tPeVwYBHzTeFQdwwEvjEh5ArC7n4lIyogcc-5jQJsvKjXSM06-SydMYMCamBWUcvMXFc6do" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90222c673.mp4?token=hRZh2jW2LiZc8l9g5Xq9npCCktkmRqjJ-As4V2Pd3n1mP6JuWrZGriHKx0XyzEDJR_AI3e1r_wMqqdfAxN5YxFjOOonux8zsr2DtCSvZ97_uPAFvS9QY9cYQ2t8Tko8zqxBddOM1CtIHnlyk0ekb5PjHSt27ryBJn9B-ezCNiB2vH5JaDo-PjsygkitvtlR99ANqQjqZqI0iNr0q6tK3yTcWPF3kg-Z9xiOqOlAWly8cjMLAejOl9H4WjhejLSLWG9Cb8urVYAHcGuh62r6BjkbDjb7mRVJiV2q2IDenR2EtBiMdX4w_VlDSfZMN6fo9EnJmFA7kcTZP1VQ-0ttwHEJuYB-SwemQn_32JlkgFJCqx9MAK6EVIYPFM9TmBFid3h4a_1ID8fUgWDu-ofism5Yw0Li4tBm2D4PWml49pIoyWYSlUiUHBjXS0Vs8GElJ5nYHRMH3L1e24D1t1oaAj4szQi7BOjd92RjbEp0OkeS5UunP_2rIjVai7tekff5gfC4zC0AmFV8g4R4vK5ozz_grdn75ES6Bl0mQLBh47QEBt_C8uJUI82BgadAlSiC9BHb3viUI4lWWhR9S7SKxNgBKHJu_HRoZGpB6tPeVwYBHzTeFQdwwEvjEh5ArC7n4lIyogcc-5jQJsvKjXSM06-SydMYMCamBWUcvMXFc6do" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جیک جیک مَستونِت بود ...
فِکرِ تابِستونِت بود ؟
+ شُمام
#پیک
شد ..
#قطعش_کن
. . .
مِثلِ ریز‌عَلی ، مثل امیر ، مثل آقا ذوالفَقاری
🕶
#ایران_روشن
💡
جوین شید خوش میگذره :
@IRANroshan_Media</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/655120" target="_blank">📅 23:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655119">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔹
خبرهای داغ امروز و امشب را از دست ندهید
🔹
🔹
پزشکیان استعفا داد؟
👇
khabarfoori.com/fa/tiny/news-3219368
🔹
پشت درهای بسته چه گذشت؟ | طعنه‌های تند ترامپ به ونس فاش شد | مذاکره‌کننده اصلی با ایران کنار گذاشته می‌شود؟
👇
khabarfoori.com/fa/tiny/news-3219292
🔹
رسوایی بزرگ/ خواننده مشهور به 4 نفر تجاوز کرده است؟
👇
khabarfoori.com/fa/tiny/news-3219320
🔹
حاشیه سازی نماینده تندرو با آیه ای از قرآن و تیتر «چه کسانی شایسته جایگاه رهبری‌اند»
👇
khabarfoori.com/fa/tiny/news-3219141
🔹
گزارشی از جدیدترین اخبار گفتگوهای ایران و آمریکا و احتمال جنگ در منطقه
👇
khabarfoori.com/fa/tiny/news-3219088
🔹
ویدئو‌های جذاب را در آپارات ما ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/655119" target="_blank">📅 23:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655118">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بانک مرکزی: رقم وام ازدواج مشابه سال ۱۴۰۴ است
.
🔹
هاآرتص: هدف اصلی اسرائیل اخراج ساکنان نوار غزه است.
🔹
قطر خواستار فشار جامعه جهانی به اسراییل برای پایان دادن به حملات علیه لبنان شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/655118" target="_blank">📅 23:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655117">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPCwt-SySIG9_t7mz9H8Nar9VVAEX717tQuDEu1r8cGaiTmxcu3aL-U1_V14vVeJKH1DUsu1pCJmaI_CGhshpc4MRc3OROEAk0yqs4VH8upBjp46azwwxOnIO9JPyVMEjzkVvEPNDzyvqeP7L7XV4G3EmDyL8D0Y2vaZ8gQnsEUlt-CdLg_Pxyu6OnQJqdX51IkwfOezOGDXnF37WsaIrjZMeBve_Lv1meOngXpCKDYvjxQRI8eyq9Znhue7u5qm48-6XT_iIZmrruKBafhCXO0ebBV0XrVmAT6JAPiVrrS-PhWnpitxH1HWeseyKhKGxZ2d2qpuVSDyyChaN9ILBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تفاوت تصاویر رادیوگرافی و ام آر آی و سی تی اسکن به روایت تصویرهایشان
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/655117" target="_blank">📅 23:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655116">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0ben2Wez0v3ylN-sGuLqtQLv2V380rxvvFOGB1kF2cnPK_wh4LarAm_ilZNkAgCWwo4W7fas-Sk3qBfuR_fAOHM1vB9EnGwLwh_eFpEYRtrUP5CAphh1hPWTk346TjaOzsfLU-cmuax1rrV42oO2pfe6xiCShtyuH9a4KLYnwBKyAFL6OWMBQnw4enmR8H_dOqK4HOm6mXWePbMXwO8Ez31sP-SyBWSgkP54sRC0gGray7rKU9TzIz2mTV5uQuFMeQaV1yS34Posc0wlcVbizSC7a9dLke27ETEWsyoOB52XiWQOulosZC3pT2ObxkXPK4MtoMS_iks0y7jzIO4eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با مردم حرف بزنید
🔹
اظهارات امروز مسعود پزشکیان درباره غیر عادی بودن شرایط کشور، تداوم فشارهای خارجی و ضرورت آگاهی جامعه از هزینه ها و الزامات مقاومت حاوی این پیام روشن است که کشور در مقطعی حساس و پیچیده قرار دارد. رئیس جمهور تأکید کرده است که عبور از این شرایط نیازمند همدلی هماهنگی و مشارکت همه بخش های جامعه است؛ اما تحقق این مشارکت بدون گفت وگوی صریح و شفاف با افکار عمومی ممکن نخواهد بود. مردمی که قرار است بار بخشی از این دشواری ها را بر دوش بکشند، حق دارند از واقعیت ها چالش ها و چشم انداز پیش رو آگاه شوند. اکنون زمان آن رسیده است که پزشکیان مستقیماً با مردم سخن بگوید
🔹
هفتصدوشصت‌وسومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/655116" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655115">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paWVB6om1rfMBRyWCBQAVPDKZs_4E06Ln2RGL9-5mk8Bvmil1aTOJVjg-mdpnua_twDDAJeOK7q9fV6ig2zz9tsRTx7kBUm1WfC-ZcjoPeduNJzF0YQafjm7EblSdTzzniSs4IUyAverdRqIYzmSV3Qf3tAdTaBzLmHrs6i5-0ZXIuLyrzLHsasGQc_5SUZfOFK_ljGPzzS6rOt3YZ52RGmKwItJMBDlRK2QdwEnWTOJWiNZrhnn8lpVQxMJFhiUafmyRaGOq4aLY4W65KgRzJZyuRCbOIknHQ8kqh2vW6vs19RLkh7cOnotAwhEOxY_lokOO14sWx_T4J7m0oIQQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر معنادار در یکی از تجمعات شبانه
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/655115" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655114">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
امحای کنترل‌شده مهمات باقیمانده از جنگ در کنارک؛ صدای انفجار فردا شنیده می‌شود
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/655114" target="_blank">📅 22:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655113">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0PsJ9_8LGhzvqHHCHHaW2Ik2UWTVaaZza5l6OAqMJaxtIw_C52j6zJKG402gvGAkLSwayw2wNTqEMvnplXgbkh0wfjxkToc7v9EMNYMER404ueaaWiVoHtqX6ZufT1vyJhPDdUHaRurlYydwtGicGgP0AqJKBV5NDV6ys3uBnceIID4OQCklsZ0iwvghY-pc95y4PcalrEGuiwLNSmJP3mIGzuri4iVhQH8Lh_yIN8bahXyKABpRZZaVBwpM1xrt1x3dYcdSrDFp_6Qbij38LctfGkum-ojFNsQu_Bme7PXYXZq-_WgRMIorjalHYGt-MSEM6Ny43ZraKNeiBa3mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
عید سعید غدیر مبارک
به عشق امیرالمؤمنین علی (ع)، هدیه‌ای ارزشمند برای عزیزانتان انتخاب کنید.
🤍
بارگاه امیرالمؤمنین (ع)، یادگاری ماندگار از عشق و ارادت به مولای متقیان؛ هدیه‌ای شایسته برای عید ولایت.
جهت ثبت سفارش با یوز زیر در ارتباط باشید
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
📍
ویژه عید غدیر
@ghararshop
@ghararshop</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/655113" target="_blank">📅 22:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655110">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rDHHAyyBLNd3fPNyMagCPpaJatd3UsaI2mfPsptEalyucewxbzV8HNiQCDaYPjVzwX5dHgwAqZr_dNwql94Lq2RxTlUtHG6TdyfF0fUCBUelXljnIQQtg9RPiKI8zj-RtBgAbPD0_j6EGBJLAd8W2gevO6c2Q7NWMlTbNuP7xKLeQwrOFxfOxC-8EeJPVMb-1IaLPECa1AYaZNhlOt7khvoMjMriopzR85FHT3eYbYfAbrf9dZD-1sbK1ZslG9l8UYQQ7fIMzUbam25SnLklqr7XEWgeXB8Y83lyph02dcL0kpgPQD3TNuitd2l8Tizt35TvWvjCwSMSS0gtFc7l3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OrYYl2ZF61lYGamLr5nHsK8zePpzNl6tMfFYTLx8so-IJ6hNMeKFY8zyG4wiFjQYjiGqNMNbW-8mArO8sGK5wByNSB28cnMAzIxoKn3Ya66VM4z-GgWTKx04TG8qWA3M6Z2UT0Aj2TeZaOB3mCnD-o_qeu5dtQ779r5alo8un2qRsFO_v-bTCAH_OAh2knF2u5Gi7XPderX7qjKwZdKpuuP1X_1kze_UpULoSD1iUFkUOuLkV78Gn6e3nW_yba9OhsiHkY3QlG8ij6jKnEhg3sildMSXrF5A4uq9SEUqKA4Zhl67xWJLEAUno3F2ngenPyrVCHY-gl-zXWN6tz8mEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ioBr9-vodL8ad7WruMQuJVuaYQY_Ak8mLaESlLMn8xZxpH7xbGBsJhL5Tr5aMT7hgQA6jR2y_Sp8TGykrxfZwxXBtEqF5YOas00zISCG46U8gWvGZmMa0x4yp8yShM1zVOpeXI9l3tKYcVbFhXvbqDq4MsxTMWYtahBS0Uz0zokCbf_PgoFE7AzvgfLXHIqjbGZDh841xuI76MeCJBNL4iYZmt188zl0qyi96YgjFNjDxly7t8iJCz0-FfaHSBqDvJPt_uPlUuZbbP27EAFKcaYHB5n_D-X1GzU4g9uy6baspTGhAZK8HgIADYiDY3BwwVRGjHE8vLxQUszfDWB_Ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر هوایی خیره کننده از ساحل معروف برزیل
🔹
منطقه پرایا دا بالیا در شهرداری سائو سباستیائو برزیل، با نوار ساحلی ۵/۲ کیلومتری، به دلیل میزبانی از بخش وسیعی از جنگل‌های آتلانتیک، اهمیت اکولوژیک بالایی دارد. این منطقه الگویی از تعامل میان توسعه شهری و طبیعت بکر را در نوار ساحلی سائوپائولو به نمایش می‌گذارد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/655110" target="_blank">📅 22:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655109">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
تاج: با صحبت‌هایی که با مسئولان فیفا انجام دادیم، صدور ویزای آمریکا برای ملی پوشان ایران مشکلی ندارد
🔹
فدراسیون فوتبال دارد تلاش می‌کند که سپاهان از آسیا کنار نرود، اگر سپاهان نتواند پنجره‌اش را باز کند طبق روال جدول لیگ نماینده ایران به آسیا معرفی می شود.
🔹
بازیکنان تیم ملی به دنبال این نیستند که در جام جهانی صعود کنند و حواله پاداش بگیرند بلکه با صعودشان به دنبال شادی مردم هستند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/655109" target="_blank">📅 22:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655108">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c108240e5.mp4?token=WDfD5bNNIx7jJZE-6sQSbyObkRyqaltjULf2BWFhl0fSUN-RxGQiu8kSAHKBM9ijueMEpYGQ8Nm8o98YxXFNaKMn0Fjg6prqeKt-Ho5UuvNQ09VrdRhuAmYRKTR0jFtaG3e-g1PhW0t4s7cx2GBoNelBicy0sonIBIQS2jxzDBa1maqWMFeMH4ylqYil08EeaIlGR69oWzhvlG8NwDv4ckcKa5vn_YU3CV-3c9bFFLlqO_KyVrFgY05hHiBWRs1jY2zD15ZzmfSjoPcx4NyB0Em8NQDxnYAmjs3BBFyu4YHI6bRntC7f8xwth-8yHMfU6wt2X6ENmW5jmPAwlKiEUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c108240e5.mp4?token=WDfD5bNNIx7jJZE-6sQSbyObkRyqaltjULf2BWFhl0fSUN-RxGQiu8kSAHKBM9ijueMEpYGQ8Nm8o98YxXFNaKMn0Fjg6prqeKt-Ho5UuvNQ09VrdRhuAmYRKTR0jFtaG3e-g1PhW0t4s7cx2GBoNelBicy0sonIBIQS2jxzDBa1maqWMFeMH4ylqYil08EeaIlGR69oWzhvlG8NwDv4ckcKa5vn_YU3CV-3c9bFFLlqO_KyVrFgY05hHiBWRs1jY2zD15ZzmfSjoPcx4NyB0Em8NQDxnYAmjs3BBFyu4YHI6bRntC7f8xwth-8yHMfU6wt2X6ENmW5jmPAwlKiEUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسرائیل پیوندی با انسانیت ندارد
مورخ یهودی آلمانی:
🔹
سیاست اسرائیل به‌طور کامل پیوند خود را با اصول اخلاقی و انسانی از دست داده. هیچ انسان شریفی نمی‌تواند چنین وضعیتی را تحمل کند. آن‌ها دچار جنون و شیفتگی مفرط به ایده «اسرائیل بزرگ» شده‌اند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/655108" target="_blank">📅 22:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655107">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4XkK2NwiA8HQNeDUozHMYG3BAamW0L4GjWAtnsy5Rxlv1fUxO96IUA66XEMERZKM8IflRy58e7LjiyeH6rR4t6Tu4ktEV-q_QbOL4yuLfLvGvpFp4KQ5zb-XGgXlcz7mIYfiIA8ixgRMOBKDeASm5tS0keRbXNI48f_r9EPfzlX3Jo_bah7mFAi1FJRmTAJUFNB-YyQ7CsGVu43T_614pLMIQFmz1lQEXWvoqAfQVKphFUmoNNaDTDqD9rjv5nXkQfauTlY-vWM5AB9rHnk7LSBWoqT5GA2oJge9XyBSZuidCdeShSseQ1Jq4TOuHmkDAQ8XeNl_rqvTwqzum9SEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خطرناک‌ترین سلاح آمریکا را بشناسید
🔹
بخشی از عملیات و پروژه مهم ارتش آمریکا که در سال های اخیر روی آن سرمایه گذاری فراوانی کرده، عملیاتی است که می توان آن «عملیات تلقین (کاشت)» یا «Inception Operation» نامید.
در خبرفوری بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3219318</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/655107" target="_blank">📅 22:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655106">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ماجرای کشتی خارجی منهدم شده در نزدیکی آب‌های سیریک چیست؟
🔹
در پی درگیری‌های روزهای اخیر و هدف قرار گرفتن یک کشتی خارجی حامل محموله مس در نزدیکی آب‌های بندر سیریک و کوه مبارک، گزارش‌های محلی از تجمع شماری از صیادان و قایق‌داران در اطراف این شناور خبر می‌دهد.
🔹
همزمان، بررسی ها نشان می‌دهد با توجه به ادامه تحرکات نظامی و شرایط ناپایدار منطقه، احتمال هدف قرار گرفتن مجدد یا انهدام کامل این کشتی وجود دارد.
🔹
بر همین اساس، از شهروندان، صیادان و دارندگان شناورها درخواست می‌شود از نزدیک شدن به کشتی و هرگونه اقدام برای انتقال یا برداشت اموال آن خودداری کنند.
🔹
همچنین به مالکان شناورها توصیه می‌شود از در اختیار قرار دادن شناورهای خود به افراد سودجو پرهیز کنند. مسئولان تأکید کرده‌اند در صورت بروز هرگونه حادثه ناشی از بی‌توجهی به این هشدارها، مسئولیت آن بر عهده افراد متخلف خواهد بود./ مهر
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/655106" target="_blank">📅 22:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655105">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
بهترین‌های ورزش سال گذشته کشور معرفی شدند
🔹
فدراسیون کشتی - بهترین فدراسیون ورزشی
🔹
تیم ملی فوتسال - بهترین تیم سال
🔹
پژمان درستکار سرمربی تیم ملی کشتی آزاد ایران - سرمربی سال ورزش
🔹
مهدی طارمی - زننده گل سال
🔹
مبینا نعمت‌زاده - قهرمان فردا ایران
🔹
هاجر صفرزاده - بانوی پارالمپیک ایران
🔹
علی‌اکبر غریب‌شاهی - آقای پارالمپیک ایران
🔹
زهرا کیانی - بانوی ورزش ایران
🔹
امیرحسین زارع - آقای ورزش ایران
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/655105" target="_blank">📅 22:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655104">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb367f0e92.mp4?token=MmwZ4D3_9npQZxbq_OVrBwdZ_VX0og6-0G5dNkYXciC2RnpOa-mYnC8CKYHxRpxg6PV8WCsor15lVBVnYOdcT4ssg8eMyDmal-6NyOFvWSnxBQK41SShWWAulSWYXnwKt3C8vEkgasnKQ57YTy_L0M0vQyobIv-RSeMcLmzHyPZleGxV4lK_IhCJWJOCjOwQb69EMB1TtIlrqzlRkPdUJy9Of1O59H9GrAJA2EZPsF7R9ah4WQ12sqlOY3IrDKddzWHSTNYxF5WTh5BRnfMUtf_2lz_eXKAOP2WlwdADr8V2V4vWqBMBwRzdeek9O53D9WQ6o5Q9vfD7hq3MPng4aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb367f0e92.mp4?token=MmwZ4D3_9npQZxbq_OVrBwdZ_VX0og6-0G5dNkYXciC2RnpOa-mYnC8CKYHxRpxg6PV8WCsor15lVBVnYOdcT4ssg8eMyDmal-6NyOFvWSnxBQK41SShWWAulSWYXnwKt3C8vEkgasnKQ57YTy_L0M0vQyobIv-RSeMcLmzHyPZleGxV4lK_IhCJWJOCjOwQb69EMB1TtIlrqzlRkPdUJy9Of1O59H9GrAJA2EZPsF7R9ah4WQ12sqlOY3IrDKddzWHSTNYxF5WTh5BRnfMUtf_2lz_eXKAOP2WlwdADr8V2V4vWqBMBwRzdeek9O53D9WQ6o5Q9vfD7hq3MPng4aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طبیعت بهاری کهمره سرخی
🌳
#ایران_زیبا
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/655104" target="_blank">📅 22:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655103">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
کمک فوری/حال این 2 کودک بیمار، خوب نیست
🔹
کودکی ست بیمار و معلول،از ناحیه دست فلج است یکبار جراحی شده و نیاز مجدد به جراحی دارد کودک دیگر نیز دیابت دارد و هر ماه باید دارو و انسولین استفاده کند وضعیت مالی خوبی ندارند و به کمک احتیاج دارد.
🔹
مورد سوم دو مادر هستند یکی از آنها به دلیل سرطان پوست تحت درمان دارویی قرار دارد .مادر دیگر نیز برای جراحی پری آنال به 10 میلیون تومان برای جراحی نیاز دارد
🔹
مورد آخرنیز پدری ست بیمار ،مدتی پیش با قرض جراحی دیسک کمر انجام داده است
❇️
توجه... خیرین عزیز پرداخت انلاین خیریه بامشکل مواجه شده است.. لطفا هدایا وکمک های خود راازطریق کارت به کارت یاشباخیریه واریز کنید
✔
پرداخت انلاین خیریه نسیم وصال:
http://www.nasimevesal.ir/payment-new
شماره کارت بانک ملت : ۶۱۰۴۳۳۷۸۱۱۴۱۶۲۳۷
شماره حساب بانک ملت: ۵۸۹۸۷۷۱۴۶۵
شماره کارت بانک ملی: 6037997599156198
شماره حساب بانک ملی: 0219934010000
شماره شبا: IR310120020000005898771465</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/655103" target="_blank">📅 22:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655102">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwul9i3ioZ3qr4bNLcGv0rS0-AjhGB69VRQqmYXRb-jZ3gu44KEtqnwwacc9QiNCK4XzCygPDQlptXLnhwP5EabQBeBTpepHS9t4TzQzI5QS_W4kiiGJTQrrsWoXKmYGs85HsNFe00GAKxWxIWXeaWjcrw1I5zelHVC_hQoriSYwRUhZzPWSJokKyJR6SzZ6vDaypwSWgYhmuVo6VWKCizcx6W4t4zaJZ9D494PEiJemxVEfkdMp7M4DLW-NQYssQyvLvjm2jkNwK_rx1TAWohSonFDzFOVgA1sM7VCaG49N3nGbp0ggC6uoIHRHYXVHqBrpvDjf9aLB-6QdhBs6WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش سخنگوی دولت به شایعه استعفای رییس جمهور
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/655102" target="_blank">📅 22:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655101">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">مراسم دعای ندبه_جلسه 61</div>
</div>
<a href="https://t.me/akhbarefori/655101" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه شصت‌ویکم
رائفی‌پور:
🔹
0:04:40 محدودیت در ازدواج با آمدن دین اسلام
🔹
0:17:00 روایت شنیدنی خواستگاری کردن حضرت علی(ع) از حضرت زهرا (ص)
🔹
0:35:30 شکست تلاش یهود برای کثرت جمعیت قومش
🔹
0:48:40 تغییر انسان به فرشته با اجرای فضایل اخلاقی
🔹
0:57:40 قسم خداوند به ذات الهی در مورد حضرت ابراهیم
🔹
1:14:20 سرور کل زمین در منابع کتب اهل سنت و شیعه کیست؟
🔹
1:20:40 گنجینه توسل به حضرت زهرا
#دعای_ندبه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/655101" target="_blank">📅 22:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655100">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مصرف برق ۱۰ تا ۱۵ درصد کاهش یافته است
علی آبادی، وزیر نیرو:
🔹
با وجود اینکه با توجه به شرایط موجود باید انتظار افزایش مصرف را داشته باشیم، در حال حاضر کاهش ۱۰ تا ۱۵ درصدی مصرف را مشاهده می‌کنیم.
🔹
مردم در مدیریت مصرف همراهی خوبی داشته‌اند و این همکاری در کاهش میزان مصرف کاملاً مشهود است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/655100" target="_blank">📅 21:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655099">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
اعلام زمان آخرین پرواز حج و نارضایتی حاجی‌ها از اسکان
نماینده شرکت هواپیمایی جمهوری اسلامی:
🔹
آخرین پروازهای حج ۲۴ خرداد از طریق فرودگاه‌های مدینه و جده به مقصد فرودگاه امام خمینی(ره) تهران انجام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/655099" target="_blank">📅 21:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655098">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">از طرح فروش ایران‌خودرو چه خبر؟
با وجود آنکه طرح فروش ایران‌خودرو از روز شنبه نهم خرداد آغاز شده و طبق اعلام اولیه قرار بود تا پایان هفته ادامه داشته باشد، برخی شنیده‌ها حاکی از آن است که این طرح ممکن است زودتر از موعد به دلیل تکمیل ظرفیت به پایان برسد.
بر اساس اطلاعات غیررسمی به دست آمده، استقبال متقاضیان از این مرحله فروش در روزهای ابتدایی قابل توجه بوده و همین موضوع احتمال تکمیل ظرفیت تا اواسط هفته را افزایش داده است. در صورتی که روند ثبت‌نام به همین شکل ادامه پیدا کند، این احتمال وجود دارد که ظرفیت تعیین‌شده پیش از زمان اعلام‌شده تکمیل شود و متقاضیان باید در انتظار دور بعدی فروش ایران‌خودرو باشند که فعلا زمان احتمالی آن مشخص نیست.
این ثبت‌نام از شنبه هفته جاری در سایت فروش اینترنتی ایران‌خودرو به آدرس
esale.ikco.ir
آغاز شده است.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/655098" target="_blank">📅 21:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655097">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
کانال ۱۵ رژیم صهیونیستی: گسترش عملیات اسرائیل در لبنان با هماهنگی دولت آمریکا انجام شد
/ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/655097" target="_blank">📅 21:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655096">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
سد کرج دوباره جان گرفت / پرشدگی مخزن به ۷۰ درصد رسید
🔹
بارش‌های اخیر و افزایش ورودی آب به سد امیرکبیر، روندی را رقم زده که مدت‌ها خبری از آن نبود؛ حالا مخزن سد کرج به حدود ۷۰ درصد ظرفیت خود رسیده است.
🔹
این سد با ظرفیت بیش از ۱۸۰ میلیون مترمکعب، سال‌هاست بخشی از آب مورد نیاز میلیون‌ها نفر از ساکنان تهران و کرج را تأمین می‌کند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/655096" target="_blank">📅 21:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655095">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‌
♦️
عراقچی: ویزای تیم ملی فوتبال ظرف یک تا دو روز آینده صادر می‌شود
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/655095" target="_blank">📅 21:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655094">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-C_e9jPGjpmOnrOkrUBosg3ats5KVWbIXX-n5S3UUk996fJOpI9e40UcEYWspPjf7SBSVN7ISe2aNJ7ntVmJEHbKjvhRpgYKQ5BHUodBO4APIFCKAWJ17jZrju2VFdE3Hqlx2fRY3qD1TEWow9crDq2OUJ7n79xwTMwwUBEjC_2oho2325n8WtflRL8LzNRnyU5OuRVXLTz8H9OBYNbCNOuDwoWCvZIsBhAyQ2n2GVPOgziBsDcJb4nVYF-50j5hK5r8UDJg7Ry6F5-A5SkRVEmMe_Kkk6Jax5HmrWsQxOiUsh8dl7W2RJ5SvYFoLrP4xMP2TmnYOfmYMv5T6iTQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اندیشکده کوئینسی: کنگره آمریکا بی‌سروصدا ادغام ارتش آمریکا و اسرائیل را کلید زده است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/655094" target="_blank">📅 21:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655093">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ss1KLGFMeP7vu5oWDx1SB-H5q_lRXapBA8wY_867UrZ8kc0A8W_FEIDiK7b5-qOq34Z9-3Vu8WIz0s89WVeoFwfccLud9jBBuKV9-HNQrGtfibiHBImGPHKqTeRyk9pRF72s9cgoFTViq6oPS-rf7_1TxJgEGumVJr22yqb4m6HgJBpD0HmGpxIU-Td6AqIXB9xONuFTpqsBmNCOVRuk_-1tK8EThiykgnTlYm0FWdWtWhgRIwyx0OOxgCkO7BjJCnrToGs8UKw2cmvQaJnG_Sy9MbcOoC-ZdWKu_m4wGjLLIlBw8uMYEDdgGYqnmbR5gf0kY-VMFtTA8bM0NgrKVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون ارتباطات رئیس جمهور: رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست
ماجرای شایعه استعفای پزشکیان را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3219368</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/655093" target="_blank">📅 21:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655092">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5910ee62f3.mp4?token=s2s3D9mQ3ZB7IIJYw204LFm8BDH8NOppDqhmCQ9j2yhfeMdiSD8v4iNIyIMk6Vfg5yPyXE8wFpUBCMZQmEmEoKeo4l3Tep-Kjqd4t_AVUvneWpyylAJgvmIttF4yqRqv0HfW2ShfcBPpeBluN4GczJLtprx8yykKVPJle-bvWmViBuFFNgpQbwkARhDrUos-w3HRJj1CFIShuPE-09hG2ZLYRShmsinlSNjeKXNWpsftMkGHTqP89SL_hO1ytRB9-eYZYBjupiHnK50MN_esZtr4kPkh9J_44YYMtQGrH4V9cAaCbpOppkFn5KOH8ltQr_syZ8QaE9BLyfTqeft2hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5910ee62f3.mp4?token=s2s3D9mQ3ZB7IIJYw204LFm8BDH8NOppDqhmCQ9j2yhfeMdiSD8v4iNIyIMk6Vfg5yPyXE8wFpUBCMZQmEmEoKeo4l3Tep-Kjqd4t_AVUvneWpyylAJgvmIttF4yqRqv0HfW2ShfcBPpeBluN4GczJLtprx8yykKVPJle-bvWmViBuFFNgpQbwkARhDrUos-w3HRJj1CFIShuPE-09hG2ZLYRShmsinlSNjeKXNWpsftMkGHTqP89SL_hO1ytRB9-eYZYBjupiHnK50MN_esZtr4kPkh9J_44YYMtQGrH4V9cAaCbpOppkFn5KOH8ltQr_syZ8QaE9BLyfTqeft2hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: قهرمانان واقعی؛ از مدافعان خاک وطن تا تیم ملی
رئیس جمهور:
🔹
مدافعان لانچرها و شهدای والامقام، با جان و اعتقادشان از سرزمین و پرچم جمهوری اسلامی دفاع میکنند. آنها قهرمانان راستین این روزهایند. در سوی دیگر، تیم ملی هم با همه توان پا به میدان میگذارد. نتیجه هرچه باشد، تلاش خالصانه عزیزانمان برای ما ارزشمند و قابل احترام است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/655092" target="_blank">📅 21:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655091">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsjD7TvDN-g6oWyRiT4lLR06h7fKGzgwMdjbpcxY0qPUBQYWYBqH4-Jtmcjnv0JBDnM97MghCRiZzpOA6hxHCAkM5ASeHt0bTDngDt7p9q07nwuFsWGAnKKTMpCEy4jJhgoO2OCYsxDPzpliXcC76pncHhimrPJMKZIufhnV9xG04SmGQeb4NcC8rySQzetK2mgau5EWuCiw0pP8-qULQHcdxPgR7dahDuUtEtcXNhjyUYSeUhejqWjsFqal3TIlDL4RNlhSkrKEif1hMwookBg5SqrrNEYdymOPLhOybNoADrmBXpieHa4rf5QbapDdh11lHfbQPCyRahvY4YUfpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جاسوس اسرائیلی که می‌گوید ترکیه و مصر اهداف بعدی اسرائیل هستند | جاناتان پولارد کیست؟
🔹
گزارش تازه میدل ایست‌ مانیتور به اظهارات جنجالی جاناتان پولارد، جاسوس پیشین آمریکایی-اسرائیلی، می‌پردازد که در آن چشم‌اندازی تند و هشدارآمیز درباره آینده تنش‌های منطقه‌ای مطرح کرده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3219065</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/655091" target="_blank">📅 20:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655090">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
سهمیۀ آب زمزم حجاج حذف شد
🔹
محدود شدن اعزام‌ها به سه فرودگاه تهران، مشهد و زاهدان و افزایش زمان پروازها، انتقال آب زمزم به کشور را منتفی کرد؛ در سال‌های گذشته آب زمزم با استفاده از پروازهای خالی بازگشتی به کشور منتقل و هر زائر ۵ لیتر سهم خود را در تحویل می‌گرفت.
🔹
مقررات پروازی عربستان حمل انواع مایعات و قوطی نوشابه را در بار مسافران محدود کرده است و حجاج در مسیر بازگشت فقط می‌توانند ۴ بطری کوچک را در کابین هواپیما همراه داشته باشند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/655090" target="_blank">📅 20:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655089">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
روابط عمومی بانک مرکزی: حداقل مبلغ تسهیلات ازدواج، فرزندآوری و ودیعه، خرید یا ساخت مسکن، ۴۷۰ میلیون تومان تعیین شد
‌
🔹
بانک‌ها می‌توانند در صورت درخواست متقاضی، سهمیه تسهیلات یادشده را در قالب کارت رفاهی خرید لوازم خانگی ایرانی، پرداخت کنند.
🔹
حداقل مبلغ تسهیلات اشتغال خرد و خانگی نیز ۱۳۰میلیون تومان تعیین شد./ خبرفردا
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/655089" target="_blank">📅 20:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655088">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3278c1f792.mp4?token=OBPPhfKYmqu8PykOrfxJsg244LyE8lf4e7PztWP4POKcUuCC4MWRmNqqIlVmerDdjXnIcwCRL2IFZdd_A57NIWwpNGP5O_iWYfXoYzicueMnFV5A62nfXPFCnomZ_ZSTi4llVM7af1D5LYd9IAcwLPh2NEP7LziIjxBSW4i7olNKPPelA4v7dh4ffqGL9PICIAwlBGhSVksMcED0F2qDr6Gsk4dberP3lzlEt7RW4dgB8BkrubrgTY12AP9B_WHxJyxj__8gSe898GMISjlUSH-AmIiWwgNWCkzXS3Njl9c4jE2EjlFwegtmheTLh_zf7sGZfuMWAE8WeNRyd-Qc2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3278c1f792.mp4?token=OBPPhfKYmqu8PykOrfxJsg244LyE8lf4e7PztWP4POKcUuCC4MWRmNqqIlVmerDdjXnIcwCRL2IFZdd_A57NIWwpNGP5O_iWYfXoYzicueMnFV5A62nfXPFCnomZ_ZSTi4llVM7af1D5LYd9IAcwLPh2NEP7LziIjxBSW4i7olNKPPelA4v7dh4ffqGL9PICIAwlBGhSVksMcED0F2qDr6Gsk4dberP3lzlEt7RW4dgB8BkrubrgTY12AP9B_WHxJyxj__8gSe898GMISjlUSH-AmIiWwgNWCkzXS3Njl9c4jE2EjlFwegtmheTLh_zf7sGZfuMWAE8WeNRyd-Qc2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: گفتگوها و تبادل پیام‌‌ها در جریان است و تا وقتی به نتیجه مشخص نرسد، نمی‌شود در موردش قضاوت کرد و هر آنچه که الان گفته می‌شود گمانه‌زنی است و نباید به آن اهمیت داد
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/655088" target="_blank">📅 20:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655087">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
آمریکا به زخمی شدن نظامیانش در پاسخ موشکی ایران به نقض آتش‌بس اعتراف کرد
سی‌بی‌اس به نقل از مقامات آمریکایی:
🔹
در حملات موشکی ایران در واکنش به نقض آتش‌بس توسط آمریکا، چهار نظامی آمریکایی و سه پیمانکار زخمی‌ شده‌اند، در حالی که ارتش آمریکا مدعی شده بود که موشک بالستیک ایران را رهگیری کرده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/655087" target="_blank">📅 20:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655086">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
یک منبع آگاه در دولت: اینترنشنال، کارخانه تولید اکاذیب درباره پزشکیان و دیگران است
🔹
با توجه به شایعه‌سازی «اینترنشنال»، رسانه وابسته به موساد، درباره استعفای آقای پزشکیان، این رسانه ضدایرانی کارخانه تولید اکاذیب درباره ایران است دیگر بر کسی پوشیده نیست، لذا طبیعی است که کسی شایعات او را هم باور نکند.
🔹
آقای رئیس‌جمهور استعفایی نداده، امروز مشغول کار بوده و برنامه‌های آتی او نیز طبق روال برگزار خواهد شد.
🔹
این قبیل شایعه‌سازی‌ها با دو هدف عمده صورت می‌گیرد؛ نخست: خبرسازی برای کسب اطلاعات امنیتی به نفع موساد و سیا و دوّم: اختلاف‌افکنی و شکستن انسجام مقدس اجتماعی در ایران./ تسنیم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/655086" target="_blank">📅 20:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655085">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مبینا نعمت‌زاده به دلیل پارگی رباط صلیبی بازی‌های آسیایی را از دست داد
🔹
معاون نیروی دریایی سپاه: در برابر زیاده‌‌خواهی‌های دشمن خواهیم جنگید
🔹
رئیس جمهور فرانسه: ایران و آمریکا باید فورا به توافق برسند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/655085" target="_blank">📅 20:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655084">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
آن‌طرف فقط یک نفر بود: پدر
🔹
00:08:40 رؤیت ۳ آسمان و عبور از آنها
🔹
00:16:45 خیره بودن تعداد بی‌کرانی از انسان‌ها به آسمان
🔹
00:29:00 مشاهده نتیجه کمک به دیگران در کودکی
🔹
00:52:00 امکان چندتایی شدن و حضور در مکان‌های مختلف در یک زمان
🔹
00:58:40 درک چهره واقعی انسان‌ها پشت نقاب ظاهر
🔹
01:00:45 فقط به خاطر پدرم راضی به بازگشت شدم
🔹
01:06:00 تغییرات رفتاری تجربه‌گر بعد از تجربه
🔹
قسمت سوم، (فقط پدر)، فصل چهارم
🔹
#تجربه‌گر
: میثم نثاری
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/655084" target="_blank">📅 20:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655083">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a79d39b094.mp4?token=TPbSxz0cluI1KQugS8507l1ahOMCiXhuc_UZidsYpLRa8GfUSKlNwphkcs-TMg2RPr5gUSQEWhSDygFylf9L2IaI9GeUuR6vPazmD0PT9A2DuMivonl2uzzmNY2eT3CLBPDYg2XQCjE_4qeQ5ruczJPgRZ038TON5yTL09A-XTpDEzALz1L3TjJtsvUpOaj2O1h-9jiQvWFmkv8ns4-hJSJVBkp27raemAva_yEK4qfm5_TC0BGrK1pHHiPc1z2ZGrhnrOczCU1OOy2sbQlKOjRdStWwCWIbIoXISr6ul7WEkjyjjGGwTgV1y5ZTmVNMhA1vg6V9gGkF3ce05g-kpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a79d39b094.mp4?token=TPbSxz0cluI1KQugS8507l1ahOMCiXhuc_UZidsYpLRa8GfUSKlNwphkcs-TMg2RPr5gUSQEWhSDygFylf9L2IaI9GeUuR6vPazmD0PT9A2DuMivonl2uzzmNY2eT3CLBPDYg2XQCjE_4qeQ5ruczJPgRZ038TON5yTL09A-XTpDEzALz1L3TjJtsvUpOaj2O1h-9jiQvWFmkv8ns4-hJSJVBkp27raemAva_yEK4qfm5_TC0BGrK1pHHiPc1z2ZGrhnrOczCU1OOy2sbQlKOjRdStWwCWIbIoXISr6ul7WEkjyjjGGwTgV1y5ZTmVNMhA1vg6V9gGkF3ce05g-kpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم روسیه با کیسه پلاستیکی؛ ابتکار عجیب همسر سافونوف در فینال UCL
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/655083" target="_blank">📅 20:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655082">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
انجمن داروسازان ایران: «کمبود کدئین» ناشی از محدودیت در تامین خشخاش است نه تحریم
عضو هیات مدیره انجمن داروسازان ایران:
🔹
علت کمبود برخی داروها مانند کدئین لزوماً به تحریم‌ها مرتبط نیست، بلکه به چالش در تأمین ماده اولیه آن بازمی‌گردد.
🔹
سیاست‌های ممنوعیت کشت خشخاش در افغانستان و محدودیت‌های مرتبط با مواد مخدر، باعث کاهش تولید ماده اولیه کدئین در آن کشور شده و این موضوع به طور مستقیم بر زنجیره تأمین این دارو در ایران تأثیر گذاشته است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/655082" target="_blank">📅 20:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655081">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_7Czlte7gd4P-5M8anSaDSjapum9zgZIlhDiw4zDUY3jqiySxxpNqLR2fPJqDu8jZpALBzMNVZJPF02ARrNahREDZTwz8A5SgcbP-NC3THkni0ehxWIBaTKuoCHtH6863NCXuglQUwRvt-IxDXOPiR9gL8LIJ_sXoQMuew8UzU8BEPEKGZ78HgAEbpsKQK3VxhdFeALQuxXizAnEkFD2Wsb4Bmqmdxw8Y9LFUOpw_wlbPBfd6Djinv2SE5mKd_WA-gXmDMfexydg9IYmVSM5nZVyyTQS429THV3zPJ_6ZLQY-Dc0q6gCEZF7HO_bogDyBYTC6YjS3IQErZvJ4-T_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: رویارویی با چالش‌های بزرگ بدون تحمل سختی‌ها شدنی نیست
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/655081" target="_blank">📅 20:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655080">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d509bd7f2.mov?token=oNzV4lCCUJKUoPphgRaJiDcmmQtN7PaJ2NXCSng8L4AoY1DoxgLLkQBDM5BZdcTAcHqmRg2c5yWVKB_GQI5HuwvAheB7taFN3cLiGxAxW9eQHUl8nicsLW7u81ZX9PsrDCLgFoPxUUyp0MBJD5tT8QHuXPvDh31EyIriC6Nt5zUEx3NROxYWxv8SZzkPC0TQ2M-zhjRiUAHprMVmmrrYsK7qrNCi4Zx03AcCUn3Oo3a8RBa-kzJY6kP5roreHfknsltLj099DfTyRea0wgd2V9kqtflp540Kvm_3cOZxv32IZKhFb0hJdXKPu37gklGm2INhusjt1mjq7wnqx3SFMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d509bd7f2.mov?token=oNzV4lCCUJKUoPphgRaJiDcmmQtN7PaJ2NXCSng8L4AoY1DoxgLLkQBDM5BZdcTAcHqmRg2c5yWVKB_GQI5HuwvAheB7taFN3cLiGxAxW9eQHUl8nicsLW7u81ZX9PsrDCLgFoPxUUyp0MBJD5tT8QHuXPvDh31EyIriC6Nt5zUEx3NROxYWxv8SZzkPC0TQ2M-zhjRiUAHprMVmmrrYsK7qrNCi4Zx03AcCUn3Oo3a8RBa-kzJY6kP5roreHfknsltLj099DfTyRea0wgd2V9kqtflp540Kvm_3cOZxv32IZKhFb0hJdXKPu37gklGm2INhusjt1mjq7wnqx3SFMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار مهیب در میانمار، دستکم ۵۵ کشته
برجای گذاشت
🔹
در انفجار مهیب در انبار مواد منفجره در نامکام در میانمار، دستکم ۵۵ نفر کشته و بیش از ۶۰ نفر زخمی شدند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/655080" target="_blank">📅 20:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655078">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7TbWwwEhl6VHsTg6ytKwnUN79rdSr99rY0QRV-Am7kHu9r1MEKiQRSWc69Zp8tpikwoBJxFGZnANkdPeKLmTXMb55DMaOSJvQC-pwkTiN7_vOZT9JaRVKKQ0mDNGJpNT98sgNd3u08U3Jp_UlIz1yHVIrJlXIjDD_ZrTuZfIyn8yU8TdypTI83vbD2-LxkfjDAtSncZeUmoVpNXbQrkyVxjBVr_FEqvGsa2snljtr3n3UuntYalOtkOHWlilSIQgMhlXJpiGdKsT5VcyOnNOi3EoXv5t9VIJQEbUi1xceABL3QY-d_8jU7_mdw7c1KqZcX-BDxruJuneZjQXWo3WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FmB3NOxQMrYq9GgfVpcAnzThFivnX2a4aP7EY7Y1uFRxpCX79nRWlxBhrr58mmCMtpa24eH2MYAUu9CiJvHpLCw502hB8pAsGUC6As2IgwTG699kLz3fkzixkZKQTa2j7ulRkGEh3iHU5qnjeezGmsm97BLYEEO0oXe_2cLm5mZIBwPLIHIqe_ewVvy1tkk7760wnMdGtFnOXKbBb2D2do-j8R4SJAtWqANAocrsSizvm7H9ej1SMBw9OWg9aVRDKFNxlUFPRV92x7R8uRMWX5FXiknbPW-o8gkT-4zxgyXD83RPMEeNRqu2lj3-HlyGDvyfTXMqPi_hebhA0AlKHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📚
نام کتاب: الغارات
🖋
نویسنده: ابن هلال ثقفی کوفی
🔹
«الغارات» کتابی بسیار مهم با ترجمه‌ای روان و دوست‌داشتنی، روایتی زنده و پرحادثه از دوران حکومت امام علی(ع) است؛ کتابی که یورش‌ها، ناامنی‌ها، سستی یاران و مظلومیت عدالت را ملموس نشان می‌دهد و فهم نهج‌البلاغه را عمیق‌تر می‌کند.
🔹
مطالعه این کتاب مناسب تمام کسانی است که می‌خواهند دوران حکومت امام علی (ع) را بیشتر بشناسند.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/655078" target="_blank">📅 20:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655077">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
نیویورک تایمز: ترامپ شروط سخت‌‌تری را برای چارچوب صلح به ایران ارسال کرده است
🔹
به گفته سه مقام مسئول، ترامپ شروط چارچوب احتمالی توافق برای پایان جنگ ایران را سخت‌تر کرده و این تغییرات پیشنهادی را برای بررسی به ایران فرستاده است.
🔹
هنوز مشخص نیست که چه تغییراتی در متن این توافقنامه ایجاد شده است. اما دو مقام مسئول گفته‌اند که ترامپ نگران بخش‌هایی از توافق احتمالی است که شامل آزادسازی دارایی‌های مسدودشده ایرانیان می‌شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/655077" target="_blank">📅 20:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655076">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74d6f98f82.mp4?token=BPI5fi1ccjX-9a1HO_lBrvIYE0yNOZwsVSeQIguYdHioRYbzYU7HZ1VdvcLv2eET1CVhfhthKvXpQDT0OQBHzXeB_YY-UO0etqmhVyRIqISKCs5ahwUlIP_XdecwkMBNCCU0FviSTqoUOA7tYkVTXjlE_ViLcvqanDQ8cl8sEcykDjLfi9GokzrISKBnWrVY3uDjqlLvxFln3ziGYgwmqSwBwKG9E9XJg_OmHMuhI8amFX92wW-meMUvaPVM6zUtn5vj20eCAMuK0QdEvBfhdEtT1BqUra5Wdi9_aBxtYBBViX8W0qGs9uLmsOglh7Wfz7gB4BWYeIrv0K6vbfrA-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74d6f98f82.mp4?token=BPI5fi1ccjX-9a1HO_lBrvIYE0yNOZwsVSeQIguYdHioRYbzYU7HZ1VdvcLv2eET1CVhfhthKvXpQDT0OQBHzXeB_YY-UO0etqmhVyRIqISKCs5ahwUlIP_XdecwkMBNCCU0FviSTqoUOA7tYkVTXjlE_ViLcvqanDQ8cl8sEcykDjLfi9GokzrISKBnWrVY3uDjqlLvxFln3ziGYgwmqSwBwKG9E9XJg_OmHMuhI8amFX92wW-meMUvaPVM6zUtn5vj20eCAMuK0QdEvBfhdEtT1BqUra5Wdi9_aBxtYBBViX8W0qGs9uLmsOglh7Wfz7gB4BWYeIrv0K6vbfrA-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
با این ترکیب جادویی کیلو کیلو وزن کم کن
😳
😍
👆🏻
این پودر جلبک جوری لاغرت میکنه که انگار اصلا چاق نبودی
👌🏻
کلیپ رو کامل ببین و از همین امروز لاغر شو و تغییر کن
☎️
لینک سایت اصلی برای دریافت اطلاعات بیشتر و سفارش با تخفیف ویژه
👇🏻
❤️
از امروز تا پایان شب می‌توانید محصولات منتخب را با تخفیف ویژه تهیه کنید.
🔥
https://landing.creditsw.ir/UEXKr
https://landing.creditsw.ir/UEXKr</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/655076" target="_blank">📅 20:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655075">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c72db1b5e.mp4?token=Mcbemubhn-4UAeDFDXCfVLYrQNgJ8Q9T5AsBhxaB0beHP4U3dFGTzt4RCW31zNO_uPDP_B9my8lEzkS_Rf2J1lSWhAqFqEUxNGVvOleUZXIAAVfDS4Qnv_Xb82E4sWy-QDZFnG66xyk1qQ11t4m8HzAkbxcmS-QquCT0ig3BMJkiuBioQpOWl0-_IIDTzVqrVtTmMO0I8IkYTh8yLNbQL9UF_QZ1AessEWffQHP5dqyBfOrjb83r3WAkXCPrNsKjNN-7tqTMe3HNow7rU8NSoIbCvVaS_XFSgxRXq_fT-qEi6VTmVLVNInJTRtdEOo7f8aUOrhYF5P5_1ffwqEXS6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c72db1b5e.mp4?token=Mcbemubhn-4UAeDFDXCfVLYrQNgJ8Q9T5AsBhxaB0beHP4U3dFGTzt4RCW31zNO_uPDP_B9my8lEzkS_Rf2J1lSWhAqFqEUxNGVvOleUZXIAAVfDS4Qnv_Xb82E4sWy-QDZFnG66xyk1qQ11t4m8HzAkbxcmS-QquCT0ig3BMJkiuBioQpOWl0-_IIDTzVqrVtTmMO0I8IkYTh8yLNbQL9UF_QZ1AessEWffQHP5dqyBfOrjb83r3WAkXCPrNsKjNN-7tqTMe3HNow7rU8NSoIbCvVaS_XFSgxRXq_fT-qEi6VTmVLVNInJTRtdEOo7f8aUOrhYF5P5_1ffwqEXS6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش گرفتن کارخانه هیوندای موبیس در هند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/655075" target="_blank">📅 20:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655074">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
نبیه بری، رئیس پارلمان لبنان به شبکه «ان‌بی‌ان»: من تعهد کامل و فوری به آتش‌بس از سوی مقاومت را تضمین می‌کنم، اما چه کسی اسرائیل را ملزم به توقف تجاوزش می‌کند؟
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/655074" target="_blank">📅 19:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655073">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4253207142.mp4?token=mzO5BCyymMHCZ7hlledYLGPPxvfj-PoEXkbDmQjQ3rDovjtCWaSqpepWQuZfQ8qyGasg7-GWRvUwpQJWSwxYbbmYNSbyDq0dQSMoDlbnkJ1gU-xMLev6hvbyWinz8KZnyFmWIYkBTuDQS0I1rrmU3BGfjm8as8VV0DRpuh-nPU-UgbL0q0Oou9lsnpFK6Sd_hUc7iGXy94BCEoWodxWlYW38Hat7GOL3oo0sIoWw3RD60mgx1-UZfn1twreQqNql_CuTaX1CBG_k0ifV-KBm6va4qBEsY2DuJPK475UL7NElEfgyTOmtF307Md9M56aZoASIj4nHbj39mZvTtjxnIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4253207142.mp4?token=mzO5BCyymMHCZ7hlledYLGPPxvfj-PoEXkbDmQjQ3rDovjtCWaSqpepWQuZfQ8qyGasg7-GWRvUwpQJWSwxYbbmYNSbyDq0dQSMoDlbnkJ1gU-xMLev6hvbyWinz8KZnyFmWIYkBTuDQS0I1rrmU3BGfjm8as8VV0DRpuh-nPU-UgbL0q0Oou9lsnpFK6Sd_hUc7iGXy94BCEoWodxWlYW38Hat7GOL3oo0sIoWw3RD60mgx1-UZfn1twreQqNql_CuTaX1CBG_k0ifV-KBm6va4qBEsY2DuJPK475UL7NElEfgyTOmtF307Md9M56aZoASIj4nHbj39mZvTtjxnIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا در گفتگو با فاکس‌نیوز: اطمینان از اینکه تنگه هرمز باز است، ما اورانیوم غنی شده با خلوص بالا را دریافت می‌کنیم و ایران سلاح هسته‌ای ندارد؛ موضوع ایران را تمام می کند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/655073" target="_blank">📅 19:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655070">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9be5d7fff8.mp4?token=g8dZGMOOrS-13bHOm8T-whp1Ansi_rwMUE91CYqzPdIpVGBOa8uNJXfurWkDYXT1Tsyg5Co_7K45Cgq6ORc0TEF2MYOOtnLlM6egB2yxhEcc9FC-qox1spsbcFXeRs53uE91hnT4yVmBiOohNabvaiWpJYKvC6MjRO_jNtWne5hiX9NWQpmlgU1aEgOxsRQVkdrx82rBinxKPUUVZchW2XB2AgFcPZruERSdwMTaZmhlqz8X6mleDlRaMwgmLpzLWScn4BdPFAbmQpfyhab_iwYIKpIb6xmwiGPvIcm67n0ouReCNfX7By_UH2lcyx0klpo8r5wDCYAsokiGTbMCLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9be5d7fff8.mp4?token=g8dZGMOOrS-13bHOm8T-whp1Ansi_rwMUE91CYqzPdIpVGBOa8uNJXfurWkDYXT1Tsyg5Co_7K45Cgq6ORc0TEF2MYOOtnLlM6egB2yxhEcc9FC-qox1spsbcFXeRs53uE91hnT4yVmBiOohNabvaiWpJYKvC6MjRO_jNtWne5hiX9NWQpmlgU1aEgOxsRQVkdrx82rBinxKPUUVZchW2XB2AgFcPZruERSdwMTaZmhlqz8X6mleDlRaMwgmLpzLWScn4BdPFAbmQpfyhab_iwYIKpIb6xmwiGPvIcm67n0ouReCNfX7By_UH2lcyx0klpo8r5wDCYAsokiGTbMCLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات سنگین هوایی رژیم صهیونیستی به شهر صور
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/655070" target="_blank">📅 19:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655069">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213580575c.mp4?token=tbU4xoszAX8aqrzLET4q4pVx9TwYdJ_FK-aKRZQ5MTyUKEL2oThjejnNt3BLDQPM6LYXVOuCJZW4nlXNm0jfLnp2ylDjuBD2IO58sK2BLYSCEKS9Jtp3guniWEIPplfGyMhmfnSCzRcFnz1jaQsnCbkJIanmReOmqe47LZjVVV3Vrny98ZaeFVibSch4eh_gmq4PvK4G9vsz8ckIKDwx2uRWqLICdkS0xPawfPQndjX6F-U2NmGgFK_Afk8LFRHJlNKXNR5p3lxSKQOtmKY0opLiq_tpEMTCA_-OnXaa4dQNgIelu8EOi6WQ75S42kkp9aWhmAxzEYcUckXpnqE9qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213580575c.mp4?token=tbU4xoszAX8aqrzLET4q4pVx9TwYdJ_FK-aKRZQ5MTyUKEL2oThjejnNt3BLDQPM6LYXVOuCJZW4nlXNm0jfLnp2ylDjuBD2IO58sK2BLYSCEKS9Jtp3guniWEIPplfGyMhmfnSCzRcFnz1jaQsnCbkJIanmReOmqe47LZjVVV3Vrny98ZaeFVibSch4eh_gmq4PvK4G9vsz8ckIKDwx2uRWqLICdkS0xPawfPQndjX6F-U2NmGgFK_Afk8LFRHJlNKXNR5p3lxSKQOtmKY0opLiq_tpEMTCA_-OnXaa4dQNgIelu8EOi6WQ75S42kkp9aWhmAxzEYcUckXpnqE9qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی حضور ربات در نماز عید قربان در دبی واکنش برانگیز شد
🔹
یک ربات انسان‌نما با لباس سنتی اماراتی در نماز عید یکی از مساجد دبی حاضر شد و ویدئوی آن به‌سرعت در شبکه‌های اجتماعی وایرال شد.
🔹
این ربات که «بوسنیده» نام دارد، با پوشش کَندوره و شماغ در کنار نمازگزاران دیده شد و حرکات نماز را انجام داد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/655069" target="_blank">📅 19:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655068">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
تردد سراسری خودروهای پلاک مناطق آزاد چابهار در سراسر کشور تکذیب شد
🔹
چین به خاطر مصاحبه با رییس جمهور تایوان خبرنگار نیویورک تایمز را اخراج کرد
🔹
سخنگوی آتش‌نشانی: دود مشاهده شده در اتوبان ستاری تهران مربوط به حریق در انبار کالا بود
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/655068" target="_blank">📅 19:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655067">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c342424265.mp4?token=IxTwOryVdURcV9dbShBUJX82Uwn3rVs5zJLBtjrpZaDioWsQK5gu_gMT6ioJKMQJ6mX3Yh6fJNC-I_uo9KGXLmik086Xlzsdq951bzG1R1tE7CVLn9WRIn9g_UJlT10Ur7RvHgKJTfMclNROFCHHvHMYdbg8RD-M4uIfUuVLwhrno4G5JZsiDDcnPhJHHe7RRLy8nD4iOcsFYsCiqjB6Bpe_jQj7abppNYrnHo6pDb1kFiaYZc2WfH1r0wuZzQgJHTIJwHceBfgbZBWAa2SoXOYabXq2ltWntuHU_yCL6uvlEdIdqR1vANXSjJpzy8BInXMVajyXvVS9Epz9rRAukQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c342424265.mp4?token=IxTwOryVdURcV9dbShBUJX82Uwn3rVs5zJLBtjrpZaDioWsQK5gu_gMT6ioJKMQJ6mX3Yh6fJNC-I_uo9KGXLmik086Xlzsdq951bzG1R1tE7CVLn9WRIn9g_UJlT10Ur7RvHgKJTfMclNROFCHHvHMYdbg8RD-M4uIfUuVLwhrno4G5JZsiDDcnPhJHHe7RRLy8nD4iOcsFYsCiqjB6Bpe_jQj7abppNYrnHo6pDb1kFiaYZc2WfH1r0wuZzQgJHTIJwHceBfgbZBWAa2SoXOYabXq2ltWntuHU_yCL6uvlEdIdqR1vANXSjJpzy8BInXMVajyXvVS9Epz9rRAukQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت حداد عادل از ساده زیستی رهبر آسمانی انقلاب؛ پذیرایی رهبری از میهمان با نان و پنیر
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/655067" target="_blank">📅 19:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655066">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtzCX996BLxT4baGrjKfppvVWIVv9nE1GJmCnUKNCp47HWFsyUy5x6vBpJ2PNkcx6g3GT49jwmn-CYgdFl_NHZzqPqJhCplMhAFae8Q5ZbfWZljh90ld7PV-wHa1djOvomjZ1ezqGaancf8lc03a2YYZ3qyDUSq5doWe4puTaQCMw7I20U8JbXq5pyaLGdDhnUA-ftsU8Yn59KG1GzieV0A-gZfBVfNndhZRSoD3S5PIKXdPms4kr535QEPVzhZ2FV9OnUOYROfPmUC1Pfgp_iV_kIleYRfCYpJjX6UsDxw9pkqAi_cucYLf4UtNNAhdn-5JMyA2G3q9A2oWPgHIFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در شرایط «نه توافق، نه عدم توافق»، اگر پیوست رسانه‌ای مذاکرات درست عمل نکند؛ اعتماد عمومی قربانی خواهد شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/655066" target="_blank">📅 19:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655065">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
سکوت سپاهان در قبال حذف از آسیا
🔹
مدیران باشگاه سپاهان در مورد انتشار خبری غیر رسمی مبنی بر حذف این تیم در آسیا فقط سکوت کرده‌اند.
🔹
این باشگاه به‌ دلیل نقص مدرک از کمیتهٔ بدوی مجوز حرفه‌ای را نگرفته بود.
🔹
با حذف سپاهان، گل‌گهر، چادرملو و پرسپولیس در صف آسیایی‌شدن خواهند بود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/655065" target="_blank">📅 19:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655064">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
سپاهان مجوز حرفه‌ای نگرفت و سهمیه آسیا را از دست داد
🔹
باشگاه سپاهان بعد از عدم صورت مجوز حرفه‌ای به کمیته استیناف اعتراض کرد. این کمیته اما همانند کمیته صدور مجوز حرفه‌ای رای به  عدم صدور مجوز داد. AFC با درخواست سپاهان برای باز شدن سایت جهت بارگذاری مدارک مخالفت کرد. بدین ترتیب سپاهان از کسب مجوز حرفه‌ای بازماند و نمی‌تواند در رقابت‌های لیگ قهرمانان آسیا ٢ شرکت کند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/655064" target="_blank">📅 19:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655063">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac492f7a9.mp4?token=W4Jr9wJev7ePDSAJUUXrssrL01WRXarUrxPpgclrPU2n0SsOwAUeZnWJq6Fyrkx8sftxADMV0RvYy15MVRkGZQM1_U3sjIW7s74ljzckTnYcwaiFTjUY2dESsj0E53Y1IE9ktPihKaAjQVA8LAmKKgLEY_-JKhg48UGE0JFbmDQ7krTpB93ZFzSI1IV3VVbGDSIV6j4bCGiXIPH5M8h5GGBmsHtw-Q520ABjdhMi3vj3IYhJ9-gHkFGoadF0y5LNu_LKJHSsvJSAsJ7qT12HQyW-G1Ghkcpev-uG1pxjHHDtL3qe7izTEKXmk52NrlYsVYtYSQCoG4ooVR-S_FgJTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac492f7a9.mp4?token=W4Jr9wJev7ePDSAJUUXrssrL01WRXarUrxPpgclrPU2n0SsOwAUeZnWJq6Fyrkx8sftxADMV0RvYy15MVRkGZQM1_U3sjIW7s74ljzckTnYcwaiFTjUY2dESsj0E53Y1IE9ktPihKaAjQVA8LAmKKgLEY_-JKhg48UGE0JFbmDQ7krTpB93ZFzSI1IV3VVbGDSIV6j4bCGiXIPH5M8h5GGBmsHtw-Q520ABjdhMi3vj3IYhJ9-gHkFGoadF0y5LNu_LKJHSsvJSAsJ7qT12HQyW-G1Ghkcpev-uG1pxjHHDtL3qe7izTEKXmk52NrlYsVYtYSQCoG4ooVR-S_FgJTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کار دست مردمه؟!
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/655063" target="_blank">📅 19:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655062">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوهشت - دیده‌بان رشد اقتصادی ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjA36z_Qqqqec57adJkbPkc5_birS4RDTPLLjMC39qWc-9JE8HRRXPTgtpmnSx7zqaXj-FFLz8-R7k07KroRuzZ37Fq6dQgq0cD33vJpirIYAeTnXlpuxTe4e6uHxDNVzMIXAIJVoBRaEoPnt0V-dlIw6YYolqpGPx-srLENB8ZxBrIvWB2TpQ0enJAwFrK9AK7hGcUK1VWK6R-_RHEFhjcSoLdxjofeBY61AuOdpN01TbJyuvZDt8bQ6nH6beWBhYr4vthRq2QX3c1rjNMhRc2QBzXZMGdFSYAT2yzmYR-bfK6VB8WlSJxHa6IvuwH32ArC-4nKWG1tXmvYmABK2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔦
قیمت مرغ یک پا دارد!
تثبیت ارز رسمی نتوانست قیمت‌ها را برای مردم مهار کند.
🍗
از فروردین ۹۸ تا بهمن ۱۴۰۴، میانگین قیمت یک کیلو مرغ با دلار آزاد معادل ۱.۲ دلار بوده است.
در بازه‌های کوتاه چندماهه، قیمت گاهی بیشتر یا کمتر از این عدد شده، اما خیلی زود دوباره به همان ۱.۲ دلار بازگشته است.
🏢
این مقطع، بازه تثبیت‌های طولانی‌مدت نرخ‌های ارز رسمی (ارز تجاری و ترجیحی) است؛ دوره‌ای که در آن، این نرخ‌ها تنها در چند مقطع کوتاه توسط سیاست‌گذار تعدیل شده‌اند.
⛔
اگر سیاست تثبیت ارز موثر بود، باید قیمت مرغ به دلار آزاد برای مردم
کاهش می‌یافت؛
اما داده‌ها نشان می‌دهند که این قیمت در فروردین ۹۸ معادل ۱.۱ دلار بوده و در بهمن ۱۴۰۴ در
همین حدود قیمت
یعنی ۱.۳ دلار قرار داشته است.
اکوهشت
- دیده‌بان رشد اقتصادی ایران
@ecohasht</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/655062" target="_blank">📅 18:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655061">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ترامپ نگران شرط آزادسازی اموال بلوکه شده ایران است   سی‌ان‌ان به نقل از مقامات آمریکایی:
🔹
ترامپ بر عبارت‌های سختگیرانه‌تری در مورد تعهدات هسته‌ای ایران و وعده‌هایش برای بازگشایی تنگه هرمز اصرار دارد.
🔹
ترامپ نگرانی خود را درباره میزان پولی که ایران ممکن…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/655061" target="_blank">📅 18:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655060">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16459d2426.mp4?token=gSg8HirMflj4GN0hHdBmY_fRaZYCli7LwivRt36TrUSPN0BlKccV99YRiRDV9CCeGbEfEyX68XU9ZE4ZhHUVGoqFOlGzA6aa7UnoDWJdHq9uM0x4mITEOf7mKhKJBZOchLpfy_YkO0SbDlKRc9r_Qho6X18hjROGyllpz7sEr0IcZOR9l8NBzrES4oceqaaVjXqHml7TQzVuols3w3mtu1f13YvFLz4yeT_eaBS1yhMoKf1csLxVQmUg9dXCDCwIQp_VXj2nI2hjmtjFmOyc9i8bqYqW7Nd8IBXpa0Ezx17wN_yo42yf9ZMScbHgYHDv_LYP0lXMq8bldEOWlFB_MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16459d2426.mp4?token=gSg8HirMflj4GN0hHdBmY_fRaZYCli7LwivRt36TrUSPN0BlKccV99YRiRDV9CCeGbEfEyX68XU9ZE4ZhHUVGoqFOlGzA6aa7UnoDWJdHq9uM0x4mITEOf7mKhKJBZOchLpfy_YkO0SbDlKRc9r_Qho6X18hjROGyllpz7sEr0IcZOR9l8NBzrES4oceqaaVjXqHml7TQzVuols3w3mtu1f13YvFLz4yeT_eaBS1yhMoKf1csLxVQmUg9dXCDCwIQp_VXj2nI2hjmtjFmOyc9i8bqYqW7Nd8IBXpa0Ezx17wN_yo42yf9ZMScbHgYHDv_LYP0lXMq8bldEOWlFB_MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین ویدیو از خلبانِ شهیدِ جنگ رمضان قبل از شروع ماموریت
🔹
شهید جابر طاهریان از شهدای جنگ تحمیلی سوم است؛ که در ۷ فروردین به شهادت رسید.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/655060" target="_blank">📅 18:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655059">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
سی‌بی‌اس:‌ آمریکا متن اصلاح‌شده تفاهم‌نامه را به ایران فرستاده است  سی‌بی‌اس به نقل از منابع آگاه مدعی شد:
🔹
رئیس‌جمهور آمریکا روز جمعه متن اصلاح‌شده‌ای را به ایران ارسال کرده است و این سومین بازبینی متن تفاهم‌نامه از سوی واشنگتن محسوب می‌شود.
🔹
تغییرات آمریکا…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/655059" target="_blank">📅 18:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655056">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VvRZ5gd7kGn2CMkrdrqBnzzMMncymX_KCkK7PcIUMBsnjKBIB3AmoGJ4DGiku1HRfcWBCA6E0rDO_iaNAVaRMrWqmMZYdIKAIwRkTfd5UjQBm92cd4FlXIxMRvzaIkxADBCch26kCLZyJNgGqkPqketFmZ-7Z5E50P6xDNNWtCegXqnH6w7ZsW_g5mYkooIPUBDqJFKTFie28raRi5nYtvpNiCMDqUTbMxTINpw9AQ_18N-Hg_nRIICFtdsNPKEBxrKi6sqmCVugGdK-G7eOYRou6lrobjh88-uFTIDzYUhYWHraS3VNiwbQEHbOhkh-QoUIJIu0A5WLBxThY9oP-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ulgCGJX4jqsYHg_2xV_NLAa9j6ocFMDF4CpuSEhdmSSC-gBWs4knq5wGfJ-0MvRuyYoqfRWdbISO__ZCsgNpIBCCfIVXGPbBqb3YNorl4YEmeKz5nJkDcrxihi3nsO86gAXSZZzHBHzq8c21BuZllvykuOkd4WUUuKz9yZ0mwiexGEKmPwtK2IOJEBkfm_lfKBn74TH0pQ3-ABf-398yET7WeuNcj2cuftb1fgbHxwRUoKk3l5_zD8iBsThQdkPc4U6dMwGrCMjkewbM_gmkCtvN0RAAKi3MBnrW8niva6ciq8d5Ws0_J1mxVccuO3Qq3O3qWoH-ByK9jBaD6ntWWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EFxkC_w4Lc7GmCiVsVuxN-Lm9Jo5FzNQOUKVgUWbsO6vle2baofRJdW3cM6r3xS1a2ZE8siVU27kqXAADkr18F41vyud-NllwTPtXC8-LjJuNV_7FF3V_9_oYz2Kf-pcyov8XS_NQA_xucoJXRwwD4xdeOUhajafXu0-jpHXBG5P1qa7QHBlAHmz4ypjJVPSwCAdiYxkowES2D2ufaRB20VydnzMRyRpUyOgZ6Unitdl45KyQunSOxNWxUwbmpbigWT6j-IPOAn4R_pfaqwavKYP6Y4zRcHHhfY2iMhiTHKNXn8qhzOXvlnIm2K2aeeRx27MFAwUo928fgHo9dSpug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصویری از ابرهای متفاوت لنزوار یا لنتیکولار در بلغارستان
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/655056" target="_blank">📅 18:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655055">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
سی‌بی‌اس: میانجیگران در حال مذاکره با ایران و آمریکا هستند  سی‌بی‌اس مدعی شد:
🔹
میانجیگران از صبح روز یکشنبه همچنان در حال مذاکره درباره یادداشت تفاهم بین ایران و آمریکا هستند.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/655055" target="_blank">📅 18:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655051">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JavDtrLFWo7C_2e0uPU0Py0TJ8Aj_2IQvDCrb91niCapx-ataI5lzScM8cugkafZk90vKkQnvG0Cs-U9L56rlJjlhjlswN1xkrAlt4xKCpdnI5aIMB6CLOPCWAL0O8ymTol-aubKIK5uHaWQ_AWFXJMve2sjDzOeJ_tGQMLWqlbrJMGWufF8QGKEerdP5MkkgP-7IfRnlXqgC92YUnoHxMtpPMr-g6YFs5ZqEOCq1FS18ArjfxH9wYu5ngY-iHLLNHa2DIosgL5qn8WFaDV_JbfvrHTnuXojexL1OsW39_G_tRcGMWc1ZUwHFA9NRA_7iSQ2Ejf2DAPh9I_hgw6uYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PciPcW0RUMkpPtufCLLX-66Y_bwgvA2a-FrFwzeG18ypT-6_GomG2FLRvzjsdPSFfqTI_a0tA5sc0ydsCxD_Zapojye-gP6TtVFN_NgiVsc1OPwiBVAQnwGQcWx-7D4gbup9cVb01aS2uRQqQfU1I5jy0Ai7dPbITlTj-jFDdYme_cgR0zmgM98MWyVx_RIhzcajQmS8_f_CEeOsVo-QFhlsoWz0ImC3DoW31fXeuYgmgGwxwyvHk-I3sTB1SnjiHeIyjTq7n1Laq-1ow8HFeWh-2tjnIzB_rjVs2v8P4upItX7C9xxrZ_mBxD3vBCt91mLvf9AGVR8oCKjuXFmn9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fa_0xVD58-yyCwtyQZQKM93NC_WXfqHz1PFosOUZg_Ns8rMix8YmkrVrlf5YUBjjpPqdf8ZAllowkaph9oJ15ls5MsZdTjBSHplFT91XB0-ALj22xakGgdUkqworbIfDAFb98VqrpTMTkt_oews-RFv0n6JP-75WMUfDV4_bsVVXmYepmXpzngvhThwO5iUNCIZ8iaTwOhmhl2JzBbG2Pes2rjZ_mTLWQvNbdvPFV10uwdXZ_0fACL1HYWV8nPuQHvrhCERHXEdcRUt7jbyOPaRUCGV6k_JoyBqxqdfnjZCz0mNwMnm1M_T2NGX_ZZXXKgCNjjDSDfP9nrYo77db8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ADf-LP7aXfxnG6sj6m-3GSyEqM55k--55kt_z0lkVvHziIJGM7gpdyJwYTKAUQxyyQkPd4XNZD635CuEWfNHShkuPtNLCwAraTD4-WbQz7_CAxwA0HFA3XAgRgm3pGadSptwHbNo9tUqURXp1rYGmrlCAmOWoxgzFENH7X9Me8aIKkoQRUlmPSfbOKscFfXkh_uJEvxrQ8Du67_jPzgLFwSUiuFG-J4lPwnyYWRGKYbF3VFtTBi8F4rm72Kn8KxBn4YKAnXsHbwcFaE45kTbfmpp3XDC4tbGuxXTc9Qakj2UTpX-bcRllUNfa4zu5x6r-60pNWrYFqe7qCo9O6MVeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از خوش و بش پزشکیان با وزرای دولت
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/655051" target="_blank">📅 18:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655050">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hi9dnV564DhgINYV4OPkI-gtUGQsRMjS91y6SKazL2Icu0GudeMcDOZdMTCS2Hm3DpMw0YwYKfjE5yjLihCqKxkYK8hDVi4N7BAs-QGun4WwtbTwNtg_D7Sold_0jYCK06-SptmTuRABjmoXXfMjXbB7IzQYlrOAByRS6NT3yx3dYjHpKe5cVF-mZbRsnJh7gVYSWX7sh_fPLa1nGvlcYOZgDMCkPJPsQUpQ1cxBF_zbC4BlrrXCsKhwl7uYaPS1IGJBT8u9TCqmRNKUTT3XfzadM2FR19gSIgAo7zVIGi0bmQQZhoSacwblPYV0w4reKTRUW2F4J4AXA24BNYVfrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خاندان بختیشوع؛ بنیان‌گذارهای پزشکی علمی در جهان اسلام
🔹
خاندان بختیشوع یکی از مشهورترین خانواده‌های پزشک در تاریخ ایران و جهان اسلام بود. ریشه‌های این خاندان به سنت پزشکی جندی‌شاپور در دوره ساسانی و پیش از اسلام می‌رسید؛ جایی که دانش ایرانی، یونانی و هندی…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/655050" target="_blank">📅 18:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655048">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌
♦️
پزشکیان: جامعه باید نسبت به الزامات و هزینه‌های مقاومت آگاه باشد
🔹
اگر قرار است کشور با اقتدار مسیر خود را ادامه دهد، باید واقعیت‌های موجود برای مردم تبیین شود و همه بخش‌های جامعه در این مسیر مشارکت داشته باشند.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/655048" target="_blank">📅 17:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655047">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‌
♦️
پزشکیان: هیچ جامعه‌ای نمی‌تواند در شرایط رویارویی با چالش‌های بزرگ، انتظار داشته باشد که بدون تحمل سختی‌ها مسیر خود را ادامه دهد
🔹
مهم آن است که این مسیر با آگاهی، همبستگی و مشارکت عمومی طی شود.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/655047" target="_blank">📅 17:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655046">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
پزشکیان: شرایطی که کشور امروز با آن مواجه است، عادی و ساده نیست
🔹
مدیریت این شرایط نیازمند هماهنگی، همدلی، گفت‌وگو و تصمیم‌گیری‌های دقیق و مسئولانه است.
🔹
تداوم برخی محدودیت‌ها و فشارهای خارجی، به‌ویژه در حوزۀ دسترسی به منابع و ظرفیت‌های اقتصادی، پیچیدگی‌های…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/655046" target="_blank">📅 17:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655045">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
پزشکیان: شرایطی که کشور امروز با آن مواجه است، عادی و ساده نیست
🔹
مدیریت این شرایط نیازمند هماهنگی، همدلی، گفت‌وگو و تصمیم‌گیری‌های دقیق و مسئولانه است.
🔹
تداوم برخی محدودیت‌ها و فشارهای خارجی، به‌ویژه در حوزۀ دسترسی به منابع و ظرفیت‌های اقتصادی، پیچیدگی‌های خاصی را برای ادارۀ کشور ایجاد کرده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/655045" target="_blank">📅 17:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655044">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
سی‌بی‌اس: میانجیگران در حال مذاکره با ایران و آمریکا هستند
سی‌بی‌اس مدعی شد:
🔹
میانجیگران از صبح روز یکشنبه همچنان در حال مذاکره درباره یادداشت تفاهم بین ایران و آمریکا هستند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/655044" target="_blank">📅 17:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655043">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
حمله موشکی به حزب ضد ایرانی «پاک» در کردستان عراق
یک مقام حزب به اصطلاح آزادی کردستان به روداو:
🔹
روز یکشنبه  پایگاه مهم وابسته به این گروه مخالف ایران نزدیک اربیل هدف حمله موشکی قرار گرفت. این مقام، این حمله موشکی را به ایران نسبت داده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/655043" target="_blank">📅 17:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655042">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae626b6d9b.mp4?token=N_o_4Si-lteEcVYFnf6VN660KRTbTH0vyZeK3ioXo9wzj8WjJjyVz55ChJaDdpHI1gvP7Pqy07ZRxjdxz5wRe_-8o2G1k0EDH5PHmExTT0Fo-IZR2dD0u_VBTTxCo8p8oLYFIwJVroHmcHMm0krtcXhmKtFwGlpY6HxuslDoBWkDGRIs41BeRR_wlYkLrRQWGsFTLNtLCXHy-rzAa4Ocj29ThuU-X5FGNrcJU8OjLs8mazReYK2xOiJaJwjZPEIXoHJCbK5mOA8tteDfPpzrowARmJrhEg8mFK_A0cMJB_k5aXnQM5UccLtCzfturalnJkzVrG6vBSaKiAtGTD6Gnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae626b6d9b.mp4?token=N_o_4Si-lteEcVYFnf6VN660KRTbTH0vyZeK3ioXo9wzj8WjJjyVz55ChJaDdpHI1gvP7Pqy07ZRxjdxz5wRe_-8o2G1k0EDH5PHmExTT0Fo-IZR2dD0u_VBTTxCo8p8oLYFIwJVroHmcHMm0krtcXhmKtFwGlpY6HxuslDoBWkDGRIs41BeRR_wlYkLrRQWGsFTLNtLCXHy-rzAa4Ocj29ThuU-X5FGNrcJU8OjLs8mazReYK2xOiJaJwjZPEIXoHJCbK5mOA8tteDfPpzrowARmJrhEg8mFK_A0cMJB_k5aXnQM5UccLtCzfturalnJkzVrG6vBSaKiAtGTD6Gnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ سخنگوی دولت به سوالی در مورد غیرقانونی‌بودن تشکیل ستاد راهبری فضای مجازی: این ستاد همان شورای‌عالی فضای مجازی است!
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/655042" target="_blank">📅 17:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655041">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpdwyhHpEQV8W2dxl1r6VYZkBPQl8GLXzKJsuRXy7HvGcyq_WJPDv8diKbKMb76UktHuHMWPhTEvnIE5rDo98NUl5vSXhhDCIoH6zl4PKencdYnqdOLX64tZagq7fAvmZ_m8XCGAsa8WMFnXzymu_VCk3Jcg0YFOYzgN8-rgElKaYtj6jCt0dlFmhQCNBf9lMwgLYIKxXy_QtrWHiryKADJ3HZvs8GRN5K4NbUbSFVPO5H5B6aT3O4ZNtPueJN_QhfEltse4WfmlNntDlHfPWLldgKgX6pY-UUddlOTdN5BcsmGWezCgSJX8byBQgc99XFuvYo9s3YWdYRKxCQ14GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تلاش ۲۶ میلیارد دلاری پوتین برای افزایش طول عمر | علاقه به جاودانی جدی شد
🔹
گزارش تازه وال‌استریت ژورنال توضیح می‌دهد که علاقه دیرینه ولادیمیر پوتین به موضوع طول عمر و مقابله با پیری، اکنون از یک کنجکاوی شخصی فراتر رفته و به بخشی از اولویت‌های راهبردی دولت روسیه تبدیل شده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3219241</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/655041" target="_blank">📅 17:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655039">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rHxv2dJBVxnZ329IZGKMcibbRm3tKOzQd4nFs7LVBw9AM9a1pztvsTSV-u4kqavdlMB8NqYs61SEGzIQTb2OWTBBfT2WWS_XwqhPP1ri0FkL8niEoY2CjEzNJNgkDmDKdRjTxoE0OVGWisrqXn5_ELd7UBYwAobG3ib3dLtXYdatcp_cJN4clbuMQVcWI8kQSHgElFaRLJRINgv1tIMRqw-3mckNNZFwSqSdzIEkyfyoa7Kl14vdzLNjYHnzy3d_6AANACTc7U_CwZDp8rHNOY_F-EFCKDVvxOQ_EhMIO6VxRaX6EYy0zIgm0tlnIsaC2VSomH4jCljYxzPYfHYbeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UqWFB4zDNSpe1iSCcuXIxz3FqxhkpjtC61b_n7xH1Z-LB1SaYEz5_-BYq3Add749G7DQDtmFVXKqBCj-gBlohFHlr38UnYgwqcI-ECGQV_-FGJkgqvi1JfOY9WLm7PeOCrHnx7i53PP59_HKe1SuJeLsS0rjkBY_GSTxjyjvfvrxh6b09WKXMiVQfvX1p5NKbAu3-wr8zXanpHJRT92NVwYxYTO7xxxMjfkayfM3-_W4Ki-BTT57DDFrq7Rlb0lH8miexbLwIxIWwuSb945izcfHUA3ZXUxvGiKRqvpSs9DJzQ9ImzW7rxbkI_OSbWaXPV-VPwWfjiUzYKYMXKuu6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از یک سوخت‌رسان آسیب‌دیده آمریکا در اثر حملات ایران
🔹
اویشنیست تصاویری از سوخترسان KC-135 نیروی هوایی آمریکا را که در پی پاسخ دفاعی ایران به پایگاه‌های آمریکا در عربستان سعودی با ترکش‌های انفجار مواجه شد، منتشر کرده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/655039" target="_blank">📅 17:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655038">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/544378e4c3.mp4?token=cifHzpnbFFM2d4B5Yv7eu_N3c2AsviQVN7cp8XtgnTKAhBbcB76vFTgxg7q7-2n0AF4SjxeNhcnHi5Qtv7uO5GfCSEX9uLaTBFzfUFVlYoHK1tysH_2SLoZTt6AOwn1kr1Tx9nkIWqx7OqsGyCFcG4pTaekPEx1KGOqrISuOvMoCP6_nsaIFgqbW1PuEYRMiJfnI6NqccuToH7ZMvxJvMT4qPYlz1LiHntZ0qMn3UvDzu9iTy4Eh-e5Sg2q4564XFsVhZW1zuQ7wR-RWLA9lbNLqMPv73t_pJa_GNrcKWXkLEh86v3b0yd2yRk3LMpETB7pNhh1_PprsgQYbW6eaHHogU4NCusbOOxERn_sZatGU0wvafRz1EktUvGR728hjS7geCG_5bsga70Bl14MIiPkSKJYUT2KSKqQ8lIPhTjuLb4VoLlC2dwv3O7aNiNLNopAO_kDJRPEBgf322HZpu-a2gsVZYR9UaxAM_zRucdy8J8J89kzUe5uJbn4dZA9dzKgKBuBXZ9rqclK5m_R4ryv38bUTnCg9P9a4jhjhnYMeYy-C3lVBxo4xyQbFnmEzYqTmi-cvo-SY8vAyush-VS_RqWzU8Nqp30T7WsdQgugGxE5teaUH1r0Js3Jm4EmCcdzhx5ovVTjSTOGtv4tlR7eWCOmjltpx8s9rtif_G1U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/544378e4c3.mp4?token=cifHzpnbFFM2d4B5Yv7eu_N3c2AsviQVN7cp8XtgnTKAhBbcB76vFTgxg7q7-2n0AF4SjxeNhcnHi5Qtv7uO5GfCSEX9uLaTBFzfUFVlYoHK1tysH_2SLoZTt6AOwn1kr1Tx9nkIWqx7OqsGyCFcG4pTaekPEx1KGOqrISuOvMoCP6_nsaIFgqbW1PuEYRMiJfnI6NqccuToH7ZMvxJvMT4qPYlz1LiHntZ0qMn3UvDzu9iTy4Eh-e5Sg2q4564XFsVhZW1zuQ7wR-RWLA9lbNLqMPv73t_pJa_GNrcKWXkLEh86v3b0yd2yRk3LMpETB7pNhh1_PprsgQYbW6eaHHogU4NCusbOOxERn_sZatGU0wvafRz1EktUvGR728hjS7geCG_5bsga70Bl14MIiPkSKJYUT2KSKqQ8lIPhTjuLb4VoLlC2dwv3O7aNiNLNopAO_kDJRPEBgf322HZpu-a2gsVZYR9UaxAM_zRucdy8J8J89kzUe5uJbn4dZA9dzKgKBuBXZ9rqclK5m_R4ryv38bUTnCg9P9a4jhjhnYMeYy-C3lVBxo4xyQbFnmEzYqTmi-cvo-SY8vAyush-VS_RqWzU8Nqp30T7WsdQgugGxE5teaUH1r0Js3Jm4EmCcdzhx5ovVTjSTOGtv4tlR7eWCOmjltpx8s9rtif_G1U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرآیند بازسازی بوگاتی ۱۹۳۲ که به آهن پاره تبدیل شده با هوش مصنوعی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/655038" target="_blank">📅 17:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655037">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb4c5c5bc2.mp4?token=Exz4J4Mb6Cf1biKFVwthVaWWsz89hW3teXlm0p8FMBCb0hGgfePQlsaXruRqphQTYSEUIcNVmpMEMSE0ouAWDLereInoyj3shT3J9Kt7eQjbAsJKM7bo58RNc6MPAvwzkXgw_tLlfqCgTMMzpxiHOEyIEWfcPdXAjdPkGUTGKN91FEckzglnlx7PKuS4SVqqUl3gu4Xa07RkpTAbtHiVunUkIe0ckIfWyN6U6YHA5IOenGTsEkk5qkThHX2pEFJorq9_FPeVAo_ELb3C_IEAf2xg2lmMV0W9RtE_1AYrxXO9EK_wYJVe0FStuHc5Uf-Kg4FwQjdqiaegyBCDqoOPcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb4c5c5bc2.mp4?token=Exz4J4Mb6Cf1biKFVwthVaWWsz89hW3teXlm0p8FMBCb0hGgfePQlsaXruRqphQTYSEUIcNVmpMEMSE0ouAWDLereInoyj3shT3J9Kt7eQjbAsJKM7bo58RNc6MPAvwzkXgw_tLlfqCgTMMzpxiHOEyIEWfcPdXAjdPkGUTGKN91FEckzglnlx7PKuS4SVqqUl3gu4Xa07RkpTAbtHiVunUkIe0ckIfWyN6U6YHA5IOenGTsEkk5qkThHX2pEFJorq9_FPeVAo_ELb3C_IEAf2xg2lmMV0W9RtE_1AYrxXO9EK_wYJVe0FStuHc5Uf-Kg4FwQjdqiaegyBCDqoOPcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکید رییس سازمان بازرسی کل کشور بر لزوم تامین قطعات مورد نیاز سایپا/ قطعه سازان بدون گروکشی قطعات خودروهای ناقص را تامین کنند
رئیس سازمان بازرسی کل کشور در بازدید از شرکت سایپا:
🔹
عدم تحویل قطعات از سوی یک شرکت خاص به سایپا موجب تولید ناقص ۵۲ هزار دستگاه خودرو شده که این به دلیل انحصار در تامین برخی قطعات است. وی افزود: در شرایط فعلی، هیچ‌گونه کم کاری و عدم همراهی از سوی قطعه‌سازان به بهانه وصول مطالبات مالی پذیرفته نیست و تأمین قطعات باید بدون وقفه به سایپا ادامه پیدا کند تا مطالبات آنها نیز از محل فروش خودروهای ناقص تامین و پرداخت شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/655037" target="_blank">📅 17:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655035">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDcBCLgvFzwR1EogDYCgjA4u0XDyRVWhwU599ywrtAl-mMP1-fLN05itGWv4RZypaswqy1eN3zJD-2Pstpn2EmP65jdIqOeVwj2ruMoxhVeB_Ll5j2SM6_ui2HWfGKiFq-kaH9REHUzEqstxD1WQhLp1ctftFsLvSj50n-6lWh92-7s6BdIwmF95Y7J6iZ7pSgYL8giE3uMmutOfnRNoXtR2oHhfyeFwjCzqKdkCj4lBcOn6FrZTqOxKfkjlap_9zztpJhprTNYwF2078KqbeCYKckLoEF-_rvYSXNJZIL3XE6EgVdLOfMyLQj7VYuj7gh2dEZfCwFKWQGYZIoTPvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/817b2c792b.mp4?token=DcZyov1JMAPFlTs1_cOpeuD6XvVz8-mH9jmo_Z1PukvzpXc_CYTH768LweU5PcZYPFtoLid0c2sQmTmEYbDURpdg03PKeSa4g_x3Me3-kBmuSJ1XtIzf2TY2xTT3CgHpuwy1BOQTZGjCY6DV56McayCgr14PlbmAFcb05iu7cdgtGVpE39Ep6HiuBABCveWPN73nudY09UsxTW1YzrgPcHoxT9_fl1iLifK09THewCEwsPog8lXoVZRa2mjZQrJJOlQ8hVNAV1iVUhQx5tgUJzYoPIUszK80laKsbqpPXvxHI4heMjidbG_WsH3XyI1SUj3C0Nifl52gpZD5LpEwyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/817b2c792b.mp4?token=DcZyov1JMAPFlTs1_cOpeuD6XvVz8-mH9jmo_Z1PukvzpXc_CYTH768LweU5PcZYPFtoLid0c2sQmTmEYbDURpdg03PKeSa4g_x3Me3-kBmuSJ1XtIzf2TY2xTT3CgHpuwy1BOQTZGjCY6DV56McayCgr14PlbmAFcb05iu7cdgtGVpE39Ep6HiuBABCveWPN73nudY09UsxTW1YzrgPcHoxT9_fl1iLifK09THewCEwsPog8lXoVZRa2mjZQrJJOlQ8hVNAV1iVUhQx5tgUJzYoPIUszK80laKsbqpPXvxHI4heMjidbG_WsH3XyI1SUj3C0Nifl52gpZD5LpEwyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاهده یک مین دریایی بزرگ در تنگه هرمز نزدیک عمان
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/655035" target="_blank">📅 17:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655034">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
کشتی آزاد نوجوانان ایران قهرمان آسیا شد
🔹
تیم ملی کشتی آزاد نوجوانان ایران در پایان رقابت‌های کشتی آزاد نوجوانان قهرمانی آسیا در ویتنام، با کسب ۴ مدال طلا، ۲ مدال نقره و ۲ مدال برنز و مجموع ۱۷۸ امتیاز به عنوان قهرمانی دست یافت.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/655034" target="_blank">📅 17:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655033">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1acebe8b5.mp4?token=Pvdgwe7dLLnFwaB_tBZuDPDX3CEUnLYV5U_dM9yRqdwyA5C5p0TsOc-aGlGCmvntcD723y65ujcYdf6U-mH2NZx8gxbGO4l424y7jPHJZ25JJrKQOqXlbFjRMFokvW3bnS8bkfGotRiKpQKhXhG8IcorJ7Ly5XqB4-7KzW0cuOVhIIO9d-oE4QjIhdAuwjZxvaiLVIDoeoQlvbu2Aa1cSjn4HPPPD3HLiX1Dc-Fq3csU2rcSEA2tmvHGLgDVK6Bf1ye16EKRte31uJ-nojV45jMCaqugumrwa8Z-mRd9jVQSqg2mXgZaUTSjF0KoDksOl0nI1u_qQc8OpUgu6W5oZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1acebe8b5.mp4?token=Pvdgwe7dLLnFwaB_tBZuDPDX3CEUnLYV5U_dM9yRqdwyA5C5p0TsOc-aGlGCmvntcD723y65ujcYdf6U-mH2NZx8gxbGO4l424y7jPHJZ25JJrKQOqXlbFjRMFokvW3bnS8bkfGotRiKpQKhXhG8IcorJ7Ly5XqB4-7KzW0cuOVhIIO9d-oE4QjIhdAuwjZxvaiLVIDoeoQlvbu2Aa1cSjn4HPPPD3HLiX1Dc-Fq3csU2rcSEA2tmvHGLgDVK6Bf1ye16EKRte31uJ-nojV45jMCaqugumrwa8Z-mRd9jVQSqg2mXgZaUTSjF0KoDksOl0nI1u_qQc8OpUgu6W5oZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور سرمایه‌گذاری حرفه‌ای انجام بدیم؟
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/655033" target="_blank">📅 17:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655031">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
کشف محمولۀ تجهیزات ضدامنیتی اپتیکی در منطقۀ مرزی ارومیه
قرارگاه حمزه سیدالشهدا نیروی زمینی سپاه:
🔹
محمولۀ تجهیزات اپتیکی شامل مقادیر قابل توجهی انواع دوربین‌های پیشرفته و تجهیزات شناسایی با کاربردهای نظامی از گروهک‌های تجزیه‌طلب در روستاهای مرزی ارومیه کشف شد.
#اخبار_اذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/655031" target="_blank">📅 16:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655027">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mPrG765-H7lHJW8A9udRmB1441AeysEGIyyc0gysyAd9LMDHLqAT6SN05go9ESXD-mxdg-NVl4n3cZwrB7oCiMjPxDeQJjTW95tYHmN57BV_S1t0XoS0gtj9QGERuFBN_ASP80V_K6eTx1jWfw9MbgR_OY2W9YRVVMg7MeoEWJAyKfr7mzYEiWBdvPhfGV-DKh94N7KCfql-yJAL9Kgj202nWNVYqgNvK3qEtqVZWJ0iP1GZA9zeWMSb5TeOXytSgBdz0mfdXyCDB0u8OOqCCAlMYicMy0qbufVxZKXyUS5lW46XcdibOKBiB5-_BiWX7P-5_P2xiUH5xi3mC89UtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cK4XIIJBvSyQiQ_wyav95Eri104dPZy4R1neOMRBW-pR--vG9lfOSGyrSePg6DZc__cJCsHQRDK9xAslO_QO1aGiwGv_iJ6-EX6M1E6f6yl3Mu7HziH5Q4aOGntavuSFslol8Hfs1dWDDMO5K8ZNwF9is4U3vstn9RODGk0gIEqk-cIrNm7G7Q4jU52nXkIVZ97H0tzhxdcOQn6-QyPEnDr5nzJAPKHfA1gTycCFXI4cV761WM-Q0NTwf_rqkZVhsR_M3Cir4fuWTToGvrbdJsQ-ITgaGGK9Kk18caUTaAW8YfG0KmrfvPoBbFd3ryP6iVWoQ2AjCEg_NHlPQ7UIEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PigiLJS3tceOAE3DoXacwga04OITeKwKV-SsjgdH5syKtI6kRs9VaxU2z2A6hUq2nMei9We1_Qs9Ovd3_PQa9Ak7yjLJeeaaQFXeuelRUcLdyFgdeBNuPgBiYkizlAan4a_Oa2OGawf5F8ulmvgcN92gy7c2hakxB7iR4ob_7suDKLIbv5QCFxfO1oCGxPQkT5G56RAclBYzZjg237UdIwm_4OG4h0R2H_zqviK2ehl-ZqfAu1dOo1X_OCl7ZTk0X18zYB4yTxGRcL7hNRovWtSbd7GR8Vt1PcqR5Lc7X7D0qENF906qPclTaYjICdiAZApEFluzInfCqWPHCLlgpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sz0yzLKedBdAFKYekcW6oJtF3Elx0R2nCnyE5Y096tjYZBmvi79FW1i2McXEUYlebVOyBOOeUS-Bw2zJR6z-wUOVKn7_5_0YmvvqI9y1ZSt3byHTW0xr55nHGiuIU2lfnz2c0lZ7ePMplZrD_Uw1pDhqW8p9NP61KhCw3j2EzF99ythuKRQFd46XYJFuPFOFutd55yO96qhxbGcKlucFB-CB89txQWRl38A1rvN9ncXUj_AKW3qkf_RMxyQrJK2MsXx6QoiNTYQ--KEZRsExnlBUrSkAtWbJGMAzB-MHRsajcapmVYBbxj0lC-3wnXboDlWdVcvbjzQupMu1jisCBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
طعنه گروه «حنظله» به رئیس اف‌بی‌آی درباره جایزه ۱۰ میلیون دلاری
🔹
گروه هکری «حنظله» با انتشار تصاویر هک‌شده از «کاش پاتل»، رئیس اف‌بی‌آی، ضمن به سخره گرفتن او، با لحنی کنایه‌آمیز خواستار پرداخت جایزه ۱۰ میلیون دلاری تعیین‌شده برای دستگیری اعضای این گروه شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/655027" target="_blank">📅 16:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655026">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BY70U4RQtfTqSGaoeH3--bEUWgYdycXqKyKvNbVXq2aFCELJxIQ2QT3rZZyBQnorAvNmgjJfYrSHP4Kcs_rRlQ8s2cUxBMROIUVSxs4ijzsEBXnbToHBRhJAlbQ71gaFk4PAj0jxbWNOePnD7fJNj-wyZUY0DDKDZwrmrSjRYzOuYQJcyoyeITvwVteAEX2rBJQ86_YT0ND9D_tR-yfkNFuHHMdv5Tz5OTkepaGvABaeSjuenfmfPHH1GlCClU1g9Q0jMb6UbbWG3GPmzY1z9IaOr1PTdSDVG_PimV85rTHacboiTAMwTT4JGcNOgPCM-SkyTC04CzPfnjP_WQKHlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با این پرامپت گزارش ارزیابی زیبایی‌شناسی چهره‌ات را دریافت کن
Create a clean, minimal, high-end facial aesthetic report based on the uploaded photo, using a black-on-white editorial design with thin linework, rounded cards, generous spacing, modern typography, and a refined luxury feel. Include an isolated front-facing image of the face, presented as an analytical attractiveness-assessment diagram. Provide an honest, objective evaluation of facial attractiveness potential, avoiding excessive flattery and focusing on symmetry, facial thirds, overall proportions, eye spacing and shape, nose harmony, lip proportions, jawline, chin, cheekbone structure, skin texture and tone, hairline, hairstyle, grooming, overall facial harmony, and photogenic potential. Assign clear, realistic scores to each major category, along with one overall attractiveness-potential score, keeping the ratings grounded, useful, and not artificially inflated. Include practical, achievable recommendations to improve attractiveness-potential, covering grooming, haircut, facial hair, skincare, eyebrow shaping, posture, weight loss, minor aesthetic procedures, styling, and photo presentation. Maintain a refined, direct, constructive tone that feels elegant, credible, and easy to understand, with an emphasis on actionable improvement that build on the subject's existing strengths.
All visible text in the final report must be written in fluent Persian, with correct right-to-left layout, accurate Persian typography, clean spacing, and no English text anywhere.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/655026" target="_blank">📅 16:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655025">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcee3d1a93.mp4?token=F8u5Q9hTGAVc1EZ7-r5DVk8mUVgohJgqsqVnATKpdTv25hncAhX2oCyBpNxmQaYxICVyDjiTGWtJ2bvOoZai5MIeb7eBnMXtFp9v_viUtAw3GxVZwXgfmo4CPqUbkT3zb_Kp4SXOxSWB4ECb_YZxgHM3eIW1qVrYHgN55FFHCffCn4Bv39gxdzzXVwq4x7jLuaYOvFgdTk--lTnEah-v7P8p87ivL2gUjYe2ooI0BS2RgCd8Rm388f5aORlcEyCdeO-WBc53BEz2eeP9g4XVsAAESdGsXtDUKotJvQPj8w8ANg3r_X__zBw5Z4W5VEDWkCyARw_Poa9mMJ_91Ed-6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcee3d1a93.mp4?token=F8u5Q9hTGAVc1EZ7-r5DVk8mUVgohJgqsqVnATKpdTv25hncAhX2oCyBpNxmQaYxICVyDjiTGWtJ2bvOoZai5MIeb7eBnMXtFp9v_viUtAw3GxVZwXgfmo4CPqUbkT3zb_Kp4SXOxSWB4ECb_YZxgHM3eIW1qVrYHgN55FFHCffCn4Bv39gxdzzXVwq4x7jLuaYOvFgdTk--lTnEah-v7P8p87ivL2gUjYe2ooI0BS2RgCd8Rm388f5aORlcEyCdeO-WBc53BEz2eeP9g4XVsAAESdGsXtDUKotJvQPj8w8ANg3r_X__zBw5Z4W5VEDWkCyARw_Poa9mMJ_91Ed-6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ذوق یک پسر بچه بعد از وصل شدن اینترنت
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/655025" target="_blank">📅 16:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655024">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
نیویورک‌تایمز: ترامپ شرایط سخت‌تری را برای چارچوب صلح به ایران ارسال کرده است
نیویورک‌تایمز مدعی شد:
🔹
ترامپ عناصری از پیش‌نویس توافق را اصلاح کرده و آن را برای بررسی به تهران بازگردانده است.
🔹
او نگران بخش‌هایی از توافق احتمالی است که شامل آزادسازی دارایی‌های مسدود شده برای ایرانیان می‌شود.
🔹
ترامپ از مدت زمانی که طول کشیده تا ایران به پیشنهادات واشنگتن پاسخ دهد، ناامید شده است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/655024" target="_blank">📅 15:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655023">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معاونت راهبردی رئیس جمهور: ۷۰٪ شرکت‌کنندگان در تجمعات شبانه زنان هستند
🔹
سی‌ان‌ان: ایران ۵۰ ورودی از ۶۹ ورودی تونل‌های تاسیسات هدف قرارگرفته موشکی را باز کرده است
🔹
ادعای نتانیاهو: من به ارتش اسرائیل دستور دادم تا دامنه عملیات در لبنان را گسترش دهد
🔹
وزیر‌خارجه فرانسه: بازگشایی تنگه هرمز اولویت است تا بیش از این هزینه جنگی غیرمرتبط را نپردازیم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/655023" target="_blank">📅 15:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655022">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ناتو: ممکن است در موضوع بازگشایی تنگه هرمز مداخله کنیم
رئیس کمیته نظامی ناتو:
🔹
کشورهای عضو ناتو در حال نزدیک کردن نیروهای خود در خلیج فارس هستند و در صورت فراهم شدن شرایط در مساله تنگه هرمز مداخله خواهیم کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/655022" target="_blank">📅 15:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655021">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHggPFi59qF-Fa4lAAqzdUzGeMJ3EZ7_ZsCyD6ShPZmmrDW6d5Jf1EyCruINh4ftNOp6Rqj9mljVpqHTEsJqyNgbfbJc4vEQBmCmhudChCs2qoJNgwjiUj7X0U9Yyk4nVihZexrnvkoA4K-tNJdjFW3zZliJV70ii_tSo9MOoUbWqFuHzOn4WIfXlvZLN5Gy2hZAkdHj0L0VQKe0y6CGR2O6logVG3fRQFb7lV5M4Nu6cM4Whaq_4nnqFLzMkaym6o3THmGFLiOkAOkpmiSP7c2OkzEyYUKBUYXCkULDrkYVm6OBN7wfoLgVbUgKCfdSBhhbXQ4yML6R_FB-RxSatg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس وایرال شده از استایل جدید صابر ابر در یک نمایشگاه هنری سوژه رسانه‌ها شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/655021" target="_blank">📅 15:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655020">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
گردش مالی نیم میلیارد دلاری کنسرت کانیه وست در استانبول
🔹
کنسرت کانیه وست در استانبول با حضور ۱۱۸ هزار نفر رکوردشکنی کرد. در صورت فرض حضور ۱۰۰ هزار گردشگر خارجی در این مراسم و میانگین هزینه ۵ هزار دلار برای هر نفر، این کنسرت می‌تواند حدود نیم میلیارد دلار گردش مالی ایجاد کرده باشد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/655020" target="_blank">📅 15:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655019">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
قتل پدر توسط پسر نوجوان به خاطر بیکاری
🔹
مشاجره یک خانواده ارمنی در محله مجیدیه تهران به جنایت انجامید. پسر نوجوان پس از درگیری لفظی بر سر بیکاری و عدم توانایی در پیدا کردن شغل، با چند ضربه چاقو پدر سالخورده خود را به قتل رساند. متهم دستگیر شده و به جرم خود اعتراف کرده است. پرونده برای بررسی جزئیات بیشتر در دست تحقیق است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/655019" target="_blank">📅 15:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655018">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
ادعای فاکس‌نیوز درباره آخرین وضعیت مذاکرات ایران و آمریکا
فاکس‌نیوز مدعی شد:
🔹
بنابر گزارشات جدید، ترامپ شرایط توافق با ایران را سخت‌تر کرده و شروط جدیدی در موضوعات هسته‌ای و تنگه هرمز اضافه کرده است.
🔹
پاسخ تهران ممکن است چند روز طول بکشد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/655018" target="_blank">📅 15:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655017">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7106a3dc12.mp4?token=AZqffglLuC4q1EpLsUBcpXhuKA54C4wQZ7sMWuVl5PUqHTqqmGLFsLFJ6N9m52GAXKboBkozW5vzURF81IdtncfToY_3zHdm7AL_xjSbyAKPrgqs_mP_lCJQVpkl8K2Aneu3QpUGUdC9kgg1vjQymgU0L-ABUj0EoCU8mTQeDfUOITlTkcH6Tql37u7IDo32fKdyNT_7ObsW1ScaVqa_V6_wE9ujWLOfbQt8oIkzsvY89oudWO-H0VR3WtbXszpRUr-fPEIx344UxvgEihTT3eR_KwULJ6CEWs8R2PZQ6jbPzVsxv1WqdZi88VRbIw-78hk6A7fCQmpk20OWhDKLrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7106a3dc12.mp4?token=AZqffglLuC4q1EpLsUBcpXhuKA54C4wQZ7sMWuVl5PUqHTqqmGLFsLFJ6N9m52GAXKboBkozW5vzURF81IdtncfToY_3zHdm7AL_xjSbyAKPrgqs_mP_lCJQVpkl8K2Aneu3QpUGUdC9kgg1vjQymgU0L-ABUj0EoCU8mTQeDfUOITlTkcH6Tql37u7IDo32fKdyNT_7ObsW1ScaVqa_V6_wE9ujWLOfbQt8oIkzsvY89oudWO-H0VR3WtbXszpRUr-fPEIx344UxvgEihTT3eR_KwULJ6CEWs8R2PZQ6jbPzVsxv1WqdZi88VRbIw-78hk6A7fCQmpk20OWhDKLrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرم امیرالمومنین(ع) مهیای عید غدیر می‌شود
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/655017" target="_blank">📅 15:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655015">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 آیا شما از دخانیات (سیگار، قلیان، ویپ و...) استفاده می‌کنید؛ چگونه و به چه مقدار؟</h4>
<ul>
<li>✓ بله، به صورت مستمر و روزانه</li>
<li>✓ بله، به صورت تفننی و صرفاً در شرایط یا جمع‌های خاص</li>
<li>✓ در گذشته بله، اما در حال حاضر استفاده نمی‌کنم</li>
<li>✓ خیر؛ تا بحال هیچگونه مصرف دخانیات نداشته‌ام</li>
</ul>
</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/655015" target="_blank">📅 14:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655014">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
توافق نهایی هنوز حاصل نشده و امکان منتفی شدن آن همچنان وجود دارد
تسنیم:
🔹
تبادل پیام‌ها میان ایران و آمریکا درباره متن تفاهم‌نامه احتمالی همچنان ادامه دارد و دو طرف به صورت متناوب اصلاحیه‌هایی را مطرح می‌کنند.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/655014" target="_blank">📅 14:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655012">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fNGg8obo3mWw3sM-wJuJoWLbdMncSFvjhiCQVklhBmsQ8meC1WHOKE9kSg7BFONbzw3uv0AIhTcWuvVgkE2q0QYvOXbQkP7UxN8E3LXtGqfLY5HEE1Ob0thVxTvNyzg2pDY8aw-1GhFRVpWJ6N3uJubo4coHv3B0PnbTHbK0BY1mz04YKLR1dkBG8FZL2XwyCx64DBz5TDsbnet4lVlkJK-K2gBlsYVsNA_CLqthIR8TrumMoqWJYnfZrcsLhS7t5WZOLP-SqE3xFb3GKInwyooYZrXX8FjcKzLlm1O2aDZ2mHnGiIh5fMRGCL2SSkA6BymSC-5IZhp88CL5ykEFvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T6YJQNLvqoesdyccqqXUq2CddbVKQPj6eI2yKe--RHa07X2lOprt8JPx-dZ9cjcdEXVajVo7VcNvW97HfV7BN5QGKnqtD708cuJ3HOCqnwy8gdq2Z1GgB1rQLN-JkRS0zsUe6XA2_ha3GF8l7199mXo2-be5UcDHew-MPcAGaSmlSlAytKU_7uiNw5AYfV3Mz5i8o_rEw7lYvzXpImHXH1S2XC5uuoYfLfx9dzqyJrmSWNbgoxAefXnJoFkLEGG4BE0szqI9t-N4NkFi-fFObt4PCjoaO0DwCSwJ_qVE3zE0S8TCn2SA4wa0qCUDalj_VjPb8rXaB4_4wZ5VkRrNRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قالیکوه، الیگودرز زیبا
🇮🇷
#ایران_زیبا
#اخبار_لرستان
در فضای مجازی
👇
@akhbarlorestan</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/655012" target="_blank">📅 14:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655011">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsdwggwXwfKVS4_K4okOPGZSIEnZueZP4VSdll8OKruupv602Ass9Al7GBVs_eO-NfPDOGqXwaJrYEENndEcXqyQ9Vsyt1l3EnWp6UMpJe0yh3uUTY_pwQ8lbYKQy4DQ6Ffd3UDjbOtAJm48tZQUdxY7Yf28QHf5rNXKVnoHKSnbOruGlTrXMKY9CAkfs-AMcdWyJluv3pDUpUXnD-xALI4cHnCt4Q8ajtpJn_W40Mx6lsnPrqJEs1Kov09_-puyQbMqfA5K_h3ai3TLev1Er2-fKCWXsA9Q3exo14mM67IjiCaPpCtnrEZrfrBIdW1ITqiPejQFB9gjYezRBOD2AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیما، پیشران بانكداری دیجیتال/ بیش از یك میلیون فقره تسهیلات از طریق سكوی دیجیتال بانك ملت پرداخت شد
🔹
در کمتر از ۸ ماه پس از آغاز به کار دیما به عنوان سکوی بانکداری دیجیتال بانک ملت، تعداد تسهیلات خرد اعطایی از طریق این سکو به صورت کاملا غیرحضوری، با ثبت یک رکورد جدید از مرز یک میلیون فقره عبور کرد.
🔹
دیما که از مهرماه سال گذشته در دسترس مشتریان بانک ملت قرار گرفته است، امروز با بیش از دو میلیون و ۵۰۰ هزار کاربر، به یکی از موفق‌ترین نمونه‌های تحول دیجیتال در نظام بانکی کشور تبدیل شده و نقش مهمی در توسعه خدمات غیرحضوری بانک ملت ایفا می‌کند.
🔹
بر اساس آمارهای ثبت‌شده تاکنون، تعداد تسهیلات اعطایی از طریق دیما به بیش از یک میلیون فقره رسیده که این تسهیلات شامل طیف متنوعی از محصولات اعتباری و تأمین مالی خرد از جمله تسهیلات پلکانی (میکرولون)، تسهیلات مبتنی بر سپرده‌گذاری (نیک‌وام)، تسهیلات سازمانی(فرهنگ وام)، تسهیلات ویژه کادر درمان، تسهیلات حمایتی حفظ اشتغال بنگاه‌های تک‌نفره و اعتبار خرید «دیماپی» است که تمامی مراحل به‌صورت کاملاً غیرحضوری انجام می‌شود.
لینک عضویت در دیما</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/655011" target="_blank">📅 14:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655010">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32db4f3eed.mp4?token=vnSdepNxX707PdZnzJ17LkZbSVffg2GkWt3IWT250Ry6LaF1P6l9FKhqczbFWNHiHczMy3wj7IQYT0obkW38sbFkcCNV9vM0OtmgzNzpkEaisSk0Uz41A15f0VNsgKlliQMBzo1JXu6fE4oOJlInkxyo4oObdwpMlzfDDdKk97etTlSW3xLoree2R-m5_f_ROWqdVXSES-79qujpRxmyYyLV69W7jdWsP00cbRIvo7WbQz3NPrtOBQs_b_anjDik0V6BUyoqKiZwgamRCtsabh9gw3_bj-ftQ2mEbkfj24k6zZVudn_2WciNtgThb_psZTVUZ0Ifl9lc3DtsZ2hWNZV5CFDr_eW0kcvsdY7QGFiQ85-qYcb5O_hutldxritwsdPKGM24MWMiydWmWRQGmdmzB7M9Cvn8sWt1g0HkjQ1CXUEnQXooMSVJzD7GnDc93lVkf5HG8yOgiD_NyGtQxZEW5bj66HIItp0fxOgK2KtTie9tPGxSDO4LOQk3tZ2o-vxhz_Sj_pSoIu3OYWhOZIOQLeWWYsNaiS3BrnkQP5OVzfFK39xHPIqd8dv0PzhIqSuO1SY2i3_9L8IcQJyE3zCC2CzoDwexGVkEgAWrx-olBZUanfifp2tyzmvmQBJoje5S9fJ0nd5oxUrorCix7snrzxWPtYotM3rAi1OF4ZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32db4f3eed.mp4?token=vnSdepNxX707PdZnzJ17LkZbSVffg2GkWt3IWT250Ry6LaF1P6l9FKhqczbFWNHiHczMy3wj7IQYT0obkW38sbFkcCNV9vM0OtmgzNzpkEaisSk0Uz41A15f0VNsgKlliQMBzo1JXu6fE4oOJlInkxyo4oObdwpMlzfDDdKk97etTlSW3xLoree2R-m5_f_ROWqdVXSES-79qujpRxmyYyLV69W7jdWsP00cbRIvo7WbQz3NPrtOBQs_b_anjDik0V6BUyoqKiZwgamRCtsabh9gw3_bj-ftQ2mEbkfj24k6zZVudn_2WciNtgThb_psZTVUZ0Ifl9lc3DtsZ2hWNZV5CFDr_eW0kcvsdY7QGFiQ85-qYcb5O_hutldxritwsdPKGM24MWMiydWmWRQGmdmzB7M9Cvn8sWt1g0HkjQ1CXUEnQXooMSVJzD7GnDc93lVkf5HG8yOgiD_NyGtQxZEW5bj66HIItp0fxOgK2KtTie9tPGxSDO4LOQk3tZ2o-vxhz_Sj_pSoIu3OYWhOZIOQLeWWYsNaiS3BrnkQP5OVzfFK39xHPIqd8dv0PzhIqSuO1SY2i3_9L8IcQJyE3zCC2CzoDwexGVkEgAWrx-olBZUanfifp2tyzmvmQBJoje5S9fJ0nd5oxUrorCix7snrzxWPtYotM3rAi1OF4ZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عضو ناوگان صمود: در زمان بازداشت مورد تجاوز جنسی قرار گرفتم
جولیت لامونت، مستندساز استرالیایی و عضو ناوگان صمود:
🔹
در جریان توقیف و بازداشت توسط ارتش اسرائیل در ماه مه، وقتی دستبند و پابند داشته، داخل یک کانتینر تاریک توسط یک سرباز اسرائیلی مورد تجاوز جنسی قرار گرفته‌ام.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/655010" target="_blank">📅 14:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655009">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ادعای آکسیوس: احتمال روشن شدن سرنوشت توافق ایران و آمریکا تا پایان هفته آینده
🔹
طبق گزارش آکسیوس، یک مقام ارشد در دولت دونالد ترامپ اعلام کرد که احتمال دارد تا پایان هفته آینده وضعیت توافق احتمالی میان آمریکا و ایران روشن شود و واشنگتن برای دریافت پاسخ تهران آماده صبر کردن است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/655009" target="_blank">📅 14:24 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
