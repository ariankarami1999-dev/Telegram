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
<img src="https://cdn4.telesco.pe/file/LqoIAsZGMD8vZ99jof7rp0L3ax0M-39cYYtbHvnw_sQ35tuiiiUPqA2pWX6VbLz0WXvFh_0_Rtqmp9qq0X-OVXWFWXtmWz7f8FIP4SHOKfd3u7O2ytW4fNEuY31Yf-HiLcQxSYejPdE-GptiYVhC7G_N6645GnTibJf-lk0b__g_rtfN2OrjHSdCSrSdp0zB88WFlKJbGa4iVBbygBlo2jqvgXAbepptdSkopjCiNpBpqMxA5jZzfX-BqJvrpa2U63jTmwaFej-WHDHaqr5OXkt0XYkQK8-J3l8BUlQV1p21FcY0Sp3zuhnm11e_CMVDMB86XF4daJuLZdm_bB7z5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 165K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 17:23:10</div>
<hr>

<div class="tg-post" id="msg-90715">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5iXHd1wXI96Rrc0JUuMTIdF-LIvOwlw_FjWYaJKEDsa7zAK1KZHChV7E2A3xJpvT69QzLccXNkMwXIINEGe8yw7snAzqUQyG4EX5JJcTGSAK3xGLMelYZPn8Rb1DZmpgvxLpnrjW4UryIpG0VFT5QCtgeeXuMmp0TQgK03FmCasapLskWeUjda5zJUmib2Zvml1mErENUHRhWxV7L0GMJaMzNNsNgqEOjQ-2ySqxRiHbQn0rqCh4DKgBXt9xyKYf5Vr_NTc_R-DSVw83YJaSunryziQfXhtdkSYZmuWOTLsGL7B7rBw7SB2muYbSNy3dJd3Y58UgyxK7Hv7fhCISw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👋🏻
املیانو مارتینز : اگه قهرمان جام جهانی شیم از فوتبال خداحافظی میکنم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 736 · <a href="https://t.me/Futball180TV/90715" target="_blank">📅 17:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90714">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-GgQO_MiscPwLchJGroEcfZIsi_aWLbfYP5l6z_JcFAJ5Dpa7EYZnw4IB-jZf88F7ABxZH3I-Jqb5sjCseT-2er3LwVbrePvSIBENf3z5xOA2GgfHquxIWX5JXPBU5dWsDOnNvaHi33Gnbpv2CKc21cqaaspEdTdu9Ok4V-Updj26qmA57aP_Hknrs9ZS8D5bZKwFdErVe2Bit2CyE35bdTzQEeln0MjgSUZZXB2y-2Ds34eObiOKeuPBFg5GP4GMkwsFzmOaSHcd1SG1C9IMKZp2ih8sMAqks43Bzjll3hnTFyMn6TwKoZBOFtt2ZTYTnbEcgYhUoYcGc2JgIkKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#غیررسمی #فووووووری ابراهیم‌کوناته مدافع لیورپول با عقد قراردادی ۴ ساله به رئال‌مادرید پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/Futball180TV/90714" target="_blank">📅 17:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90713">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe786fd544.mp4?token=IySIYBiABO-7W-mi5W9dPDNb3xfYUQYR5sYpkdhobQZLB3fUCgWe8L-K0z6-VnT4--O0uIjyVQSnEL0J04doh7O_ztCvd09cL9OkYd5fnjtr4HsFKe_hXEH1WBKqhRV6lco8QsuCygBG0Lf0eRfrPgx9zV3I6lZyjkW6gq-HN1_Gpgnf868llsZGC-y-x3NVhJHVVZCe3m_nvYcRWvdQd7GVkFXRrEffcFGkffQdTynr37BrJ1Z2JVHIvKBvRPCYdcZ4BtzVAngyZED77WFTdzCkYV9yEMNtBEvUdcgR0S6-1J0j8JwX9QM8JE_OIIqNmdxLYKKvYiTMIKGPIdJbvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe786fd544.mp4?token=IySIYBiABO-7W-mi5W9dPDNb3xfYUQYR5sYpkdhobQZLB3fUCgWe8L-K0z6-VnT4--O0uIjyVQSnEL0J04doh7O_ztCvd09cL9OkYd5fnjtr4HsFKe_hXEH1WBKqhRV6lco8QsuCygBG0Lf0eRfrPgx9zV3I6lZyjkW6gq-HN1_Gpgnf868llsZGC-y-x3NVhJHVVZCe3m_nvYcRWvdQd7GVkFXRrEffcFGkffQdTynr37BrJ1Z2JVHIvKBvRPCYdcZ4BtzVAngyZED77WFTdzCkYV9yEMNtBEvUdcgR0S6-1J0j8JwX9QM8JE_OIIqNmdxLYKKvYiTMIKGPIdJbvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
یه رسانه فرانسوی با انتشار این ویدیو از فرصت سوزی‌های بارکولا نوشته که این بازیکن جقی رو باید رد کنیم و یکی مثل آلوارز رو بیاریم!!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/Futball180TV/90713" target="_blank">📅 17:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90712">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPcnPsWhHIwmSqI9OHJse4cnUzGDc4MKuVC2MpMgVcXrPDwnyRwTlohPqPzE_cBkNYcSSfkTePBhB5OF5n7x4M5DfydWdBspbiarcHs14Lko1zkJbrQD3HsQSLEDwwuzKLEufzBwqFtujjgtqfink3LnuahPeISVWtxAk8hEf69Reay1AgOJZICVEmVp2vWO8FouKCBtp6yaska1SGZWr-O9mvHlj91gKTV_2WYWwvffEWWop6wdy9_4KGrgJsL9XbqBQhHQIYsE5fIVXKA6aowxgGajNi_MRrYTW_bgAp6zS0D6Cz52c0bf3eiiszwnTWPW0mH_qmA0JawdWshAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇵🇹
شماره پیراهن پرتغالی‌ها برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/Futball180TV/90712" target="_blank">📅 17:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90711">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQzn0veKxetOP9LYhWaBNnkJ4sQ3gIrLHrKZ2ctRqfB7aSonNm7v0sX7gRXk0Nf69o5exbcu1LCAaQB4fjshIjdNd8zCiIjzh2O6OyYP9o0FXH-GiZ_GH3stgB_9uN1-kGOORdB42rrxGbN4cb999ouA2jfjlR6eB2nkGP_kMGz_okYkZSV8G7ZUDKS9-b-vTpMIdWO5hbSkfQBxIp1GYxmHSL5d_ov5Dy1Pp-wd0TVK1H0F7t8IRzSdyBIWVFK75smjZlD8iG9E0wksn4MPFUNsC03zehRdppK9njc9lCpV835JAvwwb1eNXd7JLyUNIGN0b8t2w2hJSs_sEaJ_8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
نظر روبرتو کارلوس از بین نیمار و وینیسیوس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/Futball180TV/90711" target="_blank">📅 16:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90710">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/805387d840.mp4?token=jL-G4bHJaFFWNCLdJgUA1JVCK-igTTjb1MDh_7ShTpqbgR0zC22MiRnPt2PrAi8ftiHm6ZmdetlNGc8TMUSGR6n0QmnAy5mnDV77YKHrf5ad629TUDu0eVExf8dmjFPWukhjvzHhOXRLnlDPqsg08Id80yhMKe4LRdS6TVeV3e4XgGyHaV0lDHVNvyHeLU-V5UzH3jvFzwBTKiVcWeYQpk4Ks9NeaXGtFo3l522quL8Ibs5aKGLv_633WzUJhAXwoVuoFBp8X2lq1-1_qUKh5AwvJMyjaQgUpw528svexsGvVZlvtfWMbvf9tqC-AUn2851vc_tTTq8mGFASb1drr2fDqaF6sJe1UBStu9kZXML3S8MCuvfZOFihoanRzI7N7yfQEXozdBtSFD6AZFy_RAPpR3yAjYsG5ENt1HhNPBYT7AHmZhERJbqd4mYWdgpQ75zkiED9dBBKbZK0t2PH_DcCoi75VkZjWOAtZBGwHCXLSGitD9gA-zCrWhYD6J1dNrCn1iSYML8xGxCZk-bEGwnsCMrr38nb_WNsVae2avZMxuP3CJxPK6NZa-4ImsZBKfKAr2jWbtXNfe1B8YWt1HSEMtHjR0CDpXzUr-u2ybbQg_o2gt8sAftExiehkojn04XLpNjSaEa42z0ET5l5UHVZhJ1o65wwwqrzdB9QpYc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/805387d840.mp4?token=jL-G4bHJaFFWNCLdJgUA1JVCK-igTTjb1MDh_7ShTpqbgR0zC22MiRnPt2PrAi8ftiHm6ZmdetlNGc8TMUSGR6n0QmnAy5mnDV77YKHrf5ad629TUDu0eVExf8dmjFPWukhjvzHhOXRLnlDPqsg08Id80yhMKe4LRdS6TVeV3e4XgGyHaV0lDHVNvyHeLU-V5UzH3jvFzwBTKiVcWeYQpk4Ks9NeaXGtFo3l522quL8Ibs5aKGLv_633WzUJhAXwoVuoFBp8X2lq1-1_qUKh5AwvJMyjaQgUpw528svexsGvVZlvtfWMbvf9tqC-AUn2851vc_tTTq8mGFASb1drr2fDqaF6sJe1UBStu9kZXML3S8MCuvfZOFihoanRzI7N7yfQEXozdBtSFD6AZFy_RAPpR3yAjYsG5ENt1HhNPBYT7AHmZhERJbqd4mYWdgpQ75zkiED9dBBKbZK0t2PH_DcCoi75VkZjWOAtZBGwHCXLSGitD9gA-zCrWhYD6J1dNrCn1iSYML8xGxCZk-bEGwnsCMrr38nb_WNsVae2avZMxuP3CJxPK6NZa-4ImsZBKfKAr2jWbtXNfe1B8YWt1HSEMtHjR0CDpXzUr-u2ybbQg_o2gt8sAftExiehkojn04XLpNjSaEa42z0ET5l5UHVZhJ1o65wwwqrzdB9QpYc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تبلیغ جدید مک‌دونالد برای جام جهانی با حضور رونالدینیو، یامال، هنری، بکام و سون
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/Futball180TV/90710" target="_blank">📅 16:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90709">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkxJOnWPi69M8mcSg8qaE4i83i4A1fUonKJehMVXqd3Y73-_CtaSnXgf87NBZsKpzpJKuuhWDHJjBRwHZXyvlMH8CA7F2c7Nls_enMQ-Y2owZ9YgDyvYg3r10sb7feZZqFJlBwziowV6cGtRZLkgQjFyGwtJsOyRbEz4SWs1TZzLkkcx8w2gEKnTRZmmhSG56vMXVjaj29pJAavHSInO2M1UPCLUGHZXD3Ke80ZgkZpyCV2CQfLGbrt5HlWurTC_97bSDklL6S1Aq3bJIlwum4J9k_cW2hF7LeIr7ahHN_nrmt5uBt2kWNNmM9DLTqoTNDNfCFtITq9TTem-IPRHTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
#نقل‌وانتقالات
|بایرن‌مونیخ بدنبال جذب اسماعیل سیباری ستاره فصل آیندهوون هلند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/Futball180TV/90709" target="_blank">📅 16:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90708">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FH6-3A69Dpaj4cTZOegRpCFvydxe7e73kogpMjg9Rc1iVIigtj96TZJbO2BpbeAeBBVbQWNLY8H6fUBbwlAySKrhhwHn_x6nD0cD2MhorRRYGDac_YB82A7xYy-o5dq4bOO8kpzAml-iSRYzC3G2vMYrBdMMpOj_6g5VpHpcO2rwYjNKky1YwZLAtfjQIO1u57DzgPu1GfWXtNAr8qLzJMlEfPQFUAieixwYXz0xeBMPuPEbkJZUQgn6QfteSqLhXj1oVHgB4ymmhS1wZAaH2Rh8ehrVx-rxRyuK-84y8e7MH1H-1inDM5Jf0979wXOthbWjeUVwXz49AS5rYMtZbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#غیررسمی
#فووووووری
ابراهیم‌کوناته مدافع لیورپول با عقد قراردادی ۴ ساله به رئال‌مادرید پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/Futball180TV/90708" target="_blank">📅 16:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90707">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvcUt0f_Na0WMonfcZkzaQre9cJNcdtX5k0b9qXP2v24z83u93Ewnr8xTQiCT50Mp0v4Jp_E9GzW5knqY0e5-XOlwFvB77Cr0kXjiuRr5kPhKx_2b8fsODbxtbKM472pfyutdPhXuiDkhnGmBdYm70aKVEwtxnqa3Ukje0iCVYqdFrynv6HFT4Ob3Jw2R-hDe9j8Dp4NT6_wSgsytcb5ZkKKKfWqH3as56zIwvAbtgWAu_qCSe34MkuX4tSNYZoHIJkr1dVrlDgHeA1L5zmBuBsLdlMBNblRfXmUn_o95rGiKwZ-p87dw3A3AxhKTbOY4f-FSYJgNl9I6w88IFp5Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منتخب فصل لیگ‌برتر انگلیس با رای مردم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/Futball180TV/90707" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90706">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDxTbqA3XvG-dHuPTrefV8KcwffKkPPQLTm0vaBe99GUQH7HFI7TRG27LXD7DmlIyLkV77SfzRmye1AweByWX_FPzQMtxuQp51GHBsaHRqfpN1NPwpdaz2V9ZVk6iT2LDzib9MewT3BWza0duFNBgp0tLaGT7wPAfEnZ9eJDxu0c3Q2vnhb_xdJXi1LwA5bI-UY6awPTwXT_xgYVqTxTq0hG7gSG4MgEm56AUvwvDPAL_bFg3rEwT5ELCE1lK6SoPDT6c98CSiOQTndXMMUVujzzw-Tu9u_OM8TTgRUAgqw_tZO-_k2Gm7qmy1xkLlii3uhhC9dnqgasikv0Fy69Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😊
عمر مرموش ستاره سیتی هم رفت قاطی مرغا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/Futball180TV/90706" target="_blank">📅 16:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90705">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWAv0uNvWnJ8f4oSAdbspK4XLW-BO9hjrhQBSU4-k9pv4vjrHZUJnHXY4e1S4PPvGhvDgLF6wJB0Rm-LSVVKJ2hb0x7my35D6MfqCKc2ieqR8jRxUUD3BqHsKHF3qDmG-YsaOme8mt2B1gQ3wvvhYx1lZOGIXYRqiOew09QrxtT2fAWYTR0DnznK_B4gIWdw9qu1xgefFbhV7MXR71XTvJTvr9OwljBsotQ5smXEizp2zXi8sKC0LiYmifegOvxl559P-zH3YdcSyMFZat0tsMIGug0LH_2kh7BM-dFb-ZnU9zRLjO0EETgODZy25rZgrRabn30cUvmqppFfg5-R7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
طبق داده‌های سوفا‌اسکور، دیگو مارادونا در مجموع ادوار جام‌جهانی با کسب نمره ۹ در سال ۱۹۸۶، رکورددار تاریخ شده و‌ تا امروز هیچ بازیکنی نتونسته در یک دوره از مسابقات چنین نمره‌ای رو به دست بیاره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/Futball180TV/90705" target="_blank">📅 15:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90704">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/90704" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🔵
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/Futball180TV/90704" target="_blank">📅 15:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90703">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/Futball180TV/90703" target="_blank">📅 15:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90702">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDA7XIveJRiSNTQqMbnXLPpAlIpDr1PQAv6j-ucjg_Oi_0fmDHaslAEJn-up_owPY1cFixMUErvVF1C23RlemFmwm45qALoHfp_oD6CYZuq91tYjqp0TebKZUMg4l27APdPQnSUTgAGrDiiHIQ7yKuH47ellkMMz1M6ehB113zATrN9fd6bIJzHv1eZufUzZLmYIi4KiBpX7U06hIihayzOWbS68qGemjiA7uB0Sw7c1QbEf76JQH2w7FSSiB5UE3SevxKjZ7YYGKVkWONofRH7ZU79SWvNwjBoO0TGLxLjSfdV97VG9RK0f3311lKGdgCHHm-F4oOEL9a7oLoJZAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
👀
اتاق شخصی لیونل‌مسی در کمپ آرژانتین؛ مسی خواسته بدون هم‌اتاقی در این رقابت‌ها باشه و از دی‌پائول جدا شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/Futball180TV/90702" target="_blank">📅 15:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90701">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b52d4c89.mp4?token=HcX7y1Ln5YN7qRsUYUnx0-BpUgUwnlLNS6MfpnthV7YGAlChOYdI6aUmR3HgO0v2cicK4ldXfkLD03ISD6wdqN-AgLvhF0kX3DqKfOxcWqoug5X3ZGfbubZZ1C9X6WAtCthCCUSgr9L-BHq6AMPW9S4mTqOtq4bpGG6EOIrNOOiN-Udmh4YUiZTEJu_HuZ2tJdxkUn_OmPl8VAaDS70OWAoWiSdluQl_TVYZTwaeAOM4mKTbIx9DsytKBltLdJsQve5wjdE97ol4nUaPAJ_Np7O-CpscjUuq1TbN3omnYbkNWuab7wIh2Hnwl_eaZkNgslSVV3l1HlgwFbTJmogNtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b52d4c89.mp4?token=HcX7y1Ln5YN7qRsUYUnx0-BpUgUwnlLNS6MfpnthV7YGAlChOYdI6aUmR3HgO0v2cicK4ldXfkLD03ISD6wdqN-AgLvhF0kX3DqKfOxcWqoug5X3ZGfbubZZ1C9X6WAtCthCCUSgr9L-BHq6AMPW9S4mTqOtq4bpGG6EOIrNOOiN-Udmh4YUiZTEJu_HuZ2tJdxkUn_OmPl8VAaDS70OWAoWiSdluQl_TVYZTwaeAOM4mKTbIx9DsytKBltLdJsQve5wjdE97ol4nUaPAJ_Np7O-CpscjUuq1TbN3omnYbkNWuab7wIh2Hnwl_eaZkNgslSVV3l1HlgwFbTJmogNtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇺🇿
🇨🇦
درگیری دیشب بازیکنان ازبکستان با بازیکن کانادا بخاطر تکل خشن!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/Futball180TV/90701" target="_blank">📅 15:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90700">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pavh5YPBqcENEAvAPthc5l-QINzw4LmyqWG4S9rVUBthrObI2e_z41rGMGgs4743eHBAOFFShMKjFYzd06Z74AZLx_k1z_B3KG8lBLvwvKN8lMp7PZ5pAApyDrR0_pmuvYRQNfVVbzZUWqJokzmSMOKwSSsujx9aNG6bWHMMP1RecCoVJs1dYdyojiJwt7SKK9ftpBK1WPviLETesxek-U7BHDnTDry7wJ4N146r-YT9rtEYgTWjR5zepL4zKqMmdgKjQYHjFd1jbTBY4l1KL-wMtRFOrcL5CsxfxSJ5cPzjH5CQZK-fULW9T5e8H60RZN-3dsUGowGSElGwF7A0Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
یادی‌کنیم از سال ۲۰۲۰ و شاهکار پدری در سن ۱۸ سالگی که تونست طی یک فصل ۷۳ بازی رسمی رو بازی کنه و قیافش به این شکل دربیاد
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/Futball180TV/90700" target="_blank">📅 14:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90699">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cab41e786.mp4?token=laWTSEP_uTDwWmXoi7pHOdK9GKid43haTNkZyclOiOEbaaz1UXFpyiNR2eCuHM-mi4TYYlBN1vRX9FdaIGp1S59rT6ba0S3h4aFFTBUaSkXxu1X23KFO_e8X5lYtkKEzybZuWE9m4DAQkJ66bcUen_q472LFotYnIEjpS364zrCMnEGR6CaXcW93zBiYcr-KOyVg7PmvdWcdVFySeZqZFh7NIDMlyy1Ag7lnOee9L1uRLjwhr1lIWdenqAilUaQJhJwaT0X05Y_Cceo0RmIBLiViCeR6_RrdDO4D69NdEdd0bTgJIiMhiTxhBd1DXgjAlSe6rnTHM599AYQlMUP8Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cab41e786.mp4?token=laWTSEP_uTDwWmXoi7pHOdK9GKid43haTNkZyclOiOEbaaz1UXFpyiNR2eCuHM-mi4TYYlBN1vRX9FdaIGp1S59rT6ba0S3h4aFFTBUaSkXxu1X23KFO_e8X5lYtkKEzybZuWE9m4DAQkJ66bcUen_q472LFotYnIEjpS364zrCMnEGR6CaXcW93zBiYcr-KOyVg7PmvdWcdVFySeZqZFh7NIDMlyy1Ag7lnOee9L1uRLjwhr1lIWdenqAilUaQJhJwaT0X05Y_Cceo0RmIBLiViCeR6_RrdDO4D69NdEdd0bTgJIiMhiTxhBd1DXgjAlSe6rnTHM599AYQlMUP8Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یادی‌کنیم از روزگاری که مجریان و مهمانان ویژه برنامه جام‌جهانی صداوسیما برا خودشون یه پا جذابیت خاصی داشتن و کلی مخاطب این برنامه‌رو می‌دید...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/Futball180TV/90699" target="_blank">📅 14:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90698">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJ4y463bljzHUmT0dBDAf5UgR7Ys5ISwZTHy95n6dubLJhv81jV77FrCJKQhFi5qpqsfLZByoLrgTvmjqvQ4HeW2V3VaQc-_xC7E8A-6g8oIMiUVmwmy5NWKI9Y3Ph6jG5EioZdOKWxarAP_D4rBM19a4wL4PncOVBDV-5_Pw0tGX0vXun1juWaW7JPCH5AkB9-qs3xBPuwgTv8uunQ03cbygBPQvuP_P2fxFzsVNmkms3pLc32ZwO4QFwqPQJl285SubxqCadi7BFuVroqU5oDIcaYrMm-7y_VUlWi-I58sonS4e1k9D2CMp3c_lii36KDM_5_E2NP_MnoGfOejIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
🔄
برترین پاسورهای تاریخ جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/90698" target="_blank">📅 14:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90697">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/Futball180TV/90697" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🛑
تنها سایت روسی فعال در ایران که درگاه ریالی امن داره
💎
شارژ دو برابر با کد هدیه
IRANBET
برای بونوس ۲۰۰٪ این کدهدیه رو وارد کنید
آدرس سایت فقط با فیلتر شکن روی سرور کشور های آسیایی
👇🏻
derbybet.org</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/Futball180TV/90697" target="_blank">📅 14:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90696">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REPtvDgWqCiAFjY86aLlHApG8-bd7GBroso-sZ58bWpFPC9kqEVx1PVLu6sHj-CSEGxtvNGvD9MEGAqcbbd9IYhZGRDT1XU6IyMNEXeSAJcIdPMa--SJMD1HB9iFyY3G8aYLK5s_Ogi29xTqhhh7GyHAltXkDNiylI5xqRa88WRJYuHi2ORWduYsxZhvPgCz49b2h3sVfQSwk9vUP7CfnY5ozBACN77XMBxFskKKf6MfIAA1YX_h5Moqm3gkLKoFQUE5U2mPl79D1IohyKX3HQzq37II77tkaVxbB_Q5MbOu7cIQB5c0WLC9SvxawsXvk_ASSzNc1EK6e1t_R3xCmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
Derby Bet – تجربه شرط‌بندی در سطح جهانی
━━━━━━━━━━━━━━━
🏆
دارای لایسنس رسمی CURACAO
💳
شارژ حساب با ووچر، رمزارز و درگاه بانکی مستقیم
💸
تسویه‌حساب سریع، امن و تضمین‌شده
🔖
آموزش گام‌به‌گام برای شارژ و برداشت
💎
شارژ دو برابر با کد هدیه
IRANBET
🎁
100%بونوس هدیه واریز اول(
شرایط
)
🎁
100% بونوس هدیه هر شنبه (
شرایط
)
💈
آدرس ورود به سایت
⚠️
💈
دانلود اپلیکیشن دربی بت
📲
💈
اموزش شارژ با کد ووچر
👉
💈
اموزش شارژ با کارت بانکی
👉
━━━━━━━━━━━━━━━
همین حالا ثبت‌نام کنید و تجربه‌ای سطح‌بالا و ایمن از شرط‌بندی داشته باشید.</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/Futball180TV/90696" target="_blank">📅 14:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90694">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4p29O-xqthHMRvRjFSt7LXymC2SVgzZRm867Zh4S5BTWasN5WIyQMggK5e8n3wmyWAVbvupEAHQJigtvd_oEk9G0C9OG9fajoanl1wgTYoEaXPyWs0_OrCmJ0A8zeMh2BClzqPXeUAeIhf0NOQcbZuBF4eQ8H5gD0S4t23lxa0BsrVmf1sWRBNkschHW_jUH6p52f97P2FerS6fbTIZlkUmmWEmF9lWgRgUB4KOZKSeTeblXwArLu736KCp8MH-1OQSRBj6Lyu4IvWyvh8EHZhGEwJDRSX8xkbJcH6rlpWOvM8e5q9N-02a0Ght2ucQcD50YFdxrR1Fq7ladxSFww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🏆
مکان کمپ ۴۸ تیم جام‌جهانی در یک‌نگاه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/Futball180TV/90694" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90693">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری؛ کارلوس مونفریت خبرنگار مطرح اسپانیایی مدعی مذاکرات بارسلونا با اینتر برای جذب دامفریز شد. ظاهرا فلیک نام کونده رو در لیست خروج قرار داده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/Futball180TV/90693" target="_blank">📅 13:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90692">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRD9hhofWV9ZmRPrH5mjskLgaS91Z8RLFzfjAwqSR3Ty17JkDG4jhJwl6jGmLOc9xWzzAWfCChtOw-lBdQQrUXqHTOuU-o9twSUU7u8PG9QrtWOSEM-Vi9UOoW2yVfuuqi9-mpsgjmDB_VZe2bAWrkmb_2FGRuBiWWTiljRdXbRdluU8FOoPxXGaC2FSAcaAYi8UNfCbbCsRdkzBgM_1ce9P1Zvh5YxUaDTV2fnJkJ2Q_ZggdWYWI8R8Th1hMA3sydE0oMoc_660TRZdr1BO_QFrgYDKitYt_XjdY-nmrSyRhosynDTgemzw-WY1am1UZ6nFNN8L1_yIYRcRMzS3Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
با اعلام رومانو، بارسلونا با پیشی گرفتن از رقبا حالا در آستانه عقد قرارداد با برناردو سیلوا قرار داره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/Futball180TV/90692" target="_blank">📅 13:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90691">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JW50aFWr8ij5270_hUKafo0GZ9RHWk-RGCTKXYlYYFodcwiK_j29euBNLpOTcdWGFFeS4ta-rzvZB6XIiNTBz3ti3dCQ3QhQ7kp1GlUYa9RGyEFdfy7s4RpPNNkvEuzTNwYmim8FIeYSP6Nu4TYfd7yWU9K4l0aN_czolfyjow3rABpR7jCfWTn-dKZTbwvDbQNYpF0uY6-YvKNrpvcaKQt9GbmVnEly0evGDIatS6Q5bFB97bFWFgQDj7xOKyq8gkijiCa6O4f8rAylUHRjMXuTLJPuTl7hN79wS_7AhY7YZBJV7AQ6W0y8AuiUVobKJqJ1KluVEl0pJq32i55qJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
مقایسه آمار این‌فصل مثلث هجومی psg و آمار لیونل‌مسی در سال ۲۰۱۴/۱۵
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/Futball180TV/90691" target="_blank">📅 13:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90690">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2IZK2AaFvJELp-xD1nBuQN7G9UN7dkGXE50LlWrP8itMGkf7sEmz6BX-wc2RIfVv-Z23Jcgu0yELR9CFfVAWeWbtJ_ms9Aa1rVujDT-1BfEAJ0K8-Pow6ZaP5GjxpwXofeu-U0t2AuB84Si4efBc_nALyDL_Ok9nNa3qt0TiTtm23GPqWtT3L7WnI9mgAZTYxcBQtIsk-efVMhysNnJJnYsUgquu8htxZhyxEqHbb6afy285E99tb4pByI2aO_TZVKTVoWOBOezBS0P1Ih99Es6SkMF31LDuGfr5fgTfj_HF6fnHzbi-4xsAE6E8EHUqBCKXeZ0YzLMyWCEuMmKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇧🇷
نیمار و مامی در حاشیه تمرینات برزیل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90690" target="_blank">📅 13:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90689">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
🤯
💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری؛ به نقل از AS، آرسنال به صورت رسمی درخواست جذب آلوارز رو داده؛ اولین رقم پیشنهادی توپچی‌ها ۱۵۰ میلیون یورو است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90689" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90688">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9DSqRQOlSfWczAFAEzHpVRlIjWR7FHzPOFVzDjZ0dKlbdm-0xdA1a7vwmGHZKTClW-8Dh5OWmFLAIDKYIFa_CZkitrem01CF2BW0gJimr7WYO5WzEQccfHmL7Uh9MFjhavRnS_sGUxj3vA3114CNdqV2b6XRdh-de_HTTuOMrp45X5Te8rJJluf8_uBYP8RYqJAxNjfvyqWktcr3BjZ4vWKZt1dU5swrCwUKl6RbKAIz9htvG6QCndvlL7FtK-1ha9czLZnrTBrHITtLZ3rQ-4vtNQPXCseqnU5RPss6FrhXJRj6Bac7R-Uzs6nIZKzE7inYJ63xEFHfL9JjDspZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🤯
💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
؛ به نقل از AS، آرسنال به صورت رسمی درخواست جذب آلوارز رو داده؛ اولین رقم پیشنهادی توپچی‌ها ۱۵۰ میلیون یورو است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90688" target="_blank">📅 12:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90687">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EW1pt7f_eq4HuOwWjR82iWfRL7gHokOoXH0sZ4Y-brrCELYrFbBrgIFZF58o6J3i84GZ6TCx3B0LEUek6R82segD52bY7m2cPr3R_tjxMWND-J6NaIjR1iRxWH4SLGKxu72pnOq1itSvWSw8t8EKU04Zdjs3svAixugV-A3MQRpXTWq4dVS9f3Nj0hp_68V3DX0CcscgDWKGbgTcivDIwTpiI_4m1KAe1zz465ocG4iVWrIZAmZciKvenpQYPT9fU5RL0rw-QWuD1TpI6Di5dwOzQQZ37-YbTTDkTJZUYC_39KrnWiHtt0aNjlLxWWfbYpytN_5GWQdeaHG2CPOdSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇹🇷
لیست‌نهایی ترکیه برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90687" target="_blank">📅 12:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90686">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6aad5b7d29.mp4?token=FR6yZQEy0KNtByQP7kY7Mab28GKWblIHMMiKQhODC-8TT3YmqnDxZRxu8Cgvqjv4G9Rr-IfdI5pEVeyzN2cyujt5XuAiOkVBtHOado2YQH4lJZqVwnJCp3axw0yZvaqZ3uqDw3OvEro9RG4xuB3mrSbpTaFjjOxayPGVo01KKuz9ZhHopEZJn5xPkIABy3phKawItqrCNAdTTEpXPktBlr4_8SPAFSMVDZtsNXsPvUYn9T107NfTW9Yn7dwyf67J_JCzT70cqIZNtq7i5b3hfoE9pelDb4D1xr9hOCwQ9vTwsNnL-lT5nV7mlFAGlglEQ5YaOiSnz-ifGu0pyaiM-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6aad5b7d29.mp4?token=FR6yZQEy0KNtByQP7kY7Mab28GKWblIHMMiKQhODC-8TT3YmqnDxZRxu8Cgvqjv4G9Rr-IfdI5pEVeyzN2cyujt5XuAiOkVBtHOado2YQH4lJZqVwnJCp3axw0yZvaqZ3uqDw3OvEro9RG4xuB3mrSbpTaFjjOxayPGVo01KKuz9ZhHopEZJn5xPkIABy3phKawItqrCNAdTTEpXPktBlr4_8SPAFSMVDZtsNXsPvUYn9T107NfTW9Yn7dwyf67J_JCzT70cqIZNtq7i5b3hfoE9pelDb4D1xr9hOCwQ9vTwsNnL-lT5nV7mlFAGlglEQ5YaOiSnz-ifGu0pyaiM-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
⭐️
یوونتوس ده‌سال پیش یه ستاره‌ای داشت به نام آرتور ویدال که اینجوری پنالتی میزد و رد خور نداشت سر گل شدنش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/Futball180TV/90686" target="_blank">📅 12:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90685">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90685" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/90685" target="_blank">📅 12:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90684">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6tkA-q6Hqpi8NcIfSmFP_-kDeEQKkHteEglo4wWBelim3-_Sh6vyEdHw7vZZglaY8O93ablJPjXfvZGEKSyUKw4oBhAuNDZbnqIZ9AN1XWxrRQnpzRW5lNd1dm_J1L57_HompWD8jRACh_YAmzDPQNiihgmycSiBoa3ZKv3w-GcG47Eu4ifshcqzQQgfz85HxHC_ILI6FVxXiebY77Pv1bQfsKpxde5zDquhlj5RWAk4R8DafJz8ZVVKXxhywGh9bi4GPJ15j-sqII0_INLE-fG8SCPvNvK4mGubaDqO1xL8L_ifTk5ZFHChvsUmQVNT2isgc3PuiO0NLqcSJEPsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
روی بهترین مسابقات ورزش های الکترونیک پیش بینی کنید و برنده شوید!
🎮
تنوع گسترده از بازی های انلاین  CSGO, DOTA , FIFA وMORTAL COMBAT ...
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
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/Futball180TV/90684" target="_blank">📅 12:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90683">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oi_Px6QDG4iPcfiRDv-Yf0tUC29dXqjOoXWClp-wK4z9ca-5wrSACl6Gn2LpARgYrJ7Hyxb__SSTC8nKheIzeVc4VXL65iYly-HRIwJjaGe6LrSjSRISyWOUdAATLy5NYjaldJaxvUgZeduOBcLO0srMfuyc8kSccURg9Xluszjwc7OcGGv2NGRcfnykmvGkN6dmagdMrbncdw-iTz35T6EYvcS5xjD-winNISlf5jB5s9fQCbYe7DjoqBsMKBUCW4OUO_G3xwwpbRP9S__uwzHBBk6K5ALHmV3eObZW7tLy7qYYOLrlyXH2HPYyXJUlwrkEByFVCjr3Ka0sprWsVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
رومانو: آندونی ایرائولا به عنوان سرمربی لیورپول انتخاب شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/Futball180TV/90683" target="_blank">📅 12:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90682">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYn08tf6IcxxI2hF2MzysqeavMHMdKyFoIjn8yVEQ7Ak-vTPVE19Co5MUqmKoXmK9K4j3s7HMuKhEznqzBfrHHQx6LVuv96oHaHV504fYYlnR8bdmYskNV9ok7t9fiuKigL6vS-1vbtF09goHmzQUIPSk0TwXjZWrR0krCmYfAYvR0zjZGgscxe7GI4yOecTqk43L8GfGT-FlMoRxB0TqJxV8Jc_89ezzEgFC7ZGHlsX-dM_eVbk1mhOo_7mmR8AR7nvGpmqG_d3R4Mfjc464j-lrNRzC8oi45Clwp9eN04Q69mvW1S7zyefzJ_bRuTAK8AwpgbRHJKHcj-M7slqhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری
؛ کارلوس مونفریت خبرنگار مطرح اسپانیایی مدعی مذاکرات بارسلونا با اینتر برای جذب دامفریز شد. ظاهرا فلیک نام کونده رو در لیست خروج قرار داده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/Futball180TV/90682" target="_blank">📅 12:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90681">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/866da1fdc1.mp4?token=AMidSdx2ELF4OpKYsraRLW24fedXDAO545GBzepHUjnWubA3cVoE982yAY-UAyQqkxZ4NB2KrDYwk7fihaOds4FxGACmjuO8RG_ex_yDz_f7_w-PAH10rNrKLCUeJkpRW5FEdMTqkufyFV5dhtOmhLOk_3b82nOJlBp5tz1xvrVP1bLYTYXb6y-0qqlm-eKjFKyKNrZmAVDgNQhcqdHorkzrC90hSU3oiNC7ZGCxjs_jNyQRfIk7sFfkqnEZzyhUI5JY5uEFwuj7DtXsSl5Od96HiOOyyhiaXhvaZG2ztr3Nzi5SBhKDrszgcQlwlpSJTqmAzcKrHGKhyqd9OLmFMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/866da1fdc1.mp4?token=AMidSdx2ELF4OpKYsraRLW24fedXDAO545GBzepHUjnWubA3cVoE982yAY-UAyQqkxZ4NB2KrDYwk7fihaOds4FxGACmjuO8RG_ex_yDz_f7_w-PAH10rNrKLCUeJkpRW5FEdMTqkufyFV5dhtOmhLOk_3b82nOJlBp5tz1xvrVP1bLYTYXb6y-0qqlm-eKjFKyKNrZmAVDgNQhcqdHorkzrC90hSU3oiNC7ZGCxjs_jNyQRfIk7sFfkqnEZzyhUI5JY5uEFwuj7DtXsSl5Od96HiOOyyhiaXhvaZG2ztr3Nzi5SBhKDrszgcQlwlpSJTqmAzcKrHGKhyqd9OLmFMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇲🇽
مهدی‌تاج: ما کاری نداریم مردم مکزیک مواد فروش یا هرچیزی فروش هستن
😐
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/Futball180TV/90681" target="_blank">📅 12:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90680">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qw3buVRaegPUwq9VHNsmWGAhDNy-jC9M9axH9O_bW3IbXf-2JD11fdr_4yKY1PZShIeQ5xCYL85YlgX7Yy4IRH8ihZi-JNke8kGljQoQMXWzTWlOhImQM-HwJuu67uctVS8J8uu6CkV0zNoU1Iz6aerT533xfn2ZIINhJbQvmFnCayd48-LRAt77rnZM7sG5D2OqNt_PBJaxf-sTP6njm58z4CiXvL4idKWrVEDoOeGAUjC6C5EpzBzwGS1z0CsvmNXOLiuUN7LE-P2RV5Imc60-D9dCseNszRWnf5rqTwgkt_7fd2R2IRNywrwS60_Abiw-_e6CPv4JYmuBIHFf_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونایی که جام‌جهانی رو از صداوسیما دنبال میکنن باز باید این دو تا نچسب رو تحمل کنن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/Futball180TV/90680" target="_blank">📅 12:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90679">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8766b7f17a.mp4?token=hrdKalsruWuP9UWLpPKa3YOlHUNeV5U4mqBEakHKevlxjpNSBhst56Xi2cQ-cJuRj-N-WASZviNo4oO-h5YsFqoeY4GSJU98881NllA6EG5ENlC6Z-TaPDH61ZoJEAsSR75obByjBVom49ABU1CyMftsIiEVef4uuv7E5K_5jVelaf5pIeLUtq8zlUKcjyc2RdNm1nfpgs4ZpU5NNdykjStRWFJk8Jmj2qreiw-HtA7okpW-NYL9DtfcjgfNcnntS46_EKw9yZ5pHRTCtRd6-nfbjkl8MR9k6O94qZtUbAPGXZ1e1jii8oV8bsZSet0NqD8Oqvzz6WkveU-Pj805TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8766b7f17a.mp4?token=hrdKalsruWuP9UWLpPKa3YOlHUNeV5U4mqBEakHKevlxjpNSBhst56Xi2cQ-cJuRj-N-WASZviNo4oO-h5YsFqoeY4GSJU98881NllA6EG5ENlC6Z-TaPDH61ZoJEAsSR75obByjBVom49ABU1CyMftsIiEVef4uuv7E5K_5jVelaf5pIeLUtq8zlUKcjyc2RdNm1nfpgs4ZpU5NNdykjStRWFJk8Jmj2qreiw-HtA7okpW-NYL9DtfcjgfNcnntS46_EKw9yZ5pHRTCtRd6-nfbjkl8MR9k6O94qZtUbAPGXZ1e1jii8oV8bsZSet0NqD8Oqvzz6WkveU-Pj805TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‼️
🇮🇷
🇺🇸
فرهاد کاظمی مربی سابق لیگ‌برتر: وقتی شعار مرگ بر آمریکا میدید دیگه نباید گدایی ویزا آمریکا رو داشته باشید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90679" target="_blank">📅 12:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90678">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9866c6c42e.mp4?token=jm3xPntwevJvXV2vQ-V3VrVDgVgAoqpVdMLIR4YvyvdedF8xfxTDj39dxXv3uXzP3Q5v8Gm3D3zZ5RhcGdPiYd9k30rgfTCUywIYzTZtuqpeBQ5vUnZEx7btslY6Vb4e21Bu4RmH2Deh5NSwRV8dmR1tzYW0DyUoIi41fDa9lVMsnXF-2lKd0__C_G5udB-MdCRnJ7S-f5_XkcmsVc47j3yV2txaG7RbSahEDBPfx0UWUitaAWOTjxMCcgpEFAhBQTD9uJ-oi1UuHssW9YfDvmOSlmpj3J6e_UTonPpMTVSuoyyOAtiw4IfX38Flr-qcxxakjnPnOzuNqTZLcnwhNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9866c6c42e.mp4?token=jm3xPntwevJvXV2vQ-V3VrVDgVgAoqpVdMLIR4YvyvdedF8xfxTDj39dxXv3uXzP3Q5v8Gm3D3zZ5RhcGdPiYd9k30rgfTCUywIYzTZtuqpeBQ5vUnZEx7btslY6Vb4e21Bu4RmH2Deh5NSwRV8dmR1tzYW0DyUoIi41fDa9lVMsnXF-2lKd0__C_G5udB-MdCRnJ7S-f5_XkcmsVc47j3yV2txaG7RbSahEDBPfx0UWUitaAWOTjxMCcgpEFAhBQTD9uJ-oi1UuHssW9YfDvmOSlmpj3J6e_UTonPpMTVSuoyyOAtiw4IfX38Flr-qcxxakjnPnOzuNqTZLcnwhNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب خداروشکر تو این مورد هم عقب نموندیم.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90678" target="_blank">📅 11:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90674">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ef18n9K8WNVnH92lCrPqIpSBTAtQf7q1NUz87_wZ8xkm8l7_NRsdyiz6UDFs803u84PaFOCVBe5I4w3bzqvw47BZJValmIuF35erjoC4bpbJDDUtC-NNP2uEr60WNb4K4rdxXdK-LXlNu7XjYdZtKYlymrhSz1GNcU-wnI1YUnBs7fDPNeMthTxEusPJr5ZIiQWuK8nt0ULwbuRvf5cveVyXEcvgWrIKpEqmmcBtCx0jP_zWeYMvUm5oDeX1UECo78LEDaZKXfy07---5A5JoKSFAt_14q6eiJh0dbWCGRh0kgthWYuzQHmXeLQVEjucSzoVFgd1lEtVE04bb7MZWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tjuReVv18yZb39m1RrkUGxd1gHt6_Rmh2vZ8T2uMeieDDyzQ6bOsA8Q93fmvyaZTLufXZhX5gbXxRGXfHpYyf3e7p44wSHmd36ZjfnO1ZJs0VoCohuTrKk-GOFgrKUcU7Az6KEs9j4b0P613tfVrtN78_O-k1lbDBYh7atJNem3VtWPwBOJ17oOKmrBj9LuIgBWIK5iIl4Ag4YsjQXXIkxtjgOyw0tpdTb-zmkQD6B3_0PGX-vEpWQQ3Ft5K7IucbTdKLwpLTE7mLtovMvvRYFEespCryLIKGSpL424rFocBKIyiz8dTlDG-bKJ2F0g-pAq3XZsogS6vl7FbgE2OLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f9-c2KtEdGgqpF8g6LLs9zpdF2g2FC0MQ6h7e11rCML_86S61JvEBRTPk0-vohz9Tzm5d-SjWwnz8NgLU8HN-hBDgXEt9PcZqGY3Q8Ot-BzcOE28n6EfSd-XWXbu0sAsnQyX9NaqHyocDr8tpT4o8stNDrXjDn1lwF0kS_6U97eSAa5IUrEF607hze1FJR-TPSDrZr5d4togtEZeiJFGh6WJB-PlmBbrVqCx_Tp8SWpkfw92vTF5EyKD8IkRrwBUMjmdun3It-fInEjcFbybjDBWGnGIRpgd4K5dBmP68LhrZSjYFL6jPnXFkkKkFIftcTVDOAK97GQIPVo4mYFxcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LQU3ZuOAxiNvkeq8uMb3gkdjqUVSmAQBpBnuZZ7i1pmrxO7M7Nip1_e_HvxFs2woS31RQVX_83xQHCZ-dnhcxvPEjBgm_dNYZ0zPU9wcCSlDTm2i4z9FuqFoso66IlCc1jSysy28F4h_xH6SkHTEyZ8nrwCFcdhtmADdFH976wZqQibrF_XhmDvioXL0uIopItP7WKtDx4BAh77dnMTICuXUvdU98ogZDReXG3hFumTEnY8eSAQEvV6sV-72MSi7IeQuU8V5qlJX8XJNbiwccsPwtr3eYLKRKsJvQid1Np-_9ZnMTjYxUxViLIeKxNzj1Dea3-uNfvRm_xXqBvdnfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✔️
آدیداس از طرح استوک‌های جدیدش برای جام‌جهانی رونمایی کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90674" target="_blank">📅 11:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90673">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5291786993.mp4?token=aE6D2XUqeEqGsXksDgtXu6y93Z9uYMzrcbcOth216F10z3bzs-5jsmCRVV85UbGIhnWWUw8NwXbcwTyvNZmPAADzvCLNw-O5EXwbcCTyno2rDgXo0TMb7CrrUj1Tz4eOz6N4-lO6uczYK2GRGr9L6r0aWQECegkY1Z2_tKD27fQW960oyihCKx1OB-F-M1IPw_DmFH6YdEvh7XRVGILKaO1j2AedhBcrkd1ypSXJUgnyrXZ6Z2J_ZuyJIo1BQFo8bvFSzh4qStqEQMKiTrVJZGTadaaSZsG0B2HJkd6ILrQifpl5XpwgMKBK_uIvC4xK2TjLR4u9CHBT-_yIj_3IYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5291786993.mp4?token=aE6D2XUqeEqGsXksDgtXu6y93Z9uYMzrcbcOth216F10z3bzs-5jsmCRVV85UbGIhnWWUw8NwXbcwTyvNZmPAADzvCLNw-O5EXwbcCTyno2rDgXo0TMb7CrrUj1Tz4eOz6N4-lO6uczYK2GRGr9L6r0aWQECegkY1Z2_tKD27fQW960oyihCKx1OB-F-M1IPw_DmFH6YdEvh7XRVGILKaO1j2AedhBcrkd1ypSXJUgnyrXZ6Z2J_ZuyJIo1BQFo8bvFSzh4qStqEQMKiTrVJZGTadaaSZsG0B2HJkd6ILrQifpl5XpwgMKBK_uIvC4xK2TjLR4u9CHBT-_yIj_3IYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
بدل‌های کسخل و ایرانی مسی و رونالدو:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/Futball180TV/90673" target="_blank">📅 11:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90672">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHVoUU1r5iDfuddU4Pwlvwbxw1IoXXgoFw68_PJcnkZcKLDq0g0ssGAbJp36W5zYf16GnGseQoUs2P6KpohVzPDwDdazxh6k3rhGqQFdAyta4ibKsjAo7hOuXDx1E7Wi8XMXXRJiVCgsTxnW2cl9oMLvvITSK_RAItHKbhH5Jgr959gxquC-lBj5CYnD_ctFYkb_T_gcgdekSM6W5sZgjWIGah6A4yLwW7q_Kr2ohsKsBtyy55-GQAobEO7Mj8vP6lN1GQ39wjYc30qI3RIRnOJeYXj8Fn9l8Ka4VaPYo3UQ14kXjQ8sY0d0HkFhvRMOeWQjcJHPeNr_CJE6KWoLig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتوی سکسی گارناچو
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/90672" target="_blank">📅 11:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90671">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3c911c332.mp4?token=ba57hU0clsd47O0HeCxN-XRJuzHrrwwzhkKBYTUYflE1OITu2nyGqZ0BRw1bZyNFqGqNUdQa8-OPDic6X1-Ch2K292ykpI1lq7glTA2w4KXXn9O7NrBB1mq7h_rLi03_l2CZ4Erre960Evj6NRftWOI-WuVnFTdUfcoxI1VhcMPGCkc7VAbdeCfOTRP5uHbsolxN4NlE2y2wFLaAHF1PIiLfWyknmAi24H7MhKAr01t-uFquUE6t7wK6MJbIw_gj_URbU0ZDFn6nCq-HUeLjygqSMCrhKbiR4Fib--SBlJVHbKU4xxTJA5dxiNqxLzV7tarZvAHRM2J7zJgT228_AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3c911c332.mp4?token=ba57hU0clsd47O0HeCxN-XRJuzHrrwwzhkKBYTUYflE1OITu2nyGqZ0BRw1bZyNFqGqNUdQa8-OPDic6X1-Ch2K292ykpI1lq7glTA2w4KXXn9O7NrBB1mq7h_rLi03_l2CZ4Erre960Evj6NRftWOI-WuVnFTdUfcoxI1VhcMPGCkc7VAbdeCfOTRP5uHbsolxN4NlE2y2wFLaAHF1PIiLfWyknmAi24H7MhKAr01t-uFquUE6t7wK6MJbIw_gj_URbU0ZDFn6nCq-HUeLjygqSMCrhKbiR4Fib--SBlJVHbKU4xxTJA5dxiNqxLzV7tarZvAHRM2J7zJgT228_AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
🇸🇳
ویدیوی جنجالی از بازی پریشب آمریکا و سنگال که شدیدا بوی نژادپرستی میده
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/Futball180TV/90671" target="_blank">📅 11:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90670">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=UNf5VHTq_F0W3tqG1E5K_GWj2mtCPgwP3wNyjAQ2_LKqpGjP8LDkvA4LDFX0cQt_FsrN6E_Hi0kyIjTlVluhTimrJAxno4qW_0oLOf06-dpzIwAb7_6yq-_mlc54ebqStnoEtJb5SFyyXaIy-I5hKONPYZYKL8HzD8LoYPWhi7i-ysh_w4r3Bw8KEdnvtKOJ_6SrlAkg1-L3q5UuhvsvtiyyX3tfIEf8uu2NtaJ6BXF03xtGCNdY-XXNqIF_hYpH9eCZYIEbFY445EEaoADOLGFmLKEqE808cKTkylcTZ-RjdbG78AcweBxt-eVX8qPW26NoEANgAn7pjcsQmqBHPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=UNf5VHTq_F0W3tqG1E5K_GWj2mtCPgwP3wNyjAQ2_LKqpGjP8LDkvA4LDFX0cQt_FsrN6E_Hi0kyIjTlVluhTimrJAxno4qW_0oLOf06-dpzIwAb7_6yq-_mlc54ebqStnoEtJb5SFyyXaIy-I5hKONPYZYKL8HzD8LoYPWhi7i-ysh_w4r3Bw8KEdnvtKOJ_6SrlAkg1-L3q5UuhvsvtiyyX3tfIEf8uu2NtaJ6BXF03xtGCNdY-XXNqIF_hYpH9eCZYIEbFY445EEaoADOLGFmLKEqE808cKTkylcTZ-RjdbG78AcweBxt-eVX8qPW26NoEANgAn7pjcsQmqBHPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇧🇷
صحنه پاره‌کننده از خوش و بش آنجلوتی و اعضای برزیل؛ آخه چه‌وقت دست زدن بود
😂
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90670" target="_blank">📅 10:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90669">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0777399bbc.mp4?token=bR1HwwHkpp1oMmYRxSmAKd8Lu5zNgJLv2MMI694l7KqSfz4cNRKjBGOK36rfSuy9gTWcENQLY9svsDJVrwg6V116-CxngV4qp1XhDzqirrs4EyCltlJeTaTTdGSoKtlAP1ZF_zSmDipJx5Vu0_wjdScd0qPA1jOdh6BiGR7mD2P-NB5seotsbR_yfmoWZEtYuIcfI6HQI_k5XQRY7glcpkRDwDHn270Qw78mWBJ6IX7-ANBZ81_5DRqmJ7VlqtISyId0vPrJDWUKt5vXi9xSlMSuEeoL_CvT3VwE_1iHnkFp_B59HLgVBpju6NAXN-zrLdS2vkqokbbXQkfpjZq52A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0777399bbc.mp4?token=bR1HwwHkpp1oMmYRxSmAKd8Lu5zNgJLv2MMI694l7KqSfz4cNRKjBGOK36rfSuy9gTWcENQLY9svsDJVrwg6V116-CxngV4qp1XhDzqirrs4EyCltlJeTaTTdGSoKtlAP1ZF_zSmDipJx5Vu0_wjdScd0qPA1jOdh6BiGR7mD2P-NB5seotsbR_yfmoWZEtYuIcfI6HQI_k5XQRY7glcpkRDwDHn270Qw78mWBJ6IX7-ANBZ81_5DRqmJ7VlqtISyId0vPrJDWUKt5vXi9xSlMSuEeoL_CvT3VwE_1iHnkFp_B59HLgVBpju6NAXN-zrLdS2vkqokbbXQkfpjZq52A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپید هم واسه جام جهانی آهنگ خونده
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/Futball180TV/90669" target="_blank">📅 10:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90668">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJrd3jqbGv63LbER7R7Mb1VB-gzS7B28imAl_nRTLAef7aQg8ntdlN9iYJV7bnsAQS7NS1QF2JXCRBAZfnqZ6v-TSly_l_aCgJ9JdvPQ2AuYw1t_lnAwNdkUhSaedLUHP6KHZROc1jcjelS4rIMPrJZUh3YXJ2k8odDL2qzB0g9PeGzfksT0FQ-NG8hTwUR6PgVSS7iILVuSN0XW614NAjx0FuncHNRsRSIKZVGtx0RW-Bh1tsq9qXLr-3rFCCoM-mqxYqDfEwynhe0R-yCgZAXQ8snbhKkfSYxJwxDrlyO-XZMG4F2btmHXGfKpVITJurU0RhsQXDPoAhjhxfZnzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌اول چلسی در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90668" target="_blank">📅 10:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90667">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNgAgJuZqfGTxUQ21FGMjjkwQm860osy_RsxI3JWbcFQwlmsm1P2Hre6wsLgwqpxGvpt5-BWoJI0wQtKRDKHDBDTUF55V0BXcag3jWYNPd78tepVtbEThJ7Tq0XwtvmKXYpUFF_Jj1UyYblv3knxgTBfASg7KMhFuFI4d8DCvH-0nDuslZLdsuQuD4nedEtBPtaai_G51Gxziggehug1UqnbfsN91EDhK2_gZk8uemtxusA9w3sXqSyE8cabGEukdTR21qWbtGA1ZCmm-JnOXU7f54leX3mF4dmfCw54azoi8bYUeEo02Js1z4iwNTgESlyeNS7172WU-Rw_RTNg_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد دمبله در سه‌تیم مختلف؛ معنی واقعی شفا یافته رو در تصویر می‌بینید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/Futball180TV/90667" target="_blank">📅 10:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90666">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=LWAxBatX1Ey3ZWMD3vLMNcf_sfPNqdOwaqnvL1Yu3wTR0UpRseZH2qsuDpM9Zlm7XLBdqX_xlDRaQ_ivVN63bSpoiH3BJdGmF1TV3La5NMGVwM_3Kzn3ehG0qQ7StwqsELWFgQtsudfr1Ow-JDifkbFEYDVMJIaOdjehzAwvhLWUCaR7rfnJYND-dQZLfXe5g24NF7VHOACI1OXKmn5uIpbQxsjkTIGYBvrugo7WX3PKv2oxxn8mYRJyV5Ryw3hM2HHZ0TJv6vkIP8692ijar_x1gL6ZiXoE6_2e7gm4eE9Mg0uY2o9K0_hJ-4MotuNk7AJ9lAZqT41wF0GWC_LslxDvRGWi6kVpfawJm4kE7nH7c6Is9gVpndWKXHFplD1852uIRQGdRjq1rdFTyvAgRMlSQLZpVqseFebd8hTWq0lWWRCsJbAQm1Y5-bkqu0n86G3DfRjJ8CPXn3LM7hk_RfSOvcDIS1jCP_Q5K-iwQBU50zwP2OW9n3F8m4XiT5TFn-Yuq14t3G56bwA9ZuAOKfUtakgDhM3z53GgzoHCHmKBQix3li80I-fY1kOx4kx8QXgKnXhwHNebFKuJvj5DGZ_nNRKHg4IiF_SJOKWZoNedb-c5v3SM-IbP5VirS-NUkOk7gMtGRJOC3jcsMvkTTGJ27lFn-csnUYAylUxPo-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=LWAxBatX1Ey3ZWMD3vLMNcf_sfPNqdOwaqnvL1Yu3wTR0UpRseZH2qsuDpM9Zlm7XLBdqX_xlDRaQ_ivVN63bSpoiH3BJdGmF1TV3La5NMGVwM_3Kzn3ehG0qQ7StwqsELWFgQtsudfr1Ow-JDifkbFEYDVMJIaOdjehzAwvhLWUCaR7rfnJYND-dQZLfXe5g24NF7VHOACI1OXKmn5uIpbQxsjkTIGYBvrugo7WX3PKv2oxxn8mYRJyV5Ryw3hM2HHZ0TJv6vkIP8692ijar_x1gL6ZiXoE6_2e7gm4eE9Mg0uY2o9K0_hJ-4MotuNk7AJ9lAZqT41wF0GWC_LslxDvRGWi6kVpfawJm4kE7nH7c6Is9gVpndWKXHFplD1852uIRQGdRjq1rdFTyvAgRMlSQLZpVqseFebd8hTWq0lWWRCsJbAQm1Y5-bkqu0n86G3DfRjJ8CPXn3LM7hk_RfSOvcDIS1jCP_Q5K-iwQBU50zwP2OW9n3F8m4XiT5TFn-Yuq14t3G56bwA9ZuAOKfUtakgDhM3z53GgzoHCHmKBQix3li80I-fY1kOx4kx8QXgKnXhwHNebFKuJvj5DGZ_nNRKHg4IiF_SJOKWZoNedb-c5v3SM-IbP5VirS-NUkOk7gMtGRJOC3jcsMvkTTGJ27lFn-csnUYAylUxPo-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
استفاده از گاز اشک‌آور توسط ماموران در بازی دیروز بندرعامری و شهرآرکا البرز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90666" target="_blank">📅 10:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90665">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMzk7gS3sNdm6N_ndJ5I9egOpX-CkMTJCCeLuwnFIV9s2zHL40o38GpJS39jULfk8S-uJweEqV2c6oQuem9BfGZmkIdpBvmR6tVQSAhTijLDpt132BjqrFafav0Wume5_hfdqu1gcMAzn_CIAeLXe25WCX8ihT1kGVMEhBLiHLQYiYaxLKMT4KnmzzSDEqRMnl4LCQUVd2K0vcXrEXCHQFyjM77qLW79rosflTFfz7iLGIT9IrPzL7JzojSh6KqC9Zlg6CWDGVSSVubMeJWBRpl5hk2XoKxmem6h0az7qONlsIwPr_Ky93w8qT72rCJmXJMkJQ-DrDmrCw5yVZ7aDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 بازیکن برتر حاضر در جام جهانی از دید FOX
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90665" target="_blank">📅 10:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90664">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b95b443280.mp4?token=pzu1LAmaLCG7YPARSY_TI2_QPdknq_TSYOe5q0FU1Fw1nia51jn3RuTz7ymbhWoSFtgFdbTGDMmo-OHuSHHCAGLUS3tuala3Pz0hgSKPUIgLOnA-Rdl_KctQNGkeUTwS6yXhIYLfQG1gjDqTcnxkMWkcd0LCYlBvywu0HSUU1JxOc0LUbPN2bZUPqFjw3fCNsM1Yofu0pgG-5tPw69Ive3XM6nSRbMVAHA7km6JCKupTVJPfQljoYtmX3yw0HP6SEB11bN35kihBLo4_-CkVH_U3UzVF03-gYrbvCYtbZnuw2mvJlnPZ3TLH4NNrGlbw_2q9eJ8iBXRBU63ebh08vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b95b443280.mp4?token=pzu1LAmaLCG7YPARSY_TI2_QPdknq_TSYOe5q0FU1Fw1nia51jn3RuTz7ymbhWoSFtgFdbTGDMmo-OHuSHHCAGLUS3tuala3Pz0hgSKPUIgLOnA-Rdl_KctQNGkeUTwS6yXhIYLfQG1gjDqTcnxkMWkcd0LCYlBvywu0HSUU1JxOc0LUbPN2bZUPqFjw3fCNsM1Yofu0pgG-5tPw69Ive3XM6nSRbMVAHA7km6JCKupTVJPfQljoYtmX3yw0HP6SEB11bN35kihBLo4_-CkVH_U3UzVF03-gYrbvCYtbZnuw2mvJlnPZ3TLH4NNrGlbw_2q9eJ8iBXRBU63ebh08vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید از لامین‌یامال در آستانه جام‌جهانی
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90664" target="_blank">📅 09:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90663">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjVk6zbGvtAlvY-2BnLluNcwlsnRUfwxB2wzfHXBX9Os-QrIgQB6icn4nLZpXQl3U9HulT2kfgBVtBaaetJxamiDnne3pMgq8xT83-1EWIpI1b7zImoIdMGYE1DYN5n0LZrIfQjphBKb7vvwAgvFSPT5WcUWmt5D0RR35DUOk3KWevpii7EqbnKmZNqjLfTabx5FnHtrkV4dtOBG0bZnZa7rpdi6LyCs5fml7lSRMbRkT56ExF-A-PwS1pZWgNQOIGLbpIlSY0TD_2OIxqdUUzf7vmpz2mwRD0AOCjOaZQnKxMfuLWwFyIdQG5iOpnCMbqDQLYFW5Ti07T1NtMWacg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
⁉️
🏆
پیش‌بینی اوپتا از قهرمان جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90663" target="_blank">📅 09:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90662">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🏆
نماد کشورهای مختلف در جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90662" target="_blank">📅 09:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90661">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-xKdf-QJCXvvHGziVpBiT-HOVY8rSz1VuBnmRpDDa9-ChkFN6d5Q_hXNdycmUJHqFKik47sO_hISs8gr6ZRwNU74HoRFjs76c3oKhSqHaUzY16EWAoURtQbSMHcpU8-Nys0Qh2Ij5t10HCmDn6OULrZuSatN2lG1gJXwa5BRYQfTfxJmA9V9eUNIOV3syN3KxotTC4o1Az0JgPkX6vjjFu2b5Ivxt4Pcv1zsKLfjbRH1BHiwxu9SDOIkY9zpgFhCxzat_Ifj7tAzOlq8sjmqTvACLfxfC3mxkWYENaq8yzEEWRLs3ig4y0FEV-tU5-7xUj9WHRgfbudy6olyHK9vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
انریکه ریکلمه کاندید ریاست رئال و رقیب پرز
: به محض انتخاب شدنم، خرید رودری قطعی میشه. هالند گزینه بعدی و حتمی هست که به مادرید میاد. سرمربی رئال کسی بجز مورینیو انتخاب میکنم و از بین افرادی هست که الان تیم داره!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90661" target="_blank">📅 09:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90660">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71618ccd35.mp4?token=Eim8UnJMHzhRCvqFzculAjNl6lRrTrxpBWIxX7rmtblwObW_osT3EYMfRaumI1lXQTQfO12q_p82W5sFKiNXi1eA7Vf_RowQpEgpVkU3BrXxr6ykY8VjvGk1qahGeJQKzyuZ8iy2gZ3XvyOp7u8XYt-F8w3NoxAtTvdGWJpezwCD5efcfTbwBl4t40uHpfr5MKR0Al781ZyDX_bCiKastP6U1i30nrA2TXSXE1Oe0POLKT_Sf8jwrKmK7DcDfAJc5n3LvacV8SvcJNQhrfubNKte0KM2k1eG09YnXU4y5x1fIODvURDpC_fTvdSYhSOz54BVpX6GY6zzKSBBZPwWCTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71618ccd35.mp4?token=Eim8UnJMHzhRCvqFzculAjNl6lRrTrxpBWIxX7rmtblwObW_osT3EYMfRaumI1lXQTQfO12q_p82W5sFKiNXi1eA7Vf_RowQpEgpVkU3BrXxr6ykY8VjvGk1qahGeJQKzyuZ8iy2gZ3XvyOp7u8XYt-F8w3NoxAtTvdGWJpezwCD5efcfTbwBl4t40uHpfr5MKR0Al781ZyDX_bCiKastP6U1i30nrA2TXSXE1Oe0POLKT_Sf8jwrKmK7DcDfAJc5n3LvacV8SvcJNQhrfubNKte0KM2k1eG09YnXU4y5x1fIODvURDpC_fTvdSYhSOz54BVpX6GY6zzKSBBZPwWCTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
ویدیو منتشر شده از یک زائر ایرانی در مراسم حج که در فضای مجازی وایرال شده!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90660" target="_blank">📅 08:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90659">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfff56a47b.mp4?token=VYff1E4bBh095A0x3V4K1wRcuLoTvBMHlQw_rGNG4PLWlNjFUuhhPOpGXsmKkM99HP2TTViszNZQ-DT9xoImCS3Pi0dAJWpZJexymBko34RlIbHKsITcWVy7JF_o_xLW61e4IUpw9_XzBx8gOsvXKsvpq5EYyjS-Jr2NMoENqovs19_lxtahzsNVRWvVfdp37h-_htdy5CemLsDO-0S9x6_gTR9niyNkl6Ing35MINpkWuPeiVqjlL3AvBeJZ_-525n50Qa3jcIIQKvxml1YJihogFHV4AI0a8og1BM3zDo9pUD8HV4AUmMrQTsLLk67FkSrY7-FC5SufalOMurmbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfff56a47b.mp4?token=VYff1E4bBh095A0x3V4K1wRcuLoTvBMHlQw_rGNG4PLWlNjFUuhhPOpGXsmKkM99HP2TTViszNZQ-DT9xoImCS3Pi0dAJWpZJexymBko34RlIbHKsITcWVy7JF_o_xLW61e4IUpw9_XzBx8gOsvXKsvpq5EYyjS-Jr2NMoENqovs19_lxtahzsNVRWvVfdp37h-_htdy5CemLsDO-0S9x6_gTR9niyNkl6Ing35MINpkWuPeiVqjlL3AvBeJZ_-525n50Qa3jcIIQKvxml1YJihogFHV4AI0a8og1BM3zDo9pUD8HV4AUmMrQTsLLk67FkSrY7-FC5SufalOMurmbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
حمله شدید‌اللحن مجری بی‌ادب صداوسیما به مجریان معروفی که قرار است ویژه برنامه جام‌جهانی را اجرا کنند!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/90659" target="_blank">📅 02:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90658">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgRiG2VyHL3aPUaMJ2kLo6GRER06kEtaa9jU50I3pdQRtv6fm2aJPbQYVBxLQydjRj33swiLaItvnE_RQh36hkb_uUb7qHi00AnyffvcqNrZq2GTIyJ0DRSlVKIJ18AD7SkUS8iga6A-gB16G6Pd6VBg60hUSXQKeucv_AaSIcCRzXkL0x6XEX4lJVEEwFpub2bKwVzoVezM6ivXeT9A993qO_bDMGpwGkZUcCWzbDdVYAVptkfqc7ncykryx-vVLhL5OnhZuP5Q5Bl0y6NkyuDsOGdfjIPlIJ1SNu1_Ltk_lRhdXOkA4WrfSYLgteCC9FVH2kvFWBbcjH01KK2nyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
یک‌رسانه ورزشی برزیلی اومده جام‌جهانی رو پیش بینی کرده که در نهایت نتیجش این شده که در تصویر می‌بینید. موافقید
👍
یا نه
👎
؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/90658" target="_blank">📅 02:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90657">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njCRvZ5AF5hhHDHkV1EnCjxZ0UV_ZqWEw1v0DpEJFf_YXZCHaHob0bu-qgeelcfZHwCmSH5EP81_kLPT8DKw7d8ZqDKOBNoNxxv9kD6ySCgm4T3qK3SnKGTVwRITxPPjnAYfj1KmjhmKgsDsdp9l8RlC3mVZFq16gT57-LoTS-nGJgAWk72YUL8Ac7gMlzFxmgzCXeI3PhNSuYZL2ptBTF6UAcUsDaLJz2BxO69rFJZbU3rG2FVOHaTgxj7scSrvTQmR1AqlGPVCrcmwx2FIT4JDwpGdoiaCp9-XcQuyd-FG-RUWBzV4r2CqcK-el9_yRqjtIJc2gGfaYg8gcVCmjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚫️
#نقل‌وانتقالات
؛
یوونتوس به دستور اسپالتی خواستار جذب براهیم‌دیاز از رئال‌مادرید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/90657" target="_blank">📅 02:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90656">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/90656" target="_blank">📅 00:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90655">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=DfWTphGwmD4WHQqTH3jl2xtaKegNWN9I00WcrAdqQ2UGw-9IGSsT5AJECvD_IoSExSK9DFGyIHO5DkfdAdoGQ7pb9iXog02sArbNu2wAAOX9CTmklqQA4p1J1hw5qXg1PuYXqNRd5TGyUNJhSI0HqhfkAHbPxWNK4g_xleU_e35NQ0zogNp5BteiPDf_GawFZ-ueIMyuGLRPa9r8OHK7FwTRMMkZfwq6Ux5gkC0esGQbSK1cAUu2tNjZ5emufmM4TsxoWaaBxIiqmofNtBE16ZH_aE51HaDKP_z_zFM3l8cBSjfnetRrwoN88Cv_nrJslFshO7mgZPAzkHTB64THPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=DfWTphGwmD4WHQqTH3jl2xtaKegNWN9I00WcrAdqQ2UGw-9IGSsT5AJECvD_IoSExSK9DFGyIHO5DkfdAdoGQ7pb9iXog02sArbNu2wAAOX9CTmklqQA4p1J1hw5qXg1PuYXqNRd5TGyUNJhSI0HqhfkAHbPxWNK4g_xleU_e35NQ0zogNp5BteiPDf_GawFZ-ueIMyuGLRPa9r8OHK7FwTRMMkZfwq6Ux5gkC0esGQbSK1cAUu2tNjZ5emufmM4TsxoWaaBxIiqmofNtBE16ZH_aE51HaDKP_z_zFM3l8cBSjfnetRrwoN88Cv_nrJslFshO7mgZPAzkHTB64THPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
🎯
همین حالا عضو شو و شروع کن
👇
e11
https://t.me/+6ckCmywafrxiYzk0
https://t.me/+6ckCmywafrxiYzk0</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/90655" target="_blank">📅 00:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90654">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQoRQ2gym5OuEpEc67CLiS2y9u_kZxgB11rf9xg06HDdYhUMdXrIiApuMdyy47ZlT7ZWJx5DJOj6tslHJ-gatuhL2FUyhK0-E4UQ6yT_oCiKS1SIb0afHA4m7Tpfk4-wJcVWdXN2_QIq9epm6iQPmXOWmMvBZFUOiuJ7raMkIpzBzGqCt42WCxHRqBWwy5Y4vJsUcjSVP1V8xS-BnODvoX4K-ci8-w7gFW31WIJyElnVN8Kx6_-iCViHkx-2kI2z5gia4O6FbVLBx2J6yE2IQm-yUiPXGz9aRki1z-2UVXTM7-adZHSZsQpxpI8uE03SQszQ3BVP4VlnBtMxl3NoOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ال ناسیونال بدون اینکه خندش بگیره گفته رئال پیشنهاد معاوضه والورده با فرناندز رو داده و چلسی حتی ۲۰ میل هم حاضره بیشتر بده
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/90654" target="_blank">📅 23:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90653">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
ملی پوشان فوتبال بابت برد مقابل گامبیا پاداش دریافت کردند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/90653" target="_blank">📅 23:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90652">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کونسیسائو رسما از الاتحاد جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/90652" target="_blank">📅 23:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90651">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pR5v_7UmreK1W0KQfo-4pKWvXozLYiSK23YErEnILqh-bdthyy8NYGpW0EUea78TMB53xPY9esSta6dgI6kFPX2hnJXdAMlyQC6bv04_sV1zBx7oacWYj2f7CgCz85Sp8j67Zw0FUA-ZTKJfuBy4Qcc-xarGZ14egEL4lRrrx698dIQARS6xaEtFp3UksqFTySqBBXLVjRwoV_Qgd60YZQFkOrNwnIwPo-T5vqMJhhf7BIn8cYXTsATJ5pNoyzLWvgMxEaBg6Qj_2TVFCc4BuzkZHZxh6VicRV7rVigb9qXyovxFzxKjbPJgH9v4Wi2SXe8X_QnbS93zXh48F-3eGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوبوسلای به این شکل رفت اردوی تیم ملی مجارستان
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/90651" target="_blank">📅 22:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90650">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfeuSz3OyW_VMjJMJVHpQc3ns1GVtAWnugLxe6OO0l7s77BUf2B37sRLzD2ELLfp6rJyBHoCKEQNI6SPNMPgkq0KMPxY_NlRlhUayDnegFTcuTFvGWgVcLFuZcl9KhndxaSnL3vueqkFgKgawMo7fXG8YrA-wJJ2-UACQQn1d4ioZQ-mPeRBm-tJaSZLmeyweu9ZEAzSGt3GDYLDipBt6QKHh1bzHX-vS7JRISxqgaw_L79r3CDaiAvwUr7PEsWcX4_tATj3e8wDpohK8BDJLtvKY_h0iUQBoqiGboudJusFXeydyQgmfaVo2AsRBWGgSFVsTv8roVQrbsTs1rQZ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شماره پیراهن بازیکنای اسپانیا تو جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/90650" target="_blank">📅 22:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90649">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJkxqjJ3tKiv71csyWdYEWZNIxa0s0XajEdy9qCScD8c7YEIuOS5KgS901M37m7eYgx0IbdP5ZWokpGn90qsZqPhuKKfP0LDHz5aDrfBcS4iAEWaVkBEI73mB19_MzANb95DZ0VC-SJTcwtpUlmYkEc4mjGYVnqbpX9GYZmPcg8DvsYZm8nB46bEB8uiJ5hfBqv74pWLKzXvX0ScBhRWzHUvEaEJrZf2xx6_Uk-NT4u2GnqqwgCyrMzgGIDn3QFRIXggYTj6gSYIeR8goaMLesrFjyNF2w9sEdQ587xsVyBXTyxusw1Oe2GsCLyaCx8cJvLSTWjQs8bT5e7uUoY8Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ورزشی ویژه اتصال به اینترنت
🔥
⏩
به بهانه بازگشت اینترنت ایران به دنیای آنلاین جهانی، روزانه با حداقل دو میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی میکس معادل شاٰرژ ‌حساب بر روی رویدادهای ورزشی مورد علاقه خود، بدون توجه به برد یا باخت، بت‌فوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین:
🔗
bwrd.link/BACK100
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/90649" target="_blank">📅 22:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90648">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sojYM2lu3iJixXbp_QBKvDRIsFtsx5qcIiZZhXmfPCdhKv1a4z2IVa5kyrEWQBF-17cXh3UL7pSa0fS4TjO9kwzH0qx9LrIVOcqkQUHMu0Nj0_NYC9a_7-Xye8FIbao8GRgY8LT9BPus_RARXJa9UgN287XjE957goeoXKYWoy6cYuoHMN2qRgOpUl7pnCV25oiDX4SGDoDpjfN-GgrSkv4H_5ZPd7jhkI4g2iCAMmR0g_X19KTadeziEYC5Bp-E-bE7bZlljMDJBSTQQ1ppnKi2cPOuMblDGSAwizySR8CT8H2kRinViAOgZ0plALfh13kgaY2gWnwh9wkW45Uvkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
رونالدو به تمرینات تیم ملی پرتغال اضافه شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/90648" target="_blank">📅 22:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90647">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e0cb16154.mp4?token=np_VUMoYrOYnOmzLV36frFhwiEt5-mmdlQvov_K-LUSRHkddIYmCLMsnwyCNB_z_hUiA7Kb6stT4nsxeqqzUvU7_pLXE1YQL0aWzwVozc70wcWsbEi3Xa9jYbkQKIGv7Zks5A5fOh1a8aBaKvR8I5bQJOau0dDQOQQpUcTApbSZqzY_IRh6P1GK64qlWkvU9smoO_q1vvBMT6QgsnFDvX43yvIm795p7GKZAW2QeD8JVm46JyhQKu3hbQP6JhsvWqN_h1TtBTTnDLLFakJke2jOj3qPclHL3SdiAIQGQ728b8Db1ZUfPoWjqqWfHeWiI02XXKW2gOJi3pFZM74oE4x7SRQQN9mZacydDfvnNiZvksKupE4ORWgwKe-hoPdyo8Y-tNwgmdtSahviObDvxOVPzVM85N7HJn7C9AllgnY9sBQpqrXNZlh3dIzW7VI8-v4uYOD7EAHWMyIUos67-0-FzUDYguxeuUosBWAFaWESjRnjlt6tGdxZMfnIRmm-Cyitgy5FkvV3O363eyk3S10yZRf_MCWK__7jFeU9QWes6vAZf64g18TiOdp4FWZDn-C8UUjBQSjmc1v9a4td3cZlbBTAbNzcg6CrmdfkxW77ey1u7_jAtl8ZIq2ptPYGNzUfJaC44vtjRzVurwIsvvxiStb0AWlA3E8cQvCcjeoM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e0cb16154.mp4?token=np_VUMoYrOYnOmzLV36frFhwiEt5-mmdlQvov_K-LUSRHkddIYmCLMsnwyCNB_z_hUiA7Kb6stT4nsxeqqzUvU7_pLXE1YQL0aWzwVozc70wcWsbEi3Xa9jYbkQKIGv7Zks5A5fOh1a8aBaKvR8I5bQJOau0dDQOQQpUcTApbSZqzY_IRh6P1GK64qlWkvU9smoO_q1vvBMT6QgsnFDvX43yvIm795p7GKZAW2QeD8JVm46JyhQKu3hbQP6JhsvWqN_h1TtBTTnDLLFakJke2jOj3qPclHL3SdiAIQGQ728b8Db1ZUfPoWjqqWfHeWiI02XXKW2gOJi3pFZM74oE4x7SRQQN9mZacydDfvnNiZvksKupE4ORWgwKe-hoPdyo8Y-tNwgmdtSahviObDvxOVPzVM85N7HJn7C9AllgnY9sBQpqrXNZlh3dIzW7VI8-v4uYOD7EAHWMyIUos67-0-FzUDYguxeuUosBWAFaWESjRnjlt6tGdxZMfnIRmm-Cyitgy5FkvV3O363eyk3S10yZRf_MCWK__7jFeU9QWes6vAZf64g18TiOdp4FWZDn-C8UUjBQSjmc1v9a4td3cZlbBTAbNzcg6CrmdfkxW77ey1u7_jAtl8ZIq2ptPYGNzUfJaC44vtjRzVurwIsvvxiStb0AWlA3E8cQvCcjeoM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">2 سال پیش تو چنین روزی رئال مادرید با شکست دورتموند در فینال لیگ قهرمانان اروپا برای پانزدهمین‌بار قهرمان شد
تونی کروس هم تو این بازی از دنیای فوتبال خداحافظی کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/90647" target="_blank">📅 22:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90646">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoRm8ajFAeCOIA5PJMq4lPINDD3hPk4DgoB97flJ9pBb8YC3OQBYHWx3LorJ_rQDEvvfseC8_nGG9dBs5PHRsgbnQ2v6XxY9oKt6rywhDz3w2Gy1GIrjQYxqOGja8cq-1_H2S_LURkuBWtDE-6kVf1liCBo48C_XLA5oHvwMOPR5w9fIz3vKHE5xA6hp1fidgCLZpp17qgUsRCPq7IrxxNy_wb3aS1BTEIqvrH5wUm7Nfn0z6fZjoSPjW-BSUhXiZFOuJv3CYVpyYxKRt0i6HgKuvIi4Wl_w6bGcSO1MSpPDFOkO5icWFoVnx8DZLl6wtJd6UFM27h6BAmdZNFkmmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
فهرست تیم ملی کرواسی برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90646" target="_blank">📅 21:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90645">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3288c4bc89.mp4?token=V7BHhpHtVyiZWeepJ6YaT39PC0HcwLp8To_90xvLg8Ogu0PKeRA7SwQZSY2vlly6pBZgSzWZ-esagqTJFGChklz8vzHZceqRAykE0Kjd42txaGXhW9fXaYEXvlDxXf320SMa34lcvbxUr6oM_abiTDpJhayIxCNWpMqA8BLxskSTZK1uezpmbb__sEo9uklLG4TC95BEIK_OsTL0w9tCNxzEgGqfEmUrP0RJBvTYrHGjDGEKPefraU1PNLHE2bYg_8MZ0zsjQEZLMxZdyRLRu06fLPm66wtsKMMA4SlwcsFl3_WNGuSfodpsqSWYooTOKXT17dQcOXLE7flT9_4PFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3288c4bc89.mp4?token=V7BHhpHtVyiZWeepJ6YaT39PC0HcwLp8To_90xvLg8Ogu0PKeRA7SwQZSY2vlly6pBZgSzWZ-esagqTJFGChklz8vzHZceqRAykE0Kjd42txaGXhW9fXaYEXvlDxXf320SMa34lcvbxUr6oM_abiTDpJhayIxCNWpMqA8BLxskSTZK1uezpmbb__sEo9uklLG4TC95BEIK_OsTL0w9tCNxzEgGqfEmUrP0RJBvTYrHGjDGEKPefraU1PNLHE2bYg_8MZ0zsjQEZLMxZdyRLRu06fLPm66wtsKMMA4SlwcsFl3_WNGuSfodpsqSWYooTOKXT17dQcOXLE7flT9_4PFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
چیزی که رفیقامون از باشگاه رفتن یاد گرفتن:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/90645" target="_blank">📅 20:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90644">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔹
اگر میخوای قبل جام جهانی با بازی های دوستانه مثل رضا کینگ کونگ پول دربیاری همین الان وارد کانال شو
👇
👇
https://t.me/+YF28GUBRSZkwYTlk https://t.me/+YF28GUBRSZkwYTlk
‼️
با درآمد دلاری پیشبینی های این کانال شرایط بهتر میشه  g11
🔥</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90644" target="_blank">📅 20:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90643">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHYt1dJukp-qaTtZzOEYdy0_P7davXPx4_q_5_u_36OOYVC0S5us_LxQAWGr0A3oBc2lSEzEl0QAioNwjo6-B7JTIZam3QQAZE271poo9HB-zF-oyLKbrtpfBNOJ3UWRTjuI1LsscExe3OwIv-WkVCtyK8I2M_efhgNVh2OU5Zwuf25RvX5AfZDLaYxz7XAj9NIIFsXfwUZr0Gku2csxzYDseIjyPrsDbKA_OYjbFAB-VjI9oR_EOGMnvrzXYE-I8wYI-yyQpcdQeuVSGisHBbqDs5OpC8P3CblTqak-CoqEkb2hOok7PczdddaXGfI_zo3mogfJmZswA1ivid_60A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
اگر میخوای قبل جام جهانی با بازی های دوستانه مثل رضا کینگ کونگ پول دربیاری همین الان وارد کانال شو
👇
👇
https://t.me/+YF28GUBRSZkwYTlk
https://t.me/+YF28GUBRSZkwYTlk
‼️
با درآمد دلاری پیشبینی های این کانال شرایط بهتر میشه  g11
🔥</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/90643" target="_blank">📅 20:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90642">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2260d09ec3.mp4?token=H9PelLdyEm6zpIFVdn60bCyIlvm5Ie6jIzo_MewBGYNjXSHCITsNFDgSNxHxxAgwelZjPJJZMMTeC6peO82rpc4nU9jeU1DU_r16qO-jl-M8DGBLcpAqYCkw39AkMzau1cWHa-dwSe2JZSyqV3uWl-pT4AsipQfdh2AFVG3PBJOrtZ6AG9qUcVx072ljsjRct6ZPFnjER9Y2LWGrJ7vSp4nhaLAD9xmHrvjEaQM0L4qeNpAZjxZ08rQmVDlBSvOyD3sXNlCoTlEXQbfmtLyOI5oCoGMgLRJ1k_7Qx3XBCazxrg5H0rNApBNtYon6soSTcTJgoB-FsOR0SEc4UGL5Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2260d09ec3.mp4?token=H9PelLdyEm6zpIFVdn60bCyIlvm5Ie6jIzo_MewBGYNjXSHCITsNFDgSNxHxxAgwelZjPJJZMMTeC6peO82rpc4nU9jeU1DU_r16qO-jl-M8DGBLcpAqYCkw39AkMzau1cWHa-dwSe2JZSyqV3uWl-pT4AsipQfdh2AFVG3PBJOrtZ6AG9qUcVx072ljsjRct6ZPFnjER9Y2LWGrJ7vSp4nhaLAD9xmHrvjEaQM0L4qeNpAZjxZ08rQmVDlBSvOyD3sXNlCoTlEXQbfmtLyOI5oCoGMgLRJ1k_7Qx3XBCazxrg5H0rNApBNtYon6soSTcTJgoB-FsOR0SEc4UGL5Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
‼️
دیشب نیمار حین واکنش به تشویق هواداران کونش پیدا شد که آلیسون زحمت کشیده شورت نیمار رو کشید بالا
😂
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/90642" target="_blank">📅 20:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90641">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f80cea5c99.mp4?token=TpkU-1BT9A2w65kvk0lR44GU8dw_hDHhoYT7sAzKIrc-wVAoNzHX2WpQbLBulGZROYPWuKNCcmFI3gmxJBorUA7-Bnd9Wg22talJn_GYKI22UY7ZgBpd-7viiSttB7RqQlyY0N2jyyKabPxyZYcSr-NqjYqFoLivt22zE68MRUDQPSTMqrXKMQDz0do2TX3ZEkKIzxFeC2nEbYmnCfA2asTFSt22W4fWsXdhb4tzz88tkelCEWhnBJk0SLP4KWy74dGLKfcLWWxDItfMs7uPa0YXXrfwIJDOfK94ruXR0ZAyKIxe5VtUvf7mBO6F0Psj-gfv3vBjS4TfwSLdpQuEJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f80cea5c99.mp4?token=TpkU-1BT9A2w65kvk0lR44GU8dw_hDHhoYT7sAzKIrc-wVAoNzHX2WpQbLBulGZROYPWuKNCcmFI3gmxJBorUA7-Bnd9Wg22talJn_GYKI22UY7ZgBpd-7viiSttB7RqQlyY0N2jyyKabPxyZYcSr-NqjYqFoLivt22zE68MRUDQPSTMqrXKMQDz0do2TX3ZEkKIzxFeC2nEbYmnCfA2asTFSt22W4fWsXdhb4tzz88tkelCEWhnBJk0SLP4KWy74dGLKfcLWWxDItfMs7uPa0YXXrfwIJDOfK94ruXR0ZAyKIxe5VtUvf7mBO6F0Psj-gfv3vBjS4TfwSLdpQuEJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیرین‌کاری اودگارد در جشن‌قهرمانی آرسنال
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/90641" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90640">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
⚽️
❌
🔵
#اختصاصی_فوتبال‌180؛ فرهاد مجیدی سرمربی سابق استقلال بدلیل موضع‌گیری در اعتراضات دی‌ماه، شرایط حضور در لیگ‌برتر و بازگشت به نیمکت تیم‌سابقش را ندارد و شایعات مطرح‌شده پیرامون حضور وی در فصل‌آینده کذب‌محض است
❌
درخصوص نیمکت‌استقلال طی روزهای آتی اخبار…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/90640" target="_blank">📅 19:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90639">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
فرمانده قرارگاه مرکزی خاتم الانبیا
:
با توجه به نقض مکرر آتش بس توسط رژیم، در صورت عملی شدن این تهدید به ساکنان بخش های شمالی و شهرک های نظامی در سرزمین های اشغالی هشدار می‌دهیم اگر نمی‌خواهند آسیب ببینند منطقه را ترک نمایند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/90639" target="_blank">📅 19:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90638">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e11054c811.mp4?token=fSJOAHozCImiC2uYemyLta5HeZ_fV7jb_e_zxP2LnOf9ob7ZkwUejkDneb5y4t1bA5emn4DTnncKbTkJNP_y17xNfXYjCNqjWWqkMRNr-CSRb5DR3HK9utHtjjXSyMEV81yHfcS4pGVqIdef57X4Y6qa4cGzK6lPFEC6cbl6CO0WObOq1hy03S-Cno9FS_dXk_v_LEG-JWTAvM-HEuCXN3aYspNIxCuIZbO5Q7rwjynzNYj3mMBjKVEpzb1V3kVoIFE559g5qhYXRIB4MCRhNt0j15slfMdOHMs8NJ0OX-_gicFFcJZ3CCIHc8EDOe9KlCvrBmofkyB540BA73N45Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e11054c811.mp4?token=fSJOAHozCImiC2uYemyLta5HeZ_fV7jb_e_zxP2LnOf9ob7ZkwUejkDneb5y4t1bA5emn4DTnncKbTkJNP_y17xNfXYjCNqjWWqkMRNr-CSRb5DR3HK9utHtjjXSyMEV81yHfcS4pGVqIdef57X4Y6qa4cGzK6lPFEC6cbl6CO0WObOq1hy03S-Cno9FS_dXk_v_LEG-JWTAvM-HEuCXN3aYspNIxCuIZbO5Q7rwjynzNYj3mMBjKVEpzb1V3kVoIFE559g5qhYXRIB4MCRhNt0j15slfMdOHMs8NJ0OX-_gicFFcJZ3CCIHc8EDOe9KlCvrBmofkyB540BA73N45Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جام تو خونه میمونه
😉
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/90638" target="_blank">📅 18:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90637">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLmceFbtvrR8wv5wRdwH8o9QxxQ16qqWjHMk6KiM3p4x2LTfjCKwYwtjtQr95VnRKDKQEZdrYS6ELUsbwm2Gytu2TonGPU6Hi3r-ieF3_VCmMPCvHCmyzWmrxMeSmlVkIithwztMiHthrzLYOqHj1QESqMFr8FCNebyqeOix6B3ueOr6X9IdP_cIT8XPW3CagGCsQUVgYCCmL30IsDmRLbvFmvbLBB9bgnD2GPOYyBIyA8GaUTnK1oMqpXdnE5URf5_O-PFW_sJYW-GY_BjyOsSypJXTqne3sTtCkMC2O-MsDF73O-L4O7QxHyVtUwtDFLPPMO_6guNNLFiUaHlosg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بعد از متصل شدن اینترنت، معاون وزارت ارتباطات برای اینکه پیام رسان های داخلی ناراحت نشن رفت از کارکنان پیام رسان «بله» تقدیر و دلجویی کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/90637" target="_blank">📅 17:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90636">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V6pLGWUC7yfkVvOPDpV7Q5iqJh60_aCLqJ-SEhMcecPL_baYAYnv4BamztSA7OduNIlIosjt-mEclDH6ibcDFfVWaLHJwZUdqunim1B8iVyPYNjh_dXtL4GwPGkw1lWDP62FTmIAhuoTh3Gcl1tmetjVI9jJWwmqdlMjhCT0NmiBa97azK05gFdMpA-p0B92Qjde0A-3_PcjDkeyIc0R8nkhJhnEM3INW536DB7kMLKriKV5w3WXZAYu0TB1g6xvPm21NNL0CYpPCgqoQXxMDFcYzBq1jbtVWn7ttvZ9JaW7Lg-Zud3lvzmUWRNhQoaLMMtZ_RmCKkc8iSeDxGuMLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تعداد قهرمانی هر کشور در سی‌ال:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/90636" target="_blank">📅 17:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90635">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a15c25cc8b.mp4?token=FrF6XICN_d7A9GiHgHCfQTay6sCopaHK6PPJ-ojhTWQHkS8atO3rLVqxuBafaE4m26EVm5KLLs7mXfvulbkOOqx-3XtmwiEAkiIzLLzI3l9DKqNMi0QK5tDFZgYwBdwZzRHSbGZQlaVeKVmd2hY_U10qFpVFTmgYKCGZ0EglLlS0GKvGX2i2wfqkgQuNWJuMJv1eH9yZk01zzvfJZJ3q0NVZDM-Bb8qDqe2ESUHIEGLttrOzSSk9H32HJQM7FaQMd5JkVaPNyMj5V6c9p8E18Rd9Z96M8rXyJts-tIaeIn0sBptR-Qu3inotFdzSGX50uegb7tzK1szHVjCxS8nXhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a15c25cc8b.mp4?token=FrF6XICN_d7A9GiHgHCfQTay6sCopaHK6PPJ-ojhTWQHkS8atO3rLVqxuBafaE4m26EVm5KLLs7mXfvulbkOOqx-3XtmwiEAkiIzLLzI3l9DKqNMi0QK5tDFZgYwBdwZzRHSbGZQlaVeKVmd2hY_U10qFpVFTmgYKCGZ0EglLlS0GKvGX2i2wfqkgQuNWJuMJv1eH9yZk01zzvfJZJ3q0NVZDM-Bb8qDqe2ESUHIEGLttrOzSSk9H32HJQM7FaQMd5JkVaPNyMj5V6c9p8E18Rd9Z96M8rXyJts-tIaeIn0sBptR-Qu3inotFdzSGX50uegb7tzK1szHVjCxS8nXhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇧🇷
Vini
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/90635" target="_blank">📅 17:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90634">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da899e08a7.mp4?token=bn18A_XFP04lXMc-xVNN6ltkzO97huXMu8tAhTTwJrVCFWVXQj3lkXHYk8CuFchTrn34QjTiLdKTrojGmjjb0tAn8ViBWPcdJ6Oz1GiE-5nO_ngXXN4n-XMgJVl0onF67cSMsLpZ7oNnePwhJha74oIv7E4nKqUrNZY4acveWGo0uJhItqfmNQhJuvbfFkpBfrPSHtZVh8sQyvcllyf1QvAwqvErApkja0Q2eIv-8eB9vopNR2hntqli8_6pRotAyDGFO2S3y_dC4uw9oXfupIoCkO9M4L25PuuX8AE6h-KWOLwBQTcSTrNKKvQvE5_EhIdeRrS667LTvR6Cgem1Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da899e08a7.mp4?token=bn18A_XFP04lXMc-xVNN6ltkzO97huXMu8tAhTTwJrVCFWVXQj3lkXHYk8CuFchTrn34QjTiLdKTrojGmjjb0tAn8ViBWPcdJ6Oz1GiE-5nO_ngXXN4n-XMgJVl0onF67cSMsLpZ7oNnePwhJha74oIv7E4nKqUrNZY4acveWGo0uJhItqfmNQhJuvbfFkpBfrPSHtZVh8sQyvcllyf1QvAwqvErApkja0Q2eIv-8eB9vopNR2hntqli8_6pRotAyDGFO2S3y_dC4uw9oXfupIoCkO9M4L25PuuX8AE6h-KWOLwBQTcSTrNKKvQvE5_EhIdeRrS667LTvR6Cgem1Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حدود ۹۰۰ نفر در جریان ناآرامی‌های پس از قهرمانی پاری سن ژرمن در لیگ قهرمانان اروپا در فرانسه بازداشت شدند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/90634" target="_blank">📅 16:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90633">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🔵
باشگاه‌استقلال با محمد خلیفه به توافق اولیه و شفاهی رسیده است اما این گلر جوان اعلام کرده که پس از جام‌جهانی و برحسب پیشنهادات دریافتی دیگر خود، تصمیم نهایی را خواهد گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/90633" target="_blank">📅 16:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90632">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b05db8d1.mp4?token=ZmSNC0BQKtOGx-SO2xdGTde5BD0PRJ3a2Vj4sVispQskBSYva_t-21jbad3jTIkmk4kGRjYcXQ6kCerswKd8VCf9AT4Q-XHEX18_N1eS0nlBlIOlI5gJjzbFL-Bqgl5YJ8wluxcpj1SM6sNiXPOaj56kJUdzmBy7pUAxrLGwEYsav9NAqQwwUCNMOiOo7FeMqCinQM7rIQ-kRjxDWb7l6hwTlBxPMDiTGLXVfan9Hn0lJJe1PsNgNREQwwXW1x82PMiLfgDOOaTKgV6bIsJgaTDrOp_Vm3hHnwenQEK5nQVurbhbGpAiqlxlm-eGiXsfG12yzf82qxi5rGuLwBeBvGBsyK8SayhQdRhVyXBC_cXO-UJN2MnIxneGEXXogantK8pGS_lJYz4vmIxcU0oAZf8iFopftSI4fWQLhes3EE-KWOHnWzcXrxCkOtGS64hChvkaK2PYlpDmJ5ZawV-LIwn1jHZ13ZfeM_n5U2R4-eGMZaUXSyDWZBzmOvRd_4trFnKAXlZ2hkTPGLlnUgKQujpvEsQQwGk00T-winHXpWdaFN4qiFFq7i7fLxeBcmlnKDm-no91YZ6vfcV7IJ2VK49-o2Oh1cuVky3eKJzhqnjLgEqHCUxoejsZv-sKUQRcd1nimYQbHFBeOWCOgBvJWzy4gUXSZL1Rm0K_6erHsjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b05db8d1.mp4?token=ZmSNC0BQKtOGx-SO2xdGTde5BD0PRJ3a2Vj4sVispQskBSYva_t-21jbad3jTIkmk4kGRjYcXQ6kCerswKd8VCf9AT4Q-XHEX18_N1eS0nlBlIOlI5gJjzbFL-Bqgl5YJ8wluxcpj1SM6sNiXPOaj56kJUdzmBy7pUAxrLGwEYsav9NAqQwwUCNMOiOo7FeMqCinQM7rIQ-kRjxDWb7l6hwTlBxPMDiTGLXVfan9Hn0lJJe1PsNgNREQwwXW1x82PMiLfgDOOaTKgV6bIsJgaTDrOp_Vm3hHnwenQEK5nQVurbhbGpAiqlxlm-eGiXsfG12yzf82qxi5rGuLwBeBvGBsyK8SayhQdRhVyXBC_cXO-UJN2MnIxneGEXXogantK8pGS_lJYz4vmIxcU0oAZf8iFopftSI4fWQLhes3EE-KWOHnWzcXrxCkOtGS64hChvkaK2PYlpDmJ5ZawV-LIwn1jHZ13ZfeM_n5U2R4-eGMZaUXSyDWZBzmOvRd_4trFnKAXlZ2hkTPGLlnUgKQujpvEsQQwGk00T-winHXpWdaFN4qiFFq7i7fLxeBcmlnKDm-no91YZ6vfcV7IJ2VK49-o2Oh1cuVky3eKJzhqnjLgEqHCUxoejsZv-sKUQRcd1nimYQbHFBeOWCOgBvJWzy4gUXSZL1Rm0K_6erHsjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
ازبک‌های‌جذاب آماده رقابت‌های جام‌جهانی
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/90632" target="_blank">📅 16:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90631">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/079475458f.mp4?token=f9bbqdLURvCLoHb2JFTI8lolH5uuBZHUH5j7AUx2Jns2QXzMdCGeL99TGiqJjJhAzksT6F9TH608tdVA0bchfUNaYV6rrNEgjESCqX-REQFJsMT5LA8UfhYiEGN9iyrEXJlnTJfDHuXoNAFkhIZ5KVNODTz8Ol3C8NYwWiunztKD8ze8y34zAqi9leSQt_APyiGrnZPBh9RqiJ8mHdnlgx_XW7YWaMC2Zn1-RQvH4EUYKsMTgWboqB-AAt58Hgjssb4V6e1gAZOett-JyOgwaR_EcjVrHje9a-VVDEHfdqlFRLEjsLv0I0ezyNKwTkpd1TWQgKDX2xCWY3nT0ByEvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/079475458f.mp4?token=f9bbqdLURvCLoHb2JFTI8lolH5uuBZHUH5j7AUx2Jns2QXzMdCGeL99TGiqJjJhAzksT6F9TH608tdVA0bchfUNaYV6rrNEgjESCqX-REQFJsMT5LA8UfhYiEGN9iyrEXJlnTJfDHuXoNAFkhIZ5KVNODTz8Ol3C8NYwWiunztKD8ze8y34zAqi9leSQt_APyiGrnZPBh9RqiJ8mHdnlgx_XW7YWaMC2Zn1-RQvH4EUYKsMTgWboqB-AAt58Hgjssb4V6e1gAZOett-JyOgwaR_EcjVrHje9a-VVDEHfdqlFRLEjsLv0I0ezyNKwTkpd1TWQgKDX2xCWY3nT0ByEvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
همچنان حاشیه‌های دوس‌دختر امباپه!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/90631" target="_blank">📅 16:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90630">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfc7d5cd4d.mp4?token=DhRhJnGvs-ISdQYg8JBU5Vhet2SLtOAtbORplZsdqqM9ErYitr8tQ0n27eu6A0cDYR23BN_PXK793NPxSIZWQ66Xhc3-X5SrB5we1IWFr5RnZqdC6t--eQVGBt7B0fM0IfgQlXIVIGlDAxRrdZWRza4r7GAtke5_k2WqVygA0GFuqvW0tHgafc9OjJhSxx7pms1ikUm5B1UhU2ErBHAbx4KKMlyDKaHzi5IULtynGEYzlREMICFmLb_iu8Mh3ZAqeMrIylh5L2INt7ASHhU4Ajah3mlzQnIfUecjtslq9Ak3n0rbtpv8S4o8SyVs8mOAhVEeqzpUPwqTJTTBlsPs5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfc7d5cd4d.mp4?token=DhRhJnGvs-ISdQYg8JBU5Vhet2SLtOAtbORplZsdqqM9ErYitr8tQ0n27eu6A0cDYR23BN_PXK793NPxSIZWQ66Xhc3-X5SrB5we1IWFr5RnZqdC6t--eQVGBt7B0fM0IfgQlXIVIGlDAxRrdZWRza4r7GAtke5_k2WqVygA0GFuqvW0tHgafc9OjJhSxx7pms1ikUm5B1UhU2ErBHAbx4KKMlyDKaHzi5IULtynGEYzlREMICFmLb_iu8Mh3ZAqeMrIylh5L2INt7ASHhU4Ajah3mlzQnIfUecjtslq9Ak3n0rbtpv8S4o8SyVs8mOAhVEeqzpUPwqTJTTBlsPs5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
دیشب بازیکنان پاناما بعد شکست ۶ گله مقابل برزیل برای عکس با نیمار به صف شدند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/90630" target="_blank">📅 16:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90629">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
لیست نهایی تیم ملی برای حضور در جام جهانی 2026 اعلام شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/90629" target="_blank">📅 15:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90628">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d59f93bc5a.mp4?token=nuxs2WXTSYbX-KxOoooYj4KZiT8-Vr669TBlzKpxt4mX5XFZzNDZPf90DE95soHCqVXSfs7MZ18mo8t1dQ3LaUHARPrbdkU8D60ET-t9FPWQk71ZW6MQoLVpAevsnhFeNq6-yt6ddDRfBO7v_XxjB7yTX6_3-TWEOPH9GDLNUq0RLB4ApX2cJ_bxeNxAm21N_1skVCUTPax5zxK_ZW0GsqthDMS29f5JSRUpeD-SnkMkuYDrR3EjU0LTViQmH9oN1-uEgqBfemK80VWn5GrVB0AxR6Be97vJQ9Hwl6EQIUU0pU0GelCrgNpc9_BXSca1QD15fCJc-H4m9mfAgrlQ_1uJjvb0W1NfKeNY5QOQp-g2jfEi4jnAk_LjwumEgSaxU0yTCikFa2e-phVgdtpI7yZzgy1ZvJCAaSEob-fb4vMAmXkqL9T2uWwamDTW2jJ4JhFTy6lDu0AJX_1fuyYlC1PyzkYPxUZfQvc9yk4WXClARt_iGZ7s8xPI2_debzY0i3rr3KbohYcW6YYNYgrh6hmMHqr-862mCF0ZJzHrTq2Tx76-buFzsuFucS9eBNod-Ej4xmeRZaPLwCG9Bf-mAKy8JllsM06L349aE7ravKSJ7RuqWdzkvxEJDZERPaXKFumbhIONNxjgXH4S_Vgp1EIPmdnU8K7QHI5W5vebdIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d59f93bc5a.mp4?token=nuxs2WXTSYbX-KxOoooYj4KZiT8-Vr669TBlzKpxt4mX5XFZzNDZPf90DE95soHCqVXSfs7MZ18mo8t1dQ3LaUHARPrbdkU8D60ET-t9FPWQk71ZW6MQoLVpAevsnhFeNq6-yt6ddDRfBO7v_XxjB7yTX6_3-TWEOPH9GDLNUq0RLB4ApX2cJ_bxeNxAm21N_1skVCUTPax5zxK_ZW0GsqthDMS29f5JSRUpeD-SnkMkuYDrR3EjU0LTViQmH9oN1-uEgqBfemK80VWn5GrVB0AxR6Be97vJQ9Hwl6EQIUU0pU0GelCrgNpc9_BXSca1QD15fCJc-H4m9mfAgrlQ_1uJjvb0W1NfKeNY5QOQp-g2jfEi4jnAk_LjwumEgSaxU0yTCikFa2e-phVgdtpI7yZzgy1ZvJCAaSEob-fb4vMAmXkqL9T2uWwamDTW2jJ4JhFTy6lDu0AJX_1fuyYlC1PyzkYPxUZfQvc9yk4WXClARt_iGZ7s8xPI2_debzY0i3rr3KbohYcW6YYNYgrh6hmMHqr-862mCF0ZJzHrTq2Tx76-buFzsuFucS9eBNod-Ej4xmeRZaPLwCG9Bf-mAKy8JllsM06L349aE7ravKSJ7RuqWdzkvxEJDZERPaXKFumbhIONNxjgXH4S_Vgp1EIPmdnU8K7QHI5W5vebdIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
یه‌کم از جنارو گتوزو ببینیم که دیگه بنظر بازیکنی تو میلان و ایتالیا مثلش ظاهر نشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/90628" target="_blank">📅 15:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90627">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oi0aRxVEyUM_jSZd62XlqeqIj2JtDRy0f352VnntkYKv-V3qTLE0BbSkEMNuOr6WnjeVQPbbXwn8tpzaMT2Y6s5EjPPeloBhrTw4m8vW1X3plb9S7WSFC2nWtt6wFmx8jRp8D4UDXBE-EiKTC4-FNMV09ol7LB19iA4_ftmoLqVT269PqQFuPnWQJ5ZLKpAmLEtGMzQqS8P7KWBycV6ntpnvfUZQjnP5YjrNjSFtKks834jWP21Bp45CpemlYOtQmwRNraHYob7HkxG6MgjERPo39SaMGDRobfl0546jxrbspnkwu8Apb0ciOP1326E8RvgROMuBXuQYS4GAT5JQSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست نهایی تیم ملی برای حضور در جام جهانی 2026 اعلام شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/90627" target="_blank">📅 15:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90626">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda3613d9c.mp4?token=ftS3KnRfsM_mG3_s76yAELwf5nGuLYn0EZIVJ5wIyxyZT6lqOFai18wc2Ij_G1JVquQaSFhYTfSKXeUs0P0qQLU3_ZkBkYjv98oiDsJVEAq3F4ZpZEM6yjGGD9qRv2-ZfLZui-_Y1GabhEtoqpa_YoIVtR2tyeAOgCQxfpzCdddXnqHIKWvXYMdR3KXrMxtIBoQ9Vff0477Bt1SLXrtE7jK8EkXm00yGsK49clgOZNa7P38WRHapy8ogO9sRnWSeO9M6A9QPjdE0t-Q6gWqWkNIVjufxKqSmSACfFUcU8b6D3qFUVQzIqGFafNDSlurRWjPVW6SqLmNhJ8H89mk3Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda3613d9c.mp4?token=ftS3KnRfsM_mG3_s76yAELwf5nGuLYn0EZIVJ5wIyxyZT6lqOFai18wc2Ij_G1JVquQaSFhYTfSKXeUs0P0qQLU3_ZkBkYjv98oiDsJVEAq3F4ZpZEM6yjGGD9qRv2-ZfLZui-_Y1GabhEtoqpa_YoIVtR2tyeAOgCQxfpzCdddXnqHIKWvXYMdR3KXrMxtIBoQ9Vff0477Bt1SLXrtE7jK8EkXm00yGsK49clgOZNa7P38WRHapy8ogO9sRnWSeO9M6A9QPjdE0t-Q6gWqWkNIVjufxKqSmSACfFUcU8b6D3qFUVQzIqGFafNDSlurRWjPVW6SqLmNhJ8H89mk3Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇳
کشور سنگال با انتشار این ویدیو نوشته که ورزشگاه لس‌آنجلس یکی از میزبان‌های جام‌جهانی مشکل جدی در چمن داره و خواستار بازسازی فوری این زمین شدند
در این ویدیو مشاهده می‌کنید که توپ با برخورد به زمین ارتفاع نمیگیره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/90626" target="_blank">📅 15:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90625">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/90625" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
✅
🎁
کد هدیه 100 دلاری:
Sport100
🌀
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🥇
صرافی معتبر
🌐
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90625" target="_blank">📅 15:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90624">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">چرا این روزها همه سایت جهانی
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🌐
اسپانسر رسمی لالیگای اسپانیا
😀
مورد تایید سازمان Gambling Judge
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90624" target="_blank">📅 15:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90623">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4y2uePdPsTQqsLJ8Exj5TiOcITSPCZt6OK_qZ4sXNBSfnPSoNCgwKotlZl5XN-74LuZ0vY0ZBee3uzsKRG-ooOQig4FJD7mq8Ch67UxXaSPsjZaoyZKtShfoorZkQfAFdAirZABQa9KIDahYiLuY0BKzwOLnrnCu8S1kAapvuP-H9dQ3eVAZHkxLMyXYM1avrR1g4wjRL0DugDvPUjx6s3oGQEHC2mycrGdOVbJV8NVlvprtPXIMaNwMQ20U3q8lBiXltmIunFbYFL4qnQjnQKTmCJOvgkdF5i1DcenstKcnZIfo601vBIFrJjOjgWjfbedGbp2-z6Alh7PU6pkkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی و بادیگاردش تو اردو آرژانتین
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/90623" target="_blank">📅 15:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90622">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIdQCUTZqodTEZoGPadtucSjK-oM_yYtAIpLjdefvHhi7iPuM6TdZjhX2dRulo64pq7rno7Cq3E9s2AZtsHI_HJDM16bA_kPNYIJC3tYpFgBufP1NLr53K17sA8S1Uzqg-5Pf-zoouJczkziLBJ-zOmyu9JNGhph-IW9nmFJJaqtzK2wVlykcrPacy6XxuZuq7eF6YpngDYCqiGh1R99h_J8NjmwDPLp_6I1NMedR8wtg3jEa3ub4kxJ8S2xfTQCBrzbs80WCpTsmpA21kV4VbsMZm84G7BD7iKfr-w37rwdqhBoG_YYKpkOZj0SM2Zf8bQ_wBpgWvgWS7_1q0iv6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فووووری
؛ با اعلام رومانو، قرارداد آنسو فاتی بازیکن بارسا که به صورت قرضی در موناکو بازی می‌کند، دائمی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/90622" target="_blank">📅 14:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90621">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0da9f9a8d6.mp4?token=egjo9xzCD4p_iH7ENEZgNXr4xP6eZl0XPlGvzM7Zbo9_uVA4PB_IF1jYMMvd5DtllJwO031FBv6FP1K2CSFG1_oMSqm4t3M1ybdfSk0-BTPTsV9nBrDcNbyI93Pqg2vcOtpFOvSgQDCcxFYcbUzn81CWq22oM1-f5QYduLcZLqhpXa4CBeZ5886DP-TY11hW2QcT6lDeO1cDztcgcubVC5UkBGfLKemfHDOdiXCeRI43vyFU4FOeK6kWzWpM1cUk2twDWDZWC9YtOcHsi3SM3jjpcdx7b5iZxwMGk2XARK_4mA1KjL9OUS7Uf82czstc4js3YbGMGyoB-i5TyiiL7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0da9f9a8d6.mp4?token=egjo9xzCD4p_iH7ENEZgNXr4xP6eZl0XPlGvzM7Zbo9_uVA4PB_IF1jYMMvd5DtllJwO031FBv6FP1K2CSFG1_oMSqm4t3M1ybdfSk0-BTPTsV9nBrDcNbyI93Pqg2vcOtpFOvSgQDCcxFYcbUzn81CWq22oM1-f5QYduLcZLqhpXa4CBeZ5886DP-TY11hW2QcT6lDeO1cDztcgcubVC5UkBGfLKemfHDOdiXCeRI43vyFU4FOeK6kWzWpM1cUk2twDWDZWC9YtOcHsi3SM3jjpcdx7b5iZxwMGk2XARK_4mA1KjL9OUS7Uf82czstc4js3YbGMGyoB-i5TyiiL7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
یه بلاگر اروپایی اومده فینال چمپیونزلیگ رو اینجوری بازسازی کرده. حتما ببینید عالیههه
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/90621" target="_blank">📅 14:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90620">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-DJQsa8Khe2CLPxBHvzDkPGA7QUKWF3ZXnfEEn3_eEA3YKGQhEHXn7k1i9I_zwUhDUCEs5wX3rQXzZgfH5kc2bMhRrRXE7162l0PbXzu7T5RW_ZnqHAV3Oplg4QTd_0CVC_XEmaR082rl05h0TXPkFb0Qp9zwPQEIBhcIwMtMsOtNRxMBVimsagfnfYYrRT65QCP5Zr8n5l9rjV2RH37zgAeqqNUMfpW2LLMbWTXntlKxhK6cKezGy6av3cHVfxJBs01Mv7qfx4XBtt2Li6Y9s5VWG55CD1CsUgQu2A-qf5UTfqmXKZVl3cTR7iCpX-EGOityPj0rfkd4G2X8ZaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#نوستالژی
؛ سال ۱۳۹۳ و همزمان با جام‌جهانی ۲۰۱۴ برزیل، بسته‌بندی خاص چیپس در ایران برای تزریق نشاط و تماشای مسابقات در ایران...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/90620" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90619">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
سرزو (رئیس اتلتیکو مادرید):
«جولیان آلوارز بازیکن اتلتیکو مادرید است. نه فقط برای فصل گذشته، بلکه برای سال‌های زیادی در آینده. ما همیشه در حال تلاش برای جذب بهترین بازیکنان برای تیم هستیم. تا ماه آگوست، وقتی لیگ شروع شود، هنوز زمان زیادی برای بررسی، پیگیری و انجام خریدهای جدید وجود دارد.»
﻿
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/90619" target="_blank">📅 14:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90618">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wh_KrYmsaaKVdwtzHcVHFpIMRmJ6CvJhHc4aqiHGsM4OIb-HSqMkh3m1ovea41n_X2kXvvS79Ld_U3eDta7N8zhI_KAfZBzBdtW-hkeZHNdf6ZphkgbnKOvCNrtmWylhB6_a3kqsBdP9jKaFq5hoigdwsMWTu9gQkJGZw2vSk8SL9ZA1yQ4DKnCda1py8dfA1cQbdbMdBxtldWSZbUqZTbu7MF2u2XQ3J5Z6F6MR02pibIXBoz7ePYPKUWLpgosMm1aRDYLSUMYrBljTkK73eSxWd08C5WkR3IPlpNUY9WZNMQwF_WK5RdgZ_xeTVDwfImGm3X4QZotf-atkfXbfaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
⭐️
مقایسه آمار دزیره دوئه و لامین‌یامال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/90618" target="_blank">📅 14:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90617">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14d1ebf50c.mp4?token=aVBWVe-TLoQYbsRXQx3Invrd04KYFFDXgP5iT-MazsnO7pBFFqP_bQGMBGVZIpbPLgH-KKC8ZodjEIKbGbvlts38ZNqBQs_UbRpGhH4E-bnv6l6e6vPPouvdmQ-ffUktg96_p4QCpiKuKCYDdkq0wkR36-QnSxuu3LwJ9WuyFCxBanBgX0-F9CJKSNVWfDalUAA24YGW-3EfrQKYXEUF9yVhEv6tkc55i5OTsjU6eQrkqE4oqq3DEzwiutJwBCupO6t70uWjOAjc0EZ3SOXNdCbFPor0JIBxMI1hX8iFoug_suBMji612SKO9vjsh1cs5lMsU69th0czmG0clT0ieIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14d1ebf50c.mp4?token=aVBWVe-TLoQYbsRXQx3Invrd04KYFFDXgP5iT-MazsnO7pBFFqP_bQGMBGVZIpbPLgH-KKC8ZodjEIKbGbvlts38ZNqBQs_UbRpGhH4E-bnv6l6e6vPPouvdmQ-ffUktg96_p4QCpiKuKCYDdkq0wkR36-QnSxuu3LwJ9WuyFCxBanBgX0-F9CJKSNVWfDalUAA24YGW-3EfrQKYXEUF9yVhEv6tkc55i5OTsjU6eQrkqE4oqq3DEzwiutJwBCupO6t70uWjOAjc0EZ3SOXNdCbFPor0JIBxMI1hX8iFoug_suBMji612SKO9vjsh1cs5lMsU69th0czmG0clT0ieIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بالاخره یه ایرانی هم پیدا شد برای تیم قلعه‌نویی چالش اخیرا ترند شده رو اجرا کنه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/90617" target="_blank">📅 14:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90616">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dx1m1uydgwl1ms4Kqj91WH22P6RKokP4jpNuiWZ6xlIZzN256CanwoENXr4wPEiCyL4nnLaWPQt1ZAy6UG_AFsZ7X0PQ8KTZTSBywf40l0iLjCUl7Wp3zYvBp5T77pU5LdNlq-quzDWCrvu4bK5UIb3TPfOr9tV-LesmVGZkYENI1a4zWzqv3hzKXX8S1Npvrbff2MdG87YOuUZJTpxA71q4JSNBjS-UOrnCPsbvheqbu-wymOBf8YTTsgUlNWNxWmN_2rOLtxWEkdFyH5PIhF4OC7zg0WjCS5MLa2zPZKupAJToUwB3ZjD5Bf6TtYkvtblljsjjF0F38u8HyD-fsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
داویده آنچلوتی به عنوان سرمربی جدید لیل فرانسه انتخاب شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/90616" target="_blank">📅 13:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90615">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
#فوووووووری
#منهای_ورزش
امروز حوالی ساعت ۱۰صبح در دانشکده پزشکی قزوین، یک دانشجوی مرد در ابتدا همسر دانشجوی خود را به ضرب گلوله به قتل رسانده و سپس با تفنگ، به زندگی خود پایان داد. سپس این دانشگاه تا اطلاع ثانوی تعطیل شده است
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/90615" target="_blank">📅 13:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90614">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a22b3eef4.mp4?token=DCRP45FD8vUCLjstadA8FRFrOTF1z5v5oPqCBww5q6Vd92vJgFwWeGlcZMk87UExvmCYObC5rjFliRBhQumxnn0GB_5-FF16_L8pRdO8tYbDgZ8Mc43v2VBrx-XTM3iYaxa6QHNpKv6370bP6-OWyDVYuhHw8NR8916KSB6AjuBVjnfEQqlshIgRZNxNHiNUQREvO_TSuIpkDTvcaFNqZbFic9X8rb5zQe4oh7dValTKpxum6cqKrE81nVg4vTk94-sN6iTQii1q8vRGAny0MbDvheihwX9p9SIruFLGQsLrScOFSaikpJvClkRBTTAXcy69joQ4gEbKt3JsgO8IsTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a22b3eef4.mp4?token=DCRP45FD8vUCLjstadA8FRFrOTF1z5v5oPqCBww5q6Vd92vJgFwWeGlcZMk87UExvmCYObC5rjFliRBhQumxnn0GB_5-FF16_L8pRdO8tYbDgZ8Mc43v2VBrx-XTM3iYaxa6QHNpKv6370bP6-OWyDVYuhHw8NR8916KSB6AjuBVjnfEQqlshIgRZNxNHiNUQREvO_TSuIpkDTvcaFNqZbFic9X8rb5zQe4oh7dValTKpxum6cqKrE81nVg4vTk94-sN6iTQii1q8vRGAny0MbDvheihwX9p9SIruFLGQsLrScOFSaikpJvClkRBTTAXcy69joQ4gEbKt3JsgO8IsTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بعد فینال Ucl بخاطر شرایط جنگ در اروپا، استفاده از پرچم روسیه برای سافانوف گلر psg ممنوع بوده اما دوس‌دختر سافانوف با چنتا تیکه پارچه برای شوهرش یه پرچم می‌سازه و بهش میده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/90614" target="_blank">📅 13:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90613">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIYSatwQlCKme3xKiR86v_y50juvxIJiyWkrVI37AS_wFjql5bKU9SZwcZGFXNSX3KPjLhk_jVcumcx03fB1GoTWbtgtRkNWlMFgYFdlG4aLKuwt-p3ptBjl5PRyjgslJn9Laa_weyELjejoNqGArX-nrw93X4JwiJY2Ot-_I-Jmp3gq6hrtYC3gRRFNDMJPynJ5TXvXh4AU8e_tIR7aWaB_NyOs8tW0M7x1kT-BExQ-12SM0pGQkMrcwskB-UYheu16apljiLGFFX8RTb6_lWulsqXR-aAPu-ZrJ64C-Zzg96rTIsTlq7psruymCAJsrxzUuuxd3OZu8hV5iGT_Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
|نمایندگان انزو فرناندز درخواست رسمی خروج از چلسی رو به مقصد رئال‌مادرید به مالکین شیرهای لندن ارائه کردن. فرناندز گفته به هیچ قیمتی حاضر به موندن در لندن نیست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90613" target="_blank">📅 13:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90612">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8WuQ7ryTMwdPLu4uWjKUeSWhIkTlYOZTu8G8L0f5tzgAdeukmjKOOeQ4PtApzLaJLtdaqM1CQGHvWV_YM2l7WIme_8_5FC-vd7PFPJoHF2xoPC8vyG86yqQAiix7LwPVi-J4zUYh-PIgA2LohyGzZn_gxY_MiIvP41KtI9bA3vrIw5ZEalXRMFSQQ1utpNS9nlHXUip2juSF3U83PgYA2ydk1WwXwuSwNVi_sqPrXs5uo17oVDhYeGlvCq3M_grxrBfBn8uEQhP4s5B53MGU4bme_gFgqEuEJ2IPWrzQb9nA3Es_AN_FYXzuo27gJq61mBH70ggvPqMCbwEToPkaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
مارکینیوش با عبور از دنی‌آلوز حالا تبدیل به دومین بازیکن پرافتخار تاریخ فوتبال شده و‌ فقط لیونل‌مسی از این بازیکن جلوتر هست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90612" target="_blank">📅 13:20 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
