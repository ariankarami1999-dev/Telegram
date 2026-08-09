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
<img src="https://cdn4.telesco.pe/file/iIZgDxNvE0QYsCsbx9tvvJPpU8TjLLmiPtTHZWVOwkTatOxDce8exvwbEUWYnDi-q-idtG-4i5sDIT2j-zg1zMqEYv0WTvUPD2s354qdK22Rl1whXjBpSkHHirSmOvEuCicjlFTMMYuMbR1ENXK9KlSxN45IApbJelZx18fCPE1zIiwOPnxDKoo5s7IndSVvRUh5kNNfVU46e74ustR9rqBDBGGEq7DrfU4VxyIWjSZH9DE5ukwW8j56zehYYsRMM1Yzr6Ml3sdfi5jK1rHOfw5YTv2X7tJzDCzPjLHqRsowcb8mDTs1kh-YsfeD0b2xZmlfw1HjyyaOheq_8jSd1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 633K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-18 23:24:06</div>
<hr>

<div class="tg-post" id="msg-27426">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1bEIvSesDfcEtp_mEpK8UamGFNnx0MlLn1hCTmBjq3Tak9RXh-5fjjYRmdM5rq4fqprTKAQMAIUKhvVatU3nSBa5QBt4-srpVBNJdxnzvtSqm_prirP1vJK3tizo6lBaXHaoFWc4VORnFxV3LVk4_CeYsuMH8_MdmlgSiCkaP8DgI8-VYqc9xwgx77l_T3kxLB2Y2Lh8l8lTExaPgPrYEuUsN9JDw78RkOOhQzNbZnzInrp3I8xXZwjtBWKvE7iUbli5HWIQeahtRPMl3bijHGZ6g3PorMx4f_g7j001HKQoe4dazt6r5F48GLgiTSdJPykavH679QBvbBATOa-Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/persiana_Soccer/27426" target="_blank">📅 23:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27425">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5Y8nIu-PcqF4LEg_VqMOEOr0ZlenLTrVtMIrtzJt2cJvtSD8F9IbjvsPgpu3oJ9OznZkiNogbPIv0OEzTbWS9JwSuRWTiuN1jsuw4CLldPhcEym7OCUu0nccxjhPG6Sjv7aUXsTriAeQeeIz_GGnjFDtqKtZ-zXVQA4exaSJFkWe5sAm_jVtQGgBBFJRzJm5kKBHUW4edzG3ZWvQAYPHgRtIWzntfyjUdD70Xb59yPpafB_JvyxdU4qSH3ITJXlqHKlxMWaL9jlCgX-DeiyKtN2SnxtDWj39vySI8Wpb-Q4uY2yvqrc-PI9O_Yesv-N0rROhuzQ1Jjl905VC8mR0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا؛ احسان پهلوان هافبک تهاجمی33ساله‌سابق پرسپولیس، ذوب آهن و فولادخوزستان‌مذاکراتی‌باباشگاه فجرسپاسی داشته تا درصورت توافق نهایی شاگرد رسول خطیبی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/27425" target="_blank">📅 23:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27424">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gv-MrJUSYrMc98K4fdkqBolWsnKoOFIe9IYt_TzWwiYLHlBPwT0NrwXm4SSAt0yBnmWPhLyRvHPm1FVDU4wTblEAA1du_ucvHqnNBwp82KxwqWL3pU_vBIdUxPoGZnCUyHkghexaYdnQmjlWkwVRiP2HOn7GMlwRu_kdsOLjZZ0qrAXXROtYFI7M5yCk1mIArO9YXFkbzL22d_YzlPjSfEk1X4AYSawIuc9HfBmLvIsNnX95dQiU1IHbsVhQUSLh234UrYrX_ZSy-buNFLuTP2aK-NJaEsWDyYA9J3XJr-yLZSCvwtPIpqTiBRwp8tGqymOQuRKZeNxRnFzd26e-_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری از موندو: سران دو باشگاه منچستر سیتی و بارسلونا بر سر انتقال رودری به نیوکمپ به توافق رسیده اند و این انتقال بزودی نهایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/persiana_Soccer/27424" target="_blank">📅 22:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27423">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXMtOo113x3b1nE7mxhYpX_saht_RJmRl5Ut_PzhbhGsfKRBO1l2BIdpY0M0MxPbqYT685UF-BYMCIMZDQzM6F_nqqIuLLgjhLAhKR3S66GrgQx25DNec0WzxWIxWPcg3wwClyGv0Rjrj72v5eA_VHDv4sem810AxI21cfMq1uXtUijm7sn7hQtkDTxlcEB981tYqQMnND7YKPyXuHVeyniA-wDmAOGBnqhURHt3nI6A3hbQG1T85xXsaoMoyUDAbPaGwzO53Y2n4uECEK-5Yq39QPeF97VI2zCXzzCsGwsNrDg9MrMV8CDIPdMYw-HpH3Q_2yRNYkrM6aISjkkNvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔵
اسکای اسپورت: باشگاه بارسلونا بزودی 55 میلیون‌یورو به‌باشگاه‌منچسترسیتی پرداخت‌میکنه و انتقال رودری به‌جمع‌شاگردان فلیک رو نهایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/27423" target="_blank">📅 22:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27421">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f508d354c2.mp4?token=i0H00PnIj8QTZF09txuCtnlGWnV4b9ikwd0kZF0eM1A-wnhML53g6wBNhv3OM8xrzDUwBoSxmNgb6I0F4-4mgZh9Cd0jocGXliSUU3fWQKKpcqj20MyF1T_DC37hT1I3Ph06fhXOUah0Hf3MbJbfOpHMFSyS1Lab2CHN-1fVChesNXRW-zZgOaSgJpxl5SUM4aUBX5eg32uCfa4k95gGi-iCP4qvgXEMjy0Trc8Jmhw8rr_dP7ojtH8j2_wdMiposVDox1-GHDITgs63xO1snY0rMlo4a19-7fkgz_9VWcJjxxrWMxU_K8ei2mdUxoC33veef3T4B4qcCuvDDgoG0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f508d354c2.mp4?token=i0H00PnIj8QTZF09txuCtnlGWnV4b9ikwd0kZF0eM1A-wnhML53g6wBNhv3OM8xrzDUwBoSxmNgb6I0F4-4mgZh9Cd0jocGXliSUU3fWQKKpcqj20MyF1T_DC37hT1I3Ph06fhXOUah0Hf3MbJbfOpHMFSyS1Lab2CHN-1fVChesNXRW-zZgOaSgJpxl5SUM4aUBX5eg32uCfa4k95gGi-iCP4qvgXEMjy0Trc8Jmhw8rr_dP7ojtH8j2_wdMiposVDox1-GHDITgs63xO1snY0rMlo4a19-7fkgz_9VWcJjxxrWMxU_K8ei2mdUxoC33veef3T4B4qcCuvDDgoG0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌امشب دربرنامه تلویزیونی خود از کوروش اژدها کش و امیرحسین طاهری دو خرید جدید سرخپوشان رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/27421" target="_blank">📅 22:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27420">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec041c42ba.mp4?token=DeMSXi5E6OKe1547JFO7ugm6JQtjdntGLzZUtwpr67-DPn9_TTV6JvollYeylJom0e_dBog20ovACJg-1ZrEtQLjp31RsLIXdTIrFVsXDtcGglwRHlhvvHKcc1PN3erjzk339QjSNKNsEpbmS9FF3rhgoolZozRmsRc7hyTVy5LSKw-sthdDLISmYEumbN0BI7B7raIDcofTV3DjGEDhgBDB7em3yUGum_mZ9e0bDSzGfvL35vt10qzrb6D5q-rstMqYghDfcVgA2L-EJgjm8giK0I1NAzTnMEuZiMtAKiL6mlqq4ml7YMjB41od_HCZlq6wgqaD8gBIUspYiOK73w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec041c42ba.mp4?token=DeMSXi5E6OKe1547JFO7ugm6JQtjdntGLzZUtwpr67-DPn9_TTV6JvollYeylJom0e_dBog20ovACJg-1ZrEtQLjp31RsLIXdTIrFVsXDtcGglwRHlhvvHKcc1PN3erjzk339QjSNKNsEpbmS9FF3rhgoolZozRmsRc7hyTVy5LSKw-sthdDLISmYEumbN0BI7B7raIDcofTV3DjGEDhgBDB7em3yUGum_mZ9e0bDSzGfvL35vt10qzrb6D5q-rstMqYghDfcVgA2L-EJgjm8giK0I1NAzTnMEuZiMtAKiL6mlqq4ml7YMjB41od_HCZlq6wgqaD8gBIUspYiOK73w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
مرتضی پورعلی گنجی مدافع سابق پرسپولیس هم به این شکل مراسم عروسی‌اش رو برگزار کرد. همسر مرتضی کرمانشاهی و پزشک هست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/27420" target="_blank">📅 21:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27419">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2458f36d9a.mp4?token=XoumrurUggW4GzJ9wkICHlvOTWh_gVPScAeC6gUA6FKvHS4hVmwWTqlGl3EerBHJb9cYT7RduIJlZb38J2Eky7frE4aHa6ScP9D3K6tjmBf6OHIAUQF4qEB2wSY8L4DSgMVI_qUQnq-4F5QqzH0OcxSW4GuHh6JHJIn8fR7wfe5r3Vv5gCwkmg45UPkiESyJufh4tyCztYDAiigZ05ot3H4FgVnlNIAFHsVj9xbRT0pCLe8Q9nUiXtwD7Pn-3RQrF6ODl-pHuVFZ-qRLMm4T3m4tVHCWCEPU8juf1KaJ1iOYtPzmmis7TsaaQVsFoRG1qHubia-SnuXU80TTYagLizzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2458f36d9a.mp4?token=XoumrurUggW4GzJ9wkICHlvOTWh_gVPScAeC6gUA6FKvHS4hVmwWTqlGl3EerBHJb9cYT7RduIJlZb38J2Eky7frE4aHa6ScP9D3K6tjmBf6OHIAUQF4qEB2wSY8L4DSgMVI_qUQnq-4F5QqzH0OcxSW4GuHh6JHJIn8fR7wfe5r3Vv5gCwkmg45UPkiESyJufh4tyCztYDAiigZ05ot3H4FgVnlNIAFHsVj9xbRT0pCLe8Q9nUiXtwD7Pn-3RQrF6ODl-pHuVFZ-qRLMm4T3m4tVHCWCEPU8juf1KaJ1iOYtPzmmis7TsaaQVsFoRG1qHubia-SnuXU80TTYagLizzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
سوپرگل برگ ریزون و فوق العاده تماشایی اللهیار صیادمنش در بازی امشب لخ پوزنان در لیگ لهستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/27419" target="_blank">📅 21:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27418">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDgsUTis2Om4z1BTPKbu7bYZteXoWWfEugMePwaKrc6vLO1JWhk7rHfRWaOQruKK8H0o6EzGJH-To1S-iaPztkrtDUZeISmd0bmSGdcP8ELgqj9mSB_H-pbpf9uimyS8-4b__Gs72hlx0cKMfZQmiKtk2gu9ShOjhZE_xhrJ5IjtNltQCeFMTq6gmaGLJ44SSy-bj36AqCVbNAH4dl63N_2jXW0U1NrLQBEbwDb3Lojk3JZimZnqKYipr6pwn1j3g8PxbFr3EeIb24JAfXtxw1fLYIy91aykyrCkBO-aDNjUxFslrvGXBMlN3oUpzoCCVjachV6Z0dPj--wGduIPwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تیم پرسپولیس درآخرین دیدار دوستانه خود پیش از شروع فصل با یازده گل تیم منتخب کرج رو شکست داد. پوریا شهرآبادی مهاجم جدید سرخ‌ها در این دیدار به تنهایی موفق به ثبت زدن شش گل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/27418" target="_blank">📅 21:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27416">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bOE01qAQOvVwYLkObewLvpBQ5m1AuEV_vLA97oKUcu6yQCHXRT_c3Op00QwDTPeYq5onk7T2RYH3sVvh9UEQMVOYQFclOFc3PEXpxuP4AAVIis712WH1K3r6RLSD9r7t31akIYerypWRcmy9K-XOnAoNhV053m6f8gP7VA-kGGw_lcjVUhE9EFjaZJQ45dDCV6mnJuXHpizR5hN1NcId3jVwHbS8A36drR1t6JUApbihYG1GZc7HcCBp8X67cRVIWosZVBE3yaiPiizjHPVCTJ-qM9zPWZBmcGnPeLRFKen_OrmQCxqbSfPs-CW9oy9J1eYHzgSAxRCFfHduPF32Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ojScIx5sg_IlJsvhDkPEjaBHT_d_G6Acy0ujEF9N3_aaVBuWaJnk7FpQ1ZbPcAX0ZQ2D_My9sQ83V2Rn8csSGjImx60zjg2vaOENcJ7MHTwS3XrNfqVf5vFkESrQZP1QfdFkDVfxFr3QBMfiaBQF--rm1T9UEYHBJlJR0L0u-lC45mJeBSJKjcDZX_Crm5vIL-KNR_TmjALW7kxI3jDfAy6EUIOTGSxhB_hPxh9BctODy0jnjkgqZnsWFrThTRbu5-DqpEnJaGPDpc53TqUplsZvgc1ziNqZO_znTVTbWau7PDLUOJokS5wTMJIMvPythETb0Lrm4qtfmsjh-mGrRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
برترین‌گلزنان ۲۴ فصل‌گذشته لیگ برتر؛
در ۱٠ فصل اخیر، سجادشهباززاده با ۲۰ گل، بهترین آمار گلزنی یک آقای گل را به ثبت رسانده است. اما رکورد تاریخ لیگ برترمون همچنان در اختیار رضا نوروزی از فولاد است؛ ۲۴ گل در یک فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/27416" target="_blank">📅 20:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27415">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srxfIUNdI_rfd1puxFs6sHTPv_zX2KX1_FyC2wzEE43c3_Jj_JuqtKqbcSYNodPiiDKuBYPWH9-5qsttLzUe3npz0zAVhKLA6crQeVYj7HOZ-SA5vCNSPEtmCboLLq6vTBvAxtxOBd-DkmfWccgn01Jj7VHzQfpUVGRg1Dykw8syLiNnN54Xugn9hu9mNokrWTgOuhyzupCGkbgakI-hoXi0VvvJJ3d-Wf9oenoUGSOjSrrVMMVJra-xyH20xzUkE1dY2zAzycFoEy4JguKZDATIPGYc_SlFepWFlR5-vBOzSNdjkS3gXDLWkYfaGeNAT2qR-riAzpyKMsi_lE5gOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ جواد نکونام سرمربی تراکتور خواستارجذب آرش رضاوند هافبک تهاجمی باشگاه سپاهان اصفهان شد. احتمال اینکه با اشتراکال مهاجم تراکتور معاوضه شود وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/27415" target="_blank">📅 20:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27414">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58a8a9a5f5.mp4?token=WkSBLRb-eJHcuHdxbV17Bfanih6fzjIzkXJCvKO3KWQdWYZfE7d0fnlC15piEiyi2C31mMfBWLJvLg6t4rGc8It6QqJRSCStBfgrxdFqzHrG1tkfaVKBNNoVgeElrvLcPQ7afHb29U--kRsEq7y8uiNxH8huSmWbm-kk2NeqXnduObNsmyx2zTB9Ap0afOEcT5z0k8mCY-bd_SIkOCxgWktIDMYdnAUIEZj_9RSu08MIrUHP0xFxUaiA-3HRv1uV3Hlg_eEYTKR0ZFlzz6w9FI-Nz9xGgaqojRytiOtshEawroix4zTuJUAY2p_J_rr_Sfzw6rDFV4N9j06DHkGivg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58a8a9a5f5.mp4?token=WkSBLRb-eJHcuHdxbV17Bfanih6fzjIzkXJCvKO3KWQdWYZfE7d0fnlC15piEiyi2C31mMfBWLJvLg6t4rGc8It6QqJRSCStBfgrxdFqzHrG1tkfaVKBNNoVgeElrvLcPQ7afHb29U--kRsEq7y8uiNxH8huSmWbm-kk2NeqXnduObNsmyx2zTB9Ap0afOEcT5z0k8mCY-bd_SIkOCxgWktIDMYdnAUIEZj_9RSu08MIrUHP0xFxUaiA-3HRv1uV3Hlg_eEYTKR0ZFlzz6w9FI-Nz9xGgaqojRytiOtshEawroix4zTuJUAY2p_J_rr_Sfzw6rDFV4N9j06DHkGivg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
رودریگو دی پائول: یه بار لئومسی دیر به تمرین آرژانتین اومد و من‌بعدش به‌لیونل اسکالونی التماس کردم که مارو بخاطر زود اومدن به تمرین تنبیه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/27414" target="_blank">📅 20:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27413">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f5820aa32.mp4?token=W4PJ6zr19c2quIYOfA2KuZ2bzprPjfnG7cEwCXTPo7n6nmlH8Uspg-7m1dq6S7ak8QFDfpqR9WnCJhtKVUedVo_QO-mWvRbl8OhcEkCGemcLSVypK9ctOEZXEsEdrsvPiwhzPqNK4Y3gTv0YrI1ei1YLfbWz5SUXjQzM5H6lpkVCJVOirRhpsRpWi9T9Ix-2jx5-19FTKMcEhaI3sYPIwyLrnr1hv_V8ppHlKvN49F2-izZXRZK1ysYqKKLU2wBciMkwK65WNu8U7Rd0cPvNA0wWCnEzyC9en0chicXddTlA0Phm8j1RxCyuFFiyQdhD648sx_lEffOeRhx7t8h1C61XCyKBVVto6WwkTHpNRzU-SPwvv27c1q2Q7U56_ZzhDDMo5E0PILrY8KiIMJ65vURKV6ogNVJzqBAiUOIRWiNQO4DeiS2i6hKldoly8MfIgmSpXcoH2mcy1pQSWSkAIYFG5BP2uMY39f1L2w44rL9qwYGpCC4DIaWLu56wXHSpDb79iGkKzrkOcWCya1_PVnisNu6SRrM0yyeaa7QPcFYIltllRCoAnhl4Gq02LtRDL4ig4N64bvxpH5l4hyVtdYETZZ6cjjFoAAVb7k2RzU-ff-bjQ1qlmZ2GYms5XT_vWCHeh9iuTLCKH4KnIeWddQ8XBOv8w5XrDjErh7Sj9Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f5820aa32.mp4?token=W4PJ6zr19c2quIYOfA2KuZ2bzprPjfnG7cEwCXTPo7n6nmlH8Uspg-7m1dq6S7ak8QFDfpqR9WnCJhtKVUedVo_QO-mWvRbl8OhcEkCGemcLSVypK9ctOEZXEsEdrsvPiwhzPqNK4Y3gTv0YrI1ei1YLfbWz5SUXjQzM5H6lpkVCJVOirRhpsRpWi9T9Ix-2jx5-19FTKMcEhaI3sYPIwyLrnr1hv_V8ppHlKvN49F2-izZXRZK1ysYqKKLU2wBciMkwK65WNu8U7Rd0cPvNA0wWCnEzyC9en0chicXddTlA0Phm8j1RxCyuFFiyQdhD648sx_lEffOeRhx7t8h1C61XCyKBVVto6WwkTHpNRzU-SPwvv27c1q2Q7U56_ZzhDDMo5E0PILrY8KiIMJ65vURKV6ogNVJzqBAiUOIRWiNQO4DeiS2i6hKldoly8MfIgmSpXcoH2mcy1pQSWSkAIYFG5BP2uMY39f1L2w44rL9qwYGpCC4DIaWLu56wXHSpDb79iGkKzrkOcWCya1_PVnisNu6SRrM0yyeaa7QPcFYIltllRCoAnhl4Gq02LtRDL4ig4N64bvxpH5l4hyVtdYETZZ6cjjFoAAVb7k2RzU-ff-bjQ1qlmZ2GYms5XT_vWCHeh9iuTLCKH4KnIeWddQ8XBOv8w5XrDjErh7Sj9Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
باصلاحدید سهراب بختیاری‌زاده سرمربی تیم استقلال؛عماد زارعی وینگرچپ 18ساله‌آکادمی آبی‌ها به تیم بزرگسالان پیوست و در فصل جدید با شماره 99 برای تیم استقلال به میدان خواهد رفت.‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/27413" target="_blank">📅 20:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27412">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsB8ly9zFZqa9SRcM2-16JdFZTRmux3O2fCenVIh69ZXiHJ3bNw4hJsL-InxMXt3xK-Gu3FObXmpvN7af5yAzgf9dgHbxPrBmNvI4HQX1OILp9bvp0TVea5DzsXujWbetDXZsqj7dy_Psj7Cq9uaQ2WKwsMYVfcT4yBcnklXtpWSOdwkYGqmmztrM2iKqPhVYs27eZQqdw7zpaUzQN1CpuW8cWp92GrmpkuM_RdpkhsyPsA3ILEppWx89ZzhugggQ6USBG6ZQRTbU9NYGef7zT1GESSxi_ZUzKKgPeU9Gv7VW0SoqPeHhH8gvAIqDvM0XjFQRqQjtHe6WcseISyG7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باصلاحدید سهراب بختیاری‌زاده سرمربی تیم استقلال؛عماد زارعی وینگرچپ 18ساله‌آکادمی آبی‌ها به تیم بزرگسالان پیوست و در فصل جدید با شماره 99 برای تیم استقلال به میدان خواهد رفت.‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/27412" target="_blank">📅 19:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27411">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNmPz2WTuLs655l5rOHsrZDyKZYE2hHKPeKLwTRwpgdJdoqOmKRJm50O4pIjPPV3JUI_IO3H6s6JW6fEyg516LcbIeWcfVSvJogeXuUbkukg8JoBYd6p8zWXPrrrgbuWCAng9aWXVx8p1vHKq2np2c-TpBXaHSu9xhUtg-DwK3Ccv0asZQEicrBeoJ0_2rVIb92WdLfTuR8hoLmtL4AD-IZK4yCalrJRMMCvA09ubvGoVf4jW81-AkzkBaZXjGQBfLmkJPV-20lyefOMrs61zz0ZK-81eXBvCMWjM36ejUJBTtl5EVJknOweadu2JWIigFopOBV3ugvBA2l6pIqGwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تفاوت دستمزد ماهانه موسی جنپو در استقلال و تیم جدیدش؛ درپانتولیکوس ماهانه 20 هزار یورو میگیره در استقلال ماهانه 140 هزار یورو میگرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/27411" target="_blank">📅 19:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27410">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1wnD-Vvglzdt4yDblwZXEliCZ5Itck4xN7590_gTVIEbREcK3xDuXs9h3x7k72mLnmyts9FWZRwz1gQEqSYbqQOOhZ1TMzCuGJd_mJf0-fB5Qs25Ata2ykkIvD_msVK49IdTtN_JnbreJZ8v4gE3-mX0MdbM5rk9zvasF9k7M7qHvyUFtQAjO9f2ChDGYKmHpjFswXDrrPiaIg0DxNDBcqfyu6ip96FGsjmR00sifVU5P25mkQy3kOhNuFBVDKSjxmmScL2ZDyA8SRFxg1yGrRXAIp9znboT5r2SF647i9nI_CT0jaMNhIqWO430d8DQOLIR4MRY9bq8wEuPO-uAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تیم پرسپولیس درآخرین دیدار دوستانه خود پیش از شروع فصل با یازده گل تیم منتخب کرج رو شکست داد. پوریا شهرآبادی مهاجم جدید سرخ‌ها در این دیدار به تنهایی موفق به ثبت زدن شش گل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/27410" target="_blank">📅 19:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27409">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej8Y0RGtvsZlHAFAUffMxQ2dRyZrM1EglGjpHIFQD38URfXxtf5bwzy2nCsgqNijv3XjtHbB8YVeRBnlvyBAwLj4w5un4--RrbhyTGx5UOcDcIjVqIbUgaHf9Kk43HQ7g8IWydUfN0c3slqfARN23s5TyhofqyfAwji3q7s0544NWsX4XvGkMywTRm7r6i0BVesYC7l1nj54pCdHp9TCA9X4kGHTwElcqYqK1-PJh13n8GH9CGZMXrEPAtZHbBV4gioOWh7nT1fr41iDRfRgEkE2lfD-6hbglsqXYuvP0VB5r6PmK5XZeyBe5IeUBX7-oYngVsQiShamvlSvByS47Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌‌امروز؛از دوئل شاگردان مارسکا و سیمئونه تاتقابل توپچی‌ها با دورتموند در امارات‌کاپ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/27409" target="_blank">📅 19:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27408">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJ66F1HykJfbgV67AZkfZrNY5z5p_adUZRGNIJF9WyehRdme53gR01hq1FFwAheu8FzkPJxNUHJK2y7c5Z2aOGWiq95PyZexd1S8TKoVtg01pbPTb-ZH7nq_SG_Gk_gPOe0u5C2mga_EVduKDFCScaWqNCDKrb5jD06jEqkApnoNr3oAlxDBu7VwTTZnbyMCXm2MvZe4afSHGaBz7W0pRH-6bwM99kAK7nBwFrymwwuWFC20IRzfo1JRQFZK45RNjviyZcn5Cs-gE_4hUYWjzV-JN99cn1-MtClwfxYlaq7mbR-ZTfNEc084Q7cYHDpmvKkpKnZmM7eCC1yR0ztP7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ در صورت تاییدیه مایکل کریک؛ مارکوس رشفورد قراردادش رو با منچستر یونایتد تا سال2032 رسماتمدید خواهد کرد و درجمع شیاطین سرخ برای فصل آینده رقابت‌ها باقی خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/27408" target="_blank">📅 18:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27407">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faz1PoZ1hZsEBBIshlZbr6b2Mpthw7Wr0IRE8P5V0PeKuCkDPHpVMXAbiFD5-VNQCty34-_g9tPMljmBHfWB0_BA5CogjHWPi_YJDSSCw7Na4TflUJY3er9-Aegf8QBe95uB27m3946xUbWzpj6_X1p0YtjtScAx8xWOJ5Z7KAtTvZna3jJP1D0TfZECyvZT9i5OOI1SNhaJFREir59SZnHukSlhY7cyIFBVi18CA0-zEFunl0-T0PtEUtTZRL_YMigRtmowySxiJZuQn_i95C4QMySyQqz536ags00rwJ_eoXE435tmKQZRx4DhS6Y_MQO2gPAPxAASyXnTASFDWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فصلی فاجعه در انتظار روسونری؛ آث میلان در اولین بازیش تحت‌نظر آقای روبن‌آموریم این فاجعه رو بار آورد. حدود یک ماه که با تیم تمرین میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/27407" target="_blank">📅 18:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27406">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9154dc0f9c.mp4?token=ARQUYkx6QmXv2l2GMWH6Uc3s4Vy6PPE2irhvRD92m3jMjVD2-Zf9kGv_QMkMqGwKtxKTEHeXCASvYQkyozdZPKIHxK6c2KTREhgy-qramdXyq5jkJDGiE0qAQrpu0F9g-SlxDz99omhKTJ_5Y5ypbJHDLC2g5tmdg3pt7jU347wQcJc-8IWyqxHN3dSL7MEl6CntslQtlBZwvu8FPj4RHR42oH4gla34gmyPFUGQrY2LG_AxRVQjAZ80ssAU_tfKU_KjbFDyNSjzRhO89xp-gsZR8RNB3-harOu1ItmhRgDe-RvKmuRtRA8lFtzrMMijOnY8B5fnJahAuDRJMnf4Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9154dc0f9c.mp4?token=ARQUYkx6QmXv2l2GMWH6Uc3s4Vy6PPE2irhvRD92m3jMjVD2-Zf9kGv_QMkMqGwKtxKTEHeXCASvYQkyozdZPKIHxK6c2KTREhgy-qramdXyq5jkJDGiE0qAQrpu0F9g-SlxDz99omhKTJ_5Y5ypbJHDLC2g5tmdg3pt7jU347wQcJc-8IWyqxHN3dSL7MEl6CntslQtlBZwvu8FPj4RHR42oH4gla34gmyPFUGQrY2LG_AxRVQjAZ80ssAU_tfKU_KjbFDyNSjzRhO89xp-gsZR8RNB3-harOu1ItmhRgDe-RvKmuRtRA8lFtzrMMijOnY8B5fnJahAuDRJMnf4Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت سوزی عجیب شهاب زاهدی در موقعیت تک‌به‌تک با گلر چلسی؛ تو یه لحظه هم رگ غیرتش باد کرد یهویی با پنج شش بازیکن چلسی درگیر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/27406" target="_blank">📅 18:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27405">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1-FxjVUdoB_PRT5GyejznBchl2qbiZNqyxHqgc6b3t17cBUYTR5B-rUAaWB0SSaRn3W-b9TY3oDtnmrkbrMrctiOZ88_0vx9hTSXUfD2c0AnnfKDlNGMlgVF_dUrrIrcYJzCw_h1BWG_D1HJUmwiOsEpikGShq9wKHQdgUsJJSX23m1Q9dIcOxzqEEe9Acjt3CeRIprQl8huc677CXQG92cx6SB9ohJ8U5laNAQzcgn_mv9jPHALOMtq37bLeTqwOeahe_6NrbgzKij-Uw7c62jCIUpcXVchvQfj46NKz67QCKpsQH4QmzCfm2nXlRf_nN08ti_P5RRIrpOF2VdqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پیرو خبرریپلای شده؛ ماخاچ‌قلعه‌روسیه‌امروز تو لیگشون‌بازی‌ داره و حسین نژاد طبق معمول بازی‌های قبل روی نیمکته چون کادر فنی جدید این تیم تمایلی بهش نداره و به باشگاه گفته این بازیکن رو بفروشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/27405" target="_blank">📅 17:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27404">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKRqu1jL3C8H3hcaUKYBNVajR3imaKV6TzO0U5yHV20H7UVqT7QhsOQ2uJn4kGZkji_al9jk5vccG3oVjWYFYfXdXJXBgwQUgi_Qra-FpwZ9QA3hdEnAI2LwWFSieYB3IrRQ1Ab0OwEbV4IswIiv6r75aV5eRzRry3_Am5BVAMa1YDVkFrHIyGhwulZU1K7BsxBDAuSXSlxw8OI2Pk1FxFcIykzwfA0gf8yiRNMp9g8WLA9rRshwzwUJvNGaElzPB5Gre3i8dTe9Vw71axaCFyhziBZRIW27Oo2IeQO61FMFRryX6dsJu6dDjJZxa3-KadmI53G8HyFy0PzkeBFVQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
ایرانی بس کن؛ یه بار دیگه ثابت شد که تو مسخره بازی رتبه ۱ دنیا هستیم بااختلاف کهکشانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/27404" target="_blank">📅 17:24 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27403">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8dde9dbf8.mp4?token=Z5YprtN463_J44F1frWt3ZOc99eTo6X2wED2UDhHw9njAre8lHCGul7u46KYBv_Ooj-kR3OL-PRDM25mGCzYTO8HrQ6XfqqJ_MFsXUbrnwMEN-2sTjjChcXac0qZsCNSE_uRhLMxfKqz1PHnjOL1V-l7P8XjrKfS-AyVY2-txD46R_X1lelSozEnmiMZBEh19HGMDeB9uKcahtkgBwbKAheOEG6cOd5GkcBnwg0OTvVB7s0qMyR6fveyAbZct69YDQ_AS2aHZt3Ktg_Yp79tniBHeF1sUSQUYo2B4_4jFt9q0Ih0q5oxs-3xi6qHCDj8cPO3XZ6EAC1ZBO-LEiLKXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8dde9dbf8.mp4?token=Z5YprtN463_J44F1frWt3ZOc99eTo6X2wED2UDhHw9njAre8lHCGul7u46KYBv_Ooj-kR3OL-PRDM25mGCzYTO8HrQ6XfqqJ_MFsXUbrnwMEN-2sTjjChcXac0qZsCNSE_uRhLMxfKqz1PHnjOL1V-l7P8XjrKfS-AyVY2-txD46R_X1lelSozEnmiMZBEh19HGMDeB9uKcahtkgBwbKAheOEG6cOd5GkcBnwg0OTvVB7s0qMyR6fveyAbZct69YDQ_AS2aHZt3Ktg_Yp79tniBHeF1sUSQUYo2B4_4jFt9q0Ih0q5oxs-3xi6qHCDj8cPO3XZ6EAC1ZBO-LEiLKXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیانا؛ درصورت موافقت مهدی هاشمی نسب، مربی سابق استقلال به کادر فنی جواد نکونام درتراکتور اضافه خواهد شد تا مثلث خطرناک‌ جواد نکونام، خداداد و هاشمی‌نسب تشکیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/27403" target="_blank">📅 17:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27402">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atZHoxRxo-Jnhq7jocfh7Z3fGcsVc9p8IM_yK2zxHX0fbBC4rvU4tDPylv6uyCE1GXeYDmBHlCt2VKBBoyxEgys7VqgdLy-8U7UvmxQICsDBTis7eoowDVns1dPRJTjbEtI3OBQOt_tfRGS1zTBzDXmeYKHE3vIrkvTspP2aCURUb9FZ2hYBcKylqd1ox2KbiloNyjsEHvGfFC9fjo4dSR92MVMd8aH6h2rKOWu78vbGr0uPRffLhXWjYzl7LYZcKDVFMCUIZyqBKtCfr2vTKu4-ueEAGKefgfH3cH8IHyxVAn_MVMOvTaWEEP12QrOmh3DReLikdQvKNxSW61Y59A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔥
فقط و فقط ۱۱ روز تا شروع بهترین لیگ دنیا و رقابت‌جذاب تارتتا و سهرابیولا مونده؛ برنامه دیدارهای هفته اول رقابتای لیگ برتر خلیج فارس!
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/27402" target="_blank">📅 17:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27401">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGkyjWSJrW1GMH9tDE5ex9wIaOPPOONMHXM-C0ZjuRJgN8NeN-6jsjvXnfzueD2CxgIpNhJf6esXsrrWming6SKfKj87xnaErR6IygaOOClgwM0nyBJALwBDRuJzxkld80Q_fQbIhkr6x1bn0Ea64QGOJ9UGNcZKK23U0TVHBI7uB6liuY07LAxaWMvYa9Kaso6qd7KIRjVCRYuWNkZObBhNcJ4GNEDydI-6LxG-gLVfbxco_VJPkfgqi77vULrv-siIbRsx6-EDDFYIG6wmwgfpOdfKcq4Ys9fkvnMTd8d0jsrSRbJBUlTZ1nRsaxSQ0D6mmoWN-i5ZgDsjK8wSfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥃
خسرو خان هستم و با همکاری مافیای روس، از شرط‌بندی و پیش‌بینی درآمد دارم
⭕️
بامن‌همراه‌باش تابتونی روزانه بالای ۵۰ دلار درآمد ثابت داشته باشی
🔥
💵
با عمو خسرو، آروم آروم به آرزوهات برس
🔗
آدرس عضویت کانال vip:
https://t.me/+J_q7c-COftQzOGM0
https://t.me/+J_q7c-COftQzOGM0</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/27401" target="_blank">📅 17:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27400">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b7307f5c.mp4?token=Il_sJb8U7uyVKbNm7n62GBg78ykvN_Imcr0n1Gy2ME5vqbwH6vdF8vrGZOW4leb-wNMyo84-i6PDg-euuGsIT785nhFFuk9jZjGLrQwP_r8uSyv2ht9eBlITVco6BgJtGQ7W_r-41jc-jtrExcHwpDqy-aH7PTcdQNvUCBWgMypoU0MtKJen5ZzyzlycLWXPOnRhEDSfBezBmTiWUf8JsXfDA0ekRBWFBDag0oN83flbB48-cadz0H8llDy64c1dAWdS4IC8DWcM3x43tfKWgJFZRR_Zex3qVTrF9RJnGccjPZ6-2Nyewdo7TwtoHrUjOAFwLGikTvojnxGcYgS0pk3D5xBC7-jrEyBNuQacUftE8bKQNcSl_CifzNC3hKIzs7vIEABrS89WXaxsyUgbag5CCatRgiu-_S7CPWGNRn4hJaXChVZ3riMQWhqI8BtJuMMKtjHtiMI5_4QZlep4xp7fa_b3iOrFTw4Deld37uzEuAbt0Okp1ZybfKtrCDk1-f7fnTQb2B5HHAhwNzaqli9ysRjSlxQhkYq52RTgmLV-5NEr2MHxJM4SjF3OufX6a61Nmv8tK74hCJ_uCaXld5itFw2pEAYxhMfRor5ao3mjj2axJS-lxXxqBoRxGjWYcUl4gbWgrwYSk6fTc9fir8eomr-7IbzkmqtRIrV7ENI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b7307f5c.mp4?token=Il_sJb8U7uyVKbNm7n62GBg78ykvN_Imcr0n1Gy2ME5vqbwH6vdF8vrGZOW4leb-wNMyo84-i6PDg-euuGsIT785nhFFuk9jZjGLrQwP_r8uSyv2ht9eBlITVco6BgJtGQ7W_r-41jc-jtrExcHwpDqy-aH7PTcdQNvUCBWgMypoU0MtKJen5ZzyzlycLWXPOnRhEDSfBezBmTiWUf8JsXfDA0ekRBWFBDag0oN83flbB48-cadz0H8llDy64c1dAWdS4IC8DWcM3x43tfKWgJFZRR_Zex3qVTrF9RJnGccjPZ6-2Nyewdo7TwtoHrUjOAFwLGikTvojnxGcYgS0pk3D5xBC7-jrEyBNuQacUftE8bKQNcSl_CifzNC3hKIzs7vIEABrS89WXaxsyUgbag5CCatRgiu-_S7CPWGNRn4hJaXChVZ3riMQWhqI8BtJuMMKtjHtiMI5_4QZlep4xp7fa_b3iOrFTw4Deld37uzEuAbt0Okp1ZybfKtrCDk1-f7fnTQb2B5HHAhwNzaqli9ysRjSlxQhkYq52RTgmLV-5NEr2MHxJM4SjF3OufX6a61Nmv8tK74hCJ_uCaXld5itFw2pEAYxhMfRor5ao3mjj2axJS-lxXxqBoRxGjWYcUl4gbWgrwYSk6fTc9fir8eomr-7IbzkmqtRIrV7ENI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گلزنی عارف آیمن ستاره 25 ساله مالزیایی جور دارالتعظیم در بازی دوستانه امروز مقابل چلسی بعد از دوری شش ماه او از میادین به دلیل پارگی رباط.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/27400" target="_blank">📅 16:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27399">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsstT4zozxuCY6pjwFD5CPDqOSeucfFnTxevnlVSmx2fiMEEAaYT7Rhhg5ElgEUxpLImRH0-jPAf4XD95oq80mwBIjODAvAKt7LUSPjA0SqLQIvfHaU7OVeO1vpkwCxayUoexl6OqmAx2RMPXMjeAs2al2e7QnpmR0zyUtFYBOmTbVVS6OueQrSN9cbgeTREGRQlLkaOqbZTfodLgIdGBGW8YfUSi64rR6jM-0RqBbUsvFdG4kRF3ILdkBGguBI6xv4O56zugt6nAH56NfwpiJJjkjYdM8KhBgKmyDSFb5Kig-RV-czx_f6r5S1ucHrxRvW32_CvutmkL5v9LYIwAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/27399" target="_blank">📅 16:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27398">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIIU15RMpbEWqUAs6wybwB1z__8wh_tgHVxf_M3KnHi5Ccvn4XKoOeXwGjGVawC--94yRGtRooOUPlvIPuQD8CAor4Imxlv-lO2-vfbjOxMmbj1MYRul8PZe_JDOmQ7vjGfJiQg6zLh4DRiy6I6rsYxN0bypwOm-t7Q33SNmYVCsTCLMicjghoEcd3FQ3LRYyOInIKUTbsjd9_K9WYJsM46aTuBOGN2lxxn5mHVe1FOS901Z8Aq1hUtkg83746oQbkkZ4tro4TMnje0uBp4ppkjp0MPAfOg_4Wf4Hhg-B93NDs36FEGVHSX_ZrE1ARKEFrSoHIE7chcy1zZ7VgKxrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
جوادنکونام‌سرمربی‌جدیدتراکتور: تیم خیلی خوبی دادیم. چهار بازیکن تاپ فوتبال ایران مدنظرمه که نامشون‌رو به‌مدیریت محترم باشگاه تراکتور دادم تا اقدامات لازم رو برای جذبشون انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/27398" target="_blank">📅 16:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27397">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c0eb7a5bc.mp4?token=qxCQV5W2DIIbBhUTPQbRVOvUiaUdPzYuaNmKfFaR8O2ej9R7SNF7kSka1OfVccWi1QoXTLOgwLBcAXKvu4m_mHio8xfgk7hxXgROeEPRUu3U2f9taCEgjV0A9jRDJzYfKovyjHF-N28s0vmpQg0133mqJA1vM6O95nU_kCUAzWaqHS9QhtY7uTaeoqfow_4arTu4fdQuaGG_KNUGLwhmRuR2ksBEMI9gfN0rAxW49OQ6M_o30GeOtF2M2vK7cPtcKM_4hf7TqntPTKfW7TvuvFrX1RMuLx2rTeyI0-vCuyTZlno1qa7UcKzagGc9adsWCb_fKfgJ_Qe7NOBC330QbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c0eb7a5bc.mp4?token=qxCQV5W2DIIbBhUTPQbRVOvUiaUdPzYuaNmKfFaR8O2ej9R7SNF7kSka1OfVccWi1QoXTLOgwLBcAXKvu4m_mHio8xfgk7hxXgROeEPRUu3U2f9taCEgjV0A9jRDJzYfKovyjHF-N28s0vmpQg0133mqJA1vM6O95nU_kCUAzWaqHS9QhtY7uTaeoqfow_4arTu4fdQuaGG_KNUGLwhmRuR2ksBEMI9gfN0rAxW49OQ6M_o30GeOtF2M2vK7cPtcKM_4hf7TqntPTKfW7TvuvFrX1RMuLx2rTeyI0-vCuyTZlno1qa7UcKzagGc9adsWCb_fKfgJ_Qe7NOBC330QbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
ایرانی بس کن؛
یه بار دیگه ثابت شد که تو مسخره بازی رتبه ۱ دنیا هستیم بااختلاف کهکشانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/27397" target="_blank">📅 15:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27396">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ca826d21.mp4?token=Eal-RBuBmdAhGhO1xgfT08pLNWrpeTiXPeA3hHga2blSXjdb9Eua4qTSG-9OhNmH7v6rJmg9rXghNFSkGLxH6zo3F7na43I8x7HiTL5zzvDD1r0QuzjCvTVyqo1-ObRa3R7KBg5PHxC2hvkItJrSqFrhNJLBhKeyeY5xB76MDV25YYroOLqv58Ajkvmj3IB3ttiDw5s05RdcPBIazq4lcZPIDJIV7UcYYRAnC45r5NgUmNSWdi17dJqgDW1Ecrj3WZc5xYafdwZ4zarVll-mIlN_KbGtjssyzIVQD-v_JgPUGW2oGMmWqYgouHuPtlnXS6uEV-6KH4dSiU725fA51w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ca826d21.mp4?token=Eal-RBuBmdAhGhO1xgfT08pLNWrpeTiXPeA3hHga2blSXjdb9Eua4qTSG-9OhNmH7v6rJmg9rXghNFSkGLxH6zo3F7na43I8x7HiTL5zzvDD1r0QuzjCvTVyqo1-ObRa3R7KBg5PHxC2hvkItJrSqFrhNJLBhKeyeY5xB76MDV25YYroOLqv58Ajkvmj3IB3ttiDw5s05RdcPBIazq4lcZPIDJIV7UcYYRAnC45r5NgUmNSWdi17dJqgDW1Ecrj3WZc5xYafdwZ4zarVll-mIlN_KbGtjssyzIVQD-v_JgPUGW2oGMmWqYgouHuPtlnXS6uEV-6KH4dSiU725fA51w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قرارداد عارف آیمن ستاره24ساله‌مالزیایی جوهر دارالتعظیم به‌پایان‌رسید و باتوجه به اینکه اون هفت ماه پیش دچار مصدومیت شدید شد مدیران این تیم هنوز برای تمدید قرارداد این بازیکن اقدام نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/27396" target="_blank">📅 15:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27395">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0574804636.mp4?token=kLhlBe4qLhv6xNOL-NvtKEgY3zSonJmYK72iAKxfkqly_CLNbMaSsl2ZgU4IbsZgXCOZlYAxLHNCfiSWEpjqEwXlmZVvBRGvmRZ56GHiCY1ClPHC-kIVW8NG51H7giDKlXdXqvz1sTwiBIm2B_C2hqcm1v4vqhq8u_qOUWll2ncGPWwjlejQ0X19tw4iP5QMyIYonQXxdH7V5x8TrZ9lcKeSfhjMEFTaKVufwUDhnZaXRxg0od5pTr2vcAYB9KzklifBWcogiAifXXOl8t9tNjp7j6JEpf54fL7yYopUATOwX5Pcd9EjHA4AdMRFEaQL-290gO-nBULl25DJ_NdVyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0574804636.mp4?token=kLhlBe4qLhv6xNOL-NvtKEgY3zSonJmYK72iAKxfkqly_CLNbMaSsl2ZgU4IbsZgXCOZlYAxLHNCfiSWEpjqEwXlmZVvBRGvmRZ56GHiCY1ClPHC-kIVW8NG51H7giDKlXdXqvz1sTwiBIm2B_C2hqcm1v4vqhq8u_qOUWll2ncGPWwjlejQ0X19tw4iP5QMyIYonQXxdH7V5x8TrZ9lcKeSfhjMEFTaKVufwUDhnZaXRxg0od5pTr2vcAYB9KzklifBWcogiAifXXOl8t9tNjp7j6JEpf54fL7yYopUATOwX5Pcd9EjHA4AdMRFEaQL-290gO-nBULl25DJ_NdVyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دی‌جونای‌کارینگتون فوق‌‌ستاره سیاه پوست لیگ‌ زنان NAB پس‌از اخراج‌بدلیل خطای شدیدی که روی سوفی کانینگهام انجام داد، در توییتی این اخراج رو‌ «امتیاز ویژه برای سفیدپوستان» دانست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/27395" target="_blank">📅 15:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27394">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifiiJr6VZt1kMBR8ieUFJ6oQhurgKsMTJrw-I1KI_eCcRhMVmD7hyTvZpWHykAeJr7xKQTjSNVXVNbJQoGQ9fVsRCz5_Rwkl9GZjueVpjvPjYuj3GPcdsW_Iw2sgLcVEvW9OZztbqw0F6zyBRPi7R5PGmDiJ1UpsSMJGBetzQfooFODMxUkn64mngOeF_4hQu4P5ExJxT7d1lFrzPVGt-TUV58R6d7CPIGRlnCJR6ky9vOTAmjrujxVQwS_CdeveDjDYgGoDLmyq1eO3prJzIZZG7QAbBWHtFxJv3Dv7v0OUHnu41BphK1yuRTTNqX8s0D6svss_cPntPKW7XFqELA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ حسین ابرقویی مدافع پرسپولیس: از باشگاه‌سپاهان‌پیشنهاد دارم و مذاکراتی‌هم بین دوتیم انجام شده. ظرف‌چند روزآینده‌تکلیفم مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/27394" target="_blank">📅 15:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27393">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnRTCtiPWfDkKgG8Kvxwag5IruUSRNIqSOkBSrGWcjiKxKO9PR6nUOp3_l4sUq5_OaE5k6GEk2NUlZXkenvkCUsBRrNNcxLj5tlsQ-R7GhixA_w_UULKIJK4Q-k_dQlcyfG0F8SzO0KbbM2OtG-v1czA3PEUrudTZ3nt0TUG3RNdECr1pN7AIr4AqVhqcZa87nPhW_4_iS8KS4r2WgfC2kBu386XIWIwm618bHeBORlTPZMhF0Ctoc8ZpZ8nmLui1lpp1OZHTrYBmyYG4bL8EAcVDGV1iilkSLHHDd7sIS26r_ibQLMhryn69JZl1ZazFiF2BvbSAoQF-4hUX22q1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینکه‌گفته‌میشه؛ باشگاه ماخاچ‌قلعه رقم رضایت نامه محمدجواد حسین‌نژاد رو 4 میلیون دلار تعیین کرده کذب محضه. بار ها این باشگاه به مدیر برنامه این ستاره اعلام کرده هر تیم ایرانی دو میلیون دلار پرداخت کند و خودِ حسین نژاد هم راضی باشد این انتقال انجام خواهد…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/27393" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27392">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arIF4RXup1lIb-dSBkvPNm1UTuL_zXHCOWwhjYFDD9xO_khXfByOOoTPc9y4gkRiEWdpyyAZ2HeyuhN8gub9MGhnZbAvYy0okEorNFOxLJ99pMsF71bxju2O_GtJfaBEoxCeMbGgHps1N1hBBWQZl8y7pPQHXm0LxycgHvAYNPYYT38OHfPjD6uZLF3g9x5TaTQ-SHsAAFiwwW2UkgnR_VJ4mO5IKWyD0HMWWDznhBDBiL_b3V1DA_TSCYQtcQ-upKUv8pWfNxlTWQT7mz3RPdJMnncVeFxlUlHKh-UNsNtqqOwuqANrhk1NzWDJZ7PXun2wbRx3FRy7puepzPiJaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
جوادنکونام‌سرمربی‌جدیدتراکتور: تیم خیلی خوبی دادیم. چهار بازیکن تاپ فوتبال ایران مدنظرمه که نامشون‌رو به‌مدیریت محترم باشگاه تراکتور دادم تا اقدامات لازم رو برای جذبشون انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/27392" target="_blank">📅 14:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27391">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4ZX825WWsT6oQkjn04eT7A2U0iwwWSPz708AUsaciKsIYe8TJ5qu98lgc-D8-BshNenG3-ueCafjahdXV3dn6JkYM5BbGNPy5rv_1rVsNVGpmifSAehPOitPJOpFe-TSpryL9qmFe-3JlOj-gMIRmAsN3K5BJ07LrbSwxQ2emeapf9wnCHeIVccvFnpsP-4xcf190o-6IUFu1kzziNCvVQV-Y1HUTtX6pjrjUUgw7gQoFjC9ci25TeW4bwPLiQB12WbtZqTxWmtT9KoQ5AQYpCKyM0ZabJ_H1aARSAUiigsZHMU7o3wiVYuoSFm2rWqhTRT4j55D5vLRTCgeGod3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ احتمال داره جواد نکونام از بین صادق محرمی و مهدی‌شیری‌یکی‌رو درلیست خروج تراکتور قرار بدهد و درخواست جذب رامین رضاییان بدهد. محرمی رو مهدی تارتار برای پرسپولیس میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/27391" target="_blank">📅 14:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27390">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3mC6JNE7nNbk8fUCYXUZdN-TcVCm1_rR6U9sSNBxDoIs7TvYLJ1SC7-UDvZbBo43jeDR2hZ2u_hPgWuNjDisJ-bSMAlKN1OaZ3lEzlAJKXqJiqZ7cdqNstJ0A0A7xXSK6ky-RHUOUD4nzz7EJ70kBZRo_prY6n8Ik1hkvVeXFNvuw-DTJwOpFeWQ3Stg21Da_JJfJYOvuQt81JbupiJ5w4WzHadxSHDWslOWLO7KgGALc9pkE_HOl48K51mlMVwnrrHTy89FbLfcRmydfRkjxOijpgr_0-vFl4zM0WGUmZ-xtebJV9TcPMj2IgTxdrG-eyoL_MgxtqWJjTo8rtXvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ باشگاه تراکتور رقم‌رضایت‌نامه‌صادق‌محرمی مدافع‌راست30 ساله این‌تیم روبرای رفتن به پرسپولیس 100 میلیارد اعلام کرده و از طریق مدیر برنامه های محرمی این موضوع رو به مدیریت سرخ ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27390" target="_blank">📅 13:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27389">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpQdV3vvTm5h-fu987fA-5_kVOWo2rTLzeTkYXT9os8qGRcXvjcF9tz3ICcqz4GKsms8HP_UYnYb6fYaBO8URQxQUJQSIhM2mZKkvQiFS_ZUE986W4Na2BsfUz6bjrOEXgeaBkUPFCQQbSrWhunFmvKeBhTtmEAUX59fLHNw7TtfCVolXgwhY_iM-KF1aUDwnQ2a2wbqqI_W7L-zNjEGLMemqnXmlozmdBC8FdVc6PXyrtBpu2VKn0VY3Dxzo3jD79qQI8mNM3PXoT7vY91hksshgj4Ayz8qwfgeMjukjJDVVSWoawFhYuM9MkzhkeiOrmgVblkx_JA5sreKsLXFbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🤩
با اعلام جرارد رومرو؛ دکو مدیرورزشی بارسلونا هم‌اکنون‌درمادرید بسر میبره و قصد داره که فردا بامدیربرنامه‌های‌ خولیان‌آلوارز جلسه مهمی بزاره تاراهی‌برای پیوستن‌این‌بازیکن به بارسا پیدا کنند. چند روز پیش مدیران باشگاه اتلتیکو گفتن آلوارز خودش رو هم بکشه…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27389" target="_blank">📅 13:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27388">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0gKfpW59HnbdY3EKzBQZS102mfRJHX6QQLuJ17kjPOamGyp_EgPebRvy9XPUVF9wwD7Ve1Yb7GTY96o3reSSMcF68BmvErIADNtjDbHIwnYTrrzcEuRKjmKZY1B5zvOywJssLHHWAI9RGr2LiGsOd9sgipDWYQMkSEhDkE2tz7fL6ktKg2Od4JP3Sq8x3yV9jW8anIX7vVXkRkeJhyxu02CXqa8xlRfwjalHvRBkw648caUiuK6-lXFFPeVsVcaet43wVDSn4KcfAXX0EK5VEZayQWygTWtyYTQ45GC-XjdUwKjoRezuY-bNiGpYkYms1dLYVBmy8ttQ853DkcKCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 28 روز پیش پرشیانا
🔴
شهریار مغانلو مهاجم سابق‌تیم اتحادکلبا با عقد قرار دادی به مدت 2+2 سال به تراکتور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27388" target="_blank">📅 12:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27387">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222f7c35af.mp4?token=mAQ7DUWws6fLFJHKiPGj-SO5SWY9naiRCRRWzQkaWUzSCD6v-K0GKCW459umL6UC2P5IWMnR9g3-Cjr0y9b2VvH-B-KGhCNJq_zGRBNaRY6Xw0izovGjKoX9h15FJQon1ldN7QdMPXdBFAGhsbrR1slbZhUPU8uZGfl0vPtmINem2ERHWRvi1UC5uRLj4EX5I-CGUAJtKucSL5rFNdEMXv5wMEysYATRZU21acFoGC2HcT2Kw6MC1y5Q3AHVvK1SkdnJZ0It-KHyptP0Vg5igCQljmiZQbxzvc6A5DsYhvV3LECLddoFV-ECdRy2U9NTYyMqghnSPpWLuHhlM53O_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222f7c35af.mp4?token=mAQ7DUWws6fLFJHKiPGj-SO5SWY9naiRCRRWzQkaWUzSCD6v-K0GKCW459umL6UC2P5IWMnR9g3-Cjr0y9b2VvH-B-KGhCNJq_zGRBNaRY6Xw0izovGjKoX9h15FJQon1ldN7QdMPXdBFAGhsbrR1slbZhUPU8uZGfl0vPtmINem2ERHWRvi1UC5uRLj4EX5I-CGUAJtKucSL5rFNdEMXv5wMEysYATRZU21acFoGC2HcT2Kw6MC1y5Q3AHVvK1SkdnJZ0It-KHyptP0Vg5igCQljmiZQbxzvc6A5DsYhvV3LECLddoFV-ECdRy2U9NTYyMqghnSPpWLuHhlM53O_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برگ‌های‌ریخته‌شده گزارشگر بازی امشب سپاهان و ذوب‌آهن‌ازپرتاب‌های‌بلند نادر محمدی؛ واقعا قابلیت خوبیه بشرطیکه‌درست ازش استفاده بشه نه اینکه از هرکجای‌زمین توپ رو بهش بدن بی هدف پرتاب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27387" target="_blank">📅 12:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27386">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sH9lJnnE546qOYtBupFPqz1-jgKLrjRYO5O6wz-wp5uwM1vnXpkbDJ6MOpLE51vE6vYxY2J7nAdp2HP7_y2keeEVyPb7ctryOC6q3n2l72zNHWXifZPollWtdxMytIdxn3ldc-IHNdNkzN0nZoduTEUIMWUfduHZfoZHXyfoP6QBbrqjzXY6CvmPhUl6o5So4ZuZlfFm1Gjl7C4W70YzHoLSZGrTaYQ71g79-n7_iIlJ5SRUmkxn5mXwHmkXfKh-AdKnLzNuxvVbWPDZDxQ5RHzp786ozrEEEMdteYz9YQda55hIUpZ3vbp_0hwmLkWFNnZCE9vi_dHYU2Eji7SN6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخباردریافتی‌ پرشیانا از اصفهان؛ مدیریت‌ تیم سپاهان‌ با‌ حسین ابرقویی مدافع میانی 29 ساله باشگاه پرسپولیس مذاکرات مثبتی داشته و درصورتیکه حسین‌ابرقویی بتونه رضایت‌نامه اش رو از سرخپوشان بگیره راهی اصفهان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27386" target="_blank">📅 12:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27385">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuIwxSD7EkRn8SBRG6vqu10OhGdCD1c86QiJbIIdtQKLOEqf9W8DVOIr5JSWqq2UMdEIh9GxWCrrrFPHi2YQcmhbb_QhFAKFuL2eMj6zeGsEP9Vc3uO471n9UQU34l8vqTNPRqlqKe8IdVFaAf0YRTKqRnSCDI6eGbOn7Ps2FhfDGBA6wrQ4gJv-rK20Y66h2Kq6qlnk_i_M_Y947OpJJ8XyjWLWP47VTXInTCiRCgnQ6J8elwRemJbBfTzQGZOzfgVPH6PiL_N87lh_6a3-aFxjZ1yb1dydUoIZo96AFl8lpDPK2xXYcvmGdLnTW-Kr3M9jNCTyfan_ten_BqfsuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ بزودی فابریزیو رومانو خبر پیوستن قطعی رودری به‌بارسلونا رومنتشر خواهد کرد. تمام توافقات شخصی صورت گرفته و توافقات بین دو باشگاه نیز در مراحل پایانی خود قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27385" target="_blank">📅 11:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27384">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSib_VRNfGGXXvefXrrNqCkPasMz8oGcxbGK3y3Y2pwdpyzRTof56N78P6oSZV2EH9uyUa1Cg9U1AQYdcPPV7X4FOTYDZfZX42zUkliThd3Z7oPhmLJ2pa_GEEHxp8vyvWmSxP-dYqJETY_FhlWZYFfmRtN2U547e33LJq_lrMkWZTyfEkwirsli82BKjZdNSnqmTJ_6M9_miXmnmW8EDpQIv0CqceVNpFJXochUv5pTRujjHkVVNpALIP_9kfyeCxek3TNgQCNt4Kj3yQj3YjN3BtvklIG71MYvHRLpJk-TzadH63BH48Go_7O1UXmrHrGz28IRZCdzoyx_f8B34A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ عجیب‌اما واقعی؛ رامین رضاییان تنها باپرداخت 100 میلیون‌تومان قراردادش رو با باشگاه استقلال فسخ کرده است. در واقعا زمانیکه نیم فصل باشگاه استقلال قرارداد رضاییان رو تمدید میکنه بند فسخ 100 میلیون‌تومانی‌درقرارداد رضاییان میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/27384" target="_blank">📅 11:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27383">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLQPcxRwTbL-NA2GJMdJRpMk-LIMw2GSDueaJe0pqpKqfKD5_QNjtnDBwW8mYboD5DAF1nWVWG8S9yZcBF1BGtfS16CGUif8kJeECQUUDQ_CrMOlLgrcWw9JoupB9mzAfeKdKOHQOEYsQ7qLxHDnRBrMLm03VUZEYqtnu97YYdyXDTLJl7hvilDaLCqzDb67ptaiOAHk4Tt2fTUrM8VebtWFlftn3RECxAeDB7bEJw4jbeh1JLx8XevsZBNlZCxaTNE8QOw8sTEGKiWBQFcAhc0w1vIdF_3dN3HrRsW9HEmsYc_OQfMRBiQl8pMQhmt3R8avf3JVyRhA1-AxLUZLqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌رسمی‌باشگاه‌تراکتور؛ جواد نکونام با قراردادی سه ساله بعنوان سرمربی جدید این باشگاه انتخاب شد و جانشین محمد ربیعی شد. محمودرضا بابایی چندروزپیش گفته بود اگه بزارم جواد نکونام در لیگ برتر فعالیت کنه بی ناموس عالم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/27383" target="_blank">📅 11:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27382">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jr8Bmt7Vn169m395jP-Ui4CsQ4GGSG3R5VLzN4obGEve8LQpHfI7OKzByu7-IEduflFHx8_PmoMTy_4RDJUUBrg0nAqOR_43Z3YSj5BpaCczBH7jNNfmFVj8G61ohdLjGYue9sjY4S4suR5JNAQnaJkpFSFAREAdNhKmlWB6lpZmONCGHB5R7IxA7_vu2s3Jb7am4vfRkfdeSNU_-1bjCBQZenFLGODj54nzgRzDPvULFuM_L_jGKNKO_Z_0KSgmikYn4E11NPtXUjjvAPzmTsed1VRiegMdquFJvmbCMrpCb8YPZ_XHs6H5drslj-pItIg2U15DExjsk3afrlhycA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27382" target="_blank">📅 11:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27381">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtPz8lTzq6Q2tFdJTqYdqbKKnIS38Wkoym-y8jBRX4jTVBUkGh6VnBivh3r5sQpX7YqPejN9loefFZY5ENnPUXjzke1tnuUxcHXUmfKsahDrRktvb0wOP323R3GUj7IMljC3rDLORmtRjhU3FawuOILUYOXsVX0d5vQsfempd2hGZP7XEsK9_CqjB-dfPoY1ch_NqHd_VtmGzK8egbGOs9G3_kbnb6X_IlioZz0mi_iNNqv8pYMpZ7WaGbfgkFY337hLCihAhdiKXOqTPEItdaVwygglUnK-FTlxjo9zcgN3bkcF-Ws081rPXCI5flbbJO0X_KQD4j6fQ8nUXzceXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌رسمی‌باشگاه‌تراکتور؛ جواد نکونام با قراردادی سه ساله بعنوان سرمربی جدید این باشگاه انتخاب شد و جانشین محمد ربیعی شد. محمودرضا بابایی چندروزپیش گفته بود اگه بزارم جواد نکونام در لیگ برتر فعالیت کنه بی ناموس عالم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27381" target="_blank">📅 11:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27380">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L40STQrru7Oe8WUnHo7NHTuDg1ifueeRTKlyZaye2a5P-7OkdkdRb-_019D5khUa4UtLDwFdoSEkWWEYVHZL2chM0f26M1GpEfJBIwy9RLxDtHbQs0T_sM21SagSwA1gQdbHv1pWGR7gPprEt5Y6v33XTealleAMwsitOtJxitOLwU6P991tSp-kBH7MTXPYIvWvDWadjkSVfuWujTx4g-i2U9krI-rJueVs3_9LtaRMVjjEJeKg6GNqlN47BICV9HTAUxXKelcAdO7NvbpWvq6OnwXkHzccTW7o3kLn65BLbFxdVO0dSArpQelHEpOhepjvI7kJCiILPaXM23KEuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فوری؛ در آستانه شروع فصل جدید لیگ برتر؛ حجت کریمی مدیرعامل باشگاه تراکتور بعد از توافق‌کامل با جواد نکونام برای هدایت تراکتوری ها محمد ربیعی رو از سرمربیگری پرشورها برکنار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27380" target="_blank">📅 11:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27379">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvWWUFD2JWPwOIJhVzP-3xyNRGzRLYQDjRUgUtskHQ2kV-Zhmia2zFZrj2_ySXE6rzbo1-Ooy-iX6OIHEFdz8MO_mpqlF1bNct_QoL5hzOolCx6RI8CrHiZ_jIlmY5ImDdoq3_ManlF6n1zbL4uivF3oDkmC3JXuOv1_1vRgRe8OfvwpQCPACN4knLli0kWWTncWoBenXF8U5x20gXE0Y_98g41IMkZ9ERQYVQ6yIQIwbF4FBZXqnSkK0Nks7tffyShs4gAOkxORj8DCJOx9Xgg77lF2K46XduZbVW5OlGCqyLhjIS55GWyez2BmpJ2g_W0ePagwk__OS7wqswyN9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ امیرحسین‌طاهری‌مدافع 22 ساله نیرو زمینی باقراردادی پنج ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27379" target="_blank">📅 10:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27378">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkmgmYf1ry8DuDRMUCsBD7jgOAR-TTDynqSEyme9J1otYu1GlXDFS0rOctrcJbJaWMjOlvGyCLHkxluVQT3Dyq7Hb3C1bpcHz5vh0k43gZacMaC-qaCk9ImcJ_qHCi_J75_oj8MPlntbUMplYUj-39JFdS9C9EyaN_ENEt2UQ2oyKip3P658GVrHxAM22MrwD9x0Yo14pAEkUT6e5fgdqZPtUqG6zqXZVuAhX_KCVZh-VamHpkECNhkb_Oc1aJnsLxmh1XdsF0GId0OBmeFACETDBlSBS5ukisITGndbnedM5EIsraTX6Upr2lGLGFDgCoXerrYHUt-u6x6ahK9taQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق اطلاعات ما؛ علی کریمی از تراکتور نیز آفر بالایی دریافت‌کرده</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27378" target="_blank">📅 10:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27377">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkN5FfQ2ZAn0kCo3xpkuFkqn3uGjp3CIRHAr0c10MuKZwq6BKBKKmPeVX13YDPoohaA_wN1D2ETRkPnY6JIJ_YQW1gwDowzOE1Bwvb0U8OhQe4Ew-xdsDdg4WN1MH4r_uijhlaHGOlYE21bNisRmtzJLCFrd1TphjLDJlDm01dEnmKZm2Sa1SeBS25uqbeaZCEtv8g2Mgkla2Kb7BymIA7ijTgb7_e-M_kO8xy2oAS8CDtEeujWev-ArAddSfjCbKRhmUfVQ-a0jN0YipjRSrLUtCIGasgt510AienvOBfRwH46o7BfgIX-1q619k6iQnR0h2i0zxHbph_SjFvp6jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فوری؛ در آستانه شروع فصل جدید لیگ برتر؛ حجت کریمی مدیرعامل باشگاه تراکتور بعد از توافق‌کامل با جواد نکونام برای هدایت تراکتوری ها محمد ربیعی رو از سرمربیگری پرشورها برکنار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27377" target="_blank">📅 10:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27376">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vejud2YuWx2bk3QFHwO5GbgBUhi-MxwHyUmRMrWd8jR8Zpt9OcgXWkvgefsqB02-JNDA9RbnhPaM4zFoWavAEcyZn3STCEjvh1pBvdyyv0OooBS7dYLbUQBqhRI92K-nTeSlXF6cYsimJ3-ojfIVKydS45Ob9R_HKaLNCc9DHVH4DVIJcJEPRvNBk1aR1jMYtjlPt8MzicuE29xZrBv-QKQgGYoAjM9AmMjgBrNfM_VGh8I_m9qR3RmfbidHdPNFzWpmojXTNPNHAgBgtYuhziSSbVS6nD9zWxCNho8QROun1RLsw9pAnyLeGSTnKq7T6-jfj7ISZbGv2KWI9mFV3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فوری؛ در آستانه شروع فصل جدید لیگ برتر؛ حجت کریمی مدیرعامل باشگاه تراکتور بعد از توافق‌کامل با جواد نکونام برای هدایت تراکتوری ها محمد ربیعی رو از سرمربیگری پرشورها برکنار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27376" target="_blank">📅 09:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27375">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4RmvV4GRihLa_OKyn24zxZQ5Zb7eatQ1-D_ohwtu8lR5oCWuBULk5FxlO7P7WiNa5CNbza5joW8TJverIYmmCXTLQOiuQHs7NcLHRJJ92s8rwRF-sYNkDbKH9SOGlw6XRcbulN2rSRb8vIS38kwvs37_Z1IEGUG2IzsGiZ9AKT8Of6btFQNcKbouEj6N9QGscFeGIPqEMp9i8eIfFBGux5TILsb_yaujHYR05KlagnfbwnrRDNamuiHbv6Oj-nOVptDQMSw_VWz8sNzdwhscyzUdA13HdbHt3TawoA7iujtXZzHVyzbdTVUvUtI7k9_89SjYgDXfZ4h4P4D6yvVBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فوری
؛ در آستانه شروع فصل جدید لیگ برتر؛
حجت کریمی مدیرعامل باشگاه تراکتور بعد از توافق‌کامل با جواد نکونام برای هدایت تراکتوری ها محمد ربیعی رو از سرمربیگری پرشورها برکنار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27375" target="_blank">📅 09:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27374">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rga2m_hiRxR6JjJPieiqymKSD-7f8pny8Ua8dbyx_Tohuo-6uOpa9woP-dNBIw1sZiV5K_aqWeiARS-xzQEGjhQJz-9z6BWsPEL2uDx1WsUuryUYsO3vCKbJYnQDrbSWoIQGSo8OfWjNCOvw10KvcrjKEpeCZk8LsKzSxFKnggvLWmPIMXxN-iiT8h6zOzIVHnWFoec-7ugdky1yYSS_pboR30Olf4dpXLMlLIEHzbHpTQd4TZ_SgsYe5xw1p-TU8Z5h-v_RnOlDcb6CAohtPWpU3YUWo0aK1HtyTR3RBpi28U7OljJlDhCpO5Vkb4sZhQw4PiV_PbOM64iQVJ65hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت‌شروع فصل جدید لیگ‌برتر؛ 10 رکورد تاریخی باشگاه‌ها در تاریخ لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27374" target="_blank">📅 09:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27373">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-Q1medUUtwYp_bGuAMTdoron1uVmx7kPVI4FdANjAkW2HS8i2R0lcFtgFy-CCl6981nc_JKw4wzVzSScEsG06qsdJJK7jy2JWVfufWEVdb7tde65nMK1kjEbEzlriO7V2hBVUMRQ_BwBwX8PE_yZ-0MgMpG4cD-GYvaIesKGtQwuFN9wwqrXKbEGYT5mPFMzn-05kL6Ms_09ih9N47OKnc3C0uqUrbVGJ_lhit0rG2bGdcFwYISEP5GE53-6OUfJNpO0o2-zUmNGuk8HbDgu88UyXyrRGdMCSTbsAZspRFqrlG8ayNUIpimg4io7IRctvPpHwTL0bks92yOJewdrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خورخه‌فقط پدرمسی‌نبود؛ ایجنت، مشاور، رهبر خانواده و... هم بود. موقعی‌که مسی تو رده‌های پایه "نیوولز اولد بویز" بازی می‌کرد، دکترها متوجه شدن این بچه مشکل هورمونی داره و باید درمان بشه. خورخه‌که‌از پس هزینه‌هاش برنمیومد، این هزینه رو از نیوولز و ریور پلاته…</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27373" target="_blank">📅 01:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27371">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQfJMxwzxus9X0hnzgENBIy6nwF2t-HJL5GlYrziVj3WA90X0NaPRch53VqvGpUgHTy88ltiFWffzEYXmv-wrYZLLudemVv4DcVxIyQXr752_AIU9J8crMdIr-0rSBattpuejk0mebcvVpkm6ED3Za_5_h0dKMuW5eSx7YWgnSREc5pKrQbYXhu-HlDd9EauElAaLv4O5e17zBj2pGDpHMZoYez4ZEw5GLIJnr9aV8FHVxnEdlKucln-HJETFvFm445QsnNPoCUC7WQZ0MnHe675ZWIdxbdoDFlxs9e-u4_byNHyH25M9qUoTmDx8UNVexSMrVLloTyJB0F3e7QJ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌‌امروز؛
از دوئل شاگردان مارسکا و سیمئونه تاتقابل توپچی‌ها با دورتموند در امارات‌کاپ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27371" target="_blank">📅 01:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27370">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEjV4YOIOAZOhTgaSSe2GbvJlDAV54bueRp0s58qw1JwhYJJeMUWwlWuJIFf6UCqGyehKqba_bnb1pLSYHqPS37HHQXzZwtr2iWSiTSMRPqNBxlqMQGv16jNDACxXoZDTjWgH3CpiilmDlrHD9ymsjcp1XAsUOyv0fgoagakskEwffrWy_isvoPzATc0oVzTZFequBm0uuY76QtuSzaOJxecs3jHvtU2Qf3jebrudfqhZfqeYXPw_XLcpPVn0rlhRz-lriEHD4cs0ZSQscRrE4MIkkWXo5zA1QCsmPhz66JPnnbIzabxEbyuaOAskyyOV-4B7pE8u0olRuMk6p6L8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای‌ دیروز؛
شکست شاگردان آموریم مقابل چلسی و تساوی در دوئل پاریس و یونایتد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27370" target="_blank">📅 01:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27368">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWZJ__ooERljQtUc0qjbiV6yGsDLGxl4IlPOfOo3amYGQR_7E0e0n8ZxVzB4jzUl-TDtNBej7xWMcm6ICslhqWymJ_goYGg4h_er5xCxuR47rrmrMiBfHTRypDrzFjtthHLgXa8NQmvFDf-lJmpvNjQqsyuCT6fpeGl7tYgdvn-NYsN7uAUS9iGDFqa-n8qhJoaYc8ZXzvM40J1Qkc_u4qhGj_S1KD05Lh2-Nh3TdSsAuJzGIuJQe0biXOMl60Op9AdAI9199BQsaxvOQ9lpTjYFyyfckcj_xBFBekqe3G4nISoz6z5WvgrZexc8HqI7jKdbDP7l_D4eK3sGhImIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری جدید خدابیامرز دیگو مارادونا افسانه‌ای برای درگذشت پدر لیونل مسی که آمادگی‌اش رو برای پذیرش مهمون جدید تو اون دنیا اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27368" target="_blank">📅 00:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27367">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCjNB_mJ-sYFAqt_ALeEmzVa4E7XqsF8nU2uZL8UI3MZsk42lFr1ZmV72CIPYmGMfRPIj5qkDYZmpmfBRvrIBe00BRM7EXU9pfws5oKHxxb4jzIB9JGmTsUR4O0-aHJAt69B6oh9OtjCwGNkcwNCTnYmOgziJr80RUppTdnM9REWvumoDIQzUNjFWWTApjttzGASSYVBvcgZN94EhqfWW2HiaB3MDOgxNe7S5dzzSKk-mLQETJFR_yPhENtJNWKiV0LL3b3RWQRMmMYd7PT0FlXTnKqYotto0NXv2Ctqxp5ecWxN2nunOFg2MYLmpFI63fd8eUdH_QW9HKT9_AZKxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
از پنج قولی که پنج ستاره تیم ملی اسپانیا درجام‌جهانی 2026 دادند؛ دو تاش فعلا عملی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27367" target="_blank">📅 00:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27366">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rV0uafUj4FmdgZzFJgvVOOAOZlEHKpq1IHv-_mwVJDM3AN62yr_ggsHg5VBirMqnyEIdiJ6h9URu5axKkkAHlMTfp0ckCuDC9TRRrvwP43cp0y24nYAZYqnpsd585ged8uB2tU9xr4OZUPe6iLHJilLK3_znn7RqBRBVJM6o5Cuti421A5qWS1LBaYaueqlh_iJ8OPnhVX7Khsw9CsH8pLNpalAxEEKFn65HZo99eB4DOYb-ktNB6CC3nuwAd2mSq4gFq5UKwLdyx-9SrqSTvZbIV8y4qOhJrfFS3grnelsOM4ietTmRNHwxbfqEh-zKGR_FnhqO9FevflVzw5UpFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛ درصورتی که محمدرضا آزادی مهاجم‌استقلال قراردادش رو با تیم استقلال فسخ کنه احتمال این که راهی سپاهان بشه وجود‌داره‌. ایجنتش با مدیریت‌سپاهان مذاکره کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27366" target="_blank">📅 00:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27365">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-cfVUAcfrdwzNDEKXodHcjCkpTLTZzyLq616rw_cwA3euM5zy0tsujsskurHLylFhSsSvLn0Tbm4ELtXXHxgbv7M46wKr5Es7cE6585NlIWVi5_UNHL-HNxp10WJ3A-Xs22kb_SdllurY1il4w4oN9v5DABVKGdt0pX-hOiRT6V3eA4ndDftFe09nfvO-Pmuwc85WTQ5B0v8NthoRyrv42QjNYJgH63IvwuY0sgTIWVPhg5UkMG-oga--yci6YFEhBZcFStURWxsCtwHpDM1ZolGgW86HKOOzXcdlH0ewEe-rt8V0hbtyYPNsh8QrQOYhxy8pQV36hocTcnszqy6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛ یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27365" target="_blank">📅 00:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27364">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhiIFW-scrXNUTZVpNYs3OU7vCdRX3k9TztDvFJDv6vdahmUF_dxx2tGiwnExBiNQA1Nk8SVzJa-uPgD5FhSZzMqNZR9wculDNTTXQec2CS1-htMfFRU4KOBHCtGqad4mp1HbZpMitjfe_aUXzb26Q5ar9Y_EaugQ2NDTC0pOkdt_ne6gS_SxJ7TM-Ge9jsnKS4lFRmCG8XoDdnN5CFGSmg09MOMBSpYeIPWLw6j9FFJPYOuCIFegxIDKjHFyZ8c6wrHKxKbqbiJL1jkeLG90apmbNw_UwVbAWz1Gd03ztXbIwha0mMmWzghgXbsO_5kOxsLsi980z1l4E-Uy8dZpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
مسابقه بین دوتیم استقلال
🆚
پرسپولیس در هفته پنجم رقابت‌های لیگ برتر برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27364" target="_blank">📅 00:13 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27363">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap6rONI6qB2E1DorMampU_2EpJ0Lo6xNkmCBjJa-SRX9HagD_Iu50x8xUnNBIAn89JFuBfmJ1dk9sZF5ADAAUhS9Ue7-VPi2ujcWRsvrGEpwrrDuyMkoGg0s_aIBJ-3uIEAXZJLg2F1k8DT0QFXsBnwpTTS6_Jbi3RMPovjB2ncUUYK3FLTmqIre1r7KGjSt3SD8_G6mPmkhkOeWRus_PtA3bXJgHGmFxydg7zIk3S63W7khnMyXEpMKDC88i9CNqnIuzOLKELrwFansw6obnJhzZWPMaxuxn3JRkNkRbjP509XP8f2T5i_YM8RCb4koR0YNldk_qAcjYGBfyTVtPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خورخه‌فقط پدرمسی‌نبود؛ ایجنت، مشاور، رهبر خانواده و... هم بود. موقعی‌که مسی تو رده‌های پایه "نیوولز اولد بویز" بازی می‌کرد، دکترها متوجه شدن این بچه مشکل هورمونی داره و باید درمان بشه. خورخه‌که‌از پس هزینه‌هاش برنمیومد، این هزینه رو از نیوولز و ریور پلاته…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27363" target="_blank">📅 23:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27362">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f50f562360.mp4?token=EcD5FHmnB6uO9g7PEPP08DTRuGAOmnKeu3KhbeqWvZ4BIaeh2wb1T-ozp5WcjiYCll1MncTH-k-enpa4U_FeC5BbfnKnO8zKnLtEOqPWwmAZlR-MVdhhASdIgaOH_xZ9mdwrMzh5NDtbzbvQaBpOq_7ItHVvPQ_NdFsFmxcrCbL_2IpPLuihl25v2FI4wY2yhWTb1VBQ819XiU6zWU6aD9YlKGzSDySKcQyBXZVEx8MsHWCpeCYbMhCtKp3GVKPGIJ5kLtpAU8nYNGIq_r6RD9uCrRWG8EvcPl_0JU8aZB_Pa9HeegLvHuFmOYvRJTdBc3TsSWniX0XWZu49ARUiXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f50f562360.mp4?token=EcD5FHmnB6uO9g7PEPP08DTRuGAOmnKeu3KhbeqWvZ4BIaeh2wb1T-ozp5WcjiYCll1MncTH-k-enpa4U_FeC5BbfnKnO8zKnLtEOqPWwmAZlR-MVdhhASdIgaOH_xZ9mdwrMzh5NDtbzbvQaBpOq_7ItHVvPQ_NdFsFmxcrCbL_2IpPLuihl25v2FI4wY2yhWTb1VBQ819XiU6zWU6aD9YlKGzSDySKcQyBXZVEx8MsHWCpeCYbMhCtKp3GVKPGIJ5kLtpAU8nYNGIq_r6RD9uCrRWG8EvcPl_0JU8aZB_Pa9HeegLvHuFmOYvRJTdBc3TsSWniX0XWZu49ARUiXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
هایلایتی کوتاه و خاطره انگیز از عملکرد خییره کننده الکسیس‌سانچزستاره‌شیلیایی در دوران حضور در آرسنال؛ یکی از بهترین وینگر های تاریخ و یکی از دست‌کم گرفته شده‌ترین بازیکن‌تاریخ فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27362" target="_blank">📅 23:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27361">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTMQBVuWeB4ZuWTz5izIfw2PAZMb19eMpMkni0M7-XjwUR-hk8c5zXw8_uryUfjr7sTfz7Ytr37HSQDkse5B2pYNh2Ewb9yrlJhthFD_Fv52laWanv4AIcPO8GRTggSfBzzkXyKOKtF2PMvhni11GT9NKxBBAmRjtKpdOyybdrpgMqfUEG37CAsazct6I-ZKfKZ6ADlf9a1nmgjk62tC2qD0E4-iGIxBBLP1O5mNIIfWAY8tKHNSi8q5iQ50PLrKj7bj1rWJuvPQxRxS25bkd_nvYEzVGSQPpnCne2-ZIaEGR07u2fwKIi6ZkQW_ZZFg8-W3_5HFSqX3M8wzoRjRPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه «عراق اکسترا» مدعی شده انتقال مرتضی پورعلی‌ گنجی، مدافع‌ ایرانی‌به‌باشگاه الطلبه عراق در آستانه منتفی‌شدن‌قرارگرفته است. این رسانه نوشت: دلیل اصلی این اتفاق مخالفت شدید خانواده مرتضی پورعلی‌ گنجی با اقامت و زندگی در عراق است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27361" target="_blank">📅 23:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27359">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcV-htyOevqiMZgd9AkKN6Hwc9xuuQKxxDW_jxlVNHXU9TPpgUGD0tknKg_F_rS4aOPM7KbAA4mFcyUMi4k_fu-280C4zhSjBHbdV1EZkNLxvl9BHJGTzL0ay-JyDWy1AGdMeIIYDWXRTK7wIUx9R6x2RpRmWun7dU2wCo5Ff_6fJ9Twn4Crt9GVoU3SbBdhCf8u44b-MFkPBHoq2mRUaq9LgaHAabBlrbJy3pjFrIZHzju6LIki4M4r3YH5YiVZaFsfVKmJL8FBSh9djJxhic5nJd-fJE_rrf3JtAzX5CAbtxecAKxFwbc4op_azST9PGnnUtSgC4bLrhtDtoPtgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مهدی تارتار امشب‌باردیگر به پیمان حدادی اعلام کرده اولویت اصلی او برای پست دفاع میانی دانیال ایریه. باشگاه‌نساجی هم اعلام‌کردیم که منتظر است‌که‌باشگاه پرسپولیس 120 میلیارد تومان بابت رضایت‌نامه‌دانیال‌ایری پرداخت‌کند تا این انتقال نهایی شود. فردا…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27359" target="_blank">📅 23:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27358">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzbW8LoziSkZAL4W5fH3Khk9YNus5yKsv_3N09WaHV3j_L9F2lb7cOdKCTrMo3a_R3-9dHv0ljCbf-BzKS-66ruPditAxvD-DjymepNhJnC_fH-UmKvR6vT_l8kakY-iwxC7xSwRgidDL4O5T1w0mqe2Ekv8ZsO0S7aril5PHEkrLTtWq0aXviu3jaZlnhZ7sbWuNEUiEVqd28iEAxiLXkLau8vsJKT5i-P-_wFrBTdpSEZ1y0k7Suly2QkfEF3a-DHc_6kzTtbdHvFLcmdysDmClgSBRGuRheQ0a12Nq8NdJ_G9jODKVHFxbV5dTCElkElGYR1tAbc4llJNdyrL-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔵
🇪🇸
#تکمیلی؛ پیغام فران تورس به باشگاه بارسلونا: دنبال‌جانشین باشید. من با PSG به توافق رسیدم و فصل آینده در این باشگاه خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27358" target="_blank">📅 22:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27357">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8O21eG0_JRpnlYpC436Oacg5MWg8njZSTTUgonp4vsOSSNidtvBbvnzUrybu7SnhqAaAFr2eRcqZ33VtIdk3ldtOWsZSSB1sdg1PA9Zb_a6GQAaA9kDmy0tYcogO8XUG415OAC061dZmpHe9gQwymaYO15H6A9fQZoeLnbrN2M3xPejd6ULAzYBC2e-31JaXIfQbkGUA-FAeTOhJPAX4iX2P55shszf8y8Csl9FkZL9-OQesycgqk3JNmamVmhHr5ecqM9LBtbfcJwsh9UIXtYSCnKBkeeFgsM2u2A04li8qzifi_x0TBssLFwNn6PfKRf98ngtfTRiMJyFYPGKvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار دوستانه امشب؛
توفف شیاطین سرخ مقابل شاگردان‌لوئیزانریکه و برتری رئال مادرید در شب گلزنی ستاره جوان و تازه وارد کهکشانی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27357" target="_blank">📅 22:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27355">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Df9g7YMp4XcXTVqm7cASqvnOLgPpfnwQKrRHREIClcVseH_SeJFQ33UQiF_gPMIIKsRsf4PfYUb-FVGJQCVUTTUDGz2SccudPhypkdv7GD8KPZoQv0qbb4N3mRs7tb50KAdqW_-3aFn0Q_DHX8F_rFIWTzeIzJApDF-YWp79AmfEWVl6hXyzPkgQZFwtOjqkjAVD3-AJTY2mpNN8OebIOlSjvEeFqkL42p7lp5Bal_SYM5etMckHX4UPNtgNh14fcj2id9jgp7GirWPwUBlxPnDblgscpvsCmkXrt6D1Bqg72qaC5esR5i-Aw8INl9Dtk5O9tlxnCCAJMtDZPDfvXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgO8gM236y7hKXU7g-d_VZQY3kYFFuTyhuxa3udaK9K68_cF8jdzgBkjesZn-zW3SaFc3ryV5eMNacN_7Em3lJfdxZpN3gbM3ka_zfS7lvIXiphabDxk2NgA1a9qwZRBRGr63afmHOc69wm70_dqH4A8NT-359e0w9phZpkyNixXUkj7m46YsmAcSkxb3NWs241dG4YCRXCNEeSO04Y2MHw_OykBr9BwsgzC74-VCjGYzDLfKLmAX3zKwAvVh7trlHVAOUW9K_bqVC-H703RKcX9mtcyx26OGAneDF3uSqPK8jCewN1yyJEZc08Chne5jhP2x3RGzz5Ykh0ed7KrMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
دو ویدیو زیبا از فوق ستاره‌های تیم ملی والیبال بانوان ترکیه با کاپیتانی و رهبری زهرا گونش که اخیر قهرمان لیگ ملت‌ها هم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27355" target="_blank">📅 22:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27354">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYU_RovxaqKiBzZAf3rXqviNI_2Rok_o_I-ySPmWc3VHYpxlyaPMIeY3rtdrJRpruJnKom0HZL-IqvlUPAaHz8JXUqow0gHyaytyFvw1l8f3gSlRZkhTqSEketvWA0177Qs2RZPxJc4fgU4-cWruaQ8SQOYnySVVYsqh8mAjS34prejFB-OXJ9XDqI1qpwfphCagVWK37zkodco-yjMQ-T4QRdEUtmNSDcdJrv8wwULVsxAOIchx50mKvjAwjSVCIgJmtmKeT1D0SmUgBLPUWuA1MfH00FXGT9Ja8fSPRzTIOwb5fRJ-2wC1ypDIAoIMc7jxZiuffZAEZnRoeKYk4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
بعدِ توافق با مدیریت برای تمدید قراردادش؛ جلال‌ الدین‌ ماشاریپوف‌ از امروز به تمرینات‌ آبی‌‌ها اضافه شد. ماشاریپوف به باشگاه گفته تا تکلیف رضاییان مشخص نشود شماره 10 نمیپوشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27354" target="_blank">📅 21:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27353">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24f51b1028.mp4?token=kyoOnec1P6ccs-5qjA1MnwhNNKrXfoE645gmd1OA-UVdMJ9z4URpqLShLy0g0-wxDQesIlXE82H719cGqLFC7ZuQjigX6lqtbNaGeHseewIjG6NddUsu6RWpqKg3yUCtQfVzlwyHUm9KOPATQ7pK5okhu9wD_P2pZDLCBAJA6qQGcJkgIofyjo201koz49t_PVH7Vqz7IdJHWZJ4V28KCJEMB6mdWGqPsvFZeoIpsNVPwZjD9Rw_97jdNBnU93smlSU4vyeQ1hZ_hzMQ3ZEFcRUXk-p28iN7PFp_nA6XTrW00gM2uSdZ2hkQgxzp6HNMItQ_RHuUk4Bywoq5y7q8nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24f51b1028.mp4?token=kyoOnec1P6ccs-5qjA1MnwhNNKrXfoE645gmd1OA-UVdMJ9z4URpqLShLy0g0-wxDQesIlXE82H719cGqLFC7ZuQjigX6lqtbNaGeHseewIjG6NddUsu6RWpqKg3yUCtQfVzlwyHUm9KOPATQ7pK5okhu9wD_P2pZDLCBAJA6qQGcJkgIofyjo201koz49t_PVH7Vqz7IdJHWZJ4V28KCJEMB6mdWGqPsvFZeoIpsNVPwZjD9Rw_97jdNBnU93smlSU4vyeQ1hZ_hzMQ3ZEFcRUXk-p28iN7PFp_nA6XTrW00gM2uSdZ2hkQgxzp6HNMItQ_RHuUk4Bywoq5y7q8nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گلزنی دنیس درگاهی دربازی‌امشب استاندارد لیژ مقابل  سرکل‌بروخه درسوپرلیگ بلژیک؛ قلعه نویی تو جام جهانی 2026 میخ کوبش کرده بود رو نیمکت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27353" target="_blank">📅 21:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27352">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZ4MTxxR5OAAG-bniiuRcWKVoV9ZRIejvmoFGuJAfDh9i0FAFCatwrbIYMiic6GvB-w_ox9vIb-SGmFkjzO3QJvBb66psKEGBmE_ta4NpjJxRIO8uESo3G64RYZ1_han9WAVxxpCIm1-rDdJCrk8dowv8K2QY8C6AOniew5jfRRHxRVtyi1HQC-VI3XN9wljCZdOpXdsTSA-HNM0j-LyblTUjfK4OO2AUuEA2v2nsR_rm8uApv5VZ4ByRMPgOqwb_6eKoRPhXY0WbXGOwxXtAcQFJprn54NjO1CwFVWG-aG5ueo6svGU7nmpK4Gssrv_KBSk8F7AMo1hXHe6KTb9Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تراکتوری‌ها با پیروزی 2 بر 1 مقابل شمس آذر در دیداری دوستانه به استقبال لیگ برتر رفتند. شاگردان ربیعی در هفته اول به مصاف پیکان خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27352" target="_blank">📅 21:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27351">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6gWHVo2XVcocfQiJLMbgztg6FW13INxaC49hGDCYkNDuleKFVxemDJYFbT24JRIPX4KfMnMr0cZWS4YnpINs9ORmGE-fzlu6LwNIccBAGvGcRsX6n96X_6YCemgp1DMCJyPKM2CnjUaYI8xb1NcDYQPmPWiJnlnboOsv3S2ktlN_qoVVVAfFZ9iRMcKNEB6PibuVfsgORBXyCDCQ45aFc2-6u6dX866Ij0ZaL9_HWimCAlMB51BdxwXHs_NJu25xDn2Gs_xt1GUMfa0D0b2WH5m0YUsp4UbDQjHkpM_edz8JVL6NAHMEgn3PZ7wPqHFbNVpMz_isFG5sKIjyIH79g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
بعد از جذب کوروش اژدهاکش؛ امیرحسین طاهری مدافع‌ میانی22ساله فصل قبل نیرو زمینی که عملکرد درخشانی داشت در لیگ یک برای قراردادی 4 ساله بامدیریت تیم پرسپولیس به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27351" target="_blank">📅 21:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27350">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24945e30c7.mp4?token=DHaqdJIHpfBJFWUjV4zAajiDcNhJqLjIkjY3JhY3b1JZqbfTwQ3HArMsQJ1h96J4j3FNvqgWIIMQn8Pq69i2-d-r-w93YPyaWoVyC8Ad686DWcR4-Qc9yFQ27hwxy6wc5JvAnT-bNXQyUHdYotCLEcU53Ju1DNoLGtj3TLQzLcohxOq-Pzc3d8wcsdMQJKArwtBjtiprl3FM5qNBhWweyl6CeBprYaTP-a_peq-JNSmuQOp8D0-xzXD07XqqKEElm7MIXbAtiOinGxHSqqootu7tq5Qk6_8Ao2RNoV9jK8srga9IhUfmtlRpxXMz5hYpACiaqDkbytf7XSqv3Vp13A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24945e30c7.mp4?token=DHaqdJIHpfBJFWUjV4zAajiDcNhJqLjIkjY3JhY3b1JZqbfTwQ3HArMsQJ1h96J4j3FNvqgWIIMQn8Pq69i2-d-r-w93YPyaWoVyC8Ad686DWcR4-Qc9yFQ27hwxy6wc5JvAnT-bNXQyUHdYotCLEcU53Ju1DNoLGtj3TLQzLcohxOq-Pzc3d8wcsdMQJKArwtBjtiprl3FM5qNBhWweyl6CeBprYaTP-a_peq-JNSmuQOp8D0-xzXD07XqqKEElm7MIXbAtiOinGxHSqqootu7tq5Qk6_8Ao2RNoV9jK8srga9IhUfmtlRpxXMz5hYpACiaqDkbytf7XSqv3Vp13A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
🇪🇸
🇦🇷
ویدیویی‌زیبا که فن پیج‌های باشگاه رئال مادرید به مناسبت فوت پدر لیونل مسی ساخته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27350" target="_blank">📅 21:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27349">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbe423c6dd.mp4?token=QPE9kvLYHCmNX6iwQvyu5hjOCn-JyGo29c0H-3nzB3Q38Eqh4gjvE_uMA-YqnWUiRkZtMYXXJVwHf-0uNwSU_6nFRXQOpylac5r_LaSjPVax_cQPW2ZebPOTyJ5FOT0LlIYuIrY28aQiEm0VHdkKGqLIngCLqIdepovrvNds7y_8gQDWnmSvvrs90hcMP6YUB_fT8aUEKm7KTTf0nlxac_BeGkvo5RKiRhX7W4dHmbHacp0GvEyIYglcNgHpLsAwHG8kLN9rv17xqPnlfTg6Xr0DG1xYltIEvTX_XrF2ngo1bq1zPj1ZqcqtpAjjvSH08E0lOOdUfJBnOFNwKVHZDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbe423c6dd.mp4?token=QPE9kvLYHCmNX6iwQvyu5hjOCn-JyGo29c0H-3nzB3Q38Eqh4gjvE_uMA-YqnWUiRkZtMYXXJVwHf-0uNwSU_6nFRXQOpylac5r_LaSjPVax_cQPW2ZebPOTyJ5FOT0LlIYuIrY28aQiEm0VHdkKGqLIngCLqIdepovrvNds7y_8gQDWnmSvvrs90hcMP6YUB_fT8aUEKm7KTTf0nlxac_BeGkvo5RKiRhX7W4dHmbHacp0GvEyIYglcNgHpLsAwHG8kLN9rv17xqPnlfTg6Xr0DG1xYltIEvTX_XrF2ngo1bq1zPj1ZqcqtpAjjvSH08E0lOOdUfJBnOFNwKVHZDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
واکنس ابوطالب به صحبت‌های اخیر مجری‌ های صداوسیما درباره آناهیتا درگاهی عمه دنیس اکرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27349" target="_blank">📅 21:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27348">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTCdEtPgLjU09kNQ5nEt1rvnEQqxX3eFyOJtA33Q4mZ04zoKaeh3pTLo7xKtSUbHuE7sp_eHn3jBEYPETkYbccSlYWpzdATTOnzvNjcGVBDQdoT5z_sS3ab4Eo-1btzkdm4yCzs7aJB2CQhoPsy_6MnzFgnFPdQESazhpY55_llTfTojkZJ6hlmch9Ivn_aL72D0-PY81qstV-BEqg6eDcduig6Dzrxii1NOD59x1FeACOqg6_fcbrw6tJ205BCw2IdT9uziqw-Bsb7T2OiaBznIuB5pjdt_IEHayVqUpchrQW3ZdA05j-qhphPax_4Q4hqyxkFFxVygcqvuTKttRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27348" target="_blank">📅 20:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27347">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQzgWcYzGO90JNdRk64U4O2GPjq8-22mE2D3AaMUBP6khp8Ej1sYKCN3zQpMyZtGie683_-_6zXjM8C0f1A5zWPCgd2vZSXsOHH8kKlN9SQP7tu_6D5ibboy26X_ciFzozqnEwziQYE_wECsviPknFGiEkZylyFwYogqJjkwx87jkx9SHsacwviB6_XBvpQmaywsPeaskP-5FMWZAtCT6mS5rJq9l5A2o7CML1AnzpO7d87xf7n7TgDWeVLEI00Hv5BGTR4DkMwStBIR05R_q50N6MTtY_VYD8gUBDhRG0vqnVKuUuze3-W2Fl7KLNlx5AKUL90pS2s4itmOtHLjxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌پرسپولیس برای‌ جذب کوروش اژدهاکش مهاجم 18 ساله آلومینیوم اراک 150 هزار دلار بابت رضایت نامه او پرداخت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27347" target="_blank">📅 20:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27346">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAMrgVkqGxKYQOcS5w2r70tXLj6Z4BcA07JNw42UWxiM-43jIjcp1NpyNJAN38Vjk6m2czrPJksMT2lAx8PSx8enUaKCQKHVz_4ll_4wsEhNSTcNWZegGjANS3FmiikzTylCLoiUfpybSCmhewo-HPrZ_uxkq-82fpmY7HooyXQpZqbX1Io5KGD-rhqRSQT1i4xUUgsELvwg7DeUxtAQTFWL1YhsQD6vKJBor0dw2dwFlN7lzPrTl_PMZakoR6mcrNUiltgyEsJe1c09YbdGw4RjEC8soiesZiviODmtr3G_Vmh1WS4T10v8SbEMBhs5NFag9vm6me6GcMkED_NQRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در فاصله دوازدهم روز تا آغاز لیگ برتر؛ تراکتور امروز در دیداری‌دوستانه بمصاف مسی‌های شهر بابک رفت و به زحمت دو بر یک این تیم تازه لیگ برتری رو شکست داد. شهریار مغانلو و هادی حبیبی نژاد دو گل پر شور هارو به ثمر رسوندند. هیچ تیمی در این فصل بردنش راحت نیست…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27346" target="_blank">📅 20:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27345">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_j0ybBYL6Ie3c3WTK1qxqglscNHQhBGBiMmgF9AoqhOFymrRoBzSZoW17cTEXxAHRxfwWKhyH1PEecUuPMvuiQcRR6jyjHpF25lVpPX24PcTZcI8AaLLJ-WPFge4n6vPAkaone4mgaHWpE7_XFYkMujQplWaMAJVLp2VeWZz4uv2E70rikP28lGGqZ9iQR1__uHHwjNuLP-q2OhMtwgLjENatXHhpj0gvkd6AeGVs3yYo4qUJOegFbONTrgiuA3naj6RLO-jQZ2ofdX5VzEFato11U2Px5dMstInw_4p7deixhgiAbR5_3Kh4VUCUCE9xn_dS8CiRmLemzaL89lJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◼️
#تکمیلی؛ خورخه مسی پدر لئو مسی که همچین اسطوره‌ای رو بزرگ کرد مدت‌زیادی‌بود که با بیماری دست و پنجه نرم میکرد و دربیمارستان بستری بود. دلیل اشک‌های لئو بعد از گلزنی به الجزایر تو اولین بازی آرژانتین در جام جهانیم همین بود. در نهایت، خورخه صبح امروز تو یه…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27345" target="_blank">📅 20:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27344">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWfx4obWyaMyshEqmr_rLINKGCWlVMSo6A3l5aTEEdljRjqQnxGT_G3l5duo3zvPPv95pAWVKvHgqWLGumCceCBImRlvO_saJiRhaYfH0V5EDqRwlCr9iVlmi715WXMCFFtGFoInjClOrE3Mukbt1cPkoE_Nkfo69dGDoex1FXwhCD88v4Vo8a6YRF_d3KEuNRVFMYZkutDm-QsVlPVuXnp9RH0ii-xyI7UwhPnT1U0dHe9nYe4iS_VM3GBFcKLsJgdLY97F_9jwDUcLAqY5Lb1-vdqmkATGbaE07XSFbpvWd-8FDgUn3pJFGsxGZGTFmg6Uk8YmGxeTLdoq5k56fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
رضاشکاری مهاجم‌سابق‌سپاهان و پرسپولیس برای‌ عقد قراردادی یک‌ساله با باشگاه پیکان به توافق رسیده و به احتمال فراوان راهی این‌تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27344" target="_blank">📅 19:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27343">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APMMfWBYbcqSz-lisGqRVxtKBcmoi7FqEqsjhYGSCEGhS-1iL7fUXtvX3eAML3-5n-KPl6H67WLbd5_apa23SMM_KUKKTluYkFxoYoXtgUJo3UwSkLmMpxohHE4PxdtdwwZOw32NGJemdBuRPs94964qnLswGc6gvMWqmtCZYe0uxsxSL7vVNxdc5FAThY4r_XfozLreXIAGcQG6KTg-vOd3oPyoGx7eMgEe4XSrN62d-vTqWNag68VsfWWQqNMq5x0QCbf5Urj9rJVM4sENHuMH-hkBPs4p58VTw2n_P7qY1Y6d_oyOju4OEb0VcjpJGI8KLiNJVWB6V603J57L4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
طبق اخبار دریافتی پرشیانا؛ محمد جواد حسین نژاد ستاره 22 ساله ماخاچ قلعه علاوه بر آفر از سوی سرخابی‌های پایتخت؛ از دو لیگ پرتغال و لهستان نیز آفررسمی دریافت‌کرده. یکی‌ازشروط مهم حسین نژاد برای پاسخ‌دادن به آفرباشگاه‌های‌خارجی اینه که رقم رضایت نامه او بیشتر…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27343" target="_blank">📅 19:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27342">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehL7H7UbWy_EOjeeLnSaiZq5maIXLN3h-hdLkfRTFB-pHitWffOm71PeKyxJu-2ozDeirZiK48lqIamxm7p8RfrFNFwswZZbJdk7QwgxwUaJJbLGucdq86rR3nadLjLYyisnhkLa9276zEIMRd-SFJHcH5WS3e-Sj1ktaz8yhBufGao7VmpAGUzFn09CIHoVxMIiDLmzHbS32waYt58LsuRGVzPwt2F9-UlQyea6ShMCYC2rqEbjsrsd_5KhDgI7eMWr1FNBJFcgi9vTfvPzyjJIaFxBlLbh_lzsivQRKgMcHFNRBRr4As8fMMWca7f88teOVXLl9xo43Nn9sndx_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌سازمان‌لیگ؛ دوتیم استقلال و پرسپولیس فصل جدید رو هم در قلعه حسن خان شروع خواهند کرد و فعلا تا هفته ششم هیچ خبری از آزادی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27342" target="_blank">📅 19:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27341">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDG0QRbytL3UFBcc5o9oCSgCdxAQKkkXcrKEHniKVzSXAzVeoKbgFRqXQNYA3ahR3I4534bkt4Mff2JAu5ITy41YV1a1sDThOz6OoFkST5pVrDQ9iDtGPVRiQuE0k9laHvH49HB9tg9dGJpfSHcgsdQrdzdvLfP-2SAFjw0enxaFA8NnaR_kGFIeqwE7OabtFIl56CKXuGbLWdIH_ulrQ-1_QKeAetzcYO0ywCzw0I64eVUaGU2bzZxou7cmD6TJmPbiPxEHFmhI3z2fL9eTjF-xY9yVkXWvOIJJXToF9EXyqCLFjgu2qCUhYaR8DrH7DPdDqHP0JXRP8caWN2c8tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
باشگاه رئال مادرید دربیانیه‌ای درگذشت پدر لیونل مسی فوق ستاره آرژانتینی رو تسلیت گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27341" target="_blank">📅 19:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27340">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrZXMsk2GOg8y4Xa3SB3r0KlZAIgt8dKpHXRhtz0LSKEQjiMpA-KfHR8k1oOzvaTwj6y39cVB7qYeqdQbBzm3c0E-LkSMSBLey3PFSKUowKBimibEvoy8MANRGNs_obs_xUYNe0NrY3WpQZ_TlDytaFNnYqlnyX55rwQLdNhINU1hdM2SeTU5E2xc6UbT_V63ILTKa8zK-Prtvnrih_A4DiFi1djIdjp1KqOLBcsdGmi2G6SsC0o3Y0f-zWcHShaZ5rDb3ivIhq165s3ZpUyhPCWJoNFaXalTVNEz22u4s2csYr5eNtfZqFAF7DVwTXpfyIaouvOnarDtiql9nYNHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◼️
#تکمیلی؛ خورخه مسی پدر لئو مسی که همچین اسطوره‌ای رو بزرگ کرد مدت‌زیادی‌بود که با بیماری دست و پنجه نرم میکرد و دربیمارستان بستری بود. دلیل اشک‌های لئو بعد از گلزنی به الجزایر تو اولین بازی آرژانتین در جام جهانیم همین بود. در نهایت، خورخه صبح امروز تو یه…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/27340" target="_blank">📅 18:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27338">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIB3i_HE7SQ4Z0jK5wXU0vQzj1WmU_BlSuyKrSv92eBNcZT_2NJ3EVcODojN94iA_ELWAf2tZ5P8s_V6_0I4n12jp39DN5wIA5CgXCCKD9vTf_0IDBQ4-WbLkq3Yo0jE2Clru34j7nrsYZP_UVgc9Bhbe69fkxtYpDpGioYd7YpQ-aQgH018ugvboUr7p_UB_DUA9QyULEz6RdfNZIOGKdOJyGwEPkpLY7Z_Nb4VTPjWRz_e3PX8qVFwTg3V1JfsxnbEkAQws50Ao6cS0Pq5rgOKTSp_3jkOLlNPH4Rx4PlAyd4oHaiX2f9BhJUkDWXZgfgTfg7eCqd3bg5fKILpGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
وزینیا دروازه‌بان‌کیپ‌ورد درباره‌پیشنهادات متعدد باشگاهی بعداز عملکردش در جام جهانی: من میخوام جایی برم که منو واقعا برای ترکیب تیم و مسائل فنی بخوان. نه فقط برای مسائل رسانه‌ای و تبلیغاتی چون الان یه پیج دارم که 30 میلیون فالور واقعی داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/27338" target="_blank">📅 18:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27336">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca7c42226.mp4?token=B04wZ0XII6CMI8i_t1AC_3Vsqcwgu84dhyugQttc_Y-x2x3PBtMFE_tSn38IiJ52eWi6MFwjvSbVVx-9WPWjFSqO4QuW-g5oa4gW9gXIqGHfAzokvERptjkML7ljNAPYXP41hxKDKan1mrBE_cQ3iqchVuw_aMkFque8xOPiy7Ba8igrSU-F7WjeMB_Mnf1lxe9MnNsmnZaWpDP1LvmKisNrJnFmueTRV74857fGZWeS9etAMaDpTwXTmMkO2MteAy_9eZPd4XYraiKy_tewVAJhvJ_D1UvT55kJKS8qR7HrI8tO8TP6U4BD_wfeEOO3S0_N98tx1SzZznJ-pa50ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca7c42226.mp4?token=B04wZ0XII6CMI8i_t1AC_3Vsqcwgu84dhyugQttc_Y-x2x3PBtMFE_tSn38IiJ52eWi6MFwjvSbVVx-9WPWjFSqO4QuW-g5oa4gW9gXIqGHfAzokvERptjkML7ljNAPYXP41hxKDKan1mrBE_cQ3iqchVuw_aMkFque8xOPiy7Ba8igrSU-F7WjeMB_Mnf1lxe9MnNsmnZaWpDP1LvmKisNrJnFmueTRV74857fGZWeS9etAMaDpTwXTmMkO2MteAy_9eZPd4XYraiKy_tewVAJhvJ_D1UvT55kJKS8qR7HrI8tO8TP6U4BD_wfeEOO3S0_N98tx1SzZznJ-pa50ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مرگ درپخش‌زنده‌ی تیک‌تاک؛
یک تیک تاکر وقتی داشت لایو برگزار میکرد داخل‌مخزن آب پرید و چون فضای‌کافی‌برای‌چرخیدن‌وجود نداشت تو پخش زنده غرق شد و خیلی مفت جونش رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27336" target="_blank">📅 18:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27335">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbV4H0axGqGPv5vw-Gl7FR0fRy3JC7e7nYt8FOrwU2Xys1m1mWYmoIuELl4FyDQqkrGCZelNMHiJdjK_h212KtxvW2oSVghz3uVoO5ivfqYzZLi7fyUab2pcV5cco_aynZDATCmJNONrefQsXO4jhIk333hF8Td3EFzOTZ_TpuemLvkG32gD0DSu-leoVXQyEERpp4vQrrIByGbGC1ua8hm4rgPy2JEwfps5GWNjXzSZ3jBKgoQS_Isqe1Do3ViM5KvS4b-9MZt4ltGdJd1x-EoEjv-H_eKTCqDoxBOd-bjuQH2QLC0Sd3cx8Kse7GhYCfjXb4VgN5ieV0Fk2UIH1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون‌فوتبال آفریقای‌جنوبی در روزهای اخیر با پیتسو موسیمانه سرمربی‌سابق‌تیم استقلال در حال مذاکره است تادرصورت توافق قراردادی چهارساله تا پایان جام جهانی 2030 با این سرمربی امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/27335" target="_blank">📅 18:28 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27334">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9v0CLMkmEcH8MxQcRDmLb6FYhWxZGQpmG-dDJOHmbYFfDFM795ar9CppTlFWDDdaEL_4iS7mehuTDGI1whX324qP3lmMraeQa57OOaz6JJ8J5qeBYaYSO21vLA6aUsIRufMkBzkGsmrLP9VKTwDGwePYW_V3KqXoGc65mW2qLy1bthBr4WVS7g-u-h_hXIanscv2T2uFd-Zz44SGMSdSB3mlhxC2kdj-T9YCfqiT8V5cGjSMujRNb17EnI0IXxH3jDomMUpiZaOSY8U77brIPNdBvLzDtqqElM4vVfNHwWXfhD_hqx0_KihF5zLSuGOhZjo3wSQuDmk5JjIDcdbPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔴
🇺🇾
با اعلام رومانو؛ لیورپول خیلی شیک و بی سروصدا رونالد آرائوخو مدافع 27 ساله بارسا رو باعقدقراردادی‌قرضی‌تاپایان فصل به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/27334" target="_blank">📅 18:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27333">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IU-IEInOH0xrvrzpJOmOt37ScO977Im28NH2g-5y9fTguUSrpDkKGX53JqqEkkWIgacHn-jKmdEB7qZBWIuPwaygZNYWahRplJWYWc8yfI2uAWstkQeHo5rMo8przAomR30xkElSIJ-HO4jSIFd4FExkkJdYVvbfaxfakUncSE4tbZA8t1jIgw4TCKNmfldDjc5qNhVE4Urie_v8UXTqQwfe--dtuVzQ0HFyEwdD2rrY4FMAjzXB8JgpYmmQsq9zRAE8UL1PGruMy2rpe91rDlyLZBfkY-vk_Uln3gz2p7PHhSAmtGUdWt_AF27ZY8PMrXT3OhYRcgOxy_nYHd9SxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌ امروز؛ از مصاف روسونری با آبی‌ های لندن دراندونزی تاتقابل دوستانه یونایتد و PSG
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27333" target="_blank">📅 17:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27332">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZXP4imYwz-Q9lU58ha2543TTemeliTs1XdoeSqz3QYC0CSdyTUZ0cyc46wIQpPJRTV4NDWHUnCNiTQZZprAM9RZ-FBdxWzm9naldrYI50EQDilwEBZE8p_ydl--M_wHMOGQlNTotfqAtGv94RDDeB17F9kaztjP_J1jVhl_pfFmsvPrJGCD7GFhW1w8m0odjLUqAAb18JCEqMElJQGLPXwpGQy4q-9Jt1KGtrETmugOi9FAi39KVvMUl1Cv5pEaV6eLKGtNdcno_lf8KWz3Uqb0VEUOTH0OdYPk94DK6FbhVBDqbYLrYkctpLZXb4JytmI9pmIalk8KzrWZXwG0Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◼️
#تکمیلی؛ خورخه مسی پدر لئو مسی که همچین اسطوره‌ای رو بزرگ کرد مدت‌زیادی‌بود که با بیماری دست و پنجه نرم میکرد و دربیمارستان بستری بود. دلیل اشک‌های لئو بعد از گلزنی به الجزایر تو اولین بازی آرژانتین در جام جهانیم همین بود. در نهایت، خورخه صبح امروز تو یه…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27332" target="_blank">📅 17:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27331">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnFnRhove-Rpne2GTUqbdgU0TR2uXDhNMrlOYhe67SF9sy27_7plpscsZO0TdkggXFf2-mBc5VfWcVLUC1zUAADdcirFgjzKuLaHj1GifwafNhKN3fXD7753-wQcNwNsk_dW23jvBbgGqXy1TLRfiQgE5LxoBrN8RFJmYptm3kOaLvXemidZF_K2WZLQCLjHSRiKCDuhUVz4UDxD3fqFbF8MRfooPVwM6V_rO2IM50aRVXxgUg0uO-HKlkUp6Wzi_MJOsuxzt07ocbwJ84EIZfwbA3eppo8SPWNvcEIiBtcCyApkjb9L61t9vUxWDqTo3CilGXhno3zaIebnv0IULg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوباشگاه‌استقلال و آلومینیوم برای‌حضور قرضی شش ماهه محمد خلیفه در آلومینیوم اراک با توجه به بسته‌ بودن‌ پنجره‌ آبی‌ها به‌توافق‌ رسیدند. درصورتیکه تا روز سه‌ شنبه پیش‌رو پنجره باز نشود خلیفه تا نیم فصل راهی ایرالکو میشود. سه شنبه آخرین فرصت باشگاه استقلال…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27331" target="_blank">📅 17:16 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27330">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XK8nmZgScBtshO4uxoVYcqao-G43IHZQN1ERp0KOxED4r2eiDc2Xj9irczehM7Tsm27QRd4tBGsZVSGSnuiBcAgeiFI5Qs9nyagLbT55SJ1U5FoI1YCV_LKF_7rx-h8OwP3hjrj6iN08h7H8neQACa7RUaT3c6MnZUyTlKvgsfm3yhaHJNFMS7PC2VkQqE45c3vgsx2TZfJz2BXi5xAfv6f8Zdyo8QOu94cW8GfccduZCG-12XVIvbYHg_oNZNQmLaTGFia11Rikr-PRf2fVOqDMABxacdS4xR08Xgs-TbvGIfc6HJ1XAGhIEmm7KVQ_oKvFZsckEZhovJuRUaNZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیورونمایی‌تیم‌پانایتولیکوس یونان از موسی جنپو وینگر جدید خود؛ طبق گفته رسانه‌های یونانی قرارداد جنپو دو ساله و به ارزش 800 هزار دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27330" target="_blank">📅 16:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27329">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATFsK-JuW7y8J_qo70eSen-710oTEx4anM9Bv-a78D4Xu8qe3I7PY3WJ2ep1soadtCNiM9QxLvlRTToTHNsOh6I8qYQRGFIMwZDhhTxkPCsm4lRbB7ACHuN4StdOU1DjgW51eb9HPNLkJ05OGrn5pjUroLMBYfypbGae2rlfeZDpM5TqmUfMEX-h3_NAvfivgBZNL8iacb8vmlFm07r5FAFShIjE9z0Wbi2YR9iLHjkDTY7n_AUjQ6UXdDJFnwQPbbzuKjo9siJLBIXwGGa4KfIvw0vWiGQFr-V-LW3oiussckR3ZVn0Ro6JgG1B7dOWrSwmajQ11UKlEXwOFUxkPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔥
فقط و فقط ۱۱ روز تا شروع بهترین لیگ دنیا و رقابت‌جذاب تارتتا و سهرابیولا مونده؛ برنامه دیدارهای هفته اول رقابتای لیگ برتر خلیج فارس!
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27329" target="_blank">📅 15:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27328">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDBbCG23b0rNpzWXfDPVqnzkdXknnAGGu2aEyFpWF6gsnAuCTZ21BMgDzx1fkhlLO3rUYj2W9HI6Rw0l-GGqH1XeVLge-chGx9IaV-b67sFVBevCXrlfxIDtYopqkxg5zqMY9VmUn_zUYh1x3PPlfjStNKqss8dv9umnzHnQPN2WLK7y96QSaXllshy2KT2Pef_LJalJqywyOgbYusMaf3yDkKP0n9lT4ve_MWy9oFUT6ihiXI5ePZNwFzWEMhSOWbVITWz_gLnINeslmXRHxWwy63kV-ByhcnJkiTxIDYH7NKXv2Ks3tp5G9F19FCGrS2sGTEqmaFbrXevH6amXdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پیغام باشگاه بارسلونا به سران پاری‌سن ژرمن: فران تورس رومیخواید؟حله 55 میلیون یورو بدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27328" target="_blank">📅 15:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27327">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C50Ff2Kt35-TNYgKohY4tXI_J5CIzpy-NWeGDcYN54bwAhcq6yw91HTsfCFKNeJJM-mkQLDO9T5QbZew1l8dRH1mUsxQAZGDEqGx5X_abeAL6iJcDfJjTKOjGVKXJ1ha4AzcAYTh8iivhjmQR4RsB3fp0f7Bta8o33Ec7rQnA7k1UrXBbFaq5N_4niUtU-XhkITMyRaOHESxWmxRYbW19-8HxxWp2aZ6M-OiCv2IRhIrlb7mVZeqlADakRh9ZqoWNP2lkOKhysvaswKIE7SEqfi92Ukz0gXh1BEjnZQMGMJPZrZe9qqPT654W2mProA5AUmok1pj2WLd48TXOxDCJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ سران‌بارسا قصد دارند بعداز نهایی کردن‌قرارداد رودری برای‌جذب‌کریستین‌رومرو مدافع میانی 28 ساله تاتنهام و تیم‌ملی آرژانتین اقدام کنند. رومرو برای پیوستن به بارسا چراغ سبز نشون داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27327" target="_blank">📅 15:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27326">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNbjYIzfisD1AbtzywU2i5SEybSMBLPvQZ_A6Eal1NGudHdn-v0Y9S3Kzk7i5Ni5A4YplCCGtWHdTQ5k4qiAHjaSW4uTe7pc4-XavK5dEEj8lH-_WNUHwIY2koH_TNoVzIiYbt7fWnkdmRiYtWMVtZh0oMHOZ2O1ut52mT8ZJTUV6DmHV0SM2cfOwUsibXrQ_UlkPJRCr-FPpBLDvn8hIQJmTDSA_0ZDV-t3qRFx8EYg2fYjszHfTxi0L3S6oauKcONuJq2VD2g4ZxZxJVKR9N-EJMTQim6_yWyi2Zz41GjFTR__Hmc3T1ab-9mXJqtpJ7Fb3bEiSb8dEOXBdUAb3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27326" target="_blank">📅 15:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27325">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsamqxMbKOsPGqITmO7MuNOnYddvVJVGPzebZwGrsjitDR3t1WRxUj8zE93WdzgTrhqtX7wfaSA8HD0LjCkMlZMrnY4YmXBfRHLK0ZUDTB8aL99E5hVHkA6jyETAoZqF90p4rnjKdxnwbev07g5AK0hkvE7gIOF7JgFIFwdTCPGYNkoCTrnrEe_kjZWb1EQhRzVY57yZJrgAhCHgF1C7Zv2ccJbISJu9-6k6_pxYpkhULuofwtfDZRexMH34CWZwriTn4gV4YAO5bYjNcJNs9upmZ5pgD2CT3sF0XwTOiLmbuCybDKWZwgervJYo1y9mRh5GcNAfP1MFBGNWF2lsQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#تکمیلی؛ هفته آینده مراسم عروسی کریس رونالدوعه که اتفاقا لیونل مسی هم دعوت شده بود. حالا با توجه به این ضایعه بسیار تلخ باید ببینیم لئو مسی دراین مراسم حاضرمیشود یاخیر. البته ممکنه که کریس رونالدو مراسم عروسی رو عقب بندازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27325" target="_blank">📅 14:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27323">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U6yjVBwDas9Yl5s8c-tgCMyilHVqB64dgEUSWVvPiugGPolVuk2A-oLJV0GgCAwdoR3YWSnEiD5oaKPkXrSRuWLqgmjxYyezDpQeJHgefdnJwZjGeNsCREJU_BvKvolLK370e_1tpLOSq_BhsPvRtZu_MVTQ7ab1HExM6KZm_hhRTIV4DUhMfCxoxduuh5YoKv0pOxv2Dr8mzoxKQFOQEdiy00PURyYROuRJXS0wZIyJJMAzQ6qIKascmhTSxz9sfVs9ZkYhf0gQP-I45rn3zj-iu4teuP2ivH_EbD3I_JyfLkvWy4C0Ya4Dz200e68Hs7-ezfHex-Q-dwSFEfbrrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NRqhOsYA_uvYlH6eXQKCiXStBQqMSM_G0osWr9vcAOus8IZe7LoLyErc3qpWDWCilnIsnXzPUhdrANBplDqkE0coiOKxXTE5r2q7oDLh6D_aY7PMBNzCa72Y99uCVBwvrBSz5NPTbssqlklyK78gRJqfuhY1UcXkod_VV6HlGjCVlTvZlV3F246Ng1-P1zS3gP0T5aWzaF7aS0xsXT0oqfIXBzOKIHRFTWdvMVzHNO4GuyM4rTfX-WynWTkLanizO30hmE8rOq5tYRiCQhI_ObiFcGBhl7dJuNiAMLu2dRiV-y3P7EOAX5l74tABWe7di8YS6b1OgLPCUvKlsWpAmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚫️
🔴
🇧🇷
رومانو هم تایید کرد؛ باشگاه آرسنال 75 میلیون پوند به باشگاه‌نیوکاسل پرداخت کرد و برونو گیمارش ستاره برزیلی کلاغ ها رو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27323" target="_blank">📅 14:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27322">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qI9ENzlPE2OvLBoM42FDEhgmcKF_GFHLHbm8I5D0pNDCLCYg5OrlPZtR6UZ8JrfmovNX7EItigj9LTcOaF7msdp7AUw2gd40b3EpmRw0eA-fJMH29x0KGh7F50PqBfm7Uehyj-smKQ0TjVBLAALs0kSVEFRgJpepoDzAyGkWXgRMggNBbGkQN9vl2y0jlhQqt4oDkJP6L72WJIloP_H1hvbQN0848F8pP3VdfIFIbf5xFAyfhburkZq2Y3LnAq0-EK92Owvlm2xILYDOCJJbUdkxg6fNWNTIUDq4JCZFCANXBtEidtBJs1BcXg0FIPGCPjv-WnzMrs5cMEkU_dDJtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پدر لئو مسی فوق ستاره آرژانتینی فوتبال جهان ساعتی پیش در بیمارستانی در آرژانتین درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27322" target="_blank">📅 14:28 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27321">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RC7n9QGq9N8cVyyWnmdHLIi8NKNvJIVD07iew-AEHW9VJ4It1iD32zJndsINZEvDVvaEMzflXPwz-8j3HSeKEZv4ZXQ37M_mj9bL1OaNgxmGuDd9uC-Tc5f-SU6qvtIdGc-UkLIMJl0-xVxDmlW_YFT0YcubCjJsMXa6AEnsgGcNqKqdrtX_PZTxumvRj0fO2bchiNlJ4gHqqWBjj9_a3Oev9m87orMOVJ9o6-ssahFMlXMm6lq0xRE1VFkMHbNcqIArPgLlgigNFxENv6uVUbsIyYbCEjlQDEBdG8OtqDiN0xR_BgwtiRxWVb4bUgKt8jcjxDQoJ-DDcjExXW1vYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پدر لئو مسی فوق ستاره آرژانتینی فوتبال جهان ساعتی پیش در بیمارستانی در آرژانتین درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27321" target="_blank">📅 14:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27320">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euzZT1mSvXBd5WUdy_NJZ_z4vP5kcQwd84jUblF7O5Yg4AUMoNfcJGNcAM6jvn-a2RmNLS8y2AfZSjoUQunV1nlQp0XI315E_lAVFeQvGPyR_FVkpj47glPZgkdMzEB2NNOB8GkGI0e6Rr2tdJTxLc4elWO8sOiNvBTaHObwk8jeDcbuVfAuTwkUmzy7qTqNwnX-adJtINrDlBO4yPpLyqw71inyurAB6aYaRGNKYdepSE7nhS2jrED4YwGGYJHkD20etiUlPmjzbhQNiecrmcY4x2k3XXBTyfDktN-16IR-M5iHUSVYrrA9eJCnuXC2Y0bYbjoGRYaou9-mJYW7sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ بزودی فابریزیو رومانو خبر پیوستن قطعی رودری به‌بارسلونا رومنتشر خواهد کرد. تمام توافقات شخصی صورت گرفته و توافقات بین دو باشگاه نیز در مراحل پایانی خود قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27320" target="_blank">📅 13:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27319">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fa190d851.mp4?token=Fajo63S97JBS7aICF7I5DvK9ik8lF3rBk-mH6NorEczMuN80czHQMddwSy5lxe5QsJ814FlYcJgxOUbW-7mtFYz13cbQ8lUUO8GNPJDCnwDycpUborr2j3xYi5Nrj6Wp1cuK5Y5X2a623Fco91KlqjnfEKW6Mbdo1TORTKcQxkcX8w1NNT3GDuykNWw1zTYsBSHPtL6vvGp0ZH2Gur8vO-m0ZxDJ2c0Qq5mkwdIUR7SjVhKfXmGTOiZzFajHr7he4tIMsXgvTLHEdkydtFSu63EBsrlVcsc1piNid0R5EaqditLT2vqt4vW1gDnm32lb_UZ6JVAh7SGgCcw2gy1rOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fa190d851.mp4?token=Fajo63S97JBS7aICF7I5DvK9ik8lF3rBk-mH6NorEczMuN80czHQMddwSy5lxe5QsJ814FlYcJgxOUbW-7mtFYz13cbQ8lUUO8GNPJDCnwDycpUborr2j3xYi5Nrj6Wp1cuK5Y5X2a623Fco91KlqjnfEKW6Mbdo1TORTKcQxkcX8w1NNT3GDuykNWw1zTYsBSHPtL6vvGp0ZH2Gur8vO-m0ZxDJ2c0Qq5mkwdIUR7SjVhKfXmGTOiZzFajHr7he4tIMsXgvTLHEdkydtFSu63EBsrlVcsc1piNid0R5EaqditLT2vqt4vW1gDnm32lb_UZ6JVAh7SGgCcw2gy1rOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
ویدیویی‌ از خداحافظی چندفوق‌ستاره از رقابت های لیگ‌جزیره؛از محمدصلاح رودری‌هم رفتنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27319" target="_blank">📅 13:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27318">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgpZrHbqmhJyNfk2P4E_09iP26650hCHrGteCv9CyFjf9MmzOSBpKDKK8OxMkDdvvdHVlTFzTrdrPksbjaKmE4FfmnN_76hUjjoD92v9-3B7hVf4vezboTwarvY4zcgWeBCenDDXZIOJ_GN3DODo-3O-ynxe7kvcG6HIcDnVuasRqVnuyu-hhHn1HyXk1jHkvADLxy1yz6moyj3afFpD9O9abhv3XQ81EUMvz7_y2U4kDqkiP8w5u8RmVlBCoDAtoqY0cN5wiwofcrCvrFwd9WLUDBJBK3EAxjfHBnmBHKOlC68iRvdNKFUvTbCSgZcouDJ265YG4_dthWW8ULiG9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ محمد جواد حسین نژاد دقایقی قبل ضمن تشکر از باشگاه پرسپولیس آفر این تیم رو ردکرد و به‌پیمان‌حدادی مدیرعامل‌سرخپوشان اعلام کرده که فعلا قصد نداره به لیگ برتر ایران برگرده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27318" target="_blank">📅 13:04 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
