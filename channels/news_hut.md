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
<img src="https://cdn4.telesco.pe/file/h3vM_fUKgUKpaYxbpR4uK3RHcnHD6gfZFd0MdUIGVbVKyiPCU1QOIJlRPfwDa3Cl7pSzNGw7e4-PTuGx6moAxfaKLlhxqipOaMScn6vU6ci-B_ievdr3zyha1HTl3bVWxaEUB7Vi_Nk_2G7z4YtzgvvfDPpuOYAdio9ff4uhIxYUGszKBNcB2nDbOhNzhnzdfZCocpZCenho0Qyo6We8gONAvMo2IXwbRopfcQK7MOr1CCTLD1xAZSKwKK9wLOeo2LevY_38PzUKankYA9mZpkigkaf_MqpWTxfwT46w7HCx32jfqMA8h06ZtwTCe6xal9Qy00a5E_8ypvGCStsQzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 15:47:36</div>
<hr>

<div class="tg-post" id="msg-66762">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=To4u-jvVDYHzQoDDnANU81aIzh20obBBZHnyLhK-WdM-wXP1FnuYEt-3cMY-AOUWQDOiebtg4kY9ErIcXAOeqLe91ywSzqoYXloTNlMk0rnWP_hOpy8E0FRR48OwpLhOnzPUM5GbNwouLsr9K8pKzWzm9fKVSPgCkN_Kxnkygyhya7c5t1mQluriZZ0JZiw6z5VHPVY3Y2wbpC5kr8RJ7vWpSN9DlkWp4dlZ8Tq5D9i-QpfFMqZGY91YhZsGpXDOcxtoA2eYypLAmpSOZXzQr08GNI0Un6blElmK3oTQSxL9i6gxENWgMek4HGBWqkEJUkBAnFRJ3uU83YboV37qkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=To4u-jvVDYHzQoDDnANU81aIzh20obBBZHnyLhK-WdM-wXP1FnuYEt-3cMY-AOUWQDOiebtg4kY9ErIcXAOeqLe91ywSzqoYXloTNlMk0rnWP_hOpy8E0FRR48OwpLhOnzPUM5GbNwouLsr9K8pKzWzm9fKVSPgCkN_Kxnkygyhya7c5t1mQluriZZ0JZiw6z5VHPVY3Y2wbpC5kr8RJ7vWpSN9DlkWp4dlZ8Tq5D9i-QpfFMqZGY91YhZsGpXDOcxtoA2eYypLAmpSOZXzQr08GNI0Un6blElmK3oTQSxL9i6gxENWgMek4HGBWqkEJUkBAnFRJ3uU83YboV37qkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجری شبکه دو:
کاش قبل از جلسه تفاهم نامه یه سر گلزار شهدای میناب میرفتید.
اگه محصول آمریکایی کیفیتش خوب باشه میخریم یعنی چی؟! یه کم بهتون بربخوره
@News_Hut</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/news_hut/66762" target="_blank">📅 15:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66761">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/do2hMvulqIdUaDQY9EXOPIqMEvqmk_yHohOAjHYmeYR2lxk7NU-QWWJtMKK4wrHR7r-9ooiehceB3NlTsvsdvjjqtDZk0o54OdbtK0j3s3BkxevdnWnYB8khkMjWpv66P_3Eq1jr6mscPdTTdnthScLZ5qf2R1gm91UJ5GNRKBAY7WrFbVqaMu3BdEsSX2eAgOKktEWYuzvAbuxAKLg7v1ZS9ZjZ9pA3pwASsoHMsPpqsVyvdx0DZ3A4Zrsoelrww8xzBzzUxE_YH2RxvUs429vPp4OTGkUH7j8qmjdTSYUmWSGzRXuYexV3j_uKKi9VUGTVpNcPoVxIH3xMLe0rnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله دنیا جهانبخت پاشده رفته کربلا عرض ارادت به امام سوم شیعیان
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/news_hut/66761" target="_blank">📅 14:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66760">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcTN8lp9HAn4rgKtG_kdqimJETHVUzWGje00fVLmwunaek8yMPZinYpqBlzqydPJqXJ9uc3KZP5GihvyAlCLZF2nl6iV5YZ_mNm7nIkLHyRdePfXA0S7A6K5lC08Xk0klgwTl8AA03b6HJGbFKgUuQODcicrepMmsmBLhlMAT-vdBHzXspnKGJaNi2bp03oy7N4a1UQ8aUYV6Qg9o8q0pnyBysP4YLj4fbtLEXPB-CWtH-3FaRgEPQ021T_eMdO3d64WitWuVmqHLF7SYVLxTZ1pxwmZERY1Y_P0J_DEFd_BhE2IVIP63sT519-a2xPnTm3goNRmUD_eWOBZ-g9iyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران در آینده‌ی قابل پیش‌بینی به آژانس بین‌المللی انرژی اتمی اجازه‌ی دسترسی به سایت‌های هسته‌ای مورد نظر خود را نخواهد داد. چنین بازدیدهایی مشروط به پیشرفت قابل توجه در مذاکرات است. تبلیغات و تاکتیک‌های فشار بر محاسبات ایران تأثیری نخواهد گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/news_hut/66760" target="_blank">📅 14:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66759">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=bU8RsgVogYP5B4mbAEsTS61OjAyE2W4dy59AFRuBap8U9illNdrszGBBRx_QkEdIqVuKKfq1jDKfiea7mqJCH2XKcLHf2694lKLnwNFKc2usNDFq-fzCrwixSD7VIXHIRwQH5j-5l8OwMjWGaCOidaqfxTa4P37pDrfvl3g2La7KvEt9SjwXA5tZWyBX8iWhz0yK5R9clvVOj53fVRyo4vBVb8eaiZgF-EM28LU4m_5df9N9G1MsG5Ye8kKxg6VTLBLByD_tlZCKucPQWYsZQclMwrRd4hTaK1Zi5z5T2GsHfkTfunPJWXKhFbZPYcBkXfCIzEL33Cc0VgmDp2r13g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=bU8RsgVogYP5B4mbAEsTS61OjAyE2W4dy59AFRuBap8U9illNdrszGBBRx_QkEdIqVuKKfq1jDKfiea7mqJCH2XKcLHf2694lKLnwNFKc2usNDFq-fzCrwixSD7VIXHIRwQH5j-5l8OwMjWGaCOidaqfxTa4P37pDrfvl3g2La7KvEt9SjwXA5tZWyBX8iWhz0yK5R9clvVOj53fVRyo4vBVb8eaiZgF-EM28LU4m_5df9N9G1MsG5Ye8kKxg6VTLBLByD_tlZCKucPQWYsZQclMwrRd4hTaK1Zi5z5T2GsHfkTfunPJWXKhFbZPYcBkXfCIzEL33Cc0VgmDp2r13g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
یادداشت تفاهم اسلام آباد به اعلام شکست آمریکا تبدیل شد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/66759" target="_blank">📅 14:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66758">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b87jU_tvcpJZwuIr-YWhNCARNzjCraLgy6mhFH5FtDG8msJ8YbT5B8qp784Vmn9PCQ69g5CMhZL3My1HISAb7y9N19IDeZJulzN4rqCNWrjU5-e4JrDZhQwg_nECpgz9cdAGFsXqiRHfr2tyNOR1ns4ZDyO7Wqeg_0mIlZQDPSqnnxo9zXRsdURujx91DWYUPnC56AkP2NPJ3pUEEcHMeXaN89aWHD1qzuCMZMC_TGDyd0_nZYchi9p4Fg6PLoWzdlJYvqecC-fbqsHF5eNyhcDw2-uL4ywKquYtfBwlWp_wqJ4qfFpkgaBP-QAa8bcXoF94vnd9cquyhfQ35orUTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت فست فود برای دو نفر، قیمت سال ۹۶ !
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/66758" target="_blank">📅 13:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66757">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=BB0_aFOvEXcgPpEDamGZv-L_bvw6gxvJT62vvg9oLbEBss9qoMn-Tm3UgrJXNbmK2H_N4lRgfgd7aVZaJlaay6cn5kHo0c-4b4YUfLElBfIRQSgyxWwYh-_lVPOJfBh1yh2os4Qc1vUKVX2KUbDdZ994rlLRA1mANm97s8xlQY5lI-wY6lwOn6b9bqQ0GeDm9HhzwQUSWOVYHEUo9IWbrMQDfLbCQvozf9aljMjqYtl-pQ_Ymsq9-HHVSQciTYKeVxjP3uioKfLcNaqZPKJ9ZHVo5pfAU5t8tItlvbZ96c-X8dwvIKvdS3_2hv_OrtJhWWSMKjN7ab0KhTRyxS2QSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=BB0_aFOvEXcgPpEDamGZv-L_bvw6gxvJT62vvg9oLbEBss9qoMn-Tm3UgrJXNbmK2H_N4lRgfgd7aVZaJlaay6cn5kHo0c-4b4YUfLElBfIRQSgyxWwYh-_lVPOJfBh1yh2os4Qc1vUKVX2KUbDdZ994rlLRA1mANm97s8xlQY5lI-wY6lwOn6b9bqQ0GeDm9HhzwQUSWOVYHEUo9IWbrMQDfLbCQvozf9aljMjqYtl-pQ_Ymsq9-HHVSQciTYKeVxjP3uioKfLcNaqZPKJ9ZHVo5pfAU5t8tItlvbZ96c-X8dwvIKvdS3_2hv_OrtJhWWSMKjN7ab0KhTRyxS2QSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤯
بلندترین پل جهان که به یک آبشار عظیم تبدیل شده است؛ شاهکار تازه مهندسی چین
تصور کنید روی پلی ایستاده باشید که صدها متر بالاتر از کف دره قرار دارد و در کنار آن، دیواری عظیم از آب از دل کوه به پایین سرازیر می‌شود. این دقیقاً تصویری است که این روزها از پل «هوآجیانگ» در چین توجه کاربران شبکه‌های اجتماعی را به خود جلب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/66757" target="_blank">📅 12:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66756">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=vagVfZ3GSjo2VhGwbX4vgMkw6MwjNjB6oK-EeSCmMrU3tygpzvid417b5Fyno0ZN0A7QWlgIQRvHcXqT-RTswoM6bMEltCkKc5AMwyF9QnRKwWoTBhMj9eGl50JnlY8APzNLs7oQ0lJpqEy4TkKGhiDnRhSorpgr6B8jgl3vNmjKs4paERJJ-7ZBV3tnsEe93mYaWI5VHmLHuEqxJsLLIc8fduSVUAEyaK_qHJnBAlYXKBjstzVmSkz0DY8fX18XkPuKkiYG19Am6Dy1b0risNbRMTVnL3Z9pcBJVI6HeC4J6PhUvQOXKGsxLoaYhJQM80i2Nh1NFcVY5JPp4-sYPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=vagVfZ3GSjo2VhGwbX4vgMkw6MwjNjB6oK-EeSCmMrU3tygpzvid417b5Fyno0ZN0A7QWlgIQRvHcXqT-RTswoM6bMEltCkKc5AMwyF9QnRKwWoTBhMj9eGl50JnlY8APzNLs7oQ0lJpqEy4TkKGhiDnRhSorpgr6B8jgl3vNmjKs4paERJJ-7ZBV3tnsEe93mYaWI5VHmLHuEqxJsLLIc8fduSVUAEyaK_qHJnBAlYXKBjstzVmSkz0DY8fX18XkPuKkiYG19Am6Dy1b0risNbRMTVnL3Z9pcBJVI6HeC4J6PhUvQOXKGsxLoaYhJQM80i2Nh1NFcVY5JPp4-sYPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه سرباز روسی که با پهپاد اوکراینی روبه‌رو شده بود، از اپراتور درخواست کرد که اول دوست کنارش رو بزنه تا بتونه سیگارشو قبل مرگ تموم کنه
اپراتور پهپاد درخواستش رو قبول میکنه، اول سرباز دیگه رو میزنه و بعد سربازی که درخواست کرده بود رو میزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/66756" target="_blank">📅 12:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66755">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=BHx6sl5oO_9B-kGBzq0g0mlVSRZxdgwKmdM8bR0_ItY3ZBCM7CyOY43BAOZN4Icod_XigW36FgV1sfeh5_XV4FLj3oYpviPV883cTZwy48eFc1cGgVoShjj9Mjzci8Drn9naEjjbe1L6qzgNmTW3NQB3WW4e8D1CVDT0pcWUs7g5FW0Lu4M6T3qt8zRpOk_hutVUMs_5l2wXsCQWNyOiO_g_WnY80w_5nxq114XtZXFA_ZfFXfWRNkrzsf5VPdl4DPM_hac8EWGWWdjtw68pgvkxFPNc1cBDMQNXeXwKKTYt4qYir5nuGKDYJnEMsXwiMI4siwiBlYGls_TimvB9NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=BHx6sl5oO_9B-kGBzq0g0mlVSRZxdgwKmdM8bR0_ItY3ZBCM7CyOY43BAOZN4Icod_XigW36FgV1sfeh5_XV4FLj3oYpviPV883cTZwy48eFc1cGgVoShjj9Mjzci8Drn9naEjjbe1L6qzgNmTW3NQB3WW4e8D1CVDT0pcWUs7g5FW0Lu4M6T3qt8zRpOk_hutVUMs_5l2wXsCQWNyOiO_g_WnY80w_5nxq114XtZXFA_ZfFXfWRNkrzsf5VPdl4DPM_hac8EWGWWdjtw68pgvkxFPNc1cBDMQNXeXwKKTYt4qYir5nuGKDYJnEMsXwiMI4siwiBlYGls_TimvB9NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
دیروز تو دولت اسلامی عراق یه مسئول دولتی حوصلش سر میره و اینجوری با منشی‌ش کارای ناخوشایند اسلام از جمله
لب گرفتن و ساک‌زدن
رو انجام میدن. میگن که این یارو اخراج و بازداشت شده
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/66755" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66754">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b320081976.mp4?token=FAyhCZgI98A6aq0Rb4gj1eWqS9pmjou_GmbrI8Oq29wd5OKMxkyCUzovnjRlniRE56w1HOXR9icSK2N1SgToT2G24yeNhbVhkzzr0Wccvrg7EjzIQmFI3VmdX3FGmEJh2L3we_MUuMPLpnU0kWPqMZ-00VzwoOkcsRfZILMNG9SH_04wFv7zpT4nAjlCtEc-Lqe5N8ynGkHNH9WiD7Oyi-uLKbJxwOznG7YFp2t5V1Aw8nsWy7ZJnNVNvzXbTYUHdbGzyKsX_XaBany2BDgZk2sb4dK8fRbi2ix2Sj8GemHSHDbGnjg87SphiIzUesHCyWi-jTZUvWi44GbJtcoruA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b320081976.mp4?token=FAyhCZgI98A6aq0Rb4gj1eWqS9pmjou_GmbrI8Oq29wd5OKMxkyCUzovnjRlniRE56w1HOXR9icSK2N1SgToT2G24yeNhbVhkzzr0Wccvrg7EjzIQmFI3VmdX3FGmEJh2L3we_MUuMPLpnU0kWPqMZ-00VzwoOkcsRfZILMNG9SH_04wFv7zpT4nAjlCtEc-Lqe5N8ynGkHNH9WiD7Oyi-uLKbJxwOznG7YFp2t5V1Aw8nsWy7ZJnNVNvzXbTYUHdbGzyKsX_XaBany2BDgZk2sb4dK8fRbi2ix2Sj8GemHSHDbGnjg87SphiIzUesHCyWi-jTZUvWi44GbJtcoruA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ای که مسعود توی مراسم کاشت نهال در پاکستان بیل رو ول نمیداد
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/66754" target="_blank">📅 11:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66753">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44438818f9.mp4?token=gebWfRYBtenaQGWCCe3qsaHkR50w-C8hFHdDyKdIJ_Al50vo6PZ57QlCs0d_TPnflZdONQXJ5ML8OgryIoFQyrQZ9KQbf81Zc8jzJPNd78u3KtDk-dBeSjsfpkuyxLnnRUMsRnBBxIzYx9ircmB5i5N5B6qKsEezbdRywNPAy4nEGSN4VBs6D7Y3-Gh6ae89OEl7xKAKm3L6Z3aB63fG8VMdCkspK5tQYPxPuCy4Gnqf9Ugkk2my7cBsmERklcesQ1_RUrULUWI93_G-2ic-5I59cx1g41odToe6L7_sqtOplQ3qSzSkzosOEPGLbzpxpeX-YhZ1TRQjKxLE_EcvmGsh-lz-ryNxsvHNkcV1dm9mllfbRPwtvym8FHdmHDdhsNsAhZpd2CW5PFkWhz3YqFejFZ1gMpD4IL687U-NozG4XYuTLXP6Bp55YDHusMusRpWJl2s2jfzgKpN0TXYIM5b1bojJu1UGko4qGdKNKf3YLNv030bjsROajUr7QNkXVOgYvwaYg1NT4v7xI3Ej6EM0zO1U4YzuJNt9g45NfK2ucjcNbUcsBqObwI6otFnaQUxjbrL9rekOZBxx-oxJwBJU8xEB-zOrTr2sLMMTES8Pc6uL9GcYsod9wG-7l4Lqn73oC8r8WAR-3Ogz4z3IIEsVzgUR12cFGlBz5dXsUGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44438818f9.mp4?token=gebWfRYBtenaQGWCCe3qsaHkR50w-C8hFHdDyKdIJ_Al50vo6PZ57QlCs0d_TPnflZdONQXJ5ML8OgryIoFQyrQZ9KQbf81Zc8jzJPNd78u3KtDk-dBeSjsfpkuyxLnnRUMsRnBBxIzYx9ircmB5i5N5B6qKsEezbdRywNPAy4nEGSN4VBs6D7Y3-Gh6ae89OEl7xKAKm3L6Z3aB63fG8VMdCkspK5tQYPxPuCy4Gnqf9Ugkk2my7cBsmERklcesQ1_RUrULUWI93_G-2ic-5I59cx1g41odToe6L7_sqtOplQ3qSzSkzosOEPGLbzpxpeX-YhZ1TRQjKxLE_EcvmGsh-lz-ryNxsvHNkcV1dm9mllfbRPwtvym8FHdmHDdhsNsAhZpd2CW5PFkWhz3YqFejFZ1gMpD4IL687U-NozG4XYuTLXP6Bp55YDHusMusRpWJl2s2jfzgKpN0TXYIM5b1bojJu1UGko4qGdKNKf3YLNv030bjsROajUr7QNkXVOgYvwaYg1NT4v7xI3Ej6EM0zO1U4YzuJNt9g45NfK2ucjcNbUcsBqObwI6otFnaQUxjbrL9rekOZBxx-oxJwBJU8xEB-zOrTr2sLMMTES8Pc6uL9GcYsod9wG-7l4Lqn73oC8r8WAR-3Ogz4z3IIEsVzgUR12cFGlBz5dXsUGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💢
سنای ایالات متحده با رای ۵۰ به ۴۸، قطعنامه‌ای که توسط مجلس نمایندگان تصویب شده بود را برای جلوگیری از اقدام نظامی علیه ایران مگر اینکه رئیس‌جمهور ترامپ ابتدا مجوز کنگره را کسب کند، تصویب کرد.
«همچنان ترامپ میتونه وتو کنه»
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/66753" target="_blank">📅 10:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66752">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=Nf5hgSkTbPXQr8CPDUONdLg2ql-FkcyDKJdaSr7EVv203zJ7mnnXDu3vMtUDCr9GAwlMEZAGHAsN0WDgcNXkrmE25fVX1IkVSqWzQ4CTUiDOeOLdI0SUp3oWXjEbOiiWdWySCSb7IS0yxbjOytDVzwG78mBmYURtLdiyTLusIsMTvwTW_UP4N5f1XxDfwYUhac_3uYPOZA3PgN27I2hceIbZ6d5cIxksVWc47a6cgeA7NbP_YtKpZ1mKA7S6E8wwwpG2WH-Ncs4414LtQuChl1ukm_s1mVXDMdc5PXr6yvXlnW4I45YXNPaHwnUvi-oNYEJsaPou6V4h5jJyrtkmxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=Nf5hgSkTbPXQr8CPDUONdLg2ql-FkcyDKJdaSr7EVv203zJ7mnnXDu3vMtUDCr9GAwlMEZAGHAsN0WDgcNXkrmE25fVX1IkVSqWzQ4CTUiDOeOLdI0SUp3oWXjEbOiiWdWySCSb7IS0yxbjOytDVzwG78mBmYURtLdiyTLusIsMTvwTW_UP4N5f1XxDfwYUhac_3uYPOZA3PgN27I2hceIbZ6d5cIxksVWc47a6cgeA7NbP_YtKpZ1mKA7S6E8wwwpG2WH-Ncs4414LtQuChl1ukm_s1mVXDMdc5PXr6yvXlnW4I45YXNPaHwnUvi-oNYEJsaPou6V4h5jJyrtkmxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجیا ملونی نخست‌وزیر ایتالیا:
نمی‌توان اجازه داد ایران به سلاح‌های هسته‌ای یا کلاهک‌های هسته‌ای دست یابد، به‌ويژه با توجه به اینکه ایران موشک‌های دوربرد دارد و این مسئله را به وضوح نشان داده است.
ملونی تأکید کرد که این موضوع تنها به ایالات متحده یا کشورهای نزدیک به مرزهای ایران یا اسرائیل محدود نمی‌شود، بلکه مسئله‌ای است که نمی‌توانیم آن را اجازه دهیم یا تحمل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66752" target="_blank">📅 10:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66751">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3361863344.mp4?token=IE0jq0s24ChhE0NpUuupgXHQMD9Et1XBOq6QLGMSpDA2PLBF41t1UiYLyNbmUmqUWeEAyZfBGrEqIjfiWOP1c-ON0ZSPbfA4CUtqRumsmm3j60dcjwV5QvbL8S0knoAqBN6JiOcF21HOfl0u7Wk0GNabRMcELc1L6jV43fGNjDf2WWKUzb-UHOCftYO0XqnG9briJXtt8SmNhgXVQw3AbcAdXXmp9daVX-hHs-MiK1Et9HYwltioo0LabCbCyRinSXKm3i0ffChNc6nmg5lEdgUS_X9CXQr966XdKDZgkP7nXsGTC7D2Vr3DeeN3H2rhbiXa_bv_CHAkSdAT76-O0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3361863344.mp4?token=IE0jq0s24ChhE0NpUuupgXHQMD9Et1XBOq6QLGMSpDA2PLBF41t1UiYLyNbmUmqUWeEAyZfBGrEqIjfiWOP1c-ON0ZSPbfA4CUtqRumsmm3j60dcjwV5QvbL8S0knoAqBN6JiOcF21HOfl0u7Wk0GNabRMcELc1L6jV43fGNjDf2WWKUzb-UHOCftYO0XqnG9briJXtt8SmNhgXVQw3AbcAdXXmp9daVX-hHs-MiK1Et9HYwltioo0LabCbCyRinSXKm3i0ffChNc6nmg5lEdgUS_X9CXQr966XdKDZgkP7nXsGTC7D2Vr3DeeN3H2rhbiXa_bv_CHAkSdAT76-O0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار «مثل رهبر ما مخالف با تفاهم‌نامه‌ایم»در هیات
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/66751" target="_blank">📅 09:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66750">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=ffyprLgY_gk3FCwrty6_8kT1wMutnDTXyXstwon8tuvrRgi08hxqjzVPqv-KceDj0phWj96Lvs0Qa2-sQVke7ascleyn6VTjIvn0gIx-dt3VmulX4g7bNqAAzcYlVilQwvG9g2z0VYJ17DdhLu5t2ybH6sjWR5aZwJpT9HS5WJTM9xRbqg3iE4ETI6-wm2TWW6znt56-oSJxml5qS2bSQaUaXJ38X2h_dhFCy9VqQDoe5-GCHBIioByq72GNSKnfd6u5VcWnRwu9S2hHNYx5pMF84ul7dbi0GPSzFxgQ_OQjBSe7b26CQbQCd3oYn_FzEByK2x-C6I2sT1m14RSoqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=ffyprLgY_gk3FCwrty6_8kT1wMutnDTXyXstwon8tuvrRgi08hxqjzVPqv-KceDj0phWj96Lvs0Qa2-sQVke7ascleyn6VTjIvn0gIx-dt3VmulX4g7bNqAAzcYlVilQwvG9g2z0VYJ17DdhLu5t2ybH6sjWR5aZwJpT9HS5WJTM9xRbqg3iE4ETI6-wm2TWW6znt56-oSJxml5qS2bSQaUaXJ38X2h_dhFCy9VqQDoe5-GCHBIioByq72GNSKnfd6u5VcWnRwu9S2hHNYx5pMF84ul7dbi0GPSzFxgQ_OQjBSe7b26CQbQCd3oYn_FzEByK2x-C6I2sT1m14RSoqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای وایرال شده از خوشحالی تیم ملی نروژ به سبک وایکینگ ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66750" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66749">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66749" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66748">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZyrLAg5Bbfw9Rh1tEQAl8V0TYYGuWDlTxMX9CtSElotiYc-Ui6rCafcyGX3CLiYcTQh71oY24EuWqNJCp7UVpOoHSW3oaZ1Ia1znSc99jY9AgQSLuesiVKjaK256GU7K2-G18FrOw3RAzuG-crxNNWQMnGcpdM6VW1miQE2yVkvArR6mi5lIDrhai1LnhTPjD8W5S35T7F-DxGBhf6EZ9lhR6DHaxH-XOjkRMpDn6Tum3c_3t9XRxapxWIr52HG-8b-DHvwkA3R1Zdi_z0_ZmHwhmDoSDHbptlbMuMLtRezwsCrdNh9hUqR6fD15lowiw2Xy0RpsOBDg9ZRRLME0_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66748" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66747">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=bbdvWT_ef1_ay6zlbJqAn9z3rSY4yUslYqcfR2zv4RTqO7Xj8DtOR6jlKW7YmOtYh9GR3rxSe4wZcO2DzrgITffx_mhFOtJINnR0V0xNOoqKNZ8NC6EBLeHDKjJTtRYETaw-CUzTDtk-8z5Fz-CCdQsp2Neb-mYLTJvhmeSXcfh91ZXAchT9toyPpgPJa4KhNRVlGkelPZpKvNokMAgkeasgAnoSpwThtRwyC13hYyTiLUsPp5S36TyUhABUP1GQHbwLoqxAnhTctigVqmwd3gtqvcYUG_YR1tqltyJhXGUSF65kYB4tT-uFWLjQWMdhL_5eKR06VOuO7ynALGDTCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=bbdvWT_ef1_ay6zlbJqAn9z3rSY4yUslYqcfR2zv4RTqO7Xj8DtOR6jlKW7YmOtYh9GR3rxSe4wZcO2DzrgITffx_mhFOtJINnR0V0xNOoqKNZ8NC6EBLeHDKjJTtRYETaw-CUzTDtk-8z5Fz-CCdQsp2Neb-mYLTJvhmeSXcfh91ZXAchT9toyPpgPJa4KhNRVlGkelPZpKvNokMAgkeasgAnoSpwThtRwyC13hYyTiLUsPp5S36TyUhABUP1GQHbwLoqxAnhTctigVqmwd3gtqvcYUG_YR1tqltyJhXGUSF65kYB4tT-uFWLjQWMdhL_5eKR06VOuO7ynALGDTCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«ایران عالی بوده است؛ ایران منطقی رفتار کند و باهوش باشد. در غیر این صورت، مجبور خواهیم شد کار را تمام کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66747" target="_blank">📅 01:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66746">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=tEZoJwDp2SaQRTEDrV0T3w1HI5OvLty90nWZHg8YvJCNTZXF_I1WJ9bm7E9qe7OFbWc_HKdNwaF9XHgYUFCYnEY_vn2k_B055ew_Zh_W0ZtT_5sjeSw9t6Otm0YIZldRbxvd4VyPZJNDh3nYz_3uLMS6Tqz9XzFNx6K_wu_r7wjXUX3sz9_njS9GNXbq4qUQMOycAInpFmEV5ATjLHXsrFrPecpZjMApSyW43MQJtVERuzZ_Zr9yXOV3lOS-t70QLsyePtFQzBqvhnWAnE4mPSF3Hb_yP5G8bal2Hkm-EALG8VFcn6C_LrAV4LSQes685xLJMdRfl1Xf3LotV1QJVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=tEZoJwDp2SaQRTEDrV0T3w1HI5OvLty90nWZHg8YvJCNTZXF_I1WJ9bm7E9qe7OFbWc_HKdNwaF9XHgYUFCYnEY_vn2k_B055ew_Zh_W0ZtT_5sjeSw9t6Otm0YIZldRbxvd4VyPZJNDh3nYz_3uLMS6Tqz9XzFNx6K_wu_r7wjXUX3sz9_njS9GNXbq4qUQMOycAInpFmEV5ATjLHXsrFrPecpZjMApSyW43MQJtVERuzZ_Zr9yXOV3lOS-t70QLsyePtFQzBqvhnWAnE4mPSF3Hb_yP5G8bal2Hkm-EALG8VFcn6C_LrAV4LSQes685xLJMdRfl1Xf3LotV1QJVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران ایدئولوژی بسیار متفاوتی نسبت به ونزوئلا دارد.
ایدئولوژی مسلمانان تا حدی با ایدئولوژی کاتولیک‌ها متفاوت است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66746" target="_blank">📅 01:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66745">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=Tn7ylaltwuJWk3NFPirEk8IX8NnwFH3XBq7Bc76bqMmUZ13nurOujzteifi3JOsBr0M90PxKA2zN9FnD2fEQOrEa3hw-whUd1xcUEpYnWV-G8Jp8XAoEWt3E6Nnc2IpGowT0XkZbd4SCF7puXF4nXmuilOqF808ZtwsWxdeuBOEli08cektP-si0O6dKp1BHps9zIsRR-bOcsyAJpg6DNFq6xKzGgGdOlbl1yFCUTr38e0J513vK2dfMW5slBNpk48ClwqIeXE8kuMm-Qx64Ct8QjyhoEsNTIm8PDM7sGjV_DTSR1_Qc8yL1wK2Cf8rpsEhVUT8xcgxWlMgAT-ecAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=Tn7ylaltwuJWk3NFPirEk8IX8NnwFH3XBq7Bc76bqMmUZ13nurOujzteifi3JOsBr0M90PxKA2zN9FnD2fEQOrEa3hw-whUd1xcUEpYnWV-G8Jp8XAoEWt3E6Nnc2IpGowT0XkZbd4SCF7puXF4nXmuilOqF808ZtwsWxdeuBOEli08cektP-si0O6dKp1BHps9zIsRR-bOcsyAJpg6DNFq6xKzGgGdOlbl1yFCUTr38e0J513vK2dfMW5slBNpk48ClwqIeXE8kuMm-Qx64Ct8QjyhoEsNTIm8PDM7sGjV_DTSR1_Qc8yL1wK2Cf8rpsEhVUT8xcgxWlMgAT-ecAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این میم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66745" target="_blank">📅 00:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66744">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=sa3SZwnGxFsgucLJpb45c86AcBiuC18TRHF6WD8nk3noLF_pJcy2OR-NXyFkH4sPqvIUpJOAC1EXD3_un1z54QvKDz2DJlDe-lX3OgzeFjxmAfKhpZ4AeLLvGAbKMtdWa8QW0vz4gVUKolIG5wPVzk0Yh9y0YQpJDfWhXZe8aZT25QkNbQKdnR5soKXhTbF2gGwb8fd5Qf9ma5zsyB7H_rRlyCxY3NdPd3miWTTlfr5x6BH3ODuUFTUVmALmq_NaknE-JCShGPeDRT4_fFqt4wKPm5r_T78ncKcF9LljeySDm8drkbzgUIVdiBGlsOwieGqhuBYjlxoW0r3X9bXUUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=sa3SZwnGxFsgucLJpb45c86AcBiuC18TRHF6WD8nk3noLF_pJcy2OR-NXyFkH4sPqvIUpJOAC1EXD3_un1z54QvKDz2DJlDe-lX3OgzeFjxmAfKhpZ4AeLLvGAbKMtdWa8QW0vz4gVUKolIG5wPVzk0Yh9y0YQpJDfWhXZe8aZT25QkNbQKdnR5soKXhTbF2gGwb8fd5Qf9ma5zsyB7H_rRlyCxY3NdPd3miWTTlfr5x6BH3ODuUFTUVmALmq_NaknE-JCShGPeDRT4_fFqt4wKPm5r_T78ncKcF9LljeySDm8drkbzgUIVdiBGlsOwieGqhuBYjlxoW0r3X9bXUUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
​
اگر ما موشک‌های خود را که برای دفاع شخصی‌مان است نداشتیم، اسرائیل و آمریکا با ایران همان‌گونه رفتار می‌کردند که با غزه رفتار شد و هیچ رحمی به پیر و جوان نشان نمی‌دادند.
​ آن‌ها از حقوق بشر سخن می‌گویند، این یک دروغ بزرگ است.
​ اگر نمی‌توانستیم از خود دفاع کنیم، آن‌ها به کشور ما رحمی نمی‌کردند و قدرت ما را نابود می‌کردند.
​ بنابراین ما تحت هیچ شرایطی با هیچ‌کس درباره توان دفاعی‌مان مذاکره نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66744" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66743">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=gC-Q1_op8B-TKcwdGx7Hz0uTx593IQDQ01_qWnhm0dCJeyITi6bqLP0HwEjZUYztg95AU0amrb46XrsoID-Sy2vgxd-wBmksXJMFq4j1Gre0NLdtzMJ663oXQHg6EaLPlL_MmYjiGgcQXeFJ4cVRXmyLMylC3ML_9lfUcVC7k9Hrmm5ZzAXUU2GrOEqX9qbQGFazIxiihiN7JyQ_qgmlPk61GzLkGwTq2qp6OkMCzxSWHFSMXlthlEHytX71cEVgr_0gm9Dwbw7cIMwaTsPKI1RP6KhRFeffHwWXP2jNW1d-ZaU-XilcvNPOrL0TtB7Yd2obYaIhr2KyIN8u6ma1bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=gC-Q1_op8B-TKcwdGx7Hz0uTx593IQDQ01_qWnhm0dCJeyITi6bqLP0HwEjZUYztg95AU0amrb46XrsoID-Sy2vgxd-wBmksXJMFq4j1Gre0NLdtzMJ663oXQHg6EaLPlL_MmYjiGgcQXeFJ4cVRXmyLMylC3ML_9lfUcVC7k9Hrmm5ZzAXUU2GrOEqX9qbQGFazIxiihiN7JyQ_qgmlPk61GzLkGwTq2qp6OkMCzxSWHFSMXlthlEHytX71cEVgr_0gm9Dwbw7cIMwaTsPKI1RP6KhRFeffHwWXP2jNW1d-ZaU-XilcvNPOrL0TtB7Yd2obYaIhr2KyIN8u6ma1bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو وزیر امور خارجه آمریکا وارد ابوظبی، پایتخت امارات متحده عربی، شد. جزئیاتی درباره دستور کار، دیدارهای رسمی و محورهای مذاکرات این سفر هنوز منتشر نشده است، اما این سفر در شرایطی انجام می‌شود که پرونده‌های امنیتی و تحولات منطقه‌ای، از جمله موضوع رژیم جمهوری اسلامی، در کانون توجه قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66743" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66742">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=cUM10HB9biCFz8OktSb3MKhfsCidu56cLYUUarQ1_Msv7uLc1M8n1BsEeOKJjjo2eQrMXNLpgubpFYLjI_C4eO3IFj16XFlCn5WzBFng6yBHTX7a_K6IIvK2PeP7x4DM_9nr8LYGDXRnjxc60Ioq4nOm1uClivgLclO0BIY9QMoDzYUDcNG2AEL3tDM91Wvx1Rpze0htNU8bUuOPMMZi2f4rywzR3ldkge5pdFKl3uGYje9ptYU0g5PYtfzfUYoFGP8RcTAMJPRnM9kdhb6Trn1JUhmI5K5EHgEPJNUokyXJcaahdxLrYZZ-vFJq0rioE83IhllXC0KnvIqSqvi6jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=cUM10HB9biCFz8OktSb3MKhfsCidu56cLYUUarQ1_Msv7uLc1M8n1BsEeOKJjjo2eQrMXNLpgubpFYLjI_C4eO3IFj16XFlCn5WzBFng6yBHTX7a_K6IIvK2PeP7x4DM_9nr8LYGDXRnjxc60Ioq4nOm1uClivgLclO0BIY9QMoDzYUDcNG2AEL3tDM91Wvx1Rpze0htNU8bUuOPMMZi2f4rywzR3ldkge5pdFKl3uGYje9ptYU0g5PYtfzfUYoFGP8RcTAMJPRnM9kdhb6Trn1JUhmI5K5EHgEPJNUokyXJcaahdxLrYZZ-vFJq0rioE83IhllXC0KnvIqSqvi6jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعرخوانی جالب شهباز شریف به زبان فارسی در حضور پزشکیان
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66742" target="_blank">📅 22:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66741">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما ایران را در وضعیتی بی‌سابقه قرار دادیم که در ۴۷ سال گذشته هیچ‌کس موفق به انجام آن نشده بود. اگر ادعای ایرانی‌ها مبنی بر عدم اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به ایران صحت داشت، نشست با آن‌ها را فوراً لغو می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66741" target="_blank">📅 21:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66740">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=DUTzEwfcHcSvr2y0XnbA41ASo46D_jMVHFyHNXab67PagITSd15JgMD9r3xsLY5fXL0RYGvyLjMCOgfkrreChL1gKDWjUSet__KXOtwMgH61gKI75cecVg0twP1rJ1egTsoFoT8m_1BVOCF3LVpmfB65BGkJ2HVSJsCPjFw08p4XKLMmGTxe18EJK9rn7swLLxPE62pgzW7Wvgr6t5NSnC1dvD1d2koBefn9DuQybXp0KbnrfWYgdTW5j_0usipboPyFSvsM4OJ9K_kj5ls4rbe1t2SWn_6ViOIfiyujsmsho4e9u4JFvsI807l5Soc_rwHuX7-MQ6jtogOn2KDZFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=DUTzEwfcHcSvr2y0XnbA41ASo46D_jMVHFyHNXab67PagITSd15JgMD9r3xsLY5fXL0RYGvyLjMCOgfkrreChL1gKDWjUSet__KXOtwMgH61gKI75cecVg0twP1rJ1egTsoFoT8m_1BVOCF3LVpmfB65BGkJ2HVSJsCPjFw08p4XKLMmGTxe18EJK9rn7swLLxPE62pgzW7Wvgr6t5NSnC1dvD1d2koBefn9DuQybXp0KbnrfWYgdTW5j_0usipboPyFSvsM4OJ9K_kj5ls4rbe1t2SWn_6ViOIfiyujsmsho4e9u4JFvsI807l5Soc_rwHuX7-MQ6jtogOn2KDZFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره تنگه هرمز:
این یک آبراه بین‌المللی است. هیچ کشوری اجازه ندارد برای یک آبراه بین‌المللی عوارض یا هزینه دریافت کند.
این همان قانون بین‌المللی موجود است. در تمام آبراه‌های بین‌المللی در سراسر جهان همین‌طور عمل می‌شود و ما انتظار داریم که اینجا هم همین‌گونه باشد
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66740" target="_blank">📅 20:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66739">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=YrpGXxBM0bamLKdXKJaJbray64lMDDYQu9h0GOViKx8M5FLeX0o5U2JwHGmBTD5VHP8JwGDTukDzwUrQRJFqW_nwh-dbT8D6BHbkLaNgBadKQlK9wZceO_OkQzKtE8zi9g6QB0RfDYH2yVOcBvjlsKByq2MFzJvZAnWGGT0hvJU0qr8i-zsQaGK58XJVJbxU2yzqdw2-3LeZXoR3tptE2IdZSPpocatTwI5MokeZJ-MmQZe0Ys1XVGmthebqic8i5Nb0WetGxOy_jyaWaJyIzeu9AgtEcsg0oFIMXNUQxN5bQ9hDn4Ea-mHXzDFz6XIz6K4bk1-Tff68jWPqj-X_Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=YrpGXxBM0bamLKdXKJaJbray64lMDDYQu9h0GOViKx8M5FLeX0o5U2JwHGmBTD5VHP8JwGDTukDzwUrQRJFqW_nwh-dbT8D6BHbkLaNgBadKQlK9wZceO_OkQzKtE8zi9g6QB0RfDYH2yVOcBvjlsKByq2MFzJvZAnWGGT0hvJU0qr8i-zsQaGK58XJVJbxU2yzqdw2-3LeZXoR3tptE2IdZSPpocatTwI5MokeZJ-MmQZe0Ys1XVGmthebqic8i5Nb0WetGxOy_jyaWaJyIzeu9AgtEcsg0oFIMXNUQxN5bQ9hDn4Ea-mHXzDFz6XIz6K4bk1-Tff68jWPqj-X_Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
تا زمانی که نیروهای نیابتی ایران از داخل عراق موشک‌ها و پهپادها را شلیک می‌کنند و در اقداماتی مانند تروریسمی که حماس و حزب‌الله انجام دادند مشارکت دارند، نمی‌توان به پایان خصومت‌ها و درگیری‌ها در منطقه رسید
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66739" target="_blank">📅 20:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66738">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=jXIywQYkvdmYM3dIBHrlJmrINwJi2dxjkoBpZBJVI3CKZqRfww4Em0xW8PLktzVUx1VO2F1r6SXh9MBlnyrrJfRNlJ1Oan6seH9kVafBbrlY5RsjCAtzYM2nEnV-PINkqwepO_0IqoTh2oKFSFF7fulNtvlcuT7u0GEIVpxCHlCo3RQ-kI-2aj2GfKsB_beFz7UPCzFGRrrRQbQbk4kX26qJpnzTAqw0GD84GZh2RTDtJj8ZJDlnd0dOLAhh-VeZAi9SBnurA1oUSxHEFh3SL0J4TTZezf3eixJyXyBZ8-QL32QVXZWqTjNl_KTKRQtiGRePy0dYrTcsnn50iRaiXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=jXIywQYkvdmYM3dIBHrlJmrINwJi2dxjkoBpZBJVI3CKZqRfww4Em0xW8PLktzVUx1VO2F1r6SXh9MBlnyrrJfRNlJ1Oan6seH9kVafBbrlY5RsjCAtzYM2nEnV-PINkqwepO_0IqoTh2oKFSFF7fulNtvlcuT7u0GEIVpxCHlCo3RQ-kI-2aj2GfKsB_beFz7UPCzFGRrrRQbQbk4kX26qJpnzTAqw0GD84GZh2RTDtJj8ZJDlnd0dOLAhh-VeZAi9SBnurA1oUSxHEFh3SL0J4TTZezf3eixJyXyBZ8-QL32QVXZWqTjNl_KTKRQtiGRePy0dYrTcsnn50iRaiXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
اگر رهبری ج ا  تصمیم بگیرد که می‌خواهد یک کشور باشد، نه یک جنبش انقلابی که ترور صادر می‌کند، آن‌ها فرصت خواهند داشت کارهای فوق‌العاده‌ای در ایران انجام دهند.
این فرصت‌ها می‌تواند شامل سرمایه‌گذاری و سرمایه‌گذاری خارجی مستقیم باشد… این پول دولت ما نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66738" target="_blank">📅 20:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66737">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=GChVAy2aN3Ao9j-DWCqfQ85HdG04nplVV8HrHUP8qlZA4okm0ig__61ZJqfS6nNYPCrOGAqUd3s5G7ekG3an3sdDafx6akt24eh5i5EEX9S40bghQbUyC45ukfrUT6lyxFvowk495RNqq607Vo0gqTIfI_6E8geZAYVYG9NT1WTRlePyo13ZYa9lQIJAa7Wl2oSk7286f0zigkCG0DYWdyhxWXC2oW6kPLYKztdLju-QWe2OlwZKG-CLu54wwrfMXU0EazytJJNWEqAeLjKCclRthOM1khw8IHzw-9AQ5yA2dMWDTV5vxu7MRPSWC8SD4rL1l68RiE9KWMkMcOvpQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=GChVAy2aN3Ao9j-DWCqfQ85HdG04nplVV8HrHUP8qlZA4okm0ig__61ZJqfS6nNYPCrOGAqUd3s5G7ekG3an3sdDafx6akt24eh5i5EEX9S40bghQbUyC45ukfrUT6lyxFvowk495RNqq607Vo0gqTIfI_6E8geZAYVYG9NT1WTRlePyo13ZYa9lQIJAa7Wl2oSk7286f0zigkCG0DYWdyhxWXC2oW6kPLYKztdLju-QWe2OlwZKG-CLu54wwrfMXU0EazytJJNWEqAeLjKCclRthOM1khw8IHzw-9AQ5yA2dMWDTV5vxu7MRPSWC8SD4rL1l68RiE9KWMkMcOvpQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف، به پزشکیان:
لطفاً گرم‌ترین تحیت‌های خود را به مقام معظم رهبری، آیت‌الله مجتبی خامنه‌ای برسانید.به لطف رهبری ایشان، ایران توانسته است این تفاهم‌نامه را به دست آورد و در نتیجه، آتش‌بس را با کرامت و افتخار به دست آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66737" target="_blank">📅 20:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66736">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=vOhlmvBYH5cVXVVTuaoDEhf-1lJzCDOBvd86EABY1BuzqWzvhotPehsIFscOE8wzhcnlu-RaVR1L3G7_QGGd-twSJpaZbE0IRlGEh3JCSswu1xKyaXm125SvTSLKWTfxj1XY4DvTsuAwnb0XSUaYuHkMPFnDZo3hjG441NxAbfrueZ2sBnCZkA0W8hgSYy_TjV8MGqpbNr7UIUy9lw7mbSz4uZuB_1_1UlarohYtseTPsqacs603MUxf365uT8hUC-tTDxs3-ryMBNZCi27eZf-Xdq979b7FS3m2w64PT4QXLeCcRzgBWiRKOqaJgvDSo6doWYVADCkQikwiH0lrPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=vOhlmvBYH5cVXVVTuaoDEhf-1lJzCDOBvd86EABY1BuzqWzvhotPehsIFscOE8wzhcnlu-RaVR1L3G7_QGGd-twSJpaZbE0IRlGEh3JCSswu1xKyaXm125SvTSLKWTfxj1XY4DvTsuAwnb0XSUaYuHkMPFnDZo3hjG441NxAbfrueZ2sBnCZkA0W8hgSYy_TjV8MGqpbNr7UIUy9lw7mbSz4uZuB_1_1UlarohYtseTPsqacs603MUxf365uT8hUC-tTDxs3-ryMBNZCi27eZf-Xdq979b7FS3m2w64PT4QXLeCcRzgBWiRKOqaJgvDSo6doWYVADCkQikwiH0lrPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف:
این تفاهم‌نامه هیچ اشاره‌ای به موشک‌های بالستیک ندارد.
این موضوع هرگز روی میز نبود؛ هرگز در دستور کار قرار نداشت.
طرف ایرانی هم اصلاً نمی‌خواست درباره آن بحث کند
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66736" target="_blank">📅 20:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66735">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHspOgZZXINZs4zJadPuQkd7trIa8BhY_j5Iq3hcd7r19PDZV1OmSEsVqocMc0S9vh0RYqfHQ4Ysod7dAZDfRg9lwjgIUIahlfHJit3YbRS04-d-KKnFJSBlya3oFogP9vIkaqyyQaGjqaH_YfpQduJHBGzUc9UFIyUw5anggS5tBHLpxGK7ABIRPxW0OdYKQmuwHe7-ka5aTxIoRDN4kH_dDHFoyn-KdEg4Tj6IwrOXyVOOTrYCC9gyTWQszeW6T8RYVrLqr2ucmJfvMteKf4EI1nuUa2uiLWnHjNf8E0vYeVuC4wxEgVQaFi7-lmVjqyeIaqh_EIpq8iTAAEidjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پسر پاسدار کشته شده علیرضا تنگسیری فرمانده سپاه که معلوم شده اینم طوری زدن که فقط یک دستش جا مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66735" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66734">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66734" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66733">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UnrCCF7l_9UxMLh8NLUZZjsT0svMV3NFJmhR7TmC9CLgrpweBGw-o_ctgDabogHU9IptbOd7T_CKzOS-o56U2LxMv3SLZkbXZeQM2mwcxluGFwv9-tPe-zcf1hmCCwsK-FpuP9P0voDQOTVn6KkwRL8vJwUkcdqwsq5-i8eH6Lq17VnX7Wqeo2yZtg0N863Gvmyi_I99BqzjAKKR332cIsUGS6I9T6gMjeknpq6pHDvYLU25lUega_RYFLtvpemM85d4HlEEbjZC2H6QzI_Mglv448Kl2U7pk-NQQhpiPPD4C-uXCbZ-jwAIhJAhR7HJ83bjtHJVaArVk6GTH1ltdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66733" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66732">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=n8O3oOLugU-dJMIY6RZVcj0rroQgNZQVPC5ZCpoebuuinEL6VGWj2_yMBnu8kPCsvKois9dJG4teCBWineUAQr0djRo3zExzoLGQX21NlmjUbE69_Z_yIf5nefI2J0EBTKIIKca4Xf8Uds0GF4RytpH0RNTqnnGvMx-WLrFtEV0wa_e1lN9zTbRMpc1zJ6ckivUZPC-CbYpoJs-NzwmNI42Q8C-zb3TCcrCM6tLd1RQl8Rq3FrjzEPIp7_Z76r8YtmZuq5h10ywhGBhI2flx0hO7RSGJW6aKbTdD7RLQAS66hbbKSypxSYxpjTJ3qJ4d-ywSEUML08waDooXgStD5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=n8O3oOLugU-dJMIY6RZVcj0rroQgNZQVPC5ZCpoebuuinEL6VGWj2_yMBnu8kPCsvKois9dJG4teCBWineUAQr0djRo3zExzoLGQX21NlmjUbE69_Z_yIf5nefI2J0EBTKIIKca4Xf8Uds0GF4RytpH0RNTqnnGvMx-WLrFtEV0wa_e1lN9zTbRMpc1zJ6ckivUZPC-CbYpoJs-NzwmNI42Q8C-zb3TCcrCM6tLd1RQl8Rq3FrjzEPIp7_Z76r8YtmZuq5h10ywhGBhI2flx0hO7RSGJW6aKbTdD7RLQAS66hbbKSypxSYxpjTJ3qJ4d-ywSEUML08waDooXgStD5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی منتشر شده از عباس عراقچی و همتی که وسط مذاکرات با آمریکا پا شدن رفتن بازی ایران و بلژیکو تماشا کردن.
اینجا گفته بودن مذاکرات ترک میکنیم اما رفتن فوتبال ببینن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66732" target="_blank">📅 19:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66731">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=oOGs-5dO287uXkYpMT1lL4xZvNssQrkJS4r-IvxNBY-n0_vaa9v_OfSJhEzJm_Q7I7Z860Qln20wpmTOn_x_b7b321FwJY8JJkYah100kgsn0FQTTeNtZadS7Hlxwm8_vhON5ZQWxJOPK1yoytw5ihn2UuZEB9iStMePr4WGF99hV3IBrYJJI7f4Pib8C3tb9e7uoljtNPat9vzaKeFW_ZHHgAq4XqiqrXuErH59Wl5DfBHXe7GDRTJgcojXJ49HIEheWIw3H0QpVs_mgK9EKxVmATBGwZj2JIkNFlw2vaassCyZGmHai9DOWhTmJ1z-lZEZ97yRiiCFChTn6ZDr7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=oOGs-5dO287uXkYpMT1lL4xZvNssQrkJS4r-IvxNBY-n0_vaa9v_OfSJhEzJm_Q7I7Z860Qln20wpmTOn_x_b7b321FwJY8JJkYah100kgsn0FQTTeNtZadS7Hlxwm8_vhON5ZQWxJOPK1yoytw5ihn2UuZEB9iStMePr4WGF99hV3IBrYJJI7f4Pib8C3tb9e7uoljtNPat9vzaKeFW_ZHHgAq4XqiqrXuErH59Wl5DfBHXe7GDRTJgcojXJ49HIEheWIw3H0QpVs_mgK9EKxVmATBGwZj2JIkNFlw2vaassCyZGmHai9DOWhTmJ1z-lZEZ97yRiiCFChTn6ZDr7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روحانی : اسم بچه‌هاتون رو امیر نزارید، ریشه این اسم بهایی هست
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66731" target="_blank">📅 18:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66730">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9028c70792.mp4?token=eRiY6-xMf1IQ1f_jdda5FNwfZtmTuB0M43a32OwX4QZHwV5dq4B7Bi_WBsSA_tAepJRB-mz89bXRgjFot9Wxku9yCqRc9YHSOWbGobypdOxnUeTQTW4SytmKqElWfqKpch3lO585uV3rrHaCaBK5m0_p0XfyeFiHNUAFBRU36EOzHyw3YYY2ENlf5lYrpkIPpEO0K_SqbbejwqEOP0CwNVRpm6rk-16331WFn9kViOmJE8Gj3FSQaxprVikDrSi7T8bWC7tI9pORjEx5u7IBk5O4Rr-gaFJCjSs0R5bYA4Gx6ffxcvqYvcdUYS5wDWaHwsLDo2YHrNCbGdOZse5AbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9028c70792.mp4?token=eRiY6-xMf1IQ1f_jdda5FNwfZtmTuB0M43a32OwX4QZHwV5dq4B7Bi_WBsSA_tAepJRB-mz89bXRgjFot9Wxku9yCqRc9YHSOWbGobypdOxnUeTQTW4SytmKqElWfqKpch3lO585uV3rrHaCaBK5m0_p0XfyeFiHNUAFBRU36EOzHyw3YYY2ENlf5lYrpkIPpEO0K_SqbbejwqEOP0CwNVRpm6rk-16331WFn9kViOmJE8Gj3FSQaxprVikDrSi7T8bWC7tI9pORjEx5u7IBk5O4Rr-gaFJCjSs0R5bYA4Gx6ffxcvqYvcdUYS5wDWaHwsLDo2YHrNCbGdOZse5AbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ثابتی:مذاکرات به رهبری تحمیل شد وگرنه نظرشون چیز دیگه ای بود
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66730" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66729">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=bzdku7jDDUFXCzQLc9Nxt2G1f5VOsE2GgJVUQu6je0JYISoAfvnrRI_ehDivq0oTbsz2TGBgkYxD9AjMJT2aQHmMwxE6yoXanh5DsRc2FncqBxHgpEqLYJBB1aVsLk2h9xsZS0zbIImHDcibdpxSCKKbPN8Tx9g2ewdgBE1HjZ8vAaq04J6WWALIUUhQQ8ZK-1AQFgu23EmuQoz7kKGMuLVt3vX7th1esXAGFd8MUL1sFK6P89yFNGV_pSHILeVhpqEWYBWNY18xvFwwoZqU_ZyjxpaC2pjDTKQJS18PYOxUhQaIjLl5K2VVL__LkvBRnExt_Jt_GbrF2VdlgWdsKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=bzdku7jDDUFXCzQLc9Nxt2G1f5VOsE2GgJVUQu6je0JYISoAfvnrRI_ehDivq0oTbsz2TGBgkYxD9AjMJT2aQHmMwxE6yoXanh5DsRc2FncqBxHgpEqLYJBB1aVsLk2h9xsZS0zbIImHDcibdpxSCKKbPN8Tx9g2ewdgBE1HjZ8vAaq04J6WWALIUUhQQ8ZK-1AQFgu23EmuQoz7kKGMuLVt3vX7th1esXAGFd8MUL1sFK6P89yFNGV_pSHILeVhpqEWYBWNY18xvFwwoZqU_ZyjxpaC2pjDTKQJS18PYOxUhQaIjLl5K2VVL__LkvBRnExt_Jt_GbrF2VdlgWdsKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد مجری صداوسیما از رفتن قالیباف به مذاکرات
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66729" target="_blank">📅 17:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66728">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URI2sY1KqRYkdSL70MLfUFZuo1X42UeTkF0qcRHLId7Ljjt7dFOa_aN0G9XIjOupUx6OeZ-9mmK2aauR7KKw_xulOJNSkcnvgBm53ke_hKi_GShrDjWD5K_VSUcfWEhilCiRWd_cmUnBaRaKctE49oYz5U4XhU5H8VDbrw65uNawtqWfzAhjVOtaMX7K3-8l55IYfpN1KAgjUi_KjTi7HlNTX_ugOGJ1PzNPW0jCKqMzah-rqDDB2-P4syClPMBLYLCOmLtJi0h88YFalqteInOcAuIDkrVlGVwxfZWoes50adGhpBUUzgRnZmr2viE8Uw2X21eJGQ7rhihNcsRhJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آناتولی گزارش داده که شهباز شریف گفته قراره درباره برنامه موشکی جمهوری اسلامی هم  مذاکره بشه
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66728" target="_blank">📅 16:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66727">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbYzwIYONJxdC4egGI18Y9d4Zcah_A9K10T43mWicfm6jiS3yNVy0E7vYxrPw_4xOHRPngR4tDfS4tluR5dQiIi1Vwx9ESwcYW6-qljsj7BZMnGWLCxqS4qGw5S6Kr9Oy5a1oL4blHxCsNSPCcIWX3t7uJFtr0Vhrpr-yu_CIpxlGgOQxFtNBvZr-uI_ym0M_m7v0yTFdCAW3zgqgCU55wEgO_K70iJnjYnBqBMw5ZW8vyzdrepjIhCaodp1w2IPnaX-cGTeir8vzXbU_CuFsSkDoHyzEmC5xX2ctzNkrSUtu05FP3bGBV1gCW3o-gb5uRgf_La7m3pfNsac8Eqehw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ورود عاشقانه مسعود به پاکستان
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66727" target="_blank">📅 15:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66726">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JosPgRBRPEAylhgpiAMRVF9iAhn11bPakXQsNiEa6r3ONdAIX0MYTDZwxVrBkJwdi4YA6sbYhJKgMIa8Bbd3yC9cdtF4jW3iW858gSAp8Zalc-jHSOSc6qtuRn3DEit-wEPi7CrDeepHhEGgXijwVwrApizw3-ZQCtHRQC9dpwNq0GoWYb-DxKj9Q_b55XimK3aIiInfsNleWuD2fPiBUBmZ_zbmNUNq2lm80OCu-rvoOFDexJmvwmzLMbOJk_NturlLuR2o3LZhw_wucusXtRIeLXIzlakcgE1ZwYaaZparqLUMu8K9o8UwEV9HMdSugAKF7lvf1vTIjbqdpGxNRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«با وجود اعتراض‌ها و اظهارات نادرست آن‌ها بر خلاف واقع، و همچنین هیاهوی مداوم رسانه‌های جعلی که تمام تلاش خود را می‌کنند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهند، ایران به طور کامل و بدون هیچ ابهامی با بازرسی‌های هسته‌ای در بالاترین سطح و برای مدت بسیار طولانی در آینده (تا بی‌نهایت!!!) موافقت کرده است. این امر “صداقت هسته‌ای” را تضمین خواهد کرد.
اگر آن‌ها با این موضوع موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای در کار نبود! بر اساس این توافق و دیگر امتیازات مهمی که ایران در حال ارائه آن‌هاست، من موافقت کرده‌ام که تنگه هرمز باز بماند و هیچ محاصره دریایی دیگری اعمال نشود.
با این حال، تمام کشتی‌ها در جای خود باقی خواهند ماند تا در صورت لزوم محاصره دوباره برقرار شود؛ هرچند در این مقطع چنین چیزی بسیار بعید به نظر می‌رسد.
پول‌ها و/یا منابعی که وزارت خزانه‌داری آمریکا آزاد می‌کند، در یک حساب امانی (Escrow) تحت کنترل ایالات متحده نگهداری خواهد شد و صرفاً برای خرید مواد غذایی و تجهیزات پزشکی از خود آمریکا استفاده خواهد شد؛ از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما. ایران به شدت به این اقلام نیاز دارد.
این یک بحران انسانی است و من احساس می‌کنم که لازم است همین حالا کمک کنیم، پیش از آنکه خیلی دیر شود.
گفت‌وگوها به خوبی پیش می‌رود!
از توجه شما به این موضوع سپاسگزارم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66726" target="_blank">📅 15:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66725">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=J8TcXqAnI2YBj5HITB0YXXloA6cO05UOAhME3vdmFheVGCXd_2KvGB79u_ussZ7IPBPpNQsWvo4tm8Fw_CuogcHHwtadJAGc_zkQLtQ2Xa_WMwn2CVvHb7NHe2L6LQMIHiiqFqOY7UJo2CcjbtINJsm0DmuN4LFU2gG8D2eDNbFF9kT3B-eogvkUrYariCTmV3iK3O6wZWsW8snhd1QoPFFIFNRvQUUZxbwoGHh1pA_WIu9yVsawIAdgu8yMOUBAlxpPRho0MUzafnbkGCcTUQdZ55rU8qZ9Y2UcQyYvSu_jnfHbVsq62eL5-ULHsGIZ8LxyLCNwtwZiORej92EAqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=J8TcXqAnI2YBj5HITB0YXXloA6cO05UOAhME3vdmFheVGCXd_2KvGB79u_ussZ7IPBPpNQsWvo4tm8Fw_CuogcHHwtadJAGc_zkQLtQ2Xa_WMwn2CVvHb7NHe2L6LQMIHiiqFqOY7UJo2CcjbtINJsm0DmuN4LFU2gG8D2eDNbFF9kT3B-eogvkUrYariCTmV3iK3O6wZWsW8snhd1QoPFFIFNRvQUUZxbwoGHh1pA_WIu9yVsawIAdgu8yMOUBAlxpPRho0MUzafnbkGCcTUQdZ55rU8qZ9Y2UcQyYvSu_jnfHbVsq62eL5-ULHsGIZ8LxyLCNwtwZiORej92EAqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
‼️
ارتش اسرائیل در نبطیه الفوقا به افرادی مسلح که در نزدیکی نیروهای این کشور شناسایی شده بودند حمله کرد. بر اساس گزارش‌ها، ۲ نفر کشته و ۲ نفر دیگر زخمی شدند. این نخستین حمله ارتش اسرائیل به لبنان پس از ۳ شبانه روز بدون هیچ حمله‌ای در این جبهه محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66725" target="_blank">📅 14:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66723">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=DdedgWlatcrkav_OfTifPvKVtQK4ZmCD0HN4ydLJjuPjKauzh1KlgQcLyXE3iPH3CGR-o6X3nhvGH-icoewgEx3PCwNMTJQG8edHkD4M9LLE38IiHB3MjJBS_xq5cU_40fbrQYVL2O-1YnEq0Fwqwg-6GQztmk9TDMVa4DPZ6fEoV56rTxTWwGUWxnHe0QXzrNxmDslwDELHit6dDZy99kp5nq1MkcXMoqjKWEZursZjgbpKjfg7IMxAsH_tZpODpQgumTPjp4e2VlMnZA7owtbO_xtB7jJVfOIh9ZgWcPxX8aLeQqWOFrp9_OQeShzzxXyFIRCel5xbvQuLU2DcdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=DdedgWlatcrkav_OfTifPvKVtQK4ZmCD0HN4ydLJjuPjKauzh1KlgQcLyXE3iPH3CGR-o6X3nhvGH-icoewgEx3PCwNMTJQG8edHkD4M9LLE38IiHB3MjJBS_xq5cU_40fbrQYVL2O-1YnEq0Fwqwg-6GQztmk9TDMVa4DPZ6fEoV56rTxTWwGUWxnHe0QXzrNxmDslwDELHit6dDZy99kp5nq1MkcXMoqjKWEZursZjgbpKjfg7IMxAsH_tZpODpQgumTPjp4e2VlMnZA7owtbO_xtB7jJVfOIh9ZgWcPxX8aLeQqWOFrp9_OQeShzzxXyFIRCel5xbvQuLU2DcdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اوکراین یک پل حیاتی را که به ارتش روسیه کمک می‌کند تا تدارکات را به نیروهای مبارز در منطقه اشغالی زاپوریژیا منتقل کند، تخریب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66723" target="_blank">📅 13:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66721">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0iB1QqZsrnxqiU6P2VXoPLGJSztrdpJxqLuEDjRNAPqoOyxKK0il3yEiiXhsnMMlDVp3DF8QAEQyNMQ8KRXmBmLGzIu6TTPMwEmBk_-J5WO2g8TXlAUy7pSKxOb7CbQ8R_Mtq8tKDMuSiHZgIrCYDAAgZH-f7lLCWHaajQm_BxhLDpyhQA_cZpKvAGFRIgKX5nBotkhe0NxZt_8X1SeM8DT14g6L1xZemRrKkp-RIqdIMhQDgJAU49zNs4RrGPJRVZLehevio-7zIIlUFrcxbaD2gXwJiAxF0c6rBm6n08frSSOxZErnfWtFgTOQhUJZ-G8PQA6RpjRBpbVU3KoqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
اثربخشی مذاکرات به پایبندی کامل به تعهدات توافق‌شده و اجرای دقیق آنها بستگی دارد. پیشرفت در این مسیر با پایبندی عملی به مسئولیت‌های پذیرفته‌شده سنجیده خواهد شد. اظهارات خارج از متن توافق‌شده کمکی به پیشرفت مذاکرات نمی‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66721" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66720">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66720" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66720" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66719">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=Kx3bWhsZmWq0zNjGA80iXkmjmZ3TB6Sd_TrM2IqY7YYNYLHYYIjU2gE7aV3XieGZJuBLntZZ1bOB_PK54B6oTphJ00fX6OXKvrST-Y-LsgGXUr3OaBHA8HHgSdVn7UE0dZMFymVReCxr6CIk-DoDoNa3mtDBuT0CqYqxo7VTOT3kvZaBWwki-TBZ5h3amr7I9qICy2E_BPHRfBtcvTe1P1cVf57vq8olh46KMeO82pr8aQwTNukhq4IEpfPnvRi-E5f1oQDIkPqoB6jZEQdxgfxR4BJVZmj6KRJ5FF5u8NrheReFwi7UkGDLYLkRIYe9ej30i-pj9v0HW8zzEImePqoDgsQRBo3lCLHOIW-eisNa_DRq4_HHuAk4ou01IPydU7TTl_gcB5_g9tFlyhyDNYdl0DR5Lcfr7irpdobpk-p1XUv53jaMoGhANfomJiIMG-3mY5AINjNf8aqixDpvir86oyqtpS5_Cf-YVHRSLX4LuwG1XiQFNS1WYVHVnRxGNGbWB69y_WXPYWEpjfe-b4irGBpvyuR86HwRFEXk8qcEdL56HkQl_3P_sVBUpm7b8HTLpBTNY7yIL87vVZuA33Nib7oNeNOFqVPUieT4GkRNkAjeafdzO_zVF3begKuWtGAvXmYmEofiaoEz4wYufp9t_d3hwr_xggE04QCvk0M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=Kx3bWhsZmWq0zNjGA80iXkmjmZ3TB6Sd_TrM2IqY7YYNYLHYYIjU2gE7aV3XieGZJuBLntZZ1bOB_PK54B6oTphJ00fX6OXKvrST-Y-LsgGXUr3OaBHA8HHgSdVn7UE0dZMFymVReCxr6CIk-DoDoNa3mtDBuT0CqYqxo7VTOT3kvZaBWwki-TBZ5h3amr7I9qICy2E_BPHRfBtcvTe1P1cVf57vq8olh46KMeO82pr8aQwTNukhq4IEpfPnvRi-E5f1oQDIkPqoB6jZEQdxgfxR4BJVZmj6KRJ5FF5u8NrheReFwi7UkGDLYLkRIYe9ej30i-pj9v0HW8zzEImePqoDgsQRBo3lCLHOIW-eisNa_DRq4_HHuAk4ou01IPydU7TTl_gcB5_g9tFlyhyDNYdl0DR5Lcfr7irpdobpk-p1XUv53jaMoGhANfomJiIMG-3mY5AINjNf8aqixDpvir86oyqtpS5_Cf-YVHRSLX4LuwG1XiQFNS1WYVHVnRxGNGbWB69y_WXPYWEpjfe-b4irGBpvyuR86HwRFEXk8qcEdL56HkQl_3P_sVBUpm7b8HTLpBTNY7yIL87vVZuA33Nib7oNeNOFqVPUieT4GkRNkAjeafdzO_zVF3begKuWtGAvXmYmEofiaoEz4wYufp9t_d3hwr_xggE04QCvk0M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66719" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66715">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=VJT9_ZmP0oqq1aFnMmRdxYtQW6uKV5TRXFM3BpjxRMXFMjUCmSnyh62H9karZ_MWZW0cKUPL3jqbmIzJBbvQYRxM-JqIC41aHW0HzAIKjsU_aJI8O5R9h9KRRMApFm3btrx0ca82eKCCM-ovDm1Kvi3MepqpTVhxoQ0-C79PoN6_VdZdlKsIQLWwNGeutgU_iJ-1Mv6WHN2RzKE-BTq1uQtVuOM3chuWj5fddGz-A9iq6tHh1QqOd7aT52oJfuOFa7NXATdMcPM7XFBMTpZ8I-2pTiB8G4hmiXWA4VRltibxmXXZLrqeXC9gZAh1gyxRdfqN8ohism9HJurO4Sm_Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=VJT9_ZmP0oqq1aFnMmRdxYtQW6uKV5TRXFM3BpjxRMXFMjUCmSnyh62H9karZ_MWZW0cKUPL3jqbmIzJBbvQYRxM-JqIC41aHW0HzAIKjsU_aJI8O5R9h9KRRMApFm3btrx0ca82eKCCM-ovDm1Kvi3MepqpTVhxoQ0-C79PoN6_VdZdlKsIQLWwNGeutgU_iJ-1Mv6WHN2RzKE-BTq1uQtVuOM3chuWj5fddGz-A9iq6tHh1QqOd7aT52oJfuOFa7NXATdMcPM7XFBMTpZ8I-2pTiB8G4hmiXWA4VRltibxmXXZLrqeXC9gZAh1gyxRdfqN8ohism9HJurO4Sm_Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نخست‌وزیر قطر در گفت‌وگو با الجزیره:
این نخستین بار نیست که نخست‌وزیر اسرائیل با ادامه اشغالگری، گسترش حضور در مناطق لبنان و سوریه، خودداری از پایبندی به خروج از نوار غزه و همچنین عمل نکردن به تعهدات مربوط به توافق‌ها، موجب تشدید تنش در منطقه شده است.»
اقدامات دولت اسرائیل بارها به افزایش تنش‌ها و بی‌ثباتی در منطقه منجر شده و اجرای تعهدات و توافق‌های پیشین همچنان با چالش روبه‌رو است
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66715" target="_blank">📅 12:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66714">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=jpy2pCzJXRZq_EuyaGfcmwTFtdiH21XjiNCRiXPA5x48uE_XsWJ3iw4CUdd3SEK6-tuWKlOCu4tpagJFBOOmMbnvdsudD6QZznrNfhyKXSq8edvMAH4NFmBlwStmOwsZxINZlj5xQx99aNH3XoU7KhpG7S3iK0_NXXM_voTl_K0-aJV5d0bvSi5rFGb0x307Z7yWWQXHRjaDJ4a-LHGuSm-MYMTYKqrhG6xKmuOW-V4pGFaEFhr9C2J8k3dOxpXgCW91c1fK5PWIjkx0On7DJvt9Kfx6_IgKYShjgTQ_wQNzvPD4nr5f2zziv_CVfF4ch2OzpWl62yaQ9F6GMJbf1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=jpy2pCzJXRZq_EuyaGfcmwTFtdiH21XjiNCRiXPA5x48uE_XsWJ3iw4CUdd3SEK6-tuWKlOCu4tpagJFBOOmMbnvdsudD6QZznrNfhyKXSq8edvMAH4NFmBlwStmOwsZxINZlj5xQx99aNH3XoU7KhpG7S3iK0_NXXM_voTl_K0-aJV5d0bvSi5rFGb0x307Z7yWWQXHRjaDJ4a-LHGuSm-MYMTYKqrhG6xKmuOW-V4pGFaEFhr9C2J8k3dOxpXgCW91c1fK5PWIjkx0On7DJvt9Kfx6_IgKYShjgTQ_wQNzvPD4nr5f2zziv_CVfF4ch2OzpWl62yaQ9F6GMJbf1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسایی:
قالیباف و سایر اعضای هیات رئیسه باید پاسخگوی چرایی تعطیلی مجلس باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66714" target="_blank">📅 11:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66713">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=XzgoglALV--lF051bAhOxacwkrZwkrmAOI3FEl0Yb_ci68_CiAVDEMGuruZMaLkvU93_Y9yl9N033VbE5PtxtpZ7zJ41SGfI5gDeHi6HLAt8n7YkeC0WCrHmgLTf5bkdnRAwqYUcVqOOZITUcpL1GawcIdnaHsSKabBA-C1Mtae0CtheOzhlZS7GgyCciglobZY0UN-9tKmXQvHO3PPnFBvMsPDM-2tgcrvBPxIZoJJy1kJ29jHjs56JGX0lUdvYoMV18fG81cUtdeLdzJtIjtOBpigZOZuZ2vwjnu4iYGZfJT3mx98j7K58dUynBh_Y1hGZpJ5KjSJFQpIVeeJc-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=XzgoglALV--lF051bAhOxacwkrZwkrmAOI3FEl0Yb_ci68_CiAVDEMGuruZMaLkvU93_Y9yl9N033VbE5PtxtpZ7zJ41SGfI5gDeHi6HLAt8n7YkeC0WCrHmgLTf5bkdnRAwqYUcVqOOZITUcpL1GawcIdnaHsSKabBA-C1Mtae0CtheOzhlZS7GgyCciglobZY0UN-9tKmXQvHO3PPnFBvMsPDM-2tgcrvBPxIZoJJy1kJ29jHjs56JGX0lUdvYoMV18fG81cUtdeLdzJtIjtOBpigZOZuZ2vwjnu4iYGZfJT3mx98j7K58dUynBh_Y1hGZpJ5KjSJFQpIVeeJc-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور سر زده ناپلئون بناپارت و درگیری شدید با شیر تعزیه
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66713" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66712">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=tQ02eKvpQHZGva26fE7pv71OtntA-e8zcMUx1HYe6BvI3dfXBuHDnlCpLL7UmFMnqILKnbbLBrFe2ZF7rH0xmztYHZfNCmxJ5JsmBhMNIXE12GPdrtNPaAs2zvw9UKzZGdx-soIrLAyQgdn7JrqscXwxp3hK0XjolOOeZgRtrggPXBxbNVBqTrr9WM3SwXWL_liFAF1PnnE1QMOki6UzNCGTk5i_CFIgdrxRtj6OMnFWDrjElk3CasgXX1gQTw-9tIiZwCU3Cg2xda1YnoHfPrl84-3POfqwom5JOV8MYMNWRypd6unnxYFQRAqAh5qE6bkXw7X7swFGcPRxvTmK3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=tQ02eKvpQHZGva26fE7pv71OtntA-e8zcMUx1HYe6BvI3dfXBuHDnlCpLL7UmFMnqILKnbbLBrFe2ZF7rH0xmztYHZfNCmxJ5JsmBhMNIXE12GPdrtNPaAs2zvw9UKzZGdx-soIrLAyQgdn7JrqscXwxp3hK0XjolOOeZgRtrggPXBxbNVBqTrr9WM3SwXWL_liFAF1PnnE1QMOki6UzNCGTk5i_CFIgdrxRtj6OMnFWDrjElk3CasgXX1gQTw-9tIiZwCU3Cg2xda1YnoHfPrl84-3POfqwom5JOV8MYMNWRypd6unnxYFQRAqAh5qE6bkXw7X7swFGcPRxvTmK3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
کریس رایت وزیر انرژی آمریکا: آلبرت اینشتن ۱۲۰ سال پیش مقاله ای منتشر کرد که...
🔴
ترامپ: برای هیچ کس اهمیت نداره
😂
🔴
کریس رایت: به نکته خوبی اشاره کردین قربان
.
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66712" target="_blank">📅 10:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66711">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=l81mK8B2H4OJxgdJRhjyPYceaXI64UT_fEFyr_C1lFxW5km0mIQ9INfU9ERpwsTUKeEYQHwsqZVA0QPJphm7NBHqvBOpX1eVTT9HB7R6H2oplqGCnHuDoGKuC_AhH3CGw8YsbTpgUMXtL9vVyhByJeNPvvtQP4LKFB7ssYw_fCL6mzdltYpjdwe_tOfjqvi_jOkhu6d2l9oG7sABjiNAQLehbiroogFlLw3hs6VOSDUZsW5hKSi6z0bFXi0vZ-X_rCj3flLv6zVwElCTKYRx7zM3d9otB-fuO73R9WQsnwcOYSN8cWzurng4y9i1ZWmrvv1mY1EwM_M5mIsgFLpc1nmBCBa-J8K0d2b4obIWIqJIjLnlelJGaRT5Pl2NsDA4RZSoK8mDbElTI-xh07JNQm-5R1hKRi8GLM_q3OBZpENR8RiZ9QaujbQc23wdsTf9et7jTgki8d-ojIBX1Uu7jLbdSe5DagafjuT1EI0yJfoXGZM17ixoVVj3TigWva7e_XrPadsVQ7RccT1mCQTxHDVrcIJF4xrq7rrTMLtghLSF2zg1flL1OIqn4GA29VoJF5Xfjkao86i7Y-i6eg3lNp7YbgDNLJLIg8Xp0ee1fceIaBhHx2mO-S0SEcVq1g6DfqUM9muKl6DoNhIHMfZaECmpKyciv7De-B8IkQGY4Z8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=l81mK8B2H4OJxgdJRhjyPYceaXI64UT_fEFyr_C1lFxW5km0mIQ9INfU9ERpwsTUKeEYQHwsqZVA0QPJphm7NBHqvBOpX1eVTT9HB7R6H2oplqGCnHuDoGKuC_AhH3CGw8YsbTpgUMXtL9vVyhByJeNPvvtQP4LKFB7ssYw_fCL6mzdltYpjdwe_tOfjqvi_jOkhu6d2l9oG7sABjiNAQLehbiroogFlLw3hs6VOSDUZsW5hKSi6z0bFXi0vZ-X_rCj3flLv6zVwElCTKYRx7zM3d9otB-fuO73R9WQsnwcOYSN8cWzurng4y9i1ZWmrvv1mY1EwM_M5mIsgFLpc1nmBCBa-J8K0d2b4obIWIqJIjLnlelJGaRT5Pl2NsDA4RZSoK8mDbElTI-xh07JNQm-5R1hKRi8GLM_q3OBZpENR8RiZ9QaujbQc23wdsTf9et7jTgki8d-ojIBX1Uu7jLbdSe5DagafjuT1EI0yJfoXGZM17ixoVVj3TigWva7e_XrPadsVQ7RccT1mCQTxHDVrcIJF4xrq7rrTMLtghLSF2zg1flL1OIqn4GA29VoJF5Xfjkao86i7Y-i6eg3lNp7YbgDNLJLIg8Xp0ee1fceIaBhHx2mO-S0SEcVq1g6DfqUM9muKl6DoNhIHMfZaECmpKyciv7De-B8IkQGY4Z8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
دیروز یه لحظه بود که عراقچی وارد اتاق شد و به شما سلام نکرد. شما هم دست ندادید و بعدش رفت. آیا احساس کردید که به شما بی‌احترامی شده؟
🔴
جی دی ونس :
نه... باور کن، من چند ماه اخیر رو خیلی با ایرانی‌ها سر و کار داشتم. بعضی وقت‌ها واقعا برام گیج‌کننده‌ان به عنوان مذاکره‌کننده
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66711" target="_blank">📅 10:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66710">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=kBJ1RcauJUH0oY8WGo_ppsF5d93II775mzxQt-oTfWayGJJcP1Cvt-NpuZmDw44XiDGMNsnjASuNqJnth-KVMLgEGtTUGX8lRdoZHC5WIZFYnTlDOD5SKvmRssaq-meA7i9B5tJmSQmbmxuxsTcYqchnQmjzwOriqnNYMxQixE_O2Iu2ByWrERQOCOB5B_yo20h4bUTZKu3vBEHBRH0jZINrGJMG44PRLKkuZrJo1mw-S5Fuh02vsegjUgrVtBl4c6y7C4pAmoFO_1am9bw94ZsvBqAZInYuEvPt67VhHY3GGJWc1lUuy_JthiDNLoKmaJrFOzkfv83dc5KlwN9tFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=kBJ1RcauJUH0oY8WGo_ppsF5d93II775mzxQt-oTfWayGJJcP1Cvt-NpuZmDw44XiDGMNsnjASuNqJnth-KVMLgEGtTUGX8lRdoZHC5WIZFYnTlDOD5SKvmRssaq-meA7i9B5tJmSQmbmxuxsTcYqchnQmjzwOriqnNYMxQixE_O2Iu2ByWrERQOCOB5B_yo20h4bUTZKu3vBEHBRH0jZINrGJMG44PRLKkuZrJo1mw-S5Fuh02vsegjUgrVtBl4c6y7C4pAmoFO_1am9bw94ZsvBqAZInYuEvPt67VhHY3GGJWc1lUuy_JthiDNLoKmaJrFOzkfv83dc5KlwN9tFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شهبازی، مجری مفعول صداوسیما:
طبق تفاهم جمهوری اسلامی و آمریکا؛ از این به بعد شعار «مرگ بر آمریکا» ممنوعه و اگر کسی اینکار رو بکنه دستگیر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66710" target="_blank">📅 09:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66709">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=DdL1d3IsW-NFRkmkgJ6td8O9gvMYhGDZNODPm6Q2sY2hgsRJCIOyqdHcHnud2b9-AajnKZupOdovO70Ac3j7uYltodhRYOcFjeGLKCQ3QBt_ULmZtCslWFUxPy8A8FE_2CFY2hl3gN9ZQWca211VLqXAU1Ouz8AnbfEWv5wHrluIl5oZ2x40k6zE7Bj1GYxo7jKIOULmWxG1zjXFYluE73s_nFgGDxiT1d4aV8d_q4eaYLZwu-0eV3UhLd-DiFDPbNo668LGEnOLznNkWlsOzDhmRLq0Lt1ymh3Dy__m23sMG-fKm-7hNWtfKO57XSIYaepsctXzdifDZzl-9bd3wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=DdL1d3IsW-NFRkmkgJ6td8O9gvMYhGDZNODPm6Q2sY2hgsRJCIOyqdHcHnud2b9-AajnKZupOdovO70Ac3j7uYltodhRYOcFjeGLKCQ3QBt_ULmZtCslWFUxPy8A8FE_2CFY2hl3gN9ZQWca211VLqXAU1Ouz8AnbfEWv5wHrluIl5oZ2x40k6zE7Bj1GYxo7jKIOULmWxG1zjXFYluE73s_nFgGDxiT1d4aV8d_q4eaYLZwu-0eV3UhLd-DiFDPbNo668LGEnOLznNkWlsOzDhmRLq0Lt1ymh3Dy__m23sMG-fKm-7hNWtfKO57XSIYaepsctXzdifDZzl-9bd3wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
ما هرگز نمی‌خواهیم با آمریکایی‌ها در یک قاب باشیم
میانجی‌ها خیلی اصرار داشتند و ماهم گفتیم در آن قاب حاضر نمی‌شویم و ما فقط برای مذاکره می‌آییم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66709" target="_blank">📅 09:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66708">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66708" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66707">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NU3pmlvXxteL7-iipRzLL_kWDZJLZOmlyp1FhG_xwL0DAcdKumTOsxh7N0xugaRctB5VQ4eg-XE41MSiBr0S48_ElftnvkHlj2uYsDYtvy3CYywfmfHrVOgfVmpujXncej3iWNk6SE1AX7Wh1KHinrPBuJV989RifGx07R1mMp-XkkQaAE2DNhyaRjC7HxNlpFFcJvcN3Hd-wR2JSNp-eUnQchd2Nguxa_M_EGbD65mAUkrKKw5-p9Vlr4nuAg3z3B72kc5JKCyHjoVTDjlm4ro3gQX3Upy4apea_jGwolF_I73oi0McyryWhQRhlF7ib0pMctcrGcvqiaDkhkJZ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66707" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66706">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=e-2fF9bFr9TKZAst-7o_T3kceWLEg5d7lzU5hZQ6TItsDPAqwEmw4PKCIBQQ2loQNtSnet19YU3d9ZrsAlapDiiu5t0tIVyNgk2mrCwVLPusfaTLJrtC2mByvzXdN_CrpByocP5uJ3klcPju2fLju9d9o60Eb8PCDMYhQp9uE9JHuDRXxc-UNsT5W5bAbKaIh3KPqkFZ8KD_xDPdJcjWD5aHP01y-IylKAg9-aWb2Upbjw_oE-FeDL9LdGczWFvZnpasduS4U2Hnd7vPr2aAE577i9LzLHJPbkkSNF0B5TdrPi7TcS1PvWaMrZKsEQ2lLhT4ayVkkPUa4fpmmWrubw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=e-2fF9bFr9TKZAst-7o_T3kceWLEg5d7lzU5hZQ6TItsDPAqwEmw4PKCIBQQ2loQNtSnet19YU3d9ZrsAlapDiiu5t0tIVyNgk2mrCwVLPusfaTLJrtC2mByvzXdN_CrpByocP5uJ3klcPju2fLju9d9o60Eb8PCDMYhQp9uE9JHuDRXxc-UNsT5W5bAbKaIh3KPqkFZ8KD_xDPdJcjWD5aHP01y-IylKAg9-aWb2Upbjw_oE-FeDL9LdGczWFvZnpasduS4U2Hnd7vPr2aAE577i9LzLHJPbkkSNF0B5TdrPi7TcS1PvWaMrZKsEQ2lLhT4ayVkkPUa4fpmmWrubw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت‏ترامپ:
پولی که از حالت مسدود خارج می‌شود برای خرید غذا استفاده خواهد شد و غذا منحصراً از طریق ایالات متحده از کشاورزان ما خریداری خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66706" target="_blank">📅 01:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66705">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=oxhxga23ZrxKf1inQrbJnQB25K76_xnosE_1Cc3LJFOGjoVRqbfxMY1JXt6h7Cioyz7X7oIYYHkwXQ-pw30dpQx2tDlIUhn5oyugZlGP0nhC5TO515W3kcqI0OOt-qdMSPCTZG_rL3GrIIITteL5AUwXG2l2HzJIQziHpAApCa2whgbgqf6OUoFmTCidKiGEhWe3YnmG2bV8yQkcVk1ycLpEEAKvSsg2N-2h9ei8GZfh1qbYwhD-NSq99JgvTkJWsvInc8257aL5if7GGRKeB1dCRkXrMWkPgrfg8SdL4CaCHQlN8Q1M_kLwTDZ-o4ns1VQC9Sw3l4wmPUuCBs4yFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=oxhxga23ZrxKf1inQrbJnQB25K76_xnosE_1Cc3LJFOGjoVRqbfxMY1JXt6h7Cioyz7X7oIYYHkwXQ-pw30dpQx2tDlIUhn5oyugZlGP0nhC5TO515W3kcqI0OOt-qdMSPCTZG_rL3GrIIITteL5AUwXG2l2HzJIQziHpAApCa2whgbgqf6OUoFmTCidKiGEhWe3YnmG2bV8yQkcVk1ycLpEEAKvSsg2N-2h9ei8GZfh1qbYwhD-NSq99JgvTkJWsvInc8257aL5if7GGRKeB1dCRkXrMWkPgrfg8SdL4CaCHQlN8Q1M_kLwTDZ-o4ns1VQC9Sw3l4wmPUuCBs4yFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: وزارت خزانه‌داری امروز تحریم‌های نفتی ایران را لغو کرد؟
ترامپ: خب، من باید دقیقاً وضعیت را بفهمم. تمام آن پول به صورت خرید مواد غذایی برمی‌گردد. آنها ۹۱ میلیون نفر جمعیت دارند که نمی‌توانند آنها را سیر کنند.
خبرنگار: مطمئنی ایرانی‌ها از سود حاصل از فروش نفت برای بازسازی ارتش خود استفاده نمی‌کنند؟
ترامپ: قرار نیست آنها این کار را انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66705" target="_blank">📅 01:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66704">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A16BdBfw3WrYC3fiR-vKc676riVEmuOMF9tGL-9kvRfo4xiCsdFCszgJ2yxgZIFLamof9IkN8MrwnFrBKRdJ197FN1RO3KDFm2fVPnTjen-HDEVcynN97_JqGvYxOgcJJSJJT5wUSNqjA1Q_J54c_tGElhh1YrY8TO_Jgj74IhLKIdEpBtOnDkzhu1EEmgyCjTtQMAW3DUl6iujregShhqJW69HLF5WL-cg_EiOFefumIyPbDhZvw-anA2-zJg4V5k-tQVs3yJfsvA2Tde45Vk7aS_RApakZq37YP-JHLot2P9B26PsZQRsLpmwHWedde9PV_N3Y8GWAEedU6zlmGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
قالیباف: اگر به سوئیس نمی‌رفتیم خون بیشتری از شیعیان لبنان ریخته می‌شد
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66704" target="_blank">📅 00:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66703">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=h_J7XPSF5n-ZpwautXhsG3j5g3sonnr_Cji8WeoULujnllpSoxfpuT2NyK7oZyrKk_EzXkywuYhq3KbLquMWIKHQ4mT9L4JOsHwYYIafnNXs7L-jilXddhhkSAYD8-5TjD9zrqTxqPwUEZumKmW8sCAA3HFTxc47Lc4fQ3RGJl6gLgBZ701Fq_3NxwjgUcJzFAnu5vKRBoxXRynrhTYD3SlvIG0p4RAQT5IZI2Q24gb9WvLGxwaJDzWWPTqOlWteN7YicrDN1917Uy-EvODxRVs0bwSoz4djn13GuGDfbeW7o5Is1B260c5-3Mb5sPCzr_VKVz1P4NYfpGvpgebRkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=h_J7XPSF5n-ZpwautXhsG3j5g3sonnr_Cji8WeoULujnllpSoxfpuT2NyK7oZyrKk_EzXkywuYhq3KbLquMWIKHQ4mT9L4JOsHwYYIafnNXs7L-jilXddhhkSAYD8-5TjD9zrqTxqPwUEZumKmW8sCAA3HFTxc47Lc4fQ3RGJl6gLgBZ701Fq_3NxwjgUcJzFAnu5vKRBoxXRynrhTYD3SlvIG0p4RAQT5IZI2Q24gb9WvLGxwaJDzWWPTqOlWteN7YicrDN1917Uy-EvODxRVs0bwSoz4djn13GuGDfbeW7o5Is1B260c5-3Mb5sPCzr_VKVz1P4NYfpGvpgebRkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏قالیباف:
به خواست خدا، حاکمیت ملی لبنان بر کل قلمرو خود در این مذاکرات به یک راه‌حل نهایی خواهد رسید و تا زمانی که این اتفاق نیفتد، ما آنها را رها نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66703" target="_blank">📅 00:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66702">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=L7oMhj9rLdmySvkt8fDzhGQ6MsGNlCdwllw6T5OIQ9Ppoo4pI0fISdZFjckibXV50kmLLbHz6sMRswXw9IKYyk6jCxr64aMN5oxLn-EdUFgvCQZR24AhKikAXvDlJ-Jinw_ayu4CP-51K16F3bcdzlO2cIRCK1XNM45ybc4uL6sg9PYfnK1fXdBPwxMmvzkYKaWipbpg5hquJ1cWeSWDmm9JiQtDSoSuGehFuHctGaZOpV6GWorLkxaNZXp_7lPERU8ppBIVGrfXfIAsFO9nHlrm4UK0JKwYAMos4RqkSEZn_bza4TmQ67alFlsboTbugL8uBP5py9WQC1E18LMTDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=L7oMhj9rLdmySvkt8fDzhGQ6MsGNlCdwllw6T5OIQ9Ppoo4pI0fISdZFjckibXV50kmLLbHz6sMRswXw9IKYyk6jCxr64aMN5oxLn-EdUFgvCQZR24AhKikAXvDlJ-Jinw_ayu4CP-51K16F3bcdzlO2cIRCK1XNM45ybc4uL6sg9PYfnK1fXdBPwxMmvzkYKaWipbpg5hquJ1cWeSWDmm9JiQtDSoSuGehFuHctGaZOpV6GWorLkxaNZXp_7lPERU8ppBIVGrfXfIAsFO9nHlrm4UK0JKwYAMos4RqkSEZn_bza4TmQ67alFlsboTbugL8uBP5py9WQC1E18LMTDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور تانکهای مرکاوا اسرائیل در حومه نبطیه
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66702" target="_blank">📅 23:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66701">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146941c66e.mp4?token=CsupO_qImeErChevtRe8gT6lOCDZJq92x5adit90B3GB2vpN5kSOUJOWEW9h_phNO0_KlepdZ76RIcwEV6tiL0sZ3ENia_5FldcvBcGjnnZp7EQ0q-zCkGj2CkGyfSQ98Fnb9tnBFa1umQ5FPnimpu1t7y1whXDsYvHCCYn2495JKE2Iw_KNTb9dBwOAEqj4ghV_S_lr_Z0vGAKJz5TP3h5l3UgBDR-fjYf6lIdddjJG42cofVMomcwE8a3auo0HM9Lb9BKeAErex_SEzV_qyta-HK8RSNPt0dqQLD_KXKSh8nnAbLk7vk4WJ5HWHN3FNzNvJlQ5eYIpQYMp4rsg7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146941c66e.mp4?token=CsupO_qImeErChevtRe8gT6lOCDZJq92x5adit90B3GB2vpN5kSOUJOWEW9h_phNO0_KlepdZ76RIcwEV6tiL0sZ3ENia_5FldcvBcGjnnZp7EQ0q-zCkGj2CkGyfSQ98Fnb9tnBFa1umQ5FPnimpu1t7y1whXDsYvHCCYn2495JKE2Iw_KNTb9dBwOAEqj4ghV_S_lr_Z0vGAKJz5TP3h5l3UgBDR-fjYf6lIdddjJG42cofVMomcwE8a3auo0HM9Lb9BKeAErex_SEzV_qyta-HK8RSNPt0dqQLD_KXKSh8nnAbLk7vk4WJ5HWHN3FNzNvJlQ5eYIpQYMp4rsg7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعتراف
کارشناس صداوسیما: نتانیاهو خسته نشده،این یعنی مرد»
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66701" target="_blank">📅 23:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66700">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff06705953.mp4?token=nIPvv763mcZSg-eHLcgfS6L-6nJwC7HpFr1-3aD7t0_PYVbUxyMXn8BDw373QeNipni7TcA9lYZPUb_-XagDUshBAImNqK4Z63F2aHa1PSreN6oyyQRP8C4eU6FnEpPQXaEYsBEpa6XtfwH6RQHhh-WAJ5lYZqjsRhJu4i55Vk8AXk7zUmBPYIE9rXQgYgPaN-ZQU0-Yu5PPeFl8teOQ6RXubeWgcPYJh07Dvp__0BlkBzjjYYygtYyhzvF6RP2nQAnTqlWoZtdffvjtwnDdajHQ_Det4IZc1WsV91sKbWq8NBz89DTcW6pZGnTE7LCCljqul9nmONm_3l_XcZ1FBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff06705953.mp4?token=nIPvv763mcZSg-eHLcgfS6L-6nJwC7HpFr1-3aD7t0_PYVbUxyMXn8BDw373QeNipni7TcA9lYZPUb_-XagDUshBAImNqK4Z63F2aHa1PSreN6oyyQRP8C4eU6FnEpPQXaEYsBEpa6XtfwH6RQHhh-WAJ5lYZqjsRhJu4i55Vk8AXk7zUmBPYIE9rXQgYgPaN-ZQU0-Yu5PPeFl8teOQ6RXubeWgcPYJh07Dvp__0BlkBzjjYYygtYyhzvF6RP2nQAnTqlWoZtdffvjtwnDdajHQ_Det4IZc1WsV91sKbWq8NBz89DTcW6pZGnTE7LCCljqul9nmONm_3l_XcZ1FBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏اوکراین یک کارخانه تولید تجهیزات الکترونیکی نظامی و واحدهای تأمین انرژی سامانه های موشکی و راداری روسیه را در شهر ورونژ در جنوب غربی روسیه با موشک های بالیستیک هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66700" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66699">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=IhGeT7rLJd077pHkZA-8bZoUAhNdDksyTuO9XrB3L-LSA1bZrouCQNgjU5IwXcq7VJC2ekS2sGcp3TZLLvEEVYYhhid0tSLJKpiV6_l7gbpZ6YtwwqkVfmzHuEFRXdUnIVO2j1jafFsXS4hL77oDye55GPhI1zTuEjJBn9iqoPVQWKMWXjGVBNrHqktc6DQKz9s38e3PT0bYURHSFoqwLtGuDL3O-nH6kHHLMO6h69Z5BlldTztjZ8ZtiBMlWml7Q5MGMlXC268NUeyLTvAs18B-053Qhh2jPUKY7cVB-iJmQiBbJu8Q18N-AC5woGjRERl2P-sOigGjW36ZpJsahQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=IhGeT7rLJd077pHkZA-8bZoUAhNdDksyTuO9XrB3L-LSA1bZrouCQNgjU5IwXcq7VJC2ekS2sGcp3TZLLvEEVYYhhid0tSLJKpiV6_l7gbpZ6YtwwqkVfmzHuEFRXdUnIVO2j1jafFsXS4hL77oDye55GPhI1zTuEjJBn9iqoPVQWKMWXjGVBNrHqktc6DQKz9s38e3PT0bYURHSFoqwLtGuDL3O-nH6kHHLMO6h69Z5BlldTztjZ8ZtiBMlWml7Q5MGMlXC268NUeyLTvAs18B-053Qhh2jPUKY7cVB-iJmQiBbJu8Q18N-AC5woGjRERl2P-sOigGjW36ZpJsahQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس صداوسیما:
نه تنها از کشتی ها در این شصت روز عوارض نمیگیریم بلکه قراره آمریکایی ها بعد شصت روز بیان و عوارض بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66699" target="_blank">📅 22:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66698">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZwcnSSWVmvyYcU947GrNOlh6EwhsvdA0N-eunZx_AegUROFzXUFVWWrudjVNsTpdidtbjvNcVgVJ5sblqVaIH5-4H8qdj-xuM2x6D4Tpw-DHGr9v9YdWgFOWyZ9-bQPawcjgJ7QpvcraOgmvYMf9Gqegs2nbT5sVB6muaszx-KZU-xbNNjr-kXfOQsQH350L3xkn5AAu7oPn6nhlykxnKGc8wUVwiMeq3RO3drdJoGc2P0bO8OesIo_OByq96OdkoItqRsvl2O1wTYer8n88C1RShyCBeTdSTSyKms7PetMe0XNvtD1NaK0r80bygW51vq4pW-RYeKA71S2ZbNpdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
وزارت امور خارجه آمریکا تایید کرد مارکو روبیو از ۲۳تا۲۵ژوئن به امارات، کویت و بحرین سفر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66698" target="_blank">📅 21:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66697">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAZTKj9I2B7tAbAs6Y7hPaqrhZNd6dpqma9mn9TkGb89XsuyN3_a4RyiXQw-bsxUO7F9_vb4PM7xNy6IlZbSas1-ZHDQWvHUoKWLOB_jOeYHIkp3PlslBtYtCEvbw7TBfiesJafHP84eLi0TFghw4L1J8gGKZ_42XDuXFQbL5qU4y96GZGS64fneFLIr2RKrtdBBT8zY0CgO3q1_iuXgdq9F_oeovggKRhoBUkoBSrpNarYlbm0rmXg9lGecB4D1B3_WKh5K3UvYq1iXcmmjwM2MtOTifOZ2ubszb8_TzcxiSK3pxeNOJq7rNPS3-Mfg6Wtn-wP6NWa6HJCMbi8G3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
همه کاملاً آگاه هستند که ایران با بازرسی‌های عمده تسلیحاتی موافقت خواهد کرد تا «صداقت هسته‌ای» در آینده طولانی تضمین شود. رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66697" target="_blank">📅 20:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66696">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDb4liMACnXzs1xdKrq78ZhSl7qJAyaX7YOgevvXzNhaUgo4jsTAPRXBsEIuavoD2G7bpYZCZ4lxp2zoCQE00e5NG6HHSgre3i5hBF7f1E8SgZQ8jqDSvnxTmF5PeTIvCuvXBy6eNiwE4sQv3jIqA3bowUm17qIJtZELlWQBGgVn2C9g1_YyMskYgCXGAenWCVDngugY0wFFPrvBZ7TpiT0z1HSv1R4WEe3R07mgRomtWTAEXqLmPQilRBFPXaUikrWYFKkRpc9GsonI6SAHeViFKfIeQ0VF5uZXSWb6071-CkfyZuJlAEVn09rw8n2zwwN29E9njJ3IGG6GsTiROA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏رجا نیوز:
در حالی که جریان رسانه‌ای حامی تفاهم‌نامه اسلام‌آباد تلاش می‌کند آن را یک دستاورد تاریخی معرفی کند، اظهارات «جی‌دی ونس»، پرده از ابعاد فاجعه‌بار و تحقیرآمیز این سند بر‌می‌دارد.
سخنان ونس نشان می‌دهد آنچه به نام «آزادسازی دارایی‌ها» به ملت ایران وعده داده شده، در عمل یک سازوکار استعماری و نسخه به‌روزشده همان طرح «نفت در برابر غذا» است که این بار قرار است عزت ملی را به گروگان بگیرد.
ونس با بی‌شرمی تمام، مکانیزم طراحی‌شده را اینگونه تشریح می‌کند: «اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند... سپس آن پول عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد.» او با وقاحت می‌گوید با این پول قرار است جیب کشاورزان آمریکایی پر شود.
مشخص نیست این توافق چه نسبتی با پیروزی‌های خیره‌کننده ایران اسلامی در میدان نبرد دارد؟ آیا خون شهیدان میدان، باید پای میز مذاکره با وعده «سویای آمریکایی» معامله شود؟ آقایان مذاکره‌کننده با چه منطقی پذیرفته‌اند که حق حاکمیت ملی بر دارایی‌های خود را به «حق وتو» و «نظارت» آمریکا و واسطه‌ها واگذار کنند؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66696" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66695">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66695" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66695" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66694">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oplACL6sAWEjumMRNz7_tDix5zeuGoaposGcPzB6C3pZ0jD3NVJ7IIxa-gYUy_eb4TmWdZK98KkYc3vdZBGR3Va2qyebhz0UyA4JX5vSkGXxYdWuVJAh4RvG6SlQRKA6kvOn1O3HpkPiR9kHTD8M4UgyqyDLY-1CyPivF8LZkxYTh0NiNg7YVXWO9kp02jRpdCmHuJyKI68SsufUBrVv9q2gpRgSXGR7_k_-2F_n8qsOxXDsCOixiv6aRUr30YrtrWRueWRpXX20ANwK2mX580X4d0JMfheK_J2XV26iY7bJINIfFwSTxc4eOWeMpDOWMy8e3cQGKgVNrTERMnF5cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
پرومو بزرگ والیبال Ace Arena با جوایز تا 5000€
🔥
🎁
جوایز اصلی هر مرحله:
📱
آیفون 17 پرومکس
🎮
PS5 و Xbox Series S
💻
مک‌بوک پرو M5
⌚️
اپل واچ سری 11
🎧
ایرپاد پرو و هدفون سونی
🎟
کد تخفیف تا 50€
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66694" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66693">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8KLjFeAEa1RGUmuYDbvo6fqWZhUGdCmgMjDd59n0wzRwwFHjttLjXSZgbrS8kYJENgSUZHVzt6_ukwBEyquplwCwNGzIOSNFMJVZ-kHvpxtGp7JQin2tvp51JgjUviW-Z7w_K7jQiqe41qzDt9t1BKtZFA_UV6KPuYA0ZkHPaS5To7p4TGGb9xhiZAXp7cqZZpFlYnY6n6BpGA5GgqDIi-W7U9TKvxNJmH7nQeTrn6Q9K2tFFbb71H1rj-1EEyxpK0KgKzc-FHE60eKYtDO6to-LUE82cluLyLHuDHKRE-s59VseEv436wCx_rxpKvIYodebxtF5ahiaT5r6AFJiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی به ایران صورت نگرفت. تبلیغات غربی را نادیده بگیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66693" target="_blank">📅 19:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66692">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f18d416253.mp4?token=gVTg9KOPF0V3ZK08J6r9qD-uljwxSBMUOsOC9Xeo5tewLfEA2y-O80zowdjCaqIwceVQ3LZcF5kwIcGd6TPD3pvlnCmMb858OznZ4CoqG5TBQQt25J6jcCotNRNbRG9e0MvzxQHuTecJaP-UO-O0ysUDzRCNd1K62K4OUT5oVs4c_8Mme3LjECarwTbyRUIeu_RQ9AFNC6TOjO9oK_GPeYCztEeZ3qwJ2tu-rjNs0LMyyhJLz5KmlnbVaLQ4HKXudxXdeTswGfnNxnd9hEzTZBvFT_Kgs6EigIpVFWrJ8b9xa7XWTi3eso5p7nuYltCp05TYlymWhXtg7ZIzmy7zModYy9WXF-JEVK219nt7wWrHFacnGZGfe-0uavIU8HRanF4opbyUdL8voUdwubqczEIvUSKg9mtNE7E59nnP7fOr7Wlaq0EJTk4r8VATKs7QyLoENG8TTTQX6HOLq1T9zBG3mLWKMlBXs-xbFCecfsA8mbZaQEt-waWLvwa_hZFnyaqRpsC2vT5s_L8iod2sMf8jSwUybvrbcNHf8ryXe7NPj3B1wVTs9ceVxxfudXeqeEK5SAAT9O6IJITcWUTKYPM6GUipblMNLkaxttjFoxaRJzhnMzJmjcFSuGApUS6ju-KhMZywd9auJMPad9kDikHCA84YPyMKBaMrshyJB6o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f18d416253.mp4?token=gVTg9KOPF0V3ZK08J6r9qD-uljwxSBMUOsOC9Xeo5tewLfEA2y-O80zowdjCaqIwceVQ3LZcF5kwIcGd6TPD3pvlnCmMb858OznZ4CoqG5TBQQt25J6jcCotNRNbRG9e0MvzxQHuTecJaP-UO-O0ysUDzRCNd1K62K4OUT5oVs4c_8Mme3LjECarwTbyRUIeu_RQ9AFNC6TOjO9oK_GPeYCztEeZ3qwJ2tu-rjNs0LMyyhJLz5KmlnbVaLQ4HKXudxXdeTswGfnNxnd9hEzTZBvFT_Kgs6EigIpVFWrJ8b9xa7XWTi3eso5p7nuYltCp05TYlymWhXtg7ZIzmy7zModYy9WXF-JEVK219nt7wWrHFacnGZGfe-0uavIU8HRanF4opbyUdL8voUdwubqczEIvUSKg9mtNE7E59nnP7fOr7Wlaq0EJTk4r8VATKs7QyLoENG8TTTQX6HOLq1T9zBG3mLWKMlBXs-xbFCecfsA8mbZaQEt-waWLvwa_hZFnyaqRpsC2vT5s_L8iod2sMf8jSwUybvrbcNHf8ryXe7NPj3B1wVTs9ceVxxfudXeqeEK5SAAT9O6IJITcWUTKYPM6GUipblMNLkaxttjFoxaRJzhnMzJmjcFSuGApUS6ju-KhMZywd9auJMPad9kDikHCA84YPyMKBaMrshyJB6o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانی‌جماعت حتی کف آمریکا هم باشه بازم دست از کسخل بازی برنمیداره
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66692" target="_blank">📅 19:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66691">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=BjFfpt3UBi-bqKSuoXjb6-bM-DrhqiRvhFq7KLSJdkQRGj8peJRvAYaqDo3GSjjg09mwYwn3kvpA0wsG_Hbw999ip-IVO4jyRhWHCMcerVza-wURoV7Ko5M6xv7ebKv9kUhbklSw4DuJ7FlClTi9Bza7gYvldhvVg6-xAt_I4KmP9EkYV8jzewOFIZ3HiCEdoCSp8OVgVYnqZsDicOYDNGk6n39tiwdbwPu1hDcdpEZPLqw2anaqVobcSSILd8jJENITAXW5jc6xJES4_7TFrsGpn2P28SPZB07j_xPWTXba3BVLWrVB-r6SV9cqq_1fjLF18F_ugS_JlTQtW-26jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=BjFfpt3UBi-bqKSuoXjb6-bM-DrhqiRvhFq7KLSJdkQRGj8peJRvAYaqDo3GSjjg09mwYwn3kvpA0wsG_Hbw999ip-IVO4jyRhWHCMcerVza-wURoV7Ko5M6xv7ebKv9kUhbklSw4DuJ7FlClTi9Bza7gYvldhvVg6-xAt_I4KmP9EkYV8jzewOFIZ3HiCEdoCSp8OVgVYnqZsDicOYDNGk6n39tiwdbwPu1hDcdpEZPLqw2anaqVobcSSILd8jJENITAXW5jc6xJES4_7TFrsGpn2P28SPZB07j_xPWTXba3BVLWrVB-r6SV9cqq_1fjLF18F_ugS_JlTQtW-26jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😂
یمنی‌های فلک‌زده بابت گل مردود تیم قلعه‌نویی اینجوری دیشب خوشحالی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66691" target="_blank">📅 18:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66690">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=itgchpxjOf5YITMgRPaOIQSO7nRF4gIEaMi6duvpYksxY2MdTSd65eZJNiMYUn73oc-JoKUlARxhKymP36RCY555lYwHvZ59rxDa6SbkUpQWau2Zeyk9s9HblBR-Cxw-MCTi9bS_3df_3Y6KkSa6FrDkEhSA7Gg7CiD47Cw3RMw9279kjRe9Nj3vTBnCOHzYv7uIVR-bKI7eu-98XaLoqYcxRV9KrspGnlRFim5ffczA3caRyo_RIzh6HMH-t9LTMha2SJrUd1t-0z3rINcyly4IgEcK_Rl9XjMdy2QSsq87n_7yM0nBMGyFhuCxQ-j03UIt9fSCS2e6pzs_FsFoRjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=itgchpxjOf5YITMgRPaOIQSO7nRF4gIEaMi6duvpYksxY2MdTSd65eZJNiMYUn73oc-JoKUlARxhKymP36RCY555lYwHvZ59rxDa6SbkUpQWau2Zeyk9s9HblBR-Cxw-MCTi9bS_3df_3Y6KkSa6FrDkEhSA7Gg7CiD47Cw3RMw9279kjRe9Nj3vTBnCOHzYv7uIVR-bKI7eu-98XaLoqYcxRV9KrspGnlRFim5ffczA3caRyo_RIzh6HMH-t9LTMha2SJrUd1t-0z3rINcyly4IgEcK_Rl9XjMdy2QSsq87n_7yM0nBMGyFhuCxQ-j03UIt9fSCS2e6pzs_FsFoRjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
دستور من و وزیر دفاع به ارتش اسرائیل واضح است و تغییر نکرده است: رزمندگان ما در جنوب لبنان آزادی عمل کامل برای خنثی کردن هرگونه تهدید مستقیم یا نوظهور علیه خود یا ساکنان شمال دارند. ارتش اسرائیل هیچ محدودیتی در این زمینه ندارد. من پشت سر آنها ایستاده‌ام، تمام ملت پشت سر آنها ایستاده است. من قاطعانه می‌گویم که تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهیم ماند تا از ساکنان شمال و همه شهروندان کشور محافظت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66690" target="_blank">📅 18:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66689">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=UkjtKV0kYWjYWn0eQD8eN8NcAiic0fzeOJMnfcQSHLv2MQ5fwgKuX9m0YEbURlY3vsvECmTxHhqznnpsV7v9ckV5z2O7YDCnIREybBCO3Q5189KZO0G2TWPGkZXuMqqiBsiWcUpzJCRKOrWuKxPdfMBMpn5Of2yJs8_T2knWoP698KXgUwvjwNOnj87Nve-igfPCfO2USaNPU3nBUCho0G6o77pEEmEjhoFjSeu5HK9nUczBV3iUIgXK4OmmjtCLhYTrVp_kFry56HFD4CeyV55VFj3ZwEpm1bXoOaVTzPKWwMkZGWKIQXjq6GCQQlBx318_HMDghORPjmMM8rPEfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=UkjtKV0kYWjYWn0eQD8eN8NcAiic0fzeOJMnfcQSHLv2MQ5fwgKuX9m0YEbURlY3vsvECmTxHhqznnpsV7v9ckV5z2O7YDCnIREybBCO3Q5189KZO0G2TWPGkZXuMqqiBsiWcUpzJCRKOrWuKxPdfMBMpn5Of2yJs8_T2knWoP698KXgUwvjwNOnj87Nve-igfPCfO2USaNPU3nBUCho0G6o77pEEmEjhoFjSeu5HK9nUczBV3iUIgXK4OmmjtCLhYTrVp_kFry56HFD4CeyV55VFj3ZwEpm1bXoOaVTzPKWwMkZGWKIQXjq6GCQQlBx318_HMDghORPjmMM8rPEfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66689" target="_blank">📅 17:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66688">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMRi392gCEMKJdVi5Bp7wV8RqIVWYwAp5L3cj_-1AxZpy1N-0XQpfmbZ0PKXJUUvceKHWe72G3OKBjz8SJOJp7liOlThcOR-UoFOsTQW3HA2ZSUPsvG8FOYvu9aPks_Rv9sqFbocR2ach6sO30N6bYNp8P3HoP9nysDCr35yiW0zAdyZq8XFyZZosqSXWnBQXd_H_VtaWcHpNRZpXiEq-O8lW_wQZjxJWDOCmGkJD9QEoby0n75owfCd9U6YWYiG0Z166zQqdUH4pSLzEqM2itVjVuRm_wr7dfKWk-yf6lZ_GWV1DuMeu-0UnrqRZViywbYCE3qn2UPpsXQYFs4pdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اسکات بسنت وزیر خزانه‌داری آمریکا:
تحت ریاست جمهوری دونالد ترامپ و معاون رئیس جمهور، ما همچنان به امن‌تر و مرفه‌تر کردن جهان ادامه می‌دهیم. در راستای مذاکرات سازنده جاری در سوئیس، ایران متعهد به ترانزیت آزاد و باز در تنگه هرمز و اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به کشورش شده است. به عنوان بخشی از این چارچوب، وزارت خزانه‌داری یک مجوز عمومی موقت ۶۰ روزه صادر کرده است که تولید، تحویل و فروش نفت ایران را مجاز می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66688" target="_blank">📅 17:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66687">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=Q8PnpvHFb6t8TmIizTYOgcpgiDh51hzpXDwqJYNwA7m5rXlP4vEEGmBTCIB2WWiSdYd8__QQ6pGoqU71ONo1LhQY8lYRwBL0PKfGHD8LWM162PJSeSwpdXFtDZamwOmj1GEPae6berCaVC8U63NyUcxS4KRUtmp8aRh7Qk3XCUMF1Qo9yAUIc4qu97EhS0RHPxlr5pg3xpmVH28qKD-Kz122a39IFP1Mv1f6DsQCy0hgwc_8OC81P4ISgFDRAVoREpO-3_tqjg_-KdEvJjJtA8ALDmkftJscZrf_Ry5RFO6N9dME5ZqSrjybAGkWxkHzdZ1wSYqLURPF_31NU3_YhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=Q8PnpvHFb6t8TmIizTYOgcpgiDh51hzpXDwqJYNwA7m5rXlP4vEEGmBTCIB2WWiSdYd8__QQ6pGoqU71ONo1LhQY8lYRwBL0PKfGHD8LWM162PJSeSwpdXFtDZamwOmj1GEPae6berCaVC8U63NyUcxS4KRUtmp8aRh7Qk3XCUMF1Qo9yAUIc4qu97EhS0RHPxlr5pg3xpmVH28qKD-Kz122a39IFP1Mv1f6DsQCy0hgwc_8OC81P4ISgFDRAVoREpO-3_tqjg_-KdEvJjJtA8ALDmkftJscZrf_Ry5RFO6N9dME5ZqSrjybAGkWxkHzdZ1wSYqLURPF_31NU3_YhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
استودیو آیت‌الله BBC رو مشاهده می‌کنید بعد گل دیشب طارمی به بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66687" target="_blank">📅 17:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66686">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=HM7Av_k0fvituTBmgfm1KypIk43vHNDeIJxPKHUyfjZZJPTZSw3mGPUUj78unY4muHa4t-r3gaFFYv0r_s3nO6gQg9BVo4dCFOrLH3MxBSzg-bnFdYklODcuWj3fhAm3m7kJJVWEtSTgbgGvYrxI5sTB4AF5hqefxjt3F5OqQf73uY84hgTUl8aK-cX63G3fngqttatr3QLORzUZVACnvQcb19Xx37d1jaSuX5-jvMgdYyeXF7KtUAXkJ4gOf-1DsO2Q5uwH67QqaxHeR-E82iJl4IB8K2ZNv_2ZZ1TiY8PfHz26T6vB5jvhbC5zJYcjTlp_suVhFw3f6mdZ3Zf4QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=HM7Av_k0fvituTBmgfm1KypIk43vHNDeIJxPKHUyfjZZJPTZSw3mGPUUj78unY4muHa4t-r3gaFFYv0r_s3nO6gQg9BVo4dCFOrLH3MxBSzg-bnFdYklODcuWj3fhAm3m7kJJVWEtSTgbgGvYrxI5sTB4AF5hqefxjt3F5OqQf73uY84hgTUl8aK-cX63G3fngqttatr3QLORzUZVACnvQcb19Xx37d1jaSuX5-jvMgdYyeXF7KtUAXkJ4gOf-1DsO2Q5uwH67QqaxHeR-E82iJl4IB8K2ZNv_2ZZ1TiY8PfHz26T6vB5jvhbC5zJYcjTlp_suVhFw3f6mdZ3Zf4QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیعت با رهبر مقوایی
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66686" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66685">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=uOb91AT0b9HsAD0rQvdfk3Hbo_5j3wGGJ8To4x75mYLy9WmRYYArUuySeSuACO0ELb7cltf-6n-KwURe-8mDlUrFPkH1NtotjPM2FWmKEHB__nenXUJbvKgsFVOAnU-6NDgcACbDDMDYtEcIZFMoe7o0fL3Rol0FkcSbVk31ldW5Xl1iG3i1vx_IxLhDOK6oj6C2MUE6ZSNAzSycyP1jTsGGQD9hs8zZ4LRC24pa_HP92qFovSuQKZ4sHNbOi4yezD0LGXdEhbLcVISens6__dHgJaPRG2heK22RHU6rS8F6-pVXXcmzdqIh576lJPIYMEmWtoZ8wHp4EyYfv6MSCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=uOb91AT0b9HsAD0rQvdfk3Hbo_5j3wGGJ8To4x75mYLy9WmRYYArUuySeSuACO0ELb7cltf-6n-KwURe-8mDlUrFPkH1NtotjPM2FWmKEHB__nenXUJbvKgsFVOAnU-6NDgcACbDDMDYtEcIZFMoe7o0fL3Rol0FkcSbVk31ldW5Xl1iG3i1vx_IxLhDOK6oj6C2MUE6ZSNAzSycyP1jTsGGQD9hs8zZ4LRC24pa_HP92qFovSuQKZ4sHNbOi4yezD0LGXdEhbLcVISens6__dHgJaPRG2heK22RHU6rS8F6-pVXXcmzdqIh576lJPIYMEmWtoZ8wHp4EyYfv6MSCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوش‌چشم کارشناس خبره صداوسیما بعد اینکه عادل فردوسی‌پور بهش رید اینجوری واکنش نشون داد
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66685" target="_blank">📅 16:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66684">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=tDIbWNkvZRFrMQkavsGHCcEoP-dm_oaxcvOln3MY2r3K0AmBKnBxLY2_VgfpAxTjQGNMSGgTC8-OYzGpMSN_SyMgrRi5oOIqgSdh4-ay9hacx_KaAqLY8uqYHWQZldTNcchCHAsf-94l0FWzgs0gqP_kg9bPAusNZBHWQrjPvt_-8dZSJloBCf5XUn2UhdJE_6kovEIk35eFUT-r2RmFW7PybUEAMdZgHAl3X6emtS9S5boR1lyg4ihbv5aIgnWn3NO8Mt-_vpfrMwPNX_xaCnPPnq6TbDcqt_09tAFImL0vd2QCChaPEEYkVlcc9GyNtjuWgkB6lIS5QorU6pQz9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=tDIbWNkvZRFrMQkavsGHCcEoP-dm_oaxcvOln3MY2r3K0AmBKnBxLY2_VgfpAxTjQGNMSGgTC8-OYzGpMSN_SyMgrRi5oOIqgSdh4-ay9hacx_KaAqLY8uqYHWQZldTNcchCHAsf-94l0FWzgs0gqP_kg9bPAusNZBHWQrjPvt_-8dZSJloBCf5XUn2UhdJE_6kovEIk35eFUT-r2RmFW7PybUEAMdZgHAl3X6emtS9S5boR1lyg4ihbv5aIgnWn3NO8Mt-_vpfrMwPNX_xaCnPPnq6TbDcqt_09tAFImL0vd2QCChaPEEYkVlcc9GyNtjuWgkB6lIS5QorU6pQz9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب تو ورزشگاه بعد بازی دخترا اینجوری قربون صدقه بیرانوند رفتن. حیف دوربین رو صورتش بود وگرنه معلوم نیست چیکار می‌کرد بیرو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66684" target="_blank">📅 15:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66683">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=ihBQZ95pq-7EdzW2FDbDgtacBgGGnbqoGiwMHzCzJGygOpZLThI060fvVB3Er1z3HGnWrZ81fG7haR7n2bKZwiMFf4rzsfjteexhnUmrFqOnQjVujh7W8IRV97InTXcjsq4uDz_SJhr48eGEvgnsosekzyuKxCgrEuodeCCjUvAyzjYaJNTKMU-PApclpt-P8S52z2Q-YRYXp6nX6VQbwFpKeyf2HBtjAzUNh5B0TyH6SgVIqfcWgTH5yB29HUpX1R0H4dHiG8_P0REr237IBPpzfqCrtDbkJd2F4WPX5EwgCfJp8Ai-GPoai2UL9bwjaKyPcWx1DKVVZnj3mT4fIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=ihBQZ95pq-7EdzW2FDbDgtacBgGGnbqoGiwMHzCzJGygOpZLThI060fvVB3Er1z3HGnWrZ81fG7haR7n2bKZwiMFf4rzsfjteexhnUmrFqOnQjVujh7W8IRV97InTXcjsq4uDz_SJhr48eGEvgnsosekzyuKxCgrEuodeCCjUvAyzjYaJNTKMU-PApclpt-P8S52z2Q-YRYXp6nX6VQbwFpKeyf2HBtjAzUNh5B0TyH6SgVIqfcWgTH5yB29HUpX1R0H4dHiG8_P0REr237IBPpzfqCrtDbkJd2F4WPX5EwgCfJp8Ai-GPoai2UL9bwjaKyPcWx1DKVVZnj3mT4fIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس در مورد لبنان:
گاهی اوقات یک فرد جوان پهپادی را شلیک می‌کند که از فرماندهی عالی تأیید نشده است.
البته، اسرائیل باید به آن پاسخ دهد، اما اگر اسرائیل در چارچوب گفتگویی که بین حزب الله، لبنان، اسرائیل و سایر شرکا در منطقه در جریان است، پاسخ دهد، می‌توانیم وضعیت صلح‌آمیزتری داشته باشیمما معتقدیم می توانیم به جایی برسیم که
حاکمیت لبنان و همچنین امنیت اسرائیل حفظ شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66683" target="_blank">📅 15:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66681">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=NMUopyd6X3wLvoG6WL9B6UwelxHRftSjp-ySr8XRoWfRayEI1d_bUoS1Tt8mE9mAqbIC4OpJYOX3HLlC5nhD5KjMNgvps_nUdbejoRbpezOdD_-vQPyYcTHwUAnbAWBLIkdkR1H7F7QO63cAP3TFKlOEwdPE7DHj7c3YF9tUChmq8rU3Rc4meILNssk6gfBjvq6zeW91aixTmKwrwv3y259ebkc6iru_3NZzknIz26830vL2ZCcu9EutosoLRP-mfzrut0Uzk4Ahw3i5Beb5klalM6yxaOyBroPgGd2oVp16UVRHAABnop5P7eQPiKO4vyRaddJSF6FxVu-ZeLWgnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=NMUopyd6X3wLvoG6WL9B6UwelxHRftSjp-ySr8XRoWfRayEI1d_bUoS1Tt8mE9mAqbIC4OpJYOX3HLlC5nhD5KjMNgvps_nUdbejoRbpezOdD_-vQPyYcTHwUAnbAWBLIkdkR1H7F7QO63cAP3TFKlOEwdPE7DHj7c3YF9tUChmq8rU3Rc4meILNssk6gfBjvq6zeW91aixTmKwrwv3y259ebkc6iru_3NZzknIz26830vL2ZCcu9EutosoLRP-mfzrut0Uzk4Ahw3i5Beb5klalM6yxaOyBroPgGd2oVp16UVRHAABnop5P7eQPiKO4vyRaddJSF6FxVu-ZeLWgnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
ایرانی‌ها تهدید به ترک جلسه کردند، یا حداقل تهدیدهایی در رسانه‌های اجتماعی مبنی بر ترک جلسه وجود داشت، اما آنها ترک جلسه نکردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66681" target="_blank">📅 14:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66680">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس:
ایرانی‌ها موافقت کرده‌اند که بازرسان آژانس بین‌المللی انرژی اتمی را دوباره دعوت کنند.
همچنین دارایی های مسدود شده ایران آزاد نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66680" target="_blank">📅 14:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66679">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏جی دی ونس:
من نمی‌توانم 60 روز آینده اینجا بمانم. به ایالات متحده برمی‌گردم.
تیم‌های فنی مشغول به کار خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66679" target="_blank">📅 14:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66678">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=g0Q5oZ5bPe7KjnNhqRnE2EPSMrt1mL_of6oxJsjfETUpEWrEfGbuLLyEpw3A6oq2-ZwP87Zq1f7_HyvDjmkDcjtcHb3lg0nW1V-OEIaVHtf9yeaxRaiyzwGglVv6nqFyCz1zG0VigSZnNxmMxfjzqLTBesiYWPFjpcbovfom_4iAbOnSmQ70muf6ciW08OUIlwjnvSG1lSIBWEeUowu2QS7dy8FlfVk0SUVTE0DVKC_X5U9hVk3RTb2H-tpQsyRZUX2hW25-6pshCz8zMg6k1nnulzRkZaPT9PWO1L0-HRpS8B34wxA2YIoauKQ_oJ1qNnCkiZcgKAnwrZE02z6zog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=g0Q5oZ5bPe7KjnNhqRnE2EPSMrt1mL_of6oxJsjfETUpEWrEfGbuLLyEpw3A6oq2-ZwP87Zq1f7_HyvDjmkDcjtcHb3lg0nW1V-OEIaVHtf9yeaxRaiyzwGglVv6nqFyCz1zG0VigSZnNxmMxfjzqLTBesiYWPFjpcbovfom_4iAbOnSmQ70muf6ciW08OUIlwjnvSG1lSIBWEeUowu2QS7dy8FlfVk0SUVTE0DVKC_X5U9hVk3RTb2H-tpQsyRZUX2hW25-6pshCz8zMg6k1nnulzRkZaPT9PWO1L0-HRpS8B34wxA2YIoauKQ_oJ1qNnCkiZcgKAnwrZE02z6zog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
همانطور که ترامپ گفت، گاهی اوقات این آتش‌بس‌ها به این معنی است که شما کمی کمتر تیراندازی می‌کنید.
اما ما می‌خواستیم مطمئن شویم که هماهنگی مناسبی برقرار کرده‌ایم تا اگر تیراندازی شد، اگر حزب‌الله به اسرائیل شلیک کرد، یا اگر اسرائیل پاسخ داد، ما واقعاً با یکدیگر صحبت کنیم و بفهمیم چگونه تیراندازی را متوقف کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66678" target="_blank">📅 14:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66677">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d38c244991.mp4?token=L3Jsv3QobIfQwIoDtZR3dC7JZsBe_CL39wr4cZxt0_0iiXzgg6Nc0v9L4jBR4lyUZDfFirN1jb29zlwty10oDO2ZuEuqARrHO0unrf7OwYMsvHDMwzrQVigjoxFQ0PPU4U2D-aUpjDsP-cNzFlRC9_87VBGmy5q2XMFnNy544a5vGqX3bvPa_BJ88RRMvypOV70jBncb8iAawTFPk9w8qlOSLwhGYvlWZi06nC8j-SxdqGBHQGdEwqWUArivxvZ2g2EAqfuzuRJ0LTdvsxFQR6RN4gQaQToLNJdfvd4KrLDk0y7NyGGYl_H_zV46EOwTIIeNeFuNDghkBHX5kS0itg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d38c244991.mp4?token=L3Jsv3QobIfQwIoDtZR3dC7JZsBe_CL39wr4cZxt0_0iiXzgg6Nc0v9L4jBR4lyUZDfFirN1jb29zlwty10oDO2ZuEuqARrHO0unrf7OwYMsvHDMwzrQVigjoxFQ0PPU4U2D-aUpjDsP-cNzFlRC9_87VBGmy5q2XMFnNy544a5vGqX3bvPa_BJ88RRMvypOV70jBncb8iAawTFPk9w8qlOSLwhGYvlWZi06nC8j-SxdqGBHQGdEwqWUArivxvZ2g2EAqfuzuRJ0LTdvsxFQR6RN4gQaQToLNJdfvd4KrLDk0y7NyGGYl_H_zV46EOwTIIeNeFuNDghkBHX5kS0itg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی ونس:
ما می‌خواستیم سازوکاری برای باز نگه داشتن تنگه هرمز ایجاد کنیم.
ما می‌خواستیم مطمئن شویم که سازوکاری ایجاد کرده‌ایم تا مطمئن شویم وقتی درگیری‌هایی ناگزیر پیش می‌آید، می‌توانیم از آنها عبور کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66677" target="_blank">📅 14:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66676">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=JG6Qapbl6gcQt5bXPV61BJo-nxSFQLhlwpViBp7CCnP4mfnZ2n7deq0wDHDRwa6SPCYyhBeQqrWia-sqAD6WhyF_ukPC6-dJzZxprpCmxAnOeUW3t0FiktYAdmuk-mFylR98hJEL0IAQTUyxrcRv_E9RJ3Hka53sng6UKteyigE9i8e9BZ_Owfd6fF4d0hEqsIwceQEktynbfiOZg17AxUcTdrXSYviRZRJ61m4k-cgDsrVJamdivWQi3MkrPDk2zzPyREGqCiPuEX6eFj6JurVNEb9JvpU4aGCztXUPYakQQkJZ0JQTNkNr83wgioeRR42jqYaIQweeVGau6PSI9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=JG6Qapbl6gcQt5bXPV61BJo-nxSFQLhlwpViBp7CCnP4mfnZ2n7deq0wDHDRwa6SPCYyhBeQqrWia-sqAD6WhyF_ukPC6-dJzZxprpCmxAnOeUW3t0FiktYAdmuk-mFylR98hJEL0IAQTUyxrcRv_E9RJ3Hka53sng6UKteyigE9i8e9BZ_Owfd6fF4d0hEqsIwceQEktynbfiOZg17AxUcTdrXSYviRZRJ61m4k-cgDsrVJamdivWQi3MkrPDk2zzPyREGqCiPuEX6eFj6JurVNEb9JvpU4aGCztXUPYakQQkJZ0JQTNkNr83wgioeRR42jqYaIQweeVGau6PSI9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی دی ونس معاون ترامپ:
در زندگی خود دو فرد بسیار مهم دارم؛ همسرم و عاصم منیر.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66676" target="_blank">📅 14:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66675">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=JhMIkGJ6vgQdxJCvww_j5cFG5ogjBl1dJ-cwfVPaI0hw__x7D99zCcNwJrMG0as5HCwNKLbjpyUlWFFYYAiZrmlF6zotG1oZmcaCnAVSZfpphAIFvh0KD1TWTAuSz2F9ZrYZZHXuspiF2BJaInCr4zXw9m4KWFLiVIBkzIOGzGr5sWEQ2zoPcNuzisMRwgAftA3c6LMvjrt7nnuUq1KRsDMyHLIRjlJ1l2ZAkklywqaYKtUGQOqvw_BU9Eu3HcSRBUToZ2aETgMZMcYdySBwiasKCuJPZwzxGA1QZLLlYGJWrFtRHfG6Iz2OH1SulwlzLkcVr4JJFKc1dEc9BSXXEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=JhMIkGJ6vgQdxJCvww_j5cFG5ogjBl1dJ-cwfVPaI0hw__x7D99zCcNwJrMG0as5HCwNKLbjpyUlWFFYYAiZrmlF6zotG1oZmcaCnAVSZfpphAIFvh0KD1TWTAuSz2F9ZrYZZHXuspiF2BJaInCr4zXw9m4KWFLiVIBkzIOGzGr5sWEQ2zoPcNuzisMRwgAftA3c6LMvjrt7nnuUq1KRsDMyHLIRjlJ1l2ZAkklywqaYKtUGQOqvw_BU9Eu3HcSRBUToZ2aETgMZMcYdySBwiasKCuJPZwzxGA1QZLLlYGJWrFtRHfG6Iz2OH1SulwlzLkcVr4JJFKc1dEc9BSXXEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دومین کشتی کانتینری پس از پایان محاصره به بندر شهید رجایی در استان هرمزگان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66675" target="_blank">📅 14:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66674">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66674" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66674" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66673">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66673" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66672">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=rzouV2nuu33xw4T5QDM0HymAvnuaieuhtXRn7l0y9nZp9TFAy3P44YqwwTOTiWpOkLyopwVqUdwcq8TVPIgM8iYshLG6E89Nl_I1XJlk6EAuc9ZKTOY6b0mQP3vVxfbO2kK0TBUbngNuyDAm2tqXfw5jNENX3EXkZ2FhdNN9jq3m2KheQNEjzf1gRJBs5em-Ne8J0x1Cx9fhMd1ST8YCZsp9Uxi-SwmWQu3VjsO1v-JGcQPAUakBht0pFOrCJEexk0CG_U9X1m-jx-usLoJG7CnECYS76CjpSwWc02vrAECxZIgDlqhB1H5GXkx94z1C-59lJOpR02uNsweuhsXRyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=rzouV2nuu33xw4T5QDM0HymAvnuaieuhtXRn7l0y9nZp9TFAy3P44YqwwTOTiWpOkLyopwVqUdwcq8TVPIgM8iYshLG6E89Nl_I1XJlk6EAuc9ZKTOY6b0mQP3vVxfbO2kK0TBUbngNuyDAm2tqXfw5jNENX3EXkZ2FhdNN9jq3m2KheQNEjzf1gRJBs5em-Ne8J0x1Cx9fhMd1ST8YCZsp9Uxi-SwmWQu3VjsO1v-JGcQPAUakBht0pFOrCJEexk0CG_U9X1m-jx-usLoJG7CnECYS76CjpSwWc02vrAECxZIgDlqhB1H5GXkx94z1C-59lJOpR02uNsweuhsXRyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پهبادهای اوکراینی بر فراز مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66672" target="_blank">📅 13:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66671">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efTloYkHhmkwPlhKSRwcIBvexhCSZ54HmQVYNM2J1WQ3VNSc2em2vt8gBQ9lXPx6lCFZrGDbIWXH8NMnGVle0cE925IITrQYzx7KGE0j4As-dNDsR_bfWa6Ywuaki7qU1_QOyHMij444xGLNjahKYkZFRyd8P86lMt9hW-GTzPCoU9tV7oHOXlU-JeeLnO7ZpIishmomXw3QWdL5ZB3iEaNnfsp-S4uqOM0Lc2_CeovWFKZIwLflPp4CpWKZR0ui73oleIwUE3S2edR0Toj2eRiRrsPpTqcKH10-bX8PpH5GG7mX3anRnIzH6HeTQeBjGfCCz1ti9ifF6-GMY52pqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل بقایی:
هیأت نمایندگی جمهوری اسلامی ایران بعد از انجام گفتگوهای فشرده درباره اجرای مفاد یادداشت تفاهم خاتمه جنگ مورخ ۲۸ خرداد ۱۴۰۵، عازم میهن است.
این گفتگوها با تمرکز بر بندهای ۱، ۵، ۱۰ و ۱۱ متن یادداشت تفاهم، از صبح یکشنبه ۳۱ خرداد در سوئیس (Lake Luzern) شروع شد و تا ساعات اولیه بامداد دوشنبه ۱ تیر ادامه یافت. بر اساس بیانیه مشترک کشورهای میانجی (قطر و پاکستان) که با مشورت ایران و آمریکا تنظیم شد، ساز و کارهای اجرایی برای نظارت بر اجرای مفاد یادداشت تفاهم پیش‌بینی شد و مقرر گردید گفتگوها در سطوح کارشناسی و فنی برای پیشبرد اجرای موثر تفاهم خاتمه جنگ تحمیلی ادامه یابد.
با توجه به اینکه طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی، منوط به شروع و تداوم اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است، توافق‌های صورت گرفته در این نشست (به‌ویژه بند ۱ در رابطه با خاتمه جنگ و عملیات نظامی رژیم صهیونیستی در لبنان از طریق ایجاد یک سازوکار کنترل منازعه با مشارکت طرفین و جمهوری لبنان، و نیز بندهای ۱۰ در رابطه با صادرات نفت و محصولات پتروشیمی ایران و ۱۱ موضوع آزادسازی دارائی‌های مسدودشده ایران) تسهیل‌کننده روند اجرای تعهدات متقابل خواهد بود.
مبنای کار، «تعهد در مقابل تعهد» است و جمهوری اسلامی ایران ضمن رصد اجرای تعهدات طرف مقابل، از همه اهرم‌های خود برای اطمینان از اجرای آن تعهدات بهره خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66671" target="_blank">📅 13:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66670">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe1a1177a.mp4?token=XeaX1CSlAlnnEwsmI9_9qQLefKOL_eXN4AngYSPvJlNPmsq9bw7jucf6fwQ4GxSqAF5xIUoJMxLRhcXU6JXAVmGlZ7piiuX35x1pWfdcTMYKiEPeJ8ooCYeI8EUQISnOoBYPaEg8SmQEUZ3lCEkh2N9Pboa994tjcxqFpUMhMi3dnPXiF5508In2xJozKoUkzGlgYoIdkct0ZVfSjn7so5lByZ3BNbym3N88ytqdnRkDhlYZRZHndHFeIi0vyjT64WCiNTL7jmQFlIAE9ZIh39iMGZkGm7_JRqJnT_CS6QDOSBi7DxeCiuIInFIZSN_3ruAGDc-JsuDn-4ED3_tWfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe1a1177a.mp4?token=XeaX1CSlAlnnEwsmI9_9qQLefKOL_eXN4AngYSPvJlNPmsq9bw7jucf6fwQ4GxSqAF5xIUoJMxLRhcXU6JXAVmGlZ7piiuX35x1pWfdcTMYKiEPeJ8ooCYeI8EUQISnOoBYPaEg8SmQEUZ3lCEkh2N9Pboa994tjcxqFpUMhMi3dnPXiF5508In2xJozKoUkzGlgYoIdkct0ZVfSjn7so5lByZ3BNbym3N88ytqdnRkDhlYZRZHndHFeIi0vyjT64WCiNTL7jmQFlIAE9ZIh39iMGZkGm7_JRqJnT_CS6QDOSBi7DxeCiuIInFIZSN_3ruAGDc-JsuDn-4ED3_tWfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
روز اول جنگ آمریکا از طریق یک کشور اروپایی به ایران گفت مثل ونزوئلا تسلیم بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66670" target="_blank">📅 12:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66669">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7d3de545.mp4?token=jVK8ESFmIan4ZKauVnZerx6yxgYwtlhSSrkvlpREbP6XrG8QQt7BQbF-5TJKYOurgmWk94ODUQZHsh0Q7uR1vY7XZy3Gs5mC1MsXtHWFr6KbzXTHAiNucAHjYcEIbpWqwlQLbSl2UmhaBWJ56abPthtGQPK4lpPDCYH5Hp3161nTx527t1qNrJt_2B2FnHIQpj8PJbYoTf6nDPP-F1EpThR-XtZi5eo9ttXskkkIJ-0cyokWeHIQPpSNf3J0HUVo_5XZMGgRUlLxSu5rpqL2AXl0SQtYDxxTR1Um10HgD7G7tmRjRi797Smu9pQ2w5ehMrAAA34dOLrH1B7PAgNP2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7d3de545.mp4?token=jVK8ESFmIan4ZKauVnZerx6yxgYwtlhSSrkvlpREbP6XrG8QQt7BQbF-5TJKYOurgmWk94ODUQZHsh0Q7uR1vY7XZy3Gs5mC1MsXtHWFr6KbzXTHAiNucAHjYcEIbpWqwlQLbSl2UmhaBWJ56abPthtGQPK4lpPDCYH5Hp3161nTx527t1qNrJt_2B2FnHIQpj8PJbYoTf6nDPP-F1EpThR-XtZi5eo9ttXskkkIJ-0cyokWeHIQPpSNf3J0HUVo_5XZMGgRUlLxSu5rpqL2AXl0SQtYDxxTR1Um10HgD7G7tmRjRi797Smu9pQ2w5ehMrAAA34dOLrH1B7PAgNP2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کاپیتان نفتکش وقتی میفهمه تنگه هرمز دوباره میخواد بسته شه:
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66669" target="_blank">📅 12:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66668">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14f482273e.mp4?token=PZ-k02LhyXT1f5LWfyAUbzh0q-hoPjwrBPSCcV0engs6dLezzPmQeBrYC8V4oga2Sl5tRCaZwRqjsOhLB6WuezB-pdvkwNdr8Bdj4gZTeQZ08ds0T54DUXIh9BFejE88HrSpp3UfawXVIAbCVQsUBOirnzIhEqGz26xvejktcd97tPTUI1nsJ2jfDOn7nIMHkEsbq2orCDR0LOTxRGZW1cNJ0t5KYaKLN8Yezqvh74MlqO-LtouKktpFkuEmwpx6GMZpUMK8JoZGLgyrvtX0swlDnT09STajslP1gp6OlFUU_vCRl-Qq6O_EkE8_pdRs_ZNErILhKWICHoU2DIElgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14f482273e.mp4?token=PZ-k02LhyXT1f5LWfyAUbzh0q-hoPjwrBPSCcV0engs6dLezzPmQeBrYC8V4oga2Sl5tRCaZwRqjsOhLB6WuezB-pdvkwNdr8Bdj4gZTeQZ08ds0T54DUXIh9BFejE88HrSpp3UfawXVIAbCVQsUBOirnzIhEqGz26xvejktcd97tPTUI1nsJ2jfDOn7nIMHkEsbq2orCDR0LOTxRGZW1cNJ0t5KYaKLN8Yezqvh74MlqO-LtouKktpFkuEmwpx6GMZpUMK8JoZGLgyrvtX0swlDnT09STajslP1gp6OlFUU_vCRl-Qq6O_EkE8_pdRs_ZNErILhKWICHoU2DIElgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
دلیل موفقیت رزمنده ها بخاطر پشتیبانی ما بود.
دولت بیست میلیون بشکه نفت رو داد به هوافضای سپاه تا بتونه خودشو تامین کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66668" target="_blank">📅 11:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66667">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCY7YEUnIEt1fIL_PpVJ7LeIKH5FwgEzTqPDWscTHvxDCIsRp2gsCzeJR7DnGQ4nGbdfdl5qEeQmCxCGltqL07CwDBfKoxKtp12ERLjIr0KNe_eIb048FN4kIIl67HOD_Aa8jc6IbS5ES1W0mgwOzD-Xu0At5iddcmO-8LU3fryTMtOOUV-sOL3YWIlztTMFFyXuLsuQAj5lJul6feCTEszjMcMobLJbHF37-Fg77mJgY1sLbn_UJbI2t7v5bdZeEqnPR24Ke5Lvyz51s9AmydInG0fLovgRf8YlnrGcPXLbwkX4wDmL_feyeM1KvNQC2RdjownBGjxmertCkFM-Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه؛‏بیانیه پاکستان و قطر:
نقشه راهی برای دستیابی به توافق نهایی ظرف 60 روز تدوین شده و یک خط ارتباطی برای تضمین عبور امن کشتی های تجاری از تنگه هرمز ایجاد خواهد شد. یک مرکز هماهنگی برای جلوگیری از درگیری در لبنان و تضمین توقف عملیات نظامی تشکیل می شود. همچنین مذاکرات فنی آمریکا و ایران در طول هفته در سوئیس ادامه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66667" target="_blank">📅 11:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66666">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372418cb00.mp4?token=Fo6_C0jmZVAZrtSG8YxPU9_IGtzlvmdN_qV1VbIj_cytXn-4IFbhe44IXhjuzRpP4EFc7iJBYb49fhu2PZ0P9eSfOmoMbPyfXExI7fVPrueuTo2FLVQr9jTH4-Yq2A98p1UKpLO7zfZ5ywPtpVLJopFZVqR4nFQFBmcIPXP-LmdNEIlrrh5Ls44V6fydNuK_USQrIyexXf8AqdKH93NFa6h_eq-g2Vnpc3L-TywnEgZgQ4qx4z1fDlv83bJS_NqRUFiqVl-2pD54LauDnfNDmEtQuihblkTKOVDcOw7Ef9wQMzoVvY1fg61wcNXIrtBcD8dO9_Z3onMNurBw7ZGlrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372418cb00.mp4?token=Fo6_C0jmZVAZrtSG8YxPU9_IGtzlvmdN_qV1VbIj_cytXn-4IFbhe44IXhjuzRpP4EFc7iJBYb49fhu2PZ0P9eSfOmoMbPyfXExI7fVPrueuTo2FLVQr9jTH4-Yq2A98p1UKpLO7zfZ5ywPtpVLJopFZVqR4nFQFBmcIPXP-LmdNEIlrrh5Ls44V6fydNuK_USQrIyexXf8AqdKH93NFa6h_eq-g2Vnpc3L-TywnEgZgQ4qx4z1fDlv83bJS_NqRUFiqVl-2pD54LauDnfNDmEtQuihblkTKOVDcOw7Ef9wQMzoVvY1fg61wcNXIrtBcD8dO9_Z3onMNurBw7ZGlrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اسماعیل بقایی:
با حضور میانجیگران، سازوکاری برای تضمین و نظارت بر تداوم آتش‌بس در لبنان و در تمام جبهه‌ها پیش‌بینی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66666" target="_blank">📅 10:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66665">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
‼️
مدیرعامل توانیر: ادعا نمی‌کنم که بتوانیم تابستان را بدون قطع برق بگذرانیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66665" target="_blank">📅 09:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66664">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuAO3cEkY6QoliXndaaHZRVJtkiUFd_wgxZKwqPNRnzINPM9YvnuwaJBAliuKxqrkc5-5DkUDWrIfF7Or9ylVJTTmE8qf8fS0ELLRhh2eLcQ0ZAwuyz2GAnZIcPyFKjk3S0roQcNYdoyFUEv3mS5RYRLLFcazuko6qrn41bpl-kiNogyFPoZbeZ7SFY7Pb1EcuWdhNtMsvS9J-T_anuEWdxN7kRgFjdPwQaUQ-9FuithzryziYZ7SPmWTPYxvHJd3vviBsyUy3o6IT-wKv3O7_-zQgCyvOOPDWZrC23deU6enpnA2FHPM7aWQmV_zi8wh63dzfG-mIle8OkF5vVqAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
عراقچی: تحریم صادرات نفت و پتروشیمی تعلیق شد محاصره دریایی برداشته شد، برخی از دارایی‌های مسدود شده آزاد شدند و طرح بزرگ بازسازی و توسعه اقتصادی ایران اجرایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66664" target="_blank">📅 09:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66663">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eN16V4cauNtluTtMgukOeXPXlBRLA0luvtVp-VZWBegh6ub4WBKhR4bTn4k51PM-17IOXiAkV0g4fTO6IN7TfmXPmN-soAjeFpGxBQcZOXAA4_1Pn1qpQoUhUwcWNw-y9qvq7UfKsir3I8rFiBER2KXxcb8ojgxVyqg43APUNMmgbvuILlB6FQ7Kvbm1aGSAjYqK47l0PBEvB3NMqULvvlvYqGjzwblF7UTM9mESr9Sq5kS2GTUq_5DYrV4HEMvhd8M-Qh_5mxHkPeJr2fmFSuy3F2U8j0T_NPQgRu7gMBLPuWg4HKWo21IbIqfd1gzU9bgh12lWq15OUyKELSKfjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
ایالات متحده بر اساس تفاهم با جمهوری اسلامی ایران، مسئول تجاوزات و اقدامات تنش‌زای رژیم صهیونیستی در لبنان است و باید پاسخگو باشد. در صورت تهدید علیه ایران، آمریکایی‌ها را پاسخگو می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66663" target="_blank">📅 09:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66662">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66662" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66661">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ny5KPH0WcHGXUoljTNRtPDLJmaiEoNK19uiu7JrlBq56uQTMiLJ9yuzqByzr96kSKYKwH7Xz-iS3qXUL8U0VdTemxf1-vXEEBkQmY-TLFIA9jjx-NO3TZXqNeTj4ERXRgJIYFi72hZLUh8GPSUsV39BMh1M2gwhZj4KTF-7g9EZLK4a_jMuzafVO1by9Gk0hHmY8VIv6Mw8fqeoHnbbTvggnV2XpDOmejjuVKgb_cPf1KAUpFBuyCMBaa0TPiW0FA-MNoPgO8n96RD8cH3YEIBnyuodjf5eJ39FNS_KOAPxp9B9xnZbXHPMcWOUqNaidFcUBfwV3K-OQ09Xb_mcO3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66661" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66660">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/denaIUXRkwjhmQcb83XdOsLt4hbn1RBpdPMu3kesvkTpprZhXa48UQO6ghUBLtKYMooIiEai0FOnzvQ8Rg3enXAcHL8qGlBXae3dn3iLobt2K7R216PCFSy39iUsoCy6WZc2g8SnB-eta5JArEkss9hpU72u9Y8zSQqbgNj89D2WxeDfByK8QomO2awly8-5j8fpXV2Lqf2GziK7u8UKk9bI5hqSclpgINKB8uPy_uU9N6Bd8W5oNjgd8oQ4NtUT-qGXrBPzilkYbA6KCIqemTPSwxZXnw8Q7TzMiA_OPVmYBwSTiwRUuc_jssSSp1OP-Z0OT29wMHpx3UPmCMhh2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
قالیباف:
ما به این شکل از سرزمینمون محافظت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66660" target="_blank">📅 01:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66659">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnOteNI8ZIM1RU1hpT35Mb0o3CBKdfU3TGLChW-v5AJ7SrKzbkD4_EZKAye0OC6ipI8ELFGdkF9cevAEqAR4sdVnU3I1sc0pYrxUz8eJvcXjE6lPAa_Eiuia812u5LGongZLtjdi2qRqokWBPUaMbSVp5Y4CG_bZBkIBkX5qytS_sJ6V3p2ORNGauTAqFWlyxsKf7CzSzPiSXuWQzTl9YIpvsBCj5tW6iBVMK-xYfyIF6WnV1dVQOW7hG9VVEC39YVrr9zoJ-s2GJQAuIvZrAi5wO-Q0TDNjUwLbGu81NuKQTQn5yECyZYjcZyQtcg0_X0jd1FAJeJM1Sfd0FmDpfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
تیتر نیویورک تایمز فاسد و شکست‌خورده: «بعد از تقریباً ۴ ماه جنگ چه چیزی تغییر کرده است؟ تحلیلگران می‌گویند چیز زیادی تغییر نکرده است.» واقعاً؟ ارتش آنها نابود شده، نیروی دریایی آنها از بین رفته، نیروی هوایی آنها از بین رفته، سکوهای پرتاب، موشک‌ها، پهپادها و تولید آنها تقریباً از بین رفته، دو گروه از رهبران برتر آنها از بین رفته‌اند، تورم آنها ۲۵۰ درصد است، اقتصاد آنها ورشکسته است، سربازانشان حقوق نمی‌گیرند، تنگه هرمز باز است، نفت فوران می‌کند و بازار سهام و مشاغل ایالات متحده در بالاترین حد خود قرار دارد.
این چیزی است که تغییر کرده است، شما بزدلان فاسد و بی‌اخلاق، و موارد دیگر!!! رئیس جمهور دی‌جی‌تی
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66659" target="_blank">📅 01:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66658">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=dxDMgiHa99iQYfihMu-w2uyA95urvV65LxZnHCcZKj8v8RsixzY8Rtc1BTblA6PyiTdqRUZ6A4z5nI5_xAnFY7V7sJaxrLySUoU77DocI-jSz0VpjTzFINNmalMc7rce-UKMnnYr2RD13DGOZJM6O1kRfya3NOAn2VZ6Fke1feOgj153xzbeB-3vnJi1n6R2i2LsIm0xFQL-qtJpH-uHKERxlNNBxMEDd4S4HlBE_ui0Ogbj6mYw_z3wi1BRcAVHwCYSNj2qe9SvxWnq-sTW6-TJdQpwW8-qJz00SYZDlCuRSlUpkYU68iQHvMNrM2HnWST5AlCLwxqb6cwvI2JdRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=dxDMgiHa99iQYfihMu-w2uyA95urvV65LxZnHCcZKj8v8RsixzY8Rtc1BTblA6PyiTdqRUZ6A4z5nI5_xAnFY7V7sJaxrLySUoU77DocI-jSz0VpjTzFINNmalMc7rce-UKMnnYr2RD13DGOZJM6O1kRfya3NOAn2VZ6Fke1feOgj153xzbeB-3vnJi1n6R2i2LsIm0xFQL-qtJpH-uHKERxlNNBxMEDd4S4HlBE_ui0Ogbj6mYw_z3wi1BRcAVHwCYSNj2qe9SvxWnq-sTW6-TJdQpwW8-qJz00SYZDlCuRSlUpkYU68iQHvMNrM2HnWST5AlCLwxqb6cwvI2JdRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میساکی و رفقا بعد بازی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/66658" target="_blank">📅 00:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66657">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">قلعه نویی تیم ده نفره بلژیکو نتونست ببره
بازی صفر صفر تموم شد
👅
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/66657" target="_blank">📅 00:35 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
