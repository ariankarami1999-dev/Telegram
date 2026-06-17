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
<img src="https://cdn5.telesco.pe/file/UBNIVpxf4FvS2rIN6QVoufTh_hwWFV9w9g0GpKpalLqYCMZwloDseJscb0f--MArqt5Yq2DYNeFQXq50mppWj0BrcpfnsPElqi-ZbomdYoELk_0nUXRbylUjLT41ka_Yedtpj8FmUTd4Ema1zOd7RsfJ72PdGsK2p_NgVJpKuE-5lwNjywTjr4fYRM1AJK_QFqetUonKFtJlW3Ean20XeJoA-NOnDtS6_4UewVd0XTxhIKgq78koBs23bbdVtKoVEhh0FuFkwjJgoG5DZU9KwQiIpZHqL4Ox8Sqp37VxmyQKuycyrYfFGp4wh0XG4l3H9y9QkODK8OU-hnWYDfb2DA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 629K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 13:42:08</div>
<hr>

<div class="tg-post" id="msg-93899">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7feb575370.mp4?token=TTlofqKQ3bJo1xY_4Bst2DSJ35cyJDejdqqDiqh2zl1WgvseePLclulEJlEalB-1ppHulXcD3PBaotwCHrQZPHVlU6gtBA5KYE-6RyfvNMSgrdRpm9UjD1cu8V3YZ27b-JWwaxNc5lFwgL1OtEpIkqoSvP4UrQipA2F96jZSj3mFPyuarsZPCceu-w-Y5mDrspSRfSExnDuUtxhEoboR3jDE28JIDsRQM5A54f1jGmKT8gbr1YLTVaZ98fO0XJZM9b2bRqa1SfpIsFZ3LKZZ9QxaKbeg_5VgQ18aJUfmdZYjC44qHmqvFDp8RXjNLgoO8f2GfAUk63-irsFvyrQOgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7feb575370.mp4?token=TTlofqKQ3bJo1xY_4Bst2DSJ35cyJDejdqqDiqh2zl1WgvseePLclulEJlEalB-1ppHulXcD3PBaotwCHrQZPHVlU6gtBA5KYE-6RyfvNMSgrdRpm9UjD1cu8V3YZ27b-JWwaxNc5lFwgL1OtEpIkqoSvP4UrQipA2F96jZSj3mFPyuarsZPCceu-w-Y5mDrspSRfSExnDuUtxhEoboR3jDE28JIDsRQM5A54f1jGmKT8gbr1YLTVaZ98fO0XJZM9b2bRqa1SfpIsFZ3LKZZ9QxaKbeg_5VgQ18aJUfmdZYjC44qHmqvFDp8RXjNLgoO8f2GfAUk63-irsFvyrQOgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت تیم‌منتخب ایران در جام‌جهانی ۲۰۹۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/Futball180TV/93899" target="_blank">📅 13:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93898">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuWRs_QRwIQom2nvSzUql2RUXspfVT2i1hmBdD2kPY6MIYxPhmTOMhb34-fqjaAasSmp67nD5zU0wwMl2ZADElyUgOsEEom-7E8GtuCGAuktTwAGgEa9D84OaWI9uqgyGNNJgOX1TkvHX2fb9CLquLddl563LVQgOUBgmXzm1YsxR2phWsh4NpgU_klcKi_v0I96nZSRnkfCuYNW61sJxEw2k78Y9-Flnwq9C1oasGRi2NVzoAH4DJWkMrmjfKFYeZ3VAscan91mJjSwaBJbovQpIeLIMSzpSNskugtJkkS84Jlxe5H8_pz9qnVvh52bv3Kx1Ffa9ZJA1Qhwwb3JPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید بانو وندا با کیت آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/Futball180TV/93898" target="_blank">📅 13:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93897">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONKUjGJI7IXBoTWeYs8hzH_YxEdWEVwUlxNvX6oD9nV31w6vFSqYh-fSJL07Lb1i_vKLPPXd6cBsFt-tJnz8SBfz3gSillRpxa5bEOvtmBEGYKzoMtiCssa7TdHoMUmTo9Uz69kw_eeagJu46zs3Mbr1LdbqoxRQSZS0YRF2QIxPvFQmgDV9qrsHwxFuWmVbOvBSbhSOyOrkWzVeWbxsp7Y42aWouxMRBjSeV9ruElFARPidwWswOPO1RQyslKhKjtiw3pv7UNA3OEb4P4gdZsaSSxKYn2axKGqGcignz-kDVwb4TcRP6_uhPNSo8X3jgc5PSpxxTbB9yBQaMPGR6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🇪🇸
رئیس اتلتیکومادرید: به‌نظرم فصل بعدی خولیان آلوارز بازیکن تیم ما خواهد ماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/Futball180TV/93897" target="_blank">📅 13:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93896">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18bb140549.mp4?token=KxTgLi2K8BwAUwJfQ4tRDPhaG4ThJR8C40blvw4KrLpsuuxzM2LwPbCR-aVQTuuRfuXO_qd7XtmCGYIrEHynpre6E6WMmnNEPJauU-7bktNm9RkpD1XEVCaZ_1Q-xe6EZ0kJuLjDTn1A2ik71lTSpdPrOPVlEXKOm7NyiqoQ5Defwh7OJvRKYovEMjWdZTec5DN0LMZC4KrgjAdADmzDvEkNVAyzc-xRtl4EnpqKGUA-JuEFd_ijjqVmGnAIaQ0KMk1IVSm4IMh7PppT8hKtOu4mHb21eFcIbDue1prDTq0GKs6iNECNi1gfEnfgze78950ucJ6q_gk-gQC6ZA3FDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18bb140549.mp4?token=KxTgLi2K8BwAUwJfQ4tRDPhaG4ThJR8C40blvw4KrLpsuuxzM2LwPbCR-aVQTuuRfuXO_qd7XtmCGYIrEHynpre6E6WMmnNEPJauU-7bktNm9RkpD1XEVCaZ_1Q-xe6EZ0kJuLjDTn1A2ik71lTSpdPrOPVlEXKOm7NyiqoQ5Defwh7OJvRKYovEMjWdZTec5DN0LMZC4KrgjAdADmzDvEkNVAyzc-xRtl4EnpqKGUA-JuEFd_ijjqVmGnAIaQ0KMk1IVSm4IMh7PppT8hKtOu4mHb21eFcIbDue1prDTq0GKs6iNECNi1gfEnfgze78950ucJ6q_gk-gQC6ZA3FDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
بدل رونالدو:
این‌طوری نیست که من بدل رونالدو باشم چون اون خودشو شبیه من کرده نه من شبیه اون؛ رونالدو صد تا عمل جراحی کرده ولی من نچرالم
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/Futball180TV/93896" target="_blank">📅 13:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93895">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51823a43bc.mp4?token=qYlYmANOOO3SMN1P9H7FtD4EPQ_FXXvmFbyXv2YlPOKm5QnYawNi82gpA1lZVxUHXbzGhv5hYbvBUEx6Wdnh-JV4aoEPSYn-iZADCNPoEOEjjpicJbtWkah8VeFrQGq71Uv4x9NSbX9ZFXL9YrSiZMUG0mn1QQRNovIGz2Wa1WANs4TgG1Yp_U3PDCwYH395eXM3VI1R4dsCZ_CPJOZ08Aopm-5zZ-a-SK9rXFJw7l8w3tNXTztoMV45yD-bVSXBOVDA0CocJhKUZwA9mtIPLzTyVhwbZgMDK8nzUI4FM016G1BIhRcJC_lFXmEcJVDsgL8csDFy9FPKry2A5TlN-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51823a43bc.mp4?token=qYlYmANOOO3SMN1P9H7FtD4EPQ_FXXvmFbyXv2YlPOKm5QnYawNi82gpA1lZVxUHXbzGhv5hYbvBUEx6Wdnh-JV4aoEPSYn-iZADCNPoEOEjjpicJbtWkah8VeFrQGq71Uv4x9NSbX9ZFXL9YrSiZMUG0mn1QQRNovIGz2Wa1WANs4TgG1Yp_U3PDCwYH395eXM3VI1R4dsCZ_CPJOZ08Aopm-5zZ-a-SK9rXFJw7l8w3tNXTztoMV45yD-bVSXBOVDA0CocJhKUZwA9mtIPLzTyVhwbZgMDK8nzUI4FM016G1BIhRcJC_lFXmEcJVDsgL8csDFy9FPKry2A5TlN-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاوره اخذ مدارک دانشگاه آزاد
واحدهای معتبر تهران
کارشناسی، کارشناسی ارشد، دکترا
با استعلام
💥
(
بدون پیش پرداخت
)
💥
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
Telegram :
👇
👇
👇
👇
@irantahsilat_iau
Instagram :
👇
👇
👇
👇
Https://instagram.com/uni.irantahsilat
جهت ارتباط با ادمین
👇
:
@madrakuni</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/Futball180TV/93895" target="_blank">📅 13:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93894">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🏆
🇪🇬
ویدیو وایرال‌شده زیبا از مربی مصر درحال توزیع آب میان هواداران داخل استادیوم. بنده خدا از آذوقه بازیکنا به تماشاگرا داد تا گرما زده نشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/Futball180TV/93894" target="_blank">📅 13:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93893">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51ab3ff261.mp4?token=NB_xpiNt--r7D500pCApEVyYD1ykI3sCDtgeIq2a4DiAMgL_TyD2hiUNc53igwBqz3V1aYumh2lCHJlfeClINQRO5T0Hcg2vVFV-cpi6kH9JKy0NieE-mpwL89usedLHedmalWDt919vsRDzbp_i5Uv62U50SGzNe__mA1-LbYX8BpYBB-8h7SE1dxGULHH3zFJW7rAxGJUowAwYJ3O0RlvIJb6SJ2no2laJ0FGPf2oie6LGAkOyGqt83Alswow6rZO-2qXisdUL5LxaPEPyQIBID6ojMepP-fJuy7DzNQZL0nzpXDBqmlie_lXmKMFl2ToYEB3C1hWLaNjxj1AZRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51ab3ff261.mp4?token=NB_xpiNt--r7D500pCApEVyYD1ykI3sCDtgeIq2a4DiAMgL_TyD2hiUNc53igwBqz3V1aYumh2lCHJlfeClINQRO5T0Hcg2vVFV-cpi6kH9JKy0NieE-mpwL89usedLHedmalWDt919vsRDzbp_i5Uv62U50SGzNe__mA1-LbYX8BpYBB-8h7SE1dxGULHH3zFJW7rAxGJUowAwYJ3O0RlvIJb6SJ2no2laJ0FGPf2oie6LGAkOyGqt83Alswow6rZO-2qXisdUL5LxaPEPyQIBID6ojMepP-fJuy7DzNQZL0nzpXDBqmlie_lXmKMFl2ToYEB3C1hWLaNjxj1AZRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
نظر دین‌هویسن ستاره رئال‌مادرید درباره کورتوا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/Futball180TV/93893" target="_blank">📅 13:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93892">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e6f682474.mp4?token=H3asiiEwNVdj8jE7loVTLuZ2_7EBdRNS7pYOxwXB2XvjLZPxhyACCAPUoVAayPl0G5PM5kmU0_ZoXFXX60873HVb-WTyGwtC_eG5sL5w5L5raMWVBKRteW4tyQePbO6_Tc3VyfbpBR8Iz3NMbLEMEK2lHj8AD200-DmFK81RziY5v23Yh9TPhADwPE26bIMMRpiwGVtKD2fDGES9dPJa8EtKKFAIOid7OoSANWFWYcwbzxjc3WlG6mrsCZ85_uayaoFFH318w02C6omORTS7qbcoznXY26DA0gW7KOndgoZqEBEXqr_LNi-0rYon7SDFmUpLgzBngaDI_dhcjNlEqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e6f682474.mp4?token=H3asiiEwNVdj8jE7loVTLuZ2_7EBdRNS7pYOxwXB2XvjLZPxhyACCAPUoVAayPl0G5PM5kmU0_ZoXFXX60873HVb-WTyGwtC_eG5sL5w5L5raMWVBKRteW4tyQePbO6_Tc3VyfbpBR8Iz3NMbLEMEK2lHj8AD200-DmFK81RziY5v23Yh9TPhADwPE26bIMMRpiwGVtKD2fDGES9dPJa8EtKKFAIOid7OoSANWFWYcwbzxjc3WlG6mrsCZ85_uayaoFFH318w02C6omORTS7qbcoznXY26DA0gW7KOndgoZqEBEXqr_LNi-0rYon7SDFmUpLgzBngaDI_dhcjNlEqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
😂
صحبت‌های یه خانوم اصفهانی درباره بیرانوند:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/Futball180TV/93892" target="_blank">📅 12:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93891">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/93891" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/Futball180TV/93891" target="_blank">📅 12:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93890">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFV1emPqj_TJY4FCyCsYHP2oHoNyK3-Wt7z0S61v8-_12KB_I1A1jmrxtEK4XWgQnqny7mrQFEoB302OQPwC7fqahTfMUXKbftyvUq_u_t9fx6lSGzi0IEal0jxb2fzNiWBnnX6ZzSrWJdBXoympchKim-P7o9PbmEFzZoqwQSHPi1P0RP6WxSg9rU34gbFwXTQl3uwXEcrAKsP2svl9F65SxCW9hrmWyexvJ1EglQHLeUBaxflGkDn3IueKold8TJRyX8D6adFvYy4Zd09BOx2RtCJo5uC9MNnhhnj6wf16IjIV48N-UAjVTLMhCFH0C-jckGsWL3TlH9qSHapl8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
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
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/Futball180TV/93890" target="_blank">📅 12:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93889">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlpHXXPOwUcnWnbuE1vrZt5ZXr0GlaBs24aAZcotAbblzvXVxT18xX9nPB7R3-cgnR2RwT8cJLUnt5HgK7bQbmZ0Mt_UjPh7k7UFhhGbDPQIAoQwg0r2ZhoY8_PpAR_8hKdbjhMpHg-sBgJXmTKqQmUEUHXBSimNdFluPeu4tyYx7HgDkvm21r0luFYfXLzUO1AcobbilpULKZeiR_G5CM38DOkIVdqSKFOa4AVbbGhz7Xh7iB0Pl3m9GyTt2o-NZgA4SaKBv6iQqe_87mWhW2vcXx0SQhoUAk2UhcIPBv5Ed1e9PIOiJ1i3oueMN7-v1IDFuchhtxcwE7MoxLcLIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇦🇷
تمامی گلهای بین المللی لیونل مسی با آرژانتین تاکنون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/93889" target="_blank">📅 12:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93888">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33232f8760.mp4?token=GrpoKfmgvm8RtVMUl2uYgPQOOiiQwTr6pkGm4vKUt5r34YPFTmyhevY8pPcSkOhh4QZH70NpwuoUpasEVAFuYxRXKX3vcrhVuKfs9RR9eBi7zaXOmWsx_J37K7HBiryh0JXyx7lmQkUWmyDzDIgBMknZwa6DvJ1Xdko0NT4-EJS47lYhaznqE3xAyuN4uUdrDyAqc7LsKsOkYzT2HVB-inGhOlVUQqQu4f0c-M4MuSHo9uccqpujqUuWl_-e3ni9k1rVEkpvokNK5VZdt5Qdc6FRFR2-gXELSD8TXesRG6mC3LgUKxn8t4Sb_WenBEslTFwLYsABnZhdKN5wARwdzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33232f8760.mp4?token=GrpoKfmgvm8RtVMUl2uYgPQOOiiQwTr6pkGm4vKUt5r34YPFTmyhevY8pPcSkOhh4QZH70NpwuoUpasEVAFuYxRXKX3vcrhVuKfs9RR9eBi7zaXOmWsx_J37K7HBiryh0JXyx7lmQkUWmyDzDIgBMknZwa6DvJ1Xdko0NT4-EJS47lYhaznqE3xAyuN4uUdrDyAqc7LsKsOkYzT2HVB-inGhOlVUQqQu4f0c-M4MuSHo9uccqpujqUuWl_-e3ni9k1rVEkpvokNK5VZdt5Qdc6FRFR2-gXELSD8TXesRG6mC3LgUKxn8t4Sb_WenBEslTFwLYsABnZhdKN5wARwdzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
▶️
عملکرد تماشایی گلر کیپ‌ورد مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/93888" target="_blank">📅 12:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93887">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjQcEbQuEk9XBG9aroYRtR7EXHYkOb0Y8ai7b0LBb5REPku6R5_xBIAimLZAoxh3KNHVGSPKV8shl2vXMzLAymXQdG8zS1XyRf_xZo_pz2peDCVikUZlKCs-DheFpSLIMttzvH8bwouBNXYSkk35XgdyNWiKk1TOBdG887sVXv7UBWJnOR-owGggFeCv2GvNFwwn8nB5s2e8vwaaHF_EqpwV6L2HrJ9JS1vSM9z7ogGbGHnsYvHD-a3KRXUe9S2RVeB9lVGl7-12Y1UbSxpmXpDq4HnqR6BepyjciVC_kVUzVEM8cQ81GwXI9kZof-04W-CutDsOZ-wKM6pD9yXYNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
برناردو سیلوا رسما تا سال 2028 به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/93887" target="_blank">📅 12:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93886">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e52fd3bd1e.mp4?token=ezV1sK9du2MLep9mThgnmoG3Gau-sKw6OmJ01RfyLOp4rho6QXU4olBqhm-eUD5OkdaYH7XHru5XsdJkLjmmXWod4-elElwnZ-rCNwKCF4X1tULJMOpjFVWAu9PG5aeTI71GlWvJQwMWGmdOMlzDtjZGB8L9LjTjfb0KnPxjsAEjbnjtRouHp4hCl4l7r-8C7g_0DK1V7T_JlilwQww_-LM29TGUAxDFa9OGQC2XpgNOS7Uui81uSw8QeGodOi7SVvt1bp4L79XXIBdoBnfvz8Mas27IjgXasDML9vJk38LRin_YsmHjAZVoJnmlOVx1aF5eoGYAulMQ4iH63rrqYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e52fd3bd1e.mp4?token=ezV1sK9du2MLep9mThgnmoG3Gau-sKw6OmJ01RfyLOp4rho6QXU4olBqhm-eUD5OkdaYH7XHru5XsdJkLjmmXWod4-elElwnZ-rCNwKCF4X1tULJMOpjFVWAu9PG5aeTI71GlWvJQwMWGmdOMlzDtjZGB8L9LjTjfb0KnPxjsAEjbnjtRouHp4hCl4l7r-8C7g_0DK1V7T_JlilwQww_-LM29TGUAxDFa9OGQC2XpgNOS7Uui81uSw8QeGodOi7SVvt1bp4L79XXIBdoBnfvz8Mas27IjgXasDML9vJk38LRin_YsmHjAZVoJnmlOVx1aF5eoGYAulMQ4iH63rrqYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های امیرعلی اکبری راجب هالک ایرانی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/93886" target="_blank">📅 12:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93885">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc16e86e4b.mp4?token=ibDPSwLpOxGBo18FD9cDNnaf0K9HQOfUF7bx13iJH7_NjXjTmvfclT5ueAqTe7Ow3aFBZY-TyucRSdXz1Emkkan3SvOIQjsWFaXhVMJVCxQVa3qS63RDEEJ9tM7PGRiWrUZDdNbguiYYlLnIqkiqJtPPiDOuMrQcLBck0brtzRetIOasMSWXyszTO8VIiuNrJh1huLouFj3LRxbsMBBIJEqxP1_xnizkOpUeO5haOf7AhjjJQfgwwvtm2RQ7C8dgjxx4SMkk7MFP37To-XkrJYhVfxfHCIxa8-oYf2MLZpUnCJhdzcUN89ZrU2sIjg6cix3hVNI6o8XA453L_Vk0oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc16e86e4b.mp4?token=ibDPSwLpOxGBo18FD9cDNnaf0K9HQOfUF7bx13iJH7_NjXjTmvfclT5ueAqTe7Ow3aFBZY-TyucRSdXz1Emkkan3SvOIQjsWFaXhVMJVCxQVa3qS63RDEEJ9tM7PGRiWrUZDdNbguiYYlLnIqkiqJtPPiDOuMrQcLBck0brtzRetIOasMSWXyszTO8VIiuNrJh1huLouFj3LRxbsMBBIJEqxP1_xnizkOpUeO5haOf7AhjjJQfgwwvtm2RQ7C8dgjxx4SMkk7MFP37To-XkrJYhVfxfHCIxa8-oYf2MLZpUnCJhdzcUN89ZrU2sIjg6cix3hVNI6o8XA453L_Vk0oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👀
🇲🇽
خانومای‌مکزیکی این‌روزها حسابی دارن پسرای خوشکل اروپا رو کف آمریکای شمالی ترور میکنن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/93885" target="_blank">📅 12:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93884">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62a17b1db4.mp4?token=dQ6q20xqss-B1DfGeRf6eS7Ie3MF1LWWrHGe666EORCqy0T51grC2louyOvBsW9PGRxdyOHjnV6f657D8BaxZD1AQ2guaz_2WKFevFfegqUTAiMlv2J2WxOvce_twdbJPmw8h_7qZCluurxTZ15GiCRyoM0KFF8LEW8InmXjTCFBepRP6LlsaXbOIklvUuTtS-PVnGVwfxSdhGpvy8FDFrD8aU9pnRSfLasKwAPqNzwu93MIXx4KDASZdsc6i5D7ttscWqiGQZ-nSDMfpSKEmzSfwszGKEB4G1sSMOxOJvaoqm1s-ceV-v1nLNGhsfgzvcUnEKywqRRypnlx3uGOfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62a17b1db4.mp4?token=dQ6q20xqss-B1DfGeRf6eS7Ie3MF1LWWrHGe666EORCqy0T51grC2louyOvBsW9PGRxdyOHjnV6f657D8BaxZD1AQ2guaz_2WKFevFfegqUTAiMlv2J2WxOvce_twdbJPmw8h_7qZCluurxTZ15GiCRyoM0KFF8LEW8InmXjTCFBepRP6LlsaXbOIklvUuTtS-PVnGVwfxSdhGpvy8FDFrD8aU9pnRSfLasKwAPqNzwu93MIXx4KDASZdsc6i5D7ttscWqiGQZ-nSDMfpSKEmzSfwszGKEB4G1sSMOxOJvaoqm1s-ceV-v1nLNGhsfgzvcUnEKywqRRypnlx3uGOfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خواهشا تو عالم مستی فوتبال نبینید. خارش گاییده شد بنده‌خدا
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/93884" target="_blank">📅 11:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93883">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd5190b2e1.mp4?token=PJmBUcRS8GERN5a1dLqtia85FbzBJ3xvJUA7MrzKXACReIuC3OX3tPF6G8YiIhlm3pxbhRMKbNgBan_ebRNKdLQdHSPQSExDm88LvlsZeVmDuqtwf2RK5JIFKXwwLPyPk8pfBc68NPa8nY6mLmON0fBCfX14HN-2hGeor2QZV-QKlWRwTgoG7TefSXVQsc_ay-rx0IKyndeVUkZ57PiGJd5r-5OLvFmyTTF7pJMBcyPcokIPGcHiGtB1NqTBXi0es_vDcB7OR7lb7A0vNMfspSgdgojOJJDCyR_uUZqwKFqikPCgbLAFC9r8KohiLVptPfzKBlISJXWBg1X2a_aVAEn3S6HIdmLt5aRXW_G1av5g5Buf9dqzcJls6bULOOZNqWxSUbVzccDt9727TXwl3hBmTV076tpdYax8irTRV0prhEat3WwJ3Kx1dUvBPhMqUYlwDAz8OXsf6y8Rx40CjCltBsyGu6HM_st9JF03rh87O1tmLUg7Y7xX6NCPfNbuRwf6FZ3WTb2-CkNnaAuppqko0NBTQeSgRlcPpeWZyi0QVFQlFwyYAMcsAZIr0GomXvSrk5DcdHAW3i3xEU8iHn_1u38mzxqGNCmSiGQEhJSa7C5cHSP_lS0n3GjRULAj9IrM5OvgBQs4Om1expXXhQKEnYblEaIX0Tq36eQmadY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd5190b2e1.mp4?token=PJmBUcRS8GERN5a1dLqtia85FbzBJ3xvJUA7MrzKXACReIuC3OX3tPF6G8YiIhlm3pxbhRMKbNgBan_ebRNKdLQdHSPQSExDm88LvlsZeVmDuqtwf2RK5JIFKXwwLPyPk8pfBc68NPa8nY6mLmON0fBCfX14HN-2hGeor2QZV-QKlWRwTgoG7TefSXVQsc_ay-rx0IKyndeVUkZ57PiGJd5r-5OLvFmyTTF7pJMBcyPcokIPGcHiGtB1NqTBXi0es_vDcB7OR7lb7A0vNMfspSgdgojOJJDCyR_uUZqwKFqikPCgbLAFC9r8KohiLVptPfzKBlISJXWBg1X2a_aVAEn3S6HIdmLt5aRXW_G1av5g5Buf9dqzcJls6bULOOZNqWxSUbVzccDt9727TXwl3hBmTV076tpdYax8irTRV0prhEat3WwJ3Kx1dUvBPhMqUYlwDAz8OXsf6y8Rx40CjCltBsyGu6HM_st9JF03rh87O1tmLUg7Y7xX6NCPfNbuRwf6FZ3WTb2-CkNnaAuppqko0NBTQeSgRlcPpeWZyi0QVFQlFwyYAMcsAZIr0GomXvSrk5DcdHAW3i3xEU8iHn_1u38mzxqGNCmSiGQEhJSa7C5cHSP_lS0n3GjRULAj9IrM5OvgBQs4Om1expXXhQKEnYblEaIX0Tq36eQmadY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇸🇦
هوادارای ایران و عربستان کف لس‌آنجلس داداشی شدن و عشق و حال راه انداختن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/93883" target="_blank">📅 11:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93882">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzegrH4CZQEPQ5zhxvFycV6mVKneclItaUYwVqG76r155Tc7ryMgVOwkKJCU6LRYVHLzDtQdizWQr7neRhLPnNGVYs4kPhdnDeN-LFB85-kULDma416dzDGUMGNfEQzjcUmjnKVjk-PKWJ8Kfv4-uf_BIQl27n9PKVHP_wGCraZ4fE2GhoN6RB4GlckB6OTXUoZBvMCaq-g6c1DUzMLxg6v5Sc2fsEfCe5aMQx_dzyV1z52NRtL05SCAvRYDgrMz2nU3034j7dT6fNf3QyyLVSwkqkPQtUE6UwUYx8Jxe6ZwyG7zWdPjAy1BNwtlrbbDqXLcUUXGrO2hHN6pw62mOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر جنجالی رسانه‌های اسپانیایی از کص‌ خنده‌های یامال و زیدش بعد ریدمان جلو کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/93882" target="_blank">📅 11:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93881">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INAES9rE8YCDbG0FIJhYUoIwPvoEzmBBlxiYVNWzzGamXPDGsj0dKd34QcnOPSIap9I5Ck2XaD23IIBPh13Rz4osiWYE8QgdmNs9fa6mvr9Zlq2nvj3AiL36AUVxr-2ThSfHEX4GAa0Tp64UkAtqJY44xOQWkeLz67NtkZfCJO-zJRVg4APrBcT-BxIljX062xs8Upgw4VNtKsxbiJhiIWppZ4ecHgh6rIQLFxhwmNwrArBIxsWSOwGbomBmxkOOe-_ex_2JvxBWxFZfssurvfBDjoacwQbE9jruhCDU9HrsiHr-1J84iY_SnbBRA_jxI8B0H54uIMD_fuvMljiyIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
لیونل مسی:
دیگه چیزی بیشتر از این نمیتونم از خدا بخوام، اون خیلی بیشتر از چیزی که تصور میکردم بهم داده. الان فقط میخوام از فوتبال لذت ببرم. خوشحالم که منو یکی از بهترینای تاریخ فوتبال میدونن و بابت این همه محبت و احترام قدردانم.
🩵
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/93881" target="_blank">📅 10:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93880">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12875b1bbf.mp4?token=Jp0tBxzFWjaL4QyAvRas7Q7p-msI39l2MwLecHZiPD-XLLVUK8u2PGeK4dJpoPOa2DkOzn_FqleXZoY7VLrS8CCiYIBUYoomt_V_1Mcyen4OHk-Lq3clx-fe1uWwQH7IQs34nQWcPCM3VC8BXMlVWf6Pxe111ONwqpyCHf_F9aEFXn6O5HSOVXV4y5zRadM8S2Wcqvza4HElptrXHpQDVxej3XzlF3W9_X_bdeU-LGz0Xh8t03B9yH2Q1emc0lA9jdgKftzLhJYVIPUUEc7utVIKwzfqv4bDWP6zDBU6HlQvE6-7MWZaJxi5_Ef1hU55dbsJ4Pnc4VVj0vdzcZ1HvoNaVzOhQtS31fxV30valIjktVMOBKwe-YMCBlDk6P6VvKfOPSi4tG0VSZg94KmvRVXeAYf3XlxBjqLpFYxVl8Isy7WywUGd0U3PQ2Zfy9pbdTAMz0RAlwcNDUIcvwkEGlxzCU7aTCxd4Gt4BrPQ1BAJVdYGA9bJBSNCNjEGhWlb-TUkpTDyxquLB3vAeGRkYC9RfLKmMe-X_eGKI08EZMKVqQQSu4zW5GDqBCn7cIIHVXs3e5vgT2QltwcNhW9etTie4uIMRmiOzEuUsdvYHb2GTgwaEkV9EU8bEBieUJXObXlKyIdGWgfKwpua9t6Ut0AwAeqhQzwSx3SuYinHIvY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12875b1bbf.mp4?token=Jp0tBxzFWjaL4QyAvRas7Q7p-msI39l2MwLecHZiPD-XLLVUK8u2PGeK4dJpoPOa2DkOzn_FqleXZoY7VLrS8CCiYIBUYoomt_V_1Mcyen4OHk-Lq3clx-fe1uWwQH7IQs34nQWcPCM3VC8BXMlVWf6Pxe111ONwqpyCHf_F9aEFXn6O5HSOVXV4y5zRadM8S2Wcqvza4HElptrXHpQDVxej3XzlF3W9_X_bdeU-LGz0Xh8t03B9yH2Q1emc0lA9jdgKftzLhJYVIPUUEc7utVIKwzfqv4bDWP6zDBU6HlQvE6-7MWZaJxi5_Ef1hU55dbsJ4Pnc4VVj0vdzcZ1HvoNaVzOhQtS31fxV30valIjktVMOBKwe-YMCBlDk6P6VvKfOPSi4tG0VSZg94KmvRVXeAYf3XlxBjqLpFYxVl8Isy7WywUGd0U3PQ2Zfy9pbdTAMz0RAlwcNDUIcvwkEGlxzCU7aTCxd4Gt4BrPQ1BAJVdYGA9bJBSNCNjEGhWlb-TUkpTDyxquLB3vAeGRkYC9RfLKmMe-X_eGKI08EZMKVqQQSu4zW5GDqBCn7cIIHVXs3e5vgT2QltwcNhW9etTie4uIMRmiOzEuUsdvYHb2GTgwaEkV9EU8bEBieUJXObXlKyIdGWgfKwpua9t6Ut0AwAeqhQzwSx3SuYinHIvY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🚨
‼️
بخشی از درگیری شدید ایرانیان در سکوهای استادیوم سوفای لس‌آنجلس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/93880" target="_blank">📅 10:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93879">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaFFmBREUfV8PKycW-P8iJ56DKG4tOeW2sIQcjIeo-IBniz9flYzOBQQjTC8cJks2RuiNarOr-T5XCzsWCvcEkuokSyayJXvjqN40fYC_D6F6hxEdipi9uApduzYZtmoNQ2DBzm6oUibaU7edZdK4wCOoH9gxgwPZppwTAHOqfkxL-t5QGn6rwlW26VIPRHffX5o40zpDbkq0E1mIIZNAtGbKiiMcCwBA70ERAvs8NX0k8Vkd64nBv6yP2UnuC5Fj5bGS8aHGuzdRphdhMP7tu-4yxkiclRJXPbcmlcUOYgtccVUZNikAq9xQu8RI4zeVv0eVKe3wHdzBO56Hqmo3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
آرژانتین در 7 بازی اخیرش مقابل تیمهای آفریقایی در جام جهانی برنده شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/93879" target="_blank">📅 10:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93878">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyaguQ6njFQxKXhZ0Bd1BJ5zUTQvaSeQtwWfFZ9B0-QpF2xbkrR_l9LCMUm4bbYD3amoNfO8i-crBD2xamoT7svA1eu22T3j6nNLa3dfyPO85Rs0B9sbO8JMhQ7PGBDsrfHCUckkosJmn-c1K0QaMbWYTSgcbABp-Kx39Ae2s0ni9a46zNwtC0BI3vb0AaAEYgftGC4hwxOakW7dPKLoHG56KQrLH7177PE1UPTa_OyFm5TxAls7iIu1VGkxwKaWVqodudFGS12WEvQyiWCG4ogkF30pzhGiheF39zFz9ujNWpyDPbGpqq-_n3GA99nITd9BPyNSksQjubd1hx6EqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🔥
🏆
زوج‌ایرانی جذاب در محل بازی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/93878" target="_blank">📅 10:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93877">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bf4a59c61.mp4?token=nCmqg4gwDJ0mTlxHJFQFFyNve_s5qoO058AUcKQHX_pASv8FD5G1GX-kLkAyN3nIub66ZhNLpNfS10KPp08JINDAh4SRf5D8k94ve7kmgqZAP1T5fCI0pNhzHAxZoKSGinMxG1JQ6jxT0jtci6MXRwtkP17z7pVErjQSDvCmBdyTu5WoIFr_viJlRZ1upOIvqzj-ZdWD-YjS3MOGcGPffVovWuwZFUvOzlAeCuTXV636HyBroinH07osLGaizz0LTEtoAZ7EIRkJS0CRIv6e4CzKZMnKLo8NK801qhEroJGCflHoawZ1j2SdqrRmWWDhheyUg0Ielci3xntaVc_Q6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bf4a59c61.mp4?token=nCmqg4gwDJ0mTlxHJFQFFyNve_s5qoO058AUcKQHX_pASv8FD5G1GX-kLkAyN3nIub66ZhNLpNfS10KPp08JINDAh4SRf5D8k94ve7kmgqZAP1T5fCI0pNhzHAxZoKSGinMxG1JQ6jxT0jtci6MXRwtkP17z7pVErjQSDvCmBdyTu5WoIFr_viJlRZ1upOIvqzj-ZdWD-YjS3MOGcGPffVovWuwZFUvOzlAeCuTXV636HyBroinH07osLGaizz0LTEtoAZ7EIRkJS0CRIv6e4CzKZMnKLo8NK801qhEroJGCflHoawZ1j2SdqrRmWWDhheyUg0Ielci3xntaVc_Q6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
تنگه گشاد شد دیگه چه صیغه‌ایه؟
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/93877" target="_blank">📅 10:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93876">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUtFZY2KfAHmUJDFv8sebVMmRXZ3jkTYUjKCA8ILWR2yaS0YQUE7nSL6taaWW02ZVetmVTnCeJJcz8CrxxK76vF0CPirzj25xv4bfpVhR5Qeo11MyEZbRLez6JlU1Uk5DN0P5i-M5mv3ZkbMiikDehWnZJVCxtMx6MIm3PnurrxAI4QfMLLeJNqir6QkY9dlaGY_9AEQqB0MVqemNLLY9Gmw3gfcRtw6vcrbRXPjJk5NbhaTCq3C_AXOO_0xCWCVMY9MVLSleBxtLfI9Hce_R_otfbSS6YsqpyS020srJ3i6L8Vi-MoSVybyD0nHYei1vGN3e6xd-lGQBJir7PAI7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه J جام‌جهانی پس از پایان هفته اول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/93876" target="_blank">📅 09:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93875">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc3df4ad3.mp4?token=op0m6FBIqCz95vNIEIN1wrxC3ACZ0DTmNF8NeYqDbbIrNYQn_GQdZLmiFxDzTTJCycquuHH1aJRuKZBFxFm2-PFdF5Maa8KKd3qWOWJgJWUZeRgoJcsObgLcHubzXrJs8uKpzcR0fh3B3yrVzOI-wFynPUZZPDS9mksm3nXFJkAlGTTNkJ4JErrRBRTx2mmpOsItAskLS8xQh8ZKvdBHmSVHbGGqwiwkZo2GRMqYdhzZHVXbgM3Pi-eC4LUBCwAjAWLrU-KzkXXlhvnN6fLhBxZIi_8oJaHyp6w22JHLgK8Y_umz349jhlPkp0a8Ey663tSBxJht8bljluPO6Atrdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc3df4ad3.mp4?token=op0m6FBIqCz95vNIEIN1wrxC3ACZ0DTmNF8NeYqDbbIrNYQn_GQdZLmiFxDzTTJCycquuHH1aJRuKZBFxFm2-PFdF5Maa8KKd3qWOWJgJWUZeRgoJcsObgLcHubzXrJs8uKpzcR0fh3B3yrVzOI-wFynPUZZPDS9mksm3nXFJkAlGTTNkJ4JErrRBRTx2mmpOsItAskLS8xQh8ZKvdBHmSVHbGGqwiwkZo2GRMqYdhzZHVXbgM3Pi-eC4LUBCwAjAWLrU-KzkXXlhvnN6fLhBxZIi_8oJaHyp6w22JHLgK8Y_umz349jhlPkp0a8Ey663tSBxJht8bljluPO6Atrdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
تیکه عادل فردوسی‌پور به خوش‌چشم کارشناس مسائل سیاسی صدا و سیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/93875" target="_blank">📅 09:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93874">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRLwXu2izIEj4uiCLvTGyH5xNaQqEgGkb7HRea47gJVPs8K5SxDwrMWd52aKbAM4jg5if3uDWC3ocPSK8rcRtxGuMXFWsRKVO22_8HT1sdF-fzuK0rMw-OnMMZEMybCGWt1SdBy3smhFCPEwpyk-wenZsznKL0yID7ZSoLKx_M8u8c00n8P26jZHqzjOhRe1rJwGTJQbERKw9hO5CFGuTCHl3uuqKq4cNKNAQJ0erAkZAemDyVRtt6-wG7TkgOBvNcooocbG2ChlVd4QpAFy68fPNCp7X2Lo4s4V5E1OJR6Pk54WG1HHM_wwKB8mWA7fiFjMztDXqlVDRDqvBw3_pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|ایستادگی اردن کافی نبود؛ اتریش جشن پیروزی گرفت.
🇦🇹
اتریش
😆
-
😃
اردن
🇯🇴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/93874" target="_blank">📅 09:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93873">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گلللللل سوم اتریش ثانیه های آخر با پنالتی</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/93873" target="_blank">📅 09:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93865">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LiSMAPGnhJQqiLs-QsV_2uJcv2XY--m06DJ98nk8YVd_CQUVUNYPn_sCgsRma0ljCKlndFxb24NrH6Qs0hzWo7cjyQvGFtSiA-tnogvXtP-nNPZfepxL-O4IF5zorjnSmwozFAuuHbwMRyjMJMjm-UFVSkVND5HC-6BwB6wetCAmZxvwKj-J3fVRDepxJItq4HramGsj0gXV6SCQWysOSUEiO6XgLsWg0AhnySW37OVnAryidGUzJ8hGELkFVmc-Q0WZY3_0GgjBSve5DdM9Z__5iKZrRdagfmeAG8KZb7lSRZi8EixhMSNiXcVD59NkpS0vYF3Usc4CcThZGwgK0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NdnD03abEPyD6JXywPlHfDcKWuaXLJ_Qvn3ANgNj-mri5XQbDyGpLraTuc57m4ME28nwQKztb9zczi6eJHNMlCP3afzrbvYRV1Esj2WUrHpHhHlBvId0Dbz518fV1LJ292LfZSLLasaA34_OXBAUbP1f0UoQvHz9EyFHC7dMNs-SicZYwxyRjh6AZ3S_nIpZtCqzeDJ9KlTadnGK0cDcIRd6BZkmofD2zcKm6MMtfp2BT3cJ-_2_TJUtsrQra_t0Y554etxwzfPq_ssGSG6JzmvEqySWSM82Pe8hn-QSGJAHnrjTgrxOTLvkZyB1kLJMqyJe176VR_9TX3qnlHYTJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z7hdbJIZM8-B4PDHZRGjfEEyreTG3OZfbJWgY4K7VkeVJWjM05PnJNdIwstfVAA73AEjNUWhgUOvLH2dv7ivuA6_CQrNAgWEZfMXZ0CjvHyt5AwqS49wrLlGzugWHXYQbYrmeeTSK-xLZJ3G8he9U2V8wRf-KhJmBu44pWf6aLwMXAqTMDD6LOfoSOvfv8kANyfp-dN7_ebMB0lPdLziB_c-kXX7AIejPQgipEw0GNVDLjPup-fFoDKBhuOnihC-4vGAIcanI_KgS6ipYqlZlP1r64nRZDxHh9RnKixR8Vkxxnxhs_M9Vmwi1Z1bDyJIGFjQisk6OKqH1yznsYopFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOVZVqAsdvh1XWSaC_wn5AjScm7jZAKTSh1YCbiyrudLhOzPuCO0QNDDnruc9CbK8ONjjJbVTPvAZnn1DTxsWUfbDdjNvcvxpVCzBGBJx-T9ap5T8ymmeSe2oq5zRZYhO0JTFh9kQ6HG9s9Mu0ICBwg2F4F6WANn5upQVZpuTUweQ_EJNniHmDW0xiin4zbYGmpHg2QkIsdvyZeBaublH9sh04o3hPBKGGDebDmR3XyfDayezEaUh2iida1O3ya_dNoRTJq_ShFEHBugdJ8nfhDEFrT0DWJIoFtGbAiVfvWICDnq8f_aC69IIFF3eRCIhT-4cFCTesIrMtzo1DBKsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eLdEz073a-VMeGfF3-DaRt3QCxBOXH1ePpWHt5zo6TbozvPUTH4dsUf3mmXWBDK4vu-L4rnhZF8pQQ8bBQmziVstqjh2o0IDCXJWq66psl1dbKUcltAdEiy5V4BgyBcfKhxnQGg_xaTNWp8M0GDddLpcuHSi6tj6ztyyCagnR0hMF6hhFTgautxV9P7G7QP5HfFnp56TZ-ZeVrvvrsuCZEEaMs_qC2Rfp85EVNK1Akq3IcQTKngcgz3eMj3TEgfE7OoOsDY58JiG-azCK3yLMEWv5wUqIjxdxdfqD6s6fJWb0movewhVs9IssPkHsL3W4uzBVlXTo1T4HKO5XMmF5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0fg5q-TbX5j0DRfUGc7SltZrnDY7qfFDob8pJMCmA47mfe8t-LHruXrWgT1JKX2DCi24iuZXQklsdE1sGkekiseM5uJU8BXySVa7B-PgY_aLaRObm0wHWCdOYGpZo5SHSC6MlAN_-mw9TI1DgaKpV39xzgR8jIf6N9ILqRMmwgnZRFsp6vteRRrCpZTJwW3UICxqmozNxUJ9VRgdWIPoI6wrhRVSPFhtA6zOddPnEH0mjHYQbyBoY6ekzgo34g8PnHLtLFwf1FfIP0rCBYbOWD1tYAHjMSdFLqPj3Xy1_WRUvdP_0cUbUeFEUIO7npyXyUftMNWvXn03S3oQ13Ppg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oT09njQj_3cC-QeyzfInwfVuy_fngaXMQr-jbyHjXZ43LWujVc0A9Vb8w3U833HQF4OpV3p4GTb1ahWcLAxq7f7CsfRko6wCjGn8F0UWBXH207L9_u3uQbDjF9Y0ygg8nPqaanW2wTLNspGGxm6gMcRPpP1-HtMGeVxrC02dLINWa-dKZk4-QDE8aTYSF9U1O25mvIszwAvKbrNBqBe78kI5XQd5a36vvG7w1uO6HA6gn3eO5pucye-hdvG7HB5FtWry_WfkKg3g8VWmy9xT0UZ70fCLgnvneDChbP66BVdJyAo8bSGpiy8ZP1um3h5DzSkiSY56xnfrgTkdcLS6Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmOcYzx519ZNgOLND9ZqZMFjrhtiZoRGVIyF5aV7zb671qKhyIuAdEo6knNM1oxh1epgKAJ5wXbOVbTTrgcxRQZq_SqvIluR7bwRhS-55eMt9hEEh5DeQsqMn3iZMLH0Np0vXU7WOsxlN72_3G4XqngdIMZtFBNRMFuXQovDXYa4F7NlHNWlUST-Uo0wasdvZ-uSEbfdtZBk1-VTo0DcYA7tiv_FgVI5fX0sjg9pVMFh18TU3s5zD6bCkEI8P8SfTZjI7_KKF3kHbj4Mu9iGdNXHmZOCSjF4gwWUiRCD4P_bx_t9aWBtS5gTKFkIw0QJRsfxajH0dECcS0j3vKnxJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔥
بازیکنای آرژانتین و زیدیاشون هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/93865" target="_blank">📅 09:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93864">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گللللل دوم اتریش</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/93864" target="_blank">📅 09:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93863">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b18CuW0S_BalSUg8NBRPjwOIMbisU5_njRhGivyTOqihCNHNbBSIbDGpF9HsFuUScyJozKu9S_8uB-dz9rP-qTf6LFtf0EeDAH016w8SEpxpgU6X-hR0-ywMOKxnj1NvqfCXlAYvUhGTdUi7YDHINdXPtO-fuYDoPnB5hr2Dx7X3gQmmuWCi5g_jA7JKCHOpfEivqrti99QphV3QV-Mbq_xfSm537RLOYWd2A-A_BybumuSog2QOgcU4je4P_7Mji_nL7FGjLplpZu20owjvvbhMvZXuwxi0woN5PfG-nkT-7qZZCPzZI_ZLDsvFlnE1mywwVXyFsFk0KSiKHRzkaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«تو به رکورد کلوزه رسیدی و از رونالدو نازاریو هم به عنوان بهترین گلزن تاریخ جام جهانی عبور کردی...»
🇦🇷
لیونل مسی: واقعا باعث افتخاره که اسمم کنار این همه اسطوره قرار میگیره، از جمله رونالدو نازاریو... اون یکی از بهترین بازیکناییه که تا حالا دیدم. رونالدو نازاریو یکی از بزرگ‌ترین بازیکنان تاریخ فوتباله، ولی با این حال نفر اول این آمار نیست. پس آخرش اینا فقط یه عدد و آمارن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/93863" target="_blank">📅 08:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93862">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اردن و اتریش بازیشون 1-1 جریان داره</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/93862" target="_blank">📅 08:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93856">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SmdffhvwQPeNIb5KC6Pb8wKNOTfeQucj38W4IOnL-looOPt9KiLxpNQD5KK9-U11jNEiDije9fLvO7XVeBE3jhJbdKxzlVBIxoGUJ2Yvy3iE7FOg-G2PiFn8gFS2FHKlKkk8YeZ0wM44C1EGuLrDoNbYj1cjtwKeJZ8BE98HgsLq0aaGoX_p9OfvCY6zgwJVkryS4qFxlGU2MX9edVmf03DrZNCDK_ZJPpyrCvkiG3VHVd1x9e3W4tzDeuutzaj9oa5VMIvKUY-FIHrYYMlZ6Ec14ChzyelIB6cg-ETqhVaQKjFdkXLIJcIWCYfgJq9l-wcpIxZMfoh_VhscP5CH0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/StI96xgq6m_HXdmyLNi9yJDDpK9iX6YQKKo6Y6yi0m8mJsSAFK-SH6-NwzICiBwjDunP_rQ89S9kGGeUM9OdzP7AGRDyscbH7kGroXRnmi6Qz_C8n_2d4Zat-6PNXy96Jm5Qx-EziUr1rjn3c9gdrUIxc5zoNiI3yU1-LkiE7UsSWvEDYVsmKeF3SoW1lo2c7QXGCMIB12syHJNsybZygcyAmrexbslyJeAVSJ9MZ_LdhrHqMMHdtgVW6vItuc3z_a5TgevVNn3mg9fwNXWm3tG7cjnhA4BDbAocO1OLtuaAnK7MZXgIz7x68jJRtt0NxVXy2lQSppGBrry7pWtHxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZaR5SmowZyI35B1UMsiQfTBR2el3_pDOachdQFXenlYaSobLMUK58RVx4_Y4Xf3Z9LL6YJSF_ztFRY6qi1gnTjr2ElOXWmqiOL0ycIr9XPGARLZ4brQGYJRT6phBYI3RhgPwV_xzm2HF7mMtTxZ4ozxQ4lrLl3PamB5yN9Al2nq2_Dpzamheh-SY_d3ZJIEJUtuEL0ZtyeaGFGWau5n1qw8VHocFmdwSQnLlzuv6L8n09GZ2Ec_RRyXeC0uJudU10PFfl6ARu1ooB694W3OXkASBYGrndMfBKjuBhC7eY2nyriP-edB8303NX86DKwfRMMR80YgAw3blRbYgNAqyaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQUt6zR_krjGXoFYWpaZgbS53f8bZ0hmF2e7M-7KN_nnwk1-QrndW0pcmVx9QJGl9u5cBBW_hV2WVe0VRYISCwTLHmtl9rfgmW53J7qVgyquqXOQkbEjF0stl667IM3odcmvx3WCOTKKCEu2PWOKgRRfLLMXhMkRz3cyufwFDpa1_W04vKkws9KxkVier0z4zVcL08Ld1_f-X5RdHtTRv_PQcK-o9VG7DHkx_mStFUuqv4fvi0_w0ocQtuQCy7vsTubchlxnClPPFY7qEkTsjdFENjelOJoRSaN5nIPGs0y-NN_U8JsDuvWFYYXOMDAanP3llGMEQhLE2WB6D-cekQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SaoP03eRttsIHS7TsAO74-fksZoHvwO4DwdhY4xrc-XniyIROczJFB386J_ibFnPZCCjLOFfGfvWCmS9yW2LYcUljvVS48J76lCt1FhURCMcdfAEN1PTfISo-1Y0Wa9p2R9RUCRO-PaChl6xY7-JGINEgMzg9u64uoX84JifXOPNaHomtXo5ktkB8A1SPfgrFWGmpgUtTwPm1Hp6azwjR-pBiqgNu8wgUng-yNB937vmy-6dhCOSKHwbkLZjTmM-v3epJfNeFpH6yhsb3t45tvVxLCs_SCYgSvBZR2U3nZAGvONCnmc2FNNbic0TdSULKp_FK53VaJ3wg7ldFxwWTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KPicZCvQ9w-Zx--BjRmbH4IfUWQSPIJnAbVQJjYuZ0Aj0QGliHJxTgRrFNrSTEQo9iEGNrcXcDDSCfKfy-P3OOHgijqX_QtSG1WmLn28_wMufle3Uo3J3b6pbP89UxHw_whR6CjwyS1NRVDkFoBVhl43jH9TX6B9mEc1U7e9iqfafZCw6jJeclaQR0hagu-pTddLlP4SCHWxFX_ctxNgpITdJ9oBykFE0QUKMyOT3n6F1DsbmpSAD-BewreZKG34R1PXjF1mJGxCG6g56kbdtIqotP_aHaFfFtF1hk24ifQ3kme104mSJ35rYOdQ3Bf9ooGma-rwpT0wb_0wpUh6fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روز دیوانه کننده جام جهانی
🏆
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/93856" target="_blank">📅 08:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93855">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mg2OToyi9NCsQLSffX1-v-S6vfblsfjPoqZA-PtHmlvGqedBdUVyENfBFCUU4BuEjhR0Ifzho7Y-xTx8HRRGDfudWU3AaTsyFmXJu6O0cpC6z-bbz1WWWfI4vJkAwg9d5gwJ0tH0avV5t59MmBE9YiF6QlaTxyCFK6gWK7_qBTHsKgcTOvWXhXBx9aoiUDkNFZhbqCAVq7WXAXU5YPXqRxsAP5HepxPwQ-0Y-CB3EFebw6Xp9cQlIhfQsorQpBcpDzMjWJeqYUBpTVEhV3mtVhDGhxGlYmzPJIPjhQbbGkO9_b-jk0Y5HijRCx19g8pPh_OI1MrcupH5S5y_antRDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇦🇷
لیونل‌مسی درباره گریه کردناش: روزهای سختی سپری کردم. این جام‌جهانی آخرمه و شدیدا احساساتی شدم و گریم گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/93855" target="_blank">📅 06:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93854">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🎙
🏆
🇦🇷
رودریگو دی‌پائول: برای لیونل‌ مسی ارقام فردی اصلا مهم نیست و هرکاری میکنه که مجموعه آرژانتین نتیجه بگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/93854" target="_blank">📅 06:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93853">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gncLSwLAOh-RkgoJQC4DHcaa0BLPbIuduDjAEiwBD5iIKswypgEICNSIaklRh4feyMiPGwqjmnwydyPKVlcLvV0tdDxMyQMuvfwmPV2hw1KJtAlZC6XvZ5VREBpxzbfrEG0I-TM0n5G2rEAnJkSARS41qimQe4hehR4y-wCpxTZKqF9Vm4pR1-QqeygLCYMmIhz81LOJVJMrhF3pcJjGbN4oiR8Q-Il3A7g5u97HVL0cJt7Miw3Uf3CG7SCO36KzngJx6AucZizdiy98B0b1UNLBE4LXttGC5YaFAnHDRlLz8I_dakZkHJPH_dmw-POHCJ0kyHl122ia-4_Ftjf6kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💥
واکنش هالند به درخشش لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/93853" target="_blank">📅 06:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93852">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f19dfd3f.mp4?token=V9Ck5M7oJ0OY0kN7i6_2vW9cHE-keOuGAX6ynDWkIV6gUdMBuD1PcHNDUhO4YIKioWuAB8RRmkQb7ieiNk205NFpSU9dV73B75N512vf6OUyZwt9qzTiqhDF-2RHRA7MNoAvXzoMeGCB7fZBOk_4QUAq5niZtoG75aKPrWwLJwrK1UNh3Fgv9_rIpvU1r-Yp8U1blMMxNrgA528HHm66Z5YOiB1mNhMy3Q8gzP9uyKBl_5txkpPd317bXkYZ6HiZpns3ME158Nr56RM8o_8JZSTyaIyK9HFQXRp0AxtDlZPRy4XYAA6MysvJ0mePw-iBqgpkVyCviIR2aPE1rMuwKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f19dfd3f.mp4?token=V9Ck5M7oJ0OY0kN7i6_2vW9cHE-keOuGAX6ynDWkIV6gUdMBuD1PcHNDUhO4YIKioWuAB8RRmkQb7ieiNk205NFpSU9dV73B75N512vf6OUyZwt9qzTiqhDF-2RHRA7MNoAvXzoMeGCB7fZBOk_4QUAq5niZtoG75aKPrWwLJwrK1UNh3Fgv9_rIpvU1r-Yp8U1blMMxNrgA528HHm66Z5YOiB1mNhMy3Q8gzP9uyKBl_5txkpPd317bXkYZ6HiZpns3ME158Nr56RM8o_8JZSTyaIyK9HFQXRp0AxtDlZPRy4XYAA6MysvJ0mePw-iBqgpkVyCviIR2aPE1rMuwKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🔥
خنده‌های لیونل‌مسی حین دریافت جایزه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/93852" target="_blank">📅 06:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93851">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcGqK1FiGGBP6LAlmP3BNOWcPe_77D0DAZnQOarnHxtgA9GzOqthGRbrdrefxbaOmIQlBuh3g18BXiHZ6Mc_SmwqpY8RU-DI-lnCsVEvnhonM8QxJGuu_1P88C9bYo-y81c-0AgOhb6LQzknW9vXhhIcjcf6xVMfHZxSw0_1bRX8A_dGRnVCvAszAB3hxjUB6LmIVnmrHIqfM_jE5Z6heh51zX_er1Z_2h78Qh75gvo5Hz0Xh2-wFSXXR2xpTCVEVYtacgWfq91noEgXtmAZVpQtSA4b5FzhQHat9OKyZcWUzdaC2CmNrb4XPo2VzFblOncMXu-WBAKvq7Cz1z1hhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
✔️
لیونل‌مسی بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/93851" target="_blank">📅 06:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93850">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8uSW5ZpJ_d450B5LJgEYDOvDgET0eMnX20teEP5-pYmd3zcgoJt6DB8ZhVRwWgapt8g1P_lS0mtGdVO-NMvf-VCV3ts36FGqb9KL92jg0dzXuWzJPVgVsTK37TZG29wAAfx9hnoxRLKe-6m__UvW0_NB3mfTyuKsr7SZ-I-iKM0DIyyt0f8Yeh61X8791xM6WNDHkL-PCCQj26mNSUSLuYpHgYBvO0fcJvDZDU4KvUDe45m97TXAFT8tRF1OrRkcp7L0sfuAsuxNTMCAkY96wcKP9g3NVS990znK79YXI3aEUtcj28CgHRZYtjr1aekjICZ9aaXRNx2AB-IUIuS2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
لیونل‌مسی با ثبت سه گل درحال حاضر بهترین گلزن جام‌جهانی ۲۰۲۶ هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/93850" target="_blank">📅 06:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93849">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgQ58bS6RYJJi93tq3spFpYBrB0AhKoV0R0sW6IhKGuaWVw5ZcYsPOK4z4DXZORC_K1r9CMC9pVYM639osU71uavQk0ernft4GWwAZgbNr0oczBCW1M37NsX_MJVqmnHwgGNMYjgSHX04Ay5p5yMuI_pkMcytoO-Kfe9ZJS-a9SUkgz-9lskQ5Z4_SHUMntXVWJZF9sL-SLa4W6Q5aML7DmFCvYf9lHAximAJsLHdxlzRkaxMhb7wm0vXjlF3PyMr-9zUlTE6_KwJWOOv5CNye1yl0X2JOsFH8ELZxa85H_sV8FDqboxYkiDYRwT_EGbx9o4Ry6w4I5BOG-GLB7-Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
پستی‌کوتاه برای درک عظمت و تاریخ سازی اسطوره لیونل‌مسی
🔺
بهترین گلزن تاریخ جام جهانی (16 گل)
🔻
بیشترین پاس گل در تاریخ جام جهانی (8 پاس گل)
🔺
بیشتر از یک‌هتریک در تاریخ جام‌جهانی
🔻
بیشترین رکورد دبل در تاریخ جام‌جهانی
🔺
بیشترین جایزه بهترین بازیکن زمین.
🔻
بیشترین تاثیرگذاری در تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/93849" target="_blank">📅 06:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93848">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXvt-qDMXKbKPKIf0jvEqSdTtaDw73l0xR_4jqhoEanLQuNuz9NpZUPHEZGKHHlgoDMBc2uiWQ-jiGH6beVqqZqC23Cg24v9nwS67LbUt1WxtBZwRXqGgntXek6R8eenT_okB8PH4SBXAVHccvAHWAe4RO__r4J5sO0YBS_7D6mr-XzEyEg4J8mLs1ihdCqEd1aJjaMixMlBAuiSQ1TnaE8MGFrJEWVBt-h78sc_1DfNEtUXh9KYszxcT9v3rofec0wjpOwgIRyOHX4ez-Tr7AYd4Q1KIK5sTHdqtnevr5lDe1oRe-qd9TxqL8paXQMt9XppPe5Un-xPxZ_5hjqKeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
#فکککککککت
؛ در تاریخ جام‌جهانی لیونل‌مسی با کسب ۱۲ عنوان بهترین بازیکن زمین، با اختلاف در صدر قرار داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/93848" target="_blank">📅 06:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93847">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vyfboy4P0etuxRno_53EEz_Q_VxXcGXv_BMWx_mxO_oOFLt8OdaJ1m_ikZFjQt-Q5bhGvItwCIJykTMj9MUMyR23_PkLw6IGhwKOWrgu1WMWPuTQth5tpHg5TP0sFNM4etf1SOnenYxZoQzY-8aAjuCXyD4EPFjw88iNbqTSgsnRLyM_zyen-Q5pZLyKhswBEUerX5hI9mlBmTY2S7-SazHfag9tM-ulJzgRLudn9jMO9KhXL2ufZ4Bh3KzaQkZOcVx0UFEVhzDOQ4lhwu6wf_2AYauMacXsJYAqCpleP7ea092TNgdSWSJDjFDQxsDQWw2sTQqlvWiVplbb321qvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🏆
#فکت
برگگگگگگگگگ ریزون؛ تعداد گل‌های لیونل‌مسی بعد ۳۵ سالگی در جام‌جهانی از مجموع گل‌های اسامی زیر بیشتره
كريستيانو رونالدو
‏- تيري هانری
‏- مارادونا
‏- ریوالدو
‏- نيمار
‏- هری‌کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/93847" target="_blank">📅 06:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93846">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSjCSfhXmhGkaiT-3tazTm-31qh-N7Q9wqI25Sg-8xQvYueJjHPVXw83bnVKwiLRDmHdQ1K199Fn4sF0K6ozSOFbpGm0aobB4e9XuQYseTX3F-dRtCIJf6iEqGGvMq9miW83wI3zEtkCqs97nV3gHaRjvvl5bHd4w6yfVa9RQ9cjADOpb69FozUrTJe-AkEQZx2Iyar5elh-Zf2LzXC4hfym4s9wHZd_EKgy96C_yR2XrOacicb4TgWRWkTca9pgLZgdB2BeyDujIjP9pna5q5-p79AmMVFXn3P_5iIFQ2qd1tc-74SeyfKkxORAz93ylALn8WUzAIwRmTjRG6XFKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
پشمااااااااااتوووووون فر بخوررررره؛ لیونل‌مسی در تاریخ فوتبال روی 1328 گل تاثیر مستقیم داشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/93846" target="_blank">📅 06:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93845">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXbm3IY7m6xKtr4ARYO7zWRx0dyjG3cUIHlPFsXWl9--1uJqnN_Aty2NfbhxHF-_XcJ3NuzSm1jB_FvO_e0TrJ8L74a_Aw7tMFIzzfOp7Wrt2YDfCifKxYGFjwtJS7a_ifsRQhTxelHV3egrU7IIUs_FQSB13dHqaraaxpVZo7QcLzKoAhpYW_uLGLWmevUlcguaC2BtDLJjpxlMg7Mow8u-eKbbfc2v8xwT7v0K3rnulg2UWef3NKfoE_BcMj7_Qu3Y_u4-I5FX-vLMzJVKP8nqN33JkXC-EqBoEtYOlzR1yKhpXvu9AGYbDcgjcQdqXWucRuIbrLZ-zhuhb_rt1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|یک‌دقیقه سقوط برای کسانی که ندیدند؛ شاهکار لیونل‌مسی در کانزاس‌سیتی؛ آرژانتین در شب متلاشی‌شدن رکوردها‌ توسط اسطوره مسی، الجزایر را درهم کوبید
🇩🇿
الجزایر
😏
-
😆
آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/93845" target="_blank">📅 06:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93844">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
حفیظ‌الدراجی گزارشگر بین‌اسپورت: رونالدو برای اثبات اینکه در تاریخ بین بهترین‌ها قرار داره، فرداشب و تا پایان جام باید شاهکار کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/93844" target="_blank">📅 06:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93843">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">📷
🔥
🔥
🔥
🔥
🔥
شااااااات تاریخی از صحنه هتریک لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/93843" target="_blank">📅 06:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93842">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYtKKVC4iqVkg58hCWD-Bnr6EAUJimKGt0OLJQFrtq_Dw7DQAPwvdpc5SdZSx97T7hJChLf-hyMM8KwyFtF2xk0jSdLTMXf8flSOcC44BA6YAVk3SXsnWSEnYXa23UJGTcVdLKOtv2YFJ8ceOdTt88sjOXTM51UwhkZLcdMy_Cb1X5Xra2xgcSCsCiO5FIVtHwPzsu67kF1j1j65zaBV5tLh4SWpRaa98-waaJlS_5jfzqCubnmsace8Okx_9z8MsCF_XsgaHAdLcMNc8YCqRBQDtFqYz5gFFZBzn3DyKhntUbZlOZ2WOpu1Ro9bJxM1bgNltqjmDgeXVNjQgljYXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
🔥
🔥
🔥
🔥
🔥
شااااااات تاریخی از صحنه هتریک لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/93842" target="_blank">📅 06:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93841">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWYVxc-T1r6fGZKvU1Dyyt3cOSebZuWSKSGqtEcRrxGl4poSBuAEg3Yr823StbBQt3DHHxUrWrnw25gXakXfa6_W27BjLSmgcHaTOr51mwI_B9GoLY2emmjdMFxkW-e7gMGNE0OQJ5j4dONi8G39gFrI7GjjyM5yCwA8bwQws2HhpdMe8Wp-Zk0h28bfSVraSWKKx8Q2TnVJG_0AD3ajIsSH7rjMJZ_kHMcizH6oCsvdklq77nzai8PSnAMxMi5XoStgv6QvAAhCl2WJTO9N6ER2DuuwjVWp9l_6m6SJYqmmGC5s1r6L8B4otPyC5gAV27_fB9LKSE9eBe72kg82jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😛
😛
مسی اینجورررررری کنار زمین لش کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/93841" target="_blank">📅 06:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93840">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6Zp_S3YRokX9IJ4Oy48c4iCJDITNOghOSxMGh23fUSlL8nNvzDkVlDJREAqgzASSx6UMjPdPP-uoHDaJe781ehjlI9AWvwps5tkDqNgDAMa-kGeKTtkg_HCHAFAiQ2OiMgpBvXOrlukOcFKzFWtPBNQ6B_bWuWhDA-BdQwBl-M1xtWrNsR2k5Z8t9kqbziu81bkgRKjwqeJ2heRSaQl2dPLs-DdBKXyd9rgzbj5ROXlRlgEpn0czSLLLfFC8c5ZRjHSvmW6o3AxtPT0yAY4Zz4PURHhVjVRecakyV7tVu1gYT383h3HFXODIlA7RL9jPtaDk2K97LMHwUWjRNR71w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
همچنان درحال تکمیل کلکسیون تصاویر جادویی امشب مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/93840" target="_blank">📅 06:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93839">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrsE528QI6f4EQwc2Lb_1ss2EhyakG4ThqlmWIg_9fZGDkxVGDHLE9Gm22oQjAOvLrs6GTrgdTtWrx-izapf5rm9TZlO2Dv8Bl7rmUeBx3_XZOR_B2ly8jlzw5q-t6eXQZG403HJtgbR56DAYncB9Hwrla8SfGCrqKkCbrUynTGxZURF7x3dPm7JFUBlAwoCOLFe_WS-2vQWw_Ic073TSwS-5SdBe5QVRTkgRQoKrjKM8ST-t4bf3BsCqv3XH6mDR1MNEyor0y-tTP-bNcjsIyckkEKkFh-IIQ7m_-kDIxYt4vb5OctCnCrp2xjhT4Ilq7gDFZrhmrXT5HE29m5O8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
بهترین گلزنان تاریخ جام‌جهانی؛ از الان برا مسی و امباپه رده اول و دوم‌رو کنار بذارید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/93839" target="_blank">📅 06:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93838">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEHZidffRnmGIe2z_k1a3fc5lp7z69yY0gotfvYUBbav0MMByqCXYD9QQlRyeId8RxRScxB9VtVBg6NTn9UIsKyZ0y-qw3dwTBnS2VDGOBjgKg1GKrvW_qPq14yz2ZtDD-L2psJ6lFRAM6Ml7i0q7ewi0CMf7zp7kqUvS6CkqVnLoQUjQ9RUwjcPYObpwkKyMkEk8Az06WcbjblsH8NjVwf-aEhQ69IDzkusq-BIc29RlRq2sYlSBg9ZA2ATgB9-i6U3KKVTYVv7gxKCSM9HlaoRAxPex5tphPqFs_qSm4_3scDGMIQZhijJ5qYX-uRyJsaiCicsyBeY0VyXWOm5VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
📊
لیونل‌مسی با عبور از رونالدو، بیشترین تعداد هتریک در بازی‌های ملی تاریخ را ثبت کرد
‏— اسطوره مسی (11) هتریک
‏—اسطوره كريستيانو رونالدو (10) هتریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/93838" target="_blank">📅 06:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93837">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فتح‌الله‌زاده الان داره پیشنهادشو برا مسی آماده میکنه بده تحویل بکام</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/93837" target="_blank">📅 06:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93836">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
گزارشگر بین‌اسپورت بعد گل سوم مسی:
چطور برای فرزندانم در آینده بگویم که ابر مرد تاریخ فوتبال در زمین نقاشی می‌کرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/93836" target="_blank">📅 06:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93835">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">هوادارای آرژانتین تو کونشون عروسیه</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/93835" target="_blank">📅 06:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93834">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
لیونل‌مسی تعویض شدددددددد</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/93834" target="_blank">📅 06:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93833">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔥
🔥
🔥
شب بیداری اینجوریش قشنگههههههه</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/93833" target="_blank">📅 06:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93832">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e341d92384.mp4?token=o8tOMtMZrrfY1h7H3dTaR64vsNNkRuzVVffgHvU73xn8rGlPT8iwUyau6Pc9pOvUP9-w-KFC_7H3dIbMdFZlaquAW1ThcuAPa1iIxM_x8xSRxYoEjoeOiT_rRTaHSjMjc6YiCmPTZl_xVDVxymST1L-o0xOB4qm-ISz81i_AuYM5fxhhVV8ZItk9yYlbc9uErD0AnFURT-VoExwfry2CDS-xPxaSUA2o3izJTxb8TZaB20ZeIB65kOGohcFKoHuEeZNJTMLrc9FwnWrF3HO5KWi4Q3ylD-Gfx01hF-mFw5k6hex9LekOGGKfGH1XO5D5VIuX2ppKHwNS-tgi8LVpLbK2z9szZZLdStkIP07uIORMa1nftIW7yr0FNqfIxjF3f7FEpMtnSrZLEwA6MCxTvIS13SytZg5Y44T_f23l038Y9BvLyKXXNVr9SXhu4V33A3K34O343lY__MFbAdYK4nIFBD0-0SRZl4S_4iuVHOGdB6K7s7iuP8Zi_9XWilTQ7wGgSvFMhgyRPXp8sCya6jYqkQG7mJp92IE2BlDofDYr1YC4voSFxdyJ73nP3RS911HCdr8zSpyCjv_xaUaCtx2Z1KY9T5Kv-doGmxrR8cVcBAejYMd_atde0xoal61bUZwOGOOwcvbB8konxBU5p2-ZjkIPPu0jqnAVXVy9woQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e341d92384.mp4?token=o8tOMtMZrrfY1h7H3dTaR64vsNNkRuzVVffgHvU73xn8rGlPT8iwUyau6Pc9pOvUP9-w-KFC_7H3dIbMdFZlaquAW1ThcuAPa1iIxM_x8xSRxYoEjoeOiT_rRTaHSjMjc6YiCmPTZl_xVDVxymST1L-o0xOB4qm-ISz81i_AuYM5fxhhVV8ZItk9yYlbc9uErD0AnFURT-VoExwfry2CDS-xPxaSUA2o3izJTxb8TZaB20ZeIB65kOGohcFKoHuEeZNJTMLrc9FwnWrF3HO5KWi4Q3ylD-Gfx01hF-mFw5k6hex9LekOGGKfGH1XO5D5VIuX2ppKHwNS-tgi8LVpLbK2z9szZZLdStkIP07uIORMa1nftIW7yr0FNqfIxjF3f7FEpMtnSrZLEwA6MCxTvIS13SytZg5Y44T_f23l038Y9BvLyKXXNVr9SXhu4V33A3K34O343lY__MFbAdYK4nIFBD0-0SRZl4S_4iuVHOGdB6K7s7iuP8Zi_9XWilTQ7wGgSvFMhgyRPXp8sCya6jYqkQG7mJp92IE2BlDofDYr1YC4voSFxdyJ73nP3RS911HCdr8zSpyCjv_xaUaCtx2Z1KY9T5Kv-doGmxrR8cVcBAejYMd_atde0xoal61bUZwOGOOwcvbB8konxBU5p2-ZjkIPPu0jqnAVXVy9woQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔥
🔥
🔥
هتریک اسطوره تاریخ فوتبال دنیااااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/93832" target="_blank">📅 06:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93831">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
لیونل‌مسی بهترین گلزن تاریخ جام‌جهانی لقب گرفتتتتت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/93831" target="_blank">📅 06:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93830">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پشماممممم
مگه میشه
چیه این فوتبال
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/93830" target="_blank">📅 06:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93829">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خداااا نفسم بندددددددد اومدددددد</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/93829" target="_blank">📅 06:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93828">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">قلبممممممم داره میگیرههههههههه</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/93828" target="_blank">📅 06:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93827">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وااااااای</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/93827" target="_blank">📅 06:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93826">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">هتریییییکککککک لیووووووو مسیییییییییییی</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/93826" target="_blank">📅 06:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93825">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هترییییککککککککک</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/93825" target="_blank">📅 06:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93824">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خدااااااااا</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/93824" target="_blank">📅 06:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93823">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">هتریککککککک کردددددد</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/93823" target="_blank">📅 06:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93822">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/93822" target="_blank">📅 06:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93821">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">زیدان تو ورزشگاه داره ریدمان پسرشو جلو مسی از نزدیک میبینه</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/93821" target="_blank">📅 06:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93820">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_lg5Xf-AXwrc39TOp24waYLWSHtt5uOYYzf008fEPU9ggvSydGJwOezhv1gW1i1rozXitmoW2CbkmfyYYm0OrQwcaLNgk82Q35ImWVj0p-iw_7wps2scnNDddPwXFMfKKy5RN2yRKE5MV8a-5_aFdJ04mz4XNzLD5tFA4hj5kzD2zlzoCOc4TuEIMrrsYHi5wLPu5ehmLMNbdyA0QqxBxPmwlPGQ7xQjQDa-4cJVMnxr1UIhG6ZX_vWwemksdjg3vT6jelsVv6iUc_w3l0uiOc45HsLvTH1LhYu0K0iMlIc5UCudtkqkYFvmGLPXBjt6gJG4FT1tKIvbg3yUnQ_jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
69045 نفر تماشاگر درخشش امشب لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/93820" target="_blank">📅 06:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93819">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">داوررررر رو مسی خطا نگرفتتتتت</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/93819" target="_blank">📅 06:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93818">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پنالتی نبوددددد</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/93818" target="_blank">📅 06:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93817">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DocNbj7oVL5g4lqw1IgLUQUfYiY7y2DuTl6ON3tNXexZywJV7wsz7F2b7Ub6dB5aOi2vTXNnw0Z_T6FJyhOldBe0WMZULyXrHZTRI2XgErQwmBsyF7wtw_LV8_6XN-9IyyMrvPBFbqz0cBaAKADRY7p6g2LuODAhOnaamprSZ6Gcjj3Lhd8zrAUi0ByDy-ZRyV649gbLxWhEZXp_Ll0BRega1xLC5VrV7XKvOAvIRdgex34Z_oZVVgSQ7MMAg9BSUfZ2WQC3Mo08tKHLWWJRXP9HAC8a6WfCrheeiJjM4gMcKvawCe_vyzZyhnoL6aUqlE0yJO5M2fgoznItpQKLwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/93817" target="_blank">📅 06:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93816">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
📊
#فکت؛ لیونل‌مسی مسن‌ترین بازیکن تاریخ که در جام‌جهانی دبل کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/93816" target="_blank">📅 06:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93815">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فرازمینی
👽
👽
👽
👽
👽
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/93815" target="_blank">📅 06:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93814">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wqb4HX9JMpUKxZYmhen9sARF3j0aRczERo1X_qXnQPKTIyinr_1xYUAjeMB-_C9SnGYiiA_1JD1OQFj-ZcotGm0BJSgaZtEq4JPIVx45fr2PwE2kgc7naDKb-Uxd32HjZK4gHHueR4apoQVTPGlxHgWvEIDneR8fCpqOGZvvwOt6FyGWcLxF3mxu2cuMl6rjDa-SdRiG-Lid6DqJe0_A1fyVrPvcJ0Ssq1tE5g2kIJDppvYIc-essUI3JOrJ9iXQw1CvG8gNsRV1i8sF68nOveQ-MjNJsSNegMXzGIRBUEO-cDLZEc4DUQkN5BNZ6490qUc4sFlIvPUHEKc7aSR4GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
ری‌اکشن اینفانتینو که داره حسابی از پخت و پز مسی لذت میبره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/93814" target="_blank">📅 06:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93813">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exsyBgvP6Y9OnydYbty0jyQkn_mNaiYaFgSSGy2yB_WUTyMDT95BH85mux1DiTHcU6G3r1_gpu2xjh1mXzZAbzpWHGNLjysqhcgG1vmmIjjXNYLLpJhVH4NsqJn0nQ2EnFkVXj4WFTyhIX0W7xJmvCvHSCdw6uacnx7658qFbtEN45M_H3-2vy2kN4Anx4B5t05vMDgwY0UYdWdgDs-RjtMw-jq26bEgqUV-vPRpSDaON8jena25zCfsGF0xwiRT0P9ibYnjp3oV7eVJc5ir9-vjDyCRtEG7pESFwLi44SBc_QxDg9QRsaECrXZ00-uxHoAimRSgvTj36dV7A8S9wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرازمینی
👽
👽
👽
👽
👽
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/93813" target="_blank">📅 06:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93812">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گلر حریف نذاشت مسی هتریک کنه</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/93812" target="_blank">📅 05:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93811">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/93811" target="_blank">📅 05:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93810">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🔥
🔥
عامر گزارشگر بین‌اسپورت:
"خدا را قسم توپ چشم دارد، توپ دنبال مسی است، توپ به دنبال مسی می‌گردد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/93810" target="_blank">📅 05:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93808">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b0f517f71f.mp4?token=VtlPb1qhcTYgRokRV7wzGSCoA12HpMIIZaBgFHYTAIhvKZ0sHDilJwAc80zkG-BkwHdU8Lvk113IQx_5Mm1nLX7I8KxBlNAiPH9NsVq7jW5lQb90faodg0xkg_OKpYP1L4_vgEoPdJs0npWfHnIx-8ssIZPONQ4mc43WkSfVoS1FnA9hZyCiQ1g4quiG8do6owL_E0VpcyC1crFrWxkuuJQjLnqJ-nTLHW29vnIkZJdYSN-ziyHl4PRai2ACrGasBTEtoSbemESDbfQ8xBUBn-fwqgYI2lGGcBA50g0jypviCoYusEfZQAjwSYo4_37QYoULR-iDVa1srEkYQ92dIw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b0f517f71f.mp4?token=VtlPb1qhcTYgRokRV7wzGSCoA12HpMIIZaBgFHYTAIhvKZ0sHDilJwAc80zkG-BkwHdU8Lvk113IQx_5Mm1nLX7I8KxBlNAiPH9NsVq7jW5lQb90faodg0xkg_OKpYP1L4_vgEoPdJs0npWfHnIx-8ssIZPONQ4mc43WkSfVoS1FnA9hZyCiQ1g4quiG8do6owL_E0VpcyC1crFrWxkuuJQjLnqJ-nTLHW29vnIkZJdYSN-ziyHl4PRai2ACrGasBTEtoSbemESDbfQ8xBUBn-fwqgYI2lGGcBA50g0jypviCoYusEfZQAjwSYo4_37QYoULR-iDVa1srEkYQ92dIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
دبللللللل لیونل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/93808" target="_blank">📅 05:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93807">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گلر کسخل الجزایر چیکار کرد
😂
😂
😂</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/93807" target="_blank">📅 05:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93806">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دبللللللللل کردددددددد
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/93806" target="_blank">📅 05:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93805">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">جووووووونم به این پسر</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/93805" target="_blank">📅 05:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93804">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مسیییییییی</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/93804" target="_blank">📅 05:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93803">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دبللللللل لئوووووووووو</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/93803" target="_blank">📅 05:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93802">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">آرژانتینننننننن</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/93802" target="_blank">📅 05:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93801">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گلگلگلگگلگلگا</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/93801" target="_blank">📅 05:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93800">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z393tT1-N4TUXDJmAsp5YdIOfp12gJIy6NdgiE2MF-Py5rYpYkzHMsuKFuoX2pMfvq7NYxq29bcK9LZlqRlgwYtnxTvHLinTtDYe0_cX85QneUh7A0jhrgvdT5Cf-iAU-vgUxDnCR4ku8skrM25D0eSLFwyn2O4qwYwUumdUBvkTiwko2ZZIIprPid3FHgBijHbNWbTE4siQAvcV07lcegekhSvGTdT0ciXAFFGp0Zgsilf40PeN7nGKFXy_n1azGckKivbyBpeSeo6NUYfs18O4hSgeURQgOKK7MCuXzzSrMK8PtNY6mmSrMbHoQVADj0YL6xiJnRsOgYfzelFGfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طرفداران نروژ هستن حاوی نکات شدیدا ریز
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/93800" target="_blank">📅 05:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93799">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آغاز نیمه‌دوم تقابل آرژانتین و الجزایر</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/93799" target="_blank">📅 05:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93798">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ecr9PJZPeUfR1vxkjr2A24BXG1wxdRY9T7l52wXsGbtiZ4vHi4aSTizTrkvX-Kl11QNKFb0KorsZn5RQLyDX2f165SNIJrLDr7_GCudscPJeiQF8iIR79QjCqUzhCwO6UA-HjagVg-ZEtstOqIBViMnoQ6BnVtE3TfzV-IgxcokhhnfdHaj5yQiqfy_3FSN-CXTRQPxAgEFAUHbXU26BIpZLEkDitDTzctCbgD2S04LAyHoVa0Qh3i1EEGK7YeBkYOQILPZUvOdGwLY-Q3FCOioZt5b7haQOrQaNUJf-iGPALut14_42dLwKcruXe25cMWlg3oBj9CTy_uwAVqIs5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
#فکت
؛ مسی اولین‌بازیکن تاریخ فوتبال که در جام‌جهانی به ۱۱ تیم متفاوت گلزنی کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/93798" target="_blank">📅 05:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93797">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔥
🏆
🇦🇷
گل‌لیونل‌مسی از زاویه تماشاگران؛ از نور فوق‌العاده خورشید و جمعیت مردم و شوت تماشایی یه قاب تاریخی ساخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/93797" target="_blank">📅 05:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93796">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9REkFFwNFkCQMkD9ZRmM67i4TELcsH0vztR1_lfzb_7px5aQ2QMHkAF7tQU3TrlZOJCc-08ld4oVrfeTu6haYo9kGBtYyKQetTWG791on4xXnqC3_3WTSZ1HMxd9twX0O7-IYxkwDm89eckEf8EmWFxTEMody-EtndCxFYDW6Xjo84we5PoSg_R3D06_uCE98H8iFBxemGUwp-3Yeqvoth-xiyfe_y9viqdnel0WgduUPHtv7PWJFVoZyweeplg3ijhQ94o3w8RlBMEQjNH14ZQXEbXzpBf2xLVcvuab16SEb4cP8V3WEiouxI155K3vZBGIPxr2GGVp7OcMXKwMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
💥
لیونل مسی رکورد مطلق بیشترین فاصله زمانی بین اولین و آخرین گلش در تاریخ جام جهانی را شکست: دقیقاً ۲۰ سال [۱۶ ژوئن ۲۰۰۶ مقابل صربستان تا ۱۶ ژوئن ۲۰۲۶ مقابل الجزایر]
لیونل‌مسی: ۲۰ سال [۲۰۰۶-۲۰۲۶]
کریستیانو: ۱۶ سال و ۱۶۴ روز [۲۰۰۶-۲۰۲۲]
کلوزه: ۱۲ سال و ۴۰ روز [۲۰۰۲-۲۰۱۴]
لادروپ: ۱۲ سال و ۱۹ روز [۱۹۸۶-۱۹۹۸]
زیلر: ۱۲ سال و ۹ روز [۱۹۵۸-۱۹۷۰]
مارادونا: ۱۲ سال و ۶ روز [۱۹۸۲-۱۹۹۴]
پله: ۱۲ سال و ۵ روز [۱۹۵۸-۱۹۷۰]
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/93796" target="_blank">📅 05:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93795">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d0967a51c.mp4?token=NLhmJ84UIq1iymHvv6aqkPEP5I5rrXB7uz_0x02ofBggNqZanmsrrOw19UvYdt-Mn1nwQ-Mptv6Gf4gWfLyq5HEXqJLWUCmFteZUHX1cRKwijWWRSnnjr2inGbBSvpcr9ThduNQ_ddLqhPcHhW2eigFTjhtSk6eQeodJgaClxBuWYXHAb1AoSl7c8DLlm1iEQLt1-bKPWjHPuiJHe6MwXLx2E5VepHCN8SoM_olcvOVGvrdcPm96A0O2s-8HSMWigIIAJIvVL5Msf8nW3gLsjlMijJWCNF0dGDqcInhmyJSEbkg7I4eJg3tVC4oWNdUyCAu2kA-2DhP4xxBbePprWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d0967a51c.mp4?token=NLhmJ84UIq1iymHvv6aqkPEP5I5rrXB7uz_0x02ofBggNqZanmsrrOw19UvYdt-Mn1nwQ-Mptv6Gf4gWfLyq5HEXqJLWUCmFteZUHX1cRKwijWWRSnnjr2inGbBSvpcr9ThduNQ_ddLqhPcHhW2eigFTjhtSk6eQeodJgaClxBuWYXHAb1AoSl7c8DLlm1iEQLt1-bKPWjHPuiJHe6MwXLx2E5VepHCN8SoM_olcvOVGvrdcPm96A0O2s-8HSMWigIIAJIvVL5Msf8nW3gLsjlMijJWCNF0dGDqcInhmyJSEbkg7I4eJg3tVC4oWNdUyCAu2kA-2DhP4xxBbePprWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
تشویق شدید لیونل‌مسی در استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/93795" target="_blank">📅 05:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93794">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🏆
پایان‌نیمه‌اول؛ آرژانتین
😃
-
😏
الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/93794" target="_blank">📅 05:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93793">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDHYr7C4W6enVkKZGlAqrn2juDye3NEykR6aXw_EZh5haIInddm3D9y8GAtM2Qa5TZ9m8eBZ-XIvaFszSdr2u0Rtxur5HzyD9tGlHTr2taH7NpK0TcqNNd73L6XAcF_2sZGeqx6rwUv0kSAAIimYGsAUUt_3KCzx5et_yeqRkNYKmkiap8leUfSCzO6zkQTG_Sm2NWKbS5l0rYmPXGZFZWAFG2HMCny7ly6G5aLrAZvppb0LjIKj1nSiNhR-b0kkPaSaIxvnIK2KS_CF_6vff0ijUYHlWIbeyDUB3EcSKRvvFqwTkZBnyT8vlfaSJOsf0EOKIQ53bZEPPUawQ77IrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚠️
#فووووووری
؛ آرشیو وار: کمک داور ویدیویی اینجا در آفساید گیری اشتباه کرده و گل الجزایر کاملا صحیح بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93793" target="_blank">📅 05:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93792">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7J_C7XjylhCtF5IEiKPgmmq8xsuDL33kWMbSaL6UYD6TgjSEEtc_yWUeQuMV6UKR5L6JJxrkz1mzFlZQnubU4vQy9M7l2pAoCwjd5E2Y4ErG7XG6aTdC9YZ_dyW1cSFcaCyAXsvITJxRiZOPQWystln_aQ8kBvjG5KffIvALKQ8L7KpzSsY2-8grZya0q9fayGoYbjJqVAXS0m4zWc7bQUJKjF9GvPYwrdzf50d0-hIo1T9dVxqcabV3dVxtN2AXhw1yW1uNdP1D6rIkwzMpo9lRA3fY_9tCvZ6ncRNw_H-A87vnGpijGdVQTcy1UK47ezJuxvtjz0XwrKBFYFX6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پشماممم مسی عجب شانسی آورد که تو این صحنه کارت نگرفت
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93792" target="_blank">📅 05:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93791">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EzmWP1uCUaN-HM8cpkeCVrbJ4nEdFDFmvfQVcUVpTo28ke-39_ZuDuSq8gNIZXvbfiYBSyNaxqJ1uHgTORy1KzWBJ2aliHdzHlb4GDtGn-jPrJn-6UAuBvmbOPbZjoILChSQFrh66k_9VGSg_i0EHrgrGVZ1IZGdeLlp8ufSUbTpbISmTYBsevFbKOOpHEhGKNPOWPhY7J9wQPZo8b7f00hUwfM1XvzGNMYPWB19y3Jlj5GiD6YMp20TzTkc-2pOJ3l7wv_bOQEeoMH8bBPvh_BMDYr6OZFTNNbBy-ei5YAmqR6_5cDcaNzaiK-WEfpFnc5dolOfV3oxcGSs9vP-1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
🇦🇷
لیونل‌مسی در تیم‌ملی آرژانتین:
🔺
۲۰۰ بازی؛ ۱۱۸گل؛ ۶۱پاس‌گل؛ ۵ جام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/93791" target="_blank">📅 04:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93790">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E61pMxvktq0Xijnm6BA9242IMbC7puh5tcdDRyzRVb9OUaI0haxk7Ff-3KKLY-lVpfxlA6PCV7ebuypb9Zxd0xWtKl7mCwOZujaU5o0FHV_kQZmwxofarzKSFG69Um2NkPtnhqWTommPmqU_Iqi9AgM56Ra6xL-6qI2q6gfynWPFitNkcDRj9Y9vQ5-8qA-_NJtR65oHLheDv_dNJSQGrhL-3GfS4YXpCcvoqSM2aojDPl0ru02Zy2_Fz23Zg08o-5XFb4tF7KwQJjapVl9PYyVRkbJe-EHSN2f7BEuTeZEnqWZSxlc_sgn5BGP-4AZVekPnMFgfYvDPcKu2tAXCrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
دومین
بازیکن تاریخ فوتبال پس از رونالدو که در ۵ دوره مختلف جام‌جهانی گلزنی کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/93790" target="_blank">📅 04:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93789">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">عشقم‌ مسی عجب گلی زده
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/93789" target="_blank">📅 04:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93788">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExwmHYDruwSQjPopT1O_7LQK1QxtlhP5g61ygsqjnyR1pMfJL7am7jh9GWo02bSNYdvL_L7wnCoiYtH75UGx-9BOTiSkJ7FqZceYZ4faLxeu1OzCvgmJ2JEZ6rOglIUCB2A5TuBg5gSYOAxvVlguFg7CX8Irr0a3JETRybNFcWx-tDy09i_fIs_WzyV6qz28BTBoeusbEMa-PZZrIauQ5hiMGYoEPEtpW3s10CBFV7iw8yWuuJzs1WOxA0oH6nWec-_OzyDdXwqX5e1010DWACSc52g12ZKYjqceGIfay8g7ijWsjV3KC07ky0vcwPhebrJurM1uSO7Vj8tBeQgM6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
اللللللله یا مسییییییبببببببییییییییییی</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93788" target="_blank">📅 04:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93787">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🔥
سوپرگل لیونل‌مسی مقابل الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/93787" target="_blank">📅 04:53 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
