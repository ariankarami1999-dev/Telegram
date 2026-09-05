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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 14:49:11</div>
<hr>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-3NE_E1m-shGhebw4sykigZd2YZSbcDkKsyQ1Dz5UvBQmi3CqkT8E_0l2etZ7mTbQM_Kt_7tZBEAL7_G7y4SI8KoJOtezay4VmWvjv5Z1yhJv_aKO-6eaEl3wcdyKA15s7YW6_FO-_abWD2nT24w_XXw3Gq_N-OZI288tcFhFaiko0EBtCYDkEVi_e8t2BoaYhxKbffvyN50O_ElpkEg0nrcuhnEmWlCpIOkFjKdBYmHz0Jm557XvFzhET4Pf5wHHX_g38ZGaN5L7l9y31Rt1iaYnTAYkSaqShScaicSsoDsiPtgDP7wFPLbhDwmw9vHl6A-RYCLzlrHJOdM8GqPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=eqwK7ZRqs-vHq7eflBWJ76dO4ECMlIV9CVrB7zryykIi2TibKwSGCnFNtCnVIg4x6k98ek2EhL8Lfh5uPGGd5O8rtZsSo7nY22h-SJONdSYMxSS3AYMeavXBLSsGE57Sav_NxwHR1Tka2dxV8zI0FyW9nckbcrsowxOglzVkeD7xxWuee8jrN86ME-PXNL6NldpRr4ZZ1ytA_SAcnxBWzPy7zM8FJ-GKpGSppLbd2x4DlFmGCK_P1NxPYhAr_oVZ9rs_WnuAURlMGaIfsqPyJZpVgUTbs75Va8kY8FqUkDkAcY_TCq6xVTM7AJdRY39OWaSe6nwkjThah4Af9eAvHAWzO5DisdOYosZLO1wdsAfIyIeH63GdjedAC9Fm6V17lATsf_0wJldGL3rszNmXxmPpXClFxuwypVrVu4c9Qu4NGiXkLqbeoTIc1H5BxpKrYIayyEh4RKw8RqivMqYniopzljaFBdpeSVpXk7Z3vKF3HHEC3wRLz2UE-9JdY5yCE74f_LorG6V-pUlyYSzSqHvohd5zB1sKRafrAaQT52bhjAbsi6LVK5NCHBLpZADBVPDvuLB7uCTJlWY8XVSNDlQUamWZ1Q_xn7m9yrIxpQP8uYXFGS6-LbGYCLTJJQ3cgZPtoHxL22MfWZo5qayqJkSSvFFXYEwTYiEvPyrxF4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=eqwK7ZRqs-vHq7eflBWJ76dO4ECMlIV9CVrB7zryykIi2TibKwSGCnFNtCnVIg4x6k98ek2EhL8Lfh5uPGGd5O8rtZsSo7nY22h-SJONdSYMxSS3AYMeavXBLSsGE57Sav_NxwHR1Tka2dxV8zI0FyW9nckbcrsowxOglzVkeD7xxWuee8jrN86ME-PXNL6NldpRr4ZZ1ytA_SAcnxBWzPy7zM8FJ-GKpGSppLbd2x4DlFmGCK_P1NxPYhAr_oVZ9rs_WnuAURlMGaIfsqPyJZpVgUTbs75Va8kY8FqUkDkAcY_TCq6xVTM7AJdRY39OWaSe6nwkjThah4Af9eAvHAWzO5DisdOYosZLO1wdsAfIyIeH63GdjedAC9Fm6V17lATsf_0wJldGL3rszNmXxmPpXClFxuwypVrVu4c9Qu4NGiXkLqbeoTIc1H5BxpKrYIayyEh4RKw8RqivMqYniopzljaFBdpeSVpXk7Z3vKF3HHEC3wRLz2UE-9JdY5yCE74f_LorG6V-pUlyYSzSqHvohd5zB1sKRafrAaQT52bhjAbsi6LVK5NCHBLpZADBVPDvuLB7uCTJlWY8XVSNDlQUamWZ1Q_xn7m9yrIxpQP8uYXFGS6-LbGYCLTJJQ3cgZPtoHxL22MfWZo5qayqJkSSvFFXYEwTYiEvPyrxF4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=dcjPb75sqIdGPPcvlYvl4FOWgqZhVerrcszwNTEYaFrALw6lOoCRrVoJ8BvaCOYXKDNjhPZNnQGAhNfaGkk24X7Ic153shdDDSuOJ9u7kI_s6YIpqysNjQx8DSg31fSQAqUT6OPbUgpGBz02wFR8mNZul4X9_i4nr0vDbQGsk07pHmW7WSu_vsODw5WewrVM-MuAE4IDnoeepGX5tuQIg7eIMqZwA494rJWmjKSTxzNxdMrD5Egbx0PT3_-a54Lh6uzZE6VsSOLF2885G8hpXFF4CzEEXjL03Up5GCQKpKGrIArBk35mjTYKHlwqubIBPStJOGzoN5p_d8TMKq2G5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=dcjPb75sqIdGPPcvlYvl4FOWgqZhVerrcszwNTEYaFrALw6lOoCRrVoJ8BvaCOYXKDNjhPZNnQGAhNfaGkk24X7Ic153shdDDSuOJ9u7kI_s6YIpqysNjQx8DSg31fSQAqUT6OPbUgpGBz02wFR8mNZul4X9_i4nr0vDbQGsk07pHmW7WSu_vsODw5WewrVM-MuAE4IDnoeepGX5tuQIg7eIMqZwA494rJWmjKSTxzNxdMrD5Egbx0PT3_-a54Lh6uzZE6VsSOLF2885G8hpXFF4CzEEXjL03Up5GCQKpKGrIArBk35mjTYKHlwqubIBPStJOGzoN5p_d8TMKq2G5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szdW39AOqUPaWZYeUizdKIjcPhc04Ms5b_zNT-90XyPh2tCvnaSDC-kcSCyKcF1lgfUO9WW9iYpXOFJat7grr_oMgTVqXcR7472mJNXW61zYuu_MPiL8mRWsKSJNtELYzXrliEQTwB9Mmd5RoDiHBU-nV2TGkciek-UjspGuHZBxsdJU4pn0g1eMVB_HitDMP0o68-bt_4FPCMHGSSe0BJ3CpFe1s4KGnFO6tlGSaqcXagb2jml3BpNqUSfYAUduJfrU4-HSn8daURiBrN2eMnehOiOOhXW1hUSVRUANB6JIKpMFokbzhyE09gMQZoiUCCLWGTjVPt5zvcfjB_6jKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=fVL-Q0YgiYAIB7NATVS0D85pmKECNJxpAJu1dGSdiYS-vmRKBHL29I13Y5sKuuQP-vbAOzk6cctmo1GHyOe9uy8Axo5uVFB5XAhLdyLg7h1LB0ceOoQtEhbc_7p1oGKMQVzDP9eZcZ3zhDM9gwDlH2AI8qvO8FyopxnWZG_6Eiol3kF_8zfDX6zVTnBFJpPzGrT9BZNqY62VLwSzt_9wiFoBTMxH_HzP-k53TozUHD42vU_WS0SffZ0eJtbkmp-Onyd-mbn3O1z5eHyT034AqC4yJhyDgACYxEJDK-7tQTgrkp6S7_0risOlM0Yd-eNr0yd3pfYmh6cQ5PKonUMb2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=fVL-Q0YgiYAIB7NATVS0D85pmKECNJxpAJu1dGSdiYS-vmRKBHL29I13Y5sKuuQP-vbAOzk6cctmo1GHyOe9uy8Axo5uVFB5XAhLdyLg7h1LB0ceOoQtEhbc_7p1oGKMQVzDP9eZcZ3zhDM9gwDlH2AI8qvO8FyopxnWZG_6Eiol3kF_8zfDX6zVTnBFJpPzGrT9BZNqY62VLwSzt_9wiFoBTMxH_HzP-k53TozUHD42vU_WS0SffZ0eJtbkmp-Onyd-mbn3O1z5eHyT034AqC4yJhyDgACYxEJDK-7tQTgrkp6S7_0risOlM0Yd-eNr0yd3pfYmh6cQ5PKonUMb2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=Ed--jvl3Y4vjWbfPL1kKpSZzQzAYU70WVylYs4sKKSYupxxF_0Z8FWeU4iLvRN66GmDf4ZylwLIGoQcI4hE3vv-B95G5BAWIemKhcMS226UZl5uA0fmxGIEyY2ehN63gEMfQyrTGFRpQhE7tjL2J5cQ8LyXzSsewlkht-ERhM2th1qNHQSKJcYAXE6sBYIPij8Jl9u1QWqe-WybViCogdWJHez831MNno9jTyTmcBumktMOpWye4m9E_sTNQPF8bPWG_E-p-jwNqyXakHlM_8S5Lcc_rwMhAO1SS4gB2wtTmT1Ya--PN9l9kxMOlECX3iDM0Awi_3iOXUulqNd018Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=Ed--jvl3Y4vjWbfPL1kKpSZzQzAYU70WVylYs4sKKSYupxxF_0Z8FWeU4iLvRN66GmDf4ZylwLIGoQcI4hE3vv-B95G5BAWIemKhcMS226UZl5uA0fmxGIEyY2ehN63gEMfQyrTGFRpQhE7tjL2J5cQ8LyXzSsewlkht-ERhM2th1qNHQSKJcYAXE6sBYIPij8Jl9u1QWqe-WybViCogdWJHez831MNno9jTyTmcBumktMOpWye4m9E_sTNQPF8bPWG_E-p-jwNqyXakHlM_8S5Lcc_rwMhAO1SS4gB2wtTmT1Ya--PN9l9kxMOlECX3iDM0Awi_3iOXUulqNd018Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XG3f9QOi3hKDDyJvO21Hx7hCCLAMCXCJRS72UU-RndNcIaVcYQgkChldHvKpo4c--VdJE76-vVQEQTlZbGzZA0JTKhU3MC-Pxw_yeQLEY9GUw1XZH96cqZkCi3zkKebnm7mwkTzvh6mIpGTROobJgeGrFkjFoG0ZfGjmRhsYd8k3p1YYf8541ak9Ui5Tf_ElRTyQ4Lq3e7k7m3egzW9iVqRJWie51Acjvjq9s1mFNxAM_kCayTubZzy63e730Bybvw1UbbPAZSAVRW0WnLYtj38vdla8_EqaOxFSDi2tgHOqCG6RVI5nvQk_p8v3RHp9T3ybwF7Zvveb0OqoxJ1TmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZEqPWWiNRlANetar915GXSvcA5DOr5NiSp_TTM851_KqsahyRTJIXvUEjoEUgyGPp8snDIUQg7w3gJ7P-j63LWL3ibcQtPY_EHeN07H-2A9pBXqj2gCKVWPwtHwdp0W-Yp6IjfYRzCIaljae8CLJobgnm3bNXvmQrPsOdlMkL2f8c778-MdE7zcsP6r_yXnrGG1wqbbc-Scn6q5HEbo30GHLO0A-dk_cQmGoKnb14NJTdZ8fVVx_sQo6Klpmdwal4eRPey7u9YhXHIxjdFDAtaZtl9RFtsmuqumFX_gjVB_i1o6peY6juGaL_Y7D-cbi_yHpWee9Eh0VrMHu_UqAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJb_xaXd_XA1jutx0oYBhNG44bUcWHBEx16DFyvdqiRY4Avwg9fqwnhP_c27i2nGS_oxQ_hSLHCkm67IZBrjSuYhaQM1TLqh8Mik0_c1DQJXqvu9BjCocfyXAABt8vkO2upODVa0WgdOZyUmKFRKOR6GygJWQzAVz7mwpjHcR72G0myZIvo2AY7kRgqm9xnJRWnd-bpxBYPzS5U93loF-7Kds_yNSFNqkTfSw6jhZrsfowOxnPLYB4loANz_PLN62s5K6l4qlm9Hne4kVSNfFMU_FNnjx6kl33xGaurLRUWvy-ZBj5l80IPu5pbaxwYA6QwJsAKyt9XPQ8-Dg1PmpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e64AqqYhYloXlssAIW6RNsnkG7U7P6hhCg3nhkolFtIqy2CWaz4M0u2NJbr2FlAQJfNsz3U33CrDNyxAWJ0aW4qIX4ViLgqFcjjPJiP-dlHM1eVfX1TqkRj2BFqCy220lD1_U_8oeA484tVIDuW4S3NfIs7Sxz7MnuN1EzsvbbtZNUq7HlUHBPewe6HVvOo6vdXcbCjR9XzJvlP-0NTB2WrM9TXUzQ1vAv_yjb3Xwkn7Sp0MvrBN4GBUytIdGqwrhFIlDPOD-mYPPphvdNw43iRPYgCAPFRl_k1ppErSXW-rcIwUReJolUJcL6LKr12UB_WPHASJaB7FctSt1iegiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXN1BL6nbd6fRTBrfywG7rGRhfNcM1JlriI1F3lAxWrlZwACylULYgLgHvUPxYGspBcHmZy8sED2zEr5z8NmWfpHlbiVJ1pM4cj3jhtMz-wumqo2WwO1lxMj37Pyd9DZOWEjNin6bJgaZOy0IkUnNfaNllIYBhRS0lTF23XWzcL20kF9v7DXBjw3jGLTlB7UJAHS60YhpkIv_xGWTy4UtANrw8Dfo9Efc041Zkym3WyloR8YUVx_TfwDTg0_ZQCeFagHOnUyu_xGsyOnd48qpDhDEMLkZ9KMwxaZXHXw0E_U7EpXRxZcpxJjXkBATA2TtOIS1PPE-4Ip3ORjHz72mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-etrp1vday8DDLVnGhIeLsapjx_OedWUR4NkaBvbWhJSDgAcCmTw_8wPk2iJ62OfpG8PrXMvINyL7u4OE3WKaBdGt3GNxiPanR5PbxaBlOwO6KYI39rj4lrGABCIT0zb1pBYMxw6n-eirc8lUHUfV4t5IfyBsXQIEiRZDv8QdKJ76_diSYTTSn2SmBHhmeXGrbXv6OefVM8jcmjmiIhis7zPiuHAxSvzVYf5vVXdcwyIQVPs7rZcHA8Hf9nXySRR0Cbj3RrpWCV9_61JNyVkFy4Sx62RjMVc0iluJ5QhbNS7ApMV1OYW3fHG2kvhCYslafV3NDAfkKCrcSGoo6FjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ts3jiyn_4N4_U9AjWDR1DDi5MeCAY5LuH7lDg5210lS1A9vUpAkLybxHPYTtjvEMlmbvEs4anKrPOczV8WwrOsMapmXbYPE0xBilVfhzpL7VdYSS0yAeBMCAeHai0Gct1r3JfDn3MJIKWtmyGPTH0pWmw4KQ7wxrIZwPPkYzpGxbqe47Tf9keV-lBbnXeTO9eOROn71o1K4E8iQR6zk4spZ8y5HBuTU9rX5kLor0LFSXRVcLVT9eE3js0Qu75KCJOFuc5d_ddJDisnWzyc7oKQt0CkIcFO2lEildvAhoBLtVWYt6tklO9U_0SdvEnCRYKVgmOP1aeuXbk3-KubUDbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dfvol-UnqzGHl3mplD8DuJxLcOVF5oIwp-VbbwAKUmc0vuYKHwCkx91mqRDB0ih5SaSaLMon3qKqr7sTw-V8hRjIJS_kkW7t4cuTfTSvRI0u61O7_cEYkKN9pk3zDeXQQsU6r90-TvKDAtMXfU7FhWXuMMGgztyIOP4Tl6c0932dIh4MZElHZXQywiCy8oN-gBdcPEVhfE2_gMXpyfXDGi42RRJbkWNvjlXj-GgybCM2QHr4O1y5kjNPs3JEgxU-Tc2wzAiBgB-nvBx-V_6WoPd4o2zl8q6YttKDkKUhumXwmFtjd5obD3eX9o1xa8yp7cwAcuKLL_JNNzCnqh6dRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ztxe6un9uYK1xlJNIFqxFUDloBnzjikWWO_U8ZxJdDMQLUZfqbivB2HCa7Uz00NJPUSGju0uwWUONvMOEdfgYAPRyw3k8LM92ElFe3mCYF9SFwX3Nwjd1pNbFumU7_5BOMHHZ_JoRQ-6Luw0O9oGjmFplcvCGy5e-Q2HnsR2a6NxqbfFipRG8wSEiEe2jO-w6RH5pDMWpDIRNmn8hbOStZWS8zQnXjTFkrgFSjNpFrQsfK_8Sgog-aSlaNYZXCGwN8N_dvSsA_vka8bahmMxgft2pY5SQ9dI6-m_vXIhoEMH4xwDT8CY0F7exhjSW2zUBW8IqNJiM_VYUGrpA_aPZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ODCyZyqYo2nzc03VoG8Hte7ZC9_TleRJOeodOpdKgHOuYQ_ZnLqsL1WjTg2EyBvrdadZxrL8iOS5I-04CpqHLrPr6RCYI8QXfPrMNwcXkwDJuuxnMdowZg6eR7DvgaUdWFeptmxunVIsULFtnmneXuF6riRY-g_EraiMf499G7CC-tR7vQDabePIUzoXylBCOhZUGxpi3dnpUOXS5FBU7o0BM2Z74YAFqQ7Z5DWkVE68YZe2qCchaVKTOZfu7djcKmUUKqXtfVAL8gsJQOBkfQNdjrYa5X-KxadUyM0aSJieyTuPTEy1zTcS1rrLTbx_3uz01gMcTX1qCyeTQ4mNAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=I7T8rR3ErvIJOd4_1JoWeycHOeQc1LDTquExK86eGpVI8s30tKGs2yXSL1_N4CiMY1hYd6yA3qE8rnTxnubRpMN9w50sCcWaxlNrrqjQgvpRkFLPUHE45_WiqWnZgwqvDoNKwRWRWdLKzVIdpT2InkOtsJzlrBs-rmdqAyajGrU2CA4stYw8oOcvs3aVPFdzkL0XOyS8jMe1_zMypyTb5KAHZFVy-sK2kUeO3zRTVV2YVnkF3fz6vWmZlzQDWnIMmNPaMR7aOQjvKqCm-rkAzvfXmpfMQ2GZBKZ7cL3GEpDSF0AhhziQGKyY84hHL3cGhs44Y-kb9YkbAAaDtRpKeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=I7T8rR3ErvIJOd4_1JoWeycHOeQc1LDTquExK86eGpVI8s30tKGs2yXSL1_N4CiMY1hYd6yA3qE8rnTxnubRpMN9w50sCcWaxlNrrqjQgvpRkFLPUHE45_WiqWnZgwqvDoNKwRWRWdLKzVIdpT2InkOtsJzlrBs-rmdqAyajGrU2CA4stYw8oOcvs3aVPFdzkL0XOyS8jMe1_zMypyTb5KAHZFVy-sK2kUeO3zRTVV2YVnkF3fz6vWmZlzQDWnIMmNPaMR7aOQjvKqCm-rkAzvfXmpfMQ2GZBKZ7cL3GEpDSF0AhhziQGKyY84hHL3cGhs44Y-kb9YkbAAaDtRpKeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHsj68zQO-EY_dbyb0tCpCkeW6evab9D8brLWCrcZQIcV2IixjwzwxLiyWjhtTcC-oFD7-qVK8oRdVvMQFIDzbTWshpc6cfnxocIq-ya8qNgb8s9DGg5kHWidunFwARoKFgp8PUkY8uO3xzfJKnnKH8C2Vyeo9lRaGpBwWyauUluH4QFjHjDEhMH65psvMozYWs-qnHnopPSHqajasU-yKk0PvA0u_hRQwf5u_vistknx_x502kBcunorHXxiET-wZtz-G6Wj-hHCSKjj4KGKBHhomReoR_UN2hpENON0y0_jaxC2HekCAk-estvNfkZJsgNASsWV88aXc-5tZI5Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGCFt3dFL_j7n-87lMGDqeMj_OnlghVsXxKJBhbevIl0j4Jq699Kc8ZF8LLDgiPvIuCPyruD1jUVq0XfSpDnzxpOdv_VCKy35LSWs0vVEquZkfGoWqr1pDT_E9wNnMhNvlvItbNYRUOnQnPeoHTiUHPvWUGWbhPpAlhZHPb1HMM1xhroKEWwmOn__QSBZ9IlVyfWcaw5j3WaZamW843FkO2ZEuNqF5jXhVr5icQiETJezi0eOzGz-HDnot6G7hd5Q0otRWd3bCfpVIcVWgy8nImAlQ4dTrLn_8AHcClO5dhvXs-6AXro8Bj36w8n7Cn0evolq05pOrv7k_cas58GqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=BcrcbBo9FWQ5GZHx5mLIETeNJ8dl308OJEGDR0a9Fd-UQ6PHj1Hid_YJzZTMqKEOp-cy8Rln3ceWBiODBuXT6-_ZSnjCrTJVP8SH5ZnEKL5IvkJkZU_x7ENL0_25hruLd70wdJZidxJZ6t7qSsQGwJeqEFkW6zIym3T4s0SJeHIGHuHfA8r03-hUsLOhUC4g7bAMU-bazsKnEhK6wl-VbDPE3CbQ9DrMzyjTPW0wOzqGgER0JBOtjNXUHy8VR92IC4t1Rs-GJLc4kXZp2IOZmHd8jWj_76XWZCA__MIxgpXb0ShoXuMFsEze3UJVUf1H2WsBh62lrSkLpFj8r4JTXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=BcrcbBo9FWQ5GZHx5mLIETeNJ8dl308OJEGDR0a9Fd-UQ6PHj1Hid_YJzZTMqKEOp-cy8Rln3ceWBiODBuXT6-_ZSnjCrTJVP8SH5ZnEKL5IvkJkZU_x7ENL0_25hruLd70wdJZidxJZ6t7qSsQGwJeqEFkW6zIym3T4s0SJeHIGHuHfA8r03-hUsLOhUC4g7bAMU-bazsKnEhK6wl-VbDPE3CbQ9DrMzyjTPW0wOzqGgER0JBOtjNXUHy8VR92IC4t1Rs-GJLc4kXZp2IOZmHd8jWj_76XWZCA__MIxgpXb0ShoXuMFsEze3UJVUf1H2WsBh62lrSkLpFj8r4JTXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=ayB0YvrfoB0Q5PmkvuQ2IJBffA1uYM1GwvfEXG7uGqq8ro0mNeFkKx_y64x7UQB198whtMEupu2gFrvq04za-GiLOu3UoQ_vsRqCYVIRPwGyw8DvrSeqj9wFI5_b-yJFsyYQbBj4kBHT7IVwmzSvdCUFkuHqvd2nUOMglXHK6xpPWYDYlj6ujSp7wkNTFjKNIAQmmNO4_ZA4Ca6URP_Orehn6r-obIo6SBayHZmHcfELwcFNf0_QBNm7otvZL2CK0XgEQ8gyV79tos6l_f8RYuAMS8MwJLurb6q7c6YuO3Da5aJIzQdxkhRb67UllEsJf8Nh3-qnVKvD9LcObJ4J6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=ayB0YvrfoB0Q5PmkvuQ2IJBffA1uYM1GwvfEXG7uGqq8ro0mNeFkKx_y64x7UQB198whtMEupu2gFrvq04za-GiLOu3UoQ_vsRqCYVIRPwGyw8DvrSeqj9wFI5_b-yJFsyYQbBj4kBHT7IVwmzSvdCUFkuHqvd2nUOMglXHK6xpPWYDYlj6ujSp7wkNTFjKNIAQmmNO4_ZA4Ca6URP_Orehn6r-obIo6SBayHZmHcfELwcFNf0_QBNm7otvZL2CK0XgEQ8gyV79tos6l_f8RYuAMS8MwJLurb6q7c6YuO3Da5aJIzQdxkhRb67UllEsJf8Nh3-qnVKvD9LcObJ4J6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WX8y0IqDzV0ciTLAESzX4eAXlO_scrUQvwiVaqPwqAcRO1w59K_CKMOOkmYUuhBiSn4WfG15qW6eGTH2AyZgWl39yXmJhwwkZMRFqu3Ey4qIKWyHwrBN4kUXcbcV0rJDI3mvkzcniGGJryaMcRKear6u_0Ewj-pScAl3_AX5MhE9KWNGa2Mxbx8yhlzvS_npAqkbf8WFfx2Mxwdy0L1do3rvFMC4tmXW26Mw3_0V4R5PxCduTmf7_9J53GECxXjfKDosnZ5WI8sDUYptTcQ_1OM7DCBS7UFtCbEpU2-sn82UVV49NCmzYd3_jwH1HS4A-bulNhwmKYtD16jd5k0GbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJs1OxSKckqFTz0Lgc2-bAk73-1Y7-LvFtMRGy8EkRVkOH6l2MG1BWKJfTxKxWqe9vJjyvJcq5FsnCuw1fksX2htsyrRwJUo8RthKkrHpRxARDysIOqWWHcuTiaAzvUIx_lLGSk9-x7-lJceCrsLt7rzIjlhjCPynkv-njxYpwUkzy2IV0QqqDm1L2MV5ZcThszx391Whag3fHo6qp1HboNlMztv0kRgqGlfcBor7fJsbCQAokSDKudiazVyoFliFuLCD2p_DwWRCessCgO9Es38GVeirm2eqO7joFdiZUF5kHLeSB0Erj7fBrC9H6NM3IiOTzqk0uKaJzRK8c2hIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IweHHsHa6h5PuNWpQmXLS6ZD7EFQkrf6WpUx4m0MDOsaSmoGPrVFRk4vecw1gWVo1cuIqjGIHgrikneG2o7_hibDJt34Udh7nehJjN8NPiSnfFedis_Tv-P5_DEzu-OIYyqxtl1LhWDhYfHa1ashUJa5COPZyrvmBXxcMRlxccfFc-kOtwfSj_RMoqaOaA9dzXMTR9t9PAGh32y_HQgxiXXcxrBsb49aLYNaOfmgPu4LyWc0hgKUynU3aXtQA_cQj_6RXiUH32Gb-f9DjWak1tT5ltGjF32razMcpIupNt0e8rzgmLHnVH2XHRSoFE0WcplHnIKOnxspexNUWFDpbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szqoELmw4VKCvU0V4TB1HbMjxYiVvGa8RTnVNwRAnxMXuDqXcYybbrJvqq69z9HQItSNKyF4xeEGLncZavDdUc6VFeZal5f4LmCZLjcKyL88_ne7VlqGmr6Nhs0q_86v9p0bvqwRwzbVkFAYrz0EBIxpvKhCH-Kd1G2H8LArIOFsyzDWBeJnUV1cXADTYZkDWunUl2MSubv-eehzY7HByVgDA3i74rYiDIpjnBXZcs_bBlWu9sXkYT6I3QZwN87r9EoeJPl5CWQngh2F4jx8TZhYw_YJ-27oxrPtbAkiCGQzTCJGGQTicFh9JiFGGDURfNuZ3uposEVIHyfonHwcjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkMSNI4PEIWhkZnrIzlYV7o8XKB4H16CZES5K_Ss5bdaaEsZsWd5GfHIZ2N4IUJsZmOv-iIIfvKC81TS_71mH2zeqTUvKh38hiEFUCMy1WNAKY2dM8urT3ctP-fy6cavkExDzrJ-qtKx55ej0prxxBM6CJurRpCimJyLZEXzJvsjqcUF-9Yh9YDuWi-y2o0urvPEKtkdKOW_MxxClvC27v08Apm21WqvQ25ezBrvEiJGTIzYZeOUcAGosuK4sDdKclDIGvMvtgl3pXnENMDBvG-G7EzJHaEM4Py3elDW-QcaUHpvzy5m7Pvyhnt2QGLBZ-zXe8hXhqbOvjWmr2ij_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5dPau8aXiBRhmJx2SpiMIVQBougGCC8YyrLe5dLeTSVARzOWfKflVou7WkP6sIfBICPhg2Sd5yYACe0WGBKO3g0mwhYW65MgO_J2cSVmJJHP8dVg3YyVStOeBWKLtbU8ellstN5UShluKoREwjsZ5rrZnWIy9Yo2j65eHCgssZsDxRaMsJberElZ3laXd6lpa4nGTDbaRTY31kotR7oGPg8Ku76BVacNtcCratxZMhRifP2_12rRXWYU0wLIyQLA3gRjoaBFQX3aLo6nvGmjvK1JcRZeYRbePhSS64F47IV239F0KJC1p9ye3u5h8s7RbvjNGrPaOFeJkrOZlhuAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzfbG-kzCRZM64_Uh1Sdr_zpwW2WNVW-DG97t0IeN_YcZ7nbszFGNonBJXntbK06pp5rQBSjRJQ8MIUaVYkP6kIgOtKqG9mvVigM38VVexEpnXl6Bp52giq5F58m0zusUfY6nswDTYmt3_5LICIkObSWm0TDr2qHEUnVCwYn39ukIuX-c_BCuJQzTihcFjFr5URxZx-7gNjSFbBq725U1uPHfiSa-PjFCIgmxJ3KlEpBD9OMwfA2cHSvw4HUF7mUjtlsD95goJKQviIzdn22BGJRcNtcnHm9qwT1vryzb3KgIFB-wPIUsoHXB3VdZ8gFsWWZ2po3o3Cj78meTnKNPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=Ygvk4DyrevEXRT2SjMxYhCeT_bLhhWulnfUayg83wSM8y5n8gmMDcKDsy6r4RXa-ifukP4btDuttq92pxZIWBZVGwmAFZgaxbDzhM-uiAHkXC-1Cxu0VACixxzuIxSeVWL1q_zu1VqpWqLRCbE04DYfYpYb8XPR-PLQdULnzeSkUl9Rz1uz81jY4B7KUrylhJot1jbaHuEH_ym4pvE6lmKPY50LOVK0JZplmtFujz9E87Kj_JqlKkfLK2Q_I1fUsPITD07FusmLLiqaQwe9CtKPQcCCU30tCWFh0YjTfRU18JGcz7NUK-dxZfZBkcq1m5O6i7IXHwGW42lD_nswaGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=Ygvk4DyrevEXRT2SjMxYhCeT_bLhhWulnfUayg83wSM8y5n8gmMDcKDsy6r4RXa-ifukP4btDuttq92pxZIWBZVGwmAFZgaxbDzhM-uiAHkXC-1Cxu0VACixxzuIxSeVWL1q_zu1VqpWqLRCbE04DYfYpYb8XPR-PLQdULnzeSkUl9Rz1uz81jY4B7KUrylhJot1jbaHuEH_ym4pvE6lmKPY50LOVK0JZplmtFujz9E87Kj_JqlKkfLK2Q_I1fUsPITD07FusmLLiqaQwe9CtKPQcCCU30tCWFh0YjTfRU18JGcz7NUK-dxZfZBkcq1m5O6i7IXHwGW42lD_nswaGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/my-hxHx_pGEbXXhzO94FQXisiPkmBiOBnRNQ_vx1ZvXVGBHIbflygqdx7epeyuKprPviCC4xr9F0j6CCHsBqj8cSFBpMq65SbIqJbSCPPlAJCVqf50L1mohTIXphsM3VbBsA6ZZvrgPFk8UShecZdaz_f-YGHfYKAiTVu_elMSNyThDu9dNJIgIOpHKXHUNX_J3f-BVWksOrILMUW-_hVWXJaACBvRkgrfY-xKyq1w-XXz4aFIaeQKIT3GUvXlb85dLSbfOPMWxbXPkOA-elQObnISUG6ggxEGd2UV69nAYfh-m6OHfm8uPsNGjIZQOLtVelO9YNhO8Lq16EgrKN1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=FE7O2jqiwHCCVTGaW13YgkwsKJ8I7t3kvWKZyho_FIaJy9XwSb1oa8iwJPe9H4BehRch5qMHQS49VrFtpfYRd75jJMRFB6eyx3ZlFfxcPXsJXoUgpws3VAqZWl64hfDU4NGqaqbNF8lEWN-i7-zq6HzBVyGDfecQeh9hgcKfIQR4qqJ1O_j60_EEkqgyQf5Qsg2M6EDNmOMXIckEEC6fsREmtSXUJRF6DbYlWK-UVaZs4ZTu6voUQrnrkJ7F9YYPk_m4WbUZGTpHIXk-MIoj0XP3ITUlOdxZ5bDPtZJs3BmmyTKuHkPu258LpXsuhDmyVHs5nIdpRHqtoL7i1-WcSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=FE7O2jqiwHCCVTGaW13YgkwsKJ8I7t3kvWKZyho_FIaJy9XwSb1oa8iwJPe9H4BehRch5qMHQS49VrFtpfYRd75jJMRFB6eyx3ZlFfxcPXsJXoUgpws3VAqZWl64hfDU4NGqaqbNF8lEWN-i7-zq6HzBVyGDfecQeh9hgcKfIQR4qqJ1O_j60_EEkqgyQf5Qsg2M6EDNmOMXIckEEC6fsREmtSXUJRF6DbYlWK-UVaZs4ZTu6voUQrnrkJ7F9YYPk_m4WbUZGTpHIXk-MIoj0XP3ITUlOdxZ5bDPtZJs3BmmyTKuHkPu258LpXsuhDmyVHs5nIdpRHqtoL7i1-WcSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=iR_OkmsQdvrh43vvan4dUWFqtKrR2FJYH80cJlGRlFlVr3Hj1QktGxwMiKp5hVnnDywLwMFDyRl3WpLSTNzxlMESw9wgUaVPlKH_qavHHuDVw8aSB6zhTvuOoKmRScvNinOD_oTpj7Vm7UPdbATrPQpoLH1I3XJyDjI2-ywPjGEotEuyI80dhh5Yhn6Rw_ltdXX8umF3Lkp3RoX6PIt9LNwTs4xhyNQHbrQ5bLng4Ao_nKHSymEtQ6uwVSl_GXjx-ntqVJD_MfFxyo0MUrnh2I34MvezaU2Lpv2Y3QYShLns90ZPtbx46GhR3uvX3c6oU0xdVEZR2egxe_IjNsznYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=iR_OkmsQdvrh43vvan4dUWFqtKrR2FJYH80cJlGRlFlVr3Hj1QktGxwMiKp5hVnnDywLwMFDyRl3WpLSTNzxlMESw9wgUaVPlKH_qavHHuDVw8aSB6zhTvuOoKmRScvNinOD_oTpj7Vm7UPdbATrPQpoLH1I3XJyDjI2-ywPjGEotEuyI80dhh5Yhn6Rw_ltdXX8umF3Lkp3RoX6PIt9LNwTs4xhyNQHbrQ5bLng4Ao_nKHSymEtQ6uwVSl_GXjx-ntqVJD_MfFxyo0MUrnh2I34MvezaU2Lpv2Y3QYShLns90ZPtbx46GhR3uvX3c6oU0xdVEZR2egxe_IjNsznYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogxhlMkl8OVwxmATQ9_A80ElWWAfkc0G0OQ8yGRKhHkEpu3-k6eCq-HO-uOm5eT5WU2ltEc3_IS-Yx85jU5gcPHRVcK0v2TN4Q5wQVLLCKV23lqQ3baFpgiFI1YIIWpwM535KmknyXPQziWCXh19NY2pDq5j_JiwP11E7ZPcgBfx5fAhUzRdBGgXBHWUHGqSz0DwPzS9WCCok0WioDi7HtOa9-N5Og1DM45ysf-mMa6EtE9BKxnNTKgcN-nzow9RG5PyQWBJ1Adv_r2mlOIqe1d5IbdGubl6FVUcI8UCwwDija9GCooXYmKX9lPNZ4EdT0I-UHNHPmwTJpN6Suy4hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHAAObjEDnGQThjTnNNYLiF03AV279S6yBXdROALiz6EhrR-J7HlTNdVBV31Q1mKNkklUereWr5LffcpgtScpTwhuUi-UxeHxd8ARCbspo9zjOQjHO1Rgy8MMKVaUqzadMvZ2wlzlOUaqfFlZORCUvRii8gPVeGdneeT0exXhw6abhuQJ1aosf_RgtJ0Olpyeeck6z0sN-ZNdt1dv2ltfHmxb5tpFjaXxWKUvoOcu8Tg77heG3gdb5av_tEi4pUubHYqi2lm5Nn6WldDCj-444qTZLtAX0wufQikG2xtfF846sdfUtccic2htFbcq566HStPL2powMb4m1fJGaVWCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=Solz2i-xq5RrDeMdk9M4a80kydc8fbq3wc3YMyCx-hnfFZK2lLdNI46KtYyr_5IA1chn16bNECsTad4tTkVFCC3Rolz4sbeQL0_347J3B_-hItk1btr5v1JUycFVG3Rk7A9DE87DterUXavABndS2luO1AkICN33nPsxJ9CoPJxsFfkyLJAKodubW6Zzy-idQWiHbLVb9w03fWQZNjxRztE0cZbGzWjN7g1oPfvqr4Zl5hSC7dzVNTILke2jzRsPUz0olWLMU7g3TvOmPF_sZcKZAdVxoLd1-3Pjz-xZdXlQBlvq1DwyxdhSXJtGERLulC2--__PtTaZw5xQtb8MM6i8wqhOmKFL0jaEPhkmUu0WqaqOv_yKmYfwILe7xJu7OY3U9Daf52sochdYqnsdYe9J0UWRUNvTamAC9tVYh7DxMedDddVTZOrWJqZr2AsuOX8rQHthzh-zOKHZeRQFYE7g_WdUFACrkVmaU2c0jQWopCpi4E5pG3kP28R9iaq3Lv8UUccnkKT-5Y3GbXpU73w8_KdPqPJzWhlF3A5mCVtPQYohlkc6I4EdFQrqT0xZD2pkqpgrTC1fn31IfoZZa13mL5qRqTuJjLycaZ2rrw6jxzyfuw1rMfmH-LylEnWbmk_4oyBeOpOP1trl8d7FGgCZowOSwQaP2LvfNe-7xxo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=Solz2i-xq5RrDeMdk9M4a80kydc8fbq3wc3YMyCx-hnfFZK2lLdNI46KtYyr_5IA1chn16bNECsTad4tTkVFCC3Rolz4sbeQL0_347J3B_-hItk1btr5v1JUycFVG3Rk7A9DE87DterUXavABndS2luO1AkICN33nPsxJ9CoPJxsFfkyLJAKodubW6Zzy-idQWiHbLVb9w03fWQZNjxRztE0cZbGzWjN7g1oPfvqr4Zl5hSC7dzVNTILke2jzRsPUz0olWLMU7g3TvOmPF_sZcKZAdVxoLd1-3Pjz-xZdXlQBlvq1DwyxdhSXJtGERLulC2--__PtTaZw5xQtb8MM6i8wqhOmKFL0jaEPhkmUu0WqaqOv_yKmYfwILe7xJu7OY3U9Daf52sochdYqnsdYe9J0UWRUNvTamAC9tVYh7DxMedDddVTZOrWJqZr2AsuOX8rQHthzh-zOKHZeRQFYE7g_WdUFACrkVmaU2c0jQWopCpi4E5pG3kP28R9iaq3Lv8UUccnkKT-5Y3GbXpU73w8_KdPqPJzWhlF3A5mCVtPQYohlkc6I4EdFQrqT0xZD2pkqpgrTC1fn31IfoZZa13mL5qRqTuJjLycaZ2rrw6jxzyfuw1rMfmH-LylEnWbmk_4oyBeOpOP1trl8d7FGgCZowOSwQaP2LvfNe-7xxo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkgKmj8nF3IjcE1teMTlYsc200SRBbxOdeyhcLBIVFB4kknjctfA0Nq4eJOOxGPFyfuivtSTSosMQS-GId2CWfI0g9BLx3tJU0-HIX7wVpcbepQN0qSEGoEcyytGjzHFb5mpmn9CGcS60Gopj4H3Rh620cA32R4ywtmKgipxAwbN_WyAKAZyu2ZEPmrRAgd3s9Uh6Fizjyv9OoJgFTP3Bmd8Y-SIH85ZmGETycH-dmlzLKa8aR_0RUgwbiwIXZD78PrcRe99EhJv3GeD5418LrW4ie0JCVsRFxeboEFAQ9Pq_KHmNSsKr_Fjsv7T3AGRwgMnJtlpZXuMAhnL2MGuuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=r7eDb_aHmd4miHK64oWw6vrv0l3Hct4sPz3ykJ8qNbohucf_6M0fc42DlZNVj9SSDqA4U20AMg2hD11Tk8BcDlqaq6HcgVF3qpfahu6tCdcsGhp47Dfvt9VuOB32REOrSCvojhrG6zCTgK9ZwgbRBMrmCfT4Dou2qxjI4ZFtWtRnzAN2MiAr0JV6Dhsr7vSxcozTWTNMeTJtiCZCxCqzq-2cdMgZRlgRCi_3rHbNTIHWQr-rvYEUFHXqyy-a3SOEmUHe5A2q_m3GrWZUlcKA-_qhodFiLvjgZKpheEsGFxpbOcN5SFDJ5HjX34Vdk2n38Twizmc6Oosj2LiyoE4tPkhBaIx3vx88v9R2gYrv6wizLCW1FN2gwa3_zr2yl7EEr6X9eSMIkYTeZCOkT65wXrYkPaOvml2UboCB41QnlKKC-wvxV6CTA08rRXdxK1l0LKF-0EOWKmd8vjM0bkM9UmZMj0-rpiNdJKyhvn302u-qpJqC0XOU-Qg9RkzX5hOoZAUT9uzdUhWVRAQBiqXLoYOPx2qTQnhPVDLQf8UbiKF73V8hOUEvX-69X6asNT_SYvtuk-SZ9e3F9FdKC66MdEY8hRinjpUiMXEwLhArnN4j8raZDaAs7fULSQHSc6osaOrnsTNkv9MQEShq8pl0k9k0_pOZDjpy-LNGnuQ_TXk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=r7eDb_aHmd4miHK64oWw6vrv0l3Hct4sPz3ykJ8qNbohucf_6M0fc42DlZNVj9SSDqA4U20AMg2hD11Tk8BcDlqaq6HcgVF3qpfahu6tCdcsGhp47Dfvt9VuOB32REOrSCvojhrG6zCTgK9ZwgbRBMrmCfT4Dou2qxjI4ZFtWtRnzAN2MiAr0JV6Dhsr7vSxcozTWTNMeTJtiCZCxCqzq-2cdMgZRlgRCi_3rHbNTIHWQr-rvYEUFHXqyy-a3SOEmUHe5A2q_m3GrWZUlcKA-_qhodFiLvjgZKpheEsGFxpbOcN5SFDJ5HjX34Vdk2n38Twizmc6Oosj2LiyoE4tPkhBaIx3vx88v9R2gYrv6wizLCW1FN2gwa3_zr2yl7EEr6X9eSMIkYTeZCOkT65wXrYkPaOvml2UboCB41QnlKKC-wvxV6CTA08rRXdxK1l0LKF-0EOWKmd8vjM0bkM9UmZMj0-rpiNdJKyhvn302u-qpJqC0XOU-Qg9RkzX5hOoZAUT9uzdUhWVRAQBiqXLoYOPx2qTQnhPVDLQf8UbiKF73V8hOUEvX-69X6asNT_SYvtuk-SZ9e3F9FdKC66MdEY8hRinjpUiMXEwLhArnN4j8raZDaAs7fULSQHSc6osaOrnsTNkv9MQEShq8pl0k9k0_pOZDjpy-LNGnuQ_TXk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzpG4NDO-txGbrMzHqE3bJCsElZyTS0xfAe0QrAkXmO4Q1IcCydgXPFCJLxP9uI5ZlSkc7k-4sr7yoJTRY0x8i97GAVcNAXBPzCxbH9kZAbQZfzFUfC-lUUufMkZSWcYNgVc7ijbVCVFO5ziB9GpXaY5tqF_ngBpp5kq3tfTrzaO4BG2b98RdUMNS44x_kfEK3G0Dayg0vtm9i3nrCaiTxzaU5JYcbnHh1RFGgmw9SusHaYAbfhEvftNzPvHzSPY2_ChKjmRbcZUOfif2QEFn3Y3VBYZyfQcShFdXilxQLDJhZmaDt4nQm_c0uw32zj5MhuH-hGtT8GnALqepoT1oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-1gnhy8LK-18uZc1TU89z-mRqLb7_8_VcBWAPdMI3-VWr5BJl_3nuDeDloa9wq4b9y9RDexcqBSkseJO66tzu81677zwFSVivCH74CTd5XRcGNvOanakncFbADQWYGty78gkJuZtRZNbCXDHVwrEudPUWDv_PVp0pHhIIywdO9sIz7I_O9p3FaIyhmeKIMQEjOR6BpzxWxhmIgJ_xTFlURvaemY0_atXmRgkCK7XGuVr1vHjy_DHJGx8wGUg-aAB4c-k7SKEcP6g3Kiy-TtpUhNBufVfWFl2iAMyWssQKJI09te_I36aq1hlAiAbBmSBzYowaiRMPrpGCBh3EV8iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3I5ZdCCwMXgqc8H5B9HEIZnxoCtmN0ft6rb7dH-ZOfCdHHJXPCuYaf_XgA25PbKmW4bjsaqdL1VJQJBhWtYREMTFULmO0Gwp_V8VCyNWJf7rHbJHvBDXtP0x0thMaALPJcd6rAdepFRz8uPRNn-7RgZggAaPqGddAlpDEYfcaQATtXsxSU8Gu7DGW9DQuPJTJn4sFQNNc_wWOBbhiRveNjjxvZdkRsomcxLyhwWmWtpBgBElpqBf3YqXsEsp2Td2ifEaJAG1AVSpeFRtEDtBLthPMsuUUentMTt0GpiX_2xd_kI4tP0AfRGNnUX-eUTd1IetqN7wfrf9ec1tkQbVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsHAPPTDMnyc2BMEDXi52SXaSBVVz_ACuYwXRo1BVPd1ZuYgst40nInvtesMexiIQ5PTllSJfUuD4JxysjIQWaMYUUgW7UGU2byMa06DsXiM2Ou3i1ZsFtRbLab-YT9WZDikt_kPj51G_mg7GJ7Dv7ABFU8m2lEr5p6p8NrWEZX0CkIMcJTcX6luw12VjiDbds8INMWQ8iliwrzt_wELf_ZA8TtD5kHjGl-8mp1RFkBWBeDyAfQoEP-DfVhIV5CrzxlzmgFnjp63G5aZvKk9SreO89UyFILegDgWXF3hQykiDs_Bdc-YQTOjDETRuZfp2BJR7-JrjBYDm21Z2Ir3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aa2A08S73J_atnsR4kLCJNSSZ6YI2oJkR5Zqyx0_5qyzgLJPQ2E5j-UKJ5-XZQbOvwFBD4adWNj1zJQ-dy8Gakmh4UJ2npx264ALxJcMHgHySFnIcqy4R7gYB4k2aMezwTH-JUP-TLEcmfxMM2Yl-T0qpDGAKwvWXxESVQcoUa2uG31r0TDf-rOn21kEeta2UHMkH7RTC6y_RS9N1IgzmqXAzUG2yL7gV8WcomD2-WVCz3WcooT2bRcTRT4kcCFGmbb88BKx-eIYPa_71aEH_gH4Qr1wPxpYXmr7ZVfSAzff8ICR-lX029wn4qO3Rh8dHRf6bXiXdzMoW88yaaVANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9p8WhmXDXKAC8H64nYAR3gGqn2_7sPauGxz2GiATJx0ZZGFX7ummifK-z_b5mGIMn-lPJItHe0M1ThdhUXnHwkszVcSbuSQ5qVmzmxQ-9R8iDqG01o1T1knyOzCr7t5e4AjTdkLfHYt9sn688Vq5RGoDx2royA39xMKKWU4w27MRX7IafQGlM85ZQ5qUnfDpPd6WsN7V7LpcLw76xSqpKgGvRQ-IZ3tLr-oo_DuNKf8RB_XPMjW90CHf5t6e8rlMvjfb1jKlzqFcFZPxWeIMuzrJ7n22I5CWRtz4RzHwsBggVbH1L8EV-Fl5hVOfFlK4T3xQn_NtG_dC_ejhPQqDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kd7mXDs9ikUikNt095ZMVqHrpUblVf5caVBU_f7tS68PqQWMmca4ugHVQcgv0kH6PlEkBu70u42DBCwvEDCe_g-JUlR6EQw1QzGROs09AHzNgC2AE2bo5Z3OB9_dM5QpJb1AI3H0OtHJLlzPTGEQeWUbyfAm3nNEeDTpL3e9ZDahsUrtnIoC_mHiuL1UlRmwsV5cR7w-1hC6qWXpluLRPMSoVJpKi0g7gxSyPWErJrB-7wi9aU-UThwyZJHjL6DJnxcYOwq0ekI7bx688Is6AHP3_xQUQNzbErojlV7YbSnWs-wrjNSskozZwt_NRnxt7lGAssuOzyoxF6h6MyvcjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlH3dzJ4ezUjbRQyGBVSLaREAsFruy9d8qLZ2xpgam9D8VX_vsOhXdYZwjLr15rSbjCzpTKJvNE0F0Dxp7JTTjnOFcV0uuwMn7OqPEoFguDerJ8ElPReJ0ZdXy3D54HU6or6KKAllWOmO8_YtHlcVPeU-EzQwNsvVMbbFAY7UR2uSQHTZnBFPTUNZz10pp9BMrm6yNK6_P7AHVya-GWBdzcveUfC3IyXRQ1kZS507gHTp4VQjSruxuckS4bQ1QEa22EyI4YhFXcHZjFqlHKA6mQm1z3DDib7ZLQE739QBid-bsgLINyYVw-5hotB5lQSpUtUvKbFmhbcV8eU42SQpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgJZJ7n50VIv7xuq4cnKS_04ZPSYeAZe2fHHuKFjhIq078d_U8DITQcQQKPI6q6ZlMNgD6CIZ_cyEB7OKKX4OHjIi3Hz1xiROhvbSkknpKkwy5Iur_n6qjTNHIDSZyMETwTIAlXiSy-l9LcEr_QP0vtnXlsqLxeqhvHREQSVQfBjcF5XrSxRpwOtSyn_4rYxqQFNjSFJ6P1Ncuz355wJH7Z4fDoKcF_uRYHVfHDYoqflTbmuloXI4cnPZxtl4J142jlQbO5lqf5J240QLHJUUF-ttUZA1PtIK1LTIJQgsFUjSOc9tU5Ddw-z4bClXYO_J65LqbWDxMLHvo1b58lRJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMLsuuHPj3Cq1OrTwPLDyqzkjvcUjY7OR1uhJPNcc_JOJiKGumVBlk6awSgcLsbBB_kwggOpdeMMZO27QU7l8YvfL-MW052eTeyxsKKPAR6pwrpfdYTeRpuyxcG6kpdj9CsD1vpuI_r1UHaF1SZjMXBa4A8FtPquciVPn-xPKCPSrgMLnA5_ZRcG_NTWF6zjZRcQU3VajbN-02ij3RD6cq8lkLTy1rY0OG7_l5QouVq0L_pk1Oe3KJll_dXQkUAo12qODKGPMXj1nrIymzuWYUcJ5smCtvMFtHW3WcxSKXa6qtJwHzDe0Uxv3QB2To8QFcOr6JJm-zSmgRoqoPzbEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCiE40gytY84AktMmHVnJ1ZqEa7quyHjX0HM2Mr1cy_RfPP95vHnu7hplALlkKxDh4mAjj0QXM-Frrvpl0MPkPD8k7kb5fl5GaPjTugoALeJ9tGEzCOqyj2xBU9dIjZyYLY7YozSS0n7FdDoMUKTAO1QlI6OBN10CQtANo6fcTui_RbIwJCTP7EuMOnvukCQ3dniVyVwQWs8jc4uuF3QfFeeWofA81irL2Pu4SRXV6K2Ys8ArfVJ-DF64M99wusV45CSeFHw_QlZ41LoYQg9g0Bkgc3041fiumFJAWqgtHiA-M7ZRpA2TQwm9JeaCoXpOKyux2cNRfsyteGQl3bZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsYo8LA7WxrGBxgm7UNVJ6IlyUGlvYl10Y2dtkecZEU4Ahb6XWJqMJ7LDtvuu_uGL_B1o8E8nRVqM1X6t426vWNBGLv5A_ST5QritGIqnQ1Hcljk24e51YR-0yU1OchWTuAj3LEkZVAa6Dvv5c3vr650EJ22sOk2NLbZT6xhboN0TPG1oCYxYX7sCqRf1kuO_IkSn5pdVCtu-pZoDhWnAOpE5CA3UnptcDZA_Q-iM1lGNEfbWmEVsk1tw9J8sNiuPWf4Uznj9B1O6F1VAAlbB_xp7uBkNb9IZJpNS_1Rt2OT63eAenXxH5rEO0eWTNkW774hRCrHP6pvAUzIEd5dFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2rxGEhhxK4DvQaOhwP-U3PFiZHn2c_QJtfLhhr9gDotMg9OOZ9dxhveGdb3lhWSeNaRlSMkQdfEFkbQt-22x3462OjM_LpXfglO67JAgHg9BrO8eZNzqFdIi6zzrniN6aGtLn5hCAqTaUTQ8n4d6wXBUYXNcClHEz4JWF6w0LDbOPps92eueP8AMzcRKCuZE4RTg9s3ETkR2o-W60oyoGSHSYCFGXo3i9klWfskt8SGQSdNuJA1zO_9tbgXDpeQGjQ-E99HybcPWUOxeJb1WFTW8fvsn-up1PvrtqGvDn5B8BwuDL3aHjJDyYPG6tzyjgUQ_KsyglmmujAdRfoH-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaJYmpGRN5gmG3_lnK3G-GExyxfrvd3Z1h_WwIBQYh-wSW5K6dJAixIkeCoYv3LOAdeftLPzK2I_kWmuE1he2cpvo6TgSMLnkO2KQndg8x6oRjVCIfXGKuAp8xV9MxEie6TJo-sW9395cOSvKzQqsOjuxlkOuPyqi6jNurNuVcmtdqyhSp02sWlq_0YwPu90lnkL-V04oBswLz6po7ITM3-kFTNc7RtY7eWyyTxy33I0D3fw2zr8m3r2PKXSLrX3Xc8vebvQ9zCOChrXLYWIKdRGnYwEOQvoT4j1kqTiIE3qKbuhuCRNM9S4xHEiHc7AW-PslbVpuRX1OfvoWIb7vQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3xByTjbDleLFxj38BjtPqwWRdm2CyoE8xL4RtTCn9PSnO_zG8RrJZ8EzhOxw_i2CEWnDegjopT3JfJDRhRLG8MZS51fKPfNV1WK4UgCVtnejPrZzaYhthrNG9WXmJ2V8z2Fsg9VDT4yqX_tc7Zbb723_n-_ZL24xP837YAc2rlPj9aaCHKuwBgMnuySjaUd2KyFZ7DGk8Jgs_uGHyy_mjWLd13OxtMOei_b7tTAtN7fvb-WnpgtwaLyVPrFFOOxD53mFLElNcsjiaYBsi0WMoKBbYoqEd1Blntgb6oS55vrftKY2zTfI_snFjbqaD--jgIIrkz6xpigzSlJZAqfag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAaZ1ydaHWWKIrKSBbOBkYAfHCt7bt1xPh9QI5WZd5CM-og-m9lPbBSzGurFNs1vsgioDKOspgk27GGwhzHEMzec2R5uviVgDdMnzQKnE4Y4cvUSdsC1qY8W7LJfRHN9J6A537xyx_AHCALxxWrRy0Z-dVwjvTuLszFdAN9LiRFdrj6Xu_fToBPttlAzMkWFEoBBMsY8u2TKl-gWleyQ9V2nRlE25ZG18gURbmCIaiOhDa6hr07BquDZmwfWxrG0sa8TR_21oWhLPxfFbzZst2ZM9OqwWMzTE-cXznm2_7ZQZrvq3eGxiuOHNZykXdFaSM98iNSBtbJFiz4-l51ZrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-QX-Ny8Q1MzDkBDOYRFzRISbD8O8U8KlkOtoE28qzJmP4ZkAAnLIdfhByoXs68GX7xQ93vDiNQ82umWNrjJPa9LlohaZiSnTFrqOh8CJbTBmqqnMs5yZBlaYDc1aXt7tBlmOBqvxYocIkSGc8DL7RKg0r0NOq2RtQ_Nu1jDck5TIp3sfQ-0pn8Zof3uW4gJDG8c_JfxxYmzMh2EmkSRnttDPJqHuYmJxjtAeKAq1ID07my7qIFFexRsWooFNosfWCxBw9GdacVQy7FX5JJogYfpFFe8BqOaEO9MXD81SoN-v-PTXGXCHQRc83Pw_ZtLBmD8mFd1Yr6C1mARs1lxPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GN-Ju2gLStT-BHr3xE6n4BzVSjFTB_Ep9XI-a-Okf9QPz85YWApp1UsOetM4YyJNEK-KKgvX7Sah6UO61HpVGc9bu7cV4FU-stRhI76i1t-Qn52kbQcKMElUxaBPmMoaj1ZMdTuuoBRWzhQq5KLwZT3twlt-LV1wZrcpcPwCMtWf2gq2phooJFKqh5uxkdUOoxubFonNNK9t1kn-8CMnOgUDyQopiFw7fhXMmfvkXgh9GDxUVEtQkJitP-Duaf7syPQUw-YSzH6MgS_zGikgzIYrHGaW_5ziv0MT_YOBSPl-aPnM1UpqdWXcRjc1gwYjWAPvVl50zFKjB4xSMQbCRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDea2Vv3yD9fsi1Zmhve1NxCGwsOURT7KDUXTInji0duH95RtbEKMxBnNHsKDrTQqeWo2aGAV_HjXi6obYEKC_YdkgTAVll99vP7BiqPDA33zlpfTrfka2am3V808_DwtTNfCm6RVPEostTdgVEV_aueE2NUGP1wbxMZHSb1EFX-KpB4kpzxtouGrhaFi-ZtuLK8X-8-bLCNKJIq6bliohaFYJsWZlepLS3W8FqRhwzELafU19V9CshXrYX_A9aIrAL7IG3DkUqirH23LlTnFiFxxO5YPNSenFU7Me3-dv5NmprW5nNlTDiKhRkzUDReukMLfIA6qbtdiowfj4FM8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktJ6yviILcCD8Fk3WKDtgm_w2E9-rp8_exSrM4i6cBiv8r8uIt_9Ey90VFHx7UeUuBb9wL1Hkqmouy8FKdVHG06lJjft92TY_QGGoXM6y2ngf12pVw2JUEL5sjH4J13Q3uISK1Wgzrmq9RA3eCZi84_eLSro3BdRNCISl_wXouivc_WO8bng9X8Rsihimc6q4xKonAdcH8rCaFF0E0qXsXVg0Vm837VwSfouGHwskcm5xK2uh_DsGIFFOLTcxU4i4puiozM_wqEulBPAn46QUZDN2gU9SAHibGTGGVD_52coaB8s-CT9TdVy2A99LCzjk6W--khleeR7qSis9zXqtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViADKPMpDqySh7Tm_W5z5wPRtd_sCvWiHfJ1wmgSFx2C0c5_cWuXU8cO_W_eFiDkG5oYZo4ovny_R6LIpP1JOKBF7OLclvXpv8up6h0Q4-v8Q3FRBqs1-HvFuWPyci0dsDvoZXA0UKHpHpkISbTAZJmIScWtOV60j_faUuYOG17oCGSVc9Kq6xGw4D6FePwWK-YylSzvTv8xxDSBgH8MSeJ3wCoGz11Ttbtns2OBo_OqY92yl5vnpMCrKECTO81SbC1LVNkpSPhVQBO21b-EK09_Fbr9Vn2KohwR99qqRvJw1YXgnQi17ZXFNepqfHTdRtEHGVLLgcaj1TRZPbxmnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8Lz3C8ANGzKRWyk0lMS6lUiO-ahDPaZQHlMnBaTun4sRKTzujaOIyy2kD8VrpOgs9Spov6oaNBJr786gcB4QlbAQJuotLqtFX58lehgEz_f-J5qCFV47QeuZhix05bIJaDaEZmiYEgJK0d_qPf__QluhAI7rH51A1yQsXWinUr2_SwJlXO0RtxDwt4uuZdjbCyjYGicUDwzSADcodMEFd5wog8bYr4-u9moN8QAHS-ZIiHcGN9-Ky_iwH1-gJZbCywae-d7wqVFEE6lVjuIk32CFuQcOy4S7gNZ9szQvlK86itU9kZM0KyHPvtjIuSek2bF7xgiczG44vZQo8JmaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhVgSoYbpPouKPj3pYrxB286yvmEhmuJm-pCsINne8ecSZlPJ_cZZ7E3APuGwHLb6tvV6z3qk1ZZ1quiD0fpLiwl-8qyu9XuMYkPc8UMuRItuC9FCq32G4GhhO6FvTK2pkZzV91pAH0fqGYJG45iH_5O7dqfS7Ow4VZYmd7Lp19SGFroCJOfh7hoOLyZsDtVWSEoah4u55TV4eEd28Pr6BUZVKb-uxK09qr1Ff7ZcRoWHoBC3Ad0LvLEAHyzNRgkP9B1zlNF-w0SrZ7WeHdI5PN_V-GjbmZtGH1rWlOnA6bx4E0z14WQOzsz-O8OEVk-5G14f4rCdkdV1DqXFw4Bnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmZEH92HKt5uDqtoxRExO_VtIzKUNpG2zq8O-6jryzjynQca43PDfZ9F1DhgfRNcDPLeDlDqfa8iWkIDodT7HuK9Gqm2A49uOH_CDTUPI3ZBZfAJpb2tuPoZBnQnie2IHhzUH6xKU_B5FO48R1x_y67aBj92DF66A6f-TPKB-O6SNsSv77-jfAgAtdC922dHkSGO1IxC9wkrog5XX17dwNZPw3KLpNhXRtLWkWaW0QJ2MksqUvGg5iPk5lXq9MFU8N5iFppw6zpCbDcJ-petYsVC2phA5Znso1FHTMVyfGxETu5-AqfQF-XoHaPPO1Ad7KLXVjqLTy3CPCBpVg0EDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOD9xPNgLtYgeE90Sg7LJgS2WnVGfGBCtvKIIb2zenE1i-Vr8ANj9EvZA8Lk4i96TLLOJIZ2vCg2a_7lPzr-LakqnZD3B24jFy9sOFZzkXHyiOIZyU4u0GOuM0gvmgx8o5za9OLftBCHxBiSv55E5rJNJ9w_Wd9n5-3KeG8w4m211KL5Zv2Y_2C09AdPa61eSkUVh6SbXz_CFMwY1OucBEycJj3DQm8WGYkhMZqAtVWam66EFQM27SccrY6qTmOqYK4OnOwo0XTmWYNWEjym6xXCnNAIcSaJ0dcX7YPen5AsGT2Qnqj8oRNLPBgqY1gMI-Tx3giP0X2XZtkN8Z3yiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/js3igDcCs8qrc1scZLaa7aK2Bzqp-d5gJLLs09rJ7OCDdAfh1W0C3sfWEQeT3uTk0K-DkpjbsH6SUMNM2N9d-fADonaWF1mQkU8IYi3gK_BxbdECUm77-n7Uio_AlggiI5YZoH4JyNoavkg7UqOIveF7BzacictiUK5C54u8e5tzqCebTGpSlQKugRvhbSYYD2NLJs8UDz-TGqefPNLFFh28Z-KQ2Wi7qxzbaIicEnpJimNG8TXCZAIQVUUPEOMvs8VK7rF3ykxhLMj_R3xlm2zfp3hMKwKUBBEg0ywFHzYv8QIlujZExrwz6qqcoKvOLKtVLv_jG8lsjqR0KLZCIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOocwjW0OSjKjmvK322DzPZTavpT1LP18NQxyVXzIUDPDa-Dr4cwsKELVP2ogEFOmnecETHiTiQW-KJIvKyhkv2AJ0U7B59OeEpThXpTeMjwdV5VMjmSmgFEIYAfs-gN4_UBX47-rXq5X3nj4hl6IhxtB5Sqv5rfkpVmaNxUiHeVuEeWfthY_E8CUis8VorbiziHI-EHwIC3h4VEd_q084Aj3F9RfZ1tazMSNK89ROUBTTSOnNrzS8YQw178jn761FL4jr5qFRpVKqKelMFy_NQJdvygi10CldbRfo-Q18lmjcklkjsDPpTMZouFOAXlIihHxFGVACAgwCzM16HftQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upP8G03ZwSKrMqJPaeVzn4HEz-tltd6a8BhBXFQQcNUeSQuRdoWsD1nD31hM_X0zVYR_EyfmWqR3w-guGcVaejFUGlFG0k9TTWTc6Hq6CBZcUPzXrmNJK8DZj1MUD35jpftwP8CG18cMJe7LF0-KXlPEOfPlJUOlEzuhkGq7GsGgVo3Hx7MUcpoBIRjoIn1pg90AjYwp6so4hGNochn9xvwxy48HosSEmdaXMW45ljNhPW0ZOaR0w3ypSrxFXaVmbz-5spJP9GN1kz2EdIK3LhaNPOq-laBaqQ1aIGgeokzHdBJ9KynUEb0Bax29FhvddmQpzUddgqHCvADSIxQ3iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxAAL8Y0WwUMwR6CxHQ38ceUmd872JqkDf05EEV32QgcTT-eCGokVA_7IF2-3AMNYqC_5Bsg-jz0_R-oCUJfDmvxF1jDRJsCTqwjWkBbjLm2d-S8nxa2QToQoxuiUNhpKZv9ieb-5P1Qw6dqBZCrkX4PxC70LT_ws8tt1FW7qT1eW81GXiSp9cCRo9spsQibvMskKz0Ogw7-yUrhN4XI4AeISB3H6X6CJP2n18zVigWOuIP17Z_oXm-YZQyYKokU-vnF4LTJ2mC9myMFVBl-cLcYrlkiTXjeAmnbLDEz38Rpb-eJhY0AXThI9OMpIyqltOIb_9CUPQkDOUvrUbw9ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qn9jFjXq_kNRFYRt96N15tZeVINWwowJJOcmGiIE6W7YDIz2v-Fg2Hle9PNBbBgHR9vxqqTXlbfy8mU0MXcWeUx9Oi_T1nG76Gqg8JFzYKfWblQjVhTnxaZJCtb4pl8ozgK9uXmnH472V9UnzRYZz2epU3KlITerDLvx5OU6cGOJycwKqFc9GqB-thGTraVb6jxDwbBJgWz3sx-6EmnlnVstW1i0yJ_2IEwEJngEhZXazmxVwIFTMsY8j7CnSeqAwT--zrH5mioGsz031gwvwtWhHNsXU5r0xIo7nvs7ZHTKWe5WWTqh9NAXVSHgOhRT3OiWuhz7yy3PMbykREXvmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oORAVlFdf70Qor8upfM0YREw10JeVfgYma0fTV_VfpeR-j7TVOkTVrvvixnEtRNT2BvLNNZblOc2vufusuUhDrLb5B2wR-v5cE7IP94Ueen01yDiTSTBxtSjWz8LjqbFQDt3-gORqdhX3MKsDTmqVQMSdCanvfnF72RNH4UsrY8rrNP56hNDKuSmnYcYFBqBMZelhaaAFDAj_LJAilgDwyBh8qBNwYBREJ8B_EHfFRP_y_UDoDiXKui_Kd7UC2a0ddGzRSRJs5wdcoG-1y53M-lhq9CZfcerZQjT-okKEz3rxPiG4TdshMtRUGs8uQpv1_JmVCww33Sif1fcm6ZaVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJ0sYaQKhdr09_Z0dVxPgciVSYLu-WouKWO_i95F1Yq6gLbdAEBrZVRy8IqiHpD5lVy0hZ9oUQx_AdAxnK_7D4N7jmXSssAPxLmmN5hKr_pBwYqQTYTolDst8fS6g1X1M9aATXL9Oe2U5DEYb6rTCnrsI_F6-0o9bGCKa8lYTuefvyvsH5ks9omZBk3Wm2ZNcZWaOGaQ8JmQbzgarb6fawSE5B1Sm_cMWlgqvRVVZhrw_TtMH119uZO85HMU_nkeGzxIwvOERkQ3JxbFUJ6_LVlk3XNliixkMYuRjEcqihq2BEHRtFlhPbNwosrTWkKlQ59ioPwm8Bi3PWvhIVVZIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrrQ8VfgAp72SEf5FbWEB2CHE9HA-gYaO4csZCu2Y7Jtw5j0LA0mllisDSM-UOqhORi23ciVSVcQGjyenWdQrvMSFWc2JNJBRxt1TINAq1StW42AOacxqZAVx6M5Wx_n7moXqu24kNfNnfa41vjOIupDlXMw_2P9iQ64_q1oCjdDh8kfjYRCR0OkKNSdH9fYBefQfFSg-HoUOna0pvoE_CtPgsLbBL4Dy_e3CvjjJ9fwM17Oky6QdfkPMmHma7quUqHmQbbKDIQS0oppqNAP7xQ2CyOVf36w207iCi9NarHw-NbOimB2agKrPaI6gXOMxzbistABj0DbputacbCUOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfQFDHX80f3KfUlFxyI8MBU7A2Tuxmi_ZozAuEhzqNdkJzQy-YofAGlau-mfbqda-SFJGV_yeS2dzEdx1KrTP2jBO2A8z3dfhGCJliOegdDILvumQ1s03V-xnvnsYW8-GUygCQyrWzWulR3ZqyHF_CynZq0iRs2H_ORAvodqsn5bzyf40OOObXjnaZoPyN-KSL3g01V7Mdc3UvWJ-cRhHL1Fk4LbxAH1BA6vhFVz0RhS5BGPg4W-5pxj-cI1LoHTZQt94UpwtCowd7ZDMZgRea2jbqLsciYEnGQdmXQTUkmDSQUsAuutuYgxViBhG8L81mObMEH5qZTqesos4mkDog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
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

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=UhGA5eH5lAiDBNMgmo7Z1hCecVoLe-i4gAL-OHz-3TLJ2J8r5rIhU86HtHcUuETw2VQch7N505hcanurrxv1CBS6HKNROLU4_vbgXzsjuem5fB_SSuo8jY5N-1roFkYK_iQfMFgiY_RRf9dfp1aIBgH31R4EMh3hwTH_yra1jMk90YATavlh_ghemGJpet1pqsI6U_uBMmiQ8sxx7QAqSiDKJXCeBKvgbklPDA2cx2CJocIcentSVykz8-f7SIG6RuuqxBgdTPVXj9itnMPyEnhs2PehK10_fzaoLdAPkO_Wo2CLbU6her7vUGp_Y8ZLg9gZenT3aYg31I_dvSY-tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=UhGA5eH5lAiDBNMgmo7Z1hCecVoLe-i4gAL-OHz-3TLJ2J8r5rIhU86HtHcUuETw2VQch7N505hcanurrxv1CBS6HKNROLU4_vbgXzsjuem5fB_SSuo8jY5N-1roFkYK_iQfMFgiY_RRf9dfp1aIBgH31R4EMh3hwTH_yra1jMk90YATavlh_ghemGJpet1pqsI6U_uBMmiQ8sxx7QAqSiDKJXCeBKvgbklPDA2cx2CJocIcentSVykz8-f7SIG6RuuqxBgdTPVXj9itnMPyEnhs2PehK10_fzaoLdAPkO_Wo2CLbU6her7vUGp_Y8ZLg9gZenT3aYg31I_dvSY-tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنبش شعوبیه یه چیزی توی این مایه‌ها بود
اعراب فاتح، ایرانیان رو تحقیر میکردن،
زنان و دخترهاشون رو توی بازارها می‌فروختن.
می‌زدن توی سرشون و ازشون جزیه می‌گرفتن.
ولی ایرانی‌ها گفتن اصلا ما خودمون از شما مسلمون‌تریم!  و در اسلامگرایی از عربها جلوتریم!
انقلاب اسلامی در هیچ کشوری عربی رخ نداد، در ایران رخ داد!
جمهوری اسلامی توی قانونش نوشته بی‌حجابی ۷۰ ضربه شلاق داره، نه فقط نوشته که اجرا هم میکنه.
هر روز پلمب کافه‌ها و... رو داریم.
هر صبح اعدام داریم، هنوز چند ماه از یک قتل عام نگذشته. اینها اما برای موشک‌های جمهوری اسلامی قر میدن و میرقصن.
البته که مردم ایران آگاه‌ترین مردم جهان نسبت به تاریخ و هویتشون هستن! خیلی!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVlbtZou1n2_GbFw1A3cyay7RFwdtMdz9qYflxOXMS2ZvSAmdp7AHee9ZW60QR9ZWnndydv_k_NSeJ6oeNWJKR5e8h3oEHq26vrh0X7bVYluqdhRGQF70GlyOOVdvq3UdNazUaVU6-LjfVmjwJK2tTnKg1o1gknkkh5bDGvdh8JTaus8ScNgJwPm6zeSGrzfV84rxCdEtWVv3zdjBEYyAOCivPD7TvPgiT-loJ25juI6P6wmpV8Nm0SebM3j3wleSDWM2EQswVqONngFw1T4wfSpOLWHjL-vgFlNtaFZW9h3d4GVR7TQIN4xflEmaIMHl8MwzSAwVVrRpE8HJh_vwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
