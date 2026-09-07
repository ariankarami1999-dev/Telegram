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
<img src="https://cdn4.telesco.pe/file/RoZXVF4XL_9VAl7bGhhd-jQs7IyXEonstcbFuo-I8GrSh385wYJeuGojLacGxQNtyNzZDjL-iiAhg73ZKSQZ_mB1ySj22HZ-XpnJGiapxLhRakwcGAyPOOxVrz9294C-CljMKZbM6cbCvuxkCiiZlMGuniWiy1LaRy4wN8e-5yPEVjGUPOFDYBp-l4snIE6orhOVDevo0w4e0SNSwMpvs8HTkT5xd5ttCBMHZ1QNuZfVxx8lEXxRJMPFXc_cG3Qs3hSBvCsNBKRa-pltvZxnkVLGZo4sLfxz_9lT5kZ8QYyPOLTVTaXuv5KhVEKLlUjANMwMRRoUVUQlUxDj630anw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 448K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 19:42:49</div>
<hr>

<div class="tg-post" id="msg-22509">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ : در انتخابات میان دوره ای به پیروزی قاطع دست خواهیم یافت و آمریکا را نجات خواهیم داد‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/withyashar/22509" target="_blank">📅 18:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22508">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/688ebf7bb6.mp4?token=Hw6eVqI_aNRZFG9o9w14gfn6LgA2pfASDw003VUP1Qq_bKiJ5kaP-iBIOVbDGn1EQjcDU72tYms-cW7xaFDa-dAI3KSxQq7FPC_LTSXnxzcEjcEixfEM6tABq9IW2eXK3pGrvBooryC6KLTLjmlJW5AWGbuqPTkAVjgfS1rBNUYsFMTA8YDr4-3Bx3sKJH8_JwrKiLwMsmSel-w_SULHmUTSVCQEaJUrVzUdqBo2UZXyY5EbEAzi_qleobbHFTG7HojcD65oXJs_TwRL_idXLb-vMX2iIkYN6yRFsCEeZrZYgS7S090Emp6TWI4wjEFNh5tS0JjnTnRgybdJ2f-0kR9XNPbMgMLvw9nOueDHEnB7VXW_yPulBRocIiSq7FTpi5xXDjMT5dCaNARxKAZmapRUMPr7azaOHqsaPyC7EqyDkqPaxM_ddLRc_XZehmgmw-ctpaEW19wVgnklh69H_ag_RV9-yyuvfFxqVSyGiTcjPcv-E6IE1L9zIXgQocgktMvY-DMk99XsJlL_i8GE3Du4m1EJtzvAAAYPaY3UDULkQlicsCuw3DpiaztnhML1jDeIC8chheypDgDX8Aupl_iu-22K_6ZfVb8WkNC0Vu_tQlyWXtXyc3tvimjyWxucq3_6_1YAeMUnY8AuDho6JNX4FNH83wgDZvpYA8Q9TWI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/688ebf7bb6.mp4?token=Hw6eVqI_aNRZFG9o9w14gfn6LgA2pfASDw003VUP1Qq_bKiJ5kaP-iBIOVbDGn1EQjcDU72tYms-cW7xaFDa-dAI3KSxQq7FPC_LTSXnxzcEjcEixfEM6tABq9IW2eXK3pGrvBooryC6KLTLjmlJW5AWGbuqPTkAVjgfS1rBNUYsFMTA8YDr4-3Bx3sKJH8_JwrKiLwMsmSel-w_SULHmUTSVCQEaJUrVzUdqBo2UZXyY5EbEAzi_qleobbHFTG7HojcD65oXJs_TwRL_idXLb-vMX2iIkYN6yRFsCEeZrZYgS7S090Emp6TWI4wjEFNh5tS0JjnTnRgybdJ2f-0kR9XNPbMgMLvw9nOueDHEnB7VXW_yPulBRocIiSq7FTpi5xXDjMT5dCaNARxKAZmapRUMPr7azaOHqsaPyC7EqyDkqPaxM_ddLRc_XZehmgmw-ctpaEW19wVgnklh69H_ag_RV9-yyuvfFxqVSyGiTcjPcv-E6IE1L9zIXgQocgktMvY-DMk99XsJlL_i8GE3Du4m1EJtzvAAAYPaY3UDULkQlicsCuw3DpiaztnhML1jDeIC8chheypDgDX8Aupl_iu-22K_6ZfVb8WkNC0Vu_tQlyWXtXyc3tvimjyWxucq3_6_1YAeMUnY8AuDho6JNX4FNH83wgDZvpYA8Q9TWI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تفنگداران دریایی و ملوانان ناو آبراهام لینکلن، مشغول عشق و حال در کلابهای  پاتایا، تایلند. @WarRoom</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/withyashar/22508" target="_blank">📅 18:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22507">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ در تروث ویدیو برنامه مارک لوین را بازنشر کرد: در این گفت‌وگو، ویکتور دیویس هنسون ترامپ را «معکوس‌کننده‌ی انقلاب» می‌نامد؛ یعنی رئیس‌جمهوری که قصد دارد روندی را که طی۵۰سال آمریکا و سیاست خارجی آن را تغییر داده، معکوس کند. در مورد ایران نیز تأکید می‌شود…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/withyashar/22507" target="_blank">📅 18:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22506">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏خبرگزاری عراقی «بغداد الیوم» گزارش داده بیش از ۱۵۰ نفر آزادی خواه ایرانی به محل اسکان دانشجونماهای عراقی گروه تروریستی «حشدالشعبی» حامی جمهوری اسلامی در دانشگاه سمنان هجوم برده و شماری از آنان را مورد ضرب‌وشتم قرار دادند. تعدادی زخمی شدند و ادعا کرده پول،…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/22506" target="_blank">📅 18:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22505">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">الجزیره: ایران به آمریکا اطلاع داده که در صورت اشغال کامل تپه علی‌الطاهر توسط اسرائیل، مستقیماً وارد عمل می‌شود، این منطقه محل استقرار تاسیسات مهم و استراتژیک حزب‌الله است.
@WarRoom</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/withyashar/22505" target="_blank">📅 17:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22504">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سی‌بی‌اس نیوز:
وزارت دادگستری آمریکا در حال احیای یک قانون قدیمی مربوط به
توقیف کشتی‌ها و محموله‌های نفت ایران
است تا بتواند نفتکش‌های ایرانی را هدف اقدامات حقوقی قرار دهد. این موضوع بخشی از فشار اقتصادی آمریکا بر تهران است.
@WarRoom</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/22504" target="_blank">📅 17:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22503">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dd84c2849.mp4?token=LmZaUfFR0CFQmLy6xznsmUe2i7nkO6JdWGLXuJ6niqouoH0h-7Yav_ZwU81RUT5lgYrim1fQZIurD2i2t7hcHEUGCyV_0XJaSQSamlx6zv5xTk-FLuaK_uRIRueggomqeHxEJJZhWIhlNmevtm8a0XtzhokSE7igjCWrS8pbdEIIIbN8xSwAv8vCvcAizur-K6YKFbIaLh0_0GThd5Ue1ry835htLXh7vFLb4Fr8v_6G7UQzKuzXtWijN9Xa7spYnwCS5DlaFc0GdoHkdA7NbsoGoEKtxApLU_eQItXZmGPXwFiJ4axXoDyk_4L6E-RPk7ebQ0tKuNe8gby32IthsQZgDws-relZAiKGeos-JskYUXmHxC3mUCQzWOGj7sdFoVjy__AfiLVfn8CC4WdYr4DMTmGsOUsGJvSw2GudbJse0eI1aztU35_g12JZ-oKBAU9wp5IE4L6AgIhxsQzT268k7D2Vo8Bck-l8-m-9hUK9sNNh8k5uQ6Iu9WOFqx8HznmEfAGcdH1exbaXneoPaizXU47Egxft7IlqI_p0vAGU8EOUyRy2A1c3yGc45lUWVNdyyCEj9-RWjX1PNwLlzCWDHuc3z9BwDMBXn8eLoBDHY6PwyF5S4syRdZgbZTdUMGhT-_WtB3D5JtF6VMoI0IK-2eCLQ4l3Gop6nwWRlhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dd84c2849.mp4?token=LmZaUfFR0CFQmLy6xznsmUe2i7nkO6JdWGLXuJ6niqouoH0h-7Yav_ZwU81RUT5lgYrim1fQZIurD2i2t7hcHEUGCyV_0XJaSQSamlx6zv5xTk-FLuaK_uRIRueggomqeHxEJJZhWIhlNmevtm8a0XtzhokSE7igjCWrS8pbdEIIIbN8xSwAv8vCvcAizur-K6YKFbIaLh0_0GThd5Ue1ry835htLXh7vFLb4Fr8v_6G7UQzKuzXtWijN9Xa7spYnwCS5DlaFc0GdoHkdA7NbsoGoEKtxApLU_eQItXZmGPXwFiJ4axXoDyk_4L6E-RPk7ebQ0tKuNe8gby32IthsQZgDws-relZAiKGeos-JskYUXmHxC3mUCQzWOGj7sdFoVjy__AfiLVfn8CC4WdYr4DMTmGsOUsGJvSw2GudbJse0eI1aztU35_g12JZ-oKBAU9wp5IE4L6AgIhxsQzT268k7D2Vo8Bck-l8-m-9hUK9sNNh8k5uQ6Iu9WOFqx8HznmEfAGcdH1exbaXneoPaizXU47Egxft7IlqI_p0vAGU8EOUyRy2A1c3yGc45lUWVNdyyCEj9-RWjX1PNwLlzCWDHuc3z9BwDMBXn8eLoBDHY6PwyF5S4syRdZgbZTdUMGhT-_WtB3D5JtF6VMoI0IK-2eCLQ4l3Gop6nwWRlhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کریس رایت , وزیر انرژی امریکا
:
ماموریتی که نیروی دریایی ما انجام می‌دهد فقط اسکورت کشتی‌ها نیست ! بلکه ، جلوگیری از خروج هرگونه نفت یا محصولات صادراتی جمهوری اسلامی میباشد.
@WarRoom</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/22503" target="_blank">📅 16:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22502">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4abd87594.mp4?token=ikg10pvffh72wfNFb6qHdwQlw0dPxYA6dp9bKaIbIQKLMsthAgCxcSZPeh4ustJ3WILWiWbfbgoCEMXHWs5c_CqbeuE_TviZJLS4qqO8ykliuxGDNU91hYmqF68almn-i3LlDo6QSnSgnash0XvNHFoxvxKOPzl7Poa6_Yv7craj4ZLoY5dCaSLRq8CDqlO5z8FdTiwp1k2rVwYv_eEy5Ev5roplBnT6ZBk0uEZokG9UaYB_8-l9cM2w5x3Ql9a-KDzA-VloYfbNNZARGtgXmm4jBPG681eKvplFVCu9F4QpgotZG_zFwbKS8dutIxK4N1VGykZs6XAokUBlT8AsnERH49cHUv8DdSfbh1LugA39W8dmN0hBnibBZbE7Ak1syQWaNHGlLSGu_jRKQBUmMquYhTcXnEF5B_dlA6cHtmizyvb2o7QDiwbvcXHlL-Uh4YzWMqlXJY09Sh0a0_dPNsbsFbP9DdD5qu1_W-XmmDlY-kA6h7L6TrGjMYd6fMK5LHOLl3n8V2b_3_zF-bJD8HxK68i_DFtTh6WkGTBs3Y1ElWZbTf1zeEA3IvoR-6esJEH6_znsd6tnHnTgEKno_3raJDqs0h5jCzThUhLr3_DsIl3WxcpWxUFMYnVdvT9z6cBE0B_nWE_uLNuJW5tZIpqxAfUYr1XFacRN_EZ-te8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4abd87594.mp4?token=ikg10pvffh72wfNFb6qHdwQlw0dPxYA6dp9bKaIbIQKLMsthAgCxcSZPeh4ustJ3WILWiWbfbgoCEMXHWs5c_CqbeuE_TviZJLS4qqO8ykliuxGDNU91hYmqF68almn-i3LlDo6QSnSgnash0XvNHFoxvxKOPzl7Poa6_Yv7craj4ZLoY5dCaSLRq8CDqlO5z8FdTiwp1k2rVwYv_eEy5Ev5roplBnT6ZBk0uEZokG9UaYB_8-l9cM2w5x3Ql9a-KDzA-VloYfbNNZARGtgXmm4jBPG681eKvplFVCu9F4QpgotZG_zFwbKS8dutIxK4N1VGykZs6XAokUBlT8AsnERH49cHUv8DdSfbh1LugA39W8dmN0hBnibBZbE7Ak1syQWaNHGlLSGu_jRKQBUmMquYhTcXnEF5B_dlA6cHtmizyvb2o7QDiwbvcXHlL-Uh4YzWMqlXJY09Sh0a0_dPNsbsFbP9DdD5qu1_W-XmmDlY-kA6h7L6TrGjMYd6fMK5LHOLl3n8V2b_3_zF-bJD8HxK68i_DFtTh6WkGTBs3Y1ElWZbTf1zeEA3IvoR-6esJEH6_znsd6tnHnTgEKno_3raJDqs0h5jCzThUhLr3_DsIl3WxcpWxUFMYnVdvT9z6cBE0B_nWE_uLNuJW5tZIpqxAfUYr1XFacRN_EZ-te8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
حاوی الفاظ رکیک ولی به جا
,
دقت فرمایید.
⚠️
جمهوری اسلامی در یک تصویر
، خودش لنگان لنگان با لباسی ژولیده، بدنی نحیف و لاغر،خرکش بدون تعادل همه پرچم ها را یکجا را بر دوش میکشد
😂
@WarRoom</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/22502" target="_blank">📅 15:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22501">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">روسیه و کره شمالی نخستین پل ارتباطی میان دو کشور را افتتاح کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/22501" target="_blank">📅 15:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22500">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">الجزیره: حملات هوایی اسرائیل به جنوب لبنان، از سر گرفته شده است. @WarRoom</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/22500" target="_blank">📅 15:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22499">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b12d040c7.mp4?token=Q2hEVipXJ0S_7_QHqK-rM68xCVfkVAhjqeviDu4TIHwwPii5Ka84KzHBdic-arnQBf0WCcA80vA0i6l2kJpOHNwfRwBwxbqCznsjWn_Ctad54NOdyJaS5OPLND6L-TSsM4egn72PbikEsG1JlpyY8Nt6pCpw-Sc2Jwsne2Ip6nZCQlWw0rpFDSrL6ZpeeWH15S4TlOHDkHw8biCCTX96aykV6jub3WldZioyQ1GzzCJstxrQCaN7e6s59-l0oWtsPIQiWGJquP-64aCHsdZHoVXEyrKXrD9jBKzhv18GeT-YAB6MKZePvkshM0e162O7DAIhONAW8dyNTDVCCLG3Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b12d040c7.mp4?token=Q2hEVipXJ0S_7_QHqK-rM68xCVfkVAhjqeviDu4TIHwwPii5Ka84KzHBdic-arnQBf0WCcA80vA0i6l2kJpOHNwfRwBwxbqCznsjWn_Ctad54NOdyJaS5OPLND6L-TSsM4egn72PbikEsG1JlpyY8Nt6pCpw-Sc2Jwsne2Ip6nZCQlWw0rpFDSrL6ZpeeWH15S4TlOHDkHw8biCCTX96aykV6jub3WldZioyQ1GzzCJstxrQCaN7e6s59-l0oWtsPIQiWGJquP-64aCHsdZHoVXEyrKXrD9jBKzhv18GeT-YAB6MKZePvkshM0e162O7DAIhONAW8dyNTDVCCLG3Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ اگه را داشت ماشین ریاست جمهوری رو هم الان معاملشو بسته بود ، یه ایرانی هم گذرموقتش میکرد میاورد ایران دور دور
😂
@WarRoom</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/22499" target="_blank">📅 15:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22498">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یک منبع اسرائیلی به i24NEWS: مشخص نیست جرقه‌ای که باعث شعله‌ور شدن اعتراض در تهران شود چه زمانی خواهد بود، اما خواهد آمد.
@WarRoom</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/22498" target="_blank">📅 14:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22497">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فایننشال تایمز گزارش داد
تأسیسات نفتی شرکت آرامکو در منطقه جازان عربستان سعودی امروز هدف حمله جدید قرار گرفته‌اند.
میزان خسارت در حال بررسی است و به گفته یک منبع مطلع، ابعاد حمله با حمله ماه گذشته به این تأسیسات مشابه بوده است.
جازان به‌دلیل نزدیکی به مرز یمن، طی ماه‌های اخیر چندین بار هدف حملات حوثی‌ها قرار گرفته است. آرامکو در حمله قبلی اعلام کرده بود اختلال ایجادشده
تأثیر قابل‌توجهی بر عملیات یا وضعیت مالی شرکت نداشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/22497" target="_blank">📅 14:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22496">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommorteza</strong></div>
<div class="tg-text">علاالدین داشتن اعتصاب میکردن اطلاعات ریخت بالا گفت باز کنید یا بازداشت میشین</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/22496" target="_blank">📅 14:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22495">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromyasaman sh</strong></div>
<div class="tg-text">یه دونه‌ای
دلم گرفته بود داشتم گریه می‌کردم. وویست رو باز کردم گفتی زارتان زورتان خندیدم.</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/22495" target="_blank">📅 14:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22494">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2827c98c29.mp4?token=R7R3FhYYl9EpgX2aqNCHo8HsWPMj3mjaT3HmCh7ca_DexhhHWdhQi_ZSFqrMM7r09YRcDSiawG3vTTTG2qHjXXMGppNUCSbPrhw2MqhBOmLBImfEN1aEQwbX0J5iOoApi0S-HKL8UnrbuvcS4UW-dnxVdorfkPf3PKzLmshyzdfXuOt0ZgquQSDyQ8bQv_l249IzI21IOQA5fw7Kip3AKaScBPV7z6nGArPxEv57nLHw-23YhuQW0yP9OUvsOm4yanCZexHhECE4WLysOqIRErNAJAiL7rjiOrb-mzWOga62LvJb8vdv8yj3sA9cYPDZoD8YuWY1AnaWzXY5isGEBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2827c98c29.mp4?token=R7R3FhYYl9EpgX2aqNCHo8HsWPMj3mjaT3HmCh7ca_DexhhHWdhQi_ZSFqrMM7r09YRcDSiawG3vTTTG2qHjXXMGppNUCSbPrhw2MqhBOmLBImfEN1aEQwbX0J5iOoApi0S-HKL8UnrbuvcS4UW-dnxVdorfkPf3PKzLmshyzdfXuOt0ZgquQSDyQ8bQv_l249IzI21IOQA5fw7Kip3AKaScBPV7z6nGArPxEv57nLHw-23YhuQW0yP9OUvsOm4yanCZexHhECE4WLysOqIRErNAJAiL7rjiOrb-mzWOga62LvJb8vdv8yj3sA9cYPDZoD8YuWY1AnaWzXY5isGEBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : مردم شریف ایران، شرایط ایمنی حمل‌ونقل کشور به‌شدت نگران‌کننده شده است.
در بخش هوانوردی، گزارش‌هایی از اختلال سامانه‌های ناوبری گزارش شده همچنین بعد از‌جنگ اکثر سامانه های راداری نابود شده اند و از ترس حملات خاموش کردن عمدی ترانسپوندر برخی هواپیماها منتشر شده است؛ موضوعی که می‌تواند شناسایی و تفکیک هواپیماها را برای کنترل ترافیک هوایی دشوار کند و خلبانان در موارد بسیار بصورت چشمی هدایت را انجام میدهند ، در ویدئوی تازه در این رابطه نیز یک هواپیمای کاسپین در فاصله‌ای حدود ۳۰۰ متری از یک هواپیمای تابان عبور کرده است.
در جاده‌ها نیز وضعیت بدتر است فرسودگی ناوگان و مشکلات نگهداری به علت هزینه بسیار بالا سرویس ، خطرات جدی ایجاد کرده است. تنها در تازه‌ترین حادثه، نقص سیستم ترمز یک تانکر حامل بنزین در محور سنندج–همدان باعث برخورد با خودروهای دیگر و آتش‌گرفتن تانکر شد؛ ۱۱ نفر در این حادثه جان باختند و ۷ نفر مصدوم شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/22494" target="_blank">📅 14:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22493">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نتانیاهو: ما به نابودی خرابکاران، پیگیری کسانی که آن‌ها را اعزام می‌کنند و تخریب زیرساخت‌های تروریسم در کرانه باختری ادامه خواهیم داد. @WarRoom</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/22493" target="_blank">📅 13:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22492">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نتانیاهو: ما به نابودی خرابکاران،
پیگیری کسانی که آن‌ها را اعزام می‌کنند
و تخریب زیرساخت‌های تروریسم در کرانه باختری ادامه خواهیم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/22492" target="_blank">📅 13:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22491">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">آمریکا و اتحادیه اروپا در تلاشن شورای حکام آژانس بین‌المللی انرژی اتمی قطعنامه‌ای تصویب کنه که پرونده هسته‌ای ایران رو به شورای امنیت سازمان ملل ارجاع بده.
جمهوری اسلامی هم تهدید کرده که اگه این کارو انجام بدید، جواب متقابل میدیم. بالاخره از ان‌پی‌تی خارج میشن.
پیمان NPT در سال
۱۹۶۸
برای جلوگیری از گسترش سلاح‌های هسته‌ای ایجاد شد و در
۵ مارس ۱۹۷۰
به اجرا درآمد. ایران
از دوره پهلوی
عضو NPT بوده و جمهوری اسلامی در سال ۱۹۷۹ از این پیمان خارج نشد و عضویت ایران ادامه پیدا کرد
@WarRoom</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/22491" target="_blank">📅 13:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22490">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/22490" target="_blank">📅 13:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22489">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5pITdcVjxiF3hep_uNhVZ-9g3oItQZy9F41Cni7W8mk0-UtvF_1MoWoPD2LUEOz-f8uGlygSAXH73_czYeMtrYQjeCuNzMiQsGU09NHpti5XOrrfPRrNFbHJXe7MjqqHrCVb1Td5DM5WbYolD4T9jT3y1-WFCFrE90GZvTpomF7yFHHUv1CtPKa5bfIbWCR4vfZOdM-k5pGAjS3G60gyL_uAmPfJ7l8xQ9p8jvR7Isrh4QlRdHlhM7ZSGPtRRiLmMNxQqj52wUL061rxQ3OEU2Na8katiUaFKvWul1Es5WuJVDkwbPQxNwg8Q8Dxu9aVnXXu2CyUwksVMmpn3YSqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث ویدیو برنامه مارک لوین را بازنشر کرد:
در این گفت‌وگو، ویکتور دیویس هنسون ترامپ را
«معکوس‌کننده‌ی انقلاب»
می‌نامد؛ یعنی رئیس‌جمهوری که قصد دارد روندی را که طی۵۰سال آمریکا و سیاست خارجی آن را تغییر داده،
معکوس کند
. در مورد ایران نیز تأکید می‌شود که ترامپ برخلاف سیاست رؤسای جمهور پیشین،
به دنبال مهار موقت جمهوری اسلامی نیست، بلکه می‌خواهد تهدید اصلی رژیم را از میان ببرد
؛ به‌ویژه
توان هسته‌ای و موشکی و ظرفیت آن برای تهدید آمریکا و متحدانش
. هنسون این رویکرد را بخشی از همان
«معکوس‌کننده‌ی انقلاب» گسترده‌تر ترامپ
می‌داند؛ یعنی
شکستن سیاست‌های گذشته و بازگرداندن ابتکار عمل به آمریکا
. نکته امیدوارکننده برای مردم ایران این است که در این نگاه،
جمهوری اسلامی صرفاً یک حکومت مزاحم برای مذاکره و مهار نیست، بلکه یک تهدیدی است که باید قدرت آن از بین برود.
این گفت‌وگو همچنین بر این ایده تأکید دارد که در صورت
تضعیف قدرت رژیم، مردم ایران و نیروهای مخالف جمهوری اسلامی می‌توانند نقش مهمی در تغییر آینده کشور داشته باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22489" target="_blank">📅 13:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22488">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbH4gfxSkgq19uS9IL7xQ3LjU3JsFja2xzz5hrROawnQgtP-KHl_-xZSfIx0qbAr2dAvfmKoGhgfccdUIVDhKplKSReWSeAsURSuMwZcmfVXZxswHeshbhLk3cIb9KLPkkVWzjujANnRlMSy2oNukmkO2miiMCtjJ-OeZbH1yBqSXqzhteLTHYu4H-GpqPlvhsFIMCBNM9buavB_RI_YQGl_-ghR6skcaEEKFDJJKwHpDQMQGRLpnUMZgdY2U8LjtEqDB5X1j7kynmj59gipVwDCquUK0YaTMw53jgM1q6CId67Dw9dICmFvk7QbgMH3uX6r1h0Kzb4rOY_Wl-GWLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث و نظارت بر نابودی قایقهای تندرو
@WarRoom</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/22488" target="_blank">📅 13:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22487">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dbc57d78d.mp4?token=gIG_GbIxgdVdX06EMo-BIo78zrWlxr9PM3p5UyvCj8gA6zINVvFXk8VEnM38yXkXUJBG0MNg06HJdeM0IHBu5dwHijheluwW5HIcC0Ti6PkvaI9EHWTfR7g9bOqRL_sVnlZCSuySsvK3WCbSjpHbfOG42ZvUMGLOuelycmr-XR7KNu2pW_M4IeU-UPhTohMgjo3NW0iUC2ryUOpe-29I7MhpuFuxa2yx8qlWQC1LFCwM4VViX7FvcCF96cbHhCTUM3wRghaH8ukKOeV0x7iDInjlTieciwPpcTKhz2izmlc2NeE02cHQYUcph6pgiHmkmN1hz991yWzeu6bm2ZzVWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dbc57d78d.mp4?token=gIG_GbIxgdVdX06EMo-BIo78zrWlxr9PM3p5UyvCj8gA6zINVvFXk8VEnM38yXkXUJBG0MNg06HJdeM0IHBu5dwHijheluwW5HIcC0Ti6PkvaI9EHWTfR7g9bOqRL_sVnlZCSuySsvK3WCbSjpHbfOG42ZvUMGLOuelycmr-XR7KNu2pW_M4IeU-UPhTohMgjo3NW0iUC2ryUOpe-29I7MhpuFuxa2yx8qlWQC1LFCwM4VViX7FvcCF96cbHhCTUM3wRghaH8ukKOeV0x7iDInjlTieciwPpcTKhz2izmlc2NeE02cHQYUcph6pgiHmkmN1hz991yWzeu6bm2ZzVWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادای احترام یکی از آسیب دیدگان چشمی به ناو هواپیمابر آبراهام لینکلن در تایلند
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22487" target="_blank">📅 12:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22486">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گزارش های
تایید نشده
از منهدم کردن یک کشتی جدید در
خارگ
توسط امریکا
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/22486" target="_blank">📅 12:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22485">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ارسالی : سلام یاشار امروز از تعزیرات اومدن گفتن تمام لاستیک های کهنه که جلوی آپاراتی ها هستش باید فوراً جمع کنن کلا 24ساعت مهلت دادن برای جمع‌آوری گفتن به خاطر این دوباره ممکنه اعتراضات شروع بشه اگه مردم لاستیکا رو از جلو در مغازتون برداشتن و تو خیابون آتیش زدن  خسارتش رو باید مغازه دار بده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22485" target="_blank">📅 12:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22484">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بقایی سخنگوی وزارت امور خارجه: ظرف روزهای آینده، تفاهم ایران و عمان درباره تنگه هرمز نزد سازمان بین‌المللی دریانوردی ثبت خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22484" target="_blank">📅 11:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22483">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بقایی: بنا داریم در نشست مجمع عمومی سازمان ملل مشارکت کنیم به شرط آنکه آمریکا ویزایمان را به موقع صادر کند
فرانسه، انگلیس و آلمان به دنبال تشدید اوضاع هستند، حتما ایران در قبال اقدام نسنجیده‌ سه کشور اروپایی و آمریکا تدابیر لازم را می‌اندیشد
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22483" target="_blank">📅 11:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22482">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2b940d08b.mp4?token=daHztKY9159pFIW-qgekN47MqS0CEp4wnSDcDl9WVT21v2QYD9FB61GAT3xAqcbWj2QNsiZxEDcIjrHsO5eWkDbhQKCt4lb-JA56R92LoqBDOqlOXr2uCuuqVOVamF4iCzRFbVs03ZOhXxwWbTnvezjWVU7jD0sauObbagswyxcWB_FV3j8yePtqwN3sAXFCWXQ0kjBMwoSNXfkxO1gwjrgRNZ31yQXlni8C3uLAbT4xzGVJounUORpLqMuAZV4nxNvl-KLyjaV88CNLW0rB59y7-Aefld1e1BnFH8zh2-eLevgGvTH8G5DynJCVpyC2_Iuz0kBMTd3dmte_sj3sa1tLMYkxeB3Em6XSyDwI1vLTfP6iTnJBccrV3H3EoGOghMv8FkqUJnrXAck-D1KqSe8RTsF16_6PAlue5EOy1V3mImzRzQuUftDH43cqC6tMeFBAAPTXMnzSidFuj0ggP9Ydtjc_Dn31G7WOcS1SSMjwRwSypsQ-2gpCWMLTbDaTPuZ3ESKDNfvVpnUm70dEHw8ACoTx0WxakQ_76cAetucOG_trb6AB_h6OaUBe6geli81mEXVxcwGCmoPOH4qvg3jt0_0RaIZqiFgVzhYJf5L8BADWBRg-pfRmvvME_Z2Fdv-opGO-S-D78WvhkvwdqTl0VRcZktBR18YgQb7D_BY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2b940d08b.mp4?token=daHztKY9159pFIW-qgekN47MqS0CEp4wnSDcDl9WVT21v2QYD9FB61GAT3xAqcbWj2QNsiZxEDcIjrHsO5eWkDbhQKCt4lb-JA56R92LoqBDOqlOXr2uCuuqVOVamF4iCzRFbVs03ZOhXxwWbTnvezjWVU7jD0sauObbagswyxcWB_FV3j8yePtqwN3sAXFCWXQ0kjBMwoSNXfkxO1gwjrgRNZ31yQXlni8C3uLAbT4xzGVJounUORpLqMuAZV4nxNvl-KLyjaV88CNLW0rB59y7-Aefld1e1BnFH8zh2-eLevgGvTH8G5DynJCVpyC2_Iuz0kBMTd3dmte_sj3sa1tLMYkxeB3Em6XSyDwI1vLTfP6iTnJBccrV3H3EoGOghMv8FkqUJnrXAck-D1KqSe8RTsF16_6PAlue5EOy1V3mImzRzQuUftDH43cqC6tMeFBAAPTXMnzSidFuj0ggP9Ydtjc_Dn31G7WOcS1SSMjwRwSypsQ-2gpCWMLTbDaTPuZ3ESKDNfvVpnUm70dEHw8ACoTx0WxakQ_76cAetucOG_trb6AB_h6OaUBe6geli81mEXVxcwGCmoPOH4qvg3jt0_0RaIZqiFgVzhYJf5L8BADWBRg-pfRmvvME_Z2Fdv-opGO-S-D78WvhkvwdqTl0VRcZktBR18YgQb7D_BY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاخ سفید : در روشن‌ترین روز، در تاریک‌ترین شب، هیچ پلیدی از دید من پنهان نخواهد ماند. بگذار کسانی که قدرت پلیدی را می‌پرستند، از قدرت من برحذر باشند... نور فانوس سبز!
کد سیگنال این پیغام
:در داستان اصلی «Brightest Day»،
Entity منبع اصلی حیات و نیروی زمین
است که پس از حملات نکرون و نیروهای تاریکی به‌شدت تضعیف می‌شود.
Entity به دلار آمریکا، منبع اصلی قدرت اقتصاد جهانی، تشبیه شده که بر اثر سال‌ها سیاست انفعالی و بی‌ثباتی‌های ناشی از جمهوری اسلامی تضعیف شده است.
حلقه فانوس سبز نیز نماد
اراده، غلبه بر ترس و ایجاد تغییر
است؛ و جهت‌گیری آن به سمت سرزمین ویران‌شده، به حرکت ترامپ و آمریکا به سوی خاورمیانه و به‌ویژه
ایران، به‌عنوان مرکز ثقل منطقه
تعبیر می‌شود. در پایان داستان، نور سفید نگهبانی را برای احیای زمین انتخاب می‌کند؛ این تصویر نماد
آغاز دوره‌ای تازه برای بازگرداندن ثبات و امنیت به منطقه
است.
پیام نهایی: پایان دوران مماشات با جمهوری اسلامی، اراده برای تغییر و آغاز روند بازسازی نظم خاورمیانه با محوریت ایران
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22482" target="_blank">📅 11:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22481">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مدیرعامل شرکت فرودگاه‌ها:
۲۷ فرودگاه در جنگ آسیب دیدند
که آسیب‌ها در سطوح مختلف پروازی، باند، ساختمان های ایمنی، دستگاه‌های کمک ناوبری و بازرسی، ترمینال های مسافری و...بودند.بارها گفته‌ایم که بعد از آتش‌بس جنگ ما تازه شروع شده است.
بازسازی آنها کار سختی بود، ولی انجام شد، زیرا در بخش ساخت و ساز فرودگاهی توان خوبی داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/22481" target="_blank">📅 10:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22477">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf4f398265.mp4?token=oQWJGjJojS-C0lnA-Qv95rV3ULmCsq369n29lJbhEU3FuIyzjmwNJgsds4bi-Dq3w4KzssLyCKQEWKyQ5hpsSp4X9wNXLZNHQDKhDjGCDYnbsf7v5s6ssgYacpuOV2calArKgyHOTpbBGGRgmpi2kI60WxUNYxRykZU2-dw8Hsfqoi7SquM57Y3t2MuJADOSKY4FaTHMzB3_ZmFDKHXY3u4M1U3RldGjwLURckU07LjyAP5QZkfK9CQWoEfjXsBZHTBXQAFOfuOj_yPF22IzEoUYVadB1trx9Sys4A32pjBhjc_dOp4VVzcpAX76UmNNwiJG6lZHiFI5hmnkA5m2lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf4f398265.mp4?token=oQWJGjJojS-C0lnA-Qv95rV3ULmCsq369n29lJbhEU3FuIyzjmwNJgsds4bi-Dq3w4KzssLyCKQEWKyQ5hpsSp4X9wNXLZNHQDKhDjGCDYnbsf7v5s6ssgYacpuOV2calArKgyHOTpbBGGRgmpi2kI60WxUNYxRykZU2-dw8Hsfqoi7SquM57Y3t2MuJADOSKY4FaTHMzB3_ZmFDKHXY3u4M1U3RldGjwLURckU07LjyAP5QZkfK9CQWoEfjXsBZHTBXQAFOfuOj_yPF22IzEoUYVadB1trx9Sys4A32pjBhjc_dOp4VVzcpAX76UmNNwiJG6lZHiFI5hmnkA5m2lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏خبرگزاری عراقی «بغداد الیوم» گزارش داده بیش از ۱۵۰ نفر آزادی خواه ایرانی به محل اسکان دانشجونماهای عراقی گروه تروریستی «حشدالشعبی» حامی جمهوری اسلامی در دانشگاه سمنان هجوم برده و شماری از آنان را مورد ضرب‌وشتم قرار دادند. تعدادی زخمی شدند و ادعا کرده پول، تلفن همراه و ساعت برخی از آنها نیز گرفته شده. گزارش‌هایی از تجمع مقابل خوابگاه و محاصره تعدادی از دانشجویان عراقی منتشر شده است. پلیس رژیم جمهوری اسلامی در محل حاضر شد
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22477" target="_blank">📅 10:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22476">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddc3ca6006.mp4?token=ny9ig1GhZWEFapAiWHfCZlnFgGSgQFKs8anbU-uDxP7glkVaOz02TmNiv17WjB9RDiysUZnqKzhi4okF15e8hIeywr3QUWqHXMiF5914hz3Deml74h15Lyv1rAFSsLlmnsKN0suGpvubtXYGYEvfmIOL9rEBwsd63e5fLENzK_lEI-R4BOY4PWDNVcY1iGgrarrhLezs8LW0stkj0nYkr2ZFLNZ5Ld_RwsjKrhU0-7JtwLWkicVqqfyvVEBqCC3ZnWdZDoBM9P-2FCpXhnyK7H9pEYfeaWBxMiwtujmVd9W3VvlEhqRCdVYr2NFyxad5OQS0yUOPyDao664Gx5cNVI9PTGVeNTOj7y9YxQ5k3l2zrM1_jO6sVjaitBe0-42Kaa0TcpQpgp9hM50AW81jfs7Hi9_XtWAgcG6pBeJkpJuJIj1zzjMQG8vAp64PrRHOVcduXftgH7d0Nq0-u4Cpc5LEN9Ujd1tamgayPeeTSY-Zpqn_VR7HYnkMDpUAJFPBAj-SFr7R-pn2kQpjqiPzdhXPdCmd2NY2OSRnDp94qXipk5WGV6in2JpGmYr4lFp7O-0dk6NMhhMO1WrWV_H3bUZfHt6S9ZaU0Oy9dGiB1LL52YFJHIkmMr9hyZ6hQnzKfTJc3GTFNzJpIo9Fo68CPKIOqAtissMXEmPAeTjTF-Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddc3ca6006.mp4?token=ny9ig1GhZWEFapAiWHfCZlnFgGSgQFKs8anbU-uDxP7glkVaOz02TmNiv17WjB9RDiysUZnqKzhi4okF15e8hIeywr3QUWqHXMiF5914hz3Deml74h15Lyv1rAFSsLlmnsKN0suGpvubtXYGYEvfmIOL9rEBwsd63e5fLENzK_lEI-R4BOY4PWDNVcY1iGgrarrhLezs8LW0stkj0nYkr2ZFLNZ5Ld_RwsjKrhU0-7JtwLWkicVqqfyvVEBqCC3ZnWdZDoBM9P-2FCpXhnyK7H9pEYfeaWBxMiwtujmVd9W3VvlEhqRCdVYr2NFyxad5OQS0yUOPyDao664Gx5cNVI9PTGVeNTOj7y9YxQ5k3l2zrM1_jO6sVjaitBe0-42Kaa0TcpQpgp9hM50AW81jfs7Hi9_XtWAgcG6pBeJkpJuJIj1zzjMQG8vAp64PrRHOVcduXftgH7d0Nq0-u4Cpc5LEN9Ujd1tamgayPeeTSY-Zpqn_VR7HYnkMDpUAJFPBAj-SFr7R-pn2kQpjqiPzdhXPdCmd2NY2OSRnDp94qXipk5WGV6in2JpGmYr4lFp7O-0dk6NMhhMO1WrWV_H3bUZfHt6S9ZaU0Oy9dGiB1LL52YFJHIkmMr9hyZ6hQnzKfTJc3GTFNzJpIo9Fo68CPKIOqAtissMXEmPAeTjTF-Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخیراً تماس هایی از مبداء نامشخص
(شماره نمایشی سوریه) با مردم بومی جنوب کشور حاصل میشود و درخواست میکنند که طی درگیری های پیشِ‌رو هیچگونه حمایتی از سپاه نداشته باشند
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22476" target="_blank">📅 10:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22475">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS.A.H74</strong></div>
<div class="tg-text">سلام آقا یاشار گل خوبی من بندرکنگ هستم سمت دریا ساعتای ۶صدای مهیب انفجار اومد نمیدونم چی بوده</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22475" target="_blank">📅 10:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22474">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">العربیه: در حملات اسرائیل به کفررمان در جنوب لبنان تا این لحظه 9 نفر کشته شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22474" target="_blank">📅 10:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22473">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رویترز , تنگه هرمز در پایین‌ترین سطح تردد: داده‌های کپلر نشان می‌دهد میانگین عبور کشتی‌های حامل کالا از تنگه هرمز در ۱۰ روز گذشته به حدود ۱۰ کشتی در روز رسیده که پایین‌ترین سطح از ماه مه است. همزمان ایران اعلام کرده قصد دارد یک منطقه ممنوعه جدید در نزدیکی…</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22473" target="_blank">📅 08:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22472">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گزارش صدای انفجار یا پرتاب موشک از چابهار
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22472" target="_blank">📅 08:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22471">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رویترز , تنگه هرمز در پایین‌ترین سطح تردد:
داده‌های کپلر نشان می‌دهد میانگین عبور کشتی‌های حامل کالا از تنگه هرمز در ۱۰ روز گذشته به حدود
۱۰ کشتی در روز
رسیده که پایین‌ترین سطح از ماه مه است. همزمان ایران اعلام کرده قصد دارد یک منطقه ممنوعه جدید در نزدیکی تنگه ایجاد کند؛ در مقابل، عملیات دریایی آمریکا همچنان فشار شدیدی بر مسیر صادرات نفت ایران وارد می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22471" target="_blank">📅 07:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22470">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwyEGws-I_YBvl8nGt4pqydLwq3uO1iCeiKPQOckavTeNGqtwiQ9_9LkWl4ZP034IXQxMUUAtl9_O-lHofx25MjzN2Vta2l42A75qx_-BpKC3Bov8gSYYL3O7embtukV7H2VOgzWNKZOpf68mbKF7UYFZhv39aUrZSy6Jb9rdJ_m0OG1ZkK4o0-PZD4IL-3faTqwNWIwrUD771BAmXspdskniCVR5Mfuj-fyMrjbiZDgeitd3UT88l1uQTNBd-L3FWNzlKrMi2wwbqMaTAmbIiq_qhD1tbZHklgS90unuBwGbHEIEcwClSXomzFih4ecoS2f9qayCGyxj2vJrkxB-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی : سلام یاشار جان امشب اینو دیدم تو خیابون تهران رو زمین بود ، به نظر از این تراکت ها تو تعداد پخش شده باشه تو شهر ، آخر این حکومت رسیده و جشن آزادی بزرگی قراره بگیریم
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/22470" target="_blank">📅 00:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22469">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Par4ylA6ye7ufnIAVYRJia7fWj8qghg8AkBMVWE5P278WikpOYpxPW-BR7hjfNfqol2ByhxsA4T-JPF_Ho1I4KVDq7TZqxp6nI9ORy27kyaut89wEKhOVAXKcn4ISro3mrAWvqJ5EjFS7_Nn5i2plpe7j69CyTzY5XMWFWbvSQdrI9ABdxtETwJWnBqKl8pRyo1JkIWE7TMQSMOqHkdsT_Bx3H-Wi_5uUqhjC4qtzw17zxyCIHokGRslQE6Ar3eQRYLAGyhCRYz4Qa4cWYhcVCqRhTztBXq1R0pZn8wRKxwYaPUaDKJEI3xrKQwI643WQl6uDRT43wqLyqod1hyIPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنی که جمهوری اسلامی او را «شاه‌مهره» می‌نامد، اکنون در زندان قم جانش در خطر است، برای نجاتش کمک کنیم
نازنین برادران، معروف به
«رها پرهام»
، پس از اعتراضات دی‌ماه توسط اطلاعات سپاه بازداشت شده و بنا بر اطلاعات خانواده، اکنون در
زندان قم
نگهداری می‌شود. رسانه‌های حکومتی مدعی شده‌اند او
معاون و دست راست بیژن کیان
، رئیس اندیشکده «صدای آزادی»، بوده و برای
هدایت اعتراضات و اجرای طرح براندازی جمهوری اسلامی
آموزش دیده است. آنها همچنین مدعی ارتباط او با
آدام لوینگر، افسر سابق پنتاگون
و دیدار او با
تام کاتن، سناتور آمریکایی
شده‌اند. نهادهای حکومتی همچنین می‌گویند او در تدوین ساختار حقوقی دوران پس از جمهوری اسلامی نقش داشته است.
اعضای خانواده وی به من گفتند که او قانون پس از براندازی جمهوری اسلامی را نوشته و آن را به سازمان ملل برده است.
اعضای خانواده وی می‌گویند
او از نخستین روز بازداشت ممنوع‌الملاقات بوده و حتی اجازه تماس تلفنی و شنیدن صدایش را نداشته‌اند
و اکنون
کیفرخواست پرونده‌اش در حال صدور است
. خانواده نسبت به وضعیت و امنیت جانی او به‌شدت نگران هستند و خواستار توجه رسانه‌ها و نهادهای حقوق بشری به پرونده او هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/22469" target="_blank">📅 00:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22468">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmqwiC85n7mC6abyubUSUl5gDtZQho7KInC1k4GQTpMuyvLXlaAtHQyi5TGzHkVmnOzE_k8VNgdMPy1p-VB4gmcAemCkx9jGwTZCJiIGGUXBdwO6tpPXSn_OzivcNWy3pi_nfQX18baaxPp_CCG8PoXqyRueKodPeHmfw-2U_KSURrYo9qeXEbAm22G1_5PCxFt3Nj0VcoOci4QrHeYIuqBI-94tIOLUaiw4EyU5LFDxM0FpMNN4DdgUDNZ4WELxzUQO9VhGSh0wmk7I9wvolIoRch0hAiP_hifZH-O6m0xaey1UlD9DWuNT0mJVg9DMeXZSWwe_ThNOjtH8KD80Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درگیری میان نیروهای امنیتی و مهاجمین در زاهدان؛ بر اساس آمار اولیه، ۲ تن از نیروهای امنیتی کشته شده اند. @WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/22468" target="_blank">📅 23:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22467">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">درگیری میان نیروهای امنیتی و مهاجمین در زاهدان؛ بر اساس آمار اولیه، ۲ تن از نیروهای امنیتی کشته شده اند.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/22467" target="_blank">📅 23:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22466">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNef0cW43_j6Ipy97MHRLls_CGAPgn8Ch-dbFgjN811Lfztp1JV5xb-LEVauWfZM3FqyHO8g7xqbf6xvli6oshoOfy7YJRmybhLWiAFfPEnkMPhE76cv9651vWKNoU9oBoSc9p7WAez8svdzcnJg13_7PfnLuWlycCOGJJOKz_9NuTfRhPdtdlw4KKOV4HtSJ39Wr3ci-Db8kcIxXNBF41Be98Dfr_EDL_WgnmgfgHXgSSWj5S1zQN56TjgltIOhLWvLD984XOjs8kFpRmoyoL8zQ1WHzIvfBshqXDQzMvylrxw7bHPrgTBOQXD93QUkx_JeYm8AL04gEiqkmyawSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران کشوری در حال فروپاشی است.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/22466" target="_blank">📅 23:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22465">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPb2Axfw2-H8cc2MQ01Q-iWvULGa2gbX_10FKYEkdkfYF5epsUaYGIfOyUvNW07LSGMHwp1SWSGOvlXJPoAhimAkqQOp1u3CNq1dd_5BUNa2xYRpdvm1FybvZhBTtqukwjqQ1ZXMMOeDI07SaojMBkggh12OgxD4eGTLLEjXeszKEUBaWEqjYuSM0TB8Rr_YBV5MiOJYovziEov4vreq6-L_vDsfINwV5OOIeg4mNWrPzynmYF5-g3nfNZwflLpYh6AfseqNyvHj7nZIaj6UxcypcV6qhMp50FGiDRIuKSUNFByZjpNdB4sUDDZfsaY6hf4wJTqlcCwpYawd-7gvMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : حجم نفت هرمز برگشته است!
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/22465" target="_blank">📅 22:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22464">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1PffmccY4wru1FDsOEqiBlCNayNBp-iVOIK8IYW8TVCWjEFDSYrUIlKPZNqw7f6TaVJWguJmTnbl8Nm7etQuy2MSoOgcwDYROcf9CF0ySvLAYcPBMOG5OLpL1LszJQZuAxx1osx0Ytp28XkjKeQYJQBIXzVpOlCUxf8Hz_qxhTzZ_hMXnHMERRTjUO3adu1CtjyBLRo0MieMiZsns18RkcS-4E9BcLadt66lAGFXlNMjnorjfO7U2Szr8q4wIVYSjI239madi35sp1O-EvqrDFJOAnCkoVF1VgUNcaey7b_3mTJqrBMt9g-fAPecr2CAkC9xmEZql8Sxoo8HjDAVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : کابوس برایشان بساز
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22464" target="_blank">📅 22:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22463">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHffedJDodpmEGGaTk2XImh6B24rpnDvVwLonAzeUde0aq9uzIBc2SgqrMdP1LZwKqUC7IM5F8MKhxQfxRLrWevHjZ9jwxLiO--00XKouyKotZtXflxV52nxHfkJtw8mmlUV2Qmf3iWRarTVIVvqCm0VC8oeO8hzpzTsrFpt5y450jCK1CyXChdgEmqgOji62V-QNCOASXlvK4RpCzB9QtL61jAEscZTQVb4J-r8x1gnSn70tNs4cxQnR1yVECTTEBdtuwohveFFMDe0zV62M52NFQysCjDDOOU5AtVSdfUS2oWZpWAa8BOyxKtX2__KM0fln9zSU7au5JJ5vnOhKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : صادرات نفت ایران در حال سقوط است
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22463" target="_blank">📅 22:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22462">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLa3yDy0jc8Fy7HX3YMt3Z7sIxsW1wJWHeUclGxOPC728nXM55hDFyIP3g879PDU9B0gjxT85LQtHay3dUcNnD1Hro84apl6VVj9H_TrjZ_Eu11t4lRMgruNrWlC8LKzvG6InqAcqGGIyWoZNGekSRBimDFobnPhqMtd8I3ChSgiFJ2jqNt4XRJZNvrIP06Pv4tA_ImfaA6GQegXDU8PuR9Zao6ktblBEOeguRbQH05XE633r_In6OKJONHRjpWTUeKB0rePNrEZ0myt2m0IItUGVZ0RxW2oNiZxNJosHWKJrXJF7W1G3truy9UMiqJy1GiNozut-Zc65ZSTroq2Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :
ایران دچار ابرتورم است
پول ایران نابود شد
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/22462" target="_blank">📅 22:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22461">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbtR0Zp7hLfsgcZ2_9DWiJOBRCOM6lc-ZlMrcrIhpXk4pynjfEzp2QwudOt59HRtxE8EMAukPIJVGaKqPjn8Pp2bpcf3qaT7BZ89bwKrigMKUIwdrq8PYlvJ_iR9UsmxvXCbdjntpvDmJ5wHc5n1DW8_0izqOSNVHOhFG7I-TzPVcW3vgNh69LPSS18RuVj2dakSOt2S6Z-YWiWs3O3SIXSEC3o9zZGueGq8Ni0rj-oBFhSV-EiTuSi76KkTpqqjEhBQcfjoUJaE116aKysShCN2A8CrN3Cii_DCp4uQJIBzDPBEevQWLB2QcL-BMG8wbzBU9Y-fgk5NKoB9yDq7Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : خداحافظ خارگ
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22461" target="_blank">📅 22:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22460">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ارتش اسرائیل پس از شلیک دو پهپاد انفجاری حزب‌الله به سمت نیروهایش در ارتفاعات علی‌الطاهر، موج تازه‌ای از حملات را در جنوب لبنان آغاز کرد. اسرائیل اعلام کرده
انبارهای تسلیحاتی، مراکز فرماندهی و زیرساخت‌های زیرزمینی حزب‌الله
را هدف قرار داده و برای انهدام دو مسیر زیرزمینی در زیر ارتفاعات علی‌الطاهر نیز آماده می‌شود. همزمان گزارش‌ها از
انفجارهای شدید و درگیری‌های سنگین در منطقه نباطیه و اطراف علی‌الطاهر
حکایت دارد
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22460" target="_blank">📅 22:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22459">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUZ3mQQ4cyOIbx5xYAcEZNQhpkliqPWpYD4M0et_tzFvjEmXjlY3L3OkBIG6Gw6GhDx9IQ2rU8jlAHtLwVGxtIOOg86J_WmfsI1HDr7LdIkdyiBZIRoQohbwCt834Po75k6UDr5ZcfCqsR4u9x7i5l9oMI4LAKaSX13yIuXIuOXycizyalaVWuQbycg6ExPK6sjsF3yJvx4I8NcqiL5V7h3ux34UvoEFLAlWhbHi5_hV-Mt3XDLwxIqQLJ-RHmmr-NNMQ3OmfTrKqXFqm3v9f5yruBw0kp6P6nzZwQPzotA0_4B4lqFefLDWMmyL7fo7ghGKkSbzniDeaJWFHvuIeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث: نقشه ایران رو برعکس کنید میشه تصویر من
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/22459" target="_blank">📅 21:29 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22458">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22458" target="_blank">📅 21:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22457">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رژیم:نرخ سوم بنزین تغییر کرد/ سهمیه اول و دوم بدون تغییر
سخنگوی دولت: نرخ کارت جایگاه سوخت از بامداد ۱۷ شهریور به ۱۰ هزار تومان افزایش خواهد یافت.
در جلسات کارشناسی اعداد متفاوتی گفته می‌شد اما چون رئیس‌جمهور به مردم قول داده بود همان ۱۰ هزار تومان تعیین شد.
۶۰ لیتر بنزین ۱۵۰۰ تومان و ۵۰ لیتر بنزین ۳۰۰۰ تومان همچنان بدون تغییر ماند. افزایش قیمت نرخ کارت جایگاه صرف معیشت مردم خواهد شد.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22457" target="_blank">📅 21:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22456">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کان نیوز:
ارتش اسرائیل قصد دارد
شبکه تونل‌ها و زیرساخت‌های زیرزمینی حزب‌الله در منطقه علی الطاهر در جنوب لبنان را به‌طور کامل منفجر کند
و بر اساس گزارش‌های اسرائیلی،
در انتظار تأیید مقامات سیاسی برای اجرای این عملیات است.
گزارش‌های پیشین نیز از آماده‌سازی مواد منفجره در این منطقه خبر داده بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22456" target="_blank">📅 21:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22455">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یعنی خوشم میاد شهید سید علی خامنه ای پدر ایران خیلی میسوزونه شمارو
😂</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22455" target="_blank">📅 21:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22454">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یعنی خوشم میاد شهید سید علی خامنه ای پدر ایران خیلی میسوزونه شمارو
😂</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22454" target="_blank">📅 20:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22453">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmin</strong></div>
<div class="tg-text">یعنی خوشم میاد شهید سید علی خامنه ای پدر ایران خیلی میسوزونه شمارو
😂</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22453" target="_blank">📅 20:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22452">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نتانیاهو: ما مصمم هستیم که مأموریت سرنگونی رژیم ایران را به پایان برسانیم.
پایان جمهوری اسلامی نزدیک است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22452" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22451">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee397b868b.mp4?token=Asjlw3Ip6B6bgOaP8WS0lJUyVcOE6z0aKaz-TVzhcaAJAOFmNtQpvfHTFyQ4sfFgrl0WCXlSr4LBSWmoAi0-iN_vSGgNOJhyHduijM0LNLlXYgXajle832CChYGTwkHrfDQmac5wTLpmJfehiVYnR0bD1gXKbkCY83I32C6hI8nJB9g1577hesoRPHlga8SPUtKynXY0-dO1vcr4R-gWtkBS3TfwYRRki1Lem_H_qgiczRVu0fihT40C9gpZGsHJCJvIafIze_KjcqcPOM3JKFc92WBbnx51gP7KdKyDQAWfaJ2xeGf7Y_zcEnVL0sZ0aQG0VC9yGp9EiQiaDdduXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee397b868b.mp4?token=Asjlw3Ip6B6bgOaP8WS0lJUyVcOE6z0aKaz-TVzhcaAJAOFmNtQpvfHTFyQ4sfFgrl0WCXlSr4LBSWmoAi0-iN_vSGgNOJhyHduijM0LNLlXYgXajle832CChYGTwkHrfDQmac5wTLpmJfehiVYnR0bD1gXKbkCY83I32C6hI8nJB9g1577hesoRPHlga8SPUtKynXY0-dO1vcr4R-gWtkBS3TfwYRRki1Lem_H_qgiczRVu0fihT40C9gpZGsHJCJvIafIze_KjcqcPOM3JKFc92WBbnx51gP7KdKyDQAWfaJ2xeGf7Y_zcEnVL0sZ0aQG0VC9yGp9EiQiaDdduXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جرد کوشنر: در دنیا چیزی به نام دشمنی ابدی یا دوستی ابدی وجود ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22451" target="_blank">📅 20:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22450">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کریس رایت، وزیر انرژی آمریکا، در مصاحبه با
مارتا رادزاتز، خبرنگار ارشد ABC News
در برنامه
This Week
درباره ادامه جنگ و سیاست آمریکا در قبال برنامه هسته‌ای ایران گفت:
ممکن است دولت ترامپ به توافق هسته‌ای با ایران دست پیدا نکند و در عوض، توانایی تهران برای دستیابی به سلاح هسته‌ای را از بین ببرد.
رایت تأکید کرد هدف اصلی آمریکا جلوگیری از هسته‌ای شدن ایران و کاهش توانایی این کشور برای تهدید منطقه است و گفت
اگر توافقی حاصل نشود، گزینه نظامی برای نابود کردن این توانایی همچنان روی میز خواهد بود.
او همچنین گفت آمریکا در حال وارد کردن
«درد کوتاه‌مدت»
به اقتصاد و بازار انرژی است تا به گفته او به وضعیت بلندمدت بهتری برسد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22450" target="_blank">📅 20:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22449">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بهنام صمدی خبرنگار بورسی: از امشب نرخ سوم بنزین ۱۰ هزار تومان خواهد شد
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22449" target="_blank">📅 20:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22448">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f35315292.mp4?token=lyhWxVYZWMBBO9ZrXxG-Zj0AIm56Q99bWNUUffJ5RCI55tZ6Enw2NzLAY3mG2PGkbeQGYmt2t8JnFuxOofzKRMMuY235hQpRgU-CScP6iepoL3iCDVx_m52YGv6yWsGmCXk4_26e_Qd2iVyFV4VYDx3VCscRDBR1kCV33Q7fGJ5TbUTrP7xbOQhaNOFjKBni2aXEy_d2gSf0D1GvcwIVIqEaRABY4J2C8igpLvzo_4pVbm5DHRx7N9S0j0tvZeiv4oDfpp8LzozensyPK-7oSOtUzvKp9AJBiJCGn_2o96Bbmy7Wwxccgi373FyaNVzboyaA7zICWZ72m_o-Y5CGuaYPhK9FXbNFF6vk9jT6Yxtp-dmlMTpu14dQXQ9inMBFCvqHGCY7VtKz_i7n0jD2FHQYa_t8NettCT2PqrD_NMYFW2NyvzonIAIWdxXReAokJ4eOHlglmWObDqyJG8LaPxsT-MP0cYUF-saGd_ML9565SujuuGGsX54DgnrsG7XJUXWX98NeQMOAAeQzHMT6x_aFlq30XVXTsx4hH-udjeJfDvz8oPBIy06Efu9B0vX0E7VEifnopvXRPBigiJp-9A-a88pMvp_28d_GV1ZAqr2Cn6DzqbUugn2Uv_UrXqSWmQrPg6em8fzsJhAMAp5dnH47qO043Sh56s_Jbgzh_Dk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f35315292.mp4?token=lyhWxVYZWMBBO9ZrXxG-Zj0AIm56Q99bWNUUffJ5RCI55tZ6Enw2NzLAY3mG2PGkbeQGYmt2t8JnFuxOofzKRMMuY235hQpRgU-CScP6iepoL3iCDVx_m52YGv6yWsGmCXk4_26e_Qd2iVyFV4VYDx3VCscRDBR1kCV33Q7fGJ5TbUTrP7xbOQhaNOFjKBni2aXEy_d2gSf0D1GvcwIVIqEaRABY4J2C8igpLvzo_4pVbm5DHRx7N9S0j0tvZeiv4oDfpp8LzozensyPK-7oSOtUzvKp9AJBiJCGn_2o96Bbmy7Wwxccgi373FyaNVzboyaA7zICWZ72m_o-Y5CGuaYPhK9FXbNFF6vk9jT6Yxtp-dmlMTpu14dQXQ9inMBFCvqHGCY7VtKz_i7n0jD2FHQYa_t8NettCT2PqrD_NMYFW2NyvzonIAIWdxXReAokJ4eOHlglmWObDqyJG8LaPxsT-MP0cYUF-saGd_ML9565SujuuGGsX54DgnrsG7XJUXWX98NeQMOAAeQzHMT6x_aFlq30XVXTsx4hH-udjeJfDvz8oPBIy06Efu9B0vX0E7VEifnopvXRPBigiJp-9A-a88pMvp_28d_GV1ZAqr2Cn6DzqbUugn2Uv_UrXqSWmQrPg6em8fzsJhAMAp5dnH47qO043Sh56s_Jbgzh_Dk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلنسکی، رئیس جمهور اوکراین: در طول یک سال گذشته، فکر می‌کنم ما قوی‌تر شده‌ایم. افراد ما کار بزرگی انجام می‌دهند و به دیپلماسی فرصت می‌دهند. بدون یک موضع قوی در میدان نبرد، یک موضع قوی اوکراینی، فقط اولتیماتوم وجود خواهد داشت. اما امروز، دیپلماسی امکان‌پذیر است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22448" target="_blank">📅 20:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22447">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64dc505262.mp4?token=T26xmW_tqamlvmvaUnPNJZtnny2IaP7seZuHwNg8qxmz9YkaOLm-MW4Ks9_T3VHDQLyZwLfTzTpbyt3UjY_k0YnPDfpMAFD_OTRYW-n3OfSF1OUPsaPTxqB8RIxeynewnPkuJ6lvkUDptwbcfRzhyAmSCY6Hs1qPm0MpOqvmso1hupi7wuU2KytNcErrU5wAw1a5JCGRHjcNS8AWSBhQCEzSmaPd1U7wKhd6q6xtSCi_WYs6M9Vin5FOBQwIqTVxjEzllC1HWcWQk6lQ9vW-zve2iifcyTu1zhu1TDgY-ujLqUqnY_o-9pb7rmzJvcF7AwYOy1bHBhkS1f2Gg628PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64dc505262.mp4?token=T26xmW_tqamlvmvaUnPNJZtnny2IaP7seZuHwNg8qxmz9YkaOLm-MW4Ks9_T3VHDQLyZwLfTzTpbyt3UjY_k0YnPDfpMAFD_OTRYW-n3OfSF1OUPsaPTxqB8RIxeynewnPkuJ6lvkUDptwbcfRzhyAmSCY6Hs1qPm0MpOqvmso1hupi7wuU2KytNcErrU5wAw1a5JCGRHjcNS8AWSBhQCEzSmaPd1U7wKhd6q6xtSCi_WYs6M9Vin5FOBQwIqTVxjEzllC1HWcWQk6lQ9vW-zve2iifcyTu1zhu1TDgY-ujLqUqnY_o-9pb7rmzJvcF7AwYOy1bHBhkS1f2Gg628PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: هنوز کارهای بیشتری برای انجام دادن باقی مانده است. این رژیم در ایران به پایان آن نزدیک است. آن ضعیف است، برای بقای خود می‌جنگد، لنگ‌لنگان حرکت می‌کند و هنوز مأموریتی برای تکمیل باقی مانده که ما عزم جزم بر انجام آن داریم. این امر در نهایت چهره خاورمیانه و مسیر تاریخ را تغییر خواهد داد
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22447" target="_blank">📅 20:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22446">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کوشنر: رئیس جمهور ترامپ می‌خواهد چارچوبی برای دستیابی به صلحی جامع و پایدار ایجاد کند، نه فقط پایان دادن به جنگ فعلی در اوکراین.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22446" target="_blank">📅 20:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22445">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ویتکوف: ما برای از سرگیری روند مذاکرات به کیف آمدیم و از دستاوردهایمان احساس خوبی داریم و مشتاقانه منتظر دستاوردهای بیشتر هستیم. روسیه و اوکراین باید برای پایان دادن به جنگ امتیازاتی بدهند
ماموریت من و کوشنر این است که طرف‌های روسی و اوکراینی را گرد هم آوریم و شکاف‌ها را کم کنیم تا به یک تصمیم مشترک برسیم که به جنگ پایان دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22445" target="_blank">📅 20:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22444">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پرواز پهپادهای ایرانی بر فراز تنگه هرمز!
سازمان دریایی بریتانیا (UKMTO) اعلام کرد که پهپادهای متعلق به نیروی دریایی سپاه ، در حال پرواز بر فراز کشتی‌های تجاری در تنگه هرمز هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22444" target="_blank">📅 19:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22443">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e697dcc2d7.mp4?token=rxK5WcD5mHvuTgk1FKjau6NESRzyqSxM2d66CIMqZ2bLmpjwtzxcrhMHRvANIgv265fI8dS_IH2kB2yAqOyLVlHwOEhd1KRfSmko4eKo1iGGIGaQf7iCbd4kx473OfI_cbFBRs6oExkhUBkGXfRfSfz5-0UsgPtQXJRx_SFB6DH-mlxp7mx_U8pbUVcPT3CwUiESsk-R9UcOuIt5Gj3F59m2Ka50ddzND0aRx2YujLFwcjsj1N_J36cgWj9aLLs4Ts4BWwgoTMrxL_QLn6uyoZhqIU3G2mkDath5PHxAhdg1ld2niiQ7W2QvbB8YXvfqN4r9ISqfzi4du8nJzdCAkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e697dcc2d7.mp4?token=rxK5WcD5mHvuTgk1FKjau6NESRzyqSxM2d66CIMqZ2bLmpjwtzxcrhMHRvANIgv265fI8dS_IH2kB2yAqOyLVlHwOEhd1KRfSmko4eKo1iGGIGaQf7iCbd4kx473OfI_cbFBRs6oExkhUBkGXfRfSfz5-0UsgPtQXJRx_SFB6DH-mlxp7mx_U8pbUVcPT3CwUiESsk-R9UcOuIt5Gj3F59m2Ka50ddzND0aRx2YujLFwcjsj1N_J36cgWj9aLLs4Ts4BWwgoTMrxL_QLn6uyoZhqIU3G2mkDath5PHxAhdg1ld2niiQ7W2QvbB8YXvfqN4r9ISqfzi4du8nJzdCAkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو، نخست وزیر اسرائیل، درباره ایران:
آنها به ما حمله نمی‌کنند. ایران از این کار اجتناب می‌کند و دلیلش را هم می‌داند: چون اگر این اشتباه را مرتکب شوند و به ما حمله کنند، ضربه‌ای خواهند خورد که حتی تصورش را هم نمی‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22443" target="_blank">📅 19:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22442">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwzMuLpr6jdGXIfXeIOFrfgG0BaUDx3aIlgsDK6KuRS9XdejY1bSHz0vXR2BjTtqUVt6rAEgbbp-pRGH7kjvHp0pKxv3OsrBhREgZw6dtqaYom1EEGYztHTGkOTTWRvxnnz9aMxyCDmCNxkxcsWikd2cGy5can0nkcJ9nKqZKK832gy6Mg7mNRBFTmunCpfoVaIC9p735UdNLnT82erGvZBMdOqQk-0LT2UvzQI8Ojz784EsyDcUnt40Q8_kI0TIROnLrXWfr8sJc5xEGhfv5gdT5UURUmZknyEhJ71EnLWkohYS3rs55EvVnONGMbkPIxEXrrLoe2FoVVRFhNOvfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث خطاب به رابرت دنیرو : حتی این احمق هم داره متوجه میشه!
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22442" target="_blank">📅 19:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22441">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKt9XkRn1xrqcYNFZjKsWBa8EadOdjQVt3Iu-jTWpR4iyZ4gX8ffjKySDq0kXTr8eBaM7vI_7nc9L-SMq5iVBVGxsSpNwFZthap7h8cqeTBRKPWVb1rOeYSNp6myuJyNGElb_-_wZIVtEYlPMaKfWoKnGj_ISq_4wa5NRHJ_o5gPP5aNK_LFF08DY8jhmDZVkoroXcVUZNwSUOdfDEGYQ4bCUlBpb5AgZXgNL4Vn4i-52WQt9FZ66axn8Ka0rO6qgykaGpTUHkoK0awITrcZV2xs9vm-y-oZzzG1wHuGtjZX9x5NMCUmm0cWY7COOINiIlwz2frUSnCQwvy0pF63GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استیو ویتکاف فرستاده ویژه آمریکا: از مذاکرات جدی و مهم با اوکراین راضی و به ادامه آن خوش‌بین هستم.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22441" target="_blank">📅 18:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22440">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8pAT8hS0gVsoUdEJl202OFKWFo6F2UCaCVHxRRDKXbNrftIPyKQOfc_n_d44sbj14428BxQj9Nc5cjYm0tmQAs0XNnjTpXtH3QgMMxiPT-cwHY3yy6SoShMCNB0PwWbuinW2amvrs67TxY-Bk_XWxoA2auQJqkHalR6iy4j2rLReHYa5JHI3v3mhtiQ47HoB9U56H9l6-ZbuvjmN9EIJ2SrGa4XUvax3iejCRqMjjgNBEB6SfNOc9jUys_a8PyHeH9dHcQ2JZ00roFPZIawo3mNCm3GcWqbxZNfi82utNovfqlh3pGWiw6x-UmZKfd-sJ1Fh_OUOOQKa78rmgSXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ رنگ موهاشو تیره تر کرد
@WarRoom
😁</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22440" target="_blank">📅 18:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22439">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وال استریت ژورنال :
سالانه میلیاردها دلار از منابع مالی ایران
با وجود تحریم‌ها، از طریق حساب‌های تسویه بانک‌های آمریکایی و بانک‌های خارجی دارای روابط کارگزاری با آمریکا جابه‌جا می‌شود. در سال ۲۰۲۴ حدود
۹ میلیارد دلار منابع مرتبط با ایران
از مسیر بانک‌های آمریکایی عبور کرده است. شرکت‌های پوششی و شبکه‌های پیچیده انتقال پول، شناسایی این تراکنش‌ها را دشوار کرده‌اند. مقام‌های آمریکایی با یک دوراهی روبه‌رو هستند؛
سخت‌گیری بیشتر ممکن است به جایگاه دلار آسیب بزند و تساهل بیشتر، مسیر انتقال پول ایران را بازتر کند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22439" target="_blank">📅 18:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22438">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تلگراف: لیبی کلاینر، همسر یکی از سربازانی که پس از سرنگون شدن هواپیمایشان در غرب عراق کشته شدند، در یک پست در شبکه‌های اجتماعی نوشت که دولت ترامپ او را برای دریافت غرامت‌های مالی واجد شرایط ندانسته است، زیرا کنگره به طور رسمی جنگی را علیه ایران اعلام نکرده است.
تلگراف هم گفت پنتاگون از پرداخت غرامت به خانواده‌هایی که توسط ایران در خاورمیانه کشته شده‌اند، خودداری می‌کند، "زیرا آن را جنگ رسمی نمی‌داند."
اما نکته مهم این است که
پنتاگون در نهایت غرامتِ مرگ را کلاً قطع نکرده است.
پرونده‌ای که خبر از آن شروع شد، مربوط به بیوه یک افسر نیروی هوایی،
الکس کلینر
، بود. به او گفته شده بود فقط برخی مزایای مرتبط با منطقه جنگی، از جمله
combat pay
و معافیت مالیاتی، به دلیل اینکه «جنگ رسمی نیست» شامل حال خانواده نمی‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22438" target="_blank">📅 18:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22437">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3A67E6hry9_7zMfZILmyZNQfqqWeUinvyoWR1bGbbRrqBisb4DHVfRDyB3Xj1whmm5XJLctYsNWi5eUzb4u86LG8QJRa-qulx6OULmry4JD5iFNsm8ywevB_tV93kgf6EuD5mGZpLXg9vx_bZ3sBoFcrju6ybuyiVp-q5D1RQdRtuWvg--mPOtw81lWxKa--IjLNIEvD_17jgSkXgOflv0yJIsQO7gAVycHQSqKtHWd-gPQVqlHzEuLbyrmu_i7MXU8a75YsjMjefUWDw66e2mS61Am43mqn4CJw460NLyFrmZ3Y9FfvmImJ_XsW4PJIaQz-cEhmDLhBuMmZbWr9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوه کلنگ گز لا (Kuh-e Kolang Gaz La / Pickaxe Mountain)
در شهرستان نطنزِ استان اصفهان و حدود
۱.۵ تا ۲.۵ کیلومتر جنوب مجموعه هسته‌ای نطنز
قرار دارد. مختصات ثبت‌شده‌اش حدود
33.7051, 51.7081
است.
@WarRoom
https://maps.app.goo.gl/LJq8rZ2kNdve6xiVA?g_st=ic</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22437" target="_blank">📅 18:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22435">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گزارشهای بسیار از شنیده شدن صدای انفجاری مهیب در اراک
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22435" target="_blank">📅 17:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22434">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اتاق جنگ با یاشار : با تماسی‌که با منابع داشتم نفتکش هایی که دیروز که آمریکا هدف قرار داد ۱ عدد با مالکیت ایران بوده ولی ۲ عدد آنها فقط در اجاره ایران بوده که حتمأ بیمه هم داشته اند
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22434" target="_blank">📅 17:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22433">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SguOQ_bAcEQb8T_UYMXIWXTeerTF4sXCmpS0wF-TflZEOOOcUbDMmDyRd1pDkN1VW-8CiuM_w8tWtlFyPhru17Q-uZFO7dFbMK37yUIiJS7ROvkM-iZ6lGU6f1op9WObhMJqLokv_OUj2zTsD62n_zl2d6e6xqkqKdQ6r5ZfNf3Q1cMDsCAVhG-swDfrtegeokryN5Gq_x_iTWifQhQTopzR3FYj32YswqXnUjtXgTZr4t4M9WA81BwODYIX1VrGxVVMElEqW0RF6QzoeIHXKrORiQ0-FzaYIUwlVj_I7yGVy3He2xQZcGh8ufKnlQ4ahjY-b8W_EpJ3NPsXRJZxZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکار سوخترسان آمریکای توسط دیدبان اتاق جنگ با یاشار مانند پلنگ جگوار  @WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22433" target="_blank">📅 17:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22432">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e8d0bd6c.mp4?token=AguO210d9zqGwUK-R1tSBUNmctM7pRAsycFD0mHPG03Rph2wclOlFu5T9EVpbauhzODnPOCVINIf2HS0X-VUuu3n--16MQSwrgN5tOztktsehOYNAHMXWsScyG8JBsK_8PaYkUGhQ45w30Fl0Tdx8IPoJvvKGYv-yhLZLZj74ORk6b3CPYFddWss6QbE6RFRMh5h1JJDInlVkH13fvzYMGZBUNp48msX0KrkSN9jr09kagRNYivejPjjgdRwpxr1Gl9ohHezDV8FyrTzVieOwZZZnkuInsi4Y3c_vrHSDL2cXiQRxqT6FRxwyoVqqxmsJjNZAq86_jCSlvcZ43d0Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e8d0bd6c.mp4?token=AguO210d9zqGwUK-R1tSBUNmctM7pRAsycFD0mHPG03Rph2wclOlFu5T9EVpbauhzODnPOCVINIf2HS0X-VUuu3n--16MQSwrgN5tOztktsehOYNAHMXWsScyG8JBsK_8PaYkUGhQ45w30Fl0Tdx8IPoJvvKGYv-yhLZLZj74ORk6b3CPYFddWss6QbE6RFRMh5h1JJDInlVkH13fvzYMGZBUNp48msX0KrkSN9jr09kagRNYivejPjjgdRwpxr1Gl9ohHezDV8FyrTzVieOwZZZnkuInsi4Y3c_vrHSDL2cXiQRxqT6FRxwyoVqqxmsJjNZAq86_jCSlvcZ43d0Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شکار سوخترسان آمریکای توسط دیدبان اتاق جنگ با یاشار مانند پلنگ جگوار
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22432" target="_blank">📅 17:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22431">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2dc5c16b1.mp4?token=osp8JwvxIh3wSgZwHWcZe5WqtghjkVSMVAkI-exYbqN1mz_IYWxBik3AMtmJ_onb4GN84sSkvhJn8qUyi4RVxMiWVcVA7qbS3VlNtUcURGgG6HaA3hFzJnqNqgfO_gGsAaK09X_THZG4yyDJhfW8M08eolvFiSRfSeG9ByhqTfG94efmslkI23al_wTzz6etzVNED0bvsaSK6znr2rQ8wEO0yGa8eyM2hbEUXZsKNeoBk65N7K2mgucVykVCDX169EPZsyWJ9iRHDksnPVWHshvjifFeolzcwvGDRiAeJz7tIWwt2O-Lrk4OqqQbr8zY3LFP2O6YpEXyrtZ9aSDDWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2dc5c16b1.mp4?token=osp8JwvxIh3wSgZwHWcZe5WqtghjkVSMVAkI-exYbqN1mz_IYWxBik3AMtmJ_onb4GN84sSkvhJn8qUyi4RVxMiWVcVA7qbS3VlNtUcURGgG6HaA3hFzJnqNqgfO_gGsAaK09X_THZG4yyDJhfW8M08eolvFiSRfSeG9ByhqTfG94efmslkI23al_wTzz6etzVNED0bvsaSK6znr2rQ8wEO0yGa8eyM2hbEUXZsKNeoBk65N7K2mgucVykVCDX169EPZsyWJ9iRHDksnPVWHshvjifFeolzcwvGDRiAeJz7tIWwt2O-Lrk4OqqQbr8zY3LFP2O6YpEXyrtZ9aSDDWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلگراف: حمله به بیت رهبری با موشک‌های «بلو اسپارو» انجام شد روزنامه تلگراف گزارش داده اسرائیل در حمله ۲۸ فوریه به مجتمع رهبری جمهوری اسلامی در تهران از موشک‌های هواپرتاب بالستیک Blue Sparrow استفاده کرده است؛ موشک‌هایی با وزنی نزدیک به ۲ تن که از جنگنده شلیک…</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22431" target="_blank">📅 17:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22430">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drgiwD-V_KcN9AAAOVq8hojnisHO0ta6UMCgfDOpOI4hTCjrCWN-BQyhf6759zicJeQrj-zcwZusecMUsjUA0LJERsn6oWKoJLGww6KqeGpdqDLsXe5uvxC0L8Y__2pwSNmgtW0-8Bqjftbm3XiuKvfRyEfIpckxzDmsvuT-hc3oPReQQYcA13OlgCa8cOiY24HX0v9WGQtF_NAt57YKexNhntdApxTLtPDKuQR7Kq_yGZTY9RNoaDxGDUhGybWVg2wbE6XeIbTeAW5koLcLgirwR2ZR3DL_MIq3Gsix_y5mLbor9X4gU-aDalBIJWzoyyzcz5gkh5ECStXJQlzF-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگراف: حمله به بیت رهبری با موشک‌های «بلو اسپارو» انجام شد
روزنامه تلگراف گزارش داده اسرائیل در حمله ۲۸ فوریه به مجتمع رهبری جمهوری اسلامی در تهران از
موشک‌های هواپرتاب بالستیک Blue Sparrow
استفاده کرده است؛ موشک‌هایی با وزنی نزدیک به
۲ تن
که از جنگنده شلیک می‌شوند و پس از رسیدن به ارتفاع بالا با سرعت بسیار زیاد به سمت هدف شیرجه می‌روند.
گزارش‌های اولیه از پرتاب حدود
۳۰ بمب
به این مجتمع خبر داده بودند، اما گزارش‌های بعدی استفاده از موشک‌های Blue Sparrow را مطرح کردند. با این حال، مدل دقیق تمام مهمات استفاده‌شده هنوز به‌طور رسمی تأیید نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22430" target="_blank">📅 17:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22429">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">روزهای بسیار حساس در انتظار پرونده هسته‌ای ایران
؛ نشست فصلی شورای حکام آژانس بین‌المللی انرژی اتمی از فردا با حضور نمایندگان ۳۵ کشور برگزار می‌شود و پرونده هسته‌ای ایران یکی از محورهای اصلی آن خواهد بود. آمریکا و سه کشور اروپایی در این نشست چندروزه به دنبال تصویب قطعنامه‌ای برای ارجاع پرونده هسته‌ای ایران به شورای امنیت سازمان ملل متحد، به دلیل عدم پایبندی تهران به تعهدات پادمانی خود ذیل پیمان منع گسترش سلاح‌های هسته‌ای هستند
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22429" target="_blank">📅 16:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22428">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22428" target="_blank">📅 15:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22427">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cvjiba8x9uRBZQADH82Bh26uJLYI7ylBIygpRRUK3OwGqBQo4TcJNW6azlN8VKOahTwczbWYUqhIr7bGqQ4ugYNy0iVUoGJbVyQh_jpJ-ZOEsPLJCEqJUa70Lc5ROAINwHjNkq664YSNDXnXlJwin2Mr0RTH0U1ucErgcDhbALt6dySA2igl43nxigLXYEAfNBPYA-GNIfikar2avyvxHMLxMpqM5amPPPlyykDF7djjGNehzwndWhpE5PiegpanxKqdqeTy1MtWEU7manbhHeb2eUMAeBHNjf6Jfg50EdHMgd5KVuaDJaszd-4Iw_nCnql9TGiNnW4AsMrDHUpJ5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت جوری شده که حتی اوستاد هم نمیتونه تحلیلش کنه
😂
خدایاااا بسته دیگه
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22427" target="_blank">📅 15:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22426">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eql2p1TVgBJZJVD3saptgKWEEkFp-vrD4KH3hH88AjrYEEfdVM8zTTFKUNQVlTTUlUq2LyjvJQWkOjnKyQ7vlXBeD5EyNE-3QEu313jaRMbmMbYjWD_7qV33lp0h46U0DIbNH7yFJXOwS30n4y3goMqMqpKSz_EDoI31Y6QZ3jmzWpWAKOECUfeQ250tHDbPbG33F6vmgdSuZmPNJA4bTw3cZ8gUC5_GzfO2CmmqvsL0K2_0dlKEREamv0YWBrw_ZLfEuUpeIhI4WQcJqJjd9UQk5sidYOzXJAZkhaFf2NYYn-vhsFewshyC4c5Uee71l-bzgyz7W8hF1-JZ5N6awQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک جت جنگنده رادارگریز F-35A نیروی هوایی ایالات متحده در حالی که نیروهای سنتکام همچنان به اجرای
محاصره دریایی علیه ایران ادامه می‌دهند
، بر فراز آب‌های منطقه‌ای گشت‌زنی می‌کند. تا امروز ۱۵ شهریور، نیروهای آمریکایی 92 کشتی تجاری را تغییر مسیر داده‌اند، 3 کشتی را غیرفعال کرده و 2 کشتی را توقیف کرده‌اند تا از رعایت دقیق این قوانین اطمینان حاصل کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22426" target="_blank">📅 15:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22425">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">منچ‌ اوسینت : از صبح امروز دست‌کم ۳ نفتکش هنگام تردد در مسیر جنوبی تنگه هرمز، پس از شلیک هشدار نیروی دریایی سپاه، تغییر مسیر داده و برگشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22425" target="_blank">📅 15:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22424">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رویترز:
اوپک‌پلاس امروز در حال بررسی حفظ سیاست فعلی تولید نفت برای ماه اکتبر است و انتظار می‌رود افزایش بیشتر تولید پس از ماه سپتامبر متوقف شود. رویترز می‌گوید
جنگ ایران و اختلال در صادرات نفت از تنگه هرمز
یکی از عوامل مهم این تصمیم است؛ در عین حال اعضای اوپک‌پلاس همچنان پایین‌تر از سهمیه‌های تعیین‌شده تولید می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22424" target="_blank">📅 14:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22423">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خبرگزاری i24:
ارتش اسرائیل امروز یک رزمایش ناگهانی و چندجبهه‌ای با نام
«Breaking Dawn 2.0»
آغاز کرد. این رزمایش به دستور رئیس ستاد ارتش اسرائیل انجام می‌شود و هدف آن سنجش آمادگی نیروها برای سناریوهای همزمان در چند جبهه و تقویت توان ارتش برای مقابله با تهدیدهای ایران عنوان شده است. پیشتر افشا شد که
ایران در حال آماده‌سازی یک حمله هماهنگ و چندجبهه‌ای علیه اسرائیل
است که از نظر ابعاد و هماهنگی، با حمله ۷ اکتبر مقایسه شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22423" target="_blank">📅 14:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22422">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c2c28d2cd.mp4?token=rw0-1Q-njscjs7uIhyecHXY9-Y92mfCmthXQ_9BBVKHXYVkqEPRiCo2uYCSuo1G-rvUs9u-iPxJ-1-cbaLHmm_8WgusM_uNRb8JVRdCMvQ063LrHGSkRs8VzUvKEmo2nH7ZbJcxhLtkbN7_8N3_MFv7RXT_LDXONtAZJpx723_Jsf99ddBl-RowC_HRLaU5yfSrYvfb9p7MrXRixL2eb6iiXsBVocrvOAVajhO4frIVqPiS3O5B6h3g9zGcN3W2EcwW4AsffbAmAt09sj0fKBrRD7HzaZ18QDaUQ7MAa0n020QHaesA4hHvly_Jr7RsA7M330OYjOuUpEPZbWV1gKC1VUldVi2dzMR1uJN5G8bgwf-7UtROx9JJuUl1mumr6baDZtdLV0MmPrrRywpVCxBsM7J4k0VzkLT7_CC6j7V31WlbtxzZYX_FOR1vEFPEzItIMjfsWufFBLP9WCSavwqG7eil1q4U8YS0GTZknG54zrpKNDus1HvSdbaxqkVr26x-q3wNbOW0AQJyqoU7zCYwbJJw5kUpWvNMekC11I69eNlwfzrdfJF3nd59R9zgKRNNnVPNE0PeJVaoprTQSlHJwZv3TIzVpm6RX_poTZ7wyaGaKsZlUNj_YllQpnbPAmhaz01K5LGkLPmgpzXWC-iQmkePmwq0v8dQN7fPoEoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c2c28d2cd.mp4?token=rw0-1Q-njscjs7uIhyecHXY9-Y92mfCmthXQ_9BBVKHXYVkqEPRiCo2uYCSuo1G-rvUs9u-iPxJ-1-cbaLHmm_8WgusM_uNRb8JVRdCMvQ063LrHGSkRs8VzUvKEmo2nH7ZbJcxhLtkbN7_8N3_MFv7RXT_LDXONtAZJpx723_Jsf99ddBl-RowC_HRLaU5yfSrYvfb9p7MrXRixL2eb6iiXsBVocrvOAVajhO4frIVqPiS3O5B6h3g9zGcN3W2EcwW4AsffbAmAt09sj0fKBrRD7HzaZ18QDaUQ7MAa0n020QHaesA4hHvly_Jr7RsA7M330OYjOuUpEPZbWV1gKC1VUldVi2dzMR1uJN5G8bgwf-7UtROx9JJuUl1mumr6baDZtdLV0MmPrrRywpVCxBsM7J4k0VzkLT7_CC6j7V31WlbtxzZYX_FOR1vEFPEzItIMjfsWufFBLP9WCSavwqG7eil1q4U8YS0GTZknG54zrpKNDus1HvSdbaxqkVr26x-q3wNbOW0AQJyqoU7zCYwbJJw5kUpWvNMekC11I69eNlwfzrdfJF3nd59R9zgKRNNnVPNE0PeJVaoprTQSlHJwZv3TIzVpm6RX_poTZ7wyaGaKsZlUNj_YllQpnbPAmhaz01K5LGkLPmgpzXWC-iQmkePmwq0v8dQN7fPoEoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولودیمیر زلنسکی : «روسیه اجازه نداد هیئت آمریکایی با هواپیما وارد اوکراین شود، با وجود اینکه فرودگاه‌های ما برای ورود آن‌ها آماده بودند.»
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22422" target="_blank">📅 14:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22421">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گاردین:
لئون پانه‌تا، وزیر دفاع پیشین آمریکا، امروز هشدار داده جنگ ایران ممکن است
شش ماه دیگر نیز ادامه پیدا کند
. او سه مسیر احتمالی برای ترامپ مطرح کرده: عقب‌نشینی، ادامه جنگ فرسایشی و حملات مقطعی، یا تلاش برای به‌دست گرفتن کنترل تنگه هرمز.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22421" target="_blank">📅 14:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22420">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e392ac131d.mp4?token=obxzvwYgSP-TQb32g5zf_MkqvczlW8TtoIQ2nwIST8JjU7wY7D-QxYC0H6z7Owx9tsR4ae_TXkBnFQr0sUTAKD7SS8ZkxIcul-xY5YTxEgz7Oza2mMmBTdp0_K1F4w4G6KsU2PvxMxCYI569IrZs_G5ssOtkCSU5s_vJzxPPcgj0WrXQ8-nJXbwbgwAp83Ga9WFrE0a4iSErecOnjSoWEfNeBKhL9dNImgKYe5f-67gaSoUihnRlGoGvGhYHJPXQyDZeB6HaNceGSvXqkPNGZnsNHRA2zJ69lyy7pkzBu18emLlkN24GMGTo6ut0YGgvOIKFK_636oW0-jPQo7ksRkBlRm7NHbTaxmjnowyRYRjCyuxcxa-lj-MWG4GBqyXaW8ymxX_CxEQpP765YD4dvfCgbLOUeTqIuarZq_x-K9FR1BvjkXUQtylUW_BSuxQ4b45wh95lojftrLMVgcLURNwI0Ia6Hsac8evzwf_EDmixphuVJDK1e4RSOMaVOoZ56YLYa1nl4X7Wb8ubcDeqAbpQQp6QDsIGQ0SqJElxGQbEYOQ74gYbnfNW-I93F4KLo3E9E4e-sNSQTeZazj3Q375hO1KxkVJ5X1iQedkdxTfEZj-4m8AwQb4cQgJz6C7kDkCRPU3zO7OIe3n8ANKRmUc43ypCkWwhvhEjSitV1HM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e392ac131d.mp4?token=obxzvwYgSP-TQb32g5zf_MkqvczlW8TtoIQ2nwIST8JjU7wY7D-QxYC0H6z7Owx9tsR4ae_TXkBnFQr0sUTAKD7SS8ZkxIcul-xY5YTxEgz7Oza2mMmBTdp0_K1F4w4G6KsU2PvxMxCYI569IrZs_G5ssOtkCSU5s_vJzxPPcgj0WrXQ8-nJXbwbgwAp83Ga9WFrE0a4iSErecOnjSoWEfNeBKhL9dNImgKYe5f-67gaSoUihnRlGoGvGhYHJPXQyDZeB6HaNceGSvXqkPNGZnsNHRA2zJ69lyy7pkzBu18emLlkN24GMGTo6ut0YGgvOIKFK_636oW0-jPQo7ksRkBlRm7NHbTaxmjnowyRYRjCyuxcxa-lj-MWG4GBqyXaW8ymxX_CxEQpP765YD4dvfCgbLOUeTqIuarZq_x-K9FR1BvjkXUQtylUW_BSuxQ4b45wh95lojftrLMVgcLURNwI0Ia6Hsac8evzwf_EDmixphuVJDK1e4RSOMaVOoZ56YLYa1nl4X7Wb8ubcDeqAbpQQp6QDsIGQ0SqJElxGQbEYOQ74gYbnfNW-I93F4KLo3E9E4e-sNSQTeZazj3Q375hO1KxkVJ5X1iQedkdxTfEZj-4m8AwQb4cQgJz6C7kDkCRPU3zO7OIe3n8ANKRmUc43ypCkWwhvhEjSitV1HM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تفنگداران دریایی و ملوانان ناو آبراهام لینکلن، مشغول عشق و حال در کلابهای  پاتایا، تایلند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22420" target="_blank">📅 14:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22419">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فایننشال تایمز:
آمریکا طی چهار ماه گذشته یک عملیات پرخطر و محرمانه برای مین‌روبی تنگه هرمز انجام داده؛ این عملیات با مشارکت نیروهای ویژه، قایق‌های رباتیک و زیردریایی‌های مجهز به سونار انجام شده است. با وجود اعلام ترامپ درباره پاک‌سازی تنگه، کارشناسان هنوز درباره ایمنی کامل مسیر تردید دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22419" target="_blank">📅 14:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22418">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">رویترز:
ایران اعلام کرده نیروهایش یک شناور بدون‌سرنشین آمریکایی را هنگام تلاش برای ورود به تنگه هرمز هدف قرار داده‌اند. آمریکا هنوز این ادعا را تأیید نکرده است. این اتفاق یک روز پس از حمله آمریکا به سه نفتکش ایرانی رخ داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22418" target="_blank">📅 14:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22417">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">افزایش ۲۰ هزار تومانی نرخ دلار  دولتی:
۱۰۰۰ دلار با کارت ملی نرخ ۲۲۰ هزار تومان
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22417" target="_blank">📅 13:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22416">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/025828335d.mp4?token=rTB-OzzHHNZqJuT0CqtJWk0rnIZkq7maWIhhm_qyzS3iEJ0ytZX8R1tdsvY2ExAEwkXW3aMFJ_uF0gl_PMrWJ-OUZ3PIrtio9fZk9yNKz3bT-SXHMEC9jhj4cQorYW7A80xFVbDlhbvdj99Ent_IaspNm0qn_eEiYE3a6ibgyZG9HtitN18GDa9IOggUm_F6X334H9q92gM4A97YIN3S7aSMJBZpjqvdBvsUgYVJjL7Q84HY5Wu7LbVuLR0TJTOt4aBaSr6t5QOurULZ3UAvFBGuJ4c-sXVGg_Cj_o5V2x5ISXY3I7EGpwcAxqfq_2lwI9ESPmdiVqeI9-Z0m3E7UXu9hvDmVM9WZbTjuz7JKcBxRc4tmnjyfOASmpREyQeHNnefB4rSmjim4JO9yIMhNb8zJ1HQYdyaCnHo6gZ08GR5FIoHNxA1JTgmeFaQwk6cdBib90xM12PI_RjkWWQEM5QlHBheXM-CUM7bB6M2ORLL-xo4HzHbPY520ZaocTrZqwTBbRruHE8lAxqeNv0ntL59S4OQVsDTjNRTxGP4_s5JrKslP9l6QwxlrVqYMzPhz7O3piGJoPMuo_LpAqvckKqVRRAxs4wYKXXX46ENuQOjvLKdTqa_aDbBmS3Ft9_ur1Qd4099DHPCIZ3SHsHnQ1PU3enr91dK0sUgwC-8vaY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/025828335d.mp4?token=rTB-OzzHHNZqJuT0CqtJWk0rnIZkq7maWIhhm_qyzS3iEJ0ytZX8R1tdsvY2ExAEwkXW3aMFJ_uF0gl_PMrWJ-OUZ3PIrtio9fZk9yNKz3bT-SXHMEC9jhj4cQorYW7A80xFVbDlhbvdj99Ent_IaspNm0qn_eEiYE3a6ibgyZG9HtitN18GDa9IOggUm_F6X334H9q92gM4A97YIN3S7aSMJBZpjqvdBvsUgYVJjL7Q84HY5Wu7LbVuLR0TJTOt4aBaSr6t5QOurULZ3UAvFBGuJ4c-sXVGg_Cj_o5V2x5ISXY3I7EGpwcAxqfq_2lwI9ESPmdiVqeI9-Z0m3E7UXu9hvDmVM9WZbTjuz7JKcBxRc4tmnjyfOASmpREyQeHNnefB4rSmjim4JO9yIMhNb8zJ1HQYdyaCnHo6gZ08GR5FIoHNxA1JTgmeFaQwk6cdBib90xM12PI_RjkWWQEM5QlHBheXM-CUM7bB6M2ORLL-xo4HzHbPY520ZaocTrZqwTBbRruHE8lAxqeNv0ntL59S4OQVsDTjNRTxGP4_s5JrKslP9l6QwxlrVqYMzPhz7O3piGJoPMuo_LpAqvckKqVRRAxs4wYKXXX46ENuQOjvLKdTqa_aDbBmS3Ft9_ur1Qd4099DHPCIZ3SHsHnQ1PU3enr91dK0sUgwC-8vaY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارگران تایلندی لایه‌هایی از جلبک را از ناو هواپیمابر آبراهام لینکلن پاک کردند این ناو هواپیمابر پس از استقرار طولانی در خاورمیانه، به طور کامل تمیز شد و بازدید خود از بندر لائم چابانگ تایلند را به پایان رساند و به جنوب چین باز میگردد تا در مسیر خود به سمت سن دیگو بازگردد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22416" target="_blank">📅 13:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22415">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وال استریت ژورنال : ‏
در نبرد محاصره، زمان دیگر به نفع جمهوری اسلامی نیست
.‏ ایالات متحده به کشورهای خلیج فارس کمک می‌کند تا مقادیر قابل توجهی نفت را از منطقه خارج کنند و در عین حال مانع از انتقال محموله‌های تهران می‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22415" target="_blank">📅 13:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22414">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">قشقاوی در گفتگو با الجزیره: جنگ فعلی برای ایران یک جنگ موجودیتی است. ایران درخصوص پاسخ به حملات آمریکا به نفتکش های ایرانی ذره‌ای تردید نخواهد کرد!
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22414" target="_blank">📅 12:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22413">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نیویورک‌تایمز: دولت ترامپ در حال بررسی طرحی است که بر اساس آن،
خانواده‌های متأهل با یک والد خانه‌دار
نیز بتوانند از یارانه فدرال مراقبت از کودکان استفاده کنند.
این کمک‌هزینه حدود
۹ هزار دلار به ازای هر کودک در سال
خواهد بود و از یک صندوق فدرال
۱۲ میلیارد دلاری
تأمین می‌شود که در حال حاضر عمدتاً برای کمک به والدین کم‌درآمد جهت کار یا تحصیل استفاده می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22413" target="_blank">📅 12:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22412">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بیش از ۵۰ هزار نفر شامگاه پنجشنبه در مراسم مذهبی «سلخوت» در محوطه دیوار غربی (دیوار ندبه؛ بخشی از دیوار حائل محوطه کوه معبد در اورشلیم) گردهم آمدند و به دعا پرداختند. بنیاد میراث دیوار غربی اعلام کرد که از آغاز ماه «اِلول»، بیش از ۵۰۰ هزار نفر در مراسم سلخوت…</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22412" target="_blank">📅 12:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22411">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دیدبان اتاق جنگ با یاشار از جنوب خلیج فارس نزدیک تنگه : در همین لحظه سوخترسان آمریکای در حال سوخترسانی‌به دو جنگنده آمریکایی ، چیزی که ما در صفحه مانیتور نمیبینیم ! @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22411" target="_blank">📅 11:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22410">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بسنت: محاصره و تحریم‌ها قدرتمندترین فشار اقتصادی تاریخ علیه ایران است تنها حدود ۳۰ میلیون بشکه نفت خام ایران باقی مانده که چین هنوز آن را خریداری نکرده، این مقدار به زودی تمام می‌شود و دیگر نفتی نیست که چین بخواهد بخرد @WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22410" target="_blank">📅 10:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22409">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بسنت: محاصره و تحریم‌ها قدرتمندترین فشار اقتصادی تاریخ علیه ایران است
تنها حدود ۳۰ میلیون بشکه نفت خام ایران باقی مانده که چین هنوز آن را خریداری نکرده، این مقدار به زودی تمام می‌شود
و دیگر نفتی نیست که چین بخواهد بخرد
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22409" target="_blank">📅 10:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22408">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTip72x3YdIMVxqFpclrsrQzxgc2kaM4D9ePAu25Un1Ch1F7VTYhphcKFXNEe7T4B3Yz-SLg_USizJ9KOLxTFwmKoyvcRx4Rm11uqbuV31_9-W_DV5F_ehGfo35MfmjP0F2vnGi7PY5RrueuviAV4HnL-Mp0-dWuj5NMFePF-eQVFNqY87muEumkCygc4WUcBY3ZdpEhRCI-X5xuE-q_AU6dpr9m4A4YxVk3phl03WKdkbUrnUUhVYyQtJENQ7rSl2Aoh7_EdVFoIDtB9DB1eaThu_ylWPLrq07ccLdtHHoI7B0Kw69mg3hzFjN8Vgr42cR3y1tpcXe37z929tCY4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : بسیار تأسف‌بار است آنچه در اسپانیا در حال رخ دادن است؛ کشوری که
ه
یچ کنترلی بر
مرزهای
خود ندارد. واو!
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22408" target="_blank">📅 10:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22407">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دنیس راس، مذاکره‌کننده و فرستاده پیشین آمریکا در خاورمیانه، هشدار داده است که
احتمال دارد تنش‌ها در خاورمیانه به‌زودی تشدید شود
.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22407" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22406">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مارک لوین در واکنشه حمله آمریکا به نفتکش در جزیره خارگ : «در حال نزدیک شدن به مهم‌ترین هدف اقتصادی در ایران؛ منبع مادر ثروت.»
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22406" target="_blank">📅 07:20 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
