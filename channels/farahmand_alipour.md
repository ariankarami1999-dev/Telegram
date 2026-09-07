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
<img src="https://cdn4.telesco.pe/file/myTIqbPJyGTcU4pBZ1YeTzrwCuKooL9Xi8IT73OQHqQovWZ5ttQKSvwOP6Z_vzAaWT4bD5QDfdfepMPct8ghDBdGLH-GVBAlScp4K5tRuH4FxVEUrZyZ9cELa5JlTjKiH3PBlN6Ku3f9W5gS4rhlX2FAE9GMjC7VG5lHEFkkUvknqg7zQNpLa_alo0TgVeaP-CG6WUFmzLmoZONCUsIeMIMnhQ5ZdvhZ71hw9CeFt8rUKGMiDghcGI25qnpiUc2HnBOrrZYH3KPtwtiqj5I1woXDK4A4DaPiqKDuxI8TOKrjJ0SDV5j-9PHxkCAmhXASRczTQvjNgpvey8Rp56zsFg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 14:07:21</div>
<hr>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Ho2z1GnbSvuD9NyoVs7kLecR3bymOZ8ePX4N06Ysl7ekh9ZcT70HmPVHQWMaCEv_ZPnEVsI5UueQoRbbFZYqxcAtmT3KYUNIS5WXOfyIUlGxgJWf3Pf39UmacNsEN7zW9CDWW4qQtijfEahtcq0mHv4ihKTWpArdvWiWiPLN18Fyd4B5rvoe_Y9XlVPAgURGgGYE2UlngnJTcpwIe77Wd-RKthS3qwCxJ_LG_uT6T_cmrPwpYxuWHHS3_nU0WLS2VnBjYn1QBF0ivF02__8LCstOenIBi59_a6MIdQdHlPVNq7T9w52mpKkDg00VmbwpuT2VvkcAf6SEzN7NN5qeeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Ho2z1GnbSvuD9NyoVs7kLecR3bymOZ8ePX4N06Ysl7ekh9ZcT70HmPVHQWMaCEv_ZPnEVsI5UueQoRbbFZYqxcAtmT3KYUNIS5WXOfyIUlGxgJWf3Pf39UmacNsEN7zW9CDWW4qQtijfEahtcq0mHv4ihKTWpArdvWiWiPLN18Fyd4B5rvoe_Y9XlVPAgURGgGYE2UlngnJTcpwIe77Wd-RKthS3qwCxJ_LG_uT6T_cmrPwpYxuWHHS3_nU0WLS2VnBjYn1QBF0ivF02__8LCstOenIBi59_a6MIdQdHlPVNq7T9w52mpKkDg00VmbwpuT2VvkcAf6SEzN7NN5qeeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hf3duywbe4OA2wuOP_lLtgEzjgUeP_ELAfHYaeZ84YKHB2v859H7YGQ4WvxLjeuX6u5yhLrPOCGRWJ-FdMsgmH_zaqLj7cJZZPWiGUXrsKPda_OZKyxFEKs9G3yqN0ojPw3VAjgNJ6KmLUnPFLhBcNvxED5v_u4fUtNKB4zz7aZJTlzAgzOlb2eJswpN8HjvYkG4hTiOz6Sj3sZeYY6eWGOOPvrx-F7nnYyjTCetTmO6rkyNvIIswDrXNViUkuycLaNF4cIvmmgq-HyVVvAf_eUmrcXJdPWkPm9pb1_cFD6qoOdg99MzIkaz6C8AQ2nsEwlNBENlyBWItL9dFx0nWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uJjValImkDxm-veeAD2RE8kByE_9sKjhGJB1e4dLxUIUxTaj9ZVkSjcjHUcwqnQv9YmncHPDVHvIqwHMO9ysXWzgQG5YTp20LDFI1UedHyLifyUqr2yt1PUGba5H1FH-ODbQ_KS2q_ZGhaGHB9g3mUGvTxSHfEZsj8G8U7e7tqqi_xWb8c81RR76WPH9ByOMC2c8gB7BqmsXjqhW8yn7L5YAE40ieIdtF8XQOioflMVfBToG3jP_s6T59tmq0KVtHKx1QCuk2U84XKh2_WaUnB56Ibz2-wvYWnqhKHLLXwVVE19vZpJMb5HPoCS4YAo5di736vRj0Eea7CmW8r3zuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=TxrmNaSF6ug9lMAkZ6AJ_vj97cXe-zVZN4Wa_xHsb5ecpL6QPAPY3cJqat0O4TAtALbcrGd7DEIae_JqS5-JUTl6yryk9U051k1naUkjpelCThwjaCYRPcO86LptFWHoewu0CDk5Qhiadu3m3ssimfyXrZt0VgNIzZYw2wpUE8shxtumPtJaM9dJvYNjATjmW_j7YgZfFaAQT5czH-eJtC6SuyBKK-UCbyL5xIZx15oK1H6kziV774HYrFO7y-aLIMEypSbWEua0wEA1EZtowCetWYhd2YBIEvR6xAtQhTWKmVop7hFIUfoxLK9brqnYZ-1NNHhENDD-QzifS7GOzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=TxrmNaSF6ug9lMAkZ6AJ_vj97cXe-zVZN4Wa_xHsb5ecpL6QPAPY3cJqat0O4TAtALbcrGd7DEIae_JqS5-JUTl6yryk9U051k1naUkjpelCThwjaCYRPcO86LptFWHoewu0CDk5Qhiadu3m3ssimfyXrZt0VgNIzZYw2wpUE8shxtumPtJaM9dJvYNjATjmW_j7YgZfFaAQT5czH-eJtC6SuyBKK-UCbyL5xIZx15oK1H6kziV774HYrFO7y-aLIMEypSbWEua0wEA1EZtowCetWYhd2YBIEvR6xAtQhTWKmVop7hFIUfoxLK9brqnYZ-1NNHhENDD-QzifS7GOzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9Z8z0K5QN3YjOaLAH-wOmFnnV2RHoxH1kKFUKd21bk-ktwswrhkTbkhPaJoYbpabn2o6jtpH5iEWhiowsTzHzNyooDpoi7g7B53WyvfxXhc5OlvanTVLekSYlUPoTsJcxogMsfOB2a0AO3gFe3XaUP9-rlkphez3igr2RibWU5hHiPBq7aOJxs8sfoDD1e0ho6GB8pkKeVoB4CXvO336FWX-MycIT5gnP3bGO_QfkfuBbPe3dnJNd3l-6GnMGEYksYQXqe_U7HneSY8opPfYveXYv80vX8quL9YyNC1clpVhtDZV7dxyFnSjIgmEfq2Ww2dHM9pC80iPtlxwUJIEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcApaWyesX074CoP3lDbQVfJbSr0AUGukH_KCF1PegWPqAskkKHClkVigxWvbw8DXlZt_XjcjqGey2OZ8Ksr6cPXAD0WbS5atJrVE2mq33FvK6QEMSlk4Ggciw_qdHRL23hO3zRJLt4Gs3V-iE2kCtWBP0Qr5JtHf3evPDbsu-rv-561BViB3tbpUkdHoPpp2sqliuBeIq-fCgkOMM4NxQ9bCWzk3w1xoZjPq1Dus7C7AD-zpfd1ipyTjGpOZ-qph4Zdf4e2MMJUpAcB6nEI4i-OLsbE9S325lGNNo1LAPUFrhYlGN0HNPr0n-GXKjClVKp1ijin5KmZCBI8Ko0GEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDNswknBz4ZT67LImWh6wcADlsqSCqP-ljezuM6XZKShMhw45S-55Bzen-SAIjBfv0C6rnNxnOramk4ineH_nRb1iRmzh3YEadoEk4rOeXinEnO2bs4V3QuNMrnuiYybRGleuiq30khtUcdDPz2EdZajWaNE_LFT2NFyFB9cb1eDOGONUbruWjYFigrbLNyKbgmKRgk0d2BCIkgPz-LIgKwWUhJ7lfWXh8xyjsLJh9ahEnatJxTsswMLDhMwwJZy5RuxM8rC1JdxnTyHUVlExcPexSUaPQd59GQohCUaBguEV8JHPvwHnbGzoRsSleV4yyKzsY4Hs26jsQ4aqlezhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=Y9edIM2dWrv0AAEUkP7OJxxepFyJ4cCgfGFABX3cQoLsQcJ9OsFbGmhReSOor0uK67Sdm8gnvOnWS8tncbRPhgpP-5CGxIHeotSAMQEifYZzAsSUq2udycqPc-5WMXZ45Z3alJfC01-M9qvXPZTuzdmwJl7m_X4bnlKcCFE-o6K4Zk2fdJtHwvu_3gfx0Yw_0mxr3uC5Ca5qJAK08aGfSCrpL1zs1Nvqkc2iCCVwOTLgxKKNZWs9jE57mcNxeVGB2fXBu0IS3xIuWQmRvOVI5j7PHsKR78k7EB0L4jIQi-Y6YhUcv2diEBdklip-O2VtLQtnc0zAzVVKxfCoSdHEHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=Y9edIM2dWrv0AAEUkP7OJxxepFyJ4cCgfGFABX3cQoLsQcJ9OsFbGmhReSOor0uK67Sdm8gnvOnWS8tncbRPhgpP-5CGxIHeotSAMQEifYZzAsSUq2udycqPc-5WMXZ45Z3alJfC01-M9qvXPZTuzdmwJl7m_X4bnlKcCFE-o6K4Zk2fdJtHwvu_3gfx0Yw_0mxr3uC5Ca5qJAK08aGfSCrpL1zs1Nvqkc2iCCVwOTLgxKKNZWs9jE57mcNxeVGB2fXBu0IS3xIuWQmRvOVI5j7PHsKR78k7EB0L4jIQi-Y6YhUcv2diEBdklip-O2VtLQtnc0zAzVVKxfCoSdHEHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=EKa6epKDz5UJAcJ1H8DyhBxZYCxWSRJgC6DZakgs3FWcR0FNqX800n9NF38Xp-AmuNTtc_RzoxoBHvte0LcCAjE1QLr9TdXtB_c469hndTYKCNfo4QqjD_9iPKlZGyHPaL9z2_hOnMX27LLF8Q_yubl1WAlk9aDriJGTMWzABALXJfNHt2FoItJijyh-AiLkDpYcoWU-xVY7aedFgfarK_x56AKEUh680_Lj8nN0qH6HLjtH-7urr_ubCUKqIYyCvvQBOfLNT1hUxUY39fUynTmKDAOgPpifgOj1yrAMooXjDkaW-5luy53rTq17kub6Ls7yTqyHfx7kkWzB6CecjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=EKa6epKDz5UJAcJ1H8DyhBxZYCxWSRJgC6DZakgs3FWcR0FNqX800n9NF38Xp-AmuNTtc_RzoxoBHvte0LcCAjE1QLr9TdXtB_c469hndTYKCNfo4QqjD_9iPKlZGyHPaL9z2_hOnMX27LLF8Q_yubl1WAlk9aDriJGTMWzABALXJfNHt2FoItJijyh-AiLkDpYcoWU-xVY7aedFgfarK_x56AKEUh680_Lj8nN0qH6HLjtH-7urr_ubCUKqIYyCvvQBOfLNT1hUxUY39fUynTmKDAOgPpifgOj1yrAMooXjDkaW-5luy53rTq17kub6Ls7yTqyHfx7kkWzB6CecjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=JzwKTqWO3HcANkX-jZr8Mx5ozzPAcYPGWyPqbelxJkLejN_ffHGDiQUM-uO_juLWYTNyAeAH5K7JhZubkOKsCeUYYyHiPeqrKlXvh1ITy7HBmeK0A4sRBrXrv_btAqgex0z_yjrS7Neq5576mgSPA111NzpSvIXz18XLRIKlKp1bpx5kiRDyuzGO6xOzCLlg1eeQkMwTxM2ubRWKqRXmRX84TStxkT62srWsCmsX6_KMKUOUTHzjio646PTDSyJJLhsFKHtMV3OsDCpGZSUPZVxvWnJeuuosXx8XXvHQGYFUZA8OFXjTBxWr7rE6pF77xLcKH3khYPo7nfc5CeX10osIWl2WCBiJgEURMd9rgDCQ3JjiU6q4sUxAPmE_LwV8aepYcJrZYNKRGur1rmyHLrlzeH7gGa2-ZWP_h9hjNI42TJZ-md1ddYQumyctUINu6Uxq6p-ENjv0WeBo2jryooeDApyVSd1wymR3zIE4KJfsrjx76Qgz-eetxkFXXnlYkwUAWKJw3seXA6e7j5kTlYPMgB_dscaHeILLof8CqqMAWRUZukfH3UciakyXP09r3tQyUMeUc_wmvoFbLbHvKYujTqwCR7FdVyD77QpTOEwNQsyIRSUml81ieGV2-WECnbXAQq5cIOgDDDWMRF7epcVFMXet_H9t_CwsTBd3g9U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=JzwKTqWO3HcANkX-jZr8Mx5ozzPAcYPGWyPqbelxJkLejN_ffHGDiQUM-uO_juLWYTNyAeAH5K7JhZubkOKsCeUYYyHiPeqrKlXvh1ITy7HBmeK0A4sRBrXrv_btAqgex0z_yjrS7Neq5576mgSPA111NzpSvIXz18XLRIKlKp1bpx5kiRDyuzGO6xOzCLlg1eeQkMwTxM2ubRWKqRXmRX84TStxkT62srWsCmsX6_KMKUOUTHzjio646PTDSyJJLhsFKHtMV3OsDCpGZSUPZVxvWnJeuuosXx8XXvHQGYFUZA8OFXjTBxWr7rE6pF77xLcKH3khYPo7nfc5CeX10osIWl2WCBiJgEURMd9rgDCQ3JjiU6q4sUxAPmE_LwV8aepYcJrZYNKRGur1rmyHLrlzeH7gGa2-ZWP_h9hjNI42TJZ-md1ddYQumyctUINu6Uxq6p-ENjv0WeBo2jryooeDApyVSd1wymR3zIE4KJfsrjx76Qgz-eetxkFXXnlYkwUAWKJw3seXA6e7j5kTlYPMgB_dscaHeILLof8CqqMAWRUZukfH3UciakyXP09r3tQyUMeUc_wmvoFbLbHvKYujTqwCR7FdVyD77QpTOEwNQsyIRSUml81ieGV2-WECnbXAQq5cIOgDDDWMRF7epcVFMXet_H9t_CwsTBd3g9U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=N-NILdyKEyXNSYvSFx3rFgVsoXruAkjn_yBx5GQK-cjK3kCWuz_aaoEjrxgYypiM0sYo3wzjEyroyr_wZ5CrMY1gzAsb5-yE3IKG-pRKk5RPRYqM6s7GwhfhBgfrh9qeKEU3QH0UBXth0G99ZbbZvcCHED0yeHe3kajyZpAA1x6AWiPpWZbfDuI5e6gbJ5wjrLepknTEqhsOuPrPGyAjR-8JxAzFAcrk6OlzlXKhFN82Q24w69wwCXxp6WX6zfhsJg1xOyN9Q3WQR376iSo7pu886EL8V6sUEMWaMQhC4L7g8JacQbcnMvL9onyRw1rLezglV84Q7RaCrWY0mK3WNlHbmE737_84nb0FrF-2XT7pLHgpnVsRv9KKOn3hVOuLrLcWad23XkixEirNpF2Ewp-JUHwB8xW8gWpNZ96OcwnOHZ0mV3hzxP0_d1TDxaE02LowdK-xtu10Y-Hw-hwnqCdVdB7Tvds-LhWm5ZXbqQ02gWG_uPK4ll_-yewtBiSHcqGH8XceDIh7lkrJilQI9xpjyPRuhbbLECR_rCZMLYrsnCjZMa0LtJfvrIdL2LfLd4DT9CNYugpO6bTBWsFGKihPLvv8rUvPMUoJQRMtj1ILhIAnnwL7p5dP2dbbKtCIolTrRQ1PhMJq6oDJhVn3_tkL-QLjDu-Et1zulxfRLFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=N-NILdyKEyXNSYvSFx3rFgVsoXruAkjn_yBx5GQK-cjK3kCWuz_aaoEjrxgYypiM0sYo3wzjEyroyr_wZ5CrMY1gzAsb5-yE3IKG-pRKk5RPRYqM6s7GwhfhBgfrh9qeKEU3QH0UBXth0G99ZbbZvcCHED0yeHe3kajyZpAA1x6AWiPpWZbfDuI5e6gbJ5wjrLepknTEqhsOuPrPGyAjR-8JxAzFAcrk6OlzlXKhFN82Q24w69wwCXxp6WX6zfhsJg1xOyN9Q3WQR376iSo7pu886EL8V6sUEMWaMQhC4L7g8JacQbcnMvL9onyRw1rLezglV84Q7RaCrWY0mK3WNlHbmE737_84nb0FrF-2XT7pLHgpnVsRv9KKOn3hVOuLrLcWad23XkixEirNpF2Ewp-JUHwB8xW8gWpNZ96OcwnOHZ0mV3hzxP0_d1TDxaE02LowdK-xtu10Y-Hw-hwnqCdVdB7Tvds-LhWm5ZXbqQ02gWG_uPK4ll_-yewtBiSHcqGH8XceDIh7lkrJilQI9xpjyPRuhbbLECR_rCZMLYrsnCjZMa0LtJfvrIdL2LfLd4DT9CNYugpO6bTBWsFGKihPLvv8rUvPMUoJQRMtj1ILhIAnnwL7p5dP2dbbKtCIolTrRQ1PhMJq6oDJhVn3_tkL-QLjDu-Et1zulxfRLFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=MnrpiL5WvGjfvfl2fV29F9SanSukHki3LYDl7mKPcgVdu0_k_N4Edd4Hl3Af1cmZgKfajtI5-zf_vPGmgF9g4PzGuAHNJLs9qMFPRKdD28IDrjQHPGUMVB4b0k2AogDElx5MwUKEjdcMql5yEnXnstDTnv61wxU8Bb887upWKTEvtqvPNtJX4DP83JAo29elx5Zj-JCaY1w0iU8vCAUoWUh4wrDZLUO9n9Zyx8mGX2G4_-SNqhh9DNew9IJ1n9n_OmujYCMgEakBxORFKfTuEwv6Uwu5K1jgkSw_e357JoqpKNGJJTjYjO7Kwm6iWPZ1-i4-GIedIqh1myZ5CxUhEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=MnrpiL5WvGjfvfl2fV29F9SanSukHki3LYDl7mKPcgVdu0_k_N4Edd4Hl3Af1cmZgKfajtI5-zf_vPGmgF9g4PzGuAHNJLs9qMFPRKdD28IDrjQHPGUMVB4b0k2AogDElx5MwUKEjdcMql5yEnXnstDTnv61wxU8Bb887upWKTEvtqvPNtJX4DP83JAo29elx5Zj-JCaY1w0iU8vCAUoWUh4wrDZLUO9n9Zyx8mGX2G4_-SNqhh9DNew9IJ1n9n_OmujYCMgEakBxORFKfTuEwv6Uwu5K1jgkSw_e357JoqpKNGJJTjYjO7Kwm6iWPZ1-i4-GIedIqh1myZ5CxUhEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAWSv0TbJVAS3ZbPhjDzTqgCYna6_5OpObGhDB80OXhfKOn7LVisyvQl3SPYmnT3J93mZ0naMgAuVSTfuG1pGPu6IZNLJ4e9ZJaPT1X6O4oqJySmaSZaQOeQkn84mvS-h32g27EKvRkVQNit7HUS8BHZpAJNmoSaRdI8zANz9WZwV3qdeTClRVy7C-zs0HqvF_HS83PcHHJcwKxgGk33KHKAlXNc-4N7AABJk4FM6n0m_fIATVTybFRABkqAX7XA3nG_6bMc7ySRAgbSgGhAmJFppfd3nLHCYXuswVthwfh51kHaWnYDJmudHWS0_FfAYU4Qqh3aKf2opeOsubW78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=lWyk2RJKWJ_v5n2obwkeKtsRJ3UkpaX0SojjMD7CKuMDD6_hdxcKKD4kCDkq6xb_LWh-yO4D0Trr5YJkW6pKBKLRtmRndDh7qc8yJqJGl4UDoJ-QOqiyyEgkskiAdq_Xe5im0cTzKZDHGkFpw4Wud8kpIdPD3b3HEbpY-Jp3yNC7J8fYYgwpvPu3LW48-2PiGgbLZDDMjEtIw0LL4AXD6vtRcm_xy9osvhG9Wlc225qkgsXVWm2369vt2wbDisMCtylMsFkixT5_dg5QIu6eGwfeN-9U8SToO8Z1qv3kEGEUnt_Z7GxP6uV0iTOq9qmZ-tdFjFx7Cc7-LPhAm3UlwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=lWyk2RJKWJ_v5n2obwkeKtsRJ3UkpaX0SojjMD7CKuMDD6_hdxcKKD4kCDkq6xb_LWh-yO4D0Trr5YJkW6pKBKLRtmRndDh7qc8yJqJGl4UDoJ-QOqiyyEgkskiAdq_Xe5im0cTzKZDHGkFpw4Wud8kpIdPD3b3HEbpY-Jp3yNC7J8fYYgwpvPu3LW48-2PiGgbLZDDMjEtIw0LL4AXD6vtRcm_xy9osvhG9Wlc225qkgsXVWm2369vt2wbDisMCtylMsFkixT5_dg5QIu6eGwfeN-9U8SToO8Z1qv3kEGEUnt_Z7GxP6uV0iTOq9qmZ-tdFjFx7Cc7-LPhAm3UlwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=RKEOC-9tvxzKJFXIaywQLK3PxM6fvokArgcYvC79BndX0VNrzSgXV85PZ3H0Q4-6Qwn3fwBuXRIOytxMZKYi1A2X-7vKZ7UDLugNm6jNXFBovp56STUYA6JINWGTMcucxRrzw7RSLt-N7ggNAipQyV3dfBgOKVmDm3l0LK-BNVRIw5GUe9na5hkgOC0hWd_yG9R4qdB9t5ZlZAovsdETcDTJHxWFv0gwPyQxgDhga7c0aTsZBvJsqEna4SwPqdM5shb7UqSHaSQd-JRizLUDqY7tQXO8lJZE_fWaP4iwQay0wVyiCpR8Xmtn0cQduOmOFxRb1QqNEFdNXru3_fgLRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=RKEOC-9tvxzKJFXIaywQLK3PxM6fvokArgcYvC79BndX0VNrzSgXV85PZ3H0Q4-6Qwn3fwBuXRIOytxMZKYi1A2X-7vKZ7UDLugNm6jNXFBovp56STUYA6JINWGTMcucxRrzw7RSLt-N7ggNAipQyV3dfBgOKVmDm3l0LK-BNVRIw5GUe9na5hkgOC0hWd_yG9R4qdB9t5ZlZAovsdETcDTJHxWFv0gwPyQxgDhga7c0aTsZBvJsqEna4SwPqdM5shb7UqSHaSQd-JRizLUDqY7tQXO8lJZE_fWaP4iwQay0wVyiCpR8Xmtn0cQduOmOFxRb1QqNEFdNXru3_fgLRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYVT7F48U_RVyPeZcQGCTOu2kdb1_UCYdlWvXx2pd01bgx-krRf1JZjzZNfmohz0U7c6ZdFdPMGbA_rYTw_pNPoGVXyO62K58pFIYaFw5YNJAX-wtWFpH8iyh0BM1d7w-E4F1sYy9IwKFTRwKIM3YJXNONMLlgiHkChUmvyRRVuG6_Bedp196lNMi8GFlUdTV-Xy8D5l_1s_z8uIOkF2ziaBI0mCa7JG8J_AHHpFWDT0e8k4P81SQwFH1eclkursF8l37foP0weFQ5Lg8ww2OMOXzhBg35d-KZ95OfQhjFg0wmAXCCJdn3LQquHtgMdHWCnvO8HfIJ4TGpDJ_fcoRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ma_bR0k7D5nmYiWzpxsLhifa2OvmDjv4SNhbmAp6lm-LhwxbsGgsRmZUZxno7zD6wzfsBv6vGCn0fUdpyi63TmI7Okmk1TEn4NFyEOXhG5Uiah2aDEJ1xJOEvJkV2M_p9ZhXjnnySs8eJtg3KFtj5csDJWDA_6aQyKqWB3GNG6yGn0__qy43YV-prvMXq8CshmbkjFdCzjsxczZMtiA43a23Il0WDaHQMM7GOhvNcwp3uMzgOkT_BiVz-46kMQqUDQWPHVwpbBpUq3-_gsEXjkpAjlfpNp8o-AVPaNv81EUQ1r1DFk3Rw2pfOvwaCg5ayLhR6x5i6yNcKlctuN0jwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUzTQwcCEav8-IcgTsXD8dOSstS4Uvkqv69-_uEceqWHdw1fY4WVgUAcJl9yifH0iPDv9ARqVZebzoyUaDQw54gNfkhSrsKtTibWEfgM13BND5mHfJAh3h4r-mhvhYCODj7uJ25k1lsr975hKpbZenXugt3Zc0TSKTkf728ZT43YlX2-7NQ3SiK2Cygu1DWjDxiMHIbzSZUrZ6zInip5vMgNAFCVvb1EbeOB3bvpiiZu8VsvBrr7fUYy5b_GgTvgCA0tB9WVN4Pz3v3G2naFwDUBIaY8DCvF7znzzM8SU5q1enoNyUdpjO8UTWNbB5pWilo2mdK80Z9xLjpRuJtNuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXtqUrmI4sRfRHg2FVgmrccuWWc1Z8ERc049bBtV-QoKhNlLxxisgvKePwFLhqJH88vbEZtrrd9xijhW2ZmKNxq-ahQ0lMBxJlc0E4_A3AUHsFWCOLSsblALhXNF5-36J0CcTgGQARZNA-y_UAZ7UxNkcKHkIWaVAoQGQoZ2KU5hdwL5SYhBEXJVpVqofpRDTcMR5oSX6N5rJGtoSvIYoHQccRtxjJafj7wmTNnZq9cQa5LdKq-7x9UreaqhtS18D9AgmjpsYxIfc575xDb1P7ZY0ulh6GF0XA7s9y7vbFrLB_oaJWwjGlCnnMn2g_ht0QgY6nRem31ebB6GKsNvlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6_iTKTd6WMs1jik6V_jbHVgT834V9OEagF9lbqlJI9SbSrBbwNtpfbJrHV48dK57kql8j2Ugt9wdE3BT8xFmJA6LF7ZxELUQlV-MOpQTvvFz7s2XwmXYF8UtCpTnmgmUZ-UvKdeEq5JXjTa9k2kRtPr3nn6NsvQIzh_Q41Ei5KO7R9r51k5U7hJc7KyQhykC1WwHJkGhJUKDKJFhUL1_7CsYaJ6PX1_lwtLvZklG0JiEnaxt7mYAbKpGj_dDWa3sC_-j89t-9A58ftBRWNRAtzEvWYopJfowAo6qjUFfCuaNR9hzzww68hAX1gQCOIsKvnQiegJt-y9g2Hfnqbxjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEAhfmPJkBDeeBv93KElVgtvXtV_caLR9-3pjostfuVaz0NnhFPZKwnmDIgu1AlsoQXZzcLLKeLdoX8u4sQxBCpBuK9y14FRnPXaDc2LRPrKO04gsW4QF91wwJP0zFdHQ9ajgTim_RZl5coGa96nLC_hwlt4AORMSzoWUD1A7ihMkelgzskst0KTK9HXUe_zwJiedUdE0U7udNKB06zFt5ZBh_xKNZRKUQs8v72mvoZjgY5LkvFAzjU1vrAo4ibIe4gKx_INFNuYl-3l5-WkPxf9cHtaFQQliIcf0GEx8Idm_c5-0PFxubhRXfppGumZJPZgaiV2KFc6kSVHT3aIYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gt-wY2odKReJU4Uuig5469ud7B1quupm50rvAkzW2lEiNhGzT61zvZB2BX7cuy7EoDaRpcvY3Jp8jZh1TGpUKxhSRSg32lvBtH3ym6SM6_vn3C_V3tRmwmJK6rD96T5Y51IUkH3h8lTzcwyiSKkHLRXOvGxwod7yGWqdiH7DgkOImVqiWCMh8D1b6azal0x2tgsv2NsDR5PMv0_vl_G0ed03EhgkE8JABeUS6ldFSiTbEkjoMZfJ7izXwfqU0C1OEC8H7yeP4kBlfM9A8aM-ji_Qd4XekjP50iJO1fj3p7MSCPMlfq4mr2TB4hXZyQpQe-dqRsQ8VYpqI-1F5oMQjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c_ha9dsUVuC2cmXENDZbtr7oT7EGKhEDQ5xJhLRjeP90lVVk5Cw6sshaVBhjWB3JosFms5dzz9IDomTu64QmolfEqRE7xFipzG_cLkTNLIslVscXhEziWFS0TIztEasCPo3CTrTwSFL7zWDDfJD-OzusGhwVORFBzNWE9D9rSQ08cl5QrK8Bo-CJMTBV6h29aEOg0ablihPW6KQYklHMKQ3xam-CFRBn8q3HeShoIFbXq75N-FUBDJgMgHSlTPmPxU-Q4NMg2aoQZdBUfb8j8BZNTNy_oWqkT3nwa38UDb_KU1foeFakY8Ku-KaZl8HHpqj9I1DzRw8wDrX84mAg1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujzAX1rQu6LHnlfl4irfEfw31WFwiAy_Hij9G6A6sewjsOpbu2SMmPBSnok6Z0Qe4FqetojY2c4a6qEZSUXSnXEEzxc5qGE0E_MK1fp4mPjfDzgu4J_H5Ilm8_Y9D9CaklxD7hujbHo-ohqQRqeLzGzwZuQvWatR9KACXyDgMEFhmfzzPatZCe9zJ4H8rPRH38ZecGbijoQ6wruIBntXCBZYoX0K7yCGl-9P7Zow465o4yntuTYs_PGpHTWmn8cAUG_dDc0weOfj8M99j5GVW63TUbAbVp6WBFGuSvgDhbGvnAperX93UvstAK4YSB7mYz1mi9eln3fmzjZbaFe1YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gn6aC50elTVmhkdvEtjCdXkragmo965Q-Ui_qUmzEBwy-PxYHYtK_KhdOddWPo9Bp-d1TxHN-ogQmo2eFyq3LGF-CGAqU2F-lt-aZgsRWJWnc7qCWwHSKKz_S-017MD9uLxXqL129hT694jDPWvT1W8oTTvs3mtmV_oS0COZHQXwVPUHVloAchtX0W-E7QAm3JfS6A9O40ZXGerI0M48mTaWCryOfFqzV4Rk3ej4gMFtvE7q3eIldOiIAkTKHIO0yVSmcDvFb1oWm32jUH_KfT7zxKFb5mW2rpVISWA7orvs57kD9TTs-wW3bN_5TvqWeAnWstoLtJPMb_FrZXTt1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=FjjZTAlWMTEGhwVTK4svH0-Nk8pk4iUcWqmgd4nz3B8hqXjzze5X7DqMAteMPAycWWwQekLYhQUXN3Fjm-9OVJR7P1VQVNkhgOirt9f3gKz9d6h9vZbX2gbUsuCSCrEtaPqpcQCXDRPE99VZzzGBXj-T2LEGo5HmOd1JnXaQ4XQIlDevHlv6fAPxJwjskDy8UpR26P76vXYneLXqYld1Iyd8BuLEPrc3JYC0MKRKcIe33l52IS28DKpRE9i-w8iwe2gwVL6YFhRpp34qM0TKv9a994Aa-ZOINrSSDFVPRALBVBNwfPd4HJuSUFaqk8xeGbruAurc3XYzMahMU_Xhig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=FjjZTAlWMTEGhwVTK4svH0-Nk8pk4iUcWqmgd4nz3B8hqXjzze5X7DqMAteMPAycWWwQekLYhQUXN3Fjm-9OVJR7P1VQVNkhgOirt9f3gKz9d6h9vZbX2gbUsuCSCrEtaPqpcQCXDRPE99VZzzGBXj-T2LEGo5HmOd1JnXaQ4XQIlDevHlv6fAPxJwjskDy8UpR26P76vXYneLXqYld1Iyd8BuLEPrc3JYC0MKRKcIe33l52IS28DKpRE9i-w8iwe2gwVL6YFhRpp34qM0TKv9a994Aa-ZOINrSSDFVPRALBVBNwfPd4HJuSUFaqk8xeGbruAurc3XYzMahMU_Xhig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmz1nJvMxZsSvl1xH76Htl2-mjHhKgRPd83U9ztqveSzZOoy9M90A_UEu1dpZ5PSUDu-V4Bww0Nigc164-YGgywvSflwTcApdQOabW0QBWk0nOVTBZcgG_xmzsBilXYHhkA9sshrF4acwN5oo_d6jEPTUpdeOeZGmwdePdbCLcZwU89Cyxxm0_4fE4lA67sCkaabg91swsTm8-SPKmm9ngB3S2Q7y2dqNNKVvdacFz4VGq1eKd0KVL64WYuGIS3TMlg5sMw9Dmt9oxZVXbgQIcoq6wOPyReocIqXVLUGvd_5s5fftYH6eUobEHlGHgVCNA7DQVRqoB0ivKiJhsIU7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGM9HLmKmMl9KLsQAP0D2ad8Gk7F_4s9W0831wPjl5E0SL3apNUvnn9gtowstmodz2bsDfbWNYDXoledoVqhR20rxSVvmzg32uq2HgbzqopTiao6GgQbpglN4jHBHtg69Qru-qOSAMe5tbCBjRU1aaq7WveVqZMah5ZB9MFpHFYVN5vfzCvpBDWhdPqXq8bsVzL_dDmrB3lSRdsLZOjZuUktW6yOAxwokKfRtmR6b4m699K9CkUODwwjTs97tbvXSxyeSn5FiwaHYTYAnGkjlJFMIwgh_8Ch2gnWQ0v9HmGAjEujYb_4kr6E02b5kfL3oN69ve_MTmZvQEM65SCrQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=dWMSXC9l1ZrlpAcbUukE_egUG5gTLboad6iyOhH9zx5RbiLSbR6QlNXx6RQsWV-PSKh1bMK6QWAzHNIWrfxYc0lUi80qxFAnd5z3hRCjFhBywduqZljANsoUVa9Qhfcx1pGt1VKSuQ2FfLOFxRxTR6h7uezjG3618jZEF9Nun4ICuY_AYlqHNguHqXaPburb1onxQIhoJiIanc42suwbWM7VAGmJpdwPcsegjX_BcduQNpUgCuiFqLo04E0D55G9xxhUQrJ1cUpVABbtp608vd1cBN0EsRmBZZtqXitJ3tU4565wTOOD402BfivfRE109O9_OFqJTJ_86LES-fqAvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=dWMSXC9l1ZrlpAcbUukE_egUG5gTLboad6iyOhH9zx5RbiLSbR6QlNXx6RQsWV-PSKh1bMK6QWAzHNIWrfxYc0lUi80qxFAnd5z3hRCjFhBywduqZljANsoUVa9Qhfcx1pGt1VKSuQ2FfLOFxRxTR6h7uezjG3618jZEF9Nun4ICuY_AYlqHNguHqXaPburb1onxQIhoJiIanc42suwbWM7VAGmJpdwPcsegjX_BcduQNpUgCuiFqLo04E0D55G9xxhUQrJ1cUpVABbtp608vd1cBN0EsRmBZZtqXitJ3tU4565wTOOD402BfivfRE109O9_OFqJTJ_86LES-fqAvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=jqU_7Op-p_jXnr1EZzr4g9F3N5CTbt2a8xCFswoHwOCmhbMYxMt5-rD7u44PA7uOuOaiR4KU3cLeKlg_n1ZomtxSSZqMqEGeJ6QxVdrYIJqdvyAWd7nP99ETypTnz3-uCk_aOsQOUQxZ9WC0OUnQr944rGJ0Es-6XRg-gui1TKkuSqGdOWfaylucNnUDPWQ7fQZSYGsiYTuyQ7s7sO0bSXkC0YZtdGKmwN9ytfo6m0T2TJ8CRR7CWTrVLFFPN8zhjdtMbeBGNd4uyFY19Ra9VVLafkvbmebmWRM1gf9MIfjJ5SXlmc0FHWxu0XLEsfMC-mm2FR0b3-KwFiI_7Toc6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=jqU_7Op-p_jXnr1EZzr4g9F3N5CTbt2a8xCFswoHwOCmhbMYxMt5-rD7u44PA7uOuOaiR4KU3cLeKlg_n1ZomtxSSZqMqEGeJ6QxVdrYIJqdvyAWd7nP99ETypTnz3-uCk_aOsQOUQxZ9WC0OUnQr944rGJ0Es-6XRg-gui1TKkuSqGdOWfaylucNnUDPWQ7fQZSYGsiYTuyQ7s7sO0bSXkC0YZtdGKmwN9ytfo6m0T2TJ8CRR7CWTrVLFFPN8zhjdtMbeBGNd4uyFY19Ra9VVLafkvbmebmWRM1gf9MIfjJ5SXlmc0FHWxu0XLEsfMC-mm2FR0b3-KwFiI_7Toc6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzcvJWyju5IEwmrdTcR1Zmho40_KrAYA64NCyjRooo5HiuAszDZRG4g8eR6wS2pihG-0W4KYHo4F2wsaM4SRW3t4VgRIrxbCP5sx_szhkklyFYpuzkXVEOdRZiKCOhDzC_AYHs-h1fRqVCjRFbpc1yP6_CzARrCT1hieimNHnwafBWefDj3jGXMttmHaz6vHk5AH1ePdumZk5zTwDjKR1Xt9tobgCIGylWOXGa6hkdjMSQnMyS2-HiGLaG75hneynMQE_0gu64N-KZBuYsVpPL54vfBe45Vg1eGpHc-eWDt6mNkvphymaA5YSHMdb8daTWJRqFEnPa1c5SJv71oTLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsNbFnwUUmoZwR1dtcFI5fzj-Z8Rerw8kuYQqp_pggYHVA1JWHG970rea-ViGRQ0v9kIri-Y3x3_u76_85CePlTL9_j7MxMb1OJgtQR04anaqb5sAX5jIFJOGd5L0Yb_znOrm1SP4bW0G8_ueRW4EVtjqeEbrUslNo5ejtbhaLzyx8H6gacwTeOjePXfipc3YyOF-E3boVnZCPsTx5U1R1MzkT9x7z2ystbE_BqVvAJgYViQVj_pfLWYZ7VJrxo7EYUparDNcMRhGxcc7r22o5VyDXjcfOgtxH-JPOjF6vVbce_w1Ijc5poevfXANFBSvtYhIUZpbbad9aASnFVmKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSdpTBUtNJglbd-xzkNGFASmy85vD_jC62bW-D9ANslbHgfpdqG_mOxkwa49SHK9r_h4zLG6WGoKMl1nIPw9k3DDU3OLgo2EAdiABSCLZ9wDUlMCc59M56jLjax1mAm85Wi4j99rKbw1W_VsNH3iZ-2xZtCiQN4b5rXju1LTdDoH9J780Jalh2TonEJRojE7v4NhVdMV2YdcaIqfHHh_H99E6B6m2bquOcJqbIU5lJ5RBu4ibJJmgPoMhEb3HE1sFC4QNdpC0NHYS7shLCDYKzrilQ8mB50E-PkEiRnwKlUFDbS02x7rRHTRNZRjpC1fx7CrUlCe6plG0ViGj4tt1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quSpXhxQ2xMt-LMZjDRYV_SwYIqT0abe-1myYIS-crG4acOgEvHviP_74ZCms4cw2iSsU9eafiox3zro-KSbAoj7p1v7cXzj4MpMBvthVOx9FWrD0vsrG2v-XaBS_YqBT5B3gJcbwjdtUDlVExbik_TAOdIkQkEANkiFRk826Z2BRWWVt4IM0-DtbT9gSzh74cx6BMyrOzQXmxKrleLzt81jTvoaRW4_7OPLB_me2GbSmbGwWd2O_QN9jsRbWxm9wXg2D_EPqYnWYv0Df1-RMwFbHtfv_iUQMAhVZbLRaYDY9FKBv9huDA9pqrox5xSsEoYMC27De5WpV2TYqwk4Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0jsIjQQJtOU1QC3I-LPVlqyErtPEGYn214AGnDRXU7kaaFEdD6WZ4R79kFzQ_xKYPu-vKNWZlM0LIBEstJfMtoR0Elzd38-k-7GFBpDOeH8oJ-5fWx2g5vSW1kwU27A8VJLog64J2HQglFIqcHH5UPMb-CuEN9uDET3-20MKsqBci3mHEzsab-Ol10GqHrG80XCStxvI0qpaiULSHti-FihGwuB6EjI0PU_ocoA64FIjE8KVZWObZfkvq-lxUb76U13ZNQlerPnZ0ioKvrrC-FU9MHxZ6seEXeAj_3od8NCHIsjWEFy5Ow8ooEmucMcu6BrHZ0DrZqCeqqk9c1TOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYzRPujORzbBtHAqfetVbjgyDW4SPQzP_pxN0lX6_14yikQ4b9xeXJqcnOWQYhLyXq26G_l-JrzaYR7xLanYlCU02zs_aUTB5zhP3kSXFlybtGm5Jd2fbaWvG-o9kn0uhuIUgpGNlWBvDg0V5JGBciga5MJrTJeRwtfFdjv5a6fgI09eJo1wUCPC2bNhk0vay77-9ea-b7Vp8-CTDsGAhJAoXWRJASzftDA4IhbLYWLMEc30ZwHt2x7q9RAPKdNz4et2LoVN5Z-yLuTjC1Bq1Z4TYHijuGCEOynA6KURHzGrA-MW0AXjvjKc6A5KCCjX1d6inYrKn8q84jm5vvSZ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvXSk6-CeIjG73B9EkHK9UHKfGvThn00yLMAy_6CxQhjHRsPVRo8wpUZ1qzFeFm3gQBpUYrfx3NRcVziqJG5hVxTh0iA31qCjYxyOlyWi7UBsQFstTF_p50z4Ick8jU2k7dxFnrogRzj_mfnNOT1JDn5JKxclmxo0lZt5Sw_fdqsyNN3hM5fKuDVDGqe-RZj5wuDkXotX-x84hYiaGjJg9hxZrlSp_WX_m7KndXvt9RvB6F9awG8m_obu_jXzzsGgtMD98U1QAkb9rDMFBNtJTTNKjy5TmuFLy90NIQitfEL9Idv87JfLvZ-bQDUv4km159u3bfhUNkYvoHR4JpBIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rh8toHRRYHtd-8gClnae9J04SZDgGU0xq8VgyXmnlg0hWm5KhFxl5DInED6Cs_MLpvUvOPIlu4X2mZccUzNDMZW0-d0P1qCXmFD3ybVqnx2gInvB8NZtSTwZzSGfv6873-JWDtIRuj2-Fr3MDtB3dWQ6oZjHN0CWNUVcP3YmB2InlyrAXXhG6nyczfPoNpym1VJ7lxu44tyrg0g6tzZ2YIkGWITLOJ6wlxM6jczX8TuxeG0D3h5qsPEEPUHAGkOPnfvnIrSNwLJMUYHr0dDZnocyexXLuyShPCMg7aD0PlyQCau6BBhYDNy6nFdvIlJL25pfpAs-x5y02XdQBQ0aNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=GfgwvHo7qVImGxrgtgzLPHfkzNGtrGaqLpLLkfm5C3uAqsJPZRkWZZNKlAiBo1PiYDm2QAxfRaBMM7jeR-VTg0aF2GrS4cTDEQRFyUH53fCip6e--Rk7JeXbZYa7ifkNPrLxxrGzERESXLuRJ-uwXCMlpOnfoi86fHNt_anhD1eIenPtVd0ZdwlRC4QEkPg4774jwdBBF5UQK5FDitU6521aeyjWfz5nd8feakXD2H0fsOi9TF2S-N7lJgyTDPk6dhljNQcer9UX9ezWzr3Ty6OBLJ0_PK1WY8o8X2NJUbWvQyC3HXWzAb-znoYk9A_o9WDPRv1MUaiuudUkNzBEcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=GfgwvHo7qVImGxrgtgzLPHfkzNGtrGaqLpLLkfm5C3uAqsJPZRkWZZNKlAiBo1PiYDm2QAxfRaBMM7jeR-VTg0aF2GrS4cTDEQRFyUH53fCip6e--Rk7JeXbZYa7ifkNPrLxxrGzERESXLuRJ-uwXCMlpOnfoi86fHNt_anhD1eIenPtVd0ZdwlRC4QEkPg4774jwdBBF5UQK5FDitU6521aeyjWfz5nd8feakXD2H0fsOi9TF2S-N7lJgyTDPk6dhljNQcer9UX9ezWzr3Ty6OBLJ0_PK1WY8o8X2NJUbWvQyC3HXWzAb-znoYk9A_o9WDPRv1MUaiuudUkNzBEcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuZbUbIMe8fXngdqIE-Vum9oJ83F_od2NQ48ZvlzlGHu9KrvXj_yZJ6ACLI2BtiZFARYarmFNDfYh3yr6YyWYbV7bEjNgTO5TBGooumy0B4u6ck8mMG0W5YKwAjSuJlDig1rMbU1LWhSY4JhEI3fd1ymjwIXjDmPtA5fFj0xThL1LjZpApN8Gll8u9egM2kL_2JU3Z73s5osM54P6jruWDTB8lHu5q38xIuFoR_i-WkNhuvn-l4jA3fJts1n4g_xOs8TqgGSWhY00kh0DhE8_NhCRkh1OxZ2wiLI6L3RJTsfijRDJvSzJTGZzlhcWfSnzAU1Mv5PshItyczTJmGi3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=tb0hrSvlBR3J6PVFxs1MMdOMZon8gqWB59057dGKdVR6JqZa1nHY7BzM-s5WoLLmchAs0EbE6hMJy8I9-hsx8-ML4QXn59cmuG6a7u2Gv4qDea6WpQJro4j4QyohXtIeuW1HSc2bbquLd9XDVH8kQI3E1VS7FjIv5ToiqcYygobeGlL0Mye2GAtDdfpvatv7FHRadXUn-AJJNd3xBIWclP3r6luFT3iHeYCc6OLUBWNgNs0z6u1xknaHAihjQmV2mA3wXqdKdZIky7jXXvRpG1wgbDNwZS3DGsRlo39kLy3CrIwNYGBlJoWVRkJ5bo81LKCsC39YkmFQVQiiL3LIKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=tb0hrSvlBR3J6PVFxs1MMdOMZon8gqWB59057dGKdVR6JqZa1nHY7BzM-s5WoLLmchAs0EbE6hMJy8I9-hsx8-ML4QXn59cmuG6a7u2Gv4qDea6WpQJro4j4QyohXtIeuW1HSc2bbquLd9XDVH8kQI3E1VS7FjIv5ToiqcYygobeGlL0Mye2GAtDdfpvatv7FHRadXUn-AJJNd3xBIWclP3r6luFT3iHeYCc6OLUBWNgNs0z6u1xknaHAihjQmV2mA3wXqdKdZIky7jXXvRpG1wgbDNwZS3DGsRlo39kLy3CrIwNYGBlJoWVRkJ5bo81LKCsC39YkmFQVQiiL3LIKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=B-jUni4jo8_rvHRwJJjLTXlgsHkNtngyNMMOrgmEAgkgY9hrIwzh2pAcp4Ru5_jttfI5mO7lMpuoFP-RTOJesT11ZBpdekSc8oBGVk5A7TboCgrcB0y-oPCPJRLn6rO45bgoI1JNBmwwp-3U83L0EJISS03fS-WfZ2WhMcRHFhE5TcF89NK3TyJ02IodKpQYIFH3gd4mCdUk6TG-UvqS4IqDipE4qrK2LFecbMI6vy8ebrHn3EmRZCWUrF_yPJUOpUTnsVCTMKb-tZM5n2N8VRf2dciht-TvxCgeyGtJMFCzOnLRVEaxlunQUETpwhr87pa5Q2vme_Z66V8GXXOwRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=B-jUni4jo8_rvHRwJJjLTXlgsHkNtngyNMMOrgmEAgkgY9hrIwzh2pAcp4Ru5_jttfI5mO7lMpuoFP-RTOJesT11ZBpdekSc8oBGVk5A7TboCgrcB0y-oPCPJRLn6rO45bgoI1JNBmwwp-3U83L0EJISS03fS-WfZ2WhMcRHFhE5TcF89NK3TyJ02IodKpQYIFH3gd4mCdUk6TG-UvqS4IqDipE4qrK2LFecbMI6vy8ebrHn3EmRZCWUrF_yPJUOpUTnsVCTMKb-tZM5n2N8VRf2dciht-TvxCgeyGtJMFCzOnLRVEaxlunQUETpwhr87pa5Q2vme_Z66V8GXXOwRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAu7X7Y4oAHnsoSA50TZPwFtQhL8XXLzVKThF28uAUnnzq3PeKx6j7_rXOWBbxNhwjc_SkCYz70WNIE-QCw16BB8fdGB5zePtfXhiTInmE_uAjf9CR1Zx82tpLAMUqYUXLACc91gLby6bC7nJnBPhFUh8JpeHdddCxwqoUbZb4XSw4agdw81wRzHM3s8NDh1dSX98_TMg9GKDwQUEFrPh-4o4ShVNoHGsH8Ed1iEquj3_8QmAhhGWFfJiUsguLT3pBKFJ_pJ8mg5c5L_oExiaNzx-W8GrG6G_tF5MbJWkmnz8yj-7q8iZe3lEjjxTigOi3T4pdg6q6QdfiAzP1BYfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHuKTwUeXTGjZQc8nk3tMEVJvuxSX3gqUO6GybxB-LMYGIxq6qe-2sHaISTWChMdn8Ezetp_HCjMJOfR7biFoq9bA5_gV0tBNsz4zWWS1rU1qaoJGmLbBx0xtvzLTedYPeRGhkrcBhplfAn2EUKPSZX_jo3QOYke3n8wB_i5pCtVtZYawKjujbD0xUhqCABtDoBh8fi_lFf6yv0XsQdTVIckwkLqGZ67OC5VUWrFm26ddSONcsbXzoNG_UhEjFcFpZ4ryZr2uB4Jbevq3Z75RmKiiwpDH_cX4S_DdWwqvnxlV_JcQXCMM8UZyufcDvgwd6XUdM_SoaNPc8JojcQD5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با افتخار می‌گفت ما مشت
و سنگ فلسطینی‌ها رو به موشک تبدیل کردیم!
همون موشک‌ها و ۷ اکتبر،
قدس رو که آزاد نکرد هیچ!
غزه رو که نابود کرد هیچ!
مخفیگاه حسن نصرالا رو که تبدیل به یک چاه
با عمق ۱۰۰ متری کرد هیچ!
بیت رهبری رو که شخم زد هیچ!
رهبر فعلی ج‌ا رو که از ترس جان
به غیبت کبری فرستاد هیچ!
حالا بادبادک هم نمی‌تونن دستشون بگیرن!
اینها همه پیروزی‌‌ان!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
اسکات بسنت، وزیر خزانه‌داری آمریکا :
‏
🔺
امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است.
کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
‏
🔺
خطاب به رهبران جهان می‌گویم؛ امروز زمان انتخاب است، یا آمریکا و یا جمهوری اسلامی.
‏
🔺
هر کشوری که با ایران تجارت کند، خود نیز منزوی خواهد شد. هر کسی که تصمیم بگیرد با ما همکاری کند، سود خواهد برد.
‏
🔺
به عنوان مثال تمام شعب بانک «ملی» باید تعطیل شوند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=pydpwpSmQPfv2qK1nbdiqHwbE2ANMbRin1BNZXePnBCVZGlmoIYub_zcsD-0cjPuEZtnLtXOwTAcx0DicT9ExBGjbJPWYVtOH3vD0h6FBqVnmXFJ6P2dSncSYtZssk41bDIgwDuyOVUpMXF4rT6t_7vIpbqjVtQ-qUkIFIz1kw4piCfY3FxTM32kT-Z5vomUa8IuQNWk6Brn5FVvAgfXaO2Z_B8U_xDg-m4pEbim50OOX2VzbYOxjXwtMT15K3cdAmsFjQGo8iwZTOprpjSNAXgj5vtv2ZeMS092g7pJKuFZXOa9-TG36c2pAj6NutEsOyqQk7arJPyrTx4RJfSPGaH9_3AaYTbTx5_kKKXWzOSQG_m7iJ7xu91MOkBG3oujBs_BOMouiu-W_TB99N4-mcgAUZApNNwoH66wrULIz3yXi5JGLAFAjJ2R1_yOO0rxEs6dDnR8hPTs4HmhpIBRo0KUuaAe1Myveeva_xxoWHl-PpXXRzpgnN7lKOJxqYTh2gN-uncU11N9KJ62RuGKAUKsQmd78v-p100oN_z8zRV4TwlAHst-nnYb8luwhJqh1OHcBON1K33JANcppYre5sXoGxvQN9bJkSkuJ2yf9pL-aRXGnMJVkDy3qN5lICGQ5RzN1yzhGVVICh4mA5oRpW9WsBN3aqs3wsr6tj8PsA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=pydpwpSmQPfv2qK1nbdiqHwbE2ANMbRin1BNZXePnBCVZGlmoIYub_zcsD-0cjPuEZtnLtXOwTAcx0DicT9ExBGjbJPWYVtOH3vD0h6FBqVnmXFJ6P2dSncSYtZssk41bDIgwDuyOVUpMXF4rT6t_7vIpbqjVtQ-qUkIFIz1kw4piCfY3FxTM32kT-Z5vomUa8IuQNWk6Brn5FVvAgfXaO2Z_B8U_xDg-m4pEbim50OOX2VzbYOxjXwtMT15K3cdAmsFjQGo8iwZTOprpjSNAXgj5vtv2ZeMS092g7pJKuFZXOa9-TG36c2pAj6NutEsOyqQk7arJPyrTx4RJfSPGaH9_3AaYTbTx5_kKKXWzOSQG_m7iJ7xu91MOkBG3oujBs_BOMouiu-W_TB99N4-mcgAUZApNNwoH66wrULIz3yXi5JGLAFAjJ2R1_yOO0rxEs6dDnR8hPTs4HmhpIBRo0KUuaAe1Myveeva_xxoWHl-PpXXRzpgnN7lKOJxqYTh2gN-uncU11N9KJ62RuGKAUKsQmd78v-p100oN_z8zRV4TwlAHst-nnYb8luwhJqh1OHcBON1K33JANcppYre5sXoGxvQN9bJkSkuJ2yf9pL-aRXGnMJVkDy3qN5lICGQ5RzN1yzhGVVICh4mA5oRpW9WsBN3aqs3wsr6tj8PsA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYlbUrk0D14EFmNvjt314ch5lrGMCps2N1MET1dyZvLcbPdet5KZ4i9LA3NC8efvj4Da3pGBCYqZOPymrogK_tYCGHg5lxu8xJvUe5Myociy8z4XjFHLwrcXX4rf4HZvAujWfSQmdX7E9ODUWHcW5oO4wu8NZNHcts3gjea5DQHKdCzyixXhjoVENarySWw9kP-ZiWiRYdFicZw5bdGqayV7_fLugnkZOu17FMEkoQD66J2ym0G3qXizDqKNVvSYMBvxGAQ_BKoaZfy4gWlEtPrP1gwlQFiGqvIW0ClHgihtLX2wXuGCbFxyGXvJ0fnqXCx8CtYjzvVmAK-1KkHusA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=oJvO_9kXEQCKRI-9F6_jE-pHtQ10pD_-dHw_MHRm6PGZtLsG2v1jbp1TP843h-Wk942j23mmEi-wThMB8ecLXKgpUTlI4OW6D3KdMV6Rp85g5x-5oTdGqI7_AlIEAO04tTYgMp5ARMjOdnE16NXs0N3zVE5m6VCNBQtK9LNQ5cAC-wiPKUAHWxvF8SnwK1OQll_r0TIIs97p0sYmroYjhlZLwOBW2HlICyrNhvFXnBJSj54ZXKR7CPhIdXiyymugwh_JF5fPIIED_aLPgPJjcGkPKOr8-FZmE_pio9x0ytTCQiI_oYVzNcuY__HrKdyUZkj1cTyDbZPASEKFyylGgwsrBujyhHYnyXZWvKwt-GM4A0hDifbcnfvptNvnMW3l6qKA6bYcEu8biEmJrjyp4ukpiQCjMzimSRH6vChul3M2J0MuwuLaZX2sbI_iYiuTdurC2KQXBD1WcBIQCrIUQnpAckjWQAJoZHRMu9eRWW0umTBQLTHsu2q09R7ToOAeMFgjC2ya3gi9PqUBYsY3d8izVSnQIf6aCcw7lz2EOHuC0vAdPbAPw1RbwEhsjwVKHe60pm4ZZbl2h_UzcgIILvhejss0nGwO2FjJxj8r1tyLTrhiXgYkFhwKLzQ2__NuqJrlkt5kMbAhKL-9uMqWJddNC5NeJz0Ei9M5VnjfT9Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=oJvO_9kXEQCKRI-9F6_jE-pHtQ10pD_-dHw_MHRm6PGZtLsG2v1jbp1TP843h-Wk942j23mmEi-wThMB8ecLXKgpUTlI4OW6D3KdMV6Rp85g5x-5oTdGqI7_AlIEAO04tTYgMp5ARMjOdnE16NXs0N3zVE5m6VCNBQtK9LNQ5cAC-wiPKUAHWxvF8SnwK1OQll_r0TIIs97p0sYmroYjhlZLwOBW2HlICyrNhvFXnBJSj54ZXKR7CPhIdXiyymugwh_JF5fPIIED_aLPgPJjcGkPKOr8-FZmE_pio9x0ytTCQiI_oYVzNcuY__HrKdyUZkj1cTyDbZPASEKFyylGgwsrBujyhHYnyXZWvKwt-GM4A0hDifbcnfvptNvnMW3l6qKA6bYcEu8biEmJrjyp4ukpiQCjMzimSRH6vChul3M2J0MuwuLaZX2sbI_iYiuTdurC2KQXBD1WcBIQCrIUQnpAckjWQAJoZHRMu9eRWW0umTBQLTHsu2q09R7ToOAeMFgjC2ya3gi9PqUBYsY3d8izVSnQIf6aCcw7lz2EOHuC0vAdPbAPw1RbwEhsjwVKHe60pm4ZZbl2h_UzcgIILvhejss0nGwO2FjJxj8r1tyLTrhiXgYkFhwKLzQ2__NuqJrlkt5kMbAhKL-9uMqWJddNC5NeJz0Ei9M5VnjfT9Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxQCOXZ2KVyQZb6TgOqhOmskNWaR_H1UOQ6ES--hKIqv3ZB7gqL635Vc-AAwFcuao74jdTo5izjzT0h25t4w8-kZJhPPz3x-6AAQvVhIdOnYjiCY1ZB_sQFrLACe_COiUJ1VCcakepMJW6Ve_GhQYG_4hiHhBK023VOzWLQQJPEZFYlBilmeIO0BDM1HQ-6LCEBlMtEXzhT1Ya_KZR2ysJchBgbZlLwj2VFbznZFxxD026rabejd6_xRRGV5QqssDgmn_nTlfELcilaZ4TxsbmIjJbjZawS5zJ_I_RAhxB9K13yPHahVO1M2ulELTXGxuIfYU7oratjghwNtaE5l0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRWfF_mWmpcm99ussF65Qro2mEZcSYZPZeYNTE-Nn0icpO_KI8-YcCH-L988mE4EhRyostOqisOiI-EW6d_54NagX5r3Wqu4zAZFcwOKsNq5GQfSATH2EX3IFQbAUlYZ5iOa3bd4WT920sD1aPbc-it2kRckeOAFHYvhxWJUKYTqZwkcV_nAXnY74mmfPPa6hlTU9zzpw7xCDfp2oK-yhwaz_IHmoK_AFheFbIwKVcb5ova7LK78Q18qPLicPQsxVhX_wwKArJG4lcL8UQCwQ9AENZpOe8VvPD4PEjWvVmYYj3cuLmgC22t9PubWTi1R9jLmwU_29akCeRqm6jBjog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKymZNq9WXRWi70qJzybav_8f-NcZxhI0wVEZuCI5LJ-YHkDnThLRxS9CnHUDOmz1dUrt9rvTxlLJk5xLwc667GO7lzxrIvBxxrRhMAcuDT57n7HO7IQyChW5046niG00Y2Myek8IJWpArx3fMXy7I5s9h94U-aU4W6E9oa2v73zORUmRz8KUpz2Clsh2n_ewKT2iHRwsgdSO47JOrcEtdT966WErOJ2FW1-ftoM0mG7orirGadUevizZ_8S9kpAPxDef9Om7z6THGd6OBn_KBeicxSIm0ERXJdTytGt9bRfRqHzXafysGlzcdvPVwPHn4TPt_kjqoBxuIOosroNnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRtAR9EfaN_Mg5XH0MWAAPPdeuTOp3W1DSOkBC8U187M9xjnBPmeaIaTzmgiNixVtAj4zoveBg2Vepm4J7IS3xh14i2lI6y5y8fi4ua6I7e4lFQ84AfWC2y93TZBAnPVRNgmHK_5VGDb9yXcH0YyZLgtob4k9q7IhcsAY6507zK5HZljsJF7JL47RWsJL1H3wDQrPDXDT_WWYDm4fhgs7_JkBesV0d3fIp5WnoRCx_jHaihWtZuOjfwRKZFVGbgTLM7fNMcjSF8EZuiOXAlYhWHQEi9xPtX8EOl3heuqHWtt-nJAx6VD_7KC_9cQWA7JhliQfS8AVEFGVIO924V_xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMj1Jk-0C3zMDAK_osfdP7i2G5mjhV2KJSxXs3DJCwVrKciwriVCgmq1824b8Pqkasv-S64s9R3EC9LVs_tVzw_43RFvadp4lyGiDLCWSM6zvsWqzdcGYeex7KhgEvM0wCPU9mDmL8j7eLglqmfbur5w7vqKq1QiN5fTxjXJCHh6Ja9M4f__125mpWSQldT7cqrRN8s3wlGajjtQRikV_6k1pLHknJKzD_4iAYHtngM5MpIGRfPSSacnKTGdoOGEZCB93UVT5mGMGWpCHFhyoDCRw0Ah5TIl4MltTtbP8MhwIOvW5j3sxq78vxDOhO1Y6NPgDFrV_nOU7y_iLJ3n4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ydbw__DCFfq9Lc96MxqSPIQc6Q3Kuka7CsYFKqbcKCUtNcopC54KnNisvmzW53j_2RI87junW4JEVjLg1C-LHm8vO5fIsyLynUjkxRHJcJXFXmhWqMnFquKNGlkId_sKfTnM9DHFfcgTaO0o7y0kYm9aBSiBiIU_WZ3Kr6NNyy01HsIGq3AAlA39QX99Z57_d18Glc1cs8WajoaCCOcwQ3uX9CbFwz6vAHprPu5qCG8TFLvmELkFNdCESdzFvlLk76mnTSPkE8G2Vz52f3PDFahrBZKV2WZP-yBdrB1kB9IoV5hcAo9gOM1acV4Y8azMZiOVzV1VSOTzPLwj3NOCyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lybDGet2Y_HeceV6zIREfXv30cYftwUN11bF_CdBLbdqKqzrH0izwA1nfvTmtD29zzQ3XOHAHZJoBw_dQgyg4gwvo3CXGgT75ILdd_PBc6ULklxv1T7y01WsCh-ylMmFShhYo8GSrTOva-_4afsttrMPFs4QIGNNGRrKRVt0OpJuM_gnkXUWahZU1za9PqtV2_lc1OmY_AqZvB-H_RAeqN1lYYhq7_rUIWNh1F_abT_Em7iY1KXqLwvm3YRVZUOu4DZ1E4A-lcuKtKDziGWcna9zUR7EWskhUTY9S5p-i0ziv9exUQwpNaHw7MggmVi-KryFTxWbl0cOQYgjnzERfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WU-EEEN_xy1ZeaWi7ZgcthHYAYSj2ly5Zh1wRzgDVmlQZzlh0a0sdlX3dyEaohrjDLW9Tnh3cgEZX4JFBGcKkH2WEqKYPys0ZMAixYBvfrKX94DNa41ViSlwtzSqvcrUH28BQiwOEuy36XU-9-rr-90Skpv2sF4T66rSeXGXY42QA1vmLZB0I7RqlRQGs3dzvwze_EGNrvqk4otam4nsfwwT1GKEmTAtfJhuPj2f2t9pmoF2e4Xb7F6vXFAO54oWHuhJ5EYTJWdJRLEn3TwvJPpTD9y9hfNvQ4LiazskCm8u36fSrRK-4gU0BMGoyW03ZBSuArWWxN16ZXN6mUslAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pB9C1XDmtptezWhsNnyJRvCHOy3q9uHy3X6tPUwicnBSKc1doE8XnKKWTH7Ri_6Ss0x4eBm1exxVf6PXscvSN9Bu473iQRFA20VS4zSaCv34RBFsTPAzAlGINPNHUY6r5cYqTmsounI82kXdYWMCseG0BV_SUlczaAuhCQMRx9z8zqOoKDwGi_Xnxl0gerKrforYkCiNmq5ncShesv045rQKFMHHPI4R6Y1ymW9lC2vAVTUpJFvyz__fVbF6zFWHHJLqQXjKBkgxfACvxAwEbMOQA2qJiPASzlveCmDPa2joATtyAUOVXh5U4AHNhbYSnb0Ov9o0vmjfKS5JpN6V_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUpWHsQ4OgqFmbZMxxFmPgjnHhkGpMEHVHmYG3b45LZkDq_8iTDeYxe90E5xB4g3wEllOSXyyvGwIusrfJfTeChbiqk3VddFcvw2j-r3xFyEVlF7iUR6HZ0uvJPQ46KUFarBLYH__ic9ZVeF6tw2-JhNYGB070okRV66ydPd7HFjmHK0vv6S0GI8kFRJYjXPwuOJJBkDcQ0muSBidhM5pjf35OWxqcLj4faxfKhbqcDPh3UaxOF-cG0ovXgqDrwEVlZIJ4q3avZP8VjuwEQB7fv75DaeUQJkThfefntjr6hQItqPBFErWRtycse1oIgUbckvlvGm4xtTnIYz_YR9Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpVCqKPi4Qkmcl8UcbU6AliDJVNAZrCWyhi63BG9aq1qgoi1Rn-iFXCioSCnS4KnrEL-0a1-VXQSQSA_IBXP3YiHnHGugO6eQMjHTgepqjuX1XDFealZUejgC6XJOR9UBIPxkM0Xb76MnQyfBm4RQnQf1mV0RgMqFy-V2UektZLQpN2_JidgFukYEodIWtn0EMPMf53z4JRDQftna_DTnNa33cTSTCch7q-BieOc2kZ3Si8VBfv6XSxMDDV47YwvuuLnKoMQY5LG5dCRqlIIeYEX-X4dQOUf0JdNB71Ew_pHTIlmgHZHoaBLDHBoDVNqOUILt1CYTfoQaCtgnNUWpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KT8MUg1H3ulEM0_G8xlXo-C4cXVxsRo9dL9WDY9lWBUdICNhYIxr7ygfsbtEijAbkgnYLYZZEnUdt2W9K-q3I5zq71gthVt5OHvq2uCEg1LwdMVk6OddrsmkD67FY-9Z5UZGbpnX8-cTddF4X2lK-NdxtyYVTG6FdLHTjGHDMAA1a9C75KR3ZKwJ1ALedFcHcA80bMbrYi7zuu68V06OqCdKWnW-3TvUSKEViAG1xbYfFeZXDbUBEQJMtlpXWXFQ9gO9WQCyhAq15dSrPHEuJIw6-74ba9k_hA3r_13tzzO0PzAWFL7dVyyac6fAnDZOebMRcIlQbl8-t16kt8vpQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/few11o_K9JYj3skFfH0qgAGie0lcOuZBmhkeAgKq9ZEmEoo6FQU288XPImwz09dJM8UM0MIGkKdsBTiBMqayEr4hPDQnQL2cB0Ix46GxqW_CTsFdZsk60-10aZHrZiqTWVpZKXD6pRrwu8xOEugOCMtjS5OsanF_x3q9PIO6-MVHN2ux0X-2chF4yPESS6WcibQiedGGjsGWWpQ5vBkF3JsvY-_3NxvBHfFQdwlc4Y9Fn70sd5cZU1ZSvbHMaCVxqI7613WubO7a8C8EVBd6GKxfBAw7lvdEfythDbXu_ZVspsAJSIAj9395VkgRBTDUQD3AnjGYdPJX1iF4C0BZvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUkgL83uZdTuPJkv2PJUTB6gF2wB5-QAirqAbAl1PLmKBMxg3J40PpbXy165OcuvsaiiBSFj3WeTB-BSv6gQyyNG8p5Tm7CR8SDSJEHBswpKuxccrH3fPzbG2wDz95gb-Q9xRrNzcQYb88fi7dOd5GZnH95N0OsbNSHnsJVTSlHdUNRjS0_IkRiDyRUqUEst5eLQwNwMLByIpkKFHIXVXejFuJq0EZoTlhABo_tez51gvQD4DtM6pMA0rc4WEUf357iko_2wnFE819ufsZb9dG__K9UHWowZBUJ46gsa9CqtpzW8d505wjQXyg0gSjOxbP4wB89T24qlt96khy3foQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند
«مصدق علیه دیکتاتوری شاه بود
و شاه علیه او کودتا کرد.»
ولی یه سوال! قبل از اینکه شاه حکم
عزل مصدق رو صادر کنه،
چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند
و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟
بله! یکی از آنها «حسین مکی» بود!
او نماینده ویژه مصدق در خلع ید انگلیس
در صنعت نفت ایران بود! به او «مرد پولادین» دولت مصدق می‌گفتند
به او «سردار ملی» می‌گفتند!
او دست راست مصدق بود! او مسئول اجرایی  ملی کردن صنعت نفت بود!
اما علیه مصدق شد! چرا؟؟ چه شد؟؟</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJ2hLoyIR7vCJA5p1h2uEjvcCEYb5xtmmFaxJwnH2WhNNt79hDpSTDa5dIHPuTsdwK5igcdwt-qtyD3oPaxGIl9M6OilDimVy7K1vU9tX2-8apBxnl2dMNW4kHZ5C8Id7sN2MU_hMjcSNEheEfpIOKA8arTEX4UE5MPI5K63vbhviMTIdQOdso8EwMhEoETJq97BT8d6AlTIHFhr2NU9gbmTBdLC39_a6JSoQzmBjT67Cen9qkT7h4AvDxlFCnrPuKgd38RXdcZIx-_uw4lB-KBoBC7a3sktxiAjeb2CvDZoGC-8YFgB9PsjH9iVPmBYsgVqoyyFDvTIpzYvzJb76A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R185AE2GRpEC3jOuGHk0oJrBkc8xRzQeoeUHDoV1VupOM0HQ2h5R9r2wscM30azWfsNoxNFVEKQrVKVNg3ql8ACV-s85tDY2bwtEwZkKIr4fRrbBccHeRHlTeuo-4O5ieLc9l4_I0XmLoblpnK0lu4mwTtetZ434YMhZ9j0W7r44gJAf38Ao97LKQ5Bn3JAqXRu1B-NiFZZr-lxBtkj68RuPgkLzX9iR2pYhRsJ9lfcPfgYkx5LfRssaib2S_1ROMHHTe7KaQm3g-25jRr-X41nfr7FwzpW_EG22-BTqkoPdT_rlArmrikJFzmtmQs_q1_3Pxoi6tyRE_Qky5fMOBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cnghe8wDpr3q-IC5umE_HEYLF-UsHy-bSMeKQ8n0H4cj_p036Mn0vFWDz8_mAylGOsZTAOzdAyUjJ7OaeDpea152RE2WHYTcsIlHyNB2uUpxyBC3073ZSGH4mqyBfhHVKJ8nOfodNALkzwfaXQBkjnqGg8wl91m_68V2fDm8qXrph4rf_5oWUPTMq4QkY6QEik65fAU5c9qK0wpazQzkUCQTXN2YwtRY3x0e3UNs7ljGo5tWwKFAHcX8w0yOyEvSgu-LdJh35IgO67d2PINcAPAiwSKmPNpJ25mYn-3gvCIOPkySxgnRFXvV0mUFBRGdaniqujZ87BzUo26Sw6qRXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gdH1xRcJRnaHiwsge1HrEgEq_KTmBpKPBLesPlRwwbLnqzDDBQezGS36ftqa85vTLgBI1fWfhNhIQ_vRZj0oQFRuBB-n_DHrHRwlEYu9XvCYFCvkrX5JYJAkP5QgDFe1pkszPnp-cg1-NyySzrWijDdMkEv15E4fLpN7IhMNzQlAM9mg9td0kynJx2uyw0xDi87eaX-ggcoIU88YNR__56s2gXCY5F_SRgoDLDDyg1efWDzmVARsjcn2722EB_9EntXs0ip-N1WNYAV86-aKhirngpNCirT82s-LWIcpxqlWsU8bUwznA7m6l8ta5yT1cY_a6ZdSFZiuTaJjRRe3pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4Qupc93BgRPKzJlfQQ9OM0_D9l0mfWrWffF2hUNh_5Ueds9f_1t2wBv5ObhLNxvqGe3TsuOU8Z_V8-eISU82WnncW7_hk_8CdsujhF3_q3EL3HWJSkiijAyIciJZxl0DvXLLbYutc0iRO4r3vx03Hq3WMCkezJkyuxuWMOTru0VicTB3F_xy0VR2RmKjk2pNKrs_F5JQD6zqamGKR93QfiCYNExjkdtF3BWqW8GjPEl5SgIN4a4WGwkDzTulxR7goceMm0Ko68h4s01veIyzdhQSHoECJgyawTTiXzb2AQkSOrCiqHnTmoBnGHSpyk70zZZjQDl0enJcSMIM-voKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvypzfLDwli2FabVBBFR7RC1jQwmoyQzTgechBYn3e8iU-ltXHFoJNvbdJzDkGPlygWJRgpv1ckPc7ef4y2IvSQVkK80jvYkqrWA8wWEafY9Pf0MxY7Pa8nAPQ9YM7r4pz4llLWqbrFUbECm-JhiM6WxAtXHnhy67xbkYy8y-KkgWnWFqs7LyxUXh03Be-NXXlysHr1hES6wx2PfZ6M-FB0ozu4-1weCFqXO5pit9vACBMvr47316uphOSqa1-HcfCc61wsdRe5PRncA9NU-7r_SZdu93-W42mEd9Zz_cqhPLEKLSNZNIEu3K69McEoKIj4Jgs0Ap1_6ev5wEJc5Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpXr3Movf6Ma4dGvG-05kL0mavzvT0hPKER5d3tu16f7txuQ_XVwb0UWcoZG7U4LKWt3A0KXBZRooR2l3p7ZrOGorC-YHhiKepMyLO8b5mWaURd4-aZ0mZSC5rvurYa9x3f6f9lrCVzg6Hwdd-akLQhSNbiJaouEr-KgP7Dm2JNGl6YuFg65NVzKE_fatGNV-0oqoNH9hK04tAye88wn7R92_esRwsP7SJttye0A5MtKvtkyjkcVnE_0rH8OCTFeWiV71yi7_bt_eHaELO0cn4RGAPKXpbnD-Nr4fZo29_W5CAGNW6jzCwFKoJsAVz9DABRINoKIT434CK_is686HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRlI0vtQ7yCfgvkb2cS0FaIjdBrQaGkWBmjh-F-cbeECXY1LUk0JUrmq1zNlAFuXxF1Ly4iaSkcz4_3RjsA43Fy5BBeL5cCnbH1tNjkxvu3OVt932onvudnQuU-HMtAX6nccWQU-8yIWg3tXMLtmxPRyoMrNZ8urhGHvliCYb_8GuTreGtDB8ZrpwhA-4gfovkQo0ahp5t5QCEaHtS5XccAImz-SwCX4mI0uMiOut-8weSyLN6qKXNVA9LdSHPHcnmk4OsQO2OkDKJNoZaGTIm6S8Ke0_oOYbNlwKc2BUsDs77yE7LbmW2QIdhxTQp-5sD1tV3FMsxK1_W8W9FIlHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBQquI_T8OgzEtgSVgvz7xpQaMWX7QgPfp2EPUHPFw1DmyjeFM_Cn4WFXwWvQZBGrX3qUIujSjpY1l22howh8UbQzcbehDUHbWvT3d2YCstTs7A4PZh044aGRC3xiIeurFoYuQAMEwWezBwMBAfMKNnEAa8IG5QH3tHSyJZlMnILUNTh_5wc9lnd-iiKxRMo3DAcZFEgk1TegypTa1W4zf_99Yro2-dig4uE03omME7uSer8T0OgCraUIjMBiB7m8vwtw2Z-AHcx6o6MtrZhAA9P0TN3iX1M65zQ_0iSTvGEUGxeFdVrsYEV2V6Q0J0lqBh3CTHiuddsYLPqIsirnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGUTgfzbOJxMaBQ_cqlKbK35z5KQaflhNYrnFmGiE4-XxBadZvgigyezOaRHNJHi2G8oUjnoBhuEMlFcfL1c_3CBSA-OGFQDY6T_D_2kjJies_BtBkq9sYvO8v_3DltsgiO0u7h0wYX0eHvCEOz7cUSykXJ3rDi9t-AU2pzrsWgwupro3vJi6LNopfsc9-nwCM6VXAyCJEa2cfsly6MtGy-wADhhg-R1nfHfEtGXEePORQOB3tjhMe39K01M3IxMOLG8SXI8XYV6ifBFS2a5UAitOkbZ3WWqVtF5p0Wo_6cMv7RmTWIrre_-5eSu4QoQjRzEtyLJdHBSLUlUF-TPRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0_rl_sUiGtAHz7S4dTynzwTnIyeT9NWMrND6a9othR2gXq-fQ62Qjhv8Ls9BbRnBnIY4F1hjD2rae68FZJoDJk4MMtiu6WxdkvuoDdSJQ9Gi0X2W7LAxsIhtD9R-HUFJaq_tpNfoi7DNv5mrbHvC-YbQhCA3DaBAr9oEq_suMrwg7aY2pER3XSju8V7zFkZqtpvGdyTXAfLJA0SK2Q13kQRq3evOU-vB9jPfvU647doWCDtJYj-rdcEuOy_yfVqLWpJnoBSj4uIF0t1RWOB-fMYvVbrYpOqGMB7gED7vaJvsxP_Y7krNnvGyXWbeGNwWCngRU-zpJuVSGXjBZyJww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vedunPqI1aYPddFDGG_J56t2k_X9rUVQ19Y1-_FAZQNx9-TrS-xPqsw-HEeZ7ialP2h-_ZOnN39CpFXmdDp7P_b1NwCA5uhbGtQc9QgJaHmvVBw5pYk8a4Ci-9HUjdLkqN_1C53sYJZ8gyasa70iLm5vV8t94ckwC6XfLxMRHu5YIEUtRETNBg09SnVuv4m0yqNYhv-YFBZFOA29mfkQ_iyzg1Havnim_6OBM5MTifD2fqKnMeiOnBYdhNlG9kxQDSVaq536BgjRvhbIug6bG6q77-AheKQL53jLsGOLMYJtxArKVyBmbLpoxKi5saEr3I14Td8FcesrIUFZBTrcMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DC-C3BWPNYU-lHGXYcCCSsAln9AUVCabw-D97zE7ZOivFdcAOe3xJHVwL7NXtXCkP5BlKMzwOnZ_rjuCEZJomVE5mA_qOx5a15XzoDo4W6oWN9DYCHHGWX-nb2scBwIRWb-LnITbAkpRkNYWBZcTZkAyvgnii6n3d0R_LQfUBsGhv1HgUuU1M4dBp_kmIw1keLAVjvZ0xEavsQerN3VPz0sjc8JPM8P91QFiFfCaZtk50qjqkXek0mHUnQ7RLe6LR0PO5Trsco8KAjIp8OezBKRLNj5aVg3_3stRm43BI9GVmhaBUVSQuaS4jilG3uA3hWy5OfiUc87yp_fSdXPj3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qq0Svi-_Ev6c_CoShPhG-QgAZa3Nwd2oPgqzBmdp1erZ5ogUor7lChPVv8NqK5FHi4r1D1D7KUlj0PE1LUJF_R-vsMKDvietd69y2bCD_LoSYH1DjvAZGZRCQT7n3DZzz_ZN_3U9z6CiRvM2ReIMqzmU3e-JVq9UxJ-vTKRz6AO19MXo-xPxIDfLbQ3UtvmsBDg1NBZmEi2LUerCnnhgAAbp0HAJwgx-2ph_wT_oM_vviuYIjwdcdksy84ojPZE2sUmp0Qsp_GAqusPSTE6AuM75aqYEi3RF-3DiJo0FgUiHS6jkFnN8YjpgSv-HZsvjiWWMijos8NRlyOZo2zelWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-HjVhzeAFGCOLKfPvPrerduBtZGbYdiUTBNMDWG6BkoxuU0ZStFSQ439XCo9G6VLQW_0UPBeH4bGqL6YHl1GYk9JSvZvU9mHWJYzkFZGy7ZqJF5KP8xxZoglkTIZbazsA6yG3g8tTEB02Ozvj65zK9T1-X2LX3Tz6RpkEhQU_U1ybt1kgY5UgkkMOPcSLMcaONuJ7hC-eAoE92nAkMd6dXpXiFmod0nwU9RNQ-as1ZL1fgC9U3nbbTZP_4F_CZezUJQO0rENZGpTzBq1zVNp7VuSKwOBqhEk_6Mu9r2EBquyMi6UyArO9W5ieToKekr5KuCGnoiJ5QvRcaXBehuzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1hyNAeKlsqVUCu4YYf8UjUNFoK5-bcNhax9Pg5-1jNW-7-tFApGFdC28kHeqXQFiwoWOyzt-NjUGi026Zav_g4HpzRPISUxPUjaThjHMD3FrOFUYjeqa9Tj5b0fNsl_K7BYjP3NXy8xqnm-hyY4btjoQr4qwx2P6xJgHOmNeCGyE0aTGF0m2IssgFK6veogazgfF8VoX7sw49wB8QUTUxkdhb59DFTEIOtILJ-gmca07jajhivDiLDD5svgVoNXS6QUuqG42NsjubAW0WC34R1JygXJ0IBg-CdL1m8GY6ybSjAqdpDPFhRv8IT9P3fI-uwVwg_6wdnJz7uFbJWsog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHjxzjTr7VnTvktDTjnbXnWx4c6Hnylmo7QYrK88JYQcxhUSLebQJ0rPrnG17MAnGev6yGvsl56qdJgosGRHoMjr4aQ2GR6auQDhSqwAlPAGdIPnEN93_J5-TycwDIhL5Sgp4sLzLkKr7dfZpvAbv3oE9xbzzuUGGaTZvIUnH_F98FoayTl8kWAYAbJRijtju3jd7m-3N0TiTUjSOIL-rgi5H0lEeiEvj_lSnFlLQKOcvu00CO6lnIcoDy63ARNjb5dv4JW-c-KDICf9TAOCAd_dyclh7ZeG-Arh4CtgrvQw5dyFuAXcQMg48id_Cc01g1mKJLVdACJlIw7chteZ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
