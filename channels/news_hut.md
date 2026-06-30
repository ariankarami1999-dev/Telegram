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
<img src="https://cdn4.telesco.pe/file/FkoP_aIeIL4_-_inYPZro2KkX3opEAg21gfjMIaaHHMqWBonI0wH0NP7B1zMp9_tXARGNQLpQBLhpn8-vBOAwLZ1aGwwmFjStYdT7Ojt1pJias0tSQmw3qUZHuM6ax2iPaGj01C9cAX-3EdnCWYbkSH3AAoyKdgWRKdxJca61ijaFJtRyCvS83xET_e0hk0Jt_s4HmLIW99JH6RzpIrlJoF5KQM6TdfnzHjoUX5u7GqxpP8_E_ifu9k_w-Zv66zlX49xblAQJnVD_BxIABhHXMaUAvSxqSs77j0CHIjzii52kUIcOBZvE002_HJgdbEh8RIlT-NkM6M5WcmYOWfjEQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 217K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 18:41:02</div>
<hr>

<div class="tg-post" id="msg-67095">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=PEK4GQjUPIcAIxLOhC4kjjCDRkw4GV8H8HuQLWn5s91bA3sRAG5jMgPG0GzFIL6sYilfc5XAdbAH0ytRlNCLkPN7fhAqbXT5B8qG-VWCbPieWdQJqjf8LNqp_fdwApRDK1ZNzfuMykoqcxxgKNi_0c6vPTxvGuU-9wr0dj4KYhpiQoFbF4pkMY-BWpGdClPgoCGMNOgCl-taCZZUIX5KjhXNBDw9mMZ3UTEPK2SMYk-6rQ54Pf5VXOxk_FoN5zwRPUU993SGHhV9IBmUIVQardapJO2M3iOfknSKmYX9QZ7PBZS6-ksUArUhrPH3PLB6_ByjnkFg3hbB8IMYVmndoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=PEK4GQjUPIcAIxLOhC4kjjCDRkw4GV8H8HuQLWn5s91bA3sRAG5jMgPG0GzFIL6sYilfc5XAdbAH0ytRlNCLkPN7fhAqbXT5B8qG-VWCbPieWdQJqjf8LNqp_fdwApRDK1ZNzfuMykoqcxxgKNi_0c6vPTxvGuU-9wr0dj4KYhpiQoFbF4pkMY-BWpGdClPgoCGMNOgCl-taCZZUIX5KjhXNBDw9mMZ3UTEPK2SMYk-6rQ54Pf5VXOxk_FoN5zwRPUU993SGHhV9IBmUIVQardapJO2M3iOfknSKmYX9QZ7PBZS6-ksUArUhrPH3PLB6_ByjnkFg3hbB8IMYVmndoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی روسیه در زاپوروژیه اوکراین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/news_hut/67095" target="_blank">📅 18:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67094">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=D8a5GLdpUfOkdMG_3FRp7W92p_JRPV7vE23uGUnXcRBazmJzVvEInpitTIm5GFENIRiwBc8FHWEf6-SZnpU7KdqPypscIdqDcQLVudSQzeVrUA5slanDv4rTVyKS_6UVne60cXz_1xMS6iCglUTTGMze_SHeh-fTgGfOAqThpsijvglCh8UPXcwqRi3l5RtADQSrT7watIon-pD9CY39_L7-ClrK4l_RVBpsKTOsBivLy9dnkzL-rwSLHXQ5iDhOzq72hQBPbv0GBs_FcPsZL_AFH7serlPKMkTyWuDws8L5-p2Fa8CMeSQQHw7X6dK5ziWKDNYEPpr5KRRGdg0vOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=D8a5GLdpUfOkdMG_3FRp7W92p_JRPV7vE23uGUnXcRBazmJzVvEInpitTIm5GFENIRiwBc8FHWEf6-SZnpU7KdqPypscIdqDcQLVudSQzeVrUA5slanDv4rTVyKS_6UVne60cXz_1xMS6iCglUTTGMze_SHeh-fTgGfOAqThpsijvglCh8UPXcwqRi3l5RtADQSrT7watIon-pD9CY39_L7-ClrK4l_RVBpsKTOsBivLy9dnkzL-rwSLHXQ5iDhOzq72hQBPbv0GBs_FcPsZL_AFH7serlPKMkTyWuDws8L5-p2Fa8CMeSQQHw7X6dK5ziWKDNYEPpr5KRRGdg0vOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
پلیسا شوهر طرفو دستگیر میکنن زنه یهو میرسه به پلیسا میگه وایستید لطفا میخوام باهاش حرف بزنم یهو بعدش...
@News_Hut</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/news_hut/67094" target="_blank">📅 17:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67093">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⏸
🇺🇸
نوه‌ترامپ رفته کاخ‌سفید گردی و با این ویدیو مکان‌های مختلف استقرار بابا بزرگش رو نشون مردم داده
@News_Hut</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/news_hut/67093" target="_blank">📅 17:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67092">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c791837da.mp4?token=q3m84EgSAQOWHjzxNyGotj8wmkPoIZoaDCgJiP6xa8G48j-urCUIx2njk7pf7FTG1IR--PN8GI4QJy_8PUIlKtEsYI4AH_pzkUzayrLz51D3vhYRnC8JIxGPNRhq4JqEM0q9kSQhx-dRE1XSg6431gyhjTTKckvpMRsNxeAMzsZHZkcmB6zX7GExr6Sp9qPdDw-pSYMKgPI0bdZuAH8pJPsttlDoXZ7caTVfwBb0pHN3oqMsL5ASgsmUAAnD-Q1cAh5rVur0mlk61zfJp55cI3diFfh0YFsaJk0q8cKPdiivG2e9-3ta85OQ-1d30QAgjpDGT09ucQ9ftdlDschKQbcJjTOV_pkhjLPH4uq23erXoRfPK0IgQvfLrxlHFkMxYydxEcEOXwNxUFPR5nOo63_Foy1ZvorcZd6mbnLNe-hEomDbQirjr5wKNuP_mwsmyBO9zsoLXtLohoz5DzKBxNgEueQqGpUfi7n0zu9MeduFELjARiamdhBVFqGr-O3QNNXS6yo5d5G0X7IuX7HH1hTj6MSfSQt5pDDkqSB0fmf_vYJXwofnEKmXUf7szC1Es6gF1IqLD-cTjqp_PYjJEDteW-9dz6OnsTT9uHpeYfBHgaFBDGZUEp9Jgg8qf-G8Rc6KaY-O1fAmi3sKfjQTi5E2MJ4-gVEGVbGZcwiTtbM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c791837da.mp4?token=q3m84EgSAQOWHjzxNyGotj8wmkPoIZoaDCgJiP6xa8G48j-urCUIx2njk7pf7FTG1IR--PN8GI4QJy_8PUIlKtEsYI4AH_pzkUzayrLz51D3vhYRnC8JIxGPNRhq4JqEM0q9kSQhx-dRE1XSg6431gyhjTTKckvpMRsNxeAMzsZHZkcmB6zX7GExr6Sp9qPdDw-pSYMKgPI0bdZuAH8pJPsttlDoXZ7caTVfwBb0pHN3oqMsL5ASgsmUAAnD-Q1cAh5rVur0mlk61zfJp55cI3diFfh0YFsaJk0q8cKPdiivG2e9-3ta85OQ-1d30QAgjpDGT09ucQ9ftdlDschKQbcJjTOV_pkhjLPH4uq23erXoRfPK0IgQvfLrxlHFkMxYydxEcEOXwNxUFPR5nOo63_Foy1ZvorcZd6mbnLNe-hEomDbQirjr5wKNuP_mwsmyBO9zsoLXtLohoz5DzKBxNgEueQqGpUfi7n0zu9MeduFELjARiamdhBVFqGr-O3QNNXS6yo5d5G0X7IuX7HH1hTj6MSfSQt5pDDkqSB0fmf_vYJXwofnEKmXUf7szC1Es6gF1IqLD-cTjqp_PYjJEDteW-9dz6OnsTT9uHpeYfBHgaFBDGZUEp9Jgg8qf-G8Rc6KaY-O1fAmi3sKfjQTi5E2MJ4-gVEGVbGZcwiTtbM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
قمه کشی ارازل اوباش میان مردم در شب عاشورا رودبند دزفول که با دخالت پلیس خاتمه یافت
😐
😂
تاریخ ویدیو 1405/3/4 امامزاده رودبند
@News_Hut</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/news_hut/67092" target="_blank">📅 17:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67091">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=ip_FjGyw30ZZ6dZifOfteYW2x0V3JHSxccnuDy8OXS6SYDMIL1YQw-O71lRipJrzjPLIyEwUD2b6heQNYIRvmaPltKClRDl_8SvIgMDCD8qfxsrLt2fAVGbEJsM5LP5dWt9LTTFMllMWSqe3qI5xVbXORCgZ_gZFMh_OlXnInlzzd_6lQnV6eQ8o5akSRUCQg3fhe8w7rOti3TZHi2BAz_3_8BapWPRA268uQIv9UQtXf_7yNRCvdrn-ULYXWo_AkeYsqIvldTwo3PY4AsK6yLL5LMPsb7VmPqD09Y7RzijCL4y7A8GJPUP5jko24pdiCIiSU6x7AjC6vrVjd2sLQyUnF_GYYc_1DA0awiO9KMdpNqfmGrpNDg7w25Zg29LNl7CqSTJLyB7tS2Ch1FXmMiC4htYKXAqC2reOK5ZiCHc_6MCGmm3bWkfg5Z0H6mEg7jLM3kQMiqN7BqRJrY_dYpGO8t0sd1e9XsWbX_5bSwqQ85buPcN0y9iflmKGDRr5iGI5lcCYmk2CH6gQi-ImftE-bs7MsTPU4P6Ua5PBO1jj4hVWP3o4Ls8cUUyJ6UMnrXIhUs_VVUGIGsMywyqU5aC3hATYbcCtw54fi-_JxRYOJq-V16-9FZ1NhmTaP3wugPTo3DMEdSnx_e7NrU18FTVDrd1yOMGwaw8NSwnoaBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=ip_FjGyw30ZZ6dZifOfteYW2x0V3JHSxccnuDy8OXS6SYDMIL1YQw-O71lRipJrzjPLIyEwUD2b6heQNYIRvmaPltKClRDl_8SvIgMDCD8qfxsrLt2fAVGbEJsM5LP5dWt9LTTFMllMWSqe3qI5xVbXORCgZ_gZFMh_OlXnInlzzd_6lQnV6eQ8o5akSRUCQg3fhe8w7rOti3TZHi2BAz_3_8BapWPRA268uQIv9UQtXf_7yNRCvdrn-ULYXWo_AkeYsqIvldTwo3PY4AsK6yLL5LMPsb7VmPqD09Y7RzijCL4y7A8GJPUP5jko24pdiCIiSU6x7AjC6vrVjd2sLQyUnF_GYYc_1DA0awiO9KMdpNqfmGrpNDg7w25Zg29LNl7CqSTJLyB7tS2Ch1FXmMiC4htYKXAqC2reOK5ZiCHc_6MCGmm3bWkfg5Z0H6mEg7jLM3kQMiqN7BqRJrY_dYpGO8t0sd1e9XsWbX_5bSwqQ85buPcN0y9iflmKGDRr5iGI5lcCYmk2CH6gQi-ImftE-bs7MsTPU4P6Ua5PBO1jj4hVWP3o4Ls8cUUyJ6UMnrXIhUs_VVUGIGsMywyqU5aC3hATYbcCtw54fi-_JxRYOJq-V16-9FZ1NhmTaP3wugPTo3DMEdSnx_e7NrU18FTVDrd1yOMGwaw8NSwnoaBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
😳
عاشورا برا این اراذل هرچه نداشته باشه یه خوبی داره و اونم اینه که تا سال‌ها سوژه میتونن دست مردم برا خنده بدن
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/67091" target="_blank">📅 16:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67090">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=Rdbh5jp9WuVybQaKnTOF5dODVUpCntUjztyFQSemHyYcmk39uFcZ5AFDeOmMgrkIdpY1-09g20AtAJvc4o4czFhJvOI1YFoQlQyugCHxSS6pWkDRz9YSLy7nbxNDcs1jOkMsI1Wv3TI94lpZngcfmaGh63CK0hYxbWkRX_6HKDo9z3qMmxo1bh8Eo7iYpeywnJGNyXBg8szvajZjS2UlS9aGsI1xdfIrQAl1DoRR6E3cpCDc_m06t0XCMjqAC6lXQMwcXvIKSVRO1L5s7O1nEytT0WxKyKEC1qIB4sKP8p7ObB3bpoXq1Eq4Mu0s4qYumza0oeYI9J940ngI6DrJeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=Rdbh5jp9WuVybQaKnTOF5dODVUpCntUjztyFQSemHyYcmk39uFcZ5AFDeOmMgrkIdpY1-09g20AtAJvc4o4czFhJvOI1YFoQlQyugCHxSS6pWkDRz9YSLy7nbxNDcs1jOkMsI1Wv3TI94lpZngcfmaGh63CK0hYxbWkRX_6HKDo9z3qMmxo1bh8Eo7iYpeywnJGNyXBg8szvajZjS2UlS9aGsI1xdfIrQAl1DoRR6E3cpCDc_m06t0XCMjqAC6lXQMwcXvIKSVRO1L5s7O1nEytT0WxKyKEC1qIB4sKP8p7ObB3bpoXq1Eq4Mu0s4qYumza0oeYI9J940ngI6DrJeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی وزارت خارجه: اساساً برنامه‌ای برای دیدار با آمریکایی‌ها در هیچ سطحی نداشته‌ایم که بخواهیم از آن منصرف بشویم
🔴
گفت‌وگوهای دوحه دربارهٔ اجرای بندهایی از یادداشت تفاهم است و با هیئت قطری انجام خواهد شد.
🔴
اجرای بند آزادسازی دارایی‌های ایران در حال انجام است و امیدواریم کار به نتیجهٔ مطلوب برسد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/67090" target="_blank">📅 16:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67089">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dahKW0wXjoBzb7IUGSl6dho8B8EINbXZ5cqTiluKu-RgEMCJgh4OtjX7EZnpfCjLPZVCrZkXjtbu6stT9hk70iQ-tLP07ME7ddplPCgkjCgekGydbLUSNzW2yv-rtRZ5LHPK13z9FwZVVT4XxVolhzWJ7pDct8Vx9IDSFuTiWDFM-e-JKYT1BxuYz0TL10vLyyGsWx76yedFUsmMV8i_IAxDjmykqGRzFUtvaDy_-vabsa6aj-4T0tQpL1pjhdPUo2Tu4cgtloCVDxyPboFHxc1Q7sBq0iyKV3fm-TtMgkZ1DfR0xFsMBofnlvI_e0fg10GcswhJxPg0zm_SZkmhNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
مذاکرات غیرمستقیم میان هیئت‌های آمریکا و ایران فردا با حضور میانجی‌ها در قطر برگزار می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/67089" target="_blank">📅 15:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67088">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhdfZn1vh58UHrLm8lfZkD-_V63xgH9zFbwZcNC0IT3WwiMAY-AIJyX2Y1XjhYJiroY0hzg_ntpHK1FTJtZ91F4TlAV8ZGtTJEfeWRtuEbMKVa3LD_-TUgNWR3ZWb92l583-5eyQiCGxzAgLxhFbXhOD5Eg691yQBOd7PmA1Y0l-iUXJB4UPPVEon3AH83c5Ow9-bejISwD2ksN5yOTc1Y5TLtzt-pbm-xKeZlSm0mucpaAvVC9TuZNeCoyubLxQsEmqCEQqnyGLprpwq1bd_VEINLAhBBqfHL0gcG46ldTmNlkYn4OiptaqRUJ0QuYl-Mk3OBVoJ8x3uu59RG9Uew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه همشهری با این تیتر ترامپ رو تهدید کرد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/67088" target="_blank">📅 15:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67087">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=JDAf80GfVsqBGPCHQvvkoBPMrsQM2vVANTTcl5anBnyar9EW40HPCdd59eg6j7K4QTC3AQ5n5P2RsivFEgr0H5umkNy6TRLekCPfo1N69iB5tTxbwLNCa75W9AD4L__1Lws5_3UBzfnwQlFRJmH4Sx94k_RskQt2uC2709HyKRyEtHQwwRNA0rIas0eiWo9VcSukTP7awb7rnZY2CYWbT9iB8i55lf0YAI6HAOQ4xOKMzkjNECnwjgheQUiLWH-mxm78cftV5px0xCMllBZAOtAlWqKSkf6MYyLMZxt33f0BJhEu-f-8t21zsIE8IaCuqNcPxZ4z9UBdCkQn4TVt1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=JDAf80GfVsqBGPCHQvvkoBPMrsQM2vVANTTcl5anBnyar9EW40HPCdd59eg6j7K4QTC3AQ5n5P2RsivFEgr0H5umkNy6TRLekCPfo1N69iB5tTxbwLNCa75W9AD4L__1Lws5_3UBzfnwQlFRJmH4Sx94k_RskQt2uC2709HyKRyEtHQwwRNA0rIas0eiWo9VcSukTP7awb7rnZY2CYWbT9iB8i55lf0YAI6HAOQ4xOKMzkjNECnwjgheQUiLWH-mxm78cftV5px0xCMllBZAOtAlWqKSkf6MYyLMZxt33f0BJhEu-f-8t21zsIE8IaCuqNcPxZ4z9UBdCkQn4TVt1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
ویدیوهای جدید از زلزله ۷.۸ ریشتری که در ۸ ژوئن ونزوئلا را لرزاند، در ساعات اخیر به سرعت در فضای مجازی پخش شده‌اند و لحظات پرتنشی را که در طول این لرزش قدرتمند تجربه شده است، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/67087" target="_blank">📅 14:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67083">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0ogAm1VWZYxX8epuOvnSY3NOWIypcelOK-NJmhP_u0O7bEl7Wm1U5UWx5SnXR18g0jKUJMUu5NakQH8_sX2rVC26crNb3YjCUoqjRPz1QucG0bBSjFBtd5LBQhXUCcxcTTS6Dmt11vUAXY8x9vw9Yon6428QHN7GWsMRfPF8daBseiogJNJ7Q2zet8wReyLNin1-1DIvlayfTlcfZfAGq7ajW6Linn2SoCzPz4EVCTxx8qpBk4hMZbgTClTBJUTrGga3kjKwndpNj8mpFyI7AJbdc3UPjV2vWf1lBLIWYNT1IXVfz8O8rnQcKNGrCeSu8lNt0HqMSzDeTGZ94q-ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGjz_08JDImxL9NPtQQFdK44ksvR0v-G8W8I86TsP9zqZvNpJ3jYnm9ywi6MyeQQ3wftUjrBwnEaplhHDjDkepmS-SkFDIM8iB0-dZ8lvsVRjH4WNHLLrYWVUVwCwPzQG5A-tNX_UpBv1j76fZ6r2RWiSsG18_X5517l5NQYvDnc7fx9vp2aDgYl6n-Ya94w5BAZA9s68jshdrETwLCU58jAeyxsbL1WwPG67d2URLD-yrw19vM6Ax1jrlXmFoG9JBp4FdCGMKmWGnox1CZDGj7xhT4wFJvrpVfOWDCL2-XEZjNUzkqcN0ufQnCKcuZkge21QyyJz89WkE6vtZfMqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qfPZl_UIVpAaQwEYJwNw6-LzNC7GQT0JpRXMbRyEZl9d0Ivfwvo-iZrT06Cf26w-2eD0Fo1eZJKin2n31DO0jVyGZ3jRf8tk5Y-3d1nG6vy1V7r2udzCEUX_MUDfZoP8tX9Wz0oExpylTN4iB8H2UTNT_lTeFyMOvVQm3LFXmGlksTHyEIzdkFIOA8WRZBFdKaxjJmQm7yBgN6Ej6Ps0I_usympFlihZkS6Hx5UwTQ-U14NgCsygdIhQd83lPUNjalrZdl_fgDgtowD3do-FkKRYvMdcu-CbBsOjj1h2rgSYGguuT1Pxx2qn3dF8PeaP5sJ1QmQ0xRvK9tgPekTrFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQ33eMYPhGn7V2fuWMMMiNHHEi2Mvf17pCsqmpS-JrVq3YhhP_FnjvMdKncYXdR_79Zh3GMbKxlRbLoDxPuSDsnRQ1ZtNby0gmRQyWNmujc8aOZhZRLWvFrzUkR1IgeKmDKZIIMRIn-mawufUAT-jPsDYIKLkuqfiEqAyX4YSWxKb5--4vihMcCwndeRO84dkfC5oZwatpapIZRmjqHPMgHAnExdJRoGzIN1zzwxTYqi4dQeyG72GTGwtr7KhsvKTlTI7xbOVCYTA7Nf-ewjiEazOTvl4FhvEGXkTfRa2UzFnfZJV0tPDt5G-cAhBaw69Co5tTDu2gGUMs8Hs2hicw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😂
یه پسر 19ساله به اسم آقا سامیار، اومده چندتا عکس از تولد خودش به همراه دوستاش تواینستاگرام پست کرده؛
حالا به دلایلی نامعلوم، این پست تولد آقا سامیار تو اینستاگرام فارسی به شدت وایرال شده و بیش از چندمیلیون بازدید گرفته:
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67083" target="_blank">📅 14:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67082">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
⚠️
قالیباف: سوپرانقلابی هایی که هیچ غلطی برای این انقلاب نکردند، ازهمه طلبکار هستند
این ویدیو از قالیباف مربوط به سال ۱۴۰۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/67082" target="_blank">📅 14:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67081">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی وزارت خارجه قطر :
هیئت ایرانی از اومدن به دوحه منصرف شدن و مذاکرات لغو شد.
۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67081" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67080">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
جرد کوشنر و استیو ویتکاف، فرستادگان آمریکا، در دوحه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67080" target="_blank">📅 14:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67079">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
هیچ نشستی در سطح عالی میان آمریکا و ایران برنامه‌ریزی نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67079" target="_blank">📅 14:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67078">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EQOova1yluilZtP9JY-O4NIQ72SJek6f4QopdbXFLcHKl7vTeCNo5R_yKWQHytgGDEPjhnWj3MYlBPcZgyB-J0z6Oto5Yl4IKa0kEnONUkebDfJiPpX1_wipnf_ytad3Swo8RZTAG-NM36QI8NbS1lRu7mNIRPSiA-zw_IJrM8JwAW0UT01BSoaiUMaCt3BMW1fXnhuf25ApzJg5s69yXJsLVlnBUKmRY2Zv69ubnV626UoxCgcO6mL580T5TStS8Egk4CurMnTuW-08vJmIy5HyJh24v3VC-0lt8sHTM-pIeF8u7aY-a9Eph_9Kc3yLluzy6qmWQpUPSKAxcjqzmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افت رتبه همه دانشگاه‌ های ایران در رتبه‌بندی کیواس ۲۰۲۶.
این فقط یک خبر آموزشی نیست؛ گزارشی از هزینه انزوای علمی کشور است.
رشد دانشگاه‌ها را با قطع اینترنت ، فیلترینگ، دیوارکشی دیجیتال و انزوای دانشجویان متوقف کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/67078" target="_blank">📅 13:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67077">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXykCPw51hgwYEx2VgnxXUjbBS2fMflF1QSsFLmVNh9IQmrAGg_zed9V__jc3gjM36Aor1QtTmzjt0qnpquEzR8faujxxiXQJHQoideh8DJz269Lolwp6VOBJJnsoQVf1NM3K_otZ2eDE2wJVr_AVBff_apqWf8aRwxtqTM205IRjmqswTs5KbHFEiMnSTMXeElXOytND4MGKr_Zpn1LIOfNau_Lidr9BDL9UiJ12sc4vNsm5DmZs9mOIUfp96qqZIQPZZdQ4_ogzRpyaeN_HyLFrOUyo1whMENkgjGIOtNoafX08mRbSBkXUd9ara1B2y2TymGCmKQ5wattIkOp4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
💢
فرماندهی حمله جهانی نیروی هوایی ایالات متحده برای اولین بار تایید کرد که یک بمب‌افکن پنهان‌کار B-2 یک موشک ضد کشتی برد بلند (LRASM) را بر فراز اقیانوس آرام شلیک کرده است. ادغام جدیدترین موشک ضد کشتی آمریکا در این بمب‌افکن تاکنون برای عموم ناشناخته بوده است.
💢
نیروی هوایی ایالات متحده اکنون توانایی انجام حملات اشباعی ضد کشتی را مستقیماً از قاره اصلی ایالات متحده دارد، در حالی که پروفایل پنهان‌کاری خود را حفظ می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/67077" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67074">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpC6vG6ECtlsHXyZtZ1Yd9kg49Uv4WQxPX6DC2zxW1qYZZV1TnE2prqJRYFU-hOVS_2q-2QdLjMlIbr1SJKj_6pGHU48lsCcqFx3vTO0fNZXfw6qIsMfK9AzLsq_qMsK_ZkFSOdcsBIUe1mCYUy0r2cmwxojGDgdHb9VyOyzqJa7j_xv_eV-o_b4IhbNuTK5gMIxlFlhqu41cLIBTKz8kUmcxfktl-XBvLbyPvjYsZRvuZOidD94s5hbaon0oL74CCVHXt8QxFz3zHbreA4FrVdpTqb1SMu3PqU9gbh3_RCs59cInc2X6YQZ_0KtgIgCjoDoNfNxJ2gbzTL85lEikw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚠️
🇺🇸
مولین، وزیر امنیت داخلی آمریکا: خیلی خوشحال شدم ایران از جام جهانی حذف شد. انقدر خوشحال شدم که رقصیدم. نصف اعضای تیمشون سپاهی بودن و هربار برای ورود و خروجشون کلی اذیت میشدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67074" target="_blank">📅 12:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67071">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TlW_1A2pNQxcHJAzkIXQKlzSpMRv0beXQ9k3a0hrdmX6mODchd_zX982uzXskU6z7x5ONRgUDjtYzvZutg1ss1eCU7Fj5AZtb-53FhW122CII6mcqX6yFnA6Tjx2JGorenGec0fwKIx9dvbLnvaMjVG9vVaWZTlWEhU1xc-PAhK3hO784O_nDA8KmpAzxDojasXMSFl7H84VJuiO01atHqA2Z1eIR1Sn35oy1CsIxGEkbpD3AWWP8_tEtA1nkNDHRNKje2WSikT0CwT3vz2vfIQLxB3vaiACmV3jJOfZyzBE7mjwm-3WHSwaTHNWQjNJ_m5d3E2tkM8kvjG2X0MTWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uiYwciNxEnvqhgRat9x1JCKgf_XytWE9n5IxIHC5EN2pVNq7x9Kw0C9GKCcfzK56J6wVd2k1h-ufAOqbNXvrDEFRHoeuplm0F3wSVOa3SUeOCOZZkih3POAttIci40eTBtd-sJ0ZyaYCqkxP1WG1v7csu-JFRvxGv-ArZxhOtJLNpfw_dtxz_8nbl16bfJHN26zv85xlhjLsaSStr0isXom00ZM3t_IsMshhP0bOP7Yt2oEmrqmqhw_uBrI5gGE6lZHlW7KhYQWRNGCOTU7XUf4vlMFVhfff4YrEtQ-UR5kH-Y-87qYvBJSJT0GPovkHGOok3Zm6PU81vxO2kt2WHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BdXdpjBe8nwlQx7z3F_EGy1Jz6O_Z_NJWy6FhCho2NUm-1dFFkDjDqwo4hQSoYIQts_sphVZJkB3FALTTTg4GqKmsQfHB4ayH9FtqGMxrPDGQzCWTWBH1ZLInVu8PEEt7QpIFBKXbqlsihFaO1euW5y5fkKyaaJlN-n5IoIy7Dh65BfzObApCMCPns8v2cVjl9kdQDcpZFRtrHyolewcRt9Fml0QOf7tzpzjedNSl2t4NmujHfcGNXA0127QRIcZWa_cwHEorJ5XFPyyzZU5f3pOalmmS2toe3NlUQF139cIJEAZoShNt7n2BDE8A1rBs5_hApmAz6kD5Sum1i875A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اشتباه نکنید، این زیرزمین خونه والتر وایت نیست، این بخشی از دلارها و طلاهای کشف‌شده در منزل یکی از نمایندگان پارلمان عراقه. حالا شما به این فکر کن توی جمهوری اسلامی از دون‌پایه‌ترین عضو  تا کله‌گنده‌ترین فرد چه اموال و میراثی از مملکت رو چپاول کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67071" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67070">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmVIBmwq8cpCtRZWy2ZFfn9s6xAMjAWA51BioJ-Z5fNLgC1WBm1PXgIfB4IQwoKILPEjtGG5Vf38rC9J5CWnE5ql4CCQ8Uf8r-Y-oAXj2EDwIKmdNi3vwh_uaSezs1Q_XBpdemrzNEoykdQlTnKTZ6Xgvz9Rwj0atQQmEmUjCY8N5P0W1yKMgT1mlqBLHlwpXaMvPRUr0vE7F56YpCEzVBI4QXDES9CUaMSeIbWv1625BSFN_n_Ihrw_mI3txT3Avoh4Gtyb0H94tQPsKH7UN5wg3L3w1UWUPD9wdQWoD4axk9Z8Rqf-o8KMtccvoMFQSU3a63qjjXCsw0XPXpey_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
اموال کشف شده تو خونه یکی از نماینده های مجلس عراق
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67070" target="_blank">📅 10:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67069">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=ptW60INbDxoPMQga3UFIKrQgbgO_YrXt6wo3f-Zxp1BrM5e2LKOpO_KAzxR9CdWnqUfBoncVcLYZ7A0lV7h9BWr-Rbso10rJgvkUekOHd873Lr-bFciApRJqRXCMO8BO5vI_E-WxG4Wt8fsTdEPjXmHj9D_Shnn4r6GGml-5yxrPF43bQa7V-JrOnECko58ORHEHDXd2Mg2CElx_sDTJLCS8j5Fm8zi0bUY1DXVWe5UB4Ji7QcBLG6VykbjOiSur-GBW7Zb6DkEMm9mLfYnMVfOGbAm9S0z_sy7jVwav4NO08TLlwpsmIlSfCjJLqc0jNCiu8wRwxeY2T62ARo70OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=ptW60INbDxoPMQga3UFIKrQgbgO_YrXt6wo3f-Zxp1BrM5e2LKOpO_KAzxR9CdWnqUfBoncVcLYZ7A0lV7h9BWr-Rbso10rJgvkUekOHd873Lr-bFciApRJqRXCMO8BO5vI_E-WxG4Wt8fsTdEPjXmHj9D_Shnn4r6GGml-5yxrPF43bQa7V-JrOnECko58ORHEHDXd2Mg2CElx_sDTJLCS8j5Fm8zi0bUY1DXVWe5UB4Ji7QcBLG6VykbjOiSur-GBW7Zb6DkEMm9mLfYnMVfOGbAm9S0z_sy7jVwav4NO08TLlwpsmIlSfCjJLqc0jNCiu8wRwxeY2T62ARo70OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مداح:
رو هلیکوپترشون غیرت داشتن بهتون حمله کردن و علی خامنه‌ای رو هنوز دفن نکردید.
۱۰۰ میلیارد دلار پولتون دست اوناست، و میخوان ۶ میلیاردشو بهتون سویا و ذرت بدن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67069" target="_blank">📅 10:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67068">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=LPkkeJ03i1Ih_tXiQShscgW82GQquzLtch5ZDqdT5qloWMuudv9VVrzofjXf8vxBzio9R3we-UGM48OVINozuKsQ-Mti79GUtpIopwLKg_BzmnGlM3lOHHx5WVUglTejh372o3FbhvKC3gxs6OrzLac0s1e3DMGBZYjoq40ThqDjnf2EyTGBSYg8vCN_lBy6shVZPJjGsfn17-Nbg-sv9htV9XSTdouSmn8YCmmhsDOrtLNt9klyWFpDhnOsH4gFZ983zcASKX-HeJnXiQc1DogUI9AClsH-_Om_Y5CHw2P6383brR4HH_qFcrWoV1KGLM1XIpJvv61S1uoUwnRYlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=LPkkeJ03i1Ih_tXiQShscgW82GQquzLtch5ZDqdT5qloWMuudv9VVrzofjXf8vxBzio9R3we-UGM48OVINozuKsQ-Mti79GUtpIopwLKg_BzmnGlM3lOHHx5WVUglTejh372o3FbhvKC3gxs6OrzLac0s1e3DMGBZYjoq40ThqDjnf2EyTGBSYg8vCN_lBy6shVZPJjGsfn17-Nbg-sv9htV9XSTdouSmn8YCmmhsDOrtLNt9klyWFpDhnOsH4gFZ983zcASKX-HeJnXiQc1DogUI9AClsH-_Om_Y5CHw2P6383brR4HH_qFcrWoV1KGLM1XIpJvv61S1uoUwnRYlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از سخنگوی‌زن‌قرارگاه خاتم‌الانبیا هم‌رونمایی‌شد
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67068" target="_blank">📅 10:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67067">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=btVz6eClnR1QR5TRvrHV5OsRPBQMaA67YljHRukdJbXE46PejgWZQmqqsK7hQY82pcWYXNhUQxu5iPvWDwu7M6z-jGalkQ-sgoR6emu34Uc-X6n-IqbzMZY28I5jrVgT_v-Rge6lGCQ7jxRQI-bpuOEqKQYmHKzX_ixli2aEZ9AK-JgQ7QNIjppmPYSIQ0etjTdVj_tfTiG-vMgj6WGATYrfIzg_wHM33e8ApcwaztkvBB5VIJyQzhShbgl52nIWBIhujnnaX3EypjB8XatS_LWf0nNKifhoERuZU7-rG-dp4ioSNChtl9rAgYGHEijJGDFZbURtzz4BHbW31OjTZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=btVz6eClnR1QR5TRvrHV5OsRPBQMaA67YljHRukdJbXE46PejgWZQmqqsK7hQY82pcWYXNhUQxu5iPvWDwu7M6z-jGalkQ-sgoR6emu34Uc-X6n-IqbzMZY28I5jrVgT_v-Rge6lGCQ7jxRQI-bpuOEqKQYmHKzX_ixli2aEZ9AK-JgQ7QNIjppmPYSIQ0etjTdVj_tfTiG-vMgj6WGATYrfIzg_wHM33e8ApcwaztkvBB5VIJyQzhShbgl52nIWBIhujnnaX3EypjB8XatS_LWf0nNKifhoERuZU7-rG-dp4ioSNChtl9rAgYGHEijJGDFZbURtzz4BHbW31OjTZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس تلویزیون:
جنگ تمام نشده در وقت استراحت بین دو نیمه هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67067" target="_blank">📅 09:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67066">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=m8FgviyKRGld4svE9dsKmR8wcJm9JiV4Is0W_ib-1HXd40k3Ju5_GNKavb6XGNlO9FeDR72StFnMKHyDlDBWoHBro0S-2e3LA_cRBIaUqdTenRjxrdZY2dtCEU4BkI_bNBjAUIicX_nmmEnhpavU-ldaxc1UEg9sXAvPa0lG3eVzou4ssLH77FcbeMQtUPljl90zhtq-9c2NOLIfCziehmtUrIemWZfYB7uh66FxaqQoe62TxjOuvZptGBZbRDzhTsiJP8bnJX1yaR8kjJIVhm2lZHcnVUGWcR8F9dqMa4rGSFlGpk9UdWCM_7p6eAhVgNAUUwcKR1gWcTOuk_jiCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=m8FgviyKRGld4svE9dsKmR8wcJm9JiV4Is0W_ib-1HXd40k3Ju5_GNKavb6XGNlO9FeDR72StFnMKHyDlDBWoHBro0S-2e3LA_cRBIaUqdTenRjxrdZY2dtCEU4BkI_bNBjAUIicX_nmmEnhpavU-ldaxc1UEg9sXAvPa0lG3eVzou4ssLH77FcbeMQtUPljl90zhtq-9c2NOLIfCziehmtUrIemWZfYB7uh66FxaqQoe62TxjOuvZptGBZbRDzhTsiJP8bnJX1yaR8kjJIVhm2lZHcnVUGWcR8F9dqMa4rGSFlGpk9UdWCM_7p6eAhVgNAUUwcKR1gWcTOuk_jiCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسعود پزشکیان در جریان مناظره‌های انتخابات ریاست‌جمهوری ۱۴۰۳ با مقایسه وضعیت امروز و دوران قبل از انقلاب گفت:
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67066" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67065">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67065" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67064">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nwE5adGO0A2e4t-WOKYdZvMgzGnpuhb6JSU6yE6EbzMcOIbuiHDYbDh4P1HSmt-P_yabtcpdAvCvzf_AXUkF0hfXj3yI23mBCpoHkX3eOS-AG4TQELepD8DDOa8eGy27rX4wGWmuDfhVarp6ctp7_bbL6THhXZVUyqoMILakcBkRrC9qTgIOP_-7s66Y-GiyFmNXF9neHRNw9FrguFAYHxRPnDgJLFidVrFA8_RxOuHHVA_t41IKOY-wBDXRJLbKbOhfb34hZ_icHJQLq-0XsJhQ6HSr7ScC9ReOMMUVK3nxXplCUJzMZBvkBPulagKP4oJC2leA1-xy-9CeatnHpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67064" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67063">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر جنگ اسرائیل:
احتمال دارد جنگ مجدد با ایران طی دو روز رخ دهد.
وی اعلام کرد که نیروهای دفاعی اسرائیل آماده عملیات و هدف قراردادن ایران در صورت استفاده ایران از موشک‌های بالستیک خود در راستای دفاع از لبنان هستند.
او از آماده‌باش کامل نیروهای اسرائیل خبر داد  اما خاطرنشان کرد در مذاکره و اقدامات آمریکا در راستای ایرانی‌ها دخالت نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67063" target="_blank">📅 02:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67061">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuPm5O56Hc8vFKDluvi7WZbpUa-HQsqw5K6C_hAH90F9XRGhBA-QSaDf0Q4H4mwnZMuHWAQRmF5ntuM_wD4Kc3UIfbuYzjvF4mSnYEF31gHmYNWb93gLB9RRDJi3-IWd3eOTqdKS0xGdY_DbGXpsMQqvg0Xidv20WkcPckBW_feplOrjbUrLK5zmlkFp3owXs3fkQqyo2fJBVkpFsNPjcIGLIWoqEAVf7sen7ExulsDnOvSA3FcFo5LTCCcbw64OEGb8IYV5Tcd8EoSiAc0uHfQe0AfrlDtA_Y66ghWNlo55RgM28lDv--5ccc2mvqvgIEQ6O_OF76EQGgYGHRNHUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویری از بیمارستان پاوه و هجوم خانواده های نیرو های امنیتی به این بیمارستان،به نظر تلفات و زخمی ها بالاست.
«کشته شدن سه پاسدار تا کنون تایید شده است.
سیروس درویشی،خالد خالدی،برهان کریسانی»
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67061" target="_blank">📅 01:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67060">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
گزارش‌ها از درگیری و حادثه امنیتی بین نیروهای کرد و نیروهای نظامی در شهر پاوه ارسال شده
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67060" target="_blank">📅 01:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67059">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpB5FelV197nqOLQGqKqJzKJnI42lKo_IHStKetjNfpdQWFiQ9C7ES60AazIkug0IjoHbucbLFUHE3wnzKeDLvpAWK7MC3SfiGO7bjDbvut_HBIfawWYdpL4Ajv1ruiJPW2FS33-Gijahxun3762peGZS7J5xlw6HnQO2iv1BwjKMk5tJf_9UhJrylGOqd2L_WQ9L0JuYx8hDTBWfxJ6Ox3wHyWdvcyHxi2omUDf-lkutA7nFErmIYjuN38-ItGpg583uemM5CmfaL2gG9yO1uAuK4Wk5A39g5BYxu2frMyGkEfVIP_5ThlbDsNFeN5NbUVahz8brhubXo4GwpLdOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
تفاهم امری طرفینی است. اگر طرف آمریکایی به تفاهم نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم.
رویکرد ما در مقابل رجزخوانی‌های نامعقول و تهدیدهای بی‌پشتوانه، تکیه بر عقلانیت و کرامت انسانی در تصمیم‌گیری‌ها و دفاع قاطع و بی‌پروا به هنگام عمل است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67059" target="_blank">📅 01:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67058">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
این نشست در دوحه شاید مهم باشد، شاید هم نه.
خواهیم دید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67058" target="_blank">📅 01:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67057">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15a452960e.mp4?token=YmYANDidpyWG7Ybuo9dO1W8mmaBojoO5jSnx5Cxlyvr-2kZefkygjMfJ6wgQrQX4wr18CKGEGLJc0ZtoRq_CoZhdO6TytkrwGSoHtOMoVsvsdWz_kIOomcY6kVIThDCAaLAiHnf8otrFo3U1RBweChf7aELN_FvbzoHl1QeLaUwLg6A60U4JOexF2h2SvsX-3Nmss3cq4QozTRIJPqFT7TN7nON675qqjDSlmCKikC36kqyivbxovWUnzyvtuFq4wBRcJRFjT5bEwKXZipFQj8vXnMmZZXbHbUqJ1lUFeCp4jxRxQC0okSDhaQonRYljNsq4v2LM62dCmMN-QQyIZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15a452960e.mp4?token=YmYANDidpyWG7Ybuo9dO1W8mmaBojoO5jSnx5Cxlyvr-2kZefkygjMfJ6wgQrQX4wr18CKGEGLJc0ZtoRq_CoZhdO6TytkrwGSoHtOMoVsvsdWz_kIOomcY6kVIThDCAaLAiHnf8otrFo3U1RBweChf7aELN_FvbzoHl1QeLaUwLg6A60U4JOexF2h2SvsX-3Nmss3cq4QozTRIJPqFT7TN7nON675qqjDSlmCKikC36kqyivbxovWUnzyvtuFq4wBRcJRFjT5bEwKXZipFQj8vXnMmZZXbHbUqJ1lUFeCp4jxRxQC0okSDhaQonRYljNsq4v2LM62dCmMN-QQyIZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ درباره کمونیسم:
این سوسیالیسم نیست؛ در واقع کمونیسم است. آن‌ها از واژه “سوسیال دموکرات” استفاده می‌کنند چون خیلی خوش‌آهنگ به نظر می‌رسد، اما در واقع درباره کمونیسم صحبت می‌کنید.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست، شاید از زمان تأسیس آن. این شامل جنگ جهانی اول، جنگ جهانی دوم، حملات ۱۱ سپتامبر و حمله پرل هاربر هم می‌شود.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست. بعضی‌ها وقتی این را می‌گویم می‌خندند، اما افراد آگاه خواهند گفت: “می‌دانید، احتمالاً حق با اوست.”
این در واقع وارد کردن کمونیسم به ایالات متحده آمریکا است. هیچ‌چیز تا این حد خطرناک نبوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67057" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67056">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgciX1gtoo50-alJM4VXlGbWOLFjeym0pD3KRZnDbOTeYbDbf8XPTjIWnPfnO3DzqUnaAy9HBH3bUVKwx_OH2tCsUfRohih3lKLU3LfLjnFGok7w756stO2_cPyBrSEK5JT1vnB80pqxmoHLje6I1VJWGjae23B5Q3JYBLcWzCMp9keYgRP0LVznuEtvaak0Hma8V9SKLAd9p_WDzROZL_r8OWX2YWwl-iMofLlWAIjLckyC6ZE4hbDxo6DnkGwaOlL6IR8yCzDE3MgBJhcqNNKdaEhWQo4bS96s6nsloUc1eIkTCqNfeIMVWLk6ch3Jk5pKn45fMaO-DIywhD-_6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67056" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67055">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=Be3UNhqtgwRK3iVWQIV-Lfham5wwzAN-g_S_GghrSbZWsNQ1Bf_rjHg4HCQBScPB_7TFz5OcWfwGD3A14ANIEVqIJv4ZpghN7KtPSzDZMfZd-vo7dFdS4Z4HpMwECa3d7gj0dAUJwwv-uGEsC7oYK9vYscgmjh4HcXSsDgLghERY0WGBpAop_5NABGwejhke21TgOVQ4GmhwowpneaS0D91IbfdTdCOwFGrHjoHZzVk_QGmSpCLgt-bOyt1BEpUIm8GijGmx7eZFW1W4rlTGuPsAJSZrs1OUnc0t0ncYv6Z6CPfapBvLAgrUr2rvBgDJpoeWPRNg9eJXJCPiIt4KRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=Be3UNhqtgwRK3iVWQIV-Lfham5wwzAN-g_S_GghrSbZWsNQ1Bf_rjHg4HCQBScPB_7TFz5OcWfwGD3A14ANIEVqIJv4ZpghN7KtPSzDZMfZd-vo7dFdS4Z4HpMwECa3d7gj0dAUJwwv-uGEsC7oYK9vYscgmjh4HcXSsDgLghERY0WGBpAop_5NABGwejhke21TgOVQ4GmhwowpneaS0D91IbfdTdCOwFGrHjoHZzVk_QGmSpCLgt-bOyt1BEpUIm8GijGmx7eZFW1W4rlTGuPsAJSZrs1OUnc0t0ncYv6Z6CPfapBvLAgrUr2rvBgDJpoeWPRNg9eJXJCPiIt4KRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67055" target="_blank">📅 00:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67054">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1336110317.mp4?token=mgEdW6CKXr3xw4CH70iPQsTcBCzykC6uTzH1A4aKsBuCGOs-PFcz-r8im8I5ze-NapH3ikC88CODnk7hss9nG9TrNmwaxHP2vzwQ7xwYi-pomLhy_Qb6eZJEZqCfSLz7cki0Rsp7Ddteta6NWIv9QCSIk9yNNGzVM99MParyDorMC2HtzJ1VjqX2L3180t6V_09pHDm1IrHXtB0VK6vKYiKoaRzRjE-Uk_3G6ccMOwZwBnURKXZNAc-gTCherSodBe_cEUU3iL5aLFKZhlSXFxWlv88ytHFmqcXGV2T1R8OiydFdixevo7psdrg6zWTwUualc8Oj_TyooDCrELeFJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1336110317.mp4?token=mgEdW6CKXr3xw4CH70iPQsTcBCzykC6uTzH1A4aKsBuCGOs-PFcz-r8im8I5ze-NapH3ikC88CODnk7hss9nG9TrNmwaxHP2vzwQ7xwYi-pomLhy_Qb6eZJEZqCfSLz7cki0Rsp7Ddteta6NWIv9QCSIk9yNNGzVM99MParyDorMC2HtzJ1VjqX2L3180t6V_09pHDm1IrHXtB0VK6vKYiKoaRzRjE-Uk_3G6ccMOwZwBnURKXZNAc-gTCherSodBe_cEUU3iL5aLFKZhlSXFxWlv88ytHFmqcXGV2T1R8OiydFdixevo7psdrg6zWTwUualc8Oj_TyooDCrELeFJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادگاه محاکمه ترامپ و نتانیاهو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67054" target="_blank">📅 23:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67053">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e959102c72.mp4?token=r7D0kO4RU-ILkWt_gVUsFWhim_hbcpRmGeuOC3q_l8BV2YzJ8vcc8KXYcKj-lXplezOWmppl_FHAUzlLgfUImiX1L5Cmb6hiqSOB7O3W7yQUoydnk8tkkZvfZRnkddKaXzx-hmCzzVMTfS3w6xf8mX59_CNh3LZl3I3pA03UH6JrLHcZK21dYNtN8LKGVvA3FvY6ej8hWbT0wXg9hGf3tbYcfWZBIz6hLbzReKecVWfT9J_m3a2XGFQrSCNEzxQodSyGBaWzRSrOCYfQQ0sbwb9qol2rp_H5V050DCi0EsWAl-m1DD04hsM_Hvh2W4YPQPn_wWBA4qzrI_KZh8LY_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e959102c72.mp4?token=r7D0kO4RU-ILkWt_gVUsFWhim_hbcpRmGeuOC3q_l8BV2YzJ8vcc8KXYcKj-lXplezOWmppl_FHAUzlLgfUImiX1L5Cmb6hiqSOB7O3W7yQUoydnk8tkkZvfZRnkddKaXzx-hmCzzVMTfS3w6xf8mX59_CNh3LZl3I3pA03UH6JrLHcZK21dYNtN8LKGVvA3FvY6ej8hWbT0wXg9hGf3tbYcfWZBIz6hLbzReKecVWfT9J_m3a2XGFQrSCNEzxQodSyGBaWzRSrOCYfQQ0sbwb9qol2rp_H5V050DCi0EsWAl-m1DD04hsM_Hvh2W4YPQPn_wWBA4qzrI_KZh8LY_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عزاداری پدر جاوید‌نام داوود عباسی بر سر مزار فرزندش.
جاوید‌نام داوود عباسی یکی دیگر از کشته شدگان اعتراضات ۱۸و۱۹ دی ماه ۱۴۰۴ ایران بود.
داوود عباسی روحت شاد
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67053" target="_blank">📅 23:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67052">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddOarcvnVSlFzuaW6k8PdbQ9cqLXMqiln8bx6Pgpct4yrpSnmAefQk4z07U-2A6KeETmmdk0SPu6Q4EOWmaVskE6TKhI-_fmNQBk9xYbvcbh1t-iQekeo7V5kRzfpRTZDKw7cCGLi3rQp5kxZpRS8F9TBdF0NfQFsjC_7J4xObWqsr3iR55vnLXEwhiLAKeeZVOhZBxfBMB9LKd88JIFXoaHloNRJ2ExalyfjfTW2CVtNCXjP1NoyZQV42-buAWVeeUUtV65imR4ICi3qG5ETa4Z57UvCGHReA6gOvUAKDqPgY9dBfQXMB89-_FteNmjAVMelMnwXmzky-IAJFb49g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری فارس
:
معاون سیاسی نیروی دریایی سپاه طی سانحه کشته شد
.
دریادار دوم محمد اکبرزاده، معاون سیاسی دفتر نمایندگی ولی فقیه در نیروی دریایی سپاه، ساعاتی پیش در یک سانحۀ رانندگی بر اثر واژگونی خودرو در یکی از جاده‌های استان کرمان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67052" target="_blank">📅 22:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67051">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‼️
اسماعیل بقائی: هیئت کارشناسی ایران برای پیگیری اجرای تفاهمات عازم دوحه می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به وضعیت اجرای بندهای مختلف یادداشت تفاهم از جمله در رابطه با موضوع فروش نفت و دسترسی آزاد به دارائی‌های مسدودشده ایران گفت: در رابطه با تعهد آمریکا طبق بند ۱۰ (فروش نفت) مجوزهای لازم از سوی آمریکا صادر شده و پیگیر روند اجرای آن هستیم. در رابطه با بند ۱۱ (آزادشدن دارایی‌های مسدودشده ایران) نیز فرآیند اجرایی شدن آن در حال پیگیری است. در این چارچوب، همین هفته هیاتی کارشناسی از جمهوری اسلامی ایران به دوحه اعزام می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به شروع مذاکرات برای توافق نهایی در چارچوب گروه‌های کاری تعیین شده، گفت: هنوز وارد مرحله مذاکره برای توافق نهایی نشده‌ایم؛ طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ و تداوم اجرای آنها است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67051" target="_blank">📅 21:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67050">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‼️
بقائی سخنگوی وزارت خارجه: هیچ‌گونه مذاکره‌ای با طرف آمریکایی طی روزهای آینده در دستور کار نیست
🔴
طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم و اینکه نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیات ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله بند ۱۱ انجام می‌شود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67050" target="_blank">📅 21:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67049">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=fHl8ot4KK0eVCws_yjR4jTL_OHWc2bp6aqJ1rl7IJi-cfq9MEF12LjSMZyt0Kwc_AnoChDRzliZe9TqlQ2SUa7s9l6ns7hEIwHpQt679QyScydzUF5afWV9D8Xt-01xzR6gVJSDnRWUkLzmco_S5WUe5Mfv_fRt8aRP9H4oSx4MK6cIIZKIbmkNtnNEt4LTSGnpCNK-AlL_wfCLL85_eCQ_3DNhnysuFAwbSVDHRHmhT8YWEGtIx4QLBTOeHG1DrCJtKj9sUy9AOmM-9o865peqL7WbVShScjOjWCzSWub40jszttRvzounfxJdiBNhQfbj9EsbSSpzNRBZsWMvTxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=fHl8ot4KK0eVCws_yjR4jTL_OHWc2bp6aqJ1rl7IJi-cfq9MEF12LjSMZyt0Kwc_AnoChDRzliZe9TqlQ2SUa7s9l6ns7hEIwHpQt679QyScydzUF5afWV9D8Xt-01xzR6gVJSDnRWUkLzmco_S5WUe5Mfv_fRt8aRP9H4oSx4MK6cIIZKIbmkNtnNEt4LTSGnpCNK-AlL_wfCLL85_eCQ_3DNhnysuFAwbSVDHRHmhT8YWEGtIx4QLBTOeHG1DrCJtKj9sUy9AOmM-9o865peqL7WbVShScjOjWCzSWub40jszttRvzounfxJdiBNhQfbj9EsbSSpzNRBZsWMvTxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناو آبراهام لینکن امریکا توسط سپاه غرق شد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67049" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67048">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=txMd1NkyrThd2qmUK0X9rd8sZt-wK01qaMw-dj2HGJzjZzo2NUJcrOKsd3kRQrE5_II4lO1CDHNDuNfaevIAi4lY75l4p2dDp_PCfD5JG4dcRtpM2xnjCdCSW-JwUY37XN3gmuuXuPTl_P4g6KnwzNBryM8kfRbjaU5gip10jh-w9eGCaaK3vQp1c-wmmtKEDEzVb3XxtW0mB_q8gMnPU_4XWFLavJocBh-IhyiCEjLhS-ltLawAT8hGrixYUPW_ksheO83FBK1b0e45qY72SK7Atc9VzFBRj1QeOqC-EVhCAsLQB8f-kbpV4uqcDZ5RpN_Aul9wmrm2IG2_ZDiNSZVTZKhNp-OD4j7GD8_8BknBMOLtJOXnxcX6ySNRUljMlSylFrHRHtHldtQUU7yF_UcwcgVCo5Jx3q-q-rUdslDii13cB0c_MR3poI0PAuVeOh3PQ4cnZO0f53tuB099Qu7_2CH4plE-6BFW32w8B4AETvQDIuNvLNtusNUCkDZ0aeckzlvfWTZbarhz3rJH19vie08Xq5Lb2lvwWnWclyADLTFp7IJwE79O0vQKDFeNAaJvfqrwmqeZ_ELLw8nGzpSNPAFVPyccC0oG35RwL01FXTd2MCxvLX-BnCsKSlmCIVTy2SoQFnzHiro7XN2HK6iz9ssXi0whtYdvGe_JiMk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=txMd1NkyrThd2qmUK0X9rd8sZt-wK01qaMw-dj2HGJzjZzo2NUJcrOKsd3kRQrE5_II4lO1CDHNDuNfaevIAi4lY75l4p2dDp_PCfD5JG4dcRtpM2xnjCdCSW-JwUY37XN3gmuuXuPTl_P4g6KnwzNBryM8kfRbjaU5gip10jh-w9eGCaaK3vQp1c-wmmtKEDEzVb3XxtW0mB_q8gMnPU_4XWFLavJocBh-IhyiCEjLhS-ltLawAT8hGrixYUPW_ksheO83FBK1b0e45qY72SK7Atc9VzFBRj1QeOqC-EVhCAsLQB8f-kbpV4uqcDZ5RpN_Aul9wmrm2IG2_ZDiNSZVTZKhNp-OD4j7GD8_8BknBMOLtJOXnxcX6ySNRUljMlSylFrHRHtHldtQUU7yF_UcwcgVCo5Jx3q-q-rUdslDii13cB0c_MR3poI0PAuVeOh3PQ4cnZO0f53tuB099Qu7_2CH4plE-6BFW32w8B4AETvQDIuNvLNtusNUCkDZ0aeckzlvfWTZbarhz3rJH19vie08Xq5Lb2lvwWnWclyADLTFp7IJwE79O0vQKDFeNAaJvfqrwmqeZ_ELLw8nGzpSNPAFVPyccC0oG35RwL01FXTd2MCxvLX-BnCsKSlmCIVTy2SoQFnzHiro7XN2HK6iz9ssXi0whtYdvGe_JiMk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی کارشناس برنامه خط انرژی به غیرقابل شکست بودن ناوهای آمریکایی اعتراف میکند:
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67048" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67047">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2iBtSEbsVeU0Ned4q_lIQA173sXKhA9kxCE1ipC5fktfYqlUpn4whhYolBFehzNb0AusuY1sppUViHIoB6DBwbZarfa_s_3u9xeDqKNqyT87BtVr_tpwGTsvfuisz2zWRj2VjApbU2qjpBWm4iuo48YfePyeFMcIiexNLZyXkbQMUgoW_NzwrlP3CvD8_S7n1FQDMCYrb7pqfjzGg9YvIoiMV74osxvFf0jHBj-bKPmsP9bsroMWejOgig-IDxFiIWoRgY4xMWIxTEG6BxClgptetcYkAqqssKimCl5emmgQQNH5uSapjkMKhgvZVTTKE9ZAS8iGWlwz7YM6e2VRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67047" target="_blank">📅 20:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67046">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
نیویورک پست به نقل از یک مقام آمریکایی:
ما به ایران روشن کردیم که تا زمانی که پیشرفتی در پرونده هسته‌ای حاصل نشود، دارایی‌های مسدود شده این کشور را آزاد نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67046" target="_blank">📅 20:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67045">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=jEnuNTkVujyLwh3Xzi8yrgoexkVtJcYm4Tp4IcRrhnaK5AswVB9CM4CPghh7weGZCPpoAbKJJhLus0jS7NULEPfsDdRoGpHRhJvFsvyj-OfjE2qIhhTLYB0N935K16Pj8rJbo6femNKVQ3KKnI2HBjVbruwdltXb__XcJSMdL8nS9S4ONb6tFLZu5Xkgp35h3kWOqeuLaJVV8AgYQK2SojeYjjRbOcummEMkOkIbkA-hIuJw28luD5ym_mRtx4R71K69Gjx3n35dTPWxU9TM1CnsgSi7F4vmiz6UydMZOAAwrqS0MxMoEw8eYJ_CPlQZK5jLrapgS_dNrADZRx8qtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=jEnuNTkVujyLwh3Xzi8yrgoexkVtJcYm4Tp4IcRrhnaK5AswVB9CM4CPghh7weGZCPpoAbKJJhLus0jS7NULEPfsDdRoGpHRhJvFsvyj-OfjE2qIhhTLYB0N935K16Pj8rJbo6femNKVQ3KKnI2HBjVbruwdltXb__XcJSMdL8nS9S4ONb6tFLZu5Xkgp35h3kWOqeuLaJVV8AgYQK2SojeYjjRbOcummEMkOkIbkA-hIuJw28luD5ym_mRtx4R71K69Gjx3n35dTPWxU9TM1CnsgSi7F4vmiz6UydMZOAAwrqS0MxMoEw8eYJ_CPlQZK5jLrapgS_dNrADZRx8qtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان این تحلیل رو سال ۱۳۹۸ مطرح کرده بود؛ تحلیلی که از سال‌ها مطالعه و شناختش از روابط بین‌الملل میومد. حالا بعد از گذشت حدود ۷ سال،
با دیدن اتفاقات امروز حرف‌هایی که اون زمان میزد، داره عیناً جلوی چشممون اتفاق میفته.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67045" target="_blank">📅 20:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67044">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLZ2pn8Xf2hO6qwsMf9Cuw-W0Xeu79MlU34RtiQB0EXWQKKOeQdyu5CJfDk3FZoDeodd0gJAUkwIQKOjcwNlU4xqOHuJ_P_AvbNL8HGifw_9sg1p06wv8vN45LVHySRiTV1rIKOklYagVBnAnttpZh_8sk6w2CHYjZYsQNR9Q3k4P1On1uvFpXo69VZ3Pt9Re3PO4F8GZEfWvtEfwxZnNRrYtvkOfb9QntOMJvTHGj-JTWWS6ZQIatyj1hGRsFQ0RofXbcYh_AwuMIkTtjFiiWzwMglqrbSb5W9oFsFrU28tYbzpXH3af6AKdf2V74mwmHT_c239kSN9NHCmNglIDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمله ارتش اسرائیل به دیر میماس در استان نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67044" target="_blank">📅 19:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67043">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز:
اگر ترامپ تصمیم بگیرد که مذاکرات به نتیجه نرسیده است یا اگر ایران به اسرائیل حمله کند، جنگ با ایران می‌تواند دوباره آغاز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67043" target="_blank">📅 19:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67042">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=M1H7uHRKmqCVXjHorLdCb_BudOsdUeyITjDwuuwr1TstvwEcz0GE3GKLY1nlYhOh6k2y1hxxVUdFTlggBm0l3pfqs0xjmlPs7OCYgz5PrF0KwWBdhT9IbYjlJ2Bc6rYMuigHvMDxPD7AUUMHBEk8QP89PdVihEUa3Wk1Eal88-e3mo2A4p3QQv1WE9KP14x9MfyOMd-eBiCEULdezDtFmfFVOkTbX2ReEo-VcRDOiB7REUcGTdvaSO0FAVY16HTz6L_3dLheNnl30CzmHQ_Wy46dvUflEsdg97_F2BciGTCgD690N13F1Z2rDmt71WxbDs3T-AV_QjoHGF3i9Fm3KYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=M1H7uHRKmqCVXjHorLdCb_BudOsdUeyITjDwuuwr1TstvwEcz0GE3GKLY1nlYhOh6k2y1hxxVUdFTlggBm0l3pfqs0xjmlPs7OCYgz5PrF0KwWBdhT9IbYjlJ2Bc6rYMuigHvMDxPD7AUUMHBEk8QP89PdVihEUa3Wk1Eal88-e3mo2A4p3QQv1WE9KP14x9MfyOMd-eBiCEULdezDtFmfFVOkTbX2ReEo-VcRDOiB7REUcGTdvaSO0FAVY16HTz6L_3dLheNnl30CzmHQ_Wy46dvUflEsdg97_F2BciGTCgD690N13F1Z2rDmt71WxbDs3T-AV_QjoHGF3i9Fm3KYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تردد در تنگه هرمز در دو روز اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67042" target="_blank">📅 19:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67041">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=oYraTGSpyVd40tk1l-Z-Jt2h-hlTR0zKyOgHCYZYkxUWb2-y5DEOeurdZj17j1LiYrEq4JCxeyR1QPUoCS1rRxGnx0n45tAvkfGDW9qvcQ8QaRdTtW1XRUBUGfSlecO7ImPw6ei2xIBmIc55q48MT83pBPEiYXlV8MfdvMXZL_pA2QY6U7kNo3kjEhoqNLs6_dR9pvHIXI8ozF2YrbK80yyy24NKCQr0V-rmBT3vZWlLhbX5MQR_wUo8J82mYE8zu973rmJOL_NBeQTn4tlBpUjphtC8iNVFKZjh4PQaAGqDFqYEuY_xlXetmdJjhF2AFV4C18DoXwNBq9yCRI5A2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=oYraTGSpyVd40tk1l-Z-Jt2h-hlTR0zKyOgHCYZYkxUWb2-y5DEOeurdZj17j1LiYrEq4JCxeyR1QPUoCS1rRxGnx0n45tAvkfGDW9qvcQ8QaRdTtW1XRUBUGfSlecO7ImPw6ei2xIBmIc55q48MT83pBPEiYXlV8MfdvMXZL_pA2QY6U7kNo3kjEhoqNLs6_dR9pvHIXI8ozF2YrbK80yyy24NKCQr0V-rmBT3vZWlLhbX5MQR_wUo8J82mYE8zu973rmJOL_NBeQTn4tlBpUjphtC8iNVFKZjh4PQaAGqDFqYEuY_xlXetmdJjhF2AFV4C18DoXwNBq9yCRI5A2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر امور خارجه قطر:
ایران یک کشور همسایه است. باید بین ما و آن تفاهم وجود داشته باشد.
آنچه اتفاق افتاد غیرقابل قبول است - هم علیه ما و هم علیه بقیه برادران ما در کشورهای خلیج فارس.
اما در نهایت، همه ما بخشی از یک منطقه هستیم و راه حل باید دیپلماتیک باشد.
ما می‌خواهیم یک منطقه مرفه ببینیم.
ما می‌خواهیم یک خلیج مرفه و یک ایران مرفه ببینیم که به طور سازنده با کشورهای خلیج فارس، با سطح بالایی از اعتماد و همکاری - به جای آنچه این جنگ‌ها به جا گذاشته‌اند - همکاری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67041" target="_blank">📅 18:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67040">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=BjnHmSXgBVIE6bljrmXi4DSUZV8U3UlLzH8N30o_5ayNXJkn1c7aRPxAGUQe426IX_HGoUYlpHD5tKPqcLL_Mp27-Ee4GfrwHCs3A-lg7TqIS7A11EuIUdKhrbRnLMgwHLf9v59JaLtyzOJJV7_G5VfCeoq_xKLdI-VW7Rlwunipfa7FJ_8oZrMAhgYBtuQ3McNFZ4ghY9GplLOKkDU48Fvu90iqbCZWklypnWs1tQeekoIoEBm80H2KE8bS8Klb7DIr8lNFNRaObQnv6VfOM487OnAS32pY6ZwLYhZ4KG8P5G1T6WHjpHi89F342XfKTY7kzDArntHIEYo9dyiPxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=BjnHmSXgBVIE6bljrmXi4DSUZV8U3UlLzH8N30o_5ayNXJkn1c7aRPxAGUQe426IX_HGoUYlpHD5tKPqcLL_Mp27-Ee4GfrwHCs3A-lg7TqIS7A11EuIUdKhrbRnLMgwHLf9v59JaLtyzOJJV7_G5VfCeoq_xKLdI-VW7Rlwunipfa7FJ_8oZrMAhgYBtuQ3McNFZ4ghY9GplLOKkDU48Fvu90iqbCZWklypnWs1tQeekoIoEBm80H2KE8bS8Klb7DIr8lNFNRaObQnv6VfOM487OnAS32pY6ZwLYhZ4KG8P5G1T6WHjpHi89F342XfKTY7kzDArntHIEYo9dyiPxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جزئیات اسکان و تغذیه در استان تهران در مراسم تشییع رهبر شهید
اطلاع‌رسانی رسمی جزئیات مراسم تشییع در کانال پرچمدار
👇🏼
t.me/Parchamdar_tv</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67040" target="_blank">📅 17:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67039">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=aKh5psVgLARa9lTQy4kIqiQWZHCQuprnqQ_ClegGhQbE5Pqzye1h3OjIKqkNmxjpkRE7txFMWLL7Cgm9KKAedzYruaAwFxM_WnjXOuTT2UtOxlz-HX6m2EAzupj6gUBCbe1RgVha4IlLpFm4Xrk3Qd2F7gvY-2nCMULTRHrnf0-ONX0SWWRM8Wks0nnShQQu5BxsUBRIRdJn6t4B3kjVmRIKRNLpwtF4vv-1MwPSnj8UB4gVSZSROydVRWwLoAaAYTfaFQZcX05NAFsZ_5oCZB_5uOkGZJsj6co9E3dQ6Y2eRLZrnO7WqbCNMmg0Z4hg-XPgu2nQDL7K1fbvIO3x8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=aKh5psVgLARa9lTQy4kIqiQWZHCQuprnqQ_ClegGhQbE5Pqzye1h3OjIKqkNmxjpkRE7txFMWLL7Cgm9KKAedzYruaAwFxM_WnjXOuTT2UtOxlz-HX6m2EAzupj6gUBCbe1RgVha4IlLpFm4Xrk3Qd2F7gvY-2nCMULTRHrnf0-ONX0SWWRM8Wks0nnShQQu5BxsUBRIRdJn6t4B3kjVmRIKRNLpwtF4vv-1MwPSnj8UB4gVSZSROydVRWwLoAaAYTfaFQZcX05NAFsZ_5oCZB_5uOkGZJsj6co9E3dQ6Y2eRLZrnO7WqbCNMmg0Z4hg-XPgu2nQDL7K1fbvIO3x8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه داماد، وسط مراسم عروسی تازه متوجه میشه عروس 11 نفر از دوستای پسرش رو هم به جشن عروسی دعوت کرده؛
گفته میشه داماد اول فکر می‌کرد اونایی که دور عروس حلقه زدن، فامیلش هستن؛ اما بعد از پرس‌وجو می‌فهمه همشون دوستای صمیمی عروسن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67039" target="_blank">📅 17:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67038">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=QoK4rvMsCl0X_-07ek3tYaZGdMKImxPO_6_ZmK1m4ofz2eas5M8oLEZWEIc1oSG-FAYStvtdnDeqJiJ2ZE9ir0klpQY39kQdyzNe5lFds43Rx-nG2dOKh3VKGnoTbuVpgLLu6dZRkHonr7SZHVQl0VtuAeoTYmB4SV_0t_tRsPDy87ytI3Ev7GT6G0J4IrhaT9NZOrT5D2SfZmeA7KoB2M_0m33ePHhIi5ACZMGb5L-ZznzhyZSnNALpNmVetIdvfhMZPmHrlOpUsQ2QfQQcvCDGkDQYD-kokThWCREZmSxDQ7UQRoPTY_NNX1se5OHK0_PxS4116HDdGFmrRhJDEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=QoK4rvMsCl0X_-07ek3tYaZGdMKImxPO_6_ZmK1m4ofz2eas5M8oLEZWEIc1oSG-FAYStvtdnDeqJiJ2ZE9ir0klpQY39kQdyzNe5lFds43Rx-nG2dOKh3VKGnoTbuVpgLLu6dZRkHonr7SZHVQl0VtuAeoTYmB4SV_0t_tRsPDy87ytI3Ev7GT6G0J4IrhaT9NZOrT5D2SfZmeA7KoB2M_0m33ePHhIi5ACZMGb5L-ZznzhyZSnNALpNmVetIdvfhMZPmHrlOpUsQ2QfQQcvCDGkDQYD-kokThWCREZmSxDQ7UQRoPTY_NNX1se5OHK0_PxS4116HDdGFmrRhJDEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جان کری، وزیر امور خارجه پیشین آمریکا، درباره ایران:
اوباما تحت فشار و اصرار نتانیاهو قرار گرفت تا در بمباران ایران مشارکت کند.
و از اوباما درخواست شد که اجازه (چراغ سبز) بدهد تا این اقدام انجام شود.
اما اوباما گفت نه و از مشارکت در آن خودداری کرد، و آن را یک اشتباه بسیار بزرگ می‌دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67038" target="_blank">📅 17:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67037">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=r6hmjlEMt8AvPUclVGMIAg81ffqfvxmPnb81en2BMgy_6L9FHR2MVRqTsnRN1sdtlaTC25fMkEINKaYJAx3sK0gGN7U86MymgzXMaf_bXqLk_amTjowMFbi8dNN3J-Wmu9iiTYR9YlNEl_iJdcB0L5s2I9n9Y8d1NZZLToy7g196RlS43H9sCcBngN8Iz7WYf5y1t6o6XSovugNRmkcbHYWWkmRP9UL6NfSJ4XFopxdqFhp2kBwy-dq4WU-4-xlm-z08aDXZxoWU7kUZ-GVj2Pipd64zp65ni3sVkso4CuFurzX091axvBu1Bi6Wzoyx7r8hjixYxkIJ4hdgLhK_uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=r6hmjlEMt8AvPUclVGMIAg81ffqfvxmPnb81en2BMgy_6L9FHR2MVRqTsnRN1sdtlaTC25fMkEINKaYJAx3sK0gGN7U86MymgzXMaf_bXqLk_amTjowMFbi8dNN3J-Wmu9iiTYR9YlNEl_iJdcB0L5s2I9n9Y8d1NZZLToy7g196RlS43H9sCcBngN8Iz7WYf5y1t6o6XSovugNRmkcbHYWWkmRP9UL6NfSJ4XFopxdqFhp2kBwy-dq4WU-4-xlm-z08aDXZxoWU7kUZ-GVj2Pipd64zp65ni3sVkso4CuFurzX091axvBu1Bi6Wzoyx7r8hjixYxkIJ4hdgLhK_uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو ای دردناک از لحظه وقوع زلزله در ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67037" target="_blank">📅 16:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67036">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=QX98rikyTaGeaF0SOXg5g5YKrJqG8gmjCbRaax5WAhHThAvEGdTzzfuk9I4PYt5_9je0jzebLJ1Cpyh6dpvbFaMkWQ2P0BV6uSRNVCfMSIGyljfe0FsLCVprQ3alOdM1yQZEO0HL5tDYyOdp-0KkaqTSxs32-WNnvJACAHzQDwhNIhwNwJvahLyzIxRu02G7nIt_bQsrt1rdqVAnXFYmVWx1kxcg_Uz0s8wyTmyHSLp1Bnj7qLCpqiWbMPY18CZDAdkG-pGR6zY63BFTfeORr6bt7Of0gpn61if-MRjv4BUzAni-jXgUdN_Tn7aUl-DeEhkx_FfDqDBKh25RDJ2_rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=QX98rikyTaGeaF0SOXg5g5YKrJqG8gmjCbRaax5WAhHThAvEGdTzzfuk9I4PYt5_9je0jzebLJ1Cpyh6dpvbFaMkWQ2P0BV6uSRNVCfMSIGyljfe0FsLCVprQ3alOdM1yQZEO0HL5tDYyOdp-0KkaqTSxs32-WNnvJACAHzQDwhNIhwNwJvahLyzIxRu02G7nIt_bQsrt1rdqVAnXFYmVWx1kxcg_Uz0s8wyTmyHSLp1Bnj7qLCpqiWbMPY18CZDAdkG-pGR6zY63BFTfeORr6bt7Of0gpn61if-MRjv4BUzAni-jXgUdN_Tn7aUl-DeEhkx_FfDqDBKh25RDJ2_rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حصیر آباد اهواز؛لحظه ساییدن سیم‌های برق شهری با «برج میلاد»:
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67036" target="_blank">📅 16:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67035">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
سخنگوی کاخ سفید:
استیو ویتکاف و جرد کوشنر، در نشست روز سه‌شنبه در دوحه با جمهوری اسلامی شرکت خواهند کرد.
همزمان با نشست‌های مقام‌های ارشد، گفت‌وگوهای فنی نیز برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67035" target="_blank">📅 15:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67034">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdF5GqyjzmpRvyN4JcPO0KwQRoYweSwL3LhqcnKZ_QbVK4KJU3vED7pF0SCy9Pept8iBlSm_ZCzKQ5hdnJUdCdjv9kE9A2QojCOl5_C4IQAAEhuIcnVLh1B0Su44GtmITGxaTW98Zsw998yPJkq0YS6s_iFiyq5gG5Yq3sn80sP3TLxAKfCvOEsS3Y_e_v_ZvOfIYecWZRMcWsMdmsQJB578yvHSeELmuSQZDL_P2GuL8QfRQfrQb3a6AccNqDAvXLplpcV-pbR1rzOdSiEgZ2dXIkVmzsphxC_KTpSiO1ywziDyZpR5Ru2Ujh5JLXO4z4yeqe1nNAt1oQVpp9kPeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران درخواست ملاقات داده است. این دیدار فردا در دوحه برگزار خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67034" target="_blank">📅 15:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67032">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQrpMZ0RfAu34ihaGdpIvB4L2YaoUM0nUpM8G14xJLvw2WDMZFULe2MMFh0DHu2WCRDkpgpxCJdfGh1S0yHLIGfxL-itqsJEbY5HuA19YfGiO0B_6H2ZND7BudoTIsMo4JuJ7PHL7FuBm93xeDQOea-xZANAaS1lAZ8iiS6u1E5eptLVfB2miv3Hm2LXjjm3CFD_WMe6mLmIiX6fRKO9U_KHC77eJb0UzaUilu8whGRnNk10WcH35WKtPgZvGuP92VMlDtFhJb2Ec7mn9cafAkG5LSUuYigf-48RG9RgQbUjZ6VggzyXaP3U0FH81tIZk_m8h8qeTi9pmIFpJRZShQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در تروث سوشال:
محبوبیتم تو نظرسنجی‌ها از همیشه بالاتره
حتی از روز انتخابات ۵ نوامبر هم بیشتره؛ با این حال ایران نباید سلاح هسته‌ای داشته باشه
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67032" target="_blank">📅 14:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67031">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uv-8siLWLvpw0K4RHMcuXu2o_LI0QEnWv-uIKCbn6IReZcXuWsSU2qIs6XYDmRb7lBFvioSNHsGgzfNzU84VuR8tcsKSlBooeMAAT9dq1Syj46l4WX95wZRDGbtPcoqVx9fGqZdunmsMpGSYYh0KS_PaVjC4LdVgGzsk-BbMCZAhDQnKgOqlR4-qv9gVJ1n1jwHgU-wqgWF2noYae3zUV9qU91GrS6ILs3d9Yw5QaPsV44lWeXL4frjRZ3aoAzm9I8Wxrexk03YtF7VJGr8LRunPdPpb8Jx6FhiLGemF-AlsJp3MFCqrGGet3WpRXhvwJdMKUp-kv6Nb7C-Md4Ykeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حسین شریعتمداری (کیهان) :
گام اول تحقق خواسته‌های رهبری در مذاکرات، تاکید بر تحویل ترامپ به جمهوری اسلامی برای محاکمه در مراجع قضایی ج ا است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67031" target="_blank">📅 14:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67030">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=Auf1lAUlnGERR8KK_Z-rCq7awlI43zq3UEduOI6VR6WQEpGpSOOjxqMfyKuNM11Yw_IdXnCMrqyWmqv_fbu6M4dZWpTYO4oulPkH5rMlImwnC7aiZ49sVgVPjwnP2RGQigxAOexUaUr26w0FY5ckyhyWsfxTQAOGqPIqycUeNhKzvKvJiGyZRapGQTfdWZYSlEfYvlopQIfX5xNJUsUKa9E7ajDbBXe4L_cgEcFiSr0pPqN_qItgATrgwzLwCo4RSyMZfKEzc_fx2gxo7aaVNq9ufJjgqN8kyxAck9LoQ9dlDif6n1qaD3upevR9QWOn6ULu7uJjPXzFBzx_7qrIcKNZ2MfhXM7ds91B6S17I1Mx3CiAqJrGb2lRWVyjTRcL8xBDHnSCPP-oY-DNrjc5VVX2iz3mvFXWXzIwWpgvBVP28PQSSqAt9KsOMzk9cZONB0Ngxejw1F9ITeyM9OlqzndlVxdrg6dWBexFROqQThpoiUmrVrOPrU4vkPIKL90bC_uJ7CMeUy-DUSMPdkvSGlH6bUvm7LRpGOjx3DSpmkb9zpQXVmWf154iEAAKQH2MgvYnn11QegeOtTWh3EH_8etJhHbu1TCDjlmnCsP_s9qwbve2WAQidFcPH4Im7vQcT97T3BXBphikZC6gLbcUIATMlhrQfiJlqdezEBnbSdU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=Auf1lAUlnGERR8KK_Z-rCq7awlI43zq3UEduOI6VR6WQEpGpSOOjxqMfyKuNM11Yw_IdXnCMrqyWmqv_fbu6M4dZWpTYO4oulPkH5rMlImwnC7aiZ49sVgVPjwnP2RGQigxAOexUaUr26w0FY5ckyhyWsfxTQAOGqPIqycUeNhKzvKvJiGyZRapGQTfdWZYSlEfYvlopQIfX5xNJUsUKa9E7ajDbBXe4L_cgEcFiSr0pPqN_qItgATrgwzLwCo4RSyMZfKEzc_fx2gxo7aaVNq9ufJjgqN8kyxAck9LoQ9dlDif6n1qaD3upevR9QWOn6ULu7uJjPXzFBzx_7qrIcKNZ2MfhXM7ds91B6S17I1Mx3CiAqJrGb2lRWVyjTRcL8xBDHnSCPP-oY-DNrjc5VVX2iz3mvFXWXzIwWpgvBVP28PQSSqAt9KsOMzk9cZONB0Ngxejw1F9ITeyM9OlqzndlVxdrg6dWBexFROqQThpoiUmrVrOPrU4vkPIKL90bC_uJ7CMeUy-DUSMPdkvSGlH6bUvm7LRpGOjx3DSpmkb9zpQXVmWf154iEAAKQH2MgvYnn11QegeOtTWh3EH_8etJhHbu1TCDjlmnCsP_s9qwbve2WAQidFcPH4Im7vQcT97T3BXBphikZC6gLbcUIATMlhrQfiJlqdezEBnbSdU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش چشم کارشناس صداوسیما:
آمریکا فقط به دنبال باز نگه داشتن تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67030" target="_blank">📅 13:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67029">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIrORde_rT4NOwvh-oUDqJUcrUZ0nXboBRQaDg9zZ6MlOM1Xgj_ZWgiC6Ea7zPyGcwS4x0BHIDfZIQku8ztAK-VtTyZLwY050iGHDmq0EUgOR1ML5nesoLTtyafnTCGTvvEdL08ajmTp5GeynzsI9ncY0ypwo1gPLdtkJIYg6vjOpux8f4mk9LiCTztVVBYu7xwQbX00QvkLG0jt9HXwaeUsKo85Di2xp6lkOlxGVMNC0RT9lJEHRYXzXS83eFUtNrAt_pz1WxVuCHI8gn92l7mUTbJMyNzURu0IU0UMRo4CWDrxpWf78pHStZLbDfA6rHogUmnP61QMHm6dfb99Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی : قالیباف ٬ عراقچی پس خون رهبرم چی؟!
واکنش صادقانه ممباقر و عباس اقا:
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67029" target="_blank">📅 12:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67028">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706d335e17.mp4?token=trN025zfGNShY2ODz3d5TQm_iykNunF3Vd_GmAmtvsVOwpe2-qonNUjz537p6dWVZtsf_lZAwQp8rwXOJqmOU2V9IbNvpsJBRHe9Is7R70EgtY9YCd0paeYvl_9aj0XCDHdluuBNrUx_NEZwO9VFLxaVrMjjmIxbR_tB6HI-fxg2U48k-bGV_UmUws2fRNL5QpGiaKCTH2h7oNBldDr3fchbQdy1vkKM-dEEz2LHnL_-GTU5jq61Yc6yQOom8DXfqeaffHS0ccgnHdI3UZkQBhh-7YepfZCwhPxnBB2bNkoXMsdWNMMZmcVaggOC7JblC7gbHmxFdLxV6izK51KufQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706d335e17.mp4?token=trN025zfGNShY2ODz3d5TQm_iykNunF3Vd_GmAmtvsVOwpe2-qonNUjz537p6dWVZtsf_lZAwQp8rwXOJqmOU2V9IbNvpsJBRHe9Is7R70EgtY9YCd0paeYvl_9aj0XCDHdluuBNrUx_NEZwO9VFLxaVrMjjmIxbR_tB6HI-fxg2U48k-bGV_UmUws2fRNL5QpGiaKCTH2h7oNBldDr3fchbQdy1vkKM-dEEz2LHnL_-GTU5jq61Yc6yQOom8DXfqeaffHS0ccgnHdI3UZkQBhh-7YepfZCwhPxnBB2bNkoXMsdWNMMZmcVaggOC7JblC7gbHmxFdLxV6izK51KufQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
آتش‌سوزی گسترده در پالایشگاه اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67028" target="_blank">📅 12:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67027">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
پزشکیان:
بر اساس برنامه‌ریزی‌های انجام‌شده، شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع در قطر، آزاد و به کشور بازگردانده خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67027" target="_blank">📅 11:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67026">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=Kz_UzkCJter1Kumhh93PYOb4VX4hz3a61J7iWGDZrW2jDi3UX8UoKCCSIwrsnxqxZPhOA9IoSOgNQiScCSQUkpKNGHwgllj1KlXLiPSlrRUc20GVI-fTNxwzBzldM1Tnce9mslMAvlR5SPf1rf7kAEdwj8KuEm2gqBhhKCgc7V63uNV1qZpI0q60s51WpJQKdhHQEjpHDj-JyQ0cgXAMNb193_BgPOw6cXVH06qr3rkFQ-4kMiWtCs-081iZiZc9-K_Ee0A_tRU_NOdyvQgX0h4-gJu0nRZO-Ua6X3DfJNK2clJELnF-ScLjrDcEpFSv9SkMI3PVSGlrZJVLMBlfLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=Kz_UzkCJter1Kumhh93PYOb4VX4hz3a61J7iWGDZrW2jDi3UX8UoKCCSIwrsnxqxZPhOA9IoSOgNQiScCSQUkpKNGHwgllj1KlXLiPSlrRUc20GVI-fTNxwzBzldM1Tnce9mslMAvlR5SPf1rf7kAEdwj8KuEm2gqBhhKCgc7V63uNV1qZpI0q60s51WpJQKdhHQEjpHDj-JyQ0cgXAMNb193_BgPOw6cXVH06qr3rkFQ-4kMiWtCs-081iZiZc9-K_Ee0A_tRU_NOdyvQgX0h4-gJu0nRZO-Ua6X3DfJNK2clJELnF-ScLjrDcEpFSv9SkMI3PVSGlrZJVLMBlfLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات سنگین به جنوب کشور در جنگ اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67026" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67025">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این کلیپ داره مثل بمب وایرال میشه، الجزایر گل سوم رو زده اتریشیا دعوا کردن که چرا طبق توافق پیش نرفتین‌...اونوقت بازیکن الجزایر اینجور با دست نشون داده که مساوی میشه نگران نباشید و ارومشون کرده  @sammfoott | پروکسی متصل</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67025" target="_blank">📅 11:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67024">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=QYENU4XM86S4HkBh5mScTIcmxw95cEWl6p6m0Gewd3GT_melR4djddreSd3VrVka163pU1dfPbBpqVMMzd8LEeWa4MMqsN2k7r_J_DyutZPTAtRfKXLu1XeJ5eAVgnvY3Q8nSdK6JlhtO1sueMbaUoDLvq47kKD4h07_yHonmMXWODce69Jum80bYCkEu15N4JWB6yIpxZavSB8fY2fiM_hkTxv_VaT4ZLuUNZ-qQmpyvBD2KhtiBAiNPGwrS2vUXli5Ul3XxSOUlld6KO9Nc4WySlGXc2wx1VQkHq-MRpvHQNNwagBGvwTai6S04wrg8zbTQZvV1fhjUnj4Ifov0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=QYENU4XM86S4HkBh5mScTIcmxw95cEWl6p6m0Gewd3GT_melR4djddreSd3VrVka163pU1dfPbBpqVMMzd8LEeWa4MMqsN2k7r_J_DyutZPTAtRfKXLu1XeJ5eAVgnvY3Q8nSdK6JlhtO1sueMbaUoDLvq47kKD4h07_yHonmMXWODce69Jum80bYCkEu15N4JWB6yIpxZavSB8fY2fiM_hkTxv_VaT4ZLuUNZ-qQmpyvBD2KhtiBAiNPGwrS2vUXli5Ul3XxSOUlld6KO9Nc4WySlGXc2wx1VQkHq-MRpvHQNNwagBGvwTai6S04wrg8zbTQZvV1fhjUnj4Ifov0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67024" target="_blank">📅 10:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67023">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91138929a8.mp4?token=M1J4NqiFige8H_fFQXskuj2s06Rp96mrq-ksLrsDa8saFhXRCm1Kr9tIwXuzpbQ625U6hDpSgB6RsVPbG09PjkqJ4POgFpsc8DqK94mIvDSqfE2oamfTteD2TRwGUeQZ39zXj7solEY2uxRyk1O43UuBDJOVNEWQqNRxtV1LzMeBT4Qk62WFmu2XrGoC6qP05238psbq_F-vPaCWE21dryzlNLH0Cgkxxa5XM2tCSaUtHS_kCbuXzg-EVtD6WZrYf7uy8HyuNRMOxP9q2Zk95HCI0xki0mOdErF6Bt9uaomcEBmrHnObOWKTEMDrAdkDstRrOi4hnL01DPLcQy-h1oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91138929a8.mp4?token=M1J4NqiFige8H_fFQXskuj2s06Rp96mrq-ksLrsDa8saFhXRCm1Kr9tIwXuzpbQ625U6hDpSgB6RsVPbG09PjkqJ4POgFpsc8DqK94mIvDSqfE2oamfTteD2TRwGUeQZ39zXj7solEY2uxRyk1O43UuBDJOVNEWQqNRxtV1LzMeBT4Qk62WFmu2XrGoC6qP05238psbq_F-vPaCWE21dryzlNLH0Cgkxxa5XM2tCSaUtHS_kCbuXzg-EVtD6WZrYf7uy8HyuNRMOxP9q2Zk95HCI0xki0mOdErF6Bt9uaomcEBmrHnObOWKTEMDrAdkDstRrOi4hnL01DPLcQy-h1oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
🇮🇱
بنیامین نتانیاهو، و یسرائیل کاتس، وزیر دفاع اسرائیل با انتشار بیانیه‌ای مشترک از کشف و انهدام یک شبکه زیرزمینی در منطقه «مجدل زون» واقع در جنوب لبنان خبر دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67023" target="_blank">📅 10:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67022">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJVlqPW57Y9IARXsDEJ6AuXExwEitBPzYMbMUdFbUkXR0kgzhGNRWNmvM2QHNPlRnGI8FiuW63JLpUmx2UDo-Tkm5GJLQ43xKwiVh-EpTrIXIq5awKgGfe1XVe2s-Gt4GLUbPQhbrA-aggN_4Zmy_WcVa-l47ERGSGZEX5Iekk54DtpLV-22Ulnk5z20kIXckKjuDxk1HrbpNj3aEG2WzmAyWy5Hp4XPxMAqW1DAurC5dbX7G3UIeNYTDcdb49JcCZqtzD87kdu_Fp7TZfyPYVaVJKjPWxS5HkoikiTl_D4tiqFovDyG6aMyyVmUAVRL0MVUtqD9I6Mq5-cwsan9hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شاهزاده رضا پهلوی:
🔴
‏از ۴ تا ۹ ژوئیه (١٣ تا ١٨ تیر)، هم‌زمان با برنامه‌های تبلیغاتی و فریبکارانه رژیم برای دفن بقایای جنایاتکار اعظم، علی خامنه‌ای، و در ششمین ماه خیزش ملی شجاعانه ۱۸ و ۱۹ دی، ایرانیان مهین‌پرست و آزادیخواه در قالب هفته جهانی اقدام برای آزادی ایران، به خیابان‌های سراسر جهان می‌آیند، تا واقعیت ایران را به گوش جهانیان برسانند، و هم‌زمان یاد جاویدنامان انقلاب شیروخورشید ایران را در ششمین ماه کشتارشان گرامی بدارند.
🔴
این کارزار ملی با گردهمایی‌های روز ۴ ژوئیه (۱۳ تیر) در برابر سفارتخانه‌های ایالات متحده در پایتخت‌های جهان آغاز خواهد شد.
🔴
پیام ما به ملت و دولت آمریکا در سالروز استقلال این کشور مشخص است: با تروریست‌ها معامله نکنید! مردم ایران را انتخاب کنید.
🔴
۲۵۰ سال پیش، آمریکا آزادی را برگزید. امروز نیز مردم ایران برای آزادی مبارزه می‌کنند.
🔴
معامله با رژیم جنایتکار جمهوری اسلامی در تضاد با آرمان‌ها و ارزش‌های ایالات متحده و جهان آزاد است.
🔴
هم‌میهنان در داخل کشور نیز می‌توانند با حفظ امنیت و پنهان نگه داشتن هویت خود، از طریق ضبط ویدئو بر مزار جاویدنامان، دیوارنویسی و دیگر روش‌های خلاقانه، پیام‌های مشابهی را خطاب به ملت و دولت آمریکا منتشر کنند.
🔴
برنامه‌های دیگر هفته جهانی اقدام برای آزادی ایران به مرور به اطلاع خواهد رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67022" target="_blank">📅 09:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67021">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‼️
آتش زدن متن تفاهم‌نامه توسط یک مداح تندرو
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67021" target="_blank">📅 09:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67020">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67020" target="_blank">📅 04:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67018">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TH7yVCntZm6NW3QEYxCSnNYuBDNLRXnG6abVp0QLDkDwN0Q9F3rTnI0xxHAD0LhhpBZ7cJT_ZqdLmIKO1PFlcS4qvEHJp7MdTMm4TZKbZvciOQpyT70w0kc4H-eSJ5kx58SHWcZkHqQyvGq7b8MoFmLJPp4B8IYzQGNhQKNs015x08CVUFxM8sC4PaJsRbUJaCXbXslcWWlvTAhRtYoU_040WTYSy15teGOfWyF8UgiX4c7Fx1NRYKPNSUE_f3CW1dSQsYnIBnsNXm3dxwKhkH5FGaDJ4M0aqK_cYWnfjgr476pm2hYvow5XdgW8acze4xA5luX3Ypo2KSWeKuNLDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67018" target="_blank">📅 02:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67017">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=sNUr_fNGfOYybp0F18HA6scH7U3ruy_GNJwMcdI0wzS-bL8O2g339F8XNTm-pLPpZxdvhUbtLgPibkmUd56dP0G-Pym78Lomv8kmnF9E5F6ECAnY4wbcLokWmys-KC-SfaZaQ-POnBT8oiMx_uZBZqe5npgZxgaFhRitXT_TOb58sVE6fdvHdWHuZlTQ60LMNiw4ldEdVAGV4uLdHMt3LwHyQzKXjzUuoRq-axtmrqpr0ocIiTuBqkoyJIM-x7dljvp5vEi_wS5rBsM4AzW1Gmix_kxCDvoZIaI_EBfQdqQG2mZd_JaIijRJS7V6idl42hTHJfpLvQrsqTNyXeDZAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=sNUr_fNGfOYybp0F18HA6scH7U3ruy_GNJwMcdI0wzS-bL8O2g339F8XNTm-pLPpZxdvhUbtLgPibkmUd56dP0G-Pym78Lomv8kmnF9E5F6ECAnY4wbcLokWmys-KC-SfaZaQ-POnBT8oiMx_uZBZqe5npgZxgaFhRitXT_TOb58sVE6fdvHdWHuZlTQ60LMNiw4ldEdVAGV4uLdHMt3LwHyQzKXjzUuoRq-axtmrqpr0ocIiTuBqkoyJIM-x7dljvp5vEi_wS5rBsM4AzW1Gmix_kxCDvoZIaI_EBfQdqQG2mZd_JaIijRJS7V6idl42hTHJfpLvQrsqTNyXeDZAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات هوایی پاکستان به ۳ نقطه در خاک افغانستان
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67017" target="_blank">📅 01:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67016">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=TgaP9D-FxgkIqsp7IKi-ePDZpzglM2llYxsr8jbKKDvTwbp_A4DJ8cGvx5YAOtRzVTmbr_mGwXDTbLXOFl6HOVnzoW3y0NoSmrWUWyQEVCpaZg2nStJjL8rxF3nKK9gvis6SuKHmIAtAJIeX7aoUgGArAxAOkQNuVVOvhwF5DtR1tpNQtB8ERQaacmk7WDnopVumzrDL3gg8564kjJ2qa1SpFPuaL62Z6lUvVmELSdmMHSQ79QitqT-sUSIFRaE5d9FTM7NcettYd-R9ZVkJNhU_-O0H51ovbiKJN1jNTYmItBXSSa3wti2-MAq47C0eKkAV9m0IRJiUVUv9Qc67Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=TgaP9D-FxgkIqsp7IKi-ePDZpzglM2llYxsr8jbKKDvTwbp_A4DJ8cGvx5YAOtRzVTmbr_mGwXDTbLXOFl6HOVnzoW3y0NoSmrWUWyQEVCpaZg2nStJjL8rxF3nKK9gvis6SuKHmIAtAJIeX7aoUgGArAxAOkQNuVVOvhwF5DtR1tpNQtB8ERQaacmk7WDnopVumzrDL3gg8564kjJ2qa1SpFPuaL62Z6lUvVmELSdmMHSQ79QitqT-sUSIFRaE5d9FTM7NcettYd-R9ZVkJNhU_-O0H51ovbiKJN1jNTYmItBXSSa3wti2-MAq47C0eKkAV9m0IRJiUVUv9Qc67Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فعالیت ۲۴ساعته و سنگین ترابری هوایی آمریکا طی ۷ روز اخیر در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67016" target="_blank">📅 00:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67015">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xjp0uZ1LVLd3ECm4gpsRvs6LXi4rM-Bz2DzlvtDOG72yt3n6NNwHu6Sn3oix4xNw25VEqmPdU-EKBnfwy5f9YsIDDjUK2xI13JpVqs51mU5ETgSM6-qE0PwQpHOLNFYrwNA6G5zXQRoiVbS0CGwFkXV0xHA2cDVhuYTIleUadKplBLL8rAZrfHUWcBXAtwfemBLbsG11TyWIHeE7myhAxIm8EPeV2eG0DEIOhNEjoo-UUqmrmcOMWcetGb-rZzFq1K2oo15fmB1YCwrP1-yC20y3w0QnAzUxe9IjMwsrdpInMdVRfRmzLuzb40gsIpydOibjYJXX90p4JxJ2Evg6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آکسیوس:
به گفته یک مقام ارشد آمریکایی، ایالات متحده و ایران توافق کردند که حمله به یکدیگر را متوقف کنند، در حالی که دو طرف قصد دارند روز سه‌شنبه در پایتخت قطر برای حل اختلاف خود بر سر تنگه هرمز دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67015" target="_blank">📅 00:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67014">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=abm_XV9P-joaGymHmRVw0Y-QietB4AZilhkj73CjreAMPyuPpwsFe0CRScGuYySie07x8eZmjQ-4MV8Qgy6sXfxxRsq8j3sfpeOsrZgewJKyUr7b2T3TskgT3m-JA0bWToH4PfsAvRcSZhcfnHKv6ME2rtkHUP1gfiSDyuBthddBv5Hj_8EpbOUcmBTi7MI9m8ovAOjMM1I36ae_WApE5PJsTRl2zoeg9QI-O83BUwMaLCSzdMRHYhN-NY9aEAyZ-vqvbsmGzmcm_FIgImvkX8icYv7NHdEem4ng9nZtn0JO6ROsqnO6GEBL-VHAPOIWax5DPxTW2jXwGcOddDtY-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=abm_XV9P-joaGymHmRVw0Y-QietB4AZilhkj73CjreAMPyuPpwsFe0CRScGuYySie07x8eZmjQ-4MV8Qgy6sXfxxRsq8j3sfpeOsrZgewJKyUr7b2T3TskgT3m-JA0bWToH4PfsAvRcSZhcfnHKv6ME2rtkHUP1gfiSDyuBthddBv5Hj_8EpbOUcmBTi7MI9m8ovAOjMM1I36ae_WApE5PJsTRl2zoeg9QI-O83BUwMaLCSzdMRHYhN-NY9aEAyZ-vqvbsmGzmcm_FIgImvkX8icYv7NHdEem4ng9nZtn0JO6ROsqnO6GEBL-VHAPOIWax5DPxTW2jXwGcOddDtY-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دختره رفته پیش دکتر، یه تیکه نبات تو واژنش گیر کرده! دکتره میگه این چیه؟؟
میگه ما یه رسمی داریم، بعدِ عقد نبات میذاریم داخل واژن‌مون، بعدش میندازیم تو چایی که داماد بخوره. چون با اینکار زندگی شیرین میشه!
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67014" target="_blank">📅 00:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67013">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=q96ea6snwjfr27SjzvBnNzPOEZfiMiYqtfRHX0c_wHGQLfnoNHRO_cned8D-DwBxivnd4JGS4Yr6qHfIJbhbFr7y15dQdZyXHVWuzWm4ju7S1fh2F3jUuJXFNfJkX0ifSQ3ROWbzXOPbSoeIlBsFvjpjsiDaTaMe_WYLRyhvkcrKxWZRDl1_YLygGSKXt6alTmW3XX2P-n7cPP1HCLtYJ6UeSWd2VMlHLlE1qgoPYKfK1MeG72xjtCqhLLe-wZ5ZVK_WgCDTpWy4bKcoJhVb_xu1-uzC8Nn8uW2OFJhzMzdC74nOHcwQFNYeu7eNgCf6TlfC4ILrR4BebXQU5jQ0Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=q96ea6snwjfr27SjzvBnNzPOEZfiMiYqtfRHX0c_wHGQLfnoNHRO_cned8D-DwBxivnd4JGS4Yr6qHfIJbhbFr7y15dQdZyXHVWuzWm4ju7S1fh2F3jUuJXFNfJkX0ifSQ3ROWbzXOPbSoeIlBsFvjpjsiDaTaMe_WYLRyhvkcrKxWZRDl1_YLygGSKXt6alTmW3XX2P-n7cPP1HCLtYJ6UeSWd2VMlHLlE1qgoPYKfK1MeG72xjtCqhLLe-wZ5ZVK_WgCDTpWy4bKcoJhVb_xu1-uzC8Nn8uW2OFJhzMzdC74nOHcwQFNYeu7eNgCf6TlfC4ILrR4BebXQU5jQ0Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله آخرالزمانی اوکراین به پالایشگاه نفت اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67013" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67012">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDsvNSAyTVwjNUCysJB0ganKAlj-rBo5j9KBVuJi4ZEb-yiC1BW7oLZWLwPLUuCRv3KzFnjzmg9YYMxCG1QIX6Sym96iV-Xo49Cylp9lvN_zjFzObuqrGZliIpQFwg_hH8uVM_3URUJZoBqxNDB_x9byzw2bD3Y9mD7he2DYqxfumTQuRf0BlVXYeWRJUBrcs6J7Fv_gNEcojzv6K5JjhmGR-VSAK6KEgYrSvyXHuBKPjm1m0y2oBfB8IJxXxpPi-VMYBMVJ0W0z9MUwo9LTgBMgh0KCGvfyPc1g-_W--qlVg-Lrl0ntv5J8agxBjtBJilLWd4CiVzsw7dhcDLfeWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل به شهرک‌های مفدون و نبطیه الفوقاء در جنوب لبنان حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67012" target="_blank">📅 23:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67011">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-FwZ7SzKZyPBXluZETKZRIt5BF-fxihdjL5lqlYWp1cD1xOT-fIp-fk0f4FN6xUhOjCudd8wWlkn4eqdJiWLbVWwPTiuBbQ6USjaNl7HOxFwDpBo_9249-0YuJaDFK4JO6-Qtl3SxU4EVfWMGiez5jG35S_ACyWgPCe9t0X_JdHx5i91WInRZq5ae25upG976k3Pi3AdewRLKb7qfVZRcgvV_FeZ2IZ2wHpyahlhV280s22fncWTHrZdaFPQMTB3oLPGuWyKi8YBmCjEZryMwoDeR9skWYej1L59I2zPxqx8mMMJxPRWY0KpWJUzb9Gv5H-6vsDFMLpatI8d_zlRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67011" target="_blank">📅 22:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67009">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GJZDoBEQw2xjavSleo6G-mNwO9G-cbrO96LOPvGDPh3L-78X_4mEb0KOrQQMgfosJxdkWtOnXRMjnjBPIf0Fu5b5bGTCjpfzNt39tYzq_mqP859qNyEbiiri9aTx9cdIa9KS2VQfbXbpVZkgXP-CWa1XKpTYkXF2B8zPlNnG_1WCUg4bU-36A6ehqbQZ3XNCYjuFAgSinnrA7sL1YflOJ--FgX2tXjVxYm-gjbe4NG5hXgOr9RN1K360gf1Qo_WcX0WaPkM3wpf2yatEk4aUJfXAKbX319UmRNsDtEaAq1orwXcagzrXLLoy8gs2wWvT4wgeN70MPls3n_37ql6bDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=dK633XqCvj4Y8dfV-miA0iQXkx-PsH5pY7r97Xi_dFU3Ay7WK9egSgdkW4KanbSbi04vnVhYbpKh4gVGOmDR9bXOJYA4FjO2CbA8wlb4oM7OtT1Ed8HDIi4UF5DRQNZEWfHID4rGiJOOiKBNX79VHz5Nq57nPnaJLCEDvkRFtQimR1Up_6nyYksdPvvaPlQj4JLisb1E7bsD13f53cZBkaR4bMt_Rn6R9GT7mB41LW6v_dN6-nPDlb86QhoDVcqusEPBK3DDf6VCTjh6cROoAf27qcJHHcs50Ok2J4bPegnvSOiAoaLTW65vg09N_0-wHnYornAzOWX2TTt-6SXKiA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=dK633XqCvj4Y8dfV-miA0iQXkx-PsH5pY7r97Xi_dFU3Ay7WK9egSgdkW4KanbSbi04vnVhYbpKh4gVGOmDR9bXOJYA4FjO2CbA8wlb4oM7OtT1Ed8HDIi4UF5DRQNZEWfHID4rGiJOOiKBNX79VHz5Nq57nPnaJLCEDvkRFtQimR1Up_6nyYksdPvvaPlQj4JLisb1E7bsD13f53cZBkaR4bMt_Rn6R9GT7mB41LW6v_dN6-nPDlb86QhoDVcqusEPBK3DDf6VCTjh6cROoAf27qcJHHcs50Ok2J4bPegnvSOiAoaLTW65vg09N_0-wHnYornAzOWX2TTt-6SXKiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاری ندارم که حیوون خونگی این آقا مار کبراست! مشتی چطوری مار کبرارو قانع کردی چایی بخوره؟!
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67009" target="_blank">📅 22:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67008">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🇺🇸
یک مقام امریکایی:
هر شب رژیم ایران حداقل ۶ پهپاد را به سمت کشتی‌ها در تنگه هرمز شلیک می‌کند که برخی از آنها توسط ارتش ایالات متحده رهگیری می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67008" target="_blank">📅 21:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67007">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFjvnErHtpHdCVNQntkdGzB9ACKtq3xxrdSwd7y1ACt3OpUZt9VvvEx9080mwcVbezbKp5p9iMaM12fZOpo1Ak3zT75R29OV6l1OUJCZ-VhFleZR0qT4T8hkYFLW_0M8T9t0MkotO0g7ipKHtHO4xdlCvoHWvyzGaRY46mXjvITDsFc65fdQ9pLupI15ge3u7HfkbiwMkVrWIb91HU92raXdsyBaeYtSylcwxWgf8V9tiII7bE0AY1IQEUnyppwfeY7UxonXHINxey-Dx7QGcMI89p1K9cb_Al1F19f-VY04-YLSLS87HIQb0pIN7YmaBK81mBH1t4OuIEMsoJMcPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو درباره ترکیه:
تقریباً هیچ روزی نمی‌گذرد که اردوغان خواستار نابودی دولت اسرائیل نشود.
ما این سخنان را بسیار جدی می‌گیریم، زیرا اگر یک چیز را از تاریخ مردم خود آموخته باشیم این است که وقتی کسی می‌گوید قصد نابودی شما را دارد، باید او را جدی گرفت.
ما این اظهارات را جدی می‌گیریم و آن‌ها را به اطلاع دوستان آمریکایی خود نیز خواهیم رساند. ما آن‌ها را نادیده نمی‌گیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67007" target="_blank">📅 20:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67006">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdPGs71ZaIh6JemQqRGC-R7Alci6l07nnwa0fTYtnHcX_i56udkV14CaaHJifg_uZxi--CA6xYY7fzukfC8sfV0G3c_t-yjOdtSQVW-x8-iEV7JuaJPeY41BPnpju3A67sIOjbAKlOYI086l0OgvnCK1Un4zSCs9ybdIck7oyn6SQ4rEjSkIf803Ww3a5qer2e7hoZZj0As9RksOQfvggensZB4m4YqGN5upxfPNgOokQrPbH5bIYLf6ZcA-w4rA3WDaUzXoDWfU4_8scaIx5ZAkeqkgu4hd7mkvRBi9ra6Q2xyEeBaOehvU-X4AM20KqrA-tboIFDMCpoTXA5G2Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:
آتش بس ایران و آمریکا در شکننده ترین حالت خودش. چون مذاکرات به شدت ضعیف شده و برگزاری دوربعدی بعید بنظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67006" target="_blank">📅 20:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67005">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
وال استریت ژورنال به نقل از منابع:
مذاکرات برنامه‌ریزی شده برای این هفته بین واشنگتن و تهران در سوئیس به دلیل تشدید درگیری‌ها متوقف شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67005" target="_blank">📅 20:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67004">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=v-M_FZi8UgieYrWwTEvErmSFmwQYd7oF14Zg-8TLrOFLjtf2NLU3PGYUVoZxD10zqTBtC2oilkvflFnkcqABgfgOys3cG6hatISjHMc-KHUb_Ni6w9gx3dKYUI3cpBpwlizRYSKxr6KHreahbUyiHZJ8LwMt8NVl_b7DQio63PBQXzPM2anDwxmJ9GgtnmEf9to8_8bH_bqN1NIIOjaEPGcuY-105ga7yp4xUf_mGi5D9eLKeMZKi6IrarpFC-DKQNKg2LK7mn62E3Mn0cyAE_03N-hQuMm0KBIS22f7KXzMogDfd92i0ULfjEKcDqnkPpr7ToTGkXrd7tY3v9k7oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=v-M_FZi8UgieYrWwTEvErmSFmwQYd7oF14Zg-8TLrOFLjtf2NLU3PGYUVoZxD10zqTBtC2oilkvflFnkcqABgfgOys3cG6hatISjHMc-KHUb_Ni6w9gx3dKYUI3cpBpwlizRYSKxr6KHreahbUyiHZJ8LwMt8NVl_b7DQio63PBQXzPM2anDwxmJ9GgtnmEf9to8_8bH_bqN1NIIOjaEPGcuY-105ga7yp4xUf_mGi5D9eLKeMZKi6IrarpFC-DKQNKg2LK7mn62E3Mn0cyAE_03N-hQuMm0KBIS22f7KXzMogDfd92i0ULfjEKcDqnkPpr7ToTGkXrd7tY3v9k7oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو سپاه از حمله موشکی دیشب
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67004" target="_blank">📅 19:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67003">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=V-KH4EWS0d4i_fTD90NMl-CRrLDBZz4o4Wp7ZD-rki8A-7uVKw5-wngwZ9Vwo2mRgCTyjfsoRZxla5p9lmlW2EORtDEAaqMmEBPuzOx2bbBlWIjqzeXH23A3HiPJgeglqLxsU9z_DysWJlBPngX6DC02IBx7y6mHmPGVCcLptSND-6qBGpj1TpQJb-j5fyrhzegs8GJ5Ll9YDTSyoMOZah56yebTaD9vwamRozqHWNSJty8xE2PvH5Pt2Fvq9lnJ5A4lsWR4Tya58qwf9gZ9iFjsTDYShxo9gNu_ze403d-6r5jQGpS4oHDr1A-s9oCKLx6D14wdt-LtxZN29migPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=V-KH4EWS0d4i_fTD90NMl-CRrLDBZz4o4Wp7ZD-rki8A-7uVKw5-wngwZ9Vwo2mRgCTyjfsoRZxla5p9lmlW2EORtDEAaqMmEBPuzOx2bbBlWIjqzeXH23A3HiPJgeglqLxsU9z_DysWJlBPngX6DC02IBx7y6mHmPGVCcLptSND-6qBGpj1TpQJb-j5fyrhzegs8GJ5Ll9YDTSyoMOZah56yebTaD9vwamRozqHWNSJty8xE2PvH5Pt2Fvq9lnJ5A4lsWR4Tya58qwf9gZ9iFjsTDYShxo9gNu_ze403d-6r5jQGpS4oHDr1A-s9oCKLx6D14wdt-LtxZN29migPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سنتکام:
ملوانان آمریکایی سوار بر ناو هواپیمابر یواس‌اس جورج اچ. دبلیو. بوش در حال انجام عملیات پروازی در حین عبور از دریای عرب هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67003" target="_blank">📅 19:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67002">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=bK-a46R9Q6s7RlVCZROL_Yiq7RnEDnYdWxT6AFdfLUvDEEewhKHodYDEshluser30l1ljsHicQ4ktkLXxZSVDSK7jk_viWJzTyuS8gH6ZV4XIZcTTSmU6Aq18ZsYLKblw3msF9w9BRLFSuR2f9oXqXLghbQxiK-Ic6SaDO3_Is5wRVkdTpVKdzIef4T5EfHJ3FQieDs82Dh0U7K6XC8V0R4opFi6Z6Gx57PsxLOndn6TKDI054SstdjgsflcSlsAw7PGRYJklYH_L1mctyxhraCaLPJ3cm1llFY64WmRiP52fejYf__ExcCvgY1VF6bPAdNuytQkfE5ZtqRcXnPQ0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=bK-a46R9Q6s7RlVCZROL_Yiq7RnEDnYdWxT6AFdfLUvDEEewhKHodYDEshluser30l1ljsHicQ4ktkLXxZSVDSK7jk_viWJzTyuS8gH6ZV4XIZcTTSmU6Aq18ZsYLKblw3msF9w9BRLFSuR2f9oXqXLghbQxiK-Ic6SaDO3_Is5wRVkdTpVKdzIef4T5EfHJ3FQieDs82Dh0U7K6XC8V0R4opFi6Z6Gx57PsxLOndn6TKDI054SstdjgsflcSlsAw7PGRYJklYH_L1mctyxhraCaLPJ3cm1llFY64WmRiP52fejYf__ExcCvgY1VF6bPAdNuytQkfE5ZtqRcXnPQ0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67002" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67001">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=n-s2ZaTTcw0jGOEYiH_lNUXLPyrwV6VgeR6CdAPIDb1QMsI7ubWwp8SNN7fRlJIvBEp62oWtFE5iy3N_vts5sD50vaE-f_YQ3RGLb2yPr8SdvyXG4q3vuITL0GvxPNFPGKnkCfJTnaFdqcyHLKd79AVCvMvvLePAGTO4YSUZiN_lV6GfdyhC2DtjG6-5d6EEuOne7loK-NTyVaupzqtKLKNqK8DoEUaFUBkvJNxjqU_ory0wLjRK3ViKNs9DLhSJmqxOmv035VMRW0Wxj1Lm7CxOCS72z0p6bb_vmE8PS_pHcpdaPVxDJxVvVNSmYkqbQnK7IIhHmsJEOE0CQYooQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=n-s2ZaTTcw0jGOEYiH_lNUXLPyrwV6VgeR6CdAPIDb1QMsI7ubWwp8SNN7fRlJIvBEp62oWtFE5iy3N_vts5sD50vaE-f_YQ3RGLb2yPr8SdvyXG4q3vuITL0GvxPNFPGKnkCfJTnaFdqcyHLKd79AVCvMvvLePAGTO4YSUZiN_lV6GfdyhC2DtjG6-5d6EEuOne7loK-NTyVaupzqtKLKNqK8DoEUaFUBkvJNxjqU_ory0wLjRK3ViKNs9DLhSJmqxOmv035VMRW0Wxj1Lm7CxOCS72z0p6bb_vmE8PS_pHcpdaPVxDJxVvVNSmYkqbQnK7IIhHmsJEOE0CQYooQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67001" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67000">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMrLomla4bGNRe6pcCjiTL44nKHwtBDRwtMvBCKc2SsudjsTjt_UJV16DGi5mXUffkVtU3u27ufJU8Y2faJ5r1VskvARRITRfqo5aLo4-6eEcstnny3GnWzUS2Gp3c7Xj1Bz8Fx3v4yMdLPH-ysAsYjSnbFShWDSD_LsoZNaQj2gxgHvIY2RGWsJL3RnwTQOTkNR8TsJUq9sveEMrTLPqUuadmBN7Jtpc-5UgH5g2A_d4t9irRrJbRTkrZ5rjWQ1QhMIT9jpMk2E9MqLuDPYwpgCU4JeaDmNR1th4graap7YFL_QpSRAmaie3OjBhmDZW6nN_VvsEfFh998IYnXwxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی کمیسیون امنیت ملی مجلس:
پول‌های مسدودشده مردم در بانک‌های داخلی را آزاد کنید، خارجی پیشکش.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67000" target="_blank">📅 17:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66999">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=pxjLE80OJb0lA5F4nALVmoz6Gop0dvFoBiWlpEFA8SDC41Vtr4a8wiouMHZ9ZvEhCWeRll9RB2Z94zQ33oRSG8NgPShNUHIB97UehV2qjJbqW94GPO2ZTlAArmebAi9AbyQgBoLhy5I7Ymn2ake9X6EWirVmtzzCCcwea6CaQWEB4cqW1DmXKptjYAN9XugPxQYktCXt8EBOnogXpX8g_5dsB7D3j4uaNxhP0kj3S9fD2k7T-Pb0oASnkZdF7EYNhFYDePXdPZT6QAcxieMDFxmhviYKy2-jp8asc644b7smPvWrSR1BK1F5M6HXFAl_q39m2D2OHN71Mi40Wy_Fbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=pxjLE80OJb0lA5F4nALVmoz6Gop0dvFoBiWlpEFA8SDC41Vtr4a8wiouMHZ9ZvEhCWeRll9RB2Z94zQ33oRSG8NgPShNUHIB97UehV2qjJbqW94GPO2ZTlAArmebAi9AbyQgBoLhy5I7Ymn2ake9X6EWirVmtzzCCcwea6CaQWEB4cqW1DmXKptjYAN9XugPxQYktCXt8EBOnogXpX8g_5dsB7D3j4uaNxhP0kj3S9fD2k7T-Pb0oASnkZdF7EYNhFYDePXdPZT6QAcxieMDFxmhviYKy2-jp8asc644b7smPvWrSR1BK1F5M6HXFAl_q39m2D2OHN71Mi40Wy_Fbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عراقچی:«بر اساس تفاهم‌نامه، تنگه هرمز ظرف ۳۰ روز و تحت سازوکار مدیریتی مورد تصویب ایران، پس از رفع موانع از سوی جمهوری اسلامی ایران، به ظرفیت عملیاتی پیش از جنگ بازخواهد گشت.
🔴
این ترتیبات هم‌اکنون در حال اجراست و مسئولیت کامل آن صرفاً بر عهده جمهوری اسلامی ایران است. هیچ نهاد یا کشور دیگری در این زمینه مسئولیتی ندارد.
🔴
مطابق تفاهم‌نامه امضاشده میان ایران و ایالات متحده، هرگونه مداخله در این موضوع یا هرگونه تلاش برای ایجاد سازوکارهای جدید یا جداگانه، غیر از ترتیباتی که اکنون از سوی جمهوری اسلامی ایران در حال اجراست، تنها موجب پیچیده‌تر شدن وضعیت، به تأخیر افتادن بازگشایی تنگه هرمز و افزایش تنش‌ها خواهد شد.
🔴
همان‌گونه که طی دو شب گذشته شاهد بودیم، رخدادهای تنگه هرمز از پیش به افزایش تنش‌ها و رویارویی‌ها دامن زده است.
🔴
از همه طرف‌ها می‌خواهم در مدیریت تنگه هرمز یا در ترتیباتی که جمهوری اسلامی ایران برای بازگشایی آن در حال اجرا دارد، مداخله نکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66999" target="_blank">📅 17:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66998">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=IthUHxnRAStmPpTDAbO_ndjt6vfff4u92hCsLPcZOkqTsOGe-Y0JqEcJUI701BDXc7AbB5kfjVfSqsVDMGuqmOlI1O6cWBktfZ4KxA8cTC8WnKsGNM1VDeF4P_0u73NOFGC1IR-Brp6RPeO0cpE-4NKXHtw2gUU_wxbUoesMF6hRtPYlS1rgxSVAblaEVi8eYagXP7iFlrq2tRn_eFO1joxlmU2JiPO9nbfWZmFLzpoy_pGUSxf3tHqAVVUFJG0ATt_fS9ETvgNaf0kNU68KBO_3rUxb-pge2AUaD5r-XnT_Z7700vWaMRXc8_ZYodA3X6JjhVE4F6urWIsigGCYHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=IthUHxnRAStmPpTDAbO_ndjt6vfff4u92hCsLPcZOkqTsOGe-Y0JqEcJUI701BDXc7AbB5kfjVfSqsVDMGuqmOlI1O6cWBktfZ4KxA8cTC8WnKsGNM1VDeF4P_0u73NOFGC1IR-Brp6RPeO0cpE-4NKXHtw2gUU_wxbUoesMF6hRtPYlS1rgxSVAblaEVi8eYagXP7iFlrq2tRn_eFO1joxlmU2JiPO9nbfWZmFLzpoy_pGUSxf3tHqAVVUFJG0ATt_fS9ETvgNaf0kNU68KBO_3rUxb-pge2AUaD5r-XnT_Z7700vWaMRXc8_ZYodA3X6JjhVE4F6urWIsigGCYHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو:
می‌خواهم به شما یادآوری کنم که در لبنان چه بود. حزب‌الله ۱۵۰٬۰۰۰ موشک و راکت داشت. و ما حدود ۹۰٪ از این انبار عظیم را از بین بردیم.
ما آنها را با بیپرها شوکه کردیم، نصرالله را از بین بردیم، فرماندهان نیروی رضوان را کشتیم.
فقط در دو هفته گذشته بیش از ۲۰۰ تروریست را کشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66998" target="_blank">📅 16:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66993">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VrZbn4P4iXh4PpHzy2xDuOa48VNJGPEYq_vIQOJ1q3QurHwwtRb5vq-IJTJQxvxEH0WuT4xO8v4SSXb2C3X22M_1UmUsvWZQUK2a1ERMLEqxPIijT-SHi24MVGQMRGjcdRt1OSmZiAbYE3zUIdRTXCVMJFGfqNRRKIC2gLL1T5ui6mjg6pjZGBHDwa8rB78DxMbuisXOqGlyIIc2G9ttAzTvnDU0eh9QL2vu0GzKUcDhZEe1eTyjRD3pak58GuDVeUoxRJjOZw6owRfZtCMxwFAEY-1DbeHPctzNlwKtYaWJ3_Qrntl8ovjrB_H5IZBvNJOXfLWEwi3VigCLsN8YIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rKVDa8TbGErMp5JMttccw2couXx9sMjxtOCMCLSXfx6JoQZiafYMmQIhlEcbauB1u9VlyOAsVxiAg4MCd16ckdOSJC29LFA3PynshhUfl5dd9Ziu1GLpnxq_t7Y6LHdeVBebIDFyShPI6MUSHKdwU80wq3K0f0r9bQxLNxzc0DvFlBR8Y1ZW0W3i_a8bs25fR4pJniCaUc0v4ZihOtRC_RaluwFsicz-4INeboj4Bx4xH-_41sPA--GLgbelxr5PCZVM6wQudso_NihJDHBps9gtsQ67xHyLS9GvacL5T_b-XAcgOHNUD7jtMzS47TcOYCj-FdYKHudwTTA7c1m9JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k593tvdTHLQGi2MZ9PuchF05QO7Ks1ruHNYI5c6227Ty1AXDx5Au48VjEfDDl1xMZDO6ZZxJrTFuxb8Tn3lF2kpt7SQn_3pgQFk7YRAxBH8OqKtYo1OKygQ5o9lOwixCe7BmRLovjpQ3UFqhDW3Nr3CUwoOrLVNiV_40SMeIMZOB8lHOJ7-N3uljgx2vfUDeMZW8O1AiDtf-_GsSf5MOqVYR3DD-zyzJXXENadxTT2Cu9hRgCqjpATH5gzCEv8RJwyjIN1uYqJLS6O6tNBvYrY_EW01emrNh3ZOr2iviN4mIrDdASAucU-GAOIgfi65fzs0OD_0b4oBxaqMS2DFM4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=v6h_o0_0fpy-mRDLl4Xrbj50VLIhzhkF8B4U-jXIfzw1kg_mY-6-UoMsOyrTmMnclK3CJRgR6RvBmH5eNPSnQcH2xfvdXmRlqEganKTvnJj-q5DsID7LOvRtJ8LWundtY5U_jwAchrUQnotmVRikZ4E7gnZDjhJCZ2XfeRKJMbF1m7cJhC-zfmKWBK8XFPsDCkdA0eAA5GZxUy8mrQIezv2qOQTA_UWDqHVQJfW2kitKIGH7CggZQldc6xDWE7yQn-0v0Zgn0zZqXqG_Jz5672fDPyX8AFzhTDdz9X_zZUixNAE1YiIX1zA8X9qV6-VGoBIbYbH04UJ4RUqR7XMOBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=v6h_o0_0fpy-mRDLl4Xrbj50VLIhzhkF8B4U-jXIfzw1kg_mY-6-UoMsOyrTmMnclK3CJRgR6RvBmH5eNPSnQcH2xfvdXmRlqEganKTvnJj-q5DsID7LOvRtJ8LWundtY5U_jwAchrUQnotmVRikZ4E7gnZDjhJCZ2XfeRKJMbF1m7cJhC-zfmKWBK8XFPsDCkdA0eAA5GZxUy8mrQIezv2qOQTA_UWDqHVQJfW2kitKIGH7CggZQldc6xDWE7yQn-0v0Zgn0zZqXqG_Jz5672fDPyX8AFzhTDdz9X_zZUixNAE1YiIX1zA8X9qV6-VGoBIbYbH04UJ4RUqR7XMOBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیاین یه نگاهی بندازیم ببینیم چه بلایی سر تیم به‌ظاهر ملی اومد؛ قبلش بریم سراغ مصاحبه های بازیکنان این تیم تو تجمعات شبانه حکومتی‌ها:
شجاع خلیل زاده :
حسم نسبت به رهبر شهید ؟ افتخار ایران ؛ گل اگه زدم به رهبر و شهدا تقدیم میکنم
رهبر عزیزمون شهید شد همون چیزی که خودش میخواست بهش رسید
گل بزنم به  رهبر شهیدم تقدیم میکنم و ما فوتبالیست ها همه دوستش داشتیم ، افتخار نداشتم با رهبر دیدار داشته باشم و دوستش دارم
حسین کنعانی :
حسم نسبت به سید مجید نقطه زن ؟ بزن که خوب میزنی ،حسم نسبت به رهبر ؟ بزرگی
رامین رضاییان :
شهادت رهبر انقلاب رو تسلیت میگم تو تیم ملی به عنوان سرباز برای کشورم می جنگم
اتفاقات داخل ایران { دی ماه } به خودمون ربط داره و به خارجیا ربطی نداره
علیرضا بیرانوند:
چه بهتر که تو آمریکا بازی کنیم می‌تونیم تو اون کشور برای اولین بار در تاریخ فوتبال کشورمون به دور بعد جام  جهانی صعود کنیم
روزبه چشمی :
حسم به رهبر شهید ؟ بزرگ همه مردم ایران !
سعادت دیدار با رهبر عزیزمون نداشتیم ولی بزرگ همه مردم بودن و این راهی که مردم دارن میرن ادامه راه ایشونه
و بعد از این اظهار نظر ها بریم سراغ دیدن نتایج، تو بازی اول از ضعیف ترین تیم جام یعنی نیوزیلند دوبار عقب افتادن و در نهایت با سختی یک امتیاز کسب کردند، تو بازی دوم فقط چند سانتی‌متر از باسن مهدی طارمی تو آفساید بود و گلش مقابل بلژیک مردود شد، تو بازی سوم بازم همون طارمی پنالتی رو خراب کرد و در دقیقه ۹۳ شجاع خلیل‌زاده گل زد و خوشحالی‌ای کرد که در تمام جهان سوژه شد، ولی بعد از چند ثانیه کل دنیا روی سرش خراب شد چون فقط دستش ۵ سانتی‌متر تو آفساید بود، نکته جالب اینه که شجاع گفته بود گلم رو تقدیم به رهبر جمهوری اسلامی خواهم کرد
دقت کنید برای اولین بار در تاریخ این جام جهانی ۴۸ تیمی بود و ۳۲ تیم صعود می‌کنند، یعنی در واقع به اندازه‌ی همه‌ی تیم های حاضر در جام های جهانی قبلی، این بار تیم‌ها به دور بعد صعود می‌کردند (علاوه بر تیم های اول و دوم، هشت تیم سوم هم صعود می‌کنه) و بعد از مساوی با مصر، سه شرط برای صعود تیم به‌ظاهر ملی وجود داشت:
۱.بردغنا
۲.نباختن ازبکستان
۳.مساوی نشدن بازی الجزایر و اتریش
ولی در کمال تعجب یک معجزه رخ داد، غنا نبرد، ازبکستان باخت، و در دقیقه ۹۴ بازی الجزایر، ج.ا صعود کرد و در دقیقه ۹۵ با گل اتریش، ج.ا حذف شد، این واقعا یکی از بزرگترین تحقیر های تاریخ بود
...
می‌بینم یک سری افراد با توجیه های احمقانه می‌گن اینا مجبورن و فلان، نه عزیزان دارین اشباه می‌کنید، میانگین سنی این بازیکنا بالای سی ساله و عملا فوتبالشون تموم شده و رسیدن به آخر خط، اینا فقط دنبال باج حکومتی‌ان و حکومت به عنوان حق‌السکوت بهشون مجوز واردات خودروی لوکس می‌ده که می‌تونن ۱۰۰ میلیارد ازش سود کنن، یعنی عملا یک رانت ۵۷۰ هزار دلاری هر شخص بابت حق‌السکوت دریافت می‌کنه، جالبه که تیم های بزرگ جهان مثل آلمان و اسپانیا حتی اگه تیمشون قهرمان هم بشه مبلغ کمتری رو می‌دن به بازیکنا (۴۳۰ هزار دلار)، خلاصه که جام جهانی بزرگترین رویداد برای شنیدن صدای مردم مظلومه، همونطور که تو سال ۱۹۷۸ کاراسکوسا کاپیتان آرژانتین بخاطر جنایت های حکومتش از تیم ملی استعفا داد و...
ودرآخر، از اون ضربه‌ی تیر دقیقه ی ۱۲۰ جهانبخش تو جام ملت ها، تا پنالتی‌ای که طارمی خراب، تا پنج سانتی که شجاع تو آفساید بود، از پنج سانتی که بازیکن کنگو جلو ازبکستان تو آفساید نبود، از پرچم کرنر تو بازی الجزایر، از گل دقیقه ۹۴ الجزایر تا گل دقیقه ۹۵ اتریش، هیچکدوم اتفاقی نبود و همشون کارما بود، کارمای حرفایی که نباید می‌زدین و زدین، کارمای کارایی که نباید می‌کردین و کردین، اینا همه صداهای مردم و آه‌ناله هاشون تو گوشتونه، مردمی که دلشون باهاتون صاف نیست، حالا هی بیاین بگید تبانی بود، نه تبانی نبود، اون بالاسری خواست تا شما به عنوان بی‌غیرت ترین و بی‌شرف ترین نسل تاریخ ایران با حقارت‌آمیز ترین نحوه‌ی تاریخ از جام جهانی حذف بشید :)
#hjAly‌
@HutNewsPlus
|
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66993" target="_blank">📅 16:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66992">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPll58Id-6pK8uRGP9GWxniyNn-Mn_QMJLkExekwz2eGr_txVIGkKjzZDbwMC2F8mqR3xUNMb8HAFIHsIWVBLHR5uupL3IMM36vW3lAnUrEISyTeTz9hMB5n2WvKopqOoCl_w4V8eFw8jDc_hJGnn8O93aKb9gEsAvfXxbItIoeneH98gbfZklsgYCCI42nu3T_Z3dQFdslZVwXaKJTdfNuzdOOVhuWNgmZLLzoEuXlrZLcn5rZkIXWMH-YPBcMLAUonsQhvnXZ_hYrKSqAN6Jcy4U_4DuA859F6rACgzQJ8VmrwnoQnM8rf_iHAxy4cR0-mrbKRo62SHD2q6R_bZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواداران حزب‌الله دیشب تابلوهای «لبنان اول» را در جاده منتهی به فرودگاه بیروت به آتش کشیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66992" target="_blank">📅 16:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66991">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHossein ️</strong></div>
<div class="tg-text">🇨🇭
ایران - سوئیس
🇮🇷
مرحله حذفی یک شانزدهم جام جهانی
سشنبه ساعت ۲۰:۳۰
محل بازی : گیم نت محلمون در بازی اف سی۲۶</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66991" target="_blank">📅 15:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66990">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
هنوز تیم جمهوری اسلامی صد در صد حذف نشده
:
تیم های اتریش و الجزیره الان تو امریکا هستند و باید برن کانادا. طبق براورد، احتمال سقوط یک هواپیما 0.00004 درصده که اگر اتفاق بی افته ایران جایگزین می‌شه. یعنی همین درصد ایران شانس صعود داره
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66990" target="_blank">📅 15:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66989">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572c331047.mp4?token=lrgwudsvmCu1bcc5b-MUOPcsXfxLOX5JKGYDAfmjWwiI8P7QUjEmMd44qIgY5TEmuptERq5zEHW6DrAGUOY8OHj8-27yIf5a2CkulrtUdBxZnfkZs6RPknCWLwe0gqPyy1VkZoegCwv8-OlL9vWj8Vn6O4LnUri8US6vCPZSFbckoNeyHEl4h7bCqMZ4E-T0N-EfsRbJPCOxeYdTsPDqTEmC9YoteemG9y_9JB4K05kyOInK6Gk1Mt1Z9dCe-NiI7Ri8ojHsswE7LJ9urCZ8K7UbKqeTlYrVL6yLEM9y4_KmpGOXC7J2kM97daJKXyGnBOQXXDQWtdeHUgQbfINq0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572c331047.mp4?token=lrgwudsvmCu1bcc5b-MUOPcsXfxLOX5JKGYDAfmjWwiI8P7QUjEmMd44qIgY5TEmuptERq5zEHW6DrAGUOY8OHj8-27yIf5a2CkulrtUdBxZnfkZs6RPknCWLwe0gqPyy1VkZoegCwv8-OlL9vWj8Vn6O4LnUri8US6vCPZSFbckoNeyHEl4h7bCqMZ4E-T0N-EfsRbJPCOxeYdTsPDqTEmC9YoteemG9y_9JB4K05kyOInK6Gk1Mt1Z9dCe-NiI7Ri8ojHsswE7LJ9urCZ8K7UbKqeTlYrVL6yLEM9y4_KmpGOXC7J2kM97daJKXyGnBOQXXDQWtdeHUgQbfINq0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66989" target="_blank">📅 14:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66988">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74845b1c1.mp4?token=aGGsFEV5V6KESdyphQMbm7sqfb3m78uIO18ZIYglyNViThbRaWDWKFq0IYq1XiA1XmxTMI3oy6upCje170AdLTx3bNTHOzVB0NMiWTVLEk7TJ2NE-RSB5q3AJWVgnzGpS6fK1FfZjPMy00rb2DsCCeYowOMxWYHo3Xe-dG7Kfr_KFXRnihBfeZpsziXojM49t_0k4k7XhH1PQtfYhU3fRLTOBsqD8SmKFvCMw8famOI_v2IQxS1jFeoJLKWY9Q5v3_VlmMKVTlOIE4tJ6h-2791xtqOb_kLu9D-krAO9Zi0qLxddQJBnusmFB31pKyEpB2-Nnk7PIgSCSVTo4A5T0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74845b1c1.mp4?token=aGGsFEV5V6KESdyphQMbm7sqfb3m78uIO18ZIYglyNViThbRaWDWKFq0IYq1XiA1XmxTMI3oy6upCje170AdLTx3bNTHOzVB0NMiWTVLEk7TJ2NE-RSB5q3AJWVgnzGpS6fK1FfZjPMy00rb2DsCCeYowOMxWYHo3Xe-dG7Kfr_KFXRnihBfeZpsziXojM49t_0k4k7XhH1PQtfYhU3fRLTOBsqD8SmKFvCMw8famOI_v2IQxS1jFeoJLKWY9Q5v3_VlmMKVTlOIE4tJ6h-2791xtqOb_kLu9D-krAO9Zi0qLxddQJBnusmFB31pKyEpB2-Nnk7PIgSCSVTo4A5T0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی دیشب:
ایران با این احتمالات قطعا صعود میکنه اگه هر ۳ تا بازی طوری رقم بخوره که ایران حذف بشه؛
فقط معنیش اینه که خدا خواسته این تیمو بزنه و تنبیه کنه
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66988" target="_blank">📅 14:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66987">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=tQFjHGPC2EdG6G2D1y02qkBUa4rxN4u1fUrhxOp2-7QiDm3nJDN3ZwldG96eo-JRUfRGJX1Olq2_nPrBREZi2zs6IS0HrfrJKHcf9E4pSiA0LNs-yti6DcGALYQgR-xogkopr1xcZ5fZrJT_8itCw4HbUUSiSzyC7AXCIow0tMJ4iF5qQSdJt66WGm1fWBT31IjA005N-_p8mH_2yOXY_HxKD3Fjv6LyScca7eeTfxExkzO6ChkY5kU5DhA_vMbkmcc9sJiwLuCLxJ_08TFNFQk4yhfDhUZTtjmlFPEKrK_4wReoGDzctOHcJU9w5l5xsRz0sV0bFpS5qv5C1GyjVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=tQFjHGPC2EdG6G2D1y02qkBUa4rxN4u1fUrhxOp2-7QiDm3nJDN3ZwldG96eo-JRUfRGJX1Olq2_nPrBREZi2zs6IS0HrfrJKHcf9E4pSiA0LNs-yti6DcGALYQgR-xogkopr1xcZ5fZrJT_8itCw4HbUUSiSzyC7AXCIow0tMJ4iF5qQSdJt66WGm1fWBT31IjA005N-_p8mH_2yOXY_HxKD3Fjv6LyScca7eeTfxExkzO6ChkY5kU5DhA_vMbkmcc9sJiwLuCLxJ_08TFNFQk4yhfDhUZTtjmlFPEKrK_4wReoGDzctOHcJU9w5l5xsRz0sV0bFpS5qv5C1GyjVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی سپاه پاسداران:
«از اینکه دولت به سپاه نفت داده باشد، اطلاعی ندارم و بعید می دانم چنین موضوعی صحت داشته باشد.» او اضافه کرد: «سپاه برای تجهیز و پشتیبانی از یگان های مختلف خود به بودجه نیاز دارد و دولت موظف است این بودجه را تامین کند.»
مسعود پزشکیان، اخیرا در یک سخنرانی گفت: «اگر ما پشتیبانی نمی کردیم، رزمندگان نمی توانستند بجنگند و ما 20 میلیون بشکه نفتی که به دولت تعلق داشت، به هوافضای سپاه دادیم».
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66987" target="_blank">📅 13:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66986">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=Aq4PbGKdLosS_ldor_OQmXL2zxBaGr-uoZ8GiAWVFQsQaNz-o4Pxq6KkbgW80uRyJkd4NMtlMGRB_xncD6IR2uv3EwD3aHJteLKhOBqUOXGI3kSZlBmHFMpW-FiCzoKX_1N_-mTgiawEw2E1YlhmmCUXeD0yGvgETSwuuowffgoWVTrfMg_0Kfi9-Mvb2-wGFGYEPgyZU330dW74M4stLSq0DYkEojc2HcDZ7RKTL8WUKe0_gP_0me7GjYdQpQwPCFt43tTUUgTHwqI4Vex6w87JcYmh5bY_frQlbUyf5dNOJ6heQp65liFp6Q_2Wk5_b6hVA8agWHjM0nU5JbRY_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=Aq4PbGKdLosS_ldor_OQmXL2zxBaGr-uoZ8GiAWVFQsQaNz-o4Pxq6KkbgW80uRyJkd4NMtlMGRB_xncD6IR2uv3EwD3aHJteLKhOBqUOXGI3kSZlBmHFMpW-FiCzoKX_1N_-mTgiawEw2E1YlhmmCUXeD0yGvgETSwuuowffgoWVTrfMg_0Kfi9-Mvb2-wGFGYEPgyZU330dW74M4stLSq0DYkEojc2HcDZ7RKTL8WUKe0_gP_0me7GjYdQpQwPCFt43tTUUgTHwqI4Vex6w87JcYmh5bY_frQlbUyf5dNOJ6heQp65liFp6Q_2Wk5_b6hVA8agWHjM0nU5JbRY_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری از حملات اوکراین به پالایشگاه یاروسلاول در روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66986" target="_blank">📅 12:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66985">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFVetWdQbDBT4hpHsjWxWkYtVWsjVedwuRR8ncmamRkOtBvsiQXut1ZNM_aWxgbqz9baL8zWDbbRXj0G4-qc9bBn8TsrIb2_CDjAFZiooO41N_zEpfbgv-toUSvgP2hxa7K0Kw4L_-sWUo_LamnRrZlQRJIrwlszj6lxNPGxKhrS7urtKD7R2piOjlm5rUhuhQsOWrLrLWmL67PqSnLZs0gjE1WEjUjFBjO6AAb378GYeKGFKHyauMXbUxwbQZrc01V5iw4I6JvF0TpNs-UAyvD9Cm8ctTI1AA8Nc12L6FZqDsSVbM2tFJXobqQEfaQKy6pnlFyk9L9KKy1PO4ZxDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
وزارت خارجه جمهوری اسلامی در بیانیه ای حملات هوایی آمریکا به مناطقی در سواحل جنوبی ایران را به شدت محکوم کرد و آن را نقض آشکار منشور سازمان ملل و نقض صریح بند اول یادداشت تفاهم با آمریکا دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66985" target="_blank">📅 12:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66984">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‼️
کارشناس برنامه دیالوگ:
این جنگ به مسئولین نظامی و سیاسی نشون داد که توانایی نابودی اسرائیل رو ندارند و چشمشون به واقعیت های میدان بیشتر باز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66984" target="_blank">📅 12:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66983">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8hm3wO-a1eSxi7lfmqHMuVd9PaJt8u-AcpQpmUP6Egc6QGGj14eSSN8zgJ8P-aeWrJhVH2jUFDsknwPClVni4JGmvxfCtuvq760N6PgQY10Vm9tUtD-K3wTV6jgqzcMDdUPoQrEbl8Y3ATwuFGGZE3XiQX8TZRPus9KvDOmOCoufsIZ_VjdQmxjvMew2BQceUg3Dy4Ft--9tQIA1yBFJghuj4Sa3Okw2L7okXkORL-hbt-hTVZ22sg4DUD5QIXRc2TmxuIVoIYN4k42PKrpFtiFAEnFs6VfC79MspIQJXu4p4gElm3nL7usimw3-UEZ7bAlTlQW6L0IJ83Qbb7O0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
۶۸,۹۰۰ نفر در ونزوئلا سه روز پس از دو زلزله کم‌عمق پشت سر هم (با بزرگای ۷.۲ و ۷.۵) که کشور را ویران کردند، به‌ویژه ایالت ساحلی لا گوارا، گم‌شده گزارش شدند.
۱,۴۳۰ کشته، تلفات در حال افزایش است.
نجات‌دهندگان با ماشین‌آلات و دست‌های برهنه در میان آوار جستجو می‌کنند؛ پنجره بقای ۴۸ تا ۷۲ ساعته در حال بسته شدن است.
گرما تجزیه را تسریع کرده است؛ شرایط بسیار وخیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66983" target="_blank">📅 11:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66982">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c0f8ca35e.mp4?token=G3DD7U1EFIHuefQpO8phpR8Vp571LAPZTGWEl2xGE8beGv9JzHxTA0hDV03mUW4oSWAipXfsBpNTL6372tEox_qWiFlis_wlFURPdt3rcmtTcTvuIDav3gfC0PN1HbMTeMnZSz9ZcIFr6heyRnLdlZan5lW6TyaaniRVrRHO3-JeRGf7XkD5YOOQ4vuhdJHxGlmeXX_RVT0WBb7Zb6rgYeU_nWIQOfhWmtF6q_GhDvibpWtewP1eSSq3QqKjPE10OII8d6E3NIvWfRjsyJmJN7XnrmOfTGrJsO1QwSasuDRVlxtvyf-H8IGLJ1r-58TGLos9CwjOaB1yUZ4WpqAX1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c0f8ca35e.mp4?token=G3DD7U1EFIHuefQpO8phpR8Vp571LAPZTGWEl2xGE8beGv9JzHxTA0hDV03mUW4oSWAipXfsBpNTL6372tEox_qWiFlis_wlFURPdt3rcmtTcTvuIDav3gfC0PN1HbMTeMnZSz9ZcIFr6heyRnLdlZan5lW6TyaaniRVrRHO3-JeRGf7XkD5YOOQ4vuhdJHxGlmeXX_RVT0WBb7Zb6rgYeU_nWIQOfhWmtF6q_GhDvibpWtewP1eSSq3QqKjPE10OII8d6E3NIvWfRjsyJmJN7XnrmOfTGrJsO1QwSasuDRVlxtvyf-H8IGLJ1r-58TGLos9CwjOaB1yUZ4WpqAX1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
سعید لیلاز: فکر می‌کنم آمریکا در بهمن یا اسفند دوباره به ایران حمله می‌کند، تفاهم‌نامه یک وقفه است
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66982" target="_blank">📅 11:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66981">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‼️
گزارشگر صداوسیما وقتی گل سوم الجزایر زد
خدا صدای مردم ایران شنید
😂
خدا دقیقه ۹۵ و حتی یک دقیقه از بازی گذشته بود گل مساوی زد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66981" target="_blank">📅 10:49 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
