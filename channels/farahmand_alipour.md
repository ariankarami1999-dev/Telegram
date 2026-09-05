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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 21:59:09</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEPvNPKmo3Y3Dh-7BN3AfgbMYIpaxh6BhM89BiSaGPhhVVYRt-VswWkRfURY6IhG_eWCcfc7Zj2Kg8TW1k27pT3GJ4gF4oZGC7hrxaQGx5-xK1ZZQz7SOl_Cjcb7QI0Und_ThoDCp_ebmGuuWyejZnlFjxjLEDrFwiK7oXYEwh2X6jHQWdNqwN0Pner-oBAXEgwFlCvti9tWRGbckm5KAMNmlhMiLbXjPQLgk7N3Vm2VX6AsyLvsPGApgNg6VoqGd1gNRL1iafTgiS4x_ogGWXXNUq3DepMx1DfvUdNHQFbvCjivhexaZ93_GkLST0r-xMZtPHfccYOT22sZE3ynPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbjp-PRdcEWORyoBfNoYsRDrz0vP-rOqtOJmksVDE4lDrV29CQGpO5Qg9EtsZrVfHafO9Zcdw3MTbGiaGjAWjBiAU-m2y11BliuHFPNOxrABUSp1EFP3BdNEzTZuO5bmrsSgwcNvHyOOiaHKieX_w3WJfEpE26zzjh08wjF8SaeNRDN-0vuDkNQ-FkphK_MxSXZ1qFEB7uL2Sa5odvQQxtKGmptzYGb1G7BFxYiDliDK7dgHEADwPNtMOootKMvM2qgtPxEs1OyHuEFiODy900Tya957WDph_MgJaAAPDKTvzORzPHTq16KV-AdsiIcRqnOgGc_l8NXRt8Fa4OijxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-3NE_E1m-shGhebw4sykigZd2YZSbcDkKsyQ1Dz5UvBQmi3CqkT8E_0l2etZ7mTbQM_Kt_7tZBEAL7_G7y4SI8KoJOtezay4VmWvjv5Z1yhJv_aKO-6eaEl3wcdyKA15s7YW6_FO-_abWD2nT24w_XXw3Gq_N-OZI288tcFhFaiko0EBtCYDkEVi_e8t2BoaYhxKbffvyN50O_ElpkEg0nrcuhnEmWlCpIOkFjKdBYmHz0Jm557XvFzhET4Pf5wHHX_g38ZGaN5L7l9y31Rt1iaYnTAYkSaqShScaicSsoDsiPtgDP7wFPLbhDwmw9vHl6A-RYCLzlrHJOdM8GqPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=MDJ1gLP0_BHuNRHkMYq5cbb_bZQpVGWRNfgXRzE-Wo8PEImKJHdVSFHhALzMl7xWlDbcsuJrqz7dmz87Rg0x3CGnAjApl4Rdl4G0hA7pjRVLFE3EKEhgh8Jnokad7m2zVF9KaHbuesMDK9Y0MVg8RdvE1SUgYUBX9nbCtCT4kF-yNL4j5AaiHRRqtt0VBzwtZfBh0Svvqt58r3933lvWetQqI4eljVTWNsuqG-v4sbfE-b9PE3PncXIc9YV4A12tEH3S4We0J8LSwC20iZ5ZKrqvMCNbmoYkQ2S8SghqWkSZVs--OHuja0EukBXbsqRZLqAfZ9rc80EKJHt2WfnFiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=MDJ1gLP0_BHuNRHkMYq5cbb_bZQpVGWRNfgXRzE-Wo8PEImKJHdVSFHhALzMl7xWlDbcsuJrqz7dmz87Rg0x3CGnAjApl4Rdl4G0hA7pjRVLFE3EKEhgh8Jnokad7m2zVF9KaHbuesMDK9Y0MVg8RdvE1SUgYUBX9nbCtCT4kF-yNL4j5AaiHRRqtt0VBzwtZfBh0Svvqt58r3933lvWetQqI4eljVTWNsuqG-v4sbfE-b9PE3PncXIc9YV4A12tEH3S4We0J8LSwC20iZ5ZKrqvMCNbmoYkQ2S8SghqWkSZVs--OHuja0EukBXbsqRZLqAfZ9rc80EKJHt2WfnFiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szdW39AOqUPaWZYeUizdKIjcPhc04Ms5b_zNT-90XyPh2tCvnaSDC-kcSCyKcF1lgfUO9WW9iYpXOFJat7grr_oMgTVqXcR7472mJNXW61zYuu_MPiL8mRWsKSJNtELYzXrliEQTwB9Mmd5RoDiHBU-nV2TGkciek-UjspGuHZBxsdJU4pn0g1eMVB_HitDMP0o68-bt_4FPCMHGSSe0BJ3CpFe1s4KGnFO6tlGSaqcXagb2jml3BpNqUSfYAUduJfrU4-HSn8daURiBrN2eMnehOiOOhXW1hUSVRUANB6JIKpMFokbzhyE09gMQZoiUCCLWGTjVPt5zvcfjB_6jKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPezdsU_hFFgawlO0KeVI-GLcODr65bqzuDQomClvsgV_BIgKnS4P_ctmdYoN7SUHdzzzfSWd7cZkuUJV5KhWmaioYxpTPMHJXgBLne8VX1ZG2TKxlI6ez4L7U9kvtZLSgvPqreXtZgTI8CwsDfriiWfp96yRLGzjUOF2T2dnjaNklkz5AgJB199uDleCt04P06WHhXoKsg8zDMiX8mLuNlJx9ry4Ogj1scAQlmhO6Q8nMInaDELL1jRTtLZsURCvSpJOHMG4THVuX9SSBOkr7tslaOVy3Lh-i-rF4AiBiIGfrKfbVHtXz6u__5lYWkpQ6TnmWGoXvLwEgkLCmO2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0kol17XAY-8sas3MGB24Gkv1ZiWONbnBTg0NFsyPVbn_qK09P9wGB2aJbwiJLVvibO7W3rspX91iO2cFOJyL_a4HHGrPF4fgpFl5epUxXM2xZVD3VTDXpm5i89iCTcHfMSU8yVJSDSV4zxLO8fFCQD4lHR-bQKl71M9XRV01y2Db4A-Z7FW-BW4X_JuRp0c09uNiHqZp3vcE-7PZMZQhJCzV4boCTo1xQmRNNpknF93GXswM1duerzd-NMUXLwGCsmPNuc4xwPYqdh_st5_BCnzv6XWbd4n2iUM5s7wdqrZ6vwcgH5Tl01jlxOAsBsl4ALO0IXr57F-Oej6m3iSUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2l_3YZelAQzAwMrqzugI7_5qsXGI2Sk3n-IHNEl3j1b4cz-qW71w6e96jNf_eaOYDRqjlBEV0UTWNTI2EbOTHtDcrEeqVvH37TIkwPtA0kMDviVMdLJ5wALaATgV5esAOil-6GNy2vfBH9ReSiLNNdXE5qsaHfMAMrYy6BlPD65sSmAsnQHdR8NRRGdYSpM5VEtUSOnJGS2FcFi-caMTa_NzKJcI8_H97QU9CKx7EluFoTtWNaWhQtM90XcvVoxpU2mMvzfw9pWC_kJGvYZxeQtfl00IpdFyrUjITA-_lO9plxTPGtRh4laNR3OM1d4EuOeVw2FDlFYk0Mt-2e1-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFsd1451O4GQ9xOCR4zMFxvqs6T1k8FTEeWV0H17ee-7C_ogt4x3V0fv-AJh89NWRcckCUdm5wQ6rlEQQi7_168CoAw8ZxqVUGnBDGKNt7ADIahRb4MKeXDq6Ag4yANJdFD-nOjPMIcPWqFn498sxCoOzOPnweYwUvCJQkb35z1k2B34ZaLpZ1gD_EzCzKizBITTByDtZD0csdQSV1IrmNRV1kZAQZVhWo5TSryOh-Z3KhWmTfu2LY3NHkXbiIh8hdyCAiENJiDvz_cH1T8OKfzugqqHhm3wVqLYeFdNJPtATgU04hcl2hoo6FFKn14Uc8YxbWVsA-vXG8m02w7EWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdlG8aN0e5uNjgrcxa_GdLvdlHpt_3IDBDsOM89c00bE3tcZX_rCzAQR1V9aFB5AA2-SfU1B9ueqJJMXG-ADaFHEOXNVw82sLvJmQ6SBb0bZfHQylxn0eF3PgvSNIvFUb76IEGzhJcE37KS5aPkXbKF7-s2Zrfgo_NtIWUtLDCB8bb-SeZqOyX806R1jJwgHE2nqqdI3oZmjr7Pv0bCsou0W6_cZmtgd0xysXfqwmuPgFINBrwHMMtHu6O-PbC_CIfexLSKxoYz4S2XCi5opxwuLF5YRNu194q7NoJmMoPvwbkh20qPK75yoefEwJ3msazOeYkCbhZJIfVK773f3uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrqxH3xL0FMqKmKVVFO3udxkVxbvKJcx55djaSMHf9TK2kaV5YdfZumhjAJ3p2BZPFx03qM0RzDkKETClpI-W7gcMsvQtTycbIUtg35LQrd1BhCi4dUVpX4Dhfz0dyFSCj2wLWT3TdvzhE92A4px_2BR0RBNiqlQVOvzWG2nCaAp7BH93Ly6oBk_bgfQXK5a1H5BfXAQNAcpO2_LSVImJcfbEjwwMt-RaUPWH19HdIjDOlGm-H4drNbSwtlzFey7qT8L_0VtSDVh83q4eOaJ-5sPWwmUDFUIOkYR5DHdsFZ_Y_ASL0y41b_PblwzZRV3jCyq5jHJm_BzB8rBJgE6GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UagK6MZ_W6BUh3sHQL9xU7I0EsI4Kxnwo3WVkm7435X8hnXpQUAr86ggE-2FWjz0eAIv0bsNNuY1vMwbayhb6YwjywBYKAuBlmJfPQjuA-y4aXNt4K7CN0lCzXjTWkhNSz32-y9pYCl9CJac8PHCwbXz6RdDedxQrqEoKr6N2qRH4-U9QGxiTaxc5Ks5lsHqoGWRSBt55ukH0d2UihjWZfeEBJuugRG1DT93OaIOgi8gP6pVRnezmnbog9urvuY7KyFL5jylqDk8BeLfIPVTSLPg_T19OimHiZoYG3oQbBi340exFk8gqZPcRlx1URnXef8_BtDmCEIOEUkuQV6Sog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/noQcz0CO_EGc3ab_iC-S3ItROCgpI-XT3bSuedSchHnWxd5PIkRgKXaKHWNHujgTCO2KoBC1Ex4icGK0jEZSEoZ_NpBJcp6Thr9UeRl-8ovdguRo-cnL_z50d5fUjSBdwdhzxNNXphCbkW4SG9-Aa2cmPOsBeXp5AUCJbiIbaWpOWJTr1m0jYT0q-t2TXKmlfGX6xReb2qBUTIf5xczkUnIiN4ygfOFAwPKTy_XTcpoOHFa-kE7rUjuvNJdSjdA9mjov0HPAmfp-Qx-B4irLm1rco5OpMSIbtLdIHJ083G3lbQFHYOXeTJl37tUwdnN31warPUacFMxcwiJHBGstZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HMp8_j4ekCYztr3edsI9FPMURHb3MAOXYtPiW9Li52TzZ-reEAah-Lm_mB9pp-dGLpW2laXaB_Bd2vxOr7vZnK_t1JA1f0gPtq30v3gzmJ7twqVsjFiFUuNJy-yMWeatAHwXL9_TPsjCkFisOn0ePANBBQDuloINbIGAh939bQlHfHLFH3m2D78HzDt56DzdcdMwUyEEKKl9od32yKXMM7XUVwxV_AbFqwb0dDpIT3vLN169a-d3VGDhmZwBTVzzW0mFvsBz0cmPs_HAuQLbbm3Vpbfaa7aZGMvALk7jsKhy9VJiUMKdvqTf-Kfr7yx_Y4-v1YkmJrjJHVoX3vlCeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sxabVmC6Izloc2Gow2O6gON7yE_qGfZp9OP4-eHg3plQKX1ZTd7AvZdwX4ZrfBTDYdzNOnuPgrHKShAam4fk0Q7AM7_qmQRmBAWG_0e7UvIzVp7FenyKgNRG7Quydb83vCyEcWc4SbUpkFH9ovETziMslpoyd9COijbIR5kcTXoRF8LRwLWRT-WOd5BXFGsKi2n2cwEHdCZLElV3Seh4d2xN5A_TAGm2D03ZMINSsA5f41hKc99oYASQacpV9Sc1Vt-9B2nCd3Ozv9j8pnlWoPKKzOgnNxVDrZUcgEG04p-nmO04-nIHp6PtF5mTPy3QGozLm3P7qqpKSaBqBos37g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=aAbQ8lT4h51CxMBOGG93LYZ8lfgWnTdINlYactktZQHrwgr4xSXxs11Y3q-hj8aYYraFMySMrNVN4IXM5qIPk-wtS0lP77oGr0_DczQzAUjvzcdqXzprB2nRR_Ps_malpnSMH68yYuao3XRk3gmkuvOUUCLI4TOKXnB4aZWjUfPCz4UHRBhQ_9CK0NHeAM3XMgecOwS3fEAL2oJ7esJPwECmqltMsIfBG8g_yhtEQ-eYWDcVzjeksaVvcDDrUHxtlF5hgpNySpZ3y2O-mjMMfRTDFpDHt45JEAH_uKjK0oskRAHA6YkUFbZdeA_slqkQnAbNiJFabx_hpLiAK1n00A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=aAbQ8lT4h51CxMBOGG93LYZ8lfgWnTdINlYactktZQHrwgr4xSXxs11Y3q-hj8aYYraFMySMrNVN4IXM5qIPk-wtS0lP77oGr0_DczQzAUjvzcdqXzprB2nRR_Ps_malpnSMH68yYuao3XRk3gmkuvOUUCLI4TOKXnB4aZWjUfPCz4UHRBhQ_9CK0NHeAM3XMgecOwS3fEAL2oJ7esJPwECmqltMsIfBG8g_yhtEQ-eYWDcVzjeksaVvcDDrUHxtlF5hgpNySpZ3y2O-mjMMfRTDFpDHt45JEAH_uKjK0oskRAHA6YkUFbZdeA_slqkQnAbNiJFabx_hpLiAK1n00A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8lDgO25TUHO5RfBm3-NBC57j1SASr9JeQBAMnMRWgqQNai6zVleDvD5CfCwnMA2FDzlO5zszqk49cLrKKYEffMDXAqegESzP1ltRrdPHOkiUQWTZ0TRHuxRayiwLQUvvsSlfSNGOsOPqintqp9GtMbyFVCli2R257fiY3JH8X7mLymzGwhvNuyayUOPDxUUc0czK_Es4VoZSF4NTAEDqQ6jIwMnKfMkQT7daXUqVnMKa2lpzq-R0zFaQNLjBuO7_t-GhLIhpj9Dvi1JP3eAztna3C5xV2EivdgPp44gRtMFrNOjj6UO_BKE9J3UMM3yUVXuTpwc7JP-glQCe9oQfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_2WCaFB4sIRcOoXRfdVCAAc0SwJiyhSow4ye3Isma8Ce3oggVWQU4dB9SuDETshlNHoJC2HweyTXOVurZ9zwhFnDhDv5in1XuKwNmSCHXv8aHJos6-3mnyLpH_7nX3BPFtOiz49ypfY70fR_CbnRddn5pE00n0Rqbivx_KQl_pZ-iNjP1fIr8zNHWN-DPHlQVNLju9DaHcP64Nyr_QQ37-f6tAbFiRCZXT-yfoh5YRTEbpqfhbo_1Ys0hYigy-lqEPWTNhNqAY715FgtIwsyKl0WqU7MA4JTCLdkUkpBfCym_SJfrsfLW2gYN28pliJxVFadqVPKhbd4lToJqVbaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=gs-N0c_eFp-fgY6DPiPLt73vwYmkNP-nDsJQq0pUZrYBh72nu2G8P7ZkaHL6ZMGRcGKUKvwP8G-J4br1WPkAUiTGe_jBVINZ5e9UuA4aYrQDNvDl5qTbu4XlyDGFswkR3NpXMk4Lmxfz3prGb_v-OP0TQNf3cjeqvzfYW6_pwqIdoJmRV2-JP0GdwXosjsnTOtLe_gY0eGMCmCQB6ryWePFpWnE1TNGAiCkozC0ymkafSk2tIWeZJq0T9dHIIywuwVIa0VSDFYacOYa17NPbeCjD_Cm-8tFA5uWXn40553eung65A1yr68RMQC_IMk_vtxXk_NHKbTtOuDM8Ntorpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=gs-N0c_eFp-fgY6DPiPLt73vwYmkNP-nDsJQq0pUZrYBh72nu2G8P7ZkaHL6ZMGRcGKUKvwP8G-J4br1WPkAUiTGe_jBVINZ5e9UuA4aYrQDNvDl5qTbu4XlyDGFswkR3NpXMk4Lmxfz3prGb_v-OP0TQNf3cjeqvzfYW6_pwqIdoJmRV2-JP0GdwXosjsnTOtLe_gY0eGMCmCQB6ryWePFpWnE1TNGAiCkozC0ymkafSk2tIWeZJq0T9dHIIywuwVIa0VSDFYacOYa17NPbeCjD_Cm-8tFA5uWXn40553eung65A1yr68RMQC_IMk_vtxXk_NHKbTtOuDM8Ntorpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=YEOxzR_yS8UcgxweXMhmBsJjlQwqwV0oyQpjIgIq11VfBMrH4xMYxMeKkNHrq-Su1cD27oo1_jnO5L-8IHyXLHXX54qNY5yJ-PWQtrVJv5JpMKybWwoHUZGyHygmqZ-0oOh0sijP0UwwCJJWzCUEZvDc3b0kfamCLIu4Wtvcb3wHxf1yP62Evz7QoAxk_marlfuUd1Tqq5nz3dPff0zs58vnYYcs-zYt3g8sYDbMiw1SsOHDRsi9Rb-M2x1x0d_KvfX63PzGqumdDOk0YKep-1gHsTJk_jFiZcrFWG32eXLd2hV4PzsNOSpoZ5Zp3inOSuHutmEs189B9lqGKk9HdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=YEOxzR_yS8UcgxweXMhmBsJjlQwqwV0oyQpjIgIq11VfBMrH4xMYxMeKkNHrq-Su1cD27oo1_jnO5L-8IHyXLHXX54qNY5yJ-PWQtrVJv5JpMKybWwoHUZGyHygmqZ-0oOh0sijP0UwwCJJWzCUEZvDc3b0kfamCLIu4Wtvcb3wHxf1yP62Evz7QoAxk_marlfuUd1Tqq5nz3dPff0zs58vnYYcs-zYt3g8sYDbMiw1SsOHDRsi9Rb-M2x1x0d_KvfX63PzGqumdDOk0YKep-1gHsTJk_jFiZcrFWG32eXLd2hV4PzsNOSpoZ5Zp3inOSuHutmEs189B9lqGKk9HdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcXg7Pb7sk_mHh3gUk02ZD4EORgVOFck2Gv8etdCQTb6bRdySbiiSUEwKvVlwJt11y4QLpHHAsWel9-2vs2dPVU0xd84SjG70sDRSaSnCB4sGkdCJM9y3X4XhkAAavaW7AWa_zOl-dupIh3MHtQXWj4rX_UjyL3QTBsfbac2TtHo8VdzqWXiB5NZBu7lFwsRtf-KN3bWcZmTDrUoTfIAH8rz4Pb0qBPAnoZbV6HTa_vA-MOAn83szmlc25qsIFqQ7ZpiPK4nf6tgsNvunnVd3WBVfZs_sGI3EA6i6TA6XXmVBuECNsmnNDopgTXHodJOgy33alLt2AaJspEOnoJ7Sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNq_bg8Gr1-YJvzReTMuc73F4Jbh8DrHKwvvJW-M6qAZshHhk_wjwyrEowHMwz2LlG0Bsm2AWjdkpsf-pzlD8Ku3U3XzfUglvQ-DuysI9n95qxwnEU7R6bluzaoVs9VdgWOdwVPrw3x49SN8h5w9whrh7El4NUKEekmsHYfejfhCjt43o3VCYjhgWQWMUV6V8gAxKWDdGM2VkZxRIOKz2EzL0TqQRjM6tybEeo15rVlY2x4ohhN3E83YygcZbVovMd9BzF9ztJ7yiLNfeaiUsVRd-Yv8FxRKVAJuDs5nTrXvxxJP_CDNhAHqHqmBJHAvfrZgfvg8r-7VsxMgA3jkbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_BJLBWyLS8SS8gyvZcIXgCeyTT1iHTKmlsStNfgO3E_anxmErjzx-Fd5vgu4hjvGtJhgWSmlU4XKkQiIgq-MlHFwQ6fjQsY_rQjhP90IRsf1ea8r2NY_ZstzwKYGWdroEto3A2TaKcbpUszIK5tLriKjz1Ama01k2U9C78zY_Tt35SmCiZPlZWu7ZIyoxk2HyVtunuk6cVAgSe09kL2Pu7EBXcQxf-92cWWAb6yBqEDnK9PllVs5umkHI-8pIzNdhCGfcuBAXgvoexnAYX9hSzDtN38sDBRplgjOL4Z85cK3QPBXz97bm5izW7z3JNK4c9f6crT6S89re7EId_cOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6eACGNe3JmtKrVSWxYFNBn13c9ohZ6O5BeNwS3w_OS5-e3HRQbBGtOlobAekfxMTq8PMX29UEw_80hWMC4uXWJQSG7W5pugcLGNd8Db6cGejZjbXNm733QNjkWPdP-rtMzYFMMO0Ivs4cnmXjnFj5m6vSkFsd0W00py6zpB6KW1DXQER_eskK38velj4xAh9v_8xcmvB8cRKAfgMp8UJxxOZH7jCVZWjJXWFtp7s_vMsYLYhcjo7P0dfGxf_pho3cEnqFclFs_qIgvz8DTg2X3pf7UbhnrcZTq5qydH_Qx4s7A3mGjm7We_MGmF0BLDwGAsgN60T4Rh1HcWTBbNnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQHTkjbm5FgjzNtn71phYJQDoK6AHmZx1q2GlIcrrdbn9CaVcoew4kf9xfgszPw-jnE4uY2AVfSWMNMmIenyagQeubUO1LtqNazPCowMeSB53IlYXWMXcDC-aEqylAT_24Db0SInumDsbSnBBHQ2MICJrnf8cQNiUK-jhZIQq6BYZzvRj4q14InWl8iEYLs_6_ZmoZGJ39sNRhNW7IaD1tUYlGYp9XHNaR9hyqfsvqnefa2BQsdKD07rq8SwMxa6c0sSEmMALGKXbhNxJJs4BBLox_nZ7FGfjB0heuJeXvP6trE-hpW6hz4-2qBeJPSjmU1J39urgGU0PocRpL2UVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILyx_y4KKw8xHahy708wDCVm7sClSKEmsV3tk34y_rGmzYMGfV-0xwNfuTvn3KCzwb76GqgbYHzDYKFcAE3nUsXEaXGLOBH8qvwTYjto-8r99hhKfXKM2jKISHnrzMDYMgJNDdXkuYZV4rhOlJV1iF4x8flElGU0YyPcmjck5E1NPC713KTbLhV-YIBjRpLGPWFbP07zNmUvYWOJh5OkiB_owv4W1yJkAOBIMt48xCHqINiakEccIcluT0ds3YUSd52k5AkTdfKymMsgoR4wx3nsWNTUwuFKNjoHB361US8quOfP3G-TZ7w15Hqc6U7jhIE9HEKeIcYAPcNYh-s_CA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=aEcA2K9yK_FFw0PmjYrPiWNE9BB2ktedReQCnnkQhROSfGeHlYsfjO4IX8cFHHVIQdH_yxL-NKN5GcqNG2biGBiEaiyjPdI4D1g9m-oesP2zBDOC1yziE6oYfqAzcMJV1_zMaQ_MkFSurRUnAGj3n6HZ86LZVs25fE6FzTt9JvdBQMskgraUVyVAmPp2VQFi2acmDnDHv1CzYUMmWFBV_G-qtgpdQD_bBe5JX30ZysoiJ2tyfrYg0EIYSYeyxYtySPSq8eUXeIzioa2KwoNx7h_oDK-fELSj3itDZBq15EjbkcP3U_ZW4IZuRW71FYQ5u6qKcyNwtmjCvvi05dnRrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=aEcA2K9yK_FFw0PmjYrPiWNE9BB2ktedReQCnnkQhROSfGeHlYsfjO4IX8cFHHVIQdH_yxL-NKN5GcqNG2biGBiEaiyjPdI4D1g9m-oesP2zBDOC1yziE6oYfqAzcMJV1_zMaQ_MkFSurRUnAGj3n6HZ86LZVs25fE6FzTt9JvdBQMskgraUVyVAmPp2VQFi2acmDnDHv1CzYUMmWFBV_G-qtgpdQD_bBe5JX30ZysoiJ2tyfrYg0EIYSYeyxYtySPSq8eUXeIzioa2KwoNx7h_oDK-fELSj3itDZBq15EjbkcP3U_ZW4IZuRW71FYQ5u6qKcyNwtmjCvvi05dnRrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjLlVtDQP17RyLBtYDJp0y6fS5v0L2qu3MC2WTHxM-VXoiPITyg1IcHKDBth8TW0hJ1A_3SwcfhyZPRKRfpvSACUbLldxfQvoaivAMaAtvGcODZt7F-P_kUB7gGZU7R-3O5mJgYZLZTP0CCdxKh_ZQ9m1ViF1UnHyk60ZiSeyUSJR0VGNcc3KrrAt4Bs-GItSHy4IkIh2ITvhRLXe1BLmiuC8Vy0PC95wjjUoWEe76Ke48WwBdvHvLkPwzTQOgBtM_utFbp2yjIcx_t9DrHINKc4Yxrc5YUzTjLp_iZCnX4SdRqBtD8WfWwGXujSFeFooQmyt9s5Sj3bziLvoew81Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=k5MaoZ2G2qSeXlcKodBAyBj4Nws8DFs_4WCZYsDpD4xr82ncxSzjLrjrqCkwC0q5kAdOVIVZl03Y9trrz8EQes_X1qA9VKVggdRDyBRE1_p3-QuYQbQ2TsoEdmGSiD2qXvo0I5I_Dt9zkcJ4buEBNZ_wo2mvuLtICYkjmqVbMxM5A1JbK3OtYmcYzllupgJXzRmHql5wl8qrttQ3-q-xM75cLj5qGwrmPsHKXABkyoP5vP2CuSVwmIk5_IF5BcZnZk1THlcKQyxhg5RR5q6NuetrR_on1NQ9fdRSWWWobnHDdupFc1mYzV-s9GgxD6oPR8yP8mB-EVc9KkyZPwWytQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=k5MaoZ2G2qSeXlcKodBAyBj4Nws8DFs_4WCZYsDpD4xr82ncxSzjLrjrqCkwC0q5kAdOVIVZl03Y9trrz8EQes_X1qA9VKVggdRDyBRE1_p3-QuYQbQ2TsoEdmGSiD2qXvo0I5I_Dt9zkcJ4buEBNZ_wo2mvuLtICYkjmqVbMxM5A1JbK3OtYmcYzllupgJXzRmHql5wl8qrttQ3-q-xM75cLj5qGwrmPsHKXABkyoP5vP2CuSVwmIk5_IF5BcZnZk1THlcKQyxhg5RR5q6NuetrR_on1NQ9fdRSWWWobnHDdupFc1mYzV-s9GgxD6oPR8yP8mB-EVc9KkyZPwWytQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=N1lAWamepPxqKoSyadghyASGfmOrtW9M2oUXR9Ni7g1XHGB44d5NTGonV7u1Em5eyaKSdgvz5GDWtefshE9OANGtP4jcn4JYYqGfOtxcdukECE-hdSYx2tKyrIb1oPxshKicdGctfz663Pm0pnJ9ijYPy2gYur_Vpqg8HkVGfT_w1wpbyFLfOSXVMZ-15oTObS5EzkcRAAnK0EVGJA30f5AHPnP7e-HspyuggBrttAfAj2HhZZAkzHWjnvl3tmv4YeOxA1OH9D2VYQBMWbvr_OM3GTdqViOKO6XfNnjhUSs12OU5bcQEnXghyMs15JS4xyCODQyEduf7xd71s0OmmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=N1lAWamepPxqKoSyadghyASGfmOrtW9M2oUXR9Ni7g1XHGB44d5NTGonV7u1Em5eyaKSdgvz5GDWtefshE9OANGtP4jcn4JYYqGfOtxcdukECE-hdSYx2tKyrIb1oPxshKicdGctfz663Pm0pnJ9ijYPy2gYur_Vpqg8HkVGfT_w1wpbyFLfOSXVMZ-15oTObS5EzkcRAAnK0EVGJA30f5AHPnP7e-HspyuggBrttAfAj2HhZZAkzHWjnvl3tmv4YeOxA1OH9D2VYQBMWbvr_OM3GTdqViOKO6XfNnjhUSs12OU5bcQEnXghyMs15JS4xyCODQyEduf7xd71s0OmmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQJgPgZ6tGEosMJRjNn6ItpFbtNG5tNqgDXd2sAbqx9-wPtb02o30y7NlrFsNGwRng0ztsVA6QFDKL895gPOembh6J-ZIZvfEwtvdcuJtySiojV680FxYnOM5_6z86FLc5jLTO8xq6l-hXw7yO7333_wv3_ponMSaHxxpGgChsSltqnEw7MdnPDFv2GtJyWzTz2XfMZPS9Dyvh2h6mXueX00GEI8cHekZjYGjXF5Y-_nq0WgDNOKlafmByko0M84Fx7h-6LjsekJ7wnJxegfdkPwAiWGtSXAsVyEfYWtqCwADA-Wh2_XJpiaAjsTtRzLuNzBYmX4OY5qdnWff4l7mA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQTOYSQN7shVsx8SwU3OMUwck7q9Pxjw23gVD7DhnzaMN9Dr5kb8z_TNTUcFluhAyjqiTBN9Gok4fGZuZkf_5LtBSHjfBvxrrXWngxYORl4-8yYbn4mw0SeD0BWDqi_tzHYUE3FIve61EJjGX9nWGJX3SuxPipctslMphrCUYOl45yrtDW6duOYy9AZTEp_Lw1HQ52add7Fdcy8Zi5Pw6jOOq7WlmhXrSSsK0jiYgKMkuHqTuSrLgbViW3G1Nh1_ZW4NQFIggmS_jY_TKJE5NBsadmHiG2Ax-Y6l1rXl4ay7UDW7zpQAxojT57EoCyjXwoXLz0VO25b_q3aH-9bkIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=q8ClBqDY3IZ1Ib-r_MI1B1ou6AQzg03F7ZYEhB_-9UZc7yEJCqdOSc0evGhYHIrT4fclPtKkqflU4qQEa0VTbH0StmX_MsfVu4Qx2dW3j7E2yoTikunXga7SGQDNBhjVMXURrNq3lWhPdCMMlviUCLLedSnccSdUMMexAhq6QpyaRWUpheZC4MIKj7LbZtpLcpIC15jdbh3FtT6OXd2Op8SXyWr4MHWIkrViN7gOfkvDlnf4rakPe0FMcBtEHHqMRTJRIznqeP3_1Ra7dGCFHpbE9M7Mff8nrAlvVl8goB5SaJycvB5uwBl5E6x79zbdZXaot3MX8qMjt5BFF4LcDlDYiM1c5PXQmJ7EDugTjXffPVHLhf4SuY4hdFlQ5ixBjEUyfsX0L02IAn90wWhhgOnxTjQ_qLKWoWgM8UFyipbqA-hzkoTtWT3ajc8zriqP17NEamRJnHz_xvJN3VQ4cK3ATxWitGtLhHsPfHkdl4UYcobch-I_M94XEfflX97bezGdeYgHfJkNlZpKDneB7BK8d3tCNh6lKnRCy8R6DvTSknfn3gRbq-7rC8ZQ9p7XN3xY7PqyqH_96yZIhlAMikKHmx6_ZMeZZ1Shi0eSshoF8V2p7cXbOjQ9Q-H6ZXkAedmnhZIXtqBBlb6Tw5U_6oBaqeZXweMaNtB2XiUZYW4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=q8ClBqDY3IZ1Ib-r_MI1B1ou6AQzg03F7ZYEhB_-9UZc7yEJCqdOSc0evGhYHIrT4fclPtKkqflU4qQEa0VTbH0StmX_MsfVu4Qx2dW3j7E2yoTikunXga7SGQDNBhjVMXURrNq3lWhPdCMMlviUCLLedSnccSdUMMexAhq6QpyaRWUpheZC4MIKj7LbZtpLcpIC15jdbh3FtT6OXd2Op8SXyWr4MHWIkrViN7gOfkvDlnf4rakPe0FMcBtEHHqMRTJRIznqeP3_1Ra7dGCFHpbE9M7Mff8nrAlvVl8goB5SaJycvB5uwBl5E6x79zbdZXaot3MX8qMjt5BFF4LcDlDYiM1c5PXQmJ7EDugTjXffPVHLhf4SuY4hdFlQ5ixBjEUyfsX0L02IAn90wWhhgOnxTjQ_qLKWoWgM8UFyipbqA-hzkoTtWT3ajc8zriqP17NEamRJnHz_xvJN3VQ4cK3ATxWitGtLhHsPfHkdl4UYcobch-I_M94XEfflX97bezGdeYgHfJkNlZpKDneB7BK8d3tCNh6lKnRCy8R6DvTSknfn3gRbq-7rC8ZQ9p7XN3xY7PqyqH_96yZIhlAMikKHmx6_ZMeZZ1Shi0eSshoF8V2p7cXbOjQ9Q-H6ZXkAedmnhZIXtqBBlb6Tw5U_6oBaqeZXweMaNtB2XiUZYW4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1Z9dqzIh0tZf2hU7vDLm1nI7sJZeS_q_8BRDECBdxeIR4ZXKIn1jxBknp1RguovKrqfcPOcIMT0hX-uRJCTrTL7ihAQTNEC98VpEkCr4BtJg41slLSe1M369FPqeEJVPcwdcTjyFTg0MX-5O6gewF9WiLYvcRkHsC23JdrSkr9McyZnUx4UUmIy3H5MWlCMBvTF69GDxwEaN8AHvvd7eXkj60iM9fMivM6Crhgu3FRWkaCvfEAy49wF6zV-h5lLC15YutmMXCrov0oP1RITLdpXQYcROkiZTtEg14eoLsy7odEl3FZMO5O9jdpNSRKSaeLKtEzjt5zCaHRcqr08bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=n1nMuVru5lQPP5cLBJb87MgrYyzUW7PqWJ7gSBx02lxIKlL5t7uJLGWWqT_LsBVsHtb4Ll4u6mKT8M3G54SwYoaN0hY_mswOV1_z81TZ-93H2g9Ss3WsFsk8Oeh51YS2xqqy5Buof_yLgrcZnMkG9B7z1eCs93q-lXMTFb477cGRrGZX_Jg-9xzTZTGowEaNPm22jTSbzIkwsMX7lM8cINkw6A_V7Jwb7V5mVgK5r9rkTJzmVKgcEMmpejpxQSq-qKqbJhFgXR-S7kAYZGHC2Opr3wGva-Ngk4j7naGJciZcq6xO7xzMDwEyFfMqEIqsSBEZK3_A6Ru1SGMCUuTQYp1iuNX5zAWhVCnWyBSb3nEgvsLeyFwG8RU8ivgyK9QVUxAwTbBBC_k9I3VZvspkbixr1X7qZrJlliuA1B5A-H0n8h7N6GH5dCmGqHz2p15BVn9DhktPlar7msMxEAU-GsIC_BNq3RF-DDoK7qbfE4tgyTEXLL9kUFhAv1pxAPoVgDiAKSqXBiuF9UhV_rW-etHrrfmYA2hyxccec90OCCFteQVpcevgQ8YFhH72HmjaehMOagHNZ29MlwD3LJQht1v-KJtGVqDS52rHGEpar2cVnhamSsv5wgp_eAY13rlWzpWade1QMZM8du5mSfuRhHH8ruta3vsmHGXfCenHD1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=n1nMuVru5lQPP5cLBJb87MgrYyzUW7PqWJ7gSBx02lxIKlL5t7uJLGWWqT_LsBVsHtb4Ll4u6mKT8M3G54SwYoaN0hY_mswOV1_z81TZ-93H2g9Ss3WsFsk8Oeh51YS2xqqy5Buof_yLgrcZnMkG9B7z1eCs93q-lXMTFb477cGRrGZX_Jg-9xzTZTGowEaNPm22jTSbzIkwsMX7lM8cINkw6A_V7Jwb7V5mVgK5r9rkTJzmVKgcEMmpejpxQSq-qKqbJhFgXR-S7kAYZGHC2Opr3wGva-Ngk4j7naGJciZcq6xO7xzMDwEyFfMqEIqsSBEZK3_A6Ru1SGMCUuTQYp1iuNX5zAWhVCnWyBSb3nEgvsLeyFwG8RU8ivgyK9QVUxAwTbBBC_k9I3VZvspkbixr1X7qZrJlliuA1B5A-H0n8h7N6GH5dCmGqHz2p15BVn9DhktPlar7msMxEAU-GsIC_BNq3RF-DDoK7qbfE4tgyTEXLL9kUFhAv1pxAPoVgDiAKSqXBiuF9UhV_rW-etHrrfmYA2hyxccec90OCCFteQVpcevgQ8YFhH72HmjaehMOagHNZ29MlwD3LJQht1v-KJtGVqDS52rHGEpar2cVnhamSsv5wgp_eAY13rlWzpWade1QMZM8du5mSfuRhHH8ruta3vsmHGXfCenHD1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EyocwBp8l5uTZeA3tuwIp0V5Je31tSFp2nsjVS7CHk7BbOrJjH8eFeJazEvl4PjKVwXVYBfdvHbMq_mU3HXy9N03DYfzNu6FK3PWdM6k4BpPVzMSJUy0JWpeoY23g8y4UAuhZwcGsG8sp7l-wUNrp3jcseLSRX6rh2iDeRejPQTlgWu5hrHoGU0o44F_Q3STT0u_bV0lRS0rFtSH1a6TAjsr8Q0dtQVrlA0RWQghrz4L0PCIyNEn5HthuflxvVbOZRX7fBWPGYPcQTyXhyFMoWDxYwo3m4vUQVQbcDPY2S4CtYlh8BtVJUJswXhPPwNxTqhy2cg_BHOtmKWQFFszzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mmri_STQK4XhJKj558xs879nNhbG7-Tng8ghsQvj2Ufh_7JSGE2Qprkh16vNsEaLZqeF3prKHdkbjjjzFE7EbODtDAJtXRbiSri3sJWQiYaxgSTvma3561S3fmzkqwSQxLwqo-9iE6UDs3QrKEKOhXcA5N29wEEAbb4SUbXPfHoc619rvUNG3Bowf1jhjEnUosrVgdTo78dXDf7Bhz0_no_VefUh5YAWMMTovT-8uUnn5dHhqM6AxjEc81yJ336dUtL7DWwhwqr5UMwagYtie70R88sIrVmBzG_I8Sn-_uT6kBZOqzFznwv0nZRIoxPw2yPoWIIMs3FaGAchZx7JOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdMGUpR6TFtFo_99KKQjrXVFDSstuV5KPNjZYK7hypFL8ziQRAFZKy6qoiNwd2N45PUSM-lrTXGqOqVNjwXVaVWXpLMhLnrxXQMej33vwDjunXPWff1-PW0XBFtedTCMRoucl0QmUoHZQbUvhXj-QT9klb-IC2XqMKkab8q4hHGpHPVBfgsk6jZ1Z5cgGswxC54xA3LJR_SMIKJtJjy9eztIScwLPbN26z4EUBqw0-2BELfub5tSUFnRZ3zIJqiwFQjKTvx2av5d0aYcjT88QEEzlWxJyt6dpY3h7JJ8yx4deKa-bY_nR-m9w5pSV_78y5Ul62MfakhrT8OIyTc1rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7UeblBP5fLgUlXlQJPF8ma8ZMTHh1LdVF38vH_GSfipJp0vNDPvcq2T9mDPs6SLbqG4TxZsbemzgkGDxUzhvVN3Ohs1VBMUm1Ji5aIkI-Jd5lS5lyCKuckFQdDeQzoQtjOqyhLbXhLf6jDbGEWhCuJmIKD1qDQiFCKoTIR11jSv9vR4a6BRQIL0vXujZR6Td3TxlDYOnGFe8wtC2_9WLMDg3Ow0_impHtfgZQ0UVjc2VYxpuosHzNtevUFqvJXe58xfUb4Nv0cH-AeyIqYV0bjdHoaFOOYdHbsAs_fZRBd4dSUDKItzwzVnEDg-cYhGgzloEl0o1kwy-NbAbtorSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXrmzKUS2wvvuJ35INre5XbvgZZCwqrIexBObhJnLaoYslzo21P3B_E_eMUkrxNN8sDzCBOXwHtniZ7l69MaSxAXEAlt-9tBnlJ6IBS8ZwKZxdSvGyrHL11RB6ffMWqFZqMY470QVwpDDKAYf2Yvrg5I1FL7BHqZUzN48YDW1gjTNx0QGj3_VM8XhebH3RZIBSEI2XIptT3labV2bXVzpGiC9CGcM2D2ERzX0felPK-k6X0e436V5fCwXZvfvdqllhDjUZ2M1T3Oq4fPoFk1TP8Lk5IXNqvJkd-d_ZcH8p1413BDheVPJGXA66H6WFXzl-D5SOOEI0NYRVatVMmNEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoHArSmTqrXvFkf3G8M92vJz_Dj_HqBGqRWh66Qjt0W4r4HYLKD_lTMW6ev2NWC4P9mPr_luUGfUqNzgHHd---y2EYstr1b8CZwvp2HefLBiB3YxFa3qBtAICLpbI3EVv3E0NjQDwVV1Jj0aYfxQjUbAk08DmzG_U3RU0BGevsBa9Q4UfkDRbNPfBd_QaWjbzoWglQUkj42jiQOEG82ZEml5URgZcoTltIuDYxs3l0NCggXb1YMtXwHsOXO720UYUSeK2Wddn1Z6fxTPHK3V4-gLfkZdUK0TKd3WxOn-xkBCNlpaXYipFWGF5WeYfnS2FnYaM99hV4wuTvUiXlDxZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kE7JyGYsGXnAw62fhl0UDMwEHOOpeERhERETfxF-PeerqDDqvP4Rsu32PNySKnaxDbWv81c4TBOtP3O1ir73R5X0qTCfqOFxi2csfkFSOclFVk_WULwgRReeM3tnQQZN9zXSVomVwnuTjYsXG1_PGnWzjg5zC5mnNEE1Hrfy-2ef3_geVUNRbuf-W5RYVDT4zbVFsqmruNLB0YOsbw8JxjJ8bsVzKd9rTJuzI37LBAcp0hVmLXr2hocM2c0dte0YGB8ey2jOFqZY8mlVZMYtBxXERJy1rSCLTsX9yK6Whs2d16L0Pl4o9aO2X7SlAEkxgA45i3M2dU0_u2hpk-MWBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4FXMQKxOSEb4SXK-CMF1Hnz85rLS11jkDHW8DfLHuChbM108NzxkKsdegDItDYxczH2eA58-pK2gh0L4_T-3xVC3KxQ0W6-tR0eFOvemdhO2pZuRm6Kc0PCsKuXfGu771eNJGH_Zl7ltmazZ1D4XDn5Tz33pZz94RL7Ji9PtgjxeeZwTinS3-yNJOkc2PzVlg6bJFKpzSy90vRnGXnV8T2UP_7z53sP2s8qT2G2FCWl_Pek4dHxf9XE0atizhOjSg1lnhlCACaosR2jBe9O1EJPeNxI1dF9KC7oweN8018Zjztsey9xZRl6onLLyNnwkXQJ7t1lJ2knnc0vuWfJDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsgJwriOOBF1ocz0gfpyxAprXe-Wlxiu7bmEf6OD2MIJQ-zN5uUKEloXJZqw_P9TD_au4e7jVYma3hwxS42xPO7HIYHwkh0AAmgHrGj3wC-e-ezgNbd8qJL-blP173MlH3uoovIxgnZ9jxSQD-5naZfH3xnzhlacGZCuxCxmdKWiVadyJw5yuIUoXItQRPfkl2YKh-uiZ7aHPUJHV9WE1VSfDncdHuzHGhAbGZecQnaOPdY0CLaYA_ZLVJbet4YUtmSXaFMrV-ywCJ2LmNRn5yzuCcFf3WNk2sTR_cIRvgsw9JTwAODjofF1vTTi3ulmWyfz8MfD_D-zGWp21op_1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCVQB8yVX99VpUkEcp8MLVx1V24oFvliq_dl9ETFsFxHwDRODwv10rtg6KveN5zJ1hEmPBtAL2rZhkG8UVTgExzayedKkp6UcNAVvs67C_bEcRkDJjGRxUWLLJGYG8floAWAkoWR9Tp8-RatNpA90Ens0m3P1ZhxBRowdmjKapM7aMIfat5DKY6_uNis2Y1ZmsWsclV9fMMuAzgMxnSM_sjO5MwdNXIvixxnoYF4A7BPKQ-EY3L3doV9dQ11namYpv5FFK4i_F0sTD42cLvJcDUrA-OXrFwNSd-TTFlUJxZkH9gfFOBhOChOlTDtpvw_gm_B5LEOvBqJ8TKOIB5utA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6tdXKkRyhzSebfB4-tKHAZtly2yY9CM4geEujoi0y0qkwoApCzK7UlkZ1-A_2d-by38HVjzVQsPQgQgwfX0BFhzUsNlJsbF0NcTn2FTPBTD3lNm7V6hZ5Pd6LEVSkg5cTbUy75wA1NnTTFeK608IWGd2b5xL3QrPtD3wcDHaIpa7LCrIVqJaiLJvROVKtSypbgDkCzJ4utq5o3fmqRy6jl4Wunrw5UWphtzQFOCIi3gC9uujQUN8jsG9vQQc4R7HEWf8fw1_Y7kG1p_xXaGwV95xmrptgR8TAXl6uxoIr-jJhul9tLP0lwqbjxJh9_aBk2TOgQwzlrC89gieSrkCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKZlkD5fcsIB3Nw1W-4Mfpnf0mrgyGcpco8Di55RQNfFa0KHIjaZ8yUrMSujspGwZFtcOeKE_HsXx4sl_TE6ZtYZSrVhsSqYUP4UD0RY9ezS2gRaepptO-84h1TWvpu2kjDnw_zNJD8QdvIrNayHGpt8WUMjdUxoTcDP9YdaU8zblyiSFc5lYRSIv7o3g12-qQeKEEt738qP9oK3rrTu-smioZvlxSoXFUhWmqUAtifnI7xaBM2DLFA6IqGtvE0UEBIy6_vs7khCuU63pPgIOy0u3JloKdEeEYEYCU3J6GTIJcChhGpXEyUBTlr1-kqUaWmwuFYlyjTTqXKrw3Gb9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMeZaER_DtfRulLeZU1weaGo9WRgT0rz93lVuZUVeab2N07cMPybM38Pdz0RFQFGDhL-V0TKRQsks62b7_hqcHIfkUbnjICieHXEZrcTdX1wWrotpfXNNAjpG4bPU9ENgrJi1NaLxC9Yo0g7D8G8KIhyG6SR501vpGcWr_vd_6PByPD2ePrPR70cIiwiE84YBdSjDeYLpO0gsuD_yFqkoNhZNZrlxIaDvvpNEnzpiTKUoQg-Vwk94Ty2UdJdWpyuWK97stb1dRpS1kHtpa6BL3O9pMn62mzJByTNyW7q8KHQhPeY7Mjw7FJ5jRaDAYC7c39au2qQ9lrksR9OE-QYkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gse_jspdBCH2PpDRdhusZ1vb9NGJQiTBGx02BUFcjSYSd4zmXlg4CSHn8uNRVmRODCoxz6TNIcyckqdkqoPYs5HfJq1lN_MQLLAy5Ulp8JBJCCWXbO1DNg8PUsK5pebQdvJe1hY-tMrwmLbQTKHnHNAuqXpgXpnXVn0r0VfVRBjReF3wRfmKBdd_loR3mPhZMDXiiLQx6GhMM0XcD1o1PQ3z8qwUIWe4BBWE1GUqBiRrmHnnp7C5-Rn8GnMwS2G-5bEmZzXjYagYh-RrXrziHz6-0vSSnQdWrPIJbvoeVA0kXWzXZE4c0EqGFOQ6oTj-vUnE3lp9AoGeK78zIcWIKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1ixVri-sVcx7j7kfqXMXht7-5NFwP1Dm5S9GigvBgRiYIJkFxwUy4fUCaVVFzvm_Q9ZUF-h9Q404wEyKs1VfSEDOhAGvnEWfwC5yEzSz_d3UPqgFjfOOWmEIY9t7CYEd-qQQzThCwtQTStEVHR0hVQ3v0jk6kFldyZCMjAGYYZCBT4F6K11rI6sVOYCog8d7bBHq1BrMPgqZl8GK3RuRnQWV538-EO_NbEtPpEBaq37IBLsURW6EuIvhVPCT9DQYQbizDI36Q1_Lt8ZgOmNVDUW7TcRWXtSbn1ElEpd3YugZElIW8UFBj4zCQd2hIX9YhB2LbPcF8rAFrhL-8eAhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sK_U4c_D0Gdg-Lx96jfC7ie5ZuMhNoDQ5dcHfwitiqAx9DMEuy6I6TsILLcI-JnybuXmzw66mzbo5m7hb8FI5BpQvUsR4ffgzNEYA_HgtplptTHHtByMNHGu4h78SPXzqHDIMCwd2EfDRyEBA2ZdgUU5rAR7HH8dn1i2t00mPjU9MZYlvMfJ_rAjAUYZBx3YpsbryvsVhST4Z31gXXQGQY87f9jyPCFlHbd2_HS6dRACXqSgHOC6AjUrQAAPutrpYaE2Q1WzH2HeJOfHu2LZcsdl3whbEm4uJJ_gEq-lQhdoZVXJ_ilHU8ZdgGi4R3NyTu2eks2O0lK_1-72mMJpyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9ANB5s5lVa4EkbRRwJC31RpevM0RR3Ic_hIiTglBllmTQ7TBhFqaEOyTSNpXiN9n4ZOHb9nQ91hoFcD2WxlhR5WGRlAgs_-czD--RNcQ3h51YIZE2q9W7tHae9yJjBRY0ZREgSamHWdoZmuP5qhff24uoIobh8uhOnGNv4q_rGQOg-LLIzc9vALKoMa3MQYqM7vVhHshg1rEQcYV6VnxnvC2bFnsVG9jwZro5kZWUTEcKK9IQ-UdwP7DkUxwDeAUJ15lVyEqe2KtDN3S9dB1BFgzgz9Su0v5r9k2Q56sOCPcguO7uyNmDUsFyIBULkJm-Tzyxd5ydO5QXYIUzo1ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W7Lm4LHhgkFlF6cq4E7L9l_2Wf-s3LLCeHW4Zp0Jc3XZP0s1G_s3-feLFtQuY4_sP5B0rY6SLXrUFkHvbjtTQ3-GAcacs-tDgOQEd4OVff1ztNYD0-bOSKUszIAuE4irHjoerVSSIRzx7rkh4V8yePkoTi9Y8fkWnYQnoS-MQdiDeVRB_Mend_6AvxHFhDkP29F0RVOy0zTzFZggHfDSn-ua_D2pd-ZNle2G2TBiih7fJTF_7t7fuUFATzyd6grCPZeW8oRQZQw3LaIpiOmd0prNsi7yME18l4QO1UO0jljqhOtrUlaaukm1SSBzd0RPhlFiVF12-8ilY0JgF4h3Jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8wQBXgS5HIVX00_2lCB3S3Jd3YYJSfA2whekARGzcxNLpy-FylL9Nra9gFyWVcXjE-nHANfo4KYzKPtk_hIW8Uae7N5uMUW9nguktUa5qGgRV4r-Kz_xbm-JoDNuYlaXmvlE4gvoGRX2Lr4TWg7evTwOsbAXnFjJe_H__PM4TKp6Z6oJCXUbELbGxd1n25cl9VxTa0q8Lhu1jYS_iFRRQYbCRJmya6sA9piGTRQIc9vuAcZR85xmZ8pA7DKNmO72dxUJ6C4Z1OAqVbrtbVuNvNd1dI-AK7Ej9IA3VraWJsR_MRO3Weym8RwVgPRY9ki7tqzpbEMHXJk1pVNi2h7nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVDR2kVIfRA_teWtghlJaOOMtyjm7gTpERkImI-GEikd6yhbzS2jFU5zGcnv-06hZ-ucbOU1Qz378IPZAvG_0y-Oa2ol1xP6s61K9e92TtZGLS9sNfhqWHNz8Id7II9oUcGhQjJY2L_CAmnZStoQJhR-HKbWV427gqfTWGnASoLCCixA9Artdb9PqVWOB9MN1VDEJlOO6VHDPtjqtf6fK1zQ4hmd55OFzRPLqK0Sqf7MFkdHp6IauisIsSR1EanX6nvLMMmzPcyUWhCWsNMhM1BV2bGNKp9nwB_c1X74CAu5DLLowyrregptBHbEz76nGuQDVy09GM23Q0lesr_sUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjIC2rpjTNo-noRA5LkzIVZQA_zitdVgcYafXuJP4dFQDB8YevAagEuo7NNrnuKWhTivZr1d70NXUMnm8LmXhQSxsHTXV1GzmzjG36Mr1aiFd6StbUEAc42YdlbcRXWBEoTpEWHD6nhrbi2L_2gHrDIN5QXel2QvuL41Rz6hcFzVP1dAR9Y5AoOT0MIEoQiYbOgI6BwFiPqZGAGVfx7-bjTYMG2mlbi16I4oY3hUza0iDKO5kH_lzj3-LOP6c1wlOHJ4WIQTXguURUA7PoOk9MytZhp18hZrKCxDDFSP7LqJLWYWvQRoGHJa1-O9WO8JWc7NI6oFU1Cza3Hj_Wox1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrHsn2iQS0FPMYiwUjh794q-AQBIC6l6qTrqP-PmlOdeCXXF1mJjCS9gb2_OJCKBeSYsjdKo1K_TPLCLg1ueW-MpECKnsP8_-cPNPQPJP-A3l0YVyKWhwqlR37N3wAun2-MEj-bsCVweBHi6v_f6BIsrQ_zczwnNz-NLfmeduWh3tjTHjBVb6SKdgi0DGamsony6DTd7gbUnUAVqtNiRU_HnbByw_zQEF6akX3oFFRfAER0m-Yud2fOsKlkKIJ0Vj_UZvVmgFUk4iJeybQ7SIg5G7tOhz5krKhoq1bwFAJmmm_JAz7x02ybdc2UadOX9k2GBqb-NwDv7v-QisKLqrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UejYD7w0ivEAF5QT7ptTntT-6LipTAt3Y5KtRrJDYEjha2bvaPvWa5WSXPqiXFVnhbuc4Yei0Dkuae7FmrM6HNNJ1Za4ZRAHPcQM8q8rJ6mlUKc_YB5b95COtu4ZDnCyWYRKfJO6VvRxEhV3kxs5AaJaYD4GpEd95nm2wTzDwBMds3O0rqv4eMTnVOYxqW61zR_YGQXIUJNm-sPd3NT0MJiP0Rcz03WffNQbY2b0X4BgpZCI4arR93MwVpWUi5I45w3ZkC48sEnshbDFqXVlrVVsiuVnQEXaWXum1JUNHsO9uDz_urVNqOgVpjZbTsMje-paBjRZXt9pEw1GQjFUCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tc8Bi3MtaNxpxM4Q7AGZMqMQC20zz1FdxmacodAs8th5j64kr6p2rRzS7FSWst1AEyeA7LZ-7EmvbD2KILJcF72JGc9XUUdR5n7ge_kKquO7E6RuRbZICYAuh5RPiTJqWtroIFuLUFYvEb8etDr6IsbRNNtJd26F3SmYRYKikQdOuY32VBKgwNfXTKDEPnMFoB3HgUC_EECU4we6Ru2E231grxr0a3ieNIMBOzV_Gt1FHz-wpAnLKvImQYGtSudZEl5LphrlLB6F1gh7N2KJ2Gndfrf2rM1-_srXOHNOP1LCq9lS6ZS10tlE5Z179nerxMkdUMJ979Xs9XdVy8XdhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScavXDDXJAm2wYx3H6exsNuc4YuRNVqKGOTq5SWM7ZnCXoZp55fPqcTaSfF1QBwhSPeJA3RxxpdMEqy2bXNiCsqPrQjCN72_MoU0_695W-SNhsGYIzIwz1HeE4EPgx-v94mIzU59O2txe8a_BIsJOFBcWhcD4jxUuKgRfY6Ml5Q1z9GDRjo7tlfy-OCdFnyL8qLMhIsTsA6G1zdl45l9oWAKaL_XbbLhFCIpDrne8Wtkyfq01aIFY7mEZZ77GU3VQs2_DAd7P8UiIipXaC3fXz_3L5wzFUozRYW6Yi1PdMYAsPNRo11YPzxsgvQEVrlzHU6P62-u2OhwNJZ_lt_cCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJBOS0tIaeW7rUBvCvsHvTniyejpWOfoBfiiCN4nWIxKKHsZhPbM4LH1W68RFCKFvnwUGm8p0gRCbR56DqAfnIENQyv5-j47Mlx_0-5F1g9hdhJy18iRRkULMY_I-zatN9NjFeZ740ken9JcWqi_q2TrV6MBYygCGIPX3HlREYY9E6gUGu3mILdmrpMuXRyRAniL-sgarJ32hm_zYXSzoB8YaUEuzSSHMK7PhHximlS5mPCa6xCMaqF32Zz7j0EJs8utiuOGqu9QWBVhWfyCTOqUP3iLRgthu-5eGntW3a30NnMivypedZvzexBGuf1hMiMb8OpBNHK5-ry8swMSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYI6BYIRgZ3kuenrxTbOka_8-D9DehZ_GWubqhat5igrDHGAaBH9_5y16Q0xQpXwqkMxBuWCZGsL6aXuErqGBBbKpqKlXBv5LLHXNS9fBek-KLw-C0WfNX9K_AKjbv-mU3bT_twldD_xBlvwpNDOK9nlerk-ypKu_GYQ1X6MTGkjZoA--LW3b68fA-FDLx47yfZWsvXfIgq9jnl2q_LMLCM6Qs63lqNveRDw4jZqzxQMz50Sl6P3HEX_XfHSTAKMmvtpR9fRZedjWL3A6isJHO2fNpnTpiUJHxLwvJ28mHRCqdK8SAV3gywMGcVU2-xsAPA4EyEnhrdALV0-xHl-SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-T8Y9Yc2yzh7o4d1Lbzxr1mRbc9meE7u6knAKgsaNN1-M1socHBLjbDEMdfYr9M99pF5dPGRYdiZ69_7h8IWyeHGuJeF5xI_IRc5OEBGXpkaKihOFMMF5ZtXCH6hClCGyNKR2WCnB-glBDKlQ6NmCZsYO0RVU_4sIIF27RrJqQn8OC1styKUtJK-WdK35eDc73ARBbgvga6PWvWFinnMqa9qWkqXo3hk0LprJ17x3TEKGVu22Qc-IDlL2S6LOfu8ygCvEKgWmsWd1Gd-8zGhmzS1UdkN5RS1vDy3b5XCvrBanvsRI_4rOGsHxaF3PlqNX-WCZ7DhO86OfDll39ueg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9pQkGztrfzFVJmeM2sFFwXz28zePkgC7of6o41jaVzjiJNYgtP08hq-5vZMdqdQD4OXMPNb-BIhqa0T8Vvq-Mjdq3JSkQH3KCVrdEIadVO4YAKikDGGfySndwZ1dENhUxQBl1XfTysx0-zuVQ1zo53IcMF4UTXT7jMHobIZvHH90kNdyWqCddediPIm-zOT5ZLk9uvVdMyeoS0QojxDEBPeP0_LaOAS-zEl8X8U7o7WyzQMXNJwfkjGi4DM3RVoMrrjgshw4NK_DnOuj-xmvva2lSXqaGhwYpC0xWV17nBnM3xU0pR-0ebGyAuSq5esabH5kAfHBrcdD0gP0qc82Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2wvpJmZhpJwTieoLSAnCP1iIsTB0TX34GNy8xGUwSzFmA_iX9jkcbV-bD-Esh0XfUKJ3onpbw3-FSYRhl_c1Fm5XyquFq-UAn0UQATM7Ran5gMAmbkQiKmSO28VE6unx3KXHoZbjYTNXv7faGtKkKeA_JO5S8u2aNepKwsNqwWtXHK6n0P8ruZ7gg5_xrMvXvvM6NSVTN3DxtRbCPLdSLJ2Y7sVrdL-KLBe4tIr1jh_rxlLb_wc0m68KRXH5aFMQlpaBcWx_ZlBQnvaeZ3QpFvKHF-3mvpe-2DaGzQAdbDcUAn8WU1M7DgsBy0WnMDqzxod2AVnuAJ95KjBjtem0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utIe2yT6JMm-el8SeX1P45r7T544Fx4pVZk19MkQ37Ov0ZL652k0wqATci19INFgj9R1IacRhPmWsNYRlmEZQRWmnTBmTOxe0IIELNnYgaqb4OGhZEScc2ZEah3uyovkJBJ1Olh_I4ppfeT7wM5kueGHiObKSAuS0CpTQ-QEk5o4FRM-VkZ-fV82oJqqTk-NkR7xhcOLcGVyFIS7DuWkd9UdjKlCM1LnUufuYIv5Tpir-yCYLuuH-T3pdHeL6BG1Ria4AReC6LxzG4Q7dOXi4Vz1OpDk70iM1MfR80A2DvshLn5j_awqe6rOfMegby3JENZNSRTDyn768tTAu_3WXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJXNp6bJr7FOReq81p9hzverT0LwpfQLe7Lpt-1DXQ4BbuHCaYTtaHpEVm4DamfFxTankDI1RwkAeuF0C9TsF6JnC8rH6_17oQr_asBJ1T3_4e_AKQXPgfwJTgwnxz3247wP3s1B3TNbyakbkqRsTa9FqxTRWC4GJuCWZpwU42CHFuINZCN6ju6x7TSrRL_ul-GVqfJicULqbqUo5WWg_bRjj9ro2XF7PlxNon1xT8CEQdq_pfnWll8WU1U2qBo17s2Aq4ns6IXJXyHKkgt39j2-ZFhvxYbZ111Tlog_ec3pyBnJyZ1w-4ecjNZscW3MJJpPjRu3H8jEUkO0dfziQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXzrT8MwRrPSrMv5oo7zZD-MCghfNXHkITbvCNOvhYDCFDamATjXOwO1dA8qetonPzrkfDKSUoahNbwjS9XeGNGg7UEwFKG57AiMqh51s-HsgLL8M4Qw_MdOyV8n79hr4oMOpCHXpKH3h-247rK-7CGSR7o7dXKM6Vb-Q6NKle7kdlOtd4r9pw42NkHtijElhVk-mURkRuNsLyMAioHW1OS6PdkEfC3iIBLNPC36P8sfgh88r0T7uDuwp2eomWEUb4lVc7Oni0b-6erfdb6y-lWTqze_I69oBzQyICr7IlhWj-3if8Ppglx5lAXjxl2MKZ0_w7oDT5nVaUyzan5Sew.jpg" alt="photo" loading="lazy"/></div>
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
