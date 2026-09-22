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
<img src="https://cdn4.telesco.pe/file/lrwVBpeIKeEicp3YX4wDP_i2gOYKbdoo_gXW89bHRZgskEmRVv7AfJ6DP6G2vN5HoQfO_Ybb39DOrNXXtUovlmlAILJcUchy8VeJ_iN_YysOEfLk1GZTQADXow2eMs-A2NZ9Pf77nggC2ENZpHwmKK1NXmvAaISnd5yaCzqDZbceC4AyG-JqSamQmq4P9_2i3WtZ74ZSIFd4ZboorUEr5g1JuAEuYlnkwiy-xSkCe9dQLG0GBXGCZvE8fjG_PiZWWFjf1MFg7NDQwpNP9KAuw0IoZmblBP6ECVTQsCQDRRH_Mmolzzhqk3zbMdmVI-uzEubEF1qxKQD3NOKzTRNANA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 106K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 18:34:28</div>
<hr>

<div class="tg-post" id="msg-72060">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/156037c15c.mp4?token=l3wYiHvpfgGCrLBm1NnHwWiTlDAh0Z3x71l5EpIah1l3Hlvo6vo2Zg1LQVveU2Hx69bvPOVQN2m-nDEScw7P4qKJ0hFBVB3lJ8TL44ISOaUN5bZbNHeJrj08LCvOfK4esSYsNMVRQO6MpOiuPf37KNw4U1AczwjXjeajLFq0GFOcFurnYHsmCPmO-tYGLbOKSaBB2sRuID3ygQlU8RGZyZkHzDNcb4QOCkunXHUGdG0UuKLFK_mRsMAptq_Hymb9PWY7_MYoNfDrEmVmfXJzV0vkhk_wa_HvcO2u02S1BQs8rAtK6015m-nNcAPykKz-9dXuTfsWjX2X1aH1CpO4lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/156037c15c.mp4?token=l3wYiHvpfgGCrLBm1NnHwWiTlDAh0Z3x71l5EpIah1l3Hlvo6vo2Zg1LQVveU2Hx69bvPOVQN2m-nDEScw7P4qKJ0hFBVB3lJ8TL44ISOaUN5bZbNHeJrj08LCvOfK4esSYsNMVRQO6MpOiuPf37KNw4U1AczwjXjeajLFq0GFOcFurnYHsmCPmO-tYGLbOKSaBB2sRuID3ygQlU8RGZyZkHzDNcb4QOCkunXHUGdG0UuKLFK_mRsMAptq_Hymb9PWY7_MYoNfDrEmVmfXJzV0vkhk_wa_HvcO2u02S1BQs8rAtK6015m-nNcAPykKz-9dXuTfsWjX2X1aH1CpO4lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایران:
نیروی دریایی ایالات متحده اخیراً بیش از یک میلیارد بشکه نفت را از تنگه هرمز اسکورت و عبور داده است و حجم نفت در حال عبور، بیش از هر زمان دیگری از آغاز جنگ است.
ما هر روز و هر شب، به ترتیب ۲۲، ۲۵، ۳۰، ۳۲ و ۳۷ کشتی را [از این مسیر] عبور می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/news_hut/72060" target="_blank">📅 18:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72059">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=PuT3UTR-1IopihU3u7Qykuf8mQaIs8f6hALE8xfx7OWI_J7Z5e-lZVrVLYh25cTfFd_BYpYDzQwgfjyHpQVF3PC2xy3d_JtCTKAO3dkTSwqpoRdzQEKdmLVM6oST0R4QmRO_WEXsi8yvsD0wf5NYcWxU5WJ9Gd3e9Kahk3D5UjmLXbhtVAq69Zg_J7j1XtsfORbdkC9Wb02SdtoM7oYOnDp_oCtG_RLr7a2hklVotw7NvIiO5JoQWODY10JCL4BQcQtiW6u8CJErCMDdAUibevXBwqrdKVrtocDLO5Jyax8JC9A5_Ruya_K96W708CL629ds6NZ3eJPrUW98FF5XtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=PuT3UTR-1IopihU3u7Qykuf8mQaIs8f6hALE8xfx7OWI_J7Z5e-lZVrVLYh25cTfFd_BYpYDzQwgfjyHpQVF3PC2xy3d_JtCTKAO3dkTSwqpoRdzQEKdmLVM6oST0R4QmRO_WEXsi8yvsD0wf5NYcWxU5WJ9Gd3e9Kahk3D5UjmLXbhtVAq69Zg_J7j1XtsfORbdkC9Wb02SdtoM7oYOnDp_oCtG_RLr7a2hklVotw7NvIiO5JoQWODY10JCL4BQcQtiW6u8CJErCMDdAUibevXBwqrdKVrtocDLO5Jyax8JC9A5_Ruya_K96W708CL629ds6NZ3eJPrUW98FF5XtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ایالات متحده و ایران قطعاً این کار را به سرانجام خواهند رساند. ما به هر طریقی که شده، این کار را انجام خواهیم داد. این کار انجام خواهد شد.
این کار به‌سرعت انجام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/news_hut/72059" target="_blank">📅 18:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72058">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e9a7cd318.mp4?token=L2DVCunqOUlb6b7W3QWqgTajUlht3wlzELbOuDWl2TmVyGMFW3rYi4ux4b1eG2ZZaiifnZYuqg9NWVySnsNjoVbuHJaIOJN0ZLe4EAKZVU0h-QuNpoiFre_9SZ7nLh-7ppSRM5Eglrc6yQPNlfvMlH1ZRvjtGVzCAHqCNEN3veHOggMrvo65XKVqhZV33oKsl0nR7joiTqfyOf74XbXp_h0ggiJuXP8nfeIORh7gE-bBerbgT9GN2xUASvKh94bpIXvkt_Wiq2XssQBUFneHDr58UQJm6WSlE5p9-mBTP2I7QoJg41qnbX8l-1WjmE8Rb1kVkOw8VNMyS6cGViF2B4mCKj3CuUE2fcJP1OjtXlq76xT1T7n3a3zZM2tUxDMttrdSr4qWqFg9P6XnJBmZ3tIsA6jOWOoctFO1UTA67WVtPmRzjo5e_BxxVF_sdeBD7OxGtqr3ZDtHxh9MCsiGzXkW386ScRoTU4fXujlHjcPnRFaegks-vyZ1wTB8KVJ3e5aK8I0g2XJ_eUNjIjLw8gQdGCauUoLJaHxQ24fApFtVvrptx9tmTaymt5vH6E_Gch5KaqtGjQ4TENBMhlZLgM5ldmw0DsDFgdJPIUz85qxJF2llxgjqsnSKW63GJUfsDX0S3-4nESxqpFrY9KkGTXfHvVe_CUxcf0CsaxdufVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e9a7cd318.mp4?token=L2DVCunqOUlb6b7W3QWqgTajUlht3wlzELbOuDWl2TmVyGMFW3rYi4ux4b1eG2ZZaiifnZYuqg9NWVySnsNjoVbuHJaIOJN0ZLe4EAKZVU0h-QuNpoiFre_9SZ7nLh-7ppSRM5Eglrc6yQPNlfvMlH1ZRvjtGVzCAHqCNEN3veHOggMrvo65XKVqhZV33oKsl0nR7joiTqfyOf74XbXp_h0ggiJuXP8nfeIORh7gE-bBerbgT9GN2xUASvKh94bpIXvkt_Wiq2XssQBUFneHDr58UQJm6WSlE5p9-mBTP2I7QoJg41qnbX8l-1WjmE8Rb1kVkOw8VNMyS6cGViF2B4mCKj3CuUE2fcJP1OjtXlq76xT1T7n3a3zZM2tUxDMttrdSr4qWqFg9P6XnJBmZ3tIsA6jOWOoctFO1UTA67WVtPmRzjo5e_BxxVF_sdeBD7OxGtqr3ZDtHxh9MCsiGzXkW386ScRoTU4fXujlHjcPnRFaegks-vyZ1wTB8KVJ3e5aK8I0g2XJ_eUNjIjLw8gQdGCauUoLJaHxQ24fApFtVvrptx9tmTaymt5vH6E_Gch5KaqtGjQ4TENBMhlZLgM5ldmw0DsDFgdJPIUz85qxJF2llxgjqsnSKW63GJUfsDX0S3-4nESxqpFrY9KkGTXfHvVe_CUxcf0CsaxdufVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
من از همه کشورها خواستم تا در اعمال
انزوای کامل اقتصادی ایران با ما همراه شوند؛ تا زمانی که آن‌ها حملات خود به کشتی‌های تجاری را متوقف کنند، از جاه‌طلبی‌های هسته‌ای خود دست بردارند و به حمایت از تروریسم پایان دهند.
این رژیم تروریستی نه به این دلیل که قدرتمند و با اعتمادبه‌نفس است، بلکه به این خاطر که ضعیف و درمانده است، چنین رفتار نامناسبی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/news_hut/72058" target="_blank">📅 18:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72057">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/415b898f05.mp4?token=vNdlcEKQR-MyUhSXBJKXaq0MOEgKdBUm25rH7RZ4RDhL4i1pcS9LrBOVw7rvWCjf4d8Vu2H42gajn8LjDJW2FGMyWIk6-fB3OT3OJuCAuk_c-qxjTdroVDz4yvseAfOas1hGaOXtdlxn7H91eIa4evTvD-dG0_88mc1BrvIZ65dlQaQ0mntCIXeM3StWM0g_XNVBRmGRboZTYfkWyn8gsomaHoIpxKy-mz5CK7WNCGVU5lf_oe43YsFgbgGjFyt-_sEHySHVQALeqL9Hw9C1zNYywtjrTLLQwCGvaoi75bNngWuPuYio04IFpQ3M1RoY6dwOyyZgpyw6G4eDu2bjhFq6ilvaN4B4LK-DAPDkD1fGYEGd59czXJH3jLK2qeTmdaqwrxD8Wo2h2L8mPk8GxuSgSMEZ-w_wEo5qgogMP2GV0StOoT7kVmiecSQkLWFcc67BS7KPfNFOWkg5w6Uti_-68SfDkZDp4j8ldGbd3kU76NaTAbJuoXWtVPlcjnSHktkf31xKEgQ0forjmRD0EfGAPK_4Au_HRkfofj1wiZzRZMnvmLnE8VHCHX2-pA-FTgweayYKD_RIgUeI1PKwxdtkSPfU7QFBSTQy4P8OCHJUzRRPE4qCfYGJSP3s1fzuialmx9Y8pscAligHAML_hW-2IdQcYMI9ktIpc407F1I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/415b898f05.mp4?token=vNdlcEKQR-MyUhSXBJKXaq0MOEgKdBUm25rH7RZ4RDhL4i1pcS9LrBOVw7rvWCjf4d8Vu2H42gajn8LjDJW2FGMyWIk6-fB3OT3OJuCAuk_c-qxjTdroVDz4yvseAfOas1hGaOXtdlxn7H91eIa4evTvD-dG0_88mc1BrvIZ65dlQaQ0mntCIXeM3StWM0g_XNVBRmGRboZTYfkWyn8gsomaHoIpxKy-mz5CK7WNCGVU5lf_oe43YsFgbgGjFyt-_sEHySHVQALeqL9Hw9C1zNYywtjrTLLQwCGvaoi75bNngWuPuYio04IFpQ3M1RoY6dwOyyZgpyw6G4eDu2bjhFq6ilvaN4B4LK-DAPDkD1fGYEGd59czXJH3jLK2qeTmdaqwrxD8Wo2h2L8mPk8GxuSgSMEZ-w_wEo5qgogMP2GV0StOoT7kVmiecSQkLWFcc67BS7KPfNFOWkg5w6Uti_-68SfDkZDp4j8ldGbd3kU76NaTAbJuoXWtVPlcjnSHktkf31xKEgQ0forjmRD0EfGAPK_4Au_HRkfofj1wiZzRZMnvmLnE8VHCHX2-pA-FTgweayYKD_RIgUeI1PKwxdtkSPfU7QFBSTQy4P8OCHJUzRRPE4qCfYGJSP3s1fzuialmx9Y8pscAligHAML_hW-2IdQcYMI9ktIpc407F1I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
بزدلان و خائنان بسیار دوست دارند بگویند که ذخایر مهمات ایالات متحده رو به اتمام است، اما این حرف صحت ندارد.
ما بیش از هر مقداری که حتی تصور استفاده از آن را داشته باشیم، مهمات در اختیار داریم و با سرعتی بی‌سابقه مشغول تولید آن‌ها هستیم. ما با سرعتی بیش از هر زمان دیگری در حال افزایش ذخایر خود هستیم؛ آن هم با تجهیزاتی که در بالاترین سطح کیفی قرار دارند.
علاوه بر این، در آینده‌ای بسیار نزدیک، کارخانه‌های عظیم تولید مهمات افتتاح خواهند شد. هم‌اکنون ۱۸ کارخانه از این دست توسط برترین شرکت‌های دفاعی جهان در حال ساخت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/news_hut/72057" target="_blank">📅 18:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72056">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=RMh8M1azmZg8m95SFfkIgaQQ8GGSm1nW_FKy0SENupU7kntd66Qgzow46KLD7uN0zKYlYPaCv0Ha0O9eLBhjYIi8qYviYA-TM659B-nAgnrs4RtDOUWoKmHbARId6nEeKFFoD9EIUUbJMy84E2gVWEYBF9ndBhceevSP0Q1LZf4h9juJtMOzfRikEbFUGUWnZVS9YMQLID3zLWiZR1ShKw4DxxvDuhHj2yFRpWleyHG_5YW74u0cPI97dcRvb7Qs_0m4Zvwr1fn1bq2M45FrdbBTneJ7mzauXa9LtYJ1pEtWHkie3ZN-ZAZO576QUySo-O9kMCmVW8yhnYpJ_In6SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=RMh8M1azmZg8m95SFfkIgaQQ8GGSm1nW_FKy0SENupU7kntd66Qgzow46KLD7uN0zKYlYPaCv0Ha0O9eLBhjYIi8qYviYA-TM659B-nAgnrs4RtDOUWoKmHbARId6nEeKFFoD9EIUUbJMy84E2gVWEYBF9ndBhceevSP0Q1LZf4h9juJtMOzfRikEbFUGUWnZVS9YMQLID3zLWiZR1ShKw4DxxvDuhHj2yFRpWleyHG_5YW74u0cPI97dcRvb7Qs_0m4Zvwr1fn1bq2M45FrdbBTneJ7mzauXa9LtYJ1pEtWHkie3ZN-ZAZO576QUySo-O9kMCmVW8yhnYpJ_In6SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
من برای انتخابات در مورد ایران مطلقاً هیچ اعتباری قائل نبوده‌ام و نخواهم بود؛ این موضوع حتی به ذهنم هم خطور نمی‌کند.
تنها چیزی که اهمیت دارد این است که ایران هرگز به سلاح هسته‌ای دست نخواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/news_hut/72056" target="_blank">📅 18:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72055">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">#فوری
؛پرزیدنت ترامپ درباره ایران:باید تصمیم بزرگی بگیرم.
آیا توافقی با ایران صورت خواهد گرفت که به آن‌ها اجازه دهد کشورشان را بازسازی کنند و کشوری بسیار بزرگ‌تر از آنچه پیش‌تر بود بسازند؛ شاید حتی یکی از بزرگ‌ترین کشورهای خاورمیانه یا حتی جهان؟
یا اینکه جمهوری اسلامی را نابود کنم—آن هم به سرعت—و هرگز به آن‌ها فرصتی ندهم که دوباره دست به کشتار و ویرانی مردم و کشورها بزنند؟
آیا آن‌ها را به جهنم بفرستم، بدون هیچ شانس بقا و بدون هیچ امیدی به عظمت در نسل‌های آینده؟
اما معتقدم که بلافاصله پس از انتخابات به توافق خواهیم رسید، چرا که تن ندادن به آن برایشان منطقی نیست.
آن‌ها منتظرند ببینند عملکرد من در انتخابات میان‌دوره‌ای چگونه خواهد بود. چیزی که متوجه نیستند این است که من اصلاً نامزد آن انتخابات نیستم. من آن کار را قبلاً انجام داده و با اکثریتی قاطع پیروز شده‌ام.
@News_Hut</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/news_hut/72055" target="_blank">📅 18:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72054">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5ddeee9dd.mp4?token=hfPPtnUsaVawchcPTM0EDqGxs1ek_-2vgyqWf8b3vWEleqwbiJ8RnH1EXLi2Z2EnssORr3PjYXejLq3rrRuAWZBAHKqadXhDEL9AXJ8P_tSU3ReFXQNPrAM7gx2hbq55YpY6pXtMLbVJlnsko_ywTPVphRHcJ4uvEmAsRQu8vQIhoakgx7_ta_IFf7RzZadMgHUmmPYx4v1Mqj5XnYoXXVZKbzNdXtAzTKJAjLB3--8QKP8bF2eofLx7DBIw6GcBMQS59feTd17GMMa10ORdCcYqUi_l2RAGqPOZs5Fxski2uboueJDDxHHyjRWmvvKzl6AllpYEshLTPVqfhHuuKycLmU5LsAL-G8gVkSYvQzit_DKAyI4vqFuYW9QABNA2Isbdw07VBmsQn96Yg6Zg1gU-jbpHF-uBzv50A5cIaK7-OJ45bFMLktdGmd9nZvjHEgOPvxx0bRjPeeEbP6gb9pZKOtKcRniU8XMroqZi2k7m2j9_dzvW-KGVasFc4E55SdKXK7YR6bBeTVEK3VR0mRJNAv4Qe-yaUgedaaMSdDgIJKmwovXV5z4JAvC5Vv9EiFOPDNQHiPM62EK5ybujtSAiSo1VbNWu3-uURODC3xUhWRLIoMwyTB_3GbONc58Bkp0Dcmwf5bS8oWFYus3rzBabbYlcFf7SJlyPj3eudxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5ddeee9dd.mp4?token=hfPPtnUsaVawchcPTM0EDqGxs1ek_-2vgyqWf8b3vWEleqwbiJ8RnH1EXLi2Z2EnssORr3PjYXejLq3rrRuAWZBAHKqadXhDEL9AXJ8P_tSU3ReFXQNPrAM7gx2hbq55YpY6pXtMLbVJlnsko_ywTPVphRHcJ4uvEmAsRQu8vQIhoakgx7_ta_IFf7RzZadMgHUmmPYx4v1Mqj5XnYoXXVZKbzNdXtAzTKJAjLB3--8QKP8bF2eofLx7DBIw6GcBMQS59feTd17GMMa10ORdCcYqUi_l2RAGqPOZs5Fxski2uboueJDDxHHyjRWmvvKzl6AllpYEshLTPVqfhHuuKycLmU5LsAL-G8gVkSYvQzit_DKAyI4vqFuYW9QABNA2Isbdw07VBmsQn96Yg6Zg1gU-jbpHF-uBzv50A5cIaK7-OJ45bFMLktdGmd9nZvjHEgOPvxx0bRjPeeEbP6gb9pZKOtKcRniU8XMroqZi2k7m2j9_dzvW-KGVasFc4E55SdKXK7YR6bBeTVEK3VR0mRJNAv4Qe-yaUgedaaMSdDgIJKmwovXV5z4JAvC5Vv9EiFOPDNQHiPM62EK5ybujtSAiSo1VbNWu3-uURODC3xUhWRLIoMwyTB_3GbONc58Bkp0Dcmwf5bS8oWFYus3rzBabbYlcFf7SJlyPj3eudxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
ما در آمریکا به‌تازگی بیست‌ و پنجمین سالگرد بدترین حمله تروریستی تاریخ، یعنی ۱۱ سپتامبر را پشت سر گذاشتیم؛ حمله‌ای که جان سه هزار نفر را گرفت. درست در همین نزدیکی‌ها.
دو هفته دیگر، سومین سالگرد حمله ۷ اکتبر در اسرائیل را گرامی خواهیم داشت؛ حمله‌ای که در آن تروریست‌های تحت حمایت مالی ایران، ۱۲۰۰ غیرنظامی کاملاً بی‌گناه — از جمله ده‌ها آمریکایی و بسیاری از نوزادان؛ نوزادانی کوچک، ظریف و زیبا — را شکنجه کردند، مثله کردند و به قتل رساندند.
رهبر عالی ایران آن کشتار را جشن گرفت و آن را «خدمتی به بشریت» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/news_hut/72054" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72053">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f9289304.mp4?token=GPCJlyIrY6_PX8IrrGkneHl_a2Mlp6cVDIK0A2PONxcB6leSt6oUy-q9XH7KPqGc-RKhS6P2GmjEp4NTfX5XXkZuV73F1KC3tU9GB0G8er_ll4gHBG7XIUlYlPQIths8almQTXwld8ETgjAVA0qpz9kiR0Ilq4wkxYGQ7684NGHodtQl50bcM5SB9mlaEGc4_-NaVl42mhyUvaWt_jlZy0MipafLlI5kNFcXTpujrMg4gFHN7GnVEhcP5XRxX2F094GNenS2TzBXcf6rWGTcyftzeT2bb9vgfn7YegYzwSXPDLFpAZuBYH4CeGq7uMwc2Z9JY895hjz2BlZDm-TzAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f9289304.mp4?token=GPCJlyIrY6_PX8IrrGkneHl_a2Mlp6cVDIK0A2PONxcB6leSt6oUy-q9XH7KPqGc-RKhS6P2GmjEp4NTfX5XXkZuV73F1KC3tU9GB0G8er_ll4gHBG7XIUlYlPQIths8almQTXwld8ETgjAVA0qpz9kiR0Ilq4wkxYGQ7684NGHodtQl50bcM5SB9mlaEGc4_-NaVl42mhyUvaWt_jlZy0MipafLlI5kNFcXTpujrMg4gFHN7GnVEhcP5XRxX2F094GNenS2TzBXcf6rWGTcyftzeT2bb9vgfn7YegYzwSXPDLFpAZuBYH4CeGq7uMwc2Z9JY895hjz2BlZDm-TzAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
این رژیم امسال بیش از ۷۲ هزار تن از شهروندان خود را به خاک و خون کشید.
تصور کنید چنین رژیم پلیدی قدرت آن را داشته باشد که از پشتِ سپرِ هسته‌ای، دست به حملات تروریستی گسترده بزند.
این واقعیتی بود که باید با آن روبرو می‌شدیم؛ واقعیتی که بسیاری ترجیح دادند آن را نادیده بگیرند. همه آن‌ها آن را نادیده گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/news_hut/72053" target="_blank">📅 18:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72052">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e271237b80.mp4?token=KyPbXRnKKoHPDPCcdC1bXnO7ULfaGYpzLNOr7rMhmwrOBbGsvD1vWErdIo923Ie-tG9G2YzBGh3CJEtp1DwjCWAqnahD8UrNC_Gt1W8rUxEc0MotcUSed8XRLNnqEwmjrlwT5ulNUeIRidybXtIKzmHEkrPmD0TXoG9snFYKqj-zsOdJ_UisJZAWeNjJeBy6TgvpoMRQ-AJh-QHLlaf58gVP9st_B3_Q6YxRvlMAhZG3GduBAwvZCZUFqqRsYXXyJiPkhz6RUiTISSGla6v4alH9fHitoWTs3NIoGdqlJACKc3bfwCQPPvKMjy2qlcEaQ4TjMb5QA3zoYNW_I6Zhtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e271237b80.mp4?token=KyPbXRnKKoHPDPCcdC1bXnO7ULfaGYpzLNOr7rMhmwrOBbGsvD1vWErdIo923Ie-tG9G2YzBGh3CJEtp1DwjCWAqnahD8UrNC_Gt1W8rUxEc0MotcUSed8XRLNnqEwmjrlwT5ulNUeIRidybXtIKzmHEkrPmD0TXoG9snFYKqj-zsOdJ_UisJZAWeNjJeBy6TgvpoMRQ-AJh-QHLlaf58gVP9st_B3_Q6YxRvlMAhZG3GduBAwvZCZUFqqRsYXXyJiPkhz6RUiTISSGla6v4alH9fHitoWTs3NIoGdqlJACKc3bfwCQPPvKMjy2qlcEaQ4TjMb5QA3zoYNW_I6Zhtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها موشکی ساختند که قادر به هدف قرار دادن اروپا بود و به آن بسیار افتخار می‌کردند. امیدوارم اروپایی‌ها متوجه این موضوع باشند.
هدف ایران این بود که در پناهِ سپرِ موشک‌های بالستیک متعارف، ساخت بمب هسته‌ای خود را تکمیل کند.
اگر آن‌ها موفق می‌شدند، آن رژیم شرور آزاد بود که تا ابد به گسترش وحشت و مرگ بپردازد.
@News_Hut</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/news_hut/72052" target="_blank">📅 18:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72051">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=ry8rLstH0ZNU3HY31Td4p0ugy8S6kv5IQP8kdh7x3smZTlBcduqB4Q1jMREUsEXZL__6kofdSBdZ7evwlJP4Ih6hXE3cfuB_bVfMmdrMv-uGJaBXhAvN8rSv6D8GLar-8IQ46E2ZDll0O8MgFB51A1mHfbkSxxwmyCiqehxwkPn3w-v4VZj3iN-yzCN2xzmvbT-5I1oc6pUpOVjPlBlLR_hUCjgOpZVoWTJm2wjaZsfIBG7-thv2j44Kbup1cZqHMTqHDtBYu2fqMUS_a2QyWq9L0_71qM2w33YptVHL7gnJMPKdey_q5BidHTRETrFVi-5A96nV4soSGIqjiorkDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=ry8rLstH0ZNU3HY31Td4p0ugy8S6kv5IQP8kdh7x3smZTlBcduqB4Q1jMREUsEXZL__6kofdSBdZ7evwlJP4Ih6hXE3cfuB_bVfMmdrMv-uGJaBXhAvN8rSv6D8GLar-8IQ46E2ZDll0O8MgFB51A1mHfbkSxxwmyCiqehxwkPn3w-v4VZj3iN-yzCN2xzmvbT-5I1oc6pUpOVjPlBlLR_hUCjgOpZVoWTJm2wjaZsfIBG7-thv2j44Kbup1cZqHMTqHDtBYu2fqMUS_a2QyWq9L0_71qM2w33YptVHL7gnJMPKdey_q5BidHTRETrFVi-5A96nV4soSGIqjiorkDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
سال گذشته، پس از آغاز به کار، مذاکراتی را با ایران آغاز کردم و به آن‌ها پیشنهاد دادم که در ازای پایان دادن به برنامه هسته‌ای و حمایتشان از تروریسم، از همکاری کامل اقتصادی برخوردار شوند.
اما آن‌ها نپذیرفتند. این اشتباه بزرگی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/news_hut/72051" target="_blank">📅 18:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72050">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29ba0a501a.mp4?token=fuAJIG3Fhau-_cC-1pqATamGwsU5PslXmxIrMo_dCxiMucfdDYW8Dh4CuF3-QYrDAcCp6F0IGDNe_Sq79Awu-4NHv9ibBe1gai3AgEBplJiuzaA4l-2MwJAwfuCcvTUgYO9hOriIbDbkK2bUPovJUX17-0eOx7ncolDb3eSN93psoxCXUuxZ903sJ3LKwvdQNAENgMtY-wM8MqrXwF3XCHuhqsCCHiz6YYS11ZnEwI0W-3hjbvo27Dk0FpunY0bdn8XU2Th9jbA_LsPM3-GvQ5AeIjOW67ckvM7ojczy_g8I4ZeMdxqolabMGKh4bVVjYXNYMpJxlsTxdNESOQR0IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29ba0a501a.mp4?token=fuAJIG3Fhau-_cC-1pqATamGwsU5PslXmxIrMo_dCxiMucfdDYW8Dh4CuF3-QYrDAcCp6F0IGDNe_Sq79Awu-4NHv9ibBe1gai3AgEBplJiuzaA4l-2MwJAwfuCcvTUgYO9hOriIbDbkK2bUPovJUX17-0eOx7ncolDb3eSN93psoxCXUuxZ903sJ3LKwvdQNAENgMtY-wM8MqrXwF3XCHuhqsCCHiz6YYS11ZnEwI0W-3hjbvo27Dk0FpunY0bdn8XU2Th9jbA_LsPM3-GvQ5AeIjOW67ckvM7ojczy_g8I4ZeMdxqolabMGKh4bVVjYXNYMpJxlsTxdNESOQR0IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها قلدرِ خاورمیانه بودند، اما دیگر قلدر نیستند.
از همان روز نخستِ ورودم به عرصه سیاست، موضعی تزلزل‌ناپذیر داشته‌ام:
هرگز اجازه نخواهم داد  ایران به سلاح هسته‌ای دست یابد.
@News_Hut</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/news_hut/72050" target="_blank">📅 18:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72049">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a4eccca8.mp4?token=Bakn_gn2Tc7jvZRZJdW5NHQTDpfGNEnCCBEyhzSJbvS-utdzg5EEjn3HlbiWBRnXwNFjulSGhmcu2AnHYup3dS8mwIfNyZII_8HY9QE-pgKeNTGv2P5ujPRayWJv3WdQw5Q_vVZqPQ1AYcTkQCd4payJT5W6CmJseHmJuml04qc7yW3W1VRuvQUCJnKBrn_e8-Or3WUF5pgCNbtA_MqQhRKcsH3p9op3owzqRV-CfW-5_ZtmTtVdfOC3-J_gCGMwzrOXaecyn8fvY-KYeiLcm37J9Kaxkz6sXJqs9HAVneO3BLRtJZGDA0CmpvVU004SYDkdDSw38RYTv7oxWFg7Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a4eccca8.mp4?token=Bakn_gn2Tc7jvZRZJdW5NHQTDpfGNEnCCBEyhzSJbvS-utdzg5EEjn3HlbiWBRnXwNFjulSGhmcu2AnHYup3dS8mwIfNyZII_8HY9QE-pgKeNTGv2P5ujPRayWJv3WdQw5Q_vVZqPQ1AYcTkQCd4payJT5W6CmJseHmJuml04qc7yW3W1VRuvQUCJnKBrn_e8-Or3WUF5pgCNbtA_MqQhRKcsH3p9op3owzqRV-CfW-5_ZtmTtVdfOC3-J_gCGMwzrOXaecyn8fvY-KYeiLcm37J9Kaxkz6sXJqs9HAVneO3BLRtJZGDA0CmpvVU004SYDkdDSw38RYTv7oxWFg7Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
من هیچ تمایلی ندارم که اجازه دهم خطرات، حتی یک روز دیگر هم رشد کنند. من به اینکه بگذاریم مشکلات وخیم‌تر شوند، اعتقادی ندارم؛ چرا که حل آن‌ها دشوارتر می‌شود.
بنابراین، در حالی که دیگران حرف می‌زدند، من عمل کردم.
در حالی که دیگران از صلح سخن می‌گفتند، من صلح را محقق ساختم.
در حالی که دیگران تهدیدها را نادیده می‌گرفتند، من با آن‌ها مقابله کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/news_hut/72049" target="_blank">📅 18:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72048">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd7fee3bd0.mp4?token=fVFzvZCceiJwPphXzM8nTDQ4h2X03DhIFwjrKxkZOx3PFory_YraQlr4jH6VD4z1T2oo2UVYGg5LgizOFlNDEB5hpBR8Tvi6snMbiixMa9-E2fuhpscaN4FglsLBu9qj0ad0sCS77oS483gM3-75tjezK1e0rhNLpT66cxVWAgkCPRTpV5WpjmHzFiM_6Qucv7wGZ3YbADev6aYXCEdsZLaM0jwxDhRhIALBCKLc6P98mfYkvGJr6BCbW85ZoEfEXDAwZyUXOkphNX2A-Ol4GxrMp_rtm2CFlTNqHur9CdoK0ul1vUt4tmzZdqZjUCedFJ1-IKEelx1q7l_K6d427w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd7fee3bd0.mp4?token=fVFzvZCceiJwPphXzM8nTDQ4h2X03DhIFwjrKxkZOx3PFory_YraQlr4jH6VD4z1T2oo2UVYGg5LgizOFlNDEB5hpBR8Tvi6snMbiixMa9-E2fuhpscaN4FglsLBu9qj0ad0sCS77oS483gM3-75tjezK1e0rhNLpT66cxVWAgkCPRTpV5WpjmHzFiM_6Qucv7wGZ3YbADev6aYXCEdsZLaM0jwxDhRhIALBCKLc6P98mfYkvGJr6BCbW85ZoEfEXDAwZyUXOkphNX2A-Ol4GxrMp_rtm2CFlTNqHur9CdoK0ul1vUt4tmzZdqZjUCedFJ1-IKEelx1q7l_K6d427w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ترامپ:
با افتخار به شما اعلام می‌کنم که آمریکا بازگشته است و کشور ما امروز قوی‌تر از هر زمان دیگری است.
اقتصاد ما مایه غبطه جهانیان است. ارتش ما قدرتمندترین ارتش روی زمین است.
فناوری ما بی‌همتاست و ما تقریباً در همه زمینه‌ها پیشتاز هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/news_hut/72048" target="_blank">📅 18:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72047">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سخنرانی دونالد ترامپ درمجمع عمومی سازمان ملل متحد در نیویورک آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/news_hut/72047" target="_blank">📅 18:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72046">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دیدم که مراد ویسی گفته احتمال اینکه پزشکیان و عراقچی رو تو آمریکا مثل مادورو دستگیر کنند غیرممکن نیست
آدم می‌مونه به این تحلیلگر چی بگه
😐
🧠
#hjAly‌</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/news_hut/72046" target="_blank">📅 17:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72045">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e4ea7a67.mp4?token=fTRqUpNBFaszfa7eWQM5ZNqFxmeXIG25Jvg4EmdpJG0D5wxYMXOL7S8_7P1XKD5Bo8j3_9o4EWGWgdtDb31EJEHCjnnKtEZSq1JsinuHn7czjSbY24P0Q3LU9MPLxNW4yJAphbCvH487fQceJqyeCV2I4PK_O939Z-DNGXb3Fb2oA0iOxku8Qd3tGFTvueFhYh5cppmA8V5lQmiMVTr1EgVXfT6HHPsMKLcj_Os2NrTKR1uQkFaIJeqHA-UVjuhDHaupwo8gS7rCxNF0CMoYfXtEAF_C3z0wS8P2337na8rFDnV-EY8syyziBEbrnjMYhhFjxiqEU1-1jkmiabWx7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e4ea7a67.mp4?token=fTRqUpNBFaszfa7eWQM5ZNqFxmeXIG25Jvg4EmdpJG0D5wxYMXOL7S8_7P1XKD5Bo8j3_9o4EWGWgdtDb31EJEHCjnnKtEZSq1JsinuHn7czjSbY24P0Q3LU9MPLxNW4yJAphbCvH487fQceJqyeCV2I4PK_O939Z-DNGXb3Fb2oA0iOxku8Qd3tGFTvueFhYh5cppmA8V5lQmiMVTr1EgVXfT6HHPsMKLcj_Os2NrTKR1uQkFaIJeqHA-UVjuhDHaupwo8gS7rCxNF0CMoYfXtEAF_C3z0wS8P2337na8rFDnV-EY8syyziBEbrnjMYhhFjxiqEU1-1jkmiabWx7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:پیامی که می‌خواهید به پوتین منتقل کنید، چیست؟
ترامپ: این جنگ را متوقف کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/news_hut/72045" target="_blank">📅 17:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72044">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7aa5b4a7d.mp4?token=vZEGyoVhIZ8VkN-XFXfg-09XIyv93VzNWVvaSU_MwAehwUhNEDqJYNIUhgBNwGXr9k1hMKmpOtPD1tZDwui-XLeXR2uqwQ1d1o7miXxvbjvXY4d1lHX_d_hP_I81pQN9Ew5xGRIbfyPo9LlIDoKfGWbk_gbiN6prti7YPbGGm-RMkUbWUt3ZIilPGOc8A5Hu-d4SgThJQradfJk_G8YVYBY0MO1YGi0PJe5HOxJAlcw5I3heLLblw5D7doNxjM_GidYn8t2KqkXVxfen6k_fV35c-a7ruH8kXmkOM3nkVhPWnYnkaUqvL1ZiQr1tvG9yfmmQGMP4cjGLo90syg9l4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7aa5b4a7d.mp4?token=vZEGyoVhIZ8VkN-XFXfg-09XIyv93VzNWVvaSU_MwAehwUhNEDqJYNIUhgBNwGXr9k1hMKmpOtPD1tZDwui-XLeXR2uqwQ1d1o7miXxvbjvXY4d1lHX_d_hP_I81pQN9Ew5xGRIbfyPo9LlIDoKfGWbk_gbiN6prti7YPbGGm-RMkUbWUt3ZIilPGOc8A5Hu-d4SgThJQradfJk_G8YVYBY0MO1YGi0PJe5HOxJAlcw5I3heLLblw5D7doNxjM_GidYn8t2KqkXVxfen6k_fV35c-a7ruH8kXmkOM3nkVhPWnYnkaUqvL1ZiQr1tvG9yfmmQGMP4cjGLo90syg9l4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ هنگام ورود به مجمع عمومی سازمان ملل خطاب به سی‌ان‌ان:
تعجب می‌کنم که سی‌ان‌ان اینجاست تا اخبار مربوط به مرا پوشش دهد. شما نباید اینجا باشید.
شما گفته بودید که قرار نیست اخبار مرا پوشش دهید. نباید مرا پوشش دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/news_hut/72044" target="_blank">📅 17:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72043">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72043" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/news_hut/72043" target="_blank">📅 17:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72042">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVaviNcNl3xr_6VMThFKotT6NZwF41NtKBmYDJfx-X-659XiCJBzgNCR84zbuxOeTHegj4zkpOha8R4n9FcF2XpFQvHPsi9z4w46fBOCyiSDYDRIxT7vX6PgzYY9-66C5zG10RXqK8Jfay7ICnWB3JcByuRog86efn6If58pVyMSwwsZ1yL-94xd0n_9R4nqBti0pQ3m34mGGQNlms68G60ew34MF1OLj6ahpTUvXh7h_BZJKUJTokyY8wnzMd-EjFU_-IobgN-DOhX00-pwFlxyYN3Kbdam6nIDmG_cLbcbYpe-VfXt7Z_VZlWQb319Kvi8q-nxIwNS35JhD7dhVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مسابقات
UFC Fight Night
شروع شد!
🦖
یک شب پر از مبارزات هیجان‌انگیز، رقابت‌های نزدیک و لحظه‌هایی که نتیجه می‌تونه در چند ثانیه تغییر کنه.
مبارزات رو زنده دنبال کن، عملکرد فایترها رو بررسی کن و پیش‌بینی خودت رو در
TrexBet
ثبت کن.
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/news_hut/72042" target="_blank">📅 17:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72041">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a05f244ea4.mp4?token=pHiUZeDSl-FRDgd81OSw038vA62W3pHS4Eao7tyOoPCwg7T88NLyRbm5rWwCbKUxuczoAgHzorhT_IB37ibidvKbBfe6cqilDBkceaFxCME-XDjWNaizveWutcj6iCuWOlih2tBAymlKgomj599ZEfGUdB42UU21KhkbFPyyyMxxMcFXveE7TOzBOCDIOeQBr8iBm0LXlPdR7jkqRw2wwdNo4rIIGIbgez15BLcUWLUVd8-_BcHIVIZur0x7mkEHBtSsH1l9fWqK0fB4hcry12TRMRWWOy8Jf-g1Z97C3kfgis1ZHeILV76gGsevAkehi5KQ4dDjXUdtFo0E7tK_4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a05f244ea4.mp4?token=pHiUZeDSl-FRDgd81OSw038vA62W3pHS4Eao7tyOoPCwg7T88NLyRbm5rWwCbKUxuczoAgHzorhT_IB37ibidvKbBfe6cqilDBkceaFxCME-XDjWNaizveWutcj6iCuWOlih2tBAymlKgomj599ZEfGUdB42UU21KhkbFPyyyMxxMcFXveE7TOzBOCDIOeQBr8iBm0LXlPdR7jkqRw2wwdNo4rIIGIbgez15BLcUWLUVd8-_BcHIVIZur0x7mkEHBtSsH1l9fWqK0fB4hcry12TRMRWWOy8Jf-g1Z97C3kfgis1ZHeILV76gGsevAkehi5KQ4dDjXUdtFo0E7tK_4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختره چندین دوس پسر داشته ده ها بار باهاشون رابطه ی جنسی داشته حالا اومده پیش متخصص زنان تا گواهی بگیره به نامزدش نشون بده پردش ارتجاعی بوده و سر اون پسر بیچاره کلاه بذاره.
@News_Hut</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/news_hut/72041" target="_blank">📅 17:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72040">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/396f2961ce.mp4?token=A2OoJQwbhdbtk7jNptV4a-P3N7Pl3gbBsTmTyexZs1hUY9zK6ipHnhgM1QHgjtMS-VVEyqKckvWJ9sieMXJ3sVbXBRWDTfXdMSo1__HVvOpoZsvetx_JR3xFQdFAjV6vPrFQtx1dmUC8ki9Rrjgz5_dfOccWhD8D3zvz2jYWyMt2wsOHAMHAG7ju_HSMBdy_nZQASOWxmzwmNBw7G-ymUA1dkctzas3mG8etWCmEoaCMAbmzRTrt2Os-gHz-i23hXiDaaWx5TplRhg0r9l5Si3-fK5hvTyFP9AEy-2IhQq2nmojVGRBvGxga6QY8fOnZ2Erj3xePXH_LIBPkygqwkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/396f2961ce.mp4?token=A2OoJQwbhdbtk7jNptV4a-P3N7Pl3gbBsTmTyexZs1hUY9zK6ipHnhgM1QHgjtMS-VVEyqKckvWJ9sieMXJ3sVbXBRWDTfXdMSo1__HVvOpoZsvetx_JR3xFQdFAjV6vPrFQtx1dmUC8ki9Rrjgz5_dfOccWhD8D3zvz2jYWyMt2wsOHAMHAG7ju_HSMBdy_nZQASOWxmzwmNBw7G-ymUA1dkctzas3mG8etWCmEoaCMAbmzRTrt2Os-gHz-i23hXiDaaWx5TplRhg0r9l5Si3-fK5hvTyFP9AEy-2IhQq2nmojVGRBvGxga6QY8fOnZ2Erj3xePXH_LIBPkygqwkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جان کیریاکو تحلیلگر و افسر سابق سیا؛
اسرائیل با پرداخت مبالغی در حدود ۱۰۰ دلار، هزاران شهروند افغان را در ایران برای فعالیت‌های جاسوسی به خدمت گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/news_hut/72040" target="_blank">📅 17:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72039">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تو نمایشگاه خودروی تهران که تازگی تموم شد، تنها کاری که مردم نکردن بازدید از خودروها بوده ؛
جکِ ماشین رو برداشتن، با خودکار رو کاور ماشین کشیدن، با مشت زدن رو کاپوت G700، کارت استارت ولوو رو بردن، شید سقف ماشین رو خراب کردن، خار دستگیره در رو گاییدن، دوربین جلوی ماشین رو کندن، جکِ کاپوت رو کندن، با خودکار رو صندلی ماشین خط انداختن، دکمه صندلی رو شکوندن...
‌
@News_Hut</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/news_hut/72039" target="_blank">📅 16:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72038">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1637ed0d1b.mp4?token=szdrFjO_Aj6zM6oQwFPqzRO0SjVPB--zOdvprLSLO9k9sC1WFSE27C1cdByKptVe18dibIe3AxWKVlcs-gpQfsQ8u8_zKx4lRb6zVECWXXtiMGE91KDZ89hEVTA7wYwguOH6IeW2bFdbI9dNwq83NPVFsLhd-C9a6Tkzl9ThUt9btGXH5WPbqfGTgdBA5A5Di7ODlP8lhPL9OolrtMNXSrsq8laV-ZDkan89DrNBiWSc8_PgmFUnfjOlz7NJfUcMiYkTBBuCyfvYkB8NfBZHNBZepX8jHYYM8zq5CpLSRy8XRRBcpwsbLGLiSzWOKQ4uTnjw3yzRZTlKFmFC5_vt_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1637ed0d1b.mp4?token=szdrFjO_Aj6zM6oQwFPqzRO0SjVPB--zOdvprLSLO9k9sC1WFSE27C1cdByKptVe18dibIe3AxWKVlcs-gpQfsQ8u8_zKx4lRb6zVECWXXtiMGE91KDZ89hEVTA7wYwguOH6IeW2bFdbI9dNwq83NPVFsLhd-C9a6Tkzl9ThUt9btGXH5WPbqfGTgdBA5A5Di7ODlP8lhPL9OolrtMNXSrsq8laV-ZDkan89DrNBiWSc8_PgmFUnfjOlz7NJfUcMiYkTBBuCyfvYkB8NfBZHNBZepX8jHYYM8zq5CpLSRy8XRRBcpwsbLGLiSzWOKQ4uTnjw3yzRZTlKFmFC5_vt_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل:
پیش از سخنرانی رئیس‌جمهور ایران در سازمان ملل، کانال‌های رسانه‌ای سپاه پاسداران ویدئویی مفهومی و ساخته‌شده با هوش مصنوعی منتشر کرده‌اند که تصویری از نخستین آزمایش واقعی (انفجاری) بمب هسته‌ای ایران را به نمایش می‌گذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/72038" target="_blank">📅 15:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72037">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3d6eda575.mp4?token=op882h7LBRhLz1ii_cSXCtlfuwSisnAJ1GxNKZQPiN6ihw_DOCS8hF4wHd1bWQL5Lza90XDDfaQLcl6kEfgXho3bCKOIdgds7UwBdrz6L_7G97ZJprmGLirTR0H0pH_zRXjGUQbXaYZWMkzGn_IrcaP56fV8tpT8-h7H-LZppdcMk67EFg1wMtIBQ6k84LLYw_Ga8sTXNs6HrYh6CtCWLr24jEhjrcbtuZH7qoee9AHlyUaZsNsoXsVg8Ff_QL6VaDv75BqfFdRwMBRQ9Bat2GV5QcwKSb1YvKf538oQTyKLRQrvcWHUUMCDP68-u22w2Yj61NYwFtfDYdJTo5Bi4V1rHVOF2rNI6InV_UKc3INsGIHphVCnSeBoarq3bpsmx1TbGMKO1nzsuiv3K-Y62CAHDGppMNP_XCfO08EUaKu0hwFO2nstf6vNTsjBXJxcHC_NYfbpSS5HgUITqHV2E41cS4wIRTdLdsxecIEWDPNf6zjuifEoyzrpATNHRFNdlfgACi6kl_6L8LixINKiMIgVOaSWlgX2h-kLbp-H0AkUrIfvSucbQjhe0YPlCITaArGatfqwNnC2dLHaRnuZVT4uuOTAt0Jn-X5vMgVGijJvf9Xbn6AWEBxmgVmarkCl1M88FxYjFms6PcPPGMozN5vSF-MS7MVBMJl5PWzTt5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3d6eda575.mp4?token=op882h7LBRhLz1ii_cSXCtlfuwSisnAJ1GxNKZQPiN6ihw_DOCS8hF4wHd1bWQL5Lza90XDDfaQLcl6kEfgXho3bCKOIdgds7UwBdrz6L_7G97ZJprmGLirTR0H0pH_zRXjGUQbXaYZWMkzGn_IrcaP56fV8tpT8-h7H-LZppdcMk67EFg1wMtIBQ6k84LLYw_Ga8sTXNs6HrYh6CtCWLr24jEhjrcbtuZH7qoee9AHlyUaZsNsoXsVg8Ff_QL6VaDv75BqfFdRwMBRQ9Bat2GV5QcwKSb1YvKf538oQTyKLRQrvcWHUUMCDP68-u22w2Yj61NYwFtfDYdJTo5Bi4V1rHVOF2rNI6InV_UKc3INsGIHphVCnSeBoarq3bpsmx1TbGMKO1nzsuiv3K-Y62CAHDGppMNP_XCfO08EUaKu0hwFO2nstf6vNTsjBXJxcHC_NYfbpSS5HgUITqHV2E41cS4wIRTdLdsxecIEWDPNf6zjuifEoyzrpATNHRFNdlfgACi6kl_6L8LixINKiMIgVOaSWlgX2h-kLbp-H0AkUrIfvSucbQjhe0YPlCITaArGatfqwNnC2dLHaRnuZVT4uuOTAt0Jn-X5vMgVGijJvf9Xbn6AWEBxmgVmarkCl1M88FxYjFms6PcPPGMozN5vSF-MS7MVBMJl5PWzTt5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه، درباره ایران:
رئیس‌جمهور ترامپ برای دیدار با پزشکیان یا هر کس دیگری آمادگی دارد.
اما اینکه آیا نتیجه سازنده‌ای از آن حاصل خواهد شد یا خیر، دشوار می‌توان گفت؛ زیرا تصمیم‌گیرنده نهایی در ایران، «رهبر عالی» است و رهبر عالی، یک روحانی شیعه تندرو است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/72037" target="_blank">📅 15:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72036">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70ab0515ff.mp4?token=D4bnDjLlwRUyVEuqMS0XBQBYWYrReTFYzsGce9fprzC2yCIiqr8ICjCjC0HPue6uUkpkCvtjpRwAXpy4AOwYcvjCbgU82C8rbBBRTX00Gy7preyc7l9eDgk8PZRKBYK1aRW5I1txBbC-aUtbAfQJ5624BtieGODVI46XGttZi87zHpx6oa6Oq7gcAe8PM-X3rim-OKiRrDFGQi5LyVjLQg5NdiAOCLO_coHBX6sqIHTD2Ht4oHhZDqN2lVwmApuEJrjaKsNuQ2DQknbS0amY52CpU_xxRmN7coGgxlzbti7tjjZdcypsyhK1X1L2_3mPA8fy0Ju38GnXgn1Hq2S7yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70ab0515ff.mp4?token=D4bnDjLlwRUyVEuqMS0XBQBYWYrReTFYzsGce9fprzC2yCIiqr8ICjCjC0HPue6uUkpkCvtjpRwAXpy4AOwYcvjCbgU82C8rbBBRTX00Gy7preyc7l9eDgk8PZRKBYK1aRW5I1txBbC-aUtbAfQJ5624BtieGODVI46XGttZi87zHpx6oa6Oq7gcAe8PM-X3rim-OKiRrDFGQi5LyVjLQg5NdiAOCLO_coHBX6sqIHTD2Ht4oHhZDqN2lVwmApuEJrjaKsNuQ2DQknbS0amY52CpU_xxRmN7coGgxlzbti7tjjZdcypsyhK1X1L2_3mPA8fy0Ju38GnXgn1Hq2S7yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران:
مسئله اصلی این است که ایران توسط روحانیونی دیوانه اداره می‌شود که دیدگاهی بسیار افراطی و آخرالزمانی نسبت به دین خود دارند.
این افراد هرگز نباید به سلاح هسته‌ای دست یابند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/72036" target="_blank">📅 15:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72035">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeeb195e4e.mp4?token=dcgJpw6K6f5qqmwdM5AKMC85NGGLVSwmDADrCL1SLt2bTZODsZIStRjqKxwGGxqAFCPOoSphIk8vj05df-Rhs69NLTzqZYbqiLsraJtsNCU-zBK_pyafZGlS2F9mPzfsNdGR7UilMjWMx2D0JPvJ1RcP3SskNrLmhSJZ83IGQuR2V3iVOvAN09aZIDzo_aHBJnub5Vy1KiNseveyoaMvTBPAcB_qy5sMMishLY8eZZbwx49UD3bzlWssrFolgrb8LfUCNrR3wHntMm2lyC0Qkf-TRwu5WYuwSVQECDB8hKUJqn-0OixKaxM-128FuM2tF62hZMCpYJtoFE93kylYkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeeb195e4e.mp4?token=dcgJpw6K6f5qqmwdM5AKMC85NGGLVSwmDADrCL1SLt2bTZODsZIStRjqKxwGGxqAFCPOoSphIk8vj05df-Rhs69NLTzqZYbqiLsraJtsNCU-zBK_pyafZGlS2F9mPzfsNdGR7UilMjWMx2D0JPvJ1RcP3SskNrLmhSJZ83IGQuR2V3iVOvAN09aZIDzo_aHBJnub5Vy1KiNseveyoaMvTBPAcB_qy5sMMishLY8eZZbwx49UD3bzlWssrFolgrb8LfUCNrR3wHntMm2lyC0Qkf-TRwu5WYuwSVQECDB8hKUJqn-0OixKaxM-128FuM2tF62hZMCpYJtoFE93kylYkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
ترامپ برای دیدار با هر کسی در سازمان ملل آمادگی دارد.
ما نیز برای دیدار با پزشکیان آمادگی داریم.
گمان نمی‌کنم در حال حاضر برنامه‌ای برای آن تنظیم شده باشد، اما قطعاً از چنین دیداری استقبال می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/72035" target="_blank">📅 14:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72034">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شرکت‌های هواپیمایی «ترکیش ایرلاینز»، «پگاسوس» و «اِی‌جت» (AJet) تمامی پروازهای خود به مقصد ایران را از تاریخ ۲۱ سپتامبر لغو کرده‌اند و امکان رزرو بلیت نیز حداقل تا مارس ۲۰۲۷ وجود ندارد.
تحریم‌های ایالات متحده موسوم به «عملیات طرد اقتصادی» (Operation Economic Outcast) دامنه‌ی گسترده‌ای دارند و حتی هواپیماهای ایرباسِ دارای قطعات ساخت آمریکا را نیز شامل می‌شوند؛ موضوعی که شرکت‌های هواپیمایی ترکیه را ناچار به توقف این مسیرهای پروازی کرده است.
شرکت هواپیمایی «ماهان» نیز پروازهای خود به استانبول و آنکارا را به حالت تعلیق درآورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/72034" target="_blank">📅 14:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72033">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_iawI-Usj0GVjqD1f3zs0zgy8DTWWUHO-rXin-LXQulrAJ0MX5Fp73WgUBDtANB4Kp1wuszdcpAbNynjhxfrZXv-YuWUOwlWaWJocjKgOqrGyErNKm5YnNFzzfTvloyi9mvzOtbSX0mDQ34OG33n8GA-LDNxYBB38EjD5jlZ1rPime3zVlM67JMZUYPIjpDwk_FlPIooLB7O2pnj2sxM5IDGlDE6AOzajY774ObA-wCeoPWd6yQ-bbQlqyXwzGGUNVdzJ0TqD4slAe8dDqT0mQrG_hfLX2yKAUBkGpSLt4vvSto3p3xJtyEcLX4kypUvtqZZiK8TBl66fuBKotsqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری ژاپنی «کیودو» و به نقل از یک مقام ایرانی که نامش فاش نشده است، ایران پیشنهاد کرده است که در صورت برداشتن گام‌های اولیه از سوی ایالات متحده برای کاهش فشارهای نظامی، تنگه هرمز را ظرف هفت روز بازگشایی کند.
این پیشنهاد که گفته می‌شود از طریق واسطه‌ها به واشنگتن ارسال شده، خواستار ازسرگیری مذاکرات با هدف پایان دائمی خصومت‌هاست.
این مقام ایرانی اظهار داشت که دستیابی به توافق همچنان امکان‌پذیر است، اما احتمال دیدار میان ترامپ و پزشکیان در حاشیه مجمع عمومی سازمان ملل را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/72033" target="_blank">📅 14:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72032">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPc8osDYHn3jbAucrtLJoLVv93zKe4FdZpCdgzcYCJcfe4OAOiqmDeef9fNLBK9klKXjMgzB1ANn89b0DxaR39ibEI-LlYPrdL2o53IrGTS6KE2oK8mNKN4qd66UfC4wjzq4Tl9SI8n_vS9MGhGpPDC-Q_pX97wfqPorsqFQ1lhuNoGh9pfH6xtcRI4EVbEgXLUZ9pAL9QG3rjDLt1frt7YXUCtAfuEWjWlk82IodAOt64d9ePCkaE1Tev-eK3F7LZ4OVXWJ9moib-Mz4qddnrYnepJ0orUXPzNoqT7OAG0KxXx-yx2u3nOKSylh5Aiog4j64hqgv_kwRfaUQUPz0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان صبح امروز برای حضور در هشتادویکمین مجمع عمومی سازمان ملل متحد، تهران را به مقصد نیویورک ترک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/72032" target="_blank">📅 12:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72031">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3534317cc.mp4?token=gjL07BLfILxaXUs-uYwV729f7_kzQPKvINB0muFHd064A4JxBFGugDslWmZPQS-KimFehh8yc9xG6vCm3mh1Kt23xpWqpRDR8iAk6-FXwUTq1FfGkk6csNXMZEanrbpWzoPxrOgJDPG6RykGUC4WE6x6mbEtH3Gq9Dkrhhi0nhWg6pX3-uqkcJ-Yf1S22hI4csJRSU-JuUtBmHKQlR2khBVCfNwx-8cr1t3y69WA1dhyoMJGyh3n6G_MEhpw5zytKYxDWOqCRGTl1IUyxEM7erMTm15692RbRvxxDfMqEiX2_u7NuH-K0OIZxz1-0YVng6V18_K0MeFJVRFMNxVeqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3534317cc.mp4?token=gjL07BLfILxaXUs-uYwV729f7_kzQPKvINB0muFHd064A4JxBFGugDslWmZPQS-KimFehh8yc9xG6vCm3mh1Kt23xpWqpRDR8iAk6-FXwUTq1FfGkk6csNXMZEanrbpWzoPxrOgJDPG6RykGUC4WE6x6mbEtH3Gq9Dkrhhi0nhWg6pX3-uqkcJ-Yf1S22hI4csJRSU-JuUtBmHKQlR2khBVCfNwx-8cr1t3y69WA1dhyoMJGyh3n6G_MEhpw5zytKYxDWOqCRGTl1IUyxEM7erMTm15692RbRvxxDfMqEiX2_u7NuH-K0OIZxz1-0YVng6V18_K0MeFJVRFMNxVeqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت عجیب سربازان روس که به بالای دکل ها رفتند تا با استفاده از سامانه های پدافندی دوش‌پرتاب(MANPADS)با پهباد های اوکراینی مقابله کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72031" target="_blank">📅 12:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72030">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72030" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72030" target="_blank">📅 12:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72029">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOyFH_TnOznpDw8o-vWp20R7GMYGokAfwoF4s5FwGiJY_q3VoEnfrcZT-MEUhF7EuwT6yixkRblXyjzdcDVJCLhW0r87ZJNDBWMioEeNJ5TWzOsZGgOof_BpnO5fVVGrURjwm_6mscYP4QVIRNiNYHyp4LlIfvr4TcnsFK3x-JPUo1ZgER-Bya0q9jiww28V8cPrlO6oKcCqa3KKdDJXq4iG-HMvFlXiyA6p__kuq2KccpBrYgf3ww4-oWONHJfS1zQs8k2XpJThP4Wo7MVVXEeL27VHhJ4fHxlKDAm8dOC2mBKXGv2yJQnMEmr_bWbAxp6-Eo7_-rUnsHrq1g4UsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/72029" target="_blank">📅 12:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72028">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCAxwowg34yv5T1dZ9cQ7PM0UE6CefyC_ERtRGINGV8sVmskJTHYP5RVOuRy4miFYtlwkjSGlCiyATUXVsOtRXM6SJzSsmbZgVoEtqYNS9egyug2t71BsEImHqWMRCnZCULtCAmCvvBYWprJOkgPpFLkxRKrJB8xgL7WPRIwGwJbKezuuRNdUxeKo3-X-oUTFI0EtFzWrkKY2o5z1Z34XBkZXzQac9838A25_VM6ODbFhf0TBR4V2eCExfmLUtBg49gQw8k2VdotZ_XG9VBzbS9BGwI76rtKMp57qKtp540OTNblKq0RiofF2e8FiLKduogl22C5xM77ZWzdy_ELMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندی برنهام، نخست وزیر، گفت که بریتانیا پس از حملات پهپادی و موشکی حوثی‌ها، پشتیبانی «سوخت‌رسانی هوایی دفاعی» را در اختیار عربستان سعودی قرار خواهد داد.
این پشتیبانی که انتظار می‌رود در روزهای آینده آغاز شود، شامل یک فروند هواپیمای نیروی هوایی سلطنتی وویجر مستقر در پایگاه نیروی هوایی سلطنتی آکروتیری در قبرس خواهد بود.
مقامات بریتانیا گفتند که این استقرار «محدود به زمان» خواهد بود و احتمالاً «برای چند هفته» ادامه خواهد داشت.
برنهام گفت که این اقدام به دنبال درخواست عربستان سعودی برای «حمایت نظامی» و با هدف حفاظت از ثبات منطقه‌ای و منافع بریتانیا انجام شده است.
«عربستان سعودی حملاتی را تجربه کرده است، به دنبال اختلالات احتمالی بیشتر است و ما باید این مسیرها را باز نگه داریم و از این رو با این درخواست موافقت می‌کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/72028" target="_blank">📅 12:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72027">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e88d60053.mp4?token=EYFeG_tl8WOY4AhVHJViuiD2T3uywAYtEJ4aLJBrKOwzf7GCvHz_NPuN_GE5de6rhKoLTFE3Fw3dg1XkNLw-9CQhH1dOAGNnYY6nPIfB3IMVjSHmWpgYD2beSecdUUzJJUSJTPh8BAtEYZnXfSMRKUFE9p08pJx2-Z9A9LjMR8WQ9m4SsU_GrUABZsp_Z8L_54WdgHIkQ8SoweZ7HzzH61e6rAlMEIGZR-y8cxVhc1x4e7X4AfrR2lXOd_8PU05aFmMPEqoNsyModjJywJwZWb4e_AnV2b7fz-r6W6hrhLEHwCWdk5TwzNN3mM1B7diF1Ccz5YGL6sdE-a3j1IEqiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e88d60053.mp4?token=EYFeG_tl8WOY4AhVHJViuiD2T3uywAYtEJ4aLJBrKOwzf7GCvHz_NPuN_GE5de6rhKoLTFE3Fw3dg1XkNLw-9CQhH1dOAGNnYY6nPIfB3IMVjSHmWpgYD2beSecdUUzJJUSJTPh8BAtEYZnXfSMRKUFE9p08pJx2-Z9A9LjMR8WQ9m4SsU_GrUABZsp_Z8L_54WdgHIkQ8SoweZ7HzzH61e6rAlMEIGZR-y8cxVhc1x4e7X4AfrR2lXOd_8PU05aFmMPEqoNsyModjJywJwZWb4e_AnV2b7fz-r6W6hrhLEHwCWdk5TwzNN3mM1B7diF1Ccz5YGL6sdE-a3j1IEqiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو صحبت کردن این پسر با یه پشه که تو اینستا خیلی وایرال شده
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/72027" target="_blank">📅 11:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72026">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/72b152b531.mp4?token=FlWoSxGBEj_MLvGTUmcMwDdZnEMEdRbr8CZb5wYP4u_5TXVwvZOmeAks5yLAZhf5VOJb0ENfdqmWDq6H018goW0XgHPQQ-NMkAT9pEFmwazhtkBZFmaOP_BnSzcpdFW9YJVduFpvaVmLkYOQWzusl87VZM1o1HQ5HtOkjNRrZJw3T2OviU8BHp-uKIvujc8cDakJRUvh2IIx7863JW0tDBzPigpEcGstaamPnFnG2b_8eH-PiX5aR0mCjByxqzuV6PeTj03GZqmdoZO96jgjWvQxB0Ht0WbjOSqbOvJfBZlFVWDkvY2_TzbcSVz0842HP6_Vo-2-8Hukvio3CJ-qTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/72b152b531.mp4?token=FlWoSxGBEj_MLvGTUmcMwDdZnEMEdRbr8CZb5wYP4u_5TXVwvZOmeAks5yLAZhf5VOJb0ENfdqmWDq6H018goW0XgHPQQ-NMkAT9pEFmwazhtkBZFmaOP_BnSzcpdFW9YJVduFpvaVmLkYOQWzusl87VZM1o1HQ5HtOkjNRrZJw3T2OviU8BHp-uKIvujc8cDakJRUvh2IIx7863JW0tDBzPigpEcGstaamPnFnG2b_8eH-PiX5aR0mCjByxqzuV6PeTj03GZqmdoZO96jgjWvQxB0Ht0WbjOSqbOvJfBZlFVWDkvY2_TzbcSVz0842HP6_Vo-2-8Hukvio3CJ-qTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی عظیم در دنیپروپتروفسک؛ صحنه‌ای آخرالزمانی؛
پیش‌تر، وزارت دفاع روسیه اعلام کرده بود که نیروهای مسلح اوکراین از تأسیسات غیرنظامی برای اهداف نظامی استفاده می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/72026" target="_blank">📅 11:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72025">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6404ec7a8.mp4?token=A21dZAOjir5KoxXlD1BvljSYhOg-9zqs7giyuBqmMoEAnZdUsDKzxM7Fp5ceLEEpLAvu7gqZlaxvwOchzEhtJ-cq35Vk_7GlDNwRMbWs11KOT7lIvPsUMhq7qUlhI9H0VQVq4_dwn80ey81D5DuW8-nWSDt3uLYCDDDfJ7QvjXBaANAofF8vc_K7rkYI5U6gGIqmyWWZCWiWkImT5tupKl97ezBCIp72W08oYvyd6pPcbyel_CCnHN5bDehrgP6cKNaOvo-G_fQlr6J7z7aElzdKBL4xsTf51ShQkewIndzX-3HCLyGsQfpNRyPirsehLxyLGDI8lyDsMvedWR3xqHNbeF9POWpiy-uaU8FQt3uR9qMeu4ye9WOt7w6sILqLetOreepCut-ZibzLpvhVmoKoTh9YEJB6FYJcTA-5SpiElPmE-w66EnV8QPScf2o2wMVNhp6vHoP5kDTrEFztu5h3K_pKrl-KnfRpK1wvjSakqAfRfxvlQtUtXYRoDEFaOKuSemuPpNLFmuoKR2UiJXx3F_MiEb4UCD9k2K2yUXPwh0PEKSMhToJHNRmAuO2MrF1PxCRazP1nMwUsoPJg3UflzmpSkS2Ac0xOI-txkVt_m-LT79Qt-FWCkbZqCT8vLr2r9K-1Lvml9IqRzaDaHkUU0AxL_UrC5HxBbvAeIaU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6404ec7a8.mp4?token=A21dZAOjir5KoxXlD1BvljSYhOg-9zqs7giyuBqmMoEAnZdUsDKzxM7Fp5ceLEEpLAvu7gqZlaxvwOchzEhtJ-cq35Vk_7GlDNwRMbWs11KOT7lIvPsUMhq7qUlhI9H0VQVq4_dwn80ey81D5DuW8-nWSDt3uLYCDDDfJ7QvjXBaANAofF8vc_K7rkYI5U6gGIqmyWWZCWiWkImT5tupKl97ezBCIp72W08oYvyd6pPcbyel_CCnHN5bDehrgP6cKNaOvo-G_fQlr6J7z7aElzdKBL4xsTf51ShQkewIndzX-3HCLyGsQfpNRyPirsehLxyLGDI8lyDsMvedWR3xqHNbeF9POWpiy-uaU8FQt3uR9qMeu4ye9WOt7w6sILqLetOreepCut-ZibzLpvhVmoKoTh9YEJB6FYJcTA-5SpiElPmE-w66EnV8QPScf2o2wMVNhp6vHoP5kDTrEFztu5h3K_pKrl-KnfRpK1wvjSakqAfRfxvlQtUtXYRoDEFaOKuSemuPpNLFmuoKR2UiJXx3F_MiEb4UCD9k2K2yUXPwh0PEKSMhToJHNRmAuO2MrF1PxCRazP1nMwUsoPJg3UflzmpSkS2Ac0xOI-txkVt_m-LT79Qt-FWCkbZqCT8vLr2r9K-1Lvml9IqRzaDaHkUU0AxL_UrC5HxBbvAeIaU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این اخوند توضیح میده چقدر رژیم جمهوری  اسلامی پول خرج اینا میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72025" target="_blank">📅 10:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72024">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d71cb9ab.mp4?token=oM3JTz_kyIPjhe5NORI33M5wuqxU21ggEr52Hzk6HYS5GxX7hih9gpM_e8yf2RZ3FGM1Qu2D6fcYSJ2iMb-f5Vr9RKV8cJfbT8n6AquC3i1V9QDfVQGvU2a8dQLTWJw2khKR-zCwcCE-5t0_5-GHpuyz4u-PBZXtEI1jiPxU6leTRI2V_fYTq1OoxyjuYsJbDpg1IwFloAwpAS0VvDBUA7dnlBdA9L-lECmKiqh4y4obxh-wSK719UxNvFJttUa4GsDNOP0TkjKQoXUOsWf8OkIzksVggO3VvSU5f-MPQ-WVjBf7Me8GbibgbulXsb3mbs9E6b1jKKtneV1vBtCcWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d71cb9ab.mp4?token=oM3JTz_kyIPjhe5NORI33M5wuqxU21ggEr52Hzk6HYS5GxX7hih9gpM_e8yf2RZ3FGM1Qu2D6fcYSJ2iMb-f5Vr9RKV8cJfbT8n6AquC3i1V9QDfVQGvU2a8dQLTWJw2khKR-zCwcCE-5t0_5-GHpuyz4u-PBZXtEI1jiPxU6leTRI2V_fYTq1OoxyjuYsJbDpg1IwFloAwpAS0VvDBUA7dnlBdA9L-lECmKiqh4y4obxh-wSK719UxNvFJttUa4GsDNOP0TkjKQoXUOsWf8OkIzksVggO3VvSU5f-MPQ-WVjBf7Me8GbibgbulXsb3mbs9E6b1jKKtneV1vBtCcWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سال گذشته مردی در حال قدم‌زدن با سگش در کامچاتکای روسیه بود که متوجه نزدیک شدن سونامی شد و با تلفن همراهش از آن فیلم گرفت.  لحظه‌ای هولناک و در عین حال شگفت‌انگیز از قدرت طبیعت.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72024" target="_blank">📅 10:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72023">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gu6kGSs11XPV9GiVqyVG5eFIs9zGgzvlsKJsqIEx7u12THaHgfXOiE0xUR4EllgPo9Xk3gKoYIOs7rb58rlkCn7wSb0c1al7gBK3D5EM9JABAlyreZu-xunwqHPzl3uR-a-flCHJkfcLxQ4NTcSs0Wwvzbmmk3Erp1rG-ScXBn5uCgrUO-leN6uWTRq-8ch65CiC16EPHLJrc8JIM6m6VEIGBxIUZ2xua71BNuxzKOtbZZyKoIXC9QAMcj_orIddgpz8VQsrZaGCHO9gAoe1mbzzy7-jkHHzbXOMglMRf0c4QVoutokCsfD1-uKr4f8aQgnZJ9T0vnqeZ88utTuZ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در پی درخواست مجدد عربستان سعودی برای اقدام نظامی، در تعطیلات آخر هفته احتمال صدور فرمان حمله به حوثی‌ها (انصارالله) در یمن را بررسی کرد، اما در نهایت تصمیم گرفت از انجام آن خودداری کند.
دریاسالار برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، پیش‌تر تمامی گزینه‌های مربوط به حملات هوایی را آماده کرده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72023" target="_blank">📅 09:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72022">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8969619843.mp4?token=UQO1bpGpgPI-YUrutfGVLtZaQZ5ByKeo0aPGO0gHeVE2Na7kYSTDqQAzKPSsYfmAXSxzItCM-NAp_QPRbHRjr3_sX1B7aj1YFzaGcZPS-nLkjUuli4s_wOnp_TuUYmhXz1SbxVITJp42VZlHTh87rvzJFA5WRufWKz5b5DvL2eleYVp4xzMa-PsQYMNGJ_aH2zQqZrkN9ue96obh1Z9E_H4P_9gDd7I8haij-5UvQraOMUPIe_9jlNrEty8h30UsbDyLo_rvpARTrB3b4vuJv3U7A5OM_M4lKMtkDSQK89K0e9VsOJjz8SIhC5xn0E3D9e34PfwcxuRHOH1qtxQvKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8969619843.mp4?token=UQO1bpGpgPI-YUrutfGVLtZaQZ5ByKeo0aPGO0gHeVE2Na7kYSTDqQAzKPSsYfmAXSxzItCM-NAp_QPRbHRjr3_sX1B7aj1YFzaGcZPS-nLkjUuli4s_wOnp_TuUYmhXz1SbxVITJp42VZlHTh87rvzJFA5WRufWKz5b5DvL2eleYVp4xzMa-PsQYMNGJ_aH2zQqZrkN9ue96obh1Z9E_H4P_9gDd7I8haij-5UvQraOMUPIe_9jlNrEty8h30UsbDyLo_rvpARTrB3b4vuJv3U7A5OM_M4lKMtkDSQK89K0e9VsOJjz8SIhC5xn0E3D9e34PfwcxuRHOH1qtxQvKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود: ‌دونید شماها گوهرید یا نمی‌دونید؟
دخترها : بله می‌دونیم نه نمی‌دونیم
مسعود: می‌دونید من اینجا الان اسمم رئیس‌جمهوره؟
دخترها : بله
مسعود:  می‌دونید من از یه خانواده معمولی به اينجا رسیدم؟
دخترها : بله
مسعود: یجور این مملکت رو درست بکنید هیچ بیگانه ای نتونه بیاد اینجا شماها بخواید میتونین دیگه من تونستم شماها هم میتونید دیگه
خنده های وزیر آموزش پرورش فقط
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72022" target="_blank">📅 09:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72021">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f75dfbec.mp4?token=CPmHGB-VPHDDzKe0FFhATXdqLFCG_Z5SOeJbiML0Xrc6yPEzBXgfpkqzHGfBeNVdjgJ1GeHv6bDF56A72_0m-oa7RuGhGGTDSlAW5AHUTJoe2IwaKizU8_UPftgVBP_dyj2YEolZ6zabq00e8FCHSYf6jzSv24WHfT518SlimCccPZaJxPjmd-USAvEPbWMMukDwO9zJnzASQj4tgyb9xRASSvfCFTpa1SPIuKdL5c5bJdL_r6N-1CCjftJtv4C8l6kTIM3AZsdd-Bk2YzOi5Cg2pk2K39D28tirxmhYO6e55fPUnD-5uAWX9VIq10CzXSsHGYvqzT9ods22pKu9kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f75dfbec.mp4?token=CPmHGB-VPHDDzKe0FFhATXdqLFCG_Z5SOeJbiML0Xrc6yPEzBXgfpkqzHGfBeNVdjgJ1GeHv6bDF56A72_0m-oa7RuGhGGTDSlAW5AHUTJoe2IwaKizU8_UPftgVBP_dyj2YEolZ6zabq00e8FCHSYf6jzSv24WHfT518SlimCccPZaJxPjmd-USAvEPbWMMukDwO9zJnzASQj4tgyb9xRASSvfCFTpa1SPIuKdL5c5bJdL_r6N-1CCjftJtv4C8l6kTIM3AZsdd-Bk2YzOi5Cg2pk2K39D28tirxmhYO6e55fPUnD-5uAWX9VIq10CzXSsHGYvqzT9ods22pKu9kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ سی‌ان‌ان، ام‌اس‌ناو و پولیتیکو رو به خاطر «فیک‌نیوز» از کاخ سفید ممنوع کرد.
فاکس‌نیوز + ABC، CBS و NBC در اعتراض، پوشش تلویزیونی مشترک (TV Pool) رویدادهای ترامپ رو متوقف کردن.
نتیجه: مراسم‌ها بدون صدای زنده پخش شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72021" target="_blank">📅 07:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72020">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72020" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72020" target="_blank">📅 01:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72019">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMVROq-CC8O0zdQ1cVMoWw_HoVHez-oGGftX1DM3pREWgZTMC6Wt-n278ZduH94NxvqnML7yIXrT9pLLGYxiCRJJgv-Pvgjl9zyfPBtqzP7lnhTH7b3AzveDndU5SpmqazD-GI7qw8fZlbQBWjbefG2Ya2uOTZDW6lb0CZEQnk2yVc6eAZN65ql4_NUtHIWn9WuWiZUlFxeyp-K2mt0kITy391_S1uRvxSrDBM2L8vtI3BhH2wkvc-Tsjtrplk9qb4nHYohd7gzEqdpnU-1F2huNRmM580iBfiFCrirFSfVQrgXyeFG79G0lnkBg8ZjiszlDhmQxVUBSJjVYKjrIgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72019" target="_blank">📅 01:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72018">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d99b0ae83d.mp4?token=JOFKBSZeA4TXeyZZ0XupZF_ko8SE1JpcvF-6FRgMFddY5mvAJam46cGBumle3oCBnb0lX3SmqO8Jrfjho1j-Wmk4Ff279KCLQV6xSopEKAh1vInBjozIkuZ59PvchBM8q645zqt71ZCKKYrhzPReHml9lky-K0-yCCpqMQjoCD-EJf7KxfC4412_1OhnLz9MI_3zOClA8IxSi58AZeQ6jBYOWEfm3FOnTELIw18a0BxZNZQhckhVfBzp0BuKsx9hpmIBnb3sU46XN8jfuR5Rxr8krPFcdHOa1aNYrd7RjEWPeBIA_cfa7tA3gg5LlmOqsirm3HRkODq7GvJhINRRrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d99b0ae83d.mp4?token=JOFKBSZeA4TXeyZZ0XupZF_ko8SE1JpcvF-6FRgMFddY5mvAJam46cGBumle3oCBnb0lX3SmqO8Jrfjho1j-Wmk4Ff279KCLQV6xSopEKAh1vInBjozIkuZ59PvchBM8q645zqt71ZCKKYrhzPReHml9lky-K0-yCCpqMQjoCD-EJf7KxfC4412_1OhnLz9MI_3zOClA8IxSi58AZeQ6jBYOWEfm3FOnTELIw18a0BxZNZQhckhVfBzp0BuKsx9hpmIBnb3sU46XN8jfuR5Rxr8krPFcdHOa1aNYrd7RjEWPeBIA_cfa7tA3gg5LlmOqsirm3HRkODq7GvJhINRRrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، برای شرکت در مجمع عمومی سازمان ملل وارد نیویورک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72018" target="_blank">📅 01:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72017">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e2686a0e6.mp4?token=japXbHE4KBLcRGCm2j7-waFEEMlkR_k6R8zAT5wOQvzIsHkA4LrdXF3QZhtRY235SyXkNb3_vq2U25QK2igifXnmipB4HXq0TMy-Zn-uq7UR-rJbhvbeakNsfJghKbTiHUSX-R3p00EGiv3mr4HQxXqMA1Bn7dz3nH3fb9ojWHyI6NG0Wwmj_upV99xSnL0vzEDnmFB3tGtHJkDY3nKJ5n-jRVRk-wYslLaDmUbAf3-8oZTB-lShNiXCZ70jlONQ4AsdODi_IdVo8cH94RiCx-Uxm1uRLcyuU68Lvs-_s1d1adXzItXz0IQo7pl02iJIN2SEXcspPmVsX3hyfKajdUqayfgsKNyfpDQnbwK9FLreQP6xSRwy9LbU1wGClXNMMNkrhxgc0IOssbU1_Pd8ZrlGmPIZWJPUWEIYttqq9srgfbPFjk47ZsQ0h2qUYVlAymJ597SwmOrLy3pnuZi52oM4FwCbEm445oRUqfdOJD-Sj2UKG-P8pM-ksxY7zAFNy2YHk-ES96vNCYH26DZ624HmQ4anuWB0Y1DZmfgmRPh5xyVSUK-w3xuxB6UuQJCEpYhQxiWE_D28lfiuSF2fSPR2rMYzqcogSRcynGAv8BPMlm94buTSU4ynod870lriZa60hmQckKVe1f8WQPXMRBMxLatqOKnM__naLKbyb5o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e2686a0e6.mp4?token=japXbHE4KBLcRGCm2j7-waFEEMlkR_k6R8zAT5wOQvzIsHkA4LrdXF3QZhtRY235SyXkNb3_vq2U25QK2igifXnmipB4HXq0TMy-Zn-uq7UR-rJbhvbeakNsfJghKbTiHUSX-R3p00EGiv3mr4HQxXqMA1Bn7dz3nH3fb9ojWHyI6NG0Wwmj_upV99xSnL0vzEDnmFB3tGtHJkDY3nKJ5n-jRVRk-wYslLaDmUbAf3-8oZTB-lShNiXCZ70jlONQ4AsdODi_IdVo8cH94RiCx-Uxm1uRLcyuU68Lvs-_s1d1adXzItXz0IQo7pl02iJIN2SEXcspPmVsX3hyfKajdUqayfgsKNyfpDQnbwK9FLreQP6xSRwy9LbU1wGClXNMMNkrhxgc0IOssbU1_Pd8ZrlGmPIZWJPUWEIYttqq9srgfbPFjk47ZsQ0h2qUYVlAymJ597SwmOrLy3pnuZi52oM4FwCbEm445oRUqfdOJD-Sj2UKG-P8pM-ksxY7zAFNy2YHk-ES96vNCYH26DZ624HmQ4anuWB0Y1DZmfgmRPh5xyVSUK-w3xuxB6UuQJCEpYhQxiWE_D28lfiuSF2fSPR2rMYzqcogSRcynGAv8BPMlm94buTSU4ynod870lriZa60hmQckKVe1f8WQPXMRBMxLatqOKnM__naLKbyb5o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش خبری فاکس نیوز به نقل از ترامپ:
«در حال تصمیم‌گیری هستم.»
اریک شان، خبرنگار ارشد فاکس‌نیوز، گزارش می‌دهد که دونالد ترامپ، رئیس‌جمهور، در حال بررسی گام بعدی خود در قبال ایران است؛ آن هم در شرایطی که برای دیدار با رهبران کشورهای حوزه خلیج فارس در حاشیه مجمع عمومی سازمان ملل در روز سه‌شنبه آماده می‌شود.
ترامپ در حالی که گزینه‌هایی همچون اقدام نظامی، تداوم فشار اقتصادی یا تلاشی دیگر برای دستیابی به توافق را سبک‌سنگین می‌کند، به فاکس‌نیوز می‌گوید: «سؤال من این است که آیا و چه زمانی کل کشور [ایران] را نابود کنم؟ بهتر است آن‌ها درست رفتار کنند.»
این هشدار هم‌زمان با تشدید تنش‌ها در منطقه مطرح می‌شود. ایران تهدید کرده است که در صورت انجام حملات جدید از سوی واشنگتن، علیه منافع آمریکا دست به تلافی خواهد زد؛ این در حالی است که حوثی‌های مورد حمایت ایران نیز به سمت عربستان سعودی موشک شلیک کرده‌اند.
ترامپ همچنین می‌گوید که برای دیدار با مسعود پزشکیان، رئیس‌جمهور ایران، در هفته جاری آمادگی دارد، اما در حال حاضر هیچ دیداری میان این دو رهبر در برنامه گنجانده نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72017" target="_blank">📅 01:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72016">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612f18036a.mp4?token=t3Ocls12Ch-m2DAsSBZYhL3xcHeWbTsaOuzFEeEn68PlTS7F4m0ARS11nGAy1uBKOS2FPy7nE0U900yq7OhVH2_mqJL6omrhuKm6jBgkkW1RH32po6Dz2VkAulHHFpwkzCnaSYD0yHlzD4IH3MDe0d22xpip-68DszNzHF-HtXQTlXcIo2fPjaLhmeyDZgF-bUA4KPjXmA1kMyZAYlrvWTAkCGjj6utsDz80ZpUNkw6TU4prbaJG-qNF33Wx8rZ8iKgNTv_SEmjz5m2rn-L82F2YGmVwSABSOFgp4OuAIVOPTtzF5Y8Sozkrrlij6qZLhJDgcOOF25jAK6RYd7P0JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612f18036a.mp4?token=t3Ocls12Ch-m2DAsSBZYhL3xcHeWbTsaOuzFEeEn68PlTS7F4m0ARS11nGAy1uBKOS2FPy7nE0U900yq7OhVH2_mqJL6omrhuKm6jBgkkW1RH32po6Dz2VkAulHHFpwkzCnaSYD0yHlzD4IH3MDe0d22xpip-68DszNzHF-HtXQTlXcIo2fPjaLhmeyDZgF-bUA4KPjXmA1kMyZAYlrvWTAkCGjj6utsDz80ZpUNkw6TU4prbaJG-qNF33Wx8rZ8iKgNTv_SEmjz5m2rn-L82F2YGmVwSABSOFgp4OuAIVOPTtzF5Y8Sozkrrlij6qZLhJDgcOOF25jAK6RYd7P0JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ درباره ایران:
وضعیتشان خوب نیست. در واقع، امروز جلساتی در این باره دارم. عملکردشان بسیار ضعیف است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72016" target="_blank">📅 01:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72015">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqSixJ_p0xRjmInAUAztuzp89ZSqOqUCMsnftT6Xp6DzH0iX6M6UbiSRyDski2QEKU2stuvYRpOP2Gt5DMwlGL3EI3jUvOgYMPfSN1m9oby3shPuWLKfjktJx9xEjmnGj29xSv5bKK-hGHKSeD_Uc_RjVQBm7GSzF4GckXAV0jPudfCGMs0raUBh_v_cqVxaUY3yGwH3hvOH_fl7n4jzwhdFR7oUoyMdE80ki1cfAyK-KHd64Pl-fNA5-6pWZs1_miM1QHcDSPSgs7UQng8RT6pVoHHMTCN9EtUW3wSZWYQoeerzABDnsISf7ISQ1mQhowubQAYLr_ARRCQbDQ-bQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امجد طاها، روزنامه‌نگار و تحلیلگر اماراتی، با انتشار پیامی کوتاه نوشت:
«اتفاقی عظیم در راه است؛ حرکتی تاریخی و بی‌سابقه. آماده باشید.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72015" target="_blank">📅 00:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72014">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترکیش ایرلاینز پروازهای ایران را تا مارس ۲۰۲۷ متوقف کرد؛
یک نماینده شرکت هواپیمایی ترکیش ایرلاینز اعلام کرد تمامی پروازهای این شرکت به ایران دست‌کم تا مارس ۲۰۲۷ در برنامه پروازی قرار ندارند.
این شرکت همچنین اعلام کرده بازگشت پروازها پس از این تاریخ نیز تضمین نشده است.
این تصمیم در پی تشدید محدودیت‌ها و فشارهای بین‌المللی بر صنعت هوانوردی ایران اتخاذ شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72014" target="_blank">📅 00:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72013">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GblVJmG04v3yRx_PDH_muhEwr5j4lH1mIbDC0Uc-tj4LvdaL7wzk-QyFHgdgSG5h-1x6QplQ5RF7xWV-7UAgM_0P6BjTpA5xRrA4LEA0NJHyrwJ7Eiv9Ts8eF4xCXNv1AnNGebTh3Gme_EHboAiUHxW0hiGMqG3zRZmMxycgiTn9vcBh-eBaM6ZQoMQ7muMiYtoTgRLBeVy2c35MbpVn7HYQVrF3spZTFd_SaC0yqe8PLhkrlpPT211ukeCjQHmDxBypUMkL4hHkq8dL3wn25QmwfVQV1XGpyYnIIK8C3WzO5vurMkBGxAvTzuGWQMXi-qdiaii6gEcLRaD9KWGGBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛مقامات استان لوبلین لهستان در پی حمله هوایی جاری روسیه به اوکراین، هشداری مبنی بر احتمال بروز خسارات جانبی صادر کردند.
هوانوردی لهستان در حریم هوایی کشور در حال فعالیت است و وضعیت تحت نظارت قرار دارد. به ساکنان توصیه می‌شود منتظر اطلاعیه‌های بعدی باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72013" target="_blank">📅 00:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72012">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">#فوری
؛حدود ۵۰ دقیقه پیش، هشدارهایی در پی احتمال وجود تهدیدی در حریم هوایی منطقه «کراسلاوا» (Krāslava) در لتونی — که در امتداد مرز با بلاروس و در نزدیکی مرز روسیه واقع شده است — فعال شد.
جنگنده‌های ناتو به منطقه اعزام شدند. هنوز جزئیات بیشتری منتشر نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72012" target="_blank">📅 00:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72011">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e699259b.mp4?token=hdmdTH2-cNstkLIJh8Zo7VxVAwaHF0ffEnAHKhXNC1YhMkxJ4vHFF5sM6rU-3zE5gbVZTmUFhb-6OfWYIFZID4-gKzJTkOTzZd4NgjaFNRS6Z5-uJ04BdHVrkwRT8IOIexJ7Vhu9Hjhojn-jYYDu95C77WRuwZvxZ2mbTG3GnE-FHVU4F99O703QyyHb0Rs3eIu0pUATuHHgrX2kDfGn6-QyZjedSrSxbrNh5Uhik2miqxJQxF0J-Sdn7Lh2jDljlGHvUzztiDF8x5meSzZSDVonMMdZFCOO-tOCHbutesvkPqoJNOUEH-hQwWESIOiWcdYbbBg6dHIVi7saHJhZxk5dO1calg_KtGoDQWttmejMjm1wtyzF5kdef7Fx7aGYsMLP7SmFv6Bg6BCs4g_5DFRNgoR7NYNrbV5iypVSkvaNoc5EgL9YbJz4zNcS1UqfwTCp-hiAuxPxlWKit6RVD51_soNlJl0b9REvipuGagNL5sFG7KFd_w7DsfnXLrfrDF0N3ka0UcMpiXpua7ksKbyrtwuMwWJZlo8UKHl1D0jJ1UV2ZbWGxHk8bRKDku2opgd4HaDTHcpC1ljEdrFuBE3Zr3cLpC7rQ_uCMqqxvcoaGUsgnnXd76dVcW5LWBMN_9F9u82x1-qbFmIXDXSY6p-2zDJ8bifLSjimYKVMhY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e699259b.mp4?token=hdmdTH2-cNstkLIJh8Zo7VxVAwaHF0ffEnAHKhXNC1YhMkxJ4vHFF5sM6rU-3zE5gbVZTmUFhb-6OfWYIFZID4-gKzJTkOTzZd4NgjaFNRS6Z5-uJ04BdHVrkwRT8IOIexJ7Vhu9Hjhojn-jYYDu95C77WRuwZvxZ2mbTG3GnE-FHVU4F99O703QyyHb0Rs3eIu0pUATuHHgrX2kDfGn6-QyZjedSrSxbrNh5Uhik2miqxJQxF0J-Sdn7Lh2jDljlGHvUzztiDF8x5meSzZSDVonMMdZFCOO-tOCHbutesvkPqoJNOUEH-hQwWESIOiWcdYbbBg6dHIVi7saHJhZxk5dO1calg_KtGoDQWttmejMjm1wtyzF5kdef7Fx7aGYsMLP7SmFv6Bg6BCs4g_5DFRNgoR7NYNrbV5iypVSkvaNoc5EgL9YbJz4zNcS1UqfwTCp-hiAuxPxlWKit6RVD51_soNlJl0b9REvipuGagNL5sFG7KFd_w7DsfnXLrfrDF0N3ka0UcMpiXpua7ksKbyrtwuMwWJZlo8UKHl1D0jJ1UV2ZbWGxHk8bRKDku2opgd4HaDTHcpC1ljEdrFuBE3Zr3cLpC7rQ_uCMqqxvcoaGUsgnnXd76dVcW5LWBMN_9F9u82x1-qbFmIXDXSY6p-2zDJ8bifLSjimYKVMhY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هلندی ها به این شکل پرچم فلسطین رو از دیوار کشیدن پایین
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72011" target="_blank">📅 23:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72010">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39a7c63375.mp4?token=mWNruglmY7bRSFUCwXuYKNgmouS5J3CP_tRDsRS3LnQeCwhYHdhDlLG6oFPYGP_wrBf2t_mSV5lCMxgeBM5sfLlWqxnweZm-Zoe7fwfnr_k8OfkjHIPQ0_w_Co9qjwVUhaJXA6WJySzqfaxVRVZsYtqtXiRyFGwTLnEHCoKeBY-fwTNJ2eRn7-Jd8sPPi2Fzmt7xVnZM_A9pqqkJE8p5i2r2GiGFR_arEi81V0l0-13phQCa-cf70PGyhy9pTW_sVBXi-q9Z5Wwc1etuxQTX9oG9wbyNlC_ecR8BHGv7_98Lj6BQo2_tyJZGvF8qnUlQAlkCFCTz53v5yXxAUB2pBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39a7c63375.mp4?token=mWNruglmY7bRSFUCwXuYKNgmouS5J3CP_tRDsRS3LnQeCwhYHdhDlLG6oFPYGP_wrBf2t_mSV5lCMxgeBM5sfLlWqxnweZm-Zoe7fwfnr_k8OfkjHIPQ0_w_Co9qjwVUhaJXA6WJySzqfaxVRVZsYtqtXiRyFGwTLnEHCoKeBY-fwTNJ2eRn7-Jd8sPPi2Fzmt7xVnZM_A9pqqkJE8p5i2r2GiGFR_arEi81V0l0-13phQCa-cf70PGyhy9pTW_sVBXi-q9Z5Wwc1etuxQTX9oG9wbyNlC_ecR8BHGv7_98Lj6BQo2_tyJZGvF8qnUlQAlkCFCTz53v5yXxAUB2pBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدر این پسر رفته تو اتاقش سیگار پیدا کرده
و پسره هم این شاهکار رو خلق کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/72010" target="_blank">📅 22:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72009">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ مراسم افتتاحیه (بریدن روبان) پد جدید بالگرد کاخ سفید را برگزار کرد، اما به دلیل غلبه صدای بالگرد بر فضای مراسم، سخنان او اصلاً شنیده نمی‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72009" target="_blank">📅 22:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72008">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05f4ea7396.mp4?token=FyreOsYmwtapTf9Jlz4HsdzJZyti2lpuTlsLRb8k20wx8CLU_y_mGy1JMBZDmZkr-XdChIWwKyK6N3G-rZHV5XsqOVF-8Q35DWZsMYgg_kwrfJjZpSKB2tYdIiUPu5MtpDeMu2f3FgJWTWJEeJzJyLekq16Mmp4qp4y7LDSwr8rwA6kbvwJnm4Hqo_Hbz4dsScNMT2IicBsIvqRfDfX7Zb-k59_BC_jn2-PUikD9e8tQb_8jOt06xgGZYbT-hXgEwngI-bt46A3OUl4fSlLZZA0uBEcc4K6_HBD3_9VzIOvB7-1-lCovr7mFVKp0gAQC0vCW6z52i-wb355C8XU7Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05f4ea7396.mp4?token=FyreOsYmwtapTf9Jlz4HsdzJZyti2lpuTlsLRb8k20wx8CLU_y_mGy1JMBZDmZkr-XdChIWwKyK6N3G-rZHV5XsqOVF-8Q35DWZsMYgg_kwrfJjZpSKB2tYdIiUPu5MtpDeMu2f3FgJWTWJEeJzJyLekq16Mmp4qp4y7LDSwr8rwA6kbvwJnm4Hqo_Hbz4dsScNMT2IicBsIvqRfDfX7Zb-k59_BC_jn2-PUikD9e8tQb_8jOt06xgGZYbT-hXgEwngI-bt46A3OUl4fSlLZZA0uBEcc4K6_HBD3_9VzIOvB7-1-lCovr7mFVKp0gAQC0vCW6z52i-wb355C8XU7Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس:
ماه نوامبر پیشِ رو، لحظه‌ای سرنوشت‌ساز است؛ یا در برابر این دیوانگی می‌ایستید و یا با آن همراه می‌شوید. و ما قصد داریم در برابر آن بایستیم و با آن مبارزه کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72008" target="_blank">📅 21:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72007">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9de7ae59a.mp4?token=ANCF9JV5XU_nH2bXOIdWdiiBolBaXCf_0fc77otJCagXOIy58sCWcp_UsnCs9XN6KzsL3-zbcJ5j2fhTF_NbKdUye7CRdVLuQaJbK7WkHuW7QLh5q88XKsv2GD3qJ6VOsxymoNfH2mzOJvZhSDMVbUb9cWLNFfPCRfZPFvHFu21lyhPXUBsZOHrCbzgX-1NeGfy_kAQDpkz6Xw6sB_EPOS9STApyo0VC5UufwQKu2-j54o4QJjy-22R2GTEt6Rt46bJlolYYwr1vkm6YquWVjx4o_5oEcIhcWBeBX4oqKT-pgfBrEazgu9UuIjZyaB1OoY7stpV9VFlz-J9z2b7Mww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9de7ae59a.mp4?token=ANCF9JV5XU_nH2bXOIdWdiiBolBaXCf_0fc77otJCagXOIy58sCWcp_UsnCs9XN6KzsL3-zbcJ5j2fhTF_NbKdUye7CRdVLuQaJbK7WkHuW7QLh5q88XKsv2GD3qJ6VOsxymoNfH2mzOJvZhSDMVbUb9cWLNFfPCRfZPFvHFu21lyhPXUBsZOHrCbzgX-1NeGfy_kAQDpkz6Xw6sB_EPOS9STApyo0VC5UufwQKu2-j54o4QJjy-22R2GTEt6Rt46bJlolYYwr1vkm6YquWVjx4o_5oEcIhcWBeBX4oqKT-pgfBrEazgu9UuIjZyaB1OoY7stpV9VFlz-J9z2b7Mww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس:
این انتخابات میان‌دوره‌ای، رقابتی است میان کسانی که معتقدند این کشور باید آینده‌ای داشته باشد و کسانی که ترجیح می‌دهند شاهد نابودی آن و بازسازی‌اش از پایه باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72007" target="_blank">📅 21:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72006">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0543c701.mp4?token=mwWrvQXsdQf4HUy_8PoiKBrwSk40e-Ga60UvkB4S0KuAWcFNcuqyxBQMSoieC9On8ZHqUeIvzqDCMzYdr2uqdc_2nZ0eoajHBFhFlsr1bTK302mai6vi6m7Q2R9kpCVll-8dzniHhvTk7njBNmZLhr-413imALXN7yVLFLKRwQDtk_oQ8MVhbddYJhO8CtfMVFY_LJm0I7IBvcgMwzkVAmCvy8KZNjA_7IDNPXKXGF1DPGBNZFR13qzBgGmnzLsUUUGrnqkwAtJDXB9eb1is0uFLur4U4Rk9h1PKnGr_hx77Ux7SKciWWQVW7JExMVs60T-lu-UUsbIVAvHQ5sAMJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0543c701.mp4?token=mwWrvQXsdQf4HUy_8PoiKBrwSk40e-Ga60UvkB4S0KuAWcFNcuqyxBQMSoieC9On8ZHqUeIvzqDCMzYdr2uqdc_2nZ0eoajHBFhFlsr1bTK302mai6vi6m7Q2R9kpCVll-8dzniHhvTk7njBNmZLhr-413imALXN7yVLFLKRwQDtk_oQ8MVhbddYJhO8CtfMVFY_LJm0I7IBvcgMwzkVAmCvy8KZNjA_7IDNPXKXGF1DPGBNZFR13qzBgGmnzLsUUUGrnqkwAtJDXB9eb1is0uFLur4U4Rk9h1PKnGr_hx77Ux7SKciWWQVW7JExMVs60T-lu-UUsbIVAvHQ5sAMJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو از آواز خوندن یه مرد ژاپنی خیلی وایرال شده به اکسپلور ایرانیا نفوذ کرده.
و حالا کامتای شاهکار ایرانیا:
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72006" target="_blank">📅 21:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72005">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a929447dff.mp4?token=gp8lfzS19qxjKr9NjUFsGlV8eXS2zRo8uJkTediYVwQOL1MKOEVWn96uGdLy3aG0skmMb3yNvJF90LJEIcEsEMc0w3bQmr34Ya8BkcP2qceXPXMh8rmoTiScHb-FBD_w8qrBqZ_WvMraMPkt1XFziYjLjAvwm5leTLWMLGNmno_qkM43Su0fp5WsS8ODSMKKN4_jzZ-uR5geN35y7lOAb4qFNCIbODOFU_2m67Icnctm3cp_1wxSh28k9nAg3laEYsVQMVpQyNhzp7WZI8yi-Ceol2msffXBCen5fcozKI5A6RlgkgBvENSdxEr8fKaUkok15MAX7FpJIXGv6_biTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a929447dff.mp4?token=gp8lfzS19qxjKr9NjUFsGlV8eXS2zRo8uJkTediYVwQOL1MKOEVWn96uGdLy3aG0skmMb3yNvJF90LJEIcEsEMc0w3bQmr34Ya8BkcP2qceXPXMh8rmoTiScHb-FBD_w8qrBqZ_WvMraMPkt1XFziYjLjAvwm5leTLWMLGNmno_qkM43Su0fp5WsS8ODSMKKN4_jzZ-uR5geN35y7lOAb4qFNCIbODOFU_2m67Icnctm3cp_1wxSh28k9nAg3laEYsVQMVpQyNhzp7WZI8yi-Ceol2msffXBCen5fcozKI5A6RlgkgBvENSdxEr8fKaUkok15MAX7FpJIXGv6_biTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید حساب کاخ سفید در پلتفرم ایکس:
چیزی در راه است. منتظر باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72005" target="_blank">📅 20:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72003">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ad0122e6.mp4?token=IrU5ss7i0eZFSfctcPMZuaA5fU8T3HIT6V9WsBHFN5SnzCR6mOgue6NrxEGtjgc_jkwSdekXQjqJy19oVWe34GGRMI7i0gy7M_HntBHlx1QO4Mm_VRYmuu4YzfaA9Jkz5XIEJb8o-Ck409sWVvLGxu20p8FaVSTZCBXHcB2bcDk3NypOApTiAxEaLHjpD3OhFAoHsKT5cRrxT917hWU417erBcbpnouPZoWdMHnsKdDxOhKAldq9huyTATtVpP5ywz-htqQbysEr3ZTzq-_XWRyUf6RPw1Yh5uGvBgEvfZAryBkLYFoLA4DNcW6PQoHg9C4-NeY96YdQH98KbOOEcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ad0122e6.mp4?token=IrU5ss7i0eZFSfctcPMZuaA5fU8T3HIT6V9WsBHFN5SnzCR6mOgue6NrxEGtjgc_jkwSdekXQjqJy19oVWe34GGRMI7i0gy7M_HntBHlx1QO4Mm_VRYmuu4YzfaA9Jkz5XIEJb8o-Ck409sWVvLGxu20p8FaVSTZCBXHcB2bcDk3NypOApTiAxEaLHjpD3OhFAoHsKT5cRrxT917hWU417erBcbpnouPZoWdMHnsKdDxOhKAldq9huyTATtVpP5ywz-htqQbysEr3ZTzq-_XWRyUf6RPw1Yh5uGvBgEvfZAryBkLYFoLA4DNcW6PQoHg9C4-NeY96YdQH98KbOOEcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره‌ای حداقل ۲۵ تانکر نیروی هوایی ایالات متحده را در پایگاه هوایی العدید در قطر نشان می‌دهد که بزرگترین حضور تانکرها در آنجا از زمان آغاز جنگ ایران در فوریه است.
این تانکرها در ابتدا به دلیل تهدید حملات موشکی ایران از آنجا خارج شدند و حدود ماه ژوئن شروع به بازگشت کردند.
برخلاف پارکینگ تانکرهای بسیار متراکم مشاهده شده در پایگاه هوایی شاهزاده سلطان در عربستان سعودی، به دلیل اقدامات احتیاطی مداوم علیه حملات ایران، هواپیماها همچنان به طور گسترده در سراسر محوطه پایگاه پراکنده هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72003" target="_blank">📅 20:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72002">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f71861d0c.mp4?token=ng9P0AVe2ORmhhpexhq4WpS9tGHJSRFIr_vDMe-4lebN8DomdOFQ0dcIhVh3cShYCfbb4kNv1k51VTeTu07e7njD8XPqxwK9EJToEzrtmffp2MIR4Uodm38ZtZ1VfrJRsnpq3ZwqJTz5bYv01c-7LebuAbSnHUHjZ5uoKBTvJCLzPfpNHGE2eKIQFKsDDBnBJr0H913_QZ_ymUHzaF0J8uTeBwZKGe5LsKmekLZ-i9Hcm2cBkYy1nBMtMUbBl1R09OL1Th2488QPkboMdajyMi0Oxn8dWRxFHV5uIuUyC5PoIZx2COSJD9Sst-NXjZv7VHBQdskhoffo88G5_TZbfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f71861d0c.mp4?token=ng9P0AVe2ORmhhpexhq4WpS9tGHJSRFIr_vDMe-4lebN8DomdOFQ0dcIhVh3cShYCfbb4kNv1k51VTeTu07e7njD8XPqxwK9EJToEzrtmffp2MIR4Uodm38ZtZ1VfrJRsnpq3ZwqJTz5bYv01c-7LebuAbSnHUHjZ5uoKBTvJCLzPfpNHGE2eKIQFKsDDBnBJr0H913_QZ_ymUHzaF0J8uTeBwZKGe5LsKmekLZ-i9Hcm2cBkYy1nBMtMUbBl1R09OL1Th2488QPkboMdajyMi0Oxn8dWRxFHV5uIuUyC5PoIZx2COSJD9Sst-NXjZv7VHBQdskhoffo88G5_TZbfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مربی بدن‌سازی:
خیلی از جوونا هستن باشگاه ثبت نام میکنن ولی تو تایم باشگاه، میرن پارک با دوستاشون مواد میکشن
وقتی هم که خانوادشون بهشون میگه چرا لاغر شدی و قیافت اینجوری شده بهشون میگن رژیم گرفتیم و طبیعیه
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72002" target="_blank">📅 19:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72001">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e4e4fa6b9.mp4?token=XLiWn-Y3E4YPv9yIOJvW4Uk9R1LVetW7E6uMUOk4j-1T04UOpgPtGQh3vN5TIcI0YzD23cNwMHxLl_-cR9kxL2jz6vgivsNeMmmVkfX5NM5HSUsNcihwfRPLkosrNvi8cYYRzobGEb09JQdPbOgiwSiYp1v1By0NF8vROREjiUqHTcgc8rgslbJLSz8usC39A5vcL6xDBA5dnMjeaU4ZKpHDHEv9mBWTYWYDlEuwQdxYI4xhZW6-vC-oPSMCziMB7Xk_fLSJMhr2RWKJ0wg46ccocr9OJeQHwnwSCYWFOt8SpzJ2gdIEm9Uo3J91BvP0MWx3nNFtKxMRxzB5hbhpSxM39A8qW1-Juei3WnbK40y3KNYu6hd1n8d27acQZ9h6fadRlNyxTbi1QyU2Fw6I6WXhS5R32rQHGCAx0NZq2WGz6u6bLMgUHB_dkhIH4Owz0OCZgF2JCYELrR9s1XVZ-GDyotE8G6LoyMRdHQl0aTEFH7buk31b2UQZs1gwzvliQXUkrEKAfe4TcMLWHIqXVz1Lz_R_5n-cl2ueyAzXltmI-kd0Fwei63TsLezY9PaCskhKRJRliipVuSqHoz17cuhM4QOeXffNmPlWZQwLWcL3V03w7a0d-u-knmyo4b6hSHanxIAl_pewkTD7bqczUHskuLRJrTxIDtFwnjNr_Rs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e4e4fa6b9.mp4?token=XLiWn-Y3E4YPv9yIOJvW4Uk9R1LVetW7E6uMUOk4j-1T04UOpgPtGQh3vN5TIcI0YzD23cNwMHxLl_-cR9kxL2jz6vgivsNeMmmVkfX5NM5HSUsNcihwfRPLkosrNvi8cYYRzobGEb09JQdPbOgiwSiYp1v1By0NF8vROREjiUqHTcgc8rgslbJLSz8usC39A5vcL6xDBA5dnMjeaU4ZKpHDHEv9mBWTYWYDlEuwQdxYI4xhZW6-vC-oPSMCziMB7Xk_fLSJMhr2RWKJ0wg46ccocr9OJeQHwnwSCYWFOt8SpzJ2gdIEm9Uo3J91BvP0MWx3nNFtKxMRxzB5hbhpSxM39A8qW1-Juei3WnbK40y3KNYu6hd1n8d27acQZ9h6fadRlNyxTbi1QyU2Fw6I6WXhS5R32rQHGCAx0NZq2WGz6u6bLMgUHB_dkhIH4Owz0OCZgF2JCYELrR9s1XVZ-GDyotE8G6LoyMRdHQl0aTEFH7buk31b2UQZs1gwzvliQXUkrEKAfe4TcMLWHIqXVz1Lz_R_5n-cl2ueyAzXltmI-kd0Fwei63TsLezY9PaCskhKRJRliipVuSqHoz17cuhM4QOeXffNmPlWZQwLWcL3V03w7a0d-u-knmyo4b6hSHanxIAl_pewkTD7bqczUHskuLRJrTxIDtFwnjNr_Rs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس درباره ایران:
ما کاملاً واقفیم که قیمت انرژی به دلیل اقدامات تروریستی ایران علیه کشتیرانی بین‌المللی، افزایش یافته است.
ما تمام تلاش خود را به کار می‌گیریم تا ضمن مهار این قیمت‌ها، در این فاصله باری از دوش مردم آمریکا برداریم.
یکی از اقداماتی که ترامپ درباره آن صحبت کرده، تشویق برخی ایالت‌ها به کاهش یا حذف مالیات بنزین برای مردم آمریکا است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72001" target="_blank">📅 18:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72000">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8571b32102.mp4?token=ZyGldENjvHTvemq7_wyUNNviXkobT1a4vtn7tWlB0XHNJeCiIN9bhrdQ6KSOUKFgwHuITSiZxVbjvVCxIKAuOAqBid6MyPUS4XVnPblFxgcMtXebT2rc4K4n268CRVCcY49atJ9AnX1t0Ol79O-Hkhqqcyt5duJWxFYqgvDpmQEUymjjK6w_BFI1woPTTwQVfGOcNlm2KonTlr4NnjgcRuyaba2PGJbXIqsOwxy5O_ohauI2EvsmbOtFT0R5pWkc_Y0LHB2NLuRiS48Oeo5dDrWlcTOR3CyWbChRRfWdbrMdKEneePSfHccGBb76qVMjKv4uffYzjBERNVmWneU2mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8571b32102.mp4?token=ZyGldENjvHTvemq7_wyUNNviXkobT1a4vtn7tWlB0XHNJeCiIN9bhrdQ6KSOUKFgwHuITSiZxVbjvVCxIKAuOAqBid6MyPUS4XVnPblFxgcMtXebT2rc4K4n268CRVCcY49atJ9AnX1t0Ol79O-Hkhqqcyt5duJWxFYqgvDpmQEUymjjK6w_BFI1woPTTwQVfGOcNlm2KonTlr4NnjgcRuyaba2PGJbXIqsOwxy5O_ohauI2EvsmbOtFT0R5pWkc_Y0LHB2NLuRiS48Oeo5dDrWlcTOR3CyWbChRRfWdbrMdKEneePSfHccGBb76qVMjKv4uffYzjBERNVmWneU2mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس درباره ایران:
با وجود اینکه ایرانی‌ها هر روز برای کشتی‌ها ایجاد وحشت می‌کنند، ما همچنان شاهد جریان حجم قابل‌توجهی از نفت و گاز از طریق تنگه هرمز هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72000" target="_blank">📅 18:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71999">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0DAEV3HDr3NxrQ3FUGxcu6op5XFKKRlFLBl07XRaPbbKv-_GVJgYoa5fsjN-dmioLIPcW9MyzC7_1-UIcAYYUZ7v76RY6sPZCw97dAO9cKjxXLuHHfk-gwGiWD3JQwYG3TdQQbFQqzTOtgjXtgRi38SoT5ptCh6HHvRAd4IVsU5WRaZlD82g-p9zsSxMVuShnkT8GpoHZExGDOYCwJ6MFe_qLq0Hh8NA3aYl78jsL7C8CZnwTlfA7qp9W_xpxzOe_uEW6FcYElcx2KGelM_yU54HAA3RgdryA5GnK1Ps8W1-3sFvGwFGMeoTtoZarSrLidLjur2273CeTDw9nFXgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای دو انفجار از سمت تنگه هرمز شنیده شد.  @News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71999" target="_blank">📅 18:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71998">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9e105be9.mp4?token=egxDnwRF5WF4_Ta2e-49_EMfK-yiRUsMrkD_nRBBodb-HS91-sN57-mMDbM56JGu5ak23B3PWVYTPzAfTLhgbu5vtLGG9Du4uY-8pTmkvIyvP0aRUNVfANDAj2YvGKuvwSs9juEHuts_HZlvoJm0-fqrXfa61DE-CKFhuqs9ZLAdefmy7ErKVYSsi0cSZynDNJAoP5p02LX_QtEdUjIJdnThSnWw_sqoweceUhNQ_BzSyiYIZ5GOseQJbzdol9AKo3V-bMMAeEV5mXnmCO2Xc2pKIGHZe4SIKWkQ_FDmQk7ni9LFu_19s4kAh7FAzZIA4GdR9n4r-KjFdfrrtkRPTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9e105be9.mp4?token=egxDnwRF5WF4_Ta2e-49_EMfK-yiRUsMrkD_nRBBodb-HS91-sN57-mMDbM56JGu5ak23B3PWVYTPzAfTLhgbu5vtLGG9Du4uY-8pTmkvIyvP0aRUNVfANDAj2YvGKuvwSs9juEHuts_HZlvoJm0-fqrXfa61DE-CKFhuqs9ZLAdefmy7ErKVYSsi0cSZynDNJAoP5p02LX_QtEdUjIJdnThSnWw_sqoweceUhNQ_BzSyiYIZ5GOseQJbzdol9AKo3V-bMMAeEV5mXnmCO2Xc2pKIGHZe4SIKWkQ_FDmQk7ni9LFu_19s4kAh7FAzZIA4GdR9n4r-KjFdfrrtkRPTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه پاسداران ویدیویی منتشر کرد که مدعی است لحظه رهگیری و انهدام یک پهپاد MQ-1 ارتش آمریکا در صبح امروز را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71998" target="_blank">📅 18:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71997">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71997" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71997" target="_blank">📅 18:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71996">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vk77j44lceswRsSi7tV9ZP_OXnreWE2xEGGnSlB_vRNp8MvvBK3IIFmcRr29qpYAfGdcDphE5WQ_jQgFgiRmu_WmbA6QeZzuH3cLsVQjtA_GF277pHfdjxy_EX2VLKjm9N4HDBceu7u8ZlrT5gmcznfGQOrH-EIXJmJbB8b5RqBQ4u3BTUv1bMQHylOEJpFhf-6qs-USQPHqCvQWFnV56fwxb3R2xB_DZozYgYwJq0UONqBu6mE5FCVyOEVhVAXmLXijooGJ7ic7xPi85ifeJZW_A1Ce9GAII7mD8Clw7_8F-nAYtNHrWqGxzhfVW0sQIWvWqR0zFMSD9_L5iS-MFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71996" target="_blank">📅 18:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71995">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5dd9ae6ba.mp4?token=gt7ga9crvMfETl163JK8I8CuSoxTK8BFGE9_gLcn70KjLFs0_y-YML0YJtyDt0xZf5NCWxLAVBKzhdiBe4chF3JcY_NiNbeghh_4tEm_azysd-TTHMam4PqiWjicNqzJgPyrUA3a-kZKWYjRxNkEbRHoU0p-IfueMxjizV8dVYnSpng8nELO-RucxqEj-_TuQY-0cpljECdiJVvmAYbtBxJXk66wT88DsmG_qtTdTf1-iV2aN56HuKNsQCHJ0RUQeGYPDZV_A51ni8iWSqfei3TduqqQZ7dNEy0FJz7y8L4O2qBX8khvn-EvyXUYcZ0pP-UYNotP7zvslqZgRZwN-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5dd9ae6ba.mp4?token=gt7ga9crvMfETl163JK8I8CuSoxTK8BFGE9_gLcn70KjLFs0_y-YML0YJtyDt0xZf5NCWxLAVBKzhdiBe4chF3JcY_NiNbeghh_4tEm_azysd-TTHMam4PqiWjicNqzJgPyrUA3a-kZKWYjRxNkEbRHoU0p-IfueMxjizV8dVYnSpng8nELO-RucxqEj-_TuQY-0cpljECdiJVvmAYbtBxJXk66wT88DsmG_qtTdTf1-iV2aN56HuKNsQCHJ0RUQeGYPDZV_A51ni8iWSqfei3TduqqQZ7dNEy0FJz7y8L4O2qBX8khvn-EvyXUYcZ0pP-UYNotP7zvslqZgRZwN-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک: این آینده‌ای است که آن را به واقعیت تبدیل خواهیم کرد
ایلان ماسک با انتشار ویدیویی آینده‌نگرانه از تعامل انسان و ربات، فناوری‌های پیشرفته و سفرهای فضایی، چشم‌انداز خود از آینده را به تصویر کشید و نوشت: «این آینده‌ای است که آن را به واقعیت تبدیل خواهیم کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71995" target="_blank">📅 17:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71994">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">صدای دو انفجار از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71994" target="_blank">📅 16:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71993">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f918318e4.mp4?token=HHiaj6IZ-CdaGxIyp4R8OdeqRuKJB_KVVpxsIfyhXZfjMzlDLfsQVqijUSdOQYy3ULshtOyWF2ZirdKHXT79Gh_YFUcgjqQW5uMVOMM-saDD11wpGHEZrkzIeL9FXCoWVQZ7dkT9VkEDdU7uX4kKt8OECQgwstHlF2Rh9HZ8vsEiGsKRxMBaDnRSsbJ5L6bneZ--QXOsJfdb48K1bMa034C_HhDeh4q4XYhxCRoJl10lj50n_sG4_a1PGkOybcSo_Z7CIyUT3sPbGHyvd-kCy_qlB3_62Q63OVOPpbuW1hpwI9x1O3N8f6TeEmaMYldICNZkd7ScUw1Eok4esp2VMTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f918318e4.mp4?token=HHiaj6IZ-CdaGxIyp4R8OdeqRuKJB_KVVpxsIfyhXZfjMzlDLfsQVqijUSdOQYy3ULshtOyWF2ZirdKHXT79Gh_YFUcgjqQW5uMVOMM-saDD11wpGHEZrkzIeL9FXCoWVQZ7dkT9VkEDdU7uX4kKt8OECQgwstHlF2Rh9HZ8vsEiGsKRxMBaDnRSsbJ5L6bneZ--QXOsJfdb48K1bMa034C_HhDeh4q4XYhxCRoJl10lj50n_sG4_a1PGkOybcSo_Z7CIyUT3sPbGHyvd-kCy_qlB3_62Q63OVOPpbuW1hpwI9x1O3N8f6TeEmaMYldICNZkd7ScUw1Eok4esp2VMTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛اسکات بسنت درباره ایران:
در ۲۳ سپتامبر، فعالیت تمام شرکت‌های هواپیمایی ایران در سراسر جهان متوقف خواهد شد.
چگونه این کار را انجام می‌دهیم؟
اگر آن‌ها فرود بیایند، شما نمی‌توانید به آن‌ها سوخت یا خدمات فرودگاهی ارائه دهید و نمی‌توانید به آن‌ها بلیت بفروشید؛
وگرنه از سیستم دلاری کنار گذاشته خواهید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71993" target="_blank">📅 16:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71992">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">#مهم
؛اسکات بسنت وزیر خزانه‌داری آمریکا در گفتگو با CNBC: فعالیت ایرلاین‌های ایران از ۲۳ سپتامبر(اول مهر) با محدودیت های جدی مواجه خواهد شد.
اسکات بسنت، وزیر خزانه‌داری آمریکا، روز دوشنبه ۲۱ سپتامبر اعلام کرد ایالات متحده از ۲۳ سپتامبر (اول مهر) با اعمال تحریم‌های ثانویه علیه ارائه‌دهندگان خدمات هوانوردی، در پی متوقف کردن فعالیت بین‌المللی ایرلاین‌های ایرانی است.
بسنت گفت شرکت‌هایی که به هواپیماهای ایرلاین‌های ایرانی سوخت‌رسانی کنند، خدمات فرودگاهی ارائه دهند یا برای آنها بلیت بفروشند، ممکن است با خطر قطع دسترسی به نظام مالی و دلاری آمریکا مواجه شوند.
این اظهارات پس از آن مطرح شد که وزارت خزانه‌داری آمریکا در ۸ سپتامبر، ۳۶ فرد و نهاد مرتبط با بخش هوانوردی ایران، از جمله ۲۷ ایرلاین ایرانی، را تحریم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71992" target="_blank">📅 16:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71990">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/939066a7e6.mp4?token=tmlfZFwmGc-I8vxcFLZmwynI3qkUM1yjrBkh4hVJ6_HjfxA6HPXzwNemT3FHbKxI-IDscG3Y7tLd3jGu70Hwovfljtp0aFGWLWtqsNQNBOF3xGC361r3_apWguIO4a1x5r1EIjJOTp9nQJJGEa1jmclBuZ-_qW_OqiVHkwxRLuDYxMzPvbLaaZ4Ix1zMzvcTzgDtyRaos4hNwu-jfdZ08hT4nf11HwFJnCxklGJhKzwQTAecfPYG_78tvdZeKc0-csbLlXXReGB1GdErInuDfJSe4ASK32sYYIzCQS8tOw5Zr2K2yXPAz-71KXW5a9jZPMADzFoAG7ivK68JKlLv9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/939066a7e6.mp4?token=tmlfZFwmGc-I8vxcFLZmwynI3qkUM1yjrBkh4hVJ6_HjfxA6HPXzwNemT3FHbKxI-IDscG3Y7tLd3jGu70Hwovfljtp0aFGWLWtqsNQNBOF3xGC361r3_apWguIO4a1x5r1EIjJOTp9nQJJGEa1jmclBuZ-_qW_OqiVHkwxRLuDYxMzPvbLaaZ4Ix1zMzvcTzgDtyRaos4hNwu-jfdZ08hT4nf11HwFJnCxklGJhKzwQTAecfPYG_78tvdZeKc0-csbLlXXReGB1GdErInuDfJSe4ASK32sYYIzCQS8tOw5Zr2K2yXPAz-71KXW5a9jZPMADzFoAG7ivK68JKlLv9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگنده نسل جدید J-36 چین به پروازهای آزمایشی خود در طول روز ادامه می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71990" target="_blank">📅 16:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71989">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34a5f81c8.mp4?token=RsnB1fY7OjhVj4Q5lC7UH-uBP-pMw31kd6cEjH3o9oUkLtKIjZ7SizHM_VEZn3lQz9STEm3WhLdViMWLX8ZRePOMCQLbqC5-Ff57bbatFZEf_8j6JzkimyKl2guj-_1yiZF1ksMP0SigEl6D41BqwIibn7myQKDHXhSYS_x9EzAhxoUReXcFkUxUW6LMBS0u-cXpV0z4dT_b9085fFMfSTQJSik5hf9m1D-yKv1wore9TWv9Hho9KSJqBXni-6pAWaBQgXM9GcRMwWZQXtZoyoKeQaStONa7pvz3ffSzhgQ2Qf1dTPJQVz_yIIyQER4NNqwTPgmNfcJPb103Rqtzsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34a5f81c8.mp4?token=RsnB1fY7OjhVj4Q5lC7UH-uBP-pMw31kd6cEjH3o9oUkLtKIjZ7SizHM_VEZn3lQz9STEm3WhLdViMWLX8ZRePOMCQLbqC5-Ff57bbatFZEf_8j6JzkimyKl2guj-_1yiZF1ksMP0SigEl6D41BqwIibn7myQKDHXhSYS_x9EzAhxoUReXcFkUxUW6LMBS0u-cXpV0z4dT_b9085fFMfSTQJSik5hf9m1D-yKv1wore9TWv9Hho9KSJqBXni-6pAWaBQgXM9GcRMwWZQXtZoyoKeQaStONa7pvz3ffSzhgQ2Qf1dTPJQVz_yIIyQER4NNqwTPgmNfcJPb103Rqtzsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرکی به نام صدا و سیمای جبلی!
با تراکتور اومده وسط برنامه؛ میگه میخوام باهاش اسرائیل رو شخم بزنم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71989" target="_blank">📅 16:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71988">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3yz6TJx3imrnJkqnzQdmgSmbvkviZM6KMzj49Tri5JbAbOenN0teO2auZ9OdKv8MJdGhy1MjV0Wp-VeskcouqALrPptu64dcHwkjYTlqmqL5Ek5b2wdf6rrIJg5QQNnKQMwesunDvqT3WYXxvZ02c3tPtFFcQ6c2XbexnJadtMFtMWlXZvC3D9xSBk9lI5p2MhKfxTCMTvfrEOFq224lxAwNxrM63nlx0Hgvxa-CP9qazwAFs_y7QjIb7_Y5Xn5qOV-X44s2RutopDjeZM3ePpN5xxrZDC1GoUDz6JLmqVpy4HmUWk91NTmY_ga2rryc3ZB05MprvGD0QkG8yEu6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس:انتقال سهمیۀ بنزین به کارت بانکی از مهر در ۵ استان اجرا می‌شود؛
سخنگوی کمیسیون انرژی مجلس:
این طرح تاکنون ۲ مرتبه در چند جایگاه به اجرا درآمده و قرار است از ابتدای مهرماه، در پنج استان کشور به‌صورت آزمایشی آغاز شود.
طرح انتقال سهمیۀ بنزین به کارت بانکی به‌تدریج تا پایان سال در سراسر کشور اجرایی خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71988" target="_blank">📅 15:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71987">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86993a4fad.mp4?token=PAQgno5kYKplMgsr3c5GWlBuuh5Sf6upykyNpnIUtv7Rzeu0XfxDetuLQV7qgv_Vcvzpz6RtxeuTnxHs-M_80dmKJecS1TRXid3GxU8Ml6uKPXyEd9XzeNq3fp00xHE0g910ffdvQH7_BQHVeri-2QCAsKGYOkOzn2KXogxiO1MpQksdkuDZ7NN7lJikOl6P0w2ZEXfotrAmO6kHK4QvD1aXDOzC41Hsx8gO-xtpBh6o52ZAJ_optSmKoii460V4JGAIka9iFiWJkj92kO-FUO5TkBpHhUJ-wiN8uVYhPCrTFtULDWRShS9j2Q5xJ1rn6n0yidRl0_PvqDfOqjuyIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86993a4fad.mp4?token=PAQgno5kYKplMgsr3c5GWlBuuh5Sf6upykyNpnIUtv7Rzeu0XfxDetuLQV7qgv_Vcvzpz6RtxeuTnxHs-M_80dmKJecS1TRXid3GxU8Ml6uKPXyEd9XzeNq3fp00xHE0g910ffdvQH7_BQHVeri-2QCAsKGYOkOzn2KXogxiO1MpQksdkuDZ7NN7lJikOl6P0w2ZEXfotrAmO6kHK4QvD1aXDOzC41Hsx8gO-xtpBh6o52ZAJ_optSmKoii460V4JGAIka9iFiWJkj92kO-FUO5TkBpHhUJ-wiN8uVYhPCrTFtULDWRShS9j2Q5xJ1rn6n0yidRl0_PvqDfOqjuyIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک خلبان در جریان یک پرواز چهار ساعته بر فراز ایالت های اوکلاهما و آرکانزاس آمریکا، مسیر هواپیمای خود را به شکل چهره مونالیزا ترسیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71987" target="_blank">📅 15:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71986">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzvWLwwk_c7WPzwcVg2q7Gobl0jvudmLbIFDoSTp9J72ldeMJuTjAXLhgtbPCI8x1T-tPAuTeUPru6lRti_-GwGluokpH-CsVsCf7jipMKb3VgSz48_ol744zAqSzEEEKSynfFPh2VKKJRnf1Gn_1GWRX5-PVsU121n0eR2KePgnBBv8wSMfH-5rAGZagSE-VgKBDvlhiu9vKsRnHTClDo2Y2h_pC1F892SOm6rmGi61k7jBv3LJjfiTpOHXq_hsVhnbYA27wRzwwl015ZN0hS538WuuTwOJkjfUgE0emjJaRiBw9uVkTNH1CkgvUmQ-tqFZNuvmmLBYor7KX7wEKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش پولیتیکو، سی‌ان‌ان، ام‌اس ناو و پولیتیکو پس از لغو دسترسی مطبوعاتی‌شان توسط کاخ سفید، از دولت ترامپ شکایت کرده‌اند و استدلال می‌کنند که این اقدام نقض متمم اول قانون اساسی است.
این رسانه‌ها می‌گویند که به دلیل گزارش‌هایشان هدف قرار گرفته‌اند، در حالی که رئیس جمهور ترامپ از این ممنوعیت دفاع کرد و گفت که ملزم به پذیرش رسانه‌هایی که «داستان‌های منفی» منتشر می‌کنند، در کاخ سفید نیست.
انتظار می‌رود درخواست اضطراری از یک قاضی فدرال در واشنگتن دی سی ارائه شود که احتمالاً منجر به جلسات استماع و استدلال‌هایی از سوی دولت در این هفته خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71986" target="_blank">📅 14:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71985">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba57cb4ffa.mp4?token=m8QqeDEQGpBo8JFHieYXTmpAPAdemCUTDD90uvQn4xJwkLhbL3Zg2-Oed80viM2z2lhaZBB7XoNmoWSZiz6Id6XX9jAwWby0x1RRap-hEBIcBQwtmMSUSVYBG4rDodfJsBujkLZNgi4BD5Ql6BmOyDBTtCawtBwNFwfQYAA2B7ndKOpBRgz3U6NvcgIkRCKcARLM7rulBzErAeX5wQE2j0vO8AL_3dxcq0dnRoN2nJAMHxqOOgJxxhoOX3rqrBWu1dorcCIgamV4TK19cPoNHWMMggvOr35g3fO_EF-d1djHtjB8slv8q1IudmJoGvcRtbPjr85tKIsLyuOpE3XjQTM_0hwppdT0eKvrzWbabcAv_XBEkqqyNNrhrhbTWWMDvkkHkPKvS0S4RX3baN2hXIMymK9eaPPCYrkRqnXzCe8-iETQQuzk9xq-qaenGfvWU8X-SeZuzyDf4Nu0rcErhWWRT7f954k5kNk5buSeuTYVTSid4areJBIm3eppNPHcQr-qxTm0V_nAC0h-h94QhPDUIUUF45PAlKpCYr6MP5AK-1UqxDvF4TnGCBESPXbYQzLaB2YVxtLSHFYYDd-9EgnB6tAMHrAHgFl6MI7817BOCHogCQCC90-qZa0OYV87ns0U_OiPaPzC-7yM-DsAfSPs332VZcDWd6rdMpeQdF8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba57cb4ffa.mp4?token=m8QqeDEQGpBo8JFHieYXTmpAPAdemCUTDD90uvQn4xJwkLhbL3Zg2-Oed80viM2z2lhaZBB7XoNmoWSZiz6Id6XX9jAwWby0x1RRap-hEBIcBQwtmMSUSVYBG4rDodfJsBujkLZNgi4BD5Ql6BmOyDBTtCawtBwNFwfQYAA2B7ndKOpBRgz3U6NvcgIkRCKcARLM7rulBzErAeX5wQE2j0vO8AL_3dxcq0dnRoN2nJAMHxqOOgJxxhoOX3rqrBWu1dorcCIgamV4TK19cPoNHWMMggvOr35g3fO_EF-d1djHtjB8slv8q1IudmJoGvcRtbPjr85tKIsLyuOpE3XjQTM_0hwppdT0eKvrzWbabcAv_XBEkqqyNNrhrhbTWWMDvkkHkPKvS0S4RX3baN2hXIMymK9eaPPCYrkRqnXzCe8-iETQQuzk9xq-qaenGfvWU8X-SeZuzyDf4Nu0rcErhWWRT7f954k5kNk5buSeuTYVTSid4areJBIm3eppNPHcQr-qxTm0V_nAC0h-h94QhPDUIUUF45PAlKpCYr6MP5AK-1UqxDvF4TnGCBESPXbYQzLaB2YVxtLSHFYYDd-9EgnB6tAMHrAHgFl6MI7817BOCHogCQCC90-qZa0OYV87ns0U_OiPaPzC-7yM-DsAfSPs332VZcDWd6rdMpeQdF8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر قطر:
از زمان جام جهانی، دیگر روی آرامش را ندیده‌ام.
پس از آن، ماجرای هفتم اکتبر پیش آمد و از آن زمان تاکنون، هیچ‌کس حاضر نیست به ما فرصتی برای نفس کشیدن بدهد.
از همه خواهش می‌کنم؛ ما برای سال ۲۰۲۷ به سالی سرشار از صلح و آرامش نیاز داریم.
لطفاً، ما به کمی استراحت نیاز داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71985" target="_blank">📅 13:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71984">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWfesoMs4ovKMBjc8KEl1VgDdYyj9WMrIt2elbtWl6MbQUhKtHVIwF6dJshWhAIWm2REgsStNzqoZlVHUMSEejAHnGp8DLmWlPPUErR5T5Xv7eyVQrNbqWMFp-FA9lkP6efymNnuIlb7h3QfyGaPgyoefoPAEDQ1BGyjwoiRpUHqDYXqnks-JyK7Q4F7DMoMfvOCrxMbdaLHmsDU_THmy-4-PHn1cmbh1JHNMUnvXL1VoprTIOxutf0buj52YabCNjbYKKcYknnLtZ3wQjQ4XxadlwwKeZSdLCrNP3qVjcQCtXbAvMENAQ25ViLEXr5xrYU0nOKN8RzfAtNRCej7rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
در هشدار شماره ۲۶-۱۴۰ که ساعت ۰۷:۳۰ به وقت هماهنگ جهانی (UTC) صادر شد، گزارش داد که یک نفتکش در حال عبور به سمت داخل تنگه هرمز، مورد اصابت یک پرتابه ناشناس قرار گرفته است. دو تن از خدمه دچار جراحات سطحی شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71984" target="_blank">📅 13:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71983">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ada732dd6.mp4?token=HWAq0sGx3XQ7gk26xi2y7nNgl6KZsR29oytEoR1-Y1-frH90RHUroMQJi68B92ve33GbJQ9wNGwm1fm86LmtygnEUy5A93zydUn1zC90ZJbmna90LF1lh-WUPJ7a1vQLp0DOKbZopR8HXNHwmoivVJKSLIljsdOJF62HOqwjELEjLVpYfpUuCeeNCYqhiBVV2Piogxz8Q31K5aEv4pHRTOvvisdwrj8SzOQxtC8Jyu5w_FGDpwmAF4QiYk-Je776YvK4l6KXgKZkvkKqKwh4UhSamC_9zNv51s9yJ6ODfz3n7QTHbi-qcGvuSF9QhUVn44fnheWxA2PfSCNNefj3bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ada732dd6.mp4?token=HWAq0sGx3XQ7gk26xi2y7nNgl6KZsR29oytEoR1-Y1-frH90RHUroMQJi68B92ve33GbJQ9wNGwm1fm86LmtygnEUy5A93zydUn1zC90ZJbmna90LF1lh-WUPJ7a1vQLp0DOKbZopR8HXNHwmoivVJKSLIljsdOJF62HOqwjELEjLVpYfpUuCeeNCYqhiBVV2Piogxz8Q31K5aEv4pHRTOvvisdwrj8SzOQxtC8Jyu5w_FGDpwmAF4QiYk-Je776YvK4l6KXgKZkvkKqKwh4UhSamC_9zNv51s9yJ6ODfz3n7QTHbi-qcGvuSF9QhUVn44fnheWxA2PfSCNNefj3bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آیا ایران دردسرساز است؟
نخست‌وزیر قطر: کاملاً آشکار است که آن‌ها صلح‌جو نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71983" target="_blank">📅 12:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71982">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0a06bd3e5e.mp4?token=GGSveC5N13zs6KOlDYRLB1Un63PpkFAUh0XemquzBmHeiS1sGYiLT327JPelCJ8xn9ERoiTs4U4eJ2_ixJMcL9Uu2F4bxpklMgTDLqN8r7WDKDJ5otHlSo0e138KaYMvUVue_arQlasPnVfm-RvvlWL-ZezVcjoyLqGLlUTXynaatFY22TJ7o3ZHWPx1wWcUW0iioJIr9Ojb_I0NEHIrXxyl9VU28I6F5oZqa3w4hXuNEiVCKHK_Fzb3FK3-NGLTDLkM4D-Y1vpfrSSMIGGzOI3YiA41bXJr1rB1rdFf5vf0R0FbISG8vzSuJJZyoyF-rPdZk0_WvCLfD_fYapKIKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0a06bd3e5e.mp4?token=GGSveC5N13zs6KOlDYRLB1Un63PpkFAUh0XemquzBmHeiS1sGYiLT327JPelCJ8xn9ERoiTs4U4eJ2_ixJMcL9Uu2F4bxpklMgTDLqN8r7WDKDJ5otHlSo0e138KaYMvUVue_arQlasPnVfm-RvvlWL-ZezVcjoyLqGLlUTXynaatFY22TJ7o3ZHWPx1wWcUW0iioJIr9Ojb_I0NEHIrXxyl9VU28I6F5oZqa3w4hXuNEiVCKHK_Fzb3FK3-NGLTDLkM4D-Y1vpfrSSMIGGzOI3YiA41bXJr1rB1rdFf5vf0R0FbISG8vzSuJJZyoyF-rPdZk0_WvCLfD_fYapKIKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان هم به این شکل زنگ آغاز سال تحصیلی جدید رو به صدا درآورد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71982" target="_blank">📅 12:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71981">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71981" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71981" target="_blank">📅 12:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71980">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THi7wLN16yDHOO9IG9v14cHO-fDDAtSgraeauRZWweDZaHWdQp5e4xwdCKPQCXjKu_5wxV4Kn112IViajfQdGtyfqIcX3xIAAf7bcs9vp_GDQFk4jgJeU7_LuSVMjl49ENEvofoBuOnw4AgsMB-6InAqJJpDDaV3J015Nj76HHs4jdNSzdgiPSot8x_npliCMsB-3tZ3gjqY_M3dPWcmnAZi_AHel2IFGudy1rX6Q_ie9bMF8-Q2Gd_HA8mqIxalAaHC63M5fX7A2If6t_HRqfgrXiaGvOXf69YZHkS0SiQCdv-2an8GuOvQtqBkbxBi3gtFwmEev0xqRAkz6cNVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مسابقات
UFC Fight Night
شروع شد!
🦖
یک شب پر از مبارزات هیجان‌انگیز، رقابت‌های نزدیک و لحظه‌هایی که نتیجه می‌تونه در چند ثانیه تغییر کنه.
مبارزات رو زنده دنبال کن، عملکرد فایترها رو بررسی کن و پیش‌بینی خودت رو در
TrexBet
ثبت کن.
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71980" target="_blank">📅 12:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71979">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/19ac1824ad.mp4?token=nCzq5StZ74Em5UVo38GYN6-D1YS11RIUDg4yaiVyuFJBf9BRlNdUWYU9pU9BSAA7KHNjbDQkhO5HCoziMsqKGRK4kY8FzywRt9aEkeJavQGjvoskOGymecHJBE7-g5bB4JjhdVgq9mqulp1uEJktGvyv_zIbr0tBcj9VLwXlLDTgDyvPwNL_jDDg31utdFdpgraKAMvI2vady2jtybj5ZpOREMX9X-d3Ws1XrsEeEbqnp0KUKtIWMohF2807Z3fZsLnB52ym_j6E1BD02J-_tWj0v2PN1Wz9m-LZdFK1xV8btmyPX2R6Kr--p81p5VgfTDo5q03cGjZllxPieKOS3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/19ac1824ad.mp4?token=nCzq5StZ74Em5UVo38GYN6-D1YS11RIUDg4yaiVyuFJBf9BRlNdUWYU9pU9BSAA7KHNjbDQkhO5HCoziMsqKGRK4kY8FzywRt9aEkeJavQGjvoskOGymecHJBE7-g5bB4JjhdVgq9mqulp1uEJktGvyv_zIbr0tBcj9VLwXlLDTgDyvPwNL_jDDg31utdFdpgraKAMvI2vady2jtybj5ZpOREMX9X-d3Ws1XrsEeEbqnp0KUKtIWMohF2807Z3fZsLnB52ym_j6E1BD02J-_tWj0v2PN1Wz9m-LZdFK1xV8btmyPX2R6Kr--p81p5VgfTDo5q03cGjZllxPieKOS3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید باورتون نشه ولی، یه دختر نصف شب، این شکلی دختر خالشو سورپرایز کرد:
یه دسته گل بزرگ+ آیفون ۱۸ پرومکس+ کلی شکلات!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71979" target="_blank">📅 12:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71978">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfc3620090.mp4?token=kIzM097o5zWselaO_OBSaNfAlc_qQF5gsS8l9GPio9nO_EKucs-zginDX8H0-YAR61Yh9jJmtjKeOh1-ucVxptjSeQ84z2g_s5qASSnjvDGqDPQVY8W-x0ocv2X_w4hU6vhkTL4jkx63uCJMJ1xbSKjqaFOPqLYQV_SfEtJ-Q-SdXmPdIn952WgzZ1dw-gB9j_zXStUWZY8qfqt2UhbQ-z048Ot5kmdutWvIbdNJDIfcoxzJ7NBpySMU7dBi3zoMFEy_ZP3KoK2P4LjLf38nxu3QTKxfZZvckY8SHDcgSw4XwZu0XIPkJWrMMJjixMKRSO3XgGfKyROJQQRxfYT8GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfc3620090.mp4?token=kIzM097o5zWselaO_OBSaNfAlc_qQF5gsS8l9GPio9nO_EKucs-zginDX8H0-YAR61Yh9jJmtjKeOh1-ucVxptjSeQ84z2g_s5qASSnjvDGqDPQVY8W-x0ocv2X_w4hU6vhkTL4jkx63uCJMJ1xbSKjqaFOPqLYQV_SfEtJ-Q-SdXmPdIn952WgzZ1dw-gB9j_zXStUWZY8qfqt2UhbQ-z048Ot5kmdutWvIbdNJDIfcoxzJ7NBpySMU7dBi3zoMFEy_ZP3KoK2P4LjLf38nxu3QTKxfZZvckY8SHDcgSw4XwZu0XIPkJWrMMJjixMKRSO3XgGfKyROJQQRxfYT8GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از دو دختر جانفدا به اسم پرنسس های جنگجو؛
میگه همه با دوست پسراشون میان رزمایش من با دوست دخترم
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71978" target="_blank">📅 11:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71977">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">محبی، سخنگوی سپاه پاسداران:
در صورت وقوع حمله‌ای دیگر از سوی آمریکا، ایران واکنش نظامی خود را — از جمله «جغرافیای جنگ» و تسلیحات مورد استفاده — به‌طور قابل‌توجهی تغییر خواهد داد.
«ما تسلیحات جدیدی با قابلیت‌های تازه به میدان نبرد خواهیم آورد و جهانیان شگفت‌زده خواهند شد.»
محبی افزود که ایران همچنین «اهداف جدیدی» در اختیار دارد که تاکنون مورد حمله قرار نگرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71977" target="_blank">📅 10:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71975">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9961c391f4.mp4?token=KS4womPA5lYYhbOGFcNAgLdEVP5ipEhxjCIGiDy46iJtLn_gwSdSXJ6474E3teniCj08VWoY1iZHl35Ors6GdMKCVC7mVZ-d0mpFXsanDOJKdQK7YHYWTanS1Oc24saJF-yVZNNmwSwPCl0B8gQ1lKGaLvb2CkjwkgzUuVOQYKdjp3-HAkW8XcZ3Kubd_ld7jJJ2DU6XT6CTq_gJ4UC1l01VjGM3PXq9-nG6l0rOvotrpR1L2eHFlCmeYgGCmfamIOu0TWlxUyK36Lj04v6ycWPP5zJp3vAYFcvqsRCtmnU3MI0VOwsIT2bFmrEzHnhHGsU2fgE4EPiDuXgACCq7-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9961c391f4.mp4?token=KS4womPA5lYYhbOGFcNAgLdEVP5ipEhxjCIGiDy46iJtLn_gwSdSXJ6474E3teniCj08VWoY1iZHl35Ors6GdMKCVC7mVZ-d0mpFXsanDOJKdQK7YHYWTanS1Oc24saJF-yVZNNmwSwPCl0B8gQ1lKGaLvb2CkjwkgzUuVOQYKdjp3-HAkW8XcZ3Kubd_ld7jJJ2DU6XT6CTq_gJ4UC1l01VjGM3PXq9-nG6l0rOvotrpR1L2eHFlCmeYgGCmfamIOu0TWlxUyK36Lj04v6ycWPP5zJp3vAYFcvqsRCtmnU3MI0VOwsIT2bFmrEzHnhHGsU2fgE4EPiDuXgACCq7-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات پهپادی روسیه به زاپوریژیا به یک مرکز خرید و قدیمی‌ترین ساختمان دانشگاه ملی زاپوریژیا آسیب رساند.
در حملاتی جداگانه در منطقه اودسا، انبارهای مواد غذایی که گفته می‌شود متعلق به فروشگاه‌های زنجیره‌ای «سیلپو» (Silpo) هستند، هدف قرار گرفتند.
در استان کی‌یف، این حملات به ۳۴ نقطه در پنج منطقه، از جمله خانه‌ها، انبارها و زیرساخت‌ها، خسارت وارد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71975" target="_blank">📅 10:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71974">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08216dc24f.mp4?token=I-RuyDvrw1EkrsqAiD55IUMyM21ruN09-_-H9wpPXIPuOLOpAtXIzBzI1yybl7V_ILib0SNnemNLRUtykAUCbj9i1i5zIOfs4xpo94oniYC1m7spVro7Ns7gDpXL8qSS9L2DKd5xUPTlcInGiYn8ENRhoNRE1Db6CFuv1c_SY9XqQCx-BRdWpnsVm4bJOU0xIVRB3s_PvnlOKjOzoWu8rMDYTaDvsQTa5rwKttDgvLjKm9XrrFXXAjGEkH_5twHMp2yCkRUBR1XWPg6oXvD2jqVlLemwHBSYhqtjfRYLMxov-V0HMPTZ3MXiaC1OLPpORvvj0jXWGAMKdOjS2Xra-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08216dc24f.mp4?token=I-RuyDvrw1EkrsqAiD55IUMyM21ruN09-_-H9wpPXIPuOLOpAtXIzBzI1yybl7V_ILib0SNnemNLRUtykAUCbj9i1i5zIOfs4xpo94oniYC1m7spVro7Ns7gDpXL8qSS9L2DKd5xUPTlcInGiYn8ENRhoNRE1Db6CFuv1c_SY9XqQCx-BRdWpnsVm4bJOU0xIVRB3s_PvnlOKjOzoWu8rMDYTaDvsQTa5rwKttDgvLjKm9XrrFXXAjGEkH_5twHMp2yCkRUBR1XWPg6oXvD2jqVlLemwHBSYhqtjfRYLMxov-V0HMPTZ3MXiaC1OLPpORvvj0jXWGAMKdOjS2Xra-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مونا محبی، تراپیست :
«یه بیمار داشتم که سه تا پسر داشت؛ فقط پسر اول بچه شوهرش بود. پسر دوم بچه عموی شوهرش و پسر سوم هم بچه شوهرعمه شوهرش بود!
حالا بچه دوم یه مشکل خونی پیدا کرده و برای تشخیص باید
آزمایش ژنتیک
بده؛ آزمایشی که ممکنه مشخص کنه بچه، بچه شوهرش نیست و این راز بعد از سال‌ها لو بره.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71974" target="_blank">📅 10:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71973">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b710ab2e63.mp4?token=aPbq728FdXJly37E0ETOX57nEh6hOfNGhFBX4Y8MnHsgNLQf7siQapN1yLTsBuzI_WrNqrpH3KOAvsWvkDurkf2vt4HuoimXRqGyMa3-749j_nPwcnnAsKsdmeI_OiORcpVEH-Xfm7KDwCFD1m3-6JRBDbEoLo5SGBA_4Prlo3zqV2Z4ZUwYGNoKQWgkgc_315chd5tKIrGwa9kQwbHg0xLuGoaPqSBRcCrSKRw9RkH3mv_GyNLk6OS0-QjlNuMojCS_cEBtEN_IU11DleYJaFpOdBhn6O3vgOlOPwsRUwiOv3tujEH7IlcF-JlKhpSd9vC-I7uiawNU4Pg7FYXbY75NSFk6p1aNaL7ccFkGOu_uufH_gj_9omR2IsuUfS1jTGDYVe5IC9RzGooNUJWInHUp4NsbZ_N2ClRvFSTSzKlDWXPKNGPed-UpTvzos21n7srMudLydn9xnFCyaBnU_wHHzBcQSb4HVvaV7HQu1AxlSaxUTVDvo_NDUtP2a3KFoOaBEhfPql7MaItrMKDkxPaKTnDm2ou-ijBFerz6uGvM70t2oJ1RWNah65JtmNffsy7L8F68ZHM1UJdFN3fN9muB0EVGJbmYv80cFXGBlGXnSLQP3jvbTSlaJcvAaRtNVPzQ5cHSu8B9EbkrsT-E9LMJwqZmTC0uUQexhDsqBoM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b710ab2e63.mp4?token=aPbq728FdXJly37E0ETOX57nEh6hOfNGhFBX4Y8MnHsgNLQf7siQapN1yLTsBuzI_WrNqrpH3KOAvsWvkDurkf2vt4HuoimXRqGyMa3-749j_nPwcnnAsKsdmeI_OiORcpVEH-Xfm7KDwCFD1m3-6JRBDbEoLo5SGBA_4Prlo3zqV2Z4ZUwYGNoKQWgkgc_315chd5tKIrGwa9kQwbHg0xLuGoaPqSBRcCrSKRw9RkH3mv_GyNLk6OS0-QjlNuMojCS_cEBtEN_IU11DleYJaFpOdBhn6O3vgOlOPwsRUwiOv3tujEH7IlcF-JlKhpSd9vC-I7uiawNU4Pg7FYXbY75NSFk6p1aNaL7ccFkGOu_uufH_gj_9omR2IsuUfS1jTGDYVe5IC9RzGooNUJWInHUp4NsbZ_N2ClRvFSTSzKlDWXPKNGPed-UpTvzos21n7srMudLydn9xnFCyaBnU_wHHzBcQSb4HVvaV7HQu1AxlSaxUTVDvo_NDUtP2a3KFoOaBEhfPql7MaItrMKDkxPaKTnDm2ou-ijBFerz6uGvM70t2oJ1RWNah65JtmNffsy7L8F68ZHM1UJdFN3fN9muB0EVGJbmYv80cFXGBlGXnSLQP3jvbTSlaJcvAaRtNVPzQ5cHSu8B9EbkrsT-E9LMJwqZmTC0uUQexhDsqBoM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پاراگلایدر سوار لحظاتی را که در حین فرود به سرعتی بیش از ۱۲۵ کیلومتر در ساعت می‌رسید، ثبت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71973" target="_blank">📅 09:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71972">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c67a57267.mp4?token=UOlVSEf8-dqMu_5keRlW43104od0VagwAePFI0_xhPsJY56Bn21YQZwahBhmy63qsKozvnbpkDJx15neWyWW7kbfdHWGhte7ZyjDbXXb3hrBUjD7nYwpcOJcKRb6fyDkdcKRJSTILqy_i-TSCTKf8mysgVuQXtJuaN4VNiBBYPJEnoo42UoPBC-pNncJmEZNnF9E9D4eiHJcNghWI_hcDGltuDn-i1uLWL1ewhkUMl8jfzNRGxWIAaxZ4jfOu6TgRRcmk4KeOIiMQ6VQYPnbRfAhCwiks0_HA6V8xlghcjMXPWVXlppQ_S4ZHFusoPUv5VUIPvLK1SyJIovZf3iqwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c67a57267.mp4?token=UOlVSEf8-dqMu_5keRlW43104od0VagwAePFI0_xhPsJY56Bn21YQZwahBhmy63qsKozvnbpkDJx15neWyWW7kbfdHWGhte7ZyjDbXXb3hrBUjD7nYwpcOJcKRb6fyDkdcKRJSTILqy_i-TSCTKf8mysgVuQXtJuaN4VNiBBYPJEnoo42UoPBC-pNncJmEZNnF9E9D4eiHJcNghWI_hcDGltuDn-i1uLWL1ewhkUMl8jfzNRGxWIAaxZ4jfOu6TgRRcmk4KeOIiMQ6VQYPnbRfAhCwiks0_HA6V8xlghcjMXPWVXlppQ_S4ZHFusoPUv5VUIPvLK1SyJIovZf3iqwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد شجاعی، از روحانیون حامی جمهوری اسلامی:
امام‌زمان برای ظهور به لشکر نیاز دارد
۵۰ روستا در لبنان را که سال گذشته بازسازی کرده بودیم، از بین رفتند
دیشب طرح آبرسانی به مردم غزه را آغاز کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71972" target="_blank">📅 09:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71969">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifvc5SeibjNpdtaUbUui2VPLNW7b4RaTPVcvB4Cv9mipLfLWSQZDKr_sB2_6fMcyXV0gymecCWjSGCuv2M8XFNerDx1XDS13ve-eRPsNBHp90s5LVYu11SNxDy1KjrFbmtDzz1h2-5pPr3zzJ-46sVtbTyNfZrecSaQ8f8rXmQph57BUHvksEBGVn5OgZO--7dYCRY_HTzL2GglixaGuyez3J0EGEhKqSaejsa2DW25XuLfw4-pvNs7Bgmol36Avm8n71jvI8cFXfvP0v0RKNTk19Fkrud01H8l0I0CvLycdEoEPZNgislT6uJ4jfS4OrELydPuKacLrsY4qz2o7yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5e7e08059.mp4?token=jGPOlNb2YswirUX5aqzRjYGrhFLPR_Kx-HDOBeas5-bZbcTapD2ABisO3ii0nKy0auoI5tx8KXrsqsbgS4uflH-JuxoB7ICJlJT11FheqrpbQHH8ZzjdpxpukRC0w3sO_RAx7fFYI8AURK7gxFa-hdByla5OtvZJFW2Wm-p3cxnDM6anHDGFMMJ17SdnZm8h5GCzwczD7mQB-0FjfbyEJtf2fvOTJGAMcvcUubd-UdQY8KfKOpdzT_7QhzcFA-hsLpumwa9HGZX7XEhHtJs4A9i1n0NePLDRGUBhNOB3hp_dWjOMZzy5AR1pbhzF6YbtxU7OeNPZZTqUDf3zmPgyHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5e7e08059.mp4?token=jGPOlNb2YswirUX5aqzRjYGrhFLPR_Kx-HDOBeas5-bZbcTapD2ABisO3ii0nKy0auoI5tx8KXrsqsbgS4uflH-JuxoB7ICJlJT11FheqrpbQHH8ZzjdpxpukRC0w3sO_RAx7fFYI8AURK7gxFa-hdByla5OtvZJFW2Wm-p3cxnDM6anHDGFMMJ17SdnZm8h5GCzwczD7mQB-0FjfbyEJtf2fvOTJGAMcvcUubd-UdQY8KfKOpdzT_7QhzcFA-hsLpumwa9HGZX7XEhHtJs4A9i1n0NePLDRGUBhNOB3hp_dWjOMZzy5AR1pbhzF6YbtxU7OeNPZZTqUDf3zmPgyHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند ساعت قبل شخصی این ویدیو رو با این توضیحات منتشر کرده؛صحت ویدیو تایید یا تکذیب نمیشه:
تهران ، اتوبان آزادگان
29 شهریور
از اجرام ناشناخته آسمانی فیلم گرفتم
واقعا نمیدونم چی هست ولی نزدیک ابرها بود نور های خاصی داشت و بدون هیچ صدایی در فضا معلق بود !!!
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71969" target="_blank">📅 06:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71968">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71968" target="_blank">📅 01:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71967">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/71967" target="_blank">📅 01:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71966">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d2ba66ac5.mp4?token=vmGSkF_AceUi5bnQ9IyRv4ZenUgi9XwiXEznOre5Hfr3Gw6xd_HWTHIcoJTS0vOeffZUGYnyuQtSc1t4vGNolZPswEiqDDk6yBgB6gVBqq8W2AlvxuXveL38vDSHjMLRqF30Set3f7QA6HlgaVmtKkYRtcsQgA-0V2_n0JoF4XlnD4cT_P0Yu4TY_gR63-k-md4TUqXD3jYwPdDVQNmVYyvdBBhHbsFL0-PSOfZScvQ8TbSyvkqn2pD3q_uf-Cm54BNYwKnGOE40HrVDJzT99bXwTp1782IAe7wocawUygfO_e-ittqlUO04dc096hH4XqcK8W9INnue3c88VKuZ7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d2ba66ac5.mp4?token=vmGSkF_AceUi5bnQ9IyRv4ZenUgi9XwiXEznOre5Hfr3Gw6xd_HWTHIcoJTS0vOeffZUGYnyuQtSc1t4vGNolZPswEiqDDk6yBgB6gVBqq8W2AlvxuXveL38vDSHjMLRqF30Set3f7QA6HlgaVmtKkYRtcsQgA-0V2_n0JoF4XlnD4cT_P0Yu4TY_gR63-k-md4TUqXD3jYwPdDVQNmVYyvdBBhHbsFL0-PSOfZScvQ8TbSyvkqn2pD3q_uf-Cm54BNYwKnGOE40HrVDJzT99bXwTp1782IAe7wocawUygfO_e-ittqlUO04dc096hH4XqcK8W9INnue3c88VKuZ7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوثی ها:
آری، امروز ما حرمین شریفین را هدف قرار خواهیم داد؛ آن‌ها را هدف می‌گیریم تا از وجود آل سعود پاک‌شان کنیم.
ما این حرمین شریفین را هدف قرار می‌دهیم تا به چراغ راهی برای مسلمانان آزاده بدل شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/71966" target="_blank">📅 00:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71965">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89dd2a1fad.mp4?token=S8qNeBpqIgqk68Du8CNKjZ3eTrHLE1ipuzIFS-2L8aacf0zT0WyrdVrB9fGFIaoiARMGBUKY73mCnBkAOywBwW-4FngBZUvH1boWYxTvYIqNsocxx-LSo6VsVquVEW7TjzdMk9mECnBc-E3jax2c3ZMnmlYKqXo0TqEJvg2F2Hod99OETaLoujlErQ8lgDbT1uzxEcv0sJUHnvvWdHAo1Hw965N8YtNTsMDicR0_OYDgOvkc7IDzChH1KdZ6QM5sGFTZKW47Zy1rSiOQU4FAZnxAvIhjStJ4YSNoPQbRTTg4WXt7ceBgT6ZTsSYgK-RDuNqqBkFXGkaabQlA3iNTzhf0Ws5tQSfDks93fGuAidHDO9YAjwDkHDbaFoX5PnXQRL4dl1NhqdJ_DvGlULWDtwssjM6rmBGLhY_LemlZdaS4BAswI8gU_37sLGukRh3V5TpenQSyiBmGJZkG4sQkMwC7MON2HkA8xUW0UuLs7qURUCGZHPnjFdVWNfTzUPpBr-kKSenO8ltZ-4dFPBk1Wm8olwG6EgAvdLpRrRwWf-txCXSN-bQKzhKzY1cVV-y3l98FEqpUCNQ7o28AE1jYm-VpEZEmq7viVDrxvMfrxvmOvQ-ngO0IrLgPV0iD6gRkuhGoYHWELBarlLjMb4qUqb56Xhv-bB32lVZyPEyMlkM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89dd2a1fad.mp4?token=S8qNeBpqIgqk68Du8CNKjZ3eTrHLE1ipuzIFS-2L8aacf0zT0WyrdVrB9fGFIaoiARMGBUKY73mCnBkAOywBwW-4FngBZUvH1boWYxTvYIqNsocxx-LSo6VsVquVEW7TjzdMk9mECnBc-E3jax2c3ZMnmlYKqXo0TqEJvg2F2Hod99OETaLoujlErQ8lgDbT1uzxEcv0sJUHnvvWdHAo1Hw965N8YtNTsMDicR0_OYDgOvkc7IDzChH1KdZ6QM5sGFTZKW47Zy1rSiOQU4FAZnxAvIhjStJ4YSNoPQbRTTg4WXt7ceBgT6ZTsSYgK-RDuNqqBkFXGkaabQlA3iNTzhf0Ws5tQSfDks93fGuAidHDO9YAjwDkHDbaFoX5PnXQRL4dl1NhqdJ_DvGlULWDtwssjM6rmBGLhY_LemlZdaS4BAswI8gU_37sLGukRh3V5TpenQSyiBmGJZkG4sQkMwC7MON2HkA8xUW0UuLs7qURUCGZHPnjFdVWNfTzUPpBr-kKSenO8ltZ-4dFPBk1Wm8olwG6EgAvdLpRrRwWf-txCXSN-bQKzhKzY1cVV-y3l98FEqpUCNQ7o28AE1jYm-VpEZEmq7viVDrxvMfrxvmOvQ-ngO0IrLgPV0iD6gRkuhGoYHWELBarlLjMb4qUqb56Xhv-bB32lVZyPEyMlkM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
من به تمام کشورهای عربی و همسایه می‌گویم: اگر آمریکایی‌ها تلاش کنند در روابط تجاری و مالی ما اخلال ایجاد کنند، ما دو اقدام انجام خواهیم داد.
نخست اینکه قطعاً به شرکت‌های آمریکایی — از جمله شرکت‌های حفاری آمریکایی که فعالیت گسترده‌ای در پیرامون ما دارند، و همچنین شرکت‌های تجاری و بنگاه‌های اقتصادی آمریکا — حمله خواهیم کرد.
ما آن‌ها را هدف قرار خواهیم داد و اعلام می‌کنیم: این حمله‌ای به اقتصاد آمریکا در پاسخ به حمله آمریکا به اقتصاد ایران است؛ یعنی مقابله‌به‌مثل در برابر حمله.
از سوی دیگر، به کشورهای همسایه نیز می‌گوییم: با آمریکا همکاری نکنید، زیرا ما نیز اقدام متقابل انجام خواهیم داد. اگر کشوری همسایه در اعمال محاصره اقتصادی علیه ایران — برای مثال در امور مالی و فعالیت‌های مرتبط با ما — با آمریکایی‌ها همکاری کند، ما کشتی‌های آن کشور را در تنگه هرمز تنبیه خواهیم کرد.
ما بر تردد و عبور و مرور آن‌ها و برخی فعالیت‌هایشان محدودیت‌هایی اعمال خواهیم کرد، یا در زمینه همکاری‌های اقتصادی، اقدام متقابل انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/71965" target="_blank">📅 23:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71964">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d864b0e8a.mp4?token=E5npriIafWO-9SCa6r47l-0mcCSCR3OHLdckoyI7hbONFDKOv89juhNHvT272Rc-gAz8DIinLW0x99GpDv9FNAbZuoavMArd8-wKzEBGzqUoIiwmtknL4yCcfB1JL56uXoCZFRfjt2hq82KchZ6y-lG-asSUG7PKr414kT7qrQT0DCVte-Fi3WXTgZFyzI9ThWUSkeTiD9STQXmLBtj-0tWxFpDTUhIahzKxwgdq17librjffQTP8Rd8dxMVxN3heO8PWT7XAU-J843yH2jbBgrUotxD7Tyd7ZPDn6BzdF0-WKm-bGTL_s2xotUFaG5K8FeU_ROF9mNqbEa3QGdY_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d864b0e8a.mp4?token=E5npriIafWO-9SCa6r47l-0mcCSCR3OHLdckoyI7hbONFDKOv89juhNHvT272Rc-gAz8DIinLW0x99GpDv9FNAbZuoavMArd8-wKzEBGzqUoIiwmtknL4yCcfB1JL56uXoCZFRfjt2hq82KchZ6y-lG-asSUG7PKr414kT7qrQT0DCVte-Fi3WXTgZFyzI9ThWUSkeTiD9STQXmLBtj-0tWxFpDTUhIahzKxwgdq17librjffQTP8Rd8dxMVxN3heO8PWT7XAU-J843yH2jbBgrUotxD7Tyd7ZPDn6BzdF0-WKm-bGTL_s2xotUFaG5K8FeU_ROF9mNqbEa3QGdY_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تهران دختره بعد از اینکه پروفایل اکسشو‌ چک میکنه و میبینه اکسش رفته با یکی دیگه درجا سکته میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/71964" target="_blank">📅 23:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71963">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3758b5713d.mp4?token=Xuj8HH4e_lIjN-MiA6fw8qtj79IjBfUU1_kylX4TAoUhDdy8MQB53XgLd-dHqaCSmU3ugvEOZJhBNmCpdu87k8Cqq_aVqnWzoA7V9XCeuWdiPqSKUjMWd6R1WfIOmVnT3_sv0llMRcVer8_T4sfNe4IKZ2YuU0CRHQTOs1gTGZlfu30GfXpFuA903gZnjzyhB3x0ZQfgZwunC1jpHqFCQN-jazS7k3Rq0gtjWjS4wVfImxhmLjaBniwkhnGOO6EhwgO-0EajnRTfP_Tez_sC7StOuSBT44zcJdPW1YUQY4hhaEOOtgBXjxKRG585iODni9r8e3KkGMZYwreHPyBMZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3758b5713d.mp4?token=Xuj8HH4e_lIjN-MiA6fw8qtj79IjBfUU1_kylX4TAoUhDdy8MQB53XgLd-dHqaCSmU3ugvEOZJhBNmCpdu87k8Cqq_aVqnWzoA7V9XCeuWdiPqSKUjMWd6R1WfIOmVnT3_sv0llMRcVer8_T4sfNe4IKZ2YuU0CRHQTOs1gTGZlfu30GfXpFuA903gZnjzyhB3x0ZQfgZwunC1jpHqFCQN-jazS7k3Rq0gtjWjS4wVfImxhmLjaBniwkhnGOO6EhwgO-0EajnRTfP_Tez_sC7StOuSBT44zcJdPW1YUQY4hhaEOOtgBXjxKRG585iODni9r8e3KkGMZYwreHPyBMZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیر ایرانی چند ماه پیش:
کیرم تو جمهوری اسلامی! کیرم تو قبر خامنه‌ای، ایشالا تو جهنم میسوزه!
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/71963" target="_blank">📅 22:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71962">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf9813dda.mp4?token=HbF-H-f2SwcEurtN2igIpuWRAnevTYu2Xuk3mVhjKKhOesQ8Xo-wTAJPH0kxsmk4mBTby8IFjCRhsz7FIJfvGNZ5_NQIZ-JlLezMXGu401BZgxmK9FugiVdA0l-Gj25DVuNDUYnF1ndp-krwh5bd30wtJ_5rerd6ZG_0TQNxHfWj2jIGTBviVWMys__rK8yVN_7GdTXSGMwU4LbO9WvWm8cKpeEI_obL9k1al4ziAfbbe-BRGUsdmutUCDRtYD5s7zI-QqOk1zX2t7MJR_lFhGEMX1c9PhAufZWxUo90f61IMieRTcLS6ikwo03vqMWcfjj3l2PtRtNwkv4h4HCRsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf9813dda.mp4?token=HbF-H-f2SwcEurtN2igIpuWRAnevTYu2Xuk3mVhjKKhOesQ8Xo-wTAJPH0kxsmk4mBTby8IFjCRhsz7FIJfvGNZ5_NQIZ-JlLezMXGu401BZgxmK9FugiVdA0l-Gj25DVuNDUYnF1ndp-krwh5bd30wtJ_5rerd6ZG_0TQNxHfWj2jIGTBviVWMys__rK8yVN_7GdTXSGMwU4LbO9WvWm8cKpeEI_obL9k1al4ziAfbbe-BRGUsdmutUCDRtYD5s7zI-QqOk1zX2t7MJR_lFhGEMX1c9PhAufZWxUo90f61IMieRTcLS6ikwo03vqMWcfjj3l2PtRtNwkv4h4HCRsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر خانومی تو تهران میره به پسرا پیشنهاد میده که با حساب خودش برن کافه، اما هیچ پسری قبول نمیکنه و دست رد به سینه این بانو میزنه.
آخر سر هم کلش خراب میشه میگه پسرا پرنسس شدن و تنها میره کافه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/71962" target="_blank">📅 21:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71961">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVVopXfueCiUYK6inXo-hnQl9fiFCDoHiXRiIhToc4Acthip1SSWhhiIgoFknTh-sr-yyNt2hY2yI9AewYbB8xwGGHgIdV5yXCmdR2aN6YXYga77e-5AUBxKMjsfC-I5Dbh2keVcLZcH93FmQeo4Vt6hP4MztKMvqv5dVLsz95WVLxU4hinq60DT9Fo1RghLF1Lfy78zGO0whvY35IBNpHCz69cQ-KSp5FTyrlgs14fP6yjt2KMcRhw4sWRWbso6kZjjZZvwQ7c4mPEZw3FtGEFiTuA1vMq4ZJuDjbHoawJowdnV75PSVF0tAXlgdhYmKLsSzKZpefhLyplmf1oMxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/71961" target="_blank">📅 20:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71959">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10eceadf6.mp4?token=tBk53yxtDXRv4LNcgX2E_3H5J76yI8L6nt34QRiRhtQ2Bg7QoKHSqy5zJVDFGpYaCZH-dNJiZVcmsgX_onlAOtKQ8Y6DF4H6S3dFU7DstGzMWM2BgrX_yMVMSb_u05HtjBXWaf8Q2_QEK4puxaL4TVPQvdaL9cdEnGDH4p-7L31xFVG1FXmoDVmwlGzxDmq-e2pLi-XjJjVKL1bFls9nN-ZDPDgleth-xipT9FmcbJo8GXtzK5P3BRg6YGpS8ueslBZbTPvzONIkv-qVX25pV_0lEdNR8IagqTyxltlpk45RrRhsGqgF-2vrdkpjLtaptQeBqrgMqT9eb6LpKcq7WmRJp3h3qhfmSdJz3YYYSfvSt5kwzVRBLiZ4qL3bJdlgZCdDf67ZIIoS33sepiRzfkRIZiNlh6BD2CvuBy9mre9qR9_sDqt6qX2_RoODRz3OdMTXuotqZKvMsACWnOmzMcAatEb9tkK0xbjUynze387YPpFWiJwL4M_g8YfCdohbLJH4hwhzwySMHZReI4iywcP_zzsI6DtuJkbO2F9JtJFi9fSvGOui3Q_slheml7quYvXDyb1Vbjixkp1P118lKL_g8Am67xEEwoaa304kBNLDHn__SwAEckHi8fAU6n4sAbooneNuhvE7_nBGPckHqIQD5DQRyep799quI1QJZjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10eceadf6.mp4?token=tBk53yxtDXRv4LNcgX2E_3H5J76yI8L6nt34QRiRhtQ2Bg7QoKHSqy5zJVDFGpYaCZH-dNJiZVcmsgX_onlAOtKQ8Y6DF4H6S3dFU7DstGzMWM2BgrX_yMVMSb_u05HtjBXWaf8Q2_QEK4puxaL4TVPQvdaL9cdEnGDH4p-7L31xFVG1FXmoDVmwlGzxDmq-e2pLi-XjJjVKL1bFls9nN-ZDPDgleth-xipT9FmcbJo8GXtzK5P3BRg6YGpS8ueslBZbTPvzONIkv-qVX25pV_0lEdNR8IagqTyxltlpk45RrRhsGqgF-2vrdkpjLtaptQeBqrgMqT9eb6LpKcq7WmRJp3h3qhfmSdJz3YYYSfvSt5kwzVRBLiZ4qL3bJdlgZCdDf67ZIIoS33sepiRzfkRIZiNlh6BD2CvuBy9mre9qR9_sDqt6qX2_RoODRz3OdMTXuotqZKvMsACWnOmzMcAatEb9tkK0xbjUynze387YPpFWiJwL4M_g8YfCdohbLJH4hwhzwySMHZReI4iywcP_zzsI6DtuJkbO2F9JtJFi9fSvGOui3Q_slheml7quYvXDyb1Vbjixkp1P118lKL_g8Am67xEEwoaa304kBNLDHn__SwAEckHi8fAU6n4sAbooneNuhvE7_nBGPckHqIQD5DQRyep799quI1QJZjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشتی «لوچینگ یوان‌یو ۱۰۸» با پرچم چین و یک کشتی باری با پرچم پاناما در نزدیکی سواحل سنگاپور با یکدیگر برخورد کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/71959" target="_blank">📅 20:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71958">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d61320a9.mp4?token=phdIiyekGb0XM7BI1Elgvab87ESmLOU-F-8Oeu7KGaOzlLiyHUumoBUZgaElqCWCPxEOIVYuYUDIRwL5EkKnBRBIe35bubc5vwgPXRv2a1FIwhk_jKA7XaG2uLABhUbkrq_mQwoa42VEX18Ki1rcupVspmfo4QMLpGVbw_QqRswi9MRwAGyxkFsMeochYYn0Q6J-nCjfVtY_XDItYtsNqaRYcYRSvJpwaSQlwILz_LATYCfIDeFN0svbkcYvWpFyRQU9v_7Kj2Pno8yINaLL6-UU5sFanfeRdFLlA97euahWEtnG9yVGA-OodyT7r-c1CYOen2QWgjywhn09NbWIOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d61320a9.mp4?token=phdIiyekGb0XM7BI1Elgvab87ESmLOU-F-8Oeu7KGaOzlLiyHUumoBUZgaElqCWCPxEOIVYuYUDIRwL5EkKnBRBIe35bubc5vwgPXRv2a1FIwhk_jKA7XaG2uLABhUbkrq_mQwoa42VEX18Ki1rcupVspmfo4QMLpGVbw_QqRswi9MRwAGyxkFsMeochYYn0Q6J-nCjfVtY_XDItYtsNqaRYcYRSvJpwaSQlwILz_LATYCfIDeFN0svbkcYvWpFyRQU9v_7Kj2Pno8yINaLL6-UU5sFanfeRdFLlA97euahWEtnG9yVGA-OodyT7r-c1CYOen2QWgjywhn09NbWIOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک هموطن به مایک جانسون رئیس مجلس نمایندگان آمریکا:
لطفا کار مربوط به ایران را تمام کنید
۸۰ میلیون ایرانی منتظر شما هستند
مایک جانسون:
میدونم ، قطعا و علامت پیروزی
✌🏻
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/71958" target="_blank">📅 19:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71957">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b0937658f.mp4?token=OzGoPDj98vrRzy5L9-S9ohXmlZz4VPUbMOMPIbpsV1uK1k96jWdJzmXRj0WY_r4v_RV-zz5nD5MqdXzNwdDc7aghr23HYrs-4T8DL9kqB7Ay9Hm8sqzHLBgM0QwR2s564NG7RLCU0XRSnC29T4GAPQHgHoliPw6KdyVXak6tTNUo6CHaeR4ZBat_VShxFyAQDn-yXBfJovGRIlPHOP1IYkItECsbJSyHPhyFgzYgrubBQyN3fp9-Fkxxz2qcVBpCJ-7y4MhexP0u_RMMtG6VQrE5geonHvaJOwoVPmMOmnBlZDDdLdDE9uPWbJS6nyHZnxH2KO8t5irZo--6_1s4Mq5iL-81AicEiMkrJt2dGwySHdqq7pxrwSTFvqAGRbxatlDxA-3GuP7O_u5d5YgPYt-AqAq8s-MP1_B8ODznxB9c94WUxZ6vdPc91ScXHu3rDdhNqzVXwW4rjXOjeBzBBMy8EeeVIqkDVzZO4L2rwMNCmf3JEvyZ29ZRB_959oS2jqoBgqQuKvys9FcO3iDEzWzfLcjGSkkXHFBAwbqxWQ0gEt2Xdh247cE2LM6MPeUpmiBPUr3eSHkIZ48VLg8dZ_n78JeObn593iQ5fOhAurhLG1esSrBkB6B4B36dT8umSKkacxf-bchBILO1jd7NBBt5Z2QXObOu5aaEC4kyIMs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b0937658f.mp4?token=OzGoPDj98vrRzy5L9-S9ohXmlZz4VPUbMOMPIbpsV1uK1k96jWdJzmXRj0WY_r4v_RV-zz5nD5MqdXzNwdDc7aghr23HYrs-4T8DL9kqB7Ay9Hm8sqzHLBgM0QwR2s564NG7RLCU0XRSnC29T4GAPQHgHoliPw6KdyVXak6tTNUo6CHaeR4ZBat_VShxFyAQDn-yXBfJovGRIlPHOP1IYkItECsbJSyHPhyFgzYgrubBQyN3fp9-Fkxxz2qcVBpCJ-7y4MhexP0u_RMMtG6VQrE5geonHvaJOwoVPmMOmnBlZDDdLdDE9uPWbJS6nyHZnxH2KO8t5irZo--6_1s4Mq5iL-81AicEiMkrJt2dGwySHdqq7pxrwSTFvqAGRbxatlDxA-3GuP7O_u5d5YgPYt-AqAq8s-MP1_B8ODznxB9c94WUxZ6vdPc91ScXHu3rDdhNqzVXwW4rjXOjeBzBBMy8EeeVIqkDVzZO4L2rwMNCmf3JEvyZ29ZRB_959oS2jqoBgqQuKvys9FcO3iDEzWzfLcjGSkkXHFBAwbqxWQ0gEt2Xdh247cE2LM6MPeUpmiBPUr3eSHkIZ48VLg8dZ_n78JeObn593iQ5fOhAurhLG1esSrBkB6B4B36dT8umSKkacxf-bchBILO1jd7NBBt5Z2QXObOu5aaEC4kyIMs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش، یک موشک رهگیر پدافند هوایی اوکراین در حومه کی‌یف موفق به اصابت به پهپاد جت‌سوز روسی «گران-۵» (Geran-5) نشد و این پهپاد لحظاتی بعد به هدف برخورد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/71957" target="_blank">📅 18:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71954">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12842b3342.mp4?token=pjJqJNPIudGHc_xanHrBH2y_VCHOxRUWUA71CmKcFDx75GxTO8PEOlQmnWyhz9wGDb5M9xHPWY6o9yE_NMkeEb_e-WhjaFj8vr8z_jXYYWpYf9ii-pSgg2rhQv2pxYH1-PDczgfF5P3O-LQswEenoFkW7gGEOBbC6A918joKgZgG3hAMW9A1J3-ESuSltnSgy2cKr9qdCoJZ90ukloSP-yFIfN5mIN2ghu6AaQgqxuDXbY3DGqLLO5vzREm1IU_Jytgwuw8fV4h6wip8pDejHnOgUBsM-ZJf2_q4_qK-lfiZkpVoJ1LE4hXgSM_zsldzj-lXmci9_Qu2RAt9NDwRUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12842b3342.mp4?token=pjJqJNPIudGHc_xanHrBH2y_VCHOxRUWUA71CmKcFDx75GxTO8PEOlQmnWyhz9wGDb5M9xHPWY6o9yE_NMkeEb_e-WhjaFj8vr8z_jXYYWpYf9ii-pSgg2rhQv2pxYH1-PDczgfF5P3O-LQswEenoFkW7gGEOBbC6A918joKgZgG3hAMW9A1J3-ESuSltnSgy2cKr9qdCoJZ90ukloSP-yFIfN5mIN2ghu6AaQgqxuDXbY3DGqLLO5vzREm1IU_Jytgwuw8fV4h6wip8pDejHnOgUBsM-ZJf2_q4_qK-lfiZkpVoJ1LE4hXgSM_zsldzj-lXmci9_Qu2RAt9NDwRUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به گزارش رویترز، سامانه‌های پدافند هوایی در اربیل (واقع در اقلیم کردستان عراق) یک پهپاد را در نزدیکی فرودگاه اربیل سرنگون کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71954" target="_blank">📅 18:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71953">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی:
دخل و خرج زندگی مردم آمریکا با هم نمی‌خواند و آمریکایی‌ها در مسائل داخلی به جان هم افتاده‌اند
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71953" target="_blank">📅 18:14 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
