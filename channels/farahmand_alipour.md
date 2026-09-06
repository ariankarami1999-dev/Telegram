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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 12:33:46</div>
<hr>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEPvNPKmo3Y3Dh-7BN3AfgbMYIpaxh6BhM89BiSaGPhhVVYRt-VswWkRfURY6IhG_eWCcfc7Zj2Kg8TW1k27pT3GJ4gF4oZGC7hrxaQGx5-xK1ZZQz7SOl_Cjcb7QI0Und_ThoDCp_ebmGuuWyejZnlFjxjLEDrFwiK7oXYEwh2X6jHQWdNqwN0Pner-oBAXEgwFlCvti9tWRGbckm5KAMNmlhMiLbXjPQLgk7N3Vm2VX6AsyLvsPGApgNg6VoqGd1gNRL1iafTgiS4x_ogGWXXNUq3DepMx1DfvUdNHQFbvCjivhexaZ93_GkLST0r-xMZtPHfccYOT22sZE3ynPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbjp-PRdcEWORyoBfNoYsRDrz0vP-rOqtOJmksVDE4lDrV29CQGpO5Qg9EtsZrVfHafO9Zcdw3MTbGiaGjAWjBiAU-m2y11BliuHFPNOxrABUSp1EFP3BdNEzTZuO5bmrsSgwcNvHyOOiaHKieX_w3WJfEpE26zzjh08wjF8SaeNRDN-0vuDkNQ-FkphK_MxSXZ1qFEB7uL2Sa5odvQQxtKGmptzYGb1G7BFxYiDliDK7dgHEADwPNtMOootKMvM2qgtPxEs1OyHuEFiODy900Tya957WDph_MgJaAAPDKTvzORzPHTq16KV-AdsiIcRqnOgGc_l8NXRt8Fa4OijxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qz71eOvpwmWscgntpRQ4INwXrXc57EFgb_SDMIcd4MRC49wQ_C4beG8wCsCBnvpKukaDqv-bmFfPkEg5UWWlDl2kjNLK_J6qjvRUo8qqYHfKxh4XF43JL2hI0KFnk-RB8OWhpqFcK1mspXkiVeeE7j15HJQXW8CBSv5bUkakADafMzbMQIu2hQYhxBFFF2vaBit9wa_d3qYSYbxyuCf0lj8OrTOdu-NT2vlnp9nBvXoBzfqaV92JhFqmdizItXaJ44sYMV6pHK1SohHXMlKpbCRVNqsKKbV5BvWFW8ZyHV8yU4uei_BXxyYQtMKt6Y7hVSRB6ZCkN3N_4sjE0yXhjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FX7fpzUZHaRLWeC_H0RQteuy-Gtf1VkHRc3lOXbb9qTS57F8cBcd3rWCk6EX2-VGTehCDgjdQsD2qENqFwNJTxD_DK22XqtfNzet3-Wndf6AYvGy2W2TM5qFXB85BEY0wLtaJJgWDKwJA--OjXDyM-KQgq0Q-Ov1JZ6Sj42-nAFMHzZZtMqw7Tr5b8onBp4GyPZPOmsBxAUSmBtrNk7PQuu5L96i4YrTYkIRJen96mBpJZZFmIoY-R7ORxZFSlSZzqLAqVq8Ctjj1uAtwQBELKigv3w7iyNebnzHzIlX8vTzOXyy2ELfpSL-TIl-zXJZlwVntu2jq2Kvmg4mpbtmSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPezdsU_hFFgawlO0KeVI-GLcODr65bqzuDQomClvsgV_BIgKnS4P_ctmdYoN7SUHdzzzfSWd7cZkuUJV5KhWmaioYxpTPMHJXgBLne8VX1ZG2TKxlI6ez4L7U9kvtZLSgvPqreXtZgTI8CwsDfriiWfp96yRLGzjUOF2T2dnjaNklkz5AgJB199uDleCt04P06WHhXoKsg8zDMiX8mLuNlJx9ry4Ogj1scAQlmhO6Q8nMInaDELL1jRTtLZsURCvSpJOHMG4THVuX9SSBOkr7tslaOVy3Lh-i-rF4AiBiIGfrKfbVHtXz6u__5lYWkpQ6TnmWGoXvLwEgkLCmO2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUGfAngaGlY7ijuSz-npUATlbNMhiAqc--feYkxn8piFQrgnl3DDQxAFkCQcQko9nT4kaqEleshQU7qhO04x-xA2DafjxPQAnxeU9htzXiM4swwuZF2yKm5vV5jDc_CsOtEsvzy3qMNOhcSdzSSYsLnkA8LXwsD6FLYxd1bCcPoblr_JH31gTZwTdwa0XhgFOqmDFDITezxcFLqWkxV4RQ5IEDEM7jw8x8WosFW4Z_5eKvycLUN1ArloKKUn8Q6AFaO4AbpMypyQ_oI1Ac_lvoz2FoN7QJQEKfv0JNbU1zjWv_S67uoKKnvkfygBjFMu5CXmXHcjbvNVbQ4o1Fx0_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oanYNfcn_Ei9SjbYOdzim8zTeLCTDOf3WxHs4DoGaiFbuH66TbloPh2grCkgRGZ1IJNKMsjBABWMnFfpWjt7w8KjRmrBS1z6gpgs5j3h7LalGsS7ZjCz4OxptD1CEY9PmIPpwx23usbZMi9P5XqeLZuDtSTd8oDInsEXU2QYLzLlnrOZMzlEW0KLXyaQ5W8yTZibI1L0DAia1qI5xAwmGQt2ISSH7ZEncESQbaKzlbb1JXRLAYnLNuXjVYMUGkvQuMfZCtZBIQCAwuno8cop1LT1RBRC1q5fCfwzI0OWqI_KZ23GXVxwhBPOoR6h6QgC4ZsAR7enHZYFaO8_oWJEvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fl3wh3WApQz_vWZ1OcAOFOsCuI1jUYyXWKNxC5fuSCV09EJk_dBipMIvnXgv-BC_kNfE3FyCjBCsYB8cJgT8tdL1idc9uSggly67K_t7lntqKhNhP5gzK2Umjq5c-cr4bPCBJnksnHYSxopfAXA5WOrMk5iJGc7wFWtI3KfY5wHiqKS43yZ3cBnKzaI_LnZDYg8rjd93OssrR5jMMwJpJusB9hWbi4Px9ase_Ag4gLHlBP_i7-nf4XYTCnutdkdZ817EPNJeSBgbPB_jo9Erqv7XeQ-zww1ZcP-rmUBqwJe6jiiSUvHFk17PZPJjvGAxoWs5LIFqf5uJvNcyWoaGKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoGY-Q1cn46A8z7-hgyOmGAW4xIinVIwbwMizdDqfBhJiHo7PHVUZReDyaQOvhsDQHAjXjCJqqc-xpT4ahFj-Hs01rjh-C0OA6ejto8jlsU77DCS3I3Sro5-A88uO6wV3mO-JDaYK0CxoVRMUpH2RtbdLjxo8jxR3BgecWuzyHZmTms9_iWpEXWYB_siBYJ058n0r2-3Hpdm0AR_byCzuzPgf1vZ4eE4aQLIFZMW20LMXcc47ZEZvak57kChADTJb2i-xazK2roefHVduRly5rSm6bFnp9aVLG4QrbJl2L_o9Dbcz7rYTcBHWYdD6DGS55CkaN92oaVKpzd3RO01iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxRMOblslywOH6bSAivcQxxI8zcHfdzgkf-P1xp-56rQzD2KIotNZCC8g8HMU-4wNXfejL3eeWyWhthW4OnNscIfxYUnPDPy0mAkirfZXZNL4QK_MpszNS6AVBbpPFgVo7Z-jzFXmzjAfmx3N-jHS8GRkyItJYAGad-AStDxOYZxK2B_iEotYITDISEebJ0nWmzNybEvMaqhJvuq9Cv9tnW64CqT2sJj1yvnSeOD9VaaqHHxNzhWTUmvyY0sz2CHkuW0CS1aJSMed4fjimNkv6rxwKtCkiV_ISdmYLi86OaDWfrMj3UaC6toJMOPIPSWYVl-jIrue4_V0PEdULlsyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YHmbf-VHKOYOb92G0a5OPVqkqHIHEEQ4_SGWTvrnB9dh9d8MhhPjerMt-4WFszwVTleYTS1LbbVG65x64QKE6KGJpztwnn4qV_wnfer2s98jKpabyTrohikY3lT9KyQmSfWfzTlUi6m37QvvtAgm1JMeggKlSkkr3--t_yM2Q0NEiGNng2EIZl3DUVSsaf0nxrxILWrKg1HMlYXF2cvUcYBvBi_1EMXxjT1gR1RarcmbXWiTqIAe-dw_yyNxrJbi6bOq5-elmYgYp3KF7GAGUY9lWUwBFv9ZX5OrXzEwUodjFhVsc56aQkVqnIjRWM3arZbpWO5HOx_bGq_1cEDiwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBTYgw7gxBSisVUNw2AsNmBfB6c9qWOfarOTIiVe7yPscLG23GNWmyLOeBZFwbQNuw17oowmZURLokt35JJ_xg7KTx5WTcYWfe3ApCuElAtKpbjJrQ8Zu2CgOG3axwIyamU0lFrFFOZ1Z1l9NR24edpfD4J-GzZb5PhYaME6wkxFIVW439QFRZkCxj44zxxEkM6dccBGZRdDrUeHd9d88kOVsug8fXw0Qt2mGOmS73IAGYGP9FkOJ1UyHhOJ4LD92OOv3fku7DbIJwkfiBcQuSUimWNHMf9smpDDPTmuwUOwCxNMexewF6WlJ6n_VCgPmFZWdREgtX0EFWEqIh5e2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k7R_mUFN02l8PDLrxWRjytjRKMqz1_iCLMSKmsZhcAmDex1g163y725r8nsTC0u7pTRhCjunO4c0xMmfplnaBac6LLeMryKk86jpjaEv5avNo3YXNF5xdQ3O05MYBM9uDAD8Pr1ZZlszxxpCLkYrqBuLFoewWlQTXnPzvtCkrRnpv-CPFTvgcjEjCqLlvpVRZH6JQe94yowMDDcHAE1L1XArX2xgjNg9Gv77M0KTvBzq4Kwn0GXbCLHBHyfQq7Z4VOKHlgo9IFGSK_9RXfRCW0do2nBR823gL3s4qUdLXt4LkVRki6ZgEa2WOZREoOVX_8iOKaDo1yGCiHqz8glwwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4Fqn8fmXQxNiEPgId7r0v8uK5Bpuu5r4UtXSOXNu3U594gfQUJWwVBkws0miiyufm4rSUQHjz5wPA7VNOCe4R57d4AyJCGnpIhpniuHXUR9vfYofgn-wDFoAI_8_4SlkcCZdKe0ubo7iExWJzws0CBOpXrpG8CwhOXWkiE22J-M2SKnyUaOUdNRqfZYH43yKQv3xD2iEg_IS8E7HHrXcLRqJCmBDv3W17R28spkOmot9D87UxgCpj_32cA5PLO8NG8IsAXcUxwhfC-31OQuk2wMyeGvqMaBlOpmiPKocyH747mnQ8AlIiJMR2UqYjBEiFqmLekpCjq3QUcEplOEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTgipaKQQaLgFHMyGRJA5Apst6E4gTyT-_cnKXYbmjWFYT_06_l0XISXmNgbZoy2T81ETioVdyJ71z_3-Q4wWOqMeSD54W5mZZ1bIj9P48QDtsW4yWow0Eb_xUCtLjFaUOuXyTV5MENzfQbTGkMXomxX9ciiXGc2TROst_WThbtza437OrFSDn2F0wZ9xGgahdUmOtUcEqKi8JhEESXxMx_4I-qfcUhUZwXfjlsUWaw2oIuJjKlq4vbxoQGfhIDcw0m8AH6QEev-j3J1T7R611cPtpcEGGBni5c7HLxB6JEnWzt0LP5rnmQTNhWxFh4Gw-9VrtTiGDkDhBNl_Ou8UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=PHNobqwB6gtZfhdY4SQ13oSwaC_iXNlEkENGisBmgkbHGToyPlOBA4RnjsPOnKL3XaxmUxi5x13cnHAP8jkE-VIIHx3LdS0rCedxY8Zva5Bk0w7W26FoR0B0pfW05JaG86AZMUukoSkjh7zk4zCpagEgG-KLMtKChIsITr4Nqj2Q03uegBnoX6pWKuCnrk7A6DD0kEJktrXXBvFjPLOQ3F8IJ3HG9MPOT8410aDiAj3l6h8UNQ4zepxjR6ZEt2Yc-pOjxmVW0eUG-bO16DuGOxwGScuDofDPJfqmXJzJvrWGmFO4dihUUNqj92lxnZgKcvpxSSrIjLwgdze4fIGH8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=PHNobqwB6gtZfhdY4SQ13oSwaC_iXNlEkENGisBmgkbHGToyPlOBA4RnjsPOnKL3XaxmUxi5x13cnHAP8jkE-VIIHx3LdS0rCedxY8Zva5Bk0w7W26FoR0B0pfW05JaG86AZMUukoSkjh7zk4zCpagEgG-KLMtKChIsITr4Nqj2Q03uegBnoX6pWKuCnrk7A6DD0kEJktrXXBvFjPLOQ3F8IJ3HG9MPOT8410aDiAj3l6h8UNQ4zepxjR6ZEt2Yc-pOjxmVW0eUG-bO16DuGOxwGScuDofDPJfqmXJzJvrWGmFO4dihUUNqj92lxnZgKcvpxSSrIjLwgdze4fIGH8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=sOOvG4lJ5-DsclEKbldJizHO6x580z-EErz-U2jhgnEUMhiPE5nDX27J9HxHtHVH6ICNeOub8D8fFIfAJP0CFsSlSWNF36l-y6biDcyqfddPue-fuGMD0MkwXAHd5Nod71ExlGg_uc1HGoHY0c0akuGBJIEew-fcIESF_r5nNIDsQ5NS6gndoSAuBoavS-STUAyWhCf_SohkBxuaZ7iuLAI4jJshhXm5UsbhkuIR_FrCLJ8-kX1Eq7k8TJOzvfNE8ThL2uXvq49pNAwH0YxVAsq79hXWf5Y7-Bt4XrgslQjOYJmUZ0HkEYUbv3VUTvke5hcjTZ-TVeoQxDFC4l9lPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=sOOvG4lJ5-DsclEKbldJizHO6x580z-EErz-U2jhgnEUMhiPE5nDX27J9HxHtHVH6ICNeOub8D8fFIfAJP0CFsSlSWNF36l-y6biDcyqfddPue-fuGMD0MkwXAHd5Nod71ExlGg_uc1HGoHY0c0akuGBJIEew-fcIESF_r5nNIDsQ5NS6gndoSAuBoavS-STUAyWhCf_SohkBxuaZ7iuLAI4jJshhXm5UsbhkuIR_FrCLJ8-kX1Eq7k8TJOzvfNE8ThL2uXvq49pNAwH0YxVAsq79hXWf5Y7-Bt4XrgslQjOYJmUZ0HkEYUbv3VUTvke5hcjTZ-TVeoQxDFC4l9lPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUff7RopPK-kl3cGPRCopx69DS1B5X2WPlPQDWN6lnQbxRwLfP4D535K7yQgTubGX4Day9FVHaucWTORhRvTycIqCZdFSkwD3vuAbtW-OMSO_mBtCqcU2zA5nNlCCCfkBadj-H95bdZ5tFIJVsbKgrR9k9S8xxXzz6MNmJmjhxm7EAiR-mcjRdX-q9PVQqKYewGuAXIbfz4xtfFVXuh9jGKsHJrkkS-Nk-58om9YlX3srArk7EX-3HI4ShE1A3b82XsaYOKbpj8I3lAqa9c5R4XszdYVYC0wvD0OzJ43Q7Tv1VIDrjzxrpbK1C1h2doOJBhjg3w_-sFOS8d9kZqj3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ec56vzbb87SAY63gpKIK8Zd-EULbw930qftJSptiQ-HyWOhZKQKtBxYHuXmXRJJrXz4f6z0lBNecVdbGIoETyDHnRwPHsx80lvhpmgdUUTHuGftUmWI2lVKX-Hcerq3j6yQP84NYKi3sY-78MiplAxZ5_yN7Uy7dtAsdxKEmJy-38VtpToIpiZce1oWnCf1NXAWu9929gu6R0pSF7qQEwRqo7o56a9k7G2G8tW2iegFpIvUlsQQAH77AI3nI490BkG6pXwi0QUajt16dlicDsRg86-SqkXdNSrVI92Lj_DYJCNMvbkIDa856C9pScp5zBDgmSFrGglbgx1EVTTR75Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6C5_X12TmMRpm03WvXKB3MKKJJfzEfkDhvFvs3JBg3nyje5ZVAKN7RYKaCmOnQ8r6NMs4KtaJ5fMz9FAYXrM-HIDVPjPVa5wH9FMFzkGh3KKDjQ84mFogfeLPAUnIxPJpxCMAQ9kVChDX2tCISM5G7YTYWjb30YD2TL8OSMxqCoK9aaxv44pAahJyLhtyWn5w5pHYOeJOvsc75IXPq354eGsCZzQpsXbH2YB3vKIfP2dEep58ZVeJwf9yoOWZVqRKPLpU_3MXDz_G_m_QlAQPeDZIYxvPNXC3MxA8yILlBcEdrt_nPKN3-IQWiPAunVXr5KlFy97fICrfsPoVjtTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJFWgjUYzxnzj6ALgkAxbYtC7T2YZR6wW2dFh1YeFOeKvJr21s2SXrsTOZjV6QgQiLQ4nwo_KmMIDynE3ZnO-GEZJK5K6GURuY0LB05iNngLg2EcSXMoE-hh7s3-oA4DEVqUZfEMrZGCRrq6eAj8GOt4yelAuaED-ca5C-BZmRPvXVmX6YGhnM8zFIFfMxDIjXFsocXO3r80MUYi0KiNeuloIcarSVUxx9wOYmlxsbwlXuaBfVVWKmVJmZ14_KAwUkiL1qF49fIzyYvtqg--aCvZC6Kt2Xnsc_pp3PzbxgRhM6bXcO50VichSWJBRuERsnBog1eW774p9y8cvlGypQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJvkFEceRKqKewONd5iKNqOZPsjJm-htSk6Bz7yZze14iyaSXMMscxmvdQkOWZBPEDgPVcHl52q7LNDzcFI6mc5crv_lrQuCIqc77lmHrWoU92Qpb-KumC7uzMPcZJQsngzyPwtICvYyI3cWZgNsbbmSuCFQ4S3SAO3x8olzJT8tfgy5KBIy5kNn_kveUhx7FZbSFehPayI9AuwOsBb4L-hX3X0C5tGwapDwvbxJWgcP1cIZjrIWrHHAdaKeXV6CDP65Yq3NyNBpkDnGtJ8nAGzog0Ef17K0T12uR8ymwaqjm5-CP0ijhJX1qUr4bxnAL6BlkurUY6KR6bDJ9zczbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slngUmgYm87bXMcDutKEnmyWdZ3XcY3nk9Fp6QUNd6gV7fNnr2jXG1SbTFsr_G26MW7vHQvgNMFh-GVzErUW0v6_RXDYF7QC9KXJ8FkOHn7yBjK_mG_2RQ0fVHC1z-FjAeCDsgTKU3xQ0lFaw-bIh8cCxIYIibsJVyBhUKC52BT9URf5kqbLH8sgdhjxASL1Ekynx8SEjO1DoQr9Zbz7AzTbuNGaWgRbqQhP_uc8-JdciK05o7UR3u3YVOm-3vaH-4OES3KUcNT6BMFhEbCHTO8HlnUVWFgYFVSy63AgH5hYJuYFg5TxjNsS3dxtvwEbUkPqHTExoUNr9UmV2wnMYw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=gwW0KuataKUSfHSZ-2S68QsxLdG4-LJR84N-4cPFAYkW1tGrw9DPMcW-KvhcFiBaIwuKliKN_pn7PUnA6Y-SczJU1-daNRCanI5GWku0dSsgKLof0zq-rBAGiDbiuWjSvDGOq9BHl_MeayWb1Fg0nCakhwcUe94_lYT0n79nscK-b9uLksrguWrU9EtbjroGlK6XtpYKhFWxm_O-njF2EhR3nNHywA2eeYZ4AtK3Xy-bXTM3RVPNABqJjKjhPlKfuWRl96urtMg0lse2Boyff2QPTRbIim_Xp1dQuyqMD2r8OUpBFw_ypFT2dKJ_GYYBTel2GFobnqIjkzMOletNNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=gwW0KuataKUSfHSZ-2S68QsxLdG4-LJR84N-4cPFAYkW1tGrw9DPMcW-KvhcFiBaIwuKliKN_pn7PUnA6Y-SczJU1-daNRCanI5GWku0dSsgKLof0zq-rBAGiDbiuWjSvDGOq9BHl_MeayWb1Fg0nCakhwcUe94_lYT0n79nscK-b9uLksrguWrU9EtbjroGlK6XtpYKhFWxm_O-njF2EhR3nNHywA2eeYZ4AtK3Xy-bXTM3RVPNABqJjKjhPlKfuWRl96urtMg0lse2Boyff2QPTRbIim_Xp1dQuyqMD2r8OUpBFw_ypFT2dKJ_GYYBTel2GFobnqIjkzMOletNNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8M7adG7PiS7Ha8mwUL5RHHk24NH-aciP8IY0GOdw31EwUGKIOuUvQk_TcariFBTLl8cHBDzg4qcHL2UL0pC4KWkNNWjnPELvQefhep-AIcwS1e0Ty0cOOHUJs18T3-lfxNLYAJq3PcJx_-aWUduvFfa_2FTsoVrNzZBDIc1O_YDiyQ7DSqyuFQP46k8pi6IvvZnJo7MxZu6oJVPFenNLW3wL4pqCJrI1dtUtK6MR0VVUS1J2GMtK4D0UvaWEbW_1k3JCKr_pAS8qsZ_rzxFjHjEoN1-r4GLy1KBbZK_ncL9kClv1s3njxhijqjm6EboR-Zaq4iMw1AMkGkNYqkbjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=ugLMWg-FwW44LGJXEXSIX1cjCpK3zl2sopxg2CWMDvfp-51ve-JTBHhZdtR0UHMIxFxEChfD5tjdKJeqydbNrRnt_F9pvYRlWkVyp8AtrQW8jwOE62vFPC4orTRYiy1nkPKvo_XcYN47lXWZaG0YIe1MidAHII85Yd3V-Pbvn9qKygGJktwMP70IUKcMv4tmhBrn0Z2z64Kh6gv1wmxSJtOhdYyV5qLReFDo6JeUTKJri7VYJrTA-RP3CIgLrHdOyBK903uL7psksIqmD7Qstsm2EVM5NiTz_bvkx5zsdCMMWOShZT1XjUXvv6BqIGLhvJ8UL8mfk0wK93sJDqhjvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=ugLMWg-FwW44LGJXEXSIX1cjCpK3zl2sopxg2CWMDvfp-51ve-JTBHhZdtR0UHMIxFxEChfD5tjdKJeqydbNrRnt_F9pvYRlWkVyp8AtrQW8jwOE62vFPC4orTRYiy1nkPKvo_XcYN47lXWZaG0YIe1MidAHII85Yd3V-Pbvn9qKygGJktwMP70IUKcMv4tmhBrn0Z2z64Kh6gv1wmxSJtOhdYyV5qLReFDo6JeUTKJri7VYJrTA-RP3CIgLrHdOyBK903uL7psksIqmD7Qstsm2EVM5NiTz_bvkx5zsdCMMWOShZT1XjUXvv6BqIGLhvJ8UL8mfk0wK93sJDqhjvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=qPt3lqjMQzFLfugPA7yxzKiRp6s9QYl1jbSM5ryOQdcj2hhP5kM1KJbYaBWz5Du8kVVl5aCf-Oi8r0yifCgE0QNqG1qlWlPvTRs2kdprDDik-yUE_Ua4NQ0K7Zt94-pCikGMz_U5HIk8L8gbuHkWafdHwfop7tocUxMK2t8lmZK59bh10qKFnsx5vunEHCPwBZCAdUX_R7gIlqnl1vjkynO6o18GuAuBy6TKzckHIVFegLpUHvB0TbOjMmY0TOyvxOu8TlRqF8MIHZUJG7GcLpn8TaY4WIhb4kIZ6MTiD9kwmDs2xCv2wBa806nCnpyuPqoaAb5QNJzwhGT5szR85g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=qPt3lqjMQzFLfugPA7yxzKiRp6s9QYl1jbSM5ryOQdcj2hhP5kM1KJbYaBWz5Du8kVVl5aCf-Oi8r0yifCgE0QNqG1qlWlPvTRs2kdprDDik-yUE_Ua4NQ0K7Zt94-pCikGMz_U5HIk8L8gbuHkWafdHwfop7tocUxMK2t8lmZK59bh10qKFnsx5vunEHCPwBZCAdUX_R7gIlqnl1vjkynO6o18GuAuBy6TKzckHIVFegLpUHvB0TbOjMmY0TOyvxOu8TlRqF8MIHZUJG7GcLpn8TaY4WIhb4kIZ6MTiD9kwmDs2xCv2wBa806nCnpyuPqoaAb5QNJzwhGT5szR85g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvuPcFWFqf_5x0gea41M7Iwb8a-ihEKg8WcHUMlgzW37-92MyYh4DMvujtKxP7OjkbmVVoGLvoHwwGPY0WX668-vskl2DbDSSPPAHqb3GOjOvyr5iReXD5aYshuZmXgKX9nxp9lBcmiG1vUV42jCPdmu7L74SawrbuFBcJhUw1_NfLfXkzxZ9rnHAfe91RqB1lRTIz5DDDXMoi4jALxkj_Zs2-SPGFzsUebJ47GhE4LYJzJsdkEqkhD4UcLo7hfTO7upxcxC4OeB214xUVUz6cbHdCZlCIkXgMczbEjkZTaGOSDnuQHh6sHYTOSOhIeot526IXZHrl13C1djLFGRug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOUmDU81l-I9lANEp4Su5yRJbLQ_1vROsgtSwjVptLF3UulD41b1sN21bVkXLgpfQiuzekenTSCTJn9UjveFvjkinrMfeRPqgxsck2Y11-_105kPEeTW8B2EwKGoPX2raeTYPfg-Zi90gRU08jeeyI2VjDkdG1K36Ymo11aYBug0W1zJhq1tKFfnw4BhyXD5xfTFedAXs64PB0wq5v-AFX15pa9An7gYsaf8Obv9Jw1BzIxqBh4wtRE3joQWTzBexqN73UNgmHq3HMOwkCJEbLK_wOkwHq0EUrJ8UxZp2oALiInahbQHC5lr1Fm8n2JdwPPAUT__tXDq6egdQvCHTw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=VBCfbrQuZOdFf9FiwHYkwazyIIqOxw9QEIvPQv-5CegLzc9MET1jPs0rXkzHzXcheJlWkcEN5TnhuUTuxHneMjWheC6TLFdLV6w6x4zQnW6I9Sup0L73NJB-6Wfr17klTasgg5YzRBW8frAao7L_V2sbwC4zK-3rKkALu4AqHuyspupbkybMKJb0sxvdXadR_4vjjaMcvlRSJXDQS9qp2KTXctULXR-SiGlVrItHvjUGW4Wgy3j29EPC3u_HSIzyvXXQ3jJEtChb1uyxQa6VgxGhfQ2UMKjcjBz-nKyfe7zHZUiNYuk4G-Esh1vGbwFB3MX9i52TfIi6zw6Byashh0UeCb-u8wVYXNDXhK4v8vk2pM5HBvkeoVrvDvDzSoyIpT_3YZJ_JRjlMUVvEOOW4qkp0TwjWkq5YumUOyLy87KmMOB7Xl3vCrZwV-ccknDJ5ps9KPkvPmA-z4gjBXBRn-gGnH8HPfrm2WsFGV2NntLjKBlJPl-agYgIiuDfxZuzaTFOpY_5LwlMePILxzSAz4UiLZOF7LqvqYbIOOslID_AXbem-bCh8wp6RvTzpsJaIkZrMKFJoklPteqiwkdNDe1Dh7ZNfGzaQqlgk4TgH5_QmZIWtEVOyeECZpcjE6XcIQ8c4Dw2l-8Z62FPz-7rtOy6c25zg48U9gYDzEUPBps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=VBCfbrQuZOdFf9FiwHYkwazyIIqOxw9QEIvPQv-5CegLzc9MET1jPs0rXkzHzXcheJlWkcEN5TnhuUTuxHneMjWheC6TLFdLV6w6x4zQnW6I9Sup0L73NJB-6Wfr17klTasgg5YzRBW8frAao7L_V2sbwC4zK-3rKkALu4AqHuyspupbkybMKJb0sxvdXadR_4vjjaMcvlRSJXDQS9qp2KTXctULXR-SiGlVrItHvjUGW4Wgy3j29EPC3u_HSIzyvXXQ3jJEtChb1uyxQa6VgxGhfQ2UMKjcjBz-nKyfe7zHZUiNYuk4G-Esh1vGbwFB3MX9i52TfIi6zw6Byashh0UeCb-u8wVYXNDXhK4v8vk2pM5HBvkeoVrvDvDzSoyIpT_3YZJ_JRjlMUVvEOOW4qkp0TwjWkq5YumUOyLy87KmMOB7Xl3vCrZwV-ccknDJ5ps9KPkvPmA-z4gjBXBRn-gGnH8HPfrm2WsFGV2NntLjKBlJPl-agYgIiuDfxZuzaTFOpY_5LwlMePILxzSAz4UiLZOF7LqvqYbIOOslID_AXbem-bCh8wp6RvTzpsJaIkZrMKFJoklPteqiwkdNDe1Dh7ZNfGzaQqlgk4TgH5_QmZIWtEVOyeECZpcjE6XcIQ8c4Dw2l-8Z62FPz-7rtOy6c25zg48U9gYDzEUPBps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oh_OOEvuUXN2Gi7h4HZa83JCyDVnE0vNQ6NZZCZXA7z199SKUNfHNJJ-t0uNNWPPYEpUfo0ceq78cyliMTUNdh6ctZYt0AJS4xIUS5PqykyGux9zNhHzdWXZRP7RdKFtKW5tWpB6c665NWxpJXC1dG6gKLOJLn1bZ3b7zfGWMyd5pkveeH3ODpDddZMRBEutZgwqaxjIQz1eOA08TPXp6pfHMQqrlgPRtBFmLbol12JOCKIg2nuzE9tlPqLly0uZk-Exx9X5WxnZl1VH1PjAHpGQgghwEc_R5jdWxwapJTP-UWJh8LsRsgbJE6uAOS-HFzybzElX3Y5FgEX8YjYUkA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=f901BQfmcUGwcfitIOWQUEUcQmjjV5GmJnBUe46j4tIhswf8ONy1rlZnYpg5P897JD_eQti23uW3NtsV0tc_3P7aLROHoXLOg1DwfnJPEIOqhYz44RmagNf-QMCr6cKE2mmQa4t4k9x29zmWmkHMuoWzZx1qyrpQNZRCsDUj2H0M__yBIiklWPDxnAXJRYTfZEU-aWek7mH2eQ2lLgetJn_PCHK3s7PL5prgtP54OrW_pGVOUF7XJ8d66uXnkZ_EOSWZ8ulztLAwDdA3cY08t9aIhOMy8-Iph-roWnYXTWBjuut6MBB3lyILmSVLGdNl97_WrcV5L8sqB7nJlw9kqJtxeHB2WVxVcOfMMthnqO4uE3GrFYv5ppAH1vVmCghXfjNf3BZ6afl8dzknhEU3jmRAVsufXpiYUjKODabZg2FylSGDQFQ_9LDW4fZ-EPVQOakEAvwh1dHFrIOKqqXWYg4-sRz9pZrVB1CIOrwCnBH9n3NeuIR1nF7tgFQnvBNf4iZ1p35NrDAvnR-mbobHCfCFb2XL-rFQq7ll-qJ-ZSVrdZyoU5y6qOiXb23NzNE11IJVSB1tpXpGj4YIJ5IBMoRXT0MspRGKuyk-G7F7d3ZihZxRFxDZxPzkymg2Kj-ryXkd4UIRcCF6LLlMvIcmUAGEGgcV8-d3C52f5MSxVyU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=f901BQfmcUGwcfitIOWQUEUcQmjjV5GmJnBUe46j4tIhswf8ONy1rlZnYpg5P897JD_eQti23uW3NtsV0tc_3P7aLROHoXLOg1DwfnJPEIOqhYz44RmagNf-QMCr6cKE2mmQa4t4k9x29zmWmkHMuoWzZx1qyrpQNZRCsDUj2H0M__yBIiklWPDxnAXJRYTfZEU-aWek7mH2eQ2lLgetJn_PCHK3s7PL5prgtP54OrW_pGVOUF7XJ8d66uXnkZ_EOSWZ8ulztLAwDdA3cY08t9aIhOMy8-Iph-roWnYXTWBjuut6MBB3lyILmSVLGdNl97_WrcV5L8sqB7nJlw9kqJtxeHB2WVxVcOfMMthnqO4uE3GrFYv5ppAH1vVmCghXfjNf3BZ6afl8dzknhEU3jmRAVsufXpiYUjKODabZg2FylSGDQFQ_9LDW4fZ-EPVQOakEAvwh1dHFrIOKqqXWYg4-sRz9pZrVB1CIOrwCnBH9n3NeuIR1nF7tgFQnvBNf4iZ1p35NrDAvnR-mbobHCfCFb2XL-rFQq7ll-qJ-ZSVrdZyoU5y6qOiXb23NzNE11IJVSB1tpXpGj4YIJ5IBMoRXT0MspRGKuyk-G7F7d3ZihZxRFxDZxPzkymg2Kj-ryXkd4UIRcCF6LLlMvIcmUAGEGgcV8-d3C52f5MSxVyU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezIzH8JhqLZo-gD9EfhYkhwmKi19SS3fjDTzZrBbw9-CQGQvFVa1aYd5Gs4JcD_LBCmftaP3PabXQaMYEEj2w52M9Xf4A9YCGgtVCI-G-Sw26ONA6ASevm4A7cbDRE06-rDf-ktG2kJx73unFzokEwqs8YIsxHWykUemJ4hgHGj1W_eKshpI-NzoWBfvmr34kmJrtx_0qFS66tZpnVMuetK21mX4BgVeeTtRJx2l_mAs4fwknYEq50dT43UP-5UgM8dYnbAXJruCmbYH9B5b3ajxie-P4YYnQRRMIh8_kf02d117bYrUNnzFrQ6oxO9mPNDIAmGVW4blHKWdBsD9vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6RdmV1zbSV_NZ1mSDTVGepKsCSfmVg4QKVzdJ-fnSB13xf6Xw9qsqGjW6Y_8bg-duD5c1WzRfMSamc2BjRc3IudmbfeTr04taojlCuYdRZ0ML6bK0UieS_qVqUjlMLcAlkD6C_nzaXD9WZdVzNph8HfQI_6FUnZaXfjXDtg5GcTdTE7xTiW29eu_LZRNgbZK6vsF0l5S_fkVU0tewGgwqgB-y0tLJEUuUkrg5NZwwmP_A5Tl0Y-majlbCjBhxXUlWYdbFXypgr_2SG08uXqkfMgh7bG5sDKJn7obNC6LG_MGcx0hNgZbIXE5DFlNKgzWdcnATLuhNtRgOYv3IcrSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAfc0IwD5rvFeqVaMpAJgK90nhSGsK5QRyKW0wnitwWll9Ep_xu17XU3qijavfpcQt4lw_BXzQL690Lon5xmwoNBgvbP1UPc77FzC2qVeMhh-lq6JxHDZwo6DKCHLt8MLPoRz9KnJJfoYcUZ7RHYsaULPKUA3jpL7dpFXOWKEsBiAGiHOEArXAdhYfdhoSiupDa3nNS1O8cgQd12UfE6Hm7xg6usaZvpg0gf0A-w2r9wiY4B1pc_2TDbQ3V0XPtGE0i26_G-acfdsASXROpVzrTUYNEqPTCBHBUmc4yJaUTpsXohYxA4QMPmx1-GkglCzYTwTBExMoIjwgG59a00ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRe4uB6C0ik5IENLlUVl3GxR5iMWoBbAZ2abgza_dbc8GB4zBvP8n1ZBswMFxMSbwARXleH7qnqlpdU27vyrwY1z5j02hfvRoCbTurJJFhFgSLyk5kkK0agMm9Xe0drAeOuDILBQF1AD6ki6If8_Jij868T2ujM-OfnxQVRWetATHp6j-UdCGt3JM7RmXE0fy-4jNeCmgDkUP_Z53g_nMB90rnEiCGSAdxoqflKYs_8jefouR8rf5jmkRXGpRYZtiQfiesjdpY-w2L9mP7X0dxavqzzpfXwKliKpHkA6WZk0n0D6439F3WvRhXolpcvnjIrviqMJBKAHbai35GAg8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3gR_8cp8yP4pJGAiKt8FtsOBcdsIWFgCnJEWX4EgMK_saNGUyzBvh5oPYf0jmD1v-bK4ao4Pd5gnA23yzeNx_N7KNdwGRTbFcn4oJ0HAXGag3Qhx4BMkuhUlf87_es5MYgaP6FkDfJO84h5Pt9KO5aw7IVbsvouKQGfrW7vNBHbQC_0wfQGnyQJrE5FWedTYjDb1haVmXLmsE84vJCcPuYXW6orXAD764IVAcepAXm-T5-kRR09MPRZPUP3na5ZD-ex7OFdPWj1SVD_-X5Rhkv1rvzU8K25ie7X3dLvCp7cVJWl6q2x1p4eI5EdnLQP-W9RhlzRKqehFkAGPgqPtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kahl0YOLj6kpYnv5wiB8It16unwa3Uxr2sE9JwSbiYHQ1pDUm9nA1HXBh306FCdNerE5_t9kS0hghYrAvbRI3RnEoM1AMBWGEJP9Bg-MEcuA5RlsJtyXtFiC--YUZoY1IYFZSb5GrctiOfZKVuhqGc1Vp2OzhgxyR2Fh65Ef-FzDoeP9JYAHv5z7WYbv1VaInSBbooLkVADFC6Fjn7Jdn0zXx1sdZJNS5y6GiPOmj0LQ-OxobSmOhNPvt_a7-Rp5cfHRkdpFd5Iq8gBFflgKUfRRjHJuK0DLPwa4WbtBgNjmGjfOATqLvCBjlZ_E5t80IrifwLG6zOOkWHBDGxoJjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3bg8aUsc5rdVJJwQijNEqaVxyYl8aoCfVT7sJ-tdQBG4L26_Wc1l5XM1MEhw7G2KMcvAUT3P51BZXVdoxeGkdOyTIYbCHyOxE_pfQtMUZayDUvfgAE2FBNtA6vdCglYokQn_8-YEZQM0chgstUpYSWVq9QHXKXZII3R27IVFfpdEDXSPx4tMrA6uSny-rWgqmIBkuB5u65Aw3MEY5uCGi-Kc3315sX1I5GvOHlvhloxDAmXB3ITfwgFkllNXc_QtPPVvd0x6zYyHphNZL6Tux7ih5sDVZVpzk3v4leBHg2W-UCCP4L1nO8UjmD_TnlAHWSOx1h8t4xDo2qcTqhDHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVE43r9s_ScrfuDrxb3wWKzdgWNP1GHK2AK0aDhsfE63D8svPDjrUE9o5ILRpimTUE6-0M1s7seBeeidt42g8WcKCak4Wt5GvHtrk6_HXM-lnWrJXwdWQzX3WGyWNiGQfc1-1rwbFvNY3IrdoFYXm00sdP7HgOu82XRSYufd_jovrpYA3EpWNKRpUmjb2anRzBOLQaw0rabz0jkwE6FVtlzSeVBmX6kpsA5JIB3E3re3UzzpF_THzaO0MrxQmdVReR4Ewqv-OHyFXecQFvx0GMoL6DOHKv51HCaIreFBlv4LhNaC_FuK7cSaUynt7irHWJbmhJCqmk8KBPSW79t8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piw0ku3ZjO0uhJMeSGc3L_Qo6fa9pMLhxCIVB7_o2Vnwn7XYtGOdAVC0tNCBZFwJSfKy6BPa_7gh0oebZThO-hSaFJysqLFR_bnkTNW4Rul4G9t4dvFYB-nlvtvJqY3RuUlffifgY-wLWqiBttwYEgRqKUo32BxKKqzSxXtu61kk9uaI-CEa-4AenkdPmZXKOP1S3AZxgH0mL3LdvczChn70aGdmZOup3aphhWqVjU9pEiXdFvTGQEnfzCGZ0joJaq1DV3gB8gXkPT1EXPz3O5Cdcdj05YMYCu48tUq0SZhoaNkRaNWwOU6WJKzU4T8SfNO6m9s0W-Qjj-JF9C7IVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNWvQkX_Yha0iHgIotmE4xyI3mH0FzkBuSYp9nM4UHZHqETZVs2wMrzNDALFPrFOu0wf8h_gYUsUJJyt51ByCAJDGihgAsPMz6lqh0tkGkSJLZ3taBlCDGIzvELGqp3mrGALpVK9GKhCmbomv1ykpvNgsifSwgTOh4n3_SgvqfFEkVztNYT_qUxeiesXzs8VxXuAtANYpWtDGAsyNCqHEzUUgLTHshnAM6Gpritm19mTHEhe_KJIQL-mFKTUnPSW0Uu535yU-II5gE_cmkXthRLoXLemJSycxKZn420tnCzeTGpD1ODI2jbqW67RZ50SdLh1LbIgqhRLR66hQrEPLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqkvuP_afXuilKqx-JZWfpCrdvljoJQ8i0QkEY-Xl-bHoeoI7OmVJdmCAjSD7F8TB-qJfmppFKA43PD3ERHOFiLqIzGLjYTDGyNK709mnwOx6rJBMbPE-s4YsYWxo2b-b67_3xg-lO6jfIe7LlW5AvRZHvyihT4acBp652D_0ZcON-Yllv5oKOtSTmgC_Ri53rMfTseqPMd1fFtUIkyRaUstgy9XQs6wIRvnVBBO0IcX008sde5iUFYNvZ-3nbpYiekkrWV0LNyIURmxSghsFsC5NKzePyUKG9vsZKf_-KULIJbgVHrDVxx9bN6uQ3qdz6D5ecC0af0HtWvW9srR2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eihNicadkPnody4zgdg0t7EfcViazvpWjtFXlqdnoPcnm9E1pwGF1ZFJnGm9QSPD7JOOKwMVAVTL5gdkqv1XRTJChKSmDvmONY6yflh_Ym7IYnA_qlGSYm95gz3LL51IVwCogPBssn_RaYHqf-2ZY6Ijz5f7a2fNEbSdXdJk88ewW1z-fyZVaBRmyux-bSS1ZqX1kJAt-eEgfb22QgQ4E5scgifT8OYw_KS7i8jZoIb1bsDXm9qbuYyveIAZyceMTsU1a7-zdZ83IasMns1rrLa85FAr6UJ8eDhYjNOLaHHzTvfz772ffNIBYG_R2hF6xyKrbRM1ifgJmR6vqiqNEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-I_Q_M9QyX7e8ewfWMUrKq1t4Rwu8S97FbgO7mxUP1tbZ8Yt84lj4mfT5TL11YUvCdQ1QWVbasvHOeAF9KxObtNYer6cIphgCwaSKP-oVMcVWvu8peS1XwMiyw54HJ4rAEUPPA05Fm3tA8AKfzFoU9RNbideuCYBdhyUNhismoFMJ0U7Mhsv0xBNFyM2zZ_AKq5VPhsxAujVtrmqTy1sgavfQYdl7zGfLpHD3MKgdULJU-3zn3XQf6s-xE4YgrvlFPcX3p7JBFBHFVafQdc2Bn4JnjcbzcVlVUv3S5gJ9qGbQw-UWiN21ZESiu9peE-XI1DaYdEvvtpy-7zOOLqCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lh3vwQ4Ngx9k8RWmQg293i6i-gC795RUGt3_OoLxGeacm4Y8FJXGdPae67UZZbHgCs0IU6aaaNKZWIGWgqAF8tCtwz4WwoY1mhUeiz9CpxV4x9ubE92n6hl4uQyQWXMatEuDPswI_jmiUCVGdoTXVwzYHEBYJrqnYgz7N__HeStf_Pnliw_SxqqC8XHK6GF8jz5msetImM_NRjA4Iq_ceglX8D31K-nr-LhohLdfPVXHa8A1fn9dlegqBKPVhftvF6RjEdKif-poZYE_GQoXbzasoZVUmD2OxZ3XBqtc8D-9D1owD3tzN-b4cN5ki6AVrtTTx8CR35uU4vfIyDhQUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gw65kKVGeaM7NgaQ0sgDd4aoPU-BBP-cZjNkFbYuSnr4UYEEm1G_-ATweC_yaCv_E2vBqZ5w6sP8nQCAcAbKr5MVFeRGmxFoYTNakF898eEJAlR7cxa10ihyKIlpVd892V3ROLef43-4qjXBfhtynBgtKPWIl1f3l9p7oGyEmKyyvqJ_eBni9aAVlkn8bkSCGvTX1T2ydKuNXOJMi4ALnxQFU-zFP33Qg2-cNhEDymasKPyYtXbZIGb51I_1l3NBpRxHokfgbnbMwz-wf_ofQqpq3QXdqGktP54Til48Syq8SoyMj1SCFOiPfO6BEqZbrJ3hQYvvzIkwr6aVZTjYwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qe0v-wLCcjAzRrVoi1PfMF72WvwgNZQVn4T2WX3YXdSLU1chj_rOTg3Du-8WTN5ADnd1S2HmrDSMvbmhBY7z5vc2MGbnZNdr4QWaMyLM7d15DiuqtcTwB_SFiEa5n7-tDW_JczNiDFeEJi7wCbfiLguGcoHodQsrc_SIwiXwoUCm4z0lPPIMbDX9svplyIyAhevJLcdfNs7RoMKJCVpRiR8h-1E6RQ50YDWOm2eARv5kz9PAXgRTTDv494Y4gxcgLSghsGvPl-7Kgp6Io-R7sAVRAUyA4rOwlosP-pYPi3gwbEyGj6Z7PoQoI75YzXyYfcD6zVWOnH-wmgEZGlFG1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sSU1trDwr85gxZGEyb9PFgYHu94Oi4PmgUmhpSMp6eUDjy3nk6weA82dViYj6qWS8KHE6zawnK0si3m4M4UHoM7S0xpbJKr3j64aZtakFFDd5hPwezjQ1JbmaDkKGPdLvz8ZXptBRF6N1I4eLd2slnYEamm7ZhXbYtEbJtX42GH6-ZLPg648q0P8qu9x0BsfILdpbG-klpO5Xjg84YiQtJ9iUeUIhvowSWW_MzqM4CsEWyJUSis97QSTRCkfhoSzVWssuFgdxAXe9ouQRl975zy4D_4q033oWiJ3t6XRt_MrjoP1rGXwm3YKLSFIXN8B36M3te8paOEMP45GYG5IOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifoIQnIqjKzrb5ZUZgak7Aya_NdfzVf5EHq7FJgDlBPHj7noqhuKiElSoBSDPreaUcSA9wEkO5eumAFp_9FGNzpJaePHRuCKdZ55flMbY16ovbb_lB_YrGGo_qA3sggFT9PUO4n6y0VcyAZWzMOs_TTrFUS-tu3eVMHfLFPfHCp9M5UMhtXURwqpvNG1Jn5tU2zTJbGQdj-jr-VroWaQi81ieUkohT6yo3-jqUZDXbpe5GdUz8W-12iIydfS7sv6b4rrOb2RmVxqCZElkc96iH2Ea7x855cmpD4FuAjyEHlivp111-yO_ktuULxoa8WxZDbQvRHtAmhGVayC-zM05g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrESVVqFRar-ULUnry4p3IOsKA_YOMnGaHai-jWH5ZYvl32li79IKeAluaVaBVzzvUnpUcyJ5PrWAMOvxkHzSgcT_EhfJPEjlz7ajwZ99itf7es5KbyIeRfIx3G_gitVhu8hvA_BTRtlWmdlQ708_-JMGJHAJJC2lv1zbWCZYYUTQYx6ih6wZfcwUu4N8YlPLllUibqiIyR3Zn0A61tIRb1sSgNBsHOaN90K_JSi4GGkuhhx4qRfxbPNwA1_95z46_d3E1JEvxGdnYQPjJUdGBvcIlSXnZ9JxR4gan-m6OaARoenP1vYEQISEqB5Z8IrjsJT2MX3JJ8rOU5YfQ8UEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKaWu_N7tSw0yRYfDqpXOLbG0SN0Uc0lI2DBnsWZkfs3ebYXPes2j_tP_NJ7k2LIvJw6m7zQT4B2hwL9hJkB1SDFaSWTkG9bEov6Rugjv_EGCEL-kTxR8Ztf2PJcDn9JfgIvBHZb9aiaUFHKCb-1WtIA2pufTjPdizxbSs28G-sBBnsQrq8JXG9zuv30XRqchGgpiQwaZzCNPz3c17HJAHB5T-RnmTi_A5U9Ahd4vM1kb4bph3GLtdXMDXBzbc7vLOLMQLKoi9N6XlF-xvj26veZpn-G354-A6RAoXBsMi7EYQc-Rumvp_nkoD-92mPT5OsT1mgnNAwS9ttNgKYSKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFHbmD0H-pAn_LqFXedFB3hphnvQ7kdIk-9BiHzscGY_9Dxs5sZgcAw-ZsWW7RPEXYlPshNDIateJztxpasdye9wfVDexqKocvOx10YrWAFQ-tAZMkB2RAWfDyi2AmnubuQ0NgZ0jZ-8iXg0pY-TMU6J34PNUPqYOFSGWHkXZP27jwgD2uTFwavTsUcCVdgP28xRfe3tBLE0h4CjOc0BHbHasaOd28d8hzbrBjOwsR88IhfQvc4ZWYg65Faf-raWbk8jJHImF6LUqT1tq1KCzOYxfl-7nMZQGGDdmxRWNrIS46KXqh1tmbHwctmPESiMkCiiKawW4T16Nlm7ZIZ50A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGhHHU_oqsaCHvnuFApuhhIx8ixFhHlJg_hv276S9LO3NdA3KZI5l1aYI-LPVsLVtJpS-LE4ywphbkUM2Jk3pe5nhuUyQ0V-5cB8mcMpsMAZTxLGLuanLtXNa-MgpOg9oDweUncOOX2YxWpQLoqLTxVPPfGUyeIFBDv4tV5b3fyjmpRcbepa-YdOROmcfnnpfbg11_wPwrU-7Vq6yuGmKv1I0hKkZfc3g-tUoWZyWskmXbsYCWnEMpN7yrl8hc6NeCtCpJi91XmVsOwrkr2AxZzBYGwYIaV4bw6fxlaym6hzn1ivFR2cEGINUOqXv3vZKM_L_HMjh_YP4r94rYkyyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSVGPJoEYdGe2x02drpXwm083RCPTPhDlHdwfnK7CQSmrlEebY7UqW_ry3atcfYcBJM9uTVaXY__sZrlGFNEawe9Helsb9-OD_tZg7uofDT1hPBY8B1LvCCHz_seASuJZUus1cXpn4iMuZj_wzPFooDJ6B1V84rLK5dB5GeuJsT0guTvKMdYnn_6jXjEEDfaehz9JMdVOEHX8UT_3hkAPQEYyucqQDB3SRnM8QfhTaHInPvLnSQTD0p2jhkVhA3amwZwwpTYsshpWz4vdpD8zGrYjmdm6H1EtQyX_UcooP6IOQ4Ygah-ZAY9AlnroMHXAMEomn1FWmp6f-HR1lg-tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTTPDkLKDWawqX-uohSqNw2zChDZlHPM-0gJZw8DpMjt-Ls-jevlAOlJrCe7jT-GgorkMCNOK-EpswVf1hK7JsPZ48osTmieLZrqqVuAWhBPex3kQvk4Y_VtQLN_k2S9V5iAuVT7EDwRoJ2-AU4GhFZnVIfQ89qZu79RKPsbOWMyplzLQxEMDUu9Y-NYL3np3GxlvjPX7n66U2DQPM79Bs8TGRnyl52IDKKG4H_hYsbMQXt5BVRtwW-6gYRR0ekbV7x1mKFUvqGtfmVgRl8qy7XUksHmaAxGhMlcazk_-TYQOvQ_iEu2mNQDDu5DLcdbkYShYw5nn4PXG0Nb2hnVWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODBuDcCqNot1ZQf_vEE48tHk-9HGCPqsn-Tbx_AVwhtpa5FhDRV_UjWa6tesYpxeZVMwheRvK0c9R8q6NAtfsHFFQH7rM_s_Ktejh6FJsXKYau_7MtaXj_6QO4kW8SIA0OlAvnXA6y0-W7bt9JuCZ0GjyKxnsM82WqwE9XasZddprD6zv8CwRPAS14sqa5qOn7yEPSh3_ak_slj6AsRlaOpcMsqF3cyy8JAMhEpzbzzmmVVaM1wAz1nsiLN5lSB3WNQydz5v0GlPlDPZwN98_2cjIGcCW2sw4TnHBEUTi65qR0wIVCPYNVSrtOjJZzNuqxvuXJ5IbWBATSau5KfqMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qmgnnyq_2unwFevOPPgzayx03aefHZmt_ctO7pPBfWqKkn5vBzi45NPwvhhKoevMQtdD8F7gMwREfkcBOe_LiON13ioccu-LgfHMdNvXGrtsZrXcJfj-YK8PS93-PA01TxF2Yh9h9owEF2saEGJ1kYDU5TtI59G3uTLjXAP9kdcYMKwaE29n5tkdnp-9hJhjg7MufZcN4D7S6eNQmbTI1BXM-nErAjOhG0F5Bgx8cXGTwQYeyTsyRy2uVENPIXMK1T3WZYUyjEUWmfRzXuMOWIcU7VvkRh5iPvK7kQTLz5Vm6OzyIX2RrKP644Xkm1f_LlI_S-7tEnPjaLruYpBHNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khpzV5D2LnsC2JFokB-eXulq0DZJG4AVNdJAJKHjGOSDx-IhP3wwNVNnKs627YkLwPryguMWizAz9_g9Op9AaFXxqR3nO4dAQJj8_JgoQ5KhbzIWr75Y7lkf1tabHTdFxNUzC6QsN5oN94agYrImGn-DVs2Lww1F7MVW9PPsH1DkD0UahSvp7vX2ta0uzH3Vv6_fBXBPr1EmMp8e6Wsb4p5_W76OO9dnbya5frPNX00XEWMYU7bDOOuJHPBaPXZOQSXfwxyIPnH5zJdIdLyPf3Oz0AHWp4sD0fH09R6nJZzV1lKR3yLebdBj0wn1IP7K9ei2iStc2F-jQNTUBYjW8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cp9TW1nnXQLjdF9TyFl2-I-nEieS1e8bQbDDNyL5oIaxWYxvsCxhNLPLjW8Q91GWpsNToBBY139uBnh4DgJ0KAIHcTlJ2ZMVzIXNOrGU_GGtRQwCyoBkMNi5yjW48PwgAlgDAYvDd1cLAnEqcQM5EO0v7hrOQMhW1QjmITGy883CK4311HRqqTSvfzcX4d9O6QJPRE5_Xv9L0aqkl4xp3oN4w9G90LA2nY7mSvhg7CfRXjES0Pb1EVgVK6RoyqmpwHFJi9KpAEGgUzlLwuw2lrLmGelwQRGehXVBP0I1sQwt7mtcHtmKq8ogr2hM6pdLUVDCSvAWwQoIUQRczMFsww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
