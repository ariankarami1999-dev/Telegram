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
<img src="https://cdn4.telesco.pe/file/QpcFfaDThY3BvG0_KwCOuHz9pZtTikXOiYxM-puMw20t6md_vRPfnobrcl-M5z1_MYzllKTKz6sAkzkn9PQ6ORlIaXBxscpZEubJDqiSp_6Q-28PEAzeOoCGpdsL_a4T_uApOu-DOmzXqBOwGck8QtPQ2TSqJHPTKlZ7VaOyskyXZC0KWagLESW5BfOWWC6u1fdoxH9w30jeCFE74CTnuJwPkPmuw6IN4eLCYRwe2EfQOz1sePf-MA000DiQLeJvhg5AwySM0QU1Whoa55pJBKdhemf_u3fkKOBwsi2AinWlw6Kq9zUWOfXW6MbuZgF5UXOAbg3fEomt1ljXgnLaPQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 22:38:20</div>
<hr>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از حمله موشکی ج‌ا به اسرائیل.
🚨
هشدار حمله موشکی در شمال اسرائیل
🚨
قطر آسمان خود را بست.</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/farahmand_alipour/5361" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5360">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ارتش اسرائیل در حال آمادگی برای مقابله با موشک‌های جمهوری اسلامی
فردا : تعطیلی کلاس‌های درس در اسرائیل.
اسرائیل : نشانه‌هایی از احتمال حمله موشکی ج‌ا به اسرائیل وجود دارد.</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farahmand_alipour/5360" target="_blank">📅 22:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
آسمان‌های ایران و اسرائیل بسته شدند.
🔺
امروز ‌و در پی حمله موشکی حزب‌الله به شمال اسرائیل، ارتش اسرائیل  به مرکز فرماندهی حزب‌الله در بیروت حمله کرد.
جمهوری اسلامی چند روز پیش به اسرائیل هشدار داده بود که به بیرون حمله نکند و در غیر این صورت به اسرائیل حمله خواهد کرد.
مقامات جمهوری اسلامی امروز اسرائیل را تهدید به انجام حمله کرده‌اند.  اسرائیل نیز هشدار داده که هرگونه حمله ج‌ا به این کشور را شروع یک جنگ تمام عیار تلقی خواهد کرد.</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farahmand_alipour/5359" target="_blank">📅 22:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiiMXvXkRe8VgTrYXjP_Z42DFCxQ9CGqpbL6d0C2GPh9ULhU-QIfKU4FcH8Mo8Sqff_7iBwJFkwmYFt7RytM35jhfjPS-cbv0EU4-8sDrTr9zOejBXbOZvaT19M2xmK9Sdn70S0WyVEB8jQhXjWNqaZ-kNv-DzhTRH_I0qBpZ8kT1kCnbRRqrpMu_qPY8vYvbUk3eZcUitr0kzpyFPOccnaLvHB8foi0jTSgnYQB5133lyKNPIm1LITXf4QqVIjcCjNmHkRosHSayeh6RPLA9Rz-OgXNjDZoI0XZ5dmuR4K8jAIxo43j_QqhvXO4n6RlUd2e0udOfKWtmOCfJvExqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز تهران - استانبول تغییر جهت داد و به تهران بازگشت.
گزارش‌ها : حداقل سه پرواز ایران مسیر خود را تغییر دادند.
گزارش‌هایی از بسته شدن آسمان ایران.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farahmand_alipour/5358" target="_blank">📅 22:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ارزیابی برخی رسانه‌ها : جمهوری اسلامی به جای اسرائیل به کشورهای عربی حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/5357" target="_blank">📅 21:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
هشدار اسرائیل به جمهوری اسلامی:
هر‌ حمله‌ای به اسرائیل به معنای آغاز یک جنگ تمام عیار خواهد بود.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/5356" target="_blank">📅 21:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اگر فرضا جمهوری اسلامی برای کمک به حزب‌الله، وارد جنگ شد و در پاسخ اسرائیل زیرساخت‌های ایران رو زد، اینبار چطوری میخوان توجیه‌اش کنن؟</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/5355" target="_blank">📅 20:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">جنگ خارجی نباید به اذن و دستور فرمانده کل قوا باشه؟
نباید قاعدتا مجتبی فرمان بده؟</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/5354" target="_blank">📅 20:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
قرارگاه خاتم سپاه : به حمله اسرائیل به ضاحیه بیروت پاسخ میدهیم.
🚨
اژه‌ای : حزب‌الله جان ایران است !
🚨
قالیباف : فقط زبان زور می‌فهمند.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5353" target="_blank">📅 20:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cH6yrJdGXD9hgPYCMzg8JrSghM6SX5mk0I0iq7ffQmyjln6dBObrTO2icOW0cwxmGi-nx45x0TCzTDc7QGbeA5NYYVM3uuV8mQjl5oX_MV2A1Udo1ejksNGz77HSO5Pq5jQGoxlZC9y8ddiO3aqeUrFBXBa63YFvg2V1zzLZ0Qnf_OLVHOGsTMAV1upVxZwXvQsMonYJ_x3DSDF0F8eQ1Q8seRGHgaWqLaCIYPY7CI3MVNSarxtJPkvBsHG0ptQ4QmBSaoKZZWHLfeebZLQtb3I7TwIBv1NsdVZN41lf9PHQPSne1eQHsBarogJsrIb5dYbBo8OwBmQfiQN5EbqjEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!  در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5352" target="_blank">📅 19:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8D6xoVzq6om_kzaBAPJOjFiSt6SsLtMo7qEujscJ3E6-ZtICWfKjZ4aSKCGm7XbWBId7elHZwqaYv-DvNsN3XlBbac_IZKL0AOmr-R5NNrab3PEQk0s_nIxuF0TRb54fILxeMeoqAe2EbxUXvLglOJOiygdwvh1ssBLkP0ffzKk5odXzPaDuUj43TtJZOhltLZRoHCqqRu7J4WXNh0RV7lhtD_N3_nYlC8t-0gM_EKBlQaBj71sBNEYFq0_DjxQW3Fc5-f0ubWPzil_d-k2jkapEyixVixI_mysPwM1YN18K6sNORfkKX5G5IlPpYWYZXcTnM5V7V43EZGDGG3EqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!
در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5351" target="_blank">📅 18:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucbQr7JsN_P1dZ3G5yxDVBNHcB7tJn5PBy42cO4n1l3zJi876RJ__qCQTAfJBpk16JKmH1D0rPp1JkGorFu9_3a-9_caMnosRrnIF93oY4nI1byQJzhrDIMMP1Hx80kknCCqIESFuHrAmQEEIzmsPYotl0wnA8av94TY5NBE4Chvpxuz903t72ZQbNd5LJ4H-IU9EPvcZjIgcpF2A_7vXGYQ8xNRlirsevsJBEhJTrsWCl7J76NPaea8ZUi4CDyk0TfeBEfF4n_hSIQqEbPQWG_JsEtDMVx_yIXH467FwPIazH53PPeTA40gotqsa_50E8eD8WBPxivkzUCXh8lT5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی حز‌ب‌الله،
اسرائیل به جنوب بیروت
(منطقه شیعه نشین ضاحیه) حمله کرد، چرا مهمه؟
چون جمهوری اسلامی هفته گذشته تهدید کرده بود  که اگر حمله‌ای به بیروت شود،
به اسرائیل حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5350" target="_blank">📅 18:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=rFMSfBiP0o8UCRXXcfRabEDH_4_saLKoi__E6hrCGCOZg6ZdEtgJzHe5spy6aTBhFegqzv0-qMsp4jA2vpF2CIrxVNBAkzY3My5ZP1dK2I1txHHSDEqZo3sprXfhGDArS3-ffMzKOYANVyNQeXAvYVGcERcJ--UzWROYbFXhPnijo8hQb-G2KOaYgglOrWAj54Fv-_75eSuKMN461Zg4TKQyofFbiSiacm5q7a-IP36fAh5DnJ9MtkBK_R3G-lrHs5bMoiDMIidoIy2zpzVROKsbiwEGoYacSyZ7Ulq6t_Of8ppc-5xc7uyKv6kAL56ejXS2IY3mN2YAMVbQWjzoKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=rFMSfBiP0o8UCRXXcfRabEDH_4_saLKoi__E6hrCGCOZg6ZdEtgJzHe5spy6aTBhFegqzv0-qMsp4jA2vpF2CIrxVNBAkzY3My5ZP1dK2I1txHHSDEqZo3sprXfhGDArS3-ffMzKOYANVyNQeXAvYVGcERcJ--UzWROYbFXhPnijo8hQb-G2KOaYgglOrWAj54Fv-_75eSuKMN461Zg4TKQyofFbiSiacm5q7a-IP36fAh5DnJ9MtkBK_R3G-lrHs5bMoiDMIidoIy2zpzVROKsbiwEGoYacSyZ7Ulq6t_Of8ppc-5xc7uyKv6kAL56ejXS2IY3mN2YAMVbQWjzoKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش اسرائیل به ضاحیه بیروت حمله کرد،  عراقچی ۴ روز پیش به شبکه المیادین  (شبکه لبنانی با پول ایران) :  اگر اسرائیل به بیروت حمله کند  اصلا تحمل نخواهیم کرد  و این یعنی شکست آتش بس (بین ایران و آمریکا)  و نیروهای مسلح ما پاسخ خواهند داد.  به کشورهای دیگه…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5349" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=NTT5KlDGyP1BqdKtMdELcIqk1MrZkrF_OXESmrNpC3CBMTqYFmsDRZJOz-yMro73IcvMuhrIAvGNgzMl6IV-ExYKL03_pLLgR-3IB6L4jgkmu7cySZq2DEqbfSt1voF2_KBJS612Pwb27mH8xkhJ9ywEpdeyTdxmnzANWzaIBJzzoaRw_hURGbqQUHCN8JwO9l6RRTISUPWsO4eo75h0RHKLeapPbD5KWY50BRDeoy1c8C0yD47ZmMuPpG8dqNhfjpK-TtPKlrpvPjAD0us_AYMh3yxP0nvN9ywJ3xzQrb5qQHSEr0ehaOXGvKJ7idz6zxeDmJelYGHWGCmhlVM4cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=NTT5KlDGyP1BqdKtMdELcIqk1MrZkrF_OXESmrNpC3CBMTqYFmsDRZJOz-yMro73IcvMuhrIAvGNgzMl6IV-ExYKL03_pLLgR-3IB6L4jgkmu7cySZq2DEqbfSt1voF2_KBJS612Pwb27mH8xkhJ9ywEpdeyTdxmnzANWzaIBJzzoaRw_hURGbqQUHCN8JwO9l6RRTISUPWsO4eo75h0RHKLeapPbD5KWY50BRDeoy1c8C0yD47ZmMuPpG8dqNhfjpK-TtPKlrpvPjAD0us_AYMh3yxP0nvN9ywJ3xzQrb5qQHSEr0ehaOXGvKJ7idz6zxeDmJelYGHWGCmhlVM4cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش اسرائیل به ضاحیه بیروت حمله کرد،
عراقچی ۴ روز پیش به شبکه المیادین
(شبکه لبنانی با پول ایران) :
اگر اسرائیل به بیروت حمله کند
اصلا تحمل نخواهیم کرد
و این یعنی شکست آتش بس
(بین ایران و آمریکا)
و نیروهای مسلح ما پاسخ خواهند داد.
به کشورهای دیگه هم‌ گفتیم که در اثر اقدام اسرائیل جنگ‌ دوباره آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5348" target="_blank">📅 18:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=E2omNYCWWNVvdvzx930ZXfESi18XeCrDJgnTCPKDMsP4Z9MWUaiMjAElP1bruxkttRDNqcxrPj9bzgh89IJiXDZE7EQlwdh9dB3sY_lZw_kFZVeE8H4QeAEbjeYNunEmbnLsehsZWgOuKadXD3cbNfh3TXG44wA6eTXibJ-SI-uJm2xHUXSZOzsxPUEq2lnpH4CxAJw0vUIhQNhCOHOnJ6c8YYznlIbiEN1hMxmO2RUk0BBlXR9mmn3tOzai5DWGn7V4GDfDTbR8bngSR7BLPvTUSmGaOmzGoVgEZh-PfcAdoRVmWuC6T6AqqFO9BzuqNdFFMoXkTqw8cAIkn_ot-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=E2omNYCWWNVvdvzx930ZXfESi18XeCrDJgnTCPKDMsP4Z9MWUaiMjAElP1bruxkttRDNqcxrPj9bzgh89IJiXDZE7EQlwdh9dB3sY_lZw_kFZVeE8H4QeAEbjeYNunEmbnLsehsZWgOuKadXD3cbNfh3TXG44wA6eTXibJ-SI-uJm2xHUXSZOzsxPUEq2lnpH4CxAJw0vUIhQNhCOHOnJ6c8YYznlIbiEN1hMxmO2RUk0BBlXR9mmn3tOzai5DWGn7V4GDfDTbR8bngSR7BLPvTUSmGaOmzGoVgEZh-PfcAdoRVmWuC6T6AqqFO9BzuqNdFFMoXkTqw8cAIkn_ot-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو‌ رستم تهمتنی،
«چرا دیگه نمیزنی»؟؟
بله جنگ طلبها دیاسپورای ایرانی بودن!
نه اینها که ۴۷ ساله سیاست‌های
خصمانه و جنگ طلبانه دارن!
در دیماه وقتی مردم ایران رو قتل عام میکردن «حیدر حیدر» میگفتن، یک ماه بعدش شد «رستم رستم» !</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5347" target="_blank">📅 11:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co3k8KY8kGJvAP2AAndTAuIcDP096hiOqHTX4vN__zSrCUG0XWofcZCTx22ov7tmWhSiTc-vF74teZiqGYAFjm1a6DQH801ylGKPGAdqcqOaW6wViYyrTtuOfzifaUmsM0RwwoyV8VKlihrrsyyJpm9f2BD31PYqOQpRtWvIrhxh_Lde-QQMSYONGi7tQt-G9FBVZmySHCZcKOLvhHTdUNu3_NZRaLZeH7F7h5Vn6ufiMYQb7fokh-SNt3LlIBCawziVsp_q95a1wCExGQp_ayPotx57smXhxGaLlpPzT5FPSdrZvIbWTaNpDp-SkTt7fdVRt1PMBIh0ZmVKn11t4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد. در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5346" target="_blank">📅 11:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwsBSRMMsea8Rh-Jk6A36yJIVd2Vh3LgTWw11UH8i3TDitHOnAV7q4iH_7z9w0o2FB1l23z5s9UJCcy1DnMe_JwKFIBhS0IAlMEL2HnSPJSSEIDTTpD41poQ3z9xA4rR7FqE7zH03J3vxG6FsOTiJ_myZtzB5f2tdMZKCX5fLB2z6_84jpBkG7RrMfHoQW55-ajzkvQQdVX4kIkSlpkHTEY41Zy0yN9AFJbRo_WSGsim13CLiwBJhh8DrtrGjellCD6HETb9tuIdrzSPDD-YBRrN_OUV_huG0ScsuRwh2aMU1kOBD4qovMYzuEVwyEqkcXYtAwi1LWvSCxuJ28ilKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت
و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد.
در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5345" target="_blank">📅 11:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">کارشناس حکومتی : در اعتراضات دیماه ۱۴۰۴ حدود ۱۰۰ شهر سقوط کردند یا تا آستانه سقوط رفتند.
نهادهای امنیتی گزارش داده بودند که کار رژیم تمام است.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5344" target="_blank">📅 10:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
رویترز - آمریکا قصد دارد از پولهای بلوکه شده ایران، خسارت کشورهای عربی مورد حمله جمهوری اسلامی را پرداخت کند.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5343" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سفیر ج‌ا در مکزیک : ویزای اعضای تیم فوتبال برای آمریکا چند ساعته است، همان روز مسابقه وارد خاک آمریکا می‌شوند و در پایان بازی باید سریعا خاک آمریکا را ترک کنند.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5342" target="_blank">📅 00:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1Rb7vOKXYANEkdTdXUwNbKtOg-yTW5f-WxScQdtnNehTCQts1OMRXGiJHXuN-NvzLsoAbMuXaSRGF2nBuc93ChBu9zXRTZNqoy9ZTksUAp7KyDRfB5kjDi92z5gNuHB-5h2tBtgdb-8q2hY1A69K2-ted5wmOLhZR4FTjAn_Apr9ozSJgTRLFO4DCAeHIZuf-kpTCp20N5L36G6wCxcgJbJ5dPD_as9diM04QqAyF-4_kET89Au41qQdY5JLTuu8O8Y4Of5rUkaAMBm3J1fgTxJXIUHQTBPYVoLOwQYpZTJzsvYV1E7jkuKx4VW3oGDfVlPx9bbXLAOkv9_s6AgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه ویژه و مشترک رئیس ستاد ارتش پاکستان (عاصم منیر که روابط ویژه‌ای با ترامپ داره) و نخست وزیر پاکستان
برای مجتبی خامنه‌ای</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5341" target="_blank">📅 23:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rT1HP5i73BrF0rHXYPbRhvCwCCumQYuZRCouCsjRwTE9oUYOTje-d1Nb794nIcCKWPaAj4PhYi9gVXG3AIMTc1TsZGuT-riYOZzYUog_eFH7PFDGByqQ6Pa4yw3lXxRyRqcgybU76tjAg42P-Y4-fnprQ3YCQ-B_FGviFtb_lYluBuR6tiIBNEvZN-ibKDp8uzwXGaLiE1lrbsQAgA1QscyzS3GUQU7_KKaKnF9JLoXSLihkp61V-MIGMzmvb-Rpa-vNBSjkeN3Qn55zeXy9xC9NN0PtCRlvfEQHH4KlXGQLJ6G-ySbJRXUEQke_4hT5MWCsHnbPocMsy82x3kun3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونهایی که فرانسه و عربستان رو دارن
توی خونه‌هاشون نشستن،
ولی اونهایی که جمهوری اسلامی پشت و پناهشونه، رفتن توی گاراژ و انباری
و توالت اونها قایم شدن :)
با این توصیف، خوش به حال اونهایی که
جمهوری اسلامی پشت و پناهشون نیست!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5340" target="_blank">📅 19:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIHLbjKs0ssRziTkRTyQVS9g4bfVEU7EgdxfAge9Tw3ccVZDVxII0qKxt7HCr3564hrH3kjngdih8mthqx2pwg8Kid-SDxLzYIQRrSzjeepzXdSlWhCVG6wDawT_IaMVdjRECSWoDOWxSyhlPe5nfjgRsBN16SlsABMXpC-aE0qrP1DbcPsHw4VuV_WrHnzlNsH_DredIKg2sBuu63wzZScz6CxhFQbap-HevmzEh9c9XGYcu-Yyk956cE6sI3vWu6a6coh_nh7iVE7oflRnovPOLfRcV4QGBYFy_dBe6X94c2QrEuRH9cWHTKewMQj1esQd-4qAm4UVKpIYV9c17w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.   ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5339" target="_blank">📅 18:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9leVI_CaN5tmNIWiUgSumsdnV4nuK3H33lzg2RkplOyACuV8CgIfgr2fq8-Nn04WrXADnrSm6MFGZGi4l5LeQBxZypCZJA0aIReoH8yJJwbQHqTsAyQiusguwPLlUdm7GlEZbQj5cEy1HITl0iWL1GI7k_cXmBKoQ1kMIb-uJRjhDgzlNMpypgYP2nyuAd94ZABiXZM8EJijE0pTPspuF9wI8AEp5YKWgB0fwZfpG76g3S4zCeyyQGNEPUZI9aM_lU_eS2_ntEudumovxgwChQea5hGcZcHQ-BSLkPag-7NqlftRhlhZ51jsMRodm3umkcEQVtkz7_iTR0YqOEBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.
ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب الله از طرف دولت لبنان نیست! حزب‌الله برای شروع جنگ از دولت لبنان اجازه نمیگیره!
🔺
این جنگ رو حزب الله به لبنان کشاند و باعث شد یک چهارم جمعیت لبنان آواره بشن و یک پنجم خاکش اشغال بشه! به خاطر جمهوری اسلامی!
🔺
جنگ به خاطر لبنان و منافع ملی لبنان نبود! با اجازه دولت و مجلس و ارتش لبنان نبود! با سلاح لبنانی و پول لبنان نبود! به خاطر خامنه‌ای بود و با پول و سلاح جمهوری اسلامی!
🔺
تا الان هم برای خونخواهی خامنه‌ای بیش از ۳۵۰۰ لبنانی از جمله آنها ۶۰۰ کودک لبنانی!! به خاطر خونخواهی خامنه‌ای!  کشته شدند!
🔺
لبنان و اسرائیل ۲ روز پیش به توافق آتش‌بس رسیدند ، سپاه پاسداران اولین گروهی بود که بیانیه داد و آن را محکوم و رد کرد!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5338" target="_blank">📅 16:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lc9qTT9iwE9OJXleQEMWUtY1qGHNtmCLOcWYPRHcsYRu7u6r9zaFQ-G3-9m78YIDR7mhZ-zySI7UjkXz3a_N0UnsS6TIpMV2CXfQ9t8JHSU2ECFyXGad95KzuceoFbW9SjOd_hKUq2oAnQd7ABPsMVckLpPDUnCJI0R3Ym0lkRTm6ogj2rGHyO3sTBX1OOdYuGbY_Nu-SmMrSFABC-Li93cJ9ceecqg71gVmxkacUgC6AHgmMvVLT1EmyIXY73QkjpHol-PMMpwbNh58dBLC_nm9NkySo77YQt9TEGTd0h0HeJqfIznBHia001WN1rktoWu49TIxexstxvYXbNPd9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منو در توییتر غریب رها نکنید :)
https://x.com/farahmandalipur/status/2063193568332615691?s=46</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5337" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2-CH53y7F_vB2Ipzbb-_kx-yUx90nTzaAgkj_mPOg7jpzZuVr5JNg6oI7fYN6NX797OgnnFVK51IRE2uLLXzljI5DPojkO2SGrpuQTp_Md6fXhzm-ODV519YHFmM0ygZ3qV6ZG_yXjh1CZ0w0kFk79O_XwdXBdNvrys-8vmgclYHkvLQEH8PWTlDiHxpuEoxyFbrcZmgV05zkv6RLcSXkQFkXMB4zEd93XCZdqprGSy4FXpYZdt5-VStEJLxG9KBQYPt3ahG1Hr-nmJG10TiyUX53mXct2GYmnTO2iTcGokTPAyE78nfhbgQfXr5Ff0MjuOifpzMmn3Y0mxJuF1QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f4QEcS3xjni5SEku-2iaq67tOSDaTgNo-Ih2OM8i-rVly9gCm05hn_Vr6aYB9BE2htzUZgkwYwNSg4B_m6ZSZzeDzeCiMoP-pNt55EJSqG1L4MIbw7YeTqhXkw6iSI1pQpthOm8fM2yVoWZR_R6_AuvSAbaoDfGBseT8g1taGppzjPntwFgIL4pSh7XVj-sNkKoFPEgcyO_tp6qg2f39m_RBCe4zBoGck2yINP9Q7oq4rWSHuTE3loI4q4wtcdwEfVSSrdalq2iU6N-cwihbt9zz7Yx9lQ3iGaOHzu3htNbCz6Ne3QNJueCDOT9fH_XylwIe6KwQXNe2J7PGPP562A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتهای ۴۴ ساعت تلاش در عمق صدها کیلومتری خاک ایران و تجمع برنو به دستان و  ….، کشته شدن چهار شهروند دهدشتی در جریان جستجو برای خلبان بود (که تشویق شده بودن برید جستجو کنید و…) و البته کسب غرورآفرین شورت خلبان آمریکایی!
ارزش این فوز عظیم رو عطالله مهاجرانی از همه بیشتر درک میکنه!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5335" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=EPjMA6yHVd3aKreada0HI87dnW2IrHl_zGauMhPAysYpWw6xdh_pynFAlmFBuSClG8qWaBdnh3y6BsF8Lkc5Pk491OBojbQBuWtf6_N8OApkHUtCZxqSROePP5lPPc61tq9yT-Cm09G6qhBHukGAK-36LKdz8RNw752dcRaY6yjM_e_ksoUKP442DEArjU4FWnxFNz6Ed0at3xgk7EjBMPSAOA-1QLDLzTs1sxv2bg-jar5k31iuZ98zIN-rG0hwHnyAtAeB962cMpQJrMi4wfPq5bOS83pXd6E1Y7qJecmIBd2Nx28iCtScxJQBnp_4HGGJLR1Io1zQ1tpOFjOLEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=EPjMA6yHVd3aKreada0HI87dnW2IrHl_zGauMhPAysYpWw6xdh_pynFAlmFBuSClG8qWaBdnh3y6BsF8Lkc5Pk491OBojbQBuWtf6_N8OApkHUtCZxqSROePP5lPPc61tq9yT-Cm09G6qhBHukGAK-36LKdz8RNw752dcRaY6yjM_e_ksoUKP442DEArjU4FWnxFNz6Ed0at3xgk7EjBMPSAOA-1QLDLzTs1sxv2bg-jar5k31iuZ98zIN-rG0hwHnyAtAeB962cMpQJrMi4wfPq5bOS83pXd6E1Y7qJecmIBd2Nx28iCtScxJQBnp_4HGGJLR1Io1zQ1tpOFjOLEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه خبر ، پخش مستقیم تجمع پیرمردها عشایری برنو به دست رو نشون میداد!  تشویق برای پیدا کردن خلبان!!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5332" target="_blank">📅 13:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شبکه دنا تبلیغ می‌کرد،   هر کس خلبان رو پیدا کنه،  پراید میدیم! مدال میدیم! ۵ میلیارد میدیم و…..!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5331" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/arAhadIAQ0Dw08SQsSmK2MBBrJVrLHvSWs3OJWjeG_zUsWVDv0S1KYi7xzPZ-nGDR5eq3LwEgwKIX8ur0_pc8H-WgQpxFhxoE-km9O4UNg56XM1_prxzCgXgrRYxDrRzFwKrvoX94TWLAIm0VusFnMMbSZN93EjVtiNxOAhf3HKEkdmLotc3RB6WrQjVDHjEk8VBqGVj5pA5Ef3DdY5oZJ2Vj5griM16ggvm5dPboHBQOOMDCTLKVJpJv3M2jZVIF9M8JDh0iyftsXy8nOCoEteqRE7a_a_AtniA5AzMhS4hHJYmEpZwWCE4uTaMn8DVCTNBNa8pbt-WdurJ0hPEeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PJkm75bNKZCpadq_4Qs10n_JDOMZB8qerZjVCu8vEj_pkV6f6QTvNKlHUjwf4qKiM6l6hIkVcqeK2-ev3lovlFiKoymhS11z91xg26F5j7L9CJZqc9VlLBeqQozCUcDDExC1-rCan2qrPmztE5ovk-WbuWIPwodCLEBNMj4yfFBrtmpixna3OpFdF7uA2amc4VDiHzW0MvTsmbeY7mVbywqjyzHsfmbo2-qAu2d9edm5DgFgE36zrj9tcQfmjWIzglkRfWLcKyrgE1nYuFch3b777nVvnv1E5PMCL_6o9TpkdWUrss1etV0LZY5O21bgFUNLoA_1WNZ8uU1UxWi-Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OYBGdXKtROP63cmmZTRsmpJxDLx3ZcyUpeI5vfoR2ijVrjGAHdDXZP_u-EWRB4WjwYJykEcuGKV8FQbaTyNvUhfevJOUntQtX_SjmBT8zwLmIb2AN5apZ7PSu98-HuArgOYyKpdrNtX-JtIgCerxwaCxUHza5xVRMRvVNCJBULTxGHP5IDeQA551c6c5PSWitNXNl-RTWFRosELuI-I0v85a-4Xi-HZZJi_kPKT7GwPulS6o3Lf_2f9-hrqC7hEzqH03kEt4RVsMFDDe0c-klUAHwzznBV5IuWTs3utqo5XHX6QsFFW_XcoeoXD_tZilncZpQoQXM4a0Hocbh3ODcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFrwbECOqEK5iiQEljCLRq3d3-ySvVSFfTt8GwXr5KUJvPKeYmdhw063lcd5MArweQScoNfVFR1MGJPaO1uJ0skRciTy3eibvIIeJ9pwMg-_gDOwWScesjh1nHxS4iUGaSfQLKOLhK0_Z1KwYpv-AHUBNq6zXQipcRpbjPdjhPwImdzjtkJof-kf4POACPdD1QrFOn4xJLKfYFjR7VaKdgwrzhh3X8BruzkPpzUWWOcsyf6RafTRCe46Nm5wYt7PwJFiRwv6gSxBKGc4AmFyA27Ctof6LiPRYIZ7oiYd3UsbXVYqLyNdJv941VUDcMTk1Sg76Y2brvPGQrbrNi6Bvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صدا و سیما مارش نظامی می‌زد!  مردم رو بسیج می‌کرد برید خلبان رو پیدا کنید و بهتون جایزه میدیم :)</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5327" target="_blank">📅 13:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=h0zGgzAKTYENf5U5nZ_KsRLe4Dc1okm8cEQqWnzsTLsjCSdNw0AHAlUZx1y3NDYoG1cmlj0WoTETfBkQW_UtZhMgSR35JXH9c2sd3u68yEogvEa-K1gsulkFNMvSbQGhXEAHnf5RmaaxWXftYwt0NM3EuY1kQ-B9EjaK6aIovolb3_Mzc9OHtM2DE-BtTYpy51pJNHJ_fs-Uvfp3Dym2N0of4qpgbqk51cCHY4egAZZb8JOU2N20NnBeoaEbBWNj2Cz6bxFy4fNREm4wzAsFIlmsPKj6mm9PisOvLatdXVzpuauEUeL72MDuq9uwe7XRXqENbVdVBIt9_lyU408oqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=h0zGgzAKTYENf5U5nZ_KsRLe4Dc1okm8cEQqWnzsTLsjCSdNw0AHAlUZx1y3NDYoG1cmlj0WoTETfBkQW_UtZhMgSR35JXH9c2sd3u68yEogvEa-K1gsulkFNMvSbQGhXEAHnf5RmaaxWXftYwt0NM3EuY1kQ-B9EjaK6aIovolb3_Mzc9OHtM2DE-BtTYpy51pJNHJ_fs-Uvfp3Dym2N0of4qpgbqk51cCHY4egAZZb8JOU2N20NnBeoaEbBWNj2Cz6bxFy4fNREm4wzAsFIlmsPKj6mm9PisOvLatdXVzpuauEUeL72MDuq9uwe7XRXqENbVdVBIt9_lyU408oqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی هم این مدلی دنبال خلبان بود! در انتها هم نه ارتش، نه سپاه  نه عشایر نتونستن پیداش کنن و  سهمشون همون شورت شد که عطا مهاجرانی از لندن نوشت باید این دستاورد حفظ بشه!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5326" target="_blank">📅 13:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8MMMSL_bukzilLui7ZbaQBlQg9Pp6nf0W_hClw6k_38KzgkD_6NQwDE8QAC0HN4M7NxhlHr7V_zXrqKQFMvR_cI4YHcZNnk_rL1miPn_bMZfZhmSXN0qcjerCUZa0BkBrPNFGLFwixqLhqdZOfsl0MCiItzaffaj0gQqY6CLHGUJXe0zxqOguWa1mqbnUvat-My3AG1Pf3IUTns20YxIkscDbjrVnJATZxQeVZk_KQInjC41nRRHKRYwm0vU4SX6AvHsa2sWEFJ-lkP1jE_rtjegiOMelQFaVtp7SQCmz15NgcFlZ_jbNeu-QpB34s__z35-ZhvfmHpgX6P_oskTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلی‌کوپترهای آمریکایی در جستجوی خلبانشون در عمق ۵۰۰ کیلومتری خاک ایران، با این ارتفاع پائین حرکت میکردن! در عمق صدها کیلومتری خاک ایران!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5325" target="_blank">📅 13:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=oYtM6_rNFh0Pszdpy0ReMJWgqBWS9T0f3GboEqHOLXL4BD2FN9Q6OcY9W7yIB0Bve6IDjqxfqtAxA05o-ZMk70i8OwAKIPN4WPmwa4yAR2hsH9eMJEL8jTiTyNTAyyQYzb63uFUq-zJxaydVjOtZSQV1oxajVMvW_UP3aRHuxRBe1BvOUPHKJIYDNjdwQmHOjDgDqyfURgovPC4dnn1hoGVIKSNH-2WmFBPgaJIvIlYONoEn4dl0ID-P-zXgqtJO4H-2_O8EB0JfZLf0Kz6PkPY2Wu9c8tkofMu7sHQPz1P0K9dyeDzxRdNrHZFTiPNjDRz3aZ10sETy8trHIwDoYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=oYtM6_rNFh0Pszdpy0ReMJWgqBWS9T0f3GboEqHOLXL4BD2FN9Q6OcY9W7yIB0Bve6IDjqxfqtAxA05o-ZMk70i8OwAKIPN4WPmwa4yAR2hsH9eMJEL8jTiTyNTAyyQYzb63uFUq-zJxaydVjOtZSQV1oxajVMvW_UP3aRHuxRBe1BvOUPHKJIYDNjdwQmHOjDgDqyfURgovPC4dnn1hoGVIKSNH-2WmFBPgaJIvIlYONoEn4dl0ID-P-zXgqtJO4H-2_O8EB0JfZLf0Kz6PkPY2Wu9c8tkofMu7sHQPz1P0K9dyeDzxRdNrHZFTiPNjDRz3aZ10sETy8trHIwDoYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستاورد عظیم کسب شورت خلبان آمریکایی چنان برای جمهوری اسلامی غرور انگیز شد که عطاالله مهاجرانی، که برای سالها به عنوان روشنفکر و باسواد به مردم ایران قالب شده بود،  گفته برای این فتح الفتوح عظیم  موزه جنگ راه بندازیم!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5324" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5323">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mg8w0RhBqqqt-2hzYrxgCBsPMHyD8jpC7swnwKshj0YJwtQYlNGuMDG8JiYj-BD9y8J8V0cJuzq2_amm2OWBvK2ae2afzUQmWQc1uySQBmahh-9smjw3XJSuAkV_eBAm4GQ4h6gw17j70asnPHqAG0lgHA07UBatp9hT8KuqxaTASvIZh-sDpCUCidz1U7juElYzPdBrHlvROnboFWCz9js7HaMK6v46FATOAaXlQ8bNdKtsdXenQXmtW0B6gKewmnC5z4Oy14ObJcUFXXx-18c_yvmup7l8F-q4G7vURULUPAwIJoqIIhU-QwWd5kD0qhxKAxGTplWTUwMgNqwIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی  در عمق ۵۰۰ کیلومتری خاک ایران افتاد،  جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!  در نهایت سهم جمهوری اسلامی  «شورت» یک سرباز آمریکایی شد!  که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5323" target="_blank">📅 13:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5322">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIYfR2ghgfHFML9NsroMjh7GeT46YL4_1QDbemtFHqS0dmTpwkZ4-6aJdup6N-HUVeXKyxmuHMAZT7Vi5lDgvXVvUqd2eEz6MEJSlrsK3wBQS1Qw8z3IlmuMLptJsoxHlUDXnV2CPtW8uZMl-WNUc-6G1LE3PwQuVLmUoPL96cQ5CAZMylTBu0e_ca0K75CV-nv3DlYYcNYhOFBF5443WkxguP-mBAFLT7pYW1pHma1uzjX90dT4f_D1P7FxwkKXqjzpOH3u3sQLExgk6tUeh3mkj1lWQTCwpdnSSCL0BrEnaMKHxa1-FVLJU3VTOP1lX7bBG1GxpIOnb082oYTXYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی
در عمق ۵۰۰ کیلومتری خاک ایران افتاد،
جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!
در نهایت سهم جمهوری اسلامی
«شورت» یک سرباز آمریکایی شد!
که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5322" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5321">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=YZMZ0xXFzWPTU0bnov1AR0_OgF7ht_5jWPOK9CWHntN6jfANn5OSaY8geIttoLD13d6QDHjqzqA_7j_-0cqhIuTLUn8OI6XxSItWEdHSSOz5UYlKh1ShHr8-hhShvv2nDNIDg80vU-mGhTwIAvLf7PpUnBnDCN4GeYELcmNNNGtfmofhmT7VhxGS25JgeYdlf2HU2rdT-tSTK5js9gkTTEXVmDK2AGWuRAuZcc5Ra9IJ5XLrQR5cqnvSrOIpfEK36-0xpxSGhU0Oi19Y0HDooVjrPvA0nekQJy-D5Uq_rClyl6m7r1XaC-A6tJC49NK4N0N1sJxl49nZiK7k6qzd-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=YZMZ0xXFzWPTU0bnov1AR0_OgF7ht_5jWPOK9CWHntN6jfANn5OSaY8geIttoLD13d6QDHjqzqA_7j_-0cqhIuTLUn8OI6XxSItWEdHSSOz5UYlKh1ShHr8-hhShvv2nDNIDg80vU-mGhTwIAvLf7PpUnBnDCN4GeYELcmNNNGtfmofhmT7VhxGS25JgeYdlf2HU2rdT-tSTK5js9gkTTEXVmDK2AGWuRAuZcc5Ra9IJ5XLrQR5cqnvSrOIpfEK36-0xpxSGhU0Oi19Y0HDooVjrPvA0nekQJy-D5Uq_rClyl6m7r1XaC-A6tJC49NK4N0N1sJxl49nZiK7k6qzd-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قاسمیان : سربسته بهتون بگم
امورات دست مجتبی خامنه‌ای نیست.
قاسمیان نمیخواد بهشون بگه
«چیزی به اسم مجتبی خامنه‌ای اساسا وجود نداره!»  میگه : امور دستش نیست!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5321" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5320">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWj7mxC5WFo-Ed7FAcYChg2Q3Gj8ApX5gH6d98FiiBVRH-BiNmwy_SnXMgU80wIgfOYBgFp6vRB21nR2cGbgeKblpSuJAtdFIZNVYtAB45TnWnaDf0ufGvBEvZR_0qwFFdKprT8a9eDEW3-5gAu57O0jgiD8bfZbO2D30qvimQ1tOYAkCExAF5BLiyEP9wstLJ4Y9BYIiZmpCOiULopaFzKv6LOzOMcFZfg7ZqZUAykdov7BF9NboABF2MSFumKoa-Om7JtPW1PysTY2JLlM40qQARF1CPqEPqS4oM0YiEkggD319nw3hAsebXpcUpIf15517nTSNkluxfsFaywalg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5320" target="_blank">📅 12:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5319">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=lQKJLRwj7rbr3vD7_hMI5zuXjyD9fTwKlHgDfapffLlwGeag-FUcBrtfa3ZXIh4EMC3Ma-q1B-8xQprTqUsT0d5acuhc2XTxfP2o-hGx0nEIhuZq4nkKIaox4HmmWhKvWXwgKMrU-eUVjIiQFndTZKLL-bE2j3LZ6w_DHiYjggYHiOpjW5JwS9GDFxTCZEDz2yfNrWYi1nT6j9ES5xNu5r4yQhYMjPxPckm-JoQkPG3TtLB5JhSOXpY_AeC5Z6EDtmaAPhKhAmkcbBO2ZXadRd6gnTPcqlys5NRzRZ6NI51MGKyQoGgjriHMzTs3_39bjif01iljAiziJSz2JD5jSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=lQKJLRwj7rbr3vD7_hMI5zuXjyD9fTwKlHgDfapffLlwGeag-FUcBrtfa3ZXIh4EMC3Ma-q1B-8xQprTqUsT0d5acuhc2XTxfP2o-hGx0nEIhuZq4nkKIaox4HmmWhKvWXwgKMrU-eUVjIiQFndTZKLL-bE2j3LZ6w_DHiYjggYHiOpjW5JwS9GDFxTCZEDz2yfNrWYi1nT6j9ES5xNu5r4yQhYMjPxPckm-JoQkPG3TtLB5JhSOXpY_AeC5Z6EDtmaAPhKhAmkcbBO2ZXadRd6gnTPcqlys5NRzRZ6NI51MGKyQoGgjriHMzTs3_39bjif01iljAiziJSz2JD5jSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاریخ مصرفشون تموم شد</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5319" target="_blank">📅 10:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5318">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6l3vPUIJ-QJuaYYfzKkv2duoDNlKa6Znh85kPYVXQ30I3qksr4JjX3k5jyh37IYyQfYr7CJ2qUTMqlQxY5nsjOW8WovScwwrCLPNNo3-afm2deNjn_T5Cfsa5ygkMn20SzEs6OK4rhiBbTJ2m_nuX9z3DvlazAltB0IB-k-ub7eOXfVD0KNdOmk7H90wuqy-FsM-JERaqhtPmxvnC8ynVYznd4ghQ6noY88k3bEKKBwjayACeeNreaRFKyJQUaaZC7kp0INBnq1kOssfDnAcgg21VzQRP6ZCQzWl1cMQqn--HkcPQ9FRY0WxAUVxfKe3B757BLczCfDK58yYQSQnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5318" target="_blank">📅 09:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات رسمی آمریکایی :
جمهوری اسلامی به سمت تنگه هرمز چند پهپاد شلیک کرد.
ارتش آمریکا حداقل ۴ فروند از پهپادها را ساقط کرد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5317" target="_blank">📅 02:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5316">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5316" target="_blank">📅 01:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5315">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8Yx6S3KV7udRIHpeRYGK0AzAm5IdtAiF0ITm97T1lk6YfAhp57F3klEtjHcyPw1uKb4An9c6n1GerS1rNcEBS73c6-69HP7RRv4_QxeF-AR4LnAWq_Ud5bzLPar4iV5qiv6uocqRIC7FoM4RrlpGO3adhXIp6Zk2F9WEXRBMkBIALJsEomXmH1S_4eJT3f8_qeLP8nQAjlcV8mOhT9wEg85OG9ewraBQBjIegkw0xm8NIeY_sXbzm2I8bQdF7s1gjBeDkvMoqo0Fj8cGrbg_5eyjBxN7m_SM2oUNufXI9Y4e2ih-mxg49I8hFdBxaqQAhFIDlC64nBM0K2Pw2a98A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5315" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5314">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5314" target="_blank">📅 00:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5313">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRAZbGmZIilb28P368SXpJ9oL8fMSgT1J_dPAby1YmjR1REd8W0-C6znzRVrmu4a-CRFE49yq4jjhtDPstHoxz1qjUYx681YiG5CzuToY49Z4jqgwwv2STbkJt87-eeCR0NX4wnOnZnogp0n-rX8zYx8RbW0Rw14TT49yzrOdVll_fkhZREpCjtTw-tnZHMbatAy2kdW23XigRfUILdY6gU-C_IyC0krqJKLUDN1gJ9-reRMKQ749pA7ETntVU1AzwGbvd-gUjk5B_wipOZHI_yg21Wzy5huA5FT3mlAWr8hpAaALG6pRi_iUyGqKG_lWoA8La8h8Qzoo0XSBJLq3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقاد شدید نخست وزیر لبنان از سپاه
و جمهوری اسلامی
نواف سلام با اشاره به توافق به دست آمده میان اسرائیل و لبنان، برای آتش‌بس گفت: «ما موفق شدیم در لبنان
به توافق آتش‌بس برسیم.
با این حال،
مردم لبنان دیروز با کمال تعجب دیدند که سپاه اولین طرفی بود که قبل از هر کس دیگری آن را رد کرد!
این کار تأیید دیگری است که این جنگ، جنگ ما نیست،
بلکه در سرزمین ما
و به هزینه مردم ما انجام می‌شود.»</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5313" target="_blank">📅 23:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5312">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=CrfjGkFbxLE_nzhaz71EdnpnfLk2WZGx4k7IYnIe4m2fwhvgVAwBYayIdUpL0oB5nQzDRWuzRdlx2ulkb61tLOtnpNScQz2oqg6SAMK5aLVRN6toGrxYgJ_gZ32afaPykqVlERN8jPa9Ii8hJXaj57DjWlNmWmcqrPzcP9VtxR_LemhAtHjuSLaUOC9kafP4qv9kpnQfmbZsVYJdtPWVuSObkNLjOsmkPAnGHKiA9Dvv7_6f5pdTazIgtkIs3pPLh7Nqmcdhj-Pt35kq7xZIhpqq5Hnu4LlBhQyDt5lB42UwROly27YIDHkS7g8sw1xQw_2Maq1vlNSQOxToUXjzBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=CrfjGkFbxLE_nzhaz71EdnpnfLk2WZGx4k7IYnIe4m2fwhvgVAwBYayIdUpL0oB5nQzDRWuzRdlx2ulkb61tLOtnpNScQz2oqg6SAMK5aLVRN6toGrxYgJ_gZ32afaPykqVlERN8jPa9Ii8hJXaj57DjWlNmWmcqrPzcP9VtxR_LemhAtHjuSLaUOC9kafP4qv9kpnQfmbZsVYJdtPWVuSObkNLjOsmkPAnGHKiA9Dvv7_6f5pdTazIgtkIs3pPLh7Nqmcdhj-Pt35kq7xZIhpqq5Hnu4LlBhQyDt5lB42UwROly27YIDHkS7g8sw1xQw_2Maq1vlNSQOxToUXjzBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون [شاخه افغانستانی‌های سپاه] : هر کس گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5312" target="_blank">📅 23:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5311">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=aKI_rK7s-3SB4mdOVx8fNsxWRPpC42JhaVw-iXC_DhVQnNyowf8EuCQfeOxx9ZxOtH0yDgBVfjzyOd5xcF2w6rCf6WWtEnrE-mIHQoS4voWKc8DQMjngPOeDZy8SVT66pp6LoQSu3sJgwpPR31Men3G0an2hboWdeAmlFZaA42hEoVGiMoUf2jlCmrw7sgEw2TWQ59UNKNG9aW0ENFP0dy7d0GFEIh7fLXmqGxGHx_FKNghG6G8VoL1Bk6dagXHBTSQkcC_ILP4QsZSoLZ-lfz-zkrOU9vUL0BYH4qA_M4UgcbvBmS-9R-G8wnPETeAsq-i-z8vqqYL-bdoQ9b76eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=aKI_rK7s-3SB4mdOVx8fNsxWRPpC42JhaVw-iXC_DhVQnNyowf8EuCQfeOxx9ZxOtH0yDgBVfjzyOd5xcF2w6rCf6WWtEnrE-mIHQoS4voWKc8DQMjngPOeDZy8SVT66pp6LoQSu3sJgwpPR31Men3G0an2hboWdeAmlFZaA42hEoVGiMoUf2jlCmrw7sgEw2TWQ59UNKNG9aW0ENFP0dy7d0GFEIh7fLXmqGxGHx_FKNghG6G8VoL1Bk6dagXHBTSQkcC_ILP4QsZSoLZ-lfz-zkrOU9vUL0BYH4qA_M4UgcbvBmS-9R-G8wnPETeAsq-i-z8vqqYL-bdoQ9b76eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله رو دارن نابود میکنن و جمهوری اسلامی برای حمایت کاری نمیکنه.
«عدم ترستون رو نشون بدید»</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5311" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=PaWkxKgpxqSPN5h1LX8UEfJvh8QpuLtzT4wndBE3W3DWAMWPJT1pADtAksLlhi50mmt2cOawAnZ5q7-fIPPALgp1dZS3R7_E7PghP0ViPrwzCM8lnS_KbYxuv4bG4YBKUsAJ7ZWqAAsNL5Qy4GOOLDRvlGxYm8P_MJoEcFfnRN8jizXf22lKYc1KltvtvG5hM6DohThgd15HXS6zt67PGav-FlSzuAnEKrjNRTuSl9TfbkureQS7zmgmY8T89SREER812mqjPIBuiZZoFaNqFImRuTfrdjqCBQ0wB7_JunYx_2JW4RVq-wJXJB0xUmNov8Q7z7rFT9EKWRNSegHGWm2E4f3SWvOYgcziARdaAwSZQ0NSA6zGAsQMecx2rnciiAfvECeKoEpD6WwGMp7VMZ9Vay95DHghjm2h7ecoYUC0Zp66ob47qvbN7gc5AAKvkpbn2IH_I01LIlFAacMIIIRDhw4Dk4CQnMHcDEHrwNyr-Jt75nQsJwnuRCBBgvKnrUjqhT_klSLr3WhblkJajCJkzgfZ1kemyXA2yo6msnXz7ISqVpjGjkYhXfG7nQZmu8tLvWQ-bQjJps275gy_CxnDhVMK9fuDAuMtbZ-RyoSAQHxlEeaPGGdNXl2o4xcNkiGk0SFy7x2ISqPu2mEQqmPziWd5PayoGex-6NUDqEE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=PaWkxKgpxqSPN5h1LX8UEfJvh8QpuLtzT4wndBE3W3DWAMWPJT1pADtAksLlhi50mmt2cOawAnZ5q7-fIPPALgp1dZS3R7_E7PghP0ViPrwzCM8lnS_KbYxuv4bG4YBKUsAJ7ZWqAAsNL5Qy4GOOLDRvlGxYm8P_MJoEcFfnRN8jizXf22lKYc1KltvtvG5hM6DohThgd15HXS6zt67PGav-FlSzuAnEKrjNRTuSl9TfbkureQS7zmgmY8T89SREER812mqjPIBuiZZoFaNqFImRuTfrdjqCBQ0wB7_JunYx_2JW4RVq-wJXJB0xUmNov8Q7z7rFT9EKWRNSegHGWm2E4f3SWvOYgcziARdaAwSZQ0NSA6zGAsQMecx2rnciiAfvECeKoEpD6WwGMp7VMZ9Vay95DHghjm2h7ecoYUC0Zp66ob47qvbN7gc5AAKvkpbn2IH_I01LIlFAacMIIIRDhw4Dk4CQnMHcDEHrwNyr-Jt75nQsJwnuRCBBgvKnrUjqhT_klSLr3WhblkJajCJkzgfZ1kemyXA2yo6msnXz7ISqVpjGjkYhXfG7nQZmu8tLvWQ-bQjJps275gy_CxnDhVMK9fuDAuMtbZ-RyoSAQHxlEeaPGGdNXl2o4xcNkiGk0SFy7x2ISqPu2mEQqmPziWd5PayoGex-6NUDqEE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏محسن رضایی امروز به CNN:
‏اگر ترامپ مذاکرات را جدی بگیرد غرامت ۲۴ میلیارد دلار برای آمریکا رقم بزرگی نیست. اگر او واقعاً بخواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتماد است اعتمادی که ایران می‌خواهد نسبت به ترامپ داشته باشد.
‏این آزمونی است که آمریکا باید از آن عبور کند؛ در آن صورت مسیر توافق باز خواهد شد. این پول، پولِ ماست، نه پولِ آمریکا!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5310" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVAWmx5_4flRxpXnlxtLT_rwHxnD962TCt05F4NnsI6Yf3kP4i5wt2YB02aklJ_Oz-DEo5-4UugSv24v1D8gYKAaRn4b0-zt0OfQDdLhWd7ot8VpU5oXlzzKSM5PDfxJKBrXo8rOqvximq0ivhmAehU1reQujQyJBFLOe9sIw8v2gY78p8Z0n7FX2Y_Ll8IYp2OlvBTlt_mlVoWprvrfVdGaQ5WemWjHRVn676rLvEm8r9NULVvTX67bD9w-9_aCXHmWwvbNlnJAHORKerbArZXYA_2s-ZeLVMKygRKBxX1Q6mEv9YLzC3lnAtcyFaianB9uCOGAGYgtvqN299l47A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلیسای انجیلی مشهد
که سال ۱۳۸۴ به عنوان یک اثر ملی
به ثبت رسیده بود، سحرگاه امروز
توسط بولدوزرهای جمهوری اسلامی نابود شد.
مسیحیان انجیلی، اولین بیمارستان در مشهد رو هم احداث کرده بودند.
کلیسای آشوری تبریز هم چند سال پیش ابتدا مصادره و تعطیل شد.
کلیسای جماعت ربانی مرکز تهران هم
توسط وزارت اطلاعات تعطیل شد.
کلیسای کرج و املاک اون نیز مصادره شد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5309" target="_blank">📅 18:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-Zl3sSA8TZlXEcnBE58DwsWTnBlKMEOFhEVj4J--lUNJWeiGvmDHHn2IP7u7A3kylDiAjU6fX4QSz2CkPySRUNgyLinI0kG_iArjxRvOuNWbi1Y5DqzmkeSLs-I1s1LLHNaxnGFPJDG5B-Q-WCHJaT66F4BEZq8QlarE7wn26s0986bgGwsxFAr5vPsPVj_JJPMwXxHp1922BKnM6yZRPSoCwrn4Iecc74SXVjO30TyHJYOqPreyaD-OATZlUVE0ywFiJcCXVpwjPmX6eA37QJLkBm0Q_hqyOXywmMrJfvCuQYcB9UYGvK6ajEwejGNc1OGp1_IKRaTqL9O68O52BIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-Zl3sSA8TZlXEcnBE58DwsWTnBlKMEOFhEVj4J--lUNJWeiGvmDHHn2IP7u7A3kylDiAjU6fX4QSz2CkPySRUNgyLinI0kG_iArjxRvOuNWbi1Y5DqzmkeSLs-I1s1LLHNaxnGFPJDG5B-Q-WCHJaT66F4BEZq8QlarE7wn26s0986bgGwsxFAr5vPsPVj_JJPMwXxHp1922BKnM6yZRPSoCwrn4Iecc74SXVjO30TyHJYOqPreyaD-OATZlUVE0ywFiJcCXVpwjPmX6eA37QJLkBm0Q_hqyOXywmMrJfvCuQYcB9UYGvK6ajEwejGNc1OGp1_IKRaTqL9O68O52BIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور لبنان : این کشور ما است!
کشور شما (جمهوری اسلامی) نیست!
به شما ربطی نداره که دخالت می‌کنید!
این خونه‌های کشور ماست که داره ویران میشه!
[ ج‌ا ] کشور ما رو به گروگان گرفته برای
مذاکره و چانه زنی  با آمریکا!
این غیر قابل قبوله! حزب‌الله هم باید بفهمه که هیچ راهی جز گفتگو و مذاکره و دیپلماسی نیست.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5308" target="_blank">📅 17:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5307">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رئیس جمهور لبنان خطاب به جمهوری اسلامی :
شما در تلاش نیستید که به ما کمک کنی،
مردم لبنان دارند هزینه‌ سیاست‌ و منافع جمهوری اسلامی را پرداخت می‌کنند، منافع ما مردم لبنان با منافع شما (ج‌ا) یکی نیست.
رئیس جمهور لبنان خطاب به سپاه پاسداران: این کشور شما نیست؛ این کشور ماست.
سپاه پاسداران از لبنان به‌عنوان یک برگ چانه‌زنی در مذاکرات خود با آمریکا استفاده می‌کند. این قابل قبول نیست.
مذاکرات با اسرائیلی‌ها سخت بود، تا زمانی که به یک پیشرفت بزرگ  (آتش‌بس) رسیدیم.
این توافق می‌تواند راهی رو به جلو برای رسیدن به یک «صلح عادلانه و پایدار» باشد.
یادآوری : دیروز حزب‌الله لبنان توافق آتش‌بس میان دولت لبنان و اسرائیل را  رد کرد.
جمهوری اسلامی عملا لبنان رو به گروگان گرفته.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5307" target="_blank">📅 17:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RitPMlo6FoEFumDwKdWrdvzIuxuhn9WRLOG_6V6Bmgtb4qRsxaZArL-BOVlThyFe0Kb7zSVEKlpB4fVNtVo8GzkLGByx-Xl2UBl4EPWAR2nfmOWB8nIJn5pU_w_uTUlTJZ1RAYkI36sanIv_GO55d1BYJinyOZm_ilhAEpXrdVx-aW9Bq02t1RRQs5uKXSUo5iibTBZZ7680FOqispll-jyUILQn744x-ldCczM7GxTvewU9nQWzA8QCOaAS0bKA73lhTBWWrS58yBc12eQbhEYP0YafAHwaiIvPqcWMoCFwFao6Ts-MezN6Gw97kYB5l24zwzKIQiGsBseWXGxCMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله لبنان دیروز توافق دولت لبنان و اسرائیل برای آتش‌بس رو رد کرد.
اسرائیل امروز دستور تخلیه ۹ شهرک و روستا در جنوب لبنان را صادر کرد و ساکنان آن در حال فرار هستند.
چرا اسرائیل با سایر مناطق لبنان کاری نداره؟ چرا با سنی‌ها و مسیحی‌ها کاری نداره؟
چون این گروه تروریستی فرقه‌ای‌ پول و سلاح از جمهوری اسلامی میگیره برای جنگ‌های بی‌پایان با اسرائیل.
عملا برای حزب‌الله و حامیانش، این یک نوع شغل و زندگی و هویت شده! تبدیل شده به هویت و شغل روزمزه‌شون!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5306" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">امروز، چهارم ژوئن، سالروز آزادی شهر رم
در سال ۱۹۴۴
۳۳۰ روز پس از ورود نیروهای آمریکایی
به خاک ایتالیا، رم آزاد شد.
موسولینی در یک سخنرانی رادیویی از مردم رم خواست علیه سربازان آمریکایی قیام کنند؛ اما مردم رم از آنان استقبال کردند و آن‌ها را «آزادکنندگان» خود می‌دانستند.
رم در عرض یک روز آزاد شد.
شهرهای شمالی ایتالیا، از جمله میلان، تورین و جنوا، چند ماه بعد آزاد شدند؛ اما در بسیاری از این شهرها، آزادی پیش از ورود کامل نیروهای متفقین و به‌دست پارتیزان‌ها و مردم ایتالیا رقم خورد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5305" target="_blank">📅 13:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">« سد طالقان را یک شرکت چینی صفر تا صد ساخت، بعد به دروغ
به مردم گفتن که به دست مهندسان ایرانی ساخته شده .»</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5304" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpnCVr0O9hxYLqIIF-fwA7EpNSgIPed0QMAVYjLrKz6aGIDPms2GTEv0LMia-W-O6s2kwIiee5a4ruV932_o36rBi9MU6RkFflKrafHG3T-qP5joqaXHCvqrhwYeOzpXDw6Ao0pXG7IpYLFj3ykYly_-P7J-_VsmCLou13p1Z9kVJgZpeEW0IaW9AB2lDQNSNd3oqiPGJUmp7_NJhj3isUxQo9owS0abetFPsYms9CeGQfwvG0sA3u336LkXNxTFha7ZEPfgWXDZSEml-8sZ52qndBah5xcJBOC2HPZHFHbYUDbeMC713ktbO0virRGUNG2sc4GaTlTJ7wjvVoXbTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HU9pdIBBgobVQoNjcJ_zzffXM_9ozBQAQqsJiIIe4Ow7SYVVRwvWM17ITNdM4Lb2XfRPutaGSQ8gXeMHpH2VUuZ7InL6-6LTaB1AXRzbUo4313wMBxhy-0Rm07jgYwoGcWJNFnZNdgtwF0liI6X7rRbakZHNwkBUHOkNzcnmuzVTxQZW4aXF7-1wNWLbF1Gqi72aP3UyvhD68oC1l2iXW_xyuy4mrO73IfdLZ5ODBMQJz-qjv3kprGiZQ6Zrr093l831tW1VpjxwvxXPikAQuov6xLMdPQRHNIvwYlrfd6ZYj3bUr_-5vlphp1uYE-H3wkunwBhBZzqhjxoFPwcThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به این بخش از نوشته نادر سلطان پور که نوشته بود : «فقط ایرانی می‌خواهند آن‌قدر ضعیف که هیچ‌گاه تهدیدی برای اسراییل نباشد.»
پاکستان یک قدرت اتمیه! ترکیه ارتش بسیار قدرتمندی داره، مصر هم همینطور،
چرا دنبال تضعیف اونها نیستن؟؟
زمان شاه هم ارتش ایران بسیار قدرتمند بود
ولی مشکلی با قدرت  ایران نداشتن!
بهترین سلاح‌ها رو هم بهش میدادن!
پس موضوع «ایران» نیست! رژیم حاکم بر ایرانه!
چرا با جمهوری اسلامی مشکل دارن؟
چون اونها سیاست شون رو جنگ و نابودی اسرائیل نگذاشتن! افتخار نمی‌کنن
که به گروه‌های تروریستی سلاح و پول میدن!
این چه ناراحتیه که ما میخوایم تهدید باشیم برای اسرائیل و اسرائیل و حامیانش مخالف این هستن؟
بیان کمکتون هم کنن؟؟</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9EmkQbTovP02C2H56HdAaCHR4BNpc_qZOee2sdMuN-D55Fj0W33FyOpThR3H9JbEhQlK_folOuQ84KXiaSsMZAM5YIYU85CdtHJizz6al8JAt8VNyDAOW60cfqpW3ieA-mIKmNvH1uUi_g27SNVP7eULr6FF1b0b00wObmu4HPsb69Zb2DiiXVo3kJ_SPBPxN_G21vt2A8BljovEq3a7VOhxPCNES9bEKmxnceOOBrtRNv3YuBy59AxAYiF9HgosGxcqs7Ez29iXWdJ5Ny35YA-WIsp2qsXeU_qn4nHySbhy6GdfyDGVMCN3yr2I1h_OyBZNj6Ttv6NnihYICWQLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a63V1i0Pju2yDXGGPtexRmrwl7iAebaGMMhTizFsGN_sCogH3Pc38fkKHjz0PeXM9aYS1HNYSxO6LHnyMWShZOw23UMtV9uxpC7LUzr_3CizEUFttoGh3rBdtLzqgMNhHuB6Eh-1Wi2Z8Q7Kwv6CK2Tq5piKbN0MlOe2mQFclpB6jR_tB0T44sviZiyFAAudQGd7OW3EKR8Ac0mSNFxKU1wayihBCpnibsggPQmaJ3HyEYca3iQ0wnGo0hE_Y3HUaUnnz_H-AztYiFLJpQR6Sv7X9L2Tnj8BYzhcuOoN6O7Xk8B2jSlDAfSb3vTBhLgSlpffCiYwnSJtk_hAlIbZCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7yYnvBcqgdp9YDB18FFnUzCEEhZKZ63DB1hBzzhr5huqUax20s_wq5Wv4oSOcxBoL9H4RjgP3xuJKRY7uIQFMlaFJjxHL_TnF3A8BhLBcmPRYru4nHHxdPJHxmojatu0Sq72fe92iaXlGwN-mqIXB8vIOeuI_W6ZEvN7WVrVt4rIRWXGZjFguZy26ak5RWIm04PtIlIOemXJlmcR2kSrKlzz93UrTXt-D4SA9FTnBoOATpn9SWZU8YznbpO1OuwpPl6Hxp4qnph0BqxRNEMuoLuulKaxWge8LTVpQ__Rl8Rpl0se3kUL_OQ-EgHthnv-g_5CzNM3NS2Lc4HstZEAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=drGVJpUTZUF_f_R4yCbVNHug8lRNe9lYILZx0ucsM15QYMmeaW2WdS8WFjksL3dY9l7aT21zvzUppWwAWOq6KhUb1c89hWURURQB1M6Oo9kSbbK5p16ISdaULC4Cb4vARUUk8i1mZ7BYBP3wj3ELTlpI7-THQC3v8RIEB2tTgIJ4U3jerlqc_ThsIsmTj15nFwv3GlU5Blwr14LShcCQopA9K_gsz3mt6TIDWodER46ipwmuo62QUQC4DTVSP6B8SXLzL6w59wyqnK1CFaNRZvlRDo62eqDhdNJgraeGAbqlfXPx6WNMn3ltcHAlepYp7Rxcwfe7nGViuo1i3Ne8KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=drGVJpUTZUF_f_R4yCbVNHug8lRNe9lYILZx0ucsM15QYMmeaW2WdS8WFjksL3dY9l7aT21zvzUppWwAWOq6KhUb1c89hWURURQB1M6Oo9kSbbK5p16ISdaULC4Cb4vARUUk8i1mZ7BYBP3wj3ELTlpI7-THQC3v8RIEB2tTgIJ4U3jerlqc_ThsIsmTj15nFwv3GlU5Blwr14LShcCQopA9K_gsz3mt6TIDWodER46ipwmuo62QUQC4DTVSP6B8SXLzL6w59wyqnK1CFaNRZvlRDo62eqDhdNJgraeGAbqlfXPx6WNMn3ltcHAlepYp7Rxcwfe7nGViuo1i3Ne8KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«وطن کجاست؟  عقلا منطقا نجف»!
وطن‌ پرست‌هایی که وطن‌شون لبنان و غزه و عراقه
و میگن برای غزه و لبنان حاضرن ایران بمباران بشه!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRk_Xmc-VJfN7BsbHVEghr1Kxm_LVHfqcfZNUAw8_I1gP8KMLjS27Ps_10xUKA8lkY3VdFFBcYX-127MNpH60lcr5R-50XjFKTSgWmVS5VoICESaAu9R26IrtmMeWkICAdgOpbjFT0YU_bdkcygSrBCLg0n4s8ng6dRufAd8MFBD6d_vF5eBd92WFy-g-Dyzkpmq799kg1hqOjRccLedrHipawMvh1OEZMnwmoXPmxIRPY9uwJLkZTalfPU-8bdU3aKy6fYtzbmeg__5VRm367IL2Ghf1vicBxudR4WpD2zx7ktLgq4nHWjchh8Sr_O8Gu4_lH3FKr3g__E13jOa4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3O19VIJraJMUPCe2tSM7DVMHN92F1atK_0rdMgO2AyX5-4qGMPNkEmcSzP_rmpdRZ1LNZ9mUvZ-CqbtnSgrD1yJCsLTINP2DoLS0i2BRT2q-iPAJB17G2QhQTiIulvXzeiXI29aJaWbDWC9OFm6yY4RLYbnBY5NWlr9NnHE51Ns04yO9Xm7RI1140r8_CEklxcsbd0WvDeVyklY94wnY8kTiCnNbdCQYEKdf2xbYMoELo-1g4Y00X5t9ZlCvgoiui3EaqcfC_wL9IzXBIZUFzIxxfBoft6nh1Br52Vv6QFJsKDISOIiGvNcs9ktMAYLHIsyEZ2mEV47WomI2luvLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YVN0KdYWZJsitaPll5jf0f8ry1WCtU2ojClVIyAOdGteA-WHiOw9vaoC1OABmiV3OGUUbaBTDUw6Z_XOgZ5e7DIzp41m-70isbvRQdjTNmZjUs7jI_GMulJjDcI79HWz1Fm8_6WwagB3OCOKpj52qq-yvcGc1BlNfe9hn_CWX17AHeadSei7L8pJPn_gPr0nKVccEr2pSekvLaN-AF-m_bWq09MQwaL_h_HIy4AI-pQatB3jQUsrmRHBvqm9VYPY4uTZ7zc9qapW71A4Xlp7nbGP4I2cB4oAnAg1e_tXy7MLumpvX-iHj377HQo8iqcASHyBGVzNOOgkm8KBqdHVvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=nffPnPbmF-Ftc5Ecz0I6RWu8DJpUNx_HIpQ1V-7kqeHgAmZlmTMXZ4Fib8xtqte25leuBxoeGYOUchokioMWveDJPJFcQTvfeCV4POlkf9ioQGduq_dqotEs5iG9KiaHsCoku8K9EOxu7xRAImVXz2yrWudELE2uQcIR1Fnkg2pxvqVc-nuMmZbBeBHL8sgeYDBSVMUps6Gv0FfNu-_GDmSxuL7p5VnDqpcbtL8u83HvPdUVbBWL4xcVk4r3XrGSOcDIvvJnkEr7EJhB9-53RAWGcSHEbg9bypvDUeu2a6I82sr-ozrZcAThEVYRYCEXaOa6uyT7iejIGb6qbFT5YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=nffPnPbmF-Ftc5Ecz0I6RWu8DJpUNx_HIpQ1V-7kqeHgAmZlmTMXZ4Fib8xtqte25leuBxoeGYOUchokioMWveDJPJFcQTvfeCV4POlkf9ioQGduq_dqotEs5iG9KiaHsCoku8K9EOxu7xRAImVXz2yrWudELE2uQcIR1Fnkg2pxvqVc-nuMmZbBeBHL8sgeYDBSVMUps6Gv0FfNu-_GDmSxuL7p5VnDqpcbtL8u83HvPdUVbBWL4xcVk4r3XrGSOcDIvvJnkEr7EJhB9-53RAWGcSHEbg9bypvDUeu2a6I82sr-ozrZcAThEVYRYCEXaOa6uyT7iejIGb6qbFT5YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=bsIdDLVciO9rjoo1bPSml_htFrLU59r4AMn63wPY9pie3XnrjXBOame5xmzr4QmM_PC0qnYka3a7y8b_HJx0-XvV_csQMtLNEKBaA-578yGyxTvPAOcfReF43-YxwWY1N11J0UmiB5Mz9A9cnogEh5Sw_SQnQyybGUpfPV9E9VPV59qvgNi5k2m7wnlFB3YWFTiR-IZdaDu7qGGgqU-YQ2lRm8CDvT2lFzzrmEacmWy8TrAt3CXR5-36_XLVMLXdJS2YsaUwrGqxgaA2QJwkrVzckMwTaRHiEuDIgEK_hFG1bxUQvra2CuISvASTbEqk8YEBTVD1k4ENlnGbB5-r1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=bsIdDLVciO9rjoo1bPSml_htFrLU59r4AMn63wPY9pie3XnrjXBOame5xmzr4QmM_PC0qnYka3a7y8b_HJx0-XvV_csQMtLNEKBaA-578yGyxTvPAOcfReF43-YxwWY1N11J0UmiB5Mz9A9cnogEh5Sw_SQnQyybGUpfPV9E9VPV59qvgNi5k2m7wnlFB3YWFTiR-IZdaDu7qGGgqU-YQ2lRm8CDvT2lFzzrmEacmWy8TrAt3CXR5-36_XLVMLXdJS2YsaUwrGqxgaA2QJwkrVzckMwTaRHiEuDIgEK_hFG1bxUQvra2CuISvASTbEqk8YEBTVD1k4ENlnGbB5-r1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxGD4fa0LfxzGfWe-VFKMYR9k2EZyQDHp34OwdSbwIpQy2JQFQ2iG43ShV_byOBnF2W2ZW1epp1ODI_daff5sdTmX_sfIY11tWKB6U9c6mYwiz19eYLVYOreKUaAACDyvtBNHzVeqf0DvDZhJZ44x6sME9HlW142a_FArVGKsiCu-1j5xakzrd-cd0Mietv3n5cE3VaFvmJWpw2V5wwoyESmA5ayWIIMLOfU8GjfZKC46bFjE0O3lVciI2WUIvnUe1Ukcy_hQ6zEVSOWvBFtgYHlA1iEI3pbxTW89XWph1SUwiYAhCS6IwmwWz57OACAfbZd0aIW-WuzOdtx_2E3yv-M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxGD4fa0LfxzGfWe-VFKMYR9k2EZyQDHp34OwdSbwIpQy2JQFQ2iG43ShV_byOBnF2W2ZW1epp1ODI_daff5sdTmX_sfIY11tWKB6U9c6mYwiz19eYLVYOreKUaAACDyvtBNHzVeqf0DvDZhJZ44x6sME9HlW142a_FArVGKsiCu-1j5xakzrd-cd0Mietv3n5cE3VaFvmJWpw2V5wwoyESmA5ayWIIMLOfU8GjfZKC46bFjE0O3lVciI2WUIvnUe1Ukcy_hQ6zEVSOWvBFtgYHlA1iEI3pbxTW89XWph1SUwiYAhCS6IwmwWz57OACAfbZd0aIW-WuzOdtx_2E3yv-M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسام الدین آشنا، که قبلا معاون ویژه وزارت اطلاعات بوده، طوری وضعیت رو ترسیم میکنه انگار ترکیه فقط یک فرودگاه خوب در استانبول زده،
بقیه کشور رو رها کرده! اما جمهوری اسلامی
در همه کشور فرودگاه زده!!!
ایران ۹ فرودگاه بین‌المللی داره!
ترکیه ۳۷ تا! چرت و پرت!
یه جوری میگه ما همه جا ریل و قطار داریم
خب پس بیا بگو چرا مردم قم، اصفهان، شیراز  و…..
برای سفر به تهران باید یا اتوبوس بگیرن
یا خودرو؟ چند درصد با قطار میرن؟
۵ درصد مسافران با قطار میرن؟؟</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rY7_9ySrTaa3M-RV8wDKObCZZGbb0i_yDq_OnkSq2zTdeofTnXk0aEegxbTLNoPwlFvxy2RRoA30MPtpzfUZIUs_y-ApDRGB6CdoP9lFt-kO7vA18YL_I-Gzp_Wh-5Yd4vXqNLqoEL9U1k11B-lPLYR_93lyzljG0iD3vSY7SMMbV8P8C3PUmiEGd7GKEval9E3h2LB_fF7Q392Om7qOV5FfYpJh8KyzlVDdkN7N05_ZhObX2Uo9KvhrBkUREEwXwNepQFZPecZYpepRJabHlBZfpXMZBDhh_AE8EmYZcWWr3OFgakH3g5o9ZPNVxoSEfyeXB42_ealyeDApSEFDNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۸ صبح حمله صورت گرفت
(توی روضه‌هاشون هم‌ میگن رهبرمون گشنه و تشنه بود! ساعت ۸ صبح!)
اینها همون بگیم ساعت ۱۰ صبح فهمیدن! اما دائم تکذیب میکردن!
نیمه شب به وقت ایران تایید کردن،
اونهم زمانی که ترامپ و نتانیاهو با قاطعیت و رسما نوشتن که حذف شده!
اگه این دو نمی‌نوشتن هنوز میگفتن خامنه‌ای زنده است و «کمین» کرده
و داره رهبری میکنه و…..!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDTBo-Ga_jSv7_gXGxBYdqJqsPo3x0gE6Nl7qLVj3BAfghKiy-2WKT2X6jYC3GW7xhRhn3bPOX_sZ-zulbxjnwEo0BtwZnhwlSayzhDd9erdmEsVMhAIGC2khkQDtMExQM9fi2r3plB-hKYjak1tvKRvzYrLdjoqj4xdaFHwXb_wra-s1wAIQPSGrKqE_Peq8tKWm88vTYkoGbZLNhv0_WjNXDGNCkXEMJ81eRVGv0eJkSOKoglmEqF7j1AiXdcJTtuuBsXGw7kzU8LNqUej5UDD3q2w7aPOJpk2RgCMVCg_vsii71BQIoE-5RQSjRNvl9EIoJeBDv1F6hxYaJSs0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015500535c.mp4?token=c3X-d_ezE_INRQ1yp2I8eKt8ZiU-DiEXVb2WsPtZ_kWhjQUviR93PHUrE83b4OifDlJPUyl1C5QLvHko2jbM_Bq4TjPv9lCrbYBDWT6__p4z1XyyyB6ParDRANryxS9Ec6dmfliocDwfSa4lE8hkN624PuY_MpjrU_wDtNiYA53ApV2LdvZ_I3qXlIZL7b5NjrNyIAt0i_kQyNARGWLOiKaPp8u5jIz5S8ijmp1p2KlrPAwQHqN3Aa0G_RjMuvBmf1ye5IVIQNByLX0lmoT01sTHFsfIrUGa76xSn2jihE5DFLNCPxAml2arvpV_7RLgugPRFk3u3_M7FveQ16sybA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015500535c.mp4?token=c3X-d_ezE_INRQ1yp2I8eKt8ZiU-DiEXVb2WsPtZ_kWhjQUviR93PHUrE83b4OifDlJPUyl1C5QLvHko2jbM_Bq4TjPv9lCrbYBDWT6__p4z1XyyyB6ParDRANryxS9Ec6dmfliocDwfSa4lE8hkN624PuY_MpjrU_wDtNiYA53ApV2LdvZ_I3qXlIZL7b5NjrNyIAt0i_kQyNARGWLOiKaPp8u5jIz5S8ijmp1p2KlrPAwQHqN3Aa0G_RjMuvBmf1ye5IVIQNByLX0lmoT01sTHFsfIrUGa76xSn2jihE5DFLNCPxAml2arvpV_7RLgugPRFk3u3_M7FveQ16sybA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ایران از عراق بهتره؟
این روزنامه جوان متعلق به سپاه !
در خصوص زنان ایرانی بدون سرپرسته،
که مجبورن برای سیر کردن شکم خودشون و بچه‌هاشون روی خط مرزی بین ایران و عراق «کولبری»!! کنن! در کوه و دره!
چون به این پول نیاز دارن، بیا بگو چرا شهروندان عراق، که روی همین خط مرزی هستن،
نیازی پیدا نمیکنن که دست به چنین کاری بزنن؟
اما زن ایرانی بدون سرپرست نیاز پیدا میکنه
که دست به این کار بزنه؟
تازه میگه بهمون گفته بودن به روستاها برق نبرید!
دستتون درد نکنه چه منتی!!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjP3jffkmXRwPEpIeYZdQnKgpIxvD4isLLce0tvyrrc5E_2BCWeh37x5w_F5JcNlM95oZwkmcsQm0LiQXoOgb_481dpotgc2QzBuKOorusQ3oST0ssacw42E_OhF5zwcitDaOzTAPBlERoPK_-uPZ9LrzjlBCjxPAIL4X8WCzqbJcww0m3k7-QwhY57ooTLwb5-M7khVb0Y4VPr-iaZ9sY8AzK2ove3xw9gnxXPzYmCKNZHg0aL3LvfyOuSCE6pz6zvZvN-gNa6zOi06hlbKPcOekhNEee-vrO71sS1gpOrHY-h5YbNBb80avdTTnnzrnNQe83rbrOI5CU1fhvHJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=Y2T5BjgO0NT5gnjxueV8dkXVpeNsfIsnfyVq7RVk4P4C1ys9lcG1104m3tuq1yyb9RH_2kYlIHVmwg8X5Kc9e05xubRe7loctyp2xOW4ASNHThBEE1kGRnvHhxijgveOhu63R0I_HLvuaVlaZHF-YiyAEgDmZglAPQUnfwx77tW21Z0PjFPiqwlmKBrUKp6VE_Fgijyz1SK9AG203Lw-R3okqpI_mHpWAdqVz2bz79hSDoWu50geynhMRJN0UPU2ZoNvrwRRkhXfyITcII8p_oxCkbxeOfLIeQMtWVOROZ5g2lKN74TCc1W06yU9aKZ7FAijmBou1lIxLtHPeOtX1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=Y2T5BjgO0NT5gnjxueV8dkXVpeNsfIsnfyVq7RVk4P4C1ys9lcG1104m3tuq1yyb9RH_2kYlIHVmwg8X5Kc9e05xubRe7loctyp2xOW4ASNHThBEE1kGRnvHhxijgveOhu63R0I_HLvuaVlaZHF-YiyAEgDmZglAPQUnfwx77tW21Z0PjFPiqwlmKBrUKp6VE_Fgijyz1SK9AG203Lw-R3okqpI_mHpWAdqVz2bz79hSDoWu50geynhMRJN0UPU2ZoNvrwRRkhXfyITcII8p_oxCkbxeOfLIeQMtWVOROZ5g2lKN74TCc1W06yU9aKZ7FAijmBou1lIxLtHPeOtX1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
شنیده شدن صدای انفجار در محدوده جزیره قشم
‏بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
‏
‏بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی  نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=seL-b_sdOx-puZ8mwoIBXHwy-zKEd7nTnPnbqKFS2KzYGjelQL92-5Y9SG1pL7KbtTENQn9m0zXbWBKmEj55DvLh3oyjOba4uLEJnHHerGL1EtZHRi5WTZ0JxyWsycoAv4AXKUIg0yyupNXiukznpL2ShJ0CV2k4r4JTwjJEEERal9cKUdxkUabPuwczMmb0m-cIYfm95YMtEJYRVZjW1OisflwPXQLg6xhoHD0vWoeixesTJGQISZjINIlQy8deJwO8m_7HvJj6qAlKT-MIzuBOTCKkWJSvMn_VJNxgZcKTWKWunfi52Ik1EP8vi4swZHnRoAxKHL1ksUOeOClidg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=seL-b_sdOx-puZ8mwoIBXHwy-zKEd7nTnPnbqKFS2KzYGjelQL92-5Y9SG1pL7KbtTENQn9m0zXbWBKmEj55DvLh3oyjOba4uLEJnHHerGL1EtZHRi5WTZ0JxyWsycoAv4AXKUIg0yyupNXiukznpL2ShJ0CV2k4r4JTwjJEEERal9cKUdxkUabPuwczMmb0m-cIYfm95YMtEJYRVZjW1OisflwPXQLg6xhoHD0vWoeixesTJGQISZjINIlQy8deJwO8m_7HvJj6qAlKT-MIzuBOTCKkWJSvMn_VJNxgZcKTWKWunfi52Ik1EP8vi4swZHnRoAxKHL1ksUOeOClidg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=tsOMPeNjh9jzpfw5NKbTCZn2yKvFwcoZEnJP7sS1an3biYhZWQrShfbU6vCvVADfH61dNjZd5ApAXte0CLILzokicuOoajgiznkiQd2St7b1TvOGEbkTF_6QNtUusStGNaHbnkThEvGLBopqTujj4ePFMYoI96qPBpSvXVN5s2WmLqjkui0a2yjpWfFBL4QRJ7wpzpL2NLh-JnS1pOAD1infUkIWCFZBNhTSp91x6vL3c4HfIkaRazJ57X4qEKjh1YYpACmEQ4brPdY4OcX-HTXAkiUiQuSVgtRBDedXf671OdGz9c3aVvJi3s__nsGxE-WZsJ4WITOfd8EO420Dqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=tsOMPeNjh9jzpfw5NKbTCZn2yKvFwcoZEnJP7sS1an3biYhZWQrShfbU6vCvVADfH61dNjZd5ApAXte0CLILzokicuOoajgiznkiQd2St7b1TvOGEbkTF_6QNtUusStGNaHbnkThEvGLBopqTujj4ePFMYoI96qPBpSvXVN5s2WmLqjkui0a2yjpWfFBL4QRJ7wpzpL2NLh-JnS1pOAD1infUkIWCFZBNhTSp91x6vL3c4HfIkaRazJ57X4qEKjh1YYpACmEQ4brPdY4OcX-HTXAkiUiQuSVgtRBDedXf671OdGz9c3aVvJi3s__nsGxE-WZsJ4WITOfd8EO420Dqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=bI1qIe3tMbAm5qMhy8YMAZrD9ONhbj-HuPPoEwwukPp2KSshEGJqNFvTp0seyyBar0GGYVghAB5o6gfiao8LsrhCR29ypcpfaLf2KBtxbpFDBGBJjYcnuAW3_oLDKeYcUhxNLu70M85nUQPRT9KoremqxjyCsJVjS8vog_GXh7SuzxXYBJsFYmQPqRECJ3hQwY24pkXWDDNTW1JGyEHB0bqfxb4GElfkIS2DKGjyMegtyRyoWIIKf4xORElMkKGJ9_tc5TPBxVnyUNDdjzElnECalDO4Lye_QDUxssahS6QlhazKwHACfGm4g6loZGFIDp9Kd7z7e8NuHQHgLw_Ezw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=bI1qIe3tMbAm5qMhy8YMAZrD9ONhbj-HuPPoEwwukPp2KSshEGJqNFvTp0seyyBar0GGYVghAB5o6gfiao8LsrhCR29ypcpfaLf2KBtxbpFDBGBJjYcnuAW3_oLDKeYcUhxNLu70M85nUQPRT9KoremqxjyCsJVjS8vog_GXh7SuzxXYBJsFYmQPqRECJ3hQwY24pkXWDDNTW1JGyEHB0bqfxb4GElfkIS2DKGjyMegtyRyoWIIKf4xORElMkKGJ9_tc5TPBxVnyUNDdjzElnECalDO4Lye_QDUxssahS6QlhazKwHACfGm4g6loZGFIDp9Kd7z7e8NuHQHgLw_Ezw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در میدان انقلاب تهران چه شعاری میدادن؟
نحن جنود الدین و العقیده / لبنان لن نترکها وحیده
ما سربازان دین و عقیده هستیم،
لبنان را تنها نمیگذاریم
(همون لبنانی که سفیر جمهوری اسلامی رو اخراج کرده و میگه این جنگ رو جمهوری اسلامی سر لبنان آوار کرده)
فردا که جنگ بشه میان میگن :
موضوع ایرانه! تجزیه ایرانه! برای خاکه!
رستم تهمتن و آرش و شاپور و…..!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5269" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcBAx4S9x4OpABmDjVUyIIKwum2MR9WXjYz0ORJivtROD52BsN33I3qwDWtHwxtO10y6H17pylHrp6LhqTtL7o-MEK5QjaTijBbI11nTqitqByO1jMIUQly9FVaO5imED0ejYrXmSR1UVcXApKG0nMB86_DajyFPKD4-ULJZfPCCcoSkDhno8-Qb5sMIzOp_1mLVxPDCGJgYSV4EiIFtw1Tq1h1Mszjf8FrhQknvqSWioiQWK0ng6X92C3lIJXqofyxpTpb9BhN3GVZQPyMnfp1IdSeKsiRoL2Z-Rpx35JsOjiwFefomHHA8zONtIWcnB6J1LbuE_LoYn5ZTdH0jsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKdQ_xqkrxvbs23FU_nBnpURaK7VCGNydGntUltfYaohRBiBcJcaMojnSETxv1Md3C579TrDX4r3EZPTI-BnbdptgS8l4uYMXkfqwcnTpKqG6qhIzSJG9DmmaAJgDFtnkrqfc5ZIsZrgyq1OwJ2HQfOumtadQjd6Acn64cWUCtq-QymsCF_gm8WLBMSuykkWtjxR8JfaHuzUFH0GZObMnZXlnXWYr5yY6Da0-GAFGzCUdx8MOPYMYLJAnpkzRmcnIvCs3Jlt_lCmTeCSjWc05eE-aAecoz665DK3KiJO1Y3_p7caB71usHS1Wv-8ckjISotJOcPp2WgYbGlXjNe8kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrNcLuTT2IO3GThg3GYM3gcZljZisc_FCmEhjXY-a_Trl-h0vHjMPiida2hSadq4htAnIp1bCbJmjqFwpRYAROs8_q16pl_K3QyvWHGzdZqz1tIXiV5ROqt9k-tgi5FCMH-movWm4ypGYrEuDqzlQ54QQSTtIifISRphTt_he_yw_It9VkLxdAoQ1K5YMcYvZirbrIpMpODqejymSS5yHs9O1jhDYKTdELOgTJrWx1WnYmCF_Ldt9DOcocwDZyJNw6NGNHpnexUx467Ff2735bOzJWLynAvP2Xtcw8p904wb7XPyiWoVpf6FAR4P3E4-eP9gt9nOqlz9bCIXPy6kfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،
وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.
منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!
یعنی از زمان هخامنشینیان این بخش
یهودی نشین بود! و ربطی به اسرائیل به عنوان یک کشور جدید نداشت!
دولت اردن نه تنها همه یهودیان رو اخراج کرد
بلکه ۵۸ کنیسه یهودیان رو هم با گذاشتن مین
منفجر کرد! فقط و فقط «یک کنیسه» رو نابود نکرد
که البته غارتش کردن و فضای داخلی اش رو نابود کردن ولی دیوارهای ساختمان سالم ماند!
۲۰ سال بعدش چه اتفاقی افتاد؟؟</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5265" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyTPZFrYwQdgJYo2NhlYGGRuJHtf8_byXje4Ato8890cUe4nj-Ln6ZPhuXEjCH5OpXmHXTu9h8En-w5V-kb7x5hOtdtK8EhkGewpPxN86WGv_O0Hj5hRoEmVj5PEgCFnpyrfVIk7ZiC3GrkJHUowmni2dxSu3miXon5Lv2CsKvIvXsAYzhOl058B5_Q3VieYArVCkRacUG_yg1vonAVWWbcBRo7pDH4SDiTIR82picSK_NSDg5nJGYBAbeSCQzYETvOhFiGlFhKL4Bf_9-qTjh3hZ0q0EnI9di2n7PYEKzax1iE12TpGJHfzV8ERWMNXOnggJJtsn7jWlbKLH3ZOYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxX2nvuE-kWNxyX4rBcEqqvi3ffempJB8m4CXB7IQE529J03gbM4M7YkTPOZQfSL8WiIdUiAC7_0H2ycjnGd1Eh4zuDYtKs1Sp7zgblM49IBqhtSRYmP_SfGo-edX_dPD-kzak6KfMOzP5OiPc8Kl8ca4Osj3o9QeSIkI-9k2-z95yBLjyf8lhDXBdqOg_sLGKjoSvpbn1k5DSu0Cgg5kWeuL95myDS0ms52if41yf_fq_S2Mg8cu18o0wOrUP9S3yM8fMLhnhpiCZ57fB3Mey30P6i27plcxRwnxZJGHgAY_jv8A48cjDlUNHXhvjnQN-0Ca9hCxBf8U9rSjrU-JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDFAr19Hg7PugL67r6yyygOrvmDB43tVNrEYBwRAWFYXUPLABpDBYGVxzhWeyfqGV9m3nKWe7KOtSebuX_2DW4zghM-ptuO9lmtdgRJvW14hMfhj1PKFh5-YfOBRcB-NgBuRNmAZK1gHCfA4CblwqVWV8XN5vUM9oFoPktT5tALxWRv8uTqlGPtTWIVveXliNA0ZKoqk7hlgRNJlqFqWfCqb9wDeVjMMalqVY3ky3U2d5LluJ31TzUVzb1DLBEO1Pc30Xgfoht-lbyhg6jlDRTg48QfjRI8gUBjga8UHlo27K6KYxOZpF5GpsJ_vFWGYCsRq1l8ZZ_OnHYeWrSEEig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZmoY1SKF35bywHAdJk5k6nj8uR_8lt0cKD4ebV4u_l-vjaY0fB5_DyRETk99mlSHEaCjx3N8WIMVnQ5ZfuUcSDEABapDMgR5rYW0UHdYiWUGTOuZvoHlkFxddJbUwinyoWOugfxcyglkFk2W4AfPkFGZaHV-OqmtS4MIvxrmu1HrglbmkCzcQ5RHZK_-ik7aZyjH7pruuDDXURfs4L5ijojdtFEIYqoi66MeUGw6FLiQM1dp38Lt7VCVm1wS-fWBHKcjLuwpGmfbvAm88lZt6opSYG3c6mItZYbEILyD8r0ro01SMt8g3qQqWxa01yNj9uR4TQw1WKcAc1-0-n8PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=NDneYrnAnuYpAJWA4MWhFifDkU7otbsCs_2VCwxeYp4uSvYHN_ucBN1viuenpvfGnoaQRb7nM7pialzoAapj7cvLWVY1m00mENJZH3XVTZ8L54iifl61vISeGFl2Xpb98JCnb6EnlW8FYmWgQB2PQjtOTi7ArIsIAS2LdpuDFmGZEAXMYIwTMRyDQz8BHXncdK10Z23Y9saCr44w6es73fTamMtPtYvc4qahUdz1ftoEf05aoHwQrCaVKXH8qgkQ1_1HEh9OqeTcqHd88HydoDArEYMrhwBM7YA98OfA8gAhE9NV5OJ9_KdQ9avVhdabRzSzNa58bc_gQ3lNd70q6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=NDneYrnAnuYpAJWA4MWhFifDkU7otbsCs_2VCwxeYp4uSvYHN_ucBN1viuenpvfGnoaQRb7nM7pialzoAapj7cvLWVY1m00mENJZH3XVTZ8L54iifl61vISeGFl2Xpb98JCnb6EnlW8FYmWgQB2PQjtOTi7ArIsIAS2LdpuDFmGZEAXMYIwTMRyDQz8BHXncdK10Z23Y9saCr44w6es73fTamMtPtYvc4qahUdz1ftoEf05aoHwQrCaVKXH8qgkQ1_1HEh9OqeTcqHd88HydoDArEYMrhwBM7YA98OfA8gAhE9NV5OJ9_KdQ9avVhdabRzSzNa58bc_gQ3lNd70q6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_IH2ZaxCpvSIcYrBPtCS_z7IsJziZeQd5YLsDkYKWhZQLnln1JsQghkY6UyT8xFCHWcTyyGGAOl9EKIxTEPcBieAywxk6XR7IeEm0Oy_nEBREvu25ITeg00PSzXhzZA0RELaQ1pbdrJnFcds_7RwY_83N1rZnQ_JZYCH9accRTRCZEXa7339SWkF4x7AS6iJNJCsNP4tCNRhiGPAI5FNiBv9lXX0B2r5LEl9aIoD7xlUsoBzFHVTVBae5FGfpqqQBZPcc4gniiqZYDUPSmwG_eFjFWvo6aObuCSjNVtIK0dWNHp20_Tmboo81V4-DFhpWb_t6O_F6Ea_jJTC8dwAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LvymngwpswDFa8b9As7v72omVEqAlxTnAkKeg7cERHQZNuE9qcybPdl1u9zY5suX3NdK1GpgwGZzU5LqiHWC25He8I5twz7Iww389mOQOUiXBBjG8YkspTwtUKVhmLw8ABV_lxtCiDAmsUGupMVpa58gmHKawCfqNjB1QxrayW6OnEs-mn9mXccDK7l0WCNoEYKIdYt3YlVtNxuWV9lmHLfIaLMIT_R8WeAzI3kPsqFXVmywmg4un3-_XggX2BYyj75HV6RVTk1SJvzKrsTQqtCVFtw1NAAnvfhq7wJ4x0a6PCbe7Lot2UYGyTXygtmY5u3XSTLJggebZNsthQmJ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MPiBxAob_LIh5OEO_Feh5HXoe9-FSXDTZ5XBMlTykETJEJQr6OlazicnxXZa3jDFb8zVQRqoqUZuAWK7L_0sxmtsEvOh6OisE57UlZhGW7jL5dAKBi_vJp5hR-cKatiMOhkjIMW-_tRcOUxhVu5tNxKTV_Yf_AEE2xRQURQPnqUS9QWFTgpazncTgPuLV3EnDrOfYPL9sKfbkI4Td468qseUYUYeQZpGSokENQRG4lODXrLicSkXjWOitRCMfvWWb3rD9-lgaMBerw5bRXeXISr2gzqRa0IM8g5vr7LF9MnKjdL6FnP5kOPxTi1D9O4sN0cEQkcxfPSX8X6R8pR_PA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVsf3Bc8UmV2rxV9zTsugiQdgjSL-rzNCjb1ncXh54OF2pXpyxQsz5y2ijmqFvuiqC2zL1mTUDXebIjmvP-SvD581wuz4BxiPQARlt50z3EZBhwYVfmn_jlzZUoNNmYfA0HzWwNcVRaFtLzKR5oIpXFVCm8DZtrpeXr2nvYxbz8yssL0WfeU3lzZFPUZAdu_faihEMMOWT8GZhrhqb4KUIwPMFiTJvSXsbkDdaYms-XLN4LsrysqBeNI5AdQlL4wAhYpB6h0Xpz0-ozfEeQ2yH2meiwQ--C2C4MwULknguTCIMcfh7yIA9Vlx-j4lTT-SkjFtAkJ6UrYNlK5QPr_uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IGef_QnwNGYMmaEfqT83aj5tXGFwOlsS9ROY77JerciAuzI09eAYWvHvL61PHmYZ4TKkb7X0VvN1sC7iNDI9dS_fTelmmjd8b6Rs_Zai8PomSFYNeS2SRYOSrtGHqYfi5buyv9d8YYg51w7kVt7RAAvuktNauS_DmKtwfez-RX1rNWpeP7_ptyTAiarmY5--w_NBIchXTcfS1_2IyjaIOY35v3LMv6VVFOyL_R_fFCnEc1WadG3q7HdVlAhjuhRm3s_UIEsWtvPq_dF-Chk-O08KbOa85mSvaA63Z2xR0OoozTbfDVGLKUxVJAUaLlibo21TiZtwJr9ZAMSbYNPzGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ovnDeo8X_vLpCiHlb2usT-honxhngRN6ljKHRc9wuq0A29H5bzr8lX-cTbQjV_INj022sOtWl9dPE0rMlGbN0cNmtgBnmdWq-j4KPMH4c1IkvsrKF_4SYb9R5AA4-Uvjn9gDvzcF607YALWKVOuw9hIfZvotS23y2CLX6JzHM4EyaA8ofSXRf7yLuLqGhGN15hzHNx2n38W38T55Rdqn0MTxmX2YB_V8VANnTzGbfuDnqfBvbPmhofnu__S6hm2gkjGxqVN8AaF8HKdRwVpGq36ARSR8uD_oTdma2oPxZMXa8pLkzNvsLM_limCL4rJpJMOFrKQ0LeB2exb9R1H2rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o9Xgrvwuubkb1u4SWuQ8ze-0rgdGiG5kMzukzIZeKKFfHPYsb_WDRGe_JfmnmDHwoL1CfdFYqHCGeOMRovTpWaGi_RPc2C72oW4Jo9ei7EK9EDv2pVsk8mOVp6Ve8IWGNUOugyfOQppPLgZdv2us3eR-oktuXk-a4JD2s3IGNrTETFtfSo8gpJgaxozGYiwTfpXRg_ZCnySnH9DgSb-N_7FJ2dLIyAdIGNUDZ8U_8kmu0IUK2MFxXAsuMG78p01z4D1J0ooHosCD3rJ3AUTbxHJL5XkuP1zI4Wr9mbLOMQ9DQIphSU1LuWU0phXBjwSv78C3hPY7M-fE6FMuFdNdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y_-Izty04m1b6CgOK-9UXFXGb3meia3bhX9mTmhjzUlEivjAtA24uYcq2ZPv7SAohfQoDs8imaL2qHWC5Ax8sCsQxGjyH0uAC-ZcRY0SPas_rbE6ELIQsK68EzZWonHeu_ZWppE7bRVs5bMi2Uy88U3rpvUQRu5QkzSfjPfzHFeWEhJvyGFHQ098wmDK_yr8f-BX_oM6PKTT1xnCCBqXsK4EZ8Jv8AEaj11CISfhHw0geezvSejY6YPVXeRYQJjNcvEblOiORxO3-PJbUMzOx8AHxQvRhWbdYVezwsGQnKAQOXwMtb9wqFjdWyh0pNOC8nh-GAjKmp84bgU7CiIeEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">و بعله! خامنه‌ای و پسرهاش
خیلی ساده زیست «بودن»!
فقط در زمان رهبری خامنه‌ای، برای خمینی مقبره‌ای ساخته شد که هیچ کدام
از اهرام فرعون‌های مصر،
حتی فرعون‌های مصر!
به این  هزینه و گرانبهایی ساخته نبودن و نیستن!
این فقط و فقط «یک قلم»! از ولخرجی
اینها از اموال ملت ایران بود!
در کشوری که هزاران مدرسه‌اش توالت نداره!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=vXsjFqkZizgt1k9v2Ejrx3BGO20FmJx7NDBOTRyuCU12QdKsUlzeyX8GhXVemXZD1GC9wGN_M79TgZQLXVNRUluazQmD9KpFxeVqeZTMek5jrteQMpDEwr_JrLNISwO5cFxmGkxMoEhrf7RkWp4P1L9EGnNv1qhOX02hpRM9gzThAxkRL3NkFHgsvPSMhwMOyWTnbOPj8XKXLRQi7r0wzegJL_qsAc8GM7WbRdkA0PrRT5kwVcUf8wETsIF3sk4Qtm9ol7-mA1SIUTeK1UeTI-KZIKlgIQgH3Uc8xpoj8vvMUv9Ypo9XuGbJAcqfaeUhkpgutPwHdWERFwiJGR77ICAy-RVqOEA5TsC_DApZctxN8LIoHF9q2Ssj6MrdCvBqR1B7ESVCMQnHQbDZBfsW2UiI8fqrCwwTDB0UzKCbQ61gD5jPL6lyo-xPdYogH_d1wz4ArKs6WlaLDsrPdQ-JJhzbIG8BeodVX5fnkKIgTR9tNOtDCPjYev_epznzR27Cqqzu3A_2MoaM3N3YlvFj2F6NMEE3JqC5aGN_QtT9RBva7DdAGADCfDYUJFVmpIlGPl3ejjJyW2mvrOf8N-Ize4OELbAAeVjx9laJ9_ZLNeyCyLaxpgK_ri8GcGb4CxwZvUjCRY4yLSYrr7sAPP7sO8RhcyFep85Snsl_Fprj_hY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=vXsjFqkZizgt1k9v2Ejrx3BGO20FmJx7NDBOTRyuCU12QdKsUlzeyX8GhXVemXZD1GC9wGN_M79TgZQLXVNRUluazQmD9KpFxeVqeZTMek5jrteQMpDEwr_JrLNISwO5cFxmGkxMoEhrf7RkWp4P1L9EGnNv1qhOX02hpRM9gzThAxkRL3NkFHgsvPSMhwMOyWTnbOPj8XKXLRQi7r0wzegJL_qsAc8GM7WbRdkA0PrRT5kwVcUf8wETsIF3sk4Qtm9ol7-mA1SIUTeK1UeTI-KZIKlgIQgH3Uc8xpoj8vvMUv9Ypo9XuGbJAcqfaeUhkpgutPwHdWERFwiJGR77ICAy-RVqOEA5TsC_DApZctxN8LIoHF9q2Ssj6MrdCvBqR1B7ESVCMQnHQbDZBfsW2UiI8fqrCwwTDB0UzKCbQ61gD5jPL6lyo-xPdYogH_d1wz4ArKs6WlaLDsrPdQ-JJhzbIG8BeodVX5fnkKIgTR9tNOtDCPjYev_epznzR27Cqqzu3A_2MoaM3N3YlvFj2F6NMEE3JqC5aGN_QtT9RBva7DdAGADCfDYUJFVmpIlGPl3ejjJyW2mvrOf8N-Ize4OELbAAeVjx9laJ9_ZLNeyCyLaxpgK_ri8GcGb4CxwZvUjCRY4yLSYrr7sAPP7sO8RhcyFep85Snsl_Fprj_hY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=dhyokQtL6xsegCjbiUOFo_JNgJBaaNWTVMMmtvuFhuAy7tY16ETF-Mt6WLRcYnANtovYNgEwqzdgg_KSg-l_9HfYPR5rD6CoS09pP0PI3BQl3QAjMtWuYrSTFlwpw3tMVTXzn_yHxJ3gTbPZmeH8NTBqNda457_ezcfbGXbmWLWIoFZXOLkRsAKYWMG0JDeQKnURz5yBMl8plqH8fD_rwQQrp-6joQqGs6xW3cIYnVe-sxeu0bHLaHVjzCUbZCIDcOW0npb6XpR1BHcv_36cLOxHezuwIXs3DxBLpguTO_kQoG9017uOkSXLMugpXQXoiIia58nypPgIWllHu-u41A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=dhyokQtL6xsegCjbiUOFo_JNgJBaaNWTVMMmtvuFhuAy7tY16ETF-Mt6WLRcYnANtovYNgEwqzdgg_KSg-l_9HfYPR5rD6CoS09pP0PI3BQl3QAjMtWuYrSTFlwpw3tMVTXzn_yHxJ3gTbPZmeH8NTBqNda457_ezcfbGXbmWLWIoFZXOLkRsAKYWMG0JDeQKnURz5yBMl8plqH8fD_rwQQrp-6joQqGs6xW3cIYnVe-sxeu0bHLaHVjzCUbZCIDcOW0npb6XpR1BHcv_36cLOxHezuwIXs3DxBLpguTO_kQoG9017uOkSXLMugpXQXoiIia58nypPgIWllHu-u41A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwH91OYHORK9lJS7P0reFxj9BPObNh58_4mt_9zB121z2f--TPoD6r___y2j0jESphoNNi7flz5M0N4su5L0GKf9rtSR6YMnr7vQu3tbdkKBr8m46V3Fb6nW1EKa4_72sD9zsJFpc8pShsqadUuJ1C7Z6kVcVSnP6o_1Alc4eu43t10a3hg2NgrqJLF1WgkKA1Zzl27Dz2uu1MOTpc5z26EZsWEIWxAkOaPHa6TWH-FFDTigSPFlyhASitHAIZxEgj_0G8o46d4YCq1uur7gk9vXbSOBdtKBkpl_Oo4RqmKeyXDvmlbkipPj-PPrtjuT0HwMV5xzJ72ZGHODUpLhyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف گفته که اگر حملات اسرائیل
به لبنان ادامه پیدا کنه، در مقابل
اسرائیل خواهند ایستاد
‌ و «زنده باد دفاع از سرزمین مادری»!!
میخوان وارد جنگ بشن
برای دفاع از سرزمین مادری!
حزب‌الله برای چی وارد جنگ با اسرائیل شد؟
برای خونخواهی خامنه‌ای! که
هیچ ربطی به لبنان و سرزمین لبنان نداشت!
اینها فقط برای فرقه خودشون میجنگن!
نه ایران و نه لبنان!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
