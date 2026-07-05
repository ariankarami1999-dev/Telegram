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
<img src="https://cdn4.telesco.pe/file/gmu0VEvnl7kkk6B3DNeqq3ZS-pldL5X1bIP7IpaMYvIuGHesme0UIMMNKxWBvnHo0VS_gDXoNGZt8PuR7wIdo-zNGnb8FBqQH-tOmqyeXzKkVHZgImNnHMbMGdvrVDMf2MS15TLYCDYfhQdY-ZFnqjZbwE71FJMg3hk0Grg_sTIIOl2uqOXHSAIA-1ai4yg2QiuC9u_hqnvIFb9i_u_2P13ju8RMktUp3Arg2N1dGg9uQUgMjYH_lkvHRLOGU5AEZcXLrg4D7K-xaijVA5his3rrIR_UwXB5lAW0oV9aRhhH6iZk4XQiHnfJw91B0kGgOAe0wpKJYTlNa0bJlclluA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.27M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 11:56:41</div>
<hr>

<div class="tg-post" id="msg-666877">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjnMI71BRGyTqQL4oz9ajGCynPP5Md8k7hA-DlwnliW7NPAHJsTFqS1LZ7bU1QWK2ibQpeL82SUbWlLHb4MRDbccDoopv9vD0ttFqK0y-Q2wCv6Bp8cDCNEtJxvL1wVbJEwxz4xgWRmSKA2ElXZJoj7fhtZe05v7Xnke_dqQecQbkUBVuCmMzOE2w7VBTueGteRgWvp6XKiO7ggkw6I-Erjq-N7ENuZxPiwUnKoimMALPBdN4_Q62qBsJnjeWteHV5L3v1wqO5OkQfxrJRnvmcQOZHj7kA_Dod5cIkmEtBvg31xUTl-GxY5XB_S_-GJzcXXI643JACoqvbI8_cNCVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥀
به امید دیدار
آقای شهید ایران
ما پا به رکابیم پدر تا برسد یار
ای رجعت تو ناب‌ترین لحظۀ دیدار
#رهبر_شهید
@Heyate_gharar</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/666877" target="_blank">📅 11:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666876">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
هشدار انصارالله به ائتلاف سعودی درباره هرگونه تحرک متجاوزانه علیه یمن
🔹
محمد الفرح، عضو دفتر سیاسی جنبش انصارالله یمن نسبت به پیامدهای تشدید تنش هشدار داده و تاکید کرد که یک حمله ما علیه عربستان می‌تواند آنچه را که این کشور بیش از ۱٠٠ سال رویای آن را در یمن داشته است نابود کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/666876" target="_blank">📅 11:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666875">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس‌جمهور پاکستان، هم‌زمان با روز استقلال آمریکا، از دونالد ترامپ برای سفر به پاکستان دعوت کرد.
🔹
ترامپ پیش از نشست ناتو با پوتین و زلنسکی گفت‌وگو می‌کند.
🔹
داروخانه‌های کشور در ایام مراسم وداع فعال هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/666875" target="_blank">📅 11:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666873">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
‏
سخنگوی ارتش: هر خطای دشمن با پاسخ قاطع نیروهای مسلح ایران روبه‌رو خواهد شد
سخنگوی ارتش:
🔹
اگر دشمنان خطایی کنند حتما با پاسخ کوبنده و قاطع نیروهای مسلح ایران مواجه خواهند شد.
🔹
بارها اعلام کرده‌ایم از فرصت آتش‌بس برای ارتقای توان رزمی خود استفاده می‌کنیم و یک لحظه را هم از دست نداده و غافل نمی‌شویم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/akhbarefori/666873" target="_blank">📅 11:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666872">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdxsKpBANhH7xoYinj-J52OjRpPLAL4qPp9r-bOxlGj2lWCNTS72OUvoynYgYcLVVOFFWKKPY_fesBLRt_F0GrxFg1R2tj7Xbu29gEJwYWj6Tw0nQZ7wbwAiIO3M5kLYIK5jsD7PgBp267opgDYEy_mRTfePp9moDydqZIZ9qYZGtMawIfKnCFetREGRPJV2iCJf7hG3QxjGgtM6L5Fat1fxje9YmSZSuFYLVzoa3yl9VY2J94EaDPxshR6z3keoYfkIwteOGehIz2wOYU7kE505dXaxUEOqdKJsehvsQn_bi-ST9-AOWcQXI1FCuHt6KjVrGxFGfc32Pnos65r9Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باشگاه پرسپولیس مذاکرات مثبتی با مهدی تارتار، سرمربی فصل گذشته گل‌گهر سیرجان انجام داده و این مربی در آستانه امضای قرارداد با سرخپوشان قرار دارد/ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/akhbarefori/666872" target="_blank">📅 11:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666871">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
زمین لرزه شدیدی شهرستان بستک در غرب هرمزگان را لرزاند
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/akhbarefori/666871" target="_blank">📅 11:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666867">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tExnkx7dxBQ-RWsNI7N1vQl9Zkz3EK5jGsbYZ4ZjkjT_p_8OJfKwNjc4xdNG7qcTo4QLiIbxbXuwebnOURMmzLgppEPw5aeRoYOscGosw1v0eoAoBcfzQiezxbS62f8jBermgZu9dkEbf0DBlS1LWjuZkllLSVdKtBm1CT3v6brg4oPN3P5IW7_WcVgPZxPqrGVYaXuRXBJcYaG_KvdCQvrZSrNhN7PLhsI_IHgJEXSE9NR7uFfVLL_cx0U2EwnFmTuo6iGZJX5ZQrDBO1xoGPhF0eAfOmWcmeP0efJgpxDwWsYc07mkOO05ImqoW0L9aAHMo87qrR2eBVZ_Fcu1Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oqWgsQhSR26Ph0xFMyy0AIPaE4wStCam_Di3vxYIr3z7YfLFzWPfh87scoAbGdTBDnvLMqYwCRxs377Se9YaIyPQEJcqnfARXL1sV7CBhtom1mIIz6wDHTjCpT0nQR3VYaHc1dxjExCAGwNYNVe8rYqV3JAz1NRNebO5BvZ2WGn8qgMx1kZuw7bK8XrCKjTol8ldrD3TVIdFKWEVLPEVZXVUkebpAAOrzhqmC9MYG-7xIYLeJ9_poZHSfZBSclggxQpG-bCpq_6Eic4y4qg0HOpBtMwyMtz9ytk7uGUNZjMahBTIgsBYbEZo4wqxCyOaquykBwRUUNb8ATMsMuDkOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_Z0fPTsh0TVMzxjTvcTqD1Pm9DM8iEq-qSrxi-hAY2lpwLyG5AoRi39ob7REPlAAcoYYmMVp6ZWcSODAjL6bIFfeAzxrKk6kd6Xa-IRAqZgY_lxxNjKvCk-6mpaaWZP15qJ2SAmzN6ujF1-hqrh5iwaGAL9d_fwYWgy7vZ5z99mr-GuDr5YUJ9JHzy3aXFFMBPmf6mKwcSvYm4Pm4yL37YwL3ETFqwRJ1rojmQF7IaCyrfQ1oJOk36nXJXCX0AE7Uy28CTxlEJC6oa_vtrBsWOFTZdN1iSE8QmKxgMkp04R976huTclW-SrPbpNb821z2dssWryxexZEABcEtrZSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hoHXi6rcBY7fw6oy-a3ra-weS0TRYsb73s0E-HBTdochJH6Mo0mlrLj9VXZmtqiudkO29r9GysKJQIVvNqHel_bZh3HGwgYnqH9QJCDfmIfndslR8ddWtTE7TybdqzG5Vo7zM48Vz_HJoU8ZU2MwxN-9vS8vRH_eHtyYQ_LCUWHhiRuLuSpDIDh0owMrVodsPwOcpcqTstwCIlByjx8I7_1Pv6gcevIiki3YqmWo5hiBTpjYVqumvl7fNAxjy7UC9842kqP481F3ACNJdpTk_iszEnpYVtDc-qIdj9iZ9E60Miq7vTUmBEKSYPOLNccNcdQN0br0LiiS7-ntXxSjOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از یک حضور تاریخی؛ جمعیت باشکوه مردم در مراسم اقامه نماز بر پیکر مطهر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/akhbarefori/666867" target="_blank">📅 11:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666866">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9429f0e319.mp4?token=CpxYIFbo7QOODcEr7R9o516ZYnlRgHWmJHkBc-2NkXE3Am34MY8PMTVaR-I-5JRCwOWyoTgbBro7fBEcZFN6znUXt4Ql9DmVhmMWJFMAtAFSkqfmpm5aP-zO8QLbXejF4yd-jkm5Y626v_Sih8BCCbKPf_FujDxF8wsRuyNSw04igA4todffLdvHWKnRWrYih57axs9BqX2gGgBl7bhzEnKS9ZJWe-lAhkdA3vf5kcxOE5nZJhZnxP2QssCUUyk2y3Gvfn2SKzF_IbGBCiY3W676Enq7urkiWcK9naRJ7i5_8-JYzDwTEY97GzyzG6SxttNMCftsIyi9P-83Y9K-5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9429f0e319.mp4?token=CpxYIFbo7QOODcEr7R9o516ZYnlRgHWmJHkBc-2NkXE3Am34MY8PMTVaR-I-5JRCwOWyoTgbBro7fBEcZFN6znUXt4Ql9DmVhmMWJFMAtAFSkqfmpm5aP-zO8QLbXejF4yd-jkm5Y626v_Sih8BCCbKPf_FujDxF8wsRuyNSw04igA4todffLdvHWKnRWrYih57axs9BqX2gGgBl7bhzEnKS9ZJWe-lAhkdA3vf5kcxOE5nZJhZnxP2QssCUUyk2y3Gvfn2SKzF_IbGBCiY3W676Enq7urkiWcK9naRJ7i5_8-JYzDwTEY97GzyzG6SxttNMCftsIyi9P-83Y9K-5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظاتی از شعر خوانی محمد رسولی:
‌ کسی که کشت امام مرا چرا نکشیم
که ننگ ماست اگر قاتل تو را نکشیم
از این به بعد کفن، جای جامه بر تن ماست قسم به خون تو، قتل ترامپ گردن ماست
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/akhbarefori/666866" target="_blank">📅 11:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666865">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSTt7Gxjr-xN_ksWvhxrRxNqCez3y2ZIeL5PIfHSzI4nsCcOW5mlkZ_BSk4eH6mlGRYNVOGCSGvVxgKEtcnneWfdSSex33YuSF0-oXVxh7WALhzGXWveoA1L43QkaOZruXJdZRoXwp-udN6DvLb4hBKiA06R0_HP99TAnUYnNief-ueRgPW83AGkmc1EmYLn1Be6td4M04w_x9o-1O_MvsqOxdCC8t7GBABM1dmh8nEK08uwDAhVdBlt9e-AZ-nM_0xaJV6AFbdKRayDxI8aJ_xL1T822XT_TWbCUdc3crMTiPs3IlkEInw1Ka4qgco3lOpZVE0W4vOW56f1MROC0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استوری امیر قلعه‌نویی سرمربی تیم ملی فوتبال همزمان با وداع و بدرقه میلیونی ملت ایران با آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/666865" target="_blank">📅 11:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666864">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
خداحافظی اولین میزبان از جام‌جهانی/ مراکش متفکرانه و مقتدرانه در یک نیمه کانادا را برد
🇨🇦
0️⃣
🏆
3️⃣
🇲🇦
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/666864" target="_blank">📅 11:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666863">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3235b035b4.mp4?token=Ja9G5UO2HcB76E1yv5_5fPs94Hw7gz3jrDTJ5Ek1hIMStR34l8Z4dxNwOJx5xabwk_2eBEVmt0WtiDBIaT5QExSM7LSH2eV663ZqVk0214j_ijD24u6qwXPt-YPWG_BJGDWeVzbcj5Db_uoXTwA9NMs9MH3n-luzqAsNn6olJ40jHVkahPrrg65Fdg5FzW-40BQEH2fgIDxSzay7NTr9oeINs7r5VDz1zk2Nj9qpiKQEVhpnlnPspf3Wuuwyj9n_LpOZ4mBCmlNz3udCL65G0gc7lVdKU2YK8F7ckZ1q82aVsWo19HNKFwgaIYJRgKDsiCVyiUApoijah01HZiJRFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3235b035b4.mp4?token=Ja9G5UO2HcB76E1yv5_5fPs94Hw7gz3jrDTJ5Ek1hIMStR34l8Z4dxNwOJx5xabwk_2eBEVmt0WtiDBIaT5QExSM7LSH2eV663ZqVk0214j_ijD24u6qwXPt-YPWG_BJGDWeVzbcj5Db_uoXTwA9NMs9MH3n-luzqAsNn6olJ40jHVkahPrrg65Fdg5FzW-40BQEH2fgIDxSzay7NTr9oeINs7r5VDz1zk2Nj9qpiKQEVhpnlnPspf3Wuuwyj9n_LpOZ4mBCmlNz3udCL65G0gc7lVdKU2YK8F7ckZ1q82aVsWo19HNKFwgaIYJRgKDsiCVyiUApoijah01HZiJRFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویرسازی با هوش مصنوعی از حضور شهید علی لاریجانی در آخرین دیدار
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/666863" target="_blank">📅 11:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666862">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/553d716180.mp4?token=NfILKZPz43tYuLlXnKlDbpyVepLMwdz1FSM8ZIsuTteRwisQJU2ukiWV9ZwrKPKL26iMLItv2raWc_ZcD1m9SFAKGSsVXgSI5CqgZgj7bdqYHk2OVKIycwJMSa8mzHMtyS0r-xT0QJpBXcDrMOkKVOVifV_gjDcQh8V-tAqxuWWT2OR5F54jJxjcOT98Cilc6ClaSKAbxCvuVe94igvbgUxiIgIn_t64w_0VyL-Kid5K8ejmCKG68FM48mEUn7mP7XNamwIIiOvatEnXfojlxR0r642OEJfUHBUxPi-Zq8wi1LTYM_8BeUFog4ufIwYrjsKc-ivELVGonpY8ZMjyzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/553d716180.mp4?token=NfILKZPz43tYuLlXnKlDbpyVepLMwdz1FSM8ZIsuTteRwisQJU2ukiWV9ZwrKPKL26iMLItv2raWc_ZcD1m9SFAKGSsVXgSI5CqgZgj7bdqYHk2OVKIycwJMSa8mzHMtyS0r-xT0QJpBXcDrMOkKVOVifV_gjDcQh8V-tAqxuWWT2OR5F54jJxjcOT98Cilc6ClaSKAbxCvuVe94igvbgUxiIgIn_t64w_0VyL-Kid5K8ejmCKG68FM48mEUn7mP7XNamwIIiOvatEnXfojlxR0r642OEJfUHBUxPi-Zq8wi1LTYM_8BeUFog4ufIwYrjsKc-ivELVGonpY8ZMjyzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظات انتقال پیکر رهبر شهید انقلاب به جایگاه اصلی مصلی پس از مراسم اقامه نماز امروز
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666862" target="_blank">📅 11:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666861">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202c4042f3.mp4?token=s7ZvWgOL9UgrxHFc1uCxssIpBdvM5wac74fB5DnB-UgsFElW1JCkxxDFrfoaxDyRIWX1K58vBa3W8QjDdYC-ePFBlHGTEDFVWLj-PvwlJKiRIXapFuJy0euaKwE_IXwQSSSLL1yPfb7YlGVoxtIPlSC43Znr5NQvrUh2jP-V9PBivbe8SWd3zVYRVdoDj6-y3Q0OL71dzj1pu0GWac12yrC7OumVgsVYd96mIKiylEbfExvpmzfspr-1Qvl2f3CqY3l3B_zo0oe4PGCBGhU0Na0DMhexi6RjI2xx3vsnyv4dh5SOwMKRi8IBAstAFv77AwXmTmstbFYJDy4y9IJqwFG3g_c5NfYpsoqUVNb_d0gy1tKTSAVNXbky7kFYwUxNgCv_0_OytbHfMUB8IANwJXzRXSOm4x-I-8S4HiCDuGwErc3vu8A5TVItEGutnt1p6nWjvkOOSO612gXws0VPS6P6oB_SQx9VXtAGPvziQqI2DWULyuoOuZBFPcUyykdMJRTk8LKAKq3Ij_eE7On28SrX_O4AKm1epg53d_b6n2DWPn2FUyrIsJM9Ti0HhvLILGq-I4mJSIaktCIxE8Zaqx0InAeipumK4APscZVADvdPqaaWDrCiMGFk8u5QOpG2JgyQj4qtFvYr5qz5ZfBEdAPx4SyzNhS1c2URUI_hUGE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202c4042f3.mp4?token=s7ZvWgOL9UgrxHFc1uCxssIpBdvM5wac74fB5DnB-UgsFElW1JCkxxDFrfoaxDyRIWX1K58vBa3W8QjDdYC-ePFBlHGTEDFVWLj-PvwlJKiRIXapFuJy0euaKwE_IXwQSSSLL1yPfb7YlGVoxtIPlSC43Znr5NQvrUh2jP-V9PBivbe8SWd3zVYRVdoDj6-y3Q0OL71dzj1pu0GWac12yrC7OumVgsVYd96mIKiylEbfExvpmzfspr-1Qvl2f3CqY3l3B_zo0oe4PGCBGhU0Na0DMhexi6RjI2xx3vsnyv4dh5SOwMKRi8IBAstAFv77AwXmTmstbFYJDy4y9IJqwFG3g_c5NfYpsoqUVNb_d0gy1tKTSAVNXbky7kFYwUxNgCv_0_OytbHfMUB8IANwJXzRXSOm4x-I-8S4HiCDuGwErc3vu8A5TVItEGutnt1p6nWjvkOOSO612gXws0VPS6P6oB_SQx9VXtAGPvziQqI2DWULyuoOuZBFPcUyykdMJRTk8LKAKq3Ij_eE7On28SrX_O4AKm1epg53d_b6n2DWPn2FUyrIsJM9Ti0HhvLILGq-I4mJSIaktCIxE8Zaqx0InAeipumK4APscZVADvdPqaaWDrCiMGFk8u5QOpG2JgyQj4qtFvYr5qz5ZfBEdAPx4SyzNhS1c2URUI_hUGE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای کمتر شنیده شده مادر رهبر شهید انقلاب
#بدرقه_یار
@Tv_Fori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666861" target="_blank">📅 11:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666859">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac8236b59e.mp4?token=It3LF9zYQ7hbTjMuaDeNcEv9f7F1Ji9AmNwlEzbGiro-q1Sg-ipKlHUqI7JPlerpma-nScn3HyKV-y9Dk2Tox-og9mPbcU67KaA5xR4fIFRXsiDcNjaeIIIdwjdfpeV8u9IIp3RUQ9J1ZOdYpnjee9oOTOMb61kuH1kbUA-zV3IMD4gSotsUpksXlw5r3-x-yQtKkkGUdw_4NUrlim86KWPMfi-tdC3PtOry1nQlB7EB7ojU8luLAaOo8vs5SympgZvDfX6XdAj9-WCDni_5_QIm-a1Ezf2uOF54LdJuwCgcHkk8IxmviZFEbUVyIDmjQ67X60WzEt83P360slH_Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac8236b59e.mp4?token=It3LF9zYQ7hbTjMuaDeNcEv9f7F1Ji9AmNwlEzbGiro-q1Sg-ipKlHUqI7JPlerpma-nScn3HyKV-y9Dk2Tox-og9mPbcU67KaA5xR4fIFRXsiDcNjaeIIIdwjdfpeV8u9IIp3RUQ9J1ZOdYpnjee9oOTOMb61kuH1kbUA-zV3IMD4gSotsUpksXlw5r3-x-yQtKkkGUdw_4NUrlim86KWPMfi-tdC3PtOry1nQlB7EB7ojU8luLAaOo8vs5SympgZvDfX6XdAj9-WCDni_5_QIm-a1Ezf2uOF54LdJuwCgcHkk8IxmviZFEbUVyIDmjQ67X60WzEt83P360slH_Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر اختصاصی خبرفوری از مراسم وداع و
نوای حیدر حیدر مردم خوان‌خواه رهبر شهید در مصلی تهران
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/666859" target="_blank">📅 11:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666858">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b347366e52.mp4?token=mmo1-xdX3sdY2gh2puV63FWSLL9nLgP-hgPJcaUZAsQEyP0Es3UCScMFo6d1bijNaz-P4Aocebwlu4sQtOnAxzXyqxKVBmCzLr6qzUVOFd86c87a9fE6fLYrr11txF6deYm6RxUR46heZznMI8HKhS9-Hox-OZ8iUhQW7LXXNWYrtVubQVZeHJlVcwetksITY92E3L6Adwivq85LAdsmQAwWUx94XJu36ZnijDJXsE_O1yu5S4xV3NCdC_xH9wZ-dCUulu8YIQPQdQGYs5faRFqJhiVwfKPkll9OGBPTB4jFgfOXw7g2m2hvljEqcXa6sYcYnMKfqOjPUQvXaTTiVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b347366e52.mp4?token=mmo1-xdX3sdY2gh2puV63FWSLL9nLgP-hgPJcaUZAsQEyP0Es3UCScMFo6d1bijNaz-P4Aocebwlu4sQtOnAxzXyqxKVBmCzLr6qzUVOFd86c87a9fE6fLYrr11txF6deYm6RxUR46heZznMI8HKhS9-Hox-OZ8iUhQW7LXXNWYrtVubQVZeHJlVcwetksITY92E3L6Adwivq85LAdsmQAwWUx94XJu36ZnijDJXsE_O1yu5S4xV3NCdC_xH9wZ-dCUulu8YIQPQdQGYs5faRFqJhiVwfKPkll9OGBPTB4jFgfOXw7g2m2hvljEqcXa6sYcYnMKfqOjPUQvXaTTiVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فاطمه مهاجرانی، سخنگوی دولت در گفتگو با خبرفوری: تصمیم‌ها در راستای منافع کشور در شورای عالی امنیت ملی جمع‌بندی و اجرا می‌شود و نظر مردم حتماً شنیده خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/666858" target="_blank">📅 11:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666856">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3jQgSXll7USUhu6n0DQc1sMvMsDcIopZ8cnPoWkaErkECOqXP_HcLREni-x3H6a22U6ZGrYOZGTnSc-_Id8Ii5JGi1rxtnyWvR82tmvXRUeMGxSs03NKaODx9z-aGlJdCe8bGsVhLqWBGuK4wuJX7Ttb9sEGM-SX_s-8FGeGTC5fvNVgWm1VGq2wZOatSw5i1AtESwdAo6Wf2MCq9oBS_2DNf9hQgaNBkeYcUsjJiicTIIQ9mCRdRbtF7U1LLs3UqdOrNOJGH5m8hFAQCOBjX6ZiBKsyVPwcGLcEL_7-M99R8A7kBA4l9Z0ZwABOkDWuK9vdLPfTUcEQBywKw0L8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hkj_NRuvu0jJAuMEeldJ6-2fK0GRxqHn8K_S-GbiFE4bZtLWmtklo_6dyzlRQZ8HFNaB4VasRlX6jtGAgWxQ7FeL2exfp21fX0hfnBYHS4aB0MA0YfJT_wfUA8SWlQsYBiLwAAcFBEMnXDIaOvyG96o6ICJpWtk8rwyMGXnREpUtfWbGZTTQ3kOe-6F_lRu8ZbtJfvoKgAeseoXh4_baF1MjZSx5AJkgLltl8KJnvi4BfKrZe88BJ4D4tbbgHKgX8KoGinX0l10w1WnmDvQWK81cye_F5T1HbJCMAp1WSW59ylvJGKbcpJzRGuyZs2E96VxCb_ARaps32zyl4fQCmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
📷
نخستین تصاویر از بوئینگ‌های ۷۷۷ که به‌تازگی وارد ایران شده‌اند
🔹
چند فروند هواپیمای بوئینگ ۷۷۷-۳۰۰ER (مدل دوربرد و پرفروش) که از عربستان وارد شده‌اند به ایران رسیده‌اند. این هواپیماها به‌خاطر مصرف سوخت بهینه و برد بلند، از مدل‌های مهم پروازهای بین‌المللی هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666856" target="_blank">📅 11:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666855">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7pAsrVSjoDlTIhol-zODEohoZEfm9SfoZuLBg4OUx3SCZBGoALj3RnJmKH39naNnVDLXL-7n1gA9xGu1XnG0Vm8sLzqg96sd0xTVKfkKcq7AUmxagOyqpP4NlmbAo8o-qDjMlbH_YOawQk8dDx1O0jKZGNxoHgAL5Zo6rqRPoj0UoU3sH0GjHIr95hoaDx8zxtFEGqz40L2Y878kVNZXYW0F7vZTLAw46NOY10YdfOO0hM2oeWfC6AmXrNoOWUrfeLhbCeUzFWhtppxBHJ98GBarfDqE3T4FOaHbaV-DKHEVQB5lBvUbLaL3AyWZkink2zZPCJA8ORASLvXQXOVhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور رییس کل بانک مرکزی در آیین اقامه نماز بر پیکر رهبر شهید انقلاب و خانواده ایشان در مصلی تهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/666855" target="_blank">📅 11:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666854">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62a7352771.mp4?token=g5HjOwoOGyFn_4TUcnomkAlOdZRWMz33C029xwezyvuQlawUP2DPXX8luZYQ8NU1jrFurTYys-MO3AW6u6vF97g-cYEj6Dy6MmnRhgE_MGKtYfikM4OPX8GmmkTlsVcphZ407IfdeWRGWjx-xlu7XUu0fZXJgb9Y36kbVVNfywrXQS8MHK5jBokbjUvPwZksMzjFfUmQgntF1DvXfO6itoY_K-CVKDKFm6oawxhO_Nkw_Nsz9151ctxRCLkZ4V-PA2YVjv5WLYEkgfcdxHCY6aMpS5u5MJ7x0fTLXYTuvkoV6LzvnKqSdXqkjYk2eDV0RV6jG8oBws19uDpCH8oXtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62a7352771.mp4?token=g5HjOwoOGyFn_4TUcnomkAlOdZRWMz33C029xwezyvuQlawUP2DPXX8luZYQ8NU1jrFurTYys-MO3AW6u6vF97g-cYEj6Dy6MmnRhgE_MGKtYfikM4OPX8GmmkTlsVcphZ407IfdeWRGWjx-xlu7XUu0fZXJgb9Y36kbVVNfywrXQS8MHK5jBokbjUvPwZksMzjFfUmQgntF1DvXfO6itoY_K-CVKDKFm6oawxhO_Nkw_Nsz9151ctxRCLkZ4V-PA2YVjv5WLYEkgfcdxHCY6aMpS5u5MJ7x0fTLXYTuvkoV6LzvnKqSdXqkjYk2eDV0RV6jG8oBws19uDpCH8oXtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انیمشین لگویی وداع با رهبر شهید انقلاب!
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/666854" target="_blank">📅 11:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666853">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
مردم برای حضور در مراسم تشییع امام شهید نگران تامین سوخت خودرو نباشند
سخنگوی صنف جایگاه های سوخت کشور:
🔹
تمامی فعالین به صورت شبانه روزی در تلاشند و تامین و توزیع پایدار سوخت در سراسر کشور برای حضور مردم در مراسم تشییع رهبرشهید جریان دارد و مردم نگران سوخت خودرو نباشند.
🔹
توصیه اصلی ما این است که کارت سوخت شخصی همراه داشته باشند و قبل از حدود ۲۰۰ کیلومتری استانی که تشییع برگزار می‌شود خصوصا تهران، از پر بودن باک خودرو اطمینان حاصل کنند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666853" target="_blank">📅 11:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666852">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa11f8e93a.mp4?token=Dv5ZcWnhuwOlWIur81_veGLDKn3y0s-xxnbPTiEhwkaJMgBuuY-fgiC5tFNbmHhYqpwOtS6-vOgiwUvAnaeLzb9kMK7Zal2b06Q9z44C8wkwVbehrZDUJ8FSAGnbpzrX9CxkGT_-EFD0Lhsm1LtQ4S23SNZ0E56xBgtFU8Vhj4A_IoIIz59XyLb8LSUgSeHhi8mOwUHoVPdZd8trYWF34h_5EwhSmsoAVFIoQDAqPlMlMcWiSMd8vJlsvUbYktXF7zOkhCdGXLE22p_k7oDNfb1WQdThtCHTN4jK3M_vQaYch77k85JmS7v_Jg8QX8BYxG9DB-GdetoRYxIB4gLEcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa11f8e93a.mp4?token=Dv5ZcWnhuwOlWIur81_veGLDKn3y0s-xxnbPTiEhwkaJMgBuuY-fgiC5tFNbmHhYqpwOtS6-vOgiwUvAnaeLzb9kMK7Zal2b06Q9z44C8wkwVbehrZDUJ8FSAGnbpzrX9CxkGT_-EFD0Lhsm1LtQ4S23SNZ0E56xBgtFU8Vhj4A_IoIIz59XyLb8LSUgSeHhi8mOwUHoVPdZd8trYWF34h_5EwhSmsoAVFIoQDAqPlMlMcWiSMd8vJlsvUbYktXF7zOkhCdGXLE22p_k7oDNfb1WQdThtCHTN4jK3M_vQaYch77k85JmS7v_Jg8QX8BYxG9DB-GdetoRYxIB4gLEcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخستین تصاویر هوایی از حضور باشکوه و گسترده مردم و اقامه نماز بر پیکر مطهر رهبر شهید انقلاب و خانواده ایشان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/666852" target="_blank">📅 11:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666851">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fe81201fc.mp4?token=F3TazMHN9BclN7HX55ZE7tfvavC0zsmYVWkpIgg9-HzC37oejjIyTfQf2yv5E4sgyK9cK09ubgne_nrCX5tLOVG0_x0c-xbQ3XikIQnM_8-C8NyhjNdHEHe-a1rfYgAsTBG1d8Uk8E-MzJRPaJ3Fvjec_s_bJThyTocCcIiKICTVHT3hEKRY3BHj-gQ1E0WHPLbwtjoEgSCB_QLoHyjjTuXpg63hoYdvH_pRUfJQFBfUm2WD7l__5rmAvWaZbe2sItd1Kc988AkoJgoqV2-wsEiRVGk8JKzNy-bPCF-kMMqzIbdaGk7HptTaLXmeDm9hmowpRpvcpnGhi6-7ajvGFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fe81201fc.mp4?token=F3TazMHN9BclN7HX55ZE7tfvavC0zsmYVWkpIgg9-HzC37oejjIyTfQf2yv5E4sgyK9cK09ubgne_nrCX5tLOVG0_x0c-xbQ3XikIQnM_8-C8NyhjNdHEHe-a1rfYgAsTBG1d8Uk8E-MzJRPaJ3Fvjec_s_bJThyTocCcIiKICTVHT3hEKRY3BHj-gQ1E0WHPLbwtjoEgSCB_QLoHyjjTuXpg63hoYdvH_pRUfJQFBfUm2WD7l__5rmAvWaZbe2sItd1Kc988AkoJgoqV2-wsEiRVGk8JKzNy-bPCF-kMMqzIbdaGk7HptTaLXmeDm9hmowpRpvcpnGhi6-7ajvGFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خداحافظ ای مظلوم جهان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/666851" target="_blank">📅 10:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666850">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b188edccc0.mp4?token=FeVUG66MqFslCm7UlulxZuptNrZbPQ96SP6Mr4qAuSHjBRcLaDhpTLZkzC76FxhBnRbPIaYxp4W3gl64QGJjjNTBU2g0CjR9eZARnEg-SvNtjIC7CT0ht7ZNGtLlGBTswBnNTmWQFmjDB_lVFEMWVqdgNrABlBLNl58-26oIDRIB5n0tjCwMlBfao9_ZPlwQxLGOmlwQU0v_kJWP01DPc6cMaT0d5HiD8TlbafNeRoRNWwft60_BTW7HNQsPmAB0nmPWr3BY9b1c2uCk69DtzzCZgmGkJEaoZw2aPArneEnDNZgA6CKoc1LuHYJBW3bnF_pcidCn84vKQN80Qb-K3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b188edccc0.mp4?token=FeVUG66MqFslCm7UlulxZuptNrZbPQ96SP6Mr4qAuSHjBRcLaDhpTLZkzC76FxhBnRbPIaYxp4W3gl64QGJjjNTBU2g0CjR9eZARnEg-SvNtjIC7CT0ht7ZNGtLlGBTswBnNTmWQFmjDB_lVFEMWVqdgNrABlBLNl58-26oIDRIB5n0tjCwMlBfao9_ZPlwQxLGOmlwQU0v_kJWP01DPc6cMaT0d5HiD8TlbafNeRoRNWwft60_BTW7HNQsPmAB0nmPWr3BY9b1c2uCk69DtzzCZgmGkJEaoZw2aPArneEnDNZgA6CKoc1LuHYJBW3bnF_pcidCn84vKQN80Qb-K3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازتاب اقامه نماز بر پیکر رهبر شهید در رسانه‌های عربی
🔹
شبکه العربی با پخش تصاویر زنده از تهران، از ادامه حضور گسترده مردم در مصلای امام خمینی(ره) برای شرکت در مراسم تشییع و اقامه نماز بر پیکر رهبر شهید خبر داد و حضور پیوسته مردم را برجسته کرد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/666850" target="_blank">📅 10:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666849">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSePMGwO54K2p4nEEm9-m9oih23UVxC8FDvVSXUpS_KEf-Rz74TPzTaZDS8jUtfYoojBj4zuVVI5F8-bKOVPOp0nI5yGof0bnFa4_jMzkFUDO7K19zqJXWsXP3C9DEOnS3bFpj8-QTDgDMo1yBo9Eegx8HcP6Hlh4oZY2d1vzWOvZjPpnDgeFJdHL6mtJUE_njP-8KLA27HYaPWTm_0GiYB84XuYuku-gRiyzoqnBXVG8IrSO33zA-hVU4X3svMyh0d9Z_h4YsLOmzZMPv2dzN7bRFMFOWBawTrMUI4Cw6QmfWJ-eCVqIdy5bf2DkvTbt9wAFeomP5a-l1LYvhMyNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوگواره بدرقه یار
▪️
از تمامی هنرمندان، عکاسان، اصحاب رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود تا با ارسال آثار و تولیدات رسانه‌ای خود با موضوع تشییع رهبر شهید انقلاب در داخل و خارج از کشور در سوگواره رسانه‌ای خبرفوری با عنوان «بدرقه یار» شرکت نمایند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگو تایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر، مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبر فوری ارسال کنند.
▪️
به برگزیدگان هر بخش، جوایز ارزنده‌ و یادبود
#بدرقه_یار
اهدا خواهد شد.
📅
مهلت ارسال آثار: تا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق آیدی
@Badraghe_yar
در تمام پیام‌رسان‌ها ارسال کنید
برای کسب اطلاعات بیشتر به کانال رسمی سوگواره در تمامی پیام رسان‌ها مراجعه کنید
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/666849" target="_blank">📅 10:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666848">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAETXP9OHhIqpMF5zQFLZ_PjDDJZ2_J7danbjKQX8MFbF3N5XVT5ocjklzSgyT3APaC4MjOLwbXwdMM6DM8RtWucMAyMOMPc-Q8_AqrSwT6H9x1QQTzKAAxsZoL8gQB0AaYf3dozb3kGRwTlINZGbcJUjFaw-t-HA-awxiuK756UJRiS7ihDQNSnHPiKvmvcbrBsWg7-kGH9q3XFnp0eV4I2WBvSecEU8KIhjqwYnkW1e0yR0xj5k3XPIsuT1JhByerqX39OBHYSGEmfGYGZbdk9dMmyC7ZDhOazzEXVp3AlrymbemBlFnhWckjpcYF1CyFxQZQhlsDKkSruRbasvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سیر صعودی شیرهای اطلس طی ۱۶ سال در رنکینگ فیفا/ از رده ۷۰ تا رتبه ششم!
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/666848" target="_blank">📅 10:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666847">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
میدل‌ایست‌ای: تهران از موضع یک پیروز سخن می‌گوید، نه صرفاً یک عزادار
میدل‌ایست‌ای:
🔹
تلاوت آیات منتخب قرآن در مراسم تشییع رهبر شهید ایران، متناسب با هر یک از هیئت‌های حاضر، این پیام را منتقل می‌کرد که تهران از موضع یک پیروز سخن می‌گوید، نه صرفاً یک عزادار.
🔹
ایران از این فرصت بهره گرفت تا به متحدانش اطمینان دهد که تهران تسلیم نشده است
🔹
همچنین ایران با چنین اقدامی به قدرت‌های بزرگ پیام داد که ساختار قدرتش همچنان پابرجاست؛ و به رقبای خود یادآوری کرد که اقدامات آنان را فراموش نخواهد کرد./ خبرفوری
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666847" target="_blank">📅 10:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666846">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1148e57d0a.mp4?token=FI4aGREornwmGOGwGXtS629yjlfJxazd8em7-p8Glgbjh6WSrArnKl7R0z16Tl7_MYOcQxM5jFbpejUGTZAmrKev816IfHCNYVf6WUjWue6pscQanS2c8gani2BlVaFXZAnaL8vRr1slnJVjwV28XPQOrvgxtmDoyleqM36xukhXn3OOYTfkF-oORZjN1jY4hwOTUKiH6efMCHlapZnyb8wfAFyup_ZSuq6oFgPA6LMEFpBhSjGqHbarlyvKACjMmgziwdn2vE_S-peSFOSM3MvyVeZhb8XMBj3vY0wDYFr-i6vGBfL1AM5_HGihgCuJeZsi3GeEs9kDdG4-9wkoEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1148e57d0a.mp4?token=FI4aGREornwmGOGwGXtS629yjlfJxazd8em7-p8Glgbjh6WSrArnKl7R0z16Tl7_MYOcQxM5jFbpejUGTZAmrKev816IfHCNYVf6WUjWue6pscQanS2c8gani2BlVaFXZAnaL8vRr1slnJVjwV28XPQOrvgxtmDoyleqM36xukhXn3OOYTfkF-oORZjN1jY4hwOTUKiH6efMCHlapZnyb8wfAFyup_ZSuq6oFgPA6LMEFpBhSjGqHbarlyvKACjMmgziwdn2vE_S-peSFOSM3MvyVeZhb8XMBj3vY0wDYFr-i6vGBfL1AM5_HGihgCuJeZsi3GeEs9kDdG4-9wkoEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزاداری مادربزرگ ۱۱۰ ساله در عزای رهبر شهید انقلاب در مصلای تهران
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666846" target="_blank">📅 10:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666845">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNN6vBG0rNC77pZ9NNSdJiw_LTt1ez_NoS5NrokJFyu6wWqYEv15Ze9k6Kn8YQFVmvMmZ6ExCK2nD2EP41A8AkWblIrMQr4m3173lKthYJopsKu5WQ70zyVGFGtXyKRnr6AR_UQ1IrdyTdtAcEWzWa41rxK6LGuYbSg5bgbLDv-g-DjpjhkpD6tdcznfNnCmaVtHy9zjax8O2Qruw_D2O8owfAcRSdb7rQzeA8WAg4Fav3QhsSYqTK4ofngg9ljOdIDInFTM7oLOTnAHDuJQrZnWwOcMNiZz849HbwgTjzjKbBU0psztKlZFzMMgcFS4VVwThlMpC94xn0sFFfeWLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری متفاوت از لورن استرله عکاس اتریشی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/666845" target="_blank">📅 10:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666844">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سخنگوی ارتش: هر خطای دشمن با پاسخ قاطع نیروهای مسلح ایران روبه‌رو خواهد شد.
🔹
مترو و اتوبوس در تهران تا ۱۹ تیر رایگان است.
🔹
روسیه: اروپا ایده سازنده‌ای برای حل بحران اوکراین ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/666844" target="_blank">📅 10:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666834">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kee9XCCrR6ca0NEZkqCMWDkCzUVgF19bHrJ8r_Q0FVroPvvmyZyBy0qEwmHYGbuwP0CC6-_hhyZMm2cvzoRNz8lQ_ib5KKG-GhHI-bYonoCy-U7YhEoGu1nMZKzP-6Y7sXQGYWoDyGgpP4vdCS-sHBCGpN6ZSgsNpiNpgjIJElCPLRibnpSInzBxbCwvVU_E9tmsw-61sPHEsq3osQ9pkCvVqbQEJznON4XYJyvhzrO34guBpM-lxr5pds369Cd6qgl3v88kEAdYrXvxJKuduMv8Gee-lVuNX94m2LC0-UYOvtqvZTWPyHU5CKOZ7lKXGpJ-LiMRaN1XgdX9idHotQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gbyAb-q5nANLpIegJDAI8lGTO_XIt7Miui-ngrVOzMB58TRA1fQeVoEiyVE-oUwF2TYNKPK-kSo3h-Fo-EXU2L5vJP-wOyoaoleQnuJVZJKp_cCfqheKtLBEQbvvESYTDnXHxHXCvY4jjAfELg2EBj6TMyqvOLfOLusB_zoIjUj1kc17LwQOVKJ3NZ7llBUDxGoxWgT7hA4Rv60KzmKXkbxUoh5lHkjO8H8ckkcljOmlgCh-QkkS-IPpLRGUQfkRmnNf_UJ_Yol9Mb8Zx-R4CvxtNNQEhjW6IS1NYVqa1Tw5m4wov5SpCxgApcD9-mbaIXJAPNSuvrauDEHaN1xPLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HTHcDYuGSsVxeBGQec95aoVfBn1F1QIoPKS66entG60QDvzeJvKHtgQBdH59nKXYqZdA0tqtO8ySSs4nOMDDMJji40JddgPWBiQyfsaEeBxGvM2gtt5N3CFnZXPXBgPPcvBbLKCOcYnU2g-DLbXH5rl8FjJABs4BwrUT9Og9eg8xXbUpAdM8hJehTXsJUL243Ty2kjmXrtq_AAmbhXuyN1htQtVVmSxDj4xQgkBA49_0z6txH6CXKFeMR6XDWPpMsQ3-utYa9jtiP0cSJQYnYt_WuPtis5E0E2MplHB6X-L-VHn4AkgyJm9lLpTY2WAY2cMdMMKFHI3IDYLg3ROnTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qhhJjkPdsl9l6FQ1BSD9ZfCb6pIAqMkvGPfWKuYunZTZcdRhntRxn_DaxdGqCZ5PEQlO4PNwyGcdHtoHzfveNoqmAS8lDGASreFa_W5efIZFFwwmbP1yeznryY2YK0K19r9X-toFRP13I_MtZ-FLyz0tHBqi57_zK1mbNXy9j94ugJByrNtT9SoZPCZQhcy-szpnnCiQVEAlTBDmHK9DMNVrl6ZZqpP0EmOyHQC3oTIMYSeDmIAfoB9Dn-vE-mKOu1-qa68Km7F0jellFA8dUDMjgMuNek-atYGPXAz4a-Gx2HqjQ7xLrKe4WUVwPXaQtp0u5YbwLA5sC0lcPhXF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5pvB6t-5uqKiK5-x32O3cCUKrXZ1msvkaPpAGeVKn9-k7rg8VdvnMV-5e7HujjAkcsyOA6ExKTB5StVpZIMVwowr6Qb1YUmSURFV0vnQjLy4Y0j5CtVdqP_CLNQO11QJCBmro-O1XCGIJBcvEkhxmAn8gu8wut80cZs9STKkmtxRTQmAOPE5mzJl4FACkCJaDpFPhgD98gFok_xc4ZHUjFTfWrH5qV25oosUbb2Ry77Xh_HiNxJGpGmNBil7yvS3_5DzLtyJbDrnwxgRGYxGRSXUtgawFO1ImKACXTE3Nf9qfDNa1MWKPuv-2fZ-vqv20Td1vTl9XOrt705eKApNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E2fa8i9oKKDuFB4aSEsH9oafAREzMHeegPQeKE_Uu9tiJyN-FoMxOIqs26-j6TBOV5VvUu7aALGsscNG3NPPzEfZux9D0Y7ps80kVVexmZvFoZJ2I7vCQOCyO01vhANlvMSsX8y5RMrgdfzgR59aW1uegw5FY3CvD5sio0_4UfF-yQkJa46ZVKdbceTGTz5toMLpJPaKaOoz-n9ThjiGymzDI6T74Bn2xVDoTXBRHQOSNAWBuabnLDp0bc3BIuW0TlotLTopHz9xJ-fPodZ_c-tZ10kudHc_aIElVuUdL97ScsBPMosgZ4Qr398a078FOsarI-eiIrlGvdJanWw4TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JhjVMhnVTAE1CjPxf00uvgiqFIaiUD6aBAB6jW4htRvgEkEbsDggUwJA377K-aVmw1FZ5L7kAR96qTSoKDggEnU90v5FmAEeLSqv0jxe1jlMIQ28ewjrn1nt6eoAJfEXJ41-dilAlwMnWQcZe79U1tQvK6SR1eRGIbz-QDfjpakUSxuBtlBsyrZE3WQaPNctHCI_R631zxSk-oDYYa0kwiu122NzHN98erVt6sHvu6hZBjJxcZZYHh2OHizmSotD__PKVWzAJbVXLyIyg1eG9i-RTrS42KyRNHvI8_nh3-Pxm5VIDxoQXY3uALk92BYWjDzVSJ9V83ZSVxOQ76CpEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fBLCxu4LgBtfTVlHEgV_eICxr7rcTXl8n62luhiXC6_wUjB_12ZYeGA1fCbLAGG9WpRosSyQ9apTETA95treDBaBcO6YqIzYNVBJFln0gIb6ixEsMBGsxgDPpDtv3l-kIrMwOnFbWunvbE3KNNOiXtgpY62b04nD0Jf9ZJmfFAt9hBRAvwP2fZrjnQ_t8RDp4dTxtKo6osX6SFWY4aGtXJMXrG3BoRW-UtRxcLuRQqZOhsztoF9HxJXPUIBNuX9eUm-P03Mwtf184dmRguSClL30dYruK-fLQrTXzYDcV-OIfzjDdE1uU9K5GJelM6cluKo8OBCYrxWFJKj--G9FYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/adOGqM1PzYftls2HMN5a9lXGvaLJn3GyUixgLM86tIB9_7nh9Fe08FLWS5jRWats3zvMTuLNKy7WcrZMw7NxLJVnRNPeeFaonh4gZHL7_i0e-1AlGH5ZqUKmyCEWeGwszgH9OdR2mSpUtqinj8Hm_Kf1FdOlFMbw5oYbkA1bggsDYWO9Em16_jJ1VHk2aRuE83kJLjkJRyTbfsX6A3fq_CHpGyWOv1sTcyF0aoYRTxPy7mVahQ2r8m9kDUZwf7HV6_h4Ni-gJRxCx_N7Jaw_01U9yAD4bmWdWg-H9rTfLE9Ug920zD-lHJXV3pgjo9TVytbggvOlpBIPYcKblxr-Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WqyNQERpLaIrUy-QmzQ-I2aw61VpUVpWPdr2Upn_hwPeBBmu_TsMkhgSEskFPUi03GU_no_ZTUy4GBPyqX3DpfdQj85jSutnB5AGtvPBd3huCD7JQNcwxLZJCujcPP6dnrm2WGP140ChXq3n7-lLpLUj6eJ22VPYl5EEbn3ukj7hvlSbo2guEpv5UwRdYI9LbY7dginiEsfNgnatI8Ro1gDiFvXK_bMc_oxxlz3EEnKKL4CGCp7i2U7OG3TAdkVYotv_uyYB0rfMKlVcWz0ICS5YI6qXH-Dxsp4HQLz7UlXT86eoESr_-BIs680pGWnioUz8lob7bube42nnWTKeNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سر از دست دادیم
سرور از دست دادیم
تو علی بودی پس
پدر از دست دادیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666834" target="_blank">📅 10:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666833">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
مصباحی‌مقدم: آیت‌الله سیدمجتبی‌ خامنه‌ای معتمد رهبری در امر نیروهای‌ مسلح و منطقه بودند
عضو مجمع تشخیص مصلحت نظام:
🔹
آیت‌الله سید مجتبی خامنه‌ای معتمد حضرت آقا در مسائل مربوط به نیروهای مسلح بودند و بخشی از ارتباط حضرت آقا با نیروهای مسلح از طریق آقا مجتبی بود. ایشان همچنین معتمد رهبری در ارتباط با مسائل منطقه بودند و رابطه حاج قاسم با حضرت آقا از طریق ایشان بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/666833" target="_blank">📅 10:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666832">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ffc7fe130.mp4?token=Y_RCfXIR9Nr9zTSb4_fszRkqYciYy9ZOxcroemEekg7vLec7H4UQcdehSlwYfzWdkmkkPE-XGcGfsfekjF_fnm96nosX_l8yg1-ssIxYEMLfo8YuRhb5yMWYGVwkjfhi9c9Y_ZMo9WkdyBsK829r-PgVjCqlM8_cpjQFkVb5_lQ61RUsU47XNLULqTq_Rp106GVllhitC7QbK7nPYV-wNUtnGuAIgAd4NnSLaa8oJqXDzpqxqae-kpOTArNztwX0Dl9NeKt2vPLVqalryxnCyMEHO5ff9EVuqhaB7W8Gj-oLcl-l60gFSxhwjgdlSC3rC1tEDzhj6zSiaIbtUbpBMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ffc7fe130.mp4?token=Y_RCfXIR9Nr9zTSb4_fszRkqYciYy9ZOxcroemEekg7vLec7H4UQcdehSlwYfzWdkmkkPE-XGcGfsfekjF_fnm96nosX_l8yg1-ssIxYEMLfo8YuRhb5yMWYGVwkjfhi9c9Y_ZMo9WkdyBsK829r-PgVjCqlM8_cpjQFkVb5_lQ61RUsU47XNLULqTq_Rp106GVllhitC7QbK7nPYV-wNUtnGuAIgAd4NnSLaa8oJqXDzpqxqae-kpOTArNztwX0Dl9NeKt2vPLVqalryxnCyMEHO5ff9EVuqhaB7W8Gj-oLcl-l60gFSxhwjgdlSC3rC1tEDzhj6zSiaIbtUbpBMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید هادی خامنه‌ای: آقا مجتبی در طول مدت مسئولیت پدر، تمام مراحل را دیده و تجربه کرده است
سید هادی خامنه‌ای برادر رهبر شهید در مورد آیت‌الله سید مجتبی خامنه‌ای رهبر انقلاب :
🔹
ایشان تربیت‌شده پدرش است و تحصیلات قابل قبولی دارد. در طول مدت مسئولیت پدر، تمام مراحل را دیده و تجربه کرده و همین سرمایه بسیار خوبی است./ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/666832" target="_blank">📅 10:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666831">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLTbS_lURaetwsdHbc3tQOY3XrZ-iLYH0u6yxGiYFpJcAcTNZIJk4zqxqn694HAAdCw3tPzW2d7lz7aqpOOKRkYiXTLZTKHkLFNxRG-qWpVpFM4rlS5z23_oJXHtrcrChtUbFREH6GHpdHPFlKt01xHd-gVhTwlMB9YyQNEHm_R0oS5Jg727d9a0RfPg9sBdPaSBQzDsNs8xhz1fz0UtRriXbqQBhso-aa9LaR7NvfdWxhSUMWd-Qghf7z-pxgVHhj0lG_bnSozwN6wB1ghjbN4YtvFi2h9PZ_g9qemmL3txE4dqXLupDRoi0dPXow7JRppKoUmkAyQuCpj_f6P7uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یاد شهدای مظلوم مدرسه میناب در حاشیه مراسم وداع با رهبر شهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666831" target="_blank">📅 10:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666830">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6625ee5382.mp4?token=GlvqiEv_m7DmoORPxUcODYpqqixxsUgy4Qb4xmDNPqJLrt45BSZ1XfhA8zIBOqfoOw7yJC1CPRLPSypjAsqRpVjFsa0GrJi8BtnXmhdlipkx3KkCXd7B-No-hB9PU30oPBu25BnhexQIz01yLmMNLvjOTBWMtvqQWeg12R4NDM3PI6f01SdUNL1ZWN-Go6aiTSLSEgb_5uqeQPiCfxmHopTtR66hucxwra5JyrNSPOEXfmi2VASaWR7Wi5bhu4GrNXQVkPtRGRbExT1ZOGTHtkDrQ-QuH0Y7NrkyicqV3jJEjiV2LzZ0xXpu-uZ8ZaYcayR96ThbWYNPSN9SXh9rbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6625ee5382.mp4?token=GlvqiEv_m7DmoORPxUcODYpqqixxsUgy4Qb4xmDNPqJLrt45BSZ1XfhA8zIBOqfoOw7yJC1CPRLPSypjAsqRpVjFsa0GrJi8BtnXmhdlipkx3KkCXd7B-No-hB9PU30oPBu25BnhexQIz01yLmMNLvjOTBWMtvqQWeg12R4NDM3PI6f01SdUNL1ZWN-Go6aiTSLSEgb_5uqeQPiCfxmHopTtR66hucxwra5JyrNSPOEXfmi2VASaWR7Wi5bhu4GrNXQVkPtRGRbExT1ZOGTHtkDrQ-QuH0Y7NrkyicqV3jJEjiV2LzZ0xXpu-uZ8ZaYcayR96ThbWYNPSN9SXh9rbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت یک فعال فضای مجازی: از شیراز اومده بودن، گفتم چه حالی داری عامو، غیظ کرد بهم که رهبرمون واسمون شهید شده ها
دست خالی داشتن دمام می‌زدند، با چوب پرچم و جعبه مخابرات
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666830" target="_blank">📅 10:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666829">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e33707719.mp4?token=G8qo8pzos83eOOlaCHcJI8EnQoz_ZdzLUKsk0zyaUNhtE59uMg3rt-U589wR1eBb0-dq6xxZQGgL8udAaHqKH1ufGY3ZXndVXeybQkEuwZjAiukuF0n-jjtfDA3JskY6lVrqCOu2FnBHBtL7kfkpdxE5dpHPjSJaN3TvKhid0L19VJpTPyAUlYCwpt9I7pzKhi1V-h-i-_AJBCJO5X4pU8Ze4HodyN6l-SbbkB9y1flpczVm5sVqsdQe9h_DujGs85X06TkTgo28gdq4_zHnUxS4TbtO-xQOUnhOJckqjelWoR3T0wzi8lmifbQ8ddkJtjbEnhuc8wv4lant_oZkjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e33707719.mp4?token=G8qo8pzos83eOOlaCHcJI8EnQoz_ZdzLUKsk0zyaUNhtE59uMg3rt-U589wR1eBb0-dq6xxZQGgL8udAaHqKH1ufGY3ZXndVXeybQkEuwZjAiukuF0n-jjtfDA3JskY6lVrqCOu2FnBHBtL7kfkpdxE5dpHPjSJaN3TvKhid0L19VJpTPyAUlYCwpt9I7pzKhi1V-h-i-_AJBCJO5X4pU8Ze4HodyN6l-SbbkB9y1flpczVm5sVqsdQe9h_DujGs85X06TkTgo28gdq4_zHnUxS4TbtO-xQOUnhOJckqjelWoR3T0wzi8lmifbQ8ddkJtjbEnhuc8wv4lant_oZkjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اللَّهُمَّ إِنَّا لَا نَعْلَمُ مِنْهُ إِلَّا خَیْرا
خدایا! ما جز خوبی از او ندیدیم..
.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666829" target="_blank">📅 10:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666828">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/akhbarefori/666828" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تو می‌روی دامن‌کشان، جان از جهانم می‌رود...
من خود به چشمِ خویشتن، دیدم که جانم می‌رود...
پشتِ سر تشییعِ تو، روح و روانم می‌رود...
🥀
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666828" target="_blank">📅 10:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666827">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec20bf810f.mp4?token=Fz1Z0zu6oRtxkjeghe5BpS3dY_XQwySL-U0NombObkfZaVoUSq_z5rfznM2UWbJ4s47B7yJ_3XXJdJc7DqZzZIuCIbEDi8MtrRQLWI8bd6-abDvzkxDNOTnYjnzmk2ExKtH5oEjz_DqahIVKtjD1WvGY1xQZ3SQsixyAPyUVsw99B1YZ0stKzBm5OWJVXA2oqm1mryP77fGgWeGjh_ZMvYVgNdZpSt4N4EVAk1bNDmvsjeeoBzuwvTpRUO69NxdgPnySrrX9QxIJEDvTmd-U-ayqTa68PtO-AOdLgZ6axLy8MED3NSzr7txNYcRPRv4UWfIhAM7husZz2H8WQqwzIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec20bf810f.mp4?token=Fz1Z0zu6oRtxkjeghe5BpS3dY_XQwySL-U0NombObkfZaVoUSq_z5rfznM2UWbJ4s47B7yJ_3XXJdJc7DqZzZIuCIbEDi8MtrRQLWI8bd6-abDvzkxDNOTnYjnzmk2ExKtH5oEjz_DqahIVKtjD1WvGY1xQZ3SQsixyAPyUVsw99B1YZ0stKzBm5OWJVXA2oqm1mryP77fGgWeGjh_ZMvYVgNdZpSt4N4EVAk1bNDmvsjeeoBzuwvTpRUO69NxdgPnySrrX9QxIJEDvTmd-U-ayqTa68PtO-AOdLgZ6axLy8MED3NSzr7txNYcRPRv4UWfIhAM7husZz2H8WQqwzIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتوبان شهید سلیمانی همچنان مملو از جمعیت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/666827" target="_blank">📅 10:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666826">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
همونی که براش نمردیم، آخر سر فدای ما شد
🔹
همخوانی محمدحسین پویانفر و حسین طاهری در مراسم وداع با رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/666826" target="_blank">📅 10:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666824">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
واکنش مقام اسرائیلی به تشییع پیکر رهبر شهید: ترامپ نمی‌داند با چه کسی روبروست
یکی از مقامات پیشین شاباک رژیم صهیونیستی:
🔹
مراسم بزرگ تشییع رهبر (شهید) ایران، قدرت این کشور را نشان می‌دهد. رئیس جمهور آمریکا واقعا نمی‌فهمد با چه کسی روبرو است و علیرغم تجربه اخیرش در خاورمیانه، در مسیر اشتباهی حرکت می‌کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/666824" target="_blank">📅 09:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666823">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjus8hvUqYEUaMslfKEv-ZoGi8lkeCixlmpe2on5TwE9QsckjdK3q3dttcc63JLAwvHkHHtg8NvmqZVUnwit2bF7_mthSsS9KVI3bQX2Rvs-Q2uooBwEAzRgwcsKXnWApNML-5_jtpYrXPJ8lNvy_Dj9R-LHKyf_0VKzaRzW57vqC3kcd05oXd5f7NA1uPBb5EGMxoiHWPCVeDkCOhwazFjog4ZClp2zsl1WQqIJZjVNdDsxsEYaw-WFK5Y5WQN__N9b4-ZUPoirnx6trO9QNXhPEb9qMew0fsnmvTAeFhg2kD4wsFF8BREAlnAA5UpQjHaJl9gK0z0YIcOcB12ACA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اقامه نماز بر پیکر رهبر شهید انقلاب روی آنتن شبکه‌های خبری پاکستان به صورت زنده پخش شد
همه شبکه‌های تلویزیونی پاکستان با پخش زنده مراسم تاریخی اقامه نماز بر پیکر قائد شهید، گزارش دادند که میلیون‌ها ایرانی در بدرقه رهبر خود حضور دارند و همه آنان روحیه‌ای قوی برای گرفتن انتقام خون شهدای جنگ تحمیلی آمریکایی-صهیونیستی دارند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666823" target="_blank">📅 09:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666822">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oniv3SpQdc0chsTZ-bPqF1Ilh3zO0tAxDWkzxP9mdEtQ7x9QB5oxbWKBnE0P5S5jFOWPERUxdzmfd1hV6Be05kk1ifCYf0QmHmPBeX9Ws2El_GRMWV3i9s2Caj7_gGlrF5FkFpxiWJAZKpTyCncJnqKRE0HiostaomiAEg55O8i6f1w1IpQ-CKrHiBNJ3t9MfozQbkpDC01ykL9NOpT_5CTF27sodE6nIMJel_WAVu3qf7yOdoZCkdJ0QpqdyTnjSQKRc1ipjV4v9ew3eOjjDP2kizcKY4hUen3Gq9J5RmLtAcQGLmBI_nOpSql1cSgUELwtkj4B25PM3zP_QG3eLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/akhbarefori/666822" target="_blank">📅 09:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666820">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cuyj078mdqklgD7NVmPXo3DyIQlYOOhnr4wlcY1lUkHl-olr594mObV0KH7ZxNkHVfNfIUpzHLGyGAh1FrYC4ppN_2kBcFdABETZhWR71S5-YVBKiVEPuQPZ8VfZi0T2_6pZwE2uQPrwGHtgdLt_rD-lh6gl4YmzjmNonJYrwwWMVuMwlhrw7swSnu_uVF8l7JMcxTwM9yOWf7prv9pHPISk1KtFTGMAibPUQwv89bRCs8ZOj-wgHDtchYBUX6GIQ7c44tV5H2luiSPnN8JAdvExrlNKDa_lLQdMWIXim6ymceVzMfwPjCV9Tj5yP4iJj26ehjXtXVfTUMEXrNTwlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌ان: دومین روز تشییع رهبر شهید با حضور گسترده مردم
سی‌ان‌ان:
🔹
همزمان با طلوع آفتاب در تهران، دومین روز مراسم عمومی تشییع رهبر شهید جمهوری اسلامی ایران با حضور هزاران نفر از عزاداران در مصلای امام خمینی(ره) آغاز شد.
🔹
آیین اقامه نماز از نخستین ساعات بامداد به وقت محلی در مصلای امام خمینی(ره) آغاز شد؛ مکانی که پیکر رهبر شهید از روز شنبه برای وداع عمومی در آن قرار گرفته است.
🔹
تصاویر منتشرشده از محل مراسم نشان می‌دهد که از نخستین ساعات صبح، هزاران نفر در اطراف مصلی گرد آمده بودند تا آخرین ادای احترام خود را به پیکر رهبر شهید انجام دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/666820" target="_blank">📅 09:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666819">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd70fd41e2.mp4?token=gaOiyeKbm6OxtKcLa1oY_eg-oTZiVs7AAtl1qH8ITVZkQm562bS5lVxLr6H2zMiJcd792pk27zQcjcM_RCXJ3Q9watwrb8VDZ9ldsfKAAZJIPIMujMwRbtzT496N0ne-xkPvsyUEeCuLzzvjLZARxMh6XSGqJDLacj5i5qUdnB-8jjsAfwg_SSG4c88gaOy_D1h6BbTutUy0-5_6DdVHJv2wt3LQzDNhX8LRpQar-aaiVpxM9GBRxaeF2kej80s2zGGWqcUC9tp4NiIE8tQUlZhPmDbq_3uwJdvzpzOM9cH3pDansGluchFJ6ZcFF7qxj_FNJpJrmId7UeJmFbFNUVRuHPKTG0QkvTU-fmLfSygZN7XqOrRzNs28pe3OGjCaBWJ0sl9-mZNfNy4kUZxuZ3GPP8R9mgAGa5-4gg4Xvz6jdFkuJfuPnPs9-UB8hqU6hZ5q0vwRXvQPlIHZX2TyR_skQW8Tc8dqx6N_1Lw8MgVoHqaO3cPrxKtKubib6ZOpemCdhWCuZSnhxYxD75N9Oxi-eFDC-pKP8rk6D0izA8S_E4uCP73uQxGkJG5ecYREJSmd4n8qaB5nK6k5_ppiXHdpgSfUOUa7La9KAXJb90FXAeV2WbWzew6QryvmeTk7RrgdZCMDiDtGQyKafVz40NrIIf4SPUXBAxSyC9wdrpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd70fd41e2.mp4?token=gaOiyeKbm6OxtKcLa1oY_eg-oTZiVs7AAtl1qH8ITVZkQm562bS5lVxLr6H2zMiJcd792pk27zQcjcM_RCXJ3Q9watwrb8VDZ9ldsfKAAZJIPIMujMwRbtzT496N0ne-xkPvsyUEeCuLzzvjLZARxMh6XSGqJDLacj5i5qUdnB-8jjsAfwg_SSG4c88gaOy_D1h6BbTutUy0-5_6DdVHJv2wt3LQzDNhX8LRpQar-aaiVpxM9GBRxaeF2kej80s2zGGWqcUC9tp4NiIE8tQUlZhPmDbq_3uwJdvzpzOM9cH3pDansGluchFJ6ZcFF7qxj_FNJpJrmId7UeJmFbFNUVRuHPKTG0QkvTU-fmLfSygZN7XqOrRzNs28pe3OGjCaBWJ0sl9-mZNfNy4kUZxuZ3GPP8R9mgAGa5-4gg4Xvz6jdFkuJfuPnPs9-UB8hqU6hZ5q0vwRXvQPlIHZX2TyR_skQW8Tc8dqx6N_1Lw8MgVoHqaO3cPrxKtKubib6ZOpemCdhWCuZSnhxYxD75N9Oxi-eFDC-pKP8rk6D0izA8S_E4uCP73uQxGkJG5ecYREJSmd4n8qaB5nK6k5_ppiXHdpgSfUOUa7La9KAXJb90FXAeV2WbWzew6QryvmeTk7RrgdZCMDiDtGQyKafVz40NrIIf4SPUXBAxSyC9wdrpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش رسانه عراقی از حضور میلیون‌ها ایرانی در مراسم وداع و تشییع رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/666819" target="_blank">📅 09:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666817">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
پارکینگ‌های اطراف مصلی اشباع شد؛ در پارکینگ‌های ورودی شرق و غرب تهران ظرفیت موجود است
رییس پلیس راهور تهران:
🔹
تمام پارکینگ‌های نزدیک به مصلی پر شده‌اند و علاوه بر آن پارک خودروها در حاشیه بزرگراه‌ها نیز صورت گرفته است.
🔹
همچنین در ورودی‌های جنوبی شهر نیز مخصوصا در اطراف متروی شاهد و مرقد امام تمام پارکینگ‌ها اشباع شده‌اند، اما در مبادی غربی و شرقی هنوز ظرفیت موجود است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666817" target="_blank">📅 09:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666816">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ترافیک در ورودی‌های پایتخت
🔹
ترافیک در محورهای چالوس و هراز در هر دو مسیر رفت و برگشت سنگین است.
🔹
محور قدیم بومهن–تهران و آزادراه قم–تهران در ورودی‌های پایتخت با ترافیک سنگین مواجه هستند.
🔹
تمامی محورهای شمالی کشور فاقد هرگونه مداخلات جوی هستند و تردد در آن‌ها بدون مشکل جوی در جریان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/666816" target="_blank">📅 09:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666815">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6acf0490b7.mp4?token=arvF0bSS1n2KCWNtmrf29LBFZWNVGyQzQzh97w6OqXqc9UmW7gGgLz6XPHRTR2SXYCBUu6V6KaWchvEDTDLd4YTPpBfjKrXM-qARRnKWzcS4JOJG3Rs782T4FNuarvuuERW6uSJ31CscvYGOL3sl5jsfpAy7_zUiGjLNIq9x1N7YuS-PbSzA5NxEKkODcIQ-S3Ilh_OxijRCk50V4CrXA5nJiT_noMzmcV3FKgO-5afRRGI9dSaAG-0_MDrLcRP3-_teXlsDy2bdQImD2xlC-mFeGY2u-3TX2wGASDnJ77ZxM95HkURe1t0Awd5QXfqnyLbW_Dijd9nSk7TWT_9J-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6acf0490b7.mp4?token=arvF0bSS1n2KCWNtmrf29LBFZWNVGyQzQzh97w6OqXqc9UmW7gGgLz6XPHRTR2SXYCBUu6V6KaWchvEDTDLd4YTPpBfjKrXM-qARRnKWzcS4JOJG3Rs782T4FNuarvuuERW6uSJ31CscvYGOL3sl5jsfpAy7_zUiGjLNIq9x1N7YuS-PbSzA5NxEKkODcIQ-S3Ilh_OxijRCk50V4CrXA5nJiT_noMzmcV3FKgO-5afRRGI9dSaAG-0_MDrLcRP3-_teXlsDy2bdQImD2xlC-mFeGY2u-3TX2wGASDnJ77ZxM95HkURe1t0Awd5QXfqnyLbW_Dijd9nSk7TWT_9J-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سر از دست دادیم، سرور از دست دادیم
🔹
نوحه خوانی مداحان در مصلی امام خمینی(ره)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666815" target="_blank">📅 09:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666814">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
تعطیلی مراکز شماره‌گذاری و تعویض پلاک خودرو در یکشنبه ۱۴ تیر/ انتقال نوبت‌ها به چهارشنبه
رئیس شماره‌گذاری پلیس راهور فراجا:
🔹
نوبت‌های اینترنتی ثبت‌شده برای این امروز، بدون نیاز به ثبت‌نام مجدد یا پرداخت هزینه، به‌صورت خودکار به روز چهارشنبه (۱۶ تیرماه) منتقل شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666814" target="_blank">📅 09:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666813">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce3be48ad.mp4?token=gR3MM5URpG6aZuixLy5VdeBfx4K9Z232ueQQHZZI_BlWED8Pnzt5HAURIsPxsHnbaeqxNo2yzj9k-TpbKsGNyqE7Qv0APm_Dm3pNjli2xhgKkYufb3o_Pu4IBkEKXdHH_lvLu_1GKfX3HwCyjcG8O-cNgCw8SljCGioZSDf8xSUeGFNCXIqgmL0ZmRtPwrciguvG_-uAusCStNQ1mqwR-lIkcNgsK9i7QL3lVzBqbJnbNiNb5X6uSGts-pKEA3_Vu84TkvE4WJImuyBU0HYVYOKgU9BiLve68qVB3DZdBGB1wfdajkZdbbw0VmDzhkZe8wl3vHHCtDbDKmAzaZ9yOUuHW4XOCmKKamdrCeiJt7_1Oe-k6K5XVqlbx5q689HdMbamY0mqVRLHMfR3dAMea7vA52JzJy6W4Sqw9Sj7URGbumnaxucF3RMjJNwRsElO9dPLHH0hGmk-uiM8FfsgT3wea807I_VvbK0oOcBRMOj9WsPbPvCAunFO4Kr0kK6wP7udT4WZ2eUzspy-1A4ovLmtHwVzZABP-xgRpDCMC_KWpGBQjmed-pH0Lb0pio1zn1cv4RNn0rmYZT3-brbnVBIMbqExFeXCDHNL6ddW6axyevJHHE2Mri1nJCrX_xE63PwKPModRZXAVtXA7XCgIRPfXz496KnRLMHngMUPTvU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce3be48ad.mp4?token=gR3MM5URpG6aZuixLy5VdeBfx4K9Z232ueQQHZZI_BlWED8Pnzt5HAURIsPxsHnbaeqxNo2yzj9k-TpbKsGNyqE7Qv0APm_Dm3pNjli2xhgKkYufb3o_Pu4IBkEKXdHH_lvLu_1GKfX3HwCyjcG8O-cNgCw8SljCGioZSDf8xSUeGFNCXIqgmL0ZmRtPwrciguvG_-uAusCStNQ1mqwR-lIkcNgsK9i7QL3lVzBqbJnbNiNb5X6uSGts-pKEA3_Vu84TkvE4WJImuyBU0HYVYOKgU9BiLve68qVB3DZdBGB1wfdajkZdbbw0VmDzhkZe8wl3vHHCtDbDKmAzaZ9yOUuHW4XOCmKKamdrCeiJt7_1Oe-k6K5XVqlbx5q689HdMbamY0mqVRLHMfR3dAMea7vA52JzJy6W4Sqw9Sj7URGbumnaxucF3RMjJNwRsElO9dPLHH0hGmk-uiM8FfsgT3wea807I_VvbK0oOcBRMOj9WsPbPvCAunFO4Kr0kK6wP7udT4WZ2eUzspy-1A4ovLmtHwVzZABP-xgRpDCMC_KWpGBQjmed-pH0Lb0pio1zn1cv4RNn0rmYZT3-brbnVBIMbqExFeXCDHNL6ddW6axyevJHHE2Mri1nJCrX_xE63PwKPModRZXAVtXA7XCgIRPfXz496KnRLMHngMUPTvU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازتاب اقامه نماز بر پیکر مطهر شهدا در شبکه‌ المنار
/ تسنیم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666813" target="_blank">📅 09:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666812">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
بیش از ۷ میلیون سفر با مترو تا صبح امروز برای حضور در مراسم وداع با امام شهید
🔹
همزمان با برگزاری مراسم وداع با رهبر شهید انقلاب از ساعت ۵:۳۰ دیروز تا ساعت ۷ صبح امروز ۷ میلیون و ۱۴۱ هزار و ۲۱۲ سفر در شبکه مترو ثبت شده است. مراسم وداع با امام شهید در مصلی امام خمینی (ره) تا ساعت ۲۰ امشب دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666812" target="_blank">📅 09:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666805">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JzKHpieF_O39BJNidqQdhfdaXdyUXxQ2hObybuGC1_Y4W7pDGeKvQtiP18aqygmJM6VAEYoX8FiSqtF686q_z9Sy3jrQwzfGETrAo2yoEfxWEZkpVQ8ZLMerCATZ38ZtsxEXQpY7p3G65dETBLRuJy1gdLwjV-pcZTR0ILb5G7eNS17N5QHNNjkXCsBQ2tcZydWkmlNcPiMz5WqlC6Dh2I7FyWjILA00G30EkEpiDy9QWsljXDyZWTyPddHHBztCcq0arQRncMnW8lumDt0GBSX35DoksN1m8Er7GwWy3wrJdzd_L0hnzqmgFkFGwmsNQug3e7IN7dBFBi7q19-XbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ltPIrzLPpi3cGxFNqkn_H1N-DtEEgeR8wInCSR1XIP9Od5lIaKTYP-C2UfS7zkG1L1XcXNeT0hMYSTuvmWPhaLDCz_gK7macsLUPFkvzta0PDc5BBRTcqFvKkLooKmV-gZc01FQbok0YwgQKDi5Oe--BYWPCzH8J8JEOjZ92VJp1e_SPceLvyUzjbWFokDq5Oi7TS9BP-zGacrQMI-9qTAPWYryJQj89rMTwZ1a1ArffuAYpi3CWNPxGzue1phOxLNbziNpDYYfSeOpLqgyE-g3JlwkM5H9CYS53d1YpljV3YojIlYKcB_fpGGfUW5kGBBJMCH5K0V6k59eP1Q0ugw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jeMGnfQCxrr036Umogz3cUK0ROMDkoXcNb16LX7ws9HlkfrROQ-Q3wLr9Kq5q9u72KnAhWpglHWbElpR849Tfy0YagAxIV43Y8B2nbYM4md_1TRNLT2KNMmfj9UPozgypJ2Co0Iwz2xMACTVSxCi9EkpToLqUBF2pmLVDc0hmxu0cvG9wNanB_HmH3zQvSCF5v75WCI7Qiq2oEsuHtu6jvV7CcCGzaqLrJiWr5STivHmr0svlLRmxKQmXhi982KcFiLpaIXOs_91eCj4tF-VT9XRiBGr4AFF8DFPUJ1HlwaZDMyjc9liVwZBaN6ck3ti4gRsPY_Mn_xEu677lnBSOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RWiRJsVpEU_W4pJW3c2QQSRG2YxJel8M-_kh6WbkZIa2GKVnO4s9L93RVLpJrRzLhVceQV15QvEshmxb8nHaArGP2_7o7vuxChul_BFCIW6aT4TCuYhEsEFEfu9WDJ5VSNwjkOvAMhhx4NpBkqORGLo3j_ik0g8mJ-Pl2e9OWIQgPZjHaha2_FyZCG1FWpWEGbAqrICDsPNyobO29s1r5qWjKRpXEO6dDwO-Fmse-nc_Um6mqRlVWLrr8SfFtGFukgP04Ta9AXHQFzYSBxUX6a2Oplmk3JZyoQTWWNnWMxYV2nUnSiWKP3cb_NsyipoJSLF-BnG-W0-KR_7QMND_6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rv0tyiy5jsW5YzSq5MN6UwgCJI0qHFfHrRc7BW7ec4Lw1RImybS7CnKqwjJ2tvyNzVxbi0LYsaWoXOWJf7GPuE9zMW2ZX3TgHkXZX82qTpW1D0OPPHQODcKtStvd43sUcxRma9ihxsn_oh1gHEllif5xr1QzTWd_vV4Sj8YTNJ5Md45IKleBQDs7vH04B9ScNvfe8eyjQ1HcxaHSXE--Sx1iSvpxSDAgoc8hxfk58ISACHCnM4W0PDzXvbqNgspYVERd84WtRJiRGEH-VNiodL7fNBiioCJBRii0e4058KiIb2VHTme5L2vsBlDBloKoUn4eAS2Vh6qDRgZ-zmHY7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gVyKwDtEi4yrB08Qhtmz2tifaH_z5Vn_zkJj_75wcut801zdAHGv4alWGKYxWfX69ibywY7x74dM3VNh4lUG5UbURhBkKzKVotKtp9q3-Dxi3cATu0M2uPJrF9XynYbxRRq_NetZkdgGCo2qk863HTnPxkB0IcXxxo4uIZC_86Y_jQLUtFfspfafFwvrKWTuX0jmDEv-RtXMXPX5WL0hFkl4ezny0Aa-xDT1agmk4NemQ5iUFd-7W7vKqg0prTZFxfGyhHSO0SWb7kRoJP76UL-agJKmbgAZD6z1w0yrO8U_IWwmR8YDli2a4soXlHIdoRDCXHQJNgSlEIEXcmD4vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d36ae94c32.mp4?token=iBgrTQ_V2VW3znrMSbUXFojCYemy0x6wm8UTpylJ3hnN85rgyuIxdRzUFaBwzm-31ukXJxeymIkykW2Hnd-tF4cJui36mEk5dp08S7aqoh527SB2Kg2JMuidf20hosfljDLdXTMM5WlJE5afqtrUbBe_7EIFuheqxq7H9Kt1WtaouBKjaPEk5k_-woQAvzYi8LTLn4B7Nevm9UlyKWt-od0QFT77l35Hdhr983-WZ2kUqSli5l7xnWyt1ddr_EIo6p4fc7wX6XCg2KO7wAAJSj8EHUR7hsyDsEIwVdPF1bFKrxuPbwXYj-aXiY6h46Cwf3eaLyP3DAM1sWG_dxr1gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d36ae94c32.mp4?token=iBgrTQ_V2VW3znrMSbUXFojCYemy0x6wm8UTpylJ3hnN85rgyuIxdRzUFaBwzm-31ukXJxeymIkykW2Hnd-tF4cJui36mEk5dp08S7aqoh527SB2Kg2JMuidf20hosfljDLdXTMM5WlJE5afqtrUbBe_7EIFuheqxq7H9Kt1WtaouBKjaPEk5k_-woQAvzYi8LTLn4B7Nevm9UlyKWt-od0QFT77l35Hdhr983-WZ2kUqSli5l7xnWyt1ddr_EIo6p4fc7wX6XCg2KO7wAAJSj8EHUR7hsyDsEIwVdPF1bFKrxuPbwXYj-aXiY6h46Cwf3eaLyP3DAM1sWG_dxr1gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر اختصاصی خبرفوری از آیین وداع با پیکر رهبر شهید در مصلی تهران
🔹
عکاس: سمانه صالحی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666805" target="_blank">📅 09:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666804">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mf4ob46WLyIQY5a1GUudcoIJwLW_aRfKcd_IldcMZggbOgt33y2G1eHKHZPyqkjktjYudV9Jn1DSAhm66xdE2xtSQWhnKvPgySNbHlJrlydlBEPffvAZTdBDJ9c86rea4JQ7HoPUU9LpS7ahUrZytAKAmUkcuNj55_KZ9NnSXwWGiC0BO9-Pkv7Em3XmameEr7EDIUnATrD1aCfbre-e52rVP2_IndnPH2vTX60i2-8oPNesMnZVGltEzJiJ_ZGv7rTLKOg5TXwWxrFwKTk1_cgF_Ufd6LBqFMMp2LOEeJ7VobEVabI-bMpEBkIZeaEJoz1BPt9k-b9vSb_60ti4Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هم‌اکنون| تصویری از خیابان‌های اطراف مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666804" target="_blank">📅 08:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666803">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5fxf3L9gBXECNkEg_31pwxXRmw165OQw41sdo8DKsXAMDTmNLn8nCZva-UMuSpgaKjoJRMLzEMRzD558MMY0YgioenmKSuof9sSAWdgqULVEamCDLIdUScjN_M5BDYxj5GLZKODFcAF2GSo7n6oDPotCP3UxnBYkIkz0aUfSRnGdWebN-3RZeujs202w4QQFv7x2Q3wUvo321k0j31lPnB-3vFJdiNrtq4Kvgs5IYfi0ttGLyfgLVUfW6klucyhUdDLiVqGX0gmbG_6Q8smyriIZdmzjsnlyJ_RxfbiF5qrCsJyrlQ3V1K_8Ino-Pj5z_1Xa7faM8IoRNlpPlqJEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلاکارد‌ یکی از شرکت‌کنندگان در مراسم وداع با رهبر شهید: « اماما؛ پس از شهادتت، ما هم خانواده شهید شدیم»
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666803" target="_blank">📅 08:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666802">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37305e26ab.mp4?token=kd8X-TYEYnLsLPFx-n2YRFosZkUIJDLkh5SAvBQH3C5qh8ZZyu2REnDswTVBrRlxAetSkhjA6uEiYN4TBhrZymJw_EN8ka4KwuRzSiiU0sD6k1pF2Va1U8yEDjgXFdRSIBWfp610zXy2C-qL_jnuwBqwKIC8jNc-FfqewozqjjHDYKfdam25ULohRNB_5v_ODiMyjFna2OMtR5GCLeR61NAaOJFvm9OrTKb2bbmbzYMza4wAV15l6nNR62xNHEa73mgW6MYti25ySWuU_rj8jiFBTkD9pP3-w-ANCdyEM2gQBv61Z1wzdIKrMWV08qOuFkUzlgyHKV8LX0g-iUw6VTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37305e26ab.mp4?token=kd8X-TYEYnLsLPFx-n2YRFosZkUIJDLkh5SAvBQH3C5qh8ZZyu2REnDswTVBrRlxAetSkhjA6uEiYN4TBhrZymJw_EN8ka4KwuRzSiiU0sD6k1pF2Va1U8yEDjgXFdRSIBWfp610zXy2C-qL_jnuwBqwKIC8jNc-FfqewozqjjHDYKfdam25ULohRNB_5v_ODiMyjFna2OMtR5GCLeR61NAaOJFvm9OrTKb2bbmbzYMza4wAV15l6nNR62xNHEa73mgW6MYti25ySWuU_rj8jiFBTkD9pP3-w-ANCdyEM2gQBv61Z1wzdIKrMWV08qOuFkUzlgyHKV8LX0g-iUw6VTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ای غیور ما، سید علی صبور ما، خدانگهدار
🔹
لحظاتی از شعرخوانی مهدی رسولی در مصلای امام خمینی(ره) تهران.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666802" target="_blank">📅 08:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666801">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHR-cPM-GRMorHgimJb1oP0fNWhwK2GFtVL7lAHNrTkvNDSsVev9ISNXZ9l_ygo6Yu1KSR1cqeqglLZK7Q-Fp81HGHOYk3WU31Et9-q1sla9ig_Fda-qEZ0zohXt67FjfyDcgLg5H775ycmgPcuPIOiWiw0MkXfR1rn7peVuUobcOyPfFdBEBnapM5__RV-NEHKbQ-Y45fF6-5yOXsXHMZ1NhPQqcqjTwZ85S5Jlse4HTe78Ta45VbPXhspqf7m_qDHMhD88WlbQnUWySxeoSZrTcCTV48KY4NVoX4WODNoI7YDXwismwiQTslSgMHfVpHddtwCw6Bu34k2vvxtXKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استاد سوئدی: ترور رهبر عالی ایران، حکومت این کشور را قدرتمندتر کرده است
آشوک سواین، استاد دانشگاه اوپسالایِ سوئد:
🔹
انتظار می‌رود نمایندگان بیش از ۱۰۰ کشور و ۲۰ میلیون ایرانی در مراسم تشییع پیکر رهبر عالی ایران شرکت کنند.
🔹
ترور غیرقانونی رهبر ایران توسط نتانیاهو و ترامپ، ایران را به یک قدرت بزرگ و حکومت ایران را قدرتمندتر و مشروع‌تر از همیشه کرده است./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666801" target="_blank">📅 08:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666799">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfubpvhAs62rMh1gNsCfmZQw6qkFxBekm7iPXU_rUKojTs6wD3KOXpD7tx6r9Irl4jyl5-9hPM1kRnhhjIn05mIzY8ImTi3eEBBy9A5NNSV148U97sOBB8odspenpMS9dN-fjH4ypi_1evARHFDhk0ISbFH5lBvgYB_abAeOz1sVnLQL4L5uco4C3m-tVC_jmWHwP5894yI6nB3TceC1tIS9ups25wgXloZ6ZflGh9mqO-TJLFzh3IYBgU3WTWhBneu6iynFJ6GvIBKZe8wlfOkaV0S1_OVcypWjqszuHAuePUBZksVcqxkRkH2MiKaCQOUwmuFNTBDZAxo8gCObRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تلویزیون عربی: خیابان‌های اطراف مصلی نیز مملو از جمعیت است
🔹
جمعیت امروز بیشتر از دیروز است؛ خیابان‌های اطراف مصلی مملو از عزاداران شده که با شعار و پلاکارد خواستار انتقام خون رهبر شهید هستند.
🔹
پرچم‌های سرخ و محور مقاومت در کنار تجدید بیعت با انقلاب و رهبر جدید دیده می‌شود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666799" target="_blank">📅 08:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666794">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-zqWwUVQQB9jzjhNg0fn_ibKBdpndxS_c9xLO5MRyM4jyLy_oPPCy8DeBxV2CJEDZZYfw-c9mBBPdG_YxjhzyAlFgH1mTflfv0wTrZnns-BS9Kj28jRb7ch_e68k2_MJV-1Nm6bMQhFNAOxY9Mxm6uuuFTvxm0oKA10A4a6bXOJdbeg9hMy_ewRslTETneLp1VGCofeaOnLas8gkGuSAzOvjbEyecOi_5P9QPzNyOOTPliSSS_sVhQBYu7tTSONORzxyFO5odx9Y7EjJjvIQW9_sRyEDuDGICnKg9_RaXqlLxBZeR89WBU0otBM-UFWjpfsQgyf7VLCSl7qeQZ9hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kw0RJXVPBwezlEDO60KUvOTO1jX5_MFcQ5GVKf3xKpVA-REz6M6RGji5t6Zgl-NImQzir2kaB6oLQ1WAgj6TiTS59awVvMMoI2N6IT5wmYKr86FIMfCSSDkhwCiVnaO0u9JF7IbBPztABZiMIcrdUPOW0tMbV6qqA7vx2mtl7Jvmh-K8FwY2Wi9aJZsXpB3OGwByL1JkPUwcI97ENmvih9MN-4Zump5WWnhJrIKRsF0t6jndLgVIoxA_cOHNNiXtdEAYLIaRT2PzNyE5rG-UBvp_0fCI1Nwijsz14m3BH9y1HhHog2SdctPPo0xc--G5rmZrhJ5O1m-2HJsZGSG3rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h5_D1JwQa2ZGSp_E3F8qVuHMqidrBI8VqLyFPzbddpo2U-iSfpUJvYupVZ85uFhS00ZYkeSiGekrqpMRBWK5gIacWRY1IL_oq1rkqGkfjl1UtUidTPma1VsSx8Pcc0cPBkrYAyB9gN--UP2Wj3JphMjdb4zibDstogUYHw6oY8W9YTqz9SN_oLqpXB07GTkizEj_MWdiBmkzRCtFXgtUPDPV0MoiGOaG6BG52IEIkVIILVc9srEqnWaXnbD6OyRJvE-7o8erp2Qlg_lfYvDY-rg4EAniWbonXsERKgEO8v0Y6jKUhKrpG4-99TcWTL1fBPtrx-GXMMzpyus4X3A1cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oc6u4Om-s0qKa_XLQrBq-E884Ygcu__2uW1eF5sBMOmh3HLsJiw426DW9qgzwm584w4SS-A-FNC8IReg18LkhFkjpTxwOtEQxZXcLfsQlM86jJ9w5LHQfJEwKoLXK7XhXGw-5th4F-r0rFqnHMEXt1nDfe6IutpxwRPquXRupgVoWmL22CoIi7xYX_z4OsUcWb84OyfXILJl5S1JjYXBsUqHlRVWVars6-vpE7v2QIJANeUZmqQycPD9ZsIUe9k6LawYe_yktqOPRcg2CQeNJBluchqjqdmqhnvJgxetHiulMD-O0F6Del-ZqIMoXyvJCTWnDjAv3szXSl8PW0ur-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZnfruFPyTVZ3we8sNM0Sk5wBqOPIQIZYgqgUkihdzaSnEXd5TuMTx5aqj7zZfrjh7s9SUPlIlSrCE7ACiYwUJlvkZffi_hlItvLAgzZg0O1gKAGZzFcq0B5jphL-DsgPvVvzRIM7seNvxeq7wYkwBXz1Cra0x1_9eYH_87YMF8eA7sOBk-lw_7MJru6K9QFUWto_F-BRVh7vFgbFPFIG-aXv2-fIdlgLVOo2D40DcFGniZAABitIranU03mm6xi9ZJqswLLLmDkftOtf0hSmncVMR6WFP8fshOiwWjS5Vh-wb2BMkLcHUQ89Zhvrw-3cJjFomBQRRdEIXcfSD9qkBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مراسم اقامه نماز بر پیکر آقای شهید ایران
🔹
تصاویر خبرنگار خبرفوری از اقامه نماز بر پیکر مطهر رهبر شهید و خانواده ایشان در مصلای امام خمینی (ره)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666794" target="_blank">📅 08:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666793">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7451993ab0.mp4?token=CuW4-7CFshGPF0o_OhHwwBjj1hhRaffASDEfVOdnVcw001PZcrkgrBhupeG9LAf7AYNPPGIh40sxs7PlsxlB5m1pPVtEqBr3wXgB8CTYDn9GBelIKuWCLkmddLBlSmhBOgLs81NqH_rw18126B6Wp_DchgAupUJ5CYcok8l4yszb4RsmIT-bWd11OZgE1VTwfmUgCn06Lh7Kg89jIiRNedBSLn7rjMDJza71Qmc507NPdRC5rizd9_m7kdzPwD9EUi8oMy91l3eKbGAZmppEFWk-_j10CqzhShekP9YWmFnj0KQbu4ef3iBl7DEw_Z3Ovz63kkIOvpjPALC3M6utDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7451993ab0.mp4?token=CuW4-7CFshGPF0o_OhHwwBjj1hhRaffASDEfVOdnVcw001PZcrkgrBhupeG9LAf7AYNPPGIh40sxs7PlsxlB5m1pPVtEqBr3wXgB8CTYDn9GBelIKuWCLkmddLBlSmhBOgLs81NqH_rw18126B6Wp_DchgAupUJ5CYcok8l4yszb4RsmIT-bWd11OZgE1VTwfmUgCn06Lh7Kg89jIiRNedBSLn7rjMDJza71Qmc507NPdRC5rizd9_m7kdzPwD9EUi8oMy91l3eKbGAZmppEFWk-_j10CqzhShekP9YWmFnj0KQbu4ef3iBl7DEw_Z3Ovz63kkIOvpjPALC3M6utDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک‌های مردم در فراق رهبر با مداحی حاج محمود کریمی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666793" target="_blank">📅 08:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666790">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e0057730d.mp4?token=okkXl6rOZJ4gXemWEs5G2hX2yTspL2HSvwa96pSOgWMBmLgJ4xdjb3k3Q8ZAnGd-1wKhkdoUNW6oKRIYU2gU7r0mUxB8RL37VO7DBNO8y3_1TMqTfJB2DR1ydDDm4MTCIwoyRzz7nogYbwpl_1TA0BTYTUy8nPE_aKTFz7ABlldG3kKm_83Icy2FjatdXcj4ePNAed6J6oUdaFswJ8zEOCQW9cPjP5IoCULd7Ckx2rZ1NV304xocKJVlqoJClglLLDINBTvMP1zP2wzboG5WZ_7VMEz19OChfzV8792geIChAIk8OTzh7UpuwVR5RqXZog5piSCBwYDa5mAaySot1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e0057730d.mp4?token=okkXl6rOZJ4gXemWEs5G2hX2yTspL2HSvwa96pSOgWMBmLgJ4xdjb3k3Q8ZAnGd-1wKhkdoUNW6oKRIYU2gU7r0mUxB8RL37VO7DBNO8y3_1TMqTfJB2DR1ydDDm4MTCIwoyRzz7nogYbwpl_1TA0BTYTUy8nPE_aKTFz7ABlldG3kKm_83Icy2FjatdXcj4ePNAed6J6oUdaFswJ8zEOCQW9cPjP5IoCULd7Ckx2rZ1NV304xocKJVlqoJClglLLDINBTvMP1zP2wzboG5WZ_7VMEz19OChfzV8792geIChAIk8OTzh7UpuwVR5RqXZog5piSCBwYDa5mAaySot1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظات خروج پیکر رهبر شهید انقلاب پس از اقامه نماز از مصلی
؛
حمل پیکر مطهر آقای شهید ایران روی دستان
مردم عزادار
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666790" target="_blank">📅 08:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666789">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9510708df.mp4?token=SIIw0e5ZI3d1OQ06nwAphVqOMTQIEVju86gt-3rxfIXKNs3KmMAXepEsSXkza_ZPH-UUjvo0i6lpfuPbcgBwFXzNXV0d38HpMzwoEtqqKu0ky86x4a9K7soS6lpbO5oytbtuYbqBaMHDrR6O9o2EfPX_dy-NXjLSBTw_BHTfWuaCr5CSB2sD77IPXkm6qAJ-wRZB2uDoxKvLpHBFK2-pyuaU_9AeC0CtQf9HHvsp73npF1SG_EZet4R9znvrnBiHo_NdjP-lVswpY8FnUbO1Wuba82gxSar_40lcnZuw1z7nlgmhjeiVG4RnuL2XCInhgFx3WcLfVms9_9XQh-4KpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9510708df.mp4?token=SIIw0e5ZI3d1OQ06nwAphVqOMTQIEVju86gt-3rxfIXKNs3KmMAXepEsSXkza_ZPH-UUjvo0i6lpfuPbcgBwFXzNXV0d38HpMzwoEtqqKu0ky86x4a9K7soS6lpbO5oytbtuYbqBaMHDrR6O9o2EfPX_dy-NXjLSBTw_BHTfWuaCr5CSB2sD77IPXkm6qAJ-wRZB2uDoxKvLpHBFK2-pyuaU_9AeC0CtQf9HHvsp73npF1SG_EZet4R9znvrnBiHo_NdjP-lVswpY8FnUbO1Wuba82gxSar_40lcnZuw1z7nlgmhjeiVG4RnuL2XCInhgFx3WcLfVms9_9XQh-4KpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قرائت قرآن توسط حامد شاکرنژاد پس از اقامه نماز بر پیکر رهبر شهید و خانواده ایشان در مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666789" target="_blank">📅 08:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666788">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65bff61228.mp4?token=tLkccoEASu-OGCO-Emvw6AbmruOeMGcdKmerIPkOOiVn_VKRmbhrflDPHKxxSN2vgAsdxesWwkbcFLMDKS7Qi6G9zTF3kiLCK7Up3jX37IxeG_cfzJXJH8AD6QWwSsd3eRF8B4dvRVttdXJ44vhT8Cl-9X3C5C6BB6avbt3MqKUwzX21bNrMl0Ub3HqFhOSKBHzt_Zl3t4OfElwcFzvjxWygEd1HnaSMPJBQKFtOasmTs-7ZyzuQ8N-HeRhY_8xoMSaRmQx_dzllbBEDKZQTHGVIlKhOKM11c7TX_bNEX3KCQxlMMF9rqH4dg5Tz50ob61uq2jRfodgswnl_-_Gr6JfdQrCc6vrAqZy4uGNE2ZkBcZEneZqXTJkshXla_wEFbhJ2NGgBpmjr7CzF4cHmnqYfSiFvgHhMddiY63ReOiOdEggH70uSSdhggsLcJf3yYTD8GExzXvo_33-ElBq4mNVvIal4rsqsqYZmjMaWH7LySR9IYrq26eAeHUJool3kTfdL6m-BIauUTW2Pp1Iy1PuLTUdEIiJaebWCKDQcytE85EJOuinnOCsW1j11hZG5URTFHZVCozRHqa5mIRuJ9zlr5QINEPohItcEL8oXvkwMD4tOb4Gu5ALyhAlG-Bh5l6JWZf-2ljcDO1aKjzwh0EtTGKpSqoSMeG-j3uep2Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65bff61228.mp4?token=tLkccoEASu-OGCO-Emvw6AbmruOeMGcdKmerIPkOOiVn_VKRmbhrflDPHKxxSN2vgAsdxesWwkbcFLMDKS7Qi6G9zTF3kiLCK7Up3jX37IxeG_cfzJXJH8AD6QWwSsd3eRF8B4dvRVttdXJ44vhT8Cl-9X3C5C6BB6avbt3MqKUwzX21bNrMl0Ub3HqFhOSKBHzt_Zl3t4OfElwcFzvjxWygEd1HnaSMPJBQKFtOasmTs-7ZyzuQ8N-HeRhY_8xoMSaRmQx_dzllbBEDKZQTHGVIlKhOKM11c7TX_bNEX3KCQxlMMF9rqH4dg5Tz50ob61uq2jRfodgswnl_-_Gr6JfdQrCc6vrAqZy4uGNE2ZkBcZEneZqXTJkshXla_wEFbhJ2NGgBpmjr7CzF4cHmnqYfSiFvgHhMddiY63ReOiOdEggH70uSSdhggsLcJf3yYTD8GExzXvo_33-ElBq4mNVvIal4rsqsqYZmjMaWH7LySR9IYrq26eAeHUJool3kTfdL6m-BIauUTW2Pp1Iy1PuLTUdEIiJaebWCKDQcytE85EJOuinnOCsW1j11hZG5URTFHZVCozRHqa5mIRuJ9zlr5QINEPohItcEL8oXvkwMD4tOb4Gu5ALyhAlG-Bh5l6JWZf-2ljcDO1aKjzwh0EtTGKpSqoSMeG-j3uep2Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعارهای انتقام‌جویی «یا لثارات‌الحسین» مردم در مصلی تهران پس از اقامه نماز بر پیکر رهبر شهید
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666788" target="_blank">📅 08:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666787">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2157a035b.mp4?token=gWWIBxW7Xujk0_g8tbCv6T8EjS6bEEjctZKbNdzAdefnpPBk8SXzzErijhgwsgKt4XE-3pxFVcBCKFqoV3_W3AKG5gkSiXxIvomcvUMh53cobddG-BkQwBWjEIgk9nxK4bTwwmX71GYEIQF8nwHQqyKl85cpgT5TVEfMEHSCyBwiYVDEZ1C1vlYfyQZk803gkFdl6LWgRuezZVRVW6gbO5-y7RKSYJI0RkHZ9J0K-2j4Uj5PP5oybohyR7PRiHszmRAqVq9-DS9Ayj-3U108JQUp5RH2u5Szr2EqvZQX933-zG-CdKjNxojtSpKu1Fc3lzWl-IUHk25ytHeBzf6Vew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2157a035b.mp4?token=gWWIBxW7Xujk0_g8tbCv6T8EjS6bEEjctZKbNdzAdefnpPBk8SXzzErijhgwsgKt4XE-3pxFVcBCKFqoV3_W3AKG5gkSiXxIvomcvUMh53cobddG-BkQwBWjEIgk9nxK4bTwwmX71GYEIQF8nwHQqyKl85cpgT5TVEfMEHSCyBwiYVDEZ1C1vlYfyQZk803gkFdl6LWgRuezZVRVW6gbO5-y7RKSYJI0RkHZ9J0K-2j4Uj5PP5oybohyR7PRiHszmRAqVq9-DS9Ayj-3U108JQUp5RH2u5Szr2EqvZQX933-zG-CdKjNxojtSpKu1Fc3lzWl-IUHk25ytHeBzf6Vew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک‌های حدادعادل هنگام اقامه نماز بر پیکر دختر شهیدش
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666787" target="_blank">📅 08:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666786">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXj1M6_9yg8pnZrSM0usxdfOczuVRDqTMy3zQPu7I464DV7DfUCrW4cx5DtCE5ziF54TYsTXIMIyOdMSvAJnHqr14nzQ_1hZe8w00UqdpsaVHGtFhpHBv6NFSTqdKLV7MRsjW5hq3L5Zdq5iIdEftg17UqjvUeWfwXkhma9QFtlR1IrgPyX3vnP7IdfLnkboOlbdqoxFOLAKXYRbnMnkXkmZIAbrkT89sGFchXMbrabhhyGHMk5Yxk6DNP2-aqy9kYX5NbHSb2X3dsRCKVIJBbXR3Uq_dHhVDDgE-AetHSTFXsRo6GvUsJGS5au-VoPa1t1TZEUtBGJsSxRdO_qJeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از پدر شهیده زهرا محمدی گلپایگانی نوه ۱۴ ماهه رهبر شهید در لحظات اقامه نماز بر پیکر دخترش
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666786" target="_blank">📅 08:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666785">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/338b21beb1.mp4?token=iK-RGs7bLII0QhHDMMszZ4fASZKCo4xerjBm62rp_adOXHmBTWYxkNfA6pSQC2Rklk33OW3QWZ5sxkVB7Tw6fTEm7nS1HCm0yTwMNOzDOtv-yS_OGZh89PAB8--0GVvhd9C5LYnqwODOkC_Wzs6L4ZPTDCOn2zj4uGE3M0MtdBsHS6CvxLqLKHLGytCTW6LZEDnogi7V1T_Ct3epPqYCViNaHv70nq4_2p_eNoNiaHjWCh-UV7meC_5Hy9boBONuim-S2Rrb6AYmNEW2FNOJJSbFNX9X7GTzxVyn897uL6Ue44Q_jvwo3bafG1kzY0qXYMgfa5hdGFGTEsXojQFl4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/338b21beb1.mp4?token=iK-RGs7bLII0QhHDMMszZ4fASZKCo4xerjBm62rp_adOXHmBTWYxkNfA6pSQC2Rklk33OW3QWZ5sxkVB7Tw6fTEm7nS1HCm0yTwMNOzDOtv-yS_OGZh89PAB8--0GVvhd9C5LYnqwODOkC_Wzs6L4ZPTDCOn2zj4uGE3M0MtdBsHS6CvxLqLKHLGytCTW6LZEDnogi7V1T_Ct3epPqYCViNaHv70nq4_2p_eNoNiaHjWCh-UV7meC_5Hy9boBONuim-S2Rrb6AYmNEW2FNOJJSbFNX9X7GTzxVyn897uL6Ue44Q_jvwo3bafG1kzY0qXYMgfa5hdGFGTEsXojQFl4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار مردم در مصلی: یا حجت‌ابن‌الحسن تسلیت تسلیت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666785" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666784">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10526db91.mp4?token=Cay4TT5yNoOSmKNKcyD--u4a1nKxGQn3ZdhqsOXSL2qwUZMZYz2TczOtM7z6GTq2KR2ia8JOtzEG3f22gLWnJAiOqkIdhCnLTVoGueBlEWdlrmWQQkjXXA6rJUkn7TCfFsoBaUkvZ2JcX2nCvev3auuPGNaFOnIWudbYE4kCiRoqR5ae5o6unU6Idb5Su4zBip5Y41MTw_ZQwajSQLKQ9nQw6yvQwR96NItBM_Jx6pjPLQQ0eZgkHhyY0TgihNJ7zIK_KcNprMhuA9EtwVMb8BXmrhHaSHfPKZv5CmrZ-v3PFKqOcWlMHZmLo9NzmuZTjM1td4s06zRBqKAOl78yMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10526db91.mp4?token=Cay4TT5yNoOSmKNKcyD--u4a1nKxGQn3ZdhqsOXSL2qwUZMZYz2TczOtM7z6GTq2KR2ia8JOtzEG3f22gLWnJAiOqkIdhCnLTVoGueBlEWdlrmWQQkjXXA6rJUkn7TCfFsoBaUkvZ2JcX2nCvev3auuPGNaFOnIWudbYE4kCiRoqR5ae5o6unU6Idb5Su4zBip5Y41MTw_ZQwajSQLKQ9nQw6yvQwR96NItBM_Jx6pjPLQQ0eZgkHhyY0TgihNJ7zIK_KcNprMhuA9EtwVMb8BXmrhHaSHfPKZv5CmrZ-v3PFKqOcWlMHZmLo9NzmuZTjM1td4s06zRBqKAOl78yMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سردار وحیدی در صف اول نماز
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666784" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666783">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c90e72396.mp4?token=LZ2qvSD8W0it1grqWtXpeUHV8pJHnh13zT-HOJL_hOkEuTiSnOv_E3Ny9-Kifj0MUM3Ca6gfBa-E_IwuaaTY_U2cjEy4ZveMCMyL1zcLwKK_ZhfgCZTDhZX5FIfOfPoYp2un67nzAZ8l8SwVPLVED0F5lwMKDCPnWEKDMDEmIbGFJ_mEGgtDeD12SYrnjcjBjH5OUVUBomZO5sZiCtvhdO_Xy-c1u5DbQicXZTRNhMUAStTJC-Tvug8Ar9ze0fDhWAaqZQvGck060_T_cpbcgRyLyBsbKV_l7lMMbx23j3AxjOtLJeneAkYsz9F7r3mrkyb8NS60WmC5XZF3b3kY7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c90e72396.mp4?token=LZ2qvSD8W0it1grqWtXpeUHV8pJHnh13zT-HOJL_hOkEuTiSnOv_E3Ny9-Kifj0MUM3Ca6gfBa-E_IwuaaTY_U2cjEy4ZveMCMyL1zcLwKK_ZhfgCZTDhZX5FIfOfPoYp2un67nzAZ8l8SwVPLVED0F5lwMKDCPnWEKDMDEmIbGFJ_mEGgtDeD12SYrnjcjBjH5OUVUBomZO5sZiCtvhdO_Xy-c1u5DbQicXZTRNhMUAStTJC-Tvug8Ar9ze0fDhWAaqZQvGck060_T_cpbcgRyLyBsbKV_l7lMMbx23j3AxjOtLJeneAkYsz9F7r3mrkyb8NS60WmC5XZF3b3kY7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماز بر پیکر شهیده زهرا محمدی گلپایگانی نوه ۱۴ ماهه رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666783" target="_blank">📅 08:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666781">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c577d50cba.mp4?token=T4-gnLBB68MjRcC4KnHsA6ukFD3lzHuuoq_ISCHGZKNHJEWogsZ4gZG-Xdl_4TmBRM8xMnIWk4_WdtgxEC6C78xBmVtvfeS5NzFsJaCPNSQm1lovgndNer0ciBG25HDN3LzwDJfv7rTlVLfFRosoaiqR-J6l66pnYYDXlXsFwj_LJvRszV2I2XPkuuPeq59-GEFWt0joaxCCEqAdvMPmPf256bFF4cul_yCC27zYK5oxGA5cRCqO0sFz7XsSvugU21ccK1542oyA4vC4IlOqlnpimuw_-_3auLui2vS9JGiVCp4TXGRZQhd93QqajKq3JELRRsEGygIzIC0JsbTOEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c577d50cba.mp4?token=T4-gnLBB68MjRcC4KnHsA6ukFD3lzHuuoq_ISCHGZKNHJEWogsZ4gZG-Xdl_4TmBRM8xMnIWk4_WdtgxEC6C78xBmVtvfeS5NzFsJaCPNSQm1lovgndNer0ciBG25HDN3LzwDJfv7rTlVLfFRosoaiqR-J6l66pnYYDXlXsFwj_LJvRszV2I2XPkuuPeq59-GEFWt0joaxCCEqAdvMPmPf256bFF4cul_yCC27zYK5oxGA5cRCqO0sFz7XsSvugU21ccK1542oyA4vC4IlOqlnpimuw_-_3auLui2vS9JGiVCp4TXGRZQhd93QqajKq3JELRRsEGygIzIC0JsbTOEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از تکمیل ظرفیت مصلای امام خمینی قبل از شروع نماز بر پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666781" target="_blank">📅 08:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666780">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آغاز نماز بر پیکر شهیده زهرا محمدی گلپایگانی نوه ۱۴ ماهه رهبر شهید انقلاب اسلامی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666780" target="_blank">📅 08:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666779">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
اقامه نماز بر پیکر مطهر شهیده سیده بشری حسینی خامنه‌ای، شهید مصباح‌الهدی باقری و شهیده زهرا حدادعادل
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666779" target="_blank">📅 08:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666778">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff1db6da14.mp4?token=YaeR36zfTzciXBNvB0mPjk0LL3CUdnsEtKBb9-z-UFITv90sQrzTkdmH_qbY_UYcKoiCefn2w9wkGh_453nKCYckk5Nxa-Pbo3YCJvBsXA_ExQ0U1Lobth9vK5tU88lH64dm7o0oUJK0gsSxq55dtuZvrfZ5GN7vKzQTTiw0su7XMhxdpW9IOIZH2PMXu4iBXPX5nwi7_MRsT14zaPf95t1de-Wbh980GG5OcCoi2UsRajBAkhawhsK15rOMSmUmy0j9KOgueef_4GV_7rAhv6jOcqID0QTfN0uXOm42-bkr0Ka6nBWLC2-p2_lZ54bptWrpk6JaKq1m78awNOh8vCtjrIMGZXcdnLkAJhos4WwIaudHNmAseV2DYqOyMmL9nMYxIpId3R8y-MsgRo8EL2FKpZ3jzmLljcYhIY-Xb-NvZoo2Aqgl33HiC4nmnBLKUJkCnf_UcYqGPUK8Q0rYWmAibo7flrCc3cfxA7485KqLDGUQ2Ax6HFMDr0lvXjnJSRwzj9cQtZ8Q1DUw0uYm4pinwCy5GdmqG2uRLjnp5927YTnW6uo6fI7gn2HBOaASCHyMPBY8Wjafi-51wp4I-a9v2j3lX9wfR0dmwQkFJNYxvIjIlPTIW_b-ptFexNW7IlX2X-3PrKQQkKqmvUijP2V3fmFTi-6yS5ErI_4AxqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff1db6da14.mp4?token=YaeR36zfTzciXBNvB0mPjk0LL3CUdnsEtKBb9-z-UFITv90sQrzTkdmH_qbY_UYcKoiCefn2w9wkGh_453nKCYckk5Nxa-Pbo3YCJvBsXA_ExQ0U1Lobth9vK5tU88lH64dm7o0oUJK0gsSxq55dtuZvrfZ5GN7vKzQTTiw0su7XMhxdpW9IOIZH2PMXu4iBXPX5nwi7_MRsT14zaPf95t1de-Wbh980GG5OcCoi2UsRajBAkhawhsK15rOMSmUmy0j9KOgueef_4GV_7rAhv6jOcqID0QTfN0uXOm42-bkr0Ka6nBWLC2-p2_lZ54bptWrpk6JaKq1m78awNOh8vCtjrIMGZXcdnLkAJhos4WwIaudHNmAseV2DYqOyMmL9nMYxIpId3R8y-MsgRo8EL2FKpZ3jzmLljcYhIY-Xb-NvZoo2Aqgl33HiC4nmnBLKUJkCnf_UcYqGPUK8Q0rYWmAibo7flrCc3cfxA7485KqLDGUQ2Ax6HFMDr0lvXjnJSRwzj9cQtZ8Q1DUw0uYm4pinwCy5GdmqG2uRLjnp5927YTnW6uo6fI7gn2HBOaASCHyMPBY8Wjafi-51wp4I-a9v2j3lX9wfR0dmwQkFJNYxvIjIlPTIW_b-ptFexNW7IlX2X-3PrKQQkKqmvUijP2V3fmFTi-6yS5ErI_4AxqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری از مصلی تهران: تمامی درب‌های مصلی بسته شده و از مردم خواسته شده پشت درب‌ها نماز بخوانند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666778" target="_blank">📅 08:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666777">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8976e23934.mp4?token=qKGMpUqMSKavFANPtpNh3qzorNEk9RksgcBHintiGYsH2BR94UlRKkwzxa6pew0WxiXLIT1xYSP17U6Qu-lRrWVxpDS2lSSIvvLqxvgYP0Kzs-LRo6QzwF51NRGlbQrV3NVyFDiHSWTMpLdtQeweFi7_v307_zQQU-Wsw_5requSlfGogklnPhiLuIjXh4By-2RqF9PlSaw-ObX2Pt_bTzp0EiDXvTL36t7YgCejPEW0pFmtJmZc6CdRFHNF7oaAh0JJemN62T9obYud1BrGGYj9QeWhOyWLAO0DVkoA9Wl9y5rYLAYObWzwszixUz4TWcJxOL2T0m2P5e8OTKA7zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8976e23934.mp4?token=qKGMpUqMSKavFANPtpNh3qzorNEk9RksgcBHintiGYsH2BR94UlRKkwzxa6pew0WxiXLIT1xYSP17U6Qu-lRrWVxpDS2lSSIvvLqxvgYP0Kzs-LRo6QzwF51NRGlbQrV3NVyFDiHSWTMpLdtQeweFi7_v307_zQQU-Wsw_5requSlfGogklnPhiLuIjXh4By-2RqF9PlSaw-ObX2Pt_bTzp0EiDXvTL36t7YgCejPEW0pFmtJmZc6CdRFHNF7oaAh0JJemN62T9obYud1BrGGYj9QeWhOyWLAO0DVkoA9Wl9y5rYLAYObWzwszixUz4TWcJxOL2T0m2P5e8OTKA7zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اللهم انا لا نعلم منه الا خیرا...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666777" target="_blank">📅 08:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666776">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCuB40J9WV-Bj09hooWe61GBAAVQllgT9DbURwnNmV4ljnrlgRzcuZKisGoPjMPwfAJ1E6BeeaXeMUTYFvkYkTlixk0JPlRi2UUL0hMsHEfFokMJxpzkzylm9McG41X5ss0LyN6XDV4logFSLhQhxiEjzyhi580K_lb5X19x5iXw5O068JRyuN1mtoQw3aWgR2YtJw50nlf0Hg7OqdL_e6kI7vQTxa3CIvx6rlkF4FVQ8oufuyA9ViCFiiRctnjNHNKCf8-kYWSKQWV7y9TjsWnla91vjDMbsrMbN17Tw1fy-SHAkgZltJeeZa8NH89fNLOtFbirayHxrVQO3-oNKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر حضور سران قوا در صف نماز
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666776" target="_blank">📅 08:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666775">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba2be1578d.mp4?token=c8GNQUXTlhm2nVXvYByDnmh_Fz8bmvxIs150iapt_dJ5IyALYOC62EP_i2GkfFQ1YFBUDTbMPPQqc6SpMxEqTIu9hMbkMmPNNs4njqt1bIApHOL2c2fUfBfDI3zPffnQYaMMINe29vCAhKbyiewBYTzhWel6I1TPWBZBMZf1ch4p5zBgVqQm8h0R0pe2s-NYqPg2kY9J5WNynOFE_ZUJYdO5Hj1wxuTkAHDpQac47e4jnf_T9GnJbC5QilIEQJEbG1MJhqk95HjCbburxYNrXIpan2qwXEp9aROLhwh1Zsc-a2gpjR-1c8n68N7BdZ1iLYayJeG797NA22tnLuSUBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba2be1578d.mp4?token=c8GNQUXTlhm2nVXvYByDnmh_Fz8bmvxIs150iapt_dJ5IyALYOC62EP_i2GkfFQ1YFBUDTbMPPQqc6SpMxEqTIu9hMbkMmPNNs4njqt1bIApHOL2c2fUfBfDI3zPffnQYaMMINe29vCAhKbyiewBYTzhWel6I1TPWBZBMZf1ch4p5zBgVqQm8h0R0pe2s-NYqPg2kY9J5WNynOFE_ZUJYdO5Hj1wxuTkAHDpQac47e4jnf_T9GnJbC5QilIEQJEbG1MJhqk95HjCbburxYNrXIpan2qwXEp9aROLhwh1Zsc-a2gpjR-1c8n68N7BdZ1iLYayJeG797NA22tnLuSUBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقامه نماز مردم در سراسر خیابان شهید بهشتی به سمت مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666775" target="_blank">📅 08:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666774">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آغاز نماز بر پیکر‌های شهدای خانواده رهبر شهید انقلاب اسلامی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666774" target="_blank">📅 08:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666773">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c413de9cb.mp4?token=fFnoY9GYD4yBelABGXvozRgeQ8iLvtnv0IWD0RxSfzzInkwvTKEAkGE8jTUTUlQlgBAB6YEcNTzYnFfSvxA9-wU0pplQZWHtHQzVHeyA2tAB6HxyLnhcDbanXc5zGxvGECqH5biUbRqq3GkH7M0r-lSERw3pVKWmIV18-YV88aT7n-A4iBroaDMB5p96lLknWtH2d7fo2zFFwPoZZaXbfLcT53h_qtSA5176vhyoqvpPHlAa81JbmleyZtvWlKHZ3xRqOxdcrhAp3wJZUccMA9mz3C8hHMuXhVKtePoP6e5EEKNgi32u2EfrqzIg_qdPdPUhFwsqUCLXNPFVTiovzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c413de9cb.mp4?token=fFnoY9GYD4yBelABGXvozRgeQ8iLvtnv0IWD0RxSfzzInkwvTKEAkGE8jTUTUlQlgBAB6YEcNTzYnFfSvxA9-wU0pplQZWHtHQzVHeyA2tAB6HxyLnhcDbanXc5zGxvGECqH5biUbRqq3GkH7M0r-lSERw3pVKWmIV18-YV88aT7n-A4iBroaDMB5p96lLknWtH2d7fo2zFFwPoZZaXbfLcT53h_qtSA5176vhyoqvpPHlAa81JbmleyZtvWlKHZ3xRqOxdcrhAp3wJZUccMA9mz3C8hHMuXhVKtePoP6e5EEKNgi32u2EfrqzIg_qdPdPUhFwsqUCLXNPFVTiovzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمعیت انبوه نمازگزاران بر پیکر رهبر شهید انقلاب اسلامی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666773" target="_blank">📅 08:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666772">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4828947107.mp4?token=D5c2o6DoIXBYJs42GKpVe69cojA-4YvuMDMm4MZRkko9Evnp3RAB3A61i3HR5t0Dr06RKKN00qaU6PPuCgJiQycMN4t18cw-Ddy94BA1P__hi6-H5EpJEgs9-O9UyzlCFUMfUeK3I6TTnwFWKmCuvjFoHbu8BWXGm2Ym1LD6-1A9uxz5PlYQ_TouWxZoU5VwCCIEfFOliGwu29k07CrwdaM9DmUJgpD6is1eDrk65eA6kiKuiDeXOzAJpxodG-smjy_-I0Lhv-fTsWJ2vGbtcPO_0H78WTLNnf8fsFpHKyRRbTEC_GO7Z1kgxX-pFvXskltvll6SZlHTnrkQ7qFV6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4828947107.mp4?token=D5c2o6DoIXBYJs42GKpVe69cojA-4YvuMDMm4MZRkko9Evnp3RAB3A61i3HR5t0Dr06RKKN00qaU6PPuCgJiQycMN4t18cw-Ddy94BA1P__hi6-H5EpJEgs9-O9UyzlCFUMfUeK3I6TTnwFWKmCuvjFoHbu8BWXGm2Ym1LD6-1A9uxz5PlYQ_TouWxZoU5VwCCIEfFOliGwu29k07CrwdaM9DmUJgpD6is1eDrk65eA6kiKuiDeXOzAJpxodG-smjy_-I0Lhv-fTsWJ2vGbtcPO_0H78WTLNnf8fsFpHKyRRbTEC_GO7Z1kgxX-pFvXskltvll6SZlHTnrkQ7qFV6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرازهایی از اقامه نماز بر پیکر آقای شهید ایران توسط آیت الله سبحانی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666772" target="_blank">📅 08:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666771">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7db1b638e.mp4?token=hda8vvcIupvVLEEp8pVbTAKQJMFiLr8Oha-igIV7gabhQpzkK8Zgb2Xm4rIj1MDOfV1spycqk4lve3I-oVZdZIPwkd9a7KtMUT2WnKobAtCA-dWEBnhrJQpS-E3dCEsBvVnaVdbL4L-m4Zf6abBIa7Hwv2Flfe5TuXnW6dkOe0J9DKyNfzud1m3hWKgrT0OTZUPTFqhm-xsUqOqrzNV8lKf2uGgXhqPrJ-VwtGW-IXlgsAFhrFvkRiuS5ZKJGJgMEocLJxaGGwxrx8D5M4kB5bCkNHWnb9-3_DsdTfPP3uLogEFGo37CUgFUyPoalK7__6uiQMq2GRWwvfQwej6jFmFe72tujf-ySvB-rywQbU3Bicf_kiw6HAk2gmX7TDY0VOU0rKKCmlMswuyK2LIgLc1JG-rTRJO42_fgIF-6JsSR5Tuc19Oh68esfnOzS7FWVeBD3qQ3XjqvLUB45af9bVIiIHt2iVaKUViFYpAoD7Np6tFUrbgAKe3BbHZgWLZQDsdSiuquYk8LwKSER5kqKDcltsLm5EMD9FhTW9GF2I4nKyf1mZlnFPLDD93MURfcns42NLzIv-EI8mr_O6OLFK-2Zl-FoeTf2cjruqutwbj5VR1vFSqtr47_4-sxcgMiFoRyTel6C7pMx7idGshM7jpBMvSOs_hBLBKhZJ06vCo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7db1b638e.mp4?token=hda8vvcIupvVLEEp8pVbTAKQJMFiLr8Oha-igIV7gabhQpzkK8Zgb2Xm4rIj1MDOfV1spycqk4lve3I-oVZdZIPwkd9a7KtMUT2WnKobAtCA-dWEBnhrJQpS-E3dCEsBvVnaVdbL4L-m4Zf6abBIa7Hwv2Flfe5TuXnW6dkOe0J9DKyNfzud1m3hWKgrT0OTZUPTFqhm-xsUqOqrzNV8lKf2uGgXhqPrJ-VwtGW-IXlgsAFhrFvkRiuS5ZKJGJgMEocLJxaGGwxrx8D5M4kB5bCkNHWnb9-3_DsdTfPP3uLogEFGo37CUgFUyPoalK7__6uiQMq2GRWwvfQwej6jFmFe72tujf-ySvB-rywQbU3Bicf_kiw6HAk2gmX7TDY0VOU0rKKCmlMswuyK2LIgLc1JG-rTRJO42_fgIF-6JsSR5Tuc19Oh68esfnOzS7FWVeBD3qQ3XjqvLUB45af9bVIiIHt2iVaKUViFYpAoD7Np6tFUrbgAKe3BbHZgWLZQDsdSiuquYk8LwKSER5kqKDcltsLm5EMD9FhTW9GF2I4nKyf1mZlnFPLDD93MURfcns42NLzIv-EI8mr_O6OLFK-2Zl-FoeTf2cjruqutwbj5VR1vFSqtr47_4-sxcgMiFoRyTel6C7pMx7idGshM7jpBMvSOs_hBLBKhZJ06vCo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری: محمود کریمی برای آخرین بار در کنار رهبر شهید، ای ایران خواند...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666771" target="_blank">📅 08:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666770">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc049208c3.mp4?token=Nq-WRhOZBy-JUYMTrFd6iZWrSLI8PdqrQGdizB7-7WgGfELGyzkWlAFkgVCLH3sjIYWmbRaJrqwIFQw2j7H5LpK5EQ7HZN1CWvvmLgV9iCpjsMMyMbXxXp3ezycMebymwfX2xi3ENxlw-Azh5nDWVfkxRnbdC-joXd2kGnMCPVDyZ_mv1tMU04oU7oqTkMPkJ0BlKS_edioJxuatM8h2mwQYaSn1RWINJnB2TBdaKDNkfNCDLvzH74Rb1mwWNiXnoxl-vO5VWHyk1LZD5m_wSI1Oi5SHZatDtjd0UFWLlz8kFfdnyc1TGJDwSvB116DoX6YAJdXx5QiZ-wZZJsTWGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc049208c3.mp4?token=Nq-WRhOZBy-JUYMTrFd6iZWrSLI8PdqrQGdizB7-7WgGfELGyzkWlAFkgVCLH3sjIYWmbRaJrqwIFQw2j7H5LpK5EQ7HZN1CWvvmLgV9iCpjsMMyMbXxXp3ezycMebymwfX2xi3ENxlw-Azh5nDWVfkxRnbdC-joXd2kGnMCPVDyZ_mv1tMU04oU7oqTkMPkJ0BlKS_edioJxuatM8h2mwQYaSn1RWINJnB2TBdaKDNkfNCDLvzH74Rb1mwWNiXnoxl-vO5VWHyk1LZD5m_wSI1Oi5SHZatDtjd0UFWLlz8kFfdnyc1TGJDwSvB116DoX6YAJdXx5QiZ-wZZJsTWGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی دیگر از حضور فرزندان رهبر شهید برای نماز بر پیکر قائد شهید امت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666770" target="_blank">📅 08:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666769">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
آغاز اقامه نماز بر پیکر رهبر شهید انقلاب به امامت آیت الله جعفر سبحانی
🔹
آیت الله جعفر سبحانی از مراجع عظام تقلید نماز میت را با همراهی جمعیت میلیونی مشتاقان و زائران، فرزندان رهبر شهید انقلاب و مقامات لشکری و کشوری  بر پیکر آقای شهید انقلاب و شهدای خانواده ایشان خوانده شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666769" target="_blank">📅 08:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666767">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c304583c30.mp4?token=VAg5SgLP_NyCGhjloxJPwZSuHcdbWVJLjDHdxMhnd0ysfNkImgn7bcYJsJWo86nOYKaTVazn1JZw2YYS5YjnDS6Y_pUvrjJkAhwcdnBEjPBChcu0rNijmSipnd2jngge2B_9p7ExX-GFaI2g4lvo6AMX6jlSYypqoV5E4oik5nWnTkgrLqPYotAELvd04W0iajNKbyIJdwY0GsazWGCC165QrfeKPugGD-m9euiWFm-P3LdD83EKthqpaQY2bXd41UeS7WpS43OyoRyb-Ve1zfA_f7wU7SvXS9aOny7w3luJEvGruK4bBgiaiUMHEYctCUmi4P2-3WNYAUD76TwndA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c304583c30.mp4?token=VAg5SgLP_NyCGhjloxJPwZSuHcdbWVJLjDHdxMhnd0ysfNkImgn7bcYJsJWo86nOYKaTVazn1JZw2YYS5YjnDS6Y_pUvrjJkAhwcdnBEjPBChcu0rNijmSipnd2jngge2B_9p7ExX-GFaI2g4lvo6AMX6jlSYypqoV5E4oik5nWnTkgrLqPYotAELvd04W0iajNKbyIJdwY0GsazWGCC165QrfeKPugGD-m9euiWFm-P3LdD83EKthqpaQY2bXd41UeS7WpS43OyoRyb-Ve1zfA_f7wU7SvXS9aOny7w3luJEvGruK4bBgiaiUMHEYctCUmi4P2-3WNYAUD76TwndA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظات آغازین اقامه نماز بر پیکر امام شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666767" target="_blank">📅 08:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666766">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19d449de63.mp4?token=F8IwZo601D0TSTAPIapTua4FuTCutKWANjgtgQlfJQWOoyw15IEf3sTdJl1GwSqGF7N-YC8LGHCAmnblpcqDuVKcRfXUetevhKrwGfFWeZFWipm2soorrPkq9_40H7IkROvTdH_T9jTFTO_rzHIqPU_ac52QAMd3OTsA0J04qX8tIKq1rQcaAnsE192MFJemJnF6k7Qa4uKdlzm13A0pAFjbVxy0SvCd96Clro3BlkS1XGXAcnC6ao479ZqnLUhCLf1iDwihzgA7fvWYURnCgq5NNVu98zOns-e4aP-n475JSbTzKqTPkkBeTXsRMgmIq1NnYYwOG_nMB-6duiLAmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19d449de63.mp4?token=F8IwZo601D0TSTAPIapTua4FuTCutKWANjgtgQlfJQWOoyw15IEf3sTdJl1GwSqGF7N-YC8LGHCAmnblpcqDuVKcRfXUetevhKrwGfFWeZFWipm2soorrPkq9_40H7IkROvTdH_T9jTFTO_rzHIqPU_ac52QAMd3OTsA0J04qX8tIKq1rQcaAnsE192MFJemJnF6k7Qa4uKdlzm13A0pAFjbVxy0SvCd96Clro3BlkS1XGXAcnC6ao479ZqnLUhCLf1iDwihzgA7fvWYURnCgq5NNVu98zOns-e4aP-n475JSbTzKqTPkkBeTXsRMgmIq1NnYYwOG_nMB-6duiLAmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک‌های فرزندان رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666766" target="_blank">📅 08:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666765">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dce749512.mp4?token=KfcbATYf-p7vXzno0NtoIawPOSJyyBFGPRJe3lTIgTRzM93vxlXD8a3_p9uLePbfMkXCArKuH8rhzYN9orP8oOqgrXHwdV39RhykoM1kyvYX74o6Atl_H_FBeo6yzeM82dMlwSJy0xXG1bjzwwFjqhJzT3RqYcISs2vtQPSC7KmBYtSb1YNQawXnFMxs20scjcXyvVBo2esg6DdBVYiDwyyykT_N5wwEziUgWnCDPTTPZ7jfv6XzVQt70tjVt0rmvfV_f9A-6U-rhCa3bJLePPRpgNcpTV970F94IUKXBiQ7EfgwLHfOEeci2PgGo7udYPkBOkl1gDDkIa8gsyXgqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dce749512.mp4?token=KfcbATYf-p7vXzno0NtoIawPOSJyyBFGPRJe3lTIgTRzM93vxlXD8a3_p9uLePbfMkXCArKuH8rhzYN9orP8oOqgrXHwdV39RhykoM1kyvYX74o6Atl_H_FBeo6yzeM82dMlwSJy0xXG1bjzwwFjqhJzT3RqYcISs2vtQPSC7KmBYtSb1YNQawXnFMxs20scjcXyvVBo2esg6DdBVYiDwyyykT_N5wwEziUgWnCDPTTPZ7jfv6XzVQt70tjVt0rmvfV_f9A-6U-rhCa3bJLePPRpgNcpTV970F94IUKXBiQ7EfgwLHfOEeci2PgGo7udYPkBOkl1gDDkIa8gsyXgqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ورود پیکر نوه رهبر شهید انقلاب به  محل اقامه نماز در مصلی تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666765" target="_blank">📅 07:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666764">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efefc66037.mp4?token=T9-RMA0qmGRYR4gyxUa_t6b2Sz5K1dUpFb1kvot5TMH0njnCQiRJ5Z41K3vSJzSvFOoJZOacDVIAUYjYTszS5--BIoMgD8npdtePAMRTtH1SdmGq4eCdsCzqXjzik7BuljAZE5WS1tQJhM7o1mdizeRfOFpQ1f5EOnHYaRw-m62ppR7rfqnLOgtR_rt7epga_5VJgLr0eAH3TAWO6-a-e7O6pGscOZhqPASzIwgOBjm7HNOgJ_ZhCGKY66OorlFMb-DVxwM55qs3Hfrrar-7CgnhYDEJ57THyBwwzTn8qkV_2dY4_kkmmsS6jE4vh5CmGetPOjbbglKrQwuIUOT0uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efefc66037.mp4?token=T9-RMA0qmGRYR4gyxUa_t6b2Sz5K1dUpFb1kvot5TMH0njnCQiRJ5Z41K3vSJzSvFOoJZOacDVIAUYjYTszS5--BIoMgD8npdtePAMRTtH1SdmGq4eCdsCzqXjzik7BuljAZE5WS1tQJhM7o1mdizeRfOFpQ1f5EOnHYaRw-m62ppR7rfqnLOgtR_rt7epga_5VJgLr0eAH3TAWO6-a-e7O6pGscOZhqPASzIwgOBjm7HNOgJ_ZhCGKY66OorlFMb-DVxwM55qs3Hfrrar-7CgnhYDEJ57THyBwwzTn8qkV_2dY4_kkmmsS6jE4vh5CmGetPOjbbglKrQwuIUOT0uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سران قوا در مصلای امام خمینی(ره) تهران، دقایقی پیش از اقامه نماز بر پیکر آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666764" target="_blank">📅 07:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666763">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/180ce62363.mp4?token=bhTKKcPG98jxZtkZrBk5NStSmYUFC8Au6FBoEc5xrzGwK68yLT-atlRtWO2lMzbOUdxDVJTcK-xo3inCEtKKb4cwMEsF_YyGmiRii-ucq0IPiioqMflfivMxaR3h64eJ-62960-1Ze26xF6r1pvEG9RP0K6wK6j1qg1EJS0nI2S8uURDGa2waCOkoPSZruRQAe2gaxPIvHmZ7oXCm_DyQVBT2FJ2n1EVf0gf_TsTgoGbcxYe89Y9-qg_R_g4hx-We2ZCbzXUipb5uL55zmxLUFVU_uQdwEoycG5mC4jQKvu-2YL_35QB5sSESdkD4lrKTiBp-Aw9fRYt2MuWbn0nnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/180ce62363.mp4?token=bhTKKcPG98jxZtkZrBk5NStSmYUFC8Au6FBoEc5xrzGwK68yLT-atlRtWO2lMzbOUdxDVJTcK-xo3inCEtKKb4cwMEsF_YyGmiRii-ucq0IPiioqMflfivMxaR3h64eJ-62960-1Ze26xF6r1pvEG9RP0K6wK6j1qg1EJS0nI2S8uURDGa2waCOkoPSZruRQAe2gaxPIvHmZ7oXCm_DyQVBT2FJ2n1EVf0gf_TsTgoGbcxYe89Y9-qg_R_g4hx-We2ZCbzXUipb5uL55zmxLUFVU_uQdwEoycG5mC4jQKvu-2YL_35QB5sSESdkD4lrKTiBp-Aw9fRYt2MuWbn0nnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صف‌های زائران و نمازگزاران در انتظار اقامه نماز بر پیکر آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666763" target="_blank">📅 07:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666762">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0abca84454.mp4?token=jtAc4I8xGC0eVYwViJaYrkHcHXDc6NGBLgi2AEvJ2o3PBjwNu1BP8sDXVeqTmjZ7x1EVaKhZsKDvWPdF4dITeOLfiuNAZVMAjqAfqKDVM4bTZ6GlFUC2aiyrJLan2ftbG55E181kMWdopT95KwIVq2vDSs6Jsl5khwAne6DvdOmpAlTqrnb5-nSMD-2-KAVGfd3RsG1Pvh34OZJUY0YV4JjWaYCcS1QXzkUB7bglofSbo6aLrFvTdgcFX-gXFCDk2fPQFyiQyw7tA3G3bC0HEX8xIJaMO-ASNo7VUE0SGLIa_YDbjDbuRnOMMiscI7Rkk5HnK9BBnoXTYDaaeyW344WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0abca84454.mp4?token=jtAc4I8xGC0eVYwViJaYrkHcHXDc6NGBLgi2AEvJ2o3PBjwNu1BP8sDXVeqTmjZ7x1EVaKhZsKDvWPdF4dITeOLfiuNAZVMAjqAfqKDVM4bTZ6GlFUC2aiyrJLan2ftbG55E181kMWdopT95KwIVq2vDSs6Jsl5khwAne6DvdOmpAlTqrnb5-nSMD-2-KAVGfd3RsG1Pvh34OZJUY0YV4JjWaYCcS1QXzkUB7bglofSbo6aLrFvTdgcFX-gXFCDk2fPQFyiQyw7tA3G3bC0HEX8xIJaMO-ASNo7VUE0SGLIa_YDbjDbuRnOMMiscI7Rkk5HnK9BBnoXTYDaaeyW344WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سردار قاآنی در مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666762" target="_blank">📅 07:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666761">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b327e2e6f3.mp4?token=DBh3kshayuI8kGpr97ABvFpzYb4GqSxFg-cOjKP0rAtlbSuJsk3-6bBq47iLL-76uD8neN8v68vvjYz2RGv485UOnmgHeq3U0BKc9L-yS0nRJo2ZN79_gP9abnlPYsNUWXX7a97lENc8vvyTJIm_xDHx2RZeyPUPH5DyTPS0qmS3G-V0NynWd8fofQzCTyFi7DXCXOPu4iFkNTrru3c6efYojHH1EN4rhHyBCmk6PVeqHui84ntUMuaaXlVWELuVyWFFipcCytfVuWmAyLGwJil0z7ebscqiKiDSCGePXeIlIm9cJ0BVYvkktl6HKFT7yl3j4of9McaVuz6Iq7hmrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b327e2e6f3.mp4?token=DBh3kshayuI8kGpr97ABvFpzYb4GqSxFg-cOjKP0rAtlbSuJsk3-6bBq47iLL-76uD8neN8v68vvjYz2RGv485UOnmgHeq3U0BKc9L-yS0nRJo2ZN79_gP9abnlPYsNUWXX7a97lENc8vvyTJIm_xDHx2RZeyPUPH5DyTPS0qmS3G-V0NynWd8fofQzCTyFi7DXCXOPu4iFkNTrru3c6efYojHH1EN4rhHyBCmk6PVeqHui84ntUMuaaXlVWELuVyWFFipcCytfVuWmAyLGwJil0z7ebscqiKiDSCGePXeIlIm9cJ0BVYvkktl6HKFT7yl3j4of9McaVuz6Iq7hmrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود پیکر رهبر شهید انقلاب به محل اقامه نماز در مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666761" target="_blank">📅 07:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666760">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/010d6c2fd5.mp4?token=q888KfcsWZQtwG1TV5jNOgjVtwLj1xg6jY1OnTkD13Ag_whVCPVMrqyrsZda8U3BW41THL683gkb2zB1yu-JenNQlIxAgHsylQ4--Gb3OJ8XL1lE1-P8rIL6JSP8jWRgE56YjZz3j3gGmjMP4tTJfpuwoUEjIo3ABB6pzqk3hLK--76QTa4N138fWppZ9IFBvvDg7qewQz5fczxPHbA2zGx6EQjeDmq8SB-38hwkuZZdC6uhK7UbetvGauxOj42MH8xVqvSaqR_4MLV-DYjjdZ95tcmBlKNT1oYu-KGzHsW61-9ycjPlpqMBSYdgDXkvs4bhBUGCpHsXYKC47YDSnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/010d6c2fd5.mp4?token=q888KfcsWZQtwG1TV5jNOgjVtwLj1xg6jY1OnTkD13Ag_whVCPVMrqyrsZda8U3BW41THL683gkb2zB1yu-JenNQlIxAgHsylQ4--Gb3OJ8XL1lE1-P8rIL6JSP8jWRgE56YjZz3j3gGmjMP4tTJfpuwoUEjIo3ABB6pzqk3hLK--76QTa4N138fWppZ9IFBvvDg7qewQz5fczxPHbA2zGx6EQjeDmq8SB-38hwkuZZdC6uhK7UbetvGauxOj42MH8xVqvSaqR_4MLV-DYjjdZ95tcmBlKNT1oYu-KGzHsW61-9ycjPlpqMBSYdgDXkvs4bhBUGCpHsXYKC47YDSnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور مسعود پزشکیان، رئیس جمهور اسلامی ایران و دیگر مقامات دولتی در مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666760" target="_blank">📅 07:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666759">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d88392f71.mp4?token=BtdRXlomiNxUzABu1eD50GfGygYCJ6B8benFDrAmxucON-5sxBuUWqdj6AZV-NwX-0ox_KjjalE2FsdmNY9bKm2d9IiC8JpdA9UcFyWhmpmaGDSgbqn8Db9x3kfolu9u79YFYIzZ_9NXIXrjYklgh2gqIi989EpSKek1ijzdtrZUEpO9KsWR81ptbB9irmoGHDoiI6u_oVNEIYiw_RMidHoZuPn6rBCyaYScLwy5O-7683lXWLjJyZIkyEVZZuWap8ysnVBNavPJc1HNncE8uFZ1LbzZ2pm0LUpWgUtgRngM84wGXpsBvAGtLYOpNyJQpIO9FiH3eIw8vfUDhGbH7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d88392f71.mp4?token=BtdRXlomiNxUzABu1eD50GfGygYCJ6B8benFDrAmxucON-5sxBuUWqdj6AZV-NwX-0ox_KjjalE2FsdmNY9bKm2d9IiC8JpdA9UcFyWhmpmaGDSgbqn8Db9x3kfolu9u79YFYIzZ_9NXIXrjYklgh2gqIi989EpSKek1ijzdtrZUEpO9KsWR81ptbB9irmoGHDoiI6u_oVNEIYiw_RMidHoZuPn6rBCyaYScLwy5O-7683lXWLjJyZIkyEVZZuWap8ysnVBNavPJc1HNncE8uFZ1LbzZ2pm0LUpWgUtgRngM84wGXpsBvAGtLYOpNyJQpIO9FiH3eIw8vfUDhGbH7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور فرزندان رهبر شهید انقلاب در مصلی تهران پیش از اقامه نماز بر پیکر امام امت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666759" target="_blank">📅 07:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666758">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5371ddc0c2.mp4?token=syySn7wsEgnGzvNg3PPSM7tIZj_iXOZu6SGdVU_kf56pucUDq0ip2bkPA58WRkkCLITldtTb3Vs_Z8Wu-6iYJ6O4op3oUh5IgXVHO2VHLt7TQzDnNa8usvYmsraihl8-Azi2RDNh_gb9F-z5I0k1VYvFE5U53a707QaJZ8d48O9WYbFOUobTgjtF1T20oK2NqKKq7zZHVJc-8wZ4-GtI9QZw35yTwyahBiFxtV7fIc33VP-UyhgEMHAekDnKJhYPNS4dD6Idtc3haY9joA2-EBiJAchEfSxE84SwHMWWKikCj-F7pI2ad3CwvoEQZc10XIOggl4fM4k-BNy5_jcsu5pCypY0vL-Wxhp_lT_M815KTFSLUcWVnBRp37yICAfqgsUk2mT0sVFDNQjnW3shDKKcvC84XZEK4U_g3vjgcCBKva-YFO5HOOEiVlChnMtC4uayBayMKSSlOKc535nQYsjp7tMZErkPtspEhvsAhPhJi8KRVPb4D9WssMq2_6QmVEIAPzU7xeSqzwPGQKZ8Sk9CIernbYTksljOpXrputdKsPmZgDTGPqRLrzid9hf-4IvYYs_822_FektG8hTpfgqK5eNjU2JLUjFyEfPaBfR8zdMX69wlwvXIqWnBpsX49nq_7gqHAYpoiE1bYcpgx0ZqmeZL5gP5aHHqWef0iy8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5371ddc0c2.mp4?token=syySn7wsEgnGzvNg3PPSM7tIZj_iXOZu6SGdVU_kf56pucUDq0ip2bkPA58WRkkCLITldtTb3Vs_Z8Wu-6iYJ6O4op3oUh5IgXVHO2VHLt7TQzDnNa8usvYmsraihl8-Azi2RDNh_gb9F-z5I0k1VYvFE5U53a707QaJZ8d48O9WYbFOUobTgjtF1T20oK2NqKKq7zZHVJc-8wZ4-GtI9QZw35yTwyahBiFxtV7fIc33VP-UyhgEMHAekDnKJhYPNS4dD6Idtc3haY9joA2-EBiJAchEfSxE84SwHMWWKikCj-F7pI2ad3CwvoEQZc10XIOggl4fM4k-BNy5_jcsu5pCypY0vL-Wxhp_lT_M815KTFSLUcWVnBRp37yICAfqgsUk2mT0sVFDNQjnW3shDKKcvC84XZEK4U_g3vjgcCBKva-YFO5HOOEiVlChnMtC4uayBayMKSSlOKc535nQYsjp7tMZErkPtspEhvsAhPhJi8KRVPb4D9WssMq2_6QmVEIAPzU7xeSqzwPGQKZ8Sk9CIernbYTksljOpXrputdKsPmZgDTGPqRLrzid9hf-4IvYYs_822_FektG8hTpfgqK5eNjU2JLUjFyEfPaBfR8zdMX69wlwvXIqWnBpsX49nq_7gqHAYpoiE1bYcpgx0ZqmeZL5gP5aHHqWef0iy8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در روح و جان من می‌مانی ای وطن...
🔹
لحظاتی از روضه‌خوانی حاج محمود کریمی در مصلی امام خمینی(ره) تهران، دقایقی پیش از اقامه نماز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666758" target="_blank">📅 07:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666757">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
اعزام اتوبوس به مصلی در پی ازدحام ایستگاه‌های مترو
شرکت بهره‌برداری متروی تهران:
🔹
به دنبال ازدحام جمعیت در ایستگاه‌های تقاطعی امام خمینی(ره) و تئاتر شهر، از شرکت واحد اتوبوسرانی درخواست کردیم اتوبوس اعزام کند و در حال حاضر اتوبوس‌ها مسافران را به مصلی منتقل می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666757" target="_blank">📅 07:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666756">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3693a04af8.mp4?token=EshrmLjpMbNK7j_XR9UCqTwvjBxDIgmgflFuOedCEFztqXJleq-EGJrDds_MK3R0cpXIeqHU_bmkLTW8VSVKs3lrdZKcdC091qMn-DQ__3CmojQCMFc_QXnjaKX5k8Z9oggJQpeuxh2tPPm8zQWJBUbiOC-O98SRgbP-ZDpu684I9ypDeTiaL6YHg7Qb51e_b82PprA-Mi5lInrnrTekoZpji1Ln9Vtq3h4qlbZlTxPl1VrkjG6jTBXCJOY0Fhs4OjhkWzowOAj3faI1ZY8LxOORL5hdVMim0kuakE0nv1nK7Tq9O9Ofh9fs3RQRgIFMsosHVTMMZGu04dV-WMTngzmA5XT4B60fcufu5gqh8gE4eFDiLQ9coLKoCzzt1tTpxna6C-AucN2qWkwLqSmBZ6Rn260ZO0ZP6-d9JqX6P5fxEkssftpGd_DtCpmp1srobY4NqjQEIjxu-fNEHAX5jpGk590BtmGgZ5bRqO16c3C0XGhX6--h-JbfPCWRh4cPd5BMjGGVpbmUdsb-a8yqeTvhHwy-vk5nIQY9SGUeTXY8Jh8jrLp_tGX3YTWy2GC1MHttIMpeOzexoGswKXrZ_6CfTIcnenZ37K_YTcSzJ27X1Loe1__NW945HRvZ9zowKyDGEIlf62NuY2XPOb4lSTaSCE2ERyHAK8xBEONwVlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3693a04af8.mp4?token=EshrmLjpMbNK7j_XR9UCqTwvjBxDIgmgflFuOedCEFztqXJleq-EGJrDds_MK3R0cpXIeqHU_bmkLTW8VSVKs3lrdZKcdC091qMn-DQ__3CmojQCMFc_QXnjaKX5k8Z9oggJQpeuxh2tPPm8zQWJBUbiOC-O98SRgbP-ZDpu684I9ypDeTiaL6YHg7Qb51e_b82PprA-Mi5lInrnrTekoZpji1Ln9Vtq3h4qlbZlTxPl1VrkjG6jTBXCJOY0Fhs4OjhkWzowOAj3faI1ZY8LxOORL5hdVMim0kuakE0nv1nK7Tq9O9Ofh9fs3RQRgIFMsosHVTMMZGu04dV-WMTngzmA5XT4B60fcufu5gqh8gE4eFDiLQ9coLKoCzzt1tTpxna6C-AucN2qWkwLqSmBZ6Rn260ZO0ZP6-d9JqX6P5fxEkssftpGd_DtCpmp1srobY4NqjQEIjxu-fNEHAX5jpGk590BtmGgZ5bRqO16c3C0XGhX6--h-JbfPCWRh4cPd5BMjGGVpbmUdsb-a8yqeTvhHwy-vk5nIQY9SGUeTXY8Jh8jrLp_tGX3YTWy2GC1MHttIMpeOzexoGswKXrZ_6CfTIcnenZ37K_YTcSzJ27X1Loe1__NW945HRvZ9zowKyDGEIlf62NuY2XPOb4lSTaSCE2ERyHAK8xBEONwVlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مصلای امام خمینی(ره) و خیل مشتاقان در آخرین دقایق مانده به اقامه نماز بر پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666756" target="_blank">📅 07:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666755">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d028f24cd.mp4?token=aCfJwEZjOVUUevyJA0xZa7epH7dd4_vLcufse45hP8SFKithy9XN96_rNgKANsW66aQIBBbmBsZORANPTEn24c-pfr6t9VW1vK7M-VUQs-TNy-lfk4-7S3Avfqowh_M4HsvaxxCVdbu79tTEWtsksNCtZsm0o25E6AZvvLahwUQfL9iXdmpHrhydIbyDGfmwHETvia46z-89EQYM238jeY9w6ic56MulJYM38b4F-jChcaSXzOivIge6kAxC3xw_kMfPUG-rDw8F6BGDwSEedXnOABODG0iVn6p70OoMQeUgnKDGgr0KiHU7SHXAIbKm2QD7LxNsTDSxeu4_unmsIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d028f24cd.mp4?token=aCfJwEZjOVUUevyJA0xZa7epH7dd4_vLcufse45hP8SFKithy9XN96_rNgKANsW66aQIBBbmBsZORANPTEn24c-pfr6t9VW1vK7M-VUQs-TNy-lfk4-7S3Avfqowh_M4HsvaxxCVdbu79tTEWtsksNCtZsm0o25E6AZvvLahwUQfL9iXdmpHrhydIbyDGfmwHETvia46z-89EQYM238jeY9w6ic56MulJYM38b4F-jChcaSXzOivIge6kAxC3xw_kMfPUG-rDw8F6BGDwSEedXnOABODG0iVn6p70OoMQeUgnKDGgr0KiHU7SHXAIbKm2QD7LxNsTDSxeu4_unmsIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت مردم عزادار به سمت مصلی برای اقامه نماز بر پیکر مطهر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666755" target="_blank">📅 07:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666754">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26b5a279ca.mp4?token=CKQl4-SVgc0OfORaPijKQ4hu3n6FW5IvSQR9G2io0pb4bluL17pdXq-MLlSoXJD-q89VfCw21S6SJxWlW3sGBDxtPNZox7rA-Ubozf_Sq-u82aoETMRpKwL7hXQedDziCIK2GVpJmALU18YVgxzoej1eCMLtEgL6nD3FUoCX-7jRWky8mSLYRXEkwbm8RQLGBTB_NhEbBhGFHNFxzAmLPLzHfKsYD4pYF_BrLoacNPWXdaGiTuzDcBUYYnoIXLhxacLL3DVygjj_je_c-HGss-cxojSQTFB2kfKwzv5Xg7mdIHhBeG2WT-KodPabPDtwrfWo5lco9BdTSjvezV-o9A_WwyCWxHQAQktrqOXm8viXNGbW1FHwHOlb9A6J7X9vd90hj4z9IUhnE7sAYjVW0ns3SVib5sWjdyFb6yOVdAw85Qh70LI5ORVbKEDBQiHAZDKbcvH9_n0rjRSo1WUPGCOxIhtHp8fx1HKt10suPvY3Z10x-TkvrN2zLGwQ3-q1dBDXsxE7s6RtZWDv539ab3tcpyaVNMpb0iKo_FyEH2KHcehHkYKgeFL8STZnYRwiXxracozFz8Ef74-5UE0QMd3zKKcYv-j-Jpdx4Clbnu90OfEjY8DAojkmDaoUXJtR2B_f2bHrWyZnrf3xKS1jl_JF2LGKfpZBzHSWZH1K-Do" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26b5a279ca.mp4?token=CKQl4-SVgc0OfORaPijKQ4hu3n6FW5IvSQR9G2io0pb4bluL17pdXq-MLlSoXJD-q89VfCw21S6SJxWlW3sGBDxtPNZox7rA-Ubozf_Sq-u82aoETMRpKwL7hXQedDziCIK2GVpJmALU18YVgxzoej1eCMLtEgL6nD3FUoCX-7jRWky8mSLYRXEkwbm8RQLGBTB_NhEbBhGFHNFxzAmLPLzHfKsYD4pYF_BrLoacNPWXdaGiTuzDcBUYYnoIXLhxacLL3DVygjj_je_c-HGss-cxojSQTFB2kfKwzv5Xg7mdIHhBeG2WT-KodPabPDtwrfWo5lco9BdTSjvezV-o9A_WwyCWxHQAQktrqOXm8viXNGbW1FHwHOlb9A6J7X9vd90hj4z9IUhnE7sAYjVW0ns3SVib5sWjdyFb6yOVdAw85Qh70LI5ORVbKEDBQiHAZDKbcvH9_n0rjRSo1WUPGCOxIhtHp8fx1HKt10suPvY3Z10x-TkvrN2zLGwQ3-q1dBDXsxE7s6RtZWDv539ab3tcpyaVNMpb0iKo_FyEH2KHcehHkYKgeFL8STZnYRwiXxracozFz8Ef74-5UE0QMd3zKKcYv-j-Jpdx4Clbnu90OfEjY8DAojkmDaoUXJtR2B_f2bHrWyZnrf3xKS1jl_JF2LGKfpZBzHSWZH1K-Do" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عهدنامۀ مردم با رهبر شهید در مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666754" target="_blank">📅 07:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666753">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59c7afbeb8.mp4?token=hPtCZ5v2CGrRpmfliwiXz4lXojrjLfAjP0vz4fDEQZ7smvozFXbIk3ufkQl2YDTyZBE2z5cp6wCwZlhc-PeNIrDZeVPwOgT-l2xYEE4H1nygNLB7G459XbRFaNXMQJildw9yhGRafpxhOAMDVAYejoWU4Yr3a0j9ognhabjymYb-YMYYANWiPAew9r8ZmZ-rccKM6uUHyqm8IiY40O3vwpsFimAHEqsVMcByHn4J6pLUbmoJS7cw0YUQLxRBdbo387kd3ECOkZkjPuepjD0B021T5OXQqS5e7HNAHExA4pxXonC1d9ua_fJCBAb_GBlnZ5OdKdI3y7F6slkYJzl9NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59c7afbeb8.mp4?token=hPtCZ5v2CGrRpmfliwiXz4lXojrjLfAjP0vz4fDEQZ7smvozFXbIk3ufkQl2YDTyZBE2z5cp6wCwZlhc-PeNIrDZeVPwOgT-l2xYEE4H1nygNLB7G459XbRFaNXMQJildw9yhGRafpxhOAMDVAYejoWU4Yr3a0j9ognhabjymYb-YMYYANWiPAew9r8ZmZ-rccKM6uUHyqm8IiY40O3vwpsFimAHEqsVMcByHn4J6pLUbmoJS7cw0YUQLxRBdbo387kd3ECOkZkjPuepjD0B021T5OXQqS5e7HNAHExA4pxXonC1d9ua_fJCBAb_GBlnZ5OdKdI3y7F6slkYJzl9NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یمنی‌ها با فریاد الموت اسرائیل وارد مصلی شدند
🔹
دقایقی پیش گروهی از یمنی‌ها با فریادهای «الموت اسرائیل» وارد صحن اصلی مصلی تهران شدند تا در مراسم وداع با پیکر رهبر شهید ایران شرکت کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666753" target="_blank">📅 07:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666752">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/797d09ecaa.mp4?token=uUicUKvau5E2P9xwxEyfVi_gBU_-K58JEwXOmotCeampmtG47jECPitzY35jcms8_JpN8jDCTiCd6M4kmqqNIMqqiTXLgj-9ZaamPPVkG_6L8quwbjvQdKs2W6jVnitp8s_LlzFuM6CWmbYdoozDat9fw3QK2qUmqRgNE_1to2_vLC3MMSKzcGGrF0aGlnFTqH9yDF4n9DTo-pctRGIZ14oZCvDnxpaun-xK2Eh8nZRLkckjal3YgGYg_I0j1EzaNR3Mirxt6HL6iDDkphwtfoFbY__zjF1PXJzidLVSenHZBN1P2Sg8rBY-aVCyuBrVS1PAG4NLEZ_ubI13E0tUhJ5wY4wKGtLYMjzmSw_cWok2jD8EtsAlv9hhz6NLSSUXCz8mUDu03qUVGDptoFGsvRqQ4lIuWIm-BdkpCVg61aXrqfZdvg5R3I3X5tZnHrudz_HW7pWb3lSjR6vMsmbNBnxWOuULAMUsrXqwCbhwH9hBqKezb63WwXmOeGilYCPXUp6DlOp8afU-qpsVIrD7KYRh4bHhxIPDhvEUE60ZlP3AK5TyP65ZFMrJ8_nS9J_XO5iw8pt1TyBOq83Dwy7DMNaz8KBJdM7F2BGlAgfHa7V22bwIobn8sXJzWDkWRITJb7QF1uSC1BXXnoot0tfhioCTlu20UzlyrNMX79WRPCM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/797d09ecaa.mp4?token=uUicUKvau5E2P9xwxEyfVi_gBU_-K58JEwXOmotCeampmtG47jECPitzY35jcms8_JpN8jDCTiCd6M4kmqqNIMqqiTXLgj-9ZaamPPVkG_6L8quwbjvQdKs2W6jVnitp8s_LlzFuM6CWmbYdoozDat9fw3QK2qUmqRgNE_1to2_vLC3MMSKzcGGrF0aGlnFTqH9yDF4n9DTo-pctRGIZ14oZCvDnxpaun-xK2Eh8nZRLkckjal3YgGYg_I0j1EzaNR3Mirxt6HL6iDDkphwtfoFbY__zjF1PXJzidLVSenHZBN1P2Sg8rBY-aVCyuBrVS1PAG4NLEZ_ubI13E0tUhJ5wY4wKGtLYMjzmSw_cWok2jD8EtsAlv9hhz6NLSSUXCz8mUDu03qUVGDptoFGsvRqQ4lIuWIm-BdkpCVg61aXrqfZdvg5R3I3X5tZnHrudz_HW7pWb3lSjR6vMsmbNBnxWOuULAMUsrXqwCbhwH9hBqKezb63WwXmOeGilYCPXUp6DlOp8afU-qpsVIrD7KYRh4bHhxIPDhvEUE60ZlP3AK5TyP65ZFMrJ8_nS9J_XO5iw8pt1TyBOq83Dwy7DMNaz8KBJdM7F2BGlAgfHa7V22bwIobn8sXJzWDkWRITJb7QF1uSC1BXXnoot0tfhioCTlu20UzlyrNMX79WRPCM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیان احکام مربوط به نماز میت در مصلای امام خمینی(ره)، ساعاتی پیش از اقامه نماز بر پیکر رهبر شهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666752" target="_blank">📅 07:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666751">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36694e80fb.mp4?token=eojOVcw5_wUmu2bnXab92fBqwK1naC9bYfC1sApvIg-pi5Bdi-Hzl3AnxZuEAMXch4pfmHTnBUJUdz2Yy5Khd13X-in-gWAZu8MVd9rLGetH69i3I4YnKQOhjXst2K6wIW5WDr5sXYcI1v8gPPjqWn6eMhfstvfMYU4rf3D9dk0zNZKxuN9hu9lOQWtquCgGLEUHGhdSzeg_berN5BBpMidWm1fnzb4y-6Ze57kzywxm0NGAPWQnY4nvfY9zBgUR8o5bvuUaUzMqIB7I1HOE2M76gdAMAbPmkuve1Kpbf7-75qB3IPZtZw2KEhvleDZyYMKJ4n8Ncq4FYfLZsXl-pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36694e80fb.mp4?token=eojOVcw5_wUmu2bnXab92fBqwK1naC9bYfC1sApvIg-pi5Bdi-Hzl3AnxZuEAMXch4pfmHTnBUJUdz2Yy5Khd13X-in-gWAZu8MVd9rLGetH69i3I4YnKQOhjXst2K6wIW5WDr5sXYcI1v8gPPjqWn6eMhfstvfMYU4rf3D9dk0zNZKxuN9hu9lOQWtquCgGLEUHGhdSzeg_berN5BBpMidWm1fnzb4y-6Ze57kzywxm0NGAPWQnY4nvfY9zBgUR8o5bvuUaUzMqIB7I1HOE2M76gdAMAbPmkuve1Kpbf7-75qB3IPZtZw2KEhvleDZyYMKJ4n8Ncq4FYfLZsXl-pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردم در مصلی با سلام نظامی سرود ملی را خواندند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666751" target="_blank">📅 07:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666750">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe180104b.mp4?token=YH3sRr1PYb7IN8I_8Zxz0tBofjoMdL9e1BSwi-Udf8vfpm-g9kkA16vyGDHv-PEbaFWYt2gSO8KUvC5NSgc--ACrpsaX5EYuA3P7jyTzTdqlJuOw4XJmLIDwJ-1ZRqIqkgzRCjl6FfcFURkLQn6jUq-8Zze2rh5qZazz7Zj5Jzu8wWkYiRv7IDCN1M8W2QdImA-eI9XjUrwSW0f1rA6kjy9WuqqXmzGoktIMwkwah9ytTA08E3ySLowKLzuWc54gsCbN-3eAjn2YdExGu30OKUszA11QYq1RTxvIs9fXHCSCu2b10hhkWPiW8a4KF6yeJc_Z4fH4CxnosMdCkxRSWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe180104b.mp4?token=YH3sRr1PYb7IN8I_8Zxz0tBofjoMdL9e1BSwi-Udf8vfpm-g9kkA16vyGDHv-PEbaFWYt2gSO8KUvC5NSgc--ACrpsaX5EYuA3P7jyTzTdqlJuOw4XJmLIDwJ-1ZRqIqkgzRCjl6FfcFURkLQn6jUq-8Zze2rh5qZazz7Zj5Jzu8wWkYiRv7IDCN1M8W2QdImA-eI9XjUrwSW0f1rA6kjy9WuqqXmzGoktIMwkwah9ytTA08E3ySLowKLzuWc54gsCbN-3eAjn2YdExGu30OKUszA11QYq1RTxvIs9fXHCSCu2b10hhkWPiW8a4KF6yeJc_Z4fH4CxnosMdCkxRSWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر چه در دل ما داغ آتشینت هست
هزار شکر که امروز جانشینت هست
🔹
لحظاتی از شعرخوانی محمد رسولی در مصلا، ساعتی پیش از اقامه نماز بر پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666750" target="_blank">📅 07:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666749">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aada24811.mp4?token=KFslWchhmJ3Pzc1E_VWTN2-j0adUnV2VLD8B2TWh7R45xbNMcWzZ-hORtaJnbnxnJe1D-UNuR2hefshpF88HVcaSJlBOTTqmrl5xLaoBAMNLZ3XbibA_fDZzaFEzDQEhg8IytuRBVSy8zE0qw_HpNxQ2D_qRH7A1-riZ8KXfYPW6MikXFVcgvbnL6iG4mkMvCWFVbg-17sMF9E41BKkBiflZ-07QAG1S1tINf0Evp09nLMxjvLiyYcI6riuUZ5RKZUerU3b9OA5XazKgnJFES-_A2eWgMjWPdCFYIjrxLc0dJVrRVX6FKvBi5JhD9OdRgBRakwZDIpk2-hZf3lw6bDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aada24811.mp4?token=KFslWchhmJ3Pzc1E_VWTN2-j0adUnV2VLD8B2TWh7R45xbNMcWzZ-hORtaJnbnxnJe1D-UNuR2hefshpF88HVcaSJlBOTTqmrl5xLaoBAMNLZ3XbibA_fDZzaFEzDQEhg8IytuRBVSy8zE0qw_HpNxQ2D_qRH7A1-riZ8KXfYPW6MikXFVcgvbnL6iG4mkMvCWFVbg-17sMF9E41BKkBiflZ-07QAG1S1tINf0Evp09nLMxjvLiyYcI6riuUZ5RKZUerU3b9OA5XazKgnJFES-_A2eWgMjWPdCFYIjrxLc0dJVrRVX6FKvBi5JhD9OdRgBRakwZDIpk2-hZf3lw6bDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عادت ما این بود که در نمازهای مصلی، پشت سرتان صف ببندیم، نه روبرویتان؛ ای مقتدای شهید
🥀
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666749" target="_blank">📅 07:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666747">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd41cf86cc.mp4?token=OukrIKMe0rzZSW1yFol5SpxcsyeQspDRTQ73-EkCORd2Jp7Sj5sF0SDAQvjKyOxxWLxLgShEYDhfPRx3WmRArT76yYGFlKvqiEDoa0k4EVKsJfdIb8x5-zwpFICcZj4efE183GNrH1zI8UmYjogWgPPPJwyY-sfiuHhVU90zvKa8V9oRqiA62tbeTyMxTsD3TLMjoO9NbHM70EacFT3AHOUtHYyY76svTXaUJjFocchiok8DMuYndjyWE4eUqENwI49iui8NhL9CybEab3GZ8Jv_x5992G66X-zUuoRZICo7UwWPSX7iOebIGXuz3BF64qWZKdKLR-eCfekHjjP1JA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd41cf86cc.mp4?token=OukrIKMe0rzZSW1yFol5SpxcsyeQspDRTQ73-EkCORd2Jp7Sj5sF0SDAQvjKyOxxWLxLgShEYDhfPRx3WmRArT76yYGFlKvqiEDoa0k4EVKsJfdIb8x5-zwpFICcZj4efE183GNrH1zI8UmYjogWgPPPJwyY-sfiuHhVU90zvKa8V9oRqiA62tbeTyMxTsD3TLMjoO9NbHM70EacFT3AHOUtHYyY76svTXaUJjFocchiok8DMuYndjyWE4eUqENwI49iui8NhL9CybEab3GZ8Jv_x5992G66X-zUuoRZICo7UwWPSX7iOebIGXuz3BF64qWZKdKLR-eCfekHjjP1JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سگ جزیره کودک‌خوران چرا زنده است
از این پس جهان جای این نجاست نیست
جهان نگاه کند، تیغ انتقام اینجا است
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666747" target="_blank">📅 07:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666746">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keJS8lqiOxkCkt3HVDBmGkmH0RpGizMLY9cIVThWuEsUAazHrA8y5riaYB5lKzAp8EIAKuRuXGakFq8LxCraSpUsa1ReqvrJSQQNwMVhNGQ5fUktvmi6E9THIlXUO6Idk5rYVFDdrGjjEUTC7ZsiC_Oq-xBuyJdNnezV1GPkaQu1HyV_1cgiaC02he5GzbhhzAaWFQKb_xirUCyIIPWm5-nXAj6oix3AvPVPX6w_olYZUkwYdldNm16uc4BcS2euzNNtzx1I0uApgKiK7W27mzliyehMRLWinFuVPUB1jd7GW_akJpD0iYS2KHN5uo1-TPXQVLDHDsyoQo4W9SvdBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۱۴ تیر ماه
۲۰ محرم ۱۴۴۸
۵ جولای ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/666746" target="_blank">📅 07:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666745">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
درهای شرقی مصلای امام خمینی(ره) بسته شد
🔹
با توجه ازدحام جمعیت، درهای شرقی مصلای امام خمینی(ره) تهران بسته شده و زوار برای اتصال اقامۀ نماز بر پیکر امام شهید انقلاب اسلامی و خانوادۀ ایشان باید به درب‌های شمالی مراجعه کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/666745" target="_blank">📅 07:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666744">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fdf8c8e0f.mp4?token=IPXGoYWryVoAJ71n-EnigceJTtj9JqkfWXPIuZyKM5PejR-ILpUNFyokuUXE_J5SWQkGoh40v9WgsPDXALFeIrAjDphL0wqR1bbolGb26gZL5_dsMdLq_QFoZOVUwuz_zUoNNOdqxAP3Zda5cA76IxfbHH3zY5_7U8A-1m49-tNoddP80r0gkTgeWzJmCxjNDEukZ2AWLPet8JVSMJ7Xd9boddLNJzCLZUH-_3rMl1Mry8_ci5DGIJyRck-Sv3zF4t7gOCL1YK-iGqHqHoWR1mgsM_CgDwwx8YUMWOE6HGpzoIPx8laqV65bbFvyYgnzXW4WLmYXSKHG5HnPMpCqUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fdf8c8e0f.mp4?token=IPXGoYWryVoAJ71n-EnigceJTtj9JqkfWXPIuZyKM5PejR-ILpUNFyokuUXE_J5SWQkGoh40v9WgsPDXALFeIrAjDphL0wqR1bbolGb26gZL5_dsMdLq_QFoZOVUwuz_zUoNNOdqxAP3Zda5cA76IxfbHH3zY5_7U8A-1m49-tNoddP80r0gkTgeWzJmCxjNDEukZ2AWLPet8JVSMJ7Xd9boddLNJzCLZUH-_3rMl1Mry8_ci5DGIJyRck-Sv3zF4t7gOCL1YK-iGqHqHoWR1mgsM_CgDwwx8YUMWOE6HGpzoIPx8laqV65bbFvyYgnzXW4WLmYXSKHG5HnPMpCqUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار «حیدر حیدر» مردم عزادار، ساعتی پیش از اقامه نماز بر پیکر «آقای شهید ایران»
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/666744" target="_blank">📅 07:29 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
