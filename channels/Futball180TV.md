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
<img src="https://cdn5.telesco.pe/file/Z94rPtLCt9ntGAgePpfzjchZ_JqVA6gFLKnzwPb3nDFBUWn-8CFcOZ_hGqrI7v92SHOaH-haX17CN7KzjNTijwlSs4YdsIVsMgf2g0igPslQW_M0LlyX129bxZSZBVK2Yht-qWqOss4w-810z4Poit7_Z_wMMk4kJG-_09YypHEYvGDsV7x0wUZRe7zAMPcSiPWSpw4IsTgx9XLrUnZ8AB4XLL4Yovm9GtZ96PABwTcU509d4HPAGs4ff9FSofaVf-33dgWpiEtMG8HA_sbRNFCediNf8beyW7P1W1OoHqb_pnxrWvwv7yQGyGw0VTc-gMmiDhXA52vyY6FOzIDu-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 507K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 01:04:36</div>
<hr>

<div class="tg-post" id="msg-102482">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edBSh1GaeRuz_SnJxCe5heoOIidGWrOlkBi4pdNa_Ybi_mWeqsTS61lTv2C0PauZ9jUPilccCnod-EgQAlFJ6a63Y-FItjqTHRJTaBGqcl_PQPJ8BMT5vx3n9WJS2XIoRgKL2YpY6R6XYm5qT2q-wXY2osRlAT0jxsdnigDNibr5sVcfp4SINpnH3W4nmZEb7yEVzehx3nWVJ1LwsAcaRLnSv5WskzD0mi3SIRY37VRlYAY8s5QKyYaxwymBJNjeqmUma0HB62tBaTy-NU_if1q2Nin74ynFXTSoM4LnJ8tWZa_93tmBU-J3-dbTdRdvULplIIrpoJRq7y35TJTtKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 613 · <a href="https://t.me/Futball180TV/102482" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102479">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y1lY4nX_NS_1lGl76WSpFtpCttQvzASce0ln1DlP_oDEJRzHqR35SfCbeLIGQft_dvHjRD78kE2boANSDaMPuUAnytaSs2ajyFz1dUnqgSBYFDQlFdUPmBrIxhNbWkKiNwTydXBXV9nr4y8pm7Eb5fng0BZIFpNzmCLykbYCmPIz_ViVBYbC_j-1Qq6aVOQckY6iwK57oFiWo2Bo4_kUW8XPFFOL__cE1ugKDAQB69KslFTRKYVkrDzLpYnruDPxpqcsSZ9kzod1yjt586HPLm8aCKhSz5LFQ1I-dwacSA8c3qVsSlhTBUSCk8prnu7qHS5JCHdbVQHPxkB2VRhMXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gBoC4qO03lwN-ZQ7eQbFbimIdBUhe5fB7qogfmvdVgHIKfK3cqKoDAXNmFtD3jkUHw0oma7DSwI1kIZVcHkxrwJLVGzs_nhUjmUyOIny2iaVjLt5isJWayHswnfR58JTMlY4E3DMnz68-KY06XQabH1z0m1cPMWaORi-UpbCLlHFFjzmyQb0ylwrGPrPdS69vgHyqm9GJzPK6e6VQwbqomMg5NFbD-9pnk8M-p5zRb5oWFwU4HbtrsBpXvS6qPQbzgvtNYN-fVNS5ypCJJzY85dNTKK_rM67EEwwr2SjYC1zpGyxeue6sGQO27XOIt30d1JDgdEBBfpOFRyxNF95Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6deKlP5xYjwdAoUOsYZWyb2kHDXxua9_mr4Ds00_R3I7P-MnO48rYPvWKHBQS2XeHUiEt_XhdDbGmlL1o9UVEd-wc2zPXhaSdFxUyw2j1H4kNVJ_IhausjpfkPpfGG_leRxuIzdbcKOtvRlBAto4CigvJphR9QpkBjMNXIW5JoigvLLTn_3JvvyVlk0qDqr-hW47z1ndexKD_KvMb-Qp6nk6RYoD8p6_m4Koq6mxh-CFl7bYEcQAVmkJjdzzmjrkTA9Tusxm_Xh2xNXAbmNsuBZN5AAb7m-T_srYURCjqm3RgOjPWfCV_ZclsioqPyDjaKLccOJhdHXWV6CmBW9Qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
باشگاه فوق العاده محبوب آگزبورگ از کیت خودش رونمایی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/102479" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102478">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LG5ad1so2sO4mttE7gPjjNZVl9OVyqAwJEasYSKI2ibVSICOsHCbjh2ylvjdIWWmxYfG5M9zz_q0Ocnz03LD7y5kN4FZXGQRAzXSKGogfbPvtdQr18FML1aunBfra9juTQsVIjK_J50Uw1DO9NPb0-IX9antrnOb5S8r1MFyyZFcjF4ru_NU1w7VJFp0x1xkXJ3jKhANhZe9ZEKqfs97EaLGi_0qSZrlYX5VuT7L4clAy8lySvZGnEP_SxXJUTkOvho5YttB6fKREM3v9CdNghBZ-JuEJs2C1kqz-ybFfgNmWt5bYnppctt_cUN9BS3r7AMReZm0LJLaSh1uUQvv4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
هندآف آرسنال رسانه نزدیک به آرسنال:
وینیسیوس شخصا با آرسنال به توافق رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/Futball180TV/102478" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102477">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی،…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/Futball180TV/102477" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102476">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=sUkYV155FsCCPvHrB6OmDVUTfJAgXl6yboSjkLSiHRUeigKCOCW_jWyDtHJ3BFAwUCHGl723hWDpHKCaSCalvaqijuRRnWTOShZqm2RE_CLR5Go4gmTjUf9czJm8sgb5KR4ZF-16WaUss9AtTO1sFB--aa8E82qfw3_u2ZKTFuFNCfG1DxXHvO86q3j2RSD8Vso5xPw5Fmrc7NabqN8rHixDf_roytPXTMkGfXdRTwZ3fde2edHbhgegT8u4VJjnj3WzBVptYmGCteax7kSlMPyNQtYdirHUdZ77Rshic1lu-3_-slyh0vH6rkzZUL2PUFYz-TEFQIeJtd1ExyiYyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=sUkYV155FsCCPvHrB6OmDVUTfJAgXl6yboSjkLSiHRUeigKCOCW_jWyDtHJ3BFAwUCHGl723hWDpHKCaSCalvaqijuRRnWTOShZqm2RE_CLR5Go4gmTjUf9czJm8sgb5KR4ZF-16WaUss9AtTO1sFB--aa8E82qfw3_u2ZKTFuFNCfG1DxXHvO86q3j2RSD8Vso5xPw5Fmrc7NabqN8rHixDf_roytPXTMkGfXdRTwZ3fde2edHbhgegT8u4VJjnj3WzBVptYmGCteax7kSlMPyNQtYdirHUdZ77Rshic1lu-3_-slyh0vH6rkzZUL2PUFYz-TEFQIeJtd1ExyiYyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی، باشگاهی و دوستانه)
🔹
پیشنهادهای دقیق گل بالا/پایین (Over/Under) و گلزنی هر دو تیم (BTTS)
🔹
بدون ادعای واهی ضریب ۱۰۰! فقط سود مستمر با مدیریت سرمایه.
آمار ما در ماه گذشته خودش گویای همه‌چیزه. فرم‌های امروز رو از دست نده
👇
🔗
[
ورود به کانال و دریافت فرم‌های رایگان امروز]</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/Futball180TV/102476" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102475">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GM9WkHhC9DUmoawt2xycjRetnyrf-4yS2j-9667SYNNdO6q6bwsoGRpPyDaCM4Ap321fFOyGLIuK45gPo6lQHZcUw6dlpxkbUQTl-8Wm4mXkA3f0XEaWpYhOULujqjV--WXrS_-rPD2sB2HQyRvhYSedQjRjSbkeyoD1JXeY4ZKBTWD5c1QdqZZaus1UNCGpdzlwtNlMDEpZ_2XM-TRpL4nmbmY3BJ0E7f-72XZiRlBPYYRJLzwe87mb5nTpeRZ9sGZRpg3nit2Eh6tJznQwRNI8qHfFJyw9aWMsJBy7CK3s2B5vknk5-XkiWKW_SQzDOm3IRhiD5JRxjTtdJcpHRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بارسلونا در یک بازی دوستانه مقابل بیرمینگام شکست خورد. بیرمینگام با نتیجه 3 بر 2 در ضربات پنالتی به پیروزی رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/Futball180TV/102475" target="_blank">📅 00:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102474">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_BkpDi_CrVjcD417jVQEzkBg7vqTa95cJWUbU--fuo4YQ_HMSn2M6q_Imp82UhpxfT4MoApdIY6HAzU2tSGHeAy_GsNi4l2bNNwcu35vOjFBWEDf1RaXR5hoX6_qHTjpvIjMvNbmLzq-E-pERXzzsKkCZi16vFGL8aJCHScW0dtihg4-7qQrly7OCHbBqlvGakBwxzQGV0fLim-LHtjFZIiXPzeTOwavIMiWcxihGcwWNuYqDDEQKskJDJDzEpAfjM2G9aWpA_dr58wS_b-ZdWdVZXCvi4jo-cDwqDOEer4F9Lees3a8P4rQ-3Lqt7gRlxp5dSLCkaoTbKS2e0jTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دوست دختر یامال
😦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/Futball180TV/102474" target="_blank">📅 00:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102473">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZ8I_VRhIrXhqgmSMqD6cpn2C-fbM8FaBW6gxw3L5DPyuoZlxIUXht_MgJlYd8s2I5Rbu6Xx2rPQXYwPYf6M4_uOz-HReEZRaQGWEtRt08tO0Dare-mykYemrjc4--K6vKm3I5ude4UkXQxEoxnUpxaQNdEI7mCgayf5LpEtkSjXyXMPFIQQB-SxUXkVNpHHEM6tw86wfeaFMoUEZF1PvGwi8WBDDE4hwaFlRVhPj40PgLm2C8qIvYKfuuar9rQ2RhmnNX_syHkgvhay68AzJZ24LpRQhuo7G1NcYYfdp86gCX0y9DNy15zFG6rJvk9xNZJijIkRfzC7KHlruvyZdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🤩
خداحافظی امید عالیشاه با هواداران پس از 13 سال حضور در پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/102473" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102472">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYMY_npcHC27ZR1mbnaIoDetbNK691Dni1nICiwb4QbGg-moErDachdvtdJV90vFMr3j_XjKRDOuYaZZJg9Strk8XqyY9xO4PWAlQ24BOXox8fAk7KATvL6NeSRmcLt1_iPTK6GNF_dxB8pFOEylCo2-1FEOtREdx4wTUWk5UYpf-dIksvc4PdcWo3fToLGIw9mxqV6RnnhDkUCMgBFbWzIClBMIsM7nO3MLpnu0ZNWkBJWWHiHSh4OpFFW7TWAKNjj_361zT5yVPleZcSueRVInDyz-TQq4ax67rrYdF8qYOFOJyQHFQ8SgONgRIT7fPKPKX-tsi1tpnLswLHiZpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
مسی و کاسمیرو تو تمرینات اینترمیامی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/102472" target="_blank">📅 23:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102471">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c665525c.mp4?token=BQsn3z5YJg5qOtHNPHWkpJgr40AlilwKMHnEXX6owxl0Wa4DjP1eKfaJ5VJaTMWDna-EYJ-iujms8cihJcKqZGcsf_XFBTwYBTWy4epDJI_Dbg_Zy6XsJf05IZSZUPZfPy3akvq8e8JXQQdFLzDk4VpjGqwHhaco75IoOHerwTgscxdHHV8siSCmpsZqwv9EihhSgfqGvWYJqIzHK_eJNjedOb_iQ1T2iwBVHIPDTkmjvFQJTwrN1tJ1Mf49z_smwP4vDOyLx5EptTEwDUEzwhoVGMN9TqHeFJY4NCK3V6WfPkUC5rooVoqjuFaqpTmRhNGzRktAVXIL7ohEOG0oQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c665525c.mp4?token=BQsn3z5YJg5qOtHNPHWkpJgr40AlilwKMHnEXX6owxl0Wa4DjP1eKfaJ5VJaTMWDna-EYJ-iujms8cihJcKqZGcsf_XFBTwYBTWy4epDJI_Dbg_Zy6XsJf05IZSZUPZfPy3akvq8e8JXQQdFLzDk4VpjGqwHhaco75IoOHerwTgscxdHHV8siSCmpsZqwv9EihhSgfqGvWYJqIzHK_eJNjedOb_iQ1T2iwBVHIPDTkmjvFQJTwrN1tJ1Mf49z_smwP4vDOyLx5EptTEwDUEzwhoVGMN9TqHeFJY4NCK3V6WfPkUC5rooVoqjuFaqpTmRhNGzRktAVXIL7ohEOG0oQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین ووزینیا که تو جام‌جهانی تک تک تیما رو سرویس کرده بود، جلوی علی علیپور اینجوری فحش خورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/102471" target="_blank">📅 22:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102470">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtvBjDgbRoJAy7FsvLzBqKBIRZABnggEdppkgmKFJFnbfNgu1hh0rVj2Bw84y2NGhoH4Lr_lqSi5_h-TaSvCD1eUHFzxZYAJOh3fvYqCkC1-cr9sOXrVukNAycoTNYoex8g38WXHt-F4uacldeB11Y9maNYaIhD53l4hzz1DZHN-PyvgYjEw4OuF41ckPx8-RFKvrG2SgVvwFnbQKfd2lnpJIr5A72hlcLXIgjQZxN_-XeZNY6K9IW254YFQ6K10Z1uvCaNXGYyhKfqldFIsd8fQhJ4CibwV7So11mdd76C6I0_hn_bj5XLnOOEeEDhkoNekVCwpE0cSRW7XjvnSIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ار‌ام‌سی:
مندی تو وضعیت مالی بدی قرار گرفته در حدی‌ که مدال و کاپ جام جهانی خودشو 54 هزار یورو فروخته.
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/102470" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102469">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261dc7eb19.mp4?token=V-1n8XsL_AqY7QcFAa9pgA7wEXxSwsFYA23PrsdvLPucBVKDc7GxJlJaxKqkHoxL73-Dd_K38UZ0p73JFm6m2DL9XNOwOV9jVMaz4qmDe91zd9wDUhtV9maFrYGoCFkrIur-qWSyW7mCvLiCWVqZ6asFnLZ8EOTVu1i_JcuVjFnm4u5lsgD9_g2lAJuCbwo7smS2Por3LhRRwEG-82wk9bHJy_OE_eF_jE2wEh9hCNaYJEvpC7DFdY5ovD9zhpm3mRDaWm24tciRooD8_Nk3dy5kxgFLRQ59JPxJcfWbDME-g2SAGGryZRHaJt_lUqnOGxSRdNFwHUH3uXGXkhOv7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261dc7eb19.mp4?token=V-1n8XsL_AqY7QcFAa9pgA7wEXxSwsFYA23PrsdvLPucBVKDc7GxJlJaxKqkHoxL73-Dd_K38UZ0p73JFm6m2DL9XNOwOV9jVMaz4qmDe91zd9wDUhtV9maFrYGoCFkrIur-qWSyW7mCvLiCWVqZ6asFnLZ8EOTVu1i_JcuVjFnm4u5lsgD9_g2lAJuCbwo7smS2Por3LhRRwEG-82wk9bHJy_OE_eF_jE2wEh9hCNaYJEvpC7DFdY5ovD9zhpm3mRDaWm24tciRooD8_Nk3dy5kxgFLRQ59JPxJcfWbDME-g2SAGGryZRHaJt_lUqnOGxSRdNFwHUH3uXGXkhOv7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
تام هالند یک‌بار به ارلینگ هالند دایرکت داد و از او خواست به تاتنهام بیاید، اما ارلینگ اصلاً متوجه نشد فرستنده، بازیگر اسپایدرمن است. بعد از اینکه ماجرا جنجالی شد، هالند برای تام پیام فرستاد و توضیح داد هیچ قصدی برای بی‌احترامی نداشته و فقط او را نشناخته بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102469" target="_blank">📅 22:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102468">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjJAhr05LZaBk5oKwHpp0bYN_dHbNaQyz8XmxlLVGX328HrqaglR5RPL-T0Ii1Fe5zDL2ajJmK0qiNbddeqGS1bAbb-2n0pFHhEAXp_8x0G9HnhSV_biaUkHZ_c0xk8NnXngSP8aIw715IEj13cboQhX6uc8F18n_pq6M8XfenGsVVJPOOuSj-Y8Z5prfIfIrGN9-KexbzefKLZ9QEBPq8cTmFr1xYJlSPLW_ecsjakNTe3mZ2smpiSS48QpojggfQ7Ep1niN3ERQuWm3mNXiJHJPFkXNpH7fqUlBe6hdMIhO6bYRdJLaHQGV5DrDOlVaLzPSfmazYDCsGaEkEpLpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
بمب لاپورتا ترکید:
جسی بیسیوو، وینگر بلژیکی کلوب بروژ،
به بارسلونا پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102468" target="_blank">📅 21:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102467">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pasn1V423e2yE5Au_5YJF0N7Jlg2ktOj6hO2mIpcrJ764GEF4ZryXwUTkd7G8KDt4trGYzeRw08aINH8XloQOOy9XeNxkdygJYYy8MalFH5_SVfey_CYeC2xwk5lD2ybXEEElktfEh1WpOFR4a6m11iSLlDe_IRFbT_CNoZKvP5noaOW8lwcdfwxq0EEnn_N9EplGy6ide4DXpggv21hEyNBGzKyTRV-QxwZU7kIilly3Rewke-P7Kj9ooRihIFcJxgETLt-BXKQDs-am0l_8zRv7k9OopfTkyRHUPsm9ZRT9YrUNMgyfTgprMmXFF1sTDi-a6SPX9ksW6QpP8f50g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب امشب بارسلونا در بازی دوستانه مقابل بیرمنگام‌سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/102467" target="_blank">📅 21:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102466">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f4d6d3d7.mp4?token=NCXpSSyqmadvMi0cW2Q7WIuB3Y3iTUuks60nObNGlneMgUo96J575c8KoT91WBtmsIwk5c3WF6ex8JVXcCyOL40bvRVm0281L4wppOXSdBLAF1UXwsd-04kBvXMTHZds_-lxfDpRvHuGYxCRned5LtLRlHn1tITisQkMs8-8OucIjB-AmSTbuSd9frxSRZbgT2BeEfIGBCW5CVIgp6dkKGqXAfLRYuhyKrVC5-a6wYglNIL2NnlV2EcYC7zB7FsU7Vy3qHkdzkdOtWGfxJNd1kUu_E5bUbTf8OQqMiC7C0HdAJWbToz76GqepeP1Zpq6rCmYnaIzgSZ3L0yvoJ48ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f4d6d3d7.mp4?token=NCXpSSyqmadvMi0cW2Q7WIuB3Y3iTUuks60nObNGlneMgUo96J575c8KoT91WBtmsIwk5c3WF6ex8JVXcCyOL40bvRVm0281L4wppOXSdBLAF1UXwsd-04kBvXMTHZds_-lxfDpRvHuGYxCRned5LtLRlHn1tITisQkMs8-8OucIjB-AmSTbuSd9frxSRZbgT2BeEfIGBCW5CVIgp6dkKGqXAfLRYuhyKrVC5-a6wYglNIL2NnlV2EcYC7zB7FsU7Vy3qHkdzkdOtWGfxJNd1kUu_E5bUbTf8OQqMiC7C0HdAJWbToz76GqepeP1Zpq6rCmYnaIzgSZ3L0yvoJ48ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔹
وقتی منچسترسیتی حریف پیکان نشد! سال ۲۰۰۲ پیکان با سرمربی‌گری ذوالفقارنسب برای آمادگی در رقابت‌های لیگ برتر، یک اردو در انگلیس برگزار کرد که در بازی دوستانه مقابل منچسترسیتی موفق به توقف این تیم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102466" target="_blank">📅 21:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102465">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcb0e2d66.mp4?token=AmdQv9Mm8g_l3j3TmGsalN-aoG9lDdSH0bmErIyqjQ9_nhf9Uy1-lGqTlNfQg-Xlq50EfQz-bOFuCYdnkvNZhmb3Yw6Lo7ldEULN2iRnJcdiK8YOb-1oWTOlyCk0gv89bBAv9Gqz8oRnPa1H3mHUAqc7soK7p-GwiF9JmS1TsEGACCAgB5SKCirfe4G22O5x69gPCvaz8Of1NvrPeGjwrCM_C-N_7QSD93nsOiX1gbO7hh6hFp_Ye8MaGKZ6F8dwOnsBRIHBTeztRD73i-UtaoLpJNxBqDimYMInt2R0zzKZsgsz_1dIzQYo1FOVhF9c4zEzwWL-4dmu-O6Cu6PCQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcb0e2d66.mp4?token=AmdQv9Mm8g_l3j3TmGsalN-aoG9lDdSH0bmErIyqjQ9_nhf9Uy1-lGqTlNfQg-Xlq50EfQz-bOFuCYdnkvNZhmb3Yw6Lo7ldEULN2iRnJcdiK8YOb-1oWTOlyCk0gv89bBAv9Gqz8oRnPa1H3mHUAqc7soK7p-GwiF9JmS1TsEGACCAgB5SKCirfe4G22O5x69gPCvaz8Of1NvrPeGjwrCM_C-N_7QSD93nsOiX1gbO7hh6hFp_Ye8MaGKZ6F8dwOnsBRIHBTeztRD73i-UtaoLpJNxBqDimYMInt2R0zzKZsgsz_1dIzQYo1FOVhF9c4zEzwWL-4dmu-O6Cu6PCQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚪️
رونالدو چرا رئال رو ترک کرد؟ شرح ماجرای جدایی اسطوره فوتبال از زبان خودش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102465" target="_blank">📅 21:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102464">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ed94c011.mp4?token=VaPLf3l2kT9NKdhjeu12yI3O5htzcTxua8H-qOCinTNanPl9F8_sDUp6uAo7KuC3-3VMwgUCg7Nr-tpeuIxu8h9IoBTFMyD7qqhjO64ma4I393jm2LHCgsT_VLRu0o6Jdv5bug1VXKCl7EXtfEqTimPRQ08uPXCS3z06c-YP7ZSULeG71eHi6ltJFHDV3IKTjbe_yIHJsAIlB3UUmRjaukJHrATYJpBsi75pdpb0G91qxAQ7gepUhQ9HItroSB5OIWKp9PaVynToL6VfLOxqSSYHDy6aoe83hwBrNZovIXzR0ftLNbKd2Rhc5q-2Ya9nH6uEtqOQgCw-1648Otb-qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ed94c011.mp4?token=VaPLf3l2kT9NKdhjeu12yI3O5htzcTxua8H-qOCinTNanPl9F8_sDUp6uAo7KuC3-3VMwgUCg7Nr-tpeuIxu8h9IoBTFMyD7qqhjO64ma4I393jm2LHCgsT_VLRu0o6Jdv5bug1VXKCl7EXtfEqTimPRQ08uPXCS3z06c-YP7ZSULeG71eHi6ltJFHDV3IKTjbe_yIHJsAIlB3UUmRjaukJHrATYJpBsi75pdpb0G91qxAQ7gepUhQ9HItroSB5OIWKp9PaVynToL6VfLOxqSSYHDy6aoe83hwBrNZovIXzR0ftLNbKd2Rhc5q-2Ya9nH6uEtqOQgCw-1648Otb-qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یک تازه داماد پرسپولیس را حذف کرد!
از ماه عسل برگشته بود و چهار ماه حتی توپ به پاهاش نخورده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102464" target="_blank">📅 21:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102462">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102462" target="_blank">📅 20:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102461">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=FJjh-TZXDgnf3E5VYZbRvSXsl63DboUaVzRP6v6Wh75ES1Ff_8N88r7Aw9R8fZwwMUtOmwvwe6onb16eDZdNs70d_6mQQPzq2JXnTE5CX9DSWL1pgMFdTFN4lgZBSySOyetjXvCooZfviB1fSky02mUVV5rUzSTTQyVl02p3EzH_XrIxABhgCzI2uCQNLvf7pVKZdjwmZcpe6LixHIHuWkVIPPHG_wDDnjG3mew_-TGzxtrKEOkrYiYtyvMIYWkBP_vWv5W66GP2FTMVNTMqr_7V4cn9dlcjrNvU5g2sa6mb8Jsm8TsPAStlIroctrcTh8GpFU_HMeTC0bZLrma5GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=FJjh-TZXDgnf3E5VYZbRvSXsl63DboUaVzRP6v6Wh75ES1Ff_8N88r7Aw9R8fZwwMUtOmwvwe6onb16eDZdNs70d_6mQQPzq2JXnTE5CX9DSWL1pgMFdTFN4lgZBSySOyetjXvCooZfviB1fSky02mUVV5rUzSTTQyVl02p3EzH_XrIxABhgCzI2uCQNLvf7pVKZdjwmZcpe6LixHIHuWkVIPPHG_wDDnjG3mew_-TGzxtrKEOkrYiYtyvMIYWkBP_vWv5W66GP2FTMVNTMqr_7V4cn9dlcjrNvU5g2sa6mb8Jsm8TsPAStlIroctrcTh8GpFU_HMeTC0bZLrma5GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شزنی جنس رسیده بهش و مشغول دلقک‌بازی تو تمرین بارساست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102461" target="_blank">📅 20:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102460">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace3163b65.mp4?token=tgSDTrUn6R3D9BeGCHW1lFzyWUgh-hPKlwxh25tpNDXUho12_a5xhoUFAiFCT3TG4vprB-eNoiJeKsMeC2myToABXPpKS8RjrdiqyCrOgAizW3t7G7OxORK134_4UzCdp_3RE6629A2-jcS6Q3SzY02UEa0Bu3wq-53dAIJJuObhdxOhNZ_E0ffUgmcGIELUn3PRx4E2Gkp3U3l1O9JFF7yYR3TdpxhFtclbHd9K2KoyHxpEr1SfCZz3eqqH2d7z7Q5CbdWetz9-JA3Ho2coxWZb_9mdmK0pCAITgIeWB2PQ8gxRn-Xg69xqu8VFlXjn6FBdhtITDwXk_DOdYIRuYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace3163b65.mp4?token=tgSDTrUn6R3D9BeGCHW1lFzyWUgh-hPKlwxh25tpNDXUho12_a5xhoUFAiFCT3TG4vprB-eNoiJeKsMeC2myToABXPpKS8RjrdiqyCrOgAizW3t7G7OxORK134_4UzCdp_3RE6629A2-jcS6Q3SzY02UEa0Bu3wq-53dAIJJuObhdxOhNZ_E0ffUgmcGIELUn3PRx4E2Gkp3U3l1O9JFF7yYR3TdpxhFtclbHd9K2KoyHxpEr1SfCZz3eqqH2d7z7Q5CbdWetz9-JA3Ho2coxWZb_9mdmK0pCAITgIeWB2PQ8gxRn-Xg69xqu8VFlXjn6FBdhtITDwXk_DOdYIRuYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کول پالمر:
برای بازی مکزیک - انگلیس بیدار موندم، ولی بین دو نیمه خوابم برد!
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102460" target="_blank">📅 20:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102459">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhtgBuSIVtECjWBENH7A2P_QF9ZTv2zzfC_ePoOR3zayZBlpak5o-kPqYxdYgMVp7_veupnruqgUugWyGBoWTXDJzgzIzKYJS6NqxdaSnghR8MTM7hN1vGRnZBgcYHKf5_d4Y8U3eXQWfo4OhilodFvs11p-vsyE3KphQA9zEYkA10hc-0D5kDeZfGFVHwiuFnunDrU-BoYcxaSmVDYir_kOmTESPxbLX2c3kBXqTBbFjruauuEGdtbOUV-F4F_QslPQKI4cSyDzOcnKg7C42iYwSw6LTmxL38RpagxcasSDKH3dWInrY6AmbLVB8nf0vVIv6YviSTVevCW4EU6jig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102459" target="_blank">📅 20:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102458">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opCd1VFSW15xEgcBW6YJbJknArSUXy7EfzriyoZgcGHCxAAQyDLN5fmTOWq7XP_eYopItp4D2hBMp6f3CisT8MZXN8p95nY6JwYDdUYovURFgiP1zeuif_pj1lMr4mGlTgEqMhzLZlmZx-Zc8smhmwRcS5rpNgQT9rQJxRh180RD3mAVXATLwtC9wid0TQmRdkinHPIjuD17_o-_8uSCj_nKM_wSYljcYPoG9Tz2FTC-HRs0_T9oBksJuXC6Lw0YQp2t4i3NkNesZ1EswVBo9x9ztUdWZCdTnmp4Xur-0ZagijAVT7bAd2Tx3P-ajz5X83zsez9-fx8pIOw2C7ErOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
فقط سه بازیکن توی ۱۰ فصل اخیر تونستن در ۵ لیگ معتبر اروپا هم بیش از ۲۰۰ گل بزنن و هم حداقل ۵۰ پاس گل ثبت کنن:
😀
محمد صلاح
🇫🇷
کیلیان امباپه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102458" target="_blank">📅 20:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102457">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4HqdcUXfQm1v0M5NiPy9CDp9c4bkVvrYhaKqcrPOcD38jMrt1me9sOF7dBVQp-gVmGhorfVCZeqMkNzgxZ1Nl2-GnecM9lU-EEqe1v1qimldDYj5WUCLpYyxJ3rihSPIcF7lZoU9SLlGw5OYVWBX5i_Jy-7BXXN4Kqnfw7qN39qVGKoOn_SVbtkkDni0z921Enw9ooGrm1Js1Pa6cDyMFcEpAsq4GxhsHt49IsOXSizHgNTWN1Cm8Xh0n-mOzlYirBq6a6RAomLVQn91FBa4jH66VW4BSLqJ8LYt-vneeCrtGbukI0pYfzqZ1XEQHvFYK_EwfLO-QbZTcKej_OG4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102457" target="_blank">📅 20:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102456">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/102456" target="_blank">📅 20:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102455">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1OiiTiAzpQE9z4tIIarAGBsZLubtLzpzz_gtv6oPhGkCN4pEZH3PD6MYw4nVFqPiQ3p5VXqWuMJdcYxcqdVeX0hD-mP9FLqrJSHep6qfCIRoIWKtEZfTkusblUSmSiAdQF9om7Pnq61dFKGbkjjL3aQdLPqzlf6P6eAzqIoWqAWlilqGa5c_cETZh0z5EwT4YDPUjSwB_mcrt6Db0WTWncBXqOsKdWy84KqeTxYlwy1EhXzaGBj9ROE4xqgw9S1Fkc4gVuAfPQTrJc_byNajYQoEG633bfSpI58-6crbxvpCIfTEl5liTYoZ7ju5o41J2bROz5kQgTfPP-HNoIFHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102455" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102454">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fq-0VXPVp2KNEzL2HBUrLP5QK-RWmC5B5AWV67s6rePpeAuMDO3pDexGxT3kXxFJ2WvCMEe9zsZt5UiIh1POgp8I2Pl_fegZW0AecYlS26chqSGCM5x7Qy6YvyOZnc3ZMTX_TeOziMfnQu4rQSv3CJ7KEajbG9Hb6hTfSMOZYtz46tYlPajU4HwEIiiOwBRkHLRtaljtxdFbMqFV7m8w82gDr8qyrPCxMRoVEhsu1T4rCZeYwx75CwdwPvwOVJq4DdWeoIq_nAnEmT5_bXNcwKI_zukk_980cbJ-N9Ww-i5DBqh6ZsfysMB4S9mfj3dQCfONk3jQPti54Z16PrIFUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇯🇲
وینی و عشقش تو تعطیلات در جامائیکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102454" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102453">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
📹
🔵
🟠
پخش زنده بازی دوستانه استقلال و فولاد ساعت 17:30 از لینک زیر
👇
https://t.me/+E5pLb4kNVJZiOGI8</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/102453" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102452">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کاسمیرو به همراه خونواده که دیروز به این شکل بعد از معارفه عکس دست‌جمعی گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102452" target="_blank">📅 19:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102451">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNG5RdvSPi8u1ASpS3YfgBHZFBwKhILKWZ2pD9_iuzFQhTwVY2lsIiXUX2F5HOtr5fUQpz72k2C4LoyYQELL_AT8-3DjxybKxUvMncYkGGmWWj4B0emGgBQ5Lv9Nt65s8xNJKFB-W7HYITVG4hEPD_y2UjFJK74N6wYmwoE0sadFvosPu5IbfNxbja-JPjtEiGFHLlJuoxYr-eYCeekUDwx2arLPR1vW2noP1MSfG0g0yfp69c7SIPlZxXJQz-j-_F2ag3INGxMy0rhFA_ZKnrxypUK7XJpXbA5zCxIuy5tr2xHJt-o_s53XqgiU7Q_oezwGhUlS_xyr66-rsF_Ejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
رسانه ESPN برزیل: رئال‌مادرید هیچگونه افزایش مبلغی در پیشنهاد تمدید قرارداد به وینیسیوس ارائه نمی‌دهد و پیشنهاد فعلی همان آخرین پیشنهاد تمدید قرارداد است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102451" target="_blank">📅 19:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102450">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEAyZD0fMXqr9TqhztnbA_tpX9MNbRDl4B7a2Rd4cIMazhFVCZZeCM3nqzBykjg1KjfjZXAOVycjuavd0FVe0O1y6LCkYFf-hXsQGUSxiCk4gk8d_1e1-CCwVK9OQAv7ayy_bbGcY-9k08CAeU9RcoLm2Gjh_6e3Y3FFcO243meLaYLkpwMsqcSLEZvqcxpsQZ9zMnHslpf5_zPn2B7yO9KVvqoZNRZr-HEUSS6D7b3jsgjVx5BrsAN4tmo8xQl2cvmT1XHmkcmBQhPEGUDzecao6eBRvIcoqOgvADfATzvA3ixHuXjVOnsE0x9R9lDAq2YJPkMWD371CBANiju8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
اینفانتینو: جام‌جهانی ۲۰۳۰ بهترین دوره از تاریخ این مسابقات خواهد بود چون در کشور زیبای مراکش برگزار می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/102450" target="_blank">📅 19:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102449">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBRzI5io77aSJ4atP-ROH80g7vDE7PCdw4DlAsAhThWrDG0kGViyC3GrMl9kEP14G0IWoLg7RSds1spO33gz8ulsihmXyOAaqIbEa1K9yUmSQrlu5G0BeBh5mKmoVt9jQDfbuBWuvzaCXgbXMw-etB0W_nCpUjpDsqzcFXsSkfkTij4mTF6f766FXRoaAfEwT3TqTaOhI7NANr2YOjmjKIFDghXxtTzFGizBXNKR0bW8ZnoCInB8knIV23RzTK868XJaereWYUs9u_PbTp_uDC_4cyHQDHeqi8y5N06EPe_HEsviiNaTL8pvWoRXcbuLlGK6KFba6-nqeg9F2H1woA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس تعدادی از بازیکنای فوتبال
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/102449" target="_blank">📅 19:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102448">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0Qe0UW7ry8ViU6hKg0Y_BUKAkXxPU0dNEJ9l96vyu0ouQe7I8ErWwNh2IVZoXNWqiNRxWThAluM9KCh3FO4YHJszGhOXjFvI116wKFajjYer5rtbGkrXiBDC0Q_SyBI8fNmq6Rq7_xw_rqPrHm64FOej-LD8g-nQnrNpoAT9N_JoB4sYul__B9mcQYTIrOUvykiXt3k9Kf9WXBovdQuDpu6MGkOL5OBJ5ylSbyn0S2oSr3Od4N0ppgk_WhwY0ejVC-ViFlFI77e-q8QhbrZMCN25QinOOmfaPHxCB-rCEhlgL3liYlcsSCucJhRT_SINNorEBWKx0DJwDsL0Hms7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
اسپی:
انتقالم به مادرید خیلی یهویی اتفاق افتاد و همه چیز خیلی سریع انجام شد، رویایی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/102448" target="_blank">📅 19:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102444">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m8qIWCyleJRdKB6tVvTkOa41IbCNeJ7pby18dqoEKVs-esrrPGOrCIuPvzFNnIesC9CZDO6DbM70DzI5rSYmQ5DEA2FhJdakSHDMP2hjwVkYN5JuMdAiGj7_1UJC-KUJ5N9VImplYPjUVga64RzqtMzAisSaqX6kpKX9kXVBJETDfq4wqy_B3U8MQvCB8PaE9z2E9M46JmACF0grULJH-UQ3-Q35tiP3-Ey1OpXo075ecScTkr1SSV6LDit4S55y6bjFy0NMWmdgzZvKDiLfO5lWS1Sf8xulxYFEOgFmpK2lRvuaLsbBxnSWMuWKFgdAilxAsnfmh8MlLx8WZTYIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hZiYK-7JxQ5JAt24REBfX6p-z2mFRmLq0Op64pPYS75nItESM5qFCNycAyqysPghDVVKbcV6aZV_6ar5TyYERRuahuM7GTNl0jZ2OLIknZzklQrMk5Vg0FkUJG1PFiWAB0njw2NG1Zs1s5AZMQJnPCFXkGSAWNvOqY60kDQ1jHr843p-4tkLxpJ1ElEJOXLMMoAfFcDERNKZOL6dFyV2v1FaU5mPKdK0FdWPm0iUMnpbVmwErXbCarKDGRaABUdc1vPu6f4r83_bqnVYrbZRU9zV5Dt1Gv8zwH34slFJ3g7V7phq3h8a9nNvY78-m2ZYP44w36lnA7PFNa600Aq4rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTcvSAD8FEF9bd36t-v2h-jYCEjvqARmEH6fCILiuiyiwepIbrmtB5IxzQPlFTa3ogsaCB4dWOqnQpPepITVZJ8tLFEVtFFW3HBRIUq6W3hctzIWqBtZIJD1xLTnvEFlPegMWHThjZJ9UqS8vgFhGUeoI06f-2GHwqU6KHgVgXaY3JeCc0Xt_gxOHRO-x27oh0B5qEyPKQQ0aawWHRNbo57vtxFkw5ll10J2DrXo9L5SXPMPzJqoAePyrkTbNK57NRcMPQ5gucq_UndZ8M24NpPrTg3az8Bpqiiucfagr7jYCui-hEfakvK3Nz1FtN2ZQFiJX7hT1exN_vSwxW5EVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vFSJi6921B9EfUAfWDcGskbw15JcMCFEVjFKEdMpCd6MYh0RCjUsjB7NmNMe7EsndHg-6SgSqzZqMkfCQv_0ywAcVtTuBz4GOUEoUptz1wc6GRe1514zdvTHkOh4Kk8Q_Kj4mfaJnVx7GMsWux5GrOrYljJUkja1UAoO_Jxznys02S5I8H08LW9lS8G4_0EQfCOZDgPM1EVJQNjMA9r5aeTU_0c6_OvzSWx48JO82VFiU4LMUYYpRfa1gThmmsDNyAfwuRrO4XePkptt6SVR09yPGeDOn_pxXITaZdfK-jRydunkBVllOYG02gbR7jwoy3ImewDD6AJ_HRnn5DRIrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
عشق و حال لامین یامال با دوست دخترش اینس گارسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/102444" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102443">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbFwt3Cx86RuRJocw5Fk-gmShKIordBCWxMlID6MoD2qbMOtb25iLJm2A7Wl9zFsK3ZPHTCJRwSyh1it4qpzzR2Z3RslW7rNKmYp4gNTR4i3kOxBzKHSxz36Q7IGLY5tIVGOF3OsCCQu44q29KiXGjR_Y1P_Z4Z7S2kUOMDy-NX1c26IqVaA_uDmnAe2bz7WQQtUfdjqVoToYaRDf5Z9D_NNM9qiMnTFkQQHg_bCRLJRRKohXaPruKoonwRZED0Wuw8E1Uu1Q6V_fuME_XI-sYDmefxjXD7Yj5Dlb6skMjEfS52JAQ6h5UOvY-0exyygncqYFtpGj4qqmCfw_HDSfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی دوستانه مقابل فولاد</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/102443" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102442">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCtdyR1eJUsR55mnjVKZ6tu1yuZadyRUkYSr9Pl22TAgDoxR0rtLBMsWneM4_8LjXWV4k928JSBhznZcNfCw0tuPWZTvWGbeJ62_p3lkyRGIukGRiwiFKqn_c02HzJorIiT0XsSaXvUsbgfNvWOlSUfZqErqbX4ETOa9F5IrL0fLT5yD7J_PO_WzTLWtFCVovD13qKfKlU9QxrK0Friaic9JTh1A7CJVi-TgKALP2kJl6Tr8_6RU5qfNHz3pTCwmaSZ229PbqaspvkcThgPaULG4gfNeT0Act1KDv4I5U5v8xYjo21L-OIlxO3J-ZR2Eii2BSO0a-myCD-HXfpEg6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فوووووری محرومیت دوپینگ میخائیلو مودریک لغو شد و او به زودی به اردوی چلسی در هنگ کنگ ملحق میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102442" target="_blank">📅 18:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102440">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CXy46wjlBCZW5XWbfkfIgxKzYS_A9ZBhdQNQVtEtqc_u5X0YyOVDhtDrVFbMEP93hcs6iJ3QVdOracJDaijEWWGpsPiL7DaJ3I2OpIlVw7C-wNvK-OJTiyxWEzd9IARVtyf-59OzLa-rHmDTOzSIYM3xDN1tjrfXnnUgREF1cPnITRJHcUG_oCCZlOEaVOVOan8imrZmSpboM3pCbF0f1Y-MAoe5i9KcY1zerC84HJAp9J3J0rSY0YBgY1uIjo62wFBBZzw6huqVmBrEtpfjfkn-ip5rPC-0O2m9ynZEPtHm2iz-GT9TYx71OwB92rlt6ZDTE1JTUUCepCvURDDZfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mqDpH5M5NX0_RAB2X8LHChxv6AnmEeIOdIwdSjHzLyAZcCj7icTvH8ocQZAeR4ZWkq5T_6T7FHzGBPDH3SvhM2ufp1eZzcdRz8lFXivCi3VYHgPE3bzZ1bMS_OwOj6DcWPYvKM9VP5WS5T0uEMKMpSf2fmKWkBP5mP2h1FRjVPK0BUKsIHvnCWxwJS-CzQPeX5m2oWowhbasJJwzZvmXcxmQd9EwcFd4ROfSneSVRbzq3aYJgXdNxeFx-evLiU3EwL1OyAoCpcA3CAb6KRkD-etbiXKrJsCtYINcfRumSFfImc8mLgdJvJ6Usi3bueyFCXDl5BBY7oQ96kxFhZENzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیر شدیم و خودمون خبر نداریم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102440" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102439">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NbVKRlzhM5cL6FPH10PQjjm6-vmj4sPuLLaTmGvUVPooVo7FrFT8aPMnqaWH4rb0aD1VjCT1bfiKsB4W4S-zgN1Wn3-h_tVlVlJ4FCh1U_pPEWKiha87LNRfl_WqQGWaHTJzZTriIN3YeX3jEgzSTBlauJ4aANzQA6BtvD4zo3cLdZlJmMm8ZtaRIWxASGT3EhxC2yPUinmnMf2XqSi30J-F_aqA_ybuh6sohScemmCQT437qCo3P6ZtRZk04rTuLNXSso1ERyQEUnSS2YoC5YIoTW-SO_kJN2SP6hFdS--PTbxJ7AQadkeLZ5YZL9ZXND8Aes0Ii-IvKm9rLlOrLmjtR6i_CGu2xqEgcu0FC2nbzxB7NIErnzXKs9J1jySiwebYTtdX-Ij5tw5p-EkoEnAuTpiH3u1MSmPDlGsLdOHynPUQ3dSoXbYbUt1pI9WnWZPJ1C0Lhj8Z5az2tWvBazZghk3riXC1fN70_QVtxmabier65dmeCbdbj4KvdEm15bReQgL3smXB9-7qUCFJ7YYZyMCz8gz_yAFYBoQ_dxRsRZwboj8HTij4ZLd7S6w5UPLOmKmXlwtFaJGy0f46MqTw8JUH0rMuDp55pemy7VqCKdeUY2qm2YhJa5yJfZTuRJS0P3pxZvf4qASkavPQ5VpvXPtI3w0kvA7ulc7DtqI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NbVKRlzhM5cL6FPH10PQjjm6-vmj4sPuLLaTmGvUVPooVo7FrFT8aPMnqaWH4rb0aD1VjCT1bfiKsB4W4S-zgN1Wn3-h_tVlVlJ4FCh1U_pPEWKiha87LNRfl_WqQGWaHTJzZTriIN3YeX3jEgzSTBlauJ4aANzQA6BtvD4zo3cLdZlJmMm8ZtaRIWxASGT3EhxC2yPUinmnMf2XqSi30J-F_aqA_ybuh6sohScemmCQT437qCo3P6ZtRZk04rTuLNXSso1ERyQEUnSS2YoC5YIoTW-SO_kJN2SP6hFdS--PTbxJ7AQadkeLZ5YZL9ZXND8Aes0Ii-IvKm9rLlOrLmjtR6i_CGu2xqEgcu0FC2nbzxB7NIErnzXKs9J1jySiwebYTtdX-Ij5tw5p-EkoEnAuTpiH3u1MSmPDlGsLdOHynPUQ3dSoXbYbUt1pI9WnWZPJ1C0Lhj8Z5az2tWvBazZghk3riXC1fN70_QVtxmabier65dmeCbdbj4KvdEm15bReQgL3smXB9-7qUCFJ7YYZyMCz8gz_yAFYBoQ_dxRsRZwboj8HTij4ZLd7S6w5UPLOmKmXlwtFaJGy0f46MqTw8JUH0rMuDp55pemy7VqCKdeUY2qm2YhJa5yJfZTuRJS0P3pxZvf4qASkavPQ5VpvXPtI3w0kvA7ulc7DtqI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چند تا از شوت های کارلوس رو ببینید، زمانی که فوتبال تا این حد راجب کسب و کار و پول نبود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102439" target="_blank">📅 18:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102438">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=u1S4RuGzqHXpa-yhuVPthbxyZlA_Zc6SEH6w0ZteVJzcwZWLzuBXo6Sg4_sTEy_jKVUX8AHx_1uqF9HliTcouVs8Bq8sukg5M8vczGu7l6U70QcrR2d55XbEpdofTbNO782G1wWf6_6TFhYkjcqVWwCIu93dUM-beKdNvlZh-OYWBYvr3bXPmqnoHNmHm9EGQe8umarmmSbqq0FejJd4yJawqTmGXETJ1PTClxB2BFvuFeJbTbOlSUijwBq6Zle4bG7k09dW7ktaa6Rceeni-TlcurXuYXchIkYbyaU8iiCURy-K_PK4QTsFfTaThhScouNs5Ht6PIW_Uy9gZ-00Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=u1S4RuGzqHXpa-yhuVPthbxyZlA_Zc6SEH6w0ZteVJzcwZWLzuBXo6Sg4_sTEy_jKVUX8AHx_1uqF9HliTcouVs8Bq8sukg5M8vczGu7l6U70QcrR2d55XbEpdofTbNO782G1wWf6_6TFhYkjcqVWwCIu93dUM-beKdNvlZh-OYWBYvr3bXPmqnoHNmHm9EGQe8umarmmSbqq0FejJd4yJawqTmGXETJ1PTClxB2BFvuFeJbTbOlSUijwBq6Zle4bG7k09dW7ktaa6Rceeni-TlcurXuYXchIkYbyaU8iiCURy-K_PK4QTsFfTaThhScouNs5Ht6PIW_Uy9gZ-00Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی‌از وینیسیوس‌جونیور در سن ۱۶ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102438" target="_blank">📅 18:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102436">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HISrN8-TZZvfekThLd0nnki5xAHr7G2Vjn4XN18g1GstHXzjdqXecv4esEHDwjE_J1mqmZRyLv-QsGhmHEKMQFa9r_I5O8_fxe8pq5bHiJ2CwHsBqyTg6qHMfFkwqdPGQ6_PQM6GQ0FY7PRGpQbjLSROl2TIKFj8HQujj_D4_gySBYwmlS4fXWuv9REuBCmTqm03CTrRX_Ecxh9gf8iJDNrzDTE95uNPEadRmwKRSJ63WxoJfMlsYX3R3ekhihY4FGRUIrCVcIZaKVqQNe0Fkju1dFRX3YJMAY8bTGx_GYNN8JyFy29taucnjhw3p_P-fEIFoZpEEup92r5Ijar70A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p81RHJGNuFTl2HMIPVGUyG6_Skd_WkFK3fkqvC3Emt6SkwEXIim0Rz1JeCBHOQTXkjmRGjaT9KUl_EhsiorZ4WZkv23CTixoJ9dO-ZDAbwc6iztcmbWtJEai1_OcGeCOQN0KiORht3HmNCV9Ith3HTZIPJBFlhNm7f369AJDokomimCU2VA8rmUPfKtD-3xGfTTD1scFWXN-HByj4YBhpkt-GWK2Y8eeSY5GX1Zz8ns04XMwnci92hIulJy2jZgsujFLCBaRq0H6jMwbZE4kmKfZlFuAafjPSRnZN5Jvz6LkdTWQ9NiELms8FyZpO5pMVpP9eFWeX70L2KbYTZ7ymQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
فوری، محرومیت سنگین چلسی:
🗣
باشگاه چلسی به مبلغ 10 میلیون پوند جریمه شد.
🗣
همچنین، به طور تعلیقی از ثبت بازیکن جدید در دو دوره نقل و انتقال محروم خواهد شد. به این معنی که اگر بار دیگر خطایی انجام دهد این بار پنجره قطعی بسته خواهد شد.
🗣
در ابتدا 6 امتیاز از مجموع امتیازات چلسی در فصل آینده کسر شد، اما باشگاه درخواست تجدیدنظر داد و این رأی باطل شد.
🗣
این رای بخاطر تخلفات نقل و انتقالاتی در دوره آبراموویچ مالک قبلی باشگاه صادر شده است. مالکان جدید این باشگاه خود این تخلفات را گزارش دادند که باعث تخفیف در حکم نهایی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102436" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102435">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=Evh7HnQtq4sjPHDxwBuPZNEnTLTGxqyJjDVYZl7bfW-fxIEg1fMI8AxejFf8OGdW5dXMk5DkviBDjz9KpgxCOFRX91bDChtc8UOl7svOnTOWI_COPU4DclRDFN_FGqhl4TbCZGVAh6v2fVpryy3UuBNSwj8UH3v3bOUU8Z0wu_wv_oMEBrHVt2tynwsD_lTwFEoS30fYh3oiljdM3aezzAXMLpnWOXJhcWFEggfPjad9aOb0XVH7ZNIN3JAFT18OUujrAPPMnQu2OVUQTYkr6sdy9m90cC50WTPZbXxbk__WKgIXd71CVzZ7Pn-gnJv9sxkIoawYweqw7e0mg-WfY41QU9ReK0lo6tDY8sxDGwGrDqf7rJTLwbwAHB_xO9hQSJILpiWK0_jw45tGOjdBazjDZHKY2F3ouu3UrWuRgvjM8rW98EoxPPOG7OyxsCkWIzC6_GEMR4tyAMOkyLeZ-8GlnLDpY5yuu6gsaOXdu2B5uUuuY-QHjsaNfXNZ7BF4lXyDMauKZWv17czUjKS2RQtoqgkr0E5Zjk1ypVI5oHBxYp4v4VhnkUCXOSEkLz9Ot4Uy1QeymV7J0ke0v070iQ1vrEPBW6uIUVGKy65bn74wWTo6iKSsm8GxRM2VLGgYs24_ibinubjdhMPnwYi4Zi1mWgrN1XkEaWeOzpRyx0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=Evh7HnQtq4sjPHDxwBuPZNEnTLTGxqyJjDVYZl7bfW-fxIEg1fMI8AxejFf8OGdW5dXMk5DkviBDjz9KpgxCOFRX91bDChtc8UOl7svOnTOWI_COPU4DclRDFN_FGqhl4TbCZGVAh6v2fVpryy3UuBNSwj8UH3v3bOUU8Z0wu_wv_oMEBrHVt2tynwsD_lTwFEoS30fYh3oiljdM3aezzAXMLpnWOXJhcWFEggfPjad9aOb0XVH7ZNIN3JAFT18OUujrAPPMnQu2OVUQTYkr6sdy9m90cC50WTPZbXxbk__WKgIXd71CVzZ7Pn-gnJv9sxkIoawYweqw7e0mg-WfY41QU9ReK0lo6tDY8sxDGwGrDqf7rJTLwbwAHB_xO9hQSJILpiWK0_jw45tGOjdBazjDZHKY2F3ouu3UrWuRgvjM8rW98EoxPPOG7OyxsCkWIzC6_GEMR4tyAMOkyLeZ-8GlnLDpY5yuu6gsaOXdu2B5uUuuY-QHjsaNfXNZ7BF4lXyDMauKZWv17czUjKS2RQtoqgkr0E5Zjk1ypVI5oHBxYp4v4VhnkUCXOSEkLz9Ot4Uy1QeymV7J0ke0v070iQ1vrEPBW6uIUVGKy65bn74wWTo6iKSsm8GxRM2VLGgYs24_ibinubjdhMPnwYi4Zi1mWgrN1XkEaWeOzpRyx0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درگیری کورتیس‌جونز، سیمیکاس و سوبوسلای بر سر بازوبند کاپیتانی لیورپول در بازی دوستانه اخیر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102435" target="_blank">📅 17:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102433">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nHwFcDHMp2wBbiK2JF9ErBGXAVY4KJL7ojrHa0TX_v_kQX0L9MNn6WtxCrotCZh7OgPJ15spZ2hP5B-CxZnkg9IUCr5b-vwu3xUVPNl0IwNJ51Zbomf6Jy0HShz95s7A2xpE6HfosHXLVsjyZZe0vz7QcsZGt3wrhWZJubFEiQ8v8e1v5ClcZlWDOHGazj-cCcsPFoXuI3JlPlOxmh4s8yVQEtj6fZtlqS-ASMfVGgH4UFu21O94u5Rc0HkfWjwc_XBNSCw85KSE-3rxgASC6mWakRxfTocPZnmvdvBBcle0qCXmuVhhHiDQqrOiatxDomElRmPmnfwpU8OIncNb_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RN0cl0AK3F78DCu7MMEwnpFJWqqKprTfA2AAfNCM5As8y1i-XS08PPhTDvrMJgkxHgPcW3PhkGGom8Ch0kPOidDq9SojmvN7yWlfzUVx-nvfM6M05ZpZy16FrkWSGO79z8UQ6feSYU8X0226U83uWtuE31zmJqV7BaZTAKUeQWgmmUZhAnUpwu3np5pKV7ixlyPlNs6fHgcPOnWGWvm_CxVwPphtKTxWtyzMkMjHdJydxMV2CrHG-7x-i5gBhnLS1S6uDCMqts0NMPR812z1DukBt1e0vDBbx8T7KxiZQo899gtffKYQ8_reIxSrdiSC25vLYj-3nsQLLrfipOCH6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ال اسپانیول:
پرتغال و اسپانیا اعلام کردن اگه اینفانتینو پیشنهاد خصوصی سازی جام جهانی رو پس نگیره از میزبانی جام جهانی 2030 کناره گیری خواهند کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102433" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102432">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96363baca3.mp4?token=umVhdByQNsT-UhaeU8M9STAx70Qu1Ur8hRfCZlyCpuGPgyi-uA2GWms-SQ6DUjnKkG3qs50aF4nhP9B0mU7qNRdWcWkZnFfI_JO69aLP5V1Dmc93IgWN2oG7CA9jutExSZ5_NtU3cMMzVBLcqirMJbA86WWp-kYJFM_MCduj_RSNOGLLc9bFQPA9nPFJik9C_an7l6H9MzwaXrgG1BcejYBJk-EDEP0ridpZVVQ9MshO8twXVo2tIKX9qXufqGBUZBc8LdZuJeOghMiQ6aMs4PeZMQJu7qYWIMF-mfYL4qGpqonOAJsxuFvH84mEkwWyRDEfdsVDGc3J7IxkVYSBkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96363baca3.mp4?token=umVhdByQNsT-UhaeU8M9STAx70Qu1Ur8hRfCZlyCpuGPgyi-uA2GWms-SQ6DUjnKkG3qs50aF4nhP9B0mU7qNRdWcWkZnFfI_JO69aLP5V1Dmc93IgWN2oG7CA9jutExSZ5_NtU3cMMzVBLcqirMJbA86WWp-kYJFM_MCduj_RSNOGLLc9bFQPA9nPFJik9C_an7l6H9MzwaXrgG1BcejYBJk-EDEP0ridpZVVQ9MshO8twXVo2tIKX9qXufqGBUZBc8LdZuJeOghMiQ6aMs4PeZMQJu7qYWIMF-mfYL4qGpqonOAJsxuFvH84mEkwWyRDEfdsVDGc3J7IxkVYSBkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مرزها برای میزبانی از زائران اربعین آماده‌تر از همیشه
🔹
در آستانه اربعین حسینی، پروژه‌های عمرانی و زیرساختی در پایانه‌های مرزی کشور با هدف تسهیل تردد زائران اجرا شده است.
🔹
در مهران ظرفیت خدمات و زیرساخت‌های برق، آب و روشنایی تقویت شده، در شلمچه بازسازی و نوسازی بخش‌های مختلف پایانه انجام گرفته، چذابه با توسعه امکانات رفاهی تجهیز شده، باشماق به سامانه‌های هوشمند مدیریت تردد مجهز شده، تمرچین توسعه زیرساخت‌های خدماتی و ساماندهی محوطه را پشت سر گذاشته و در خسروی نیز سالن‌های مسافری، پارکینگ‌ها و فضاهای خدمت‌رسانی توسعه یافته‌اند.
🔹
همه این اقدامات با یک هدف انجام شده است؛ سفری ایمن‌تر، روان‌تر و آرام‌تر برای زائران اربعین
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/102432" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102431">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">💥
🧐
رونالدو، پسرش و جورجینا درحال عشق و حال در گرمای تابستونی اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/102431" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102430">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=FgUtw-r60oDau7n9IVJWuZJ2h6tzMQObG3cJfxmo-EOxP2jYzutSPjThv5O4iOA_IY4nHhGKQrSFmoi6gMj-86fb8YQzOsb4-XOQlzknvr61owqv_74umg69RwuVRlULqvJJRoJmMm_SEy0dc83YRkFgCzwUbvMdcQB6tu9OHB61ZukbOpUt4y-oDCmlOb4VjTr6Bh--wmAaj5L_X8zAz5M3g1pCAFor-DV6S0ieTVVQJifGgRfVQ4QZVkPFWtE5334cozrONcrFKWMhtARUNzQtgVh_b_wYHNZ0pPX_nTdYHqCVERtHn7_DTfyJ-SxznuIbeWttC5GYBBZsiWFg9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=FgUtw-r60oDau7n9IVJWuZJ2h6tzMQObG3cJfxmo-EOxP2jYzutSPjThv5O4iOA_IY4nHhGKQrSFmoi6gMj-86fb8YQzOsb4-XOQlzknvr61owqv_74umg69RwuVRlULqvJJRoJmMm_SEy0dc83YRkFgCzwUbvMdcQB6tu9OHB61ZukbOpUt4y-oDCmlOb4VjTr6Bh--wmAaj5L_X8zAz5M3g1pCAFor-DV6S0ieTVVQJifGgRfVQ4QZVkPFWtE5334cozrONcrFKWMhtARUNzQtgVh_b_wYHNZ0pPX_nTdYHqCVERtHn7_DTfyJ-SxznuIbeWttC5GYBBZsiWFg9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
🎙
تمجید جالب کاسمیرو از لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102430" target="_blank">📅 17:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102429">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=oHS00TsnqkM_SA1MJRP-pk3yHsZFHF9oR_EwVAVTFqWb6P7bA1iGdGYEXs9OIVF2Nk5F5n81uYs6r-ji5bg3Gy-acOXeJ6Eo3-EJmXIkdBmUusptln6m86OOsljARsTrW6dY4Fn3mkm5cX0VSaKCYJ_PqCFDhVS8qhbqSiJS_441XfloMkDqrUCXh-K_9Z7OQUafUHCFtnMiSc7JJ4NxV1AOcnLtCxU0nWXhpDfAM1inkKhjkfWs5AI5ZiEF0hU2kIq0RewfHg6ZxlS4KD7OqTLLvGSBqRzIXcWRdms5Y6pNMdk2dRSlrpeeBgfs6KnhQgtyIkDtQFvoEB-kJ0ZKjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=oHS00TsnqkM_SA1MJRP-pk3yHsZFHF9oR_EwVAVTFqWb6P7bA1iGdGYEXs9OIVF2Nk5F5n81uYs6r-ji5bg3Gy-acOXeJ6Eo3-EJmXIkdBmUusptln6m86OOsljARsTrW6dY4Fn3mkm5cX0VSaKCYJ_PqCFDhVS8qhbqSiJS_441XfloMkDqrUCXh-K_9Z7OQUafUHCFtnMiSc7JJ4NxV1AOcnLtCxU0nWXhpDfAM1inkKhjkfWs5AI5ZiEF0hU2kIq0RewfHg6ZxlS4KD7OqTLLvGSBqRzIXcWRdms5Y6pNMdk2dRSlrpeeBgfs6KnhQgtyIkDtQFvoEB-kJ0ZKjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
یادی‌کنیم از بازی تاریخی ایران و قطر با گزارش جذاب عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102429" target="_blank">📅 16:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102428">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=o91K7Lx-zpaxXmFYy2t5227G4zX2fH9hX_wr12pGakv8Uf1_161MAxE7GqmkVIRhDMWbfDYlj98e-5HMSZIEwz-9Yjki8YrC3PcrXVz8R_9sGBR7mBc9_jnDC2gVCUv6cMX_4moxAAZ5JWqUoIwgM9046ufr7Tvrp98U3EMlI1VhSzV2wOa5aChy41xvWwvOpG4pzvLWIutJKA6Tv1_AhRH_b4-MHwmfyF0D9-y1p9Y8m7UwrSV8_tEpq2TlDdgirJRabN3KXXCrzFjnjI-jLz23cYjr_Gfg0KiqkLycbDT8-iqwptLqvg2Ti_O8wCOBnjELaJHcAuj44rMH4SqGRoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=o91K7Lx-zpaxXmFYy2t5227G4zX2fH9hX_wr12pGakv8Uf1_161MAxE7GqmkVIRhDMWbfDYlj98e-5HMSZIEwz-9Yjki8YrC3PcrXVz8R_9sGBR7mBc9_jnDC2gVCUv6cMX_4moxAAZ5JWqUoIwgM9046ufr7Tvrp98U3EMlI1VhSzV2wOa5aChy41xvWwvOpG4pzvLWIutJKA6Tv1_AhRH_b4-MHwmfyF0D9-y1p9Y8m7UwrSV8_tEpq2TlDdgirJRabN3KXXCrzFjnjI-jLz23cYjr_Gfg0KiqkLycbDT8-iqwptLqvg2Ti_O8wCOBnjELaJHcAuj44rMH4SqGRoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیاز بود یه آیتم جدا برا لحظات تاریخی فیروز خان کریمی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102428" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102427">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17c8ef3f2.mp4?token=gIndYMqmRfr371tjG65cYDKQKJnzVDKWEgtJxnQSLe1tU48-apycM3wj9DW6-_rJu19JuMQkC2EmVqQrENSQhbQUm-8GGPRCKuxJPsyGTWvj6fImSwB0fmE4pG1tsu8R4ulkkqDVw_pwX_lFTqTkCULqx1Qmrgu99upwQI-kj_L_c8_iwtj08IS2ozdgpVOzSnrD89meIZzFke4I8ogYG75R3dL1rE3LGP6sQiWFRTD0QpN77dfusNd31x3GCZUKo7x20fyYSP1hUX17JmetCA4ILSDmYmN3TYHzDvEy3NqxqpRgIG1TB438HqTqK6PMOsZCgxQ8R7bhMM9lOKCrpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17c8ef3f2.mp4?token=gIndYMqmRfr371tjG65cYDKQKJnzVDKWEgtJxnQSLe1tU48-apycM3wj9DW6-_rJu19JuMQkC2EmVqQrENSQhbQUm-8GGPRCKuxJPsyGTWvj6fImSwB0fmE4pG1tsu8R4ulkkqDVw_pwX_lFTqTkCULqx1Qmrgu99upwQI-kj_L_c8_iwtj08IS2ozdgpVOzSnrD89meIZzFke4I8ogYG75R3dL1rE3LGP6sQiWFRTD0QpN77dfusNd31x3GCZUKo7x20fyYSP1hUX17JmetCA4ILSDmYmN3TYHzDvEy3NqxqpRgIG1TB438HqTqK6PMOsZCgxQ8R7bhMM9lOKCrpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
▶️
رکورد پرش سه گام جاناتان ادواردز (۱۹۹۵) با ۱۸.۲۹ متر ثبت شد و ۳۰ سال پابرجاست. این دستاورد استثنایی در دو و میدانی تحسین شده است. ادواردز در مصاحبه اخیر بر تکنیک منحصر به فرد و هماهنگی قدرت و تکنیک تأکید کرد. او پیشرفت رشته را با شکستن رکورد توسط نسل جدید ورزشکاران مفید می‌داند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102427" target="_blank">📅 16:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102426">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543e2ce52d.mp4?token=HYdl513e0ehGcemOkUppawQmPB-0U4TFMT49D3KJHMgPnZVy5BfPPoKXPwFthHXmBU5S_49vvpFldAMCb6OyZa7MSgV6gecFukM2ofyE1tzqa5PoFSSDF6-Xecf0RM49aJBvNRBeZ8ExOS5EOcrHZ2aFMjdWuAk_VrOlgq3WgT6iVwQ7u7YKgSHqOMHBCbFtQ-MOiXHFIiahE7v94oH-6XSGMpd5QWAzKVRrDU1czKXTpBo_vEFRmtORveIaGp405mVNuc1tldggXEkPY6kTcWbMsa0evJj_MsEoXiZY_doFx2AwmKB2O27ewOgjMTece6GNe0yeJWd6CXwqiOQQyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543e2ce52d.mp4?token=HYdl513e0ehGcemOkUppawQmPB-0U4TFMT49D3KJHMgPnZVy5BfPPoKXPwFthHXmBU5S_49vvpFldAMCb6OyZa7MSgV6gecFukM2ofyE1tzqa5PoFSSDF6-Xecf0RM49aJBvNRBeZ8ExOS5EOcrHZ2aFMjdWuAk_VrOlgq3WgT6iVwQ7u7YKgSHqOMHBCbFtQ-MOiXHFIiahE7v94oH-6XSGMpd5QWAzKVRrDU1czKXTpBo_vEFRmtORveIaGp405mVNuc1tldggXEkPY6kTcWbMsa0evJj_MsEoXiZY_doFx2AwmKB2O27ewOgjMTece6GNe0yeJWd6CXwqiOQQyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو کمتر دیده شده از مارادونا و فن‌پرسی
💘
💘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102426" target="_blank">📅 15:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102425">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e43f315425.mp4?token=aPe6JLoy1GcomqXjIjoUlK5YXkFZTJw72agYupWEumdY5K6IY6FX3kbBSD4EwxDICiFzwCxJ8OvJucf562tPmccxGf0hY2fQGO-s0GEMcSDHTdOvR9ZVDvDKp0_ub9lMIW2SQ1PsWJneFsEmmGI1w1n4rZ3XLlgG2pEVLtoyiZOQ1ZLctFQYkPUReK-RvWlaG5WCArsJkqYHpMolx08cOdOuMPLHPEQVbmoyHbNgb9DHfDZupKmLNKu56uJjz8d3_SVHrSzo5nAtBtAwSkIsdk0qt3kd1H943kcCOnSI4ArSUMw-bt4N4-KPTE5YTQytE2-fw0sLJvzXupBbCMX0fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e43f315425.mp4?token=aPe6JLoy1GcomqXjIjoUlK5YXkFZTJw72agYupWEumdY5K6IY6FX3kbBSD4EwxDICiFzwCxJ8OvJucf562tPmccxGf0hY2fQGO-s0GEMcSDHTdOvR9ZVDvDKp0_ub9lMIW2SQ1PsWJneFsEmmGI1w1n4rZ3XLlgG2pEVLtoyiZOQ1ZLctFQYkPUReK-RvWlaG5WCArsJkqYHpMolx08cOdOuMPLHPEQVbmoyHbNgb9DHfDZupKmLNKu56uJjz8d3_SVHrSzo5nAtBtAwSkIsdk0qt3kd1H943kcCOnSI4ArSUMw-bt4N4-KPTE5YTQytE2-fw0sLJvzXupBbCMX0fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
⚠️
تجسمی از المپیک اگر تهران برگذار میشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102425" target="_blank">📅 15:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102424">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea1f4ae5ef.mp4?token=r1IHsPWJFEHraRIBXHOeZhfrpP3wiQOX_Cv8XuzwdO7QAvvAy1jjGBJ7B_-_ttxXlAxSBKz_8j_EL2g7XwctrGNLLfU3xfse6Yyg7NgEPwVPFMFQy1T5wfq9XqT-VA815_QCVlFkstJizasppXNM7D0HmTQ9toWXY0rG6xAd5zRfBmsA3BQwqrZCWKqky8zBvcxRY0YWjRHueNhAckrf3Yq48j68kR9SLD_b5pE0Wjt-QQCeoXLiyzJ69ff9EOsybSDjsTOVZOR_V5V89hfJzEwKXEnAjSw_Y7fTnCVGY3spVq2EIaRo1yH0BUrjSVwjFVv-mDXfhI6-GCOQKpSCGraYI1wdVCi2vUvlp7MOzDcyidwyTl4YMLXZ6nfXY2Ko3C5GMrEf8Y9gxGkPJ5ZBm1XMUiYNE_d13YmY3CyN0DiCIE9kjxhsR2uypXrJk1NUZlXB-zVoLxxDEMJvHa6nNuqHJlE6rVEu3kI1AuO0le-Z7Oe534AUzIJluhj7XrelUrNLM_KZa0KLYLEcrqYz3AqgE6dBX8ifslQBiyUeUOv4wimHv5bE8llzv_cm_bCKf5yi7uyOE1UaqdMyENuOmR794TTsdcTJmzawn9tWX8ZZdChmrGEwlkobsvSFYi1vEU7H4VCX8gsP1Vf7rhqFpm_RId7Pquy-4LvYOO_Z8ls" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea1f4ae5ef.mp4?token=r1IHsPWJFEHraRIBXHOeZhfrpP3wiQOX_Cv8XuzwdO7QAvvAy1jjGBJ7B_-_ttxXlAxSBKz_8j_EL2g7XwctrGNLLfU3xfse6Yyg7NgEPwVPFMFQy1T5wfq9XqT-VA815_QCVlFkstJizasppXNM7D0HmTQ9toWXY0rG6xAd5zRfBmsA3BQwqrZCWKqky8zBvcxRY0YWjRHueNhAckrf3Yq48j68kR9SLD_b5pE0Wjt-QQCeoXLiyzJ69ff9EOsybSDjsTOVZOR_V5V89hfJzEwKXEnAjSw_Y7fTnCVGY3spVq2EIaRo1yH0BUrjSVwjFVv-mDXfhI6-GCOQKpSCGraYI1wdVCi2vUvlp7MOzDcyidwyTl4YMLXZ6nfXY2Ko3C5GMrEf8Y9gxGkPJ5ZBm1XMUiYNE_d13YmY3CyN0DiCIE9kjxhsR2uypXrJk1NUZlXB-zVoLxxDEMJvHa6nNuqHJlE6rVEu3kI1AuO0le-Z7Oe534AUzIJluhj7XrelUrNLM_KZa0KLYLEcrqYz3AqgE6dBX8ifslQBiyUeUOv4wimHv5bE8llzv_cm_bCKf5yi7uyOE1UaqdMyENuOmR794TTsdcTJmzawn9tWX8ZZdChmrGEwlkobsvSFYi1vEU7H4VCX8gsP1Vf7rhqFpm_RId7Pquy-4LvYOO_Z8ls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🔥
👀
۵ گل زیبا و برتر اولیویر ژیرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102424" target="_blank">📅 15:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102423">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3bfea056.mp4?token=vmzBqLw_rsQ3rAXiT1HSI1-LAAqpgLSKcwkzlU8Xmja4XHrJ_rWKAtKtBOuPDjhbpl8qbB0FFlLyTX0EyTvVHZLt_fWnzVzBN1AooiOQFiLyc0Kva9NZqaROEOchlY1sy3kOGQn4Tn5nydh14X8iMonORLnLvmr0N-daMTjIiE0OXaDAXbLM2kythl1knNw9XvUogOgsPPqL0VPBwDJpQ0jS7Hp0J73hqZetVZ6fOVJTsyP4RwUEZ8ts06ejk6wxJ_W7xX__5P1Fu3XxIyrezTyReoAN68Essnb7qaKTFvgons9syVQp89GQf15juMAuxy8e3EgAJFQrrDJpNtJ88g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3bfea056.mp4?token=vmzBqLw_rsQ3rAXiT1HSI1-LAAqpgLSKcwkzlU8Xmja4XHrJ_rWKAtKtBOuPDjhbpl8qbB0FFlLyTX0EyTvVHZLt_fWnzVzBN1AooiOQFiLyc0Kva9NZqaROEOchlY1sy3kOGQn4Tn5nydh14X8iMonORLnLvmr0N-daMTjIiE0OXaDAXbLM2kythl1knNw9XvUogOgsPPqL0VPBwDJpQ0jS7Hp0J73hqZetVZ6fOVJTsyP4RwUEZ8ts06ejk6wxJ_W7xX__5P1Fu3XxIyrezTyReoAN68Essnb7qaKTFvgons9syVQp89GQf15juMAuxy8e3EgAJFQrrDJpNtJ88g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
سه دقیقه با لیونل مسی ورژن 2014/15
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102423" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102422">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Et4l1HTESEJfFUDcDjx2caF52B_5YGldqa-XDUyKbL8J-7DgRykNbWfnTpO4E9lqrGJTyUaJdfAmNN3e3asD2fuReYHIAgeJCSe0e2gm92WsLOy_3ZCUeNLYleaFiTk4X1kBh6A6bS3mYy8sDsTpWGtMR3XVsssJfXRWQbqWQk9Fs4OwqvCMA79tKr5zvZO8-QbebUiiuDui05Zcu7lfRsHPHAsmywVeoa-M3DedkO18-6Rh0UPbz7HhoxC49TvkoI7PJUwahnoUUOerivUgpMjfJnVZ1JBZSDiHWoVoUe-mDPJIsM5a-QUM8g6Dya_dcMe_PCy_DVoo27Gfyr1lVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
لیست رئال‌مادرید برای بازی با فیورنتینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102422" target="_blank">📅 14:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102421">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0ZBbWq5loshZJ6Jw6jKA2YRi7w-LzEGOHvKahPWpW7XNE3ZKN-OphaNBUX9ASFDdSTLjYlHNlPm9mInz8wBAx5JxemcpDCTOzE8UaiWOIGAPyKk95YyLtHVGKD0-44A8MsDmcZ9o9flRerclvKkI9tdH2nGezdZTKzwRCGNoOC3aknhsUr2B8WZNvbK-Dg0yLjM2sChpPM0nkfQda2y9vnFPukhPux3wuy_ohu8lzttFnUEtfoKBlp0Moyb5uY7QXQnpKzTrfmO1IBoK55IlaL1_XeC6TKAb74VKD95sJSTHjJXdkBDu_8x1wT-ZEPQwuxQSRlx_eBXAKaud0_Hlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
#فوووووری
از نشریه اکیپ فرانسه: آرسنال با نیوکاسل بر سر انتقال برونو گیمارش به مبلغ ۹۰ میلیون یورو به توافق‌نهایی دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102421" target="_blank">📅 14:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102420">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=P-2j7ZHXIPyArZpKhltpMbvbIIXhwtfz1Wet7fxpq_51Xj-1_hb-QAtC5Fmq-XHnWYZnxlqAVWUpetlm0oZKGX4anuDAAJQHzFYduglTADZ8B_6WGPZ6GXDD1M3zllKj2EOGQQctC9nixZHJUeywgNyTUfN1cNojppBMeDQ1F3x7w08swEDIkB7jO-OPSJvALuPtYpjiSE2ro3MBo-Bw_OA_4tao2c6okxqHBsU3O2kKp0oUDlkzxTkFZDDszUJQIwXsZCqcD73oKPjFljlGyhv66Os-HpMY8myC_ThNdzKkOOvljH6L3WBmcgqFc20FOT39ZD71P7ZSSXVvoyWtTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=P-2j7ZHXIPyArZpKhltpMbvbIIXhwtfz1Wet7fxpq_51Xj-1_hb-QAtC5Fmq-XHnWYZnxlqAVWUpetlm0oZKGX4anuDAAJQHzFYduglTADZ8B_6WGPZ6GXDD1M3zllKj2EOGQQctC9nixZHJUeywgNyTUfN1cNojppBMeDQ1F3x7w08swEDIkB7jO-OPSJvALuPtYpjiSE2ro3MBo-Bw_OA_4tao2c6okxqHBsU3O2kKp0oUDlkzxTkFZDDszUJQIwXsZCqcD73oKPjFljlGyhv66Os-HpMY8myC_ThNdzKkOOvljH6L3WBmcgqFc20FOT39ZD71P7ZSSXVvoyWtTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
✅
یوسفی: زمین و تماشاگر که ندارید، لیگ را پلی استیشنی برگزار کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102420" target="_blank">📅 14:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102419">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9889076a09.mp4?token=ligMdqapXWUeSUbke9KuZoLiuLT1s_n0IXtW96I1W1v2fdEYifk2SkfF76IXipGhHnN2rm9fpdPRO1auoPBMM8DrYZTrz8pPZKAsFMtcG3Z8zsneXPbEh9rJdWm0ndwRL83X1DPHcGfCeCW8NXBqBqxMI5kImHaTTApbrRX7ZMKkwXyzJrbu-Eivaa-bDR_nVEGtNnUNZYLWlhCUfskn5PRvX7BYlg6ySjcDFpbvl1zxJQtmkeNAH8hT8FPWXqB-u_NMvL8Nag45vpO0OPojhlIJQLJ7ZYNuX9-tbNr6v0PMOwkvD9KeLYgUpDL-2PdMO179vVYLxmer5HM90EtSMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9889076a09.mp4?token=ligMdqapXWUeSUbke9KuZoLiuLT1s_n0IXtW96I1W1v2fdEYifk2SkfF76IXipGhHnN2rm9fpdPRO1auoPBMM8DrYZTrz8pPZKAsFMtcG3Z8zsneXPbEh9rJdWm0ndwRL83X1DPHcGfCeCW8NXBqBqxMI5kImHaTTApbrRX7ZMKkwXyzJrbu-Eivaa-bDR_nVEGtNnUNZYLWlhCUfskn5PRvX7BYlg6ySjcDFpbvl1zxJQtmkeNAH8hT8FPWXqB-u_NMvL8Nag45vpO0OPojhlIJQLJ7ZYNuX9-tbNr6v0PMOwkvD9KeLYgUpDL-2PdMO179vVYLxmer5HM90EtSMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
💥
روزی که پیتر چک آماده ترین گلر آن دوران فوتبال میخکوب شد و این اثر هنری شاعر رو تماشا کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102419" target="_blank">📅 13:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102418">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5Juwqp-dVbKGQbm45IL7lfNcV69ACxlGpMzMbp_6rUHSwb9Q0TPT_3Yp9STYceG8Aho0mkjA-Ggh3xc3vDkeFWVOGDF4yomLkYn2IqWy6cP7I5hi5WP7v-Z7o1kkIegldFG6uxtvHq3wDqTDLK3WVdscqOHdOLyKX5qo-PsUi8lYN6-laAEAozTbgbJ4j_fAqVHBA3jdmk7dNRyY60OYyr1Oa62E3GNJ2meDCjyfk-1aBPjsKz11UdG4KAazFH7Tlq9j7mCsWYPTHrc-nyICq4BfPpLtJTnaI6Ag9zWVa_beBTMqnIwTtrTBJ0c_PDS2NiBIGKrbIJWXLKo3ZiAcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
کارلوس اسپی تو تمرینات رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102418" target="_blank">📅 13:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102417">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REIFg82wd40wQ-16PmVZ6RLNlJ-91oVZqwboO3w37rnGpKbZ4umrlzidcx0M5s-HkqEhpo7Waa9zltNhpUiMV2o3rsivUTfV8iPZ-0y1UP274qFsNjaAvNndbIn0iIm6EAFzZ1Ug6AO2EDkrysjJklyXsUnbz1QPASTLadLY9RUOE7-zaQy6wzUj5fo3SgTFDiIiT-fTr7ztU3dmofeSrK0TslUaP8U-hrAxZI5Cx_9ShvjLp_MkgLYoEdznR8PdHoo2j-28p0v8g3AtqJymW1bi94NJODXrK5VnVyup8dKUKlHipaCxBT82s84rlp5DFNNEGxWZlEdHOt0PvTBOnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
روزنامه اسپورت: دو باشگاه آرسنال و تاتنهام به رقابت برای جذب فران‌تورس پیوستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102417" target="_blank">📅 13:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102416">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4938ae1d8.mp4?token=Ap-dnUGv9lNq3Ivp5D2iYPO_VKbXMRugR-kuhucdGli-Oop-bsfwJqM8tn0oM3BFYGCSCBYc1l-39W9CM8GtvnOt5ZtWMJZp1Y7121CeAbJFtTBfkx2YlC0hbbexmCMB1aigTBMgmnIZrMn3WEx3zdF1YN6BIVjWnpvvkLBHUTFjwgwIpscA40nactxOcGqk8C-f3-yVkRUDH2Fv7s2HalOyLBsHDQKPh45uLL-6lRs3GiqE7LIETx1faII84FDE2EvdRnvIaSidVqmWqepbFakueUnG-NRTy4tjhCjXXAtUs3zt4eXNy32wdMCsbff0x3CJT8xIpHw9xU5LQYmsMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4938ae1d8.mp4?token=Ap-dnUGv9lNq3Ivp5D2iYPO_VKbXMRugR-kuhucdGli-Oop-bsfwJqM8tn0oM3BFYGCSCBYc1l-39W9CM8GtvnOt5ZtWMJZp1Y7121CeAbJFtTBfkx2YlC0hbbexmCMB1aigTBMgmnIZrMn3WEx3zdF1YN6BIVjWnpvvkLBHUTFjwgwIpscA40nactxOcGqk8C-f3-yVkRUDH2Fv7s2HalOyLBsHDQKPh45uLL-6lRs3GiqE7LIETx1faII84FDE2EvdRnvIaSidVqmWqepbFakueUnG-NRTy4tjhCjXXAtUs3zt4eXNy32wdMCsbff0x3CJT8xIpHw9xU5LQYmsMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های بامزه رونالدو از ارتباط صمیمی با پسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102416" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102415">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5029f55db8.mp4?token=v1LZzdyZc_QPndIy4f580icj87kauh6VV-S1Ji3-7pERiHV2AWA7vKymm3baHJu0ib_XeE7jjg0dki4e9Ar-9wp5vWJgO5N4ZC76u9KwalAS8GapDWZ10n4DGIdIfg_qgPkTU3cBPGmr8ipCUNnDh2lb4UEeDnDgWMHux0ZLUm-KIjldTZ1QfEOnjnlmE5QA_Tfw4xNCfqxL1P6SoheuNBEqC4kAlC4V1qcaW9FH7P3mYYxnpHjvYFD2Sbr2bukY9wa7S5__k5aleU1DM2hLQXwB9kw3cIwZyN7elGOOxdbg-E3Z5RPD6uMHeeyad_JAgKlu3K0lfoynVI2w4yISjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5029f55db8.mp4?token=v1LZzdyZc_QPndIy4f580icj87kauh6VV-S1Ji3-7pERiHV2AWA7vKymm3baHJu0ib_XeE7jjg0dki4e9Ar-9wp5vWJgO5N4ZC76u9KwalAS8GapDWZ10n4DGIdIfg_qgPkTU3cBPGmr8ipCUNnDh2lb4UEeDnDgWMHux0ZLUm-KIjldTZ1QfEOnjnlmE5QA_Tfw4xNCfqxL1P6SoheuNBEqC4kAlC4V1qcaW9FH7P3mYYxnpHjvYFD2Sbr2bukY9wa7S5__k5aleU1DM2hLQXwB9kw3cIwZyN7elGOOxdbg-E3Z5RPD6uMHeeyad_JAgKlu3K0lfoynVI2w4yISjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🔵
درخواست کودکان جنوبی کشور در وضعیت جنگی از رامین‌رضاییان بازیکن استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102415" target="_blank">📅 13:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102414">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac78119da.mp4?token=c8z2cbeLKgt7OoFzChOGLNUoF4hl_uk5aH3mxNSZMcN_rwZRw7u8wlPDy4XG4PslKLVly4QUA8UEDLuACjKVedJMtJR-1_6Cm97smGGAAjKK41YrBji2ONgr-DbIjxAHQFECvJyRHJPb3M4Lpqei1GIYqEuC_4jSPrdhe4nU8eQxqYB5CesUBryGAK5qVJdwFTr1Xx6hIOtMJyNd2NwUXE9cWuQpxp4hJS4SpOc7WTiNR9n3n8nKlrwghTblatLxqL3bEDWVZzKHNIwBxzfi13MWqMi36kQ6kmgra8sD3ZtQH-Ew84d8Jxkq81_FJnAitqqbYMw7JxxgLXxZzOBDAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac78119da.mp4?token=c8z2cbeLKgt7OoFzChOGLNUoF4hl_uk5aH3mxNSZMcN_rwZRw7u8wlPDy4XG4PslKLVly4QUA8UEDLuACjKVedJMtJR-1_6Cm97smGGAAjKK41YrBji2ONgr-DbIjxAHQFECvJyRHJPb3M4Lpqei1GIYqEuC_4jSPrdhe4nU8eQxqYB5CesUBryGAK5qVJdwFTr1Xx6hIOtMJyNd2NwUXE9cWuQpxp4hJS4SpOc7WTiNR9n3n8nKlrwghTblatLxqL3bEDWVZzKHNIwBxzfi13MWqMi36kQ6kmgra8sD3ZtQH-Ew84d8Jxkq81_FJnAitqqbYMw7JxxgLXxZzOBDAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
نصیحت اسطوره‌رونالدو به امباپه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102414" target="_blank">📅 12:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102413">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🤩
#فوووووری فابریزیو رومانو: آلن هالیلوویچ استعداد برباد رفته بارسلونا در آستانه امضای قرارداد با پرسپولیس قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102413" target="_blank">📅 12:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102412">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b732a95e.mp4?token=Izrc80HCjYv9FhwZfqoTxtH7Gxq5iWZmPCdh9pH0j2o6owm-wZ95H1PGFonyeWBKYu19ZTXgHvhex6ANzIlkiKj-nD59_jmQBACumb8kc66eRMvlMIymtmciL5o--c7IBLp7aq4WdNnPAlEpTGfa5PZlDakZq0IlSJtCTqfZ_7Dc0Q6gVJQ7WGIYNHHxb85crRgeOMrQqc23kf5zlc06NkzcyzOpff3zPFGBW0w6S1KxqKNtwVUv7qFTdpebeHJu0gxB05B-EBialBQ3h4EXXJ8rVV0Pw6vMM0IiwEfeBde044I5PGyOohJ9T2N_3qD16P3hsyr7xT0PX0r_dG4bsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b732a95e.mp4?token=Izrc80HCjYv9FhwZfqoTxtH7Gxq5iWZmPCdh9pH0j2o6owm-wZ95H1PGFonyeWBKYu19ZTXgHvhex6ANzIlkiKj-nD59_jmQBACumb8kc66eRMvlMIymtmciL5o--c7IBLp7aq4WdNnPAlEpTGfa5PZlDakZq0IlSJtCTqfZ_7Dc0Q6gVJQ7WGIYNHHxb85crRgeOMrQqc23kf5zlc06NkzcyzOpff3zPFGBW0w6S1KxqKNtwVUv7qFTdpebeHJu0gxB05B-EBialBQ3h4EXXJ8rVV0Pw6vMM0IiwEfeBde044I5PGyOohJ9T2N_3qD16P3hsyr7xT0PX0r_dG4bsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇧🇷
آنچلوتی: "در هایدریشن بریک نیمه دوم بازی جلو نروژ اشتباه کردم تیم رو تغییر دادم که باعث شد کنترل بازی از دستمون در بره و ببازیم..."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102412" target="_blank">📅 12:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102411">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=EBZeBcWkmOwxfU2mt07N9FAuluqdkzMLCEdAPkYOHpLK9HhcNouUF7dc52Pzebfb87ITNWcAQiwJuTzaZNgJdjLTTBnqXvb25bltLzjxR9eThanlcUgOyJ2pH3YHCTL5PebSD3wZCsfcuiIitgTrh1d7yA4KB-oIK4T7s60A7nklMqL01w9f7bUQkwEd9ZkTJsvKi21A__HkKhQHkS8WQhSk3pDhprXCb2vTMQHlRVGgHiHFm8lQzd47s4qBMRyAwwJ23qBFWqmHhBq0SYBUc5x3QMyj0Zo9SgvFrIQClOG617lPU5dfRatL-Z9rW9aHNYorgU0QSfd_Gx0BMauvjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=EBZeBcWkmOwxfU2mt07N9FAuluqdkzMLCEdAPkYOHpLK9HhcNouUF7dc52Pzebfb87ITNWcAQiwJuTzaZNgJdjLTTBnqXvb25bltLzjxR9eThanlcUgOyJ2pH3YHCTL5PebSD3wZCsfcuiIitgTrh1d7yA4KB-oIK4T7s60A7nklMqL01w9f7bUQkwEd9ZkTJsvKi21A__HkKhQHkS8WQhSk3pDhprXCb2vTMQHlRVGgHiHFm8lQzd47s4qBMRyAwwJ23qBFWqmHhBq0SYBUc5x3QMyj0Zo9SgvFrIQClOG617lPU5dfRatL-Z9rW9aHNYorgU0QSfd_Gx0BMauvjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
جواد موگویی که اخیرا در گفتگو با عراقچی یه سری اطلاعات حساس تهران رو داده بود، این سری اطلاعات مسکونی مقامات نظامی و ... هم افشا کرد
😳
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102411" target="_blank">📅 12:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102410">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b5a4f433a.mp4?token=aeCm49yvCWSiL77lQU-lI0JqQz61z-hMB8_QgN9cl_zOIFPX-DfFIy_6nemxPliq2dZTyEIA5Fb6Cv2quKZOArZZjYvF12_ykZ--5eA1nar4bVszh2i2aT8apdZIJaHQg4uVfQGPcuQXijYV7VKTd7jKeUhA7WM-3AyicZ9Ou5i1LLCtQcIn9UiObem6ExSxtrDWUxInZ6oeLjDw2jpZP7WK59wi3FQ7F--zNya88YHlIazTwam0_hUpwH9FKmPHHYRwLpa2chbqBVq8IgWX8lWj9Bj5Qw5ROlkM7XnL3vHFAnjqGJMDD93a72RHQ0TzeF5yOX_Y3lQMNepVJKcFWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b5a4f433a.mp4?token=aeCm49yvCWSiL77lQU-lI0JqQz61z-hMB8_QgN9cl_zOIFPX-DfFIy_6nemxPliq2dZTyEIA5Fb6Cv2quKZOArZZjYvF12_ykZ--5eA1nar4bVszh2i2aT8apdZIJaHQg4uVfQGPcuQXijYV7VKTd7jKeUhA7WM-3AyicZ9Ou5i1LLCtQcIn9UiObem6ExSxtrDWUxInZ6oeLjDw2jpZP7WK59wi3FQ7F--zNya88YHlIazTwam0_hUpwH9FKmPHHYRwLpa2chbqBVq8IgWX8lWj9Bj5Qw5ROlkM7XnL3vHFAnjqGJMDD93a72RHQ0TzeF5yOX_Y3lQMNepVJKcFWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
🔴
‼️
علیرضا بابایی مدیرعامل چادرملو: تورنمنت سه جانبه به دلیل کمک به پرسپولیس برگزار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102410" target="_blank">📅 12:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102409">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=XKPr8GxENirk5NF29NjjxhOrU4JyoJK8fHH5Xxc5GxS6nKEd3F4hDDtCuosjzi-jKrMk53ZMFqkZzN2zt5yJeayCvkdE9ewdoJ_9CT2MrZWEieRW7krYnRBUyP9oi2N7pdNA2iIO7QRHPeVGpUfwN1BnQI6AiEECRt4YSEXeew1qAHajaLIkx6nHI1R_MBwQtVzpfT0TKKk20Dzm1tyDdP2t03wbHMy3C8vAVUSf-iR7rotp2SviaghUzuE8Ma_uhKd-F6sH-0PlhSZDHEz6B4lAt1ca-1yHpEj7Dp3NCZzlt3Iv7s1hD8ymcYfUtnr5JwGwqq3p8C2B9fbtPmZGEa21qDjvPNymo5eVKG3lZGqiez0UlkjnN0mpIVk3Qiwd5bYndwl2PIta-khO34wh9rjNLBTGqnY_lZb6qIovCj5VZtzuMEkonEYU2wPuJC4tcAx-DeTSP-vTYnaUX5-YDPgOUsSbXR2C5Cjq_9UJ_pS75eD0HNQz0Qqbi6gx7EeO7RNg_FUPcA0DSh_EjCKAzNk_jgjl00jOJYCjCqhVRwK3Gqy4UJgEWuiMvV02m7UVrojNhMerYcqm5o-Af5WdEU6_CF8RrLiQTIflsJdROsXRL9txCNwEMKgUIVhoW70HYuYRx5VsoHMlm6zNpvzfvO2WGtsvfnKNAYCSIAPLj3s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=XKPr8GxENirk5NF29NjjxhOrU4JyoJK8fHH5Xxc5GxS6nKEd3F4hDDtCuosjzi-jKrMk53ZMFqkZzN2zt5yJeayCvkdE9ewdoJ_9CT2MrZWEieRW7krYnRBUyP9oi2N7pdNA2iIO7QRHPeVGpUfwN1BnQI6AiEECRt4YSEXeew1qAHajaLIkx6nHI1R_MBwQtVzpfT0TKKk20Dzm1tyDdP2t03wbHMy3C8vAVUSf-iR7rotp2SviaghUzuE8Ma_uhKd-F6sH-0PlhSZDHEz6B4lAt1ca-1yHpEj7Dp3NCZzlt3Iv7s1hD8ymcYfUtnr5JwGwqq3p8C2B9fbtPmZGEa21qDjvPNymo5eVKG3lZGqiez0UlkjnN0mpIVk3Qiwd5bYndwl2PIta-khO34wh9rjNLBTGqnY_lZb6qIovCj5VZtzuMEkonEYU2wPuJC4tcAx-DeTSP-vTYnaUX5-YDPgOUsSbXR2C5Cjq_9UJ_pS75eD0HNQz0Qqbi6gx7EeO7RNg_FUPcA0DSh_EjCKAzNk_jgjl00jOJYCjCqhVRwK3Gqy4UJgEWuiMvV02m7UVrojNhMerYcqm5o-Af5WdEU6_CF8RrLiQTIflsJdROsXRL9txCNwEMKgUIVhoW70HYuYRx5VsoHMlm6zNpvzfvO2WGtsvfnKNAYCSIAPLj3s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
علیرضا بابایی مدیرعامل چادرملو: بازیکنان را از پای دیگ نذری آوردیم و با خواست خدا پرسپولیس را شکست دادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102409" target="_blank">📅 12:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102408">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=hTfDp_W3Qa--rmRTY5hUPsEqYi0632tXR0DNmRz4hEVZcH-BsPUMi5m0satUgTJu8agFfe_FjxYc2NxWLLXTbG7ddPg4TMwxMZ-OaTBtEdsUxoT884FQqfzwlRpZWMNZZmHmvXZUEpb9ykLb9Gu-N3IFiH-_5GfEdnQdPHXTUaoSO5OaHCbishizOMaT1oZ9_eCwrxJJLcoRhJ5pO-E_y5pNg0kJsAsX3VBDX6t9QRyPtN-jIULsx7SiFLB7LIw9LrGNm-JYe6YSLoQoz0FqmQrSYBvqhlpyxfJpeYYK5NQ5R822CtidJheFTBrzk6rDu-teCWjKukRgtKX5knvXvXVoYiqY9nTVpzEQqCiHeC_jwIuv5iiRTF7P4dunYfuXsTVNGdQujlQL3MvEMRukirn238SlZULPoBP466JMCwYY6XaDOy4SdVjJqr_2RhI-4l6EvfHzRWlqb-3J2kLbBssy0L22mCY6PTxX64Z5IQ-FZL7syZbW_GN6JaByBm1dDArvlX_ErfFJiVXtKTcFMBzuC_5DQh-03wS_HRcs2IKpF4G6vud7MhisQ_1s1r8vgbVP6n3EwsVl8K7tnFqXbKkk0q18OzR-dGXqqQFCffxXGL1PcfYrJphor4-_AWBii8z_qEKtMF0br2Qjsldt4g1TmqwQFggGfenOPmQVvNU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=hTfDp_W3Qa--rmRTY5hUPsEqYi0632tXR0DNmRz4hEVZcH-BsPUMi5m0satUgTJu8agFfe_FjxYc2NxWLLXTbG7ddPg4TMwxMZ-OaTBtEdsUxoT884FQqfzwlRpZWMNZZmHmvXZUEpb9ykLb9Gu-N3IFiH-_5GfEdnQdPHXTUaoSO5OaHCbishizOMaT1oZ9_eCwrxJJLcoRhJ5pO-E_y5pNg0kJsAsX3VBDX6t9QRyPtN-jIULsx7SiFLB7LIw9LrGNm-JYe6YSLoQoz0FqmQrSYBvqhlpyxfJpeYYK5NQ5R822CtidJheFTBrzk6rDu-teCWjKukRgtKX5knvXvXVoYiqY9nTVpzEQqCiHeC_jwIuv5iiRTF7P4dunYfuXsTVNGdQujlQL3MvEMRukirn238SlZULPoBP466JMCwYY6XaDOy4SdVjJqr_2RhI-4l6EvfHzRWlqb-3J2kLbBssy0L22mCY6PTxX64Z5IQ-FZL7syZbW_GN6JaByBm1dDArvlX_ErfFJiVXtKTcFMBzuC_5DQh-03wS_HRcs2IKpF4G6vud7MhisQ_1s1r8vgbVP6n3EwsVl8K7tnFqXbKkk0q18OzR-dGXqqQFCffxXGL1PcfYrJphor4-_AWBii8z_qEKtMF0br2Qjsldt4g1TmqwQFggGfenOPmQVvNU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇪🇸
مشکل ایمنی ورزشگاه‌ها به لالیگا هم رسیده‌ و تیم رایووایه‌کانو نمیتونه از استادیوم خانگی خودش در فصل‌آینده استفاده کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102408" target="_blank">📅 12:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102407">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a01fbf75.mp4?token=XzEt7Y7hISi-cDjUUgKb6k75w9H0-AfgB5Ey-Khfky_R8TkncnLhZF_3ygZuwHZBfu7IRemZV1gniDuGFpuMDhNh84gqwTbo7Ga_DxOc6mc0LemHlxDmFTIWqiy1WPxXHsjOAMsj28qEKe4PkHxkguKS3G5NqzXdzrWdqZ5zehqUDEkXa-jEM_qPUYoohFI591QM_P2qkvyekEpv5gqbY_Nqt4SSQYHok2OXgtIFETF7LlIZlWZX5YoPytcH2XZfrzMYedfVoHk2F-xdDyQTScytQZY2HQeMztPAoE6qQU46EyBLrphxONzDqRlqTaztfaONTigENqK_JWH9Gv-stg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a01fbf75.mp4?token=XzEt7Y7hISi-cDjUUgKb6k75w9H0-AfgB5Ey-Khfky_R8TkncnLhZF_3ygZuwHZBfu7IRemZV1gniDuGFpuMDhNh84gqwTbo7Ga_DxOc6mc0LemHlxDmFTIWqiy1WPxXHsjOAMsj28qEKe4PkHxkguKS3G5NqzXdzrWdqZ5zehqUDEkXa-jEM_qPUYoohFI591QM_P2qkvyekEpv5gqbY_Nqt4SSQYHok2OXgtIFETF7LlIZlWZX5YoPytcH2XZfrzMYedfVoHk2F-xdDyQTScytQZY2HQeMztPAoE6qQU46EyBLrphxONzDqRlqTaztfaONTigENqK_JWH9Gv-stg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو وایرال شده از صحبت‌های تلخ و بامزه یک ایرانی حین ورود به‌تونلی در بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102407" target="_blank">📅 11:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102406">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262957043c.mp4?token=n0_YmwG4LIqx_NN_zOTqfcuSU-qvKHy_3Ti_VGOnH0uvu-LNjTLrjypURbmEK4ebHvQT148GAd-ibqtXyq_FFdGPnLWSX1ct3gUVrKRy_TcHNqeGnSaMLzvM0kI_kYRyisbCEVrMf6qOFtXXXeK5PkFJ0qGHfGlNQClWUZwFoJPVPey05SOZ9Epnbg8rxrRQ8PP037U9nKW3yiyor2aPuMOyGrdXv7mQ-ovO0zDvjlZaC8k1kMJDDwOZfjDxsD9dBl39AGnZpM9pE5V8wNyY4DEStJPxW8OCcbfJfVYoV5slVbvwGSg-Mm3vSEUW3QXnzBPehNE8oqISUllAtKTNgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262957043c.mp4?token=n0_YmwG4LIqx_NN_zOTqfcuSU-qvKHy_3Ti_VGOnH0uvu-LNjTLrjypURbmEK4ebHvQT148GAd-ibqtXyq_FFdGPnLWSX1ct3gUVrKRy_TcHNqeGnSaMLzvM0kI_kYRyisbCEVrMf6qOFtXXXeK5PkFJ0qGHfGlNQClWUZwFoJPVPey05SOZ9Epnbg8rxrRQ8PP037U9nKW3yiyor2aPuMOyGrdXv7mQ-ovO0zDvjlZaC8k1kMJDDwOZfjDxsD9dBl39AGnZpM9pE5V8wNyY4DEStJPxW8OCcbfJfVYoV5slVbvwGSg-Mm3vSEUW3QXnzBPehNE8oqISUllAtKTNgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپرایز خاص‌ ژابی‌آلونسو برای فصل‌آینده؛ رونمایی از ستاره ۱۷ ساله قزاقستانی چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102406" target="_blank">📅 11:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102405">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2180d890.mp4?token=UnPIE_XkIgYljwrt_Qj6FsE0FaCB4AWzN2ZlSZYRSDiKTvKJKOXYE2_JJPLctjZOXqornLZayscHCJgehbsjurnCZIepvwfHdO6cf2TMpiSwgvx5GitND_U6hQU8Ztf34ML0fnW8sdAsiF4GB7g_eqfPdpaZXZ7ZasummX7hRwmbu_okuTBDQUdE4DeoJ0OP-RizUtn39Ez2GI_trdR3qRK8La_k55ZamIcUaNxoI4DqkV9wQbuNim5T1oIB2-_XzUIRuizEwG6DqJq9zUDYulgPyUnUF5FAPoOLT82XuyRcju_2jlkrvW9w4MyAGIKO2rJrsdWQONr89MM_AckU-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2180d890.mp4?token=UnPIE_XkIgYljwrt_Qj6FsE0FaCB4AWzN2ZlSZYRSDiKTvKJKOXYE2_JJPLctjZOXqornLZayscHCJgehbsjurnCZIepvwfHdO6cf2TMpiSwgvx5GitND_U6hQU8Ztf34ML0fnW8sdAsiF4GB7g_eqfPdpaZXZ7ZasummX7hRwmbu_okuTBDQUdE4DeoJ0OP-RizUtn39Ez2GI_trdR3qRK8La_k55ZamIcUaNxoI4DqkV9wQbuNim5T1oIB2-_XzUIRuizEwG6DqJq9zUDYulgPyUnUF5FAPoOLT82XuyRcju_2jlkrvW9w4MyAGIKO2rJrsdWQONr89MM_AckU-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
آماده‌سازی استادیوم نیوکمپ برای فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102405" target="_blank">📅 11:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102404">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31c9897d6.mp4?token=kAXXN6j-M9Cn94WEzXUS-LoPZO-XiGqjlUU9sA1cod_29-_TBINZjjVCgaTq8hfe7dWPwB8QFybty2XMqFSYG3qIuYFLHllkM3US3FRlBlXUGUI6FWBEjLmLMr74Lj2ftAVMXREqrkmQT9AvA8IriRNdANpJk5I1gGaRmmtzqpp_oRTYsOiQP6ah2hC-mVyZSYmCwc5SVSo9R9SgOvDlYSvB_Hq39WMuZUehBM2UcRKkMF5s9fcwxFy31A4KbX74azjKGwsPTnecrt2yJkwFEzwCydKSh4tPgGTNZG_aIkBODTnblNblDZk-kqqrxbmJoP5wPcI-tIZbRrzBD9hLgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31c9897d6.mp4?token=kAXXN6j-M9Cn94WEzXUS-LoPZO-XiGqjlUU9sA1cod_29-_TBINZjjVCgaTq8hfe7dWPwB8QFybty2XMqFSYG3qIuYFLHllkM3US3FRlBlXUGUI6FWBEjLmLMr74Lj2ftAVMXREqrkmQT9AvA8IriRNdANpJk5I1gGaRmmtzqpp_oRTYsOiQP6ah2hC-mVyZSYmCwc5SVSo9R9SgOvDlYSvB_Hq39WMuZUehBM2UcRKkMF5s9fcwxFy31A4KbX74azjKGwsPTnecrt2yJkwFEzwCydKSh4tPgGTNZG_aIkBODTnblNblDZk-kqqrxbmJoP5wPcI-tIZbRrzBD9hLgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
پاسخ‌تند و کنایه‌آمیز مهدی‌رحمتی به صحبت اخیر معدی‌قایدی: بذارید تو‌ توهم خودش بمونه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102404" target="_blank">📅 10:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102403">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
✅
کیت‌دوم فصل‌آینده منچسترسیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102403" target="_blank">📅 10:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102402">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/869e38d1a5.mp4?token=TJEOIp7dNRPZgckON6clqMBnqc4fs22cZ0n47l0IcMTAY8iuL0RLCsZD8qEoMjGd3zcvhhQWELnDcqww_HgvENDG4yEodMR_wyiD3WTVdX-IIZiTwsEQt2iKhlwUdgqRuUVbSqKfAN6Ejh6vfVYXbzz5fyRuby7Mimqu1pY4NP7Nz5aNSM5nCRsexxUzNqrj-rZA3Ha384ZFtfGRmxuO_OAeaoZ95pjRbS1y1K8RHmigfPToslndIHTSE4kE9SdusaccrWnr5h94cBQaex2H924JrvBrvg9A8p3f5U0yZsS_AnZBpQvPqPB-kxzoan8d4CDAf8E4sg-dYTUmrGOaDoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/869e38d1a5.mp4?token=TJEOIp7dNRPZgckON6clqMBnqc4fs22cZ0n47l0IcMTAY8iuL0RLCsZD8qEoMjGd3zcvhhQWELnDcqww_HgvENDG4yEodMR_wyiD3WTVdX-IIZiTwsEQt2iKhlwUdgqRuUVbSqKfAN6Ejh6vfVYXbzz5fyRuby7Mimqu1pY4NP7Nz5aNSM5nCRsexxUzNqrj-rZA3Ha384ZFtfGRmxuO_OAeaoZ95pjRbS1y1K8RHmigfPToslndIHTSE4kE9SdusaccrWnr5h94cBQaex2H924JrvBrvg9A8p3f5U0yZsS_AnZBpQvPqPB-kxzoan8d4CDAf8E4sg-dYTUmrGOaDoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
درگیری شدید فیل‌فودن ستاره سیتی به همراه مادرش با چنتا از مردم در یکی از کلاب‌های شهر منچستر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102402" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102401">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0266060c.mp4?token=gdYFGpOuizG6BBVJl2i7Ede6zT0kETkZURJBZKI3KkOcr-tTYzz5EnrLSb7Kmp2ZIxiZm5qSkJ9CBdx9O0IZK7AF7mXSkK-8MXqEhjOvn5tPngrQkS66z1GXlzgYEzoeWxv8MEndnE67-33IMIC_EXGgyYlNPuJCigQrKQgVTIgH3tQrnXJDY-_5w04KKUU7dxhzDA1FOYAZEhSPYgn1942V3uzznIg2KnzzEwJ65tvJGaAqrR1mO0nPjwxzfD5ADZ7TPfIaWFpmfE_Xz6OI3qNDORqNUcG4vPHDWzkB805Hb96HjgdgyJNNittHSsFR5VEbjKgLmUQJerYTdVv4XAHaZE9m61lGXY0sa-gAKAx_kC4wpFqfdcxrUxLveQ2eYsVSOYCo51ZCf4v-9HNy50hY6eL12OKegDQD1DJ3Lycbch0tKNLovxaqi_aQKxyfd8A8-KYo-kkd9-DpLDJe5Ua1pgYxyfBaleOsCa0Wr8m0PXqhiGHlHQahuwIhrzWi9SFzJUpLgnHkroOA4_I3yoiFiBe8RKORhLb4CQyOJfpjGuddxaLKPIonCZPnZuEKM4LMfYoDTxpt1kXT566-TgFFxcGvOq-qBOVJuMwK4mVl1BIkO8NZzbhpHVi4JSs4XCYE_Nq0KkHbyP6fpTgpAPWcUE8gSoHzCbMs16uC-Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0266060c.mp4?token=gdYFGpOuizG6BBVJl2i7Ede6zT0kETkZURJBZKI3KkOcr-tTYzz5EnrLSb7Kmp2ZIxiZm5qSkJ9CBdx9O0IZK7AF7mXSkK-8MXqEhjOvn5tPngrQkS66z1GXlzgYEzoeWxv8MEndnE67-33IMIC_EXGgyYlNPuJCigQrKQgVTIgH3tQrnXJDY-_5w04KKUU7dxhzDA1FOYAZEhSPYgn1942V3uzznIg2KnzzEwJ65tvJGaAqrR1mO0nPjwxzfD5ADZ7TPfIaWFpmfE_Xz6OI3qNDORqNUcG4vPHDWzkB805Hb96HjgdgyJNNittHSsFR5VEbjKgLmUQJerYTdVv4XAHaZE9m61lGXY0sa-gAKAx_kC4wpFqfdcxrUxLveQ2eYsVSOYCo51ZCf4v-9HNy50hY6eL12OKegDQD1DJ3Lycbch0tKNLovxaqi_aQKxyfd8A8-KYo-kkd9-DpLDJe5Ua1pgYxyfBaleOsCa0Wr8m0PXqhiGHlHQahuwIhrzWi9SFzJUpLgnHkroOA4_I3yoiFiBe8RKORhLb4CQyOJfpjGuddxaLKPIonCZPnZuEKM4LMfYoDTxpt1kXT566-TgFFxcGvOq-qBOVJuMwK4mVl1BIkO8NZzbhpHVi4JSs4XCYE_Nq0KkHbyP6fpTgpAPWcUE8gSoHzCbMs16uC-Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁳󠁣󠁴󠁿
نظر سرالکس فرگوسن درباره‌مثلث جادویی بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102401" target="_blank">📅 10:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102400">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f864b5c9ce.mp4?token=B6W5t3S2VEtqdc5MEMtbv8WhiYmbV4Xc7xYk1XetNqGKSlLmoGUY_UcswifJKZ2h180eU_8Zcs8XDizioIJdjfW8UmBP_VzwUiMjrVSTd5e-HPF2iLgOvIP0Rc1ART1GFUDoXC9vF4JF5FYv0AJJGVeIobR9iVe7ehUOulvUuThamYa3XIy3DW6HPDYTPgqyxwclly5G2QvelDENbQsTV2iELS5kMcHmTz_A6k9JnGEFPdIj3-13TLRBlg25O47SukgU3Ei0o_Kw7C4DORumSYEYY443xBIzHiyYm0UH-LE6jMzwiJQKJ1njYIg8QmmvjZTAdAZ6FF5Zl7LPM7bIfh96WUfWhFRKu-6l55UIU1gbSEYZTw9fF5jToIHYxM702D_NEI9AzO0JoAZ9Ao8BZe6b619fWbH33vwKS6OYtAYVNGL107BjnIG8wE4GrVb0DbVomoSzE2J_3fMxZ7rtIfq4f73N1ueegcMPeUA8zKbgRpR9OqVHE_IKQZyP-G2HUA_hdfvWIaDvfyyYxvnsm8tO4V1wt-_lRpglvHFx-PNV91c53wjfWDrnbJkjXXboN9GVkLp4fba2-Td_IJiRWGIxIqasZY_Ia6sbjS8MHqVzwGUIPRZNUyc3uYWBdiSnruAjQLuxfZETKBg5J5mXPspnNFQGuhdIsmNrL0rNhXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f864b5c9ce.mp4?token=B6W5t3S2VEtqdc5MEMtbv8WhiYmbV4Xc7xYk1XetNqGKSlLmoGUY_UcswifJKZ2h180eU_8Zcs8XDizioIJdjfW8UmBP_VzwUiMjrVSTd5e-HPF2iLgOvIP0Rc1ART1GFUDoXC9vF4JF5FYv0AJJGVeIobR9iVe7ehUOulvUuThamYa3XIy3DW6HPDYTPgqyxwclly5G2QvelDENbQsTV2iELS5kMcHmTz_A6k9JnGEFPdIj3-13TLRBlg25O47SukgU3Ei0o_Kw7C4DORumSYEYY443xBIzHiyYm0UH-LE6jMzwiJQKJ1njYIg8QmmvjZTAdAZ6FF5Zl7LPM7bIfh96WUfWhFRKu-6l55UIU1gbSEYZTw9fF5jToIHYxM702D_NEI9AzO0JoAZ9Ao8BZe6b619fWbH33vwKS6OYtAYVNGL107BjnIG8wE4GrVb0DbVomoSzE2J_3fMxZ7rtIfq4f73N1ueegcMPeUA8zKbgRpR9OqVHE_IKQZyP-G2HUA_hdfvWIaDvfyyYxvnsm8tO4V1wt-_lRpglvHFx-PNV91c53wjfWDrnbJkjXXboN9GVkLp4fba2-Td_IJiRWGIxIqasZY_Ia6sbjS8MHqVzwGUIPRZNUyc3uYWBdiSnruAjQLuxfZETKBg5J5mXPspnNFQGuhdIsmNrL0rNhXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
شباهت حرکت‌های یامال و اولیسه
🔥
😮‍💨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102400" target="_blank">📅 09:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102399">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5630cebcb5.mp4?token=BjjyH5byYJu7parSGbVxgEYPG96Rz6B8P2rOojU0bJN4w6BDsfKJbRil-93fHSqfF09fbh5UNJSV-nLDLjP8nS5RhtbM1Gpw-Ss-9JpnmzDZ19wl-XDquTncj2_G0oWLDaJBd-yMEUpFvZTadHMgZPnxDrfRSc6yAOrvy7hI4MZnB4hil_0V4cvKTIwDMsIhLwXDioBaHkWyZacB3pn57A3XhgYYSzKUMxTxOTHCPDdkQ_zoWm9iEO0mrEgHZgv2zXUVMR65SdRurhpG0FqJfnnzXGwhr_k4mdKvbxVn_1MfYdN_QQc0cLEJXetjkXqbj5pd754ge6Jzs2ZiFBicYS47wJmCSpnBq4wQpCvbQ-Hz48Nqk-71y-6YtxicpuIfv2n_hE-qRNgoy8naPJOcuMfE5LAuKLEj4zu9x97KVojIvHAH6IbRaI2ARVAP3oTwwsodq9YaiwWPi8aI_fcgt0FLnSd9TR2S9hl5Jw4hP5rfnSN5LTaGb1muhTdJOwu1tmEQEdz9D0TsfZk5kdrkryJhvEETEe6C0j6KO6ZY_A0aQgTAZDdu06noc5QX99Ai1lL_FHEcKevVcTn2d-OJhvpDacq3CG49cJhKT-a7SFoX8Hw8qmByIdssf0zMx1_EGmmRXOxvUWoMd1Nh94ULELfR3H2x0Cz_XlZY_2Asx74" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5630cebcb5.mp4?token=BjjyH5byYJu7parSGbVxgEYPG96Rz6B8P2rOojU0bJN4w6BDsfKJbRil-93fHSqfF09fbh5UNJSV-nLDLjP8nS5RhtbM1Gpw-Ss-9JpnmzDZ19wl-XDquTncj2_G0oWLDaJBd-yMEUpFvZTadHMgZPnxDrfRSc6yAOrvy7hI4MZnB4hil_0V4cvKTIwDMsIhLwXDioBaHkWyZacB3pn57A3XhgYYSzKUMxTxOTHCPDdkQ_zoWm9iEO0mrEgHZgv2zXUVMR65SdRurhpG0FqJfnnzXGwhr_k4mdKvbxVn_1MfYdN_QQc0cLEJXetjkXqbj5pd754ge6Jzs2ZiFBicYS47wJmCSpnBq4wQpCvbQ-Hz48Nqk-71y-6YtxicpuIfv2n_hE-qRNgoy8naPJOcuMfE5LAuKLEj4zu9x97KVojIvHAH6IbRaI2ARVAP3oTwwsodq9YaiwWPi8aI_fcgt0FLnSd9TR2S9hl5Jw4hP5rfnSN5LTaGb1muhTdJOwu1tmEQEdz9D0TsfZk5kdrkryJhvEETEe6C0j6KO6ZY_A0aQgTAZDdu06noc5QX99Ai1lL_FHEcKevVcTn2d-OJhvpDacq3CG49cJhKT-a7SFoX8Hw8qmByIdssf0zMx1_EGmmRXOxvUWoMd1Nh94ULELfR3H2x0Cz_XlZY_2Asx74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شیرجه زد، گرفتش، زد زمین، شوتش کرد!⁣ جوک خنده‌دار بیلی مک‌کالاک ماساژور سابق چلسی درباره‌ی پتر چک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102399" target="_blank">📅 09:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102398">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdQ3RlddVlbLA1fFOs7JKQDFmhCYH-24iFze5plAzZCFvYqRmbyIcEsu0ZRENaGVgAsNy2hG6hgzD8CPh1Migv2NJtJu-e9hc2K7MeEngv5EjZ8diakc0CDTRpSj9CQs8BQSKP4IyFloJddqdFiovUUuabHPn7ZNT9cZnCn7BcsRFuWR5KhUDloMv8kbOcBZ-3xfoPyMag0GVsbRCz4IkOMlZb6jPM0zwLnUWe_unQ0ADEVQI92UwZ8Ekoys_zAL9jcVk1_b2hvLD6TWJXO3unyNilDo-5AdoxSeuV_nmC3BiGJLTMhHfpkBDdhHBpejCP-yuyd2YkPt-UMXfnEXhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
🇮🇹
لحظاتی پیش، فرانکو بارسی، اسطوره فوتبال ایتالیا، در سن ۶۶ سالگی درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102398" target="_blank">📅 09:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102397">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d54a6dc02d.mp4?token=HWLs2z-0em0Lz9bsh_0GzwEMr3rH9S2sbcwaHDuJNaAZmFqu-LdUkwNUaNJDZYOv-1rq-bdW6oKX3DdgfajBYLDkl3wEAh4vWKsZlv6ksR6GACAPFtbamNDq2jG8UsiNkpEkh7Nmcp1KwZNfaJc1IjcDeTTt9ktQ4K7QTszAft3wkSM6jACFVAHVOWlZe4goRhdsmmc8nhqAJZAWF-zV1wNIGqpMnihs-63CmdKkB1wAWJLLPzJIujXMuDRtA3IfGZxkpTzpHL8stDMZohtBqj9R053i6lUm6wpmPn9pznBH91C7-EI62xeERsrM92hp4QLeJ1a10WW9uWEsRxnbVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d54a6dc02d.mp4?token=HWLs2z-0em0Lz9bsh_0GzwEMr3rH9S2sbcwaHDuJNaAZmFqu-LdUkwNUaNJDZYOv-1rq-bdW6oKX3DdgfajBYLDkl3wEAh4vWKsZlv6ksR6GACAPFtbamNDq2jG8UsiNkpEkh7Nmcp1KwZNfaJc1IjcDeTTt9ktQ4K7QTszAft3wkSM6jACFVAHVOWlZe4goRhdsmmc8nhqAJZAWF-zV1wNIGqpMnihs-63CmdKkB1wAWJLLPzJIujXMuDRtA3IfGZxkpTzpHL8stDMZohtBqj9R053i6lUm6wpmPn9pznBH91C7-EI62xeERsrM92hp4QLeJ1a10WW9uWEsRxnbVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت فوتبالیا اوایل هر فصل
🤧
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102397" target="_blank">📅 09:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102396">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e396ec62ed.mp4?token=JWRdfWnQ81g_oh2M0i2QyAwsNJ_IZ9IuzB_s5oL2oUIKwqVEmdVTjx4pZ3sKaNl2uHDcCZQnHiucWlgP5lHY1Ik3AfptC91bbotZzUWAjkI9vdOI-mldaQ_3BIUpRW2N7Gh4t1c4WPhD2njiPZEygPY59XWyyH-zIf6cSLZP2glszTalqFMHUY1bjYPu1LD6bGMSiPOaRG9yg0xDdLYO2l-gI4Iy4O9GZ9FduCo5DgdwmT22CKvvONdMu0wcm1twR_PT7c_vhh-j-0R7KViWJ96DOls9RMzdow0yqYmlJ1dm48HbMk7rt6_O4Q2WpGkUN4YsYHbzu_KYdPU27UsksA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e396ec62ed.mp4?token=JWRdfWnQ81g_oh2M0i2QyAwsNJ_IZ9IuzB_s5oL2oUIKwqVEmdVTjx4pZ3sKaNl2uHDcCZQnHiucWlgP5lHY1Ik3AfptC91bbotZzUWAjkI9vdOI-mldaQ_3BIUpRW2N7Gh4t1c4WPhD2njiPZEygPY59XWyyH-zIf6cSLZP2glszTalqFMHUY1bjYPu1LD6bGMSiPOaRG9yg0xDdLYO2l-gI4Iy4O9GZ9FduCo5DgdwmT22CKvvONdMu0wcm1twR_PT7c_vhh-j-0R7KViWJ96DOls9RMzdow0yqYmlJ1dm48HbMk7rt6_O4Q2WpGkUN4YsYHbzu_KYdPU27UsksA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
نظر پرز وقتی مورینیو میگه وینیسیوس رو بدیم به تیم‌های دیگه تو این پنجره نقل و انتقالاتی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102396" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102395">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-1Khjgjg-PueJXu7XOCMerS97B7L9wKWOIdF88IodeDBBPgw1pfLz3OnuJ4TfwxF9_bFgqoq7GrlKa45BrC6UXXYyBv-I80r_JeY6dKOpwGXTSBS3WFwMADjOLsXdn4G8V9A8taKCxLNnifrcZnnjMmwCPCfTFkGgoh7y6-eT343vuOqqgH00m9l9Nw163BqP7ZfkZm6ELZXEFD19FpDa7jg9sg_tKZzHSnf26f-ozaBphbRrtyGc-tjKgtgl5ZNS2Yx9wPzHGHTc1SNxyw0CcAouX3JlFEfAr7Z2ojCvEPZpgOgBZ6scsVC68_qqvAb2bATT4LkXxfKB5XODOFHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
رومانو: حاضرم قسم‌بخورم که دیومانده بازیکن رئال‌مادرید شده و فقط تا وقتی لایپزیگ بازیکن جدیدی نگیره قراره رونمایی رسمی انجام نشه. اگر این اتفاق نیفتاده باشه از حرفه‌ خبرنگاری خودم کنار میرم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/102395" target="_blank">📅 03:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102394">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIyXc34ZzWlRpID-eQ89klcQZP7bDN7aew-pefVMF36Fu_94Wfxr0dkfUxJLD_E4WpNkRk3PcmZRJRLHzHRRS48pHWOSFkp2Ycr8gEgFCdJrCR_lRhvQWjl0EKBWKbFEPCUJV0y-6JLzCDj8eaC73RwhLOS1QEIhkrfg05VtXzlDVi-4rBlydX7imURSkcNFF_zxVDSM6ThvyvX9UuSiOy4XcU1AgtbYd1V07oyUBmP4esaKMkT-Fc5OzNq2uYCah0CY2HZjPLqO-sXZxD8Tcw1R_X2BPZ7x4yPqfJ8z2T6pQGFpt-sWu7FcoL1M94L_ESTh7z88YfViReI52Iynug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کاسمیرو:
خوشحالم که اینجا هستم و به لئو مسی کمک میکنم، او پادشاه فوتبال است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/102394" target="_blank">📅 03:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102390">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l_5ZYbDxtFq-FgkPfKZkz9tx9XU3Tg4eLNFE-1wcUUGM-cKUjlVXx7knjyIiELGVN8GP273fWhlEKWOe9sHgmgkj7tA7iI7v6i3pUJ-0EMigh96cUMTg6gymIuvwek_jv0iT7pfrDo0rX0B-aoYsh6npA8jc7DjfmUoZ3ghbounIZ0bDRXsA1WsTaRYobtpWo-frgF5JXo4t3mBsPOQh0CrunrHoiHsJeVQ9pWeLcEKP47zLAmhVqwZ-WMEm_cAcrVRjeycinYXAXYV3DqWuA-PTc-IgFcFsxFJbOpiElqv1PsIFC9KQ8tnRIVC3m1EO82_vIXeeNzhcGjFNA-OVpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mc23HRjfUiEsvD_dEO_CCnTBOu93zqsHGd9LOa_5l0l-6EF9muSOfewN9Yg02ga8GMKNGiWTYkFeO_JHe4YTwy5a0tltQJCVT7M2jrIQFPXx9jeP9Vnqp87X6WM7JZDKuagKiBAhTFKAIAxk-odSDeLOK3UerecuXpo5Q6hFt38mPiUhdEOn-0qhPy4cTqOM8GLerTLADn_4IaKFAY4vvu4BqM5l4Ka5y60-qbSGwqgILMAQ4MOcjji6xIdkOz8cSS_RTXDD3Lu4em--9RW_6f3bMldMK0SDK6ho-yTi6kiBqJHYGU4i7CBRN1g1RdDRlMrZYdktPNUCgwFUqRupmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sg8XoHuyl9mYfuOBvui2inDXfBDc2LTgQ_9JiDTDlz3cU3lidC9gcvhZLK-12Ls5lYRoiF3fkXH7SEJmR9z-Ko_Ra8pzpp2HDvoEeQfPhe1MnQyEgXwjNT8uFm0DaqauJacrm4e4C5uQJb4zFwAkHKoAW-OnLO4LJtgPbdNu4bpff94YSmep5kaoUG5cRaI-mtQnTCdeeMSoQKmYTQj669xmxxA0MgofaBqKclUnWTBpOFLMUJ-pP6hKRJLFfr7C5MbVuq2xfiCiL9IjU6fecNL9F3S0UOVzbJk656nhOABKcCrfPxgzOtijOdCAJybDPVTzNpCwyzvEtJi7xtCblg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LRxE8tYPv3aioXTv0Nfpz-hSUOTXjTT0g2P465OOEb1QY2ad7y0CbSOfCU0oZgs0sEm_fAjpUzW40isVBv7t8URPISglIG7fB1IXXXQiweatY1iUZ__EBRyhXu0nwPOg9ZcqRHNpLr0kW-5yU_yWAI1U_Em2m_b9cdMojqqtlpjeiQsgWHg3W0WMLXSIQWNQUl8y9yrjztzbvzNSmYBNPfgDV1SwUrab8cSFNkTYuw3z__rEhd1tg-nQQALBwX_149NZXb7GaNrl2BHGs0tn57038AaWJ9bUsgEVpZwfLqlzW3K2fYslsRqtnG_1xcO28SbFdmdkzfWct6s7TeX5mA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریس و جونیور و جورجینا رفتن عشق و حال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/102390" target="_blank">📅 00:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102389">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/511459b235.mp4?token=BpZGaIWpLHDTKRC6pQkzw_O81aPZlDfCTGwr1TaVS2pASv_DSsX0Q6DWoHo3qazV-VuPSGgcEziDYtw2EUuvsvBy_MCyj-_hxYM3A8TVUgYZJnP0L9x0jhBgnBtXlCqRyeoRkA2f8Zx0MyAwYG19wC8LQDUnvFtv09hDnv6VdBWgOtRuh-l4QCpUm_m1-8yCLwI0F3Qt3ZKKx1_0lOM8AExao3C_PBFwtd_3cfMQdS9kTm2wOoj5_niZd3Qt11W222YyzzMOMRphefMenOlaGdj66sO90CbRzLzz_mvtC0-JNkd1NHw3qvR9sOjG5XGbcxa2qSzkdLzWfXiqHhAdUB6Qu3dIIO0seUhOm1qtK_0ti6PCFgVGpLQkzIVCVUpptW3LW_73fLXvE5S6LTv2WBkTqYvgf3B3-VccWdBwvwZBbFx5tBN-kqh22Jfm7uYbw23TkDWQxQPmnXe5A3LrwyB7xgXBbVa3Rtl-81sEOSWe6cQ-FA5EPPWUc1MJ67Aal4PXeTqoF2KR1hGuf7t3EDJdynJ9kI53XLcA4vsEZlKVNPly7pObyuOvjtMpRRc_9m5D8xVeQIp3TNKWIA8hu_nw0sYsWDs-NLWw8rBZ4RzcXBbDHR-_y7NBlYNeVedkAJNyZf3iAGqFp9Wc9hvQKa5AWMBiOd7_Zn1LctJCxqY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/511459b235.mp4?token=BpZGaIWpLHDTKRC6pQkzw_O81aPZlDfCTGwr1TaVS2pASv_DSsX0Q6DWoHo3qazV-VuPSGgcEziDYtw2EUuvsvBy_MCyj-_hxYM3A8TVUgYZJnP0L9x0jhBgnBtXlCqRyeoRkA2f8Zx0MyAwYG19wC8LQDUnvFtv09hDnv6VdBWgOtRuh-l4QCpUm_m1-8yCLwI0F3Qt3ZKKx1_0lOM8AExao3C_PBFwtd_3cfMQdS9kTm2wOoj5_niZd3Qt11W222YyzzMOMRphefMenOlaGdj66sO90CbRzLzz_mvtC0-JNkd1NHw3qvR9sOjG5XGbcxa2qSzkdLzWfXiqHhAdUB6Qu3dIIO0seUhOm1qtK_0ti6PCFgVGpLQkzIVCVUpptW3LW_73fLXvE5S6LTv2WBkTqYvgf3B3-VccWdBwvwZBbFx5tBN-kqh22Jfm7uYbw23TkDWQxQPmnXe5A3LrwyB7xgXBbVa3Rtl-81sEOSWe6cQ-FA5EPPWUc1MJ67Aal4PXeTqoF2KR1hGuf7t3EDJdynJ9kI53XLcA4vsEZlKVNPly7pObyuOvjtMpRRc_9m5D8xVeQIp3TNKWIA8hu_nw0sYsWDs-NLWw8rBZ4RzcXBbDHR-_y7NBlYNeVedkAJNyZf3iAGqFp9Wc9hvQKa5AWMBiOd7_Zn1LctJCxqY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل فردوسی‌پور بعد از کلیپ دست‌بوسی که ازش منتشر شد یه کلیپ گرفته و میگه ویدیوهایی از گذشته من رو گزینشی منتشر کردن. هجمه عجیبی علیه من اومده! من اگه قرار بود چاپلوسی کنم الان تو صداوسیما کار میکردم و نَود رو داشتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/102389" target="_blank">📅 00:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102388">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjV08dJh_PrF0kS0wvc0DFd1HCSp3WSgyRnGC3EhuS9VXPGg_yFBESziTwumMRxgbmg6QKz-p7pxeuoSf6Ze-Bq0gbEcuKkVMzrFoZJFHLp0Q9WsutFmp3CD5WnPynUkbcEGIdX7aPxLY_aR-xj9SVj3zW9eUgHFIBp8h1-_tnjiBtm-piRZVmhAUXqCrJDYd3NpstwAjfFJuYGEF1vzCV4TPP4Pzq6GqJTLmSDnwqvR1MhVMdVPW8ffB5kHOg4EjdqTmFnqrNJdn865wQBtyfXx_sdoqgAS0VSCAzK24QskRpgDbsaSNR6zI1u61OZeg0EIDRrUMf2zlXxYwMwn8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری: کارلوس اسپی شده با بند فسخ به مبلغ 25 میلیون یورو به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/102388" target="_blank">📅 00:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102387">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKgKx58LQSDS-8EdKN6yJfvGG8B4TqRHEtqUdo3Y0aE0dNkvk2mal3kkrqz4nj9vmACfEOEJqEAeip_D4piPwFitzHJ-VbkEuJoKmTgBD4TG1iiQ25itwrPzOeJnBPtz_Q_pJQhrVA3V8yucXqZdxTQEshufNDPaXrdbXNTuyWIzXs8WztdadcbjOmQZ0VBtRNjNf4dOLm2IKDx-PMUnRjGyot4qr042WdJJvCLNxD9OVujvCPCrubFOrNluwFhyQEJZLz9fHkkx8TafKi6vYTuw9rw4sc4WYWV2-IOx-Dj3uDtG3cR74O2Iyue5jLBahnjvv9SIx-35ZRllxKIQAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری بلینگهام که رو دستای زیدش خوابش برده.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/102387" target="_blank">📅 23:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102386">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae65f1051a.mp4?token=rtu2UK-p-H5GmBCR91_sAu52f8sISk7OQdpgxnNpeSfIEeAfP1hNNmabFre1ueFgk85_5cjADuhuxK5XyFltLEmix_aSX81AcgMBbJ9XFH7SFmTZY8cHwR_m9sa4IUjEWDyFVe7usVaA6eRmzVYCYnQNGhfRkrJWmEmcaczOvDFIwW5NCZR9QxvxuW9EZb6uCsDCeA238zllx6pCgTvBOM7Gkb68Um2hD1ZMNC0xmzK8esCxpM1Ck6vKEPJEihQTOiONNmuVd0TePGmveMXdGeMZyBP1rVaz2alJHenlHHT1wRs8b45qtyG-Sb0zTO8Gi3kB7OaL0c7UaYUukkyCnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae65f1051a.mp4?token=rtu2UK-p-H5GmBCR91_sAu52f8sISk7OQdpgxnNpeSfIEeAfP1hNNmabFre1ueFgk85_5cjADuhuxK5XyFltLEmix_aSX81AcgMBbJ9XFH7SFmTZY8cHwR_m9sa4IUjEWDyFVe7usVaA6eRmzVYCYnQNGhfRkrJWmEmcaczOvDFIwW5NCZR9QxvxuW9EZb6uCsDCeA238zllx6pCgTvBOM7Gkb68Um2hD1ZMNC0xmzK8esCxpM1Ck6vKEPJEihQTOiONNmuVd0TePGmveMXdGeMZyBP1rVaz2alJHenlHHT1wRs8b45qtyG-Sb0zTO8Gi3kB7OaL0c7UaYUukkyCnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
روایتی جالب از تمرین‌های پاری‌سن‌ژرمن؛ جایی که حتی امباپه هم از دقت باورنکردنی مسی شگفت‌زده شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102386" target="_blank">📅 23:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102385">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxiB2I_34EiOZRKIwRzlJ4i6VyPYjKlSpDSyjs2DKBE-1-rIv0H_tiJ67kWfl4BemIWhwv21-9Jx4eSzeJu8d4hgy4f1x7cNEZPpFVmRGeX-n9dXGcrF55yHJwg0rrplBY3KmdZINd2--B8CaS3wg1dOqHzvLckSSlJ76vJuwSHF3L8CxlJKqTpWiIgFDSizBbEhQTbi8pl_w-JmkER1mb9_NkH0Pw_Lv_fKh3_EUnDVdheEPTglHUS-r0V62xFfEl_l6yGmLToUv7pCXGXL3sZe0QYN0NYd6_oxe1ceaB_KVYFJuaQHu96OIWhhckX9Sagjq2PoRPb26WqH9fj_uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اولی هوینس:
ما حتی به امپراطور چین هم اولیسه رو نمی‌فروشیم چه برسه به رئال مادرید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102385" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102384">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-QFi-tcsbi3G8zj7VM36WuZM_I1YCuZHk0L9H-tq6gtaNT6k24VQwyQHJ4-MKR7Lxy_--gT-MLS3pyznJ4NnusUG1BmXy-1VvhjyJKt-dmyBqmKLpdHar3BTMe90ZsQK3l_nQRP2OHyUfVxI2ecZzdT0ICrrqX1sQe8f2I7oOzQEGfyDqHqal6NNGi6G00stgpHCyfIofkGLFHKt_QeD9rUf3pH-GnusKz72V4KcAkjVROXaF314sfP1Qa1PuAgUlam6Ufrn1axI_7ncdOiW9vjhrrQEbeGaXqUdrEytCu41kpyXmlj00jj_MsMtW9JfLdPAvS0dOXi6cmBsWyJyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
رئال تو این تابستون شاهکار کرده و همه اینارو فروخته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102384" target="_blank">📅 22:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102382">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d31IeURkLwAe9RTRvxJ5Ssqa7n83NYmYoPEf62GJnOpZMBc4Pw4NmD8mPpHDnMTz-7GzrMb0cK8CWJdBb4Hcx-gr2jPFEABHBppexY0Pi_NMqzN-lPfs771RmfGxMK_CkObjitZDmjiem02wgTpSNWCMweDDIxX2Mb5_3hLmt1SJFy2IZj9s7Hng7OzrXOGn5hNjM7MXnwQkRkvXtqemkyvmS_bTBtvJSdbrLSADCEgRKieE_bbjX-zmiRDreH1l_xulzi1U8L4BQTJldAuc58INOUuiAFc_6Vt-RwBUERCstYPHeZVMXbNhKdh7dpZ5RzqzQpInSh3GZKdvqbpoQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZXQRs3WQ4K3f6U-RRuE_Utdhzpl5GLWFOuIw1GQRJ_qWJRKJfUTresaGl8HqNiVlnUqyWvTJtdNaawlA8cexPZSve7FuBcle2IY84L_F_EGmKnWPEv_Ijjv2rv_WJDr5hLapWnFtbBKxJ85LJFU760jIvlTDYy_cpL6CMBSXsQfQrNALcw9Dv-AlX_9lu10lKfGJuA3114hzH_c6RrWnjr8JpsHSKtFxpYnNvxaibwDD84KHQpYzuJv90jOdOh6AfEbCpGPvFMLK9HsNxo0Cu9dJwXgSK8FqnGYciGTXG4s0U847g07CkqWBApls--tpkbu-ex9pehb40LwnkZRNoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو در 2003
🆚
رونالدو در 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102382" target="_blank">📅 22:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102381">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-text">▶️
زودتر حرکت کن؛ راحت‌تر زیارت کن
🔹
همه راه‌ها به عشق حسین(ع) ختم می‌شود؛ اما زمان سفر می‌تواند تجربه زیارت را متفاوت کند.
🔹
اگر سفر خود را به روزهای اوج تردد موکول نکنید، هم مسیرتان آرام‌تر خواهد بود، هم زمان انتظار کمتر و هم خدمات بهتر.
🎥
این ویدئو را ببینید و بدانید چرا
«سفر با برنامه»
، بهترین همراه زائران اربعین است.
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102381" target="_blank">📅 22:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102380">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nht6uUP0XrLqlt_8VkF7yWDD78BFU3cwXzqUN-RsaEp9nM2f9-8RRPhbWa7M7OE25CQAZXp1kas1Zu98pwZFp85RrjG1I6UtbIwuN9k73t4NOuwsW9jCQMr_jyajKOuKsEc0WN85FlhgV0QEq6ZmNvVYeRh1-kLtSSknKYrDU1xuFY3Gn8ECkKz4fGh71YyLhYUQKTBSiXL_x6_RRmtq2Zazl2C7kdu2HQPdoQauEJgi7xzJvSwE-FM3BCG5fksHb59LwsoPJrclY6QIzuZZAgDz5HzXs2S8Nb0O1b5s0uAtesyxPo38oJYvWFoSsw8t80bERn7hSovZXZZ0au2nUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری: کارلوس اسپی شده با بند فسخ به مبلغ 25 میلیون یورو به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102380" target="_blank">📅 22:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102379">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJVYFgjwl7roFI13Srz6nj39fAr4noP2xtLjzaii-TtkLh_NZoRs7mdkEbly5Juyb5RbocJ4h7kSO2oEyHQWjSeycxu-jXEo4J2YucnbCH92_pIl_GFrfXC1tMhK--DxMPUdv83mgdHHRhKFWFLP0O5v8HuTHqjdbDAyLzkGQd6Tml0q7UYX77fQ0cPBxC4yhvsVJbHAByn_t75R-DNYxWWX3-ORd_7zGsIFRCvl552t2GiNwE37e-MjUZrM_8eQlDK17ClAZFfHY5LhsKidG1YKv7zNBI0kyn0wu6rESsFHSTzNEfbhqpqUR-NCvGRykWH_DEpZmwg8jRDTvgrXrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییرات وینی تو  فیفا اعمال شد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102379" target="_blank">📅 22:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102378">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfsb1li5efIP0XJ5iayn5sNia0E7fI0uh9daZB7lOcZKQFZSJtVxPiGXcylPsr4T_U1F7A00_DzRfPYyLosFN_v8OYt8hj85xeFCNkLJnGArO1ikMcA73UfZBgrsyhF5-YrmHuu-dYmu45Y3oNVvKrl9Ub8kNCs2VsBKdaZcPF3bGzfw1GA_ItPzIv-c5Qz7wGfVn-fAikkVRgB3ycfQbnZ0wfoIy2IfvVE5tZ0m9YCewTPpyghLzEOzYz6VOXOOQ1d008ySwiG1x4s3zC0OoN9w-bJwlT_wdT6s-BYuB-JKgwCgLm5LAf6F497t_ju-TiIFKc_mdGRMr1hN6UVjNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بایرن طبق معمول به این تیمه تجاوز کرد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102378" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102377">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCi8ZjXdnCNVXhLU6Nm5KI2OdpGi0MUOJ_tr20TAsZ7esz9Nh7nTXJLhz8My3Z863lizR5ffmBlY94cfQrasOefWn64N7UZIn8VWphKP9dKV78IqgC2qrGFQG--vC1Bup-y1_a2BYtcrvSB6tpKS-brJruQ_fRDXv51EE3V5wQSL_Mzaqbj1DxuoZl3D1pQ_n3_9JOlvVCXKZvDMGLZSHpJxhNEOy1UrCTOlNzauETmsiis4JmmHT12uYOt2V5K8hFd-8ojBwNTs637v87Gi947d2FlWzdU9cPdH5JX7jXG8zxNc2obddukjjVWhM-yr-AudTXiF9ox64VDvJdP0gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه فدراسیون انگلیس:
ما در کنار همکاران اروپایی خود ایستاده‌ایم و بطور کامل از موضع مشترک آن‌ها حمایت میکنیم، ما با برنامه‌های فیفا مخالفیم، جام جهانی متعلق به فوتبال است و همیشه همین‌طور خواهد ماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102377" target="_blank">📅 21:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102375">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIp2bvk0S4wnSNjcEtkSGqZ0dMBkpv-a5ayJOFG0f7N12IKSEGnJZoe8xMmHaaVjI9lQLSGZ9rKB1uvJcYgHbs2goH2WAkZ8K9JWIzg6A4USFm0Hta88_38xV_io692SfdQ4_rkIFwZkzH2RptsZ8rp3dv7CAtbdYW3lfbHJ3EKFlgnzjK8emsQCSbCrjmhHn3I07a-Vzqn_yN-hWyn7mBL-stuXmSAYnASWezvgFoCvfErQlgGgwHgx3wi_O9kyt_5C_J4LFcUGC8NT-Qdpet2dgrtyQ8x-bJKT_O1N5klBPmrC3tP9TLr5B38W2FeI1iq2MHi4y2dyj9ZcdBuO2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
اسکای‌اسپورت: منچسترسیتی برای فروش رودری حداقل ۷۵ میلیون یورو میخواد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102375" target="_blank">📅 20:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102373">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIOjX_UQ9wAL26lVwIouXsBEElgn7bd4E93sjex9JzIQPXiM44y46tzkztr45O_vV6pi4NRMSssjiKBajnQe4yvWijIXDyJSYlyusWkJeB4w0LW7awqdHZKIFv2k-zBv1rThTPB7MDoJMbUHO6TXgfeNId1HoncYwwhrRTkZyEC_VwMIFiVlt96-S7GMHWBUY4ubbBa48lrz7cWCzZVhbavJzp-xPiR9Qdl6ooss7kvIdjy7su-dfkaiFks6d0VIJWzeVwh13mHgTmtnwLAMCazgtBU2WS81jkn8yIIbxsvP1Dn1MpUsWY_6XOGXPVg8fSmAB498a-Qi_lF7nzbQwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d9c0f441.mp4?token=YTmPacCL_iuUwzUAzTlLzOCjpMDcD1uhSQOv0enBG9YITxaYQtBXGt8PuhTsX-6n7CUudoyPfuUpKF60TB3p_30EiF07zukFbwyYaxJkPsXVK2MC6lwi_mHMOd2KPKsk6DhFUQeg23RgCNEGSCfoJaF3pwm7fhk-gUaxVADBb-zzkGVfVaR2-LOWjxkxM7bqxQFOWkfGm8XIPY3gE1QX48H8UIeiUjyhxRpbdcrthQok0QYbdldtawSZZK64NqXfGB4H92owBzmQJjTojtkve5PIg_Qwnz6jaWhy9z2fdmkyhboZOwhL2KJFWZV9heAZ8vqRtEXmGhrNyWAZffZRLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d9c0f441.mp4?token=YTmPacCL_iuUwzUAzTlLzOCjpMDcD1uhSQOv0enBG9YITxaYQtBXGt8PuhTsX-6n7CUudoyPfuUpKF60TB3p_30EiF07zukFbwyYaxJkPsXVK2MC6lwi_mHMOd2KPKsk6DhFUQeg23RgCNEGSCfoJaF3pwm7fhk-gUaxVADBb-zzkGVfVaR2-LOWjxkxM7bqxQFOWkfGm8XIPY3gE1QX48H8UIeiUjyhxRpbdcrthQok0QYbdldtawSZZK64NqXfGB4H92owBzmQJjTojtkve5PIg_Qwnz6jaWhy9z2fdmkyhboZOwhL2KJFWZV9heAZ8vqRtEXmGhrNyWAZffZRLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
استر اکسپوزیتو درباره آشنایی‌اش با کیلیان امباپه:
ما در مادرید با هم آشنا شدیم. حکیمی به من گفت که کیلیان خجالتیه و خودش نتونسته شماره‌ام رو بخواد، برای همین حکیمی شماره‌ام رو از طرف اون گرفت. چند روز بعد همدیگه رو دیدیم و بقیه‌اش تبدیل به تاریخ شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102373" target="_blank">📅 20:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102369">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SEWBkvuN0kT5HbT2Q1xQxkh2ZAQR87cAg8cbzZbMkALl2L3b7s_Kf2sDjlNfPhb_suXr0g2g6VcWpYaD738jcjurxc_uqwNd_d3PMgnKnV83d-tkyGndGxVDcuMZ8Q3j2qGvqIIo5O6Ae18ACR926FHDLuUUgeyD7uFUt8kvn5C0vFk08tAJ7fNkZKFukmVyIv50-ZEtSalv1-BMVjONkHHjxCrlFtL7ojr394zCbaawY1DfqkI_EeJ0fmUk4aWw1Yp_F59xqGfJJmKyLTRYc_3ZmVrSMVeogbCDJJTkj9VNH4_gL-CpmHtzdh_qJHJYp-R3Kd4VFQcnDllz-s5Z_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IHe0W3og1GzWpCVh06JcbbOf5kWoftoUjyWBZ1N9OYUSBF7BpG86BERa_OrLyNieqzJNLx8Sb48ySlKiV0Vwmoxj4FITSk6I7Ot0bg4HdEcE94c7Cf7KI6vodqpq4nxZVROLGcGa9T-KjSgMoXAwscJWwgpH9ok3VQjxumMQ03cs7uIem6OpqzTMM1nDH7woTrfreYbrcblO69oKtfh9NP7sCLfXvh6sPbisMX3a_zu1BL2Tvisp0YTOQ9eF2j9FDABgVnus7mPXL-mf1eIlgQeSPvwzausdK2OaMjrISS8bsCWsafquyz_WeIBpT7QWR1qMYiVILyy_pNUBigD-sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M6Ug3BnzhmG5FsfHCOxtzSxtLm3Xyek870n6qUFdYHjMF3ELCLw6pav9wCTjh3GFA1J4Cc-YWDfWmO2cvxZ29RW25aTtvELTMThMMGKukgZdPh_Ag_Xr3kDkyx9TX7uv3JsW9nieZ3hzeVKJAme-Kdt5iXmLc54Rge59AmgnCvkL8q24doAd6Ledq_30-d0-FG8JvHEJZQCvQ2nhBie3U8dwL_sMQOXausQKNURCMJkADXlNKe9CBhfiRptnRvsgY2w5xPYCwT2J9ge1HJ1HLzooPw6JlMaOsf2REQfggz0jX25BsFcdBKZ-EBBlFAnHZPjpurZhoF_wG2t2Yigk5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JTTi39O39Qm0Sh-cUomc2-nNZsykHdkG63BR91ULOHmMAXeBd5sdXEli2k1V0TBwaog7cD9YYZuXSW-BMqM2oBAaCKrOcEFgDqeLgY5nbE6xJ5ATnSSroB4gDKrV0tIcx2o1BcHC4E51zcead1A3MEZNRqCG9dUolp6D5gzLBR9a6OGtMys4keL7v52PsUQHs_SJGzBORjD5LQ6KzY3IBIEjN8Qms5zN6g_PFkuyBJ6sdEsGWr7suCOpT43dgcSBsdzgahIaEp55Z4-dIN12Zuttg5N4QRyBIrLvP5XnKATecG9RYYo_XUHBBxrc748ZOWrtT5NOOR82FbOWMlQyrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
چلسی در همین پنجره نقل‌وانتقالاتی حدود ۳۴۲ میلیون یورو هزینه کرده!
💰
💸
خریدهای آبی‌ها:
🔺
مورگان راجرز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
— ۱۳۸ میلیون یورو
🔺
مکسنس لاکروآ
🇫🇷
— ۶۰ میلیون یورو
🔺
مارکو پالسترا
🇮🇹
— ۵۷ میلیون یورو
🔺
ژئووانی کوئندا
🇵🇹
— ۵۰ میلیون یورو
🔺
امانوئل امه‌گا
🇳🇱
— ۲۵ میلیون یورو
🔺
آلوز دنر
🇧🇷
— ۱۰ میلیون یورو
🔺
دستان ساتپایف
🇰🇿
— ۲.۴ میلیون یورو
⏳
بزودی رسمی میشن:
🔺
والنتین بارکو
🇦🇷
🔺
جردن هندرسون
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔺
دنی ولبک
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102369" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102368">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b486c4e528.mp4?token=TGHjIGdUGEDhYDtKPnrW-V7Dyko4VR4DaXvnjE0ggBeJrjEIIY4LEu5MXHym8JCtyyzYmoDAB6b_Mu_8qK-zZAPCc2QqQn9XuTIVnhYmqYyPW-hvuRuAd4b5xURpjwj_sI00TZCatt0UP_1TsHiSCAohGGFv2V0VL1ItfUPdKHXT2r51K0qKqyDLcKzoyyuvX0Bhr76bRBCi-DudldLmPbh3bmAlUYv1JuFptpfv6Q0SyLvSD7auACftw_L_1p038LOXhBKp1_6CPtAbEyJEkuoC6j72aEs1W128YNBzHI37PNUaN20JN40c1UVut_WgNGoX5-IiZ7_rd8LOE7KWpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b486c4e528.mp4?token=TGHjIGdUGEDhYDtKPnrW-V7Dyko4VR4DaXvnjE0ggBeJrjEIIY4LEu5MXHym8JCtyyzYmoDAB6b_Mu_8qK-zZAPCc2QqQn9XuTIVnhYmqYyPW-hvuRuAd4b5xURpjwj_sI00TZCatt0UP_1TsHiSCAohGGFv2V0VL1ItfUPdKHXT2r51K0qKqyDLcKzoyyuvX0Bhr76bRBCi-DudldLmPbh3bmAlUYv1JuFptpfv6Q0SyLvSD7auACftw_L_1p038LOXhBKp1_6CPtAbEyJEkuoC6j72aEs1W128YNBzHI37PNUaN20JN40c1UVut_WgNGoX5-IiZ7_rd8LOE7KWpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🔴
🔵
تاجرنیا: «ما و تراکتور، بصره را به خاطر نزدیک بودن به مرز، به عنوان ورزشگاه میزبان انتخاب کرده‌ایم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102368" target="_blank">📅 19:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102366">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBwVDUwIFvT9T0dCyFPOvbKZqnoc-lab05u1DKbKQwa9vkOyBiRKsii3_5LtjnXwvO9BBbBf4iVAiyOCbgc-bXpBi-soZYBIF2X0-xbiZz9QqMUOWOacc_uTBlR5qCANACizink5Pmk4GQ8fULnkxS5x24o1BoMm52WfMeQeRVkQlgMLsXaICXSKxswKvGm8p3oa5LqnU0jzCCNzM22-EMNI5oMQ1uu6jeeUi-h09G45-FYzYLVJFD_4D6a4tVUQtTrqSQxZWf3SiYoVqkNCgCCDHgk_p_8zb3_yspII25Hwl8BtjBYHS1bHR4kvfP9yv1Vkt-tMCXc9XQw3UjVxMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
✅
تیم‌فوتبال پرسپولیس در دومین بازی تدارکاتی در اردوی ترکیه مقابل آلانیا اسپور این کشور با تک‌گل علی‌علیپور به برتری دست‌یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102366" target="_blank">📅 19:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102364">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPxvkK5fnlVn7JxMUPxOIowsg474mTxm_aBuEiYii8b3TRMKpy9fq5QAcOT4Dk4frvaQ9_6H2KrdT2qckez8GNVhMlbDDyh8BrWCxu4PXYM-iGMblP6fVZLqshni8-5Rw97wkPMjNUX9tcRTknTltCRcBAfpFHoT4gzZ7QbCPJmmpYOMfswBTruM1lJqb-TwjWlDnJB3HtVCOUogiufanaduqh6kxzUj_38kFw2bN6FQxUGxl5nD0h6vhZC_eRmZ3eFv90f48JosMxPTT9V4tn9T7_NFLgijt6uB_OyVwPIYeMCilRn1wubiN2zDd0lZxlwPqavH7Q6Q8KJPK9R99w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08c0c36c9e.mp4?token=AmaB8V_14EC-88_AAEXHhk8oOxmESz77cgSJ4YV4Jzk3Bhe_v_bFrx1tag-wdhqHUPtxE9JbMVtzzZg45zXndjEk1yGDDW2luyH1eTzsDWkijkGaT5ObpFbya8maiSIEv7gmqike4mcNk8RkD9k2wXQJwYMWYJ6cO0yePoFOSs33t16BJcY1BCiAoRR2VjbxbcgsbhG-5ap98Q9GTc-fheP8-Q0kwTOGAlweledgD7nof2-kMzTmBEph9amRKUyNqKtXjyeervG37zNHAcEfVhEFUAXiC1qWzxTRgWcDUS_1ETMAQjjUgEmzurCSjNfoTfjEjlexnnEG1fjHYXJOxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08c0c36c9e.mp4?token=AmaB8V_14EC-88_AAEXHhk8oOxmESz77cgSJ4YV4Jzk3Bhe_v_bFrx1tag-wdhqHUPtxE9JbMVtzzZg45zXndjEk1yGDDW2luyH1eTzsDWkijkGaT5ObpFbya8maiSIEv7gmqike4mcNk8RkD9k2wXQJwYMWYJ6cO0yePoFOSs33t16BJcY1BCiAoRR2VjbxbcgsbhG-5ap98Q9GTc-fheP8-Q0kwTOGAlweledgD7nof2-kMzTmBEph9amRKUyNqKtXjyeervG37zNHAcEfVhEFUAXiC1qWzxTRgWcDUS_1ETMAQjjUgEmzurCSjNfoTfjEjlexnnEG1fjHYXJOxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اولیسه درحال لذت بردن از تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102364" target="_blank">📅 19:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102362">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6UxKYNhHJrkfXbzIpj_vp1dbxxVfjWXR3oBvKOQ7-vmyTlBIWvKhMJkx2D0Itd0WIWmuNCZ6AulJKq2SnWBobn_mavUn7IZgrN9ftt3XJZqBkuU_DIslZHdPMGHaLh5B-hrDgBLttE-PGCt6FRSPOVAnyEUoHIGTvGS2MRbUPcLXk1b9UJbjbQiEKCPOehYScioV5MaMy284u4Qy47DMNZIoCZHG5U0uIsFsdXm5BVZEeoq1YrGhLpDk9eAdKtuJCX3nXdSwr3RH2eKncR7Z4ZdqC3JJCnB3Zvr7TFUCw_OQeEbGSSyG-UVqNg6wOuNk-g8B7OJn0y8GDp74daG3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3645ae0183.mp4?token=FD8S52zt4ErJ8WknHB1sJgJrbBwsmn9Vdq2RX7qL7cT2FrS7K1Wx6MFE9Lw8d7lqP8SW-9rgps_G3rGyCsg4FTacnBJfq0BqA-lC1PtG_NTjMjXTWtGauy8GX61xJJJsyU3EyVYcVO-5U-NBkhDWgCF8kOzkM2Wj6dLvYRjW0baLJ1GcyMW0__dRDtBOPJZ1LIW2ojc7P0XFhhZmbTjhvHYiIHvyEpCCfOce_q_64GDLrmFoPHrb4QKB7RsX4WHeWdlScLmoxeiq6U3hkjoDmBX_7vVvn1NwEHcID-Ie-ZFRZSX0W-Npkci4u9VENd3e4oidTkNpvKIewN6bxQ0LNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3645ae0183.mp4?token=FD8S52zt4ErJ8WknHB1sJgJrbBwsmn9Vdq2RX7qL7cT2FrS7K1Wx6MFE9Lw8d7lqP8SW-9rgps_G3rGyCsg4FTacnBJfq0BqA-lC1PtG_NTjMjXTWtGauy8GX61xJJJsyU3EyVYcVO-5U-NBkhDWgCF8kOzkM2Wj6dLvYRjW0baLJ1GcyMW0__dRDtBOPJZ1LIW2ojc7P0XFhhZmbTjhvHYiIHvyEpCCfOce_q_64GDLrmFoPHrb4QKB7RsX4WHeWdlScLmoxeiq6U3hkjoDmBX_7vVvn1NwEHcID-Ie-ZFRZSX0W-Npkci4u9VENd3e4oidTkNpvKIewN6bxQ0LNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نیکی نیکول، رپر آرژانتینی و دوست‌دختر سابق لامین یامال، در مصاحبه‌ای مدعی شد که رابطه‌اش با ستاره بارسلونا فقط برای بیشتر دیده شدن بوده:
راستش باید اینو اعتراف کنم. مهم نیست وایرال بشه یا با واکنش منفی روبه‌رو بشم؛ من سال گذشته فقط با لامین وارد رابطه شدم چون می‌خواستم اسمم بیشتر دیده بشه و به کار موسیقی‌ام کمک کنه. با این حال برای اون خوشحالم و امیدوارم اینس مثل من ازش استفاده نکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102362" target="_blank">📅 19:01 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
