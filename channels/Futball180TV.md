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
<img src="https://cdn5.telesco.pe/file/FcIsEUqwHUiJMiI4h-c4KPWeEfQJidd04r6LyLlTyPFUmqCVNeNjl2O2piStDSqQ7s7Clk8rn6EE509w8Kh-LXW8ZZ9N7ezY4wzSN4B6X-kSBf3zKWZl0UsIH63SjdFuhq77asCF-0qhMSlwFrM44cL3QATVLz7hUFdrnvMrxUhjePK2khVGYq7x4jPPAfwGmedZ84uM4YquNKN0jbNuyUVmZg3CkvhjVdtfQRlLuKfa-mp6mL63x9PpEyMss0Eniy2EUhBSnv1SaLNrAR_KKziS_16b5QOXnXhhHaL8JZxSrI2gilfogjPKoEDcaWEz0jQrdkgei4HBlRV2TVk3Ug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 507K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 09:00:12</div>
<hr>

<div class="tg-post" id="msg-102488">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7q3yDIgOI6aD9ghFxhJoTVh4n0mdf0EeF7cgAIfUN5UaLBoPodJQ7fABvyAn0A2_IgWzidZd3yq5DiHSmahw9bcm1nB38TQqsMUkKNQNcA_0MuuDDfNha7Knt32VAYGrrEZvbmKYsxg6MYEwnMuARJij9-XoaotDAR0ExOgGsUY5Rm6vwpUbbpXfu8NP-tLVuY5MYgB8Ihzi5rs2f4-K4q-49zAwKwT8Bt4a8htqvVmlWMMK2OvNvvPZt6ZuNJsZwb5iMZDPRK7Q1JLYmS4wbrzCgG-d21RNsksDExh0clfkcjk5TlfLY4LJWfazfydvawqu-mfCFJNPie0lGxpuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای اون ترکیب لجندری بارسا چی میخوردن؟
مسی عالیه :)))))))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/Futball180TV/102488" target="_blank">📅 05:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102486">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eF96ltloueL5yidqKhK4m68FdV-Hf77RpL3qW0DjoSWIKRQTDvTivyZmUlrR07YqjffZYq20j3BYGtIYQ8LDLxEXOb_vHcWYmGYtFv5mkywik77SJG4uy7KMpK0f4UpeGAlNnsUNhm30l8vsK1L-Z7WoHxBFfNTHYYTrXDWTQ5jr-oP-hUYLY-VLbBaMaOHkL7L_8cLTbYAc3186RQNUpqdOOBCYSjBGDGBnlfVdUqpSdwCDmr-BQOlK0ffwhemuA9I3UgZgkop8NQR6dvhE8r_w6dNF587G1dRss8f35KzuaMOiLsXTjyjVJ6sRO4xmLZ6Feifn0NBNwZYcjPLHnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
گوئدس ستاره باشگاه آژاکس با رقم ۵۰ میلیون یورو بزودی به psg ملحق خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/102486" target="_blank">📅 02:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102485">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇱
کانال ۱۲ اسرائیل: نتانیاهو در دیدار اخیر با ترامپ موفق به راضی کردن رئیس جمهور آمریکا برای بمباران زیرساخت‌های انرژی ایران کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102485" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102484">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBDbcvg28_Hz6BEMr8Yg2JZMWZmlOCkl1LZl2eaF7rQZbBY_KItzWgN-U6b0Afcs4Sa2614MML0GZ_5Ccw_4blsgTgMC3auPs1bQuZ8QzMh6E5zdKZckeI1h6esVE74t2qF3d4WNxMC8Yc9BwYVuL3G8fwdiKJcsuM58QCn3fvyl_Trb72FeRRosojDwyNjyUoSZ8_M_qO_65AFhoE58J0M36kOL_TP6BSB7pHWAvLw1UaS4E00WPc3fjwkuLw9ce9Mjd1Rvvr08OqNNm_nERHwjzSvzr7uHiK8ufIXGXfWcw8dlZSQQrcRkOyg41m_tMtnb2Zo179uLcOsEVUTgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب بروبچ محله تامی شلبی حسابی واسه جود سنگ تموم گذاشتن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102484" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102483">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102483" target="_blank">📅 01:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102482">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edBSh1GaeRuz_SnJxCe5heoOIidGWrOlkBi4pdNa_Ybi_mWeqsTS61lTv2C0PauZ9jUPilccCnod-EgQAlFJ6a63Y-FItjqTHRJTaBGqcl_PQPJ8BMT5vx3n9WJS2XIoRgKL2YpY6R6XYm5qT2q-wXY2osRlAT0jxsdnigDNibr5sVcfp4SINpnH3W4nmZEb7yEVzehx3nWVJ1LwsAcaRLnSv5WskzD0mi3SIRY37VRlYAY8s5QKyYaxwymBJNjeqmUma0HB62tBaTy-NU_if1q2Nin74ynFXTSoM4LnJ8tWZa_93tmBU-J3-dbTdRdvULplIIrpoJRq7y35TJTtKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102482" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102479">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y1lY4nX_NS_1lGl76WSpFtpCttQvzASce0ln1DlP_oDEJRzHqR35SfCbeLIGQft_dvHjRD78kE2boANSDaMPuUAnytaSs2ajyFz1dUnqgSBYFDQlFdUPmBrIxhNbWkKiNwTydXBXV9nr4y8pm7Eb5fng0BZIFpNzmCLykbYCmPIz_ViVBYbC_j-1Qq6aVOQckY6iwK57oFiWo2Bo4_kUW8XPFFOL__cE1ugKDAQB69KslFTRKYVkrDzLpYnruDPxpqcsSZ9kzod1yjt586HPLm8aCKhSz5LFQ1I-dwacSA8c3qVsSlhTBUSCk8prnu7qHS5JCHdbVQHPxkB2VRhMXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gBoC4qO03lwN-ZQ7eQbFbimIdBUhe5fB7qogfmvdVgHIKfK3cqKoDAXNmFtD3jkUHw0oma7DSwI1kIZVcHkxrwJLVGzs_nhUjmUyOIny2iaVjLt5isJWayHswnfR58JTMlY4E3DMnz68-KY06XQabH1z0m1cPMWaORi-UpbCLlHFFjzmyQb0ylwrGPrPdS69vgHyqm9GJzPK6e6VQwbqomMg5NFbD-9pnk8M-p5zRb5oWFwU4HbtrsBpXvS6qPQbzgvtNYN-fVNS5ypCJJzY85dNTKK_rM67EEwwr2SjYC1zpGyxeue6sGQO27XOIt30d1JDgdEBBfpOFRyxNF95Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6deKlP5xYjwdAoUOsYZWyb2kHDXxua9_mr4Ds00_R3I7P-MnO48rYPvWKHBQS2XeHUiEt_XhdDbGmlL1o9UVEd-wc2zPXhaSdFxUyw2j1H4kNVJ_IhausjpfkPpfGG_leRxuIzdbcKOtvRlBAto4CigvJphR9QpkBjMNXIW5JoigvLLTn_3JvvyVlk0qDqr-hW47z1ndexKD_KvMb-Qp6nk6RYoD8p6_m4Koq6mxh-CFl7bYEcQAVmkJjdzzmjrkTA9Tusxm_Xh2xNXAbmNsuBZN5AAb7m-T_srYURCjqm3RgOjPWfCV_ZclsioqPyDjaKLccOJhdHXWV6CmBW9Qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
باشگاه فوق العاده محبوب آگزبورگ از کیت خودش رونمایی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102479" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102478">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LG5ad1so2sO4mttE7gPjjNZVl9OVyqAwJEasYSKI2ibVSICOsHCbjh2ylvjdIWWmxYfG5M9zz_q0Ocnz03LD7y5kN4FZXGQRAzXSKGogfbPvtdQr18FML1aunBfra9juTQsVIjK_J50Uw1DO9NPb0-IX9antrnOb5S8r1MFyyZFcjF4ru_NU1w7VJFp0x1xkXJ3jKhANhZe9ZEKqfs97EaLGi_0qSZrlYX5VuT7L4clAy8lySvZGnEP_SxXJUTkOvho5YttB6fKREM3v9CdNghBZ-JuEJs2C1kqz-ybFfgNmWt5bYnppctt_cUN9BS3r7AMReZm0LJLaSh1uUQvv4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
هندآف آرسنال رسانه نزدیک به آرسنال:
وینیسیوس شخصا با آرسنال به توافق رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102478" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102477">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی،…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102477" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102476">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102476" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102475">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GM9WkHhC9DUmoawt2xycjRetnyrf-4yS2j-9667SYNNdO6q6bwsoGRpPyDaCM4Ap321fFOyGLIuK45gPo6lQHZcUw6dlpxkbUQTl-8Wm4mXkA3f0XEaWpYhOULujqjV--WXrS_-rPD2sB2HQyRvhYSedQjRjSbkeyoD1JXeY4ZKBTWD5c1QdqZZaus1UNCGpdzlwtNlMDEpZ_2XM-TRpL4nmbmY3BJ0E7f-72XZiRlBPYYRJLzwe87mb5nTpeRZ9sGZRpg3nit2Eh6tJznQwRNI8qHfFJyw9aWMsJBy7CK3s2B5vknk5-XkiWKW_SQzDOm3IRhiD5JRxjTtdJcpHRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بارسلونا در یک بازی دوستانه مقابل بیرمینگام شکست خورد. بیرمینگام با نتیجه 3 بر 2 در ضربات پنالتی به پیروزی رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/102475" target="_blank">📅 00:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102474">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_BkpDi_CrVjcD417jVQEzkBg7vqTa95cJWUbU--fuo4YQ_HMSn2M6q_Imp82UhpxfT4MoApdIY6HAzU2tSGHeAy_GsNi4l2bNNwcu35vOjFBWEDf1RaXR5hoX6_qHTjpvIjMvNbmLzq-E-pERXzzsKkCZi16vFGL8aJCHScW0dtihg4-7qQrly7OCHbBqlvGakBwxzQGV0fLim-LHtjFZIiXPzeTOwavIMiWcxihGcwWNuYqDDEQKskJDJDzEpAfjM2G9aWpA_dr58wS_b-ZdWdVZXCvi4jo-cDwqDOEer4F9Lees3a8P4rQ-3Lqt7gRlxp5dSLCkaoTbKS2e0jTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دوست دختر یامال
😦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102474" target="_blank">📅 00:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102473">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZ8I_VRhIrXhqgmSMqD6cpn2C-fbM8FaBW6gxw3L5DPyuoZlxIUXht_MgJlYd8s2I5Rbu6Xx2rPQXYwPYf6M4_uOz-HReEZRaQGWEtRt08tO0Dare-mykYemrjc4--K6vKm3I5ude4UkXQxEoxnUpxaQNdEI7mCgayf5LpEtkSjXyXMPFIQQB-SxUXkVNpHHEM6tw86wfeaFMoUEZF1PvGwi8WBDDE4hwaFlRVhPj40PgLm2C8qIvYKfuuar9rQ2RhmnNX_syHkgvhay68AzJZ24LpRQhuo7G1NcYYfdp86gCX0y9DNy15zFG6rJvk9xNZJijIkRfzC7KHlruvyZdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🤩
خداحافظی امید عالیشاه با هواداران پس از 13 سال حضور در پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102473" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102472">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYMY_npcHC27ZR1mbnaIoDetbNK691Dni1nICiwb4QbGg-moErDachdvtdJV90vFMr3j_XjKRDOuYaZZJg9Strk8XqyY9xO4PWAlQ24BOXox8fAk7KATvL6NeSRmcLt1_iPTK6GNF_dxB8pFOEylCo2-1FEOtREdx4wTUWk5UYpf-dIksvc4PdcWo3fToLGIw9mxqV6RnnhDkUCMgBFbWzIClBMIsM7nO3MLpnu0ZNWkBJWWHiHSh4OpFFW7TWAKNjj_361zT5yVPleZcSueRVInDyz-TQq4ax67rrYdF8qYOFOJyQHFQ8SgONgRIT7fPKPKX-tsi1tpnLswLHiZpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
مسی و کاسمیرو تو تمرینات اینترمیامی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102472" target="_blank">📅 23:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102471">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102471" target="_blank">📅 22:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102470">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtvBjDgbRoJAy7FsvLzBqKBIRZABnggEdppkgmKFJFnbfNgu1hh0rVj2Bw84y2NGhoH4Lr_lqSi5_h-TaSvCD1eUHFzxZYAJOh3fvYqCkC1-cr9sOXrVukNAycoTNYoex8g38WXHt-F4uacldeB11Y9maNYaIhD53l4hzz1DZHN-PyvgYjEw4OuF41ckPx8-RFKvrG2SgVvwFnbQKfd2lnpJIr5A72hlcLXIgjQZxN_-XeZNY6K9IW254YFQ6K10Z1uvCaNXGYyhKfqldFIsd8fQhJ4CibwV7So11mdd76C6I0_hn_bj5XLnOOEeEDhkoNekVCwpE0cSRW7XjvnSIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ار‌ام‌سی:
مندی تو وضعیت مالی بدی قرار گرفته در حدی‌ که مدال و کاپ جام جهانی خودشو 54 هزار یورو فروخته.
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102470" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102469">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102469" target="_blank">📅 22:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102468">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjJAhr05LZaBk5oKwHpp0bYN_dHbNaQyz8XmxlLVGX328HrqaglR5RPL-T0Ii1Fe5zDL2ajJmK0qiNbddeqGS1bAbb-2n0pFHhEAXp_8x0G9HnhSV_biaUkHZ_c0xk8NnXngSP8aIw715IEj13cboQhX6uc8F18n_pq6M8XfenGsVVJPOOuSj-Y8Z5prfIfIrGN9-KexbzefKLZ9QEBPq8cTmFr1xYJlSPLW_ecsjakNTe3mZ2smpiSS48QpojggfQ7Ep1niN3ERQuWm3mNXiJHJPFkXNpH7fqUlBe6hdMIhO6bYRdJLaHQGV5DrDOlVaLzPSfmazYDCsGaEkEpLpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
بمب لاپورتا ترکید:
جسی بیسیوو، وینگر بلژیکی کلوب بروژ،
به بارسلونا پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102468" target="_blank">📅 21:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102467">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pasn1V423e2yE5Au_5YJF0N7Jlg2ktOj6hO2mIpcrJ764GEF4ZryXwUTkd7G8KDt4trGYzeRw08aINH8XloQOOy9XeNxkdygJYYy8MalFH5_SVfey_CYeC2xwk5lD2ybXEEElktfEh1WpOFR4a6m11iSLlDe_IRFbT_CNoZKvP5noaOW8lwcdfwxq0EEnn_N9EplGy6ide4DXpggv21hEyNBGzKyTRV-QxwZU7kIilly3Rewke-P7Kj9ooRihIFcJxgETLt-BXKQDs-am0l_8zRv7k9OopfTkyRHUPsm9ZRT9YrUNMgyfTgprMmXFF1sTDi-a6SPX9ksW6QpP8f50g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب امشب بارسلونا در بازی دوستانه مقابل بیرمنگام‌سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102467" target="_blank">📅 21:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102466">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102466" target="_blank">📅 21:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102465">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102465" target="_blank">📅 21:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102464">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102464" target="_blank">📅 21:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102462">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102462" target="_blank">📅 20:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102461">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102461" target="_blank">📅 20:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102460">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102460" target="_blank">📅 20:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102459">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhtgBuSIVtECjWBENH7A2P_QF9ZTv2zzfC_ePoOR3zayZBlpak5o-kPqYxdYgMVp7_veupnruqgUugWyGBoWTXDJzgzIzKYJS6NqxdaSnghR8MTM7hN1vGRnZBgcYHKf5_d4Y8U3eXQWfo4OhilodFvs11p-vsyE3KphQA9zEYkA10hc-0D5kDeZfGFVHwiuFnunDrU-BoYcxaSmVDYir_kOmTESPxbLX2c3kBXqTBbFjruauuEGdtbOUV-F4F_QslPQKI4cSyDzOcnKg7C42iYwSw6LTmxL38RpagxcasSDKH3dWInrY6AmbLVB8nf0vVIv6YviSTVevCW4EU6jig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102459" target="_blank">📅 20:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102458">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102458" target="_blank">📅 20:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102457">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4HqdcUXfQm1v0M5NiPy9CDp9c4bkVvrYhaKqcrPOcD38jMrt1me9sOF7dBVQp-gVmGhorfVCZeqMkNzgxZ1Nl2-GnecM9lU-EEqe1v1qimldDYj5WUCLpYyxJ3rihSPIcF7lZoU9SLlGw5OYVWBX5i_Jy-7BXXN4Kqnfw7qN39qVGKoOn_SVbtkkDni0z921Enw9ooGrm1Js1Pa6cDyMFcEpAsq4GxhsHt49IsOXSizHgNTWN1Cm8Xh0n-mOzlYirBq6a6RAomLVQn91FBa4jH66VW4BSLqJ8LYt-vneeCrtGbukI0pYfzqZ1XEQHvFYK_EwfLO-QbZTcKej_OG4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102457" target="_blank">📅 20:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102456">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102456" target="_blank">📅 20:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102455">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1OiiTiAzpQE9z4tIIarAGBsZLubtLzpzz_gtv6oPhGkCN4pEZH3PD6MYw4nVFqPiQ3p5VXqWuMJdcYxcqdVeX0hD-mP9FLqrJSHep6qfCIRoIWKtEZfTkusblUSmSiAdQF9om7Pnq61dFKGbkjjL3aQdLPqzlf6P6eAzqIoWqAWlilqGa5c_cETZh0z5EwT4YDPUjSwB_mcrt6Db0WTWncBXqOsKdWy84KqeTxYlwy1EhXzaGBj9ROE4xqgw9S1Fkc4gVuAfPQTrJc_byNajYQoEG633bfSpI58-6crbxvpCIfTEl5liTYoZ7ju5o41J2bROz5kQgTfPP-HNoIFHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102455" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102454">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fq-0VXPVp2KNEzL2HBUrLP5QK-RWmC5B5AWV67s6rePpeAuMDO3pDexGxT3kXxFJ2WvCMEe9zsZt5UiIh1POgp8I2Pl_fegZW0AecYlS26chqSGCM5x7Qy6YvyOZnc3ZMTX_TeOziMfnQu4rQSv3CJ7KEajbG9Hb6hTfSMOZYtz46tYlPajU4HwEIiiOwBRkHLRtaljtxdFbMqFV7m8w82gDr8qyrPCxMRoVEhsu1T4rCZeYwx75CwdwPvwOVJq4DdWeoIq_nAnEmT5_bXNcwKI_zukk_980cbJ-N9Ww-i5DBqh6ZsfysMB4S9mfj3dQCfONk3jQPti54Z16PrIFUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇯🇲
وینی و عشقش تو تعطیلات در جامائیکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102454" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102453">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
📹
🔵
🟠
پخش زنده بازی دوستانه استقلال و فولاد ساعت 17:30 از لینک زیر
👇
https://t.me/+E5pLb4kNVJZiOGI8</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102453" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102452">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کاسمیرو به همراه خونواده که دیروز به این شکل بعد از معارفه عکس دست‌جمعی گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102452" target="_blank">📅 19:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102451">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNG5RdvSPi8u1ASpS3YfgBHZFBwKhILKWZ2pD9_iuzFQhTwVY2lsIiXUX2F5HOtr5fUQpz72k2C4LoyYQELL_AT8-3DjxybKxUvMncYkGGmWWj4B0emGgBQ5Lv9Nt65s8xNJKFB-W7HYITVG4hEPD_y2UjFJK74N6wYmwoE0sadFvosPu5IbfNxbja-JPjtEiGFHLlJuoxYr-eYCeekUDwx2arLPR1vW2noP1MSfG0g0yfp69c7SIPlZxXJQz-j-_F2ag3INGxMy0rhFA_ZKnrxypUK7XJpXbA5zCxIuy5tr2xHJt-o_s53XqgiU7Q_oezwGhUlS_xyr66-rsF_Ejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
رسانه ESPN برزیل: رئال‌مادرید هیچگونه افزایش مبلغی در پیشنهاد تمدید قرارداد به وینیسیوس ارائه نمی‌دهد و پیشنهاد فعلی همان آخرین پیشنهاد تمدید قرارداد است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102451" target="_blank">📅 19:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102450">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEAyZD0fMXqr9TqhztnbA_tpX9MNbRDl4B7a2Rd4cIMazhFVCZZeCM3nqzBykjg1KjfjZXAOVycjuavd0FVe0O1y6LCkYFf-hXsQGUSxiCk4gk8d_1e1-CCwVK9OQAv7ayy_bbGcY-9k08CAeU9RcoLm2Gjh_6e3Y3FFcO243meLaYLkpwMsqcSLEZvqcxpsQZ9zMnHslpf5_zPn2B7yO9KVvqoZNRZr-HEUSS6D7b3jsgjVx5BrsAN4tmo8xQl2cvmT1XHmkcmBQhPEGUDzecao6eBRvIcoqOgvADfATzvA3ixHuXjVOnsE0x9R9lDAq2YJPkMWD371CBANiju8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
اینفانتینو: جام‌جهانی ۲۰۳۰ بهترین دوره از تاریخ این مسابقات خواهد بود چون در کشور زیبای مراکش برگزار می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102450" target="_blank">📅 19:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102449">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBRzI5io77aSJ4atP-ROH80g7vDE7PCdw4DlAsAhThWrDG0kGViyC3GrMl9kEP14G0IWoLg7RSds1spO33gz8ulsihmXyOAaqIbEa1K9yUmSQrlu5G0BeBh5mKmoVt9jQDfbuBWuvzaCXgbXMw-etB0W_nCpUjpDsqzcFXsSkfkTij4mTF6f766FXRoaAfEwT3TqTaOhI7NANr2YOjmjKIFDghXxtTzFGizBXNKR0bW8ZnoCInB8knIV23RzTK868XJaereWYUs9u_PbTp_uDC_4cyHQDHeqi8y5N06EPe_HEsviiNaTL8pvWoRXcbuLlGK6KFba6-nqeg9F2H1woA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس تعدادی از بازیکنای فوتبال
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102449" target="_blank">📅 19:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102448">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0Qe0UW7ry8ViU6hKg0Y_BUKAkXxPU0dNEJ9l96vyu0ouQe7I8ErWwNh2IVZoXNWqiNRxWThAluM9KCh3FO4YHJszGhOXjFvI116wKFajjYer5rtbGkrXiBDC0Q_SyBI8fNmq6Rq7_xw_rqPrHm64FOej-LD8g-nQnrNpoAT9N_JoB4sYul__B9mcQYTIrOUvykiXt3k9Kf9WXBovdQuDpu6MGkOL5OBJ5ylSbyn0S2oSr3Od4N0ppgk_WhwY0ejVC-ViFlFI77e-q8QhbrZMCN25QinOOmfaPHxCB-rCEhlgL3liYlcsSCucJhRT_SINNorEBWKx0DJwDsL0Hms7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
اسپی:
انتقالم به مادرید خیلی یهویی اتفاق افتاد و همه چیز خیلی سریع انجام شد، رویایی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102448" target="_blank">📅 19:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102444">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102444" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102443">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbFwt3Cx86RuRJocw5Fk-gmShKIordBCWxMlID6MoD2qbMOtb25iLJm2A7Wl9zFsK3ZPHTCJRwSyh1it4qpzzR2Z3RslW7rNKmYp4gNTR4i3kOxBzKHSxz36Q7IGLY5tIVGOF3OsCCQu44q29KiXGjR_Y1P_Z4Z7S2kUOMDy-NX1c26IqVaA_uDmnAe2bz7WQQtUfdjqVoToYaRDf5Z9D_NNM9qiMnTFkQQHg_bCRLJRRKohXaPruKoonwRZED0Wuw8E1Uu1Q6V_fuME_XI-sYDmefxjXD7Yj5Dlb6skMjEfS52JAQ6h5UOvY-0exyygncqYFtpGj4qqmCfw_HDSfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی دوستانه مقابل فولاد</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102443" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102442">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCtdyR1eJUsR55mnjVKZ6tu1yuZadyRUkYSr9Pl22TAgDoxR0rtLBMsWneM4_8LjXWV4k928JSBhznZcNfCw0tuPWZTvWGbeJ62_p3lkyRGIukGRiwiFKqn_c02HzJorIiT0XsSaXvUsbgfNvWOlSUfZqErqbX4ETOa9F5IrL0fLT5yD7J_PO_WzTLWtFCVovD13qKfKlU9QxrK0Friaic9JTh1A7CJVi-TgKALP2kJl6Tr8_6RU5qfNHz3pTCwmaSZ229PbqaspvkcThgPaULG4gfNeT0Act1KDv4I5U5v8xYjo21L-OIlxO3J-ZR2Eii2BSO0a-myCD-HXfpEg6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فوووووری محرومیت دوپینگ میخائیلو مودریک لغو شد و او به زودی به اردوی چلسی در هنگ کنگ ملحق میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102442" target="_blank">📅 18:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102440">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CXy46wjlBCZW5XWbfkfIgxKzYS_A9ZBhdQNQVtEtqc_u5X0YyOVDhtDrVFbMEP93hcs6iJ3QVdOracJDaijEWWGpsPiL7DaJ3I2OpIlVw7C-wNvK-OJTiyxWEzd9IARVtyf-59OzLa-rHmDTOzSIYM3xDN1tjrfXnnUgREF1cPnITRJHcUG_oCCZlOEaVOVOan8imrZmSpboM3pCbF0f1Y-MAoe5i9KcY1zerC84HJAp9J3J0rSY0YBgY1uIjo62wFBBZzw6huqVmBrEtpfjfkn-ip5rPC-0O2m9ynZEPtHm2iz-GT9TYx71OwB92rlt6ZDTE1JTUUCepCvURDDZfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mqDpH5M5NX0_RAB2X8LHChxv6AnmEeIOdIwdSjHzLyAZcCj7icTvH8ocQZAeR4ZWkq5T_6T7FHzGBPDH3SvhM2ufp1eZzcdRz8lFXivCi3VYHgPE3bzZ1bMS_OwOj6DcWPYvKM9VP5WS5T0uEMKMpSf2fmKWkBP5mP2h1FRjVPK0BUKsIHvnCWxwJS-CzQPeX5m2oWowhbasJJwzZvmXcxmQd9EwcFd4ROfSneSVRbzq3aYJgXdNxeFx-evLiU3EwL1OyAoCpcA3CAb6KRkD-etbiXKrJsCtYINcfRumSFfImc8mLgdJvJ6Usi3bueyFCXDl5BBY7oQ96kxFhZENzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیر شدیم و خودمون خبر نداریم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102440" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102439">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NL_bosH61kRC2OliQOKGXbnz_xk0GVXwl9yJ9NrbBPlhsmBQmC-hItNhSEYs2tuEbzADxJ1uBF12f0Ou7qJ2yjglFsKD64XkqBRABV6jgaY88yh8F_myjzaj2deIC9SoHp_qqT6eMvXNHXViVA-4pEA4EPaP300M5ypiykZVAkgxAuCkADlmWFRy9sQadwi0hNPIrpGTDCywg1p5YPjl8rdw3WAgauf1u7dj7MpR-tvaw74Zf8MrDrW0plLXtAPEupRDGdCtN1NqBvpGsXT3kakoiywEUKRq-KXFhH6FSxEieuUZhPJqLm8mxfeeXxk7OvzrGn__xn3nVPMLX1wyPjzuREEj6BzeUQV9fpRgJnfHUpW51V8b6zXv1cG7zqmjdQobpm2ISy8eYe-DyYI7zp5Ok8dezP4i5uTN-az9JPTdbIu1_zaSWnAWkH0RNCvJTWVYRNJjJUfYiL6keu1xMH-DnFEmf6rHaAzlMp6-T55YQhD1fMQo6vGw9i4t7_6JbPXN8a_Qgun0v4jYgz1mReG_QvJ8wKswDVJCezdY9VbiLFgRvr0Y0bzDn1VKMmERfE4HGanNNHrxK9ylMxYuHP8jfChg6kuhJNUOqdweppA-rbjteuy7KwaQtUDziwcA9OiFbnASp-f9AVdsg8mguh1QDG_pyS1T0Lcdj56FHlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NL_bosH61kRC2OliQOKGXbnz_xk0GVXwl9yJ9NrbBPlhsmBQmC-hItNhSEYs2tuEbzADxJ1uBF12f0Ou7qJ2yjglFsKD64XkqBRABV6jgaY88yh8F_myjzaj2deIC9SoHp_qqT6eMvXNHXViVA-4pEA4EPaP300M5ypiykZVAkgxAuCkADlmWFRy9sQadwi0hNPIrpGTDCywg1p5YPjl8rdw3WAgauf1u7dj7MpR-tvaw74Zf8MrDrW0plLXtAPEupRDGdCtN1NqBvpGsXT3kakoiywEUKRq-KXFhH6FSxEieuUZhPJqLm8mxfeeXxk7OvzrGn__xn3nVPMLX1wyPjzuREEj6BzeUQV9fpRgJnfHUpW51V8b6zXv1cG7zqmjdQobpm2ISy8eYe-DyYI7zp5Ok8dezP4i5uTN-az9JPTdbIu1_zaSWnAWkH0RNCvJTWVYRNJjJUfYiL6keu1xMH-DnFEmf6rHaAzlMp6-T55YQhD1fMQo6vGw9i4t7_6JbPXN8a_Qgun0v4jYgz1mReG_QvJ8wKswDVJCezdY9VbiLFgRvr0Y0bzDn1VKMmERfE4HGanNNHrxK9ylMxYuHP8jfChg6kuhJNUOqdweppA-rbjteuy7KwaQtUDziwcA9OiFbnASp-f9AVdsg8mguh1QDG_pyS1T0Lcdj56FHlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چند تا از شوت های کارلوس رو ببینید، زمانی که فوتبال تا این حد راجب کسب و کار و پول نبود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102439" target="_blank">📅 18:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102438">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=orgOsAHbxcJEm3-SJRFyE3UAL3aFtuc7fYf_pKDMfRkvzsfSBrEwUFi2OAKPGXEcP8wsMh6NKAmtDOi83VtIrqXi0DGcxeFa3W7KEu65D1EN4QYz6e8A_xLyddsFHFT9wImLeqGQKKlswgBXDfUPDRp_4O3f9asFzyCD3Og_iwU3GjqJkZRQqJTahaQIu9eS6-NzFmRi8C3mYyVNKhRkM-UXhFXwlITcN1NBdG10SEbScyZKb5p9tFr_g1OSRF8hpTA_n3BFYcu_0Aso5Y0i23-beT1J4ed30f6oHoH-IGEkUWXyvZYdRoA05EI0VPkvdUj1gdW-WUKndcFuMeiCfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=orgOsAHbxcJEm3-SJRFyE3UAL3aFtuc7fYf_pKDMfRkvzsfSBrEwUFi2OAKPGXEcP8wsMh6NKAmtDOi83VtIrqXi0DGcxeFa3W7KEu65D1EN4QYz6e8A_xLyddsFHFT9wImLeqGQKKlswgBXDfUPDRp_4O3f9asFzyCD3Og_iwU3GjqJkZRQqJTahaQIu9eS6-NzFmRi8C3mYyVNKhRkM-UXhFXwlITcN1NBdG10SEbScyZKb5p9tFr_g1OSRF8hpTA_n3BFYcu_0Aso5Y0i23-beT1J4ed30f6oHoH-IGEkUWXyvZYdRoA05EI0VPkvdUj1gdW-WUKndcFuMeiCfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی‌از وینیسیوس‌جونیور در سن ۱۶ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102438" target="_blank">📅 18:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102436">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JoPwhb2BEj27-bOY8OtIiU0b_Yhj4WY4jgn8X4iBzyGYWNS6YYABq46XpCC36sAsXmTieHZFRUtY1-ViXQasXJGe8S2AhjXlplPio_b4QGniuj8t_CInSlTNo1-tkGgXDOyb8srOpeEKC7yPv1jgBV-IU6L440hagRedWOYMH5Qo6TgU8xbSLeCmiUOLZ1fVapiHovGNwtTycnluKFA06wFefzAxW5OPEfu2q5HloMZGPGsaoyqIuzgPJgqdhuWZaXsfsXM0X796gIe2qq1BdeqkblCM6_ButI_ChjZl7TYFwsf4b63_oY_l9yIcFmZIKjpGY_9Oh27QlVg5taigVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qEdTwkReHncWTm4e80t5maQhTZNRaRurm_0TJBsbLQ1FQ3U0XbA4Y3mf5tqJzrkimBKVW_pHXzCqYq2047erxfahVs8DBXcNAYRDWHE8WAjc0sVFnaHgSgB0xDteHZ4w96mZIum1gfAgtYjog7i_9PNEaO7WkhCcu-9bzf_2o7J7BdlxduvKztjuPMJyoQCZd7aIb69boQnJd5L8QroSvNSFwLELIW6X9CReykhA7k8x9lD2Ap3-1d0iXx2f61jF0md9mddr-knqxUuBcKOhjUnx5P3Anb_MYWjybkRffxxDiB1SUglxtaZZsx1FESXcS1vILv23hVgKykreuNeF5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102436" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102435">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=MDePUPy6Q13ADges-4QXUW3eRub-xVNOI8Gbx2Tqm78YuPvi_4VX3iG1urlOFnEUorWR6SXpdneA64isE9h9_GAYIq9QgFljzipOjWzX2rb7COKi8R30oQGTscvKJ4zOlQ1eo4kBHGBl9Mfm831RDjKiiiO8BsZ95mhddg2IFzkopmHDYguOAIi6y1FUaPsvvQLMMeSWuVlvYlqjDZFNQAkcktcI1k_blaZJjMw8CJQwX9Dc5qhxFe3MpkWDur1GGomp62BUh9VsWul4zyi0hLPKUvYTJwJ0F1YOq0ZDR1_27ytvnK2pBCP5b4WbIZIJc7r7pG4ivtrb36KhhCvtwF_NbyMqOhmKDrFvWhp5BzNKoZPFP7BKq6tabrCP1kfo50UfUXPjiT0vl0P4C74wRL9k_nOzCXUTkr3R_MmSIHedoZ1B6xme_nELb1yIxkwwdpkmonwhVf0Is6FNjSB5QTONZE9Yq9Hp4v2-GIZlTEKPh37ZKujU--upzYjSTUoo1VehO7wBa8ws99boo7TFqWjLsMojBfFi3JZ4njOa7d3NEy9a7URhfUu4XWXH1A46WzS5x7JUiyvOHTqyB4uMKg5e0RFtudD9X3eGao3gX-Qe3_t8tRZzTwx5IcHnRv13KkVw4t4DOqHLDLCtj996QrUnhkhjf63Y0wVDx5PAHTM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=MDePUPy6Q13ADges-4QXUW3eRub-xVNOI8Gbx2Tqm78YuPvi_4VX3iG1urlOFnEUorWR6SXpdneA64isE9h9_GAYIq9QgFljzipOjWzX2rb7COKi8R30oQGTscvKJ4zOlQ1eo4kBHGBl9Mfm831RDjKiiiO8BsZ95mhddg2IFzkopmHDYguOAIi6y1FUaPsvvQLMMeSWuVlvYlqjDZFNQAkcktcI1k_blaZJjMw8CJQwX9Dc5qhxFe3MpkWDur1GGomp62BUh9VsWul4zyi0hLPKUvYTJwJ0F1YOq0ZDR1_27ytvnK2pBCP5b4WbIZIJc7r7pG4ivtrb36KhhCvtwF_NbyMqOhmKDrFvWhp5BzNKoZPFP7BKq6tabrCP1kfo50UfUXPjiT0vl0P4C74wRL9k_nOzCXUTkr3R_MmSIHedoZ1B6xme_nELb1yIxkwwdpkmonwhVf0Is6FNjSB5QTONZE9Yq9Hp4v2-GIZlTEKPh37ZKujU--upzYjSTUoo1VehO7wBa8ws99boo7TFqWjLsMojBfFi3JZ4njOa7d3NEy9a7URhfUu4XWXH1A46WzS5x7JUiyvOHTqyB4uMKg5e0RFtudD9X3eGao3gX-Qe3_t8tRZzTwx5IcHnRv13KkVw4t4DOqHLDLCtj996QrUnhkhjf63Y0wVDx5PAHTM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درگیری کورتیس‌جونز، سیمیکاس و سوبوسلای بر سر بازوبند کاپیتانی لیورپول در بازی دوستانه اخیر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/102435" target="_blank">📅 17:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102433">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DHTFjNYX-xen_8jK6OxTV1w1UbkZRSx_VjWCjOx06i8nULEePTCUZGDOtLnBa4SeM6uGaQTUj1q_fqxvM95U6b_VdWJlFj9PTNOo9CdkhR-lmlvengxImpm9EOdGwS0XZHEwRwrddisEcJQoekV8leKGsrgVxqZzrvbD7haglbBmO0xHEiBvL_5Sh5xyLLk59csOWGAhJAdziTipO1pz8eIa5A5Q5YC5wk4DeFYuPi-2zoexZDzyeC-rzdk27n_Lj6k5gZaSdbUjIPo5s5mvYMq4B-JqOyvuaIxLUY_x9lxryYtb1ZJGfkiTD_CSTWZbriRDnUR23QYr0YAelppfdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RN0cl0AK3F78DCu7MMEwnpFJWqqKprTfA2AAfNCM5As8y1i-XS08PPhTDvrMJgkxHgPcW3PhkGGom8Ch0kPOidDq9SojmvN7yWlfzUVx-nvfM6M05ZpZy16FrkWSGO79z8UQ6feSYU8X0226U83uWtuE31zmJqV7BaZTAKUeQWgmmUZhAnUpwu3np5pKV7ixlyPlNs6fHgcPOnWGWvm_CxVwPphtKTxWtyzMkMjHdJydxMV2CrHG-7x-i5gBhnLS1S6uDCMqts0NMPR812z1DukBt1e0vDBbx8T7KxiZQo899gtffKYQ8_reIxSrdiSC25vLYj-3nsQLLrfipOCH6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ال اسپانیول:
پرتغال و اسپانیا اعلام کردن اگه اینفانتینو پیشنهاد خصوصی سازی جام جهانی رو پس نگیره از میزبانی جام جهانی 2030 کناره گیری خواهند کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102433" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102432">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96363baca3.mp4?token=uC6GFLXcm8fCIN4TGcrfEF9XtetSpkJ1FIZbbD8nXvy53qnPmXdycITF89PWeP6d0RjHKOOUZcPjVu34fnpG4l_LnTqErD3hV0-J_aqWO4Ru_ehO9uYYdt62mURrrXxuy11Bklr8wUXqeQ42pOX5EYXw2hrQOYXkiqAw8RbledYjyo5e66sJSV2rjt9cT6MSGBDcVowH8PILgFIWTCxsXdT2u4xku80u3sZ_ClttsttVLja3PRNDaIJQFB0ILgV4ci9Sm2W8tIzuJUntTj9TGutUx7jPg6PLmN6Ky-1-zHRVWrLSeGpdByQeda7Z7A6B8obM_fp-OPc6DmX45DA64Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96363baca3.mp4?token=uC6GFLXcm8fCIN4TGcrfEF9XtetSpkJ1FIZbbD8nXvy53qnPmXdycITF89PWeP6d0RjHKOOUZcPjVu34fnpG4l_LnTqErD3hV0-J_aqWO4Ru_ehO9uYYdt62mURrrXxuy11Bklr8wUXqeQ42pOX5EYXw2hrQOYXkiqAw8RbledYjyo5e66sJSV2rjt9cT6MSGBDcVowH8PILgFIWTCxsXdT2u4xku80u3sZ_ClttsttVLja3PRNDaIJQFB0ILgV4ci9Sm2W8tIzuJUntTj9TGutUx7jPg6PLmN6Ky-1-zHRVWrLSeGpdByQeda7Z7A6B8obM_fp-OPc6DmX45DA64Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/102432" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102431">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">💥
🧐
رونالدو، پسرش و جورجینا درحال عشق و حال در گرمای تابستونی اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102431" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102430">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=dPojsYLpWKc9vHa6jGiTU5ZNf63uM7GXKF3wiglUHhs0854vO41q2_9W5L0QlKydAzniwRLd23qgrArvwLvREESrfmnS2v_-H4Fubkktvq0qC-4mYqX5YTzxa3Dy5T8SJ0Pep95lC0KvW8z1pTp7aNSM-0fok91Hlz1DHgiNdDCGhStNKAo91m9gf2ZCpIp-Vx4T8taPE8VvGqJja8YKEi6dZoUJ5uzTqJe6orDc-xx_-sVb-pz493JFoALPd_K4JVu9csc7YkFJeHcyHIPfEgdxPYrAWBjSEMLuGt4dKq8Ow2y8NVN2-gXNE_HDGz4pi07umtCGiUzKVJipdPfC0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=dPojsYLpWKc9vHa6jGiTU5ZNf63uM7GXKF3wiglUHhs0854vO41q2_9W5L0QlKydAzniwRLd23qgrArvwLvREESrfmnS2v_-H4Fubkktvq0qC-4mYqX5YTzxa3Dy5T8SJ0Pep95lC0KvW8z1pTp7aNSM-0fok91Hlz1DHgiNdDCGhStNKAo91m9gf2ZCpIp-Vx4T8taPE8VvGqJja8YKEi6dZoUJ5uzTqJe6orDc-xx_-sVb-pz493JFoALPd_K4JVu9csc7YkFJeHcyHIPfEgdxPYrAWBjSEMLuGt4dKq8Ow2y8NVN2-gXNE_HDGz4pi07umtCGiUzKVJipdPfC0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
🎙
تمجید جالب کاسمیرو از لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102430" target="_blank">📅 17:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102429">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=E4KgCioMA80v8ulKQ_wPSAFCSx7gU1l7GujHCaGQh59H974pCCFMzOS53VV8iENv-kpLfmtd85lPYqU_g8_7VOOo9L1is1KF1q8bjo7Oz8c2paC5JYGP9INnoNHwPMTT6feWCvRPQtQ8ee7ki3hf21WYGVN7jy6RZbAGd845wDjjy4uDfaLnWHznmtHbEJ2BSTySKgeCm2V7jJjw8OdrUUx9ZVwho1CRe4EQcZlRncDSkF7StxZL9StUO_B_akTRAtWBImZGWdYzD8HWE3tCN4GNsyLrUo95Fa8mdXS6d8yvQ7E1cDtOjs_5oz-yR-vKcL1gdL3cp5g_du0ESm6DLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=E4KgCioMA80v8ulKQ_wPSAFCSx7gU1l7GujHCaGQh59H974pCCFMzOS53VV8iENv-kpLfmtd85lPYqU_g8_7VOOo9L1is1KF1q8bjo7Oz8c2paC5JYGP9INnoNHwPMTT6feWCvRPQtQ8ee7ki3hf21WYGVN7jy6RZbAGd845wDjjy4uDfaLnWHznmtHbEJ2BSTySKgeCm2V7jJjw8OdrUUx9ZVwho1CRe4EQcZlRncDSkF7StxZL9StUO_B_akTRAtWBImZGWdYzD8HWE3tCN4GNsyLrUo95Fa8mdXS6d8yvQ7E1cDtOjs_5oz-yR-vKcL1gdL3cp5g_du0ESm6DLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
یادی‌کنیم از بازی تاریخی ایران و قطر با گزارش جذاب عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102429" target="_blank">📅 16:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102428">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=BaePb7wHOXkTAE97xPGCN9939yaugNycHl0bB4TL1GcHrbGnQR_J6EUZjJu1BAyb5qlu0XLNGuKO3a_-8jTHiUl5ekvlze0oM-pS5k6spPvRm4LEj6k0HqrjeZHHAHagfaGNjrKfN3EfqdYb0oBtShegLn_YyeADX8U3mo3UYw_RSjYRKpHQeHIoSVC5lDc5iUHomnpmT16CPMnnoMV5_pw_yQ2ZZq87Vs3AAIQG6guwCh-DPVGGD-IAoRh6GaYBvwc9Rfp_1aNRSFX10R7f2Lgx6nyZ6iOzp__L5vNLtRrslKF_pRvQ62A3PtkqkJarRcdgOfQXQrCHR3qf3-HT44i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=BaePb7wHOXkTAE97xPGCN9939yaugNycHl0bB4TL1GcHrbGnQR_J6EUZjJu1BAyb5qlu0XLNGuKO3a_-8jTHiUl5ekvlze0oM-pS5k6spPvRm4LEj6k0HqrjeZHHAHagfaGNjrKfN3EfqdYb0oBtShegLn_YyeADX8U3mo3UYw_RSjYRKpHQeHIoSVC5lDc5iUHomnpmT16CPMnnoMV5_pw_yQ2ZZq87Vs3AAIQG6guwCh-DPVGGD-IAoRh6GaYBvwc9Rfp_1aNRSFX10R7f2Lgx6nyZ6iOzp__L5vNLtRrslKF_pRvQ62A3PtkqkJarRcdgOfQXQrCHR3qf3-HT44i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیاز بود یه آیتم جدا برا لحظات تاریخی فیروز خان کریمی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102428" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102427">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102427" target="_blank">📅 16:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102426">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102426" target="_blank">📅 15:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102425">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102425" target="_blank">📅 15:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102424">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102424" target="_blank">📅 15:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102423">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102423" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102422">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Et4l1HTESEJfFUDcDjx2caF52B_5YGldqa-XDUyKbL8J-7DgRykNbWfnTpO4E9lqrGJTyUaJdfAmNN3e3asD2fuReYHIAgeJCSe0e2gm92WsLOy_3ZCUeNLYleaFiTk4X1kBh6A6bS3mYy8sDsTpWGtMR3XVsssJfXRWQbqWQk9Fs4OwqvCMA79tKr5zvZO8-QbebUiiuDui05Zcu7lfRsHPHAsmywVeoa-M3DedkO18-6Rh0UPbz7HhoxC49TvkoI7PJUwahnoUUOerivUgpMjfJnVZ1JBZSDiHWoVoUe-mDPJIsM5a-QUM8g6Dya_dcMe_PCy_DVoo27Gfyr1lVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
لیست رئال‌مادرید برای بازی با فیورنتینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102422" target="_blank">📅 14:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102421">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102421" target="_blank">📅 14:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102420">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=ron8Cp-oWKt1G_ASlwKKlX5SEn6JE9WBLWz6lCHn0aUAEXURH2TcWQksQ_o4oqnHqIBgVWjzwyjcVP13nVRDviE3mpMZ_Nv-H18o8bI_fs18FHBYOgiJDjDIJLP86MdHDHt3L6_Zp4MzBjlfQ64ep9mlPK0jZEja4hUJK9fE1SFClawkuARLRuG1dutCIyRx395TCarcHJOd_1Gz3Q14v2OESKZYaBlSUJ22jhKeO9XcnnWxk3hhCqzCfM2O0W-GhJgvDjlxCe8QZekZ9m9Q_LwT1Y_PEnbr8rv5N-EasAO73GHHWE9AmGE6yu6Y5uG2B7eR1hiq3EhBHVcxOKy0HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=ron8Cp-oWKt1G_ASlwKKlX5SEn6JE9WBLWz6lCHn0aUAEXURH2TcWQksQ_o4oqnHqIBgVWjzwyjcVP13nVRDviE3mpMZ_Nv-H18o8bI_fs18FHBYOgiJDjDIJLP86MdHDHt3L6_Zp4MzBjlfQ64ep9mlPK0jZEja4hUJK9fE1SFClawkuARLRuG1dutCIyRx395TCarcHJOd_1Gz3Q14v2OESKZYaBlSUJ22jhKeO9XcnnWxk3hhCqzCfM2O0W-GhJgvDjlxCe8QZekZ9m9Q_LwT1Y_PEnbr8rv5N-EasAO73GHHWE9AmGE6yu6Y5uG2B7eR1hiq3EhBHVcxOKy0HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
✅
یوسفی: زمین و تماشاگر که ندارید، لیگ را پلی استیشنی برگزار کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102420" target="_blank">📅 14:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102419">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9889076a09.mp4?token=By8IBps84F05PXfdv3wHUq8W4-FjdCUBBdf-YaIh2aVQVVt_1SUDQkirHFsGxcm4M5wtRao43ZdFMHFGvyl4AsX7zvhMEEBPlcZ5Y_Isk3WRFDyJJSo52iLcuePPBeGUBX6u_Shfnj-1hOONmAnNs4OsnMsjrfo78ZtYJeqVMosoGtWAvXflbJB74ZMymiKdFXihYz3cNJ5rZ2f3EAeGIJO_I3Ai_Gqdf5ls_tpvKHE1zGEKcTtbH9fcaBS1PXpML6IbfH1beUJM2y0WNy5V42zGKJLUUvXmohTOP7arsrs7XJKAR1u5XUd_i_j5YxtVMm_sQEx8IKB46Y9aNTtNbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9889076a09.mp4?token=By8IBps84F05PXfdv3wHUq8W4-FjdCUBBdf-YaIh2aVQVVt_1SUDQkirHFsGxcm4M5wtRao43ZdFMHFGvyl4AsX7zvhMEEBPlcZ5Y_Isk3WRFDyJJSo52iLcuePPBeGUBX6u_Shfnj-1hOONmAnNs4OsnMsjrfo78ZtYJeqVMosoGtWAvXflbJB74ZMymiKdFXihYz3cNJ5rZ2f3EAeGIJO_I3Ai_Gqdf5ls_tpvKHE1zGEKcTtbH9fcaBS1PXpML6IbfH1beUJM2y0WNy5V42zGKJLUUvXmohTOP7arsrs7XJKAR1u5XUd_i_j5YxtVMm_sQEx8IKB46Y9aNTtNbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
💥
روزی که پیتر چک آماده ترین گلر آن دوران فوتبال میخکوب شد و این اثر هنری شاعر رو تماشا کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102419" target="_blank">📅 13:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102418">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5Juwqp-dVbKGQbm45IL7lfNcV69ACxlGpMzMbp_6rUHSwb9Q0TPT_3Yp9STYceG8Aho0mkjA-Ggh3xc3vDkeFWVOGDF4yomLkYn2IqWy6cP7I5hi5WP7v-Z7o1kkIegldFG6uxtvHq3wDqTDLK3WVdscqOHdOLyKX5qo-PsUi8lYN6-laAEAozTbgbJ4j_fAqVHBA3jdmk7dNRyY60OYyr1Oa62E3GNJ2meDCjyfk-1aBPjsKz11UdG4KAazFH7Tlq9j7mCsWYPTHrc-nyICq4BfPpLtJTnaI6Ag9zWVa_beBTMqnIwTtrTBJ0c_PDS2NiBIGKrbIJWXLKo3ZiAcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
کارلوس اسپی تو تمرینات رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102418" target="_blank">📅 13:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102417">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgKKgl-NhRWuXpQBiXRmbNriOy6FhDsn2ZkPV487VzbhHdLrctchyUO0cMEIt2SkmV9p0iFFxXgnWIPgHEdz378JaiHtmtFELjrScWVAY8PmGvZaq6RYVUkOcUC8rQ6X9YKAtgwLPYYAuSnLC9KjWS4WRKLiQG3d7P0Vz3jgk-g4To38zpjRqGOTvsPMyaJi5NbbdRj9CjRwJCSwXzYl3uhnhm3sW9ZCWBexiFOs_OQcSlFaSFFdUEj0iF6iRGuh_fbE3W0DfBfZIBBaGxE2YMKwRfRpgSGtrL021C55U4U0ln9Qt275oY-8YyAbApMFGg6tTEUpjBzTXFe5gwINFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
روزنامه اسپورت: دو باشگاه آرسنال و تاتنهام به رقابت برای جذب فران‌تورس پیوستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102417" target="_blank">📅 13:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102416">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102416" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102415">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102415" target="_blank">📅 13:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102414">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102414" target="_blank">📅 12:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102413">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🤩
#فوووووری فابریزیو رومانو: آلن هالیلوویچ استعداد برباد رفته بارسلونا در آستانه امضای قرارداد با پرسپولیس قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102413" target="_blank">📅 12:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102412">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102412" target="_blank">📅 12:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102411">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102411" target="_blank">📅 12:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102410">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102410" target="_blank">📅 12:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102409">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=RzCkqd1wndnwMQgUAB0b7tNjMm1N0Z-jLV6ij4NsvAWp4EKK3xcnLtHzj4iR6q80hxWwmbXKyXPux0We230jTzkej0muGtN0wenNU9T57Yns3vmcNWPbcWnfabHA2HSdWjeIYPE-x4XnawTfkgh8WQ9mtBejIBWa0UUb1KcLeQQfyTngoCqmrYzEo_uXquvDW7WmQjTDTDQHsfcwrei3TxjAyZ6GHEmpa3kXtYNMJjPUFv_EOThasMwhvPg52C1amhl95cfof7bbCEWYauRD0SQ8d71Y27Dt0Fg1Pu959gu-mOo80IusxhJ57-BYouEb_JVqTBs0eLoIsLmGze9dACU3S_-70HjPLrGA2J6VdHwCw1Jr9rbC9slRIeM_KdhXgp0v8IV_Ko6uvhkYhJ4aOpgIcWu4H6uxsOzvj6jlGNpbAAox2o6Uc63VVlDfxizrzZDVUNd7H_EyPMa_OkdfeQN_D2Na0wYOoflQD3A9k93b1dQ4ICfElg2U9YM6otKK3w99TSpX6j_BQXNjcABYgriKL8Q1EGM5vko25MQTUjkzE3KNkp8LYXV9oiUME0HXnQZhBB2GL4dtxO9mWkZGnEwKTjlK2NO9UFmh1aCKXIYDQ3bSzNpF7XQ5-kkmhgpQD1EihBG1SW9Il_cgV-P6I8VRRPblBicrIKhRkjY65aI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=RzCkqd1wndnwMQgUAB0b7tNjMm1N0Z-jLV6ij4NsvAWp4EKK3xcnLtHzj4iR6q80hxWwmbXKyXPux0We230jTzkej0muGtN0wenNU9T57Yns3vmcNWPbcWnfabHA2HSdWjeIYPE-x4XnawTfkgh8WQ9mtBejIBWa0UUb1KcLeQQfyTngoCqmrYzEo_uXquvDW7WmQjTDTDQHsfcwrei3TxjAyZ6GHEmpa3kXtYNMJjPUFv_EOThasMwhvPg52C1amhl95cfof7bbCEWYauRD0SQ8d71Y27Dt0Fg1Pu959gu-mOo80IusxhJ57-BYouEb_JVqTBs0eLoIsLmGze9dACU3S_-70HjPLrGA2J6VdHwCw1Jr9rbC9slRIeM_KdhXgp0v8IV_Ko6uvhkYhJ4aOpgIcWu4H6uxsOzvj6jlGNpbAAox2o6Uc63VVlDfxizrzZDVUNd7H_EyPMa_OkdfeQN_D2Na0wYOoflQD3A9k93b1dQ4ICfElg2U9YM6otKK3w99TSpX6j_BQXNjcABYgriKL8Q1EGM5vko25MQTUjkzE3KNkp8LYXV9oiUME0HXnQZhBB2GL4dtxO9mWkZGnEwKTjlK2NO9UFmh1aCKXIYDQ3bSzNpF7XQ5-kkmhgpQD1EihBG1SW9Il_cgV-P6I8VRRPblBicrIKhRkjY65aI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
علیرضا بابایی مدیرعامل چادرملو: بازیکنان را از پای دیگ نذری آوردیم و با خواست خدا پرسپولیس را شکست دادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102409" target="_blank">📅 12:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102408">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=rvMqFiD5rA1_ZODoyY0iQBzXrC0qeu9u8cs1J1WkNl7wzR5KWui04UBHMis9Ns-O0YViaf3G5MIB6AdPxmtB3DOUZ_9YDTln5miHDVCrWeAxt0wGjt3PruoVWAxSTaMzcfxcq_MWMi8YGk53VedWcOPLuouDH-sZtIa_13-LtAMA0roOz0c9ITSL3l8OxSl684NZma2j9hpAv7l16bLqBPh4gPMf7bUcZLCJ3AtWsdWXXWDvN0vedvGslIZwmkEYM6mw3kkTfeiROj19SjdUtFlfXCekRmJ2a1s4Tn_OPM1knMSmS0yp2waVrW6zl1Y-PVYDcnrN9z8VKymjuk_B8StZO40cgyBDouTvDJD-_lHw-dxoYA-EngEx4NMfeqF_gBWzw8MIfQhslVk1aICqIx9DFCTBvPypvHLO5t0O3ggVqy-YMzFoBfHXlr9HawiCdtfgc52kDT1T_i_VVhlABCGpQipa8Fo0uzmchguLSCHyErs8lEa7bVdoQQoQjOPzMNspx7JczIl4bfkZXmyGJ0r2Xb1VjGQsvgNE7X2F9RAEYh0fMfS9C2AgYEkfjxzRL5FnyMxr4qxrQGZZhgqlXth7vgf7rcFsPMXYQXEe1f27NeuhqrM10LCROcp1y-rTLv-_CGaBzo2ffWp5lmSOiEsKAn6bwDo_VPltWWVW5k0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=rvMqFiD5rA1_ZODoyY0iQBzXrC0qeu9u8cs1J1WkNl7wzR5KWui04UBHMis9Ns-O0YViaf3G5MIB6AdPxmtB3DOUZ_9YDTln5miHDVCrWeAxt0wGjt3PruoVWAxSTaMzcfxcq_MWMi8YGk53VedWcOPLuouDH-sZtIa_13-LtAMA0roOz0c9ITSL3l8OxSl684NZma2j9hpAv7l16bLqBPh4gPMf7bUcZLCJ3AtWsdWXXWDvN0vedvGslIZwmkEYM6mw3kkTfeiROj19SjdUtFlfXCekRmJ2a1s4Tn_OPM1knMSmS0yp2waVrW6zl1Y-PVYDcnrN9z8VKymjuk_B8StZO40cgyBDouTvDJD-_lHw-dxoYA-EngEx4NMfeqF_gBWzw8MIfQhslVk1aICqIx9DFCTBvPypvHLO5t0O3ggVqy-YMzFoBfHXlr9HawiCdtfgc52kDT1T_i_VVhlABCGpQipa8Fo0uzmchguLSCHyErs8lEa7bVdoQQoQjOPzMNspx7JczIl4bfkZXmyGJ0r2Xb1VjGQsvgNE7X2F9RAEYh0fMfS9C2AgYEkfjxzRL5FnyMxr4qxrQGZZhgqlXth7vgf7rcFsPMXYQXEe1f27NeuhqrM10LCROcp1y-rTLv-_CGaBzo2ffWp5lmSOiEsKAn6bwDo_VPltWWVW5k0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇪🇸
مشکل ایمنی ورزشگاه‌ها به لالیگا هم رسیده‌ و تیم رایووایه‌کانو نمیتونه از استادیوم خانگی خودش در فصل‌آینده استفاده کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102408" target="_blank">📅 12:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102407">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102407" target="_blank">📅 11:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102406">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262957043c.mp4?token=JKJGQlM-KUZniN2J2ID01KHpjg0pVbT2zNYV9KzW7EISyxjpLJ-xtikOg-bEmr4KEHpXjICJBiAFXmMsvmtfPP9VhJXv-7jObICEhaR7NAejaArYm5K9Vhwa3Q9GV9IkQJXvl6I93i1APksFPByk3byzq3Vd8egPUIpNtxSELGFX0KPLZIdIKefWT8yvk-1L2nFOjQFfDnhYka9wXTFcR85LjNIJZTdybPPiJpa_abJJgPe9nkTINDPuPgdoxcpTu2Q3QKiobIlrnt59IDRCOwc1--zxM7J5TI5skOirPSCQcplBwa9BDUVw_NEUWFCJxzErZXk8Ty0_jPJlLZexlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262957043c.mp4?token=JKJGQlM-KUZniN2J2ID01KHpjg0pVbT2zNYV9KzW7EISyxjpLJ-xtikOg-bEmr4KEHpXjICJBiAFXmMsvmtfPP9VhJXv-7jObICEhaR7NAejaArYm5K9Vhwa3Q9GV9IkQJXvl6I93i1APksFPByk3byzq3Vd8egPUIpNtxSELGFX0KPLZIdIKefWT8yvk-1L2nFOjQFfDnhYka9wXTFcR85LjNIJZTdybPPiJpa_abJJgPe9nkTINDPuPgdoxcpTu2Q3QKiobIlrnt59IDRCOwc1--zxM7J5TI5skOirPSCQcplBwa9BDUVw_NEUWFCJxzErZXk8Ty0_jPJlLZexlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپرایز خاص‌ ژابی‌آلونسو برای فصل‌آینده؛ رونمایی از ستاره ۱۷ ساله قزاقستانی چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102406" target="_blank">📅 11:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102405">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2180d890.mp4?token=dixHhu6i1-A5TtWfOHm8pKfQjKv0N3Q5sci44joN9voZq8c-bC25gSwSogV_MAZCAqRAl6G11cjo_M4UTqFioWh009PEV2DhyPonblgeVDQSgh3Byh7GM7ld7a7jOsJo5WFuIeCIxGaNNm2Si0-5-qViu42L1Riwu7lvludKxjNzzFb-bb8U41gGC15mg709gBnoPTwj8GjTFhigcs-lIA3tdp1CsO9uzbjfuOGga9pCEOt0BbD4dxXdLTSAOmY2wjEPmKruZuRcafQ7cXECb9R-CU3MGgjcj6CHTwGmn9nUMhFlFCIN2C4KIZXATRzdIBukEyfePfxJy6joR7FZRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2180d890.mp4?token=dixHhu6i1-A5TtWfOHm8pKfQjKv0N3Q5sci44joN9voZq8c-bC25gSwSogV_MAZCAqRAl6G11cjo_M4UTqFioWh009PEV2DhyPonblgeVDQSgh3Byh7GM7ld7a7jOsJo5WFuIeCIxGaNNm2Si0-5-qViu42L1Riwu7lvludKxjNzzFb-bb8U41gGC15mg709gBnoPTwj8GjTFhigcs-lIA3tdp1CsO9uzbjfuOGga9pCEOt0BbD4dxXdLTSAOmY2wjEPmKruZuRcafQ7cXECb9R-CU3MGgjcj6CHTwGmn9nUMhFlFCIN2C4KIZXATRzdIBukEyfePfxJy6joR7FZRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
آماده‌سازی استادیوم نیوکمپ برای فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102405" target="_blank">📅 11:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102404">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31c9897d6.mp4?token=th4vvBgqAtFXv6vF3S62AM8UIMFK2mYtjfOco8zOXlQ3YgEsLK0-fioR1RRMpq_IQQvpGRXzNc9gW58M0iOsZmoZ4AqBFAUno6RNuygRGZN4XBJmSs89sqqj6MNrNwIxT3_d5Eid7AMncX1we3yldlSfuyJGM9d6AAR1G80R85JexrTyCtRPDa2b5xlR14ikfQeUBL8svYY1bo0DDHIGkJPY9hqShCdslBiITWEH7rmYED4c0NWlLqjk7xCw2wVwnNzTjlCkuNBM6jQ2LPNynI5w_FRtGeEiEJzxTjL_sZ_ZzRnvyT-iBq6mYkyV9wsT175XniSBoUA9Au2A12Fh5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31c9897d6.mp4?token=th4vvBgqAtFXv6vF3S62AM8UIMFK2mYtjfOco8zOXlQ3YgEsLK0-fioR1RRMpq_IQQvpGRXzNc9gW58M0iOsZmoZ4AqBFAUno6RNuygRGZN4XBJmSs89sqqj6MNrNwIxT3_d5Eid7AMncX1we3yldlSfuyJGM9d6AAR1G80R85JexrTyCtRPDa2b5xlR14ikfQeUBL8svYY1bo0DDHIGkJPY9hqShCdslBiITWEH7rmYED4c0NWlLqjk7xCw2wVwnNzTjlCkuNBM6jQ2LPNynI5w_FRtGeEiEJzxTjL_sZ_ZzRnvyT-iBq6mYkyV9wsT175XniSBoUA9Au2A12Fh5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
پاسخ‌تند و کنایه‌آمیز مهدی‌رحمتی به صحبت اخیر معدی‌قایدی: بذارید تو‌ توهم خودش بمونه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102404" target="_blank">📅 10:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102403">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
✅
کیت‌دوم فصل‌آینده منچسترسیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102403" target="_blank">📅 10:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102402">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/869e38d1a5.mp4?token=uVbMY4907IGOhlfBahJxTW_ZD-CnzZG-J-AM6G9-o7ctr5JFd1XFZ1Vkwq4T1IvQ6xnUT7vlwSv0pZDhCbXM0unV5ItFMPjiNRp85w_jSFQoqoqixGi2ca4R-O5SEHbGpIkAc9-IPdsyxn3nRX1nY0C3s64wdHiGVK28B3aOuA75bXjVlk5TVksLpOvRqd82Pui8_JDHihbNxiRmaAjMARDwC6z-O66k434oI67DJQPm9iT-b_2IOVt7Awizgj1IRTYfH35_hxuejUEC-QP7GeRUjyD3Rh-Ez-KPRxlkxJWm49GH9ktbKeW-NwGlJrTlS2W6iNU2fMTDnVJG8I-0E4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/869e38d1a5.mp4?token=uVbMY4907IGOhlfBahJxTW_ZD-CnzZG-J-AM6G9-o7ctr5JFd1XFZ1Vkwq4T1IvQ6xnUT7vlwSv0pZDhCbXM0unV5ItFMPjiNRp85w_jSFQoqoqixGi2ca4R-O5SEHbGpIkAc9-IPdsyxn3nRX1nY0C3s64wdHiGVK28B3aOuA75bXjVlk5TVksLpOvRqd82Pui8_JDHihbNxiRmaAjMARDwC6z-O66k434oI67DJQPm9iT-b_2IOVt7Awizgj1IRTYfH35_hxuejUEC-QP7GeRUjyD3Rh-Ez-KPRxlkxJWm49GH9ktbKeW-NwGlJrTlS2W6iNU2fMTDnVJG8I-0E4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
درگیری شدید فیل‌فودن ستاره سیتی به همراه مادرش با چنتا از مردم در یکی از کلاب‌های شهر منچستر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102402" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102401">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0266060c.mp4?token=FBQxfNDK_IVxM7TZnw3273tsFmLr80GhJqPoJlGcEePy7Bg81pSbkn7S4xxt7XQtkXjBpSR4YErKHoldLljxDVwv9z0wxkkTKXMnRmv1ia1LN0czZFicO9ToV9i0xK-YsYwF6dFMh9ZkoDKny2VkPKDX9yKfGgQEjRQyVGfuYWcnG0L0sXT1BuXlU47Ve3FIYAUfq3s9_nAtrlM2zQSNBseKNiT6JYvDS431aiDuLRPQHCs0xTdV-SBf-BTyelpQAJSPvKJnlD7K-tjCw0E0wT5KGrTv9fCOn0fYPfpx7WnqxjrWSNBje02v-u8wSFTBjkQVoFLc3ZBNi8AkuIXwcJFclPNbMDtOCxaBLymSJ9pRkmX9BlFWPbXKSL7gWfY3NhAI5CneV21aCUm66Qt4PY2gabVaxBQzimhiUqh2CO3FOWDl4Jy5eo2MeGju-9QI8jhHZr1UKyZx8V9Qj-p0nQsuWb-snPFaUFpQYGtR2t5WRE39q0u_eOoN0bH--twpaT8nAfAJHxXZX5mx__qld7z9WgCOp9CsLl3-LsKNIYnffNmZPSRiWDIykCycNATsTaCF5j2NTAnXqdXU1m5WmkfNFL6E-oIRTEbj4kU2nqYRHWJV9Io_zbOwrO4cJ8x_AMpB7u0m5KS88aHc8g14TMifdlDuIfm5Y9EFqjKPWrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0266060c.mp4?token=FBQxfNDK_IVxM7TZnw3273tsFmLr80GhJqPoJlGcEePy7Bg81pSbkn7S4xxt7XQtkXjBpSR4YErKHoldLljxDVwv9z0wxkkTKXMnRmv1ia1LN0czZFicO9ToV9i0xK-YsYwF6dFMh9ZkoDKny2VkPKDX9yKfGgQEjRQyVGfuYWcnG0L0sXT1BuXlU47Ve3FIYAUfq3s9_nAtrlM2zQSNBseKNiT6JYvDS431aiDuLRPQHCs0xTdV-SBf-BTyelpQAJSPvKJnlD7K-tjCw0E0wT5KGrTv9fCOn0fYPfpx7WnqxjrWSNBje02v-u8wSFTBjkQVoFLc3ZBNi8AkuIXwcJFclPNbMDtOCxaBLymSJ9pRkmX9BlFWPbXKSL7gWfY3NhAI5CneV21aCUm66Qt4PY2gabVaxBQzimhiUqh2CO3FOWDl4Jy5eo2MeGju-9QI8jhHZr1UKyZx8V9Qj-p0nQsuWb-snPFaUFpQYGtR2t5WRE39q0u_eOoN0bH--twpaT8nAfAJHxXZX5mx__qld7z9WgCOp9CsLl3-LsKNIYnffNmZPSRiWDIykCycNATsTaCF5j2NTAnXqdXU1m5WmkfNFL6E-oIRTEbj4kU2nqYRHWJV9Io_zbOwrO4cJ8x_AMpB7u0m5KS88aHc8g14TMifdlDuIfm5Y9EFqjKPWrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁳󠁣󠁴󠁿
نظر سرالکس فرگوسن درباره‌مثلث جادویی بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102401" target="_blank">📅 10:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102400">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f864b5c9ce.mp4?token=YdttLpynY98Y30ewn4yTeb7h0Klk1wyNbINbd2dTg0hwryArSuTH7_PWmd5rSCfDAV_nWTso4a44VloIKxqXF6nXVk8Tw9L2EtdNd1q28E4whSFcNiiUBChYfc9vSu2XE89U1J1ow-IUdPpi0uxOB8nU3QhHqxaV0TE5ZeqAzAbaT3hZ8F65GoXeA7Bc0whabnGA6coNa3xNvpVWQGSY1ypcLSFQHvmr2L3Ay3XdaTYodQeaeBOglaF7FZG0dgr9yvmlDfVWT_TlNLElXylF0a6zLnx9neln5-pTTc3k5ZyGZzBtAoqFEl2TbWbrH3thKVvUfmGAsHwvMch_pVJPupNHStFJ9H0JjDlFm0SmfBd5YSaAcbu5RKADw5c-LCOs-p_oeiQugIuURh1391pOgt4ZR_Vdfnt9pePH99bXl5Y5nZTqY5HmnwC3beZjOb_hLQ9YCaHEC8Dg8HmeM5IGg6O1kbcCm7oTrzmo3mtQ2Y-PwxAiDqOtkv-dCDqZcdPcQuiAuOHsJDCLEVHWU146rd8AXfYfC2emdjQ1CahGM37Ix8m55tArwcvDmjZFAIMYUANN1YW-YYplAg1obbPbCeK3JWST03Mjsm2guUxe90Bj7762CKLegsWFBdl70TsW3fjuR1ysUV136UmpF4fAEt3j5nFVOCwjgZNlhxzY94g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f864b5c9ce.mp4?token=YdttLpynY98Y30ewn4yTeb7h0Klk1wyNbINbd2dTg0hwryArSuTH7_PWmd5rSCfDAV_nWTso4a44VloIKxqXF6nXVk8Tw9L2EtdNd1q28E4whSFcNiiUBChYfc9vSu2XE89U1J1ow-IUdPpi0uxOB8nU3QhHqxaV0TE5ZeqAzAbaT3hZ8F65GoXeA7Bc0whabnGA6coNa3xNvpVWQGSY1ypcLSFQHvmr2L3Ay3XdaTYodQeaeBOglaF7FZG0dgr9yvmlDfVWT_TlNLElXylF0a6zLnx9neln5-pTTc3k5ZyGZzBtAoqFEl2TbWbrH3thKVvUfmGAsHwvMch_pVJPupNHStFJ9H0JjDlFm0SmfBd5YSaAcbu5RKADw5c-LCOs-p_oeiQugIuURh1391pOgt4ZR_Vdfnt9pePH99bXl5Y5nZTqY5HmnwC3beZjOb_hLQ9YCaHEC8Dg8HmeM5IGg6O1kbcCm7oTrzmo3mtQ2Y-PwxAiDqOtkv-dCDqZcdPcQuiAuOHsJDCLEVHWU146rd8AXfYfC2emdjQ1CahGM37Ix8m55tArwcvDmjZFAIMYUANN1YW-YYplAg1obbPbCeK3JWST03Mjsm2guUxe90Bj7762CKLegsWFBdl70TsW3fjuR1ysUV136UmpF4fAEt3j5nFVOCwjgZNlhxzY94g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
شباهت حرکت‌های یامال و اولیسه
🔥
😮‍💨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102400" target="_blank">📅 09:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102399">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5630cebcb5.mp4?token=BjjyH5byYJu7parSGbVxgEYPG96Rz6B8P2rOojU0bJN4w6BDsfKJbRil-93fHSqfF09fbh5UNJSV-nLDLjP8nS5RhtbM1Gpw-Ss-9JpnmzDZ19wl-XDquTncj2_G0oWLDaJBd-yMEUpFvZTadHMgZPnxDrfRSc6yAOrvy7hI4MZnB4hil_0V4cvKTIwDMsIhLwXDioBaHkWyZacB3pn57A3XhgYYSzKUMxTxOTHCPDdkQ_zoWm9iEO0mrEgHZgv2zXUVMR65SdRurhpG0FqJfnnzXGwhr_k4mdKvbxVn_1MfYdN_QQc0cLEJXetjkXqbj5pd754ge6Jzs2ZiFBicYUiXo1KkNZ4p6A1TjD2kTvq7dgg2LkVPKmln5lPfl93Zf_ZgwHaEGdgNHXItEvw6yhldOnjJDnGqJHz4oBYCLraX9itSfTxaL-QFaimSMXvdFwDvReFIMwu_HbPzGlu3SwXswSIVVhEnUJ1u1Jx0MzK4g5s3s4VqUu7URkSUHJdRnMDIhUlQYT3LktblNNFaf8VIVeJO-QcMPW_lTX6rn-PMI--wb_axYJ8F3fGlU9EuNxqxFIG0y0mnzLwUkb2tATmaN2RwLL57aFS4tM5IRZkmDCOUFi-J3nqbtezJccIuYfOmLW6nEU87Puh-LbppMjmhCFOkN34oSEmSdCCCyaY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5630cebcb5.mp4?token=BjjyH5byYJu7parSGbVxgEYPG96Rz6B8P2rOojU0bJN4w6BDsfKJbRil-93fHSqfF09fbh5UNJSV-nLDLjP8nS5RhtbM1Gpw-Ss-9JpnmzDZ19wl-XDquTncj2_G0oWLDaJBd-yMEUpFvZTadHMgZPnxDrfRSc6yAOrvy7hI4MZnB4hil_0V4cvKTIwDMsIhLwXDioBaHkWyZacB3pn57A3XhgYYSzKUMxTxOTHCPDdkQ_zoWm9iEO0mrEgHZgv2zXUVMR65SdRurhpG0FqJfnnzXGwhr_k4mdKvbxVn_1MfYdN_QQc0cLEJXetjkXqbj5pd754ge6Jzs2ZiFBicYUiXo1KkNZ4p6A1TjD2kTvq7dgg2LkVPKmln5lPfl93Zf_ZgwHaEGdgNHXItEvw6yhldOnjJDnGqJHz4oBYCLraX9itSfTxaL-QFaimSMXvdFwDvReFIMwu_HbPzGlu3SwXswSIVVhEnUJ1u1Jx0MzK4g5s3s4VqUu7URkSUHJdRnMDIhUlQYT3LktblNNFaf8VIVeJO-QcMPW_lTX6rn-PMI--wb_axYJ8F3fGlU9EuNxqxFIG0y0mnzLwUkb2tATmaN2RwLL57aFS4tM5IRZkmDCOUFi-J3nqbtezJccIuYfOmLW6nEU87Puh-LbppMjmhCFOkN34oSEmSdCCCyaY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شیرجه زد، گرفتش، زد زمین، شوتش کرد!⁣ جوک خنده‌دار بیلی مک‌کالاک ماساژور سابق چلسی درباره‌ی پتر چک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102399" target="_blank">📅 09:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102398">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqbsQx9wtM3TvuXkEs69JE-oMUdIAC203ZN2Uzn2g0EtBKEKtIr_QIk3FJ0T9HIJThguVEcHNRDzs_27gAMihsgnEmHq69L44tRRKhdjCo_md_Ydgy7r7SXMOwu3ILcyUX_OgLVW2T9Ersosh_FGcn7H37MTcvH9qEuXY3g03btSHpRYnkjnJMWxRKh7uMzpGZhCUCIMrCV5Z4nWzLmcD0_R8W8J_fao1QUbsqws_rr55S17NlkoDepcFI_5NazAH4QEzrOrY8DqOn89xDuslcJekbuUtgs9Yoc70kYfslXfTxZWmtwOz4j13BFsz84BRpflXTEg-_ud82iPDzNVLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
🇮🇹
لحظاتی پیش، فرانکو بارسی، اسطوره فوتبال ایتالیا، در سن ۶۶ سالگی درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102398" target="_blank">📅 09:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102397">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d54a6dc02d.mp4?token=qQ2bGCTIwl3inGIQoIP6L7DTxVs-WiS1XV1Zc8ZNE6AebzgeFoZiUQXcKnphGiw7YNvWFqG6iikp7L-nUMTuhAqiqlSW5XuvRjoOxLe-7K13Lk8-FtafBtV9Wffmg6NmaaE7J3Pvi0o0jydgXtpMADSC3aHNfOtRzGUF4z67AFdTQJ169gSR9DteCmXx9r1-rqmep-dw4QElM36-_HQNI9LzJg4OLcfX-kzTjXFBIfpueWgkOzQX-pkQAOWqGGfCl4ilg2qdtZjOUvVQGmWG2obWSRrmYKzeCD_yolqKr7h27_4ipjAsIplMnXNndMMs2Bx3l9o1xPOvGJ8Ou0j6zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d54a6dc02d.mp4?token=qQ2bGCTIwl3inGIQoIP6L7DTxVs-WiS1XV1Zc8ZNE6AebzgeFoZiUQXcKnphGiw7YNvWFqG6iikp7L-nUMTuhAqiqlSW5XuvRjoOxLe-7K13Lk8-FtafBtV9Wffmg6NmaaE7J3Pvi0o0jydgXtpMADSC3aHNfOtRzGUF4z67AFdTQJ169gSR9DteCmXx9r1-rqmep-dw4QElM36-_HQNI9LzJg4OLcfX-kzTjXFBIfpueWgkOzQX-pkQAOWqGGfCl4ilg2qdtZjOUvVQGmWG2obWSRrmYKzeCD_yolqKr7h27_4ipjAsIplMnXNndMMs2Bx3l9o1xPOvGJ8Ou0j6zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت فوتبالیا اوایل هر فصل
🤧
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102397" target="_blank">📅 09:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102396">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e396ec62ed.mp4?token=iDMiJ8MLBAbIRZVNpMhmDH5dn11D1YrSIF-fWG9vm0TDi5pF8zI0sBc-Sa8p9AN9fplrYLejTfWJQDvdAs_c_1N7mqgB0V9V5WJFHsJzJ0CVzZjYxcwqUBWbMyVtHKIX4Z1kSx17CdGUNHolEQ1NxAXy2V89lvfZGR32WnOzSxHx5ghSUmP8rM24iYlWsVFTlBO-aobCwitX0ZRijbvXCNLsRI8DiRpiGQG4P8Zf4qGeY65TtAmbyVaMzt1VO-btEiJJ3zimGQAORUESrgN6uMnet0tTxxBridye7Nlcoi3gMeToF-0AmL-a9g11TL2ICRo6hgvqiD5kNtxyD8p3Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e396ec62ed.mp4?token=iDMiJ8MLBAbIRZVNpMhmDH5dn11D1YrSIF-fWG9vm0TDi5pF8zI0sBc-Sa8p9AN9fplrYLejTfWJQDvdAs_c_1N7mqgB0V9V5WJFHsJzJ0CVzZjYxcwqUBWbMyVtHKIX4Z1kSx17CdGUNHolEQ1NxAXy2V89lvfZGR32WnOzSxHx5ghSUmP8rM24iYlWsVFTlBO-aobCwitX0ZRijbvXCNLsRI8DiRpiGQG4P8Zf4qGeY65TtAmbyVaMzt1VO-btEiJJ3zimGQAORUESrgN6uMnet0tTxxBridye7Nlcoi3gMeToF-0AmL-a9g11TL2ICRo6hgvqiD5kNtxyD8p3Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
نظر پرز وقتی مورینیو میگه وینیسیوس رو بدیم به تیم‌های دیگه تو این پنجره نقل و انتقالاتی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102396" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102395">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmNEk7mqT64a7caoKZqbjX78jN70XywplfknhqyxD2yQLHw_DCfrvWC7A251ffz5a5RA5IQXdjGUU3rYW5xN0u_pKV5chW38vHdXrsne3aJ_NxvPOW3UTQvCOZoDfZqtzIbY-bLB9y7JvSkG0XuVIobmKCDmM1KaHsroBNr6zuiRurh5iTvb9Jz5fT9NibgclCYE4p2ZvWYBytNzmG-yT9-7sLsNq8PVqDeaLJvOWfM1UyJVpw3QZ8THNARy7Los5wNIYbBTs_xJZygQJXVfAQebv15XRgNj9Claom3TcOOOv8omKArupny7nc3v5IKs6lUSsF5HlBjrmldeYRzm2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
رومانو: حاضرم قسم‌بخورم که دیومانده بازیکن رئال‌مادرید شده و فقط تا وقتی لایپزیگ بازیکن جدیدی نگیره قراره رونمایی رسمی انجام نشه. اگر این اتفاق نیفتاده باشه از حرفه‌ خبرنگاری خودم کنار میرم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/102395" target="_blank">📅 03:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102394">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIyXc34ZzWlRpID-eQ89klcQZP7bDN7aew-pefVMF36Fu_94Wfxr0dkfUxJLD_E4WpNkRk3PcmZRJRLHzHRRS48pHWOSFkp2Ycr8gEgFCdJrCR_lRhvQWjl0EKBWKbFEPCUJV0y-6JLzCDj8eaC73RwhLOS1QEIhkrfg05VtXzlDVi-4rBlydX7imURSkcNFF_zxVDSM6ThvyvX9UuSiOy4XcU1AgtbYd1V07oyUBmP4esaKMkT-Fc5OzNq2uYCah0CY2HZjPLqO-sXZxD8Tcw1R_X2BPZ7x4yPqfJ8z2T6pQGFpt-sWu7FcoL1M94L_ESTh7z88YfViReI52Iynug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کاسمیرو:
خوشحالم که اینجا هستم و به لئو مسی کمک میکنم، او پادشاه فوتبال است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/102394" target="_blank">📅 03:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102390">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VtRAHbFi7tDM72BGozdQHG16v0321tLa0xy891ShQAygO3aSG4M8F9NLpg58efasEUBlRRmlsng9ThyFvQK9Y6NLkfiZJoN_AdZYzl3XPuM9lKgB5peT5aEjyMQ-hIrg66WZ_5iJAVpc5-YKLxdeFYdfFT2AjQnxVJZkoblwi92hNUzgn1Q7QTtGWYQ97FvY-3U1c-JOvO-vurTk4lhulWIYdAeiaJC7pW-atLIFMQO4y90usUmUGNlBxkbttRviaslJd5yUj3NJ3Q87ibEPN69HSiz62qxeCm_cm99hVoe-u0KRkzUhFbAGDLNWJ8XV20l3HDuGeaWO6PM0wRhgPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qm6XSPji5R284gXNQFPwGgnpIK3EBz2OdkzRmNrtlHSnGeRuLqnlL9afvg17_Bi8VVzRgl_RuWnKcuSyKzP-ljqQDFzw2PPFANaj9eXUu_tJGNbuXBBP2-gXmdV6ugKTtqF9zuA0LJRtnhcgMZ1ul_Mf608svojysZuyHgihvL_UsDUKnACHKQ4YeLDTImX7ogcooF8dPWQx7GK7S5dWkwpEC7rMcUetonBGAoa70PoZHAtcL8Y-DAgANDcfKXFmB8eIcOzb2eOt1GIu3dVqo38KZY3ghBevY081x7nWcrnXEPusFuQ_Fifc4MPe8uLZGeVtyf5MAdmHf_XTYJvFYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eXFSa4tE_vIC5sO9LwnJuBafPuzUupacBUQxBf_BI9kObOtk-_BNWZAd8FzpjAuOmuml63kZSj4_wTOLVxYLauYIETkmmivFUuArm2UnjA4GD0ChVx4U1LxHFlBdecjpj05WrhlTDwgicAUVHUyOXeqNqGbT5L_UNIEdEfIJs77UMzIQZMDpmK_0SJ0PkuzyFqbjTW2iIXqCEdFxfADE7m2KQgwqeXjh8p7gwBwXiD-VQOhEqJfWPqMUVMAEuhmLL3t9pRhNo0AuwFlcDAIM4VtXVKht6V116HyeaM4MaxlDzVo3WU8AJ6AFRvFMRq4mCIWp7MyM7Hzw6zKQx7OpVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UPhWNuXEY_G5YQvSAgierKFSYUWeuvsujyTcQbWAI6_q_z7xTpr7PhX8ZxajB9rABH6t3TzGoYrX3fgj9AyySRlO51FdSIpJLvgaAo8TAo6CtQ7cHVoUne33CFUbgcMxEKWqKJvfy0ErVloneO6wwvN_Uan1gYrv8qQKozLYN7Puu9eUQfyCIdUfqlN95lKmtAEGZ14UQt60pDzHYIktCdt053j7PmhXox6BocpNMN2ghNw7TswZIzukD3YxCxIW-nqtPkCO1TbCUCIt788zOd37fFiiU0s8pRIOo9YioGbVadDh4nb1fnXJT2rJnVpLgdwXjFGom9tEaHSc3hBXTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریس و جونیور و جورجینا رفتن عشق و حال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/102390" target="_blank">📅 00:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102389">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/511459b235.mp4?token=BpZGaIWpLHDTKRC6pQkzw_O81aPZlDfCTGwr1TaVS2pASv_DSsX0Q6DWoHo3qazV-VuPSGgcEziDYtw2EUuvsvBy_MCyj-_hxYM3A8TVUgYZJnP0L9x0jhBgnBtXlCqRyeoRkA2f8Zx0MyAwYG19wC8LQDUnvFtv09hDnv6VdBWgOtRuh-l4QCpUm_m1-8yCLwI0F3Qt3ZKKx1_0lOM8AExao3C_PBFwtd_3cfMQdS9kTm2wOoj5_niZd3Qt11W222YyzzMOMRphefMenOlaGdj66sO90CbRzLzz_mvtC0-JNkd1NHw3qvR9sOjG5XGbcxa2qSzkdLzWfXiqHhAdUJtbxw-Mv4lylyb6WYtLY5VUK8VfHFrabobMYlLskDx8UmeK8XWnUROyzXEEg8inQIWaRqWAJ_fFvF9_Ktk-j4tVLpk77UURIEL2QhWUAakXc4Q7AMzVBkrIEKva0VKqvTbcztAI9mMZJAIclbV1mCB8WXiTYT3gzeskkNKIkBZNrI3_JXbfmUGjmemZ48x5fRsZjpkNyXOzwxkczPCO4J6YgACExysDhdFtk07QFlHUkpw0V6qy6BdQt-NK9LYh9Om2nMdcv0gkpenDRbOntuQ1ObbZFbZE0MrEWWCdlSBwsELFNHtDQUf9HV-jxogc6t3cbH0RPmfyrKrHlVgMocE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/511459b235.mp4?token=BpZGaIWpLHDTKRC6pQkzw_O81aPZlDfCTGwr1TaVS2pASv_DSsX0Q6DWoHo3qazV-VuPSGgcEziDYtw2EUuvsvBy_MCyj-_hxYM3A8TVUgYZJnP0L9x0jhBgnBtXlCqRyeoRkA2f8Zx0MyAwYG19wC8LQDUnvFtv09hDnv6VdBWgOtRuh-l4QCpUm_m1-8yCLwI0F3Qt3ZKKx1_0lOM8AExao3C_PBFwtd_3cfMQdS9kTm2wOoj5_niZd3Qt11W222YyzzMOMRphefMenOlaGdj66sO90CbRzLzz_mvtC0-JNkd1NHw3qvR9sOjG5XGbcxa2qSzkdLzWfXiqHhAdUJtbxw-Mv4lylyb6WYtLY5VUK8VfHFrabobMYlLskDx8UmeK8XWnUROyzXEEg8inQIWaRqWAJ_fFvF9_Ktk-j4tVLpk77UURIEL2QhWUAakXc4Q7AMzVBkrIEKva0VKqvTbcztAI9mMZJAIclbV1mCB8WXiTYT3gzeskkNKIkBZNrI3_JXbfmUGjmemZ48x5fRsZjpkNyXOzwxkczPCO4J6YgACExysDhdFtk07QFlHUkpw0V6qy6BdQt-NK9LYh9Om2nMdcv0gkpenDRbOntuQ1ObbZFbZE0MrEWWCdlSBwsELFNHtDQUf9HV-jxogc6t3cbH0RPmfyrKrHlVgMocE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل فردوسی‌پور بعد از کلیپ دست‌بوسی که ازش منتشر شد یه کلیپ گرفته و میگه ویدیوهایی از گذشته من رو گزینشی منتشر کردن. هجمه عجیبی علیه من اومده! من اگه قرار بود چاپلوسی کنم الان تو صداوسیما کار میکردم و نَود رو داشتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/102389" target="_blank">📅 00:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102388">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2KDK8aHTKAYzxXFstSsn95EwJd_84FPd6JS1GvspJs08MaBtC36LNrOMarEUhS-ZrHfm1s1EVq3lGeujrQ5XKLknI2XHMBWpEy-dcILdr945glwdkWw1f6X6eSHo2LaqwIwtl4aBWvQ0z54uW1bKLTIwKubeEiSPVMZLwOXJrFGYpXFSRTpdt9eZntwR-vGNGQHe4POaS6IIWn-abgG6dWZ_gYQMLlg2Qy_UmqiKWc4-gR7o201fOq_UQgXP1J8p2tEiRJViqViehfVjyTAoQph-zLpQcjSlCb0j2fhDdMPd2DSVR8c6bQgSqRnUZpD6kgdXonI9iXKKR4-qlsEDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری: کارلوس اسپی شده با بند فسخ به مبلغ 25 میلیون یورو به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/102388" target="_blank">📅 00:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102387">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8dn9g1g1tHsgyqBOhhHpp00xzMhfgJ-uoYU-jxQMVw_kTRxnwbzoSIm1nKvosvjkyawU9XqrGz_dwbiZmIbJEq0gmiIHg_JauKb_FFw2cxsmfn-KXu2b3U7oqP4WjnBsedVHbjNAUKNdu0tDzsDbql4vSddRR7izy8kYE5fxMIdKQZYVydw-DR1oZx8BO067CSGlON8O1Zt-xbKb4_YTDNH7f9PB7mzkfQHuItKxbY_JQy-KALoCTOnBUp7p7qk9t8YIJl5fc3gNtVkio5sZJVAoTfsWu75xaqIJBE5MWM3lZujcSwIaYx1bZ7acRCsgnlhleUyHXUjEjh1tnfHIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری بلینگهام که رو دستای زیدش خوابش برده.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/102387" target="_blank">📅 23:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102386">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae65f1051a.mp4?token=P5B-0i7h1KAvUtdqDKLFfgKR0064RQDI--kObo5ffiT5V-38v1P6xV7T2bWKbthB1UqEfMyDXSjErBcE60Kzv_tAcl8ZSARB9q5xCr3SSGUT8Ya9ykKIVYV_QJK7ohKFCj7_7UlW0mAknkEpXxYRxTl1-hA7NnGrdB5CIpJy7vO-4Ioz-RKFbHmrN3f93bu7tXuDioPhl220HGAcKsGvB6JKhMd6qOzPZi39-CNMMCoRaXrHiqt5pFe4c-Fx5CM2HNw9IGOAdKKQu_CYalAsamO0HbsjTSIH9nPb9tM5CVD4ZJFaS9lhPuVkemPhO5roTuEUKDcI18LZ8H8nkymYCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae65f1051a.mp4?token=P5B-0i7h1KAvUtdqDKLFfgKR0064RQDI--kObo5ffiT5V-38v1P6xV7T2bWKbthB1UqEfMyDXSjErBcE60Kzv_tAcl8ZSARB9q5xCr3SSGUT8Ya9ykKIVYV_QJK7ohKFCj7_7UlW0mAknkEpXxYRxTl1-hA7NnGrdB5CIpJy7vO-4Ioz-RKFbHmrN3f93bu7tXuDioPhl220HGAcKsGvB6JKhMd6qOzPZi39-CNMMCoRaXrHiqt5pFe4c-Fx5CM2HNw9IGOAdKKQu_CYalAsamO0HbsjTSIH9nPb9tM5CVD4ZJFaS9lhPuVkemPhO5roTuEUKDcI18LZ8H8nkymYCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
روایتی جالب از تمرین‌های پاری‌سن‌ژرمن؛ جایی که حتی امباپه هم از دقت باورنکردنی مسی شگفت‌زده شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/102386" target="_blank">📅 23:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102385">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xhabsr6_QAiAyGveh8IRx253agS3dYna86QC0SXDsy6CmRV4_MQ-ZS6pHRF31ggIkaf8E3EPDXYLYL11cnqboZ4sPscmxWEry4B6qhsSK7Pf6ChHEvRkdzV94zKXa0O3hEjXY0NDGQt2g1-rM6KrIE8BUHILtKalxZiAf-hQGE8-tGm9y9W4pBpcSn27HpdTqrm8WcxmNEoP6UIqkDGSx6mQF0BqWnPrWpuoKFwYvUZbYIo31sKiATsyUY9VVTjaNbKgB-mWYg1L8oa2PjvsLw9phXUi8yRD2lcMS3O0weI_Z1Wkl-EfSU3p2hPwin-1M3TmF1GXrKsFhIllUB-vvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اولی هوینس:
ما حتی به امپراطور چین هم اولیسه رو نمی‌فروشیم چه برسه به رئال مادرید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102385" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102384">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oy-ooYrCjnX1sZ_kdYj1fZVyZGMbpogcn-0WGDMDexVN4mLC2EdvkR_2E8Z-h8aIxUIFVFpVLkbqksUUddLBqiMa5q94RfDLgBEE8jALL3lhstKCzOFHnW6i93v5WyVpw-tJ3MpFa3uig9iJ806NGcyDl1sNuPQbFLOLxqvSTmJ4Zj4o4ZnXt92xJiHe1voa8w8BvbVGeTw4KgD5kdjEHp7Fmgvv3txBPJW9C-MZLJyWfn1A0u66EZtqEm8kF9z7g8ySz8DISY3hq98UVfWmfhlEYOUWuBBdr_HnOkrxs2ZfvqvHNNZj8VKnoPNzvn6X9nk_8z7S409iD82ztt9-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
رئال تو این تابستون شاهکار کرده و همه اینارو فروخته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102384" target="_blank">📅 22:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102382">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhabZV6KIhTZHszIC2nHXo1upvN5VBP_VEnotgYWyUXpkWdqNXthwpcccL_knAKl4Hm7FqeH28CTC33HF9byzvbazE2baiP8BEWKOg_26rAie0_mNK9edSM6AYXDo-fwE0hbrSscnndLr9Y3H4UDdzNdm5d1mItM8IG8zlPHga-dfGFUxEZydna1LuLIANfVfObcrUp5Ki5rpOTXSoO7sgUGkukvBntkRkI0ixrWkeXSDd6yNNdUdcE3wfUMhOy1yVOkPkaeEQpACNUTR0U_IqJ3Qou3X6M9BEKb_huicjuLli6ximRttfV2oXlGYlRzhKxyJLsN2sqihlqGLli1Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CQUJzNQ-VEN2hdQFzF1nxqT0UVguVKxJillhDvLB3Yo9G6h9OH7_O5aveguF3SRlaSxJQlu6eaHSwt0Lv9clfd0F9M3b82PBJwDx-M8K74GtrBvvxICLD4a-NKEeYNzUWvEihsvZiQ_OMujSrA2yjVl7ZXevJRwIJPhJYaZqh78ZXUJ6SyaSiBC8lQ_RKbLuMR6AA228B2QZFgIxi9_mITan8u9rYUMja4AZ98goZOhiOY8Nsl--oWLUyBl-2d3zk8rUm1pfo_ln-RvxKDAGwV5mzrmrHdQ2cJvLvueLrI99xXMjqeFpmJ0wjCudpZgzdMi3T3Un5oei92Dig7CvHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو در 2003
🆚
رونالدو در 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102382" target="_blank">📅 22:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102381">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102381" target="_blank">📅 22:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102380">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujWF-5hmJ91UVLjn6ssk4KpjmMhik1ehDwLQEYFufubWsjgpQgHEMIgoPuIRh3C26iN1-iGxHtCuWIIJja95oQoit1j5mOlwDeQnhKS2i06LwAKpAPN2S5hMF0hUPrpAedW5HlvFKasanXN8kc-8zt6Wk9Ef-Ueff99IheXbPsLo4Ht3x8ToSIO_xg_xASQdQZWcGNoO8QirKJ1ytzJZV1OvLsSEj0GwOQlTHMDy0pYVMovqVzPFT72-zpMw3jAyOB0ifJg2Mp6Gpqzzc-K8ScXBaBRDa5HWaUiAi1MmgBVC7mk41CHmDBdjCevCNrOMah13jZwhim2g5XHWjBBcZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری: کارلوس اسپی شده با بند فسخ به مبلغ 25 میلیون یورو به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102380" target="_blank">📅 22:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102379">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpMfmsusTAe_Jkf_ytZmndEZw13TJV6pPKMNd-IRJxVRNX-sKAPFaNbPudW0wUhWXO7YnLBumBgccpu8nX1CO_vymTlVuvxhLNn8GKHHisSLxgqtPgi23lwFrPxdWfLESgeCT-p2ZZ5dh-JUfzEAI1Rqm5jGJRGFtUhCtAdqWuYoIVhddrQXJmdAEs93c_glSTftb9W7Ye8VNhe2lFFge-V2dF6DdoJjb6PkjmtUpd6xYgik0AU35qhxG1z_6awb1bKyor1uXIDbPNrNIDYUu1ATeI1YSyk8N2sUewbjTk3jKNMbPoa2UyyDMk6-4LTWmOptG8bYph48VfHuFCcYlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییرات وینی تو  فیفا اعمال شد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102379" target="_blank">📅 22:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102378">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcAu6tahlQRb10NZLMFTtLSWYlR5Z2MsmIBthfqlgrG8qNpPtp7SiK0ezIDHR4qEZGMOFHjmNtFbyWBjRp7kwM3bMcrnWJ5Ew1XXgoBt8JylCOODTTYSezb3JXTxoClstcKCLEJ90mAv8SD479_9YZkik4EArMCykvR-L6vjLAYYO1Z6NlskEz_3AMqq0UWiMtFMpWa4Zo0NgPNZYbRbgGo9X1jH8hYI8G1M1ypWNF4JDeJvRn8Zv4pSCZ7QapDneSJrZB5go_iiSFBIiHGvjLfFSfiHOfDihm-grzuc9gKp-LShMgc7fJsH7mPTY29Kse2axduCugNGoox3m1UZ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بایرن طبق معمول به این تیمه تجاوز کرد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102378" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102377">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdKwgSoT_J_I5_gq_6p-bvT_CJ0TMk3LPM_wGXGj_YNz7n9n2nutsmlTtDLwYYopEBtHCZWyNdjKJLbdHoFuXBxg6q9eLziX5YVgsxNHTmY5ZDsvW5sXdQjVk9mmpqqu1men6DnYlUsXFJFT1JhSkgT_-kG4vIRL0LesePBrXeecRQbpdXfRUbN35QtL2ShHNIDhG2o58gayHVeN9d07b_ciII9_zgowLo_klKgjAsC0v7LQWn2czZM6pkTp4RhRlSiENb1ZkMacPYNCsECL4TnqnFevhnVwuSdgO8Hoh_MA-Hs3yuEQKDrzxv3bmPob8qb06_0-f9pTjQieWp0wzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه فدراسیون انگلیس:
ما در کنار همکاران اروپایی خود ایستاده‌ایم و بطور کامل از موضع مشترک آن‌ها حمایت میکنیم، ما با برنامه‌های فیفا مخالفیم، جام جهانی متعلق به فوتبال است و همیشه همین‌طور خواهد ماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102377" target="_blank">📅 21:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102375">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHS_itnb7H5ZRAskVNUlWmUAx9Fv6NAN438Fiz9pVEMNq3dButf1IJ2DRd8WD3djjF5EKFS2_WxUFDBtXWEI_-745sZjsA5UcK16vDTVVLYuB238Utz7xSRfstj5sKk6uwmMCyD0WIbQBr50Uj9ZSPWsIY5sJeDSyVQ4sVxp5tIwHrrV5ZZPneIFfbHBvkpQ3jNwvv491HS9XxcdGjpKVVs08Rzeo04S7Z0i0Pp6iP9nOxZwjA70qnCLVeG2aXHElomZPGRx9CTqoaMz8TMHq23hNRu4cMFzTWLK-aqnVJld-_QpFB-tWX12xmbp9dpgFsUQC_ua8d_rYbW3rDdnyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
اسکای‌اسپورت: منچسترسیتی برای فروش رودری حداقل ۷۵ میلیون یورو میخواد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102375" target="_blank">📅 20:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102373">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcIW3hqlxqTcXUQq_9KCQ65pFnCK4yYs08a1tESbgI7mu1vMkCGcRwV-pAu9tWhP8bNdVO4Xcfw6BNHYv4H6zEmGXTp43I0Pr7-7mhZyaKcA_c7pAIXt4754F3LHIgRgc_3dAXTcnqBLTspdQtAwW55OsNjp_LcDUIWjxt9SMs7CHdyU7JcJwmW2sti1uiQG6l3dy-Ycfb8Zon6lZcUBqylTXVxk_xlMtOyUrgYXucwUiwWkh4y7Csugia22gM70QwFVw24YU8ooYjSmW0On8Uf6V4wPrgzPRzrhe7xav6ja4yivSUgwTq-gAOaQ5lWU73fwyrGloCAsN2svV8rxvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d9c0f441.mp4?token=impH_6V-9SEFciMuPnGwC72DeATetexQ5KcwqSmv5f1HACy1A_sfilLZDZqLMGTb-Ajr5W2ce8_2yEKH_KUmRWfgJR-GKrtqwiUsLO5CbyemMsnzfqshuujR7jaddULiDXcbZp0lu2I116GoycDUIf-07HJC08cnimn72kqQDOSx3q7ZSbAlTU_kzKHnEVllOMCzlc7uueuTn2iKyQaAM9O9B3aBErzckmF35ZJ0C6dz4dSI0tElqBl9MH4B5J6tRwMjJgeoCZ_juxejDblCJDKpGOOBqLUqfh09H9Q1ZeQPzXDop2tCxVA4b5tlkNpoHL8FaCxERKujn-16DcXFvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d9c0f441.mp4?token=impH_6V-9SEFciMuPnGwC72DeATetexQ5KcwqSmv5f1HACy1A_sfilLZDZqLMGTb-Ajr5W2ce8_2yEKH_KUmRWfgJR-GKrtqwiUsLO5CbyemMsnzfqshuujR7jaddULiDXcbZp0lu2I116GoycDUIf-07HJC08cnimn72kqQDOSx3q7ZSbAlTU_kzKHnEVllOMCzlc7uueuTn2iKyQaAM9O9B3aBErzckmF35ZJ0C6dz4dSI0tElqBl9MH4B5J6tRwMjJgeoCZ_juxejDblCJDKpGOOBqLUqfh09H9Q1ZeQPzXDop2tCxVA4b5tlkNpoHL8FaCxERKujn-16DcXFvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
استر اکسپوزیتو درباره آشنایی‌اش با کیلیان امباپه:
ما در مادرید با هم آشنا شدیم. حکیمی به من گفت که کیلیان خجالتیه و خودش نتونسته شماره‌ام رو بخواد، برای همین حکیمی شماره‌ام رو از طرف اون گرفت. چند روز بعد همدیگه رو دیدیم و بقیه‌اش تبدیل به تاریخ شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102373" target="_blank">📅 20:21 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
