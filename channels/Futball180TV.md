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
<img src="https://cdn5.telesco.pe/file/MmVNw1imC60hETuqpU757ZhlgTDiyd4iDODdNCq437amDmWYoU4nYDbrBjItlj9HWvXutnlx_HylkupMIsL0Cy3CFqsDQJK95s4VW9Qt36QbklsNp3-2x2D0JfGFjcCEI00jArdJe6sQ88QUx7YWF1hTeh7K9EmpiQSONaE-JJXVY8_n3lPubkuVXp7CbZwrfjR-aTSrClHUmldCMQmw0F80gHgbC6a934Vfv2nQyxxMtm-eclCunApE4ygWWJ04Njun1JpZMNIFYO4Y8TupHfjshe4qDO-Gf67aK3_fYrwC6Z32M8zlgQ5eZwwrzLkltHofrIzw-EnRtLnltfvD3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 618K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 21:55:52</div>
<hr>

<div class="tg-post" id="msg-98912">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbAsl0cYVlhndB6gcCOSnJxRR265XeloRByqo-DX9cYtU7zd72bLmnjArwNn4wfuo1ncen5jwfZ331HqN1trcvTwbA-x70nREjrB6hYVvi9adO8PnjJtmnHUh_AHkNYbPAxl0Wur7FTW6dYStF8bK-6Tmjc0PI67n3nW90FZY5AAyTT_eBsJYGQNk5vkgJ6CIWYdGIXLwOd3lR5ugOLFBbC7FV1SU0tW6-rlRM5HJB8qrov2w6IJCiz8GELjJhuLbvm6-wZXkWxSJ7aa0eKdMS5gWYId5R3eeNSirk3okBbzICLJ9aWxk0gcXPZ8lG2hdIQL0R07Z-vEZQyovtDk3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپید بعد کامبک
😂
😂
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/Futball180TV/98912" target="_blank">📅 21:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98911">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
آرژانتین اولین تیم در تاریخ کل جام جهانی است که 3 تیم آفریقایی را در یک دوره شکست داده است.
- مصر
- کیپ ورد
- الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/98911" target="_blank">📅 21:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98910">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLztDppCpHjX7hjTEikZlve4L23-PeCdwpxuDTyG5vMcsY6VK36CfnbLiDL78-24CNJjSBUfBLMgWAQIPvM1hTrdyLFQfIprLH4PfMZZJbEQN6gGwiyTSkAAiVxdA7-wODtmzZZEsdYFIFo8zJOR4YVIxVgDNGQJXhIygjV0VeOM38p8aaabK3ST0S67gYedGyESpCQRnhhzyXM6yIXNBjiI-8UeAcKS9i9QuAjxwi3BLTd5ce7CAJMmoNzGGOaDW9O5QCOY1Cp6OOEXvJCjY5i8LhN1DHTzn-id9XUHvui0T38qdrHVRKmwoYRyTYilrl98NvyvNK2Q4YSWzeelOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
اینه فرق احترام به اسطوره‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/98910" target="_blank">📅 21:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98909">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🌎
✅
تیم‌های راه یافته به مرحله یک‌چهارم نهایی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/98909" target="_blank">📅 21:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98908">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmRQW-AXu07IF1NsnMf-SaiakLm22a_bIPEMT25oJHasAAKcgkDwyQPvhnkD5m9filihml3ffBwaoZo6B9ppZneqFKwFIloV0X6IreBaYXDOM2_kHUU4gkTdjY87XebST9kIsd78PsC1Xvtc_78TXKJHwfy7Ekf_GFscSJ4ZMr0vN-iQQylgECusH2qDDAawEppnb38RJ38yBZRxFRhvn4bk92sxuOemgpLY6JDY9NyRhvRiPphk-xLZFR_sVdSw2-8H5uILAuNeq6QUXJJmm3GpH5NCzPX7yWVkuFlAEc7AOH6-S-lUDTjFsvQDbx9db63pavkwYtcptg75EbwdYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
✅
تیم‌های راه یافته به مرحله یک‌چهارم نهایی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/Futball180TV/98908" target="_blank">📅 21:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98907">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5ozZDuPWUMSVh9nRZs_lxP-nd8Dtw2pbv7q_YNUOBI2ZMTrBH4JgEtma4s-sIREkapUhkjrCrYi0hBWRuyQEaV2xdiTK11eGksFytByTHvJKacyapJT80cFaLohFtWRz_R9xY-I75K3HsGV3qy1UmUFEZKoOF8bpxEhj0MS0QrB_4vXGvKZxPsftMfByg6QymElGNwPmhFfOUpH9gXqeHxXT3Ry032KHL9Cfh_x7QOa3PKVDWxM8fxEZuORRY4yWKr0GPA9QNFxW0P8a1n3zJx7MrUxExz-bx8gT1_nWtXS8rZs94T3shHXZP6d0-RrA84YNyGVVxqecjjnmFfMrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
‏بازیکنان با بیشترین مشارکت در گل‌ها در تاریخ جام جهانی:
‏30 مشارکت —
🇦🇷
لیونل مسی
🫡
🫡
‏23 مشارکت —
🇫🇷
کیلیان امباپه
‏20 مشارکت —
🇧🇷
ادسون پله
‏19 مشارکت —
🇧🇷
رونالدو (اورجینال)
‏18 مشارکت —
🇩🇪
گرد مولر
‏17 مشارکت —
🇵🇱
لاتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/98907" target="_blank">📅 21:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98906">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9deSeFH0d8Kvf74N21HWReSs74qCux20X1Is4VyqmcoMJvCtG7a6D5lPVrs9ELoc4Wrykn5Wr_53ZGMnW0AH9wnL4yucg5UF42k5jOxZ9sU5lrePKL2RNtWH3q9PsYM0gn2XfKEkw_XZYGAIcLFoz_eWo2_S2SJGEWagGqkic9UIaUBV2qIeFruGtTRBiq5RikIJEKoYZFYyq7flApA5DyzmkwH4EpgroVGcUDGeFhIsa65mg3fdEtkY4vb2IHDe-r2HxxRm8OAYgTsv--RWIcjxh_wTOJJEVdbJoa5xc4lF47WfzwIYcy56yhiArqRE8emGPyQLqR9uVbffE1pmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیونل مسی، اسطوره فوتبال، با کسب این جایزه ۱۵ بار، بیشترین تعداد جایزه بهترین بازیکن زمین را در تاریخ جام جهانی به خود اختصاص داده.
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/98906" target="_blank">📅 21:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98905">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8B-oLQLaIYbY5bl9dIZEeF9uY_2YsXcZfLrsfSiiLa_MfHR2db-kWE2dnL_TQhqoywJ_XJagIZ90bgHKbSFWrxwji7Tf7tioqsoaTgjtiPY1-NgRumKOrqj20MsD_O2fukCK_lkIid49osGmRyHmr_BbnUW-lJNhFAIwArqnq5PNkY-39JFoDjKprC646wdsfRG6A6CI6DRnJIl-lSokCYQON3gOBvMLwtBD7nUoaLK4eNX2S7vlZLLI1JIxAIaqw2HiAQyrC_PxJNkHIHfO7E8PnXoeJfz6tV9Y67OZCGfxUbqVQQmbmDlHoW4ebDdg8dBNH2nGCR0hYsA1uatdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
🚨
🇦🇷
| ‏اسطوره، لیونل مسی، در 9 بازی اخیر خود در جام جهانی:
‏— 9 بازی
‏— 13 گل
‏— 3 پاس گل
‏16 مشارکت در گلزنی در طول 9 بازی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/98905" target="_blank">📅 21:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98904">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhjSGUTeWV278OAo_WytSg-gJVZCBzM1JDi_RjRJskNaCKKIbkL7TuBzkdrRqBiEu_EaEz2W8A9673bluYXFsH9EYVyyb5LWW7OqY73fqGrYIcInGPus_F4vEJpx3J1UQ41hB4cE4MT9SxvnnCmgPaVsXIpff3Bg1Om509ibW70YJ_v0GnxDBiM80OIB2BtnUOwZ1CUgc9yc5jqS6F2vvEBOnaXSt63wWqRXnuXR-O_1u3iWefL_JqMXoG_M6BuTnzwQbxQjAA9QLWEW_M7Q7ykIKUmuHFj4_9TJuiSTK_xfNGHltU6LaAcWAi5ELdfjTXYOdnhz-WmtCPUqcNfX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
افسانه لیونل مسی، رکوردهای خود را به عنوان بازیکن با بیشترین مشارکت در گلزنی در تاریخ جام جهانی، افزایش داد!
😳
💙
30 مشارکت در گلزنی در 31 مسابقه
🇦🇷
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/Futball180TV/98904" target="_blank">📅 21:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98903">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjARa5DqMZP3wJH7qFFYkWd8VvbflOnU1Cry9B8HfZg8acexWxI8R4_c-YLknxujnJ9CSMc_EM0NqeIFKPPlOilqFhdM5n-zMYgnMJyxi2dTvCbK1P6cFfLrBIZ63jGrrhF4wQ89TbWEzk8gy_MdSxqa3LZqnXnVc3D6EEMd8ulkIolFbsO99Uc9JVBN6xHOTAZQkMYG5eBzHtlOASnEHHg__ODqnKlC8jlIA9QoGJNZ8dmWD45pW8AkiAXil1IvW8mOZRsQFmjTbd384Ccbuhm-RIKbkOs-bh6Z_MJyO4YZJuU2xCF1YQ-TqVJT1kOJ-kgd__NxI61jJ1kcmb7CbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🤣
🤣
🤣
خایه‌مال باختی کههههههه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/98903" target="_blank">📅 21:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98902">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8LTTIh3FC2DttCva8ymovO0_IPyzr46B_ZQW3FI7eWGftgCoxRmOv0J3oD3vgfd92GUq5k0JeJA7Pe0gzyesuX6fW5c7sSnoOBIajdiYOyPxk0hwlpyF5FXNnYe8u427JeBQX9LpkyHTYXrWmQZ0nSLDLBgkOLRCIHaa8L1yVoYPJKp1yGxLDHAigGiSIAHmTVAshv02aKJh0BVE2ILI9YqVuIrpZUj1hqXwQCkiiCwBs1vdNRT0S9dk00abBB5V3HjgrR1UU4xU5xi0a6cTVFMNKy0Oz18oxmxCtXjHLQiFq18SC43F3vMf0BVFEts1ZA-Dscad_BB84EWVM_VQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاریخی
معجزه‌آمیز
افسانه
🔥
🔥
🔥
🔥
لیونل مسی، بهترین بازیکن مسابقه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/98902" target="_blank">📅 21:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98901">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIpvXqD6kHvVHGQhjaD6kcmW1uWGpaEPGWVR8hsXNnxrlUE_U19H_tGGNzVmnZKmcLaEiWr-1NATpUodjlBLWD04fRCx6bSzBylZ_ikQrNeJYpfq3cjBh3e2HNpssbVraj5cRMGZ8ZjnaE4qgYF-F0bWvHZbqz1ynl0gc8K0a6pzWshvk0z_u-nwQ9ZXD96-B0rfIRKprearh7LM41Qc3YLFroP-jhXTD2YDQxSAiP6-0oiWmhioVaHhMA0wN7okJqCkx3kisSF1RaeMO7MQjskoiVp9PLxARYJqSl3ijhGgyWVfJBTvM7wI1PvfIMKW-sdOmjMdFJu8-xQaSuwjtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/98901" target="_blank">📅 21:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98899">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMSt_4Oc4BpBcmT1IqlL3NndESMndpTd5y2zeaICYL0DP4a6zud2puTLFXT6mDY-F9xWhmfrpMvPfAUozNacaAaFyZImfDkuNuoTQtajOo5aDtVPPCqAa6DTlpu48rDIt6n4exhmD8_IeB9tpM6K4lXafbDgJhVrQa0FC_FFLfjCBMeV1iyJF5lzShm_uR8mSbnWizmuBEINUj55C6eGG_WKTLwu0kyunH40nCmN9zLlz-lSkZE1UQ_7noByWZwpLRuh0A3piRrM1VOIMZ9m1Y0AV0JpbvUJ-6sAUVTBNACCk_cXnKk4Z7FA7uAsQs0h17VxRogOFCBYiRJm-htOYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LtX_sIpeYQeKocl7oBHqhVCBgVlXJ5ZsPuEC0wcuLwA4t3c731hf5bdetEOye6LINGVdkGdGM3zHO05c2IwZebSvJ32T7opgZ1p7Q5UPbI5iI_btmorkrVbcc4NUXeut-qU-IpYm41aG-ja-Yz2CQBMj-yx-Mt2PJoyd92FoGHMvJe0p7TSDEXo6eDN769jTGspUFl7tI_SyzQuTrNe1okaFONBnN9lBzc7kD_Tng8_CJHUaK0uJ0L3zyKFf4Z8x1ReAJxUQc3aD-DnbuVuin2X9tKB5ymkMUTvN1BnS5OU6EMBHo5fv0TVlLKYycf2nD0srpjMkheZM-v2Sg103Iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گریه‌های اسطوره
😭
😭
😭
😭
😭
😭
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/98899" target="_blank">📅 21:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98898">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhBLHU41OfdVvnhOUEJ_IgSSSAQBL_UHL_sw5rEjn20So3sTQlY8tIIpXz9X4jm0dG3zsoA9N9Zu5L4r2DfpYfY3CKR03l5dR544CKbEjIXAnqkq0May2vnilEs2fwvm6iwaBgKOfl9QcAeT47pod_Tw2Eh3m8SvvmI5d-DM9cCp8ykmzYRehvbZvrqvf4TfSCWZNEDSzq8qscEIO4pkxS8EDk5rNW1xkqvHETNkLPq-zJbLZVK017tuV07TLLfU8nQGmX6mWMj3idA0TsuqBAMozWy1eUxbo-10grkml4EV8-1-UUtEk2srAmj4_ZRyGofkGvoZ6MSFOuWHWigJuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گریه‌های اسطوره
😭
😭
😭
😭
😭
😭
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/98898" target="_blank">📅 21:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98897">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">چقد دلم برات تنگ بشه مسی این دیگه نامردیه تو پیر بشی اخه
😭
😭
😭</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/98897" target="_blank">📅 21:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98896">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKytMz9TxmowQGCkjXp2zyG4VKW7IlSBdZUWt2AgvgtCvXK4mL2I7wWhV0Ygco3Wj5BlxIcdkBGiyFMCJRz7Kjqz88-WiarxQCUKrRC2Q8Tu5hURP4iwB_1KPdiYjdJaHEmMdQmfzaRH907Toy7qNH08hGZWdQyc2fiWouXJp1UthP5p_jPRHNV74tXGrYtIknHmNTqEJedl-PR46hLAyHC30pRzgCBGEojnAqmiXgozgh6-eHJYJ6uTbUIpSsDPIndbGRnzEQX1w9Sy95fPQICf96MXXyi224dvh-t07a4V_1QoCvrL5-hezuA5WHdgT5ybdwX62XoEd61mLFS69g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|بازی تاریخی آرژانتین به رهبری لیونل‌مسی؛ مصر در ۱۰ دقیقه تار و مار شد؛ قهرمان دوره قبلی بازهم با خلق نمایش باورنکردنی راهی مرحله ¼نهایی شد
🇦🇷
آرژانتین
😆
-
😀
مصر
🇪🇬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98896" target="_blank">📅 21:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98895">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHfsGKSO6fL9tAniRtDxuI8TWfqrhxfgUMbpUUaDMeICMOwKZzJI0r7SD0OnSXMRzXqJLWVOdPQ2fxcbOipDu_ad58lnF9TRNdQNXYN5nDe9GsIRxO_9imTssn1MLfuNC9RM_lyP0ZuX9fYq-R9U0DmSchwi-eXy_gatVFMRn93zy7B-FA75KxyHrFTMVkwKj2PXj-sXWnt8plIkzP-tg1trNucLw04iMBTdTJ5hjOw7iOYazyBSL-MN2vtYtj-ZIqPn7lYuXR20DDf1giVawgrFWAxxVtqp_uCZTfzFcQeeuy4wtn8lVs9fb7OInwMnrmM8IMyROa7F86ASZ4dpYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرمربی خایه‌مال مصر زرد گرفتتتت</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98895" target="_blank">📅 21:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98894">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">الان مصر نیاز به میکل مرینو داره</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98894" target="_blank">📅 21:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98893">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UA4k7qBU1ud7-JzkvxViYd_gKtDNilY93hCAc0Ee49rXe1QBjOqIdJGjO3zjnTfL685X8BI1clpPqmpoesh3K4x0nta_E2OAno9AfHN6Bot1_yQDZ-ZrUbii5WpH4yrYqRNu1B5XAv4nWCdab5o9uEWAVUrWdU-kCN_ZHomlZUZPunkjH7Bk-H7AvvcQsS-I2SGyTS3F9FDPFmhHwgOJbKjtDHbfMJS_j559Y8lfd4RDoqHKvnjt1B-O5mdQ1Gp86siwlJDFmWZPUVCNUdQvfurz8keXTHFSJeeXYSJKZL0yO-9f0YJncCArQeVdc3o7c6GDehXuTPtji02EESaAEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/98893" target="_blank">📅 21:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98892">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
گل سوم آرژانتین به مصررررررر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/98892" target="_blank">📅 21:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98891">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">عشششششششششششششششققققققققققققق میکنمممممم</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/98891" target="_blank">📅 21:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98890">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کیرررررم تو مصررررر</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98890" target="_blank">📅 21:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98889">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">عششششششق میکنمممممممم</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/98889" target="_blank">📅 21:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98888">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">چییییییی بود این بازی
😭
😭
😭
😭</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98888" target="_blank">📅 21:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98887">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">چه بازی شددددددده</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98887" target="_blank">📅 21:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98886">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خدااایااااا</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98886" target="_blank">📅 21:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98885">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">واااااای خداااااای من</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98885" target="_blank">📅 21:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98884">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">آرژانتین ۳۳۳۳۳۳۳</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98884" target="_blank">📅 21:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98883">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گلللللللللللل سومممم</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98883" target="_blank">📅 21:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98882">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گلگگلگلگلگلگلگ</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/98882" target="_blank">📅 21:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98881">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مصر داره فشار میاره</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/98881" target="_blank">📅 21:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98880">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">۷ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/98880" target="_blank">📅 21:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98879">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsqALbIyUguoKJ38JTZpKsuY4nlvYiWgHrQLOIy1s_ZZ0Kfld8hnArn7U6RX8x1nVQ-stHerpG-Oy8wnYdpTKPIGfb9qK0Sa5M-J6OpNgKrl97Q8fVEMxMMDq64FSng2t6D5ze5HdLXZWKdF_VhOepzNfedNFC5eD7QhA5Pr6gKXkC-SVkHzw9IcHBdn_jzth2NeWDKkEF2SXFtnsaY2idCfsq76gSe17wihvioUgg5dPc7W1vFtGsJ4EBcEUPP1HHIwjaVCVL1Jea0RtiiXg2oclZOLyn6KVAYpbYBC_B60UT1RSszRJW45YKps3JTVgFFIvYOLWzO0BJxNeYuLxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/98879" target="_blank">📅 21:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98877">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a249f1935.mp4?token=mRDNUPDBIkIjvy8HOBW_GAXCIjks_Kg7MuwGs1U6tXRVH40TXVQv4-3vzwWTk0LEkLQvS6LhP65kUA1hSvDDbnt1FPcdFjjHgiH9xFalDVKW-Q0d2UALbX3alI54udh9y4jEeW1Q-ZAHGYYJmKWFbvIf9nJ1KkadzaaGcj-8uBr0i5MUlrtxdhk06FLmRe3C_NCj5aItjtryb1GFEG8s3wpbP6dPVgBSLSNNIYRBqE9ifJAYjTMKX8yCJ8tgnDrlkbPb3NVJ15Sc-rQjR7uyLFFR1i6fDVBJAxSwWa-6ExRgGwOeCbLy3CGSS7bOYrfAuFdUnkOSDx3-m5N_IINN_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a249f1935.mp4?token=mRDNUPDBIkIjvy8HOBW_GAXCIjks_Kg7MuwGs1U6tXRVH40TXVQv4-3vzwWTk0LEkLQvS6LhP65kUA1hSvDDbnt1FPcdFjjHgiH9xFalDVKW-Q0d2UALbX3alI54udh9y4jEeW1Q-ZAHGYYJmKWFbvIf9nJ1KkadzaaGcj-8uBr0i5MUlrtxdhk06FLmRe3C_NCj5aItjtryb1GFEG8s3wpbP6dPVgBSLSNNIYRBqE9ifJAYjTMKX8yCJ8tgnDrlkbPb3NVJ15Sc-rQjR7uyLFFR1i6fDVBJAxSwWa-6ExRgGwOeCbLy3CGSS7bOYrfAuFdUnkOSDx3-m5N_IINN_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🔥
گل اسطوره‌هههههههه</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/98877" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98876">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کسخار مصریااااااا
😭
😭
😭
😭</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98876" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98875">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">چی هستی تو لیونل‌مسی
😭
😭
🔥
❤️</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/98875" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98874">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">قلبم گرفتتتتتته</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/98874" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98873">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خداوند فوتبال پرودگار فوتبال</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/98873" target="_blank">📅 21:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98872">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اللللللله</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/98872" target="_blank">📅 21:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98871">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">این مسییییییییه مسییییییی کیرتمممممممممممم</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/98871" target="_blank">📅 21:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98870">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یا خدااااا</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/98870" target="_blank">📅 21:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98869">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اینننن مسییییه حروم زاده هااااااا</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/98869" target="_blank">📅 21:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98868">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مسییییییی</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98868" target="_blank">📅 21:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98867">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گلگگلگلگلگگلگلگل</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98867" target="_blank">📅 21:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98866">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گللللل مساوییییی</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98866" target="_blank">📅 21:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98865">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/589518b23a.mp4?token=PiFe2Lm4gB1d6GiID1Nl6iYxgWISL8yHbolwtmrPzL-koujmkV5aDI5BHVC286m2QJIgosixNSIzFrJEaByAD-yK55ByZQxfhKVnu3-Hzzvm8r7xPemhTh_6gdaj67CkUAz6uPvhYOKahvKJupjXS3k95wPqy5ZehRI1ZcZ5a2u9EVgbMx3BmRuIqNh5psF0CPD5xIu2lPspWCQdizuHMLvUzG83mqinf5Ci69mspdKmPfB54DNCej9U-afXbRkd6Ctnwvc5iNK2QCm6eK-wQW8uZodmL_YhQZNW-RrOtO3K3OSM3R7-sVfV0SJ7ls1x00c_zQIVLecjV1HGuqfWhg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/589518b23a.mp4?token=PiFe2Lm4gB1d6GiID1Nl6iYxgWISL8yHbolwtmrPzL-koujmkV5aDI5BHVC286m2QJIgosixNSIzFrJEaByAD-yK55ByZQxfhKVnu3-Hzzvm8r7xPemhTh_6gdaj67CkUAz6uPvhYOKahvKJupjXS3k95wPqy5ZehRI1ZcZ5a2u9EVgbMx3BmRuIqNh5psF0CPD5xIu2lPspWCQdizuHMLvUzG83mqinf5Ci69mspdKmPfB54DNCej9U-afXbRkd6Ctnwvc5iNK2QCm6eK-wQW8uZodmL_YhQZNW-RrOtO3K3OSM3R7-sVfV0SJ7ls1x00c_zQIVLecjV1HGuqfWhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول آرژانتین به مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98865" target="_blank">📅 21:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98864">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وااااااای داشتن دومیو میزدن</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98864" target="_blank">📅 21:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98863">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گلللللل قبولهههه</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98863" target="_blank">📅 21:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98862">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آفساید نگیره</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98862" target="_blank">📅 21:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98861">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کامبک؟؟؟؟؟</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98861" target="_blank">📅 21:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98860">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اللللللهههههه</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98860" target="_blank">📅 21:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98859">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گگگگگگگگل</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98859" target="_blank">📅 21:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98858">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LP-I6J2jFbIV4Q1U4rvPir8U-LpCfP7kNCg73bhDRI-TYkmUlqV52--RO-vwHM8cmv1J-z6MBPDYTL13JVXbqx3bTOgwskA8O3aw9ut46pv6whysM6z49rg0Wsmn0LpTddXSBHEp81wh-zLudQM2jkYgtiW5Ebsi9_70bvBJlQdT-olj-_q9sRMZDH4nxbgOuRTarXvCWJvenwmyTIyy-cZY8f54EfU_-3vRR08Y7XvemcjPYQaJtMj5X60XtjP-Rsxh878PEhwXg_3RQwUJLjm-HJd02mDOAhZ9FFwy-L7FTm2npHOL8fdTTzlbkgV4myQag3EhKwdVg3UMUaRvxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💔
💔
💔
💔
💔
💔
💔
💔
💔
💔
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/98858" target="_blank">📅 21:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98857">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تاریخ شهادت بده که مسی امروز ریددددد</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98857" target="_blank">📅 21:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98856">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔥
گل‌دوم مصر به آرژانتین توسط زیکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/98856" target="_blank">📅 21:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98855">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مسی بای بای بای بای بای</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98855" target="_blank">📅 21:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98854">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">باورنکردنی</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98854" target="_blank">📅 21:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98853">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">زیکووووووو</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98853" target="_blank">📅 21:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98851">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دومیبیبییب</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98851" target="_blank">📅 21:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98850">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مصرررررذ زددددددد</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98850" target="_blank">📅 21:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98849">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گلگلگلگگلگلگلگلگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98849" target="_blank">📅 21:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98848">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نیکو گونزالس و لائوتارو دارن میان</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98848" target="_blank">📅 21:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98847">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نیکو گونزالس و لائوتارو دارن میان</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/98847" target="_blank">📅 20:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98846">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxvKLSPXcnLUOtwxj4tG-SSqpDQaIK5TKUR5eioWTaABiYNL6iuExCFO8A4IWWRDm-vxLg1W0oq928G5CoyRrN5FoYzCjFUFHIz2HEkWaY3Xzt6Qr2mJyCLbgAJyVUMnZQYU_Q5eyYYI_hLqWfXAIsyyLAk_CKAir5uWpaq2NL-kAl0DkfYZXyzOOt5OCJp_mJoTuZoK9xM1dRLfcRQj0BzFGpBP2oEAOZeUBi55vXbIi4W_FeTW2kod28Mp1TNc7grUPPeU9xLrf1ADFqONJ_5xcs1VrQz2pzIuv_FTwDQC3GGGJ916NxxF7hlKvq5C1aFC6-mcu6fHjwP4naP6fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گل به درستی مردود شددددد</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/98846" target="_blank">📅 20:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98844">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
🚨
گگگگگل مردود شددددد</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98844" target="_blank">📅 20:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98843">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">صحنه داره برررسی میشههههه</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98843" target="_blank">📅 20:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98842">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خطا میگیره احتمالا</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98842" target="_blank">📅 20:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98841">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پشماااااام</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98841" target="_blank">📅 20:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98840">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مصر دومییی هم زد</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98840" target="_blank">📅 20:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98839">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwSLu08ahEdt0qBy76VTQxGw6wOpfBieUE5IJgwMi3Vmud7ejJEQBIk5VZHqj5ITuSz_CcV1ou4aso_X8KMhbgVxatdh6Ipp9lGk8jzciCT2eGprf0OrVQPuUmAonTO1cejZNhcoRGCwa12KDs6Rk8snc6NePJ68Xglykd0s7hN3SZJsb6C1qdcGzCOhuo_ehaxqswTj3x6qHyw3ue7MPVqqMo8oJIXk0v3OzHaMS_M_UngNo3CIFhYrdGSDzhaqeS3RSovf2znTT_-JSMTnd7b7FQ_CoUKt4apxS5VbMeh4vP-nPmJt1HZm---ZTR7DtQLrBLxOcdlMScPVsGQtkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
| بازیکنانی که بیشترین تعداد پنالتی را در تاریخ جام جهانی از دست داده‌اند:
🇦🇷
• 4 — لیونل مسی
🇬🇭
• 2 — آساموآژیان
هیچ بازیکن دیگری در تاریخ این مسابقات، بیش از یک پنالتی را از دست نداده است
🤯
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/98839" target="_blank">📅 20:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98838">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/98838" target="_blank">📅 20:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98837">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g5emP6dSa2Ceo1kjmPAPcsJ9kxwW7ghcVYQ9OtZlldyMBpZSjttANerVhIpRLHo_PixX3byO32B8JThZuym8e83st6JRFcLxSJhNWlfzQzgUEUjERBcc2ZrgfkyquqIolPn0E8aQmcyyKJA78x8N6nhuk4T5-Do5kt2pcLMYCdxgYH6B0ygo3cQww0tbElFOSRiZ5JSkPlzp07AuGBjNQNKhJYYUBaNavkCILcbE7oF893gcOjgyT8L0NLpmdHpCPtIvf5_b-udGWM0Of2USir9VajvU-H1afQP9C4YK_dO5oObPXOf6sotdYmePrJeS7yWTQk9v8od5DwLzG84IMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98837" target="_blank">📅 20:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98835">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
سازمان ملل توهین های نژاد پرستانه آماریا به امباپه رو محکوم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/98835" target="_blank">📅 20:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98834">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7dgPL_PAkhCGiagQOfSooX4hBAEaZT1ArEKeTMMr0rqKYOYst9LEAmJ1K7W2tnPgVS7KMiPwft-fr8Aqbn9aZDEToqNl0YkdvnLwlLCpRFqSgO_oh-YL2u5l73iaMpxeaAlkWNbm7QhjJ2W6NkR4Tgv-b_XVbgF3OimGO2Yz5KnCk-zyLejGJTrP7nfI6BwebnuJVojL2acqQcIWSN18xmEWsXjT2Ke82hkmWyHB3xTQQjDFq0iOHLteEL_F_g5G2ZTbItxxHNExTHB3hxRQb986V-wAKbzUT4YGuLuB1ol3VbTOg776hzp3-pc93d2f3uCmNMzZFYtng64fEGMgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیونل مسی اولین بازیکن تاریخ جام جهانی است که در یک تورنمنت دو ضربه پنالتی را از دست میدهد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/98834" target="_blank">📅 20:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98833">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پایان نیمه اول؛ مصر 1 آرژانتین 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/98833" target="_blank">📅 20:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98832">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بازممممم گل نشدددددد</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/98832" target="_blank">📅 20:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98831">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/98831" target="_blank">📅 20:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98830">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mobIRwUWpKnPBTsw3V9oVMH_hr2Dx04CUb_RT7A2Lsy86iulFmHVjI2dpXlnI16vadEE5zPDC5iMAFdt0K2H_J1Rw0DStMvPsAD3vXVcB8furO_23sDCmeZD-lJZSK0n8vLk3LUhwh9ezIzN88NxmxjXpbaFTrffyOtsOTltlXBPy186Wqne7xt4sPF5eqKAAXsUosd502-Ooh-AQMbwp5bEL9YISpXEMXcPgi72i48Ch2CsVVIhzgHLuL-Vx9qAvYa-mk6gjhihD4-fVpU0uVYNh7Mgrb6wK-2g7nHMC3yOEQeCAm7j6AVLMVcHbscF7B42hknlBJLQqlTQ2Ipzpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی گرفت بیناموووووس
🥶
🥶
🥶</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/98830" target="_blank">📅 20:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98829">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گلر مصر امشب پرایم بوفونه</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/98829" target="_blank">📅 20:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98828">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مسی چته امشب</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/98828" target="_blank">📅 20:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98827">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">شوت مسی به تیرررررر خوردددددد</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/98827" target="_blank">📅 20:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98826">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">چه توپوپپییییی گل نشددددددد</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/98826" target="_blank">📅 20:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98825">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شووووت مسی</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/98825" target="_blank">📅 20:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98824">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/98824" target="_blank">📅 20:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98822">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گلرررر مصر چه سیوایی میکنه</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/98822" target="_blank">📅 19:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98821">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مسی بازیو در میاره مطمئن باشید</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/98821" target="_blank">📅 19:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98820">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
پنالتی از دست رفته لیونل‌مسی مقابل مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/98820" target="_blank">📅 19:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98819">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e3f5039dba.mp4?token=X3JcdJdjg085wdKFM7OLUpAgzvlxq13AaqxsYe_iRefJ2zgOBG_Q-fTYtaVgYknzwBaRmIEcw5wQgYeuQWGny6RDz22ixGsQsdHmtYA52s7etWXqj-bNWlTRcRIWYS-BYGQKZKkCILs6eRJmem81mOWfHnQDITML0IUrSNsJJMKgeNwhqDs4QKyA79DWFmdTOQBoHCpu8seZwZ061MKFjBUbDwkNeABZjl9rJq4M0ewDNhMJBRAW7uVZYEInOUGnyyrPaRXSxVAPp7ymVEEj3L2groNUdHBKLXqR_pWuFa4DEE_ihf74I0iZFseD3A_qKtCSmHkb8TOIU-bqqYvrTQxlnnFJan1bNMBXbfAml2-nmjYbybZkYmSuZvZrrRmvHk-Bt-oX3ZsoIXLunR3ShqJo4yt8iTIuRp26z2A_7u8QnblvbpWOH2--VXu5I11VVA-ooVQBdbM9u8pgO3y7t2eZAHzfPJFdetsBDCPfXhY0dbI-_olK2nbh1JP4KMe9d1v8NJP36GyxXeFKZmlU-GuM2TEyAPbTOkSqpCRkcm6Yca18pex8OwCDkdoe-1YM3ar0TxLLfPgjP3tnpL2n-o_10FT2f6IHBk-Ag8SC4lQgkAds4Pm4rMzs7ilk2BV7BqFk55KOO_OJ9OOQXOuKD67DYZFzy3NfpZ3vHsqO1xs" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e3f5039dba.mp4?token=X3JcdJdjg085wdKFM7OLUpAgzvlxq13AaqxsYe_iRefJ2zgOBG_Q-fTYtaVgYknzwBaRmIEcw5wQgYeuQWGny6RDz22ixGsQsdHmtYA52s7etWXqj-bNWlTRcRIWYS-BYGQKZKkCILs6eRJmem81mOWfHnQDITML0IUrSNsJJMKgeNwhqDs4QKyA79DWFmdTOQBoHCpu8seZwZ061MKFjBUbDwkNeABZjl9rJq4M0ewDNhMJBRAW7uVZYEInOUGnyyrPaRXSxVAPp7ymVEEj3L2groNUdHBKLXqR_pWuFa4DEE_ihf74I0iZFseD3A_qKtCSmHkb8TOIU-bqqYvrTQxlnnFJan1bNMBXbfAml2-nmjYbybZkYmSuZvZrrRmvHk-Bt-oX3ZsoIXLunR3ShqJo4yt8iTIuRp26z2A_7u8QnblvbpWOH2--VXu5I11VVA-ooVQBdbM9u8pgO3y7t2eZAHzfPJFdetsBDCPfXhY0dbI-_olK2nbh1JP4KMe9d1v8NJP36GyxXeFKZmlU-GuM2TEyAPbTOkSqpCRkcm6Yca18pex8OwCDkdoe-1YM3ar0TxLLfPgjP3tnpL2n-o_10FT2f6IHBk-Ag8SC4lQgkAds4Pm4rMzs7ilk2BV7BqFk55KOO_OJ9OOQXOuKD67DYZFzy3NfpZ3vHsqO1xs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
پنالتی از دست رفته لیونل‌مسی مقابل مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/98819" target="_blank">📅 19:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98818">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بابا تو پنالتی زن نیستی فدات شم نزن</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/98818" target="_blank">📅 19:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98817">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">واااای از مسی دوباره پنالتی ریددددد</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/98817" target="_blank">📅 19:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98816">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گلگلگلگلگگلگلگاگلگاگلگلگاگ نشدددددد</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/98816" target="_blank">📅 19:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98815">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رییییید مسیییی</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/98815" target="_blank">📅 19:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98814">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پنالتیییییییییی برای ارژانتین</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/98814" target="_blank">📅 19:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98813">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گل‌اول مصر به آرژانتین توسط یاسر ابراهیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/98813" target="_blank">📅 19:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98812">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وقتشه اوس مسی دست بکار بشه</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/98812" target="_blank">📅 19:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98811">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پشماممممممممم</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/98811" target="_blank">📅 19:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98810">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یاسررررررررررر</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/98810" target="_blank">📅 19:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98809">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مصرررررررذ ردددددد</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/98809" target="_blank">📅 19:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98808">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گاگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/98808" target="_blank">📅 19:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98807">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گل مصررر زد</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/98807" target="_blank">📅 19:46 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
