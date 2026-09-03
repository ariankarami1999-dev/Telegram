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
<img src="https://cdn4.telesco.pe/file/FDrOZfdkW0TIIOVoM1CWU-8lsw1SHVqJdH7JkBa3bXQVdOenECHwo1RQatnY4FH8MWaICa5baQJ7slLjaDW_QdvH65bugnpCHDZrhUzFuOny9B3o6SxDm6_8Z0H0UQV5v5IOXhCDVQltCEL1zSY2uq6aO6qOn3IiQABJUM9N1CGLDj61aodAHVaIsVn4Q_ILI4laWIncJ_BSh0k3QtA4ELIQ0LGph3BOfGA5kDp1l9rSEmHBq-jfF9_k-Anc6CTnpfd4knlhgV2rN3LnWtqKlx1aLg6ODV4LdkueKKK0FgSow6PHHx892uuJ98ashmrxw35CDoqQpYISSJmVGTtLaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 112K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 17:11:05</div>
<hr>

<div class="tg-post" id="msg-71054">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLAfpojiBjs7iJM4ks3rgtjXHGGFAeARNU7rds10ZQMelphYrRCC0QZYnzkPGL_-76eLTYeNJ5LsBx1jACsjAfOAuW0EO1KjPpv3V-qK_WkuwA74dRKhAmyp7QUzRq3_IRBYtkjPufLeRP5fVe8GcP4XZnHybATb0WX_52q1AbbKaFR0yGxV3Ojbi2X3J4KeDGUN61K0a6fc7L1q7NrGWrWJxCnGE7qEJ6K4FcaVlWHD47XRllJcOOTwmSAGpIqJEQMxB5KV5dccOpg4yT3Abfrxe9cCrheMp7t2a3UcCSnLBJzlgwQ5x2Wk-rDaNc-VhKWAGyZNP4jd9XAYXwORWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
جمهوری اسلامی کشته شدن سه خلبان نظامی در حملات آمریکا در دو شب گذشته را تأیید کرد.
اسامی: مجتبی باقری و حامد اوکاتی (خلبانان هوانیروز/هواپیمایی نیروی دریایی) و حسین مهدویان (خلبان نیروی هوایی).
@News_Hut</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/news_hut/71054" target="_blank">📅 16:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71053">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03924aeb44.mp4?token=SHO0WlWDXb074odm41a3_4VsWK0rqm4Dwd0oBhmAbvMmMf-6xm9pM95h-pMblNhwbXhDquBr52DtrakAs1esyrBz7RB53M1071x0HaKSbubnwBu965nHiq0E88HZDdnQrlNOD9hgn0Bnlt-gx-dmxWjAqeW5xklh18jGf_cb__YvDNi5k2IrsvwJ857DqBc-1t9e1caUk3U6WfuqrjF84B-wA9D-5acyLZOxpSj77NpBMlHvqMvnrB4BAkKJr-fj-214w9uXL04N19z7xDy6JirMuYGNRYMBKBWOMEHQ8-NBmmNOvTLAjR2IbsJmRDsrwAD5HvzUzHM0PYCwLQXEbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03924aeb44.mp4?token=SHO0WlWDXb074odm41a3_4VsWK0rqm4Dwd0oBhmAbvMmMf-6xm9pM95h-pMblNhwbXhDquBr52DtrakAs1esyrBz7RB53M1071x0HaKSbubnwBu965nHiq0E88HZDdnQrlNOD9hgn0Bnlt-gx-dmxWjAqeW5xklh18jGf_cb__YvDNi5k2IrsvwJ857DqBc-1t9e1caUk3U6WfuqrjF84B-wA9D-5acyLZOxpSj77NpBMlHvqMvnrB4BAkKJr-fj-214w9uXL04N19z7xDy6JirMuYGNRYMBKBWOMEHQ8-NBmmNOvTLAjR2IbsJmRDsrwAD5HvzUzHM0PYCwLQXEbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تو ایتا و روبیکا با انتشار این فیلم نوشتن سامانه پدافند لیزری جدید اومده و همه موشکا و پهپادای آمریکا رو با لیزر زده.
@News_Hut</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/news_hut/71053" target="_blank">📅 16:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71051">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94edb900f7.mp4?token=meln53nV3zFAWRjvnF0EyabOxLGm3CGf5fxmskxQU9LFIWdNgLfC7Ox-JJoDeoCt_2sFIeiRFL3GNxcpAA-q8QUTYDEjjV8rTx4wUa0FqRhHMxAe84j6FL_nDRZ_22wEcGUapDZkTAVuBGuff_UwkwRclrjH_Mqoi7gW3vJj1GmAJ7ypi9TFTfgj4laEhsPJV3ym9bflgF3JJ9ZHJ41MzvOE5eZwUVkw_pgh8LxKhbebY-U6MNMGVBLmc3dUBHwtDNT1xeN1rSCpacbNFGTwhzTvfvLvFebQ9h8GDXlY3hIxhnyB0MIrJAurOhiP3BciVYcOio4B_KIvN4qJctkrEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94edb900f7.mp4?token=meln53nV3zFAWRjvnF0EyabOxLGm3CGf5fxmskxQU9LFIWdNgLfC7Ox-JJoDeoCt_2sFIeiRFL3GNxcpAA-q8QUTYDEjjV8rTx4wUa0FqRhHMxAe84j6FL_nDRZ_22wEcGUapDZkTAVuBGuff_UwkwRclrjH_Mqoi7gW3vJj1GmAJ7ypi9TFTfgj4laEhsPJV3ym9bflgF3JJ9ZHJ41MzvOE5eZwUVkw_pgh8LxKhbebY-U6MNMGVBLmc3dUBHwtDNT1xeN1rSCpacbNFGTwhzTvfvLvFebQ9h8GDXlY3hIxhnyB0MIrJAurOhiP3BciVYcOio4B_KIvN4qJctkrEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این کلیپ از یه دختره که سر سفره عقد، آقای داماد رو سورپرایز کرد و گفت من مهریه نمی‌خوام و فقط 14 شاخه گل بنویسید
؛
هیچی دیگه پسره دیروز طلاقش داد و اونم با 14 شاخه گل رز طبیعی قرمز  یک جلد قرآن برگشت خونه باباش...
@News_Hut</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/news_hut/71051" target="_blank">📅 16:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71049">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/01429c982d.mp4?token=EbinAKrZA_sk7XSW6uf4ZuZdp8BLhxgycTXg-F7BieE8fIHsvmc18nf65XVHtp2h9o3uxtq4ar9cGqniAXSSCQ82r3LZt9YR_p3vNTM6LhkwwV9V45XYwWJHwCZ54VKzhw6GngFWYgJCrV9NOJXRUrtvtd2B3PFQpRRh00O0V160RdHSHI0SQbFShLLXx9POlqKQRnRxhr8dbyobNTynromeOyL3aVto9KZBUkJFMA9sDAGo8IPju9Yn2dWUUpD0oR8pZNKqLYc05s2cB9ESlqjQt0trp07mXZ0gVPZueGiHpR5UgJW9tVfoaPJPsUT1XUt6xoNwhzeSy942x-F9vg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/01429c982d.mp4?token=EbinAKrZA_sk7XSW6uf4ZuZdp8BLhxgycTXg-F7BieE8fIHsvmc18nf65XVHtp2h9o3uxtq4ar9cGqniAXSSCQ82r3LZt9YR_p3vNTM6LhkwwV9V45XYwWJHwCZ54VKzhw6GngFWYgJCrV9NOJXRUrtvtd2B3PFQpRRh00O0V160RdHSHI0SQbFShLLXx9POlqKQRnRxhr8dbyobNTynromeOyL3aVto9KZBUkJFMA9sDAGo8IPju9Yn2dWUUpD0oR8pZNKqLYc05s2cB9ESlqjQt0trp07mXZ0gVPZueGiHpR5UgJW9tVfoaPJPsUT1XUt6xoNwhzeSy942x-F9vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز، اولین ایونت مد و فشن توی تبریز برگزار شد و حسابی غوغا کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/news_hut/71049" target="_blank">📅 15:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71048">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7913d873f1.mp4?token=aLXOFbwWVKRX6lr6uszpRFDaX6MNQ9AyXzZnO3oCIKh-b2ClRRCTIvosGfWxA4drfi82VEZK7wkrGJ4mDNSYfoGuZHaOWS6Jky_Jd9mUvT3NYemiLEcqff_toihuXMtEJq_Daj6J1o-6fYCJbgYhx6PlVQ9O1fw4AmS1W5dHpqheUFExdWnwhROvF5t3hMI0aB8Yn3P5Le7x4OroBvATi56GFO0Tu43BE8o3cRzkGAU99sJSKosuZUcgjvtUhV9ONP6nV3Q24MqA_Sqm-mt5p5QA9VEK3LBI3VJuBdGWM-k0k5XmmiDPUa8wsRg3xmGp7lej8fvMlke-HaMZhSXBeg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7913d873f1.mp4?token=aLXOFbwWVKRX6lr6uszpRFDaX6MNQ9AyXzZnO3oCIKh-b2ClRRCTIvosGfWxA4drfi82VEZK7wkrGJ4mDNSYfoGuZHaOWS6Jky_Jd9mUvT3NYemiLEcqff_toihuXMtEJq_Daj6J1o-6fYCJbgYhx6PlVQ9O1fw4AmS1W5dHpqheUFExdWnwhROvF5t3hMI0aB8Yn3P5Le7x4OroBvATi56GFO0Tu43BE8o3cRzkGAU99sJSKosuZUcgjvtUhV9ONP6nV3Q24MqA_Sqm-mt5p5QA9VEK3LBI3VJuBdGWM-k0k5XmmiDPUa8wsRg3xmGp7lej8fvMlke-HaMZhSXBeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این کلیپ در مورد پسرای زیر ۳۵ سال که موهاشون سفید شده، در حال وایرال شدنه
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/71048" target="_blank">📅 15:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71047">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIJc4Qq26UnaDoWpQynHwpHK2MblW9IPJaaA1oX_eI_A-C9Fj58QQe135j1mfeLbUrGfFYU20wIdA4ftXuyffFQ_9ovMYab2UQMENbRps67P5oX-mYT1vHkP6q5Cmv7mbTn0ya8WO-gmhPguzhW9oziY1zeIAYzu_BUCkOJeTJYD71H5_r-ybu20Rd8PnUwf25frVEgXJoDfWqyHWKygECBYvOpwcrtRbD5XZpK2lKAw8hkRr6UK9OyG2jWSHkJhUllArL8CfsT7GMO4zbKIxyN4GJoaR5wUwV9t7ZD3v3Sl_h_xO-ebiDywDeva_GSGW4-DG3UvTjvFXtlxykLcsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
خبرگزاری میزان وابسته به قوه قضاییه، روز پنجشنبه ۱۲ شهریور ماه اعلام کرد حکم پرونده صادق ساعدی‌نیا، فرزند محمدعلی ساعدی‌نیا، در دیوان عالی کشور تایید شده و او به ۱۲ سال و ۶ ماه و یک روز حبس تعزیری، مصادره کلیه اموال منقول و غیرمنقول و محرومیت از اشتغال به شغل کافه‌داری محکوم شده است.
مرکز رسانه قوه قضاییه این پرونده را مرتبط با اعتراضات سراسری ۱۸ و ۱۹ دی سال گذشته دانسته و مدعی شده است که متهم در «تحریک اعتراضات و ورود خسارت به اماکن و اموال عمومی در استان قم» نقش داشته است.
صادق ساعدی‌نیا، فرزند محمدعلی ساعدی‌نیا، کارآفرین و نیکوکار ایرانی است. محمدعلی و صادق ساعدی‌نیا در جریان انقلاب ملی ایرانیان در دی ماه گذشته دستگیر و اموال هزاران میلیاردی آنان مصادره شد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/71047" target="_blank">📅 14:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71046">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:  اگر ایران به دولت اسرائیل حمله کند، این اقدام اسرائیل را از هرگونه محدودیتِ موجود برای حمله به ایران رها خواهد ساخت. ما به تمامی زیرساخت‌های ملی، نظامی و غیرنظامی ایران - از جمله زیرساخت‌های انرژی - حمله خواهیم کرد و ایران…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/71046" target="_blank">📅 13:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71045">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7750e2ea67.mp4?token=cPjbLPvHX9tPeBwQ8L3tnT5s4gMSCYuTp_j6TgYJHP3pdkVtaznfRZvtNkWAGc5KdhqYmNoXw7r2UUlLWCQ2D_SOWqTyw6HazeIH-t959z9O7csho5AI48eSTktrM8KoTbRY7P2pzoK5LrgmJ06iuYMmSk7w2o1KgVlCm_FhPHvNrB5Pv2bhApspOAAMswRFEQYQX3WWV_dGAc_fkWPbxyBEaNJmB46_h-Y695C_1JqLl7uZDHhK4wRPQZoQ98qU8hMvhvu2mvadDv7q-XyhE_gM5JH7MYpLLBFGSZSz_gIWTeXdEIQmgjA_JH4ZuWEC-5rf1ieVmg16vJrTc2DJIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7750e2ea67.mp4?token=cPjbLPvHX9tPeBwQ8L3tnT5s4gMSCYuTp_j6TgYJHP3pdkVtaznfRZvtNkWAGc5KdhqYmNoXw7r2UUlLWCQ2D_SOWqTyw6HazeIH-t959z9O7csho5AI48eSTktrM8KoTbRY7P2pzoK5LrgmJ06iuYMmSk7w2o1KgVlCm_FhPHvNrB5Pv2bhApspOAAMswRFEQYQX3WWV_dGAc_fkWPbxyBEaNJmB46_h-Y695C_1JqLl7uZDHhK4wRPQZoQ98qU8hMvhvu2mvadDv7q-XyhE_gM5JH7MYpLLBFGSZSz_gIWTeXdEIQmgjA_JH4ZuWEC-5rf1ieVmg16vJrTc2DJIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
اگر ایران به دولت اسرائیل حمله کند، این اقدام اسرائیل را از هرگونه محدودیتِ موجود برای حمله به ایران رها خواهد ساخت.
ما به تمامی زیرساخت‌های ملی، نظامی و غیرنظامی ایران - از جمله زیرساخت‌های انرژی - حمله خواهیم کرد و ایران را به اعماق دوران حجر و تاریکی بازخواهیم گرداند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/71045" target="_blank">📅 13:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71044">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b05262cb.mp4?token=gP4dez5ZLS2Dvn0bB35IITMH6p4UML1o9namrznt7O2wv4i9bs6GGj0AIqY7s_JU762YjM-4oAVsmqWt3IyHY7c7ta_aoJQxAn77UEiePrBJf4-2P3pMEt1plV4F062GiH249yPYTrmK-xepB49fOgKxfODkmiptw8NVKFDXxyfRB0zR7GPnGBa1xrRVYvhrArSNNkgQGuoYdj7QarY5jHcTBBCOY5W_PBjTb3SIh2VFexaRvb09AK5JzMqQXCxChr-eVolW2KVErwZpH3y3-WDOLjVVdAREIjWULPQp_bdDn5hUBp8ut--LjMZRis3jBaYQPITJW-e0y5TLNktujw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b05262cb.mp4?token=gP4dez5ZLS2Dvn0bB35IITMH6p4UML1o9namrznt7O2wv4i9bs6GGj0AIqY7s_JU762YjM-4oAVsmqWt3IyHY7c7ta_aoJQxAn77UEiePrBJf4-2P3pMEt1plV4F062GiH249yPYTrmK-xepB49fOgKxfODkmiptw8NVKFDXxyfRB0zR7GPnGBa1xrRVYvhrArSNNkgQGuoYdj7QarY5jHcTBBCOY5W_PBjTb3SIh2VFexaRvb09AK5JzMqQXCxChr-eVolW2KVErwZpH3y3-WDOLjVVdAREIjWULPQp_bdDn5hUBp8ut--LjMZRis3jBaYQPITJW-e0y5TLNktujw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
جنگنده میگ-۲۹ام‌یو۱ اوکراینی یک موشک اس۸۰۰۰ «باندرول» روسی را در ارتفاع پایین با یک موشک آر-۶۰ منهدم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/71044" target="_blank">📅 13:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71043">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162568634d.mp4?token=bDulJXWWcs0-p-H0py8se4Ei2zMejmquFH9_kYpY1b5QN8gTu80e_oBiJfiXgyo3LTr_ltnP7adUaI6C0A3bHwzPfioko5HuDRm7t-wg7tzGxXhfGGi2h6q5IoKdRBFeXuWjYJrCp3lKBGo7ZGzeNWFoU4DEXAxOtv66q78eyCUITnMEeTxoJtLWa47A5LhHy5jhgJOa-TI27ohC95PlgCCQQaX7ZWY30zHA1FDdx1RkIU0le04GjH7DVXniI8qDJre9FzF_kmEGR2-C0aby4OvgTDb5jUJ_1TEBmergY4zXlEhyZy1pt5E3IX0V0ufULhXP1tQe-Sn80eQrQ_5L5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162568634d.mp4?token=bDulJXWWcs0-p-H0py8se4Ei2zMejmquFH9_kYpY1b5QN8gTu80e_oBiJfiXgyo3LTr_ltnP7adUaI6C0A3bHwzPfioko5HuDRm7t-wg7tzGxXhfGGi2h6q5IoKdRBFeXuWjYJrCp3lKBGo7ZGzeNWFoU4DEXAxOtv66q78eyCUITnMEeTxoJtLWa47A5LhHy5jhgJOa-TI27ohC95PlgCCQQaX7ZWY30zHA1FDdx1RkIU0le04GjH7DVXniI8qDJre9FzF_kmEGR2-C0aby4OvgTDb5jUJ_1TEBmergY4zXlEhyZy1pt5E3IX0V0ufULhXP1tQe-Sn80eQrQ_5L5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
روابط عمومی ارتش:
در ادامه سلسله عملیات‌های صاعقه و در مرحله سی و یکم،  در انتقام خون پاک مردم بی‌گناه و دلاورمردان نیروهای مسلح، بامداد امروز، ارتش جمهوری اسلامی ایران، «سامانه‌های ارتباطات ماهواره‌ای»، «انبارهای تجهیزات» و «آشیانه هواپیماهای جنگنده» ارتش تروریستی آمریکا در پایگاه احمد الجابر کویت را با موشک‌ها‌ و پهپادهای انهدامی، مورد اصابت قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/71043" target="_blank">📅 13:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71042">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71042" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/71042" target="_blank">📅 13:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71041">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYRrzw3IDK_mKg8wZWwTGRzBrBTqQQCOZ3EV-5vO1rO1fKqvkCJ_JZyB0YvoHAWmSJByD7c1z6q8ramTYq1AOtUfCpc3pUBQXDJbI2qCT9Klk2ZIhxspXkNoqTkQRmdqAjUO5fKhM_acXIS8PZiLEbxTrDLIfNEVV8CzrCOCqUEhyucPro0eqS5OZ7NNe31NfHRfgjjkI8n2ri1z5xgwNu5lfQipkeF8odyZwjDit0u8wrHCilDW-IohCLAaHW1p3fzLDJyqgdcS3Yn7ul8gGJ1Cjn5S7GCQ-w2YJjXrE8csoQ-fTPrLUp8x0Hu7DK9T8OarKtdQJtqnVINuMyXNTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/71041" target="_blank">📅 13:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71040">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2218c2694e.mp4?token=qwYvlyxKpW0_YhnZ4uCD2tah6jD8N4VAJR7BXo0GseBUBj2KLHw1shhoRCSE3pu_l_7MfyqYqtyKxgunlMwe1rtTZgQsoTc2y6q_-s5aoyvkYvV2qXUw-iuXMveuf94XOuko5Vn3WWyvGw9eUFxmTePqNp2mE0JcLRl21Jz9WcHR56WAnzDWxx2XyDPFtojbO8LvB5EIlZd1SFvielxxN7hN4SVPxLKBuOEll5q7LGRHuXPmO1S9sdH6_W2KQpEgsZN6mCJEq0islM_t8X_rtgGTUEwv6wSxgdoWwCR9DsCPnDKVJtSIlIsnm4xixmpdUEEaTFn7osfAq_JZILCOTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2218c2694e.mp4?token=qwYvlyxKpW0_YhnZ4uCD2tah6jD8N4VAJR7BXo0GseBUBj2KLHw1shhoRCSE3pu_l_7MfyqYqtyKxgunlMwe1rtTZgQsoTc2y6q_-s5aoyvkYvV2qXUw-iuXMveuf94XOuko5Vn3WWyvGw9eUFxmTePqNp2mE0JcLRl21Jz9WcHR56WAnzDWxx2XyDPFtojbO8LvB5EIlZd1SFvielxxN7hN4SVPxLKBuOEll5q7LGRHuXPmO1S9sdH6_W2KQpEgsZN6mCJEq0islM_t8X_rtgGTUEwv6wSxgdoWwCR9DsCPnDKVJtSIlIsnm4xixmpdUEEaTFn7osfAq_JZILCOTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تو میدون تایمز نیویورکِ آمریکا، یه خانمِ چاقو بدست بعد از اینکه یه مرد و یه زن رو از ناحیه شکم زخمی کرد، بعد از اخطارِ پلیس‌ها به سمتشون حمله‌ور شد و به این شکل بهش شلیک کردن و کشتنش.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/71040" target="_blank">📅 12:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71039">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f52d28bc.mp4?token=QZHtbqdC0nqbbHCKWZ7sFyT9M7YQY_LVbqgQMvND5tVWLnamHyB24tA2GoInrI4c73amLmHw2BBWOt4kEFh_fsUWOG5_zbLNqcrFTMalJ4ETqMPC_tqQ5jDf1GEs6E0zTWHNVJzJGXfxWrEO0Vp7z8d2kdf1X1xrpqEsnC_9f87uM_ZBHqUXDPAt_s1uv35gaRykCACox95H8ohkxnjRv14Ks88Vvi9rnhCmukLbzgW6ajgdJ2-5c_WM1cmoZ3BwR7Q1PAH2z7uRUDtB0nHyXNK14A4lc5vn5YzoQsq1eM3YFCKnSHZzkZ3mRGwjXNpnb0WORXGcFK0IIFwix_lHYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f52d28bc.mp4?token=QZHtbqdC0nqbbHCKWZ7sFyT9M7YQY_LVbqgQMvND5tVWLnamHyB24tA2GoInrI4c73amLmHw2BBWOt4kEFh_fsUWOG5_zbLNqcrFTMalJ4ETqMPC_tqQ5jDf1GEs6E0zTWHNVJzJGXfxWrEO0Vp7z8d2kdf1X1xrpqEsnC_9f87uM_ZBHqUXDPAt_s1uv35gaRykCACox95H8ohkxnjRv14Ks88Vvi9rnhCmukLbzgW6ajgdJ2-5c_WM1cmoZ3BwR7Q1PAH2z7uRUDtB0nHyXNK14A4lc5vn5YzoQsq1eM3YFCKnSHZzkZ3mRGwjXNpnb0WORXGcFK0IIFwix_lHYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سایپا تو ماشینی جدیدی که زده ماشین با اینکه راه نمیره ولی براش کیلومتر حساب میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/71039" target="_blank">📅 12:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71038">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xg9gVFulhQXHc8O23W7c2kVCxFuEzOLeV_hgwa19nI20EY5jgQUSREsCYzoNd_Xo-x8veiZYgiw7Xvtc3VfYHj9qLdliWeaZvRoZjuWnz9loWuRoB5_1V9-Ksj4gUybkOMzWECDvz6DJPl89M5gi5z4R4VhIIUT3_O8jZxseVOstVEiLbnIuGhmf0dSoYzUSzucoas5a4vHDjC4P5B9smcydlRteOEIRHYH7EF_O7-Z9mTRrIR5avNlVsNeSiQrquuLwDMEL6SpBrTD6Lv3zLf6wFnFY-S0UH6ZKnYZZ2XiWXWBQzM5fThNbI-BTJ39awEBK0ekvTsQSQhOnEcnPkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
📰
اکسیوس:استیو ویتکاف، فرستاده کاخ سفید، آخر هفته گذشته در ساردینیا با شیخ طحنون بن زاید آل نهیان، مشاور امنیت ملی امارات متحده عربی، درباره ایران دیدار و گفتگو کرد.
این دو مقام درباره گام‌های احتمالی آتی بحث و تبادل نظر کردند؛ چرا که دولت ترامپ در پی بازگشایی تنگه هرمز و هم‌زمان افزایش فشار اقتصادی بر تهران است.
امارات نقش کلیدی در تلاش‌های تحت رهبری آمریکا برای عبور نفت‌کش‌ها از این تنگه ایفا کرده و در راهبرد تحریمی واشنگتن، کشوری مهم محسوب می‌شود.
مقامات اماراتی به دولت آمریکا اعلام کرده‌اند که هرگونه کارزار مؤثر فشار اقتصادی باید شامل تمامی کشورهای عمده‌ای باشد که همچنان به تجارت با ایران ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/71038" target="_blank">📅 11:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71037">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به بندر سوچی در روسیه حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/71037" target="_blank">📅 10:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71036">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef77017317.mp4?token=OtEDf0zd02zH-GvByiRMtHNJiBDiE_OFJH41zb2X3G2LDg8rzPSkXqA0OK4dxQXDxwUCCE7qYJTn5YtoNP-z9QEoP1cdwViLWBnuYIX1iXc-66Hhd4BejGWeEuZh7sOLpztlrR5vDVbKi2fXRgDRUBsL5Pq-AJoNwgBCyCz_-a73SrG51XqkouQt2PN2VKZSp7TOaV3G9UbMQ2Kp56v1a2Mut87yo5CkjF2XhLgRHIcAvuUiokwizRGTlvx7Gc4fczf_XPQlIBc2DG0tI3GJGgXDUS8XO1dpDu7sFXF0JmuCp1A5oSaE1NqGO3ILNzov5srzqJ8_g9JMNWcRmm_QQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef77017317.mp4?token=OtEDf0zd02zH-GvByiRMtHNJiBDiE_OFJH41zb2X3G2LDg8rzPSkXqA0OK4dxQXDxwUCCE7qYJTn5YtoNP-z9QEoP1cdwViLWBnuYIX1iXc-66Hhd4BejGWeEuZh7sOLpztlrR5vDVbKi2fXRgDRUBsL5Pq-AJoNwgBCyCz_-a73SrG51XqkouQt2PN2VKZSp7TOaV3G9UbMQ2Kp56v1a2Mut87yo5CkjF2XhLgRHIcAvuUiokwizRGTlvx7Gc4fczf_XPQlIBc2DG0tI3GJGgXDUS8XO1dpDu7sFXF0JmuCp1A5oSaE1NqGO3ILNzov5srzqJ8_g9JMNWcRmm_QQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی وایرال شده از پسری که چالش گرفت که تو خیابونای شهر از مردم درخواست پول کنه(نفری ۱۰۰تومن) و اکثرا قبول کردن و در آخر هم پولی که جمع شد رو رفت به نیازمندا کمک کرد
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/71036" target="_blank">📅 10:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71035">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7de7f7edfa.mp4?token=iqcGl5xXLWRHqdCJpQsCAYApAOLUk5CzYEaqwFz7BOW7PKX5ucUsM4X-1cGU5SDdxh3C81B0nQTTlTc70Ye3LA6PfWALrS9K5gLeMFLtnZMCJ5uSsiN2AIFyWkYgFzph4ajkSMrGHsoV0fu8V_ubi7LR1Tar5Um95yCNvnPyqFbR5PxBgNorFohNnLi-o9WSIekn048y3acGq3AW1W409kZnpvpR5untkJofgl_VA6Y0xB3wL5LydyjrN8uHADDUcfB0UfnZsM22mybXtK29yWwsxH_NVoSRdf5OY4V3sfESKR9mCwnZ17gXfpekYVB5F3caK8fMImkZp5-69t2vYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7de7f7edfa.mp4?token=iqcGl5xXLWRHqdCJpQsCAYApAOLUk5CzYEaqwFz7BOW7PKX5ucUsM4X-1cGU5SDdxh3C81B0nQTTlTc70Ye3LA6PfWALrS9K5gLeMFLtnZMCJ5uSsiN2AIFyWkYgFzph4ajkSMrGHsoV0fu8V_ubi7LR1Tar5Um95yCNvnPyqFbR5PxBgNorFohNnLi-o9WSIekn048y3acGq3AW1W409kZnpvpR5untkJofgl_VA6Y0xB3wL5LydyjrN8uHADDUcfB0UfnZsM22mybXtK29yWwsxH_NVoSRdf5OY4V3sfESKR9mCwnZ17gXfpekYVB5F3caK8fMImkZp5-69t2vYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ویدئو جدید از پرواز هواپیمای HC-130 Combat King II آمریکا در ارتفاع پایین در عمق کشور به دنبال خلبان آمریکایی جنگنده F-15E
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71035" target="_blank">📅 10:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71034">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad58d044a.mp4?token=FnlQp6GJOAblOxPCudmp9XDV73oUabhS9HBISQ9JWcxVG6MNRRpwtY4VJ6X6Dqnn-ZhUnBH3KFMqVBnrHST6a4iKCDcJf4m2LjAbOgIkk_cDdUH71KKC5qIIdVq6LEBnPjYmYwRGOawGfm_oqEjYCQ6AX1-cuJ7nbixSzmXS5pnB11vefvD41i80TM27unvw3TFRGljGGjc_f24P1cG39-7AZP1oXNObh1KsJeNwl8YaYxOS2e5znmbwmIhy_TvNUYiKl_govlB84uVcf6U7A2qhMT6C23TkyEeBZabeKhaQ4rUya8iZNx9F-ueyqldC5NGh37u0t5UWFgWNjknekg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad58d044a.mp4?token=FnlQp6GJOAblOxPCudmp9XDV73oUabhS9HBISQ9JWcxVG6MNRRpwtY4VJ6X6Dqnn-ZhUnBH3KFMqVBnrHST6a4iKCDcJf4m2LjAbOgIkk_cDdUH71KKC5qIIdVq6LEBnPjYmYwRGOawGfm_oqEjYCQ6AX1-cuJ7nbixSzmXS5pnB11vefvD41i80TM27unvw3TFRGljGGjc_f24P1cG39-7AZP1oXNObh1KsJeNwl8YaYxOS2e5znmbwmIhy_TvNUYiKl_govlB84uVcf6U7A2qhMT6C23TkyEeBZabeKhaQ4rUya8iZNx9F-ueyqldC5NGh37u0t5UWFgWNjknekg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
تو یه فروشگاه تکنولوژی تو روسیه، یه ربات بعد از اینکه مشتری هلش داد، شروع به دعوا با مشتری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71034" target="_blank">📅 09:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71033">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e73b2179fb.mp4?token=HQn_PHaA8UEfcMIeBQ8vcDNKlIVAHSsH92LjAhW5G73podqudP-4Gb5XE3cVq4eP-OIvI-0KDMige4vI_cAJf2oe9b1CMDWmdXoPCpVmFseDfzxU1rtuTsokVXbZVoV_Von2If1LPWkdgARUD2QA1nADlS9cn9a1CUAHPsoavg9YJgMF2c9Pmak2-GJclaaETNaXY1DAKDcAaTS_Em_OQPuPiYED94qQQxztNAOf8-bkn2pYOPYJ2lHVhXVbyPZOXRrQOPEILOEYz6bNm8-dM67M2Zqe6sXz0KUqdE7TTZ_LWwovhTW9CJVBbP9qXMYBEdQGI9tFdhN8mNGTlNYFVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e73b2179fb.mp4?token=HQn_PHaA8UEfcMIeBQ8vcDNKlIVAHSsH92LjAhW5G73podqudP-4Gb5XE3cVq4eP-OIvI-0KDMige4vI_cAJf2oe9b1CMDWmdXoPCpVmFseDfzxU1rtuTsokVXbZVoV_Von2If1LPWkdgARUD2QA1nADlS9cn9a1CUAHPsoavg9YJgMF2c9Pmak2-GJclaaETNaXY1DAKDcAaTS_Em_OQPuPiYED94qQQxztNAOf8-bkn2pYOPYJ2lHVhXVbyPZOXRrQOPEILOEYz6bNm8-dM67M2Zqe6sXz0KUqdE7TTZ_LWwovhTW9CJVBbP9qXMYBEdQGI9tFdhN8mNGTlNYFVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توضیح عباس حیدرزاده مداح درباره‌ی وضعیت مجتبی خامنه‌ای :
تولیت آستان قدس رضوی گفت که شب دفن رهبر؛ مجتبی خامنه ای ساعت ۱۲ شب اومد حرم برای دفن پدرش و تا ۷ صبح اونجا بوده.
وضعیت جسمانی ایشون هم عالیه، هم از لحاظ ظاهری و هم از لحاظ جسمی؛ حتی مسئولین هم پشت سر ایشون نماز خوندن.
همچنین ایشون نیم ساعت کنار قبر پدرش دو زانو نشسته بودن و گریه میکردن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71033" target="_blank">📅 09:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71032">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71032" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71032" target="_blank">📅 01:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71031">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrYFBIyj6MshT__ZXmWZqWqBO6cxH0TRWxx98l3OaoGUko7XTnwxn4oAt-WGy8Omd7No_HashpolWyOoYOfmY8lUugxQ9PsryBso2D1C9jr5tZuY061wgefkszURYPRWc0s3Wbo3q_ph8dZqwUI9ayEkCpmOMAcleEKvxmCzFkK6b0OOlEQ9z4hCgHqnCHDD_6IBvflSFYkBQVLcTMqZqJ4t1SlvYMGmkVIYncm2hxFybOsI9UyqmYLmUtLFFfT25r7dSBAQGZGTlm3QPy6TXeOvAE5belluu-afMY9RcyqznzbhZ1xMEM6_F47Qwjq3bs67_YV0jmxqk1j2q9VP7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71031" target="_blank">📅 01:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71030">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
⭕️
فوووووری/ همین الان با شروع مجدد جنگ دلار و ارز منفجر شد
😳
‼️
همین حالا چک کنید
👇
https://t.me/+S5Mn2k3LOf0wNjJk
https://t.me/+S5Mn2k3LOf0wNjJk
فوری برید ببینید
☝️
☝️
☝️</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71030" target="_blank">📅 00:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71029">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa78544f7d.mp4?token=ElQ2QFI_aC37xpEMpxFKCNFD3N7EX4acSDDdqvNlDslvvqPNuygWLeYRlAIhBBQsVj3dbWhakQFvyoJTBLQTJhZtVoFHta5gJXht0alOskw6Z1qRSMWRKzDxbmP22QwxhSSDYPPW3lw35XGHO8cHczgmwJVUa0gP4JWoLsaFofwgegvUo7SRw9dJfHrkddfXiB56HZBOHfJ5BmH1fRXW20pjQf98tR5rl4yDpeBtsUD2fp3Bd1YJzOKsjKZOSd8KjlwGDyZQgp-T0EGNLWcK7D0G0pcaFf41JM119LC1g4cMdsgWSeHLzRB0056fGkwz2fRZMidyNN7s54gKm6FCiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa78544f7d.mp4?token=ElQ2QFI_aC37xpEMpxFKCNFD3N7EX4acSDDdqvNlDslvvqPNuygWLeYRlAIhBBQsVj3dbWhakQFvyoJTBLQTJhZtVoFHta5gJXht0alOskw6Z1qRSMWRKzDxbmP22QwxhSSDYPPW3lw35XGHO8cHczgmwJVUa0gP4JWoLsaFofwgegvUo7SRw9dJfHrkddfXiB56HZBOHfJ5BmH1fRXW20pjQf98tR5rl4yDpeBtsUD2fp3Bd1YJzOKsjKZOSd8KjlwGDyZQgp-T0EGNLWcK7D0G0pcaFf41JM119LC1g4cMdsgWSeHLzRB0056fGkwz2fRZMidyNN7s54gKm6FCiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇹🇭
ناو آبراهام لینکلن تو پاتایا - تایلند پهلو گرفت و ملوانان و اعضای این ناو برای یه استراحت  کوتاه مدت پیاده شدن
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71029" target="_blank">📅 23:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71028">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14a1d4faa9.mp4?token=OZDzubA_-lp1_fo73IFIMqYOrO5QfYa6A7s8pKyJH_keOtk00HMHV_XMNfpoBLE5ZhOR2edkJbOzqL22Mt7ZvOIxLX5qVBrCkc-YH7z-Q7W8DJTRU3HnboHKymFeIX9zugdEsgF2Zjj4DtfnOWokoNuYtBhsmovy5lehTP5L0PVBkbYgUhrWjeakT3XdFHSppPQq1Jx37fM1EeYA5WhXxPZZ3zYI2gi3jDU7PonzaiHD755qm7H8f6JJA80PM6a3vVjLYP0B3OwNaxfKmCmM69t0w2crL2WcWNhQ84Lpm09EH5rxRDRueb1xrDCsAy-Ou6-GraiBweF46IuudqXLXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14a1d4faa9.mp4?token=OZDzubA_-lp1_fo73IFIMqYOrO5QfYa6A7s8pKyJH_keOtk00HMHV_XMNfpoBLE5ZhOR2edkJbOzqL22Mt7ZvOIxLX5qVBrCkc-YH7z-Q7W8DJTRU3HnboHKymFeIX9zugdEsgF2Zjj4DtfnOWokoNuYtBhsmovy5lehTP5L0PVBkbYgUhrWjeakT3XdFHSppPQq1Jx37fM1EeYA5WhXxPZZ3zYI2gi3jDU7PonzaiHD755qm7H8f6JJA80PM6a3vVjLYP0B3OwNaxfKmCmM69t0w2crL2WcWNhQ84Lpm09EH5rxRDRueb1xrDCsAy-Ou6-GraiBweF46IuudqXLXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان خطاب به پوتین :
قدرت‌های بزرگ صرفاً چون زور و قدرت دارن، حق ندارن بدون توجه به چارچوب‌ها و قوانین بین‌المللی به بقیه کشورها حمله کنن.
حمله‌ای که آمریکا علیه ایران انجام داد، نه مبنای قانونی داشت، نه مبنای علمی و نه حتی توجیه منطقی.
ملت ما با قدرت جلوشون ایستاد و اگه بخوان این مسیر رو ادامه بدن، بازم با قدرت مقابلشون می‌ایسته.
ما تو اون تفاهم‌نامه چیزی بیشتر از حقوق کشورمون نخواستیم و الان هم فقط دنبال همون حقوق هستیم.
ما همچنان به تفاهم‌نامه‌ای که امضا کردیم پایبندیم. اگه آمریکا هم به همون تفاهم‌نامه برگرده، ما هم طبق همون عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71028" target="_blank">📅 23:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71027">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/180c2bccea.mp4?token=g3J2-rCidCt4HiqufqLpzkGX9vjtVOIAZQ28VLqKSp3XFx8lXzrkCUfIfCOy_zNBSGpcMAtfyRupLs5e4guOFxRkL5SIQjSLX1eCbITQRwdpYSenspEKQEsgdMPMQtVVrp5pGBTCp9-GxgHywlizc5RiP6VfaBar_dY6xUvMnJyGFlAVSisamA1GbYrGEZz_8nXzaAFcOreOnxWg9a0t8Ud6ucVN8jM1XUdqGIMcXL7_24uSb-Vk4QPdDkAW0iMvp513AUCGCrCjurFNtBAR0TL09qTiyHaI5BDl6e_kGf_nqwbeupu12Nf9Y11EjdMQJnXlUASS4t0p9LOilKN_5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/180c2bccea.mp4?token=g3J2-rCidCt4HiqufqLpzkGX9vjtVOIAZQ28VLqKSp3XFx8lXzrkCUfIfCOy_zNBSGpcMAtfyRupLs5e4guOFxRkL5SIQjSLX1eCbITQRwdpYSenspEKQEsgdMPMQtVVrp5pGBTCp9-GxgHywlizc5RiP6VfaBar_dY6xUvMnJyGFlAVSisamA1GbYrGEZz_8nXzaAFcOreOnxWg9a0t8Ud6ucVN8jM1XUdqGIMcXL7_24uSb-Vk4QPdDkAW0iMvp513AUCGCrCjurFNtBAR0TL09qTiyHaI5BDl6e_kGf_nqwbeupu12Nf9Y11EjdMQJnXlUASS4t0p9LOilKN_5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره انتخابات:
من تحت تأثیر انتخابات نیستم. خودم نامزد انتخابات نیستم؛ حزب من در انتخابات حضور دارد.
به گمانم حزبم به این واقعیت احترام می‌گذارد که ما اجازه نمی‌دهیم ایران به سلاح هسته‌ای دست یابد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71027" target="_blank">📅 22:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71026">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53f1ce3ca7.mp4?token=A6gNDme_6isf9E2nK5GFVJfLtwlDMH2a-6U4z0htyJRlFtw5ekaIJzIEQZ24pwcn9h7o2mibewe39lFwONdXo-CKkrwYKx9m9njAZax1fD_E49I-ppT5tuJEPg3LHnkz3XoWAlAytXGncRG3T2Bv5oaZmkGCpnqQ6WXGoapO8sF-OXdnH-ZiEkB4p18EjMX-RXsRqcwiK6adcOYAUt58DDbDTbzfpDsWPLYTgToc38UKjMqohsgWkP33pU0ZCtdz5DhXhmDj03P7NiELizJQYbkh6lAWr9m9pM3sH03xM6BQGQwQjsSyougXVqALtb8QoEFUXR1uNRkkut5yFaQ1EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53f1ce3ca7.mp4?token=A6gNDme_6isf9E2nK5GFVJfLtwlDMH2a-6U4z0htyJRlFtw5ekaIJzIEQZ24pwcn9h7o2mibewe39lFwONdXo-CKkrwYKx9m9njAZax1fD_E49I-ppT5tuJEPg3LHnkz3XoWAlAytXGncRG3T2Bv5oaZmkGCpnqQ6WXGoapO8sF-OXdnH-ZiEkB4p18EjMX-RXsRqcwiK6adcOYAUt58DDbDTbzfpDsWPLYTgToc38UKjMqohsgWkP33pU0ZCtdz5DhXhmDj03P7NiELizJQYbkh6lAWr9m9pM3sH03xM6BQGQwQjsSyougXVqALtb8QoEFUXR1uNRkkut5yFaQ1EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
دیشب حمله بسیار سنگینی صورت گرفت و ما آماده‌ایم هر زمان که بخواهیم، حمله دیگری انجام دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71026" target="_blank">📅 22:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71025">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a230c24bdf.mp4?token=CmPaub4Co3UBaKvkHnZLFS9tZRBM0dTm4knpOpWj_bJm6ERFzbAQD9s_GJawgYPC04B2tvXoDpAl_V-awzGeuCUH_GVzOOC6ihWclRwoD-3oYlRh-MJifZbu7PvoaJ0AM_nhK1aAM5RO2HX4VGH5VNkDMF-mrss37pPNSMzjI-IA3viDs9PULPhwbfooo_lG0nkCNy1RdU8Ghtbg5boET5AQSi5MmbaMomiaJ084YdBKzq_scUge4MTlOLw_7SA506UMgVmDT9f3zaHJoPWgevVpTmTpCOZDCHhNUw5RA5WnjfI9kF-djYK1vfwegXWsGrO-iImYSJu3O5jYLHVOsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a230c24bdf.mp4?token=CmPaub4Co3UBaKvkHnZLFS9tZRBM0dTm4knpOpWj_bJm6ERFzbAQD9s_GJawgYPC04B2tvXoDpAl_V-awzGeuCUH_GVzOOC6ihWclRwoD-3oYlRh-MJifZbu7PvoaJ0AM_nhK1aAM5RO2HX4VGH5VNkDMF-mrss37pPNSMzjI-IA3viDs9PULPhwbfooo_lG0nkCNy1RdU8Ghtbg5boET5AQSi5MmbaMomiaJ084YdBKzq_scUge4MTlOLw_7SA506UMgVmDT9f3zaHJoPWgevVpTmTpCOZDCHhNUw5RA5WnjfI9kF-djYK1vfwegXWsGrO-iImYSJu3O5jYLHVOsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
یک ضربه کوچک بود، اما دیشب ضربه بسیار سختی به آن‌ها زدیم.
ما تمام تجهیزات جدیدی را که سعی داشتند در امتداد تنگه هرمز مستقر کنند، از بین بردیم؛ تجهیزاتی که برخی جنبه تدافعی و برخی جنبه تهاجمی داشتند.
آن‌ها تلاش می‌کردند موقعیت کشتی‌ها را رصد کنند — چون همان‌طور که می‌دانید، قادر به دیدن کشتی‌ها نیستند؛
ما تعداد زیادی از کشتی‌هایشان را نابود کرده‌ایم
آن‌ها نمی‌توانند کشتی‌ها را ببینند چون راداری در اختیار ندارند؛ چرا که ما رادارهایشان را منهدم کرده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71025" target="_blank">📅 22:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71024">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991fb05c67.mp4?token=Na9JbyvBTzqQ9MQnp2cfA8QcrJfr_Tpv3ygdMDjvlxYSu2SJT7J9EonFrTzd94swtHxrC-8OMUHLXICHWO3VYTW-8CxlYb7nbWs9irnlVcaNhDsYlN4V3UMIle7WgDco-XligAFBGsjb_5J2KieB1SiUgyJYZrTI2jI9_kyPu_tZ_Ond36BxAVxjtpdvHkC8jKnslRL5A_Z66kPoPXD9ctkafvitGZtj-KNJuovbaLUSi8UOscLJko-pbYFWNZjzxCl5pkQCTaZRnsOimav2449UCgUuDXP9Lil-rSIOpLnUSscw1Rh0vBMk3pJfJamsuQCFjaszbw4BPae4kZJV4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991fb05c67.mp4?token=Na9JbyvBTzqQ9MQnp2cfA8QcrJfr_Tpv3ygdMDjvlxYSu2SJT7J9EonFrTzd94swtHxrC-8OMUHLXICHWO3VYTW-8CxlYb7nbWs9irnlVcaNhDsYlN4V3UMIle7WgDco-XligAFBGsjb_5J2KieB1SiUgyJYZrTI2jI9_kyPu_tZ_Ond36BxAVxjtpdvHkC8jKnslRL5A_Z66kPoPXD9ctkafvitGZtj-KNJuovbaLUSi8UOscLJko-pbYFWNZjzxCl5pkQCTaZRnsOimav2449UCgUuDXP9Lil-rSIOpLnUSscw1Rh0vBMk3pJfJamsuQCFjaszbw4BPae4kZJV4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
ما هر کاری که آن‌ها انجام می‌دهند را می‌بینیم.
آن‌ها حتی نمی‌توانند به دستشویی بروند بدون اینکه ما متوجه شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71024" target="_blank">📅 21:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71023">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/504db2064f.mp4?token=aTrzgxxhxRsmZe52SoVQv8b9oZ5LlLKWplhey6dgjflMxFUcpW455XCXwUX0ELH9cb2dYpRzSZpzqMd6mPUhSkzUG-dhXw8l0JQR0NSNHjC7MOIgck-rUdYI0cra8tlXIgC1-C_1RRgVOA3Z_L0b9alTgZzMYnixu_RBNEuByXIA32VrZYuoVYZBQEtE1TlQx7aHUcDiEV0zpr4G0jBE_LrsPkmn-kcGxblHHBCRekuGjBcdUDBc3CWWL8QNhkxqJ1Zo2FqVuXUiqbgq9sJ_DzViQNpj4Uy3q76j043aosvJMmMfiAmMvPiUkB_-BlVLAv4EPsYt2nRd7mrYjrKKwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/504db2064f.mp4?token=aTrzgxxhxRsmZe52SoVQv8b9oZ5LlLKWplhey6dgjflMxFUcpW455XCXwUX0ELH9cb2dYpRzSZpzqMd6mPUhSkzUG-dhXw8l0JQR0NSNHjC7MOIgck-rUdYI0cra8tlXIgC1-C_1RRgVOA3Z_L0b9alTgZzMYnixu_RBNEuByXIA32VrZYuoVYZBQEtE1TlQx7aHUcDiEV0zpr4G0jBE_LrsPkmn-kcGxblHHBCRekuGjBcdUDBc3CWWL8QNhkxqJ1Zo2FqVuXUiqbgq9sJ_DzViQNpj4Uy3q76j043aosvJMmMfiAmMvPiUkB_-BlVLAv4EPsYt2nRd7mrYjrKKwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
بیشتر مردم نمی‌توانند به این شکل آدم‌های خودشان را بکشند.
بیشتر مردم سعی می‌کنند منطقی رفتار کنند، گفتگو می‌کنند و بعد شاید کار به سرنگونی بکشد.
اما در ایران، آن‌ها مردم را می‌کشند.
وقتی مردم برای اعتراض بیرون می‌آیند، آن‌ها را می‌کشند؛ درست وسط پیشانی‌شان شلیک می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71023" target="_blank">📅 21:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71022">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c319507bcf.mp4?token=S4OyeIMPksSHhJW3_z_K73DH441LgYjuSm0IHPMO1t68ClIrfJ2E-Lc9SGbe79-FtpRIzYgNz-yAYVsTb9s7EvyK2lm2-6nAE8Kbd3kMiBRACh2ZYOhoAzb1ALddfMDsjIznMy8gwUp-AZcAGlRxWcJEgc3lDLy5accywmLz7H1LNK5NbkrHDjrjpAPL175Y8KmsyG3zEOkbU2dFZInXpU_BXbdrv2LZgeJ4mRAOaHWC1YRMbcldXZYZT58wwm7t2YRclB9vxvdhFL9JW1U1GCxXjrf_XLew0gpz73onAPQVr6qE79AujmmomQuQg0Auxd104M6ToB2y_Po5VC1Tmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c319507bcf.mp4?token=S4OyeIMPksSHhJW3_z_K73DH441LgYjuSm0IHPMO1t68ClIrfJ2E-Lc9SGbe79-FtpRIzYgNz-yAYVsTb9s7EvyK2lm2-6nAE8Kbd3kMiBRACh2ZYOhoAzb1ALddfMDsjIznMy8gwUp-AZcAGlRxWcJEgc3lDLy5accywmLz7H1LNK5NbkrHDjrjpAPL175Y8KmsyG3zEOkbU2dFZInXpU_BXbdrv2LZgeJ4mRAOaHWC1YRMbcldXZYZT58wwm7t2YRclB9vxvdhFL9JW1U1GCxXjrf_XLew0gpz73onAPQVr6qE79AujmmomQuQg0Auxd104M6ToB2y_Po5VC1Tmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
تا سه ماه پیش، پنجاه‌ودو هزار نفر از معترضان کشته شده بودند؛ می‌توانید چنین چیزی را تصور کنید؟
و حالا شنیده‌ام که احتمالاً بیست تا بیست‌وپنج هزار نفر دیگر هم به این آمار اضافه شده است؛
یعنی شمار معترضان کشته‌شده به حدود شصت‌وپنج هزار نفر رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71022" target="_blank">📅 21:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71021">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78e478b4b0.mp4?token=MYQkGIlYlr9lGEmCr12XCGaAHWpgDD1OGJidVakgJJ42rfkPlUwBNY8BAHB4Bj8hBk5O2e2isj3i6iInhwbTTCWsveoTQXvVrDjjjGQtaS_ZMJQntF-i-Zn453m_qatx3ZrfP2sakXvfuHN_gQSj7OPy2HuhXDzXOOKBFDR6hRMbuS-x0bLEfhW6sbyFCPJx09m6WCWM9T9vEcjzkXAWO4n9s2d30bCVKr-kU3IiEYEnD9qvw5iWyM7fsZTbJA8qU-ICdvAFFTM1abiwql3IKB8GAwk5n47nh94EbLZGS4w7ejBZ4LE0tEhhdyPhbY-6yA_46Mc_VYN1qeRVHfOxOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78e478b4b0.mp4?token=MYQkGIlYlr9lGEmCr12XCGaAHWpgDD1OGJidVakgJJ42rfkPlUwBNY8BAHB4Bj8hBk5O2e2isj3i6iInhwbTTCWsveoTQXvVrDjjjGQtaS_ZMJQntF-i-Zn453m_qatx3ZrfP2sakXvfuHN_gQSj7OPy2HuhXDzXOOKBFDR6hRMbuS-x0bLEfhW6sbyFCPJx09m6WCWM9T9vEcjzkXAWO4n9s2d30bCVKr-kU3IiEYEnD9qvw5iWyM7fsZTbJA8qU-ICdvAFFTM1abiwql3IKB8GAwk5n47nh94EbLZGS4w7ejBZ4LE0tEhhdyPhbY-6yA_46Mc_VYN1qeRVHfOxOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما امروز در «تروث سوشال» (Truth Social) نوشتید: «مردم ایران چه زمانی قرار است قیام کنند و بجنگند؟» خب... اگر... اگر این چیزی است که شما می‌خواهید، آیا سیا (CIA) را برای مسلح کردن ایرانی‌ها اعزام خواهید کرد؟
⏺
🇺🇸
ترامپ:
خب، پیتر، من نمی‌خواهم چنین چیزی به شما بگویم. خیلی دوست دارم این را به شما بگویم، اما... اما گفتنش مناسب نیست.
ولی... منظورم این است که من وضعیت دشوار آن‌ها را درک می‌کنم؛ آن‌ها هدف شلیک گلوله قرار می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71021" target="_blank">📅 21:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71020">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):   گزارش تأییدشده‌ای مبنی بر درگیری یک نفتکش در یک حادثه امنیتی دریافت کرده که منجر به دو مورد تلفات انسانی شده است.   @News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71020" target="_blank">📅 21:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71019">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8edb01b99f.mp4?token=KL6uV-k4foLmRz91ykRL0ZFCPT1-hDZt2eQl9cg4FWoLkwYGh3MplH5sFOup_xkHXdlBHs7mgHyf__6lIXpuXmy9wRB42GKCTf9ZGFg5_KbfrSR-8npknTZWxy9d9xrHkGM_kkjcLB0Ly6jU47yZvr6M1nWpV_4wQ9qK-qYViiy-iYqKXhWRTIqYgV4OWYZmOmXcGSgXikmsmoD2rgy2iz9EFbjHo4NKTRvESXWcvIlZNF7XYEuTBGIhaLe0c9Pi7Je2KAIzcWM5RIR30EW8IQvcUKT1R4o2zQV90z48IzsO4n9dtzVMQt1ZaDIU2ZzrR4e6ghoSRFDSRHEI2UTOqnVKnOprXet-AtPNeNkpzfWZ5ZhpykmP0XIrL5eqXFlYQHQIxzwjnax3Dyb05AUOWHUpu78mGNtTSR_EmxKpYfbWFEVYV_f2dHVjBIbiyoYNFysQqDV1McH-5tLOdk5pSm_689EOXmjzKJlIX28MaHbQDYZzoRhDeRPsRYffjxfT_YpgXMGEtLyKhsBnrAE1vVH3mxLOgVn55-s_4xw52xZa-5QskXmF27gZYlBvWHQORQA6JGoA27yMiW7Onlq2NNkbT9lGGGyI8HOeBoVBfKoAXOZ6h5AMVAwGrVRHFtmwUeOXQ-QlyMLC_yzIcyiLs_-3HotEgJkOGhaM02XWprM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8edb01b99f.mp4?token=KL6uV-k4foLmRz91ykRL0ZFCPT1-hDZt2eQl9cg4FWoLkwYGh3MplH5sFOup_xkHXdlBHs7mgHyf__6lIXpuXmy9wRB42GKCTf9ZGFg5_KbfrSR-8npknTZWxy9d9xrHkGM_kkjcLB0Ly6jU47yZvr6M1nWpV_4wQ9qK-qYViiy-iYqKXhWRTIqYgV4OWYZmOmXcGSgXikmsmoD2rgy2iz9EFbjHo4NKTRvESXWcvIlZNF7XYEuTBGIhaLe0c9Pi7Je2KAIzcWM5RIR30EW8IQvcUKT1R4o2zQV90z48IzsO4n9dtzVMQt1ZaDIU2ZzrR4e6ghoSRFDSRHEI2UTOqnVKnOprXet-AtPNeNkpzfWZ5ZhpykmP0XIrL5eqXFlYQHQIxzwjnax3Dyb05AUOWHUpu78mGNtTSR_EmxKpYfbWFEVYV_f2dHVjBIbiyoYNFysQqDV1McH-5tLOdk5pSm_689EOXmjzKJlIX28MaHbQDYZzoRhDeRPsRYffjxfT_YpgXMGEtLyKhsBnrAE1vVH3mxLOgVn55-s_4xw52xZa-5QskXmF27gZYlBvWHQORQA6JGoA27yMiW7Onlq2NNkbT9lGGGyI8HOeBoVBfKoAXOZ6h5AMVAwGrVRHFtmwUeOXQ-QlyMLC_yzIcyiLs_-3HotEgJkOGhaM02XWprM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
#فوری
؛نتانیاهو درباره ایران:ما رژیم ایران را سرنگون خواهیم کرد.
ما این رژیم را شکست خواهیم داد.
🎙
مجری؛
«شکست» چه معنایی دارد؟ آیا سقوط خواهد کرد؟
🇮🇱
نتانیاهو:
سقوط خواهد کرد. ما آن را سرنگون خواهیم کرد. این رژیم به هر حال در آستانه فروپاشی است.
🎙
مجری:
آیا رئیس موساد، رون گوفمن، برای سرنگونی رژیم ایران تلاش می‌کند؟
🇮🇱
نتانیاهو:
تمام نهادهای ما، تحت هدایت من، برای سرنگونی این رژیم و شکست دادن آن تلاش می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71019" target="_blank">📅 20:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71018">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5723b906.mp4?token=OM1gw-aa84bQcDDPG_S0s5cwWVMitkosF67arMccQSv_FyQx5tx2HS6_tcigcPddG4wYnN2HpIV3K4CAL7Sq_2tRgqWi0HsUeN0MslHxCvT_AwJwN5602WIdQESU7peFp74SaiDhnyWlXV4Dw1YM9SYh8DpGorNBFNItuOlTFR7_F2bOtKUp7Z-yhSmI0Rwgq7-M-SGRNzUd7-lAfoofWye3i6ebh2_W4m6VGr9gM66PbkWk7urXol3EfLyxUNpgsYjb19kVHYuGQ6AJfNMhF4VNc9bOL2DV8JDt25aO1xrn2gZbW-LwSPr-1ZqmR2R6j0PehK2Ri7J6GsNgfNbNXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5723b906.mp4?token=OM1gw-aa84bQcDDPG_S0s5cwWVMitkosF67arMccQSv_FyQx5tx2HS6_tcigcPddG4wYnN2HpIV3K4CAL7Sq_2tRgqWi0HsUeN0MslHxCvT_AwJwN5602WIdQESU7peFp74SaiDhnyWlXV4Dw1YM9SYh8DpGorNBFNItuOlTFR7_F2bOtKUp7Z-yhSmI0Rwgq7-M-SGRNzUd7-lAfoofWye3i6ebh2_W4m6VGr9gM66PbkWk7urXol3EfLyxUNpgsYjb19kVHYuGQ6AJfNMhF4VNc9bOL2DV8JDt25aO1xrn2gZbW-LwSPr-1ZqmR2R6j0PehK2Ri7J6GsNgfNbNXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از دیدار محسن نامجو با مجتبی خامنه‌ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71018" target="_blank">📅 20:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71013">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5fMGAXuaXGaC4m5gyoouDGIpcDGhaSQW1MBkRIA22pBz-K2lZjJHjP-g3FW3fHzbULrY4v3flI05N-dFxujZz3tjohuFbqQTD5E5slT4rKl9xd7e_kLCp6ErjF9cYf5m4dDd-fLt4KLmLWc_xzjfENcYQgVSXJwyABWpQJgQiuOMKLS-o67ru0lLC8Wro9inpjwb0F0BmGcb2DibqTO4IFNXG9z3Rq-lIpj9GOLfB192hco3aVJA19MVW0EB_Q0LXyM7QxNh2dEBO1utjIXIb6h1qGh6QE58aMxAEhCVnfbNxEuALOSkGoQ25Dc3VVULwEQuE0u32FOSEEEgsbfMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDQc7T_0bOY3oinUIIRDSis4McC7mSMWbxC6G6Dd-dDxSCvLC4UB-l2QwO8KK_2INGVM7Eq8OZNzCV-0y8OFWm5ozL5u7SJD1k6qgO_S1RZ19V7I8TU5KM8HnElgmMNrRoBlY9cvDCfA0RDwDE1_30y3dkJWCML863apjBgiry8i_QW7KSspWL22cszI6k-5X2Bx1eLWwU86jW3rHVLBa57Wc7f9UzUAX9mGwBZTVaGdw_MzdsccxUGKYFK2xXEfTXSQbTn5oDaZ_qMRtyHB-mb0dXNGUeGllz48IwTJA2YwAgyT9kLLPBEgsAIHI3ZEcaDMALtJk0n3e7sRjbhouw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21e8023466.mp4?token=I7TSvjg2gvIfhTrpVVWTtiajbtsA0GkJtTp4ntbfNGd0uuesQlLJ5ytvr_RwGlbICP1ovSIM17gc5n3omLlUg7MwsVXJK0RzDoyhpjGe1GUl-jJkZQvWosL9RxVGz6fYfHwFEM-q-LIETnpK6ZRULjdtGGqGOfazfcKgQI-J4bu4t_K3Ua7HGPI48FUWxJLkbImFhMKSBPch3X2nCacm42JBakh2PvR_5ABU4kCGcZPF6DjsyRS_2xQtwav3ESyRwUSEMmR7QLdMne-CGYCQwGQaOdylzE5-4l4VEkekhnNqeFZvy468g-oNIjHu53wkbrZ-37rfx3yJKmINTJaH5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21e8023466.mp4?token=I7TSvjg2gvIfhTrpVVWTtiajbtsA0GkJtTp4ntbfNGd0uuesQlLJ5ytvr_RwGlbICP1ovSIM17gc5n3omLlUg7MwsVXJK0RzDoyhpjGe1GUl-jJkZQvWosL9RxVGz6fYfHwFEM-q-LIETnpK6ZRULjdtGGqGOfazfcKgQI-J4bu4t_K3Ua7HGPI48FUWxJLkbImFhMKSBPch3X2nCacm42JBakh2PvR_5ABU4kCGcZPF6DjsyRS_2xQtwav3ESyRwUSEMmR7QLdMne-CGYCQwGQaOdylzE5-4l4VEkekhnNqeFZvy468g-oNIjHu53wkbrZ-37rfx3yJKmINTJaH5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
حملات جنگنده های اسرائیلی به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71013" target="_blank">📅 20:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71012">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/600c9063c3.mp4?token=fkknasdlyaj71SKNQ6_a0BnxKCh_kOWVp6rN7_E1Ns9gQx1DkDTYSYMKt8AEVaz90RyLStTF4gA3PARcMOQe943rF5x5wKHodWjXLC6Xn-nqQ_kl2eX-_IKkkNy4ZnkLqn4HF2kI_S7YHuOGNGzDKYZbmfAt87-N5NLGuN1G4lzSHGScnW8FYeTa0650PkssO3motT-XsThqTx2Nwaw44tFJ5RuEi3ZabQ9s5cVlSRwnZvyFsCS26WQUjsJbETDgXoQZaQmLTuqMdDmMOcOWUGVgAI4hghj1rxXZ8EuaZyY8uIHuTFMcw5gEoUiFV3EXAqf9M7_AxtT0BYo9nF2zow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/600c9063c3.mp4?token=fkknasdlyaj71SKNQ6_a0BnxKCh_kOWVp6rN7_E1Ns9gQx1DkDTYSYMKt8AEVaz90RyLStTF4gA3PARcMOQe943rF5x5wKHodWjXLC6Xn-nqQ_kl2eX-_IKkkNy4ZnkLqn4HF2kI_S7YHuOGNGzDKYZbmfAt87-N5NLGuN1G4lzSHGScnW8FYeTa0650PkssO3motT-XsThqTx2Nwaw44tFJ5RuEi3ZabQ9s5cVlSRwnZvyFsCS26WQUjsJbETDgXoQZaQmLTuqMdDmMOcOWUGVgAI4hghj1rxXZ8EuaZyY8uIHuTFMcw5gEoUiFV3EXAqf9M7_AxtT0BYo9nF2zow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مردی در نیویورک آمریکا پس از برخورد مستقیم صاعقه به پایش جان سالم به در برد
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71012" target="_blank">📅 19:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71011">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuiNmWMs1c6Q0FTLPyNML_qWy9G5R0IX5JEnzGOumXy76CQPTE9-wIAZdpJ5vT0ZEMHUSX_P97K557qMaBw7_jZFCdJ-dgEvaip7sCpKZmUe_L5d1mmeLLf86Yt3J5CNePd1lYpbUFg_1MO15jhSIgJajIR5_1r8mYeIjdHBRm4o3kQEmNCo1Kd-lpTpsIorDl3s1BzaF9JLpAUMTddICsl-ge03tdxHy6cpvru0jkcxDCO7x3WV6qG5DQ8kS3LkZ3hcSD0V3z2GpLgRe-rrTSxFuLvzLG4_JyqvFdBG6NYa_YITv1w076z-t3X-fbQ7Wfjr0_w_PU1nU8P53rdUWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ در تروث سوشال:
حالا که تنگه هرمز تحت کنترل ایالات متحده است، آیا باید نام آن را به «تنگه ترامپ» تغییر دهیم؟ این تنگه هم درست مثل خودِ آمریکا، «داغ‌تر» از هر زمان دیگری خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71011" target="_blank">📅 18:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71010">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اسپویل:
سپاه دوباره موشک می‌زنه و ترامپ هیچ گوهی نمی‌خوره
#hjAly‌</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71010" target="_blank">📅 18:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71009">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f635b0ff.mp4?token=T9itzoYSOGkyoRsccA_1vRumwIP3SUHCrKpQYBGBIjWkLtVwL5bf9e3_t4NBSCV0MyNb0f2_QpGUzEPImCNJnMNu0eK9IgU5ltUQwgvW4VeFucJY1Ya7LlTZkrTQayKGesZBX4mUbTdOMsVm_-3MNEQdEplYvM5GsYSsqjTsHGdXKBMq7Zkw-Eo8h2-lPDH1rzjLTBG9DU4l0-lXhsP81OhOG0znxxQLPjmVpaOyHu-RIns52E-lrDB8JeV2Gr8mw1UZr-JKXXnLPRTNQBNavG2viScrEYstij-CPEGkRI1XZE14Jej_ubzQG5k4eFAgrSSnvEEsyl5MonwX-AmAEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f635b0ff.mp4?token=T9itzoYSOGkyoRsccA_1vRumwIP3SUHCrKpQYBGBIjWkLtVwL5bf9e3_t4NBSCV0MyNb0f2_QpGUzEPImCNJnMNu0eK9IgU5ltUQwgvW4VeFucJY1Ya7LlTZkrTQayKGesZBX4mUbTdOMsVm_-3MNEQdEplYvM5GsYSsqjTsHGdXKBMq7Zkw-Eo8h2-lPDH1rzjLTBG9DU4l0-lXhsP81OhOG0znxxQLPjmVpaOyHu-RIns52E-lrDB8JeV2Gr8mw1UZr-JKXXnLPRTNQBNavG2viScrEYstij-CPEGkRI1XZE14Jej_ubzQG5k4eFAgrSSnvEEsyl5MonwX-AmAEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ما اکنون کنترل تنگه هرمز را در دست داریم. ما آن را کنترل می‌کنیم.
دیشب ۲۸ قایق و کشتی را از کار انداختیم. ما کنترل آن را در اختیار داریم، آن‌ها هیچ‌چیز به دست نمی‌آورند و ما آن کشتی‌ها را نابود کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71009" target="_blank">📅 18:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71008">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/116dfeb2e5.mp4?token=BRvt73bzbI_bMJd_4DxOMhjxjPFj8ErBUPwBzxjBndzHgeSgE64ohTISnOjhWj5mEX7wEuOCEf8M5bOu2sz6Sxia-jFHX-UQZAbC6cYKl1zfoFVzEgxDP63xZHC2vfvPUOBut0VZIAq4ohkfVctINMuoXo4Z699P-0shZryuGJKWaWS2XkOt_mQ8kI-ApPd3IeMl3hy9qi5gcgrClOGEy10N-M9ZGoPzBb2ov9eBgpm5EETSfGWmxAAvhZmvLFMSW2EPmjXc08t859sBznawkE-jRxZNgA-hDzwkNXvm609IcdmyhP4JAx9hQ4hy-NtMebMcD1jR5wXZNcw-jOydUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/116dfeb2e5.mp4?token=BRvt73bzbI_bMJd_4DxOMhjxjPFj8ErBUPwBzxjBndzHgeSgE64ohTISnOjhWj5mEX7wEuOCEf8M5bOu2sz6Sxia-jFHX-UQZAbC6cYKl1zfoFVzEgxDP63xZHC2vfvPUOBut0VZIAq4ohkfVctINMuoXo4Z699P-0shZryuGJKWaWS2XkOt_mQ8kI-ApPd3IeMl3hy9qi5gcgrClOGEy10N-M9ZGoPzBb2ov9eBgpm5EETSfGWmxAAvhZmvLFMSW2EPmjXc08t859sBznawkE-jRxZNgA-hDzwkNXvm609IcdmyhP4JAx9hQ4hy-NtMebMcD1jR5wXZNcw-jOydUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
🇧🇭
لحظه اصابت پهپاد شاهد-۱۳۶  به مقر ناوگان پنجم نیروی دریایی آمریکا در منامه، بحرین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71008" target="_blank">📅 18:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71007">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIy106xZdQ8qoQEHDeuDA1ZNZFDxYya9-ffeJBRfi5TCmMhg40Wstnw8mE1hdFvZikDFkSXlmwr77JlVybwWObL-3n132zifN6Y6E49u42F9M0cQIQZ8-ZnseqNQBxoGMq_LCp1ItcsJJzDsPhH4JHp_tmVTb1T4zA45OD7OznOyBekmHVhAE6VVGeWcg94rE5EG3MVfa3SMvY7omTXkpbKZnc06IB2ngEhuSYgNNhSaVExOiGHlNx8s4LHx03gsY6jE19igdHYs9ahFu---5vDOUD4MzlirHUFvwJJwLBtbI7-Rt6mKzTloIv9Hx0eOtFQ-unHvEIfoz_9nsW33tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه:
ایالات متحده به هدف قرار دادن ایران به دلیل حملات به کشتی‌ها ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71007" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71006">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71006" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71006" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71005">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcjYRe08isjGYdo6dhgWaPVTSV5X-AEHDaGvaETmX_6bL6bpV1OxeauQSH3XLZ3knvvsWDoG9Mpqe06--IZ_dLK-5tBY0lhWdhrmCSNStWJUwREuEv_PiRB-HWluGAW4jjqLPf1NHKWxT7O4Zrnvf9pImZK2s-raBU6mQ2H9rt111FmrASlgeCTUwnNNoux9f9Kp7Upsn6r3w0UJGA3LvezmnOnQONu5v_vlIpzQV2LparDBkUVU1BzS_x81qzVBpnAsSPt_EnRx278H3GZCsn9Lm3YDT7vX_hQo4ov-GC_dl7ZR9j5fpIXNxBTjTh9oWqpz6Uo_RDrSD79PoMJJOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
استقلال
🆚
پرسپولیس
⚽️
پیش‌بینی دربی رو در
TrexBet
از دست نده!
📉
نگاهی به 5 دربی اخیر:
2 برد پرسپولیس | 0 برد استقلال | 3 مساوی
4 گل پرسپولیس | 2 گل استقلال
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71005" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71004">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26734edca1.mp4?token=b5vvpoKA5mOcFVLrc3sXRdYlM3TEXM4tTpRJYJVR_EGS13jONuoZoNVl_TR8FFCyKzShhPYllGy8v3y6HWcJYYKrcsRUMiHKm-DCZoyuMZZJrzLoCOFH4_13wcFPnM1s7PC2OaMdcn5el5VxTG1Rao9hYIvk7uwuKDhp1F4JRcoCfo5ygjLtH4HD2GNxu8i9ndII-rwZdr10R9FaEYV8fpA8-UuSxKGzBSylj0GI7ix86vM_4w3mcRMJxzC_ttA_j-WEzzoD9BWBWr5oGI-5eAdLHrXJWYhqSV05S018Uctg9byddYsSiy5riYJA2WgXsjzKbv-S1v0NYkvzEyEZPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26734edca1.mp4?token=b5vvpoKA5mOcFVLrc3sXRdYlM3TEXM4tTpRJYJVR_EGS13jONuoZoNVl_TR8FFCyKzShhPYllGy8v3y6HWcJYYKrcsRUMiHKm-DCZoyuMZZJrzLoCOFH4_13wcFPnM1s7PC2OaMdcn5el5VxTG1Rao9hYIvk7uwuKDhp1F4JRcoCfo5ygjLtH4HD2GNxu8i9ndII-rwZdr10R9FaEYV8fpA8-UuSxKGzBSylj0GI7ix86vM_4w3mcRMJxzC_ttA_j-WEzzoD9BWBWr5oGI-5eAdLHrXJWYhqSV05S018Uctg9byddYsSiy5riYJA2WgXsjzKbv-S1v0NYkvzEyEZPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
📰
اینترنشنال:
⁉️
🇺🇸
🇮🇱
از شهروندان پرسیدیم پاسخ شما به پرسش ترامپ درباره زمان قیام مردم ایران چیست؟
یک شهروند با ارسال پیام صوتی به ایران‌اینترنشنال خطاب به دونالد ترامپ می‌گوید: «چه تضمینی وجود دارد که ما بیرون بیاییم و تو بعدش مذاکره نکنی؟ ترامپ، کار را به نتانیاهو بسپار که او بلد است.»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71004" target="_blank">📅 18:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71003">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4349c8ad3.mp4?token=fnqFfPT4IRkTpUVYZOZuKbiMQ2sTfIzRpoJVS_qFPF0ktBipbvOd-GUIReiYa_NfOcXgeo6Oz3cuDw1w3QuCV-d_KjRiURrTAASSHNUOvbAmzpwL-28aJ_v7zw4nhUPwzmV9H3fQYRGsi0XozmsCsLCd8pqmNdQjBuVfgeJovQyrxDJhdUcAik2PLeYwGNzOh7iwt7cIxB31sMNlf2HVGJTpdUy14lO5o4JsNHaog-cYDOPhxknMA0oL23pfi7_rLmASVFDJd8FvDCrKbgETG5qMg2eqeHiqdvgP3D-_Nk0Iz9suIlcxgwqP-u3ICuNBgHkPrqlS2IZ4gywNETTPTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4349c8ad3.mp4?token=fnqFfPT4IRkTpUVYZOZuKbiMQ2sTfIzRpoJVS_qFPF0ktBipbvOd-GUIReiYa_NfOcXgeo6Oz3cuDw1w3QuCV-d_KjRiURrTAASSHNUOvbAmzpwL-28aJ_v7zw4nhUPwzmV9H3fQYRGsi0XozmsCsLCd8pqmNdQjBuVfgeJovQyrxDJhdUcAik2PLeYwGNzOh7iwt7cIxB31sMNlf2HVGJTpdUy14lO5o4JsNHaog-cYDOPhxknMA0oL23pfi7_rLmASVFDJd8FvDCrKbgETG5qMg2eqeHiqdvgP3D-_Nk0Iz9suIlcxgwqP-u3ICuNBgHkPrqlS2IZ4gywNETTPTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
فردوسی پور:تاج و دوستاش نزدیک ۲۰ میلیارد از پول بیت المال رو گذاشتن تو جیبشون.
چند وقت پیش تیم ملی جوانان ایران واسه برگزاری یه اردو قبل بازی‌های آسیایی، به ترکیه سفر می‌کنه.
تو آنکارا، هزینه هتل‌شون طبق سند خودِ فدراسیون، 116,160 یورو شده.
بعد برنامه ۳۶۰ زنگ زده به همون هتل گفتن که قیمت‌ها اصلا این نیست و انگار مسئولین فدراسیون قیمت‌ها رو الکی بالا بردن! و هزینه ای که کردن چیزی حدود ۳۶ هزار یورو بوده.
خلاصه تاج شیرین نزدیک ۷۰ هزار یورو کرده تو جیب خودش و دوستاش
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71003" target="_blank">📅 17:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71002">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1896637f6.mp4?token=th0RVtSbj02WHBh6PLyfSny3tUvH8_ofKmMOCFLgm5ZXw1itcPh1jPX8hkWt2bI8OzqXOz4NorIzSQrejdb2ocl65xzB5D7vXgPR0RVM3J6iKxwOIOkXNlwTkwIsX5je3CaWwdYymmNcoLK1YMtkN889FpSCsMG8e1-nCeZUeUUX3ED-8bixr45l42M0HBYp1-XLq9yw9eKxD-9TLCOqeabKV10NisIsWA0wOb0RR2Hox9Mv2J6BXjstFPwaNnDrUtWOla7aCW27Fbup5CG9EHEXgeUE5uOZw7E6t1fTM5jImqtbaozjvhNBSPpkh4OMCmKuGVh5zK2dDjdagE_BLiPKKZ0Un-k3V9utbUnuOxlGkL7aWe6-B7zfRWI89v_OoysEuY9x9YVuizxPVdsStTUtly8gvwJ35nrUoD2gr3F0EAJ1p5HJ3asc9crc4IJSrovGUPkcjX1GukHveMtY157Zec25AI7VPQhL_aPJJz9yi7XlZRgFL4-qjfyr2oS81k569Dekvx-YccYr1wROkhnszdfaGGeH6OlEsslBLgEDc1maAKLYeHRNwz3fJowsVn29VpnZcBBWHUXtbBaWF6xdaP0Lulam1ttkovp5fvFP7XCnTnMNIRxkM6QRuTiZkWAlQ8kRy_kRvpb-otgRFZC9RET33KNDV1IgcXd2cYo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1896637f6.mp4?token=th0RVtSbj02WHBh6PLyfSny3tUvH8_ofKmMOCFLgm5ZXw1itcPh1jPX8hkWt2bI8OzqXOz4NorIzSQrejdb2ocl65xzB5D7vXgPR0RVM3J6iKxwOIOkXNlwTkwIsX5je3CaWwdYymmNcoLK1YMtkN889FpSCsMG8e1-nCeZUeUUX3ED-8bixr45l42M0HBYp1-XLq9yw9eKxD-9TLCOqeabKV10NisIsWA0wOb0RR2Hox9Mv2J6BXjstFPwaNnDrUtWOla7aCW27Fbup5CG9EHEXgeUE5uOZw7E6t1fTM5jImqtbaozjvhNBSPpkh4OMCmKuGVh5zK2dDjdagE_BLiPKKZ0Un-k3V9utbUnuOxlGkL7aWe6-B7zfRWI89v_OoysEuY9x9YVuizxPVdsStTUtly8gvwJ35nrUoD2gr3F0EAJ1p5HJ3asc9crc4IJSrovGUPkcjX1GukHveMtY157Zec25AI7VPQhL_aPJJz9yi7XlZRgFL4-qjfyr2oS81k569Dekvx-YccYr1wROkhnszdfaGGeH6OlEsslBLgEDc1maAKLYeHRNwz3fJowsVn29VpnZcBBWHUXtbBaWF6xdaP0Lulam1ttkovp5fvFP7XCnTnMNIRxkM6QRuTiZkWAlQ8kRy_kRvpb-otgRFZC9RET33KNDV1IgcXd2cYo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طراح ارشد موتور (بمب‌افکنB1-Lancer) متولد سیرجانه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71002" target="_blank">📅 17:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71001">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618f407212.mp4?token=JH-ejVwPB1NzygKiXLKhx0b5X2PkfwRj3rGKwP7J9hHxFQbnrcY5IE3L0WSptPR644nkFYJA_-QwvoNZUiZvr1lCiEJOgK10dAg4ZtSgmiH9puM3CDABzmzosvrt7mk7MfCX5Zsqg92BcX5a_Od0qDVYDPRi1pOuUftswqEICdcbTUcuKY-w_EonidHdDhYaQu-ceK-QcaWtcsoPsVc8kc0xNh6sSSSSVCJsPfAjCgLfQKgUNdZwnYBfTznrSe2U6RoLhpRz6fJtBd8lZ_Aa-VH6lbgGmX6a3tQFIgFnKzT2J-LnHTasnaMijeFziwPfz_85Foi7A5jWRawLDjJ-wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618f407212.mp4?token=JH-ejVwPB1NzygKiXLKhx0b5X2PkfwRj3rGKwP7J9hHxFQbnrcY5IE3L0WSptPR644nkFYJA_-QwvoNZUiZvr1lCiEJOgK10dAg4ZtSgmiH9puM3CDABzmzosvrt7mk7MfCX5Zsqg92BcX5a_Od0qDVYDPRi1pOuUftswqEICdcbTUcuKY-w_EonidHdDhYaQu-ceK-QcaWtcsoPsVc8kc0xNh6sSSSSVCJsPfAjCgLfQKgUNdZwnYBfTznrSe2U6RoLhpRz6fJtBd8lZ_Aa-VH6lbgGmX6a3tQFIgFnKzT2J-LnHTasnaMijeFziwPfz_85Foi7A5jWRawLDjJ-wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بررسی قیمت چند داروی پرمصرف از شهریور ۱۴۰۴ تا شهریور ۱۴۰۵:
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71001" target="_blank">📅 16:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71000">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df28769cb3.mp4?token=kqmuqpYLdSR2n-O20o1DcJOAy3qCKCnN4Ea7oGQsjpLMtWnb-ksNpbR6QhW_bGFlaJFCoQamJkV1BATnyjfik-9qigzCFl61t3cwz2cuZxrob1dgWf0gVXpy5pKMbp9-MX6p9GnzqG65ahomjhdl4JKJU-2sROm_Rm4kWN1D82nnMur6_eM3Ur6FB7sDlzVEe_PB-lzagsqc0rISubhctsW7WuYRtJo9dTRuMN_fu1-0gxq74oNzBRjfEhNnJ8GYWkmgkXu03ZQAjWSvZFXIwd9CSRfGcAqaRPVYjBFRMQ0CHV34TtmZTlV_gvudB-873hflfZNrID8YzyeKB2nEfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df28769cb3.mp4?token=kqmuqpYLdSR2n-O20o1DcJOAy3qCKCnN4Ea7oGQsjpLMtWnb-ksNpbR6QhW_bGFlaJFCoQamJkV1BATnyjfik-9qigzCFl61t3cwz2cuZxrob1dgWf0gVXpy5pKMbp9-MX6p9GnzqG65ahomjhdl4JKJU-2sROm_Rm4kWN1D82nnMur6_eM3Ur6FB7sDlzVEe_PB-lzagsqc0rISubhctsW7WuYRtJo9dTRuMN_fu1-0gxq74oNzBRjfEhNnJ8GYWkmgkXu03ZQAjWSvZFXIwd9CSRfGcAqaRPVYjBFRMQ0CHV34TtmZTlV_gvudB-873hflfZNrID8YzyeKB2nEfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرت زدن وزیر ورزش و معاون وزیر خارجه و تمیز کردن دندان توسط وزیر خارجه هنگام سخنرانی پزشکیان
😃
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71000" target="_blank">📅 15:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70999">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2M4HBHm9hyU_QbOK-HcSLuve9PaqOnoBzxViiy8hFzdB_LwvlMrimyuzWc4yViPM7gr6Riwvuli8A0iEhyz7drV982SAwUl_q3YZtAX3d1C9VnvjaccS0kGlGt7lr7MGGvC3jJ1Yqg10ZS6kguivcoJIIBvJ9EEr2A6fMbh97tJtzWiB-PEfhtUFeNTWO73iaYub6pWj9GvBiVgHfvy5sUlKCBOcjWWOwgkqdiHEHEY1rOjbK0B_xay2o5YpgFeUSIzE_TaGuyC7zTk5OuwtYrdVnm82Eyse2paU_hDdCzcOqSopw5n3ImjrcJ1rVJucjbA1maWS8q8W-QQnVLzRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارش تأییدشده‌ای مبنی بر درگیری یک نفتکش در یک حادثه امنیتی دریافت کرده که منجر به دو مورد تلفات انسانی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/70999" target="_blank">📅 15:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70998">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxwC7vuCYzTwpwqKN5NIlO6WKtD1s8CyB04VGaAer6jhuvsgWJUoP9esUJRzFGZ-0wEGxEArl0WYy-PUPOawvdmeLvydeVWAWqJDgUqd2dnzxOzUs_kKxqtRsPzY8iSRW9UbCFEihV-TAmUk3bStEY7fvTJEoBWH2pygquVca5tpJ8tlHQKEPg05HBk6ajQsn1oFwwU1d5JMRsgzwHfNpMXCTVj904xO-22G8NoDYP7IV6YDSsG4g64GL2fkyJLlZeg7PAjz7FAlx9LS32To4F5-1MT7dvTJ-tzuy1L5NLMZF5ueC1n6ZhconVW1_hYe196s_0zoUEjGqT6hMtFE-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
فیلد مارشال محسن رضایی:
با این دست‌وپازدن‌ها، نه تنها در بیرون آمدن از آن ورطه هولناکی که برای خود رقم زده‌اید ناکام خواهید ماند، بلکه به‌زودی خواهید دید که راهبرد جدید ایران در میدان نبرد، دیپلماسی و مقابله با محاصره اقتصادی، بنیان‌های شما را درهم خواهد کوبید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70998" target="_blank">📅 14:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70997">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13235e9918.mp4?token=EQJ4M1cvJyExfHTbBJ11TvmX0N6GEBTSO9oXMKxzQ2BN8Zd-rq0p-HAvaXluRph43P5jw9H_r2gXMip0IKCRb_JJOtDbd3ZhKzopnrS553SqbzD1ygt61GLDvOK-MZOsO1FJoh0Zr17hHIGug27bMZwvJZyXIPDULDreaa9cv7dUEbPBKIWvSk2fPftDg5IUZnMXeYTM7ibIFJF_iqi7M9Ipwqs046ImKDkto1-_pr74Ysgg2hyxpKt12gvnR_2XgcU6xhbAcuJ7iDTfHxK68WjZ2OYMOl9MH8QrTlKmQfJD8GymHRiWNq6sqUKDsLmYdBAwHZgMRlejoS_M6PVulg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13235e9918.mp4?token=EQJ4M1cvJyExfHTbBJ11TvmX0N6GEBTSO9oXMKxzQ2BN8Zd-rq0p-HAvaXluRph43P5jw9H_r2gXMip0IKCRb_JJOtDbd3ZhKzopnrS553SqbzD1ygt61GLDvOK-MZOsO1FJoh0Zr17hHIGug27bMZwvJZyXIPDULDreaa9cv7dUEbPBKIWvSk2fPftDg5IUZnMXeYTM7ibIFJF_iqi7M9Ipwqs046ImKDkto1-_pr74Ysgg2hyxpKt12gvnR_2XgcU6xhbAcuJ7iDTfHxK68WjZ2OYMOl9MH8QrTlKmQfJD8GymHRiWNq6sqUKDsLmYdBAwHZgMRlejoS_M6PVulg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
پوتین خطاب به پزشکیان:
تو این شرایط سخت، داریم سعی می‌کنیم هر کمکی که لازم دارید، بهتون برسونیم
.
قبلاً هم دربارش با هم صحبت کردیم و داریم کالاها و اقلام موردنیازتون رو تأمین می‌کنیم.
با وجود شرایط نظامی و سیاسی فعلی، همکاری‌های تجاری و اقتصادی‌مون رو با همون روند و قدرت سال گذشته ادامه می‌دیم.
همون‌طور که بارها گفتم، ما تو روسیه کنار مردم ایران هستیم و باهاشون اعلام همبستگی می‌کنیم. شجاعت و مقاومت شما واسه دفاع از منافع ملی‌تون واقعاً قابل تحسینه.
لطفاً سلام من و حمایت صمیمانه‌ام رو هم به رهبر جمهوری اسلامی، مجتبی خامنه‌ای برسونید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70997" target="_blank">📅 14:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70996">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">1
💵
= 200.000
💸
🔼
یک دلار آمریکا=دویست هزارتومان   @News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70996" target="_blank">📅 14:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70994">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a6a11bf6.mp4?token=ssZ41W4D481KrXVq-F4VMzT8AAeDozEJlwSlnwPl7g7Qz7kK-5ZQqnH2Po14U_F40WGy6NdfFH15J9c4U3bWa91t8IIgIeYILH-olLiRxW2lYVEQIDF3QKQtLdGocphy31iCrFlghxYnpVKwHlKk_XQgDivEnE-cVkFLDm6MjxWJ6LD4EFgNI1avXbKlJIDKgfvSiWgswElvGDj6p5trkWD-6mVi5Dq5qFiO2O4BpLFkWYXueefCId335bbBTjMCUU35uWI1LPS7GptvO5PMkNSBwIl0eo6Udnt1E_RfiuLWcVCFzv2r4w99mSmM0OcTZri_3sTMeW7YQsDYM1kkaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a6a11bf6.mp4?token=ssZ41W4D481KrXVq-F4VMzT8AAeDozEJlwSlnwPl7g7Qz7kK-5ZQqnH2Po14U_F40WGy6NdfFH15J9c4U3bWa91t8IIgIeYILH-olLiRxW2lYVEQIDF3QKQtLdGocphy31iCrFlghxYnpVKwHlKk_XQgDivEnE-cVkFLDm6MjxWJ6LD4EFgNI1avXbKlJIDKgfvSiWgswElvGDj6p5trkWD-6mVi5Dq5qFiO2O4BpLFkWYXueefCId335bbBTjMCUU35uWI1LPS7GptvO5PMkNSBwIl0eo6Udnt1E_RfiuLWcVCFzv2r4w99mSmM0OcTZri_3sTMeW7YQsDYM1kkaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
〰️
ناو «یو‌اس‌اس آبراهام لینکلن» در تاریخ ۲ سپتامبر و پس از ۲۸۶ روز حضور بی‌وقفه در دریا — که رکوردی مدرن برای نیروی دریایی ایالات متحده محسوب می‌شود — وارد بندر «لائم چابانگ» تایلند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70994" target="_blank">📅 13:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70993">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل درباره ایران:
هم‌زمان با افزایش فشارها بر آن‌ها، تشدید تنش‌ها و تنگ‌تر شدن حلقه محاصره — آن فشار اقتصادی خفقان‌آوری که رژیم افراطی بر مردم خود تحمیل کرده است — احتمال دارد که آن‌ها واقعاً دست به حمله بزنند.
چرا؟ زیرا ممکن است برای رهایی از دوراهیِ میان «خفقان» و «جنگ»، گزینه دوم را انتخاب کنند. ما از نظر دفاعی برای چنین وضعیتی آمادگی داریم.
اکنون در ایام تعطیلات هستیم و آن‌ها معمولاً در تعطیلات یهودیان دست به حمله می‌زنند؛ هرچه باشد، آن‌ها از یهودیان بیزارند.
اما ما — هم در حوزه دفاعی و هم تهاجمی — و با هماهنگی ایالات متحده در این جبهه آماده‌ایم. بله، در همین جبهه.
با این وجود، سناریوهایی وجود دارد — مانند حمله به اسرائیل — که ما به هیچ وجه آن‌ را تحمل نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70993" target="_blank">📅 13:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70992">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0dd8120289.mp4?token=GVCdCKV399U87QquoBhiLK1o-EVMkHSJrXxJTPuBFFilA53BV2Ra-ldm93ZxRSygeAdTHUAdPD_jNDPyMOLa52G-UcndGhGKcCI2VreLFYVnp7Ip73w9mrjXF_tLll0WCRbnVcXA3JEXDSPlW0fOEuKXfTaRYwh56kTbtai5FYPPeo6SA86nsAq54kTy-Hyri-GWjwrRzCHHzBPuD-5QRhTlOmlpPNhtW4Sy_7xUG1u3iJeB1VXicxFojlm5K0xrEd6uuVncJybRh-uKOJkN5JFQLqIJddAJLRTELE1U_WfRNgLfAXBMYNvmymbNJFa_Isg6amseg0ucJGvkc6jh3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0dd8120289.mp4?token=GVCdCKV399U87QquoBhiLK1o-EVMkHSJrXxJTPuBFFilA53BV2Ra-ldm93ZxRSygeAdTHUAdPD_jNDPyMOLa52G-UcndGhGKcCI2VreLFYVnp7Ip73w9mrjXF_tLll0WCRbnVcXA3JEXDSPlW0fOEuKXfTaRYwh56kTbtai5FYPPeo6SA86nsAq54kTy-Hyri-GWjwrRzCHHzBPuD-5QRhTlOmlpPNhtW4Sy_7xUG1u3iJeB1VXicxFojlm5K0xrEd6uuVncJybRh-uKOJkN5JFQLqIJddAJLRTELE1U_WfRNgLfAXBMYNvmymbNJFa_Isg6amseg0ucJGvkc6jh3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو از فروش طلا، به دلایل کاملا نامعلومی بیش از 5 میلیون بازدید داشته!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70992" target="_blank">📅 13:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70991">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70991" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70991" target="_blank">📅 13:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70990">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qM4wDHd0MZoz5DFsfg815FlvOZXob_gcLCooevOX7uqC5zu4E1joRPacwZGyG7uOAGNBNlrQoAjh9Sf8XoPEncwS3fkrUsqRIkdyYkZCjhxd5xqF5ll-0pCPa1J7JsAwYGxVN2rFDTb9jf9Gg174Ilfx2xpAoqELO2lXSROfQFE7oheJE9SVQpkYrdYIaaJV8WfIhoJu2WCMMZG1FPdtlXohJ6hAskjNi68mrkxvs3EOXZ4io815DcGp6eSPDoLdvyzYEjzpVAgyjMBwP7DWXYbdm0LGW31LRcpWkjOFxI9nQrUUlfMSn5sFwia4J8FUuEM-WK8wGpfEh3sxfb5dWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70990" target="_blank">📅 13:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70989">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1829295007.mp4?token=N3rQfoCpKyDxMFsOGmix7SwIepeztxDZxvLRjjIIT-9b4eQ_s3PjfhnW1ytb6SvETBLnq_VnIzmlNHgxySTO07h7Y6CtI63vrnMURvkbH6kU5cH4GaWi3XMcUaG1UvWQvl6dBYu5Tj4rbbmVzoXlw_OBBQZI9FuhskjTHmWXfkXbsqpgEzwW7crv0L6v7G8EIo4JQqOC_16XSFeV_dD6hkObmEowa1uDB3iUtscdjpVpmy-ELDpIrdR1WL9vMmZ8sPzI9IO1SRlj3_vKirzfbHgiQyI5gf8ziYLN22Mj7SgmaP_YNwEArDcxRslQg_H-8xE9O2mrqalKvry7aJmdNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1829295007.mp4?token=N3rQfoCpKyDxMFsOGmix7SwIepeztxDZxvLRjjIIT-9b4eQ_s3PjfhnW1ytb6SvETBLnq_VnIzmlNHgxySTO07h7Y6CtI63vrnMURvkbH6kU5cH4GaWi3XMcUaG1UvWQvl6dBYu5Tj4rbbmVzoXlw_OBBQZI9FuhskjTHmWXfkXbsqpgEzwW7crv0L6v7G8EIo4JQqOC_16XSFeV_dD6hkObmEowa1uDB3iUtscdjpVpmy-ELDpIrdR1WL9vMmZ8sPzI9IO1SRlj3_vKirzfbHgiQyI5gf8ziYLN22Mj7SgmaP_YNwEArDcxRslQg_H-8xE9O2mrqalKvry7aJmdNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇨🇳
⭕️
حسین مرعشی دبیرکل حزب کارگزاران:
🍆
چین سفر قالیباف به چین (و گسترش روابط تهران-پکن) را مشروط به موارد زیر کرده است:
۱- باز کردن تنگه توسط ایران
۲- دریافت نکردن هیچ‌گونه عوارضی
۳- پایان دادن به اختلافات خود با عربستان
۴- پایان دادن به اختلافات خود با آمریکا!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70989" target="_blank">📅 12:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70988">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران:
ساعاتی پیش دو فروند کشتی نفتکش که با تحریک ارتش آمریکا خدمۀ خود را پیاده کرده و برای گذر از مسیر غیرقانونی در اختیار عوامل آمریکا قرار گرفته بودند، با رفتن روی مین منفجر و متوقف شدند و در آتش می سوزند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70988" target="_blank">📅 11:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70987">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzpPduMlPTNLqlGu8oeQ8aYA_rO8pMLDGt0ojg2rr5QB9pxpBZaIitorB1WabKFHpOYvFCD-e1oQwFZW_4hWzIgMlfzNXL0lWvLYJIeqRHExns50czq0kXh8OR7HTatUpBOIMgHP3XtjWQfOPBYJ851W7oc_SGb3MJ_4Vq8xFuDIf5yaJT64ovQwjkyTM5IqTdOICa1JeSESpzlNIAbctMRKphReJP0XkuebptTCg1oqfz7PIo-UMCooTZ0K4KKElJzqKNskTuVzAApkpbZEUPGX_cHMolBmIo5bRxWS0V9WKr_xTzowaybelEtTcF7YD7kLdVCHGOUYWyb917_tQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ:
من برخلاف گزارش «ای‌بی‌سی نیوز» (که اخبار جعلی منتشر می‌کند)، سعی ندارم ایران را به پای میز مذاکره بکشانم. برایم کوچک‌ترین اهمیتی ندارد که آن‌ها توافقی را امضا کنند که از نظر خودشان بی‌ارزش است.
وضعیت فعلی ما را بسیار بیشتر می‌پسندم؛ چرا که تقریباً کنترل کامل تنگه هرمز را در دست داریم و اقتصاد آن‌ها نیز در حال فروپاشی کامل است. آن‌ها صرفاً دارند زمان را سپری می‌کنند تا با سرنوشت اجتناب‌ناپذیر خود روبرو شوند.
مردم ایران چه زمانی قرار است قیام کنند و بجنگند؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/70987" target="_blank">📅 11:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70986">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43dc462e7e.mp4?token=HJkuOGx7Qe1ykzI8iAPqDrgTVQRq9TDBkl7xtwEXTJ44lR8_nNuqLak4CijQMHJq-Au11vBwDFSFvWq2iiIrq8psxhybuKZiEH1s3o5gRKhI2IrxFu-66xe0-DMjjwaBm-STUDGgipPtGKAnicbr-tCaSanTwFAIqISM3RwAmYxn1RYNsVmt0gHr43FtWc4mSqWENXcrNxIX-1n3UkDXXlr2aU4FbVLdvA0xA5l7wf-XO2m4OHsXUc8JXVUJXvT-rXC59T_tW0tM31blF29CU6uJxgcNrK5VzZ8TA2ELFoK-ZL05aXCPFvlX6-OE24JLU7EWIYru_BGJ5Ewv8pgs_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43dc462e7e.mp4?token=HJkuOGx7Qe1ykzI8iAPqDrgTVQRq9TDBkl7xtwEXTJ44lR8_nNuqLak4CijQMHJq-Au11vBwDFSFvWq2iiIrq8psxhybuKZiEH1s3o5gRKhI2IrxFu-66xe0-DMjjwaBm-STUDGgipPtGKAnicbr-tCaSanTwFAIqISM3RwAmYxn1RYNsVmt0gHr43FtWc4mSqWENXcrNxIX-1n3UkDXXlr2aU4FbVLdvA0xA5l7wf-XO2m4OHsXUc8JXVUJXvT-rXC59T_tW0tM31blF29CU6uJxgcNrK5VzZ8TA2ELFoK-ZL05aXCPFvlX6-OE24JLU7EWIYru_BGJ5Ewv8pgs_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عطریانفر، عضو شورای اطلاع‌رسانی دولت:
پزشکیان اول توسط شورای نگهبان برای شرکت تو انتخابات ریاست‌جمهوری رد صلاحیت شد ولی شخص علی خامنه‌ای صلاحیتش رو تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70986" target="_blank">📅 11:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70984">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7PxvBIi7WtAsrFjvX-0LHRJDCfnB8fll4uzxs82iRSZm-rCi5z35aCnT3-ZTxcAM9hAmJkFgkhldJmDTW7g7wdxm3oMIfuo_Xjybz4Vlxgcyk3viJUFHQXiEJUcPnDlw_FOCDHFmHWGlkkZN7rvKht6Hxbn7aKNo1VjSZT_d_pYNtYobxNn5j5ZrHfDvOExr1DTqSgEP0Dlmflf7a_SUPGCvK7tUm3mqLGjGJINHNXuG54flaba4uDl8J6d0TI1wKGzYfd_JndYmIZhu0wfYNo7-bK_nQzg6EYj7-8K_pRQt8NpKrHD6lN7pZ17nn7QZPkBe5rjdnOLADlg1MbNLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f0caae86.mp4?token=Q-1MfKZIB5c22B-BCapT2zIzhsHCSsbxhq4bfL7vNyK7buoGdkmJ1jPKxoB135jVAtoFecOZNrFv1UZw1jqBo5y43MrE-KQ_5XBrZjkH5vS49w47vnaMtgbcr0Un1rvEXSlQYPLPY-jnTsxhxekjeuZPfeIrai7S12nFTsFFAuxr0n-K2Ir9OwGPs1AqxDrhKPx_TbTV_PdrUvVTyh0AVbjCSg1vsBmlA7r3clA0zulOywhP14w6X60Oyg_n5NGdt556GXq1f6baStdOqanxedBfah9P2l5xMsZJnKLNHHPB8zbtXK6pVQUpFgKTiGhGrcxS-_M14z0i2yLw1XZJtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f0caae86.mp4?token=Q-1MfKZIB5c22B-BCapT2zIzhsHCSsbxhq4bfL7vNyK7buoGdkmJ1jPKxoB135jVAtoFecOZNrFv1UZw1jqBo5y43MrE-KQ_5XBrZjkH5vS49w47vnaMtgbcr0Un1rvEXSlQYPLPY-jnTsxhxekjeuZPfeIrai7S12nFTsFFAuxr0n-K2Ir9OwGPs1AqxDrhKPx_TbTV_PdrUvVTyh0AVbjCSg1vsBmlA7r3clA0zulOywhP14w6X60Oyg_n5NGdt556GXq1f6baStdOqanxedBfah9P2l5xMsZJnKLNHHPB8zbtXK6pVQUpFgKTiGhGrcxS-_M14z0i2yLw1XZJtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇮🇷
🇮🇷
پوتین در دیدار با پزشکیان:
خواهش میکنم سلام گرم من رو به آیت الله سید مجتبی خامنه ای برسونید
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70984" target="_blank">📅 10:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70983">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48458cadfa.mp4?token=W9paBrir6jFipKU_dLURd0lbwBL3knMDXu2pJOWKlycr31Xln1-7gT34IWioPw5uA-KxriVENw7cNk_D4Y2YE0kh9nA8TStJjVrLh3w9TONHKikBXBLTeWdrkPKcRmwSBIqBVdy52dWgYU5HOd0KiZMfTI7pqIpFujaRKwtHpJgMFlfCR30dowvvq5oFFODta6CRtObsTVID_xd5cha57njEnAG1VzHfK7NWW3ocZjd9OKwWoj0qkzqZvXPKQa9aV-Qtg_FS-jdPubLfKtwN3ZdU5bw5sQw_30-9F9HRHbUyvikbGL6yPsqRd3qDHSPiSY7Trf8UyH67ww4R6wKnLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48458cadfa.mp4?token=W9paBrir6jFipKU_dLURd0lbwBL3knMDXu2pJOWKlycr31Xln1-7gT34IWioPw5uA-KxriVENw7cNk_D4Y2YE0kh9nA8TStJjVrLh3w9TONHKikBXBLTeWdrkPKcRmwSBIqBVdy52dWgYU5HOd0KiZMfTI7pqIpFujaRKwtHpJgMFlfCR30dowvvq5oFFODta6CRtObsTVID_xd5cha57njEnAG1VzHfK7NWW3ocZjd9OKwWoj0qkzqZvXPKQa9aV-Qtg_FS-jdPubLfKtwN3ZdU5bw5sQw_30-9F9HRHbUyvikbGL6yPsqRd3qDHSPiSY7Trf8UyH67ww4R6wKnLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایشون رکورد دار عمل زیبایی بین آقایونه و تا حالا بیش از 300 عمل زیبایی انجام داده!
پسری که عمل زیبایی نکنه اسکله، تا حالا 200 میلیون خرج ابروم کردم، 150 میلیون خرج لبام شده
😶
استایلم فقط 400 میلیونه، 500 میلیون دادم که خط سینه بندازم. پسر باید به خودش برسه.
هزینه روزمره‌ام روزی 100-150 میلیونه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70983" target="_blank">📅 10:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70982">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⏺
🇮🇱
نخست‌وزیر نتانیاهو:
آیت‌الله‌ها می‌خواهند من در انتخابات شکست بخورم؛ حزب‌الله و حماس هم همین‌طور؛ و البته ترکیه نیز خواهان شکست من است. آن‌ها این را آشکارا بیان می‌کنند.
صادقانه از خود بپرسید: دشمنان اسرائیل می‌خواهند چه کسی در این انتخابات پیروز شود؟ به شما می‌گویم: آن‌ها نمی‌خواهند من پیروز شوم.
ما برای کل جهان آزاد می‌جنگیم. آن‌ها این را می‌دانند و به همین دلیل است که می‌خواهند ما شکست بخوریم.
ما اجازه نخواهیم داد آن‌ها پیروز شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70982" target="_blank">📅 09:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70981">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=NKhpIPDNYuLWSC11e7QtsRjySjlW6Mbi0-rZsWTWc-XIgJUoB_FPy5FzcfSWuDTjiD1iKHpO32YRiegZ4Aby_pCmOqTtR5AFHxavrysFSg4R6ek6_RvgLZ3eBg3en5Wja85G9HzFjNu6nyLLHPzR1iB0eAuPCsl96R8RnwTHuFM5ayOA0BES_nMchJbqifoch4u0BfZeuXnT5NRc4Jd3fD2lnBWStIet6EZLc6G6_ze9eJ1Rbsg-Z3jBH67PbexT64JAgtCnomY6Sd8oNX2UQ6OM8LrXjb72SjvR579hN0iiP97qB7RwAa3eGdXxaHI_AkD0W7v_z2C0cqtbpCC6iA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=NKhpIPDNYuLWSC11e7QtsRjySjlW6Mbi0-rZsWTWc-XIgJUoB_FPy5FzcfSWuDTjiD1iKHpO32YRiegZ4Aby_pCmOqTtR5AFHxavrysFSg4R6ek6_RvgLZ3eBg3en5Wja85G9HzFjNu6nyLLHPzR1iB0eAuPCsl96R8RnwTHuFM5ayOA0BES_nMchJbqifoch4u0BfZeuXnT5NRc4Jd3fD2lnBWStIet6EZLc6G6_ze9eJ1Rbsg-Z3jBH67PbexT64JAgtCnomY6Sd8oNX2UQ6OM8LrXjb72SjvR579hN0iiP97qB7RwAa3eGdXxaHI_AkD0W7v_z2C0cqtbpCC6iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
〰️
سنتکام ویدیویی را از حملات به ایران منتشر کرد؛
سنت‌کام، فرماندهی مرکزی آمریکا اعلام کرد نیروهای آمریکایی در روز اول سپتامبر، موجی از حملات علیه اهداف نظامی ایران را با موفقیت به پایان رساندند.
بر اساس این بیانیه، مواضع پدافند هوایی، سامانه‌های راداری، تجهیزات و تأسیسات دریایی، زیرساخت‌های مرتبط با مین‌گذاری و مراکز ارتباطی سپاه پاسداران هدف قرار گرفتند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70981" target="_blank">📅 09:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70980">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70980" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/70980" target="_blank">📅 02:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70979">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiXBWkDK7gkJRBz1Qnnys3g_0D81YlXDJKw4PNrsNbOeH3BeV_f88VMWVlpn6HIMszaXVDgmhseKTbTz3QDmf0aP98s-M8rTtkbhW88zESUnkWBnv_6VKORRDe40c8izvlpqA07lgW-p4_r8Uv_AyIV9GiGG3Nx1RFieLhZqoH6GDwDqSrVlv7S6E3gtXplHNq2Jcl8svezCdFAXOKXMq02OhcfJFenUWQjqKtFcy42nkEZ_roXR1iY1PpD3q5IdRJSoKYaYV76Um2CLi7EZCM1SSWcmoGb0m2HAukBY6CQA5QDiBjeuM0ICyCBv_Crccu6JahqVRuPnY-1UIta9-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
سایت جهانی
TrexBet
می‌برتت وسط
جنگ
بزرگ!
⚽️
استقلال
🆚
پرسپولیس
⚽️
اینجا فقط فوتبال نیست… دربی‌ـه!
۹۰ دقیقه جنگ، کری‌خونی و هیجان تا آخرین سوت!
🦖
🦖
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/70979" target="_blank">📅 02:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70978">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
منابع عربی:چندین انفجار در کویت و بحرین رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/70978" target="_blank">📅 01:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70977">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sjw4PRVj-R0YOUC7wDI7s5iUz-wQD3fx9ZevYR4WrghMymHjchTY2tu8uFfkPVULEx49Iyn975lZDt8emW_KssolcFisCWsTDiqZjwf0evx7VNeBSo-jpNngcYsx_pPa-tPHFAogqHlAebF8loIVLFUDbnGcxsS5YQDQxj7MKiaKZZSQpYbCR_JuYHQ3QMUAhKZvSCkLSt6LXjUhxQxZwvEGruPSqUnFiIJ5HvStI20FtYkgZxS0bsaoAUSJH0aH9zxuhLwZ45OKlsX7Asj0wUTaF-igu35KBWFMxDuEX7tg1ASzrjrIFU62myeqjvaeZakW4BMycJNHL-V6ARVoCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کویت اعلام کرد پدافند این کشور در حال مقابله با پهباد هاست.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/70977" target="_blank">📅 01:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70974">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⏺
🇯🇴
نیروهای مسلح اردن:
پدافند هوایی کشور ۱۳ موشک بالستیک را که وارد حریم هوایی پادشاهی شده بودند، رهگیری کرده است.
به گفته ارتش، ۱۰ موشک رهگیری و منهدم شدند و سه موشک دیگر در مناطقی دور از مراکز جمعیتی سقوط کردند.
در این حمله هیچ‌گونه تلفات جانی یا مجروحی گزارش نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/70974" target="_blank">📅 01:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70970">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UpPkjtuQKgtKVZfkP1EIaWolkBdOfshigrvPc5IXGeI4v-cR3L_wZyc8EYXc8EGnC1qjIw3BMIDpmV6f_7AiITF6rlfwcCU9nMYrr63w_2TyycBiChXrTl1XAljfH2w-jQmq1NoaeHrczVfXnMxoxO4vQn5CETCmmUiRlmYJT95O8vB8BihTkqiFhkfKLRDXm6AtVOVroytMXfu6FPZ6XfO_UVIZiKnnlXym-LOumiLWBaU0Ic433BqDT8XM5nUaQgDasSWNYWQ6ub3COdwt7hFESWMjtISRKzc-qz01vXd-k9trNhUFPFAissxJnQRRvRFfws3kSUfuQ9Fpy8aY5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/703c34050b.mp4?token=tY0ZKY8J7p4A8hXy9Rf7o-rGKI9qcgogw7wS9O-BFBpFsKm566431wFMxOLuEWviwXCVPekCdxT-51MEiV23XlNE_9iM2U3Kbzb76-WtfB0UjmlSFCTvxMWHyYrFH9ZO9A9ZqCSduOQkfF5T4VOnMmlpwbSKUPGq6-hO3osBRIP3eQXXcf02zkufMECqjtVtiF-iGHGwD1r0bT0SdTcqw6VQKye-qJ61jyb1_w90ulm9aJFs1nVX84uSLE_bqtQRiB9IyoT_RDOFWgxJzcgRzhf7BreapFP7VS8n4rWV5rACwxxORuxj8GMi0UsfwpOol6CkV_bvho0SJeSOZdxJzw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/703c34050b.mp4?token=tY0ZKY8J7p4A8hXy9Rf7o-rGKI9qcgogw7wS9O-BFBpFsKm566431wFMxOLuEWviwXCVPekCdxT-51MEiV23XlNE_9iM2U3Kbzb76-WtfB0UjmlSFCTvxMWHyYrFH9ZO9A9ZqCSduOQkfF5T4VOnMmlpwbSKUPGq6-hO3osBRIP3eQXXcf02zkufMECqjtVtiF-iGHGwD1r0bT0SdTcqw6VQKye-qJ61jyb1_w90ulm9aJFs1nVX84uSLE_bqtQRiB9IyoT_RDOFWgxJzcgRzhf7BreapFP7VS8n4rWV5rACwxxORuxj8GMi0UsfwpOol6CkV_bvho0SJeSOZdxJzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
امشب از نقاط مختلف کشور به سمت مواضع آمریکا موشک شلیک شده؛
🤩
تسنیم:
امشب یکی از گسترده‌ترین شلیک‌های موشکی ایران (به نسبت درگیری‌های اخیر) به سمت پایگاه‌ها و مناطق آمریکایی انجام شده است
ایران هشدار داده بود که حمله دشمن آمریکایی با پاسخ چند برابری مواجه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/70970" target="_blank">📅 00:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70969">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران: پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تبتین هدف موشک های بالستیک قرار گرفت. تعداد زیادی از نیروهای آمریکایی به درک واصل شدند
⏺
روابط عمومی سپاه پاسداران انقلاب اسلامی:
در پاسخ به این شرارت سبعانه، رزمندگان دلیر نیروی هوافضای سپاه در موج دوم عملیات تنبیه متجاوز "با رمز مقدس یا رسول الله (ص)" با حمله سنگین موشک های بالستیک به پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تیتین، واقع در سواحل خلیج عقبه، تعداد زیادی از نیروهای آمریکایی را به درک واصل کرده و چند تاسیسات مهم و بالگردهای هجومی دشمن را منهدم نمودند.
عملیات انتقامی نیروهای اسلام ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/70969" target="_blank">📅 00:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70966">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYN8T3Hrttdhri2WaSz0b0Xs0Hf-5VwfPaD9N0xlBcgeYRR8bRZoH1MLoKa81N-javDzMgb5K0cvSaQvmIMDWsCx288ylUA769RW6rrpJ8AVl8M1aTJkJ2I8psm3wG6h-qexbmn988SShWYZoR_RAZfmX4V4kZtBr1K5V-eHAo8yTldedpYWf1rpR9V_d_4-fVbzSzQjnRO_rpM6hcjJ1V0xP50DWPnDk_QUQ8BZ_nYuIuacsmAQiXHH9-OS6jy3EFjFxAMUHjyKAck_bwQRmqtnq6qbb9jO_nyBzRTVTjzmACUnPvkt1Lpv5uvvQtnstwNa_vDIz-lLe3CRfwl1hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b67f6c5b37.mp4?token=BJKiEyvmkMHpuz_EdCMbd3e4VU1WIZNcTo_J6sYOuvrDp90Jr6iroNfq5wQM9bNNt30lVA6GH-G6UxeyckWTqgPS0KVeHh9lOdtPY_VPioBPBDoJzUdQpX1z20u-QwW0MYJeaIx4TzaOhEcTaj5oPlgaJpYosdHm09vef5Q9wP1wTXfHmevr_VcXRAQWhDVwCuqcZHjoWzzHjHAKmWxf4ARtDLHfoJgDInlMNusCTYN8Qt4eq_3Bf_KreY-Nc9Kd7U8AUly6HNt_aseGOidhHNgCujlYmt4M4vcdMKsC1IcMt76FB1AD9oelVSE36_wIyNjpYhqIksj86dQw2ckrqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b67f6c5b37.mp4?token=BJKiEyvmkMHpuz_EdCMbd3e4VU1WIZNcTo_J6sYOuvrDp90Jr6iroNfq5wQM9bNNt30lVA6GH-G6UxeyckWTqgPS0KVeHh9lOdtPY_VPioBPBDoJzUdQpX1z20u-QwW0MYJeaIx4TzaOhEcTaj5oPlgaJpYosdHm09vef5Q9wP1wTXfHmevr_VcXRAQWhDVwCuqcZHjoWzzHjHAKmWxf4ARtDLHfoJgDInlMNusCTYN8Qt4eq_3Bf_KreY-Nc9Kd7U8AUly6HNt_aseGOidhHNgCujlYmt4M4vcdMKsC1IcMt76FB1AD9oelVSE36_wIyNjpYhqIksj86dQw2ckrqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متاسفانه امشب یه خبر بد هم داریم، در طی حملات آمریکا تو بندر کوهستک حوالی سیریک، ترکش حملات می‌خوره تو یه مراسم عروسی و چهارنفر جونشون رو از دست می‌دن
🖤
#hjAly‌
@HutNewsPlus</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/70966" target="_blank">📅 00:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70965">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u61yVU1BEQxUaSf0PHOz5W3mK62DmCZQb4zsO8QkoLFgVLnWVV19jonroKdxTc2wmQm0egMVCj5FtNKLEEUIQMqVRC8jvZa6wHRv8ZsAHRnwlOAPz_XUcZVpY-EDLvk9l4EA5x2ZbB5GShg1jL43ADaTyd1kTodPUCmQ0Anib0VgJjukXfCzfrEVSEIg7Oj2Q2L5xVfM0oZzfTjrluhnA5jLPkCSJsQqnHyTubUlBomc7Jjwf5eWIMmGmhhj6pM3iGXq4ylnMIh8fHgR7bvt0rjAs5VeBVXt111V2qBoMFrZDHb_yr5rxzkl1iEyneGmi7pQQEjxr91hi2cIWm7-7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ایالات متحده در حال حاضر هشدارهای امنیتی به‌روزرسانی‌شده‌ای را برای چندین کشور در خاورمیانه صادر می‌کند. این هشدارهای امنیتی برای بحرین، قطر و اسرائیل (اورشلیم) صادر شده‌اند.  @News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/70965" target="_blank">📅 00:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70962">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4e410d017.mp4?token=WM69PA-kp5dPemd8D-3APbzHQB4thifKs58zJi1MeSSWBVCFdPZb742pG1M84lJ-CZ-WL7xQ0IKaKzUg8kUG5QPKhPpGq-XcPSA8hCZh9BW119vf_2EjFFVMEVR3Y0e70WvoNS1wGVIZtxZQw1JoCH-yXN7wSCwaXhUV4FBJCibAX7X0MKDJSJuQPvgrh7jTpcpPZfC3YiwLeFM9Gqh1ZYDm7HNzILuaAp-sFOm4XZJA4bD5Vl_yD6Uu4G-zGA_VsrkWRgOPp82UtmrNFRxVViU26u-XiiAQRW2K-b4omWHiZY1nW4W-6nwVQ5kT0GLi3jGq685Ol9MCIU1wdOXysg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4e410d017.mp4?token=WM69PA-kp5dPemd8D-3APbzHQB4thifKs58zJi1MeSSWBVCFdPZb742pG1M84lJ-CZ-WL7xQ0IKaKzUg8kUG5QPKhPpGq-XcPSA8hCZh9BW119vf_2EjFFVMEVR3Y0e70WvoNS1wGVIZtxZQw1JoCH-yXN7wSCwaXhUV4FBJCibAX7X0MKDJSJuQPvgrh7jTpcpPZfC3YiwLeFM9Gqh1ZYDm7HNzILuaAp-sFOm4XZJA4bD5Vl_yD6Uu4G-zGA_VsrkWRgOPp82UtmrNFRxVViU26u-XiiAQRW2K-b4omWHiZY1nW4W-6nwVQ5kT0GLi3jGq685Ol9MCIU1wdOXysg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تو وکیل آباد مشهد یه ماشین به تجمعات زده ٢٠ نفر کشته و زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/70962" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70960">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rP_j9ho9nOogBlu1EPHJA_acOIWnYfz_1AYlhUoIArIOXIxmIEUlGOJYWP315X2hoytrelwG5eUewjUr5FqcRN7swhFUZ9SgmgIZ7WQYXtZWRhZiOzbVkupMJiAr6k2LgH1P_eioT_KGUFw4P4VzSPW3akq3L8jfn_wVfaNvgIvJERS_l4CYY4FWyTTCqAdSHVZAuL8cmlgIslAgwodXvANfoTN868BxvzAVy1uNP5_ZbNWo9VVsjRAGtz0tw-3ZOcxQr1slAaLEY4kjcJSPHRXqCjhHL50n7MQy9PtMMotIbj2DkJxpUYJ50xsJTmT6CywhZzuxMoiV105DD3vN1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/791bfa967f.mp4?token=Lr2KG_GXKiz3W3daX3PBsE8olQd2qXp6zozoI-X3toBomllnxS-pSurY1f3YC6YHKyWLSfpN3J_rLTtCt0nbDC_KjTYR6SVB1An60HyG6TRHaXMrB7I5n5lD7U7HF4VRQcbF9jAb6mZmEPq57XFHQ7Hr_dWv4elIhNq9SbyFt7x9ZwtfQzPmT8pd4A_TPTLOzsTzMX2X_vJB0obf5Em4RerWM9kBMRspvcQ7NngVkwDvSZ70dk6yElMe6XBRsxh1BTGoWO0eODd-z--8nJlKrlNLyCpcyJakKW7yt3vgZ_yItYk24vmB_jp5hEZjdaHfhMOfus9QPZaIoMP3BLeEVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/791bfa967f.mp4?token=Lr2KG_GXKiz3W3daX3PBsE8olQd2qXp6zozoI-X3toBomllnxS-pSurY1f3YC6YHKyWLSfpN3J_rLTtCt0nbDC_KjTYR6SVB1An60HyG6TRHaXMrB7I5n5lD7U7HF4VRQcbF9jAb6mZmEPq57XFHQ7Hr_dWv4elIhNq9SbyFt7x9ZwtfQzPmT8pd4A_TPTLOzsTzMX2X_vJB0obf5Em4RerWM9kBMRspvcQ7NngVkwDvSZ70dk6yElMe6XBRsxh1BTGoWO0eODd-z--8nJlKrlNLyCpcyJakKW7yt3vgZ_yItYk24vmB_jp5hEZjdaHfhMOfus9QPZaIoMP3BLeEVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه حمله آمریکا به دکل سیریک که با پهپادهای انتحاری لوکاس(کپی شاهد) انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/70960" target="_blank">📅 23:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70959">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/541d79e411.mp4?token=Uaud8e8WMMbP6pFSDunetljbmHc9OetEAZuN7XJanQ4TKgDDH_qed_2eYzp_MV1TRM5ZphLOb0G2jRzTeNResFWvbSjgMGtnx4ASyHXlLE4UI9VdAEEWn6BBaPQHQJUD8TyUF0V3GWyFS7WfjmdJE7Vx-dsD0arDT0Xy2-i1ty4g9B-bCCH0_JmyM6T4kGwvAaf8dPldNiEcmPc9VDAZBb2ot91l1GXZyTbvtAKHb__iFC3yJj41RA8e84NVwZ27a3VyUbaZKooJ0JCT64z8jrbxhCMgn3IwHrzt_KhhvrASXquk1yAVbBAIQmOoIYtCN9TgtENbsAg9iCvtLbB70g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/541d79e411.mp4?token=Uaud8e8WMMbP6pFSDunetljbmHc9OetEAZuN7XJanQ4TKgDDH_qed_2eYzp_MV1TRM5ZphLOb0G2jRzTeNResFWvbSjgMGtnx4ASyHXlLE4UI9VdAEEWn6BBaPQHQJUD8TyUF0V3GWyFS7WfjmdJE7Vx-dsD0arDT0Xy2-i1ty4g9B-bCCH0_JmyM6T4kGwvAaf8dPldNiEcmPc9VDAZBb2ot91l1GXZyTbvtAKHb__iFC3yJj41RA8e84NVwZ27a3VyUbaZKooJ0JCT64z8jrbxhCMgn3IwHrzt_KhhvrASXquk1yAVbBAIQmOoIYtCN9TgtENbsAg9iCvtLbB70g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
اصابت موشک های سپاه در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/70959" target="_blank">📅 23:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70958">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
‼️
وضعیت دکل مخابراتی کوهستک سیریک که امشب بهش حمله شد</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/70958" target="_blank">📅 23:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70957">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خود ترامپ، هگزت و بسنت هم پشماشون از این حجم از کله‌خری سپاهیا ریخته
#hjAly‌</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/70957" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70956">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
از بیدگنه هم دوتا موشک شلیک شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/70956" target="_blank">📅 23:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70955">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
شلیک دور جدید موشک های سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/70955" target="_blank">📅 23:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70954">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">من فکر نمی‌کنم ترامپ قبل انتخابات دست به حمله‌ی گسترده‌ای بزنه، سنا تو تصویب بودجه برای جنگ نقش اصلی رو داره نباید بیفته دست دموکرات ها
#hjAly‌</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/70954" target="_blank">📅 23:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70953">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c95b26a1b.mp4?token=tFHEpBIL6oZa7ctHjj15Bjsn1O-a2I6ggcNpuCo-QWrw0GlU79iLn9PCLwKO2eZAn--GsFDNdId0OwPfO1tcIvmlXv6Pv9qTzz-VA9-_bxRItufxcEZOMUR1J0eOebcJabUT0thsvp_qxk9DTb9ck9kEGZ7qdiuUqDEsSulRQs-diCSnf3M6TA4u8NX6UUjm6axP7_LpwzG8SBNSKU0NiWbWexFWAXiyUdjZgRLjP7qjAu0Zwp-n36u8p3cKjFFSaOrg9gw0uFxOQLMa8U1puMLzpCresRaNuxSU6AKPG3iofBqHUvXCAs0zo9lnFtNXDbBkZwlUw0tNi302eGe-Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c95b26a1b.mp4?token=tFHEpBIL6oZa7ctHjj15Bjsn1O-a2I6ggcNpuCo-QWrw0GlU79iLn9PCLwKO2eZAn--GsFDNdId0OwPfO1tcIvmlXv6Pv9qTzz-VA9-_bxRItufxcEZOMUR1J0eOebcJabUT0thsvp_qxk9DTb9ck9kEGZ7qdiuUqDEsSulRQs-diCSnf3M6TA4u8NX6UUjm6axP7_LpwzG8SBNSKU0NiWbWexFWAXiyUdjZgRLjP7qjAu0Zwp-n36u8p3cKjFFSaOrg9gw0uFxOQLMa8U1puMLzpCresRaNuxSU6AKPG3iofBqHUvXCAs0zo9lnFtNXDbBkZwlUw0tNi302eGe-Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هم‌اکنون حملات موشکی سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/70953" target="_blank">📅 22:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70952">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfcd58ff7e.mp4?token=kktPApfwNQd6vNs8PhHLC3a4FBWuyGRSwWZsC1_lUbrN7RB_gD75wF3Nb__5466zl6agro9YnBLKJ9mPGNa8pnsKQ68Ur-KP3kTA239sKIyGPMxoF8RqEk0VSw8nOb4R39J41m0dN1vU10KZZZnxyMAMib4IF_-7xNqXSlJPQsQjkUi19uH7SswTnlvMY2NkmDs86KeWPgPcDaO7lAnh3BbwNWiV19ixrn2R9b_Apw---MCYiWDRkrzXrIbK8J5OZxYQ_roxKBn57qt4dcOPfRU43_cs59YixKVS0ZYK0QM196K2epXmO0-4Wf2UsK6eLA9cxKo7zTBs0eVTaYhg9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfcd58ff7e.mp4?token=kktPApfwNQd6vNs8PhHLC3a4FBWuyGRSwWZsC1_lUbrN7RB_gD75wF3Nb__5466zl6agro9YnBLKJ9mPGNa8pnsKQ68Ur-KP3kTA239sKIyGPMxoF8RqEk0VSw8nOb4R39J41m0dN1vU10KZZZnxyMAMib4IF_-7xNqXSlJPQsQjkUi19uH7SswTnlvMY2NkmDs86KeWPgPcDaO7lAnh3BbwNWiV19ixrn2R9b_Apw---MCYiWDRkrzXrIbK8J5OZxYQ_roxKBn57qt4dcOPfRU43_cs59YixKVS0ZYK0QM196K2epXmO0-4Wf2UsK6eLA9cxKo7zTBs0eVTaYhg9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات موشکی سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/70952" target="_blank">📅 22:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70951">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رسانه های حکومت: آمریکا یه مراسم عروسی تو سیریک رو زده و چن نفر کشته شدند
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/70951" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70950">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">همچنان هیچ ویدیویی از موشک های سپاه تو آسمون کشور های منطقه، منتشر نشده
#hjAly‌</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/70950" target="_blank">📅 22:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70949">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:  اگر ایران پاسخ دهد، انها از بین خواهند رفت  @News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/70949" target="_blank">📅 22:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70948">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اسپویل:
سپاه دوباره موشک می‌زنه و ترامپ هیچ گوهی نمی‌خوره
#hjAly‌</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/70948" target="_blank">📅 22:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70947">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=v854oYm_mM4dgmJxP_3v6mzkZqA7tcEULl2dOJddp9Phf_r3B1Vz8SSkRPXUlARaoR27w7Qd1da8MHLRbVEqrL65wMEd94M3IBWFWk3CEub5QEHaB9gwIeqM0j2PVdKMLKZzlIYXHdBvor6pfUx_JH-XB3TueM5x3eutqrONVQKsvsX9J6Mk10AHyj1vnuLbqCywo5KQTJyEw4HH0yNf1MHHyQb0D2lSBS38JdJ1r5MIb0SK2mcYmYuqklg7cSVK0s48RvdqnxdVUjnOJI6-REg4rYwV20FbZpHqRRUcxZh5Wjgxmc0MmE8B9MjTTOyuGwHWusmZdbweAleXvJVuLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=v854oYm_mM4dgmJxP_3v6mzkZqA7tcEULl2dOJddp9Phf_r3B1Vz8SSkRPXUlARaoR27w7Qd1da8MHLRbVEqrL65wMEd94M3IBWFWk3CEub5QEHaB9gwIeqM0j2PVdKMLKZzlIYXHdBvor6pfUx_JH-XB3TueM5x3eutqrONVQKsvsX9J6Mk10AHyj1vnuLbqCywo5KQTJyEw4HH0yNf1MHHyQb0D2lSBS38JdJ1r5MIb0SK2mcYmYuqklg7cSVK0s48RvdqnxdVUjnOJI6-REg4rYwV20FbZpHqRRUcxZh5Wjgxmc0MmE8B9MjTTOyuGwHWusmZdbweAleXvJVuLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پرتاب ناموفق موشک سپاه تو خمین
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/70947" target="_blank">📅 22:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70946">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
⭕️
🟥
رئیس جمهور ترامپ به خبرنگار فاکس‌نیوز می‌گوید که اگر ایران به حملات اخیر ایالات متحده پاسخ دهد، با پاسخ نظامی بسیار قوی‌تری روبرو خواهد شد و هشدار می‌دهد که اگر درگیری بیشتر تشدید شود، این کشور می‌تواند «کاملاً محو شود».  رئیس جمهور گفت که این حملات سیستم‌های…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/70946" target="_blank">📅 22:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70945">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1cb4c9444.mp4?token=Xq7ZxbHaOeLD16C9a-Scqt6T9CKg8M9C4FRwMbhi7k2-CubFFoIFuPQhGuzkh5QE6wl4mmpysf2ArY_evgd_jg_49H8O9H0unHaLq1Ovtgy-yzxS0Y2ppd6W-QV11yIO6T2acNoyB5-F6-_-eZVm91z_PRK8Ry33-ohrBKQ82j7cNh4HywCZTczrixWgQInqKBghkuSOkSow2Biu53u69IIau9P2uYI2Uing3eKUt9GAVB3yUHE7WAQNCMc8KgSe4gwYoNuCLjFA3HoC8QywbPPpoILBOw-asDvwPEgC-bye7lssGZxryot-pV7tQozlmrxl2_OwcyX_FcUiHym99AdmwLbxgVHLvgmJYjLhQMzb1mc73nujCPuo4_YuWlSrqq0vvwC8mBHsNMOZsmHqZi6OX8XevoJn7-gNogF8gq_a5WhVHtZn4mDtA8O_gIBfFLYF4jFQlvew2GW03vj5Vwg-8_WXbFPWm1Q91cKkXzrlczkpBj2yEZmxJEf9bz7x6H_FAILhqE7S22jT7UO78dei4iO01IGkG1-x_qUaaJVhEV-lFv7Eq6i5ryaFPdpzLCmuOYDxbhM758ff1KcA9y7RekmqZxFOgS9t663Mkg4zGM6_Z-cUdUC-uf4y_aCVw6G8YRU_XVhrWb2paPqrEGvvS2pUBA-iw8KYysFA6cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1cb4c9444.mp4?token=Xq7ZxbHaOeLD16C9a-Scqt6T9CKg8M9C4FRwMbhi7k2-CubFFoIFuPQhGuzkh5QE6wl4mmpysf2ArY_evgd_jg_49H8O9H0unHaLq1Ovtgy-yzxS0Y2ppd6W-QV11yIO6T2acNoyB5-F6-_-eZVm91z_PRK8Ry33-ohrBKQ82j7cNh4HywCZTczrixWgQInqKBghkuSOkSow2Biu53u69IIau9P2uYI2Uing3eKUt9GAVB3yUHE7WAQNCMc8KgSe4gwYoNuCLjFA3HoC8QywbPPpoILBOw-asDvwPEgC-bye7lssGZxryot-pV7tQozlmrxl2_OwcyX_FcUiHym99AdmwLbxgVHLvgmJYjLhQMzb1mc73nujCPuo4_YuWlSrqq0vvwC8mBHsNMOZsmHqZi6OX8XevoJn7-gNogF8gq_a5WhVHtZn4mDtA8O_gIBfFLYF4jFQlvew2GW03vj5Vwg-8_WXbFPWm1Q91cKkXzrlczkpBj2yEZmxJEf9bz7x6H_FAILhqE7S22jT7UO78dei4iO01IGkG1-x_qUaaJVhEV-lFv7Eq6i5ryaFPdpzLCmuOYDxbhM758ff1KcA9y7RekmqZxFOgS9t663Mkg4zGM6_Z-cUdUC-uf4y_aCVw6G8YRU_XVhrWb2paPqrEGvvS2pUBA-iw8KYysFA6cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🟥
رئیس جمهور ترامپ به خبرنگار فاکس‌نیوز می‌گوید که اگر ایران به حملات اخیر ایالات متحده پاسخ دهد، با پاسخ نظامی بسیار قوی‌تری روبرو خواهد شد و هشدار می‌دهد که اگر درگیری بیشتر تشدید شود، این کشور می‌تواند «کاملاً محو شود».
رئیس جمهور گفت که این حملات سیستم‌های راداری در جنوب غربی ایران در نزدیکی تنگه هرمز را که در حال بازسازی بودند، هدف قرار داده است و افزود که ناو هواپیمابر جورج واشنگتن کاملاً مجهز است تا در صورت نیاز به عملیات خود ادامه دهد.
ترامپ همچنین احتمال توافق جدید با ایران را رد کرد و گفت تلاش‌های دیپلماتیک قبلی شکست خورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/70945" target="_blank">📅 21:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70944">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری فارس از آغاز حملات موشکی سپاه به مواضع آمریکا در منطقه خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/70944" target="_blank">📅 21:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70943">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
⭕️
🇺🇸
پرزیدنت ترامپ:
"اگر آنها تلافی کنند، ضربه بسیار سخت‌تری خواهند خورد. و اگر دوباره این کار را انجام دهند، دیگر نخواهند بود."
"آنها متوقف نمی‌شوند. آنها دیوانه و احمق هستند."
"آنها سعی کردند رادار خود را بازسازی کنند زیرا نمی‌توانند چیزی ببینند. ما صبر کردیم تا تقریباً ساخته شود و سپس به آن ضربه زدیم."
"من فکر می‌کنم توافق با آنها ارزش کاغذی را که روی آن نوشته شده است، ندارد. ما به آنها فرصت‌های زیادی دادیم."
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/70943" target="_blank">📅 21:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70942">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ در گفتگو با فاکس‌نیوز:
اگر ایران به حملات آمریکا واکنش‌های مکرر نشان دهد، ممکن است «به‌عنوان یک کشور کاملاً نابود شود».
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/70942" target="_blank">📅 21:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70941">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=p3nolfgAEKL6Hubh0LwOqhEvF0uVuEpOc8UuCtz3lrEklNmLqqUSJj9LB-GdVHV51D_7rQP4E0b6xEGoH-vSy1jETkiet0LS9fESWbN_fTTt4buTaRE663oeGtOAqB6BSKlRzh4ciNPSWiKageqxDxac6iFwwiBMbEByOOwRhxCx4k6kqVdsC7Xx-krqxHJhUbBmJb7gg97KPXuBe8LuLEX7ydJ3pbL3m6hse799mRs3Q7r5luXmZtXdq5VS0f0LuSZQISO6S1OZIluqN21Vl0EGNjXj9ZIshS3jIrdtzIHuDVVFVrnKYuD4g91XoBz32ku88-N9ZuVd3jyvIObf8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=p3nolfgAEKL6Hubh0LwOqhEvF0uVuEpOc8UuCtz3lrEklNmLqqUSJj9LB-GdVHV51D_7rQP4E0b6xEGoH-vSy1jETkiet0LS9fESWbN_fTTt4buTaRE663oeGtOAqB6BSKlRzh4ciNPSWiKageqxDxac6iFwwiBMbEByOOwRhxCx4k6kqVdsC7Xx-krqxHJhUbBmJb7gg97KPXuBe8LuLEX7ydJ3pbL3m6hse799mRs3Q7r5luXmZtXdq5VS0f0LuSZQISO6S1OZIluqN21Vl0EGNjXj9ZIshS3jIrdtzIHuDVVFVrnKYuD4g91XoBz32ku88-N9ZuVd3jyvIObf8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیویی دیگر از موشک سپاه که در خمین سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/70941" target="_blank">📅 21:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70940">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91af576da.mp4?token=hCLkGs4JlIq-AEory4c4kgO-zqdSDFPbdW0O5qev5aDQ8h46H9dzPVn-W3eemQRJVfSS6A_AlDdxTTraxqcc8cnepOfQeXxkLdEeHP4AYYvNMlSkohvkL-C83RtE_0HScMr-LuSDsg9-TsQPPK-mQ2zqEtkGag12yPnghHiWZNYAC6aS4gMwW7-J2jqHedcCBBdWwJYtRlwDgFtWLEKC_4ApN6emYnRB_3F9voGc0luSQ98Hpa3qcSGozSfLQCU3d-0DwnOM5DL1FT88N-8dWtIWbpsw7qjxP9HXrN6paE9hTZFT_AjUyYHwhi9LfvE2KkFrzvFi8kPRlR5syhfnOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91af576da.mp4?token=hCLkGs4JlIq-AEory4c4kgO-zqdSDFPbdW0O5qev5aDQ8h46H9dzPVn-W3eemQRJVfSS6A_AlDdxTTraxqcc8cnepOfQeXxkLdEeHP4AYYvNMlSkohvkL-C83RtE_0HScMr-LuSDsg9-TsQPPK-mQ2zqEtkGag12yPnghHiWZNYAC6aS4gMwW7-J2jqHedcCBBdWwJYtRlwDgFtWLEKC_4ApN6emYnRB_3F9voGc0luSQ98Hpa3qcSGozSfLQCU3d-0DwnOM5DL1FT88N-8dWtIWbpsw7qjxP9HXrN6paE9hTZFT_AjUyYHwhi9LfvE2KkFrzvFi8kPRlR5syhfnOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نقص فنی موشک بالستیک سپاه پاسداران در آسمان خمین
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70940" target="_blank">📅 21:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70939">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFO43rfwskHAAEK-uomn8LU22bZCzmHSXYDtVrOzlQ-BcjKSAB3-bqfs3l0QlgJUNJAarpjmIvJRek1NE6xiLGBbBe_Q98jKpPCHquV00dsy_BZfXsIEyBI1CtqLs4vHGTmCOpvxeYAb4IMN4K6LGZ-rzcBLft2AzPGyxbA3d_U78F0QU1ett3PuwG1dsuKUo6oHRzTRMeXq0qkv16_kM5-1hQrmm-klLZUiAr-ADkSlXWeauV4TzZMQeZlxFEpo0e6dwrypTFoQVKBhC-6gheSUWO8ni4ZexU8CTNH3NXGU6y5DW0Y-YewzMVAiqdfGgKj2RvbEiKSL934w-Oar6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ستاد کل نیروهای مسلح: هزینه سنگینی بر دشمن آمریکایی تحمیل خواهیم کرد
🔴
ستاد کل نیروهای مسلح و قرارگاه مرکزی خاتم‌الانبیا:
در پاسخ به تجاوز هوایی ارتش آمریکا به نقاطی در سیستان و بلوچستان و هرمزگان، نیروهای مسلح جمهوری اسلامی ایران ضربات کوبنده و شکننده ای را به دشمن زبون و شرور آمریکایی وارد خواهند نمود.
ارتش تروریست آمریکا هر چقدر اصرار بر شرارت در منطقه داشته باشد باید خسارات بیشتر و سنگین تری را تحمل نماید.
بارها اعلام نموده ایم و اراده کرده ایم تحت هیچ شرایطی از حقوق ملت قهرمان ایران کوتاه نخواهیم آمد و هزینه های سنگینی را بر دشمن آمریکایی تحمیل خواهیم نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70939" target="_blank">📅 21:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70938">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
گزارش انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70938" target="_blank">📅 21:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70937">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbdYxlsycIkIaF71VRfngHu4GdeFumfNOF-WKI-iLpipd9SOy4Kco1ZZRZhFvVS8DVoyLYkllDYTU94uZnIQn-w6C-69myHKwAr3nz__WcoufJyzTkropiPIK_B0VqoWCxCVqlrwA2Cr6IxP2ILSmmrrkSE-7sMcBeaHzagXmJRji1wf3eq0OH_iRRMkNzv_NGqOPFOcobSa7L-nNrpwZaSnAtyGYbm9xs0DwjSrvNQnC5YJ-1lcd6oGtsIajForu_PuqFoUxznWYCYnhHVMuP24y1KYuW6ZUvGxStqgqBN08qzSQvf3E_DdH0tfAeTnzf04H3yPxyPI-_B78A-w_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:ایالات متحده همین حالا در حال هدف قرار دادن مواضع ایران در نزدیکی تنگه هرمز است.
🔴
این حملات گسترده و سهمگین هستند و در واکنش به دو اقدام صورت می‌گیرد:
نخست، تلاش نافرجام ایرانی‌ها برای کارگذاری مین‌های دریایی در تنگه‌ای که در حال حاضر فاقد هرگونه مین است (مین‌ها کاملاً پاکسازی یا منهدم شده‌اند!)؛
و دوم، شلیک هشت موشک از سوی ایران به سمت پایگاه نظامی ما در اردن که همگی با موفقیت سرنگون شدند.
اگر ایرانِ شکست‌خورده بخواهد به این حمله کاملاً موجه پاسخ دهد، بار دیگر با ضرباتی بسیار شدیدتر و سنگین‌تر مواجه خواهد شد؛
🔴
اما آن حمله، بزرگترینِ حملات نخواهد بود، چرا که حمله اصلی در کمین است و پس از پایان آن، چیز زیادی از جمهوری اسلامی ایران باقی نخواهد ماند!
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70937" target="_blank">📅 21:09 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
