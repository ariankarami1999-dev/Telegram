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
<img src="https://cdn4.telesco.pe/file/iTP5dEGbN-JKPgO1U0Og-VqIdnEQwGx1lHjREcYd_j76Fn0z0BlKPAdTNEHVPv400Vq5kzpnwPXCPhoUrm8hmleYnm-JBRtj0OCbyQyhiLWmNBfqjfcOv1X5ZrL3C6pQWBle0TCdky2SWoFEVmh1qjwIFlb2HJsU8jwhDn80ZJ9a5Z7aeN_CSKPnw29BwiUM9W6H71td3auhpMZZb0prWgDatshhwRisBFVdYX5WN0UleM2xynIP6lZJsFEPjTpF2ZEGfY0Hst-gWOeGxqaBUuWO4F1pB7kV1KSKPiBBqn7MGiVfW7yoTTMUrR6j7dBLJ935PxL0TDrJCmRM7Gm5aw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 970K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 22:38:20</div>
<hr>

<div class="tg-post" id="msg-125902">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqXzeyXA15jHNY-tZKgt5brEaTM1rekozJLRJagymmmuDG2TjSjKesG-V3obIP84dyHup0_9hnJAEEFY-yhDzUOoReFn8TOCZdUGmcI9vrGQ5iu2Vn6FwaXEzFiSy3bmdtEP5rUGBsm6NulJhGU9nSQnj29sg8vIPbToUHOoySyvxRElcW1LC1MehuuDHKExpjlIxj_VHNdjan-bWao-xmsEND327dxd2A18MjP2x2_E9ukEBO9OZmCW2OUu0g8pcmVvytwuPqPDJ5n38R0PiiUuV2ZiAYcax8fzXMuAhkccAK7K-LjO1JwWMWqDJmXDja-n5CDa8VxmehDgQGkCRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسمان کرمانشاه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/125902" target="_blank">📅 22:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125901">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qhj_nzc904oe2S_NzmSm5Y7uMYkD8zSOgH-5CuRewrcYJ_lr36vcZTHQ9haMQaKzRhdjG-zEacvEmIpuznLyZpfgQ4_8uLNtP3psrZwXi6H4Nw6euiniLcrkwwKE6tCGxcJ30rW5Bb4LAmDqyjPh2GAv2L01E_vD1UJOn2ehPTTs2iPODgrScFX0-PacJKb6cjqNSN6cy8G10o-lWxB5iwqFfb-UBoEpGcaxnrqntW34vT_tG9xwCNut86tOt8sC6fzlxJxYKu7pxf6pJDZFL2JXFQXjR_kXa3LaFn1tYLxNR4nRJE6EO1UuBuL5gtaQL5dl_7_ggoild1JL9SJumQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آژیرها در سراسر شمال اسرائیل به دلیل موشک‌های بالستیک ایرانی در حال شنیده شدن هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/125901" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125900">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
فووووووووری/انفجار مهیب در اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/125900" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125899">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
یک مقام ارشد اسرائیلی چند دقیقه پیش به رادیوی ارتش اسرائیل گفت که پرتاب‌ها به سمت خاک اسرائیل از سوی ایران به معنای «اعلام تجدید جنگ» است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/125899" target="_blank">📅 22:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125898">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
گزارش ها از شلیک موشک ، کرمانشاه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/125898" target="_blank">📅 22:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125897">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
فوووووووووووری/بریزید اینجا
⬇️
https://t.me/+mKQjO9EB47o0N2M0
https://t.me/+mKQjO9EB47o0N2M0</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/125897" target="_blank">📅 22:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125896">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
فرماندهی جبهه داخلی اسرائیل: مدارس در سراسر اسرائیل فردا لغو می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/125896" target="_blank">📅 22:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125895">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوووووووری/جنگ آغاز شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/125895" target="_blank">📅 22:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125894">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tuv2DK6ZGoGTk4w9aqJSuJhvYAzxj2LAR7Q-aLVfbJWSu_luSumdvCUMhLiiCBe-xltIvVhiuSy2Iw71oOhCw04mia48Rv-PzdED3eNQ7Ohp2Elx47EXRJ8ggyRbve_cBGiCfF3ddPueB0H33geY5FMC0nCw3jDlX7ySSv40n9Cg2foKKdjU0aPsQ7N7f4zZFW34jxSVKcvg6PQYiD48n3MRTTPI-S81QtPy-0guk5K7vfrVC4BFAAravoUYjzXiKpE-XiKy_P5NN9WX6pmfyZ3FXzfZe5_sKNJ-niGVcQJruSwxl-54IgJnO8bttm8ia7BJel4eJqr9mUdKC6BYlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوووووووری/هشدار حملات موشکی ایران در اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125894" target="_blank">📅 22:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125892">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S_ghtOckjlSpD8qd64_yGJvY64lO5wfx3UyRQ2kJnH3tAxS5dFd53w6wfbXff81_odzS_rLsuxcu9Uo7HSnjmFET4WArSeg7SDMj4tVJH9aTDhXvfyD0_nqwlRdiQSjzXAUz_2u62oNY8DM72LNMyOqVkLm9Z_7R6k4E96yC2j9L_ZBLZkjGmoLaOg0A1rfWwyFnCefbvHkv2_KXDWUZ_pfaSxwj1YUGUlYIdZ_bSXLyMU80n2_fv9soMaGIiF5cLEpbSJnJUYB0nFnWBKJxd2qWb3R0vtSmq69qcLQqoLz2eS6_QdmMCKmOlNch-PzYgggfoWc348IRds42-IqrFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W4jdrKrQPTVR5AllckpXT6X4InxiirmsdTRy2mAtkjEOCYhdeQljlZKXvhPDiWjDnF9QPCrQV3pyw8otlQcO10lHxNbCjr_sQTSlZ9JIVoyaY_tfby_dkQXmbt0sTYxgRqM_KSvedNCvMMX_k1GFkrHSqY8zxsGgbxnAmfJ69qle85nPuduCKhA3AapRLXt7FqNRodST7zgfxV6L-yTamDItw2oDDvhsaep5eBXUJwuO2vCRmYs5_F1_0bPiKYA2m1JOYvrDLP5JP4aV7ARwZFb8RXwXn3fBNq4MMT_7fP-nv6xH_E8vkAT_fKSblj3P7LQXD4RQPiz-LElED2yGFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
فوری /  حضور یک فروند پهباد ترک TAI Aksungar که مأموریتش شناسایی و هشدار اولیه است در نزدیکی مرز ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/125892" target="_blank">📅 22:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125891">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فووووری/گزارشات از شلیک موشک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/125891" target="_blank">📅 22:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125890">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arEfNLqZxVNowYuFjUqYP4-MoUXR5yEtJwtS6zhsE4_XxQbUV_mV2Punp8XV2TbRE1iHBESOPjq0WkP6EiIk3eekqjm0rQEyv5IGLgg-dXJZBPDd6dAp3suxx2AhMZ8yRQShvly3FKMN1lZse2MAz59hqj4muo8vv-GDrVcjoHAmooLEKll6GAcMl-mmpbf1QjlQTHiGEx7b4n_Y9Hctbp0z-gIvnrKc3vP2ce9_nkpuU3FB_dNlmB8c0DLHdywg__Q0s0In8cZx8pm3t6GKTlfq2wHWtg0uaElywaKmWEC74MALgiKGsUPOfTcdkEca-sckVfV70XXaEZ2EZZHJzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسمان اسرائیل هنوز کلیر نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/125890" target="_blank">📅 22:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125889">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
‌‌پرواز جنگنده های ارتش برفراز غرب تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/125889" target="_blank">📅 22:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125887">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری/هم اکنون نماهنگی از سوره فتح در صدا و سیمای جمهوری اسلامی درحال پخش است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125887" target="_blank">📅 22:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125886">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/125886" target="_blank">📅 22:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125884">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/125884" target="_blank">📅 22:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125883">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فوری/ایران اینترنشنال:
سپاه آماده حمله موشکی به اسرائیله.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/125883" target="_blank">📅 22:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125881">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d0j3vZIvro_FXevFFpqltGgHDWzbPw9fwBKX4MVtaKMMo2N0fsi1mb2YugHoAY-umLwIgD8x2nlIMaD-5xXzjKiXqfo6rIiHImxvY5tWBKy80eVg21xZvDLfg3WKILeoq3UeM6jJfJtsskb_6J1xnsSsoGFyzntUBqK4IRC0cjTNcdoVxnbWQmfct3UedOMiRHe2vK189P9__HOFmHsQ4W0g4Pk-XiXESPuhq-yJgMFnFECdf_2Gzr29CMdWHTf9dWnO8kH8rW4gWXhKDsg1tCtN8JOsTPIBaLV2ZZ-32OpvbVbp0AcU9DAJ-j7QgYJW6TEZwT7A_w7E2snpftwiPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایرباس A300B4-60SR ایران ایر در حال چرخش بر فراز شمال ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125881" target="_blank">📅 22:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125880">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
العربیه: فیلد مارشال عاصم منیر از ایران خواست تا از فرصت فعلی برای رسیدن به توافق استفاده کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125880" target="_blank">📅 22:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125879">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
العربیه: وزیر کشور پاکستان که هم‌اکنون در تهران حضور دارد، هشدارهایی را به ایران درباره تشدید تنش‌ها در مسیرهای کشتیرانی دریایی منتقل کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/125879" target="_blank">📅 22:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125878">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5cHwZyhmEGRJso9t3tuKk0FZc4otlvKNZRwndC6Zr_05NgOCRdolozG4tew43JkaeM2pqaraNzAupDNaUzU0ru2l-60JjyAILEHlCbYbyuFdOYrkXq-YmJ7l19kXUCtA4V6sCSTs2XJoYd5fFMjbf6lP04eGX0C5kWfBR3s6Enfo6_OVeUDe98ner5VFaxsSwGQ5podrJ41lHU-XYBy2D6QKl9k3uVyE6zlKxwIkfffCaHstN1DZoWtwM-syqTGo__hr_aHm8rmJV8FVsCynRrrApTfMv1CqAjcHmq7prCa9w4O9GTroZmyeyNyn4TGi1eF2yCir8ppqREFLo43yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ وضعیت آسمان منطقه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/125878" target="_blank">📅 22:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125877">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
فوری / اسرائیل هیوم : ایران ممکن است در چند ساعت آینده به تلاویو حمله کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/125877" target="_blank">📅 21:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125876">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
نیروهای مسلح امارات متحده عربی با ادامه افزایش تنش‌های منطقه‌ای در حالت آماده‌باش قرار گرفته‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/125876" target="_blank">📅 21:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125875">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: به دنبال تهدیدات ایران، بنیامین نتانیاهو، جلسه مشورتی امنیتی برگزار می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/125875" target="_blank">📅 21:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125874">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9405d969.mp4?token=oL6e3y6DJ7XBxabT0y46VhpQTHpUQYlGul3FxxwStOQilBf9SWXxE_uikQ6KWtbd4C-Tas8CDz08KodEQqhOLPkQmgUNWR1m8c25dZhPlxMi9iRXPaSX49U9cUa_w6rCo6n1Tz4iERP5Zt7fSPe6H0LDUWts9w6R3gJFNd2LvRx01GoJ8ErADxli1zdmvfRW9QkM1SAFoDNISalN4cdDg2OGFapH8FtihWwwMDyF8wtRNmqzy10xsjQOZYXcGvUZdv-U7wLlZnkHhUyLDebKTRAJ2eyTWvx3693YdxTqKmkWH7k1yIQmjTK0gH6sbGTmj1pA0t1IWlrGeYhs_zkvsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9405d969.mp4?token=oL6e3y6DJ7XBxabT0y46VhpQTHpUQYlGul3FxxwStOQilBf9SWXxE_uikQ6KWtbd4C-Tas8CDz08KodEQqhOLPkQmgUNWR1m8c25dZhPlxMi9iRXPaSX49U9cUa_w6rCo6n1Tz4iERP5Zt7fSPe6H0LDUWts9w6R3gJFNd2LvRx01GoJ8ErADxli1zdmvfRW9QkM1SAFoDNISalN4cdDg2OGFapH8FtihWwwMDyF8wtRNmqzy10xsjQOZYXcGvUZdv-U7wLlZnkHhUyLDebKTRAJ2eyTWvx3693YdxTqKmkWH7k1yIQmjTK0gH6sbGTmj1pA0t1IWlrGeYhs_zkvsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدار دانمارک و اوکراین به دلیل بیهوش شدن کریستین اریکسن متوقف شد
اریکسن پیش از این و در یورو ۲۰۲۰ هم دچار حمله قلبی شده بود.
@AloSport</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/125874" target="_blank">📅 21:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125873">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
مقام آمریکایی: ما از نظر نظامی آماده‌ایم تا در صورت عملی شدن تهدیدات و حمله ایران، با آن مقابله کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/125873" target="_blank">📅 21:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125872">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
اسرائیل هیوم: برآوردهای امنیتی حاکی از آن است که اگر ایران امشب با هدف قرار دادن شمال اسرائیل پاسخ دهد، ممکن است مواضع شبه‌نظامیان (نیروهای مسلح وابسته به اسرائیل) داخل خط زرد (مناطق تحت کنترل تشکیلات خودگردان یا مناطق حائل) در غزه را نیز هدف قرار دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/125872" target="_blank">📅 21:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125871">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnVDfVTEnltaQFkCRzTFPpRf1WlfYqAfUMVR7MAjApxJlDPAmb-EDg72Rw4Us-TCXr5gltY6cES7skD7qPoTpkyOYUbUEL2GpO3q4UXQHzMS8__TA-tY6Tj5cLoljJ0zeA-ESSLEjYKWqK23O0JeHLwviSBnhuzP5lzF9sePtlZMa_1yWwGQcretUudA-X2irA57P77HDwfMLMBkIstLHTov_ZvtMGKGyapRIfKV0u1NplKElVvVK60_sFo-z91WA0QGdKngJgYTdTtzYnxo4giKfL55QADdsA1-QNLorfXy_K6Ej7qCShXyGKLdh_r7bXfO986efl9gOEPpZyGzNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه مقام دفاعی آمریکا
به آکسیوس
:
- اگه ایران تهدیدهاش رو عملی کنه و حمله جدیدی انجام بده، نیروهای آمریکایی تو خاورمیانه کاملاً آماده‌ان تا از خودشون دفاع کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/125871" target="_blank">📅 21:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125870">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
🌐
با ما همراه شو و در زمان قطعی   وصل بمون
😎
بقیه هنوز VPN حجمی میفروشن اونم با قیمتای نجومی
🚀
✅
از ما با کمترین قیمت ، بهترین سرویس رو بگیر
👀
😍
💥
بدون محدودیت حجم
⬇️
⬇️
⬇️
@NetAazaadBot @NetAazaadBot</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/alonews/125870" target="_blank">📅 21:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125869">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GRCCQF9dKyrZjLa8-aNlVUxCNVQKG1Ra05GPAzt_tsFRMjXHREMejikGzcoityY_xgoYx8_8owWUNjE-lCLz8wxbOpnMdyxwMIEc7616ZUfjrZtUYfXxtmwFMN7kav04eXCQcPeDINfRaQKBPs6iRI_fZLRLerG9_wcL5ihZivfqqkkWBMIx7qZFDiShFgr8vtlzDSGLg-D6fGIIk_rFXztgH_jIYuE1vxL-EgswfqU2XVwfkYwMeAsVE_pHmuz8TQzMgursBWiNRsWy6-i1A5mtWpMPySc02a0SIscT11JhPsRmBvCng3Nopvn73Z3QrcyYV2od_xBcf-0Rk_6JXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
🌐
با ما همراه شو و در زمان قطعی
وصل بمون
😎
بقیه هنوز VPN حجمی میفروشن
اونم با قیمتای نجومی
🚀
✅
از ما با کمترین قیمت ، بهترین سرویس رو بگیر
👀
😍
💥
بدون محدودیت حجم
⬇️
⬇️
⬇️
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/alonews/125869" target="_blank">📅 21:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125868">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptBpKHfRR1CNtqKbxHg0oOEa668dU0ucIFoVTRtybgYxvpvSp7PXvKFy2Nmb6QBLhCzIGrhkKjtJdk1coGzGHGgCEMLpXNlWL0DM9zhAymmbBSh-NsTh5FwOK2OPNzDwvJLulgi5SwA0YoeE2KenegswjA8qlPrjrSGXBuGf-LJ8OC8GK-A34kHTeX_D31NvGs7B3nprg8cD21uRyS7w6TxJ3AgpMsY8-tSf2m5P8_E6IsMycVtadqfwRi_1l6xw6wR30IIoTpGlPKS-cQP8biXEL339pG9Cm0qtTvSe-ZjvkYBkRyuUS5Cdm2TG5E2Ka-t_m71sFHdp7MPGRt74Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم‌چنان پرواز ها درحال بازگشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/125868" target="_blank">📅 21:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125867">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری/اسرائیل هشدار داد که هر حمله‌ای جنگ تمام‌عیار را به دنبال خواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/125867" target="_blank">📅 21:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125866">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوری / گزارش ها از پرواز گسترده جت های جنگی بر فراز اقلیم کردستان، عراق.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/125866" target="_blank">📅 21:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125865">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
یک مقام آمریکایی به آکسیوس:حزب‌الله باید فوراً آتش‌بس کند و اجازه دهد این توافق‌ها اجرایی شوند. شرایط پیشنهادی منصفانه است، مورد تأیید لبنان و اسرائیل قرار دارد و مسیر روشنی برای پایان دادن به درگیری‌ها فراهم می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/125865" target="_blank">📅 21:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125864">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/168eea2f41.mp4?token=EQbKHb4-gezKVeJB6u43IoYuM08_0Nfn2lk4ZMLSeJSCaJewQDihhP4Ar1Yoku9c-8iHxjuHPBLP6KuvOfKSacuj-8rDqtX2BEW5d4BFax29NM9PIKhtfBx2iN5WrFTY5MEAw94mznj81V8xFQAMkzAUqNCiP6ho3zwyWZ3Yz1Aqq_oZjQeBw9oT7RSGv0J-OtLUcBsGrmBqkI8RpUpCcwBNssmk0jy92l4ln11GzPJIjVDuH2RyCt3h-G2ocHTOOMD-Lp7K-QXKJaj5T_l5-ty75EYMT28kD94MlV-WiUs-__Q3wK7B_9anQp_jvxEPRp-MpR3vZDqOiUB1b1JnOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/168eea2f41.mp4?token=EQbKHb4-gezKVeJB6u43IoYuM08_0Nfn2lk4ZMLSeJSCaJewQDihhP4Ar1Yoku9c-8iHxjuHPBLP6KuvOfKSacuj-8rDqtX2BEW5d4BFax29NM9PIKhtfBx2iN5WrFTY5MEAw94mznj81V8xFQAMkzAUqNCiP6ho3zwyWZ3Yz1Aqq_oZjQeBw9oT7RSGv0J-OtLUcBsGrmBqkI8RpUpCcwBNssmk0jy92l4ln11GzPJIjVDuH2RyCt3h-G2ocHTOOMD-Lp7K-QXKJaj5T_l5-ty75EYMT28kD94MlV-WiUs-__Q3wK7B_9anQp_jvxEPRp-MpR3vZDqOiUB1b1JnOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نبویان: جای تعجب است که ایران پیشنهاد واگذاری تنگۀ هرمز را داده است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/125864" target="_blank">📅 21:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125863">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: نخست‌وزیر بنیامین نتانیاهو با هیاتی از مشاوران حقوقی دولت ترامپ دیدار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/125863" target="_blank">📅 21:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125862">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
پزشکیان: گروه مذاکره‌کننده، آدم‌هایی نیستند که جا بزنند در نتیجه ما باید با قدرت وارد صحنه شویم و از حقوق ملت دفاع کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/125862" target="_blank">📅 21:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125861">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTl2usr9vGHQ4wxDbbZRgSTu0Z8A3kB44qOQ2YZfqNpqI2DClhs6f1IGB1aH0SQT379qFrc8Dq2DC0zuKxQU62XFXV-PN9yzYOWNPK7oICkib3Ns8QX3SDzFcdj0j1kWLPEhsB5dRFMqWyeihwrn6EenhTOxyRdXLiOSfD8XZbtrIv8kfB-gvT92r5P8aimPLLHZjlAXIeKctppDDrpd38I0yjYRA3laCVxdEw7A-C8kyOh2iSXEVbCb3m-k88aSHD1DdNiRPQGCvSNIBAPWt7OZ8TZbh1bp67xjJ4fX8nC2HzavkTCcNu7XSVS-f9NMdv-eVu08gvTI5eZaogdxiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌جی ۱۲۵ موتور اقتصادی بازار ۳۵۰ میلیون تومان!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/125861" target="_blank">📅 21:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125860">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: ما به آن(حمله اسرائیل به جنوب لبنان) رسیدگی می‌کنیم، همانطور که انتظار می‌رود و ایران نباید شلیک کند
🔴
اما در نهایت، ما فکر می‌کنیم یک توافق—یک توافق عالی—احتمالاً به زودی اتفاق خواهد افتاد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/125860" target="_blank">📅 21:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125859">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
همه‌ی شرکت‌های کانادا پرواز‌ها به کوبا رو برای همیشه، لغو کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/125859" target="_blank">📅 20:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125858">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
گارد ساحلی تایوان چندین کشتی چینی را از آب های محدود رهگیری و اخراج کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/125858" target="_blank">📅 20:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125857">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
یک مقام بلندپایه اسرائیلی: اگر ایران به ما حمله کند، واکنشی صورت خواهد گرفت که شعله‌های جنگ را دوباره برافروخته خواهد کرد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/125857" target="_blank">📅 20:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125856">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/At2uyl-3Kl9kkcqnOD6LHs2s8piXm2jXy6-Q7n4V3ITwChQf7bz1js_a6TbWR3VJDTnD4-l1HGCAqvbeiZ47owJL07lpVgP1Ux9Cx6E-nBwZzDDs0iXR20oXJQuRKAazrSuGV2P-8BsdjkQYuBD48bG6tfYnUYQvc_nQf6FtwfTeAojCcR8W-ForpZqjuO3vaIHJ4re4qDntutd0tqqg_F2TkQW7MaB9XSijMunp28WWYwLLqNDdcK-26fltMIC7xPvWw4OGIpjFMbHVYUtyplh8h5dVW4eKeXDaZ5UosKrrS9IleixGxNNdRkRFnClyN8eiqkZOnHlCntfA0sq1XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: صدا و سیما نقدهای غیرمنصفانه کند مجبور هستیم پاسخ درخور بدهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/125856" target="_blank">📅 20:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125855">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6565069a.mp4?token=KpJxN30WOW4VGOA27bWU7Py4Ftrry32B603gi3Ljc2FEku1jlFzd5AqEbc9-I-FZnmxcwuiD996cEb65H7TeoJ5xzd0YZLSfseQM75OGvafQL_X5HZ4ywTBLV3ZImKLQeSj3Ox_u8aD_7NZhBa0rSHZKRQHPbYoO2knBikSlxn6-b29fetFJmmCoCXTEXeDogxtAlh-8CU6JjSVPn05oJgbhzFIFdVqTJ1J8VgEDLlk_ftjPVEUXCvfdv-0KeRI00gsDVJI0TAmWsMrrcVOFefPrBTx-yGTPR6uKzq9TaTnaq_ibdM4yMQO8f3feSG1fpnrcJLk3fOKTMUYuQ9_5pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6565069a.mp4?token=KpJxN30WOW4VGOA27bWU7Py4Ftrry32B603gi3Ljc2FEku1jlFzd5AqEbc9-I-FZnmxcwuiD996cEb65H7TeoJ5xzd0YZLSfseQM75OGvafQL_X5HZ4ywTBLV3ZImKLQeSj3Ox_u8aD_7NZhBa0rSHZKRQHPbYoO2knBikSlxn6-b29fetFJmmCoCXTEXeDogxtAlh-8CU6JjSVPn05oJgbhzFIFdVqTJ1J8VgEDLlk_ftjPVEUXCvfdv-0KeRI00gsDVJI0TAmWsMrrcVOFefPrBTx-yGTPR6uKzq9TaTnaq_ibdM4yMQO8f3feSG1fpnrcJLk3fOKTMUYuQ9_5pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئوی حملهِ به ضاحیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/125855" target="_blank">📅 20:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125854">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34153808d9.mp4?token=A247W8G0xMya8MSz8l4lppneQY6v5XcQwGEqStBQKpkDbqAJ2kha75CZ-sK8aetM9jBuhqDzWKzxzD0h4w9TkbjWcmFNW-y3RE6EoYdQC0lbCd9gSewQvAsrQFyT-sppctIhb1tCK8ExmX4IssVwGauMeGIBg_Xm5Z83hncRIZixcNQtTqYw3B0fS7bS7wHwV--9ZbVsX1o8sD9fgSHFotZmKj6010s1LHCAj3mKRr0qxARJYAXmIt4GCZOBLmVYoTMO5QIe1FTv1IBIrCjGlQXf2-nRGF0AW401U9HvYGL74iY7ImqGBZ3ahU2YBPETZK-qU_D1SicVRK66a88kAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34153808d9.mp4?token=A247W8G0xMya8MSz8l4lppneQY6v5XcQwGEqStBQKpkDbqAJ2kha75CZ-sK8aetM9jBuhqDzWKzxzD0h4w9TkbjWcmFNW-y3RE6EoYdQC0lbCd9gSewQvAsrQFyT-sppctIhb1tCK8ExmX4IssVwGauMeGIBg_Xm5Z83hncRIZixcNQtTqYw3B0fS7bS7wHwV--9ZbVsX1o8sD9fgSHFotZmKj6010s1LHCAj3mKRr0qxARJYAXmIt4GCZOBLmVYoTMO5QIe1FTv1IBIrCjGlQXf2-nRGF0AW401U9HvYGL74iY7ImqGBZ3ahU2YBPETZK-qU_D1SicVRK66a88kAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد وعده خود مبنی بر عدم آغاز جنگ‌های جدید: من هیچ وعده‌ای ندادم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/125854" target="_blank">📅 20:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125853">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d20dc92a92.mp4?token=NotqOtuVsZgZ64j9bjI2venmAdC3C4x_JDnbYXkJVzoTWTs2eummCmdF5YWWfEScIyFFam6E-eIu1OmcBpqWcZQQuYLu-XbDKExaHyQgHTQT9VS6amt7qdzhO3G6rcF4I0RtG6nbzCF-E_jgRTzV0LY1bSDi14th1ysSjr_RUrjx50j3IjV0ZHMhmzXSLD_oHKEeaO09B0tsMNBPo7CRqAWEqm0A7xVqycq2UthUNkG_v88s99X_8OVoSJZ10MOvxbnrQqcvNHiJL7lRdXdiBoplKmj9tbMeONxJnJO6vUmogIjV1ZT9pAbrKQfDOpXnf49C8XULnp3RsKzi-NZbbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d20dc92a92.mp4?token=NotqOtuVsZgZ64j9bjI2venmAdC3C4x_JDnbYXkJVzoTWTs2eummCmdF5YWWfEScIyFFam6E-eIu1OmcBpqWcZQQuYLu-XbDKExaHyQgHTQT9VS6amt7qdzhO3G6rcF4I0RtG6nbzCF-E_jgRTzV0LY1bSDi14th1ysSjr_RUrjx50j3IjV0ZHMhmzXSLD_oHKEeaO09B0tsMNBPo7CRqAWEqm0A7xVqycq2UthUNkG_v88s99X_8OVoSJZ10MOvxbnrQqcvNHiJL7lRdXdiBoplKmj9tbMeONxJnJO6vUmogIjV1ZT9pAbrKQfDOpXnf49C8XULnp3RsKzi-NZbbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:ما به یک کشور بسیار قدرتمند را مسلط شدیم: ونزوئلا. سربازان زیادی، یک ارتش بزرگ و قوی.
🔴
ما ونزوئلا را در عرض چند دقیقه تصرف کردیم.
🔴
ما توانایی ایران را در عرض چند روز نابود کردیم. هیچ‌کس هرگز چیزی شبیه به این ندیده است. حالا من می‌خواهم آن را تمام کنم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/125853" target="_blank">📅 20:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125852">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef44fe5bc.mp4?token=EvPlOeomcWYZsGAbD-nCIqO09xWXNb8Pls53396MVur51AkwFhLZeQVOzORAE-fqP00yYKDoPY8E6pHgIEnuwTcWK3ZsuyOY5ExrWCp3q2w6cscmMhTYrh8lnhMlM3yCw7NXsKjhfKubNSrIE5scETuqGsiSoCgTI4mOBDwYGtYkk9_eC018Air3kRVC7jST3Ql9Pdh0HyAI2JFLiHhmkrT_HX_dMsXCNB_-3JWr57kJipHYDQjJJuBvfH0fAMyB3Vu0SbpIrnrWYOSjV8W03FEyKLCqxjjiY1WPvoYNMSOXGWBjY6ysNrkHhUToUu_GX4sMt3x9CDm0kOsQGffAlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef44fe5bc.mp4?token=EvPlOeomcWYZsGAbD-nCIqO09xWXNb8Pls53396MVur51AkwFhLZeQVOzORAE-fqP00yYKDoPY8E6pHgIEnuwTcWK3ZsuyOY5ExrWCp3q2w6cscmMhTYrh8lnhMlM3yCw7NXsKjhfKubNSrIE5scETuqGsiSoCgTI4mOBDwYGtYkk9_eC018Air3kRVC7jST3Ql9Pdh0HyAI2JFLiHhmkrT_HX_dMsXCNB_-3JWr57kJipHYDQjJJuBvfH0fAMyB3Vu0SbpIrnrWYOSjV8W03FEyKLCqxjjiY1WPvoYNMSOXGWBjY6ysNrkHhUToUu_GX4sMt3x9CDm0kOsQGffAlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث درباره جمهوري اسلامي ایران: کارها در جریان است. حمل و نقل دریایی در حال عبور است. ایران نباید به آن شلیک کند و وقتی این کار را انجام می‌دهند، ما طبق انتظار با آن برخورد می‌کنیم.
🔴
اما در نهایت، ما معتقدیم که یک توافق، یک توافق عالی، به زودی محتمل است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/125852" target="_blank">📅 20:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125851">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
شرکت هواپیمای هلندی "KLM" پروازهارو به اسرائیل، تا ۲۷ ژوئیه لغو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/125851" target="_blank">📅 20:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125850">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
کانال ۱۲اسرائیل: اسرائیل در حال رصد و آماده شدن برای این احتمال است که ایران پس از هدف قرار دادن ضاحیه جنوب بیروت، تهدیدات خود را عملی کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/125850" target="_blank">📅 20:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125849">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
قطر به دلیل تنش‌های منطقه‌ای اعلامیه ناوبری هوایی (NOTAM) صادر کرده و از پروازهایی که تا حد امکان از حریم هوایی این کشور بین 7 تا 13 ژوئن عبور نمی‌کنند، خواسته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/125849" target="_blank">📅 20:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125848">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
فیدان وزیر امور خارجه ترکیه: اسرائیل معتقد است که هرگونه توافقی که بین آمریکا و ایران در شکل فعلی آن حاصل شود، به نفع آن نیست و بنابراین به دنبال مانع‌تراشی در روند مذاکرات است.
🔴
ما از جامعه بین‌المللی می‌خواهیم که به اسرائیل فشار بیاورد تا از مختل شدن تلاش‌های صلح و مذاکرات جاری جلوگیری شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/125848" target="_blank">📅 20:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125847">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل : نتانیاهو به خاطر تهدیدهای ایران، یه جلسه امنیتی فوری گذاشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/125847" target="_blank">📅 20:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125846">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/509058b963.mp4?token=apMkQRPn-8AIkn3A2KAnapvWbzKb1DO6cVf4qujTEm3qs_gAuX2oeyY991XxkevUZJRBKIZ97u1sPMVFcMl_5I02ydxFXmlW9Z9k2ALl8Ji0-Gx-BnIkMHVTD6hvbzmO5OSOWl3KBqzIhbGsW0snXIDdGWBVgAVo7udPo7gTfbz30mp8e6yI_eY3OrbPDfJtY29iwqsXxBbyByn7XSND2XSCY0T6PzecVUl6qeSOOdVKdHVMWbKcUMJunb5qm6l8vBGfDPmYrOET3n2kOlO5vVcOumtm9mZbVbctJBg-6XlGAJMoDhiPc2fQgk0BCzQ9RvI0S3P71fAs8iC7bOaw2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/509058b963.mp4?token=apMkQRPn-8AIkn3A2KAnapvWbzKb1DO6cVf4qujTEm3qs_gAuX2oeyY991XxkevUZJRBKIZ97u1sPMVFcMl_5I02ydxFXmlW9Z9k2ALl8Ji0-Gx-BnIkMHVTD6hvbzmO5OSOWl3KBqzIhbGsW0snXIDdGWBVgAVo7udPo7gTfbz30mp8e6yI_eY3OrbPDfJtY29iwqsXxBbyByn7XSND2XSCY0T6PzecVUl6qeSOOdVKdHVMWbKcUMJunb5qm6l8vBGfDPmYrOET3n2kOlO5vVcOumtm9mZbVbctJBg-6XlGAJMoDhiPc2fQgk0BCzQ9RvI0S3P71fAs8iC7bOaw2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست نتانیاهو فقط همین هفته
:
- نیروهامون قلعه بوفور رو گرفتن و ۳۵۰ نفر از نیروهای دشمن رو از بین بردن. ماجرا هنوز ادامه داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/125846" target="_blank">📅 20:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125843">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rm8smyLMAAUZYXmsQYl9H9mgeF4nIO7eIODWsD1FVbVdwYe8BW_FX-a0LveXMEAM_nrswitOqddeWtrKwGjs9RYsl6_Aj9DX-XqZGPxcpLwSHAk-D4eyRi32mO_WUaAvT4nXo6XZq6Edtu04qPhsPfmmqrJyOUz6PfYVlqePq_ZJQ7w99Do3wgkl7yB71UBsvyzOHBGQiRmml1UPWGUp3GCqn9G90cuauU1EbKIJFpFOtG2ooGF6S0Xlo_Z0ddvzNU5zxzVLJUxK16DdCf-yCEbeM-GlBKVrOoX_7zAEDwvL-pLNmMf4nAOa3iGJd-sFHNU2KEBek_Oq9kP7I6lHqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MIkmLnIQFBA2pPakG5LgSarsNUHBqHfRARAjeX5YxpJubf495JCJvC874rPbAtuljCJ9uyV2KogL3bozybg6xBjw1TkLP445f-cD3nGKYfFQJjj2wPbgDdwVAxCDfQCoWCoLSfujw_e4MhM1g6Q1UVGPpASC0Ja5PvIxR2Ddz0CWFHsKf0LmcX75AxrRfyo2JqfGMnRxvRrApI8Ld2Lz1inGsT7-nB8res0UY8WOI6NoyLpQ7lvHiIFr-w_gyc6BBa3vV_URdyE5pRhJghFRQuVWQ7yFnSgmSjYe2QR24egULUJj8EbVKLCkigpG1aB59iz2gy_rHq-Vrx1jr4oUNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4001f02598.mp4?token=mkk8TY4E2PQabBulEiZMaUaUpCiSqwsIHi8IChHKUWwZLogGraWfUmgIrk1SJYcw0FuLg4YG73NMNL7qVLEJO1e8U1M-Lvo3cThOfXTgWdcQEthKFkfRnzkLd3XVfV9Z8YKuIbG9sOra3RgsBpxfojXm1coXjiASBFBv8vYt_mkd3RCIVHrSdrRTFV7wB_fAep7nd64YUutFMD0znOFL_YMybvMP21qZTk-q0PocQMM5hDBoWy1Nme-yGmEkW7oLSUYRuxyCYSIaDb0GkoYUBb5j9_AUEZ6ywkc0qHn59zVS7wR2uJwpihHcZ23Wc_vIRWTd-wrMpxL8HxGnyvfefg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4001f02598.mp4?token=mkk8TY4E2PQabBulEiZMaUaUpCiSqwsIHi8IChHKUWwZLogGraWfUmgIrk1SJYcw0FuLg4YG73NMNL7qVLEJO1e8U1M-Lvo3cThOfXTgWdcQEthKFkfRnzkLd3XVfV9Z8YKuIbG9sOra3RgsBpxfojXm1coXjiASBFBv8vYt_mkd3RCIVHrSdrRTFV7wB_fAep7nd64YUutFMD0znOFL_YMybvMP21qZTk-q0PocQMM5hDBoWy1Nme-yGmEkW7oLSUYRuxyCYSIaDb0GkoYUBb5j9_AUEZ6ywkc0qHn59zVS7wR2uJwpihHcZ23Wc_vIRWTd-wrMpxL8HxGnyvfefg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حملات شدید به لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/125843" target="_blank">📅 19:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125842">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXn4P4pzrW9MVE3o-58XIaZvt2ZSzxlPt4HBghr2u33NIcLculxH8HLAnJdXlUVvGK6-aOj5QfJ9daeYe-juwAAvjKkBimlN0YYzpda6JTKH8XfT0u1GNY91B3OT_Boe_c5cr-vulY23jOWKrhUj7KJaQsCBwVDPr9fBsbSNY5OqBWqKgow_BAFy-xUXGLh_ZqJfnmf7TjG7KRs5fa6HJIXW-j71hl9si_vf5v-6K2WLJR1DpLWkNO5lqPK4TltFOcHcrAcU5tMX9b-jcScOW6QFX3V4qWsE1VyQuwFkvxmlCxx8haWv3lkpc0MAusMsOmoayshUUy6u-EDpObGT9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات به لبنان کماکان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/125842" target="_blank">📅 19:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125841">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
آکسیوس: «اسرائیل پیش از حمله به ضاحیه بیروت، به دولت ترامپ اطلاع داده بود»
🔴
پایگاه خبری اکسیوس به نقل از مقامات اسرائیلی اعلام کرد: «حمله هوایی به ضاحیه جنوبی بیروت پاسخی به حمله موشکی اخیر حزب الله بود.»
🔴
آکسیوس همچنین به نقل از یک مقام آمریکایی و دو منبع آگاه اعلام کرد: «اسرائیل قبل از حمله هوایی به حومه جنوبی دولت ترامپ را مطلع کرده بود.»
🔴
اکسیوس تصریح کرد: «اسرائیل به دولت ترامپ اطلاع داده که حملات مداوم حزب الله به اسرائیل، به آن حق حمله به بیروت را می‌دهد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/125841" target="_blank">📅 19:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125840">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JO_HmmUEnljiuMp6NLZojpfxDdxT6-mgERH9bGZQ-vgkMSuYI-R_S8THlXQZ8HImh4ur0ecTPTH4QPhXaJYaPL3Apv68kJINFa0mD1pY5y6LlpXdZh8HUSecC2FqH1QP_77JYI50Ce_Du2Xydg9hdGsYyFVTHc6J7T-J1XPTCiC4DOORJ1Z4zQXDMzN6jDsgc9eyNBZ3lVCyvsXTAfamk1gcUy18PLhdPHoyT-Y6v_gmvZYYANq1SHP5RpJ9UtuvSHjaoeUvPKoJJ-D83cSLF0CTAKg_I6ykZksNFF83cqGYTzG51ouR0sxfmjxupbM0fgsnlrgErHZKgUTLb15E5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف:
آنها نه به آتش‌بس متعهدند و نه به گفتگو باور دارند، و با نشان دادن از طریق محاصره دریایی و نقض توافقات مربوط به لبنان، تنها زبان قدرت را می‌فهمند.
🔴
محاصره دریایی علیه ملت ایران و چراغ سبز امروز آمریکا به رژیم صهیونیستی، پایگاه‌ها و دارایی‌های آمریکا و رژیم در منطقه را به اهداف مشروع تبدیل می‌کند.
🔴
دست نیروهای مسلح ما، همانند همیشه، باز است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/125840" target="_blank">📅 19:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125839">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
هم اکنون نشست فوری نتانیاهو با فرماندهان نظامی برای بررسی تحولات منطقه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/125839" target="_blank">📅 19:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125838">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
قطر آسمان خود را بست!
🔴
قطر اطلاعیه NOTAM صادر کرده است که پروازها را از طریق فضای هوایی خود هدایت مجدد می‌کند و مسیرهای جایگزین برای هواپیماهای پرواز کننده از دوحه و فرودگاه‌های عربستان سعودی ارائه می‌دهد.
🔴
این اطلاعیه از ۷ ژوئن تا ۱۴ ژوئن معتبر است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/125838" target="_blank">📅 19:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125837">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
رئیس ستاد کل ارتش اسرائیل:
«به ارزیابی وضعیت در مورد ایران ادامه می‌دهیم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/125837" target="_blank">📅 19:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125836">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
صنوبری کارشناسان شبکه خبر هم اکنون: آقای قالیباف،عراقچی، فرمانده خاتم الانبیاء چند روز پیش هشدار دادند که اگر ضاحیه مورد حمله قرار بگیرد ما هم اسرائیل را مورد حمله قرار میدهیم، اکنون وقت عملیاتی کردن این هشدار ها است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/125836" target="_blank">📅 19:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125835">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twscDlmzjNkeqBE6bqNIUmL-0q6ErbfFd0AsNnstuc_BSKY9GBuevR7k4qLV_hAArDpIb0s1qbUDw_wzReTGB8UNOgAbSluPXXa56Kp1IM1PoNWP8H3lhBpoUbiBQPcRfjxEtSNb1l_oOkR6UFBFV0521uIRKRyR74Y15Nh3bCSmuy5SG0AdWcTkdD-feLa3NjhzU8aHe4cCAWMARCKKUQpR_qIcKYLBq7bH8O8xyTUHTaVR1x7E7l5dtTtRtxXKm3FurQ-ogG7UY_eNjy6AmPRaIeufIPy_B2uSJPwYN95augsPmxqJdt7UsZko9jCF5VoVaqkcE6iCSt5Huz3ZKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر جنگ آمریکا:
«ما معتقدیم که
به زودی یک "توافق عالی" با ایران منعقد خواهد شد
.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/125835" target="_blank">📅 19:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125834">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🌐
نامحدود فقط 90 تومن
😍
فقط ۵۰ نفر اول
❤️
✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ   بقیه هنوز VPN حجمی میفروشن اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 90 تومن
🏷️
💥
بدون محدودیت حجم
⬇️
⬇️
⬇️
@NetAazaadBot @NetAazaadBot</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/125834" target="_blank">📅 19:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125833">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V_zef-lCqUUNqXsn3KA-HrSBzMXZIDsPmo4yPmh_hLwsC7K1NUkfKxzWqqruV8bYyhaBSw7wy8wcqx-pixLoArUYPBuy-po0Pf30gsdCVZAkWPjRcvINX7VYTy1IhFlynIJZgBOfPzcGkpDOWpJBsV-iTD1KvQibGKK0LvrZ_mfrv32L4M_MUzKwtDuW5aKReYHyepyFZfCU7XT-4b4ZfY6eRVE0Tw-JX8mYaQeVBrjGZSSxd8v0kJXqZTQzOwTH4qhxZzJsl_GWMMSaK5GOD4xLtb6bq5Mnrl0bDVtYYSEOjLdBreZmC3kdw5yLhgiYXOFLxDeszorIy-A6VvpAPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
نامحدود فقط 90 تومن
😍
فقط ۵۰ نفر اول
❤️
✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
بقیه هنوز VPN حجمی میفروشن
اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 90 تومن
🏷️
💥
بدون محدودیت حجم
⬇️
⬇️
⬇️
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/125833" target="_blank">📅 19:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125832">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7e1602fd2f.mp4?token=nVNkLkQJDpdLDZG76LQ8Qp9HrmEHKsYjBZ000IvPl-DW8kiLmvbTh6QaDXGEIRxLZZEVLA0f4kYxSBHSQxwFtaXAyx4OwUk0w2dkwnKhz_BCqK7KX4ASlrMjI6XlF52eaXU6u57GtEevC6a-kI7sbL-R6WNVqkIqX7b66za8InF7u1mY-oGGgVnNFydOFVOhE4jaCMBsOWfSQQOq-7h4ETfiB_C38AJlTxqVPFHrKTocnz1tJMoWR2P6wNgqycwbF0WyGFZvHS7WwLMTHlYFW_6CnebffbavnxOhkpbDkNRyj-uSbenoqQeR2Q3bihJCeuPDu25IgJC2SeGFagQqPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7e1602fd2f.mp4?token=nVNkLkQJDpdLDZG76LQ8Qp9HrmEHKsYjBZ000IvPl-DW8kiLmvbTh6QaDXGEIRxLZZEVLA0f4kYxSBHSQxwFtaXAyx4OwUk0w2dkwnKhz_BCqK7KX4ASlrMjI6XlF52eaXU6u57GtEevC6a-kI7sbL-R6WNVqkIqX7b66za8InF7u1mY-oGGgVnNFydOFVOhE4jaCMBsOWfSQQOq-7h4ETfiB_C38AJlTxqVPFHrKTocnz1tJMoWR2P6wNgqycwbF0WyGFZvHS7WwLMTHlYFW_6CnebffbavnxOhkpbDkNRyj-uSbenoqQeR2Q3bihJCeuPDu25IgJC2SeGFagQqPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ با مجری دعواش شد و خیلی منطقی وسط مصاحبه ول کرد رفت
مجری: شما هیچ مدرکی برای تقلب در انتخابات ندارین.
ترامپ: من ۹۴ صفحه در مورد این موضوع ارائه کردم، ولی شما رسانه ها همیشه دروغ میگین، خسته شدم دیگه، من میرم.
مجری: ترو خدا نه، کلی راه بخاطر شما اومدم.
ترامپ: به تخمم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/125832" target="_blank">📅 18:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125831">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
خبرگزاری معتبر تسنیم: اسرائیل از ترس واکنش احتمالی ایران به حمله به ضاحیه در حالت آماده باش قرار گرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/125831" target="_blank">📅 18:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125830">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
پیش‌نویس در مرز اتمام؟
احمد زیدآبادی در تلگرامش نوشت:
🔴
ظاهراً پیش‌نویس تفاهم‌نامهٔ موقت بین ایران و آمریکا به مرز اتمام رسیده است. اگر اینطور نبود نتانیاهو دستور حمله به ضاحیهٔ بیروت را صادر نمی‌کرد!
🔴
نسبت نتانیاهو با صلح و آرامش در خاورمیانه مثل حس گربه به آب است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/125830" target="_blank">📅 18:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125829">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bae34bf9ff.mp4?token=Qkq2CDBeg20o8z_c7EWPMJbT3b_VB4Gqzwit47_K-DoMz6YcPEn6q9AligPIwaeKfbFfzdCQytGDumDPrwD2J2A8AcWAqDN3X81viVVweTBmwsDLWr_pL6R37e-DCTwY3-zPRVXftaBDubifGcsenidzw-Utsc_VQuWw7wDZJAcfZ7IF5SuBzQ5oD8_9_19-7f37fQXqD13qfd6Hiirwy0hAZG5vLr1UGbPa6E0Rt1cBPSzBirVKxrfKJeITRm4Wh5ocIdl0TL7VIYZsJPMuZuRCSADP99xcpDsy1AXjAF_1rKUCxcBjs83v5V7jbSGTmuYa8VCC2-YNPYkHtOUIbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bae34bf9ff.mp4?token=Qkq2CDBeg20o8z_c7EWPMJbT3b_VB4Gqzwit47_K-DoMz6YcPEn6q9AligPIwaeKfbFfzdCQytGDumDPrwD2J2A8AcWAqDN3X81viVVweTBmwsDLWr_pL6R37e-DCTwY3-zPRVXftaBDubifGcsenidzw-Utsc_VQuWw7wDZJAcfZ7IF5SuBzQ5oD8_9_19-7f37fQXqD13qfd6Hiirwy0hAZG5vLr1UGbPa6E0Rt1cBPSzBirVKxrfKJeITRm4Wh5ocIdl0TL7VIYZsJPMuZuRCSADP99xcpDsy1AXjAF_1rKUCxcBjs83v5V7jbSGTmuYa8VCC2-YNPYkHtOUIbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
من این جنگ‌های بی‌پایان را دوست ندارم، و این جنگ بی‌پایان نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/125829" target="_blank">📅 18:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125828">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seDRVCHpZJgC_itu_EF0CLGu1BKEyQFNTxcUKkRQFvcKB24RerA7JP0XEmTNIg5gsYPv4Cs1pSWUdUjhimt-_-YKWDqGX61FOo24njtRabk3E-Rz2c6gAPV0sNL5ds12Rn7Ccs5c8Am3UtKLkwIQZZoYUM6hkhxiIRYXg1dXlQgUJlCnoQ9l-ob3Er4Gjn9TLvvT1bEHgVrTen8wMXtj3ReLxvAlmCBS2vTPryN3aGsTbxnx4C68Y2b9rZtyx8299hQYoTKITpTwPtp5J6mrLIUOCOcAPRgHBnsu_xpSiHLRLSd5cl3h5b01o4wgi868yUgG-PH7PiQv_dsoHDsZQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/125828" target="_blank">📅 18:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125827">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4GX0F4PzGFEPRVkL9B5jkeV3DBbyFwcXB7J0P2eHsZh_yMYNnLqPW2F0PIL1RFrBRfniNL5EjG95vrFiyetcvxQ5Tp1z8G81BImDWWih5A1_h4xb9dZuaq0gpMAZ82JPar-GATm7LP8aQw4VRBxPMpGjjhkY5QMhh-QBs9u7wTbvStJMBiGFMbOYZwiIEWe1pFh6kfyAjk_dSQyY9Qz8tTOo_5yhNyQ_jrdF-akBccGyfeAADmOYo95oGJE8CUhprFgDGbkWFLO3Av4zQXkYzxy2WuQvQ8sP36jSW9va3jnggNvr-1w6TmTBYbWnVGEWkEwf-jDZwTeGXovYVIXiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پس تهدید رضایی مبنی بر چشم ها امشب به آسمان باشه ،حملات اسراییل به صور لبنان سنگین تر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/125827" target="_blank">📅 18:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125826">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کسی که بخواد بزنه تهدید نمیکنه</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/125826" target="_blank">📅 18:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125825">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
آکسیوس به نقل از مقامات اسرائیلی: حمله هوایی به حومه جنوبی بیروت پاسخی به حمله موشکی اخیر حزب الله بود‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/125825" target="_blank">📅 18:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125824">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kv0OHCSHWZpUJ9Zl_QwYvZh3O4xfv-0I2oOto2k8kTE6qbo-5SdQkrPHqn8hz-qgQuemz-Aj6kv8FhEPNonQITlgsS-oQNsuLVOdmxslnGcs1L3YMmjnhzcnqDf56oj_8QAw0XLowRrN2QXqvvrRThUNZ5IM1iG-63VEk0p2fg3cL_8Q7kWwKcVXxuaAVnYpJyl7FqYUXdTqn1fRUzdXZ5fqrVLZHQpjRS5kC6HFdMg8Z5oqklyxtimALzQffUuXyzo5OUBr7thLyxk12u4hLg5RIp4mGQTaLLRoCvE7lebONZ_BQPZVnWZLVa14uc7TwQ_PmI7NfCGtnaCggvArpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی عضو تیم مذاکره‌کننده:
صهیونیست‌ها مجازات خواهند شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/125824" target="_blank">📅 18:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125822">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOUga7NKl6erMYMLX5XvbXkiVeGFwet2ppxbWHXAQuRscqqOYPzc_MKrRLyITvZfrR1AgQ9bx_Hfi14U9dFQMjbr-eMK1U3fTrG4uPRTMtGuaVVeUTAZLaitMyagHR0BrybkIC1H0gbL6251il0wCZ22Lr7fjUPjY1Wby9oXm25KgLQWSsOL-nu3n5ALWEUo0nRkrIRA3PVsu-01zKMD60Kp9HwZrNfpnaUZU8xX5JkdJso4vcJ75lL_m9rusJxZk1XDVYfgdxxq-tJN5VjoKOUj2Fn22hdyvSMzR0HOPT_-A4G8thZtbw1Q33RPy-Mz1JveUfLtJ8ObK9nNTCs_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جلسه اضطراری شورای عالی امنیت ملی ایران حدود نیم ساعت پیش به پایان رسید و
«تصمیمی گرفته شده است»،
اما منتشر نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/125822" target="_blank">📅 18:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125821">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
اسرائیل به دره بقاع که از مناطق مهم حزب الله هست هم حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/125821" target="_blank">📅 18:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125820">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
صدا و سیما داره آهنگ تو رستم تهمتنی بزن که خوب میزنی رو نشون میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/125820" target="_blank">📅 18:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125819">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ip6J4da-JFJL5siRT2P-XgjBZOjkRRjBpuHQVhYmuWPAz02iRfXXrJh0jEHSAEQ7_wIwKcC8EAJqlbephybJzUqbJTxbnrB6ExJaRx9eVT2_kJO6zrv2OobUJu5PjETKytvV47fqzesH4EWYSAJkVSPUXFJ0JFPpXwNhKI4CCiTeni9UGmLNe6xOljkmhAKaiCsFi4g8eF7mhv95F297vf7lz2BE4TWTYECoWAJ1l7frON7_gq9tSozUBGspC6w46ui7bqbYPBJXmX7L7g9-TPZtR3OD9t0VNQh8hEGUvK8u9wvu1dtvE-gskIEZIvY9kDlSPDgduiGnjWauEtqYuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار در بندر صور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/125819" target="_blank">📅 18:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125818">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
احتمالا تا ساعاتی دیگه حمله به بحرین انجام بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/125818" target="_blank">📅 18:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125816">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDx889t9H0wsPIbdJmWzfOBj_p_ri5ch_UREVFzUlQbr3v_Dh3KXXsR9a2AvDjQvJweR0bdrZ9co8uxp-ZIcq3MsZdTM4lXJh3JrAN1fGoxTSkpPXhEH9LBpV8T7ZxBzHGSwxwoI4__oL7N-ecoI67Yluq66GWsNL9hXXFi5r2q3FuYJ4T01Kz9v5Aty2BTx-r39GU92j4jrAuhjwRMskLCyslCgUxdDM4Fl9YckqrBpMs4UXQbLeM8S1Lo3BUMv-hOe62HJxumXam6ZYGJuoRC6Wh75q95tusZJmMUIiDWiFU1DbQqamZpBTo9DSfHHy1-mylzZVnyrnZUNwNuewQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zf_yYZ_JNx382xSyoZ9i1TPb8iRVazQ2FPr0l-uRi_xA65i_-s52uhE1DPsXSkHamECCCYXU-pzcitgbnFvQSxyGFHuPLzqR-hH8GPh2rr5SVzFKYZqplehkajaaHMb4Si6pQ_XuID-FWhxhu7J_CylGkte3iFgfetSVYzoTTT_bQz095KITqoVC93qqpXtHZJPtP6976cmXZXclzwV7zRAb2ei76GMwA9UbvxpvBS9qJQqnHtlyW9sKylngEBk1LcC7Ddq9ruIVIk_arFXkmjJgxVbBqgzwSl5LVpq4bXvKlWPg7jfGON0Ti_OS3iH8E4FkbdhItJ3rZmgfueu4PA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
بمباران سنگین لبنان کماکان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/125816" target="_blank">📅 18:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125814">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8e6d5591.mp4?token=ez5M4SUof5lZXa8WIZYiKhPb4El9Wdq24bEEem-xNaQDB0EAUVw5wgAOapDlgRHzA5XzeF_vnvFwVA5iJslo2JRVcVFjFt0K4MneFzBHAJGzbYXeBbUd1KcPcLMOGME_fKnsYAGD8HNuj458c8dUVgw2Fvqq5EgbqTGnWVP3zRNjFuXd6nA3ySecK74G-r94YcNIMSmbD5xXfiqWEcA0bpLCF6nfJPYHaMPZ2wJjXzssm1PvRR5E1HB-wbN_5MqDWNx8XuNtPnCogAdU1ZEDiQ0L2f8WSGayDUvWb5iELqGD74S-P2RpiMLhu5V61RwmI0iMlpT_Sox1PCtO5R7ffA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8e6d5591.mp4?token=ez5M4SUof5lZXa8WIZYiKhPb4El9Wdq24bEEem-xNaQDB0EAUVw5wgAOapDlgRHzA5XzeF_vnvFwVA5iJslo2JRVcVFjFt0K4MneFzBHAJGzbYXeBbUd1KcPcLMOGME_fKnsYAGD8HNuj458c8dUVgw2Fvqq5EgbqTGnWVP3zRNjFuXd6nA3ySecK74G-r94YcNIMSmbD5xXfiqWEcA0bpLCF6nfJPYHaMPZ2wJjXzssm1PvRR5E1HB-wbN_5MqDWNx8XuNtPnCogAdU1ZEDiQ0L2f8WSGayDUvWb5iELqGD74S-P2RpiMLhu5V61RwmI0iMlpT_Sox1PCtO5R7ffA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همزمان با تهدید‌های ایران، ارتش اسرائیل موج سنگینی از حملات را به صور انجام داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/125814" target="_blank">📅 18:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125813">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/025910fe6e.mp4?token=rQxt55Yf2_UXJLUF5Od_68WCFRfNSw0DcJuzOgP2fljkI7QpXCXJ0LzP3yb6yhD1visOIFLet3sRpiY3Pbf6PjTDuaRPBxTmlz_dAXe6mW_9vPFSbwK6Ys4mDsZhZd8yH1PIsT4pk-WZXBcbbGSA_aCNOtJp3ulMwutqNjSRTEz4k7ampkVttTYNkV032eYl9ZDFQ88IYQh7AURlBQm-kwC9ednfW0OV2Wz8s_e4m0XzlZ9QacQviYJHOz3pOHs4ve5O3ZRBkQFDYBXnHQ25oMOLWODmQt7kXLGrDxDw9orSp8HqYCqQSTTbJfrYXJYDXuykg4L436EAp_vp8BHUqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/025910fe6e.mp4?token=rQxt55Yf2_UXJLUF5Od_68WCFRfNSw0DcJuzOgP2fljkI7QpXCXJ0LzP3yb6yhD1visOIFLet3sRpiY3Pbf6PjTDuaRPBxTmlz_dAXe6mW_9vPFSbwK6Ys4mDsZhZd8yH1PIsT4pk-WZXBcbbGSA_aCNOtJp3ulMwutqNjSRTEz4k7ampkVttTYNkV032eYl9ZDFQ88IYQh7AURlBQm-kwC9ednfW0OV2Wz8s_e4m0XzlZ9QacQviYJHOz3pOHs4ve5O3ZRBkQFDYBXnHQ25oMOLWODmQt7kXLGrDxDw9orSp8HqYCqQSTTbJfrYXJYDXuykg4L436EAp_vp8BHUqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات بی امان اسرائیل به لبنان
‼️
🔴
صحنه‌هایی از السکسکیه، جنوب لبنان، پس از یک حمله هوایی اسرائیل.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/125813" target="_blank">📅 18:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125812">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">💢
فوووووووووری/پرواز جنگنده‌های اسرائیلی به مقصد نامعلوم
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/125812" target="_blank">📅 18:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125811">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMeeBj7S87MV3Xw_Dga5c_jxb6nsmGnIQkQCWVIEWVw3z5UjvDK8dt4eLL0GeOx6x1oGdE6Y_fqfd2OaeFtDVmx-VKhWkqbnw7RVPnfjxbbrkVHrVSuQi78CepiyKre0BHOta2-EenKFlarFWh6ytieHF8KrMDan8BQYexOm1qZCPCkZ-Y6s4uQEp4vONjzvPzcIwoGFtYqTSCVXtcOwg-8igg969sZYIkZAybWf7Ie9mrwh2yq4hKMIcM6-8kDEOHwwZ3gDpfCWxiRzWZXaoZyQpSD0aSffBe7gQWmLhBJXF3V3OvA6a886fyg_aHsAU8w9SpX4jEtUwokTEgMhOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/125811" target="_blank">📅 18:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125810">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/125810" target="_blank">📅 17:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125809">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
اما احتمال اینکه یک عملیات محدود علیه اسرائیل انجام بشه خیلی زیاده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/125809" target="_blank">📅 17:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125808">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
صدا و سیما عملا به یک رسانه زرد تبدیل شده و هرکی از راه میرسه موضع رسمی کشور رو میگه! عملا شده عین میدون انقلاب که مداح‌ها سیاست کلی تعیین میکنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/125808" target="_blank">📅 17:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125807">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
تاکنون قرارگاه خاتم نگفته آماده اجرای وعده ۵ هست و تنها یک کارشناس تو شبکه خبر این حرفو گفته و این کارشناس هم پیشینه متوهمی داره و سالهاست میگه باید جنگ کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/125807" target="_blank">📅 17:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125804">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WViAWsco_IUUil2s9w4_thqySoJQLFcns8SkBzUU-TgNQJHGBGYafZQ_bhECkicP9zNF4S_RvV3VsXTpWNrUMAO83OqXJTeyXrwX9bgAdDxTclzxWT0P6ov89ai0F9uJ76ZfoebVXfnuMaHWR56k7OG5Eni6947LWXP5xtiEst2rs4J0JxK0dBvetagij81P-c-6erqsQFmtVC4qJbJLpCTO8hwYJcYHH-t1fywkU5duK2cOtEqDN_eVN5gUxHNN4Iorp5JnTDw-gmKD2yx7A1eGDF6Rjli3sQquLHqvWBPsy7pHzx0woV3L2IUZqBh1vqSkxLrAdp5sH-pJNua8Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17c821a588.mp4?token=DP1oCwA-4yVWHbKcI0TPWCX9A69OEHHE0o0vlzjhNH84hrR8qWNOF0JY9HS4xlrwEkemD53cnWAh-pxBOZxVdiq7I09ZLNn465udn8diSyMs2VlDD4yq7tynndMCom9sZ_yPe0LGq9r6BoW_Q1ItNmvnMnwC58RI8PmXBwecMdDGQVtm_Vpt87VjRyxAPBdOengkIY9YqcHyHd-rKLA6SNl5DkuKhB9rbGkunjc4bIQ-NEwrAnYz-jPmtgi5ZEa9wjOzhhahE9XmfxHcA14vSLhFkXMwnpMsSINSSAT0m2juvZ6unZFnVNB9akQHiX5bDozq0KhBiq3MD2W6kqPCLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17c821a588.mp4?token=DP1oCwA-4yVWHbKcI0TPWCX9A69OEHHE0o0vlzjhNH84hrR8qWNOF0JY9HS4xlrwEkemD53cnWAh-pxBOZxVdiq7I09ZLNn465udn8diSyMs2VlDD4yq7tynndMCom9sZ_yPe0LGq9r6BoW_Q1ItNmvnMnwC58RI8PmXBwecMdDGQVtm_Vpt87VjRyxAPBdOengkIY9YqcHyHd-rKLA6SNl5DkuKhB9rbGkunjc4bIQ-NEwrAnYz-jPmtgi5ZEa9wjOzhhahE9XmfxHcA14vSLhFkXMwnpMsSINSSAT0m2juvZ6unZFnVNB9akQHiX5bDozq0KhBiq3MD2W6kqPCLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات شدید اسرائیل به صور، لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/125804" target="_blank">📅 17:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125803">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
منابع عربی: تحرکات گسترده و انبوه موشکی در ایران مشاهده شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/125803" target="_blank">📅 17:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125802">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
فوری/شبکه خبر: ساعات مهمی در پیش داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/125802" target="_blank">📅 17:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125801">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
العربیه:پیش‌نویس قطعنامه علیه ایران در شورای حکام آژانس که ایالات متحده آن را تهیه کرده و پیش از نشست این هفته به دیگر کشورها در شورا ارسال کرده است، ایران را ملزم می‌کند “اطلاعات دقیق” دربارهٔ سایت‌های هسته‌ای بمباران‌شده و ذخایر اورانیوم غنی‌شدهٔ خود ارائه دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/125801" target="_blank">📅 17:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125800">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
العربیه: حزب‌الله پس از بمباران حومه جنوبی بیروت شوکه شده زیرا مقامات ایران به رهبران حزب اطمینان داده بودند که اسرائیل این منطقه را بمباران نخواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/125800" target="_blank">📅 17:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125799">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5346db6cc.mp4?token=Bedtyb6vS8ztnSbEZ_Qm7EtJYdl4w6X65vBeIldF02hjzvCvLEse_ePVwmACUFBsKvP10MdzjgL3t5BzvQEY_Fn7yFJFwqsZCoze0egw7vrDJ_VzGkHj9zMzqLXKxVYz-qZq8m5FkIcDOM8ERLZwii8J3w640F_GvVu2JhjIElmZGi1r0I7_N1XRcN912HzNIUf6HUNR4Reugj4Z6pvrjpnroVTmpa0iGA8N80FJPVwGJyQ8dAx_E9aJhH0dYFUobL6BaYF06yEa_MpuB5tJRm7PAnS05keCOKrzl3a1KpqRUbFjsnSDW-Y2dYQNzqHLimAJ3rkt0pQ4FKIwDOdL1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5346db6cc.mp4?token=Bedtyb6vS8ztnSbEZ_Qm7EtJYdl4w6X65vBeIldF02hjzvCvLEse_ePVwmACUFBsKvP10MdzjgL3t5BzvQEY_Fn7yFJFwqsZCoze0egw7vrDJ_VzGkHj9zMzqLXKxVYz-qZq8m5FkIcDOM8ERLZwii8J3w640F_GvVu2JhjIElmZGi1r0I7_N1XRcN912HzNIUf6HUNR4Reugj4Z6pvrjpnroVTmpa0iGA8N80FJPVwGJyQ8dAx_E9aJhH0dYFUobL6BaYF06yEa_MpuB5tJRm7PAnS05keCOKrzl3a1KpqRUbFjsnSDW-Y2dYQNzqHLimAJ3rkt0pQ4FKIwDOdL1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حضور پرتعداد پلیس تیخوانا در اطراف فرودگاه هنگام حضور تیم جمهوری اسلامی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/125799" target="_blank">📅 17:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125798">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
خبری تحت عنوان پایان ۶۰روزه ضرب الاجل ترامپ به ایران فیک است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/125798" target="_blank">📅 17:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125797">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOUp0eupLWalBEpJ8v7YYCYez2VmwQCYuAm6X_wgfV0B-p3hs_VBljiPnLFp5drLMuNdystCL0PXwtcIBVrYjxWOSkWPXC4rwTTqDrJTz8m4U-g6t7hHs-RUfndf6nMGlBFRd-1HHOkNRWlEbCYgQFXVhXOAnEZYWLNaG_w7PxP0uDdRK585JcOIYW6KOD6Luu9Gg47Ly6uZXHV5ynBM7rIaNhSnLpx5RYQDvmUyoYDDcAU3W_vLzwh4CnEobdU6YtiSjclzuAY6xbZzmx_hMs0TsOzzb303S5GsRmcDW_OBS1S6sTJyF93t79096bebWRJUwijEE3-jFrJw1IDkMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
👈
نمودار تغییرات قیمت دلار از ابتدای خرداد تا امروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/125797" target="_blank">📅 17:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125796">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
فوری/جبهه داخلی اسرائیل: مردم آماده دستورالعمل برای حمله احتمالی باشن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/125796" target="_blank">📅 17:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125795">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ترامپ به ان بی سی: ایران هنوز با ما توافق نکرده چون برای آن خیلی سخت است‌‌ اما چاره‌ای جز توافق ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/125795" target="_blank">📅 17:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125794">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
کانال ۱۴اسرائیل: حمله به بیروت محدود بود و ایران طبق ارزیابی‌ها پاسخ نخواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/125794" target="_blank">📅 17:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125793">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c568dbc38.mp4?token=BliCDPh_B87qlnbYkAIggqF452GNjKSw93ztYfKpYAJAvZIpnSKB9WPqvWt9gW8IWi3iQnTJp5h4UIGi73xRXJY-RQuPjEofgHuUc-0muzU5ahbwXYTx7PJ2nJnFCyGiBYiUHGXexyURpcMTJlA5Vt3tsa9Yc76eU4f1XWzL3hD5SgZWKVYWAxxwXU4yEULmb7bOEfJ0ZbTUTRkslpPvNmcpkj2VD_mkVjD3ZnjIVfTdGyXgRI0CUn7GyytltxoDeS-0oBG9gr624E9KbGf-s9tdjlrnBPsoM7pR-w2Kk3UZ_mOk6kj8-mET1NI42_LO0-loC5_1FDCOnB4QqQ1dpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c568dbc38.mp4?token=BliCDPh_B87qlnbYkAIggqF452GNjKSw93ztYfKpYAJAvZIpnSKB9WPqvWt9gW8IWi3iQnTJp5h4UIGi73xRXJY-RQuPjEofgHuUc-0muzU5ahbwXYTx7PJ2nJnFCyGiBYiUHGXexyURpcMTJlA5Vt3tsa9Yc76eU4f1XWzL3hD5SgZWKVYWAxxwXU4yEULmb7bOEfJ0ZbTUTRkslpPvNmcpkj2VD_mkVjD3ZnjIVfTdGyXgRI0CUn7GyytltxoDeS-0oBG9gr624E9KbGf-s9tdjlrnBPsoM7pR-w2Kk3UZ_mOk6kj8-mET1NI42_LO0-loC5_1FDCOnB4QqQ1dpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ
: ما یک محاصره برقرار کرده‌ایم و بسیار مؤثر بوده است. دلیلش این است که آن‌ها سعی کردند محاصره ایجاد کنند، و حالا ما آن‌ها را محاصره کرده‌ایم.
آن‌ها محاصره ایجاد کردند، بنابراین ما هم آن‌ها را محاصره کردیم. ما محاصره نهایی را داریم.
من این را جنگ نمی‌دانم، اما اگر کسی بخواهد آن را جنگ تعریف کند، خب شاید بتواند چنین تعریفی داشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/125793" target="_blank">📅 17:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125792">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ به ان‌بی‌سی: توافق آتش‌بس با ایران به درخواست برخی افراد بسیار خوب حاصل شد
🔴
ایران ممکن است در طول آتش‌بس، قابلیت‌های نظامی خود را اندکی افزایش داده باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125792" target="_blank">📅 17:16 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
