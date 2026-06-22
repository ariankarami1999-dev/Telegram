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
<img src="https://cdn5.telesco.pe/file/fKriYYvzTOiAeuufOsxubZX_fSB5eZK6sDHlveIFM3P0s3lutitTCmQbMztfOeGuuY8NM9VLh834NtwtuEaTCpofk_3CiMoG2MCQLDBdtoZ9anvYiZoAGueW9bhfia6EUZYZkqWrhT1pyrJiLe_LNK7OPUpdEM8teBgmz3BdSPI4QfjIQTuQMwPkXUoyJJ2_xTI31cmCErv1-lJ2uDX39YyhiYjb3gVbHYim-ZLMQsctTiekOJZAMlwV4X8IwwT3VO5PrYKmMvzkTfLpYvfyETOKNjtBenZsQctk6XUF0s_SeqQS4rz9S4537G58MF8_-apzpI2dqMUHNul-THt2tQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 724K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 02:28:59</div>
<hr>

<div class="tg-post" id="msg-95340">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhO09q7xksAwmlTZUNOfBsdXt1gOrPdQJeIaEV_dQj7CT5YhC4dqvPWfQXSRZ_NnZNuhJmvP5vELq_UxJ8szT8KLPL7DU_P5iVsyxRJMAPe5PQ_mzJgpTBt4QU3mEmcrOT2OrD1qcIhutv2qSo5ZmMFro1HgOxjWrlJ6aZwXbji9Slwtf-OUZU0-xCCTRwzDT7gFuYBAnbc9DUC45_Qk_v6CDbY73UcNuYg-s2PMln49x1Y6hHQvNaLr5qDgzBW9XTOC0WPlRoqcrNQh6fXV6M1eOo_hgMsf_hCzl34RIir-5kCAoyitU2i6nRgifHSNr0NsTonHpp2MJCGS-GJSLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇳
ترکیب سنگال مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/95340" target="_blank">📅 02:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95339">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
لکیپ : بازی حداقل با 50 دقیقه تاخیر شروع میشه، حدودا ساعت دو نیم به وقت ایران بازی شروع میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/95339" target="_blank">📅 02:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95338">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوری؛ اتلتیکومادرید به آلوارز گفته حتی اگه کل فصل بهت بازی ندیم، نمیذاریم به بارسا بری. تنها شانس رفتنت به انگلیس و آرسناله که خود بازیکن کلا رد کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/95338" target="_blank">📅 02:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95337">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtumAJUI1bjU2h_MZejlAYtN9Zvrku4q2RcBULM7SsVqETSRY2nYCO8OWpKhxs7UIi_nifZEfICxGAurDiYqwCdckMpnQwb_VD6qEIgk-GcQUsJQe_1WiUPUPHfQpZcip9Workugf_OYBpfY-lcKP6EujD6uUAoEMNJ5GnAAuyyIT0xJDKwBZlX5qsS5kup1n0ib4J_N41d9nnq6FXg4cgEZ4xCxry1L9N9I7wKA4pDhENJ2YHD3wksYntDkdVlVTPIyPtg7yrUzkiG70lLjRHvIscNlJF43z7IMp_GgEJ3sOCW8CCvgaMGhHE0I4rX8DJutGNbFIxUuviAN47oFVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوری
؛ اتلتیکومادرید به آلوارز گفته حتی اگه کل فصل بهت بازی ندیم، نمیذاریم به بارسا بری. تنها شانس رفتنت به انگلیس و آرسناله که خود بازیکن کلا رد کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/95337" target="_blank">📅 02:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95336">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBnGMyG2CjdSGZcF805M68A5aGRpPQ1L6LGnscPl1UM5_2dk_4jSGTO7gq99JvBJhUAtfWJfQImJimrykCBX4RPN3k6jZeeYiUB_gWYbBWpk1zuRqiEAluZCfjVXSCOlfiqa2bGE5nYdsJFMNYq6vfQjBypnG8u-AXEzH3dBOmHtsPCEj8t7T5k1LTQ5dj64QLH73zhnnxa_AfM3ZKFIUPQEgMJ62zCkjSaR4AKSO__GZqinvTIa59rKBE5km2W1viECEM8ocNCbKk6-uCerHMVvIZco5-8D-LvE5iUflxf9SCq-YXm7NNTX7Hbaap1GiHIqCz9EgDegpsevwZCuAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چیپس پنیرو تو استادیومای آمریکا میدن 8 دلار
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/95336" target="_blank">📅 02:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95335">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری؛ اتلتیکومادرید با ارائه لایحه‌ای از بارسلونا بدلیل اغوای بازیکن تحت قرارداد به فیفا شکایت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/95335" target="_blank">📅 02:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95334">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkUS4UNrBQwRr0t6Qrdo2tfyAaa424dDsSbKrkxMLn0qQfFpg_zbXtB2anl35mN_8w9G618Ucnp3bi5_Tojm0XwkCYYkjTyB0AwIXMYgbyfDgVXw_F6fJIu9ahAwG7HMoT0OZR12CB-jpCHdy-AFbTfAZzucT4PP_KmoROSOqbshtI96zldRRHl8fu9_BCfFzzUViObTq6AtD3XpgaMjAZd-4xkwvO-1JPo0BDKsVRPI42ZlsE7dFSGtw0Ri-8kLZSvsQzz4Gi98AAkADtr4-9OZp_oyXufDHYxNZa8nfyObgrDtfdimIVNt6rlOmDfmc0MKg3xfwlbjn_hOo1DF2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇳
ترکیب سنگال مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/95334" target="_blank">📅 02:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95333">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🏆
نیمه‌دوم بازی عراق و فرانسه حداقل با ۱۵ دقیقه تاخیر آغاز خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/95333" target="_blank">📅 01:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95332">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووری؛ باشگاه بارسلونا طی روزهای آینده پیشنهاد جدید ۱۲۰ میلیون یورویی را به اتلتیکومادرید ارائه می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/95332" target="_blank">📅 01:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95331">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciun67hUYyU5hlUm-QtMwJ4SkiKQQ8m9qEJG9gvg5XNrCp_UtqMbT2UenjBy4Q4g2KychrzjrsPqPgd0rjG4z-KyIM7o0912bx8cA4sGX9h3461fVnUQoC6c2m6DIqlAHDhuiaLu9YIfIm-7DV5bc5WRRXlOa3cKUPeL8MYKM4fKo9VswgR2UexARouqBQ4FGOXFvvmG-K4rUsx8UQ2xi1YhzdADe4BBI6ydcyTOLdBbuJ69G1VYtg1swRqaUZtYgo32H2D8JNXwIPux3h27gbTbikia2MOl2YImDwe7v5Ia9C_fmgs5km1pL41lS8oTf3nE8xpHX4yrAyHdRWIuKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرشیو وار:
پنالتی فرانسه در نیمه اول سوخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/95331" target="_blank">📅 01:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95330">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DByfw0_DetnSsxyCYm4YJabul1vO5ypcfqRcs1L0T75nlK8NK5eaPE32owcYuK6fNmKqou_saGRe7kRAf26eJ9_2aSWF6ku8xDTB1ZmafuF8R8HL7z-fzxU2VtsaaFqAhIzyLj7YEzW8HB-blcoRYE6_MhmOqHUTh1MJVNUaRuYNUIA2gniDDBlf8CGwJGvEeNXfdFV8Y-fH9arjG6rWe75KT9DQppvIK-N04T_CoZDjnjSXkGrPS2nHKXwKEd3dFe7CsvrQs86eCLDUakq6iEc1Y9di0WnZSNzR_wU06JM10luMAkGlx2ZZwfXDJfpQhPd9nU-ioM4QTecf759tpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووری
؛ باشگاه بارسلونا طی روزهای آینده پیشنهاد جدید ۱۲۰ میلیون یورویی را به اتلتیکومادرید ارائه می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/95330" target="_blank">📅 01:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95329">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sX5nt6clXi7xPWKweF-czEcpwfRxTGZqR-HKvIFKlUc4JUX7B5K7BUJb5G0pEwdQ6v-ejK64GLl6ZqhVQuf3crdt5pbwyChu15clEaVf7iJ2X2zoBHYF91N5uMPItcOGlq2o8e5me_qWi53aH0zrGdZ_dvw80NJ3tRlgUybHKCMkNX4bFpEnmyFOJ_kzdvHCwc51T2oVFmN8KfJdzcmtycJsWwY4IpGy7f5U9yrCyM8ok2ZtUX3I77TP8jfW9sRuxeb6NaTZpv_IL2q8S725q3FXyD00Ss1wzydWd1ORU-m_TbCH4C4yRp1itOMyOBIUr3qCvOHR6M-U397R-IzcCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
نیمه‌دوم بازی عراق و فرانسه حداقل با ۱۵ دقیقه تاخیر آغاز خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/95329" target="_blank">📅 01:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95328">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🔥
🔥
🗞
#فوووووری از رومانو: بارسلونا با آلوارز به توافق شخصی رسیده و اتلتیکو از الان مجبور به مذاکره میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/95328" target="_blank">📅 01:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95327">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پایان نیمه اول
🇫🇷
فرانسه 1 -
🇮🇶
عراق 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/95327" target="_blank">📅 01:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95326">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wk39N_YrDPRte325QYoH4F6TYizila67x-WXpNxVJwPoCDaajh28QjbF3fzkFB2L-PGXKd2hLzd7_3ONGOsRTO0aae4hzP3PTol-xeGuOsKGr2dYGtNO5PQpODYcMrBRzoRY1YXL0Vs9Q2DIvpnMn_CmFDK90Dpi9nwL4DrrKIi79pQ9JGAeNbMsg3oIPNT-NASiTi4omLWaH3OWx78e1vsmvHNbqyq0a_cNq-rjbxYZvUPZFqqjyOywvlo6fts-uPduyvCyCKQe9wny1ZNIv7lEFQPhhktYxniuHi1rHFUilCPLZNU58qntzTb50HapC9LfmMHbFcEP6jX_CBl54Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارون تو ورزشگاه شدت گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/95326" target="_blank">📅 01:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95325">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tm9B_G4C3Vk4rhmC-zzA-1NqHnqr1JVxv9Lhv5EfDSo6DJOKR4I_nmwjTeR7W_LHv9wljQqxVwVe1a6tS-NAZNXfmGYtCEaLw8mJoU4XhlHQ4V9tlcLbLXeleSMXWbiyP4BF2ie11Olp0-wYusM1gRIouexLU59yPdsWUzH8bUKW1NJ61O_ZElWvW0evqUkuxHNfYCNTkn_fUuYFFj10Ex6PhVU88gEXD5-g_-3P90fxumDrllHbf11i016kjhIMrEIJAzDN3vmjkxo28VKRrXNBfo-XCrWIFd0trYzVOKPYaMSevGAP7L6fsvQcqq3oOeK-9FrQLmzPoSmBnfeEFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکل فوق‌العاده مدافع عراق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/95325" target="_blank">📅 01:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95324">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری؛ اتلتیکومادرید از خولیان آلوارز به شدت شاکی شده و احتمال داره جریمه سنگینی برای این بازیکن در نظر بگیره. آلوارز اصلا قصدی برای حضور در فصل بعد در مادرید نداره و فقط و فقط میخواد همبازی لامین‌یامال بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/95324" target="_blank">📅 01:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95323">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHaXfNV2KPW7Ua33dtpzNQSYL6VTX2LCThI5-Bl-GCOSHCGgcFlyqRu5Kgoqp8M_KCpM65TLyFRlHkTYNQVXtGQg3dltL_TNDFh3PquSupJTVUCl74qL-v9e-358Qeh1xbrLQdfc6MhHz2aSH9xlViD43ZIMOSeaYcsBvfrWDNBRMiyNHcMydXGW2jrLv3N6soGb51B4_2L0sSCGyTSj6ahaMla9PeiyzCCx5S82axDVAXZar8DvC5zTmqz2hLxhZGx5V8YnHNBsfp82lPoQIKBDQ2A5KyNRiTyt9S6-x4KiRSKXB63vELgVULqqU2QKV46LNj2xArKrc9MGgxttjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کیلیان امباپه به جوان‌ترین بازیکن تاریخ جام جهانی تبدیل شد که به ۱۵ گل زده رسیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/95323" target="_blank">📅 01:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95322">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHfRbql4vyC_gvijc110ivo84pXeOqSWQjjSSts3V4z3x8xi04_K549A83dW63f8xE9WqKjO85LsHcKXseTpmnPIX6dRoctHUOSWVt-HLjOHPgauDhIMo7i1blW1gyeG9h2G20nDyzjO8LC1eo1QTBrfR0FdhpYD9e1hHLumfTnwuEYx0nCazg9Ah6uh8TXRCmNDkZg9KiTwlR6bfL9PSbjA0ROKeJvWLJPbUFcVQSVl1IoL_8Xkb__xLfy9kl9uPjNoZk9Bbn57YHnDHB8WCNkNvgoO04sRPBmW74RNnjTwg-FKlmjHcn5WOmQLa4n2vewomPEeJH3lQxgWmD-6Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان امباپه گلش رو به پدرش که توی جایگاه تماشاگرا بود تقدیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/95322" target="_blank">📅 01:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95321">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a9ad943b75.mp4?token=MPhED4gIaIyRvGxfGSb2cPLvEuNVucwhQikDiQAU0zn4WfAkHOFO3Z7QQssXaQQYueuw4jBH4O2h2R76FvZZuvdgC8MnoCv3Mw_4YDyBPzm-2Hy2PmzuJztG07gkuzu8w7Hgv7Dnu5HphapZjjnqo4D9wQkXEHHZqrpbe431t5ya1uNvMX4Stn013kKgHekmlPb4vyIJo-l0_Ex14e-Ue7FO_9Qcr2nYU5x57ckcjmupfGM3BZxY0PWdXOnIMi7R6ngFkZ_AfVI40wlVybFidDo8hgYsotgXA-BGN8gzED4xiHahqCZjXViE28ve_FLa0OicDCu6PIrd3rOBMugzsYr3YrxrsGdwHkQrBGLR-bNRC_O7SoaMVkjOm4ZvfAb_t7N5-Axml0GYxFSgL3RJZ7ssd67UBnqpQ3vsJfD-0PLklHRx5HU9mO4BIfqluaragcvI1I2XpelNtLqmTrmdNF54Rc55nP7zgCMwP-GK5qlzUWEOJFMVLzg-jfeeCSRF-u4BL23DsCP3vA6cT8Po0BXanSHDZ83ATotSVC-ua0rFGjLmp5FzEh4hRIdzQZs2cOqWApxEwVeJDK5VZajxHet511t-Ab4lwd2xEyN3ENJgjuoeetFjY0okJed60L2o2bp00kdOZG-RsAHwiJ5ymdW1CR3Aim9DgQvDh92vgcM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a9ad943b75.mp4?token=MPhED4gIaIyRvGxfGSb2cPLvEuNVucwhQikDiQAU0zn4WfAkHOFO3Z7QQssXaQQYueuw4jBH4O2h2R76FvZZuvdgC8MnoCv3Mw_4YDyBPzm-2Hy2PmzuJztG07gkuzu8w7Hgv7Dnu5HphapZjjnqo4D9wQkXEHHZqrpbe431t5ya1uNvMX4Stn013kKgHekmlPb4vyIJo-l0_Ex14e-Ue7FO_9Qcr2nYU5x57ckcjmupfGM3BZxY0PWdXOnIMi7R6ngFkZ_AfVI40wlVybFidDo8hgYsotgXA-BGN8gzED4xiHahqCZjXViE28ve_FLa0OicDCu6PIrd3rOBMugzsYr3YrxrsGdwHkQrBGLR-bNRC_O7SoaMVkjOm4ZvfAb_t7N5-Axml0GYxFSgL3RJZ7ssd67UBnqpQ3vsJfD-0PLklHRx5HU9mO4BIfqluaragcvI1I2XpelNtLqmTrmdNF54Rc55nP7zgCMwP-GK5qlzUWEOJFMVLzg-jfeeCSRF-u4BL23DsCP3vA6cT8Po0BXanSHDZ83ATotSVC-ua0rFGjLmp5FzEh4hRIdzQZs2cOqWApxEwVeJDK5VZajxHet511t-Ab4lwd2xEyN3ENJgjuoeetFjY0okJed60L2o2bp00kdOZG-RsAHwiJ5ymdW1CR3Aim9DgQvDh92vgcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول فرانسه به عراق توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/95321" target="_blank">📅 00:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95320">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دیکتاتور چی زد.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/95320" target="_blank">📅 00:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95319">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">امباپه اولی رو زددد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/95319" target="_blank">📅 00:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95318">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/95318" target="_blank">📅 00:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95317">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doIxpnHwUBiw6Y-WNcoH17fDCUhrfzxMx99uiCpsrkbTl9ufU85vG6sGFs0T3kNhtgmoSaoMyRTzy-wOlX0VH8V9oABetRkoSm3x6YOBH-Es7ffStyrPEIzxmnfEJlJazd7e18mm4tBv3Qu0OdUoOzoyKNyohlP-GeijdQzFh8_ITjpc-VbWsBXgZZKbG8jWX0wUM4PtAbi45U2Mwo2j02JrIfM3N8_LrEbEc7wPRPyK-kqSSvif-ROJctBCQ39UPpsBP__QPQjXf_thU6koKJFxfYkLomaRNqDp3q0hQfxG2giMRPs4mn2Squ2m9fyPKsz1OO6E_1_j22Pi2f9q9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فووووووری خولیان آلوارز: من می‌خواهم رویایم را محقق کنم. با افرادی که باید در باشگاه صحبت می‌کردم صحبت کردم. بهترین چیز برای آینده‌ام رفتن به تیم دیگری است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/95317" target="_blank">📅 00:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95316">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hg0Ki0uq8qGXONQhO3MKDHH1KTFaE4H2gRnM1yY2Mw91ATk1e4t3GFUvDMnmGKSBnal8yeK4c1Zybh92o3jMwtpkg0YsF_qORupoHG9PBUvC2_dRNCkAKX0e1Ay7unyMeO5AY6U3vZIz1MFDfxHJtQQLbAIYou7rnYD2a7BCdX0m5a6CqIWdulIwBFHGqRsqsOlHmBDIEA2AErHEK9IWKyCTJbDk6cvhgK4sL1wBIhU9YlRTEzjYHL3i-eFrluUOJoBxflSmazNMjWHiokV3YJglTK1o7FAkR8eQzFF5OMVMW9XB1MpiWomSMNGQyhKj23XKUx3Pr1TM2z6oGDGjdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگار خیلیم به کارل تو تعطیلات بد نگذشته
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/95316" target="_blank">📅 00:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95315">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EcwF7IzocSUK08HoyGZlsGd5OJGkbVF3zfalHH6kgeaMujUHUCSEAFnMYYFD6ajItBU1mgzT8sfdnD8CjjllKDcSUfSh3BK2xWP0yOf_JbbWL1fdgUsuyymN8B4XarXZCi89ZrTBNDQTPGoVvEji2Crp59viLlPEn29GjUS9sOdDIiikPVRQoMtXmW9EhW6Ac88UTGEv6KEoiK-MVmWqEk5STgeBNNHS9aR1WHotfImOjnZbBvwjbUT-LeE1WVn_9audwkPM49CQTx1aXfpJuPRKEhRYit8tEYSYuCCJcjoqH6IO3Sk1n4SWNAZOuUHje640yR7jnlHGnRvDlED1ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔞
🚨
🔹
اوه اوه
🔹
🚨
🔞
🇦🇷
⚽️
🔞
بابا بنازم طرفدارای آرژانتین واسه مسی سنگ تموم گذاشتن ؛ دختره بعد گل امشب مسی تو ورزشگاه جوگیر میشه و
ممه
هاشو میندازه بیرون
😋
😍
⚠️
🔞
🤤
برای تماشای ویدیو روی لینک زیر کلیک کنید
👇
👇
👇
🖥
🔞
https://t.me/FoootyHub_Bot?start=qcipRV72
💯
🔞</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/95315" target="_blank">📅 00:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95312">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
فووووووری خولیان آلوارز:
من می‌خواهم رویایم را محقق کنم. با افرادی که باید در باشگاه صحبت می‌کردم صحبت کردم. بهترین چیز برای آینده‌ام رفتن به تیم دیگری است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/95312" target="_blank">📅 00:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95311">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بریم واسه بازی فرانسه و عراق</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/95311" target="_blank">📅 00:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95310">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUT3x7g8l85o7ZxrwusORtT0gH7xwWV8Y7sWebzk7uWPZx9hnWBvLwnAlIPDd9BgmSz4FmdR1zaklsrdktNyvLHDB4MGQ4V5e4TQzQAw9MRJu3zyIriVysVFLSoOyMcNeVEU20jfowkCXqHlLYhflSHEivc2kfBI69iJN-wIpxxzOIk7NjKG1ajMwJ7VujIfAiLrnapSMbr-fTU0OZghChcjvAQEM1tjX2zaW2T_HIBofL-1TWXfdcLF2MVojVa6vV6h8oFo2mVHMaR0J_d74JGNr9ugHORH35UtGp0y0Tht_S57TZ6fPDR-WE4p6fHjhKIPtgL2TA_7xKGi6nhL-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
⚽️
تفکیک گل‌های لیونل مسی به کشورهای مختلف در جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95310" target="_blank">📅 00:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95309">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiXqgCv9iiA1ZliadZaYWX5uYMNEBR6I3-PNKAoK2JsJY874ehbJQD2WgtukUcaiytQoZXx64FL6ahcg3g2Ma_unhfx148qbW50lZzyctorxq59TwUVsUyJoZoXX51QPsBe0EwF4uidSV9pFAGjCavO7f2ENyN1gMF88x6_6haZMOlaBKckBMnMKYTdkrhEBsLqcKKWHRXvqYjD6ntYp69UD1eVxPg-i-YNqvo8t__wTD-tr2aI7QJg6K3SyNnXC3U-3EWqktspv1_OBPkdeFRanl3ddO_E4gOnY4FuDLyH_SLQJvd6YvMloOA1UnHb1kL0fpC1plcF5SsHz_Rfr5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آلوارز :
مسی رو با کلمات نمیشه توصیف کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95309" target="_blank">📅 00:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95308">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpFTWPa4iYWO3R3bhVKaKUFnJTqoZg3P-hCsiddefg88mB0YhaU2FN22ThV7WQOlWbdIgNlQlprp5gXODCkjBQDfErMH4BiccIUZMgD0KRGDoMacH2orL6IaeDc-Z6pzE_zzgO_FRCZ1-Pu-ecL5ot6OSvx6C4YixpzfaILisNx0KkMPdTFdFkzrUM8J6DmBGTMPgsYiodkWWP0tvOHIjgfHRr4F4-U2d6pm040jZcl9DFd575j3As3Js5C_oSk_ILemaL-hA_j_7l3Ui_I46r2ZFxCXOqg31GJbL59xMSU9mZLXaXo8KrhGXFrSOKV0QKILaGs7iW3ojirprP425g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب به تنهایی شرف عراقو میبره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/95308" target="_blank">📅 23:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95307">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dm8MYOP2AHwGixtdDwbcOAQf0_DymxUmNfqK3uo0Zh6oVDAQ7DgE7cjY4V-QQK6sWU7qF_OaPRYKOEh_vPv8N6N9XRoQG-5PzEdhNjGxhh4pF7NvSpHwYV4cZBuuJtlF0uhGM18uhgpjkGtSQ-m5rqtc3Ser76fu-5eMFTc0DAfoOMN_GEsoxJdh9LDKYv9dymxXybIeMKjSOocoVhwyNHI4fgJu3dpScgmTJzBAntnTyfTWX5HTEP2OewtmoLhFhJXr8msnZj2BwnETcsJ3utri4RvsRei6fVF14jEC3FI9UkRkOz2eLNiLtnHWKINxlTC1tx69o0uqi9nUVGvHjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یورگن کلوپ: ما هرگز بازیکنی مثل مسی را دوباره نخواهیم دید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/95307" target="_blank">📅 23:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95306">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a6777a2d2b.mp4?token=ArZprQG_SwVN5HadyfyGJwnLMvB7qgmX7YH0oOWGX5dw7LTQ_Fm--iSAhOsLs4fllqk_e8SjamH_2QKFUanixfyG6uT9j1GaK7oNpMM36qYlN6XAlTm3mZGnvNEcGaVxGydda_zbgG88x_0dflWQidBbP8CHger3pMw4AvJQCOY6v-xjifg5f59fj9G5BIqqrOkGQpBn8w8l9-PWZU13M8JGAwXYW6MTRWIUrHNSI4gKjYabBXRRNy8GVHVAOu9lhR2YN1BbG5IpjiFVJAaeptOgQUBvRBXBm-yGSCzRFdJxMmYKrLsuU3CCvCWytUglR3yHYy7-2jGzCfj-loaJNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a6777a2d2b.mp4?token=ArZprQG_SwVN5HadyfyGJwnLMvB7qgmX7YH0oOWGX5dw7LTQ_Fm--iSAhOsLs4fllqk_e8SjamH_2QKFUanixfyG6uT9j1GaK7oNpMM36qYlN6XAlTm3mZGnvNEcGaVxGydda_zbgG88x_0dflWQidBbP8CHger3pMw4AvJQCOY6v-xjifg5f59fj9G5BIqqrOkGQpBn8w8l9-PWZU13M8JGAwXYW6MTRWIUrHNSI4gKjYabBXRRNy8GVHVAOu9lhR2YN1BbG5IpjiFVJAaeptOgQUBvRBXBm-yGSCzRFdJxMmYKrLsuU3CCvCWytUglR3yHYy7-2jGzCfj-loaJNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا بیرانوند: بازیکنان تیم ملی می‌گویند موهایت را نبند چون شبیه یارهای جومونگ شدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/95306" target="_blank">📅 23:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95305">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb3ab2e493.mp4?token=FOn-Yg_Pk_4pv6WdsFHVs10y89fCHpWqQ5ErI8z9YdXmfuONP9nP36ipVZ4VZwiW6omdvslrk4g2NW8kBZPVxVYNdK-SnnbD89kQgCfC2UUZYLe9SJJ26rXtdPw4_XaHnw9KrduKTqUsSJeD_u8TK8XTvjEuAg4J8IbHYGGhpTxNHKckV4GS6EamoJgrEpPlbhTTS4iD8WN2yEdoHailYrl1yjh6K-CjjR7QFI0GHHzb5Oe-l1si9l9NPByEsCAeUmgnYtsWwRw5DP94Nem4sPdLCjBpLS-Ifk2jbEndKYOO04RZk-de0nVJ0KP7CfRavwEiZqwgSK2uIoq6-uc4OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb3ab2e493.mp4?token=FOn-Yg_Pk_4pv6WdsFHVs10y89fCHpWqQ5ErI8z9YdXmfuONP9nP36ipVZ4VZwiW6omdvslrk4g2NW8kBZPVxVYNdK-SnnbD89kQgCfC2UUZYLe9SJJ26rXtdPw4_XaHnw9KrduKTqUsSJeD_u8TK8XTvjEuAg4J8IbHYGGhpTxNHKckV4GS6EamoJgrEpPlbhTTS4iD8WN2yEdoHailYrl1yjh6K-CjjR7QFI0GHHzb5Oe-l1si9l9NPByEsCAeUmgnYtsWwRw5DP94Nem4sPdLCjBpLS-Ifk2jbEndKYOO04RZk-de0nVJ0KP7CfRavwEiZqwgSK2uIoq6-uc4OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارزش دانلود به شدت بالا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/95305" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95304">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
ترامپ: پولی که آزاد می‌شود برای خرید غذا استفاده خواهد شد و این غذا به طور انحصاری از طریق آمریکا و از کشاورزان ما خریداری خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/95304" target="_blank">📅 23:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95303">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b7d3caa97.mp4?token=seAnughIg53hKeX6emPN-RiEntH21lzMH1XourilAr1rKQBee05N7OzrOD4feNRPBGp9crJl8TCoL4f04Rv_EhAWWidOqso15EOupZHQNtvA9XGu1Q6KuNYWfxAstM4X-OOBigxVCyQOfa_drv_R21Wycs8QoN_hZweUOrZTAx0hO6regqSTnSelELcAQ2bbvuN0ETn4-lLZLOlbKV9fzNrLd_JuSa-gRYrcDRFcHy-OTNJDPm6CVfuvGJYY9WyFUJR5VDyTc50Z8wFkXYjnholcShCId-JwvSgDhLJbZLTTafYrt8KrOTfpzM5PgsdPAXI_wsTH-BXwtbkL8cOKZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b7d3caa97.mp4?token=seAnughIg53hKeX6emPN-RiEntH21lzMH1XourilAr1rKQBee05N7OzrOD4feNRPBGp9crJl8TCoL4f04Rv_EhAWWidOqso15EOupZHQNtvA9XGu1Q6KuNYWfxAstM4X-OOBigxVCyQOfa_drv_R21Wycs8QoN_hZweUOrZTAx0hO6regqSTnSelELcAQ2bbvuN0ETn4-lLZLOlbKV9fzNrLd_JuSa-gRYrcDRFcHy-OTNJDPm6CVfuvGJYY9WyFUJR5VDyTc50Z8wFkXYjnholcShCId-JwvSgDhLJbZLTTafYrt8KrOTfpzM5PgsdPAXI_wsTH-BXwtbkL8cOKZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معیار دخترای مکزیک
پول، قد، تحصیلات، استایل، بدن و...
❌
کره ای
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/95303" target="_blank">📅 23:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95302">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d02fae5a3c.mp4?token=LVUmeRui1Ox7SZqv7mXOGQ7swA8pVsyM7qK8c38AYjOsPaYInL0N5yFZklMXepJLxokTk2luwA1kzepuYfqxr6SDQ6WXB3v0Wj9fksBtFC3Vwj3mWBci5uhanIWGcWzRPOuQ7y7P2b6m2CKoHFrDEzTRBnYqPea-QVsVaCAXZE2H9tJVp1Y--7vU7BctuwDIjMMuJFwPzHqCkq_523ZF7maEu8ae-yG2nXjhYTeYKJ2-9Tri38pIekcKYSGXdSTsLhMO6SoW3tb2vkOMWQG9d3tewjdcqxc4RgH2UdYoTnsGE4K9NJZqrqQ1yg4xlVCOi8eqwwcCbn_sEcY8_FiV9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d02fae5a3c.mp4?token=LVUmeRui1Ox7SZqv7mXOGQ7swA8pVsyM7qK8c38AYjOsPaYInL0N5yFZklMXepJLxokTk2luwA1kzepuYfqxr6SDQ6WXB3v0Wj9fksBtFC3Vwj3mWBci5uhanIWGcWzRPOuQ7y7P2b6m2CKoHFrDEzTRBnYqPea-QVsVaCAXZE2H9tJVp1Y--7vU7BctuwDIjMMuJFwPzHqCkq_523ZF7maEu8ae-yG2nXjhYTeYKJ2-9Tri38pIekcKYSGXdSTsLhMO6SoW3tb2vkOMWQG9d3tewjdcqxc4RgH2UdYoTnsGE4K9NJZqrqQ1yg4xlVCOi8eqwwcCbn_sEcY8_FiV9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا بیرانوند: مردم ما ۴ ماه سخت را سپری کردند و همه تلاش خود را کردیم تا دل آن‌ها را شاد کنیم و شرمنده آن‌ها نشویم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/95302" target="_blank">📅 23:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95301">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNd5bwL6YDD9ZHvpsob2597pPJfgfseiXTm79mrmmLGJs7uTGVWmN0CH3nedtADX-6JOAvAvtkCcMslNGoUt0bePHEapLSNLAFyy1RkuJfPXZA2MapKDovsAeoLJHw0Il5Yca3dQUT7QsYmCTdX5ujAKTd5EeytEK6heMM_e4yB_VCg1M1Ch_w7mNxenN1EdlFx_-CVqs0hCNq7fiaRkuwsDtl9-fgNyfZLMZr_2JbJ9s1qXVb6NUQGmTV6JGZrQugdmD7P8NGNDGx09Dy8Y38crRSkCHKg1UzaShY3pC3IG39jOrPMLLdusXmpItOsalZf6OLk6t7Q80dyUe7_WHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لئو مسی با جایزه بهترین بازیکن زمین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/95301" target="_blank">📅 23:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95300">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYoHsutZmUAiznsbNME47CDEA2td_LfIbq3dSbQ_ITM_5fDXTAxKSLCI71y8RAZ7-ifIYXWjWvAqDedczlSOHxTOfMEc79QfaYv-5rfLoQBO04KW6AmXv-vAobZMdwRWmCYmIBLpXnep-EfpLpwY3w_91Zs4qQNwKj3s4iFgrQaMGUGySvlTt477c1BQTiwZrykhEsnqiC71a49UMujvJMOF5iJpAZH3ejHNpKmPRB2Ojlot4RNjQH5PvcDE2G1Wg7K0qcbQn_HOvZnTa6NJqm7i_7ALDZABcPveFyUcSMNCcBT8SY4tNadYPN1UxGg7jZXtuHC7a79dUWG6dQ1w1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی در 4 بازی اخیر خود در جام جهانی 8 گل به ثمر رسانده است که با کریستیانو رونالدو در 23 بازی برابری می کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95300" target="_blank">📅 23:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95299">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dee5f09984.mp4?token=hH8QjVkwyIDa6dVxY4gQt_ESXDmg924PBTCQQzoF1vCmFLpFQO2IVSYaBtVaWU1UJYmXJyxEcPhNtybbf1KI-a5YCANzg-LM77x-dmHucT_ci1J56yLBZ_JmGNvS4QG0bA6UuSPKu0yf_XlHw4MfNHboZ03dBTVnHVFXLrnVnExBT6Aho8OFU_NaKjLCA9udL5_Jnqc7BVMtvNZicI022GBsbu5NWHfqnvLxDHzIe6U6pOqQhSo_ABIM6xGK9BNBp43jwjwaqWd_S7iQDZ2yG2qcy4tfAuZy_AQ9eppEiH2G71hbK-FVrajgRmJKSgfY3GNrXkinTYRNKYlzBl9-9E1g4uZEPDW9T5vjXi-CQyZNU7VUEr7NYzymbgHSRFn7Iez6uR3vvku1GcUUzESXSc_NMKPFs8TEOGI0gCyc_9cx_i0nx4oSmIPAZH323qOT9ddwNLG4aWhskc2BIT0ajW9gS90cdoowcLmrOajJVniENQLLgExGqi8UMq-jBnUg2rhto81-her6mBn70KAcK34Z-mKgcrd-9UyufHAudmeIzqViafpRtGxfamC286ZfrTTlk1yEkhebAezhaGAZbhbQCtD8WFg_nz_6eNA9AkJsgXUAz5gcjBf-i4mPWtMwDvDcRCdACAh7V9QfuLTt4FDsrWvaxcW6L8ULuCoGnGI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dee5f09984.mp4?token=hH8QjVkwyIDa6dVxY4gQt_ESXDmg924PBTCQQzoF1vCmFLpFQO2IVSYaBtVaWU1UJYmXJyxEcPhNtybbf1KI-a5YCANzg-LM77x-dmHucT_ci1J56yLBZ_JmGNvS4QG0bA6UuSPKu0yf_XlHw4MfNHboZ03dBTVnHVFXLrnVnExBT6Aho8OFU_NaKjLCA9udL5_Jnqc7BVMtvNZicI022GBsbu5NWHfqnvLxDHzIe6U6pOqQhSo_ABIM6xGK9BNBp43jwjwaqWd_S7iQDZ2yG2qcy4tfAuZy_AQ9eppEiH2G71hbK-FVrajgRmJKSgfY3GNrXkinTYRNKYlzBl9-9E1g4uZEPDW9T5vjXi-CQyZNU7VUEr7NYzymbgHSRFn7Iez6uR3vvku1GcUUzESXSc_NMKPFs8TEOGI0gCyc_9cx_i0nx4oSmIPAZH323qOT9ddwNLG4aWhskc2BIT0ajW9gS90cdoowcLmrOajJVniENQLLgExGqi8UMq-jBnUg2rhto81-her6mBn70KAcK34Z-mKgcrd-9UyufHAudmeIzqViafpRtGxfamC286ZfrTTlk1yEkhebAezhaGAZbhbQCtD8WFg_nz_6eNA9AkJsgXUAz5gcjBf-i4mPWtMwDvDcRCdACAh7V9QfuLTt4FDsrWvaxcW6L8ULuCoGnGI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیرانوند: مهدی طارمی قبل از بازی یک سخنرانی حماسی کرد و به بازیکنان گفت اگر سر خود را در مقابل بازیکنان بلژیک پایین بندازید، بلژیکی‌ها ما را له می‌کنند و آبروی ما را می‌برند و باید در تمام لحظات سر خود را بالا بگیرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/95299" target="_blank">📅 23:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95298">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0hWZT4SGgLyg4lOEzMXL2snggsXEpj_BGVLq5ALfCpjdwKsl8DaO3pgiHLgcadixk4_0YNpk6W_ZSCIBXMj_fM3bnPk63fXR7FbJLRakbhRMbTC_JIE5cLpWqnbpYb3dPv6kyyZWoExBeHLubW1GiXmEAmr5Rn8ZF9xGoP6ZBuWdBtqoDQvthspGSqtixPBjiCNNYJasJWxqnXoV8fdcX-bBApxTWF0HFqlOTlKr4jiR9mNnFcpchbsanj1JZaCYCUY5G4ej3-uwEabxAMN_WHJEVVQoxfnwcOgYz-eWj9RB-2NTilEAM9F0ZF7TOIrXsfwXpTT9sY1L5ekvEG2wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهره کلوپ بعد دیدار با مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/95298" target="_blank">📅 23:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95296">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mJZn9QuTteE8UjvA6hpb7IxPTQEG6AJo6u3pDqpDrU3-yJodK54Hp7cx0wgFYoS1hvfph3dtSyMILcgWPVZf4IvtOQEaZXhAJqNp746UhA6jjFPMd-mlGieFeYXEj0bN1EObcqXC9qa_yxqynmyjhzcRz8YQJ0nZRPz6G2NQKUYv7RaLhaNXi69dSCxAl4OVMYkwpda7DimZrV_pQgWV8BYeMWWcQ3p7RxDbIkr-9GNQ1RrbHuqEcKwJj1WD7AsYPyv56jgk-Sgpx8a0fcQLmwdKR49VckOhYJch-KGnlAq_Ewyk9cw5vNovFTiotawKKIHU1EpNjwl9AbH6MOY1sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nIHm2PCsBe1abkaOiFmpFu_Kg2MI2FexabIEsruGJNJr6S8iNAQ50X35XtHjfTyq5l4P54fWlm-2t4HRwYRtdg-LO5h5IvfEAdJCGba-PVy0bQUIqRf6E49INmvXN313j_kuMoiif_54TYSVQUX2hYF6ptAKaEZ4BpeY3EFfCyNJa1lOLj4jzKweh5GHFvBwoRZ4z9mM31n30w_aTZbUyqPpL9NC3pc3NqErvk-jDRA-jp05InTwDXVkaS8qrAyo_MkKcWB5MiYwcVSrujPVEHA0cdpgY1HBw66KbZEKYHvTIBTGCTfmU7wgRoenR_GjjE4JXytTzQfArigM0CX03g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
میزان توجهی که خبرنگارا به مسی دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/95296" target="_blank">📅 23:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95295">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7151d02512.mp4?token=IZQQMO7EMNhEqu9urxGV7ZuzZlIHg0JSwrcZTsvDnAncsdcShoYcDXjzSSJfJLtqGjqP47lyk0Pv1QLac9EXfMCcOVXFcGElxUx1qqdIM23ilcrEt82x7Xb7znzAXLf2I_-lo9U1rgN2iB45sT9qTP1U5Tz0DymSZ36nus_k-Jgu32WThIWXrCL7Ntqe-JWYBSGXiwhztWeAPT9gvV_KdPnJD61jpsQP9PqcnDJbfOohuDmfPuNtdenKxddUo6ojC-DF_9zHwvnnuOo6jKeyLTc2aurj9oQMv7-2ftcYwrmoCZbdeQOcTEBhn45N_XRQ694uB3SyTJdg0FWAuhDA4w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7151d02512.mp4?token=IZQQMO7EMNhEqu9urxGV7ZuzZlIHg0JSwrcZTsvDnAncsdcShoYcDXjzSSJfJLtqGjqP47lyk0Pv1QLac9EXfMCcOVXFcGElxUx1qqdIM23ilcrEt82x7Xb7znzAXLf2I_-lo9U1rgN2iB45sT9qTP1U5Tz0DymSZ36nus_k-Jgu32WThIWXrCL7Ntqe-JWYBSGXiwhztWeAPT9gvV_KdPnJD61jpsQP9PqcnDJbfOohuDmfPuNtdenKxddUo6ojC-DF_9zHwvnnuOo6jKeyLTc2aurj9oQMv7-2ftcYwrmoCZbdeQOcTEBhn45N_XRQ694uB3SyTJdg0FWAuhDA4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا بیرانوند: بعد از برخورد با لوکاکو، تمام زمان مسابقه را با درد خیلی زیادی بازی کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/95295" target="_blank">📅 23:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95293">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XNUKWe2QejRCuZZWb88rZqtWcKgEQJRbHqc51Owf-zzFDYKBQj6bQay_6Bkcy5Of66bZWq79IQ8Yk-SiMKr42caTf_XVS13KzqzPZwYOsZHk2XvO-oEKGucr_TETxNzTrsyf4uRlS-ei3bnvvq8mQoP-vI_hzacRLwpU7Z-AtF8IfC-m9JnJ9IkyAtuDK2qxhGlhquTI1LlAoGOMdLP3RtdwsPRRkZ2RSBiCvslXGo3dnKofBnl7s1WrG6rG-M-L2zLo2JQszNOlFA6TWlhJMi8jgqe9NT85vXmkhkuo4XCTFbqNtCny5rRxyue1Gx7orZqkAX0wjjipadKNvOVeGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_oc0NhZH5ftTOJ4oiYrO8HpBMAvRdoC6rlCQHW9u_wa1a-4DZ5lcQ4jRGEqLXpnmqGMkxTR8uBUe9JwgZxkbQSHQ61ckKi5uq9gaPfBuPBqSM-zUGtrw75IU98LXvtZ-Wcgw7ZpZun7a4OReW90SusfHiXBgPeR5inMoH8edcCjetKNBfyHDwjYkDI_KYS8VUj8XWnBXmzXnj15IdoHhObLD8FpUrW1vsSoj7LegDQk8mRoxsPnK7dS2l3ImfmCJftkPFj7PcYX30x5AUo5WlxsNjZgsdT0ULoOEfCIrE68DF9KQ0ycbU0A49TH-u6eXg3IJ6hSLB46UtmTlz7Yqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
🇮🇶
ترکیب فرانسه و عراق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/95293" target="_blank">📅 23:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95292">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezPQE-9LXZJESJxSDOSoB_aS8Ws3zkEGKBQqIzWpyxEiMcJDPyeThCn2lfFuzekiAUa4bvFqZ849cMGST1ZXAkKA3fiFwplwHCTZ5_VTNucqktbj6NoMch08tEqlbI4AqQKtTwyGcSNCDg5a53yffpzLjArh2xSsbC05ghdRPXfgT-RzHoetxXhcgL7-8BEym4GG-jzQ7jSDO2tK-2u3Q9Fm9PG1MWVtgvCL-QhA2doQLfT24UBttMEi3Bia0xBZpuwML3NgacmaWX1BOCweXxvTQumwjvBBd3LfAQRtryiLU80Q7nGcKDOnZIrs2CypkA7ZslLP5PqIMMIyphJjcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
خولیان آلوارز:
هیچ کلمه‌ای نمی‌تواند لیونل مسی را توصیف کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95292" target="_blank">📅 23:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95291">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d89d6be05b.mp4?token=SW1C1loVqrRr203be4vNUYwlxXNh1IPeTVy9dlhjOtjKr3sGCl6Ttj6hi8WffgHZL4MTa1I3Vf_2bCM5JBekzWaGRwqWkMsyOAY_qCCEOw1vure90xWonUGtrbmpO31ksabGcGJUt5ALZVEhj42M4cjNEaUrbGQI1WAieEvbM0zNsE5H3FJfB0JGFoIn8lJUOXtxqMpmTQBeR4XHTNS0KUR43yqGnvG4osFqvhtmRYLw9Cb2IA0QkaWC1Z1fawYrNQL8bxGsN9ZW8_A_E0USwjdhaDMfdeeTZtizhwRfsKJzhZjCwZfTo2nAnyRxudGyBWMR4Vlzh8HiTYnIDMLmUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d89d6be05b.mp4?token=SW1C1loVqrRr203be4vNUYwlxXNh1IPeTVy9dlhjOtjKr3sGCl6Ttj6hi8WffgHZL4MTa1I3Vf_2bCM5JBekzWaGRwqWkMsyOAY_qCCEOw1vure90xWonUGtrbmpO31ksabGcGJUt5ALZVEhj42M4cjNEaUrbGQI1WAieEvbM0zNsE5H3FJfB0JGFoIn8lJUOXtxqMpmTQBeR4XHTNS0KUR43yqGnvG4osFqvhtmRYLw9Cb2IA0QkaWC1Z1fawYrNQL8bxGsN9ZW8_A_E0USwjdhaDMfdeeTZtizhwRfsKJzhZjCwZfTo2nAnyRxudGyBWMR4Vlzh8HiTYnIDMLmUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضا جباری، بازیکن سابق پرسپولیس: اگر جسارت دیشب امیر قلعه‌نویی را کی‌روش داشت و تصمیم مشابه می‌گرفت، همه کارشناسان از او تعریف و تمجید می‌کردند/فاصله مربی‌های داخل با خارج هیچ است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95291" target="_blank">📅 23:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95290">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej2FwW40Y5ZOZxAE6rIKEM3F-lFOnEZHBOEUKJm7ewMy8gdhwkA1ilRTXpem9g_aOcuHP61hZJgIb8qm08kf9ZRpT3m9JgPqpwJbw5EUUrtO-SrfG4Ry56A3pPteEe4AK3WzP9qBFNUIsJh3HCiDV782lMo54wKAaIhKNJTarQqgbdkM6qk3EpBMv953u9bc-_WURzs6z9d6njxYJBpMYYliyQK3hcZfBkHJahl5lZluS2BPaBmGSVpM543OvUsjWRUT3K6P81I5zgzBjLjkgWz4MhujMwWmUZIrJVk4Gc6_zhHduyBTR1OW4B_SVD5Y2knjkjSQixyoAQLHH8AbCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناظر عکاس‌های کنار زمین بعد از گل دوم مسی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/95290" target="_blank">📅 23:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95289">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkomdIPrmIOrG1lTrO-blmk-0ZNdAlgm7ELToXkTgg2M4tYWNXqb_0cx_-ZH7ITYF6O-4vdvi_qQS9mejgVwTqIRkN5h4VXBRz-dEVp6xl3fpCU4SHtaYxXQwPW8lfGut6jtGwh20rSC7Sre_oU8LX0z7CkhIfxbhKh3xnP2OEEzSGOfuACDk68zCBj2sFqCuFwhRaO7zIWQBaQpK2tSYWzI-lyJKN8uutyjdUDGLBE-xKxE8EVM785SfvZne0QD58Bsc-5IjhfQh3RfoJmLeAhpxYafuq9taB5mH4FuA8tf5Y7989E9IssORVuamaISj4tyeNvETaIv3aOUpz9eog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
افسانه لیونل مسی در دوران فوتبالی‌اش:
‏
💥
۱۳۳۰ تاثیر گذاری مستقیم گلزنی.
‏
💥
۱۱۵۸ بازی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/95289" target="_blank">📅 22:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95288">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn0fDr8DQ0h3j9RuF5dpw7RHvqduHZrM8k63H7IPDVK5xKcbHPr_t5gBSgJyrCyt2-6aYeVkmEj3ukiAdtXyYYF-D7nAdEv96GSFK4npXSTTSFTX1zOgjVMu35l4xZJs4QDHrb7FSSb2rZbvIgdX3feeG-4yqV4SAvQzcdGyprkfdKn7bpt1ADrwyXIfVx0GIEeR5-DmskS6R78GuT0gHyfimx5oY8p0IJm25Grng0D3RB7R2T-50F_2la25Tv7IZ2Vu5Ub-ribmBrVOfOnhwvIDhyHHMhiH_h4E95c5_sRXwnx4_RdqZtbkuS2vzWzS2zdVmj9UUBLZCC4htazD4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
پادشاه فوتبال و لایق عنوان بهترینِ تاریخ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/95288" target="_blank">📅 22:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95287">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZJ5uwsXqIHkgBpin7csJguktVG_1uCBt3xHeVyzSog71b8yCE7v3bNVIJIKjOxRc43GD7gc0NxfDOW1-AD1nQc1Mop07hkwuZSlqFh6uJaWWjEfNibJIMs4ct4OU_viiWZa74n22wGe6PKEB5dUJUGypztXlbd_AaC5et-neQCuKT_i8xEnX0M4ajf3g5TkLGp8YWfFKfNVq18sPDpf7oeAuMhrkNSp99QAE4LpgFiq7z9wPUWMvPxw3wu3vw1WrTCFucrTrFk0PSHlIlBqDuVdfMuFNEtXvem91kRFvDXS4UHFi3PZ9htuHnNULY8BcRxz9Cl67HJOnV4INSC_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🤯
🤯
افسانه تاریخ فوتبال دنیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/95287" target="_blank">📅 22:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95286">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/R_XL6gn_ePWWhFIiHriN-gKHWxOoj7V7XhHmB_Wra5UntGFSh4tiQVPlb9xQzym7LZLRX4_F8UDJoXGtsgr72frcvfSJxPmG_rObYN2m0td2E8UVRn5nSS37xf5x5A-9EIfQQgypNdI2iyBNX0gGXAclVYSWJhBCquWCyYS3-DKe1eXHCUHB0C0P9i8DMS2rNEFoN_pPtZCMsoI40JXLyayqD_WB2X9epdtSo25Yku0hQW4lFfAsMN62W0H1BvNjpFD63RD6SSOPYtXzN7X67QaiWy3VW1B1JMKWZTJyPx2XK7b3KXN1OJz8tp4C_DG3EB-WpDviLXWXiu4gpgVckQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو آمدی و توپ، زبانِ عشق شد
هر گام تو، آغازِ هزاران شگفت شد
از سبزه‌های زمین تا اوجِ آسمان،
نامت برای فوتبال، زیباترین نشان
با پای چپت نوشتی افسانه‌های ناب،
لبخند تو، پایانِ هر اندوه و هر عذاب
تو فقط یک بازیکنِ بزرگ نیستی،
رویای کودکیِ میلیون‌ها انسانی.
مسی؛
هر جا که توپ به پایت می‌رسد،
فوتبال، شعر می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/95286" target="_blank">📅 22:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95285">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biGezRO_uN7gQ1koX9Rbsu-U82f5sE5o-2cQQEVtNV0_24MhsRKHErGUUuxITbPCNXuC1X4u_2urzbuSxZh8I1SbgyHrqlwjGduSLQqNiuC_kVC6E2O5UKGperRSe_WQI6TZgSGoWgbW0Z1_ZXQQwM4Kk0-0tXWSUp3gcS52A0w7A9838FijSPzpXUIngJJ2zBdVnmel7UT86dChLn6RLEkSdveLJ9c2OEsogMGJOh3U6apmbmbMpfr30ovvzWyR3USLNTrgDdrAXg_lVTnIKUHdyjJSiwfEgS1D_tIqyIaBghP29Geaq-bQ6ZN8PVMacjY6wx4IkRAQ3sRcL-damw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیمهای صعود کننده به دور حذفی جام‌جهانی آپدیت شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/95285" target="_blank">📅 22:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95284">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5523d5321.mp4?token=gy2wyZUWFHJOmysY3il32LwE-qanlYYhrpm8CeDiXrOqjlgUeXG3IctTrxGR4u4DtwodF9EfE3WlFYSbgFvOZnJdJJ2gALgg3CUn8lb_f-YpE84Hb2t5S3LyTTCKcJ5_KVb-eLmWQ5KDR2L-w_eQbYt-6agILpRBG4YqDjmv7e45hN8MtsdMlxamYgd5Dk2XAIyShGtbdCGJvbRTs-Sgil8rKdj00WK2MU4IZflyjCE9vgckVnUhSDnNa02b7Afwk3dXO6NF-j4hlM42CTDGylhbuVzQ1rGDd9ePtASIjY8BaVcHf7AyafXdNd-XDySf58YAFeIfbtCkoYSl82pdVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5523d5321.mp4?token=gy2wyZUWFHJOmysY3il32LwE-qanlYYhrpm8CeDiXrOqjlgUeXG3IctTrxGR4u4DtwodF9EfE3WlFYSbgFvOZnJdJJ2gALgg3CUn8lb_f-YpE84Hb2t5S3LyTTCKcJ5_KVb-eLmWQ5KDR2L-w_eQbYt-6agILpRBG4YqDjmv7e45hN8MtsdMlxamYgd5Dk2XAIyShGtbdCGJvbRTs-Sgil8rKdj00WK2MU4IZflyjCE9vgckVnUhSDnNa02b7Afwk3dXO6NF-j4hlM42CTDGylhbuVzQ1rGDd9ePtASIjY8BaVcHf7AyafXdNd-XDySf58YAFeIfbtCkoYSl82pdVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپید وقتی کیررررر میشه عالیه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/95284" target="_blank">📅 22:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95283">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🏆
پایان‌بازی| دو گل از یک افسانه؛ مسی آرژانتین را به برد رساند.
🇦🇷
آرژانتین
😀
-
😏
اتریش
🇦🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/95283" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95282">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0lWQzSi57yKNYrxEk7Rgln_2FVsmIKoKBqAMpNAJn_aA-5wHWxkOLalD2xq6tuwxi_lFpa9-Q-l5h1iCtfhwynocd5DH6bEoCavMZR6vV6yxgpUF7nGQ4jQpz8j3KvnZY5CLq2ROhPvdSimzqtcqj4fAULibJ03CLOouW0rQZmeonTUrrEwbyFRmKOiU3rlVKAj7UBI8cmXkJV-ZM-E8pXho8YuOZX8-DjTw8N3Yf9XJESPWEpsyC9CGvl6Z-5FLz_OEGpGRKsOTmpnhyEX-Ma6q6wGHbExAB5O-2n13fHLtybxrwgVcr297TtW9-J-vZ7Ubgt87R1cGZJUeIy9Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی| دو گل از یک افسانه؛ مسی آرژانتین را به برد رساند.
🇦🇷
آرژانتین
😀
-
😏
اتریش
🇦🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/95282" target="_blank">📅 22:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95281">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گل دوم مسی افسانه ای به اتریش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/95281" target="_blank">📅 22:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95280">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">5 گل تو 2 تا بازی
کیه این بشر
😬
😬</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/95280" target="_blank">📅 22:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95279">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مثلا ۳۹ سالشه اقاااااااا</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/95279" target="_blank">📅 22:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95278">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مسییییی
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/95278" target="_blank">📅 22:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95277">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عشق کنید با این پسر عشققققققققققق</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/95277" target="_blank">📅 22:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95276">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دومییییی</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/95276" target="_blank">📅 22:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95275">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گللللللللللللل دوممممم آرژانتین</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/95275" target="_blank">📅 22:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95274">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گللللللللللللل</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/95274" target="_blank">📅 22:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95272">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JnRkmAIIsQa9E8PTKNtiVLIW7lUBseWpEdXg9aN3JpdlI-_zoNF1NgkZRxJQEpvPBYAs2TCXyqjVUHqJaebiqzV9hZ8gShnPJcrMVrCZM-rETtopBEqnLzI0pqi_oqoEBzeKcUNu34FIh6D37By5LXsxjc7FqnHCsMeMzYZnI821qXAnQJDasS7HtZYA9R0KL1xwMr7f4tsFPZLT6YO8HWHgR9fTphO3gh4SbYdQzlP4h5z12XebXQmn8dwQcRSAUCwV1g3dgQmc9lb5HSrUaaCzFCNVyPVmH0fQGsuNNSFwOkTTdKZyCNpIzdFPA-X4qy2cItP78s8T3_6HZvJ8Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFFSFIgtimlebRcEwlYfk_RcLG0qpRQS3gSQuoKFbGN5zGje5uo6nHyLL3D7zMgl9VqnIuBds0oPlwDBfUvpGViVPNhomWn4niAN2Y4Oz-7Bm2hyzNawyHptIgBxUc_KrP8hrpoiW4CzK5F-banV1_gXZ3UxwzO0paZuXo4L56Zb0yQhnWOKMFnPo-uhjS0gtaQ5xA7Oj2P_gSDxFHXYoEPPBPA_kM5PS-1jv_6kAFjEaxzdV4FToD4tq3PxuiuHUV7PIPs2sxcBqQx8NBwfVO5IRSFmtSN6S2sqE3Kb26Mdr5v8lG2k79FMgWxa3gsiT6y0lnWg05QjQbJJJl5gng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
وضعیت آب و هوایی ورزشگاه لینکلن فایننشال محل برگزاری دیدار فرانسه و عراق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/95272" target="_blank">📅 22:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95271">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d8de871f7.mp4?token=Anky9wlibaPHXdxLfr5UGptjJn4s6hG2zlH22nqX3R1yNu-T5rrACTjvUV5046sho2-YGGkA3_8uy1fqh5YMeS2wTyCmSulYCqu_AemJ1OXXYMOcopaqb7KuovmIoKuJeqni7-PeUSX6f4cVcRiAZTEsDneQzB6Q5sMl50Im0B1mHFmqU7zAQglMSIRDGiX_FFWDNsI7J4_n4YfYOe2TlFdHTCRsprBCL3kUyByQTCdSb8OvfeQOyTPwDN-qrktp5Lc7aeFpKbJ3cXGkiBSdJa7MVifCVtV6jOoJ7wW5nT5bK1IKzuin-pMMkudbZ--xGQLftzyQiekVzTbocBgd7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d8de871f7.mp4?token=Anky9wlibaPHXdxLfr5UGptjJn4s6hG2zlH22nqX3R1yNu-T5rrACTjvUV5046sho2-YGGkA3_8uy1fqh5YMeS2wTyCmSulYCqu_AemJ1OXXYMOcopaqb7KuovmIoKuJeqni7-PeUSX6f4cVcRiAZTEsDneQzB6Q5sMl50Im0B1mHFmqU7zAQglMSIRDGiX_FFWDNsI7J4_n4YfYOe2TlFdHTCRsprBCL3kUyByQTCdSb8OvfeQOyTPwDN-qrktp5Lc7aeFpKbJ3cXGkiBSdJa7MVifCVtV6jOoJ7wW5nT5bK1IKzuin-pMMkudbZ--xGQLftzyQiekVzTbocBgd7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
قطعا حق آرژانتینه که امشب بازیشو ببره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/95271" target="_blank">📅 22:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95269">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCEtUz0QUOkNURKQMKSKa3N5pIkqDuMHhN7iJWuZddl6Bg7SEfYlKAYOa8S6KL2VH2S2NajnxU82qtfkWAOoIKcOh6zoG0DzDJD1RC4FJYqCHWebA5yiW2sxySJJbtnGvNmdruFgmpjjh1mvMhQYwIpYw2-VENW4O28E7akZEJLVqJjTyUiL_s3HVN4JltOMY_YXm54Oj43-5ltg24_VyJG_zt42Z6ZgqCb2iPq-pEPPbUM9g9ofefBRvquRHCr92fn40Qlors4vwGcr5EI1eOPmDDEbCeomUhkkDZ0bN5Ohj40AeaWjsr9TYEpkij01TOSxAqK9KR7OT_A7-MugWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b705a1649.mp4?token=a6Nv9mJm7LswlXmKNbtCWnIkXHYW4X39FO7LzpRhPzSrCpMcA-Md3IE-9N-HwK9h4hEbOi7eziUH-nMgMYyRBDixA3irs0_TNyD64vSL6cI20dzSldHzywfdTyXKWlsspC0NIRYWdYRXcPZZFgOCt5NVSB1q91jTVlr-LSHTcYLtNp3jbM3XpcZhUTjzJSysiWAEzxE-rtkdbU9i4LJ0v0Ev-c5KFU9nw5QgTUSJDQ4m6Al0lSWGAD86Oq_RJ6_JK0uHG8Oq6ngd_7sW5EriSwdasTkfDTSnTkMHtwtcRjy2fzA3Ltpsni0pjd2QqSgNvTHs-OM6r6HxX-DCtmLlQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b705a1649.mp4?token=a6Nv9mJm7LswlXmKNbtCWnIkXHYW4X39FO7LzpRhPzSrCpMcA-Md3IE-9N-HwK9h4hEbOi7eziUH-nMgMYyRBDixA3irs0_TNyD64vSL6cI20dzSldHzywfdTyXKWlsspC0NIRYWdYRXcPZZFgOCt5NVSB1q91jTVlr-LSHTcYLtNp3jbM3XpcZhUTjzJSysiWAEzxE-rtkdbU9i4LJ0v0Ev-c5KFU9nw5QgTUSJDQ4m6Al0lSWGAD86Oq_RJ6_JK0uHG8Oq6ngd_7sW5EriSwdasTkfDTSnTkMHtwtcRjy2fzA3Ltpsni0pjd2QqSgNvTHs-OM6r6HxX-DCtmLlQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانسورچی صداوسیما باز هم خوابش برد و این صحنه خلق شد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/95269" target="_blank">📅 22:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95268">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sN-XcF9WuRFl9-tTwVHshz9-oTGYg5acWqaVcoUbxlUOPYgXQUMWJlfyx_gO2afyojm8aWWOtkM8Fd7moDgvx1CfOfh2MYhDXZFNurAkiPmUgAJNugAjZ55u0m7vt1igSauRe0yp0SPaT258nVEt0FHgljPtfnehN_F0dCOkbtt3sl0-r5lrG3DMhor4ze2sLqCE2s0KQB97H-CPz7jL0K7_uD9ihe2oMalq_wb2X-2Rk7buL55ZLg3mYeGNSTMEmwhw1-gyT-cGK0yZoSvP7D5GvNb1hWG1mfgV9-cQFB0JLx35w-glX_59T1_uMu4Ealdig_ije23XeZ16C8qLwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکیرای دلها تو ورزشگاهه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/95268" target="_blank">📅 21:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95267">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1uxUX0Hbi8ijAtA2_tu1qf6wglPkzN05-C_cravnh1mzmHto_VQgMoNxpZGzcMJck8VxPRN2eYb0sXTYDZi7RmUpCAVkGxvRBG55oMOjaBYuQEdvAiJ9kT4aYsi1ekXWLGV_-phi6ryyC_NpkJR0G6JgNvrQKvtW3kfQfZ_2-jWdmswEd1ZzPpnjdUra5VtQ-msU4Fh0DlSax3GsA0CI7blceYs0mkDnd8O71MuKVNRAVXylWfYopHv8EH5n02L9vEUSSyhVpm0H5AVyQOsI68lKcr1ituSXkomyzNkoOnKgtdxOhxJ-GpneqRKJFh8-yzE3UaflmaiFaReZZaN7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکیرای دلها تو ورزشگاهه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/95267" target="_blank">📅 21:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95266">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ffe750ec2.mp4?token=m21Y4d89QhAlO7MFMby245xIOswWvV1dMP_D5TfN704JR9tLSxRqsni1yDjbmya_dGKfSHWLw_FDeF3ztLHmF1IKAClof64L2KM674IVXZbMMNs9icEKDWX6WvNeeTHCPzw9AROUpK9C7s7Wo9U8VtOjim5S6NnIc1MlLIjJ_HKuf8MFeGYgrASR9uC-UvkE2AKgOX3okWGUofYjDqjb19ZW3uzl75Z_7oYwcDzeMBsw_mSZwF9m-ZrGTRG8uVwPvXWksGta4auSsQa4N0M-BlTz90Rj9k4wYx2SWC6K9OOgNIq_yFzr5rSMdthNv5VvlEfb2Wy7eR1btPhCeA736Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ffe750ec2.mp4?token=m21Y4d89QhAlO7MFMby245xIOswWvV1dMP_D5TfN704JR9tLSxRqsni1yDjbmya_dGKfSHWLw_FDeF3ztLHmF1IKAClof64L2KM674IVXZbMMNs9icEKDWX6WvNeeTHCPzw9AROUpK9C7s7Wo9U8VtOjim5S6NnIc1MlLIjJ_HKuf8MFeGYgrASR9uC-UvkE2AKgOX3okWGUofYjDqjb19ZW3uzl75Z_7oYwcDzeMBsw_mSZwF9m-ZrGTRG8uVwPvXWksGta4auSsQa4N0M-BlTz90Rj9k4wYx2SWC6K9OOgNIq_yFzr5rSMdthNv5VvlEfb2Wy7eR1btPhCeA736Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش اسپید دلقک به پنالتی خراب‌کردن مسی
😂
😂
بمیرم برا دلت مرد که آخرشم کیر شدی
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/95266" target="_blank">📅 21:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95265">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بریم سراغ نیمه دوم</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/95265" target="_blank">📅 21:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95264">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfzGL-wtvRHUfzZwb7pdeQcM-XZ-pyfjZllx-4jDB20yrQSverRvhKV3FwoGgsQFGaBGOR_Qo_oo3UYhmgDph5Lwb-QSLlTdOGaO4MqElnW00iLl03Rq4JCvma6h0ZN0OGu6KLkUus0uE09unM2CkVz4SHn35ekqeNItd2couyrOAHybPW5PqtyzyLuym5v5jBw626H-sQFOh-OUKwZ8vYTFRG9tC5xq2KgJDUzt8_ciiL1zx-MEuGDwqcZeeWz0QikaEtYXpc7i7TCanD1ImISbhFdvcuFtmNeYh0yIX7TRzvWRbnV-6QEsi0GK9rV4rApC3Yg0MMh_EzSB-i_uRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوادار 100 ساله لیونل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/95264" target="_blank">📅 21:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95263">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/820d8a5eb6.mp4?token=FCX_5UFRbwa9GQpIVdiQUTeLyz4n2WDK2BdCCL2CknC4GangPU14lzn4tyd17Vf528XhxV8644gClrGOH-CIrrSZBPDgD5_f2dcw2lb_iirS-cVLtIDsPBdJC3AQocsgTT6DS6L7wYIqIldSRCC4NsZBTOpj9QkB6dPjaOpIMVvuZVxZF1YoxwsGlb9YyZ72O7lhRKhWZIOKBYHzGLjezuAVTL57d_Hu5zFsVnhOIBJdOaVrmf9RJTEoVYi3YMVra92C7z8NYQ5z-F2TQZinvRm6Azd5jSIMK5iXv0KCF6WrTlMPgLWrgtBh3hMxNj3RLlqInw8ToxIgUWmS0VWYxKo9BTR_jHmQbBPl4UB2v2gJeBy70vnLDplOBy8wIEcsNTsRNd8BtFqhrkVFev9CLU0HISdJyfJzvLwp2mNEXvedHi1hJTeEN-yUGYFaMw0wBFLC5XpC-AFl46f8Bp4bpoN-_eexiYLXEDWfvohBOEgjL2josMO-1ok62dCmXpx03oi39B-A7feWfe4tOzXFnp14qldtBPpVoreywZjSQ528QFV-N8qHGjXUt34uPRYyJoWvhWAJeKwN0MG8rdZkOd23I1RTkQUC3QLlBiqrlgrgNI-6hyDfgGK4Blv9drCDCex2bZYDo_3PwYAdn6Vl8GHq6RJZ8ANfdGVvjiAyuBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/820d8a5eb6.mp4?token=FCX_5UFRbwa9GQpIVdiQUTeLyz4n2WDK2BdCCL2CknC4GangPU14lzn4tyd17Vf528XhxV8644gClrGOH-CIrrSZBPDgD5_f2dcw2lb_iirS-cVLtIDsPBdJC3AQocsgTT6DS6L7wYIqIldSRCC4NsZBTOpj9QkB6dPjaOpIMVvuZVxZF1YoxwsGlb9YyZ72O7lhRKhWZIOKBYHzGLjezuAVTL57d_Hu5zFsVnhOIBJdOaVrmf9RJTEoVYi3YMVra92C7z8NYQ5z-F2TQZinvRm6Azd5jSIMK5iXv0KCF6WrTlMPgLWrgtBh3hMxNj3RLlqInw8ToxIgUWmS0VWYxKo9BTR_jHmQbBPl4UB2v2gJeBy70vnLDplOBy8wIEcsNTsRNd8BtFqhrkVFev9CLU0HISdJyfJzvLwp2mNEXvedHi1hJTeEN-yUGYFaMw0wBFLC5XpC-AFl46f8Bp4bpoN-_eexiYLXEDWfvohBOEgjL2josMO-1ok62dCmXpx03oi39B-A7feWfe4tOzXFnp14qldtBPpVoreywZjSQ528QFV-N8qHGjXUt34uPRYyJoWvhWAJeKwN0MG8rdZkOd23I1RTkQUC3QLlBiqrlgrgNI-6hyDfgGK4Blv9drCDCex2bZYDo_3PwYAdn6Vl8GHq6RJZ8ANfdGVvjiAyuBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تشویق ایستاده ملی‌پوشان ایران پس از دیدار با بلژیک در استودیوی جام ۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/95263" target="_blank">📅 21:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95262">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2keQEEqizgZ1FW5iVvNBwRC3-Ur-UObvs4TR9cpwUgsRrScdbpY17DzXIuUOKfwVi9OFhqUK9MMDmf9QhqxRGxLRfpyrz2YCsU64za7jtIk3weSnK5_qIfYq-U_u3i6D_fBs1PyIfgX_rPgdEkTnuURheRJ3clTBgOcBGJ2nC5YI6xi88-HJD4xqNavvp-F2KrsKe8li6voic_FtMP6drRySC7mDOe6EjskjGrD_qsdpLGO3fEIKX6oeo9SPKeL2dWLDZcp9YrIxXdLE65OVSZ4vewW22aVKeXsgVqkG5vzrp_cNMe89KAgiEfRyOSPs3YOtZp7qU_-gLqktOakEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملکرد پشم‌ریزون لیونل مسی در 9 بازی آخرش در جام جهانی
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/95262" target="_blank">📅 21:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95261">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHNETGaz-zn_48Y-qX3A0nw4bk9C8f-qZFBNJcmdXZGMttWlB6SCBeIXt956rCWY0KetRRqmWHgvPyjxDR-x9_ZI4LdbyO7Vu7ts-jgemIzuImtPmSKgCjuO7lRMQaZ1Rxsb1GE4tn_GFjT_VcsTmOVD_aI8T2k6f3ocQXP56SqlZkHMZpZBZ_g3Cy_NBPbXGanlFrZC3rXd1GPLeL7nHglpVoJaX2S8wN67CGH2A7bPxmMBfXhHpoqjVT-Cgj5HRQ-7eIcXFiBI9HpAMjRtwMA3a2F52XYO2VoNlNOZZsMLdEdbkjktRTRGBoidPZ9JizKfUW8lRyJBmIA8k029UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
بهترین گلزن تاریخ جام‌جهانی رو مشاهده میکنید:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/95261" target="_blank">📅 21:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95260">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🇦🇹
🇦🇷
پایان نیمه اول با برتری تک گله آرژانتین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/95260" target="_blank">📅 21:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95259">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rrocaon0cfSFPDYcP3lctbLeyfke-TIvreOqFruC8w1sz7pR2GksWGh1x0YQaNa8EgOliYNVwQAzToPag9KsDXqaZeiEV3oiPUfGyZyofNzpHBzRoi7bhzR89BbR8-onW97xQMu6MH9hSlk1NAav6w2WKkjC4VZkbtWhxej9muKWdhnb7HvAG2Mphf32IydMGaRT_ri1MnedX85TF3lHw7Z7XdMIP57txqW9aZULIy_wbMTRAxbjF0-iAEeD_zhqyij7qwOEqvnmiIdp_QYcPdcx1a5k7xROwAAwvL-lQQ1vHm0uSI0dRZDGcUPdcqWMvGNX76-t-neTdMNngwXrpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
بهترین گلزن تاریخ جام‌جهانی رو مشاهده میکنید:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/95259" target="_blank">📅 21:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95258">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇦🇷
گل اول آرژانتین به اتریش توسط مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/95258" target="_blank">📅 21:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95257">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رونالدو فنا یه ذره خوشحال بودن سر پنالتی ای که مسی خراب کرد که باز ضایع شدن</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/95257" target="_blank">📅 21:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95256">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رکورد کلووووزه هم زده شد
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/95256" target="_blank">📅 21:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95255">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شبش هم نباشه گلو میزنه
🔥
🔥</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/95255" target="_blank">📅 21:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95253">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گلللللل آرژانتین مسییییی</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/95253" target="_blank">📅 21:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95252">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsNE94wRXbfjcXsO-qZozkpV-AsJVSfFp63fui9tAR3JRzjPLhF6XalVUZrhm6MSzDUJnIuZBeMvSScrsEUWA-P3bnk3Nx44gfJ2uXlmAQLLkbdye5Iktl-O8yO-zzUjRXRctVOt2hTAWsHQyIUwQVD0MzjXejr7O_k0Atd4uvoYzDCNS6IVRHlXpn3k-F4CTva5cfBJyeu4OYVYcOjZcw4kgS4mcoV_2N1f0twNPlrhW_i1l3AL5N8P7lqHAMGAMUG8dPmgq9f7BGGqAkx7Tvo-9hLZdPRgtHIXf_zYcGIb5o6Mrr3Dyy6RrK9OpHObUV3eAdzogapU1XDbcbW9BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیونل مسی با ۳ پنالتی خراب شده رکورددار خراب کردن پنالتی تو جام جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/95252" target="_blank">📅 21:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95251">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
لیونل مسی اولین بازیکنی است که در جام جهانی 2026 یک ضربه پنالتی را از دست داده است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/95251" target="_blank">📅 20:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95250">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اتریش داره فشار میاره</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/95250" target="_blank">📅 20:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95249">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مسی داداش چیکار داری میکنی امشب</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/95249" target="_blank">📅 20:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95248">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5cd500ea6.mp4?token=UxCdzJrt6mjuRf_qhgvTtrIKQza4ANuHN1oHW7fOMETOarlFM8N-_Ku168rC9yKi29yYpjas9rtfAGkYaDnrL_hLCiOkHFOM0BM-Vd8_u3zTSupp6DNFrjN7zLMK839p7gJEG4ncjaLIxYv0wsYAMtbxSiOwlqlzpiQkvWsjEU2o8sJj37Js_GUTdiXXjgWCnhmXiXmpikFh7v21dfweS8vpdp8DmGcbq6OrV2cRjHpqVui4-F4B5sJcnnbOvftbHb83sxpo5sSoYMU--PtYlegqupWmt1Bbh5Ee_rmsY1wQiFPtvFeMBrYWEhPIkK7C5yyevlP1na9IK_Zn07YBgXu9UfJyMTuvEqs4p2Tn7KwQ93NqnZ_AV4617kB3YSA6MWSLuatRqxeGDbjLdqm5jyt_8JhwMDxrG-5MyQ-UhW7SWmv5beBkuq43jkfJ-epzEjOcdXWLsj0heDnOslMWlv5g2AJblWjQ-zyVRfHivwtT0OeFCiWoRt1x31Gb7TVerPOKlbNz03eVNdqHrz5lXhJv57j49ZMaQCNYveHVzXRsCUgwTDiDsrxpmxSHkxEg9cHXPwOIC4mrNmM0tTQz1mdtnyQUv_NWB43gEWgsqhopTrd16uBIeOLqnyQ5u358rU3ibPSFxCsvhCYlx7k_MjG9K1j5FE_SXQSTHVMF34o" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5cd500ea6.mp4?token=UxCdzJrt6mjuRf_qhgvTtrIKQza4ANuHN1oHW7fOMETOarlFM8N-_Ku168rC9yKi29yYpjas9rtfAGkYaDnrL_hLCiOkHFOM0BM-Vd8_u3zTSupp6DNFrjN7zLMK839p7gJEG4ncjaLIxYv0wsYAMtbxSiOwlqlzpiQkvWsjEU2o8sJj37Js_GUTdiXXjgWCnhmXiXmpikFh7v21dfweS8vpdp8DmGcbq6OrV2cRjHpqVui4-F4B5sJcnnbOvftbHb83sxpo5sSoYMU--PtYlegqupWmt1Bbh5Ee_rmsY1wQiFPtvFeMBrYWEhPIkK7C5yyevlP1na9IK_Zn07YBgXu9UfJyMTuvEqs4p2Tn7KwQ93NqnZ_AV4617kB3YSA6MWSLuatRqxeGDbjLdqm5jyt_8JhwMDxrG-5MyQ-UhW7SWmv5beBkuq43jkfJ-epzEjOcdXWLsj0heDnOslMWlv5g2AJblWjQ-zyVRfHivwtT0OeFCiWoRt1x31Gb7TVerPOKlbNz03eVNdqHrz5lXhJv57j49ZMaQCNYveHVzXRsCUgwTDiDsrxpmxSHkxEg9cHXPwOIC4mrNmM0tTQz1mdtnyQUv_NWB43gEWgsqhopTrd16uBIeOLqnyQ5u358rU3ibPSFxCsvhCYlx7k_MjG9K1j5FE_SXQSTHVMF34o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
صحنه ریدمان لیونل‌مسی مقابل اتریش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/95248" target="_blank">📅 20:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95247">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">این چی بود مرد حسابی</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/95247" target="_blank">📅 20:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95246">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مسییییی ریددددددددددد</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95246" target="_blank">📅 20:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95244">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خراب کرددددددد</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/95244" target="_blank">📅 20:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95241">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پنالتی برای آرژانتین اعلام شد</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/95241" target="_blank">📅 20:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95240">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">داور رفت وار</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/95240" target="_blank">📅 20:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95239">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">صحنه مشکوک به پنالتی روی مارتینز</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/95239" target="_blank">📅 20:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95237">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">برریمممم سراغ بازی آرژانتین و اتریش</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/95237" target="_blank">📅 20:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95234">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mAO02uh96ANk6nqyYyDbzOO1jGspHKSHRcUHzFxzPytCfgTaO3t-7WE7KEDHM33xg7pdERvOcdm3WkEayuKCNmOchWK80Rz4wPcuWf587I8oV9tCbHvPCNBEccvPY3ik6r9yDq82K9wHAm4ViYQsXlefoYsCYMzRmEQqQwUcyh8td305tRRFt-oVfVAomUNjsPQ05uwoI6XCcrIcyuy0nKr6tDdSM54xXiecsZO0D93t_aNxJWiQVfrNIR6TfPkyfwXXHv0w30YxlI_FBsN9cBWWI7I0tAYX0g6rG2w0arAvXdvkWmqT1EqpcHzZSD8u1sDz7YY8N2LjvaOXqCU5hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U6paFvOdk72n6nf5iwNir0HFyrZoNiXNwpj5RdaVwHFAcRKCNnO82qtt6ENIICCE9p3qPK5ccYvOLCaTAg-wbJAv25E0W4Panh2Ef0VVdrY88flm39Th_jr982V8VAxHqfje8gyWKfmyvc75qIsSI-eAv8pgLkNMBMQrH5xRsYbX4GfFmS10v81aczpuE-GnPIp9jZUXdCcl3be-3V1CaKinDGuqnazIblyobM92FKuSV7fSB1LouZqPOEDexnBOTYVWKViO1KR3t2_TNkrTZO_BjxoRnTAF4q0vTbSkyCFkq5iTeqcweH5DpjaG8ncNQBtZrXRJlFxPOrbPxBBzSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JghO7Nojj3wAUpSkd-4w0vG99yCbonySDuO_2I5fa8dS7sqfw44W92WDJxnqu0bqAFn3b6FAQDn-bA0-MHYxIPR2qSZD4ULg7cOnes4d_tlh25sTwstpTanfYCuF5K0UuRfKpblYWlNnYsJrSjkI5REYuUTFU9hVxSjIHUF_Lar3JD2M_mylnGk9m5CopwoPpFJ1CZ8cDNRYdkL5MsNlKGvkY_10om6KK9oMO5WLD0asidf5Cew2Y_IfgYtHjG2rZaohNgH3r-2uXkuOkb5qrm4J4krrQ_JGhLXVqWZWkjBGjDkkdep8pbl_urdNyJAB06gBssXwIDLjdiq-FZcxrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇦🇷
🇦🇹
استادیوم خوشگل شهر دالاس محل برگزاری دیدار آرژانتین و اتریش
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/95234" target="_blank">📅 20:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95233">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5k9AByUT9DtT88kPfflFODWzpsvhAWbzzpcP910Rqsetgw47kZhMlfrDJLzmJfYTG0laejZoNuc8UnikNasM8HzQ7Hd9pxLWsb8bzVPDTiYioIAFH1Ph_wahtVgQfck40NbMsbg_mm3gAsQ0zRya44udQP6OI6AS28CtmgnFCzA0kyZEpDKTvwmlk-scynP648FQTa8THJYpRveXbRRfzO6BB4wpTQ1xQqx8q-u5tXvG5UlOy4P70RkFErmD3vcJS48zMsyxWkkEMEshQYapJlwY8JkZanmt69LgXmRkMto4JZ5FirPbf8Ua4KOzamIYSM8A1c4vXzniPuBppSYMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دقیقا تفاوت رفتار بازیکنای آرژانتین و پرتغاله.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/95233" target="_blank">📅 20:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95232">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/95232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/95232" target="_blank">📅 20:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95231">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1o9YC08PsavFJEpljRleMdidkPj-P-D4HUSDXTu83oMVoSnXHKS21ZmGGAv_zGHSmBq8Kg5bIIff12yQBRsXikQA_WTmv9JHtosMHEsY_i07P7T9Y5yvOgkrS8D4myCfwor_s1dZoSaEJfIODSls_Zp8Gd5-GLqAnm9ASshHvrjCFeAmZyCBAsLd7tSNTd406LHdVuKyZUeK-SUvQMYdNbAjMugpPxTp_G5TkBzxDJZ6jS6LouYnoVVXVOIInnHIGxaMmWVKhnN9Z8bvppuRUTuKGhfx-pKh7kMLC8UwzTTcsRegMznBSHiTaUVahsJFUwq8ep2BYC578T_NlmttQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
پرومو بزرگ والیبال Ace Arena با جوایز تا 5000€
🔥
🎁
جوایز اصلی هر مرحله:
📱
آیفون 17 پرومکس
🎮
PS5 و Xbox Series S
💻
مک‌بوک پرو M5
⌚️
اپل واچ سری 11
🎧
ایرپاد پرو و هدفون سونی
🎟
کد تخفیف تا 50€
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/95231" target="_blank">📅 20:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95230">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuBA6NU5eTsdyzbDcBVD4qatfnW525Q3CbrVpBA39-z2hLU29MTk0NW4HPpSloqXGrINp-p7Z7s7bHLB9nlMWhwCMB0_ps64KOZLuZc9vfdvSxXyGjrfBsQWzXdh04v1ugf37gLli3fS51jHQ8u82KhkhYPZOYLpMsWQQnFIncVjhaxdkRJXPLNpP5jOTJW_oTAqF59hyhZk8vqukq1wUtTwbKm4E8Hx7w0yrmm_Nc3B0yEeM1BRDHPicv29oz39wIisHfVcXgMEwgG0qLEG14CRwpBbdEdtrL0YPj8f5DOAi7yOcheVLq8O4XXgone9OfEaD-384tfcHeZeIX6tfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات گنگ از بازیکنای آرژانتین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/95230" target="_blank">📅 19:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95229">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxTUCrCOe4kCLOuj8NVIfZJ8SwyDnvEv7whSwkPzqbC4Erm9Tx7q-A7v7rqxmcrLVRFaVClvqBJKpPYzxu-MUFB9Y30-r2-Ua8qSmFQIcBul4izg-D0GMwi67ncX2rFAn_IHlOw4xw8KXbjCTVWRera4o_LtejUOY2lkbwztPvD_dHT_pdmebf7CTH1RYbdxGzDqNtYOTnxymnvLs_enZxMPKrvAyYrJ_BQZ0ApcgmlqyrtK1-5QyEkuwlGQq4KhUvh0hfbz5vhGoCsruC2lUCOYK7DGd0uw-jGnj3QMXeDGTkqzi-lCNhvagZDM4I7CQie2CVH8EFQ-YrPf8TvX_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زلاتان ابراهیموویچ:
قهرمانی دوباره لیونل مسی در جام جهانی چیزی به جایگاهش اضافه نمیکنه، چون اون همین حالا هم بهترینه. فقط یک جام دیگه به ویترین افتخاراتش اضافه میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/95229" target="_blank">📅 19:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95228">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZR_j87sp2K7UApjTXOLo8x0F0QB-L-aatbDvdxiNi-32YssXYR068cWACq4l2jRBM30tImmTm2DcUTxejvkMYu2MmSbgBX0XYK9idYu-ix6yj5rn_Sw2L8nnmakZejh1O_V-lIYcMjJnz2uBsqjf9uZaN7M7_F-tMv0O5tn237RpIyfM8AJd7Qf8q4dH2ock-A4KeXMUoQT09_oaGvs8tzfa85yGs-RWvUspvHenI6mSKl8VKP660694B3LGnGokBpwi1yOcyg2hZSJ8RWnCldsOcq4CMKzcZvkIQlAEno21zFS2lgCyKYIM7M3LUh1_ei2B1r3-z_m0ZbomZufoUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دروازه بان اتریش با 2 متر و 5 سانتی متر قد بلند قد ترین بازیکن جام جهانیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/95228" target="_blank">📅 19:30 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
