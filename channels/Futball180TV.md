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
<img src="https://cdn5.telesco.pe/file/vfKDy4JEPy8xOQ8t3VzYRK-qkZiUSIY_IWyNpqFGyyXfT0vTuEZFVloZD9JU6NCGBtAHyM0DO-2t0CNZMGaJZByzN8n1_Mjx09JuRGe5CpHOfsk2yxePHtSPkR9CJBW77nmUduE59ppeu4odSvxUQHmzqSvSQd8MhngKq7piaNyEEGg_4gv8X4Y_blA1l33FmIIyfqmh-VwUyD_xAWa0JQi6r3vn7UgRkBFSUyv8N2g3O5l_AvXzlxOo-h7YXaRkCQvNiQotJ0N0QFTB44xcKdO9zPyeJb9vd_NPCjsvLtTOlOlUa56JNQXddJTEol14rCAeUvnHZu6P6bGfp8ukXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 414K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 18:37:23</div>
<hr>

<div class="tg-post" id="msg-106449">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cctrfmsLX9wAMf3YxmATFDpTfHa2c6C0jVZHa64xL5eibZ_mayPUDylP4OEj2ZSlQeS7kOcFA__LQSQeTbzYfuzS9Rey0TY43h_rEMbOxlf91GpHzKMk3LRgubdT_8dvQsAZM198uwIGTK0uqzzfvVJx2NgcNDcLDgiOAZN8CAGNyseGRu_ZVazoz_6QzfHzsfl1yBtQ-mlHYxe10rfCDkXuZwfIbj0iQnMkVShy0waa86voadSFV30trnnyhUEMUNTYLdkEayfWgaeBqzpItJBMg-tY2zxaNrboSwNXpdjrBG5zFjIYwiJcBUXKMWgD-0fi7T3BcWeTr9NEwS1TTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ترکیب تراکتور مقابل شباب الاهلی امارات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/Futball180TV/106449" target="_blank">📅 18:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106448">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22236f4e69.mp4?token=NRBVbgCLHzyAKSq_UAbuBNmfar33v0xjYBXFJI4YiZr2vu7453w4S2OQDyV4-4S-BUjyuUp4Z8ovBPPUi3zoZAnXZmqqBAuqwD_X6hjYAK94Mz2kxAtkh5xfRU16CGDdDaMU5LDxtE57mZhL27Z45NuUkJlyLebcv-XVxcYqbHV9Vz5kAgK0NZURWY7NUzBjsTy08emVe_UnQIetSiCzs6noQBClnyUUKqWJvdD0WICNF215S-pzYb6uH1lM6khd9E-9RvMhwt1Hf9mkWS2FfPrY1iHN40tuxWFxiCK8tIRplyAibebnNVH9OvxcAEUgffVhHKm2R5NwK52P-cUv2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22236f4e69.mp4?token=NRBVbgCLHzyAKSq_UAbuBNmfar33v0xjYBXFJI4YiZr2vu7453w4S2OQDyV4-4S-BUjyuUp4Z8ovBPPUi3zoZAnXZmqqBAuqwD_X6hjYAK94Mz2kxAtkh5xfRU16CGDdDaMU5LDxtE57mZhL27Z45NuUkJlyLebcv-XVxcYqbHV9Vz5kAgK0NZURWY7NUzBjsTy08emVe_UnQIetSiCzs6noQBClnyUUKqWJvdD0WICNF215S-pzYb6uH1lM6khd9E-9RvMhwt1Hf9mkWS2FfPrY1iHN40tuxWFxiCK8tIRplyAibebnNVH9OvxcAEUgffVhHKm2R5NwK52P-cUv2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حسین زاهدی جانشین سازمان وظیفه عمومی ناجا: اقای بیرانوند از یکم مهر ماه باید در اختیار یکی از تیم های نظامی قرار بگیرند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/Futball180TV/106448" target="_blank">📅 18:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106446">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k6rbe6LrnBPoWmfiqYKFHL2b4cJtJQ0NctQTBjz-VgrviNYtH2kb7EBnyy8fyPF3XJCH3kJLb6EZhv7TBJ0HYK2KNJIxFNc2pryDw9wk3jwl1H3Fjzsp9aiApTPwKL6BWWtTfkmyPgSyVnQnKEkgyakNCMcqgXrWDDFUr0N57PmypDSb-3Pr7HQbeXyzdB9l8VK8EZb9PIdNJlG1ApgaKdt4vrAAM3iZ5I7nqTRa5qA3EP-4zdCGdHMV1wW4UOs-auUwEBuBwAEXoX4SkJfJFtBR-2iDLVurFnj12KqdYWiDYz-GULL6q8BBkO7o49gL9SCXs37HAN9CEKrpOaihtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C2TJBoln8h_84OcPIdxfa1v6SrMY6O9TmRQoKfXf0o5SDuRuTg0SD8IeqMoAhV8LHY5pAGnZPGd948wnsA7jjgTLULuFu_QWle2BT3vH2iD3MGEZ_UBJe1EVzBZtVYLPhBq0pR4VvlJqduKkcIm9YaNwj_V3kCHs3Q2qE0EKCdun0gLcKPREugt_upb4ZQq4NtDTTg9HUuS5vel4a9bust6qmZXcMniZ3TI0j9N4LE4pFcgfVcuonmY9qqxI_bsndFlZeHmMF_0jQuGU4pHpoEIa8qePPxlHwzwNoQTae50RimIRlZwyPxEi8Agnam_jrzGJoF5A-lFkAOWnW5r7qA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
⚠️
صفحه اینستاگرام رستوران «دستپخت بی بی» در تهران، به دلیل انتشار یک استوری با نوشته «هیچی کتلت بی بی نمیشه» به همراه موسیقی متن «بی بی گل» از معین، به اتهام «انتشار محتوای مجرمانه»، با دستور قضایی مسدود شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/Futball180TV/106446" target="_blank">📅 17:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106445">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8d5f06714.mp4?token=IJR-PiUo0HzRcVGLB5wSZQ13pBGf6U1l0p1ZA00qTXaqRSqoBTlft9c7cAoUK1fZN5FfL5EOrngjNQxQxj5TOODkD6yl5U206V3J6Xl9tRHIsVE4nlsMoiLLj0_DN7YNTtXD5jj2C2SQ7pwjBWNWNjrVuPeZxNA2RK9hHmMREQImYn_PPDqyAL5OHHhwMDg7KbCcN9gtDPCBCDwdfSRVqRmcpW3iYRcoUPeZNrxoE8CxIs0viLJyNGorsIxWGMxXBOvhHnnh6e7-kUp5edDG9LHiBJqnaazZTXEQIAaRGahV95td2x018xSeehD4KyArF5rzLpJcdo_sLPhV7rz6kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8d5f06714.mp4?token=IJR-PiUo0HzRcVGLB5wSZQ13pBGf6U1l0p1ZA00qTXaqRSqoBTlft9c7cAoUK1fZN5FfL5EOrngjNQxQxj5TOODkD6yl5U206V3J6Xl9tRHIsVE4nlsMoiLLj0_DN7YNTtXD5jj2C2SQ7pwjBWNWNjrVuPeZxNA2RK9hHmMREQImYn_PPDqyAL5OHHhwMDg7KbCcN9gtDPCBCDwdfSRVqRmcpW3iYRcoUPeZNrxoE8CxIs0viLJyNGorsIxWGMxXBOvhHnnh6e7-kUp5edDG9LHiBJqnaazZTXEQIAaRGahV95td2x018xSeehD4KyArF5rzLpJcdo_sLPhV7rz6kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
💥
✅
شغل‌سخت و زیبای عکاسی مسابقات ورزشی که همینقدر ظریف و تمیز باید انجام بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/Futball180TV/106445" target="_blank">📅 17:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106444">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6637c3eef7.mp4?token=iPm7FP9cr-lHDPU_Y8yuUu01M8tmtclvMaC7SseV8cwkIi05rpOjQ6_jHtr0Xba4FeHmdg68PAWX65iMf99abHvBr8IIwFPo29swNhFhYBABkqyxfObAbkuI3g94QsSP6zHZgxHZm4u08OxbAphUeyQ2mYle77XUugiTyA2Cdx--6FTAxclF5cHuuDrJ7uUib7T-BAUDHBGPud86I5BbPi168FYN7EKve5K0r2KrA1qx1sJ3BPY2hVkLgoZQ1xnl1b4op8-ygvHjnN4NnIihq0qCIC2tqfwS0X3EqHNOZ2-xj6k8HDMpmFQMsK6hhqbJG-s_EbiJR0R7GAa3OAKYEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6637c3eef7.mp4?token=iPm7FP9cr-lHDPU_Y8yuUu01M8tmtclvMaC7SseV8cwkIi05rpOjQ6_jHtr0Xba4FeHmdg68PAWX65iMf99abHvBr8IIwFPo29swNhFhYBABkqyxfObAbkuI3g94QsSP6zHZgxHZm4u08OxbAphUeyQ2mYle77XUugiTyA2Cdx--6FTAxclF5cHuuDrJ7uUib7T-BAUDHBGPud86I5BbPi168FYN7EKve5K0r2KrA1qx1sJ3BPY2hVkLgoZQ1xnl1b4op8-ygvHjnN4NnIihq0qCIC2tqfwS0X3EqHNOZ2-xj6k8HDMpmFQMsK6hhqbJG-s_EbiJR0R7GAa3OAKYEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر این فصل هم آبیه.
💀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/Futball180TV/106444" target="_blank">📅 16:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106443">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/300398c1b7.mp4?token=RHgoyhZubG1TsfMWqTSeSeZ7oX7Bq6o_xXyktTlA9UhFd2D1tH0-5bdC3JXAYnkh9eNSk1y9AgKyC6tIwxkA8UlintKDcPxSTTuBV-XCn2vRFpTM9KUC_8lv5a1zqsqPE_e790acoSx54_6qCzvK49Y1-iBYxxQ0JEoJgWdmqhks-w1ijfMCpokxmMFoSmIn5JeDMuiAmNu2VQSdDyfsoXdqSHdDP18aK5dIi3cO6oe1sNMUi_b7s5j_guhDRcJ3PqV04GtWfC-emlsZa9J46crNA-u3no9YBBnfGEGmoht_eZTyj0Z0kx5E1nE91vTWIdCHO3wOkVpCBeIgM9LoIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/300398c1b7.mp4?token=RHgoyhZubG1TsfMWqTSeSeZ7oX7Bq6o_xXyktTlA9UhFd2D1tH0-5bdC3JXAYnkh9eNSk1y9AgKyC6tIwxkA8UlintKDcPxSTTuBV-XCn2vRFpTM9KUC_8lv5a1zqsqPE_e790acoSx54_6qCzvK49Y1-iBYxxQ0JEoJgWdmqhks-w1ijfMCpokxmMFoSmIn5JeDMuiAmNu2VQSdDyfsoXdqSHdDP18aK5dIi3cO6oe1sNMUi_b7s5j_guhDRcJ3PqV04GtWfC-emlsZa9J46crNA-u3no9YBBnfGEGmoht_eZTyj0Z0kx5E1nE91vTWIdCHO3wOkVpCBeIgM9LoIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
وضعیت قرمز نفت؛ آغوش باز آبادان برای بحران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/Futball180TV/106443" target="_blank">📅 16:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106442">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7HaHHvBXYBHmIVSoRrJbsIFZWBMvAUY87HJIWmsmbnfa2KzD3c2N3cK4jx5b2fcgGlGrQcPw9DG6rW1QB7k43NLqb8YtVa6RYJqx2FUM1vHJlhwT8Vs4cDuic6QGsXdVRJ58u1EHmJe2O0k9Y1IFZby037tNFciWnuuVlBqppqteiCN01HMi3CHlhiSacwzX0leQ54xG9uBd0vPQM7YNAbz9vRUbhIrTigHmYb1jLc7ILRDFPb_ZYcCcvUJ2-jAIvK19qNpUNRPS1GDajSn-2269OB6D5RZN0ro9W1d7p1xMj6U1ySjrSlD2t5QQVWtJuNUOG6T5ey-xlrvmmgoJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
تصویر جالب وایرال شده از رشد عجیب و غریب پسر ریما رامین‌‌فر طی ۵ سال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/106442" target="_blank">📅 16:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106441">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OB2tOI7UTTXJ7BRwiaioZ_QuK1qG5JSlDcDI0ppLRULDpFtpLevH_rKLFIuptHR-bgz0E26AANFoGWXy_MmSnWvas3L9m2b3NXEq8a_RWqG5KuATiz7SXl_8yriZaVjSw0EqkjZ0IfgHoxuasXZKMmFJLIC_w2Yvm4cMuKHZqc2lJn3Xpo9p_FLdRUeP-4E70rXqjACB7AlCqnGwnsex-rUpbBl03WKswVRiZaKovzVc1HqRe7uog4adPYl5xyUTOsNTqDzWGPs6_tPyPi0NYoo4ChyuE8SFeH3Pc9MAd1je2DdEojRQo0YE39KYBt_IgrYFv8D4zOH-VanJgZxnOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد فاجعه‌بار تاتنهام فلک‌زده با هزینه فوق‌العاده زیاد نقل‌وانتقالات در شروع فصل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/Futball180TV/106441" target="_blank">📅 15:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106440">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0f4de3a2c.mp4?token=MS5x0MARj8tDdQ3b2oIuVLXNvaUKNiduLqPDrbyDTB1p_QAByJhjmdbRICv4kCVZBqePHgD-ZeFPHheXImhb65uquYaLD-LleBzL3eQprgvACA_BG0kE3btvzCkGlMbCBIFzLQQ1F8zZ_rfdj1f8sASk7jVqAxs_Z4xje-n8ZGCKa0bBbn16x9vj2QRT_t04n4Q4I3BXmhbBJE5GvQUp3LmE2hOZpqlsV4owp39gfqjkr6mpM-wOdtrdxkSjv2H6wg-3eYXmcMJ1QqsljvF8fDMF2SrU6fwmthiMKtuEBcs1gLyMKQdRLCDTkBYM1wlQe6I_HVP9m7ctzyAqB0flfzmHi9LiqWLaW3VZ-_0u2qh9NIjcsRzRzwVA5EJ_Nf0L_p5a3GvKuqtC16PHD5rHtzoViSZQjrWmPz9RF9-9BwT9OWct9njB5R9uql7ClDQE8YmQDZVCdE5fLZefqZTyZM3iRIhjIu1bB06xMwBcXYINaCTBxgy55uxDTx-lA2ErNfLSl0oL1nkx4ROeqCQvFWbXyq3VwVI3p0LtJtJH9aZ0qYZvfzw08OCLBCKNYXKloJ2YBRmnKByeBbV29qeYAaVfUGddIYYEw0kWyH5QDIzqpb9VafXtqs1SDnC6cUM4S_hCNLpS5P5y79brqO0supscR9JdCIlWjSG0P8_50i4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0f4de3a2c.mp4?token=MS5x0MARj8tDdQ3b2oIuVLXNvaUKNiduLqPDrbyDTB1p_QAByJhjmdbRICv4kCVZBqePHgD-ZeFPHheXImhb65uquYaLD-LleBzL3eQprgvACA_BG0kE3btvzCkGlMbCBIFzLQQ1F8zZ_rfdj1f8sASk7jVqAxs_Z4xje-n8ZGCKa0bBbn16x9vj2QRT_t04n4Q4I3BXmhbBJE5GvQUp3LmE2hOZpqlsV4owp39gfqjkr6mpM-wOdtrdxkSjv2H6wg-3eYXmcMJ1QqsljvF8fDMF2SrU6fwmthiMKtuEBcs1gLyMKQdRLCDTkBYM1wlQe6I_HVP9m7ctzyAqB0flfzmHi9LiqWLaW3VZ-_0u2qh9NIjcsRzRzwVA5EJ_Nf0L_p5a3GvKuqtC16PHD5rHtzoViSZQjrWmPz9RF9-9BwT9OWct9njB5R9uql7ClDQE8YmQDZVCdE5fLZefqZTyZM3iRIhjIu1bB06xMwBcXYINaCTBxgy55uxDTx-lA2ErNfLSl0oL1nkx4ROeqCQvFWbXyq3VwVI3p0LtJtJH9aZ0qYZvfzw08OCLBCKNYXKloJ2YBRmnKByeBbV29qeYAaVfUGddIYYEw0kWyH5QDIzqpb9VafXtqs1SDnC6cUM4S_hCNLpS5P5y79brqO0supscR9JdCIlWjSG0P8_50i4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
▶️
ینی این ویدیو حق‌ترین واقعیت درباره زندگی اکثر مردم در دنیاست. از دستش ندید
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/106440" target="_blank">📅 15:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106439">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhIQdyb5PpBZD8deNDIe5UiKy1DWBbGa6UoFIO7YRFtN3TilfPxs1NUkQtQFOGW2PaZQSrfeZARre8p0gJYBE8lEF4xsRuCp-9J31b1R5mdmiD5-LIyBqXMcUjqYil-iovd6Q27LxNSwJI30Ucb3hEwvgJ9vwOW-649EITwis8g3RpxbfKiTKcpXvILbqsz8jZBpsKxiGRd_oQ1xwi_GuJdJZb7EXlJVX9_QS4dlCXrdA_fysnR7fVJuHhAYHbsko02wup_auCf3dXb6BZsRh7GajdLCP_lgkA89o6PA3A71LXz_GzoJtCLfy3KvEZ7xrUjQstuZnRa_bDND180gmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
📱
🇮🇷
آرزوی موفقیت رامین‌رضاییان برای استقلال پیش از بازی امشب با السد قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/106439" target="_blank">📅 14:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106438">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62958310f6.mp4?token=izt90cVuYfyTYnhpHLDtnMZmmPblGmYACpDaHwsswi54XOnh7UNMFL_YtCyZwnM_MXL5it5LyyiQz4zG5yFn_CsIuSbSw4ZQcrBNvG3UjNeDATp6aOTQD-IY5PwrsFqvEhuXDXOd5X9MzaSraFWs54_eC0crNf10pd-ixHn8UxAkHtV5zbK_3tAdlirBS1ILYeFaf6KfU4Ddd940zUg0Z1Ly1Jv2n73wYy4E9Nn0e7A8V26cF9Cp0CT2S8yqDUva6I1ywmft6G8zJsB0bosz4CWQgxyioBYMvPemcQRtBtslfhCZjHM6kpMQ2Y84PTCTHMYgSvnD06p7FGCOUkT1zlM8nd1e7q7J6A6YzZXbUaGNwvK0i_L5sPnOleaN-YcAq0tacUwx8-367Q-OP62jFEKbdp-wBeARrv2Ilh-SIgvLtIA3yGUmtYFWQV6J7nzS4w_qNsyd7v22QrojBWqBLe8EVbe8vsdiUoTuyRCmNSHbpWz67LnV4H-1c9VEng4muHoAUKG4tDoc7fGecnvJPdKhPb8Qmuca8nuMmP7cRNHrWh1KPLKTa2WVLJlg4ASyxHjcAntbXa6YFwjblqnFFIw64qAqJ85kx-AhhaZ1aLI7z8gySplqpGNL2hXqpLZr8VUfusDcnfM4ZZNsilpHz7GZ2lWfBymIPloPZYRbi8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62958310f6.mp4?token=izt90cVuYfyTYnhpHLDtnMZmmPblGmYACpDaHwsswi54XOnh7UNMFL_YtCyZwnM_MXL5it5LyyiQz4zG5yFn_CsIuSbSw4ZQcrBNvG3UjNeDATp6aOTQD-IY5PwrsFqvEhuXDXOd5X9MzaSraFWs54_eC0crNf10pd-ixHn8UxAkHtV5zbK_3tAdlirBS1ILYeFaf6KfU4Ddd940zUg0Z1Ly1Jv2n73wYy4E9Nn0e7A8V26cF9Cp0CT2S8yqDUva6I1ywmft6G8zJsB0bosz4CWQgxyioBYMvPemcQRtBtslfhCZjHM6kpMQ2Y84PTCTHMYgSvnD06p7FGCOUkT1zlM8nd1e7q7J6A6YzZXbUaGNwvK0i_L5sPnOleaN-YcAq0tacUwx8-367Q-OP62jFEKbdp-wBeARrv2Ilh-SIgvLtIA3yGUmtYFWQV6J7nzS4w_qNsyd7v22QrojBWqBLe8EVbe8vsdiUoTuyRCmNSHbpWz67LnV4H-1c9VEng4muHoAUKG4tDoc7fGecnvJPdKhPb8Qmuca8nuMmP7cRNHrWh1KPLKTa2WVLJlg4ASyxHjcAntbXa6YFwjblqnFFIw64qAqJ85kx-AhhaZ1aLI7z8gySplqpGNL2hXqpLZr8VUfusDcnfM4ZZNsilpHz7GZ2lWfBymIPloPZYRbi8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
سوپرایز دیشب اعضای تیم‌ملی کشتی برای علیرضا دبیر به مناسبت تولدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/106438" target="_blank">📅 14:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106437">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b720c6c51.mp4?token=JGf0uLQCpnvJ10CagbbJ0VPH3c2azPTNbZBn1VwDbdj4T2Y8-C5_g4Ce7Y4HBbc6H0hCebDaS0fYvN-4NSw6ZkFmWIQLyxNK6O_BfzRqxHtblQVD3cUcq3rxs11EQyUbjg4kxi0PGNh1xevePnyTC7eaLXpsEFylk_SmGtFxIBacSzZp5nvEhcENb520tGHGNmudd0anZl6djKDG19X0zsB6PjpRwxb9cWtHHnyAV6XCSKMgkQgm9T9Dvjt60CWg-mTnUPNMkzs_coWynpLvcVyf5cPpxPbWhzoBYDUZI9w5uyrSpt-x0ujoEZAxDLoo86PC7hta-21emgajm2vPkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b720c6c51.mp4?token=JGf0uLQCpnvJ10CagbbJ0VPH3c2azPTNbZBn1VwDbdj4T2Y8-C5_g4Ce7Y4HBbc6H0hCebDaS0fYvN-4NSw6ZkFmWIQLyxNK6O_BfzRqxHtblQVD3cUcq3rxs11EQyUbjg4kxi0PGNh1xevePnyTC7eaLXpsEFylk_SmGtFxIBacSzZp5nvEhcENb520tGHGNmudd0anZl6djKDG19X0zsB6PjpRwxb9cWtHHnyAV6XCSKMgkQgm9T9Dvjt60CWg-mTnUPNMkzs_coWynpLvcVyf5cPpxPbWhzoBYDUZI9w5uyrSpt-x0ujoEZAxDLoo86PC7hta-21emgajm2vPkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کری‌خونی سمی هالند بعد برد جلو یونایتد
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/106437" target="_blank">📅 14:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106436">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbe5d1d200.mp4?token=nfNfc9ZOh2xQcSHN37XOQCaPfJGAZee2rrohSt1OM1PueBK0tfV2K27Fj43gIYIlCLXPVWaGFjVn17SsbzHTFTRb6_RKtcvxVEI_TSnL8NH0zrEei_61poxpxvpxln_ufNTgyqz9dlgFXHhqPvh6HKouywdxqAuwdqc4krqMbfx9fI9lYEIuX6KdrgutVzDuLHtGqqOD7OdBnkrNMpMjMs84aQHh5gwAy7TaMLuU_wU_hxfNsKRuV_Jln2I2tKbB7EOkgtJN7GzioepCk5poIQ_mb9BGZuIwBeD87n3kvE9hRVhBNkShVLFekKchqCoR9SlNCHIp99LMqFx1peyJPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbe5d1d200.mp4?token=nfNfc9ZOh2xQcSHN37XOQCaPfJGAZee2rrohSt1OM1PueBK0tfV2K27Fj43gIYIlCLXPVWaGFjVn17SsbzHTFTRb6_RKtcvxVEI_TSnL8NH0zrEei_61poxpxvpxln_ufNTgyqz9dlgFXHhqPvh6HKouywdxqAuwdqc4krqMbfx9fI9lYEIuX6KdrgutVzDuLHtGqqOD7OdBnkrNMpMjMs84aQHh5gwAy7TaMLuU_wU_hxfNsKRuV_Jln2I2tKbB7EOkgtJN7GzioepCk5poIQ_mb9BGZuIwBeD87n3kvE9hRVhBNkShVLFekKchqCoR9SlNCHIp99LMqFx1peyJPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇷
🇶🇦
آنالیز اکرم‌عفیف ستاره السد پیش از تقابل امشب با استقلال در لیگ‌نخبگان آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/106436" target="_blank">📅 14:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106435">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGVNO2WXS2DHTcsOyMhk0CxNjYp4ZodMgI-NE1GYKcMTd93Ro3EQo-6EUS54B2BUpQcqYOpMGXwsACWAllFieI9cFtGTes00W1VNqYr0xM7UXVUbXLg6rpF9rXFumSwNPMnX9fMWAQByFlA5Ct7acv-CD7y2W3ipfndEsvEhDQNJ-B11-bIHSg9eTh0RoPYUjU-fi3mXN4jDNndKhx12EBU53q_oF_arPpY33PS96zX_sE-MuoKir6BsczA57l1f0t1_uvSwqow4rkGdSRxeJARJPPaD77oERv3ZwbsiTjHnHHQa7Z4Xo0JOP5DyjjZZj1axvq46Tx-lFr1ua3noeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
👏
سعید سحرخیزان، مهاجم استقلال ١٠ زندانی جرایم نقدی غیرعمدی رو آزاد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/106435" target="_blank">📅 13:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106434">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4b9165423.mp4?token=iGeuszgOeDFt8q97Wh1kR1qYqwEv3nDDaSeDESyN5FKZHXd_0YffPZW0XW-vjcb6jFjpRJXJAboshJSy3iRdASp4IC9qPzrtqJE6W_8T0jX0cXTWQzmVR8FLx7MDgDq7M-dItBgmSfZEKArTvjWpVsUS6RQrMEKpQed3qPusbCbCXDeObWLrPdpATGO1vv6cvYqAApvlFl0knaE5D6RWeTpDxc-hIy5Yq_EHbKaxf0skipe-CwgUTx82QYEL6ZfnjG0sVJRfdeviR5UaubnhyjvR2aZFwegPxdMKN1gmuSDPX-lpDL5FFodDbBzEdMNlNpfW5dM3qn3vScGtXnAS_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4b9165423.mp4?token=iGeuszgOeDFt8q97Wh1kR1qYqwEv3nDDaSeDESyN5FKZHXd_0YffPZW0XW-vjcb6jFjpRJXJAboshJSy3iRdASp4IC9qPzrtqJE6W_8T0jX0cXTWQzmVR8FLx7MDgDq7M-dItBgmSfZEKArTvjWpVsUS6RQrMEKpQed3qPusbCbCXDeObWLrPdpATGO1vv6cvYqAApvlFl0knaE5D6RWeTpDxc-hIy5Yq_EHbKaxf0skipe-CwgUTx82QYEL6ZfnjG0sVJRfdeviR5UaubnhyjvR2aZFwegPxdMKN1gmuSDPX-lpDL5FFodDbBzEdMNlNpfW5dM3qn3vScGtXnAS_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
▶️
طنز تلخی که از دورهمی به‌واقعیت پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/106434" target="_blank">📅 13:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106433">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df19a571d9.mp4?token=fQGzQqKLf2U9JnUh3H4An0q3BmGUOTw-ZoxbaaoQlcDS4jk0KuD-iO54qvXPp78OEmGpjEHK5X6PlqMIqz6EtwpRkvVX-B1tR1BQFj9qnPolgBUVTjJN1hUsU3xhkz3levY9GUrusN_c2sUGSR2ftVp-AEvHinUVdM03D24VMEdOYctpWCWVVBP0wyGWLFeiOG8YbQrug-2HeWxrcPq2AOkUC01IJzrhZQROXaqYYehme8X6bMnPAMIyZWg4D4kGOXXiobonFKABIS2Jsvr1DCuLzxjKhgOb79jIPz8xfZkrRE9CvzszXafxBtYohXCsd9-ry2YjLy7ijDe_6JIDIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df19a571d9.mp4?token=fQGzQqKLf2U9JnUh3H4An0q3BmGUOTw-ZoxbaaoQlcDS4jk0KuD-iO54qvXPp78OEmGpjEHK5X6PlqMIqz6EtwpRkvVX-B1tR1BQFj9qnPolgBUVTjJN1hUsU3xhkz3levY9GUrusN_c2sUGSR2ftVp-AEvHinUVdM03D24VMEdOYctpWCWVVBP0wyGWLFeiOG8YbQrug-2HeWxrcPq2AOkUC01IJzrhZQROXaqYYehme8X6bMnPAMIyZWg4D4kGOXXiobonFKABIS2Jsvr1DCuLzxjKhgOb79jIPz8xfZkrRE9CvzszXafxBtYohXCsd9-ry2YjLy7ijDe_6JIDIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
وضعیت هوادار شیاطین‌سرخ بعد دربی منچستر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/106433" target="_blank">📅 13:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106432">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEBakQAfCbpdajgg8e1ag7aFp7t5lQIP1yVB9K87DsQjB-B2t_ffkR3VwmqUcDIlbNpfutp1EV_dqFcC2K7REU-_EQsqBZBAYKRJoKQrSePapB0B4GVHxDHsOndEz3xg_pn2tv6EX7Ujjq_O1NRTGGL-6QXVVWscx1-_QhsehSHwxXTGfhIQlXawNDNPWy6BTq6xBzxiBI8z-JBYoyvktP0zJKsM7fXoIuNaedM_7P1fVBBR8-aRTLm9FWoPI49fv6-qFD3-WyTvVI-RykBamWKj2m-t63qGJvTbt6zFYOYctx9GFL7kYavRCGKOqf-GeFMQLYW_-HfNsymSMklEWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇪🇸
مقایسه عملکرد دیومانده و اوبامیانگ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/106432" target="_blank">📅 13:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106431">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_zX62_2cSGX3xBivjrUmQxTjWRrmz6U7v5obVo4OhSyWO1bj64fVy8REv0UVzAE71PeT-pEbG9xMQFZN9Nahv-qu3UCF2m0qTeO4a67DswGI0Pam6s8vK5HJFt6rGh4LmHh1HN8o3LqfbQzMUReDoxffqHsdQY-0ef7FBvJ_2zbUQxRY9rZlGxgddExWejo9PX8BlLjksmGhodddh6XKjeNt4lyHhfmCMJH8S8I0EOkHXBTz66zAe_-bjBBQJg58xeYEjBz28xeQSNUQIoRmReZOfsRGTqnBISbm5jp2f3vfoGrPgErCUl58ZGcrVKU-7tkj50IDkzSbA4wtFj77A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
‼️
🇪🇸
اکانت باشگاه بارسلونا نوشت: فقط وقتی می‌تونی این پست رو لایک کنی که تیمت از ۱۵ امتیاز ممکن، هر ۱۵ امتیاز رو گرفته باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/106431" target="_blank">📅 12:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106430">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evSl3N0TpkA-e3zayYUaC6CRSjWKT7kEbZLvSEkQDN91Gnm8PEBXk8YRDbk-239yJQWghqvL-8pGXRESqhJOpO9mJiSONSHhMhyrz6DulC7XW2qBk45NvWweOevtLA0lD6oTrCPeM9XMHQwDfHI9ujzNDHtAPP2b5pBudm23_R7AbzfleyDzb_fRJsV2RFq12pvmBp5uOzfgzJo07Af0SNBbJZLyvs3Cy4oikpOJVGJ9e7Uqv8t4Z_W9yXSWU3HifdBoXH61vrUbYswwfGss1xcbVl0UopfcRWwPLO8gRVU-s5Ql_Z2OBgENMzZlAoH09zB5yPmbRY9Sf5l1wIUQSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🟣
پوستر باشگاه تراکتور ایران برای تقابل امشب با یاران سردار آزمون و عزت‌اللهی در شباب‌الاهلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/106430" target="_blank">📅 12:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106429">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psAsQM_7QIzT8aclukUTqJqVGSALJPuVxLDZD8LXmHi0du0sb0UTHOy3Vm2QoGK54oFEd-dAf_PD82oZzbuxfUmy0uXqtvoSRzZMM2ZD4sEa0K4F7DTp21DpCcUNLIzeVC_xjarDJonNqw3sAR97CTaJLa-dMYS8Yfjqu8zbatIXa2-Sr4wFJtOTTb1H6QRM7tkhJonfAxu8Bopywf681hwoYaD65KHnDOVWTgPkvcNj-UwVW55DkhGuxttSNoiQbhbTY77mqPCaxBXufi8MkSbZtSFuNTSDR4Zf1pEVZQPs-H-Xd4c3i40qJEP4tREbHFrS-NOpt7i3CPiQK3Q8eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
👤
علیرضا بیرانوند: به عنوان یک سرباز جان بر کف ایران و اسلام، آماده رفتن به خط مقدم و خدمت مقدس سربازی هستم و از اول مهر به هر تیمی که معرفی شوم حضور پیدا خواهم کرد و در زیر این پرچم مقدس به انجام وظیفه خواهم پرداخت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/106429" target="_blank">📅 12:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106428">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5d890016b.mp4?token=E_Qp6DQLgNtZox4PpM2kXAWDtamZ9quWAaq0BGGJLBTCEitNgsO2TH5hLhfn5oY-ndHa1wkaC3OJLQWWhTzET600yn7J7LmMRqSeQwVvqYHVIwxFMFQJ4wrmXxOL6-o5oO3hmHq8jCqkCmQujkvp9nnI8V9wq2MjJvp3D4jL5HupajMlNvJqzKmZO0NUMY9kNoARHlAphksCrULW9sWJwNDSkU3BtZC1kCCXYcYN6jKgKvPbqKqApG_3n4s3eKUynMUdzyNhB2IMyGsbVkeAKX0EB9S_9zmxFK1tGDhkalECG3uRrB39GfQFbfX_TBBmnMKLuPSdAZxtY7AcR2NEYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5d890016b.mp4?token=E_Qp6DQLgNtZox4PpM2kXAWDtamZ9quWAaq0BGGJLBTCEitNgsO2TH5hLhfn5oY-ndHa1wkaC3OJLQWWhTzET600yn7J7LmMRqSeQwVvqYHVIwxFMFQJ4wrmXxOL6-o5oO3hmHq8jCqkCmQujkvp9nnI8V9wq2MjJvp3D4jL5HupajMlNvJqzKmZO0NUMY9kNoARHlAphksCrULW9sWJwNDSkU3BtZC1kCCXYcYN6jKgKvPbqKqApG_3n4s3eKUynMUdzyNhB2IMyGsbVkeAKX0EB9S_9zmxFK1tGDhkalECG3uRrB39GfQFbfX_TBBmnMKLuPSdAZxtY7AcR2NEYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇶🇦
تجمع جمعی از جانفدایان بصره عراق در حمایت از استقلال برای بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/106428" target="_blank">📅 12:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106427">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c84cb00cc.mp4?token=pCiVrx38unhcfqTg6EDf4uOD5F1T6U6KvabUZH6q7pkqK0Jrqq3P93paM6iX9-3WuvQc7KpsBN3WOV1y2GgGio0mmaSFjtSZmw7guT9AE0sorBu8-81aVm4S-U7LGdZdzGb41LgVwrNpiOGcSEziU7wwIUE1_7d9Oa0DsV17Mbfy5jgr87UZiqfGJY-IjPJ1AV4paK7WiDqfsFNMWXulBEdpsA6GLouIC7KM_mSQPniMMIbJn8lpEahzXTOZ0P2vdWPIYYD7JX3ibSLCl0CM-6wdZNwzBdsRCYlmytL5G7iRC9xKypMJ4HguYhlLCXCyB7Pzl2Wh5aQhUHMgcrTGsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c84cb00cc.mp4?token=pCiVrx38unhcfqTg6EDf4uOD5F1T6U6KvabUZH6q7pkqK0Jrqq3P93paM6iX9-3WuvQc7KpsBN3WOV1y2GgGio0mmaSFjtSZmw7guT9AE0sorBu8-81aVm4S-U7LGdZdzGb41LgVwrNpiOGcSEziU7wwIUE1_7d9Oa0DsV17Mbfy5jgr87UZiqfGJY-IjPJ1AV4paK7WiDqfsFNMWXulBEdpsA6GLouIC7KM_mSQPniMMIbJn8lpEahzXTOZ0P2vdWPIYYD7JX3ibSLCl0CM-6wdZNwzBdsRCYlmytL5G7iRC9xKypMJ4HguYhlLCXCyB7Pzl2Wh5aQhUHMgcrTGsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
مترو های آمریکا رو‌ مسخره کردیم، اینم وضعیت مترو های خودمون! مردم انقدر درگیر مشکلات خودشونن اصلا اهمیت نمیدن بهش :))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/106427" target="_blank">📅 12:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106426">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCSGlb6Fl5Ck1-2qDxsQHGNmgxh8ceTOrrvDByniSXBzvNyQHxJiILvSMrQLLwAWlcZFLBkKCUsOKnYL3HCjzsve9DTXqw09YKk8k7kCOet6l_RiJYfR77S75qcdimkUeempbu1HE8Ms0U9RJlV83zhyluhp6eyJJR97CqEd7gGNKHbEh98TNdVYwX9veapgdIhhay34SwwzZj9t5slbDxjz7UyPwlB8lQ662IJxpLeg39o67Qxgcbb-OglQH9cdjUy6vGBkAACHZkGSM7KeGBSGRCkfq7w7Dwmg3XYv2k63yu5vaVaR93dLWz1vJraplAdfl01pF9VDbo2IOr5Irg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شکار بزرگ استقلال در کشتی آزاد
🔹
✔️
امیرعلی آذرپیرا دارنده مدال نقره جهان و برنز المپیک و ملی‌پوش ایران در بازی‌های آسیایی ناگویا در وزن ۹۷ کیلوگرم با عقد قراردادی به استقلال اراک پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/106426" target="_blank">📅 12:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106425">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106425" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/106425" target="_blank">📅 12:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106424">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKTajb_6bu0foR6UAWCNr8z-qek3sTvVVQpxPIB68mKz-wtl0bDuRtCYuA342Cy5BZd6CfJw1rdJ-tkAm7ycktU7RIV6nxOYr-R8p7ZpMA6d2vYP9jTr_RAsEYr5jXKBR3EKIt7MLa85uCWyVknQP1U4pUsYURWONIcICGHPmSzYv0OVfeUPCIWNohBkyrHia_lTRyEZpuohfUq8e0AVWkTRiflY8U9_rk9uMPMC12FCbrgrgx46JaS2BGFLAIrUSJxryf0_3HxgaNDpjtNFw15ecWV8PErc6i5Cj_jsd-VUVRmlZZ_Xn983M3SFnE24N7VbqQC0vKtZNVTo0eSiWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
نیوکاسل
🆚
لیدز
رم
🆚
تورینو
اودینزه
🆚
اینتر
السد
🆚
استقلال
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/106424" target="_blank">📅 12:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106423">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf78496549.mp4?token=sabXrF_ZtbPZN-9KO61zKmJiAWa1iG7z0lI5SCvvAg7xFUxz-3k9WvlbJCjLZwhvUB2tBZYuGQ5d44Z-Nlow1QKjnj5d7VVDMXSuKJ8W4dtdXxdidd2BoSLPraP3hMQb-Ofd6utTfR8orGfb42xaacxp8MBaZc8RKdiUrXWNyxFeqQcV4vSZHOLpHfNga0Yo0Lg0xs-vX69-KTdhcKpLeK7vbmPemtC6XNxp7gxY4OGXSTeh-_oHp-QI3IpebGFnxqOngLV0UoYZVR_pnxx6gk8eAjhz5wQwIrxOaWlqc6PLcdDfBQqu-fdPEsutpCvhD-D7N74hTvQSswRkpZCwcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf78496549.mp4?token=sabXrF_ZtbPZN-9KO61zKmJiAWa1iG7z0lI5SCvvAg7xFUxz-3k9WvlbJCjLZwhvUB2tBZYuGQ5d44Z-Nlow1QKjnj5d7VVDMXSuKJ8W4dtdXxdidd2BoSLPraP3hMQb-Ofd6utTfR8orGfb42xaacxp8MBaZc8RKdiUrXWNyxFeqQcV4vSZHOLpHfNga0Yo0Lg0xs-vX69-KTdhcKpLeK7vbmPemtC6XNxp7gxY4OGXSTeh-_oHp-QI3IpebGFnxqOngLV0UoYZVR_pnxx6gk8eAjhz5wQwIrxOaWlqc6PLcdDfBQqu-fdPEsutpCvhD-D7N74hTvQSswRkpZCwcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🇮🇷
🇶🇦
به مناسبت بازی استقلال و السد یادی‌کنیم از شبی که صدای صدهزار نفری و جو فوق سنگین استادیوم آزادی باعث گل‌خوردن السد از استقلال شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/106423" target="_blank">📅 11:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106422">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYIxSsW4XsxAjNrML9H9ZmoMa3Ts4iFC82heSdTyZ-i5M5S0gA99CT1tSLXlvq98utH_Y8zttaizQjdYArwwTTfQ61D2nOjw9w7WZv8q3e8BrllrxgkXvG0OdxjvilNDDYhw7tzSmt_oNVSSPpOhjEQR9-pVJoxri9nMoo5zlhTL1sHpRa86Fc4lmXXmg6EgOuHVS2OfrPDC0e5F86Lh9lUhfhzHWrdoYZkyb08p1f_pFlFjdey9N2LhgpRrIv7hgtwsHrF3I_Ol60QbPB-TLSWN93zh8Xr7SIPVZ0basO0AUqA1e_otuAv42rky9IWFImKZx_cVPqBXYUJhvBX75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
🟣
پوستر باشگاه استقلال ایران برای بازی با السد قطر با تصویری از حردانی و چشمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/106422" target="_blank">📅 11:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106421">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/285c0d29ad.mp4?token=l6acPDY_J5HB9XFyWZ6Y1eBdUM0xu_UYOV9YezsxbkavIDylarJqSOq5S43jIozdQSf--0HJJWcJX_nRbUCN9YkmEnTlgH1eiwhtE9Snd-yjMbtpUkq9pweEJnqHEsZykThwvW5rrfHgri7TBmhgzv2CQvb69hBkcEtWjbTYgNU67umF-ZGy2ZmgRRaovsdU5gv3FGjUnIwNzV-UZMaPm8s4Ey5h2l3jakCuXKK47vwhXmoDy3f98rYzszfZFVJx6GcuNj3q-riznbSIl50IqxQQIUJWB8G1qRqfWrusnXpYWX6sYe_u9_RRdFPYumLMIUvwl43Fa5ijcj6Z0oHKeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/285c0d29ad.mp4?token=l6acPDY_J5HB9XFyWZ6Y1eBdUM0xu_UYOV9YezsxbkavIDylarJqSOq5S43jIozdQSf--0HJJWcJX_nRbUCN9YkmEnTlgH1eiwhtE9Snd-yjMbtpUkq9pweEJnqHEsZykThwvW5rrfHgri7TBmhgzv2CQvb69hBkcEtWjbTYgNU67umF-ZGy2ZmgRRaovsdU5gv3FGjUnIwNzV-UZMaPm8s4Ey5h2l3jakCuXKK47vwhXmoDy3f98rYzszfZFVJx6GcuNj3q-riznbSIl50IqxQQIUJWB8G1qRqfWrusnXpYWX6sYe_u9_RRdFPYumLMIUvwl43Fa5ijcj6Z0oHKeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
هاشم بیک‌زاده: بعد از بردن کره‌جنوبی در سئول؛ سطل آب یخ را روی سر کیروش ریختم. هیچکس جرأت نداشت اینکار را بکند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/106421" target="_blank">📅 11:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106420">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErOy621D0WnsVJZMSTUD-lY0Jdn4Snz9Wzz_tzCzJeGqHpnAt4ZS2b9pcRpdHdN6YtC_qODOU7W06Dkamo-4ScCEDu1jP8IPBaj0k0RGo2RbvX8TA3H0axFTaxmf9S-N2h-lIFlD8vwpf0MpCH0FtApIwe81KCLVkAYliPKlMNd2mXS5nkQ6QzfK_TW_yM6G4KgU7-_TuWOZPE0hN8AXKVglaMSIXVnD64fwPpC_XWfGBTtNgqJNururDMWl0EC3wnd3W6920oQB-_x58Qrr-FjHQu3VQJrIrb4J9ktEfGxbvz6psRUVflcOySqHeV0FSnrQjuTXXqYZ2FExBsgNTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
دیدار استقلال و تراکتور در هفته هشتم لیگ‌برتر روز پنجشنبه ۱۶ مهرماه در ورزشگاه تبریز برگزار می‌شود. بزودی برنامه هفته‌های آینده لیگ‌برتر اعلام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106420" target="_blank">📅 10:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106419">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbf719687.mp4?token=nD5pkqfLaoZvZOdKVJuxM8NLKNJsIw1Pi0CGaP9PjcYq21krJf8IKZhzzVefyt2gNCUFA1wXWfxC3tiKyg_l8qvlPikngdPLQgjCn1lR4BGZms02Az9Y6P4fZJBSFl8p4y2DstuHfk4InnyleXGSBG6X-ulF5ALqNIaMxSZj0u6cCSqTqhuSmEPNq6WnSdFBlqHrPsIKMSnC7hwfFok_b7TpeX_Xii1JlLxS6S8-ikcwSyzXrkdIHfK2-lmPdZBuHGuN1kbp3LeOxqMZpaPQLKuxvswGf1MQAzLgsUQsRWbGVfSfxcc3xhuNXKiKHIki_H43JKBOWVVrL2usBujxMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbf719687.mp4?token=nD5pkqfLaoZvZOdKVJuxM8NLKNJsIw1Pi0CGaP9PjcYq21krJf8IKZhzzVefyt2gNCUFA1wXWfxC3tiKyg_l8qvlPikngdPLQgjCn1lR4BGZms02Az9Y6P4fZJBSFl8p4y2DstuHfk4InnyleXGSBG6X-ulF5ALqNIaMxSZj0u6cCSqTqhuSmEPNq6WnSdFBlqHrPsIKMSnC7hwfFok_b7TpeX_Xii1JlLxS6S8-ikcwSyzXrkdIHfK2-lmPdZBuHGuN1kbp3LeOxqMZpaPQLKuxvswGf1MQAzLgsUQsRWbGVfSfxcc3xhuNXKiKHIki_H43JKBOWVVrL2usBujxMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
🏆
بالاخره امباپه فاتح توپ‌طلا میشه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106419" target="_blank">📅 10:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106413">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rfaC698X-ha5sQhLWHfM7Iod4DPlA1KpB7dvFSaxEncxbO8GruazwE-S_zPnPybY2VCx4sJC_JCyaOKq1pX9pdn4fAbt15wG-sj6N4wK2fTLOnF2Jq1zdwuyu9G9Ti9ME2TI59WztQ6PJ_r_gQ7OXXF212TNQqF6uMe0IOiNIeLB03W_Y6dNt3XquqxU2fXwdZQQQ-8WBrXrzVNKIA4nQXbE5rNjwWT743JYBnsTpn7BqCXWLi2mZfglvrUbO7KGGcDWN5I7pLHmy5sTyt9bxfSmqox_vzaTcDiXGKrRdOpIy8cz8O_C52fu6K4Kwgm29jUHi9M03mvNAsq8xDNafQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BS-PfoWFcAppVsF7f1IPk1hWIkeLdUM7pn2S_AoacwaKIKf1k94sf9VaS2Twl-43w2HVQljWB3zdFpvdD1_TRKfRHzy0ELDJOm5LkTN50Rrj6YQAsoY_0tXjA6HHrVWzGzXbRSD0JJeXdxxljJzlgfkj38oYM4x3qeqxRTMahwKOgTUSsCX9dX4syCFu1Yf_2NqqsUBBgezuyNrcHVzRvSlw-ZjckUqpZcmC04jSMVgnFgBqNIk6fYuYYWrn7kRZCXGnNf5TW_RL-JU4VxBUPJ4o3rMavIu0y-hNdAfLgq5V20c-euK1svPntwiuFFLTSh5s2WbT9VrUI6iTLqSWKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j_zRck-ozRjhCJtT1xFwB1WyGOwUFFZDpgBeQds3cHb4TjNjBNDETwgxvmnHRTlkOChRQnl0QNRNR5RR6zEYy_BTzQ1PRi3fMBZy8ffKu-zcrI09C_gjhrl2mooJn4g6Y3pgQGaf8s2EEhlHgEYBuNtVRccJZXJEGD8JALfi08AqXI8lnYTIsleEm_hvi7jKVNp0ZYJbDJyxwFRuxeZutOcWkzxhqpwX3YDOdH-6bbr0zXloIwS5bSm1mXkruy9zuQncZOpuoT6wguLtoUZjnQ1fRVETALnEEk2mFv_AQnnN7u4ykn_WDiqbGx1E9S1kg96fOmDlesmVmBt0ywPdJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fKkgGqr9-M7ffQ-mElJjLcP9csMu0TIXQe5UaFxyHmC8DGFQ223n9gRq11GoJNYEhrkWXvswjvWN-hbq6T-NMmrU8lhO-OO4OUCtjGVHx1HCIdbu9_VSzl9u8TBrORl2YQHHxYthF4JMBnzq8d8P0jDjeGW-fWpbm8ShMt_OzJmneWPkTTwOygzbkSC0oX6f4MFKNTWe7XPncfLDM1aFn4_7-J7YXrrhRK5FiNOgZWhLIuhUgpVyxhn3ARTPSRz73zhXCuBM9565pZUXWLhPzMI4r0ObKG_2EsdTdEGDt7BzQ-6HP20M3L3SiIKH_aMEVIkbiepWL7VLeOPuFWTrYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GpxmpTF526twEuvpLQI87mzLbt8UnnPRtqNg6gCx-S_tbRqyhmT__BXyQrraMboDOuwnj5mZ1kA2-DV4S9Dhlfkwg3cs1b4DbVOdVk9xw4zbAYpexg8BCI29o0WTN-YlzHys4An-d1bUNpYC9oxhoLIfOw-aDyCPeXkzn61sS9-NdydXVAPYYfEoaJvcIxJL7fp-B6DG-iY0FPlt9hdsF4a0jcdwZVkSUBZZFvgS6MNMO0L1Tygbd06w5dP21OIco6AYV7KQzevu4sVlE666J_k2QQrJKNRDtD93ClPT0Q2gR6UdIA0Ond4CeSks9Ik1dCVwfGXeJvXTLlubD5Y4dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f3acf7nKeXpJxkhG4p4ngmB9ErV8dC70Nnci6wlXx6esFdL_tlmUzLSW7mHZMibIiE1qAWEF_IPR4Max0qaXZROTusGX4HYUjjMwKOE4nDuXtUe5Q2CxF6nnHbiWyc3AC7rlsjZGvaqpTG-zFeBDTvA5imNIpMa1yQZzFvUsW1qCcIQuN_qiGU6viYsaIdh5p8v1PW3y6YbH-4TOptwLUFvnTE7yrXM9CsxXPdbjW9tfLiWtQzCjhc63g8qJtZ5e30CA88wqCPk1Xx9O9yHJiZtptwzmD20ED0OdUjxDICIE4cON2yzyLzh1nAQpeoIrgZgovmzedAOxM2NNYPXXLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
👀
بعد میگن پول تاثیر زیادی نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106413" target="_blank">📅 10:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106412">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dcc7c68b4.mp4?token=LGpd-J4J8psFkcfz9Gq8IhDhwXcC6DZEw7ccFDjaoQfdJEYItJiawXPMpC9vCzeVPEk54ylKLsN6d0NehSnsfkDV6qXTu7pYn4QZD8UKnImxktAM-VVJmLJ_knpTaqpnilyoy8pIIXarCVXcs4mGPlHn3SGpKsXeWzz7-T-cCGm99141Due1o56sHeKq9xl6BYNm1WAxEwFPxuOPwjge8v-IieIdb9o0fhh3mJ5SeRxLM5kkqgKIyNg_7qO8ku_WbrigLVaHqG9tEu9CaVkwcXkran2KmFSUyZCftE5leMqLxay0fpIAW7p1uvqshhjv-zYzZbq8T6Q2cLN8DZdoz509OR2PrRoKvMVXrJzpZ5r7rPwI5FzNfPU77JqDGuFqdnt6o3tapQjBc8WUvPMwjYy2oYj58gdYnhJE_Bzv6oiUOYhxDnK40DsQylA6Az_RY9CRlswz6HquLY1owQEn-B_0WAvAkUi0WVf09PiJs_TqGxpLbw2KhcbirHac7nPCdIYCjtJj3vVt828DpqykKs_6fRl4sQ6uerYdTp8kr-0fyiPD_pK7NHHbapPsjLp0-85vIRdXhbPkes06UspDGbCePsbGpOFJbeBPzSLrdjkWqeYWRjrpUYjIT3anwBsl9hS8i_64Rlw3VXTkt9HWIBAzMW1M1pR-KDiVpR2bB60" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dcc7c68b4.mp4?token=LGpd-J4J8psFkcfz9Gq8IhDhwXcC6DZEw7ccFDjaoQfdJEYItJiawXPMpC9vCzeVPEk54ylKLsN6d0NehSnsfkDV6qXTu7pYn4QZD8UKnImxktAM-VVJmLJ_knpTaqpnilyoy8pIIXarCVXcs4mGPlHn3SGpKsXeWzz7-T-cCGm99141Due1o56sHeKq9xl6BYNm1WAxEwFPxuOPwjge8v-IieIdb9o0fhh3mJ5SeRxLM5kkqgKIyNg_7qO8ku_WbrigLVaHqG9tEu9CaVkwcXkran2KmFSUyZCftE5leMqLxay0fpIAW7p1uvqshhjv-zYzZbq8T6Q2cLN8DZdoz509OR2PrRoKvMVXrJzpZ5r7rPwI5FzNfPU77JqDGuFqdnt6o3tapQjBc8WUvPMwjYy2oYj58gdYnhJE_Bzv6oiUOYhxDnK40DsQylA6Az_RY9CRlswz6HquLY1owQEn-B_0WAvAkUi0WVf09PiJs_TqGxpLbw2KhcbirHac7nPCdIYCjtJj3vVt828DpqykKs_6fRl4sQ6uerYdTp8kr-0fyiPD_pK7NHHbapPsjLp0-85vIRdXhbPkes06UspDGbCePsbGpOFJbeBPzSLrdjkWqeYWRjrpUYjIT3anwBsl9hS8i_64Rlw3VXTkt9HWIBAzMW1M1pR-KDiVpR2bB60" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤡
وقتی هادی‌چوپان میگه هانی‌رامبد رزومه نداره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106412" target="_blank">📅 09:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106411">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5d091739.mp4?token=lJlK6SQQYbTnOD0tVgB-UW4DypvQt8AoOaKbF_h-MTLsXnP2QzfrgIIDvviTNzADYkpVcSatBb8wl9AbGBh7E93ZB2Ftzbt1z1KDMd3DYZnGhvE3eCNtFSFy1vcOJPwRSLPuQ4w4dZ1vRO0vB-cEKEmBbF7AQ4hcBjnSQMzdaiO9WxehtAKYYUx2e5KPIH-2ZZluejqcK4DKyyx8qUiaZ9MV0NdnnKg5jOKTO-gxNY8P2lUoLKqa_-22C9UUauIEkFVVMfb9P3vgYjydXWxemkBBfT1BK2ZWvlV48bHYCCz7Wef9vCEXP3Wm0FsYsMnCacJIdUFzxBhbawmg7tEguw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5d091739.mp4?token=lJlK6SQQYbTnOD0tVgB-UW4DypvQt8AoOaKbF_h-MTLsXnP2QzfrgIIDvviTNzADYkpVcSatBb8wl9AbGBh7E93ZB2Ftzbt1z1KDMd3DYZnGhvE3eCNtFSFy1vcOJPwRSLPuQ4w4dZ1vRO0vB-cEKEmBbF7AQ4hcBjnSQMzdaiO9WxehtAKYYUx2e5KPIH-2ZZluejqcK4DKyyx8qUiaZ9MV0NdnnKg5jOKTO-gxNY8P2lUoLKqa_-22C9UUauIEkFVVMfb9P3vgYjydXWxemkBBfT1BK2ZWvlV48bHYCCz7Wef9vCEXP3Wm0FsYsMnCacJIdUFzxBhbawmg7tEguw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هالند: خیلی دوست و رفیق صمیمی طرفدار منچستریونایتد دارم و قبل از بازی کلی برام کری خوندن، حالا باید یکم واسشون کری بخونم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106411" target="_blank">📅 09:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106410">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‼️
🎙
حاشیه عجیب مصاحبه خبرنگاران با اسطوره علی‌دایی درباره صنعت خودرو ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106410" target="_blank">📅 09:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106409">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514af894b9.mp4?token=bNzEfznpJi5Ks8WPvJOy3P4BYr2gFNaVAiQHqhOJ1-9Oe5uuoIXlAxVvtRITNIEVsyRN2pT2xdcfyzteevr5mh4j9HjrS25-fsx4UaEsLCuANuOJTq5cKQppG2TDucuQnG-Ql1BOjltepw6pui6hbSb3jGBYuWo6oVqGvz7uWnlvFP1lXLXqqc_ctc32DwaC-7N6W3sk4yf7LMGX06XOiMYLSDwgeZW2S5oInhK88pwKxfuvmQ_scB7Aq1HBvaUwR3RGxJD6YmBPwLYJx-nZhCG14JeYYZaXG8nPbHwC580uJQ28sfM869AqlGSvLC07BXG5bMK3bYIXZpOa9xrsWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514af894b9.mp4?token=bNzEfznpJi5Ks8WPvJOy3P4BYr2gFNaVAiQHqhOJ1-9Oe5uuoIXlAxVvtRITNIEVsyRN2pT2xdcfyzteevr5mh4j9HjrS25-fsx4UaEsLCuANuOJTq5cKQppG2TDucuQnG-Ql1BOjltepw6pui6hbSb3jGBYuWo6oVqGvz7uWnlvFP1lXLXqqc_ctc32DwaC-7N6W3sk4yf7LMGX06XOiMYLSDwgeZW2S5oInhK88pwKxfuvmQ_scB7Aq1HBvaUwR3RGxJD6YmBPwLYJx-nZhCG14JeYYZaXG8nPbHwC580uJQ28sfM869AqlGSvLC07BXG5bMK3bYIXZpOa9xrsWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نتایج ترسناک بارسا همچنان ادامه داره. 100% پیروزی تا اینجای فصل!
👀
☠️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106409" target="_blank">📅 08:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106408">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
جزئیات تازه از نجات دو خلبان F-15E آمریکا پس از سقوط در ایران
🔸
برنامه «۶۰ دقیقه» تصاویری تازه و از طبقه‌بندی خارج‌شده منتشر کرده که عملیات نجات دو خدمه جنگنده F-15E آمریکا با نام‌های رمزی «آلفا» و «براوو» را پس از سرنگونی هواپیمایشان بر فراز ایران نشان می‌دهد.
🔸
این دو نفر با فاصله حدود ۵ کیلومتری از یکدیگر در مناطق کوهستانی جنوب اصفهان فرود آمدند. «آلفا» پس از ۸ ساعت، در عملیاتی با مشارکت ۲۱ فروند هواپیمای آمریکایی نجات یافت.
🔸
«براوو» نزدیک به دو روز در خاک ایران باقی ماند و با وجود شکستگی کمر و جراحات ناشی از فرود سخت، خود را از یک مسیر کوهستانی تا ارتفاع حدود ۲۱۰۰ متر عبور داد تا سرانجام نیروهای امدادی آمریکا به او رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106408" target="_blank">📅 07:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106407">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106407" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106407" target="_blank">📅 01:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106406">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGOEI3IWGbvTkAq39tAI_iBS3RExHU-Nn_wY8kQu3sYcXgGvjAHYL3ytWyCAvrKmJna5A1rDWadLa_RkXJHxfzl3FNmab7POPtItP9bz1OEcuaY3yi9FHGKspOxL8mprlpVVkAHPrLlzHxuTtltBCdJCy0fPjYrXxKojst9Nl5QFcABcF_yaxEf5YKROQh6Tn9Qj3xyvwFTyBdJiiG6g3nh0Ov3RVEEVjGtQMCu5tXsmiTvbjPfID9XZbLHJoEjmFYBZ1SloogCxDcv26YklSVxPJ70nBLetM1tB4Sr5sqMZji3OzJ2P84ECQkWdDlm32U4DRTt5gIwbHPE0okV7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106406" target="_blank">📅 01:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106405">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106405" target="_blank">📅 01:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106404">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔻
🔥
🏆
لامین‌یامال: من و امباپه بهترین بازیکنان دنیا هستیم و توپ‌طلا باید به بهترین‌ها داده بشه. بنظرم فصل‌گذشته عملکرد من گویای همه‌چیز برای انتخاب شدن است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106404" target="_blank">📅 01:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106403">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uj4wY0eMFqorPcqPqkyKmvaDmvBwlwUmmOlazintdSlyWdls-RLohbsIleWqJWliPtgXL6_NvOBgv6nEpct3nWOyQIl6W3O3OPJLE9N7058wZSZ29NyzfOHJsv9tK-QNjlMef_d5UlLLto0rbZDmvoh0fyPLhGTdTnvsKKGkzkQrknnHMLQSTSsTV9ztrO9PMDRthVOMAh0NM-pzg9XCx3I82nxbOcNf5x9xpoFSAo1lmnsZWwltVjP1T_vnHhFYVNLkqfKs3oKy3QuKTvsHALNvuS82AtyUP-WfL6KJ-V8duTvC0-aJHqaGc7iCOUjQZBiGySkt2cgT7V6LBBbxFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
بالا گرفتن جنگ توپ‌طلا؛ لامین یامال: «فکر می‌کنم امسال به خاطر چیزهایی که به دست آوردم، شایسته توپ طلا هستم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106403" target="_blank">📅 01:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106402">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poBmRSgoCX1g7nKDMRkua5OYDUHv_ihuA6nywmH7Jpzaad_Kjec_zJoO-lwmQvIXpTwHJJf-SYIakSsTHRCGAcnw1toBRWYra3GdszwN6mKLC1Jg-dgElME-hUtMdGMnKGUAdwjEPR_fKSsW-HCka-Egzjx-0MKaPCon1Hr6olR6la_wLrE5eYPx-J5DsK-HwL-J3lHP5NkhgLsF7xG1UeCOTtMJJxP6luCMPm_TP1sghiTKoJlqwZZ3hQR5qk_R-xNDwNZ6wqAXYA3jHAn1vdyZ3PWEYG1vdqd_LxV45P37xBfMfqu76Mi4znoKRnk68Co5N4JNJY8jwyd2yvjtGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
بالا گرفتن جنگ توپ‌طلا؛ لامین یامال: «فکر می‌کنم امسال به خاطر چیزهایی که به دست آوردم، شایسته توپ طلا هستم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106402" target="_blank">📅 01:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106401">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhXNST936FC-fg6llheVdOHzIpJDTr2J8YDZ0dKkkxnY5M2eI8yB9KhUBr2VLKDbWuiMUdXC1nY2nJtSdY8FHDHsnDx83JmS6IDMmeAwrGk6SW30Ntw9TZqONs3qAUUv7wiOGuumKn9rKN0M2vvXZ0-rtpQs5TMPOV01DnempyaYIrD6RR08vjDCJxhyLpyFDTejAAk7dRfnHVEEP_Rvrt8Jw_rN3VEwfi2MZOdDCKSF-OmXjH04Hf4_HOX6IOJ1XMWwEGeMRutAh5cNCN-PDdQYihJwsj-lemNShgnDvoE1c1Kb1zq2iyonuDh5LhpEXsCMgEgP0iDPP0knp9zJ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🧕
بیانیه کمیته داوری انگلیس: "داوران تصمیم گرفتند که هالند در آفساید نبوده و همچنین تشخیص دادند که انزو فرناندز به توپ دست نزده و دخالتی آشکار نداشته است."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106401" target="_blank">📅 00:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106400">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8675062324.mp4?token=hA-QPFnSAfVEwsvmQ0r2P1ss9lv--5ijgKB0swV3mWSIvdO93iXwL_XWbd-9bJGi3MZH9xaWiIBWDceeMWUamg8u3bU7408SM4P4ATPMuGk8y6C6_pq2QEma3snGbY3eavTafJ_lFIT5xuWEU6u4cKPQxUqe6kodRWGaDrAQi4o76gzChfB5HlRmmPIk4FDcvEqLSZIXISvT6jszhoBOIdP33zmnV2FRkf19eD2P1Sg6kAz47aRl8pnD_RFf1VR5DgjXDDbwSxnT2q27gCC-Ku0WrHzjm8VsM6XPjlMM6wgAfA8aEx4bdgQ-TpF8N9o-GLc_53pNa-g3BM0AwzwVDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8675062324.mp4?token=hA-QPFnSAfVEwsvmQ0r2P1ss9lv--5ijgKB0swV3mWSIvdO93iXwL_XWbd-9bJGi3MZH9xaWiIBWDceeMWUamg8u3bU7408SM4P4ATPMuGk8y6C6_pq2QEma3snGbY3eavTafJ_lFIT5xuWEU6u4cKPQxUqe6kodRWGaDrAQi4o76gzChfB5HlRmmPIk4FDcvEqLSZIXISvT6jszhoBOIdP33zmnV2FRkf19eD2P1Sg6kAz47aRl8pnD_RFf1VR5DgjXDDbwSxnT2q27gCC-Ku0WrHzjm8VsM6XPjlMM6wgAfA8aEx4bdgQ-TpF8N9o-GLc_53pNa-g3BM0AwzwVDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇫🇷
🇫🇷
پاری‌سن‌ژرمن با تک‌گل‌ فران‌تورس امشب مقابل برست برنده شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106400" target="_blank">📅 00:13 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106399">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THyI6hXSHUslNQwQUzDEkMxsjJdnmuR9TKiYm5_Sugw0fJjCNCydf2bYxii5NavT9JLT40_AgkOH11gFkt8eIqVmtemIfYs7f9shjdrmnMZwuNVIwCJwHiju7wbJRw4fFaezuPTFIL8wIvjD09rtC5l-Wze4tcEu8ThWrQCAsnW4N6-t0jA_9xSz25qEsxDeATb2OyKMRi9yVX8H-Sjolw6rdFmUh49-2AQEAt_wrZM8KC6kyMm7x2pR7ya3KXN9QEfIkPvVjBW1fsrde9kBzQnAp5TpHVKqdfV1lGFdrzJgXpIcfQ98k9Jm0BKw96QbAqaBUn8PX8gtTdvJIwmDfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
افشاگری پشم‌ریزون نشریه سان:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔺
شین دافی، بازیکن سابق برایتون، برای یه تماس تصویری پنج ساعته از نصف‌شب تا حدود ۷ صبح، به کلی بلیک، مدل انلی فنز، ۱۱۰۰ پوند داده. بلیک گفته دافی توی این پنج ساعت بهش گفته چطوری لباس بپوشه و لباس زیرهاش چه رنگی باشن. بلیک حدس می‌زنه که دافی می‌خواسته اون شبیه اکسش لباس بپوشه و مثل اون بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106399" target="_blank">📅 00:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106398">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxqBjWbGToUgCYBXK3vcymMEGXQcyiGBqBsbqKEtRYulYJD73AT8ryJLz6jVOZFUzzooJ_vsj_EdbgYFEhc7hMiIZvfWNIOb1ala05-4kUvFCV5K9v-gDIFlSkWYwpiDGgbtl6C-kptwgp5ANx0eWSSZl_zm9vNI98SSauQhaYkzGYJW-giC-8V7ONqGdU7qpYvDTdTJTLKElCLI3t-UxtivXFBqFFqbWs1DJ0g0Gv3BTJTGz5hKnX47UttG7_lZ38R6Dh8UII02RClU2sRbixRLeDvxBCbvfAKxNbcjR0Ac53KWiil73279Yhk0yneazzFIWe_klAbhMq9DWMfuLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
محمدخدابنده‌لو رفیق صمیمی اورونوف
:
🔻
چند روز پیش از اورونوف راجب شایعات جدا شدنش از پرسپولیس و رفتنش به یک تیم دیگه از ایران پرسیدم که با پوزخند بهم گفت که در لیگ‌برتر ایران فقط انتخابش به احترام ۴۰ میلیون هوادار پرسپولیسه و در صورت جدایی در آینده دور، مقصدی خارج از کشور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106398" target="_blank">📅 23:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106397">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcBC1Jk0-MvLq-k3P8oI_hLQnzsJb7iPWHRABemxR_M2pet2L32LmT_GpyAqbH2M8HmONnIJp46Ay4VEouybJgT0VXnC-db-6iNMRrcuPIkMwAvMhOlr8uAgS2q3PIMa4TIP43qsqeOtdPsipHYJtItwVXwGRjSQPHcetGq9WzYhCNd7Ff4o1TFgbx5MZ3vJPYGPM8spzQfOEAqbM3iryVpHvezdmr9oeEY8EDiKPQz1xlhylr3kKASziWnUwaYyK7bB9e6nPcrlG8XFthGp2SSN4YvvsOvXEQcxGnl9lRFcUj8YyCYMcmS_zcBxy7dmy-EAH79eG4Cht4RS_gLkPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⚽️
یحیی‌گل‌محمدی در ادامه روند فوق ضعیف در لیگ‌عراق، مقابل حریفش شکست خورد تا زمزمه اخراج این سرمربی پرافتخار از تیم دهوک هر لحظه به واقعیت نزدیک شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106397" target="_blank">📅 23:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106396">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4S-EIz2IKcZLgjz68tgJWQ1YIhzzehPOgzMBZEdT3b_mC8kAmt4KplUTdF2gPDtcXhnwwulSzTJ3qIVl8-TOah3JzcI1amHH2WmvofnV4of6itML40Bm1FLTcR0pHoCtP84lDeS20dFWX1BADtokGjXlBO1DmSHFT9uuvUvhwcTVXv3ZM9dSf6a2la2cDtpiUAbCji1h03hsRI3mLw0u93S1Pt8P1tsd2zfql-x4GPay04p2uAbF8M6p0e4RbEUHX6mp9dslT6G7guipEBLEXv1DmmzXvFPlV6hOXyGbh-yj_12Ozh9eVqN38oMopQYyYD7pCtzew0MFlb8gSwo3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
👤
علیرضا بیرانوند: به عنوان یک سرباز جان بر کف ایران و اسلام، آماده رفتن به خط مقدم و خدمت مقدس سربازی هستم و از اول مهر به هر تیمی که معرفی شوم حضور پیدا خواهم کرد و در زیر این پرچم مقدس به انجام وظیفه خواهم پرداخت
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/106396" target="_blank">📅 23:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106395">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
📹
آرشیو وار: گل ارلینگ‌هالند آفساید بود و نباید از سوی وار تایید میشد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/106395" target="_blank">📅 22:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106394">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b66e5d4924.mp4?token=ByxMDWKR6lAXUa8dY1GERHg771suFSDexuQmwjuQqKxRMncDsdsSajqtjCDWhP_Qh5iVYPebpQVGhwUD2eyr1eQuIg_umehzYu8VpPvOM5-5YBYhujpV7TH0UY5XkG1UCX4kk7Y9K-hzo3UkYnU91xphes5f5A6OC9dnMyDDH-QWkjNYuYzsac8SRJqe6q7MbwsvIldqazP22vFOAxb8X83wdmx8rE4rlMODn5pIFlvVCPUFuleU-Ujr3mZXcjJ3gYRHtbcc_8L1IzsmS9uj-z5xqVA0EEr_f4Ncrp53PZXlUPte3jsnfTRxK8fsKNqbecPxWit1kL1nrzueWIkxHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b66e5d4924.mp4?token=ByxMDWKR6lAXUa8dY1GERHg771suFSDexuQmwjuQqKxRMncDsdsSajqtjCDWhP_Qh5iVYPebpQVGhwUD2eyr1eQuIg_umehzYu8VpPvOM5-5YBYhujpV7TH0UY5XkG1UCX4kk7Y9K-hzo3UkYnU91xphes5f5A6OC9dnMyDDH-QWkjNYuYzsac8SRJqe6q7MbwsvIldqazP22vFOAxb8X83wdmx8rE4rlMODn5pIFlvVCPUFuleU-Ujr3mZXcjJ3gYRHtbcc_8L1IzsmS9uj-z5xqVA0EEr_f4Ncrp53PZXlUPte3jsnfTRxK8fsKNqbecPxWit1kL1nrzueWIkxHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
بازگشا: با احترام به وحید هاشمیان، تعداد مصاحبه‌های او از تعداد دفعاتی که روی نیمکت پرسپولیس نشسته است بیشتر شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/106394" target="_blank">📅 22:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106393">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44897a1039.mp4?token=Zv2edYXlDyo6XgEKc8kPFDB3_uLVsZpM22gIZfnxoIbTs8hjow1XPfe40vJJEnxxDk141oOcCW7vz9CKOvE45OFuaiLK1A1w9WVcGZnY-tTKSSlVoQDDdEHDtYQ2wWxvSQisoRI_WasqqQsR_FoG0eNSK7zgxPdWgd3fEumlDgiG8ggV74zIF2tx4OAnNczzZrh-H-WdwSJhwIGn-SoWUc-bEgO2YS0-TgYe0sSYemt7kU53Cd_W_gK7Priu34oepeQUdBhkUC4pnFFZgOBnfeDRMkd41njmxmUXT60aj_yfsHTY411YQbjEahLli_4pWF8kkJATVACw0tnVQFKHJ08Z2LTKmQACJxRu4hpnCgk00SkpVk6Dk2-xl5TFk-TsqDYgw0d0SbviH8FkJWWUTzNANU36JzhiKAC9ITB2gLWxsvTi75oC7Wvwd-55pY55pYkgIxoWe-CG_pnGVvnoavqVtwaDIcAwwMigOiHAD7ImWQw1yjhvMNXHhnYwwal4TAMEszrM8uuV6YtvXqmiVPVHvjGtnbUzFxDYFssxDLqGiTjX0LE9Jatjc0VVRugC7WctU3c5heutTYey4-o36QkED-QcuwJ82D2qzEfzBiSl1bkmTwjJxWgPbZOsnyC2-nUNacWNUNxkjkJXzqGyP-DTm4Myud_Esuy1YXsKgKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44897a1039.mp4?token=Zv2edYXlDyo6XgEKc8kPFDB3_uLVsZpM22gIZfnxoIbTs8hjow1XPfe40vJJEnxxDk141oOcCW7vz9CKOvE45OFuaiLK1A1w9WVcGZnY-tTKSSlVoQDDdEHDtYQ2wWxvSQisoRI_WasqqQsR_FoG0eNSK7zgxPdWgd3fEumlDgiG8ggV74zIF2tx4OAnNczzZrh-H-WdwSJhwIGn-SoWUc-bEgO2YS0-TgYe0sSYemt7kU53Cd_W_gK7Priu34oepeQUdBhkUC4pnFFZgOBnfeDRMkd41njmxmUXT60aj_yfsHTY411YQbjEahLli_4pWF8kkJATVACw0tnVQFKHJ08Z2LTKmQACJxRu4hpnCgk00SkpVk6Dk2-xl5TFk-TsqDYgw0d0SbviH8FkJWWUTzNANU36JzhiKAC9ITB2gLWxsvTi75oC7Wvwd-55pY55pYkgIxoWe-CG_pnGVvnoavqVtwaDIcAwwMigOiHAD7ImWQw1yjhvMNXHhnYwwal4TAMEszrM8uuV6YtvXqmiVPVHvjGtnbUzFxDYFssxDLqGiTjX0LE9Jatjc0VVRugC7WctU3c5heutTYey4-o36QkED-QcuwJ82D2qzEfzBiSl1bkmTwjJxWgPbZOsnyC2-nUNacWNUNxkjkJXzqGyP-DTm4Myud_Esuy1YXsKgKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
بازیکنان رئال‌مادرید در گاراژ مرسدس بنز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/106393" target="_blank">📅 21:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106392">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1IGb7xf7MkHEC70MmJ5MJLJJIr5Qrmy3FNlazU8nwc468W_4vhlrmemvh5mOzUDi29D-mnRxVhYXerrYynfAYxS4v_pqf1bhJ3pdzB0KGekNKJPyW_GeiQuEyJA5XGQkQr5ichxATKpcigKHxy6DNqZds3yV5SCVWxzLN5FEPWUy0RSgLQ5GIsPmcFp1CPVi_cBRLGsFfy-Ij1QDvFGDJeKwnLxQ_P6p8XS2i05efmIEZHfi0ytcdmkBrdUWMzz4pcol2Qz0wEaDDoQx1_ssdwjiwSsfvZwzmNrDkLYXA-42OwdNo_D6BIhex9pxqeuds_mFXoRN1i0htIJW5lwvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب اتلتیکومادرید مقابل سوسیه‌داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/106392" target="_blank">📅 21:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106391">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkxLwMG4U2wCeunBlIoDCF6NBAGSRogXqLzlK5d3XtA0r2PJcIHV205QImLbHs9zuFWsR9v6uyhAJrgme8WaEctxZFvw-YaubILIGbn1ZLEoz2XFhMFcXVaZ7KGC21kC5uOuT43Cw8TAKA_Y6kr6MCQdaAhqQz6vpN3gKC_hWvhVs002w0sWm3FrTs5fn8bdvcRjFSRlylxJUIbnr3wnhtST8-6wgVy6p_fyhg-Olm_xTTt7ORJrGWu_06f1OnoFVZ-orN1XFrHA4_MFYmad1-mB-DghhNSA8qASGeiHHvSzDwJW7XAxFWXG-x3vVVQqj2GT58aGR-hOjueZHuN_Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔥
🔥
ارلینگ‌هالند بهترین گلزن پریمیرلیگ با ۴ گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106391" target="_blank">📅 21:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106389">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZcTFcWYLfVklqmadq2QbvsqCQ1uVrQnxvoboqguSFmIE6Ubd2hS386QiYGSYAk1XorEaqYMVPjErYnreOJwTSwHB5ibxLlWglUwgmbgd9NAN87-c8en8zQatZ2AUQzx0JVd0Z0tPNeITlHcyw0I68RSA6VzN-Vo5vO5ufom_4oMQlT87sZQxg4ZXS20GfREUYxfMvgURDEld6fhWaNATeLMBlp48m75vzDxqJ7pejohNjDHMu6u6XCVQff3b56Ybdnb_Y5bKNhtU7SyeOi4C8HZ0k4kDM37cqzhihKFkhQNvml1KEmGS8xr2LRpGW_RWUqqOZAMLh8Q_NzFzySUUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tGEq7ok70LfoUK7utCusLxuF_SblP5cAow3lRV6ZQIz--rni1mrWjbIVO-X7MG41tIyZj4cTxzoF6sbd6g0pIEalKByrtkyuT4BqUnJ6z2lvQR46OTEjJcj3TGOYNJZF85UIgOtIf7SlNcVxVjFyhE9YBCHeIehzh7Iykf9KBV18S9fggPb69ggs_vqivI5hLrS8qIXa-yUugGyf6mI-l7o3KP5GYmxJqGaEAFkTt9UMKP0PIDx0XDCq2nS_zNBLAJp6yqEnaGSFZqwCGgLsPsJF6uF-zd2kExw9qd-JHW3rPiyZ9BNexRR0lOE3vwPDX4qcJCQoL9bRdEMA5D9jVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول منچسترسیتی ده نفره به یونایتد
⚽️
هالنددددددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106389" target="_blank">📅 20:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106388">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/05e9e2f327.mp4?token=pPn1PGvzoNKhbGu8XFQKBkY3DT5Y_rJx8Bg3Gm8C2Dykffl-_QGdACqyLD1zilWtt4Ymnn1PPQRlINH5cX2JKxY0zBIxIAME9fBWphlKUE6q4EOEHJT-cuSIniSn3znIUFxp_e6rlWLrfD0bfUDoDVE0p1UUcpc7QYzlvXtDli-r0gY-1Xtr4E_55Q8K22bPJ7kP6RABoRyjYVJsfGFXaxkqaWwVXd8HAuD8FbFd-5lPFIvQWUeAJRn0ypnovoYMZS0NDhz5fkNpPIPI4gpHRsp-5BhzCJX4u8KEEWoZA01AoQbAe7eP_N5_mJD9ADPNK1Ke-5j1floKzv6HQ9BNtivSpL22IZMh4N72GJhdUhsYl7ZV1wxNXyb0-HK365oX4PJtCuCklgUr_LUdy3GyTn7P_4N2id02ik46DZPIX3fDDgXUi8plVWVqNi1njVv-UB6Gz5BAIUOrzvtoL7bOCayUO9GS6Of1pYOY1okXJQYB0ntqwkjeRZcjK8kL01LO5tqMTtF9BqCwhB4DsxIq9xtDF3PZpfqWR5hOJxZG3d0o9pogJ8DJgm88TI0kXZ6jvQ0R11X4q_Yg6HMSdA0RKUY9JogUp8Wtl6ob5_n4hbXxVhgXZJ_7LuQGKhybHjkuRkbteUJ3EwCGWRr5LtxRV4Yfec28Bh2JvN0jujBaeYI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/05e9e2f327.mp4?token=pPn1PGvzoNKhbGu8XFQKBkY3DT5Y_rJx8Bg3Gm8C2Dykffl-_QGdACqyLD1zilWtt4Ymnn1PPQRlINH5cX2JKxY0zBIxIAME9fBWphlKUE6q4EOEHJT-cuSIniSn3znIUFxp_e6rlWLrfD0bfUDoDVE0p1UUcpc7QYzlvXtDli-r0gY-1Xtr4E_55Q8K22bPJ7kP6RABoRyjYVJsfGFXaxkqaWwVXd8HAuD8FbFd-5lPFIvQWUeAJRn0ypnovoYMZS0NDhz5fkNpPIPI4gpHRsp-5BhzCJX4u8KEEWoZA01AoQbAe7eP_N5_mJD9ADPNK1Ke-5j1floKzv6HQ9BNtivSpL22IZMh4N72GJhdUhsYl7ZV1wxNXyb0-HK365oX4PJtCuCklgUr_LUdy3GyTn7P_4N2id02ik46DZPIX3fDDgXUi8plVWVqNi1njVv-UB6Gz5BAIUOrzvtoL7bOCayUO9GS6Of1pYOY1okXJQYB0ntqwkjeRZcjK8kL01LO5tqMTtF9BqCwhB4DsxIq9xtDF3PZpfqWR5hOJxZG3d0o9pogJ8DJgm88TI0kXZ6jvQ0R11X4q_Yg6HMSdA0RKUY9JogUp8Wtl6ob5_n4hbXxVhgXZJ_7LuQGKhybHjkuRkbteUJ3EwCGWRr5LtxRV4Yfec28Bh2JvN0jujBaeYI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول منچسترسیتی ده نفره به یونایتد
⚽️
هالنددددددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106388" target="_blank">📅 20:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106387">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmxkX17D-ARpnz2WRe3HbSosiEIXUeL07qvChE46BdZXTzwMVyYzepgcgZuvNWn7Zne1Kk2HNfyDHpLiB8z-CHZcI8CygZQVO4Ci9Zw6AWBLVQA9EGllvpJQiq_fN0wGp3eWfJWtKEAlF01CSXFmfv18B6vaE93QYFy9oZ9HIrTGWYDUTRTbRrT01gwj4rpaychs-QplHbDFPHFzWxvQ1xzkLD5p-9Y_chdG0897UhOndIYfhF6atB9yuJXHknUbKqsMLp9rk-c9X7kvEMEDmRPu1zohX9xWflrIlK35JiwIX-lMy17CyRG12XsnULaNApUcAErGlmqyisz4OEwarw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇸
پایان بازی با برتری چهار بر دو بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106387" target="_blank">📅 19:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106386">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بارسا چهارمی رو زد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106386" target="_blank">📅 19:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106385">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ژاوی اسپارت قبل تعویض شدنش ریددددد</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106385" target="_blank">📅 19:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106384">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بارسااااا خورددددد</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106384" target="_blank">📅 19:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106383">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گلگلگگلگغگغ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106383" target="_blank">📅 19:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106382">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868a077e6a.mp4?token=aWfDcxpdueGrLDGwCAPf4oKi--xs5vYLJllJOn_gIe5uz4iusA7X79lMZ7iH9ZXBAXXX5nfTECCA6WKinCmiWeXY4eSjw1MhHK1MkcztmIIyHjPSr0H9LBtqv_Vx2FqhQMAM0yQuBNeTedGJRYA8PbWp-pOvDJINf4c-rrLV6k6XdMwc4nUFcPMx_s_T5BmA2shjXTd51XxzGZhBAXltA3yy59XEYbO5vS06WtxP-CCAWuSoIghxLa-Zoi6CWWIqpMf8gcCYXs-8uBWnXInGDudweodz7cFVkSfPe169Xn9RM6NCpC8VI3ga5ouPUy8LEueXmP-bOWaYsHKmnfl__Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868a077e6a.mp4?token=aWfDcxpdueGrLDGwCAPf4oKi--xs5vYLJllJOn_gIe5uz4iusA7X79lMZ7iH9ZXBAXXX5nfTECCA6WKinCmiWeXY4eSjw1MhHK1MkcztmIIyHjPSr0H9LBtqv_Vx2FqhQMAM0yQuBNeTedGJRYA8PbWp-pOvDJINf4c-rrLV6k6XdMwc4nUFcPMx_s_T5BmA2shjXTd51XxzGZhBAXltA3yy59XEYbO5vS06WtxP-CCAWuSoIghxLa-Zoi6CWWIqpMf8gcCYXs-8uBWnXInGDudweodz7cFVkSfPe169Xn9RM6NCpC8VI3ga5ouPUy8LEueXmP-bOWaYsHKmnfl__Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟥
صحنه اخراج مستقیم فیل‌فودن مقابل یونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/106382" target="_blank">📅 19:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106381">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wc-VaVqWvCJN5POt2rfI6_KzPuyM2P9FzU2gdtaKm-C8iVw41pGf47bhbuSHg6GnATmgJsZEt4B0q_N6vPllAbD-ODYKAwEcYiisCLyGai9DClgjmuikrPYyCKO_IqGWxpbm67qRn3nUJEmKn4IYenmtabaL-9OJYyuZ7-bP2D2yFs9aFVlR0-DNvf4L3yBAryo0Fqyy2ItgVht1LtMgHQPOO47rPEoFE0kFMuPPcRdhSw9IoA8m73JDXnKY-ELaDQ1eE2vZYFBHWxYJE_NyRHsr4bNbk7nCBH4vIDKZEZy49nc-exlh1y-m7MaB-UCn3vWeCRmreZuxbLYV9siWwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
🇶🇦
لباس استقلال و السد در بازی فرداشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106381" target="_blank">📅 19:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106380">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8f3bfffa8e.mp4?token=v8G_JEf9YsBwV4JA2gNWvA8_N7MqDPHEFCqIAvxsHmEoG97x-4mldiueLCnQYSW_cqA_5wG37RUkl-Fup-RbTbHJ8NC7LOPQ489vX9GBwxA_z4KnFORFoSG1KH4f3LXhw4jgNHrL7MkwCwnqOrBfHQwD7pO79_VE-8I6b4CmhJmZ-GesFiuqjiyCDthDHYL4QlF7JwnuYQZLv5CNqfa9aXm2_aMYK7_6gfEZlyw_D_aefns3obr17s9tEgGPmpGnQ48AEWYHCLAO5-vHANblVe8WrIr7yrWIA4oV3o_skITnzNcUtCWwL1WQ3u6LGvNrdVxR1Raj3j0cVTy319a7V4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8f3bfffa8e.mp4?token=v8G_JEf9YsBwV4JA2gNWvA8_N7MqDPHEFCqIAvxsHmEoG97x-4mldiueLCnQYSW_cqA_5wG37RUkl-Fup-RbTbHJ8NC7LOPQ489vX9GBwxA_z4KnFORFoSG1KH4f3LXhw4jgNHrL7MkwCwnqOrBfHQwD7pO79_VE-8I6b4CmhJmZ-GesFiuqjiyCDthDHYL4QlF7JwnuYQZLv5CNqfa9aXm2_aMYK7_6gfEZlyw_D_aefns3obr17s9tEgGPmpGnQ48AEWYHCLAO5-vHANblVe8WrIr7yrWIA4oV3o_skITnzNcUtCWwL1WQ3u6LGvNrdVxR1Raj3j0cVTy319a7V4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبل لامین‌یامال و گل سوم بارسا به لوانته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106380" target="_blank">📅 19:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106379">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">لامین‌یامال دبللللللل کرددددد</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106379" target="_blank">📅 19:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106378">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگلگلگاگاگ زددددد</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106378" target="_blank">📅 19:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106377">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پنالتی برای بارسااااا</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106377" target="_blank">📅 18:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106376">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
‼️
⚠️
🇮🇷
صحبت های تند رسول برگی عضو شورای شهر تبریز درباره اشتباهات داوری به ضرر تراکتور: روزی که مهدی‌تاج برود می‌گوییم شاه رفت! چون کاری که فدراسیون نشین ها علیه ترکا میکنن شاه هم همچین غلطی نکرده بود
!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106376" target="_blank">📅 18:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106375">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRv9gr7eX5GgZBoHjf7AhKJuKtkWB2NuINPMlLFpjFny3ta9F-RrMg0v8789JBoPL6RCkTIRPQvyeDvBxgHwxi0LxTMcTvlzMb0_X4YWCCtC4GAiNXEwafklNTQHLoBIj6f58TNq8CF4htZA7skVCZpSV8KF94JgnWkEvrln32iYuZwi_DmM2BIvVW4uGOfo5-ipnFHuFQtpcwYYKipkf-HkPbzLUYMIb5uR_Ld-p-mzGPXcSAj_NKR2mHpWukvBI2mEgxkVQKwDpclZScrEmhY5E7BQ-SSNM-D0LZbKsodpuQJYhCfRIESlF24rzldF7Yq3rPrqTb-sZoB66kJHyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
⚠️
بختیاری نویسنده و کارشناس اقتصادی: چند سال قبل من رو به سمینار دعوت میکردم تا اقتصاد رو با انیمیشن به رئیسی یاد بدم؛ گفتند ۳ دقیقه بیشتر نشه چون ذهنش می‌پره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106375" target="_blank">📅 18:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106374">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqD9c84NijpNVirboSEJrcERew1B5KCHJOmaxxWk70h9KFQOCGYD288oUpm2Ho7lG-EkVrlJplGysKR4jGB9v0u69j-Zs0MA9c2eH2h7G5LstsJOnphb7ip7LTT6M9l_yS5hbWjjta52oPZYuUFRTieg-h2dRVF5a9ClsFwU8Hn8B7zSBMdgD5MsdSiB69VhfUw1kk0fNQ3rnz7Snk_-izyuNjjkVD20F6OGLkJTS-aFa-Hp6FewkdzxXkquGSJCFvDHQzI4ysOOKdtN1qoESpnyyX_kYdWcwaJ8DCc99nUf_Tjv8JY0AHBo4Da7NvRenp0NWzskLuaxRXLie01UAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💥
لامین یامال در 4 بازی اخیر بارسلونا:
⚽️
⚽️
مقابل رایو وایکانو
⚽️
⚽️
مقابل والنسیا
⚽️
🅰️
🅰️
مقابل فاینورد
⚽️
مقابل لوانته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106374" target="_blank">📅 18:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106373">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlKlu0PauWCenD4dAGs80AK60kMWUYTU-lYBonrtPa1nL8TKezOcKMXSHjFZS9-ZZa8jBbC-qUvUb9_t4b8LsmmpIfE4JkJvURLDY5hTi0k1rcuBI_Ap5JXK_krloiriTn0Cr9GNQyHxdqQcLJAZxXjhdM3QnSscnyiugHgp0w-48Zicqkk-vLzKEIvkXeXfAHrYvU6zO5ZNe1ZgKDHkbL_tvefXGBFFUM4FuKoTYDj_6PUodFDtmhqCcQFMmj4_osbrEOUUFR6CeX7nI_w-tfv_NPrBxS3njnnzN7QlTMdIH1NgSs6CQIsM46EOBw8wDqYeK-88LBQ_wfCxpdSbTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پرسپولیس در دیداری تدارکاتی با ۴ گل تیم شهید قندی یزد را شکست داد
⚽️
مهدی تیکدری (۲۷)، یاسین سلمانی (۵۹ پنالتی)، ابوالفضل زارعی (۷۰) و مجید عیدی (۸۵)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106373" target="_blank">📅 18:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106372">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106372" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106372" target="_blank">📅 18:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106371">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQInCURwtm2JMtODV4rfA0R2p2ZZEQOktHIb9N53UEnI8VltXFqlUFDZVensQXTtmYky2I7uZw-yI1CbwySiSaJ6SCPOKYt9N2bRuK_a1B2okrknfbNefdJifRwsnJH3ktcpOgW9kf3AMl8IWdKwAgThZrxBB7c-o1BZfPOo6kvjiVJjpxZCSu11sKe6eTSF7fYa99HueifWlHSL6kUBPPZUpK1gBr8bCy_q_UH5Fu7U-b8FS1SMEvEcm8z8rzUQOj83CueulMmBHexuLMh0Lci61_7-wwWHkhnZpSEplLKe6wbnmM_SGY1a1JA3Tv778UpakF90gW5zA--EHrzZUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106371" target="_blank">📅 18:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106370">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رافینیا دبل پاس‌گل
😐
🔥
😐
🔥
😐
🔥</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106370" target="_blank">📅 18:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106369">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">لامین‌یامال زدددددد</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106369" target="_blank">📅 18:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106368">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گلگلگلگگلگلگلگل دوممممممم</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106368" target="_blank">📅 18:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106367">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRNxQdE3yj-toDdzjLJEHK5lcAtcsn1qGgiV8vDBHhhNS_aNjvZL8-N8_oTWJAa_fROad9lQCzN9e7m_fQDrt5qguAjZnVfqVSccIsB1m3sQvifVeYsmtqVKDr6AGbKihmmySXeUg9JCbsy-mTq9UGyoSmH10L2uaGZYTQxERi0vyD4iJ0UswzPM2lkms5_N4yuJWnSKXcQ9J23hqk1KeUK7vy3NPkcRGv8EHkvCM07s3WAkE2Pk1SLCuAV-TsNJi-GGpC8Ligk_fGXy9nvK3-mCl2kAz7xqGkHd20G_4oOjHgppVYFMMNJwzP2okdj91_rKFcSaveFYkjbBGEFs6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
ترکیب بایرن‌مقابل الورسبرگ
/ ساعت 19:00
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106367" target="_blank">📅 18:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106366">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d40cb71cac.mp4?token=HMcZwJw_IouVV-YZy5hlXmyfkFHATb6WKluKjSDyK7hqcmlVIXEQCpcwrfpAUzWUHNsIGhXns8gQ_X9qjDFitTRnlyCvNva2tlT52oZhrMlmmQMV698vsMUMtr-UNTa8JZHOe-Gvk4Jvh561fXIt16cJn1rYBrT68cDROD_BGO1jrS5jXjKdARbkdUEVtrl-p6lz5nBb-TXEOsWOn1Hl9nFCF2rTfpL57500d5ovGUjZvrurXET_ZPAYMSJ_B8QWbGSc2DZAlDLrEhVicq_7E5MBAS051XlJwmvEDMnwbnJF-sfRFUlNoMqOGj43cCu9G9jyzlPt7u1a6C7Ja81p15yP0X3AmgMD_dWODfELWSsfKBRwyu5VeBZCM4yhhfR7zqTlM6YMntSlpsHfcWlNfYxOtCV3xK7cLhQf2Apt8SKqS8-AXFmRJDv4fjOvRbTcKVyCDJBAChas7gvXdkr2hYbLhDF_4I3_Y0TyR9U84YHuIm08tn71RRhUvFxqDayfqVEEYUCqNQo66BZQCK73CtwhuwW5WKgaHz2YicqoPIT-nLDKBxSu7M-TWVQ0Vo4rvwX8-PcmejiMr4G6idV9uysnlvBgETShLt3NTQ8D6PjYjm-ycevebxd3YFenlAcZSZx_13qN-u0H9Tjco1-bisH-1767MmTxGzhhVWh_JJ8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d40cb71cac.mp4?token=HMcZwJw_IouVV-YZy5hlXmyfkFHATb6WKluKjSDyK7hqcmlVIXEQCpcwrfpAUzWUHNsIGhXns8gQ_X9qjDFitTRnlyCvNva2tlT52oZhrMlmmQMV698vsMUMtr-UNTa8JZHOe-Gvk4Jvh561fXIt16cJn1rYBrT68cDROD_BGO1jrS5jXjKdARbkdUEVtrl-p6lz5nBb-TXEOsWOn1Hl9nFCF2rTfpL57500d5ovGUjZvrurXET_ZPAYMSJ_B8QWbGSc2DZAlDLrEhVicq_7E5MBAS051XlJwmvEDMnwbnJF-sfRFUlNoMqOGj43cCu9G9jyzlPt7u1a6C7Ja81p15yP0X3AmgMD_dWODfELWSsfKBRwyu5VeBZCM4yhhfR7zqTlM6YMntSlpsHfcWlNfYxOtCV3xK7cLhQf2Apt8SKqS8-AXFmRJDv4fjOvRbTcKVyCDJBAChas7gvXdkr2hYbLhDF_4I3_Y0TyR9U84YHuIm08tn71RRhUvFxqDayfqVEEYUCqNQo66BZQCK73CtwhuwW5WKgaHz2YicqoPIT-nLDKBxSu7M-TWVQ0Vo4rvwX8-PcmejiMr4G6idV9uysnlvBgETShLt3NTQ8D6PjYjm-ycevebxd3YFenlAcZSZx_13qN-u0H9Tjco1-bisH-1767MmTxGzhhVWh_JJ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول‌بارسلونا به لوانته توسط ژاوی اسپارت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106366" target="_blank">📅 17:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106365">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دقیقه ۵ ژاوی اسپارت زدددددد
😐
🔥</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106365" target="_blank">📅 17:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106364">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بارسا دوباره اوایل بازی گل زد
😐
😐
😐</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106364" target="_blank">📅 17:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106363">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106363" target="_blank">📅 17:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106361">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k-GANPR-IXGGRcWTze2HuGKw9bqQpslHq3aE0n-AeH0XZ-iVCPOgNoa-sm-pIaiUNgXh2n2hEgLKw2BnKr2Pw7t9RJj0Fn1cuB5j-KfOVIXHt_cslW3IWtYclLJoI6JpaTt33A_x4-IalMMEcpgk59eDTDoF6ctoiwNNRsF4j2NyzLNMNYJjcnm-t4ZK4OTHdtEJjJvIf-VP3aP8cSvevDbW4g5nR30B0jYWFePbDEasCB-jrpMV9HX9oEk2Ma9Ge-zZWNh83bcGpdaSVpLSXSt7ovG4O4k-c70wj9sFRnl0-qpPWX5dfU8Yfjqnu5Iz2m-v3mLCnHNB531TEIiY2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k760d8HPM6FCV7Z2qPMV0xymCEjjvP7hhOEmc5T2fwN9ogT3hB0w9ZjD4U2_Dm70_JCvVFgiW1BI2_IMACIX14WQoSVgs8JXZbWS5CNZO2XtjkeQvkG1ij-rpKYa4McERMSby-LyNpGAJgv8-ymKtrU-R8JI9_qmAmIZOi2jrEmITlDX9_pzwd9cGlWjUbiNzEyGOxbbey1SVQ3h21coVQRnrQvuIugZQXP-igR6lbPHSTibQ5Yg4qJcJLJyUQPrfJsNH47URSYUICY6WX34up9DvKY4glnU1FjYlsI7vALamPA-udnTo44sqtO-M5ExJXOjbIxpDEkbnlvb_bqYcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌چهارم پریمیرلیگ؛ ترکیب دو تیم منچستریونایتد و سیتی
⏰
ساعت ۱۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106361" target="_blank">📅 17:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106360">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a36fb349d.mp4?token=mqISSZHpJocQR0CJImgY_VQUdShYpGXIezR3o9jdQ2DEw45nbLggmoJd58Ac4Q0By_nGe61fx2tm8agraHJ3ZfgotCdB-f96HQQEGVdnAiju9moKHPsdp7T5rT3dVJDnZ8MolcOnvkIJZcEj_PctqwsCwfP7jn15rMogD1jjVXbfzGwa-8OXnMJUGaYkZX6ATdmgsCdVbhmLRHy0kutT1gPM__q5E7nxOqQGMcA7GNzFbikyKAUvQE_YCPj5LT57p-4Nv8weoeDw3z7knqIGubO0ppmiBmqnzt4a4lhJOCvfEhqNhhXfmORSLALdaBdUVn-HKJXGeY8TW8D7ZXYPiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a36fb349d.mp4?token=mqISSZHpJocQR0CJImgY_VQUdShYpGXIezR3o9jdQ2DEw45nbLggmoJd58Ac4Q0By_nGe61fx2tm8agraHJ3ZfgotCdB-f96HQQEGVdnAiju9moKHPsdp7T5rT3dVJDnZ8MolcOnvkIJZcEj_PctqwsCwfP7jn15rMogD1jjVXbfzGwa-8OXnMJUGaYkZX6ATdmgsCdVbhmLRHy0kutT1gPM__q5E7nxOqQGMcA7GNzFbikyKAUvQE_YCPj5LT57p-4Nv8weoeDw3z7knqIGubO0ppmiBmqnzt4a4lhJOCvfEhqNhhXfmORSLALdaBdUVn-HKJXGeY8TW8D7ZXYPiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⭕️
⭕️
رادان: بیرانوند شامل قانون سرباز قهرمان نمی شود
دروازه بان تراکتور از اول مهر سرباز است و باید یکی از تیم های ملوان یا فجرسپاسی را برای بازی انتخاب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106360" target="_blank">📅 17:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106359">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNpbkgsUWoUoj_h7MnDxpyf95tefjW2WklWayAgfmYXp_ChBMVzL3fFJRooBqugNESm09_dqbFuAfRHdmk2oEzqm81rHy0_SgaScgteanSNf_nNaHEhB2Gpbxj0LyWi-uiqs8pSc60iqLCmZcCNEkCs22nEycNJ_KM4fSzf8Rgj7BJ979iWpYxMN-Fi8Q0MXx6YF-pU2hKternNi3KOOr-Ss3i7PFendHS2fhvc5_MUHeko3joUkrvf9VjH6R99QHiOjsJt5kEgUy6DGF_oQqgujEULzpPzQfs2tpGzhBQ5ow6brQERJgL4lBENjaZokftHH5EUHDzAr6B1cBcpTLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه گلزنی ستاره‌های جدید بارسا و رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106359" target="_blank">📅 17:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106358">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjry9eBVFn2-RfeyyUIEEDHyDygCExhJDJ7LTQXdxt6KE-2e6P2tnde9X8XeTip-DLOjteOMDA-S2yU24ZylkfJrn2iGbDOpzQvrRLt959jQFDEtJThZ_h_-cd_1Cjr4dJjYzhl-1qcbMfhqOer-3N4f1iSZu0tJl9whFLAFMEhVpSBqzm6q_Hzg-YD80p24lwtDC9-1Pmaz93eG6GltHJiF-TjYtz_bnvUc_PaFyl2jUkB-meX7CulC5LHnMlZKQtLNd1GSbReW-Z_I6pUVaQJbD8-ZqKRYHvH1ewGoBOlT5cZ4kAlVEptIZ4jbZRNmEQmc5nwoN7sIV317ccfNOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
🇪🇸
شماتیک‌ترکیب بارسلونا مقابل لوانته
⏰
ساعت ۱۷:۴۵ شبکه‌سه سیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106358" target="_blank">📅 16:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106357">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53d01737ee.mp4?token=Q214rWEFpuP3CqIRLmKft9xM00UdQWgpB3McgsnZWJqY5BQ0RvLaB1kuPBHPvoLCRSZbRoKOivz22S9rLPVRHmh0aIAFsT1G7UIJ1hwYt8jkWH9wxUhhQqA2Jp_P-LcJQSAb6HydKXl_lKrC-71rO-eXlLvgXwL4U_F6DSSypdRRTVJa_lvt2YU4xIfztFB1ALXWoGW1BkluCLXXI-zhi2hTPkOAUnufNM7O1R-sylcP8_0plXqa6YNmF8eqllXBtuGGxRQDvPnk3EPYCJQKVqryyDNJVZiyhCKhM_aDA5ZPq1VZZIwiyvRz4eIAFZs0Ozqg2JOPyT-smCsD3NEu_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53d01737ee.mp4?token=Q214rWEFpuP3CqIRLmKft9xM00UdQWgpB3McgsnZWJqY5BQ0RvLaB1kuPBHPvoLCRSZbRoKOivz22S9rLPVRHmh0aIAFsT1G7UIJ1hwYt8jkWH9wxUhhQqA2Jp_P-LcJQSAb6HydKXl_lKrC-71rO-eXlLvgXwL4U_F6DSSypdRRTVJa_lvt2YU4xIfztFB1ALXWoGW1BkluCLXXI-zhi2hTPkOAUnufNM7O1R-sylcP8_0plXqa6YNmF8eqllXBtuGGxRQDvPnk3EPYCJQKVqryyDNJVZiyhCKhM_aDA5ZPq1VZZIwiyvRz4eIAFZs0Ozqg2JOPyT-smCsD3NEu_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🟣
با وجود محرومیت در لیگ‌برتر، خداداد عزیزی به درخواست زنوزی قرار است در بازی‌های آسیایی سرپرست تراکتور بماند و کنار زمین مشغول چانه‌زنی با داوران باشد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106357" target="_blank">📅 16:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106356">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWUgbLMNZesbCKaw_CpHGUXxfFtIM6SVzvRZNdM-CPpp3A5Geh-CCPGSLkKi1y6jzshLFFOq8moaZ3MJSYo-66YtBGYiHMjSU5_sScPzHivailvu46rgdITYGL8jFPfztXYPNNFi_x3JNMvDj_mhGUDT1-Af2kyRuySVBQj5uNpgxicxROYo8EKV4yluk2q0ytqH9904VAN_krHTqdXmLNohkKUPGlK7Nr_gm5Q4FeTjzRuzmRCvXY_16fWXWQFlMjXDp6mBZNYyh-QQ5ih5gUhDUon63QqOmonzrnrInuLiPSrUuOdR3aWhUyi3dGhElYrHKHgF0861S2OxEafu4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇶🇦
السد قطر پس از هجوم هواداران پرسپولیس کامنت‌های پیجش رو بست تا درباره یاسر‌آسانی مطلبی کامنت نشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106356" target="_blank">📅 15:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106355">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGB9GZkaATUoENqwKTxMAAEvfnGDQoIFl6-Aj3_glDWcCOp1YVdyWI7_WcMg9MfnNeJ7dkjGbf_T81FodrqX1HtdxcsQvzDNatSakXSr93NWMi2lj6bC3KiErrZcRHe1-HQ4v3nuUod-mxfIW6qirRciXuFpkC2hNoKwO4TJqgQVXtme2sQd6wz-mQyvoPTVbtZyqxS2Fzf7sSSbbRtXGHAw8MzOGedrEBXdmrTc2-NRl7GuNqH-qfQKa7Yy3IQHVdR4mI3tBzdjZZUd-PZ5jHX9F62NAPAg83xczb1HiJ-gkeg2LFuP25L6oa8-ROe05j_pEKKhW6Ay8QtOwkOcPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
طبق معمول ده بازی گذشته، مقابل والیبال ژاپن شکست خوردیم و سهمیه مستقیم المپیک به این کشور رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106355" target="_blank">📅 15:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106354">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
‼️
🇮🇷
افشاگری داماد سابق علی‌پروین بعد از 22 سال؛ آرش فرزین: رهبری فرد و باندش، سرمربی پرسپولیس را کله پا کردند!
بیست و دو سال از روزی که آرش فرزین حرف های راینر زوبل آلمانی را ناقص ترجمه کرد، میگذرد و یعد از این همه مدت، حالا داماد سابق پروین، پشت پرده آن روز را افشا می کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106354" target="_blank">📅 15:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106353">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1b2c19a26.mp4?token=fCeZ-V_K8iOjPPgfMeLFiuVJEZgbYtDnNNhEC3DyejW1SMskdBG7wSjCMpNqwL-wpfjHf6fMfJjINaYJ6hRuYBnp0FqdEUoV7PnJGJH8gyO2dqzF9jZhQ2AIL7ZJ0s7_qOjhM4A8wh7UcxrEZytKz1b4YvzoEOVN1Dhg6yvzkYEk5BcSsGQsA7tbP0gVnJYNH0oBgRclta4iukFCVKvus6P4imZK39QnB1cvBs-DQMvpMc7nHgJqxZhmXr6Nsoi0VtYGQwdiOH8RCvzR8zQYhJTvsCMywZpEvNmAAR4aOu6FE0oN8fLp261QYuwKRmNB8d1c9mYk6326rK-ltDadHzVFdjlAU-HxO5a7WFlnnRW5RP6DjSKIDS8nhoEJkkkF19F6Gdn_-GAn0OisH14XljrM3qUuANUkFqRGp5pDsRE8TQc4gKtNS6EXW9f6HriLkkOe0Ko7DL-Y-LYiOYciz9d2NvLP4-JqOKRMonDvcpFgGA3ucSZkjSRKWHwekvhd46_X_twQx1mjym2NVkkx_AET4BKbDPDMsy1p6PGMPWjh_LRySJqqN7jiWQPdH5SC-Lzh8Cv-O0a7qS_JxU9hsyoYastV0QXUF_3zSmW0u2JpuqFOJMDTTzb6zyCzsJYZrpUK_3Hc_ydipja7Wal7RomPUvhqd1iPRD3FYNQvGsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1b2c19a26.mp4?token=fCeZ-V_K8iOjPPgfMeLFiuVJEZgbYtDnNNhEC3DyejW1SMskdBG7wSjCMpNqwL-wpfjHf6fMfJjINaYJ6hRuYBnp0FqdEUoV7PnJGJH8gyO2dqzF9jZhQ2AIL7ZJ0s7_qOjhM4A8wh7UcxrEZytKz1b4YvzoEOVN1Dhg6yvzkYEk5BcSsGQsA7tbP0gVnJYNH0oBgRclta4iukFCVKvus6P4imZK39QnB1cvBs-DQMvpMc7nHgJqxZhmXr6Nsoi0VtYGQwdiOH8RCvzR8zQYhJTvsCMywZpEvNmAAR4aOu6FE0oN8fLp261QYuwKRmNB8d1c9mYk6326rK-ltDadHzVFdjlAU-HxO5a7WFlnnRW5RP6DjSKIDS8nhoEJkkkF19F6Gdn_-GAn0OisH14XljrM3qUuANUkFqRGp5pDsRE8TQc4gKtNS6EXW9f6HriLkkOe0Ko7DL-Y-LYiOYciz9d2NvLP4-JqOKRMonDvcpFgGA3ucSZkjSRKWHwekvhd46_X_twQx1mjym2NVkkx_AET4BKbDPDMsy1p6PGMPWjh_LRySJqqN7jiWQPdH5SC-Lzh8Cv-O0a7qS_JxU9hsyoYastV0QXUF_3zSmW0u2JpuqFOJMDTTzb6zyCzsJYZrpUK_3Hc_ydipja7Wal7RomPUvhqd1iPRD3FYNQvGsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
ویدیو وایرال‌شده از آغوش گرم دو بانوی ایرانی در جشنواره ونیز ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106353" target="_blank">📅 15:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106352">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68ecf94960.mp4?token=mQ_JHu4yCMa9_mPntZa9MadMU709i2uaT_Ea33V-FrC1SutlnHpm54I0UxmAkbgkfjlBR8Zacz7UNFj8UtZMyn8fhKOIwmLIKSZ9xjq8a6C7ze8Hsw_uLpPNiZYKydlTfs1AOBMbG0yYeUV-DzKxjaXmnHCK0IJkbQJI4BAGx42BprbbWNafixIXChl_ux9Tk6SzOT8LHt3YV7M572fffrrk93a1YCntuLQPRXEqdM2u9p0ECd52kPl1SonYaWsJdyXrSS6d2x68snVRCN81AuhsSDM0uFfkXzml1ySrAMxccCETfYzwup7bXl0q2c65PNVNMxjFO6VEzkgT6AXBgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68ecf94960.mp4?token=mQ_JHu4yCMa9_mPntZa9MadMU709i2uaT_Ea33V-FrC1SutlnHpm54I0UxmAkbgkfjlBR8Zacz7UNFj8UtZMyn8fhKOIwmLIKSZ9xjq8a6C7ze8Hsw_uLpPNiZYKydlTfs1AOBMbG0yYeUV-DzKxjaXmnHCK0IJkbQJI4BAGx42BprbbWNafixIXChl_ux9Tk6SzOT8LHt3YV7M572fffrrk93a1YCntuLQPRXEqdM2u9p0ECd52kPl1SonYaWsJdyXrSS6d2x68snVRCN81AuhsSDM0uFfkXzml1ySrAMxccCETfYzwup7bXl0q2c65PNVNMxjFO6VEzkgT6AXBgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبت‌های شنیدنی سعید دقیقی درباره تفاوت سبک بازی اوستون اورونوف و تیوی‌بیفوما دو بازیکن پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106352" target="_blank">📅 14:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106351">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnemJO_ngcHSfT0Nb7NQ2o7q1rY8ap0O5N7GVODN7f7Q75Hamdzqf3vTnrVHJDTsPtYvHosqmyaHbKy3YLx4P93oRZ7n6s8ZPl-tHYxwzftXrbBd32J-OceCrTaw3K4jAwKYRWM5DyVWYkk2NLt6gB0560fEc3xBp8vgsEt6nQ0GDXDeTC0bGzAaJ0gr4J4psDsSe6Y5NmBgC6mCIL1A-99XBOl6A_OH14q6nhZIUY9lOde3dF3WScyXixCwcHFVxayS09ye-N01JNxrOpB4e5u2DZGBkAwZW7DpJLAq1e2NuQMpflaEB_m-0uwk0FSyiyt2wpkXQK7a-LGY7nWl0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
هوادارای التعاون دیشب برای اینکه برن روی مخ روبن نوس، بازیکن الهلال، اسم دیوگو ژوتا رو که دوست نزدیک نوس هم بود فریاد می‌زدن.
✔️
👏
نوس هم بعد از بازی درباره این کار مزخرف هوادارای التعاون فقط گفت «امیدوارم حداقل بعدش نرن نماز بخونن.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106351" target="_blank">📅 14:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106350">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2eae5e40.mp4?token=rPA9gktu7d_9km8kOyXY6nxPKqYWHRkqJbJ5i3pKHfO_ELj7p6rpJJYCqrD5wdDeBVLA1vKy5wKpV5fWBqfgp9ZVSfXnRyxg7BxMQJRE19iFFrdFwPNSUCxivm9YN4stb3GOWEiROc2RjUYbwtORTDFCPyXSXDVBKDjEFiKRTyipb5cgW-QYdauDDQyNQvGgJQ5xngfEF43qy97Xv-y3B4q6pTFlrj4VI3C3MZKQZhKrZcr6IhXOv1wfDXdVuiPPSrxJTxITn2vYrt-rcKERIybpOsOs0nzEjozkxtQaaEjRpqcIBmemEmbu23MIFqaypUmFk8sGzT_t_1Dj46VFhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2eae5e40.mp4?token=rPA9gktu7d_9km8kOyXY6nxPKqYWHRkqJbJ5i3pKHfO_ELj7p6rpJJYCqrD5wdDeBVLA1vKy5wKpV5fWBqfgp9ZVSfXnRyxg7BxMQJRE19iFFrdFwPNSUCxivm9YN4stb3GOWEiROc2RjUYbwtORTDFCPyXSXDVBKDjEFiKRTyipb5cgW-QYdauDDQyNQvGgJQ5xngfEF43qy97Xv-y3B4q6pTFlrj4VI3C3MZKQZhKrZcr6IhXOv1wfDXdVuiPPSrxJTxITn2vYrt-rcKERIybpOsOs0nzEjozkxtQaaEjRpqcIBmemEmbu23MIFqaypUmFk8sGzT_t_1Dj46VFhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بدشانسی‌های لیونل‌مسی برای اینترمیامی در بازی بامداد امروز تیمش مقابل نشویل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106350" target="_blank">📅 14:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106349">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c6ed3f485.mp4?token=R4yZZr7FISlnQ1OXW2YaSazKjKC9kBnR2VSn9SU2cxSR0072xiOyZPbdaNkHvTnNzvNpsg0uHfHeMWDroX5cOnWH4NsiCzmEnnTz3Anz5v8qgXl__g2ZBBuOxArZYVIO3n-phnfMWtgTpwUU16g4LdbyM1Cio7q7c7Wg9DueI2zHJhAhlHddAhjRPm-TwK4ExxOwSZB0wRSDGcggspuZNRPSo5T_6xGMrGTSHN16ExUohTm6i7qWBF1m_oW4qi2tzRJpYec37plY-V9ceBJ8fLHjNuO3rBsIk_RoseuWMDBiDhR3bxKxONZx8qVmtfJKnoqSw6hMC08UDEYXGxjABjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c6ed3f485.mp4?token=R4yZZr7FISlnQ1OXW2YaSazKjKC9kBnR2VSn9SU2cxSR0072xiOyZPbdaNkHvTnNzvNpsg0uHfHeMWDroX5cOnWH4NsiCzmEnnTz3Anz5v8qgXl__g2ZBBuOxArZYVIO3n-phnfMWtgTpwUU16g4LdbyM1Cio7q7c7Wg9DueI2zHJhAhlHddAhjRPm-TwK4ExxOwSZB0wRSDGcggspuZNRPSo5T_6xGMrGTSHN16ExUohTm6i7qWBF1m_oW4qi2tzRJpYec37plY-V9ceBJ8fLHjNuO3rBsIk_RoseuWMDBiDhR3bxKxONZx8qVmtfJKnoqSw6hMC08UDEYXGxjABjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
یک‌شهر و دو تیم برجسته؛ به دربی جذاب شهر منچستر خوش‌آمدید؛ امشب ساعت ۱۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106349" target="_blank">📅 13:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106347">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mXbj8PuCKKRVQnShZ7d8ak2p567qIhOMj6gDsYT2ERm7leXBxSgzxblSNeJKMdcd-CRlF6zwQXWaV27Ld1d8M6McrATPfS2hsljhaOi3WvMCJ93qtBvKLu_Obzq-v0VY-eaZvFIuuTIY1mUGgF82KYdC9iLUkNM9ZFfLpR-9ug6_xbR5q9kZdXUiMKezKPAk5JlU24h6Xfnx4hVfXBXJVhK15ZkQDCZ_B32dtqZpJk1TzybQPILK8ZgOSFKaCqn3u_EKZ9lNGGPW2yNRTRs4Di4QPLOGY5g-ydgk1BIbwa52-mwHIkbirf47gIx05bqMLt6bU9BD9G7YzLhJk8lxlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qlqvEhwI17fZnwtOqN4L06-MIz4O3I2M2Yfx-tmMEgQDFeUUYro4mRIMSQFThOnZVeuIiKk_SyNNOSif8AqLjHp-X2ZLwgxGHsItDhh-XCn2zhvnZ_WaooW3kY90nBYKu1qZT2MxDYMyJ0dktxKowVcqXkdB8dMEQ4G8d9P_Wj5eCW-ZTZfQW_KedFKlmg8Y5LNZaYIzDFhFUt_Xhvbdr5P3q1JCSiSf8nTMlCn1PcS2BZzKE_RnYXUiCggdYC4-PS1E4tAv6smTIkEqg2YfO3JR17ATW8kAlnVrI2X-U55p3FuH6e7aJdcfwcdmn3nLRSYjV8GW-wJg4A_EbryuSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
بر اساس اسناد منتشرشده، فرشید میرشکرایی، مشاور عالی و منصوب جدید تاجرنیا، پیش‌تر در پرونده‌ای شخصی با موضوع «خیانت در امانت» به یک سال حبس تعزیری محکوم شده است.
حالا این سؤال مطرح است که چرا پیش از سپردن مسئولیت و منابع مالی باشگاه استقلال، استعلام‌های لازم درباره سوابق افراد انجام نشده است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106347" target="_blank">📅 13:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106346">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJLnA5aEKDQeVmTE5xVx2Z0QaRNW83hIZVm9vV6Apd1MlqD7qB2wf2Cn7LvddhHJhUJbU6PQAnhDCcM4Aksy6OWM16BqNUL9dPqKT050L-9BsZEQXRk6z6-8GDGISt-WoXWdxfMGE3oxypBlIJABu40EZ_HsXs4N1zuFbwR2lxX1IjTa9Z0wBCrK95bSyYIyOvuOlxkrQY6grlfacCWtYWk_6BnXtmzPFJlsIiX5gCItUku6Tcxj_-5oA4agn-3lmKsfKia-uUmgus7pbfX92nZcuo4yUWrtaSu6hpUzfVpZUbCAYR9KE1-zn10y2rNNNaH0ERQrHil2s8Ay-YasNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
فینال قهرمانی آسیا 2026؛
🏐
🇮🇷
ترکیب تیم ملی والیبال ایران مقابل ژاپن
؛ ساعت 14:00
🔥
قهرمان این مسابقه سهمیه المپیک میگیره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106346" target="_blank">📅 13:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106345">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddad7e35de.mp4?token=XUuQzSiqsDMlUV1dABYi3ZB62m6vRuQ62bQXXSzllQtUgtyuVekki0Z-8w3XmY-Ws6I6CTwLCHZOhMIjzeyKxdNAoWUeHeZ7dRuCkE4-I1pkTE0YecTYXfOpOx8LhCqIMeMTsXusHLpT3hkc_kAm9rOOr3dnUcjYDr9mPkKkUR2DfMTKB-l5pn30xEBtFiA5d4QdoIueS4yC2DBRD7Xt6i6B4phmJPlQz7Nega5PspV3rOdikCx7retguIh5fKRPi09KHYSlQUQq2jaTDGmwDc-o1D-qwl6kwk4UKUuc7X4RWbd85BL-1vwFr4Jmi7NkpKjlU_SDqm0TbU8V08u-qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddad7e35de.mp4?token=XUuQzSiqsDMlUV1dABYi3ZB62m6vRuQ62bQXXSzllQtUgtyuVekki0Z-8w3XmY-Ws6I6CTwLCHZOhMIjzeyKxdNAoWUeHeZ7dRuCkE4-I1pkTE0YecTYXfOpOx8LhCqIMeMTsXusHLpT3hkc_kAm9rOOr3dnUcjYDr9mPkKkUR2DfMTKB-l5pn30xEBtFiA5d4QdoIueS4yC2DBRD7Xt6i6B4phmJPlQz7Nega5PspV3rOdikCx7retguIh5fKRPi09KHYSlQUQq2jaTDGmwDc-o1D-qwl6kwk4UKUuc7X4RWbd85BL-1vwFr4Jmi7NkpKjlU_SDqm0TbU8V08u-qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
دلجویی آیسان‌اسلامی از هانی‌رامبد پس از مصاحبه اخیر هادی‌چوپان علیه این مربی برجسته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106345" target="_blank">📅 13:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106344">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0dd00f3a7.mp4?token=qkSjTZLatH34TtXaJmn2y7SzSfR4vTH1klunYSl-7gydcr1GxO087tlrFmql1By7IESJfk4g8LNCJeDnInsfbHxtwZXBRl-paLnwZLOpDPWcRL_mhPOE7LW3I5qPY1M7zSiXau3Dec-4KzUFnwBMKFZQ4y9xzCZOS1dCAvQEFceDNWy-Sc7YTRumpCuCfqULsrzppvQX9aPH9OszFSvwrEaLaBHuiuNdJhzjKyRKGmDkmwmPzPJC9PFWi0xPeo_uqwYV2jtyyPKo1s_Hn4BLkCEB6_adnUulLuGxjWo8eYHPBVZIqfw5pouZRCq2koj-T6S6vmqm14OIAX5lrVqNwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0dd00f3a7.mp4?token=qkSjTZLatH34TtXaJmn2y7SzSfR4vTH1klunYSl-7gydcr1GxO087tlrFmql1By7IESJfk4g8LNCJeDnInsfbHxtwZXBRl-paLnwZLOpDPWcRL_mhPOE7LW3I5qPY1M7zSiXau3Dec-4KzUFnwBMKFZQ4y9xzCZOS1dCAvQEFceDNWy-Sc7YTRumpCuCfqULsrzppvQX9aPH9OszFSvwrEaLaBHuiuNdJhzjKyRKGmDkmwmPzPJC9PFWi0xPeo_uqwYV2jtyyPKo1s_Hn4BLkCEB6_adnUulLuGxjWo8eYHPBVZIqfw5pouZRCq2koj-T6S6vmqm14OIAX5lrVqNwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
برخورد ناخواسته علی‌حاجی‌پور بازیکن تیم‌ملی والیبال و یک هوادار ژاپنی در حاشیه مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106344" target="_blank">📅 13:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106343">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwS_L5_014gjMFxIbw9E4pn819XIz9qGxiFUfGvqeInInJ0I89JGtCvbmgpYScK5O2fwz531rkte2I-O6fOZwJhrc8hWzc3FYpHXY8X3S-6IzSAQErWHkQ3yY-cH51bg-zucopgnwNhlzjLSk5Z3Aw-zmXbgwiR4EvnKXred44WFXqMWQbwh-S8Gr60uggQBljBI-6hvXQnkApwXTbYIQZJBJYSyVITW3z_EsJbe6Nl8GOPTu4fbV-8RMZExIhTh5CTbXnbPJDdUZjecjG8rLXEccG59vWNFohEl6FOXlp8vt_M2R-a1bIHhongOSTcC19IupM5C2KY5XjjOwaBD7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
‏
📊
نتایج دربی منچستر در طول تاریخ:
‏
🏴󠁧󠁢󠁥󠁮󠁧󠁿
81 برد برای منچستر یونایتد
‏
🤝
54 تساوی.
‏
🏴󠁧󠁢󠁥󠁮󠁧󠁿
63 برد برای منچستر سیتی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106343" target="_blank">📅 12:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106342">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIgTBIaEhtXh0f3HhCK2-Jf6P7qPMXY3EU2Lk9IC2y3w5wPWBxZOF_IeamYunChnb_20aFx70Ms3UokYhSDKGfTbFBrmYEtrr4Ibxdm02yQQf11DZE6G0Yn1wzseVkWj0620e3bawrvjsM6_zobO5QzxecXEEdwVDej3H2hvi3YK-VmewGjWc6HRFGZZsajBSu5sHNiX1sZNM8WS0P3F-BGDmx21jTzDyUdmhikHLi2qQ1OdBqVd5iuT6Decl8F-wK1UtGdllFlN3flFonEDYH5rRkcwGvFFwm8CHySsj4P32Xr1aKyNJL7zAAOGkhVlJ9b2CQ81aW-v0dSIolxG8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
آمار یاسر‌آسانی در رقابت‌های آسیایی:
🟣
آمار آسانی با گوانگجو در لیگ نخبگان:
🏟
۱۰ بازی
⚽️
۹ گل
🅰️
۱ پاس‌گل
🔵
آمار آسانی با استقلال در لیگ قهرمانان آسیا ۲:
🏟
۸ بازی
⚽️
۴ گل
🅰️
۱ پاس‌گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106342" target="_blank">📅 12:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106341">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCKjolIDAYe5aXKnTbeq5hsPhx02Y8nWRLrAUeo06MzkqN45KU2DUENSGSfNtNnkp7dpj6m9wXoc4L1TEjv7unq7vEpSazaCozHAH_UTO6UfEqG278Pd_2t8jPhck2FFS69LUOY4VSjNQbbqqViwZQl70iDTxif0JPpbj12_IYnxQ3pdm-bMDgcssuTvJt16bwcIq2-sC6ZJ6f0CtZXPgh8vtY2lBGhYorpm8luMoCDXR-Tx2ibdC6eJxZ5S2XZA7qn6K2oMGyrT7cTZ5A3W_Hz5K1BX1ykJvcAtleWyYfpxVQBWIkvKWZSTFTPZ9e5GqG-tNSOC4vAKwRQCpxKRmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇪🇸
خولیان‌آلوارز از لیست اتلتیکومادرید برای بازی با رئال سوسیه‌داد خط خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106341" target="_blank">📅 12:09 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
