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
<img src="https://cdn4.telesco.pe/file/VW6Vb7Vux_jtdLECp-A7f6wnnGQOyS0vKzkZ6lGAQObo3qHn6r3RP8jlTRFszuJgwB3f6Ti_Ohik7LlfZuV0aNVfdyl0PvrXWYyabAsS4OGMh-cia4Kl6aWQvjQTMQUCRMTVyvzgrtSDAlDVs4rkaLh4ZMJdHT7P4WXrjYsQXVMpu5xdaVSvWnyP4BThnt5tOet155wwcSO86AeJB9sQIipKYyitH7tumP3ttL4tAEXpOJuqMcVNH8GzuV_8KVNxSRj-CLA8YY9-GV8K0dASfEmKerhwsH6YUkIzofWnNROECGDV036IOz95a_lLLvcNI90T-vW0N85hXLJhAxiubg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 02:04:26</div>
<hr>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9Z8z0K5QN3YjOaLAH-wOmFnnV2RHoxH1kKFUKd21bk-ktwswrhkTbkhPaJoYbpabn2o6jtpH5iEWhiowsTzHzNyooDpoi7g7B53WyvfxXhc5OlvanTVLekSYlUPoTsJcxogMsfOB2a0AO3gFe3XaUP9-rlkphez3igr2RibWU5hHiPBq7aOJxs8sfoDD1e0ho6GB8pkKeVoB4CXvO336FWX-MycIT5gnP3bGO_QfkfuBbPe3dnJNd3l-6GnMGEYksYQXqe_U7HneSY8opPfYveXYv80vX8quL9YyNC1clpVhtDZV7dxyFnSjIgmEfq2Ww2dHM9pC80iPtlxwUJIEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcApaWyesX074CoP3lDbQVfJbSr0AUGukH_KCF1PegWPqAskkKHClkVigxWvbw8DXlZt_XjcjqGey2OZ8Ksr6cPXAD0WbS5atJrVE2mq33FvK6QEMSlk4Ggciw_qdHRL23hO3zRJLt4Gs3V-iE2kCtWBP0Qr5JtHf3evPDbsu-rv-561BViB3tbpUkdHoPpp2sqliuBeIq-fCgkOMM4NxQ9bCWzk3w1xoZjPq1Dus7C7AD-zpfd1ipyTjGpOZ-qph4Zdf4e2MMJUpAcB6nEI4i-OLsbE9S325lGNNo1LAPUFrhYlGN0HNPr0n-GXKjClVKp1ijin5KmZCBI8Ko0GEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDNswknBz4ZT67LImWh6wcADlsqSCqP-ljezuM6XZKShMhw45S-55Bzen-SAIjBfv0C6rnNxnOramk4ineH_nRb1iRmzh3YEadoEk4rOeXinEnO2bs4V3QuNMrnuiYybRGleuiq30khtUcdDPz2EdZajWaNE_LFT2NFyFB9cb1eDOGONUbruWjYFigrbLNyKbgmKRgk0d2BCIkgPz-LIgKwWUhJ7lfWXh8xyjsLJh9ahEnatJxTsswMLDhMwwJZy5RuxM8rC1JdxnTyHUVlExcPexSUaPQd59GQohCUaBguEV8JHPvwHnbGzoRsSleV4yyKzsY4Hs26jsQ4aqlezhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FX7fpzUZHaRLWeC_H0RQteuy-Gtf1VkHRc3lOXbb9qTS57F8cBcd3rWCk6EX2-VGTehCDgjdQsD2qENqFwNJTxD_DK22XqtfNzet3-Wndf6AYvGy2W2TM5qFXB85BEY0wLtaJJgWDKwJA--OjXDyM-KQgq0Q-Ov1JZ6Sj42-nAFMHzZZtMqw7Tr5b8onBp4GyPZPOmsBxAUSmBtrNk7PQuu5L96i4YrTYkIRJen96mBpJZZFmIoY-R7ORxZFSlSZzqLAqVq8Ctjj1uAtwQBELKigv3w7iyNebnzHzIlX8vTzOXyy2ELfpSL-TIl-zXJZlwVntu2jq2Kvmg4mpbtmSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=FJ7ujRFWz0Qy6yEUH49WcFZAesl7jAu2IucBqP4P2lFFz3WiZlswetjJzHFV_QQTvg4iOSFJEyLKXDKecuL0Ra10beOIt1NorZ5fc9nlmDc2IgF_sU3zbzY8T32Ev6-z737HFGi48bdCPTHRnbi7Gr6nefWp2Yo00Nl1T7S7KLs3HYpTyXq3A4CojSCpuDUI0OJGn5rIPkRWu1pQB4UOWDW2iCGzY0bj2rVamTB_DTCclps9f-_hnAd6PkuhSHUEknYCgwYDaoyJftLf46EfWkhxo3lx_4cRCcU3dIKU1pJ5tYbZZpsj4SnkSQwMzzQYlIFrjGaGV_PquJkaapD5Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=FJ7ujRFWz0Qy6yEUH49WcFZAesl7jAu2IucBqP4P2lFFz3WiZlswetjJzHFV_QQTvg4iOSFJEyLKXDKecuL0Ra10beOIt1NorZ5fc9nlmDc2IgF_sU3zbzY8T32Ev6-z737HFGi48bdCPTHRnbi7Gr6nefWp2Yo00Nl1T7S7KLs3HYpTyXq3A4CojSCpuDUI0OJGn5rIPkRWu1pQB4UOWDW2iCGzY0bj2rVamTB_DTCclps9f-_hnAd6PkuhSHUEknYCgwYDaoyJftLf46EfWkhxo3lx_4cRCcU3dIKU1pJ5tYbZZpsj4SnkSQwMzzQYlIFrjGaGV_PquJkaapD5Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=s-ws9rxIojFEbnRyKwun1yxizEEIwIsJ2nlAmYrDClRPi4w--R_U_JUh50H2wT92obc7YrfXc_d5JS9KTioUd66Bh2N89d_Aay24pPz5nelNlRvzvdt4c9YTRMxRIBhikNcD75ZHGLWUUbtIZucBhE3a68VXws8Efn5QHv-_F6kq2eSJAq4mWPtHW3wB88b1A8LT-C4Slgm8PfALb-HDSAeKHvI81rxgH-DcQ-grRjRXz7ReE-p8QjZzsCyl9-QB-1X32FQI-JgRW09eIIXB5pMasrCyVwuwGI4pWPqgmHnK_z7lQr2cJfQX1ZnoJ5xONWFzoxVTxo5pSHF1ckrMhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=s-ws9rxIojFEbnRyKwun1yxizEEIwIsJ2nlAmYrDClRPi4w--R_U_JUh50H2wT92obc7YrfXc_d5JS9KTioUd66Bh2N89d_Aay24pPz5nelNlRvzvdt4c9YTRMxRIBhikNcD75ZHGLWUUbtIZucBhE3a68VXws8Efn5QHv-_F6kq2eSJAq4mWPtHW3wB88b1A8LT-C4Slgm8PfALb-HDSAeKHvI81rxgH-DcQ-grRjRXz7ReE-p8QjZzsCyl9-QB-1X32FQI-JgRW09eIIXB5pMasrCyVwuwGI4pWPqgmHnK_z7lQr2cJfQX1ZnoJ5xONWFzoxVTxo5pSHF1ckrMhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJXVb-g77PyBeK-8U_mRbMDvePOYtY9Slxjx6LPjpMO6ZO4of9Z5JGqif2S7w05y01dAl02WOGlOS-dg1UhVrldknLSsTNMi3A9X_CwBg-VJMRqjA2K2mtjRSKFQHJG37yzNBhqKfvS3QUkLSLNraaJcWSbM2Ak1CbSLTvjzUhOeCw8OuZAcmXnbenfuobSOtEVYwopRJ8vbmhpjMvTkLfYXu1ulH5fExVAIRGvkF9GAdpKoKSKa4wpHpugNtHJC5xteDarg9stahJfid3ZKRiDtGkgjiC1euHXLJud5G7uVmYNYwLCfu0y-oNGPI1VOX5Ojaz0v-w0O6rhDqEevkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeUPsgeQzVMPTUfdROcwB6yGVhAqGBT3davFKrRBIsW9sc6gnAQnSuozhIY-3cHtamQz7QD_hIrnNnxVVRRkyxO7Uh0Kv66d57njFeo8sR-TQZ7wY0otbUIhU9sJFtkKfWYFADsKfr1I_H8BQPrDz2CkheY691j55LE-eQxuqVGXOjvPXJDdljcoJJX4PGbh7xLkeenOMxSyXa8-ehhN0pIBJxfjn0gkgNQ-NpTl8YbdstHQ1N3jE35Y8XLUsCdON4eTZZaOgShf80D36a58uqxpWW7ovxuSckvMbqtGv1IdL9xLK4FDP6y-DYAKxfWKdzSQmVo6MuH1lFG1QLgcuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGys62KWoyIPCwufqLbyorKW6Sr-QheOFyabqetCriYxaWkaOSJtICnzEVr9815_4kYSLefm3tOHyaMFUif2itELkxEuiqyO0u_ZfZEaS0XJ6giZU0NMPmBfvOWlw61GpqdvjbIbtJJqTqX9UlzWIUPpiR-ky5DxhsdRX9m9Ytp4miiSbAYamu53fwgN_0xMrSJ-K2W87rMKGclr1CkLTDkuYM5qsnkpvck5p3VXJNgB1JWTgGnwSsSpUYP-MsBlfMt-Byi255ZbysRDePgYM3eFXh0WAMiwQ28bvQvyQkxmRtT7urts2AISb56pmk7BeSLL3toHGbJoosuAgh5dWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSY4Yz242UxFS5-VbD4jHR3rwvbpDFSTnUZx30HjVVdkWJxlyb4WBkuAqnPMtHC47zO_sx7IU_Xc_MalfgbmI0bpwUebKW9ucv2qWK3JN71nJbKE-95oFk1_J_4PU8QmDkpz06DucMj-aQd25Z5Arr3UZIel6QRsSRuZA2WWdbHX8cepZo0Jf0iCWB6XaDOsgBtvg8ZNn5vrpyJbifi-wBiY6EsWwWrSEDIwbmsqVHA53Q-X3Uf9jo1-WHn7_tA8t6EL0irTbxppeUyF_eSy3_3Mkm0PyMlt9NPDTA9ONeSsyGudmwzTZCxgF167vJmwR3qyxCeTSfebNB6SFT6oBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tt5eOEYW7tebvvH2TDkEzGQ32aUARdCnnv5rP7-G1NER-y_KOoX5i2TlYQo37b-Ww-XessMKJsAXPCbfh4nKyF-q1Jo0wgJeWl5lbqqkhArqhjA816U5PcTqdHI1I3HRJz0qlGw_2oslbxohxTbE1RRACG5kceqhMXOROffw3QA7u3ixc2LjAawDT0OchPDLOmeCDsZ2uuBovHP7H5daJ9qhf2izLyQ36T4VEukKY7cRDZkFI4NohDIGe_JcVvvHgLywsPNY-3IZraneLBzs9S5QIrcRD5n3ej3rDR-mkRCSrb0gAb0EQOgM9u1w90Z9Lgblca_T9Dhyl7CR5qzKtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJEY0EMR-kf4yWBGmpzt2xfh-FYkm4yg4b3KC0iba-LNvDmna4uKD0ISCMFQye4eXXb63GJxK5K0SQzi-jXxBG1Bz24MOjLjjgYV2iTfRhpVLCH7YnA1lwWA_uSrh6GE1YX3iw8zVvfF2zYSm4YypX08TV2lWqPmUlRo7DFWe-Ri5smraB2E5xPvNyJcuWeS3BDIOqWOirSI1eBEigw7W4jfNn-KEfFgja1j3DGCyxC1EElMiYKrGP3idwTKOodK4TNUhKSt9Ze2nswG_MiCN2Kt8leVk5rfjTg6GwKbnRVIb_5g8gmWJgtzTOzqTVEm75E0wZz5jFd-g9ezPWt1lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTsFMS-Jh69mLx0zs_d5kSGoxZ_QaofKzGNqVYzGD-II91gkqRSZ6rsUXaOMe-tksRMnur72F0QlkYUAygr5RUrhH60dQgR7pGF-nkQP8LfruEC_jpatu_ulSmdPmMXYe47ovjr3O4iE6CFTm1QNgX495mEGvhGoPPCUceMZ3usJz4v6gfDuWBraZioWnyDlmeHx-Q3t79vwnw-LtaRUdYd57kJu31eXOxGZWk8tF6KRu6BT8pb8kKUM7tmROZHDYrhs91XWyWZZB_h3M7N2X1bghb2cANd8Ug2f1utHZNnly9zZND8IcmyLkBxQiLntztDQ6a_oTDkwm21UxueHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ttbt4gHVFRbZCJUhlpIp6_Kk2C_QNb8jrSRAw9Wh7rT-dF2gxygqOiIuA91_ECbwQMTE6-IFbI4V_0T4_y6RDFZG0txwC8gPXWODVjH_DVXfwhUCTScluREG_UA0uJlF0yiNo2GegdTx-DPc48bagAeWj-WHf7zMKhcDUwbqfnalXosjtrwpc1QGUpSx0rQ9VPjPouUTrCDD7li17s3VRBS3tAemIxMoY6e87yw2wdLhmY36myyc59i5cy673Qe7VBP4KWQsiz9vh9pH6R477Mvbpc4a4KfOu8nORLQ68h2ZhMs1TBEM_mW10DDjkGUlvb8xZMncy_zPBMZeLrIALQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TmxLofBGdwo0fCF6ZpdX4RDoVUHpUK7jozPXMJSgKfA4SW1Dem1NxgrUk1Vf1-MsZ4u_0Ok5LClrRnmg3n3IYZYNW0OQu4r8ntMBBFhGxnMGyn9zGF8v7Qd9EI26-laOi5vfcob6hd__VvJQut7LIVoiEaq7Gv1YOOUUU5oA4OL2J8eERNuGKGI0gVgOH_1oy_rBnac3O-lC29P2KKInP-87iLHARHHuGRg1Ll7WvM_Y6G6P4xVrtcPDid_bqHMbb2v722om3QzuAbz1NXeyZtHrFFYHT2GY95ZtK2wQmWJs72RKrSUZ-1eFp4BiCDhPbGhfGTxSZ85IQjEmFzBDRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxMmxZMFkVTrL2hrGz2Bmi6QXi22YuwQTT6WuC_XNjV1gBE6KzERiKfm0TM2FC4n6bG-KHcswzYUA-Vm6UpGPmLKEk2KnXtn-b3jelxT2p-X1SWlC97Oj9EoJYojjT_3_6qfxt4AI9SdCuUphqQEcw9MK6frrrsZPqVGgC0tlP7dJiGVjESmZFFR-7_ediHE7TqEIPRBBAmhFSPMJI6egkvH0Ob5Hg0FSs9_agApIv1AFTQCocxRq4Wj69_0U-DCpKBZJL2UN12_jfilJPDT38kxq72V5RnSWigNpxKhg4AgZAWH2u0EMl-fLoGvKCjDb5Eh4oXx_VzG6xoXxefyDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=XGgIw84kS6KAf2O3p0Bo-s1mBra0gpC9zwQEatz3fhXcD5agszMhQ_X9AJpQN3G8-xOzOY6o4m653lHYn_3c8obNSNHd6PPosHbCJCcjLbC025bplbxxR2oGvr_-ijFyWyfJBsL0oRU2Jq1UDbvZ1YenvIJm2MavFgwnrMANV9MjDZIBQ2P7lMF5sJE8sAROTklmPyWSRSVKQhsX_r5ptEoB6qJDm58u0AJDgbi85uQgohJLN-YMr0f_ydGw1c8aEJQrOk0gowgIqJl8cV45qCs4lWEfks0c6bDrJWY1Zq3NK24t5szWLUCgdENAPaCpkRRh0dpyc3cLvrWFn4ZfiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=XGgIw84kS6KAf2O3p0Bo-s1mBra0gpC9zwQEatz3fhXcD5agszMhQ_X9AJpQN3G8-xOzOY6o4m653lHYn_3c8obNSNHd6PPosHbCJCcjLbC025bplbxxR2oGvr_-ijFyWyfJBsL0oRU2Jq1UDbvZ1YenvIJm2MavFgwnrMANV9MjDZIBQ2P7lMF5sJE8sAROTklmPyWSRSVKQhsX_r5ptEoB6qJDm58u0AJDgbi85uQgohJLN-YMr0f_ydGw1c8aEJQrOk0gowgIqJl8cV45qCs4lWEfks0c6bDrJWY1Zq3NK24t5szWLUCgdENAPaCpkRRh0dpyc3cLvrWFn4ZfiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtMgLrJU-Cxa7AY2-NyWAFh1lLfoiKzzhkeUB1xwTo9sAEi2xViGxp0q7KeTh-0ST8MWY4KqY5L251XaIxuJzAAq0UD193w1ybIvb916Ck1pOQWR64YhxCEPYo6IQ-t5G48OXzu35-STZiB1iBFkwa3pkT8dRo9tIgPUmmnWGGdpckJJQTvD2iBPbVuaZkgyql71DTz-YepklPIovhpMe3EsmgVNeeeabsML8hZyq4t4Y7YctTPvTsIuMBdQPLFuc48nCm67I9ML51C8jLoZUtVD0oGekxWXqFQTNKUHA1rKGaASy812CrAIP0toP4tpyxnJ3xx85u1OjIP08J2kVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZKtnIuZTShNhWN9cZeeYhulerhCh229G0Sap5waAlq-zXCh4BTNk0b4xwGf7l7R_FmDOrNvhRV64LUEs_jBogKtTB4itRBTHjCQZnTEHCOY09BiiGzQZFWLMHQfVmfXFcyVJDrBTZ-SPphaO5ovYkg48N7vhCpLSS3u6JPt6M0RR2Y5UvTTBDUj3fBXUmHpsax64Qyd33H3ofxQTsI0fyCIoTHEykFSGni3FEUbL2cm4AEFj4fb88DKaaOsI4ebDdMttqwYKKJB1cbHEQ2mHTY0nxSNWnUq2XK--kG1gJoTsJN3PNxOXRLldMLmRf0dNT3ujJmBay5EfnZVo7n3sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=VVebRtR7bXiz5QMPsrhEh9CM8PpIR9duRELlSXd2rmgnJRSdSgznuqPcYUz2lh3a0rn7hMcNb4RUHlYPDDgc8xMhzEjoqqBgTBGYKH6X6-dHPmQmzocxaZNb6vzi-zxvlgElot8wPCwYvj8kR5VErxOv6RLWYqIbnn8_uUoruKPrer51oh4pubPEjdkU5KgdJC2QPlUt3hvAGNi7dfVVVJcbzFFakhDcs23FkBGZp48yZD2PKa2MG390dzlc6vJpfCUgSYrbnc156Tuxce28e3OlgHfZtBSgtCMkzCWgDdvgEz13NQKrY4b9PMQcmd7uvho-4muibAHIQbN5YLFFtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=VVebRtR7bXiz5QMPsrhEh9CM8PpIR9duRELlSXd2rmgnJRSdSgznuqPcYUz2lh3a0rn7hMcNb4RUHlYPDDgc8xMhzEjoqqBgTBGYKH6X6-dHPmQmzocxaZNb6vzi-zxvlgElot8wPCwYvj8kR5VErxOv6RLWYqIbnn8_uUoruKPrer51oh4pubPEjdkU5KgdJC2QPlUt3hvAGNi7dfVVVJcbzFFakhDcs23FkBGZp48yZD2PKa2MG390dzlc6vJpfCUgSYrbnc156Tuxce28e3OlgHfZtBSgtCMkzCWgDdvgEz13NQKrY4b9PMQcmd7uvho-4muibAHIQbN5YLFFtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=Hnin3WkqocEdRB2YXq15gE00ExocJOsskBYHsrPDPkMF3a0Rtmdf-vx6Mt6U39OShmK-nQcjls6O74AbeyjubJjnqJS8agJxyrVL5gEQiTXj4AgZQBx_YH5BlqcTCfW9MKF_dMsW119gqgHS2xeA3KUKW424c14KNEGeVz1uC72nLiU2O8O5t_ZG6zzIci3h2bgTd_zSfnnAhbVoiSRKxW3oPmQPmeh74B690sKfLWblhqtr3m3dLUCBSXoKysiQSeWATQPbUtWAo0_hRFitlyNEYWEx17C3OZKZgNnVYBxInHFIwrLBGqifIs4IxnsQWZmQcZv1klI-R_V9mv1Ssg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=Hnin3WkqocEdRB2YXq15gE00ExocJOsskBYHsrPDPkMF3a0Rtmdf-vx6Mt6U39OShmK-nQcjls6O74AbeyjubJjnqJS8agJxyrVL5gEQiTXj4AgZQBx_YH5BlqcTCfW9MKF_dMsW119gqgHS2xeA3KUKW424c14KNEGeVz1uC72nLiU2O8O5t_ZG6zzIci3h2bgTd_zSfnnAhbVoiSRKxW3oPmQPmeh74B690sKfLWblhqtr3m3dLUCBSXoKysiQSeWATQPbUtWAo0_hRFitlyNEYWEx17C3OZKZgNnVYBxInHFIwrLBGqifIs4IxnsQWZmQcZv1klI-R_V9mv1Ssg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dU4TngsOqmVHMkxQ72UCUquksg3u6nnj_F2Go9WKpqELqDMsXnldKP-49dyYXRnmrMo24mzKMUT826voL8lAKLH6xVOH08dJIXw0mVxBVPbPH8TQAwWYznrPpeKZQ7720RKRTka98CDW1V-WKKHd5cf4adNSeuXo3lH_yamILmzr2lmFlwmwQUxxT2cR4voslj9B3L-sJw0Gfo3mGYIcNr39GyFwzLf5GJ0BnAxYYPX0lVcshLPEGv_4g3ugBTpr-NUvch35FuAzwgZSIvtnBjhD0eT3B7g6dg4ZxlJVucVCPf870eZfkZFRix9wKFjOyyPL8tN8zfPTtcS4qjz2Og.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWkX5JX9Y2rx9SH7nodtNEq8FT9IBAg3PinBGYBCG-UPnDIXFat5LRhgjyGmnIBQTDiTIkRM-z8jB41-DhFXka2YS6Me_6AZUuuPqLY3ldn-m8bPMvYKSX0ZZxgXH4_z6UKv3RB46nzM_T9omHOoCxz2F-lLmV038luR9ej6eZoFyS050WEXzh9XHOHOitkx8WOeaaDscqhWUAlqqD164JfzZwoRjN8w-AI-7ym_S23q4Ow98v3b1N5P9EPW9DtL_DYjrAKea4RIX_Qs6lJXydnR9gvcydRLUPv_hBU0kIonBX0bo_q92cjKs90h1ni9OZKYProIz5K4F_-PLbRvAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/np_wG-s2nyfJyRlgdoUW4R6Zgv8E9RR7YV1bSpWmiUDaVrOsVrTi67JXMJnAn8UnsUARov38gP31KT6lRKgcsRQiEe-Jh6iSOhCbIhnww1rcz62F5DrlXSof9j--egUzTSavJu_m8W7dAId5nvkSzFjEJA1L2_G5kqTla45KPS86rt-fIW8Me9s3y-QR6koe5dv7BplSzsZb7yRW0YF8PVegaSUdUC26EP8wuX6-2L6BWWd-jp3Z5O_WHil38pzhg3IQ7C_p-8jfhozwqvlVqE_lvHsrYPieU45-EYG6b5YAv1dLkPi0RjyUa-eR8kE-M09BJwepNgFPj9loXmPRVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7JFclXNO4fEUmvWtaFkym1X5ynqPUVUItDDvNXGelrUfrop7jl0NMAc4rMqaybBgA-zu3CK9qTIkGjLXBEzWHWzGuNzHQZd0aoPAfqgLRF7X9C1PVtCf3J86NfF8q2iWxA0FG6YalNAgHIzYB17AmY6yPeVcPlBxeHfbO6AIntzvaladwHNPemULCkUIt7VDWkgGpwCjjwDdKgTv-zYOlkUR0WxH1GzrMgjRwYlM48ybIkHi31VSNw44scrFbpsq0sEVRMywyFVgM8tSgahYRtaWheyNncz9r6W0_QQYHDWAt01pAbsLJFMp_mHDgO2BtDkRW9_S_Ks0YZsg0Xa6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaNvK2nwy-c40PTrXIkgHiRuz11i9y9i5FhBLFpnma7ONKCBxDZDBKn4IIBoJh3rW7S6YoPFzWILD2hRx59k3OxQ_2OAbhlGqTQWzeHU2OBFUaBpMFVFjAEtm48x4E3BqHCwYBvlgG6Acvnbt7pUkrBIKivlZgL7de56YRW_hjdnD6n4-_5naeLJ0SLPXvrUCV57FZpM7tT95gOmKflrcUm70MgI9feTOHttiaQeXr6SZSChQkKnTPzFS0x7J89LCY6COPxN3XxAIKOfR5dW5Q55e5BzpfUb-BUP3ODb5u-X7c-qjMGuCPgxbdjZnDI_XoYsabUMhfs5wCH983nUFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTGK32w0Q4iaknW06U9oTUMRS5Jx-QuR9kpp9Ye0rDVUjGjEggWf5rI5XO6WpHV_lfRz4_405H-_YWyQnarXtcXXYbuTnGaz7vbL213-we3oQpDhL7EWn8jIXUHcXEaKiEXXd4YJ1Y3Pl27GR4NSeMstW4U5Yir957xMjmi3EvLB5EdGcpL4er0iIprov5WbTWyomFsnfFc_CVUeS8bt16Fc87GyVnyWb8NDKYhpYCFjHB2ZupLCR6Um7vO_t6Gmj33e3KL2N990CdAjz3LecI4xxtn-XXTMvBIB4qaeLehs4dMi2PRNONbRtTo0MX0mzOM1G4zXVJ3KHL6jYGaF9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQge7QABZfQb52mBCa8ler3aERQg9aMn9HqpuB7jve4YR9kC8xe0mjbiCYL2DRwygYM-bUBWSZcbb3oG9k_GOs2j6n4ko7VxEScsYoe2DIX96YVdUPM3kkYsnC4a2QSMPJASbGtbzN-Lcrvx-m3HfE-_StPKDaQgpJ03hgSHW3X6y0AjRax94yO2sFPNT7M1DQryk9SHxpfdYk-5fyhzyYkn07MFzJwORZ9qOaKxzDCFzWND35j-MZyuOtgUFWhc4a8N8Vag118ZlUNnxvngw0nJipSH5pypvLeNdRNKJV4MLQmfnO4TeXEkjm1KTzDXnnqUWaINEw1-gwnPF3wZoA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=sKR2bavD24ALbEvv0wN-dcYP0GnSX3__5ppj7DESd364BahKCXbKXnnOaUfSs4V6zqNO9V2y9XUH2YNn4WNbRlgH4ePc4-VyryC87QLrvyuyW-e9s4FBMfAI8h3w7aX9zIh4v43lt4i8sB3qHAEZ-cH_h1Fgq0oNGCLGCwZlMlRop-V8ecjdtFh_GnuD4rbjFbu8HpBCVZ1Q__5Z_d_NfacrERQd5JOrRr2bl8HPcDG3_TtHK5ROiCShUWGI8WZsqjdtMHosE2xKR1ZYWnq1j-jHltCaH_u3sEEi_h8NX1if768JQH1d7OUqEgDgbX268PcFmhKDcq8_OLq-_67yCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=sKR2bavD24ALbEvv0wN-dcYP0GnSX3__5ppj7DESd364BahKCXbKXnnOaUfSs4V6zqNO9V2y9XUH2YNn4WNbRlgH4ePc4-VyryC87QLrvyuyW-e9s4FBMfAI8h3w7aX9zIh4v43lt4i8sB3qHAEZ-cH_h1Fgq0oNGCLGCwZlMlRop-V8ecjdtFh_GnuD4rbjFbu8HpBCVZ1Q__5Z_d_NfacrERQd5JOrRr2bl8HPcDG3_TtHK5ROiCShUWGI8WZsqjdtMHosE2xKR1ZYWnq1j-jHltCaH_u3sEEi_h8NX1if768JQH1d7OUqEgDgbX268PcFmhKDcq8_OLq-_67yCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmKTL0gFN-QO1iIGH5zmBDAXkYp1egcP5qEZ5oBxkLzxGyhbFo1271V_pjtJyyXYy7JdadKd71nOR_5qI6UOfvdNwuztAl7dJcJ7Ij2IKnckIgjO7z2Tx5Jt6XjwENfBc-2zkwcTCUu6fMDkpwBB0La2ZzW-RPs3xfqhQOzoMxPPfMBdhnoOn5OOgaBaqfGwH7yRONJZyi2XdENH_lH6Od3ggBWBBy7KlF4qhH4HaxUBzEbNGVFDNwPNarez8D9Ar27L0tUitSgokCHLafz4U5l0pTl1xd_Z9hWscaA4piHwFDsuyWnw1wK9dGfE1QojBG_mjkLYFZ_3MCahe9jcZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=Wm8i_oCnxDwqazKmZSXI3qWdfQ30UkclakDRSe8puNmleArsqHQibzngmPs3_-3BZXquuK1ilvt0GkMIFYI-RpXTUXeyh9vqUuguEZXYmqGIQdCDZoIE68q6G4CDR3PHxzxlhACe5N_trhkzaMnq9qjTOg9GBEuIYtYzwp4y4EqqGCsEVmge0WT7adva4vPQcCH815X_a_7JctEglkzS2g7wNsItJMi2BcWXrhqh85VvDHvbL97Qu7lFaOXSbnAkjDrTle27aUiYTybzZ4d4a0ETflA0RNw4KShbvurDXrdaroiH-yrHcxokmOI8JhP3yVswNFNLE5A_jaIj2Yq3BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=Wm8i_oCnxDwqazKmZSXI3qWdfQ30UkclakDRSe8puNmleArsqHQibzngmPs3_-3BZXquuK1ilvt0GkMIFYI-RpXTUXeyh9vqUuguEZXYmqGIQdCDZoIE68q6G4CDR3PHxzxlhACe5N_trhkzaMnq9qjTOg9GBEuIYtYzwp4y4EqqGCsEVmge0WT7adva4vPQcCH815X_a_7JctEglkzS2g7wNsItJMi2BcWXrhqh85VvDHvbL97Qu7lFaOXSbnAkjDrTle27aUiYTybzZ4d4a0ETflA0RNw4KShbvurDXrdaroiH-yrHcxokmOI8JhP3yVswNFNLE5A_jaIj2Yq3BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=mTjtggaJKu0vJB44yG-vGfIfAD-Y6X_iaW3aZlarpt4-Qm23dqCB3zdTGzULpWs3lDnfxO0hU06XY-Xk2dg7D6lZAkDkob9atRB-Es5ks2vKdKLEpTXKzsXaXQYyJdtc6OWXI2oJodo91w5UV3y-bDsJZmBerGyHf6ALZqDUlvt5PLa3VOb_AA_IFafbD52OjQ_BMJvmq4T0f3wVpMmY6_U2g7aliazAvVcRPGuev57qJ2J33xt5VCn4Hqd6WyeQgAYnGSei__q0ulD3gwFfnBjD9c3NV_qjvjxCwSgdjE8NMhv0J6luqeQHQCFaWeledv6AbPQHQsCQgRtE9IH-bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=mTjtggaJKu0vJB44yG-vGfIfAD-Y6X_iaW3aZlarpt4-Qm23dqCB3zdTGzULpWs3lDnfxO0hU06XY-Xk2dg7D6lZAkDkob9atRB-Es5ks2vKdKLEpTXKzsXaXQYyJdtc6OWXI2oJodo91w5UV3y-bDsJZmBerGyHf6ALZqDUlvt5PLa3VOb_AA_IFafbD52OjQ_BMJvmq4T0f3wVpMmY6_U2g7aliazAvVcRPGuev57qJ2J33xt5VCn4Hqd6WyeQgAYnGSei__q0ulD3gwFfnBjD9c3NV_qjvjxCwSgdjE8NMhv0J6luqeQHQCFaWeledv6AbPQHQsCQgRtE9IH-bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDYEBnaRnM6Gsyw_AHm4TiGODZLRmPOfDWRi4DznwZyuZgDDJI3AA9mdS_uMI0czIPvNMiALF0OQEfW8S2VMNsSuux7TXr2EhT2ii-qDWa7KG3X4x9Af76y9qp3fdmN9WhkQBuKyCDMs35Nda0fTNUqIo-u-UeeAzwLMsQkHWJtrQJBtdKvOGccL5c5k3lhehUffV35ROyIHH5Xn94UxO3vSeF48MZ-2li_yhK07h1dqGWbUw2VkJuLonPeR1JocpArQ68OO_aBLHoSWmx-6IndUIBMborY4bfoajLqDX0Fqa2Sxja027RUsHCULyNLlLP__NuuP6A-dmIZ3ZWAf2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZvJGOy7nVKy76n1uCjwfDGnM7cLm4YPSarhgwKLP4s2ZbbQxil6IwvkRJ6Jxpahiy8zJpieyLykmAYGV3dvSNEtdF5ltn3yW1Jf66KKEhs21LbtUcukU09y5KUZFY48ItlnDKVYd-fnUF3_heXNIo4L5Hf9ZoJyUvC4I-PU3sb1TljX0CCRjDOqX3HWr0ZiS-YQy1kB6a8T6FxEIiSdJMy9LZAJJoRIizNV5eHG2Q4q6EUqY648p47TkW60y8-1Z2xOu3somen_gQA5PaM09y4S1HWxV-zjI-PWYKkeAiT0ESZYTz_khQkt13uRYGAC-3AaCd6snzUOTf8GZMiNnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=G9W0_IvXHh7tavACNpOKQj0x7M7_0WZBzqYjdAOr8JbPZhMpEBlgdWvXpUsOYJTOiCB18Fy35nOIRWcNl7gIiVP6eO401aczhjGZSbwmnSZ25meGxB_dea9XyvrzdA9qliyD0BbcC2DchjXm4F7qmaN8ex73ifNn6mtr9O2eHSpMlWpRhUallmmV-NYn8BciGsdQJyP27tQci4O1NAdejWpzYPnyoOAEmyftVfjTUhfjC9-SCH6eaxXQrCv82VdHS3R_nfkfHTsNBde2LMU2q6azHdHTxyWiSBA0fWs3RDhKA19YiX1HCg-rpP2FAkQUVjk8v2ArDJn0ECgijIjWgqmL4-K7ue0qYunZf-go-3VGCGwOMN2oqd3WsTb1IaZ-GzAKpc0bWKRjob2pZA7L7Ok8xp4Ar-7ycvFIjx-Z2dQ0RNTKdpa9CiJsn151s8jwIw7AxKPPeGrIADSW_la_unPqnumbmKuLePGtl5hiDqogkqQNoERhXuWXgZbz7YsecIyhLbn5LQcMvfb0JaYy89TN_bqPmH-lp4GEL_E90qs6z3LB-JMhSciZ3F1L2M7WzSdwApiPCHKBAS7b1wqyGhxMq4ILTgf24amtQkJm8Dftd_xhm7bSfQaLcRfgyY0MkOuEo6LJMLShVfpGPbeeTDVFKVilK3yD0eroG3HeeKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=G9W0_IvXHh7tavACNpOKQj0x7M7_0WZBzqYjdAOr8JbPZhMpEBlgdWvXpUsOYJTOiCB18Fy35nOIRWcNl7gIiVP6eO401aczhjGZSbwmnSZ25meGxB_dea9XyvrzdA9qliyD0BbcC2DchjXm4F7qmaN8ex73ifNn6mtr9O2eHSpMlWpRhUallmmV-NYn8BciGsdQJyP27tQci4O1NAdejWpzYPnyoOAEmyftVfjTUhfjC9-SCH6eaxXQrCv82VdHS3R_nfkfHTsNBde2LMU2q6azHdHTxyWiSBA0fWs3RDhKA19YiX1HCg-rpP2FAkQUVjk8v2ArDJn0ECgijIjWgqmL4-K7ue0qYunZf-go-3VGCGwOMN2oqd3WsTb1IaZ-GzAKpc0bWKRjob2pZA7L7Ok8xp4Ar-7ycvFIjx-Z2dQ0RNTKdpa9CiJsn151s8jwIw7AxKPPeGrIADSW_la_unPqnumbmKuLePGtl5hiDqogkqQNoERhXuWXgZbz7YsecIyhLbn5LQcMvfb0JaYy89TN_bqPmH-lp4GEL_E90qs6z3LB-JMhSciZ3F1L2M7WzSdwApiPCHKBAS7b1wqyGhxMq4ILTgf24amtQkJm8Dftd_xhm7bSfQaLcRfgyY0MkOuEo6LJMLShVfpGPbeeTDVFKVilK3yD0eroG3HeeKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxZPsaKoMSk6741I01qvXuDLV5id7K70pKrjcVtPpRrLSBPLJGBJUFRTRCXpWADhsRAqRM0QDaxMwZ9Rj7lVmAVmPHb5NRsRms_m-EfloqIDhofW8PdxGqBmwcTwFYTCP-eDRvnUAAt5u7Vo-o_5ZHROLNJwFptkXdyNeRUPMBuKRNxwvDOVDphoqWgIfbFG3hOImZOM1vpVislrgBRdNZZTcmfT2B0LT9d2g7joEVBelinpCZfznkE8yXjJ-9o7cN0skvhFo8VxsCccC0l4ZxRESipi8xIKutI8cKCoGcQhwiyWaEOT7aiJ1eBIA1_OjX1hUmcJqydrf42FaX84IQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=asXdpgbuGS9_BnNTdB0HXHCXwW1A9ovQJiuzk5yopQdIYXk3R4Pkp8gFMP3D6trbLqx4MV4AQ3AxMz-XMO3VAFl8_nKtFs90n7k8URyPa93H0S8kUEbMcn2afH7LY9lDytkoK3K4ywsR4a2zg8lLtM3EmJTSH9m5eH1DJKo31zon3UagMg6YnSXAe68Y6ONWcZY8SSVZ1Sfb2RXFkTwFpiJtvoK6xeC4lxa_FnrGC9rdeulTqShzZ0_hwpC6CdU276Y34VI9rm6FYPS-6LavWulxg8L4WtMwjbQhCrmOSIbv209Q2T3phyqxRvWbWSp4RElS8jcGo2tsdk4qR1QoZ4gC6gwNN5RQr_qhmdvELU0e6SN2Jbq4HEMOMQM3-ETmxu_ifu76Wy53ateqRkJtoZfFo9Zdnhzoz8hl0s3xrbgGyUeL1zEU7uclhe9w-76g4GN6XpnKWlJYKf2BtbkE0yx5ORowFsoyGn6gzien_goV81IBZiumavChm7emQ14dVwAf5hi8ceCyqQfELvSLPlOmac4E57mJ5xk0p2aMZ-mORMuVSVo6Cp8izZaJ2YT5a1LEmnP8lidct_astIe2S6IBWAwVvuTKahHh9MJ6ydrbqA8nOx0F3Ju-UgFdmSef8MAgiZhxwo832jeVBjeIx1KRtSlNx14HB7xWVyTdzPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=asXdpgbuGS9_BnNTdB0HXHCXwW1A9ovQJiuzk5yopQdIYXk3R4Pkp8gFMP3D6trbLqx4MV4AQ3AxMz-XMO3VAFl8_nKtFs90n7k8URyPa93H0S8kUEbMcn2afH7LY9lDytkoK3K4ywsR4a2zg8lLtM3EmJTSH9m5eH1DJKo31zon3UagMg6YnSXAe68Y6ONWcZY8SSVZ1Sfb2RXFkTwFpiJtvoK6xeC4lxa_FnrGC9rdeulTqShzZ0_hwpC6CdU276Y34VI9rm6FYPS-6LavWulxg8L4WtMwjbQhCrmOSIbv209Q2T3phyqxRvWbWSp4RElS8jcGo2tsdk4qR1QoZ4gC6gwNN5RQr_qhmdvELU0e6SN2Jbq4HEMOMQM3-ETmxu_ifu76Wy53ateqRkJtoZfFo9Zdnhzoz8hl0s3xrbgGyUeL1zEU7uclhe9w-76g4GN6XpnKWlJYKf2BtbkE0yx5ORowFsoyGn6gzien_goV81IBZiumavChm7emQ14dVwAf5hi8ceCyqQfELvSLPlOmac4E57mJ5xk0p2aMZ-mORMuVSVo6Cp8izZaJ2YT5a1LEmnP8lidct_astIe2S6IBWAwVvuTKahHh9MJ6ydrbqA8nOx0F3Ju-UgFdmSef8MAgiZhxwo832jeVBjeIx1KRtSlNx14HB7xWVyTdzPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGuMEc2gvcbQHfkgHApsBw1ZcUe9EVWbcXcW4WA-roYH0JbCOLgs_JjEWdRfM2cULT7JMrVCtJOTs61yNX9L12MUWs31w_QsyTgyC7JnN-uw6cgBq4hkRQwOHRPw7Ccb_JiqfLsoqPbZZ-czTgEF8RrxeWZAsL3iyLXPL6NkqbmDNs671glBS6mpErLdQh2IjqrQaskaHFtCb3AvnJAb1Pnm8l6pZPXOSUhT6WvTk6-KFkyMFyTxVedhnK15Bx8Cw23aStZPr9FOzb6KIiKxl97jS60sE432rq50pAfwI-xQR3MO2hwx3tCn6Xwq0HWomPRSf3dP7yGi1xm1CT_ZXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhkb37hA89ZTQS_WkQhHWevJnZOSaRp9Ayf4_SWVI-z0zL11C7B3KWCHgxPCh-lZbdLQjOmzYtLiYXvr5mWGmMvxpT1tQgs_Y_6VNimpD4wqBamOb82HwXBFjQSChuKWAgqIcokUxMnL2Fx2cMmx_RFDngcDGjIIyXJsJOEFjjF2ZTDq4UGYubFyiys7rtdBXaQp6DmIhib2ofPJTYGFnxEkuMZlO3K4uY00ghofTjiYswhYdViBFLl8Zlvt2Kzhqvkhaeyn5POAolTFwveLVk-a0WsrAZnS4_8RbPCH-mgF4ngZ-O1X2LZ94bhKlI1mLHOkIBWuHa2JgRSultUXmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8PirECBrrHpSLxjhGI2gnjX0ifZnUUtoseZ3byBkTMlucYlJ3j2VsLKyOCHuXWSAWoUdjGHM284_Eus308i6Tqi4wbIc1KxBtKZxEty5FKO-utS-mbF64Mhi7zDNP_zdbx4IPA_05fMfkao3HptyPCEYZsb2jyaJ0SkaTr2pL33jdi32lU9OFgq1Wzv_2vG8MAuSWPavvdQ2THWklWI7sgrdICHhxvr054hLf5afegX9PZdgf1Agi_LhfGB-HQwB7F_a_QsKtrLp9q2kRQvVIyDgqtSkrsGESmMkxxHbxpW_LBdXL93bQDTdoAaFwSKOJbMJ-H4Q6civZN0rtcSEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YK6pFIQ_yB-53FzHyS8q51RFIRUAWUC86fHZ1pkIJEvmdf1AOOX54-yVlEGe9MVWlCMscr5Hov52dfwLOkiNrNf46AKzIf7bhyL01Z2gs4GS6vV9xk5Uol-27rCO6ceuQeK8-KnGC0uyPABiipd9WKmlo2p5bwF3GJrK8TXAQ6KyqQ_VlJDUgzjKF_ABiw7zbQ7xJrip3d-t2vQNZ6v6E5BcxwN100s6OUVf_ytRFpPg8L8tVXGV4If185de6DgbIZWzHNfDnyI0tv-AUOS_P79j505IGSRoys0QUwW2p-wMHgD1WXqSkjhYPWe8ceOrN3mP3XWf0E64nXJE6oguzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hj81j1G5jKUjbGDJP64n_XdOVtoR2o8orMIfgwysKUc-luw-Zr55bK_Tu-mrNLKfmv-zvLBJRvpMpwsX61YwlSz9tWA9MxhKn5cw4KPXLbkFrulbB1ryb31J1NjFr67RWPPphzk_p7ikcTW2z0Zr8S25bgXjbt5d2OYvmo3El9pwImg84fIw_Xqz4vMytgKdtbEqE1jJy0GCj0sToVmwrKP69ybpHhiD1XMGQL4Ex58tUv5jvlWJT8mTQ1Ljks24UFx6N2Aa-LRLjbJEozkPygX5Z19lLbIMA7yvN_uwUJrLDaPyzS5ruUET9x_EU936rwuqkD6L63npyTQGCTF4aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohVzRRAenn0jboByjdb5kZrsbN013BYv3Gv-R4E3X3KUET3jim2X7hPcpetkvWM-2rXJgHjI01HPih5b4pHsowOZfAZ7gXBc5d__Ki-rIKVE29ZCQqXL_kMNMb9S_v9E_DKGwzb5zQ03WGXF151yIJLCj6Gp2rdyHraF-WQmI04qYdFJ38Eo0T2bq4lWcLBrFpkD09LazsTikeUEKXal7g_Q_tvDSQimXEYCblQqfghWzNw8t-tU3WGytkY0JghLcFIuZfrVc6xxyZnCcLLu5W_o5h7rTK2d1oWeaqvSJxOEvyaHa-Pyqs7aOI5Yw6OrFyOGUr-1kXPNbaIx22Duyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNLG98oDcjm8xmqRTJR3n5dIQtb-tZDwEdI1MDiIfO--QWUp5Ul56Q-vnN8gdbYHYN2tM1zxGqx-fSGckDJiuK54wxTz0U2xq6RRwU2BO_2JXDc_H8_vam1E-97JdCsXfAlXqvX7wmF_JzxXl_V4YAhTYRs0WXtIUGaHTK_m_kacebruFElJNpwdWHAb0M04Fj3l3Y11tm6zoSLBR8aj6o8gNMHgcIXhmw7YIVdza_CwQCvsq244w80rCQWy_gGIKS5f97HIzHl0LBV8gegWO2wFY-TPmw99hU94HpIjA_0j8dXPAQYgk8G9bgxd1p9YJYdOI4M0NC0Z0nJ8jjCN6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUwyHkZ0KHg4zMhbQpnAxEH1iCmh87k8VhGYLbnXU_WtI7BXIueiiqqodY68mpMFVk2PJ2kEmES96OvB2jV193Zx-pi_HUUUJcaZvVB5iUldDwtZLw-MHBoAdEHHCcMZVrEafy4jOd7l1P1okqJvWK5lWoqe1mc_fyXYVKYByjk0Sbtifc5h4UhxvOFdUsKwO4WATHdPUSUdVwTfnK2C6XKdGVYfoIJaWSQ_O-fl7zP0JjcDE2u8Z5X1if9YU71lY_GnUHwBG6Y-r6PPhbD1YAXIyvzSebzDol3kCk7cUQp1JXZwR9IGFRnn-UU7Np7BtQECRqImveTgFEYtDEaYmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIe99SoeGLukrx9lfXmBbe7iNnPMqa_-d-R9UHmjZamNFwIGXjav9sN1cZtAWJzShjCO6ubPci13s8UD_HrO6k1zZDxplx19rWLpMTjt_Pk0xig3no1FBulKK2rbG_EvL1h0Q7cfbCkAvTPJuZ-8iVC7iXjH-kFrzVpBcJ-CiTJDVitvUgeMpIebOIxR5ak7uTnRm7LIT28sd-5MLV5d6YvNhupiot7MGHeE_x-BSE2AvOtDsb9gyXu3Qzxhmk0U8TmM4PhyWp1cAb7tXZTqFSkr8-DRxsu7TTI8LGzXgWM-Kct7c1M6SeGaZghqM21O8-LHodes75dXdIZJJvrKhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSonDH72YVRyDxDqnQPLntB6LfZNaIewq2zQmdLI4PLQKqo7nNW1Wcd1HafrHM9TcUphu_bY5W0o4MVqoJOwXghqT4tRz04AlskXF85O_88EnRv8yzvES2TMCuSuspFbWy-lwgQJQM5qaJotPVBPocOLIZbAqRy8VX4JH2sFW5SMhYGhISmm4ljUEMecnuWjWG3X0mVjEeavvXxcMNxEh9UkS6pDrvt2tpk1P7NPoSXUyBHtyncYyTP16FfyL3wzbjaUuDuwf7BguSR85Dea6dZ3WoHTo1XzOqFktJIH5BPeH76TR1dtnapEA5kZgKuHaVPz-4WAfKcgUFX3w50NJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPy5um8_YznMv_yE8J_qEI6LBhDG0kAeeUT7BGDjYO_qraAJyu4ChM6zhWcvI6MyNlMlSbRZDvh3vKtQKOp9xCypbai-H0MplzZ2L0vciAXjGH4N1crB64Xktpa5_kSrnrKsvTzQbKAm5XRVwQGleEqtlWbGzYCyEm0bTIiy0H2MLyMDh3lxoWrQfG2SYu5vXX2lCdlOsShoHCQZ-GzSIg9qS6mlT6RkrUE-qLLYhs1NTxc51cgB8J28sxa8zqCkYmQo84cDbdVmhWq_JkjXtuTSgBD8R_jU_VL7FejiJ8apJZQwsg3WtGb3H9BilYAhG7kVOhYgGJMReCF038iz9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeQC6RBxBB5g-HCkmQ7XWH8p_bFH_0OHgo7wmxWUybrNO4x3dOLNxRnR0PxFZ9sxc6dALxsJqUVy7RQw2E8I9eFarw4XlxuzhHFJR60B6fJwUTYbylizQ4vP3vjpr-p3yBgi8T9PihK5L12czYdrCbWGcbeGsZiMjnwbareKbBSVm12bfswdYMq6knQOzL8LbHoA0G_6JXqEgT6moAcBpHyRBnrvnZwgqnd3_HG65dQkcAPZxOscWwX6pgATITG2qrE8XMBnLh7CvDu6CPP2nbDpXwm491EpUbyonLM_jPQyq5giV7hOz-EStDRTHuzUjGM124G5T0C_FK2C_Vk2HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcMbiWiDYkh5xu2likxIyF13mYuHjfJIJVPM86MSIjQe9bEt1PvjSlQicGtIEq9hvIQCRCxivNP_lt_jLc1DjEzmfOqW1QLi5bVu2uhGDfQsBbxIBB52W-zu4hOdGPAJpvqTJ632pobcU_7qGaaVuK9wyHCud6DFQjU1UVekpPLjAiJ9_5BStgTBzBRBcE-8CfBmU8GqfcrBW-2XZCh80lDCyrzrdEAd7clJcZwkibYOnTfoh4Y0bNI1fYrNxkm1o161mRp_eHeETGITedyU7lmT2NdEQrr6IaW4t2kxeH-b3Pvmrn0W-ZKsevMZSUb9c3qj5b1pXHKYSw8Xg2wSbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl5Wxl2YmkCwR0zq9eynoJhacAwTuyADHA3h7gwzGyA3qQLsTQK57xh104R90p3zcuU61oj_8-QWnER12C-wX-J0SkY3jvz1FIZMtzCOp8-oCVQbRUQ3SgAsEvSlumSJoOSRKxBNQleDzSAZ7OomDSE6kWNVXgmzWY7IgRFoYIM_X9av0WyEVgdM6BFPgH5OLjlEJyGaEBU0e_4mdsAiLeS937JI8H1afxhYdgAi_ZfOxQWfjpqBVDwGIDX582uJMiAaHfQqmqOLOoEl8YwoViLChWkB-eZuT7QgqYYrXKRWQaBcW8f1HsiNbywBv5umWMY2G3jZnhlthnx1Uzgdtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFYlCtG65b0YBsTReZXMd4Dk6PEFlGmGzEsN178gAG3k8b5KwVfXh6DXdXZ4OGnazpYeZYLC_O74aeUDp11IST44x-QtOG2z5VJAN7ahGBT6Dmve2AVLkKFrZom27izt-ptJCWcII-86syO_n70V5N7kwe0gSxmTBa8bRWxfNGk0KoSIlZx2-O07BD_hVx8fTq9V0KxfuRIKwMbGihG-CFrtYR_nczok0f6-pmYhA3csJL_ebrjRieKE84tUcJ5bfZko2_ORkc32zOoAOWq3bxfvn951jRMlNJoD7l2JPCQcw2hzdURfNJLEVfj64PUnZLI27XwxFwKM8zCFUcc-Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFhSvpd12uRTd8rK5N3bvb4JAmQ5kSniWOa1_mqhsLENSIP3eU0Tpm5JgvlkFqP1sfotHKYD2YWKf1p6Dz7iTC733lz2vpwF5Z23xED756WNTfVkV35BD9rdYrBnfWiF7mrzXOO-et6rgPCUxtVGRXZNVFxJNZnKiUj-PSYluwZRwO3ew2C8pv0hhhH60keigyI9eYJ3pFXDUivScEdLRYRtGc9Irf9HxDY-JqlAbbwDosSzanopl2I2iU-QEYbpb0JNzRemRXwYY5cYxOgULoroRamegNitjFsRA0-p-9mhL7pFX3XPJAJbaNFvSnXkChDuWcw0D56ORi0l9Z0djQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cEkunHWN1DcfLme7nPEquz4HQfMtn6GZfVurqCG3zn3xNjDSRb2n0juKO7qYlNXvRCMVI-GjVij-MaIOG3Yy5wWv5bIyPoUUjzuRuad_mY12NOE0M4dVpCxjW4-cM2yvqeDov5G5fm6WiWteJT5VbZzgvOUWiqO1GmJ4Z_zIpIXiv8WsslMlt_ivQpk3rvzgCiy9OjaT-uxPB46ThGNu2I1azEvnAqwZzNiW7ql2sIxnKKkDXncfv-oPFOzDubfy6z134UdtNm8wHrI4AB0m3tS7ZW9WeZyQ8IDlifoL4GFwhnwnpq6GRlMuQidS9_-ILkgx4XAoe1UVfYZLiufCCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sK6ABeocSSAeGhK2-i0E0LXYQLYziWzXPYIG9qu8yJNKSRkdgaKPFpIHErgMCiC6yNb3SgTvRca2nXY7y5ZU-izzq4AQ0M82A8x8ggqAARlh7wi3YhqQDtYnx5QbetaVomK27Pu_SFCZCL2MwSLh4dAB4RTOMaqJhi7GuFpnYkjK-RPr1INIAOXbLisAXC_bXH50b8EEsmUVoXkj400PcpUJT15Y9j3k91O1ve4RGjwx_kwr-jWzoKh37kHh-RrPi5QPqsxo0_Gitd0vBeQ2FdAKSJrpCNFaJ2dBBHMqiaTCCYb1RGpz5DMvGQWfMUpwGIlKCHRpNu6aOWdQCdpaxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yyocg89z26scD2mGkXDKi1HgWC5rwgSBSW1iJtHqNvYJwtwF6nPfb6hAOEylUb0jDGNIDHGnU-OojLjZo4K8T73LIMFO2AoyrPjyS3_W0xy8mqiyKNE3NmYyo3zC488_n71WOP8ADF9VVBBc97QJGQdw6vgybWXLG2g1E9wz7loGfOXODzdhxwfBsLJ3SdTLp3L4ZTuRk9RP4Yh1-VKJP55v2ChAc8o9KepHxGcvo7hkPpT8z8ru7LbPL0eb43SbT1GAKePqO8W_jhUYMq0q2Y7UfZcAkIUq9WSiKp0rqnXWRBvYeSf3tMUswpvgscCCNCBfq9I1lmrc5k3ZqtWGdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRLkFIgFiW4VbxFSMA1HdceDGt4apZCElArBOmpa8psZeuUSOg29AqbM_jI1Eo6nMnmgz64SnmtOgNaAtF-dRjlKrs1PSQhljFkgt2YksDLlcHNgo4AFjjaRUhTu1YVVlP7-vVuQdw0TQsJogkz0ahf-bewjMlS3PnhYkk6LHCDwo_yvTf8fnQhzDnhbn9JG-g9CKtBxdNXwsZ8MY2O8scgyYxO7njl8ssDqp-Ss6aVFPv4cyuNo0aQYQbDTjGRqge2ZY4tEuGGsMK6PyKKbRZKxT3yVqJaPMbP0cuWT7RcRCTVHZZRxXjvda5AjEejxl5gtoEW4Zg4n5elkBGmOHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFboREMzwiPBwnNk6f7eUb9qganjU3-tOpd-dbGnJyEjJyR8Sp4DjBy9DZbuXmMhXobKW036clOeyNZy8hnbjFw37-LZs8Yqjfg8jFsp4GpijZQUCr2CGbeDc2kahMI__ktzoYXH0V-pyo0wMePeSzKS2OMkGML_60h_GeCXfneYy06tu2Nj3OXLEz6-S5P944mCARq_hjc-BBOuWOLLx8X7JZMD0l2TWKHLbJeuJ0s4GuUPE0Be1rBS4IxMDVQRSWYBv7UvT-YEL3jc1hXWWWQZ0JzXtkhTBAJcWmW4LDFQaAz3UqKaYuVEUPodfVO_1cDsGxKzRjYNB1dn4RaaCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ee2vL7_9YzuHITX_FQtwLIU-6eg4HO3__n57Wp4xtNH9bxSYCAfg98-xdBC7VEUcOY6LCzm9iuNBoJWzrKsNEuDfQU6UlYCxyOh3W4HF7oNkYb1c-Dtsc5FsyOZ4KXHv5sbkCc2VWTp0vsy9Uph6u9jyuYSjTcRcIPiCiJjpKTR9aPzTgmXVOhPAlXC6f-Jqs7NpXt_g-nsDaKIknpNBCKFDO6mtJ40ohELlZgs0SEabwf9U2KXXnX6Hz_M8J9u8uZbNPSHE5kQbcf_lys1SivVGWdJuRimbhniAVFHdOz8Esdy5bm_GlzHvGfpFmGoDrgD6BtXApPyrY-Z1o0E7CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jitWKQjFsYJboqLQjFpbpPnsKeKbl2YzNHB_RjYwr_hkb6FgtWqLmyphMYNgEo_BL17-yr_oaMhNBuMizmVnCFJ7RuBgu4zY8aYSsdSnAL3Wqf_mc1d_WQNf9Uyzi0yHdx-S4mSrgo_is_dl4KNIRmgLh62ukfblnOK7DOogVRDcIviRHm7n2vkZ2tgG8KducGwq2Ya6OCg2FLd_gpUXg5xY7AbWdSYP7YbmpMoWW2fYQ3ZZYMad9b7yttPwcHJNBp6UJnPJ41f2WZh2EdoHNlkjzgE834KUP-gVrswT3OGhOGt2CM6xgFSFpl-OcafqFBQ6zvz1pCvf3wcLTFnP9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3mwTEZKCPVAn3T9miRG32F8Puxn0zxKZu2oZ484msxmSkaRH826-O3VW1nAV6x4PjR-dmcK-SUcA5UmsCJdHEXoNR0ZgLq6IL39r8iCcrLog-IodPE1uk7tBk-9UPLAoXGVfjdlUR6YnIpvdg8KJCpJ8URXD0NnrMMEq-CnEt3pOtNEj512mZSwCQXRraC1Bd60GDqTfrdC7FDPnZ_alNS0joNaWPSQidCRfqvU74DPkeqoR5k-Vmq8T6-ukoMmf3g2f0O2c8UokVIre1_ZNBWnGTobnFR5GX7EVFM_pmDfyGzDoKem0tZDVTMR2Vmn9GrHZxVnLGLGn4tr18ydiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ux8q-tImi-nkMTurUmNIcrOsDCuz6EkcTgU-HpbIMqKgWeulbeHjMVzZdQ2BLS_JS_ikVLHRky8cfKQuc2htDlchH42XQ0zHc5OiK8OHbDkhX92gtKcoyDv1RcidvRpRxTFbEUqM4pb0c8kZZMp_uhmcN993NBm3w84gkytNwbDKGZ0e7UawKuxi7waGxjz0bVtGEkoXfwX3P-Uboj50ytUkKx3O4VdUXz-ox13XiF-FTG8XInMc-PJz68-NdhfLNQbseNsVgj0KCL_W8xMWDqkKs-n0K5D9-moMJeUN3TbHCEAOqbEkG2muWEdXEM8qHJoOOXNgXZcuYOAOuOROqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VppZ_9kaDnA-e1kzlHIqjelqyfys5UliPg9WSimIe9DuwD1OibYJUiUHc20pE0P572pUgLrTTndlAkKjSIK0A6yuYnoEb3eT2TBs-asT0pPxoj1psVeAlL78CKpTZeriO73c93ZB7gFK6fP-AGewAZPbTnjz12mT1pr0eOA5ae-r7IcdONYFKVOxdBRjmDeI9UU7TkVZzl2lxOz1-0iAHBHhh7M8rFIqbWyHD9CMG266CVuBHCnTVTh_z_c_qjxecT-EO8HKuwHLzYwWkuljERJhFWgOsgxNvuUYISJ-T-MLlEi-roNbSibFhLt-2SqdhlO32hh5gAnhiCKP-fkMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDD-sJ9KQ8U0mnlcirXX2vEBeaSn9RdfgTOVrTzbE-o2GadhE_p22DYiyHhhVoVKyEQ5cNSQMEFw9LgZvCaZeGmbh32BJgKVK3tvXsDvgl5gAHe_7SQ90MhcwI0k6I9CkSBRbvuLxVymwoqj7TicjUGTHRLgA5_ak74wVZUoKfUfA2a9PmqDU55104yevL_HeBPbfBsXHnfuFt6ysn3IgIS82Mg0UxFYPJ8RYfzupdKbYWrEKY7KU8lh9XW8KwghzXauve7wBBThiKlA15qzWlpeeOwV7-0fhG6l-4LiNqr0YWVlza6Rqum9nuH7c2l4yHhr_LV4pKhT4f9p0q-bZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4Wsrh-vYB-uT4K1TDh2DfKT6uEh5bF8me90f2JppGLs2N0X_d9Rnb64GF1KPGrjzRK60wr3G08g3-DEFcIHf9Rj8Iu60G4YdLJl4D9sZRnc886JB5fDtP91-x5AA40ATSvZwKJOoUigAucgFHcR8WYnZpNthSYKf6vwwWU8OGuIaSZJj_0A4O--jUiTGS6rXC0Fiwg-DzwaZ8ZDpTSep7it0R56OmyyawXlLUMKgygAWp4iUvtb-dJqaBrUhENRGWMcIJuw9x2HKI2uwfjUKCohYBQXs_WxD4-Gbhir8yI6gCKqTSbgjjCtjCeRbb4Gfl9pGzAwZugIbBLzHFT0Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TacVbk1aLb1PV705KewyQmN2nIaKRi5ibYIymKAs5-IDI0aB4jzj14ac7z9ax84OxR-ZwLGLxTQPhH-1rQfy6QQQI6yVJ8LaGLCEZR46UOUXSZx67LNUiMKD05mq8HulDckT3UAN0oMb4tKQWr0EU-xvOM5ERMnpbcE9LuPDFmdRjRSuPuPIwoKRu208r9NtjpxUJi_2nRjm48WIvZvVYlmf8o49qVnEGza5z9sjGETMayDBAgpyUCzim29FZyKCz-E0Le0E4mTBMl4khWwOZHvErx83C0Ebka0mX0Ij4YrIuzvjTtaRxb7JDIEUhi75jAMoLqma4Z5AMw5iZK-MMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqTGrza2ODjC7hEhRjr8ofZKOrIZiIrIZnFCpuS11wyBq1YFMSKkOW0QlHCc3OfonSrea-niKj2ZOQAWOf_ft7EoVGgSGudDt4dhJRTsSbrdXCsn0LKXBF4RKdKRSda-i8NmhQEG0SR_Wl6HCGzQWoTycivZmbCsXWo9sTXrLmJwqVZ1j0Zv7_UKjs3ICj6qGU9tCx2KT2Uf5fvtd9_CXXhArSn5UbNqETFUGiAYGh7vzXOQfsvu385oprV79aJ7J_1515-mvBqK48kiNB6licVdvYlgKS_qoV-n35KWeQ02puIAqc9aUT5Z3tlWn95oiVnkmTVArMPfY6S-5l4Q7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqHpVTlEZ4-MeRUTe9Ldk42U3dj0xKge1vH23VYWcvgLNnSbsXNtD4nYKJXf-kVts0SiRP2CmXQ_h3Ah0U65kiosp6NfMP-n_nKerPPqDvkNGw5CKcoXzKBEba7ok-sg-CgjQKP-J8tchitXlx_QdNd1oGD2s4U350Gtl6E4sbtPEa9RK-RVMeSLLfIB-kG1L2qX4Pfn4FHpAu_aC0bRpKZeyLyFHY59KyVa3rnqbKv2r2A1cd8ImB8LlbdgWuXDI1yzUipEWjrgPvnkti_PmPrQp4UvwQvnPPSxKKtH2DrwCEKVG8BZmAyRR6q99XW4qp_dm5jEE9TvcrNgsmHnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
