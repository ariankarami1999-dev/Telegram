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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 19:31:23</div>
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
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qLKf4u-ybnrlTBuSlyp8n0zBvrUQ7Esr9i28xdAllGpAuu2mg3cB0_xzI51F3goxI1kgJ2thsfSa6ALG2sBOCYA0K-IdtJMLrkJWoXcRN9KqQhozkIJocPrFKSCHys25TyN5x7HcViQjAb9K-RvDegdsyr_z4YDBW8mhf81k4j9YTUVVQSoZuij001JbniJyPjpJnFajyqksJZjopGbxpjOr_24S7gX0LGK3huLBVT0wjmFCJw9k8x3caeG6TbfSU0UQ4-7HkdP5FKTvS6_uFFzCAoGe_I-WgdN3Y2GoVjPymuQ4io5MNJrJaDtxyxmrurFHVrsu3bPxpCLc8b0UEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYnNukPmxeRiLcb0uSpzyZoHGqlsPKdRiaC4TW-wptsxY48TIcneX8zG7hj5jxnCYmViipR1i0WaYBddfuSM4IdSfoONE6HpgXCwOZLSkmzQv7sBLkmkyd-gucAIiPqZOF7e6KUNNE4e9JXTEE1UyvZAlpn4x2sLwpxmPkUHfHs9jpYcMmZA1AP7zAB97ljLLSNohPr7QxHwzJvdm57Beg5MtI8FgNDbHHOQVLXkCrBTEUKExQI-RRXZgZamCnzy2lJpWEdOCorunqdXdOrF3b1Xff8ANalc1gLIBApb-AdKuLW_S9SjKv9P6cJ0HDA-ZAcih6m0fMoNf6IsiQEpNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=W_LW6h-LpEmzke4SqIEH7z1d1b-SFLZZU0uZ7Hqqo1-KFwQL0TePWf8TjCDntJ_c3_mMFw7lYOHqc4W-P-jEqeR2utSLp2Q4rHelziKHPDB34-GaTwr5fD6dms8B1SxD1qW4x9NPOvxt01_MqZC1a4SONgHZfUa9bQB8ackFsdbuztLBxgKclNuA49nJgDZHZmiw8U2IRBIdipEm0L1d41oNSZH0i4NNOvNH6hHDokIfvnaBB-0X74YEEzFXHZrz4bxhXXwh4NDfNTEzbMabohQsY80Z2367YQCrWoduy1InoEsdvRjUESaGVM_GZPO3V0QlNWbwmaAzPJFo4s90bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=W_LW6h-LpEmzke4SqIEH7z1d1b-SFLZZU0uZ7Hqqo1-KFwQL0TePWf8TjCDntJ_c3_mMFw7lYOHqc4W-P-jEqeR2utSLp2Q4rHelziKHPDB34-GaTwr5fD6dms8B1SxD1qW4x9NPOvxt01_MqZC1a4SONgHZfUa9bQB8ackFsdbuztLBxgKclNuA49nJgDZHZmiw8U2IRBIdipEm0L1d41oNSZH0i4NNOvNH6hHDokIfvnaBB-0X74YEEzFXHZrz4bxhXXwh4NDfNTEzbMabohQsY80Z2367YQCrWoduy1InoEsdvRjUESaGVM_GZPO3V0QlNWbwmaAzPJFo4s90bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9Z8z0K5QN3YjOaLAH-wOmFnnV2RHoxH1kKFUKd21bk-ktwswrhkTbkhPaJoYbpabn2o6jtpH5iEWhiowsTzHzNyooDpoi7g7B53WyvfxXhc5OlvanTVLekSYlUPoTsJcxogMsfOB2a0AO3gFe3XaUP9-rlkphez3igr2RibWU5hHiPBq7aOJxs8sfoDD1e0ho6GB8pkKeVoB4CXvO336FWX-MycIT5gnP3bGO_QfkfuBbPe3dnJNd3l-6GnMGEYksYQXqe_U7HneSY8opPfYveXYv80vX8quL9YyNC1clpVhtDZV7dxyFnSjIgmEfq2Ww2dHM9pC80iPtlxwUJIEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcApaWyesX074CoP3lDbQVfJbSr0AUGukH_KCF1PegWPqAskkKHClkVigxWvbw8DXlZt_XjcjqGey2OZ8Ksr6cPXAD0WbS5atJrVE2mq33FvK6QEMSlk4Ggciw_qdHRL23hO3zRJLt4Gs3V-iE2kCtWBP0Qr5JtHf3evPDbsu-rv-561BViB3tbpUkdHoPpp2sqliuBeIq-fCgkOMM4NxQ9bCWzk3w1xoZjPq1Dus7C7AD-zpfd1ipyTjGpOZ-qph4Zdf4e2MMJUpAcB6nEI4i-OLsbE9S325lGNNo1LAPUFrhYlGN0HNPr0n-GXKjClVKp1ijin5KmZCBI8Ko0GEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qz71eOvpwmWscgntpRQ4INwXrXc57EFgb_SDMIcd4MRC49wQ_C4beG8wCsCBnvpKukaDqv-bmFfPkEg5UWWlDl2kjNLK_J6qjvRUo8qqYHfKxh4XF43JL2hI0KFnk-RB8OWhpqFcK1mspXkiVeeE7j15HJQXW8CBSv5bUkakADafMzbMQIu2hQYhxBFFF2vaBit9wa_d3qYSYbxyuCf0lj8OrTOdu-NT2vlnp9nBvXoBzfqaV92JhFqmdizItXaJ44sYMV6pHK1SohHXMlKpbCRVNqsKKbV5BvWFW8ZyHV8yU4uei_BXxyYQtMKt6Y7hVSRB6ZCkN3N_4sjE0yXhjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=b-n5UYrLrSjikqJzCKNaRiZmNo3IFGKgNSeKG7iinTNfJbOu-kmdxl8ytSlC_4c6BP10DR9eHDqZo6QQC2DWMC85N11MtJAY9N7ihtrsdAe992_ih8Qq-i60AgujSv6i9-q92ahpSD95EbpNRZmdcBVNAtSsWfNPE0ZylA4ynA5fMfADRWSzVUC_ysFQtU8R9mDHgvHIWh5mD39uQ4Eeaoh2UQSKixKLxAC0SAHzVeeR3cj3J9zB-Lui1eqw84YqJDAdfvKIxyFEjsTUa2hPg6Y_-42gua6ImF94TgIYg9FAvOdOJnr0x7IbbCUcxVKbf7YHHGv5zDTfAR9C-CjGMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=b-n5UYrLrSjikqJzCKNaRiZmNo3IFGKgNSeKG7iinTNfJbOu-kmdxl8ytSlC_4c6BP10DR9eHDqZo6QQC2DWMC85N11MtJAY9N7ihtrsdAe992_ih8Qq-i60AgujSv6i9-q92ahpSD95EbpNRZmdcBVNAtSsWfNPE0ZylA4ynA5fMfADRWSzVUC_ysFQtU8R9mDHgvHIWh5mD39uQ4Eeaoh2UQSKixKLxAC0SAHzVeeR3cj3J9zB-Lui1eqw84YqJDAdfvKIxyFEjsTUa2hPg6Y_-42gua6ImF94TgIYg9FAvOdOJnr0x7IbbCUcxVKbf7YHHGv5zDTfAR9C-CjGMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Tp1FqF36FtFvFj9uRCMvi6-ipR3GqCr6wUYQipGjb9Imj6AS4CUDp3cS12XQxmJ6t7FekCgNUFFZ-BkSLSQCuneiRFEe1DWwxOgAo8_q7RtOY8Cg2y12ZQoV6vWX_GyB_IT7-MBL3K4_i57uQuS1o7e9KE6dW3HSAwPeNNI-UxJyELSGsfxYjUadkU7rA9v_2SCZq1mAmuZFmXclWQ44H7V-C9zrdoWrPP-ExvX1YbDkvQAfQzSVlvDKs6JG45FPC_COhTlrKJK258hayZHNMn2co-Y-X8FxOhCyibR2vbkJ9gjg8sKWz8Ebf7gdOfGYd2qRjQyk3HKcZifnBSwJphXMk-ETAITfmYvbkkzMGVBBKiXR0QYxEugwV-pnLKSXlqK--Yos5ypPl34rer1CQgWsujgVMGkxwHNR-1gf_YLSsElYjzB9PiMBC_12sonHpFsfUaiXYslTPgCZXej7cRUOawyATFmKwrSBhs5iwGDMFks39ZwdSKH6N-0xxgvnoMHZ2KbW0P4pa5WH6XgvbSZ-ZYUaELaC8ZjwPG7OSx19UmdzkFvibed4sNvF_qNpizrCE8qOEbPeFVSheuh-prHP_RXR0pHju9PqCrYPNH90h3u72AbYwfaTpjgqxaT2rbdWmsQ4kBCP5GvsAW--ASqdJvUtpMdoYQ3wzV8BLtk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Tp1FqF36FtFvFj9uRCMvi6-ipR3GqCr6wUYQipGjb9Imj6AS4CUDp3cS12XQxmJ6t7FekCgNUFFZ-BkSLSQCuneiRFEe1DWwxOgAo8_q7RtOY8Cg2y12ZQoV6vWX_GyB_IT7-MBL3K4_i57uQuS1o7e9KE6dW3HSAwPeNNI-UxJyELSGsfxYjUadkU7rA9v_2SCZq1mAmuZFmXclWQ44H7V-C9zrdoWrPP-ExvX1YbDkvQAfQzSVlvDKs6JG45FPC_COhTlrKJK258hayZHNMn2co-Y-X8FxOhCyibR2vbkJ9gjg8sKWz8Ebf7gdOfGYd2qRjQyk3HKcZifnBSwJphXMk-ETAITfmYvbkkzMGVBBKiXR0QYxEugwV-pnLKSXlqK--Yos5ypPl34rer1CQgWsujgVMGkxwHNR-1gf_YLSsElYjzB9PiMBC_12sonHpFsfUaiXYslTPgCZXej7cRUOawyATFmKwrSBhs5iwGDMFks39ZwdSKH6N-0xxgvnoMHZ2KbW0P4pa5WH6XgvbSZ-ZYUaELaC8ZjwPG7OSx19UmdzkFvibed4sNvF_qNpizrCE8qOEbPeFVSheuh-prHP_RXR0pHju9PqCrYPNH90h3u72AbYwfaTpjgqxaT2rbdWmsQ4kBCP5GvsAW--ASqdJvUtpMdoYQ3wzV8BLtk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=dANZo35FaRrJ1oY0yFi1MUAw79B9wq1TBw0yVk87Kq2oCXJyaTU1iLTo2usqzgLhM_ylvqUFgl04GRfgWItg2IOOquAQCbUXsbolBGRy2lCMEvdMOwCNlk7ajOzY0KVq0M7eZtqnmNDekoXYg-H62yVpkFDXvdVAWwYxd6lN0Dwr7zzwDZrZpnLHJc5dxLpOb6n1i8IfPF2Op9irz0u5CF_uXXjaDlG0RsiUh_PjLzg3Ybi74fWdpBDdRDCZR9ZQ0d-fjUwCWdJnWGcDLZc1vJTglIcaLQmEvgGq0tdgHrAAy_0VeJOXIU2vuduLe_br0cwkEZNAhtIxzayLpvSlFIorcajlQieJOBFKun76bSvk3mi7xj2Kw3RW54Uj8wb3J7wbD7iqjksvWpAgqdCPVAtGnaBbxE2h1sexeXVuHLfDfMAPjpkPoJbEzSlys6IE1gVmFWkG50y8WWaqwQukRf2I3-ibmzR4Kc0aB-MoO031t1GA6FY7_MDZ0trn-NiahdkS2EZwjPLkeVkRhI9sU0FohNl2q-SPwa9fYKdKTroubJTpcpO-_TOdkiYhyES0sPZ9-BkAeU-rAdffPYVhn99a1e_-nS8E6AjVV8ZJtNcGG631L5_wldG8dQHPKc3dSOkeb_482o8D10-GFwFy2PxJWR1lioYCKAQT7HXtRpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=dANZo35FaRrJ1oY0yFi1MUAw79B9wq1TBw0yVk87Kq2oCXJyaTU1iLTo2usqzgLhM_ylvqUFgl04GRfgWItg2IOOquAQCbUXsbolBGRy2lCMEvdMOwCNlk7ajOzY0KVq0M7eZtqnmNDekoXYg-H62yVpkFDXvdVAWwYxd6lN0Dwr7zzwDZrZpnLHJc5dxLpOb6n1i8IfPF2Op9irz0u5CF_uXXjaDlG0RsiUh_PjLzg3Ybi74fWdpBDdRDCZR9ZQ0d-fjUwCWdJnWGcDLZc1vJTglIcaLQmEvgGq0tdgHrAAy_0VeJOXIU2vuduLe_br0cwkEZNAhtIxzayLpvSlFIorcajlQieJOBFKun76bSvk3mi7xj2Kw3RW54Uj8wb3J7wbD7iqjksvWpAgqdCPVAtGnaBbxE2h1sexeXVuHLfDfMAPjpkPoJbEzSlys6IE1gVmFWkG50y8WWaqwQukRf2I3-ibmzR4Kc0aB-MoO031t1GA6FY7_MDZ0trn-NiahdkS2EZwjPLkeVkRhI9sU0FohNl2q-SPwa9fYKdKTroubJTpcpO-_TOdkiYhyES0sPZ9-BkAeU-rAdffPYVhn99a1e_-nS8E6AjVV8ZJtNcGG631L5_wldG8dQHPKc3dSOkeb_482o8D10-GFwFy2PxJWR1lioYCKAQT7HXtRpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=vAo_ECIZv96WRFDtIvDJjwTAVTDDwkQ_10Ky5s6msziy7lwtzOAYlHjtnmpPPxb86Oe_xBs8q9Ynx-c4QkvIKWeLfOQZe4AMDFhnvkpPE9RkIBsShHftB55mnW01Na44-HyhxUFY2vwFckAAaA9d230pA-8orB6N9N41QdYKenpaOWDBA9jcJXh92JfTkOHPcm7aV8gtN4BOhlPNrwzdxGQjYFb88gUxbHeLj6i_SLMR7R4psYFqV5d3eaA_5ppaImqe-xt9wzLgqUhbZXy-D30M2es6hh-kjhpvwbgS8AvSRXZjjxPPbUNADCEW9R8dJYJ0ONBJZy12xrubGtPlBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=vAo_ECIZv96WRFDtIvDJjwTAVTDDwkQ_10Ky5s6msziy7lwtzOAYlHjtnmpPPxb86Oe_xBs8q9Ynx-c4QkvIKWeLfOQZe4AMDFhnvkpPE9RkIBsShHftB55mnW01Na44-HyhxUFY2vwFckAAaA9d230pA-8orB6N9N41QdYKenpaOWDBA9jcJXh92JfTkOHPcm7aV8gtN4BOhlPNrwzdxGQjYFb88gUxbHeLj6i_SLMR7R4psYFqV5d3eaA_5ppaImqe-xt9wzLgqUhbZXy-D30M2es6hh-kjhpvwbgS8AvSRXZjjxPPbUNADCEW9R8dJYJ0ONBJZy12xrubGtPlBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FX7fpzUZHaRLWeC_H0RQteuy-Gtf1VkHRc3lOXbb9qTS57F8cBcd3rWCk6EX2-VGTehCDgjdQsD2qENqFwNJTxD_DK22XqtfNzet3-Wndf6AYvGy2W2TM5qFXB85BEY0wLtaJJgWDKwJA--OjXDyM-KQgq0Q-Ov1JZ6Sj42-nAFMHzZZtMqw7Tr5b8onBp4GyPZPOmsBxAUSmBtrNk7PQuu5L96i4YrTYkIRJen96mBpJZZFmIoY-R7ORxZFSlSZzqLAqVq8Ctjj1uAtwQBELKigv3w7iyNebnzHzIlX8vTzOXyy2ELfpSL-TIl-zXJZlwVntu2jq2Kvmg4mpbtmSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoaM5giiVLZ36-l1MbdXnKOTUbwmPWoJbJdX5g5oL74OtdZuvEwkv6ySe-TIt9pHSUV5xMXGeY1O_emU4pX1K6YG1zFfhT1y3paoWPRqS6Nzn0FRwcIYKXkqyoYDe_PJcESpkclXDZeqsZ7cZLj6nU2fbmVGlw4D0bD2bQNP2ogjHMfdx4wo4is1AegdDD_tL35FFtgWgmHiCV5pEyi7CIiF3mS7oWXPN_tL88iQYNuDFuBKeL6SRO7xWfTzJPyAK-LFWGEpnOB_fA60CIj7fpDOtWF0oPa-X0sDNi8AqejJ1PFvF2-mmBl7LYcNtsKBoqF65F5cBwGfuopM5bQCSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6F6E5Tx1nMSdpTmPp173qfm3hukqHKee-SmtpTsJ7rVPuOLmB_lRrHpbCTpSMLk0NmGJQ0bPL2ktha5zGZN27L2ziduAVABlzlcYb46rHvWZcW5jjgXjUOnLfbRsbLv5tRFCrma1f-1a5cZR8B484tXTPiuwVtKpcCQQkcIR91mrNKFsN3AdqtKQSijQgizfYsqRhBSiIk7tFbgz-nk3eEatm8-AeOM3YwzS37zV08Nx-D5-Rjs5JkSktv2rrqoHeP79wRXsoI1B3SHtj24sKijaHtS1-HnzqYhhioz08RbnhyrQFrfe3-O2S9oMhI1pVO8UFmVdRZdmvHkVi7UTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QC8UBcBxm_ZHVPufGKQQ1cQ3FAHnzZjf6LtYzeWwf1r4JXxaeVe_SCgsO3jTZntV97nsTH1HX7wGnuu2dNhzGW4WlUCwkjQvyV7ch6o2a44quKwv2vvUvyG4HS1qHFxFf2Nhrad18Fk8-WmzN9pLb8pMcr-qxq_fnNqzPkqdmm_ZFtsxVIxZwgEbbrJO1t1f3TAz_pH3vgaw7d3Uso2DMkGg5giFVAaairWO1J6nMhp2uES2JQqa2P4JDmUgOaDMGEZkFt59PuJiBt0KedvZA6zAQhG8SKCieS8mER0I1vCgIBptmhtfWQH3vHD18ez6ali7Kjqn6v6D6h6J9-M2ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=OIzn76UVvsXhNfz12Ni5AVXys8yquyPrBTXCK4Tmd2N1rLMsZ0y5z8y9BdMTLtJOhZd70ZZIJ8NecX5zuJxoKNwOabqSeeOILK24QzadmMv7Q-sF17SGari3traKCZigzkTDEhpKo4vNEZ3g3ulPoFQ-QPv6qIQjS1XzqyM04OsGJwbex23X1e_UK55KQw32GAy4FcWeeEnvykNDFhBztinamMzeC_C_C8051aDEN-OBVvcADYUvN1-1hoWR-oMBz6AF-gqxL5KzqJxAZCz0fvwNx7ifhJ7BynG7cWh4em0rboRApe-pDQ-SCXcLk_OQkTNMaxJ2-H6t44xBL9tfag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=OIzn76UVvsXhNfz12Ni5AVXys8yquyPrBTXCK4Tmd2N1rLMsZ0y5z8y9BdMTLtJOhZd70ZZIJ8NecX5zuJxoKNwOabqSeeOILK24QzadmMv7Q-sF17SGari3traKCZigzkTDEhpKo4vNEZ3g3ulPoFQ-QPv6qIQjS1XzqyM04OsGJwbex23X1e_UK55KQw32GAy4FcWeeEnvykNDFhBztinamMzeC_C_C8051aDEN-OBVvcADYUvN1-1hoWR-oMBz6AF-gqxL5KzqJxAZCz0fvwNx7ifhJ7BynG7cWh4em0rboRApe-pDQ-SCXcLk_OQkTNMaxJ2-H6t44xBL9tfag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=kqz77IVi9VEuqsTaclreL06N5KWoHteaioIEjQSCjfFXh434CJJ5BBTYFdruk5oxd2ao3jhIDdocZ05348rTWWP0YnU0ir-xCHl30UO-wBesDz5oMXDn4y-6uNd7ocoSNWwFCtmk-A7O82LZx-kYf0pYNgDxpBu3plCa56eURPJWiMWKOY0ckARYKmtQIPuexXA-K4GVwEV-wUcxViWKFTyIyknarzTe9xkmMaN29zKl390BOPciLLdrs95eq_b3834rkCyOhUrUNLfGo0C8l4ztG3QgN2_eDZbodANSS4zs9na3c0w4Ps4n9N0_fGkE_Ejh9Kf4h3ffbTpMUbgAbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=kqz77IVi9VEuqsTaclreL06N5KWoHteaioIEjQSCjfFXh434CJJ5BBTYFdruk5oxd2ao3jhIDdocZ05348rTWWP0YnU0ir-xCHl30UO-wBesDz5oMXDn4y-6uNd7ocoSNWwFCtmk-A7O82LZx-kYf0pYNgDxpBu3plCa56eURPJWiMWKOY0ckARYKmtQIPuexXA-K4GVwEV-wUcxViWKFTyIyknarzTe9xkmMaN29zKl390BOPciLLdrs95eq_b3834rkCyOhUrUNLfGo0C8l4ztG3QgN2_eDZbodANSS4zs9na3c0w4Ps4n9N0_fGkE_Ejh9Kf4h3ffbTpMUbgAbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQ-fKTXSCMlZUR1W-UFT3aRHewTCHNYuKsHHxR3fS2v6EhJgoCqurtEp-odIWl2SDcEnXf4Jj19AUt6Zp7fznQBDaZRcLQBY95L1VrMhDsxE0wYRHlANRxo_CBiPrgmojALE27AnlD9cWMC_-kD-qDum0LA8b0-DitA9j-7ISuxuwpDMbiQ_O6PrCEOG1eOkYm1SJgtPbXaQuAAhAx2SC7cKSZ0ujA-DjBzcc1TjUpKcCgJHXMIAiXQzq-HKPEj2XBuh8L-E3lOfFHsCGc9eRL1N9gycfn-1WkUaIF_GAr__A2IDJDkHreBsOfNE-kcMR4JkJHcWf_IltmDToO-j9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGU1U3dFQAQwwMHQsJVEjyhp-WOcjHNowLIq22279cfC1nvvn5nWoalqHIqrGio5ks6j07MU7fiq_3FXsCNmXAShXtv7XQl_QV34bvyDX4ykwAqAMb60FsQDLyD7EVBw1iK0SidOmmaWYmCQ2vUBQkidXr9UKh4t3C5E_6xUaL_aOhex_UHv-B0-85QLtiCt1nSa8H7avBC_2wb7GiE5lT9fUtaD31nTwIZy4qoDszmi_fDwzVuiq_LCNDJUFX8IC1cNghOn5kemcTl25z6NRoZRVeMPJAmiVYaxmXTJIbsizhL_-2UpqQOg1UuD8AFiRzERBT0HsjT8Y03ogSOA_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQjYGaU14AsAbGdIHy8k5AdoNVFTKqA9CiRc4mUNvNf9u5PT42JWA2JIZrQBQhBIZEm9YCtT6Ri4eUhCpREL16a0jO7WRBFp_0ReV5S2qnyv18CAo8RLDsAPQgle9e2YU3TLwUfQxokraDOjXot0MCTf8QQFiWbDxORiW0VdKax_b0GwNMyhAcmkQIdayAeNQ_vk83r-eBzA8rRLGMsk9JZw63uEsDvXWCvtw1B8p_0CBqNmJapCU94YZr1nJinXweQX4FiFodRWo1IccAZ4L95gjXs3wI6Zlj9YOKfrXRCYgQJaxpLrfT8cJlzLdBEgcUdhG_M4qseuVzk7e-ADrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1o0iysKgguOq2hd0bRDJxnHQNP3VrYTqT3T8hE326eCp7PUvO1XbUw9DOqrktKv74sBHOsGcEyatJL78dT4gwgxFjuI_eqJu3PixfJfBT_piHF4bGP73aAwqCa7WVVmKy1m9Rl_P1JFguXwVhdKnzw6Z_DedLINxljcdxD5ZHsEtLBruy6fUiUwauOixVPzoqaY77oNLaQbaxmWQ3_2f4PYVyg0LSKvjJqu3cCVk7lRAUH_hUlDzEVm7jdy9bhzYIRt7OKZlJ4MqBAcN6NbL4lc7NcGoUytiHNc3haI1ykY-kKejgH7ctRbs2zhu5T-DcimxS4QRlotHDr4LGg4tQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=oMBTCUblKKwuQExdJYUpzmchP_2lE6H_Q-eDKAGoYrnzrL2RZoT6zS1JDfnR--w1v01OT5RiaOFqfatUubSr0BCLgicFAK7y01rpelMbHCt8Jg-2xRRK3chStA1vZ_bw6Rb_5Q59AIKnFE1wUiUZTf8_4ke9CpgveVwCMB1EjSgGyzhJts4dHqw6kvhkAZN8jS2-WGz4BLiT0AFvJNe5hiZtxb_NNVUmlhvs5_JK2sGw9JUWZhby2scH07c8aFnjixN_7U5rPiAaMY5yiVMVLWHBkqtHUz1ya0DD28SZGBXY944jnqPCCpf_WaQIquwuuDVAiswhEjqiEgm8AMMreQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=oMBTCUblKKwuQExdJYUpzmchP_2lE6H_Q-eDKAGoYrnzrL2RZoT6zS1JDfnR--w1v01OT5RiaOFqfatUubSr0BCLgicFAK7y01rpelMbHCt8Jg-2xRRK3chStA1vZ_bw6Rb_5Q59AIKnFE1wUiUZTf8_4ke9CpgveVwCMB1EjSgGyzhJts4dHqw6kvhkAZN8jS2-WGz4BLiT0AFvJNe5hiZtxb_NNVUmlhvs5_JK2sGw9JUWZhby2scH07c8aFnjixN_7U5rPiAaMY5yiVMVLWHBkqtHUz1ya0DD28SZGBXY944jnqPCCpf_WaQIquwuuDVAiswhEjqiEgm8AMMreQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRkPDyI_S6qffwRiEeIjcAFWUeNr_D0NDSHIc6zoGIS4wM74dVSllLl5k0FsuEKTabwOzJJdhyz6D0iiFvQrerSGHTUumWDgBrVH8gpXHy0ask5VgAHG2ff-tSA9-p5NuDwj3wAFuC9m5pqhNnShPHNhzY_AEQ6iXK2Bw2jfEOVM8zCAHbQdXea5u9S4M5uDTcs8YwU2Ng7yOgaILaxqP34XtKVqVSt140N6BfoRmKNkHpZ5GrlFMMCpGFosrQ8usKP3vux6-8PXzrIWHmTrk5Khyqs6Y-kh4NDlkOq1T_NClv1AOTi6Hq7FRYat-HdEGlyFawS9x3_7hPAGBm-x4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUFW2WvxPWI_jaj4YypNCj0oVkSrAvidyLUuaL5k1OawykF0TcnU7VEVWj6I52Y8vR60-1ypPBMSFwqXVMPMN5NCj5eCsttIzxIamG8-W4ullM3BI164j_-j4SMEq_c5d-0BoFJ9j1Qzb6kSx12IDhcuSYnKV8GqL5iSETr6mMr8wEuSTGuUG4ywA5mki71ZpfOlHfQFtR07eve0DVIRcpumSXneN0_dlgLHPUv9cp1w87fGuHRfQZtzUEpJwOso8idMNdnsfGnqjYKdTrmU9tcIIClHVox-nKolvpseA2s03Kmn2E-pznV3R_kWCMl12W3T1q9kFI2JdaaTMuUivg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=PvcUum7AE_CzchHZKwK4V56sXS1Uq2dbGOKNFdGOXlNoOgRoIbgR06Ag5BU24sCbxtwd_EiAmvqDkbF4-8Ss93njTpSCiJSf9M3jwD7CsQQqJbSlQU_wL_JOxMnLHjej_WNKvWEWMQP1jRjmnlmt3eIUEvro3eeXBPq12TAIgg9vmAY9u7cjN1V9R5uuGSqnHaQMb1UZQcCtEbhJUE1H90o_HncfL5GGEe6_bxtZAQAR8ky83G0TggPykrE4U3OxyX2ko1WPTyU_BpnBYjmewXldPyP89R-9IVZZ6pRQUr1pU3JRfwRhD4vHzlpyj2dfnJkVitYAXOylXz_SLnpD6Zfr0dWi1i5daQOF43oUMT8li_YKhSz01-SxK1YcieNH9LRk55GBaavsosRsQwZXJHkx9QxvEx9dkpzMPEVTv04slroi1y1QenRjcTiuVIyleE75EiKb2y8h61qGy9mIRVZlZMzSN6PsBeACeYjeV43VXy774KSnQpji4Unfwpc8F8jwCq4aKMbZ4LnKJ6TpoOV5mCiikAEZ14ozG5I_G56fMBwdVtN7CN0xgPHzF0hBwfA6zqlx-fWDwFyRq-M9GF4MgwKV3gsyMVNHbFpmhPPWJVZlBmVjM1ZF1KrJs-Or_0dzFTTgwLH-eIeQUmUwRG5vQmJhN6AtUbKvgqi0Hfo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=PvcUum7AE_CzchHZKwK4V56sXS1Uq2dbGOKNFdGOXlNoOgRoIbgR06Ag5BU24sCbxtwd_EiAmvqDkbF4-8Ss93njTpSCiJSf9M3jwD7CsQQqJbSlQU_wL_JOxMnLHjej_WNKvWEWMQP1jRjmnlmt3eIUEvro3eeXBPq12TAIgg9vmAY9u7cjN1V9R5uuGSqnHaQMb1UZQcCtEbhJUE1H90o_HncfL5GGEe6_bxtZAQAR8ky83G0TggPykrE4U3OxyX2ko1WPTyU_BpnBYjmewXldPyP89R-9IVZZ6pRQUr1pU3JRfwRhD4vHzlpyj2dfnJkVitYAXOylXz_SLnpD6Zfr0dWi1i5daQOF43oUMT8li_YKhSz01-SxK1YcieNH9LRk55GBaavsosRsQwZXJHkx9QxvEx9dkpzMPEVTv04slroi1y1QenRjcTiuVIyleE75EiKb2y8h61qGy9mIRVZlZMzSN6PsBeACeYjeV43VXy774KSnQpji4Unfwpc8F8jwCq4aKMbZ4LnKJ6TpoOV5mCiikAEZ14ozG5I_G56fMBwdVtN7CN0xgPHzF0hBwfA6zqlx-fWDwFyRq-M9GF4MgwKV3gsyMVNHbFpmhPPWJVZlBmVjM1ZF1KrJs-Or_0dzFTTgwLH-eIeQUmUwRG5vQmJhN6AtUbKvgqi0Hfo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcj-ebIDk7a4YyAHIMWpaPy0s0vRcpvkf4uaxGxfk_zNDAEpZiA4f0rAvC_YTPGiNuF5hKMCT83OZyD_UPYPZI55l03kG9kRcsFotGCU99QwxCGmzrBYBbI2-cc6FkFeJeyBjQd8mxhg2MbCQx1R9fxSanUQ_zH_EWghNCm9QlvTsejraR-x2pcza6Ps7p3zqgLxM1yu4Y8nkqgRA8cfgw5w3gy7cW62HLjMFHsT05lkienT7kmNZcwo6Vusx1K6dtMO2yAPrdLKTWjYuIlKh9uEDeWvEWKwuqqshjRhdxEElvkaSI2g_MIXPdmWLpLTebNjttdy_R1CuExO6ApgLg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=GyVOGOPJmXl8ifeY2RZNfDgYFtJePPjIw3U_4fOosxJ1S9VGJEbstQ4uT1VgJE1M3KqrS_Z6YqEdnPbJvQHv9wsOR3pD0zpSLZvzC0dxtnF_ZHGnPMEP26j-yt9QH3CIuEB_L4yFVlBmACdv6aLif20OzbFdU0FyQmK7bPk2njAxpIR1uxwSDKMZr13dujp-kEkgf8BrmS7Hc7_8UEIvZBFJSmOqVXiSeXNF1yllpgrY-2K1lHEZgqCaehZAMwil4OX2xopaYAK57sR0k_A5H-mtGe9mi-O8oQNHzI3_PxPDI406MzFuYJklrOc90ZAh0VVRRna9LnKNxWM9mZJDQIhZ-Sgk5ySku6tfkGX43AFsYQPLNzJ0ZEMBgmMLA2JnDwnk1ZiZv5a8u2m4RR5KXUCwKJJNDRxlyI07sughWCdAmpiSSEYyCdVpDXeXf6gmKulDSSkHBUIdP4Rs_lfV5nsHAh-Fm425Lk2Hi39ti6Dp5-oSxcrldTVYqSX7Le8f8l_zEXER-SGc4r5wPffjv_3yk0NQ_AbtCi8bIR2kJ_qvPcjtk-dAy02Rbr4x5aWEUh2NV8gb46gkLI1vAHkfpA4QAtX4sh10AKygMJ6IPed-0RsyUvGuCF8Q9zpHiVKtK5GF7Jyhgc0EmAWJ95hZhELC7hU8GKbemdfXI-0DZiY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=GyVOGOPJmXl8ifeY2RZNfDgYFtJePPjIw3U_4fOosxJ1S9VGJEbstQ4uT1VgJE1M3KqrS_Z6YqEdnPbJvQHv9wsOR3pD0zpSLZvzC0dxtnF_ZHGnPMEP26j-yt9QH3CIuEB_L4yFVlBmACdv6aLif20OzbFdU0FyQmK7bPk2njAxpIR1uxwSDKMZr13dujp-kEkgf8BrmS7Hc7_8UEIvZBFJSmOqVXiSeXNF1yllpgrY-2K1lHEZgqCaehZAMwil4OX2xopaYAK57sR0k_A5H-mtGe9mi-O8oQNHzI3_PxPDI406MzFuYJklrOc90ZAh0VVRRna9LnKNxWM9mZJDQIhZ-Sgk5ySku6tfkGX43AFsYQPLNzJ0ZEMBgmMLA2JnDwnk1ZiZv5a8u2m4RR5KXUCwKJJNDRxlyI07sughWCdAmpiSSEYyCdVpDXeXf6gmKulDSSkHBUIdP4Rs_lfV5nsHAh-Fm425Lk2Hi39ti6Dp5-oSxcrldTVYqSX7Le8f8l_zEXER-SGc4r5wPffjv_3yk0NQ_AbtCi8bIR2kJ_qvPcjtk-dAy02Rbr4x5aWEUh2NV8gb46gkLI1vAHkfpA4QAtX4sh10AKygMJ6IPed-0RsyUvGuCF8Q9zpHiVKtK5GF7Jyhgc0EmAWJ95hZhELC7hU8GKbemdfXI-0DZiY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwvqb5FIVagaRc4yQMWTGbDsHoLWkoi_Y3Qbasoii2VZAngOufEUPS1w5V6D0-vRU72LniQmO0hJCVxDbBIqazXY8S1Usmut77aj_tKL3gpdlr4BgFcVBrs292fmAFZbUsQyYJ-AykiuCUFTcS99MBd3Ng92jzEOKD5I4hge2WANh2M44JkVHroRvJ0TUZez-v3V4bFsIN_2w35qVdj1NxaEgbOG6soVxFn7cyx_xA9G_OJTkkU7DZRDSYkstUdql7ATxf6zghQHwU37pcA52-LsGJoW8dDPC6ZF0eeAh2T5oHz0c4diupwWZPHKlcUNaC2fA0Ic0MIgBXS04sWodg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtF7R0_2IcA6pPccfaa5IkpPiKPSgyOdcqCpPWFLhzBu6sewoanax8EBVq239PrP_1nZm-W4ukaofP5pLnsK735lolrutl9Te32EMuzd2qsCVdGNTPc1skVYv8BZlbrjD5FNM5dlFiLOWZthXE9plzqewSvroRe2Y2tl3FWi6mSFeQjoykEWrKvd0BrCviu0lM8SSdX9cp5vb-FJLLhydOASmcTGqwBwep_rz3ogqCHB7XyPRdjbFcQuCzYM1RHHBKILIzsVkQUNpEjo_U4OjtBa6ekMkXrGILZrSVb6cYe6S3iMwnDq6MAGJhQJatbmLCk3899zRB6tXcrYbwkg4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTGwtOiFiKqmEISzJqIqX-wJJeqLMjkI_narQgHQaNYYgiKqgUmJfDfXHr2lZaMDXvnqInWjep476joomt2DT91bgA0OMKvETmWsnvlH3PsRUIhCWgRr1yf0_fjTOI9_Kdr16EwnIRSAITsRO5zjkcI9yD_HZB74_-1y8ET9RcQy8p_qmeksrkIvGe9ND5bxisoxTHL2L8davbbDodlbuSR_W8D8pSlzMjz-IsMAGYQLbSnKnGWI-hR2UZ2cWjZaCS-CKDG4JU7_XKMcCvBsxpa0_jGrf6Hf11YtuTxFD5weHxGO2wTOrxqKk6c4TKno72KpAZCivVUPF6jL3grgIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsagQgNQwEh-VF_YFkjbTD6Z5Eg7E_wptUj8Iy8yK74sgETVtT_rm00bU-ocrk-2QpyC7AJy94OjLQdkLIkBthFoeVk46zboKDsjye_-oQfUf3ZhQiGjZflQNNKIOjdr7vv6N-pEbalHyxhJJUk-_2gXx8AWE6QZRGAhe-WrINadPYFHQ5S-Jo1L3ZlU2wdKyHqhcM9JKs0d_4QWjl3JoGkJ6v8BWGLgtP1DK1WOAtF8ebexjQ2fiRQWKyiMz3mJ3uYc_3G3aP_rIcYKi80ZG_U9HE-ag85DUE-X4WDoMEDGjCA9VxVAOgFMVpg-a1B9yFWYNWvi320KX3eYkxglww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiAodBr4qqY09GfX7Y69ucGixow3H_dV9EHZnX82CtzyhouuMhTKO-At4cb7oTgPwJ74eLe-CXm1pm-7Kh7X2sI2rWQ0YAdyjub9CUqN9RfRTiVK6mHYadN3wixgOqsFZQcHlhJKVNIgPIIzUAQ3EoSkog001kyNwJGLBiWnzfNtZaahkutg95Bat2g6CB3NhtaWzNb8l_-tP02ZrIItX5_o_2bkyL5iDUW2smJV0aAsPFGnDAHSXHy9Eq1FSqHgxs4VJNn0RqGEqtAIIdM8LvQuKb-Z5Hz9zMsiexaH3l2CTvuXuvGl_F9xc1Ro1mtewnWaoC1OBuubJnv5MmLrXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eixcIAL3L0-PkFKdwGHCCCFbqiid8SlOBS5TndB_0z8vCsTlKxpZIFvTiqV16rCjolC2ftim62zKTMp3BGkQVqzh7FUbQgnp444IOKjeieMTcJy8Haox0l-YdNQYG7xcty7GWJBp8dTN7O5pof8h31yQskdRedqv6yXyog1E0eKgMhqSKo3CpaoA-jSDvUDvKFNJKVbuxhMymwcuaTh4jLY0uPS9a1vCUlUVquKGYkys2D5YdZqVeLu6K7Cx5QDnGymtgWaMdmegazI_-PbTbexx-DASKkh2AM26sdSJbJA3GD410v05gp0NC0KYH90pr_A06jOsRTs6gz7p-y9lCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzl9AgLEUkSCEFW4XlVxy6zuHgLlEhEH-Jir8ys_yxlIJjiPLAlJ_abSvE1XFYyS-J73xcJpxI8Tobffx9URDxwJL_ClNdQN-YF6e_X6H7ti1Stj_3aoqKqMISF-yJ441yUtaJD1pcB9nUwlgd3aD2tx07UeH5n1sK8fSuPtrqzOgQSMV9hS_Bn9rsNHMpegv4XVB58HwYljscZk0jWiNiuv9WgUU0Bpy_Z2rcxAw8rpxtdvltZ52old2qIjkEQctLeB9nFEFXDP_j5t8TgXMQ2gDr_pziXrpNt93n71pFkwWuzhjzgZzbzjZV_cFGctkFbRZhroAghlHNs8HhWr6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJzIYdnhxI9kPozBpX0HWqmyvUxvkptrGcFnNut3HePj83i50dPqDBKACYqIigh4ZZXa4fuL47dFvgwkPjwfKvEWbiI7BPphdF8byrTrweowQ-oOk9wxU9C2KNi9V6OrB8w1O_bnpadeuES-mbCs-idySysUP-zO9gEDGKuKVWwZka53n8RIfJ68iBVwgMQrW5l52DDOBkOtNhtCRld2_jy43_SvFOaIc_CJJEZRZExl8V0-oDATqqtqrJlvIIVYusrSV8prc9qegS9gadB31JQrLsg1zHdHk0MMblj-W4mq4fQ2dZWaHZucIhe7pk_NTegLu2TbQCvlsCu4BZNpVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBUvxgyJ3-9DrrhPw5Y9mNvkp8U1dADfJwUjsXbOhSgQdOduJ66ROyiJX4JThfeA4Lp0d-xhl-o3jIpt0hIbU5IyLYD_L4EbbrnzG1kEaj4bplpMtTs19PLCPRUD16xNZs8DY2AJClrH67CHOvYrQnBMynZeSj4IJFmSGnlZspdC5DgF8csQPXLTSEMPnLbz9g_OjcnvJDrL_eIInHBJuNNNl2i53Iz6L452_1R1MyH7IkFw5pIPj00RVVQDVNOgArpjjdamiUAPEkv9nHpQG54iXAKav7Qclmc-VfJucjJJ6m68HeizD4DqlF9GGl43-fKAUFpl0l0JxQFx997gsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaNCFtkrdfOuZasbk8-2mp4MXmnlMHzJTFVXDy6BDEWFsSeO693RlapTxIvX-T3I6OMuVRkpdua_tc2c5bql8FbvDIMm6lVM0kofx0ljQh4XwHqdXd9aulcKV4SMWgxvyKhsYCpS6OpSbSOh0gpNaM_Ld0XyEvs05jt0KjPlU_5MPQP8PLdCys5ywl80oQwtRMVL5h_rhhkIe0AsKZWIltkB77LcB1jHmIWf5XBjhmImWbSLMGrd5Q3PCpheTVGXX-LiPqlAADL8ixQCPINewsFJ4eoay5Km2aTUpLsxIeDApgJimiUD_EPQgMEZcQtBAfqRLnLERvffcfUCpqQiQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAab76d_94w0Las6xF-fL5m9zlms22jbkIYgxoiUWPheZwVgelM7nPkCyJVcazGH2QjMpYho3s5zVD80SKkCzQ_k866Ps49XHAaIJk7Crh_EI3m97mFyszTDb6Na3Yra7-6QtT-wo3vKN7B66ue8SuZF0o5aP7-dhDa5N5XW241W3oJ8WLQQre92AMRka0UoUz2dD_bN8IrBhZjhoCbKhzN_Yd4k6JPRYoEUAUqiXBU9kws0g1uXXQF8KpWkgH0wYHe-eIuSkO6RSxXZld3WgleRpRYREl_N-ca64rlGI_rp5IN0R02jjGE5CSB6ud39Y-UTjKB5d900WQ2NytKxNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFtHGRHCmSSOyIk2QkPOgkahpWCnBGpYtfyfwZJUTrDKZu457-S3gH0txSEAJmFFG4uNe1dP0S7ckc_H_UP0FjvcQhmts2YFbPpuUyBCPuaNrEDPh1xLCHgn9_is_ZMd4AgPJyeGMglJPy8Bs_w_oT7f-mdn8-z2wV7RUpriBzZ1EMq8EA4bV5ayat1czmDSRuXjuuGADd6zgdhXNqGFQLW6CwSDyDrjiBeECdn_g30CUEVeU_7isndtkKRdI9H10HaU9FXpky7si3YdMaBWK9TB110g7I2DuboIlcIl3zE5wAV2uGS1KSYFVc8lgXYe48HVeOsWn4g8X6ozrJiDwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxDxH_CWBVDxVtAuMYoNW2jx2WWVkP2m0Jv9JIhP6LjWNETjBCGmLA0aBG_9heJ3iZCRmsrHNyJ-LZcu4HXpU0vWd0PLp3kbxAJh_kukd3IYoX2e34JRRzLErLwVdnK1RHC5Nl4ZUle_-xSF7ObmmU9JApM4HNqgMPSQ1ZJIPfAA7IS8MLgYJktHXA3GBJtOIanpGnFhJ040rh7CxQx8uikO9mRsGatp7jqPHvvvO4H-e1h5WCzEFZXMIHMUipaQH5QVIIKVzeKYyrx64vj3D-CTlKFMIv35rh3absTfgs1GQRlM2SwF8CHVMW7_SlaGK6Fe_fTeWWrg1yDVNxrUsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPqtb2mxQPQx-q88K4XwetFgmx9uvc0UnjD3vIjRURxtVsFVcwkmo0ZupzKSBlG8qNOPGtg9G4pdkwmA6pbG0YL4LNUvzhkO5UyzGWPwae7I_N4xiJ5WL1KlOilVURdeTMYHiwbIoqOYtg6Ufg2D4BvKSZ93Uv8TkX1TkK6xpXc6Ii4DvSbN2kblWdXitaL1brnHBfwQXC4vptiqvsErpmkCCqSBdYY4kaIOB28cxa6GSLulU_2WX7CQgE5xdIq4FZpbHFueZv1Hsx9wqiZDujk1TSu4xmmIBfDJH_t6B-fmYRKiOtuGQIDcM6sOcjuZbiFQ8q9dIhGmwNJ1RfvaxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANOI-_NVwtZh-oxeh4uF0oeW4sccr7yyUwEBzlM1RgZLnY1aLt0MXsjzbE-VYj1zJmBXChBB9YcwoSLeVuC9ZTEWf48zSC1YM8y0N5R4o07GcDZAIYBCqpz5Vy2wsBHVA2aaK7Z6wSZSiMUaWKNu8vL2dkn9tw5PwUJ009NO2InpBlpnwa1jq2zNI5p93CBOfNBklFeRt3Y8JQw7tjDpHDsYQL9shTc_S2YPrEl0h8exE1zdhsG1UZrVu_Dq8WdiVanOZmrD3d0wppbUZ10eRjstAldE0IwCBX_vw2N0m4DODFHwu7zHWLketM5LnQm02pqpMs7fBqWNgNWIcFbR6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNOpMQ-NdS6RG-QgbIDfLKnkU72wJ9mLSBJjisnCGzrkdIH1SOzyD-VDwMTTpwRsxwsqJNUsVAI-g9NRS2MtVpttKl6CbILS6mrGOyP9LHgCtqwh-CvC7Yv--kLARnksNOCvFbPFgev-oclML3HuS7Zy2Hw962fROTZIMNl3mK2FxAwpdyG_7OKshlYlEdY7B2mNNWjY6pPhZKpfxSydb7p24XBk4JyoA9SsXaQB35QzURDlI97920ik1o2oY_HLJEZidmPVN1t7ROhidfFD1EYvgGDHW2Wf1GNVeZGk4L4xxCmxeNQOQUrc6eabNG-V9exjWWcxHwq_jd1dZE2jgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ALj4fwm_DZLLlKJgED4vNMkdLb_XpsSKNmlIY87Fp1tuFXKi90AOCzzOe4ijy2tcPSJdCF30enJhG0V-CMa7JwprUoOlGjctMEEr5ze5BhrUU0L2hig81cG5d3IOX-Ckth3PZLtYVC-5brvPWA5YilMjPp6CCK3gy0wZ9Fvm7M56DeQVBTgsmCps-ZJU1rD3nPHfWQ5CkbvSeGOLAuK4umhV___bCkbdBCtEOd6lAOue9jBxoqiKGJgsMhmLO4OXp0G53jiooZDX3gQ7Jb46HQTiDne5lg6R_vgtLfDkNyQw4Mf3wqG-uaQxq2aVyY-Rp3Lu4LhlKnvpuj8I5jYZJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FN8FX0g3rV0RAiEj0rBY9TwzuglsvWGTWYu0-y4A18fKf7OHo25Dds2ZoLUywVsHFQzG9rOI-aSdNpBKINgGhV-shKbmHio9UTdBXE20x2ehlAYx96tCfPFJ-zvM3og0cUN7VC9Km1IuL16dIMnmbeebk6f_uPHvA21ZianT5xh1kdA84YSPSoIsaU21NPcBdnVG10M2QXGl3uaKIXvA2KlkRQ_skeYu2LKYrrNnCxi-1Ggm8p07TwJ_BrQzFsjaDtsaYP1kr0X9QSJaQn-UP-LHueouBoybBvmxbuiDFd3rPIivtg_LCiGPYymuEcWFQ3PALiWv95mvk1LVZ_r1MA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLkPAHOmeOuLbNmgy5UUCfFjrNp7SgeFFMLo1P2jZ3owAydk3GI_7BD80vuh0j4iytG3mkudhT-UGt9p19vF7A_C6GGA5HFFQS5lZiSsBqWYc0fawnL2nA4lQV9n9t4GbY4hagG32lj81am7B4bBOewN9Rv45JY4H_fArHxuXGDChCKyEyn8QBmB11AesahAJ-ZOa2hpET96jEAgL3fzZ45_05C7vgiJqiyOqonuFUBu2Nd6MvUFO9r2JKDfnFA47SRsAnBafHTNv6yxOZzu4vWjWWeeTJnVWL-wPzRem3q2a8FDZ05Xg62OEE50YmElQxu1R8Yq8mHwUTf4BMqiMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGocMBeHkfgYS0WRGoazkUDRAJXK7jXK7j1_IvrHeEBsgG3FcZiyb391w5lGuBgPpv-akHGyJ7RTeRMbfHOFldt3-nJdW77ojwih__BgGEdmPhgQhDP1fsL_EIXy3fDe8XwMH8OTM0ArDwoLGpoiK3dmiW2Fph6MaLquX5owUnhV2u1S87dvl16pwD9xr5gP5xlmVJgPZ5A21OOv8HqWTRqXs8Mt_XngMUe1wuPFDgztaahGu9LtridAMRjyNK5bmqicrUuFQmirAD8PW11GiwAExIAuAq-7oTgIdF7CtMu5uVFbnM9dur0FIn_4SZkrLC38kuDy9m2f7uviJvojeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICMWS5cG_8VC6Sq3w22xzYBt2a2AcoYyUXIhbnDYxWLc91zMglnWWifp1QNTYiiiMV-U-OzAwBbbPRghMg1foeu0bvEUB7xI3PHnO18us-i_X3HsZnQZcxXjQz0LJOm0-XguVLUf9BySuiDirSGgBcGK8-F72OthAVRht3kC1bSCpwgcrx8yAGSvDcq5WAVgBQRVtxjOQ2mwbueuVi-hcumUhDpwshWWihIpp1TwO9hfCpknGUZs_mO7vUJ6NNbIfD0iobCHwh0zGEnPj4xYq-BFejfueEeiEla6gFSyCfThkPnjz26-7d1i7pLQFk7kG0afEVBxqLQkF8nsTerabw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQdz4wGf82Fmo_XKYrA_rgIftEC0ozwhTL5B4_1-_Q--ayzbDbDH60w1QpIsATdipcxpsYBZmx-fkKYvBATnArGbKRVbhJBTnj_NQmv1NSDOYd6-D1PF_6KSHVV7qiSIKdB9rYNvrRvAL5lNCd5wflZvg7Uy4fbzqB5Ir-BnFW3y2ajKqs5WYE3Iyr4Ex2zZgG48kEiTBwMrRLQAY2cOMZPfBEmL1QNMJdBSAQeRl9bEWjbK04yl1BNp_g9eB4Dt8Mm_CnH1cBGN6jnee7HnpadBN5J8w_xgTLkmzCQdAGAEL-e1Djr9ho0w0zM3m4lmIG5EVjqf4EclkLVmjY-dFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNS7LPX8D8eoAmo2Wr7tyddbAQ1vPIAouzKEHlchgpiHUlS-1NzCTt-2ydArn2074DQhG4uVtkAdyZECXbVE2oeSNO21mon3fZB9rD4giBL9pBzyrAWtTqrn3MsypLpMOXHJANy2Yjkes7y51iB3GAwe4c8c4V9wfBPdz0Dp9TlQ0to6zv-XVu1sup2uDAU0Qfma7ckEamctnpj0esP66eV_XZoOv9pfDAlPzZJb8mmxX6R39y0VfmMmMIdF2nEJtEgbYvnltzMY3NH79MMywxrXg1cL8963vo_lnggcLHmPg9R7-cNOZ5UYPmPHe_YXS-zFUiL4gI8gyZebjYtWkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2YF7TgsrIOKezA3kqU7K84o-k8l-bILViOY2HIDoMAE2OWE_ImKLn29v14nJo_rHkx2nMdYkplzG3HJmxeLMSLK5O9B2ZzoaaUanycIrbll6FnI2QefST3axVQEQBYjbf5xOSszNzy1kHT83xZ_r37qlsCYkW-SZAihw3CMjLRaeyeWCDE5X3u3hmcFUZTmw-82beT0YfmfHOgTpoNxVISNv6hE8lHI6c8dJSefTZ62kKVewLHl6D_AzvmIsnfz9zgRsOBLwgebq3oDP88zysX5bp71Fq5eJ5JJjsbttcBS3IfNUFCWz_K40uYwcJVj7S2rCMK5UZ21zptqmH15cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSHzaL4uaun5WhOp4gK5EfCjSNSz1P_Eel_kLWGSk0XrZtJcQtSNMIuiDf-u43z7Mu5IlHRJhc67-shnTFzAZzdCHXsb42KSbW_iCsdFf6QnEizRH-cBRrGazQGCpBmgJgt49zViBFRxvjip2_9_PTtKsIv5VqPR1sqx0w1pSnr2HGj3GvMX8gkNaRY90r2eFh06GmfB3lH7R7c7CHKNXuAWR3FI16cwT9gFr8SUVESKLYBiNkLq2zr3HVowbeuwbKJ46oF9ePmlm0g2GNUZQl1-nRUqfBZ-y0QXveinb-ygKZBVvLl8Jnei2ZIhZCPwsy9PNHNjMwTp9EVvFc250w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPHTRyb3m65VjLiTxyCBkRoZrArTfF615RAUSQdDmzu4LogpAJXTNZg-JHmj9FUVGWcsCka-a1oVmfLiTThs6OwdyrBBJVQDuCdkCCCXkl_wkZ5ME1kV6d-fo-ujE2RoiVeyDU2LQFQL5-lKJ8XfYm0MEDng8TrRRLKoyzLiBbafUZm_y1qSu0wy9u1OEGIXwxGWYxIUxrOIdkSKyovUflLjVE2kBfU1smrhNeTl9lJ1UhKh8M3VeNe_CfP3jYrO_TlGQdIgwAD6ywzgle908qLzMLnVeT_eKVzZO3ceNNaCERvAKmjOBgreHopPbw4Z1A5m2LQjcFgilLbdhsNMFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcJxrBBc5lmiZNCKbtlIrLL7q52NVC2kcnwH0KdCnRPhRiDHqXtKMuIyGKgLmuQFHxZwdh223XuQgkYtsURdexet_mp5YjJfxHMhPEkW5xsbCKs-V_gtXDZER3Xk-Dli1PuGE3eNzVF2MUZvkXKypz9vEuTSxRkcWlJPomVikNWpS7L8qAc34SCp4JypJQjSgxWSkc_D7hgaDVpHKm2dgdYNXrRC94NZMOubDFYdRraeDe4wfgo40ArgbEKtNgEsPT6L8bH0_P6wom2bj55yb6LGbY5I_Y1HU7dh10XDPuM0jlSI5BPRCQwCpVs95DyJc8aIP-fkXQNbgxVNHkY2xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMU_HYSdNcuMKnCz1Nl5-x1MXtd-83gs21EIUA_TB4ovVmhXeROFUAphrfclGMWr82WkR2TQrhDcIZTqObukn-fzkaMS4KnwDcej2xjK-XJSFX0B_Taqeb5Zwh5FDCf5OCf2qN20DHrCetB0h5fKLojCgLJ3y9Y7wf4WtKrbjkTEujFGkcxjdiCc9CS86nvwh7jef8KIA9QACsR9sx64X6AB8jhoQ-BgyFGzGMwXWWzHdsQS1w87oD3aTVnZFNXh61iG7_mjy7nZ4Z4LLMrEIeQD68cL_fi980ckrFKXqjzp01jJXU8X18uLtOMWnYcEVk_TF-UTXHEbypVxs2m_BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2Uy1LaRfROqFWdJTJoi7IFKaLb_yAZkiZhiQ_rhvA7vfWyKfzskzpGDJLSeh_aWxSNf0xVsYCnPNvdBKKe2D0c_3WMwpukTfW6v3u9XxrgW9SYMDsBd6RvvtUTB_WXRdNaXAFKvo0ifOlGjRGdFbueU6ZHDjjiRKVIRlUzwXWUxgcEX3gksy4n3W1uk0hUt-Ia5TYlVgxPd4CBSyNp81EfyZfWrJrtW6fxP3UpCD7OySztUIKT659zyAZN2ExeVcUUusbeK9OJj107er4os3HwqkNo9a0Eg55jPWssGcBfJmoxxbspQX86xnzbSZln03oD718-xEF4V9SkP4gzgKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPgDbXSuTNa9xOVhBo78pOqv31Wa-NI3LlEb3V4cc5ZwRM0iz7PRBwCL6-wRPyMvAoYCWsFQQe9_7V-ClwMcFd8MNGJOYYyiUQ7Se1Fmo1fPHS9yoVwZZ371qDzARsmtCS1-xaJvrbQEYDGfWjQqDUEz4bkTbCMVZcczKcpm6J79Os967hAfq6QtEuKLcPC_fGIsjE4mTqCR0PKOaIFpXLAS36Gy7BlH1htxfMnVjVkxpvmVilTlSa5J5mMOstZAIOps9FvPz4ni22aiOUsF1ExZoN52UZY76xM2HQSFG2QNH2_ZKUlA-jHTOq9q1ix79FuTP85SanQzYTw_pS84HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEPE7LP8dhUVq2efr1eksAJMuJbfBsxs_Kqz68ERotdQoJlSSkcNZ6kNOvz3fZUAudhskhCznMbMV1U7kpYk7pxjtDcgxJPlLngPqKmT37oPdzOAbqfrWuJ6kIaxkq6bTXD0iymJ-QJDyS8_1rrjG1n2E9rmGh9KPVU9h_OcztU79NxvGegOAS5P8CPJ8ByOLx3k8AgP-hLs1OKkISCVItUrS5xDSv77-w219oLdx1JmF8HKWAPqt-o6u__3eyuA9OWHKR8CRqWp2FzVF-sPaUT4EJ-Rw8Qos-TLIZjjjNVjFErQxdGgZzLezjaGCpCjlctYdJmLKRizQq47I3PrIg.jpg" alt="photo" loading="lazy"/></div>
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
