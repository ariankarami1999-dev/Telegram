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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 16:29:26</div>
<hr>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qLKf4u-ybnrlTBuSlyp8n0zBvrUQ7Esr9i28xdAllGpAuu2mg3cB0_xzI51F3goxI1kgJ2thsfSa6ALG2sBOCYA0K-IdtJMLrkJWoXcRN9KqQhozkIJocPrFKSCHys25TyN5x7HcViQjAb9K-RvDegdsyr_z4YDBW8mhf81k4j9YTUVVQSoZuij001JbniJyPjpJnFajyqksJZjopGbxpjOr_24S7gX0LGK3huLBVT0wjmFCJw9k8x3caeG6TbfSU0UQ4-7HkdP5FKTvS6_uFFzCAoGe_I-WgdN3Y2GoVjPymuQ4io5MNJrJaDtxyxmrurFHVrsu3bPxpCLc8b0UEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYnNukPmxeRiLcb0uSpzyZoHGqlsPKdRiaC4TW-wptsxY48TIcneX8zG7hj5jxnCYmViipR1i0WaYBddfuSM4IdSfoONE6HpgXCwOZLSkmzQv7sBLkmkyd-gucAIiPqZOF7e6KUNNE4e9JXTEE1UyvZAlpn4x2sLwpxmPkUHfHs9jpYcMmZA1AP7zAB97ljLLSNohPr7QxHwzJvdm57Beg5MtI8FgNDbHHOQVLXkCrBTEUKExQI-RRXZgZamCnzy2lJpWEdOCorunqdXdOrF3b1Xff8ANalc1gLIBApb-AdKuLW_S9SjKv9P6cJ0HDA-ZAcih6m0fMoNf6IsiQEpNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9Z8z0K5QN3YjOaLAH-wOmFnnV2RHoxH1kKFUKd21bk-ktwswrhkTbkhPaJoYbpabn2o6jtpH5iEWhiowsTzHzNyooDpoi7g7B53WyvfxXhc5OlvanTVLekSYlUPoTsJcxogMsfOB2a0AO3gFe3XaUP9-rlkphez3igr2RibWU5hHiPBq7aOJxs8sfoDD1e0ho6GB8pkKeVoB4CXvO336FWX-MycIT5gnP3bGO_QfkfuBbPe3dnJNd3l-6GnMGEYksYQXqe_U7HneSY8opPfYveXYv80vX8quL9YyNC1clpVhtDZV7dxyFnSjIgmEfq2Ww2dHM9pC80iPtlxwUJIEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcApaWyesX074CoP3lDbQVfJbSr0AUGukH_KCF1PegWPqAskkKHClkVigxWvbw8DXlZt_XjcjqGey2OZ8Ksr6cPXAD0WbS5atJrVE2mq33FvK6QEMSlk4Ggciw_qdHRL23hO3zRJLt4Gs3V-iE2kCtWBP0Qr5JtHf3evPDbsu-rv-561BViB3tbpUkdHoPpp2sqliuBeIq-fCgkOMM4NxQ9bCWzk3w1xoZjPq1Dus7C7AD-zpfd1ipyTjGpOZ-qph4Zdf4e2MMJUpAcB6nEI4i-OLsbE9S325lGNNo1LAPUFrhYlGN0HNPr0n-GXKjClVKp1ijin5KmZCBI8Ko0GEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qz71eOvpwmWscgntpRQ4INwXrXc57EFgb_SDMIcd4MRC49wQ_C4beG8wCsCBnvpKukaDqv-bmFfPkEg5UWWlDl2kjNLK_J6qjvRUo8qqYHfKxh4XF43JL2hI0KFnk-RB8OWhpqFcK1mspXkiVeeE7j15HJQXW8CBSv5bUkakADafMzbMQIu2hQYhxBFFF2vaBit9wa_d3qYSYbxyuCf0lj8OrTOdu-NT2vlnp9nBvXoBzfqaV92JhFqmdizItXaJ44sYMV6pHK1SohHXMlKpbCRVNqsKKbV5BvWFW8ZyHV8yU4uei_BXxyYQtMKt6Y7hVSRB6ZCkN3N_4sjE0yXhjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=dANZo35FaRrJ1oY0yFi1MUAw79B9wq1TBw0yVk87Kq2oCXJyaTU1iLTo2usqzgLhM_ylvqUFgl04GRfgWItg2IOOquAQCbUXsbolBGRy2lCMEvdMOwCNlk7ajOzY0KVq0M7eZtqnmNDekoXYg-H62yVpkFDXvdVAWwYxd6lN0Dwr7zzwDZrZpnLHJc5dxLpOb6n1i8IfPF2Op9irz0u5CF_uXXjaDlG0RsiUh_PjLzg3Ybi74fWdpBDdRDCZR9ZQ0d-fjUwCWdJnWGcDLZc1vJTglIcaLQmEvgGq0tdgHrAAy_0VeJOXIU2vuduLe_br0cwkEZNAhtIxzayLpvSlFIorcajlQieJOBFKun76bSvk3mi7xj2Kw3RW54Uj8wb3J7wbD7iqjksvWpAgqdCPVAtGnaBbxE2h1sexeXVuHLfDfMAPjpkPoJbEzSlys6IE1gVmFWkG50y8WWaqwQukRf2I3-ibmzR4Kc0aB-MoO031t1GA6FY7_MDZ0trn-NiahdkS2EZwjPLkeVkRhI9sU0FohNl2q-SPwa9fYKdKTroubJTpcpO-_TOdkiYhyES0sPZ9-BkAeU-rAdffPYVhn99a1e_-nS8E6AjVV8ZJtNcGG631L5_wldG8dQHPKc3dSOkeb_482o8D10-GFwFy2PxJWR1lioYCKAQT7HXtRpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=dANZo35FaRrJ1oY0yFi1MUAw79B9wq1TBw0yVk87Kq2oCXJyaTU1iLTo2usqzgLhM_ylvqUFgl04GRfgWItg2IOOquAQCbUXsbolBGRy2lCMEvdMOwCNlk7ajOzY0KVq0M7eZtqnmNDekoXYg-H62yVpkFDXvdVAWwYxd6lN0Dwr7zzwDZrZpnLHJc5dxLpOb6n1i8IfPF2Op9irz0u5CF_uXXjaDlG0RsiUh_PjLzg3Ybi74fWdpBDdRDCZR9ZQ0d-fjUwCWdJnWGcDLZc1vJTglIcaLQmEvgGq0tdgHrAAy_0VeJOXIU2vuduLe_br0cwkEZNAhtIxzayLpvSlFIorcajlQieJOBFKun76bSvk3mi7xj2Kw3RW54Uj8wb3J7wbD7iqjksvWpAgqdCPVAtGnaBbxE2h1sexeXVuHLfDfMAPjpkPoJbEzSlys6IE1gVmFWkG50y8WWaqwQukRf2I3-ibmzR4Kc0aB-MoO031t1GA6FY7_MDZ0trn-NiahdkS2EZwjPLkeVkRhI9sU0FohNl2q-SPwa9fYKdKTroubJTpcpO-_TOdkiYhyES0sPZ9-BkAeU-rAdffPYVhn99a1e_-nS8E6AjVV8ZJtNcGG631L5_wldG8dQHPKc3dSOkeb_482o8D10-GFwFy2PxJWR1lioYCKAQT7HXtRpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=vAo_ECIZv96WRFDtIvDJjwTAVTDDwkQ_10Ky5s6msziy7lwtzOAYlHjtnmpPPxb86Oe_xBs8q9Ynx-c4QkvIKWeLfOQZe4AMDFhnvkpPE9RkIBsShHftB55mnW01Na44-HyhxUFY2vwFckAAaA9d230pA-8orB6N9N41QdYKenpaOWDBA9jcJXh92JfTkOHPcm7aV8gtN4BOhlPNrwzdxGQjYFb88gUxbHeLj6i_SLMR7R4psYFqV5d3eaA_5ppaImqe-xt9wzLgqUhbZXy-D30M2es6hh-kjhpvwbgS8AvSRXZjjxPPbUNADCEW9R8dJYJ0ONBJZy12xrubGtPlBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=vAo_ECIZv96WRFDtIvDJjwTAVTDDwkQ_10Ky5s6msziy7lwtzOAYlHjtnmpPPxb86Oe_xBs8q9Ynx-c4QkvIKWeLfOQZe4AMDFhnvkpPE9RkIBsShHftB55mnW01Na44-HyhxUFY2vwFckAAaA9d230pA-8orB6N9N41QdYKenpaOWDBA9jcJXh92JfTkOHPcm7aV8gtN4BOhlPNrwzdxGQjYFb88gUxbHeLj6i_SLMR7R4psYFqV5d3eaA_5ppaImqe-xt9wzLgqUhbZXy-D30M2es6hh-kjhpvwbgS8AvSRXZjjxPPbUNADCEW9R8dJYJ0ONBJZy12xrubGtPlBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FX7fpzUZHaRLWeC_H0RQteuy-Gtf1VkHRc3lOXbb9qTS57F8cBcd3rWCk6EX2-VGTehCDgjdQsD2qENqFwNJTxD_DK22XqtfNzet3-Wndf6AYvGy2W2TM5qFXB85BEY0wLtaJJgWDKwJA--OjXDyM-KQgq0Q-Ov1JZ6Sj42-nAFMHzZZtMqw7Tr5b8onBp4GyPZPOmsBxAUSmBtrNk7PQuu5L96i4YrTYkIRJen96mBpJZZFmIoY-R7ORxZFSlSZzqLAqVq8Ctjj1uAtwQBELKigv3w7iyNebnzHzIlX8vTzOXyy2ELfpSL-TIl-zXJZlwVntu2jq2Kvmg4mpbtmSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=FJ7ujRFWz0Qy6yEUH49WcFZAesl7jAu2IucBqP4P2lFFz3WiZlswetjJzHFV_QQTvg4iOSFJEyLKXDKecuL0Ra10beOIt1NorZ5fc9nlmDc2IgF_sU3zbzY8T32Ev6-z737HFGi48bdCPTHRnbi7Gr6nefWp2Yo00Nl1T7S7KLs3HYpTyXq3A4CojSCpuDUI0OJGn5rIPkRWu1pQB4UOWDW2iCGzY0bj2rVamTB_DTCclps9f-_hnAd6PkuhSHUEknYCgwYDaoyJftLf46EfWkhxo3lx_4cRCcU3dIKU1pJ5tYbZZpsj4SnkSQwMzzQYlIFrjGaGV_PquJkaapD5Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=FJ7ujRFWz0Qy6yEUH49WcFZAesl7jAu2IucBqP4P2lFFz3WiZlswetjJzHFV_QQTvg4iOSFJEyLKXDKecuL0Ra10beOIt1NorZ5fc9nlmDc2IgF_sU3zbzY8T32Ev6-z737HFGi48bdCPTHRnbi7Gr6nefWp2Yo00Nl1T7S7KLs3HYpTyXq3A4CojSCpuDUI0OJGn5rIPkRWu1pQB4UOWDW2iCGzY0bj2rVamTB_DTCclps9f-_hnAd6PkuhSHUEknYCgwYDaoyJftLf46EfWkhxo3lx_4cRCcU3dIKU1pJ5tYbZZpsj4SnkSQwMzzQYlIFrjGaGV_PquJkaapD5Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=j47IPDJQtkDlCjzPAfNGWkPkhluOnE0I29OEFbh-iNnKXfjaByYCYpP9uqe8CN_MiO8FQbG-r_C2rmRsJQYCKpFTANmfNs_QQ_3rABof-WmeagHPBSy1IHwAdRWPPqJJ-xDUdYF1clVRgTxtHNpnpWBQZBX7ZwY8q2YKUYp6nLfRE4vHB0KggK6-LZl0bm8UGxBZpUKwvfHdmj-6vtjhS0T8g9KFSJmJ9X1GHOTcAtCBtEPH5lJyUpFNBYZJEfJRD2M9Yol2McBXS6GR698AAJIp2ESwwkOpSH-jiZGTl4487MiBMIoHKLvn2Yqnc8QbQRjfJ3zQNjhzrxqaHJsH8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=j47IPDJQtkDlCjzPAfNGWkPkhluOnE0I29OEFbh-iNnKXfjaByYCYpP9uqe8CN_MiO8FQbG-r_C2rmRsJQYCKpFTANmfNs_QQ_3rABof-WmeagHPBSy1IHwAdRWPPqJJ-xDUdYF1clVRgTxtHNpnpWBQZBX7ZwY8q2YKUYp6nLfRE4vHB0KggK6-LZl0bm8UGxBZpUKwvfHdmj-6vtjhS0T8g9KFSJmJ9X1GHOTcAtCBtEPH5lJyUpFNBYZJEfJRD2M9Yol2McBXS6GR698AAJIp2ESwwkOpSH-jiZGTl4487MiBMIoHKLvn2Yqnc8QbQRjfJ3zQNjhzrxqaHJsH8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ci-dCVGAoxFf4jAl0nlWndEaTuXnezT5wSSMQIfydsqkonWd7CuA6eoqXNsfUfyhtBkPwF_R57JDIhm-wE7WaTqEsYxlDBJuF_p2iSEoui43BS9kGEAYE9iqWfddzSVhdgbxxNNUEV9aiFCkGHJ5hDwoi7tZ1ptP-MT9YLfNng-oecPsaeH87-aSRxU5WZqgtouP8Dhc-j6jXIr0UcZXlWl2BK3BmpwFEW_1CAfFVlCMqUm2o7r5OaRzrFR_EzUOl9Ce5aCDXQLl3lyBu5QawmfH5_2RNGysYuC_kphnAK0xEAtnc_BJxYNjotqxcLOfmjz-9O8gop_j6OsGkUzaHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGrRHnmLcCq7hgvA0Ny28EK1cLXAziahIj8y44jFRDjGuLgvbebm9_OPHvp8wT2mT-yDidWo5ZOwSw2nxS3CI69ZMVTlhaY9hjOabxMTRfDMi2CnaC3DJHKoBmvFtLFKnlGwGu5WCoWJgBZIxK5niikXUvlPmqThnV1WIjSEFXlRTvW_6Ko0Xb8f0AK9DGW5ZPpLuJvSMrLS9dye2pfJcrojAAjxNIYQ3kQbHkEk-FMbyM5E7rMZx4hF7CafGU45G0qIUwLOli0BU8U8kCAGby0aqaGqU2MY2H_C5jg75l8jbC033wSd0rsGPPgU325K_BW9pyyUV1foDGPyOQI9bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHvkn4N2VvbWUEmIyve798i9gvLaV7uSzfK46n5bneCyXew5l7BOPj8fFNbYOFTZYdCCxVCXEp8a-ji1kqpv84EUVhP4LlRRwhpkuela4yqYLVatZdqhVnAImhsTvreOcMnAnxVzkoJYRDhQmHP_PMG4j3_nkoU2-LN1doNK7f3wdG69MBFIHgmNgzpkX8Aa43mLYcuQ_Zck511gbY33jqdxlQidtV6JjCBcWVsTr4fXPLHZh-DamZbdkQPnTbIJ_lXCo67u1NGHjPox52D5vg6cqydg-tVQSHdaTXS9Ea2sBxox52l_kqAB_1CvPPOTbux9lPDcAIL7S58otqliaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_g5uF7L7y08Jki8jIMxNBCFPvlipZE84lH4p2pf90oPmIWEj0FF6idQq9i89lBI_onuIKSPwQIUrEFh1_2LrIwwDcv_g9_PkYHtavPM2HgmLnW7QOvpVlfQo7DUGsvpr2NxUtBA00C_ne9b98nj0SkdDHNMfmBJzjck5JHsu2kiep5TL9E9OblQT4FdEQDHdzbKei8EbTo7CLri0S-P1F09-Gu6835tGYRttm4oy8Jcrnhz1_ddSW7hvbrNrEMRlDfeNsWUKm-I4S1exKSbbJhiTYKguaNW8mRZ3j6WQRsSsO_NMBRdpstB7Myxq7pjejiuDiMdwAhlIiVN2Sd43A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDstHbjMzgJUjSjSJnhiP8vzdWQAJYoIf8JuP-rwGACrL9IUcHIVlmWIqRDcP2hNoTeJyzPDUS74-J2ED2ma8i1pQsZ-1GNpF12aFCC_ZQeKYNSl2zJLieddbi2HWfs_NCEnzOaEsweh2l-ayHXDr9CZuFu80kX_AuYh6zHXe499LMyVH3862k5ezsujLjnXppN4sUlEeMyE7JXSeynuf-4rZgDIZCrnyuRokYqZTzuM17I-o8zbbe7nG2UYABqbmT-L9Z-jxwkUEvfBMSt0JRBaqOz2B6p2dEg2fB1pTk6O2LZkfonSVYMfPABuq4bKlu3Zg6KivcLQkggR8nX2EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoGY-Q1cn46A8z7-hgyOmGAW4xIinVIwbwMizdDqfBhJiHo7PHVUZReDyaQOvhsDQHAjXjCJqqc-xpT4ahFj-Hs01rjh-C0OA6ejto8jlsU77DCS3I3Sro5-A88uO6wV3mO-JDaYK0CxoVRMUpH2RtbdLjxo8jxR3BgecWuzyHZmTms9_iWpEXWYB_siBYJ058n0r2-3Hpdm0AR_byCzuzPgf1vZ4eE4aQLIFZMW20LMXcc47ZEZvak57kChADTJb2i-xazK2roefHVduRly5rSm6bFnp9aVLG4QrbJl2L_o9Dbcz7rYTcBHWYdD6DGS55CkaN92oaVKpzd3RO01iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s87Q5ZrkVUE_KeSsm7IIG-__5yQbbfIaNJnuhRuiZI2yxvuILcb7924RD2fw8Z4hP4h6O_CGuoSmCc5OaNEFgYZfecRj0zGbFhKTY1WbD-t9XDu5zn7rz5gLmwJSXK7kRscrwJRQkrrw_SZYORBdS9nfrnaakYdM7qb_TTF85qO0TE-jDE_5RScBQA5DW7-ppxznAAGWdTEzJOWK0EzKIe16jOzn8LixylHCW-nxZ9xNtbqXXqIvJYegBeVcNrwAkFbKYme1klCTKnX2Z2g7AkB28t6kZCrzyhDolEike0RQ6IGTj_OZrt8kcmLpvcyaB6qtRIAZjiwTCv-O9QVNug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IOoC5gXxLQQ3BGiupyTRJe-12TNvolt52fH2gLqDIQO34zTS-kzHvr5FUNzX8a1-iBpmALS79uJHY7rSz77Wpa8T5VMWbsCtFzmMhFSsIWEaNA49dz0PRR952nKhw3XRwArmiso7h8f8W5l-N02aR9DxxOhBKdoXSy_PvieEU5bL2u9g3vCyXQF1QmEK23YoLjXZhOt-6s029SIRLUhvEckEZ1I4Jretl2oaxUMPwcdmR_qg_gvAxOoYzCeNmoxjP23G98zS3AHFBZwoorcybjwQcUdyiG2ceqogMpquAUQKFTCdOlU3fmie5vzfUD9EaSSd0PlCkmo0t28h2EZGqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XIPOaa-HYo0TK08IHfFo9WErMeZDaO2rpUcGFV39zdnucZP-9C2ZgQumIRf50DsvLwy1IxcaAiIg8V4NHsXBmZoeQzwF243HS9QIRuN5JgstOZbhLlp-hBuFburE80z9tjFnO72vQCNLkf2KaAG24pDvxbEcbx8jTzuZFWwbrJCn0kL7hlKQOvLH6iaqu8FaD1sfAW-PNM-U1L6dqweayGA3uDwYYGGWTt8Jve4GvoElHCEDSa3s3F7TfvIkXK91ZgXXDG9SU0ZD-2lbdHTN8RCCwjWH6uY62kUWMlciKReGw0efD4_iGdzpJbsQDHFikgFFf6AGir6O6Wr2UCoKHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aWoRt70awq7J3c_at3km7Q3TK3xfIz5xPFd5nBM70SxeoajeFmQDpnbOcfmSFj_B4xNX6H5Q5A5IGHWBN2gbv5_psAUx08LDBNtvNe0QYRfjObiX-cnJ3N5wchd4DZIIlJI_14QpsD61AmkHXS__VYylMeUlCjK27jXdiUwfNp9IW19i8OK-uVZHTh8vcuijv2mKUE2LxaADUgtA7WB7qkA5HJUXyvifsSG8EciVgx-mhTGsojifkEc1GhGtJ2KsiFtf0pjA7kG-73q_w-2ZWA26Myvse4rxMBcQaaefyAfP0zXhTeagQDmesdSTmpfR3gHvvlQK14QanU_0zA0Ysw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=JS-ec7MvRdYIVO36JOFrUOZ4lywclITI21kZ2u_XzMPOUeD6DTnm_GZIztNpCdStKGFrrMsweCkGmVfDtYVDHMIVLn1-zGsqQMuFDw_2UMDq_yno72C_bpMO2GW9t296z1gFDiOsM6NHCDQpgkN9wc1uGPTIZ2ze81UaqfcLForZcg-nCyNosJ90HiaYBWF0MgftZu5VRP-pjSmX5ZVXNVh0AlMSmouRfpv-jE6nxVAMI1Nhoazf60R1yPCaBwMh5R2iLxl4c_H7aP2PrWSUA6x7pn8GjkKTVtwLV-VgUNsm4HUi-Qap-yIgB5T10DJnwRUom4SwO9xke68EMqeyCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=JS-ec7MvRdYIVO36JOFrUOZ4lywclITI21kZ2u_XzMPOUeD6DTnm_GZIztNpCdStKGFrrMsweCkGmVfDtYVDHMIVLn1-zGsqQMuFDw_2UMDq_yno72C_bpMO2GW9t296z1gFDiOsM6NHCDQpgkN9wc1uGPTIZ2ze81UaqfcLForZcg-nCyNosJ90HiaYBWF0MgftZu5VRP-pjSmX5ZVXNVh0AlMSmouRfpv-jE6nxVAMI1Nhoazf60R1yPCaBwMh5R2iLxl4c_H7aP2PrWSUA6x7pn8GjkKTVtwLV-VgUNsm4HUi-Qap-yIgB5T10DJnwRUom4SwO9xke68EMqeyCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChpbnSEp0BObcLd2ImoO_tQfVgnz_-I7FrSjEIgK7-G9QcHFOwQ4HI0q0oahQo5_49IlmMzu4UFPb7_610YDR8D8m8-PJFOO89WBETYP5Vrh0Qz_1FwZPopmRs9VxRDsV4atkhlxDwP3phWpgmtDBXtnWQ_kCBgGsYrrrFjNnZmLtB553a_40X92coDnSYsGoHKfJDSNf_C6KBRliAXv3w4u8YMNUD6mJWvSjxeHgbYgBvylysLsYrsxp6ClkXRzCcOk42uzgqKtCf3cGTGdS8Yy5ER9nCOqviqrehQxBGn6nVIjaPOg6bU0rjzzJDdSC5X-_1hgesJ05hxRVU5nFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8NunxhJz2xsCWKI_M5DZM3WAaXZFoN3i9LPltOqwRf6KD7wqjYM-e8CWtJ4bzNp6N7173cyu5Qe0NnnBvSa41qf9Nmsq8gNISRCf5ie27QqO8x4v6VY94SkqH3lLLSvN8WfjcdiNYhlkAuBwGOKhUWLPeJOvywtYIZlvu1BpfzyfwrfX2y86tQXWKBs2SCdJKQBENqAYA1haRSXpRAGhfvF4ZohLKXHLW68c0HtaIBBMXnqyDFhTzS23VK7jyNSzO_QTSU4LS_6jxXmjLn8TPdn8cvQFYNMH8IH5OJDqbRzzeCeSKMxUXDUgE7Yj6E7YTiMTzYTokXBo3zFUH_u1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=gEaIdHklh2jOdNNSJOow-zkS6apRBglg16NTvYinltPtN6wZZbBMYXD5a_jovvCDh9SNk7udnr9MvsudumTOkjAZMrikxS-dYocuYOH-AOyUQFRovKhAzMGVOikBsWNy9hmVxKrIj5zO9Y4qO2EM8edBt71D3YvDUpI_Ia1l6IxJ8DB3_2al_CTfIKxoZ707EzboS4jYU9zK9zrKvD3LxOkmo1iOJwalA3Isi59HrttvrMHprw94x1cUe1M0hWWSxHQybLJ1cQgRsUK4Tmk5ulX3eLTUxYnFRTZRyhTY2I39x5IbLMczgqj72r-KgJyvko6tYdbW7m36ir-RdaAhtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=gEaIdHklh2jOdNNSJOow-zkS6apRBglg16NTvYinltPtN6wZZbBMYXD5a_jovvCDh9SNk7udnr9MvsudumTOkjAZMrikxS-dYocuYOH-AOyUQFRovKhAzMGVOikBsWNy9hmVxKrIj5zO9Y4qO2EM8edBt71D3YvDUpI_Ia1l6IxJ8DB3_2al_CTfIKxoZ707EzboS4jYU9zK9zrKvD3LxOkmo1iOJwalA3Isi59HrttvrMHprw94x1cUe1M0hWWSxHQybLJ1cQgRsUK4Tmk5ulX3eLTUxYnFRTZRyhTY2I39x5IbLMczgqj72r-KgJyvko6tYdbW7m36ir-RdaAhtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=FgTnu9ZfmG3S1aZ3lf693EiUyMgysBGRkcjrlXSYKbxHV6HOtg5Q6jk-JbkDFhNtBQ0K0D4MetQ71B8m_Welylx6jtKprQ86xgNEbNOSwXMU42SX7vQrbk7fHCKZT645Qt2hJgI3yZF9MQblJM3_dfumArjydcuZ4gY5Dp1elYfK59LgAVxAihlGKZKWlugzCWpeWSajvii18-898TyCb2PKUgBxHYxnqgX62xCEvhH07OYdIRPUITiQU_avC0vnRYTTQ-Z9-b-TIdSsT_ZBCTvYaoGn1HFv1ssg8JKnp49UOGzdUXxcxUCA71ENyctsazVP_YARBUUgX4x8i01_Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=FgTnu9ZfmG3S1aZ3lf693EiUyMgysBGRkcjrlXSYKbxHV6HOtg5Q6jk-JbkDFhNtBQ0K0D4MetQ71B8m_Welylx6jtKprQ86xgNEbNOSwXMU42SX7vQrbk7fHCKZT645Qt2hJgI3yZF9MQblJM3_dfumArjydcuZ4gY5Dp1elYfK59LgAVxAihlGKZKWlugzCWpeWSajvii18-898TyCb2PKUgBxHYxnqgX62xCEvhH07OYdIRPUITiQU_avC0vnRYTTQ-Z9-b-TIdSsT_ZBCTvYaoGn1HFv1ssg8JKnp49UOGzdUXxcxUCA71ENyctsazVP_YARBUUgX4x8i01_Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpoIGsRR1Vg6qjam0qfErHdsccyTZJDhZrbdgwRhh-RK2Ie3t_XpS0pNjrnZpmrxR6TY16KXHBrJxfsaUR6ORaXfYWYuNfaXwV5FUMS0ORnLAtiac1lq6mf8XODeoq0iGkELxDQZ_fUg2-C-bVs5OWrYepm0AO5rNg1e3FUNpUa7sTzGs6m4lrV14LSmSi8LlceWK5cxBo3CUwuwwQ_fsM7ChOoxjSdJgX4U46G7XO-hJut0SS6j1esqPIwKu4vR0PYqeXxlSX3V21JcmYs6vub7Pl-spkxYpIdfBd6RZi8J6MI_Gx311ZvJYWbjiONE9rvelEubumYuDSbn4jwEwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWkX5JX9Y2rx9SH7nodtNEq8FT9IBAg3PinBGYBCG-UPnDIXFat5LRhgjyGmnIBQTDiTIkRM-z8jB41-DhFXka2YS6Me_6AZUuuPqLY3ldn-m8bPMvYKSX0ZZxgXH4_z6UKv3RB46nzM_T9omHOoCxz2F-lLmV038luR9ej6eZoFyS050WEXzh9XHOHOitkx8WOeaaDscqhWUAlqqD164JfzZwoRjN8w-AI-7ym_S23q4Ow98v3b1N5P9EPW9DtL_DYjrAKea4RIX_Qs6lJXydnR9gvcydRLUPv_hBU0kIonBX0bo_q92cjKs90h1ni9OZKYProIz5K4F_-PLbRvAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Njf6Dl25BVOKUhsrpDlVLF4aXShHm3nHL7LiaQ1wdHf1WzkL8ivU8dbQ26bYRshs6-pQKLrB6GdWigiFd5LvYH8xBFkP5gGHbOYXfnV-BG9rnPRrqyWPw5RKAcjMagmw-bBBBqvrH8JfjmND2iQr3rcol2yBWJYDkFoyCo1G3noHO6k073oPlyncXFN-KaT6st0dJBFjpeW56w8fY7wftW8_Q8OJdsdFcR7p-GyepyotxkfoApX_FJXauKIjPrXzYDPuzLI2K609cZZRDl1YUaurPaFzsh-K1t6jl2uMVE_kRGz5mIdIBS5x_4Py3-P1Rqiuu2DAtY2U6HQt4--c4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KF44d69T0cKM6Nl4NjpluhX9W_EAf0c7WYK1okYPNov_xaVJ9EdtFb0Vfq9xJgJv-E91DAGWviZjjikeUYOr0hSYHyYzIG2xqqQ4repuvTZlWGR5vdvPefPhQlG0-mhvQA0-keULelySBWoTwkqLlFyBbScHzjPVRFnw3J7wsN7iLL5v3pB-gQCIW-FTdSXULtSWRlI1EYawlk8UO_T0rZsAIOTQ_xrntS6mYJrq6DhLTsUWDqc9NLcbOEMq4QKpzQhB3hw2sWbsSUbYOKQCnds8diirI9TgWEtxO6AGyXdLc1tQX-wGu-R4YSmMUZPn3weaL_NnsCrO_JR1IyPeDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3SiXdL3Q5qWnc7lkzQ9pVXYB9orMWMmNOEHX2ZEX8DLpyZiBi0BPRMvKPljKNBvDw4Yv_8nyOc-Zb-skt52Zh1lRXv6fJ5oKbxywuZAYN-JHD7frxEyQymGa7E56OiHdoVLkEJunS2a-Nd9Dbu9uk5u7K1Rfc5_1WSscY8Gl_4OPo0Ey_E8xliev04CXt-A7vzclb_1IlC_0oOpBmJPFYsxhy_EUXSKnMfipQI5Uul92YfQH5HaNJ5BC9vAlvDEUtLpJLYmlMJg1mM3bsgB5HiPYWHJAPg_43FhldAi9wv65KBJQnlO2i3i56ouwezX2neikX0o88o3bnVmaZ1ZzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUOYC50EPzpGXQ7H8VvrutdSQZmS-w8Tc9pEqbO8nRdkLd30WCIOqLWsnbbtt5MF2a0ZMv8o2Y4GHZyjQudm_U8ag-05Bqkz2dwzqkhoxZU2pX2ZJaLZk-wWICo6Wx2ZSsy7UeidPl0sFbJzni5yCotkRjJ3BjSfXAP3bjbW6qMBVXlBKs0414dM4Ren0H2w2LOpVn10jHE1-_Fe_O5TCk9AxBHBUst3AMbLD21plV_7_p5kaKfNHh4q8vU0muL7GvFTt-s0vkuf2GSH_0edUqFlBlx1Argaw7sEUvbyfbJQw0CHW86ZSSY2yGH89hQODvcFIG2kpij1yDHnzy575Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFaMgL53e2I0FTpNWNRW8hQr9U4Eaif_lauOch5c9UXiN1yDgmjA8xT_l32-hikaHdypF23bcGk6Pknz4wKmof-seilAb94UF2a5_6E6uVWcCE0OOTIIz9Zup9UDky0MYskJTyAeD4NI-GlASE5I063z5KPYRi6WVo8c-vghmeYA3jGufgnsXt84oRzEM1jki23X1VCvNNxspeOGfqINut3UFH_lH8T-KxP1ArIlQWBME0XQTSKmFNmwU6SKCpI8682RBlhQO1mH3Z4SAy3ChjjaxvSf4uLhl_r7M8NG2mWFt9F5N4napmBEDY1Djm3i9oDIA4xbptBOnqhLrIX79Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=YahRvZCzu4KUntljzeinI1f7EAok5Ydw1WceUp5x6CpK45x55_x0qK2HTJHqfvFoZNxtjNeWlf5dTFwqPs-weVz-07Z7MrRay56Gz0R7jmxr6KAVrZc1fnU4fkS8N0oZsnzefwk50HI4-FFJcyrpd1hYv47Dxji6Hegfq8LVjOFO2cbBrMkCOzfJJ7tTK3u8HEkHMtyZMbBHe6etpHzW7rfV98YQWlxD_988THusbbYGugEfCH0tQgEKezAGie6SIrsw_5mBv_WeKqhOxZLmDMhVau3JJBl-91y9Eji51YutM0xKFrq9IbJBjp8Y4CgguLsEwAhE6RAfZfBZlF_Zsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=YahRvZCzu4KUntljzeinI1f7EAok5Ydw1WceUp5x6CpK45x55_x0qK2HTJHqfvFoZNxtjNeWlf5dTFwqPs-weVz-07Z7MrRay56Gz0R7jmxr6KAVrZc1fnU4fkS8N0oZsnzefwk50HI4-FFJcyrpd1hYv47Dxji6Hegfq8LVjOFO2cbBrMkCOzfJJ7tTK3u8HEkHMtyZMbBHe6etpHzW7rfV98YQWlxD_988THusbbYGugEfCH0tQgEKezAGie6SIrsw_5mBv_WeKqhOxZLmDMhVau3JJBl-91y9Eji51YutM0xKFrq9IbJBjp8Y4CgguLsEwAhE6RAfZfBZlF_Zsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzBrw4GVqyJ2HrnDlaJbw3BotWKqp_B5-VWHboM2R629HgC8hRWwU7n0gz5DZkT9I8NUWTpVMG7d69JNhSJ0bX74d4vG9gwE9IXVTbT9lItwCAbQQiSh66SjKJ2H4YnfvS1sQoTas9Eg5dPR8jpNiJHzEPb0JU7Exm5G9HT1YdfpftdoIMgCXKV5WWNmFkkSSRDBw1bTZQ4BctVgwsK2y-PP7l4tUO-73ZaMY6-1WXm8TBlUxFBNswewykyujFop7Tl_WQcYsxhjwW9lQX7zxXUcIZ0-owXwZ5qs1juJXThkoQkSPce6j3Q9LtwfZmaZ_M4iGX2mN21s8hVzc5Y1Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=ew-2TqZ7zKBJCU077Mrw2KBQ4ugewlp_eyCGMmz6ieqd_ilTba2MBAK81HB3Uwpm_4zX9gLtYdEErOfTSAN0GfNdTlzvY0LQCO_gRmwfrI0pmp-BM8iiH_J9b9nW_cNierJFYqbxC44Z6Cx94ACcjIrj-oPUBx930T8dW60iktcw6p34W_UhBY3Kr8v_h8eHv1cTT6xH-dD3QpQkHtbbrgEqUzv0hGN8ZSOH6DL6bpFPs8a-p6KvkhbLBbrvq9tDMjGe_JeNS_Lq9QbiU8HX7-e5qtnOhq5sk6ecd5-DzuR3MiElwrR2WRtxX7Pt7Ts1QZUyw_YrPcePRSAMr0h4ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=ew-2TqZ7zKBJCU077Mrw2KBQ4ugewlp_eyCGMmz6ieqd_ilTba2MBAK81HB3Uwpm_4zX9gLtYdEErOfTSAN0GfNdTlzvY0LQCO_gRmwfrI0pmp-BM8iiH_J9b9nW_cNierJFYqbxC44Z6Cx94ACcjIrj-oPUBx930T8dW60iktcw6p34W_UhBY3Kr8v_h8eHv1cTT6xH-dD3QpQkHtbbrgEqUzv0hGN8ZSOH6DL6bpFPs8a-p6KvkhbLBbrvq9tDMjGe_JeNS_Lq9QbiU8HX7-e5qtnOhq5sk6ecd5-DzuR3MiElwrR2WRtxX7Pt7Ts1QZUyw_YrPcePRSAMr0h4ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=nZMfh2qKxTpMsVRYJ1k_gr2Wq1WAA4zaSNAma2jK3CQHWHt8v6665eULZ6pvqQadTrEra8Em0o3yMbqm4Bb3RQGQKqXVA2Hr7VMLBuh9Ju0lhWbwx0lMQwO_Dy3uPA_KDYvcvyHNjcbX0QQCtq1YKPmxUZs15r60pq3zOoPVQVBJN5XaON0ascco9zKCk9qg8x1ppnvGzDu09b-TFu08yTgnkUjgGSeL6JV15BQtq-aKjk9zJ6c8O2RNPg_oJyvWr8f1kPeE7raenwKtRTUtEOXWOLl3FdcTur7irhuLsEFGFzonExmTJrkZOu2Pk7gVpYDj-pIb54BOkiZ13rQdcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=nZMfh2qKxTpMsVRYJ1k_gr2Wq1WAA4zaSNAma2jK3CQHWHt8v6665eULZ6pvqQadTrEra8Em0o3yMbqm4Bb3RQGQKqXVA2Hr7VMLBuh9Ju0lhWbwx0lMQwO_Dy3uPA_KDYvcvyHNjcbX0QQCtq1YKPmxUZs15r60pq3zOoPVQVBJN5XaON0ascco9zKCk9qg8x1ppnvGzDu09b-TFu08yTgnkUjgGSeL6JV15BQtq-aKjk9zJ6c8O2RNPg_oJyvWr8f1kPeE7raenwKtRTUtEOXWOLl3FdcTur7irhuLsEFGFzonExmTJrkZOu2Pk7gVpYDj-pIb54BOkiZ13rQdcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtNHfIoas58v4c3i13f8f7XWGn8S8eM0hWiHAColSba4i-UN_IFYJGB6NnitjoM9-sEt_l1qCpLJ7AkUubdQhkjsHku0P65tTLXHLqsZvyfrex1RCnypM4wv2TQWKC5KqTVCJ4NpWp6ZJI956_Mb48McQ2E50U2Z0kqnXJ9xZjI3xW1JL6ZA1CTF5RVfu7d5syO4c8Qk_UAweEEA1JcftuZzuXdFcptc6F4Y8O1ZvYVvO3pjyZfrd7i9ufTMNi0JhH2p2HAFdTt66-aPJUYyXX7B3pUIpA94ZH0zF3kOQhb5Y0repQuydiEFMfKquFxfEmAKa70mOji-Bb7xGi5yzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/It26MDrzSBtDTlVUK51tLBcnvLnRCm_48q6_sCtRhYwB0va2vL3yWw6mcAXndVPVSt-wD6J5fBNKNEU5a_m9ovbFx-XgnwIHpKiCK8FHtw61IZNcahSfd3hzx4BdzBCX9YRf8-10eBTDhPSRsTzdeR-OGePU6yEKW0KK0EWbxsTAYr4LeTxNtW4x8c8IdEJZbxmlBPSYdhWUSMZcmU919JUf2oRGxShXkqy6Wn2xqh2OhQUqxY3xWVbVRwO7ztMLmxVKZgwqhfPEfySusnuQErIKO1QP6jqrWDfUU37BfN9KInXgO56aP_-vM_0JbWnhcPJYkCBFTQf-hGn8eMZ0yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=W3JGAs0gvj-F4rAUq7cE1u0U7gdTu2FttlNt-hIqK3mkjZVihAIxzcC_rkeaVrt3PzWMN0eueTkPE9zHu-pm0tOEAVV-xCRCX4p8KhTK40RyHGohC-lG7fN-Ippc5ngx5bNpdzrHzRscvoU45csgVHD6NXC2adsWZhmG0i5PbDmt7WREVyk92an-FTZjgib4TgV-eLcZG7jtrGSVUb-9G73o5wbs7lDQyMO9OZnskwhYjX_Nbnha-D3B_YabeseHY_B7L0Lj6xG_xLqFVVbn7XeVRpKjpGgMpjwrjrfn3b5O5NgzOCtgaK0FS_e-Q_1VGoaiwxBzAN9sN_zK_UH1RwuTTCTwPqUXb2mQCTAm4b7WONHiImhugDcb5VDA3zjnI5lEEicKDwSuQEmtEFMF42ASzWnrjLn1kJjFpaufpqrJe1vLbuf-4-caoTX03WuD1ywwtFl8XBf4eDt7SUV0VjN9GEMR3Bkip_vLmXn2qHL5IjpCpLr5CbqYv9qvfwkw7yBSVHNaHLseKTOPMdtEbXkxkjTUXiVzliaVqJ0NlVesB7PF9wotc7BSIICaOdM6MrLf2Q9htL91hXVqF_hjEkaZEwMO_uHY77Y7jEP3ScQcmeWLhd9xou5BGg99fh6PnSUGcB4VTTthZZPyXUf0j0dqHQeJ5ovY2CWX7UP76o8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=W3JGAs0gvj-F4rAUq7cE1u0U7gdTu2FttlNt-hIqK3mkjZVihAIxzcC_rkeaVrt3PzWMN0eueTkPE9zHu-pm0tOEAVV-xCRCX4p8KhTK40RyHGohC-lG7fN-Ippc5ngx5bNpdzrHzRscvoU45csgVHD6NXC2adsWZhmG0i5PbDmt7WREVyk92an-FTZjgib4TgV-eLcZG7jtrGSVUb-9G73o5wbs7lDQyMO9OZnskwhYjX_Nbnha-D3B_YabeseHY_B7L0Lj6xG_xLqFVVbn7XeVRpKjpGgMpjwrjrfn3b5O5NgzOCtgaK0FS_e-Q_1VGoaiwxBzAN9sN_zK_UH1RwuTTCTwPqUXb2mQCTAm4b7WONHiImhugDcb5VDA3zjnI5lEEicKDwSuQEmtEFMF42ASzWnrjLn1kJjFpaufpqrJe1vLbuf-4-caoTX03WuD1ywwtFl8XBf4eDt7SUV0VjN9GEMR3Bkip_vLmXn2qHL5IjpCpLr5CbqYv9qvfwkw7yBSVHNaHLseKTOPMdtEbXkxkjTUXiVzliaVqJ0NlVesB7PF9wotc7BSIICaOdM6MrLf2Q9htL91hXVqF_hjEkaZEwMO_uHY77Y7jEP3ScQcmeWLhd9xou5BGg99fh6PnSUGcB4VTTthZZPyXUf0j0dqHQeJ5ovY2CWX7UP76o8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoMUjGbbZWK8OpEX_0W8656wa2HUsK8ExWvN906Nmr_GU5vSkWV9hI6CrbBrMy1z5IN7ajqZt3HVWARL411IQEsZlnfnkcGQHcFm-s7nKkXPRPLVVR0J1aFdA_AHxIy5yGykWJKuuzTdJ0m6T-USFeLhzzEsCtpcXNiW0uaYrBW1YkyUkrfDxq9UbYESCnI4itouQnUxdr1r6Kgs6pr75_SHIoCKxTrso3p_uQkS1VvblqvAegwkgDSeGmxvjw1QbGjXD8E4s-pk2d_g9OikEN3y__BnW77TFMADYpz_AhREaOj-_dgvfqPRVP6v0PgD_Hll0xql8u3FzNL7CbefGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=Qk4pLmUFrU9hbKycWDNUuBNxVevbFN8SYWynzXHU1HSbJSJ56q3WuRM1yROGD5mX_s-Msy2y-WIJIlXXNZH0UxDoTBUsmuohPGMm7wi-xqt5vwLXrrtpOrzqhmI2s6-VEGifIczFtK2CJuVBrgpD0V8OW8uKcqGsxLl6BT_kovXj0vCBJzaoz1WoYAAZ5IiBs3kwwrxOEyWjgBXG-qoYrF2s6kN3QxlnrrjQMqvcCu5KsAI5xG6LFlJQJIcEuS2VHZfc8byOlrtmjorxvJNTI4CHhLaaK6eo0H1-VRi8pxIB0h9bqcsCnfM2thvNL-VwPmflKXAg4Me8NnpKPdi7HxxnogRtIFz_ftZ3hnDAd2U3b_eKsRhLJyYXH32198c_qCcjg4zj0xV-SY3fKZOEPYowGUgyruegMQ0AnZGRJufNQJm9zYlH6Y9l3_glEFbZeKpB7fm7FjU2iqot2yXaQ_drckgt7HzA-bpAor37sPdqMDQ8WIV3AJzYj3BSabJcSVzsh5Ij-UTKNMEVVacbWUmyzjVbnDXTQnXQPoiihvV-Db7HB_cBopRJE3fkQ--J1krPRoCITEdkxcs-QjOwaG3RxX7WLsqRNMMih_Vh_jjDuKB9OJT1YqFw4Tcf9puobOOCPMWGacMehdNTKAErVl7Jnm_zJ15mtcKHimUF8g4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=Qk4pLmUFrU9hbKycWDNUuBNxVevbFN8SYWynzXHU1HSbJSJ56q3WuRM1yROGD5mX_s-Msy2y-WIJIlXXNZH0UxDoTBUsmuohPGMm7wi-xqt5vwLXrrtpOrzqhmI2s6-VEGifIczFtK2CJuVBrgpD0V8OW8uKcqGsxLl6BT_kovXj0vCBJzaoz1WoYAAZ5IiBs3kwwrxOEyWjgBXG-qoYrF2s6kN3QxlnrrjQMqvcCu5KsAI5xG6LFlJQJIcEuS2VHZfc8byOlrtmjorxvJNTI4CHhLaaK6eo0H1-VRi8pxIB0h9bqcsCnfM2thvNL-VwPmflKXAg4Me8NnpKPdi7HxxnogRtIFz_ftZ3hnDAd2U3b_eKsRhLJyYXH32198c_qCcjg4zj0xV-SY3fKZOEPYowGUgyruegMQ0AnZGRJufNQJm9zYlH6Y9l3_glEFbZeKpB7fm7FjU2iqot2yXaQ_drckgt7HzA-bpAor37sPdqMDQ8WIV3AJzYj3BSabJcSVzsh5Ij-UTKNMEVVacbWUmyzjVbnDXTQnXQPoiihvV-Db7HB_cBopRJE3fkQ--J1krPRoCITEdkxcs-QjOwaG3RxX7WLsqRNMMih_Vh_jjDuKB9OJT1YqFw4Tcf9puobOOCPMWGacMehdNTKAErVl7Jnm_zJ15mtcKHimUF8g4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOWgE7ccXXY-vVEIN5HmT505L8Wz5GTIJ3Zz0DuQqrmx5Wlt0QEyVaCx5w-058RVycdSB3NQzNFej3tSzOgEkvrv0MRCstwe0RaV2dk2mSu9oLj2BNsRgCt0uev0oGsnhhZOaD6_YfmKSorXIJ6d3mZkLAE037tYQ4zwzQlr4ZfQSnv-I8UrQfkFcc4BCd848LX2QpFNXb9AKLnLntqcQW6EBKXV3n8Mg2GjCZMJ6zd63eGU0HScx1LbMpfOQ_ZPmoalzN4t8sqxUnL_ZUE5srP8ryEKXnfLq8VQMNhQeUVqFoAPGSLv21jEpefOyF8Cvh4TsO5EXbwHVionHRi-hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKlpKAwE1QZnJxT9onIBL2SdbFtwc0A8z0jHEKeaEvanXP3jZImJu_-csDV_UMAgroNlVdMt9RYJ42oWH_m0WYLDqvWCZgXE0j_vnGxrhXQ17RvWvQRW_TeaVED3gW2EGDbLSDLHiCa6ejppvq_102lxsSsko95tRCs65rXlFCTd7Ud0u-fosAoLvuyhH0M-0JHQSronkeYwb2R4ethslL2Q0ao5Js902Cj3gVH0PShqHqq8aYfFNtadyW2LfEY6S-FtNZ3u-G1HT-gBQuXCUc8sHRCKyuWqA4KC31nHWZ1QWPnpE6eIYSRgfqQlJxlkpCUmn-dDPrUoqqT0ZYa9oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxTOyQqjnI2pnbhZ3osy5oeZnrAo1Rz73AX9BsrecAn_8_XPwcrC3PEHolWjiNbTVGgOsfCNRft9W6o6nrNS_icP0IMAZpqrqM8B8GqYAtc3nO6p8b2ZHBlXVQ8C0rNeAXzyjdUjbr9wMvIfpeFqT71ZVsWFcOh19nIz8LbgA3omf98RA_35abh1MzmvmHbkn1upF4LSvDWxUerrgnEgS750KeWBTcuapmgPAXZyu60FgVgNXaxcYdC8Mert01Ms7Yjnam0zCjin_1mPBNJz4XVJ3X34lZe82AgbAx3mHKCprFJoGht9CeQRrY1cAzTWWY4mH2MfKBBrnrhMVvrccA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srlLaloldE0kxVN8in2cBrvR32WBxyQTh2HD1so-pm6If4Yvnhwsfv6Ruic7eC-98Rz3RN3gZjBRG3HDJnKLl4rfdxaHEFSND_BABjS71ESmiLwj8VZd-iwuSA7bCAnWOhu6FqQuxVUp_BQqRoubtaBdMtinKdOq4tYU6J7xqpL1lOx5vb01JwOQy5w4uUUKkDAn7UO05SaVjiN7g8PYUJF7WBeD7_uVO35AIbvWHFxSFuzzDh1u58waCgWgm68ZUeUKFAPF6mqwwHZXLCw7YRaYGEkQLKpFec54jtySoukQ5rmtstq-GDbg7v_X_xm9kaiWt7HoSLO2v2skwwY_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0RSrT8vWS7FED-wFmZvgYYrVs6z_0q7sUXgDC8LnK2DLKeas2_GvbkeeyZ0E0dWS76rJMOxvqvIGf9MvmbzVpgn8cnxnM_HouK7hpAHB38PATbIGqWYTaRYsVhYYv_ttA16DxUR-HA2o6OcH9kLloR_x7eN_APYtUcyfmVKTfVtiLQOyEX0l0YLSOX0XPIsDG8mSAmpTCbth9pzlW5DXbz_bNWl1DWr1JdfMK3WIKfBx4--bvxlqj7XvE7T5WB_SEEvpATHinJBrnHDNJM0iTK6xpq91OLjcsSIEJ4Rh2C6mwtzbf05LfHmhMujSvB1HQQZ1_eoEG2nYLTMNgeMuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRaiQt5XPQNsLgRilNxahSoO0VSNL0aw7M6-QoX4tra_qxpmKrsxjq2q1x5s_r2SivydIL24t6Ljt3ir2TG2SnVdiKkDyQDI4MYifcy2APoV0uuUJM00I3iVvxvZvQ7e53WZWpUH6BPtA2zpQBzalHWVwMKmRGTwCY6A72uM8rTVvPuq3KzU0Z-0gbvRssw37NH7NDj4Vq9U8Viqtc8Df74qIx_bK8b__XLsJgJDUYcA9Loh0V_boAAYR-Lmh79oo1S77iDG9H72CYAEdG8jC_jFoutrf5AymoDUMPtmtMWrQ_rCAy8kCsz1BI846Yn4fQdYybO6yn8eYTlnxSTrdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwOhq_E3mG-4VkyB5L2uikkSXzeIgsuF2QFkPetqkT2wj3L96MGd1VfjCn0vNiZWcmHGMUkOAI1x9tDrcbLyy7Dank_79wTU7Jxwm_-ylRKieXFHUqdSUJ3qjJtZ4Z99pBH54NWNV4Mw1UO3TXXm17NQVrbkMNI8rSkrBxXVN6NM6mQxOwpCIetwrfMFT-9yEnjuMExbMi2D3rRzvvRniLXHiVeADaUnB1aqy7HoPeo64kcYXN4jmmWGH9jKIF8QnS2adWvC9zzkri4IHW_CDHWk0lsTfxWN9qO-byeBFhKCUnlXtxS7zoIOB0HyZVBxsXxbkkjIIGE5hZEB51pDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmULti_D7Mbpa579WgSEAejiCgqm-t_J9cz9BYesLF81SqQ9pn9iaqRC5ka4I7qcnXtaBvhU3vBj9Ao1lk7xRK9tqzS8Ay81fqtuHYnce0feM-qZGbMr85pwPRtOXNEm9RkOkonbVxhk8NI6UCtZZhOB8T_63GIDM6HWKSuCll_TnhbNYCfUZifGQcMX_KTQWRcJ-79lg2jHEASYIrNw2AaVmwxxvkFT4N5blVhBcsCaSlgypT2yJgpACWSjvIGAbtl4jeXfuAN4yCBAoi37tWAIFhvY6O4v9TbXFTw2_jKc-YDJrWCae7Nd9NKPWsYhP6TwG3w0KlDLZccFXoOuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idPnVWyv8PL1BhmZmMBB2z1TP6CEf1C2ifcdUjsinzTK8h4ZeOHAv3nYcGRaszOOk5oP1Kk3Ei6doU32Xy89P6SeTueszRqgj28Fs9Tx2OBQmvQ4DE1Zoqk-LxVl90qQPNw_hj6i4z0vpR9ejlGkA535OkRnrtobu1qVppn_DvRGt2X-OFE_lZyNbQW-lkvRCLm-Ocp4_7eCr6HytJZL90P74a-RzZl7skmSEXZRPI6HN1DLdHV3_oJ49iED4pJzTXoLY0xhT9TK-gp1NclMgk93oyP2Gifac0wduuqNUQtsLxCijppukdkDgk9Rl-23JWpwa8ooI6afJLWWbu3ugQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gE6xZf-7R1R0SQx-RySjcGIMApGiRmtKFfoejGPsw4Xi313bxyHeUuYsFU34S-UN7J7YCIDE5j7NmhyPyI6nvTn4T8tRRrwYiWe1mA4dSXuLyaVFsGbLIXmBwKYzbWNcXQpBN9mWDFbYehbMV8ZPCKxC9W8FUeLZT7JdI_DgDtTEpDXsLZNWZdICw8foFFKbRHhNCTVlyt9fkMyqtXD-eOXQcezIIboEunIbxT9o0jUVhsjUT_jKyMJxziVRqh8oEqIqx2bDxkWUMZcIqgBwHB-8HsJHK8mSunUXGi_F35Tj3QVngT9zakED9qATdwodcibN9MqktYZ7pstRQKoKtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnYrvj1kC-_aA4-yF0sCPJQOpQXjX9acguGWAyeBRJfXaWjeCeM4xjKa96D-IibHF9mG1wR80wMPHS68ufqKJhhm7phKOF5MGJOMDeePI0ENXGh2RsFHrS5d10Z7OZDlZ732V58UyoNZwBkvBiBPAsZayBmFqqOunASzP9Fek3r-XECcQRwEXAwEzrqX9zhobabcHCnkFTnsMj0i3NPc0w1OJY8m5EWBm7W7gnIbnI-bqTp1snoKBUev6Lc83Jr6YZbV2_G46W3RcFiUAdd-3qJosxCtFsykEtd39WFo0PXhR6lHFS3cTQbbWZhIVfamHT93A7QzIqvPGkpT48c-JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmM4Nyxnn7u0KfyDOROFlVGuDxxuWqES8Mez_evPYDSOxG1G-qLDNtXQTt0H1gOk1CyKmuQaDjPlXmzC1q02GlfTltdUL0vM0f-G6THiY1IJpMNrewH6YzzAfR8QAYQfqlc0xB49RDRah7twwXMDSSqIcxUYWfFFhM96Poq3eXeOf_1w_SpfhbmXJUoXStFlX7GkQdg-Mx05lrFSKY5xvnTpNPGo8yvIA27v8yJtUkgNBVkzdYxV5SlKz1tiHKzuPvpeX9xAQseSE7jFCBqYxr6j5UoOK6JOjsn72Tv-8Y3ztPEzNhr8wYwmbuGFQdD3iJGO_eNEedDxNTgwILYxvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvxmibhFwgA91GI0omxoVmcu8dLPj1lgQbP_OBYukvWTQ-73L0FfJsErPEt66yKJu-D7BiOGbBoBCaWjiqKAjjGs_p4_I2aqn_stqEfk_QcUg6jBt7-VOTr_B-Z77nx7BVn4LSuhbrQLIt0jRJetR-ZsMtfjKpRC6cJTQjUtMYVlw1omN4TTojMSfWCjQg10Yfykl7LfdFMEbTIqr9p5JM8VXVvMCqL2C6NT_FkK8db-TNpgUiBzwv25x03kPogjTtnHCFiI4I8qqBj8H-bynlM1B8Q0SNRgCUhmXHH_0VYhZAJntaXsrhufMTlyc5jO7Y2V901tKqaSjSAmtT8qcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBQRF8aP1KMZvGHuMkl9FHW99IkZ-ar2VLX96inmYq7gIsn2VHcXrFso6zgAWiH5uZm9C9QLK0HHZCgKabQQSIWoayKRGmK5odQzt7X1hdPWU6dQOEKaUHDW4kz4Ab3_v8EpvWF_9FVqvoUmiQ7V2F5NLRpRfFkz_Rmi2iGyfrWRx3DxyOH02IOFq5U2t2ptqNDAvc18iFZem8DpvDG6acH4C4MFw0SAolRx8Y0H1yEP4RJnWOqVjdStZPFR9LLMzoveOtt3OOWTB95-lAeLofHHkEGOqOXX8Ct828bQ5u0XAeMn_aVqlvAC-0L6khJZHLmzXqrwO0ATi2E9ezMOsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQpof_8_iNUGM1dkU7g0bCgTLPVXnccXg4p_JkLNEwl1G4oGiY7V56gso7RHLDUEGdoA9m5PabaPsoj79eAxns8o3QrPQdrZcssTNlZcvgeN1DWu8iTseBNLD30wylMq_owqTDNijjI2bFmK-gAnrQheOgvs4x_pPFnDv7-ZOxQXeI_j1thUqtXKW1C2jvxw9XAt8Vb0xccGMXCOC6Hb7XM77t-SJfZQ_lfWMkQSkZuzcF8nFyoAYiw0RfDw9ueZOyqJDg-RG35WWiIM20GAZdMaBHd8H6htOniBlneUHBAkT-BPqJf0dXW3EfUA3FlS9K5rYQP4pQGFrHfGfjI5dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_wyqOYloy0oreo4MvkoeUrMrxALywMEH4Uwy-g2jPNQlbsCTVwv4gWqEFfmTAwaMY7C2jYGSeJjk6Ze6TWjp-h8iW11JCKh9TAChhIc21lmZdRfKbmcDUGO1MgLIM8AoJIX6ki3FNhloL-mFHYyq8iTPdWP6dnbDHJKjdisZ7O8vHKFEGf01PlK1CZWPX7BoKyawHOPZdml5K_-nL6iUn1Z_J_b8kyB2qHASj8u9fQX94BuekcputSN16CivtIp_Sl79yQEft5i8L7TFm847VpYwd7zyiFkfPEV-TT5WMXpqadqCgZRl1xxi8EdI481p15Ft6tpvJTv3mGK6nlN3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rbn4QiBL3IZITTQexkSmizUeGUUspju0a2XbqA5ACZ4ufTDLUK8KT4oV_eI-sw-Lk_pBXrL3qzkomL7-foDfsdCS34uL7yl6ljkSF3jW-gXv7lf3SXryPZDZGOdqB6-ND13-sGsmROppvvQNRnMIu431XBQJR83_yKS7FXi1ZUaCBwYG7uBKvf4vrDNaAZU2TzDHWw8Gzqcz_Mh7nUYNEasFGsLz5YlKlz9e9ZoSP0J_yxVoXondR4C1e0Jtkq_iBCHko9ivN0b0Sa5oeiz37wkmUF9SrJddZsLclBJVtkN0qtJlh1o7BY7QdxGb99vrrYOpSee80y7urGRjT_CVGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kFz6Id9rl_iE5fONIcqGNE3tclOZpP4tXJ3dtb2Lg8fatKgPfYKm84gyk1te6N25VdxLg4vUuf25O9OK3b9-xg2NPlF_qaRWjy1dBYHEgxr8bBIWkiICaaWtcClCZJ6Por29GOgZ5gjPnFfRbwVm10iF7z0YAe7OWMpfAKjVGwUNeXZG3otexGXVlqloVXw4PsR85qij0g_oTpKQwQJV4kCBo2n9Dd2Bmwh682ecbn2-Udk-FhoKFELfxkiM1niCWIsoqcnMzXde59DvIbxXhILXVCzEDfGBVsYEWACZfK4J2AVTIdrMbfm2yuAOhf_qGRXXK3v1jG2PC3-R_VEIZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-Dv0LlU0pUhzvPw0fLWeQ3rH6mpv8gnznC8Ru0ZV6EzH5_VN0SI4zmBrkYL3_KyXE7q3-x-MLi1gJsndz4EMSoNni0J36ePLYxeKnEhjLx_Cg6wWuXyXE8tfjEf9SYybDDjL7SYQqGr8w8aiJAkE8oqgGmpEvSjWGZR_fXk1IBQEo8Ga9CR0iA8FVrU8O8TklupA7E1RjwNDmpybo7b6BTsiwjaQnPwJzQPuHZ_GK72P5XftGsE70r11qEVfRtbVO5gnFDCcizaW9KNyyR0T7CRnbaJQuAVkXH8c3e9prqK1QBIaflN1VzhNG1iiu0vv78xWWKnQVbthath7KKJUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STKMRkR8Wf4gkgKoQ-ahOTH4fBg5Deyjqd9FfSkzHwriH8D9aobBIMPWrKwude5OkCM1aLXfTcVF7q7SckCl6peSLhLmraJSceOvlL86wd8_CHH9xAq_jIfMa3eFhkBIfXIzslEFINVjjh29hNjMmJBMnpPOuFCoz7Gv_Rwks9GtZFauaJ0VzVZ1toyDxVOLKIeZYvz_8W01w-YSGO-qLWvXdnAxHBrMaaQQVUyKRlaXraIMl0ebp0KIopEcbWZ3MYxkzEtJlBWNh0HTgAHxFz-Rw75LQjGQhnq37eINErYmZiBEHPmVwz-qIxSQ8FB1EeGtlqTzE6XE_CYXn8uPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSmwEmjMg--912vJZbq5f1-NyLAbc5Zue_ESzcehMyQcEhwZpiKgb3EV02cGiBbO2-p0ajm3Q2CCV4fEPjuQ8S0xrQIwnnR8VQT9BgNvZHd6XK_IWk3jeC7mPaM_CpzkZUVJhyNYCZyIvV7VaVCuadaWm1pBMtyhudm4RU8NXBHy3zbEzBwLj_WRTyupdguVt5zdfVJ4cB-PILnADR-gSuwbJ8C6ZDdSZtMToIAwrQQmylgXxt0x-iM5bnNXXea8nZ_rjuvfDpu26Fhw6rXqFuqDVBGy9IT-h7Og6ag39nQwuUhrJ6LOUigK2yFfXOaTRc-aUutC2Lk7FwchK4PRtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRjpyuYCZ3_w7T_bHte7feoPTrPYcZi2UNBlPfOwKPRfctEVGICbwoyE45ENyc2-GqcZqy2Uhbm_a4zdK_IbbnM5c80zhonoPdQVW_gbg-pn1F3ASjJxWbiQtZpKhP9JgcTNo7EeMZpWCSk3MZbGvAK4nVTfL6f90nPQZtKILNEt5axDM1XliEC6Toe3kcDmreKwiNhxTernHKvhztwpK7VdCZegGnEuSbrxpeIwry2aKANDC15tlFlCzToauQPjTm13WFLpnpMumzzJpTo24LKPVbHZq99UVi8vgBMwuhqgvBFeHh66_550GOMmUE7Pc2LxRg3mtAmiLIChDqlC2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZ_pewfvTNInFvQaEI0qjdMDPuIejR4ktOyjotwBsKrVTlvQ75Dmo_Kg1tXS7nEIh3XBe4Vya1tDt2FUyyAZ0KQpyewRam1vg3D5XkMwv2be3VcKsMLzq78nrli5dp7UzX18LPa4ah_Ob-jQtV5ZtUplGKc6O8wsrwSY3Fk4dcX3Oy4iB7BoBWxOXvCMaY9AWDt4JHLHGP6TmjihUOeiJVQte6ZHNfGeJjbXAkyHkMViNPJcXG7qq0U0F3NW6kr393kt0xRo7wiEj5jOOOzaS-nnXm6bAdyvbwFij1zDVCdrEoVewlbuiI_u_blkIeoSmCzyhebJLOs7PhIQjM69wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxwsNNDfxd3CLw-TiQ5M8BsyBzXd8o7MGskUhurNHaiaZqcZ7tXEFR9JrC0S14uAT2CFSLGKJeyMsB16sQ0zuflothX4ef1yfqRwsXdPWRiehKM1afq8max1jA0_Wf32PHngBuJBuTRaij7Tilu28dK2DunIbg7WXW1dYAi5-SFYO7YLSFgNvtlSrXjv6LOytcWc0sJ606COH9Etrjv0eicj7ymediunwpUaO0Dy7TCJavnHwMDMeSOzSPp4nIQbOp29p7HIMU53lJZWrqkJUmtHFqTJc9Y3tPC0r5vLfeRS9C6ag6n4OvOecrpqNe70EBLERFIjv7oGn8dXzYlreA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bb5iw5iS7LfjPRzFt5bdfUliPfH2tE_i_rs3KrsDx69euQ7cWZMYX0wI7H4cyI4IAsuPSgos-VXqMO1ZhZKy5WRkscGQHO1iuKHYjAO2QmGXQZE0kFFzlGYbT1kOv1TBFhU8xeZhkYutgioNp625u1yxytzZxxxq6Jk-ZZb4j8bB9LM3kwUJHX3huyMs8xkTqSFP1kyvIwEgpFJcBdVdibFzpdK3e9IrqeNh6O1M1nCVjwiHuoGnhsjwM26CYBzzfjS45BcawMoZp9xuDl7nRdEELZ09Vg-tYkdd7zH2yC29uhP7ybwZkmF6YHCsYBX2tLkI0RrX-DK9RcDfTxmw8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2jtPddflZwPgYHHuyfZUSvEoksDpXk-4wlAqyTQaactFpJaKs3aVDEdoG_oFqPuDdPZFSDmwevbIIdbQ_fjZv3soUV9hiwyVBmu7VUrGsjVEgS9_mt52mvj59x_BLFIICPht0KFbtKpDF9SXqQ8YAekKf5cvoHWoHlNXRiiVq2EmNh1mnYzdeLMrfIkKpdltTL_X8J-7K0fX0tFKAHPYRpxLux5FXinhi00taPYHZ5DuTznpKiz-aOS80VRy9C-p2lbKd8238NZM21PUI-diPCkfXACMWgaw1JHZIbePUYsU16BWE5b5Ro7iHblAE3C32NdD1rphJZ0NvaiK5r26A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYuEc2oFYiHYsrRIfutdYE-dZO1B_peoRaDHLyXo1KuVoLQsxduVsiXosXoottR3GuucbvbLC3UX96ySw4YE3fOH_JwwUOg2nePuh43PyVjhbLTGXIjbFgeC4RbMXH5XDwZYqexZ_I4dpzL7-SZUKp5u_wgSVkmgiHNlHk1n2CB0V0wp_pDTA6GQhzyjlpUvUGbCs12tyhTQK1JMEd7XtTNnIt80dqReZ0Ni8fZtGjxE_bUyqYNhimSg6iqOJxOxD-VNN_y-oZ_SCbMvRiltF9OXC-gE4SdrPTAL-ilWCsceXZwFzH-8wcr7UmieW4MNTck1tpYB4r7kScgzyglZnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAfky14mpCQcRws2uzDkBNDP3Zn2--uDzESY3Vhcv1d-rt25sqy-L-m3hKB_C2Yr12ZOzjCx4jcSLpkA7nAX3tYTf7OgFihMqENAtQwKXR3z4smzTsfMrUi2Iqwplq8ROaQ6E9-EH3RnOmxxtMQ9Jf3tp1TXJDEYAl4nNQ8mTtWK2FdNdLSfKR-JqUqLwCXW-2ooFnm1mWW2Vh4hFyXTbVsaH7jHK1QEUe7HgEOAAw0lAXkwt5aLVT2BrJS-LBVTBfwk7c3yj9IUHZ-rwmNUHcUqFtTcW1wOuMlla3qiJliVVUwpwlbLcesT7DwbBxgJSFazHt41FBlG0T2cK2067Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFC1dHQCe-51k7siS_yVRZfy-kibch6ve6XQiItOnoY-nFLw8FtKvJ2bHSUzYNvheuOTFQ7AcEYhEJkNJITy-XNpUYDnT4oh9E9yEXX2ZNB1bwgfwdnAG9TQaHnskdE7k8j7zFCo8kGrhpYh2qrCMomwmvsQZCqVrqwdls2Irju0YiN6r_L7HBJBl73qDx7npND37bHVKKXj9xgpMkAWVaXiCv_c0-8aaeXHNQ6AM727SBQs78ZAYyIK60KD8V4fVfmwAVdRbJuMKpp5KAv4-_b5dUIAkLNBKM0VK7UxB-MN49Og0VmKJN_4KEC6CLf-4fU88N5zJL7D8k6-xseltA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-27Ogh9nfNS7H_Mj_YpwDC2oYgUYAfmEJIMt-cWzvewcy369OK81zfsfWPw-LUjItyUcmMqh8EfPwdqpjYt4FoPn5-2tB7715ucc3JMR_n6RiEIhzAveUTMA0u3RGXHd2VFuU-ZG-yO5CMk4CpXicq5Jrqpkgefb9R6C1e6qGobTQM6pwCtjwvgc39Gx7GjnEW-EsWOo36jmwoZXnpAphbTCvntfXmtFn2gC60PYyyNnv9yHkE90g9xnpD64K6IabGj2n-QYCf4uWrJBjIsX8L9K83qQ6eJRQ3n-LuxzKAZB7QINh6c6iea9TOhfEL-p1MPD4_dWfYpa8XYXpkMhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqTIMsw7w2GPjqhgXXUnGXlyXgavssXMn8IQ5Axim5SXwogtf5wrAyEeQA67PLr2zOe7RGx6_6lAkisWlfOh4L1labVZ8uobLiATLbIiIY1kT1wJV6TNg6hPweL4lqOGTy8Ic5BmUJt18-XCAY7o65_Xx5SrZ7oLwxlRMoz2Lw2YSeRU7nbCoAPKCbNfbB_HbVIeNNI3Xa7ZXrXvSvGc0XAgFmKWxlBxkDSyOqlPfNz7AjL_1FiZpz2D9kVNSETAkDZgie9s8A9RFJTq_qaieIuhTn1FULXvx2GiGs75hO3FeoXK1_xf4o42i_blWDbUzblDTeOw1DnURXdRV5jGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8dU2r1uEMi0ts-eT2l4fg6wnBypwGJg3gBrtfIGyOY7QNXle6BPTm2ewCGxyXde7ah35y6VSXnPkfX3YkAhevgplm1RgM6xdLQICKwe2XqMHn8JUsg9WfDdS_BrPLeDGjtehT5Qe_oOrO8pCpgVrsneqXgfflKyND5WWnlOmRKZ6Aa1S7dEzAHSS8SJwPrbu6mRI3ZmQFncDw7PjR7U31ArtmogeOzEDrOyCRqejZAHsPnw_x02GY4cqsL9XDaHz0gaX0wT0ekQBLR6NGEYR9k14OUDsg9n95buxED22yD_Ph26Iw4El1na0cQp6alEXpp_WNVLBYj0dUMpJg3Cow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
