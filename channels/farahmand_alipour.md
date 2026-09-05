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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 19:57:32</div>
<hr>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEPvNPKmo3Y3Dh-7BN3AfgbMYIpaxh6BhM89BiSaGPhhVVYRt-VswWkRfURY6IhG_eWCcfc7Zj2Kg8TW1k27pT3GJ4gF4oZGC7hrxaQGx5-xK1ZZQz7SOl_Cjcb7QI0Und_ThoDCp_ebmGuuWyejZnlFjxjLEDrFwiK7oXYEwh2X6jHQWdNqwN0Pner-oBAXEgwFlCvti9tWRGbckm5KAMNmlhMiLbXjPQLgk7N3Vm2VX6AsyLvsPGApgNg6VoqGd1gNRL1iafTgiS4x_ogGWXXNUq3DepMx1DfvUdNHQFbvCjivhexaZ93_GkLST0r-xMZtPHfccYOT22sZE3ynPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbjp-PRdcEWORyoBfNoYsRDrz0vP-rOqtOJmksVDE4lDrV29CQGpO5Qg9EtsZrVfHafO9Zcdw3MTbGiaGjAWjBiAU-m2y11BliuHFPNOxrABUSp1EFP3BdNEzTZuO5bmrsSgwcNvHyOOiaHKieX_w3WJfEpE26zzjh08wjF8SaeNRDN-0vuDkNQ-FkphK_MxSXZ1qFEB7uL2Sa5odvQQxtKGmptzYGb1G7BFxYiDliDK7dgHEADwPNtMOootKMvM2qgtPxEs1OyHuEFiODy900Tya957WDph_MgJaAAPDKTvzORzPHTq16KV-AdsiIcRqnOgGc_l8NXRt8Fa4OijxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-3NE_E1m-shGhebw4sykigZd2YZSbcDkKsyQ1Dz5UvBQmi3CqkT8E_0l2etZ7mTbQM_Kt_7tZBEAL7_G7y4SI8KoJOtezay4VmWvjv5Z1yhJv_aKO-6eaEl3wcdyKA15s7YW6_FO-_abWD2nT24w_XXw3Gq_N-OZI288tcFhFaiko0EBtCYDkEVi_e8t2BoaYhxKbffvyN50O_ElpkEg0nrcuhnEmWlCpIOkFjKdBYmHz0Jm557XvFzhET4Pf5wHHX_g38ZGaN5L7l9y31Rt1iaYnTAYkSaqShScaicSsoDsiPtgDP7wFPLbhDwmw9vHl6A-RYCLzlrHJOdM8GqPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szdW39AOqUPaWZYeUizdKIjcPhc04Ms5b_zNT-90XyPh2tCvnaSDC-kcSCyKcF1lgfUO9WW9iYpXOFJat7grr_oMgTVqXcR7472mJNXW61zYuu_MPiL8mRWsKSJNtELYzXrliEQTwB9Mmd5RoDiHBU-nV2TGkciek-UjspGuHZBxsdJU4pn0g1eMVB_HitDMP0o68-bt_4FPCMHGSSe0BJ3CpFe1s4KGnFO6tlGSaqcXagb2jml3BpNqUSfYAUduJfrU4-HSn8daURiBrN2eMnehOiOOhXW1hUSVRUANB6JIKpMFokbzhyE09gMQZoiUCCLWGTjVPt5zvcfjB_6jKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPezdsU_hFFgawlO0KeVI-GLcODr65bqzuDQomClvsgV_BIgKnS4P_ctmdYoN7SUHdzzzfSWd7cZkuUJV5KhWmaioYxpTPMHJXgBLne8VX1ZG2TKxlI6ez4L7U9kvtZLSgvPqreXtZgTI8CwsDfriiWfp96yRLGzjUOF2T2dnjaNklkz5AgJB199uDleCt04P06WHhXoKsg8zDMiX8mLuNlJx9ry4Ogj1scAQlmhO6Q8nMInaDELL1jRTtLZsURCvSpJOHMG4THVuX9SSBOkr7tslaOVy3Lh-i-rF4AiBiIGfrKfbVHtXz6u__5lYWkpQ6TnmWGoXvLwEgkLCmO2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0kol17XAY-8sas3MGB24Gkv1ZiWONbnBTg0NFsyPVbn_qK09P9wGB2aJbwiJLVvibO7W3rspX91iO2cFOJyL_a4HHGrPF4fgpFl5epUxXM2xZVD3VTDXpm5i89iCTcHfMSU8yVJSDSV4zxLO8fFCQD4lHR-bQKl71M9XRV01y2Db4A-Z7FW-BW4X_JuRp0c09uNiHqZp3vcE-7PZMZQhJCzV4boCTo1xQmRNNpknF93GXswM1duerzd-NMUXLwGCsmPNuc4xwPYqdh_st5_BCnzv6XWbd4n2iUM5s7wdqrZ6vwcgH5Tl01jlxOAsBsl4ALO0IXr57F-Oej6m3iSUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2l_3YZelAQzAwMrqzugI7_5qsXGI2Sk3n-IHNEl3j1b4cz-qW71w6e96jNf_eaOYDRqjlBEV0UTWNTI2EbOTHtDcrEeqVvH37TIkwPtA0kMDviVMdLJ5wALaATgV5esAOil-6GNy2vfBH9ReSiLNNdXE5qsaHfMAMrYy6BlPD65sSmAsnQHdR8NRRGdYSpM5VEtUSOnJGS2FcFi-caMTa_NzKJcI8_H97QU9CKx7EluFoTtWNaWhQtM90XcvVoxpU2mMvzfw9pWC_kJGvYZxeQtfl00IpdFyrUjITA-_lO9plxTPGtRh4laNR3OM1d4EuOeVw2FDlFYk0Mt-2e1-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-etrp1vday8DDLVnGhIeLsapjx_OedWUR4NkaBvbWhJSDgAcCmTw_8wPk2iJ62OfpG8PrXMvINyL7u4OE3WKaBdGt3GNxiPanR5PbxaBlOwO6KYI39rj4lrGABCIT0zb1pBYMxw6n-eirc8lUHUfV4t5IfyBsXQIEiRZDv8QdKJ76_diSYTTSn2SmBHhmeXGrbXv6OefVM8jcmjmiIhis7zPiuHAxSvzVYf5vVXdcwyIQVPs7rZcHA8Hf9nXySRR0Cbj3RrpWCV9_61JNyVkFy4Sx62RjMVc0iluJ5QhbNS7ApMV1OYW3fHG2kvhCYslafV3NDAfkKCrcSGoo6FjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=DpbeEszpk0SVAXtyWEx4jF-ayJ8qnoeGLfecMedp9Yc8vZrw9td25huA6LxfdQU5CsU6K1Ai6saeH_F9UIwQGVRuspzze39rA8jdrvxOMvluZzuEk_8a9f9_CnrF-DKUcg0XZilt0BRJ_lQJSiQBLUYJA4L46FHdqUD7R2kiv_FV-s94MC0DMu7eNBI5hea5BJEEaEzWX3awmUvKiCgIMawsIaJ68JUm53Tw_z_VnevleDestshaKTIyjsuJmeX74ixLXRfdQRpmeLscwOj463SOCqAjGqpi_XVo8uSnYTCdhcZ79gXP96XwrFeV_jrdLqP6MDUAuLICYgnBUd3eKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=DpbeEszpk0SVAXtyWEx4jF-ayJ8qnoeGLfecMedp9Yc8vZrw9td25huA6LxfdQU5CsU6K1Ai6saeH_F9UIwQGVRuspzze39rA8jdrvxOMvluZzuEk_8a9f9_CnrF-DKUcg0XZilt0BRJ_lQJSiQBLUYJA4L46FHdqUD7R2kiv_FV-s94MC0DMu7eNBI5hea5BJEEaEzWX3awmUvKiCgIMawsIaJ68JUm53Tw_z_VnevleDestshaKTIyjsuJmeX74ixLXRfdQRpmeLscwOj463SOCqAjGqpi_XVo8uSnYTCdhcZ79gXP96XwrFeV_jrdLqP6MDUAuLICYgnBUd3eKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJ-dM6wrQwSc_bGGgo5q1QhBznGjuOHXuWa_eoxqoEtQmz5murDk1q2L_iaHSfNVhrI0gLUaqGjh6_4bYkEbV0HLSokjqVZVHN7qN1kkZl5XSZfa5eColZtofz0hj7_a8-n6yezTTpJzhLBqw_mzXZHObAzhLGwUdwNJ6UcJLNjyT2ucrFq2WU8RXeHFB_PGxYU8_ODPTswKwysBI_CeDLgmSPqRUcDTHUi8sGidpOsXHWHZ-i7uHKbErDN5-o9deh5LbieUtCu5F2apHtIeTvDJ6V77DM1nVvrDIkCaK3E5RTSu0B1Zv9dwOIczllnZXWmeWCwkhLoUnHSs1YO28Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5mUXrEAXkp1ggQ67DRGDzmjcCzZLv86r32WNBzkRhq4cCFGqUKtgzNIV3WMIRcYeWJf3zYtxiSB3eHlgwf2H1-eUJc0HK_1QcRdyak_3HKyO71VowN7cibi_Afz7l_pgu6akNwrsG7uG6aHBMhhORUpF2LINM7bjRFmzdHw04KGul45HctsjCkvBm7ghEkmUF67zPaR9GdyliDyO7hJ0KbD0Rw1lenQuBBEUP5d6r7Lic8VtrO7B3ZtSdf-Hnbr7O0v7oS3VIMMMxeiS49AYigZyXIBwI80eLckvwqytiK7amD0HtZkLQCDUbLzBVXydp_ABmp4mWYC_CUSwbEnSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvHhkqN-wAuZ3d65ybslNJUAlCXu5tH4919jgyqms9MgxS-2RUURTAtAUmoffd5vN-PLNdy9a57rfkesYXX8QnUjpF6Jh4mGNUOjDTAzIjutxEPaTOxWBUeIvuFr0d6g_V9wFGXVfTfbq_Gu5w_1py7ymUpqS2scBeVNeMKb1dI1m-Kw6cmsxsQWO90AaqTu-bCg0iv4xkrEiThlV8GLioJWVpag7vub5PwBwb-RqbFz6tAAYzj_95lNF_qErRN2oXa3tJsZDA-qsTFVP1_cllM0VVIFKo9ybDc4r1j5QOQA1OHMtf7AsImfuu2ewVq9_JyjE0vtiofqCNSlMBqPfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvBFxRqd9ApoxLUkW9Je_bUxpa4t6MnpJjRdWzrRAMvPKHP33YpQxk2iT74zkkDjY05O4mAJGDF9vpsSMBIgylL3X8iEh2aODV-79DkdE53pRipXyAAn-wpurWvJPWSuH1wbfw9YHfphs-m6tmc4ywrWfK6XQZA5SOESpnswF6rK8BtVT8VUCsnK4XpK1raqKUy70sO4Z_uwPyhpJXCTFgPCmbPURubcpqTV53d6ZqgrMKbPfm0rmJZ9sFCNoQ7sXTzMGSnx6K0ArFiUIKf1P1Cma-m1SB6AqNIoOu3T9ms92C8F7mKsmZkMXWOeEEqaaNB2B1MONWldC_l2LAGIgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEk5Cr41NBaXypRrUv2C35EeNWcpMCE3aPrFoLMVJJ8tJfjEcAVr3aeCgs0SIBvgP8NCGgdSMrsGy9GO8h8K61NssK_sMl4MFERp6LNNYBuflUA5KGhkR-g09SZoZecIEdY0-HxqMhEG4f7BMUmFWcE51wFGciOs5YXAfbis2IS3aKBxY0_EyaW5nBnQ6f2z0zPFt5v6VOO01Yxb8RbfMC-GmN-5Tk8LH-WhoETVAsx-nwjyHY7alrbpEqOrZ7b99NQxVJWTHnzEVUlGzxn5aNfoQGONCfjlCkNDNfNWfWvoSO7-0pNqYQzhNOb3ROqT0jQEqBARmWDzDlmwEPdB3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtNqtgBptjr9qIt6FlcfCgM0kvEqyjJY9xETvCDXrFdiZJrXW48YFxCs8OWu3qVmptk3VbQ11OsHus6UVcJbgE8gILcyhskZFvgOnxlhhCPBFwg2GLrCBrCdAj69JHcwx9Qgx9Ae3M_fIbnna1c_sTCxrkMknNvQKDT4LQTrnlWtcFGrcsxsOBcrzvYT2sHgJB1CYthdrq_kLK8Q6yWPqMt41zmOnOqGcqoxFFI4lvihBPjMfBkYbeYcWONv1hefS-BhEgL336LsIBg5KHrpfpVyNp-Ul1jVV8Gg7hCm-OuP3Numnfy9g6LPnteyyenUi8ZuxDpePs1Oo5ZW2Kt9bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bozUOxq4R13_rApWO7qs3cNBFrPjQ3YlLTQj72-IlOVKSu8ZdqaiGNU_mue9v53GZFdzjGb5nkclDGhOHS623TY1SsRNTkqgNnhpZFxvn77xqHC_gnaP8VnAvR2rexDSjmhJ0FBWNt90nMl9keaaiVCE1wc5Z200cP4232iau3kHGl7kdbARDXnNyeAjBy2_Bw27Q8Id2UCAiiOL3t5uSRIimueTKqBel1CSFXP_dzmkLTSRvkunxs4kAXS97QqSI06JqMVW4YK9vXab3x_FU9hasEOIU9nvuT0FZZf0p6UYYppjfajhiWWxMp0XlZplCXq6bRgeDF9xrd5NI7pT6g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=e5B4iYcwmi6zaffHrox9pLhAO6TL25u4pCHGS8bpNzR9RMffhHh_vYP1VkhGuM8gbw9aT3_qpaQ9PTZmc-pwTRknNlMk6tf9lNAh0u5fiMLNUv5F4C0YKJJBUtOk9mMDZLPwOm0ilBF1RJj5B_Cu4523z2kLrYTo8Fad5c1893OUHR0qZCe9vuXlM0FIfMVgLUvy3ChuIeU_wdkJ0yo6O8zCMrl85XFo8nIQTBPv93hQEEH-N_uQtPoM-i_7G_Cbu0kEusYyFJgk86ntFR2nM_HHlrVrgC3cvzt3RxrAvYKuHN8R0-t_l3coAAJGJeIMuLWsWUuD0vtR18-zCHUSbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=e5B4iYcwmi6zaffHrox9pLhAO6TL25u4pCHGS8bpNzR9RMffhHh_vYP1VkhGuM8gbw9aT3_qpaQ9PTZmc-pwTRknNlMk6tf9lNAh0u5fiMLNUv5F4C0YKJJBUtOk9mMDZLPwOm0ilBF1RJj5B_Cu4523z2kLrYTo8Fad5c1893OUHR0qZCe9vuXlM0FIfMVgLUvy3ChuIeU_wdkJ0yo6O8zCMrl85XFo8nIQTBPv93hQEEH-N_uQtPoM-i_7G_Cbu0kEusYyFJgk86ntFR2nM_HHlrVrgC3cvzt3RxrAvYKuHN8R0-t_l3coAAJGJeIMuLWsWUuD0vtR18-zCHUSbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJq5KzO64MO6rdYsbuQWPzfOIGVi6byCUZqqerrmo7vCm88nY7MPxRctYpUrP-iQ3hll59j1iU7bcNk0CPok_IYg0OAfi9Xs9WfF68FP2edqlFRtHlwUSsFOKkINykOB4R6z9cNc9RcNVd2kzAwottUaH-0FcEts4mLC71UPs_NdpWcyvTf0JdZgzpAIy719y-g4gk68Yn5lXf3Uz9t_F6M2FIqWO5ndiJNltsCA_pcoGuBR8aNf6OqYOtjgw85nut2f3zyBV-q6mO6ybmR8hZWhGSbc-SzjS-ZpH4BTIhNq3g2Wv-ZF9ZCx757Bt1Ik_wt7Tl99GXH_aP3c63x8rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=XcVmKQDqwCcM8x3RqPNehbUrpunWkvHtboG5KkebEVSMaxg8KuBNLukP23dtYhtpYMOYik44Pa03ppX2_BRfhauTF8ehiHfVa2UCJ7fLdjTwa8lE_Kw_tAPVH17aRB3LHskBE8_2yTCuwI70B26WNr1fzxiRQ4fD5D88bPOiinbeElDZHjCg5jCX0XC5uNeQXMPy5e-xapLav2lcmCwmlZqS5GXUalWPj7n-TxIDc0vQ5DT0GXc8rnZO03S1KLFeRvHgi2Zr1qwkKxWFCaLfkLNQ8UgG4nySd_izZIJG6es-JzOxN11nMPDNkZeQ6BLvhIoLpZoNcLQn5fEXlYo32w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=XcVmKQDqwCcM8x3RqPNehbUrpunWkvHtboG5KkebEVSMaxg8KuBNLukP23dtYhtpYMOYik44Pa03ppX2_BRfhauTF8ehiHfVa2UCJ7fLdjTwa8lE_Kw_tAPVH17aRB3LHskBE8_2yTCuwI70B26WNr1fzxiRQ4fD5D88bPOiinbeElDZHjCg5jCX0XC5uNeQXMPy5e-xapLav2lcmCwmlZqS5GXUalWPj7n-TxIDc0vQ5DT0GXc8rnZO03S1KLFeRvHgi2Zr1qwkKxWFCaLfkLNQ8UgG4nySd_izZIJG6es-JzOxN11nMPDNkZeQ6BLvhIoLpZoNcLQn5fEXlYo32w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=qUnruZ-uYJ9Oz447zVNvEtqBnIKV4g4Aw6zC3ySWThVnOWGdS1vbd1xh4yKKLWbXynX3B8huXHoumi5LBLPhReCeosBTYtpWvY8jdSj1wA1BrCaDPanFfotwUBb-UI4t_7WisJd-4G0Sk8nxcnqmAWtTRzj0upwQgQLEMGIKT46qeGBB74CF1XNCSU_RmGcAwY0j8sWNPJ91NPOAof698kW-uz4nWYOmhQtrUg27wlAhPgkbyPtaa_Zd5dr4gC8VBG-tvqhLW-Ri1ChXDEzpDH0qsXMdQdixB-s2t9PutHU2MhXdaHNYxOJ_r42tjyyAw-nrNIhamO908elhMjHRQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=qUnruZ-uYJ9Oz447zVNvEtqBnIKV4g4Aw6zC3ySWThVnOWGdS1vbd1xh4yKKLWbXynX3B8huXHoumi5LBLPhReCeosBTYtpWvY8jdSj1wA1BrCaDPanFfotwUBb-UI4t_7WisJd-4G0Sk8nxcnqmAWtTRzj0upwQgQLEMGIKT46qeGBB74CF1XNCSU_RmGcAwY0j8sWNPJ91NPOAof698kW-uz4nWYOmhQtrUg27wlAhPgkbyPtaa_Zd5dr4gC8VBG-tvqhLW-Ri1ChXDEzpDH0qsXMdQdixB-s2t9PutHU2MhXdaHNYxOJ_r42tjyyAw-nrNIhamO908elhMjHRQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIGXkB0_2K-L3sN6N6HugkjH3rFXFkc8z_UTEoPCsM1V3HvSiILyMDV5EqH418AY4dVnoSEkU2lEJbJ7i1HalqvB4UW4LsIy1CPy-aQgLFZJpRWFWZyD4PuecLOPywy6Efy-3j3UwtQ7zVhOqm4HBy3_gdKZ21Wx6QTVP_pj2czcdyPOx63r41qukCsm3tRowDMg-tg1MVc60Jaf_7UOQOS9-H0IJqojl2delG-P11A8csV8IgDnSxzF205aH4xSaN57HSXJYFkqQlm6wAYamQ1Q8y1rxct5fC_BjRcOw1Yw88uvJneuC8cxPgvee2yXfNmyflLt-EmiMXY4QmuH1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ModrMhuT_X4Mj8OAo5W78WpLF5EI7q1pNmhzvXNIJkDOsj0n0ZQg40K34D8K3gx0nLmet8Nch25aB5-gkL1eCDE1kZH23I75UYEKhnj6zT9UdfCjx9UM7XFn3AN7HQbKkByTxUDg-Ba4iJWr1qHlpr4CyOVuc7KM_Z5b2cow1RsWtmlHnQoG6ESMPj4EaY40LR18POnxyYwX98moom7Zz-w0-6mwf8p3WxikXTbQlPOQTF0hduqJgTwYfSr3RO7PbYT9YtReJ57Elj4hDOZ7k5WVsOyPKEF_X5szXwCLE0qlE_YR_SE8LkYNdhlvmFX6yEdBQFKPF8-Zc0vCpocHEw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=hlCjtN4XfdvSca2zqUODNouWswcn5KQ3QzarG7vUmJEgmUe9I1qto8gLAxMGCEWMYVa-_EBjowZeDLMo-WheNfWmmGSi7EfnIm2ntAW2GT55t_6aBJT0oo_UA4euOvAXUGqAOg9bPDoesvcevYotqZGqfvG3lBV6tETlq0gEyX3Sa5q-GevXwar38FaDaNJ78jdCKxNag00bvWSjqq7yrrqoOPxKKRzezY_SSsIidjqPlL3SQbszybw8LJk7eaUcsfGEQ8lTAjBPjgmGOgHLXmX5wCCHpaIb7ca6zmg3u3vbbTgvBboUKRi4SUu4mD_rZtLaZjGhCuoB_tu5z0MvFbfuTUowy-56fG6SVCEb_MZVOlJFD_1hCwQIP2hRg8SqJX2uEswkffYyNTYPA2zs-VzR9B-6Ak2GD43zqopgqNxy9hHSq9W9rF3xPWS153EmNcrLP6owBesoWezTfccmdmUoocRJNNUish3LpUeBP1xopYF9DPhxrKl-RGf9dnoomZt80cK2BeJQYmkS0hg8xrPkxnwXWVfyXg1Ewq7xjNF1A-1d5ty0Uv2FMs3ACPNpzHviEr7T_MqQmqE8CZ6gj3SGI8XhGBm69HDCcoyv9Oicm2YIVmYs6PImnLayjZrkVIaqQFbCAiBvjERAmOWACVb3Q3lgm4KwSoTE9hCHO1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=hlCjtN4XfdvSca2zqUODNouWswcn5KQ3QzarG7vUmJEgmUe9I1qto8gLAxMGCEWMYVa-_EBjowZeDLMo-WheNfWmmGSi7EfnIm2ntAW2GT55t_6aBJT0oo_UA4euOvAXUGqAOg9bPDoesvcevYotqZGqfvG3lBV6tETlq0gEyX3Sa5q-GevXwar38FaDaNJ78jdCKxNag00bvWSjqq7yrrqoOPxKKRzezY_SSsIidjqPlL3SQbszybw8LJk7eaUcsfGEQ8lTAjBPjgmGOgHLXmX5wCCHpaIb7ca6zmg3u3vbbTgvBboUKRi4SUu4mD_rZtLaZjGhCuoB_tu5z0MvFbfuTUowy-56fG6SVCEb_MZVOlJFD_1hCwQIP2hRg8SqJX2uEswkffYyNTYPA2zs-VzR9B-6Ak2GD43zqopgqNxy9hHSq9W9rF3xPWS153EmNcrLP6owBesoWezTfccmdmUoocRJNNUish3LpUeBP1xopYF9DPhxrKl-RGf9dnoomZt80cK2BeJQYmkS0hg8xrPkxnwXWVfyXg1Ewq7xjNF1A-1d5ty0Uv2FMs3ACPNpzHviEr7T_MqQmqE8CZ6gj3SGI8XhGBm69HDCcoyv9Oicm2YIVmYs6PImnLayjZrkVIaqQFbCAiBvjERAmOWACVb3Q3lgm4KwSoTE9hCHO1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZwLW0mQ6Mw-xICKeoLN3XcQBy5-l2Ny21yRi_16ikwJ82QfxMx_uqte-fNryU54T5oFdnn8ODdNIHasauvhjBc_1hYpCfZSb5hl00wxmpoe_Uf4CA68EnFkEX-D-Cz5_x1blix4SGp7WqvmP-4FemsAqJR-oIfJpviTMx5m0MGQMMiJO3b2VSogAsaLRr7miK-8rckheWhzuxESxBn77wzhxpez2LC4j7VXA5Rjmep9EQhdZcjZlMZpscYExWamv9JacGPwuiRZKmYENhnp0sFhrN8nYi_74T0oBjrvZVuv6XAXNn2mc6Ulyy_uFaUD76-8EzfdWjDRTGQLRKP5mQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=M-BLEL4BegS1lChdUSqSsyun807d9XORS0PSXuAzyNpRCCcANaHz4zRw3h4TMPbFXXuCM0aU4hovNDZyPGrxOhAvqhRHKB_GvAWHeEBzuNQNe2GjBVk33igyLGqmGapj5BHk65ydv2hDb5J51XuH-zBSNCNYG9I5jJcsr-9dxQHT6441CDMf7UBdP_oNjHpMU2VlesReXYI4fhse6iCXzjpnTpHi7AiZtTaTpWhjjVM5OY-CLKXMlOf-VziErBo3lWuvp-bezukcvsjtF33FNaY9b0txpjJspqch9Uys2RW8vom09f12fbYimD4c4md2JCn-cazD4wvw62QKM2e9dgaEszNWXHFtK2I5PQRXO_a-Barb-ghxsJC4d4cz99WA0GYQN0cmCk-yLr8QFm6bv0ZO63HORv6oIHLqpClgZJ9YdxRfxHP7jFClZ6E4apZhNzIhY4cGbMzF9ebiEzABmdwzjnFT2393L0c4cw_QdnuV-JYtIDMylWQmdY-gsnHurpdV-jNCUPrDRCAw8v-Md6YbZh17_sggAlGFGCO13NWxbTOttvVZxQgi07Sl1EXUtoJvj-CfllJXPz51umnY845Hgq2joijOX417WBUh7W5fTxxOXRqHJtpspHmJfjnUmsR6HXbHKhTTxlAOTxj8hEl0_ZCVtBlXNRw7otNqwAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=M-BLEL4BegS1lChdUSqSsyun807d9XORS0PSXuAzyNpRCCcANaHz4zRw3h4TMPbFXXuCM0aU4hovNDZyPGrxOhAvqhRHKB_GvAWHeEBzuNQNe2GjBVk33igyLGqmGapj5BHk65ydv2hDb5J51XuH-zBSNCNYG9I5jJcsr-9dxQHT6441CDMf7UBdP_oNjHpMU2VlesReXYI4fhse6iCXzjpnTpHi7AiZtTaTpWhjjVM5OY-CLKXMlOf-VziErBo3lWuvp-bezukcvsjtF33FNaY9b0txpjJspqch9Uys2RW8vom09f12fbYimD4c4md2JCn-cazD4wvw62QKM2e9dgaEszNWXHFtK2I5PQRXO_a-Barb-ghxsJC4d4cz99WA0GYQN0cmCk-yLr8QFm6bv0ZO63HORv6oIHLqpClgZJ9YdxRfxHP7jFClZ6E4apZhNzIhY4cGbMzF9ebiEzABmdwzjnFT2393L0c4cw_QdnuV-JYtIDMylWQmdY-gsnHurpdV-jNCUPrDRCAw8v-Md6YbZh17_sggAlGFGCO13NWxbTOttvVZxQgi07Sl1EXUtoJvj-CfllJXPz51umnY845Hgq2joijOX417WBUh7W5fTxxOXRqHJtpspHmJfjnUmsR6HXbHKhTTxlAOTxj8hEl0_ZCVtBlXNRw7otNqwAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-B60PYQJSAMvbLT9b_bVCCLsO3cmrCzlBWBFHT3ocwhX60hW6AOWHUyBAXGTbTeNnV5QrbRiI1Id2mC3VEO0YxLlcRu9uP8jAoDwWjP6pjWCf10eLSYNS8pQjEo_0PAIkgOqAGrrFgNuGZVx_P1LfRLUpFtHdS1XyYY3oLZY9r1SaJSQSrMU2JRZwLJEemSQOrrbQaACL5SCsRwtJDGkIfgmR3yWCrra_a6eZlP1y6C3rKyjG9szAGvIg1wLa4_7fphCXhwDWd-nH6jjoUmRs9veVjmzj_gWFVbWO8jfto6xo60Rnvgx24a3D5bVQslhLTUCWh6tmISapQzCaEqBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxKa0dEVAjCHW1fHuxUKIsRdMnq4hEj41JNVWKui5Ax2J5rUkshMFdCxlMPtdV1WaOsU5vhXPih9BmcPm-iJ57BOaaPfI3nn1nf90yTI1gpuXvoSKeEWKThT0PAfi8_WXXmk_n7KRbxO9onizZcTL8Jfqw3Zv2OrVYbxR9UP_1aYGkjpgMJI8sXqvqOYMS6YzZd1S-_tCQ-Pp50hPfeAYsYgf6pdF6We6XltCPN5MMt_NQILHgd4yAWINUCpCn2Nq3f8HBzNGIiBCbHbF-EjE7dyNtV6awF7hodMtUmcWFPVV0hlGK6im-vgoz2RXH44xJtb_9tavTLCE9ibOI2yRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5pTVmCkX3HJbOOUKuBavZyNUsmvx1rDoWRb6Qa4DGxhHj0Ql5llGptW8g75d_dhFLWrG6CrOTlNSuhfYhYtG26Qx8AheoqqetQrH_TW9p9lZFFAlqF4sgfXRsq2ERbTcVXzVR-NsCqmXp_XW9WRlMIkAeawgoIJxCUv7RYVUn1254xQ9gBIgHr7N-qkXNeCGH7Ee_KbXEEI6gLA1P6Bf3rVB5x-JSsaA7akziyaDff1Fgu-SKRoqZwH_xBWXBjZdUCXDAUpDstvqufEZsar2O8ndTyJHD9Lfhb0sO3V3VQeDwog7Hdf7jcFtk3xH1fDmT7CEV045FgPrGAnq8qABw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdyw4vXny64TB5LwxgWKo2V-Fx7aQLkWmlbCJrPywZCpOk0yhO7GhBohuFORIexcXcIS-7Nc4kKW6XTEgE9CIExTJvMkEksOlu9elfMMDrV4ExUAv8W-j2vgALl1QE-1nMcqzoDVJjHMhDnQcJk_PZ-UP7Dy26Y3ID0B2kYZG2zddJl4pxMOBjgYH-QU7b_V3agV9tQbrvhNZ5HjKO9FR_8IPp6LpQSRAXZlykXtwQnUsaiRfUpnC1__iNLmuOFSroS1HmLVkxvEV4q-hOhpoMgrHEOrNMkS-ZtxBmPHtm7MqY5djUYbC9WEkMkq11haah0tG3ldITb7j3gqAUzG1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piBpVq_joVPx4wC5zUE_ESbnEGpu_E-IKK0pHA4fykpboB0pV_8UT9nmkRhDIDEK-IWSIL1h6ZG8tFszrFnj0Eb5zgOyDJ62p1CwKCXE2R1KXyVwdCPXYuA20b1YJTZCIyyyyqgHUPIsYQcfjOQhhioc5Zd9k-_w42O1tAlTG6AxBWnvnxa9nzRegUs4zjcd0MhnLeQQ-2w_DPRyP2Eqc0T_qPOVLpZ1seh-QSUHzaOl7uwAsd7nl_ARYEDJLVQh8lWrVl_ol1JZriruXwpUErWvU4b80VQcAWHnvi0o4Edj3OZ0RG-t2oXyhZbBzdTQIvle5L2DQtvlsgzc6xisQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tz3SRLnAzAsSp8Burq7n9iVxzco3TtJ7ruQDlQ6dz2j20fWxSwduZStNdlxgEmxssJFAbikG0uScKpViphSalztr07IhmT3TpyBDCKEZtqt8gALqtvdUqBIQJnpZuEM2BGpWhntdXpB2RbmJoPA7pjTEzInTXTatXgagfuO-FdnVSHr7UkkcM6TKwOwuDSaMYAc1PmHx2bmPiULRuXMpOQvkIh0ffGY7NTHALZboXn2ZggOhFZ-BUqQHO9zFloJy0fJrGiDvWz476c5DsmQXg3R8blVqLq-HMvGqxScqE4y8UVpfuH8aJFpFFTnKIG2-PzsNX1OV942v2LR_VhTxag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMb1P1blbiuLuTUGs5aaWlq4LISuYcGwsuC266d-hYQKG3vP2dViBK1Ir1zh4UQ7dek-MVP4bmNg7OlUINMPOF4gJuaNNIKTets1WdYpwtg-A79aIF4jSu3keZLt-2SO6SDOFex0gIVpTyeJnO0-86msoHtzxTbtTkoXYEPqospD7i2mu9BFuVyIoP8kLzHSQul_Z-PFXEMhR0Z5R79k3ucJl__40jeQpnPjgLFd7dhKxhzqjxeNvdirarIa7lxDdw-MSgUFHL4Qss60FKXyvMNK4YHMLGm_b2-HlpcsjFVLpg-br6fCbZWEfyZz-vQElMpaLyv3hAo3p-QRia_ihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bv4MuIW8cXpdAKvjO3gsw0a6ObAZHoWQ2-iRJBymRgpF_L4w28qjzSgKzET4-rz1PJTzvJqrhynTZrtSQh1_D0ciPo-8WLarOyP8eecYA7iKRS1JHAtWxXfTprxA5PvM6AmiSEhPfddVJVEtHXarS_jz9SuYRlWB3qx4K_rYYVU71PoqCOjwCmUnSteyIGjjG2yFfClgTwt1DfAM2PsAha9Byxf7dKLelWerLh1v1wincXiUvmN_1XfEhFNLIB_pQSc7LMFeN8kkx9qrDKqXZKs6O1uenMz6f0UI8-QyuCID4KQ7waggmwLJHw3cyIKO9I9LFI0m-2pXij0xiUPbxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPFfDI8VKkDoglTOZYCq26PDG7sUgoWN02lyeEyY7lANMsMkigZJfi-McRCJp-DZucIpmGPgqd56CIfmfOWN9pS_2wKZn0kCNe33k2z09GBs4FOtJz9shYg5s_AqCrzOEo3ibkvVTNfQz-T57ACpFSRjwQZ-dSe_n3pPPFpHGGPvDGj--f9MMTIjVPHfWMmOVx8mOZMufrgkYqRMB6f_mOIguPbKoBSn-0p4DKiMBUO77359odxCdkodRR1QRBqxXYg-jFV87fYTvFVQE2cZEwwr5cSEAuZMwj3mfqwAKT918sjc27bp3OXTw9_rbdYELNbrYf0kefHhJiB8BHNJqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pw4q4PNOiIyzF_n1X-7CSMCcGw9lXTF6pN2qGTLp4h1E-BR_9SShMXlZ3JpgQqewL8-jiPYRL1RXyQYtRYKmqomUi5Mnlyvj1t-3vSpRom2na0o0-jINsQIIXjmeU_qxyqOueqE-yLOP8E8BgtL22Br3h93xHkEn_O1J1liYP_buTXHUBiNFrYwhhKEkbRRzWpE2VRF1-UAITyYYdPx-pNkXnanStV9l3il99rrJMcmUQFjdePCLIK_7zY9aufWF4RVi6pJSKC7_14aPSuyYf2NohIPKkQX_Lbx9TLZ7E56Ummz5DdzwfF6uNSyxs-3VCvBsMvMxYMq0NPRFREywng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukzw7okerEZ8EMiiR0fBjPV05ZShorkyGP8Uppt5hvn9k4iINVbHyO_40dPiinwodNoaA4gQJgaqAeR8ocePMqhkc1HYF982AhS8fJS1ftsCDgbMJHNwJh1o4qh2JtUuKN_-7T_tx8JuSr2ONRS-fd-3F4boqDqFYKKtb5abRLeUvJLPNEkmxoAPACQr-bQfUZQ48SfehDHVtNozwj4p9t5UdYecoCwBHaOOcpQ7mmjDNH_YadkMgJkkBXFihKOBfPXE3x645DfkbewjzO9lPALL8rjEPSMl2mN3xIh92vPFzk51ESy-6lR091reDmfYOohD6tqYJcX5NEOOQfcr_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgQ8UlVPPaRF8bkzWhSYelFnZfyXzmUEcRvTQE-ImbW9tztzlOk4sEeGYCss6U-SzDYefZRD4leKzkyuqMuTHCOrMZ9WVodx1dXLr1QmA4YQ04iFjDJOB--Vcgh3N6aYWobfXBY47qbu0IVMtXSVbdR3tbhmgZP2i6yzvV0x-Gii8S8ak87gqn9EHzkcCXSCR0ewJ5kpEPiUQdrLA7XlbC_44Khj3ssc_2ZnOkaABK7a9aNpqXgRS1tm9Y0sXmmGqlZnLiRX9oZx029UTQ2pyClh4fYlZHsVT7xNEOJpBuVpqqBCphqGVhBouNyV-gsWQppjIF6K8KjgcRcM4AQ0UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p63uLrdKXgPUdZOLXm63V97SgLN0Wk8p78WKdlM8YrMF6TFLE3buoj-R3z1xGmh5qokAuGlajUdjQrkuM1VvvDwHVY52SNl2HVYSO02lUxB6VuzLiasPPktBT1QgDqfRHFA6QQyZma_2kpvSgNDZGUGOtYuuZTVp5NUNKm4fLoSlKpm2r5-fQdrp_5Ge_HRYsJXIOW2C5S3EphN6GX0J7DwBS_z6C71kcJTY3kPS8zrMNRKU8ZOiP1dB-EYCXNoufm2YdkC_oew9OJmlXlWAtv7dRLCm9w8yAu0MeGZBO-HSA_Tv57FYIDJSz4BgdkNIByb5YuzWCPrwzfe2l24ZKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SezVaM3cISdMjVaE2X6QwePnqECI5aQjVvgvM3oYg7PPrL03cv_ATkVCTKfhmjKHXf2S2R4Ae09MonAeOk7eT3x326MZwcuFcjASgBxBA9AUiZTT1PvyhK5ly_l-TfOzZlRRLtzNb14GzJ0-h8kGq8vOVE5lPXiYKII6_L9j9JvliGlrErghBkaNRIoxrzDwWeH7EXrC5ur8JNC4oxL8l9spgX5wi4xvy7sqtdsgdAWA0mARbHpcsAJXVKQccZmikilB-BXA1xcxpkzcgnIjGc_7rZDivhm4NKO19SQBLO5dLyoPfA6gkCx8U_q_0nfBbG2h-G038IS5gKcEjQ-JoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eix6o1WME7sI51JVtc20iTxiGOevd-RHiQZUMGw3DXw48wEoBJqKkZpuNSNJxlfXjOmC9gSG0a9anrPOfvsUKwVDHV7Mts_luqVUnrz7tUkz3h0kiEYV61GIZB9QmmIenoYKsCINFZBhnRDsG9wMLxfaRSnGPU7RGiEMutPJZHDAyOrP2GCMYi-U1NXxwD88ZoPRt3Y8dlZc5Ux7V1u89MTi5AEvRrfVo9VmIXXny_qjZw3ZR-EfhNLlv_5mBIOSYRnesYf6pV7pLbDjYL1JCTXmeuyTjxYHJF49jNYAYUHxSNSKpvy48eZOp5ajMtmR5By0diDbZWRDoprgsgAanA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMZs-JDa4StqoVWc4PGwj8JcW-k4X0FeReuCuEuJY6Ll4XS5JVXyBd2f_wBQMnGHIGRwTf1EYNqYmfkrwiLas8pXQ_9IXSu336TWga1tuDHU8oQLV7xmavKMjPue4FIAedOi6uAIUHDGVYOQa1GhvHZ7Fkua42HPLlRa_N1wAdap3EQhPfkxYsTmZx0evf9WSl-wHijJ07_Od8dlzsgCE6Kxtob42dEHrCgC6H1RBRa2IkNDnvT7qKLeSKzrVa8LNf6HE1FXuJz5kTxr5AlGBOWpFahFjpsNO5RhAGrmntFHs-3qGHZFQ_hVA3MQfBYRnyFqI6qVyfAPM3qq2WiX-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NGFeW3sw1sP1vhBbJ7wFQWgJMTWTV4lDVlpEWZVeScH8BVaVvquTgLUv_9eOoN26XMVZh9G-0B6UbUpKF9N4_I50ipnOpjTANj6X3Xj_l8aIZxVEgeql7VlPwgn86ltN3iMcz3NDkrPzMDt_UmZCC4Xxz6azpwgytkQbgOygh9lhmrtK9FZhzRhXQtR9-TjH6wVFlJ9JWL9PidYV2bbsy4afcpHiadpd9kQUZtBMFBi8Wr70nODEpTRmMAFw0lL4QBFvP7sNR7DdSbvkf8LEUJq6EH-JCkHJEl8m2OUC2YMNYgfJSmu2D3hISPqC7d45xAy2pEd9ce4ajEOsfcf9fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EXL8SSv4iHExVM42GW6CoKDBwd-InMUn3q7EaVgIQtzKTG_WoMwWI3SkSuU_qLh47BETPOvPsbiViFLYWnHR0j-pKLI2zc-6UiFFE6n5ai0ctuy0PDhP2VnxZM1TijMYNHBKdvECN_gkCS9GGfnQrLA0t3zf5qKbS258uKJ_vcX0AIFwwgIM06TpPkHJe0IGLPO0KtWfTG_Ncs8uHDV9DUhgQqa82XsayMBwMuN_E5ZIBNy0UDYFgNbYE4vdbZKwTTPIBh63AT0E2bEiWz0CHns-HurI3dKZGjnvjCAjVFmPbjkg7RaqofMUGQTw_FuDxynWrtsEmvHFxV3b5J3DAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fq9EQdeeNDSH01YroN2gt7R6peSN4EmHM_bRfxarNtmvoHy8DF8E6xvoLnQQrAun7PxQIqcW_Ufxd678738tLzFk-mBc7kEr-Q-UO_g3gDGt24HC2xvhkvpgVDdo6QtHk714fJ6VCSGyxROuq_pr9q9Qic1iPihHA2mCwLnrm5HCN1MhbeUqFALoBLzAug95X3uVadfvnNNEqujpTTJ6-3qZx1B7b6-nbpKprqL-UmQWUlYW4dzZS1SFcjn3wOoUyksYlexue7W6-oyYK6J0av-JmXFU1n6Ct_RpZcbFeQvICQTCez8OViGeJePV4JcJD35AENwmjzcFtHN_tml8wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOpVuXtGGd8jULMHY3R7_EF-ZgoexJ-B4xgiOZizsnnNXdhC9yVxFwxDIAV-4Hhz9lgEKFC4pY423XSV0BxVy_Ta1z9ddF21I93d1nDFTjLeOvid-lHf-C9Y4u_d61W_kRvzGiNa6kvCVRAaPWvirB3VRymVTEogjw8PHvpMB72xL_2LEiKHm7MlqD8BC8iBNN8QEuodZnIoPpAvaUwrwN4kNwh-HABrWX6-hylAzzPPsgw0HPgEvILfGqAAdHeeL5-XW8Wi5nsV9OyFSfeZtbHnatJ4KA5i5VydNu1m-LhgoZBYouYU-YLCY_MIjlkUYCX37aHYKzm-VQhuS16m7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKOIdLW5YXbKKg6uEdZaa41MO-foW3oYbi1mPTwzeb9Du6ZJdRDn-n24T8a43AfShNUFlgLmn1DdQxWsrGeAM475a9AoB8zdO6rRu93Ly7E76k36gSPvcbNf9aAv4HmeINQv1jKGi3zhrHULTikYYeRWJPzmeyDy1M9YFBCskbzOFm5sCAEHTIg8FWitgIfaf2zqY6w0HsH56WB80_OoKIWmLX2DZ5W6rYDtMJyo15wXg8QCsGagrePrKv2JMHB8RqW76piG1w_Z7WwolodcWDP2m7QOlQxJE8PWQy7mJkj5ROuw05Md0TrH5vrh8to5Yl7OcISqlaaoQtqkAcVlhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpoQtAKAyjc5V7bXDAsCb1hOrjio7EBGeaHJ6LNclmL1BDSnZ9tQfLQ2QZXZoy7Cf3nzDLbw2f5t9rnaC5vkgD5vOGixoPylNcSmsfdbUIBmMQPEqHaNLtmVBuwf4_vNICm2J5oR9tb-4NX5q5Wk5QF6R5-ycU6uhQs-R6LyRK6PmJD3uzn-T_z4euHafnHfR83g9pl84Kp3f8UBxei1LYSELeYieJoCCZ3oDrV4w_hDYILZSUfgbQC5cNsSKZaBqvArWqfT3Q6XEa3TqtrFdMbsdXJTZPrKPX-bqG04SaXBn1McRr6Sv2quvgPw-wN-feaPvO62y54eFSrZpZA07w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hz56zx6e24oVV7la7ygV-A0OBDZPqMsCSVYyLlUQE0xDYJcMiHwbAIR95-07TTMw75VzOXhGJxuOQOMMakPKAXhMDVA7UR0bx8JUPbpq4ArUDwT1SaLapDMLw1wUisr-TVbUnBlVXA6qMZ8cml8qFM0Slv4SFJcxElHOAu3d5G4sBN3JCOHCVxR6ZUIMpT8Y-VSvJKReX6PpUvAlvpitIqARchQok-xmUYx5rWjZZlZNoixBNdo6b6GXTRvjd0ptP_7VRm7xox5nMYlb_sFO_4RT75CdvUUSua0B0xRBErnDBs58wvVmQU0zrtsaVpzVJapwwc4tjpZYuy5PBitjBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1WAa4uqFCGP4Gmn1tQ-99O59LTSUdbnEck3IWoyMivZWFKAv20StZDthhK5SoJ_HbyXasFxenWtuyN3igF9_AypdJiJ6FuYw_yPmdmIAGfJ6_qyxM9Zpc2SGfx-xSFJG5QB-NRVqjkbUC1v57b53ISCXn36RPrHzvbewsF95vl-qdxyW1jioTWkkxAoufijYQ1F7yXujHxnQXFO2uR7gAJkfFDqJPywpSkFQgCxaD2-BJpiCkzQ6vwfWxARYYCkFUkxrdfDYIq4mAMMRqKEh8bAFZIxJgMXRTl1bsMI4V0kXJjtV5JoIUPohkhSCokRUJVOzlBiXAMW-HeBdEcPVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YACiBoiG6aI7JoEexiSrxAcWoErMjxwRjYpLcTjUMgn3p2bvHGyz68c6961kwJaA0OwgVRuEITwcuT6d5LavMiYWM6bGP-x0sjEOt0n6lxwNMY_ssNiR2b4uyrfkKRE_Kh5oeVKRlCbuKxLbbwIdtlF73KU5rlGbq5Evm8zuAMYGetxjps1Aa-NGlkpcnsp9pK-LmfstxoxvowIROmb4Om8VXXa4GP0e5JKeErGDWzv3TorWDqEKzw0GBzTEJBIi85LSFtSvd_RGUB4ih-CFyCeEmSvdNWbCmw6Ruia6yDRCjamCUfCEs0a_9iOZIxmLvDT4FrSsFc6wvUlD-uMrAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMZ8wRguOv5ffQTcEo8imJhSxRMdD7N7rHazZUpJq0g6_Yf8SZ8sQBnqBYzd7N2GV33pKK8nHWKzUTO6WWkZEyXCEtS4zZq_nkwcJ5BazVBLp7lE8-8vi_tkIZMPY9gJvFUg1Gf1ICY9hhQawlj5VqgjLO87neiFEyz33XDM7Sx9wFiwXQJMbHVLN9SBE6d_X_8GFIKXNWToml2a6F_opt0-8l5G2P9P6mOFSuuMCBDRHrXuB7h8d3hbnsgrX6MosF6xhD9TTjneLoISmv8_wbk8Hn7s6KHWvyb-W77U1npuyMnvHO-t08AY_UnZRiXS0LtBqrspFAQ5xV0ULGvL2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClRy5ET76dAdlfpeWMXt0gcyJz_rriSLqyplaBwYBM8DEr4I59beli7NlW6jRQiSHVacLD-qD8r5CZmWl3_zfWc3oXUiNf4wDfUlMzUDSifuqa2C9GUkHHa-dji_s1IYlR6Hgtxf_pEKyqPwDAPu2k_0W9fXRyx9Rxzm1c1plUPcHIX5GMbdrI_G7wIEzeVN0BJOBfZSPWUbU7LdDnHpg7_lLW0VKa_8FH_OD00HAHX28VOjL-XekRbG6Q8MGpYV9yEHdsr03aKJcODIYzDeQyBHAPjhbaFh0jLzacKluZo4SNdFNpx_zAP0nSREaYrUmygA5bMeheGupsTcnz8gcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-AP9pliy5c3X_T7tiqyWeWG29D3e1PECCYGHE7wsItIEAvYkD_-XKBV8h_sLpTn2yZMwQ37WWRF5rmAvNlKS8my7lm563GOaUn6v3fBTxHF-5Xgxd1yCEw9EuIm61u8Q0lGCs0nbsQ68UF8ZMXk4oXQBe0wGghxeTZPRoKIdwiMij8hi2U6a3TBB-Wv1X87OGPmx7GIvAP4srP81b8h885xUvqjgnfcLev-mHCt5tbX759e0q-nxkLw_VPJclD5y1rfuYJnm34-YASH2bx-QaR6YijhMpcGymaVq_WLR5Q3rwzFyau9ujMYQQ6Z4j1JILb54rRcjquIpCk1TYLEow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTynmgw_hJoOasXg2bvfkBXjR_94HUJCMbQAJkPa3SsAAUr1T3gy5iH-xAJ5hGXU0BvUvS_HmOWXkgk6j2BWL_6RPC8r5lrNckvRp3D3gzF0_IFHeuuuRVmraOyR0SWP-njiZUvIKqWvj6xIiMAmDXlRqyB59OGO5bMlWow0JTy6Bhx1Q4mA5KDlbI8fFoalqjtt6-H69-PRmdLi3JEjVmD2VWsPVojVLUtAZ-cOaF-guNkIWzD64kcJMkZbI19pIl2PT0vAhwjsc2wO09o_Ez-1tlTOVE98q8p4JMf3OH5Oy6JR8FQizcA4ZlrZeCQgOPgbK2e9mdkYFbk06lbZgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8vviuYacuthoJ897Q9eIBYG3CGe6mVEXICUAbqQXSPopRDxa3vcORDGxUP_RBiXUua29Io7PQmNJgTGxEwX2BtjvNuKsfrYLClfIDR6hTwTmRlO6ei9zQEHvVZY0O-ZqCUtirpcaxf6hxamCiwrdyaNrt6mn_7zbanLkjs-BMHv0G3ZlCdemgTKYX9nRcvu6jRofOKLOhcg9DgXcbUilG0ZgGsq_s6oFq9kAFQNTVEwCm0ZIhV-WE2UtseYbhxriRjvxsqns9cix4LmsXrxlrYbUvKCBFOiGKo3x4akuiZqgrymgTuOXvDpdsoGNEr5CotsrKwaSE5xE5N4mmR9zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/it5962LpHuF1eb1iIJ2jukk7emxozBWAt7JEDiIChAsNvWA5JY7Pj8KeyClU3Ckhi85GUgmTrAWtLT2MNxTGZwH-EvdB7tJng8zW3ShlFEUUBVPBgiMv7cmdD280tVjO1F93vJb4jSqSI43kHvik7nmk5rZRp9RTo6I9Yd7xyIIGBau33VvTmkhaGCLa4jLQWZc7ZsTdPDt6WfSkqGB4M3ndPjzDNjzWWTIj7EVKT07NrMUc2m-MkwcbOvLJxsnP1Uabe46-aubY8zb7xkqx6FTqaSKAcvtRH-rbUMMgCCmteQOzY_NmgHxX9nP5LsIKaPt5WrJGfmnrgU58GMHkfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0pyKv3X8jxcmF8pC0Yuj48zb0nOcwJvG6zHd6m8-zIkXOdEG_3MVT7TNkKwQ6trHcyjQFRTTzE5x-YAGU6OlQWNFCgORSFCk5E_KS7Ri2Z0Hcpa_riyZIC23Iz6lSdKUYf9dkCgItNQmywCWR0d2cc-H7bvsi4mCRti0v8b3KzdmXCL7yvpezyUEtn5wECLzIDOfG7CHJKu-waHCMSCtjloR5PRZqGgBr_MoatdJn5D43tNm9rT8z0EMbD3rQjHFa2wQK9FeehW6knN3gKwTh6C0yNRmMKaBjtb0GXxRpvvtDGrRoYfDl5n84sUx9bRh-bJb8O-25UPHoSweanoQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5gPPzp9VxeGGkEESGdI5I55-ZyrQ4SjxoKz7e2UWeODz5JapfQaszMx6aq5LHAiWK_AkMEW5Ox8vnTUPOA1QwRHkFr1N0W0oSl2iUfHOI4Yp94KJVgQFTfcoUcoXUnTt7OdIP67GzLu0ugoady4BgdRXEHyht4hJ0nhw27H3eyTHeyN2Ownmo4Phr01Wur9q_hmOX8imoMy9SKZ4VfDqacrCCV-jljP4eQf7pSU9TXfcNXosGSOzBPe0XZh3cZnKtrYOuOfCyC97GJIFcTSfEj5qs0FY-kk8a2Gea4d1_LLM3jDInGcTg85qVTtBQ8rKFFYiPW_84qoljkhnJ_8Cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B21OUvi9nbrhMOMQLTrqYpZLmSZoosIYh6FmTQfW0jPd4gwWq1lsil2zX9HNshC_QOCn7_0mSFVT4kMNI9jdZxybu-qgUpRiMDOeQZZzG52thoZtPmIJdpxH_pS-yvW4YmGY12Q9WmT_QKzEcBHfrzmj7Zt5BJFqT5_zN3-9sjUZOQaG7tiV1KAlN62dzgz-n0dP1qtrQegpclCHHSgo2fPQlwdk78pqYY0-J2NZ4ITEandqwCAQpbsUWlt_xQgAPk31Q4MJAEKNlUa72cFjkj6SB0a8lNGlnFBomo_0UlpFyhSYOSOb2P0f8q-gOzIHNSGmOZZajmpVPmCtT2gSdg.jpg" alt="photo" loading="lazy"/></div>
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
