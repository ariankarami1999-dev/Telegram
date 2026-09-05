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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 17:26:02</div>
<hr>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEPvNPKmo3Y3Dh-7BN3AfgbMYIpaxh6BhM89BiSaGPhhVVYRt-VswWkRfURY6IhG_eWCcfc7Zj2Kg8TW1k27pT3GJ4gF4oZGC7hrxaQGx5-xK1ZZQz7SOl_Cjcb7QI0Und_ThoDCp_ebmGuuWyejZnlFjxjLEDrFwiK7oXYEwh2X6jHQWdNqwN0Pner-oBAXEgwFlCvti9tWRGbckm5KAMNmlhMiLbXjPQLgk7N3Vm2VX6AsyLvsPGApgNg6VoqGd1gNRL1iafTgiS4x_ogGWXXNUq3DepMx1DfvUdNHQFbvCjivhexaZ93_GkLST0r-xMZtPHfccYOT22sZE3ynPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbjp-PRdcEWORyoBfNoYsRDrz0vP-rOqtOJmksVDE4lDrV29CQGpO5Qg9EtsZrVfHafO9Zcdw3MTbGiaGjAWjBiAU-m2y11BliuHFPNOxrABUSp1EFP3BdNEzTZuO5bmrsSgwcNvHyOOiaHKieX_w3WJfEpE26zzjh08wjF8SaeNRDN-0vuDkNQ-FkphK_MxSXZ1qFEB7uL2Sa5odvQQxtKGmptzYGb1G7BFxYiDliDK7dgHEADwPNtMOootKMvM2qgtPxEs1OyHuEFiODy900Tya957WDph_MgJaAAPDKTvzORzPHTq16KV-AdsiIcRqnOgGc_l8NXRt8Fa4OijxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-3NE_E1m-shGhebw4sykigZd2YZSbcDkKsyQ1Dz5UvBQmi3CqkT8E_0l2etZ7mTbQM_Kt_7tZBEAL7_G7y4SI8KoJOtezay4VmWvjv5Z1yhJv_aKO-6eaEl3wcdyKA15s7YW6_FO-_abWD2nT24w_XXw3Gq_N-OZI288tcFhFaiko0EBtCYDkEVi_e8t2BoaYhxKbffvyN50O_ElpkEg0nrcuhnEmWlCpIOkFjKdBYmHz0Jm557XvFzhET4Pf5wHHX_g38ZGaN5L7l9y31Rt1iaYnTAYkSaqShScaicSsoDsiPtgDP7wFPLbhDwmw9vHl6A-RYCLzlrHJOdM8GqPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=b6MZ4nAaOU82DLpBGt99iXgI_I_MQTMawlBrU_p5vK5Uun6IyqsNPBIOMK8Tgn8cMRoq33FO9jf8ysqCiuKpD3xLvfmd8YPGsddz5uW9ROQYV9QHoMd_yEwe3WR89cFkmMCQ3vu2JPjum7VzHc9C4salH06lVfIaZUo-7pQPVBf1x7N883PMzq3xMFYY_DfCBnoPPnIh1fzdhJo4hod9xOnjfoMn8EQIz0--VpRSjr-IuMzZUsiu3Quiv354AAld3PtBRDfbUUDR_RhsbFT-r1gnenJFmWKth5VT5iO5dlkgZZTG0H9FnHcStGh0jJv0HXQktcOvRSTQ_IgU6KTDgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=b6MZ4nAaOU82DLpBGt99iXgI_I_MQTMawlBrU_p5vK5Uun6IyqsNPBIOMK8Tgn8cMRoq33FO9jf8ysqCiuKpD3xLvfmd8YPGsddz5uW9ROQYV9QHoMd_yEwe3WR89cFkmMCQ3vu2JPjum7VzHc9C4salH06lVfIaZUo-7pQPVBf1x7N883PMzq3xMFYY_DfCBnoPPnIh1fzdhJo4hod9xOnjfoMn8EQIz0--VpRSjr-IuMzZUsiu3Quiv354AAld3PtBRDfbUUDR_RhsbFT-r1gnenJFmWKth5VT5iO5dlkgZZTG0H9FnHcStGh0jJv0HXQktcOvRSTQ_IgU6KTDgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=bQKU5_gsYUW3A3NpJNdrpcQziqwWyoDJRYfJlXQK6GmjEgzA9lYoE9pIpe2kJ2El-PQjsFkOHXYeKglzrkuLOkpXaC15nQ5_THVdWRDsqzZATydiLq9NfVZgO8aDxEzN0aIhXk_09q37PO4owwpY4vPq8K0p-OUu13teSvf594ghPpyb8H7orROnmZil4Ro6uzZBiK3IUxz6KPpQuVIe-epeOnCJ8JKdsWUhYbqZOOQjheyjqNlg1t80tLKo2BoFHuNoebN5Jz2OT-WvYd6O-nz_1XUwDzCjXoGZ_HrnGNqo1Ne1rpi2XaDkxzaDNGsX5zu9qwPvC_OOQoLbz6gbakruedlMrZuIxrSUHH2MPV6FbIZPIc70WaS0lFCmZ6T7lNXY4Zlq4OaZ7rzOguoavSavFS-kiRJNf1IPxvSNH5UuVy0ijPO4iJ7aiea2OQ7XwoyGuKy_iUh-NKOerNym_Ercqc08fspGx4dDo4852-3fRj2Dhj3wb3KbbvELIgcuXt1ud9Yn-tnRpkZaGNoVWvc1N7QFGHHZJrtuuUcicKhlxMDWmGA9xqKk9_doFPHwVtiylLH6EV-jLosw6Bv1mEy9wsOyIfQaK2UmTI7zWt8uTxmR6-F19UNYgwexODepYlzw3MAMmFNwJzVIMqZlw8d327djRMMR7aZx_MvDYtk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=bQKU5_gsYUW3A3NpJNdrpcQziqwWyoDJRYfJlXQK6GmjEgzA9lYoE9pIpe2kJ2El-PQjsFkOHXYeKglzrkuLOkpXaC15nQ5_THVdWRDsqzZATydiLq9NfVZgO8aDxEzN0aIhXk_09q37PO4owwpY4vPq8K0p-OUu13teSvf594ghPpyb8H7orROnmZil4Ro6uzZBiK3IUxz6KPpQuVIe-epeOnCJ8JKdsWUhYbqZOOQjheyjqNlg1t80tLKo2BoFHuNoebN5Jz2OT-WvYd6O-nz_1XUwDzCjXoGZ_HrnGNqo1Ne1rpi2XaDkxzaDNGsX5zu9qwPvC_OOQoLbz6gbakruedlMrZuIxrSUHH2MPV6FbIZPIc70WaS0lFCmZ6T7lNXY4Zlq4OaZ7rzOguoavSavFS-kiRJNf1IPxvSNH5UuVy0ijPO4iJ7aiea2OQ7XwoyGuKy_iUh-NKOerNym_Ercqc08fspGx4dDo4852-3fRj2Dhj3wb3KbbvELIgcuXt1ud9Yn-tnRpkZaGNoVWvc1N7QFGHHZJrtuuUcicKhlxMDWmGA9xqKk9_doFPHwVtiylLH6EV-jLosw6Bv1mEy9wsOyIfQaK2UmTI7zWt8uTxmR6-F19UNYgwexODepYlzw3MAMmFNwJzVIMqZlw8d327djRMMR7aZx_MvDYtk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=eqwK7ZRqs-vHq7eflBWJ76dO4ECMlIV9CVrB7zryykIi2TibKwSGCnFNtCnVIg4x6k98ek2EhL8Lfh5uPGGd5O8rtZsSo7nY22h-SJONdSYMxSS3AYMeavXBLSsGE57Sav_NxwHR1Tka2dxV8zI0FyW9nckbcrsowxOglzVkeD7xxWuee8jrN86ME-PXNL6NldpRr4ZZ1ytA_SAcnxBWzPy7zM8FJ-GKpGSppLbd2x4DlFmGCK_P1NxPYhAr_oVZ9rs_WnuAURlMGaIfsqPyJZpVgUTbs75Va8kY8FqUkDkAcY_TCq6xVTM7AJdRY39OWaSe6nwkjThah4Af9eAvHAWzO5DisdOYosZLO1wdsAfIyIeH63GdjedAC9Fm6V17lATsf_0wJldGL3rszNmXxmPpXClFxuwypVrVu4c9Qu4NGiXkLqbeoTIc1H5BxpKrYIayyEh4RKw8RqivMqYniopzljaFBdpeSVpXk7Z3vKF3HHEC3wRLz2UE-9JdY5yCE74f_LorG6V-pUlyYSzSqHvohd5zB1sKRafrAaQT52bhjAbsi6LVK5NCHBLpZADBVPDvuLB7uCTJlWY8XVSNDlQUamWZ1Q_xn7m9yrIxpQP8uYXFGS6-LbGYCLTJJQ3cgZPtoHxL22MfWZo5qayqJkSSvFFXYEwTYiEvPyrxF4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=eqwK7ZRqs-vHq7eflBWJ76dO4ECMlIV9CVrB7zryykIi2TibKwSGCnFNtCnVIg4x6k98ek2EhL8Lfh5uPGGd5O8rtZsSo7nY22h-SJONdSYMxSS3AYMeavXBLSsGE57Sav_NxwHR1Tka2dxV8zI0FyW9nckbcrsowxOglzVkeD7xxWuee8jrN86ME-PXNL6NldpRr4ZZ1ytA_SAcnxBWzPy7zM8FJ-GKpGSppLbd2x4DlFmGCK_P1NxPYhAr_oVZ9rs_WnuAURlMGaIfsqPyJZpVgUTbs75Va8kY8FqUkDkAcY_TCq6xVTM7AJdRY39OWaSe6nwkjThah4Af9eAvHAWzO5DisdOYosZLO1wdsAfIyIeH63GdjedAC9Fm6V17lATsf_0wJldGL3rszNmXxmPpXClFxuwypVrVu4c9Qu4NGiXkLqbeoTIc1H5BxpKrYIayyEh4RKw8RqivMqYniopzljaFBdpeSVpXk7Z3vKF3HHEC3wRLz2UE-9JdY5yCE74f_LorG6V-pUlyYSzSqHvohd5zB1sKRafrAaQT52bhjAbsi6LVK5NCHBLpZADBVPDvuLB7uCTJlWY8XVSNDlQUamWZ1Q_xn7m9yrIxpQP8uYXFGS6-LbGYCLTJJQ3cgZPtoHxL22MfWZo5qayqJkSSvFFXYEwTYiEvPyrxF4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=dcjPb75sqIdGPPcvlYvl4FOWgqZhVerrcszwNTEYaFrALw6lOoCRrVoJ8BvaCOYXKDNjhPZNnQGAhNfaGkk24X7Ic153shdDDSuOJ9u7kI_s6YIpqysNjQx8DSg31fSQAqUT6OPbUgpGBz02wFR8mNZul4X9_i4nr0vDbQGsk07pHmW7WSu_vsODw5WewrVM-MuAE4IDnoeepGX5tuQIg7eIMqZwA494rJWmjKSTxzNxdMrD5Egbx0PT3_-a54Lh6uzZE6VsSOLF2885G8hpXFF4CzEEXjL03Up5GCQKpKGrIArBk35mjTYKHlwqubIBPStJOGzoN5p_d8TMKq2G5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=dcjPb75sqIdGPPcvlYvl4FOWgqZhVerrcszwNTEYaFrALw6lOoCRrVoJ8BvaCOYXKDNjhPZNnQGAhNfaGkk24X7Ic153shdDDSuOJ9u7kI_s6YIpqysNjQx8DSg31fSQAqUT6OPbUgpGBz02wFR8mNZul4X9_i4nr0vDbQGsk07pHmW7WSu_vsODw5WewrVM-MuAE4IDnoeepGX5tuQIg7eIMqZwA494rJWmjKSTxzNxdMrD5Egbx0PT3_-a54Lh6uzZE6VsSOLF2885G8hpXFF4CzEEXjL03Up5GCQKpKGrIArBk35mjTYKHlwqubIBPStJOGzoN5p_d8TMKq2G5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szdW39AOqUPaWZYeUizdKIjcPhc04Ms5b_zNT-90XyPh2tCvnaSDC-kcSCyKcF1lgfUO9WW9iYpXOFJat7grr_oMgTVqXcR7472mJNXW61zYuu_MPiL8mRWsKSJNtELYzXrliEQTwB9Mmd5RoDiHBU-nV2TGkciek-UjspGuHZBxsdJU4pn0g1eMVB_HitDMP0o68-bt_4FPCMHGSSe0BJ3CpFe1s4KGnFO6tlGSaqcXagb2jml3BpNqUSfYAUduJfrU4-HSn8daURiBrN2eMnehOiOOhXW1hUSVRUANB6JIKpMFokbzhyE09gMQZoiUCCLWGTjVPt5zvcfjB_6jKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=fVL-Q0YgiYAIB7NATVS0D85pmKECNJxpAJu1dGSdiYS-vmRKBHL29I13Y5sKuuQP-vbAOzk6cctmo1GHyOe9uy8Axo5uVFB5XAhLdyLg7h1LB0ceOoQtEhbc_7p1oGKMQVzDP9eZcZ3zhDM9gwDlH2AI8qvO8FyopxnWZG_6Eiol3kF_8zfDX6zVTnBFJpPzGrT9BZNqY62VLwSzt_9wiFoBTMxH_HzP-k53TozUHD42vU_WS0SffZ0eJtbkmp-Onyd-mbn3O1z5eHyT034AqC4yJhyDgACYxEJDK-7tQTgrkp6S7_0risOlM0Yd-eNr0yd3pfYmh6cQ5PKonUMb2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=fVL-Q0YgiYAIB7NATVS0D85pmKECNJxpAJu1dGSdiYS-vmRKBHL29I13Y5sKuuQP-vbAOzk6cctmo1GHyOe9uy8Axo5uVFB5XAhLdyLg7h1LB0ceOoQtEhbc_7p1oGKMQVzDP9eZcZ3zhDM9gwDlH2AI8qvO8FyopxnWZG_6Eiol3kF_8zfDX6zVTnBFJpPzGrT9BZNqY62VLwSzt_9wiFoBTMxH_HzP-k53TozUHD42vU_WS0SffZ0eJtbkmp-Onyd-mbn3O1z5eHyT034AqC4yJhyDgACYxEJDK-7tQTgrkp6S7_0risOlM0Yd-eNr0yd3pfYmh6cQ5PKonUMb2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=j47IPDJQtkDlCjzPAfNGWkPkhluOnE0I29OEFbh-iNnKXfjaByYCYpP9uqe8CN_MiO8FQbG-r_C2rmRsJQYCKpFTANmfNs_QQ_3rABof-WmeagHPBSy1IHwAdRWPPqJJ-xDUdYF1clVRgTxtHNpnpWBQZBX7ZwY8q2YKUYp6nLfRE4vHB0KggK6-LZl0bm8UGxBZpUKwvfHdmj-6vtjhS0T8g9KFSJmJ9X1GHOTcAtCBtEPH5lJyUpFNBYZJEfJRD2M9Yol2McBXS6GR698AAJIp2ESwwkOpSH-jiZGTl4487MiBMIoHKLvn2Yqnc8QbQRjfJ3zQNjhzrxqaHJsH8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=j47IPDJQtkDlCjzPAfNGWkPkhluOnE0I29OEFbh-iNnKXfjaByYCYpP9uqe8CN_MiO8FQbG-r_C2rmRsJQYCKpFTANmfNs_QQ_3rABof-WmeagHPBSy1IHwAdRWPPqJJ-xDUdYF1clVRgTxtHNpnpWBQZBX7ZwY8q2YKUYp6nLfRE4vHB0KggK6-LZl0bm8UGxBZpUKwvfHdmj-6vtjhS0T8g9KFSJmJ9X1GHOTcAtCBtEPH5lJyUpFNBYZJEfJRD2M9Yol2McBXS6GR698AAJIp2ESwwkOpSH-jiZGTl4487MiBMIoHKLvn2Yqnc8QbQRjfJ3zQNjhzrxqaHJsH8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPezdsU_hFFgawlO0KeVI-GLcODr65bqzuDQomClvsgV_BIgKnS4P_ctmdYoN7SUHdzzzfSWd7cZkuUJV5KhWmaioYxpTPMHJXgBLne8VX1ZG2TKxlI6ez4L7U9kvtZLSgvPqreXtZgTI8CwsDfriiWfp96yRLGzjUOF2T2dnjaNklkz5AgJB199uDleCt04P06WHhXoKsg8zDMiX8mLuNlJx9ry4Ogj1scAQlmhO6Q8nMInaDELL1jRTtLZsURCvSpJOHMG4THVuX9SSBOkr7tslaOVy3Lh-i-rF4AiBiIGfrKfbVHtXz6u__5lYWkpQ6TnmWGoXvLwEgkLCmO2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0kol17XAY-8sas3MGB24Gkv1ZiWONbnBTg0NFsyPVbn_qK09P9wGB2aJbwiJLVvibO7W3rspX91iO2cFOJyL_a4HHGrPF4fgpFl5epUxXM2xZVD3VTDXpm5i89iCTcHfMSU8yVJSDSV4zxLO8fFCQD4lHR-bQKl71M9XRV01y2Db4A-Z7FW-BW4X_JuRp0c09uNiHqZp3vcE-7PZMZQhJCzV4boCTo1xQmRNNpknF93GXswM1duerzd-NMUXLwGCsmPNuc4xwPYqdh_st5_BCnzv6XWbd4n2iUM5s7wdqrZ6vwcgH5Tl01jlxOAsBsl4ALO0IXr57F-Oej6m3iSUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2l_3YZelAQzAwMrqzugI7_5qsXGI2Sk3n-IHNEl3j1b4cz-qW71w6e96jNf_eaOYDRqjlBEV0UTWNTI2EbOTHtDcrEeqVvH37TIkwPtA0kMDviVMdLJ5wALaATgV5esAOil-6GNy2vfBH9ReSiLNNdXE5qsaHfMAMrYy6BlPD65sSmAsnQHdR8NRRGdYSpM5VEtUSOnJGS2FcFi-caMTa_NzKJcI8_H97QU9CKx7EluFoTtWNaWhQtM90XcvVoxpU2mMvzfw9pWC_kJGvYZxeQtfl00IpdFyrUjITA-_lO9plxTPGtRh4laNR3OM1d4EuOeVw2FDlFYk0Mt-2e1-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HauyCZ1uehA-YYFv33YaISx8LNhapYW-UPtM3Pb1AgJAybTU4ZNz_SD6SninqqimwhgC57qnJKmS8-GZ2kdSlEb55Kl9RONYe9hf8vIKpsheODcrxTiagroASkFlR_UvLdBG-UXwWiMbLdL2e3cleM3zG1Q2qH-yRNEbFW46b0aKoLcLgHd90XM7RIQMgoJmi9GFHW6KK_yYxq8qQ3hQY-LUvXLity6lsOe1A7dJpxuAy_DjTGn2S1T2f5OVBt4MU_ev88e7N6UBCSPV3mK6qXW_OnkK8x62K4k6H3zToAhh9AoMKnmpIyTBmxuT-SFGI83DAtDoALRUZrr41WI_Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXN1BL6nbd6fRTBrfywG7rGRhfNcM1JlriI1F3lAxWrlZwACylULYgLgHvUPxYGspBcHmZy8sED2zEr5z8NmWfpHlbiVJ1pM4cj3jhtMz-wumqo2WwO1lxMj37Pyd9DZOWEjNin6bJgaZOy0IkUnNfaNllIYBhRS0lTF23XWzcL20kF9v7DXBjw3jGLTlB7UJAHS60YhpkIv_xGWTy4UtANrw8Dfo9Efc041Zkym3WyloR8YUVx_TfwDTg0_ZQCeFagHOnUyu_xGsyOnd48qpDhDEMLkZ9KMwxaZXHXw0E_U7EpXRxZcpxJjXkBATA2TtOIS1PPE-4Ip3ORjHz72mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-etrp1vday8DDLVnGhIeLsapjx_OedWUR4NkaBvbWhJSDgAcCmTw_8wPk2iJ62OfpG8PrXMvINyL7u4OE3WKaBdGt3GNxiPanR5PbxaBlOwO6KYI39rj4lrGABCIT0zb1pBYMxw6n-eirc8lUHUfV4t5IfyBsXQIEiRZDv8QdKJ76_diSYTTSn2SmBHhmeXGrbXv6OefVM8jcmjmiIhis7zPiuHAxSvzVYf5vVXdcwyIQVPs7rZcHA8Hf9nXySRR0Cbj3RrpWCV9_61JNyVkFy4Sx62RjMVc0iluJ5QhbNS7ApMV1OYW3fHG2kvhCYslafV3NDAfkKCrcSGoo6FjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_zTGG_yJd2p9t1A-qoI_xzf263azGUe_g5j0ydJiKQuYmL7bqINiomTDToOdNtIai64QN7DAmfiGYRsKLmaOS55iB1qiuUUvNO9lsdri3J3qrNjq61itcWPWlUcqqonsagwBQwdxq9ZigrSHP6NtNk14BmzNEwnZP-G46fLFfAgqZeYfMl0k93qxSEpHHbT0wu4wFalJ98F0lF01xwtn9XzM19SCm_s-N0NtlZuThQ-tNul-GIZswz2C6jMc9f5L8ExLLrNErhr7u3mPypfO9t4eaAgaXT0NS47dR8mcFsQa7DkVmbaj29Eu5eXIl62FMzZ9Ak6HoZMx2bCAf5o4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TwIYWM4crVfdpL-P3ss9zV7NBO0zC8_6EeM3eaZ3-5WmGY8fW-CqGV82HIg23HTQ9OrIhi-Z_mBH-JTL7T_bO2jPO4yAMvE9KsyrMJsN2gxbToYo7-fF_8MFUF-fOCX7cWUSzS0hYdRqD9u4dUflJYqP7d82kI_b3i6-MCv3S5fGU5HI-VkpXOYXp1BQrlHgrWcMg6Tl51_6PfzIkhWUb_SoiqRd1VC1GGeF2U4gKKBrOAiEjjKeZ68rKS1wl_y0q91iemzbIoVbFl0ZVpwLR2WfBq9MdCHbS6uwQOycR78nuI-vSUOVwTuJVtcYv7gK1qlIU-CxbuVVY5UsaWCBqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pyuMVcDvB_6qvXlV9QI-S9bTgT8QKHswKBU8ZxEKlFSoIHexVQw3uotXj9mwvqgtfgJiYa5GRTtV3h5LhiEPRRhXpoTs1U4uC0zCjfO9nrxePTYqrxQZypH5q8uDqcwO7lXt9rc_ofXouWk-yuaLD_g9JyAEugE6p80chNhQS9pBXVFUrqK86XOFdZwYANSyrP2s9XhshGqPZt6HXohwNLs3xoox0CUNY1xxoEzT6IaaD8EmYzsy16Yv_B4jbW9J4bO3QFuEhPVWlE-BqBkk_H6dqvypvTH5id8PCyNJX-vIJ8EQed43oY_-nI61-4-RSgAJ3SGk_OMAw0XDjBsYwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NLS3PW09_8tZ-CsW-ybbnQkUidHljMS4K_ROjjKD_j9LuI9Ypc6giJoHHMMRDeMKQe2uAjYoBl2WG1I5KHGqTW7b5OjiOcfwJ4zjscQtghZ5a6nKM9Rp7ywV4WrlcQSfd2gQtblhvIrxODa7AWQWe7GN5w4_h3aLpQyn6XqLnhgUly7Q3zlNhEx01YAu3RW4zSSCcoO1_YhCtQnXSDQ_TPBSdeuT9FjWN_rIHukj-zWJ73HhAwbu7cgFZ97jk9gqcZ71zYEaYlC-MBYkl0MP2jzK6v7-fZa9YNM4_MaL1ZKn8LQ8EGhNrBAIhq1-jRTvUn4OhNMrrtKbCz6HUbejYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=I7T8rR3ErvIJOd4_1JoWeycHOeQc1LDTquExK86eGpVI8s30tKGs2yXSL1_N4CiMY1hYd6yA3qE8rnTxnubRpMN9w50sCcWaxlNrrqjQgvpRkFLPUHE45_WiqWnZgwqvDoNKwRWRWdLKzVIdpT2InkOtsJzlrBs-rmdqAyajGrU2CA4stYw8oOcvs3aVPFdzkL0XOyS8jMe1_zMypyTb5KAHZFVy-sK2kUeO3zRTVV2YVnkF3fz6vWmZlzQDWnIMmNPaMR7aOQjvKqCm-rkAzvfXmpfMQ2GZBKZ7cL3GEpDSF0AhhziQGKyY84hHL3cGhs44Y-kb9YkbAAaDtRpKeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=I7T8rR3ErvIJOd4_1JoWeycHOeQc1LDTquExK86eGpVI8s30tKGs2yXSL1_N4CiMY1hYd6yA3qE8rnTxnubRpMN9w50sCcWaxlNrrqjQgvpRkFLPUHE45_WiqWnZgwqvDoNKwRWRWdLKzVIdpT2InkOtsJzlrBs-rmdqAyajGrU2CA4stYw8oOcvs3aVPFdzkL0XOyS8jMe1_zMypyTb5KAHZFVy-sK2kUeO3zRTVV2YVnkF3fz6vWmZlzQDWnIMmNPaMR7aOQjvKqCm-rkAzvfXmpfMQ2GZBKZ7cL3GEpDSF0AhhziQGKyY84hHL3cGhs44Y-kb9YkbAAaDtRpKeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUEcfJib36-QIACJouqDQVJlnBU62V_jmGzmM5wUvcZyrpufFbiqAWyzyUG_HdubJx8AEw5cAOGrg5ZDbSOwAwUfztwJ9l3BgwlN3HLUA8ohPr3IwHlOrEvOBrjwcGbrPFQRaMtLxk5YIEJfC0kwtpjvyfN3EV0TdXltFs6QjeGSRoZeRfn-mMYy4h-R9TDuwWb4nqOwUgh-5uyA2yewdGyH5Uu1EyV_1IT--HSaqAOlmtopEz9FZnOIe8sAX19wKNBQYedgIq8Z4iw0_7ozBMrkquySlpXXvAg4J9pCKXGl6PrfmyOU7vGNy4xL4WiJ5WgWRp8-aHgF1n09qCXAjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZT_YqF4OoTjdO_XwUknG8ZgzKobenGxsw9OQn7Gxe_2F2RCMdi7N5RlLJ8Y5rGwK8VQ28a-EkDDViWKbMOL08cmZFIQpybWsIfdHI1S1yQaWQI1RBxurYGVtjgXKLnKA4HUG1RzUptG5lpq8wbTTYeStmz-gHbWVXpicoWodfCJjO9fDt4DHkBEn0X7P9B8Mec2XwZN0zxl_dLQc5-rNwFSNWz5gnCDxKt7QtTx5_ECTC7BwyOBJxAbzduBNf-8zRgMgkLSuzLeB_s7HnTvxwKLtvfWyoWqtisfhY-FD3tJLrBUNBVqt5kFUH9VDCPP5uFGIhQ439WGDAPmDevplw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=GPbVpRlsb3FvznH46qKt4Jsb9445pA2Pl5kF-HhJXuzr1WLI3ao0w0N4-4MstmIfhLxiY_SAemgTPXtnjBZQlifxcNupJUB4xbHuCJIaVy8kOT5fYhcvUD7gb9sNzeTSE7ve-NJjGCd23JNhPutRCFkyzkTOxCbZWfU4AnuHTX7amcztpfmcpRiecXWk7tICzJzAGF-NdOZcPHhi5ME16q0bSavNMABcDq0VByMgpi1X4vIBSVaRMyOxvcHkOGU0uifk17yvjm4xPL-Qr25sG9UYZA0bSxqj-JfCidGogo5nBUk44k3Z4n4nOtB7JN5c0dtaej0ZCVWoIpgS2dso2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=GPbVpRlsb3FvznH46qKt4Jsb9445pA2Pl5kF-HhJXuzr1WLI3ao0w0N4-4MstmIfhLxiY_SAemgTPXtnjBZQlifxcNupJUB4xbHuCJIaVy8kOT5fYhcvUD7gb9sNzeTSE7ve-NJjGCd23JNhPutRCFkyzkTOxCbZWfU4AnuHTX7amcztpfmcpRiecXWk7tICzJzAGF-NdOZcPHhi5ME16q0bSavNMABcDq0VByMgpi1X4vIBSVaRMyOxvcHkOGU0uifk17yvjm4xPL-Qr25sG9UYZA0bSxqj-JfCidGogo5nBUk44k3Z4n4nOtB7JN5c0dtaej0ZCVWoIpgS2dso2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=HFay4DH-T6qNISD3rX1Dieajzr0TwYZXuL-H4duA3La3prarahGTTrX-j54Y2r44NnCp29xlto8QUs7Z6cO6etwahbmzYQJKNmM4VKwkRxqH5iX65OTmgE8wP_Y1OgZr9o-7fvZGTdsYDew7uJFUbAmw5O_LPwNHZagl7jEOnCv8bGc0C91VAaTQHxQtNJQaZN9t0AvwAxj5jP4es6rgiNty4e4aax7fxFLWgtjUDEqjaJw1V_JuuYZKSGMUgrAe4fwrkInePHeY-MCN6uniSX5LprhG5mqm75C66E7ure7gueof1yHsxfDsYQMq7Oq5hyP4Ow5tBjvmYNCza9EbwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=HFay4DH-T6qNISD3rX1Dieajzr0TwYZXuL-H4duA3La3prarahGTTrX-j54Y2r44NnCp29xlto8QUs7Z6cO6etwahbmzYQJKNmM4VKwkRxqH5iX65OTmgE8wP_Y1OgZr9o-7fvZGTdsYDew7uJFUbAmw5O_LPwNHZagl7jEOnCv8bGc0C91VAaTQHxQtNJQaZN9t0AvwAxj5jP4es6rgiNty4e4aax7fxFLWgtjUDEqjaJw1V_JuuYZKSGMUgrAe4fwrkInePHeY-MCN6uniSX5LprhG5mqm75C66E7ure7gueof1yHsxfDsYQMq7Oq5hyP4Ow5tBjvmYNCza9EbwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUIwH1ZHUs2PaL7AtnV0bQ3Q_V043XUHm8nIiIZC0-9OZhvV-IAvKJmFjPIajhoxVfZ6_3J-gQHnwqFnop_Gxf4ZZ8AKKf7MeFh2nBVnIpJWc2lFOVr3FNL1XzqMKTtM20-OuYpYKDzdEVc5gT_PEveA84CyLTWIiOQ5WaUzpqI1v-WBlM87shi-iihdDU69swGH72ri0rtsGOCgHfwJ8u3pfdlEZUFEN9exTaioIY6IK_RhywWT6s9HMfRJKST85kfwt-M5MP7kSMub3K4xk2FRYQDAhozvXDlRtNGW0AEcswf0mKiCglwYD53BYYKEV1nRKknmJ0MJu1l6wjgEAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJs1OxSKckqFTz0Lgc2-bAk73-1Y7-LvFtMRGy8EkRVkOH6l2MG1BWKJfTxKxWqe9vJjyvJcq5FsnCuw1fksX2htsyrRwJUo8RthKkrHpRxARDysIOqWWHcuTiaAzvUIx_lLGSk9-x7-lJceCrsLt7rzIjlhjCPynkv-njxYpwUkzy2IV0QqqDm1L2MV5ZcThszx391Whag3fHo6qp1HboNlMztv0kRgqGlfcBor7fJsbCQAokSDKudiazVyoFliFuLCD2p_DwWRCessCgO9Es38GVeirm2eqO7joFdiZUF5kHLeSB0Erj7fBrC9H6NM3IiOTzqk0uKaJzRK8c2hIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMtaYxdeFRWoLB2CUP2rVdPecg7cxHPb_BVhnFgrxp98uMmXqNpHPM5G-k5E3TAjQ2Qa6Uhh0uNCDbX9iXFbdJWWr0QEol4iY4IDaARovwCBJPd5EznD-FmKZIdHSDab8uNI8Tpx1ts_vBWJy4dip8ACzzE_6rOcg7f5Jd8uPyCbK2JldHTRNnVnO-UdBZQ5PMz1fjOuaz1dYn_pIRe1OHJVHOojF3cYxh7mEiShKkGYFlXA1sq-ab-DV8CP4Q-5o1DNRsrcmC58ecZhlANd_NVO5vwqo0ULS9tj6p91qeu1c5izlgCw9F_4xf0OIjtFM8zAxCXNYWyaVHFwF2nCEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Txw0JMyTyAiQpyBlGXzesQqtPtCmIyQ8tJ1xHh2cRlQpxKv33NhLQPZhYPpMcjmEpbhGBU0cm0sJW0q4F9tm6R86XJXKAo3V9OcrKitnVJ1ZGUV3ZidvkijlO4HVQ1x0zbeGBmX8-0hRjn5QwvvMOHQm9SFhFEO4aiacINMsM1E7Nyg8UWZIc6gy0eyAxzoB5bPp1TWDCx_480uFqNOm04_BoPumSktMkr2ZOLrc4zWNCfIVm9nYiELpyznEkkvfevDpEeLvb1czZWtKB2YVZjPHdWwfYEWhEuXtqHsSQMasSTuoIvVI2ADV_4iy8LIRHeduhEeuUyWCF0mC48vt3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRtOCa4xxOmF1wf1ediFBnvnbsFgFxqVIL4EXv3B9hwSR6IMtf4j9mB9ABP4xwMsba0NxONWs7Htkxdfe8rqs_kRQSIbcrr9d_uvr3kS3dTs3fweHZFrQZdB5zUaj0nmY1H5Agk0oRbksW8o4PRMCmsWw-vGycoGv0vQfyUcbUYD5yVcxTd0EfPF13OpBpO9jcTLa6YAUvU8X65T49tgGqJTDnoskwO6u7jtMVl1p3U-iH4ezoFCnVTPUL63EDb5oQ3s_jviBNUYW-vBShmcRReJQ8xaftz5wnatki7hMZ483jc9yTz48wVlhvLldu2GVudDB8COhDlu3p0yYth5Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PV9Rl4d7db91CTcWDXQIJTQF0Yx2M1JQVRB1Vp2l77TpBwQKQaVgKXHUTVxGDsyImOLTtyKEcZlN1AM4bqEQHJJnrj3Q_guzD5lsxlrNsCAXJ8udcxkLqcTBJsxoFapxxW0yppMdh8G9iCH0JgEoThmPQbgEye2cso2Qh_iWkId05w1sSJYLEC4cG1V1VQgaiRCI0ckgFgcBXRk4o0BBQysrfN5LdEFDL3kK_E_B_otleqf4ri7K9_y5r5q7DUsf9eFBG1vK63zKKSqiz94OXBVxMFjwRdoWsiGH8prMhvP2snEGPXprUM-_qjwTQzfh7hiFzUTDpKBGCFgKY79Wvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSjCZAGt8xz4dSwwDO_BN5yU1xAvgj2gvzmPSnxN8G15oKiM3bRYSG5_4KTF1X1x5QjOJpFIOnYQWop-ZAWZVmWwNo1cohm48CWskAYuT4LH--L9xYk4pNxpLYW123tNfcz5zCoiE-c-M6xWa2vd-eZ8zwlVHV5R5aXOqyHPjyQZsLLujoXZUwYu9n3ZL0JIz0pdxx5LJL8-WonBefB-5dfwe1OQdCfqEsDXZZfluq5KSJ6v-85dNozpCaDFdn53PLPjYZRVb3JuUA_NWF7tHMSUvAZArrRJlYsxdkj82CKcBotxVEFV61jCqmsUAZFgyeWlJ2VoaFRMi9CiJA1rSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqHZMjLgUnXh8fHPMA64MfumfzD9gXf26tFCjfA1cxChxm9TgiaKACGJKrOcwHf5xZvbR0_mMKbJzNhWqN5AgruBd_UEvw202eXZDwA5CcexHaf4p1uhutIUk48d8w07brAS0KhHi1NPDeYIEoXF39R451RlQ_kyIRsaEx2aTZ7o36NZXTpOsHy8VGnoAV8kLjkMg10FUZNqiNtM7SeUG0Ufmk23zLmvCU1FVnRJQdjL6ilRiJ7hDgcRTWEeJwsgKqLevUfdsIqCMWVqdNKliaGnJ3HsTz4n_7ZhPi8UMqYXxWNRLFvS9TW9OyIQHQLdN-u19O1aQhSx38jBz1-Ong.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=VcEQtloaocx4laXODrEq5DBKw1K0QlU_5IZ1eRQXbtQnBS--b7wB5XjpO7r8vZMW_M3ypBX4Wd9MFkdRTWMp9yyvedwOW6DBlIzf-w18zO9d4oflAc4hZ460AbkWImkykcp2jkEW3h23N1cC1ZnuLqekqrLMyuNGXxCGs50xRT5eKT7LKAacxk8F0L4FIyuyTslpzBPYHl7ycINRqt-zpWPyr7kcEAaL50MueVSjqDGRbUiV7GkeRG-BgLLqiEystDKhHfvPTrj8ps-Gt-4ZnnsmmjWk17B9VZLS12slSeXcuOwHLrvmxZinHeOFZP7omRLRwfLya7tdad4lLO5s0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=VcEQtloaocx4laXODrEq5DBKw1K0QlU_5IZ1eRQXbtQnBS--b7wB5XjpO7r8vZMW_M3ypBX4Wd9MFkdRTWMp9yyvedwOW6DBlIzf-w18zO9d4oflAc4hZ460AbkWImkykcp2jkEW3h23N1cC1ZnuLqekqrLMyuNGXxCGs50xRT5eKT7LKAacxk8F0L4FIyuyTslpzBPYHl7ycINRqt-zpWPyr7kcEAaL50MueVSjqDGRbUiV7GkeRG-BgLLqiEystDKhHfvPTrj8ps-Gt-4ZnnsmmjWk17B9VZLS12slSeXcuOwHLrvmxZinHeOFZP7omRLRwfLya7tdad4lLO5s0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBXM8UjGarsB0oz1Whq3VaPsUYBSsXz_c23avtJqAtYYwKbfsNzFtRMQE0CAkh0UU7x88gkK19scrc2CgicAe3kQM9uGIbMkY65urmJoNRg3H-OJ_6vXGDRaJj_6ypT2KaowdUzsWhkcJ-r-fbW6SgI6OToOeAtCnYVGhTOryajI7CYkOIrwIJeCy2NRFrxkx_5FFNxKmxJzmj6Bf4ofj1StZev-gZdg6XM4mtAb2mdkNE5wN5n9fwXVWcKjgCGQ5ZO4hNHzKLmQPzBPQkr2uRII_7MAj1Zoyel0pYuTDF0zo-MqVMzf7OqEeb5GvE8-JUVPMR7Uqiyk8pzYBSG9YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=uMQ4oFGTC8odEv8H8GaeLMYPV-21AB-UAZ8ewCLLNeaXAP8kPKIa364qF5-Hy-uMPOmtrtedAQq43zcuSF2g-Q9uKFETQXj0KMQ_LE9N_F9U9BOjM6eCw0NUjJuTqiqDCZi6Z8bWIC-js8u7C_C-VMDx2SecDdDHrH2drrrnLCr5mKyj_sHaB2TeoZ2bex1zP9x0fYhJYKvDZGWQAnfPmXLcDn67u1tUc7fMi-MO_e60Jdsm-ZRk15yptQ_1J8eZXcCowIyjZkyhf13TQHmoaFsQ1KlFtZ6FF6L5amVMPAJJzMUO3e7GaHqfLIak6XX3baqK3fjSdj0CNAYstPZ58A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=uMQ4oFGTC8odEv8H8GaeLMYPV-21AB-UAZ8ewCLLNeaXAP8kPKIa364qF5-Hy-uMPOmtrtedAQq43zcuSF2g-Q9uKFETQXj0KMQ_LE9N_F9U9BOjM6eCw0NUjJuTqiqDCZi6Z8bWIC-js8u7C_C-VMDx2SecDdDHrH2drrrnLCr5mKyj_sHaB2TeoZ2bex1zP9x0fYhJYKvDZGWQAnfPmXLcDn67u1tUc7fMi-MO_e60Jdsm-ZRk15yptQ_1J8eZXcCowIyjZkyhf13TQHmoaFsQ1KlFtZ6FF6L5amVMPAJJzMUO3e7GaHqfLIak6XX3baqK3fjSdj0CNAYstPZ58A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=voJ3-QXszCE1JXbtFyU3Q67JKbi-UTgGwUpzDuMsO120SQH7XkO5WoYEWRO2WMY33tCdF-Ckhn3ppGGWzQ_d-MqRp44h1PZlyRqjHFUaPCfR6LXPG6_PRO2PkOpReU5gDQ9_X5DGZpS--NW-0QqZq3sBJzWm8TradIiqiIYunm8sooj5Wfu-qE7oFKeqnpN9cH-ejkb2eZ8P5mVaicYBSwJH664MB6OcRS0j47hKFeB7S7XZRRlXvjVo7TPRqMpTHTcfwF0eVfpLpG_i0CwJEnK3dYOtRSsZ0Gs8b_td0ndt4mYDdnNA08L0cZzcirzWvTZ7uKZQRyr9ArQY0FX5Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=voJ3-QXszCE1JXbtFyU3Q67JKbi-UTgGwUpzDuMsO120SQH7XkO5WoYEWRO2WMY33tCdF-Ckhn3ppGGWzQ_d-MqRp44h1PZlyRqjHFUaPCfR6LXPG6_PRO2PkOpReU5gDQ9_X5DGZpS--NW-0QqZq3sBJzWm8TradIiqiIYunm8sooj5Wfu-qE7oFKeqnpN9cH-ejkb2eZ8P5mVaicYBSwJH664MB6OcRS0j47hKFeB7S7XZRRlXvjVo7TPRqMpTHTcfwF0eVfpLpG_i0CwJEnK3dYOtRSsZ0Gs8b_td0ndt4mYDdnNA08L0cZzcirzWvTZ7uKZQRyr9ArQY0FX5Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyvIWfyNS5vAvOVpNQPSuERqk71z_uNaG-qTBh62T4O3wwqY9AWoQfnAmdsUVXcWy0-I2sVThjQ6SQRX520BHrFlaErQ6JObWvpEBKjb_NHNusJ3W9EvuhKshHmkTMUxFOWq71jUxUDqHFUeJTUbuRsxUu_B1X4keiQmZKXOO_AHzkL7z-5JBS93xqfPe254bf_4Q4iNpsLqFX6cEH1XjJIGJgDGPa9nx2ia7IPeB1kperkCeYdz0R761SLcptfwDZdw3g3fCltwCZ1D1JQDCV-26a-cKwYkX_0P4ootfCUrwkWS9h19i_v5NFNuTbA5epFwh-FXZIR4Y5KSl7lgTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dI8BajsHokOpldmlWXHjLIl-bXEgBw6_NBe16znSXGvz7VyYm4cyuEgE2WUaNBGV8fB7hOIa1j3uug0Hr3J-FaW8e4jHus-Mrecatz1bBGw5X-M7JQyaENVFeDLRxDU35T7eErvWbyQ-9QPpqoEx_64ZRF8zQ9XcMAYaQ_xzkIiIOkhyjRnGUQtX2Z2cawsgpHznVqzOdIsStvzzxPAdFhJ1M4b65rBLM9JH5iyZUYs8nA8nnGkCei9iphD7x6vJmd8_p8UqieIcRv-swQXlNN-pTZB5Iplo3HDm6_IGlQ35cf31YQgly2ann-o0VMn6ZW0RYVORXudsOza6ggwkCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=sUfP-dZ9I7ZRFXr2aPhSIth7RZF9sCjMNRV1fuPGIWNwb7NgaEqyixLUdC0nd1ZAEkiOYtU-1oUOa44On1abWHmMBFiFNRMlTSQJwIYFWyCkyKjFBPsa201r20JdkNYIg5qc_zkMNTE4LlieWX-gehTI7SKMpcdnv0023iD0sHlpp4xCTlmJPaKUR5tk2_pgjnhBsYRerpn7LyB9ogC-yPWzlJR-h-km07Q6XRFGLFyfH8-QcB7aBU-4AGlDFYSKf6DHshVS_GcVhU5tMwTxmXHw0kDGyBp9iF-CFrDAk3b3PQ11Zyu_5_eCiDqgk9Uxjds3XLtHZ5ZWvqmsyCtG-lz93xxncgRtLI2QMEPkQW3lZlhyaKAh7y6rVc175LXEz4bdLEG_M7zsAWuhXWVZTlSnKuu3wcpXG8oVHKHl49z8LMKemsvbiAwGMioSz0jP8LpxuaIIcq4jdPJ9TisB7er_cOgkgE4S7bqAJCugz7a-5qeoIjjaXQfeYT-d8638aaR5rfR9kEV2C8kOizEn7hZ_mY1OBG3j-10-xeBMYezHbvs93-9NcnCwh7ARf4Hj2wcSC0xwY18IpkiryFQMYeQa1XPWPI7JB2mGGU84ZZLVF1Pm7wN9_jFmH_MiK72lHXGIGVMKwY1En7YGDaU23YUGG6AVWtJFjC_f9NCAcAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=sUfP-dZ9I7ZRFXr2aPhSIth7RZF9sCjMNRV1fuPGIWNwb7NgaEqyixLUdC0nd1ZAEkiOYtU-1oUOa44On1abWHmMBFiFNRMlTSQJwIYFWyCkyKjFBPsa201r20JdkNYIg5qc_zkMNTE4LlieWX-gehTI7SKMpcdnv0023iD0sHlpp4xCTlmJPaKUR5tk2_pgjnhBsYRerpn7LyB9ogC-yPWzlJR-h-km07Q6XRFGLFyfH8-QcB7aBU-4AGlDFYSKf6DHshVS_GcVhU5tMwTxmXHw0kDGyBp9iF-CFrDAk3b3PQ11Zyu_5_eCiDqgk9Uxjds3XLtHZ5ZWvqmsyCtG-lz93xxncgRtLI2QMEPkQW3lZlhyaKAh7y6rVc175LXEz4bdLEG_M7zsAWuhXWVZTlSnKuu3wcpXG8oVHKHl49z8LMKemsvbiAwGMioSz0jP8LpxuaIIcq4jdPJ9TisB7er_cOgkgE4S7bqAJCugz7a-5qeoIjjaXQfeYT-d8638aaR5rfR9kEV2C8kOizEn7hZ_mY1OBG3j-10-xeBMYezHbvs93-9NcnCwh7ARf4Hj2wcSC0xwY18IpkiryFQMYeQa1XPWPI7JB2mGGU84ZZLVF1Pm7wN9_jFmH_MiK72lHXGIGVMKwY1En7YGDaU23YUGG6AVWtJFjC_f9NCAcAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTSp0hKpqbm1ylukAQBLBlPGyxNHL-IhuMKq87Xolz3GnUFSfUk1IDkPd4UZYH-jGh7JzfBNQD_hizc3iT2U7N0AjhqjgE4onmSnBint1pZdbmgh6yLSnHboWovSOGLFPyvbHsKo5IKR-k4h7WgHdGtyzRdwhmAF9nfVtvLDnHocYPaX8KcSPPYhhOCRuRNCBbZM1p72xR1tyysBsxcK-jc7P_qjN_kdwjZo8yTBTkR8DX4D8LxD36M5PtNFyAw2CxdTQVio5hRNjF3mDwyZ3XBKc3H4aQHeRmCZkl4eD7d-rnUADigoqI8UUtUfO3rQyYMXH3IPMnqqmDmc4ZLtvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=ClET-MectzuC5TelyTKU4-nhCddvb0IOsxFhwX-Fqp3cGCh-boy5bpbZSH-mIAlNcLKQ5j0AXcEmG4IfAX_LGl4xogaLNwGSTTYdD7T-0mVSRzkB49yHMrSl-U5gJLmd0C2QZPkE-_GgELHT2j0n7SyYzDLhxcGgXLJswSK89LitMfSc9iyu7NnrT3rzLJCeLu-hFEX_jZvBBu_yjKqsbHHkT-gJ5evpr8YYYbCkhdSwYH6oz859qnC0VgT_ZNmrwRwQCLki99EQ_kgD72K3O2DefTpK8AK7yRL7WLxrrk_wi8Vpyrj0fERf32oiIYLmbH36oey3EAla8aHB7rkgaovtV58Qg52h37gq6u6lWsHVSxTQrlFlJ2tgUYkH28LcIK9jtkDQRnrbx0k5Db6_hlUQzmLwxmXeVgWmqT3ysdlgy_gv42apNlrU6llAsU2DfZT-6La1gZQ8udczNOiFRwlfLzfiQYrZ58sttP2GgyYNB9_OnBJsOt9EX5VnGzT_-i1nxwnaSqhQbD07eSTSPk6oHMd2GNAHsjA9M0wmRcCQjzadLAANMx7Wdmtcpo5LyKSE2IZn5XbkLyzY4yOQfFo1L86pPKgS9HXm7xyCpAdNuemB5cQpy5r2ZkJ7G_lg00XfvBIW9RkgUE48S1bDnga1k6EMwP3JPixBOVdJojU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=ClET-MectzuC5TelyTKU4-nhCddvb0IOsxFhwX-Fqp3cGCh-boy5bpbZSH-mIAlNcLKQ5j0AXcEmG4IfAX_LGl4xogaLNwGSTTYdD7T-0mVSRzkB49yHMrSl-U5gJLmd0C2QZPkE-_GgELHT2j0n7SyYzDLhxcGgXLJswSK89LitMfSc9iyu7NnrT3rzLJCeLu-hFEX_jZvBBu_yjKqsbHHkT-gJ5evpr8YYYbCkhdSwYH6oz859qnC0VgT_ZNmrwRwQCLki99EQ_kgD72K3O2DefTpK8AK7yRL7WLxrrk_wi8Vpyrj0fERf32oiIYLmbH36oey3EAla8aHB7rkgaovtV58Qg52h37gq6u6lWsHVSxTQrlFlJ2tgUYkH28LcIK9jtkDQRnrbx0k5Db6_hlUQzmLwxmXeVgWmqT3ysdlgy_gv42apNlrU6llAsU2DfZT-6La1gZQ8udczNOiFRwlfLzfiQYrZ58sttP2GgyYNB9_OnBJsOt9EX5VnGzT_-i1nxwnaSqhQbD07eSTSPk6oHMd2GNAHsjA9M0wmRcCQjzadLAANMx7Wdmtcpo5LyKSE2IZn5XbkLyzY4yOQfFo1L86pPKgS9HXm7xyCpAdNuemB5cQpy5r2ZkJ7G_lg00XfvBIW9RkgUE48S1bDnga1k6EMwP3JPixBOVdJojU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEPxr-uBUlfm4Ltcl1Jxa8cRLxw1KBSREzorGHH6sKALqF70hiEc-B9kBP-bqpJftdIFTdOAVCFam8YVweb-VkkXxroHBeczXraLlRngfdnzBWe8Lj6H3OqLuYaPamOKasT7a8yLVrk2iUAH6N49Jmgdsf4k2Tej7JTqmZlXhmbFHNx6Xu5O7RTsrNsA9SMNl623RjxUPKOigDExZKaV7oraYN1s2LfZwXjZlPuYfWkKT0VUKzYxaw2rUev9P9HKL8uHxjSeOSyDIcb8nt7LpxKZM55myO9S2LnizY3Qlb0rJn_1oO7JR86MnEBGK8V5W6A3Lo3S7FKV65pIg9WTKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvwCyp4qda8DBnPU_YxpyRhPEfvjaD7u2GCC6BaOgSrMXssdOX-TJpjegXZmF9xIhY65tv2MVBT4l3HxM2Z29d-hzfXPRqo-Ody3DDbT_s3_oJ07AKvQdUTfv67O5lM3AoOVXXLJC5H-J2-u6ThY8ABX2yadCl4noA6B5ADlY7YjkIZgmWQyW4mNX4f9kLQrNuwGlVjQxzT8Idry5eCGJG2HAfGZ0yE-t8GISl06U7-xk9BLzi8ThW44ems3HxNgStJBJkoZLvdhLNj39ThBuH-29w7s9_Jec2ZceekWijkeqht8_5uwrj26eLkpr1BTHrKnWyF7oma6RIltmFLIQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkSQSujqHdTYPLeld9Nq9jBaZVttDaKAROCOwQOAXf3OiWkbrIPkpCjcRalGr4Zam_KN5w-rUmFKUp673yqCBhGqc0guWAdBOX2hA2qh8wH14mB1KBsNMYPDOt57g8m6v5ui_qyVwHeE9JShtP6YmyKTzQ5uc4mUKimSjFh2k2JiDG_b8xHijsfc16oZs79wJn_n9-QzB1o4sqdhtkG6G8_G5rzZ5B39NHEi0fQ2_8eHmMb7datB7FwCGyEjalp4eEDJ_in_LDqWTlwn6fGfzAoFIZzZPti4I3vLKt7ewzuuC00z2GL4QEL8-5B5ateTJmtLiU4B34HK5vCFHWVCYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsHAPPTDMnyc2BMEDXi52SXaSBVVz_ACuYwXRo1BVPd1ZuYgst40nInvtesMexiIQ5PTllSJfUuD4JxysjIQWaMYUUgW7UGU2byMa06DsXiM2Ou3i1ZsFtRbLab-YT9WZDikt_kPj51G_mg7GJ7Dv7ABFU8m2lEr5p6p8NrWEZX0CkIMcJTcX6luw12VjiDbds8INMWQ8iliwrzt_wELf_ZA8TtD5kHjGl-8mp1RFkBWBeDyAfQoEP-DfVhIV5CrzxlzmgFnjp63G5aZvKk9SreO89UyFILegDgWXF3hQykiDs_Bdc-YQTOjDETRuZfp2BJR7-JrjBYDm21Z2Ir3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6Q-2DUCZSiIKhAkjGcMLotx0oO_Y2r1HrVbxgU3daHrcoSgjOFtkzg9vk9YsiAk0XgJd-eD_-VZznCs28-I2JJ6uD-l0W8WFE9lWsNysL7pNmD1k4WB1mpxto5YnDNeLwYinVGJHD077_0ynZWmff9Zl64j__pJk3kPCuyu0tkmNPUBnz3JDtn9JaoivtKM70CPqvRs8uS18iJqYriIrklGBu2ZK2PKBqdr6nZr3kMPBJaLxonv5ax8jfYPSdkkzepZiY5TriiPWdZHxy2M3xVPmtkV56RQ9IamEiNI61Qd_RrDhV9carZ8Ds5VXwebnMpi_wJp74RZvx6jQ3uI9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWhU_0xa3B1T4M2vJPoSf4zFjWRGYR0R2T3fUGIItHyMfYkIdWLVjMlmGeDhFOvUHUhXvWaSaOAKdOLZ_DS53wgaSOQBRq6m3L3saog6vQVtxSl_bS9vxCd4J0iU99S1Sb26Nheiv_IWAuDldVDC4U-Ii6jifVBO7Ec8Urfxj34ChD3tSbcICG314BdS8ZkZ5EQHDRfQmlTjqWBskHP_7esU5V3GfH5JKBBvlJ6o2SD1xNDUzlYMkMJ-XgL80r8QM1jb-lu093h3-EP1IfQy-KYU1lm3_2inAONaMmZxDWzWZZgVYhLHjnRwIvVo3ZHcF4atBViWMW8lFDIlN5YQoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kd7mXDs9ikUikNt095ZMVqHrpUblVf5caVBU_f7tS68PqQWMmca4ugHVQcgv0kH6PlEkBu70u42DBCwvEDCe_g-JUlR6EQw1QzGROs09AHzNgC2AE2bo5Z3OB9_dM5QpJb1AI3H0OtHJLlzPTGEQeWUbyfAm3nNEeDTpL3e9ZDahsUrtnIoC_mHiuL1UlRmwsV5cR7w-1hC6qWXpluLRPMSoVJpKi0g7gxSyPWErJrB-7wi9aU-UThwyZJHjL6DJnxcYOwq0ekI7bx688Is6AHP3_xQUQNzbErojlV7YbSnWs-wrjNSskozZwt_NRnxt7lGAssuOzyoxF6h6MyvcjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdXqj9-YTFPq62PsKiEqXWBLN8s8PGFJJus3aUvwc10r2P02GSrLTFY0I50BuE1ZDBSUc-waL2mHd7LShrlwZTr-kMuSYeJuDUpPHPUqXwQQXBqEifJKb138Mu9My4N20dvwjfawKBbQ5TvE28_Qat9EhWqYhSN-kHsiUJ2NXQNfK8m61CMkta5nawHKZJV2y-VrxAr5Hr4oN7rtA3MkBvKT8DwzSHpRqIE7xxPOVNgEnRUMzpSY62ZAT-60LcVM1zwUwTb9_QGzu328xIZX5GhFPtKNSqVwdJv14YMtYynsVWh9fyUqJNSQqh_VH6QadQwIc-qndf2MFBd4QZiFyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rj5GfdZ6vQQDKdJmw5JXyDcygobI3DCPzMkBdEICwi25o3uFf5sJePjYBu9zha3SVuL8qBKEQR1yyx2GYshpPNPLcEXHZDAWaOjOGHdf_mmGL0yaj7zCEa2xcjqTEDFfP3n-vTRnLO6IkFkJgf0RSuZYsP2xzyBtW-JGbDpWhE9-zZIcnUzk8Vdg6zB7OO5TXScemMxxWn5g9UDl-Hz4moTAo9m-vFExcIQ_1v8FRCvzJ3e2T8kTv0nkuPhk_oqOD0wg_f2OnKYW-TW3MPMT8VPZdtY8mXP8oRKfJ5MWhHO4bYTsiATd0L-nWojXzREA4vd6_yzt9vpXYlpSLexdCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgN2Mc4VbMmF9XGFr_tSEN0pupqUnlHo0jNA07Ctd6Rn-jg4js1GKGfOsKrU20HdaLega3XfdV4-dnbYggxghiMeeTXQ1_nQY8Ch_M7w-J1NRLcEjScr_CKRFtxsRcjabwTuXFGHmC2jfBZFjouvfRTbuDhhnJ7ipXwsTqfuLuVlaJU9gXmCvkA-J0mpIGP67O5GpYYjwAC5et-ow50jxXPFVk8ocFWzhHh-u1UMc7sl_rKh5wHiKH3XR79uUk-Y9aFF_rehHimApd6-d5SbU653SPu785tKV3stA7VUGqnu9diuGCQmmpDHUmu8O8woCXonPQTpIuhnfmqfgCviTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M77nuiBqOaIqVeGuh1zawV7oeOMXImm26FDkA5fAvrHExZM_fNnThmJEkhYUdOfflxW-6lJ7O08M4sIqYA76zxz1sRy9-WDjiJhOnovsLdQBBw20ulIo9qkFlTp_0-rTB3GWKGmo6kDGdG90-18tIqnR4QT7pr_dNuLm-w3AxPO8LFjXfdESSqW1KRfUrixwVtNQLn0Iq4Eo4bhd6MJgwrSZDxhBEJzkEkwbVqd-r-KCQpUwQ8iGcqjZvGu7OdaxaVc0GOExr6Xx-FmTvd0GvSCp43yJu-QtDFrh2o7miA1Y0EOiYiUmnahioq2i7pQ6ruqNq8fIiJgXbk7dnv07Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3M4-x7mvP9qOAI_qXO2ZbVdBcHpm3DGNtsY-OVD8_j8ZgBrMn4uKUfiLoBMhLLlLc18rvqaQ6RrFklMYtRFGO-G758quhaNDfTs7ewKuA_XWPZMQA6hyIg6VNCXVNAkf2pfoyb0p4_wfv8w4AwACvit35yuvf7qdZmJ4nuwAK88iuPr8UkY-abokzww-nifvzYZnW90dF4ig-FCn3q_m6yzuzs7JORdPPYXkOtOSZsR-nYu9BTC-qlcy6AORoRmNPstGSeQWPM3Z4W3xM2fg-mgnoNWM2AtZjel1SH_BT-SrTGUlIZIMCfzcFD0W4qyPoyp4RrCtMlFXK3_kp56BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aj8i3fxa8wx7UdHX6yqj-vGcR4N-zfhoo2mjY-WNozQNypKuxvHgRExJECcgjiZqsz0hsaK-vKqH_jIA0OH1EgRE1umYuSDAbxCDE76T9ki7H7tTx5FoOjlBZmwAdrSpHZYnPgDdeumMV_r_-I-I1ArBHOJetXU1tx5eWR6AxGkhNj6AXh3U7M3R-Fw19Vt8TvZ9Ruq5NN-KhdBq-Jey_wI0HBlaCN3OWLIG_bH2MTrOKNT5SpDG10Yj5J63lvrjEB-k0ZrNL7Wut_PY3fGAAR1OfI-VJaCciE0JS7-JcOou453zb3hXneGKQc6g1lgXdPxcW2QM6xZ2lVB0o3yt4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq5x0rGY9httB-laxi6m4NIBeX-jxCOdHkWfdO6WAgJgbx6D7AJmWrZtA5myQXJrBxMx9w977msufgQdy_sJVbmvLQeHfcRhFy5MOq7Msw9GXYxXODuYE_BTMWR_sdaZlLLFq5H0KHjcExVrzjOAotzi578385TADSHNQi2QlxZlnqS9qPmhyssJ34djavnZR_7-ure7IqxGm5gSfmaDooz6Wnps8r5Y66OT23E2RBvVoSPR2Q9OehqTneqcP-YI1IISzokoX7o1ul9b8n_GMUjk752bov3uf3uH7HGm9lkGy_BQjirNbS6vpGRbXjuRtLrw_f3QwmX9HBCr99Z_vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0GTcUOeXYke9xpXKipoJX3Rq53kij63ObR3Pouh_EEqLLSsh5eVwHbSeIzRy2Ymbe8t08sy3Io8B6TV1DxO7GCnOjyuK8dLE7tWfS4gH6kjzKFxcV9knfsz1dYrW464Fca1RIlOIwIKiaZuZTiGp9EUsk9fgk-LkfnZGhXJTmsXtUUiCsQ6EjV8C3e-8AQ-ndYqUb4z7cUDRMA8I96zKiUZYPX674WplTPv8N2BxGn-2z257fV-O4xctiFj0yUCl8k3U_qHBPoJ8eLfo4FE0PnSGPy2YUFQM-HjIXfRlSOknRVfO674fp07oWb4Teh3Sov4dVuxmuIknBfvcJStUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4wkLKcFsiXggnhLbN8MuX4yE6VLUKxMft9tg59usaBRDOyg6pbq5sQNHsMLTUpEi7grzTPU1u5X10eit16ASpSiDrMfi-pAPJw9Sbtc86sJDWU2njuqK4NFjJ5jk335wrbOkEuNXySoRoynbCTRC6xv5ElUIpq_mLLFcdSCLbwEh8mdsI0ERniZpj5jeBfDJwJeUqL08t78uPt0l5QcPvAEaxKtSxcRmG6-1KF6pcf_rVRCDKbPtnWehpTxbpr-lWKBXUZy7tjqA-KskbxJZqKW0I0bUr4l7nTVz5mkS1LnqV5xjibbdQG15fCiokQGlCRr9cZlUlg95V_RTSiPew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e3IcAPX6uYRrvfUSKnxeUfmLE8YWKCl2OVdgnHEx_Q4yG-iEf7t9bTsD8VTw3_17bm12v2cLiGJChxqRw3VSuoVc8YXrlUXx7qzqARe6RGeF871Dx5PVVrf5KnVFKwlaT6eQjybSZkYmTP2mLTncortQYRw2HudGBKC2N1tTbQdbcs06r5e3YvkRjFg-GXbHLgMhuVWFDCQC4CPlLpWxtt8RbcLRmDDKVZXneM3f3PUEYEOJB9q5OjKEA3Mi2DeaaDpQ71a-c4LhrGHJrEqOM-aeNVbzTLw5DDlqwY4Rj-_qzYCBkcABmFKstbXRU0_d1FnsYzWAFMBJAeN-9rMZjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ck0j1GTdeMf4uNTZYe_DneZpbNKm77-3pkBvkyuzXp2gMcsVEv-8b9BAsZXbMPbjzgZMF2nS9Ldm2dYreQDRhKY37Rixlx2hVwAv2Aw4-SjnGKxKQQhxbXH6Vze-ekNzY81Ac57oNYy0qb-Xjnx66yP9315fPcaZl2VdBDGryTgCdf8eo4VXFpoeBWvKSKadyyFTWDluB5HtZLOAqackcLS-9KpRhEkra1eRS71GpdZGV1omKryNzIVfScNDp12L3548TR7lPH54_n4aBEBnJjUpgFubHhFmRt1iMuD672LuLWWjrfNKoltRZwTmNi-R6RN3HQcWyK3j9M1BAtFBzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5tpsf4woUotzFBPCLwNJexcN4k6cYDhXPT6DFHx8mLFh-Jw2ZfV9NWR2XGG9wi-ZBurFsOhNF4FF7qKlTO_EsxHvFpfudRUR4OtoCEYWXiARz9VDDTpre5QEO10dbEmptviy9Mpie-_pWkDxbBts5MgW5n-9oHCiyfTNC3T4D3yGcyumaBdtGPXAL0KJWSe05i8gArwZHw42jERQ3o-wWnr6bIUaATlPClPiKnZaVq7MPMW7aoyYaL9AIZZkR9utqnVlP536Tft9_T_9i8S_z7oZkKCayW6xtKfY2FS1BKaWohO2THfYOJslqwd-gj8PV8N51PmFHx7cwmWXxX8QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbYpzhSHUG0oxM9j96z-_qssGln79awa7q1r6YLpq4nuv_RKP6aBmDxXSVwSMn5EGb-mPFYT7iEkJTLnl9L_g1WjmRLMZiX8L3lZykFio9C4F7HayM9in2kQkesy6TF8s5kACZXr7VSioy_0CDwuVWo1qAuSUavgh-prkUOcgcXfZOHdVrqliM0ujwdWx_jkpINzStyIqoyNA311KGae4Bd9q2l12uoP-cN8jXYbVWP0mGzOYPBI1TxdEsmLlXxrjZvRxam7VvJS-sbic3hKt1BxnNl8u2GaVhSKMZnIkRU6expUo2Nt3eLUSNRfHFdQa28xVsMb3nUrxMsx58zniA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViADKPMpDqySh7Tm_W5z5wPRtd_sCvWiHfJ1wmgSFx2C0c5_cWuXU8cO_W_eFiDkG5oYZo4ovny_R6LIpP1JOKBF7OLclvXpv8up6h0Q4-v8Q3FRBqs1-HvFuWPyci0dsDvoZXA0UKHpHpkISbTAZJmIScWtOV60j_faUuYOG17oCGSVc9Kq6xGw4D6FePwWK-YylSzvTv8xxDSBgH8MSeJ3wCoGz11Ttbtns2OBo_OqY92yl5vnpMCrKECTO81SbC1LVNkpSPhVQBO21b-EK09_Fbr9Vn2KohwR99qqRvJw1YXgnQi17ZXFNepqfHTdRtEHGVLLgcaj1TRZPbxmnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8Lz3C8ANGzKRWyk0lMS6lUiO-ahDPaZQHlMnBaTun4sRKTzujaOIyy2kD8VrpOgs9Spov6oaNBJr786gcB4QlbAQJuotLqtFX58lehgEz_f-J5qCFV47QeuZhix05bIJaDaEZmiYEgJK0d_qPf__QluhAI7rH51A1yQsXWinUr2_SwJlXO0RtxDwt4uuZdjbCyjYGicUDwzSADcodMEFd5wog8bYr4-u9moN8QAHS-ZIiHcGN9-Ky_iwH1-gJZbCywae-d7wqVFEE6lVjuIk32CFuQcOy4S7gNZ9szQvlK86itU9kZM0KyHPvtjIuSek2bF7xgiczG44vZQo8JmaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVeXLBOUCMNUY28VuHkZIQGNQ6qHLibbevGzrS__OUSus3LtB8EX1bEJE1vwVZatvsFCfKI1zrVBWlQbICh1lrsPpBeyhygPpoEXyhpcIeSZGNvZjiW1G-jwJ_LxUWg-fXrLlePyxeKfPFih5Qb3sZQc5EpdXxX33EZ8FI409H0N9Uhvc9kdaa0_mJvgp-ZP2byhm5yNnPgM99rxCXJMV5kMq1t_quftEweYKVntSfbDZMzx6HSfVIxYQxsAeHrFI95MchXL61oQ-GWrC_Y-UqKQ1TyDUaE6ReD32QPhirccpskZBr7C_1FHzmW4r3fud-oE3GUoy-Znclo08IFd9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOMCmEdtli3-5U-3vBxvvIsj_w0GuUNa-U4OeNoKcid6aqsZZ2Vavgx-TeBiQdY05nJxcI2JwgUvWatpT5w_EI9TlOz5pUAHt5cPy16HAVn9cZceOc5HqJ-SNTrXI1J6XDH2wEA4jD_otP_zciRxkXBgvpjk7BkueD5hshmg5oazoip-Y9XOdTP3qwgu74CLZo0QDf9in6hhh_gXRB1Oaw-Unc1dYNdLn9tcp1I3IG3Of2AYhrUWIOf-9pKXpq1uvGUH3XnMXm1SFF8cithKKvuNvAsiOJoJPAs7DSz4UDbLTeTfJVK3g1ewtMGUWhVd9u7RqbuhfdcUUS5kjQVIkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j12sbMSZVFvW0aD7JeJM13dbAqo4FCGdc8L5jyoWno6U-Vz9yAP_6beFO4Iq0aJ9y37pKFJisIpFzV_x_m5D3wC4HuDiqCQM8320a-GXe5sPSzIpm3Ojt6iicenpyIVFffzB4BpNI0L2oaLTQFtSBHt44QRwrg8OnO9YI0OZJYSCM0Sq3PpxycYDSGbQOfRFdkZQPMF7GECT_gOZ4mPWlajO1SU1xup06qBpqEsWzOJVx_YYnVPf-KDGTqhm9gy7d8e_Eh0mYv_a1Z1Ax6H2zW3wFxq0_ovp_yFxLaJ7rSgT8j2QENAmtaEKTiHDCUq6El56CK60KdwJczPcDVpeyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/js3igDcCs8qrc1scZLaa7aK2Bzqp-d5gJLLs09rJ7OCDdAfh1W0C3sfWEQeT3uTk0K-DkpjbsH6SUMNM2N9d-fADonaWF1mQkU8IYi3gK_BxbdECUm77-n7Uio_AlggiI5YZoH4JyNoavkg7UqOIveF7BzacictiUK5C54u8e5tzqCebTGpSlQKugRvhbSYYD2NLJs8UDz-TGqefPNLFFh28Z-KQ2Wi7qxzbaIicEnpJimNG8TXCZAIQVUUPEOMvs8VK7rF3ykxhLMj_R3xlm2zfp3hMKwKUBBEg0ywFHzYv8QIlujZExrwz6qqcoKvOLKtVLv_jG8lsjqR0KLZCIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qky4UBHrwXF1LmUSNZh_ljqBeDI0jh7g4ecaLNas0lfJ-RALBRYJvpBL6jOfR3Q8r2e6kvGxeXD4sKaTS5fzgMyHwj-0yTVUJK4rrJHltyutsOT38vkzaqGffS5SREaGeKs9td3N8r67d9BE1n4zEAw1AzRDxW6JtQPkdG1uyfwhe2myXBoMMRRt8XxxaxIxDHGnV9lu3yBaIvPyHtcj4JMtW0RobT-ggfDIejc8GcqzydQZm5HTHW2rAONbMeu8jNdTm23AODmn0vK34HwVHTMZK3WTcm7R2rThV9qNwsedi2AM1GxESeUGQqOROGVJ_seQkFZU6izatIJA8W2Rdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPg2D4NzNL_S8mRw6BMvkFIsFvCS8g3UB7Lr3cNZ3u4k4dp2h5XC0ovaG9NXzv_fcASi8SpOfZhdIunfjJO5UyAueUZyBzFp3hRrrJJjCqHwh2yBIYzQDUHC6Gjgn2trXONY7dysAZycTQYLc9AUANiv3F1b2hJvbI8tiAq27dvutou6hyqNtZocy7w2V6bZ_5xJColLtOyhPL4VTt7yXwJc98hcHh6UCnlw1xHe-tQ6FQWHf5CdD5fXobgLIu0S1m6nZq_i5WMyhbVRuKD_mhRtJTPcPn0QB8pre3PjSgBd-D_OLGRkCeZwScjigsgDdwOKOEL7bb8V-33jPFUHBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxAAL8Y0WwUMwR6CxHQ38ceUmd872JqkDf05EEV32QgcTT-eCGokVA_7IF2-3AMNYqC_5Bsg-jz0_R-oCUJfDmvxF1jDRJsCTqwjWkBbjLm2d-S8nxa2QToQoxuiUNhpKZv9ieb-5P1Qw6dqBZCrkX4PxC70LT_ws8tt1FW7qT1eW81GXiSp9cCRo9spsQibvMskKz0Ogw7-yUrhN4XI4AeISB3H6X6CJP2n18zVigWOuIP17Z_oXm-YZQyYKokU-vnF4LTJ2mC9myMFVBl-cLcYrlkiTXjeAmnbLDEz38Rpb-eJhY0AXThI9OMpIyqltOIb_9CUPQkDOUvrUbw9ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRSX06D56RW2JIOjKljV9NXYoS-ABLX7wPhkoCKKAoa0IH60dvOG3CtDeNfBrN9ePhKeDpHsMRSnx510ra6ZpCi-Hsn8UOPLJoq536OGrrC6FddKxQK2jLEvco9rWKjijj4hEZHeXvdZJuTiCGRNkwT2G6yRUgA1T2_P7oXOviS7nAC_7BKv9Lqu3InSYusmT4Klz2XoNc25CEQvtrEqhtnCHjADWUU2_ffu5EeoDCZnjVvegHSgCNg2ucE1XgT8CENbIAxWMI8SIGryk3ZeJKzCwVIEbs8bYeqJyx9klQBUy3j5NK_yEstoR1Rrkgo04l-S25BQKj6z4x_uIC1-vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8OKoC5BFWXQim7YkpS0nuZ-wjbocBNcHgkg5H6XNmR1Dagb4iphl0KmiM4svcFQ4Grf8euEDaKsOSxR1tKtp8G5f8BSGliGOzYHPd-MejttNlTJALks1CRJfjFm1JBCvjFFKEQkKEkMpONlVboEgj7qEn978akqwLA3JsQ7LIziCm_9P6Nq8lW1x1lk6PAFUrFGkCKeEWyYWNMG2DJzrcNE3BmEIZYLIsjsnmgZf-tiDtlih0CvYng2tgRgHJbZl3xHlyxSrHBvbAMO7SG3_pFsAQEQqzNA28glQy-iQkuijwpnbwS_gOEzC0tavkFGTmD5OYWk2rJK5UhfzsaORw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svqWkEZnx9h2VYWX2sW2nLqSJUbnIvMQN7KNvGfRlFQHRwxsiJoTnPufviDkC78DFYDVQuh1q6k54pWZN0ZZpxScsGCyWTKUl9arqe-h1ww8oIy5KzZ8bL89uFPXve42uvSmgjSQpDJD4sXWhtTycFf416kUhNRUNLkerbaFJP-0G6wVRt79EdsptpQKtzhei-dHD6i-2ekjhTIdYcEc0aZTgoC386z8Uu3cfa9VBYB8DBJ2mc604tFEpf7HstRy88ToEHsfWTon-EkOtzjMfS-8Y5ZsWesSqUYYZavgqvRBvEQFVOXXZM1HmvGoAivfDpqT1Aom3NPrMTh66Mza8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0qZBtoctIAKd-RCWd-BxLVc-FjfwB2ojXzKmRKb8pBkg9EUKrSu3Zu4DvqyOPqWXLsutxJ48wcuzq3pg09ogUwPm-IgrCHnva0PpKE8ETvwzVGEZUbtPzvciE3JM4jfAjfK7QkFGPqZ6iTxVN5-eGePw8gk7tc3kvl7v_3IQ14rwVFQgXIBHU7iw6FHoSLxwTZrFOipPS-qR8qBcnMqwWYy3svTD1Kj9gT7D1SqugtwHDuLxsU5mgOcNDngFdLA7UjxzSfD_YxxSl_wkdg9XXAFyYjwZV3hjA1NSpkUOccBJVvFFVglPf-cDc-HsXEFcuuJ42mQ20-Jz82Hnop7ew.jpg" alt="photo" loading="lazy"/></div>
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

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIMRfOz2QOte110TrkvXL7ST1D35ZmYHJl1WWiwQhx-BZN6d8VRMkHc5g_oaJzUalkCgHBp1DQwsDDlavQ2jdEvzLGEk8HC7iKajAhkhETCnlpdLNh72zydpI9tAgOXx9P4xezsR0PfSkBzvR08yp3ELfEMT0uKWFcA91Nnv7PSJeiNSGhzKzm1QdPfzCYAMU4ol1ZLnu1W8uSn1d89nfm-hoMraBQN_lOMX3enx9169Za1v_YoFYMIec7pXENJOc511qnsSYf-6Kj0_9TgNDlcXYyme-eGFK9UMQGdrK-_vUxGt2wlYQQASk47CfrAMTLDxsygRox_C4lxnyVOVsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز نچیروان بارزانی
رئیس اقلیم کردستان عراق رسما درخواست داده بود که بین ج‌ا و آمریکا میانجی‌گری کنه.
خوشبختانه جمهوری اسلامی
همون دیشب با پهپاد به دفتر نخست وزیر
اقلیم حمله کرد، تا یادآوری بشه چه موجوداتی
در ایران حاکم هستند!
کار خوبی کردید، قطر و پاکستان رو هم بزنید!
قطر رو ولی حتی بیشتر!
که اون شبکه الجزیره‌اش
کپی صدا و سیمای خودتونه!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپایگاه خبری انتخاب</strong></div>
<div class="tg-text">🎥
تماشا کنید: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
🔹
این هم نتیجه باز‌شدن مجلس پایداری!
🔹
عقلای مجلس از تصویب جزئیات خطرناک طرح جلوگیری می‌کنند؟
🆔
@Entekhab_ir</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
