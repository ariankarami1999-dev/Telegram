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
<img src="https://cdn5.telesco.pe/file/vB9xIVf5gQy9DFHWlrxQGSLgXICoMtY-_OIHsdOUuKFBkZi5FEvDYR_uAaOyk2-9oAknWfvh5H2js8m8Nh0g48IY078UpPx7wLJKm34v0ZFz5CEUxbeB33Vqfi7A0xso5oh0gjN3myLD4VCJsfaIc1BsTjkZWDC8d5TjcA71SeMjAjH_7u4Eeyu3-we2ZxMKA18GkrWrTfTKqZ36nGuScbyC1iZhseEu4zkB7j82Bkmp2jpwz0Nkiy9m1UOwi8A7WN_CyadCNp9a85ziJ37L8x4RacNhdY_2QLyoNTa-KyKbPtPOg5beXGs6DYxk8uWjLyG9OgLBL3ENtcD8JMlvqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 611K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 00:11:03</div>
<hr>

<div class="tg-post" id="msg-99110">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82d743a24e.mp4?token=HkW5eVrjs2-5RV7A6dDgp7V3CnyJdVyYTgmG3WjC9iuPsERckaEp7M6zsmteFZ8ncJ2kYp3ydcMglLPqluxtht5lrIs2OTkGnw9lo7kIZnVArYLix1lo7Z40eyvm4OfBccHNTCIAJsOBF8810N_s6IhJ8CcJbWLxoVquenAHz2YS_tbx-No1Hw0RnSqJLbk9AfTqjgf0FbpGQXP9yUiKY3X6PJRI0gNxtz035voGFIqiX2F8m4b4yJN23ETYDfaZUeKMaD86hJGzjto-wI1v41q0jbroJBxR4tSKwkVNUDOcLYBvqMtys121Fej31dey40djRuznUQQbFmbV5OXisA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82d743a24e.mp4?token=HkW5eVrjs2-5RV7A6dDgp7V3CnyJdVyYTgmG3WjC9iuPsERckaEp7M6zsmteFZ8ncJ2kYp3ydcMglLPqluxtht5lrIs2OTkGnw9lo7kIZnVArYLix1lo7Z40eyvm4OfBccHNTCIAJsOBF8810N_s6IhJ8CcJbWLxoVquenAHz2YS_tbx-No1Hw0RnSqJLbk9AfTqjgf0FbpGQXP9yUiKY3X6PJRI0gNxtz035voGFIqiX2F8m4b4yJN23ETYDfaZUeKMaD86hJGzjto-wI1v41q0jbroJBxR4tSKwkVNUDOcLYBvqMtys121Fej31dey40djRuznUQQbFmbV5OXisA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات متعدد به چابهار از این زاویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/99110" target="_blank">📅 00:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99109">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf4c74933.mp4?token=lYj3wpoiVWSRQ960q_MzNZwRVfHjIFcE83DmvUhpMt9ZC35DkWgy9pZbsLWIDs3Zd2Ik6nxfvA8ven-IbVBWoYg-xGyNYhfgfKtD6NeqnX_lVv7j5vYGXRsP1KiMfcw98szjh6GEiKToki9K19sfQHD_kFcPAWEUsLgqAlzSxfWnvNCXiV7Yq2PT-5QJ8soLoUB8WJ2alU7_UMtn0hrbIvXJ2RGk9uqdaqrOuH8KGuy4DtIbhV0HX-nh7ORWl8heG37jdSUsvPUcCvCD2y-UvWcgyrW8Y8snamUKh89SLQn00QmjZYYUF4HLnvfal7Pwv-IE0vX6hY3xLbefGl1KXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf4c74933.mp4?token=lYj3wpoiVWSRQ960q_MzNZwRVfHjIFcE83DmvUhpMt9ZC35DkWgy9pZbsLWIDs3Zd2Ik6nxfvA8ven-IbVBWoYg-xGyNYhfgfKtD6NeqnX_lVv7j5vYGXRsP1KiMfcw98szjh6GEiKToki9K19sfQHD_kFcPAWEUsLgqAlzSxfWnvNCXiV7Yq2PT-5QJ8soLoUB8WJ2alU7_UMtn0hrbIvXJ2RGk9uqdaqrOuH8KGuy4DtIbhV0HX-nh7ORWl8heG37jdSUsvPUcCvCD2y-UvWcgyrW8Y8snamUKh89SLQn00QmjZYYUF4HLnvfal7Pwv-IE0vX6hY3xLbefGl1KXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نیروگاه اتمی بوشهر هدف قرار گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/Futball180TV/99109" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99108">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
ایرنا: در پی حملات امشب برق بعضی مناطق چابهار قطع شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/Futball180TV/99108" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99107">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
ایرنا: در پی حملات امشب برق بعضی مناطق چابهار قطع شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/Futball180TV/99107" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99106">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
بیانیه سنتکام؛ فرماندهی مرکزی ایالات متحده:
‼️
به دستور فرمانده کل نیروهای مسلح، نیروهای فرماندهی مرکزی ایالات متحده، حملات بیشتری را علیه ایران آغاز کرده‌اند تا توانایی این کشور در تهدید آزادی کشتیرانی در تنگه هرمز را بیشتر تضعیف کنند. ایالات متحده، ایران را مسئول اقدامات تجاوزکارانه اخیر و غیرموجه علیه کشتی‌های تجاری و خدمه غیرنظامی که به صورت آزادانه در یک آبراه بین‌المللی حیاتی تردد می‌کنند، می‌داند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/Futball180TV/99106" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99105">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=D125W6mqIjcTZRYOikj3yewe58ZwJUk-3zSOyetLMS-jJ60Nt6QgTI1kRjT0RVyQYg58-QO1MRMvD2A0yJawSHMPmfRrzPGA-Ax1JT98V3G_u2jpSgoFZKDgUAICZZWDOlGyaFsV3Em3UhItgApQ0X-zbCRoxXh20CN0W3FfDo1n6MoLec1-JPcMDbBeV0yqKQvmXSQJFUI6EjtYrDWSKuipl5BFsGMZ6rXTvOnj2G1DhxR7hnqOgr5xw2xVj2beoVBA4v1vmcB12lEWYu10PkyN_YmxqBqkAC-ic212tlETzNraogoftnebaRyK-ZEMbLytI5kdrbb63C9QrOkPrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=D125W6mqIjcTZRYOikj3yewe58ZwJUk-3zSOyetLMS-jJ60Nt6QgTI1kRjT0RVyQYg58-QO1MRMvD2A0yJawSHMPmfRrzPGA-Ax1JT98V3G_u2jpSgoFZKDgUAICZZWDOlGyaFsV3Em3UhItgApQ0X-zbCRoxXh20CN0W3FfDo1n6MoLec1-JPcMDbBeV0yqKQvmXSQJFUI6EjtYrDWSKuipl5BFsGMZ6rXTvOnj2G1DhxR7hnqOgr5xw2xVj2beoVBA4v1vmcB12lEWYu10PkyN_YmxqBqkAC-ic212tlETzNraogoftnebaRyK-ZEMbLytI5kdrbb63C9QrOkPrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات سنگین آمریکا به پایگاه سپاه در چابهار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/99105" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99104">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
موج جدید حملات آمریکا به جنوب کشور آغاز شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/99104" target="_blank">📅 23:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99103">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
موج جدید حملات آمریکا به جنوب کشور آغاز شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/99103" target="_blank">📅 23:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99102">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDECduwyPSRbiyHgXax1KOCgGcewFclDFZicav5gGx6O_MXOXl0qH5YmFAMrIqaAQGXPy9SLWegTRYAib5jfOEh9HeFVC-O508VHaXgNnRlzXDUW8MRaRaaOZiRskig-3U8YBUbl8Jvu0LzP9Hwu2fgkIrHVWJ9cQfDxifPG9Jr6u4OiRIvGBoo-RqJ3lzi4ZbDRIyyAL74M4HZOrRGhfHjCVFWxSnucFUd35rZ3oDPF37Vj1ftKKHfPL_ORz1UeOLiMgzHYDOCRYidYgG2fLEu9RNNMYgiMiUoE7AxOdoy1gJmBec-EZpZuHBdVDV5RqXAfeh7wlPTXYUTr27kyIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنژ پوستکوغلو:
چه سال اول، چه دوم یا سوم باشد، تمریناتم را تا قهرمانی ادامه خواهم داد.
میخواهم امسال با باشگاه النصر بهترین باشم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/99102" target="_blank">📅 23:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99101">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2cb709e88.mp4?token=KqUr6sd0nra3TlWZW7-e_ubVcskT72ezblPdslFF4hOwqe0-KArDbiPfw8AUz2lcf-zGnUQSXlyrQRcxPRxBx7wCnepMzF2TcuNjGFoflxlMz55gQ-0BrpmF3JvS7xJOuKlNbCVaWw4PWqn3qg3efVf1bXvB4aDA3AhpEQc7qqcr0EmcbCQdVoSCcAH1EyTFogguV6Jd0qmmdj7C61AWKBu1QzcpXv7Xir2fzjIQEtEFeg89NWgSDidHoRsoakWpUwUMX5Fx6Z_gSNuwbCsKzSqkdmYBQMLDEN9fhSLWysPXfnqjYF0XPknrh6ob8qyJE8fTIc9a5JTNx4q4OloHKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2cb709e88.mp4?token=KqUr6sd0nra3TlWZW7-e_ubVcskT72ezblPdslFF4hOwqe0-KArDbiPfw8AUz2lcf-zGnUQSXlyrQRcxPRxBx7wCnepMzF2TcuNjGFoflxlMz55gQ-0BrpmF3JvS7xJOuKlNbCVaWw4PWqn3qg3efVf1bXvB4aDA3AhpEQc7qqcr0EmcbCQdVoSCcAH1EyTFogguV6Jd0qmmdj7C61AWKBu1QzcpXv7Xir2fzjIQEtEFeg89NWgSDidHoRsoakWpUwUMX5Fx6Z_gSNuwbCsKzSqkdmYBQMLDEN9fhSLWysPXfnqjYF0XPknrh6ob8qyJE8fTIc9a5JTNx4q4OloHKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چی شده که برنده توپ طلا اینقدر با ما احساس راحتی میکنه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/99101" target="_blank">📅 23:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99100">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKPIrhh3XtC_YfiB4kTtDhu_LwULQ1aykss99xdRn8ebwhiTPqJJocAfVnG04VErn1OeZmQOCl1ymH032viqKwrxE9D9w3ySFkf2RW9QnKZxoK4E3LwJ5tm41mA4PQQCErkekzuElAGNikqp0pVmzjGg2jSR2LUBuJxRy78REsmmY0jd0cwTG47WGJPQfio7y3zLd_m1STbbOYSMNl70b7l7DEX05ey9BPOaXp3oReDIWBLGJLBB37dcWLGfgZdXIbsNuIyszu6QkqUPfaJ0qqVTTNWgeIF6ISq47tTv1V_VxZnzXK6lxZ2-nXHo77ScEB6gP4b7y350jpD-iyodsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاستین بیبر بین دو نیمه فینال جام جهانی قراره اجرا داشته باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/99100" target="_blank">📅 23:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99099">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1GiaLakCp4M5PRRpCj1SreRKOeUHgnHId3U3uEnBLcCywIGXajsTN8jLIbuqqVEVBuMPFENiEa28noqebqI-RAdDUSuiDyzrTi_DsF93T2HmjBPCylrNwf-6ctB0BolRg2GLlTB3BBbkaStx5jhNgN_Odbbno0jid3nPd9SLEAvh2LpmMhnF3NnLjbiCUecxzgkYwMIQkUVTdDka-cau3tsVH5-RF_CoCeOZnj8rJBpmiOI5yUwRw6GTTAyM3rasu0lmDCffBbIRuP2gH9T-0e7o6SvzFYxruPFpjSwJUD2kYiU6R-B5YI96wcLN-_opc41v4kzkJkpq4MBSd2RaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رافا مارکز به عنوان سرمربی مکزیک به جای خاویر آگیره انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/99099" target="_blank">📅 22:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99098">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FB5LLQfcwxA7IsRgp7t4XrXDIhW_aM24XmrnxnoN0ZKOCVxvDkL-8jHA36YN5KY6vSZQrAgni8G3DofRwLhxpOdHgB_JcsSPnjjibtip9Kblsap1Ni2oGdNYIVxiKNx8q5T5uJO41vUiHeo011KcMXTvX_1CFs80DQoW025PdXFy7intfAMR-0vJwiakWM-B7J_jaKIMkvSA7Icj5iD8KnT_LTgMgqQQVDGb6QXyLdUDNXkiLTZ4srfqTOXbTRAD9Nb5s-lfj7kM__xnV_nYaBfTayoEQVNYNqsLgH9C1qFPhtBhr5f2j1MTAfBxxKjSm7Nd-ELid5OkLfXBNEwVGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلسته آماریا بار دیگر به کیلیان امباپه حمله کرد :
"این حروم‌زاده فرانسوی نیست."
سلام و احوالپرسی یک رسم همیشگیه؛ صبح بخیر، عصر بخیر... این یه سنت پاراگوئه‌یه. چیزی که ما رو عصبانی کرد این بود که وقتی اورلاندو گیل این پسر جوون، با نهایت احترام و فروتنی دستش رو برای دست دادن به سمت امباپه دراز کرد این حروم‌زاده نه‌تنها دستش رو رد کرد، بلکه سرش داد هم کشید.
این رفتار، رفتار یک فرانسوی نیست؛ یک فرانسوی واقعی هیچ‌وقت همچین کاری نمی‌کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/99098" target="_blank">📅 22:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99097">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRQ9XhlyrHttUhgsh8F1QGn1f8dWNvRd_3j3gcrLoAMd6g1XAdumowe2rgkgJiIJMuCBWv_8ryFu_DQQ6WhU-RNELmyGhsBFPwIFbgcQlkTVxXeRf7U_f_jI8x2RfrEj1ZwPLbhOF6rAieM3wIXVoLAs1X4y7e-WOOi1yZKS2KBLeSXn6sCvqK3qrCEGHNSt-8UIVeiimlY4D9AXFmZY9uYquXqaRqZw0rQKUUKuCrYGxLDpKD6W1YWC0s0LLiiRsSZjORiAlhzt0RKdRj4BGrJ4VDkejGnuaTou_wGzexz-gJGOghsN3fCuqLmbkK26VZKqaoS5uqFc8UFQWVMbsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در چنین روزی در سال 1990، آلمان با بردن آرژانتین برای سومین بار در تاریخ خودش، قهرمان جام جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/99097" target="_blank">📅 22:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99096">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqsAg-aDxcZhox9wU0nPBkoL9ATnQ3rIJEISBV7k7AQiatuaKaaymHICXDFzbkzvVLHKUnAsQa8X4SO4CQ5wsOMCK9hfUA7arn_-grgkIRfdxRKNNr9ilCoApaqMvHVIFKh6JMZMRywe7jcg2Ohh5JjNDcuQVtPgmuQTcEcJI6ZTqhEVfcDXLRLEB1fMNFQ9EqKAaprajdJColDGt0N12XFs_AtlOhhOEAfwRCSh1GGdCnihDpcI9VFn13fvsTFtKPKdLe8I_p1zRCGQS4tGpkMxoIA5c9lTbrkcbzSAbK_tnDIEO56mY8dnM1EgnU9fB13dw2C2SalF1RpHbaZKKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
شانس بردن ۱۱ جایزه ۴۵میلیون تومانی داری
فکر می‌کنی از بقیه سریع‌تری؟
😉
⚽️
وارد این چالش شو و
کارت فوتبالی اختصاصی
خودتو بساز
⏳
فقط ۴۵ ثانیه
وقت داری؛ سریع جواب بده، امتیاز بگیر
و ببین
سرعتت شبیه کدوم فوتبالیت و ماشینه
👇
👈
شروع بازی
👉</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/99096" target="_blank">📅 22:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99095">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3rOQ15k849MsC7Rrj-c_eX4ozKcR_TYKGw8u3H-_bCzl20PA5X60i38qNkAXXlf3-rH1Pv4Rg_H2vpPb084ZptCu8x1vyJjTH78qH3oSPzH-nyhB675du040dRAfwych6hyEZrTfxnHm_UBf3qfnuTv65o53bAuxzogceID7ZkMrI37Io2_iM3sLgV7GhYDXsZol1GXh10bfukqFr0hJojkQ5CRGgjnQ2gvWctPbeUBbgp5lS0nPh66CaytB7-EbM-dzCUmWqWgx2tBxtwS7TCp7gdm6_uVNNyXYb5QNrVCJQVLC1IVHzZqVeQ4-tiHjZWcpKhWoKd8wvJH5xJpsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
فران گارسیا رسما به رئال بتیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/99095" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99094">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4kgKaYFq0mDNR-_q-xdNJuntZ47_VHBPTcxh_KcZF8WR2Rk6vGOiq7SNW2FEcg-3AJ8ibqobiFL5AXamsGhJJxLjfthkkCnZw9LqgF--NCz8ws-mw28sPFtP-4IhpNkHDVwc-Yq8A1GjXwEpuFCf4LXMfEGp9TlbiPsrvZSglDapFCD8UHMSASYIeXDl5WHq5toGa8JTWt85xbkqyMuQAcs-rcYHXhA0nmuibZ9rIN3De5_rpK-lhgmg7pbkKVcWxIpDzDKbuhEBWmgHb1tKKDx19ItHxDSmC_73n2CQNPiCFLX8bKiFvnFDlb71yGJo8dg3HGbrns65qasjuSOOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هوادار یونایتد رو که یادتون نرفته؟ هنوزم بعد 634 روز منتظره تا من‌یونایتد، 5 تا برد متوالی بدست بیاره تا کله رو بتراشه
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/99094" target="_blank">📅 22:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99093">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agn6zVoV1_K3TXynnn9mVbTU7M6ETb1g5j9-FBje7akCt-2M_a9auposWKPVu8yvF4tU2VHxeUOE7Cq-po7t2JZbtZw5ZSdSipZKp2ksiy0PrVCir0b5R8xNC1AakDxbgp0jFWr4N8ekHHL-kEk9Dvtikw1-WW3tDEkSYgZv0IXsQNexI0hwwBTJo-KnRodw7RWrhWjBBMUqvYyJZ2AY2unax5dYqnrqohjKYZwWMD2Xr_2JGz82qMX1Nak2XHGyzFGA8lu2ogOpi-vbqtZaAcWwrldN7cg2oiDyXW1SuZseW2D7lLsxnldM7MFvYdnqJ--3ZBjoWinyNbH4_-6DrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ژرژ ژسوس رسما سرمربی تیم پرتغال شد.
🔻
ژرژ ژسوس رهبری پروژه لیگ ملت‌ها، یورو ۲۰۲۸ و جام جهانی بعدی را بر عهده خواهد داشت. او این فصل به همراه کریستیانو رونالدو در النصر قهرمان لیگ برتر عربستان شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/99093" target="_blank">📅 21:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99088">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rgyeMb-GH7nC0D5l9EYe-i_aahAODZSpmvqJv-4bbGK3DqI8WmGzlJxdRYwspyfh3tHNo9JXuAZtyPk0JTem9kM0VKKsk_oa43yYY3XfQrOO5A7JYXcOEH5pYnbDj78iP-RAJ2Kq-XawggEJ70sV5R6AF7SxWK_6stw68IqYMZn1WRF8Ve7WUrxgDm5lelnhSK9Z46lVXsS8WWr2ZaJWc5d92MADD3Wzxn5KahkgWvqMI_VDM0c1DHhwIxgJ3IxFeaJLl_shDqdHpCA_wWNp17nSHjilVFn8ewtBU6ukN1ASB4gfkX1NugW0NXfBWmYvX2K5WFyVUtx4s9_2CDAsTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ADergnm_adM_OzIZfrZoi2pKg7QjU62YETQCCauEQ6qiRqgAj5WThsmC4gY-KZf4NyfSQm9jrVcITCAZE7RDGGgnK8SHIx2JhhWFFQpNcAajgIv-ri2Q2VG4kAfI0E6oe_CJR1WoJ4gq2XlJlBWa_c_6rdQHFI-WLd3R2hiFB4D2K3yPkk5TMbKhp5FKpcg-E6aOZJTHCdYSPm9BuJFtPJcIivZhC5kyo0nfQAqSsUtBiphJdemwrmaS0BzS1_scRbeCJ20jO1ZHLnmteJqsFHAuqi0qDf8QKQMQUAPJ0BO10AeBhMz-J6lmq-ZiMpHye1hPnLF8Rkkf40HD4J4LHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQl6dP-vFtaOilYNFYzGCZQ2yOqo4dAMvdpZYcxF4krzBJcNwMZK15o2VHDxQ-53POgvrj5bcD1z-No40BGMPrDGid5rOeAqMtBa953hPdk7p3XLPC7RQdA9UxYNgteEb4LPlhTsDjyutB6BF2FomWSoPSZ8IUQBlcB5KeAsJiqkRtXxynM9c4nZrf9mZaRfKjpC3epNfylpqfG3zHn-5fC03Xu56J_QRfyFyeeoClI9k7yh0DCz8vsPEjXKVSm4ScfZZMSNkvTQGFqDKbgOTg0FxFJYYxt33ubtqiNXT3I7furhnHD1spr2khDzJvYSTcN1znPq3RIL7qPdPjdrWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XCpAGsisYFiNnHms5YLg7jyKLAGCD3wCDsvMwPy1RSi74-6wuoooP3tiXJg-wPhgtXSj8htyvWKAxUIPbywRJeEsHSNnrstC_EmGdd7jXrvza582mBik9Khge2XlwabW3uzbno4sknJ1hOr4fZzKv0fFkoKPrtlMlsY17WGtCCIHixTHfdY2qeK9IhvlnPZzedE70IQ601SS8jBJ5CvNf49T3rCR8El8yD2VObK2YunzNTpooEwth-zXV3vtoFwjPYyEmpBD2vF7egXSU-mT45CSX2Y4lEhW6px3k2oHGxJtOs3-1fZusuAT3o4pAjyMcyOla55zYImhy5vhrPN4MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lCBddQWbFMqJvkSxfHr1HAGWFZDoZUAjZpR3wyt6XqPvo0E7l_RB0b_lAmMbQYJu5H43SWMs--KL1xzaSTzxmrnJDP7QLc5AEH8OrYldNLe-OV9G19TO32XlSfb2ZGop4pOyBlKXhxblaFwE0G74SgKfQXTWIAn4FNFJMaBuaCgzagD1cC3REQn2QrygoYApp80zFrknPQt6Bi-_LYSkKpNQRgsIi6pwy0tEIGq_RJ9EGRTXug464oPvpJFSC01a4KG_C-sWEFXzHDzgZ_KvwE1XV2ZIoQ_i1EhjX3jcQ2nKzBYHfZR6p3HeNj4jdVEd-H5LtbjaHvlbZEgteTrazQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
والپیپر آوردم براتون :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/99088" target="_blank">📅 21:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99087">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lheicuy1zYWEF1GCKfT5QAyatNfybMLL5NeTULmuTX6wffqp9gseFelxozeWr85fknPTpVzEi2163t8OxTY5WkduCckTVMf9JbrVJq8rO4GC8npcgnqqlfL3xk4on73_riKQzPbOMejXFjlhuGtI2DRVxutHsp_DqPPhTHyjqyeQNSjz0nXBjS2T_VpHUbN6OY3nstUJK4iLyXGdVMM9p4Kbftaf2gBtkAkwsClqJmfHn1RQpjrmoRIqprAI-vwoCiMzPEbI9nmdxFZr7vs-NT6SsnmRrVMpiXUmqRQT-sjbB8HZ5acUGQQ1gxZvcLo7jKoWqY8kJCXul3pd3vdyPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوووووری
؛ رسانه‌ UOL برزیل: نیمار احتمال بسیار زیاد بزودی از فوتبال خداحافظی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/99087" target="_blank">📅 21:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99086">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A44VUQHi7OlCEPxKKcqhj9gQy1TUhmcFBbGYcu6XhS_zz4CgH7KPpZeg3Z0DZa6HewPnXjEKb03OuiUMlnIhfjPa2YE3t9zX402MUDpNokZqFYyp8Nqt9qrtXgn0SBYz7j8AiSrJ2oqgWF-fiamu4mZhl5U_sciPnXoCIi-CB3NmTOi2UvJIYvQAY_HjVSDjZgg-9f2_L1VQPMKXrZE5_XeooIj-NrHBEsqEvLFm0yX-JbCFt7bz99CcKGUH6eN-XlX4wh8md-mZcYLRNYATigau4Lv4NwR2JAoO45BAArTjXXJTqiknRGBXJ1ANwxM_RjWEAh2gc9nQgzh8fbEHhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
آرژانتین میتونه بدون بازی با حتی یک تیم از ۱۰ تیم برتر رنکینگ فیفا به نیمه‌نهایی جام جهانی برسه
‼️
🔺
علاوه بر اون اگه آرژانتین سوئیس رو شکست بده و نروژ هم انگلیس رو شکست بده، آرژانتین میتونه با شکست دادن نروژ در نیمه‌نهایی بدون اینکه با ۱۰ تیم برتر رنکینگ فیفا بازی کنه به فینال جام جهانی برسه.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/99086" target="_blank">📅 20:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99085">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNN011yqaAbB1uxn7heIUf6P6llDPxvdDY9B2RrevoCCHlQYR3bRJNcbZoQadfvFDu9AwgD9kRdtly8r0tj8erBONS14617977oug76qmne-gZznN42ltfXxFljbfke9wdktc40DoR_1K2NKWOIUaJ7IIedzWhRWVavBx79dCZnCT2b_1V4EZelSh2POkXI6S9of6In3b1fkj23Cp25sKPOJVBVsgvHTOoTMrO_tCm2s4xEYgEzYq8bMpfrBfQjcKLR2ZSNjI-S968aqaPYez2axFlsd0W8SPdO5qOnMh7d57BVs2WtQz9X-u1_Ded-00_3H8MnsGN7EgdsyELZZjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
#فوووووری
؛ فنرباغچه ترکیه با مارسی به توافق نهایی برای جذب گرینوود رسید تا این بازیکن را از تیم اتلتیکومادرید هایجک کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/99085" target="_blank">📅 20:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99084">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YetI3D6ltOMSp5en7PnZPlqYjaaYU0F2P_yRX6R2VRx8lZJzLhqwEYAx97lkW7AkbGDi7YPZM9dNEMosC-kOx4MXM-olYmi1N6dLafIw_RG2B75zaijlbkMnvErmGiOqvn6SKC8ydM82RMuIKFxA-fc5YRvdii-CCIxfzt6H54jPRlahM9DXGyVhO2uHtiIQJjCoaiY-kTSPkBVwS0yN7Ul_ZLH1SxE5eQElBqJysx7uP6SZ8ssaTHimWYrK4WlypUk5KGQX6hAUB7hd7cil4DqCiTHYO-NfWOMRxbJznf7FLzCM_Ey5dXT1y7Byug9ZZ8QiUkJzFXHRWPo1Aa4qYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌بینی خودت را ثبت کن!
🇲🇦
مراکش
🆚
🇫🇷
فرانسه
🎁
۵۰۰ دلار جایزه
بین تمام کاربرانی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، مطابق قوانین سایت تقسیم خواهد شد.
⏳
فرصت شرکت فقط تا قبل از شروع مسابقه.
👇
انتخاب شما کدام است؟
🇲🇦
مراکش یا
🇫🇷
فرانسه؟
🤖
برای ثبت پیش‌بینی روی لینک زیر کلیک کنید:
https://t.me/betegram_bot?start=p4_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/99084" target="_blank">📅 20:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99083">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLy7DmPfgIobCR3b8RCSUbSYj7e800GVQo6n9batmDdAyIchOmhcQokTXb3wyGoebguyscwB1dleNjwqJ_492_Xxtgs0YdtVjVo8Tk6hCleZfqC-t9jwxsvbCVqbnfbdOte43TE8k_i33KRb_NmZrV1GaWYaBNiq6pDm6Kze5hBCWeQn2mXzi5D06amVB7LbmtHn6OfL4z5Vh9d-vVOXNpRDnV4NhCdJI1Ibe2p5XLRS_9AC-aV1yb0WMq2w_HSp2Zvh3silmUziGM1nqEr5CtzcRhrfjTuuzbIAZBxqmJ88vVlpgQk-9QGibJXKr9YZ_KJZJh5GYt_OqLEm3MF7cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁳󠁣󠁴󠁿
#فوری
؛ روبرتو مارتینز سرمربی اخراجی پرتغال گزینه اصلی هدایت تیم‌ملی اسکاتلند است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/99083" target="_blank">📅 20:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99082">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQ5gSxa9FGFYGmstJnacsZRm7ejKvIGv7_h7b2rtzcN0e0p-CRGP39-lzVsXXDAjBWf8qnTsok-BEQngkbyKL37EDnqe-Gg6Qk9zPheGJcPLnl4KToLwH8IYf-Ni0K8ASGK0NlvtMfp5vYx1exE2e254rpQcW00vQXgMGnS3bTWt9SvHe_qZ3rMGbjTHlLYCY7vVjw-RFwPgkofJHJ-nWj5TBoEHrOV6h9SPEfeZZgqKlQIB3VwsxR6mxxJPSaA07Ur3zxPOx6M7Mm9xrjCf-FgzCzP8jSFOo_0ex1PjIPeuBp9LIHuMzohKxM6RTdUMj5AiCkn8h_-0r2OD50tCIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
الکساندر نوبل دروازه‌بان بایرن‌مونیخ با عقد قراردادی به بشیکتاش ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/99082" target="_blank">📅 20:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99081">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2GUYsNrljKu6DyYHGnEWhZz5Yp5A-Go-sFvqS82t7BdnLskHwnYQGmRB1-ZUPwFG-Z3dXMnu1CsgcUq04Viu0TLSZ128XH9bwbyf62Z3PkKbJ3Sk6igJ721q8uN7smY_rvv51p55F4SYfgiqPxRlIewKv7cNaXk9yv7-1KI_JxCcjQpk7mehAHfyI740o9tyJTCV11gSJLGnX2XtCgWot8F_ChrGkt78Rqfd9bELkvGAfCTqOzp3GJELUPY4XM_CMWMi7rdBQa4I0rbA29IgZ-QZPXGW6S7BX34IEtri3FItD7pYtxwRTb4Jeq4LtOx7f7-1EQ4l2RV3cNc363Lsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی به رودری اعلام کرده که ستون اصلی تیم در فصول آینده است و هیچ قصدی برای فروش ستاره خود ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/99081" target="_blank">📅 20:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99080">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری
؛ ادعای برخی رسانه‌های انگلیسی: رافائل لیائو برای پیوستن به تاتنهام به توافق نهایی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/99080" target="_blank">📅 20:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99079">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3Nv5JM-gvIAAyJ463wFQKr18jsNRmB5kFAhc1cbT3LWUw2mfyr-4kJVQBi_sW5AIr03XYCrLjaD8PJaRxe2rXXrvK20tw8NDthETxdr2FA8SqUqB6r9foXraxBly8mVaw2RybrHt1C-DpawhOKGL6x5qBCv02UzkWlpALBA7g05nxukQQrPI7vK20ugE2UDDyNwMxH5XcEJ2VFgees4vItxJJviFgwrSymQ0Xzpw8vdro-Xcm23zE22XH3-t5LQ2APmZ8VcWwpeoCn8j3nCsLN0wwEYb6XYb5p5Z7IEyqklRJmq346E0tf7Y3sCbVrIkLGiV_Oe1cd6r52kJD5bJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیوید اورنشتاین:
برونو گیمارش از تمایل خود برای انتقال به آرسنال به مدیران نیوکاسل گفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99079" target="_blank">📅 20:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99078">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c18362372c.mp4?token=Z_jgPbZf527IN13htYgdAYZKonDpo0XEYmTELhGJ4zI7b9CgKzKkSFU-OTN8PTnjwIAusYY_8uzniB2cn3ugqLHMa__MCR-NSq60LpRMdOMCuAskQ9Xar7gcThioBaxji42Ux1DdWuDxct-W2IXEzbjRwVpHccf6xktPxy8XXK21uYQhAA3AwRRpRVvgEIYK6KbDrMnco4AB4r1ylrWHw2jvyDDBVMgF7YrxEZwU91ozFFKRqQ-LzU52hgfUPtQkeBBYbz7B9bhMpfBlmQUFIgfahzf3__o3PZIlWxHpzBSyTfWsXqONy4ysxDtb_Eb3FPrr9pdl1OCOGlmeFlff0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c18362372c.mp4?token=Z_jgPbZf527IN13htYgdAYZKonDpo0XEYmTELhGJ4zI7b9CgKzKkSFU-OTN8PTnjwIAusYY_8uzniB2cn3ugqLHMa__MCR-NSq60LpRMdOMCuAskQ9Xar7gcThioBaxji42Ux1DdWuDxct-W2IXEzbjRwVpHccf6xktPxy8XXK21uYQhAA3AwRRpRVvgEIYK6KbDrMnco4AB4r1ylrWHw2jvyDDBVMgF7YrxEZwU91ozFFKRqQ-LzU52hgfUPtQkeBBYbz7B9bhMpfBlmQUFIgfahzf3__o3PZIlWxHpzBSyTfWsXqONy4ysxDtb_Eb3FPrr9pdl1OCOGlmeFlff0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
این چه سمی بود خدایا
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99078" target="_blank">📅 20:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99077">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3xUHghBTZT1ewV_lBtF1-kgRFjFPnVScPbD3gTw_5KiEs8XuP9pq1_pEAOpRyI6nRaEkBi0XTs2TwjEG4rHPIZTwws9ZVNCF5yFewGpESDGNB4mdXJK2R_PV_EZmN-NBvrXvTfzThgAytHLIittXV7ObbiYg9L9-HoN_p6RDeEXH-ITFQbz-A-XcKkRAeODvZtuISllskRXn0xabGBELQWrPzB3NqXxamjqbpjtKjdQz6smxNYLOB4K38RtjOeCVLPvrWkl_xbvihDAKDYsamAAXpOLVxaaLdDZZG3b65uMmEAr2kwsonYUGfbz0yRU_cMpzzPpkbJHUUWWa8K8CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
🗞
روزنامه رکورد پرتغال
: ژرژ ژسوس در تماس با CR7 اعلام کرده که مایل است به حضور این بازیکن در تیم‌ملی پرتغال ادامه دهد مگر اینکه خود این بازیکن تصمیم دیگری برای آینده‌اش بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/99077" target="_blank">📅 20:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99076">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQKpLJcDtSgiVuWMhT4odiIr_QSqSz5w6SiLtJtstA8qQlpNO2-22Scwows787r2aACA68CTgUd5dxxT5Fme5OlApGmaz0j3YuMUF9IBO_vtV2_hdc9H-5gk_ITD_O64kuZlAVQuZZbGiQd2gmlqerUC_tEZaGq-i_ejo5U9DuPdXwCSJAIR-6Fp7I0Uq1mOyfqZnw3VQDsOaTtU6DwrkoegxJNtz8i82UjOkOMuqhHIN7nLGoQ2BQ9WAlUaLgH4dT2ezBgNO6ewS928AlbnEFk0FG0IY79Bvect_JI3D9nRmdUptvzRqoh4ozmrZT2OtLFv4Nr7e-O1YjU_OhAu9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گلهای دقیقه اخری جام جهانی تا این لحظه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/99076" target="_blank">📅 19:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99075">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0dCDUOWMj4Fr4JKdB6no6Q1gIO-gbxVyXbJCXND_JST4FyxdTG-TvElWtgZHh-teMzaXzzo-RQZlLOoPDMSAbgL--TN0Cl0UNCTAIWnpSDfkostqAawI3apbyyQUx1nQq2iWTlNKBDa-LHtY1jBFXR9Nby5jD8fdeXdsjrGgNffrNO9S6w_JhjQ4okfc3FxkTMefYHTWpXDSloPulo3wMzaUi7FUlHVP6y2QwZYfvCRdDFiTInoS-5V5SmGMl63LkAjzo5cJMUXEk-4mJnfX6n7aSHk3glqbzGPxadHdZPL03FA81J_V2bvKLiWX7iZQgVc8n_lZLd4ifyFtq7e_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مارکا: موضع اتلتیکو مادرید هیچ تغییری نکرده.
❌
❗️
اتلتیکو قصد ندارد به جولیان آلوارز اجازه دهد به باشگاه رویایی‌اش منتقل شود. این موضوع چند هفته پیش به خود آلوارز اطلاع داده شده بود. اتلتیکو تاکید دارد که تغییر موضع در این پرونده غیرممکن است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/99075" target="_blank">📅 19:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99074">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/99074" target="_blank">📅 19:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99073">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bw88yalEF_-_GDVMYbDRPkkuSOREBWmWDfbSXAi9zcFGhl9XJxC5G3P9E_eLm29mMQ0fjYUndP_oh9Gso7RJ3AX7B6923QjFSMGU8twQwHZLW6_nXASTugC3QZhQDtHll5kRhQzahAWiyGcqipIuHu8iweGNTuu-4UpdpxjAeGe1tm0oXWufuqntfl0D7ru0gfjyRnpkUmIEnZNjhHvSiYyoLioQj0kCjhVIOsugQrod2KT4kPpAnH7dRAio3s6Z30zi5tsxkW6KY5OFMXr2G29o9oN-epK1NvAQxfoPaoF4Um2LCDAUtr3OK5j88FfHDsOQq9piTNjTqBtkcMbUwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/99073" target="_blank">📅 19:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99072">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745dbc9962.mp4?token=ZoYfM2Z7204AQ1LHe8Idgbp3BQP9jpJqmqD3ItBVmAdYEr3CvmEKuddO2QsKzdi3rap1Ydmd5tnBrlbJXwgUpxF5YM49GKD2oM5TkLIUaX9wZoAFZ98JDBwvbCZzTi-TCAgrzxBdQcAa-HFSouSD8oqQTBETiJed6MLs4VqFwLoCWtdBZg2g9MPrRLIcr8Ox9uihP8snW5CY4HYZGezOgbVXpLVOdEwL83IqtRf_TWa-wAPgfQoFetzjT16S24IQJHpxPFH0Uxia1i17vmHxin9dwPSxlGWeTspw0qiYtz5uZnU-oBg9JNDXM1j0I1FiJ2817giOK7ylq2D18k9YHmTtJ0sGh1OSrrfWN6OiuoGcf5B4bU4GlhYjP6LNWpUP-buwBwECeytu7bz0I9eXkQlwXGO8ENHR5UtsVxRYE8E-taqjK7zpOkPetF5azzPoyrdFxByS9ymW_WBE08u3kJh_uzLMxAlE-FTWHILfVP-KXGi5WqS7GiuPKuGFKDo_GfNM7kfvbUxZGywYMS1QZYowfnt37IE5klYatqPnyJWG3Iz8LB7SYTkA1Th9pkLMZo67jTW9j22njv3_pUfKpk0xRL9dT7tlw9GVhmzKfDLGWjBiastisgYBWHVr0YE8Bj4D_TSFCvCahL-XY8TshWSyOFStwnOv6a27VJoduIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745dbc9962.mp4?token=ZoYfM2Z7204AQ1LHe8Idgbp3BQP9jpJqmqD3ItBVmAdYEr3CvmEKuddO2QsKzdi3rap1Ydmd5tnBrlbJXwgUpxF5YM49GKD2oM5TkLIUaX9wZoAFZ98JDBwvbCZzTi-TCAgrzxBdQcAa-HFSouSD8oqQTBETiJed6MLs4VqFwLoCWtdBZg2g9MPrRLIcr8Ox9uihP8snW5CY4HYZGezOgbVXpLVOdEwL83IqtRf_TWa-wAPgfQoFetzjT16S24IQJHpxPFH0Uxia1i17vmHxin9dwPSxlGWeTspw0qiYtz5uZnU-oBg9JNDXM1j0I1FiJ2817giOK7ylq2D18k9YHmTtJ0sGh1OSrrfWN6OiuoGcf5B4bU4GlhYjP6LNWpUP-buwBwECeytu7bz0I9eXkQlwXGO8ENHR5UtsVxRYE8E-taqjK7zpOkPetF5azzPoyrdFxByS9ymW_WBE08u3kJh_uzLMxAlE-FTWHILfVP-KXGi5WqS7GiuPKuGFKDo_GfNM7kfvbUxZGywYMS1QZYowfnt37IE5klYatqPnyJWG3Iz8LB7SYTkA1Th9pkLMZo67jTW9j22njv3_pUfKpk0xRL9dT7tlw9GVhmzKfDLGWjBiastisgYBWHVr0YE8Bj4D_TSFCvCahL-XY8TshWSyOFStwnOv6a27VJoduIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
تاریخچه تعداد یازده بازیکن در فوتبال از کجا شکل گرفته؟ ویدیو جالبیه ببینید حتما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/99072" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99071">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‼️
نکته کنکوری: اگه بازیکنای یک‌کارته در یکچهارم کارت دومشون رو بگیرن از بازی در نیمه‌نهایی محروم میشن. اگر کارت دوم رو نگیرن، تمام کارتها بعد از این مرحله پاک میشن و تیم‌ها تر و تمیز میرسن نیمه‌نهایی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/99071" target="_blank">📅 19:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99070">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHx8SJETcrC15oc1KPJNgAVYvrY6tPUHz7EQEwgM6eh6W3sZpTTufggoIHABEB8nRe0WYrKNYo7yw4CZHnleT5oAKqxB_v03atcK35UORhLIYhOORonbl2NI8izrE4F9fTscGyADBaEjpfHBGYBqsQbXdYceSr040UtnrlKC4bFD_gZ1bKB28ZltAaU8VrdXzSyXFPwqukgY2lunL_zubXWiw7ZxhhrQb18HDkpwCf1PuMPeyxkLse60QSNPYhtSw9x4aScI-zFGZKOeDXt0m2IExzVsK3sQP_Y_iDNUXrwWvc0-bMKtKx3oDpu_WCR4zORTR5gwrrze4qJ60EQ8sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نکته کنکوری: اگه بازیکنای یک‌کارته در یکچهارم کارت دومشون رو بگیرن از بازی در نیمه‌نهایی محروم میشن. اگر کارت دوم رو نگیرن، تمام کارتها بعد از این مرحله پاک میشن و تیم‌ها تر و تمیز میرسن نیمه‌نهایی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/99070" target="_blank">📅 19:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99066">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m1t54yXQlJsYKXvbxOY3zejj-4heSBAud4jHqQoCD48k4La2JhxqHKAcc_6qAJIIeDgn8_H-u8pY-A9lJMXqgqzuKXAJjSpdlINpNCK2Xv3WNbnndBSvdjttgIBUGeH0LSpnR_6rzekZLpxY9_G6FXqFC3hxb5Oc1NU6yWi6IMcK13WxyeFWkPJM-udAoHc2098CbmOE7GUUbsb5q48sDkOdhsKG8raR-p7d6TwymlaC0w7DD2hpOPUG5qhxOA3aa0gepkoXBvMCy11hEHuZR3T202DEZ7ggkwutc1kNdXO8o85mhB8uDaTi7Pmeutzfbh1oZwCwlJaVf568gCNi_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vBKSqkLR0Z3jmbmZCotlR5Id3jv9KSFPZOUqlY9w6BxTfpHSSN6FUA5VTeRhX5w5a8x2rRq3EXT-39WAM9PIJ9zTC8pWF40PgrxG03-b18BFP5KN6Xs5Gi6vqv8ipnSvkPrzBeVV5Syt5OcvnghV6IYBYLXvd2ALNmOJ4i8XDZh30BAZwTJkV2-aH0lPYjfam13Ytjc0IyaGrMinyqdk0syCTBVYGkQ_j-I0kyv_Om37wxCCOcrADDFvfzp8oTb1gASrW3-P_0o0bHjNfwXeEVjNKuglJg3GEg_8bpsXLc-LQhnrjgmtw3gDpdB5-Uv0MTd-c1v5vLvOKBetAq3yAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H_U59ClL_JF4gl2wlWRqbnEQB8gRI1hHP0rAdDvY6vf_38ASIjjsvz_hiHIN6VT_XgjyCsho-4CkUeR7cCPKPeCwzTxPYimOsQ42J9-m12tujaEF6CrXntGCa6UnmpEyekGfANMshh6B8wbOA0BFyC4gAgoJzpZPA_KBRf_iQja3uIKi-d3OJ772DzAMvjPvFh2G1G7K4IOly0fcd_SCCk7g9jm7rdB5Z_BcpCza0w6zuw04mwRdMtjMt63I7u_TwUTVTYuZW1hKbMfaIu3UqITHYezWbQJ2VfFwsxkMZdSkG-wuATXyeHSJXK0eH6m29vK0coDIH8hQWxPyqk8eOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Up3Sg2QqLxOfhsUlkBfTVYtcQRjTv-wl-Z2WC7DxUCC2SVzZX-SH9Db0vIKW90RPOGZmhejZVZG0-rTcO5dVXz60Ll1oFfS1nvUCc-iFoQW2M_CFlOPPUZB7BLgtPxIwo50w6kCfZspB3H4A8CguFbIPRQtUx12HT3WBKO1oJFJGO2THhAvduFjjhoFPqZorCO11ap5Y6L1_KxRW-gNlRf2E_IYJ8chHs7SYjgYdva254zmKKpxsROqRrmmbcxE4B6ioaRWtyo6LRkw2ZEsekxm9vKZl1DLdRvtZ6VpYsRboOer1ztZ4FIhwFaMpo3P852WboXBSrgHNqNKHIQqU5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🇧🇪
همسر جذاب کوین‌دیبروینه در آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/99066" target="_blank">📅 19:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99063">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cKXPRBaqA_fOzD3jprmY1DiovgDfKN6VgkyIXuiVwZgyW4ZTBqy3OladjnoEVrHx8YelYbcNdEtodi2ruFhXhN3FyJtngShgE_7rfZA-CYsqHhMMLJlBZ24I9Ra4U0qrEhJDdWcKlgvsyPoEEamKtQkLyEdxxmv7LhNIm36TswE6szqT6eDkakfQVQfXEGWgfx-msB4e_01Wq0FIwQ8Bg60vCxArcM8AnKS9qDygrQXrKHbhPahzIUNduN_VKK2gYFNsNbiKhzLnlxSxKH9KmLbZQdKLwl8j9zM6l6Al8o4MMO3n_cKAQJtIy8Ff2VDutVpZWJjTlHa9645t7A8eWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ezzimqn9jrQLftTAO9tbMfCV4JZP5XkT7nusQdfu0Mierb_VLEgp8V3UdkaweyolkYHL51Gjk0RosTcIFkS5VL6DjbjMCG4u4butfnW1K7Uu19dO7R9fKKS_CJQoAlAmFdzis9qK80xw6UkIOXGKUsSD65gyCCuuaEXC9wD3m7I0b850x-s1NM6ciI4gwLymx2Soeuh7QtcS_YLddYlK8-5Rsm0R-7t96ZRk8f2A8hRmeUqjPS65rcx85W5VXnxbfC9U1sQcElfv50bTf3AkqfGg5P9x42cUQvAq6BehvelT0Di4X3CHpYtMHxN7HDsIjLRluOTBZh-Qbi5g312cBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UdpZL93TO6Fd4zKzBBwQDGj0X8TPbrZUYa4iowEHCJv8-gmOv0YpBEgyIGPXRhYEg5n0OlHwcvdcAT-Eny4Pp8Yi4gM_YQMAi1VOUl3hQD4ZQHbWPE-AdrsO2hUEJyQ5lMK2E8idWGSgipZZHdg6b_bTKmiUKJlkA1Zsh1jccwQvzTvjhOmkRR5CLVKI9V5F1-KWDgaFHGNNw1uGasPl6UmexFxMcEP3hfs6coqWLwydj4YXpSLVWfxOVA-1wJGZf4v6bmZOscn5MZt4lR2EHVWfZlXoYyzkUXtrkoTDVT-LaClbNjOu7wzEgxMo1QsdxmJ1yIEwEphhTvitCkrnAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسپانیا قهرمان جام‌جهانی بشه چه چیزاییو قراره تجربه کنیم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/99063" target="_blank">📅 19:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99062">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fafdc23a54.mp4?token=bKgheiteTyw-pBOEFFc593oYEM_xShOaeAhFQooCTDVF8QKq14Mia44Q2cUJ_Xas-4lTA53J9hTX6CyXeibXT0IVJr_wEHsiKAcdb0eHLExMZIKD3atIrqilndO-l_VnWmNOcaYDsUxfvuL-lygQZI672FkF5T__sZ6So50SG86JLhSnoQtUx4MCH4H_Tuk7GiZIr-yr-WT-_sVchfsf7ThhR-7gbY6BtcXlaCnad0zTE_I0ERefTEcO8ddFBTnqVsyjrMjTRNOjsQbqLX10cz69WWmOzhwd5uLWgQbToMU-um9X17MpwtXpjuXdqenwnpEl7985ogSF3y2pEbeKgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fafdc23a54.mp4?token=bKgheiteTyw-pBOEFFc593oYEM_xShOaeAhFQooCTDVF8QKq14Mia44Q2cUJ_Xas-4lTA53J9hTX6CyXeibXT0IVJr_wEHsiKAcdb0eHLExMZIKD3atIrqilndO-l_VnWmNOcaYDsUxfvuL-lygQZI672FkF5T__sZ6So50SG86JLhSnoQtUx4MCH4H_Tuk7GiZIr-yr-WT-_sVchfsf7ThhR-7gbY6BtcXlaCnad0zTE_I0ERefTEcO8ddFBTnqVsyjrMjTRNOjsQbqLX10cz69WWmOzhwd5uLWgQbToMU-um9X17MpwtXpjuXdqenwnpEl7985ogSF3y2pEbeKgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
صحبت‌های جالب علیرضا فغانی درباره چگونگی آشنایی و ازدواج با همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/99062" target="_blank">📅 19:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99057">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22194ef951.mp4?token=TcfMqLI7bNAPLqBHw2w2lF2Q6ELodOoMQtR9DSmWJtoxpfSeIvCAvv8tpHWEy0NKmdX0oHK23A7URq-gz-IrQVpqGSIPgMZJPmxKMdIsjmt5NbHmklYAtfnlgISmG-J-2PT3pBvPOnoG5tJmdGRDis0v5K9WjNAR_kWV9OzX7vpl3asIKfia_OTvIgS74ETY_4_yUfAwwJOhWyU9UNXLbc9tkKw5JhXaMyS3IPmHMzClowYbk9RJx27OwMcGtrFcwfTzC9-z3fwSPgiK44eKRNA2hLE5-iCYhpV0zQOeHendeQOfNh1McC2yU7lm9IxbGwpdhuIysg0Vhny9tIcISKtcgtVVl9LIMu1x6W9hQbxbaPIB-zYb1ScnptbSe__Fg2CAeo1pM9QNqYlSnA4ZFk4jll4Jo0dlPUrt-45GvwpcAB08FnFO7Eqcmp_iuuCu4Nz6npbyS5HIhwUklUY749-Cbw_ycV0VHPrvpP-hzTedliboPazpW-uf5XhiBEKHBwMOwVeUdoTjiAe-pQukaQfUFnmjJ__m5JBlt6mwh3GJ7ERAb9bUB4j2np46rT6Xn-pZLz-SIQ-IiGUGGXfnnOIypaJUuuQH6EArvMsSmx15hhRHhsHfhBXCvrP2TAbNIMkse8_qNWmI-olTGtCopZ53wMPI7IJA_2AjhGZ3g-M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22194ef951.mp4?token=TcfMqLI7bNAPLqBHw2w2lF2Q6ELodOoMQtR9DSmWJtoxpfSeIvCAvv8tpHWEy0NKmdX0oHK23A7URq-gz-IrQVpqGSIPgMZJPmxKMdIsjmt5NbHmklYAtfnlgISmG-J-2PT3pBvPOnoG5tJmdGRDis0v5K9WjNAR_kWV9OzX7vpl3asIKfia_OTvIgS74ETY_4_yUfAwwJOhWyU9UNXLbc9tkKw5JhXaMyS3IPmHMzClowYbk9RJx27OwMcGtrFcwfTzC9-z3fwSPgiK44eKRNA2hLE5-iCYhpV0zQOeHendeQOfNh1McC2yU7lm9IxbGwpdhuIysg0Vhny9tIcISKtcgtVVl9LIMu1x6W9hQbxbaPIB-zYb1ScnptbSe__Fg2CAeo1pM9QNqYlSnA4ZFk4jll4Jo0dlPUrt-45GvwpcAB08FnFO7Eqcmp_iuuCu4Nz6npbyS5HIhwUklUY749-Cbw_ycV0VHPrvpP-hzTedliboPazpW-uf5XhiBEKHBwMOwVeUdoTjiAe-pQukaQfUFnmjJ__m5JBlt6mwh3GJ7ERAb9bUB4j2np46rT6Xn-pZLz-SIQ-IiGUGGXfnnOIypaJUuuQH6EArvMsSmx15hhRHhsHfhBXCvrP2TAbNIMkse8_qNWmI-olTGtCopZ53wMPI7IJA_2AjhGZ3g-M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فشاری‌شدن بازیکنان مصر از تکنیک لائوتارو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99057" target="_blank">📅 18:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99056">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aIj93traFWym-PNFKeYBnBmyjzwCnO9_PBpG2kHNr3rmsfOoCXI87luGkbrrrVWmiPehM_Rd-bQMFSAC0uhNP1bPOaR5oKcU0wXlzj78W29g282P4yICZtFopq4qkYjQkKN20uj9Z-ZkYUzXhJ9zlFPEN-ZGf_3ZYS-oSXE0gUg28-_X9JJANr5VUyhND4OlSVuXak4F80aYdCNHf9dvrsER0N0WQDZvvPbkL0hywJl_m22r2hr5iGsYgSqBnRe0p3PH4Dp9YrLhk_gZriZ5VofSMJ1O4FW9wz6BA9csloWOV8d9s7uAd0utkqNenIw7gDnN8FfYVzFnr3laW5nFcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JskIMPxKJlwLxl0ThNqfhDQUbWKMllk_6DpvFvwfuuRL7O7RPcByAoXv7n3ftDVxkM7eClW7Lh4r8EGZQ8g0MQQM-bi7SujWaPGNnyuRAWqnkRSSv6OgrTRAovLovLVKVnp3GjocWDmTwf4SJl67QQU97OCEC3S47uYzqZGShoHABfCJ_IM2aIsomGOAecIR0qTjwbo1Eik3E6GopbIVoKHpB0iPYN-Vw_JmK8VNZWTXTP3fIWrxLgrVGC99WcvRgwq2BwlTXB3FvZ37zcl0-1Jl5eshMLyyzeYLKyh8tVWN1UQ74Ja8Nc-Dic8NLb-PYFMHC4e6fF5DqUq9E8P8FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eK_PKFqszNZbzPwEIGqJXl3WpY6T5inxrwhh7UmpJqcZb_LznUAquvIxxh9FXJXj-7zNUFFiFvgyhh6IvpLWoUzeQm-FFEJMxrXFK71Hppu1UgwARgMpAVDQuMXyn56_YojiBlLGRaaIEi-ZjltNr0M9mvQ1XJXSHIelaYcbjRx2INA_DSi_WRTNi0Ny4Ot-klubBCxfp7aQa--w8sUWcZB09KPSUeEFRs2ZllCX_hxMptRv3cyzYcJXwBiPZ8iiH3lNk9T9Du1RI7TIgVCJBtjtjFSaN9FAFxyaC3IzfPTmStaI6suPYpff53xPHRHcakMWGgSBUviDO32WmwkM8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZ8IrO8pj43MjB7KijTSF8efL59JxymnEPFhh5e9fhvlMWE58JyVMSyDyRTf7-4EtKhTlrk3Pmmtrhqwy2c_8AsmSQFgTbhH-Oj3QGYL-SdYDNBYU6DKlbmcSFWWFZe6His2yvi2-N4IihfEMDZdWrBkpIh9JPvTHMxP_5s7lYuJNbuCYPwEZHOlebu4Uy6v_mfZS3QHJi7WBBKrTKSGrQdt_RE4c4habtlyh4GlYyYOeQW5y9S2oEHSOYBzQyS4f5yR_U4T-zMcJDZ41tNaTB_XPUoxXYtU4sozlK1t2Ltkwq9TJQc6ZKAXJxbKdCIu6PHSNZZYKw1FJbcQwZcnyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NM6wnfRHOyfXalZAdjf1LwOovRnjaG9WSXR1bn1LjD_aj71qqPvkHtRfVdk4huxq6Q8fZz-bmqpz1X9HeBg02zDlX-D2koLk9tDxpwndnF7kM6SdM8ojmvRmA-zir8ennva7rBXbaCMnxqipiYbQo700MBWCw40V55alNDK1SS5QyEiof8tYEMHbS-xrvCStZpzTDZqznruBxxI7DW2tJKNfR5kA0Kq-PjVPc_0rFN1GDKeDL_pe3HMLYNgA_Mze7eudxNe2-bTzWMKuZ_F6INPdRzFKYRlqoaYnBGcS2nNapFYUoC9vDIr_mG5tydsmfW1XofOLhhLQ_IC-rbhyaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇪🇸
همسر باردار فابیان‌رویز ستاره اسپانیا در محل برگزاری بازی با پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/99056" target="_blank">📅 18:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99055">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nr8I9WQaJxZ9uXKRBLF7GCfNyMEqOHNXDPr171MOWLrJBgAL024zGGXkrmCuQvaQVqabvRHliJuU9gag1mhvz3TjkYbot-Vxefpjqf7o4UFSaF9He7vm9HWEiW4jNQRQItv6ctXY6WthiNJgHZShjhXBFyE0imF4kNdY2QjFhJAEAp2e5PIhDNhFWjuSVl5kzsU7PS--amlKyesnwj7wMtwnrDfeKlgO-IEu4TgSOuR3wlLSzLMPyxkPlI_pA8pr_HDylDwy8OzLQ8A47vh46TBvNfF99wYSBHq9ZzUlqX1JoilMBy7Kr1rVg_ANZQ3x8xdoOor2rxyuMRUjcR0XHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری از رامون آلواز:
اورلین شوامنی با اطمینان 100 درصدی در فصل آینده در رئال مادرید باقی خواهد ماند و از این تیم جدا نخواهد شد. او به منچستریونایتد نخواهد پیوست، این موضوع به پایان رسیده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/99055" target="_blank">📅 18:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99054">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ouj1JQlRnfmS7QU_X04oUwJy_i9D844gQ6upZgNyCb-tLTWNyky0fCAxsxxnAUZozEDIc9Aw9uKNlt56JAfWxpiBNVROcUuO0Hk603Nz10DCx-pF4Qr7dujb7c6j-FnGivaEi0qq6oo8LfR9UdCqKQeGbcvwr1PpyyRnW2XPgCYvQ7cGUTRBp1gdZzkGK187vPWoLXSMXXByZtzzRrIjKyD2VvGmii-8LPMCdiPGQb5nd0YpzmJpBCDDeNEz-MhmgVFIsVMrPWhuKUzGUr9MMVDijL7-MjKrs-3NGYP3mJlKC7yrXkre9bmH_LKej7AvGg25Xc0TKbrvJUau1ZRR7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
🎙️
دشان در مورد انتخاب داور آرژانتینی بازی فرداشب با مراکش
:
"انتخاباتی وجود دارد و ما باید با آن کنار بیاییم. من به داوران اعتماد دارم. امیدوارم داور ما به اندازه آقای لیتکسر در بازی آرژانتین و مصر، کارآمد باشد. رقیب ما مراکش است، نه داور."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/99054" target="_blank">📅 18:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99053">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Id1YWAS6igb3Xz7utdX4YGgTT1Ebe9vyzRy9TPt9VC9HiNUT7qMsrC7BjSwx9rarqn2TvAiEk6Undfwq1e0gtFGHDQjzvfeuOLGo_3lussnZX5LAI2mBVP0har8lj2_8QclAazxMpYpnJYzH-fkK72MuhxDTncVY0v-HpRmIZM9kynhJoNHIhDflxsqeJQ1uGf2ylecUhUNCGphaPcLq8523PBiKv_jd8hYK8gh9a-jdx3J3TUl6_iMdbU-jeoAvEAWwOJQ3cXP9L5K6Ru6RBYqCK-fAz9tRt2rmtJH8H8ABccTdoAcfkgB-2_hbieJdJn81gsCEox5AYx_7rpssAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
عملکرد لیونل‌مسی در ۹ بازی اخیر جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99053" target="_blank">📅 18:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99052">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rax1PD36Qtgpnt0x6pBpoJXU8WlouMkM85GD-FsINSDE_nubmxE5B5ctlH1IJpH7eVQVpwbS75FygRr9BhdyuEHE_BQ6jIymO9FAvQTIG1bqj6RmBspocHDLrx2y2GXNzpxiFagtQSKvcKspkswMVBnJizQYV1-pg77B9zVzMFnh_B7Z6H8aYqMkwPHrx8W6dRDpTOMacWbfnfZ3nrvfyOBhfA8nwIiNFI9r0D08tqLQmLgMECMVYJai0IQfwuuVTQ4Siv4Pw8fxg7DWGx-vi1RRzc8VuBKPLhMy5sjpvDKkE7VakFPtxy2o5v1-mayNXI1K6nSNn8nQX0VdwfIqkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇬
ابراهیم حسن مربی تیم‌ملی مصر: هدف فیفا برنده شدن توپ‌طلا توسط لیونل‌مسی است درحالی که همگان می‌دانند لیگ‌آمریکا را نهایتا ۳ نفر تماشا کنند و اصلا سطح فنی خوبی ندارد!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99052" target="_blank">📅 17:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99051">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e25d8855.mp4?token=Xc5rO3UzRcvNlLqpHzqrrGSwsgVw3CrM8Q5GUX-8S4_2zYKvbT9RvzJfOYONMsmEMDr0-bFQxLybud_u4y5KBfLRWn6nyfn-0ahoLMgAzf5HnVRGl7drvhU5Knj-Igmq9vNnUh_YqPcbV53pqcLRfkn6-yJE-3GYKOCveXg0Q_w4YqFgh8IiE_JQWGxNKcAw6axyLAYKzH0GrQuOLZaTvbWJKBeBS2bFdklTm7F3O2U9J_Y_MD5bvhXn5ovrTWA6T9TcE7Q-sJ-UySwZaZ4LmxJtkRBtCNTkpgoHH65fvviBjRVT23TRAdu2SWs17AbMZkRA1Io3Gb-V7yedVzM3VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e25d8855.mp4?token=Xc5rO3UzRcvNlLqpHzqrrGSwsgVw3CrM8Q5GUX-8S4_2zYKvbT9RvzJfOYONMsmEMDr0-bFQxLybud_u4y5KBfLRWn6nyfn-0ahoLMgAzf5HnVRGl7drvhU5Knj-Igmq9vNnUh_YqPcbV53pqcLRfkn6-yJE-3GYKOCveXg0Q_w4YqFgh8IiE_JQWGxNKcAw6axyLAYKzH0GrQuOLZaTvbWJKBeBS2bFdklTm7F3O2U9J_Y_MD5bvhXn5ovrTWA6T9TcE7Q-sJ-UySwZaZ4LmxJtkRBtCNTkpgoHH65fvviBjRVT23TRAdu2SWs17AbMZkRA1Io3Gb-V7yedVzM3VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🇦🇷
صدای وحشتناک شادی مردم در خیابونای شهر بوئنوس‌آیرس آرژانتین بعد گلزنی لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99051" target="_blank">📅 17:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99050">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44599c3a8a.mp4?token=VmOMU_nuKxUeASuwz_rvz7yZHr_g3O2dQSuraEjxVwirOvbaL5uIeZPVy1cqX182tbo-QJf7VsnpHlv1CJKHEyv2mYMOr8Y6mEBWWFGDSbo7GOD0pE6C1EGlNxgCmDrZfue8pMkzSv2eTQRJqWbZKRGoMHLahRyaRQOUhc1iiRhovnsDwkPuC91SsYQR-ejHmGSIAeubuMQ350nGNMXjAC2Dl7yTJAFuQdVnwN2mpLKyEjZb3on4ZqWmu54dIg89EK2vooNdQxjHcX2rswiKL-c6SzYpQZa41-Gl4AaOCeS9EE6fSYToobLOzLvzy-7WpmjDTfwKHh3NhreH1XwmBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44599c3a8a.mp4?token=VmOMU_nuKxUeASuwz_rvz7yZHr_g3O2dQSuraEjxVwirOvbaL5uIeZPVy1cqX182tbo-QJf7VsnpHlv1CJKHEyv2mYMOr8Y6mEBWWFGDSbo7GOD0pE6C1EGlNxgCmDrZfue8pMkzSv2eTQRJqWbZKRGoMHLahRyaRQOUhc1iiRhovnsDwkPuC91SsYQR-ejHmGSIAeubuMQ350nGNMXjAC2Dl7yTJAFuQdVnwN2mpLKyEjZb3on4ZqWmu54dIg89EK2vooNdQxjHcX2rswiKL-c6SzYpQZa41-Gl4AaOCeS9EE6fSYToobLOzLvzy-7WpmjDTfwKHh3NhreH1XwmBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
آغوش گرم‌ لائوتارو و همسرش بعد بازی دیروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/99050" target="_blank">📅 17:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99049">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری
؛ ترامپ: پیت‌ هگست از ایده ترور مقامات ایرانی در مراسم تشییع علی خامنه‌ای استقبال کرد. ممکن است دستور یک حمله تمام عیار به ایران صادر شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/99049" target="_blank">📅 17:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99048">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5b20b4ab0.mp4?token=IVkp4r8qVpd8RkrQWw8ojKzZs1KFRhaWf1hCDzqMdfdBuIiG3_4-U7TjRQVnbqjUFf_SR99aijm0B2BmtFCwmn12K8fYzSokraAMsxZXN-Vkl2KNPf9zzSXVfPJE359TQpS3TVhWTqoEp_CIQEcZzhEBI531gUXCLCW42CTcKlJhPyjcqpjFn_ODQ1ctJjnEcHdbR1IY8QGr5us6EJqpniI-7lvQw2ahZIXr5CSsoDwHxeo4J0H8Xx6ooBzNLxWgQEKwLLFUek_sjir4k7OVOgQrcAly8dw3R74J8z5f1eAcluN5qs6NiVINeHfStuRn0AYs8_Oop-xTL4HiAxbxp4XSjknDRhF0UTSXCKAhNLcU0knubEkxz_wvcKp89PkzYH6reNduywV-gmgmQYm1ArIGBFAeTPfxBMY0SzX49fA3HUDH9xbYOA--Ek7gQKOCamMfDqioP4vc7Tff9eH1XDK7MbLshhhCkOo_KsnlC6LaI0b-IxELAeIhEdj5w-Gjvhb46IJN3Bm2cLSaZ2EmVe4oEd8jRDbwQT3uYbBliBPibxAeI1BDXQttWdNScK1KnQipuC_ksBO-h1tt37RsNsESW6-oHhy3xZL7ppdwVlkdMv7aHPkxBvHjSaZEPFXCKlxREf09OcOh86S4tnX6dPqkc21v1ztrFZqa8n-_nmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5b20b4ab0.mp4?token=IVkp4r8qVpd8RkrQWw8ojKzZs1KFRhaWf1hCDzqMdfdBuIiG3_4-U7TjRQVnbqjUFf_SR99aijm0B2BmtFCwmn12K8fYzSokraAMsxZXN-Vkl2KNPf9zzSXVfPJE359TQpS3TVhWTqoEp_CIQEcZzhEBI531gUXCLCW42CTcKlJhPyjcqpjFn_ODQ1ctJjnEcHdbR1IY8QGr5us6EJqpniI-7lvQw2ahZIXr5CSsoDwHxeo4J0H8Xx6ooBzNLxWgQEKwLLFUek_sjir4k7OVOgQrcAly8dw3R74J8z5f1eAcluN5qs6NiVINeHfStuRn0AYs8_Oop-xTL4HiAxbxp4XSjknDRhF0UTSXCKAhNLcU0knubEkxz_wvcKp89PkzYH6reNduywV-gmgmQYm1ArIGBFAeTPfxBMY0SzX49fA3HUDH9xbYOA--Ek7gQKOCamMfDqioP4vc7Tff9eH1XDK7MbLshhhCkOo_KsnlC6LaI0b-IxELAeIhEdj5w-Gjvhb46IJN3Bm2cLSaZ2EmVe4oEd8jRDbwQT3uYbBliBPibxAeI1BDXQttWdNScK1KnQipuC_ksBO-h1tt37RsNsESW6-oHhy3xZL7ppdwVlkdMv7aHPkxBvHjSaZEPFXCKlxREf09OcOh86S4tnX6dPqkc21v1ztrFZqa8n-_nmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نمایی از نیمکت مصر در صحنه دریافت گل‌سوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/99048" target="_blank">📅 17:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99047">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1dea537f8.mp4?token=Gny_x9mY4NxdgIdlGLd8nb5YnEUEw8jegdezFKsqf98KtDnIEYoFsvcIELDYF0KpA_dfuykVp-f25-25jbkGFAv569pwVZzTPhdEF9OdVPmxj8mg-YTI-L8-H2-dp9Xi6IZ4kNcA8w1_ayK5KMfkAWufhezo0UgToGX1dJmVmRBXrbMx7lRP2wJLpeWuP-9RJLRGDDNAZlBmTRt0Sw23m2osvUN2DeihACD4uncl5QkSX5wgXH8-PIW3Ibwk9sI4JsS-f_3-l-48xG-XLWr59yM5HWLTv49RRA0ufnqHA3lzOOv03hCzvIqJoieTZv_oXrBC3GvhvS6P2uwncFnTVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1dea537f8.mp4?token=Gny_x9mY4NxdgIdlGLd8nb5YnEUEw8jegdezFKsqf98KtDnIEYoFsvcIELDYF0KpA_dfuykVp-f25-25jbkGFAv569pwVZzTPhdEF9OdVPmxj8mg-YTI-L8-H2-dp9Xi6IZ4kNcA8w1_ayK5KMfkAWufhezo0UgToGX1dJmVmRBXrbMx7lRP2wJLpeWuP-9RJLRGDDNAZlBmTRt0Sw23m2osvUN2DeihACD4uncl5QkSX5wgXH8-PIW3Ibwk9sI4JsS-f_3-l-48xG-XLWr59yM5HWLTv49RRA0ufnqHA3lzOOv03hCzvIqJoieTZv_oXrBC3GvhvS6P2uwncFnTVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🔥
آنالیز‌ گل‌سوم آرژانتین مقابل مصر؛ چه ضد حمله وحشیانه‌ای زدن و انزو چه کاری کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/99047" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99045">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVglmXO2ZsLsCdrOPxlvhsXnIPOY4WYLIAz4AJ_ANfIN9bHwflPUQnvQzGTBq2DbO7BKRtpww-hMNPDziBJVScbJ1D049sd0ugYhal4_ghQRbzfswv7a6S3SJl5xZZ6_Z4q1imeC9qqXNWu_7tr9xMzmMQrwx1MLSblkubCVB6r3ey_Ffm99xSygogXK2gJ2LXUx1AvmGHziCYKyctBevpQunCLHSG45Vtma0_gZWLfvxLky5jHyomziMTddgUt-2oVTDQw6WGX8CpukKyRyI8yaXFa7vvRMO2Um3pHMbmFJv-dULA7wPAAFViA4oJVPvKZiy8VULhCgPc_pLRFs8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oxy7ozqzdRIDBdiUfqe2D2N5v7Q8v6Y7WmCraeRcpXW-jc4RdD_Q5EgdQa3Vm3mDEoJJ0OS7kOv2VUjR9IttxYyoX7-Y8a1O1kcIQzkVCfuRx8p0XLPT8THkTvRl-ee8jmBZtRUMY7Lv_Ts1jmqqAI3g0GszNEjn7U4MSyGSmzOQQvzFgGza2NejeuZVi8aLgudztkIFmBlppVkrcWD6RRcwEo_oXNbZtml81qwQ7hp4gKB5ptFjbe5BAU6d_JliEU41y4KcbBGjhLEu6TP2PnbkL87tpistFt9rfouebtfyjVfBB9ohI_Krt7cSVkDeD9xcplRwvpoGUgUWV3IemQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
بازدید روبن‌ آموریم از موزه افتخارات میلان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/99045" target="_blank">📅 16:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99044">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔥
🇦🇷
هیجان بالای گزارشگر تلویزیون آرژانتین در صحنه گلزنی مقابل مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/99044" target="_blank">📅 16:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99043">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/be8Rl2sq-yfwqsByrwa5hhiBZZmCXmzp-MmfWGC_mPT2DVBikhaIhmYfwSx_gu6zA0oIx2o1DWZYTIfPu0e1Rd-NrI1RPgifNOn8lUyR1SjGStsREC12nj1NTurcfjzOU7m-4ulE4TqEPpRvja_jJWbKT6U-tAejZna1mV_eVvfGHL3e6galTmMPTk41cU1GQHPw-L0QwOI-ncGDjqZZl5LNNz4jJIoO8x6R0qyVChpLNoBHL1S3AYh-poRzGbvbhBrHVSM8dVkJ8n_kabqGkbS1j1GA5sQLQ035sp-Unw8TGCRRbQt7xr9XsiBhSK4W0Z2VsTIltjOAFXTanETiOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🇪🇬
تصویری جنجالی از داور بازی دیشب مصر و آرژانتین در ⅛نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/99043" target="_blank">📅 16:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99042">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e80c79c91f.mp4?token=quCISkm1QjLAgxoYQvOMguiRq2sErMILZ521YjZU6oYhY12wZNov6J1CVZHyBSh_A1ibCcKnhbxVPUpr0FVNV6YNQsqXdpk9yPduDfjfiWQ4uwTTtT8oZ1hDMkpP_iIxeUMUjOKTRzDeTBDxSsnKBaZkwEZIEsH46Nj0kMgyy0H8zIRLvNpDRnt7Aq3t6dQ6GJWbWcTwE9VRbPuebw6l8H7AI6_f585QCP9fiH5OUlafTIUHRaqxaUwL9Qti3LrUEQ_Ah0waynN12KXlC4AZ_ke1ZZ-Bk09WwCEHM8R5gUWKLoA4NCivDXHNChLfXupRi0tXSdrAqyvV4mNpBFgopQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e80c79c91f.mp4?token=quCISkm1QjLAgxoYQvOMguiRq2sErMILZ521YjZU6oYhY12wZNov6J1CVZHyBSh_A1ibCcKnhbxVPUpr0FVNV6YNQsqXdpk9yPduDfjfiWQ4uwTTtT8oZ1hDMkpP_iIxeUMUjOKTRzDeTBDxSsnKBaZkwEZIEsH46Nj0kMgyy0H8zIRLvNpDRnt7Aq3t6dQ6GJWbWcTwE9VRbPuebw6l8H7AI6_f585QCP9fiH5OUlafTIUHRaqxaUwL9Qti3LrUEQ_Ah0waynN12KXlC4AZ_ke1ZZ-Bk09WwCEHM8R5gUWKLoA4NCivDXHNChLfXupRi0tXSdrAqyvV4mNpBFgopQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
🇪🇬
تصور اشتباه مصری‌ها از لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/99042" target="_blank">📅 15:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99041">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5807d621b7.mp4?token=nCiAgrErusM3AoNdDJQPaj1RsKxwzdVY7w-1Zqh4Sce1S4QmBXQGL9TQ3oQNIHyS66Q0OM0So06JQ7coc9e8hRZ54RRhrYWaJMPOG1XtdLPkGz5X0ngYN9uDU6SekcZa-VivdDCgKX-cUyAjezknwyPHN7jIxdFTj_0DFVKagjhQOVrEAYNO1vyeYzWq3sG8i6QiDNBgu922zA5tPa1Y_wUsg7QysbmhdGsx8sVaah-iV2Vnu7XCDlkps_5xRHDN1Nn4Pv3OW_Al-AmKhaAvB8sJCiOVnVHErnqoSAovhNI880bfaIJIIFTujrBZITL-Y9Ba4LlQrfV5KG2xD9D2Z4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5807d621b7.mp4?token=nCiAgrErusM3AoNdDJQPaj1RsKxwzdVY7w-1Zqh4Sce1S4QmBXQGL9TQ3oQNIHyS66Q0OM0So06JQ7coc9e8hRZ54RRhrYWaJMPOG1XtdLPkGz5X0ngYN9uDU6SekcZa-VivdDCgKX-cUyAjezknwyPHN7jIxdFTj_0DFVKagjhQOVrEAYNO1vyeYzWq3sG8i6QiDNBgu922zA5tPa1Y_wUsg7QysbmhdGsx8sVaah-iV2Vnu7XCDlkps_5xRHDN1Nn4Pv3OW_Al-AmKhaAvB8sJCiOVnVHErnqoSAovhNI880bfaIJIIFTujrBZITL-Y9Ba4LlQrfV5KG2xD9D2Z4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کسخل‌بودن که شاخ و دم نداره
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/99041" target="_blank">📅 15:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99040">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/537c4a99f2.mp4?token=IdjJs9I30LVXb5dm2pl5hOXmfBR6t0hZAfsfcIX8d6oRHP-pYvu3x84vJZPL9N5m57uuebUxcFfasGzEImaymmWJPUKFubThElfXWzV612lrB57B-KmEqDof1EbRJIYt5xvrAGrztM2CzEteYRIPqBYeHjuwudsMXaO_U1fSwgjLE5QB_MJZtysy_sbRAyzDwA_cKuQTDkyaWBxDcbQYYlWo7yAw0mRJBIEB38m-RAY7ASS-r1-wouD_6IUszy0b8WEDKl-e8w6diw-m1-6fhOcnY8z5AR1EnmrqrB9CkgePLmAT62NkjP1VE8p3m7Z3LZNxwefJop1281I97-9wGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/537c4a99f2.mp4?token=IdjJs9I30LVXb5dm2pl5hOXmfBR6t0hZAfsfcIX8d6oRHP-pYvu3x84vJZPL9N5m57uuebUxcFfasGzEImaymmWJPUKFubThElfXWzV612lrB57B-KmEqDof1EbRJIYt5xvrAGrztM2CzEteYRIPqBYeHjuwudsMXaO_U1fSwgjLE5QB_MJZtysy_sbRAyzDwA_cKuQTDkyaWBxDcbQYYlWo7yAw0mRJBIEB38m-RAY7ASS-r1-wouD_6IUszy0b8WEDKl-e8w6diw-m1-6fhOcnY8z5AR1EnmrqrB9CkgePLmAT62NkjP1VE8p3m7Z3LZNxwefJop1281I97-9wGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
👀
ارزش دانلود 1000000000000
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/99040" target="_blank">📅 15:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99039">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmtcro9SL8KYcGNrGs4GcCFmtKfR-DGpRwZMYYVrlpWTKjDCFq5aaRjwgws9u-F9tOzxjoYpy3n4DERr-Yoiu-bTFUP839etq7XaokDeekZz5aa2WKOWgURk3DVvswGbYjN7UydQm1VnB2XDAouq8j1PYbc9SqPU0JXV5uC1AdrT4DOQGXA44hS7Je_cMn8btGBeou8aMx3fov5PODr-FOir3YHEAL-okBJ8NhGHElurQVnhRiUA2mMy2bzm5Qi4Q8T5QYkvWUYVP4-3VdeWPAu56WxKK_tp2qrtaCVCo2MbU0WDlvjfIrHWaFE8qYiy97VySoayfqnYjHcc03SoBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین پاس گل تا اینجای‌ جام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/99039" target="_blank">📅 14:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99038">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41611ce35e.mp4?token=HugA34S2-bHqI1J1ClJHXbH0yRkgstpqluLX2jd7AgmYZW8si3fVIriitTxJfDiUmstDvCPFDdJp3qfh2bpit9Bejwm11jv7CVS9RCNYmjqczJ1rDVeJRKA4K45WjDU84osGjtMMJxloLVG5kEiD_UgDB25hLmUCYbTdSfqH241PwXFM5a5wTfS6ekmXxeVr6M7IP1Yv2fI64shDybFQ-g1dEBcqQTL6vJMmDeoloT3vOxFOqSyhl66wW-DkzDGrEmGJ7GlIHfs6WlGv9WefLp_1izSEQUoTFw649HbDTO6ptjnaIUcCQPssqe1lzvYhAlJJKEQnfmhdS5FSBAIqMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41611ce35e.mp4?token=HugA34S2-bHqI1J1ClJHXbH0yRkgstpqluLX2jd7AgmYZW8si3fVIriitTxJfDiUmstDvCPFDdJp3qfh2bpit9Bejwm11jv7CVS9RCNYmjqczJ1rDVeJRKA4K45WjDU84osGjtMMJxloLVG5kEiD_UgDB25hLmUCYbTdSfqH241PwXFM5a5wTfS6ekmXxeVr6M7IP1Yv2fI64shDybFQ-g1dEBcqQTL6vJMmDeoloT3vOxFOqSyhl66wW-DkzDGrEmGJ7GlIHfs6WlGv9WefLp_1izSEQUoTFw649HbDTO6ptjnaIUcCQPssqe1lzvYhAlJJKEQnfmhdS5FSBAIqMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدرو پورو
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/99038" target="_blank">📅 14:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99037">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/99037" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/99037" target="_blank">📅 14:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99036">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/99036" target="_blank">📅 14:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99035">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👀
نظر دخترای آمریکایی راجب بازیکنان منتخب ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/99035" target="_blank">📅 14:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99034">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GiNQG2tynnUTAEFIn0oTn57XkW3Hm0np3c0si02nOQZFLjmxqEu23m-65qg_8BonI8Wm8Ly1q36UZr3f_MWixqI4mg8LiM4Wzetn6AcGeUtbLf22YJHZZTlEvhx8yXSFWJdPpQx50kZVBkhBCBdHkSbWqfE1nkJgP0_5L25kfYqCBOsRfgu3QVeM2YGXEtp40WL5JmggSsQVeV5xdtbDmMwbEq1sRgvVQgyecLHgdpzU2CJXjBhyvE0YtPiSiJ_0ME8mwPH0kGWSuEioF9lPzbo-W8qj_gFtLZuQ3OqgYh-EFOPdsX0dZMfFNAhPxMMziMlX0vZI_Uypwf_7RVZmUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
تیم ملی کرواسی از جدایی زلاتکو دالیچ سرمربی این تیم پس از 9 سال خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99034" target="_blank">📅 14:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99033">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6fa320e90.mp4?token=PWtDW_Vc6ViEXqamFGo2RkttrbLE2DlTvx-BwcB_nOkM5YumgiycQjiVbHJ4QCyvCRycf4KEdR1Q9fiabo0ggZyePBhH6_pKRLqlKx52r4dUJCJEmAEIKBY6-YsYYOXarnpV2Pnxh2F6Bfx9lEwyTaeSttMtybHnD_k0G5oHe_jefAwm64Y6FWl1-kr-k1Tnzf7Ss7l8G9TB0aK8aDChE8cu_NpuKzXsmDjHntCf_UgPgwGOPGVSTydp6pN6DuM0i9nySmPQS1dX2bH3sy6tI0AQ0u3mn81HFU31AMJrhu6U4PmI_GVGAzo7ZU1U1JzYSZbf30nnCyN_JujetXmlyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6fa320e90.mp4?token=PWtDW_Vc6ViEXqamFGo2RkttrbLE2DlTvx-BwcB_nOkM5YumgiycQjiVbHJ4QCyvCRycf4KEdR1Q9fiabo0ggZyePBhH6_pKRLqlKx52r4dUJCJEmAEIKBY6-YsYYOXarnpV2Pnxh2F6Bfx9lEwyTaeSttMtybHnD_k0G5oHe_jefAwm64Y6FWl1-kr-k1Tnzf7Ss7l8G9TB0aK8aDChE8cu_NpuKzXsmDjHntCf_UgPgwGOPGVSTydp6pN6DuM0i9nySmPQS1dX2bH3sy6tI0AQ0u3mn81HFU31AMJrhu6U4PmI_GVGAzo7ZU1U1JzYSZbf30nnCyN_JujetXmlyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
تمجید لائوتارو مارتینز و خولیان آلوارز از مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/99033" target="_blank">📅 14:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99032">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSS05X1_zfgqPZpC4lOUvmAXOZhnmdwaLqGspJlLDcDRsZ4T9hLF7uofqb4vUd6rbpxM_6InIqMRy1covmHkrKXl-E1tbxd8193q_yo3k5bkSe5JK-xfxYraL4jhLV5tR5hGj9qhbGt6Q751ItTxYK-5KhWTEQE_srf4Yq0VMfiJTifmxjGmzDIzPidMAuxa_KQt4AF1kczxSHVypa4_Icf8InOBQYEdPZmqsF0wDli_NSs6KzjZ3RVPryeaGzYA8vQiYP_Eav-bJSAT_3O2Cf92KuD9uMdtXDu2YwDoQXDLVhENFxTMNoxFnyplmOCcOJEC8LzyoxCEDTdzJF2KEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
وضعیت قلبی برخی از طرفداران فوتبال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/99032" target="_blank">📅 14:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99031">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e4a201f71.mp4?token=T9H7TUgOhDbc_N-FoB1caI-Vp1iMf8AUij4k9Rv5gXdkxmP3I7jf4KCU1zHG4D6VpwJKUTgb8q2EBVAE9m1D8LkK_A0LIIF1MR2h9XCJwosPEASUjSzMLrtHKUtoSUaa2IcxNOIPFp6rI50cMiohaZiBp6HW1du4r-H5wlNZnL8uPzVcJxDY--qnuuM_s-St6Ox4QS9Xi0W28iCYOhoBWwYnAW4Uk1oCRoKZEnuId1nTas4bpsQILVmZijUtVNRC4t8ZGi7PimUBs9XG_f4DLhWVOEIVLttK4bEb6y51sDTQ358AYSAqK78cQSAOjYtbziDPdsxA2O1E3xPlmDzWaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e4a201f71.mp4?token=T9H7TUgOhDbc_N-FoB1caI-Vp1iMf8AUij4k9Rv5gXdkxmP3I7jf4KCU1zHG4D6VpwJKUTgb8q2EBVAE9m1D8LkK_A0LIIF1MR2h9XCJwosPEASUjSzMLrtHKUtoSUaa2IcxNOIPFp6rI50cMiohaZiBp6HW1du4r-H5wlNZnL8uPzVcJxDY--qnuuM_s-St6Ox4QS9Xi0W28iCYOhoBWwYnAW4Uk1oCRoKZEnuId1nTas4bpsQILVmZijUtVNRC4t8ZGi7PimUBs9XG_f4DLhWVOEIVLttK4bEb6y51sDTQ358AYSAqK78cQSAOjYtbziDPdsxA2O1E3xPlmDzWaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤩
#فووووری
؛ ابوالفضل جلالی بعد از مذاکره با مدیران پرسپولیس، بدون صحبت با خبرنگاران، محل جلسه را ترک کرد. گفته می‌شود کار او با پرسپولیس را باید تمام‌شده دانست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/99031" target="_blank">📅 13:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99030">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaR0ntGZ2YBvqh16B9MOwVjNAHaQekxXqDoZw0WNSuymF9Lc8opcB0lAWdYqirbVCbqaUnOrpE4tWChKZDWDGc_6WLmWX4VhmbvjF4MFoS_9Ctp9J0T-ylSeovjjhe5Ep9hPpzjbLhNgOOX8xDMHOH3WL_ByqDju3ztejClucpC8JncYEwAZjs3IwGIdYD7Zuq6Qkunm8If3MoH7XySAIB3ebkakbHa0DIvesioWllSpG7lXm6e9G9rUYDh1Va3DZfe7etuhmXbRIL5J5aKTY5zWF5Db96bE_JEpqwr0BY8WtMlgvm9tf5tYRX-zOiEh_40c7JvYV_JVHeL5f-7gYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇦🇷
#فوووووری
؛ بدلیل توهین‌های نژادپرستانه هواداران آرژانتین به اسپید، فیفا قصد داره فدراسیون فوتبال این کشور رو جریمه سنگینی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/99030" target="_blank">📅 13:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99029">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc2e7e2d4.mp4?token=Qe58GBflvDNHMOhdly_eV8gK3XloLktBRZroUC-dfGvRXibn0ojmvwCtX5y-BRsFLZt-0VZP2MIxq1Bd0BtN-SAijve9itKnReXqjP24D8zCFg8zxknWRSJehAy_b0tmRUgp7B2_IU75JYznRH0zqCD4AzGXHvZi00YnYbLiAOOxN9l_dSIehFj2yUmK12svo0P75MA-3ByQh-GWEkRIdK9PPqdVphOnikrxbQ3z1IQ9vw7SY-H6WxcA0GtNUcybuetIOsTb9r4GwdZPVs1QtkIGWfqHVbre07iTBO54YBylgO6h1RBe0RXFKXWy3w7t-XZ3c4z8H-y7liAl9oUyew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc2e7e2d4.mp4?token=Qe58GBflvDNHMOhdly_eV8gK3XloLktBRZroUC-dfGvRXibn0ojmvwCtX5y-BRsFLZt-0VZP2MIxq1Bd0BtN-SAijve9itKnReXqjP24D8zCFg8zxknWRSJehAy_b0tmRUgp7B2_IU75JYznRH0zqCD4AzGXHvZi00YnYbLiAOOxN9l_dSIehFj2yUmK12svo0P75MA-3ByQh-GWEkRIdK9PPqdVphOnikrxbQ3z1IQ9vw7SY-H6WxcA0GtNUcybuetIOsTb9r4GwdZPVs1QtkIGWfqHVbre07iTBO54YBylgO6h1RBe0RXFKXWy3w7t-XZ3c4z8H-y7liAl9oUyew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🐐
نیازمندی‌های خونه هر مسی‌فن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/99029" target="_blank">📅 13:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99028">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
⚪️
#اختصاصی_فوتبال‌180
؛ آرمین‌سهرابیان مدافع استقلال که از حضور در تمرینات آبی‌پوشان منع شده، پیشنهادی از گل‌گهر سیرجان و مهدی‌رحمتی دریافت کرده که در صورت توافق مالی، این بازیکن بار دیگر به سیرجان بازخواهدگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/99028" target="_blank">📅 13:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99027">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🔴
⚪️
#اختصاصی_فوتبال‌180 #فوری؛ حداقل دو بازیکن گل‌گهر سیرجان در فصل‌گذشته بزودی با پرسپولیس قرارداد امضا خواهند کرد. یکی از این بازیکنان مهدی تیکدری است که قرار است جانشین دنیل گرا شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/99027" target="_blank">📅 13:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99026">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vaaZXDGiOJKR8LmTgNJm2EG_cpLCQtCnVxXlAdmrdQFAzNwVSuNx0rgPn1GzGC3sS_a9OJ_q713cRJNta5zyi8edPBH1OUp6fX9Vcn7QmJtuzpll8ehueAnpyHjhEsOkCmb9NshhouTb9ny7QnRck7u5FF3mGpXC2H0nNvYNFEuw7UoOCtcalc7G2gG36CWzfUyAM9ObICFwn_bIJ9M7FhBbn_qcfz5qnD6AnQdoAxg2SBa8EcZCPQ1byPw7HMpM9PDm4YDlxO19_AuOo9ualVqJkb7QkWkFrJo658xEZBbf0hncUil_mh6_d0RvaOt-GPGTUV2sXt6lUJdTeP-6mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
جمال شریف، داور بین‌المللی سابق:
- تصمیم داور مبنی بر باطل اعلام کردن گل مصر، تصمیم درستی بود.
✅
- تصمیمات داور مبنی بر عدم اعلام پنالتی برای مصر، تصمیم درستی بود.
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/99026" target="_blank">📅 13:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99025">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tokRtPfHonxRR3h1OScoXEzs2yCkrCxfY3gFJggX6bqnnxNXlSavE6riTmYgpxuQcPTKURzfwfAioQnWK6CE5KOAnAnhPeA9XWYUznsLIWf1wK3IafA-0Nb9N-RZE8TccV6DppNHOTDZQOeBzEqbBK6zIkCWkj-ngvgJHZ8V1_OTDbb7tVUfpDHrfzOP_rx_jsaKpaPhgNYHL_akPmDebJ4H7Jhc90cPuRVwAGAfYeKZEP8eB5hWijljkbmESM6O_N-jlrrAnUrEY6Qa5dAhs3rabtXyUlBvNpvilcEoHJosqDGrEdNIjoY_Hbd0fDz9uyIiuh0D8UnmfRwa9emSBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
‼️
تعداد دفعات اخطار (کارت زرد) دریافتی تیم‌های راه یافته به مرحله یک‌چهارم نهایی جام جهانی
:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس: یک کارت زرد برای هر 7 خطا
🇲🇦
مراکش: یک کارت زرد برای هر 9.8 خطا
🇧🇪
بلژیک: یک کارت زرد برای هر 10 خطا
🇨🇭
سوئیس: یک کارت زرد برای هر 11.5 خطا
🇫🇷
فرانسه: یک کارت زرد برای هر 12.2 خطا
🇳🇴
نروژ: یک کارت زرد برای هر 13.6 خطا
🇪🇸
اسپانیا: یک کارت زرد برای هر 17.5 خطا
🇦🇷
آرژانتین: یک کارت زرد برای هر 22 خطا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/99025" target="_blank">📅 13:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99024">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ddf556eb1.mp4?token=nrnzG6Ua7NfhPdHoXwP6m1z-aI2YRPMP192gOoT0wVMJp47S5JXyVuQ2wWRcXPcKoyPncvJ15_evH2xZmFIgWbq6Ov1S65DsJFQ53bB7Y7rm_i0A8scoWkC5oj84eJ8BEcccObLvQDQ8HEWLnyPZ4xhqHeHHQQfLXmaENNtZ4BdxzDM2cqXnnfMh32bR2FbKLtCEW6Gg3HSLN_umkjOoNSS5Z1m8PGWoqVgOOH_1XFSv2UBW0Sy5sipY8isFu_aTVoLtH4htJm2Q2ikWXwMrBWyqPD7eUta5yGiI_ub3BUKnN5bdpzVi83koBHEXryvzYT5PlUXkFxiPBxjAcQOMDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ddf556eb1.mp4?token=nrnzG6Ua7NfhPdHoXwP6m1z-aI2YRPMP192gOoT0wVMJp47S5JXyVuQ2wWRcXPcKoyPncvJ15_evH2xZmFIgWbq6Ov1S65DsJFQ53bB7Y7rm_i0A8scoWkC5oj84eJ8BEcccObLvQDQ8HEWLnyPZ4xhqHeHHQQfLXmaENNtZ4BdxzDM2cqXnnfMh32bR2FbKLtCEW6Gg3HSLN_umkjOoNSS5Z1m8PGWoqVgOOH_1XFSv2UBW0Sy5sipY8isFu_aTVoLtH4htJm2Q2ikWXwMrBWyqPD7eUta5yGiI_ub3BUKnN5bdpzVi83koBHEXryvzYT5PlUXkFxiPBxjAcQOMDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره تاریخ فوتبال لیونل‌مسی
💀
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/99024" target="_blank">📅 13:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99023">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aff9a0d70.mp4?token=TqZqbPmKc_TmLalbYOv5uqUfrRCOJFts10G4bHaBovZKqcJu7XoRLiEtIfo2hWiobop2kPqMatxdsLAXJlOcsdnxsSJd1yFKR-c36P_KepxeKcVvNGJmUU0nKm_gZl7JMPuN60xxoilp80X_idp8yByznmgHArKrNYPakqsIMA9nfa0MD7sroNLTcJq0BeOaTPCOIvH-p8KVlsgr5ZEmS5HYTd55s39N7g8k71XwmTQOAMMMgfAWhGbcAvPwePmC3Xcy979VDWxEC4HtTKJlQ_Rc4uS6Ssxe7BT0DrWbHF3RMP4BJTA8FueYu0CnZ_DWjZdgSmy_dWeph9JWa-mSPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aff9a0d70.mp4?token=TqZqbPmKc_TmLalbYOv5uqUfrRCOJFts10G4bHaBovZKqcJu7XoRLiEtIfo2hWiobop2kPqMatxdsLAXJlOcsdnxsSJd1yFKR-c36P_KepxeKcVvNGJmUU0nKm_gZl7JMPuN60xxoilp80X_idp8yByznmgHArKrNYPakqsIMA9nfa0MD7sroNLTcJq0BeOaTPCOIvH-p8KVlsgr5ZEmS5HYTd55s39N7g8k71XwmTQOAMMMgfAWhGbcAvPwePmC3Xcy979VDWxEC4HtTKJlQ_Rc4uS6Ssxe7BT0DrWbHF3RMP4BJTA8FueYu0CnZ_DWjZdgSmy_dWeph9JWa-mSPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇹🇷
تو یکی از لیگ‌های سطح پایین ترکیه جوری داور رو کتک زدن که بنده‌خدا نای بلند شدن نداشت
😐
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/99023" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99022">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🇧🇷
فدراسیون فوتبال برزیل حمایت قاطع خود را از کارلو آنچلوتی اعلام کرده و این سرمربی کهنه‌کار به فعالیتش ادامه خواهد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/99022" target="_blank">📅 12:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99021">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/869cf9501e.mp4?token=A85dcOtpGqKjN1_mk59KYtXI8xHxnVaAVNivDr-dUr6zCyhRV0R9PczuaDHjY9eZm3ke4gpeUGEr_8YuT8M9mg_63nOi1JGJu766mVnZBDWaFl4DJr1shjQ0BFfrO1lkTBP46fhCALEvRhuAb8V0070WBZju79FYC8aAFyGl8_gEj_D7AY5t8IcTf8YGmpPcBLZGqOFNxd_n7KB_RslUpheFLQbcxoxI5APDbxtp0SbR-jo_ChjlJeKRCDm0Y_ahbf_yLpp953XINZkuThWLLiHRnAjSjQfRII08s0P1n_oxWc6NJWUsj4vI6ulf67ZJRwOeGRTfqj0_uLNcpSnC4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/869cf9501e.mp4?token=A85dcOtpGqKjN1_mk59KYtXI8xHxnVaAVNivDr-dUr6zCyhRV0R9PczuaDHjY9eZm3ke4gpeUGEr_8YuT8M9mg_63nOi1JGJu766mVnZBDWaFl4DJr1shjQ0BFfrO1lkTBP46fhCALEvRhuAb8V0070WBZju79FYC8aAFyGl8_gEj_D7AY5t8IcTf8YGmpPcBLZGqOFNxd_n7KB_RslUpheFLQbcxoxI5APDbxtp0SbR-jo_ChjlJeKRCDm0Y_ahbf_yLpp953XINZkuThWLLiHRnAjSjQfRII08s0P1n_oxWc6NJWUsj4vI6ulf67ZJRwOeGRTfqj0_uLNcpSnC4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇦🇷
لیونل‌مسی با این طرفداراش محکوم به بردنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/Futball180TV/99021" target="_blank">📅 12:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99020">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
‼️
🎙
🇦🇷
اظهارات ژوزه‌مورینیو سرمربی تیم رئال‌مادرید علیه آرژانتین و فیفا:
🔹
وقتی شما دو گل هم جلو باشید، باید به این فکر کنید که تنها با ۱۱ بازیکن آرژانتین که در راس آنها لیونل‌مسی است بازی نمی‌کنید بلکه باید توجه کنید که اتاق VAR و فیفا هم مقابل شما قرار دارند…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/99020" target="_blank">📅 12:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99019">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXLu-C11bFcVRDHG46w0AyC8oRB4WMOYtG_XRuX8q0RI2Z2bIRNh1loEJ83pSJW_myFvdF5y9z-a1lAt5fndt_jgeRHcR-5NPfC58t-yiH5BjNOjNklEqRgirXHqJu1OU7WJeTzuNagxp7-bvvWxG2VDJ0e9bYIQ4joFSB96zB_evlfKhf-t9s6fWr2KpzowiI8K-lbKs6nSY0cDFiM2ywZECJcIU7qn4eZUko-Z0NnwXyV5RXSrM53sm4tR3VDdvSbIptuquy0b6yh9yAHKKQNyhNOnTSeIHNRkBUiZHrAAZBW_BY1NyoR0zU5U_ObYkH-vjXm-dHAPuKzZY4iiLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خوزه فلیکس دیاز:
منچستریونایتد به اورلین شوامنی پیشنهاد قرارداد پنج ساله داده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/99019" target="_blank">📅 12:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99018">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_codByA9exYlcveQ51SbZbGcJQrzzLzdtAqnP8vROG7eTRlViqCdRD-MDusLAUlBK1feLnk6lmJQ2NA8_Sqt6z1_1yyzTlyxRMAeCxi147OH_zcx3Zo0iwjEhXd8MayXKcQuUV2Sr_6riDZOJY3NL51Fr61P0REzbnjUh5L1NpZmRk9wHO-YKMjnUNcI8RiFBa-A-mwepqWwXD0ciOMmf53JQyDwq55ukIOm25LIVa0W-AEAeTxhxuyaCysr9BBdIusEh6Li5yZvwDlfYB9hqb5Z8IknPPBTqQog_pM5Fee67RhjJaKPslp2vKKh9uQz2jNE5DKcGGyvP2fyej39Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🎙
🇦🇷
اظهارات ژوزه‌مورینیو سرمربی تیم رئال‌مادرید علیه آرژانتین و فیفا:
🔹
وقتی شما دو گل هم جلو باشید، باید به این فکر کنید که تنها با ۱۱ بازیکن آرژانتین که در راس آنها لیونل‌مسی است بازی نمی‌کنید بلکه باید توجه کنید که اتاق VAR و فیفا هم مقابل شما قرار دارند
🔺
مصر شجاعانه بازی کرد و باید به آنها آفرین گفت اما این سناریو مانند فیلمی است که از قبل نوشته شده و برنده داستان هم قابل حدس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/99018" target="_blank">📅 12:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99017">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwjBWpUBdXPw6QirFmnnF_ohZbrFFsEqKYizA_BhMscdKycwR3qj0Ie9pan8KK53cFZrVUJtCvlbP5QDbgtBI6xHYaH2bBpO3nxi1VYZ7iux16vYkacGQY_1LlJXtkAUcoyN-lTuTI9LOcurvMrBp49kG19frbQZLKt6Zn02yM_WgZgYNZ7eP0KqTN-EqHofW9nUJ-ls2r637oI5lJzFM2IuHQX1Y9Eq114Uq8nrhVjcuV4RSQyFim-PNfgTpp4QLQ2Fv-8Fo2Pp_jVUyT_MKXj0SZnJY2f2SyqqUR-x9sgfA4uUjYjuNCped-uhsaByri1o-gyK_ZGHpaWqEJxHsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🤩
ابوالفضل جلالی که چندی پیش اعلام کرده بود حضور در پرسپولیس به معنای توهین به هواداران استقلال است، تا ساعاتی دیگر با عقد قراردادی دو ساله رسما شاگرد تارتار خواهد شد تا به عنوان یار ذخیره میلاد محمدی در جمع پرسپولیس فعالیت کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/99017" target="_blank">📅 12:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99016">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری از ترامپ: تصمیم برای ادامه مذاکرات را به کوشنر و ویتکاف واگذار میکنم اما از نظر من دیگر تفاهم‌نامه قابلیت اجرا ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/99016" target="_blank">📅 12:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99015">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری از ترامپ: آتش‌بس با ایران به پایان رسید و از این لحظه هر دستوری بخواهم برای زدن ضربه نهایی خواهم داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/99015" target="_blank">📅 11:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99014">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوووووری: ترامپ: توافق‌نامه همکاری با ایران به پایان رسید. ما زمان زیادی را با ایران تلف کردیم و باید کارهای خود را انجام دهیم و دیگر خبری از معامله با این افراد شرور نیست
🔴
شب گذشته، ما به ایران با قدرت زیادی حمله کردیم. ایرانی‌ها مذاکره‌کنندگان کثیفی…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/Futball180TV/99014" target="_blank">📅 11:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99013">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوووووری
: ترامپ: توافق‌نامه همکاری با ایران به پایان رسید. ما زمان زیادی را با ایران تلف کردیم و باید کارهای خود را انجام دهیم و دیگر خبری از معامله با این افراد شرور نیست
🔴
شب گذشته، ما به ایران با قدرت زیادی حمله کردیم. ایرانی‌ها مذاکره‌کنندگان کثیفی هستند. ایران به کشتی‌ها موشک شلیک کرد، و به همین دلیل، ایالات متحده واکنش نشان داد.
🔴
آن افراد بیمار در ایران، چیزی بیمار در ذهنشان وجود دارد. آن‌ها بد هستند، من آن‌ها را دوست ندارم، هیچ‌کس آن‌ها را دوست ندارد، آن‌ها شکست‌خورده‌اند، وگرنه تا همین حالا یک توافق به دست آورده بودند. ما رهبری اول آن‌ها را از سر راه برداشتیم، و حتی رهبری دومشان را هم. آن‌ها افرادی بد و بیمار هستند، باید از ریشه نابود شوند، مثل سرطان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/Futball180TV/99013" target="_blank">📅 11:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99012">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYG-OurkqIjeeScCVybjP9y6CFaRTO5xDYZXLJoyufmzLYj3YI02W0MLdkjyIkTeq0IuQQIHAg8hn6qPBS6giWFovkZ6LSXkOPWYC806dyYDgjREYN_j964K_6E4B5QXvyGkSzL5n0cllNM4b7O9kc3OF-lkgR_YlIwbxZZyh_3xkZyFT3aAl2ckExruODKZkhr5h0P244_jFAD3bxvMJzxJ-LPOGXI_M2fEfFTRq0X2YpVS9vlaHtmHotoSe9AieLwh4puyflgF60fn6BDTuQtrAb0jAjQL5UdcevjWC4uUDfW1UuA8_pKVZ8YegDOKa5KmKa4ul2aBcGgR-zu0ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اتلتیک: رئال‌مادرید تصمیم گرفته که در کنار داشتن کوکوریا، آلوارو کارراس را نیز حفظ کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/99012" target="_blank">📅 11:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99011">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ls-_vfxfxs4c7yzfuuE4lr0rdIfab37VnT_AvjZ9RD_KrlWwGp_kVPWzvyo3u-wL6jFFq1bbWSPHjpEvPr2SzsNQSOqzsOfjqfx1AB6kFz8jqAQRBPw9V2qQ9Mfaumg4XRSjlN3vV4xLU94bWu43uiILU564YIh-l8MPkkrCyJe-yrDIvL6i-0cEb1WRhH5B-m2RMms1ZwPnq65-o65wohzkdlGfoLIoM-5LOPYnkZF0Ixta1sHvnpy4tLzpPqBK9G3iXs6IHPFki77tPs_FlDhPRVpijUNZCu5Mz2AH8QugCLtZ1GcUi7L5YWjs_Z8g401aeHs7ZySjHHHAGhzJZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🤩
ابوالفضل جلالی که چندی پیش اعلام کرده بود حضور در پرسپولیس به معنای توهین به هواداران استقلال است، تا ساعاتی دیگر با عقد قراردادی دو ساله رسما شاگرد تارتار خواهد شد تا به عنوان یار ذخیره میلاد محمدی در جمع پرسپولیس فعالیت کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/Futball180TV/99011" target="_blank">📅 11:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99010">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37082570ef.mp4?token=IKhPE29uoHuAe_-HSXZCgoI2SK4ahujpWEpQ8LRLUML3vZCVU1G8gjAg9fYLjL89htnEtkrQ_0zOLBhJLzM-3qGjJws4rf-8bfV_wCGRae8hIwnDWHH_TkQZjZgHrkTRzIQuOs6I_zCUR9VLjC3ac_qwY8swrsHMs3xmkCmgz941rBdhYu0r0HvdkLtQShE7z27MkYRf1nAN2nJMrLYbVPmLupr466Xra0Xf_fLZWHNlFcW9B0IjQR3ls-Z0_rJ8j0w6SxMEU0zEUNZHoy5H7xzegbHkph9IK6Swt5heeGBSkat1eMrdMwvdqsnt2ULX_GCmzgo1OWYwNCAktpY65gq0q8leTjAw6C_OuqnqXuEYZ2JQQXcaLbcaY9YWKepwx3ScZghNHOn8G-pUDbURDZjGPIA20kV3yJPbBogVKrtVofd88ohnH0zww3VwttBEgG27CFZLNomptmC73Ffg2rDbi6EunDgry_6o0O9M6404agApHhrgFyPTjNHdwRZHaStfFTjYR9UVPCeO8G85HioB8ZaFpRwo3SISaLV5E5PbZYXytzsR0N3QDGIeBuYy_gHnPcZz7y5H2DOYailpPJcqKDcxT01OFUa2P1hF7n5YN9bX844mvd-0KOBWWEv48AOnx9VOWugRajIFHdnrtp_9iY18Fv02YdZnr2zQ-cU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37082570ef.mp4?token=IKhPE29uoHuAe_-HSXZCgoI2SK4ahujpWEpQ8LRLUML3vZCVU1G8gjAg9fYLjL89htnEtkrQ_0zOLBhJLzM-3qGjJws4rf-8bfV_wCGRae8hIwnDWHH_TkQZjZgHrkTRzIQuOs6I_zCUR9VLjC3ac_qwY8swrsHMs3xmkCmgz941rBdhYu0r0HvdkLtQShE7z27MkYRf1nAN2nJMrLYbVPmLupr466Xra0Xf_fLZWHNlFcW9B0IjQR3ls-Z0_rJ8j0w6SxMEU0zEUNZHoy5H7xzegbHkph9IK6Swt5heeGBSkat1eMrdMwvdqsnt2ULX_GCmzgo1OWYwNCAktpY65gq0q8leTjAw6C_OuqnqXuEYZ2JQQXcaLbcaY9YWKepwx3ScZghNHOn8G-pUDbURDZjGPIA20kV3yJPbBogVKrtVofd88ohnH0zww3VwttBEgG27CFZLNomptmC73Ffg2rDbi6EunDgry_6o0O9M6404agApHhrgFyPTjNHdwRZHaStfFTjYR9UVPCeO8G85HioB8ZaFpRwo3SISaLV5E5PbZYXytzsR0N3QDGIeBuYy_gHnPcZz7y5H2DOYailpPJcqKDcxT01OFUa2P1hF7n5YN9bX844mvd-0KOBWWEv48AOnx9VOWugRajIFHdnrtp_9iY18Fv02YdZnr2zQ-cU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
این 45 ثانیه رو ببینید بعد بگید هوش‌مصنوعی خوب نیست و بی‌روحه. خاطرات زنده شد.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/99010" target="_blank">📅 11:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99009">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeadf8f078.mp4?token=QhfBwcNxolFtVSbAROJISAt-9one3RrnuD5E2MToLUVc_e2Ie_OiImUlhOK-aYXYp4-c9kdyoOVxnGB9ihqruA8M5-W-yxY7ufkFvZt-8vNaG-F_ntkJ87MCLNnd-hJkXJZtV8WuCv4KXslwZKpnPSVCqltfSGu_96k6VaeHf1YlF8xuHH1kiUkmxzyQexgn0oZsGQatVlOWwZW-jZhB-T7CSBqRXBNHGPcIe-TlXfri7eI8aKscK9grnSCQ9ndbG1brzOg6WspxAYGUja_RPk4O8-2Zs2Q-UIrX3sG1QzKB2cztdfU7Uy-iN3sqtkDWhP2g5ubdMYYcGcw0XENQHUEb1yrqMrA7X0bnZ950c_Vw62VYgCttxH1of_DF-sV_bgfzXGTOLdmz04o08oXEUDLXkMe8_cN9hpf7LYqrxGXF8xk-rzZYZPZUkDYU_ku-MBFOfd6C3BXmlBlFq2EYSI5mhOAVKxWrqU2qjBUy72sJiR12b-aTIPwCiQkXFiNhLGICFDQokqoJNGaxDBJll6ZqhCTS3E20G7Zpd7PDrVT-TxKXm2KtwTQGDbij-7dg4ZCeiiiZccOfg_hXxFotai8gorB72iYbB99hN9NU18SqQteGmVvCo0uqSySDbuT4jbz4kuW9A-tzThV-lhdEYXR4j8NT1GoPCr22LJBDdNc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeadf8f078.mp4?token=QhfBwcNxolFtVSbAROJISAt-9one3RrnuD5E2MToLUVc_e2Ie_OiImUlhOK-aYXYp4-c9kdyoOVxnGB9ihqruA8M5-W-yxY7ufkFvZt-8vNaG-F_ntkJ87MCLNnd-hJkXJZtV8WuCv4KXslwZKpnPSVCqltfSGu_96k6VaeHf1YlF8xuHH1kiUkmxzyQexgn0oZsGQatVlOWwZW-jZhB-T7CSBqRXBNHGPcIe-TlXfri7eI8aKscK9grnSCQ9ndbG1brzOg6WspxAYGUja_RPk4O8-2Zs2Q-UIrX3sG1QzKB2cztdfU7Uy-iN3sqtkDWhP2g5ubdMYYcGcw0XENQHUEb1yrqMrA7X0bnZ950c_Vw62VYgCttxH1of_DF-sV_bgfzXGTOLdmz04o08oXEUDLXkMe8_cN9hpf7LYqrxGXF8xk-rzZYZPZUkDYU_ku-MBFOfd6C3BXmlBlFq2EYSI5mhOAVKxWrqU2qjBUy72sJiR12b-aTIPwCiQkXFiNhLGICFDQokqoJNGaxDBJll6ZqhCTS3E20G7Zpd7PDrVT-TxKXm2KtwTQGDbij-7dg4ZCeiiiZccOfg_hXxFotai8gorB72iYbB99hN9NU18SqQteGmVvCo0uqSySDbuT4jbz4kuW9A-tzThV-lhdEYXR4j8NT1GoPCr22LJBDdNc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇮
کشور شاد و بی‌غم فنلاند یه مسابقه راه انداخته به اسم حمل همسر که میتونید ببینید
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/99009" target="_blank">📅 11:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99008">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f700303ae.mp4?token=GfAxtJ1hjbtMp2c8lG7G-RY5cHeqoH4f3xIKeWuS46msHgLYailTlhwN4X70U1L7btJXrGRRzjozYFq-RescB0tYzqnbAhMm_aE8dUSyApVMrKmxk4y2ZtSTDt_L8M9HqOUKHZdXaqbQ_dyLUN3v1qx9Ykvqji9APfTurMwVbLmyCvt35I2kYuq3cnJHDQjveYtiS-HCU5pWxzitNRconn-A2F30zCKPoB8k5aP6Ib7HHi0lGKEqvXHuLfdFogjIxIjOZShuL4aQp0xnuX7TdVF6atp1tK3ym5zvfKMPi29dMhUAif2WcgYPwddNvpE2TNBAAFcJknO_p4Cbmx2nNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f700303ae.mp4?token=GfAxtJ1hjbtMp2c8lG7G-RY5cHeqoH4f3xIKeWuS46msHgLYailTlhwN4X70U1L7btJXrGRRzjozYFq-RescB0tYzqnbAhMm_aE8dUSyApVMrKmxk4y2ZtSTDt_L8M9HqOUKHZdXaqbQ_dyLUN3v1qx9Ykvqji9APfTurMwVbLmyCvt35I2kYuq3cnJHDQjveYtiS-HCU5pWxzitNRconn-A2F30zCKPoB8k5aP6Ib7HHi0lGKEqvXHuLfdFogjIxIjOZShuL4aQp0xnuX7TdVF6atp1tK3ym5zvfKMPi29dMhUAif2WcgYPwddNvpE2TNBAAFcJknO_p4Cbmx2nNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
تیزر تقابل جذاب انگلیس و نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/99008" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99007">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwfmNTKbmXuwJedccf5FGBXuDfnDjw5KTQaZGfFtd7qN2IBT5H_r7mbpq1oQrBu8aJqoo68TEgFd9U4nBKhFiEPcYvbehcFYXIFvUOpnInlbnj9P8bCNF8IyHLNoISKSt0Mxm1YvU1FuZQPqgaRxqyHt8X9kiw1FhPt0EXdgJt7VZtO8MWY47dgrrTz3k1F2Pm20h4rbmlMtG5JhdgmYD7u8yav4ZpTE6HmwpLfQOImKLeuc-vhdP3Crv5kWuAZSvznYf4Ewq-C5AvoqnduHTs_8nc0WZsP4SnzYfVIccieXCOZ7rnYJMEJZpQWDe2FKXDnyszox5W-dwvcJO2IvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
♨️
مونیرالحدادی ستاره استقلال در آستانه عقد قرارداد با اتحاد طنجه مراکش قرار دارد. این بازیکن که با آبی‌پوشان یکسال دیگر قرارداد دارد، به استناد به شرایط جنگی ایران و بارداری همسرش قصدی برای بازگشت ندارد و احتمالا با توجه به تعلل مدیران استقلال بزودی قراردادش با تیم مراکشی را رسمی میکند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/99007" target="_blank">📅 10:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99006">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری؛ موج جدید حملات آمریکا به بوشهر و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/99006" target="_blank">📅 10:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99005">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/235d7e30f7.mp4?token=pMTetE0kStfqiU7H1NUw6YR9Bu0YHkGQvEkeN_JQP4s1xCD0m6nT3yB6R3lKwVtCqFsT7q8ZdlVre5yE6QQa1tt440Q8K1nzSO2QytlGhugEgK1AfKbcAMMsigDE0BpGlLObJVD7p62Z92oL4DZ73BhrALNv2EKye15Mt3FggXRv82LaSECeBnDJb2IZr6XqVI0BnWzkAdkfS-Rvcl9COu_2jAiDbw5ypJvVkqcdvjmHNZarGW88Lsy94W72O094cNyZrjOhq_A7MRignO9ArRc22E-Us6A9mc9BINytaNxrjhvHopWvz6R86EJUg3UA__18KWTELplRbBCc325MlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/235d7e30f7.mp4?token=pMTetE0kStfqiU7H1NUw6YR9Bu0YHkGQvEkeN_JQP4s1xCD0m6nT3yB6R3lKwVtCqFsT7q8ZdlVre5yE6QQa1tt440Q8K1nzSO2QytlGhugEgK1AfKbcAMMsigDE0BpGlLObJVD7p62Z92oL4DZ73BhrALNv2EKye15Mt3FggXRv82LaSECeBnDJb2IZr6XqVI0BnWzkAdkfS-Rvcl9COu_2jAiDbw5ypJvVkqcdvjmHNZarGW88Lsy94W72O094cNyZrjOhq_A7MRignO9ArRc22E-Us6A9mc9BINytaNxrjhvHopWvz6R86EJUg3UA__18KWTELplRbBCc325MlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇫🇷
🇲🇦
تیزری جذاب از نبرد مراکش و فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/99005" target="_blank">📅 10:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99004">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12da15f688.mp4?token=gLAckSkhVdDHL9Ef7beD6hEvDq9geE_xwK53FBsh0nKY6AOt2Ada4GSjrKEvfVHFvYPIQ0C9AcsHmoIB_1AtTm0jLK8UVVfnYvjXh0LCfq3WbotMyyI1UQqbwyfKvKFYvFuyLsKQIVzQUM1hgJSaG2pS2wVdWlP06ssWUK_WNkD9DMVoEAvjUTf1Fbi8QFhHWXUZkbn323xNcGmUYK2nMdiNZHVQk0Mp-lDO9YmigInT_cvWkUZNmQlIbTnKISYzpl4hke4b2YH7e812UViDdDSiV3kLZcH7N32GVKuaygIL0hk_8Q4UhZcgK0a_Oi6v2Apw0ZwGZmL9jnx4xWWNVoDZB0lmxt3n5QBHkvJHMFf0Z8_nAoBxfScNtu9Pn5xfgbhulsxdhWh6vaslPol3hfK7rfHEa33JiRknd34QIQ3yVM9FiSFhsNOj5c_xCTi9lV5aCDWJj1nf-FGIfI5KQfCqI9wTOQnPWsOkv2jmUY6kYGNGE05XbX5PgwrEdudYh2WGtzXYt0PC2mZzuwH0UzJBId-GSPituB0Qt1JNmMuthMBT5HeBmL6RoiaNp1z4kNlhFE3OYp9QD2zxOvGWQ0XoicVhAcfBi7IltbUaG3Xk2RKWxPs-CRoETf8_heveTyzGK0jPkvZnBn9jCkHn70qhtXrxEo33L5pg7PAm6fY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12da15f688.mp4?token=gLAckSkhVdDHL9Ef7beD6hEvDq9geE_xwK53FBsh0nKY6AOt2Ada4GSjrKEvfVHFvYPIQ0C9AcsHmoIB_1AtTm0jLK8UVVfnYvjXh0LCfq3WbotMyyI1UQqbwyfKvKFYvFuyLsKQIVzQUM1hgJSaG2pS2wVdWlP06ssWUK_WNkD9DMVoEAvjUTf1Fbi8QFhHWXUZkbn323xNcGmUYK2nMdiNZHVQk0Mp-lDO9YmigInT_cvWkUZNmQlIbTnKISYzpl4hke4b2YH7e812UViDdDSiV3kLZcH7N32GVKuaygIL0hk_8Q4UhZcgK0a_Oi6v2Apw0ZwGZmL9jnx4xWWNVoDZB0lmxt3n5QBHkvJHMFf0Z8_nAoBxfScNtu9Pn5xfgbhulsxdhWh6vaslPol3hfK7rfHEa33JiRknd34QIQ3yVM9FiSFhsNOj5c_xCTi9lV5aCDWJj1nf-FGIfI5KQfCqI9wTOQnPWsOkv2jmUY6kYGNGE05XbX5PgwrEdudYh2WGtzXYt0PC2mZzuwH0UzJBId-GSPituB0Qt1JNmMuthMBT5HeBmL6RoiaNp1z4kNlhFE3OYp9QD2zxOvGWQ0XoicVhAcfBi7IltbUaG3Xk2RKWxPs-CRoETf8_heveTyzGK0jPkvZnBn9jCkHn70qhtXrxEo33L5pg7PAm6fY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
لیونل‌مسی ورژن جام‌جهانی ۲۰۱۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/99004" target="_blank">📅 10:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99003">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
❌
با اعلام کمیته جهانی المپیک، تمام تحریم‌های مرتبط با کشور روسیه لغو شد و این کشور میتواند در مسابقات مختلف نماینده داشته باشد. بزودی فیفا هم معافیت‌های مختلفی برای روس‌ها اعمال خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/99003" target="_blank">📅 10:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99002">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ موج جدید حملات آمریکا به بوشهر و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/99002" target="_blank">📅 10:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99001">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb36066e1d.mp4?token=OOmd7RQjg1fA-FdN0PxAozWTS__5KkuGfl34Y74tvKUW1qVo7_fzaQjNMcgBUsHkfxkvwFkU7_KdeZ8ALnSY4SaVsM68X5uZm88xdxLaUbXA27zX6mO96V_nFV1yEtu-oEuE3Mmew7QQR6OBSUvsGi-Oh0B_slzetGjQ1aWmSPqFL6C2PJ4ilCEDlt7JCFgXsAXLUsHtRq5j_IggEVBV8xC9rKjbwEaem1JQ40tRgy3Yc680RvPtvtrUax5sS6U9TGbl1xKqljEpOGeQYvXnemRX7jRJWgO3O3HAv1iXDiXaoAkri-ExwHgmCLN-edVeaCkkH7Ck4YwmE8kczk-Yb4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb36066e1d.mp4?token=OOmd7RQjg1fA-FdN0PxAozWTS__5KkuGfl34Y74tvKUW1qVo7_fzaQjNMcgBUsHkfxkvwFkU7_KdeZ8ALnSY4SaVsM68X5uZm88xdxLaUbXA27zX6mO96V_nFV1yEtu-oEuE3Mmew7QQR6OBSUvsGi-Oh0B_slzetGjQ1aWmSPqFL6C2PJ4ilCEDlt7JCFgXsAXLUsHtRq5j_IggEVBV8xC9rKjbwEaem1JQ40tRgy3Yc680RvPtvtrUax5sS6U9TGbl1xKqljEpOGeQYvXnemRX7jRJWgO3O3HAv1iXDiXaoAkri-ExwHgmCLN-edVeaCkkH7Ck4YwmE8kczk-Yb4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
دیشب هواداران آرژانتین برای فشاری کردن سرمربی مصر با پرچم اسرائیل تو ورزشگاه بودن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/Futball180TV/99001" target="_blank">📅 09:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99000">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f26zKpCr96CYkEFqhBviozTW9g6EPRn0SrvJnWkvOhL6l9V7SgEZ7q7kvA5fvKF01ezx_TtOIzR8P29EqYgMZB7ip-GrcPTj3RxivBKE6tGCXO28yyKUmnZ1HiUGl3GBD0p2u-oe77rdkmMNn5a2LWP3WBAQT0tQImQ0TbttkPHZDMWDSCWO6W9DhfiKTMVBAelEb65qcrD-Vo-mHXtpKXYQHCGgKkg2m_4AVvpn3HNIzsn_krWG8F3REmeRJVcSEVDqGQlasqFwnz4XZraciyirW6EZyOpIrVhLFe1bOUm7maUzHFMbmCEImSqWT2jTz7I9rXlOKgATkRsM3qF0yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
🏆
🇪🇸
مایکل‌اولیور انگلیسی داور بازی حساس بلژیک و اسپانیا در ¼نهایی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/99000" target="_blank">📅 09:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98999">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ef60ffaa3.mp4?token=F6-mdZLVYoDivVrugbhiskecYXNVYNWlUoo6qM4ubxnZouRUr698puO9HLByIKEoVbcgmmf0my9wIaEOKoXMvE9YLINDTB4UxkQU1fxQWmfMVsbKW2nO3uPbyMh0bCp25n5XpUY2c-rJngTZoq-bigQzii3W0kmVK2EVi09pv4GLUBTolUiwKYNEBYCKVfQfWdXzxyEPI-V5BFLsd9y4JN2RQqTj86bLQrNO8XweRZQ2GKEAQ9RhpzK3VSDB5d-zDragYf-UX-tIsx8C-ga3Kt9vV3UuTmqJksbTFe48poTuyTDE2TW6i7L5cGQab2l3fab7MAbPo4ezaVXUOyR-og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ef60ffaa3.mp4?token=F6-mdZLVYoDivVrugbhiskecYXNVYNWlUoo6qM4ubxnZouRUr698puO9HLByIKEoVbcgmmf0my9wIaEOKoXMvE9YLINDTB4UxkQU1fxQWmfMVsbKW2nO3uPbyMh0bCp25n5XpUY2c-rJngTZoq-bigQzii3W0kmVK2EVi09pv4GLUBTolUiwKYNEBYCKVfQfWdXzxyEPI-V5BFLsd9y4JN2RQqTj86bLQrNO8XweRZQ2GKEAQ9RhpzK3VSDB5d-zDragYf-UX-tIsx8C-ga3Kt9vV3UuTmqJksbTFe48poTuyTDE2TW6i7L5cGQab2l3fab7MAbPo4ezaVXUOyR-og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرژانتین به یک چهارم نهایی رسید.
🔥
🇦🇷
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/98999" target="_blank">📅 09:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98998">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FphjUkDfeYEtFescSOAnEjnHbMu0U3F-1PuKNJTxF1jBXlqM03Gc6haKIjSv4KI0pR2NYOHk9i4nKRsG4fmI0yDYdKesgM9jtjaH-pS1C5iDkkm8Jvlx6LljVsUAG8aNbR408fsX1bXCPlIx2WKJe7bGUPEBGcYMrGPDbdIlldVDRBgcbFE_qiXaQEASq_eaHx7lmgNaHaaVsPQhPT5sfGPzPtaf_ibcEb2_h6m5ea4iG7ti6esvlhJrLqKgcyKiBnu8VzobOag0-lP4e5MAr0MNcQF2JExgHK1KBHdmOKqeSCVLJ-F2huTPh5uSMqemUhJHSB0RY_AQ9mt8zq_rXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
| فابریزیو رومانو: قرارداد کانسلو به احتمال ۹۹.۹٪ با بارسلونا نهایی‌خواهد شد. الهلال و بارسلونا بر سر مبلغ به توافق رسیده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/98998" target="_blank">📅 08:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98997">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PD8cSHuUDbeiEV743upQQwWTuwn5GtLJKMZos7EoXuMPBDuYUWAYIXwMlP2eWNzYO38_TiAPXiuD0Sdzq7KQc_0jxr938ym58X3kcAKJ99UpptBYA7NcFPvSPXtVUMoncfNNgLCCTMesj_mR8NNCL3IHCFGfe3OtGW2kJvfwe4VYRdYQNZMo7tCcc8RTAjnug2Q_uQVCM9x6AeBLEu8Lq_eNVXMDbpeVcGDaZPgBvA2lHDNhAqFjYGzQx3YuFA8mQQ9a42I779qbOnIO54Y3upxzVkX8AH6rkBSFUaXM9WDjw3oiy5jEp1Y7MOOJ12SVQbZCxiyyrTqUM541kM6Whg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
◀️
تو گروه D جام‌جهانی ۲۰۱۴ یکی‌از عجیب‌ترین اتفاقات تاریخ جام‌جهانی رخ داد، جایی که کاستاریکا از گروهی که ایتالیا، انگلیس و اروگوئه ۳ قهرمان جام‌جهانی توش بودن صدرنشین صعود کرد و تا مرحله یک چهارم نهایی اون جام‌جهانی هم تونست بالا بیاد.
👏
🔹
جالبه بدونید سایت‌های شرط‌بندی شانس صعود کاستاریکا رو 6٪ پیش‌بینی کرده بودن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/98997" target="_blank">📅 08:17 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
