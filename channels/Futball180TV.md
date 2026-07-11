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
<img src="https://cdn5.telesco.pe/file/huH1SWU_PLgyH5k2JruYd6cOsT8i45jhkbxv7sNCIZIr8nuOTWLcpE9L-qNO2UpXxibztjQ7b1Z-GE0YO_qrcmHNYtMzh_qmvgswTbLJhuI3mgIcBLWAbPIC0QW_zm5WnPFwAtBC0LGA7O-oic16q1WyA0IpJS75Na9PKqO-dAjC0AmsthLfutcq2nJOZ0OMr8K79jRwxaUYGU3zYIUGUJaKBlWV_ntGFeeyBy9Xjxm6iyoVwrE4Z8Q_vpcxKdwbFck7m4hIxWs1ai6hpPfBhlPVrscwK7_KmcSbxstWXfAplWOm68xEzNVlTpaT4HusDPqD4olQTQAh21hoaHVp-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 597K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 05:21:07</div>
<hr>

<div class="tg-post" id="msg-99515">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
📰
فوری از فابریزیو رومانو:
👑
- باشگاه الهلال خواهان جذب رافینیا است و به شدت به او علاقه دارند، اما در حال حاضر، رافینیا تمایل به ماندن در بارسلونا دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/Futball180TV/99515" target="_blank">📅 03:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99514">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gi2xn7TvFn-e8-j7tzPg_43W8UV0G_5gpRwzDxAnye7eWV5VOe2WZB2pxe9ImUwzLOoTAQm_-rk_yALN3VobD6vFFqc9nOKICLOIqDkcD2P8-fZu3efPxb7JFqccweJ4gt8WNdV8hWRz7jlLDXtp1Mbh4tuFhfNzGizBevGYufMeuEDpkxRLpVyJEwYO9ZJ08q7lPC1A9rnVLMxp3z6KT2oBh4ekvX4Pn99_I4a_H7kx_-IXP45O_A3BZWNeB9Su0kUxmycKtFiBOClpRabt1MV9g5yHbEVj5Z7mLYLgSAhYgGVQvUkcvbdZyXzWLujyQgewhIZOeBnUssAEMUVzPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📰
فوری از فابریزیو رومانو:
👑
- باشگاه الهلال خواهان جذب رافینیا است و به شدت به او علاقه دارند، اما در حال حاضر، رافینیا تمایل به ماندن در بارسلونا دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/Futball180TV/99514" target="_blank">📅 03:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99512">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfNx7ANWIxc7-LQJuVidzlUbw432kkw1FeeFRackU15ymPtsxVDgQd0nPaAn34mCBPrfCUESjpzKVDzgRxd1tIIOtdpyMpwWTYJhzCEKEiK54cTznZsI8U7AYkD_eVDthbo1lfZT-aY8NbPBzaTrCk9Mn9X88xTi-2ua0mWJg2RC6ur7OfJ8cRDaFegq32y7Vk2sNvSBHQCqBNeYwmmI4SExtIAYsUIc-ECIqA3utfYheupl15zccaw1BbiO2Z-0onuggPWLCiIQfsO5XB-WKmY_EUd2RciCjUX1u9gOgejix94m1E2zw-CqVOSsZTeQrLU0R7l7Mi_KpPHVD_tJZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔵
رومانو:
پاریس سن ژرمن به شدت به جذب فران تورس علاقه‌منده و اونو برای جایگزینی گونزالو راموس زیر نظر داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/Futball180TV/99512" target="_blank">📅 03:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99511">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pziDmPVadVDxwSCuJi86xylSPw9yNp5jX7jeCvdTQ3j58xePPXgOnEoubb2J21Z3fXAgQAxoH-TMF2xvTPWEm0aEGNoxWnZddOU9rH4HQP1SpFaQbdUzU0gZpc1RzaTZVvlG6-cBFJQ4heKz0220yBaOUQw87dniZURg4uwBy1oVldKo_9m5CZ4SFV5D-EUd5eb2bdLckT9q6ySNBK5whrZKo81B81AX_zHktSsBooTKiQDCMgHYVoIBUA-ZTs38HL3VitEu0ibiplP_4FJ0VH7Bn672DrJSTXhPqNpiNfN-8a5CziCWgELdlg8ig5D9tmMNQhUEjm7xcJMb5aK2Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند پیش زیدی بوده که یکی یواشکی میخواسته ازشون عکس و فیلم بگیره بعد هالند زودتر طرفو دیده و از یارو و زنش عکس گرفته گذاشته استوری و نوشته هی یو
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/Futball180TV/99511" target="_blank">📅 03:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99510">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0867b13a.mp4?token=Qr9uFYepKtEmtEhTL9gXwvUUWA3VIScJUEF4pvS78-k0AJhr6NUxSIrCBRiT46-CiRzd1lUqzsxyTlu9TU6zA3jIbBlDsSzPKe-BmCp0jeBRT-t4HtOSiaKyNEfr7dVs3Cnb2x-63pg1Ry_KLmljD0G9jOS_QlWbGLoeYXgt3YAE44dJxcDpGkucpJZDX0RTOF8msxvp9q0kJWEtI-KwN-tf5n2B7WKYjdDgS6JY0p2FDGdtN7GX10lUQVnuF2esFV4xMcGyo9O6fxK663qefR1mGIEhCm0dwbHs_B6WRCeJKPaqENhCsCm9fmeDL6X75Rypk4-lsc5jJEdh4lA1pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0867b13a.mp4?token=Qr9uFYepKtEmtEhTL9gXwvUUWA3VIScJUEF4pvS78-k0AJhr6NUxSIrCBRiT46-CiRzd1lUqzsxyTlu9TU6zA3jIbBlDsSzPKe-BmCp0jeBRT-t4HtOSiaKyNEfr7dVs3Cnb2x-63pg1Ry_KLmljD0G9jOS_QlWbGLoeYXgt3YAE44dJxcDpGkucpJZDX0RTOF8msxvp9q0kJWEtI-KwN-tf5n2B7WKYjdDgS6JY0p2FDGdtN7GX10lUQVnuF2esFV4xMcGyo9O6fxK663qefR1mGIEhCm0dwbHs_B6WRCeJKPaqENhCsCm9fmeDL6X75Rypk4-lsc5jJEdh4lA1pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😭
گاهی پایان، با یک سوت آغاز می‌شود...
🔻
امشب فقط بلژیک حذف نشد؛ آخرین جام جهانی نسلی به پایان رسید که سال‌ها از آن به عنوان «نسل طلایی» یاد می‌شد. نسلی با ستاره‌هایی مثل کوین دی‌بروینه، روملو لوکاکو، تیبو کورتوا و اکسل ویتسل؛ تیمی که روی کاغذ، توانایی فتح دنیا را داشت اما بدون حتی یک جام بزرگ، صحنه را ترک می‌کند.
🔻
سال‌ها امید ساختند، لحظه‌های فراموش‌نشدنی خلق کردند و بلژیک را به جمع قدرت‌های فوتبال رساندند، اما جامی که شایسته‌اش بودند، هیچ‌وقت به دستانشان نرسید. اما بعضی نسل‌ها با جام‌ها به یاد آورده نمی‌شوند؛ با خاطرات، با احترام و با تأثیری که برای همیشه در تاریخ فوتبال بر جای می‌گذارند.
🥂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/Futball180TV/99510" target="_blank">📅 02:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99509">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dN1Uff_9ILyiPEo7cw8ujHxsAYOIm22Jrz6Q2jXqKzuy5pHE5y2TacdxG7sJs1KqnUn7KrE0IADmk-O41bjodp9h9Z97_RW-98Mdhw3HCBZMmESU2_QFD9-5AlQ6JCCqNN_cqr1eIg6oEHQtZhcBC4utxJsODxM6-hIw94s3cfwngqahL9YUzbp6eHcZ7hkqHnrG1t_Ep8KvEkq9zlbLLMhWNR5-PZX3pIMH1kUk8sOUs76Qc6Nji6_2IcWwglR9MmG67aZU4aoGdisdpWAgh2YXL3odNSXNWGa24yeVl5Tipa2U1V6FU24prXMV9Y-3QorXi_gC3Ec6EB3P-3IJEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
طبق اعلام رسانه های نزدیک به بارسلونا، فران تورس از پاریسن ژرمن پیشنهاد دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/99509" target="_blank">📅 01:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99508">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
طبق اعلام رسانه های نزدیک به بارسلونا، فران تورس از پاریسن ژرمن پیشنهاد دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/99508" target="_blank">📅 01:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99507">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pl9snllZUUePjLsclFdwdvSXXhz1b-3wIudxBcVbCHPA76DE2dR1Y6yriWc2IFfGKaLxLuCY5ry5RvHxzHClvG3YVNvTS70MM_p4qxhXOpplyrOuAefn2G2EyHED3sfYzbTl648002iQytrlrfE7wkcZYggx8P0Qnm-vvoKjsp5bhPujV__iRWUDUYD2lFzPbTYZnUJdSXKlGml0aPEbO4HEHbgCkS039_i0DHuzjpO4xCAcTaitvnN2KTvxggwZx7Kd1KXoihU8tzGDQo_NumFsaGAJ5_SbXpnCYiB44IYqUkE4pZw4Q-Jtu68bEZRSnF38LLC-xKFMPnLl6iV7yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
16 سال پیش تو چنین روزی اسپانیا با شکست دادن هلند قهرمان جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/99507" target="_blank">📅 01:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99506">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLXN0HoXo9pLliHkqLdaEj8sK4HDbQCDVa-l7T1pBadMe_hvnz-ZnUDXg2DQLvBk54GQeVcadcSagl_mXzTWwa-FsqGesYecw3WjRZL0NbC4lM-_2nmQHizXfhG-HdimxI2StGXBMcIxe55xaf7e0OCip3UryzLA_UtIbaO5pL5yj2aXN6zpJdsm-LEZ07gOVsUMkrV5wRQi24_smt4hjoIm7xKPf8qqemP-FPCiHvxPzhmfIdV7XsisdL6efTJMfbNEMKB1MRA_DXcbYt56LPjka7A1_kDmqCzQYRpRM1-rSqjBc8o6Paiq5HhpEUd0fonoeijwXD_WDiO_YwLbsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🇧🇪
تیبو کورتوآ: «می‌خواهم یک سال کامل استراحت کنم و در هیچ مسابقه‌ای با تیم ملی بلژیک شرکت نکنم، و سپس در مسابقات مقدماتی جام ملت‌های اروپا و خود جام ملت‌های اروپا در سال ۲۰۲۸ شرکت کنم. نمی‌دانم که آیا بلژیک با این موضوع موافقت خواهد کرد یا خیر.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/99506" target="_blank">📅 01:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99505">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gm_E1hxn6MrrYhYfu1tGX38mg5Itoz0eMhxmtAJcX3EJSOoylTQE0rra_EPYSBC1RHqHsK2bz2Gs-xoRPQ-wYNHIcFGsWsLTUIc0rnhY6jzAhHCBw4dRI5GQMuPRwOPhGuEBQugRrJ_O6scVur92Dc05hhfiv6HOs9OKGjD67CKZLiAWHnqAFNXaPyPTtRAjiTOgeYVAdqYMWsznKXephL-voqHcmZqsCJzEuv64zrWIQrB3uBhCScgw4RS6C0OQi9NJm4BT4IY8VDK4sHjzLWS8GIxeIskcpciLVtJC2Nn1RZjLP5ROXcc1oKmnH-ZNbVXAd1f96NtLnidxppGQ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🚨
🔥
🚨
🔥
🇫🇷
🇪🇸
لامین یامال:
‏فرانسه یا برای بار سوم متوالی به مرحله فینال جام جهانی می‌رسد، یا ما آن‌ها را برای بار سوم متوالی شکست خواهیم داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/99505" target="_blank">📅 01:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99503">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
💔
💔
اشک های تیبو کورتوآ پس از تعویض در دیدار بلژیک مقابل اسپانیا به دلیل مصدومیت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/99503" target="_blank">📅 01:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99502">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqpNpKAT04G9W2yWGC95yAwcvfvDx7Q7EX7OaTJGXLcfW4IFUJt57OnttByk3Eyyjrwe7soxNJMi5znIIeIhMQ1eXD1w7g-N_TgFRiRIeX94uVYn0UCl6Bwu3SxsdelfAsgcRPH1yyhnyueL1i3b_bWUSLhdTkHuRIhJ0D_M1JfOIes05fahsfigqKOYwATPuzLjHl2irgzQ8Y0J-rLN-xO7wUKUa-8qM8mzQ-b5uy7ebo7X0vhu9Mw7VMyHT0VtWlE0Wf1pTaYpClBxEpM8b10vvT0W9QG3zyszPoIwW5pzHvDk2ZGeAeQPe7opam4wiI8n6m9rkgIvrgwhGKf1AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🎙
استارت رجزخوانی لامین یامال: « فکر می‌کنم اگر فرانسه قرار باشه از تیمی بترسه، آن تیم ما هستیم ، چون این ما بودیم که آن‌ها را حذف کردیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/99502" target="_blank">📅 01:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99501">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b961be455f.mp4?token=dEu72Oa7R5uEig2mw7uQelQPnnWEyHJ3fvuoqw8x7ooAG3UpYkJphtkuCgQfiCupdjYQ-J_NrI69nl3Pe_MVKvWU0s5ftaIRnk7eq1XVDjYlwEeW_GuTInSvtvbeq98GWs_JLN4sWzAaeCbOJL5C6Q2RvAnPqRCSHrsOYnCTiuMLLa6_UT_6N1QqgIhjDLqPmagupv0DesUQpjbD76WIDEPvFchrsTuS9wFGWiTh-FLuhhsOs7RKRC6lP-P2LGsHFtaqi6gySQSdjD2XHCzwoC6Z7lX3yrb3RvHdUu6IIywY244WSYPTudoRvNO95P6UnrhKuWqYZj1Mpd9RIxuT4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b961be455f.mp4?token=dEu72Oa7R5uEig2mw7uQelQPnnWEyHJ3fvuoqw8x7ooAG3UpYkJphtkuCgQfiCupdjYQ-J_NrI69nl3Pe_MVKvWU0s5ftaIRnk7eq1XVDjYlwEeW_GuTInSvtvbeq98GWs_JLN4sWzAaeCbOJL5C6Q2RvAnPqRCSHrsOYnCTiuMLLa6_UT_6N1QqgIhjDLqPmagupv0DesUQpjbD76WIDEPvFchrsTuS9wFGWiTh-FLuhhsOs7RKRC6lP-P2LGsHFtaqi6gySQSdjD2XHCzwoC6Z7lX3yrb3RvHdUu6IIywY244WSYPTudoRvNO95P6UnrhKuWqYZj1Mpd9RIxuT4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش یامال چرا اینجوری میکنه
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/99501" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99500">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87d00634e4.mp4?token=S14J4m3IIfErTXe6_6TN9BBHLuJGa0nM29QuLhhl7hJHeg1LhUvd2VtpM-LogPgR0wHBkVLYbSm3mi5HhXA1o1DZuadq1WZlu8SGqbDHexXYpnxnnwrgXsSsC2tn99DM7wRIdN2tvd6a39OMz0iL1INKYoQyMS2z3xHCkKV1uLNkHIh8P2_15StNeKYHmA3125_I3DoM4P1BTQ6fBnv_7cMGhhxzbUQXWJyy1LZ4QM5NqOu0F479GkY-I_rS0XCo3obTEd76ELNN6YsS3Sqsrx27hUWSJa8w43RLPfqG8cH-JhNYszLX0_UcjucAvsgjHPk1j_nzEFdSXOz-q9p-JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87d00634e4.mp4?token=S14J4m3IIfErTXe6_6TN9BBHLuJGa0nM29QuLhhl7hJHeg1LhUvd2VtpM-LogPgR0wHBkVLYbSm3mi5HhXA1o1DZuadq1WZlu8SGqbDHexXYpnxnnwrgXsSsC2tn99DM7wRIdN2tvd6a39OMz0iL1INKYoQyMS2z3xHCkKV1uLNkHIh8P2_15StNeKYHmA3125_I3DoM4P1BTQ6fBnv_7cMGhhxzbUQXWJyy1LZ4QM5NqOu0F479GkY-I_rS0XCo3obTEd76ELNN6YsS3Sqsrx27hUWSJa8w43RLPfqG8cH-JhNYszLX0_UcjucAvsgjHPk1j_nzEFdSXOz-q9p-JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
MOTM
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/99500" target="_blank">📅 00:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99499">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CG3hGOt6vt2ATwBWqHA6PwyQcmQrPit-5CfjDvEvs-GM_K5N50vmtpb1JCX0LRCx0jeigtP1QsgRMSn6JIBXGrvlCLPKhyaK7WIUyGtbt3VZt1s-Q3SwWBtQ_yyfX7uijB3F8tu2h-wCy8a_OjGU5RQ4k7PL7FTyI8HNXv6lFZ6YCaLqQ-DoGTjj49_dETF5FhC1VSM5ljEo6CRtL6xWlnrIo_w51sjHv5JIp8VHhsITGzq_eEvinTp7x1We0cl3PiKWi9uZXa1LiDy3AOdxvJlxGZFjW3tVYESdhIy19WYjNqW7DM0jFTBzbAnT-mnyIuk_rZKjDbGYHxHx4bntyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🤯
🇪🇸
فابیان رویز تا به امروز هیچ مسابقه‌ای را با پیراهن تیم ملی اسپانیا نباخته است:
‏
📊
48 مسابقه؛ 33 پیروزی؛  15 تساوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/99499" target="_blank">📅 00:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99498">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">📊
🇪🇸
مرينو در دو بازی آخر در جام جهانی:
🇵🇹
در دقایق پایانی بازی مقابل پرتغال، او یک گل زد و باعث شد اسپانیا به دور یک‌چهارم نهایی راه پیدا کند.
🇧🇪
همچنین، در 5 دقیقه پایانی بازی مقابل بلژیک، او یک گل زد و اسپانیا به نیمه‌نهایی رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/99498" target="_blank">📅 00:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99497">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQw9-x08b7-dzCEsaYxfWP3vV8-lj_xKmH3Q3_oq77AHVfSYtGUWWq88xq8fW5AWtUS9PGLwvmvGy0TytnnaWHHfs03r9nQ0nCxF6Symn9vRRF2M4Lr3Q17ewAWiq4WWa2uNiriDdqmhCgQ11QaqVhb6sTkaZS2nBbNqDmRhhxhvOU-cUMmrS7kao36EBQnPaaACqIog9V78A4y0N_mrNhHSXdbnoNb6np7rNXk31lZ5j8rArKbTBG4XriIolEj-s7gd1_gkE_rg-O3sLO5rv3LGya8qUtZYxe-VNgR3i7PfoXx3jkSQywMMiILpF0C87yCd0NsvewLLS9VldOGQ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🔥
اسپانیا با پیروزی در این مسابقه، برای 36 بازی متوالی، بدون شکست باقی ماند و یک رکورد جدید در تاریخ این تیم را به ثبت رساند.
✔️
‏آمار این روند: ‏27 برد؛ ‏9 تساوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/99497" target="_blank">📅 00:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99496">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/Futball180TV/99496" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
اپلیکیشن اندروید بدون فیلتر لنز بت
🚀
🛡
ثبت نام آسان و سریع
✔️
📱
اپ
ل
یکیشن را روی موبایل اندروید خود
نصب کنید و بدون نیاز به
🔤
🔤
🔤
وارد سایت شوید
💬</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/99496" target="_blank">📅 00:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99495">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ZWOSisUuQFXXlIyBXUs34SLKCDjnN0ewF1L4EeGxp9f-gRf_sw10GqVj1_7BRt_Fiujqje9QgZDylzPHe_F1MjenYMufJZPVCdcrf8u-76MP2cWMDb3g-9Oru5GITRN4jPkMLOxq8qXHq-mA84Qf9XxdttZjgMbTuJX1goHmqLadendVWNlPCH_x6cdenk1XM-xAMvboJuSpv5tEVOc7qtLAbl1vvNRbSSbiR_MPoOSFfQ9zkQU-rnMc4Q75ZohmtD_z8653qrOZL303XtPWxoOjcn6Xs66Nk65bPmn-OeSXbeimKjiFbMrit0UvT7D-Bx_2qZt-uPDQdtJkNFeEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
قهرمان جام جهانی ۲۰۲۶ از نگاه شما کدام تیم است؟
✨
با پیشبینی قهرمان جام جهانی شانس چندین برابر شدن بردتو امتحان کن
🚀
💥
متنوع ترین آپشنهای پیشبینی در
لنزبت
😮
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
برای هر واریز
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
🏦
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از واریز
🔣
0️⃣
3️⃣
کش بک هفتگی
📇
امتیاز وفاداری با انواع هدایای نقدی   روزانه مخصوص کاربران فعال لنزبت
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
📱
@lenzbet_official
A19
📱
https://www.lenzbet1.living</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/99495" target="_blank">📅 00:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99494">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOjMWq2tf_H4_Lv3fDjBLZ5VKkfZNJMtos6vfHxyPgNFv3i8qgKhmj-O4wJ4HXN7KaGc01kMrXbelCN3buuvbDJnLnMlZGv-GmA-WI2r5uuC_pyi68V69SIiTkCBbsFru4mai-Z-JfB-G-pWcRkA6G_1t-YSQITteN-DUL1BqJ4PhkvwuZtWXpiNq-DVjgkVUSXRPYevG3Dfp1lzzXIF8SUofhrhWUHfQavuUPuy-054vK12_twlj0sVqAVYCTY3Rne0_MciQhAVqcTW1vq4W3eqOFlq-eORRSsH_Eri7PNZbrZOVsDAUTdUulyCJ_hULszm9BbsIuJ3APjM_nvfog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
در 11 بازی اخیر که لامین یامال از ابتدا در ترکیب اصلی تیم ملی اسپانیا حضور داشته، اسپانیا در مسابقات بزرگ (یورو + جام جهانی) پیروز شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/99494" target="_blank">📅 00:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99493">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
؛ دکلان‌رایس، مارک‌گهی و ریس جیمز در آستانه بازی با نروژ به تمرینات انگلیس بازگشتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/99493" target="_blank">📅 00:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99492">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RA5ESzgKnIztBhRqr-P2qRtk37LwWeYN89CqHhDUe918HrE-nE2BIMOePnNMruf5mjeFPZK7gX6GjxQ0ZWI2UW7-mIxfLobhw91_MhDfwDcGXsRL6Ozx83zvEyteHhUofJvlYNwO_7yAUFxpbgqfDG2byOYCVQlu49QJfjb4EI4qOTc-DnPZ6D3XFSaKnNZWGY-esue6XPqiuQRKxPDi_K1-bQKzff_Ev9X-7xO11IO0_Dj0kw7Wxce0vz8Mz2NTHuMNJpiXoaSsTZSYWD6876uItGGNzY52Q_wcjDllVIEmw2kH4uXx5K4tvqPvBkVR3KxGR8RWy7fyiPJkfy2cdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
مرينو در دو بازی آخر در جام جهانی:
🇵🇹
در دقایق پایانی بازی مقابل پرتغال، او یک گل زد و باعث شد اسپانیا به دور یک‌چهارم نهایی راه پیدا کند.
🇧🇪
همچنین، در 5 دقیقه پایانی بازی مقابل بلژیک، او یک گل زد و اسپانیا به نیمه‌نهایی رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/99492" target="_blank">📅 00:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99491">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_zTBU8yaR-g0_kRIetrvAKwGRl4O1JLIxHoiPfS9pDiCCCr6K9krbjw7WfXR3SlVynnfViSW0mar3rJeHMugikxeBF5jI92tdjKqv73Jhica_OQ1xO9rCe4tUgzXMQV-_J8_SU5PUPxRtJ4QOK6nKMchpA-cnVv-cMfDruI64xqN4oPHa21i1otIwYM6cQikLozaAhsjvwZAw1IpvlwktAj85A4Ds5oLwkxn0wTCcIuCcDaPr9baOjk01inFqQ-TnifiZ5-zw8f7rG64tMGBd_K2FWJ4GOkhIOdqB2vIzk3JVqVWF1c6jE6OH8oZ45-7TijuuXif1zY34ihk4DzUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اسپانیا پس از سال 2010 برای دومین بار در تاریخ به نیمه نهایی جام جهانی رسید
‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/99491" target="_blank">📅 00:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99489">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eEKuBEDmLpITb2pWEQ2xVwAwyVKGeP3Gk-UEAMyq5pxTCor_znyBP4Kob61J_IvleUE1prGi0Aqukv5ohNxBeqd6dzbx8mj1OqxZbwuMaM5WVqJ2XXjUE0xfzzPNBt1qA17C3SQu52YK2l8hDwhMFXfPIsqgmXilfKhilo1tlCQifuRHF25YP0g4xgEM8zTP87CRGIN0RKjHGSxdAX2VdpWIXe3jZwqbK9Ivo2tSXC_UrgBU4dw4BovIVggjbwoj5qwS7jZnFlLPlFZjCjFo13Atpq2h29xi9o50bfF6lZAudxB2agoRDWL8q3WhnkiDWE6bPtWFI2McODzNyU-9gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PT4oPHZOB-3mQTEQp5flg3xWq9C_uv0iKmzMw1evXkeTZk0gAW-3C0ysQ-MS7gCfvrsWifVKS5wZ4qQMuZEGuhroS-E-bnOwv0GS5kJ2473f4ihQazHk5Lfhu41ab9w01RQrLVz6hWxLb7j6Fi6p6Fzjati2LkOpLiEpTnowLroagbzpMdthcu4n1P2OLV_Loxcq5BB6Q5krjxp5LhQZ0nhtjahSZoB_yinLGmB0jrDHdktIYXZOoS_B-80ik3JBMvXl1E0vuy4d16tWIB0OhEX3nfx5KatszxCkEs3vop6Kq7cXSZvi9K62Eb6EptB7ZbbpS7YkTIP81EMfv0ZyGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">داش یامال تو استادیوم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/99489" target="_blank">📅 00:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99487">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1PySIOxGD9yMdHPu32e37v68Mpapoo6XaqR8s8Ck5SIUcBNL2mpZtZs9s5tq47d6BUTw4rPbE4alafF84yVOduY4VbcT9z6mcjJZPN3-aQtZClngzkPob1lIVG4ZbyHhtyf4l6dCL2RR7D_ic_W_KCKymGe_xN-4MnrfNpLLoC26wLnv4LE69M8D1oFWvY-2Ft_rXs6pSHT-YobPSTJtDZHzw1Drq68TKO1p6dKe3nrcf9MhRskoYZTZ7U32l4MfOiCjBy5-7rKIXAwbdpquyRb7_KViPSTIl-6qmYbl4KzmDPn-0rEe3aDrHdHP1b3I-A1SiejJBwvCxBQ0nvsIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
🏆
🇪🇸
آمار بازی امشب بلژیک و اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/99487" target="_blank">📅 00:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99486">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnyQ_dIq1Vpf1hM6K8RYA7iiHlzyxuImXHu0CxHSq3o-04m6WBdQyRgIwSdz7coihDD6Xzd0Uf_rIhA-vNj2gfy2KLWmnZWuYgxSSyOAaprWotwZUWqdnhOx80JQRsERVP-2bqdE1jdC3F6L6q-SyE_MujJ8g61bypnRvyhc1IteaA2XXn1nH-v6jwa8CCBf0v2DtIcvQvlYW48fY9rL3vNP6mL9y_AOSYDkxlTA9xfa-mvthwgm6bZ7ReXzae8tMsGEtjw98fuAj-rmOhwpKoPEhk_PPWMToesxlTwgo_2PHsiFPcXvcSVcoMcv0JlBYqux12zMRt4EbSVZMklYyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار جام جهانی؛ این سمت که واقعا جذاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/99486" target="_blank">📅 00:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99485">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiU_9nnOt43V0idmBkeHKF18SuGl5I5XPhdy6I945IAskE14n9pFhggfYvJc_-l81bNzBuBWQT_seafUu5ki4d6195uWadnxZuRAsjPI15Ayw_NW9t00kpnoMwG-FjK9twP6guNAQr64xbFpYCQoCZKD5o7xi2aUShT4tEeYXkNpw7fzRw5hB7KXdTSv4DU3cFtW962Fh9K64Udpsrqf2eY6GK55g0etyV7EwPdpwIEqrtkC0EJKcdWx2-ZvIIx1u5lFIEBU73FiddMENS-qtdu5GE_v1jqXa9xT-CS9gaoHNIU2qfGouEw84LWXYJbarNRbCkiaI8gkJQ8IfBFedA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|داستان اسپانیا در جام‌جهانی همچنان ادامه دارد؛ راوی قصه ستاره آرسنال است! بلژیک در کمال شایستگی حذف شد
🇧🇪
بلژیک
😃
😀
اسپانیا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/99485" target="_blank">📅 00:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99484">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVyoqfNZ6-L5FZhszf0YiC2KdFH8tps5DWv3yU1oP9WP4SqVRjhk6U5ret9TC5vHlhkIcSmKp57WE2SorZMiqOB3VH31n0XBSCzg0LgMxhZ-EEwhMJOrPA1bPZCBuFgzSthKXBaODWZdLEYFUeXJJw75a64So_vyXE8Lv3ZApwfpHGS0ivBPLv-HbaYsZUqxRSaq9I2PhKWh8X43t5ZvLDgjGL5akYOB9wmB64JCkA057wNBeuVJ23uL8Ztqewub8GmWz7VoqeXU7f3UTSf_RuYWLW-CTXPuAYmUIjMAFYt4uZl2tMb4ePHE2l-yObZOvQyz8JoG_ywZDc0EEdlteA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
نیمه‌نهایی جام‌جهانی فوتبال
🇪🇸
اسپانیا
🆚
فرانسه
🇫🇷
🗓
سه‌شنبه ۲۳ تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/99484" target="_blank">📅 00:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99483">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCLgKddncrHOZbaWfu_R98jcXaIsi6qemro2egKuVw5YSRvZ5zkQvI0o5Y_zilyQ794O7sHvZl9EQ31elMeV0yOE-YefyGQW5l_UtP1fYv_vgNwOSjeBn7O0XuqAGGIoCBmoidsmZGnsAL6drLHOXW5w_LZKfWaaWR6UJ_5W4saGIAVkldTM9ENETFryC0oL7mul96ZSA2tM2ANn50XN1V8QY3jypDA2pHYtZNNy4S1JqZqXxWDbbZV9MoOnZIQXRFWvbpGc2BMaMm4TgRNWW0sXgcr7QrhWvx5BJQUbgd1lMSSmI7A875qTR0VkvGYCIPenlAbp3OgcVNz_lmrVag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|داستان اسپانیا در جام‌جهانی همچنان ادامه دارد؛ راوی قصه ستاره آرسنال است! بلژیک در کمال شایستگی حذف شد
🇧🇪
بلژیک
😃
😀
اسپانیا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/99483" target="_blank">📅 00:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99482">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پدری ریدددددد</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/99482" target="_blank">📅 00:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99481">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">چه توپییییی در آورد لاپورتتتتتتتت</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/99481" target="_blank">📅 00:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99480">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/99480" target="_blank">📅 00:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99479">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">هفتتتتت دقیقه فقط تا پایان</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99479" target="_blank">📅 00:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99478">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بلژیک اونجایی که کورتوا مصدوم شد بازیو باخت</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/99478" target="_blank">📅 00:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99477">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e4b3fe7a64.mp4?token=PtjeS38ETg7GFwUek9gDST3nlTl9nHfyFfhFdGnPrQgFhAUq-EzP1KeyVR_HbQY3SS2hY-wWjQyK6sUON-MmOKrDX2Rh3qQFAVfuhUXolB6NiESQIwF5PwdIboEV7palqwSlLXA8Vy40bMPkWP89BZGwBxCTxDF1kV8KvNhqOcZMsujN9rFYnZOZEHMSrHf2EXDy2khA_lwstc5Q0gm_YpVHOVqRqgkZO8M55-Y83MRAkv1kfR70-edW-g3P3KfBt-Fek-2OWLrOGLCGuGIqlh2y-TeDFQdcegGOudUGQk7T9Ru9-tIe54oNR0tC8gJzYr1Nldx5GTY9LXOEyq9b1XGxNgGyWrgFA2kDrnO8KV8iR1ysqttE4ghLSG5yRuVGiQ9dHBFEm3KYIwk46myIE9DD2OnrKFEgSpDf51agLAJTEc5AvnGsFzJYtlqv3HjpnxSEhJxg4FG27O7jh8TOievHm8xWj2e6MYUiE6tLU0VHYX_4ddvFgFNbV7dv6nsK2j9aJEs2jPfEhhhfe18Lp32KP8huA2XbLyA1rWENczHZSooAN9eu7IAGJflcLOpqikeF0zuO69v7J9X8mgnhw4e1QKbyE1BxKA7rVH3gZPswvax07-o66PF-K23OeP_bN9XqX8Q3oVdESxFsy2iB_3BYaGuodkNZLNo4yC909DU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e4b3fe7a64.mp4?token=PtjeS38ETg7GFwUek9gDST3nlTl9nHfyFfhFdGnPrQgFhAUq-EzP1KeyVR_HbQY3SS2hY-wWjQyK6sUON-MmOKrDX2Rh3qQFAVfuhUXolB6NiESQIwF5PwdIboEV7palqwSlLXA8Vy40bMPkWP89BZGwBxCTxDF1kV8KvNhqOcZMsujN9rFYnZOZEHMSrHf2EXDy2khA_lwstc5Q0gm_YpVHOVqRqgkZO8M55-Y83MRAkv1kfR70-edW-g3P3KfBt-Fek-2OWLrOGLCGuGIqlh2y-TeDFQdcegGOudUGQk7T9Ru9-tIe54oNR0tC8gJzYr1Nldx5GTY9LXOEyq9b1XGxNgGyWrgFA2kDrnO8KV8iR1ysqttE4ghLSG5yRuVGiQ9dHBFEm3KYIwk46myIE9DD2OnrKFEgSpDf51agLAJTEc5AvnGsFzJYtlqv3HjpnxSEhJxg4FG27O7jh8TOievHm8xWj2e6MYUiE6tLU0VHYX_4ddvFgFNbV7dv6nsK2j9aJEs2jPfEhhhfe18Lp32KP8huA2XbLyA1rWENczHZSooAN9eu7IAGJflcLOpqikeF0zuO69v7J9X8mgnhw4e1QKbyE1BxKA7rVH3gZPswvax07-o66PF-K23OeP_bN9XqX8Q3oVdESxFsy2iB_3BYaGuodkNZLNo4yC909DU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
گل‌دوم اسپانیا به بلژیک توسط مرینو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99477" target="_blank">📅 00:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99476">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مرینو عشققققققق</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/99476" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99475">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">چه شاهکاریه این مرینوووووو</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/99475" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99474">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گلگلگگلگلگلگلگلگلگلگلگلگللللللللللللللللل</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99474" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99473">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گلگلگگلگلگلگلگلگلگلگلگللللل</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/99473" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99472">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گل دومممممممممم</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/99472" target="_blank">📅 00:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99471">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اسپانیااااااااا</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/99471" target="_blank">📅 00:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99470">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مرینوووووووو</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/99470" target="_blank">📅 00:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99469">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گللللللللللللل دوممم</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/99469" target="_blank">📅 00:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99468">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گلگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/99468" target="_blank">📅 00:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99467">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مرینو عشق پرتغالیا اومد</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/99467" target="_blank">📅 00:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99466">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6497dfae.mp4?token=pjbjVISQejHRto4x8zm9UteYGcuQfqLTgH99IMPEv2pdWzyS_7brYjee8FiJg-_ZhgnpOgdi83TR2fdqY0qyWB5seU2WXHNYj9668yh4wB_-GAJSw2nCswUMseUSCe7e3og0buqGfr4KlTbfVOD0qfub-zdkgyRMwovLDDCpnqPqxx9owShE_lvIQFAj3Ao954uN05G6io92PLJ_8WlfRsBEkSRtZaUbBb5hW_7IHZYKLRAnyx3AvzYdGpbohqyolC9iTqRDD1h4QWfCbcMGLfW8qqDUKJF2XOrmM6oWoeMZXUZeDb5iedbys9_vsFMq7DSfhuGrnuWPyrEmIGbfoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6497dfae.mp4?token=pjbjVISQejHRto4x8zm9UteYGcuQfqLTgH99IMPEv2pdWzyS_7brYjee8FiJg-_ZhgnpOgdi83TR2fdqY0qyWB5seU2WXHNYj9668yh4wB_-GAJSw2nCswUMseUSCe7e3og0buqGfr4KlTbfVOD0qfub-zdkgyRMwovLDDCpnqPqxx9owShE_lvIQFAj3Ao954uN05G6io92PLJ_8WlfRsBEkSRtZaUbBb5hW_7IHZYKLRAnyx3AvzYdGpbohqyolC9iTqRDD1h4QWfCbcMGLfW8qqDUKJF2XOrmM6oWoeMZXUZeDb5iedbys9_vsFMq7DSfhuGrnuWPyrEmIGbfoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
💔
💔
اشک های تیبو کورتوآ پس از تعویض در دیدار بلژیک مقابل اسپانیا به دلیل مصدومیت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/99466" target="_blank">📅 00:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99465">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uN8MJod6E1NEcBGBpSDxW_5HoMYL5d8fbKwEmXqBEZ41c_AohbkpJtG-1sGXHPKwsm_o45bxHLeRntGcfSykNjs3RbVih3DOuHMqrGGJ3hgqhHOhEYzsNhOcZA9z5PFU-CpQBq-c0EgD47ip6U_qQ_hfl24KmBV6GxmfXEIRbtP1wElNYG5hZHaVYCqifuFGchRmqj1dexsEl-XuFK4Ycu5zA6_7rcVOX19YW_5qG9MuaU_2LFMebIM9EPgD7BhY-WvrOg1t5f6GPh0CJ4Hdvgy_WbZDa8OHzNOS1xNMX3Mr2NYfUaGMxvBVPwQtWp9lwriYBv_M4Jitbp42L5NdUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گریه‌های شدید تیبو کورتوا
🚨
🚨
🚨
🚨
😐</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99465" target="_blank">📅 00:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99464">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کورتوا تعویض شدددددد
😐
😐
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/99464" target="_blank">📅 00:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99463">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دو تیم خوب بازی میکنن</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/99463" target="_blank">📅 23:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99462">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بلژیک چه ضدحمله هایی میزنه</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/99462" target="_blank">📅 23:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99461">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">آغاز نیمه‌دوم بازی اسپانیا و بلژیک</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/99461" target="_blank">📅 23:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99460">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
❌
📰
فابریزیو رومانو: انتقال ادرسون ستاره برزیلی آتالانتا به منچستریونایتد منتفی شد. این بازیکن به این تیم نخواهد پیوست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دلیل لغو قرارداد، بروز نگرانی‌های پزشکی پس از انجام بخش اول معاینات پزشکی بود. (این نگرانی‌ها به ویژه مربوط به آسیب قبلی زانو، به…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99460" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99459">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇪🇸
🏆
• 10 گلی که اسپانیا در جام جهانی 2026 به ثمر رساند:
6 گل در نیمه اول.
4 گل در نیمه دوم.
🇧🇪
🏆
گل‌های تیم بلژیک در جام جهانی 2026:
‏4 گل در نیمه اول.
‏9 گل در نیمه دوم.
‏1 گل در وقت‌های اضافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/99459" target="_blank">📅 23:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99458">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jh-JF8mJqgrp2_yqLMYg-zEE1hJb2T6jKQR_qIukYiluTHoUUDJbvq9ok_iqRbU3Qvm1YVCVzmuykUKj3JiDZgdPYJYAy53AGAo0Y40OgkGuf9ITvlXB72qMEaNnEvrNgWFsjo5DfQsARkBVVglB-4bAqagmxBhx1Ns1XVswQD37pTXPNPMPLUmSkm1sop9wZzpDis0gI8Ur1HTqWary9rbsKmGVFtDnMeMRPQVxJn-pGPWw2GOGbOoGrC6AC0RRANzijT9DBvGPj9D5xKFOetzzfdAT3TO9t0WUTSNDWzXVy2hm5uSV2wvUlsDaRErBvhHW7A05XhOtZte3fx9HIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇧🇪
دکتلاره (با ۳ گل) به عنوان بهترین گلزن تاریخ بلژیک در مسابقات حذفی جام جهانی، با روملو لوکاكو هم‌رتبه شد.
🇧🇪
🇧🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/99458" target="_blank">📅 23:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99456">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
پایان نیمه اول؛ اسپانیا 1 بلژیک 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/99456" target="_blank">📅 23:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99455">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🔥
گل‌تساوی بلژیک توسط دکتلاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/99455" target="_blank">📅 23:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99454">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گل تاییده و موردی نداره</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/99454" target="_blank">📅 23:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99453">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">چه ضربه سر خوشگلیییی</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/99453" target="_blank">📅 23:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99452">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مساووییییی بلژییییک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/99452" target="_blank">📅 23:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99451">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گللللللللللللل</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/99451" target="_blank">📅 23:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99450">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_-aX9lTnltL6x27hwuSgaDTPzk1qSeXA17P009b50KvwfepmdFM1xQ2M-TJuMb-5kapxpUxVC_Q9WXBo-UTL0HU3tqnUvlEwm_LwJ3tZfdwrTVCSd5LH4m-cVdyfpXR_KM7-k16cQfyqzRPDKwvt8tUZDvYYA84m0EyAXN86d1AIRQtJRBD10D84BFnLlBok00wHiU-cJCkWv2CenDaYqnkImoEtNoZKaxJq4BIx7kARUxZdtUzbZDoDO6S2bdNR-memNG7WqH77hA9DajfQJ5Q5nhW3FcSPq5dT559uLGvgOuYwU0QdeW5mSk8__PCEb5hkezm9kS3GRH5wnx3fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور برد پیت تو ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99450" target="_blank">📅 23:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99449">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خوشگل سیو‌ کرد کورتوا</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/99449" target="_blank">📅 23:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99448">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">چه خووووب زد</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/99448" target="_blank">📅 23:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99447">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/99447" target="_blank">📅 23:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99446">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">چه بازی ای میکنه یامااااال</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/99446" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99445">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یامال دفاع چپ بلژیکو کرده قشنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/99445" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99444">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خطاااااای خوش جا برای اسپانیا</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/99444" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99443">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🔥
گل‌اول اسپانیا به بلژیک توسط فابیان رویز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99443" target="_blank">📅 23:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99442">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اسپانیاااااا فرانسسسسه داریم نیمه نهاییییییییییی</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/99442" target="_blank">📅 23:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99441">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ببببببه بببببببههههههه</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/99441" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99440">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بالاخرهههههه شددددددد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/99440" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99439">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فابیاننننننن رویزززژزززز</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99439" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99438">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اسپانیاااااا</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99438" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99437">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گللللللللللللل</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/99437" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99436">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گلگگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/99436" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99435">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEYvYQH4a18trmPAM3INIl1uSH2sgFjUMIwVo9sPsgJjcKnDgha5N4rZUY9qHqQFbI1b0EB7KxBdexCcbGlBlUliikPiyXjMbGgJ5XC4OWpWPKSlSD0fH6HJ-iD5J5bwYjuHkGm3sAIOExFl497AsJBRrJfnal2J3j21g8K5h4ZppQhz8PGYAbL18Q1i4KXkQJrNI-nUewR5n3nPwYdezk6eVpgvdula1o6MNMcZdwYkWbHUAxJcECHJyz2tJoVFAiE51dxzXqe8dRwp8UzE3l--pU00r-yfhdA25-3ABk3VI3QqqL4yaan12ZoxgSsxNlCIXO3HN7JjvgHuXXu67A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
#فوووووری
از آرشیو وار: پنالتی اسپانیا مقابل بلژیک گرفته نشدددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/99435" target="_blank">📅 22:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99434">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAewh6dhZU5la-q1xapnxhw1OQW3vyqKBu1-ZQNm0h4yKONJPs_YcTR02Y4oG7dJIMm1uMtQ1jcsxBz5LJhIwfFLA0tJqjrLcUoNjbJaWqJRlDnN0wLVLT1op1dW6YqcpZglIoPOV1DWfPP8c13_DY9Bh3JS0vWW3D48HLYmuSSpKMKiDzBZJSlkYZT4QHRqyLDuNeOtbkGZjqYOMTxcPwJfatcaTSxhtrZL2lMj6HYoA23rNa0qVxcswoHcgRQAx33Q4Rg6RfDCRzhx_PoJX2pRRXbU17sxhT80I3RUni6TL8ctJQQMQe49hITJ1FymR36mX-_SFlBaIXXJki9Egw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
پست جدید رونالدو: یه پیروزی میلیون ها میارزه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/99434" target="_blank">📅 22:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99433">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5C6afMWdSHl6CfLhV1TKtzB2Q_2nEtmp9JRxPc4bZOiWrmZOGoyu3vLzXADew_Hfsd2FTiiwc0d9LKjj4CHwIDmN-27i2uPKg9PpM3I3sXTkPWdx9h6TJEqYUOFy25PEeGNw8kKgQ6LWxgOKSD_ZM3sGGpgO0jo8ZJv5s1ZPWSSHqdqryVYfYgwOSPFbgpTCU4escIyndeGbwFDZtJFkDNflEBxuseXYvBuRIepeAAASPcNbysNWqsb0-rHmiPyadXHPr3bVNx2-jXsQkFEoIahyI3UtQy_aINiBW0klbMR5uahtbFLu3IzsdLhcmLYWOKQKV1iAizAsdvGS10ERQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوست دختر یامال تو ورزشگاهه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/99433" target="_blank">📅 22:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99432">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⚽
تحلیل دقیق مسابقات فوتبال اگر به آمار، آنالیز و بررسی تخصصی بازی‌ها علاقه‌مندی، این کانال برای توست.
📊
تحلیل قبل از مسابقه
📈
بررسی آمار و عملکرد تیم‌ها
🎯
نکات و دیدگاه‌های تخصصی همراه ما باش و مسابقات را حرفه‌ای‌تر دنبال کن.  @bet_maxxx @bet_maxxx @bet_maxxx</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/99432" target="_blank">📅 22:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99431">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSKl6K7JBTK096YbckijnizYic9Ch99J2cjyma5QXDnhMLg-s0n_GhLNax1gwTOWhK5aSHj92mSvFvCIeFYtYk7mjD4cLHJO3mQ6scIp5ZY6WdcRH4srn7lIVP0VuRHaVQb_wv3oEXp-6KIVZQitvLLikjQCUQyXmFNt5PG3Lt9JBKQ_RGU8KHvgBxUob6EdWfClirGzMe3mEPB6ulSkKq4QUsJoAsqBdUqso8L5mJwctXkdoUHvhsj7z0DNnQClpMx2sVwpDcocOoNIhk9ZGjZFcvXx6Ty2MB6eWktgx8cx0qyQvFiJX2T3OQA7GAWb_qG3_rqVc2XzY-wCjE9yrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تحلیل دقیق مسابقات فوتبال
اگر به آمار، آنالیز و بررسی تخصصی بازی‌ها علاقه‌مندی، این کانال برای توست.
📊
تحلیل قبل از مسابقه
📈
بررسی آمار و عملکرد تیم‌ها
🎯
نکات و دیدگاه‌های تخصصی
همراه ما باش و مسابقات را حرفه‌ای‌تر دنبال کن.
@bet_maxxx
@bet_maxxx
@bet_maxxx</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/99431" target="_blank">📅 22:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99430">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بریییم سراغ بازی جذاب اسپانیا و بلژیک
🔥</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/99430" target="_blank">📅 22:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99429">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇧🇪
ترکیب بلژیک مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/99429" target="_blank">📅 22:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99428">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDqUO7jevOOMQ3JKtqpCEerlsZdVLn6T5L6iqZ4SIzHPsBfCHRP98exfS-r2gDD3BHYg6yJiANEnZnXAS7foJLOy-WxUadPFo6TL49sKUckcTF3MCiYO-iSyZTKXSdz9d5B0r4Ss7Fl7k-knK9jjia6gAPd6OfY8nftFY0MGqGn6djE2NFTyGfQ3l86T0ZSguO-LgPVWzF6itb7Xj61tqj6WMekMa-2VcbG8HxsPntsnbJUHfrZ__0QCOqS8-6ABd6YZRSmAgsq0w01hrkqLgqTC_Zf4V6wNFTVD__Tke2t0NRY5xuaK8VEn2NAn9janagUcTwBnQifxMbdZ2Q3JSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
📰
فابریزیو رومانو: انتقال ادرسون ستاره برزیلی آتالانتا به منچستریونایتد منتفی شد. این بازیکن به این تیم نخواهد پیوست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دلیل لغو قرارداد، بروز نگرانی‌های پزشکی پس از انجام بخش اول معاینات پزشکی بود. (این نگرانی‌ها به ویژه مربوط به آسیب قبلی زانو، به خصوص آسیب غضروف مفصلی که در فصل گذشته (2025/26) رخ داده بود، و همچنین تردیدها در مورد سرعت بهبودی او بود).
تیم منچستریونایتد از نتایج معاینات راضی نبود و تصمیم گرفت این قرارداد را تکمیل نکند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/99428" target="_blank">📅 22:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99427">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoT0mcZUf8Kpx05xOeP-clQuUDt98MG7wMUut_BlBRGopnlXCbRlkX8HJrLpC9vkN5eMa_ggHAi9vjQjiGsdQHOLVa1GOYGlZdFD3wHFU-WAnpldq_tZe_cXsVXo3KrIkdTd0KCZzUlG-8ACu6sr4IeavRL6OgSgoTPSjFOmEYsMfLd8HsEgJn-sZQdt6Veyiv8SMZKmChplMO3RTRiLo6FkGwA2BIPhix3dnwXxvSKGGYiurtKOXZcHLY21xqEmFm-ThRL-qkiRU-KJ5z1f8Lw_XiJC7jt2bJDFrS5fZ02T2e2NwS88PO46DnEisyhYayjvie_KO1b6GIlRA2KV_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180 #فوری
🔵
علی‌تاجرنیا مدیرعامل استقلال در آخرین صحبت ساعاتی‌پیش خود با سهراب بختیاری‌زاده اعلام کرده که پنجره نقل‌وانتقالات آبی‌پوشان تا ده روز آینده باز می‌شود! هرچند به صحبت‌های تاجرنیا نمی‌شود استناد کرد اما باید تا اواخر تیر برای اتفاقات…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/99427" target="_blank">📅 22:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99426">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a87c3f99.mp4?token=O3D3WBg1KluHjJHuzm70RCg8115zus3ecwPEul1gqibO1b7YJuoXwZ0nnL9BcBbKmRbzvmoMzKThgFgZ8Sp7gK_6R5AZEjAvZo3r1o6OdZ6U3X36TVUgiB_Kp5fYr1VYMEcLP0QWZdxYl0XdCXtp8QNjunaSvZHck-GfegalOtmLX-tbZkz0OrStFeJv-pBpBZzxGf5dsJBaf78A9ro3CjOkVzoYZ0no6GW10kXfz8Dvp3waSa57RL5F1iQ17wTzN6tonpx5-XUmpr03QBtjaauZi-uB7vmwjJsuSRZ76e32Ca-yMfWzaFBTXsUHr0UMxQLaW0DHKqvqPDiK-RbZew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a87c3f99.mp4?token=O3D3WBg1KluHjJHuzm70RCg8115zus3ecwPEul1gqibO1b7YJuoXwZ0nnL9BcBbKmRbzvmoMzKThgFgZ8Sp7gK_6R5AZEjAvZo3r1o6OdZ6U3X36TVUgiB_Kp5fYr1VYMEcLP0QWZdxYl0XdCXtp8QNjunaSvZHck-GfegalOtmLX-tbZkz0OrStFeJv-pBpBZzxGf5dsJBaf78A9ro3CjOkVzoYZ0no6GW10kXfz8Dvp3waSa57RL5F1iQ17wTzN6tonpx5-XUmpr03QBtjaauZi-uB7vmwjJsuSRZ76e32Ca-yMfWzaFBTXsUHr0UMxQLaW0DHKqvqPDiK-RbZew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید سیتی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/99426" target="_blank">📅 21:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99425">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فکر کنم کیش انقلاب شده خبر نداریم
😐
@sammfoott | پروکسی</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/99425" target="_blank">📅 21:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99424">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1w4rdwGpDn4u2jbm9Cu83TzzmiEffqVWP40TcXPgFGjoaPDjGluwXeUJo72RPH0gHTXXaxxP9Z5jepCDMrtvVUhz5eQwOCT6wEtPRt5FYOOG3pzAzKhXSCsfY3dfPeYW1FZYY8nc5r3qa1wTDzbqt4gK6AIV0kj6oK58-Q0OWPUtzakbHwFw1DGiGIvAXloudD2bKaCfeXs8kaUH7ZgvcHyJYwrHxGfdQSiTLewnRIms8U5DJPCdVwk9vilK2GmYIZJRAMzNx27QhNrD2oU8TIr_b9VZcFU3lFzQ8PHleFU1ORB7QviuDivp_gJ7wo4960_2ENgrrFCVSv-KoJTJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فابریزیو رومانو:
هدف مورد نظر بارسلونا همچنان خولیان آلوارز است. قرارداد آدیمی، تاثیری بر تمایل باشگاه برای جذب یک مهاجم جدید نخواهد داشت، چه خولیان جذب شود و چه نشود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99424" target="_blank">📅 21:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99423">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHohJ0E6m3OXu7dhint6vdKM2WYLvhMCR3BFZiLWPSixriaGdlR-X7j14bmX-vvk4UkJBUk9IVIBjmrwaMnTFoAcrLsyWlMpKNB63QUCSmebzQJ_j0Tmb6n-bd_QpmfZxZLf3v2SwruY8KbjWMT3qx9GrLMXAXFuHsIXVM8W1S3e9rdRoDlpq_-UQnduMwN_G3YLiL4isEH04ZHcN9RBXJWymLxjdO2fzmmb_8gO-8_LRFiG-ohPDsf6SRsjJXxF5c13DKR3l2bKIlAKngWiFX8dK34mTLqAQdv1JrMSjkoQAHpYGzTLMitG2AUINWKMDSMt3ATZaPl8aRY_Ly_dYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب اسپانیا مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/99423" target="_blank">📅 21:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99422">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBvnUkpzcvKjRfWgStMEpoH7-gCGSHItWBaVyPzxnpe1zkIaAQ0khvZUxg9S7fP-kkZmPQV24yAJjF567BqEcjpJZ4lYz60v6PxaloUIkKyeJL0kAQ1PPHAp9zKQG_RDheXT44nJQYLz1_bcwFbrurbCe_Wg1j0qnv0Zg_BVWfevxX5yH2nWBbIAJgki2nuZuuIJ43GcX5YunYUYCgPWJYwlf2SwKFvtPHvhV2DYJfaXavxrbyA04smN80dwVFJoRv8DCvu8BAnrm_zNAUgvUYI6T3q_UYZ_lepkmKn78GXdLktlJnXZBE0BsjPk3zzRhW6ra-tyEi9OBac1QdBH9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب اسپانیا مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/99422" target="_blank">📅 20:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99421">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd631f7d8.mp4?token=E36IxxD-TV2jPS_ZNdq4521l2mtcDY7vhxw_RgKKNNCQbhYKeD_rRiUaK837H0TNPNTJlv6qc3th4l758RM7-P_wddXAiVi8sOypLdC4ZHAswEDCfIWf0CuvIejanIvlLJG2FF4XhtkzD1ITlF-dS0CqyLPcjZwWHUVY6UrDzLodQ_XjWPzxoOXu3JoihH3MGreixb5A09JADk1Bgwf1KQQTWRwTQeQt45TZ7UYaiDDkBLZ4JxM9wY7OoUHTEN_jvOQOJvTFDRGyWUAYQyTbeoijGBQbDt91PU-AiwO1JYA4uZQ2m3EsZIP-8YotsNzYrybs8H_EWOsCDkAQGcjadQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd631f7d8.mp4?token=E36IxxD-TV2jPS_ZNdq4521l2mtcDY7vhxw_RgKKNNCQbhYKeD_rRiUaK837H0TNPNTJlv6qc3th4l758RM7-P_wddXAiVi8sOypLdC4ZHAswEDCfIWf0CuvIejanIvlLJG2FF4XhtkzD1ITlF-dS0CqyLPcjZwWHUVY6UrDzLodQ_XjWPzxoOXu3JoihH3MGreixb5A09JADk1Bgwf1KQQTWRwTQeQt45TZ7UYaiDDkBLZ4JxM9wY7OoUHTEN_jvOQOJvTFDRGyWUAYQyTbeoijGBQbDt91PU-AiwO1JYA4uZQ2m3EsZIP-8YotsNzYrybs8H_EWOsCDkAQGcjadQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
سرقت‌ گوشی سینا سعیدی‌فر گلر سابق استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/99421" target="_blank">📅 20:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99420">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPBpYtWBynaUEm5TrkYYvnUIwaaePfjZQUEhEXoGzGmLVMhqwtQqpHmWAhP_CbwWl2qhxudBG6dC4_ZZ9t2ElUkZjMNmzNvkLHSIP_iKP5zURoerMAnqxUy5K-Sqx5wD6kipzj8bSYUxPtJ_vhURcgswkmf1f0s-E88rXbUwLI26i9sTmOcm3bmgR7EZ7sNUE00ytkOPKdHad1L5u4QfvybzaPCFKbZXPeflAh9aPaVWMpruUjM8fLq-qToJKXS-XIGaAQByctvHZZ806M4fRRIl0ji8UGs_nxpn8Qk7mFeVh6rf-weaS3m21d8IjGiWUCEyjxAAQY77jXyNcWViHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🔥
فابریزیو رومانو: آدیمی به بارسلونا
🔥
🔥
🔥
🔥
Here We Gooo
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99420" target="_blank">📅 20:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99419">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzFVm6IqyArFbdH7NBuPZVkHRO0fZ74edLeSlnLNiYFguC8UTeMzLBZOC4Ny_DDCFzsylTcV-14ppqIuwCqcd3Lk5Lnvq2rbolw0mx4NexG65f1Ekn8RX4CczSRYI1nwaNU-AQcIWmjOPxjZmkh8wv_nhq_YNZJIIOxNYeGIcNlxnWpPv1FpU5fxI6VjyxrYkbkfySyozQAdX7CoQxNBUK0-DJnY2RuUxIzpJOHafAjJLNCK10RNq-KJu1E-rUv9IzE3Gpb00-Q-TMaiYqnFNpHP190Zf9DPYd-5l-DU16bQFdF_nR5bYRvvY0ThSiza8tGDLuTmMK5Q3y16H7aqoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
👤
استوری رامین‌رضاییان که تمریناتش رو بجای حضور در کمپ استقلال در کشور اسپانیا پیگیری میکنه و اعلام کرده که بزودی اخبار خوب در راهه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/99419" target="_blank">📅 20:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99418">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZwm459kXz7ubl90t1mpFxB1LomxAvwnFnelhwzcTa9pcvPGjG75DxiQpX4xcrfNPivTYL61ww_6ReGYLsfsm4VOqLTygZQVC8rYwgvtHOyVWoWSx5Ay4teaO_yr3atWziHgs3nxYyQqCHkTZ1lDuXEfoYzmrsohGyVDBy4ncd4Xe026p3fBrOCtwAv5EspNJ2APASf_Z8GdszQlLkgZWBKrRXdYI6jBjqWqOjuZXVsNvfOwfp6S05JEFjki9By_tAanLLLwrIsKTK3KpzdBmcvOY2Ix6bv_md61n842PxA2fWoAwBrqVJV_2Yh8yGuogqa_h4v1E7zhutTlNH1oxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مورات یاکین سرمربی سوئیس غیبت یوهان مانزامبی در بازی با آرژانتین را تایید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99418" target="_blank">📅 20:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99417">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180 #فوری
🔵
باشگاه استقلال با چندین ستاره‌جوان لیگ‌برتری به توافق نهایی رسیده اما تا باز شدن پنجره نقل‌وانتقالات آبی‌پوشان، هیچ امضای قرارداد رسمی صورت نخواهد گرفت. هرچند شانس بازشدن پنجره استقلال کم است اما پیگیری‌های وکلای خارجی این باشگاه…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/99417" target="_blank">📅 20:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99416">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔥
🏆
🇪🇸
🇧🇪
تیزر فوق‌العاده از تقابل امشب اسپانیا و بلژیک در ¼نهایی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99416" target="_blank">📅 20:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99415">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/024bbfbe87.mp4?token=DJk7LnmEcmX9NEFEUqRTkCpZ2UdKH84kpuJbCAREr5rSkVzWy69jfUfyLD04DgDCSmDYYazvRdvIkpxQSDLSR48ZQ_0bOoQ8NFzbZ9y70vMyoYmnNXesWnsOVXhYBfxLSoRbm_dPeMOULLb3BbbEz1qTuNyzISpXoHwwMMlwxrYmsXanmm8ffcxha-wU2ySHtezafdo2VF2_XnT61ZJEuzEsotoNPJReq527y0opyW0z4CvQPRittCAgDll8MsVhSCpdYdK2bUAD3NM77Rcsiy_BodWTsLNxblHBqO-tnMVqn3LedCqfrLCUQbIF2XKipmtOSMG6B6QPPZrY7ixkxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/024bbfbe87.mp4?token=DJk7LnmEcmX9NEFEUqRTkCpZ2UdKH84kpuJbCAREr5rSkVzWy69jfUfyLD04DgDCSmDYYazvRdvIkpxQSDLSR48ZQ_0bOoQ8NFzbZ9y70vMyoYmnNXesWnsOVXhYBfxLSoRbm_dPeMOULLb3BbbEz1qTuNyzISpXoHwwMMlwxrYmsXanmm8ffcxha-wU2ySHtezafdo2VF2_XnT61ZJEuzEsotoNPJReq527y0opyW0z4CvQPRittCAgDll8MsVhSCpdYdK2bUAD3NM77Rcsiy_BodWTsLNxblHBqO-tnMVqn3LedCqfrLCUQbIF2XKipmtOSMG6B6QPPZrY7ixkxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
هدیه‌یک هوادار برزیلی برای کیلیان امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/99415" target="_blank">📅 20:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99414">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fd28a0670.mp4?token=h7kHub9en20y0ez9zAufFG07uRqYvFE4DAUbJcAaX_RUzhfPeDp79IciS_EYEIWALaKDQ4sIhCR3OZD3HM5mByoTAfFDRgue_sT0qMLG__49BXjxW5QJDFKlk_IadlNOGjggiYbfmDCPRB5Tm2Gnz9JD_lnSKw4zOdgv6YpqSGa1-Hex-ITF_YXp2uX8rNA5BkXuhN_cEEw27JAGvIF-E_q8vl5XePKS5FJXDXCnQsiujY3ZvBs2sRCCg7hF3-yjFv3UUB5RoTCYEQMUk7AAO7CL70ATMnPhxoVFoK4dF8WTviBCgDKDw3nOK5bceIWtLzp6EUruZ3oedx-jPY7nqWtpfIh_EJ-6e4vJSUdbjnKwNU7J3d6Z1j0GZovUABY4o5ny_KmZWJu-VEI78DpmNoIxiyGGDnNxqp9HU6lom96VkPaAV_Xd8yzZ3vSvsGq5Ct9cEGG2NNZb9-brUl67GcdufRyC5OYA0BC0AwVtEUxih6p-brE83-GX-FdQvKCcEVFuFuCvo40hFR_v16_EtNckhF8uqnv5m8NDSTCPyTbjpjUdxfnQHFERJrfWfuUHShij31zsx9Zt_-OWiiFl3_pMAtrJt5_f14xCemz_gcxyXwyfidqML1Uz4Z5OMXjxYdHWPomYZ8omRNF2If8DjDaVk5ggBbhVTbhbVh0kpLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fd28a0670.mp4?token=h7kHub9en20y0ez9zAufFG07uRqYvFE4DAUbJcAaX_RUzhfPeDp79IciS_EYEIWALaKDQ4sIhCR3OZD3HM5mByoTAfFDRgue_sT0qMLG__49BXjxW5QJDFKlk_IadlNOGjggiYbfmDCPRB5Tm2Gnz9JD_lnSKw4zOdgv6YpqSGa1-Hex-ITF_YXp2uX8rNA5BkXuhN_cEEw27JAGvIF-E_q8vl5XePKS5FJXDXCnQsiujY3ZvBs2sRCCg7hF3-yjFv3UUB5RoTCYEQMUk7AAO7CL70ATMnPhxoVFoK4dF8WTviBCgDKDw3nOK5bceIWtLzp6EUruZ3oedx-jPY7nqWtpfIh_EJ-6e4vJSUdbjnKwNU7J3d6Z1j0GZovUABY4o5ny_KmZWJu-VEI78DpmNoIxiyGGDnNxqp9HU6lom96VkPaAV_Xd8yzZ3vSvsGq5Ct9cEGG2NNZb9-brUl67GcdufRyC5OYA0BC0AwVtEUxih6p-brE83-GX-FdQvKCcEVFuFuCvo40hFR_v16_EtNckhF8uqnv5m8NDSTCPyTbjpjUdxfnQHFERJrfWfuUHShij31zsx9Zt_-OWiiFl3_pMAtrJt5_f14xCemz_gcxyXwyfidqML1Uz4Z5OMXjxYdHWPomYZ8omRNF2If8DjDaVk5ggBbhVTbhbVh0kpLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇬
استقبال پشم‌ریزون مصری‌ها از کاروان تیم‌ملی فوتبال کشورشون بعد بازگشت به این کشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/99414" target="_blank">📅 20:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99413">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/99413" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر پنجشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://t.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/99413" target="_blank">📅 20:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99412">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOV6eScU5rxheKI5xfLovhq3J7zRZ4OicrlXYeE9Rtnx1xPyFcnM7FEE-jsDxGEL4at5ZldrdRo6oTBqHv5DE4zWqjTv_YRBEfNYd4sKireYsLd3YOLu-KUCokMLkuscW2LcB8NYp-lYvK6URGY07jjSpapkMMqGz5vNFoOPF7TdVy5Dx7i3pV4ecdktrc49ue3Ewxn0U3O4UhwerGyiddbdx8AXVzoKmNyiO2Y6CvMgrLOt1esG6tRSGYReX54FV4DIkdjjXbtuwGu2gXQdq3AZdJlP02OIhrAiNeA7tOBT4r6i6R9ewRIlEM-gPIQR1h4T-rlQd688AlhpEMqPrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین سایت جهانی برای کاربران ایران با واریز برداشت مستقیم
⬇️
🪙
سایت بین المللی و معتبر لاین
بت
❤️‍🔥
اسپانسر لیگ  فرانسه
💳
واریز و برداشت ریالی
👀
بازگشت باخت ب صورت هفتگی
📣
دارای پشتیبانی فارسی فعال
🎁
بونوس
💯
روز های دوشنبه
🎡
کدهدیه ثبت نام
➡️
L5670
🔗
《
لینک سایت برای کاربران ایرانی
》
👍
《
دانلود اپلیکیشن اندروید
》
❤️
https://t.me/+dukgrB6-zGsyNGM8
🔻
جهت استفاده از وبسایت از آی پی کشورهای آسیایی
🇷🇺
یا کانادا
🇨🇦
، استفاده کنید
19
🔤
✔️
آموزش کامل و جامع شرطبندی
👉</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/99412" target="_blank">📅 20:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99411">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_cHly2RwUg6amR5jlrn2dTeGW0KVvUbMWpYGbHKT-cERIjXmI5l9VmNlRiNpN9FbZkyphcUOJrkeUUkyjeQg11NdBz7g6sdh8mqt4BRkBbQeEjKhdfNr2MvutbBZ9ERAaxkNHbGegmIIVs1BtU6L7VomsLfG81FBPt02pgCsguFa6Pe9S7UA6CTywAdpyFMZ_K0Ny4BMS4PHCkZVyB0iNF3uSvBVDHG4XVZK65WPsvbzzSejs3_Er9spFuHjAIgVSAp2Ma9-Qovt6x5QFBVl8U2oWpwSHmGMNSGMlXsuyxBKPmExxHrp8VF998ixSVb4nKOoXXNrPkH2lWgebs7Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‏
🎙
🇧🇪
رودی گارسیا سرمربی بلژیک: رویارویی اسپانیا و بلژیک اتفاق خوبی است، اما زیباترین اتفاق، حذف آن‌ها و صعود به نیمه‌نهایی خواهد بود
🤩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/99411" target="_blank">📅 20:00 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
