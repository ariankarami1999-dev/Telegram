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
<img src="https://cdn5.telesco.pe/file/K5KdHhrqbYE3bN8Xqoz16yQipHvGbIU501F09ppmQ5BVP_FyjxoxjHVINnFfTkgOVd5LGo2qhKgDtpYbkTPV1lHdlKG_vUl5zKeR51IwQ8JLqOxRMRzDNkXbk822GMzPU9lq9zQhxd0XRybI50iUYnB3iXkyqxxyr-5A3n_OtngYmTJR2oJ5nJykqYO6hor6Lt5fIsGP4MzzuHlMdLnLJP7C_3Fwrrdk5aUmCrlsWoez7WDOfDbLsujT8zDiDkoUW9ev624_IV2qPCEAunnjQ2wMXfIIXZ0askuf_XPUNuggih5o4Irct_TAGrAJoTcnIYI73cFl16fAXSKsKWb1Fw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 690K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 13:34:21</div>
<hr>

<div class="tg-post" id="msg-96770">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWMIaBfGowNcvDV8NM3k6SAs_jOSIELAxKjI5JeFah3WNj41I7_fyXDEIfGq1jSze8KsLcOyuE4vTaOd4d3SUqMBuUDlXOAMjyodieQ11BIEbaozk34lol1AcJlS3zlB4jjM67LEui6fMKm99YV5hj8NC_vZvNV3GWyBMgHTD6m6Buq0WQu-RwPJT68SYuvMd5Xe8Uf_FsI5Y-oE11J2euL4TSxUT6VGKqQbYiOhBleImP2_sHebmNC81wCxYcvL7VfQlPa8CdEXOgP6A-aJpEBApsjmx0znkGBVhgDNqL96mOHaGgODkI7k2RrNB1nqom7bJv1s7y5_mN2B0z3Hxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری | آاس:
مورینیو از مدیران رئال مادرید خواسته یک مهاجم نوک کلاسیک شبیه خوسلو که در محوطه جریمه تمام‌کننده باشد جذب کنند، هرچند این انتقال فعلا اولویت باشگاه نیست. این موضوع می‌تواند شانس گونزالو را برای ماندن در رئال و ایفای همین نقش بیشتر کند؛ در حالی که پیش از این به جدایی نزدیک بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/96770" target="_blank">📅 13:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96769">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzkDfCD2DG0ZFOzF0tVqHlyFNncHexs-tiFXEnUkQeixMSue8-nNbRX45cKIv4qISgWntC3HqDLYKOhuQleYSt_DOpci_3rBQkMYeJd7JmYgo50HVLqANio8RwV8c8FdE5ozzgvfT0pB3pv0v525TUNBZCuLfM0KfgBaQaj7YdPGelWpYT1vHCIz_pmWa9vhmKNCJUrNJgzjDXPDO0g64HG634G7HCah9W-ygu9RB-1MtU1fceJR4ywsmY4p1jHZfRqvKpY0AvTWvqfGsA2zzsFOu8hJfsajy6mGdZazdf_CbNIWpzFgpjtVEcuxjeydLrcMdFcw3WU9DzzlCEKVnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
آمار دنیس اکرت درگاهی در جام جهانی:
💥
نیم ساعت دویدن نرم کنار زمین
💥
حرکات کششی
💥
تشویق دادن و روحیه به بازیکنان داخل زمین
💥
یادگیری دست‌کم ۱۰۰ لغت فارسی
🔥
🔥
💥
نوشیدن حداقل ۱۵ آب معدنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/Futball180TV/96769" target="_blank">📅 13:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96768">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKgNfosT1sbtdPfuJIHRjRfoDnIe3BTsqXvnx6oL9LHTS0I4znh4bY3U2wczfjg8oX7egixZan1efzH6NZ9D_tAMbgYvMUMtqQ2faOigUjUT4iyDn4SxQYj_C-R8anpzlmI50MQo6pOuno3LZsC8kYWdYcWyn_g9S3dm0m1wMx3ufdhHw6AjJC_Nq5r0WwgGcU3p6W-ZATCieyeqVv3HeES_TCAbf61zPWLSKOj-nb1LU_vrHJ5ry28UWFOQdiN_9CJbScYvXm_BRFydt3muPgtdTPfWJDeb1pRILOqA1PyepK4T3pT3QuEycQDxXJnnkABUBtlo09iTaBGo5B29vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
؛
موندو دپورتیوو: لیورپول به کاماوینگا علاقه‌مند است و با رئال مادرید تماس گرفته است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/Futball180TV/96768" target="_blank">📅 13:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96767">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
‼️
🇰🇷
پرتاب تخم مرغ به سمت بازیکنان کره جنوبی بعد از بازگشت از جام جهانی
روسیه در سال ۲۰۱۸؛ ظاهرا در سئول مردم تدارک دیدن که طی روزهای آینده و با بازگشت از مکزیک، رفتاری مشابه هشت سال قبل با کشور خود بدلیل عملکرد ضعیف در جام‌جهانی داشته باشند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/96767" target="_blank">📅 13:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96766">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e142b950f.mp4?token=aGsU7ySlNtUj8ia7l1iVfFoooegaWKdUIXze8OIbwJ8qVs-fbCKz_eNm506vhy4OCetRNgJ0eUv1CLIASK14KQdx19btN5WydO1ybZkRWT5ZByl5NiIdmCPFdBeWoqvIbM9wzE7pGbWX-WlJE7TFOF86ybnNd1ZwyRKwo5G1pw_QnezIPcclMYAf4h6-V7tIIu9ZKcOqtWwPmMyKLHw2Gi04jmEIihtwrK913IkCEFpNdWNAB7M4ETkDxH6ZzcubcYPxKYymXZhla2rJYOTv7IOic3FSc1jPTdaXAgho-lF5J5ffT_h6X08H1HoCvzeG_bl0EoFcjpVKmq0CPpgkxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e142b950f.mp4?token=aGsU7ySlNtUj8ia7l1iVfFoooegaWKdUIXze8OIbwJ8qVs-fbCKz_eNm506vhy4OCetRNgJ0eUv1CLIASK14KQdx19btN5WydO1ybZkRWT5ZByl5NiIdmCPFdBeWoqvIbM9wzE7pGbWX-WlJE7TFOF86ybnNd1ZwyRKwo5G1pw_QnezIPcclMYAf4h6-V7tIIu9ZKcOqtWwPmMyKLHw2Gi04jmEIihtwrK913IkCEFpNdWNAB7M4ETkDxH6ZzcubcYPxKYymXZhla2rJYOTv7IOic3FSc1jPTdaXAgho-lF5J5ffT_h6X08H1HoCvzeG_bl0EoFcjpVKmq0CPpgkxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
لحظاتی از بازی ایران و مصر و وقت‌تلفی گلر تراز تیم‌ملی آقای علیرضا بیرانوند؛ بابت حذف شدن اینا اصلا ناراحت نباشید چون میخواستن حاف بشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/Futball180TV/96766" target="_blank">📅 13:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96765">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/az1ISDSH6uX2IKpGlultECGXXSynhhQSnjLQgdoEEd2Fvp9acBgdeU1RPWO7Avbne9vZZxtWyo5KRfYrRb4X6CFL9cpsAzCHYBQ3S65c4FHuM0aD5i4kUmZO6GyLt2-tbfe0xKEgWJjXg8HYlQyqhMTbPf3OYRXA67AL2tkAz0gYgNUEAifGmt-a3uVE64TiIJej7LM_-VOPs0ngo_i9uqRXgvqpRY3Zro8KWntk14eOt_qqDztkF-oIY8i6q8RPFGmThI1kZuT4CKKqjp3yyrgQZdiyHdHmHUViqsRAye5_oCPBQ2oelc3iw1YmWSa-GX8TkEglWAPuRALTQ7kMpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📰
فابریتزیو رومانو
:
ترشتگن با انتقال به آژاکس مخالفتی نداره و حتی مذاکراتش با این باشگاه هم به مراحل خوبی رسیده.
بارسلونا و آژاکس هم در حال مذاکره‌ان تا این انتقال فعلاً به صورت قرضی انجام بشه.
تنها چیزی که هنوز روش توافق نکردن، اینه که چه مقدار از حقوق ترشتگن رو آژاکس بده و چه مقدارش رو بارسلونا پرداخت کنه. فعلاً گره اصلیه انتقال همین مسئله حقوق بازیکنه.
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/96765" target="_blank">📅 12:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96764">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a762bac2b9.mp4?token=hE1fQtY1wPfUqBdLeCvWB1ieJSruxt8b4zDLvrQC7Elq7MUn-9lclLqsJOnuCjRO7B_Skl7pAlwFNqyrN9ZudhlhxaW8V-CFO8R06EKGC9Xr3_B_g2EYf4u-3Q6MISzCmQ5gEQjAd6DC6OHKmoKiqwvUIcnnQ9pqyuH7ipPLRNY0bG3PJwhe9H-IFYYj4qG8Nu0Cle1cvzIgO8A1lV1eVFSqQDLqJmqN4F8rSEJAEurIPpiQpakpXDegHp1VI8Ok8XyVyNKHYzbK_VI3n4k5uvOCJFwxDbaxQy8833S5I9Wy3OWMZxewX9iTdzj73J1PH9eQ8gCvRebnTpz2AdV8vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a762bac2b9.mp4?token=hE1fQtY1wPfUqBdLeCvWB1ieJSruxt8b4zDLvrQC7Elq7MUn-9lclLqsJOnuCjRO7B_Skl7pAlwFNqyrN9ZudhlhxaW8V-CFO8R06EKGC9Xr3_B_g2EYf4u-3Q6MISzCmQ5gEQjAd6DC6OHKmoKiqwvUIcnnQ9pqyuH7ipPLRNY0bG3PJwhe9H-IFYYj4qG8Nu0Cle1cvzIgO8A1lV1eVFSqQDLqJmqN4F8rSEJAEurIPpiQpakpXDegHp1VI8Ok8XyVyNKHYzbK_VI3n4k5uvOCJFwxDbaxQy8833S5I9Wy3OWMZxewX9iTdzj73J1PH9eQ8gCvRebnTpz2AdV8vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
انتقاد شدید خداداد عزیزی و جمشید خیابانی از حمایت محمد ربیعی از تیم‌ملی و سبک بازی ایران در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/96764" target="_blank">📅 12:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96763">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293cb5ce55.mp4?token=SKzlVDXIV0KTRqw5mnIsmp08Njwmgp5ywBVGc9BYxcq1XpV4t5x-mazDKkoo8OYdp9EhU8RQy1SyxmjHKbGOPhK3aYEXQ6Il9xPjnt5E1rCFqm0fLRSnqjPkj1XqteMXd48WtEk1SEPz6uTC6KcnOv0Oj1DnrSsvXULyR_2z67t1B2B2nhnkoRqkegbuViQlT7ixlC2ijB38_FVwo1dfdjYSVcac0EQD_ftvIFdWDM9VIbY6v9L6ipHKuHy2NgfIebmoUkdZBg9SqZZjMHGhTeouvyhry4cy3fGHDIvRd8zV_VuSTtu9z_ypvk7LANHCj_eIGTkq72dBagrpg8nnsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293cb5ce55.mp4?token=SKzlVDXIV0KTRqw5mnIsmp08Njwmgp5ywBVGc9BYxcq1XpV4t5x-mazDKkoo8OYdp9EhU8RQy1SyxmjHKbGOPhK3aYEXQ6Il9xPjnt5E1rCFqm0fLRSnqjPkj1XqteMXd48WtEk1SEPz6uTC6KcnOv0Oj1DnrSsvXULyR_2z67t1B2B2nhnkoRqkegbuViQlT7ixlC2ijB38_FVwo1dfdjYSVcac0EQD_ftvIFdWDM9VIbY6v9L6ipHKuHy2NgfIebmoUkdZBg9SqZZjMHGhTeouvyhry4cy3fGHDIvRd8zV_VuSTtu9z_ypvk7LANHCj_eIGTkq72dBagrpg8nnsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
کنایه‌های تند جواد نکونام به قلعه‌نویی: فرصت داده شده، حتما یک‌جای کار ایراد دارد!
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/96763" target="_blank">📅 12:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96762">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10e14e005e.mp4?token=ta3aQhYD65fudkycMXb4W4SSKBmyLQdzqEygwzKyUflpWcGK-Rft3XsDrTELAoUtK6r1E_FxlZ6-b6Aiz3uhB5r2GvY7sUKMUsbNTqi8XwFktNhtCr8JpKpI5VkxQgptWZrshDw3apLASAXG1B7lDvgWW0Z6GvGBCLNwaeKW5h-Ykvics7GLeQFut9rBRuQTVXpU-tCpCZ_WfMlxFtoe_yv3mdgaWtG7PX22XeRc8BFno0vcqlGt8fJ4K2AzE3Qo6O-__3PA4JADgIZHhykM3GneAFxjAmf1z3f3gRTmiCC5fAFO9Jki4QIAob4v_-Ye8v5gLorDhbSbGBTzDwWO1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10e14e005e.mp4?token=ta3aQhYD65fudkycMXb4W4SSKBmyLQdzqEygwzKyUflpWcGK-Rft3XsDrTELAoUtK6r1E_FxlZ6-b6Aiz3uhB5r2GvY7sUKMUsbNTqi8XwFktNhtCr8JpKpI5VkxQgptWZrshDw3apLASAXG1B7lDvgWW0Z6GvGBCLNwaeKW5h-Ykvics7GLeQFut9rBRuQTVXpU-tCpCZ_WfMlxFtoe_yv3mdgaWtG7PX22XeRc8BFno0vcqlGt8fJ4K2AzE3Qo6O-__3PA4JADgIZHhykM3GneAFxjAmf1z3f3gRTmiCC5fAFO9Jki4QIAob4v_-Ye8v5gLorDhbSbGBTzDwWO1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
فیروز کریمی: طارمی در‌ جام‌جهانی حتی پخ هم نکرد. طارمی پول بلیت برگشت هواپیما را حساب کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/96762" target="_blank">📅 12:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96761">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fdec54ce.mp4?token=SDPpFyuZRlLUAZkIRa61JDwdl_kx4nNr_fl587uZMMwBSwfpwYyCTeVi3ac-Ir-X4A1I_SprcJkBhJv3ozLL6o2iCaPQ0gE4k1S4hjmd-cRNWtQHjuaP3oEMmwSG7OyAqgZSZGXRMIh1P5-gSxjTrMsxh8rbrbgZ5hSEsaaB4FMfWNqSeHDQD0ELopCtfhNvtnk11l4aYHSJryBYSv5iEzY4LKUZKV3aZwpCY1ODQl8eOvWhrPZ_XjW414RJApUyHS5BmDHcARtupw7KUe-to70XEfgNZgxoyKC658Y2Wn7tXEHMvzfx_sP4JDYtgLB0_QYGn_3vjO0m3nyDp5C4wBCX_X42-UqpNBbd2HEAnbFDi8InfjiCJhILeYRQJYMi_zzWKDkIi9RSXLn7e07vxurReeQsHd5RvCUCDRchkXLz2wm6qJyrs18zQ1MuultC252v6PjBFMpsBlTQ--EWulch2opqWXJVHJ3n6Mn9oWbwClzDrC5Fx-Zd8UvXbZxOUPXpy7xnKVLco74XFQIvoR5vDiHLNbae15-15Bq7ETE9xLCgQkcUQTxobp1uvmk6BOJEkfvnJjISjzKse0dRU2w0iM4Ew1QWBp2Q3EP8veU98vbfV46O_VavTPWHOF-PtZPuUX3gVCHlvmbnZaQL4stkGXsbvoLlGQekBbOYGHE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fdec54ce.mp4?token=SDPpFyuZRlLUAZkIRa61JDwdl_kx4nNr_fl587uZMMwBSwfpwYyCTeVi3ac-Ir-X4A1I_SprcJkBhJv3ozLL6o2iCaPQ0gE4k1S4hjmd-cRNWtQHjuaP3oEMmwSG7OyAqgZSZGXRMIh1P5-gSxjTrMsxh8rbrbgZ5hSEsaaB4FMfWNqSeHDQD0ELopCtfhNvtnk11l4aYHSJryBYSv5iEzY4LKUZKV3aZwpCY1ODQl8eOvWhrPZ_XjW414RJApUyHS5BmDHcARtupw7KUe-to70XEfgNZgxoyKC658Y2Wn7tXEHMvzfx_sP4JDYtgLB0_QYGn_3vjO0m3nyDp5C4wBCX_X42-UqpNBbd2HEAnbFDi8InfjiCJhILeYRQJYMi_zzWKDkIi9RSXLn7e07vxurReeQsHd5RvCUCDRchkXLz2wm6qJyrs18zQ1MuultC252v6PjBFMpsBlTQ--EWulch2opqWXJVHJ3n6Mn9oWbwClzDrC5Fx-Zd8UvXbZxOUPXpy7xnKVLco74XFQIvoR5vDiHLNbae15-15Bq7ETE9xLCgQkcUQTxobp1uvmk6BOJEkfvnJjISjzKse0dRU2w0iM4Ew1QWBp2Q3EP8veU98vbfV46O_VavTPWHOF-PtZPuUX3gVCHlvmbnZaQL4stkGXsbvoLlGQekBbOYGHE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏆
نگاهی متفاوت به یک قانون جنجالی
⁉️
چرا محرم نویدکیا، موافق هایدریشن بریک است؟ مرور مزیت‌ها، و تنها عیب این قانون با سرمربی سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/96761" target="_blank">📅 11:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96760">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38e9d0491.mp4?token=j4r8bSSj2btd0VJaJjPqoeGr6TuKeUCR8q6QkPsrJR9wdMDMo1_UADIvdrgAXO7qeStyWJl4e1kcUzn8XSWW6hvNzz_hO3C9ajRE0CxvCyqz43ryWXGRIapMsfkY22A3CnB7_KuSZttjig4e242nU3MXY2hoPwNp5Win63ihQh9IYidxP763CLVGFuY97ayn5iZOEhioTBL0oKnwljCQiYzWfgLd_ryjhXwKDXJr-mJ_eV7nA-8WsPkYLU88EbE1cY2sgaxCrwcr2a_UQ9p29kQ8Axl7xGas27KylV4cQZxurfdyqUp6AZD3h-w-sAAuSIB-ZeXsazO_W564w1ZD-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38e9d0491.mp4?token=j4r8bSSj2btd0VJaJjPqoeGr6TuKeUCR8q6QkPsrJR9wdMDMo1_UADIvdrgAXO7qeStyWJl4e1kcUzn8XSWW6hvNzz_hO3C9ajRE0CxvCyqz43ryWXGRIapMsfkY22A3CnB7_KuSZttjig4e242nU3MXY2hoPwNp5Win63ihQh9IYidxP763CLVGFuY97ayn5iZOEhioTBL0oKnwljCQiYzWfgLd_ryjhXwKDXJr-mJ_eV7nA-8WsPkYLU88EbE1cY2sgaxCrwcr2a_UQ9p29kQ8Axl7xGas27KylV4cQZxurfdyqUp6AZD3h-w-sAAuSIB-ZeXsazO_W564w1ZD-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میزان سگ‌حشر بودن دخترای مکزیکی پشم‌ریزونه
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/96760" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96759">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
فوری؛ رئیس جمهور پزشکیان: ۶ میلیارد دلار از منابع ایران در قطر آزاد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/96759" target="_blank">📅 11:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96754">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ItQTvOjMaY72hFnp33Uu5i171b_GecWCiC_yWxbvvIKG03rYIl0bwmBhGnbhf6NC6jy_qk1y6D3irt44hcavgGspYAjnbRXAdrNsiNi9tw8uD04tvKFN9Aeq9EvDL8aX_P-w29T68yMigcuBfpgEP3NVqlSxuPA1iWKwF4K2Oju9mwJ_9ktM9ekb8EabNaPUo011qpsvkbluVzYdTd0GiYvRDeWOZyduT5DrTml9CUpXrgQxEZNyvuEhB5CdlgnbrhB6ursfhZ6EXanYsQWTPjB_zhZYjXTZNRmt137mjFFHSfX3wsKTs_cJmTpdVR0daKsFJWFh0DnFMNzxz1RviA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vuVAdiawpJgqJnsuw2DFg9xz7_gkd16Fe441d-kZRaE73B6Ll1Gw2amPmcp4eDAFBCQDiAcnlyDJPUjmPyV7gnwKtNX4mX0M0sgQMpS6B3KWhOHfYyCfsHyjMp3jpeAJuTlSdu8EucH_wfuh-mnOwQp-XAk-BdPz_nTTJMTDchK4KVGrPkPCUtnjNQRTztTX_s2NuAhNVkofhzTSnXKt1tFudUvFEse4LE7N_lkh05wySF5agqBldIA1lERDWArvRngXd3HER34h8vwksRJEbbjjvQnKXPzskO39hlXoEoLYM-FxCBh78KCBVE4SR2IAs1pwT97TOrdbygvfVvYqxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UfFB3CggZKZ6DnLSjDAmwCONi-xKRYJ00T9bHUwrgqiKFev8ERAK4YiYUh6CLbBZ1qgWYmGJ0jU3GrWb106nBWKQih5xSoiHJr-R1N8FzsxWwqbQEpNNM5NrW9r20uVIpBkBJ-deojl_JOzgekgjC589kNWGtYrvmvXbfy_QXYutDZ2MR_ufPV8DbTmL5BHt8siAr6iRhy-KpnsOBjQOFOr1XrflxTTBu2UW5QIaR5rvrpek8ruZuNgUmIQcUqSJRMMU3oKoVJ4zyRl6B2b3miU8WekkKzqpOhmuAiAjm8aJnEqCpxDk5XOJyuWPVBJDkmvn897JJq29N_-35h3f3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZISKfezz-Sfg8MW_ypPXyqj8kflHmlitJuFt_kFJD1ZHBH4-CDgkGpcC_uNrPPHIByEk4G8dHt5s3G7W-D9SpuwPySxAZZduTyOgEtZQmrUFfuEm9NbNoddukI2LTQ4MxSL8QR1t6rxDBkwmJBTERyP9S_4ldUM2UCNHkCERv9DGklcvNw7Vi1Ge8Oel2seJi9D_sOcifqScELhw0bRkC66J69vXBiBOTPa0xaygTONzntSeZT50QxaeLwTivTQ4oJla0eYTE1RGTHa7e_AM48wnEek4oCBfBr8yzRVW1CCeT6-aYSrGLWLjr9aFrB8k6_EF116Zya_bAnZ8-xDn8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CT2c52bCFeKzVBI98FaDrfdLwLkHoHa_OUbY4sryK4swK8QjN5wF8dwHJEQRYKZZnin5Az0Q0lT3OPrYSiIUwj1LXNk25HzWEl2dnE-zh_NzqN2vxupJE7Z6iaBQD9-KbD1PlVMRVsjAaP4l3QMM0I1pdnROfByk0ZvyRZiqRElW0FZSRba0tTTcur_VAeVTzD3cMjGiz2EHl_NWORB6qSoOSLJIwEtgGNA9HJFtxe8k4RMkx82vbudezvEWxAyNuHdZz_jEaIVkCaapQqydWJTYxfqKeP1L6dv5QgARJyfXqM_7MvsshIe3aEc66_BJxdvNXFQIfjfZB799Xx1kYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔥
🇬🇭
همسر جرمی اکاپو بازیکن تیم‌ملی غنا در ورزشگاه بازی با انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/96754" target="_blank">📅 11:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96753">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGpq2gYC1QWkN4No3LWtE52xqrS4fkXpT0jGUpKm-P1mjhsXpBHFr1_opvy8qXqcIISiDFkiI9mNjjieYVYXjEjzjbiMtXkEW_JU8uzYUuZ_XkFAw2SuQlpRAAXcVp_TvddiC1Fa4he3vPMVglF8ADy7fbgKum3MNSag_urbOyfBja4AYCmCBZ3h9oULETUkOrmK38GU1pUrdv4dD3v88XH_lGiRzpvelDBSfkKbkxVrb5Gl96Ic1VBcr_c_JqNOlAq1hZfoOEfOw5LOMwQDug2lPStZY1RwWAMKC6-fmYTGFvLS6k2oSNJV0sf4Xbh23nQDl9BWqYOuiZuQB17eyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسبت‌ها و احتمالات قهرمانی ۱۰ تیم برتر در جام جهانی ۲۰۲۶
📊
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/96753" target="_blank">📅 11:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96752">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpOTD8e8MGlZImfsz3krQm47EpHMVGMD7VWw8Hx_fEeULzICmDznQ8fed66YHljUoJTg9GoRH4bjYxkcDLid00OnCd-OpQSR6LMssGFDaZc16l8dhK5VVi9e8caDX46QEeQDnGNg5F4xDmJMxaxWGZnSEdt22o9VcPC4nh3WkJ219bbGQno9PLYz6tHGWle0RtAEKn-tYxZuw__I2LYtoMz7HS7jECtnAxOtgBWgLeeJEQzMddrtEWOKd-tz81SSzu15V44PJh0uvLi_mluvye5Qvl444JDeBqmRwz8tfsHm6nkEPqNzJ58N4IsuK3S8iv-sQy0vlDdhaXR64KFkuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تنها بازیکنانی که در هر سه بازی مرحله گروهی جام جهانی، عنوان بهترین بازیکن زمین را کسب کرده‌اند:
🇵🇹
کریستیانو رونالدو (۲۰۱۰)
🇦🇷
لیونل مسی (۲۰۱۴)
🇧🇷
وینی جونیور (۲۰۲۶)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/96752" target="_blank">📅 10:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96751">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTAbx_AebxIpH5GsulJ55h6e3Xiod0Z9gkaqK3zS34toTvnJd7P9uUgzFOQ17-w3URZtSfBojPF4iAMIYGHt1JnnWxepygehqajo-4mOD3TSbJx_yNuSPj2qZfrC7bK5j-ZQ7Z35VbEM5bVaPG0uEUz60OhRlM9EbJGART7eRyJHwgT7TiC8qnIJYpbcq5YoWewKyrAYvJI1v20hYkqjxSZ0bqGpmGsNfBkLAYM2-naZzLD05uBldTAKd-yEFVAZsAOWgc2HTVszM0m60YMXPLl7lvkRgXaLNzgoL-nLPbI81XrzX6v7f1bFQE0wQ8VcKsAfduVgU4OkNpTNZ57xrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📊
مقایسه عملکرد کی‌روش در گروه مرگ و قلعه‌نویی در گروه زندگی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/96751" target="_blank">📅 10:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96750">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oe_A0RhFCP_IPiSSUipxgFFy9DgkFWG1ESx2FqG-MNyNSF6gkTwlGjwJME01KjAQNTGDXCdo--f27FeyVg_mOq6JWScvu-BEg6SccgucceNIGwVGX4-QLs3gol3w6nHQ2wcNjui_yHiFldpGt-784jRYsFSmenkkE27tfmb-f_-3aavxuZqaPhpNyYnvT3MOnd7AqDf5hDYdagxDE3I3Dlhq8otadxVMheejXwr7s6eBnnjU5L8Mn6lQ6bU-yBgnb819gRsb34tvV13gG7Qt9zFhkK3eoCG7aH-n7X5rl6IJEhR-hHEM7Oha2s8CIPhl5jpY_YIoFEOkstZEfzjsbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🤯
🤯
پشمامممممممممم
🇪🇸
‼️
رسوایی بزرگی درباره بازیکن اتلتیکو مادرید، متئو روجرری، امروز صبح فاش شد، پس از آنکه زنی پیام‌های خصوصی که او از طریق اینستاگرام برایش فرستاده بود را منتشر کرد.
طبق آنچه منتشر شده، متئو روجری به ازای هر پیام صوتی با محتوای جنسی که برایش می‌فرستاد، ۱۵۰ یورو پرداخت می‌کرد.
او همچنین از او خواسته بود عباراتی را تکرار کند که شامل توهین به مقدسات، عبارات نژادپرستانه و اهانت به خدا بود و نحوه تلفظ آن‌ها را به او آموزش می‌داد، به طوری که می‌گفت:
> «آن را با حرف دال قوی بگو»، «خیلی واضح تلفظ کن»، «اینطوری».
و همچنین از او پرسید:
> «اگر هنگام گوش دادن به ضبط‌های صوتی‌ات خودارضایی کنم، آزارت می‌دهد؟»
روجری پیام صوتی دیگری نیز فرستاد که گفته می‌شود صدای آن نشان می‌دهد او در حال خودارضایی بوده است.
زن افزود که او پیام صوتی دیگری فرستاد و در آن گفت:
> «به من هم بگو که به سیاه‌پوستان توهین می‌کنی و نژادپرست هستی.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/96750" target="_blank">📅 10:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96749">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nT3E3FGr11tCmch_OVg-Xj_4swN15_lPPgUzOTWDdOh843mvI0pwrtjwCNemzB5JDPk9jiMThFxVp2yxPBkvuWK3BnJQb4pd62WjAuX928uuleoXfihHg2IIahLUAiFDChMtzuE_UjDXOBo7x-o1b4qsSHCLGbRMquKW5HKn67YThdLue4BShIu_YX3xnwRr_ecLuRg_rIt49kbdr7qAiKy6WWE9qo4AeA5u0M3_AmX6RY4FchYKrkcnKsN5i2AxRsOy8cXLmlbp2CrFyyOtA9BxSpq4jH7ChxUTpzh40tyylNBzlf72jxboBqdRHJCLkYQO-XM6IzTMKG9oyy96qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
از اسپورت: دیگو سیمئونه از سران اتلتیکومادرید درخواست کرده که خولیان آلوارز را هرچه سریعتر به فروش برسانند. سرمربی تیم معتقد است که این بازیکن بعد از اظهارات اخیرش به تیم پایبند نخواهد بود و مشکل‌ساز خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/96749" target="_blank">📅 10:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96748">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f669d874d.mp4?token=GS63XHeTL16hQIfyMTK54sxgTl8Jg6a5f4aP2PoW1_0OeGhq4OoXTXA0q31fHfPzjmI6VoEJPUAYk_YKQlrjGTx2h7eb95p0ENRaewSGFGXfHp2XrfVIvya53u4z5A1wNPvc9chK7oM8uQKu3kvrsLqGoS8ZbpRSe0CfozOuvFveGXen2GuTjbw0xDtT0W0sZLxV3KtQ4aziGJNN_WctzDxazSYqPAul_227uDs87YZq0sxT7n4RP_rZ7FJ_yNhXQvyx9mlr47xVUX9_3fh1sO_IkUIlJfHufYJW1Ki47lb1-O4x6dCPwS3HPGZIdNwjDJ8wxoBfSQOXvIWHEwvbNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f669d874d.mp4?token=GS63XHeTL16hQIfyMTK54sxgTl8Jg6a5f4aP2PoW1_0OeGhq4OoXTXA0q31fHfPzjmI6VoEJPUAYk_YKQlrjGTx2h7eb95p0ENRaewSGFGXfHp2XrfVIvya53u4z5A1wNPvc9chK7oM8uQKu3kvrsLqGoS8ZbpRSe0CfozOuvFveGXen2GuTjbw0xDtT0W0sZLxV3KtQ4aziGJNN_WctzDxazSYqPAul_227uDs87YZq0sxT7n4RP_rZ7FJ_yNhXQvyx9mlr47xVUX9_3fh1sO_IkUIlJfHufYJW1Ki47lb1-O4x6dCPwS3HPGZIdNwjDJ8wxoBfSQOXvIWHEwvbNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
😁
😁
مصری‌ها سال‌ها میتونن با این شاهکار شجاع خلیل‌زاده میم درست کنن و بخندن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/96748" target="_blank">📅 10:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96747">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🏆
برنامه مسابقات مرحله‌یک‌شانزدهم
🇨🇦
کانادا
😃
-
😏
آفریقای جنوبی
🇿🇦
🇧🇷
برزیل
🆚
ژاپن
🇯🇵
دوشنبه ۸ تیر ساعت ۲۰:۳۰
🇩🇪
آلمان
🆚
پاراگوئه
🇵🇾
سه‌شنبه ۹ تیر ساعت 00:00 بامداد
🇲🇦
مراکش
🆚
هلند
🇳🇱
سه‌شنبه ۹ تیر ساعت 04:30 بامداد
🇳🇴
نروژ
🆚
ساحل‌عاج
🇨🇮
سه‌شنبه ۹ تیر ساعت 20:30…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/96747" target="_blank">📅 10:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96746">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5a653813.mp4?token=USWJ3cdXLBUmvSlpQzRnWODp4EE20NxtNBhqTUlOtQ1Hp67Z1ldUyoRQ1Y5kGRuDl-1x6PhP9nRUomC8qCJX_8hchDdPG_CRkcHzqU4EctVGSkeLg41vrFfQbVS5seFHOydq6PE8NoHDvOMxIAl6X6uv83h51Rfwol47p_V0nbzJHQBTHMAkW5miCoHJOsITLvExSsgLBfnknjViDq9zIHoAKAzGysd2V8HuCbndCljyh1g33rKHiYSpEsrYSk4LhhAlA1NqSPGHDx44nu2CwK3z0mMqKSPnVcTVwsTKfIBhD4n_OJKIPF1nc3ssbKnsOkKrtFF4uqujO6Ot2Y8xBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5a653813.mp4?token=USWJ3cdXLBUmvSlpQzRnWODp4EE20NxtNBhqTUlOtQ1Hp67Z1ldUyoRQ1Y5kGRuDl-1x6PhP9nRUomC8qCJX_8hchDdPG_CRkcHzqU4EctVGSkeLg41vrFfQbVS5seFHOydq6PE8NoHDvOMxIAl6X6uv83h51Rfwol47p_V0nbzJHQBTHMAkW5miCoHJOsITLvExSsgLBfnknjViDq9zIHoAKAzGysd2V8HuCbndCljyh1g33rKHiYSpEsrYSk4LhhAlA1NqSPGHDx44nu2CwK3z0mMqKSPnVcTVwsTKfIBhD4n_OJKIPF1nc3ssbKnsOkKrtFF4uqujO6Ot2Y8xBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤡
🇮🇷
بهترین نسل تاریخ ایران به روایت ویدیو:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/96746" target="_blank">📅 10:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96745">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c6df7bd6.mp4?token=v0X-Umi9KMeStQwNTnVmQpXf6yErscyoYqecoIEzitAE4CIjBdI3bHPeM9hSncXplhe1n0CW2TLw1IS4AP4nmUqnUyq_68Rged4MZwE8qWdfsoNV5lCFJQodue-IPtl3DNvB-ob8bUQp4X200UQtpFvphVkvlqAxoCROqz8mhaJBwpPcCT7ACwa6D9b6gTN8J2ywe9RSHIWB7aBcFF-9M9i-2z2BnjxNDmbMAo8UBJ5axj5SvJg8s68ok0C90zpH4x7PXgoZ3JqVv6K9MQsTUJg0fiTpi29sE91m6owO7IUuRWHinHHmqnwXkGhYuYj3wTNsiHOy8NLNnj8Pxc1I9nZsTCUHIkVnXvcBhHI2ozQ4WgjjHWgl-s_VnscmLc4yy4pu9vRqct6xPBr0CckhSyVze8Bx48OgULLW1WfNcEJn6cVEYzwHNnfvRezSzp6RSgmzpeYE8brXb5UXOasZAMt8pzp1_ZmwfZwxd1qN_lK4XNN_iZY6ATOKz4C0BXfQTB7tEKZSQOKAW7eKMDbvquhEkPCa01wyg6rZbq1ARw15l95vAQq_nD5eLqwLn_tKfazZkQyg0q-LAX6eDJULHxWVtYSfFbNuhXrOl65v1GCHsK5tk0JEoaia3R1jSamel6f4MfO1C-NBN9dLo3ENhRplj7t2CL-ibNcI1pub0vo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c6df7bd6.mp4?token=v0X-Umi9KMeStQwNTnVmQpXf6yErscyoYqecoIEzitAE4CIjBdI3bHPeM9hSncXplhe1n0CW2TLw1IS4AP4nmUqnUyq_68Rged4MZwE8qWdfsoNV5lCFJQodue-IPtl3DNvB-ob8bUQp4X200UQtpFvphVkvlqAxoCROqz8mhaJBwpPcCT7ACwa6D9b6gTN8J2ywe9RSHIWB7aBcFF-9M9i-2z2BnjxNDmbMAo8UBJ5axj5SvJg8s68ok0C90zpH4x7PXgoZ3JqVv6K9MQsTUJg0fiTpi29sE91m6owO7IUuRWHinHHmqnwXkGhYuYj3wTNsiHOy8NLNnj8Pxc1I9nZsTCUHIkVnXvcBhHI2ozQ4WgjjHWgl-s_VnscmLc4yy4pu9vRqct6xPBr0CckhSyVze8Bx48OgULLW1WfNcEJn6cVEYzwHNnfvRezSzp6RSgmzpeYE8brXb5UXOasZAMt8pzp1_ZmwfZwxd1qN_lK4XNN_iZY6ATOKz4C0BXfQTB7tEKZSQOKAW7eKMDbvquhEkPCa01wyg6rZbq1ARw15l95vAQq_nD5eLqwLn_tKfazZkQyg0q-LAX6eDJULHxWVtYSfFbNuhXrOl65v1GCHsK5tk0JEoaia3R1jSamel6f4MfO1C-NBN9dLo3ENhRplj7t2CL-ibNcI1pub0vo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
گنده‌گویی مجدد سجاد غریبی با غول انگلیسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/96745" target="_blank">📅 09:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96744">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cdcdf95c9.mp4?token=fD_yE2D_73WUaFAkZ9TfRS1R_tu6qWODvxK26lnyMyNtwRDhqN4hPR0DieG-3vD6OUWk9RDV5VYtp7DwzZBAHLAG87DJ78F13VyR7T9TY_liBuoaQu4NEfLa7Mtp9tORTtPmsaOOnP8YeLJkqBQEWYrB8l72uJ2Js2yIc1psd3QuRweiiQZG8yqyszpiBaxZXny6oxPK6wkxXqM7Wyxno7ZYlfAVl5J_1fZ0j7QXxB5lQBFPePxIJ3u4jViCRBwZWigGTIkzjpMTVd0ALhW6abbAAhk14ptjoK1pztkEoqKYCW8Za7LdakWxcPhUhAW7wUX8v-5F_7z9weGZT4Gq_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cdcdf95c9.mp4?token=fD_yE2D_73WUaFAkZ9TfRS1R_tu6qWODvxK26lnyMyNtwRDhqN4hPR0DieG-3vD6OUWk9RDV5VYtp7DwzZBAHLAG87DJ78F13VyR7T9TY_liBuoaQu4NEfLa7Mtp9tORTtPmsaOOnP8YeLJkqBQEWYrB8l72uJ2Js2yIc1psd3QuRweiiQZG8yqyszpiBaxZXny6oxPK6wkxXqM7Wyxno7ZYlfAVl5J_1fZ0j7QXxB5lQBFPePxIJ3u4jViCRBwZWigGTIkzjpMTVd0ALhW6abbAAhk14ptjoK1pztkEoqKYCW8Za7LdakWxcPhUhAW7wUX8v-5F_7z9weGZT4Gq_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کواراتسخلیا - بارکولا - دوئه و دمبله کم بود، ناصر قراره این شاهکار (دیومانده) رو هم به خط حمله پاریس اضافه کنه..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/96744" target="_blank">📅 09:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96743">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBEfoO6sRAxs01NS2TuooptHpgwuuYihiIEaFRdhTdEjWmk_X_7mP_btjij5Z5uzYZPZoU8zdey6J3JgvXwYagIagv9i1mqBjHsG17QeMb-PheFbwj6W6ZnlqKt6UHY0n-4sM5Jsa3L98OJ4r83KiHfDOUIhABs39yc9nmlA7kNCmgruG-dOugzwJ0FkvSWbw06g-03Rmh4LC0SzBIdnoBwj_eMNT6q-g1c-fiDrd3okA3AcpwO-1vGuJrKQ1Pfnqpevk_WjwrpfLLkw_skBPGZGee8ZR3xvIJ8-ohj93noNE1kusyI4DUkcNYWtDucdfybEqB1uGKND5DqbOTBq7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
توماس مولر: «در آلمان، ما به سوپر‌استار بودن اعتقاد نداریم. از سنین پایین به ما آموختند که به عنوان یک تیم بازی بازی کنیم، نه اینکه تنهایی بدرخشیم.
🔺
به همین دلیل است که بازیکنان آلمانی زیادی را نمی‌بینید که توپ طلا ببرند، اما می‌توانید ۴ ستاره را روی پیراهن ما ببینید.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/96743" target="_blank">📅 09:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96742">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmqJo32B7CbbwauJKBKr_6xVnjwHbcsK86UCcb8HCRsdHvDCZZHFBqld42MfV5gPKFAO_T343U-9HjaPxAMkIC3hPN1_EDcrLq5hWu0e9vhyeBqagiysNtrJwwDL2hHfURjaEA92fAZnXhY_KsZXkNL3IghAq5SpOOUDAlvnKxRRsPjGgkS9I13Rz0e9qgjbgcDTObNKIVtb34uNowLBtnt5pDB544eh7fVlKZcFdJZCUjNWCJVlm63yv7ALT5xH33qIkoVC9yixumyaiUtAXsV1HjgzUka5VjxyKfO3IUwmB9pC5Q4EzYqNlWtw7IE7F0zvjhYmGT4jLt3UDBHTmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇️
در مسابقه‌ای که هافبک‌هایی مانند:
🔹
ویتینیا: بهترین بازیکن فینال لیگ قهرمانان اروپا و حضور در تیم منتخب فصل چمپیونز‌لیگ
🔹
برونو فرناندز: بهترین بازیکن فصل گذشته پرمیر لیگ
🔹
ژائو نوس: یکی از بهترین هافبک‌های فعلی جهان
‼️
حضور داشتند، بهترین هافبک زمین در بازی کلمبیا مقابل پرتغال، خامس رودریگز ۳۴ ساله بود...
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/96742" target="_blank">📅 08:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96741">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9609549bad.mp4?token=SSF5uWyDlEiARGRupRdN8A4r2r8kPVwynInntKRQvZ5OEtwQ3LdunpWcBZLGdXXsL3iGfnzEYLSe_k3pLPWAGO1v6wo477b3vxKjUzcCOqJkT-j_Q_wUjmIxqCN5kpb0hflvwo0KXlPqEpfHSaLtsUqi0kfHkMQr58pxFKFy4DURxZ05z_w1dAe7Snc6S2tywwcbOMC6y215k7VZw78KShE47x7Df3ii3oR7c6pXbt5Ax2WImKPGZctpUshHmLolaI9h23azEPReOoEvI9ITLZ6wDc703hfNoyM2zTeISycTsz_0A7ZL2_zJMWiKtEZmYxovimi18G4WE-BtwMmF1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9609549bad.mp4?token=SSF5uWyDlEiARGRupRdN8A4r2r8kPVwynInntKRQvZ5OEtwQ3LdunpWcBZLGdXXsL3iGfnzEYLSe_k3pLPWAGO1v6wo477b3vxKjUzcCOqJkT-j_Q_wUjmIxqCN5kpb0hflvwo0KXlPqEpfHSaLtsUqi0kfHkMQr58pxFKFy4DURxZ05z_w1dAe7Snc6S2tywwcbOMC6y215k7VZw78KShE47x7Df3ii3oR7c6pXbt5Ax2WImKPGZctpUshHmLolaI9h23azEPReOoEvI9ITLZ6wDc703hfNoyM2zTeISycTsz_0A7ZL2_zJMWiKtEZmYxovimi18G4WE-BtwMmF1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تناقض‌عجیب صحبت‌های میثاقی راجب شجاع خلیل‌زاده؛ رنگ‌عوض کردن این اراذل خیلی جالبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/96741" target="_blank">📅 04:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96740">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7323fbe34.mp4?token=QrsjJOHYA0353qj0RsqG_FkDJ0vCVaXuLSKTlYDQDEEjOJclQyQ0_6vlJQpe_m1r15JKrUH7A5cTQMwQP4ylKhubkRd6_tqdW7tvjprBjE_uuPjESjtu6mgH6d-5tf7fCRp1rFsf3dcfwB7AJkHG7VG6_VbZo2n5f0CgspOTcww3PmL73Xf82-LNOtF0HxqrQB5WH6RyMeTsCpDoCRQf3lY6UADYwn_2gsrjDDAD2JbbPsq_P2YxNLl7rSje20NNEMywNur7X41pQZrJhkwGIw-EbO3XEgqWqNByAFVbG27p5E1_oAoI4jxTHcPFip2Rs2jnEsOIa2RS5vElXnhJ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7323fbe34.mp4?token=QrsjJOHYA0353qj0RsqG_FkDJ0vCVaXuLSKTlYDQDEEjOJclQyQ0_6vlJQpe_m1r15JKrUH7A5cTQMwQP4ylKhubkRd6_tqdW7tvjprBjE_uuPjESjtu6mgH6d-5tf7fCRp1rFsf3dcfwB7AJkHG7VG6_VbZo2n5f0CgspOTcww3PmL73Xf82-LNOtF0HxqrQB5WH6RyMeTsCpDoCRQf3lY6UADYwn_2gsrjDDAD2JbbPsq_P2YxNLl7rSje20NNEMywNur7X41pQZrJhkwGIw-EbO3XEgqWqNByAFVbG27p5E1_oAoI4jxTHcPFip2Rs2jnEsOIa2RS5vElXnhJ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
عذرخواهی پیروز قربانی از امیر قلعه‌نویی بابت مصاحبه اخیرش بعد بازی با نیوزیلند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/96740" target="_blank">📅 04:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96739">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/96739" target="_blank">📅 04:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96738">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8cda33a18.mp4?token=ET_4pSriVGZ2sVKN_gs-6n-ocany7hnNxovA93XI32bRGKxC9qp26UluWiBg5FzU-b6_MCWsO6GcCMKeW8MUaxpFRTKKj6FFeBnaCnrRPv3YvZyrPJnNbI8OTrb7Qoz3mPpaK5db8fTGiUOy7DUBLL-zGYSJtfgpgA4-dH7XAscEfhDigZK0-SionhsocAXziIaFwoj6KchKfFzC4NsuSFU8tOPhAFneDT1gwpJNtTEd5xDBAx-pgcvrB0hcnS-DpsObjeMfzZoES0dBCbPi1y5-INIUaHr_tlEmTnV8h56uhci1ft6RXugUuhx5njYLzVZLN-FcV4rcFeUT5QCaOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8cda33a18.mp4?token=ET_4pSriVGZ2sVKN_gs-6n-ocany7hnNxovA93XI32bRGKxC9qp26UluWiBg5FzU-b6_MCWsO6GcCMKeW8MUaxpFRTKKj6FFeBnaCnrRPv3YvZyrPJnNbI8OTrb7Qoz3mPpaK5db8fTGiUOy7DUBLL-zGYSJtfgpgA4-dH7XAscEfhDigZK0-SionhsocAXziIaFwoj6KchKfFzC4NsuSFU8tOPhAFneDT1gwpJNtTEd5xDBAx-pgcvrB0hcnS-DpsObjeMfzZoES0dBCbPi1y5-INIUaHr_tlEmTnV8h56uhci1ft6RXugUuhx5njYLzVZLN-FcV4rcFeUT5QCaOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلیل نتایج خوب آرژانتین همین هواداراشونه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/96738" target="_blank">📅 04:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96737">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43e217c61.mp4?token=JH_c6LCn8RhmQcKvgLCN68LYXR175PAVVtCIozG-nJk5N5-lZ9_yne8qtNKxxbuq12CCIJqecsjh_oWYgGsjouxs6lC694PL-V-j11QgIwE6ty1Gb_ie2dxEvi4Z0oAsfi5dc9naObdiXyexi8B8LspS6HAIBFPuwJU01swWn-cjC5h2IrVt0jN3amAxmmlnRAcaQZOIr-jo06Db7oXfHHvd1QSMyizgMmm24VIlyivtAoeYMrfia7q4rPu9hpGXbwC6UaWG15dLdXolQC4_CuLYQiG_ScnNRxSLDrCxshIzn0WtNf5zpkXrcJHYYaM8EmyN1JBHX_bUSla0WBlAoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43e217c61.mp4?token=JH_c6LCn8RhmQcKvgLCN68LYXR175PAVVtCIozG-nJk5N5-lZ9_yne8qtNKxxbuq12CCIJqecsjh_oWYgGsjouxs6lC694PL-V-j11QgIwE6ty1Gb_ie2dxEvi4Z0oAsfi5dc9naObdiXyexi8B8LspS6HAIBFPuwJU01swWn-cjC5h2IrVt0jN3amAxmmlnRAcaQZOIr-jo06Db7oXfHHvd1QSMyizgMmm24VIlyivtAoeYMrfia7q4rPu9hpGXbwC6UaWG15dLdXolQC4_CuLYQiG_ScnNRxSLDrCxshIzn0WtNf5zpkXrcJHYYaM8EmyN1JBHX_bUSla0WBlAoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
12 سال پیش تو همچین روزی، خامس این شاهکار هنری رو مقابل اروگوئه خلق کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/96737" target="_blank">📅 03:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96736">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CW5Yrjx-84-X0BOsBrQKmKfItMmS5FpD10Quvm2i4k5LGIUSxBpcoo3G2y66ej43PCBGwgwtGGX83AkJzi3dosvC0tl349nzMXaQqqy6AspPCG7KPr4dJ_cKYtnLTp6wjKds6erTm1MgaO1mpbVq-BU1m-1b0vVNhr2f0vV0_o-xZWjWutc9xLkJt__Z50W5bEG5RNOIInK6LvXre-P_9qE9aKCag_ZgT9V55NyNC-S1VkjAgkALJ544JFxEq3cgGdQQ8_uTjzB4AeDnTVDAEA30i7K91L6UYtB1ZM8LjPibUphr5L33HbJMZ4fOJ7raiAHssVKs1PqJpOiF2oO_Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔵
#فوریییییی
از کریگ هوپ:
🔺
بارسلونا در حال بررسی امکان جذب هری کین از بایرن مونیخه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/96736" target="_blank">📅 02:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96735">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb77bafea0.mp4?token=gzCKU20zWBZdZ49HvPx7SVHJuWkuJvVsewUppgTOwT7z9Nzi1Ctu529570ERVtGUTSdr4ME7K2zxaTHJoRNB828wbVPKFb8KTJcZGEP1vSb2qiPmie_KuA15o3qFS_kihQHDeNVOT7_kdqRmt-SlqMsyvebaokQc4FGy1X1F4h3MofF9QftU53ie7hGSQzKIQg4QukLwq1Ke_eZyG3EO_4Yd_KROFoRjTNJv3ssiXJMcqjdpnC9qCKbagEwoHoVjiNVDwVIIg-am92OZnZ1YPgHgv9p6LbGwuKNT9YUDqnrpKJfI2WuqztCIqbOyCCrfmvT7l63WjKQt6kxYqHCyoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb77bafea0.mp4?token=gzCKU20zWBZdZ49HvPx7SVHJuWkuJvVsewUppgTOwT7z9Nzi1Ctu529570ERVtGUTSdr4ME7K2zxaTHJoRNB828wbVPKFb8KTJcZGEP1vSb2qiPmie_KuA15o3qFS_kihQHDeNVOT7_kdqRmt-SlqMsyvebaokQc4FGy1X1F4h3MofF9QftU53ie7hGSQzKIQg4QukLwq1Ke_eZyG3EO_4Yd_KROFoRjTNJv3ssiXJMcqjdpnC9qCKbagEwoHoVjiNVDwVIIg-am92OZnZ1YPgHgv9p6LbGwuKNT9YUDqnrpKJfI2WuqztCIqbOyCCrfmvT7l63WjKQt6kxYqHCyoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇵🇹
تو حاشیه جام‌جهانی یه خبرنگار میخواست با ژائو نوس مصاحبه بگیره که ستاره پرتغال با دادن به تیکه پیتزا به خبرنگار، سرگرمش کرد و تا از مصاحبه فرار کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/96735" target="_blank">📅 02:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96734">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fee527586.mp4?token=iufZ0nyrgO3ZhTgPd64PQYn_yM9qZJUm42V6YvESwNCxpMJduAgoywzB6hhwR7nkbMASeNu2YQfEJkE7x89Xa8FHxmelyCN8QAg8-EJ227KiGhSU-iBB7ShCXOBeZau8KyRpRXDBiohDkbo6yvAbKJkUS5FgqKAM1KYjW7I4QGlK7ulsZ4PKN7P0BxeZBPZ0vo5Zi__ekvf-_qxgo0u-98RFFsfRVanVtwdoggz0o1guH5JXzHFm8DcgH-atHLBFv0KolBdvx5E5fiOXc_YEL3Ykt3qgB0I3i53Y0WGFqIHROdKZ39zfTbieHqXQzaHdvBgXyjlIAy4BTZkzZa28GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fee527586.mp4?token=iufZ0nyrgO3ZhTgPd64PQYn_yM9qZJUm42V6YvESwNCxpMJduAgoywzB6hhwR7nkbMASeNu2YQfEJkE7x89Xa8FHxmelyCN8QAg8-EJ227KiGhSU-iBB7ShCXOBeZau8KyRpRXDBiohDkbo6yvAbKJkUS5FgqKAM1KYjW7I4QGlK7ulsZ4PKN7P0BxeZBPZ0vo5Zi__ekvf-_qxgo0u-98RFFsfRVanVtwdoggz0o1guH5JXzHFm8DcgH-atHLBFv0KolBdvx5E5fiOXc_YEL3Ykt3qgB0I3i53Y0WGFqIHROdKZ39zfTbieHqXQzaHdvBgXyjlIAy4BTZkzZa28GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توصیه رونالدو به رودریگو: «باید صبور باشی، همه چیز خوب پیش میره...»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/96734" target="_blank">📅 02:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96733">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hy0rwRYH3YbZjqOt5zpnhZ00iaf9ooIVRk0QFUG8_C7jDL26OuJJw0hMx0FJ6NnpmLf2B5Nw5DachxhxJ1s-_RE_r0jtSnTw25Nn02KgZwigQMoGINbryFRFvNTYofPSZ-efHlu15yvY4DaPLbUShZEmF3vkLsL27yda_D-b8eboXA7RrwFBFfAujS79M-1DHg0RR5yvbj0Je6SmczeC83zHbDETO11Llit90-5BUaFIPwbGLWLVFW2656vnanrgMhYERjYEC5_i-mOn_JdzAQLTITgmXNjxsV3Ne6XXQwbjMTCBdUyIt44FK8tLF5U_HdsDQgT7VtFiyEG1iykhjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند و ترویس اسکات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/96733" target="_blank">📅 02:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96732">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RW_XS3_W-Y0cYB5RBgVCbg-aiFdj_tSb2r6C_8MRPF8XHcSXVucolhTMtv7nODtDWkb7Sc9ClcDPX6EqvIpwGH-P9W6lOJ0LlS3C6KuT4w4j4JvD5FT2oNUDMIzDeoIMX2tjPvMnh_GqWJ7e3_ALvhreaSzZkfCrnOPidgOo8FVEcQrGItysfQSNXKJ3xLdU6s9R8yUvhfBhlmWBK-JRdq6dWOSHC9mr8zt3i-fpViF0mJvEwizoDNq-gC16v_YnC-nWXHy3_pzIDXM3TUm7wiYQNg8AYN9D7loqP8kugTMo6Yg6sV-rCTEesuxAqeFI9MO8KcVlkOnhNdRe3QfBVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریک 230 هزار دلار رو صعود کانادا سود کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/96732" target="_blank">📅 02:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96730">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G27n7M0AXmSBtJd02KT6MnURwwzfAvrxhGL_Dm0ywQDZP8Hehk-q00rUaOGOc3Z1h8pcbovzef_QwK_Ve9_lvVnqctpUJa2c-k9zM38kgfhQNyvYStBztYjHuy7IMzeZm2YxpDhCUtT_IHJz_bdne4D0KvVDr4ziG819uwneOqASX9hzgkitGCIGgMcbVQFX0E70a8v3BwvX9sXAWG2Of8k6-9zd9LLZOlbOldwlwJ25LwyA8AEuirbu7mkP3ceNksr1s_LrbUBpsZCNTFFtMwoNtCDauh5HGp_SI07UrYwYy7Z9NymSq2MbsJ5XD9PYM9CcI9FHCztcMVufi_WiTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/96730" target="_blank">📅 02:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96729">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gn4BXUfYL3jIdhjIXYWgt8I2GkydhLXTy7A7FJegRC1HYxMV5qB5HS2cyvaoOTVMPMcSTvQOE1zpFvkbTCzFJtdZYR34FiAj1UF_5gAx9OU2PwbQR4kNNlat7PxiCVIEmYLrjn85T-pN1fYga_SxbIKZhgzR72cS7O_HKZyU2_SOdR9OITyrwujEnaddgMdtIiQdLW9jitB4UUtvEoo7wrv_BOzahM83rnFH9SHG4FHlNDUYz5XpOsvQhdrETClWXYXgpg3eF59Q9egEACk3gWgV1uPsj-C3VCC_xuPXJG0uhBnMF4t_oP67NnBA8lwkzXlM1Tb7Jv7vrQ-eYl8-4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
ماتئو مورتو:
بارسلونا قصد دارد با بردلی بارکولا مذاکره کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/96729" target="_blank">📅 02:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96728">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l6HgFqmCRkBOadb8-fGuBqMKFnPGKCf_Fktd5q8pynXSpV3wQowwZD5q6YoPv6x1kHIGSmpYLUo2mHCkOWvNLgGHiD9_T0cRB3PCVfvCfJPmM--FYZ7lwwLhQdh_oq9NRCsaJr5saRWcZNvBQiMb6hOfjt9GgO0A9f7xm9vWGJqAfo2BKV5jgd_WbFK8xuQseLdw2mZonWK2J-ElQMyLGDVAPSJwyJjRV7dEljtktLgd5D1P_Mx3MqmLZ-y5m98pskVkcCz_fNQ2uRSAz6OwjzMk13iJCiuG5WtmqEvmS40qJtMgxXYIC-m62kfUNC1iOcwE-WMYFaWC0b4jeDgWYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇯🇵
موریاسو سرمربی ژاپن:
ما می‌خواهیم برزیل را حذف کنیم، توانایی رسیدن به آن را داریم و فلسفه بازی‌مان را تغییر نمی‌دهم، اما برای این دیدار برنامه خاصی دارم و برزیل را به چالش خواهیم کشید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/96728" target="_blank">📅 01:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96727">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlxnDliLTXlkRsFVc6uRgYNRkT_JHzEgOizrioQlm8ztOwpOchBnKFzVYjuOBTg9Z5gCyPNIesIGd9FTIG8DIXrO_IEB3cLGJElG8Z8m4lE05mbGW7bjKh6U_wR6abjiISVtAAsH_u1oNFCItLDM8bKk6GqCAUB93_O_88cjUCIhyIMaWIjE31cDyqOrukh1u4odV3IKl9sXeF7a-4tPjSgbwtaf15LS_NJkfjyqg1Za4XYSR0Rup1RvmYlSYd2-vgDZYV7ErEIuEGmKjedqSmC5JFIiJ8CIhtgkyqhZ1QYAuboX1LhoBz4j-2ilFnJ5hmkhY4FX3u0waH8JyKIo7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو
: پاریسن ژرمن در تابستان امسال روی جدایی سه بازیکن حساب میکند، معاملاتی که تقریباً یک معامله تمام شده به حساب می آیند.
گونزالو راموس به میلان با 74 میلیون یورو
کانگ این لی در حال مذاکره پیشرفته با اتلتیکو مادرید است.
کولو موانی با یوونتوس به توافق رسیده است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/96727" target="_blank">📅 01:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96726">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bf096ac36.mp4?token=Og6f5K5yp5cv0v1EA5leCgaGgqoI36VOJl9hDHj2W0NywHoNACrpGulEhk_C6CV3NMLHpzVsgpebIJhYO0McESJjvmfx6uuuXkoMqLQqn0Zm4erDhLUf0DyeLXCfV2qs0M9m4dAXGliN7hTlPzvOGFx6jpJdo2GOdcVVo4tUG-zGnOjrai5lvRFTgk5TqUiCq_L24MyFHV_S-brzHFzo0a_6ZqYvez4H89RaKouViKRI9WuWZ8HvLzOug1NMcs-5YlyqoigIjBmgPwXQnltJxXI50kY6oAwLa8p4eDWO0YEnKC2VsvhDDphSOXeNi1Cuvn1pBmEKIRc0qR7CJn0YBmZ-qC65oq4C8x7WABqAmkbahRmfMi-5QVytDxIC2LNqbmSiLeHgCUYys3eeiHECDkcq75WHKUUytQZVei0_CNXQqUCR1ETbs0Z_osm7u9zG532NHC_0WfkRMa36w4SUavvUdumaiXzL9rV1L762t18ygNK9qiXHLINtsElAIiYXO6aeZJfnwDKgpvDnH_agybQArZz0c2wucRDmKM93BnRJDBtWxJeLUHC2vK1q-2lfrrX9KDsCANy-_25klKsCmtKmghSPS0c8on6vvVcR482BjBM7Kv30ILFnRcVqzRSNdrfg2oTw9ro4GUfHHE2pD1Gf6VNgNnrdXCPmVMtgfmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bf096ac36.mp4?token=Og6f5K5yp5cv0v1EA5leCgaGgqoI36VOJl9hDHj2W0NywHoNACrpGulEhk_C6CV3NMLHpzVsgpebIJhYO0McESJjvmfx6uuuXkoMqLQqn0Zm4erDhLUf0DyeLXCfV2qs0M9m4dAXGliN7hTlPzvOGFx6jpJdo2GOdcVVo4tUG-zGnOjrai5lvRFTgk5TqUiCq_L24MyFHV_S-brzHFzo0a_6ZqYvez4H89RaKouViKRI9WuWZ8HvLzOug1NMcs-5YlyqoigIjBmgPwXQnltJxXI50kY6oAwLa8p4eDWO0YEnKC2VsvhDDphSOXeNi1Cuvn1pBmEKIRc0qR7CJn0YBmZ-qC65oq4C8x7WABqAmkbahRmfMi-5QVytDxIC2LNqbmSiLeHgCUYys3eeiHECDkcq75WHKUUytQZVei0_CNXQqUCR1ETbs0Z_osm7u9zG532NHC_0WfkRMa36w4SUavvUdumaiXzL9rV1L762t18ygNK9qiXHLINtsElAIiYXO6aeZJfnwDKgpvDnH_agybQArZz0c2wucRDmKM93BnRJDBtWxJeLUHC2vK1q-2lfrrX9KDsCANy-_25klKsCmtKmghSPS0c8on6vvVcR482BjBM7Kv30ILFnRcVqzRSNdrfg2oTw9ro4GUfHHE2pD1Gf6VNgNnrdXCPmVMtgfmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😁
😁
صحبت‌های ابوطالب‌حسینی درباره شاهکار دیشب جمشید خیابانی به زبان عربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/Futball180TV/96726" target="_blank">📅 01:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96725">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Za9Hx7S-5LH12RbYKDhkTAKIKsib0RX4F6hL6KHj7D8EBWSRAmIrwzL8G5ERMyenom9nbfQV3wHakzTvjwBZ5V74wTrAMUVEOPspEb-Nykp426EGYSEBPUfztUwa_qlCXFZwTcdbJSBtLUaBbATaQIRiNjDbq7ucpqRcO_Z71ErpmGV3k7pepSkitFs7T6pUuBmfgb9eH5J-6idUd0z0TYBybLjmXko0OQDNjJtCG0BeeNiANT1UoHnmmNyvOSII6MCgbIVvT179W07jQ-lVfcUhdWtuZtJ2CkU6YOxS_YuOkGYDfc_XFgYLy7RoYLPfnwambD7KmJT2wFaJawtjiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🇨🇦
کانادا در جام جهانی ۲۰۲۶:
🤝
تساوی مقابل بوسنی و هرزگوین
✅
پیروزی مقابل قطر
❌
شکست مقابل سوئیس
✅
پیروزی مقابل آفریقای جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/Futball180TV/96725" target="_blank">📅 00:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96724">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pV8TqLN80ak8f88710wnlT6wifb4nNQ6z0uPyQhyYHGWkunP5M0bb2KkNQQyeQf6WP4I1NBG8O4XIAhqI3RBa8ehBuJU3DwisU6mjsYeRxDYK5MH0j-Mdzbw9oUlEd8EchQGpxTMPTI8UyDW6l6y8YwpNlk-Vfbqz8hRy0WwzC4ou4FVLijRQI-INmLxq3GNGoGzPROqnoGSbSmvs1JvAsEU42fjFIFUUMT8e4u9_0tw3czk_EjFSPIhAJtkj8i0yw7YKL0elNRnKt8ZPmRRnXJ8-q4KCx7PNt4zSKHYvjRGYzH7DPrAb4HbH224Nhr8wgShq2jWrCH0YVeqlnpF2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇦
جام جهانی تاریخی برای کانادا:
✔️
اولین امتیاز در جام جهانی
✔️
اولین پیروزی در جام جهانی
✔️
عبور از مرحله گروهی برای اولین بار
✔️
اولین صعود به مرحله یک‌هشتم نهایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/96724" target="_blank">📅 00:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96723">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2ocqmf2n_cOYzdd9puWFdb01FhUXckSis47k3Pd2i-3b2fz7l3jLccsN_Q-bhumevWSvrwtAJWu06U0hm1R8tvzNxs_hzjYx8IXaoVK2xE3U9RFB98lJpDII-rPFhit3v9dF6oYAIju-m1Gqn2Py1Iq1bOUPC5y2JjODE2akyi_6LtN9k2Rzp9TM_fiiOKBjXDSynyqNbq83JQF729wzhZPx8et6TAEQA7J4MKC4lfDWML_ZjHdp_MOB-mCfLn5emocYM9LmoOmCqCt2U_FMq11O7rCFAHsufruMvESkeJdLrWMX3p8r4FeERnCFxPg-InPAKSQ7rNNLhTW27IFMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
بازیکنانی که در وقت‌های تلف شده نیمه دوم گل زدند تا از رفتن به وقت‌های اضافه در یک بازی حذفی در تاریخ جام جهانی جلوگیری کنند:
‏
🇳🇱
ادگار داویدز (۱۹۹۸ مقابل یوگسلاوی).
‏
🇮🇹
فرانچسکو توتی (۲۰۰۶ مقابل استرالیا).
‏
🇳🇱
کلاس یان هانتلار (۲۰۱۴ مقابل مکزیک).
‏
🇧🇪
ناصر الشاذلی (۲۰۱۸ مقابل ژاپن).
🇨🇦
استفن (۲۰۲۶ مقابل آفریقای جنوبی)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/96723" target="_blank">📅 00:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96722">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opL2BSqtXzH-zpOFOQ9D6eEKzA-kmvrCsxQ33A5q9Rbn4YhcLnoK1Wx2wef1UQFdT0RCvd3d-ClmXSjQMDzhBgQOR-jTslI-eQvfT6FgZKzi_D1tKwEgw95IMmC7i_Tp1YbG3ix7jzYyKtALI7Sr46fY1BenJBSU7IXA54_gMTMh-gg-wOngG-r2w-CxFk8716zFzyrLxO3sGajyI-WVkyTri6v6hV-Ta_EkO6BXoVs13QHdSPJBdfAQRO1aMZwG48sDTUbYw8yZ9dHp4xptgVeiV45afG7XXo3oiI1bJWk946bQB-y8remUzyAN82PkvD9Sqm6XjbM-eBdSWvTYYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
#فکت
؛ تیم‌های آفریقایی در تاریخ جام جهانی ۱۴ بازی از ۱۹ بازی مراحل حذفی را باخته‌اند. ⁦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/96722" target="_blank">📅 00:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96721">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COPHEGiOUpypqKrt1ltmR_ybtCqeO3Ix4y9oDGukklfKqkKc9JK36wco9ZCJ9bbum28-Oy-gx81s-RStGOVb71Q7S7w6T3uY7uRc8wYzlGF9PAlaeunw5Hg2DIYvW73iuTXrR65WgRnUbjCW3loc7DXPs8_NN_GqP-e5eDrTnFe-OxVVqAQ9q6akpa5hUBFnBaH_TyPLPb7-mgToV9UeGgSgCSPm917DPPgKgOrX9uA07QjOf_qHtoaESkHgS7GUE0-kFcNgSff_8mG2nJI7mi-3KOSVQgEj7N_0JZ1JI-rQumVXt8tw8h0c8PJZOxwF0uYd6LCZbGO7eYXG0dtSww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇦
📊
🇿🇦
آمار نهایی بازی کانادا و آفریقای جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/96721" target="_blank">📅 00:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96720">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-4MTrNP-JEHlaVpBYQWo23XImgIvihB4azvidCXf1QsRzgzHNAxK3laPerJNBzoEuj9ppVl8xilRk2Yxn6bH5Azyrtlcn_DggEsI-8jHzOH1nhLjTrfPH1McCRMXdBvoigY74KuobbwC9J0wepqvn5t2ePk_m0LmnXGWBuisALh9KlLFtT-u8TKB8hJEr5ZtXen9hXGzFCkABssEJzcXplM8cM_B4-pl5GDYmRBoQB9eWhbg0pP2pjOWmsygBKLId3v2CN0Agd7O0gejdIpGTjcEJYEib4jNBeip--MYIAIJ29u_06kf6AYzB-GXIfAWKhKJuP-8PLiIP4hxbTXQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کانادا در مرحله بعد با برنده دیدار مراکش - هلند بازی خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/96720" target="_blank">📅 00:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96719">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🏆
پایان‌بازی مرحله‌یک‌شانزدهم‌نهایی؛ اولین صعود کننده به جمع ۱۶ تیم برتر مشخص شد؛ میزبان مسابقات مقابل تیم چغر و سخت آفریقایی جان سالم به در برد
🇨🇦
کانادا
😃
😏
آفریقای‌جنوبی
🇿🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/96719" target="_blank">📅 00:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96718">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vy-1XWQrBo6Uj5hrOBXd7FmTEw07izeZ4bPPhEZtRrjXe1yXYQu6iZ6teVbUks7-BeJuyo6dKH6UzqLPhZGK3uxaoe9lL0gePCwQGtu8hP4O-PmfQx5VDKI-q5dbPN6mtBnLGlfm3bVrTEjrGV91aY2rC-C7Sc8w90CDcjVF-D7VlUK-o3GHTvrifCimeHxw2738uc_GctaQjIybrqYwPjjHZOAqs04ISUdW8ibBGz6tW-UFmFdFN-MkFLSH-MKcQSTPy8Mr8rTNVzYg5G84TqafU9-_JSwhx4aqZpMQEfC9ZQv3ChLsjKvab7m6Q6gXQMGBoTfXwcrjBjek-leHSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇦
گل‌اول کانادا به آفریقای جنوبی توسط استفن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/96718" target="_blank">📅 00:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96717">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a1d55eec6.mp4?token=SeaGHnQDf6J6Y_n3qzlvxoceQDb5-7diFnympcrgLkYh-GTt3KHk38dyWHkoypVM68SOoIFlRnkMNZ0QckSBjpCv0z-Em76_aY9u5nbkH42z6B8ZzJidW6NsAqb6bVMTfs_1Oo-kab_LXtIny1EuqcpXbZIdZtgw8gYz_SKuJJgA5Hobg2tRBhtvvwHmVK2jCfyh8ULBQbg9bLKsYSrkeKaIuhDcUOnR7fdcOKO2OVkPJRCzricHqeOtfVoSv_v02MS2S3kh2HLPhOJpdwbb74y7l2Cjh_a1VQ1x4I_lJ2xY577UfgeX3Dd9dyhbJJB-W5EVeysSI7411ShYPDr_PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a1d55eec6.mp4?token=SeaGHnQDf6J6Y_n3qzlvxoceQDb5-7diFnympcrgLkYh-GTt3KHk38dyWHkoypVM68SOoIFlRnkMNZ0QckSBjpCv0z-Em76_aY9u5nbkH42z6B8ZzJidW6NsAqb6bVMTfs_1Oo-kab_LXtIny1EuqcpXbZIdZtgw8gYz_SKuJJgA5Hobg2tRBhtvvwHmVK2jCfyh8ULBQbg9bLKsYSrkeKaIuhDcUOnR7fdcOKO2OVkPJRCzricHqeOtfVoSv_v02MS2S3kh2HLPhOJpdwbb74y7l2Cjh_a1VQ1x4I_lJ2xY577UfgeX3Dd9dyhbJJB-W5EVeysSI7411ShYPDr_PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
گل‌اول کانادا به آفریقای جنوبی توسط استفن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/96717" target="_blank">📅 00:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96716">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">چه دقیقه ایییییی</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/96716" target="_blank">📅 00:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96715">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گللللل کانادااا زدددد</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/96715" target="_blank">📅 00:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96714">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad99d57cb.mp4?token=ojfUrZQnKa_5BALu_o_C2ocWLiDNqtixwdb_cYqxHy-ALyS0fsEPv39Eae0vx4sUy1O6xW4rnaHXe9XJ0qjy7_YAmFQdes62yO5DUzTEmH4fBHsBNzA-CZkLI7p02iGTcTR8SajGjcOD-5FzBLAQInVf0dCTgsAORfJLStWoMftXpYIHASXfeYK8_qqu0fBay6Z0ChZeQkVUApP8zEERKi2q3FegwekIImZZEFF6LQkqER1H-TC-4Xg5OVx37WX0hAdtvv8cJ4YQuYr-1OUT77YXdcOFWhSKJ5EkC4F_1DTEjy83nLy66uJP3pWKqL6jE-bz7H5nr0IihRQgGNhEWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad99d57cb.mp4?token=ojfUrZQnKa_5BALu_o_C2ocWLiDNqtixwdb_cYqxHy-ALyS0fsEPv39Eae0vx4sUy1O6xW4rnaHXe9XJ0qjy7_YAmFQdes62yO5DUzTEmH4fBHsBNzA-CZkLI7p02iGTcTR8SajGjcOD-5FzBLAQInVf0dCTgsAORfJLStWoMftXpYIHASXfeYK8_qqu0fBay6Z0ChZeQkVUApP8zEERKi2q3FegwekIImZZEFF6LQkqER1H-TC-4Xg5OVx37WX0hAdtvv8cJ4YQuYr-1OUT77YXdcOFWhSKJ5EkC4F_1DTEjy83nLy66uJP3pWKqL6jE-bz7H5nr0IihRQgGNhEWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
توهین ناموسی و بیشرمانه میثاقی به مردم ایران: کسایی که شادی شجاع خلیل‌زاده رو مسخره میکنن، میرن تو دسته همون جاخالیایی قرار میگیرن که قبلا صحبتشو کرده بودم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/96714" target="_blank">📅 00:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96713">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iS8ZjmODixtauErbv1mtAxK31Ek9_wsHte3DsTLYEthZgAkKkYYYX3UCNNTEKkZwieLu_0YIu0YGrezhu298Sfi_RcnRRiHt0zFRY5HHie9Tea1fx0yDWgSScyi2f6vwnOy6lWd-c3TtJ1G_WVPYVqzOm2D7mmxNEp91Eo9AJIODOuR0lwhAV30iZHGMMqv-_k_d36ORHOi-Ls9fC9lNKffPX2pCF1Fvzc8NHVufqIMudeXZw3GJlb56KDvCXtUWyVRv6z6btPGc3tWNFDs3FV0Rqd6qykZ0BKyPxMAKK418v-RTTNeAQzNQvIVOJ2P_7h578v8uQ6Il_q2HzPoltQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عثمان دمبله میتونه اولین فوتبالیستی بشه که تمام این جام ها رو تو یک سال فتح میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/96713" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96712">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/126ee96f6b.mp4?token=n0Q-WEYwStSVA2y7cU_YuCe4HEFjd401EQ07d3wHg7b2saDOkO7tBmDgknhZY9YZIrCdoFluZw50bYO6kwb_dZCDB9LTyyr_Afn8rsa_O1rDLcagVEzpc844FxuH8AI1GN4bCfqfBlC59RgnPbRXKHnzCe8OeqU9OM6VFyzxGeiDZqMFlLhb5lMNjG6jAo8vdE0CltoGp1l_kKSIYYNNp6DWKPzoOiT0cEOh0YTg0gqDdZ3jTNRIH6I93EkkrGKoQiZlfyrCGLpR-9W86yjINyE5Ly7q9Rx14tUnxdXlgWjMM0vOZ4w2WnT1hJ2En7K7hYOuxuGHq42bF0LpYbuZ9As4y1vnYke2Ve8dkM692butqOleV6f3ZBXsa3LLHVs-jEfT8cCtlJ4J3q-h0WI7MMwuWZZXdJRA-X8Zv_8dMv3xQtW7yVJamqp2ksUVEQSM_6JFRk9MebCfF7mUj_3TA75_-fjjH4zdfo8JhJDZIqxLlaxEys0JadBfc7JfGvWbpYhPiKN_ehiz-zAustJToSzsb7Rtv4onLcSvXLeGsO5bDvAVOIiwvqFC49naY361NuE2Yaq_R1i8D63_iBOybgmTFWnyRpbnkk3HQRQ-PNv7CJZgUfWAkHZD1DeVyhu9zmCRGf51RdxnQBoXEoKD_TxQ7WQXZLkAi257yYznhEY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126ee96f6b.mp4?token=n0Q-WEYwStSVA2y7cU_YuCe4HEFjd401EQ07d3wHg7b2saDOkO7tBmDgknhZY9YZIrCdoFluZw50bYO6kwb_dZCDB9LTyyr_Afn8rsa_O1rDLcagVEzpc844FxuH8AI1GN4bCfqfBlC59RgnPbRXKHnzCe8OeqU9OM6VFyzxGeiDZqMFlLhb5lMNjG6jAo8vdE0CltoGp1l_kKSIYYNNp6DWKPzoOiT0cEOh0YTg0gqDdZ3jTNRIH6I93EkkrGKoQiZlfyrCGLpR-9W86yjINyE5Ly7q9Rx14tUnxdXlgWjMM0vOZ4w2WnT1hJ2En7K7hYOuxuGHq42bF0LpYbuZ9As4y1vnYke2Ve8dkM692butqOleV6f3ZBXsa3LLHVs-jEfT8cCtlJ4J3q-h0WI7MMwuWZZXdJRA-X8Zv_8dMv3xQtW7yVJamqp2ksUVEQSM_6JFRk9MebCfF7mUj_3TA75_-fjjH4zdfo8JhJDZIqxLlaxEys0JadBfc7JfGvWbpYhPiKN_ehiz-zAustJToSzsb7Rtv4onLcSvXLeGsO5bDvAVOIiwvqFC49naY361NuE2Yaq_R1i8D63_iBOybgmTFWnyRpbnkk3HQRQ-PNv7CJZgUfWAkHZD1DeVyhu9zmCRGf51RdxnQBoXEoKD_TxQ7WQXZLkAi257yYznhEY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
‼️
کنایه‌های طولانی عادل فردوسی‌پور به حذف تیم‌ملی ایران از جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/96712" target="_blank">📅 00:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96711">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🔵
فوری - فابریس هاوکینز: پاری سن ژرمن به توافقی با یان دیومانده برای قراردادی پنج ساله دست یافت! اکنون مذاکرات با لایپزیگ برای تکمیل این معامله در جریان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/96711" target="_blank">📅 23:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96710">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پشماااااام چییییی گل نشدددد</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/Futball180TV/96710" target="_blank">📅 23:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96709">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9ef2aada9.mp4?token=OIK4kbPucJZGYQIjYWYUrcZHT5Uk0IfPZHZGA8Kmk9T0HTYdjNWscQ5yELgvcu8TVBwAyERvzST3bIChrikZiJL-xaF_iI9rSndmiTJunqbvSdr2HofrmmyGHdQTgvlLeNXjlDZQDF5SHxzko4hH4y9d_du-UnUBm0qRu6rgfWsRqtIye83iNQat1C5ajHBaujw3hIcGw6RIyLJUu6VmGhaL-x3CLi1iDexZ9sPzLWCV2b53WglJTPt4AEOJYctPftZoW7aBnkgf2wegZb-dgXSAenWCLFwa3S1pMBN4FzKnS8uwblctKo_NTEqExDP9sZ7Psxooj8cPyl8ilLMjtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9ef2aada9.mp4?token=OIK4kbPucJZGYQIjYWYUrcZHT5Uk0IfPZHZGA8Kmk9T0HTYdjNWscQ5yELgvcu8TVBwAyERvzST3bIChrikZiJL-xaF_iI9rSndmiTJunqbvSdr2HofrmmyGHdQTgvlLeNXjlDZQDF5SHxzko4hH4y9d_du-UnUBm0qRu6rgfWsRqtIye83iNQat1C5ajHBaujw3hIcGw6RIyLJUu6VmGhaL-x3CLi1iDexZ9sPzLWCV2b53WglJTPt4AEOJYctPftZoW7aBnkgf2wegZb-dgXSAenWCLFwa3S1pMBN4FzKnS8uwblctKo_NTEqExDP9sZ7Psxooj8cPyl8ilLMjtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاره شدم
😂
لاشی بازیای اسپید لای فنای غنا
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/Futball180TV/96709" target="_blank">📅 23:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96708">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3kTYAnifUmXLF2PUZxHeajTwq89qNyp-TVxuxis4_heDT8VmYYqycUj4nFkE1JLFo8Yubt75-cq54w00S2CFvf05FxTTtdD3oaGNg4cJgt-oOmVEse_lIu1deh8tHxVOmKRM3rDoXBLYFq3sBDHJChlmAXENRyYRjx0WowsTcnd_ujAdVeb46ljIQD1ja8bQqtEsVTCKS5uPtFETLgq4LJ1n8q1X6WEfo2AwU821pmKjhGkSse0Nl3D-NYe1GRjZJca6Bu37-yBqqVs0losfKcyB1Wt6jeQ30mXEcdWOYpOKys6t5srFaa6a1PRqvO0yAAWD-fjK5mvz36pPtgOAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تشویق و موج مکزیکی گاهی وقتا تلفات هم داره
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/96708" target="_blank">📅 23:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96707">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بریم سراغ نیمه دوم</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/96707" target="_blank">📅 23:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96706">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پنالتی نیست ادامه بازی</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/96706" target="_blank">📅 23:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96705">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پایان نیمه اول کانادا 0 آفریقای جنوبی 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/Futball180TV/96705" target="_blank">📅 23:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96704">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پنالتی نیست ادامه بازی</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/Futball180TV/96704" target="_blank">📅 23:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96703">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وااااای چیاااا گل نمیشننن</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/Futball180TV/96703" target="_blank">📅 23:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96702">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🔵
دیوید اورنشتین: یان دیومانده تصمیم خود را گرفته است، میخواهد به پاریس برود، او به پروژه اعتقاد دارد و میخواهد توپ طلا و قهرمانی‌ها را با پاری سن ژرمن به دست آورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/Futball180TV/96702" target="_blank">📅 23:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96701">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4r3DcaGk8A_Ky6nji-Wf4E2FjicZNH7hnohlqgYcfF5F1NasLFKiLRBGbX-n9r-3rhDCCy-W7CqQGI_eUNMnnz-yONJHyvjW0G4n4s4s7fjc14r_qVBUttUh0bVg7poUXu2KfEbHbnlwyWBpWEZcKGxiFiL4aJ-1QLx_FouxVt4DCfNuUzDtBTuFGKuLKjhyo_IRPKARf1dFsIvrOWQD8GZqJXXb20c6YG8BlKjkCpbQ_4wTsEvYNIJrenVMvLpfbkmP1A3TfHwQkFlTkbbMMxXQqqzevtFHJTdeUzbVWg9JyiL8uQ2igpr34M_bxnWRSo3p01I1puoXT_x6-IBtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بادوم زمینی یه بازیو هم از دست نمیده.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/Futball180TV/96701" target="_blank">📅 22:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96700">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ای لعنت به هایدریشن بریک گند زدن به فوتبال</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/96700" target="_blank">📅 22:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96699">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBQNhDh6dNyHcuYAHTy5MEszmQSqjBD6smCLQLQQCfmTh0L3gWxUgIiwZpiNXGw1PFaBtcFKr8VyOLtwrFt9zBsDWFB-0yvnK_-C39y7QTMVVQ3SBv414b04JmCJc0mY8dycJC2A8dCRXbVDX1Xwu3BHswb2aIpGGoGwu8NWQSPXoLoZEUISGw_0R1YNnYBd3_ezq_UL6oTgRj9CbNECWP1AFlpc_xLgepVr1PGnOKItl4YH7hhwLKxiq_F3evXAD_hStlseqGxyojOQ9FH4IDuXApS7Aku-zJNYDBommIIDxEfPoNAmQ_waN6nbzlJAWqEMbBxjG56CtTXGLTn2jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ست اول بازی تیم ملی والیبال لهستان و آرژانتین
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/Futball180TV/96699" target="_blank">📅 22:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96698">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">شروع بازی کانادا و آفریقای جنوبی</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/Futball180TV/96698" target="_blank">📅 22:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96697">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-ifEWLzq41DCtE2_Ct0q7fh4dP9sDMs2LU70BTvupMiCB7457bPYxjZNDyuTQXmrm6M1JAR0Mw9tWAgAHuIpMAVERkF2ZNJs_opD-ZM3TpEU_2NVyh-M9IvQ3QACr1hF5u1SNRNUVAjpEkTioJ_U3cZg3a5-g4Nclxw2dsMqwxyOEPyOQSdQnNwSZWzE4A7seBlejz-pUeJ0LwdzBeuGpwqfeIOBSe043gDc4Nvpy3LBTYmtL0b1u_JBOH3_ZmLAUDgmy1AvHTP1Csyt8YkgR3O9qRB1JZS2MTD59c409lYcLwUS3LLDvo_eH29Lq2xhUn_LNFOLd9Hg1T0KiKwuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
#فووووری
— نیکولا شیرا
:
🇸🇦
مربی ایتالیایی آنتونیو کونته در ساعات اخیر پیشنهادی بزرگ از یکی از باشگاه‌های سعودی دریافت کرده است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/Futball180TV/96697" target="_blank">📅 22:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96696">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmjYtlyKghPQdEg7wcZsVYuo-DIBsPDb910QwYMoLPPfUgwD5E9GHMP_NpXS8507lY30_fvM07KZ6nUCA8B1gyGJWUWap4mjWOWe5DjqLg-w6KshYeMbSFCF0m62GfDIcNgbOmQ7-BDderNbgLthufR4WbpnOjnO6S9_Z_-63T6BemXUJ8eZDkIPO1Jj0TpqruVYDJCfeY7dB_cK_ZRr9YsUWDuc9UoTzJAAH-_GmSZ4XsFcnhkJ9FyifPuQwOzRCgB5MTEZSI2Y9GyWALRrwbMtOItCrpKj-6n3eZFKOBVg3cq5wjlFAilOilfCIYAhUxWBNfJVLphEyIkTSYyjaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دیوید اورنشتین:
یان دیومانده تصمیم خود را گرفته است، میخواهد به پاریس برود، او به پروژه اعتقاد دارد و میخواهد توپ طلا و قهرمانی‌ها را با پاری سن ژرمن به دست آورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/96696" target="_blank">📅 22:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96695">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووری؛ فابریزو رومانو:  آلوارز بارسلونا و بارسلونا و بارسلونا را می‌خواهد. من مطمئنم بارسلونا دوباره به خاطر او باز خواهد گشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/Futball180TV/96695" target="_blank">📅 22:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96694">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUa1P3DTQS4mZa_QLFCx1eDo5NL9_5MIMLAEghBBtYtW_7jk4__ihgBFQjeR_tN6auVchX_q9ELV5XfUFGMdc56f6fJ8ScqxcjjqteBfj8mit6NhdOmulUs1LHZpHkzN5bCPdHa0lq4V5h7s3S4gVRNVnJp-W1MP4bXaYSCXz3MiWkZ8bQkM0EDcHcNcddQ-9rRdytccbkeq-XsnvUJeqGBcfXGcTw_fuK8P4ekhDmeectLAoxmcdpPNAss5kIoSqQenGAmPEsXJp1WpL8lJJdmRTu_WXk2fH3479GsWQfrhy7cLZ4jagBbavLbxZVsw3Ax0PMM4-tQeLLFT3UGZhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووری؛ فلوریان پلتنبرگ: چلسی با ساندرلند برای جذب گرانیت‌ژاکا‌به توافق رسید. ارزش این انتقال حدود ۳۰ میلیون یورو خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/96694" target="_blank">📅 21:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96693">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu5-iUuASZCZXs_TBULGK6ATmh6qKZRMyufs3mB6fsUTWoz7cVsIVy4X40B1xvCn478bw8D7l7upUl67s20OCxTIYIMop8hKSUOV_2bERODIm7wuyIMMFCLmiyseQYSRZrzBj1mMy9uMDC0uYX7zOAPDQ7EaM-BPJK8juv775tr_EO43Wne96f8sJoP1-shEnQAqtDIPQG4ZkoXGX0M7W7caPjoLUKj2G7aHx2e-oJH_znwwBNXXyU8UeMNcu90aXpGZ5_z65GkpZ3ofYS15T5O1oAuk5k4Ek_L0o1aI8CGWeGcw_itlQdsgC7uNcl1tf1vwvIj1d2nZvyjBYad8Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👀
رونالدو نازاریو : نیمار؟ امیدوارم عملکردش همه کسایی که فوتبالشو تموم شده میدونن رو ساکت کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/96693" target="_blank">📅 21:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96692">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووری
؛ فابریزو رومانو:
آلوارز بارسلونا و بارسلونا و بارسلونا را می‌خواهد. من مطمئنم بارسلونا دوباره به خاطر او باز خواهد گشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/96692" target="_blank">📅 21:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96690">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iAOwNvrevqRfEv7-TY2_7n_QyN1EVFLHsvSyWqBWdRz_SgMIyRY3OdzxfSDt1uvempF_yT0t1xovLAtScf6XCsMp3wEQO7Bxi6O9dAVyB5nUKZCyBIfKv4qlQdP8lt6-DRK-gr8oneEdWUTvsEXEdygaMYoeR15JThJ_LVtEIzFiwCiViPOx1DWSWsxbqaEnxjUQIpyx1d9JUT2OCAFq6SnmP1nKFDux9jcTsXQEXHC_4xNFag0PjqTvkoowjs6anpItj-zjyxp1g99ZleQ5jqEIAEj02FhEFVL541L8D5X4zlLmJDPYgZV76_0rhtEcCEb7fKhj2wPTlfNU_V5n2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ro7yjt5Gbbg8gpLf2Iurguaof01aBTnlqo39M0eCoy37BRBS_ncNQPyBVkUmOoHzPVFXgJUM4kBFM7WqeVZehZV-B-HUFm_VEUES6bFVBgSMhGybfqhI3JTutC9C6vMkQhy4Np0eKWyU9RENyAcMCKv__H-lo3WcNsoBeMwDvjXu7BVfS0HPM2wK3xTC38FoQD1lGO0wRDhE4C_ZvEUHOMQllIyrVOGXrhQdrZiXcvTTSvD_O8D_2elB7eCgCgsCrFrLLanpGfKS6icQPNPCtHhlHWkdAf00H5JLar_7C_gSsfKAePIFX5FgCVptYgpB1bUvfF5PTytXLhO_FUXlDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇿🇦
🇨🇦
ترکیب آفریقای جنوبی و کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/96690" target="_blank">📅 21:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96689">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSLXqPic8yCC_B4nrSzxaL3Sxz1qehB4EbeGznkl__IJrWSdEwq3TruoEcxN4pgybjTPc0F9LdwYC3qSqt2_53FQ9Q8mBMJGxj05j_mgbcoj5zQ9OhV0mn7pPTvHTVM7sePAjRMXcf9jgB_Ji1e0XGl3TN-5j-fIz2Wep7ls0MzP44K9DkpdHZa4hmWiIWFkWdKKc0j-LTOgv4bvOaw4xAuE0RPCjdtbGIuAroFAuvaH2wutqgIMX0_nf3cbjkYpieJgS3muF1EkGf_ebDfAW3U08Dn65BXpKBY_-RMJZJHscJBejTNXrpjd069PRNTLiJJ73jvahudTja0-k9b2Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
روبرت لواندوفسکی به شیکاگو فایر آمریکا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/96689" target="_blank">📅 21:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96688">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/96688" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/96688" target="_blank">📅 21:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96687">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prErEihScnH8lTPN1rsKBYNRMYypdwBmlNW9Nw7JVa41Yr_AlMVgcyZ-ZnOUfShd7JZZNh2HTjHewajNtlBGbm3QB3NWmo-1-YfNGC1iDiI-khQEc81TaFRl11cpKhQkecr26I3j_jZ255ZqAJaofy2lAhcPSR1W7ydGZXdihxP1EGTEiQyTUM7DD5uoxGjT5_bjahp-bTifyIxjaEdvp3eda8GRRLuP7M5M9nghUhKtp5hvw9lWZ1pEw0A5_HiAp8B9Kw45kheVNL9WJxK_AM78JR9PmdOSBBWAqNqzRfff9ClxwY1tMSJkJOsvPDvwEubePtNt1J9VDkr7BNMPdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/96687" target="_blank">📅 21:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96686">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1560dfcd3a.mp4?token=cxaG-W9FR7oHrjjzsDemSHwfACbTudKn-uXmppMN--Wt2rrwbokLdoeSD-1oAu38_quCtr1W4G6WPNlebkP0Tr50iobK1mGlsmiJ6btyvU6PRVKYOe-WAyPtrjOzZcQkYt_IPrWWCiXxLRjjpNmy2z0knazYJYvaSSquFxPTIKPS4zV1Nb_0GGXNxtoGJeRynVCZ5J6GCdGWDvWB0OI_bljZQ0t_BJyHuo3hBOzyRhr941nSMX-ojhxMOZUmWj6yPhNJbwEKje_lFZzi0MZYg9gTg5xNW8iGDq_m1q_9TSsblDL3h6BbfdFgEHyj6UefIT2dqUNIsIg-uBOZrLKanA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1560dfcd3a.mp4?token=cxaG-W9FR7oHrjjzsDemSHwfACbTudKn-uXmppMN--Wt2rrwbokLdoeSD-1oAu38_quCtr1W4G6WPNlebkP0Tr50iobK1mGlsmiJ6btyvU6PRVKYOe-WAyPtrjOzZcQkYt_IPrWWCiXxLRjjpNmy2z0knazYJYvaSSquFxPTIKPS4zV1Nb_0GGXNxtoGJeRynVCZ5J6GCdGWDvWB0OI_bljZQ0t_BJyHuo3hBOzyRhr941nSMX-ojhxMOZUmWj6yPhNJbwEKje_lFZzi0MZYg9gTg5xNW8iGDq_m1q_9TSsblDL3h6BbfdFgEHyj6UefIT2dqUNIsIg-uBOZrLKanA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
بخت یه جوون ایرانی وقتی ساعت ۷ صبح به امید صعود تیم‌ قلعه‌نویی از خوابش میزنه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/96686" target="_blank">📅 21:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96685">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S74nt8I6KWhiB2YBQQZqnsh77HrKfMm9lBnggGR5mXbJYuEgIXnBzpj8Aws3oGJCJCkjH3iU23YjqTsV67T2Nm-RZFFuJEdLHda4BBbtc8wpuuca9zPSlpq2_uZwYvdRsLef_c2mJE9Ildv3CR4hDnoChLQ8OYbG9-gi1FnZjsttrL1EC6yxd5Q_KJ429ATBTl0hv1fatOqSf3ZXKIcLhhHJhKUJs4_HJa9uduz3VgWYP1nxEcayOPfJKrbRaADkeRC6DlT5mOrvytYpE1YWrfgU1WHj0MZNYuKkDBPYBR4KTOpbmGVojhbdGknMpe6REcMONNPnlasmO9PKqCQhqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیکلی نیکول اکس سابق یامال تو کیت آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/96685" target="_blank">📅 20:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96684">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a512c25b6.mp4?token=My56tZfvlhIlGp1tBnPCUH61rhlX-NNT2XCYReKPUAGol8bkyDAc8rjZ3RNicNRgWXe4T-HQXiwTraxzJ6OF2bzTGkEsVaputhDVZ5PfyOUw_PtzB6CWxhA3hpJYGP-37YiblZEOzLj3hx7Sn77B9E9FSnaQ7DotR7lpIfgysTf5Gn8lzsvhcrt-kxcuV_xnhfQJcsUbEPtR-BDI_o3rcS-sJ_-oOn4x7Fcfs8PPOrcrHkoqCUwFn5qQCTFkuf8DQjTRG8eAkkdXAJ7byegsB18P8EgbH1qO5RnGHs0JknHMTDEDkqZ6zY-yFTAsl0B1o9DUY9ZcNV2jO1BOQK_0FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a512c25b6.mp4?token=My56tZfvlhIlGp1tBnPCUH61rhlX-NNT2XCYReKPUAGol8bkyDAc8rjZ3RNicNRgWXe4T-HQXiwTraxzJ6OF2bzTGkEsVaputhDVZ5PfyOUw_PtzB6CWxhA3hpJYGP-37YiblZEOzLj3hx7Sn77B9E9FSnaQ7DotR7lpIfgysTf5Gn8lzsvhcrt-kxcuV_xnhfQJcsUbEPtR-BDI_o3rcS-sJ_-oOn4x7Fcfs8PPOrcrHkoqCUwFn5qQCTFkuf8DQjTRG8eAkkdXAJ7byegsB18P8EgbH1qO5RnGHs0JknHMTDEDkqZ6zY-yFTAsl0B1o9DUY9ZcNV2jO1BOQK_0FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
😁
دختر جذاب ایرانی با پدرش تو ورزشگاه سیاتل که به لطف‌طارمی ناراحت رفتن خونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/96684" target="_blank">📅 20:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96683">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/207e25de79.mp4?token=b1U_ruRhpabFs56H0buPKINlRlXz4adMIYbFMXBtYX5HkqJqSKPYEioBg-WCZ0p7swaX-R2ErMry2C48qprzeq96H9xAQUPQ5SH6VoWBfvZReiAgh1PDfL1vs8rHac0fHJYivYLL8eFje7fGrIBp6_2b9P8ePqiQKjuUDmrfsuTTgvNnAPArG6JRxGoaPZp2L-GtPsDF2FSm1h7VzQJcPu4RGECtz7CZ0Vew4W-MGaa_CsBEZTiNq9gA8wll_aiYcXYUPwKSGYmGXkF0JjcMI0sgP1TrDpk69qRyOl4w3q3c_o9f2P9gEkPr8uUFF1wE2rGSxPpftofMttr30rmXpUw4rNCczSELlPrTS_cH9FqFoZNxbrtWlOJuhqHLMyRh1hhw8KVWEMm2hVUv04Vh4SxDlNhj070gBbnP29jMgguSlKez2Z3U_7ZztlG3VRxUWOGc49LqzxxBnksd1PMrqvbJQECkDoToqV4kjHCMynhB88Q6aubzVl__TjKPzUWt6MevXbhFbNZYSgCxwBDi2vCEHohbX4b5GXUp5Be4NFDcOTrjmk-LCu4-zCEZnPl5z2lP-sfpEl90RkbzPmB76tGe28Vsp7Kt_4gUfYBKZvDSwHu8fhCPzH2DFQsEjAozmSxq1DVYkz5yLs1s8lkrZDhhCJTP35iAG3GF7wqzuzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/207e25de79.mp4?token=b1U_ruRhpabFs56H0buPKINlRlXz4adMIYbFMXBtYX5HkqJqSKPYEioBg-WCZ0p7swaX-R2ErMry2C48qprzeq96H9xAQUPQ5SH6VoWBfvZReiAgh1PDfL1vs8rHac0fHJYivYLL8eFje7fGrIBp6_2b9P8ePqiQKjuUDmrfsuTTgvNnAPArG6JRxGoaPZp2L-GtPsDF2FSm1h7VzQJcPu4RGECtz7CZ0Vew4W-MGaa_CsBEZTiNq9gA8wll_aiYcXYUPwKSGYmGXkF0JjcMI0sgP1TrDpk69qRyOl4w3q3c_o9f2P9gEkPr8uUFF1wE2rGSxPpftofMttr30rmXpUw4rNCczSELlPrTS_cH9FqFoZNxbrtWlOJuhqHLMyRh1hhw8KVWEMm2hVUv04Vh4SxDlNhj070gBbnP29jMgguSlKez2Z3U_7ZztlG3VRxUWOGc49LqzxxBnksd1PMrqvbJQECkDoToqV4kjHCMynhB88Q6aubzVl__TjKPzUWt6MevXbhFbNZYSgCxwBDi2vCEHohbX4b5GXUp5Be4NFDcOTrjmk-LCu4-zCEZnPl5z2lP-sfpEl90RkbzPmB76tGe28Vsp7Kt_4gUfYBKZvDSwHu8fhCPzH2DFQsEjAozmSxq1DVYkz5yLs1s8lkrZDhhCJTP35iAG3GF7wqzuzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپید بین هوادارای نروژ : چه خبرتونه کصکشا؟  من اومدم هالندو ببینیم ولی چرا کلی هالند بین تماشاگراست؟ اینا همشون شکل هالندن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/96683" target="_blank">📅 20:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96682">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbWlQK0-S4jQo1yEnrElthW5khvOchGsq-lE7YDD7xLT_R-s5o7py4ugvEqHBCmEYWUPOa6L3KYPI6csuslt4H3kWF5WHk5fNM0kt6_5-V1DpRWKJbGJManvfcSLIxDdGx4d0o3-1S90g309LschPB85cESpDM-cH-wjNzqd2Q69RT3ZbGgLAqMJ2BMhFR-1nTF9PJnjKTbUi0CVfSHGA4QQdOolCLZO9gxVDU6QuX-mhzlPD1HngYVWv4C3t3gt4gEvjTFJz-DD2Ax_xtpIWrshzz-bhjR8-yxBMEWki1ghv--GDmznj_nbgr7OdX9CGWWuQu9u0j9qAVli9x9HBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لوکاس تریخو، مدافع آرژانتینی که در لیگ ونزوئلا بازی میکرد، قرار بوده برای بچه هاش کادو بخره ولی چون مجبور بوده برای تیمش یک مسابقه انجام بده گفت: وقتی بازیم تموم شد، براتون کادو میارم..
🔺
بعد متوجه میشه تو شهری که خانوادش زندگی میکنن زلزله اومده و بلافاصله برمیگرده به خونه‌شون که میبینه ساختمان کاملاً فرو ریخته. بعد از جستجو متاسفانه لوکاس، همسر و بچه هاش رو از دست داد.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/96682" target="_blank">📅 20:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96681">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af312cfcd3.mp4?token=nAqWh8j6cjLxZs1daZ2pOzgXUrLE_zeDht9DGXTdNLqpH3IDTuIla3BY0IhwS4UVCu-Bx4SyDB9-MO5HblH4kRPZDTHYU0NFWtT7xSqIp1agCrvsmcp4f97np-8rOGXRxeLc6q5oUcpFpNdR0Uw-kaqu7sOS0GsAM2Yui6HuiZFLmJzl2nwqAYo0Bdhf_yywFTyhwx4E8mhMmBh2wic1DF-71KbEwHdy8yPp6lM8KN_ThcVYHstCXLxEMswOw_O1ZKCfEmXFWghCmvsAjlVQu0FTbif6Kn9Q1mBxGBU-9aW7MCyPr1S_GgGw5J6ZRaEzq_QH0iF09UgEkqVpnU9e3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af312cfcd3.mp4?token=nAqWh8j6cjLxZs1daZ2pOzgXUrLE_zeDht9DGXTdNLqpH3IDTuIla3BY0IhwS4UVCu-Bx4SyDB9-MO5HblH4kRPZDTHYU0NFWtT7xSqIp1agCrvsmcp4f97np-8rOGXRxeLc6q5oUcpFpNdR0Uw-kaqu7sOS0GsAM2Yui6HuiZFLmJzl2nwqAYo0Bdhf_yywFTyhwx4E8mhMmBh2wic1DF-71KbEwHdy8yPp6lM8KN_ThcVYHstCXLxEMswOw_O1ZKCfEmXFWghCmvsAjlVQu0FTbif6Kn9Q1mBxGBU-9aW7MCyPr1S_GgGw5J6ZRaEzq_QH0iF09UgEkqVpnU9e3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
▶️
وضعیت نفرات تیم‌منتخب ایران بعد از گل تساوی اتریش مقابل الجزایر و شادی مردم از حذف شدن تیم قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/96681" target="_blank">📅 20:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96680">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpS_-fvd412RaQkxCsMc0dNgPTG2bEsHQU2u584DoHSf7Q0vxIOymhAQOEov6z73ztmFMXCLahjJTuQTR0iJDXXlKSX-VHxCtaFxRc2T11dWwHu860iEPnMw0gNO5VQaQrtloGHZFCnOM9mi8-v3e0R0MvsJIjq6nYoEh4TlI-lXvq1D46JVbY2VmE6NNYBDY4fdAvxbAg9NffLOvvrxqgOJT24KWd5zM5Is2OP0x6FkhQzScA4DSa2WNVBVQ4XRzmsY8QRdulORyavJej86nhotCdaueiwGiL5yDASqSu9DZo--5Wq69esxVe33UKXrdUz6kjYrf6OfQy30OzKIdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🇵🇹
وقتی‌بازیکنان پرتغال حرص این‌دوتا بانوی جذاب رو در میارن و سوژه رسانه‌ها میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/96680" target="_blank">📅 20:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96671">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DEIrPYAnDlm-fMbykD_F7XFXxozAB6Uo2XjU6MDR5mYJLmI5rw8XGfGkkojljhyi67v_YETbJOO981uThSCCQtUEsR0lrjYZ-tQ00sxGofvPLukde1Mnc4zt3NffHdV04d6y5tINVTmL7TstoBAwIpIC5gGw7rJOXEz7pfEg4sJEEEfGsF8smii6Wk4tFjWbrVUKiyObZ6MxFFSJChusAgRIkb3X7rLHIw9xofL4n7FzkbM2Ft4QL5sVmFj0IMYwfSXMRQahhtnw27SuSRw-mGSWslnlcqvmHMKLVsowXixy5c-Dnt6s5pXt2CIxCC_mS7P_015PkxTFp6fa0dz5kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JrxXW5eRa4j9_neCYxb54EiICr2eLfZoRFPpSfIMI-eU_VC_8xA-5m_eCsJttEJNZGE8Y-wzlTVPyUGhfcxKRqkuwN8EICW_Kez9_WzrANGKtbPZVKI-7WxTFsgkTk_njxbDCnmX8jwaClBNI7Rp7BLRnHeRi7kax4dt9a6n9tj23Vbjcj4CCtW7EwiWMda8uCuicCCgKF7eXzpC76MUYeshczppXLna0MhNLSipdlnd17FcXK7Q5Lt7Jz75WuT4pBSAeVFwGC8FGNWvKlKB-kmBxbCrsX_f1cPOUe1nXJx5jr_YV7JKhgWEdj2-29UYrgPDMoFpuaPp3z231d31Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kdg6ha3Rh244k74nfl4XxlywmLYwylHC7akuNWGr1yMA3Na6Wg7rQJcndnN5nAvdDuaca17TREQ-5OzFNauvXBrpzLVwZNBudtPckQOWMiXxkAjQCptpOHr6AYRFuREJo_i9q1JBA07SiIYMsH1XxepT_R5BQImidSEZA5k0nusl3aEtlgT7zudeb76PZO1Klwwz40JKPb3TNAI_F-9HFZKfskOvm_s3vwES5mSzaDhPY15-M62jiO5KqDj8NShPtmgV0U3k0tCuFgPMusKZEKZy1cMWSMTKPyjo0qGmEG7AbZXglaXhdd4wddMWBeMa9n4zNz1r44egHUE2IXiAjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rDyjFVHkx8GmSRj9pzM1YDCI7rC9xUi_RjRtXOkpAiQtDDIcmc40_uloBzN1emS3YtuEFZvmEJOQBCVEg-GQy0_CaJBMEetjMo-cNcsVTDmf4NPXLMV__CY0LY-Y6plEkooOSmRe_q5JnMfoMCNZ8QDtrQKDtNpoafZbdBILPHxsPdS8ghDccUC8by12s0pFqdRxoF2Vwc4yUG60MyGUCw7KAKoF09nLYL-Zjz89vwL8FEdge5omF57ccVbxvUrU0RU765CB-CeAvCZhhYnfh_CXxIA-oimD5Vk6Y4xwKKDka9xhLIruFgKRv1GpFHeg_I7ULqX77tCnSUMCDlNS4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pPRFdV430Gc-4Kzf2yvb2ipkV7Kk8e2qpSJSrJgRy1-s0LL7eoX9bvk-rTq7RgyVIHWgjhjaTM69yPbPoKnXE0l3wZX1JFQKMrN7PrsX94cjpyi29F3UVYJKuaBxyISrIvoycm-Gb3aWCudyoHFL0jY1PALlJuwfkQUkzP0b_O4_fqUV5aewO0aCj86B74bvd20PNryZfOP4ynnmiz_t25FziF34zAgIfG2fo4d8ZS5PJtu09gjuiWlNbyTHzOSfYg6te62kGrsmClm1-9LYl0GUJlWE-FkPpsMfPsrizNBupryJNIywC-x6jOFTp9_mgBr01k3HTjP7cySNMNd3tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qkd4Z-ndf1LqXpI4HNOSsXPz_DyQ5HydgvJvE9YdQkM-TKc6__d_gy7sAKbYTqe1rkt2pG2vSprE0EY2PIJ2jAJj1XuDQB3b6FAsJ4LKNoLF9wrZsrtKCRno5vYrlFWDdt4INTgl5MsSp-2AxL1ej8KmcGrz6VCvrI61Ym4ul9rIJol_3VBW7gV_Uh4uaIkUfdxPVo2I0NpFbCB30cc2WBKvX0d_ROQ_0LaFmy0VSLq5dNkNe36xtU0vPKCa98RM9O1e3ayHb6zefdSIj3u_AVfVwve8A_dtDJguNjy5-l1hKYlCz-SPba0XAia4F0ZNgz7COZmJSA0LS0-_DzIbng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aRfQGAqBkUQqNarqeK23ANof1Cg-QtV-rzFA4-1wx-vw7SP6OrgGpZ-u1ByD2v8KR31uzJsHGRBYl8GEoeeI6MpbYxmOg3Sypb7O6fvsy6CDZc5qrvpSbXDAPFguUt-tSvT1k4WHwAhusDUqFNIUb5GiwP6Oj5o86MvIlFywS6_nktqdpaEI3WkEOrQaaKXR6wQnLOZ5HHbxpEqDhboaIlXW1XHHT3_2GPi8ZcITxXGgmNY40_yD7Yti-mDQhNJ6Ril8b9wOHrjA995yRN4QDmAmIGQ-QzMqwcuAAAoL_K4r_ferBL__xXyqvlscEwF_S5TMYJabds1aqqcZWWkfig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lt-BT2OoHf2BYM75ZYQDjZVn0gZE3I-qNdTJ3Md6nBicmIqmJ4_xeDp9LNttM0CsMtFa6wK4QLA_2I8qiQGulTPxulDhuJLQPC8PgRV_MEEX2cEVyL7Z58TGIbDQr1qDMgVDIXJRWuJ_pGV2pduIolUWcxJqwUSnPdTfmfAVN7SAbXUte6lMsXs_rSuMec6HF7CvGz1VwikC4W7HQm9ibDKskEV7Ld1z2F3ZESRv5hLkgUztudriIl_ry2nQ5htxn5gjc9QBjhW7-Ht92x6ZZfHMDk7uqjfVRk0WEZ2CcmBU21u_APOP-gPVWtf7AJyOQn9stTcqHe6wDIxw1N1bCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uqmNnLVmFnuxjdbE-ztpPXAx8MDw6TFG2Jbbc_FMkc7hoFt95ALT4XNqpb2T6lkYDsgcCWFrtrqO-P3unWMPt56lnV9RxgdoHMXRBTbUv3_Hd8bFypJKneOQ7ZZ3KADuJwMfoaUPz1uGJQaUjbFx08DUBhDopZOMd9tZIO_k9Fn6ph8KYB3VQZ4uJWt2pFvlNUi2W3FFJzCh9b8Bdglae2XrsVwWZwA6OwgNVMrw5AIIxcOsKYbxpCjVtm4GXc_NemEV_Pf2MtC78s4dEVA1IfpqsaUWIXuTFo4wZQhf4vZWO_Ie8iR4bJCNlogqoszqoOhbqmvWhc1w-D8urIUpQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😐
🇲🇽
تصاویر ازدواج نیکی‌هرناندز بازیکن تیم‌ملی بانوان مکزیک
💍
💍
💍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/96671" target="_blank">📅 20:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96670">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e4bda6f8.mp4?token=igTIUcIQsSnx10orzkEAdXisQQV9fZNu22eq4jtgix-_yh9NnuoIoSpirIap5FkwtMvYNQ4a-YokkFzsIlQ43BG5NTjrYEQLCvKh0HbNvEZLpyat2AeGaoe0VRlGmX8vZY6MDuY6yd_LrBdx1NPiPAYKHcQGeEV9aZcwk1GsSsPj7Qnb7u4ce1r7eVTvda0z_8tA-52VkmWLKJPHcaIex4JRnQUz3WZBVuQOrDC50n3fPmiYgASLB0hCAFC_npTmobmvkOYITE4C4LE5jufpOOMp6KSWoXwKyfDSe8IAbKs7gt79apOCdXwY12BDTg0PyK6EQibS2uAHoYcYLpYUjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e4bda6f8.mp4?token=igTIUcIQsSnx10orzkEAdXisQQV9fZNu22eq4jtgix-_yh9NnuoIoSpirIap5FkwtMvYNQ4a-YokkFzsIlQ43BG5NTjrYEQLCvKh0HbNvEZLpyat2AeGaoe0VRlGmX8vZY6MDuY6yd_LrBdx1NPiPAYKHcQGeEV9aZcwk1GsSsPj7Qnb7u4ce1r7eVTvda0z_8tA-52VkmWLKJPHcaIex4JRnQUz3WZBVuQOrDC50n3fPmiYgASLB0hCAFC_npTmobmvkOYITE4C4LE5jufpOOMp6KSWoXwKyfDSe8IAbKs7gt79apOCdXwY12BDTg0PyK6EQibS2uAHoYcYLpYUjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✔️
🇰🇷
سرمربی کره‌جنوبی بدین‌شکل ضمن ابراز شرمساری و عذرخواهی فراوان از مردم کشورش، از هدایت این‌تیم بعد حذف از جام‌جهانی استعفا داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/96670" target="_blank">📅 19:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96669">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Igo8QKteMB1oZMsDJngcGWJQACgBwRsknNinHKHxZJjxQCyv-wfD4YqvZfviweNQduWZewh5O2-YRNp8kL_3wpS9z6UJQWq7fBojmjzhERNfGK7LVNeYZ8ggsQ5u5zDPbOKOyJAoL3dbTOmI5qdqlD6eZrocsYbJmFYNEiFKvIkNj4kGVhU5dplDSQyGCUtitzgTsxI1R2SuX29aCx1z-Mnvds_bHUjsCodlcegZpyNuxY9W6lHBhecU_YF7L1E2JNi9CYuKUG8JQg4ibFYruDQ08gMHq6wn9PNfTcjWy9taPVe_OzOOIbW-heZ3jO-HDvcZSdaTW9hxQqGhQQuIjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه منچستریونایتد اعلام کرد که مانوئل اوگارته، دچار پارگی رباط زانو شده و برای مدت طولانی غایب خواهد بود.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/96669" target="_blank">📅 19:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96668">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b44065a1.mp4?token=KZHi1pTFWwoWhnCJDrDBe5sQifrplYv4IymFesQ06xWkGkvsKBm-i85CJq3tFWv57ZzO4XZIpFloHFSr8P5N9BwdJ_CrAVsKGa0f4LrqEkNhVG36uwPKmVRvu6-7_IE31-tlNIM5eXtnwcvoBJscjiEN4Wm_H3CstGaQK6AgcbJ2MfqcM0GWJ1fuDRPumAbplb6ZzxKrH2NnMT-PDJlKaH-vp2T7WmzrePEfiZvMQvl_yEp_5H96-l9WQonSB4QXyaHyNHU9qOzvaK4wgFSUiqk0jL4eJXpjZ8uulKvIahRysdDhdUCqKKIAvnmUBlag6AxANWKLirr19GqNffWsxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b44065a1.mp4?token=KZHi1pTFWwoWhnCJDrDBe5sQifrplYv4IymFesQ06xWkGkvsKBm-i85CJq3tFWv57ZzO4XZIpFloHFSr8P5N9BwdJ_CrAVsKGa0f4LrqEkNhVG36uwPKmVRvu6-7_IE31-tlNIM5eXtnwcvoBJscjiEN4Wm_H3CstGaQK6AgcbJ2MfqcM0GWJ1fuDRPumAbplb6ZzxKrH2NnMT-PDJlKaH-vp2T7WmzrePEfiZvMQvl_yEp_5H96-l9WQonSB4QXyaHyNHU9qOzvaK4wgFSUiqk0jL4eJXpjZ8uulKvIahRysdDhdUCqKKIAvnmUBlag6AxANWKLirr19GqNffWsxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📊
🇩🇿
پاس‌های فراوان الجزایر پیش از گل در بازی مقابل اتریش که رکورد جالبی به ثبت رسونده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/96668" target="_blank">📅 19:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96667">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVOjm_OgXl2GhzoXYZ6zOY76aiFiF33A8ncCjmMHlbPu9f6YFjcM1_dyy7fRgxMAm-keQoWAbfrIZsUUMGnqP41GZqPxxSt3aUr2JCcSWWkPU_-Y6FEuwuzdVvugzsJHYJihbTh8sDZezlb1kH8T69jTMz0wmgJGqHO1Dwwd6tAIJ-Gn9-GBz3tkYyvPBC9G-ftjP8aSXNq-YZoNfTyK6zyErTCYa1zvTaIZq3xdzIYHqF42lKk8BmnRw6HV7Pt23ik29fyS1eJ7koNXCAjfUD5bEnvyeA3ojlfMp5WB8Dldda8DuiWRlR_TByS8XwGAIYdrkMPxIohUgBqsWKmBlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
😐
جاسم بازیکن کسخل اردن بعد بازی با آرژانتین برای تمسخر مسی این عکس رو پست کرده که جمعیت عظیم فوتبال دوستان زیر پستش از خجالتش در اومدن و مجبور شد کامنتاشو ببنده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/96667" target="_blank">📅 19:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96666">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94d5bf8566.mp4?token=X95VrPKEn0vVpmL4GnIxeUzdpVAGvn04BtkZ6SSTN0dLIVL6lDuOwufEAoXkYHIjHxaXrMCm44RbMDB_9kx5I_Roerj2BkVU7a-lJl7HZ9sB-_d4Gxr1PSzeAxzQXOxQWMAEJTvxFEI958fw4r17zvaw_W1lafoiav80CAfiU1hLhqVR2WOel9C3erNrv0gYyJHAeuyzl0yFgJShidg51jtkxDEj9dBDpHOJw0ux7FvMCNTMXcUb45cl3G6E0uvTweahQ3aErwhnUWlujHAHZqkaXY19mutwvuE_0s6E0HovOX1h-KPC_k_3S5knmA65qU_koCMXS4B5hUosLN7Z0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94d5bf8566.mp4?token=X95VrPKEn0vVpmL4GnIxeUzdpVAGvn04BtkZ6SSTN0dLIVL6lDuOwufEAoXkYHIjHxaXrMCm44RbMDB_9kx5I_Roerj2BkVU7a-lJl7HZ9sB-_d4Gxr1PSzeAxzQXOxQWMAEJTvxFEI958fw4r17zvaw_W1lafoiav80CAfiU1hLhqVR2WOel9C3erNrv0gYyJHAeuyzl0yFgJShidg51jtkxDEj9dBDpHOJw0ux7FvMCNTMXcUb45cl3G6E0uvTweahQ3aErwhnUWlujHAHZqkaXY19mutwvuE_0s6E0HovOX1h-KPC_k_3S5knmA65qU_koCMXS4B5hUosLN7Z0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
😢
🇩🇿
خوشحالی الجزایری‌ها از دریافت گل‌سوم مقابل اتریش و عدم برخورد با اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/96666" target="_blank">📅 19:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96665">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIsup7CJVrBtdLO6b2czBvi1gZsneSKpLVSrAEn5zpMnx09PNRfxKK-kB2UVaK3BMdZK3ZReLstKFe5jszrrFaAGyOFuPXpTaurEe6jkr1jHKw9n0ffWzirnSBt1wZgkAZuRWR34uEI9KCXWMx4AjoMt84kk6A6Zwo-O3im5OhmkSeMPm_s8qij5eMDtMxDjB0aTnMp-w4mwRQuDFRL2fOKfvpAB3Oqz3BgvQR-nUrY7CIaNDRP7djdocV5K_bar34RRaCukz_IbVuPmyf-5u9QoeZdOBhLkB_NmEULNqEJ-aHJAb5dXcKcYs91oyc6OVlC4XNYlAxRvNezyIpesGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🇵🇹
کریستیانو رونالدو  :
• ۲۰۰۶ مقام چهارم.
• ۲۰۱۰ مرحله یک هشتم نهایی.
• ۲۰۱۴ مرحله گروهی.
• ۲۰۱۸ مرحله یک هشتم نهایی.
• ۲۰۲۲ یک چهارم نهایی.
• ۲۰۲۶ صعود به مرحله ۳۲+.
🏆
- عدم کسب جام جهانی
❌
.
📊
🇦🇷
🤩
لیونل مسی  :
• ۲۰۰۶ یک چهارم نهایی.
• ۲۰۱۰ یک چهارم نهایی.
• ۲۰۱۴ نایب قهرمان.
• ۲۰۱۸ مرحله یک هشتم نهایی.
• ۲۰۲۲ قهرمان.
• ۲۰۲۶ صعود به مرحله ۳۲+.
🏆
- یک بار قهرمان جام جهانی شده است
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/96665" target="_blank">📅 18:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96664">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geKjD3WF0F0o03iQNcY8O18a69XqsdBZ9OCL1j0CRCEheQquhvaM3uWi4c99fg4snzWenqPvLIgqaEE-4T7opOih1rOHKT2HSy5HAe33ud3JTZV0Lqj4OPkide3zrN71VmDb8feDCYp8HPds3CsCHPMfFMsDBDLU2Uhky-4_UAxHv4fql0juSt88IAOqyoUpwChXrCAQs-R4Y4keWMxXK8rjyqgV9uAXLD9nn4uiNOiOSx1Tl2mvUEnJ-bfxmSXR1pAAgup5zMTt6RgqEJgMq1YlHNgXFMUyqCTgMdqn8cNvqLFJEwBodmMJ6FiyBDMwhKuvEYEfHArRlX3QGNG_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇦
🏆
🇿🇦
پیش‌بینی اوپتا از اول بازی امشب مرحله حذفی بین کانادا و آفریقای‌جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/96664" target="_blank">📅 18:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96661">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bOqWaXqbB8J5v_PlSe6yiACNdaPdeF3nwBIhK92kg_VuW3Xc52nKlO0jtAaYOzKXNfW-gL13x4_R3X9dG2BCxfWKssfQEyvbaVhkNrJHAhAhOZmqxMJ3Kfl9nb40NJsx_eyDg1N3HZ1DQ-5bKwhjRqHveJmNCqYQHAFFtjZB-lF5TCJoZUuOVy1J_b8al5cFWWFimqj_CsJOMVY_c7VHOlsVLr83ibworPivqOTJeNGRMrovtk4saILFQhyCbaMT4gDpO6MAiKBrunGtbvpQUSJ-wafodLFc6flGPhHeBN1051Xz7ZxC8soXN5qBYbpEWAorR27fPITQVqU0pQR0AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ygji3XAZG-LO8tlIyj6ypHpNu-BIb6eO991a4XW5NUCgPIK2iGOD0NHA2m2VgRUN4O6BG38zs_PAO6ye4N0P6AOBHRavuvq2OSa-luD7e3n1U51bsaifSFcutqqSrhL4YlZv76pPJ-VANrZ-aIAbn7ZRqegvxVDNcBMJe8QF_P53hp7lyU9Cw53yZV3Ita41uofPwy415DrUS_YofvaK240lHg9eAgb5jvhHpP1KeFffMs4ZgXtZWW-KuTtHKWyTbrIO9JZdI4llHLbNxuPDj_0lHC_eSEE10TKZs4tStRuHlqpWmmAwvsM-SMJyWjQko97eRUnOnXknhGEdWnA0vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bt8z8FIkfBS41w5C7dIG6cyGhZxky2NNWt_RKhV2xFhuliNJzMwJyB23Tb5h36UjblvN7ujiPNsSbvIcfY93kY3y9sJd34KKOONuQ7yh0qickFyI71zm9wCVFnn5d65J9k4OJXkhLWOjFO0YLG4cVf7GSe3t5L1yCrYynGdOV3p0poip2mYH2gi8WHaoqj8y1ARzttaTE7EBcNdfcVcMKXEG7URpJtMtebeGxdtQrmS-HHux7L3D05d6EzU3f6O4BizHgy3jpMd_eiMpRf5aZIZ5aD3z_p081xMW1Tf24ngjuBcTPuD4T2pwq4cCMOrc0KoQoTcDGqRsfqSYGWZxMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
🥇
رئال مادرید مرحله گروهی جام جهانی را با بیشترین تعداد جوایز بهترین بازیکن بازی به پایان رساند، با ۸ جایزه، پیشتاز نسبت به لیورپول با ۴ جایزه، و پاری سن ژرمن و بایرن مونیخ با ۳ جایزه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/96661" target="_blank">📅 18:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96660">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2382f7a63a.mp4?token=V__McqTjmfEkDUs7tOqP5YXhHwY8by_mepTTkPFq88WLxEFa49JJ8-Xi1AhMUBQbuctncGyLTa-BYkIWrd1UCVcruudbrYb7nmk7zRO9RlUJ1bvh3ZyMONhdXgQo65VKcsfFdjrc0gpmoqaCMGX8uWZgClEg5ZpsVTgrLcO74fp3_f-HOO2dSJxtJqyGDbEUOuAmAsHB_UZx6OvMUmx8VKL2Q-asyu_h7jF9EREuzgRzLrpvFK0ajR6F8CqCepsKKqb1Jk0PtA9Gt5GdaOp3_j9JrLvO_h04hobZYKMyS1Q0BytfDFXaXsSPNsW5RglXudk6r2ADD3dKYqfgN_4J1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2382f7a63a.mp4?token=V__McqTjmfEkDUs7tOqP5YXhHwY8by_mepTTkPFq88WLxEFa49JJ8-Xi1AhMUBQbuctncGyLTa-BYkIWrd1UCVcruudbrYb7nmk7zRO9RlUJ1bvh3ZyMONhdXgQo65VKcsfFdjrc0gpmoqaCMGX8uWZgClEg5ZpsVTgrLcO74fp3_f-HOO2dSJxtJqyGDbEUOuAmAsHB_UZx6OvMUmx8VKL2Q-asyu_h7jF9EREuzgRzLrpvFK0ajR6F8CqCepsKKqb1Jk0PtA9Gt5GdaOp3_j9JrLvO_h04hobZYKMyS1Q0BytfDFXaXsSPNsW5RglXudk6r2ADD3dKYqfgN_4J1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلیپ کاربردی برای بازیکن های تیم ملی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/96660" target="_blank">📅 18:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96658">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jg81L0t5rVLjKjRo01QujUVTxoPY2yVIaxVBmXnCx6Vdv24UP4YzX71OIkc_hzUeVT6c3VftlklQ8VDx_Cxgxkx_wavC8w-WvjpEbzomb1Jcwdas6BBsf5ZCcl-ZqN9QcJsDhHJiZ3UbNSJAoUbuMx5D5JoYvFxZ_YzADAye-HsGfuBIA_mCtomyOYzzjZhPjJGVUCG0qiNfU-HF4-gWb09-jqiIdE6lqNqvv_yLMG3re0hqE4Z6A0A4UF2wPOlBQqQ-w2sVUCp7SY7lxEzzDNbHD68xEh1fcCXHPQaZ_ZseynqGcE8ftgEiviyvESeUwNxp6YNTv_Xm0R1nPdSliw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YF0F7ou1UrocgRgkEl4GI4aWkAHVO3Ka2sd1JPCCB2LqDloEmN_7x4k29dZ0bKJRHB1BdrVdenm9ksVYctzbBsTmvYR_PJWizSNjBYDChU2YBMjazVbeLHMJP1SV4-xva-HmxQtDUCaI5Ji93vo5GlqIfCykCEz1ACsyEHzTZr8B5xLJJmpdjUOMXlA7-zqVX9SryAV2dssjo4tsMqsPwBA1b-S6IvTq0af76myykf3msxjfQoklWsk5-3HK0EYACXDKep86RNiCI3tRXfgZ07_HfYBzNLAYuO7sB-C1fdZ9KCCFZNMXr-q7eCrYg3z2I4nQWaXrS4rB3SDhUlpzbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
یورگن کلوپ:
یه استوری از سادیو مانه دیدم که عکس تیم ملی مصر توش بود و براش قلب گذاشته بود. از اون پست اسکرین‌شات گرفتم و برای محمد صلاح فرستادم، فقط برای اینکه مطمئن بشم دیده! اینا همون خاطرات قشنگیه که همیشه بین ما سه نفر وجود داشته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/96658" target="_blank">📅 17:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96657">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5053nqvzyFdU1wka6ueSAxiBT8c_cD4MFcYvr0qxtNvdKWmS6-UN7OpW1EmbKQAQlhA4iAErKa4PCCenNJG4Gyzmf_qYcSY36d8R46VhTsdjjOlKZimgP7kANCq1xujnuTo7fZC2c4uKLefrG_wIIijwA8jT3NC9p0ICNyfA_QRx2mxHkgfnbD8zIgHeELHTyESXphE3UE-UpTsi4DOHf7ebBeRNB0tmwHJsiJ2B_YSQlk9YUwvwXwSw_j_ud4iYVpD0wluzmI8zLmKRhvtTqqGHX8gcByCJlytkMvemcZ8LXeERY-4rRpejjCamyvHd9fLcHwJwepH6g4IEtEVHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرشیووار:
در بازی کلمبیا و پرتغال یک فاجعه رخ داده و گل کلمبیا که 100% صحیح بود، مردود اعلام شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/96657" target="_blank">📅 17:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96656">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVxwokcy1bRwVoate0E3bg5vvKNoVakv8D3Yc_Qf3rL_bth2ONAPPEkMh1SC7L-4-ddL8QChvCZ6lWGhC7lnhwEcQfu5DVhX1XjxrCumGQ5Oq1kk3oN5LxHKI9rth9hYwS3LApharem0X4IyXbsrBubaRGrCcU6Bunk27Pqv2LQeYqldRAkw8Z24phDV1aFUfcfsMIabIc5Ul0JN9NN-yPXziA0I8PyEWPLjH140dwexi8bjqlYhIj_QD7pv1uLv5e9O-IMHbynub0RVwbX7AuZppdB8EsGMl3Ij0GjFc0hVNcfWmEeVuxoWUHyJPY6HlwBz_-rXbjQkuDOyD4fCsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان والیبال ایران و کوبا با برتری شاگردان پیاتزا
🇮🇷
3 | 25 | 25 | 20 | 30
🇨🇺
1 | 22 | 21 | 25 | 28
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/96656" target="_blank">📅 17:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96655">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEiuqYOdq0SZd088ahKGbv9NpBkb6NnP9Nagher8PQyJZPa_N28Xoh7dC5uUxVrvLngwN_PuwIU1cIxOtcJ6CWAq-Cz1c0jkQzXq4aMzqKOmbGXJltjMpQudJWp2mlyM5PHvw9oyFRjUo1B1V9GgwhmZZLe9TXm6pApvHygo6FP_7j3XIfB95biogejRUgZtT1Fx5YwwONVZpPrnYPfOVuGiNP26YALBwokC-UVMDl2klxGl1n3X1FymMbX-yjdkdLInq7LD5ENwDfKGGD0PyDl5gs3SgBSLROwhN7YiJef_d8ejHxvHVidHzf6oZeCnCf8pWsw5-Fv5asY7KQ1V1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سراسر حق محمد خاکپور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/Futball180TV/96655" target="_blank">📅 16:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96654">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnAddZWuOYIeXqcEUPcOBDUuPSoE7Y_vIqPtJZHWO4gw9BPNpbJSN2qrpbmF7Fk8ywyD-r0rAcx9YhsPRAHBtCmi6sKB9NPml5wJLh1yib30R8sFzIVQCvUdbgZg0LXEe_Ib4WFJ5gKMg-thWIY2vFaveSI3XrwEhF0ecyki-eM2ystef4wXUf-kNJFqRFuwpR8OQejTnTMm9sDhRtUnhXktWHsbLbvBWBvO5lAYAUIp58QIXwoqc5Bx1UJu1p8DbPN_Vc8AYsC8vYM93oykGel9ixrBmua5CmVgahoNRfHd1fktlhd6VzdmgQPziPJDUhXaD4FI3tQjn3gL0WTIMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
ارلینگ هالند [
🇳🇴
]:
🇫🇷
فرانسه خیلی خوش‌شانس است که امباپه را دارد، کاش او برای نروژ بازی می‌کرد، او خیلی سریع و خیلی قوی است، او بازیکن شگفت‌انگیزی است
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/Futball180TV/96654" target="_blank">📅 16:44 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
