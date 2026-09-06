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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 21:56:54</div>
<hr>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hf3duywbe4OA2wuOP_lLtgEzjgUeP_ELAfHYaeZ84YKHB2v859H7YGQ4WvxLjeuX6u5yhLrPOCGRWJ-FdMsgmH_zaqLj7cJZZPWiGUXrsKPda_OZKyxFEKs9G3yqN0ojPw3VAjgNJ6KmLUnPFLhBcNvxED5v_u4fUtNKB4zz7aZJTlzAgzOlb2eJswpN8HjvYkG4hTiOz6Sj3sZeYY6eWGOOPvrx-F7nnYyjTCetTmO6rkyNvIIswDrXNViUkuycLaNF4cIvmmgq-HyVVvAf_eUmrcXJdPWkPm9pb1_cFD6qoOdg99MzIkaz6C8AQ2nsEwlNBENlyBWItL9dFx0nWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uJjValImkDxm-veeAD2RE8kByE_9sKjhGJB1e4dLxUIUxTaj9ZVkSjcjHUcwqnQv9YmncHPDVHvIqwHMO9ysXWzgQG5YTp20LDFI1UedHyLifyUqr2yt1PUGba5H1FH-ODbQ_KS2q_ZGhaGHB9g3mUGvTxSHfEZsj8G8U7e7tqqi_xWb8c81RR76WPH9ByOMC2c8gB7BqmsXjqhW8yn7L5YAE40ieIdtF8XQOioflMVfBToG3jP_s6T59tmq0KVtHKx1QCuk2U84XKh2_WaUnB56Ibz2-wvYWnqhKHLLXwVVE19vZpJMb5HPoCS4YAo5di736vRj0Eea7CmW8r3zuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9Z8z0K5QN3YjOaLAH-wOmFnnV2RHoxH1kKFUKd21bk-ktwswrhkTbkhPaJoYbpabn2o6jtpH5iEWhiowsTzHzNyooDpoi7g7B53WyvfxXhc5OlvanTVLekSYlUPoTsJcxogMsfOB2a0AO3gFe3XaUP9-rlkphez3igr2RibWU5hHiPBq7aOJxs8sfoDD1e0ho6GB8pkKeVoB4CXvO336FWX-MycIT5gnP3bGO_QfkfuBbPe3dnJNd3l-6GnMGEYksYQXqe_U7HneSY8opPfYveXYv80vX8quL9YyNC1clpVhtDZV7dxyFnSjIgmEfq2Ww2dHM9pC80iPtlxwUJIEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcApaWyesX074CoP3lDbQVfJbSr0AUGukH_KCF1PegWPqAskkKHClkVigxWvbw8DXlZt_XjcjqGey2OZ8Ksr6cPXAD0WbS5atJrVE2mq33FvK6QEMSlk4Ggciw_qdHRL23hO3zRJLt4Gs3V-iE2kCtWBP0Qr5JtHf3evPDbsu-rv-561BViB3tbpUkdHoPpp2sqliuBeIq-fCgkOMM4NxQ9bCWzk3w1xoZjPq1Dus7C7AD-zpfd1ipyTjGpOZ-qph4Zdf4e2MMJUpAcB6nEI4i-OLsbE9S325lGNNo1LAPUFrhYlGN0HNPr0n-GXKjClVKp1ijin5KmZCBI8Ko0GEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qz71eOvpwmWscgntpRQ4INwXrXc57EFgb_SDMIcd4MRC49wQ_C4beG8wCsCBnvpKukaDqv-bmFfPkEg5UWWlDl2kjNLK_J6qjvRUo8qqYHfKxh4XF43JL2hI0KFnk-RB8OWhpqFcK1mspXkiVeeE7j15HJQXW8CBSv5bUkakADafMzbMQIu2hQYhxBFFF2vaBit9wa_d3qYSYbxyuCf0lj8OrTOdu-NT2vlnp9nBvXoBzfqaV92JhFqmdizItXaJ44sYMV6pHK1SohHXMlKpbCRVNqsKKbV5BvWFW8ZyHV8yU4uei_BXxyYQtMKt6Y7hVSRB6ZCkN3N_4sjE0yXhjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=k7RrF-KM-sArRMvGL2GW5NZFPGF3kyG4wV79JtP_w3rj8l7S00j-IcxkMpJOeZRZUDoyHd0lNIIp49dNhYlCVB8nEedBa04urOSNFZB63hw34t1OwNgz3-_36m3pYghLokbBR4T2I5uGl6Gu2RbcFq1C743WTTyswvMFg6KSFe0hFuGhBTjwMZX8SlZTi4vBWyysxZYkkZuDPuKRdAYVFqUjDFHImAILXNHvG5V1v6m12nV7mXygpCNNEzNU-VEJugEUd0IVafqaEeIP7BTy_hFC9MGcdRg8a6o_p0lRs66OoAfQ9KgsLc1cYjCsnf35oadhNTrkbN8Rhsm3BWwZUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=k7RrF-KM-sArRMvGL2GW5NZFPGF3kyG4wV79JtP_w3rj8l7S00j-IcxkMpJOeZRZUDoyHd0lNIIp49dNhYlCVB8nEedBa04urOSNFZB63hw34t1OwNgz3-_36m3pYghLokbBR4T2I5uGl6Gu2RbcFq1C743WTTyswvMFg6KSFe0hFuGhBTjwMZX8SlZTi4vBWyysxZYkkZuDPuKRdAYVFqUjDFHImAILXNHvG5V1v6m12nV7mXygpCNNEzNU-VEJugEUd0IVafqaEeIP7BTy_hFC9MGcdRg8a6o_p0lRs66OoAfQ9KgsLc1cYjCsnf35oadhNTrkbN8Rhsm3BWwZUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=N-NILdyKEyXNSYvSFx3rFgVsoXruAkjn_yBx5GQK-cjK3kCWuz_aaoEjrxgYypiM0sYo3wzjEyroyr_wZ5CrMY1gzAsb5-yE3IKG-pRKk5RPRYqM6s7GwhfhBgfrh9qeKEU3QH0UBXth0G99ZbbZvcCHED0yeHe3kajyZpAA1x6AWiPpWZbfDuI5e6gbJ5wjrLepknTEqhsOuPrPGyAjR-8JxAzFAcrk6OlzlXKhFN82Q24w69wwCXxp6WX6zfhsJg1xOyN9Q3WQR376iSo7pu886EL8V6sUEMWaMQhC4L7g8JacQbcnMvL9onyRw1rLezglV84Q7RaCrWY0mK3WNlHbmE737_84nb0FrF-2XT7pLHgpnVsRv9KKOn3hVOuLrLcWad23XkixEirNpF2Ewp-JUHwB8xW8gWpNZ96OcwnOHZ0mV3hzxP0_d1TDxaE02LowdK-xtu10Y-Hw-hwnqCdVdB7Tvds-LhWm5ZXbqQ02gWG_uPK4ll_-yewtBiSHcqGH8XceDIh7lkrJilQI9xpjyPRuhbbLECR_rCZMLYrsnCjZMa0LtJfvrIdL2LfLd4DT9CNYugpO6bTBWsFGKihPLvv8rUvPMUoJQRMtj1ILhIAnnwL7p5dP2dbbKtCIolTrRQ1PhMJq6oDJhVn3_tkL-QLjDu-Et1zulxfRLFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=N-NILdyKEyXNSYvSFx3rFgVsoXruAkjn_yBx5GQK-cjK3kCWuz_aaoEjrxgYypiM0sYo3wzjEyroyr_wZ5CrMY1gzAsb5-yE3IKG-pRKk5RPRYqM6s7GwhfhBgfrh9qeKEU3QH0UBXth0G99ZbbZvcCHED0yeHe3kajyZpAA1x6AWiPpWZbfDuI5e6gbJ5wjrLepknTEqhsOuPrPGyAjR-8JxAzFAcrk6OlzlXKhFN82Q24w69wwCXxp6WX6zfhsJg1xOyN9Q3WQR376iSo7pu886EL8V6sUEMWaMQhC4L7g8JacQbcnMvL9onyRw1rLezglV84Q7RaCrWY0mK3WNlHbmE737_84nb0FrF-2XT7pLHgpnVsRv9KKOn3hVOuLrLcWad23XkixEirNpF2Ewp-JUHwB8xW8gWpNZ96OcwnOHZ0mV3hzxP0_d1TDxaE02LowdK-xtu10Y-Hw-hwnqCdVdB7Tvds-LhWm5ZXbqQ02gWG_uPK4ll_-yewtBiSHcqGH8XceDIh7lkrJilQI9xpjyPRuhbbLECR_rCZMLYrsnCjZMa0LtJfvrIdL2LfLd4DT9CNYugpO6bTBWsFGKihPLvv8rUvPMUoJQRMtj1ILhIAnnwL7p5dP2dbbKtCIolTrRQ1PhMJq6oDJhVn3_tkL-QLjDu-Et1zulxfRLFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=MnrpiL5WvGjfvfl2fV29F9SanSukHki3LYDl7mKPcgVdu0_k_N4Edd4Hl3Af1cmZgKfajtI5-zf_vPGmgF9g4PzGuAHNJLs9qMFPRKdD28IDrjQHPGUMVB4b0k2AogDElx5MwUKEjdcMql5yEnXnstDTnv61wxU8Bb887upWKTEvtqvPNtJX4DP83JAo29elx5Zj-JCaY1w0iU8vCAUoWUh4wrDZLUO9n9Zyx8mGX2G4_-SNqhh9DNew9IJ1n9n_OmujYCMgEakBxORFKfTuEwv6Uwu5K1jgkSw_e357JoqpKNGJJTjYjO7Kwm6iWPZ1-i4-GIedIqh1myZ5CxUhEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=MnrpiL5WvGjfvfl2fV29F9SanSukHki3LYDl7mKPcgVdu0_k_N4Edd4Hl3Af1cmZgKfajtI5-zf_vPGmgF9g4PzGuAHNJLs9qMFPRKdD28IDrjQHPGUMVB4b0k2AogDElx5MwUKEjdcMql5yEnXnstDTnv61wxU8Bb887upWKTEvtqvPNtJX4DP83JAo29elx5Zj-JCaY1w0iU8vCAUoWUh4wrDZLUO9n9Zyx8mGX2G4_-SNqhh9DNew9IJ1n9n_OmujYCMgEakBxORFKfTuEwv6Uwu5K1jgkSw_e357JoqpKNGJJTjYjO7Kwm6iWPZ1-i4-GIedIqh1myZ5CxUhEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FX7fpzUZHaRLWeC_H0RQteuy-Gtf1VkHRc3lOXbb9qTS57F8cBcd3rWCk6EX2-VGTehCDgjdQsD2qENqFwNJTxD_DK22XqtfNzet3-Wndf6AYvGy2W2TM5qFXB85BEY0wLtaJJgWDKwJA--OjXDyM-KQgq0Q-Ov1JZ6Sj42-nAFMHzZZtMqw7Tr5b8onBp4GyPZPOmsBxAUSmBtrNk7PQuu5L96i4YrTYkIRJen96mBpJZZFmIoY-R7ORxZFSlSZzqLAqVq8Ctjj1uAtwQBELKigv3w7iyNebnzHzIlX8vTzOXyy2ELfpSL-TIl-zXJZlwVntu2jq2Kvmg4mpbtmSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=FJ7ujRFWz0Qy6yEUH49WcFZAesl7jAu2IucBqP4P2lFFz3WiZlswetjJzHFV_QQTvg4iOSFJEyLKXDKecuL0Ra10beOIt1NorZ5fc9nlmDc2IgF_sU3zbzY8T32Ev6-z737HFGi48bdCPTHRnbi7Gr6nefWp2Yo00Nl1T7S7KLs3HYpTyXq3A4CojSCpuDUI0OJGn5rIPkRWu1pQB4UOWDW2iCGzY0bj2rVamTB_DTCclps9f-_hnAd6PkuhSHUEknYCgwYDaoyJftLf46EfWkhxo3lx_4cRCcU3dIKU1pJ5tYbZZpsj4SnkSQwMzzQYlIFrjGaGV_PquJkaapD5Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=FJ7ujRFWz0Qy6yEUH49WcFZAesl7jAu2IucBqP4P2lFFz3WiZlswetjJzHFV_QQTvg4iOSFJEyLKXDKecuL0Ra10beOIt1NorZ5fc9nlmDc2IgF_sU3zbzY8T32Ev6-z737HFGi48bdCPTHRnbi7Gr6nefWp2Yo00Nl1T7S7KLs3HYpTyXq3A4CojSCpuDUI0OJGn5rIPkRWu1pQB4UOWDW2iCGzY0bj2rVamTB_DTCclps9f-_hnAd6PkuhSHUEknYCgwYDaoyJftLf46EfWkhxo3lx_4cRCcU3dIKU1pJ5tYbZZpsj4SnkSQwMzzQYlIFrjGaGV_PquJkaapD5Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=Zc43cCpB-itRHpU8hkUBYZydALsaBoo5pWnZxdGSLgGCyhFFoJr0MRd64RAtvB52kKrWOAjS3rYIYIrkrb-8xrnZ0J5kShy74G36Z41VvLf32Pmy-2d51Cvz8iXYSjORRfplSRJyaXxJHS7hE6wOwlw74B2RoHFKrNRHBJiL2wPygb2HdIRJ7Zmpdc8xTUIMMDqHR5ptyItFnAK8lWKxOGYP1ntQVL0z-RUtt0twmGBjYKlsHDKhZg9CLpWR-MDr0Np6MjJy9gvszaayU7ioi7JdhawQ9N3N7QqAanV4IZNpjTE7ljeKzfFTtQ6MqnI5ek5b7xFo9Joa3a2qx5LN8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=Zc43cCpB-itRHpU8hkUBYZydALsaBoo5pWnZxdGSLgGCyhFFoJr0MRd64RAtvB52kKrWOAjS3rYIYIrkrb-8xrnZ0J5kShy74G36Z41VvLf32Pmy-2d51Cvz8iXYSjORRfplSRJyaXxJHS7hE6wOwlw74B2RoHFKrNRHBJiL2wPygb2HdIRJ7Zmpdc8xTUIMMDqHR5ptyItFnAK8lWKxOGYP1ntQVL0z-RUtt0twmGBjYKlsHDKhZg9CLpWR-MDr0Np6MjJy9gvszaayU7ioi7JdhawQ9N3N7QqAanV4IZNpjTE7ljeKzfFTtQ6MqnI5ek5b7xFo9Joa3a2qx5LN8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tY2j6O-TLLgyBQeQ7pCp4I5vn-zq3wC_8YdT0PiLf4RhtkWnc85wDk2p1ibLbiDbJ0ta9ksFwd8sJS9BMDEj8ufsrBpNK-njROT0HBnkEcUOli2mzoMDRvdH8kEORM3lITu1eGnKQO1YF7JMaM9u__nLiJ9YnW1dg3CnDxlCoBAhJeaES9I_GvTrJyRJvolG6i11Ez_VrEKIsHNkctj7GfbEP5unZOh1mxOxwVUdN7FVRN-58XrzrgNuTA1p_H1HvHAVkJhMH6aAXORS4WEDDrPbSDnBypFiMJe-xvP2em0Gv8dN2A9oXP4W1uOJjTG2rn27VDoTIFGPvFSzs0_OIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGRdVYnlcgQZu2TdU3STk8qmoisocNFIIVi2hC1jThaVm9yjYVp5WBln5d3ErzplZLI8R-SR_VTPSkFjMsybEPLVfDs7Jgkqy2a1yeWRu40Pou-frsZpCKA_z5Z5_H6VBOw1NXVb29okErhbNYJ8DleXQ637N3qXSA4Ogg25RQNoIB94LegILKe5H3hq9lrjwrForKPwTnuEJgFfcy0HgKwfvxN-egPfKlkEvbAsF8hCQXm7hmRw-FgeckPWwQJnmqtHCaKmS3Wn3sfreDpg9nZ2mHBeS7d7_C1dFhzFJdUbUuQIsfuricDpfaH8uET7353XBk00wDVeFQJUKvG-Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHvkn4N2VvbWUEmIyve798i9gvLaV7uSzfK46n5bneCyXew5l7BOPj8fFNbYOFTZYdCCxVCXEp8a-ji1kqpv84EUVhP4LlRRwhpkuela4yqYLVatZdqhVnAImhsTvreOcMnAnxVzkoJYRDhQmHP_PMG4j3_nkoU2-LN1doNK7f3wdG69MBFIHgmNgzpkX8Aa43mLYcuQ_Zck511gbY33jqdxlQidtV6JjCBcWVsTr4fXPLHZh-DamZbdkQPnTbIJ_lXCo67u1NGHjPox52D5vg6cqydg-tVQSHdaTXS9Ea2sBxox52l_kqAB_1CvPPOTbux9lPDcAIL7S58otqliaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVIFheZxkWzYJ0ofkB3BMipOgmFrZaWKD2w_GdUxIAITrYVfy-AlcuvH_lqKIkQQfEfyMcTe-2e1_Lr2mNeSMJi06nDlLyO0ECXDrrXytfMKLQ8mwlkZWOqy8cem6-Bj1V3Eu2yI6QgRCG_NHjez2QamX9DVpZsju8vANkfMA0IRV_nqSqLlZcYBRTgQYEqmJcSLS98oGPtCLAlwBfY5J0Q3i8VUe0zVwgQAIp7zkl7dpLX6Bd-1tSxqDi6rCfWBzOK3s5LqGxJEkK8-o1tWxDxbkunL_yho9CwrIBRHXowy8l2OBt_1ZlAZQCnHiUuOIdjFGTP7FD4HFzYKWzC4Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0nJXsfVhva4epCbGZX6YP4sj93amiXLZ-OYdwIH-P1t2lfvfXjx9Kpqo_lyzNmDdYOQWeMyv4xY6n8dGrhp0mhqL3ATvrDrinELNt6CI7bsKMzLCvMi7f0gcPhWZiVgzE2u2rQ9dtdUibHxoTkUKT4SjNMs5DC_ZD3LCZ66eAECO-ermmZbCQVvpZ7XzXrO0wfMhSeEt47AEjScyvT6Ukt11yZEWU4cqxX6du62rPijMtdMq4vzTiAlNfEVa8R0cCENu8OFn57Ref9kI8CR7Hg6KswqrSvaH7cmh8gwWtngMgXikd0UB_G4MM3f9X29UAnoJBcn_iYc5GZzSVmp-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoGY-Q1cn46A8z7-hgyOmGAW4xIinVIwbwMizdDqfBhJiHo7PHVUZReDyaQOvhsDQHAjXjCJqqc-xpT4ahFj-Hs01rjh-C0OA6ejto8jlsU77DCS3I3Sro5-A88uO6wV3mO-JDaYK0CxoVRMUpH2RtbdLjxo8jxR3BgecWuzyHZmTms9_iWpEXWYB_siBYJ058n0r2-3Hpdm0AR_byCzuzPgf1vZ4eE4aQLIFZMW20LMXcc47ZEZvak57kChADTJb2i-xazK2roefHVduRly5rSm6bFnp9aVLG4QrbJl2L_o9Dbcz7rYTcBHWYdD6DGS55CkaN92oaVKpzd3RO01iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCJgLHuGw2-TSjHmhsT3_qDFhuSUu4PVarzS9EekwyeALZ4osG58rE43sjDX402nyKelXnLppTIKcz4iO4eBOceRsWfy4Q6jZH5LoTODGAIC9lOpbeYEz9CPVUBn4JL5diKATCLmCIrzwRsFCH35qTeFCzqj3_We7Wqb9rrG-saZHIvT0q-RE77h6CYwk4BF7aILj14HcBqSkXMNeaqefGki7CwIIFtVJLb1MToX9HBkc1w_uiXJ_qRMRJdflnMuIYhX5cC-Kl3Ka7PqL2fNspVwMwSsyTQ9JTbDNuInA5dcJ4VBK9nzVSiOqifsJmFDafTvZC8tzbPelWcVZuPhZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cb1C9RTInguYE8XCmoxMZOidOLvnse9bQJHOeT_rvjnkJnRJaQoqrKS2hKDimu2BlAZA4k4s8arP0bUrmuyARKomlhtnHXqZhOMVaqajTv63rEkMlOLiMSkr_KoYsD4bJoyYRiSffSqAuakKTrewIT2MNiNnvQc2tVXmMxSdhqZjKv6eF8565gAEUVGfGQpuL_o0o8xShasNiLMRc4zDmOfHcCmkXjeerU1p4KE4jl5JG48McEAn73v7LKpI4MaE0qsnWJN6qmTCn_EehuJ8VhUY9LPDUhqSyRxfJx7-zGFzID0D1BELVs6NJnK00FM6ofIvtbM_N434Iy8JMmaTvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kTUkWtZXwjWgPgTzAAWhOYWuNJPXMVtRSQ1MFts46WZCYroBBchX9EnPsMg7Wa8tKpTizB8Y7kj3qpnHDIZLpavEDLWDsASu1WK0o-DL7vhVWZjbL72dHQYg6ULZHcSnwM0tD2WNwhbBE3VuQw-UbAEOrKkZsKkl_DG54qnn6716UtDEVl98sp70e6xdPkoF4YjZrD-OWi9jfDrGK7SobzYL7zHD258cDBUTUwlSddwBG9SsY7EbfRJqQO35ux_Zcaty1ZrshMQrDrvmeP3XGBY1JiwzIaSfaG7Mn8UifN1o0PVxwlnUB-y00vC6iWoNEMktVucoHVRBU4Ts-J2rQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aIuJ6i2-o0r9_UciPj9Pf7R1Mvo4li8-fAqcPyw7s2sXMopHfPXztMxdH-fiKYIj0bxhgBZJABcephYU69dYULpugbqVOvd0CS4mmgJ71gsq_DocVA53S1LgG3lOt-rjrQH1NCd82ql6IG9GuoQb2bmLBk_xOAFujr2Vrg236uxR01yq7MtiiNqgrc74ga4WNh3pa3IFdU8rLRKoPW3mFiIJ6WG5uDgck1iN_e8WT8-bAFT00de8OCZ-ksKwG33FSM-RKwJ8-SfwAjiszHbqVI47R1w1MxePk1FwgamOM3CBVrSrlJiR5qzZ5TgQqDQ7jvnEMOc_ShYvUj3RSTY8qQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=JS-ec7MvRdYIVO36JOFrUOZ4lywclITI21kZ2u_XzMPOUeD6DTnm_GZIztNpCdStKGFrrMsweCkGmVfDtYVDHMIVLn1-zGsqQMuFDw_2UMDq_yno72C_bpMO2GW9t296z1gFDiOsM6NHCDQpgkN9wc1uGPTIZ2ze81UaqfcLForZcg-nCyNosJ90HiaYBWF0MgftZu5VRP-pjSmX5ZVXNVh0AlMSmouRfpv-jE6nxVAMI1Nhoazf60R1yPCaBwMh5R2iLxl4c_H7aP2PrWSUA6x7pn8GjkKTVtwLV-VgUNsm4HUi-Qap-yIgB5T10DJnwRUom4SwO9xke68EMqeyCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=JS-ec7MvRdYIVO36JOFrUOZ4lywclITI21kZ2u_XzMPOUeD6DTnm_GZIztNpCdStKGFrrMsweCkGmVfDtYVDHMIVLn1-zGsqQMuFDw_2UMDq_yno72C_bpMO2GW9t296z1gFDiOsM6NHCDQpgkN9wc1uGPTIZ2ze81UaqfcLForZcg-nCyNosJ90HiaYBWF0MgftZu5VRP-pjSmX5ZVXNVh0AlMSmouRfpv-jE6nxVAMI1Nhoazf60R1yPCaBwMh5R2iLxl4c_H7aP2PrWSUA6x7pn8GjkKTVtwLV-VgUNsm4HUi-Qap-yIgB5T10DJnwRUom4SwO9xke68EMqeyCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwEQHyeHMf2wV0Qun1iV-l_dTf7L1ZZYVuvSkH9KlgcvEUdR_AWj-Cw6rUHrbiFTkdopdyQXEI8V6Z-_uAX5h6cCMD4wN3Nw9g0Fc2rhBseM2eHcEWB8TM19xEueJqbnb5Zj_vWonVsQWTwQhFaU0foIyZmwCjgLGH4iJrSzJ5Xw0wZnnS4JFAr0NelF_dACMCEEGrrrS1uwbjolC9z2TSYRomtcs2qd1aTYAHp5jBBxbQXhEuCF1ugx2darCg2WKIBt59O48xAGABf5Wiqf37Q_1EAWyKqHAksFsHAD4MAMt5OIKPWN6GRPvN3FGjDMyyv6k8sy-x8BgYk5HFVxxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgx06NK0KUIof4rx5_4LaOZzz2K2s5Ju1R9J7VqXqeZd2jxqO0xUnLV1tYeRU-gQduWYvFv7mPTiSqp1XAPrPomGeWBDDgJFKt3uAqsHW4bYwYi2rtHbBIbn4p0EzudG-vZtU820CD9hyTGilGSdu5UDOe6Te_TMl6peCXmNXt-xcfLbj0r5oXFHxUpOpIZocohxTX2aafCVxIFWxg8CtKxsTCWO5amUiZkyvN6RnFyO4kddj2LypwrboO3WoJizQl_W8qQKQhzKQHPJd1rR5-b64pgbARFG8NAYE6I_LOEu7Weo-UaMWb3dmiDFptux-GSs4cDTbL7UcZ99WnMJNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=L_wUJVLMLEne-9s_TTbyhSvwzTyyPCDXT9kc4uBIGW10VJ-Nq3yYvmB7OKNy1yTECo9-kc4UDexQlBd5Nxwo9wJ0S0gq2kl_IqIOo30K2QD_3zn8EFb1x6ehLQ01bBFNePrt3VOHmejhgaLfBubbimcHI2B1yCEBhDgHNmWulHKF0mBywI4DJ5TU1rhYlT5MfqhjWyvRgTH_djxP2J189uxeucBGi0sbr9TL52Lmwf89XS6XZyVif9_x_9laRxptLNv0cP_q_bFdiw7wMIbuloJL8G2EIJvLg4X7mjWBvxlIRfLXJdIxWLJl_zK49o-OqBtc-iRnu0l-G7ftyUTiig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=L_wUJVLMLEne-9s_TTbyhSvwzTyyPCDXT9kc4uBIGW10VJ-Nq3yYvmB7OKNy1yTECo9-kc4UDexQlBd5Nxwo9wJ0S0gq2kl_IqIOo30K2QD_3zn8EFb1x6ehLQ01bBFNePrt3VOHmejhgaLfBubbimcHI2B1yCEBhDgHNmWulHKF0mBywI4DJ5TU1rhYlT5MfqhjWyvRgTH_djxP2J189uxeucBGi0sbr9TL52Lmwf89XS6XZyVif9_x_9laRxptLNv0cP_q_bFdiw7wMIbuloJL8G2EIJvLg4X7mjWBvxlIRfLXJdIxWLJl_zK49o-OqBtc-iRnu0l-G7ftyUTiig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=aJeLFeLHOsWZc45H6aNXjZDAxMiA4aaTKColzS4yxHSDaTKHuQeDOffMu9Y7V0i4lQtLdDdDsOfLt3qGQdu828_OFFOEiMq3gLlNqXB4c2Xm3eAsY3XjPheTZaFOGeh9Sfg88Tn0dFzwvZ8mylsJ76scjy4XP3Mlx1ZZ2OtvecVLaRkOgqFg2GnkHu9xTcaRG7goXICj6n16bRHIBYmAjb5S_UyFl6_1yzJMJbfLwgrISifNqILM8xrQiEFEjdWsDgXaaQ3V6NmOOHw9r8IQ34X50uK-TyBLwieAuGxpkZ0kd8OCsg7I-F5JDi7CmrY-YhQCxes9Hzi73QeU4jeEog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=aJeLFeLHOsWZc45H6aNXjZDAxMiA4aaTKColzS4yxHSDaTKHuQeDOffMu9Y7V0i4lQtLdDdDsOfLt3qGQdu828_OFFOEiMq3gLlNqXB4c2Xm3eAsY3XjPheTZaFOGeh9Sfg88Tn0dFzwvZ8mylsJ76scjy4XP3Mlx1ZZ2OtvecVLaRkOgqFg2GnkHu9xTcaRG7goXICj6n16bRHIBYmAjb5S_UyFl6_1yzJMJbfLwgrISifNqILM8xrQiEFEjdWsDgXaaQ3V6NmOOHw9r8IQ34X50uK-TyBLwieAuGxpkZ0kd8OCsg7I-F5JDi7CmrY-YhQCxes9Hzi73QeU4jeEog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmbdyCBhXVbQ_SpzkytniAy9Ao-_uusMlP92WnHR0EuejDph5_SP35cFrTmZMPfruLG9mhy-xV0jF6xPRZnP2WrjHXsVnmQrQtMbt1a0dAxxmlX6LmWsif3VhyUamwOHY6Y469HgTp9SG4cF7-usrn2x_sZSVgw2wN3w67k_5J25nAspxoOTeiTAlk5ZvwolUgzxR0ud6RvG8QVa9lYLdCjq9W923nabPdCRXbxoLbefJ0hBbZkJ0FV5m3ZtfbcEyzRDR1T3ZUP0Ru_ZcYHIducl2nQS3tk9dmDkH-2Vfali2wFD5YvtSq14Xn0oC0epSQ0Oifwq-s78I7_1PoiuhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWkX5JX9Y2rx9SH7nodtNEq8FT9IBAg3PinBGYBCG-UPnDIXFat5LRhgjyGmnIBQTDiTIkRM-z8jB41-DhFXka2YS6Me_6AZUuuPqLY3ldn-m8bPMvYKSX0ZZxgXH4_z6UKv3RB46nzM_T9omHOoCxz2F-lLmV038luR9ej6eZoFyS050WEXzh9XHOHOitkx8WOeaaDscqhWUAlqqD164JfzZwoRjN8w-AI-7ym_S23q4Ow98v3b1N5P9EPW9DtL_DYjrAKea4RIX_Qs6lJXydnR9gvcydRLUPv_hBU0kIonBX0bo_q92cjKs90h1ni9OZKYProIz5K4F_-PLbRvAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbJYBnc0Yf-PKSp3hrQ-tmjzPVVojXZ6DWsiAG9Xs4zgGl1-E-2WRXRIDL0OTLzX6ejoAo7ScEnqOu3oC1dG49F3tpyWyGVYCfeR2vv65qvDj_JXwskwOs6G9-V6fbr0te6quZcqwKH1PDjzMN1t-uTRNBkUTfSv2axQaQpT2oouwKgpXLuFMEoHdUaibhndamH5D1w_hkOJyIz_QMEuwQLt4pPporQLdOO3N5g19g3NLmY2r-YSo0SSXkjgISDMa1O6QJcmZM6h0RIUZk4fe0FLX9s3CwZmG7VCvxZjLSzafycCMEF34IERvc8O-KP0FAZ8vvc0t-23YTpO9UgSWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udFR5jxyl2xxuWffPbRt5Nvc3pROyAmSUDhFkdIS0Q1t1VKkFJ2RiRRtCjz8YdPPeyqNpgGkKMvihh_WGMOsStx-PNRH5A5FiWYw1_wW1r6Wfu2W0A8dSPIZ-51dWArGW4-Y4uXwqdn77EiUzrbVOrsUbV9QAVoMXVcWjpWTN2g9ub8ouGOqC075wKZMzkSjgwM8l1U2wcC2YvuwvyDxLxuYmqIxe7SIX--KOQ_B1ByN8u12Ze2xMKRrjKNdQSxDhlq_eX-761V8Q7K7NmPM55hQR59LyPKhPhugohqbEI8Ehz2fUVY4H_vEHFGdrVSTYc9sQuWemDKN_qmSMjdaNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_3QNGyhDDWMjZBusa4bP8WJcRkxy5M4H1J_IYEKoBhFcMdmpmljoSPwkf8O6T4zn9eYiJhd7OGK6TPodXkmmwzxq_0WLwoEC3OZ7SCuIkuVUThhU8EnU92tg9HKs9il2-Dscu8jDUYktOKQkEUTGymgx6VMJWFp9hFz8vM4beuS2Y8WpWCLdyReQ6fUJ7g0GTk7_RmoMWX96J5aA-o4edHG9avbWIV8s0SyyUuCaP07a09R48ufS_6lPjNJjZP3LSQyZw-htMoRqHv0HfQkAiYIHIYooKwiDXnWF5x4NMGSFTSvcCijqaydvvcl0sLgxQz4I1NglI6NXPS5f8ZKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWyXx1dF5K8IoH0jJt4XKqRYPyz75pYfedK-d0xRgcZDSUe3VaEqS1MQX1JBlUFH3qxkIuLwmbsE2WQ1o7sIp18zo-wiTNssP88_DtQjPLLyaMzChfBX2zWTd4QNF2ICBb7gsopdxkRM6gIweiTwb1TQmCAmP46580QM1OERghOC_ji-3x-2WqtSb-mjK3W7cNUPKpFlA_SXXNGUobHuIfFb3wqyXNPgnvU_17QPXksXL2osiZ5gmxAC6lEXa3s85yEvGbja6BiFrtApVABNqlNmS6d1Uo1iwTN0fES3lQZEcnXAMKvKpXOz0WzhRrJjKUs3kB4Bgv0jZ9N3GnwcNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsBKl9MryZHyxN_JmYJ1w_QPWUxzi5U58pDm2Ds9C3psKqv2PyBDOqea2A3gUhXw5vImTbPrZB7khwsCX7aX3jM5vxf5bD_6FcP5-KPwsb3z_Y42uH3S-kgGN9UC2ytVPek8IcAVmXQceVYxzmR16p0p8SzMLFMBr0qNL4V_XCpOc0CIcGxGvF0kcTuUAg46nBAqZwwtuniiIQIfnjjXu-iFJnOnontWMQ_SS_a01V5-EOKbVqPE4cwQF_AKnbkcfDD1hsN_LmS7XdrUu_Tmn0ULNgSeZIdKNoVaRo5y5jDcatSHv_3yEkMR3X234iafZ02r9hgyWk5ys_bKEF-rvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLW17aHMyGbceHOLVbHEoC_SzMXgRODSpcwe4ZNSe8E_eLrEF52uvG0XIKh0EpcgBjluVsZOo2UIS6Gal7-lzeXjmx0M9ijh1icagGrYGx3MVPd16QEEukF9kL2DBPmn6DM-142JWQWWr-WQ4MErCHiDWNYEkyg__xuvm7LglyxQQaQ7kWR0KJVvjp3Sb0VpTgoJ-uE0PsC8YeTlMlbsSwoMYKRLCtGyKEIKsn8yhx3eWjikP7wLKU3NVlG-3H1Ll3c9bDSQVr0dN7_P-LToekjAN2NuHsoPgqX5hWT4guE1JCGbYExUzetTmx5RsCLkTnLymPwcXi41uvaRrgv5BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=fyGifw3vjUBpubfgKkGYiTEqaXphvDfQZm1VGAxKX-LZTvEaEz5tPErgdvCPoznjxO9p2A49p2rTM_mlNM_Tmw4ZcF9Wu6WpcngsUu5i9UmTiBodNB3S7wPmDRWT5sEnwY2SpKWTBi7A7dEmTXaqNupFyncQz6hSPmb1X1Uhq6w19hp2s5bL6yH4b5ZsXU8EhKs3FjliMus-kO4_F6Zatfce5tcuuFkDWTBSSAwCo6H7e9-gwi2veha2KaI2chfoatGSRg5oq_7lh2FSLwx4TaUTFDcSjf9_4yZE3cjsdH82UnPhWVMFcy1XDzBwmKR1sCYlGySX7YNd9CCkVUSIfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=fyGifw3vjUBpubfgKkGYiTEqaXphvDfQZm1VGAxKX-LZTvEaEz5tPErgdvCPoznjxO9p2A49p2rTM_mlNM_Tmw4ZcF9Wu6WpcngsUu5i9UmTiBodNB3S7wPmDRWT5sEnwY2SpKWTBi7A7dEmTXaqNupFyncQz6hSPmb1X1Uhq6w19hp2s5bL6yH4b5ZsXU8EhKs3FjliMus-kO4_F6Zatfce5tcuuFkDWTBSSAwCo6H7e9-gwi2veha2KaI2chfoatGSRg5oq_7lh2FSLwx4TaUTFDcSjf9_4yZE3cjsdH82UnPhWVMFcy1XDzBwmKR1sCYlGySX7YNd9CCkVUSIfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ks1dJxt4JbT1iaFMAIOPukyurarv2TdGTbIGdF3ONQmoKxw29TP4g-sjaezzKF6H_ygNTYQlJIht6meBVyInwXZMDNdsZOskzoGx-2Afstaq62sjkbaSNVMANDw2z_oWq6nW_5l53YQBGEg3M9M3_uKv3mnIO8dTEdUo5VwtmNA62Z0jph04rj0Akxp9XjdFTjo5VHCPSQlEsbeV3-UTUrCUMie1oBsczg3aymrcHa0MwluJRCeF-Tgcz2dm-kWtOPSrezOaPXKucgn55_uMCfgCzgtrlQz7kwXu2resBRtjRfEqUjhXspIB7KOgyiDDlO7mG1HqHc9fJQw5EzmKBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=GuiwqHCgaTN5toPl1jso5X9T6WnHfoo9nHZClUciquBmqBkXZpPuJp2ogSPUYdiWqCZy35nOL-3H3lsadMBa7rpenwi7KT9l95EQvwFQMoWF7Hpu9Aj30_MFdDsSz3loRVw5T2AgKzwXbyr8-MbhwbBDTChmOiYT91WucTVeP34dDdTf0sa2aQ4n0RBKi1TKGCp0H_-_q792A8VbbHwQBZoSRRvucelx_L11yS9DJ9iPILWfYLnB1V7gkx3CBDY4Nj5EVtaG1VV8Jw913oYdgyYyONdBuFPjHm_BZrHzVzzAAE4rbj-jD6PrU6nWCzSDFfCRfuK_YYp1Emt1bfBAHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=GuiwqHCgaTN5toPl1jso5X9T6WnHfoo9nHZClUciquBmqBkXZpPuJp2ogSPUYdiWqCZy35nOL-3H3lsadMBa7rpenwi7KT9l95EQvwFQMoWF7Hpu9Aj30_MFdDsSz3loRVw5T2AgKzwXbyr8-MbhwbBDTChmOiYT91WucTVeP34dDdTf0sa2aQ4n0RBKi1TKGCp0H_-_q792A8VbbHwQBZoSRRvucelx_L11yS9DJ9iPILWfYLnB1V7gkx3CBDY4Nj5EVtaG1VV8Jw913oYdgyYyONdBuFPjHm_BZrHzVzzAAE4rbj-jD6PrU6nWCzSDFfCRfuK_YYp1Emt1bfBAHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=JSa4CFHT3nFKUSqFiM3jN6jZSfqgC9AX1ZcaodvKFRPgsgd-2uXsN1kSZp5gAv6H2sBzSQQw1l3baJ_eIyETbxgCC7fjhOpYMZGf2r9Ap7lskbep4ig1q4pL-fy37YZgx-l3yeOuGj4pNfHayI0r2XY4l5BHvLdz2k0l91t9Lzj-d-e40iVckZu2j4vaDrSsKa87bdos8W3fbAI2EXtV29wL1jCRxjaVunct1rGm5_fLdoqagAQoN8lmOCnwztSiqLrK6AqRlPS5IJ9-nfujAP6OBfM-DWFIcCTqz-mx1lOdaXoRa9asFYkItdt61BBj653_GprqQCZRZBq9siI_qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=JSa4CFHT3nFKUSqFiM3jN6jZSfqgC9AX1ZcaodvKFRPgsgd-2uXsN1kSZp5gAv6H2sBzSQQw1l3baJ_eIyETbxgCC7fjhOpYMZGf2r9Ap7lskbep4ig1q4pL-fy37YZgx-l3yeOuGj4pNfHayI0r2XY4l5BHvLdz2k0l91t9Lzj-d-e40iVckZu2j4vaDrSsKa87bdos8W3fbAI2EXtV29wL1jCRxjaVunct1rGm5_fLdoqagAQoN8lmOCnwztSiqLrK6AqRlPS5IJ9-nfujAP6OBfM-DWFIcCTqz-mx1lOdaXoRa9asFYkItdt61BBj653_GprqQCZRZBq9siI_qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcQdr170sBxp3u3UlsNxmx7MluELvw8VGigZXJjrHsReyEc5n5fZy2-bMp5b-9azdPKWydRuu2XnB4Arf8pJZrBy0vvbwV0ZMCd9aPvWzSCyhEYqv6hm3YDvenwtwzne_XLUwbgZdK6aices0nMwpxXp2naa6amn0a3h5DaaPhNW2O8XmptAsQxWPr7UQ68uBrtaU1vNiRXOVFITM6y7aJGDAQTt-y0CEuqZoSBx1nN1ZtQFy4oyu_F2DsezJ5MN_9FbjqeGTM0h-UbnPImPkovNkqSe2_89XUXir2CUCHTHs_3UzDAQitpU-G0mCt8EmSNlGAl-xm4DdHxR8wjJlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQ1DKxKPDNmNiIfkv06HYy311YTuhi5bKiCV9WC5W7gkkg7Jhx-7MmfqHuGH2678oZkZYzz2_4EZbcn7KMKC1rg8pk6jjHKyAXlQ9HiLpHKD7aWcFhVbCEk8WlOi852gUlJattM1MT9gMP7BNrItiapXgth5gc5Yb3ULBBfuzVwmL1oyTkJ89LgHVT69TywBKwvPJH-_YcHUDLl1zD4VggH7zBPPWp4-YwC8ON_VmVIBq2w-28dbAxi0FJJcz8FX5qHDurZzycL8iOiEjySfcI8wtn-UcQYiCyA12B9Wt3DyKmn5szZ8tAQa8j75ynFig3HmQoYwcA_aO8Xryn1qFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=HRN4Xol0erJt_v7_Z5zbrTOwSMkiLpd9EQyqBmLoocWfud1RcQcewTBka7ZCqBB7cn3PPZdMXvRH85a6GlYCgyyPlhJ6vL8CjH-N1zv8A69Ks7wQ30LXRMFKHAdA8TcAfIURRDhfuu5cZ-lssIW-V7HAlWFAwUcCCgRXLMomEGmReOvVc-tlFA77eaHTQ_qrN_wLtRp-L4f2pEGEYcxiGXzU3mgr3B1SVcVYG7DyVlDQnseYgA5p_9OG8cW_7kSCPHx0r52DiXHpDGeVRuEldFWl3BkF_btc8niVP05UGuRxFnzrQHfyL-NKHNz4F0VTB8aCbHRR0XRHN1cwiWa2NEVuubO5BaUnqL3z2Buc5QnSpzWXgMvv8wymABbqg_g1WTCNvr2qFWy6nqoSFghye2qJHGf2MEJLk2E5LbsQtToEW0lHTgr-m5SW08rEMkAnpfR5qHtS5ZKrtyYzqBMMD0QvIn3XysKB7Uh16uz_aIjK5V1eZ8Ydsik8k8QUhBM8jA2dBqeF0f6gyeS04ai5IMmhJ0yv7SbNpik1bSPvjLvqw1PdIwicC42-AqPMKsvT-vBmk91BVv1PIpEkTaMGhXsV5zwHsjxpV_Tlw9n7DxsTpX7uE0HxlfknZBJx3GZrM0-yEgqPb6YBj2k_v5eHdH_AZ1hj77meXGuwdx6OK14" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=HRN4Xol0erJt_v7_Z5zbrTOwSMkiLpd9EQyqBmLoocWfud1RcQcewTBka7ZCqBB7cn3PPZdMXvRH85a6GlYCgyyPlhJ6vL8CjH-N1zv8A69Ks7wQ30LXRMFKHAdA8TcAfIURRDhfuu5cZ-lssIW-V7HAlWFAwUcCCgRXLMomEGmReOvVc-tlFA77eaHTQ_qrN_wLtRp-L4f2pEGEYcxiGXzU3mgr3B1SVcVYG7DyVlDQnseYgA5p_9OG8cW_7kSCPHx0r52DiXHpDGeVRuEldFWl3BkF_btc8niVP05UGuRxFnzrQHfyL-NKHNz4F0VTB8aCbHRR0XRHN1cwiWa2NEVuubO5BaUnqL3z2Buc5QnSpzWXgMvv8wymABbqg_g1WTCNvr2qFWy6nqoSFghye2qJHGf2MEJLk2E5LbsQtToEW0lHTgr-m5SW08rEMkAnpfR5qHtS5ZKrtyYzqBMMD0QvIn3XysKB7Uh16uz_aIjK5V1eZ8Ydsik8k8QUhBM8jA2dBqeF0f6gyeS04ai5IMmhJ0yv7SbNpik1bSPvjLvqw1PdIwicC42-AqPMKsvT-vBmk91BVv1PIpEkTaMGhXsV5zwHsjxpV_Tlw9n7DxsTpX7uE0HxlfknZBJx3GZrM0-yEgqPb6YBj2k_v5eHdH_AZ1hj77meXGuwdx6OK14" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oP1aG9go8khr5P3KHHbohVsZtBQ8lFHWJXP6Jn7UsNg5Qnks_BLyCtFVApqONluBOMVk9LWBMrioBSF3NHt-RBT0m5n_ad7F0SVg25R2ZESV3vscz9wEuLshWMlNf2hawT36lCch_e-GPSt1yETqjS5S29g4Vy-l0NWp37lPV3SXnZCVdfnHR2LijUPRo1YMLD-vlvgKzSgiWUgwRPgYgjSmphY7KoIjqGUPScWVvZydpZ1RX3zJqNamdB1vpb7YfNnDk50ij2kX77vZ1LVhazHWVQuCNjDNyyyrJRktDz6fwoL8DJz5Xo8S8P1qJhcCzrLxbEt2zV3HP0x-29PUFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=NB98F7FLKmG04-Y1G18dgUDtDack6G6uefKQ4XnOgI3u94_J8VmawG5VFdPIj5sMlsbgyH4Pu5S1TcMbPebQoy0TmFrtLXL33umkfwG5ctnZvfiJqfbHA0rOgNqKf0t4V8LEUnThTj0h3ArniLOsg1z4zBlHtJhJl5VrWFp5-gFY1rzPgK0lXecFEl8OF-YHFEKXRNq5N5wjhzqNud_UXZXlFQ4nsIe3yZ06saYpYvX_xXfTB-J74n6EPb9QSw5YWswXu36XTwzinGg-nEijYo_7RdJtjLksBZDtJOtalAusa7q490BpvmeOzmxtdMqWWzg9Jarp_opRkxsL50dntmSb2kSCAzdf54iUCXLTbWy6uk5yiEDw9F8E_ijPC-Ksd9JtTMD9cMgdDdJWxgcppwBFOxbZhSP7scY0yP_YXdCoJFaSEhSjlRoHr18_WKLd5gtgW65WnVW7GBsIq7qLSs11Z80GI2uXxVMwY3RR1i4DYZi4m-lWyPWz8MLXZRgyhctBYROL15E1PKYtKyZzM0zucyGPJ7le9bi2ueVtr8QTdd22RCiHpqoePMngf7LSgOY1RZGqzic0m-AaA2QNZTody3mWX5sY4mVqSe2HSzhqPEg1VvnWK2Elc8sxICprust6patxxuJpefaGmTpHkvk2FSaftUGzoXiwWRdO2Cs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=NB98F7FLKmG04-Y1G18dgUDtDack6G6uefKQ4XnOgI3u94_J8VmawG5VFdPIj5sMlsbgyH4Pu5S1TcMbPebQoy0TmFrtLXL33umkfwG5ctnZvfiJqfbHA0rOgNqKf0t4V8LEUnThTj0h3ArniLOsg1z4zBlHtJhJl5VrWFp5-gFY1rzPgK0lXecFEl8OF-YHFEKXRNq5N5wjhzqNud_UXZXlFQ4nsIe3yZ06saYpYvX_xXfTB-J74n6EPb9QSw5YWswXu36XTwzinGg-nEijYo_7RdJtjLksBZDtJOtalAusa7q490BpvmeOzmxtdMqWWzg9Jarp_opRkxsL50dntmSb2kSCAzdf54iUCXLTbWy6uk5yiEDw9F8E_ijPC-Ksd9JtTMD9cMgdDdJWxgcppwBFOxbZhSP7scY0yP_YXdCoJFaSEhSjlRoHr18_WKLd5gtgW65WnVW7GBsIq7qLSs11Z80GI2uXxVMwY3RR1i4DYZi4m-lWyPWz8MLXZRgyhctBYROL15E1PKYtKyZzM0zucyGPJ7le9bi2ueVtr8QTdd22RCiHpqoePMngf7LSgOY1RZGqzic0m-AaA2QNZTody3mWX5sY4mVqSe2HSzhqPEg1VvnWK2Elc8sxICprust6patxxuJpefaGmTpHkvk2FSaftUGzoXiwWRdO2Cs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWO_WusNSRnsX34-dKq1rfgT--tljSZ-w6sR2ZxQaXm-PsvEISLETT78UvM8byCkcd-0q61uEmhkZihMoxLWq1R8iqFeR0c6FGZoyOg8UgVM6uyZkhWzKEGT-Yk1YOiKgR2J7rZlzakMFuD0znvWXOub1whlS2-vHadzoewK5fl7GIfV1qp2UC1VJ47ljlVRT6Hrnbb4t2WutOO60JlJJ41XpS9aBUoiIG-KwKs7c3ZiU51UwcjYflVvZO4JYknu8yWnpkQZaBKmclfUa_e-RBSV1om2U5GdLGnZZFqTV37Gv-G7VrDKe79zQshAep7qPp-vK96FzvRKfBYlLx6-Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAvjpnLNhxbrY8R6ndfAEmZX6IXGe1P3LnXaG43-5Lan6H4tBnip4w0-I9ZHF6vrif7A_DPaa2N96z-um0xHRkYG327Je2oz2y2LutKSnX3QJZ5n-90nsa5zQJx31ZZ02SucbNZtHyZnMd8AyXkOHHpJDNzvn6GL-oL4uGa6-CjY0mdL2X2yIl3TQ8Qf11NdY-YgjbLDE0hxwqXrE7EpprXITaz1PqSDMU-dggk6rMJAnBXQiX4ZqLpWSiciRCgeIZluvoo2xAo6H6PutFEvgo7qxl9Q22o7iCHUjEj-vnQ33C9A1CAwAh7tyQJXeAFz9UgU8HN2yfGex1A0GDtuHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afU3Wmsh-XD4KRjscEYTzArPjFxDDX2s-mvPdXJP-H7yb0xGz-32znW_Rgp_sruizEXLAL-4yiN6CcmYv7tdmSVBs_jvS0AH96APrQaSMmAt7-l1f_dvIbsyacM_3AtaCKtV9UisPKoiWbz6IglgAKIaCZ4epj5zVjm0EskdaSd7xaw3M_AKH1pMgFU-6Mi0QknQAUBWDHSavJggNNYHmDa7aRmY08f35nzzi8MXxlF7gcwP5WvfjjaeLnRZchKFSSO-5eKODWDDIep9Nc1qPzPQStZLld2mzNklwc5qiuYJ9rReOS6hlLXmHh-DTqC36zElE78OOGJpe2XP7qnApA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obHO7EubNXOO9-b3JpsbSIxxz27Ha9C0EeVRXtJqbXujg6sEzV8RF8ymdo_5cVe1-iS7v4fSaof-kI-8phMavMb7yC32UUVycs8nfkEwec8f71z5lD6r9QVkDwk3NpGaX2juP_nN08b0ttK2SFAnoj_iBxpd5GJYtwq9VcAh3_31p5DMAmLK1cOnq6FwPIM3eohyIORNH28VEizXpW5FKqJgxd9pOeF0qcutG9ni3NbKFAEyL1lq4CAICaQQknvKPkFeFbuae_1_zQStYkdNujW8UWF062jHSMn1jpo91u01ivupYY4YWm8uQAArZkims-i9PdyrDqzGN9P63bXI0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssf1xQ1EIuYfrtK27KN10q9PeGr_wxhUgR588JAO_n-f8RL1gHGpaOeyBdOCG6tQsSQdMk1sgM6EfhdI3k1PthOAyuRsiJ-3cQJLP5_wpitOxwzLTjhyo54B_DV9-X4GrsaVvuzOgIjiSMDwsrr4n4q9P22P9taoZx8HdNbjuXApxsl2y-Chx5AwlQWAS1jVvYehwcKcxSmGVN8P3LR2hJdb9hXzybL0nm4ZL3C6k6umS-P4CZeZs6ZkCwG-xJ7ylmNGbeJjeOlgQ_fJASiPeFknVjYRw71oj52I3342MAAYa9IRoEecvcpOqhqJhK1-Umj4H6IsXIxa9RclLaMyRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn_uPVfGkiasCJSqcI8oc4n8qIQK0GHPufQxVZpUCrafKSylISG9Du3ZdvDevaLEHswiKjxhLzGn2czPJ-_c_aJZ4JugNO-Hv-JBu9FXdATNTvCT5tHc6ZyniapH5zJWFL67hiZz0B86xG-CoiWoD3Juv486EN7nnaV6B2Px7HvtvpterLaqi_7EcqH5kIeC48gsHGdZ9_drwGBejjzhZdG2ltV_f5AZA716K6OdAyVEgyqD3l7GZGh8NUmcMRVoDoqaAaAMu0gJWqNjGckq1jf1WUjvahRFufPfsAPACn0Og_mcxfsxdCIIX8B6xdsOHdaIShedKWPQtnhrCfFLfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5TCScnmDH0RxtH0SD9cSFRu2HXh5iRMZsLTM7JRdvrGejgpKBAfcHhRaf4HQ_AnLZ4vjyivDjvS8VGg8Zq9mO14q6XGMNaehsKiV6WG7mJ2OgvKpASllQBev0bJ-TbOAQ1a_P68ZaXcBXTLw-AbUQJPcPOGWVljaCU9Y_drWSUmst2eO_8EVkiBpPv-5D-8HD3GyMFtG2efpLkoiJLYrqmcF109vk5x94Yc-cPH3T2W6iVBsZDexj4YNP62akwW6fRGIYxCjec_1X7jW4OoL6RaePOMfUxciA-7JnlzG8IZUKCh2FHrAzFnI7tpYXrbcbKBxGSNFZ5DgEDf8j5TCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9s2wx1ywUOds94ZmaryjMX42MCMNcvMRipP4_3iVTgiY1zHGuRRuSbBP7cnKayFl-pkV3Z1pBWy6D_N4W4VfNXO14a50vO5BIjuaUegFFmQ7seFsqf9zgfflsePE852MCorl8TIaMGWMWpnNAa3U5wykCH0Spti4T-l8NlD-xDxJ2_ZLUA7N1XECOOG9eZkQ0jUrxhZbSQkvTPjklBUXkM5C5hzzRzOGaSpIGH-QdtYRyBSDsDSDq_QNZsAdGBCafc92r6G1ZtGH3x8UMxy5gXgMBy5jWV1gNuGHoFgUnZi7DWDN9yIWQ2T4qAhaHl_2Bi053KDy1L7eN1UibqBgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3GbJfOilXRXr-FdQhh8HvWWdV3t2RG7HH1h4_GYZKyZOYCYvOZlZh9OvTX91WfJwRjP2q0TKJtbF1gHay8e9R70YY-7Kij7jGtIggwJdr-XE_kkb9PcH8bSkku9pP2XIjWn2-9H8tI0Ih2Nx8fHlu4QiWS8J02U8pHuoUyLaPiL9WetoO4X24iayKevDxVWSG14rUmLcY-i25c_w6U9FF7YwD1hpQudYbo1KEmxozn-FDbDJDo539ylp_VTRDSmF1TcDPUowZXD6hCir7i6YEcoE7cTfhyCU5d2cu5Ljkb2kPwsl11pOFNdqH02yCBNao5Wzi93x3BUVaAVW1V3Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCw-KeFGocrGpv6l7jkkWqTAL4Ng-__2JI4x8_iGUSp6cfOqmtFoRC3RHPjfLBpWiYnKCacY_5tNSVHgNlQOVeA1m1nOG7oNwQ1bq4ymsV4XVPzxgso6xFYNTSH5kvs6j3GABMUMU1nDBWGBYWvcKXC6tHyfJvWkbMYg2fUxefIaoULTjP6PB8qgshjGrc4LrlNhMjsss0gyLsCjTblq5KMgExh9nrND_BmuPcNXvUyRsCTGwXkSt3syycm7L61UVa8Sr5C-hTpLISLbbVUJTgkvy3SOioJsxshF4YzTH5Pwcp0YHW6WzNK9ztyy8ItdgrcB_o0rquBXGXcSWdCNqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmUhRJq3epPQ1rjmIg1hrQSyNwgIM455u-rMi7A8GI_9ohN7UwJdDpuzo9MF46b7YeGQXoZ2TvlEn-LoQ63_Kj1KMazHLuZOf_m-InVrd7N8_jmBf8TKoiqfGjo-NCpHI-KasFXfZuXrBvqBU3tdlAqSa-vgItYnk5Ljk3y_bnzgH0okczlRvU2AcoOA5YyvtCe-cf-61EwWJw-nrFkKqvgRJvK1yh8eIhrR36DUJO_3VxrxNUvDtyBEMVjwarWe3AOd1PW_hjTc23V-6mG5C4aLiASpQfjiXIJt0YCXR40l_SgJ2VMTS6pzvKiVGZPd4vem41yBN18Y6NG-eOGwCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdIBsOTFBJZXBICu3xfD0ICku6dNJj_3Hn4hCyDsagEn6eOz2h3xx26EM_KOP9ET8owISsZHYeFf_FMpJwNAFQKPOTT5c1e6uhzt-eSKe6hxk6mlDbaZAZWx_jtd2T6Uvx-f3krbHrnNQu1eGJn2fDbmq7x8sCfbLl-POTqv7UGgFsNY3qbJijV3lsZKZZrt2R9MKI0AH9Dgzn7psyCewgDHWHFiyXXrqlaX1VtzsAFB9kc3YGIs5Y_bqzf4WW0o9LlTpGDs3FVuNBEUKBN1rVtGMbdcccxVIrC_FW-RHkOlaC4A5Nk7b-bWYf4Uj-vz4q8EWycxhhmqOR8BexZWHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLp3PyF653VF7yU1VueC6kh-vc-4ONGvlgCGudAVDBaqC_6wWPMa5tEd1H7BV4YCsE0hpSooZCDp1W8Da1ccSnHeUOl2pnsPGIu7VF3Km0Z3768gJQdECdg-GrGt46Vem4eqhLncURCefbZ5fxxRAkXryMJwr8SqdTx54TcNqOj0A6w-DIKCLzVWmeSAt09xEQfzxcpWOaAwf_zgeXZC6ap1YDNPeU2hvjUXHKcRqEClY9WJQcORNKRmXqbgtRQH_4LfifwlPkucoj96nsVv5cpTdof5IqbEbFnGLn20Mg2wswokbdC3EuXf4hyggn5iGFIGL8SvdSR3sEOZRF7w7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhennvcGRcx6k5Hey2RyMt3nYB28Hj1Mjqo3FCXeOwH6e6XmzEplIocuTBNrYsBy4QSD9QfD499c9OTaGNDIuMx9swwmL9iIzYs7qrW_AXJEYqEtXKVLlyhg8vAM8HSWHp1AM_bRPErRGWKYzuK0OOxx8ysYdW3WGDCqhqcdDLslB6_d0RoEOcDTtxBZsp1zjrPNpNx8vHNjtgGCE3tr6squ0Csp5-K84NH5q_nj3QajhgI6KvRMEfj5nf9xAu2R0Brz3j--4pfEO7rRaKoke4whu5FQ6JyDzPTxi_XzXAoFjGeiZ4K_bEDhYj086S7TNUEmBU2Fyr2FUanb4whb2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UygnYuJMMZ9ChuMyGK3ErrC-bNvJcD6zc2JhJyZS679lN1iDUeGMUSFYXUkAUb-UbEhqiSkc1doH7p8w09twt-L_biSoYQlzpUupxdPJG1NyWhURjybIMrBa5Kd57sz_fhI-3Dg0-2KaSx7r0fhWNjXxopEnHMlKbU6pJngz5U3AG5LlnRlPrUm3aCzRmRdM8wGHaXKVLB6p7BYM4VFWLlB6ntfAX9nyrXnUfi6GBZWpKrLU2Eq-bMup2TzsXLJ2D0DU5313ig6jLt5BrNCvfC_K_d08oTEO2QMFdXMQHJocwUQAIjzsCiQ4vNQOTgg09ubJw8t5OqFd-8eiCtGojg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2MDGRtW3drk9O0I7X0L_UBafWG1dQtdhD5iHJ6pcv0I2q6qeiuxWyEwj8LgkjFfyOihpIYsMDfcLcqd-Z8OBaWmaT8ZmDWI3uAYynw0KfzZcTGhVulR1hrlJ9hjCvFy1RGAlv03TajWGZqyjgnOBlOVF7auv5yPwXpgt9I9LAz8_4VhLf2WdcMOHjc9mnMD2vnuSHa_aFMPGm0NqVqEWYFQx0AgkWTYHiPvSWbqupa2AxIlgMwcEwztwuhNwjQ9IPbW2Wuo8_H4nLQuYggSEKEzlA-elt3YPGiN4Ch5C1_w0PkPvaPIXxQA6i4Lqa-zd6XSCCcUevAf6WGDhpzBJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U1g5NI1gieCSzeyigkmabYZTcVkkd-iqxxaG86gDFs74zrznuWhUcNyYbcLbxm9k0ImMkDsyPWgaBP7GTDXZa2bFOdDk9qqySO87WRbfZO65SFlg5JAJtNfKurzYs2uBcTNEjoCKvXmWY5U7daX_htTXRjOKlfpN9aaKwLa3vM0S9jArz9eiB4vHGqeiGZdOh8jiodX-fwS0KWn9yed8hmnv3DcwCn3Tumd34u0BoUZ2PGP-Bbnws07mo2cnzkVz7OijSCEjF3maalQ4bPiHG_uWA1XOyAzPIWeq5A80ZvvYGT00Mpr6AQU_jamthjOFEsgKJEnfrOhtTx-Tf9K6Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KznzGyCmdzKLbBPMs3mKKHlR6Pcoo2yDDQ-7uGyBJ4IUqgkDwqagxlkhQdMqt9fFtfnQ-q6nWUIjs1BeMY6M2uZYmq39Fb8LBEcCwCl7YcS6D6eg8VRgYlmids0ohEU7FQPzUO5oLyChNC4q7s7CKYLdYim9-HSUhTtZZoBSdr2V7pyRVDYo28TKg9wFMhsBxpDiDauBbI8LH-oqLFMwSZrR1DiS5F3forhv_29PnB2RTcYDdYhKJk_c4oPqhyqNS1Tx--rG0dcWlKu4WvajklK7ODT8PH23ZHreOWrC7ZoGQ5_DDgf6PQXQEr7suPcE2E5VzwNUidCdXVHT1y5i8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY5w4x3Ro3KDayoLEpi5KPJ1B_bdJuwtTXoUeSrnvJ3FoFqBDKcd7LJ82u24tcZ9YZWRGsruZ_4r3nHSjVF8HuhrJJHaRQY12G34iiX7_r8K1j3HXS0XX8wLza7yvL7SYAHAseMPgfXA_FYQjZH6_X-H3NOplTk3gF3PHj_et_1iJBFSNGuDcv9haHLz2DfXMDSWCIjQE4TkdApzY_HLK99u8u01Ovjec5MzaenFufnkE1Aj0gjZDPTmK3wduUXBBI9ndzmhLzLP9MHfCWfkyCPeb6K15tR3wkFio2xSsFjYAF6GeXKgURU0A0Hu6P5fJLQKHniDBHfAAmgNmxZ-hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNeIWuOdzCSaoSs7LCMXe1jbVm56BLC8sszLyi3hraiQGqzjZYAEt_ts9Lwe16HnJirScCaiNQRPoihA7X4CPNzm3vQJuYg8Ns_pCo0NwGxQcf72wkyQ1-Q7Gg4OXmU6I6viMeQO3MFmvw1EQHewF2N2iewvvHtsfaAI6BCfpRWVliWZxOlQhWAqbFKyFfNMD3VcHAzgXS_qgjflZiTiIlm308ifZ0p92MNyXsTYRf7Z1xn6or8UPTVjqzXU0l919bawRqeTwPzI-sN2BEjluggGor86U6BnSM1IGaQE2xFWdz79rLDecC5_8NoMKObtFG4A06X3syBeoL2Ro3tZlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rcjh8MrZbOTaxDRhtuMTZh5-oz5zQRLF0VvXqNe-0Evh3r191fOXxT66uAzJZq964FTwj4i5JgsrLAxnSQFNC8r5ibw-6wjL7xFJF9BFoyFE8A2DSlbDMnURzeWf4hSMW82Ep9vqxv3J-XcIMPAaFid_wDtJIZnZC-3_cXCZyQM8I2dbgRB1qaUkUHQjDgH769kTR4ZF85r2LBbC-Nu5uvco6_AHirZFvJ1Js_Q-MfhSH6ZFjaRXWUYYlUubcHKlsjSmwPDjnF34L-WHL2nedVb7p1ZIXDmPPObhHR21kmXK9cykL3Rf_Tkci6LjGKwRdbeSJz5TcovltTyOCFETYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJ4A_DCzJPOHNkhTJGodlQOmCQzej479CHR7avXMZ4EMXic5tUR1FVrgWN3OLDBpaqXnSUXKbFbK_JB2Hv5NbVSmsfUEz_DF7xkB1Iky5uJUPjWwXj73ewaBsbfdQ18Q1Tfgs0HZ62jTHzhY0hnjDovvmcOCGUjW7jodTpky7hFlx_iSSfmXkQPtOPyiDZ8bPM2oGLbpFeJN8HpLU0KDP_gziOemACEBHWnT3rqqDPGGawy_P0IZjI9XBN_KTZmfvXqx-HRxY7KPMEtInUH57yc9QwQOnp1IM7ViWJXQqveiZaerntfkBU3GQJ0uG8dG4m9ITUAk5kuVNtftgLfKdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsuMBmeTKJAr96PWeCOifotEAGqsv-W3oqyhS_nRQd2e2RMkGljWH6hnkN-rfnthLQOv06jkUP3nj5y_9qDYCf3gcyRNAkp4vDzwYDHvmpWYTa5p86sWl60J4Zv36N4bHcGv1hJP2wilOhPldAdwfhKKbQLzKlQeU8lQXCcmGc797enAjWCYdPJneiY40SDnxa5UP_Zunm5LdEVFbXWbb-wIF3yWkiiDdoKE20j90zsEV_P7YepmjBPeJ6nJgJ2iq4g-U9qz5avc-uMm_MGlUdzjxiwAaSF62qRHy9QeH_-qjthQ1Obsvlbmo8_VFNssx3hYw5VGjpDsld7EzvzuVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifnry7FQ7V3M-LtzG9SMMaoemr4i83qR9tLxxiDpQGZtGcpVU2nJhU1H9E0UYHMv7L5MHL0_Io6dceW_m5xzFB9ruK6S1LRwgedttfJifY3oyy4Xw3N1LVY7G9mbsL-uQMtxyIcMv8lwSRLA-CpL6N86drzax_fZfOYphLb9STAUK9g66W8n73hP-kyyvitENpFEdeOoiPqfrMKqS7l-6xNpD5UfumyQ6Rjfv2dAzMVOG7DcziZJA2tN6s5mQR04YKBES6R3TQenScNRAGOAdPkLvy-CfuBb3krbWRs6G91rAIhxzap5pVNu5LGcSYQjg_xiLXTLFG5NBYRvFxe8ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7G9AyWL5d2JiAPGJK3X6m-pW5PQesPW-0LPVP-8SzIfEq78jImzJPhLt_iIDYCiWIVCtNgDqZNyHk14VU-cItG4t8mJ5Esxbz-absjze9-Ou_jThkvnau8UrcBpBxj2w3U-r5nQwCz3oplzS5eXjGEri4AJHt_GbQuyx0U8swUz1dJZCh5jCI3ZC_jcMwFGt6Zb5kYYx_Jv2vGK9q1evRjHnT_fJAVimEClSBHZBfLuFbNOoS0z_enb2SG_jc6zgTWRCUS0Ddbuinau0q7jHGRFXBE6X7wh2aYwQQhjJZPZavtdsrBvorDN5Yl-gyzGVhT_XrVRili4JiqX4AEo_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AidTI_M40o_tKY1jOepwt7GX8TnjN_w_toEPOLnlvldEVlvJo8getrg2KXKZYkiIEdQz6o9JM9ug8ZqPCnm87D0HN7HOeVxBon0FR1ie8ajp0PDY-zdkdG6MD7Y2sXv4ojTNvtvJJpDd45MeVexWB2ilMELRdj97-WSZWVOUYYwYkPlXjEcJitWMxDQ7Ke7dE5nONx1fIyrsl0qiMw4LKvr8o-IhWQ3tLuSxqo-jzH_HRyD396wBzVI9HuRqPQ7Nhe6EStdzhDOyGVALTvR4OqgrD6Jr-mmjoMPtdl_wbQoWfpDpvGnjVSu8KTaFZ3FgAA0QpgiS84TFXtZvckYlqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eH0GJFyxqRpju51UcbHdzUk3QBvnNqjkfhzAukD85-7g8ZGBocA1A2zF2jZWqVEtkWux2dE8ymNA42eJpsG6n5MBMTX6cFaWkM4j52-7SykFSw1jK0wIlBZVfPa-xrhZyuLMuJC7QCFxfWoPx5q5EA6FXV5iKvi-IzpNys3Bi8ZEPeLkQwi65J_6ESfp9Gob7yoA4AROXLkzwewOu_8Qg9CVcN_RYG0OoXqfc09v7wDdQfS3yda6Qc9y_A47mQf-P0-iuTV8c-dVB4IhO2X1UaxXNAyJieirczqkxn5yh2QKFHO1lJFVNBrjvVcj9Fjna2rp7klJrECPYY-2SxMoUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVrkwYGaSLck0aH1HupP0GxKnHksQAWroRHISpzUpy5rWS6r2KDILotXXr8iAATP_vfUf6oelJuwpoDcUvlGEDIXceNwVJl-FzU3pc3m8ztxbb8LGK4N9dNEeSI4O65RHK9qJYPHrT0btvjMmg6a1kfxSUNni-8sofA76Elp7hh4ifcBx_YtMfb4wZrjzNJTZ_G1iSX05Iv2zOXsDpOlR07wVsNgwd1oXVWJMcXWEquGWCwFOxGzmbAQaLcxULu_IxnEsalov0vhg0s63naqwo7L8-_OcWn8xYfG7nMpDqS2fPG3F8sdl3fGNeRPU30v1bSZduovGtL6d1S1-HwOJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEc8jUlocddmoSQIYH76dMI7gB41Q1Zw11zvmJX-nPVKwlVdTs6IurVg9em-np69ULDbLugZyLMU_9k3L6-dF4RiWwHoNMuSYAMItO5Iha4NhbuFMWdrTeTY7CQMEeC6AU3Ulu47f6p0rF9dCoj5IhO1nrEV7PNnSD1ExLOJ3uxRzHQlNWdNgOTn3_70JEQG2C7_V6dNYcOdxXLuDR43h2kNIHovn7hQLt4qpimwz4ztHRDKqdFRIymw8A5GqInFprvcUzK7U0gJ5wt33DpjT5KQvD2xxbOfIfjjZMXGB0IaWfkjjIVu_13N7l2KIdJBWdw8el-2oa1IBv66VOU6cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pesWeN-iH_3_tzaIXWw9VchsA-Cu-Knv37vZo5oH8Lg36xUIGTQuMeP7BSHT0sPDt4s_oKzxu01roal7Fre0iJjD_ardnj2zugPw_ZGL-4YmisbyFaZUwVQugCgDv9dQbB1WVZxrivmg7CT4Io6obzElOXW0UJrqdVo0s3z-qUvXyR6t0ToiXcURSa1uJUUK461HVurpbl8Hgx1pFrd2UOjqQMkfHYJ-m9C5TVI4lNMW96DxMseIKhOWH7C62IiTsA8ccbtsxAxUQVzaG1GTKnsg2ecbr72YeaUW1bPs1-fe8KI3q3waz6M3qYHIC07dY7tELY_1WUeJHIlAs6tDhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A84XEFVcHDugjIidY2eMp8eUcKQDUlK6ic2vtlrITVZNDlA5y3NrIMcJtOOna0_2q3ABhoZL8ACtcnbVpA9Xqse9tJcmxdMrG9kymWQ-gkcSQ5ofzVNFXAbPPFE61SXdsISn_hK9rxivYzNWTtjO5Dp0SpUx992in4538Ec_LHwBej3uVwJqmGIWQAAEoreT14M7gVQymbXwBVDbjlaA_V5nMN_X-HEYsvCZ2SZF2A6hp3goTVACTZ0muGi7jEfFZ6hxeM3myXHWFzrkV8sqJcJjV2YJrFXJ3nCgxACCO5wkQ13F1pnooMVwauirL8k0CB_P9Kk26hh0ETx92YqTRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
