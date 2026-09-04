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
<img src="https://cdn4.telesco.pe/file/vG14YVzSrhzBhgPD288OOqm_opVUcqTL3UapPqGaBgh5NwC6Syw3PCAH_-mk9QxfmVPuVSEDje8J6wp9S-FbBdTpE3RPRhQ7vHdrACELP5nEjc0R3Md0d8_9rx6CwLfXbFbIAU2t1gLa8NHveUZaIRgbgc6JiX5OfJv_P9eV1YkdQNavu_eFoiveEcAO9mQMWKfWgNMbEUt8-PGZEhDCnN9zuS8wY4lAVZrMPdGmg_07TpFsOCXlgrClSrJlkgnFSRADp4A8ZTT1LlVcfVY_5WrbeNV09nepB47-3_e6s7NFzSRbvBaFnAdyjsny6N0Pd_P24hH6-xKkprZzMbKswQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 23:13:55</div>
<hr>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=eqwK7ZRqs-vHq7eflBWJ76dO4ECMlIV9CVrB7zryykIi2TibKwSGCnFNtCnVIg4x6k98ek2EhL8Lfh5uPGGd5O8rtZsSo7nY22h-SJONdSYMxSS3AYMeavXBLSsGE57Sav_NxwHR1Tka2dxV8zI0FyW9nckbcrsowxOglzVkeD7xxWuee8jrN86ME-PXNL6NldpRr4ZZ1ytA_SAcnxBWzPy7zM8FJ-GKpGSppLbd2x4DlFmGCK_P1NxPYhAr_oVZ9rs_WnuAURlMGaIfsqPyJZpVgUTbs75Va8kY8FqUkDkAcY_TCq6xVTM7AJdRY39OWaSe6nwkjThah4Af9eAvHAWzO5DisdOYosZLO1wdsAfIyIeH63GdjedAC9Fm6V17lATsf_0wJldGL3rszNmXxmPpXClFxuwypVrVu4c9Qu4NGiXkLqbeoTIc1H5BxpKrYIayyEh4RKw8RqivMqYniopzljaFBdpeSVpXk7Z3vKF3HHEC3wRLz2UE-9JdY5yCE74f_LorG6V-pUlyYSzSqHvohd5zB1sKRafrAaQT52bhjAbsi6LVK5NCHBLpZADBVPDvuLB7uCTJlWY8XVSNDlQUamWZ1Q_xn7m9yrIxpQP8uYXFGS6-LbGYCLTJJQ3cgZPtoHxL22MfWZo5qayqJkSSvFFXYEwTYiEvPyrxF4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=eqwK7ZRqs-vHq7eflBWJ76dO4ECMlIV9CVrB7zryykIi2TibKwSGCnFNtCnVIg4x6k98ek2EhL8Lfh5uPGGd5O8rtZsSo7nY22h-SJONdSYMxSS3AYMeavXBLSsGE57Sav_NxwHR1Tka2dxV8zI0FyW9nckbcrsowxOglzVkeD7xxWuee8jrN86ME-PXNL6NldpRr4ZZ1ytA_SAcnxBWzPy7zM8FJ-GKpGSppLbd2x4DlFmGCK_P1NxPYhAr_oVZ9rs_WnuAURlMGaIfsqPyJZpVgUTbs75Va8kY8FqUkDkAcY_TCq6xVTM7AJdRY39OWaSe6nwkjThah4Af9eAvHAWzO5DisdOYosZLO1wdsAfIyIeH63GdjedAC9Fm6V17lATsf_0wJldGL3rszNmXxmPpXClFxuwypVrVu4c9Qu4NGiXkLqbeoTIc1H5BxpKrYIayyEh4RKw8RqivMqYniopzljaFBdpeSVpXk7Z3vKF3HHEC3wRLz2UE-9JdY5yCE74f_LorG6V-pUlyYSzSqHvohd5zB1sKRafrAaQT52bhjAbsi6LVK5NCHBLpZADBVPDvuLB7uCTJlWY8XVSNDlQUamWZ1Q_xn7m9yrIxpQP8uYXFGS6-LbGYCLTJJQ3cgZPtoHxL22MfWZo5qayqJkSSvFFXYEwTYiEvPyrxF4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=dcjPb75sqIdGPPcvlYvl4FOWgqZhVerrcszwNTEYaFrALw6lOoCRrVoJ8BvaCOYXKDNjhPZNnQGAhNfaGkk24X7Ic153shdDDSuOJ9u7kI_s6YIpqysNjQx8DSg31fSQAqUT6OPbUgpGBz02wFR8mNZul4X9_i4nr0vDbQGsk07pHmW7WSu_vsODw5WewrVM-MuAE4IDnoeepGX5tuQIg7eIMqZwA494rJWmjKSTxzNxdMrD5Egbx0PT3_-a54Lh6uzZE6VsSOLF2885G8hpXFF4CzEEXjL03Up5GCQKpKGrIArBk35mjTYKHlwqubIBPStJOGzoN5p_d8TMKq2G5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=dcjPb75sqIdGPPcvlYvl4FOWgqZhVerrcszwNTEYaFrALw6lOoCRrVoJ8BvaCOYXKDNjhPZNnQGAhNfaGkk24X7Ic153shdDDSuOJ9u7kI_s6YIpqysNjQx8DSg31fSQAqUT6OPbUgpGBz02wFR8mNZul4X9_i4nr0vDbQGsk07pHmW7WSu_vsODw5WewrVM-MuAE4IDnoeepGX5tuQIg7eIMqZwA494rJWmjKSTxzNxdMrD5Egbx0PT3_-a54Lh6uzZE6VsSOLF2885G8hpXFF4CzEEXjL03Up5GCQKpKGrIArBk35mjTYKHlwqubIBPStJOGzoN5p_d8TMKq2G5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqgPO4L5-cWo13NZXBiUQBBxyPePYMKPdxDLbbZToL7P4p9fdeeJQ0yqZ1OBoFguePcF-p2XAEs2wKFdIsl9blOkNYsougYUSTDgAsgsGFTONxPxJCY1krhACm3pE9DtQqTyuBwrL13miq3QMtb2UUVjLHYdaHuBohZZvRETUMvdjS9C6YLv3kOTT8d9XP5d3oj2cSXTonXn2mk7GFUjeiJWeopji4ZIzmPEUhexUiknAq_8qNCAYJjMR8ySeoRtKmhCsAWWb_ye9H04t3sOaGlna9ykZuXkGaifDDriiSgmae-Izv5rqExGkp8MfzAe4CLeTEHfQCGTsD_eOlTNwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=JS-5voReP6HIBhKhH1SSJIiDFVxv_MIJYc27-er5Blq6HSSkFp_ppaIOuPN04vBzw478Nf2DZY8i4tGLndOGK_RzVE5BuzXlBotRzFfuNK0sA8UNBvHTwZytdMo8Nd-YUXlzIdRd68x9IP3nm7jU-im8U-PC-cwAVg3yOG8raIAJAYe8VxtfxIQl1BJw7GAPjk13BAdlKns9s-QLEZn6P3NSxLJqFneLI2QVosQF3_Q2fVRCM7mz4ygMBQxfy7bA594gRs5vMiAoaV0ZGNOD1A6Nu_9tmW3OUO7hJor_M1pzJQzTQIhhj_7F43LgtRzyp2z8UA1gZCLg1jgJmkTodg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=JS-5voReP6HIBhKhH1SSJIiDFVxv_MIJYc27-er5Blq6HSSkFp_ppaIOuPN04vBzw478Nf2DZY8i4tGLndOGK_RzVE5BuzXlBotRzFfuNK0sA8UNBvHTwZytdMo8Nd-YUXlzIdRd68x9IP3nm7jU-im8U-PC-cwAVg3yOG8raIAJAYe8VxtfxIQl1BJw7GAPjk13BAdlKns9s-QLEZn6P3NSxLJqFneLI2QVosQF3_Q2fVRCM7mz4ygMBQxfy7bA594gRs5vMiAoaV0ZGNOD1A6Nu_9tmW3OUO7hJor_M1pzJQzTQIhhj_7F43LgtRzyp2z8UA1gZCLg1jgJmkTodg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=Ed--jvl3Y4vjWbfPL1kKpSZzQzAYU70WVylYs4sKKSYupxxF_0Z8FWeU4iLvRN66GmDf4ZylwLIGoQcI4hE3vv-B95G5BAWIemKhcMS226UZl5uA0fmxGIEyY2ehN63gEMfQyrTGFRpQhE7tjL2J5cQ8LyXzSsewlkht-ERhM2th1qNHQSKJcYAXE6sBYIPij8Jl9u1QWqe-WybViCogdWJHez831MNno9jTyTmcBumktMOpWye4m9E_sTNQPF8bPWG_E-p-jwNqyXakHlM_8S5Lcc_rwMhAO1SS4gB2wtTmT1Ya--PN9l9kxMOlECX3iDM0Awi_3iOXUulqNd018Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=Ed--jvl3Y4vjWbfPL1kKpSZzQzAYU70WVylYs4sKKSYupxxF_0Z8FWeU4iLvRN66GmDf4ZylwLIGoQcI4hE3vv-B95G5BAWIemKhcMS226UZl5uA0fmxGIEyY2ehN63gEMfQyrTGFRpQhE7tjL2J5cQ8LyXzSsewlkht-ERhM2th1qNHQSKJcYAXE6sBYIPij8Jl9u1QWqe-WybViCogdWJHez831MNno9jTyTmcBumktMOpWye4m9E_sTNQPF8bPWG_E-p-jwNqyXakHlM_8S5Lcc_rwMhAO1SS4gB2wtTmT1Ya--PN9l9kxMOlECX3iDM0Awi_3iOXUulqNd018Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XG3f9QOi3hKDDyJvO21Hx7hCCLAMCXCJRS72UU-RndNcIaVcYQgkChldHvKpo4c--VdJE76-vVQEQTlZbGzZA0JTKhU3MC-Pxw_yeQLEY9GUw1XZH96cqZkCi3zkKebnm7mwkTzvh6mIpGTROobJgeGrFkjFoG0ZfGjmRhsYd8k3p1YYf8541ak9Ui5Tf_ElRTyQ4Lq3e7k7m3egzW9iVqRJWie51Acjvjq9s1mFNxAM_kCayTubZzy63e730Bybvw1UbbPAZSAVRW0WnLYtj38vdla8_EqaOxFSDi2tgHOqCG6RVI5nvQk_p8v3RHp9T3ybwF7Zvveb0OqoxJ1TmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZEqPWWiNRlANetar915GXSvcA5DOr5NiSp_TTM851_KqsahyRTJIXvUEjoEUgyGPp8snDIUQg7w3gJ7P-j63LWL3ibcQtPY_EHeN07H-2A9pBXqj2gCKVWPwtHwdp0W-Yp6IjfYRzCIaljae8CLJobgnm3bNXvmQrPsOdlMkL2f8c778-MdE7zcsP6r_yXnrGG1wqbbc-Scn6q5HEbo30GHLO0A-dk_cQmGoKnb14NJTdZ8fVVx_sQo6Klpmdwal4eRPey7u9YhXHIxjdFDAtaZtl9RFtsmuqumFX_gjVB_i1o6peY6juGaL_Y7D-cbi_yHpWee9Eh0VrMHu_UqAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJb_xaXd_XA1jutx0oYBhNG44bUcWHBEx16DFyvdqiRY4Avwg9fqwnhP_c27i2nGS_oxQ_hSLHCkm67IZBrjSuYhaQM1TLqh8Mik0_c1DQJXqvu9BjCocfyXAABt8vkO2upODVa0WgdOZyUmKFRKOR6GygJWQzAVz7mwpjHcR72G0myZIvo2AY7kRgqm9xnJRWnd-bpxBYPzS5U93loF-7Kds_yNSFNqkTfSw6jhZrsfowOxnPLYB4loANz_PLN62s5K6l4qlm9Hne4kVSNfFMU_FNnjx6kl33xGaurLRUWvy-ZBj5l80IPu5pbaxwYA6QwJsAKyt9XPQ8-Dg1PmpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e64AqqYhYloXlssAIW6RNsnkG7U7P6hhCg3nhkolFtIqy2CWaz4M0u2NJbr2FlAQJfNsz3U33CrDNyxAWJ0aW4qIX4ViLgqFcjjPJiP-dlHM1eVfX1TqkRj2BFqCy220lD1_U_8oeA484tVIDuW4S3NfIs7Sxz7MnuN1EzsvbbtZNUq7HlUHBPewe6HVvOo6vdXcbCjR9XzJvlP-0NTB2WrM9TXUzQ1vAv_yjb3Xwkn7Sp0MvrBN4GBUytIdGqwrhFIlDPOD-mYPPphvdNw43iRPYgCAPFRl_k1ppErSXW-rcIwUReJolUJcL6LKr12UB_WPHASJaB7FctSt1iegiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkkUbk8PJ24p4q8n67RQxhVsJwLZ-BQ2ZOIwDSxcxBZohJGJ9HmtBqPjxjPasUCJ6bx-KwvA7OdAoncaIAl3gX-5n6yXwZAtl56eZXQqDfSQmPFIzKIrsKct949u29WjHqIV5Zi9WhXK0iabhpv1iMMzrkLwUREv-UFP8n4mMQnYRHIcU8jzM_Lttc6J3qJf-SHCaZqYRrQHGPEUufaPz7-qaMWuAcXYpU2b6UGpkANSe1wnAL7LaiJeSpFCT85w9PpfLPkGauFyWNmM15EvKYLZQpQ5Jgne8tS1397C5Fnd6vmhJsAQJKqXLnkGCj7nazYWNPJ3YuxTOp5KHTjlQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5D2EX_RfuUvWJ1_ChccPPvOEmMYDhCT3sOXUi0Mz5dRdm89WHBYMFFD6Lh-15Hib6za6mDCWOAfcgbp0DkGoH1BnWBKs4UwO-pPc4ET8qH9fwRN3EcOeagiERjnjUct6nE5HDaWxfmmqX9yLQKCd-VIEd4KRFfuwYphDiyyhbYhBIsmOarGsyp4RiLi0Ayl0VvsCDSbyj0cLv17wrjtT5C-lz8YJjmTgHq4yEaovcgclAFaJ5JzfywgxUgDWGS_R7ck4Q4UQvqDSue8_T_h9dUpIkFTdHT9Gubn2HvxYpB9BfsWTKIDTYKUxL_V95GZAFYXqQPXNU8b7HRTFieTMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeemvMPMMWIWyDBUi7nAktagt5iCRKBqTPgsg0YyEWM7HbZWgZbGik9Kc3a9GIBmio_lHNICqCSjeGcNT1zb4seDlOFLgyjIvGFpDRlCwmwWGmyh4u-sa9xq9cEYwylSCJdi5xTAKZKQ18lRW73Apc0SbOnwLL8tDsWbEJgcHrBg4GM5GYUR36fXJny1i0teA2qA-U1HAtISxUZyfSFDD1mpxDlW_BfqZXwCTAA0LOmXIMwZfo8HQt0CSR1Ao9sxqPlh2K9ZJA5ZCzbE5hkvLHDBWeTtulGr5i_39u4CAlB_8o6qDex8I8yWKg71GWBqBZk4XWuydAPmcQ-cLTfpDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZdhZkCNBTA6k1oD5aYLwpDuRF2PWUob1R-m0XUM0V8DJvrWq-HeKi8k3FaufirQMvNqGzWzPmrnnnSZNLcQ7VHqSn9AeuiJYut9P4LJBrJ8o1NRMkIOD3g4NibvcGz-u5DbOBu5CZIk_iaGtxizBubRZ2ot3-0hs4I-180oGLG1bnY1VCCT-uG7OnJ31SmEE7NW12uTiQDzD2xFnR57NgqkE7f2eYtU2DqFCSX3DIRsckYmUnh2jnGH-1rYwya93TSUS0HsJCnno8CNwSM4f4l7-U17f490dwbm9MV-19JTPC27IBL5ev2S_0UMVKQ9kcuQ6WZcgUwJg6BndXGSFag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FuYrJ6cQZ3FM-Hdgrh6uLn8bHMzavtkrVB2JBViAn6A4Ei26PK-IILBdEOn2W88E2GyCb_9gZ-3L7BcOE5k2fY7Qi-1vZKU32a1H2FmiQ3QYtZX9eldBLjOZkHDulag5FauyBsKQ8P-C3onoOaiKaGMMrVBIkcbLgB2FPIVZqp2_48d2UoNC5YMLR0J5sys9fMxCotxnE0GFSKxpPCXgp9zCXoDy_zqK_cSTV2haZ-UzWLUqsbhafTIQfomA-Y4UzYDoYQI7-jVPhsGxQQXFPRf-by7ygsyeiEaKyuipX0-DG6UdJn4_cK8ePynOFJch1tTeZXOs9U1yW4Rs0ft6Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/awpJ5prG1Lgiks_aXG8OZJEpu6HUbPf9yLnQhrcxf5CvUoMj6rOLXm1A94h0WnyMvb5ps-uj8pN2tqNa9cQtdDTu4m6nhoWS713PiBmku5zALlIosa-RsPXAMmOwPqsuQiLE6OT0Y19M9ZZVSDf19oZyEMtM0C4DfhSH02k4vWEgonKsS9jwNlzG9Z7PaKHCtTIVWqrwOw8Zl3RnU91e014L-MGWr9HE9iEsK6KXFfWgNnwQxTaI_obL-_Xs-ny5yoC8sjzSrZn06jWKn_pHR1orv5XtrYe_cYqZnJihMdsSm0pKgo_DrHaQqva0cDqUgdXx_caRLr-3Ibk1JQkoTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=dp3uuY_kAGFUhCu8nvSGpky9eHlfGeNU7z4TsHf3tPMNHWf5IujXZf869cDcCcA1I7feBEHcov4qMDdUeXv3WcB3rdCxMejfm5kOfGwhi3CZhuLjKFbsPZ_BA2pvswrnwLFhpjlZuJJ_v0WbJL0MdH55iQSgOp1Ul0iCavSNS-3hMXfQe6jfP-7hi-KHYzU6Bx-Zi2lT38avb_urrpoW1N2dxa1jHpAvpyiil_ua4KYZ-abPsqkrZBXu5ECwMD1Gh_qAWfJ4UFNOLzyhL0xAV1LJtf9Jvh54-X4iE1mwVctfSdeCi_zfwxDi9oM2eElqUNc5OFTCq8G7r-4mu0NXaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=dp3uuY_kAGFUhCu8nvSGpky9eHlfGeNU7z4TsHf3tPMNHWf5IujXZf869cDcCcA1I7feBEHcov4qMDdUeXv3WcB3rdCxMejfm5kOfGwhi3CZhuLjKFbsPZ_BA2pvswrnwLFhpjlZuJJ_v0WbJL0MdH55iQSgOp1Ul0iCavSNS-3hMXfQe6jfP-7hi-KHYzU6Bx-Zi2lT38avb_urrpoW1N2dxa1jHpAvpyiil_ua4KYZ-abPsqkrZBXu5ECwMD1Gh_qAWfJ4UFNOLzyhL0xAV1LJtf9Jvh54-X4iE1mwVctfSdeCi_zfwxDi9oM2eElqUNc5OFTCq8G7r-4mu0NXaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzUn5vZJBiq8LEooKtMkdOZiZfBwQSzT-mcigSow1j9zN_yI9hnj2xoDWCmQqpWFEjrks8O0GSy1SgVLpsrsjD1-Smw8OnGbn7EZ7ZWfBGOHlpczkIgtbXz9sY5jBb4xbzpHyhIX19pWGGZq5eYrMAYYE0tGtfRx8CRkTJXKS4WDI_cfIPyFjg3yPPmZXBynNhb9i9LLEk2QbRqOcym-nrAVVxoCGS91KQK1KL8QuBnvLwvrPad7a7DrvNSbCUna2mopmaLVYlru6SjukhFzKScyGp7huJTUWdRJOaJR8167hMqxjq8iwcPfaf0A2Z8xqBptddMrh7qmtLwzGsNwXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fG9i4EsGSBl6q7ngYq8CZP8S4owGDIDt3t5J1ndKSavS5xAihcRx-QVyx6eEs5tk5j8YtEYfgk5qjvbBVEKpJlDwSulPRTfrwfqj6GYuMiSNr5ki82vo6REU7b3HlaxcWyhDbcYgFkKfnqXLhMZ3Yjv4_yq9N9GEanMnBYCGqbKcd9uGY2fu0XRLVS3Q-Muk2VLcl-b3OUWdTzfQWSItCNv2RBsqxkJUih2_TtAs81ss27r1IO3kDrT7afL_8RMxJJIZhUHIT-OGT7NXK_PzbuY_oY3s10qTeQNMKCYIK8i_l4BlIYJ1mPxmCrojHynp2eg2HauVe02JekfXHrMkKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=Rv5ULHNDFxg-N8OsL9MFRdzWW5fy5_k4XGYqDRMjpTH0tdFnsDngnrj7-a73U34pkVrs0Zti1eutaLNxmjQU8VkxEptvXKHDyjAcc3W58y87s75QogFSQ0phBUuvZ6FqwkVA4MeuURJx8xw71zcEnqbQzeO6QgDpK7CWaqMeVd5DEJk1wprfR5mxbpv_jrcd08t9r-ejj_l6dDvUBpeBLDt8Z-DKtGu5P1ZV24d9mIXdk-JFho5Z9SkDBFA1GUY57scvkch5cZrlq4CF4-JsgRHWmQ_p4O_ekqGslDHAOKqkoaMjADLLejZuV5ug8r_GSriywMNMU4be-ZYIeV82zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=Rv5ULHNDFxg-N8OsL9MFRdzWW5fy5_k4XGYqDRMjpTH0tdFnsDngnrj7-a73U34pkVrs0Zti1eutaLNxmjQU8VkxEptvXKHDyjAcc3W58y87s75QogFSQ0phBUuvZ6FqwkVA4MeuURJx8xw71zcEnqbQzeO6QgDpK7CWaqMeVd5DEJk1wprfR5mxbpv_jrcd08t9r-ejj_l6dDvUBpeBLDt8Z-DKtGu5P1ZV24d9mIXdk-JFho5Z9SkDBFA1GUY57scvkch5cZrlq4CF4-JsgRHWmQ_p4O_ekqGslDHAOKqkoaMjADLLejZuV5ug8r_GSriywMNMU4be-ZYIeV82zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=dpxay8DJkQk6nZ57zqNtXE8nbH71eJHQwFgBIBJxDRwyjIlavxtzSPLRyq8qd7uz7iVhzKfOAcnupIZq4RAGGV5i83JS92LBUF-4RgOAEn6hNhZpwv2INtNIqDYzgwXLlwRNub0O3ARq-1Ew2UifPvSmqJYQfr59IocTMac0ykx7dekMFhzbWHr4y7jI7-vU2a_uX7kaNxF3RbXAXsldYu1FKkNBx0Mf5kpQWL2Hz1chjfYi967EpkLX21I0EvcY5HMaakqxDth4OTlXOhqU4RpsN9roEvttwLbdhUPXm8XE52n7I38dIMzSDxaLB5uVbqErZ1VguigELGqFjYxoWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=dpxay8DJkQk6nZ57zqNtXE8nbH71eJHQwFgBIBJxDRwyjIlavxtzSPLRyq8qd7uz7iVhzKfOAcnupIZq4RAGGV5i83JS92LBUF-4RgOAEn6hNhZpwv2INtNIqDYzgwXLlwRNub0O3ARq-1Ew2UifPvSmqJYQfr59IocTMac0ykx7dekMFhzbWHr4y7jI7-vU2a_uX7kaNxF3RbXAXsldYu1FKkNBx0Mf5kpQWL2Hz1chjfYi967EpkLX21I0EvcY5HMaakqxDth4OTlXOhqU4RpsN9roEvttwLbdhUPXm8XE52n7I38dIMzSDxaLB5uVbqErZ1VguigELGqFjYxoWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krTZVhaKt51_674Icio1frtyDBHCtZX-VGzHSm1_GSdBEXr2oQg5NW2chjdTF80YCxJ209FZvKJguf_LfkTmpEbwL6IiyR3u4ZtZgiNJ_oW1sfpuvrkb4WohZ_4T8QzNbeBmspL6_Rv4HdbU4acTiHQLY7rIaQ1fsYs_onGE-WWwcZrLoYHVmZygGGrC9H5iR7JaEe0LDeznlOUKYEtBHkhlxwCuF8jh8NjDitL93KuPEDvLLqdgzSmJzQam99nkczCILov8tIsQckk_qR0MbCORkvtOeogj53niD7jd3yqN6C1jUnoN5OtEG5YdgJAX3G-rfs-hfBxNNXkhcLVA8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUk92Bw8HBslQMj0X3Aci1oiM7yyCBhT_Ui_ly-8VHBd_67mWqhNSlfNG14gIZf75--WhEeUpdxHTpU7QbQqwztSaM8gbrDTcPimPFeh9sTgW031Di07GA55xosT3M9QWa51y-5w8VUDCqJ13doKchwKtl-SUc3BgQxgA8qc3XSPcM6TnQwgCmWoh09zUDjCq80c0pRzk_d-EDfSrFVsHSlB-Z13VMhU4W3SO59tt_ppEgUrAa5j8OKf6h959iVg_8F9TDoeMMrHTbF_fTCyLMXavvG94EBUiZTk2mya68PdCnHBOoFH7M2fuyoSeN5gavbcW30uEk9WhBDMsq9mpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhVG1xmiyQR3vAa5dR1sdzvsmT2ua9UK6R9AFRpR5_vzRxCeP0-AhM74RZg7WA05JeGrm4S03xlVq4x-g78FQxBqPXmVAhvOobeKp_aHh4VVZE3Q6wdK57BLIvHpeuE3xKEUuRBnXnrb0dikKLKxqjagWKWr9StAQJ7i4MbyA0zStoL-pnsTXLOpIcoDzeCaKPtAKsBXPHvHDegKYCBRkvo4iFFZwm-Ru-I_J8_j5W4z3xMjIaATJW2xaelzCVM1AoPN-7m_ANnfWfI01lc-HnO8qJz3ZPPrSmYlrU_miON3LmVvBZGUitqqLnsWr4vh5LtR6EXIFjaau4gZpsPWmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYj2x-Hp3Ja52QeHYs9dLqAosstQ0CyRRn1ZWCh_1DFGvekX3kDT4hkF_z1ZoKWrzpVSafcvuoFSqnl0KjGyet0wQ08XwTuqAewQqfnK4Ni3P3sls45O_Al36DP98OPpD5poargDgQue_4x4PsRsqpzHP-sOh9GT98KM6z-WchgBip9a1eZ5V7wyNXfg1f0J-CDQI1ChhkAf5D61C2bBR5HEk2f3Hn3CRb3UxX45ZoUuaFib7c7YpvknIg0Ddrb1NJ-rt8K7n_wfIF38j1thw-yJSje1hHJTOk8eM-EBpsTJMD4N614kmqbPlaQaaIbSXBgazz05ah6_fsdemmQ86A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hp48qHqcuyTxT5PlX2miitOJjgRNm_5PotmCApTSrNvoRJaGJnJiIhGEzvEp0e1PWDkknYmK0gBgL6EzZ1_Zfo6CQxmdmmNY1USAxFKYhIpgIbHawTTqgl635M5YJAIzyJE3gPd5cIOUegbmLuUIb0UKZ03RUztdqGkprjS02isHcwKpt0lSEbBHHykWs5q2GdI9MlSwxJrvxKyzWGvuqAFs3DixJAe_E1PX25Aky-xGxLfXGAsuiUB30pST8cADd2TVwnQQYGeKMNZqmnDlSQH5LerdzuaujaP917Pe4Or4e2s3-1JsMeSwJwdg6Pr6O3-PeETFE_xVilqSKJa13Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKC9KVRrd_icvs_pon4fjK809q-F8J_D0FQp_CJbAJmDMuRLZHdqV3GtypOr-INIpy747sM6cdwqYCUgsl_bM8vP217LoaeN316aU02wkBJ2xVIY9RDkVZe827HK6943-s1nnAsx-_nId75jXzrVtSGcN7jo42DvFZd4rAVtbZ21jjrlQwb3eXJsF0KSIBv6Nv8b9B0NDuN4YAlR6wiacvyZLFIBWYBor_tpWFEmRkc_a3478RoDC-PKxG_EBb-822D5Q0zAJdmrl_WgtW_O085TriRJPtPP0kTwoy4Mu4MavlV3AEIJ_smgb3rptnoZ7OaEeQlgL8EDSyhh8HJhIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TclvxoCIjGqruIJTaF4mDmy2rC-ZC5wegjLdtXdXN_lksA8p7_Y6TPfLbx-RFj2z0aux8mTvyL7YIHbfKK79-YDzVsOo7QF-ZjLFFHJY48vNbvDvNBfgnE0Cc-HwedkrggSP3zDZFbSPgiGm2G70WYMMcvBkjbQ-HuZd4M6taYbr_1j5-UgTO0rgmSaGqKqgd7jdFJ9D1sgucGejBnZvGe7kxIQiAluF0YuVV3DaDPyxSQfJRVj0nbHKebKK2SMlOdwLdDTV_CpqOEhv_iAI6-gm2Dx4CUNWXtFl6IYQA9c_y5kteU_DZSZBAZ6IOIRtIW0nhtJaqSyphu27Vm2p8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlgtyZxN6quJ-MPKjG5axwBwqgTbOhNhZ1eU8EE655eOxMFKFxMIP_7UTIb2_hW-d0ETLUfELsfw1yHo5sqEB5I1SyYfpM33K7FPY28sbWnHJDXKEd3i2vYKAJOFbbnv9DEPjbuVdQu9IOoWfManGBFNqJCA3gZCJLFHkXTR8t0rR2soRxRFYzsDgHhr5Qx7THDwrQmIfkbCjGdXPJDkvmNdBn1UU4oY2hucMEfwmmaIdd4ZXL1gZq4KSqDTyRoSBqoEL4aFz-4JZljdyp1ywH3UA3B2GnumqLwh7d2iZzUiOcDw3nFHXFLP5_2V0UGc435sHcBpev6MitY6AxyO2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=CqbxWIiTYld_BnTyVot8W-XcjmAMcxBCPfbrnuRSre6L46XfEuTp9hX-ee7Cp9kVU2s2cE_8F884_bJX97qucOnxXlo18KuyMv6ydbqi-rojjGQoGX9yJcjQtVWMC1XlQQZYQAQd5uMycJCpxEkemWQ4S0UpMmwinf6tUVuq2h1PGhW2fwT_vd-4aIywdINpYUK-Da_LIS2FGdDL8ksXP9ry0rWbOQI_2w1bqoK23d1rGtA2CK-LohjSJZL5OThC7tL1tKdBzU-WIkjaVACYenle28g7Scn1keq_Qvg2YVg7f8dDyrKl-axfNx8lVXt2a1frLEzzw71YaTkT0fT_pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=CqbxWIiTYld_BnTyVot8W-XcjmAMcxBCPfbrnuRSre6L46XfEuTp9hX-ee7Cp9kVU2s2cE_8F884_bJX97qucOnxXlo18KuyMv6ydbqi-rojjGQoGX9yJcjQtVWMC1XlQQZYQAQd5uMycJCpxEkemWQ4S0UpMmwinf6tUVuq2h1PGhW2fwT_vd-4aIywdINpYUK-Da_LIS2FGdDL8ksXP9ry0rWbOQI_2w1bqoK23d1rGtA2CK-LohjSJZL5OThC7tL1tKdBzU-WIkjaVACYenle28g7Scn1keq_Qvg2YVg7f8dDyrKl-axfNx8lVXt2a1frLEzzw71YaTkT0fT_pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NK4I02wfcuaMXvMuyrNng7YDcsWHfTwZjb3rnvyqaKyO3AsU7gww43OORszfEdiiHGGrXRB0ImP3wPuGcSpManjgjAYFsC4a7bN2oUFalHCcHUrpktEbl2VX3VFRDbkr5M8y6RXbbWe-QHeLRKVjSNDklnGtGIzCc75AC2USyQHgfgxfbwI8GVbF4zHDJAeBBD6XnBphFUm3N0tQ-OD7OhqaHiN3FI02wtDI2mjfOQjVBFyG10pDNSj1FkrNtKuSZpRPYhg9RHUF_kRR5V1NPr3Y_TdF_OxVIRYqvIwTvHfSsQVMr5FSaI9V1aXiI_7KXzUOsoodGxXr8zJ3Br5FtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=pMsfnl0iwdb0IqkRMxEyASXuWGhYTFlyWF-hDzVxEp70RH6haco9CSCzFQT1LXaV_gXFpwYoklxD56INZ-jmaJs6YOEjznja_hpEdOYdofEPqSnnJk-2AhhxvCzuwf01_538lshJJmQH79mDtE-ZdtodPEmc7N5sIaWvm3a8c5THOMOkoosV3IkpFErAJTJSLER5XrvBvyK8iEYY5ensF1d_Hvkh85jxcTGSt186Z7ecmA4DuiGwPnlzWAPO4Ght2un8Mf-CrgAfMoYSdTk5msb3_aPdPv_-nNRY5ig8knM5hAF0n9S1dFBK72LBVuqpGQ2oXWIVNu5HNt9xwe4yTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=pMsfnl0iwdb0IqkRMxEyASXuWGhYTFlyWF-hDzVxEp70RH6haco9CSCzFQT1LXaV_gXFpwYoklxD56INZ-jmaJs6YOEjznja_hpEdOYdofEPqSnnJk-2AhhxvCzuwf01_538lshJJmQH79mDtE-ZdtodPEmc7N5sIaWvm3a8c5THOMOkoosV3IkpFErAJTJSLER5XrvBvyK8iEYY5ensF1d_Hvkh85jxcTGSt186Z7ecmA4DuiGwPnlzWAPO4Ght2un8Mf-CrgAfMoYSdTk5msb3_aPdPv_-nNRY5ig8knM5hAF0n9S1dFBK72LBVuqpGQ2oXWIVNu5HNt9xwe4yTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=jmUNaAZX3h_gKItuRm1BCQsirzUsKlOEs_XDuuOevQ-ftcuXV8l-sK19yYeJytlNPC8hphTXNDyijULekHxt32HymAmKQ5cHPufFQudMm22DRNkDURv1zCWKnMgTfRNTiqrI2TfiREj-DLFVstGCK65hN3Fot1fvn7EltF81UVi99G6WXPXbF4mme6iKfnenzCEWnrFpLynRb76O0zne_j0vfxUZ8X5nAvyQHP9FC-BYw_HaevEOH-5Lwctig1rGCQY2wS9iPPqQ3aNnd4-leExHvJBOq_F_F5q8fLlYwdqYHjo-BLJxrc-ntCHPj8JdNXjaolLsxKdGlWuZizJvVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=jmUNaAZX3h_gKItuRm1BCQsirzUsKlOEs_XDuuOevQ-ftcuXV8l-sK19yYeJytlNPC8hphTXNDyijULekHxt32HymAmKQ5cHPufFQudMm22DRNkDURv1zCWKnMgTfRNTiqrI2TfiREj-DLFVstGCK65hN3Fot1fvn7EltF81UVi99G6WXPXbF4mme6iKfnenzCEWnrFpLynRb76O0zne_j0vfxUZ8X5nAvyQHP9FC-BYw_HaevEOH-5Lwctig1rGCQY2wS9iPPqQ3aNnd4-leExHvJBOq_F_F5q8fLlYwdqYHjo-BLJxrc-ntCHPj8JdNXjaolLsxKdGlWuZizJvVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGCpREQ4cYtVPBnruVE8hcxtekW82_Li3lmo3TbDpdD-B4nFsXgCNrjKVhbWWAbmM4Wa6HmmsrTkTEikzKwPExVbU69FSGqIpNGYwx4hKJ3My-li3JhE_fqqLuMOC2YZ3dYQEGV0JsKF82q1jgP1xRebcCiWkb8FzW4SKK9ydmN-BWmFvtemTG2JTlusXAmNnTOPN1MZeWPQCQjp45izs0Aw2dl_66BF_LAelXGNLc0ikK0vTh37w36CS73liQKFHkvet9Js7mIR70fbsH0WIvhUMCRzLYmq1yPO-ho6hrx_HROfRzsIq0exSiBz3GjSD3i7RxfnGazwlbK5NJYfeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLOmt1Hpi6wkm_aqKzCKNAvrQPsCsK-yty1V5PAG6x_4ofms4QcU1IN2MoOA3v-lCPKvJv4cDn5trMZukZT7p7zoeCE438zLYALGUXUarjLJdjmEtFJPwc_acS6MieDxWBWgtkAvMafNr8QA-5nGm8lwVGqDn5XLSkLM6amLG4GPvTdWmhbKieSIzr3c4QD-mLn3pd_nUIR5-nKDrqPJrHbAYQ5kdbFJDAF0DdBhJAKigAnLAuvnirlFxmPJ1z3DSIFN9U-mqQngdq-AnrbyfmOmAP_2GQXWBwPHIthGd9l_zdpcp1TuyvRFv9sV-KGOyr5Qg3Y0_9XO7eGAjpAXww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=YKGseNRPXVPqP47ZgsUkSqK9VUJbcnICRtWFsbTvtU7SKP2xifqBleqVNtvt2K1peY6MmVtLArMvVgWDK7Cd4RcP14zBtYqHw2emME8DGPIIKcuQsPKa1zpiDXBpwHOFG_hOjfFyR-iqWINt5eHkV1c4rvZgv7DH3PzUwM4uGMEwqVNbqwUanYK127Hy4da4zHHRz7E97WdKDKnSwuc-3H7kHbsCBgfX78fAi--gFfjqvkTkr59bZx_PrztXMRpYNY7KUPLc81qXOOOBUolQ8xDFGh621wpkB6xJ_D9N08_F6XEPY5rnQlDM4NuNiDHYLlHvis_gdFpro69BGhmgUKZzXwuy4PdQA0eAMWxSjZuZYCTzUaKLqyjunnNjOe6I48R377VB51OR2suK69V3Nm2om9z74QxyfXhQqdkS3_928U2Vxt3Bemv-DtlMkk1C2izkqCmSpCp5r2XQnFUgguc4lVKFX83_LrHDaRCWxzPIvmUpTsWh_EKQ9hCzLud-MlorOgHOpiMnOJyj4bWfpb3vrcts_tyja_KeoHt8vFp9VqevT53AWSXaMLPPEVdPaNPU2VSE1xDKshTG24L0PIzQl0Q_MkE49uo5h7m7_hUcraVF4R8tnhc_DhQN6zql_fPjt_OAInzoZ31t5_7ed2KyuZdP3jma4Zqc7q-BuPU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=YKGseNRPXVPqP47ZgsUkSqK9VUJbcnICRtWFsbTvtU7SKP2xifqBleqVNtvt2K1peY6MmVtLArMvVgWDK7Cd4RcP14zBtYqHw2emME8DGPIIKcuQsPKa1zpiDXBpwHOFG_hOjfFyR-iqWINt5eHkV1c4rvZgv7DH3PzUwM4uGMEwqVNbqwUanYK127Hy4da4zHHRz7E97WdKDKnSwuc-3H7kHbsCBgfX78fAi--gFfjqvkTkr59bZx_PrztXMRpYNY7KUPLc81qXOOOBUolQ8xDFGh621wpkB6xJ_D9N08_F6XEPY5rnQlDM4NuNiDHYLlHvis_gdFpro69BGhmgUKZzXwuy4PdQA0eAMWxSjZuZYCTzUaKLqyjunnNjOe6I48R377VB51OR2suK69V3Nm2om9z74QxyfXhQqdkS3_928U2Vxt3Bemv-DtlMkk1C2izkqCmSpCp5r2XQnFUgguc4lVKFX83_LrHDaRCWxzPIvmUpTsWh_EKQ9hCzLud-MlorOgHOpiMnOJyj4bWfpb3vrcts_tyja_KeoHt8vFp9VqevT53AWSXaMLPPEVdPaNPU2VSE1xDKshTG24L0PIzQl0Q_MkE49uo5h7m7_hUcraVF4R8tnhc_DhQN6zql_fPjt_OAInzoZ31t5_7ed2KyuZdP3jma4Zqc7q-BuPU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMjh7RBgNW6iALRTNWSJfYT1zLPohAKbRfaU9Ds1d5oovvJHU4yBd0XxqHzs8AGtg_DgZnghMH9wau5hsj0Uyub2m-cn1_yav87cl_PBmpQfUvwMYpgmJMqgn8bbIA6GKtK92U2GLVl0cuaSs2dQIjKHO7FibNoK0BoUVu_MCawNuDsxgCe9bCvkB7TRbWAK4O_1EsogIp8Fuf_kZb9poWYTMYmqb20CIGeaZmpRHBXEyuPq3hAomo-580sizIgqd-0HJO_KxFqNQCapLe5sxUYhaThXyLI9SyoskQW__9DojIq3ts6TG48bWATjz505adpz8W9tCPaDUETA46fDHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=oaYsUqxqXNdcTOVfxWTe7vKcUweQbgKBlTXncJABAnxtbu9BTDUtONTMfe6ZVTLwBgYlJlxAymJqTE4WHMN3lyhE0ClWVZ4wG2Sd7KfhwAiGjOoUgbsFK9OyNHNJTDO78XRisGXeElOLyeKf0yowYEMXZie8A1TWnxuClnxc3EDTHJt9PfhPfIGe3i5MhqMf3LRmggp0C5IpQ_sNuxQOvG9YrrNr_vRhmBpYetGTT0tqMFdBdclCw5jIfwuH_CXmq2yfT47U5wR5nxJxghUwdXxz5yQBghWJDli09gPny93nvau1MFUTwNr1NpcFFdEezmAgUS66x2m3CkaGgQXxWJExVuYggc0U6lLgYTPITp-oZoE1eY8nSydr4wUFVS1WU_NeyMQ3egekGfkhDa16ZhXq5X6bLqz0Ff5g4d1zUqnU22-5MOBSnZWqwJPRf7IU0obHBQCus4faiIzn0YlrOcD5EQcGGB6I2Y9W8a-mi2pqSLZmGTO4ZeSPPmXjjP-X9LOBFYpMceKrETL-eBqkpUqwUg5Bo7yyoHCfi-yHb_6fcCWlMIEL8SK915P1O0LnShVV5aS_u52zN1qGjOrg85JYENMx3LLM5Dp7yotsY5r7xpc5LFNEKXVxnCYfcanGG3tUurJ2T-TafpmM70I_jOIGB0DY8tagartZuAPYOfE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=oaYsUqxqXNdcTOVfxWTe7vKcUweQbgKBlTXncJABAnxtbu9BTDUtONTMfe6ZVTLwBgYlJlxAymJqTE4WHMN3lyhE0ClWVZ4wG2Sd7KfhwAiGjOoUgbsFK9OyNHNJTDO78XRisGXeElOLyeKf0yowYEMXZie8A1TWnxuClnxc3EDTHJt9PfhPfIGe3i5MhqMf3LRmggp0C5IpQ_sNuxQOvG9YrrNr_vRhmBpYetGTT0tqMFdBdclCw5jIfwuH_CXmq2yfT47U5wR5nxJxghUwdXxz5yQBghWJDli09gPny93nvau1MFUTwNr1NpcFFdEezmAgUS66x2m3CkaGgQXxWJExVuYggc0U6lLgYTPITp-oZoE1eY8nSydr4wUFVS1WU_NeyMQ3egekGfkhDa16ZhXq5X6bLqz0Ff5g4d1zUqnU22-5MOBSnZWqwJPRf7IU0obHBQCus4faiIzn0YlrOcD5EQcGGB6I2Y9W8a-mi2pqSLZmGTO4ZeSPPmXjjP-X9LOBFYpMceKrETL-eBqkpUqwUg5Bo7yyoHCfi-yHb_6fcCWlMIEL8SK915P1O0LnShVV5aS_u52zN1qGjOrg85JYENMx3LLM5Dp7yotsY5r7xpc5LFNEKXVxnCYfcanGG3tUurJ2T-TafpmM70I_jOIGB0DY8tagartZuAPYOfE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4lDoWK3Sh2fQzJ-6r0PHqDglcIuXKlaOMLuzmP88vqZQp-9BbRTvxwdW7sUEYDMmpYlE6Hmb0g9FHW80vcX7Nm5JIR754onf8eP0Tdcv4bizNx65_K7vQGWn7vHtGIhtSakpAHWHXKHu5Hx7-gWaBXvBjTpyy9IJ796Z7r6vfxC7qrL7-IjkGlaN4jp7NUqeQOwo8jgC7Ds1WJ3x3Txz8p8ScMXM5_rs116y6DgoOYUmG9mGcaHnmBDnrXT_TnMq2Rk0TUN5zYIeddbJGhqfgO1dXprzH3v6bdxoK3Vj3A1cLOcdromWy1eYByVHMoOQajpYqKXJcx2kHribDtx4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liuFLSW2yp7xk3lCjGHcVINf-B2SAZiWIZb3O-IauGBfGWvRLaYr64aZai7XK5ZIYE0BNn__E6Wd8_IytqnlSGe-z0aYdFdJIUj9-6eVF1nka_ie5TQbnzJBpkRDlDZf65bI-papVXXcJJzmLFtiPWhm1QV2WxZ76raY-EJNgZrT4-TOpOU77V8Z3-CnYCfSSAGqMGPezTw1aVpBqi4SbcMRLhBNNlIZywb7hvSOflEjJLdcylNuyjdWirm9tw4y_YmCCNw8OF8XoZ5GuVch_qHJ-JN_Lp-EJRxXJYmd2oL4N0hc5hhxsDcKlkjWyQOawtk-1FkcPrzgESPIu9euLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buo7NEdfXpU6ui67eqzBgq2VMne2eRnBPao3T_mB9zV6EuQZNtr9b63WHAw4n1KaZXj7YlK788XPFoWDMbRiKJ1N4qtbc9BX-JIYn_Q-4XTzvxKbwIAoSUPLisB4q2GxkvnVED0Aaq3Rma0MECcqT1xCQ8FtoV7UpHpebx8x-fInc5uO5R56YkvUl7CbnDjQIhA53pARZoH-N7RRMBtZqPh9IMfMwKuQAKVT5A8DVZPMysifnDLcS0KAl22HShAaa38ulr84C1qMVFdWiBCUmRwuHpikAZxA5Q2E29XCLSdq9Kja5l2f6z0tgwt08QgGENVtv9fe1NCFja1oZ0EBSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNtWZaOamUaWbdLIzLqbyOom8xw_LcTctGb4wnqt8mgL5pliXGNZ4jgXSqpL08cEycwVSrJk2ZmkVZb6HYoIg2CL25fGQpv0NO9RrpCctPSxlv3ZUT8gg7kL2ifoGxqTbRJ1RsY-ie-LyErocE3UE2mZYLJTnxFGeuWuPgvkQ7Q4Xqm9WI4LTKgtXXZm_VStz8YoS25wKaSDK7rMNWPSbjItbJ-m9wxncRmBZIrPr2HTeP7BBvLBl9cBV6yW6FHZ0EVWYPiGz9Up9Sdwvu9bJahjgMja4wMjD_gLDR2aUQvfT0SiqvwAPrNFRYe-AfNCiJOdAuVHhT-J5mEfU8CBcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjPUBfolVgY8vnDazPDoeSciJ4b6sFyGSEbRsJvHcuV3GDoC-PzLUHur3Mh5pUetCTb_TuE5u9NW8dwASSTqhN4zWRhrWkp6dH3mfMHPh5YsQUmoxYUftVsOnnEl9jqDeDUISc16fB6oGRm7TsKQ2hEp3b4_Wv1lyXP-N7PNLAQ7IWjmJ-ywxfhJQl7Ib0zeKw1_tLBBNxsXBtldpwvX_8NN9UdrjSCqgqKtbO5dp4PWoy6sYxdSSWCCammAyqvCMm6X2pV4Nrpji1o07yZqltsYbnNYvTMRSLGQFZohJxPnkfa7OllOLV3_6yYSpavojEWCL-AwQNRg0cGY6G5y8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3RC5fwzjMWQFB153IAiBoopDOdszKyyymEzkHo5odE18sWAfS7eEbAlWmkMZIoWtYhGeq6xM6M3usq_1S4gxkTzTXh7YgV03m1WtNfuI4QaE40NESf5m67DCCAPZEBgZiXcUce_0eYYvFvSIMuMjZN0zDHT-InGf1T4GwJunaVh2WuIX-2qwgzLYbrUcFTeZi6REFcXlo6dGi9JZ0rpFp1ZHUt_DbkSs5D0qDeERGouKEOEWzB7bxdUFw3cJ7H4Q6aC2v5GUNr8uBxCnZhDFK7pNivtB3RbX5KMeiyp12_faVUYExpa-waNwvpuHuWfrJF6uSlqzKXx5E_Fj4g8Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzVsVUQv0vSsTnrmWiH6krUO20iXsipkJ-4YKXE6Ts6xThz-eZNQtBr6Xhce0MI3lQK7YB2IyjYZPi_4wk0TSY4_6E3T2ugi3sv6eKpS2vo2ZRmK36q3h51eugobt2FfGiD7UWOZMgwWou_YRlLVG8oUvMTgtGzfS_VA-v1hq0uHmWKInjGtyHUNpyVIVpFDVzPg_dLCGAc9-fvc8EFHjVIEh-8KZCv19r3kLJe0hFx1FNnNL884NWp7H3vZpWbjQ_VJwDLvWet4KbdYdCfUMKYva3f3duGwZwOMYCgrJWqNj2HUUO6-v2pxl9tgXjsOI1To9qXKLaOHHc0Jk30-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOECw5gk3ty1E8t5wu4uPKQDT649OSR64m8ldyO8TFSNddtAyUQ_LyO5WyT327bfNd3vpSimrAY9HDhAQh4EnNzaVtE1WSCe6Yg-AevQDjKBdBUBHt-SDU-p8RgHhro99IVVAIglqghS8DCfal44_A_OGxIkMlwk5Uix6kCsiPlmjRVRGbEZMkLXIpuFKEFaBnnuqNFrv8p_3A-FohrZrcMXnPnuUzqkiJJ_2XH7dJLqcohqUi9AN5e1bbJGpxqWDcMvEJcweZ3cNw5gktW9hef6ruK5Ei-R963hv1bo4mGAMq_KydjvvO5brDyv1DWapPbtKCDHqkzMhlahVcmOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZYdi--qqqJZD_BdZVhgQl6j1QaHKMD4q8K5HPr-Jvn6K04cfUU0dqll5d3Vn-nOsI9Vesyxhp5AUdcxuwGCFA_I5XfgT2NauydXHNzciuLTtS9ilyvlnUacCD3ObdGhCm3K7cDDxVhvDcB83OdCL8nKvFWK5fdR9XMeQMBmsD_ah-toyKwYYjAc19Mjur6bz7Ecp14q2I_ChuS76PLCAwhk7EDQKwVqhyaRa2sqwmPOvboB9zZANoVPfiV4Mlg3IeVD1xU_3ZF7WH6DR9VUH5h6X2uatY3Wl1AoqXrjs4AMsBMmmcbMa7oYB_OKqFjVoT-uOp34DriUQMZzTJ57oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tq2fpkf5oeC71cMGXpnRzHBjK9LIMaiqcZ5E4rUrMYN-M94GQ5LjaDQiEeO8Jj1cZjahWowRl_9c2AmC_QNxn2GKIpSCiOO2lLg42tGMCygdZ_AQIPmB9yMQ5Ev8Gt8nYB_IflQEDHIyS4oNh5MIXbJnhN5q0NU8hdKa6H2eFQOaGv77fqJeiKR169EoT9-m5mVE5szYwqRGjqNoROB2rmTf9Hx03ky2b-RjqHQeVqw-g_0NpN7TAReIq2-2tAciBlkAmb3PVzB9mahmOPw2jRtf14UCZvu6pQ1fHi1WAdZlAFBS7X1sAycx1joUGnW6sbx6qDqoZYnf6JVG3j81BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwTru6mst5NajkT5m9gK2KZcn32lTQN-rxSsVLWhkB0kc1SnIV0559qXGvQdfrMZvgiAY5_EZC5ypL41CKKDMYTVxTusRiM6B-WTuDvFf4ZamYcTbkfEc2greY2CgiRZm0Ea0-gn4tPCRfKojwR9qkdmQaTkPYtdsXuGPLk4_7t9F4ZME-4-3y46eD56SBl-PSkJHPRsm7_u7_buNOLg1FJrDMhdz7KpsHTcbaXJC5LUEft5TfeG53O48YrGhUuaZDmuA7dhtte2b-7D59Og_yzSw8OmpOi_OdyDGZqKx3D8DQXjofe53Ed5F16kDwp3mLCX4ot7ePcfo2Klv39OwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3L_F-CkdOYTEFXCsvNNmbZOsxq1c8Mux-4oLVDpcj1CBmVT4I2OA4fKapMKVwu7mqjbEwPx4Mlih5lnvFh7yTbPOcFO69wvVZuWwZLdOFLKm6QBfxX2ddPskW3BPXs4TRfBQy6YO1_p2r4xPEdEIzD83IK7aXCekpBsQ7OxDk5t5t4IBrdR0Ol3IFA-gsGLXDV_T7MtJc2eS63oUKBcaHC1fGJ0G04VDSoyuntq4lyZjOABUfKoVkLy0mkj_uhrtPISRLa0QUPb9lA7GBeIresacNDIxewEslJh4PA5TLDWTiiIFs82VQ4O4jz1XM_GN5ckY-ZoQy95lYSA94QLRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uepTxFRKuZNpjAxscgjiCSmkiAJg_5066MRiS_fZdhMffbaI1B1ApJPmJ6p0w9KTRyKwojsJ84WlH6naZRj1otdxOw82o27PuDMjtvrtT7NNe2QvjwT4eMy8T02uJ4V5FS-EG1z1tbidKKkJFJhEjXEg9IDCNw5PLxjZQnfqbmp_x7U2hlCRZWXd9I-QM7lM2EUDjiSbvntexH63Hub6zn1CDcJKViIJuy1dg5LfjZ15ItYfcfO4kZvTSxlGO78nxekIwqRhhfx7Ulx3YP36cj7NordruFcXSiqt4dh7mnrTcez33v05GFJSq_BtMeGzyzzkcIl2WdQUHeNsh7muAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7FeiRSXABpRBvVtcHmRe3naolIzTWU53hc4EsofrSY4GG3sAszOit35jEpjzQoKHUSr-KKwz2WHShVnxbuPoom7I-pG3ybqIP522VkcCgKNUZRIOOdPsqME5xYsY5jcFqVulMek8LcQIX4c2SbmS5Cr206C23bZ2iF_ryOY-0lZIpU4p6TSP4LXLeeOHp3d__q05kNFIcEwoHlWje88i25M6JZXOZIGpI_ngcje1VsBUIND_Zb4JaRtBzI_z_N6XWxiiNl18u-H8YJpbCzSahoy7RmHWVmh5yC5_PXMG147JvvVkUepOfRHDbLqyeZ6RLo0RywGazO8HDMp1d0Lqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0ll61jii0b4alo26kgKyV5eAJ3IO6K8fWVxmJ2s8bkzODotMLdvBijJjIZVzOZxCNrf2VwbS3JPA3IRQ2Z_mVqPILIj0wosD27w_vSYTABgOUqmhM-lDDTL70mE-NMseN8EB9zsq50chhera2rYBvS7lKZcScXyvJ-1XfE8B2Av7G1rco8phQpBVaBY-iwj80e2ONEVyR8IEBITaZlrSkEzP2sDLKKl-zp-QFDAGTRqIeLsJ-0Isky4bYwqKOEwgSreDYpnqa_wi1AG-FyvNKHfBiD_tGwdQ0W2uX7n-kP_UKOoadmfHTkcXLSha_isaLKlKtTiFhCe3ZRc05QTFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgRRwkVhSnwcVSPF6A_Cuy4gLsfNyjcD4dIXq3TJvcNTxEn-IxYnYqIvsLmRAp19sLZ4z_wnXZ9uSpZHj_tWqrxcnBGXohMWoYTicm1ntt7vXMMwf3QoLPAvW5irrDB1JIUEsPMdyp-F4sPcKVv1dbvlKSnbCXCmfb76o3nK8tgCp6RXxwtSPuO7MVHtIU5-CvbndT4eDoIeXwrXC2KVjbN4pIxhUT9m1TdenoZBROZ4P6a7bs5SRKTIoEO7L5-J73riVGnR-N7eShmMi_wryIibdUux__0pJMPU-ybHf2TQESQjweoatE9VuxgjyeWnL4txJUeJYXmiSkYT9MBGNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eM9mKx3T76BQdhDO6YtGIOYjjBA5xVZb3sjDiz8xl_L7-3LBUnRmpg6cSteKJxnOGLLDtA6rJraNzGU7z-sq8UVApP-y3ZEi__40fJlgqgJnHTpo15RQNFdcZaG0C-k2A3Kz1_NxahlL9iqRIVYIs_hSI6yZe7DZjybPGto3beZ4sxG2rSnPbHlBLDIFURHGZDN0RxT6seP5oOMLJ4jIUBUCPXEXxKOe8MXp_O1w2-m-xjl2FW9ZMkaO8vIMKLATmKyght9rwTf0cZzfkezPq3IVRoIhtsw4cT9y4wSYeHDLx7pWnnuVINuF3Cg41QtRctEnKSyOTdFASPLjZw0CHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTNfK3nqKpA7dM14kLWd13g3ur9rDmX6uBUANgGwMbquPVSUpvySkkVJJ6zhyGX4eywcHoiXFQuSH3wwT7knrrjo5hJwPX1k_SYczk0GemMAwQeeZZ4LJLrbQ6jBAbRIT4iB5Ov5mlrYX_l7sFEMBDRLnOYwPbSvOpzE2VxaL832taqqinwu7rXCHW0BJOeHIKSH5sIN9bMtNPDtDHT0SpsiHEvZ90fA3aPpjH0hetLF6khj9mUk4081xXGINkr_Uxh-VwW1SbT0ZPF7_7Y0yc_shaGDp8QrYrzgZtkgH7XmBuUFEabkU-0AW2KIihXNu6s8OQWABsw5QrG2LzfckA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhp8oVGEaVbkq4MyZA-WPDopSa1kfiqoPj74kx8s3LllzmtqTb7hf3fOBwDTy9YRpvQGA97yQaCKSpf_DPfqz0Ws_BooynpMWAd_8HNg90DIo74nFQONyergReqmHBTtFJqxavG3L5ROnWmKJwOsJeEpZN_xZiMsITo2yxvqZAskOncCbTIvWRi8akVsG3UqIvQxO_veohQXgotL7eyAGWUKZnwfAXzScxOcLZpdQZaZUnGWXjzWEnPGSYWWVlq4lqPhdfGLpRCHuczS7jB49GExya_dzv_FalBZKx1T8Re24sQftKSKzZCMNGWIriveeF_KySqI-uQGa4Rex8VFMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7GepNLP8nmjZ6OStYtABxlxNmQwc6jf76ypjOSeMv3Mh_DGUej5TaaszY7uPIrC9P5VzlJ8CJivpsRRmG7YWwNDsDbP171zX_tSvZZ5JlNEKQGjq3mGyAP_MIbHsQYKHPsHK4-gMbYZdx3kB9f7PhRe0VTQh4il65p-DxkppiiFj3dtLW1q_Po-BinMHr-2VsJoSlzC-MPQ4ealLF4ZA1XkSVVriHyyCYItSwFVpRd2zenjzmHT0BUdoaWtdsxE80b7MKeTYzCzHaZ0on4k01kQ1LnPRUCVLSH5oBkvEZztt87fhJwmylz7GDraJ0l_hyiMcKbcLLYMfw3oEzZlAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PANFQ-3lByMH37hKBOLf94dJ6cSvT_JrXzFP0gZ72Y8p-INE_tssW0YAtWOCYDzJTs3hGfRexWzS_JLS8bAIOtui1exqakYE_cuhpg3V39xRlVEL3qNRv2sMrmL6do54LB_e73qGDeYwyyhb5NpkcyQKzWbaGY9AKqpRdoTiQ90Kz6Pgf64GBjlM6DB45PNkKBqRkHSzvVXZwfcRGK9edqZ0RMHvE-AXa3GbpKVRqcnltM-CXh-YH9ikh7iD-Ew87w0_GR15m4lnqd_Nxv6HipehZ3uHP99y6jZfu_A46y6PiYxX37mHS1UoN7HYmcaLdKXnCwRfcwnO7m8DPZKcDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SH4xJEjdb2DXXWGn5l8SoSth3gmQcHwLAXoLLT0vOFDvOrxxqBwZC0qq0fUh1x1L6eox117yYPXMQIRYXml5n-lZCPqKXc_J9u6GkDn107_HQ7_rrbYb8BkDN0qpP-nCRcsNa7x2ARdrQb1u5xjYISRy1mCdwnnJqWDJ5j8J7j5_D0HB4cPYmlgEEmjt0EpOJEz5bPiigaWxfd73FutEWb6Fi3U9fgIhB9iadX1q6eKvfkR0-omrh0ujzLzKznxCjR9roB6q7MEiHkXbN4RBUrwfB6F9I8zHvf0H8pUpr1-C7wbcLQzwPX52g4ZQyk-r6DScIlUR68uHmTKYanmxPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLhinStQARhE3sDUhVyLH4RNo4NIOBLr_QxI7iv6IFwIrWf0B9Fiug-gk6aUy9SJ6oOpBDBUeUYcShVMJSXmtcmlgMvH2P57z0zhMRZQ5cDi-UUxej0C7ePW6koWSrHxP5Ykh7v55vxkO1dcKFghehS4oatETgE_O8aLYZdDg2b3TL1iRfrGZkOxuG0MNCBNg3T6QeAotM8Jf-OEyhqyfA6bZaMxwsB0822WL6R8rzdb-hvH49oRmkvwR-4O8HQXhCyjyLvkqP-wJYqwtIs82v4Tw8uuwXxB9OFtdp0pZmPKGFxbqbVVRCHqjRdOtjftpSV3Hk7tAkkWmLl2qS26dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdhuE4_bgkZZxxWZp-TBs5XG8PmnXBGaWhbiAHb_DsshJ_s7tn-I4ejzHIDyArNPRFyydan2NqdGY5X_5Ilvz7egq9PjASikG_KcLvzHCCtTiCg_aGSxarmeWokOqyx8Lo5gRflc9hPqyNDOa4v7JsabPHsN2EvryzwP6t8MbCDC6BujhpC5dzVftPetQGoXEoCMWGzrohgHq5ZDyGn0axl6Xy5tf3Rp48cntyW-pkPu5nsSquDm_FW-T75GVmWvzdwFhiYoRmt1YMUe9gFCTvgwSp9MGFapxaXg4W9UAwTjC3zn7lB7IbRAJEbR4NIRcjH_jWQ6ZnuwYwAw3hUYPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCqgWiHHqx55LKZO_k4YgEhMctOwr1afKXFyO2asKylXu7JKOgV2oLxYCdjDmJaeyR_j84oFytUosysw31slcIEKezvgsDgAWd_nhdvDNd8MA0JOSqXIqUcoBpm6l2VVHB-Yr1vyaROHNovKlFWDoBjA6bwTh7ACCb1S8cOwmX1R2SsHbyVWPoGhJ6x2JiUD2gK2bWH3z38XSmaHY_OPf50PfVh2O5HZlFrN1FZe431g5uxjZMB5jHxCI7q1ySWVtR7Od6Jzj0CSq0vkkKoJkLfmC-W97XadJgSqssE2BvesbUmmG1ZlIRvdxF6E1SKFRB4X_ApjFjkP8_YC37CVYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWk3RT7DRe8AbQQPJA9IRYeNtMX0ervoKyf9e-DP0OcR-pSIFRboO9C70FoxznvgawG1_D0Xf52FkXEo4lSOSnapcsdH2JJyvcjwh43mKbvN0hzd4-V55_i7S5pM6XTP9y2Cx1xJnnOpJg-4Jx4nuDzCFA09gfYZqByYDGMRRgJpFT0ZJIMoyK7BSCs0vEZrkXDJCLWOz8kwELqsJe7GaeE-xp1XBOsSHzwDNVVUqVbhlpyBAvjVsYrKSET2KvLD6kyKM_Cn-5m3JEIBKahsmYXWlCbRWs4P_b2QZLyNyzPfrVJAjH_w2rMHy5uLA3Wmt5r3snqiTz41_JTCwrFWcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_y4nrQK2fsj5dBpnzB27kIyR33ooi3X9Ji0sXh52NyL57FL_TXFxKGdc6MmCydGZ_w3JquyxJ4RhgYm6jnXLrYfrInJsv5ZwI8QMNx8ktgJT56DkoFsNo75bJ4FVHEAIuw7kWQS1lcrkQEWNlxRkcUI-PKMeTped3i2XVj12RJ_K6JqaGKNa6YcXWqVte_UKH8XDqG2XUBEgEIEDm-h4QmcrOj1rDzY7hYHSCdKUT9z1NMmoszA9Ug_wiACYiivKYnePKZvN4HufhtssuwwPjMPk5nddce2XW7J5Pv9h89Ri37Be1D5aZuj5YvQC3AaHYqxIs4zu1WiC9Rs47-lKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_62rQDDr01KKPsGq6GiNs6Gzr7KuR_aOk-K34o1dmFONaRH_NfErfRzAhSJ6rKosHrrMr7MlsI38Y6XCPL4XCnxg3TUO0i5utwv8Bl21hCPRCLrqHtYfdIVGLEVFYbaTHPEEuhbzaI6pIV6XIyALRDluJXjmyjmCHIQPiCxfC1IKBun-_i5Eijv85b0rxqEDiKNRSI9o57TgWNt9aM-pAOOv_OA_dfNd84sb4qBrT_sVSApVhGMN3Sbj-pX4bd6CV_YhkBkvC7Vic_wL1ZMJ_OvH0pPWDOC6B9G4FPpfMOTLytNXQQpKdj_J1pQBejSzRr_dBn5iqoFG-ha5R5xgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuwuMDcfNERvIBgGeekE4tdpAdyOQKWYEnZRgtwHutLpYK1ihB-31sURYnw_6HGXKhj2Z9blTcMB5dTHOjju4Ixn8sImZTMmplBLwEToFcEPIK-Q0x_qj-6Zj1gXEAHzCyxuESg8i3BPgDL9O2azu7Tfrs4xYyiSVTIq730KNOk6O0Lq5sHksXy0aoebJGwupZ6yrx9yBZYSmOwGIjBtrjlm1i7cGgbMIAvbSMXPhuVR2HZScl1jEyHd6l7a1nz2KtlrwFFyJicwHdOBzo4r9rLewbBc1pMkCxntGogHJTxoDsNPmzxyjO8WT1GPH7Hvhz7Qb00ZlpoQ3TLscMUUgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tugwwJVWQ9gbQJhEqtvOfFDVtNeE5nj0vojVHeteSuZETB9zH_FIb3wJdfikAOjEmVo87770FGyg786mQfPgWdS7gZ3VqcFyjrNDRhLLl1fuX3KyrqgmUkR6TviaL5oKaBhlNMVADpE2XbBw2TpFo_3mDCdundG4jfGaA-An_XyPMlPHjxA76qhl6yue7iToE7hE_7Y7QCdj42VlHN_Ua-aC_PZwm1vu8Jock1F3ObqdzytBP0lmgw_poXtTL9c_yyPnXpOavNZImZ34PGBc39XPfNou1PGwci9cSAMcYdUDf3POz9BibB17tQLwMo7zuG9rjg5rK8j5HCY9m2FW6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSvBMSugSE3bKdOLCMVe0CNaxXlvLH-kSDCssDQD2S4rzetie0U-eaSRh8onwkEN5cvJcX2KzzY88ab9MsxneRUUkct0lWnS_rliqcGwINgFH40wHJs1k0U9TktV9xBGBvwuKby2FnSO6Hyh5fxxm_zoCqqv4sKdOFgQBTKmIFng-jPehsd2Dv0uNRxOSHzFugqiGUE7D8lDTNaguCf4ZK1A9csNGZ008r8h7M8UdbxvxzbO_24rOV_Pnj3F7eaRLZLJYw56pwbU2pweICDWLTPQoWqVxTMmL-o_iuxpJgoU_AFtCJE0PEMEldL4N5CpMp83ebGdZcZXyiTWgDuVqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vasiG3ARN8CL17sD71qY7E6GWtohD8CJTuM5yFWH_qJJmBt4AMM4-e4yZgIyy276fL6wAhevZJ7CSZXJYkbIQbBtrFYfRFPTuWAZ09Q0a1hv_8O1Rw5v0oHV26AwN6tLPpnW2t-eiZzKRfdCAdU7Xz0xjrtnjljRx8cqBf7kZ3_pn5OH89SVbLFujufA2ZSaQ3g_5CaMdKN0Pq_9X5Fe1FRMuAPL_9-8Govv47Y0xZd1V56_h_ySQDyG_cjnCXcWLl5fk_WYbx2pVFg34Obg9ea1Z-UtaiUq7MLdIDScAcZ924S8XNZfNvV8rDqOGxH8zaYsKXka2zH7l8z6KG69YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMT68VcuSLAv8GPh_zb4sWwpLFJdZFuhKuyhSXtXJlxhk2QYtpZwANkAnMi-KbgFf0_BlULARmVt79y1ptCB7lMMXvD7fdLCJMu_KJ9YjpFijuqGr9ZX2w_FtxNS5IZqtbAzL56ENu66eFikOp9TtO_ebWMTgw0TuY5Py-gpHXKF0UF-Mb-69mmSFzLJvbr6b03BfhEVcESH1ejhvh2K-HMXwxlJJ6uvXMkvOlCZqwKVC6ErrjjZ695wTCWB5pIXGAB4SDU2i2rW7IT6qd1x5WW1wJcCcOLfaKLZzrXvWRPjR7OKiCyM9YXrMvsn0qqxhDKaz_oZip61VtScYdkcLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-QHaRgEQfF5VVdRODaerk_Xo6t5PLr9gnbbeD_GzBmJFu5t_WlXoqDAnirOs61ul9sgCuRkgNczgCuG_auFGfhVSGpDUUqBwNW1lYGx8n8LY-j0AV9bmTOT7SFo33jHgOiifUAxzS7CujMbs-XutYPAYOMbaPdEu7eb2DXwvYYtR5uCkgaVSa4MeyFNnbx9VmhacfxzBmfpm9DrxFpdvulmiDV9BE_vfGjdl8ff04Ib-AwgVYGSVchWWVVHprZRM3PE9nZJFBZ0ld3E9JdnFiR-iOu6bPkxof8bdJQuBC2neUAp2MlC35u7PS1XAmmDs8a0LgYCTg-sdg0p-Ttcng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=bHV58O6v6WjBgW6xgzfqfi7hB8EdwZo0ujStnFWv_3TdFLUXFZu3xJt9GGoDoV9M6g_SWQC4bl8U4HeyAqgKupy3LjkLLyDWzZ3ilw-Kdfu4afVn_paC7y3GmRqsv8Yn9iZAX4Zxjs8hmjXNPL5BRtsR3f-QKiAGjvQKXH5XgxOFh_tej4BH5UZTtDMAo0f1Ms1MptVZNLLEksDzDwljd-kEyTh5NjCgXRoO4N-APTsD5x4JQrqnbx9_t47Bc6k6A7QXnyIRTe3ppclcy3LX8gcVvfWBHAQLO68n4BSlEpXIGXGUSm8-FutpLB71ltTh5hv0tSzTmQec9ktSzd1gkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=bHV58O6v6WjBgW6xgzfqfi7hB8EdwZo0ujStnFWv_3TdFLUXFZu3xJt9GGoDoV9M6g_SWQC4bl8U4HeyAqgKupy3LjkLLyDWzZ3ilw-Kdfu4afVn_paC7y3GmRqsv8Yn9iZAX4Zxjs8hmjXNPL5BRtsR3f-QKiAGjvQKXH5XgxOFh_tej4BH5UZTtDMAo0f1Ms1MptVZNLLEksDzDwljd-kEyTh5NjCgXRoO4N-APTsD5x4JQrqnbx9_t47Bc6k6A7QXnyIRTe3ppclcy3LX8gcVvfWBHAQLO68n4BSlEpXIGXGUSm8-FutpLB71ltTh5hv0tSzTmQec9ktSzd1gkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfJxu2Ds-KD53Tbh8D0-XP3Xuwp_kuIWJMElErKLIRi17H2E4Su8NaEk-jn-U_9S9pFy4Iz_ojRdnqThdpwdUe9DBOgNozQJHBBOud1Zs2jxqAJRuvXoeiO2L6K3DftOh41WTbkqYBjzVjpFMo9wvyD3Yvb6GzJZe0q1_N5O-sEdoPS-BBDotqEz_AtNOcO2LxAPvtrOsCnT5l11w8pWlQIytScmEoS1e1kVAod6mLlnlLUuxA0bjuw2QDOVeFbj8zH0yjpwlbITs-TUNLhNcCRoUAcwN6bSqxAx209_N5DAYLeSzHjktFjKut8gdN7HcwNMuyN07fo6n8pAVZDJvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
