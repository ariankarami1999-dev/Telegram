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
<img src="https://cdn5.telesco.pe/file/d8FMdeVjuv8LA-TrPQ7By5mi-gnmKO12JacByxiSGIREAuZl3OlK04IMWDx-HoZEd_-0vE5wW5hETgz9GIji41EZDVnR2FVOrPZy70IvNbEFVwTDQPfO7CkY-LkbehH9SwEv7ti9RPtVx-LDdO_0dWWP9bQIbfbUDtCJ-lqmpyiWDkYGMbZ52WPMKlfYtNGn3XMYt-YzZ6d2uXrERmdikaaM_knNDpjcCXfibgqACK9XL9tEgOqZLE0yViOirAroPwjhxQtu2O-cU2KtXn2MPq5ATvL8R4pLTCFW4dLLwUToIgWV-FBKzIqmrkat64yHmpqHnpR8H5U96IleP3o4Sg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 688K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 22:44:31</div>
<hr>

<div class="tg-post" id="msg-96120">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">عراق اخراجی داااددددد</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/Futball180TV/96120" target="_blank">📅 22:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96119">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گل اول فرانسه به نروژ توسط دمبله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/Futball180TV/96119" target="_blank">📅 22:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96118">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dca6328400.mp4?token=myewQoUEoH8AVyfTnrcbUtUsJyiSnwHRetTC6vqQSXGJWBjLRMN7096PH5HBE-tZQxaLCqYIzrlb-Yb49QpIMMg6Qb-10QiYKyze0abD-WrFO6L0bNWQHBATEFwujqQQef6d9wezYKgGPuXjdaHscS-EmZ6bCKXWC0xR7iqcT12lKnWvd-qa68R6ZBWd6_hwESDGgKbBss4-vn4kociKu2oLRWmcIMyPGMczEt1Y99-V2Q7I0QdmIlxSCtjsAhlSHqnAWRGhDu4nm7nLAubfacS3oG5Yne11ROmLXkZJTt1YixFWwjy0IGZD7u7Ib10PU29j3DOp4u6VBlLzJRvkbawdVkKPA9I77XGjnd2AnIJhXtWDIy37061lpx-SxMyixVFiWGFxjW-s0FVas886RZFoaUUWb36jzhoaVG4sbecX6GucY-sW5MWXECCp8kdtYnsJH49VZGLnf6NADnkMfly8aO1iFOoY22YJsxmeICTpq-5nGDZVezoiKc9EiWiCqSYINE4LlzxcMjaSdVZ2haHES9HRbOx7lb0_xsg0U8BP0S5S3YkUpI8wkb5BWKpzRaB8td0xt_ZoELudmlGSeKr6OeOlkivRPcYKXPNGj2sJx5fK8GUKOjtsDJtfoUq8i3xinRkduM5R-_K4WVqvnrG_n8IE6ycj32kxno9C47c" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dca6328400.mp4?token=myewQoUEoH8AVyfTnrcbUtUsJyiSnwHRetTC6vqQSXGJWBjLRMN7096PH5HBE-tZQxaLCqYIzrlb-Yb49QpIMMg6Qb-10QiYKyze0abD-WrFO6L0bNWQHBATEFwujqQQef6d9wezYKgGPuXjdaHscS-EmZ6bCKXWC0xR7iqcT12lKnWvd-qa68R6ZBWd6_hwESDGgKbBss4-vn4kociKu2oLRWmcIMyPGMczEt1Y99-V2Q7I0QdmIlxSCtjsAhlSHqnAWRGhDu4nm7nLAubfacS3oG5Yne11ROmLXkZJTt1YixFWwjy0IGZD7u7Ib10PU29j3DOp4u6VBlLzJRvkbawdVkKPA9I77XGjnd2AnIJhXtWDIy37061lpx-SxMyixVFiWGFxjW-s0FVas886RZFoaUUWb36jzhoaVG4sbecX6GucY-sW5MWXECCp8kdtYnsJH49VZGLnf6NADnkMfly8aO1iFOoY22YJsxmeICTpq-5nGDZVezoiKc9EiWiCqSYINE4LlzxcMjaSdVZ2haHES9HRbOx7lb0_xsg0U8BP0S5S3YkUpI8wkb5BWKpzRaB8td0xt_ZoELudmlGSeKr6OeOlkivRPcYKXPNGj2sJx5fK8GUKOjtsDJtfoUq8i3xinRkduM5R-_K4WVqvnrG_n8IE6ycj32kxno9C47c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول سنگال به عراق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/Futball180TV/96118" target="_blank">📅 22:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96117">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فرانسه اولی رو زدددد دمبله</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/Futball180TV/96117" target="_blank">📅 22:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96116">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گللللللللللللل اول سنگااال زد به عراق</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/96116" target="_blank">📅 22:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96115">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شروع بازی ها
نروژ و فرانسه
سنگال و عراق</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/Futball180TV/96115" target="_blank">📅 22:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96114">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqJASjRc0G_7wy6F1LfRGXBcJxCv019XlvcDk7L-HZMsf1qlGU43u2Awsnr-hAXOND_IRQ3esVj-Rm5CxDoin3D84J_y9McVRSzJkx7RzpmZu-ZwirF-Z5enWGenrNHoBHdjvcW_-8iq9_WzEO9z0oBusYeLKSfiyRe6jhv_B8bOgy34hIdreY5Fs28o0V16Zqp_mD2LSRq9R9xlRyo-t9l6jVFwMAcMjid3B2eYm6zMJlqskKhP-Upfo5iB4hLqo17W2nMcmajXXTI5YpSBziadbVcA2XYBSAGDgQZxUav_QWebKtbIXio27M-ClXiGr3XweIUwNiXlyPgSyHBZ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کن 15 دقیقه دیگه از این قاب جذاب سوئیچ‌ کنی رو اون قاب زشت و تکراری جام جهانی.
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/Futball180TV/96114" target="_blank">📅 22:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96113">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/814f149c24.mp4?token=dn08eCI7db2S7-mapth74SVlOAwAJpxoqqhbVep0izAGg6oNKjewc9IBIN3T2jEFKcb8aJ5RmdFXJrJOU6Fvs5uucCrqWFi52IkuhvCG6JZd0qA2SVlVPYVVqdcVUIwuMmKe5f6rf9oOCnT_sm1JckcoGkWFLbyZ_ocrgCzP_55_iH9uXkU84I57Bg_oqYTgP0LJ0YkFgAKjhBWHFWjRTqs-Jg2itrZvAV5v57CLb-yNZhlb3URtJA2afjZc0v47rs019yeUuHNk3j41RtUXAs-3npP7PU_iLIjqThH2UsRQyfm3eG-B4cWL24sp-WfvGLDMp4tygIiKEHjj53RcLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/814f149c24.mp4?token=dn08eCI7db2S7-mapth74SVlOAwAJpxoqqhbVep0izAGg6oNKjewc9IBIN3T2jEFKcb8aJ5RmdFXJrJOU6Fvs5uucCrqWFi52IkuhvCG6JZd0qA2SVlVPYVVqdcVUIwuMmKe5f6rf9oOCnT_sm1JckcoGkWFLbyZ_ocrgCzP_55_iH9uXkU84I57Bg_oqYTgP0LJ0YkFgAKjhBWHFWjRTqs-Jg2itrZvAV5v57CLb-yNZhlb3URtJA2afjZc0v47rs019yeUuHNk3j41RtUXAs-3npP7PU_iLIjqThH2UsRQyfm3eG-B4cWL24sp-WfvGLDMp4tygIiKEHjj53RcLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤩
گل اول چادرملو به پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/96113" target="_blank">📅 21:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96112">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b610b221.mp4?token=W9AjyscdJryL-iiJTsSQBXpoi3bPhEZZR5FqWbES3wFBl8AjvWVmdGynQL7WC-0m1MtliWSxx9M4ROnLM2VfVlxd8ujngbWAPBQNGwQqrNe3-5w1XVD-LsSxlRJOpXZgmUS2YUfVMaHzUcReQrbQFueSCphm5nHPKT2e2RVnP75a-VQJqtUCIOftp9hWBAz0xSbuRJE-DC2ZcXc7pGJ93kaXJUcyBCkSbW1A9E68JqZALqb4C9LyiAMfmEeBo0qytMbBdowuqcM7qGN7NZ_JnqinLMgy1gUK83x8uLvT1qVDYt28bJ30CR5oJcLu8BSlfb7zyO1K_O8kWKexMUvl0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b610b221.mp4?token=W9AjyscdJryL-iiJTsSQBXpoi3bPhEZZR5FqWbES3wFBl8AjvWVmdGynQL7WC-0m1MtliWSxx9M4ROnLM2VfVlxd8ujngbWAPBQNGwQqrNe3-5w1XVD-LsSxlRJOpXZgmUS2YUfVMaHzUcReQrbQFueSCphm5nHPKT2e2RVnP75a-VQJqtUCIOftp9hWBAz0xSbuRJE-DC2ZcXc7pGJ93kaXJUcyBCkSbW1A9E68JqZALqb4C9LyiAMfmEeBo0qytMbBdowuqcM7qGN7NZ_JnqinLMgy1gUK83x8uLvT1qVDYt28bJ30CR5oJcLu8BSlfb7zyO1K_O8kWKexMUvl0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادار تیم ملی اسپانیا واسه بازی حساس با اروگوئه آماده میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/96112" target="_blank">📅 21:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96111">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMWUI330AA2tFW2Wpd5R18aGtlmwJmSmaAeklJ9Tc1zMlF5736HxprGrPnnD8ErmjN-cYbQ6NWdZxaxG5kKgSDnIJpVHyswL3sHo5VvRuSXutgaJ3Yx1HuZNQC3iexXjucX0R1ni4oZg_3Jlt--YqVxx1_WJKuyFvrWZd8DXVUvjkHL5PxHD-05kyvPQ3uZoVBVnmoSVwpqfrFkeExvu1Tm7j_l8p_9OyLc0Qln5Cx-0KFq05OXfmcp-3Ythh6LVK8xTQqqnC3_Y9KPNMYsUAR5gw7-dp72woIJkFhpj8vFT8Dqyv34NnviYSixWOXstV1faTLoqA7PEBPGyf6FBCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرسنال در حال آماده شدن برای ارائه پیشنهاد دوم به نیوکاسل برای برونو گیمارش است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/96111" target="_blank">📅 21:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96110">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0GrYdVzH0SPa5bTtEqbL59nSjZWohGAeGoITM-E1j7LH2rxijAfxRkwYEq_MXsmKJDdy_yaShFzppVPsIWCU7UPzsJHzGOUyROF4LaMsna6zFoDfZ-elBqGPS85Hd38Z4eIiXZ2XUy2vTLuE8cydceOFEo991DZ2-KBP-fKVQlK6FVuRhCG1yQhYAJXx24g7FwnneWXkQ6dJi3hDq74_5MYCOZA91ekAmFya6MDBpH8KBZmSu372za8lhfTWbfpQH-7MHpwV5SXdV9zGY94VoXjiGT-z_5YeC1-gwOseG_X0U4aSsV8Qcx4oapcnSmC9sVPYvXY1G0KTuSNaRuaUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ایران - مصر | نبرد صعود
دو تمدن بزرگ، دو تاریخ کهن، یک میدان سرنوشت‌ساز…
این فقط یک بازی فوتبال نیست؛ جنگی برای بقا، افتخار و رسیدن به مرحله بعد است.
ایران اگر این بازی را ببرد، صعودش قطعی می‌شود؛ یعنی ۹۰ دقیقه تا یک جشن بزرگ ملی
🇮🇷
🎁
شرط رایگان ورزشی
💰
۲۶ میلیون تومان بونوس
🌍
فعالیت در ۴۹ کشور
📡
رسانه بین‌المللی
📺
پخش زنده بدون سانسور بازی داخل کانال تلگرام
📅
ششم تیر
⏰
ساعت ۶:۳۰ صبح
⚽
ایران vs مصر
صبح زود بیدار می‌شیم، چون بعضی بازی‌ها ارزش نخوابیدن دارن.
ایران برای صعود، ایران برای افتخار، ایران برای تاریخ
❤️
🇮🇷
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/96110" target="_blank">📅 21:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96109">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9dqNa8RSiimuo3COOJmDcz9iPg-qdBGl9VM5ybv_L8Ou7OqKVEUUDKXcv2zidtU6ycdekZdVKKky0rHiSoUpWKD784p1xafeTTuwNynCX_c_VrKrfaDWGRFjfPcTnnxSmzGdPbd4kcQNxDcMjULjKZvDNrO9R14AWCsqb40udUUekwXP-Ot0kLZ4ULzC6Cv8yGoqYKEQhcW4P0XEbc7a3rowx4HGJebuFsqgbAM5MY38rV2T-SpXwwJUAQRoroovDnsREt9PEA6DlLXGApD-luQoq7lF_Kz4UOQGbuzX2Lf--gY1lLZOde7CSKEHD5HTjGADV-EP-P-ukw7sfq3YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رئال مادرید از فسخ قرارداد دنی سبایوس خبر داد.‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/96109" target="_blank">📅 21:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96108">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpHk8EOKpEQHoQzQLQejpVfl83D5-DRMcvI96p1tgVE35fWgx-WmZlDpLeDzxasBZvX5ceXV3JnOp73LwGvadV_Fbes56JgPbxcuFYfOHI4hrzb6lQvTR4YzxwpFDN9vE8ekimQxhUPpJDcopVAPl2V-TRg7iwWZaO6wCVXrMxOLvikDViYz2yuqsWzcaShiNf4urNbi3H-mQ7sbrbhFjdWlRXBRF7XC2tBOQEI8b1nMrxPqUHi8gM6lk79-6MRlpIucYAHH97CQdaWmGZKUzD01_6FjaQ3o1gv1Sfb6brmBiRSx-eACTID3LaIvix4X9iL-F9rhoXIYUKK1GAzDdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/96108" target="_blank">📅 21:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96107">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0QJcIWciH7Ah_oHW2JBpDdwjoThzMDdw34hOyhlzCKYXWdVoutjItV--dFvnD3A02GhxyyTawzHKiQi3hDXRdI0vQhYkLl5aV5NCpkY_z9MyvGJYgqIJm4YP9bHxlFFA64s5lqYIbTh6RbYHrM3sHDJu2Z3Zo83QxkR8vSD0Oofj24FbVDq9bdS_v5W__8F9OVtXBYDl1PeCFUVUc_Zb5QVNCtF9aUIbvYsq2fNf4guUzKP1QzWKvzZbgnWQ5VJ3-rjkYou5MV9Q8kSNpc3Rg-hLcUAeUlj7Q6o26sJrcpMGDJ73TduFST1JsjcwOgil7tuvNPPS_p5kWmC1DhMbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل موی جدید پدری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/96107" target="_blank">📅 21:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96106">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAnXOpzTkQ9kQ98njGX4FYZad1t-k9easw9bLXEFXwB-fTvaL_KesSojTEofXB9tMMWOEva7bI6wRjU9C7ojkmCly7qhpWZYLHcw10Z-R6ky-Omb81qRkgYOHQtYRlAAKs7Qzgki4n0CwSuqPv25d7dozTtL5vVlQtSWcSEVxYdAy4CvsM-c43oUjrO6Y64zn3yYgvqSRI9t9g17Go078DaeTO5T9DJlGdQN0rOLzQ4OberPTPG5gTI5fDtK4Z4UNjd-sIV0pjnhCegyEwZaTHk735ifg9ag6gLOPUGBI0Fix5yai5nOHRFj4jLFSRakReJxM5yx3xMvwI4s2Z1opA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران
-
مصر
نمونده.
🇮🇷
⚽️
🇪🇬
⭐️
با پیش‌بینی این بازی، هم
۲ برابر
امتیاز
می‌گیری و هم وارد
قرعه‌کشی
iPhone 17
می‌شی.
📱
‌
🔥
با جمع کردن امتیاز این بازی، یک قدم به برنده شدن موتور، توپ طلا، PS5، iPhone17  و ده‌ها جایزه‌ی هیجان‌انگیز دیگه نزدیک‌تر شو.
🛵
📱
🎮
‌
فرصت رو از دست نده و همین حالا پیش‌بینیت رو ثبت کن
👇
🔗
روی «
لینک
» بزن!
@Snappofficial
🏆</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/96106" target="_blank">📅 21:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96105">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔥
🇫🇷
🏆
🇳🇴
تنها 60 دقیقه تا آغاز جدال تماشایی وایکینگ‌ها و دیکتاتور امباپه؛ از دستش ندید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/96105" target="_blank">📅 21:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96104">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7VmFu7mAdYRFepEIQ9AFt5N8QADWiOR6t-u8JvWqBIKhR5-3ohJLwB5ytPbUrxTbWCDSx4aM7UrCUn5ro1lkqwGRpltw3jHkLjeAC-peKSH9PuwIV80YtqGLiMJxg2q2s9b2Asce0Bi-iaiNuPfMkyQab4oYJ24CwuY8BJgY4ZLq_2IgcnaGAORu59Nu5yBPMKoP-Q0lOEbYkI_W8Mw-rUZ6v_EI354pEO3Yaiw82WxQ0qZcWYW71yDATwIx8f5ERPNBGlKpDNioLnkhigF3lTLb5-idC4P99q6QWY9q_mfs4L07rKEKKU1ra2lTPAe9ky2G4xR_AorVjo4UcfkKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇪🇸
#غیررسمی
؛ به ترتیب از چپ به راست: پیراهن‌های اول، دوم، سوم و چهارم بارسلونا برای فصل ۲۰۲۶/۲۷
⁉️
کدومش پسنده با ریکشن نشون بدید:
اول
❤️
دوم
👍
سوم
👏🏻
چهارم
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/96104" target="_blank">📅 21:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96103">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🏐
✔️
ست چهارم ایران برد.   ژاپن
2️⃣
-  ایران
2️⃣
🇯🇵
25 | 25 | 20 | 23 |
🇮🇷
19 | 19 | 25 | 25 |
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/96103" target="_blank">📅 21:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96101">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uROpMAOzzNZHfUmS6Ma7N0qBbFoJmf1aKHJtBYMoh5yBayiMBPvXxRqI7QwL8MCBccWkmJfqwZEoUWG_fbZZrgVxpkSLt8kvJm3goGHkABqI_ylEKxHGBNXo6qpr6zfFezbJ3jhodRnLhr_wEH7s-1GN9uRHD6vewou9RLveeNjGAmOD3EhirTEpl9mrAMqP9cYAsEp9vEJ6AuwoacGRz3tyBGXizOuTPQCYpOEiUy5b-pif8A53lMYnVfeB_0ZCTN4wFnvl_hElZ4IGAKkyqd5NEzhDmyg-DVovuzTtuR5IPV8-qXaASAMd_XqpW17APw_5JQzIImapSvp-Fn0PQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eIw8oXDJychXXI-W5Bao5BhqklYsWmPciFK9QDSWWvpDC96ZeO2IWZJeVnwcuPYTAwHruEGj8QqaK3_7G-Bahtf6F78xytMNbKbfSGZoehztvaLJfUUnx_YfZSCYTq3AS4q-_NSrej5W_1nUOTSUttndKP2eAh46uCcO43yIngaq3GMXGDfoSHCpI-rF0fdkWprWqNvOTDJ6XHKHpqduk2yFmilnXqB_kIL0tVEVlAK7su9QSoAlUUkHgbRizoW0d3S1xWQvfF9zSbSpzT-79IN4e26hoKqIPLPUR236G6Fhb70DxrhrIH6UvQ05ylJMHblqmNgX1s5Tm_wc96q73Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇫🇷
🏆
🇳🇴
ترکیب‌رسمی دو تیم فرانسه و نروژ با حضور نفرات ذخیره وایکینگ‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/96101" target="_blank">📅 21:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96100">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u95lYFMbbhkr7ZJ6BGLc0RhSD6lZtpjlvQ3Kxbwgz3fOpfzv4sMURdVv8ClH1lPLW5vHn3bgmUVi0D0JgvPv2YDnB-XhOdOaAAefy0DszQ0967mBGgUtp5vJIGSJTl3Q56VglgJ9N0yD8AFH4J2wDwzCaTnaIw0EXbSK7KxaJSHZSXV__4wZspbhAevVG4Z2fYDejRmmP_VTFwnb8soOkk8DeJF6gu_a8Pk4HYDwzIv_WJ7quUPfwl-iTC52UFi6HteJmS5X3aPy42m2UrkjBsai4duextrtEZCCq1YHKrzauSdUdL046VlNDShPaQNa8kThk9ARPnnqqt76n-MnbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇶
🏆
ترکیب تیم‌ملی عراق مقابل سنگال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/96100" target="_blank">📅 21:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96099">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGyrIvokg3wK_IEwXmTt9nBuE8f9uPnpO5kBPQWKmQJTGIa9fsVwgbF4uhyG12mEql19b8MdwnNSk3hw7TPyTz9sYYIwolNduiR8aGNGmfF2EI0rdOaa1A8wTxxxh_mvVoF5fwNy9s-mYDzfMR48GO-vWtpZDAN9EWLmCvIdI3H4MVqwZbNPaNe1ffVEeqqc52X7hhPeqT9xohlwoKOiuKfVe-hGrCMjQFCyf7BeSrd-btWIa1GxUcgoAZNuMrbTisnqfUinNR8cLZP4VhIVBV2aVD7z0vgmF6vGYc1y5ezehZGMKcLW5qdXYkU4UURw4Czgw8zD2z8Rw3hDpN7drw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇶
🏆
ترکیب تیم‌ملی عراق مقابل سنگال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/96099" target="_blank">📅 21:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96098">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc25ce70cb.mp4?token=IC8th0KgvX9PKGKqBLNja1BRHb82kTobTRxhE5Q2tVodBiKTmvSd48SRC5zG37t2lM3YvC8diiG7DmEvNscF91SsRIsKnVYgkg_xHs12C7GbUlagJ1Lcck-qtVquRLrpGWit8Ua15WY6pcqFAVzINM6Hgr-LCa1xlDVP9-RyGdcCnO5ZSzzktAVV1WLOfh28dcdCVxKI_rZKb8Ynirhy1gOtVC8fvn2l4qaut1hfyF74mXoIAnqdW2AmhA3eOf1NAnNC3gI7cYeF3fbsVoLJ_-OmLvg0J-8lvLW6jYIAVhFiFVVRco8XJfbLg086UM0nFgE8mB5dOF4YqUgkh5sd0D529OT3P41zrA9Dv2A-gHYk282ilBVRIbG5Xmd6wjwnJTkUjwluVKhDcT8z0OD9mPiG4WRduyWOuqY-wALrKULJzxzL1YiL-9SVZAB5X75Yr__BOcKg7XmsRb7AIia4KWb_Y1_q7hmTLnv_gHkLqW4WjbcU1m2BoR64XRCY6Bcht2-OHuG4LPNR_3JiXSdgznxjDIguj-vNe-Ri44TnmKH8_y7KAA_5Ynr5McPyTgEbpfe6rm_rXWaoDouGEBoMbCFh2gmP-A764kbxDU0MiIXqThN6XNZ2h1WrKpJAj_51nbNNRDsuwCfQqwts5Z8OiW0qvT7STqDvjHcimHfwqB4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc25ce70cb.mp4?token=IC8th0KgvX9PKGKqBLNja1BRHb82kTobTRxhE5Q2tVodBiKTmvSd48SRC5zG37t2lM3YvC8diiG7DmEvNscF91SsRIsKnVYgkg_xHs12C7GbUlagJ1Lcck-qtVquRLrpGWit8Ua15WY6pcqFAVzINM6Hgr-LCa1xlDVP9-RyGdcCnO5ZSzzktAVV1WLOfh28dcdCVxKI_rZKb8Ynirhy1gOtVC8fvn2l4qaut1hfyF74mXoIAnqdW2AmhA3eOf1NAnNC3gI7cYeF3fbsVoLJ_-OmLvg0J-8lvLW6jYIAVhFiFVVRco8XJfbLg086UM0nFgE8mB5dOF4YqUgkh5sd0D529OT3P41zrA9Dv2A-gHYk282ilBVRIbG5Xmd6wjwnJTkUjwluVKhDcT8z0OD9mPiG4WRduyWOuqY-wALrKULJzxzL1YiL-9SVZAB5X75Yr__BOcKg7XmsRb7AIia4KWb_Y1_q7hmTLnv_gHkLqW4WjbcU1m2BoR64XRCY6Bcht2-OHuG4LPNR_3JiXSdgznxjDIguj-vNe-Ri44TnmKH8_y7KAA_5Ynr5McPyTgEbpfe6rm_rXWaoDouGEBoMbCFh2gmP-A764kbxDU0MiIXqThN6XNZ2h1WrKpJAj_51nbNNRDsuwCfQqwts5Z8OiW0qvT7STqDvjHcimHfwqB4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤩
گل‌اول پرسپولیس به چادرملو اردکان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/96098" target="_blank">📅 21:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96097">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZzk8Jw5DMVbONB9zr9x2Ej9rvzAcokY4MUrYECab3FYm-dXsEStC3nhzmWL0-s13IceSYLER7Q_51akR4YgnU3tZo2M5PoYnRrjUqYoI-J_ICGmLiakvzvEXceCrngn2nG23v7kw1oY6kZipDTPo9EFNwr9QIJnBxqFsuYj27bil02bLw3YI_HGYrNu90bn9qUmJziCwprZjpNBpIg0wryHOS0vPaUvtlByrCGihR58cxKRWS4_jkvMHhTnmLzVb5NFmj2bAVD1z188Ir5wdub6qZB0JOvKV0oYPqRTINN5IV_IyGoFrC2APNPzIrxEx074FWFym14wYUjyAed5ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جسیکا آلبای عزیز که اول صبحم تو استادیوم بودن مصداق بارز جمله مادرو ببین دخترو بگیر هستن. البته تو این مورد باید مادرم گرفت
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/96097" target="_blank">📅 21:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96096">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPetOGyMePb9gLzycnOyTKrMbdILIhsZVUokiUMOPpHb2chGAyRxElg-nEgESirmEv_64iPjFojIXWo6jcrP38Pz4r7clViGpCtmv-UNJdca9Ny5oQUFap3DTomJp8ej6LFT1RJn5aRkuEI3P5-2_90l6UEAn-_6kLwHdtOMkikE9LZJwvg9uoqG54_4SYcs-9mtYOJwbpD082jEjCug1CJirOYF7ddLJaaFzZuWwXTG1460eUtcrfPSUrXqxU-k87WGlGW8Br88Wow-sFooawUmKmRye8GjqID8xJ2Idy-B1EMHJivrdHO9gA2c7xbIiOwj9FfKoxoAmUcWCya3YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇶
عراقی‌ها در آستانه بازی با سنگال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/96096" target="_blank">📅 20:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96094">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🏐
✔️
ست سوم ایران برد.   ژاپن
2️⃣
-  ایران
1️⃣
🇯🇵
25 | 25 | 20 |
🇮🇷
19 | 19 | 25 |
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/96094" target="_blank">📅 20:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96093">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbxjoNe4R28HVhkEcX7ljBj765X1MTOKW2m6oSHyt1p48YE21fpXDTqwR_zqGXROsfnsxi4xH9t2QF7Chulp6x-s-itJ_BcjctUeGHN_M82DB9svkqLBvKSk_ljkSr2eruGXABzIPvED3oqV1vYlLol4yR2F4A2juq3359OjSHkXoFb8f0-wk2JMjmYQnLpolTkp1bFU9aie8_FLlcjryNqCKriPkWOwzQ-Xg2n_01ZZk8b_to5ZYEgdLmSabySbKEdTrBgP90EWwNLhJRxXTVaE4AS9jqzKQYPFlutmTT0C3cvN-6pqr6VN3o2m4A5CZjthDOBGLXoIOaDfqb5upg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🇫🇷
💸
#تکمیلی؛ میلان برای تکمیل قرارداد رقم ۵۰ میلیون یورو پرداخت کرد و قرارداد تا سال ۲۰۳۱ خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/96093" target="_blank">📅 20:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96092">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
#فوووووری؛ با اعلام‌ رومانو گونزالو راموس مهاجم پرتغالی PSG به میلان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/96092" target="_blank">📅 20:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96091">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A53f6AKXzEaEP69DSwDbPmcY-p_J6L7elAPp5LXY3AJj9sfiizj3WQre1vUMhFo85TvwE1QBFixzFzpGGbtJcs6BL7VVr3ZVtcbf9kG0Vh858cXZJcYBIoZAFDumT3LlBaQjhKXMp_fwK6HmihjamOcKVy9uDJvg-drYcC3x8tJLhg-zdieVcl424Lg37p3rz__AZVmMCBRLsSgFGQ4ur-iffVQwYiUudpbktWMJV8aW9Mt4mJqmDZ5JYCgp7i6rbQxemmWl5OkGD9770h97-gJS3vVSc5Wpgrin7yKl3d91-QSIpfXgo3soajR3ST2ykSi7oEFV6XO48vIqVHAIoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
#فوووووری
؛ با اعلام‌ رومانو گونزالو راموس مهاجم پرتغالی PSG به میلان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/96091" target="_blank">📅 20:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96090">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXpswmY-IlhTY343ze_aW4gLFnmQwxsARDdHPyUDm4lvvKs6ufU3p8duRmr1XyuJAKHB78ml6QjF_Odfjl3jLlA2NML9OxtgYOSkrZQJH7aaSxJXHpzjXOzXpV2vwTUTT3s0wwQXgVKTD-SFPsgZaLjDWaG9OXDSX0IO_Qe-BkZXlg9xFNB1qQGHtcVh4DxPD6LLWoZXzLhe0p6k2uG-YtONFvbslby36e7zSMx8XSAEHkYTa87xtlW4HgblA3VwvDzGIU2CzAKne8MpozsMgFT_iwvGe8eBwGEhxJs15yfMSfZE13C7XLVSy25IoqgKG1cckhOgvd65V4r96lab2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🔺
۱۰ سال پیش در چنین‌روزی لیونل مسی از تیم ملی آرژانتین خداحافظی کرد.
🎙
مصاحبه لئو مسی: «من تمام تلاشم رو کردم. چهار فینال بود و نتوانستم برنده شوم. هر کاری که در توانم بود انجام دادم. این بیشتر از هر کس دیگری مرا آزار می‌دهد. من بیشتر از هر کس دیگری می‌خواستم با تیم ملی قهرمان شوم، اما متأسفانه این اتفاق نیفتاد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/96090" target="_blank">📅 20:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96089">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKop7afHF2K_bRlhLEd-He6GXFMGHX9UaiF4vaJhdI1uqnQCafWzaWXKfLsjGLFLQEKee3AiX3RoG3aRnHPn42lC1sUbRl53SAzWFstBW3OpyAyFtXnqp5ZAwWnQpxLW8kSFzqrLoJai3DU4612ovXXq8vwltqwPduHjnnrsqu7NilRhUd9JSjLPH92JkAwU6ivq8mjqTzL1GgG4yz1mTe4jhb0OC60s9wRvSew39Ge20E8OPAmO-8Q6YGgts6_3gHxziAR04CWIuSB26jwWnHXE3cBOjgNfj4rnIhp-9RAHOQhShCxNOg8dULV-j_VNap--qE55QGzDXl2bJaKVUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
؛ نیوکاسل یونایتد با ارائه پیشنهادی به ارزش ۸۵ میلیون یورو بدنبال عقد قرارداد با انمچا ستاره تیم‌ملی آلمان است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/96089" target="_blank">📅 20:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96088">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgPalmdBZ_Y652rNXy178GYE7hMjBAjgkkwoXpljKl5dz9wjZsuUxxLzed-z4X1R6O7ZCMiDy03vLzVEYa-roy7CA2zVWerDBAAbnYk-Gw2DUuAGzOGBlmzTEpesKYbb0AQujGFICNOo26Y9qsQLLn2QWQeV1KGDI_wGcooa0vUU4shMjuijfUlc-32wjHUKhPOTTQWwpR9c9xwlAJd-_2682X2e_bbI1zGi827TFbBR2fUaYT59s3Dpe2g2dv_ubx03o3N7Z9OKSW8ZJIuO2nCkl4OoFO8LCN20AjFOZxB5VXc2ZO1HqEZZw-mZfQvVMOBJV0yPgZ9g7LAyrIe0oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به بازیای جام‌جهانی ببره
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/96088" target="_blank">📅 20:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96087">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🏐
❌
ست دوم هم ایران باخت.   ژاپن
2️⃣
-  ایران
0️⃣
🇯🇵
25 | 25 |
🇮🇷
19 | 19 |
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/96087" target="_blank">📅 20:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96085">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XS8Z909ypHlHC6lTYVyKwKQ9c2LMyZXvl1tvSa9Peh8rmX-8OuoX2CkfkcdnkOIqMZm6YP_W5Rs9Hi4tLfclS190ZAWZAjkSW68ryXFFApVLS7VDr5dExgXrKmo77FiOHQhlMY3Vgs-yRHM4Ssq0W1alpCjvLIqEek51rskUYQtH1Snk30lKV6lpMISjWVKQzZ-CH3HdeowqCbDPyYkHY8re4XB9DqpV2tBcv8ZqmL-diG8orkLntYsED_DCmwberWw4MzBEPovKIKcm8iTklQ-hEn5yaP1WgfslMLYVy3PgP0imiksbcMzShP3puRe0K008_7S0GUPxNRzSJ-lwdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/howNci1C8YQ2kiTBvEEmvWQmMko_twoMk7kYQXOn-x_s0iKBGGOwJsTHlcFL4TaJrXBfVJJ7Mj-yEliPu8Rm9a6p8VyKshf7zdELiLvrWl3Nod1Xb74AsXYw-RvkJMe-GbtiZpY_B6ad3HCobkH_SHF85ZF0DAAlGa5J_zKTXByWxNFCel3nVC7zaitXVVoMJjvHxHiGtBYfAzszsm7-xVz1M9_a_PSgGwZTwGfu3HJ0-V6qsMkJH6T4JkZdu4ENrDRgQDJkej49ILEY7BA0KdnyVxQyMMHvQwXJO-gf6WaukxFhphn-xkRCSuXt_ZEUQNr1XUu-kVmH_-F03tztBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
پشمامممممممم
برونا مندوزا مدل ترنس برزیلی گفته که حدود دو سال با یکی از بازیکنان تیم‌ملی برزیل به صورت مخفیانه رابطه داشته.
🔺
به گفته او این فوتبالیست ترس زیادی از افشای رابطش داشته در حدی که قراردادی 500 هزار دلاری بسته تا رابطشون محرمانه بمونه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/96085" target="_blank">📅 20:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96079">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZZFkZhsr39uLFmc5AP4FiM77aFR-7eZFWhlxNLx26PSzXAybOLTMQZOcomYiiyhW3VLLT39ziATYDioP4e2dlkVEhXBEdywWob5SvD8tC03LlY-ITLU39tPijouzzibBnSucUJLJK3OKPOQ7medQPxGC_g4ggb96_tPmqYRlGWGgBPOFDIpjbcUkwyB1e--mhK6ZvHXIU0LjIW5uGbO60FYhV098suGNXAoODriM1ZATvxE4OaHbdUves6YmvW98gmVjlViRLFpu7YyFINOeg-HElDuzK65guVmilXWjVoXXgAizqT06ZdCKbdK4eyj-mw9NWi3qbpCn4UjtSXsLCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FlTAHx_kSk7uKy9MWlMN8vTjIu2B0OecDMVzxRUymF88Sh3ZaVIyGdvTwBFKOXC6OF0WzMypp1tw34fjtaG5d0Zj11CXHwGb9rEiBgnoSqzkHjJIakuEu7jx3keNXn3cBplFoSg-Oi7GyI-k_A-VKzLpR0TUmIbBYrmVbGFmAP-POl8c-pB_hx8baqtXYUHsy3GSFQNrYLjT0R1wb5am3FU8eStCEDiiT2tIOhE2Ro6G2Ll-9oZPAX6NUdaMIc-7ux-gorg8FO6hoBdZN1ZVvBdoy9Nt-AgvXb5Yg3LJAaKdBI8EHky6eoFciZ3GWVPOe89k2QhWkpXY5JhYUlGQIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C8AIn9YzkfYkaMzxfzfnjmMir26iIywTlOXeu6tJm0ykiaH5RGFpn-KVYRXO3n7uflue_Z8-_07Oyh8D67o6fCjwtCUY5ZEWA8mGBPCyzqLmxP145JPnjb0Yu6LMJKjxVmf5f8pW0EdLBl-pIzH5KWX2REYw4a8a1_bsZMWS8yT41elbmgwyr_DjPc8RRGOwYHeJJKjdkTUegHqs1TYBDJNC0195g555XxQdhYXm2mbUe7ksk5JbOWY5VyIAK07aXemvd8fUaCQu2exLn_Mx4_FtGYrj9nOw6swsT0xGRC4GUVvdq6neIWotJy30X4WMxwGQ3vh6Q62BMpxxDAxK2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lCm9zY0WqTa0T2n_C_QXyGOFa-PINAck1nVBF4LhvRoEINHEMgsoRKg81v8l0vE1Z13MsmivGWJTDHGYGH0Sx0pYv83wJdbTKO1UZZlhmXNNHOjbyA6g0AffJMQJD3lo8xMiCKfI6BqDGWKgnQixavftrMUxqDZXSKsVQySbgyRFNqwoVAhWRhGS7jVCzoanhpKKfPEAWD_-zJDPri7jA97o4jiFSQ8TeEII1_L1qn-k3wqzOpSfrKrXT4_99KRUk2ljHwi9gZY4w8MBW0BvntolCjRqszcBwsIJqGE83DHYhC7mgKJbNLwkYf-GwKASvwSWwlrPk8390ZDJqLggDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d565175c8.mp4?token=iW_ErVzodVI56hLeJgJwYLdyXiDHUQzsQEVkpOo5O6gprXUWNm0tNj-jI5aWmxmtQ9D3WGeBUnGFc0sBpNNBeS10W_TY0b3itWc9xNXfonCEjKMsjuryrMjvP3V0cvq7XJIc-AaFSYZhuvf7QUBEwaLcdQbJD2y6WiPb2w_PkyYYnU8EC1ATPI_tMg-6Bw_wq5yiPNtIyAaGd9d28bnBFBPtpFDFHlPhv7HiR1VNLJqxM7tllwfWrYQi-HpPPOa5DVUHLD3u3Uw2EEmxcPZr9pOywRQVuXjP84ZSMFWj9VLtPLzHJRe-CwpM4nxIQu2Zd5j26njVvceIlULkks8uHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d565175c8.mp4?token=iW_ErVzodVI56hLeJgJwYLdyXiDHUQzsQEVkpOo5O6gprXUWNm0tNj-jI5aWmxmtQ9D3WGeBUnGFc0sBpNNBeS10W_TY0b3itWc9xNXfonCEjKMsjuryrMjvP3V0cvq7XJIc-AaFSYZhuvf7QUBEwaLcdQbJD2y6WiPb2w_PkyYYnU8EC1ATPI_tMg-6Bw_wq5yiPNtIyAaGd9d28bnBFBPtpFDFHlPhv7HiR1VNLJqxM7tllwfWrYQi-HpPPOa5DVUHLD3u3Uw2EEmxcPZr9pOywRQVuXjP84ZSMFWj9VLtPLzHJRe-CwpM4nxIQu2Zd5j26njVvceIlULkks8uHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👀
یکی از خفن‌ترین قابلیت‌های گرافیکی GTA 6 سیستم نورپردازی و بازتاب‌های واقع‌گرایانه‌شه.
نور خورشید، چراغ ماشین‌ها، بارون، شیشه‌ها و حتی آب، همشون فوق‌العاده طبیعی به نظر میان.
از اون طرف انیمیشن چهره و جزئیات محیط هم انقدر دقیق شده که بعضی صحنه‌ها بیشتر شبیه فیلمه تا بازی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/96079" target="_blank">📅 19:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96078">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🏐
❌
ست اول والیبال؛ باخت ایران
🇮🇷
19
🇯🇵
25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/96078" target="_blank">📅 19:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96077">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSe42LyAzPbOK408WJlkxSxZSwHSnieoT5duNrn0Ctq0sVHJIwXx4HCdqR8MEc_CtWFIHfxR_vL_iPT0SV4tpBEa4SzaRkVXZj65pvY9xWD9vvzoK0ouHFrkjApxl0aUbkN7Yh0xRndI3oUOHNq1NFIKnVkJl-5qBhvcqkYf2lgfoRGoPoICOVCt8hKIP-c2yR4GKP9zoCSUbY5UxHojJ43elWOpgLoUo5bevYpRWRVP4kPEn0pgsBjDCZH_qwy4FLMKTLXWOeUj_TAccCqC3zStAveswnEREZQokt0norkkIbstdixnUFsxSaoHpCqMRzlzLnfhtJGsr2eSm0iw4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
🤩
لیست‌کامل بازی پرسپولیس و چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/96077" target="_blank">📅 19:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96076">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🇮🇷
🇪🇬
فوری: تیم‌های ملی مصر و ایران اعلام کردند که در صورت مشاهده هرگونه شعار غیرمجاز یا نمایش مرتبط با جامعه همجنس‌گرایان برای بازیکنان یا کارکنانشان، از زمین مسابقه خارج خواهند شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/96076" target="_blank">📅 19:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96075">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🏐
❌
ست اول والیبال؛ باخت ایران
🇮🇷
19
🇯🇵
25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/96075" target="_blank">📅 19:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96074">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCWLhp40VNZe6J1kPx-cAvXhmEFkhtBB5Y0iwQTnubUKXJolQJQJRz_aWUNfQksUGh8kZDjZo2OcAFR1ChbY4JXbNxWuudWa30P0scGKPLzCnQT90Dfkvr1YtpnDSsHZJE7lmYJx7r387f6O3b-ybr6qQM1ha_VeLon5VHDVwbLBYoIdHfVLCJwsU9QC-gPqFjeTUZsk-XrvzJJXtuEu_R7A2xmm9sLNkBduIP2bS1ItBKIiIb_K1hCR-dGQEuBA5dJixpQTD6mDs2hweJiCvU5ic_8hQdrCiz7LTgSn2NUNWmkKJf1WIfQFXSGCrMLN_RfsUj45YxwWDqdO4G8Ldg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
اکیپ:
نروژ با ترکیب ذخیره مقابل فرانسه بازی خواهد کرد. 10 بازیکن از جمله هالند و اودگارد استراحت خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/96074" target="_blank">📅 18:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96073">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn7QuGqOdAbxY6sLanQm1--QZnwT8gDLdPisoz-TtjpoLZm7X6WA7SvffwHmuFalOza5wJgThhtauWC8ogefloBuFwUbRh87mtdTDTOXEnbPbnmyFZE3czHQjdVlukTM4qCQiQ1QR95RqwV2q-Yn-O4i3AQpAL1fuz9YSl44GT2w1UPEwEGT8dawEpz6tcMGhAV5O-d5hRuk7UhjAJjjMdGNgRiG_yP0CY7vVLE3zWnSPOb3tem3xaetydG3K5pL4QCkJ8Mp49Lcj3VC49K-zchO-jK654XjyiQaDVFmrH-GsN12UCAkByr-atcXgYSc9QSmKqDsKLYnknybgCjJIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لئو دیاز خبرنگار برزیلی : پدر رافینیا از حق‌وحقوق مربوط به تصویر و تبلیغات پسرش سوءاستفاده کرده و حدود 80 درصد درآمدهای اون رو دزدیده، ظاهراً این موضوع زمانی لو رفته که رافینیا و همسرش میخواستن یک عمارت بزرگ بخرن و متوجه شدن با مشکلات مالی روبه‌رو هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/96073" target="_blank">📅 18:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96072">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEORirRH8TX4ZLKpZ5cZp-X9JQLqgwxAzdPopl16rA-gyc84xRdHHl-O6VITj_EHw03EPewAlkZyI88pTCphjQ7RgZWBxdYTk4Pmqb2l7Syc9HLzO9ABn4jTTqFyNoMc_UiYzE3-0rQjduKbzT9_hBo8HQO-z1DnTP_0-S82uZaSzWI8w51MkjA6SA6056bDc3QdFk5El_PVG2nH-c1M7KwG_SwXT29RMxTZO3HEYMSYqmC_cFDdgEJhJYDLPq1TaU2olr7Ibsyn3le6LuqS75LkxEg0MXIl3gjSpA1vu_5g4jjriMyeLsGPI1CXFcICCcURpA1F8w1gEwqEbrhfgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مسی
18 گل در 5 جام جهانی
5 گل در این جام
34% شانس بردن کفش طلا در پلی مارکت
⚡️
در برابر
⚡️
🇫🇷
امباپه
16 گل در 3 جام جهانی
4 گل در این جام
31.5% شانس بردن کفش طلا در پلی مارکت
⚽️
حالا پیش‌بینی کن چه کسی کفش طلا می‌بره؟
شرط بندی روی بازارهای پلی مارکت از تلگرام تو کمتر از 30 ثانیه
👇
https://t.me/PolyBaaz_Bot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/96072" target="_blank">📅 18:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96071">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1asEkpYe3iXl-6Rwp4YwqC8lV8cGAlqPp_vwXvwAhcZywBS7w4dMG0_9gZPEx317fphujB9VVAsu2RwooWVjaZz-Eh3eHB3yI0FmKq3lMwN3-09YXumotjZCH_SzDgMpIlZPKO_TwS2Yr-EEpU-fSOpky8hcL6WX6zZob-VGhj0LbyA0ep-hBfgUiqqIaHGjslCuuCqEpIVeZGX_OiBKLlJefpEFeNllZcvKAKMzpZDdqHdd37_FK-Jpz7lh_SoaNzxn-yhPw8LzAIhdU3q1M0iVcFEtfv6Up8NQXIsRDUHJw9ufxLKnvDAtQZ3BkUlg5hx_ScN3qleYDlr_NLf1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت ترکیه تو مرحله گروهی جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/96071" target="_blank">📅 18:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96070">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd55ccb496.mp4?token=Jkvwna4B63vcTHEJHGCYZfYvCuTOqYH7pj7so3o0Vf1oZmGk5qOtAxcczE_HKDRaAysUgs1MCb-6WS2CwPL-wexiOY0JiIN4YqS5QMTnort9_f3aCgI-xLUZ2Rsh11EcGLrtR6liSIcq5IoEa0-VdVX6xCatj45RyFr7tGuDPrOs6CJN5JlSLgtgEnRlxBCp2VFRo9kv5qTORLAd5ugmcgRT_-T8wt5Spu40RsX_S3qabjWPYIoh_of50oUZxyByLSZS7h5w-cFjMFHcp2EncJXJeCwgnowL_5bgE6SpFwDiIuqIByYBW-cJtJlwgYXxj4fhzau_8yGOB3Hrng3cAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd55ccb496.mp4?token=Jkvwna4B63vcTHEJHGCYZfYvCuTOqYH7pj7so3o0Vf1oZmGk5qOtAxcczE_HKDRaAysUgs1MCb-6WS2CwPL-wexiOY0JiIN4YqS5QMTnort9_f3aCgI-xLUZ2Rsh11EcGLrtR6liSIcq5IoEa0-VdVX6xCatj45RyFr7tGuDPrOs6CJN5JlSLgtgEnRlxBCp2VFRo9kv5qTORLAd5ugmcgRT_-T8wt5Spu40RsX_S3qabjWPYIoh_of50oUZxyByLSZS7h5w-cFjMFHcp2EncJXJeCwgnowL_5bgE6SpFwDiIuqIByYBW-cJtJlwgYXxj4fhzau_8yGOB3Hrng3cAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اکوادوریا به این شکل تانک آوردن کف خیابون تا صعودشون رو به مرحله بعدی جام‌جهانی جشن بگیرن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/96070" target="_blank">📅 18:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96069">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQpDik0ZgdaymK_ZiJFkgoZMEA1pKZhEM6L0sKQ0RRaL39Hhmj-tpjPWIkW9k7EQKRiproUMPVwbuuYHxPZy8XlOaKsktnMvG8qgm1TPUhM20pbeSZsrVLLaGVTt7mt3lwkszITPxEotwx97BKl9SQKtBBQJdALZnqkKHsgqt2RE1KEOvX15UmkZgAse3TulMhdpLl1lObSkTFd7BlAgi1at9L5hug88xAY8ujxYgG-ZAz_sSdtobSMWB3ZD701FNVWvidLTdI4ZbOqY9WKqoETyBr20RENF7LNzUpOolKUWeFv5n0oQFNnt91fzYWRkH5HEE2oJiWqFBQGt-hvYlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
⬛️
🇺🇸
#فوووووری
؛ ایالات متحده آمریکا بزودی با ارائه برنامه‌هایش کاندید میزبانی جام‌جهانی ۲۰۳۸ خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/96069" target="_blank">📅 18:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96068">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6FgFHqiE6mJDUZXwTBoWTNSITdR5wlk7g8czFeLE2zSPMYAM62U9u_hY4TN38ypK31xICl1BOyDKCjvN11DxEbf6zopLhfaFDhsChG0DUktBHxFRH_6_1lhlzmRapXDOmnJ-3gAi0dSFbqriIg4O1MfASAomfX2OSec06TWygvFSsK-zGCRxd2SGbsKe_qXd_rWne6qIRam8vvQajoDy1T51q-XbQ_f4BmW6TPwxIitaTRoLk2hsTgQCbFMHORXXLf8XtpJ0ioHyOx83Mzoe2_A_VW8lISPfM8w-7G_Ujcr4tjB-mVZ-KeDs8RT0zVdrYjMzR_8IXU1WJxBhxDO5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
هنوز کلی وقت تا شروع بازی ایران مونده ولی رژه همجنسگرایان شروع شده و هر خیابون رندوم تو سیاتل این شکلی شده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/96068" target="_blank">📅 17:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96061">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TC7RDRAr7TcQSj0PPGdAKm0rAPms_tUjfZ9mfjnGZZEhGtzaWabr4tjnrvJwS02fvMBRzqRCJX2uzwzLXB4GGVS3dZ5oh-uUaED4HxV8zuCL-8lFymeKTvLk9RpWQCTl-WztBk7wEoszMCI2xSMHFzO8Faj4JfOKzKNHscQuV65np7WlSdBnXhTLQ4-itITBhVL1dXYxfPnrf5PcUd0lF21v0FgM4GewxcwAs5ALtmZ0Ft7WFHWETvlaRjmdHgq_7g3AeFSvws0NrRyfZM3Opc8SQOvTrX6pwV-qNNBcXbM3V6ik5QKwfjkZWG2BqmDmto5Uj8zsdS-b_TTLHDVjYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SWorjxboXlb1kMWdgAld3ysbPawcuGx0MX_oGCpsf8Fd9-HbDSc8aK6oNgyIJT94qV5nhiHCjWUrv6D0Ufd3LLWcECWtn2I6AA5BOWTBtxG8bZHWfFJs4SE0dgp2xeyh7eZ2FEZA0lUJSOwRgd0AY-tBA7mZ5pCgZjClvCpVOwpbaofeXb78D96Hek9V1VH0RlK6hNvJbrtFFjnjKNKwSMGlaD9TFjutJso32x8KhH4Rlr0pJ2Sz2FsJbGIBvQRhZQO5WzC0Sa8uzk2ZCp6K-4j3d0PAPzkC8G-lQJkC9wr4A85CQCTKwgGWIMsgwzvTe3n24avv2JfgN8xKc1G6Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1p9BsknG2bc5sHtwsoF7vVcxjL9z8K0W7aUrbFDod4hGa-xuEv6bDV074Hwc9Z59goTyX_-j6CqqIR76F2UD5H2RzCN5iHFL6l2R-ArSsBS0zBYc0vOHO_m70VLy6iCbcA1rOFvOR5RFoHtFmP_CWQG2TH1Dh_OUUxSTtdEOp0zFM57o-cdNpc8XfzU6KmYMe0QWXFdrA5bE4At-wuT2LDx37CHmKNpzUdEglQ_4ONUFRYbZii3Ns4Zuq0LruFjCNLXlJEFRvo4GL6snB8lQV-TF_KyOrICv4ICDG--AXGIjEzRZ0f0RRGAcoSjLM0Wr6QfqNq8Nxp5SBe2UhxbDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U3GKlR3L70QUaOT6tNTNo1Tk0Ay0aL1d4un2iPteWy4xoEfIs5WLMhP0qTa5HWb4PfaBGFw-NcFMhJwgQ5x9QyaO6txXOfuI3hiXzlx8jWdYOFEotL5adtS4v5Eu2dGYM-OQg78vh6zrG1H8rS6ceE1dfhXATJqSXVTwW2PfqjANZSTu2gHX7WQSt1mOk-sGCicFA-oOCdSHeQAKqBQmpklXqKpOnVBMzDSxiILeskjxgccNg3pnbx15q0MqVb8gHiNiOfAQw5ZxXnJZR4s0S_EbZyPY4aUbmQySp5jwatOdJOXOYDGDf1bdpHipMy_F02Gzs-AWtVNXNEUAg0lNtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/adITU7qKDzGycBgrsvpTdFwOhKYRVUor496RbqZg7fkm8iC4JXRmPhX4BeqL0unf3fdNUQcAjOt-cxgD2Byw59hCHmXNme39WXmYk2689KH0EDBcsFtPZ3osxQOtNXOkqW8OEeo2RV6n4YDmjR7m5PcxjLTSvU8ZKhBVN4PZQayO64yNweQ0ZeixAMdC4FEBB43FUkTezt_7Hh4kbUUFz3ewMYVCo58-G-YnNd5Ya6CMUrXqAA84ocib3L-_plsOyugD5IKgTfikSLRp15hRbOvQVTk6yQ_PmBIpRZUtTQ6Csu06Q_bJ8CiMI5OBZz5OhgFfkE2yA8Hr7PVvlJzGZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s9SQMW6xx1ftz1SGU1q4ML_oIdJ9gPjo7viilWjQWrBXVblbDAvm7Vj3teqbTaHgpwvAWuz4s6fX_UuJ1ASB954LPbbCifhQjh7-K4VBH6GZfymwD9mzZCeAIl7uK2wEIpEHxUTyTr7ETlbeucUa7IujJcGE9gm0cyVxTcEHm1cPilo9AU8EmoAjwRPxfc7tq19vbFvxJKA6G31Ni3Wgds0RhBJ_h6wfdtqn01V-pQsKg47AMgFEOFPDr27GSXA0bxLaeaRUUdGY6lsoaEzYZYdHPioQWWa0sSamggEgB30LdY4zGlWNWWqLjEkkyZIpY6NKj1fI_SJe5NNK7pqCaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/up-MvLnan69d5wa5ZOUDVzERjGNCSO2HTcp2wZKbJ61urpcg7XULx9pG2cnfXmlthGWgPvXvvaPw42fzUcZhQKiMSsAoRnlMP4kOGZfeY85scjO7MGXy4_rCwMN6Bpm2LE9IQOhk7lYmhMI4Mja52ZbspzzgP0csIGweAFt96zmd4u7SQMmdpFKkwYQXEfFhMkEGoFmePwqiyawA9fgjAWv0UHNLDuQ8mPSVLJNgQEHD24dvI59FcBmjmbYDPajIArolA0sdCDJlxNHl-AVvJk9vUbw10pJAkMQM3CTcyr8a_SuL77oqhKAFmQgxq2_MEtDI8D03psw_WeyuriF9Ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔥
بازیکنای نروژ - فرانسه و زیدیاشون هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/96061" target="_blank">📅 17:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96058">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XvgB4O6Ub6-0VjYk1YVo89LkwNTA-MpYa6bew897BiMoZUczqYFDLIWzhFgXlxivUKmMrV5Neo-BoFrnZKp7STH_x_pzDd-kCaw9j7rqNiPhZIwhf1wKUJsjUKWZqDZ1n25sstjkNKTWb8TRautKIoa9Ru9YT72vNsiTqFS2BveGJrLk96ogJ2WLze-WcvW6qy1zhRnr7Q-pbR8kcI-oAz6zMm4Wv1ELI2EufZ20nEgpOt453L6TFXIr9ZKhBL_UEHH4WpFm3SAOs-JRZPHvpIz7OOnsXVTnLGyq3dEdZyjJeqJmNR5JtsFcFn1kG8VHC2Xrn-WxNVyvEhERfZZzYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jX4WWcMCKRSxfvLhJI7yLtIXWJIxI9yOxXgnQOUClQvQwBN1XQHfhR8KuL_4tiJvxgR0HvrG97iOW_6veohUomEFISdJhW7Q1r5suP9-Qbz6dAId_vIum5TyMQEYQgwt3q-l03C15FzKoCU0GvfuKU-JovIvU5V1cKjn_UwHNDopq9koGxFvPGEHSauzZH4d07smQk802fbJHR8Uq_FCjWWZQO65g5bVsojuHpleVEGFzF36V-GARy1W4t6bxkCPrHPHJrCfzEMBE9WDxoR1eFe-vOsFOidDVoNxAa1vnwZxOuMEWWTVf7jlHbUqAIXr-lKwUR14hCCRqJePlvC7uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
هینکاپیه بازیکن تیم ملی اکوادور مخ سابرینا کارپنتر خواننده معروف آمریکایی رو زده و تو بازی اکوادور - آلمان هم بازیو تو ورزشگاه تماشا کرد تا زیدیو تنها نزاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/96058" target="_blank">📅 17:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96057">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0cd7304b.mp4?token=qFVfYeisgdOOkJSRpi6pzvCUmoMZb_XfcPEWxbgd9Bk8fSp50Ca9Q9wnJGzj1CpKUq6gxOekWgXh-LMNekQ4oqvbpiG2q1J-yXrWybTRAvdkG1VmqcLOp0NuNZ0sLrudlF2C2a1e0S4dbj31JY-rXd9bhgRbFH3S290qba7kSuAAZvFF2VOlKE-NjpdnSFAtKrUYERTJf1uZs-8dFLyN0fZ2k-U-OxywEFb_OwhqHQlDN5Bpia1BYe2au7a4wWPe6heMJofPcmrZhDpzDkxp_g6MWOkjGR-MTle1qWmwSKhedD07RYdYpvYYww0wVkIwZAX_QEM6mL35CzrKLc2K1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0cd7304b.mp4?token=qFVfYeisgdOOkJSRpi6pzvCUmoMZb_XfcPEWxbgd9Bk8fSp50Ca9Q9wnJGzj1CpKUq6gxOekWgXh-LMNekQ4oqvbpiG2q1J-yXrWybTRAvdkG1VmqcLOp0NuNZ0sLrudlF2C2a1e0S4dbj31JY-rXd9bhgRbFH3S290qba7kSuAAZvFF2VOlKE-NjpdnSFAtKrUYERTJf1uZs-8dFLyN0fZ2k-U-OxywEFb_OwhqHQlDN5Bpia1BYe2au7a4wWPe6heMJofPcmrZhDpzDkxp_g6MWOkjGR-MTle1qWmwSKhedD07RYdYpvYYww0wVkIwZAX_QEM6mL35CzrKLc2K1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
پیروز قربانی: احمدرضا عابدزاده و ناصر حجازی از لحاظ قبال اجتماعی متفاوت بودند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/96057" target="_blank">📅 17:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96056">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekhjmqr7XanedVftLD2ISQKPswU6TxviQXlNGvWLnFkV06c8KIPVU-cNd2f6BQEfPmEMMkGlNC5-wJjNR7NlRJ3caRzx9rUZl8y_EtkY54H22ht8r34KbDluHaWXvRFyRM8d7XuSWeTWshP6zfwq8K01XvfGmLRL7c966r7FLi18XkB-6kMvqH3FiGL1jP6LNqHGPhBC-ixG0nDvr1iemlcGSmjpMIFZFBuhdhqvIhoEZCHfMUW_C6lyYjUrI91e9Tq_VLpyMXk_dUrptVGlW5KINMnW_StdVZwG4jjiU-Y3mO81FS3ObyCIyxDJjkLzpfvbmCKJNPIuTC9KyGG6-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رده بندی‌ خلاق‌ترین‌ بازیکنان جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/96056" target="_blank">📅 16:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96055">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKw_aC_vILnWhsrYMRHz-wR9ZuzqCLKdjQHSGTUU8EeP8vCE59IFnoEwpWeM9e3WmiiWQ85V2ZYbLKYn_N222gFENZh6z5H04e2oApAvyk_4YTniuVr7Ag-gmOe5i1iJjixZRuWt9caHMMagbIIz4Al6hxAhLc_qBu5YMge2Xz4wByxyvvdZGgkphUBXMxj9prc1m6pF3euvBUCkYje9k9OizSd1iwW1jN6KxafzpaCgwWCkF5fb7H6lzLi6jrSJWR9Bs7ZDiqoCL7I6ORFPdhO2SZ83dE_aIydWE6E87AlGDq-1OHh0R3Xz40CcDiCzUTSMIWcptpW7n0Jc5xhM5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پرجمعیت کشورهایی که هرگز به جام جهانی صعود نکردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/96055" target="_blank">📅 16:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96054">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_NqOQc75e9KEC78gJyYy82kNlc6gXWEzTA7HmvyFlTDDyJrxead--NttztLTYVBevxF5-kQpA8Upb2b_l_lDrI-EC0L1ZPBgHa6-90XFLQpH3mwJyWV2Serguwm4-zuTj5DlZ9iqZTsPr5zy95Sc_rI4Yr4qEPg_YBvSdsBO7fLfxioAYu_HbWY50abm4UWc5KG85JLbVqMaJ-b9RMnbLmpNMDMqOUOMAYZ38IghMR2QI2TNhViI19BsNhgZ7fDc2au5Yok9Qf2cdGEsk9YPD_U7uWD6Tuv5vHH043W5wI_IegpDLsEl3K3cGyj9Rkg0NUl0fEQasNbbKdCRpTTyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه همراه اول به ایرانیان با صعود تیم ملی
همراه اول در اقدامی ویژه برای حمایت از تیم ملی فوتبال و همراهی هر چه بیشتر با تماشاگران بازی‌های جام‌جهانی، در صورت صعود از دور مقدماتی این رقابت‌ها، یک گیگابایت اینترنت رایگان به تمامی ایرانیان هدیه می‌دهد.
در صورت صعود تیم ملی فوتبال ایران، می‌توانید طی سه‌روز با مراجعه به اپلیکیشن «همراه من»، بسته اینترنت هدیه خود را فعال کنید.
تیم ملی ایران، شنبه ۶ تیرماه ساعت ۶:۳۰ صبح مقابل مصر صف‌آرایی می‌کند. برد در این دیدار، صعود مقتدرانه و صدرنشینی ایران را رقم می‌زند. در صورت تساوی نیز شانس صعود از مسیر تیم‌های سوم برتر، همچنان برای فوتبال‌دوستان ایرانی زنده باقی می‌ماند.
همراه اول ضمن آرزوی پیروزی برای ملی‌پوشان کشورمان، تمامی مشترکان را دعوت به مشارکت در پویش پیش‌بینی «جام‌جهانی ۲۰۲۶ در اپلیکیشن همراه من»، امتیازگیری و بالا بردن شانس برنده شدن مجموعه‌ای از جوایز متنوع کرده است.
http://mci.ir/-VK6ZFX</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/96054" target="_blank">📅 16:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96053">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffafe3e9dd.mp4?token=nJpZ9y8RXRLkhSOnW_AcjL86Nr_c3hyuTMLch8VJEduYIPil1pDT5ecOrpCyVm6w_M7G4Uprew4pm5AtuWMGn88n7UfBjlgLfHaFpO8XU5X5p1Bm9hT15WlgmQL_4ikpcOjVta2cLprDjYr2AXg8ldXQJXW3Ru7F5b0Kutiy4DpsuBtQPKigGjtHUQQTZ8RWAg-BEfrWV1W4g_JDQEMkp3ex7K5yic5SCJrMuyrhx4BTineoag-koTniiI8NcHtLUS3pSttEdtU99CumMPKPqy3ugaeDBVJibitlR9Alw5h98RlcCpGIBaJa_rTbQXynhyUn2o6o1_3t2m1KOkeklA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffafe3e9dd.mp4?token=nJpZ9y8RXRLkhSOnW_AcjL86Nr_c3hyuTMLch8VJEduYIPil1pDT5ecOrpCyVm6w_M7G4Uprew4pm5AtuWMGn88n7UfBjlgLfHaFpO8XU5X5p1Bm9hT15WlgmQL_4ikpcOjVta2cLprDjYr2AXg8ldXQJXW3Ru7F5b0Kutiy4DpsuBtQPKigGjtHUQQTZ8RWAg-BEfrWV1W4g_JDQEMkp3ex7K5yic5SCJrMuyrhx4BTineoag-koTniiI8NcHtLUS3pSttEdtU99CumMPKPqy3ugaeDBVJibitlR9Alw5h98RlcCpGIBaJa_rTbQXynhyUn2o6o1_3t2m1KOkeklA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
ژوزه مورینیو: دوست دارم بازیکنای رئال مادرید در جام‌جهانی ببازن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/96053" target="_blank">📅 16:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96052">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45704079cd.mp4?token=cFvzOxucVVEQe-ETPMDN1lqT7Uo0FL0LQLhi1BYE-BmKLsvEACvkTMvk5gYedQWdBtB-5gX0l-j0frLGYeKW7JYLGvbu-y3dUjo1UXRLTril1f4wnH8UIs0zGd5QlpxHglKGUakXYUWBrJdh-KhAkY7fcFoWXfP9ImOVL3lBQPg-52Tzz4RuNM-fqJ-DRqxW71JITIR7NCl0Xa22nT0WbHsN1LNQ2kCjsV12-yS6favGsAb7WkS78QLfGdNV9tiay5xpgOpa9V667TqS9kqp1ForxrRr0QMYxFHk_UFeKUIOahQ3awOevOB9CrPJ2VXZltlmSji_A8RgLHmziCSI7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45704079cd.mp4?token=cFvzOxucVVEQe-ETPMDN1lqT7Uo0FL0LQLhi1BYE-BmKLsvEACvkTMvk5gYedQWdBtB-5gX0l-j0frLGYeKW7JYLGvbu-y3dUjo1UXRLTril1f4wnH8UIs0zGd5QlpxHglKGUakXYUWBrJdh-KhAkY7fcFoWXfP9ImOVL3lBQPg-52Tzz4RuNM-fqJ-DRqxW71JITIR7NCl0Xa22nT0WbHsN1LNQ2kCjsV12-yS6favGsAb7WkS78QLfGdNV9tiay5xpgOpa9V667TqS9kqp1ForxrRr0QMYxFHk_UFeKUIOahQ3awOevOB9CrPJ2VXZltlmSji_A8RgLHmziCSI7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇧🇷
🏴󠁧󠁢󠁳󠁣󠁴󠁿
اسکاتلند - برزیل و دوباره زلزله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/96052" target="_blank">📅 16:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96051">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-hiRxG3gpnBRnMD7bjstafJWhfVoeM9iSCAaZ7TNWP3RQLoOuRjTT8woa-BFHebEhHNkU7V4d6WTRtZ92hPrYbm-akjZgvbd4JsGpiirDrd-gazKc3bfAz0j2XAusThxVxneXU_oPVRRylEHDeKceZLExEzL9vVa_jDp9nnVMa_xS1v-LV0rD-duGp3t9NoYCYIDTUYxhMI17JgZjdABBItOURaSzNZhS4HLBy6KlzZZSqgloqcMeJPI3eZ-8SXA2EcRXM-OKJKTB4lc69eJ2dCKg7B8W949o92E1r4JRriBR_pZ3Gd-4MxpjIOiPjb8wVqMhAZrYt6enWZRbtSWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتو ناگاتومو 39 ساله به اولین بازیکن آسیایی تاریخ تبدیل شد که تو 5 دوره جام جهانی حضور داشته و بازی کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/96051" target="_blank">📅 16:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96050">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vnu1SK-Jyt-CA2YGGjWb_WUw6aKjwnvxffdAvb9zyGpku8KKY8gYlES_zwVorSVUl-ziddWaXL95qgidpPO4ihUY-fQQTC_ZnRdM9pZR39IaXWqB_UzXNeZFsfPj9sY4BFAsrhV7WrQZzaEy933ADEU-rahz84EEpW9aKaK7IjLylev2Ny2sv1hiQbd8oIhJs-r2wtwMPOIoCKBlrOv9gBlEwt-yHo45RTUNx6YPjO7aBhs_WhtrMaciBBG4BQMY_bJMNhJXtRElBnUOPrtEmM8pvp6KLH8SqyOZgHw0eFCJMP_rFtjfGX-DprmFEIpQ3rCd-ntX19JnBkdNgq-9Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
💥
سرویس‌های مولتی‌لوکیشن موجود شد
💥
🔝
🛡
کیفیت - سرعت - قیمت اسثننایی
🦸‍♀️
❤️
🎁
فقط و فقط گیگی 8,000
10G
▶️
80,000
👑
20G
▶️
160,000
👑
50G
▶️
400,000
👑
🔥
بسته ویژه:
⭐️
100G
▶️
600,000
(فقط گیگی 6,000)
🛍
حداقل خرید: 10 گیگ
📍
لوکیشن‌های متنوع و پرسرعت
🔗
همراه با لینک ساب(برای دیدن حجم مصرفی)
👥
بدون محدودیت کاربر
متصل روی تمامی اپراتورها
🛜
🛜
🛜
متصل روی تمامی سیستم‌عامل‌ها
❤️
🤔
👩🏻‍💻
جهت ثبت سفارش و خرید:
✅
@Trust_VPN3
تست رایگان هم موجودِ
❤️</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/96050" target="_blank">📅 16:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96049">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VweBvNy4ryHIRtuTGhWF3toABAIbaTgFiUJjlmEIiv7kTrtKIqSDgrFsJt5WQv7qVC_eCR8Uq-_mRxSukkkywWHoWxikAmCvpjfHhzyBQBAJJA9TrAEiWgzz-WeleZjB2w6uOQiusuLW1sdfAfGRwbe4dhvZtt2Et49d9Av8hfmqWMqQ6uaZAztUUR_oPDOf8JWR7NoDEwTIf2JIhOsWl1km6YQ0n_MLNDt5DtNpLFOEGHWdOoq83hx7yWX1lI7eYE_ZsmBLchCVrCp3bsyy1_vnw4yjkaJEVu5apgtscmxpeE0-cJQ17HUKhyf0u7H8SbmDQ2fJgywFMqvSH4AdhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جدول گلزنان جام جهانی 2026 تا پایان روز شانزدهم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/96049" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96048">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sr4ww5sBFuq-rXBGBe_rrjio8os-Vt0UNY0PsCeCwvB98RZoGUvsJwpqENFWJ2BwWuiFbIm0UoBetUA2M9EoIao5jQ8u1gZosfLh0MkcIjtO9chFudqVBzDmG10nljKG54n81RmXFuuimy3na0jhmQGbncbZ_MFZ8upj0Go-hrctOWWLhliLxNACZtkCoUbYmTUix76ZzvjCLR7P9IsQ74axOvx6rDcKueCIw7rMN38oiUtQmp0jsFW8WzxwucCdInk6YfXdRs-M_4QCFLpvKu-FzPILeUgWVzHl-IMzyrOV5s15J5086AqANrSiF1o8mTp8Kv4zd3PZu3-zBIViNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیته سازماندهی جام جهانی، هتل تیم ملی مصر رو با پرچم رنگین کمان نورپردازی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/96048" target="_blank">📅 16:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96047">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/96047" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/96047" target="_blank">📅 16:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96046">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=PMMc2Nctw0GcoyrP6aOGxU59fefW1LyeBTVS8lro4QJMKm9dG2kHQxIktfVSCPPiiBLhPDXshYDnyqDZETLi-K5rBFfHXXf8HNUtyz2l_cSvLLIfLOHsMlZ-gfXt2pDgWOw5ifzI8lbZuyX1eW-tSXnNe5MGkvTbOLUB3giV-oKKAgof2Ffz3IJdTEc4B0mUyyWW-9ZxgrtCCg7frPxeamSHWwl5jqUID4-ysr02eWbZYzupPfMVaoNt4TOlI3J6yby6_Om6jX0O2l8tJ4u9PXHqIx0v6fdGowcnDjKR1IBINy9k5vRnwB4pkKpCDy9nTQZk2OPfEj3QlOfEeI3dlC6bmYClwXArweG4pJTpZugnVwJV7a3STV-vsNZK-h58x2PZsBWEijzis63C7qtprDjha5Lw7Al8RIn_qylsVH_MDWQ6RtGiKdniUenZyhQb2BPAphA5VTccidlUrqIOgIFcWaqPPehu37ldi55A7hoXK_1ADq4dYu-2GFARjlYXN9X64awIlskk2p1Pw_nUnwhPFEkLzNlMJMvT3dDHmgD39FNCDWIooPfJt4061PqJIyt_Uox_tDPqSsOAHv3WaLOPw336lA0IH-bj2m2_9WXvRddDpopU1uNniuDmyi2s5X83GQI5D2DwYaW6f9hfhr865Wf6aX-7Rg5d-mpGWYM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=PMMc2Nctw0GcoyrP6aOGxU59fefW1LyeBTVS8lro4QJMKm9dG2kHQxIktfVSCPPiiBLhPDXshYDnyqDZETLi-K5rBFfHXXf8HNUtyz2l_cSvLLIfLOHsMlZ-gfXt2pDgWOw5ifzI8lbZuyX1eW-tSXnNe5MGkvTbOLUB3giV-oKKAgof2Ffz3IJdTEc4B0mUyyWW-9ZxgrtCCg7frPxeamSHWwl5jqUID4-ysr02eWbZYzupPfMVaoNt4TOlI3J6yby6_Om6jX0O2l8tJ4u9PXHqIx0v6fdGowcnDjKR1IBINy9k5vRnwB4pkKpCDy9nTQZk2OPfEj3QlOfEeI3dlC6bmYClwXArweG4pJTpZugnVwJV7a3STV-vsNZK-h58x2PZsBWEijzis63C7qtprDjha5Lw7Al8RIn_qylsVH_MDWQ6RtGiKdniUenZyhQb2BPAphA5VTccidlUrqIOgIFcWaqPPehu37ldi55A7hoXK_1ADq4dYu-2GFARjlYXN9X64awIlskk2p1Pw_nUnwhPFEkLzNlMJMvT3dDHmgD39FNCDWIooPfJt4061PqJIyt_Uox_tDPqSsOAHv3WaLOPw336lA0IH-bj2m2_9WXvRddDpopU1uNniuDmyi2s5X83GQI5D2DwYaW6f9hfhr865Wf6aX-7Rg5d-mpGWYM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/96046" target="_blank">📅 16:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96045">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d15632d71c.mp4?token=VlpjbFr-10aHMc7IfgPlm4QJ46ZQrYEkuB73u-Q9UaQ5EkyGvrJTCSK18IyagehE5FQxEscnSqZLnhs-7irrnQFNMPFBEvFDHVLy0B6g9kpfajle4TnzkoA27EEH5Tx6AwuzH0X9rwVNyNJj1DsqvDOQ7P62hh-1eU4MjG4bCjKQFigK96vp4Iqael2LSgQaMWwT0EQ7gW8njoeo3G6M5tLBZviNosp-hgxtEezB8p51Ay2mLTAb4HYSZibVfqFSDkNssjmCU7F5BvdC5qrX_cmFBdAOi5oJKpXwRo_tdI7FSeu9wQ0EISef2E6sxbni1bPAWTMK2Z8qI4tjz2lLHoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d15632d71c.mp4?token=VlpjbFr-10aHMc7IfgPlm4QJ46ZQrYEkuB73u-Q9UaQ5EkyGvrJTCSK18IyagehE5FQxEscnSqZLnhs-7irrnQFNMPFBEvFDHVLy0B6g9kpfajle4TnzkoA27EEH5Tx6AwuzH0X9rwVNyNJj1DsqvDOQ7P62hh-1eU4MjG4bCjKQFigK96vp4Iqael2LSgQaMWwT0EQ7gW8njoeo3G6M5tLBZviNosp-hgxtEezB8p51Ay2mLTAb4HYSZibVfqFSDkNssjmCU7F5BvdC5qrX_cmFBdAOi5oJKpXwRo_tdI7FSeu9wQ0EISef2E6sxbni1bPAWTMK2Z8qI4tjz2lLHoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
ارتش هلندی‌ها در جام‌جهانی؛ حقیقتا پشماممم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/96045" target="_blank">📅 16:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96044">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkRzx2NJQ2-7MEluArPzGvpzinnGLLQBxiVTuF_O4f7zFvWBgZLQGgMYLUHmO_BdrP_wCRkDsYcfKB6_DlwOvYhYPookvGn4JA658vZlC9SnQkI7QMiXLz4lcND2cJ39wf3WwzkXjDdULrRp59LLx5FdTenIGL1jWkFsI_8blZauD92nuxrYNvove2WEFs1pGKhG_ZithBfSSTeSKREQJZ_En8WDbphTNjJrY-RSpEvd0zWf6pf_XWFd0oa09TIxRC3DOYeaep8juDXzYp0p2yz-ntJ9GgrEL2H90589lZxU450s9Fm3o3LyLvCBnr_GyS3EeWSstDfSfg1KgphDIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
کومو با رئال بر سر خرید دائمی نیکو پاز به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/96044" target="_blank">📅 15:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96043">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7trhZmdNzQOrDZrxK8nQ-v4bfQ5Y8YYX7HHpImLN2al1J6OCdH-X6Hd2DIRj0NcL2KSTvbqJLpBI0JIUiSlCoP2Zo2rGa1kpufX7GErlmkBMDE0XlnSM8fLMc_oUMaKSJ_7wvsWtpq3YsBPdH2WdgVIupaS0KjYAFZEqcr3wVG0W68SA15PZduxn1dVjVdS13EQ95QTiTDAipTAgLb7zt-ykowNeUeOX_8q4sS6mBnT7bGa49vh10VuX0CNjTP2pR3PWXSWhIcGYkq9HFhd7RJ5K7IGKX6wOaDScpl5amroLH28BXlSSzt_HD5BEOHGf2ywGrco1yawndK6q6l7fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بازیکنان کدام‌تیم ها در جام‌جهانی گل‌بیشتری زدن؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/96043" target="_blank">📅 15:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96042">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1pAfgFYvEqRsJbtgVXVo5GQA8XVP7cniwsCKQnyKlF93KgFImWtX0bO-nzK0jg92atH8eLgs9skqDc4pD_UaTStXA2kBeosA-4kWqxtlZ1CXHFwVv4LftRnREuwzJPfV-qnUfy2T4017k6EUS2gYkIIqUHgNzl-Hrp7lFTe-47qVjIICJcQ5Gj3to1oYld11lfZSXKMBtDvMli5q9Ej_gNukg27av3qxqz0aNyaffV-tnp9SsXQmmdzVaxM0fovfABF0l3zhdijZfmQRYY8XZi-P-9SYyxBn2Sx9eP1vOwfaVt1jriUVchMgP5BHTJjsyUj3Ih8EgCehkjlGHL4tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏆
🇧🇷
تیم‌ملی برزیل در ۴۴ سال اخیر همواره در دور گروهی جام‌جهانی صدرنشین شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/96042" target="_blank">📅 15:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96041">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c2067f79e.mp4?token=gIT3tEmQAXBzYmHID0dK0qD4mcJdethid-h4x7dYu37cVpf7A6dx79PiK4JO2SLzy0SqQpuAzqTaRaELnL_HEYyGRm9XXRJsjcJ96kdhBz4mnZWiMFypk_zdtPS7hlTkw1Xi_wiPMc97ZXswBExUg5y_DFuhTBUTkilxRvLJ-8Tmb25p6szCeabDqlSOMRedZL8Y6UHz5_NqbVKqY2ZXffTCIoIST8UMS5Xg_ztB6r8nmudaRun-lkLjHmH4se2t3_gpIqfqzlJhGxdFLcW4f1A5gSaSJSbAm8Orm3mySHFYbWF-qBqFMrnJafWhOmZWtcDUaJIqt4nmasazldJzsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c2067f79e.mp4?token=gIT3tEmQAXBzYmHID0dK0qD4mcJdethid-h4x7dYu37cVpf7A6dx79PiK4JO2SLzy0SqQpuAzqTaRaELnL_HEYyGRm9XXRJsjcJ96kdhBz4mnZWiMFypk_zdtPS7hlTkw1Xi_wiPMc97ZXswBExUg5y_DFuhTBUTkilxRvLJ-8Tmb25p6szCeabDqlSOMRedZL8Y6UHz5_NqbVKqY2ZXffTCIoIST8UMS5Xg_ztB6r8nmudaRun-lkLjHmH4se2t3_gpIqfqzlJhGxdFLcW4f1A5gSaSJSbAm8Orm3mySHFYbWF-qBqFMrnJafWhOmZWtcDUaJIqt4nmasazldJzsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
▶️
خاطره بامزه مرتضی تبریزی از زمان حضور فیروزکریمی در ذوب
آهن:
‼️
سه روز مونده بود به پایان لیگ گفت تیم از نظر فنی اوکیه مارو برد ویلا یکی از دوستاش تو کرج باباکرم میذاشت کباب بازی می‌کردیم عشق و حال بود کلا. فرداش مارو می‌برد یه محله پایین شهر دیزی میزدیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/96041" target="_blank">📅 15:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96040">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OINFAOTp4hsx8fCZGEBh-2ygqNdbuxsdiU-dhxOwj2hlJS-zRR3fIOvmi2xOvM4EwWMeYELWI-AiAY8609TrDYZI-N2n3tIrobbaDz1njs6BwtjLpewXgwh0lyDejNft1xrycw269gzVa5LQAn8b41s2KgvBoG_xaV1Cejpwlo9oLaLOXR1vSSIJj3Y2SIYkHhxjqJHlxE1NlYgrC4oGdQ04x1Gszgj8XOeiMG5TJCX5O_t2FXDp9JVIouFLEZg0m70uraorbfDNaGZPVpCK8rLacfuQesZx3G9lPr_4pK24Je8vT_fju9IQAUS7iTNLyuZEFIO8RpB6aobBrTXAEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فنای تیم ژنرال رو ببینیم.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/96040" target="_blank">📅 15:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96039">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZISQjxR4ZSO7iPFhR7rUf885mbSYbrZKW19rEfmd6Gtj0f4MJrxW-ip53ZJaXEst8rtqAG0cI1yXG1ILXkAA3isCsXx4dqyKnA7DpBj4cWFCBZUDrc707LgAhZCnnGWoByyVl8QxVCYEDszRYNvAB7Eex6UfebkXd8E2ZOz1spBarvbdO7NPXFaBu_RWf_CHU2zF46xd8ieuDNzDych9VHPM_xUksRS8uUknoMf-uM4yYoeTp8RLb5fWGJTFYaaaak373ckfZ6Tsapv7fCzOmjJlUXhOeePi2wneSSy9yKbyT4bR01fU0egTYe675RnZY-UlCTx8JT-dqlREld8mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇧🇷
ادر میلیتائو:
تیم ملی ژاپن همچنان در حال پیشرفت است و در جام جهانی ثابت کردند که قادرند به مراحل بالاتر بروند، بنابراین باید بسیار محتاط باشیم. آنها هرگز از دویدن دست نمی‌کشند و انضباط تاکتیکی عالی و بازیکنان متعهدی دارند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/96039" target="_blank">📅 15:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96038">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74737ca0a5.mp4?token=JNLHkNq0AjAt69kBcBAgKFEuKW4zo6BCPlNJnn9-9ROophSaBr_RXN29IxmTUb5_jpxtUS92nRTSkjz_ixYZX7n4zddxtKlzOTHZNeE3eKO7-EPDSBZXyZNXLmWoPj-YMrFFtVAKZ7PTA-y-lqcOlxQ5zonOaYbCSW6rM2h11lv7ehRWM8ZMej_2erqPIeFDLXfrZ5QIzbWvKVsLqGC56LZ_AdJBarPN82UUkGz75U3rmwJRaB5c535k-t1ASVRYrMXw_DcO-2BVRXvJLx8QCjfFldsFRdctKfxA-e2y6Y-ZF_RMBtk_lgbrXpZSlFo-SsIS1f4yj7TTB9oie4Jnfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74737ca0a5.mp4?token=JNLHkNq0AjAt69kBcBAgKFEuKW4zo6BCPlNJnn9-9ROophSaBr_RXN29IxmTUb5_jpxtUS92nRTSkjz_ixYZX7n4zddxtKlzOTHZNeE3eKO7-EPDSBZXyZNXLmWoPj-YMrFFtVAKZ7PTA-y-lqcOlxQ5zonOaYbCSW6rM2h11lv7ehRWM8ZMej_2erqPIeFDLXfrZ5QIzbWvKVsLqGC56LZ_AdJBarPN82UUkGz75U3rmwJRaB5c535k-t1ASVRYrMXw_DcO-2BVRXvJLx8QCjfFldsFRdctKfxA-e2y6Y-ZF_RMBtk_lgbrXpZSlFo-SsIS1f4yj7TTB9oie4Jnfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
▶️
وقتی الگوت لیونل‌مسی باشه بایدم اینجوری بدرخشی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/96038" target="_blank">📅 15:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96037">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltiv-Wm1WD8IZ8x662M3TmlGICusn4t0iAzms8HTaUmzfBFPKWrfx8GT0z8YoWC4_dZF9xKX2J4pnL6q5jOxomrshisptg9dCAbe8g1qwNLuMRQ7pAojSOTq1W-kuioBYAF-qzpLAFDPgmZiHDBATyye-xV4QrBYUhXO4NxQQ7kcWA5jKN9n5wQkSs5GoX2qtpmGN_zneUpEKbESTU4dxfLq45w2DWsSIDzLGRKJPi0R-HDE4J16tBQca0ygLh-pj4jJ6FZWvFZjZIdxGPRhucvzgqdot0ydJeQai0fvB85-2c7y5tweIZkYKxBPNgHZF91g3KgTqC5XWkJsg0rV_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
🇵🇹
مسیر مراحل حذفی آرژانتین و پرتغال با توجه به نتایج فعلی مسابقات
🇵🇹
پرتغال
🌬
🇫🇷
فرانسه
🇪🇸
اسپانیا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🇦🇷
آرژانتین
🌬
🇨🇻
کیپ‌ورد
🇪🇬
مصر
🇨🇴
کلمبیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/96037" target="_blank">📅 14:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96036">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
📊
🏆
نمودار مراحل حذفی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/96036" target="_blank">📅 14:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96035">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d3c29823.mp4?token=YMZVrh0_JKKQpAAgJCJinY-CGOC-TamI9XBu_jsQqoBA3nkZHfcr_uvEF2X4GsYyQIQrqcswbi_p6gT6_w39V4gLVylJVOtC_lTdlTeccfhSNAo3UemtWgTwxAiBlic0zbTzFl2nq8VFpNmGchKk499pwYgEoLNLXfEhAPZ_i90bLdqRMxMdq1V3NCLAT3jb17FmC53BhZ3NKOKl2rdnwv1hfXRQ12eHZAXRshOf0wLV85yteCV7JPwN82sWg3iwUSvQisO9_4Y12wAlAnfbZVEs3FdA69fCaRRk2l_QNltf82SVvLHHxGQjNDsEyrCBSUrslF3qAqm-FSfWbakRXGCUPgDN8FJQ0gMarzWaF-B4QaClyNdv57qIbocNHpvFh_4fQbcPP-SPR8RvkguJ4Za-btu-AACg3wxINu1iWnjZmhlRpmoyGqXGh5tAS_Turv0uTgIstOTIlEmYkUj6GXRg26LP06gH8u1PZDIELsKRwieQ_Zl5jym4xR_s7jAmiuVfCIyq8YqgHMzl9NcK8e-GwKTGMDpVM8U5tUNdl12u4-WaXgSklUa95uPpZDhfNka_ysHyHANacpzO237Tp0wPgJc4YtXNo8RKcFarF47J9PX_1AUTAHuyAkZGDbM-SyD7Z2kzGYQWxsZNlQQz_k28sQdSJnGempEjmSIVzPY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d3c29823.mp4?token=YMZVrh0_JKKQpAAgJCJinY-CGOC-TamI9XBu_jsQqoBA3nkZHfcr_uvEF2X4GsYyQIQrqcswbi_p6gT6_w39V4gLVylJVOtC_lTdlTeccfhSNAo3UemtWgTwxAiBlic0zbTzFl2nq8VFpNmGchKk499pwYgEoLNLXfEhAPZ_i90bLdqRMxMdq1V3NCLAT3jb17FmC53BhZ3NKOKl2rdnwv1hfXRQ12eHZAXRshOf0wLV85yteCV7JPwN82sWg3iwUSvQisO9_4Y12wAlAnfbZVEs3FdA69fCaRRk2l_QNltf82SVvLHHxGQjNDsEyrCBSUrslF3qAqm-FSfWbakRXGCUPgDN8FJQ0gMarzWaF-B4QaClyNdv57qIbocNHpvFh_4fQbcPP-SPR8RvkguJ4Za-btu-AACg3wxINu1iWnjZmhlRpmoyGqXGh5tAS_Turv0uTgIstOTIlEmYkUj6GXRg26LP06gH8u1PZDIELsKRwieQ_Zl5jym4xR_s7jAmiuVfCIyq8YqgHMzl9NcK8e-GwKTGMDpVM8U5tUNdl12u4-WaXgSklUa95uPpZDhfNka_ysHyHANacpzO237Tp0wPgJc4YtXNo8RKcFarF47J9PX_1AUTAHuyAkZGDbM-SyD7Z2kzGYQWxsZNlQQz_k28sQdSJnGempEjmSIVzPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مداحی محرم با موزیک واویلا لیلی
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/96035" target="_blank">📅 14:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96034">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOrJxsPhFvnr29g_HY_9oZfq6w10eEiHOnx-dnF5-FcaTsEmDHhgh4gCMf0EwXbv8TIrnwKEjT90ER1iTddmdSz_8CGUx5bGVqgGz2wRGaVRFXrFmjsxNGix5ZLJLyKmWl6Yg4i7WhrjclTIdHyKHDrbLPY7G6rrzbkpBtuehUd_Grl5h_VD8NxVIJshcqFmxYt0Dl_v5QrfEv9oH9Of-HvYHfeS0VygHmlillrLAnruX340ei2Dz0wpfUW9lXoyGki-pgh3afd0pxC3tZziK1OuVhIay57yrWqU__NXE8qLdooUEuyHUCbNXxqpP4d5N_oVao_eIoPMvJe4Tk2tWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه هالند و امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/96034" target="_blank">📅 14:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96033">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=h842_sjCGSecY8GkKmkQTvqN9Qq8vMWbpGW20dTPT3L9ALaW0L3uxAp7KmdN2opKTPhpJqiMV0y0QnHWxdy4vrERocUSDBOEk3nRPhZnLnytSE6uvQuKjg4QdP8JqAcCn73TSuOzsX-GHat_JURHAMlg1Cb7GIyoqGyUdAG4XlgJeE2C-qSDMIyHCt3NDX56jfK-gxLWEHikwi_yds3lErb-lSDhkvFMkrx-uPmCzoyK38mFeDgd-Mw4AtO-qHZruvSnh2JGravcPHCVK9uT6J80TY8uc7H5iJPiHjyUvnRHlGbTl9DLBM4c199b6j7BjuhoG00sVzZtfH2MezPwIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=h842_sjCGSecY8GkKmkQTvqN9Qq8vMWbpGW20dTPT3L9ALaW0L3uxAp7KmdN2opKTPhpJqiMV0y0QnHWxdy4vrERocUSDBOEk3nRPhZnLnytSE6uvQuKjg4QdP8JqAcCn73TSuOzsX-GHat_JURHAMlg1Cb7GIyoqGyUdAG4XlgJeE2C-qSDMIyHCt3NDX56jfK-gxLWEHikwi_yds3lErb-lSDhkvFMkrx-uPmCzoyK38mFeDgd-Mw4AtO-qHZruvSnh2JGravcPHCVK9uT6J80TY8uc7H5iJPiHjyUvnRHlGbTl9DLBM4c199b6j7BjuhoG00sVzZtfH2MezPwIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
💍
امیر قلعه نویی درباره حضور پرچم‌های رنگین‌کمانی و برگزاری مراسم حمایت از جامعه LGBTQ در ورزشگاه سیاتل
:
ما اینجا برای فوتبال هستیم، نه مسائل دیگر. تمرکز ما بر روی مسابقه و کسب موفقیت است. درباره موضوعاتی که در دین ما ممنوع است و وجود ندارد، نمی‌خواهیم صحبت کنیم.
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/96033" target="_blank">📅 14:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96032">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkUYWhBS-WRmqrY__yGxAB4_2pa-xbawxhJBzXLaw7HDpVmueO51zKgSmmUWTrG_xcb3BuXK4e_1mwjEB7LCSt7IbxyoVWpNG4clk0Ee4wSAnp_CHyT8s4nqfrHX9zAD-FAX89JfsGvscCO8uqROP-ViJvbFaXsbfmAQ2AcVyCv8x_t2Wh8-6wXH5V3bQDuAVDxkWyamT2UWRJ0y89T3RuzsN1PZ4QSO26odxjo0ajk75eymVHaq9lUsWMd8xY74sKFKO533ZdNcygtMcrfsJkozw5a6O200ncJqMTQqNCeKv_aOxCEmKqjf04Kq7kP8FD-vb29oCEpbVDHO84vHDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇪🇸
🇦🇷
پدری‌ستاره اسپانیا: دوست دارم در این جام با لیونل‌مسی روبه‌رو شوم و در نهایت پیراهن اسطوره را از وی بگیرم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/96032" target="_blank">📅 14:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96031">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21833a49a4.mp4?token=p-mv2x7yYnZYZtEdEJuQxt2Hd4167QYEQ58XJt-filpYSqubGouxbGfb2rgFNSG1jg18e9lnjNJNR2lzQ8jSJKk1tSe2SGYWK4K60zxcOB8XDU8Oqa2y1JMZeIaqbTR2kgbbP2imoGz6rK6o5fdvIVoKDXIm2duoai8SOeUFEYH-8UM-myoM5G73TWbnrHzh5jgmN7WOCaCN0SND3mZxPlIuOJeu1gDAwClEYrhUUt_CwILvfYjeu3g540dfkO3gi4IqZ6IOaC9JnME20ZDpO-1CwENurjH2JqYf7SpRmiv_UrKr8wgz8nIeAL5hHgxaBQlwLeCBi1RI1BbILXVo0IRAAtmKaN012KVZVTYlEzEic9Kw7hq687KAPKFCl_JePEh3ak2xSNmYDvuDnLnjgtQ9bhi4_R7rRMT0NokX5Z1wsgvk5bdfPcUbl9mVKDQi3xnwm4QXiry--1qz-lrKNtdIppvDM8V2cYPWhxmN6P83H0FZigmJaJIlCX_vLd-pVzn_Qj_aZRaaeFpsf6IX90B-pznD_Z9uJ6YgWw6Za7VpY9E3qbUi1RfXJJc-U-Th12h4s8OKd4tc0hQ7x7SWmiOZk8t2tBWaNO4o3oH03uQcNo-Pt5IoD13-SDzszm003CONNbW7UCzWGmcHmTkZ65ZWHQvezLfFCNw9l4dWirY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21833a49a4.mp4?token=p-mv2x7yYnZYZtEdEJuQxt2Hd4167QYEQ58XJt-filpYSqubGouxbGfb2rgFNSG1jg18e9lnjNJNR2lzQ8jSJKk1tSe2SGYWK4K60zxcOB8XDU8Oqa2y1JMZeIaqbTR2kgbbP2imoGz6rK6o5fdvIVoKDXIm2duoai8SOeUFEYH-8UM-myoM5G73TWbnrHzh5jgmN7WOCaCN0SND3mZxPlIuOJeu1gDAwClEYrhUUt_CwILvfYjeu3g540dfkO3gi4IqZ6IOaC9JnME20ZDpO-1CwENurjH2JqYf7SpRmiv_UrKr8wgz8nIeAL5hHgxaBQlwLeCBi1RI1BbILXVo0IRAAtmKaN012KVZVTYlEzEic9Kw7hq687KAPKFCl_JePEh3ak2xSNmYDvuDnLnjgtQ9bhi4_R7rRMT0NokX5Z1wsgvk5bdfPcUbl9mVKDQi3xnwm4QXiry--1qz-lrKNtdIppvDM8V2cYPWhxmN6P83H0FZigmJaJIlCX_vLd-pVzn_Qj_aZRaaeFpsf6IX90B-pznD_Z9uJ6YgWw6Za7VpY9E3qbUi1RfXJJc-U-Th12h4s8OKd4tc0hQ7x7SWmiOZk8t2tBWaNO4o3oH03uQcNo-Pt5IoD13-SDzszm003CONNbW7UCzWGmcHmTkZ65ZWHQvezLfFCNw9l4dWirY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
▶️
🏆
توضیحات هوادار ایرانی برای جایگاه‌های ۴ نفره و مخصوص جام‌جهانی به همراه امکاناتش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/96031" target="_blank">📅 13:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96030">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c892433e.mp4?token=I-HMSYLYHzZwj2YaKRt0kRvQiL-SI_hPWAofOHWpYgIwbA5MsVwpKi8LLcyE4U54FZt-pyJPJPMlORSdw2KE6EzHJTeroRvBkE6etP1rmDhb4Y-0n67lWZ3i6eQabqDRQPYtm5skpeSerEVuGJcbxjXj3sVVRKvn74-J1WBS4G_bx9FZbpq_svBRQ3tQXOIoXyGa6MHhaFRMqe2-bXs4lKG4faw0IlSJ-gc6d5Euck2PvbeEfX7rAX38ncrzZaPDo9i0LZhlopd4lYmkGA8RAcwpYmhwvJ-qKs5eK1BJMp7g87k-1HX31LWPqgys4BD7v4swJj3P1N-sq31ck_-AcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c892433e.mp4?token=I-HMSYLYHzZwj2YaKRt0kRvQiL-SI_hPWAofOHWpYgIwbA5MsVwpKi8LLcyE4U54FZt-pyJPJPMlORSdw2KE6EzHJTeroRvBkE6etP1rmDhb4Y-0n67lWZ3i6eQabqDRQPYtm5skpeSerEVuGJcbxjXj3sVVRKvn74-J1WBS4G_bx9FZbpq_svBRQ3tQXOIoXyGa6MHhaFRMqe2-bXs4lKG4faw0IlSJ-gc6d5Euck2PvbeEfX7rAX38ncrzZaPDo9i0LZhlopd4lYmkGA8RAcwpYmhwvJ-qKs5eK1BJMp7g87k-1HX31LWPqgys4BD7v4swJj3P1N-sq31ck_-AcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متن حماسی که در اتاق همه بازیکنان تیم ملی نصب شده است
🔹
در تاریخ فقط یک چیز می‌ماند، آیا ایران صعود کرد یا نه
🔹
چند روز دیگر هیچ‌کس از تعریف‌ها و تیترها حرف نمی‌زند، همه فقط می‌پرسند آیا ایران صعود کرد یا نه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/96030" target="_blank">📅 13:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96029">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2Tgg7vRpMspoNi27Nq5lA0qNc62xf8iGxvPJaFfpFuSYMtQbOhqINPxfXb7HjgZVh_vPNHX-meDxZUErgnyRgwSmLeykf16X8NLI5FNaEGzyQos1j3FucOhKBwbXLKdEVgyoPtxXtMk1_z7TXoHlVFXyZNcdmu834tn71fLzIm37wTwunHJ1pA7S2osAinWrx5FiTmeq7Ubbj8zLuuCXn7qZ2kXrMbf6ErIsj9BVmXUnqo9goFcP2w2EwtIpBd5Af5zrANThpNolYhrpNb-X-HKAucviVCfHiXja3gaI9eXYXOJ0WnTKjGCHA-S0-Bm_JtNe5kPmaJ-D1gV8DTTTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇬
🤩
💍
حسام‌حسن سرمربی تیم‌ملی مصر درباره حواشی بازی فردا با ایران: برای ما حضور یا عدم حضور اقلیت همجنس‌گرایان اهمیتی ندارد و فیفا اختیار دارد هر تصمیمی بخواهد بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/96029" target="_blank">📅 13:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96028">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2RueiA0vEDLZL1HqtpI6FPEIjiMK6VCr1qlz8lEuTgMFNvU96NUiK655XtC91vYw-tBqL94u0zsL1vRq8Q2dPz8H7hBx79bi8ukuEaWnrAGgExghjOm3iVFhFDME6-zssJ6Wxsvm6RqPn4OPYAntcUPLypr0H_GBtMceaRDfYBUQ-N4cI8EmSYCz5f1D1MjNcq8tF-BHIlzBhaigK_eTK0h8mCn-xeVHJVAWsKZ_i6bn4MMPQHoSvN6FB5HvjAv8MFoBQfGH5Q50XvnOMNGAq0j-VMZLHCGKxIBboh_1kjb-P5CmWNx8Hu-hFbhWCxh0VJDIfABmeRl2-UcPbS5ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
لکیپ: مکسنس لاکروا ستاره تیم‌ملی فرانسه پس از جام‌جهانی با عقد قراردادی به ارزش ۵۵ میلیون یورو راهی چلسی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/96028" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96027">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3yL01rUGkE10V_hfHwEoMewH0ckxWy4UIvMONq4NOGWkARp7eHCf8AQwkIKKbL4GlyRbvT_eF_DPBQBxcZIRJOrIWGeWqMw7L4PGHud1zCopz7QU7-e_ho9URp0y0AxFSxbCaguxgGoiNosjLP0bfhAVybPoUXQ_cJRETrwYoKZmGhyO_cf6J0a5m-XXdOTEcTwNqZZlMh-zlr7CjcdUuNs67Te_lxcUDmsZonzoPFvShmTWL0F99iEUl0dKRtT3wObM0J7Bsr37HAwnD2HkOUK-ZoUpew8K25Lck8r59Dr2-npB2Hj3ABggzPKHoKFt6Dc4ThWEc8PNyqSqs5ujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
تصویری که لامین‌یامال از زیدش منتشر کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/96027" target="_blank">📅 13:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96026">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8aae82768.mp4?token=vtHN5kbsdjgh313PRheMFKDX2feXhDqMTHsyIdjACjqpIcP49cj6jxSA3RHtPIkwwm3mehEvWSysV9NFFZa7sx95b_HYyseA_xuCVvj_aNPeHBT4XEuoalR5pbhlndJwjSQ8-e00ELq9BqkYSd28oeycByfdOqGFkKz-9ouGfi12jpq-k9z-qShgVAYBDo1JVzIR5SVW0neiCOl-CfRCDpHcvTHzwQ0igFc-TaoWMTKVQfPqThJIwYY5x43K9GRWJfPFEgZBPqftmibJFKRKvcyrex_6-EkJrBSBMBAErORUil9OQeT8WXs2E6Mo26UU1jXGrTjCtVApWRgZKOc53pdjYNe4pthPlonbGnfk00gm5cr2EDkzJqT-qzwCd3hntQzCW0oTDTzJ_h5EA6fQkhLznUT8EduKMdXWXmdWaUt3NyAiIUfI7zrdqq8TJpGMR-ZeiS20PO0Gv4D5MTYTCCeb5C3hNS7s9LsQL95wIx9yxQfap3ruEx9_0sZpj0inAwGWia6JjkGo8BpVZt8GNgE2Hwwguw6LcjJrDk8q_d0CTHWzOk2lLnZGz1JiFIS76IoNY4GPgzn-WoHZFtr-MolvVPNaScXQoxAp3UtRYbO7_OEveF55iZfgrFszF21SzFd-Ho_PAajb9vBkXJZr0mHGzUguGO2g5B9NKGyWv1c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8aae82768.mp4?token=vtHN5kbsdjgh313PRheMFKDX2feXhDqMTHsyIdjACjqpIcP49cj6jxSA3RHtPIkwwm3mehEvWSysV9NFFZa7sx95b_HYyseA_xuCVvj_aNPeHBT4XEuoalR5pbhlndJwjSQ8-e00ELq9BqkYSd28oeycByfdOqGFkKz-9ouGfi12jpq-k9z-qShgVAYBDo1JVzIR5SVW0neiCOl-CfRCDpHcvTHzwQ0igFc-TaoWMTKVQfPqThJIwYY5x43K9GRWJfPFEgZBPqftmibJFKRKvcyrex_6-EkJrBSBMBAErORUil9OQeT8WXs2E6Mo26UU1jXGrTjCtVApWRgZKOc53pdjYNe4pthPlonbGnfk00gm5cr2EDkzJqT-qzwCd3hntQzCW0oTDTzJ_h5EA6fQkhLznUT8EduKMdXWXmdWaUt3NyAiIUfI7zrdqq8TJpGMR-ZeiS20PO0Gv4D5MTYTCCeb5C3hNS7s9LsQL95wIx9yxQfap3ruEx9_0sZpj0inAwGWia6JjkGo8BpVZt8GNgE2Hwwguw6LcjJrDk8q_d0CTHWzOk2lLnZGz1JiFIS76IoNY4GPgzn-WoHZFtr-MolvVPNaScXQoxAp3UtRYbO7_OEveF55iZfgrFszF21SzFd-Ho_PAajb9vBkXJZr0mHGzUguGO2g5B9NKGyWv1c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🏆
یه خانم‌ایرانی خواننده خارج‌نشین برای جام‌جهانی موزیک‌ویدیو ساخته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/96026" target="_blank">📅 13:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96025">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q0OswsK-LOXzIwHNbYhaiARRhNOGXQtU60Riv8O97HxTXJHbQxqBf3jhrmfYQy1UnNwqCQzb-3Z9M-CtUJSxdN4lZ0OO0yw-NqjWyIA8N70iB3539pfjUruPwJlV5Z6wKZnKdHSwX8lJxyFhknfigzEoYk90WPnO44xtH6QN8s_z5zF90d97ocJurc4heGFGsBLlvVrGA_sl2KdONJRRtMe2JO7pUrqqwPFmIF9LhJEG_CRgWK6XLrMRkysMq4n_AKuST-t48282NzaWP67Ry3HC3ixYX5lAi1N0fOCOzQxsea5esRBS1SWXb5tBaVYFbDRHHjCSAe_URBMA8wOzdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💍
🇪🇬
🇮🇷
وضعیت‌سیاتل آستانه بازی مصر و ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/96025" target="_blank">📅 12:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96024">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53bad2b136.mp4?token=kCJjJNznMprtjO4NQA1TaV_uTHWGZWkddRtkzUkWhJKrKD85f9JLJamNwk4LAvKxR-OqeM_yIz_3Vx_ZbU4esMVdXawiQkHpDi0cuaVlHwWxj0dap22m3V-wh-WtqhYGLB4SRFh7NLfjpCRvw2QK48uE5mMf1yh54P1ImBHYTeRmc-I5V_okWEP2YdHUZutOLcj21YXTIPkVt7Bm8sSG-lgpvarVa4wug_FXfIJDd22M6kpeGF1dyJmyQbjYvsmiyAMQTBcFcwmWXXZWwdbdeb5MuptKUKkcDrrVicK9lx40QOy--90FkBEC8_E6qbkuBG_djnHC9hTC_5YF7ao7B5oS0vFMI-o_uX80ZALtnBgzx0VBfGr7s3UVCY0ywyyR2ibzaTrK4YUKmGAiAPpb_EZuqokrYXIQ9b82O_0FNk3fIHMMVpVABIj7ZYEolMyWgBQwVHYjy01m-kFSkLa1BI-VSQKoyzIrBWjn1Dj8njh-ksFE67E7Qz2uN3x2WDqHchuVgplHztEGozwmTzlgeS3zOr1PZAtjReizXxlz_jROPvS-ofMaDhKjlhE71_ic1kSzDD6Qdu2EeuS6v4U8XFUCa8FZ-6T48DbzhCL8rnIZ66exLkblbhHqzj_rp4eWZqkxLbSFFWvZpugaP5zB8fE-6-AXthCYnuN3S4KJ8aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53bad2b136.mp4?token=kCJjJNznMprtjO4NQA1TaV_uTHWGZWkddRtkzUkWhJKrKD85f9JLJamNwk4LAvKxR-OqeM_yIz_3Vx_ZbU4esMVdXawiQkHpDi0cuaVlHwWxj0dap22m3V-wh-WtqhYGLB4SRFh7NLfjpCRvw2QK48uE5mMf1yh54P1ImBHYTeRmc-I5V_okWEP2YdHUZutOLcj21YXTIPkVt7Bm8sSG-lgpvarVa4wug_FXfIJDd22M6kpeGF1dyJmyQbjYvsmiyAMQTBcFcwmWXXZWwdbdeb5MuptKUKkcDrrVicK9lx40QOy--90FkBEC8_E6qbkuBG_djnHC9hTC_5YF7ao7B5oS0vFMI-o_uX80ZALtnBgzx0VBfGr7s3UVCY0ywyyR2ibzaTrK4YUKmGAiAPpb_EZuqokrYXIQ9b82O_0FNk3fIHMMVpVABIj7ZYEolMyWgBQwVHYjy01m-kFSkLa1BI-VSQKoyzIrBWjn1Dj8njh-ksFE67E7Qz2uN3x2WDqHchuVgplHztEGozwmTzlgeS3zOr1PZAtjReizXxlz_jROPvS-ofMaDhKjlhE71_ic1kSzDD6Qdu2EeuS6v4U8XFUCa8FZ-6T48DbzhCL8rnIZ66exLkblbhHqzj_rp4eWZqkxLbSFFWvZpugaP5zB8fE-6-AXthCYnuN3S4KJ8aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇲🇽
مکزیکی‌ها وقتی ورزشگاه نمیرن اینجوری بازیو میبینن؛ غرق در عشق‌وحال و مستی
🚬
🚬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/96024" target="_blank">📅 12:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96023">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🔴
🟡
دیدار امروز پرسپولیس و چادرملو ساعت ۲۰:۳۰ آغاز خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/96023" target="_blank">📅 12:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96022">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b381fab19.mp4?token=MBqVvWv1nomLfQK33p92BBr7AksrIxO-c-Zr_LIJM9iL48rnUzUui0xOtoiPF5wsN0OjvtQAw86t4HoD58jSmELhgB8PYVvUTeTaTYzSO-fN4DraN-IXdFEFS4mQy18n6Yyxsz6Jb90HbGX6HsslMbADHtEjCRsymNsh398R0UCDTLC_CtAPRG-YLE9mC6FJS_Ru0Zd7zNs6qSkwiZ-syjUIE5yAG4HRjmn3dgjvC3mi--5AGb9zoQ6PwNwh1tLdNEh48hs0Sj6tlZ1Z0cfj6nHFFgrDoND3KoOxtK9xXgEtpE4iMCvfHcBPGq9u_nq9a1pmeMCzRcMmVnHaO41anw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b381fab19.mp4?token=MBqVvWv1nomLfQK33p92BBr7AksrIxO-c-Zr_LIJM9iL48rnUzUui0xOtoiPF5wsN0OjvtQAw86t4HoD58jSmELhgB8PYVvUTeTaTYzSO-fN4DraN-IXdFEFS4mQy18n6Yyxsz6Jb90HbGX6HsslMbADHtEjCRsymNsh398R0UCDTLC_CtAPRG-YLE9mC6FJS_Ru0Zd7zNs6qSkwiZ-syjUIE5yAG4HRjmn3dgjvC3mi--5AGb9zoQ6PwNwh1tLdNEh48hs0Sj6tlZ1Z0cfj6nHFFgrDoND3KoOxtK9xXgEtpE4iMCvfHcBPGq9u_nq9a1pmeMCzRcMmVnHaO41anw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
✨
▶️
همه عمر می‌توانم کنار کروس بازی کنم
مدافع سابق تیم ملی آلمان و بایرن مونیخ بهترین بازیکن تاریخ این کشور، و یک هم‌تیمی برای همیشه را انتخاب می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/96022" target="_blank">📅 12:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96021">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5KkT22j3w2PzyLAjiEbVR1VurVeHFA3EslYcSMOxCg_dgMVfT8yoUUWfDIk4FsS4AsOAS2F6CME64OvFIqEeBcvIKFbli8jH_nWNr9acNpAlimuNx9B_y0U-4S7WYRZhX0gM3J3-9Hu_4ZM4VFFywCKiYeeNmYwnc2rAdcdww3iml4QtNGPhaMGvoujVrJo91yHazI0CQlTCIRg7u9W8UuiRtnyNU-A24C6-Xm4R-G7-ZxtAygA1JjKjI80mwCQkvJEDuneoznginWbdChv5JldU4rVwEfCMgQJ-YefBBIlR1TqvDJPPBJci_Lz1OpQdC1ASceixIn8rC2JLHyo_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
#فوووری
؛ آرسنال اولین پیشنهاد خود را برای جذب برونو گیمارش به نیوکاسل ارائه کرد. نیوکاسل به تیم‌های خواهان ستاره برزیلی گفته که این بازیکن فروشی نخواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/96021" target="_blank">📅 12:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96020">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871d57299e.mp4?token=tsJmw_gNeM46dNZedsfqnDFl-CPRaIiDgY_QNIVkeH4ojPmtBYigz9-e7IX2K88GWh4FxwxUBPJNgPrgWfCTr5WWaOERp_NTJJMJ7F5z_2QtdGZVji0QZreB3UpsBNCWWUzzWNEPHE6Kd8GOQvYkrDqVfYjX94_i5_hxjpWj4V0Kl3V3g6dfsGwEPpCqgAEitAwh5AUf95w7z-VdaUatA51oDLkQPDaf_XuU6qA4SavosxD4YyFZFfo8nc_mCDAda0qKVMDDyh_XORoxSdj8CXzIPVPVqhjGKAcSDzKfUEkQjJIKZpToUtrU0SJ9t37ksNCu3CaHOFaQgOgmgc6SRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871d57299e.mp4?token=tsJmw_gNeM46dNZedsfqnDFl-CPRaIiDgY_QNIVkeH4ojPmtBYigz9-e7IX2K88GWh4FxwxUBPJNgPrgWfCTr5WWaOERp_NTJJMJ7F5z_2QtdGZVji0QZreB3UpsBNCWWUzzWNEPHE6Kd8GOQvYkrDqVfYjX94_i5_hxjpWj4V0Kl3V3g6dfsGwEPpCqgAEitAwh5AUf95w7z-VdaUatA51oDLkQPDaf_XuU6qA4SavosxD4YyFZFfo8nc_mCDAda0qKVMDDyh_XORoxSdj8CXzIPVPVqhjGKAcSDzKfUEkQjJIKZpToUtrU0SJ9t37ksNCu3CaHOFaQgOgmgc6SRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
معمولی‌ترین هوادار برزیل جلو اسکاتلند:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/96020" target="_blank">📅 12:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96019">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwLwK1avN-6DGTBOtGqRlDZdIJBuZjTOzDA_xzkjnNkz_i2JNQ68KqshraNAqonDzhl9HN5m9OXXf5ZW_nNk9p0md6fz5bnoBcMOGtCghnZBWBR9Jz5xeW7uXGbDGAQRJC5mis6_kOMs17GdxRqvwEQV6LyMv2GUgIgkC6NH42WL3ONW3hKEooyMHEu96dMhNRR-iXmUJ0XuHD8oha0X_qE7sEw1F4SgPWfTGDNL2XdVVXPkhvjY5KYJwzpOSqxErgD50UKJi_bK3OijEKgqmjdXDnWV5S1o_V13Snr1UytIuikvc69RpDtd_fWknwiOHovu0QxUcMijSVe2Y5c4pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🏆
🇪🇨
پس از برتری تاریخ مقابل آلمان و با دستور رئیس جمهور اکوادور، امروز در سراسر این کشور تعطیلی اعلام شد تا مردم به جشن و شادی بپردازند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/96019" target="_blank">📅 11:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96018">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2CorgQPBwCkO95Mu3A8AF5mP9j2clHQ5KL8RGh19TU6bUdmxGsj-ijYneQMfOLlAGjViFybA210CId1CjQ_aJGYQ6NAdqOuZYCao8fhpYQ6lmlk6T1jksOSSWBf5UAxIsqWsA---wiN9oUq1bfQgWU2TYRZqhQ-JMrxut4XgUDw_uHMtim7d8zgempIj6J_i0wozwG-QPIRiiP_q4o59yMwwpMDIZdcpMJbKKu5nkI1gb2qLv_wxDE2RZJ7elFdpZMPkOxcBrv0YfEgNYXNxVO4TZqaH2uONCEg4vcZmUdKog6g1yDhV_TfNe6PM4n58ju4Tb2pwXNx0P6xzVI1WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇺🇾
هرج و مرج و درگیری در اردوگاه اروگوئه پیش از دیدار با اسپانیا.
🔴
اختلافاتی بین مربی مارسلو بیلسا و بازیکنان وجود دارد. تعدادی از بازیکنان از جمله [والورده، اوگارتی، بنتانکور] درخواست کردند به صورت خصوصی با مربی صحبت کنند تا به او بگویند سبک تمرینات و بازی‌ها را نمی‌پسندند.
‼️
بازیکنان از شدت تمرینات شکایت کردند که باعث مصدومیت برخی از هم‌تیمی‌هایشان شده است.
❌
بازیکنان همچنین درخواست خاصی از مربی داشتند که فردا مقابل اسپانیا با دفاع پایین بازی کنند و روی حملات ضدحمله‌ای تمرکز کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/96018" target="_blank">📅 11:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96017">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9ab104e91.mp4?token=M8qI1akyKYXkq1SJpXHbBsax6gxF5rxHXZRfDvdbLefuMyl29uDulnl68e_oUGDqG6L8UCtIGH2mi0DbGJR-eaoYUZ4iTMjcQQ8C2M47wZB-Q4cYTqfIVufGAOd8w8rqFNPSmnOAqm9kML7Acs6xiJdLH0cYvuy9DbvS8CjRYL_FI_LIiPWVzqC475sqNYDya_I3IeRrJLJxv-zGj5XbsC6Z5rfOXNNk2cAcwanp-xlI02I_NkVLX81N8G2zR6AI346RHjcRcijB5MKFJPk2U0eMpDIxGwJzNVVn6pLnMz5Qnm6Z_u1EZA154Ijfg78lebwhmXQmRXPxEztMj_RaoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9ab104e91.mp4?token=M8qI1akyKYXkq1SJpXHbBsax6gxF5rxHXZRfDvdbLefuMyl29uDulnl68e_oUGDqG6L8UCtIGH2mi0DbGJR-eaoYUZ4iTMjcQQ8C2M47wZB-Q4cYTqfIVufGAOd8w8rqFNPSmnOAqm9kML7Acs6xiJdLH0cYvuy9DbvS8CjRYL_FI_LIiPWVzqC475sqNYDya_I3IeRrJLJxv-zGj5XbsC6Z5rfOXNNk2cAcwanp-xlI02I_NkVLX81N8G2zR6AI346RHjcRcijB5MKFJPk2U0eMpDIxGwJzNVVn6pLnMz5Qnm6Z_u1EZA154Ijfg78lebwhmXQmRXPxEztMj_RaoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🎙
💥
امنیت و آرامش با حضور نویر
‌
خصوصیات مهم مانوئل نویر از زبان ژروم بواتنگ دروازه‌بانی که کیفیت کافی برای بازی در جلوی زمین را هم دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/96017" target="_blank">📅 11:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96016">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMHh4pueG38F0urFtz9E4nZIfuVlzoxFaPu_JWs_Lojteyt2_5IjQOPKovKigS14KThdwfl2c76M58lkwW9khwubZDJpmTR-jugs_hh47jv6l17mEgtIZ2SMLfHxNhs0us64VuJ9i30Ssx72KR_H32ja0MY4Ytf-zHJN6zQQ4QvpzdtCiKCg_1zXfJo6EgkNuIg0Ba-Vx5-ffIMwuQ7XCxNPJdBdsbV3bjMVrEjSUt66Wt00ip6P6suyU2Hl0bGyT2Tx7_hbCKord3KImCOTlWW0RQOc4kRb6C26xTQlEkRMKDkpj2O-TeTSm5y02n3BwAp-HFXxkVQIhuRQ9UtzaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📊
🏆
🏆
تیم‌های آسیایی با بیشترین حضور در مراحل حذفی جام جهانی به طور کلی  :
‏5 بار —
🇯🇵
ژاپن.
👑
‏4 بار —
🇰🇷
کره جنوبی
‏3 بار —
🇦🇺
استرالیا
‏1 بار —
🇸🇦
عربستان سعودی
‏1 بار —
🇰🇵
کره شمالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/96016" target="_blank">📅 11:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96015">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVeRkoiVqcRTGtK6-Q-hpCw3RW5aSzK7B_D5cWWJcjFfGkH7DmiDbsDBTxjNDyA5NtbCehrOZkYkv1hxi-MaeYblPM8Tm-WzUUj1WY3X9MNwC_6AOBE8G5Ms68rX16TU7tJi9SvqYZuYyFlQoX8gpQ7cTFQKmQBUWnE3E8DG44gdl5A1-96roj8N91PyaFuFRTSRUI0kgEbcD984j2_V77Yfa7_5Urgt-543v_zuv3Jv2pa25VPR_BRlGlJstu6LZhYoAMcZhCJB1a7zlqpaMVlE8fVojbwUogLHOqjr09YpK4PxF_mxkgcubFMnDfjwrth1g-QafmcMUw-ueBDUoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇬
🇮🇷
پوستر فدراسیون فوتبال ایران برای دیدار صبح فردا مقابل تیم‌ملی مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/96015" target="_blank">📅 11:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96014">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd157c98e3.mp4?token=Q8z8oIzpEwB8DNyKL1t3uPp4UoGF4PMP_9vT14HM9dV5QYsmHIh38vdC3uK3iQTPidhBxAT4EX5BgJF-wdtCf3qD8uhiA8H3zmIPNiPJd4iSkiQSrtXKpakx3Le-QCwWp0WxCN2m3YPfy8J4OXCN3UT513VcoyY2owRhUSjqf1Kew13308opK93ZTWcSRqyf-Nr9udvo_KJ1GodoKJDYQafJyhc_VUVqCnUgdZFTNcHKDmO6sWNtF79CvOXhh2STu-8zEqHB8i2EZM16bTPhpo6wLh96Bm8mSyDtzHMLwemU15c4cpvzyF_YSEoKK9f5OrDwH3dw0koszb-aPpC2rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd157c98e3.mp4?token=Q8z8oIzpEwB8DNyKL1t3uPp4UoGF4PMP_9vT14HM9dV5QYsmHIh38vdC3uK3iQTPidhBxAT4EX5BgJF-wdtCf3qD8uhiA8H3zmIPNiPJd4iSkiQSrtXKpakx3Le-QCwWp0WxCN2m3YPfy8J4OXCN3UT513VcoyY2owRhUSjqf1Kew13308opK93ZTWcSRqyf-Nr9udvo_KJ1GodoKJDYQafJyhc_VUVqCnUgdZFTNcHKDmO6sWNtF79CvOXhh2STu-8zEqHB8i2EZM16bTPhpo6wLh96Bm8mSyDtzHMLwemU15c4cpvzyF_YSEoKK9f5OrDwH3dw0koszb-aPpC2rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇫🇷
مصرف یک چیز عجیب قبل مسابقات جام‌جهانی توسط ستاره تیم‌ملی فرانسه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/96014" target="_blank">📅 11:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96013">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l82lCkA5ZyeUa6ScInasN4HONDJVbNkca9_g7Tnt5jZsOSdVFRkiCqv0yRicdSg8QiF7HODrtY7OMFr8yi8EV2jGQEwnrbtaeqmRlhSTfG1sS3-FMyWTytMrtLf5muh8i6-SqOKkULAK-Y7c659EFsJLvPMVOKrIbvUk2MCpppTZ71aP-lGn9JcRSzi3fLqRx9Ep2lqRfMuO4BAlg1Y_JowJUNhFsIehBK686LxYk167XKxX80zKW8hRXsVKw8RmMbWp8-Ci0QteHSdJPPTYlCaKWfDDywKa63Ey69Ed61qFvNFuRgkqcUJwDj_fBfkE-qe4bZwN8VeNzj4qcTcTMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تقابل دیدنیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/96013" target="_blank">📅 11:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96012">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fG9bD7gVra1UuP6HHwnTg2TrOd2IZZJu5qob-qS63Bzl8XGFJMd2tmNo-ZeqrHvEWZbhFD4AqVkfFZp0IRfez2Zz9u9VDMxqZffE7Y8yKWEeMs5vwSURZCSe_3aP1dMcJOsDe1qKYI--wHsEFr7BkluqbHYWWBuVc0HCLfv0JLyvKqJUI2fXE31gS4Bqr1w8eYVa29WeSy5JV2RyuJU7TmiU8P9sTTBLkO1ydkLihOb6nJO7zjt2zceajWaNqRe3KGcQNzpOWspf5gLgZwyYAy6aX5XQ0HqqR6qB22fNtz2zwZI-g_q2LwWQtod7fLWSlrF6ouLPwqQ3DLv-Ucv4sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
تکلیف دو تا از مهم‌ترین بازیای این مرحله جام‌جهانی مشخص شد:
🇧🇷
برزیل - ژاپن
🇯🇵
🇳🇱
هلند - مراکش
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/96012" target="_blank">📅 10:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96011">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83cfa0a889.mp4?token=uO4BsWbG_Vh1Av8g-QI77SFojNpd1vxkEG7aI9Zzomy5ba6mG5EeeIVQoSxHhwrWUn-bfpesoWpn_sJdsSOThXS2H8e8EUZ_RktEHezmJov7yAshPXYmHFNpQOGhnboQc2ggpwHR_jLgOFo8_on2uDz5wClf2ZbAuW3L9-K8oGi1dwXrhnrgeOpW-56R1safsLZR7klRNwaUZdj2KrV2J8-p7Ty5w0Ek96wf3ya-nhW4LHvjPvS1ZzYw-Vu4HzlNhEx-TDPiS_l-nh4PobxBttqS2c-e-OkbUruByJFiy7Dvfyxi7aHeBnW1ip2_OkVYk6gXe29f62go3YgTtSnvvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83cfa0a889.mp4?token=uO4BsWbG_Vh1Av8g-QI77SFojNpd1vxkEG7aI9Zzomy5ba6mG5EeeIVQoSxHhwrWUn-bfpesoWpn_sJdsSOThXS2H8e8EUZ_RktEHezmJov7yAshPXYmHFNpQOGhnboQc2ggpwHR_jLgOFo8_on2uDz5wClf2ZbAuW3L9-K8oGi1dwXrhnrgeOpW-56R1safsLZR7klRNwaUZdj2KrV2J8-p7Ty5w0Ek96wf3ya-nhW4LHvjPvS1ZzYw-Vu4HzlNhEx-TDPiS_l-nh4PobxBttqS2c-e-OkbUruByJFiy7Dvfyxi7aHeBnW1ip2_OkVYk6gXe29f62go3YgTtSnvvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به‌مناسبت حواشی بازی ایران و مصر این صحبت سمی مرتضی فنونی‌زاده رو بشنویم
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/96011" target="_blank">📅 10:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96010">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89114baf09.mp4?token=Q2-c7WDds9I7I2Hs7tY4c3CJUxePx4xJ2WW-AOvVfOx8TTYZVy236ApCNu8xSzqO01QU0OP_xleACl5vvOk12yKz8-8ec-bz3po843RkLm-t97oMvlqKsy_jEE2PJidLGf95NoA1a7Hyx1l7M5WETjaSgI8I0kSBef5r_4k9ojcm9tOHzbwKe6xOvwmvdEQ2T7BA0k1j6peMHVkMOKc5ds0wZ4U8WmlZ_U0Un_NuwZKiAc_D8GyuOWeZ7mMlb2MGlmY8x7-QDqog2Lx9HeilfU8xopvc5FnXUZGzhwcqWrjYSGYAkU-f8eaYK6Z4rL7WQY79X4tnKTncKkvVofH9QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89114baf09.mp4?token=Q2-c7WDds9I7I2Hs7tY4c3CJUxePx4xJ2WW-AOvVfOx8TTYZVy236ApCNu8xSzqO01QU0OP_xleACl5vvOk12yKz8-8ec-bz3po843RkLm-t97oMvlqKsy_jEE2PJidLGf95NoA1a7Hyx1l7M5WETjaSgI8I0kSBef5r_4k9ojcm9tOHzbwKe6xOvwmvdEQ2T7BA0k1j6peMHVkMOKc5ds0wZ4U8WmlZ_U0Un_NuwZKiAc_D8GyuOWeZ7mMlb2MGlmY8x7-QDqog2Lx9HeilfU8xopvc5FnXUZGzhwcqWrjYSGYAkU-f8eaYK6Z4rL7WQY79X4tnKTncKkvVofH9QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
🇳🇱
دیشب مکزیکی‌ها به هوادار هلند یه حال اساسی دادن
😂
😂
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/96010" target="_blank">📅 10:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96007">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nf571FH1cROE5Gite1i2elyKuXPPFBo1ylV16IME0wXwE_gShNNoQEV-Lc4KLAOCPoMOF5qRi3QjG538vmaK1lZEW5cKcb1rT7pcy9IJ2WSIwyEscbfymphUbqpXBgIoKcB2KS6hIAYjnt0aX1pTgRFaaB8QgFSwVWxIJwpOecbDh85qdPeaamxGZzPTZzO7LlppoROh20YEeLv6LaKCvq2KRO2XYFP3PfFb7ykfyhhA6wmpKQZrVEpe6apiPKRRttBzoXx2MevyQK5_3DUk3L-G-DBDXedrhLUx2Xresr6aw6kj1dhiUoeRf-A9psKGnaAdbdszI6tU6ugVWiKQbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BEGOI33-qInngyiPrJ_6Cee0c3y_YLJX8S0wkyR4wZeMo120i_UKTcD1i6UInz5v3-UUaGxXNnVIm8ORNZozIoDbidGp4QYd4MhfYCleSAaqajz6RM_mwczLcvRGakoSo0h18sJTMxs2RFnBUrF52RaCywEjRh05rCkja8FAbjo7k03R2rjWAEXHZ-0B-KV1Ef63Kf-2pNdr2yMjQo8VVXrBtTYhRDhsb6o-DkssJtdAMzk-hgwSAj3E3scGwicRV7LVo1RJK9rICv8_yQYn5U6BccDKVpvymWaUceqiowVseW7z1ROX_suwNm1ygN8L8K-cUN5Gw-fU_iOHJ9luLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nmpDCml_6Q69ivbpw3sFyjTDhuXLU6F1Y_fiBrcPwYHt1H2DgnSnQHN6p4vpBJ5k-Wv6RP7StwupNxmD9joRJz3ISjd1deAq3HbK1pNGuD9jIGxDFPeTnibCQz4EST7soVwpi90eKsqCKX9lRGoyrEfcQQejefNcnXhSXiyAi1msZpwzX57ooNLtd7PMuDTE8-Ee3VluJI3PpWX8qmKw5JYKPIe_Ki6mV6-WzVBTy3Ia0dFwZfXI5HPQV8LG1AfPN14drqX10rp1AjEl_yRjFGTHYQQxy5vbyc3TiDtG5aS0xYZzhiuL2qvz7inV5SKTDfRlVOp4tl0knV6Rp3fquQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر چی از کیوت بودن فنای مکزیک بگیم بازم کمه
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/96007" target="_blank">📅 09:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96004">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
ویدیویی عجیب دیروز از درگیری سر گرفتن یه ظرف نذری تو شهر همدان
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/96004" target="_blank">📅 09:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96003">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d6d7c284a.mp4?token=X78Z-gHmgq0AwsKKl0THEfNaX6Ex_QckNzjbJB__r_KpeyPvFGb4ddxEGrQgzWZ7ApJ2YEIkjUEi32EBjldmKfpMF0xIIjovOAyf3L3OuJgEyGZ8Lxg6Mx8c6eDD52MXdg1z4iSRKmJz9ToDzmTZydndkhUUNQ5NgOKX1N1bjx9bDpE2e1LCdH5r4J5sPKuOEU9WqOvNqhmtJSqP_fTkbWD2elTlT9fZjb3OZDDzqdBjgE15IXQAVzJ-C2Ga-gaqcSK4xklkLvxn5IUwG1DEfVpw2a6l7fXEqfueyuudOLlrRM3LHmZWxUr9HEGcHNjsC4TV0oDToW0RBWUi3eVwSpadY7apCLCpuCShJlvdonIajmt9_zL9JxqdXbnIljAaHGhbPZLmahX5arpUOi1a92q6KQLHiaUp5WzQJz3C4PoJhXz2ZKzggOXilk86BveS2njOioPPOIw2qhUfM6_m24Kmhrpc2CyegvSBkaCCXiYyLQFlW2ZVpdkVsK1wzCtIMjAiCsg79EsX0VgHeiX25fsVsube35h_G9Y1XM7EK-78eO-VNPoDjwJOuITQM7NTOPrdOGe1CZVJ3vF0qLjEBAo0gk1pVklh_r1Ehi3IVjH5uqIBloXjG7VDyQnbale1YplWzXliHy7zgDbaxFuPi25p0T7rO4bya-_pMgeKrUM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d6d7c284a.mp4?token=X78Z-gHmgq0AwsKKl0THEfNaX6Ex_QckNzjbJB__r_KpeyPvFGb4ddxEGrQgzWZ7ApJ2YEIkjUEi32EBjldmKfpMF0xIIjovOAyf3L3OuJgEyGZ8Lxg6Mx8c6eDD52MXdg1z4iSRKmJz9ToDzmTZydndkhUUNQ5NgOKX1N1bjx9bDpE2e1LCdH5r4J5sPKuOEU9WqOvNqhmtJSqP_fTkbWD2elTlT9fZjb3OZDDzqdBjgE15IXQAVzJ-C2Ga-gaqcSK4xklkLvxn5IUwG1DEfVpw2a6l7fXEqfueyuudOLlrRM3LHmZWxUr9HEGcHNjsC4TV0oDToW0RBWUi3eVwSpadY7apCLCpuCShJlvdonIajmt9_zL9JxqdXbnIljAaHGhbPZLmahX5arpUOi1a92q6KQLHiaUp5WzQJz3C4PoJhXz2ZKzggOXilk86BveS2njOioPPOIw2qhUfM6_m24Kmhrpc2CyegvSBkaCCXiYyLQFlW2ZVpdkVsK1wzCtIMjAiCsg79EsX0VgHeiX25fsVsube35h_G9Y1XM7EK-78eO-VNPoDjwJOuITQM7NTOPrdOGe1CZVJ3vF0qLjEBAo0gk1pVklh_r1Ehi3IVjH5uqIBloXjG7VDyQnbale1YplWzXliHy7zgDbaxFuPi25p0T7rO4bya-_pMgeKrUM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
🇩🇪
زندگی باورنکردنی دنیز اونداف
سرگذشت عجیب ستاره تیم ملی آلمان در جام جهانی ۲۰۲۶ که با شادی‌اش، اصالت خود را با افتخار به دنیا اعلام کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/96003" target="_blank">📅 09:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96002">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYeInyTxUqd9DpIgK5-OnExyDnSfJMGP0bbY2DYBX7SzZ8QVnpjNrS9vywSp2agOrHzCxyITtRgGjviVaJaq32SXPj9mf0DHZHWDIiNJenzTP1blF-4r3pfawV5ehPF6OagFVE_WYbjwGupYI9HT1yqIwcm1XWMx1R-OM_5o0g7ZfKWaQFEWn-HBAQLxXZhYJDWYVhyzOarB4LX1JiLs5n7YnewWhj8MvCjEDcCU80NLZJBvEBb8IIp3n0gYoVWiH00UE84YbELhh0ekqHJ_yia1EtT-tpfezrM1eksi5fav6IDjlLbeFdthu0-hrZwU1ghaKH1cMfC-8m6PFH1xQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
💥
ترکیب‌احتمالی فصل‌آینده بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/96002" target="_blank">📅 09:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95999">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PhJt5K7TzeqQb_PwFm9lO0mu0hRyxEpUDrKZdh53rFR08VMxPQ9B2z2txMIxWwJ3Qy-VkcdqYY_FWGyaAXTczhNkYL4Js6dCUBoduIT2Ef9JaoXdB09oPMVTO5lkbaQPjRiO6RNhUOAznO4f8yQ38zOY3iNGko9JwnnLyhAlI4HlD5QWtrvSheQGJw8cJ1oaG2We0JD_JaRrmj7Byxk_5N8BS9fKz0M2VwXJ6wVJ6em3ICCki6GTNUPF4m0nH26_sQMvSfocOdsZtWwZ-O3JBLjm3QIzBXP8RrqxJFBsLU22zQxGkB4dLLK1PvvT7OIkHSj9JA0nG2_hjcLKkMZNyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZ965ZT-2TTL3J7t7kgXPcRoXSPDfDGOakSJsNlbhypTaB_0K9srZLVJd8cOUPNBDf5EJFqtFmzchOKv8WKxqV_mSeHgCXfrnOnACIaBUIiR8KgAHRi09Q0A_SIwG69qgqkYUX33DkZ_EbZBHI0AQsAP7hvo81DIAaO6aIeWkSjdKSIffIfKBfyTk3LusutJTAf-9Qy66ZN7_T7Nz7nOJhOqt7twyHAZyWJ-GmN4ehfukM7J5DiMDAiPUDwo64hMa-5jJkMinis4vzX5dIVaXsCUrmd1vjnp2R0oiniJuskZAUmVZU81axiabJVH_SzdIQqoeVh5CiPTs5Om20kHTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XS0ReRQqJLyLHmUIxmA3EXICqR0iTHm1OpE4UGgE36pviCCgXTMRT1WVeN87Lhz9BMjDalDXRWy9g9uFZGR-vQ9zCqICrzqOsvwEXCzkY43hFawcEvzzL8-wvlWRYl4JRRpmKWejsCnfl-nCB-Lct_pilejn7oTmlj7K1ecgPpX3-hSmmJUmuz9pPWMybdXj3eIRlrt-xJIN4LtgQK0xF4wPf48LT1jfVamxHrSZysyn0WL7ppKvhOt-rC8KYu5lWbpNlL8U0YRqJy_4gD94X9Q9YSznmaHPMOKmFU_obfyTqE-gYS4vOpVNUt1mqJohNI2OM0jAmFtlepArS77g6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ای خار جبر جغرافیایی رو
🫣
🫣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/95999" target="_blank">📅 08:10 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
