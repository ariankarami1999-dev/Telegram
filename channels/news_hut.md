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
<img src="https://cdn4.telesco.pe/file/bXca-b8SWx0tTpih1-aWrk_ISuEviuD6adU5B5HPnDPgTUo4dYNkWkX11Ad6rPLAfkUU_12Zs6B6-lRcfvS__Q67sMkXfUw2WAa43yvkzwjKTgHjEOHqoqwAjrukIdM1Il8WHLxkeLWuNHSmsW5ecFXlnQnHtacB5lkhp8CTg0-lWCcKxld0PmpWOOwSZ8Gp0A6fWYrObFqvT7gKpcMgMaWWifcYZeF3M37_mpDtiSdJ3GajspuMv5GUIAHBoNjKs5A9xvRz1axTG4FEaqwqNJsBkWYlNd2FGdmAlVu8l53L0yZKxjjSuQqzSTzTkihcI-2n77rETxU8f6flWfuxsQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 160K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 04:30:39</div>
<hr>

<div class="tg-post" id="msg-68619">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DU2mQgwPPpyeadnPaC7b8QjEsJbE4SGsgk0pZCAmweuXdJvWlpoQZ431_lHBc7ei8xTtVnHPtaNo7xF6OvPtkCHPyGGdSG5hm9SebhwDYphxyHp-lV1iKwr97AfBIW7v32EL8gGfPMFBb18JPUb7sD0uqeGX7SKCjHAYqFsxWSWCOa7h-VFWstCDzzlswvLKhm6PSyn5p9t_n3rWbpbvmHd3GEZfaC5N5LVeMd4RHb8OPJUD59uUFNpPjSgiBwElPRTfclFj60RbXKSf8DDarVo8uXH7YyqMLqHaAntbFYswAwHhsX0e5ZZn-s8enOeyccNsDFx1lY3ObPAeRRCSwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/news_hut/68619" target="_blank">📅 03:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68618">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGZloMVydgeS1So-w3InX_MysJTwgdgj5ihXKaxRsL-muESgz-cffLjSkX_l4uID85gYwl7FGAe-Y485YbKrRySb9BoR-h2w4QoLOQsZj72PIUXuvSGRetyZphq44OMaDH12d5fDLvkFbhCEXvfVJC-quevNA4g65viNrY4klUl48Dtq_qQ_4LkQEfL082KskGlEPU4tGYCsxMljY0LwthvkPzp-ynQM1RAVQGFiI7infu7k2ATXgxui0SdLccqXjugaBcLGf8XNlDhPchhv120CYIJzgqCZHsO0wvlII-keBeWEiiFA0isffYJdwXe0eeyhJ1kvHfFYkIjwqGlThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی در نزدیکی سواحل عمان مورد اصابت قرار گرفت و دچار آتش‌سوزی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/news_hut/68618" target="_blank">📅 03:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68617">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
انفجار شدید در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/news_hut/68617" target="_blank">📅 03:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68616">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
انفجار در خورموج استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/news_hut/68616" target="_blank">📅 03:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68615">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00f692dfa.mp4?token=Er1DmuGkSa8oiaMfI3eR85xoG9kjgtC51y9XBHnp2-IVBHwUv0q6f_gOx8oQ6idy8Zo5Buzsoby9asIQKDU0MYPJYHzjWY56MoFz_qB-Dv7jFqruH8Rae3U6mqYnfQ9F-B_sV98HRlNQW0K0LlCKyrjrwW5oSZcFX6MEftD28hJfkNNdfsnDf8UKNFEkQdJFef8gQLhOhifOUlCkVCyYM2_dFis3lCT4wHD9oBzuZkhF6xLx32o2hHVozNyLNyrGVFFGWI_VJDpyab9-EQqNpRMN_2P2GSpNqNM8MdqhFt_Ca8ec25nPlE1nTFJXSLcy_AAXJUSMNeEdmVBdusiaVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00f692dfa.mp4?token=Er1DmuGkSa8oiaMfI3eR85xoG9kjgtC51y9XBHnp2-IVBHwUv0q6f_gOx8oQ6idy8Zo5Buzsoby9asIQKDU0MYPJYHzjWY56MoFz_qB-Dv7jFqruH8Rae3U6mqYnfQ9F-B_sV98HRlNQW0K0LlCKyrjrwW5oSZcFX6MEftD28hJfkNNdfsnDf8UKNFEkQdJFef8gQLhOhifOUlCkVCyYM2_dFis3lCT4wHD9oBzuZkhF6xLx32o2hHVozNyLNyrGVFFGWI_VJDpyab9-EQqNpRMN_2P2GSpNqNM8MdqhFt_Ca8ec25nPlE1nTFJXSLcy_AAXJUSMNeEdmVBdusiaVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پایگاه امام علی در چابهار مورد حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/news_hut/68615" target="_blank">📅 03:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68614">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/deY1RE5tE3R9RUCd_2JlCn2BYFJkoyO8zv2uWCZleWPmY7Fc3Yg7WewL60DmFhGMzplTm7dr_zVjqBXDwmiGaAv2MZNNMX5DjH7afAzrcJBFE5uicbef2mrWJgCagI3HOHpAbxYkwA_uCcerRmSZMLR0T1ZHNE5NuWA5VUb7OZx3Km2kg-Xwa9ozevewGS_ZeYoI7c-chotKps6Xl7g8MfOu2OoztwQ0_TS98fB7uZwIzSYnor_Ji1LRup-aAreOdbmMH95ddBFpxH5lRAs6ry24wgqIC-j8FPPnzV2FMF0XRBTTt_u9nTMPsQFU-1pSLMelLB5_Rc_SyjuK2-QotA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ماهشهر
@News_Hut</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/news_hut/68614" target="_blank">📅 03:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68613">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
منابع حکومتی:
انفجارهای شدیدی در شهر رأس الخیمه، امارات متحده عربی، رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/news_hut/68613" target="_blank">📅 03:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68611">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521034efe8.mp4?token=Bom7YbBR5XqB8O429GDuRGUjWGyf-pcXD0FH7or1dyFKRHAvdGK9POqNvb7MJeJdWgfdQt9OntU9q1XOgvaT_dKDNSoPF_vJO7XUabiLDtVp4eSQrMJwI9ZnYJwUzr7OxHS2YxFnKptxMYJ0yw1S63mQn0duozRUvYZ2BMm1DA-jYILB5OXIc_XOFwRnjDrutzzX-7xkl6phjhZgn-gAAk_4jg0KSk2CnJDBTrYu2twrQe7X7801QR0z8WP7GttaZnYnqfNFLXHkeQWpecdJx2uOT1jXUi0tV6FyznxZEJ908JlaoRbkuC95rzOXd9IIxA7IoQS4QgKak7eGrFkIDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521034efe8.mp4?token=Bom7YbBR5XqB8O429GDuRGUjWGyf-pcXD0FH7or1dyFKRHAvdGK9POqNvb7MJeJdWgfdQt9OntU9q1XOgvaT_dKDNSoPF_vJO7XUabiLDtVp4eSQrMJwI9ZnYJwUzr7OxHS2YxFnKptxMYJ0yw1S63mQn0duozRUvYZ2BMm1DA-jYILB5OXIc_XOFwRnjDrutzzX-7xkl6phjhZgn-gAAk_4jg0KSk2CnJDBTrYu2twrQe7X7801QR0z8WP7GttaZnYnqfNFLXHkeQWpecdJx2uOT1jXUi0tV6FyznxZEJ908JlaoRbkuC95rzOXd9IIxA7IoQS4QgKak7eGrFkIDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت سربندر ، ماهشهر استان خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/news_hut/68611" target="_blank">📅 03:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68610">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f087874ede.mp4?token=MhmGCduy0uk9iA_8VqqvSm72l22iOMf5Jz8WYdAn23KUWIbm-uGcT8GF_hzEOIVOpNNU410UbsrItjuDLnMMrQiRyvUs5WolVtfscqGN8vd3z1DxBoKxcjthlbZlVl6nrF0SVnVLNJ5BBGTsWg7XgOHJr2e7FgNM98Vw9I6hYbVoRTrzzN00A2y5WAmpCzltooffGq6vb45DMXGsZN0cHQc5mhx-sN2G6kC3BKi01_PCoSBKy7OSPtbL3IlnNAMICBmBGpLwC30sd183cWRY4LUGBv_gJuT-m8cQk5iBgoAPUCmg5TqLYqM47LDpNjPYmqvhwWq0nHZxi52bJroVEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f087874ede.mp4?token=MhmGCduy0uk9iA_8VqqvSm72l22iOMf5Jz8WYdAn23KUWIbm-uGcT8GF_hzEOIVOpNNU410UbsrItjuDLnMMrQiRyvUs5WolVtfscqGN8vd3z1DxBoKxcjthlbZlVl6nrF0SVnVLNJ5BBGTsWg7XgOHJr2e7FgNM98Vw9I6hYbVoRTrzzN00A2y5WAmpCzltooffGq6vb45DMXGsZN0cHQc5mhx-sN2G6kC3BKi01_PCoSBKy7OSPtbL3IlnNAMICBmBGpLwC30sd183cWRY4LUGBv_gJuT-m8cQk5iBgoAPUCmg5TqLYqM47LDpNjPYmqvhwWq0nHZxi52bJroVEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
منتسب به تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/news_hut/68610" target="_blank">📅 03:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68609">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
تسنیم:
دقایقی قبل صدای انفجار در شهرهای تبریز، چابهار، کنارک، بندر ماهشهر، بندر امام خمینی (ره) شنیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/news_hut/68609" target="_blank">📅 03:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68608">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در بندرامام و ماهشهر
@News_Hut</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/news_hut/68608" target="_blank">📅 03:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68607">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/news_hut/68607" target="_blank">📅 03:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68606">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6436592f1.mp4?token=EGPg9G4zCM-Yu7jFDD-rKnKw3SJZrYnGUfttgolBLaKdkbMmvbKGDBqbWXFuFomScQURuRfzRBq_TEV0rJWmdPFbhuzUz81dxSZeXFBhh5yCkAEKLu00ymwBzd3pqiEtskgjVFbYuS8BAp_pAaNFSRzE8k0B6-vs8dITnlqkwI55d-nUoyzcHRJF86EWXW_A5k--AkjW5WygRmpyZoH3vf9GU_FMbpM-2YfWBvNq3KJB8U7Uhehntl2znbe3fPoFIakOZ86vCcSfuIbbEQympFkGCF4kmybAlp7EQ1ORY6Iv2d39c3Z5-DXmuQA3qER2ZNjw4W-KxdzVhsu9k1COCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6436592f1.mp4?token=EGPg9G4zCM-Yu7jFDD-rKnKw3SJZrYnGUfttgolBLaKdkbMmvbKGDBqbWXFuFomScQURuRfzRBq_TEV0rJWmdPFbhuzUz81dxSZeXFBhh5yCkAEKLu00ymwBzd3pqiEtskgjVFbYuS8BAp_pAaNFSRzE8k0B6-vs8dITnlqkwI55d-nUoyzcHRJF86EWXW_A5k--AkjW5WygRmpyZoH3vf9GU_FMbpM-2YfWBvNq3KJB8U7Uhehntl2znbe3fPoFIakOZ86vCcSfuIbbEQympFkGCF4kmybAlp7EQ1ORY6Iv2d39c3Z5-DXmuQA3qER2ZNjw4W-KxdzVhsu9k1COCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله موشکی آمریکا از مبدا کویت
@News_Hut</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/news_hut/68606" target="_blank">📅 03:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68605">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
خبرگزاری مهر:
یه پهباد رو زدیم سرنگون کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/news_hut/68605" target="_blank">📅 03:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68604">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
شنیده شدن صدای چند انفجار در بندر ماهشهر و بندرامام
@News_Hut</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/news_hut/68604" target="_blank">📅 03:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68603">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2e2ba6741.mp4?token=cDFUJmhgb7PP-WlQsMBQkuF_dN5cAkpEeuHCM1jkXVprq3gvzzMHm-SU6B2ETmW-yD9BHi_kM0a4DtSRiLOMmsaY_xaQpZtfQbFiA2VyMpPmsXhU0I7gzA7Z3qH0bWyuXwjWQE-rcD4D_YejMrXQLzzMHPblWApz8TNzZQmu7_IFtk6qdagKeVBEV4pp1pV4GEygndIIdwFe4eTqNtvzCeoOlrhAaUf9Q9Q4Ygq6nc6C7GYByCsR3O_jWwaJ0xNssT_udFPRC4_0sVuMN2RdCYiDtTFhqUHD0MrtgHGfc7i75RWr2sDhg6zbXwHp3dBlJnfJOs6RJ0ZFvbkIwijkDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2e2ba6741.mp4?token=cDFUJmhgb7PP-WlQsMBQkuF_dN5cAkpEeuHCM1jkXVprq3gvzzMHm-SU6B2ETmW-yD9BHi_kM0a4DtSRiLOMmsaY_xaQpZtfQbFiA2VyMpPmsXhU0I7gzA7Z3qH0bWyuXwjWQE-rcD4D_YejMrXQLzzMHPblWApz8TNzZQmu7_IFtk6qdagKeVBEV4pp1pV4GEygndIIdwFe4eTqNtvzCeoOlrhAaUf9Q9Q4Ygq6nc6C7GYByCsR3O_jWwaJ0xNssT_udFPRC4_0sVuMN2RdCYiDtTFhqUHD0MrtgHGfc7i75RWr2sDhg6zbXwHp3dBlJnfJOs6RJ0ZFvbkIwijkDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات آمریکا از کویت به ایران
@News_Hut</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/news_hut/68603" target="_blank">📅 02:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68602">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moLAL9oX-HDi9VCCviAIcrc2-4hroaRt-1IcibVueJEOAofvjThjRp2IcmU0fNWXoRW8xJf7VTv8OajN_leZA9kbIn2Db_GmiaSrhI7ZCOhjzvVhoYA3Kcng8bteTDinRQ9elRoed0FtPTX895Xjp0LdiDuLdvA8kwa9F9MoXj79qPUC2wwJJZ5KpYrcfOI5OMsLX5oE-G-6dTBRK3OHK7Xr7p7EHi5g1WgftEkRDFTp9xvhddfhoXgxvJ5RvQBRvWLMbeaBABLV6E0EpaHtksaPdaFUH0HKdf1mVezgEdPXZNwIlXoOD-NnZphAT7OFA-clHmL0dpWVQS3VhCw24Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنتکام:
امروز ساعت ۱۹:۰۰ به وقت شرقی، برای نهمین شب پیاپی، موج جدیدی از حملات علیه ایران را آغاز کرد. این حملات با هدف تضعیف مستمر توانمندی‌های نظامی ایران که برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامیِ در حال عبور از تنگه هرمز به کار گرفته می‌شوند، ادامه خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/news_hut/68602" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68601">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/news_hut/68601" target="_blank">📅 02:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68600">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز شدن دور جدیدی از حملات آمریکا به ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/news_hut/68600" target="_blank">📅 02:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68599">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
خرم‌آباد چندین انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/news_hut/68599" target="_blank">📅 02:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68598">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
انفجار در بندرامام
@News_Hut</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/news_hut/68598" target="_blank">📅 02:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68597">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3c5e9c78c.mp4?token=NUokd7Sjqv25LM3_nD7kLJMCCZZv6aNiMFSTQFYEG3jk6c5q2UKwmcfwxMs_NlRvFuUg0iKNDqdhnr7UYejCKDp_cz3KACXgw2avXiXZnAuH4pL8Wr3mQZi3_-r9lC6A0rD_o9wo9qWZIq1et6EUdrbmvmPqGh0Gc28gFbDPsVos10JpoHfQZUtyV4BzK6xR6MwwzS-z_mUNs7pt11eYx4i8wLRKxDHvYcU9i85Kox66PCD5GWaCrfBc_jw46YT-WOLa4tegr3XNguIkTLGUSiAj7rUooyO1xcwZ5H-A1vIK33bLnyB_SW1t5ugA4Xac6iw9NiF7q8yURRbuHCPKcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3c5e9c78c.mp4?token=NUokd7Sjqv25LM3_nD7kLJMCCZZv6aNiMFSTQFYEG3jk6c5q2UKwmcfwxMs_NlRvFuUg0iKNDqdhnr7UYejCKDp_cz3KACXgw2avXiXZnAuH4pL8Wr3mQZi3_-r9lC6A0rD_o9wo9qWZIq1et6EUdrbmvmPqGh0Gc28gFbDPsVos10JpoHfQZUtyV4BzK6xR6MwwzS-z_mUNs7pt11eYx4i8wLRKxDHvYcU9i85Kox66PCD5GWaCrfBc_jw46YT-WOLa4tegr3XNguIkTLGUSiAj7rUooyO1xcwZ5H-A1vIK33bLnyB_SW1t5ugA4Xac6iw9NiF7q8yURRbuHCPKcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
چهار انفجار در سایت موشکی تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/68597" target="_blank">📅 02:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68596">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
صدای چندین انفجار در تبریز شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/news_hut/68596" target="_blank">📅 02:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68595">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1IJIfv4igKs_IkHOGV4Hmle3P9AY0Ck6vNMUiZbKmXETfn03NnEaU3iNL85p-6mG1rCsRTISdKouDhXt5bxW9TxFMH61RAJtAH29vN3c-Ul2mB-4k3RC0BvFGKGkxL6Th9-ZYjL9lqxkhCq9IK7qoGiucM4pQv9t9-Mt1fJpMavMjHwMTbJ4UKuDnsTMImBJVPLJDlu_aWLTgLuJR7HyB-i20Znj5pd-A44G3Qokq4jbjXU8cIq48XJOaqkxDieytXyZrktvSEXZNS7dAiecsmB8uxrBBJh8KV1ThaOyJD7bcYMBX4r2S-28QvjgSMXqU1BnzlEW_1lVVkKxfLI4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ بعد بازی:
از دو تیم ممنونم، بازی زیبایی رو به نمایش گذاشتن و تبریک میگم به تیم اسپانیا.
همچنین ایران سلاح هسته‌ای نخواهد داشت
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/68595" target="_blank">📅 02:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68594">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10cd1a4acc.mp4?token=j_fFSiqMQMlF888PNzQqva_JMXXBimPzA7uC-kezShHSh3Nth8AGTydrBtQHUy_hobu0V3IECOdXUvXRk21hOaR7pC5dBRoBRFu-HI8MdA5oN-Sm2kxyIpqJUMtMgVvqlEiE6snuCHSlugToi3KzIuD1_U3rjQVbvPDLwEeLsqin2nVfxNUyOk6mGPWIBgpLhRZ1N1Tq-crkEKUgzuBedR68keVEmoHUHxZD6UQDKUVpI50m4uXle3V_ViIumullHwixHX1GshV7cN_k-QhsBtTDLBT9fHChfgkOmUjox_NXSWnM1LJ_gLt10THIIjDFgRWn2u4_R1Gme_Jn0Lw-1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10cd1a4acc.mp4?token=j_fFSiqMQMlF888PNzQqva_JMXXBimPzA7uC-kezShHSh3Nth8AGTydrBtQHUy_hobu0V3IECOdXUvXRk21hOaR7pC5dBRoBRFu-HI8MdA5oN-Sm2kxyIpqJUMtMgVvqlEiE6snuCHSlugToi3KzIuD1_U3rjQVbvPDLwEeLsqin2nVfxNUyOk6mGPWIBgpLhRZ1N1Tq-crkEKUgzuBedR68keVEmoHUHxZD6UQDKUVpI50m4uXle3V_ViIumullHwixHX1GshV7cN_k-QhsBtTDLBT9fHChfgkOmUjox_NXSWnM1LJ_gLt10THIIjDFgRWn2u4_R1Gme_Jn0Lw-1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🏆
لحظه اهدا جام قهرمانی به تیم ملی اسپانیا توسط دونالد ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/68594" target="_blank">📅 02:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68593">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5ecf5e7ca.mp4?token=TuQWRE1fQ0geHMKeKsosgaO3zpBw5SWQTF8sjwfn3b7JAqdFgJVssmpxiNxjWF4VXs4fOoRr45vpgJ6w7a1X4btMAOv2EGKU4YrmHILiub5e4716GIG7BE08aYOZYeePzExtEox8DGFdNr_4Qx90LFjovpfqVDeRU5XwG0f3HFtmage0szuyWWzdyKHZrueiHRZR95fo0IfJmPPQN8DB_kHlEYouAhx3RjrW399jBTHu6TGlXyHqngMt7UgODkl4EYKtEQre3j4n09AJ3lhgzLcVfKc-TdJMhbAb1oOxEFt4UcNzrc5X1FkP2AiJhhGkMwKm0hIGiLUxoaiAw_FtDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5ecf5e7ca.mp4?token=TuQWRE1fQ0geHMKeKsosgaO3zpBw5SWQTF8sjwfn3b7JAqdFgJVssmpxiNxjWF4VXs4fOoRr45vpgJ6w7a1X4btMAOv2EGKU4YrmHILiub5e4716GIG7BE08aYOZYeePzExtEox8DGFdNr_4Qx90LFjovpfqVDeRU5XwG0f3HFtmage0szuyWWzdyKHZrueiHRZR95fo0IfJmPPQN8DB_kHlEYouAhx3RjrW399jBTHu6TGlXyHqngMt7UgODkl4EYKtEQre3j4n09AJ3lhgzLcVfKc-TdJMhbAb1oOxEFt4UcNzrc5X1FkP2AiJhhGkMwKm0hIGiLUxoaiAw_FtDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
لحظاتی از اهدای مدال نقره به تیم ملی آرژانتین توسط دونالد ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/68593" target="_blank">📅 02:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68592">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067eca16ef.mp4?token=r659grr_NBcRFTKmBK3upLQSRedT3wlo89Ywu3Ev96zKrUEOfwpSiQTgwA9b44TBcoK5bYVcBm6wmar1pPbU5fE9BCDfl1dfhmZp7LThqG7rNIWE_dKbzcA-bp7se7AWENChiuFMMpIdVdX9PR9b9PqBBn6KsWKZeHaQWf7TERvTqw8yD1YpjHcp24Wf9A6BA2rTNO2IUcahgNOBnMP-WvjPkHymrgkzjdX_TQ3UpdP8j4CJjnwswrePAY8eSP1-Mtc3MStYWwmLFha54dc0VC7SSxMeQhuu4LmBRbqAtCv1l4gDoKES4DtDU6MHvruEJVFyRGn7kurjeNq0B1vtQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067eca16ef.mp4?token=r659grr_NBcRFTKmBK3upLQSRedT3wlo89Ywu3Ev96zKrUEOfwpSiQTgwA9b44TBcoK5bYVcBm6wmar1pPbU5fE9BCDfl1dfhmZp7LThqG7rNIWE_dKbzcA-bp7se7AWENChiuFMMpIdVdX9PR9b9PqBBn6KsWKZeHaQWf7TERvTqw8yD1YpjHcp24Wf9A6BA2rTNO2IUcahgNOBnMP-WvjPkHymrgkzjdX_TQ3UpdP8j4CJjnwswrePAY8eSP1-Mtc3MStYWwmLFha54dc0VC7SSxMeQhuu4LmBRbqAtCv1l4gDoKES4DtDU6MHvruEJVFyRGn7kurjeNq0B1vtQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دونالد ترامپ به منظور اهدای جام قهرمانی به تیم ملی اسپانیا وارد زمین مسابقه شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/68592" target="_blank">📅 02:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68591">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDBxc1YV0waSAb3YqO6fC7RnSYBUSRwYiCyFb6g62P6BpybJ8IyEhNWuaM5akUxsI1udpmCuovB2y_vGAN43mR0k8Ay_DhnrhKLQlBi2aEdc82i8cWFFojY1gC74vCOGAI6myRONq1Pn6yfTvsU6adwFsD9Rp-Y1nUk2XjCPx6uxL_PRhmq5axkWO1KxFxYjOnUBahP2GYWceY-gfOySd2dnM7ua8g-N7kuVMZTtfCqp5ukyP-e8KsPh6GGVJjIGAlswm_Y1lHYxJFH3T4az9AjDX5_At_jnLRgFgH9Y5f8sJbwnUqR8nCswJeBLdj7qMDS30p_a-WOXKSiDfyAs8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
عرزشیا به زودی:
ژنرال فرنان تورِس، از جمهوری اسلامی اسپانیا، گلزن در مقابل آرژانتین
😟
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/68591" target="_blank">📅 02:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68590">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqDKaOPJQr7FAnwUN-gN5J_DYGbEWfGPQcOWWwblzzGZfXw9LwGPOq4J_MjJ4oQXeqHKuxT20b8PHZcSpDrdJTekewJ2SWYUKfTt10ZF54WEvAuOnHp1U7LRwhxAcjgFdxblfKxZSGcXEzb3mQVDcr_-9uXSt6ZBXJ6KoxK1pbx0FV8uXnnptx3ZOHs6SUTICyXHYIqLjy9-V8q9i0HS1uz5Q5hgRvWVL4qyb_zEB5HARZh_7DN1qwvCttxI2sMc8EQ7FuonI9QjKObyTSa3WxovmXQnJv21rkvQao7l4iubibDuO4fbF3ps_JT3JuInjexJ-h_-rwhcd-but_HslA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ اومد تو زمین
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/68590" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68589">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">امشب سنتکام نمی‌زنه یعنی؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/68589" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68588">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaXC7OmrvgMXsvlKWbRdc1kiVgNRi_W4wfa_Qj7_IKvVs_eZey88BPDtUFGyYjCEdM0VpXnioSAjGOeL43XGnVNyxb7DKM61bi0cAV0Q6GILaFidZEZdMPs08DRh6fnd-bwfjOvgcRbD7uYZ4RPPqmDFK8yNKIVqpmSwPf_WYkjT1umvjWUGL-gUQp864kZZwazkH951lgA_dKPoZb9pnIMrR2qURCULAosOCvCahHwtznXztOEf_DcSw-J4BjT4vMfaJCBQ02FCG-f3SBJ9rsu-5h0HdkW4kGmEqq9BEEReVG5X_0R_HHA_-7fqJzIH6jRbWMUCQXjM9tiHBxivPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آقا تموم شد به راننده بگید حرکت کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/68588" target="_blank">📅 01:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68587">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPRxR1fxo0Icm57grzU0YKiMLbF4_e_9StNqXMQTCN7SvGkd2asn_Ev_HG7mmWjGjIhBQBwXhk85BVGpoVV2ZYSCTVeACxgSbAHAHdo_MC2oETKyMPZgquExw-XFbVPMQbmvdhUXCYkj4hIiq7_6Mx4pFU2ehfBNfonlf4gtk0pJ3bUJoF0x209ajS5MlN3i2THjpmYrnEIQ40hOa7rlq4j2YMJnZltugrL4cGQcWcYfDpLVqsVVu98x70XB9O1ZjL4b4sAuTK-Ws3la3PUt80Oc14ZiG_F40gxQNhCjhD6UasF7egIDsYtrjczh-z_xAH6GZFe-AKEmZFKDHdvHAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی 2026 هم با همه خنده‌ها و گریه‌ها تموم شد؛
قهرمان: اسپانیا
🇪🇸
نایب قهرمان: آرژانتین
🇦🇷
مقام سومی: انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آقای گل: امباپه
🇫🇷
آقای پاس‌گل: اولیسه
🇫🇷
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/68587" target="_blank">📅 01:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68586">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDHmdL2Ei3K605d0pRVm-GQCJGuLaxf4eh2mp5dS3i5o-ZNIGNkMKh95BxsFSmBSMAsWV5k1KgBgO5h4zE41rN3GH9OfZSfxIneEiczgUNv-Zu63YNy1znn3fGGinpYWEmVhM0zferaQpuOdrEpzlzA5yxZo2sbBjKmcwGDt7_nf8ZXaX53y-Kzp3PKY7faxzK6PALWKbg9Qi8_B7opONaRPonezCD4KtM8FWkOEEhSILlWt9BiD_rqRz98ofwK8mv_oOUBusF9qXhY1vvQzfkVC_1XbMO5Nr4LuRPb9YeHcgn8-6VxigO828qQXu8ZEolAKBusod-ZooErp99nXQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💢
🏆
تماااام؛اسپانیا قهرمان جام‌جهانی 2026شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/68586" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68585">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اسپانیا خیلی بهتر بازی کرد انصافاً
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/68585" target="_blank">📅 01:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68584">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇪🇸
گل اول اسپانیا به آرژانتین توسط تورس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/68584" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68583">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
گل اول اسپانیا به آرژانتین
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/68583" target="_blank">📅 01:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68582">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plZv_R1RZlgRoK-l3msxZKS1atAdgauomM8pCI-mnbeivTPkrhcP_WeWrJR5zu0vx3Dj2SxJAROSGYBtispA8jFCyyck4iVqRqbwMertkyQEORePONOfccTkd7f-HV2oESFN_MKIKKYSSPdyKeOfor0UvIKQxMhVRvZLvq3xBBIhqHXU4ILDVLatGaj0-9_odyDg2OZeC_OGDLrjIPg2c4oaWIGfr4Tlt-KGWkHhB7kytoKK9W8m8Cm-TbhPVrkMXwOYp3dB5EnOI4SZHCVAuDKMsq1i51gFEnN5BqaClS7wXU0xodLZVt0y61do7qQ2BgXFlB6vbsZkKIktlML4Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پرچم شیروخورشید در ورزشگاه
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/68582" target="_blank">📅 01:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68581">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بازی که رفت ۱۲۰ دقیقه، نیروهای سنتکام هم دارن فینال رو می‌بینن، حملات امشب، نیم ساعت تاخیر داره
😁
#hjAly‌</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/68581" target="_blank">📅 00:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68580">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
آرژانتین ده نفره شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/68580" target="_blank">📅 00:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68579">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
آژیر خطر در بحرین به صدا در آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/68579" target="_blank">📅 00:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68577">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a67fe75354.mov?token=NNk1hCgzCGv1QUOlWVSC3r9xX9O1ruziHqplxxhcpa1doEn1mKirA39LbooX_15DNZpu8S1DTj2OZQwOwp9AZ4UqHK0M5OtFTeQD-gYc9J8Wl8MMbqkj2v2mp-IgltmY_ZOOIdEodb_ui3acHYLgiVjndVZu7yefx-oSrNTzM2bpHtYZdMC4PzQBIx6iHYH13rQ5s0L78AMo9RTxMBaeCkP3Q4VG4L5LCzLzGaDcUtYMa3CLDLOtUU7KUHfGt5pjqqsJjqJhwdriAq1DqxJCk6ge-gd1B7dFdgxSFtfFKZ1bBBs1CEKenAKqcpb7mWAjOvBbPnA1tYaF0NboxzTWmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a67fe75354.mov?token=NNk1hCgzCGv1QUOlWVSC3r9xX9O1ruziHqplxxhcpa1doEn1mKirA39LbooX_15DNZpu8S1DTj2OZQwOwp9AZ4UqHK0M5OtFTeQD-gYc9J8Wl8MMbqkj2v2mp-IgltmY_ZOOIdEodb_ui3acHYLgiVjndVZu7yefx-oSrNTzM2bpHtYZdMC4PzQBIx6iHYH13rQ5s0L78AMo9RTxMBaeCkP3Q4VG4L5LCzLzGaDcUtYMa3CLDLOtUU7KUHfGt5pjqqsJjqJhwdriAq1DqxJCk6ge-gd1B7dFdgxSFtfFKZ1bBBs1CEKenAKqcpb7mWAjOvBbPnA1tYaF0NboxzTWmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گویا از قم موشک‌ پرتاب کردن
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68577" target="_blank">📅 00:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68576">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sv8L5ykZdBgCBr_bGI4ObcrQ5vmCKrcFZH2pioJ0F0J2E3hwtU2Of64EhaHFLNpLa6dWmU-mUzRK06w7CvCjYfnQ5PTHNHqp_Zy07b2VrHYTvnTrEqldTwqJm6kl3qwKWrCe-uU0voScAOgu7THI-nUI9tkyGycW8wFTA-ZZMyWqq6soJiGIHPjpucz51cASqQweZrS6IN0_5XegwveVTuVVJeHQhTNQ5R_BwAYrniHnuugKdzBxReNa1gVPbUw74FrFeKkZaK4qvVMrSNoLhjGhAaCnp5srmvTBr84vzCkVcynuikS1niTwlDm6k3J5MxPJtzEjB6TVpwj-CKb06w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو بیژن تو فینال
🔥
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/68576" target="_blank">📅 00:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68574">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🏆
اجرای کامل شکیرا در بین‌ دو‌ نیمه
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/68574" target="_blank">📅 00:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68573">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🏆
🔞
🇱🇧
حضور میاخلیفه، پورن استار اهل کشور لبنان در آمریکا برای تماشای فینال  @HutNewsPlus</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/68573" target="_blank">📅 00:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68572">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در ساوه  @News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/68572" target="_blank">📅 00:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68571">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در ساوه
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/68571" target="_blank">📅 00:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68570">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416fb2b432.mp4?token=G3M7TgIbjC9Qays5HDHYxfpn-NJfRIjbunyhFTeDvyZw8maFmIsVFPPBkHly3scxQpYWnGFa22vhK7_IUA9O6NvuNezh58lp6864FoAJjngm67fjSJiPHk2PO6CQ84aide7l4m3bNGZTV8mAcJSMCZVqzn3-KhxiHI9RFmcYN5HU--0mErRGC2xqC5nsIJFKkXM-vu3H1aygXdJLZS6E_HjhAxsIjgFScVJf4eyFsPuKO-Lgcgntl9Zd2UR0KNxH9TeadVuj1gAe7uM7dEUjipR1KzNKvdFGpK76USNJcky3nA4Kf1SaLaF-ArvUO4GaqvxhoY7CrivM21C7FDnT2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416fb2b432.mp4?token=G3M7TgIbjC9Qays5HDHYxfpn-NJfRIjbunyhFTeDvyZw8maFmIsVFPPBkHly3scxQpYWnGFa22vhK7_IUA9O6NvuNezh58lp6864FoAJjngm67fjSJiPHk2PO6CQ84aide7l4m3bNGZTV8mAcJSMCZVqzn3-KhxiHI9RFmcYN5HU--0mErRGC2xqC5nsIJFKkXM-vu3H1aygXdJLZS6E_HjhAxsIjgFScVJf4eyFsPuKO-Lgcgntl9Zd2UR0KNxH9TeadVuj1gAe7uM7dEUjipR1KzNKvdFGpK76USNJcky3nA4Kf1SaLaF-ArvUO4GaqvxhoY7CrivM21C7FDnT2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
اجرای عمو بیژن
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68570" target="_blank">📅 23:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68569">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOb5badZYncXb2Ww-TKJpfTw4gPgy7i9PXEs6zlBd35rKBW0h2N7Ys3BY5wjIX9ubkdZkGzbZklHv06QfsvvnP1OAz2TedF16Ju3Y6VsSZ2rUMUEk9kLs9nNzWDzi0Q6hmv74vYuq0mv6g7EEDWL0Va0bdMAbj8K2utFqDsyzxyHEe7ns021zH4mv-7eJ5O0aTpntt3p_e2TsBQK8m9-90Jhu3ynhQAcxaeBHSgHqrELuT3ULh2ygpyEMz68LHV49Q-4Wc-vGxBl9gB5nIlD4RJgQkifqVnUdQ0FJnlSDVNsji_h2sEkCUtM5a3O5WWomWTogEbDQaCJZ93I7vUSDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه آرژانتینا دارن کامل لخت می‌شن
🔥
👀
🔥
🔗
مشاهده ویدیوی لو رفته از دختر آرژانتینی
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/68569" target="_blank">📅 23:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68567">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esWc0ZdpjBhjOcDMTTnxVMfV6eUBRIncutmrcCwA_mLRWyMj32dN9Uy5ruLGzf26a0ZPoc2HTOD9E3j0JayK3E-wsLb_-IgL0POINWOrx6_T5it2OTK43oJVQ_8x9tt9FEiWL4BMcmhXp9dQ16GCcOQBh9rIYrq_5yVftfs_fP2EVIjHpOoEV0wsC1qkFdmc4rtXYIeChl5EgpoMr4iwXSGvPmXwh7LwW2KKkO6IqwsZ3uHlS8Usv8bR5OKiySFvxJz5vRj6vFvgRSArM3PG_UgX7yMev0M9YbjNIpdosWo7gcev5NTEILnIvga-ZNBoKi_LG8eoYzmamLVlZN3miA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:یک نظامی آمریکایی در شمال عراق در تاریخ ۱۸ ژوئیه و حین عملیات انهدام کنترل‌شدۀ مهمات عمل‌نکرده‌ی به‌جامانده از یک پهپاد تهاجمی یک‌طرفه (انتحاری) ایرانی، جان خود را از دست داد.
روز گذشته، فرماندهی مرکزی ایالات متحده (سنتکام) خبر جان‌باختن دو نظامی آمریکایی و مفقود شدن یک نظامی دیگر در اردن را، در پی حمله ایران در تاریخ ۱۷ ژوئیه، اعلام کرد.
پس از یک عملیات جستجوی دقیق، نیروهای نظامی آمریکا امروز بقایای جسدی را که هویت آن هنوز مشخص نشده است، در محل حادثه پیدا کردند.
فرآیند بررسی برای شناسایی و تأیید هویت این بقایا در جریان است.
در رویدادی جداگانه، یک نظامی آمریکایی در شمال عراق در تاریخ ۱۸ ژوئیه و حین عملیات انهدام کنترل‌شدۀ مهمات عمل‌نکرده‌ی به‌جامانده از یک پهپاد تهاجمی یک‌طرفه (انتحاری) ایرانی، جان خود را از دست داد.
نظامی دیگری نیز در این حادثه مجروح شد و همچنان برای درمان جراحتی سطحی تحت مراقبت‌های پزشکی قرار دارد.
سنتکام به احترام خانواده‌های این افراد و تا زمان تکمیل مراحل اطلاع‌رسانی به آن‌ها، از انتشار جزئیات بیشتر، از جمله هویت نظامیان مفقود و جان‌باخته، خودداری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68567" target="_blank">📅 23:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68566">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uu8PiutGI_EWrL9qktMIUsHWvgsUR5iKA83wwmd6MCfrl35YjST_gEUNrupTgq_qiHdxngzhRVyxICpyH23TMswafWdShJzlbC4DlcO5LfJVtVwXummZwIpIOLZE2DOpMBJlj7B0JQ3wVRKviXSw6PUFDtPIpz-krKXqCb1yCInbbKB8A51sPGJk-LYYQoWdXGzU-OPReWjfIH58lEWqDCVHcgRJYZRA0Rh3mepAeLVknObenDIkEGuFuDdY4A1qNnk5V7gZZS85ABNhqp1le96H2OwZGDJgxnIlTX7njwGnsmataCfciWDDv-rdaLtLSi3giWQ53HaRIhZDsD-IIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا کاری به کریس‌فن‌ها ندارم ولی هرچی چپول، عرزشی و فلسطینی‌فن توی دنیا هست امشب طرفدار اسپانیاست، به امید باخت این تیم کثیف و سراسر چرک #hjAly‌</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/68566" target="_blank">📅 23:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68565">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3cfd8ff5.mp4?token=a9e_uLNqd7cotZhRHuB0fo1cAfJYGvAl1vasSFBP0v34Tx1NMmq8wObwKt4tYHXibrUrnVcznKseE0BoJCKJM4YI9_MSG0Pis2riYqhfpmmQ0brUcD2uEva-09jpcw6UAZlHYUwlULRi6_9zFTNYWLhbau2dkavfw6sIS9QSkUFUBwbcDbBMSIaLRkY8E8F0aAUqgPy0s7BG_iWmkutrhcF90N6-k1PozO3NGeCaxrEcle9jsYcioxUcLxb8E9B5EAxdy5i7OSHXYpIzQjK1JkOkOS12NDU9TyacTvzBpxkvogDeMX3Kuu5O5NGBX93DhdG-OOm9JBRM4wWVvSI2NEZoCFiK5wk0LXg2f15OPbFbJ7pXVzhlglSlsZxnjS_h0dGYMIaJKpvQJdTiYwrUiEQ5XkiRjG0mAcu2kQ_Qyi_9ogJ43OSvWb9DAWtRJhKs88v_3JWs7-qLvseHHb77EWnMYjYm97xRyKvxm0s9023RLtX9fD8j3exQDfHCg9WNmxeKKAtjyeE3zQxf7BMBXnqzpVlFuVld8cwDAf1ytuV1TMuM4qHGjd3OZY9vD_gdyqQLnyl0BN07JBOMLSINeXlPUdWSubREIm1z0m1DlV388KMCjkhbVNfDST5qPKEqYJTAHXTXi4rdmeDilHZ9TA7A6iHwGBfbm3Q0fBtdJk4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3cfd8ff5.mp4?token=a9e_uLNqd7cotZhRHuB0fo1cAfJYGvAl1vasSFBP0v34Tx1NMmq8wObwKt4tYHXibrUrnVcznKseE0BoJCKJM4YI9_MSG0Pis2riYqhfpmmQ0brUcD2uEva-09jpcw6UAZlHYUwlULRi6_9zFTNYWLhbau2dkavfw6sIS9QSkUFUBwbcDbBMSIaLRkY8E8F0aAUqgPy0s7BG_iWmkutrhcF90N6-k1PozO3NGeCaxrEcle9jsYcioxUcLxb8E9B5EAxdy5i7OSHXYpIzQjK1JkOkOS12NDU9TyacTvzBpxkvogDeMX3Kuu5O5NGBX93DhdG-OOm9JBRM4wWVvSI2NEZoCFiK5wk0LXg2f15OPbFbJ7pXVzhlglSlsZxnjS_h0dGYMIaJKpvQJdTiYwrUiEQ5XkiRjG0mAcu2kQ_Qyi_9ogJ43OSvWb9DAWtRJhKs88v_3JWs7-qLvseHHb77EWnMYjYm97xRyKvxm0s9023RLtX9fD8j3exQDfHCg9WNmxeKKAtjyeE3zQxf7BMBXnqzpVlFuVld8cwDAf1ytuV1TMuM4qHGjd3OZY9vD_gdyqQLnyl0BN07JBOMLSINeXlPUdWSubREIm1z0m1DlV388KMCjkhbVNfDST5qPKEqYJTAHXTXi4rdmeDilHZ9TA7A6iHwGBfbm3Q0fBtdJk4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇺🇸
پرزیدنت ترامپ و بانوی اول ایوانکا ترامپ در کنار اینفانتینو در بخش وی آی پی استادیوم
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/68565" target="_blank">📅 23:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68564">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zri1ytGa_taBkzXmFm4vw8n5Yl3WW7-QPBgvAkPuwEXzM4vWe6C8yyZxoxMErw_azdmkn9QexABHj4-km-qytlskNoEFipwlh5opj5ODg33cB-7O2c7EvVWDhseV7J9BuLE0EMNrlE1PCWxk_Kl-ODFGUwZ5XAb1Tj3cLBzvVBmx-lISXaEetnyU5UfdmhDTOMoBxHGzT3g4x-na0UJ_0ejIvi5Jas8Z7EUeMsQndnBu51mQH5XQrnUhAtkE8kWUYyrrGwmFkq5ucl5zpBT_xAR3i-IwdwT9jFHgn2YPX2t9bw02aL2OJAQp3NkboF0FkKZNYmsyN6LnheD1uxH_qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
گزارشگر صداوسیما : هیچ تصویری از ترامپ کودک‌کش و جنایتکار نشون نمی‌دیم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/68564" target="_blank">📅 23:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68563">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حالا کاری به کریس‌فن‌ها ندارم ولی هرچی چپول، عرزشی و فلسطینی‌فن توی دنیا هست امشب طرفدار اسپانیاست، به امید باخت این تیم کثیف و سراسر چرک
#hjAly‌</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68563" target="_blank">📅 22:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68562">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOlji2n3SSKvNu3IYu_K8yj0hhNWizLcV_8i28grm8tlB6Sgs7Rn21Mfak9CzcYlqVaskW-DTBUiTMze3LGu-uv4Zc31Co1bNYdbZ63W3LBxZ7br-_JENUEj-1vAQHzyDwKSJRiv6kLnGk1WoV6-GijLgpDMUTCfglGBLYAjT7f6xl_8Bm_lW-ervMFLgGeopgevamgA1lP_b4Tvk7g1gSuev9cNfzXGefa23EBhllkS2mtLYo44BTxek7pneT5wRwdix31ze0vwfZAnRlVjeEgEMV-2bsQGS8IcS2YmME1bjXPsXX768SJxNRDL5i8nAL8Wz7C9mMvHObxeLPiRLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
هم‌اکنون ترامپ پشت شیشه ضدگلوله
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68562" target="_blank">📅 22:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68561">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nup3XcAVs-cb_FEl4FHfV7rbkTE09WAxZIZFzQXvj2u2Vnd2n9k_dorSzv-W2_y5AWZhn1_DqX7cB3dFbFyk7N4AJ9QGRlIRcufJIyibFuTXDfzriNAGizvdUhjhAi17GPIVwALDM-EZjBGFmEZcTQEMRzawkT71FOpTA7lHhaCekCTbKaZvhF7FiQzpofJ2O3Kgol-LIgZyB3FuK1QKv3t9K4VKtRupX8BC8S_z8odOsb3q64tMJuSqxo4JKT3ZxwM--k5V9vYqeBUqaLJDfOpbzTChCUkhOqxGyZ6c3KjAyAGGf0PBW2WxKcw09lR5jWCGzplzjnOyuMfiqnRbyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فینال جام جهانی هم شروع شد
سپی
یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… همرو
بدون سانسور و رایگان
میزاره
گفتم اینجا هم معرفی کنم شاید به دردتون بخوره.
هرکی خواست بازی رو با پوشش کامل‌تر دنبال کنه یه سر به چسفیل
بزنه
👇
لینک پخش بازی:
https://chosefil.com/fa/programs/318
ایدی کانال تلگرامش:
@officialchosefil</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/68561" target="_blank">📅 22:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68560">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c88de66012.mp4?token=aQVx_8A2mFN57TuBoxHHYmLFusGZOCSTfb2dp_IK3jYlwxv-KGJwoRv-ijOSdXxfKsLNWps4NK5KUjmxFMXMfiNzKGjxdZ4zjB6QCC3IaUmdJHl2oQz2kCCZs8QpSfhJIMK7k3cve_okWmXdqqLj4ey1cLwiQJwd910gORSRbbwE2vR5JfXNx3eNhJzruT1HwmqNKT3pZh0ZoPfIY3gXRbgZztN0y57pw6S8ZJV76EWFeFsFlGALZ4pw_4X4wkEFoknz7ycxCP322N1ui4fIygFzlp5icMpkV4Z2XrRYqF9EioqcKBP_aTDZ41FTg3Oq3c7ys2U7SQK-_GFuxCgWMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c88de66012.mp4?token=aQVx_8A2mFN57TuBoxHHYmLFusGZOCSTfb2dp_IK3jYlwxv-KGJwoRv-ijOSdXxfKsLNWps4NK5KUjmxFMXMfiNzKGjxdZ4zjB6QCC3IaUmdJHl2oQz2kCCZs8QpSfhJIMK7k3cve_okWmXdqqLj4ey1cLwiQJwd910gORSRbbwE2vR5JfXNx3eNhJzruT1HwmqNKT3pZh0ZoPfIY3gXRbgZztN0y57pw6S8ZJV76EWFeFsFlGALZ4pw_4X4wkEFoknz7ycxCP322N1ui4fIygFzlp5icMpkV4Z2XrRYqF9EioqcKBP_aTDZ41FTg3Oq3c7ys2U7SQK-_GFuxCgWMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری حکومتی:مشهد در18و19دی پنج ساعت سقوط کرده بود.
عراقچی: اصلا انتظار اعتراضات ۱۸ و ۱۹ دی رو نداشتیم، جمعیت خیلی بیشتر از چیزی بود که فکر میکردیم
.
مجری: ترامپ درست می‌گفت، من رفتم آمارش رو درآوردم، مشهد در عرض چند ساعت سقوط کرده بود!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68560" target="_blank">📅 22:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68559">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c26a9bf5f.mp4?token=T3zXlS3u3MLKh6h7tBPTODIsNAnUDUZkNxvH_eLvHnMaAvi_2WIiw1idNv-XIWTCNh0ISinbjNlkiA3PXur5WsIEwt6qpgCcgtV_NhXjcImW-CnW-WalDVRWL-ZForlqXsUU5VFjE_SIImw4Pn1X9AGtKnDEu9LZDzMXLt7gW3QiMGDQC85_Jw_pYMc37OiRIRSut-RTCpJN0sJR-oU1xmzRcnjoM6P9706fshyM_35M6LD7SzWKRPG_n0II-A2XavsUHohet8MZNzOn42jzd3yqIL9JpylKUaDDdqDYJaDFDYpDhwggp4ocj2RiKuXFmh5xgujxEFPJFn8NTcqjZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c26a9bf5f.mp4?token=T3zXlS3u3MLKh6h7tBPTODIsNAnUDUZkNxvH_eLvHnMaAvi_2WIiw1idNv-XIWTCNh0ISinbjNlkiA3PXur5WsIEwt6qpgCcgtV_NhXjcImW-CnW-WalDVRWL-ZForlqXsUU5VFjE_SIImw4Pn1X9AGtKnDEu9LZDzMXLt7gW3QiMGDQC85_Jw_pYMc37OiRIRSut-RTCpJN0sJR-oU1xmzRcnjoM6P9706fshyM_35M6LD7SzWKRPG_n0II-A2XavsUHohet8MZNzOn42jzd3yqIL9JpylKUaDDdqDYJaDFDYpDhwggp4ocj2RiKuXFmh5xgujxEFPJFn8NTcqjZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پخش تلویزیونی اسرائیل؛مقامات امنیتی اسرائیل و ایالات متحده:
ایالات متحده در حال آماده‌سازی برای تشدید حملات خود به ایران است.
این هفته، خاورمیانه شاهد تعداد بی‌سابقه‌ای از هواپیماهای تانکر سوخت‌رسان خواهد بود، که این تعداد حتی در مقایسه با آمار ثبت‌شده در جنگ اخیر، غیرمعمول است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68559" target="_blank">📅 21:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68558">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
کانال ۱۳ اسرائیل :
دونالد ترامپ، رئیس‌جمهور ایالات متحده، پیامی به کشورهای حاشیه خلیج فارس ارسال کرده است که در آن تأکید شده است: اگر این هفته آتش‌بس برقرار نشود، این کشورها باید خود را برای تشدید تنش‌ها آماده کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68558" target="_blank">📅 21:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68557">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
استانداری خوزستان:
دقایقی پیش یکی از مناطق خارج از محدوده  شهر و حاشیه‌ شهرستان آبادان توسط دشمن آمریکایی مورد حمله موشکی قرار گرفت. این حمله تلفات جانی در پی نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68557" target="_blank">📅 21:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68556">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مسی و نتانیاهو
🇮🇱
یا یامال و فلسطین
🇵🇸
؟!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68556" target="_blank">📅 21:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68554">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UHZGDWBfFOp0nbdHKExJN2qlj5qkVW5L4fzYbZOagVj3iIIwLYkPLLmDH1WKUq8AvrOrUrUftU8kpYe9c6daFwAsfPI5N3wjq7xF_0IgsWKuJS5z6vl2EfLLGhMHMllM5W6dTbGMDSPCo58V-VMCQUx5Ui_2szKDJ6HpEo6j3H9DVpN7mOd95i59WNXv48efG7PX6xB1GOtLbTrxDCZm73aYypKNbFZV2v01oMG0sgqOPNyE3lSt76cbTDunD9akA5hOtaXNUn2pOVmMwa-xeKZjZRPO1GPXDExyPfIMNVqj6m95dugMIlLbuPGcgj253l-ZIHdHI24jFMf7EfmIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HakuTlevRBJq0prKzEmkh47d8J_wcDX1qaEt_aZfnhLiZ8RDqtULeZGzeosYZXBZB9piwP0d75Eo4xl2dj0ncHnfu6AKGbXNZy989nkhooL3Iw75eH6SnsD1zq9I2nYNMr5jluBHke8rpXLe4ZY_tTbOpZRgmUo73tWYm4E_FArJ7Bbhg3dmFXepV_X2-habVjV9_-3pCQdPCSbSLVqvfeXwkSFhhd_HAjkIksFtAiq_u4mdUmYnIcpQU_N7Ifza_EYU2P1hVLw7xwY4l68MAOzzvWXiFt2NDmPlIUt50CJhuoRPKxB-2doExCb4EjhJvF-aUSySiRnkq5R7ael9aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💢
🏆
فینال جام جهانی 2026؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68554" target="_blank">📅 20:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68553">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
یک پیشنهاد جدید آتش‌بس ده روزه از سوی قطر ارائه شده:
• ایالات متحده حملات را متوقف خواهد کرد.
• ایران دو مسیر دریایی در تنگه هرمز را به مدت 10 روز باز خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68553" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68552">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e08df79c06.mp4?token=o7KsnWtyht46vQguGrQDO-wCDSmMhu8oPbBnznH63plHDAIgGO9Z03dk9d5aAfFSGjbk9RW9I8jVb7bdDjildaN7uh9kImyf84Mpdbk5OtPU2Ruef2wI_dSfU_mUCPJHUjhjgumAI_VZoL85SCe19KlM47gx_NJ3wOU06xPxti3IXsCqCgq61IzOTriuAzCoggw-Lri7OJ94n4B62im0yyD9kr3tKEBT_l0I5ls_u_Cph3zZ8sgQJNELcuIYQGCcyk4uWesa8NN5_kDanG8S_ijhDdSwMFW1CM57EjxOodaZsAhmK5Z9wLMe6_qLeEBQ3dEDZ_N2Bfxl5zoqpCu0Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e08df79c06.mp4?token=o7KsnWtyht46vQguGrQDO-wCDSmMhu8oPbBnznH63plHDAIgGO9Z03dk9d5aAfFSGjbk9RW9I8jVb7bdDjildaN7uh9kImyf84Mpdbk5OtPU2Ruef2wI_dSfU_mUCPJHUjhjgumAI_VZoL85SCe19KlM47gx_NJ3wOU06xPxti3IXsCqCgq61IzOTriuAzCoggw-Lri7OJ94n4B62im0yyD9kr3tKEBT_l0I5ls_u_Cph3zZ8sgQJNELcuIYQGCcyk4uWesa8NN5_kDanG8S_ijhDdSwMFW1CM57EjxOodaZsAhmK5Z9wLMe6_qLeEBQ3dEDZ_N2Bfxl5zoqpCu0Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
رئیس هلال احمر:
در تشییع میلیونی نه تنها یک فوتی هم نداشتیم بلکه شاهد چندین تولد نوزاد نیز بودیم
👅
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68552" target="_blank">📅 20:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68551">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7091c7c4c.mp4?token=fMcJmR-n9nL1AG7Ro8GiM4CASjoXpybmIb7uVkrc0lx3aVNY243Aq78AxZV8yTyTnAhBWFZ1vHk7MSIMydoNsi0yc_0z_39mv6G2_23TyWf1ZnXc8wEwD4mHcBF255v-2T9yjkgrgRl3FDJqXRd0GBaJc6wICGzS6ALjMlTxoZ_mzX1dYAPCxPGzwDxqkWbjZGtPAcaCXS2OEIaZGCJuKNCdgk3Iy5xNUI7m7eafPMZAwUrujTaEBNQvRPTCB5Jjdjd6sckhGl_Orf7zauM3mgAv2G9a8-yVeGuBtJuhUQmPO5hQAbyawvFkJ-oqixXD1Stcj11Ph0S1Qgnfs_v7pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7091c7c4c.mp4?token=fMcJmR-n9nL1AG7Ro8GiM4CASjoXpybmIb7uVkrc0lx3aVNY243Aq78AxZV8yTyTnAhBWFZ1vHk7MSIMydoNsi0yc_0z_39mv6G2_23TyWf1ZnXc8wEwD4mHcBF255v-2T9yjkgrgRl3FDJqXRd0GBaJc6wICGzS6ALjMlTxoZ_mzX1dYAPCxPGzwDxqkWbjZGtPAcaCXS2OEIaZGCJuKNCdgk3Iy5xNUI7m7eafPMZAwUrujTaEBNQvRPTCB5Jjdjd6sckhGl_Orf7zauM3mgAv2G9a8-yVeGuBtJuhUQmPO5hQAbyawvFkJ-oqixXD1Stcj11Ph0S1Qgnfs_v7pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو :
آرژانتین امشب قهرمان جام‌جهانی میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68551" target="_blank">📅 19:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68550">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i732u5z9bGcueAGlw6d2-Yxh-54mFWH8SKQNafcf3MClOUovxwCP6iHRwVTcmACw1MqcH9H6O4GmhRqMmQhqhvWpwLNKMAhOdLyMcDaUr1LCroRohr_JvsJkRULsvgO_B6_cBaDyseTIZc4ZfdP4R35iyVb2LGl1dqLE8PZzeKza9eLNIzw_d7JPtMZ4rD1OZgOENO3CQsOM0ecqCsB-P4hqbNTzb43UhW1Ath38i5z56RJeko-cYWtil1_VCp05wXCPAtHxFH0o_lEsHjskEsVMFwNWVEY4NdCADt_3xuJP8cBfDQ8S7FwGdSSZOiA87aNVluK4FXTEtzZZp7LyHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه امشب نیروگاهی در ایران هدف قرار بگیره، مقصر اون فرماندهای زن‌جنده‌ی سپاهن که امروز برق کویت رو زدن. #hjAly‌</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68550" target="_blank">📅 19:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68549">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‼️
رسانه های عبری:
برآورد‌های امنیتی اسرائیل حاکی است که رهبری ایران دستور حمله به اسرائیل را صادر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68549" target="_blank">📅 19:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68548">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
هدف قرار‌گرفتن یک نیروگاه برق در کویت  @News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68548" target="_blank">📅 19:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68547">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VM-aNTucoC_3fWMvxGhtTNVSdA5b3P4bjRIY3bwnTw20qBbbj55s6xruIZgiePEg9yG4iFW9kPRZc2MH_01P0BgPTW-NHXMkAJsPd6Ge093xY0v2a1as7adyVbfsUWA-78LWN9IavskG9Cvw-h3P4yhMjSp4kLDv8uK8XO01gViq3M0xI_VYWqQq9jefkPdRGSISz5Erga4mpIyDggoMYhYr6aCUR62bFEieuWm5YgTswfxSl_F2cvT2jqmPnO4DVeD0bd67-aMvTyE8pGmA-yiCLSnFim8ck8RDCbN2zpfxl95h8slSNyNj_3FBn-XTcx5AAKK6QJatAF88qVnSqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فینال جام‌جهانی ۲۰۲۶ فوتبال
🇦🇷
آرژانتین
🆚
اسپانیا
🇪🇸
امشب ساعت 22:30
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68547" target="_blank">📅 19:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68546">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/798b52eeca.mp4?token=aDCP6-4rUKXwrRnAgTAvGWpiAausihS9AY_-YJ1YwBWtaV7BmTPZgW-qOLwmeT4LIfSc4kGw4CaTLaXMSM1JUejo_n4bEGYQvuvz_GHIchns8gh0rQEEE_CzjEJf4po62r2rlDh8Hrs_57lJL64AbHeQ7Y1A8KMO96X6OWO0CRnqBrKbHnEQ0kDVDy7PDLTssnbbTC6HO08Ac3i1UlY8a3A72X6GYzOvU7BfVONrSKAxZ3hKi5srzPBT3GoOu7CuldjmzWieUk76v1golPG3Zq3Sh_H6tS3_k9qWWIEvy9w3aJe7tLGKD0c1GoAk5tDNS44Wvv8nUKkUMIrHT8cGxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/798b52eeca.mp4?token=aDCP6-4rUKXwrRnAgTAvGWpiAausihS9AY_-YJ1YwBWtaV7BmTPZgW-qOLwmeT4LIfSc4kGw4CaTLaXMSM1JUejo_n4bEGYQvuvz_GHIchns8gh0rQEEE_CzjEJf4po62r2rlDh8Hrs_57lJL64AbHeQ7Y1A8KMO96X6OWO0CRnqBrKbHnEQ0kDVDy7PDLTssnbbTC6HO08Ac3i1UlY8a3A72X6GYzOvU7BfVONrSKAxZ3hKi5srzPBT3GoOu7CuldjmzWieUk76v1golPG3Zq3Sh_H6tS3_k9qWWIEvy9w3aJe7tLGKD0c1GoAk5tDNS44Wvv8nUKkUMIrHT8cGxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هدف قرار‌گرفتن یک نیروگاه برق در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68546" target="_blank">📅 18:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68545">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر دفاع اسرائیل:
«ما اعلام کرده‌ایم که اگر ایران جرات کند به اسرائیل حمله موشکی کند، ما با یک حمله قدرتمند، بدون هیچ قید و شرطی، پاسخ خواهیم داد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68545" target="_blank">📅 18:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68544">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
جمعه و دوشنبه‌ها، شانس بردتان را دو برابر کنید
100% بانس میکس ورزشی تا سقف 30 میلیون ریال
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68544" target="_blank">📅 18:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68543">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkkThs2KygTF6VDJx5LcAyx28IQ9Qh33yWHn4F7vBrSH_E5Bglgo_ai4hMaL3a33n3MOMBc-iYvqpj0lK74-uMv5wZ3XjOMuXYW3mVIfFYrQ5zNNm_1UVg-8vUXNIPyOYbXF55JFkhZMRTgEyU7QaFSXAaLwpdbdxtlLKqeQbUHK-RHs0QnLiyzBIEFcByZDIZQQ0Hxn9Q2U2cq5jrBXdiADypfZ9iv3kNDHLLdaD6FgRLxyqKOnzSlouzm0pOncaWdi017SBFmrA44vOshFJkn9yvWl-l4NAVL0eO8x8eAqWw5Mvl5G-duqEOO1XIxuSgXZq5X1czBrhPTV-ExcYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال جام‌ جهانی 2026
⚽️
اسپانیا
🇪🇸
-
🇦🇷
آرژانتین
⏰
شروع بازی ساعت 22:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68543" target="_blank">📅 18:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68542">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6b1462.mp4?token=Lv3JJaEQgc79Sex2luXshv9Ubx0-2seMLRqcz1O5gpc9kvD3COEH62TPzfMpMsZaiDcDYnXMIpBcAgEufggcEKguL-sR0TLZJTPWS2WVslxxH4r-O6fVQU7O6zCGMI4JA39kbTCfGHcBiy88OnOpRBSgHuKcCk4OEjAtGpXHwUk0EJtjXbC1muxjiSPBNCi0gRs0-Brut2JQf_mfFPTEID3FUl7ZLZixJ1M2sot0oZfQMEhN6eGRo0C8UU9LYOMTHGl-u33p3jkQ6eJ9HLcKct-sHUnaxLkA5VtAxftA1tvkqpAEH1uxqJzTA6Xp0Pl0oQitjGMbA9wAT8T92f17Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6b1462.mp4?token=Lv3JJaEQgc79Sex2luXshv9Ubx0-2seMLRqcz1O5gpc9kvD3COEH62TPzfMpMsZaiDcDYnXMIpBcAgEufggcEKguL-sR0TLZJTPWS2WVslxxH4r-O6fVQU7O6zCGMI4JA39kbTCfGHcBiy88OnOpRBSgHuKcCk4OEjAtGpXHwUk0EJtjXbC1muxjiSPBNCi0gRs0-Brut2JQf_mfFPTEID3FUl7ZLZixJ1M2sot0oZfQMEhN6eGRo0C8UU9LYOMTHGl-u33p3jkQ6eJ9HLcKct-sHUnaxLkA5VtAxftA1tvkqpAEH1uxqJzTA6Xp0Pl0oQitjGMbA9wAT8T92f17Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در دزفول
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68542" target="_blank">📅 18:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68541">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c53fd88605.mp4?token=T_7a7rjRHICDlo34NclC9tFGBPfrSAWdcH9ttq2BsEsoHvWZi9SA5vrLyFnTiYcH_ypB2lbKkvExB63Jqt3y-gRiJub7fYdlIbs0d_AKzB3JAyYAEySpCDqvPZMCPME7pg93HH90VmfBDGfVDBTcFoXQzh-K-2AJjdHC3trKAaRr701ZDAtRXpK2-UUswNdtFBWLL0TVfUZG27e3OrzUELvnUDVMpQidqtykZ8T9b6AYJkaKiFdxH2hBod3sJVDpTRZ5POCOCCNBidqi_n5Nm8xK-JI5RwqeTrEDr-NfvdkEa7UjyIoH4NJlnzuZbrz8-5mnSpXyFRzcSCkZygCwprKoC6Nvd0RPO1wXgxA_RM-wGjcgjP4tObKEQwRWp1SpiG4iZ8Ki_a2LIZl3lK6vTZTdJDTrok3VRt5BhUWd-zW3evACMp16ebPxDVVUt9hpFVSwUtB-CCR9wWQ9b_4uE0Mmoa0NOvFhyeU3tAK73e0rGaMzyIPbIiqpeuoegwJ8Ge2P1tEy8lA1hSd497EsP17nRzuWTNCzkWb0qQg-aFY9fhjkCGto5OoLcqql15rd9YhrS-y657kP0xU9C9PqgIncbIPh26WahGVYCAUSP-l_JlDW78-av9bByvrdPD5OY0wXIP1pUO2-A9jcDyddiPxCV99pvthV9NtuREh8bk0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c53fd88605.mp4?token=T_7a7rjRHICDlo34NclC9tFGBPfrSAWdcH9ttq2BsEsoHvWZi9SA5vrLyFnTiYcH_ypB2lbKkvExB63Jqt3y-gRiJub7fYdlIbs0d_AKzB3JAyYAEySpCDqvPZMCPME7pg93HH90VmfBDGfVDBTcFoXQzh-K-2AJjdHC3trKAaRr701ZDAtRXpK2-UUswNdtFBWLL0TVfUZG27e3OrzUELvnUDVMpQidqtykZ8T9b6AYJkaKiFdxH2hBod3sJVDpTRZ5POCOCCNBidqi_n5Nm8xK-JI5RwqeTrEDr-NfvdkEa7UjyIoH4NJlnzuZbrz8-5mnSpXyFRzcSCkZygCwprKoC6Nvd0RPO1wXgxA_RM-wGjcgjP4tObKEQwRWp1SpiG4iZ8Ki_a2LIZl3lK6vTZTdJDTrok3VRt5BhUWd-zW3evACMp16ebPxDVVUt9hpFVSwUtB-CCR9wWQ9b_4uE0Mmoa0NOvFhyeU3tAK73e0rGaMzyIPbIiqpeuoegwJ8Ge2P1tEy8lA1hSd497EsP17nRzuWTNCzkWb0qQg-aFY9fhjkCGto5OoLcqql15rd9YhrS-y657kP0xU9C9PqgIncbIPh26WahGVYCAUSP-l_JlDW78-av9bByvrdPD5OY0wXIP1pUO2-A9jcDyddiPxCV99pvthV9NtuREh8bk0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
صحبت‌های وایرال شده سرباز آمریکایی خطاب به مردم ایران :
اگه حمله زمینی شد بهتره فاصله بگیرید از نیروهای آمریکایی
نه اینکه بیان شمارو اذیت کنن، چون ارتش آمریکا خیلی مواظبه از سپاه که بعضیاشون لباس نظامی نمیپوشن
سپاه میخواد با اینکار به نظر برسه که مردم ایران علیه ارتش آمریکا هستن
سپاه اصلا توانایی نداره علیه ارتش آمریکا بجنگه
پس اینا می‌خوان پناه بشن بین مردم و حمله کنن چون اصلا نمیتونن رودر رو پیروز بشن
خداوند ارتش ایالات متحده و مردم ایران را حفظ کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68541" target="_blank">📅 18:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68540">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6029372426.mp4?token=a_T54Lk2j9b3Z-KZEgVKjXVxIcqejnOvga9qAKpLE6aZAAjg_bvBcsmSuRFZLINHGqdmgmoP9Fchowhu5mYWDgYwRbiWObnaKIbWAH7a3wASvSpK6hipVo5vmnqenL6Z21Gzlthiy8Abfx2AU3HqlQl2l9jMHQCAhxJAnkyLAsQn3xG3Ff_-jrCwAhZFvsbH9NTyoPalKysJFmfSjJrNy_2gfFB5m-28PXmvj8AWExTV6zDYY9sRmZgcRF2Qt6b7FpHhQryyG3h05Wg1p2yMRxV540WCKu8JSnRjBEwKkL29Qp9Vl4bJtdn9L0vI4hUPujPZHs01WTfzLVYcC_PRUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6029372426.mp4?token=a_T54Lk2j9b3Z-KZEgVKjXVxIcqejnOvga9qAKpLE6aZAAjg_bvBcsmSuRFZLINHGqdmgmoP9Fchowhu5mYWDgYwRbiWObnaKIbWAH7a3wASvSpK6hipVo5vmnqenL6Z21Gzlthiy8Abfx2AU3HqlQl2l9jMHQCAhxJAnkyLAsQn3xG3Ff_-jrCwAhZFvsbH9NTyoPalKysJFmfSjJrNy_2gfFB5m-28PXmvj8AWExTV6zDYY9sRmZgcRF2Qt6b7FpHhQryyG3h05Wg1p2yMRxV540WCKu8JSnRjBEwKkL29Qp9Vl4bJtdn9L0vI4hUPujPZHs01WTfzLVYcC_PRUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این مجری که اخیرا زیاد در صداوسیما حضور داره گویا اهل کشمیر هندوستان هست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68540" target="_blank">📅 17:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68539">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCIF-HyGoYZTL5eZvcfuUW7kgUkh1lEou22awQ_nkAj_THz-ceGjQx7REAZ5pcOJWvsMRc3JKRSXhayRJTRHS6CSXJC29Z-lIK0t85JOlAXeUYH5WnZ-miNK8klqhz0d7yw-jxUkWSvUODjr-3WMTuE43kt8LzhynJ0N1fHCSyN-XevtizdXgYrYs2HDuvSf4YBhE5nLdRDHsrNOn-SZ484Ak98aazhWFlaMWzvhWMtWiaHDhfzsj6ohOwQujBVRVqHGU3AtOxxEiiJtUVRdlD7w53FAkAAhZTd_5OoaNOJRA5EPBRhcPBxNIpTMnJ_Lt5NONzjrWKMOTwxnTjlHHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان انرژی اتمی جمهوری اسلامی:جت های آمریکا صبح امروز با شلیک چند موشک به سایت نیروگاه هسته ای درحال ساخت دارخوین در خوزستان حمله کردند.
ما حمله آمریکا به تاسیسات هسته‌ای دارخوین در خوزستان را که هنوز در حال ساخت است، محکوم می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68539" target="_blank">📅 17:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68538">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4472fedbde.mp4?token=dCGzH1B4QkrJnYEsaxwlsLUrSAXjnf_jrEjrfztGNvdvPfxU5SxyLq5ZTN4S5cxkMOMhcGbWgXBffAOxZ7XD_7s-dIAWiEtg4xG1vopygSaVO_oDncJq20S8TPCogxE9RZk507lWJlxO-VHwF5tG9icq3lFWuwYdgfNCyVrhjHwJ5m_Gs7XcitCsH8Y6l2xxUAwd_gm7utoSynC4_uAwWLasOVMQoSfLhbE8WXcElwpIXXj7h1JZoQPwWCLi5QY82oJImlY-z_dDJLqq9CphxNm63KRSPYYvyWii67kjXlk83Uu9lQ6KbdglObGWk4VcqufSMRIhyGHTlWkP9GVF9QOf8YKNj6WtPkApBDMH2QC-7D8zSotv_USj2WyrNh4kFqGNWN_KwQYAGA6YZfp2-1_IRk14yodkqAyzDgleTr5Vy2lU3egaLxreXtFaFysaE_K_IqqHbXQnZU3qdSzJOpODhfXUlQ8vmNcIH41RjlDMaw5l3JMO5K3Rq5FV9cK-qBKfteluym1115_wHh_NHo9zgYmaw3JXBoBvMDWNCYtitSvzitZt7_ARM9vCRV4ELLpKM06no8yEHBUjRXqRFq_NOs4E6AcMZXe25fPBPGQZvHkf4ZezBOm_tRyI1OZYWKBIjIO9W8W4uaKmt__ez6DfCx8ebopqRjyF-KyGmPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4472fedbde.mp4?token=dCGzH1B4QkrJnYEsaxwlsLUrSAXjnf_jrEjrfztGNvdvPfxU5SxyLq5ZTN4S5cxkMOMhcGbWgXBffAOxZ7XD_7s-dIAWiEtg4xG1vopygSaVO_oDncJq20S8TPCogxE9RZk507lWJlxO-VHwF5tG9icq3lFWuwYdgfNCyVrhjHwJ5m_Gs7XcitCsH8Y6l2xxUAwd_gm7utoSynC4_uAwWLasOVMQoSfLhbE8WXcElwpIXXj7h1JZoQPwWCLi5QY82oJImlY-z_dDJLqq9CphxNm63KRSPYYvyWii67kjXlk83Uu9lQ6KbdglObGWk4VcqufSMRIhyGHTlWkP9GVF9QOf8YKNj6WtPkApBDMH2QC-7D8zSotv_USj2WyrNh4kFqGNWN_KwQYAGA6YZfp2-1_IRk14yodkqAyzDgleTr5Vy2lU3egaLxreXtFaFysaE_K_IqqHbXQnZU3qdSzJOpODhfXUlQ8vmNcIH41RjlDMaw5l3JMO5K3Rq5FV9cK-qBKfteluym1115_wHh_NHo9zgYmaw3JXBoBvMDWNCYtitSvzitZt7_ARM9vCRV4ELLpKM06no8yEHBUjRXqRFq_NOs4E6AcMZXe25fPBPGQZvHkf4ZezBOm_tRyI1OZYWKBIjIO9W8W4uaKmt__ez6DfCx8ebopqRjyF-KyGmPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش امیر رولکس به حواشی ساعتش در جام‌جهانی:
به جا اینکه بگم فوتبال با ما سر ناسازگاری داره از کلمه خدا«داره مارو میکنه» استفاده کردم.
چهل چهلو پنج ساله ساعتمو دست راستم میبندم.
اگه یه سرمربی ساعت می بنده و لباس خوب می پوشه که اشکالی نداره.
اگر من زنجیر طلا مینداختم  و یقه پیراهنم رو باز میزاشتم آدم خوبی بودم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68538" target="_blank">📅 16:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68537">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSsBCVPRuJapN6HZm4YSZJvmqekUsViBKdZvVhkSGHY97EvFGBOSD5RSEpdDOVix89CCZPn_hL89DT6HMNRAiMU1U6EQPKnNd53V5bqdVl2D8ZXJ8FobHPGqgR8yYxN21bC7V2xexsU2P9hGADosdcKHfK76rShX7ZpmlxUY_glHvqY1K_2BT69q-4VK4tddWHNEivtpa0IwxzqkWAWzovRDsFVAgsCm2FxC0Dq59_nt7uWbMRlYNZfdf0fuN7efaH-uMUqfaBL38h5DyRCnrx5C41qoOV_spwsbhXayVMSeZ_WjNM97JaJgCKvAzc2zBuawmCE2WfUjwNscDWT0lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پرزیدنت ترامپ:
جمهوری‌خواهان باید ایران را به لایحه تحریم‌های روسیه اضافه کنند. این همان کاری بود که لیندزی می‌خواست انجام دهد و قرار بود محقق شود. مهم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68537" target="_blank">📅 16:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68536">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeZQsFi1nNXCdPgkaEXxheJYYvKz59T9X2o90m1cHTLvhacYto9DDX_UtBZ8bnpk7uU1jpMP_8qFzfNjrF20laIAJ1QozNtqGFdBf3mZp3HptmgLUhpqtZTZuEhxBJea5vbVMp63z_K-kw7U6Ok8FpbGVwACe_I0-04DQbtXA5tjdtNg_CANaWr4rDgeURHJa6jCs1gSKbjhCw3OpArE155P2ieocz7vGknpOEYusJQ26g0YEuu1AHd0fGn8TeaVYC6sIqdZvTcr_D8Lzo25n1Hlk29uf0Q8xdmJoFqY-xFAO-cBLGnRW0xHcsfoWog9UiEd0mlTF7iSzhDYYHlT3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">14 زندانی تو زندان دستگرد اصفهان برای اجرای حکم اعدام به سلول انفرادی منتقل شدن؛ این 12 نفر از متهمای پرونده میدان علیخانی هستن. +پرونده میدان علیخانی مربوط به  اعتراضات 18 دی 1404 تو اصفهانه؛ اون روز بین معترضا و نیروهای حکومتی درگیری شد و جمهوری اسلامی مدعی…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68536" target="_blank">📅 15:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68535">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇷
عراقچی:
بمباران بیت از طریق حفره امنیتی صورت گرفته و این حفره امنیتی همچنان وجود دارد
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68535" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68533">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3548648f57.mp4?token=EngxXc3kUSX1LTEMlUTksaOcYtwSgR2808WXiCIDYXwdZggdLPH5KFdKgpDDW8OCFR01I6ExCEPvUewQtRdzv296vbgKVJMeWDzm5nU7zIuefNVMq6kMNXV9mpPnui9MWX8u0tiUKe1lvYb5LLowGFvoZDauTxleldf8LOUkO6UWAeftS9a8qpWm-5EEyRp5lMPAaddkoeQqx-VZawR7BNHkL9GgL6v1JIfwgH93PXSJwq5IIoirC4HYsg3NOt-G6XVicKnsWtbfK6c16yOWQPCnaXQVc9f7qHbWqs0ss6btwmgzgCQlasGfwUzrE67P8qchS-VUmo2qxZSNSkvMfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3548648f57.mp4?token=EngxXc3kUSX1LTEMlUTksaOcYtwSgR2808WXiCIDYXwdZggdLPH5KFdKgpDDW8OCFR01I6ExCEPvUewQtRdzv296vbgKVJMeWDzm5nU7zIuefNVMq6kMNXV9mpPnui9MWX8u0tiUKe1lvYb5LLowGFvoZDauTxleldf8LOUkO6UWAeftS9a8qpWm-5EEyRp5lMPAaddkoeQqx-VZawR7BNHkL9GgL6v1JIfwgH93PXSJwq5IIoirC4HYsg3NOt-G6XVicKnsWtbfK6c16yOWQPCnaXQVc9f7qHbWqs0ss6btwmgzgCQlasGfwUzrE67P8qchS-VUmo2qxZSNSkvMfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
وضعیت ایستگاه مترو در کیف بعد از حملات سنگین روسیه به پایتخت اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68533" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68532">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
جمعه و دوشنبه‌ها، شانس بردتان را دو برابر کنید
100% بانس میکس ورزشی تا سقف 30 میلیون ریال
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68532" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68531">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAUHcRK_Ks6RlmKyWcVrFTGdq79PSTB9NXiKwxi2cMtucGmzh9udlWq_iic-O5bVjmZoI8S3f3JzPbE4LBozAvadXCd2CnEZ436mltVt61YjC6fkd2kO18HMRh3BgGtWFEaIo8_PTT-Vk51V4GuF8HjwxDiaooIqwpK7fTNsZKZihA__nFldcZKgLsp2bYFqQWaABBs2w17Vuinuvzb7QZJp7LCgDYwlIM9DlvLqLGEAFieEVzyP4913MbXM477i-6c-aTncvV9-rhM6X24F76URUJED1j893EwwlNszLgXkG83UxCmaPzKoXDzqMlJ7CfQcy63n8ntBDsztidfdKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال جام‌ جهانی 2026
⚽️
اسپانیا
🇪🇸
-
🇦🇷
آرژانتین
⏰
شروع بازی ساعت 22:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68531" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68530">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/326d421018.mp4?token=UWJo-_12FH1ig4A4jaW-jPlQsXS4Kw6t5CaV2X1npFZVO1xx-fXJ3apQ7U0xmKAsCGfn-zraFhZEndk5BdRgqd5_wo2y-NBxLGnrq0_ENvSIPCR9INhVpQ3v1C414rzgiP75bRBqBLLd12nGG8LFQwGdBlWF7UYF5zt67rQt4exY8v3vGMwPxhryauE_tHcRVgRipEXOnEj-T_DX6pQd7ngs4DVMOmxRL5BYL0uef06EfYwRzZlUkIw_CoMmJBO_5Q7_bQzcU7s24nSL4gpiktIbQYyqpWfLwJQwCqlEhpSRB0mJFp2qWYhga9w-k8pX6wwG9Aw7KPfJrpSE43j8lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/326d421018.mp4?token=UWJo-_12FH1ig4A4jaW-jPlQsXS4Kw6t5CaV2X1npFZVO1xx-fXJ3apQ7U0xmKAsCGfn-zraFhZEndk5BdRgqd5_wo2y-NBxLGnrq0_ENvSIPCR9INhVpQ3v1C414rzgiP75bRBqBLLd12nGG8LFQwGdBlWF7UYF5zt67rQt4exY8v3vGMwPxhryauE_tHcRVgRipEXOnEj-T_DX6pQd7ngs4DVMOmxRL5BYL0uef06EfYwRzZlUkIw_CoMmJBO_5Q7_bQzcU7s24nSL4gpiktIbQYyqpWfLwJQwCqlEhpSRB0mJFp2qWYhga9w-k8pX6wwG9Aw7KPfJrpSE43j8lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
نیروهای امنیتی سوریه یک محموله تسلیحاتی دیگر ج.ا به حزب‌الله را توقیف کردند، این یک کامیون خیار بود که زیر آن ده‌ها موشک کورنت ضد تانک قرار داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68530" target="_blank">📅 14:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68529">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
ملی‌گرایی از نگاه خمینی، بنیان‌گذار انقلاب اسلامی:</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68529" target="_blank">📅 14:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68528">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93f8a1edf1.mp4?token=PwlNGgtCKImAniz__rsLLwx31T5QP27fxS-iE0shdhPfRb56fihvIb8AOl6K1AuC_AiRgrnw4uCL6fvVTPSTdN_f1bnkSIR2kfI1hhiAmXi3eQUGu8XhXQr0zWWRVoJFDHHII5XUVDbxjV_QBHJCun5iC_G_aMXw72P84TDlf01hqFiC3gu4XS16qYuD92B4LKW55xofyV-CrbrZrAehjSLKUTKlOtpDfHqggM1GsD9ciFWU2VNuDSh5MIk4wMbKiLkReMjvuVU67Oo5jZD4DaA02N0pcEhLNI8Lpait4W5m1przPMtYRlNqVRYfXk7iFiNK1bDuDX7RmzeQELHnkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93f8a1edf1.mp4?token=PwlNGgtCKImAniz__rsLLwx31T5QP27fxS-iE0shdhPfRb56fihvIb8AOl6K1AuC_AiRgrnw4uCL6fvVTPSTdN_f1bnkSIR2kfI1hhiAmXi3eQUGu8XhXQr0zWWRVoJFDHHII5XUVDbxjV_QBHJCun5iC_G_aMXw72P84TDlf01hqFiC3gu4XS16qYuD92B4LKW55xofyV-CrbrZrAehjSLKUTKlOtpDfHqggM1GsD9ciFWU2VNuDSh5MIk4wMbKiLkReMjvuVU67Oo5jZD4DaA02N0pcEhLNI8Lpait4W5m1przPMtYRlNqVRYfXk7iFiNK1bDuDX7RmzeQELHnkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
آتش‌بس با نظر آقا مجتبی بود؟
🎙
پاسخ
عراقچی:
این چایی برا خوردنه یا دکور صحنس؟
☕
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68528" target="_blank">📅 13:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68527">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه پاسداران:
ساعاتی قبل، دو کشتی متخلف در مسیر ناایمن تنگه هرمز دچار حادثه و دو کشتی دیگر از ادامه مسیر ناایمن منصرف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68527" target="_blank">📅 13:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68526">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6daaa9359.mp4?token=RBXbX27f2-Qq4lo8ZQhc9LJgx2kSCxgaYcBYmUAqPeDa6FIfcjfDKoEquDQ54uKexMsTfDZoj627u0eTHUmNEN4K5tATBcZ3jASVu8b_7QjkX4C5wK-oeHZLcup7Iz2dhBoWhZzx9i60LI026MqvkoLSqkEctA22PDWBislTrBmoVHpVygPuortZ-tSFrQYxileeiS7ovu9vZ8muswLOd75cM1Y7EwPcoVeT27Fmh6O_TZWolkRL8tGHbYIUd2cmHCVGg7bo5sbitjgFLfLTh4mET_GfMDjj-cKzWwSIB8wl2NjJt1gUQ0BWd0x-2HgU_9FTLtJAdwDlumF0izFp2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6daaa9359.mp4?token=RBXbX27f2-Qq4lo8ZQhc9LJgx2kSCxgaYcBYmUAqPeDa6FIfcjfDKoEquDQ54uKexMsTfDZoj627u0eTHUmNEN4K5tATBcZ3jASVu8b_7QjkX4C5wK-oeHZLcup7Iz2dhBoWhZzx9i60LI026MqvkoLSqkEctA22PDWBislTrBmoVHpVygPuortZ-tSFrQYxileeiS7ovu9vZ8muswLOd75cM1Y7EwPcoVeT27Fmh6O_TZWolkRL8tGHbYIUd2cmHCVGg7bo5sbitjgFLfLTh4mET_GfMDjj-cKzWwSIB8wl2NjJt1gUQ0BWd0x-2HgU_9FTLtJAdwDlumF0izFp2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تصاویری از انهدام یک پهپاد نظامی مدل MQ9 متعلق به ارتش آمریکا در عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68526" target="_blank">📅 13:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68525">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c817c7306c.mp4?token=s0STUnolCWRawKiFE3lUsnQBYFjZUVE86ryOZcWh1v0ESHmggIcvbqUAmhh6s1DJVY-wnp31fzjuS0H8WfoUAHNwRY99g0t7SNsbal9LDuAX5KTYD7I3C0xy6eLcS8zNDv29drICOnXo6vkefnJCoreXpHI-K-Lksm-RUwFVrF2hvkinKdFT_Y8Gc2AxnE7X2jKHskVVvtkulpqA-2sp2zgYD8pDn2LHFBPKkQJoqkZxBMk0WoUIfoCADFshHRoMfyfHy4aEe9Udj9AlUBZsfrDc5npekBeUa93vlu1nv1AW-w0yAxRXkRUiAKkcBx2OVeNy0NM2HRWVoLgLsEoEolvIYTf8das33ZtEKA8EhYZ--YuIJdejl5QgQFX0OnI3Y1tz6rCaJBUWfhELdaBLlRPKkefIED7ZZAeq5HigYSBX5RPbT9HWvldSTUOeM-S8kXXmTraSYcDRADilpNUA0BwHbYOifBQNI-lFb4vq51pv0gcWiL4G6UTaemT3DvBg-EHN1b6JbuM_ezVZmwMO1P7el0qZfbOd3ixxqNX7HqIru3PcpZPk69w9R5lKHxbEZ62cBfoXP1v3YudQ-Ze0QKt1pRB40D5wD-BEHKzs5yCuzWdDyPML6uZRdp8R2mnWRNKr8gLuVQONBPmp73nSgcPw5jpIZRwOa2qiIbsR6w8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c817c7306c.mp4?token=s0STUnolCWRawKiFE3lUsnQBYFjZUVE86ryOZcWh1v0ESHmggIcvbqUAmhh6s1DJVY-wnp31fzjuS0H8WfoUAHNwRY99g0t7SNsbal9LDuAX5KTYD7I3C0xy6eLcS8zNDv29drICOnXo6vkefnJCoreXpHI-K-Lksm-RUwFVrF2hvkinKdFT_Y8Gc2AxnE7X2jKHskVVvtkulpqA-2sp2zgYD8pDn2LHFBPKkQJoqkZxBMk0WoUIfoCADFshHRoMfyfHy4aEe9Udj9AlUBZsfrDc5npekBeUa93vlu1nv1AW-w0yAxRXkRUiAKkcBx2OVeNy0NM2HRWVoLgLsEoEolvIYTf8das33ZtEKA8EhYZ--YuIJdejl5QgQFX0OnI3Y1tz6rCaJBUWfhELdaBLlRPKkefIED7ZZAeq5HigYSBX5RPbT9HWvldSTUOeM-S8kXXmTraSYcDRADilpNUA0BwHbYOifBQNI-lFb4vq51pv0gcWiL4G6UTaemT3DvBg-EHN1b6JbuM_ezVZmwMO1P7el0qZfbOd3ixxqNX7HqIru3PcpZPk69w9R5lKHxbEZ62cBfoXP1v3YudQ-Ze0QKt1pRB40D5wD-BEHKzs5yCuzWdDyPML6uZRdp8R2mnWRNKr8gLuVQONBPmp73nSgcPw5jpIZRwOa2qiIbsR6w8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
🇮🇷
مصاحبه عراقچی با جواد موگویی؛
جواد موگویی: دست فرمان شما دوباره باعث جنگ شد.
عراقچی: دست فرمان من نبود.
عراقچی:اگه ده روز زودتر آتش‌بس رو انجام میدادیم لاریجانی رو داشتیم خطیب رو داشتیم عسلویه رو داشتیم فولاد مبارکه رو داشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68525" target="_blank">📅 12:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68524">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4be1f5800.mp4?token=mRsv8vfhS3zfv8hjQd-qIxa9orRniZoypoDzy9prhCRFJInxqrTW4xWDZfq_8B68VsBMqtbye0bubyejPfjMo-sdzrU3aWXJv-Il7QRmwpJ-cjcZooAzjALb5qnWUXjOfKT9-Ar1FLu4ejCYDOmyoGWs_o0OilRpnz3Dtr80RtBpWM2WQtgUi2GHVQG9krV_Mvx8VzAbg_8iHsiapQi84JAo_LOa9t9M-T1lTDkjSLWhXtdSIQ3VVV130osLTvbI9UUebvWRJinQOY452egsranXVnsFq6DV_qowgBP_axjB_oLVRb_IazyBGXKX5zy9Jnw5BxdhPSgI_ojfHXW4gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4be1f5800.mp4?token=mRsv8vfhS3zfv8hjQd-qIxa9orRniZoypoDzy9prhCRFJInxqrTW4xWDZfq_8B68VsBMqtbye0bubyejPfjMo-sdzrU3aWXJv-Il7QRmwpJ-cjcZooAzjALb5qnWUXjOfKT9-Ar1FLu4ejCYDOmyoGWs_o0OilRpnz3Dtr80RtBpWM2WQtgUi2GHVQG9krV_Mvx8VzAbg_8iHsiapQi84JAo_LOa9t9M-T1lTDkjSLWhXtdSIQ3VVV130osLTvbI9UUebvWRJinQOY452egsranXVnsFq6DV_qowgBP_axjB_oLVRb_IazyBGXKX5zy9Jnw5BxdhPSgI_ojfHXW4gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن سامانه‌های پدافندی بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68524" target="_blank">📅 12:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68523">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🇮🇷
فعال شدن آژیر خطر در بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68523" target="_blank">📅 11:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68522">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvgXMkDfpPf_ki7qj2LI9xqoYFdC7UJsByWhVGvT_Hwj0Cws9cOLFuAN8fwrJ2TPRqtSK6nTW8mdrYdid0YFmT3EJrMqXY4TvDoAy8EeFGUQL2JGwvLPwb7mUTby2PEKobyCGnLEzPLO6ztoULPlqYjCn2j3FWAneiVY1xym0w_o7pG8lLFS0THbToTULnPLkozvcUx6hobIK1CkCz1-86X9eboywIXpULiDLzUWlQbH8fqVT_zP4_oo06hO_j-3gyAEwIiOXCbT-BLBd_oLHp7TDuNnBpPHfl70MO46pCK0kSYrsBYNH8jzqLH731z44cbk0oX7WOTiZpMbEydyRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">14 زندانی تو زندان دستگرد اصفهان برای اجرای حکم اعدام به سلول انفرادی منتقل شدن؛
این 12 نفر از متهمای
پرونده میدان علیخانی
هستن.
+پرونده میدان علیخانی مربوط به
اعتراضات 18 دی 1404 تو اصفهانه؛ اون روز بین معترضا و نیروهای حکومتی درگیری شد و جمهوری اسلامی مدعی شد؛ چهار نفر از نیروهای بسیج و فراجا تو اون درگیری‌ها کشته شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68522" target="_blank">📅 11:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68521">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef80c8768.mp4?token=AsjhMFu-IlvppITciFPTuZw5Kp1lwYag5b3hyvT1MbgzxMxlsWOaUIHMhxAkKTi0GaB_UTe3jFpZba4pN89vcdjjcl4dLZQgJoB1Uay8ItpN0elovcW4ymB2zASBlaUxvovh7RetOXAHzS0Q5zzOqRCy3k1esHa7dXC9bpoCmMYptupKhxNBAhpIcowHrE1ATq_CL9sPbPwor2LTTLQ64HdiIIQ_wr25IxqosOboPzZd9kHqraj8tI0HLSKCN0z_e6u0aVXpw57gFS8v2FPhuBxBEnxrMFrG3oN8H275J2rgMBWG4MXvwwTQYEnamkMTMbuBn5Hs4kLUoKX94Wzphg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef80c8768.mp4?token=AsjhMFu-IlvppITciFPTuZw5Kp1lwYag5b3hyvT1MbgzxMxlsWOaUIHMhxAkKTi0GaB_UTe3jFpZba4pN89vcdjjcl4dLZQgJoB1Uay8ItpN0elovcW4ymB2zASBlaUxvovh7RetOXAHzS0Q5zzOqRCy3k1esHa7dXC9bpoCmMYptupKhxNBAhpIcowHrE1ATq_CL9sPbPwor2LTTLQ64HdiIIQ_wr25IxqosOboPzZd9kHqraj8tI0HLSKCN0z_e6u0aVXpw57gFS8v2FPhuBxBEnxrMFrG3oN8H275J2rgMBWG4MXvwwTQYEnamkMTMbuBn5Hs4kLUoKX94Wzphg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
در هشتمین شب متوالی حملات ایالات متحده، نیروهای CENTCOM با موفقیت به تأسیسات نظارت ساحلی و پدافند هوایی نظامی در ایران، قابلیت‌های دریایی و انبارهای موشک و پهپاد حمله کردند تا به تضعیف قابلیت‌های نظامی در ایران ادامه دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68521" target="_blank">📅 10:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68520">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‼️
جدیدا تو جشن های تعیین جنسیت دیگه خبری از ترکوندن بادکنک نیست
الان پدر بچه رو میکنن تو منجنیق پرتش میکنن تو بادکنک و آب
😳
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68520" target="_blank">📅 10:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68519">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0c1d5cc2.mp4?token=v8mHbsnA-lvrxFqMv2hBtG4nfMvl-RwcLz9pBgfv_gk5-rrfplGA78JLdHrsKXYedorjvOxj3ZTvb6UGKPmxkBw15I1JsvKZVSL4KoJRO-JMdvNUXb-ELd1AvzgQCSXz2DmlJcdQVN_zPju2FtQfp0dkzmJQ4iaOsATrkgOFbH88EingxtVsIaykme6kBdRqxAfwsztYReh5RcUcUC_Roox1zzYJ3Mk4SnTqum3fHdz3RtT1Q18LOeOvEwwjQWYUM43M8Gx3p4ACshnHsg-90csV10zIgQ7Q4OFz4jyl2PIbvLyblZaAPm0-KbpAf-vxqAaf9cRzi9kY-AJwSL-nzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0c1d5cc2.mp4?token=v8mHbsnA-lvrxFqMv2hBtG4nfMvl-RwcLz9pBgfv_gk5-rrfplGA78JLdHrsKXYedorjvOxj3ZTvb6UGKPmxkBw15I1JsvKZVSL4KoJRO-JMdvNUXb-ELd1AvzgQCSXz2DmlJcdQVN_zPju2FtQfp0dkzmJQ4iaOsATrkgOFbH88EingxtVsIaykme6kBdRqxAfwsztYReh5RcUcUC_Roox1zzYJ3Mk4SnTqum3fHdz3RtT1Q18LOeOvEwwjQWYUM43M8Gx3p4ACshnHsg-90csV10zIgQ7Q4OFz4jyl2PIbvLyblZaAPm0-KbpAf-vxqAaf9cRzi9kY-AJwSL-nzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇱🇧
پس از ترور خامنه‌ای، یک گروه از حزب‌الله تلاش کرد تا پسر نخست‌وزیر اسرائیل، بنیامین نتانیاهو، به نام یایر نتانیاهو، را در خانه‌اش در میامی ترور کند.
⏺
سازمان امنیت اسرائیل، شین‌بت، این توطئه را در آخرین لحظه خنثی کرد، زمانی که این گروه از حزب‌الله به طبقه زیر آپارتمان او رسیده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68519" target="_blank">📅 09:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68518">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68518" target="_blank">📅 03:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68517">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=RswTzT6GSFKXSk8GaLlJRUVZapgie_bYhScbGxQvv8JXhWz9olRMO6Yi5uw-7Ydk1xABOUG5yBJbglKIcN2RoIYJuPl6BWICNg5zLDhgpayboR5jzw1sSHNRyW9C9jXH-dOZwC2HjQO_vIx1haNDucCKEyhO42YZI7K_lzP7MuYKPZi6Z6Ehkvw1mbEQ4DCyVWHoYEGzP38BR9pLGBtvP4q1icC53wkMS3yrCL_ro2DNH_01dm2HljerFmjAPit7pc3Qazxi466cjDvejzV0vAIN2miJ_TT5Xpno8nxZNHbYsnXU2bVAdvX_YMIfN9JG8RNdU2n4Ng2Y8dB-TahFgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=RswTzT6GSFKXSk8GaLlJRUVZapgie_bYhScbGxQvv8JXhWz9olRMO6Yi5uw-7Ydk1xABOUG5yBJbglKIcN2RoIYJuPl6BWICNg5zLDhgpayboR5jzw1sSHNRyW9C9jXH-dOZwC2HjQO_vIx1haNDucCKEyhO42YZI7K_lzP7MuYKPZi6Z6Ehkvw1mbEQ4DCyVWHoYEGzP38BR9pLGBtvP4q1icC53wkMS3yrCL_ro2DNH_01dm2HljerFmjAPit7pc3Qazxi466cjDvejzV0vAIN2miJ_TT5Xpno8nxZNHbYsnXU2bVAdvX_YMIfN9JG8RNdU2n4Ng2Y8dB-TahFgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68517" target="_blank">📅 03:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68515">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NmKjOyRsVXWE9sqfBguG8MipPDkA6lNg36xNvJil4Ck1Gf2ck77rNaLii3YHcDLaddEmET6F2a3Onc7L0S7E2n2l7DrcCBMiqz9tm9T059gbCYFJ8ZjSmp-AKQBqQ0J0ERxdf81eoVMiZTe_F1oiOwa75aqZ7qL2e41O5uDcBFYyKhBfjC2OFy05koLKEGMrIc4wRaForvF2jL70EZLSx0qocNrHeu3iHhsE5G75yoEKXmz45QYadJVDp5jZhxmfd71gjJ2snK9wJ5Gbnrs5I_0_HDUm8_T23ZQU38uw3u22QySzelLrj3lS8xLUiSqFIF3MuTk_Bw6BIsOe1rrKBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jgAkhbZqAxGctXo0lnRFD9-YX5LQuo2mWZLlXNO58d8SW4LYub7eSCZuJ8hKJDQDufuHvwNUxjLsb2ABQ1abofRqY_K_HBi84du6hRJvTkdA2a3WDQ92kCV4SSu53RVWbPti6sc-r_sThT5FPWle6mZBDtDj0Vpd-EIg1H-jdVm6wUkckL-sxJWYq0Uh42U-jMBeeiw54ESouKCORf5vq4HQkWEtAOuBieGCz_DHnTOm-rOqd7PO4UX8N7QEwwoz32w93ySuvYQDTs8EMI_-0qBhaetUA5p7H9UqcocH9ki9G6k7aCw-RaR8POFvkAE0k_MvN97TFKtMTsO2XxYTWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
حملات موشکی روسیه به کیف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68515" target="_blank">📅 03:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68514">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🏆
رده‌بندی جام‌جهانی فوتبال|انگلیس برنده جدال بازندگان در یک رالی تماشایی گلزنی؛ دشان و تیمش در روز رکوردشکنی امباپه و اولیسه با مقام چهارم با جام ۲۶‌ام وداع کردند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
😃
-
😀
فرانسه
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68514" target="_blank">📅 02:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68513">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
تسنیم:
حملات نظامی دشمن آمریکایی به حوالی حاجی آباد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68513" target="_blank">📅 02:35 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
