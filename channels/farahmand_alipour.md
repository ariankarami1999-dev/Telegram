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
<img src="https://cdn4.telesco.pe/file/Ut2tKv10D-UzHtgIpZTdt-yXEp1lhnNfejKVdAgjEXz2uh2P6-etHEUyEXCMpCQirfZJvd3vVMB8kS_2UAv9uZtNulbJSxwH9s5RqNWDlrKj2QvpDNCHs69v3F-OtgrUghM39S-aWj3l7o5IOeLuFDUzy0pvMFmcTjcWl0-6SY9G0gIAZIt4z839FSa4vxaJQYwSi6lqBRB6-QflxvAAzyM4BCiogUjLFSBd_RdQFSnzIODOwBAkchvfTwg24kyT_r1BxGV-xH-mgoJAFJMEK-CLIHXDcpjUAwn9xkhODCMEApbfPSYwAKYkXUBnqmICAKiNNkM96AMo6YR6eh7oWw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 00:05:49</div>
<hr>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qLKf4u-ybnrlTBuSlyp8n0zBvrUQ7Esr9i28xdAllGpAuu2mg3cB0_xzI51F3goxI1kgJ2thsfSa6ALG2sBOCYA0K-IdtJMLrkJWoXcRN9KqQhozkIJocPrFKSCHys25TyN5x7HcViQjAb9K-RvDegdsyr_z4YDBW8mhf81k4j9YTUVVQSoZuij001JbniJyPjpJnFajyqksJZjopGbxpjOr_24S7gX0LGK3huLBVT0wjmFCJw9k8x3caeG6TbfSU0UQ4-7HkdP5FKTvS6_uFFzCAoGe_I-WgdN3Y2GoVjPymuQ4io5MNJrJaDtxyxmrurFHVrsu3bPxpCLc8b0UEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYnNukPmxeRiLcb0uSpzyZoHGqlsPKdRiaC4TW-wptsxY48TIcneX8zG7hj5jxnCYmViipR1i0WaYBddfuSM4IdSfoONE6HpgXCwOZLSkmzQv7sBLkmkyd-gucAIiPqZOF7e6KUNNE4e9JXTEE1UyvZAlpn4x2sLwpxmPkUHfHs9jpYcMmZA1AP7zAB97ljLLSNohPr7QxHwzJvdm57Beg5MtI8FgNDbHHOQVLXkCrBTEUKExQI-RRXZgZamCnzy2lJpWEdOCorunqdXdOrF3b1Xff8ANalc1gLIBApb-AdKuLW_S9SjKv9P6cJ0HDA-ZAcih6m0fMoNf6IsiQEpNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEPvNPKmo3Y3Dh-7BN3AfgbMYIpaxh6BhM89BiSaGPhhVVYRt-VswWkRfURY6IhG_eWCcfc7Zj2Kg8TW1k27pT3GJ4gF4oZGC7hrxaQGx5-xK1ZZQz7SOl_Cjcb7QI0Und_ThoDCp_ebmGuuWyejZnlFjxjLEDrFwiK7oXYEwh2X6jHQWdNqwN0Pner-oBAXEgwFlCvti9tWRGbckm5KAMNmlhMiLbXjPQLgk7N3Vm2VX6AsyLvsPGApgNg6VoqGd1gNRL1iafTgiS4x_ogGWXXNUq3DepMx1DfvUdNHQFbvCjivhexaZ93_GkLST0r-xMZtPHfccYOT22sZE3ynPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbjp-PRdcEWORyoBfNoYsRDrz0vP-rOqtOJmksVDE4lDrV29CQGpO5Qg9EtsZrVfHafO9Zcdw3MTbGiaGjAWjBiAU-m2y11BliuHFPNOxrABUSp1EFP3BdNEzTZuO5bmrsSgwcNvHyOOiaHKieX_w3WJfEpE26zzjh08wjF8SaeNRDN-0vuDkNQ-FkphK_MxSXZ1qFEB7uL2Sa5odvQQxtKGmptzYGb1G7BFxYiDliDK7dgHEADwPNtMOootKMvM2qgtPxEs1OyHuEFiODy900Tya957WDph_MgJaAAPDKTvzORzPHTq16KV-AdsiIcRqnOgGc_l8NXRt8Fa4OijxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qz71eOvpwmWscgntpRQ4INwXrXc57EFgb_SDMIcd4MRC49wQ_C4beG8wCsCBnvpKukaDqv-bmFfPkEg5UWWlDl2kjNLK_J6qjvRUo8qqYHfKxh4XF43JL2hI0KFnk-RB8OWhpqFcK1mspXkiVeeE7j15HJQXW8CBSv5bUkakADafMzbMQIu2hQYhxBFFF2vaBit9wa_d3qYSYbxyuCf0lj8OrTOdu-NT2vlnp9nBvXoBzfqaV92JhFqmdizItXaJ44sYMV6pHK1SohHXMlKpbCRVNqsKKbV5BvWFW8ZyHV8yU4uei_BXxyYQtMKt6Y7hVSRB6ZCkN3N_4sjE0yXhjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=dANZo35FaRrJ1oY0yFi1MUAw79B9wq1TBw0yVk87Kq2oCXJyaTU1iLTo2usqzgLhM_ylvqUFgl04GRfgWItg2IOOquAQCbUXsbolBGRy2lCMEvdMOwCNlk7ajOzY0KVq0M7eZtqnmNDekoXYg-H62yVpkFDXvdVAWwYxd6lN0Dwr7zzwDZrZpnLHJc5dxLpOb6n1i8IfPF2Op9irz0u5CF_uXXjaDlG0RsiUh_PjLzg3Ybi74fWdpBDdRDCZR9ZQ0d-fjUwCWdJnWGcDLZc1vJTglIcaLQmEvgGq0tdgHrAAy_0VeJOXIU2vuduLe_br0cwkEZNAhtIxzayLpvSlFIorcajlQieJOBFKun76bSvk3mi7xj2Kw3RW54Uj8wb3J7wbD7iqjksvWpAgqdCPVAtGnaBbxE2h1sexeXVuHLfDfMAPjpkPoJbEzSlys6IE1gVmFWkG50y8WWaqwQukRf2I3-ibmzR4Kc0aB-MoO031t1GA6FY7_MDZ0trn-NiahdkS2EZwjPLkeVkRhI9sU0FohNl2q-SPwa9fYKdKTroubJTpcpO-_TOdkiYhyES0sPZ9-BkAeU-rAdffPYVhn99a1e_-nS8E6AjVV8ZJtNcGG631L5_wldG8dQHPKc3dSOkeb_482o8D10-GFwFy2PxJWR1lioYCKAQT7HXtRpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=dANZo35FaRrJ1oY0yFi1MUAw79B9wq1TBw0yVk87Kq2oCXJyaTU1iLTo2usqzgLhM_ylvqUFgl04GRfgWItg2IOOquAQCbUXsbolBGRy2lCMEvdMOwCNlk7ajOzY0KVq0M7eZtqnmNDekoXYg-H62yVpkFDXvdVAWwYxd6lN0Dwr7zzwDZrZpnLHJc5dxLpOb6n1i8IfPF2Op9irz0u5CF_uXXjaDlG0RsiUh_PjLzg3Ybi74fWdpBDdRDCZR9ZQ0d-fjUwCWdJnWGcDLZc1vJTglIcaLQmEvgGq0tdgHrAAy_0VeJOXIU2vuduLe_br0cwkEZNAhtIxzayLpvSlFIorcajlQieJOBFKun76bSvk3mi7xj2Kw3RW54Uj8wb3J7wbD7iqjksvWpAgqdCPVAtGnaBbxE2h1sexeXVuHLfDfMAPjpkPoJbEzSlys6IE1gVmFWkG50y8WWaqwQukRf2I3-ibmzR4Kc0aB-MoO031t1GA6FY7_MDZ0trn-NiahdkS2EZwjPLkeVkRhI9sU0FohNl2q-SPwa9fYKdKTroubJTpcpO-_TOdkiYhyES0sPZ9-BkAeU-rAdffPYVhn99a1e_-nS8E6AjVV8ZJtNcGG631L5_wldG8dQHPKc3dSOkeb_482o8D10-GFwFy2PxJWR1lioYCKAQT7HXtRpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=vAo_ECIZv96WRFDtIvDJjwTAVTDDwkQ_10Ky5s6msziy7lwtzOAYlHjtnmpPPxb86Oe_xBs8q9Ynx-c4QkvIKWeLfOQZe4AMDFhnvkpPE9RkIBsShHftB55mnW01Na44-HyhxUFY2vwFckAAaA9d230pA-8orB6N9N41QdYKenpaOWDBA9jcJXh92JfTkOHPcm7aV8gtN4BOhlPNrwzdxGQjYFb88gUxbHeLj6i_SLMR7R4psYFqV5d3eaA_5ppaImqe-xt9wzLgqUhbZXy-D30M2es6hh-kjhpvwbgS8AvSRXZjjxPPbUNADCEW9R8dJYJ0ONBJZy12xrubGtPlBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=vAo_ECIZv96WRFDtIvDJjwTAVTDDwkQ_10Ky5s6msziy7lwtzOAYlHjtnmpPPxb86Oe_xBs8q9Ynx-c4QkvIKWeLfOQZe4AMDFhnvkpPE9RkIBsShHftB55mnW01Na44-HyhxUFY2vwFckAAaA9d230pA-8orB6N9N41QdYKenpaOWDBA9jcJXh92JfTkOHPcm7aV8gtN4BOhlPNrwzdxGQjYFb88gUxbHeLj6i_SLMR7R4psYFqV5d3eaA_5ppaImqe-xt9wzLgqUhbZXy-D30M2es6hh-kjhpvwbgS8AvSRXZjjxPPbUNADCEW9R8dJYJ0ONBJZy12xrubGtPlBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szdW39AOqUPaWZYeUizdKIjcPhc04Ms5b_zNT-90XyPh2tCvnaSDC-kcSCyKcF1lgfUO9WW9iYpXOFJat7grr_oMgTVqXcR7472mJNXW61zYuu_MPiL8mRWsKSJNtELYzXrliEQTwB9Mmd5RoDiHBU-nV2TGkciek-UjspGuHZBxsdJU4pn0g1eMVB_HitDMP0o68-bt_4FPCMHGSSe0BJ3CpFe1s4KGnFO6tlGSaqcXagb2jml3BpNqUSfYAUduJfrU4-HSn8daURiBrN2eMnehOiOOhXW1hUSVRUANB6JIKpMFokbzhyE09gMQZoiUCCLWGTjVPt5zvcfjB_6jKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=fVL-Q0YgiYAIB7NATVS0D85pmKECNJxpAJu1dGSdiYS-vmRKBHL29I13Y5sKuuQP-vbAOzk6cctmo1GHyOe9uy8Axo5uVFB5XAhLdyLg7h1LB0ceOoQtEhbc_7p1oGKMQVzDP9eZcZ3zhDM9gwDlH2AI8qvO8FyopxnWZG_6Eiol3kF_8zfDX6zVTnBFJpPzGrT9BZNqY62VLwSzt_9wiFoBTMxH_HzP-k53TozUHD42vU_WS0SffZ0eJtbkmp-Onyd-mbn3O1z5eHyT034AqC4yJhyDgACYxEJDK-7tQTgrkp6S7_0risOlM0Yd-eNr0yd3pfYmh6cQ5PKonUMb2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=fVL-Q0YgiYAIB7NATVS0D85pmKECNJxpAJu1dGSdiYS-vmRKBHL29I13Y5sKuuQP-vbAOzk6cctmo1GHyOe9uy8Axo5uVFB5XAhLdyLg7h1LB0ceOoQtEhbc_7p1oGKMQVzDP9eZcZ3zhDM9gwDlH2AI8qvO8FyopxnWZG_6Eiol3kF_8zfDX6zVTnBFJpPzGrT9BZNqY62VLwSzt_9wiFoBTMxH_HzP-k53TozUHD42vU_WS0SffZ0eJtbkmp-Onyd-mbn3O1z5eHyT034AqC4yJhyDgACYxEJDK-7tQTgrkp6S7_0risOlM0Yd-eNr0yd3pfYmh6cQ5PKonUMb2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=j47IPDJQtkDlCjzPAfNGWkPkhluOnE0I29OEFbh-iNnKXfjaByYCYpP9uqe8CN_MiO8FQbG-r_C2rmRsJQYCKpFTANmfNs_QQ_3rABof-WmeagHPBSy1IHwAdRWPPqJJ-xDUdYF1clVRgTxtHNpnpWBQZBX7ZwY8q2YKUYp6nLfRE4vHB0KggK6-LZl0bm8UGxBZpUKwvfHdmj-6vtjhS0T8g9KFSJmJ9X1GHOTcAtCBtEPH5lJyUpFNBYZJEfJRD2M9Yol2McBXS6GR698AAJIp2ESwwkOpSH-jiZGTl4487MiBMIoHKLvn2Yqnc8QbQRjfJ3zQNjhzrxqaHJsH8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=j47IPDJQtkDlCjzPAfNGWkPkhluOnE0I29OEFbh-iNnKXfjaByYCYpP9uqe8CN_MiO8FQbG-r_C2rmRsJQYCKpFTANmfNs_QQ_3rABof-WmeagHPBSy1IHwAdRWPPqJJ-xDUdYF1clVRgTxtHNpnpWBQZBX7ZwY8q2YKUYp6nLfRE4vHB0KggK6-LZl0bm8UGxBZpUKwvfHdmj-6vtjhS0T8g9KFSJmJ9X1GHOTcAtCBtEPH5lJyUpFNBYZJEfJRD2M9Yol2McBXS6GR698AAJIp2ESwwkOpSH-jiZGTl4487MiBMIoHKLvn2Yqnc8QbQRjfJ3zQNjhzrxqaHJsH8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPezdsU_hFFgawlO0KeVI-GLcODr65bqzuDQomClvsgV_BIgKnS4P_ctmdYoN7SUHdzzzfSWd7cZkuUJV5KhWmaioYxpTPMHJXgBLne8VX1ZG2TKxlI6ez4L7U9kvtZLSgvPqreXtZgTI8CwsDfriiWfp96yRLGzjUOF2T2dnjaNklkz5AgJB199uDleCt04P06WHhXoKsg8zDMiX8mLuNlJx9ry4Ogj1scAQlmhO6Q8nMInaDELL1jRTtLZsURCvSpJOHMG4THVuX9SSBOkr7tslaOVy3Lh-i-rF4AiBiIGfrKfbVHtXz6u__5lYWkpQ6TnmWGoXvLwEgkLCmO2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0kol17XAY-8sas3MGB24Gkv1ZiWONbnBTg0NFsyPVbn_qK09P9wGB2aJbwiJLVvibO7W3rspX91iO2cFOJyL_a4HHGrPF4fgpFl5epUxXM2xZVD3VTDXpm5i89iCTcHfMSU8yVJSDSV4zxLO8fFCQD4lHR-bQKl71M9XRV01y2Db4A-Z7FW-BW4X_JuRp0c09uNiHqZp3vcE-7PZMZQhJCzV4boCTo1xQmRNNpknF93GXswM1duerzd-NMUXLwGCsmPNuc4xwPYqdh_st5_BCnzv6XWbd4n2iUM5s7wdqrZ6vwcgH5Tl01jlxOAsBsl4ALO0IXr57F-Oej6m3iSUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHvkn4N2VvbWUEmIyve798i9gvLaV7uSzfK46n5bneCyXew5l7BOPj8fFNbYOFTZYdCCxVCXEp8a-ji1kqpv84EUVhP4LlRRwhpkuela4yqYLVatZdqhVnAImhsTvreOcMnAnxVzkoJYRDhQmHP_PMG4j3_nkoU2-LN1doNK7f3wdG69MBFIHgmNgzpkX8Aa43mLYcuQ_Zck511gbY33jqdxlQidtV6JjCBcWVsTr4fXPLHZh-DamZbdkQPnTbIJ_lXCo67u1NGHjPox52D5vg6cqydg-tVQSHdaTXS9Ea2sBxox52l_kqAB_1CvPPOTbux9lPDcAIL7S58otqliaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oanYNfcn_Ei9SjbYOdzim8zTeLCTDOf3WxHs4DoGaiFbuH66TbloPh2grCkgRGZ1IJNKMsjBABWMnFfpWjt7w8KjRmrBS1z6gpgs5j3h7LalGsS7ZjCz4OxptD1CEY9PmIPpwx23usbZMi9P5XqeLZuDtSTd8oDInsEXU2QYLzLlnrOZMzlEW0KLXyaQ5W8yTZibI1L0DAia1qI5xAwmGQt2ISSH7ZEncESQbaKzlbb1JXRLAYnLNuXjVYMUGkvQuMfZCtZBIQCAwuno8cop1LT1RBRC1q5fCfwzI0OWqI_KZ23GXVxwhBPOoR6h6QgC4ZsAR7enHZYFaO8_oWJEvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fl3wh3WApQz_vWZ1OcAOFOsCuI1jUYyXWKNxC5fuSCV09EJk_dBipMIvnXgv-BC_kNfE3FyCjBCsYB8cJgT8tdL1idc9uSggly67K_t7lntqKhNhP5gzK2Umjq5c-cr4bPCBJnksnHYSxopfAXA5WOrMk5iJGc7wFWtI3KfY5wHiqKS43yZ3cBnKzaI_LnZDYg8rjd93OssrR5jMMwJpJusB9hWbi4Px9ase_Ag4gLHlBP_i7-nf4XYTCnutdkdZ817EPNJeSBgbPB_jo9Erqv7XeQ-zww1ZcP-rmUBqwJe6jiiSUvHFk17PZPJjvGAxoWs5LIFqf5uJvNcyWoaGKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoGY-Q1cn46A8z7-hgyOmGAW4xIinVIwbwMizdDqfBhJiHo7PHVUZReDyaQOvhsDQHAjXjCJqqc-xpT4ahFj-Hs01rjh-C0OA6ejto8jlsU77DCS3I3Sro5-A88uO6wV3mO-JDaYK0CxoVRMUpH2RtbdLjxo8jxR3BgecWuzyHZmTms9_iWpEXWYB_siBYJ058n0r2-3Hpdm0AR_byCzuzPgf1vZ4eE4aQLIFZMW20LMXcc47ZEZvak57kChADTJb2i-xazK2roefHVduRly5rSm6bFnp9aVLG4QrbJl2L_o9Dbcz7rYTcBHWYdD6DGS55CkaN92oaVKpzd3RO01iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxRMOblslywOH6bSAivcQxxI8zcHfdzgkf-P1xp-56rQzD2KIotNZCC8g8HMU-4wNXfejL3eeWyWhthW4OnNscIfxYUnPDPy0mAkirfZXZNL4QK_MpszNS6AVBbpPFgVo7Z-jzFXmzjAfmx3N-jHS8GRkyItJYAGad-AStDxOYZxK2B_iEotYITDISEebJ0nWmzNybEvMaqhJvuq9Cv9tnW64CqT2sJj1yvnSeOD9VaaqHHxNzhWTUmvyY0sz2CHkuW0CS1aJSMed4fjimNkv6rxwKtCkiV_ISdmYLi86OaDWfrMj3UaC6toJMOPIPSWYVl-jIrue4_V0PEdULlsyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=JS-ec7MvRdYIVO36JOFrUOZ4lywclITI21kZ2u_XzMPOUeD6DTnm_GZIztNpCdStKGFrrMsweCkGmVfDtYVDHMIVLn1-zGsqQMuFDw_2UMDq_yno72C_bpMO2GW9t296z1gFDiOsM6NHCDQpgkN9wc1uGPTIZ2ze81UaqfcLForZcg-nCyNosJ90HiaYBWF0MgftZu5VRP-pjSmX5ZVXNVh0AlMSmouRfpv-jE6nxVAMI1Nhoazf60R1yPCaBwMh5R2iLxl4c_H7aP2PrWSUA6x7pn8GjkKTVtwLV-VgUNsm4HUi-Qap-yIgB5T10DJnwRUom4SwO9xke68EMqeyCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=JS-ec7MvRdYIVO36JOFrUOZ4lywclITI21kZ2u_XzMPOUeD6DTnm_GZIztNpCdStKGFrrMsweCkGmVfDtYVDHMIVLn1-zGsqQMuFDw_2UMDq_yno72C_bpMO2GW9t296z1gFDiOsM6NHCDQpgkN9wc1uGPTIZ2ze81UaqfcLForZcg-nCyNosJ90HiaYBWF0MgftZu5VRP-pjSmX5ZVXNVh0AlMSmouRfpv-jE6nxVAMI1Nhoazf60R1yPCaBwMh5R2iLxl4c_H7aP2PrWSUA6x7pn8GjkKTVtwLV-VgUNsm4HUi-Qap-yIgB5T10DJnwRUom4SwO9xke68EMqeyCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4Fqn8fmXQxNiEPgId7r0v8uK5Bpuu5r4UtXSOXNu3U594gfQUJWwVBkws0miiyufm4rSUQHjz5wPA7VNOCe4R57d4AyJCGnpIhpniuHXUR9vfYofgn-wDFoAI_8_4SlkcCZdKe0ubo7iExWJzws0CBOpXrpG8CwhOXWkiE22J-M2SKnyUaOUdNRqfZYH43yKQv3xD2iEg_IS8E7HHrXcLRqJCmBDv3W17R28spkOmot9D87UxgCpj_32cA5PLO8NG8IsAXcUxwhfC-31OQuk2wMyeGvqMaBlOpmiPKocyH747mnQ8AlIiJMR2UqYjBEiFqmLekpCjq3QUcEplOEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2GpbmdQsoZcMT0y29Lr6NCQ9_ML4P-XYM-vXv7YMv8A5BEw2BdwXdvDNPjxRDr2FyUtNGW6pQcTkq2gqhEQDTx3OdpfV_KK7fvulpuYSQdOtYZgLlEhX_BkeQeZUQuPf8Rz4t3CAFyLWwXP5HAaVemvtJgnjr7YtnDrUoLBxSOpPv1dSqQkVqCB1tlpCM75oIb_RHKtDHlDo8uNtLfBOFOv9c61W79FuF2HDhIcw4UiyeyVoPuyjr4pyOTDz2PNdKk-bncoCrRplbwX4uDWGJ6Z3EF0uiyppG1Uvv6LehNML9Eg9hUKJs0hB_6MAorxTOJ07KMJDhOd4Oxxi4XwhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=skwAjG8ccuYl8i8vrt1B5gzH6MoZyiyNh7hUG1w51Bz4b4rK_9s6cSLFJvn_vzp82xd8XgN4D3U9Aoirg4WbdIy6Jyaq42S3WvDUhayVBvUByz44NZUVJKqmnSAcQGeWx1x5q95GwkRL3vdGLIi1P9sCsgJ6j7JZ-kVR7CA3quPSiZQiFa1hp2uzICAFcvOdD7lCbcGabFNpKgYExVZZg2YvInBYIb9qrg4Fcx18ivliMr9K6w6dBvhgrfwd2pJRB9ghTXWMnZkRVdIspAmdXG08x8dDhazHALHl0jg7qQRM9QnMeBc6tOuH35c9AarRu65LGj2ykNh_V3nhw6Lx0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=skwAjG8ccuYl8i8vrt1B5gzH6MoZyiyNh7hUG1w51Bz4b4rK_9s6cSLFJvn_vzp82xd8XgN4D3U9Aoirg4WbdIy6Jyaq42S3WvDUhayVBvUByz44NZUVJKqmnSAcQGeWx1x5q95GwkRL3vdGLIi1P9sCsgJ6j7JZ-kVR7CA3quPSiZQiFa1hp2uzICAFcvOdD7lCbcGabFNpKgYExVZZg2YvInBYIb9qrg4Fcx18ivliMr9K6w6dBvhgrfwd2pJRB9ghTXWMnZkRVdIspAmdXG08x8dDhazHALHl0jg7qQRM9QnMeBc6tOuH35c9AarRu65LGj2ykNh_V3nhw6Lx0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=lNHG_y3X1oG447YSloB8tPMZ1mFXdf0jw7pZlzTY9RPdTaIYdTViQbDAN2qRh_T9qRnvEZm3Rq-YQDxadNKCEVUcikLdYhb7V-xS1mJCNDTSZbvDg9NnMpeulYsod0JtUiRJadkldz-7ndWoNqINRXx-UFsOSJW4S-BAToDz1jHn2atuJPX8gmcqtzcXJxvuVis76KBihaeC2ZSgK7CfZnqt09sgXqZO4luDxwWns1lJuUQ24hUs_4mHt8MAPNejOteuV8IPsW2SD45hcnYmQ7PRWWXhhPj5kYqOdx3nWYny0b6tIe1xdSXDeXEZ2dHNwRR7t9Aasy6-3p2kZ_CXIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=lNHG_y3X1oG447YSloB8tPMZ1mFXdf0jw7pZlzTY9RPdTaIYdTViQbDAN2qRh_T9qRnvEZm3Rq-YQDxadNKCEVUcikLdYhb7V-xS1mJCNDTSZbvDg9NnMpeulYsod0JtUiRJadkldz-7ndWoNqINRXx-UFsOSJW4S-BAToDz1jHn2atuJPX8gmcqtzcXJxvuVis76KBihaeC2ZSgK7CfZnqt09sgXqZO4luDxwWns1lJuUQ24hUs_4mHt8MAPNejOteuV8IPsW2SD45hcnYmQ7PRWWXhhPj5kYqOdx3nWYny0b6tIe1xdSXDeXEZ2dHNwRR7t9Aasy6-3p2kZ_CXIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_F0LE6t6Rqh1MWUtDynDTxaPFMWnm8BEuRm_k76WxPqyCjX_ZjA9JRikSrU182LroKMCKD1nINh4LCMb31jehrnBUDg-lNxUlfwvxDqkdiYQn32saxwenqevJhZtwKZtODyUDw9F6RlJRqqnMbfLVvS1JiZfVbZ-9SwQ178-Ex2lm_V6VLEck7athgc9oiRzUvz5isptk3bj_BsC6OWGgZ_OvQkrwnLOV9Kq8zlDqui5J6knWGMMy_BT2Nt1DU7qtJDslIImCXUk61OaerkhC8eI9EZqVMZE1pnq-sm3rtg8V9MJ_500W6eE_xgrvgX78zczgKsjw86iG78ljblJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJs1OxSKckqFTz0Lgc2-bAk73-1Y7-LvFtMRGy8EkRVkOH6l2MG1BWKJfTxKxWqe9vJjyvJcq5FsnCuw1fksX2htsyrRwJUo8RthKkrHpRxARDysIOqWWHcuTiaAzvUIx_lLGSk9-x7-lJceCrsLt7rzIjlhjCPynkv-njxYpwUkzy2IV0QqqDm1L2MV5ZcThszx391Whag3fHo6qp1HboNlMztv0kRgqGlfcBor7fJsbCQAokSDKudiazVyoFliFuLCD2p_DwWRCessCgO9Es38GVeirm2eqO7joFdiZUF5kHLeSB0Erj7fBrC9H6NM3IiOTzqk0uKaJzRK8c2hIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IW71BWa_qm6yGCMQKZDP1kcWq-gvlsNC3KCVdRPSQcb228l-KS9w3P4PLSe8M9T4rvZbMW26QDHwP6zURjVmxYewFBHSAcrPwNAN8yrXxPS5ARtUJ-US2nkYl-JI87b68_YPyjTsYFERL_aFQNK1V8ppUWDBTJLGOZKW_T2rzNF6MH6DkydnUm74KLjgNQIQIkZKqENLQYeYXe5fZnr-wLZvY7lzx7_s2pL6g6n9ElFrMUWYvdXj30vHSTghzJLAVpOpMbemBVjIA5WPHjhrCpKiox5Wlw5e6rZ-fHQF52IKFKs7PFiaL5CxwH_hvmPtNrlHfxrI8VxxgSXpK2cPvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IP3sZbgU6bWKtBj89Jc3uOs3smxc1L-oAfKSWrekJ-1P8tSzN4x5JLpC98Zuvfvo3kznik37GQwLve9ydQaPH1-cdXWAMB-BRfePfgH7Ec6Edi4mdm4_bW8Zu0lbCV5qSiouWnmDOS5DDJi31dW7KiFn6dXR83IWrGO-vRLyA0-ngXWX8y7oIwpISfBWHmqL5u7M9bk93Hl9kY2A4Nk-tpFtRwpe5Tr0B1Ng-XuCfD1zvW_QIyW1TrizHUA0BU4LZ7NBfM9RQctdJy5gHbDjiXvSGvJgm77xiL_xasNGe4_61xGZrZoh3OLrz_z6D2xcZZZS-WpV-mdsZsbavhyXBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnHWI17SRvEOjtgBw7MxE5jsCfvV3NbnAtQKNyUhBkhP402O1q5bijfiBO0sTYMMhixGfp5iAbsCOqaWDn2EJ1oMxJLpTmz3J-8SlJrbApFQxlDYf9KE5dH5XQjcBNflrzBOX_n9TAf8evLtbURMwRQORXk6W05TWS1ywtOzyaNf-T8SR5OS49D6gZ1JoPhjRb-NsqKSMa9-spL0DJ6DBexV3KSF6UuyDcEX_EAYp4jLvOfjYsnTNBkUOYhzh7gJ1gkfrn8Hnvfgvt1bsefxrmlz1e-icKEF5q1EouUG8PsaBsa5agKYf0cgVguXDuclN6yHRQGiw7CLULMs_VtkGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_BiXKzrCLTqlTnnohV_oL2IS3x22uWVs5pkF3h6wct4n3GB_nfdIvGaVJiVTqP0macbTtLqciOUHMg2dyJhviyGmK68wuzNIMU65JK7a3nPNt5QacAcraBcGRUUlGKX186PmVgvgaAUuO49H7TjL2UCIYQyzH2ZwXWvQmJzRHd3XLTDClqQBvAWlqGkvne9y7coZbjEUEMsoXuOm4Z1aCfwR35wGiNGtRROwKves8eB1g7jmUtyTuQUw5c6B-OidlMr-h6dhjPfllu240AdOOtooRLcci1SgJxvGqSN3m0iqAG6-RiTsKYrJeoG-8Qn_QLE-h6eY6sdtLi4kqx-Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEoC92R5VzDw-DmhqBcq7CD-X3F7JsPC4NQrC-OJG6X8eqgOLOl8ALCOhTzwwj--u1xMWh-vyD1Okp_vdCANyJwIMxzLGtpNDeeZ_qadIW83NIWdNpDxVToZwGi3tvszOuHB46MD6fh8HlzgstsCjLVNye57d9AugqsGNYasBQxF6L-KWb7V1l9fhwjw8UQSNpOF-ntK2Hp4TpB7jIqPW4hGmDy00XMQYPrYojjwBIwTsKAEBNmoMUb1PjxpUu-IQsmuB5zOR0FIa2zfkGp935jD5Raa_jHiYH5HB2FRGI_tUHkCx2CeGqkOq3tSc9A5OZdQhfr8qa5E8jv6seGz7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1o0iysKgguOq2hd0bRDJxnHQNP3VrYTqT3T8hE326eCp7PUvO1XbUw9DOqrktKv74sBHOsGcEyatJL78dT4gwgxFjuI_eqJu3PixfJfBT_piHF4bGP73aAwqCa7WVVmKy1m9Rl_P1JFguXwVhdKnzw6Z_DedLINxljcdxD5ZHsEtLBruy6fUiUwauOixVPzoqaY77oNLaQbaxmWQ3_2f4PYVyg0LSKvjJqu3cCVk7lRAUH_hUlDzEVm7jdy9bhzYIRt7OKZlJ4MqBAcN6NbL4lc7NcGoUytiHNc3haI1ykY-kKejgH7ctRbs2zhu5T-DcimxS4QRlotHDr4LGg4tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=XUjGZev8V2XWQWvdu-2gVTn_RaAS9_h8JELRWdkvekAnSrvvEzxj65rl6pgrObQpbNu_47W6jniUMcG3Fl96qQFV0EhqcEejRhwsq_tHovc0L6HvRK4Qeeeeab09IxrEXekYNBrTTPRBbOwuYmqJDNoxPrULrGE5SZijSNd820JDHEpVIeIjGlMX3oHVK-8jnhUfa3Q6UtytbGN9HscgQRijK1plS8UOQxKKZrRU8BDthcFMi2hJBQ29gy6jMDeUHb2S7FVs7q9gYTe16odKe8oarxLZj9Kg1jw6yWQGzu1vYMkRzwZrcMVIG3WjcQsgA4ysic-fFiJ57HRlbu34Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=XUjGZev8V2XWQWvdu-2gVTn_RaAS9_h8JELRWdkvekAnSrvvEzxj65rl6pgrObQpbNu_47W6jniUMcG3Fl96qQFV0EhqcEejRhwsq_tHovc0L6HvRK4Qeeeeab09IxrEXekYNBrTTPRBbOwuYmqJDNoxPrULrGE5SZijSNd820JDHEpVIeIjGlMX3oHVK-8jnhUfa3Q6UtytbGN9HscgQRijK1plS8UOQxKKZrRU8BDthcFMi2hJBQ29gy6jMDeUHb2S7FVs7q9gYTe16odKe8oarxLZj9Kg1jw6yWQGzu1vYMkRzwZrcMVIG3WjcQsgA4ysic-fFiJ57HRlbu34Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vs2sWhZYRnXP-Pu5gBdEYfN5SJrx1oG1txJfrlXEMY_POgevh3CooeY7L_0Uz5A4g4V1krljMbm3R3phg4ARV_NYgqW2h3_eMD7Zvz9IYKJrsllZGFga10EYNwM_iZsvSri0N41hAJ_iO0Sruz6fg9Z55ZrmL4g-dzbEU7VP4gAYqfwg2XI_aUOXs1CkZ61Ahly87uMStTONPmuYMkplORYihRlVvo_h1r_Jh7XCOXD2whiyp2XlpGltzjsA8DRd7IkSxUYNL_4VovX7XaB5DDwbuxAGCgYiJwBvBDfyUCFFkE_fndUnzveGkkFI70T0Xods1zNzCVS9eFuIfKv8MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=S9JJPlYiTjxnVR1JnZAdWwuHrzGiWYvEpGDEok_hRQ7FnNDBYnUO3doZDjQUgDwoPmrMSBoouNVDFQrfkN11dH5sFLgiYtQuxTbzYKWT_8bPvjgNeBXcpfEo0xwDgQcss5Bzvw1QeR6-gyKpjGdrm4ZobFAbyh15s93awB1vuOmQOF5vDHDweu5--6xpbdSeGzDaMmNGY9fC78jYyXmP2C8GUKeD8RO08C2kUOrgsdBecS6huUWFlzkFFLAMJi7E4FngkAgZBIKyr1d9Stp_uLdxcz50DURJvOPaEdLsPHI59GyDB_pGcy9z1U2_zd2u7dFK2UJoMJPGvNrQcwAmeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=S9JJPlYiTjxnVR1JnZAdWwuHrzGiWYvEpGDEok_hRQ7FnNDBYnUO3doZDjQUgDwoPmrMSBoouNVDFQrfkN11dH5sFLgiYtQuxTbzYKWT_8bPvjgNeBXcpfEo0xwDgQcss5Bzvw1QeR6-gyKpjGdrm4ZobFAbyh15s93awB1vuOmQOF5vDHDweu5--6xpbdSeGzDaMmNGY9fC78jYyXmP2C8GUKeD8RO08C2kUOrgsdBecS6huUWFlzkFFLAMJi7E4FngkAgZBIKyr1d9Stp_uLdxcz50DURJvOPaEdLsPHI59GyDB_pGcy9z1U2_zd2u7dFK2UJoMJPGvNrQcwAmeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=SLEUfCPmo_HmQ9lrrJAExSjImOP6uHxjfcK6nccsNOSMYEGVYpwZEFW0lzVExX2w87MLOJHDHljYOYtPYAm8XqMC3LJ0eAhLRD2PxrmxNvc7QodiWgTegX0oJ6NH5cJ1Ti3XYI-LuxRmGBlpgQAfnJm1D9oAwdPQuDlmuhbGaVmvacf0wy0iaL4vLNOK5cQvuVYjNfTd4XV61tCwcCWCHs04nHPX3tyuBBYQvTOLjgPDIR0YVgrFePWS7p7lBprHKVRSuzRYj9vlV3nX5d2H7C3YQF5gh1SccwbIEndPxja-N0LKKExQqY13LoOUK1viWy09Nspe1y5dYcp-_ebLig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=SLEUfCPmo_HmQ9lrrJAExSjImOP6uHxjfcK6nccsNOSMYEGVYpwZEFW0lzVExX2w87MLOJHDHljYOYtPYAm8XqMC3LJ0eAhLRD2PxrmxNvc7QodiWgTegX0oJ6NH5cJ1Ti3XYI-LuxRmGBlpgQAfnJm1D9oAwdPQuDlmuhbGaVmvacf0wy0iaL4vLNOK5cQvuVYjNfTd4XV61tCwcCWCHs04nHPX3tyuBBYQvTOLjgPDIR0YVgrFePWS7p7lBprHKVRSuzRYj9vlV3nX5d2H7C3YQF5gh1SccwbIEndPxja-N0LKKExQqY13LoOUK1viWy09Nspe1y5dYcp-_ebLig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-3UGcx1eXE6Smuxxlf2AVwgkk2gGIMIbwFLNUkwUqSJ-8uj6n-gOQNy-bCmU-DDXfH3kzW0Hv-59Xn57AAUCUZ4_-0vhG6khwKZfVhhKWuXPq0PgkpTk3-UGha3kNOtg6JU79zTPnc5_M_Nxhi_dexORAWw10i_I5tx08wN4iage6-FSVSVZSoGT3sMjdhxYWqJtdry3FhiwDZIZuCJln_9j0qXHwfJ6uaynQ-0WE7w4o6hnli-Pj2JITAK7_j6uaPzKROfehRGLfH7MKKgXj5YaYX5C0w4kPNaNX6s3zPtEAzUQXj9ggSYDdrxnc6txaGMkkwTuNZgoqQw-hRqMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfqAYIxWdK-TyAso0RG36s_g2tJQViQIdtN_peiKmFpcn4jy5JW7rxwrVuLkJ_tf2GHb3fMgIAFfl7AypAVEu8Z2jjoajZsEnZGI3grYu2h5PmjWNKsqWC-8eRiOd185ez_YCKo1bWKmBW3IRA_SC3FSPTTMzeKVBcq7X4dlK7xDpxJXjlZ6sCy_oAT-VQE62gde9bEWW09Ze2JqoKyEPUU5uepUtxmZN_L6KX8uvA31KaAZLp5E8Mv5qoB0ijOp4hcuf9jtCv6Lx4AoZ30PaRp1jL_umldefiNIahaXbpE2BCIf0TYxki6mmncFTV50Ifw1OS7bwVZ2-UQzx1gaGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=C966Mv6Ze18W_H0g6OvMEdPgKmrTnF7uVws559rZ6Hm07hqVhFC77Q-b7jN9RxuTi9oTrTy_s5_bk5wfg8nXfPyyMAsSU4Pb0Dh6ZR-EUpJm_C3jL-dQhZ4WqMA19-qyNLOIKeVGHDgJ34KqEXbyiv3huDvyIy-rqEsPGBfdZV0QrGaI8Tdo0h_tNoo629tgF7sYEBTf4EWvGK9BLNnBm2eQHlwYmyM_a7Yp8DaaHXWt7Ll0rW6f8K6WrgXwBKkac9LerCvbbRUFw4aWtTXExVWkQv66uBifNslgZQ667KPvvjwouLBk9Acc-CGDP9ZsFeQ5gRhGLeGwZ3uA6aFhDp77f9GnNWQfR_7KDsdqcGWDVNS1eUYLOjSsBG-IbSFk90qWWkoZoWdYy_PE11TO4ULkN6MY1Dusni0fCCqa5eKudsrC_wBexWM2gSgPUK7C1NNrxSdZwS-pDUFPnX3wfu1G8aeoi0QK5qGTu3jJN2g7__V9Rojvjh1PVjTEiu0PIw0xMvsBJSO1XHIcGBlA_ZyqmerMTZ-LMlX1YKv_igl4oRSQpjqX7uaARVD2Yh21PerAXLV92isi6zhAkuzANKCd-WV1d_xkXGNKT2W-1y3D5x017ADdWvDFJa1doOFcUMVQVKWgO3hZJzygytrxRzjf_WDMgPwUqp8UQ-3MFBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=C966Mv6Ze18W_H0g6OvMEdPgKmrTnF7uVws559rZ6Hm07hqVhFC77Q-b7jN9RxuTi9oTrTy_s5_bk5wfg8nXfPyyMAsSU4Pb0Dh6ZR-EUpJm_C3jL-dQhZ4WqMA19-qyNLOIKeVGHDgJ34KqEXbyiv3huDvyIy-rqEsPGBfdZV0QrGaI8Tdo0h_tNoo629tgF7sYEBTf4EWvGK9BLNnBm2eQHlwYmyM_a7Yp8DaaHXWt7Ll0rW6f8K6WrgXwBKkac9LerCvbbRUFw4aWtTXExVWkQv66uBifNslgZQ667KPvvjwouLBk9Acc-CGDP9ZsFeQ5gRhGLeGwZ3uA6aFhDp77f9GnNWQfR_7KDsdqcGWDVNS1eUYLOjSsBG-IbSFk90qWWkoZoWdYy_PE11TO4ULkN6MY1Dusni0fCCqa5eKudsrC_wBexWM2gSgPUK7C1NNrxSdZwS-pDUFPnX3wfu1G8aeoi0QK5qGTu3jJN2g7__V9Rojvjh1PVjTEiu0PIw0xMvsBJSO1XHIcGBlA_ZyqmerMTZ-LMlX1YKv_igl4oRSQpjqX7uaARVD2Yh21PerAXLV92isi6zhAkuzANKCd-WV1d_xkXGNKT2W-1y3D5x017ADdWvDFJa1doOFcUMVQVKWgO3hZJzygytrxRzjf_WDMgPwUqp8UQ-3MFBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdgjwXwKX1GAcbNnqKy1SxhTkumpZU8QJdvXHltudXjPxqxgWUuBrPiq1duD25OYsxAcwbzW_APT284aft4SDNDeQQkzoeqgCq3F_9RLaURIIbfCl2ifD4njFV0JmnsbBx8v_lJz9KQnnf2ZykWcYAt5u1dy1iHSn0zlgbdb2CWCUkCEivX8pGtOa4UiW39zKhe6iu_XtVqSahMPkChyC9KNvdg982A8WBMzLuds-lzEv0OjCdQpED5QDroDZcjtZS_So95PClgE-HkMi3Bo9Elq5YtoYIPwGihpK2si2lB9_wv8QVvdvw7EGbU-o-qoBz4uHX2Mo99hRvtS_04W4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=AUgRo5akDivjONqFYNDbZcnx4gy4KyForwJBGRktThEHeHcxqPJiPsIXbevuKaD3sUGMA4pMsAhfJe1PH8_OxIflk5zZFbMmmd4hW_U6f8A0yD5OSc19VX638lPXJakyET-f5M99Yi2NyUhxlLQYScL-jghVHwyLs1tkxfHd5iltfwC6-rrXVGr6n8QEi71wR_jglEhhcrE2HUWwboRAAYenc0l4-MNza-syH6MttvlcN_pWJsuNC6XndLUREw6giwTVyLbWKDjRJj17o9eMW0kdPmurZ6v-HW3MIUeBQBhRgTG1WpbptBwxT2KBPExaKPKOmPXpqDXdDeUX8mwWmmTHgK8ioAk1iGKM8cL3agj0wMMSHtlj_z3ysoNLIChrfjo-egyeFwplygAEOyZ8WA0LtzC6pkx2fsoVHifqENTafIshOV73oZVitTuK8h8xavzbxWl_Ykq4f99qchfLZCUVpnzNV3IN6axV4O0nE_KW3Dknu6xp3_Sag4b2ORMWVWf3OimP-K_zh_TifjBkfczH5nvDDKOJ-hUm5yRVwFblk2junATR5TY5L1awTegA_qicfQgqKaGskjAxttlOXeGEyY2aQ1tjwUwuyPf-C9wwu7lXIveXPCx-OhnwPcTeWCSPChCSpsx8Yjz58_C9tCtO0qKMRc1BPWlZ0pUvro8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=AUgRo5akDivjONqFYNDbZcnx4gy4KyForwJBGRktThEHeHcxqPJiPsIXbevuKaD3sUGMA4pMsAhfJe1PH8_OxIflk5zZFbMmmd4hW_U6f8A0yD5OSc19VX638lPXJakyET-f5M99Yi2NyUhxlLQYScL-jghVHwyLs1tkxfHd5iltfwC6-rrXVGr6n8QEi71wR_jglEhhcrE2HUWwboRAAYenc0l4-MNza-syH6MttvlcN_pWJsuNC6XndLUREw6giwTVyLbWKDjRJj17o9eMW0kdPmurZ6v-HW3MIUeBQBhRgTG1WpbptBwxT2KBPExaKPKOmPXpqDXdDeUX8mwWmmTHgK8ioAk1iGKM8cL3agj0wMMSHtlj_z3ysoNLIChrfjo-egyeFwplygAEOyZ8WA0LtzC6pkx2fsoVHifqENTafIshOV73oZVitTuK8h8xavzbxWl_Ykq4f99qchfLZCUVpnzNV3IN6axV4O0nE_KW3Dknu6xp3_Sag4b2ORMWVWf3OimP-K_zh_TifjBkfczH5nvDDKOJ-hUm5yRVwFblk2junATR5TY5L1awTegA_qicfQgqKaGskjAxttlOXeGEyY2aQ1tjwUwuyPf-C9wwu7lXIveXPCx-OhnwPcTeWCSPChCSpsx8Yjz58_C9tCtO0qKMRc1BPWlZ0pUvro8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGecn_jmL9simevmQmNIPRycMARkBOmafEXzov8k5PxiErHfzV8A_0DJZQEFG_24u5avEZ4q6R3euR6eEgFcUNROudPHq2x-C5bRkA4jSXp6N9vPnp_VtVWFUC7-IbYHB2iUft07REONke7VCDGtxS8weUTpLaPH-ZFWa6NYcE5yGBSqMgRHVdbKYxEFGUKxYu73aZB7uR5R1H51GfBEZcWnsLUAe_iascLT86yVR-P6qCNYYWhgT6aQGm2uj-w-wlo91ce1563sN4szVtc_fyNUW_c9ufWuYyvtvgXrRzObAut_ark3TmC_IvbuwWZ2JBuNmrGEOi5Q1fHUb5doig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBE5pRrq_CXpYmOFwc1YZCsO1TTpaBaedrbZbH-Nwu7mthBPXAEPUgH6mJKmNcvQXyBM_J9mmBnWNVMm8SdzT0TQVh-rSBl4nVE_6ZW79coBUqKctTdEJqIUBggTWsoSD50zgA3xjEpgJfNYJi5iyRxX69Y708bzMpFMQh6xPKCSnBJmeghsDy3vYYHX6zqf1FfQyQfPoV1vgvC6W1o-DxJSlcYDdzeupluD9jGjdjKRC96uUjrI5JUGcDMzYguGEcd-jM_eYZMs_JCUH-bBkLbQjc0DtYqtEpIx_jE_DfXHONuYz6UJEk-8GdVJPk7qfy5Oj47i6X4XCETPNCznQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXWOenSt3Jb9788rkDKknqyO4KhwCVCroFpzjAWGLMzR8wSMRh0WHFpjxH-QSjyJcXZB195YFK7DdBJzeyChZNqCbcSg8wFW6n1ek9RInC3uo49zSsPt1C1AHWtWIw591UX5BjEzjha0LS6slL1AjmxoicYV19QCC2J7BwMRjdMIrYtGSOFT4i-EF6G0Fgy2Nu_mbRYcY0bx3zipCUl3YAZIPlxA4QMjspZCZ1hM7FqWmUEWdq7g-hPoZ7SQ-CimYToChgcyWeKIc6s3WAWRA4nmDusvT3br0Eg4KGsrSIjMm_al192qmLiIld_SsvbfqrNI-sbaEqb0y1MUL4ea6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srlLaloldE0kxVN8in2cBrvR32WBxyQTh2HD1so-pm6If4Yvnhwsfv6Ruic7eC-98Rz3RN3gZjBRG3HDJnKLl4rfdxaHEFSND_BABjS71ESmiLwj8VZd-iwuSA7bCAnWOhu6FqQuxVUp_BQqRoubtaBdMtinKdOq4tYU6J7xqpL1lOx5vb01JwOQy5w4uUUKkDAn7UO05SaVjiN7g8PYUJF7WBeD7_uVO35AIbvWHFxSFuzzDh1u58waCgWgm68ZUeUKFAPF6mqwwHZXLCw7YRaYGEkQLKpFec54jtySoukQ5rmtstq-GDbg7v_X_xm9kaiWt7HoSLO2v2skwwY_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSvS-IsVcKQBtKOdHatvQIzPMrufGoPMX5yU6XyoenxZfU-48cC-fq1eyXzpteX_VYzPUk-XRd38bHiewgYdnorSSnG3MxAKHv_Xim8xcvyXLvkRmZmAWz19sAN4-7Gc0bfjCHFtxyStVicTwmIt13WJobfosOIMSm0W76RwRCLvVXzXsMVFSrm7xkkUi-xnZWXbix9G2fr4vP1EckBKQ8oPnnwSUFppu53vlz6KZN7x2jRMNf7v8G6lUwItdbh5Xs0eED8muEgiO629x7jz4KX7bX2g9Gdv6_kJXuN_zTdMdR5_6Kf7ZikXS5a0DJ6_rURudLQUo1_bUT7picyiDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGqIvgu92ZR0RxoV4Dk3Y3sLR0hQtNBF3PiYuk54LAfbqYhc2G0_fLJhXP4QlK45M6fTV-GqJRlouPG1yVFwL5jJ0iYEq4lQdfHvedCgjkTbgkIMdKw58_QR4QL4f9vNocaaaA5gDHxV7rFX0qE46fkkVuU3TMg5PvQQOmzotnS3RSaH1GMbzfcmsc1FBDMhQIrQf3IOKvELuM72BK2XtgEOjHbshvJG1hFMOmmtp5Hrp8_269eMPWmYs52tsHT_E7iuIbSsV4H-EHtHlWOBoYDTDLqHHu1MQniwGpIwd8RgvDVIB7o5cly8CQeB0ICnBfv_Uzzniee9DS5SmAc2sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Le_iieOhuqekvsQgsTpgWoaSg7pENv_HA_Yl4OiOEvmJzuDmHqVMQWbD3NOpxQTk1Sp33QbT0Pg_p4LIT5EDt5dphKlXVerFnXAQLzMoU09mhz1HQ5ShBMTCVqKYoPNNiBQdx0qEHt-RlwbzAhx5DkEVpMdLyuIRkbZZczqXeJy3JvJUNfoSzDbWPF6I3GwdmfYGxcogBrGVTuRT1iLXPqqXXB-jdNeIOzSIS3gxCjLpIpTwQEpdgUglJppBuTDzGI4VowZSG3uY6OVoeUM1dzvAZjiF7anpldclZq2c3PBSlE1ib_czmw7NFhjgkdl8I0gWUlwqFI7eZq8a97_lPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRz8xTtB2Cu0hwVXTbMi_n3qeGiXomD1IO-RP9zJKpHJksRLf5hfIhb5nocsY6Gcm_cqIgNjrTZEd-L2U6kGsXRY1dsZ2RjrRRjedhnrAKx-RrJLXt9rkziJBjRZDyOFlEq3F7AEHeQ_hAcegQkSqcvlRx1Ud5YYDmJJ-dT82PwB6EUPrLJxqN4ovVQciS8KKLm66--rW7tLPbhVp02pfewC5i3KJn99lcU_qVlj5qHLjTQ4OXTpIyiWaN9-iDmpdMyS2Pxdwc8W5zdGvucGhIT3q1dM7oIlIDHnWVHb4WsHJyxmsUnQFZsI-mJrtLOlcROFm3MtIUo56KtOkMPyvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_VJOdd6rFwVM2hPULbpEM-Y-yeLUa_RsRExfpjHnYBkcaV8BGvlnsOvsjhpyFk-O6xLJquQwLMZINqKtcvAhqhZTuJJYykYgbHwexADhrSmcdVrNTp_ZaLXZpSwIDQ6RfLMtj6atZFhgMsXud8bUq0hF7P5qH2HPHLrMj4icKQkiDKz9F6WTtVCPvyO_LZ-2hYVkJ6-Qjo9zG3i8OA7sJcZyQL1sMUFGDpkOBbrQDS2uBVqAGHh6Yry4igCPSwummo6vp4QxS7YNRI-UFBFWZn_vRP3QWMLlLLVeoOqicYqu1FV2wCyLKjetPOf1URHJGwg45po4Ln_f0xTVla8Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEWVM0WwqBB31hw89vMhHvzkoRJ9oGiu6XgqGzGieWd9gYHMoDDPPk_W0u7xA6QBdKd-qrFOXAPVY3o7w-j7kel-RNLttnpdFQf3ZIB897GWSQ6ZBwIyyqgBHRZkxh_qeUi9e5i-MyVBXIozvQ1cOWFB58XitBmMl2ebk7z1oejHrdM2Z5IFI7QLwf3RuwSX_VN66e-kgQIopH9SospbYDd-3xGpKMrfZgp0XMwMY2kxVtxuBM9AtuHgfq4xLG5GKBh267uJNsI927hthPwINbRIHar-1NY-LbL1JmPhww4Cca7HpUQCmuVC8w_MKCS5XPqomLNcBky7NChJAy2puw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-2ApXgrdgzKsbAxXX5H7APUsMdRMwWIIZSSi0hafaYb3k1BCyG1OZHNcMWuFdHykObpYtUVpVbXQstLTyk30B0QkGJUiXvjP8D-gsHf8IhYTog-w2xaQD2pkmrxVBEewg1EXUDTTUb0pSzHOpXRdOJN73f5hlqNMla7_CXBW_4Y2po_0l_6qr9L3Y8jhCKJAY-Tf2kjDHTPu7VyIMxcEw5hK2UqXcCiq-D-L0QhleNN7uo5zJil1-NuJkhyH6isyEKD2PuSk-yT6xEEs3XuFW0Jev6Yn7YsP9UnlmHgO3XTCTauBHe_NZoVX6Xc2LPhe05L4OVuPitCeH57mLUkSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFFTpWIqUoQaWhm-6tRPn7pee2DxNWmhpXxF-BLZz8CeA2DE84Qk6hdTNXDqCL0ElIv_bduGsDqaYpomqGCH2B228ZzD5Zu9PZ40Xr13SSYzNrB7pufCaMmykNVnb-cdeyQsKLNJeEbqig5zqqExF-3iAFaFC3QW-gApEHV5F_DpZSbDA43TyyIaN0hb3gwMsKJBhU_vha020UqpusQ378Sy7QuAM6-80GzUzQxC9DqAAiCbUU3enlM-tFwIjB3RHTxy1wxWOerYhglbo-YHDAoRFrBTgdNe2lZWNRhb23j9dRpwOH_EZqahrQUCkVBEhH-EBNVmGlDzE2syt-Z-3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtAMMvcxqqPZWCOdicDDL7rbQj0fjc1tYLIDsjX6pzPMwW_8A1QS_o8jwRCAOto78nBYeyjMmDC2Wc9KpgXJ_AC_VVuyJlQDFDGmNsaKOpImqyIXoE-BcncKAZnBoIhaML4vIUfBwfo49sQRb_dSwqcgr-BcD_IUl3EfrCxfQyB9y7Qo5LuIj8t8_TY2djP12Ch--6V1VjBPccsihzu9wbUlGiZR-fsxaYiOne2heLg1_lSOKAiJkkBMf6r8ha5zdf2Z24KHRqMeYMpFJVmm-YXbRoy4Ixe-UItgBr3mu1GXoByIbSeOE5dDLl8o8OGy_0zzMx5ziE1XPSVEebFZ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwXnrl-ubyWOrS99a1Z2sGH9d_gUHQx8txit9CuOmBMBzwmUCMK9Iuzf4Wjd6xaRTT2fR5hvJrB3nJFsh1Fw7_rHKLbxNQEF4DpjtjEmdoEhOGZtQOE5Et9Acal6FB6VG4dqQ5l7h8_37odJnC4LevXGrKQ1l3dSNBc1LjCUZsuoDQoapHvytCIfSFOFiWn9k5TmMIMOPWLNYmVe6MDE0b2jvvBuyAVRdohj6BpD7KCgyvk6gHz8sYOKVkqUwm1F3JLKieDvI8_5vAme_VUN_np0FFTaCQv9yEmmL0nhXMbtyq3_aU11qFcXq1Y9zc3K5kR62JP0QTzWTl7EGBJ85w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQo3FZ6LVLD4mEe0u1Ly1_ETgcFXr3PJZ1JqydfuGfMgO94dSvKCWhSmc20ITsCOr-9WLkNsPknv7UNQIIx4e6WqJBs9d5oPD0PaqvbLA5j2UT_Wwo90_RdB4EOWffrmdwnfynHf9_4ML9Z9_a9uq4tsXSttoBKt2vqZcXbT9kp0Co8ZzHKutfV49Tw9x76k15vtB3LD69rNXsM9XPcqDL3mvpobnTy69lk01fbdlBnqMSY7b6IhqH5WvTjShDKDOfTyhwAjCcOc8DcwgdDVlAuz_awUZ7ILWLfu2E_2R_LQR3d2NnlRnUWaIzm3R-wVsgPYy_e-ix0tRGUyA05nrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1FCOz8T51lp325CdHV9PpEr8qywDgDGoOHgFkZgBLwhyRwx1WOp41rF-eqN0KxuX0PWZ_amOJlvVmuePm39mvSZHtiZ4G70qhSiD1wrLMpNcMUPAzRw82zrrA9NIOiKW0TuLUIyqNwJPqxToBDmZ0ZhbhbMCzp957xquImLD8roVMclVxa6w0EwobVPOZZjZoFlbM2GvhQkYIdBr0jaXarpbnjVq8o4tUjIMCQTt_TEtvcdQcLgZrXIS5Zbo7eZ64orfMiHFcEeST6vFho8sMxEDxuKk49DEsCprQJWMkNh9-qYmBDXDD31kluGWlANLBeeG2tgoFXvcgmCkPxjbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OxMd3IRQfXbItjzAaazDstNbE38y5Hbk7NqtZT0FhYEuWR9ssLGZ-xiLTxJL1rJmlTADzxpYXZGCMhSHBsz0_hye-w22x7M4pFDganwgsNx6MgiqxJL-nK-BW4GmSMlyrv-7L-XhnBpv4EdcUZ0AkrA9-fHwvj-HMdl4UxBIbTW3joumD3Nz0Jh8DQbuyuKgsWDTpGAB4bEMWgOTsFTpYDThJLGDTsQeoubIwuw7DSQlWH2b6mSPtF-VTLmjHeLik95hHIOqsjot18Kn6P27YRdBG_aIKQa1VNJy7HXlbX7KiFTohfBIodl190arHev6NG5u80pyYi8MvMVq2GoypQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LCagFgrMkQHuTRVs8XGozCyxgtowOa4Hx28NK8Aaot3EhGuJtFxmiT-WIszLKVVOdFl6ZC2E8zyvA8q_L0bOaQ7pdWbTqbQLr_0yiSpijGSjflrG9c_OpQbo6JALFzig3MICDUrUGnOL4jLi3nr6SdgtFqITPvPmTc1_cHXD6qJogA5wChO9hepQMCopop2Y5i2VunV6-wxSJq_TusKhTQWwrbssX-Sum5gdY7LssW5W2-ljNqgdyjeLxzMv79aw7L3zeIQQSUz51mh1gG_v1yle7OzvpbkwLOTqe8GYlR9WcJiGGraBKRLx3U_UOs1emQEz93Nq9uOkoL6G9LtdrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-voXx8DE1Qj307N3NkWXrKep7WLhgRZrpkExrosRWvPSWRIcKYZ-t1wi6hvxmnplyVOkzDoUX86z6FWRt82gCUAIi5hHwo9OWyLvX23J2oiX4JPnEeeZu3N6IlqEwzcZXaQogaCz98ZZBvJpzT7TH0xkV3hIqvAcFlYwytxGraMHPBnlGBGbb8EN6ImlpxTPgExMVf9_8gx5KcJA-XrKL7DNn7mnXBlojy4kt-ZCryrqO-ftg1hgxpr3-XZAeYIkQV8lWooBOlF1fDhGbHoADLRWk2xPh6joVYfviJrmpUyjXjfljko8b9XScTqdhjWbu57zh9mhw40OyzBneHhmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDT0ey0sWBJxOkBP0KJW-vRhjzmeGYwEyWnyEs9o0V1PVvaqA3TUVEYizqwLF-xfHK0VUSbA_G-t7iROYBvZ7VlMcOsD2TFH6f_E0ifHzPKFbl73SCK42LscDcB-TVAZzhTWdZ_lJ8PUOAjMVfsESQ8q_Lf0NJQDDVMk9OSGy2usQmaKTznOL9wnJA_uwh74rB8c6OQF5vA6iEn0CqNJrz6exF49H_wzAa37T-9EeqtPXU9CsL_GTNu7CGpT6BVzg6fAsUbq5UO-Mi3xpdBsJY_eh-FIbNRsSWPWP3tHg7MArSHVvy94Lgbnp7_7AnMbQQ5RNnHT3qXoKueL7pJMSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSmwEmjMg--912vJZbq5f1-NyLAbc5Zue_ESzcehMyQcEhwZpiKgb3EV02cGiBbO2-p0ajm3Q2CCV4fEPjuQ8S0xrQIwnnR8VQT9BgNvZHd6XK_IWk3jeC7mPaM_CpzkZUVJhyNYCZyIvV7VaVCuadaWm1pBMtyhudm4RU8NXBHy3zbEzBwLj_WRTyupdguVt5zdfVJ4cB-PILnADR-gSuwbJ8C6ZDdSZtMToIAwrQQmylgXxt0x-iM5bnNXXea8nZ_rjuvfDpu26Fhw6rXqFuqDVBGy9IT-h7Og6ag39nQwuUhrJ6LOUigK2yFfXOaTRc-aUutC2Lk7FwchK4PRtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xi7jUHKiE3k-p602zz_qo2vlG9E_t7P_z96al_Sr8zCeeL_HBCuNOWiXe0lxk5jzN08S2oHchOPIaXg-8MgIJhq92utoFks3Bvvxcs7g96EafFbDL3oTQrR2dms8HkbAL-jBkj7xavY0g378NtjyYrEOpxnWyjThtcdJgJ_PzTwUQZlxyQ3hbIBo0fY4EavAtdCj-aGwowGPg6v6ZNnZ1av6bEq6skCPHJSz8cy_GsgUovtxwmrbvfIqZA_51qzSWFxigB2VE9PagkR7-McOo1RDhIt3ttlCo46Jl84VGO4rYFl3fBeQusDwDcW72vg5WYFAHrYIfX4hpfsHJlTXUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHWj2fIx62L6tBkqJlnHZjgOy6wCD8yeXE_okDuWGHCEcm3SOLQIp-rdqkXmRbvCWs6_k2mkPItE7X9OX6YjDxf4dKZX2HWtrmJ3GguFpCC4M0njIE7lyJDT5fyCl-zKtCglThVqz6PdNvk7v3-z0ijqiLKcYjjxkkhYqJfOi4bOQr4AqlBnhnjNOSuyy1N4fo51a-NtRDwtHZlZw0wM864QwLTKGRMWA1kH81qke374bboqztJ9BFEHicz7ynj0_LNebAe0OL6T8HBoh7YBAJLsXpaIS2kNwIG0oHuW12sO9bykHDaB7Jn9uMrcjhXb0_0tS4tz5wwVwc72KR86eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaFarjeV7V1Pyik-5KYy8-jAY3eke18nkX4I7sBSyqSv7OvyXn-p_FR8s9PFAVe3ctb-R4BTfmOIBbOckfEMI2rjO5upfTqCSs1tRqusfrJHDrn-A3WwRfXvbtQFX81Rr0O7q9zfJIz0dDtW6fil8egMMmV3I90wzh7Twed5IEc-F-HS26JAX2sBlzsPVbJ7CFPgIzgpE3-RFPMBdQ6pVZ2B-e_PRdKz_ynXrJIBA9EMjx6gRdGzgW8Xt2SdjjJO-jLkF6C2MrjmC77kHZxcbdO1tN490TD4mds2hv0zizI3yqolDVvcvlHPx3Ro3EgUKS5DhoEFbZBt-WV-Ogv_bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRAO9JU7EgZH9Zdz9n52uq1TDVEdHDDhMwy448Wv8KagB-fsMHvFhGn1MVG2RPNYX_qHcm38h7qS4YUty5dSN3-VVc35rkPS4UTtbK9DSzuNQMK0v-PQeixBFnLg5HhfJKU9nVc_7Z9JGas5ylX3Q9pV7UQ8t9O0X2nPySwnASCc3XXVQCmjlmHnVbqJxeh-0z3OmKgP-5ti3PFG4-vRALu-pFYJ3Y2Yx3zeJK-A1bQ5gVCr-rfNWa5KDb7ePHYMD7l08Eag40cnuPrfXVfEQWnwyBkoieLGPJ60TV0XSj-SpwaDJEeNpXme_WWYIahKPCCIMKRKI9uXeYjlkc2rGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOlwlnHHNygoy8YrWMgme6b14ZwVhRCs-kSl1Pvti4L4aIzwzK_UyKg6YuVbQ1mk5E8BVXvzl9HS7HFxZr7tZ_5fr78d0Nplb70KrJjeCXnY-unY-6v0EdNdd_1SlJfKOxiKQFJjVxSVad7lB2MgsGqNjMAtDVEi_XKhX3BD6ymhNyWZSxcGHRMNr9D3IDrXieVcBJ8DOBE-tapzfHilv0eXk5ixUK3E_hiI2iHKiIYC31my33Fc0nnwJ0Ma08FzxzXFLNBZe3zDth0HoiVM4bzJOmzto6FrA87r2S7_6xehEc_3_7Cvc3i6OjRxw0HsYm_1menvgj3kxiBAvZpqdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lm-mn3ydup0yXL95bBGV-sgI6qN0wgZ_XpOB1wKDM7E_zrFstooL_tW0qswjahS1y3WXM3v6NEsKoK__M7bsGwS_fFkHenRiUvyFA2kX49tSsdgwbxSxti4tOH_whSZCqnJkgdjU3ZZYd-oO_MoRCbpRf0pV58R0WczcVDPZSTOs_S0fVGIjmDCL9zZycpBAi8JXx4OmTX3dkjxStr7ZRdRDezL34iDdgyU_kLaEenSLFVIsofMFgVAig5niqalfwRT3WPoPBn9lr_Q3mrSCGqRthk-pTRBc9fS-e6xopGVrmX4L9LtJQMV3gpE1GXwsbb2IMws4e3yyxuTzR_GCbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ob0uJB4ZZm6HiAe93xM4cCOVI_ME2ymWpkFrY9P6rxgag-8DPlCfWtvkWHTwTgBFMcFlW5bu50Z7hy7Ig8JCv82GGgEayq4nCX-0Baj4PMW4v_NWnXKqSDD15yf1T9XI4gl9piDA0ZBm-YOc2EBRSzg_BjJGhGnsedk2LgcRb6QXMQWxSIOHvy5r0HVQUnLTjIz9PIEakRttKibFMkdPGbrNfhuewCaPlbRAYfwZp_TgEEEUdmIxHc1qfu24fncKJDJ-XbyXEOxSKKFRURx0UWhgaNyn2imn4AGveCRndK6XZcqM2C4iyox56LJ8Mvx66SZNB64Wc1u-AjeRsQ8QSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRuXjQ5AHWHHClD504O4Zv3WpEYsOae_DdYBTFfsXNC86u8WhuY5UQVaM7yIhHK_fS8AfkyRUJq0_8jGQlVkQRM3XJzuvKwVir2JH0ogF8DOW77LNMMG8L-RNRo0kha6ogam8P3ROOIjpTVqMXBP5JegQngfLNWoDlVy_pRgef_2rToVYRqRm4bfxDE6j1Wf-Xf30kUu_MaawLqw9mZAlsZ64Fwmvxi2hpuUMWg5MQPjVThNybq6ZqES_HTwD1JSTSFP8z7IdTnZRKLzRR22BvLDyhSKJIytuU9NMbqrZmMvpAPoauttoTDa5rQi-FdaTJlV7Fs2XaunDpoUlgG9og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ruipui_o1k8ikPFWbhCGeUSTt9v-PUbLBe3vcztc1tBTRoI1rJdX71m4F-CG6M1CHmjxy4S7N2ljNVyS0RXU3RFSPMzD00iRCLvguse2c3fLJH44VEAlDUCgWPMeczkTB2vaWkc9GYjAl4t-jsSoJK0nd8pY6Ce3WhBjMwfnisZVaDRxEAPXLqp2zxDcXF1eF-lbkES4UFXM6a3ewtifcJHrxY3HE3ItAuFZY0SOIjpzroiFYtLOLxG_pKKguHbe0ckQKzRdaCLeXlbRf5iyj0HdSQMxAACEwkpVkvG5ymV_6zJyE4KDw3mOyrLnEsQWXaQ09ElsUl-LDzx_CVt4XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAFz1C2qof-nJbOK8FzXoYzQ0qAeR1z454x3B_TgFURSxe7ZKvvOUkRpWcgY4fXpJcqu5D4FNohrOkiXK9j8J7veTEnuVNYeoGlaK88LDO2e7bxz6TGEeRkKgRy53rpvBAtOAGJZZEuh9BCzQ86dHfr01wZJfQ83msjGQ48vgiib5vLM5aiN3nGPq9L00M0OSiciljp3CCoxHcEXirTZoGFpfK1kmK3T_dFh7hmSOgNhG0yyWvSWaAfbnlnB7JnwNpKfHxtG5OvlVygafJV10Y-OipH1zAvrbrQd3IKek36STIcy44DbWuvo4c1llhig478T4cHRv4iYCLykmmvFdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPj9gb2yEyJOV4_cqX0C46h3cixp4TtkLfhoWL0QnhAr_5O7Q-6sIcTJM2ESSdnb6IoK9JCXfq4THXrzjqedTqsagW-HJFKpfgR7UrdA4Sk9HSeyCSsgBsefj6wtv41whqzcwdF1KoKxZgYykV5SkR6bMq6UtULeQzgHDl3V0RY9Tt25FKhNDmWJnpQjv_LHfNM5pTN559qkBxCfnIYrGIR6G_KQc9Nn2UT2wx4IL04BdavSMboT1SlfPnasKjWeDptck6co7cPsbhOAeGbCW7p1FSvfRiPiQL8aFBlNRNkfhm6pI4CSDEWQpJeAneZJDHy9UuvczzCCQilkCvD_1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgBbTgyvJoDtRUPnv2jq46UFrZD11LWfO99Z7IV38boLqp5ypBIfgMVDy6Lu_2cw-sVvtiMsniK2rojIIPFrjJosnXaBClI6vn17qSyKmmAp_dViRuWVsLWCHg55UtCAn5E3c_CTl0oiHnZ_9G6X5U1vyC8bhInGwAaaO79s7Llo8FSasKuyn88m02js4jEdLxhzBvMARxNkAfPnuvCF4So6SQ3gpN5PDSyw_6V5RTRL-v4mWW9GePqcnV8U0oGGYy-rJ-bk2NN-o8Bj8OE8e24xkIV26sn86PcSq1wz7_A8MKbnNRD8O-mm0vFmMNoPAndlcej0S7pir2HQcvJTXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت.
ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى،
چه كسى میگفت؟
این حرف‌ها را مصدق میزد.
مصدق حتی اقدام رضاشاه در آسفالت
خیابان‌های تهران را به درخواست
انگلیسی‌ها می‌دانست!
او ۱۰ سال پیش از آنکه با محمدرضاشاه در بیفتد، یعنی در سال ۱۳۲۲ ، نطقی در مجلس داشت از آزادی حجاب در زمان رضاشاه و تغییر چهره شهرهای ایران و آبادی آنها انتقاد کرد  و از جمله گفت :« رفع حجاب از زنان پیر
و بی‌تدبیر چه نفعی برای ما داشت؟
اگر خیابان‌ها آسفالت نمی‌بود چه می‌شد؟  و اگر عمارت‌ها و مهمان‌خانه‌ها [هتل] ساخته نشده بود به کجا ضرر می‌رسید؟»</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
