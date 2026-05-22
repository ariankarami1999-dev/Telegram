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
<img src="https://cdn4.telesco.pe/file/sls4_Y8LxVvoFGRV2yIDclmH6DNsRiVOirhQu32wfCZa8em1if6SfkNqTaJY_Vl5SSmbJRdZnFfSImrpnATvqC5ZzMOjXnEnbVm6FEwfkEwNCh1_NuqXsQLQqhjGEj2Sf4tItK83DaoniOshtrgRzBgdMu_YqheWy28VswO08M-raLE03TV4APBx1PkhvaEvJod0DHPxefghAFGnD2Ne2drRfjPL1aQGpKMOLwEbWuCRPu-bzuH0PRImV1tx_pIPK-GmP1M5aL5AEiIdZy8g7b4_vn3H6J8dsIvTRHwuX0eSQ6pZQ3Fx_IVucwU_UupHPxYouyCjlnlkdfWDRusFFQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.92M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 13:48:30</div>
<hr>

<div class="tg-post" id="msg-653493">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9a4f2cb19.mp4?token=qFPA8wfIMA5mfFHF-tc5_aNPZ0AKyxzdml8QzvudrC_rzaDyiSnOCsSfyXnYqQ0YgBTQQTK7GwCGED4CYxzhPjtcve0BMNJE__-qYD6gaVgSPU3iVVGy7Z5DvUIHpDILE-lxhluoOWjdN289u_FlmVgJ6iMKCmBBhc1yXyTlkMUD662IlGWH-5DS851MKI5w6-HoNcOc9KepbfRT6kukfob1VbdzrRvuzAPWoUEkM-3Qm19VYl5gqWduMpU28RQdb9o1zKaypIEgS-cc7LXkduG7UFjFGfBzjIi4MZgNbQLMALqKDTY1MNZtENmI8IZjFnL_ufoodj0DqF6xuPKIfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9a4f2cb19.mp4?token=qFPA8wfIMA5mfFHF-tc5_aNPZ0AKyxzdml8QzvudrC_rzaDyiSnOCsSfyXnYqQ0YgBTQQTK7GwCGED4CYxzhPjtcve0BMNJE__-qYD6gaVgSPU3iVVGy7Z5DvUIHpDILE-lxhluoOWjdN289u_FlmVgJ6iMKCmBBhc1yXyTlkMUD662IlGWH-5DS851MKI5w6-HoNcOc9KepbfRT6kukfob1VbdzrRvuzAPWoUEkM-3Qm19VYl5gqWduMpU28RQdb9o1zKaypIEgS-cc7LXkduG7UFjFGfBzjIi4MZgNbQLMALqKDTY1MNZtENmI8IZjFnL_ufoodj0DqF6xuPKIfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار وزیر نیرو درباره وضعیت آب تهران و استان مرکزی
🔹
تهران و استان مرکزی همچنان در وضعیت ضعیف آبی هستند.
🔹
وضعیت سدهای ساوه و کمال‌‌زاده مناسب نیست.
🔹
اولویت نخست، تأمین آب شرب مردم است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 574 · <a href="https://t.me/akhbarefori/653493" target="_blank">📅 13:44 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653492">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
کنگره آمریکا رأی‌گیری برای محدود کردن جنگ ترامپ در ایران را لغو کرد
آکسیوس:
🔹
رهبری جمهوری‌خواه مجلس نمایندگان آمریکا، رأی‌گیری درباره طرح محدود کردن حملات نظامی ترامپ، علیه ایران را به تعویق انداخت.
🔹
این تصمیم پس از آن گرفته شد که مشخص شد جمهوری‌خواهان رأی کافی برای شکست این طرح ندارند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 928 · <a href="https://t.me/akhbarefori/653492" target="_blank">📅 13:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653491">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGvWx8DkupSMbGE2DKP37Qvugib9JWt2uNI8GEJXPUNWZUNxoUNY4_OefG2yMffM3tNYxcs7HOVFeCJI4MJ-I6-9RjMt4-xaFk4VkFV9_8dwg3PWf8NsCa2avoBUWuT66qI4Aycpm1UUlZbRtY003ifRnI2mPk-mdkF0OJKlp-g8QSFUAhKdpNQ-UWt-O9G1io1fFI-37pr39W2cthQSQ46YKb9i_xywgtth_-kaJw-M_FZKDhAl2n2JQvBhPseTiKVpBGqsjiuSEOHzjOBCnYlZimbv60IbIDd_B2QzutNHBClKYdUOM6AV05AqZtkCMvwj23B0ZnAZuqEOlDfxrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت خبرنگار لبنانی در حمله اسرائیل به دیرقانون النهر
🔹
خبرنگار لبنانی «احمد حریری» صبح امروز در پی حمله اسرائیل به شهرک دیرقانون النهر جان باخت, منابع محلی می‌گویند او هنگام انتقال مجروحان هدف قرار گرفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/akhbarefori/653491" target="_blank">📅 13:28 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653490">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/816be2b81c.mp4?token=vTkczUoq5eDCsz5pXmduJ6_UzIrDcgCb3HSaitObq8qZycwWwjUnuDl5WR-v8EwdN-FYkzNorpUtih3YHDHeqLbDErxEDeerEBy0N8mkGyjxhx0CEdFJLRWalamtc21-rUrVewji2L9JZJG5zAnxOzbdUMSNVoKUzLsb6c0RMs9Ph2tc9SfwW7C3rzveLZTC9rfTFZzZeMClcGiz2c1FUS3VRiAANDar5MJACFVbH8kQ45H-tFpPbptl7RvAGrsSV20BHwTN5BrJJjJAclEjQuW08LgJzDhtUW_FSRPcsU43wbBV_jcp4McenapFcBHhsqkGs1N0uQD2sVLnupiZ2SOSgyWFB0qipuNz-zu6OwX4dKXDggvWttzG0l_5B4PSH6eyCElC2vlEXRyl1tBMed6InAx1p5uu9j_3QsL4rqarmsne_yK5i3g5c5bhvUB_6TEbT938VD7PpfBdTYMnL0F1DfJt79koYYo5cLCbQ-4trVFRIS764KEvZvyB8gVddAFgQQPtEtpY7-lpdWTZJFuS_ipS5dHNKOBp1RPMCl0oFjw1_Nw0qJDwiU_ahohK1amMGktzyo5Pp-6bibTt60CkHy9SJYlb-vaWiXev_FM9AHraFjDfLTWKuMuH-HvkmG3merS8TBLHKJXNYBCBZ6BFdQszwrsO_CqFk8v81j4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/816be2b81c.mp4?token=vTkczUoq5eDCsz5pXmduJ6_UzIrDcgCb3HSaitObq8qZycwWwjUnuDl5WR-v8EwdN-FYkzNorpUtih3YHDHeqLbDErxEDeerEBy0N8mkGyjxhx0CEdFJLRWalamtc21-rUrVewji2L9JZJG5zAnxOzbdUMSNVoKUzLsb6c0RMs9Ph2tc9SfwW7C3rzveLZTC9rfTFZzZeMClcGiz2c1FUS3VRiAANDar5MJACFVbH8kQ45H-tFpPbptl7RvAGrsSV20BHwTN5BrJJjJAclEjQuW08LgJzDhtUW_FSRPcsU43wbBV_jcp4McenapFcBHhsqkGs1N0uQD2sVLnupiZ2SOSgyWFB0qipuNz-zu6OwX4dKXDggvWttzG0l_5B4PSH6eyCElC2vlEXRyl1tBMed6InAx1p5uu9j_3QsL4rqarmsne_yK5i3g5c5bhvUB_6TEbT938VD7PpfBdTYMnL0F1DfJt79koYYo5cLCbQ-4trVFRIS764KEvZvyB8gVddAFgQQPtEtpY7-lpdWTZJFuS_ipS5dHNKOBp1RPMCl0oFjw1_Nw0qJDwiU_ahohK1amMGktzyo5Pp-6bibTt60CkHy9SJYlb-vaWiXev_FM9AHraFjDfLTWKuMuH-HvkmG3merS8TBLHKJXNYBCBZ6BFdQszwrsO_CqFk8v81j4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«سمفونی مرگ» در جنوب لبنان
🔹
ویدیویی جذاب از حزب الله که هنرنمایی رزمندگان در شکار موجودات صهیونیست را به تصویر می‌کشد.
🔹
این موش‌های شب‌زده را
🔹
ای گربه‌ها شکار کنید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/akhbarefori/653490" target="_blank">📅 13:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653489">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVVFyMl38DxyPrjWtYgOOQ0WMv2SXFhAOPy3sUmuDCjQ52fX4Y-T2Rh75jrJmEPyWX0ffPuFZknqF3yeh2Ppg7NGpgoebCUalG8eGNanfD5YqN34FOXaeGd3UJpZWxQ4vYjsxQs1G-W13bZJ4PuQtaHKz6Zakgn6LIRN0VFWddwYQZ_8B8cfwtZg22lGghJgQ84Vq6Wb898CAIk7bMjJfPp2n7EzAneNHQD4VwkNbFcjtn8UJvI-D6ZJNKxYo4FpvskqQ6IvU1KqlN4alPBgeOkFuv3yeF3Pqip91KCAay2LDedSDU8LnERL3sCATj_V3mDexVBVEcxAH9D8Gztfyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله پهپادی اوکراین به خوابگاه دانش‌آموزان در لوهانسک با ۴ کشته
🔹
حمله پهپادی شبانه اوکراین به یک خوابگاه دانش آموزی در منطقه لوهانسک دست‌کم ۴ کشته و ۳۵ مجروح برجا گذاشت.
🔹
یانا لانتراتووا، کمیسر حقوق بشر روسیه، گفت که ۸۶ نوجوان ۱۴ تا ۱۸ ساله در کالج استاروبیلسک دانشگاه تربیت معلم لوهانسک در خواب بودند که پهپادهای اوکراینی به آنجا حمله کردند.
🔹
لانتراتووا در بیانیه‌ای گفت: «نیروهای مسلح اوکراین یک حمله هدفمند را علیه کودکان در خواب انجام دادند.»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/akhbarefori/653489" target="_blank">📅 12:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653488">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f35adc40e0.mp4?token=TIH5p--ClVD1XTnnwWMowfF-iWio16pWgT47OaZnxdh5Hq12ab_5XTGvNce_vt2cc9qBxNZ_aBOdxZnCaJenhD17ejsYX2AXygfMxaIpzlzuFatMPukuDdv_iueaERLPVKuk2YUaT_vbUnH0VvXlHu9TIvu7ASrgflADc2KOOxgiYmPYof-HcyhE2_7KbLEtzBWkXkWyUl6kN1luH7OVJv8peMu6Ki-OQCcPWSqvEF-WSMRqyURMCuwgSFoGP5upKMEGqpwQqdIEH0BIoKjGhC6KdQPeBSVxPWoicVT04P6jkVX-ayyQut_0dm1gdMSR8B7AMLzheYyoaXXoMExD3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f35adc40e0.mp4?token=TIH5p--ClVD1XTnnwWMowfF-iWio16pWgT47OaZnxdh5Hq12ab_5XTGvNce_vt2cc9qBxNZ_aBOdxZnCaJenhD17ejsYX2AXygfMxaIpzlzuFatMPukuDdv_iueaERLPVKuk2YUaT_vbUnH0VvXlHu9TIvu7ASrgflADc2KOOxgiYmPYof-HcyhE2_7KbLEtzBWkXkWyUl6kN1luH7OVJv8peMu6Ki-OQCcPWSqvEF-WSMRqyURMCuwgSFoGP5upKMEGqpwQqdIEH0BIoKjGhC6KdQPeBSVxPWoicVT04P6jkVX-ayyQut_0dm1gdMSR8B7AMLzheYyoaXXoMExD3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدالت یعنی قرار گرفتن به اندازه هر چیز در جای دقیق خودش ...
درس انوشیروان عادل به دنیای امروز
👇
https://youtube.com/@caffeinepodcast2025?si=ZkcqfzRb9diYDZJV
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/akhbarefori/653488" target="_blank">📅 12:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653487">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/617f81fe39.mp4?token=EMYoHbsX23RMnnX7aACLnKbadXstZcksKupUrYwkEsXsPBFEjpsR279XonQqJawcG3f3Gzay1XMC1QpMrd5M1emORhcI7G092VdWdN1wcTk99MLA987AOpQjDstm009_Gc3Jb7rZKkDRAgE2Pfz4rW9S9tkHpePkCDeQ2Bqe0dH9flq5ZiScuZbpCy_jjHKaPGzSgC4aehH-DFRfuHFVlcHwAZWPFc5vWIleXVw9FlfYd0c8nEUZxEo_BCwoHxtxhFHzlAyS_Hdv5rtsy5Jtukw2X0-NWbZ0ivMRl1HQyZ-4Lfah_J5An-qiPK_lkf4TQeJ8bOfy0Thvm43rkxtwYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/617f81fe39.mp4?token=EMYoHbsX23RMnnX7aACLnKbadXstZcksKupUrYwkEsXsPBFEjpsR279XonQqJawcG3f3Gzay1XMC1QpMrd5M1emORhcI7G092VdWdN1wcTk99MLA987AOpQjDstm009_Gc3Jb7rZKkDRAgE2Pfz4rW9S9tkHpePkCDeQ2Bqe0dH9flq5ZiScuZbpCy_jjHKaPGzSgC4aehH-DFRfuHFVlcHwAZWPFc5vWIleXVw9FlfYd0c8nEUZxEo_BCwoHxtxhFHzlAyS_Hdv5rtsy5Jtukw2X0-NWbZ0ivMRl1HQyZ-4Lfah_J5An-qiPK_lkf4TQeJ8bOfy0Thvm43rkxtwYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موتور سواری فرمانده سپاه تهران بزرگ در رزمایش جانفدایان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/akhbarefori/653487" target="_blank">📅 12:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653486">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1KO6irFkhY4s0mYthHMSpMc1NvxGznCmrdiTHX5W6Z4PYKdX9U3sLlqKnnxSjafXYhBvinvtsgvTcF5OwjQ9IQeg_DaMbKx9V_-XaeCAV22pfQhfO0BPtHAl3BSILt2ZM7a8XtZiS3RFRQsdahFEc6UyQI2LkQ83qdXWXlEu6T8TUZ8fmu44Z4UUXcRkaM2346XPVEdeVjYCfGzjIhT1LCdlSiRckYqooB5lkq_fuM-sBtI8zaB4x0vm4MgkLpL3ingwk7mAeDSHJxSfewYllno-WhEQLmneQk4kJp4UemkHYAsYGZpb6TtEW3lf91fTKaS-JLcrcgySxIWQnBfrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مذاکرات ایران و آمریکا؛ پیشرفت نسبی، اختلافات جدی
🔹
تبادل پیام بین واشنگتن و تهران در شرایطی ادامه دارد که همچنان دو طرف بر سر مسائل کلیدی با یکدیگر اختلاف نظر دارند. نشانه‌هایی از پیشرفت در مسیر مذاکرات در طول دو روز گذشته گزارش شده، اما همچنان اختلافاتی عمیق، مانع رسیدن به یک توافق نهایی شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/akhbarefori/653486" target="_blank">📅 11:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653485">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpcKMuW42yRktVNEGuCEdgeXwMGZ4E4ANfSXEK_qz7K-5HoliwNgy1XWEBz2OTe2RHRK1fW6FgZLheQ3f1DWCZcRplKT0AIc4-ZQdgdQiRHfBr3hcn2RQT2CeIVl0_sF84i5KT130mWRagVNxhecqdtgTYS1TuPS1XA3Sq1D0ofVP4mKr0cbLFBWu3oPWb4olRZUoQt39UIr3FNbb6L4B6bbXli9iTn8mXApwdKQS5IUEuplTbagbPzmKbVG7Y_PDfIR4uUpDwRtdq1fIkV8S8NiEOp9u5M8qMkTWGRydlbJFl-IHRVMUAEKPq_Hdwt-jGndTO8LWfmKAXLOP8mcxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقوع حادثه برای یک نفتکش نزدیک یمن
🔹
سازمان عملیات دریایی انگلیس امروز از دریافت گزارش‌هایی درباره حادثه امنیتی برای یک فروند نفتکش در آب‌های نزدیک جزیره «سقطری» خبر داد.
🔹
این سازمان در بیانیه‌ای اعلام کرد که یک نفتکش در ۱۸۱ کیلومتری شمال سقطری، تأیید می‌کند که یک قایق کوچک حامل پنج نفر به آن نزدیک شده است.
🔹
در این بیانیه آمده است: «تیم امنیتی مسلح نفتکش با شلیک گلوله‌های هشدار دهنده، قایق را مجبور به تغییر مسیر کرد».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/akhbarefori/653485" target="_blank">📅 11:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653484">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hb5kYR-HLHWY1zhGGB0f0oFv1rs4iiJXvNyhcQyuVub4lGGT2y6NMTcAhlq5FpuiM9I-KsmEaI8w3VJfHjr5J7YHKeHI_xrSXhF9ehuQ9HJnIqeBFhBZi9Yv7jzzIQcKDQn20paXqNzXJQrhRKP4TmPDmwXBU-SUWZyQtF-Wt9HhQQShMWe56DzkCvxdiu0MTP90ML1LtE0yasBc4fPYKM2N9_edrPRhDD73n1S0EjMfHCuBkrJGh0JFisPpZfhAgdcDeq9wLGQlPNYjHqDkoOjMWPOaRi4K0eMBs-v6hofx9gL6ceQCCgaazqHUwpw84aoR0fPYVkuJm6Dnen9lJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلاستیک؛ مهمان ناخوانده خانه‌های ما
🔹
پلاستیک سال‌هاست بی‌دعوت وارد زندگی ما شده است. وقت آن رسیده با انتخاب‌های آگاهانه، این مهمان ناخوانده را از خانه‌های خود بدرقه کنیم.  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال…</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/akhbarefori/653484" target="_blank">📅 10:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653483">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgGXBTj6AVNRnchwmGzRY1My6k8usqTrWypaEKVvcfax6d5yMrVH841W5uKu54gjnK1k46TQTpTfMKv3YyQiviozJNMM2WGEL3wamCOFztelOcWxbgJQF_JqSajoay2sb-OLDVC44fB1a9vRm1-WHcLSqcAlu7-r8h3BG8cp7zycWPtXfnM6ssMsyV6IK-Ji46n9j9Oh1jNOPheWEERELUdXBN9nXz_8vEBHE1SxQxPdjv7nZH6TIE4rBrHGCtydnUgiAf1c5YIzMcISF1Gcu9ki680aUsLz95WHDs7NslY75g2OsKDopQktDysvTSw4pPxCRW70EUF0ZKCUKmrNWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی: موشک‌ها را برای مذاکره با شیطان بفرستید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/akhbarefori/653483" target="_blank">📅 10:56 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653482">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
چین و پاکستان یک ابتکار را برای پایان جنگ ارائه دادند
🔹
سخنگوی وزارت خارجه پاکستان: چین از تلاش‌های میانجیگری ما حمایت می‌کند و به طور مشترک یک ابتکار پنج ماده‌ای را با ما ارائه داده است.
🔹
نخست وزیر پاکستان فردا در سفر خود به چین، ابتکار عمل مشترک برای پایان دادن به جنگ را مورد بحث قرار خواهد داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/akhbarefori/653482" target="_blank">📅 10:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653481">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4OJgaBbjjF8xzPNCvQ0pAeFhn6i_GD4-sfIWgKw4WWvPqjaAI8Q7z6f2SWL8flaBk5mnLj8GqHT72iXSvTce1zxBTRFDmBYWZjFcGvS5tE39lWsV4DJUi5UD35cWAI_5dkNQyRTQGgxMNvLI4O7iWUxRqNob5NOOWk72AhcjCsxErNsF500GkPthb8_KRgAggmo41oskmyfN17Zn2nO0L16eDRTF7CLFPScPpEm__KYWpN76mdbgv-HSoG4sP9OupWAegBfJsSDwx0RkiHDVEAoFJaGPSzOm0G9s_ysWTLlT_EbVrZqyp0QN9JQb8ro1kBL-Kk-6WfAd48gE1xyew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نگرانی در اسرائیل از تکرار سناریوی اوکراین به دلیل پهپادهای حزب‌الله
🔹
تحلیلگر برجسته نظامی و امنیتی اسرائیلی با اشاره به استفاده حزب‌الله از پهپادها و تاکتیک‌های جنگ روانی، نوشت که این روش‌ها، اسرائیلی‌ها را در معرض تهدیدی شخصی قرار داده و نگرانی از وقوع حوادثی مشابه اوکراین علیه نظامیان صهیونیست وجود دارد.
🔹
آلون بن دیوید، تحلیلگر برجسته نظامی و امنیتی اسرائیل در روزنامه معاریو نوشت: اشتباه تاریخی تکرار می‌شود؛ منطقه امنیتی جدید در لبنان در حال تبدیل شدن به تله‌ای مرگبار است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/akhbarefori/653481" target="_blank">📅 10:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653480">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rju5At4_GH2ePXtsJVxKgFyo5YXHMJw1iMcbxkFjoOI7KLm59ppB82qEXIib-q3dOeUwG23iW2nU8mH94k5Asxtsiiy9bHvbSHza8oD6_tHEq4nlFq6MW_FjFE1H7kgj-0TIyifhygKClafnEAJfe5YVLt2wCwnhrDHXLw-jp2O4xQaU6bUrKXD1f3Wca2anXKvJOyKZGUSDPXX6RTsso2OyPpRMk9OcPJe_K8vQX6OKZnUZ9zNhQZhx1S6koHEwLTDUdN1o9ToPaFVN0QSKPkAwVa_eytyOYU0PyLZUKOpz7dk8aIT3VzcPFMkEYxlhrG6fKunj93uPDxVZIA894A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا فروش مهمات به تایوان را به دلیل جنگ ایران تعلیق کرد
🔹
سرپرست نیروی دریایی آمریکا از تعلیق فروش ۱۴ میلیارد دلار سلاح و مهمات به تایوان به دلیل نیاز داخلی به آن در هرگونه جنگ احتمالی دوباره با ایران خبر داد.
🔹
هنگ کائو به سناتور میچ مک‌کانل (نماینده جمهوری‌خواه کنتاکی) گفت: «در حال حاضر ما یک وقفه [در ارسال تسلیحات] ایجاد کرده‌ایم تا مطمئن شویم مهمات مورد نیاز برای عملیات "خشم حماسی" (Epic Fury) را در اختیار داریم — که البته به مقدار فراوان داریم. ما فقط می‌خواهیم مطمئن شویم همه چیز را در دست داریم، اما پس از آن، فروش‌های نظامی خارجی در هر زمانی که دولت لازم بداند، از سر گرفته خواهد شد.»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/akhbarefori/653480" target="_blank">📅 10:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653479">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pj1yJvru-zMdoA5gc6VycUVbd53bm8giTtMahhqTRSWQOvNTxQQlAqf-s92633jL8OXMyZ3UOLRRn7lXZfZO0kvBtk_cA0Ai8QTqYKy7CQrngopIU2DTbDP8L1zhkh4H0uA0s2ENN7aWeTjMD10vRdabpdish6ljNVR2Y3dO-OgWSDfh_dKu8F-fdT0UUreSI8uDBykZgAzNwtd1Oq1-1Y9Pp88KEV3qMwi7aEQPPmO4BJDe2PRAGRipaMlwG9_GdFPeaWGkngqmVqu2sxyLoHVUuNd7zejtybIft4hzW9jeWKbnWbMfEW39Z79rX3dOjoVoAJqAw5dng5yjLcvj-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کانادا و استونی در مأموریت تنگه هرمز شرکت می‌کنند
🔹
وزیران خارجه کانادا و استونی روز جمعه از مشارکت در مأموریت پشتیبانی ناتو برای آنچه که «تضمین آزادی ناوبری» در تنگه هرمز خوانده می‌شود، خبر دادند.
🔹
«آنیتا آناند» وزیر امور خارجه کانادا امروز (جمعه) گفت: «ما با ائتلاف به رهبری فرانسه و انگلیس در تنگه هرمز همکاری می‌کنیم».
🔹
همزمان، «مارگوس ساهکنا» وزیر امور خارجه استونی نیز مدعی شد: «تنگه هرمز باید بازگشایی و ناوبری دریایی ایمن شود، ما آماده‌ایم تا در هر ماموریتی مشارکت کنیم».
🔹
«ژان نوئل بارو» وزیر خارجه فرانسه نیز ادعا کرد: «استقرار نیروهای نظامی فرانسه در مدیترانه با هدف حفاظت از شهروندان و متحدان ما در کشورهای خلیج فارس است».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/akhbarefori/653479" target="_blank">📅 10:40 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653478">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vz3_wxefN91z9FUqYedDkrNsnXFYWykO9QUmnMsJ29DnISnVtEMamNOyblZ-hb5yO6O_dW7OaQ3hoVdnhjfw7WwcNn5ln_IQxJmlDwPH3_-a3Q9J9T2VhhrwZC8QoJa5UDtyt7FVZeMUPIt_OQPLg1tTFaHrGKmPn5rc3oFOxTbxxMjdLeeHnfqeucSXVRCf2-iK2KQjGHNuSRjqTHZfRfOMArVURj2FmVo-PromOiDQU2kPv8nr9YUuncyyw3913UiDdBX8QcKpR7zh4ZYzzPOx1uP9LkMlaf2WuI9MpWpO1jpLHJ5Gu3omo4E0V5ReJEMhhEAFoQ4-x5c8-nztvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یورش اشغالگران به کرانه باختری
🔹
منابع خبری از یورش‌های گسترده اشغالگران به کرانه باختری و استفاده از گاز اشک‌آور و بمب‌های صوتی خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/akhbarefori/653478" target="_blank">📅 10:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653477">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3KBDjCts3br5lb5QG7tXaLeVvKZeejmFoD-fXk1qtimOxlY08aOapHLNHOmXzR2BkQcWEb1YgJ3ZlmUCFPJliuoJhaK0hiaIG-9qc3LK98vXkjU8voTUsRDKngDSisdoTY9d95qp6qXv1Zj1G1RXUTyDLw4APT2A8wU5P_gWljtzfDJxgg75cdJt9HUYLCtOnhpsg17o0x9CSin3CaMinm7_z-Xqzfsowk5CF7_q7FBgBpJR0gKRnHidM_ppMKevdstiGJmJIJIz7p1DoA1XE74XN_V6IaBTNbcekd98F8MmmrLBUFE2EeaMdoKMIdRn2BF3LWaySVzM60YNfds5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجوز ناتو به آمریکا برای استفاده از پایگاه‌هایش در اروپا
🔹
دبیر کل ناتو اعلام کرد که آمریکا می‌تواند در عملیات‌های نظامی خود از پایگاه‌های این سازمان در اروپا استفاده کند.
🔹
مارک روته همچنین تاکید کرد، به عنوان یک اتحاد غربی-اروپایی، ما می‌توانیم به ایالات متحده آمریکا در تلاش‌هایش برای بازگرداندن آزادی دریانوردی در تنگه هرمز کمک کنیم.
🔹
روته افزود، چندین کشور اروپایی تمایل خود را برای مشارکت در تلاش‌ها برای بازگشایی تنگه هرمز و تضمین آزادی دریانوردی ابراز کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/akhbarefori/653477" target="_blank">📅 10:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653476">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAFDPGtiidzQMTliND54rnEXA4w6CMqZQ9RabvDPWLjccfA3_V2OLs29rkf06_Qxc0wfYa3AXbf8Q_-qGhOUt5s7ygW2e39wY-3cWtjaXVv9chJN6ZGMm91T6ZyuENjZ0R-64QrqSpHMZ7DOaSrV6DY3xDtpyA9dVl6eEe4eE4pbI80dBIgZ7exX2DAFO9Lk_TRrtORNL7XUwPnG0mle-pHY1LC7KkMotBwEXDNfwOVLeMjHDR0QCsxqQ_mRhzpJLpA5bzVMjpoEOPjizsWfjyfRIXPv2_0olfGrduN_st_3hAe32ISW4u1tQUQLGt5TmXY9N5OQFLau8XhLagns3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران یک‌پنجم پهپادهای «ریپر» آمریکا را نابود کرد
🔹
وبگاه آمریکایی «بلومبرگ» گزارش داد که ایران از آغاز جنگ ۴۰ روزه موفق به نابودی بیش از ۲۴ فروند پهپاد آمریکایی از نوع «ام کیو-۹ ریپر» شده که خسارتی بی‌سابقه حدود یک میلیارد دلار برآورد می‌شود.
🔹
پهپادهای منهدم‌شده، حدود ۲۰ درصد از کل موجودی این نوع پرنده‌های بدون سرنشین وزارت جنگ آمریکا را تشکیل می‌دهند.
🔹
بر اساس گزارش‌های منتشر شده از کنگره آمریکا، واشنگتن مجموعاً حدود ۴۲ فروند هواگرد به ارزش تقریبی ۲.۶ میلیارد دلار(دو میلیارد و ششصد میلیون دلار) را از دست داده یا آسیب دیده است. این تعداد شامل جنگنده‌ها، هواپیماهای سوخت‌رسان، سکوهای شناسایی و همچنین هواپیماهای «ریپر» است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/akhbarefori/653476" target="_blank">📅 09:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653474">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KFysky31xs9RrI61npi3gYDf4X3vYpaTZeiNzoYSzXVmc6GSGw36xuXPw-tjtw0bmZXQXpeqkcVNlDClshAqmmjJeiDiobroIYFCCYYLb86nUXp9rCKp0YJRGCk1mj5wVRP9aX7PiHHuw6-ZEmliuHLL3kvzG8geieRA8qF-1txQ6yW1TD94b9cxI8B_jcPqxzXrIJAIEg_GPgs58hgyZN3nqg63t6Q7ERQtjK57yQjbFfICorxJ2k5UaFl8b5ahuLslEjzcz7_W1nElbnip6Xfoznx3OYxQYC00S6m4SQan32PbzQ9Sp1nJHm64lN4Y3qFgvGGh35KC2gZPXQL53w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s6tI_DUjmZMtV6oLNJP-ACe8Y4BygmpcIedXirXRKyuPzn1ijqHiT1S2jphG6ozAAty8HHsC2IIy2QyciOh6xbPHM0Iyz3Vk_vezLs2JdOKc9IdCvk8KbNtRvT55I4o0d1c1dFqf6rIzYCpbfuVkEUqBdsiDycHQMmgQS-a5l3ZHGk91BGzaYGY4al1HKHBKVxVdvQH0PB6KiV_O-ynVFWLYDMWKB0mY-DyhC7NtJDIAqBfJ0huCA6StxxK-UDycftSuzofFOAglN8F_4n5Bdc9K9MTBWfk--yT-5pWo0Xh5oYSKA3_YRTtWyyvIlxvXZW7p-xNi94KTUH2iSfkNUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جزئیات تازه‌ای از آسیب به پایگاه‌های نظامی رژیم صهیونیستی در حملات ایران
🔹
تصاویر ماهواره «Sentinel-۲» نشان داده است که پایگاه هوایی «رمات داوید» در دو نقطه مختلف آسیب دیده است.
🔹
تصاویر منتشرشده از تغییرات ناگهانی سطح زمین در نزدیکی ساختمانی در پایگاه «میشار» متعلق به یگان ۸۲۰۰ رژیم صهیونیستی در نزدیکی شهر صفد حکایت دارد.
🔹
تصاویر ماهواره‌ای خسارات واردشده به یک موضع دفاعی در داخل پایگاه هوایی «نواتیم» را نیز نشان می‌دهد.
🔹
تصاویر منتشرشده از سوی شرکت Soar از وقوع یک آتش‌سوزی گسترده در اردوگاه «شمشون» خبر می‌دهد.
🔹
نبود پوشش گیاهی متراکم در این منطقه، احتمال وقوع آتش‌سوزی طبیعی را رد می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/akhbarefori/653474" target="_blank">📅 09:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653473">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5XVoG6FIBZXP30BxlWjE66RH2Dy_zux5JAi0r4Nh5xphTybSCI6Srd2IEQXzKnwtA_WJVwXOfZzS6QbBd1NEIk85HxaPwgn0eXFOWoqqDVSZ5UySMyFo3WnkH8Bs9L71nOS0eZxhgedzDxop65m_vSDQIzsFuP1d4U8OsRNkcpOCoxTXQrfTzmNTxuaVjVLXcVVp-U3hImXB1RGxu8OBBLSzRoqIMQ2El2ODSGNAoPQrnESiIJtY1piimLkYFLg3Ojn1hgonbzWt4uEFjapQMIUjUN6qmpZpPDDn1Pdiq87t4FZA6Yq4zjTLgg7vZEvbQGVoT1vAuFDXRlTszvj9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت چهار نیروی امدادرسان در حمله هوایی رژیم اشغالگر به منطقه حناویه در شهرستان شهر صور در جنوب لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/akhbarefori/653473" target="_blank">📅 08:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653472">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a2f35b9f.mp4?token=s6QG6U4LfsumI5nPfGzHVkimLn6P-NsVmjZUiciHohRQmb0bFm70DhmrZRJzOuqhwA7dAyF3D5QtlT3k8gzOeeqJh4hEiuNwFrjWw6qXLdrU6tQ3aLmYj8S4rZQxxfz4LA3n7_8Dl2UhiO0Trmzs9HtdLEJoiQa4Pk592DrtecrHO6xEck5SEhXrnPfRrfrcVMeiheAac_8HNeL0sEed6k2FboabuLcQfKkBfhH5YghFp5JCyYTO7nMUozNun5KJQcb1PDg9YHN6LOGbsDG0wg2OncF-YykOMQ5MgF1sSYuGChvjj3esccrzHIbBk50wx9E-flI_ZzrkN_Xdy_3WQp9BwFC8SMbWM8oMiGzzgFstKdOBaQIldBmBNKHNpFcqOwBIezNVlILfoksMCiBNb25vPED_1VVZ6-jRlSP53MgGCvf7VuiVPsK3lOJiNEWDFcPsnuKilV1JyK6JbuqTl1Vkr_o1z6M02pJb55VWyIG-c5KLHlilF8GjMWX7TxHx7yh6VuF-2qeVwehWJOPOdP6YBbhc0jGco7LYTV1G320gQtTxWBu1L6R84YFwupw1Q5y0Z1nJOyALcxJXYE03pm-qoRh5Et6-3KxpoV9bHvCGmKWKhnu3j9JR0R9hUPPi1-7cbsD8S4CJqhw5Or9Bkjx4Ie3IMciOllsmMad5XK0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a2f35b9f.mp4?token=s6QG6U4LfsumI5nPfGzHVkimLn6P-NsVmjZUiciHohRQmb0bFm70DhmrZRJzOuqhwA7dAyF3D5QtlT3k8gzOeeqJh4hEiuNwFrjWw6qXLdrU6tQ3aLmYj8S4rZQxxfz4LA3n7_8Dl2UhiO0Trmzs9HtdLEJoiQa4Pk592DrtecrHO6xEck5SEhXrnPfRrfrcVMeiheAac_8HNeL0sEed6k2FboabuLcQfKkBfhH5YghFp5JCyYTO7nMUozNun5KJQcb1PDg9YHN6LOGbsDG0wg2OncF-YykOMQ5MgF1sSYuGChvjj3esccrzHIbBk50wx9E-flI_ZzrkN_Xdy_3WQp9BwFC8SMbWM8oMiGzzgFstKdOBaQIldBmBNKHNpFcqOwBIezNVlILfoksMCiBNb25vPED_1VVZ6-jRlSP53MgGCvf7VuiVPsK3lOJiNEWDFcPsnuKilV1JyK6JbuqTl1Vkr_o1z6M02pJb55VWyIG-c5KLHlilF8GjMWX7TxHx7yh6VuF-2qeVwehWJOPOdP6YBbhc0jGco7LYTV1G320gQtTxWBu1L6R84YFwupw1Q5y0Z1nJOyALcxJXYE03pm-qoRh5Et6-3KxpoV9bHvCGmKWKhnu3j9JR0R9hUPPi1-7cbsD8S4CJqhw5Or9Bkjx4Ie3IMciOllsmMad5XK0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون پیشین رئیس موساد: ما به هیچ‌یک از اهدافی که داشتیم دست نیافتیم
🔹
ایگرا: حملهٔ آمریکا و اسرائیل ایرانی‌ها را به هم نزدیک کرد. اگر از من بپرسید که هدف و راهبرد این جنگ چه بود و ما چه به‌دست آوردیم، باید بگویم: آن اهداف اشتباه تعیین شدند و یا دست‌نیافتنی بودند و ما به آن اهداف دست نیافتیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/akhbarefori/653472" target="_blank">📅 08:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653471">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
دستیار سابق اوباما: توافق پنج‌ ماده‌ای در حال شکل‌گیری، به شدت به نفع ایران است
دنیس راس دستیار سابق اوباما اعلام کرد:
🔹
در صورت صحت، توافق پنج‌ماده‌ای در حال شکل‌گیری میان آمریکا و ایران به شدت به نفع ایران است:
🔹
ایران آتش‌بس در تمام جبهه‌ها، تعهد به خودداری از حمله به زیرساخت‌ها، لغو تدریجی تحریم‌ها را به دست می‌آورد اما هیچ اشاره صریحی به برنامه هسته‌ای آن در توافق نشده است.  آنچه آمریکا به دست می‌آورد، باز بودن تنگه هرمز با مکانیسم نظارت مشترک است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/akhbarefori/653471" target="_blank">📅 08:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653470">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddt8u7IhjFpCZ4gLHJQqzQzvB4kRRYOt-YFVJiRdvFqhPCVKP8CRYLjAJ-G0yIhvHgYt-3OCF2ObEFsFFBOtJgxIJSOmDUnSTmyGb-efvwX175OuVc7L7LK7kLrx2Iq_DruymdmgRVlvieUSSsPUe5ex4MK0yuwhY2In2h-KW8BbF2JsFyvCrKqv5Mj6Nf5caTvrIxOlS7j6HBHdL3zovoZiD2e9uhIGdLBk8GLaeWeYiC_jKfneQcyW9uztfPbQy5UZW2FIZtSfkAo499vtojXEZMun8blpTGqukfGrMScA89X9itLL7_YFWKJMt6ZySSsyCAS3p7H2AVTG4SMuJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۱ خرداد ماه
۵ ذی‌الحجه ۱۴۴۷
۲۲ می ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/akhbarefori/653470" target="_blank">📅 07:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653469">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MU262_cm_oDrkmb6mV1wQ4E6b1Y7DmndP-Qttt_g-oCaVT9hQ9uShiRSt7DViCWYH8b7COd9wq6p_DihlDPaLNlsomKRBh_0d74M5l7AqED8QKxRkUwkT4Bxe5QWzscFQONyIzTW36dwLOQgyzej_8IjAi9wh91ovQPu7QKsGBjIGBRFC9p_NYYlxRihKnA0URxX5IRTIfyQStIv0XX1Y3SEqrURdHw3viNfLmrZTr9cYJTbVmkVZaCCrCmngxBhOpHeHmjZioATzjaJGNnqWGLGVO-Og0OTqWVoLaooNdX9jVUq_I49TLMIlkR-bn5d_FxK38ZlgSkMnIOmh7Zexg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهم‌ترین ابزار نفتی ترامپ، در جنگ با ایران آب رفت!
🔹
ترامپ پس از یک هفته باز هم گفت در مورد ایران عجله ندارم؛ اما آمار ذخایر نفت آمریکا از واقعیت دیگری خبر می‌دهد.
🔹
جدیدترین آمار مخازن نفتی آمریکا نشان می‌دهد که ذخایر تجاری و ذخایر راهبردی آمریکا، در هفتۀ گذشته، حدود ۱۸ میلیون بشکه کم شده که بزرگ‌ترین کاهش هفتگی در تاریخ این کشور محسوب می‌شود.
🔹
بیشتر از ۸۰ روز است، عرضۀ نفت عبوری از تنگۀ هرمز به‌خاطر حملۀ آمریکا و اسرائیل به ایران متوقف شده و ترامپ با همان ابزاری که با آن از بایدن انتقاد می‌کرد یعنی آزادسازی ذخایر راهبردی، تلاش می‌کند بازار نفت را کنترل کند اما هنوز نفت بالای ۱۰۷ دلار در هر بشکه معامله می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/akhbarefori/653469" target="_blank">📅 06:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653468">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef66287df1.mp4?token=NVTAH8lDl2CcAC52R4N19OwEtfLTB-plOWBihCQwI_lX3s_qNC__KwFPt7ToHS0FBElcFwQvvMqHMxlzDv-u20pgG_Zco7VtPABZaVcFPV2pKGhU1RvHsl2w9LE8EjMfu4iRem5ov_kdhrYjpwNDfGIEht8HGcLp9DT7eUuh8BjsI8EMZhsgm2vry_67JFJxttoJLmsKGCS_rUpwbpL7ZNSkV7-GHX8OPBC1RQq9fxqR-qqr0EuFms80KIaJn98DrUfu5cjmS6V0igTY6gMG-MSzdd-Ui05dPjd-Hnq826YjvCU00qSHeyoKQ4XpVcImkDTWEpaTXqs86wOmCtI1cok0uS8uLVRBeQSQFghT82UHw4mcZ_5zJCrm7MQIQx089U4aznLKUaazDDpFl7EkM2bwOi1C7ZCEQbRZ2btLsysnJYqW5BE_F4oamKkqoJ53tHem-LRut4p4pS_Ki18wCKW3oqSOT5pddrIQShtLEgwymqzeA7kp9SQ5jqkiVQJccYsRas9xXUrgtwsxtEFjbcELAHVxto6peVa1NVUmF_X9kDTUd7C3KhQ8EEeu-yw2OKSZyJIk9cIlmrVUhr4ywGhFNzoHYgOip38QeOp8YOfGouVEG7kJCHmL8XWf4vtXLvy9LEyBWUQIoPY3Sbk00hl2bEEaDgtvHiqrki9enCI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef66287df1.mp4?token=NVTAH8lDl2CcAC52R4N19OwEtfLTB-plOWBihCQwI_lX3s_qNC__KwFPt7ToHS0FBElcFwQvvMqHMxlzDv-u20pgG_Zco7VtPABZaVcFPV2pKGhU1RvHsl2w9LE8EjMfu4iRem5ov_kdhrYjpwNDfGIEht8HGcLp9DT7eUuh8BjsI8EMZhsgm2vry_67JFJxttoJLmsKGCS_rUpwbpL7ZNSkV7-GHX8OPBC1RQq9fxqR-qqr0EuFms80KIaJn98DrUfu5cjmS6V0igTY6gMG-MSzdd-Ui05dPjd-Hnq826YjvCU00qSHeyoKQ4XpVcImkDTWEpaTXqs86wOmCtI1cok0uS8uLVRBeQSQFghT82UHw4mcZ_5zJCrm7MQIQx089U4aznLKUaazDDpFl7EkM2bwOi1C7ZCEQbRZ2btLsysnJYqW5BE_F4oamKkqoJ53tHem-LRut4p4pS_Ki18wCKW3oqSOT5pddrIQShtLEgwymqzeA7kp9SQ5jqkiVQJccYsRas9xXUrgtwsxtEFjbcELAHVxto6peVa1NVUmF_X9kDTUd7C3KhQ8EEeu-yw2OKSZyJIk9cIlmrVUhr4ywGhFNzoHYgOip38QeOp8YOfGouVEG7kJCHmL8XWf4vtXLvy9LEyBWUQIoPY3Sbk00hl2bEEaDgtvHiqrki9enCI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میلیاردها دلار در آتش؛ خسارات سنگین به نیروی هوایی آمریکا
🔹
تحلیل‌گر ارشد سیاست خارجی: سربازان آمریکایی کشته‌شده در کویت در سوله‌های بدون دفاع غافلگیر شدند.
🔹
صورت‌حساب تبعات این حملات و خسارات، اکنون مستقیماً روی میز ترامپ قرار گرفته و او برای انحراف افکار عمومی از شکست‌ها، به نمایش ساخت‌وساز در کاخ سفید روی آورده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/akhbarefori/653468" target="_blank">📅 04:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653467">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
۱۶ عملیات موفق از سوی حزب‌الله علیه رژیم صهیونیستی
🔹
حزب‌الله لبنان در واکنش به ادامه نقض آتش‌بس، شانزده عملیات موفق علیه رژیم صهیونیستی انجام داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/akhbarefori/653467" target="_blank">📅 03:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653466">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtNEeRzZQQhJioxQ8q3ge0b2ZUaPx6oLInbOgJ1RszqIAkBi78fOOQruB8MerZzvIn8q6hG_MAL_5mf0XB5nzC0k-YrVQOkdGyiSLGFqkyOu9fMEnr-lgF6FrwyGpGoFNw43lFWbTU_1sfztgVU8JIG2UY84lE44w4Cy8B6Nm4rLAvUewYrDWlZrmYdpQ-FU_tSoaLJhqKcVAb5gZbLLXVTk7p1F1_NAsa9F7dAlX6jbjHwOWQiWEp3bTU3KQVhMh9VyiBph0XlrW7ZHeRbdI2osaVFYKVXWwvVkjbvN1dlyV5GWwMrQvtEEjT2lkLMrsCG0uog_wm7cG7Sv3p79OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعویق رأی‌گیری درباره اختیارات جنگی ترامپ در مجلس نمایندگان
🔹
مجلس نمایندگان آمریکا روز پنجشنبه رأی‌گیری درباره قطعنامه موسوم به «اختیارات جنگی» را به تعویق انداخت.
🔹
این قطعنامه را اعضای دموکرات این مجلس با هدف محدود کردن اختیارات دونالد ترامپ در جنگ علیه ایران پیشنهاد داده‌اند.
🔹
نشریه هیل نوشته به نظر می‌رسد رهبران جمهوری‌خواه در این مجلس این رأی‌گیری را به دلیل به حد نصاب نرسیدن شمار نمایندگان حاضر خود عقب انداخته‌اند.
🔹
اگرچه اعضای جمهوری‌خواه در مجلس نمایندگان هفته گذشته توانسته بودند قطعنامه مشابهی را با اختلافی بسیار اندک رد کنند، اما روند تحولات در کنگره نشان از شکاف در بدنه حزب حاکم دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/653466" target="_blank">📅 02:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653465">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
هشدار بلومبرگ: احتمال رکود بزرگ در نتیجه بسته ماندن تنگه هرمز
🔹
بلومبرگ هشدار داد تداوم وضعیت تنگه هرمز تا ماه اوت (مردادماه)، خطر وقوع یک رکود اقتصادی ویرانگر در سطح جهان را به شدت افزایش می‌دهد؛ رکودی که ابعاد و قدرت تخریب آن می‌تواند با بحران مالی بزرگ سال ۲۰۰۸ میلادی برابری کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/653465" target="_blank">📅 02:17 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653464">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaZQa4_ss2xSfj9clRZQnCJa_S6_5ghUL3SljbSbSltZDhO79KSUSKREuIaMz3cMuRuMWD_9gTUdPY4ce8IUcXhoEs3o6NVMxrQSZrc98fOuSGh_XSbOVoGLTn7SP8icIX27YHxmSDUxZrjHgd9vQLoe0YGCsvh22iAr3M2xSNYpVr22Zx85R4nMHJu_tY0Op4ciAIUQ9doayp_97hJpOLFl6YipHWq6x-KyDpCwjbmjeuRXJTlh8N5mrdfyzMT-D2UhHUO5_FJp6xaq9wFj8R3awBfkTOMweOE1MKBiOfgU5mGMUYrydiCFQLkIImjDe40ndm6uhBHMagtcR9XyBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصطفی نجفی، فعال رسانه‌ای در تحلیل فضای مذاکرات نوشت:
🔹
۱. مذاکرات پس از بن بست کامل و رفتن طرفین تا آستانه جنگ با اضافه شدن میانجیگران دیگر و ارائه ابتکارات جدید وارد مرحله تازه ای شده است.
🔹
۲. پیشرفتهایی حاصل شده اما اختلافات و شکافهای مهمی باقی مانده است.
🔹
۳. موضوع توافق کامل یا مرحله‌ای اورانیوم، مدت زمان تعلیق، زمان بندی رفع تحریم، دامنه کاهش تحریمها و نحوه مدیریت تنگه همچنان محل اختلاف جدی است.
🔹
۴. تاکنون هیچ متنی مورد توافق قرار نگرفته است
🔹
۵. همچنان احتمال وقوع درگیری بیشتر از توافق است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/653464" target="_blank">📅 01:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653463">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPxwwBnaPwmjKaWwcs27XKUOgBcvzEczQ6d67vGAhImgIHxhPIqT6KqI-1l9m_0eCBGahBXVZZW35JTVB0eauIvHIXFfXzaoRk-433xHaFSmT5u8eU_GKt4hTkyvkTxVQJFlm7qaMa-iGM7CylB0HOSEpsODAY7IIzpV5c3FssGPgi2lMorR67DrX_ThoV0xapwfaDksghT7OKWeQeyRBJj_d8LEFrRU_TFe4YY2qZ-9yG_ixX1SDpf1VZUniG2cu7Zzk4u4EpAzsdezoTlEh-zE8sQPbiJt1KIeicaJWA-iwJKIVtCp-ZEJbNGR4t1c2gR-0-0cB7cgaNxWLJc_cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش فیگارو از تجارت مخفی اسرائیل در خلیج فارس
🔹
امارات ظاهراً دو فروند هواپیمای هشداردهنده پیشرفته از شرکتی اسرائیلی خریداری کرده
🔹
این هواپیما‌ها که مجهز به ایستگاه‌های شنود هستند، می‌توانند ارتباطات را در آب‌های سرزمینی خلیج فارس رهگیری کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/653463" target="_blank">📅 00:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653462">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
الجزیره: مذاکرات ادامه دارد/ به دو دلیل مذاکرات به ثمر نمی رسد/ افشاگری مهم واشنگتن پست درباره ارتش آمریکا/ ادعای اسوشیتدپرس درباره مرد اصلی مذاکرات
گزارش لحظه به لحظه از توافق احتمالی ایران و آمریکا را اینجا دنبال کنید
👇
khabarfoori.com/fa/tiny/news-3216870</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/653462" target="_blank">📅 00:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653461">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/368c47b54a.mp4?token=IvSdkNHNICTpnaYPj0MvzswAQZOoDmDRmdPECIn1zN4lpoLoARLuqGE6LEd_mn3_OUgLnsV_FO8dLj5hOb4JVUN1EzhSiUAwm4ljf_coIY75Hk-UIv0gQkNDUDHG3_mi2GkJTB3cQGvukYzsAwXWN0O5bhPhmg2Z5OpklFpWA4h3n3_lqBbFVc46slnS194cisFFMPkZ6JXbhNS8k7LPvOin6EEoCxpME0KX31OzkIqglIJ7XGPT8FlUFvrIyIQpyTuhTE-_OnIrt1UPKj5AI3Cewfxmv617C0av8ELrJfYUSM_O04b1O9eVK54z9qbPeCItsn2m_k7qp9b4BWqpAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/368c47b54a.mp4?token=IvSdkNHNICTpnaYPj0MvzswAQZOoDmDRmdPECIn1zN4lpoLoARLuqGE6LEd_mn3_OUgLnsV_FO8dLj5hOb4JVUN1EzhSiUAwm4ljf_coIY75Hk-UIv0gQkNDUDHG3_mi2GkJTB3cQGvukYzsAwXWN0O5bhPhmg2Z5OpklFpWA4h3n3_lqBbFVc46slnS194cisFFMPkZ6JXbhNS8k7LPvOin6EEoCxpME0KX31OzkIqglIJ7XGPT8FlUFvrIyIQpyTuhTE-_OnIrt1UPKj5AI3Cewfxmv617C0av8ELrJfYUSM_O04b1O9eVK54z9qbPeCItsn2m_k7qp9b4BWqpAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ارکستر سمفونیک تهران در نخستین اجرا در سال جدید در تالار وحدت، از فراسوی مرزها نواخت
🔹
این اجرا در آخرین پنجشنبه اردیبهشت میزبان علاقه‌مندان موسیقی کلاسیک جهان بود.
دراین‌باره بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3216851</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/653461" target="_blank">📅 00:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653460">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rn7GghqwW_i2Vp__Sz1r2u-8dxEJMBl5F-5tTJkXKOu-tEzqQmBbzLWoEKLz3BpaTwqOndcWy7q7IpDzlVbw6pdFXsXlEwx_Nl5YecjdIfAybELVw2p-M5lTYE6owAuyg74U8rTjOS0-WQZFsoraVVVIMmy6v2jquGdyTEF_2kem4sxJ1FHTysEcYg3Q9RY9uQWPL-oXxmZy_gwqrK-w_BFXxJNqM6dp40o-ln_-vFnnsEkyYVc5VCVWxDbiPSnh9g4jneIjWKu6yXPUemsgKmEmKSZN30ibGNsZiyt7PhpmtBk_yWRJiMcXCn6JDrRsCOK0cksGQbybjFpXmpQfbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: ایالات متحده ۵۰۰۰ نیروی اضافی به لهستان اعزام خواهد کرد
🔹
رئیس جمهور آمریکا: بر اساس انتخاب موفقیت‌آمیز رئیس‌جمهور فعلی لهستان، کارول ناوروسکی، که من افتخار داشتم از او حمایت کنم، و رابطه ما با او، خوشحالم اعلام کنم که ایالات متحده ۵۰۰۰ نیروی اضافی به لهستان اعزام خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/653460" target="_blank">📅 00:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653459">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
رویترز: هنوز هیچ توافقی حاصل نشده، اما اختلافات کمتر شده است
🔹
برنامه غنی‌سازی اورانیوم ایران و کنترل آن بر تنگه هرمز همچنان از نکات کلیدی مورد اختلاف است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/653459" target="_blank">📅 00:14 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653458">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔹
داغ‌ترین خبرهای امروز خبرفوری را از دست ندهید
🔹
🔹
ایران و آمریکا احتمالا بر روی این متن توافق می‌کنند + جزئیات پیش‌نویس ۹ ماده‌ای
👇
khabarfoori.com/fa/tiny/news-3216834
🔹
ابراز آمادگی احمدی‌نژاد برای مذاکره با ترامپ مقابل دوربین‌ها + ویدئو
👇
khabarfoori.com/fa/tiny/news-3216840
🔹
ماجرای دستور مهم رهبر انقلاب درباره اورانیوم ‌۶۰ درصدی چیست؟
👇
khabarfoori.com/fa/tiny/news-3216695
🔹
شوکِ ۱۰۰ درصدی به بازار لبنیات | صبحانه هم لاکچری شد!
👇
khabarfoori.com/fa/tiny/news-3216783
🔹
چگونه با وجود جنگ، تجارت جنسی در هتل‌های دبی رونق دارد؟
👇
khabarfoori.com/fa/tiny/news-3216745
🔹
ویدئوهای جذاب را در آپارات خبرفوری ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/653458" target="_blank">📅 00:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653457">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
العربیه خبر منتشره از قول این رسانه درمورد جزئیات پیش‌نویس توافق ایران و آمریکا را تکذیب کرد
🔹
این رسانه پیش از این مدعی شده بود که به پیش‌نویس نهایی توافق ایالات متحده و ایران با میانجی‌گری پاکستان دست یافته است
🔹
در خبر پیشین العربیه مدعی شده بود لغو تدریجی تحریم‌ها در مقابل پایبندی ایران به مفاد توافق، آغاز مذاکرات در مورد موضوعات حل نشده طی ۷ روز و تضمین آزادی دریانوردی بخشی از پیش‌نویس توافق است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/653457" target="_blank">📅 23:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653456">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213f1db8ef.mp4?token=UTvB_TxSpgezEHxtptJ8cByWDYWS0BBwT1NovvDJfimRZooLWUY7500FVi8Ml6KAE0HKRHOli7JCgscNGe4jDZ31Df5pIszDpElEe8VB7of2Nslo3tFoi6vCQOqjr-1E9xvOTutrXxy5AgeaDVcealYvBY5HfsNo8yQZLyIcpMcJxiuPBEQxV-49GT7M03r4XSRpBPiJH8foK617rPkbXghi9eI6MoJD3BxfVltU1LrSlsngQcA4AtK8qvesKw7r5vQbz3StOnIl1sCFi1LnHmyFCSU91IANdSvlo6Pn7QdKFZJ4yuDW7u0vQji4XtojBiykhRQWIBypMJ-4h7ZQ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213f1db8ef.mp4?token=UTvB_TxSpgezEHxtptJ8cByWDYWS0BBwT1NovvDJfimRZooLWUY7500FVi8Ml6KAE0HKRHOli7JCgscNGe4jDZ31Df5pIszDpElEe8VB7of2Nslo3tFoi6vCQOqjr-1E9xvOTutrXxy5AgeaDVcealYvBY5HfsNo8yQZLyIcpMcJxiuPBEQxV-49GT7M03r4XSRpBPiJH8foK617rPkbXghi9eI6MoJD3BxfVltU1LrSlsngQcA4AtK8qvesKw7r5vQbz3StOnIl1sCFi1LnHmyFCSU91IANdSvlo6Pn7QdKFZJ4yuDW7u0vQji4XtojBiykhRQWIBypMJ-4h7ZQ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مخبر: اروپایی‌ها چپ و راست برای عبور از تنگه هرمز به ما پیام می‌دهند
🔹
تنگه هرمز سرزمین ماست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/653456" target="_blank">📅 23:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653455">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3db5c1fc5a.mp4?token=ENTCf7UKIp4TPjdyCFnsChXBLclYtwPHVdcG28TKAI2pmAtm8uHJgfsVhsZMn5HPT5ZDDngsZomBQOWDhjZ8LO26sMjl0a6eDUUrxqx7T5vi6KEl1_dzET7Vu1YdS1HSAoJEuy2uMCHfeZ32b4XEfyhEPo8WsPpGV-x1lCNQ7LZkIr0xqhErfuPRTKxCNXJ6n6coLpWRm0tWbyRj7zMT8BJxDQSjdEMchldtPyAbGluwOIFW83LlC1P3brju7GkQLp1CIloHQI5oIRaXPl20DrE7dIaZv7-7Nl2w8tEL-Y0Z6LgqqjWJl-3MTZbDExEDa7ZxeRas8Wq-TfJKm3sEfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3db5c1fc5a.mp4?token=ENTCf7UKIp4TPjdyCFnsChXBLclYtwPHVdcG28TKAI2pmAtm8uHJgfsVhsZMn5HPT5ZDDngsZomBQOWDhjZ8LO26sMjl0a6eDUUrxqx7T5vi6KEl1_dzET7Vu1YdS1HSAoJEuy2uMCHfeZ32b4XEfyhEPo8WsPpGV-x1lCNQ7LZkIr0xqhErfuPRTKxCNXJ6n6coLpWRm0tWbyRj7zMT8BJxDQSjdEMchldtPyAbGluwOIFW83LlC1P3brju7GkQLp1CIloHQI5oIRaXPl20DrE7dIaZv7-7Nl2w8tEL-Y0Z6LgqqjWJl-3MTZbDExEDa7ZxeRas8Wq-TfJKm3sEfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مخبر: مردم تا خون بهای رهبری و‌ شهدای جنگ رمضان را نگیرند، دشمن را رها نمی کنند
🔹
مشاور و دستیار رهبر انقلاب: ویژگی‌های رهبر سوم انقلاب منحصر به فرد است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/653455" target="_blank">📅 23:38 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653454">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e2ba597cb.mp4?token=TkucCxDgoaDYyHB-EcNjQGZexioe7_AxlRe0qTlr_4_ClsL_8leYyhkyFWyx2zDzJGhrwX4PN4eYMVnvCVomkun2EdqFttYv5KYxoCtKv6cLUWqg8BxIKCSZrhmjoxi1HQ4Bwxvvh9eGgBNJrmiFQnxgbU49MeEcLCMI_-_bljweXNYoVzNX2LI9n33bMXdzkGxeF9LDOQS8O2fkCTAtvhn9AWZh4d4X3hFZHUVmTs7FBWOqMrDNKBPc67mG4Avna2Mm3s9TSUjf2L_B4fDV0QXWWjjIQTIQDEUvBqw31WRVziYGm0qzlCdGHROvXSulwRTMapRT1AgjdlES5x-3iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e2ba597cb.mp4?token=TkucCxDgoaDYyHB-EcNjQGZexioe7_AxlRe0qTlr_4_ClsL_8leYyhkyFWyx2zDzJGhrwX4PN4eYMVnvCVomkun2EdqFttYv5KYxoCtKv6cLUWqg8BxIKCSZrhmjoxi1HQ4Bwxvvh9eGgBNJrmiFQnxgbU49MeEcLCMI_-_bljweXNYoVzNX2LI9n33bMXdzkGxeF9LDOQS8O2fkCTAtvhn9AWZh4d4X3hFZHUVmTs7FBWOqMrDNKBPc67mG4Avna2Mm3s9TSUjf2L_B4fDV0QXWWjjIQTIQDEUvBqw31WRVziYGm0qzlCdGHROvXSulwRTMapRT1AgjdlES5x-3iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مخبر: مسائل ما با آمریکا وقتی حل می‌شود که آن‌ها مطمئن شوند که ما به‌حدی از قدرت رسیده‌ایم که نمی‌توانند در مقابل ما کاری انجام دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/653454" target="_blank">📅 23:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653453">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a351191c93.mp4?token=uk9HOZt_JVluJNQFL1EqpkC59D0hNwJ6aB6NQsFmEk8kugIBhyzbYG6s6UF46pN6g6KrxXiZtsCaynLv6rs6cQGXFPo--3MJwT2aUHZ8H6D8iSJ4ZFJFsD85w4Cku4EY0YNyXmvp_Khcrt4xLd5ipBV1lkCwQ6owIOKk2oeJPXRPhGwI31zDQ4HzHor3xy1XhnSAouE27XbJx0shtubbiA6LDncRDHm-lciag5C5_XTjtikLLpK6kVKuN_Vgp3l0iyYv3vjfXCtaqWEzls-sPjpxBhOdkyk_KVonZCmyhdkxHKRDeYRWbeV5Fa9T_gUKQNyiB8GL_H77XKfiCSrSDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a351191c93.mp4?token=uk9HOZt_JVluJNQFL1EqpkC59D0hNwJ6aB6NQsFmEk8kugIBhyzbYG6s6UF46pN6g6KrxXiZtsCaynLv6rs6cQGXFPo--3MJwT2aUHZ8H6D8iSJ4ZFJFsD85w4Cku4EY0YNyXmvp_Khcrt4xLd5ipBV1lkCwQ6owIOKk2oeJPXRPhGwI31zDQ4HzHor3xy1XhnSAouE27XbJx0shtubbiA6LDncRDHm-lciag5C5_XTjtikLLpK6kVKuN_Vgp3l0iyYv3vjfXCtaqWEzls-sPjpxBhOdkyk_KVonZCmyhdkxHKRDeYRWbeV5Fa9T_gUKQNyiB8GL_H77XKfiCSrSDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مخبر: بحث پایان منطقه‌ای جنگ، دریافت غرامت، مدیریت تنگهٔ هرمز و رفع تحریم‌ها چیزهایی نیست که مردم و مسئولان از آن بگذرند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/akhbarefori/653453" target="_blank">📅 23:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653452">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USkOSpTt0bwbTKjLqVUlcsr5vjq07rsYBvDho37hahljhX8y05INc2gHZlyGOqH4YXbzzywGKe1xxilNrsvlZIln0OCmge8N1IR2t0k0p10jg86uFCyE8XaU1ZYC9Gd1BmzbBNS_Zq25V1cOWAKg9n3YrMdRogD3yQ8mcnB5D59biQa53zOIPeKN8P7vRQf0bzVPNMsjU8aldQVrQ4I642U0_n2iQzs6Eh-p73dPaIfYT51TymUWK80BhqlZYNe_pjxlOPvaXycCDOADmKHPwIG0v6tR9GFdHAdBjE8KcRGSudHhhD0Th6sOQkpSigyfcq5YYMEF0CJp2yIYwpXGcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رويترز: با نزدیک شدن به بحران عرضه، ساعت بازار نفت به شماره افتاده است
🔹
صنعت نفت در مواجهه با بزرگ‌ترین شوک عرضه انرژی در تاریخ مدرن، انعطاف‌پذیری فوق‌العاده‌ای از خود نشان داده و اهرم‌های متعددی را برای کاهش ضربه جنگ ایران به کار گرفته است. اما در صورت عدم پیشرفت در مذاکرات صلح، بازار جهانی ممکن است تنها چند ماه با یک نقطه شکست فاصله داشته باشد.
🔹
بازار نفت قبل از اینکه تشدید کاهش عرضه به طور جدی آغاز شود، موجودی انبارها را به سطوح بحرانی برساند و باعث افزایش شدیدتر قیمت‌ها شود، احتمالاً حدود سه ماه فرصت دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/akhbarefori/653452" target="_blank">📅 23:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653451">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuD22qei9PDUpZbfxBQGMs8SJV4_PffwZke8x_uSVHtLl6JEtC3trVbFbW1SHigvFRU5YAeFF7S64jYEUCVqOSqiB2wtGJ_Ru0WEtTU9OOcTduRJvufOcvfcyvGDV6QBOOGmcoeEDk5X9EYMC09BxsRf43xstp9ShOP3VkSA1MgaJZzPUf1eso01jfnjuqdYNvGlsPJAgqLJ7bx91n-uq94id3chlRKXOMMUpcb1zgkhHcRGflYNKKk1Yizvt4W9tnqk0juoHkjnD-tOUggzRdgXexO80Sej8YilUW0VxN7jABFD7i9FTHfdmS6tawt9mQwafmM-nTOjl93eIKOhzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری برای روز اهدای عضو؛ «نبض ماندگار»
🔹
همراهان عزیز خبرفوری، برای شرکت در این فراخوان کافی‌ست به پویش «نبض ماندگار» بپیوندید و با ثبت کارت اهدای عضو، سهمی در ادامه زندگی دیگران داشته باشید.
🔹
برای شرکت در این پویش:
عدد ۱۲۰ را به سرشماره ۳۴۳۲ ارسال کنید
یا به لینک زیر مراجعه کنید:
https://ehdacenter.ir/api/gateway?code=120
🔹
پس از ثبت‌نام و دریافت کارت اهدای عضو، تصویر کارت خود را برای ما ارسال کنید تا در این حرکت انسانی و ماندگار کنار هم باشیم
👇
#نبض_ماندگار
@Ertebat_baforii
@Alo_forii</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/akhbarefori/653451" target="_blank">📅 23:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653450">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
واشنگتن‌پست: بار اصلی دفاع از اسرائیل بر دوش آمریکا بوده است
🔹
یک ارزیابی جدید از پنتاگون نشان می‌دهد ارتش آمریکا در جریان جنگ اخیر علیه ایران، برای محافظت از اسرائیل تعداد بسیار بیشتری موشک رهگیر پیشرفته شلیک کرده‌اند تا خود ارتش اسرائیل.
🔹
این مسئله اکنون نگرانی‌هایی درباره آمادگی نظامی آمریکا و تعهدات امنیتی این کشور در سایر نقاط جهان ایجاد کرده است.
🔹
سه مقام آمریکایی گفته‌اند ارتش ایالات متحده بیش از ۲۰۰ فروند رهگیر سامانه دفاعی تاد که نیمی از کل زرادخانه پنتاگون را تشکیل می‌دهد برای دفاع از اسرائیل شلیک کرده‌اند.
🔹
نیروهای آمریکایی همچنین بیش از ۱۰۰ فروند موشک رهگیر استاندارد-۳ و استاندارد-۶ را از ناوهای مستقر در شرق مدیترانه برای مهار موشک‌های ایران شلیک کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/akhbarefori/653450" target="_blank">📅 23:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653449">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnwEWS-0tWt7mkKqFP8rAFfvdAzSx3rXMkr8JUcGACTgNBkPCdpM4YUr1CoptniaCabWuehUyo_f5hCQhG2C58tKkdRioMy9vlMaQsUAt5ZjBwWtOJymNN6Ld9y4XYCFeiZV_xGkI5FPZRoAS7TM8xys57k0eZvcIYZ4VcPLUqfbElDQQaWJUsA5242Y-zz0U5IoGMrR-7hp4ro20q45u2PhFFxGxtxS2VDeNL27ohYBWRSC9dFfdi8GJpTeVast85XXwqDrPg93Ji9uHk4Fa_rHSKSwmwPfHUB5jdWqoxqzLsPD-gZkUzvOC_nCFmA00NUzWtx2gLPJLKJzOwvkrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه ژاپنی: ایران می‌تواند با جلوگیری از عملیات تعمیر و نگهداری کابل‌های اینترنتی زیر تنگه هرمز، بدون هدف قرار دادن مستقيم آنها بر این کابل‌ها اعمال حاکمیت کند
روزنامه ژاپن تایمز :
🔹
از جمله وسایل ارتباطی مهمی که از تنگه هرمز عبور می‌کنند، یکی از شاخه‌های کابل AAE-۱ (آسیا، آفریقا، اروپا) است که نقاطی از هنگ‌کنگ تا ایتالیا و فرانسه را به هم متصل می‌کند.
🔹
داده‌هایی که از طریق این کابل‌ها منتقل می‌شوند شامل ویدئوها، ایمیل‌ها، شبکه‌های اجتماعی، تراکنش‌های مالی و ارتباطات دولتی هستند.
🔹
ایران هم می‌تواند خودش مستقیماً به کابل‌ها حمله کند و هم شرکت‌های کابل‌گذاری را از انجام عملیات، چه برای تعمیر و نگهداری و چه برای نصب کابل‌های جدید، بازدارد.
🔹
نظامیان آمریکایی نتوانسته‌اند مانع عملیات ایران از سواحل طولانی این کشور در خلیج فارس شوند و تهران همچنان «توان نظامی قابل توجه» خود را حفظ کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/653449" target="_blank">📅 23:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653448">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ابراز آمادگی احمدی‌نژاد برای مذاکره با ترامپ مقابل دوربین‌ها
گفتگوی خبرفوری با احمدی‌نژاد را اینجا ببینید
👇
khabarfoori.com/fa/tiny/news-3216840</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/akhbarefori/653448" target="_blank">📅 22:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653447">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
پزشکیان: سر خم نخواهیم کرد
🔹
وزرا و کارشناسان ما شبانه روز سرکارند، بدون حتی یک روز تعطیلی
🔹
رئیس‌جمهور در همایش راویان ایران : برای عزت و سربلندی ایران حاضریم تا جای ممکن فداکاری کنیم و باکی از شهادت نداریم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/653447" target="_blank">📅 22:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653446">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
اسماعیل کوثری، عضو کمیسیون امنیت ملی مجلس: اگر امارات از مکان‌هایی که در اختیار آمریکا گذاشته علیه ما استفاده کند، قطعا آنجا را زیر آتش موشک‌های خود می‌بریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/653446" target="_blank">📅 22:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653445">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r750vc-gsCsnH66Q8MRueb3o1CBGSYP3MPmrKxPP-3mF4YLdZYTV8NEMLES8C_KRfgzU57XOT_0NAn_wa6nNUhQCfrGzNZfRg9mK8QNOFLIPJwoatZxOm1O12Yl4DXiuVk2JU1ANjltP4smotMnGofx-BXP4bCyPL_RN0uHf5FtUXOKhqMOyxq-S2Da3LX3Pza1lAeJiXlaEiliPtgQTqc-_LYorEGXv3zs54QhD8uZ2fuKgo1_RI62PgoIj0N2izTRmydn-lEHKS3aAxu04Fc5aye9zvO0Q6J8XEc0rNbgoC3ORbSYxbLdsiweYCQw24xpb01fN7yUNjxEd9DK3aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس از ملونی و مودی که زیادی صمیمانه است | هدیه آب‌نبات به جورجیا ملونی | حرف‌های درگوشی پشت نخست‌وزیر هند!
🔹
در جریان سفر رسمی نارندا مودی، نخست‌وزیر هند، به ایتالیا، یک اتفاق ساده بیش از مذاکرات سیاسی و اقتصادی توجه رسانه‌ها و شبکه‌های اجتماعی را جلب کرد: یک سلفی در کنار کلوسئوم و هدیه دادن یک بسته آب‌نبات «Melody» به جورجیا ملونی.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3216749</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/653445" target="_blank">📅 22:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653444">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BV0bXh0TY44Ff6UqK0AMTrlcN20X-Y-6RkN616Ri_qQTxACQ6KbzdM2aQWTcWo-sbTStXkCsT5A1QxQhjvA9v48AChVlxliSNh2edsVSLEUpwUb91ytEdA1zhJUmWM8G8hDv0TLXz1TpEX2lu3bFgPrQeqULc-7foVx5GNgQVFYMkyENbKYuPDzAHUYfbyJcCkL9xLWrCtJK7PoWYffpLYBzcGFFBDfGdrwvwTgheljgaaV2IA6ou-DyVo77c0FLiCHDMP93JxU7deN2IVqOuIHPkV0X537S5-b8PYyv8WO0YT9oF3kzmXuKPGizqbVel1Na9YWqslCGBEWoVzIGWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعرفه گمرکی واردات تلفن همراه اعلام شد
🔹
بر اساس بخشنامه جدید دفتر واردات گمرک ایران و در راستای ضوابط اجرایی قانون بودجه ۱۴۰۵، نرخ واحد مالیات بر ارزش افزوده یک درصد نرخ مندرج در ماده ۷ قانون مالیات ارزش افزوده که ۹ درصد است، اضافه می‌شود.
🔹
در این بخشنامه نرخ ارز مبنای محاسبه ارزش گمرکی گوشی تلفن همراه معادل متوسط نرخ ارز بهمن ۱۴۰۴ در مرکز مبادله و هر یورو معادل ۱۵۵ هزار و ۱۹۶ تومان تعیین شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/653444" target="_blank">📅 22:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653443">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">مراسم دعای ندبه_جلسه 53</div>
</div>
<a href="https://t.me/akhbarefori/653443" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه پنجاه‌وسوم
رائفی‌پور:
🔹
0:13:30 آیاتی که به فرمایش پیامبر در قرآن جابه‌جا شد
🔹
0:26:40 حرام بودن گوشت حیواناتی که گاهی حلال می شوند
🔹
0:39:35 کثرت منافقین در ولایت پذیری حضرت علی(ع)
🔹
0:55:25 اهمیت و درس آموزی بالای خطبه غدیر
🔹
1:00:40 نازل شدن آیه در رابطه با پرداخت صدقه قبل از دیدار پیامبر
🔹
1:19:00 دعا و نفرین پیامبر راجب دوستان و دشمنان حضرت علی(ع)
🔹
1:24:30 علت داشتن عمر زیاد ظالمان
#دعای_ندبه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/akhbarefori/653443" target="_blank">📅 22:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653442">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromطوسی آنلاین . خبرفوری جنگ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c940235b7b.mp4?token=llSjw0pckQ9TXR9s49kASSdtls6rW1MPZtFTtD4Bh_oOvDXuBqI5zKel4rcFupd1OCX1Z6vvTuq4hI_-XzTe3n_zE5yGDGTgNti3DBia5oimeA55itx4Hc_ZgwIQoKESeTBlqlsVe41Xdz9nBTmCTBTNFhhQoLPXLtnUhF8hX20vmwo3hJ3DWB8n9mDQ1_e1B_f9HZ2TZQZhG_w7B-2LIWs2KBiU8pUuFTiH-MfiDn913nP7te7VV0Hy4IwCeqtYtB7yCICcUPDf4Dhw6tYOXmC0oWycvTD27L9lvX5lhyoybVW7Ry6rha7TOMsrORiWkapz0YC5f8HbJ-paKjgwAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c940235b7b.mp4?token=llSjw0pckQ9TXR9s49kASSdtls6rW1MPZtFTtD4Bh_oOvDXuBqI5zKel4rcFupd1OCX1Z6vvTuq4hI_-XzTe3n_zE5yGDGTgNti3DBia5oimeA55itx4Hc_ZgwIQoKESeTBlqlsVe41Xdz9nBTmCTBTNFhhQoLPXLtnUhF8hX20vmwo3hJ3DWB8n9mDQ1_e1B_f9HZ2TZQZhG_w7B-2LIWs2KBiU8pUuFTiH-MfiDn913nP7te7VV0Hy4IwCeqtYtB7yCICcUPDf4Dhw6tYOXmC0oWycvTD27L9lvX5lhyoybVW7Ry6rha7TOMsrORiWkapz0YC5f8HbJ-paKjgwAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های زیبای جفری ساکس رو ببینید</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/akhbarefori/653442" target="_blank">📅 22:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653441">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zv6My12oQyG9i9TG-CSTtfslvBvu7yWOVLhmEaW86Dt2N3JyN9bsErmrOaACCm5uCWa8mmHEbiJnsDsbaoFnMkFA8U3gtmkyEl7FiJyzBf_GoKOw56YuwfvPj6dl9-i9HYw6dOqvmX9IvHdi4U8ZDRpihSqH8_jmOVZKfqhjdq08DtezKN1lTAsBUdyaM5cg2dDUFZyyaneOKL_q1ohr4uKVKo2AkrDwbkjyCOdqkcpQAFS7vg6iLOvdLv59bv_4wwaP4TcOStWahtK1FrT5Z-dEbQndafpK-8i-04MxQDfQBJ-B81uhph9eMjWE6hHIBDAHwqjFujXa8hOy0T_l-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری برای روز اهدای عضو؛ «نبض ماندگار»
🔹
سالانه هزاران عضوِ قابل پیوند، همراه با بیماران مرگ مغزی دفن می‌شوند؛ درحالی‌که هزاران نفر هنوز در انتظار زندگی‌اند.
🔹
با ثبت کارت اهدای عضو، به لیست بیماران در انتظار پیوند پایان ببخشیم.
🔹
برای شرکت:
عدد ۱۲۰ را به ۳۴۳۲ ارسال کنید
یا از طریق لینک زیر ثبت‌نام کنید:
https://ehdacenter.ir/api/gateway?code=120
🔹
پس از دریافت کارت، تصویر آن را برای ما ارسال کنید
👇
#نبض_ماندگار
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/akhbarefori/653441" target="_blank">📅 21:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653440">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HquzXOZKZqObo5aIM1236r_OcrZi6SIGyf80ttwChzzcLqU4QJBEUdUzrdNFvIUK0foyHaK-TuDXq2geXMzZK8oM8miVbeasgCAE1DpnxjDhNS0sDfh6aWU-uewxntaSNGvSO7aqxGcs0RgJImdTbISm0zQv54H2wGvWCYtyjAd_pE68Z_J7CIOXUwY84TBSa_ZMf2oWVhsUczR5XsbfokYe67W65J5k5cN1eP6HnWJ4WAhUoA31qwgDnkvx-CbW-S9RCVziKqcRUqtOJs8DzJ49ioXaYCPzEDmO0uDRxlWppQqFigSCIkW0ZW_yA8MToWO7eF9alY2tpXExfZd3ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اذعان رسانه صهیونیستی به قدرت نقطه‌زنی حزب الله
🔹
اسرائیل هیوم گزارش داد، در نبرد قبلی فرماندهی منطقه شمالی بعد از حمله حزب الله علیه تمام سیستم های جاسوسی در مناطق مرزی وارد یک حالت کوری و نابینایی شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/akhbarefori/653440" target="_blank">📅 21:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653439">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bf946ca32.mp4?token=QLyXDbp_WmGNumJRxsmQzgBXdyTNqWzrmGZem45joYMlpYNn3MEUMXpe0W3H-rOC0bOceuyMSiEyJhaE3CKvsujB_DAZpEYPZ4RxRiJgvTjKxoB-rlSdv6ucFaz8kdroOYTdCdHzu6Gh0agipoX5OFKfmSyb3s4fMI_NLE5DQGLgZ4CWN_U9dYfiPjUQ_zwmAkEZ9NsJ4IPl4NgalyNyTtG8VG6hWv1oaNLRjhDOwwuTvrz6pTFAa42K45Yia_cGFy7Glw74ewHzvPJZ2kQfwLxkXdZZEFlMbCQ4vOXyQ7Fv1toHUupUd6x-3J2F2UBW4fbuuo1SpZksnmYwa68agw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bf946ca32.mp4?token=QLyXDbp_WmGNumJRxsmQzgBXdyTNqWzrmGZem45joYMlpYNn3MEUMXpe0W3H-rOC0bOceuyMSiEyJhaE3CKvsujB_DAZpEYPZ4RxRiJgvTjKxoB-rlSdv6ucFaz8kdroOYTdCdHzu6Gh0agipoX5OFKfmSyb3s4fMI_NLE5DQGLgZ4CWN_U9dYfiPjUQ_zwmAkEZ9NsJ4IPl4NgalyNyTtG8VG6hWv1oaNLRjhDOwwuTvrz6pTFAa42K45Yia_cGFy7Glw74ewHzvPJZ2kQfwLxkXdZZEFlMbCQ4vOXyQ7Fv1toHUupUd6x-3J2F2UBW4fbuuo1SpZksnmYwa68agw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر جنگ تمام شود و محاصره دریایی باقی بماند، آمریکا توانسته دست برتر را برای خود حفظ کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/akhbarefori/653439" target="_blank">📅 21:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653438">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCUM1p6TC5_VChTEJpQvlQzu6MDY-83G6MmCr76iXYjGP2sUjBhRX1YPST02Bxx6u6HiUwXOmLY7_G13Mm5k1colGD23ICYdCHZuua_rR0qMbwOpytPdWuXJ3ki_Eg322bgZiZccnhMl6clBbqeaLALZ1uqaYJHOjNylq1c3vWj2x4Cd566iNikGutkJZIOu7sTDW3ezGkaDRnVAvm_MwkbsU6T8QVL9z214phtJRcZUIzo5ww1egufBFHuMr-zGjsAOLof2FamAGTr3Jbzu7sY2j3_vVGM4zwK5IrnbEcisbGA2bDGpoPAq7urF6CjCndutCC6qh67qvrre0eCibw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویتز: ایران در حال تثبیت کنترل خود بر تنگه هرمز است
🔹
ایران با ایجاد ایست‌های بازرسی، توافق‌های دیپلماتیک و بعضاً دریافت «هزینه»، کنترل خود بر تنگه هرمز را تثبیت می‌کند.
🔹
ایران در حال اجرای یک سیستم چند لایه‌ای برای عبور کشتی‌ها از طریق تنگه هرمز است، آن هم در شرایطی که کشورها تلاش می‌کنند ذخایر رو به کاهش انرژی خود را که به دلیل جنگ به شدت محدود شده است، تأمین کنند.
🔹
آمریکا نسبت به تبعیت کشورها از کنترل‌های ایران هشدار داده است، اما برخی دولت‌ها و شرکت‌های کشتیرانی این خطر را می‌پذیرند.
🔹
مکانیزم جدید ایران شامل یک سیستم اولویت‌بندی است که حق تقدم را به کشتی‌های مرتبط با متحدانش یعنی روسیه و چین می‌دهد و در رتبه‌های بعدی کشورهایی مانند هند و پاکستان قرار دارند که روابط نزدیکی با تهران دارند. پس از اینها نیز سایر دولت‌ها قرار می‌گیرد.
🔹
وضعیت به شکلی است که تنگه هرمز تنها با تأیید حکومت ایران بسته یا باز خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/akhbarefori/653438" target="_blank">📅 21:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653437">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
واشنگتن‌پست: آمریکا نیمی از ذخیره موشک‌های «تاد» را در جریان جنگ علیه ایران مصرف کرد
🔹
روزنامه واشنگتن‌پست گزارش داد که واشنگتن در جریان جنگ علیه ایران بخش بزرگی از ذخایر موشک‌های رهگیر خود را مصرف کرده است.
🔹
ارتش آمریکا در این جنگ مقدار زیادی از موشک‌های رهگیر خود را مصرف کرده؛ حتی بیش از آنچه صهیونیست‌ها استفاده کرده است.
🔹
آمریکا برای دفاع از اسرائیل بیش از ۲۰۰ موشک سامانه «تاد» شلیک کرده است.
🔹
این تعداد تقریباً معادل نیمی از کل ذخیره موشک‌های «تاد» پنتاگون ارزیابی می‌شود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/akhbarefori/653437" target="_blank">📅 21:44 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653436">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
یک تحریم دیگر علیه ایران از سوی کاخ سفید
🔹
آمریکا، سفیر ایران در لبنان را تحریم کرد
🔹
وزارت خزانه داری آمریکا در ادامه اقدامات خصمانه خود علیه جمهوری اسلامی ایران، محمدرضا رئوف شیبانی، سفیر کشورمان در لبنان را تحریم کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/akhbarefori/653436" target="_blank">📅 21:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653435">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4I63IiRfQCRxn5mNKgwUbI9myEJNBgfo910iewzt_Ysoz-zOnCSZMHA73zzWYaqDtnZC5SgfoqoACU-N-oSVkOpTof0TaaIF1VXP0hdbXGd6i9p3Ym95uM8BfQ8F_NRl2hxUofQtsW_G5rda0K9MfWCKIomU_NdaEBPOqu3BQPttUA7MZb9R7MvZY25RpPr24KFRnxFIyZxeMP4EW4LRw8mgNBE-bAzPGwOPkP7IVKfPsxVN5oTOl9D852iZoD1rcl0hu756wcwRsM1TTowym32kp29QYJqa46G-oi79zQPeqCoz1o2ME2HHxQKyrXy2B8XWRZrtJSszqCFVAY9cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فایننشال تایمز: بحران خلیج [فارس] احتمالاً تازه از الان آغاز می‌شود
🔹
کشتی‌های که پیش از بسته شدن تنگه هرمز از آن عبور کرده بودند، تاکنون عمدتاً به مقصد رسیده‌اند.
🔹
اما از اواخر ماه فوریه دیگر کشتی‌های حاوی نفت، گاز طبیعی مایع، مشتقات نفتی، اوره، هیدروژن، هلیوم و... از تنگه عبور نکرده‌اند.
🔹
تا به امروز، کمبودها عمدتاً ذهنی و فرضی بوده‌اند؛ اما با کاهش و تخلیه ذخایر انبارها کمبودها واقعی می‌شوند.
🔹
از این پس، جای خالی محموله‌هایی که حرکت نکردند، به شکلی فزاینده‌ای احساس خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/akhbarefori/653435" target="_blank">📅 21:30 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653434">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd4e2eeed.mp4?token=SVKU6t6HDeIHA5ytNnNlzaYdlTMhLPWo3jlexiWngVS-_FqrBBFVVIobg_y6cghTTNUes6UF7cw7Mig-o2OP-xRmnVh5FSm5Id2K3kFcKglaZfeIrD9QmIo3wMA6Ubbs2rsxCmHGnAFKaQ7gyDSiYZR7APVVCylIXScb9v6ZH0w8EquKFF0LIGAESZZ8pmYEAji7x5GafV6CsNYC26Cqk29d97L6VJHoUrZ31aKFsKcySJxMHN6OvQyVLn8DdcXzYGB-sy0V8VUfBTg4AA10jlb2pc_0lM-Oq9fOlMMNxCaEsIg0Cp7S1gjwfs_M_EgLOtnRrKDLqqjM-bZiK6Q4ubRPpGIFhWK_3zDL8R2j_UaGlukgKlIJRiExwfrXAPTOKtEaUGl7bcaYsJ70IpPOPjq0ZUlC7CrzNtdoCZ86JUUzxAZG0uySDtO2nxPgsVzm6mmWBljqRXRUyZYVe7Kf9QtWd3qvf88Qmb_5MaO5_-lIoi_SWxPy2o5hHiV4jdwIRVlmQZoN6NF8toOfYf_awHUiXHNfAmoDPEMs7s4EOq9vsTPVOoFwZvnqJrKg9TGvDNalI2_peII0K3aefjuZ4ECno8W6_W3hWdk9_rRCKUf2oW0IgQFOnf7RgNFZRtFuCyQUXmLdrdMLWmfN1scWkR3uwL5OoTzL5trkSNfJnE0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd4e2eeed.mp4?token=SVKU6t6HDeIHA5ytNnNlzaYdlTMhLPWo3jlexiWngVS-_FqrBBFVVIobg_y6cghTTNUes6UF7cw7Mig-o2OP-xRmnVh5FSm5Id2K3kFcKglaZfeIrD9QmIo3wMA6Ubbs2rsxCmHGnAFKaQ7gyDSiYZR7APVVCylIXScb9v6ZH0w8EquKFF0LIGAESZZ8pmYEAji7x5GafV6CsNYC26Cqk29d97L6VJHoUrZ31aKFsKcySJxMHN6OvQyVLn8DdcXzYGB-sy0V8VUfBTg4AA10jlb2pc_0lM-Oq9fOlMMNxCaEsIg0Cp7S1gjwfs_M_EgLOtnRrKDLqqjM-bZiK6Q4ubRPpGIFhWK_3zDL8R2j_UaGlukgKlIJRiExwfrXAPTOKtEaUGl7bcaYsJ70IpPOPjq0ZUlC7CrzNtdoCZ86JUUzxAZG0uySDtO2nxPgsVzm6mmWBljqRXRUyZYVe7Kf9QtWd3qvf88Qmb_5MaO5_-lIoi_SWxPy2o5hHiV4jdwIRVlmQZoN6NF8toOfYf_awHUiXHNfAmoDPEMs7s4EOq9vsTPVOoFwZvnqJrKg9TGvDNalI2_peII0K3aefjuZ4ECno8W6_W3hWdk9_rRCKUf2oW0IgQFOnf7RgNFZRtFuCyQUXmLdrdMLWmfN1scWkR3uwL5OoTzL5trkSNfJnE0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت پرده عقب نشینی ترامپ از حمله به ایران
🔹
همکاری تسلیحاتی ایران و چین وارد مرحله مینیون‌ها شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/653434" target="_blank">📅 21:30 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653433">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gF89unhyjmxx2QuysMei-OkmjuEHXNeHfi6BF-vsC6Sm5U1Rucf7NwKNbQFEIvJsYKjaVH0kUBRDu5xm1WILaUTgNQvenIvVYFuLGbJSUek8MkfvnQIJA7zU3sE_Q4sGPpzPNKJ3IwgrqcZuiCHp_IytNn7-LF3K8yNQF1ybfT6xx6yMm0gbIDI4brYdxjREDc__lXJIF_m8sI2cvm21THxO-6GEZE-Gl7t05s4K96z9N8dGoMz7_5IkRVSFFCmJ_w7kKOvmlZpF6Rg_4Ts1MXt2e4_Qyimwy-VvIRoM3FqroLp-aFtJeYwEcKjjs3w7vse0pVwtfqdf3zJQNBzHRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان اطلاعات سپاه: جمع بندی نهادهای اطلاعاتی آمریکا این است: «گذشت زمان به نفع ما نیست و برای رهایی از مخمصه چندلایه، ابتکار و تهدید ایران را جدی بگیرید.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/akhbarefori/653433" target="_blank">📅 21:21 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653432">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ae5f4c459.mp4?token=h_YaeDy_wh1COlaD2p_DwFrhvQKspT3s_wqZ_U-eIfi1R8Yh9C8xLwCQZswZqvJr0cWYWN7Z12a_PIMOhOJTkSpvX_Vg95IpdebNl1IcaGtNTSApjVvZT8n9-OfdXSOylpSPP46_G0kPwD1fplkUEenOAfs7AyAs62NygVlpk1UC2i34E-l1UWNi4cWdFpHabNdG-hf5jhCw1fjHWVasi39-q8tIGGs8z_tCIm9G4Db1ituyE2jCENq51cR2YByoyOnsPgpHYKZF7T9AUzwQOqbiQWHj5iGt_GEnZeKlcrLC3Yd77iHYQauJW7-hUuuG9iQEze3n3MKEUy01XACvkI1B_lYZJnYRrkw825jKuFStg8gb6S3tbJlLh4gd2qTOqwocfABIEJgach4lwgFX8g0vqJvU68n9zC5j_thTBj_JECUr21vQvBJkFwMb1rYfi7fvBcabIy04CPflf8xVs84VGJ5fgTegKt1G2mKupRciCgS81D2MidYIKU3B4taFYnDGdX5cCn60q5ytRTChohnG04JOZuN5El9QG3xMda_hb0XspD4xtNY-16TSRwOUrdfHaTn-JybywTTXmhbSsA9-gepqJ3M8YEVdcjf-rU8rqRucaLShvwkrSOeQEqLKHlCQEFtrAKcKqvuRK-f1C48DfigNt8hnHnZiqHyoSwc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ae5f4c459.mp4?token=h_YaeDy_wh1COlaD2p_DwFrhvQKspT3s_wqZ_U-eIfi1R8Yh9C8xLwCQZswZqvJr0cWYWN7Z12a_PIMOhOJTkSpvX_Vg95IpdebNl1IcaGtNTSApjVvZT8n9-OfdXSOylpSPP46_G0kPwD1fplkUEenOAfs7AyAs62NygVlpk1UC2i34E-l1UWNi4cWdFpHabNdG-hf5jhCw1fjHWVasi39-q8tIGGs8z_tCIm9G4Db1ituyE2jCENq51cR2YByoyOnsPgpHYKZF7T9AUzwQOqbiQWHj5iGt_GEnZeKlcrLC3Yd77iHYQauJW7-hUuuG9iQEze3n3MKEUy01XACvkI1B_lYZJnYRrkw825jKuFStg8gb6S3tbJlLh4gd2qTOqwocfABIEJgach4lwgFX8g0vqJvU68n9zC5j_thTBj_JECUr21vQvBJkFwMb1rYfi7fvBcabIy04CPflf8xVs84VGJ5fgTegKt1G2mKupRciCgS81D2MidYIKU3B4taFYnDGdX5cCn60q5ytRTChohnG04JOZuN5El9QG3xMda_hb0XspD4xtNY-16TSRwOUrdfHaTn-JybywTTXmhbSsA9-gepqJ3M8YEVdcjf-rU8rqRucaLShvwkrSOeQEqLKHlCQEFtrAKcKqvuRK-f1C48DfigNt8hnHnZiqHyoSwc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نظم ایرانی، تثبیت قواعد در بیش از ۸۰ روز ایستادگی در آب‌های خلیج فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/akhbarefori/653432" target="_blank">📅 21:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653431">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
رد گمانه‌زنی‌های رسانه‌ای راجع به جزئیات مذاکرات مرتبط با خاتمه جنگ
🔹
سخنگوی وزارت امور خارجه درباره فضاسازی‌های رسانه‌ای راجع به مذاکرات خاتمه جنگ تاکید کرد: هیچ‌یک از گمانه‌زنی‌هایی که در روزهای اخیر راجع به ابعاد مختلف مذاکرات مطرح شده قابل تایید نیست.
🔹
در این مرحله تمرکز مذاکرات بر خاتمه جنگ در همه جبهه‌ها به شمول لبنان است و ادعاهایی که درباره مباحث هسته‌ای، از جمله موضوع مواد غنی شده یا بحث غنی‌سازی، در رسانه‌ها مطرح شده، صرفا گمانه‌زنی رسانه‌ای بوده و فاقد اعتبار است.
🔹
اطلاع رسانی دقیق راجع به جزئیات مذاکرات توسط مقام‌های رسمی صلاحیت‌دار و سخنگوی هیات مذاکره‌کننده صورت می‌گیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/akhbarefori/653431" target="_blank">📅 20:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653430">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
دوران اعتماد به گفت‌وگو با آمریکا به پایان رسیده است
🔹
رئیس کمیسیون امنیت ملی و سیاست خارجی مجلس: ما اکنون برای هر نقشه‌ای آماده‌ایم، هر چند آمریکایی‌ها برای آنچه در انتظارشان است، آماده نیستند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/653430" target="_blank">📅 20:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653429">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
اقدام خصمانه آمریکا علیه حزب الله لبنان
🔹
وزارت خارجه آمریکا در ادامه اقدامات خصمانه خود علیه مقاومت لبنان، تحریم‌های جدیدی را علیه حزب‌الله اعمال کرد که این تحریم‌ها شامل چند نماینده پارلمان لبنان نیز شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/akhbarefori/653429" target="_blank">📅 20:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653428">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84f78c0103.mp4?token=eHfTor_wximiKoDXhmI_BHLSholJA6OoRs2R5IxqOYFvFtlH_SEYCCHdpD6gGo4k1MFNQ0iIAQ2rD10wBvSbv_FMFTAZDTkEiJYEutdQdwZ2WHNrqQf-s8cJ1h4IIh5URFIRCPvtIqM8ZH5cJCbBPqOJf9cM7s9b_3RYvPnoyZrviVuLl3SdYqMPHOo0Ex5udDMst-ww6HmG2HkWS7YsUTlo-tuX_NcARdsFoesPw4kinEZ_bCC1zAdBk7GgK_5osAkL-V-TvzSNE7dZhDGh-sxaTo521nazWdxG9WBrNcsFpND96mXVZKklp8oT_isVCXg6CSmzuQpBPRFPbHhP7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84f78c0103.mp4?token=eHfTor_wximiKoDXhmI_BHLSholJA6OoRs2R5IxqOYFvFtlH_SEYCCHdpD6gGo4k1MFNQ0iIAQ2rD10wBvSbv_FMFTAZDTkEiJYEutdQdwZ2WHNrqQf-s8cJ1h4IIh5URFIRCPvtIqM8ZH5cJCbBPqOJf9cM7s9b_3RYvPnoyZrviVuLl3SdYqMPHOo0Ex5udDMst-ww6HmG2HkWS7YsUTlo-tuX_NcARdsFoesPw4kinEZ_bCC1zAdBk7GgK_5osAkL-V-TvzSNE7dZhDGh-sxaTo521nazWdxG9WBrNcsFpND96mXVZKklp8oT_isVCXg6CSmzuQpBPRFPbHhP7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هوایی مهر از مدرسه شجره طیبه؛ میناب هشتاد و دو روز پس از حمله جنایتکارانه دشمن صهیونی-آمریکایی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/akhbarefori/653428" target="_blank">📅 20:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653427">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccMJVd5g0dcMIAtbW3Cp6Jnd40Nqmi4-uwSYnd2T1Kv9MiSTiWGMPmeOWuvu9doMFeoG88wti3vd9mmk9_QtyCj-k9Xx8IGpxdUNGzjFck3dhOg4pIl3_Y4uC3jUflHu94tU_bYUfjnuS9Tpnx3ieBBVAvncCyo815ow_t-BMCmndGgGzuMdsJYbyDXtJ3eTMXFtd7jmjDST1p1oQZkBQrQ1MqN_cYewwLTRQfhhDAPie1n9jnPGPkZzVHdmq6UyxffzQzPlIpfEF_6iMjcrBIP6zoE_oVe7PUAkS1Z1GPPYKCcjg_eu7NOfeRz20YBj_WXPthWLTGFig14gUai_uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: ایرانی‌ها خواستار عدالت برای شهدایشان هستند
🔹
مردم ایران همانند مسئولان، حملات به مراکز آموزشی را «یک جنگ سیستماتیک علیه بشریت» می‌دانند.
🔹
با حضور در هرمزگان از تداوم سوگواری مردم ایران به خاطر جنایت متجاوزان آمریکایی در مدرسه میناب سخن گفت و تأکید کرد که از مردم ایران «فراخوانی برای پاسخگویی و عدالت» برای کشته‌شدگان شنیده می‌شود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/akhbarefori/653427" target="_blank">📅 20:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653418">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JYwDy5EWyFDTyplNz_1l4yiE1OEoK4UjU-Bp8Lnic4CCGs2RaS1idb8flWX8RXMlLLDTN8L-k7Mx1-GXKA9UJqMXeK3j2Sa2garwpmiRbjkzWDM1zCeh8m6385HIy8WKF2Qvicq7qkug3Ge8iiNONsMPdOq8k9CrhkK42L7bCwh4WvhX7SKTjZL-JntJlnlesoRjTpEuliu4q1EiT-z0anHw1_COMNAcgCezWLABKwBX6vIyESldtVg37CvnDYtNwQJL0zGpBqLFMkPoPpee15XpKh6qA5OWjpsn5tBTrb_QjnB2di-8hEF16lVW-R513SULPs5ZrMRmFFyonlhS0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANvfznzenUOuKrDv2Iss2EJcqCeTjARqbikGOfHWL05QWtTVFfSzJcwkCHDaV_E5ko5srO3_jCrHGVzf8G5cIchdGQtP_DtzAJXkU8xufq6-HZLX-8e51099ZUz6l2nNtJ_Uuc9WKiB8syT9Lkb10pOzSnfmiADCoyuZqISFJYw_8b1zdQ1dJBTwnPu_x8CxsvvBU39i6NqEWP8CdYL5Zp4z8JXyo5FMyXoDmbGSGjKeo53Qx2cMkNrxe5VX3lW5jNYIhukiXRSObfWOowGjYuHTo7YHAgKKwHK_BM4121hnPeqhXarnHpTR5UkdIdoFv_H2kpB4jvdzETdFMMuI4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BhF3RYkzDR4CJjjV6VmHRSzPgNspF1GpsHNZ3BdNQ4HRXaXPsIitqvpqxSj_o5Sv5aLENZ37UDqwqk6-8VOwUcyyZ6EhRe1-RHFERaDVcSQ_GsvfkQQTbrd4dvWJ8LtmlBTADwNQKxv-9ECzrDqMJVfcVeH3tpFP8hysz2l0iWCEbpEgX7htK3V9YTVuAMbMkxoV3m1Db32Kz-s46im4DSU3jUxd8C4iTRl-qeZBj0stL6Lj7ox12l6Iw6Tb1R07LCdGblCv6xCVKIiqEEfJ96RKDxyiM74VFjsWJHSro3p2GK7Glkre1dCkvGfIp8JcI9JLllRnpd5aZUK0Ek2Msw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JfjPfNqzmFgEoG4_Hn5390djkbzrKw-pzC7x37ZsWn5fu3W_qsZh37fMpZbMwTjiZytlTUTnwdzjN8b4i4Onf_8J8x0kgY45i6JohVPVwmuQhABX7sHp2sdasmEAi39sGpJBJrPZjjAEv5wQGuWf2o7h-3EcwmxgJt-RKo09nKXgbpWH5lhFceWRuTWn0OFmusg9MxjeOFnLZqj0tn3UBmCsxbgn7H19xUXU3NxxD8sgZdjc5Rvghhi4ZS4mHYcizDmsGvHIPlMu2JqiLImPP6rsrWftpZipk4mEPXGi4dj8KsNnrW1X_7JihweIyAsA69AMyzUeZP8Pbx26Kt7pSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njEBMt0bx_QWMXd5yAwHtv8r8E7BijmmAvmTNMZ2at4eJJvJaIaUy5dJkzb-KHXHphDbGCEfRxQ0eAcwTZNg4FlqMRTWWsX--UfiW4oeti2SUAJ5_tO09TeiLHB4vUaX-O_SWwVluOje65-bLif4pap4iafgleF13rnhMPXMaFA9RxM3zU0VgtJyg-hYhYJPDMU_UCDxSTF10vx3HMtNiWYLg-vfYEThLYtLVxyLxc25jJnadTtLnLEjC65xuXbruUrF9Ons6C4vv9njokK2Bo7VULKWt_T5rBtjmxk3iEf1QajR9Q86PIut6xX_ZVhzv4oQsHGnfoA9YWsJPskgcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OYyw7ZBWQHY0vyp_6vK3Gl45VINSg-IXTkAJYqo_ObKBP0tdPSoWOEtaG_X1oJ95GnsIvj_oO2zl5VxDxXmcUxbIw7hkxLMRjB9frhTzgoaNQkS8SJgOgYESnP7mTT77ccbvfy_6fWZ2hk0Z5Ju4rC8ja3k8yrmVamrNoNnCZi4GOidtG-vSFKq2hvKashdsBGTkLDUdTK6fB-YNz7Razlxva0IK5_2MIGRrRKtM4AXdgP014WeguXxxeR9yJ3p6-_sZQeb24K-y_XGohtDeItnOpg-JQhCS2fE-A9QthFfTCSpW6iqZakvSjhK1iGDWbbNCMfAsbhqQdjgn4TNpZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APmV8wmlSUEjrhSc6YqNS_fBETFZJSs5Sn1z7qNL_zbb8T5mfw9dAeqE5M7R-xS3ZKrQjuHfQ0kfF6lM0ASCWH9rGf4vYTtLHJzVvo0Ejlgk_LX-sOawnRApAKGPPj65i48XOeBe8DpzyIjoJT_p35hc5V0Mm0k1uhclCJ_TPF70xEOiCCxhv5YUYk66Zo0xgvE755x1KG1QVLD6Sn6ESRaRGmuangqR4MghCSQNr4HOtpJBbdlIZxXNxm2SEE1LGx766AA8S2HvFU7QRvlAmpD4FYwpXiXKT2A2dLtkqoEb9IRP2dixYk6q2m1HIxGpzsRzCKCXauiho7jcTgBCNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3MQvBz3at01cj2Tc3f5OCTaAG7WG29uhex0P6Z4Lvt4BdsAOPJwlKEdLZZR_VUcsYowiaQux-3TZ8JoQNZjiRP18f_ykAFZRG-GOQhCk0p0hmMIK_5CzK_8NNXHO8xxpG4VWadLNVbOuj166rWg2pPDUpHcOU6swqPBRX-BHIRVMJLRQgNBiARLYHmhwNuZ84dCTw4kBcfyjn6NowDWoz3IE3aTP0e9yIDYEs047WTQOdYuhGbij2pWAEkbMN_kuV11oFO0Rk88oji7_qfMc_U0bwEaBV_y68CEk82u4YTBPQC-1Dv1gBOvcxa8HCdveiJPvA2DWjoqYkEScQBFBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت
#همدلی
امروز
💫
امروز هم سهمی از مهربانی در این مسیر جاری شد…
#هیات_قرار
با مشارکت شما مردم نیکوکار، ۳ رأس گوسفند را قربانی و گوشت آن را در راستای حمایت از خانواده‌های ایرانی میان خانواده‌های حائز صلاحیت توزیع می‌کند.
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/akhbarefori/653418" target="_blank">📅 20:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653417">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ایران و عمان در حال بحث دربارهٔ سیستم دائمی عوارض عبور از تنگهٔ هرمز هستند؛
🔹
در این راستا، ایران هزینه‌های سنگینی برای کشتی‌های تجاری پیشنهاد کرده و معافیت‌هایی برای کشورهای متحدی مانند روسیه و چین در نظر گرفته است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/akhbarefori/653417" target="_blank">📅 20:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653416">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emePojtTjKNGJc0bYsjssutVnxMisn3Xb25Gl-910ie134-P627aAWoE8dbuloLQsskCkz66MV1ochanc-iDRtrX9EvGTusQVtsu71h4Oc4dmXCt4DGpzJlviAn4k7bEc1XKWoivgN6jlP6n5_DtDvnCmyvrkDbjsAIvc4d4SQIfHitwb3eSbDPMe7oixiobpTJfYdaubEdA9hMtBL8qAxQvQSUsKGS7MGFFlEte13WYwzuUKatpsNk3988lX287kMd6Ah6KiV4KSFzqZ8Ns5E35I5KhUg6OyO-LviGldtOVm9qHTPDVjIk9y6hwmAfX5NppHFhDSQqLS8yirqc-0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت انگلیسی رئیس کمیسیون امنیت ملی در پاسخ به ترامپ:
🔹
دوران اعتماد به «دیپلماسی» آمریکا به پایان رسیده و اکنون ما برای هر سناریویی آماده‌ایم.
🔹
هرچند آمریکایی‌ها برای آنچه در انتظارشان است، آماده نیستند!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/akhbarefori/653416" target="_blank">📅 20:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653415">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c9573f99a.mp4?token=oy_UkqsLikgyYFD0WZRL-L9NB_Syfsw0oFMKwIRdez7O3Dkmvs7vqmCls7enrhHJdVO-mLRdfcRYzM9BKF7dlONgmdEfXwWfgLxsQdVvhHF16xyJCAHA7AmeBYxcpIXRndMFkE3VE5OYGJU6Gl3EQnNZ6PRgYXinEBPT9HNEihKtvQbrNkZbcXGYlZPsgHC_REkwnCSE6a-riftvjFfgUrE9pWSHqytU_AwQQ0ioPJUMfkzj9fPgtazurb5o5uxy-b9wGagxvjOm3dUrFfwTzKKoVUN4VTS-EH0Y-87BGLjvf4Zznhot9sEWSoV_KBIc096N401lZdmBgY0DurXVtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c9573f99a.mp4?token=oy_UkqsLikgyYFD0WZRL-L9NB_Syfsw0oFMKwIRdez7O3Dkmvs7vqmCls7enrhHJdVO-mLRdfcRYzM9BKF7dlONgmdEfXwWfgLxsQdVvhHF16xyJCAHA7AmeBYxcpIXRndMFkE3VE5OYGJU6Gl3EQnNZ6PRgYXinEBPT9HNEihKtvQbrNkZbcXGYlZPsgHC_REkwnCSE6a-riftvjFfgUrE9pWSHqytU_AwQQ0ioPJUMfkzj9fPgtazurb5o5uxy-b9wGagxvjOm3dUrFfwTzKKoVUN4VTS-EH0Y-87BGLjvf4Zznhot9sEWSoV_KBIc096N401lZdmBgY0DurXVtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: ما کنترل کامل تنگه هرمز را در دست داریم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/akhbarefori/653415" target="_blank">📅 20:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653414">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2975fd5ff8.mp4?token=OHiEvbQcVZS4z5E_wAb5Scfm8aXtJuhi2vTiTap_ZUvXEBkBIIgCF4tLrBzFnF9GMD4x_8Lj3N3y3KPwAgRd_bPSh6GX5scxEM4iIjwCCnc9szp9W9m4uezOYyoxJbZ8j10M7ikCch-FhjBKHx26IUORhRYirk7e22luvr_OJ7gAQgReCJ-lDuRsSwFeS5Oht178ZxIfsPSKJ4ntHhGYFW99VS6oo9vI1cyjyy1kT6sn0h4hZhnFKPONaxMnq2ICcxrWlvQfmRSEidUgK9h5NWDzjDuk1ImzmtQlldMRbApNxh907KtQj5SKh_4byw81x1BPVSmOQDu9Wpmxdfdi_mSquWUb4XjkbleGNoDFJ8r8SAFrGGr7Wq_Zj7ohGeIm-_1Qc4Wn5d-nYhvse7weHtvKUk2QnzFkho5VejUa-yAwfh6jYjq7SoHyTrIv8MT1aiSSjItiRmu1LuZupfyqG-PKbQmUSa20FKWl3WKn_FNrvt_ILIC1nar2NFsMd9HH8kGIlWtwtILKh8xsnQq8d6Ra3QOcBkcxoDlsRd-bsD2nZd0B26gTEawQkufRPa4nbAu_0ekHOXpd_BZT2IpKXvfOnbPuenNEk6LMpqvwJdrvIgCEj2cfpTwwoxGFm3iN-XJh9B3wojFUx9c6F7T5h-WVnE1J-YSIq2qe7Qd3Hbc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2975fd5ff8.mp4?token=OHiEvbQcVZS4z5E_wAb5Scfm8aXtJuhi2vTiTap_ZUvXEBkBIIgCF4tLrBzFnF9GMD4x_8Lj3N3y3KPwAgRd_bPSh6GX5scxEM4iIjwCCnc9szp9W9m4uezOYyoxJbZ8j10M7ikCch-FhjBKHx26IUORhRYirk7e22luvr_OJ7gAQgReCJ-lDuRsSwFeS5Oht178ZxIfsPSKJ4ntHhGYFW99VS6oo9vI1cyjyy1kT6sn0h4hZhnFKPONaxMnq2ICcxrWlvQfmRSEidUgK9h5NWDzjDuk1ImzmtQlldMRbApNxh907KtQj5SKh_4byw81x1BPVSmOQDu9Wpmxdfdi_mSquWUb4XjkbleGNoDFJ8r8SAFrGGr7Wq_Zj7ohGeIm-_1Qc4Wn5d-nYhvse7weHtvKUk2QnzFkho5VejUa-yAwfh6jYjq7SoHyTrIv8MT1aiSSjItiRmu1LuZupfyqG-PKbQmUSa20FKWl3WKn_FNrvt_ILIC1nar2NFsMd9HH8kGIlWtwtILKh8xsnQq8d6Ra3QOcBkcxoDlsRd-bsD2nZd0B26gTEawQkufRPa4nbAu_0ekHOXpd_BZT2IpKXvfOnbPuenNEk6LMpqvwJdrvIgCEj2cfpTwwoxGFm3iN-XJh9B3wojFUx9c6F7T5h-WVnE1J-YSIq2qe7Qd3Hbc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشییع شهیدِ خنثی‌سازی بمب‌های صهیونیستی در بروجن
🔹
شهید حمید خانی، پاسدار بازنشسته و از نیروهای داوطلبی بود که هنگام عملیات خنثی‌سازی بمب‌های عمل‌نکرده دشمن به درجهٔ رفیع شهادت نائل آمد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/akhbarefori/653414" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653413">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
گام بلند برای پایداری انرژی در غرب خراسان رضوی
🔹
با همت وزیر نیرو و استاندار خراسان رضوی، عملیات اجرایی پروژه بزرگ نیروگاه خورشیدی ۲۵۰ مگاواتی سبزوار با سرمایه‌گذاری عظیم ۲۰ هزار میلیارد تومان آغاز شد.
🔹
محمدرضا محسنی‌ثانی، نماینده مردم سبزوار در مجلس، با تبیین حجم عملیاتی این پروژه، آن را محرک اصلی اشتغال‌زایی و ثبات زیرساخت‌های برق در منطقه برشمرد.
🔹
وی ضمن قدردانی از نگاه ویژه دکتر پزشکیان (رئیس‌جمهور) و حمایت‌های دکتر طرزطلب (رئیس ساتبا) و دکتر خدایی (مشاور عالی استاندار)، این طرح را سرفصل جدیدی در توسعه صنعتی غرب استان خراسان دانست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/akhbarefori/653413" target="_blank">📅 19:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653412">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpmWizvfR5EWCAwmMuY_cXzbfiaqH-E4ikpa4x29LBj89M0HV_cRvDpONy7AjBI-MRcZ-CitnfTzg_z_ivYr_GiwZec-xIL12WL07oRmkOJLrXnI68nkg17ZMRAUur4jVg2bVQOIAzHohKwGzdKZgQek-Xd4BIRriyCp86olHOO082dBSTbOvkFyYy4nA_V0GUmlzu2QXk8fvZedbiHFB6-i_nQqnIAOo4seibZaQMOBSbxFp0-7Ciex6P-WPrWAvP1judbTZJAZbmsgmjpyQc4PffKCpQ69a-ZIh7Nn4XoEi2lmLUso7cUzmVeVo9QgIvf8qq2vcEWrNYdyhkLElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علائم عجیب بدن و علت‌ها
🔹
می‌‌دانید خمیازه بیش از حد یا بوی بد غیر عادی دهان به چه علت است؟
🔹
در این اینفوگرافی علت‌های برخی علائم عجیب بدن را خواهید دید.
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/akhbarefori/653412" target="_blank">📅 19:20 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653411">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
روزهای سخت آمریکا برای پذیرش واقعیات جدید تنگه هرمز
🔹
وزیر امور خارجه آمریکا بار دیگر علیه وضعیت جدید تنگه هرمز موضع گرفت.
🔹
روبیو در این باره اظهار داشت: ما همیشه گفته‌ایم که سیستم پرداخت عوارض در تنگه هرمز غیرقابل قبول است.
🔹
اگر آنها به تداوم پیگیری این موضوع ادامه دهند، یک توافق دیپلماتیک غیرممکن خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/akhbarefori/653411" target="_blank">📅 19:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653410">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkStALHbBdv8IQgmJ4f7PtrIT6fj61Ta3FaCu7Ho16nnd_bm5_gX_LPZu21lu0gC6gpS-2DNkzLQ6N1Tzy6KSsHeWkIKHn4GS7s3itUeGhZBe14tRPT19YdKJmFbEMFwSUUT1Qg2CN6cVC0R7dFUjEUNDAusgT8VjpOy0KSVuUCSSnMn5UFf4xn1fmo7C9x3GMO2E4WfVSVul22J09YositvqqKmb2ie0uARyiqcpXMhw3yep73VjVZDAMftVzooAyvL6aq-QAS4XwYQbN1g4613bBpNCBLngFGX8u-0PdY0MsyoKAWBBwHIrA55ljFerfd6CZPxANLt2XBJ1Vvu7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گاردین: ترامپ خود را در احمدی‌نژاد می‎بیند/ آنها خیلی به هم شبیه‌اند
ادعای گاردین:
🔹
با وجود تمام تفاوت‌های ظاهریشان، همیشه به نظر می‌رسید چیزهایی وجود دارد که محمود احمدی‌نژاد و دونالد ترامپ شبیه به هم باشند.
🔹
جذابیت متقابل بین ترامپ و احمدی‌نژاد چندان دور از ذهن نیست. این دو نفر سبک ارتباطی پوپولیستی و جذابی دارند؛ شباهت‌هایی در سبک حکومت استبدادی آنها نیز مشاهده شده است.
🔹
بدبینان ممکن است ادعا کنند که این دو علاقه مشترکی به لغو نتایج انتخابات دموکراتیک دارند. پیروزی بسیار جنجالی احمدی‌نژاد در انتخابات ۲۰۰۹ را با تلاش‌های ترامپ برای لغو پیروزی جو بایدن در سال ۲۰۲۰ مقایسه کنید!/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/akhbarefori/653410" target="_blank">📅 19:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653409">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
موافقت وزارت نفت با حذف تدریجی کارت‌های آزاد سوخت در جایگاه‌های سیستان و بلوچستان
🔹
نماینده زابل: از خرداد ماه امسال، سهمیه سوخت با نرخ پنج هزار تومانی به کارت تمام خودروهای شخصی استان واریز خواهد شد.
🔹
کارت‌های آزاد سوخت در تمام جایگاه‌های سیستان و بلوچستان جمع‌آوری می‌شود و سهمیه کل استان با مساعدت ویژه و مقداری افزایش، به کارت تمام خودروهای شخصی واریز خواهد شد.
🔹
این سهمیه جدید با نرخ پنج هزار تومان (نرخ سوم) محاسبه می‌شود. همچنین مقرر شده در هر شهرستان یک یا ۲ جایگاه سوخت برای استفاده مسافران و مهمانان سایر استان‌ها حفظ شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/akhbarefori/653409" target="_blank">📅 18:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653408">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxYD3sU0z-hqZXH3J5aoklxNhtlTQF-S1mXk-7naHww7d367t3cKtlHQc09EX4y5t4-EV6Vg_yXltbQH4NA31ppKU4kRGxUAd5JCYA-x1hqTkk9kCzctPcMVmpX5ksuQeGYJiJu2mGqIeuSgCHPI31J8uTmh2t1omO8HMdt-xBiTC9dZXRaDpjEXOFlJHKk_wj9WyygESXPIMIWAOHUurVkVCHgEXAC4z_i6f88BmVsg39IwN5qQrnt7grolWQ7OPVT24wUhHomvRizFQgFpxI-n4G4Mw8Ogf0OOxC4yHW4CYh7IkC4O75-WSzTDDO1YiHMzo13nc2Fc8nHUvN1P2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پای لانچریم
🔹
رفت وآمدهای دیپلماتیک پاکستان به تهران و بازتاب گسترده آن در رسانه‌های غربی، گمانه‌زنی‌ها درباره احتمال یک توافق قریب‌الوقوع را تقویت کرده است. اما تجربه تلخ گذشته هشداردهنده است؛ هر بار در آستانه توافق با آمریکا قرار گرفتیم، جنگی ناگهانی رخ داده است. جنگ ۱۲ روزه و درگیری اخیر، مصداق کامل این الگوی تکراری هستند. از همین رو، با وجود آمادگی کامل برای هر تصمیمی، یک اصل غیرقابل تغییر در دستور کار قرار دارد. ما برای هر سناریویی آماده‌ایم؛ چه توافق، چه رویارویی. اما این بار، اسیر نیرنگ دشمن نخواهیم شد.
🔹
هفتصدوپنجاه‌وششمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/akhbarefori/653408" target="_blank">📅 18:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653407">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j05sZJOWvAZ6947VJeUm-0joQLJniyKJzQz1j9MZe2pwKQZCaoChx2qGVC5E6nPHEz4bUHWtM_LWYLfTKHYFcNYdjdBHwOwoD7p5OKA3s-CQN0nrXmIHkimTFohseKrzpjbW3f3xKT6U9FbYIIrDz1l0ovMlqZi8U0tByNoFwnfa_kG5KJnmq0vHzq7YH6qgHpsTRXl0KD5VtBDxo9LKaq-2-uV7c-ouR5CvNLpDDZd_Z0R4gbRO-m-H95MzT3NX0_uTRed1O4WgHnVvpPVqeysHJYh3eTy-uhgtBIW0_w-g2P-8HWC0DdTNBl55EDLMr7STSIwv0MC1Pu0dol6dZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/akhbarefori/653407" target="_blank">📅 18:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653406">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3516a0697.mp4?token=h6yF35qS6zNZ3I9yljwAR-rthc775BJszYVnNl96jc36g0sWTIDVyVnLAuwvi7yNtm3ey0bTZ7jUkTuaB1d-J6KV2G0R7wIzYCy7upik1F9DGeXoxpC9E0pDxN7gm9xOhzhqseOm2RapHSNoTIsZbKAc9UN64nMDDkUPMXR87MSYNpxBJmeRKq-z58NZnEQTgcZexZlFsy_1kdkN7If_nOp8nul0GQkNLvpxtuQB75ZEvgiydRtT30tSo7VPBta2YgDXR2Epe7cHnev3S1fFauI-a9NP3k3jdSIsQyw1Qnke5lCytqpIvzDqsD2GXTCVj3b6ilw8tb-P0uHoI0_yVTtHzG3JzfRhavJUvJKq4c4ioqdTi2dfNb2a4c7fwrwg3C2W4xIrz_69hLq7tUcFCDp9RnXBYHpoxJQ2PfNW0ASjbX7P9KW2eu_5fQCL7lothO8fjGPYyvIoc73zXKCvLD_-LHLZciFEdqsF9LV0GqRE3t2A5D-HPXIfyDt9z8-wvHzna-xrJEv2DCSNxMz6PJFJwNWEKbfBLpPRlSDHeYwd5DrrDd3y0mTZiptnP8nmlz4dkuhHRPjpWixYLoeLprvZApE-q4ITSGc5mTaz4QXd3epW991znEdKSbCOaO2WZt7gLOMNQ8NmvE1W_6e8l5z_aHUC1EnE_xnsBiLeg8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3516a0697.mp4?token=h6yF35qS6zNZ3I9yljwAR-rthc775BJszYVnNl96jc36g0sWTIDVyVnLAuwvi7yNtm3ey0bTZ7jUkTuaB1d-J6KV2G0R7wIzYCy7upik1F9DGeXoxpC9E0pDxN7gm9xOhzhqseOm2RapHSNoTIsZbKAc9UN64nMDDkUPMXR87MSYNpxBJmeRKq-z58NZnEQTgcZexZlFsy_1kdkN7If_nOp8nul0GQkNLvpxtuQB75ZEvgiydRtT30tSo7VPBta2YgDXR2Epe7cHnev3S1fFauI-a9NP3k3jdSIsQyw1Qnke5lCytqpIvzDqsD2GXTCVj3b6ilw8tb-P0uHoI0_yVTtHzG3JzfRhavJUvJKq4c4ioqdTi2dfNb2a4c7fwrwg3C2W4xIrz_69hLq7tUcFCDp9RnXBYHpoxJQ2PfNW0ASjbX7P9KW2eu_5fQCL7lothO8fjGPYyvIoc73zXKCvLD_-LHLZciFEdqsF9LV0GqRE3t2A5D-HPXIfyDt9z8-wvHzna-xrJEv2DCSNxMz6PJFJwNWEKbfBLpPRlSDHeYwd5DrrDd3y0mTZiptnP8nmlz4dkuhHRPjpWixYLoeLprvZApE-q4ITSGc5mTaz4QXd3epW991znEdKSbCOaO2WZt7gLOMNQ8NmvE1W_6e8l5z_aHUC1EnE_xnsBiLeg8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روسیه فیلمی از رزمایش هسته‌ای نیروهای این کشور منتشر کرد
🔹
ولادیمیر پوتین، رئیس‌جمهور روسیه بر لزوم افزایش سطح آمادگی نیروهای هسته‌ای راهبردی و تاکتیکی این کشور تأکید کرد و گفت که توسعه همه مؤلفه‌های آنها ادامه خواهد یافت.
🔹
پوتین گفت: «مهم است که به افزایش سطح آمادگی نیروهای هسته‌ای راهبردی و تاکتیکی ادامه دهیم و همه مؤلفه‌های آنها را توسعه بخشیم.»
🔹
رئیس‌جمهور روسیه در عین حال تأکید کرد که مسکو قصد ندارد وارد یک رقابت تسلیحاتی جدید شود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/akhbarefori/653406" target="_blank">📅 18:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653405">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAFy_JhGo0EcVnpnO0iITathdPerNaQnCylJsnFy7zboVeNr5K50kC4R9A8xTiXmIguSIr0hw98hEFuZ5VK6EwNXtsMbm7_ZKZf_eiZj3dlLgeTq7qdTz2_YCnnKuAgP_3crdsr70nPeOGDLDE2vCKjCL9iku9kN4REuAadZ86cWv_2K5QfhK0jyAQ_LtWxuoeFLUicYR4dOcZ24ttkLb3EKgh-k2-wsJ8IC6tsDJ9h-iThrMZqbcLIjgpLVFCOKeQx8JxF71-tuwqD_t4gGpPlAaxYHZ1Dag5WoHxJ5AQc0YqAfhHkTtkJf-cnaHjuV0B47HZOIksX7FMGWY6_-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلاستیک؛ مهمان ناخوانده خانه‌های ما
🔹
پلاستیک سال‌هاست بی‌دعوت وارد زندگی ما شده است. وقت آن رسیده با انتخاب‌های آگاهانه، این مهمان ناخوانده را از خانه‌های خود بدرقه کنیم.
شما هم به کمپین
#نه_به_پلاستیک
بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic
#نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/akhbarefori/653405" target="_blank">📅 18:20 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653404">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWKCZJqzgw6bZVQE0_nIvCRHjnqc1z5r-Mhhrnie66lycREfeyIgUr7j5txB7iFZdKljbL8d6NJsonpWoNBWD0Fhi-CQCnI4ElcfKTJzclAk8oSMmVgk8QsSkjj81SDq69imr5wd54TCGqYlHJCsEk33KHYh-8jxtRSEb2yjphbvvxdi0sVBphQgTc3TYdQtNAT_A_FL7k7xG-lxsyK5s5bRL7qTB9gJ3FQ70gMhzAwlg5EwI9D6UCBWnpKAMGlYz4FihMnt3E2e8IhDgkUoWBZLxvgByLl_kxC5HulGnXLqfgvTY8LID2JrjCS2UB0J8NLQ7XEGbvIU47zZPZ828Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قطعنامه ضدایرانی پارلمان اروپا همزمان با سکوت در برابر جنایات آمریکا
🔹
پارلمان اروپا با تکرار ادعاهای حقوق بشری خود درباره ایران خواستار تحریم‌های بیشتر علیه مقامات ایرانی شد.
🔹
این نهاد اروپایی بدون ارائه هیچ سند و مدرکی از کشورهای عضو خواست که مأموریت‌های دیپلماتیک ایران که با «سرکوب فرامرزی» ادعایی مرتبط هستند را تعطیل کرده و تمام تحریم‌ها را به اجرا بگذارند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/akhbarefori/653404" target="_blank">📅 18:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653403">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
رفتارهای غیرانسانی مقامات رژیم صهیونیستی با اعضای کاروان صمود، صدای کارشناس صهیونیست بی‌بی‌سی را هم درآورد!
🔹
مئیر جاودانفر، تحلیلگر صهیونیست: انتقادات نتانیاهو از رفتارهای بن‌گویر، کاملا سوری و ویترینی است؛ این‌دو در انجام این رفتارها شریک و همکار هستند.
🔹
بن‌گویر قبل از ورود به کابینه نتانیاهو، ۵۶ بار کیفرخواست داشته و ۸ بار هم متهم شده بود.
🔹
این‌ افراد مدام به فکر جنگ هستند؛ چراکه آنها فقط بر أساس جنگ و خون‌ریزی می‌توانند بقاء داشته باشند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/akhbarefori/653403" target="_blank">📅 17:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653402">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aP_H2vv337ip1RZfG557c1WbukEq4IbN70HDkSeQO3R0pToEusC7218aF4Uoot07idpoUR8gCb_arZoBrB9gJfxBzybIXmSa3D0cfqNukrV8Akx_9E4OThG-vFb69b2wzwJzZut3JhcsRMfcSk13QkuBck-vG_s9sx1rFuO6DanlE-ZG-sS8PedSDob_5FdFMOnagvu0_iiB8ME5NGN-XoY4ntLDuSfWUXAMOROoHVsO_D3x7x6ElCoX5qWadHRy2MMlf60QU7M410pWAsW0wsNEDSlRn89MEHJinbHyttjeB1zmzvNG3MFNuoZncbtrf9UPxbszGJbjk3rwx4mj3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غول نفتی امارات: تا نیمه اول سال ۲۰۲۷ جریان کامل نفت هرمز برقرار نخواهد شد
🔹
رئیس شرکت نفت دولتی امارات متحده عربی ادنوک نوشت: حتی اگر جنگ علیه ایران همین حالا پایان یابد، جریان کامل نفت از طریق تنگه هرمز تا قبل از سه ماهه اول یا دوم سال ۲۰۲۷ به حالت عادی باز نخواهد گشت.
🔹
این چشم‌انداز از جمله بدبینانه‌ترین پیش‌بینی‌های مدیران ارشد صنعت است و تاثیر اقتصادی طولانی‌مدت جنگ علیه ایران را برجسته می‌کند؛ جنگی که به گفته آژانس بین‌المللی انرژی، به دلیل مدیریت تردد در تنگه هرمز، بزرگترین بحران انرژی تاریخ را رقم زده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/akhbarefori/653402" target="_blank">📅 17:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653401">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/630c1a7be9.mp4?token=SWSplZpuZSo7Q3sLdOcn4NQMMqAoVr2PO0eSp6uuaKvmjvYRUnwEqqD7bON0NXE9GT8PKeowzV_tnlBpxWEMp5AfVbgNa0g8dwdavQJGXtu72s4YalqLI18ACjrJvs17Mo_IXQNE5aHTVWuiX6RqPahrpgipXvhePYqJDBpnmdTtJmXAM0n_BN9Ohuj0-_xzh791jDL2gjLIhRDyyvvubvlC7iM4wr4Gc0fSo4gGrb1CXGGYrFBhYw2VHwV3RQ9mZzyTdG5aB4alR4Eu-CxPflsiDWTBeTVaZLApJ5eONvit5_6RL3oXbeCLjYbtmcSFNl05OW3xdbpwIrlVsUNwYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/630c1a7be9.mp4?token=SWSplZpuZSo7Q3sLdOcn4NQMMqAoVr2PO0eSp6uuaKvmjvYRUnwEqqD7bON0NXE9GT8PKeowzV_tnlBpxWEMp5AfVbgNa0g8dwdavQJGXtu72s4YalqLI18ACjrJvs17Mo_IXQNE5aHTVWuiX6RqPahrpgipXvhePYqJDBpnmdTtJmXAM0n_BN9Ohuj0-_xzh791jDL2gjLIhRDyyvvubvlC7iM4wr4Gc0fSo4gGrb1CXGGYrFBhYw2VHwV3RQ9mZzyTdG5aB4alR4Eu-CxPflsiDWTBeTVaZLApJ5eONvit5_6RL3oXbeCLjYbtmcSFNl05OW3xdbpwIrlVsUNwYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشای وضعیت سربازان آمریکایی پس از حمله مرگبار ایران به پایگاه آمریکایی: نه پناهگاه داشتیم، نه آمبولانس؛ فقط رها شده بودیم!
🔹
افسران آمریکایی در گزارش جنجالی شبکه «سی‌بی‌اس» آمریکا: انتظار داشتم ببینم صف آمبولانس‌ها به سمت ما می‌آید یا چیزی شبیه به آن، اما خبری نبود. حس کردیم که تنها مانده‌ایم. بی‌توجهی بسیار زیادی به ما شد که این غم‌انگیز و دلسردکننده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/akhbarefori/653401" target="_blank">📅 17:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653400">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0LHIb-y--UkZ8BvCgrMqKAa3atL5BbfMskFTYWbabtp_EDBU9jwldRp9y9Wa4E2RBgOAc2_sfseh68JMG-O6a_Q6mhYfblGDTTbWx8S6qJya7HeaEF5qmypbLiNbwwqXcqOV1fR96Z8wu3ZvKWiqh0iouwrJ0pSLM7a807Rq3Htu93x1rQ7i2o-XXOsCH5jVv5IH5_DNXNgH1DI28UArJXQ0mP3YCYIcmbxbpERMvc2DQsX5nUF6EUdV08Z6CdlTQk7WDW8WUtrfkttcSxkQIVj-dReGDRP42Yslu2Vt8xEPFVPUU7fjsDo4ZwzoFEmxRq6I-WJ0GWdlbjE9EF1dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شگفت‌انگیزترین عینک هوشمند رونمایی شد؛ دیگر نیازی به یادگرفتن زبان نیست!
🔹
گوگل با همکاری سامسونگ، تازه‌ترین شگفت‌انگیز عینک‌های هوشمند را رونمایی کرد. این عینک‌ها بدون نمایشگرند و تنها با دستورات صوتی کنترل می‌شوند و رقیب مستقیم عینک‌های «متا» هستند.
🔹
با این عینک‌ها کاربر فقط با نگاه کردن به یک شیء یا مکان، می‌تواند مسیر رسیدن به مکان مدنظرش را متوجه شود،  تماس‌ها را جواب دهد، پیام‌های متنی ارسال کند و جواب‌ها را از طریق جمنای به صورت صوتی دریافت کند
🔹
اما غافلگیری بزرگ، ترجمه همزمان صدا است. این عینک می‌تواند در یک مکالمه زنده، صحبت‌های طرف مقابل را فوری به زبان شما ترجمه کند. حتی متن‌ها (مانند تابلوهای خیابان) را نیز برایتان می‌خواند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/akhbarefori/653400" target="_blank">📅 17:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653399">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64d9f1e65f.mp4?token=MJK1AwQmsStzaExEacXryRUzjBNXKXveCc6p-uU_yv2j2o3rDH4wri7j8M-PMNilHtmiJUxtdDHvJW1TJMXfHZPTHS15CkWFn5z0hRw0rbDPCBAegjuiaWTWqdxfOytDqItUTbkZ7l5HQXRHHwYcqCwpop4mGMIhDMiG2HE0DjP3-PuXoZfg0vGXudVx2PlWgxGG4WY1sK6GCORsxpcfkgFkG_v8zzBahi-CQvp6JCB4CqxLZpMxxKSDdNsBQfaJ1UOYHgRPVYNam66wgCGZ12lBzZzT84C1QVQGWhRHKZNNZpr9ihv2kFaSKQSBO-JMro-fCi-5Rv0_VwWQZGmmkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64d9f1e65f.mp4?token=MJK1AwQmsStzaExEacXryRUzjBNXKXveCc6p-uU_yv2j2o3rDH4wri7j8M-PMNilHtmiJUxtdDHvJW1TJMXfHZPTHS15CkWFn5z0hRw0rbDPCBAegjuiaWTWqdxfOytDqItUTbkZ7l5HQXRHHwYcqCwpop4mGMIhDMiG2HE0DjP3-PuXoZfg0vGXudVx2PlWgxGG4WY1sK6GCORsxpcfkgFkG_v8zzBahi-CQvp6JCB4CqxLZpMxxKSDdNsBQfaJ1UOYHgRPVYNam66wgCGZ12lBzZzT84C1QVQGWhRHKZNNZpr9ihv2kFaSKQSBO-JMro-fCi-5Rv0_VwWQZGmmkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیگیری اتاق اصناف برای توسعه اینترنت پرو
🔹
فرشید شمشیری، عضو هیئت‌رئیسه کمیسیون تخصصی تلفن همراه و لوازم جانبی اتاق اصناف ایران، می‌گوید محدودیت اینترنت بین‌الملل، خدمات پس از فروش و تعمیرات نرم‌افزاری موبایل را با چالش جدی روبه‌رو کرده است.
🔹
به گفته او، بسیاری از تعمیرات تخصصی به دانلود فایل‌ها و آپدیت‌های حجیم نیاز دارد؛ فایل‌هایی که گاهی حجم آن‌ها به ۲۰ گیگابایت می‌رسد و بدون اینترنت پرسرعت، روند خدمات مختل می‌شود.
🔹
شمشیری با اشاره به اینترنت پرو تأکید می‌کند حجم و سطح دسترسی فعلی پاسخ کامل نیاز صنف موبایل نیست و اتاق اصناف همچنان پیگیر بهبود شرایط برای فعالان این حوزه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/akhbarefori/653399" target="_blank">📅 17:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653398">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ur1FWWifK7S5njGd_K1ybPOFmNktWxRKlAmuaDvbwcnr9pYp0dSZfO_RvfUPFSvKT0Dd2ktyxJvZAPoy6ITWO2MqM0hFr0dh2-2aV6Jrk61rJ9j5P8CHi-9GPnyECIU3tdqq47B5cvqVSgfuwm2l0Vr1wNmmflWX8bTtsl4gbGRv8PXwOuTf4Yu8wlliQn_I7RpaMoWHklzRh6rEoc1Y-aUyAytWhRepz-LmwX512cjK30cRMiCaQCJa41K1shwGKfFZ9oiHIHw0QnbpW9pb9tmc3WACu1aL8EIQkM81ShA0j11DWz_OOE6UQupqjkcWIQoJ5A5OC3CIE7nY5fhEag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت وال استریت ژورنال از «شیخ‌نشین کوچک نفتی که بر اثر جنگ ایران منزوی شده است»
🔹
کویت پس از حمله عراق در سال ۱۹۹۰ هرگز به طور کامل احیا نشد و اکنون بار دیگر در بحران فرو رفته است.
🔹
با بسته شدن تنگه هرمز و آسیب‌های ناشی از حملات پهپادی ایران، صادرات روزانه ۲ میلیون بشکه نفتی کویت متوقف شده است. این امر جهان را از حدود ۲ درصد از نیاز هر روزِ خود محروم و منبع اصلی درآمد کویت را هم قطع کرده است.
🔹
تقریباً تمام مایحتاج غذایی و آشامیدنی جمعیت ۵ میلیونی کویت اکنون باید از طریق مسیرهای زمینی عربستان سعودی با کامیون وارد شود که هزینه آن ۶ برابر بیشتر از حمل و نقل دریایی است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/akhbarefori/653398" target="_blank">📅 17:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653397">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کارانه پرستاران ۶ تا ۷ ماه معوقه دارد!
احمد نجاتیان، رییس سازمان نظام پرستاری کشور در
#گفتگو
با خبرفوری:
🔹
برای کارمند اداری بعد از ساعت یک عملا دورکاری وجود ندارد و این کلاه قانونی است که آقایان می‌گذارند چون نمی‌توانند بگویند ساعت کار را کم کرده‌ایم.
🔹
از آن طرف برای برخی از نیروهایی که مجبور هستند به طور شبانه روزی کار کنند، هیچ امتیازی دیده نشده است؛ دولت باید برای این موضوع فکری کند.
🔹
درحال حاضر کارانه پرستاران بین ۶ تا ۷ ماه معوقه دارد. یک پرستار متوسط در ماه ۵۰ ساعت و بیش از یک کارمند عادی کار می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/akhbarefori/653397" target="_blank">📅 16:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653396">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
نظرسنجی تکان‌دهنده در آمریکا: جنگ، ما را ناامن‌تر کرد و ایران را به بمب نزدیک‌تر!
🔹
تازه‌ترین نظرسنجی مؤسسه امور جهانی (انتهای آوریل) تصویر شگفت‌انگیزی از افکار عمومی آمریکا پس از جنگ‌های اخیر ترسیم کرده است.
🔹
بر اساس این نظرسنجی، نزدیک به نیمی از آمریکایی‌ها (۴۹ درصد) معتقدند جنگ‌های اخیر نه تنها امنیت امریکا را افزایش نداده، بلکه کشور را ناامن‌تر نیز کرده است.
🔹
در سایه این ناامنی، اکثریت (۴۳ درصد) نگران‌ترین سناریو را باور دارند؛ احتمال دستیابی ایران به سلاح هسته‌ای اکنون بیشتر از قبل شروع جنگ است. ۵۸ درصد از پاسخ‌دهندگان از نحوه مدیریت جنگ توسط دونالد ترامپ ابراز نارضایتی کرده‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/akhbarefori/653396" target="_blank">📅 16:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653395">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
وزارت خارجه رژیم صهیونیستی خبر داد: کلیه فعالان ناوگان جهانی صمود از اراضی اشغالی فلسطین اخراج شدند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/akhbarefori/653395" target="_blank">📅 16:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653394">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pp1sTqR8rd06cWrqP1Ykmr7zshQs3yRRhWDKdbuWAoU02XhUSAscjHEyOdqm7ba8tvS86Cg5lpKBqxIcHBqf7PNoaGUang2Pz9IYyujXZzFMO-DLeMLKwiFhXIHYXM7WQm1WtOFnFqrF-T-6Q-_WGoFbkzirMwNJylruyuYs6EuSSOSfUCM2fYHdOrCVTeiOAGtMmJjefAUV-KC45Hz-VtSTShD_iTPkwrAnKCJihG-gVN62XPS19cGMu9I1I-IDTfvyAk_ZkaaKImN5Jf_a8EVDJ3YQRO6tOMIfQH3fYoii9m-hcngfyHnT1OU973S5zxWLLqCyWOqC4ep0wRt58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری برای روز اهدای عضو؛ «نبض ماندگار»
🔹
همراهان عزیز خبرفوری، برای شرکت در این فراخوان کافی‌ست به پویش «نبض ماندگار» بپیوندید و با ثبت کارت اهدای عضو، سهمی در ادامه زندگی دیگران داشته باشید.
🔹
برای شرکت در این پویش:
عدد ۱۲۰ را به سرشماره ۳۴۳۲ ارسال کنید
یا به لینک زیر مراجعه کنید:
https://ehdacenter.ir/api/gateway?code=120
🔹
پس از ثبت‌نام و دریافت کارت اهدای عضو، تصویر کارت خود را برای ما ارسال کنید تا در این حرکت انسانی و ماندگار کنار هم باشیم
👇
#نبض_ماندگار
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/akhbarefori/653394" target="_blank">📅 16:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653389">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OERmXVOMVD4JZzPei-4BxKhA3quQRuXakH7VWZ0D_r6piIv-TfGfNIt_RBLueMYq1gx3lNsFLesTVBhZ_2m8OejqIEjEWeDGuMAPLrOCLr7nH_3kl9x2iwC_FQETx7z_W3witwAWfnLieqW0oEdNUeQD3k1v976WKcCsbROoHkRJrmY4XYW5E9mVy9x4QDtG9nGbrC4uRt80_Ps2pHKN-GIw9t0Lpvplw8cXZ1ofUjm2N0DVeB2Cs3TNeFnVR-uHO51JJ4LIz44O4JrQMcV8F3CDM0mH04HXhw8FMKkoU0jrz6Oh-92fokC9-y-tAw3pzvfYicZ2B5XLJ_2D76eRbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGhUYp3mSfKlEqsOdXXq-MovUEL1L9kNgZIjOQ4tt59hdNkddtOxa1QP9WL-mtqMqJloO32eLmo7Sw9Q14Ly396uQNCKbRZvH5SJ1JTZ2dYEBdR7YB1ujuBRtbJt8_uCyGHsPlgy3GR2V1y99TxCsMEQyunn8E9xYqf80MaVEiLgvJ2WaGwie2V8QRuEO9vE5g9RvCc0bIHGIWqqZG4r1ZDbbKlVBlIcmEbA5cQ_2f3Yx-BYfIXf-KxPseFlxdLYPpU1mo16v2dYybTDR5umISOIrtJfC_H0fXQU865pkfr5CidreC3VgczlSTjXLwffngUta2RTGfKDUVJ2r1NpFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G1zmxA2jHmDmGqtjPM5AttQVUnCINUTJGPXMrTC799xUdoYvXEXhxA0AXeQwgs-3SG9XpRYPWxQQjY1NyDXZwostz8ctIYTEgBj8wbYC9QAQl8ACFkYcB1g2v60gJX2MvL6LDryKRS_GtmFjGGxIwlMNipwODD0SfVIJN9TS26aeL5ihJhgzam_l4vSqWsd5eG5pLwjVSROOX4lxbUUNvQXJsLrlKH1T1_TDdJNRYYdCFi-pLc1UpryQfTKNTjYFfaJbg3VhT9Qc1br_KKCNRvkOZDoAOqojM2iEdGzZyk2hVwgG8DTiAWemd0u8Z_2RuZ3od9fIEe_QMrkDJ-_mOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n6oWlqoRVj_zYtqCv1mRrGq350kmrZx7yQEwA10MtaVoUi4dCoZkzayc_lWVjFW47ezhUQSJoSqirpWOHrrG25UZVjhzTgE3z90GAHh1Y2c0h4aCtDRjXu6XCL2fi-Ya2OxDtP0AbKmS5tuAR71xGuAc6iEdfpAsgTqeVoHZjYn0YnKQNCADwGkJbMRoSMb4XESafgymsmXAOCgyKZlD7T339EWTXGnh9F_JMsTlnlpvIct9eF-B8PLpB2LSYkpQq2ztXvx1q357aGMw-CyYeJtKtyfb0arZS5l90W3hyBwwr2ihA5Vzy3YXW8IosbEU5UTCeDxqUXa5ymoBsDeSFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/URvJPe1xaNf1yRcqbXaFpDMAY_YFouGa-BIcIkTPAnfb3CEpsRU83I61QyMA6n_Fs7_wnptNepU3ornRjxd_-fCMaoO-qE6-_czNpCFFsgqq3nNv_5_S58OOCuWXNYXfpawta8rM_3HtY86KrgeL5cGB8oelN9P6W9XkoZ2SnkMKYssoVrfLJ3KWjTfHZBERmXJABWkXIptLeGFXCevUSwrhyCgYFPQENiQaLoT5RNj_GkLbprUVL1mgKgpR4Wc5hokcHfcNXRBelVTnXdEbi0rDdxeiBdQIH92KmUHFsalt7enPchWfrPG2pNJOy9CZ0Ex6NuwqKAnFOFJqw86yJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دیدار فرمانده کل ارتش با رئیس‌جمهور
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/akhbarefori/653389" target="_blank">📅 16:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653388">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7fee370e6.mp4?token=E19xl6r2c9jnW3krGIWKzW4Hb0Cx8SJVVVRx3hF3W3OBzA-cbU_HkNWUX0KGumdYASTNwYnhNucD_92Rhdeuq7MrbMydsw248nFN9ejJMXUjt28c3hwjYte-RIOjs14kMtcqNbxzu1ToNLG2p6Svp6QtHF4bmf6vJhPLLc0lGrgr636emZHFFOxPtJa6570cJjFvXP9TSQANlJXWJj_aiOW71yHyrm6gUDZp4bNsK2MlCdALq4EVXFfppf9JbF2EBB8imz5pHhWnlsJ09Bbdw3w-LMK0AuELZVz8tATijntkN_9ZRKqZJpkDe0rOENWx10zv_gD3QxVlUAJec34rLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7fee370e6.mp4?token=E19xl6r2c9jnW3krGIWKzW4Hb0Cx8SJVVVRx3hF3W3OBzA-cbU_HkNWUX0KGumdYASTNwYnhNucD_92Rhdeuq7MrbMydsw248nFN9ejJMXUjt28c3hwjYte-RIOjs14kMtcqNbxzu1ToNLG2p6Svp6QtHF4bmf6vJhPLLc0lGrgr636emZHFFOxPtJa6570cJjFvXP9TSQANlJXWJj_aiOW71yHyrm6gUDZp4bNsK2MlCdALq4EVXFfppf9JbF2EBB8imz5pHhWnlsJ09Bbdw3w-LMK0AuELZVz8tATijntkN_9ZRKqZJpkDe0rOENWx10zv_gD3QxVlUAJec34rLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۶۰ درصد زایمان ها در سال گذشته سزارین بوده و تنها ۴۰ درصد طبیعی!
🔹
اما این عدد تنها عدد شگفت‌آور خبری نیست؛ در این بسته خبر رسیده که قرار است به زوج‌ها تسهیلات خرید جهیزیه داده شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/akhbarefori/653388" target="_blank">📅 15:53 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653387">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7Bvd18uO-tfOXp2pMwoyeWsVlb_HgFwtvAULHZL228gIa7xw__DvN_XYKFv2U4oi9RtJl0xUBuT7pSMUOLbI7_YHJU7iS2znRff937TRFDimUXdaneG9WLwKCHEBkFCh-MimS7wAaAgkzG5Ba3wSN6W4ERVpEBIewdZTXqv8fTYeeMaQsIKWFvWHQs-oks3kp9duAry2hbBtR9x0a5Su9X6ymdRiqNvyTjI27mPjrt_nLZk1nyUAgxcBWFiWP2RVRzVW8RCuD4yrStP_Ryd3wbr642Enb5DfkUz9N9Fb1c8N6Wk9M3Jns1XsHX34Bgdsq-X_JVkNy-Ug8XzE2_Nww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: اروپا از تجربه نازیسم عبرت بگیرد و از بی‌عملی مقابل رژیم اسرائیل دست بردارد
🔹
سخنگو وزارت خارجه: تصاویر وزیر تندروی رژیم اسرائیل در بندر اشدود که شخصا فعالان دستبندزده کاروان بشردوستانه «کمک به غزه» را تحقیر می‌کند، عمیقا تکان‌دهنده است.
🔹
این تصاویر، خاطره‌های تلخ تاریخی را زنده می‌کند؛ زمانی که رژیم نازی، متعاقب بهره‌مندی طولانی‌مدت از مصونیت مطلق در برابر جنایاتش، خود را استثنایی، معاف از هرگونه پاسخگویی و فراتر از قانون دید.
🔹
اگر غرب همچنان شکاف بین ارزش‌های ادعای‌اش و رفتارهای عملی‌اش را عمیق‌تر کند، باید منتظر تکرار درس‌های بی‌رحمانه تاریخ باشد
🔹
اعطای مصونیت بی‌پایان و سکوت در قبال قلدری و قانون‌شکنی، هرگز موجب تعدیل این رفتارها نخواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/akhbarefori/653387" target="_blank">📅 15:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653386">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
تقدیر وزیر اقتصاد از عملکرد منطقه آزاد کیش در جنگ رمضان
🔹
در ایام پس از شروع جنگ تحمیلی جاری، با وجود شرایط ویژه جغرافیایی جزیره کیش، محدودیت‌های پروازی و آسیب‌دیدگی بخش‌هایی از بندر تجاری کیش و بندر چارک، سازمان منطقه آزاد کیش با اجرای تمهیدات عملیاتی، فرآیند تأمین و توزیع کالاهای مورد نیاز را مدیریت و روند قانونی خروج خودروها را تسهیل کرد که منجر به آرامش عمومی در کیش شد.
🔹
محمد کبیری، مدیرعامل سازمان منطقه آزاد کیش، در سفر به تهران و در جریان پیگیری موضوعات اقتصادی جزیره با مقامات ارشد وزارت امور اقتصادی و دارایی و دولت، گزارشی از نحوه خدمات‌رسانی، اقدامات انجام‌شده و نیازهای پشتیبانی جزیره ارائه کرد که این گزارش با قدردانی وزیر اقتصاد از عملکرد سازمان منطقه آزاد کیش همراه شد.
🔹
مدنی‌زاده، وزیر اقتصاد ضمن تقدیر از عملکرد منطقه آزاد کیش گفت: تجربه مدیریتی سازمان منطقه آزاد کیش در این دوره نشانه‌ای از ظرفیت اجرایی مناطق آزاد در مواجهه با شرایط پیچیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/akhbarefori/653386" target="_blank">📅 15:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653385">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjhsppqWCx_7RGkrnOQjSK5HL6iONbOeZU-daP4B8rHY2r1xdv5x9P1beOSOzp67iPEsG-Ti2zgd2dcOC9t1t6yHd9ZBiOyGPTs_kEYWY2KnStPKaXV0NDAneRL1zZns7fDtGip-QwaU1g-J-DiGQR8CrcQ0HhYEYz7voroaSbNLxhJWiR8UEcCHgQ8uAkxU9l9RclGFzY5S8Zcg70jY3SFE8KgTAD-o8z-Ud_D877nxIT5EAcheVd0Uj9DfgpcjMv-AqNmnFg4wxhVHKmtYOydmhI0ud_AVtPvPvNPJL8D7fUAyINK-CvKPavWskGxtSqwc162uRiC6eBGaq4HMTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادامه انتقاد ها به خط سفید و vpn فروشی در مجازی؛ یک فعال رسانه ای از فشار بر کسب و کار هایی که برای بقای خود از اینترنت پرو استفاده می‌کنند انتقاد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/akhbarefori/653385" target="_blank">📅 15:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653384">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d438d2ebbe.mp4?token=mWUxUjoL3EAPN6u1xG5MGAxw4mIaDm1mVG1LRDTTTHijhRYoBfMoGoU8F5MWtjSNaWznptJqwU8JYstPJg9iYSwzUYuPR55t_1GIGbdzXOpp3PVTxhUHLDGStJouc9z6wruOr9ToUZfMhc4XEzl9pxaZSRVLPnNAXzOhwpC7Bu7253pp2pQXBr1Y83oKDxNsJAQdN2WjL_pEIG5ZuI8r1BP4fr4Z1XJWhLMPW-bqQHGzlyzJDEke9N7AfSOMYmh65so98xbBgXR8qKAfXELwTIB755qFc9wFWioV4BqDyw76pT1iRAgmz5VpO219OzYuitZSeQ3nh9AF6bDqBCQVig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d438d2ebbe.mp4?token=mWUxUjoL3EAPN6u1xG5MGAxw4mIaDm1mVG1LRDTTTHijhRYoBfMoGoU8F5MWtjSNaWznptJqwU8JYstPJg9iYSwzUYuPR55t_1GIGbdzXOpp3PVTxhUHLDGStJouc9z6wruOr9ToUZfMhc4XEzl9pxaZSRVLPnNAXzOhwpC7Bu7253pp2pQXBr1Y83oKDxNsJAQdN2WjL_pEIG5ZuI8r1BP4fr4Z1XJWhLMPW-bqQHGzlyzJDEke9N7AfSOMYmh65so98xbBgXR8qKAfXELwTIB755qFc9wFWioV4BqDyw76pT1iRAgmz5VpO219OzYuitZSeQ3nh9AF6bDqBCQVig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری برای روز اهدای عضو؛ «نبض ماندگار»
🔹
همراهان عزیز خبرفوری، برای شرکت در این پویش کافی‌ست با ثبت کارت اهدای عضو، قهرمان زندگی خود و دیگران باشید.
🔹
برای شرکت در این پویش:
عدد ۱۲۰ را به ۳۴۳۲ ارسال کنید.
یا از طریق لینک زیر ثبت‌نام کنید:
https://ehdacenter.ir/api/gateway?code=120
🔹
بعد از دریافت کارت، تصویر آن را برای ما بفرستید
👇
#نبض_ماندگار
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/akhbarefori/653384" target="_blank">📅 15:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653383">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irQRqkVQ82ILUd18-EDi_zaXkgK91eRy0nfiGMtEO9sOwq45ovroNWm8Ks1ZJFyRC-90eNUlzsaGvedI3K6kPD9GNGGl-EYQr_DJhgFflOHGF31LSKCAOKnHL1eQoJfr9o-hOd1wW9JaKPyUJxKg0CVRIbRDsmtQX26MiFpcjqibBO_WpkhReCyhjT2suiS9wKGgSroqGVgXkBWf-Jmdamwuyfb5j6n8UH6ytY7F_Boa5WxnRm6dtbItXhaOonKiYv6j38zhRMZSOHCkiH7UnImAb7HN-v7vmdgpTpTH2qV09gJgn37AvtjqgiMheHz3Z1kg_xSgzSYQwQIOqemCdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: ارتش با آمادگی عملیاتی بالا اقتدار دفاعی کشور را به نمایش گذاشت/ دولت با تمام ظرفیت از تقویت نیروهای مسلح حمایت می‌کند
🔹
رئیس‌جمهور، در دیدار با فرمانده کل ارتش جمهوری اسلامی ایران : نیروهای مسلح، به‌ویژه ارتش مؤمن، مردمی و انقلابی، در جریان تحولات و تهدیدات اخیر با آمادگی عملیاتی بالا، اشراف اطلاعاتی، انسجام فرماندهی و توان رزمی مؤثر، اقتدار دفاعی کشور را به نمایش گذاشتند و اجازه ندادند دشمنان به اهداف شوم خود علیه ملت ایران دست یابند.
🔹
دولت با تمام ظرفیت در کنار نیروهای مسلح قرار دارد و از برنامه‌های راهبردی ارتقای توان دفاعی، پشتیبانی لجستیکی، نوسازی تجهیزات، تقویت زیرساخت‌های عملیاتی و افزایش توان بازدارندگی کشور حمایت خواهد کرد.
🔹
امیر سرلشکر حاتمی: ارتش جمهوری اسلامی ایران با بهره‌گیری از تجربیات میدانی، تقویت آمادگی عملیاتی، ارتقای هماهنگی میان نیروها و به‌روزرسانی ظرفیت‌های رزمی و پشتیبانی، آمادگی کامل دارد تا در برابر هرگونه تهدید، تجاوز یا اقدام ماجراجویانه علیه کشور، پاسخی قاطع، پشیمان‌کننده و درخور اقتدار جمهوری اسلامی ایران ارائه کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/akhbarefori/653383" target="_blank">📅 15:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653382">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
رییس جمهور در دیدار با فرمانده کل ارتش: ارتش با آمادگی عملیاتی بالا اقتدار دفاعی کشور را به نمایش گذاشت
🔹
انسجام ملی و اقتدار نیروهای مسلح مهم‌ترین پشتوانه امنیت کشور است.
🔹
دولت با تمام ظرفیت از تقویت نیروهای مسلح حمایت می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/akhbarefori/653382" target="_blank">📅 15:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653381">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07ada4d4a.mp4?token=oP70LR-5eBMe_sXA3CCpVKCyJ5c3_6DOEKIVDivFT1Vm42gZHlL-gu0vH2tA72yfikiboNZyMOvb2w95igJrkHXcE0A0x0f42KMMSbyfYe9saolFJpOfh-YBfMC6kniX23RBRre_gDTlw7NAtR6vYC1lIiy_yk7YhTlPlfjRrqasGCxayIY4cC4JZt12OLYvYe76HWNXVQrKnvifQlQP5xiodR-dbLqW6gmiowbqDcCsWJB1hGF-IzMlxqPisxNfNfUVxJ4oI4V97-mRkAXQMMPSimENUDkR-xzIjZFMxwyL63z7azd4pI52YaKy-yh4-xye30BcLKB50FGNImkFFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07ada4d4a.mp4?token=oP70LR-5eBMe_sXA3CCpVKCyJ5c3_6DOEKIVDivFT1Vm42gZHlL-gu0vH2tA72yfikiboNZyMOvb2w95igJrkHXcE0A0x0f42KMMSbyfYe9saolFJpOfh-YBfMC6kniX23RBRre_gDTlw7NAtR6vYC1lIiy_yk7YhTlPlfjRrqasGCxayIY4cC4JZt12OLYvYe76HWNXVQrKnvifQlQP5xiodR-dbLqW6gmiowbqDcCsWJB1hGF-IzMlxqPisxNfNfUVxJ4oI4V97-mRkAXQMMPSimENUDkR-xzIjZFMxwyL63z7azd4pI52YaKy-yh4-xye30BcLKB50FGNImkFFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مخبر: رئیس‌جمهور و وزرای دولت برای حل مشکلات معیشتی مردم بی‌وقفه تلاش می‌کنند
🔹
مشاور رهبر انقلاب در دیدار تولیدکنندگان و فعالان دام و طیور: همه باید به دولت کمک کنیم تا با اقدامات لازم، گشایش‌های بزرگی انجام پذیرد.
🔹
دشمن آمریکایی‌صهیونیستی امیدش به فشار اقتصادی و تمام شدن تاب‌آوری مردم است و خوب می‌دانیم این بخش جنگ برعهدۀ تولیدکنندگان در سنگر امنیت غذایی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/akhbarefori/653381" target="_blank">📅 15:22 · 31 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
