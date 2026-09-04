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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 20:46:44</div>
<hr>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=eqwK7ZRqs-vHq7eflBWJ76dO4ECMlIV9CVrB7zryykIi2TibKwSGCnFNtCnVIg4x6k98ek2EhL8Lfh5uPGGd5O8rtZsSo7nY22h-SJONdSYMxSS3AYMeavXBLSsGE57Sav_NxwHR1Tka2dxV8zI0FyW9nckbcrsowxOglzVkeD7xxWuee8jrN86ME-PXNL6NldpRr4ZZ1ytA_SAcnxBWzPy7zM8FJ-GKpGSppLbd2x4DlFmGCK_P1NxPYhAr_oVZ9rs_WnuAURlMGaIfsqPyJZpVgUTbs75Va8kY8FqUkDkAcY_TCq6xVTM7AJdRY39OWaSe6nwkjThah4Af9eAvHAWzO5DisdOYosZLO1wdsAfIyIeH63GdjedAC9Fm6V17lATsf_0wJldGL3rszNmXxmPpXClFxuwypVrVu4c9Qu4NGiXkLqbeoTIc1H5BxpKrYIayyEh4RKw8RqivMqYniopzljaFBdpeSVpXk7Z3vKF3HHEC3wRLz2UE-9JdY5yCE74f_LorG6V-pUlyYSzSqHvohd5zB1sKRafrAaQT52bhjAbsi6LVK5NCHBLpZADBVPDvuLB7uCTJlWY8XVSNDlQUamWZ1Q_xn7m9yrIxpQP8uYXFGS6-LbGYCLTJJQ3cgZPtoHxL22MfWZo5qayqJkSSvFFXYEwTYiEvPyrxF4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=eqwK7ZRqs-vHq7eflBWJ76dO4ECMlIV9CVrB7zryykIi2TibKwSGCnFNtCnVIg4x6k98ek2EhL8Lfh5uPGGd5O8rtZsSo7nY22h-SJONdSYMxSS3AYMeavXBLSsGE57Sav_NxwHR1Tka2dxV8zI0FyW9nckbcrsowxOglzVkeD7xxWuee8jrN86ME-PXNL6NldpRr4ZZ1ytA_SAcnxBWzPy7zM8FJ-GKpGSppLbd2x4DlFmGCK_P1NxPYhAr_oVZ9rs_WnuAURlMGaIfsqPyJZpVgUTbs75Va8kY8FqUkDkAcY_TCq6xVTM7AJdRY39OWaSe6nwkjThah4Af9eAvHAWzO5DisdOYosZLO1wdsAfIyIeH63GdjedAC9Fm6V17lATsf_0wJldGL3rszNmXxmPpXClFxuwypVrVu4c9Qu4NGiXkLqbeoTIc1H5BxpKrYIayyEh4RKw8RqivMqYniopzljaFBdpeSVpXk7Z3vKF3HHEC3wRLz2UE-9JdY5yCE74f_LorG6V-pUlyYSzSqHvohd5zB1sKRafrAaQT52bhjAbsi6LVK5NCHBLpZADBVPDvuLB7uCTJlWY8XVSNDlQUamWZ1Q_xn7m9yrIxpQP8uYXFGS6-LbGYCLTJJQ3cgZPtoHxL22MfWZo5qayqJkSSvFFXYEwTYiEvPyrxF4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=dcjPb75sqIdGPPcvlYvl4FOWgqZhVerrcszwNTEYaFrALw6lOoCRrVoJ8BvaCOYXKDNjhPZNnQGAhNfaGkk24X7Ic153shdDDSuOJ9u7kI_s6YIpqysNjQx8DSg31fSQAqUT6OPbUgpGBz02wFR8mNZul4X9_i4nr0vDbQGsk07pHmW7WSu_vsODw5WewrVM-MuAE4IDnoeepGX5tuQIg7eIMqZwA494rJWmjKSTxzNxdMrD5Egbx0PT3_-a54Lh6uzZE6VsSOLF2885G8hpXFF4CzEEXjL03Up5GCQKpKGrIArBk35mjTYKHlwqubIBPStJOGzoN5p_d8TMKq2G5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=dcjPb75sqIdGPPcvlYvl4FOWgqZhVerrcszwNTEYaFrALw6lOoCRrVoJ8BvaCOYXKDNjhPZNnQGAhNfaGkk24X7Ic153shdDDSuOJ9u7kI_s6YIpqysNjQx8DSg31fSQAqUT6OPbUgpGBz02wFR8mNZul4X9_i4nr0vDbQGsk07pHmW7WSu_vsODw5WewrVM-MuAE4IDnoeepGX5tuQIg7eIMqZwA494rJWmjKSTxzNxdMrD5Egbx0PT3_-a54Lh6uzZE6VsSOLF2885G8hpXFF4CzEEXjL03Up5GCQKpKGrIArBk35mjTYKHlwqubIBPStJOGzoN5p_d8TMKq2G5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqgPO4L5-cWo13NZXBiUQBBxyPePYMKPdxDLbbZToL7P4p9fdeeJQ0yqZ1OBoFguePcF-p2XAEs2wKFdIsl9blOkNYsougYUSTDgAsgsGFTONxPxJCY1krhACm3pE9DtQqTyuBwrL13miq3QMtb2UUVjLHYdaHuBohZZvRETUMvdjS9C6YLv3kOTT8d9XP5d3oj2cSXTonXn2mk7GFUjeiJWeopji4ZIzmPEUhexUiknAq_8qNCAYJjMR8ySeoRtKmhCsAWWb_ye9H04t3sOaGlna9ykZuXkGaifDDriiSgmae-Izv5rqExGkp8MfzAe4CLeTEHfQCGTsD_eOlTNwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=JS-5voReP6HIBhKhH1SSJIiDFVxv_MIJYc27-er5Blq6HSSkFp_ppaIOuPN04vBzw478Nf2DZY8i4tGLndOGK_RzVE5BuzXlBotRzFfuNK0sA8UNBvHTwZytdMo8Nd-YUXlzIdRd68x9IP3nm7jU-im8U-PC-cwAVg3yOG8raIAJAYe8VxtfxIQl1BJw7GAPjk13BAdlKns9s-QLEZn6P3NSxLJqFneLI2QVosQF3_Q2fVRCM7mz4ygMBQxfy7bA594gRs5vMiAoaV0ZGNOD1A6Nu_9tmW3OUO7hJor_M1pzJQzTQIhhj_7F43LgtRzyp2z8UA1gZCLg1jgJmkTodg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=JS-5voReP6HIBhKhH1SSJIiDFVxv_MIJYc27-er5Blq6HSSkFp_ppaIOuPN04vBzw478Nf2DZY8i4tGLndOGK_RzVE5BuzXlBotRzFfuNK0sA8UNBvHTwZytdMo8Nd-YUXlzIdRd68x9IP3nm7jU-im8U-PC-cwAVg3yOG8raIAJAYe8VxtfxIQl1BJw7GAPjk13BAdlKns9s-QLEZn6P3NSxLJqFneLI2QVosQF3_Q2fVRCM7mz4ygMBQxfy7bA594gRs5vMiAoaV0ZGNOD1A6Nu_9tmW3OUO7hJor_M1pzJQzTQIhhj_7F43LgtRzyp2z8UA1gZCLg1jgJmkTodg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=Ed--jvl3Y4vjWbfPL1kKpSZzQzAYU70WVylYs4sKKSYupxxF_0Z8FWeU4iLvRN66GmDf4ZylwLIGoQcI4hE3vv-B95G5BAWIemKhcMS226UZl5uA0fmxGIEyY2ehN63gEMfQyrTGFRpQhE7tjL2J5cQ8LyXzSsewlkht-ERhM2th1qNHQSKJcYAXE6sBYIPij8Jl9u1QWqe-WybViCogdWJHez831MNno9jTyTmcBumktMOpWye4m9E_sTNQPF8bPWG_E-p-jwNqyXakHlM_8S5Lcc_rwMhAO1SS4gB2wtTmT1Ya--PN9l9kxMOlECX3iDM0Awi_3iOXUulqNd018Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=Ed--jvl3Y4vjWbfPL1kKpSZzQzAYU70WVylYs4sKKSYupxxF_0Z8FWeU4iLvRN66GmDf4ZylwLIGoQcI4hE3vv-B95G5BAWIemKhcMS226UZl5uA0fmxGIEyY2ehN63gEMfQyrTGFRpQhE7tjL2J5cQ8LyXzSsewlkht-ERhM2th1qNHQSKJcYAXE6sBYIPij8Jl9u1QWqe-WybViCogdWJHez831MNno9jTyTmcBumktMOpWye4m9E_sTNQPF8bPWG_E-p-jwNqyXakHlM_8S5Lcc_rwMhAO1SS4gB2wtTmT1Ya--PN9l9kxMOlECX3iDM0Awi_3iOXUulqNd018Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XG3f9QOi3hKDDyJvO21Hx7hCCLAMCXCJRS72UU-RndNcIaVcYQgkChldHvKpo4c--VdJE76-vVQEQTlZbGzZA0JTKhU3MC-Pxw_yeQLEY9GUw1XZH96cqZkCi3zkKebnm7mwkTzvh6mIpGTROobJgeGrFkjFoG0ZfGjmRhsYd8k3p1YYf8541ak9Ui5Tf_ElRTyQ4Lq3e7k7m3egzW9iVqRJWie51Acjvjq9s1mFNxAM_kCayTubZzy63e730Bybvw1UbbPAZSAVRW0WnLYtj38vdla8_EqaOxFSDi2tgHOqCG6RVI5nvQk_p8v3RHp9T3ybwF7Zvveb0OqoxJ1TmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZEqPWWiNRlANetar915GXSvcA5DOr5NiSp_TTM851_KqsahyRTJIXvUEjoEUgyGPp8snDIUQg7w3gJ7P-j63LWL3ibcQtPY_EHeN07H-2A9pBXqj2gCKVWPwtHwdp0W-Yp6IjfYRzCIaljae8CLJobgnm3bNXvmQrPsOdlMkL2f8c778-MdE7zcsP6r_yXnrGG1wqbbc-Scn6q5HEbo30GHLO0A-dk_cQmGoKnb14NJTdZ8fVVx_sQo6Klpmdwal4eRPey7u9YhXHIxjdFDAtaZtl9RFtsmuqumFX_gjVB_i1o6peY6juGaL_Y7D-cbi_yHpWee9Eh0VrMHu_UqAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJb_xaXd_XA1jutx0oYBhNG44bUcWHBEx16DFyvdqiRY4Avwg9fqwnhP_c27i2nGS_oxQ_hSLHCkm67IZBrjSuYhaQM1TLqh8Mik0_c1DQJXqvu9BjCocfyXAABt8vkO2upODVa0WgdOZyUmKFRKOR6GygJWQzAVz7mwpjHcR72G0myZIvo2AY7kRgqm9xnJRWnd-bpxBYPzS5U93loF-7Kds_yNSFNqkTfSw6jhZrsfowOxnPLYB4loANz_PLN62s5K6l4qlm9Hne4kVSNfFMU_FNnjx6kl33xGaurLRUWvy-ZBj5l80IPu5pbaxwYA6QwJsAKyt9XPQ8-Dg1PmpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e64AqqYhYloXlssAIW6RNsnkG7U7P6hhCg3nhkolFtIqy2CWaz4M0u2NJbr2FlAQJfNsz3U33CrDNyxAWJ0aW4qIX4ViLgqFcjjPJiP-dlHM1eVfX1TqkRj2BFqCy220lD1_U_8oeA484tVIDuW4S3NfIs7Sxz7MnuN1EzsvbbtZNUq7HlUHBPewe6HVvOo6vdXcbCjR9XzJvlP-0NTB2WrM9TXUzQ1vAv_yjb3Xwkn7Sp0MvrBN4GBUytIdGqwrhFIlDPOD-mYPPphvdNw43iRPYgCAPFRl_k1ppErSXW-rcIwUReJolUJcL6LKr12UB_WPHASJaB7FctSt1iegiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkkUbk8PJ24p4q8n67RQxhVsJwLZ-BQ2ZOIwDSxcxBZohJGJ9HmtBqPjxjPasUCJ6bx-KwvA7OdAoncaIAl3gX-5n6yXwZAtl56eZXQqDfSQmPFIzKIrsKct949u29WjHqIV5Zi9WhXK0iabhpv1iMMzrkLwUREv-UFP8n4mMQnYRHIcU8jzM_Lttc6J3qJf-SHCaZqYRrQHGPEUufaPz7-qaMWuAcXYpU2b6UGpkANSe1wnAL7LaiJeSpFCT85w9PpfLPkGauFyWNmM15EvKYLZQpQ5Jgne8tS1397C5Fnd6vmhJsAQJKqXLnkGCj7nazYWNPJ3YuxTOp5KHTjlQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5D2EX_RfuUvWJ1_ChccPPvOEmMYDhCT3sOXUi0Mz5dRdm89WHBYMFFD6Lh-15Hib6za6mDCWOAfcgbp0DkGoH1BnWBKs4UwO-pPc4ET8qH9fwRN3EcOeagiERjnjUct6nE5HDaWxfmmqX9yLQKCd-VIEd4KRFfuwYphDiyyhbYhBIsmOarGsyp4RiLi0Ayl0VvsCDSbyj0cLv17wrjtT5C-lz8YJjmTgHq4yEaovcgclAFaJ5JzfywgxUgDWGS_R7ck4Q4UQvqDSue8_T_h9dUpIkFTdHT9Gubn2HvxYpB9BfsWTKIDTYKUxL_V95GZAFYXqQPXNU8b7HRTFieTMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeemvMPMMWIWyDBUi7nAktagt5iCRKBqTPgsg0YyEWM7HbZWgZbGik9Kc3a9GIBmio_lHNICqCSjeGcNT1zb4seDlOFLgyjIvGFpDRlCwmwWGmyh4u-sa9xq9cEYwylSCJdi5xTAKZKQ18lRW73Apc0SbOnwLL8tDsWbEJgcHrBg4GM5GYUR36fXJny1i0teA2qA-U1HAtISxUZyfSFDD1mpxDlW_BfqZXwCTAA0LOmXIMwZfo8HQt0CSR1Ao9sxqPlh2K9ZJA5ZCzbE5hkvLHDBWeTtulGr5i_39u4CAlB_8o6qDex8I8yWKg71GWBqBZk4XWuydAPmcQ-cLTfpDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=dp3uuY_kAGFUhCu8nvSGpky9eHlfGeNU7z4TsHf3tPMNHWf5IujXZf869cDcCcA1I7feBEHcov4qMDdUeXv3WcB3rdCxMejfm5kOfGwhi3CZhuLjKFbsPZ_BA2pvswrnwLFhpjlZuJJ_v0WbJL0MdH55iQSgOp1Ul0iCavSNS-3hMXfQe6jfP-7hi-KHYzU6Bx-Zi2lT38avb_urrpoW1N2dxa1jHpAvpyiil_ua4KYZ-abPsqkrZBXu5ECwMD1Gh_qAWfJ4UFNOLzyhL0xAV1LJtf9Jvh54-X4iE1mwVctfSdeCi_zfwxDi9oM2eElqUNc5OFTCq8G7r-4mu0NXaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=dp3uuY_kAGFUhCu8nvSGpky9eHlfGeNU7z4TsHf3tPMNHWf5IujXZf869cDcCcA1I7feBEHcov4qMDdUeXv3WcB3rdCxMejfm5kOfGwhi3CZhuLjKFbsPZ_BA2pvswrnwLFhpjlZuJJ_v0WbJL0MdH55iQSgOp1Ul0iCavSNS-3hMXfQe6jfP-7hi-KHYzU6Bx-Zi2lT38avb_urrpoW1N2dxa1jHpAvpyiil_ua4KYZ-abPsqkrZBXu5ECwMD1Gh_qAWfJ4UFNOLzyhL0xAV1LJtf9Jvh54-X4iE1mwVctfSdeCi_zfwxDi9oM2eElqUNc5OFTCq8G7r-4mu0NXaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hy8VZ9XBNJuBAyCPnRsMPS3ct9A9VbRtfCkW17DXS82feIoJKrzRhMI59ASV2txhJcGZ44FnCPBLe9UBzC8VpFbK4FEvCw_29pDnA7WYmLVQgFF6VcdpK5_WqMb41FW0N83grMm9blQuJjU2vtuGgOEp7nOgzY_rcKp0rgQr6oy1C2apsX4etUxNyX1ImbVRwY3h-ImCH4ifWj2viv4lOwU6jZZ6MZXS-eQaoz05l1GHadNwWBjkgskYarGoN9kpNFNgyJBJUuEdt4KOywr0SAF5BBcN3ASbfeg3QmnHek2i_tImHMt8cFp1Zvwr8bm9H_-bSKZ0Q7k3SGIy24EiTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hx7X7ifEhRGRoTXtTMLPSyqcDkW4Eeg9oAAejWu6NLth7HUgcR_12rqUOruQXijRiHhiKRjJn92pTDHOMRM-8y2AJeOUD0hI4M4wAbR2kqpjc5JVkyL9K-xUHvO9rkHkOWCbWIewI6155biFc7-eBIdJlHS4b_41Ofg7Bvq1guRTet1ggu3IqP1UP4uZNsCas4-7Hn8fJzdgLrRchodmIpDoc-aSxe5uZ_0CtISZlW2hZGv5CgU117dmU9Z-HqpQb8iiyooaJX6k8XqQR0IuXF9zMHIm2EiJVakyeRm2rCMTuOWK1oo0YV14u7ukvwEPmdnTgeapGqRe22i2dqUnNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=ezMP2Yu8pIOnHc819xmfh5jwWoZtLk6d3_EwptgkT_0rbyLHXBt0nMFeTE9jwXKMSj4gQFvV33t5JsnOvC-hEjxHK8RoEvNQ8gZEby4ztA0EYOWYGAgmtXTlkM8wAfQVKe4JASr15xwPiu-9GY-m3WbqGVRBkvKgvwGbk5XlXsu3-XcH_QeMoFW4IIDqba6whtQkXoxg3tkxUOZXk7hIqNFUleyBKQLNx1fcpf_WN2_pc1c3yyiXpvnzddGuyr__FixdbehsDTHY6uKCb-CfMbLyYzj2assP5q8ubExQLlbKQXa7KjSYhEM0y_xv5Dw3CBlsfJRsemWeRY8goI3qvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=ezMP2Yu8pIOnHc819xmfh5jwWoZtLk6d3_EwptgkT_0rbyLHXBt0nMFeTE9jwXKMSj4gQFvV33t5JsnOvC-hEjxHK8RoEvNQ8gZEby4ztA0EYOWYGAgmtXTlkM8wAfQVKe4JASr15xwPiu-9GY-m3WbqGVRBkvKgvwGbk5XlXsu3-XcH_QeMoFW4IIDqba6whtQkXoxg3tkxUOZXk7hIqNFUleyBKQLNx1fcpf_WN2_pc1c3yyiXpvnzddGuyr__FixdbehsDTHY6uKCb-CfMbLyYzj2assP5q8ubExQLlbKQXa7KjSYhEM0y_xv5Dw3CBlsfJRsemWeRY8goI3qvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=OhxqJDMhmlqyNXcuGYOG7kfiyDBlQGZFwI6vX_Egf0d0v9Z4bQLW3PfK1dyt66Etg4QrOMEiT-lK0DLj79cqZUcgu9CZsBLJwJCjx3WdiMlvxNHB4x7-_hmY6bAZVcNi7aFqi9hYgAFbNDX49Av7ieV4LKa11p4tfoFJCGtWlKiNYJdarIU0uGSBMoyuFMXamY1c_8Ulql9a_DvUm94wZSWchokWfnfLg5KQNQiyxdv3Id_Vr7tT9IK6BPOuNLAYNnEMkk8QA2NhcSk8scJvTKJEfGo92SAQkLzv76P0B0NX5B89Zseg3Jt4yKy2sauLdUB5sNGtgEkCmt8-5hGOHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=OhxqJDMhmlqyNXcuGYOG7kfiyDBlQGZFwI6vX_Egf0d0v9Z4bQLW3PfK1dyt66Etg4QrOMEiT-lK0DLj79cqZUcgu9CZsBLJwJCjx3WdiMlvxNHB4x7-_hmY6bAZVcNi7aFqi9hYgAFbNDX49Av7ieV4LKa11p4tfoFJCGtWlKiNYJdarIU0uGSBMoyuFMXamY1c_8Ulql9a_DvUm94wZSWchokWfnfLg5KQNQiyxdv3Id_Vr7tT9IK6BPOuNLAYNnEMkk8QA2NhcSk8scJvTKJEfGo92SAQkLzv76P0B0NX5B89Zseg3Jt4yKy2sauLdUB5sNGtgEkCmt8-5hGOHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onR984x0H-rznV-KtgH_FemT8ir53qnHZcq7ChZsxIhiowIfUnxlrTLL6szeivF-jLdR1HOqgNrdT4szDXNNve7CoVKZDNXg6iMj5A6urY1cQMxgA7RPoBvFo37HoEoU8idvYyqXB6qfpmwCIvEs-AU8nKfMVdysyeJAujenq0U518VvrmPsg-d0CUr-_PPDxTCaKp0vZ8rJD-z8c-rTAWTYlRdMsf-2E_rZ10-_PF58pAxcnISZjjNBx3-QVovdBWjl96tA203QiED2BFpeVWF_wbDaO6B_rGwBg-2hBssJP20whmXhMyaT8NAKkYTz-nHiWx8KxXDntyT-21TPTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUk92Bw8HBslQMj0X3Aci1oiM7yyCBhT_Ui_ly-8VHBd_67mWqhNSlfNG14gIZf75--WhEeUpdxHTpU7QbQqwztSaM8gbrDTcPimPFeh9sTgW031Di07GA55xosT3M9QWa51y-5w8VUDCqJ13doKchwKtl-SUc3BgQxgA8qc3XSPcM6TnQwgCmWoh09zUDjCq80c0pRzk_d-EDfSrFVsHSlB-Z13VMhU4W3SO59tt_ppEgUrAa5j8OKf6h959iVg_8F9TDoeMMrHTbF_fTCyLMXavvG94EBUiZTk2mya68PdCnHBOoFH7M2fuyoSeN5gavbcW30uEk9WhBDMsq9mpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdgyFenRVdsTBFg-kn_wNedb6aWmshXTU6eLavTiF-ZJpGTdBENRYWr10kN-szZKGsrWe_A6X9uvO6p2cry_opbwmB8yIPg0RGLnHI6wKxfVtb0tn0B40c2ubSYLJuADkb4eEi3ldgVKGfOj5kxeYTycVeRw7UlXtllxlVJY0taECfDoR9P-dPrgiVmQouyN22ew39pEYXI9HKMuTdMfnryseSoTvrz4E1DCDc0RoiaaKY5Wc0198kOGdjSWv4oDSfibpIqisD2pQNCf3kUMnPf-BYKLZs6MoWG7OM-xykWBaWmUaTeH9CyFVaesFgBytaxyT8omYYt3TCUgPGuUAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRcyItjPNwFeQucMCacebKYcyWyXElFtY97Swe4pflT5RpICV5PImzpe6Q29TWiXDPwRo1L6vXP8LTOTL8wgB6sAYXMCmrR3aKtjMRRJhO-TZN7lgXkfugIqI2qA0dy6MLha60UCwdGcB7SGJezjniOjh3GtNZeeQJM0unbX9c9fkwNH7V6UMeat9pXegNXf09niyXNRPDhzg13TSTd0hrN8Cn-rH-0EgIFNlymdgwcZfhN3bwT2Rcs-y2fuBfbkXJk_q1Y7HyRV9rQoh0HyA_uQqqcKl0djicgBTwd9VQv0muYlqkln6KlRP8UIreKxQZchDYVlbfaQ3wdKJYWWDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O15eEE59SxAoHC_g_nC0_5pFD1fgScTkXaTqGoo9IPa5La8vPiVA2edvU48oU_NIjr7drN1k5ktzx9Rts6VAYNMn-PCme_1sLVWCA_k9BCN2BJYGFkLl06aQAVMBkp3OMd5ocxKHkXz7Pg6bHcCtlNA8rZ-jzGj7Tz8QnijHZPSGWx7VwIknyisXTlOo47zXUuxGOBwhUg5mUERkw9is4iWptubMfeXzrSB90L28Svt6sNPwRDerff6xHxV31Pz83sR6HzuZ2_X_RX81Zy1sybq3LMWY4iJ7_is33JwVsKsy3gSYXdaEZLFsD_RLsfNJAIIZzV5UslznBYv_Fe9iBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEpydpFTvZqx-NcIM3FPSGJuE_pvdeTZCayeAMvNiyVFlbfwHoY-QKJ3VsokPUh4h76K2IfKfpg03ShMm5_oxFGancToe2VI7NipS6V4l4fo43ksumKXX9MrWGwkJizCHj0h4HqaP2pgneV4DDcr0SJAKO1vypxbeHruBKEjvw7WjvosJdivhKZTa2sy0cyWCGym2q399WEPWT9EVOE6jaG5olAHUwWDWsihGD4brVQhqqUmkudh-dEj8lqqIcBnE3-8og__vr9h17zWBlYA4OVk2DhmZ3HUK-oxI-dtv0fGGBJPA_nGpDhtOSHe0CnPSYp0qXdwULvgZYaW9fMF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9tD0ztDUDKUm1z__LpUvLukPpJZ6qUxH2rokrL79umuglxk67dgnvymm329bUa_yXCgWG2wfneMs3KbjvPlWXqclq8S9rj8BRDbNJN7LoU_-1f0kH5DGidQfsgbDVBnHVsw4eoL74Uat2jfLDDGYd-_KYRzWtyTeVV5HWGynpWr8ajjG0G3lArvizYm8CGAKdytQ9ryWJT6P6JG1_5F5ae-yuoBkXHY7_oEl9rhXdYdgDFkUT-MYcZ8RsI8uINXxd45SXT6MOH31mqveL7faQY8sx7XtFt1tMqy292R0LdTIA_pN-NlqC6dd9TBIlpk2WBAMa6Ea771tqCAW0lTkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=ZCZSM5_LQsE5sB0J24Iic5Pw8PxD6YIv8lqGR3qLsm78N6Ux41xZ6NrtEIQsX9mGelQQcYQ8ysf0SvmFV-bFlnTDPGFo35SNA-n7OIpCc8PgqvKXI4Aotg8jToDQhv1eF4gvoS5N_Tu1ieBCKAagja00x4fyJZFFw7pteZS5BGlOoLwh-o5mWok-OxY70XIDzesrndN7-sNHGXZowUpZDW-_BXTADTy13LxH3Nw70WoMPFPpPLNBxLJC99DRi6rITtVY_UHHhPKqWKdP4R27aOVdwO7hXESyTZhaobd3pwz8kGo-9WMO7Q8M3aSwfpKWvdqk4ag-aEQlnnoaXtF2GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=ZCZSM5_LQsE5sB0J24Iic5Pw8PxD6YIv8lqGR3qLsm78N6Ux41xZ6NrtEIQsX9mGelQQcYQ8ysf0SvmFV-bFlnTDPGFo35SNA-n7OIpCc8PgqvKXI4Aotg8jToDQhv1eF4gvoS5N_Tu1ieBCKAagja00x4fyJZFFw7pteZS5BGlOoLwh-o5mWok-OxY70XIDzesrndN7-sNHGXZowUpZDW-_BXTADTy13LxH3Nw70WoMPFPpPLNBxLJC99DRi6rITtVY_UHHhPKqWKdP4R27aOVdwO7hXESyTZhaobd3pwz8kGo-9WMO7Q8M3aSwfpKWvdqk4ag-aEQlnnoaXtF2GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtITKNfsZBBD0BjcivwKqvKPrcLAxAfq0ye1kFcvhjnLaQmElkxspkvlX34A3OLjaJsXcxDG_Rn4IiwlMhBS0j0E65npN1h7zAD3_Xz6oIhYp4I_Fhz6dq_MJEU5ez62_5uDcQR4LqebpmcJKHVa7TvkdIqSp2Lt6qwQi4OlQAAIAyz5SjmpPcGm5ao69VfDwyObQCt4bKSWJlp1fcfm1L_nLa-mveSmtis3nTSvhZneAaq_DIPrdfQfVBebllY4MPJqtIADqttit-g7f5AtKtgiEyNAApB3NIkSt8-FX1oR_UVNkycZV8LMJDmJURQyhc3yQ2uQoqkt6H26Xge3Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=XJjjOt0Hrt_UjRhuZD3OEHXU6v_RLiGX5wtRxRYhsWyQPyVWnKf5SvqCvMvePkk5VHA3M5YQIV6FT5hK6ySeURvMGyTcFA_p9Qq_e1KKKScR05uaUk-vqf4hfYx6ECQEtKQfe-Xsm0jrTvBHsQW9m2k2nCPeb2a2RWA56Yivx-CsgmzfYRwJQlSOXurSyUbkZPI5PQTyMtb9w72PnUFY372iTvgmTFV4KWHjlNm9MsC-yBNeyrDSX0pJ1G6wJng996jsEF5AOHxv5gxEtz8U9KUcFWcsIQTrK4v4dLO26oWh1bnJWUgjPAS_NSVXkdXwOX9YcZjb_-0daSu_XTbOmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=XJjjOt0Hrt_UjRhuZD3OEHXU6v_RLiGX5wtRxRYhsWyQPyVWnKf5SvqCvMvePkk5VHA3M5YQIV6FT5hK6ySeURvMGyTcFA_p9Qq_e1KKKScR05uaUk-vqf4hfYx6ECQEtKQfe-Xsm0jrTvBHsQW9m2k2nCPeb2a2RWA56Yivx-CsgmzfYRwJQlSOXurSyUbkZPI5PQTyMtb9w72PnUFY372iTvgmTFV4KWHjlNm9MsC-yBNeyrDSX0pJ1G6wJng996jsEF5AOHxv5gxEtz8U9KUcFWcsIQTrK4v4dLO26oWh1bnJWUgjPAS_NSVXkdXwOX9YcZjb_-0daSu_XTbOmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=jmUNaAZX3h_gKItuRm1BCQsirzUsKlOEs_XDuuOevQ-ftcuXV8l-sK19yYeJytlNPC8hphTXNDyijULekHxt32HymAmKQ5cHPufFQudMm22DRNkDURv1zCWKnMgTfRNTiqrI2TfiREj-DLFVstGCK65hN3Fot1fvn7EltF81UVi99G6WXPXbF4mme6iKfnenzCEWnrFpLynRb76O0zne_j0vfxUZ8X5nAvyQHP9FC-BYw_HaevEOH-5Lwctig1rGCQY2wS9iPPqQ3aNnd4-leExHvJBOq_F_F5q8fLlYwdqYHjo-BLJxrc-ntCHPj8JdNXjaolLsxKdGlWuZizJvVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=jmUNaAZX3h_gKItuRm1BCQsirzUsKlOEs_XDuuOevQ-ftcuXV8l-sK19yYeJytlNPC8hphTXNDyijULekHxt32HymAmKQ5cHPufFQudMm22DRNkDURv1zCWKnMgTfRNTiqrI2TfiREj-DLFVstGCK65hN3Fot1fvn7EltF81UVi99G6WXPXbF4mme6iKfnenzCEWnrFpLynRb76O0zne_j0vfxUZ8X5nAvyQHP9FC-BYw_HaevEOH-5Lwctig1rGCQY2wS9iPPqQ3aNnd4-leExHvJBOq_F_F5q8fLlYwdqYHjo-BLJxrc-ntCHPj8JdNXjaolLsxKdGlWuZizJvVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tquaoTQBBIFp3CdVvDkGPbejJoE7NwU6F-Rf8jJV-r1Ce_AGzuTczq9HWnYRDRmddVQDpreIua6ZcsDQKgVSV988q9sL_d1VvbN2-NuIp5Zpxy4bFMvLHXbeaZzuig6IChtYHmqsRolinaLWNzr7NktfI2bKDIbW0uLANTFqga90TDHsGWauNRSGrEmkIGTnPXi6Xx-Wk4f5cQMYYOBe7gcLB4SZZ0NME1kKEbCoFrnXlBASOLMpk_pUd_MX18tgJSzWYnS7f3gHqhig-sfVqMqEHAWd2O2wkCWm2Y8hS94GpXlPl2SCfi7ljkMafQYv2QJnVVhFIxam3_hYkRMTPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Go90-QV6XmqwLKjQU2niDnp8LQH4HgXzP32eFTBTEaJ8wH2s6YgkKxhmVkfGN0TM_4g-q92nuvdCTpvnm0u5Xs0TbooL5DC1xBi5rkCqzEmV7X-WahzYrp_IG6BsPc22cti7e3XmJ_2vovEemWfU95uCGUGi4EYNT5TmInATE_qzIkYRpxTXloH24v83vupcm9GD5QQ6Wyqm532rznFBJHPJR9lx10xOULSKu3fGIkxFSyBmA5qDUE4WyF_4ianYsB5idL6NGGnJebzCJWAWlUA92gGUeOsY3bPcsvW9ZXuWE4vcRdUUHKguq8bSmHMHXwMMNCqPY2cU11g3b-W9hg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=eS7ZSNVnAY4EH8ey6D1GqD-risF_KZvsWUez9tljYwfnuHsZVhtAWRGUNGxBB5KnUDzwvsx8VPdLagglL4DeevCj0moxJHdVHmGv-uVF_j3oRB6dRD8aavqh5vKcmEkRn3YqGkNsrnV5AJPZtSPYb5i9yTgvdGSTdThQFxUVOIHgLKeM3mnYFA1hlXT4uX8dIPW-W2Vv_g9U1c6AnOsu94RWEm9eLXIOpUCHJsIuGik3_tiDnbvbIjLUilV6RizbYBf4qWqVtcV5pgCLkdyCwTFKpKP6TIiGdoNmEYt8PLMQBIzEZqbdIOaFULNZOStRPkMb8hs8Jz2Il9w9SSlTVDcF61mxDWr5qjgsX3psIEytbIeGiAblyFkG0Xx4qdE37dBBys4PcQPPXoD98n5ZMtlVwkzQ4FbbUnF1Ddtkt2P7_XVkpRI8sUfWwgb4dwlVG-Z5N_uOCfS8EB7jlNQR4KzAeiln0IR4IdMMbi0AfHTbGOA32E3R3zBsBAawaiXknxyhgTGR4sOawZt39NWLVp5RhyB-SBRpepmcdK7GcIVj77leSPruwrh9FpbvDKa2F7hcyLf7YKBJCVzFRW_ntFozz7yixWGFEqwPO8vXoErfHqR2ZbVhZMFHkczeAmXYFqlvchPN6nel_3_bz-E7SqsM1f8a_cMSlfKhiP11iPo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=eS7ZSNVnAY4EH8ey6D1GqD-risF_KZvsWUez9tljYwfnuHsZVhtAWRGUNGxBB5KnUDzwvsx8VPdLagglL4DeevCj0moxJHdVHmGv-uVF_j3oRB6dRD8aavqh5vKcmEkRn3YqGkNsrnV5AJPZtSPYb5i9yTgvdGSTdThQFxUVOIHgLKeM3mnYFA1hlXT4uX8dIPW-W2Vv_g9U1c6AnOsu94RWEm9eLXIOpUCHJsIuGik3_tiDnbvbIjLUilV6RizbYBf4qWqVtcV5pgCLkdyCwTFKpKP6TIiGdoNmEYt8PLMQBIzEZqbdIOaFULNZOStRPkMb8hs8Jz2Il9w9SSlTVDcF61mxDWr5qjgsX3psIEytbIeGiAblyFkG0Xx4qdE37dBBys4PcQPPXoD98n5ZMtlVwkzQ4FbbUnF1Ddtkt2P7_XVkpRI8sUfWwgb4dwlVG-Z5N_uOCfS8EB7jlNQR4KzAeiln0IR4IdMMbi0AfHTbGOA32E3R3zBsBAawaiXknxyhgTGR4sOawZt39NWLVp5RhyB-SBRpepmcdK7GcIVj77leSPruwrh9FpbvDKa2F7hcyLf7YKBJCVzFRW_ntFozz7yixWGFEqwPO8vXoErfHqR2ZbVhZMFHkczeAmXYFqlvchPN6nel_3_bz-E7SqsM1f8a_cMSlfKhiP11iPo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJVRrMRlJSiZDuqOoswbm5nAp4JqOV060Wsf3YGXhPXe1SpBH0f8NkiLyAdF4yKkjKgujr3SXo_X3rYtIgZSmeXLilWwEx0Y-9ORAt8KqziJWZbxwNQO33ELxQnAIEGUGYe-YuDTYKclSVrvY_uUXfS7Li-ACavwFGacKOdxEj_MH9gMbc_tEqeEkpVso3uOV6rdZNHFD6xPV4X04toaKN4GpDpRDgx1inWlvBG9tKopYP55V5MLBr6XIpXjQQ7-Av7yeQykWfdLXb1EBEpbh3C2_QVouPZLfAS4LTL4O_xXUGUwqi5ZgjXe2mUjVvKiGHRPtLvsL5ZJc_Y_kBoPaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=Fqz4Lp5Ds0UH0dUzt_n-ErNpVU0dBpTRCNG_iZqrrE9ov1c0p_oVPBgmV08-R_T4ZO76Jn9mOxAcRTtIYhompeX0wTayc961s3vrOAFSS_OAJHbuIlcO0XnDmxKtm9QbTxmDXm8aphwzji-54hNVU0CqXDvWPPGHz75cc_Jr9CqpDGmMqLzKe-YJLC-xz15LRArsu-9JngVBZgfb12C7MUXnoaupFYdjJ3A2TxNJn82vnOtjLh--6xBe8vewh75cVVaLXYAL-6Qt_hvHD1MO9LORC_5WgzA-SnXRsolVITt4Q5nY0pqouVF8qyGlBL7wXQLHw1lB1syTZZTTgxgr-I1MPuCnkrMCMgjUZoAFSc21ETP62J8QEdeolKu3E6-UDe7225Z9bzN6pimM4esJdN38nfr5O8imw5G_Zpn4-6r0YoJaT02pSaU-8-gC43CqkehkB-ouzWJLKNKoK4o-XwHP7wKJT0xAdaIv48dwU6KS_YXfWiO9kF_6vlditDifSNrB1h4dJSx1tgJ76wkuvKKWA3Lgk681JNxu2zA1duDyrknPbYKLQmqqxMEUbVVaL73S9WmVsDgx4YrGMdhzMDP-cdjpQAZHqhGZQB3Zn_SzgJOqb0oDdL5p9tmqQCX50KqqfcVN4l3JoF7OF1mtMn8C5fIllEJ9ZWL5EHUPcn0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=Fqz4Lp5Ds0UH0dUzt_n-ErNpVU0dBpTRCNG_iZqrrE9ov1c0p_oVPBgmV08-R_T4ZO76Jn9mOxAcRTtIYhompeX0wTayc961s3vrOAFSS_OAJHbuIlcO0XnDmxKtm9QbTxmDXm8aphwzji-54hNVU0CqXDvWPPGHz75cc_Jr9CqpDGmMqLzKe-YJLC-xz15LRArsu-9JngVBZgfb12C7MUXnoaupFYdjJ3A2TxNJn82vnOtjLh--6xBe8vewh75cVVaLXYAL-6Qt_hvHD1MO9LORC_5WgzA-SnXRsolVITt4Q5nY0pqouVF8qyGlBL7wXQLHw1lB1syTZZTTgxgr-I1MPuCnkrMCMgjUZoAFSc21ETP62J8QEdeolKu3E6-UDe7225Z9bzN6pimM4esJdN38nfr5O8imw5G_Zpn4-6r0YoJaT02pSaU-8-gC43CqkehkB-ouzWJLKNKoK4o-XwHP7wKJT0xAdaIv48dwU6KS_YXfWiO9kF_6vlditDifSNrB1h4dJSx1tgJ76wkuvKKWA3Lgk681JNxu2zA1duDyrknPbYKLQmqqxMEUbVVaL73S9WmVsDgx4YrGMdhzMDP-cdjpQAZHqhGZQB3Zn_SzgJOqb0oDdL5p9tmqQCX50KqqfcVN4l3JoF7OF1mtMn8C5fIllEJ9ZWL5EHUPcn0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDvD4vIaiqSy72QFkMgljaa93NlETcHzsSx5GavLjD7kZUaFFKM3GzrmDAxlfTRdDzF7cp9-T-zTycV9drTF5rMIZqY53DcvXl1HSntqzWlRWttM6sc-cStp9jYli1k6sfp3naXeDiaU08SDQQ63a3-tQiTLfXl9dfixK2yrks9GjASh_ios2IkQ9QU-H42X43ekOzePwy4phKRYvbwvumuolbtfW5wfMSJz4IH3GVZbS-V6NvoqFmDOCdLC0ITlYjZ9fJgMM-PIsqhBwedTAh3uNpjW6wVdhVV3-r1A2f6KEHtAdn8zrJAvK0-4uVWfsKHBvo4ms2wfvXLjJb4FTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIHZ7nCcsMcqRiSpaBKG6uISxCVwfMlfbRn1k34ytStLS95aHXeV04vTw7yvuBZ320orbszP_8uDV7qE1MQyaO2hvxYPl2JTQJJLjXDFkqUKoUOJimS9kyvAu-UpgUs20QwqGf1cGjtl98PIJTJi_F4xhkzc_3WiVOPUYeWPDP06Bm0Ifts-4JuVYg7-Vd1m9AKhrIfb4O__WtcmvR8KaaPnyUaX2u9DR0YXF4luD1EAKX050lsfzGpKk1ui1u6vfQhvobxXbhcTBAU-0B-7MTVeLBmOJofno7UeTfP4kNdxf0_1l4sX7vCqmVKrdVaBwELi826g-LyfTd-hZscsdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WV1ps-srjv3_ItxUgzKcOY0_jJEqfAZ-XfODhC1R8rctRxTnOCsDwNh2ZKPUKhAHOiTnRSxw84Lf_BrhAZu_xJF0OWLt86bBq_0MOfYh8v5t1LvQrF5h9DLyGO_r-30nz0ygX_XYiesTFS8tEYrFEiO2Ae0MPYsDmGls7vGTxSQzHJUTsfhyl4q1Bsxf6QOSnZxqsPpKOYRG5jeiuKqKuxDbViqMpxL9566aR4eozrdyjZGUkfm06It72ZB8548egFCam8PwuAboLGpJZPx0Uspadn_Cak5mnHps3hkjALkxCLcQb-4cNyztUtm4J4dT3YpGQKHwnWvNXBtZuzfwbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNtWZaOamUaWbdLIzLqbyOom8xw_LcTctGb4wnqt8mgL5pliXGNZ4jgXSqpL08cEycwVSrJk2ZmkVZb6HYoIg2CL25fGQpv0NO9RrpCctPSxlv3ZUT8gg7kL2ifoGxqTbRJ1RsY-ie-LyErocE3UE2mZYLJTnxFGeuWuPgvkQ7Q4Xqm9WI4LTKgtXXZm_VStz8YoS25wKaSDK7rMNWPSbjItbJ-m9wxncRmBZIrPr2HTeP7BBvLBl9cBV6yW6FHZ0EVWYPiGz9Up9Sdwvu9bJahjgMja4wMjD_gLDR2aUQvfT0SiqvwAPrNFRYe-AfNCiJOdAuVHhT-J5mEfU8CBcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjPUBfolVgY8vnDazPDoeSciJ4b6sFyGSEbRsJvHcuV3GDoC-PzLUHur3Mh5pUetCTb_TuE5u9NW8dwASSTqhN4zWRhrWkp6dH3mfMHPh5YsQUmoxYUftVsOnnEl9jqDeDUISc16fB6oGRm7TsKQ2hEp3b4_Wv1lyXP-N7PNLAQ7IWjmJ-ywxfhJQl7Ib0zeKw1_tLBBNxsXBtldpwvX_8NN9UdrjSCqgqKtbO5dp4PWoy6sYxdSSWCCammAyqvCMm6X2pV4Nrpji1o07yZqltsYbnNYvTMRSLGQFZohJxPnkfa7OllOLV3_6yYSpavojEWCL-AwQNRg0cGY6G5y8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJsv2IPIq1xy2HE1TM-jmHqg3RVJURC47T-9OVtvWYbiB4LUc7j8_mDGLurr96jfTGvt96OB6EX9ECMjz9uty8qobMCDee3-S4TXBJIaIxOu5i3h5iaADM12776JHXpNTif4X-pgL3rBsqI5o87FEauPMAZlnC_cHpP8_6iaIomBRiyHjHprtzv61QbmGWBovrWFn92VP5lhpCS68G1Z1qp8VY8cJnFrF5qqTG9gdgA9_yNRgf54KEEG2DWOpfEyo1VB2b8HBSa6UhjxLBro325oPH43CLLt1l1OlalrtWdjF6ijycwkalXsphzLSFU9BhjNcW-nn8o5EPLtwLQT8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3bJf1W0xfBY4mICMOxg0SIAELwRgKSOsWmD47AgjQK4H6coim-K7zYnMo-GTIz62BjfUee13FF7-rDAUbXraxh79JSEmG6jcv3bXicbjO7IU4uIu8P5XsEq6wPGDpwWA11MrgRgV8gwoS8JmBdKezsuMSU6sqHB6C7jnOn7noeUDVPH8_ODoKyEyPwjZrni3_G2xpWRdnFPrB_bV-IN3WE_aU8KB2hf1a51cnIycQ90XEeptBiay8__lsxYeUxZmVHbjPj-EfArhLSTk6UXXDX5clXWg1Xs6B_a9hxZy0nDLqK7qR127y1slfPxGUML1L1_ZR3GmC94ZHHaN_5Tuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ns_s93CtYnw_uMp-zh4wlvDYjbeLV9NQqXda1RDlBeMPT5QVyOQZnLKSlyQBVYWR73xiyw_LPtKmkUC1ZfFZeE-zQ7jT2GceZFjvWAaTSTejdmCEwSZkBJN0IfYVQEunP_NJrd3KQj7c96pm_xIzcyvvxERhfpFcFJmBoIXk7CVKt0QmFb8_EhSJnZCqWjzc0D9aT_heQWifWgjMCV_V8a9II7WDYS931TqnEEtrf_YXzEBoJTiLA5MCBkWi1xwNzMQH1hxCiBOXOQRafpI6Tv7ZmrLvhHihNM9ppmTL8QwwAjSIL6bxyrUMN_KLxDthLJmauApSsi5K1sx0CVZD5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZYdi--qqqJZD_BdZVhgQl6j1QaHKMD4q8K5HPr-Jvn6K04cfUU0dqll5d3Vn-nOsI9Vesyxhp5AUdcxuwGCFA_I5XfgT2NauydXHNzciuLTtS9ilyvlnUacCD3ObdGhCm3K7cDDxVhvDcB83OdCL8nKvFWK5fdR9XMeQMBmsD_ah-toyKwYYjAc19Mjur6bz7Ecp14q2I_ChuS76PLCAwhk7EDQKwVqhyaRa2sqwmPOvboB9zZANoVPfiV4Mlg3IeVD1xU_3ZF7WH6DR9VUH5h6X2uatY3Wl1AoqXrjs4AMsBMmmcbMa7oYB_OKqFjVoT-uOp34DriUQMZzTJ57oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfC4VFnZ9Q32PNf8n0gNAhJBJ5wnS55zC5nhxz9-1hFpA_ABx1I0ki4x39fffRZ-gtjhHhtUhKh4SYlhI4MxlRNV7CDwqJY8pfecCgf8WRtm1sJMXAOjp-gA5U0ZlWrUwCupjVeEFyw2-asr1pPaoGsl5xTGZqrqtGya903bPqTlH_ZEHqyiKlirIlvwtxy_n9tETLIJmuAyjuVgxHlLUVHR-yqkmSV8ctG6e-r8AHMerptIAIasdeZIS60yppY-o2GHSmBG5627e3hROcaaaN51OddbcccKvw-_OXSlvbgX8vg7TJYrLiIvzZpfrg9_UHrqWQRZMwNNGypuY1-0HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcigqcoVbvpwx9Bv53nyKL6UumleT3Is1oIO-lenCvQu85w0jkIOugXeSIHbxe4-Rx5n587-uZUBvJ6BOeIdTqFi2AO6X9H9xCAIYRnETBDt7t0YjhfANjbl-PjxR1sJsEGzFcdU6BlIaOcTLXdeXKOVveF6ZC_L7w29Qjsf8GSSBMXylY7TdH4bZ4yJmaWFsKZ14MGD-cS7XeMlNbdJvrdxC4QpVbqDmgJFHKSnaL9Dzbr8tWg3KzE3BW3-eEVz4kFzShnn3-_fzddHddBo1L2wgWfgON846-F5BRa5xIb3upEWO-Ss9ISp3dFmtGErpwjYy-cwr098xQqt80B3hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vybp02IWUqv82MFnAgdWvNkGkTa-F4Je285KoR44Bdb2Ord-qANWkqr8L7DHwi557l3sb5dbwMKSRGnTcNl_OBhS3rMdquCkmgyUr9ZJI_7Zk3Nln9SWE1ysDAgEERVdibhI5-dnoMhXL_Em1yuQhk1KH6H42jzVKW-cQzU8Y6PLYoF2JIjucgdslqvM5AOHs-wdDmTDdhY-Ic_Z8c5sCE9BY-fxWsrfzE6CCwmV6Q32kymkRW5NQOWqyGPFCYSQp6C7MwYft5ATLIhJP7q1tZZ43rSbzXU3Tr9xmESptbYr5HSLqj_7HWDYebaUUIviaGMpHnluqWBsdEH3TLtwrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gf_XsuLc8IsVAqoHZ64PUdedY5Z0fl3T6sj-45EHMS_76siBQyHLq5cyoLAHQ2KAH2PWGacJgFj4EmFqQDl-Z0Ol82ZapYAZuv1q6O_CZLM-YIhJ_cRM8tTw0ttHCpgLzY_wuaVd3ff0dNyirad0OzWZ6Zg9wZbfBvPKs1MzMIVkzljTJHaaJnFMCHFDPp08xjqphxqg2jxoWdMzQooSLW0qlYFo3DAu9VXN0ek9itHvCcKUrLSysvijs3VSQbMiaiUeRzV_MP1517gxZFFETYHmmJIa9vqnRyUY_EheqOt51miDLJpfABNPHGAq3fgHHOaQqh0poI12RcsftyCLXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTkxGp42GzYKeq4bMIvUjwLavqYvIucrcLgDbu1RIHO_b9OhEf6auTlQI31x5ES9TwgsAieVyI3lLaxNH9wX-_IbhjHqOmLisG0ZhmyQymWCFdHOtjBe3q_RaaNj3LNm15Pbw6z3xN9VmvtQoYFqNHbMK-AhYKXkyNKExyp3LY8EHSl98a2RNgDK_1tl8axy-vE7ZOJJj7TPJslZrsF7kyac38pWtAeAGRgOeL2RY4R_rTs7EDofIIIKjImjz08TETcUNhiT1EqYY--JymlFbe66jBhG1IMxFoORnAUf9aMFwrkg41oaGwVeHOiEgCOZxEDaRTT7vgm2fI9AzYcQZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8W96EZu6g9KlpRlx6lNRadJffX9UZjhvU-jEIUF_kk80PMmEdq-Fx3iSA3Emmjmir-W9JVYfnI35iVf2vu7VHM-CN2XdYmv-SOcypubef6oMhCBOsaGbZEtmf_r-v7TDL8jwDYqFHH3wio3tlGL37NpYNYdtuY7wpjxTQgLK8ishxwAMld-bsVZudLmetkwSOCiVLF4-g0nnMLe6Dvg98azB8ib0-HFKnPw3iOuYaKaN59_7K3-wd-hUb1AQmVnj03j3CQYW4HDiAjrWi8KUv-8XEXm0J6LSordWd3MEKiEs8e1TbDBmKjRBOKfTLfXYZYlfz5LV9ocjVUXrQ_a5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qy1b-hsDvqKs9ZVS1th1AJvIkWGLiPyGRiD7aRNGLigcdCOJifxCJJFNwHRPmOjmmQ_choLnh-7y3XAd3zOk2rx7Wf7i7jBQX7BO7N7TqoQp1WS_F2xV9rBp45GSnxGhWvL5vLkWGGvlMEZ6vfvPvjXHUFO7UBxmleA5CuWFhJWxEwQTVp1BvFjqZVUqy085JC3qXRVRH8FfI0jhYg512qjemp_Kgw3IYMjvJBohB9HVBcHEMVobqPQpU97RHFz-Qo5wewBg1iSYtGJG4o6S_Nv9amUz1u7GgxvnXmJO6GQKW2XnuySQWfqeI_pH4AxZYSKwgHKueoQaYwt2-peiXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bbjaPpFsnvxUtv-CSUzuCsaKjf1fzGIuq1AIRZfJVtnQ13_WUuwl0rrYmeinO-DFw1T5_YzncEcQyW-68VlcKymK9UCgH0mQDgjbAH8VkbHqwBWU8Dz_jDTB4JnObXRDcFopB73u_RGnqB-BovFcEdIex0F7J7xQObfqFt26uJyLyQswUsW7hV2kbD24cwAHJ3-WxqCjdm2qNVNdX4my3y8bh5GYdKxly4EOvHuXwPSNODbrno2VKiTJv8_QCKsUkK84gFj_54YRMcrXX6CBQOYo4XuFv3blc-7D6ew-o2SGjKdycRanZJ0sFr1OjKyCqniS-BBguTl4lv_iUUP2PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fB84ifEv-5Cxk157nhI-87JTRvUDIgASNmdgZYZOmz89DeXWmXugF2lJh14D9ajBhiGkF9sDpfLuAZcrdv1r7wJKWoeyc9aD9ad5vwSfKImYcJOZZspx4sQmpUigVgUBeaQfWG4Z6xZqrglKmPqstYoICNHyt5SVze69jErktr7d5iR5hqxRgS3xwizCDs2LJvW1qW4irp824SEKF7NkM9RbVykKoqo5ZGU6x-4v3gBqLgkKeejbpJvyJ5Ff-Lj8MjDjFB21XG7rnUA2squBrCpKGo43DdUWcBhUqNl0E3Q_btIA7OZDeJ-4kN0Kpg1VKxmDgg5awCn5yL2WbTrVCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPb2K2Wk9EfdmuJ6_e--CBp36hMfZ6cYNT3nxUpeRQ2D49iIL_6A3JPQltgs2_TIhNJc4xGxFFX61Z1_AfbkSjuqjxcHJjbHZXlOHVPVcnYjjciQ3dHS4OEY-Wps2a4tnm2NbgpK-e9SKWdlLg0FYRZKajSqIru1qABR2E-ZUo9hOmg11MEPvt_15EjXSJ-uRzJDtq4yg-1mTtfGUwIC2sCl-u9Xdlvl0zMfgRV1gTnFP6J1lhfQD42-Q-BKZwd7qVkDUupUgB6a7LZqT3eY8L9ZmztsaCRunWZxDsz-lTrrXZPLJST15rvBE3rjG1NRrOcTPPIjp5qvHzcrO_KcrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUVb67IsNYypGHtaXgXj8T70jXDxn-B9gJx6HJd-QtxM-T5QlTjRewtoxSO7vXXJcB1LJsCFDou988rvyKDrYuSxxWgo1oW9zK1mPnv12-nbb46NDDmyP0JfO00mRLTog1-zdnNwIbqGultX-b6s0UUoL9ybqGR-VHvGYg-FS0sDfrr0oG03M2fEa-YIBd2xxfFaIEp1ZzuUlIDgPQD-FafR5guCBxRoYX5pX3kGnB_jE8_o-2j_obRUbEOFORX9weaRRa4SiCWMPsX-BV6SYC_xvEajMzvwXDupvi1P6RNNVu-2As5oLW52cnqHX61pmOMuy4ygRZUGu6uj6O7Ztw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PANFQ-3lByMH37hKBOLf94dJ6cSvT_JrXzFP0gZ72Y8p-INE_tssW0YAtWOCYDzJTs3hGfRexWzS_JLS8bAIOtui1exqakYE_cuhpg3V39xRlVEL3qNRv2sMrmL6do54LB_e73qGDeYwyyhb5NpkcyQKzWbaGY9AKqpRdoTiQ90Kz6Pgf64GBjlM6DB45PNkKBqRkHSzvVXZwfcRGK9edqZ0RMHvE-AXa3GbpKVRqcnltM-CXh-YH9ikh7iD-Ew87w0_GR15m4lnqd_Nxv6HipehZ3uHP99y6jZfu_A46y6PiYxX37mHS1UoN7HYmcaLdKXnCwRfcwnO7m8DPZKcDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SH4xJEjdb2DXXWGn5l8SoSth3gmQcHwLAXoLLT0vOFDvOrxxqBwZC0qq0fUh1x1L6eox117yYPXMQIRYXml5n-lZCPqKXc_J9u6GkDn107_HQ7_rrbYb8BkDN0qpP-nCRcsNa7x2ARdrQb1u5xjYISRy1mCdwnnJqWDJ5j8J7j5_D0HB4cPYmlgEEmjt0EpOJEz5bPiigaWxfd73FutEWb6Fi3U9fgIhB9iadX1q6eKvfkR0-omrh0ujzLzKznxCjR9roB6q7MEiHkXbN4RBUrwfB6F9I8zHvf0H8pUpr1-C7wbcLQzwPX52g4ZQyk-r6DScIlUR68uHmTKYanmxPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9QCyigbtqNA4mhbDB_z2d64fBLZGOlZWCFtxyiHpyLb7dPDkMFyrlDfDEJ5AhtvZ2ll0oaiirVUsXYZjsZd0AqimN92jcaG362FtEaohvIcpQhK-Lz0rmatct4vq_izX1fo_nqQEp_WWXxFJsKm-OcgYjI7b0hKZ5z_cRQoPZOaRJkpkGwPQwt-ygc2nv7SHSYtqqpvkIBAVaGdHlTBC15xrMZmAi0O53ABkfZ8qw_J8Nvag3QheQoWcyA8yZVuz41kaigvZCfQP0vJU5Va7cjJxV4XWYu63aPE3mY97GD3NGW6Lkz_mfJBNKtajz8Zida-09jqN3gynd8IyGKOeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWjn7wxS9hZLmez8e53NhAz3gDh1fMM2Ll42QuPdYfkrhTmpSVS8VztAX5Dpr4Ez8Wx19k9Tqd0FmIajIt4nyob3GOQ6GlfaoQjka1O_z7MnYdoPxCSGYQtLdMaU_W5BXn100wkhn8kGvzQ9XWy8LFOm9nSdRyCDTr4DYHupcaQ42TPhpEFTlqauHyJjx0KUOE93XfwI2QDAVbcAcyMzmgwVLAuNMH0PelZJDXV1uHirkTxRLcU_T_MaExmDDbge77dO4xjr8_nnaEqaBRp29iXFP97OptlcTbjvbz5h7Hl18McFmyoZPa22F1c_qshI1CbC-6aCknLkTit32bSQnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfaihboYnuDd1GAnT_l72UZ0ViQq-2LLW4bqoQ6WG7sJtrgjiGaV8rKlhm0T30gKxLbruKwRuX1ZcSZISqO-H_GJXkkT89tP0IdVvSrMYoRzIY6lZzGywdG6R0rDjH2y-TQPtXMeGBf3U3a0ayywU5aGks382WcCGN1eCR2FY5CDt_neTRsw1clGBQaQigO7rXgNexdEAlxNNlU7B_OfQYh84Kb9Pq_Q5-A6RzhUO2VGsTmE5jFf2Q37SMtMUUMK27DkTMaw9PaDwPh7naGMFuKdDhQyYIrHCf4f-WAzU9QwlGvHHFFidPybKUP5p78D3AxwUZlaY6Eu8ZBbILlj4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWk3RT7DRe8AbQQPJA9IRYeNtMX0ervoKyf9e-DP0OcR-pSIFRboO9C70FoxznvgawG1_D0Xf52FkXEo4lSOSnapcsdH2JJyvcjwh43mKbvN0hzd4-V55_i7S5pM6XTP9y2Cx1xJnnOpJg-4Jx4nuDzCFA09gfYZqByYDGMRRgJpFT0ZJIMoyK7BSCs0vEZrkXDJCLWOz8kwELqsJe7GaeE-xp1XBOsSHzwDNVVUqVbhlpyBAvjVsYrKSET2KvLD6kyKM_Cn-5m3JEIBKahsmYXWlCbRWs4P_b2QZLyNyzPfrVJAjH_w2rMHy5uLA3Wmt5r3snqiTz41_JTCwrFWcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kl_Ay137UKZLR4GbHpojencfqtlBedqt33CKaqnWk7ZmSvxDlsrnhaRDtO6NNJNS82LDmkzW7ji3udZqndwLVoH6zrJmU9ykRkUVmpslMVudtyY6whXJbwXZjNQOj91YRsgssef77i2loxSb-YCCrWqwE1MLLBmiaKE7gLcSL5VXPD1_KkFZMJH3F7uikyuQ3EJaliCkRWsa8dGVRS2zuU1E9TEFXgjJIB5Qxv0hdCDgSKNVpRA43PX33kVk50KDVMogn9QIaQBFmuTBaZLNcfj3XUGHzeADuBhRHJXVIuu3X-k5ekzeRtJbT-33z8dWfothRaKBkBaUOK5jFsWvsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pm1RWibjpxXkVBOeQ8OTZ6RLK8gwA-75qQixPVqTSET62nfl20patAW8WIoeaOEj_vJsUqKKBiop-XhegFU20mzaR_CoujWpYYpELZSL3Wl9Q75EANiGV9_YYSnAYexP9jPOUlntbz_fOBPyHEfxyEIB2DmvttX9iSmiv1z9HWXXbNgZyWyF0GxJgKqKEJ7x3BUkphKFahRcqQGYEu5ud9aR5jhPELptjq1j4nkdjbiaXs2B9b0zSXez4d0Tf-T3vMuN_RMaHIC7Btuy002kjwhin_CTDLD-EEF-NT61QKT2UQYpEjNDq6b4YtiD37Fs9uriKWwgequ0OX_n7a6Ikg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuwuMDcfNERvIBgGeekE4tdpAdyOQKWYEnZRgtwHutLpYK1ihB-31sURYnw_6HGXKhj2Z9blTcMB5dTHOjju4Ixn8sImZTMmplBLwEToFcEPIK-Q0x_qj-6Zj1gXEAHzCyxuESg8i3BPgDL9O2azu7Tfrs4xYyiSVTIq730KNOk6O0Lq5sHksXy0aoebJGwupZ6yrx9yBZYSmOwGIjBtrjlm1i7cGgbMIAvbSMXPhuVR2HZScl1jEyHd6l7a1nz2KtlrwFFyJicwHdOBzo4r9rLewbBc1pMkCxntGogHJTxoDsNPmzxyjO8WT1GPH7Hvhz7Qb00ZlpoQ3TLscMUUgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8B6lukxN74Et4f9GTSfKNi9_A6cEClwNW3WfWhH9sTtL1TBXI4dHxm5s2-OoAY7WEbMypyNKeIE7dbTJVd0-DjeHOwO6qyFYl4CcuMPdFqqoF4AIlB26nk2baZkaUNov-omslLs4w4-GEPOvfULnCzr0XQ7rHRh-2VKWEKr4Wwl9VkXKGR9oMbbQ2nnBhhbzIhf3T5OxP5EnLCUrqV1UkNGbjjngttMKr5t1J9FD-Mkq7jyNaoAoVBp5OjeXS_hYnj157cSKFOz18r8NZ7lOLa5c83ALDuwrtZah-VYQphexmsGtLJKihFjWvdC0FKLabwsR_eTQp4rUWSRjjQgnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_fNjgk8Nrg38hfp3mLJOwr27fleIDhmeqge5nlDDw5VZsvYrC9HuMQ2g-V43982B3LNbc_8hsCdNlJGYN3_zloNU17onlkPzsvZ5ot4gdKBj-gIKLQ6NLJfTnFQ5mHfYYYOzeRTI8C1ClHRmqpai7o7WJvEBdau1WGskhLAE3wpnD5A8Tx_LNoHHoF7WHgjtAFAFRvgZIuXYgvI_J_gqKRed2qOn89O56r1FDf1wTCmuENoSAq_yy5LulSrV9UTs8La2bwXrhK2Kygs6cHJ6EbmtSOGmWbjGxJZh06U_uZQu1S4-am0ce6nqq71WeNvz5WmzYZMzHgKaQQEcyTclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ne8A8iPbqU8S7aAsabnrIKHQTnQmrdMczxWkMqlpIhH3jUqw6xZY06-XdTMWJM9Juq3fAl_z6RWlQHi8ALtcktcPWgBmufEX2H-inGuYhuT5oowy2rfJewmoXxG12ZNltaNaiKfm0OfRfRUQYJMvH6fOBPLU1xBzab55SQJ-mddeSqr0cXuOgbtQ0NL0MA_kDIAPFMnzA05zI-3I-IPitKGikuyEK0M8lNHoMxpTxVyc7SQnOeALaj008IPei8k08haq8is0cJJDvssGLymoaHDvFU7yvX28-HUUcukwfNvZPU8FYpfMs3naQMC1dln2uWPo93bSuxOki918BIfplQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKZUhgM24Ew6dfy5kuJZzcQSUBZ9CF9O5HXwgrwUf4xnlCgp4QvhYa70X_i0FZcK-e_R_6y8pGCaxnAzJ-GmtNSmkSeSmMbAO8Fp2iD_int_X5FHGP1pJFQdODF7NknR8bM2lb4H4DCSAn3xmd-Ouig7P4qLliaLrMy_rd_jmATh4w4p5rw0wwvXWIVJ2yvAwcDVl6AqZnZVRaJmkAA_5W6alTtH5HcZJxVD1RzuIuHLUTyrGjcI2PPAFamqvL8RZyNHs-uE7Gm2VuXt6_hAGfqUWoYxYlyLivCq5MvIrmdmEmY5w5p4Gs03OtHZVYQwNPhsXHSdtWRsnRZITFr6fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
