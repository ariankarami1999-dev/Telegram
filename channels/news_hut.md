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
<img src="https://cdn4.telesco.pe/file/hdrV6YhTaG3fbObnFoVwWOQcbpn2pSnz7kP9leXsXH0Qcg0znWe43TYQOx5Ljs7-qhiWJZQFsx3SNw6q7UsF2M-D_vVyGa5zJzh_jnGno238bl1tEyY4vL8M_Nuk606nHKwnkuDb4Hq_cxHwOkPnElC_joS5lO32q5P031YqL6NU26XWrRYtWELfacSkww775kKaSdYz0sDBBWq2PlXTKjE0ivLS1LNLYDQ0veo-m7S1VXQ8ZOqtl4_3_VHFFNkGixEtAOimlSm8OKh2uCTR41GihyVpKug3LpNDtpzkSZFAN9_CyhHTfxV5UznUsP0z6S-5K_6TOoE6inTTceKIng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 19:06:26</div>
<hr>

<div class="tg-post" id="msg-72183">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fcd656bf7.mp4?token=d75cbENqfC4k8wlXZPWwkz0oYaB4_gEFKUauHPGKQwFb4k9c3xeiMbXmx84RVubv7Lf18JIelfX_Utdd27yexsCUxzW8U0uc58Ah2TdKdURWfFHTzQbE9gTS8luPZRco2QIeBL9PEWKFwCEKz8mbjZ-WX6liIanJmsZGENHSJHL3QfgNW43I0PZ6IrQaGPmCwgGjaZGzC-d0mONkr_TUCs5kU19rlPBhuXOpPLkT3Q0z9gDZ-qtRCZCOAyfUBZfz85OC6E5KAlYHGu12BW64nPMLJbbpfbv0YolQxKRMzad5vNkjcWNy6F8yAdHFWF1LN4cqMYrlm38i04coCjQzNKTzWvqYVO5Y4RWXMDRrE0uicTUxg7U6d0udctsqUdRc-cip_z39Fi8QhS3M4UzdNOwv787lNM1tRNjQioo3hNE8k_dOQpqilmbGEwttcC0Mw3jmCHDAQ3GKkb-zXPzQpW9D2aPYcZF1nHmBcUnPC1q4r6umFBACkw9SnHth90wI2Q2tXJQh5VdKZZD-D4eGcIly2Bt8OwLMXqRf0j8PFSmKGDWpJF1-zHFoJe27Ki2Knuu0TW35Cc-clVkhez-mI3UAj1qmBvNjUxLm7eugH2qrgbyzcWJtCqo0vCFseQDmKfzPrVOgBIhKCBe_YhICq1BHQ6B1Jjcr_8I0Gfvh-Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fcd656bf7.mp4?token=d75cbENqfC4k8wlXZPWwkz0oYaB4_gEFKUauHPGKQwFb4k9c3xeiMbXmx84RVubv7Lf18JIelfX_Utdd27yexsCUxzW8U0uc58Ah2TdKdURWfFHTzQbE9gTS8luPZRco2QIeBL9PEWKFwCEKz8mbjZ-WX6liIanJmsZGENHSJHL3QfgNW43I0PZ6IrQaGPmCwgGjaZGzC-d0mONkr_TUCs5kU19rlPBhuXOpPLkT3Q0z9gDZ-qtRCZCOAyfUBZfz85OC6E5KAlYHGu12BW64nPMLJbbpfbv0YolQxKRMzad5vNkjcWNy6F8yAdHFWF1LN4cqMYrlm38i04coCjQzNKTzWvqYVO5Y4RWXMDRrE0uicTUxg7U6d0udctsqUdRc-cip_z39Fi8QhS3M4UzdNOwv787lNM1tRNjQioo3hNE8k_dOQpqilmbGEwttcC0Mw3jmCHDAQ3GKkb-zXPzQpW9D2aPYcZF1nHmBcUnPC1q4r6umFBACkw9SnHth90wI2Q2tXJQh5VdKZZD-D4eGcIly2Bt8OwLMXqRf0j8PFSmKGDWpJF1-zHFoJe27Ki2Knuu0TW35Cc-clVkhez-mI3UAj1qmBvNjUxLm7eugH2qrgbyzcWJtCqo0vCFseQDmKfzPrVOgBIhKCBe_YhICq1BHQ6B1Jjcr_8I0Gfvh-Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز یک بمب‌افکن رادارگریز B-2 و چهار جنگنده F-35 Lightning II بر فراز کاخ سفید در جریان سفر رئیس‌جمهور شی.
@News_Hut</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/news_hut/72183" target="_blank">📅 18:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72182">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wj1dZ-ZAPByxSVL8ldzaTGiBXc1ecNiXQ2pgVptn847DAjjufQVcNG5U9XnbDQB_qZWdw5-lbY1BfZM8SOePdEcgVTYHySNBuJr5bMK93DheqRpjDxFemmq2crerhOKVOdqYiQpCm-YXc2qIrmYacH6GGUFD8nS4hXhCIHWShRXFXvAUqUCQ_7pOa5nekfrTYyxeBX38SnGBiLyIpTBsHX3EwJgPoow3vNG_6SW9BICVRFIRRFwYtUc5rl-4BbykiRRSQZOCUhGM1bq2na-SU2OfimAzLY-rZpVqqTQJSl960TUyeckJ7ABKZjPb2mhJbNWTKW0Iiej-J4D8ilS20w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تانکر ترکرز گزارش داده است که نزدیک به شش میلیون بشکه نفت خام توقیف‌ شده ایران به ارزش حدود (600 میلیون دلار) در حال عبور از اقیانوس اطلس به سمت خاک آمریکا است!
@News_Hut</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/news_hut/72182" target="_blank">📅 18:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72181">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41a961ea41.mp4?token=vqPXVLNbGG_4snu4VpeRNP-SnpDXBiXzyaQn5mW6EHgRr0B53izAtAZ0jwMNI9VkiNBWf668Xe6wKnbPrXHHd5RgtXKasvH_k8wX5MHhi85uqpRcT2u_px2SERWWFAAQctzfAM0eyvJx6tq0A-NNnL5MdQV0HdjUe5FyOkKKgPB50troSnjDeMbZCSWBrpn-6n-VefQTGCE0I-92HUC95TP9PZ6KsTFmjtKMmhm8LRSLsEi2q-iVP2yyApJ-js3VDIoF2fjRcR_Sqy_4J31VPHqszh8pfYmsS1xwMy5NCcNFWX9SYgSnkMRmci2NSx6HOnEhdzEROLhASr9ETsVzrATRS0kVdnwQw-T6ID73EHcHjhJUN2z3VNzJV72rhRW6WrHK8xGTYt_7wOOvt5MwpF-_TMouGG1nn-7OFNhcuhll0iTVdi3XJHeuJZo8Ru1LsjkNTVAimr8pcErkSCGsI3wnFqnK9LJycLgB1ZUabL6FLvowSiFXfcMWhJ-M3fS5qEGg9scvyv9WVDBONM1saszFGy2FSkNaqXUqpplio70HFZCG5qj52K6atTUz8cEYPUr6XAgaZyibz2qKUFbILkskgYJZ5w8BNRbhV7vJP2zPoTApJxj6L3pRLrJ7MvkW526eJUmkp4P79lSQ_TR1Zv5xzFi3KOJ_iAciIcZlWco" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41a961ea41.mp4?token=vqPXVLNbGG_4snu4VpeRNP-SnpDXBiXzyaQn5mW6EHgRr0B53izAtAZ0jwMNI9VkiNBWf668Xe6wKnbPrXHHd5RgtXKasvH_k8wX5MHhi85uqpRcT2u_px2SERWWFAAQctzfAM0eyvJx6tq0A-NNnL5MdQV0HdjUe5FyOkKKgPB50troSnjDeMbZCSWBrpn-6n-VefQTGCE0I-92HUC95TP9PZ6KsTFmjtKMmhm8LRSLsEi2q-iVP2yyApJ-js3VDIoF2fjRcR_Sqy_4J31VPHqszh8pfYmsS1xwMy5NCcNFWX9SYgSnkMRmci2NSx6HOnEhdzEROLhASr9ETsVzrATRS0kVdnwQw-T6ID73EHcHjhJUN2z3VNzJV72rhRW6WrHK8xGTYt_7wOOvt5MwpF-_TMouGG1nn-7OFNhcuhll0iTVdi3XJHeuJZo8Ru1LsjkNTVAimr8pcErkSCGsI3wnFqnK9LJycLgB1ZUabL6FLvowSiFXfcMWhJ-M3fS5qEGg9scvyv9WVDBONM1saszFGy2FSkNaqXUqpplio70HFZCG5qj52K6atTUz8cEYPUr6XAgaZyibz2qKUFbILkskgYJZ5w8BNRbhV7vJP2zPoTApJxj6L3pRLrJ7MvkW526eJUmkp4P79lSQ_TR1Zv5xzFi3KOJ_iAciIcZlWco" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ از شی جین‌پینگ در کاخ سفید استقبال می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/news_hut/72181" target="_blank">📅 18:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72180">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72180" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/news_hut/72180" target="_blank">📅 18:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72179">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZndKmgMYnYTT-Xys8WjHP1lwRRjGXobczyKni3oWtMkDuVODfPghrAJUUydQlaVoTLrAyLZoGlPKhVLO6s_m853RZViI6WP_okn1OhUrtLv4itdnYS8Fup8QQLRK-ZfClong1vytTrKV4OYpJSLbNkaGFzekDENaJcZRZecKkmgljoLeIAJTLYbwnsrtwE4cG5_P24B9irNaqcawNpF2rqVUp0bNs17zbV3Pjo0_n7W52fgCttB7YpWxt_-Rpo0M4UDpVAcExzCoON7ufDHblfPVy3RgCGPlpLDnoE-EDuST9M6-bOqkTKdXIcnX-5I0Jrb2_GBT89aEWszZB9pkUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
ولز
🆚
پرتغال
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
ولز: ۱ برد، ۳ تساوی، ۱ شکست و ۱۱ گل زده
پرتغال: ۲ برد، ۲ تساوی، ۱ شکست و ۸ کل زده
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
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/news_hut/72179" target="_blank">📅 18:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72178">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffI3scvaGt02E_-HTGpaXT8Np8q3Co7ld2eGIPctCpUBwJrJLBfk7Y9RYn3W_jNPPxbAqX6E5tCGuZsd8tWzZZmlgJItPWAqOQFnML5QSxoQBzKNqaS8ouNQ1_eOF8nGCD_wrhYFZiw4vDMNV5RC12CBkGxKUiG2-woVS3Qj94KSyUcrLlRHVwXJHxVWIutZWZjM74YILxIQZ_FfoQCvfWAC9WLZcGBb6isoG4myjoo1Cbt796v50cKN1dkL4wt-j0QiHdqxm-RQXqnWsBwPNNDZjaz0kvMu9_ThtKOF83UCv-ba65gTbGY4_zR2Brw-HXd9A5Y5h9sFPoIxOYDU4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو برای شرکت در مجمع عمومی سازمان ملل وارد آمریکا شده است.
او قرار است امروز در نیویورک سخنرانی کند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/news_hut/72178" target="_blank">📅 17:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72175">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fibLwHkFfUHdlLIHUrct7gbRE2vlc9kNXGalZ5rkvb1bQKgZcbQP65zqkp8x8OglCuXV42V6TOP-OQDEOxqAbec9QKJeS1e7VQTUZrZN0HXF7a3l1JAkjT26cJaGyW5xf00Dzb8pyWypfQENOcpNqKijhfs8auTBrflxBmn30UYsMK3iVHvBz0q-cZLtKS32vOhuK2ltMjm18IwYfP_Kfa02nWVVQELn3XfDsO0s9hYOM1EF0O9ewqUBBt0UmyYUwi7WTiRNiarKHD9IB-8i4-fwp8HHKYpSW0KH7z0iwV4avhK4SA-u0qdqPWGExeuVceGxPA148KvZLKuMcuYhwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YOg7OMcV7a1iJB14W-3MfQMKozDvOY_Yy9Jx4-f-7RJuAak_RBA09VIO-aS7MKXt_9mbK16sin_hPFRwISKdZVMv8TKAqYQt4kd5ZnMYpkHtgwkq68kw-G2F0HOqfXrwsQQ_J0WGcRxEz17pSou1cwDD-wM9-KnPbXiTfdcaSm2LpJImzf4HWTdd5Xy1XewK1zwhuzW7BFAmujI72wwuJiUNr1pyDpqT6RVENoeCQHxupbMk1dMc7DrE1BwEZWPa8e_ikiBflGMdThXpfqwaUw8s8j8gsb8FFBgUKstm6WkiUBZuHWlP7i_x_vLJ3u5Ega2UhjSx4la_2CHpyeLFtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e7959de70.mp4?token=ZhguuaVX9jYQROVkWS7N2tFlrrKJL6lx8pN8zJRWH1w_LQbquK40SsEN_YZ3tZdk_hElCrVtx5MdYG9zUsP16rO2mXApwSbf2j1cYrXvdf4sbEtABnCXdWxU-UQB2FtckLxkB-pb8pTRFVaMdN7usPSfFxYbnBCAmqGhi5UO5iO6Sw7Y5O9hz7bvRzljTxEbKG6NDHPWIS0EbOMpJXq_BSAPmJ7dzRGQaxv3d7E9m6X-JSXsgAqvzKRFGHQPwcGq-e1EvjOkjDA3WGwidwlYcJ37DntuuA4OcPRUCjkWHrfTT0xkYyfgjfVUFquW7ec9b4kBRJCskjXgd-c2-yB_AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e7959de70.mp4?token=ZhguuaVX9jYQROVkWS7N2tFlrrKJL6lx8pN8zJRWH1w_LQbquK40SsEN_YZ3tZdk_hElCrVtx5MdYG9zUsP16rO2mXApwSbf2j1cYrXvdf4sbEtABnCXdWxU-UQB2FtckLxkB-pb8pTRFVaMdN7usPSfFxYbnBCAmqGhi5UO5iO6Sw7Y5O9hz7bvRzljTxEbKG6NDHPWIS0EbOMpJXq_BSAPmJ7dzRGQaxv3d7E9m6X-JSXsgAqvzKRFGHQPwcGq-e1EvjOkjDA3WGwidwlYcJ37DntuuA4OcPRUCjkWHrfTT0xkYyfgjfVUFquW7ec9b4kBRJCskjXgd-c2-yB_AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هوایی اسرائیل منطقه «کفر تبنیت» در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/news_hut/72175" target="_blank">📅 16:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72174">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb1a6b62b.mp4?token=G1w0Ob23QLvbjIulKoZj6OijSZTMSHgjtzaFWTN3279uUjK0rUohF2po41ET-i2MC_NK-mMW9zVK0Snv7rtEAQl_PPpNipmNNZ_Iyob2SfX-5HzkL1o0APvr1UIVI7arZs14f-xNL1Nx-vy5bzih9N-JbIOG7pty1uuVl7VTitfpFrWVNeyIuuL4HKgM07A4JWV3qa78HYSZdBc9Oh7OqR6jlYJH82Q__DpKg1raq57ifuzeXIs39q4Ogljkd5P3-7VK2Acj7bYNkspeQWIaMDxKOIznj0huKF72cZcCoP5hdzsDtQT84RVvjUhvsMGFRReHYUoXoDDmylDpEMlyIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb1a6b62b.mp4?token=G1w0Ob23QLvbjIulKoZj6OijSZTMSHgjtzaFWTN3279uUjK0rUohF2po41ET-i2MC_NK-mMW9zVK0Snv7rtEAQl_PPpNipmNNZ_Iyob2SfX-5HzkL1o0APvr1UIVI7arZs14f-xNL1Nx-vy5bzih9N-JbIOG7pty1uuVl7VTitfpFrWVNeyIuuL4HKgM07A4JWV3qa78HYSZdBc9Oh7OqR6jlYJH82Q__DpKg1raq57ifuzeXIs39q4Ogljkd5P3-7VK2Acj7bYNkspeQWIaMDxKOIznj0huKF72cZcCoP5hdzsDtQT84RVvjUhvsMGFRReHYUoXoDDmylDpEMlyIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غذای مجلس ترحیم، اگر خود مرحوم. این نوع غذا رو خورده بود حداقل ده سال دیگه زنده می‌موند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/72174" target="_blank">📅 16:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72173">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d6256f78.mp4?token=vebAuKPnK1yKOHVKN4cne0ZCx3PmGVudx2ln4tHbXZzgZHYWs77josXPUVIwTjBuBAvKXptVULs9l2vnBfz4NwEWBmy-3jo6zLCuGnT89Q88c-QkyKI_jh0sC1_v76vPpm9T0r8ClLigw2k0Jkh-bkmHgtpcE-v7EbNAEqQLgthjXpXIstADLwL_k-SamSZCXb3J5tFMueX5u4DFm_j3ATUhiJID_wtbSpCYSIsb9lY1l-4F75aMWdvDDi3tBaWa6ytldRQsaXgIp11lxiiXVzNfc49qyzTqnzsQlD485NfR2g8jLmqa7nSawwuKcQzEYRl7zF94AXz8Yu8oq3gwNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d6256f78.mp4?token=vebAuKPnK1yKOHVKN4cne0ZCx3PmGVudx2ln4tHbXZzgZHYWs77josXPUVIwTjBuBAvKXptVULs9l2vnBfz4NwEWBmy-3jo6zLCuGnT89Q88c-QkyKI_jh0sC1_v76vPpm9T0r8ClLigw2k0Jkh-bkmHgtpcE-v7EbNAEqQLgthjXpXIstADLwL_k-SamSZCXb3J5tFMueX5u4DFm_j3ATUhiJID_wtbSpCYSIsb9lY1l-4F75aMWdvDDi3tBaWa6ytldRQsaXgIp11lxiiXVzNfc49qyzTqnzsQlD485NfR2g8jLmqa7nSawwuKcQzEYRl7zF94AXz8Yu8oq3gwNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این آقا پسر برای تولد دوس دخترش ۲۰۶ خریده و اینجوری سورپرایزش میکنه :))
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/72173" target="_blank">📅 16:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72172">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a803db071d.mp4?token=iBBWkBBuJn6PxZkaHV-KYECtaPq9jmo3PqSpW-q3Mwxg5mLU64VeVsxxXgiMuA135YzizACNuQ8wFCgmzFGvjmjO_dVcs41j9jMUzWXF2EozSoZCwIunuD06xWwNHyrfmPBgpZ6VnBWKmvveDTV1F3amDyvTkGUB_5tiTkGyfhXT1UgLhO5aT2IwzmmCmkIbQBTR0gqJX4Cg7NcHDQvY4G12oRTIPReRvpTA16lsFSqOFEB_gek4C5h5QqJGE81It5ag9s06fdgAyaNHNO9Onsl0t3jioO3Q7-e5mQB956jvOdVwXfumgfVBozOg718YDVbS1X_bnPSITYck-RPuOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a803db071d.mp4?token=iBBWkBBuJn6PxZkaHV-KYECtaPq9jmo3PqSpW-q3Mwxg5mLU64VeVsxxXgiMuA135YzizACNuQ8wFCgmzFGvjmjO_dVcs41j9jMUzWXF2EozSoZCwIunuD06xWwNHyrfmPBgpZ6VnBWKmvveDTV1F3amDyvTkGUB_5tiTkGyfhXT1UgLhO5aT2IwzmmCmkIbQBTR0gqJX4Cg7NcHDQvY4G12oRTIPReRvpTA16lsFSqOFEB_gek4C5h5QqJGE81It5ag9s06fdgAyaNHNO9Onsl0t3jioO3Q7-e5mQB956jvOdVwXfumgfVBozOg718YDVbS1X_bnPSITYck-RPuOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور هائیتی در مجمع عمومی سازمان ملل خیلی جدی، از پارچ آب نوشید.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/72172" target="_blank">📅 15:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72171">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b973e065b.mp4?token=sTBK3aRFn6995VS79-jW6V-ShDIoWrJAbHaxQ7j2BN9ePfpvUrLYmhdnlBdEl29EpxqZGy-3yiai_f1ZJtrWyenQ_oYzui83sOKLdnhkGIbLLKY1UzEfVOj1saP7xNxHerPEUblTqNf2-SOLibuOG-l1YrdyzgjiqhlMWtba2138babdedfFK2EoX2901oARIdXL7EygK8cZMDzVXNtmQgn_F-1jeGKSTZCuw84IHSuCVSwxkSB6RhlOPOoueD0t1BiJCgnb_U4ttAIXpE72lRR2z9EFR01qCuzR7oNG6DROFKH1QUf6-_VcWuYwGx_WkM838d2yjGdsvlQtY0GO7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b973e065b.mp4?token=sTBK3aRFn6995VS79-jW6V-ShDIoWrJAbHaxQ7j2BN9ePfpvUrLYmhdnlBdEl29EpxqZGy-3yiai_f1ZJtrWyenQ_oYzui83sOKLdnhkGIbLLKY1UzEfVOj1saP7xNxHerPEUblTqNf2-SOLibuOG-l1YrdyzgjiqhlMWtba2138babdedfFK2EoX2901oARIdXL7EygK8cZMDzVXNtmQgn_F-1jeGKSTZCuw84IHSuCVSwxkSB6RhlOPOoueD0t1BiJCgnb_U4ttAIXpE72lRR2z9EFR01qCuzR7oNG6DROFKH1QUf6-_VcWuYwGx_WkM838d2yjGdsvlQtY0GO7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشماتون بریزه، ایران شده مهد عجایب خاورمیانه؛ این آقایی که می‌بينيد لاله گوشش رو سوراخ کرده و یه مار کرده توش.
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/72171" target="_blank">📅 15:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72170">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e89ab3721.mp4?token=u8jqRboLJloR6GpnBr-26clB11NqByNBEh2YFaZegHIM1MsQK5nXhEcRBSIoe_6glyN7Mjsj3J-sP9kuDFD9OxnEzeMJW_b4bOQ_Muxvw_XXpDLc68MdYVJItaLK8s8fQPcN5Wy28Nmeo0Txg4kpXQSK470TavN2Bh3T2bj2OttYQYs7Fdt71-4_hlGVsGKQBqT9LXAQ8Pt0sf8xc9OVRyCcOVdtuQ_C7BjUdX_xV_cwtyrSs9IQRtTJDRQDpr20WE895vSusIBev0836t27QXcygUpySsSsbf-xUNVw8RPPl2acNT0CWIIXTWKljx68Ymi1nJId8zNRMZHU3qTdvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e89ab3721.mp4?token=u8jqRboLJloR6GpnBr-26clB11NqByNBEh2YFaZegHIM1MsQK5nXhEcRBSIoe_6glyN7Mjsj3J-sP9kuDFD9OxnEzeMJW_b4bOQ_Muxvw_XXpDLc68MdYVJItaLK8s8fQPcN5Wy28Nmeo0Txg4kpXQSK470TavN2Bh3T2bj2OttYQYs7Fdt71-4_hlGVsGKQBqT9LXAQ8Pt0sf8xc9OVRyCcOVdtuQ_C7BjUdX_xV_cwtyrSs9IQRtTJDRQDpr20WE895vSusIBev0836t27QXcygUpySsSsbf-xUNVw8RPPl2acNT0CWIIXTWKljx68Ymi1nJId8zNRMZHU3qTdvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چهره ترامپ وقتی B-1 لنسر وحشیانه از بالای سرش رد شد دیدن داره
🤣
انگار اصلاً نمی‌دونست داره میاد
😂
قیافه شی رئیس جمهور چین دیدنیه
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/72170" target="_blank">📅 14:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72169">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAGwXhtDlgzUiIgpEKR_YPVkOi2wQB3JL1pFxfwQOjwOkEOI-Ilfw71Q4p_WQaYaBu69BVPMP27t80DjfkJ_mRlvfoaY-4soWt9dDwMziGQ1umZgUYf51eSjOVAnne9CnKk7JLEIF0pHKMfL2rCTYhf4rZ-KX6i7DaVSz8M5SMCzrlo3oz3EKeJystCctFu5LxPZ_oZt6woO0FNFLRUPTWjmN8jf7K1NOOuvVHqooLyamMKpDBDl6KDs8lnFX-nV-h1wCHs-o4l2Q-C2tbFutW1-IKPhE-Ji_VP2YsoiId-butUXeniayZNWdn0cRtA9koVgNbIg0ZGs9tbr-6xB2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش ایسنا و به نقل از سازمان هواپیمایی کشوری ایران، تمامی پروازهای شرکت‌های هواپیمایی ایرانی به مقصد امارات از نیمه‌شب لغو شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72169" target="_blank">📅 13:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72168">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f0e98c345.mp4?token=AO51_RrWOgivMK4hdVmIsL4TKMrLqZskGenuROzJ4xaL9yCjf1kO0Xr2U2XWFNLkR9XX9LG8qlHvA9t_cDl80uTXwwKhgRhJPv9MwqO8k9brSC4V6Y8uOQAxzRBescVbUXI_gWf901dwk1LYhH0tMRBAcECIvLUT3y1kBZWaSufnNxbSDgSSE-Lu8Wq5NVJ50fVJkkuGJD2cJW60ixyg-jH24PhFpxpSBkwURcPf2S_gpMgSxQnX5VuDZMfXFKAOwHkbm3n8P-WFxFdF_1Q6SA_dpb3SX2D2uq0JDUDFxebQJEA_xb9P6o8TzyxbXZEWpbLR3WKuojtFDsaRmbNyP173xWHKkagPR7sklOC0-U5CBBDgH6656RUqoUISP259Fon7VGUGFpuqP9NM05T3ebxPpFM6dO9lBlqbIWm7YkqFp-_Hdo2Zl0H0Bo_MobfZwsYTzNqelBUb30rvpE1_g_GGfYPB8c8oXYLmyZYeIEiYT1kNp98UKXZ9ZIw3CFMbdydT4wuVqMSLh_mKEZN40sbLnAF8BmxtCvtuI2zr3A2_RG4eGFEI20rd2mpgEslo6x094lZ2hTqUzR-G3EeQYrP-P3afV-VHzltGnyfl04dUPA8WNE1guvmtHLX8YY8WHli1_gr1FfEgb4_cxctyqAFP73ud1O4PtvM4nLBEGzI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f0e98c345.mp4?token=AO51_RrWOgivMK4hdVmIsL4TKMrLqZskGenuROzJ4xaL9yCjf1kO0Xr2U2XWFNLkR9XX9LG8qlHvA9t_cDl80uTXwwKhgRhJPv9MwqO8k9brSC4V6Y8uOQAxzRBescVbUXI_gWf901dwk1LYhH0tMRBAcECIvLUT3y1kBZWaSufnNxbSDgSSE-Lu8Wq5NVJ50fVJkkuGJD2cJW60ixyg-jH24PhFpxpSBkwURcPf2S_gpMgSxQnX5VuDZMfXFKAOwHkbm3n8P-WFxFdF_1Q6SA_dpb3SX2D2uq0JDUDFxebQJEA_xb9P6o8TzyxbXZEWpbLR3WKuojtFDsaRmbNyP173xWHKkagPR7sklOC0-U5CBBDgH6656RUqoUISP259Fon7VGUGFpuqP9NM05T3ebxPpFM6dO9lBlqbIWm7YkqFp-_Hdo2Zl0H0Bo_MobfZwsYTzNqelBUb30rvpE1_g_GGfYPB8c8oXYLmyZYeIEiYT1kNp98UKXZ9ZIw3CFMbdydT4wuVqMSLh_mKEZN40sbLnAF8BmxtCvtuI2zr3A2_RG4eGFEI20rd2mpgEslo6x094lZ2hTqUzR-G3EeQYrP-P3afV-VHzltGnyfl04dUPA8WNE1guvmtHLX8YY8WHli1_gr1FfEgb4_cxctyqAFP73ud1O4PtvM4nLBEGzI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:جمهوری اسلامی در نهایت تسلیم خواهد شد.
نمی‌دانم یک هفته طول می‌کشد، یک ماه یا دو ماه، اما آن‌ها سرانجام تسلیم خواهند شد.
هدف در اینجا می‌تواند یکی از این سه حالت باشد:
اعضای رژیم به جان هم بیفتند؛
نوعی قیام مردمی در ایران شکل بگیرد؛
یا اینکه ایرانی‌ها را متقاعد کنیم که اگر خواهان توافق هستند، به آن پایبند بمانند.
این بار، اگر توافقی حاصل شود، تضمین می‌کنم که آن‌ها به آن پایبند خواهند ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72168" target="_blank">📅 13:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72167">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb27b8d8bc.mp4?token=VbF8QtOVr-jUZJIchRw-nV-2_NPYBIMvlzAXwT8UzWT3cTpNX2Xu2j-04fd2gSO2Ziu0sFOTnlR_N2nUJHgT6CfTFldJrkK7V5P74JpXNDvOwNf-YLBDQUY3Ftgex0WkjTQbGYC0fOG_0DSQVUa3vUHvUhzDb6QD-952ZKQxHslnwYSjl9Ua3cPADiCozNap-C5IU6mKdpO6upjhY8pnr234_mEct1V8m_BM9knSr5JnLzNtQ5kb6a_FsRWQgwCuQz-7q8oNOd9ICyo5qi2t76YN7UP1AcgN-kEeQIwF9C2FeRl4VDEaEiTNWk_yFy39S8RsKG1Ujoi_ZjyegBv87A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb27b8d8bc.mp4?token=VbF8QtOVr-jUZJIchRw-nV-2_NPYBIMvlzAXwT8UzWT3cTpNX2Xu2j-04fd2gSO2Ziu0sFOTnlR_N2nUJHgT6CfTFldJrkK7V5P74JpXNDvOwNf-YLBDQUY3Ftgex0WkjTQbGYC0fOG_0DSQVUa3vUHvUhzDb6QD-952ZKQxHslnwYSjl9Ua3cPADiCozNap-C5IU6mKdpO6upjhY8pnr234_mEct1V8m_BM9knSr5JnLzNtQ5kb6a_FsRWQgwCuQz-7q8oNOd9ICyo5qi2t76YN7UP1AcgN-kEeQIwF9C2FeRl4VDEaEiTNWk_yFy39S8RsKG1Ujoi_ZjyegBv87A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی دبیر شورای عالی امنیت ملی رسما فرودگاههای کشورهای همسایه را تهدید به موشک‌باران می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72167" target="_blank">📅 12:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72166">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd3cb8e2e.mp4?token=F8YSFgrhVwUNP9NQFtsiQGzbSdrUoS6GCSHAZp3tyrOVSMAvUJMWX5t92FAJ1v5Idhg8VP8o1Q91M3_VBRfkq6ZQn9zUvDZqS5jzHcABMh9t8Qlh15J3Sjiw0m2M9odQEz6iXLmdDJkY3epu4O72BG7CkFlKjs05zFxW3q9P8HVzgT6cHc9uGpBuwN6o2W8kTIwvi7ObUXOu0AsueGTbqign9vIMgK72u5d3E062eh2DhNL3tSWTU2JZBkR1UUt0W3EpM1KZiXZGLsbRMLmjdfefCEJMI7Z6zbL7H6cruxmsgtijVbOFyqU2JUn_5-AJkUop5dU_mkvOohbtEgAgHn_N9iBlADjdWozl2plaPkfnYzt-z78-XWfNPCXLTJDLLNPgCClJutRyD-3DAGOvTQ1TTDetETGDuiYc1OHShZQDmDKnmcKO5J-fRT4G2YbWOB72TFYXpKYjKcxZniQsgdRecZFKZTzE6UhrgSnPw-axux6Pk18PT0ibnoMrun4ABdGiXrWUggiIe748vMhaPAyQVtNx2kgVZYODsl48YN8KoFQ0tyjGK7Uqfys2JvZAtdKXYjqZpeFES2xJhIFap2HQj_a4wwt2GvWTmPqGLbmKtC3wndo2gHTAQAhx-WxU3sRgO7avP13segTlrba9S3-CP2lzq-zrHdsk2MGD9JE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd3cb8e2e.mp4?token=F8YSFgrhVwUNP9NQFtsiQGzbSdrUoS6GCSHAZp3tyrOVSMAvUJMWX5t92FAJ1v5Idhg8VP8o1Q91M3_VBRfkq6ZQn9zUvDZqS5jzHcABMh9t8Qlh15J3Sjiw0m2M9odQEz6iXLmdDJkY3epu4O72BG7CkFlKjs05zFxW3q9P8HVzgT6cHc9uGpBuwN6o2W8kTIwvi7ObUXOu0AsueGTbqign9vIMgK72u5d3E062eh2DhNL3tSWTU2JZBkR1UUt0W3EpM1KZiXZGLsbRMLmjdfefCEJMI7Z6zbL7H6cruxmsgtijVbOFyqU2JUn_5-AJkUop5dU_mkvOohbtEgAgHn_N9iBlADjdWozl2plaPkfnYzt-z78-XWfNPCXLTJDLLNPgCClJutRyD-3DAGOvTQ1TTDetETGDuiYc1OHShZQDmDKnmcKO5J-fRT4G2YbWOB72TFYXpKYjKcxZniQsgdRecZFKZTzE6UhrgSnPw-axux6Pk18PT0ibnoMrun4ABdGiXrWUggiIe748vMhaPAyQVtNx2kgVZYODsl48YN8KoFQ0tyjGK7Uqfys2JvZAtdKXYjqZpeFES2xJhIFap2HQj_a4wwt2GvWTmPqGLbmKtC3wndo2gHTAQAhx-WxU3sRgO7avP13segTlrba9S3-CP2lzq-zrHdsk2MGD9JE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«پرواز هواپیمایی وارش» از «تهران» به «دوشنبه» _پایتخت تاجیکستان_ از مرز هوایی لغو شد و به فرودگاه امام خمینی بازگشت.
این هواپیما سعی داشت از مسیر جایگزین و از سمت آذربایجان وارد تاجیکستان شود که مورد موافقت این کشور نیز قرار نگرفت
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72166" target="_blank">📅 12:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72165">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72165" target="_blank">📅 12:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72164">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAwMfgMjEonGIajxScOGkVoWN7AKj6e0-dn-lklao6PrGQruqIe4tWJRJsGRjEZV-EIY6ksQWShQfKjWVbzk1X6FrxeJt5GjB8d72w-QFH-fMEJAcWuZG5cbO1oiyxqRJ9jJgXo7sJwFeK-ioUgBoLn6P_d17md5Rxn5yhBgR7FR8kSKzwhJI_WbYPwkzx-KwWbJ9lOJUA8K8ffafyoFfo0jSI3c63DcBvDPUEj5_XaAzJyhypG4TdITzWPTum8HQxkwYogTkXUvm9e2TUqxpnLb9dfM2wn0tkll1S1mJ6z4V7yaER_58tEJPCsFV-zi44ym_EBKtxPZBXNZo3OiXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آلمان
🆚
هلند
دانمارک
🆚
نروژ
ولز
🆚
پرتغال
اروگوئه
🆚
ژاپن
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
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72164" target="_blank">📅 12:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72163">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2bbdedf07b.mp4?token=EzvTNuRqbsErtQhLAQarbSXwihbqt3tBqZ4qNIFM-o9rQaa-j-0vMQw2jsgKEyzJn9GkACjwaaI8UeEINs9awPt8TrMTH4Rs7aSaMxUL0y1z7AT6qBZlBtxlwRwdYZQYtdQn-czFiDA1ScTen7C7xzn8Cbub_xgB6TAux387GVpkp7M-Z_tTH5Rr0zVlz-eYtRs_FADfc8DIeUx02DloRPgZ1VlU9x-Vo5Bfgk4BeqFDseGs7OEo8tTS0L9g9bsdaDmOaV_eGfPsRk0KAbEqfuO5iIMnewnzGX2oq4Pd67BNkbDee32hrvAHEFUZ-GCkiIR5q5MU5B-YoSwXqOMRfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2bbdedf07b.mp4?token=EzvTNuRqbsErtQhLAQarbSXwihbqt3tBqZ4qNIFM-o9rQaa-j-0vMQw2jsgKEyzJn9GkACjwaaI8UeEINs9awPt8TrMTH4Rs7aSaMxUL0y1z7AT6qBZlBtxlwRwdYZQYtdQn-czFiDA1ScTen7C7xzn8Cbub_xgB6TAux387GVpkp7M-Z_tTH5Rr0zVlz-eYtRs_FADfc8DIeUx02DloRPgZ1VlU9x-Vo5Bfgk4BeqFDseGs7OEo8tTS0L9g9bsdaDmOaV_eGfPsRk0KAbEqfuO5iIMnewnzGX2oq4Pd67BNkbDee32hrvAHEFUZ-GCkiIR5q5MU5B-YoSwXqOMRfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که یه پسر از روتینش قبل از رفتن به مدرسه منتشر کرده:
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72163" target="_blank">📅 11:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72162">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa04cd3fe8.mp4?token=m8gxOTVduvxl-STCaot23Q5Cffh2AxIqSmuJ__2-dejxVU13AGAByzkwlcpOeAIEbqpbLFK0k3UKf60njn52aN8232IBBrqjD6M0xlVSf02jA626LF5PJAd34h1Hh_zsW0anq1QtCa0POsDG4ES_99oMrAVmEzLsZRNwucczt0x189B6TpmELbMtk91cS6h2M7-Ejp3qzDnqj-A2hgwXLPt2E_OrNgWnwW2Cg6eU5GF34j1Svnfn-XQhaKGsD3Qyo0_2BN65tnIGfXisnh4WhhcNF8QsUF-aYKWkkrgFQUAidsZvz3OwOQJj8mkdOYoAm7YMOD2kZE0hFIYxTm-ALLpU_KXZs4OhO-PWxCexF6WcRwI-ca-92A6oHLqLxXDewhCushSJwyT450-Z7L06a_M9NNaKDEqsLGyY6YjiAaUZoAZHZOYkTnUNT3CiFp15yKl2lh8R_DzL1IOX5xjXgVycuplFnOHEyA45SqyKWhj_zacbitZyW3rxnO3k1l_yoP7HJGHF4yr7UqgXm4YDgfZbjXt0TYNnNYxOgAOIvXDez4gGIhIhBhbpEeIbLNehNBkNkxIJZyFDzuigZfCkaJRJCiHVCy0PivJhd1K7rhPVbbnUA3FJDfRA6AhBNcG3drMOGCjujOguyLnrU-MBkpD1q18UBvXv0doF85hU2ZY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa04cd3fe8.mp4?token=m8gxOTVduvxl-STCaot23Q5Cffh2AxIqSmuJ__2-dejxVU13AGAByzkwlcpOeAIEbqpbLFK0k3UKf60njn52aN8232IBBrqjD6M0xlVSf02jA626LF5PJAd34h1Hh_zsW0anq1QtCa0POsDG4ES_99oMrAVmEzLsZRNwucczt0x189B6TpmELbMtk91cS6h2M7-Ejp3qzDnqj-A2hgwXLPt2E_OrNgWnwW2Cg6eU5GF34j1Svnfn-XQhaKGsD3Qyo0_2BN65tnIGfXisnh4WhhcNF8QsUF-aYKWkkrgFQUAidsZvz3OwOQJj8mkdOYoAm7YMOD2kZE0hFIYxTm-ALLpU_KXZs4OhO-PWxCexF6WcRwI-ca-92A6oHLqLxXDewhCushSJwyT450-Z7L06a_M9NNaKDEqsLGyY6YjiAaUZoAZHZOYkTnUNT3CiFp15yKl2lh8R_DzL1IOX5xjXgVycuplFnOHEyA45SqyKWhj_zacbitZyW3rxnO3k1l_yoP7HJGHF4yr7UqgXm4YDgfZbjXt0TYNnNYxOgAOIvXDez4gGIhIhBhbpEeIbLNehNBkNkxIJZyFDzuigZfCkaJRJCiHVCy0PivJhd1K7rhPVbbnUA3FJDfRA6AhBNcG3drMOGCjujOguyLnrU-MBkpD1q18UBvXv0doF85hU2ZY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدیداً دوست‌دخترای مردم دارن برای پارتنراشون آیفون 18 میخرن:
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72162" target="_blank">📅 11:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72161">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دیروز صبح، تو یکی از مدرسه‌هایِ اندرزگو تهران، شروع سال تحصیلی رو اینجوری شروع کردن :
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72161" target="_blank">📅 10:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72160">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c86f2846ed.mp4?token=sYL4nwFyiLBMP-_6YGtFMafTdYwj9o0wPxFAZJHGWDuLSTdtCaqwja6mCkrS2QJU1_sxzf7FNlASNh_QouT5HlhVq6n9BN6vZ6Z6kkLNFFGy8IXAa_suiAPIyvekPAJEds7NikmEGhxswzKheoyCGB8H2mdo-LuhdwZzD2y7A0Ty6jW_rL6fx2SCuwroBRjirSjZbY669sWDN68O8tpczosp04x8rE2PIuAk9RcJd4sDWN-Rd-ezIrqHZGAXHMigCruAFTuRFMGTgVU3kTTNooaTZRBaz9ozjAnpPhWW7eZ0uvYvHmbyC5MAV56PA4E4BvDUhJUfomE22gYl3A9mbw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c86f2846ed.mp4?token=sYL4nwFyiLBMP-_6YGtFMafTdYwj9o0wPxFAZJHGWDuLSTdtCaqwja6mCkrS2QJU1_sxzf7FNlASNh_QouT5HlhVq6n9BN6vZ6Z6kkLNFFGy8IXAa_suiAPIyvekPAJEds7NikmEGhxswzKheoyCGB8H2mdo-LuhdwZzD2y7A0Ty6jW_rL6fx2SCuwroBRjirSjZbY669sWDN68O8tpczosp04x8rE2PIuAk9RcJd4sDWN-Rd-ezIrqHZGAXHMigCruAFTuRFMGTgVU3kTTNooaTZRBaz9ozjAnpPhWW7eZ0uvYvHmbyC5MAV56PA4E4BvDUhJUfomE22gYl3A9mbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسره از خروس میترسید و رفیقاش گفتن اگه بتونی 10 ثانیه نگهش داری، بهت آیفون 18 پرومکس میدیم.
و در نهایت این شاهکار خلق شد:
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72160" target="_blank">📅 10:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72159">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/034c3c71b1.mp4?token=L2CUH0FXvygiC5e-Vf_Uq6xtwLKtu5PkmjntJI1n0GVFHDaF3EcyZ7b7XEwo_rYH9nKnZeuTxPB3K4Mqhd3h9u6aiuEsCVK4WfCtBJfsMNY_axDg9M4Lez_ghK_ssr2v-TggVGw0lqE_5Yj_KGC-JIGqDVO7NIaLC9A6NR0wPZrghGnaiCe9SwMRr9S9lk0p2NXV9OIBv38MY5bB0Qv5j9WeGowgTX5Rnsy-rkP6zR4Lte1_UnW5yiI5YbVt-DzyW9ILkD4yFPZpTQwa8VBfNRxMYvBzoVzIyeZ_RsSWBZUGPtLc-Juluae5aqLF7wxLMkinYEkHicfZy0P6zj2irg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/034c3c71b1.mp4?token=L2CUH0FXvygiC5e-Vf_Uq6xtwLKtu5PkmjntJI1n0GVFHDaF3EcyZ7b7XEwo_rYH9nKnZeuTxPB3K4Mqhd3h9u6aiuEsCVK4WfCtBJfsMNY_axDg9M4Lez_ghK_ssr2v-TggVGw0lqE_5Yj_KGC-JIGqDVO7NIaLC9A6NR0wPZrghGnaiCe9SwMRr9S9lk0p2NXV9OIBv38MY5bB0Qv5j9WeGowgTX5Rnsy-rkP6zR4Lte1_UnW5yiI5YbVt-DzyW9ILkD4yFPZpTQwa8VBfNRxMYvBzoVzIyeZ_RsSWBZUGPtLc-Juluae5aqLF7wxLMkinYEkHicfZy0P6zj2irg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم لحظه سقوط یک جت آموزشی RAF Hawk T2 اندکی پس از برخاستن از دره RAF در انگلیس امروز را نشان می‌دهد.
هر دو خلبان به سرعت بیرون پریدند و زنده ماندند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72159" target="_blank">📅 09:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72158">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04b2935ddd.mp4?token=ZLCnnv8-WCcZK2kkl1SYYIbaQL3uk6sJZnqTa2lES1AcDVwfpA51Ibl9C_EdSgE_Bg8K6NvCTF_o1DhEgoQeWsyHpfnjTdv266_Zfj3cBUpadq_jDEJvSIDlzkPfEjb25v4oyEdMQiiqbMkQ930_lOQQghiGEM25DO5WV6KKav8jVAo1rLhpeUiLfabl4VY1vRO6wgHk6p99AXfGNFA664c9P6IU_ZA6akv5foRxeQ66_9Bk4TltOw7suR6Ut08eWAIyXM-r5FJcDGK19Lda1yKJ-WsnFPSEniMs4iI_xSMYNErjsR_fxteE2Qe3niarsm0TsQv_BBaXxBQYGyc-KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04b2935ddd.mp4?token=ZLCnnv8-WCcZK2kkl1SYYIbaQL3uk6sJZnqTa2lES1AcDVwfpA51Ibl9C_EdSgE_Bg8K6NvCTF_o1DhEgoQeWsyHpfnjTdv266_Zfj3cBUpadq_jDEJvSIDlzkPfEjb25v4oyEdMQiiqbMkQ930_lOQQghiGEM25DO5WV6KKav8jVAo1rLhpeUiLfabl4VY1vRO6wgHk6p99AXfGNFA664c9P6IU_ZA6akv5foRxeQ66_9Bk4TltOw7suR6Ut08eWAIyXM-r5FJcDGK19Lda1yKJ-WsnFPSEniMs4iI_xSMYNErjsR_fxteE2Qe3niarsm0TsQv_BBaXxBQYGyc-KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تعجب از  عکس‌العمل بی‌تفاوت نماینده جمهوری اسلامی در سازمان ملل، به تهدیدات ترامپ در یک برنامه تلویزیونی
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72158" target="_blank">📅 09:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72157">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad1a7d8580.mp4?token=nHvcKVMl6zb4I--8lDm8LUwPnjOM2iQ4w6v7YSTGgGdqtnXyZU2_Y57TpYCa9SPMLnIzmPAEGowIlIgGMLQOQnEmqB1dqHXd0hpLQUHo6K4CQsnpNdUHQphSQ-3unaILCEp8D_qJA1nj44EmuECdzvWw9kY6Je9py_s68qzIk8V1mXqvU_SLWd6O8iCNQyq9OKGuHuQvddFOh3s77pMYjtn3a-A61kgs4-Wl9qA7rQU7xva4Kc9ZZHtXqPSmn95ljfxjQGMJHWjwe3kcusGZRoyinMAkw2bMM3g07djkaFI5w072NjgOwHvUz0XM4LSQiIMzlQuJlsWXjmhf2uuaCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad1a7d8580.mp4?token=nHvcKVMl6zb4I--8lDm8LUwPnjOM2iQ4w6v7YSTGgGdqtnXyZU2_Y57TpYCa9SPMLnIzmPAEGowIlIgGMLQOQnEmqB1dqHXd0hpLQUHo6K4CQsnpNdUHQphSQ-3unaILCEp8D_qJA1nj44EmuECdzvWw9kY6Je9py_s68qzIk8V1mXqvU_SLWd6O8iCNQyq9OKGuHuQvddFOh3s77pMYjtn3a-A61kgs4-Wl9qA7rQU7xva4Kc9ZZHtXqPSmn95ljfxjQGMJHWjwe3kcusGZRoyinMAkw2bMM3g07djkaFI5w072NjgOwHvUz0XM4LSQiIMzlQuJlsWXjmhf2uuaCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
ممکن است به نفتکش‌ها حمله شود؛ اما بسیاری از آن‌ها به مسیر خود ادامه می‌دهند. آن‌ها صرفاً به حرکتشان ادامه می‌دهند.
ایرانی‌ها ممکن است ۳، ۴، ۵ یا ۶ پهپاد به سمت آن‌ها روانه کنند، اما نیروی دریایی قدرتمند ما مانع آن‌ها می‌شود.
با این حال، ما روزانه بین ۱۰، ۱۵ و گاهی ۱۷ میلیون بشکه نفت صادر می‌کنیم.
برای درک بهتر این ارقام باید گفت که پیش از آغاز درگیری‌ها، این میزان ۲۰ میلیون بشکه بود؛ ضمن اینکه احتمالاً ۳ میلیون بشکه دیگر نیز از طریق روش‌های جایگزین صادر می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72157" target="_blank">📅 07:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72156">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dfe7fd741.mp4?token=JAtMp7v3ySd6FfwnAE1CyHedbTmfb-ky-YDbZsG1TtmtVzQNi7J2S3lbLYeITlrulwBDptvX0RnziIlk8oh9CFaeWf9UaGLm4U4sd3ZM89xUTJCRqmvEN_r5UWiAAAdD9WOE9TIQOr5Ca0HwZA9urjNN1E1hJSBVCurGV_jIjbmQNwvDpp9uc5ph0HUvhzw_wcJFfellNWuUA0SKiIrmlkKQc1Pdn2mQ5W0o2Tu3KeJk02NVYYVSJpGHFcHndl4PE74bZUgYnG6wqcy2snQZ1w3GRLny6kBlH5wqU6dLfVcbLkoMwAxf5Az4t8-slHHAlpD-blZqIRsX54n6FxuXLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dfe7fd741.mp4?token=JAtMp7v3ySd6FfwnAE1CyHedbTmfb-ky-YDbZsG1TtmtVzQNi7J2S3lbLYeITlrulwBDptvX0RnziIlk8oh9CFaeWf9UaGLm4U4sd3ZM89xUTJCRqmvEN_r5UWiAAAdD9WOE9TIQOr5Ca0HwZA9urjNN1E1hJSBVCurGV_jIjbmQNwvDpp9uc5ph0HUvhzw_wcJFfellNWuUA0SKiIrmlkKQc1Pdn2mQ5W0o2Tu3KeJk02NVYYVSJpGHFcHndl4PE74bZUgYnG6wqcy2snQZ1w3GRLny6kBlH5wqU6dLfVcbLkoMwAxf5Az4t8-slHHAlpD-blZqIRsX54n6FxuXLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
احتمالاً بیش از ۸۰ یا ۹۰ درصد پروازهای خارجی از مبدأ ایران متوقف شده‌اند.
مطمئن نیستم نمایندگان ایران در سازمان ملل چگونه قرار است به کشورشان بازگردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72156" target="_blank">📅 07:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72155">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72155" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72155" target="_blank">📅 01:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72154">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWBhKZ_QBQKomiZWBeNz0LmW4dWcDI6G9UWWYUY6GSuwcDOlziP-n5s1DraBSgWYGgsYho2I83ownXb5guY4mXLUaP2tBYx8RfUF9cF8Tms28s4dkL_4X3AQcAoz0FMCDzu99WK0_q8b-aL4pCoxwNULSkdx5mIOwQGqmvHUEgMQ5s9iLnxt5_K8RzK1oY6Nx8EGzqmEcgiCF2O8yrEEdYvZjjEghyxaBSPShmS6o3mCIFMsfWdjHTG1902uQ-UCqBdKAIfSuyPiJIeyfYNpx3JQUDhjCLcE25668mvWOs2_h1MFYG6CLm9RLAj-zhR574KGGvc-ot5_QfbvVUHzjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72154" target="_blank">📅 01:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72153">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c59219ac7.mp4?token=qJd6XqSvRUNpMH-SPVz2oMWOoMZnDf3eNKQJzB2YM3VQVMnhFr9t-cyhGNFEGy8j-XAnwowj_hkyd6oY9-89vlT0dkZWQnuV4g2yAuJ5qmbEra7Mp89Qh6RgQlOQ3iHd4HtylelPSO7fqONuhnF6UWCA4M6Pla8SjchEsDza7TWtFgb65GCjCxahLt3asA2htMJuzbThI93gdHUT6aHWIkj_KHvyNKAyP-wf_sYcSCE8Ruw0Lo3WaC9V3bXpyxsbU0aw8eSV7HPysJVrpV099Rf0wis8yOYzQBoYfcMYFzUoQv2bF5wyhw-0Hk2s-UKU3Sg0LpSiXJt1cyyDmQhkXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c59219ac7.mp4?token=qJd6XqSvRUNpMH-SPVz2oMWOoMZnDf3eNKQJzB2YM3VQVMnhFr9t-cyhGNFEGy8j-XAnwowj_hkyd6oY9-89vlT0dkZWQnuV4g2yAuJ5qmbEra7Mp89Qh6RgQlOQ3iHd4HtylelPSO7fqONuhnF6UWCA4M6Pla8SjchEsDza7TWtFgb65GCjCxahLt3asA2htMJuzbThI93gdHUT6aHWIkj_KHvyNKAyP-wf_sYcSCE8Ruw0Lo3WaC9V3bXpyxsbU0aw8eSV7HPysJVrpV099Rf0wis8yOYzQBoYfcMYFzUoQv2bF5wyhw-0Hk2s-UKU3Sg0LpSiXJt1cyyDmQhkXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فروند بمب‌افکن B-1 Lancer نیروی هوایی ایالات متحده، همزمان با استقبال پرزیدنت ترامپ از شی جین‌پینگ، رئیس‌جمهور چین، در واشنگتن، بر فراز این شهر پرواز کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72153" target="_blank">📅 01:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72152">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a5acb93e6.mp4?token=JoclJLIJySyKnrxy-QDSRZeOnLyyZ7WzyextMOOzBfs_2vDxoXZ5hZLU0T_QYA0RXXlqEg2NA5N3fhm1msFc3hOJ01f0vr5DA0K6pDcYkuXxsB8nvlKMMfi_JyMYmJxCtIzYjv9--36TbdKYUe9CiAA2G6PowHdM9MEpmcWFMqaZjn2aAc_4icQugi_mpZXv7d7isIpDH7j9nuva8AwU5CARMu5ICTIGutJ9PSauAMek6r5zcm8f3_0iYJ1Sv-_XNhsAx7EkEkzfhTAfYlh_KlTBuO-eTRW59YMA19TVCFAzI-dnJ9eF3xB6Injp8wHUlmwSDIw3hLall6DX_vwhvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a5acb93e6.mp4?token=JoclJLIJySyKnrxy-QDSRZeOnLyyZ7WzyextMOOzBfs_2vDxoXZ5hZLU0T_QYA0RXXlqEg2NA5N3fhm1msFc3hOJ01f0vr5DA0K6pDcYkuXxsB8nvlKMMfi_JyMYmJxCtIzYjv9--36TbdKYUe9CiAA2G6PowHdM9MEpmcWFMqaZjn2aAc_4icQugi_mpZXv7d7isIpDH7j9nuva8AwU5CARMu5ICTIGutJ9PSauAMek6r5zcm8f3_0iYJ1Sv-_XNhsAx7EkEkzfhTAfYlh_KlTBuO-eTRW59YMA19TVCFAzI-dnJ9eF3xB6Injp8wHUlmwSDIw3hLall6DX_vwhvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شنیده شدن صدای تیراندازی در جهاد‌آباد سراوان
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72152" target="_blank">📅 01:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72151">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4470cff685.mp4?token=dH_HPuYGrAuijIlt5SpGMeUwnvKPLzTXVnffXsruilWyUbr2z0T8VQI2QTOcTW8RZNbhc-gSnMm8D4jP9ihPe-zng-1DjOxNUHxrx_Vp9pNxcrKpxqBhWm8Z-5CJ8JUUoPojpCgE1B4R1faod3FeuV49jAHZgtW1KlMNbv1_jwyeoDNvOl8vfH2Vw3R6Gfo7Xy4hgOTKEgVYTH56FDQOv0HUguwzzw6H9Flv4YzxXc9coM6uMSMfrHqoEAh3gq5011SwW2MRsdRPm_qUWXwwQvWjNl9AAQ6_K9t5QmqtdpkVAamogcHpY7KEDZrz192didh2MOPyYO6qKhi6VciKmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4470cff685.mp4?token=dH_HPuYGrAuijIlt5SpGMeUwnvKPLzTXVnffXsruilWyUbr2z0T8VQI2QTOcTW8RZNbhc-gSnMm8D4jP9ihPe-zng-1DjOxNUHxrx_Vp9pNxcrKpxqBhWm8Z-5CJ8JUUoPojpCgE1B4R1faod3FeuV49jAHZgtW1KlMNbv1_jwyeoDNvOl8vfH2Vw3R6Gfo7Xy4hgOTKEgVYTH56FDQOv0HUguwzzw6H9Flv4YzxXc9coM6uMSMfrHqoEAh3gq5011SwW2MRsdRPm_qUWXwwQvWjNl9AAQ6_K9t5QmqtdpkVAamogcHpY7KEDZrz192didh2MOPyYO6qKhi6VciKmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شی جین‌پینگ رئیس جمهور چین وارد ایالات متحده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72151" target="_blank">📅 01:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72150">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رسانه‌ی حال‌وش :
دقایقی پیش تو محدوده‌ی جهادآبادِ سراوان تو سیستان و بلوچستان، درگیری مسلحانه‌ی سنگینی شکل گرفته به طوری که آرپی‌جی هم شلیک شده!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72150" target="_blank">📅 01:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72147">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d2cde76e35.mp4?token=s42UEVvdgnMe6EUTmUifBGzlOB3jT_rYOoZeFFATHpVRfK8YGfI4N2pNWEYRncjGaXWn77-zpkMWX0cm0xZgzBobF63D-kj-s_A5Iek1aIZQxKe-pM29b3VyiEBtgPkQCPl6kdK4dsOeatvPqdnU2T8Wp4C-PbOLihcTPuysalnGyYlzDVq6LSRc_Mn7RQPnTZA45G8jedWqNIltuTFRyT4PANdodwJt0mEdDe8xOum8ba8icg3UNrc-GWENn3L9jh5hTpiuXtWxAc4r7IKriNcfibUh9Bw-04KwjfFimn6jsjARbj_pEZ5orivWenWCXT9fAeKzlPyJfponxXCcOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d2cde76e35.mp4?token=s42UEVvdgnMe6EUTmUifBGzlOB3jT_rYOoZeFFATHpVRfK8YGfI4N2pNWEYRncjGaXWn77-zpkMWX0cm0xZgzBobF63D-kj-s_A5Iek1aIZQxKe-pM29b3VyiEBtgPkQCPl6kdK4dsOeatvPqdnU2T8Wp4C-PbOLihcTPuysalnGyYlzDVq6LSRc_Mn7RQPnTZA45G8jedWqNIltuTFRyT4PANdodwJt0mEdDe8xOum8ba8icg3UNrc-GWENn3L9jh5hTpiuXtWxAc4r7IKriNcfibUh9Bw-04KwjfFimn6jsjARbj_pEZ5orivWenWCXT9fAeKzlPyJfponxXCcOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«اتحادیه دریانوردان هند» (Forward Seamen's Union of India) خبر مرگ یک دریانورد هندی را بر اثر حمله نیروی دریایی سپاه پاسداران با دو موشک کروز ضدکشتی به عرشه C و موتورخانه کشتی فله‌بر «MV CAPE DAO» اعلام کرد.
کشتی «MV CAPE DAO» متعلق به شرکت «ForthMarin Corp Ltd» است که در امارات متحده عربی مستقر می‌باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72147" target="_blank">📅 23:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72146">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rp28E_J__NrOIiiZvkXUHr7YD5I2oiV4qrIYWVBeTLKOr8wJSfQXY0bykeex0Mo2qhjphzLgznT5DxsCadps-RMdDYpDdHPwSnuXgYV8TiBLxzOnsmQ5ZVFTtudP2-WBYxNjGipeEOCU-g157feGzfdEZmJVQKbRpu7gtFdx1cZ6GOruWJ6BrwHRFlNkMERSbzUfn_QVBqgmEyuCYux79eoPJmOHkpYfQAcbvBvbRdTw8NGv8jYY5FCQAj-MhmqylFvM6vEJ84aDFE5fOXxOK__9bS6NyViO8LZFi7P4F5Tp2lzpq8QMOWWZM1Mx0HmN8joNBK5TnpavPWfmJGm-pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار ظریفی فرمانده سپاه شهرستان سراوانِ سیستان و بلوچستان، توسط افراد مسلح ناشناس کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72146" target="_blank">📅 23:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72145">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/223e8fa625.mp4?token=GAW6BRuxxs6Eh0UfeHhCspTkHLrTsyZ8W98MAVplSHkUWqExS0jyFW5SA8h8Vn8HMkl_AucDtsSssaiP3i1wbKctj7o8k-0nQTU5QsNfc0JTvh3FA1gAlezqXyFGHwG9knvNGNMoMhrDyMvWe3St0e3nxBllpEbwNvMLWicffiztOpdjYOKDfBLpdk6ph_Iraf-rczy-r2qQl3Ondm94-XXEd751KMR7tfZfL73-oX4bMR0y0wmamv0V44S3_hw81RludlScfnGcK7zdBuvsRCAFDp1f_Aoia7mzRAtE30YiIvvNfvBIOh_tPaz3iC5G755UsNplMi5CZNj5grQ5Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/223e8fa625.mp4?token=GAW6BRuxxs6Eh0UfeHhCspTkHLrTsyZ8W98MAVplSHkUWqExS0jyFW5SA8h8Vn8HMkl_AucDtsSssaiP3i1wbKctj7o8k-0nQTU5QsNfc0JTvh3FA1gAlezqXyFGHwG9knvNGNMoMhrDyMvWe3St0e3nxBllpEbwNvMLWicffiztOpdjYOKDfBLpdk6ph_Iraf-rczy-r2qQl3Ondm94-XXEd751KMR7tfZfL73-oX4bMR0y0wmamv0V44S3_hw81RludlScfnGcK7zdBuvsRCAFDp1f_Aoia7mzRAtE30YiIvvNfvBIOh_tPaz3iC5G755UsNplMi5CZNj5grQ5Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواننده رپ آرمین رابر، برگزار کننده میتینگ های خیابانی رپ در اطراف تهران بازداشت شده است. او پیش تر نیز به دلیل اجرای قطعه آقازاده بازداشت و به حبس و جریمه نقدی محکوم شده بود...
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72145" target="_blank">📅 22:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72144">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تسنیم گرفت رو عراقچی:
تعامل عباس عراقچی، وزیر امور خارجه، با استیو ویتکاف، نماینده آمریکا، بدون مجوز یا هماهنگی با مقامات ذی‌ربط ایرانی، از جمله شورای عالی امنیت ملی، صورت گرفته است.
ادعاهایی مبنی بر اینکه این تعامل از پیش به تأیید نهادهای سیاست‌گذار ایران رسیده بوده، نادرست است.
بر این اساس ضروری است که آقای عراقچی درباره این اقدام غلط که مخالف مصالح و‌ منافع ملی است به نهادهای مربوط و ملت ایران پاسخگو باشد که با چه محاسبه‌ای این خطای بزرگ را مرتکب شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72144" target="_blank">📅 20:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72143">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d86a283f5.mp4?token=dfaEQY94catmOEyKgtzlRBXofGnSN5equcl1ae1ifg28EjAypKxeUEaw45ZafNxWgxTjttwq-ZsI82Z_wdo-GX48KgRn6DNGmoqIHAAXnV5-BxHQ3s1o_k3LhNQVgWYvkbSnVsj0aBGKCtilKYIdp4FV-Cbc0QXuaW8RL-zu_zCeXHV4F5gj8-j0cpTycN4R7I6V1EjRAMg0HkMENmoLoNQtiLlTAhA79nEr9xo3bHGG3PcVohTCGAZrp7GEZIq3z4yRcLTzDexqsmVPgkmeBNqnjFxQk5p_BJfyafxR0-V_tjqSIVSKIqPCgFMwiNgb7-QojNGKO-OCcCbqlXa27w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d86a283f5.mp4?token=dfaEQY94catmOEyKgtzlRBXofGnSN5equcl1ae1ifg28EjAypKxeUEaw45ZafNxWgxTjttwq-ZsI82Z_wdo-GX48KgRn6DNGmoqIHAAXnV5-BxHQ3s1o_k3LhNQVgWYvkbSnVsj0aBGKCtilKYIdp4FV-Cbc0QXuaW8RL-zu_zCeXHV4F5gj8-j0cpTycN4R7I6V1EjRAMg0HkMENmoLoNQtiLlTAhA79nEr9xo3bHGG3PcVohTCGAZrp7GEZIq3z4yRcLTzDexqsmVPgkmeBNqnjFxQk5p_BJfyafxR0-V_tjqSIVSKIqPCgFMwiNgb7-QojNGKO-OCcCbqlXa27w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنتاگون ۶ مورد دیگر از فایل هایی که در آن اشیا پرنده و ناشناس به اصطلاح UFO دیده میشه رو منتشر کرد که دو مورد اولی در خاورمیانه ثبت شده هست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72143" target="_blank">📅 20:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72142">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9819ac349a.mp4?token=C9QJDktPn22Az5ST5ngUGN7m9HkgjD_XqkVTZksLULVizZGyxJxNK8N0AB-0P1RBUPCkLSiRznIvNT1YMc76YPROYyrEa4vL1IRkt7LCkX0KEFEzWx0wjlZyJYsvP6dbHfIIaDLx78W9Ouw7JlWTmABLkSr1cFitusiSq7NAkus17CTZu_Urrvg3GKQKmRAPKJXiJPDElnEmdttEHfUUSJa3gynFPLMEwMpkNWiQuvqJFb9M_lFrNW83H0O7qdxZwXDtcPMQCf22BjMygBAX0zwVXTYOajMBMryWY3aJUauFJ-7GrRPzNv1HmqOX8dP2JzY7QEw9ymE_tJldWPfcjIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9819ac349a.mp4?token=C9QJDktPn22Az5ST5ngUGN7m9HkgjD_XqkVTZksLULVizZGyxJxNK8N0AB-0P1RBUPCkLSiRznIvNT1YMc76YPROYyrEa4vL1IRkt7LCkX0KEFEzWx0wjlZyJYsvP6dbHfIIaDLx78W9Ouw7JlWTmABLkSr1cFitusiSq7NAkus17CTZu_Urrvg3GKQKmRAPKJXiJPDElnEmdttEHfUUSJa3gynFPLMEwMpkNWiQuvqJFb9M_lFrNW83H0O7qdxZwXDtcPMQCf22BjMygBAX0zwVXTYOajMBMryWY3aJUauFJ-7GrRPzNv1HmqOX8dP2JzY7QEw9ymE_tJldWPfcjIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از هموطن‌ها رفته یه مرسدس بنز خریده؛
همه منتظر بودن از خریدش ذوق کنه ولی صحبت‌هایی که بعدش کرد، جالب بود :
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72142" target="_blank">📅 20:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72141">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اگه هنوز دنبال یه کانال و گروهِ «واقعی» برای پیش‌بینی می‌گردی، درست اومدی!
👑
✅
تحلیل‌های اختصاصی و رایگان
✅
ضریب‌های طلایی
✅
گروهِ فعال برای تبادل نظر  وقتت رو با کانال‌های فیک تلف نکن. حرفه‌ای شو و با ما همراه باش.
👇
[لینک کانال] https://t.me/+fyrt-rnxFjNjMmQ0…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72141" target="_blank">📅 20:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72140">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCBJ_qzmUQlF9hfwIzZPIe6kQCL4CUxfwX_38tXtphH3b4r3JiHUYgePaIyzifpyQqeoNgR-r-yUb1zMt1zGasIdjv-CvL1S0bBgQrBqkE5J9YCaVGNyY4NmQ9Y1ISNk0z4GKJkVKY2uj3mwEu46A74DG6_2OYiEfiHMVe7W72loIzEWscZllO-w3GCfbqcwtrSzDM8W_FzMbQYC8mAipdGfAdvY0QTIvW7SY2qnCYLLRh8Uc0icpA_WJZ7q52C_oSBZZuv_DoX3mUR_il4YImdBA256UcQ9U3DKbXxWqIDacLpyM_kxmkNInlLimmLHez0rolsDlzoA2o73iB9O0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه هنوز دنبال یه کانال و گروهِ «واقعی» برای پیش‌بینی می‌گردی، درست اومدی!
👑
✅
تحلیل‌های اختصاصی و رایگان
✅
ضریب‌های طلایی
✅
گروهِ فعال برای تبادل نظر
وقتت رو با کانال‌های فیک تلف نکن. حرفه‌ای شو و با ما همراه باش.
👇
[
لینک کانال]
https://t.me/+fyrt-rnxFjNjMmQ0
[
لینک گروه
]
https://t.me/+jpSLBx8PcgBlMWI0
#TipsterPersian
#سود_تضمینی
#شرط_بندی_فوتبال
»</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72140" target="_blank">📅 20:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72139">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fa977cc40.mp4?token=lpcs_ZgKrwKch1JzIFJsfpzzvBzhzjy4cfIOvgXoWLw0IurIB_YLTEbieuOg3BxKUQkNArrVZZoUZ8PTua1JkUwDGQ8aFjwi2q6dFNZkb15VOCtkpF9CoQUjib29cI5SfHbiGzaJ-1BOMK9A1ibrdwTsLLrwY9r7yXa5w40Y3-USLFMT9vVkJq5Q92A4CfES7QazbKx_FDJ9R4mlp6n3U-1t4nL-yf95kGU_cycW617ONpOye7-zWA6d9_z2BccnEKj03-K6DmFAJQD2kb-PBW7zLvuCV-iUBTHanbfwdIqqbcgkD5mmA-c1hiUJF2e3A3csJM5Z8keZiWgMEMBQfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fa977cc40.mp4?token=lpcs_ZgKrwKch1JzIFJsfpzzvBzhzjy4cfIOvgXoWLw0IurIB_YLTEbieuOg3BxKUQkNArrVZZoUZ8PTua1JkUwDGQ8aFjwi2q6dFNZkb15VOCtkpF9CoQUjib29cI5SfHbiGzaJ-1BOMK9A1ibrdwTsLLrwY9r7yXa5w40Y3-USLFMT9vVkJq5Q92A4CfES7QazbKx_FDJ9R4mlp6n3U-1t4nL-yf95kGU_cycW617ONpOye7-zWA6d9_z2BccnEKj03-K6DmFAJQD2kb-PBW7zLvuCV-iUBTHanbfwdIqqbcgkD5mmA-c1hiUJF2e3A3csJM5Z8keZiWgMEMBQfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتظار می‌رود سخنرانی نتانیاهو در سازمان ملل به شدت بر ایران متمرکز باشد و به گفته‌ی ایدز، این سخنرانی حاوی «غافلگیری‌های» نامشخصی خواهد بود.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72139" target="_blank">📅 20:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72138">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پزشکیان:
تو منطقه هیچ کشوری به تنهایی امنیت نخواهد داشت، یا باهم امنیت رو می‌سازیم یا باهم تو ناامنی زندگی می‌کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72138" target="_blank">📅 20:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72137">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15be798879.mp4?token=HOzqY5Qwmp1IKPCJt3U4Rwwi2s6_hbUHEJ_p7Bk8NLoAeTOx8Kp05R8k78I8lOG9PYJ8Yk7hGDWBfreb_QF6eFVNJv1QLxZ2YU0cPJXcZSbIbJfQSn7CVXzomCS3ntBb6uzxMqqHTuxMnyrpdK6d_qumWnDIXO91ujeuFGDeg1HXQGIgvHciLb64XyAsJGXSv1ab3kfI-Sz-vCyCS42FzHkt4Cw-Q7bObw4fJp8MtAU7Pdt8UDAH-Z8MAAsx0aHn-A7EuUdhls3hQd-6QQC_6Xb7_38ptBpGPqqwpIqonO4EGheoMSS23wIvkMqq16muwENqx05ocW9tCtDE91HSgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15be798879.mp4?token=HOzqY5Qwmp1IKPCJt3U4Rwwi2s6_hbUHEJ_p7Bk8NLoAeTOx8Kp05R8k78I8lOG9PYJ8Yk7hGDWBfreb_QF6eFVNJv1QLxZ2YU0cPJXcZSbIbJfQSn7CVXzomCS3ntBb6uzxMqqHTuxMnyrpdK6d_qumWnDIXO91ujeuFGDeg1HXQGIgvHciLb64XyAsJGXSv1ab3kfI-Sz-vCyCS42FzHkt4Cw-Q7bObw4fJp8MtAU7Pdt8UDAH-Z8MAAsx0aHn-A7EuUdhls3hQd-6QQC_6Xb7_38ptBpGPqqwpIqonO4EGheoMSS23wIvkMqq16muwENqx05ocW9tCtDE91HSgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این خانم معلم قبل از شروع مدارس، برگشته به اولیای دانش‌آموزا میگه؛
بعضی از دانش‌آموزا هستن که پدر، مادر یا هر دو رو ندارن ؛
پس وقتی میاید بچه‌تون رو از مدرسه بردارید انقد قربون صدقه‌ش نرید که دل اون بچه یتیم بشکنه، برید یه جای خلوت‌تر بهش ابراز محبت کنید
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72137" target="_blank">📅 20:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72136">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bcb578f315.mp4?token=kbnRxCW-W6PHsLsEiJQcoHv1UStPUazNdRWEB_YsOE25AddNRi0W6s4n2mKXcffK1JcrXkNi8p3ASm0eUwaSs2xoBkVT6IMK8HEhFTrUTH009sOSWc2p5AIQQGeNVwTolAJsRTBi-Lh27CQRC4IFwF6SRbMPRndJMFOEBiD0l7sxOWZvHs3uFQDV-mGw2KX1Q0DH5qWYAHrqelUG1IZZntWrYKl-i_I6bjvkXL53aooxX9pTOOerPkK3K0yBQ5_NnZAhbg9rVX0mP0vzpRqvHyDAPygEsYeEchHQw61kpiTboOHl4kaJCVnmasn-69z-kW83WNJ5cNP4sCLoYdIxQg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bcb578f315.mp4?token=kbnRxCW-W6PHsLsEiJQcoHv1UStPUazNdRWEB_YsOE25AddNRi0W6s4n2mKXcffK1JcrXkNi8p3ASm0eUwaSs2xoBkVT6IMK8HEhFTrUTH009sOSWc2p5AIQQGeNVwTolAJsRTBi-Lh27CQRC4IFwF6SRbMPRndJMFOEBiD0l7sxOWZvHs3uFQDV-mGw2KX1Q0DH5qWYAHrqelUG1IZZntWrYKl-i_I6bjvkXL53aooxX9pTOOerPkK3K0yBQ5_NnZAhbg9rVX0mP0vzpRqvHyDAPygEsYeEchHQw61kpiTboOHl4kaJCVnmasn-69z-kW83WNJ5cNP4sCLoYdIxQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه زنه با شوهرش رفته بود خرید که شوهرش این حرکتو زد و آبرو برای زنش نذاشت :))
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72136" target="_blank">📅 19:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72135">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff0aa24390.mp4?token=R2Sf2NCNkSYqfqpxFRzyeew4uDlBJqFu1zqu22Ii3gIKFiQJl4caPWkXN1L8AUgRQEBal_UDgR9_FSMinIZ81dVXHLvdexq-f8OiL-QZzsVrzbdIL2oZjgarS0MVcKYs0BD-xOTh677SVKgrhKfCldLimAiF26TX4dFlIlFb2AEOGFXRiuFoziQOfUF34EU10gkjueUTmQ3sBZ5swyFyG5Nz99gsTPYb1j8ZURP2xj_dBog0RxBOTYtuon3tnIgsN18tXKkT82iuJvIikobqzZA6bHvy9MmpCOm0FIfhqcSVXUi5hv_ODzNA47uB5QQG5bGUIdCa_ehW54M4ZVLtdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff0aa24390.mp4?token=R2Sf2NCNkSYqfqpxFRzyeew4uDlBJqFu1zqu22Ii3gIKFiQJl4caPWkXN1L8AUgRQEBal_UDgR9_FSMinIZ81dVXHLvdexq-f8OiL-QZzsVrzbdIL2oZjgarS0MVcKYs0BD-xOTh677SVKgrhKfCldLimAiF26TX4dFlIlFb2AEOGFXRiuFoziQOfUF34EU10gkjueUTmQ3sBZ5swyFyG5Nz99gsTPYb1j8ZURP2xj_dBog0RxBOTYtuon3tnIgsN18tXKkT82iuJvIikobqzZA6bHvy9MmpCOm0FIfhqcSVXUi5hv_ODzNA47uB5QQG5bGUIdCa_ehW54M4ZVLtdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
آقای ترامپ و کسانی که به دنبال زورگویی به ما هستند، باید ایران را بشناسند:
اینکه ما آماده گفتگو، دیپلماسی و مذاکره هستیم، اما زبان زور را نمی‌پذیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72135" target="_blank">📅 18:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72134">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80dd97167.mp4?token=T8XpfkABX_ZS8cpPVRZfUA43r1P6G08AYRvMDRBv8TTJye7W1k4En_woJgdPuH27pAaqETLdnQQ6S4oXWKeKl8eybg5WEz1i889dYABCRUvpDIkUCSyxjemW5efP-2roxK4Otcnt7DLoDcAHZP1rL7TC-r0qpj88Hr7-U7fDx8UNJHP2zX5GvN_4Ao_vtQIUGvtrr90FdfmfExyw8_g2A0d8uYGZBY7Xq-MSMaecOwLNeq11iJRKpKhkxz2MyhrgHe0gLC9WfOID38sTDXOSZAO3FIYW5BdlDktDFISpN4k2foxDO01CgX5MghH6e0qHNYylrondntIzItaxHTKmiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80dd97167.mp4?token=T8XpfkABX_ZS8cpPVRZfUA43r1P6G08AYRvMDRBv8TTJye7W1k4En_woJgdPuH27pAaqETLdnQQ6S4oXWKeKl8eybg5WEz1i889dYABCRUvpDIkUCSyxjemW5efP-2roxK4Otcnt7DLoDcAHZP1rL7TC-r0qpj88Hr7-U7fDx8UNJHP2zX5GvN_4Ao_vtQIUGvtrr90FdfmfExyw8_g2A0d8uYGZBY7Xq-MSMaecOwLNeq11iJRKpKhkxz2MyhrgHe0gLC9WfOID38sTDXOSZAO3FIYW5BdlDktDFISpN4k2foxDO01CgX5MghH6e0qHNYylrondntIzItaxHTKmiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ترامپ باید بداند که مقاومت ملت ایران در برابر تحریم‌ها، افزایش فشارها و زورگویی‌ها، تنها بیشتر خواهد شد.
ما هرگز سر فرود نخواهیم آورد و زانو نخواهیم زد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72134" target="_blank">📅 18:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72133">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مسعود پزشکیان:
بمب‌های اتمی و هسته‌ای در اختیار رژیم اسرائیل است، اما از بازرسان خواسته می‌شود که به ایران بیایند.
اسرائیل بیش از ۷۰ هزار انسان بی‌گناه را در غزه به شکلی وحشیانه به قتل رسانده است، اما ایران در حالی که پای میز مذاکره بود، هدف بمباران قرار گرفت.
اسرائیل بمب و سلاح‌های کشتار جمعی در اختیار دارد، عضو «پیمان منع گسترش سلاح‌های هسته‌ای» (NPT) نیست و در طول حیات ننگین خود حتی اجازه یک مورد بازرسی را هم نداده است؛ با این حال، همه امکانات لازم در اختیارش قرار می‌گیرد تا بتواند هر پایتختی در منطقه را که بخواهد، بمباران کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72133" target="_blank">📅 18:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72132">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7f87b6f9.mp4?token=d1V14rF5Tku7vI10ZbUp4ZtuHuS_ct4s4Gy7uDIqp2lQ-xa_BIbAlibJa-wda7KZbInS4ftf2P5iCrN-DzEueX2zwfWZfSJAJkzGrp-wk5vWWEmTdnS54kAykJmUdLqX7EGoPeAYH8nQ-ok-JN0pO7GEtptiOrln81hZ7IWvW7NM-JAPDLAEHkXgJfE2MVgIx91Hn_qhREGgsGhNirmYBpFag5JS3NC4q8Zta2PUgYT60U0bzXj5NHjs1Ei89XJZ3MAi2WHy7ymK9Sc0-q73zSm5ykq3KFFSdNN0DNf74nz6HlQPm4Qr7E31noBEuw93TYEIRRU-E32AYNKONEzNS4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7f87b6f9.mp4?token=d1V14rF5Tku7vI10ZbUp4ZtuHuS_ct4s4Gy7uDIqp2lQ-xa_BIbAlibJa-wda7KZbInS4ftf2P5iCrN-DzEueX2zwfWZfSJAJkzGrp-wk5vWWEmTdnS54kAykJmUdLqX7EGoPeAYH8nQ-ok-JN0pO7GEtptiOrln81hZ7IWvW7NM-JAPDLAEHkXgJfE2MVgIx91Hn_qhREGgsGhNirmYBpFag5JS3NC4q8Zta2PUgYT60U0bzXj5NHjs1Ei89XJZ3MAi2WHy7ymK9Sc0-q73zSm5ykq3KFFSdNN0DNf74nz6HlQPm4Qr7E31noBEuw93TYEIRRU-E32AYNKONEzNS4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
مسائل منطقه‌ای ما باید در درون منطقه و به دست کشورهای منطقه حل‌وفصل شود، بدون آنکه به ابزاری در دست متجاوزان خارجی بدل گردد.
هیچ‌گونه رابطه‌ای با یک قدرت خارجی نباید به ابزاری برای تهدید کشورهای همسایه در منطقه تبدیل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72132" target="_blank">📅 18:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72131">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4be5f428e4.mp4?token=ENO-vwY1ZEv_2rAGXyhTVYUgJeG--gP5QKL_owzBg2rybdoWvwGPpnM7FDJAa-ORffcnFYoUU8EdWkWq-tTm4LecmB01jD4oBL76BMEUr1hDDbcUrYDLj9SbFO9QcNHOzOGqb2JgO29oh2bOi535ds3jbBzEKU1vh4ZhVj4_zoyKzUeYuW4YfDAjf_syULlkHdtqsL5mlYfdme34wo9NFCTpi-T5KfWVXioqqjYpf2KZtd74vigPcrT969q4ddW0nojgVeDQOPBi_SgolGNMLsSJyFpWKIAw-n0teMOLiORgWP7CppBNH24IdzgNVnUGH6s2rMh_2Ad56QM6-yFeU3fXNRXv_iD7XUxincb8OtR3ZC42oafPzE03Jrptf4KyPwRbW7WObgX1HkrYcrk4C4YbGl-uH7hI2Oa5_Gx8Vvt_UDSyR-QULRJsvA6tgUZTdJDHDZ7jd9WBuPh7J0HNSe9pXosQ2JQoBQ_3nNPSc9rpIdmRgvTlyF-VCnm3zNCFLbniqVzKUJIIkDgdVVHen_wZ979yvKWJUdVgQCDgLGkTcFWaSSBtFyN0QZdTiy3vJGm4c6lgIAXvwT-Wk8VByPBt_9Qv2Hm05gOwFP5aCNksPmP37HhHLZdZiof-91W-YJII7gUsLQQidZEB43ODUHyy1FDCf1fXa4VwrDPaA2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4be5f428e4.mp4?token=ENO-vwY1ZEv_2rAGXyhTVYUgJeG--gP5QKL_owzBg2rybdoWvwGPpnM7FDJAa-ORffcnFYoUU8EdWkWq-tTm4LecmB01jD4oBL76BMEUr1hDDbcUrYDLj9SbFO9QcNHOzOGqb2JgO29oh2bOi535ds3jbBzEKU1vh4ZhVj4_zoyKzUeYuW4YfDAjf_syULlkHdtqsL5mlYfdme34wo9NFCTpi-T5KfWVXioqqjYpf2KZtd74vigPcrT969q4ddW0nojgVeDQOPBi_SgolGNMLsSJyFpWKIAw-n0teMOLiORgWP7CppBNH24IdzgNVnUGH6s2rMh_2Ad56QM6-yFeU3fXNRXv_iD7XUxincb8OtR3ZC42oafPzE03Jrptf4KyPwRbW7WObgX1HkrYcrk4C4YbGl-uH7hI2Oa5_Gx8Vvt_UDSyR-QULRJsvA6tgUZTdJDHDZ7jd9WBuPh7J0HNSe9pXosQ2JQoBQ_3nNPSc9rpIdmRgvTlyF-VCnm3zNCFLbniqVzKUJIIkDgdVVHen_wZ979yvKWJUdVgQCDgLGkTcFWaSSBtFyN0QZdTiy3vJGm4c6lgIAXvwT-Wk8VByPBt_9Qv2Hm05gOwFP5aCNksPmP37HhHLZdZiof-91W-YJII7gUsLQQidZEB43ODUHyy1FDCf1fXa4VwrDPaA2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
ما سر خم نخواهیم کرد و از حقی که ذاتاً متعلق به ماست، دست نخواهیم کشید.
صریح می‌گوییم: نه سلاح هسته‌ای و نه هیچ‌گونه محدودیتی برای فناوری صلح‌آمیز هسته‌ای.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72131" target="_blank">📅 17:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72130">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2213909800.mp4?token=KhvbgCPerbDRLKNYe5pMUXiVKqE5MqchfHqNHhkhq0j6GUG-3yRiRbW3ZTuMGP6CXq9GpxRXYj-ktIriza1ujE9aBJarTAGHIFDE-CxaE7But24MrTEtg0-zYh90szpw_y4EB2ytk9CfqcfCLJjbGzcgrIDxYQ-UKX4bZxwRRL9wT_sDGsUQrVb4QsSJqqqpDr3TJi5v3fsSPiWnAw2QkG2GeQyxJiuzdH2ITDNJ-l8vRNV_0MhbCLtXgB_Qq0-6aHc6mbU1jqgfOtIJMCvCEMne5DDZbNhh3CS9Yo4K9S8DdpKWeNtDUr6nk3JAQ_2bdq45TFBMqRD-jpx50L-nv7I9SJl49uX8UqY1rV4iLYFKs6WpWfNT7vN7n7SVmgXzXYwnZx3pXJ7jqPR-uvROS7EpVwZkYng7Gmn4KG0lQQgZ3pslBdFstjjhG84fxQdcoo2Uxjb74e-rhOXvJNFqLQSvH_Y4jjolicm6lSN4PEXL4Vc91uUOT0VTXafwmJD7ZFFEytOkbr-HdsCwwG55mmtk95X_HaNUAYrVJEZKdNljKrVFM0mC4vEbKzyJU1OJrUjBmMR2gIPlDSkjqucf3hnFFWcxJp-HuxT1uFviIKJq2IP4XsgJbkcmFCltu6YAD06itOL9naU7mrSiUqMWK_SP6qZyuzVnLHJwPGLjqHM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2213909800.mp4?token=KhvbgCPerbDRLKNYe5pMUXiVKqE5MqchfHqNHhkhq0j6GUG-3yRiRbW3ZTuMGP6CXq9GpxRXYj-ktIriza1ujE9aBJarTAGHIFDE-CxaE7But24MrTEtg0-zYh90szpw_y4EB2ytk9CfqcfCLJjbGzcgrIDxYQ-UKX4bZxwRRL9wT_sDGsUQrVb4QsSJqqqpDr3TJi5v3fsSPiWnAw2QkG2GeQyxJiuzdH2ITDNJ-l8vRNV_0MhbCLtXgB_Qq0-6aHc6mbU1jqgfOtIJMCvCEMne5DDZbNhh3CS9Yo4K9S8DdpKWeNtDUr6nk3JAQ_2bdq45TFBMqRD-jpx50L-nv7I9SJl49uX8UqY1rV4iLYFKs6WpWfNT7vN7n7SVmgXzXYwnZx3pXJ7jqPR-uvROS7EpVwZkYng7Gmn4KG0lQQgZ3pslBdFstjjhG84fxQdcoo2Uxjb74e-rhOXvJNFqLQSvH_Y4jjolicm6lSN4PEXL4Vc91uUOT0VTXafwmJD7ZFFEytOkbr-HdsCwwG55mmtk95X_HaNUAYrVJEZKdNljKrVFM0mC4vEbKzyJU1OJrUjBmMR2gIPlDSkjqucf3hnFFWcxJp-HuxT1uFviIKJq2IP4XsgJbkcmFCltu6YAD06itOL9naU7mrSiUqMWK_SP6qZyuzVnLHJwPGLjqHM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ایران در دو قرن گذشته به هیچ کشور یا سرزمینی حمله نکرده، اما همواره با صلابت از خود دفاع کرده است.
با این حال، اکنون ما به ایجاد بی‌ثباتی در منطقه متهم می‌شویم و برچسب تروریست به ما می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72130" target="_blank">📅 17:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72129">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مسعود پزشکیان:
کسانی که خود تروریست هستند و تروریست‌ها را آموزش داده و از آن‌ها حمایت می‌کنند، ما را تروریست می‌خوانند. ما تنها از خود دفاع کرده‌ایم؛ ما تروریست نیستیم.
مردم بی‌گناه ما هدف حملات بزدلانه‌ای قرار گرفتند که بر کشورمان تحمیل شد. ما با نهایت قدرت از خود دفاع کردیم.
آمریکا و اسرائیل با پیشرفته‌ترین فناوری‌ها به ما حمله کردند. آن‌ها به ما ضربه زدند، اما ما سر تسلیم فرود نیاوردیم
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72129" target="_blank">📅 17:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72128">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baa7d4e9f3.mp4?token=TgAwotAe1tPXQacuce2CseGydqACwJk8KoIKPaLCtNSK4ZLyTNAEcbP2l8bk2L8EfXxq1eNkwEz6hYL4zEzP3wuwmbi1VCpsWq1HlEqmhYd0uFlTnRVXd7UYkSCeZU0bHPllDEm6_0T4SMYl7QIQGZ_vsKbNxH1MFvvtzi8eOm6gce7oHSkT-LrY8jR7Oq0xojI-WBU83HNEiJg3NNWGBvpr3xzuYPe2mpI3qrx_zz9n5qWYeR0I5c34SOKk2CgrQYBYKKQzixv0Fm5SLdPqTKmBTzK04019H2kMy5nnRwUMDwzbjaKi52mA8BP1Mhb_eIjHHFL-x0VDE3Ajmgbu-ZQIfPAP4Q2JCs9qfeX4bkMWGLZBH2pyjNP4QEC_ORGLxm7hUG6bZ034lQby-mgZcSCOB573ofPxLdo_eSLlpRY5QnBCwEHn_i_AGjb04m2H1te6_FdB7awxX-JDsaFApKSNS2bMPom9hh8my5Ha3rGn-yTnuJCSqBcn2JOhC89OvcL-U4wgnp1JWG5mfdEKiql4Wbm8-T7iP_wS_RAcl4H6fbVJ6N8PzJlb1xm5p2WzuaG2NO3SAC517oQgxAMcS1VL44V5n_SypHRi7OwZoEQ2-E2_gNgVQjPpAkC3JT9VeRaDvbc0_BOMJZ6ApIZsIWIINwunb3aKM7f-N9T1XcI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baa7d4e9f3.mp4?token=TgAwotAe1tPXQacuce2CseGydqACwJk8KoIKPaLCtNSK4ZLyTNAEcbP2l8bk2L8EfXxq1eNkwEz6hYL4zEzP3wuwmbi1VCpsWq1HlEqmhYd0uFlTnRVXd7UYkSCeZU0bHPllDEm6_0T4SMYl7QIQGZ_vsKbNxH1MFvvtzi8eOm6gce7oHSkT-LrY8jR7Oq0xojI-WBU83HNEiJg3NNWGBvpr3xzuYPe2mpI3qrx_zz9n5qWYeR0I5c34SOKk2CgrQYBYKKQzixv0Fm5SLdPqTKmBTzK04019H2kMy5nnRwUMDwzbjaKi52mA8BP1Mhb_eIjHHFL-x0VDE3Ajmgbu-ZQIfPAP4Q2JCs9qfeX4bkMWGLZBH2pyjNP4QEC_ORGLxm7hUG6bZ034lQby-mgZcSCOB573ofPxLdo_eSLlpRY5QnBCwEHn_i_AGjb04m2H1te6_FdB7awxX-JDsaFApKSNS2bMPom9hh8my5Ha3rGn-yTnuJCSqBcn2JOhC89OvcL-U4wgnp1JWG5mfdEKiql4Wbm8-T7iP_wS_RAcl4H6fbVJ6N8PzJlb1xm5p2WzuaG2NO3SAC517oQgxAMcS1VL44V5n_SypHRi7OwZoEQ2-E2_gNgVQjPpAkC3JT9VeRaDvbc0_BOMJZ6ApIZsIWIINwunb3aKM7f-N9T1XcI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
مردم بی‌گناه ما هدف حملات بزدلانه‌ای قرار گرفتند که بر کشورمان تحمیل شد. ما با تمام توان از خود دفاع کردیم.
آمریکا و اسرائیل با پیشرفته‌ترین فناوری‌ها به ما حمله کردند. آن‌ها به ما ضربه زدند، اما ما سر تسلیم فرود نیاوردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72128" target="_blank">📅 17:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72127">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مسعود پزشکیان:
دیروز ترامپ ما را تروریست خواند؛ در حالی که ما خود قربانی تروریسم بوده‌ایم.
من از ایرانی می‌آیم که در آن، رهبر عالی‌قدر ما بدون هیچ‌گونه مبنای قانونی یا دلیلی ترور شد.
من از ایرانی می‌آیم که در آن، مدرسه‌ای بمباران شد. این کودکان را می‌بینید؟ این کودکان بر اثر بمباران با تسلیحاتی که توسط آمریکا و اسرائیل به کار گرفته شده بود، جان باختند.
آن‌ها بی‌گناه بودند و هیچ جرمی مرتکب نشده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72127" target="_blank">📅 17:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72126">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aca1a8c79.mp4?token=Gy1dQFMk9uu6PET0__KWepfiL_77EHkh3MdXuYiR90DQaSNlRwiN2T6DRjmBLas9DyVBom1eqnvHtTA-dP-PHIV4Xc_CSX7HbZ6fBcxbdRYWIakVNzr-u5U_-r9pzKM48QbFd1MUyP9KyJzk84GcA10cbPClgxyogKmKy04Tg-cRsm216PWYIkEF0i0EtypXKMrIGPdpV0rTl8RhMg_MutS1AbUZx0bQJfl8yegdUHqT_JwluNed6rm85wMnfjqwGlUQfbPG-OwPKSuoE5zM07Rje-8VNydTu-8J300pZmqWtshT4dJ1cuNB_9w8kkb8Er_Qzj3kVcUPGCSo9ZWYC4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aca1a8c79.mp4?token=Gy1dQFMk9uu6PET0__KWepfiL_77EHkh3MdXuYiR90DQaSNlRwiN2T6DRjmBLas9DyVBom1eqnvHtTA-dP-PHIV4Xc_CSX7HbZ6fBcxbdRYWIakVNzr-u5U_-r9pzKM48QbFd1MUyP9KyJzk84GcA10cbPClgxyogKmKy04Tg-cRsm216PWYIkEF0i0EtypXKMrIGPdpV0rTl8RhMg_MutS1AbUZx0bQJfl8yegdUHqT_JwluNed6rm85wMnfjqwGlUQfbPG-OwPKSuoE5zM07Rje-8VNydTu-8J300pZmqWtshT4dJ1cuNB_9w8kkb8Er_Qzj3kVcUPGCSo9ZWYC4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت نمایندگی ایالات متحده هم‌زمان با سخنرانی رئیس‌جمهور ایران، پزشکیان، صحن مجمع عمومی سازمان ملل را ترک می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72126" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72125">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72125" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72125" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72124">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OipqtBvleSy6pQKeq2vAxWyUdyL3ZwZ7CpSAQBBQCU8E-xjgSwWnKEJOReF2h4lZZ4kaM_eNe-hsE4p08XrQsTbvWIiiPmGS5QveIR4X0Ry9Ipmy7zF01nmOxb8zUK5ZTHkDWF9Qh0JkkNMG-eOvA0B9L2gtkZW4JKCGOgvhgXFpo68nmcVqiPBkFvjCwhN8Tay6WZEtLfNR4Sug5nr5cDqYS4or2R7Hc-QpKBtZjhXlwdfgSa76foOIB32kf8_ch4JjyCa6UVmBGWjiESZBPkA364sxpEo71PSm-ZSZIeecdJkeOnevH2HO_44zsweXtwOzFsav8aWouQaMInMnTA.jpg" alt="photo" loading="lazy"/></div>
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
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72124" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72123">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4142dc5d8.mp4?token=eIA4qIChZQBa3nkrLowI7ck6TKHoZq9lfzpAPqsuoPXpBxhLWAJHO4Ny6GeNA5_H3G0n6ZFzPqiJR2y2tboJV7M4GXDGeE7SlaBpay5sfF03s5JweV7bhxwyc3hG-9g86VgSC5MG_Jq-PDyDhSLSj1RAosuFtd4xwKx4jBu2uiGOmWXJUrsCSF1rrBEoH2SL-D5VJR0fhPomLjhVGniZITvfSi-qLLdgFEHlrUFxveXPFpsW3YgJeJSozhP6ELl8uTPSliA8aMHxEYeQKiEAiD7dFaLL2JhIVl1rR00gQmJNWuO_BfqRVhwaraFukvbVwkxoy1cZfRkBRMt14Umi5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4142dc5d8.mp4?token=eIA4qIChZQBa3nkrLowI7ck6TKHoZq9lfzpAPqsuoPXpBxhLWAJHO4Ny6GeNA5_H3G0n6ZFzPqiJR2y2tboJV7M4GXDGeE7SlaBpay5sfF03s5JweV7bhxwyc3hG-9g86VgSC5MG_Jq-PDyDhSLSj1RAosuFtd4xwKx4jBu2uiGOmWXJUrsCSF1rrBEoH2SL-D5VJR0fhPomLjhVGniZITvfSi-qLLdgFEHlrUFxveXPFpsW3YgJeJSozhP6ELl8uTPSliA8aMHxEYeQKiEAiD7dFaLL2JhIVl1rR00gQmJNWuO_BfqRVhwaraFukvbVwkxoy1cZfRkBRMt14Umi5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیمت کوکائین در تهران چند؟
پلیس مواد مخدر تهران بزرگ ، یک بار بزرگ کوکایین کلمبیایی را قبل از پخش در پایتخت ، کشف کرد .
این کوکایین ها بیش از ۵۵۰ میلیارد تومان ارزش گذاری شده است.
گویا داداشی ها سهم  مامورا رو ندادن اونا هم بار رو لو دادن
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72123" target="_blank">📅 17:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72122">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dadfb7a92.mp4?token=YTw8krkiyvqHhKbHpsrrkTBLQgNpGVhv6sUOXjkE6NMNd30cn-Aw02gwyIchJbrsI9j6K6P-tZ506462zmoaaoxv0PXrdfIuGuqlsM6KcCaBI-8B_bwyFaLxVJy1RYaLnf5Wp35WVNU9E7ly5uOwc3tp6LJWUBZtihWKLdJSP7JkIII32EXssHNDzj593dQboiAW6kdxGefr_38y8JzdrWoAcbysOyw550SOvDRw7OMg6eiGEoMF6mXHBwpN4XCTJ9AEAVPt8lcyD-vtWZFWOhM-reQNgDof1MWxxo4LwMzoMun17b55zTIPfMSAqIxfeof6UZHE-h1mDgFXo6brHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dadfb7a92.mp4?token=YTw8krkiyvqHhKbHpsrrkTBLQgNpGVhv6sUOXjkE6NMNd30cn-Aw02gwyIchJbrsI9j6K6P-tZ506462zmoaaoxv0PXrdfIuGuqlsM6KcCaBI-8B_bwyFaLxVJy1RYaLnf5Wp35WVNU9E7ly5uOwc3tp6LJWUBZtihWKLdJSP7JkIII32EXssHNDzj593dQboiAW6kdxGefr_38y8JzdrWoAcbysOyw550SOvDRw7OMg6eiGEoMF6mXHBwpN4XCTJ9AEAVPt8lcyD-vtWZFWOhM-reQNgDof1MWxxo4LwMzoMun17b55zTIPfMSAqIxfeof6UZHE-h1mDgFXo6brHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مادر توی کمد لباسای دخترش، کاستوم مخصوص سکس پیدا کرده، بعد دختره هم به این شکل مامانشو قانع کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72122" target="_blank">📅 17:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72121">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/st4r7ODbPaHNAN9l5ncZOMi_-Olx2gbg-lDdFkR8sjyBkx2WQiaj0D72gmfj-v-dMy3TFNDdz123YvnbmpHQ1PYwtAhuoJGCIpftf7F9DLeZ3g2Ye_D7uVblduIkxxeB_LhrBKKhDsGacL3uu-337kEmCXjdrhhquJsO73-lbZU_7o22TUaCqdtsM1Qv1fEFzB3Wi6O60MF4__wcu-7BUz5mbEreH1bpJiaUtl9zi-PMcfMdbZ8zQCvlEcwLphenyEfoDycIPqFHbHYN47NBOQm-D99_7LIHfO0MeinWRcC34SaWaJ9WxjFF-JUunbfUqCn7EpN_RWV7DKsVMg5SIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد که یک کشتی باری در تنگه هرمز هدف اصابت پرتابه‌ای ناشناس قرار گرفته است.
این کشتی دچار آتش‌سوزی شده و بر روی آب سرگردان است. خدمه کشتی تخلیه شده‌اند و گزارش‌هایی از دو مورد تلفات منتشر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72121" target="_blank">📅 16:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72119">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/056cf75693.mp4?token=uuZLwkRlCtrePGoKortD5fV4Fu1kHy5XrF1uKsC0IZlB-Yp7hG6S8GtCbEt8NTQfiFpObDekQDg5AIUsp8PTSYExuABt_dfMnoo-a6YaKksR3wA9RHk7dTIO9IDgb3YY9KVgp_PWjehGJIsWHeqOWUYp0lHfM2m5nAHuvzEYqv7Arj8G6q0zM2PWBvZTz_YqsrdNUou-mGftQ_Uxgtys6LP4Oft3qF54KyD3vGbMKoCnuAnxRyC9KM45lo58Nm_zgdCume7rrJXaK7SCc_qr8XrTj7sl4Y345lFAZMaVXOykrb76ubDaqAHUL5GJq9exISJiNt2r_20Ad2suiRYXKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/056cf75693.mp4?token=uuZLwkRlCtrePGoKortD5fV4Fu1kHy5XrF1uKsC0IZlB-Yp7hG6S8GtCbEt8NTQfiFpObDekQDg5AIUsp8PTSYExuABt_dfMnoo-a6YaKksR3wA9RHk7dTIO9IDgb3YY9KVgp_PWjehGJIsWHeqOWUYp0lHfM2m5nAHuvzEYqv7Arj8G6q0zM2PWBvZTz_YqsrdNUou-mGftQ_Uxgtys6LP4Oft3qF54KyD3vGbMKoCnuAnxRyC9KM45lo58Nm_zgdCume7rrJXaK7SCc_qr8XrTj7sl4Y345lFAZMaVXOykrb76ubDaqAHUL5GJq9exISJiNt2r_20Ad2suiRYXKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانیال عیوضی، مجروح کشتار کرج، پس از ماه‌ها تحمل درد و جراحات، در دی‌ماه ۱۴۰۴ ترکیه را به مقصد اروپا ترک کرد و امروز خود را به سازمان ملل رساند تا درباره مشاهداتش از کشتار و برخورد مأموران امنیتی جمهوری اسلامی شهادت دهد.
هیئت ایرانی تلاش کرد سخنان او را مغرضانه و تند جلوه دهد و مانع ادامه صحبت‌هایش شود؛ اما با دستور رئیس جلسه، عیوضی به سخنان خود ادامه داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72119" target="_blank">📅 15:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72118">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b96e8038a0.mp4?token=j3vulONJXGAS7_siccDV50s8ZOujlZAanzGBUvgAmdIjwirXuSR3FEBsIGkIRgnXnMIyjUmoiFK-bdrbcZs_TcASYGZL3gALu4-CsoGk61_kT-8NwsJhvMObZA3NurOfl05eS-TYVQW7OxBZ13kPZrvWTAx8ISc83w6ry7ZAsyP1jUQqZtDNWIq0380iLF-jYYuiRT3agQWdiQE7BeIPT0kMhAGHhTP0fH2HLFa9UKNzZapw7ARyhEb0zOXxxjdDnw2ZPBXlgcn4qx0uye30QGI4HVCQgF8OyxEnjdiCt6I01sq1Rnlbel6CSTIXMcxtkMn9z_y4blr5bagMPXmO2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b96e8038a0.mp4?token=j3vulONJXGAS7_siccDV50s8ZOujlZAanzGBUvgAmdIjwirXuSR3FEBsIGkIRgnXnMIyjUmoiFK-bdrbcZs_TcASYGZL3gALu4-CsoGk61_kT-8NwsJhvMObZA3NurOfl05eS-TYVQW7OxBZ13kPZrvWTAx8ISc83w6ry7ZAsyP1jUQqZtDNWIq0380iLF-jYYuiRT3agQWdiQE7BeIPT0kMhAGHhTP0fH2HLFa9UKNzZapw7ARyhEb0zOXxxjdDnw2ZPBXlgcn4qx0uye30QGI4HVCQgF8OyxEnjdiCt6I01sq1Rnlbel6CSTIXMcxtkMn9z_y4blr5bagMPXmO2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقرار پدافند هوایی روسیه وسط بزرگراه رو دریابید
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72118" target="_blank">📅 15:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72115">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fnWBrduQJJclkU9cEz3SC-9YvmgF8F1sX3u4Tfy1R8qCI7kBKC7r12zIrX9BM9wYiNx5xuEmoOhe2x742LvmIfRTYR1ADy-JJsTAWdXbLcjeOXHdgbpvorzreBLmbLAeY75_okVnx8nw4xgsM2zsP-B8YFGdos33orMWrlDZHu6_7pIXTLhKkhxr9sHTGS0_RBoUqtqs8clKpDHnObYFyoYlnShgvwCIJtGTs7MDC2QUOQZITdnfsDKuF96Zoh-zGbtUsiKs74LuYBV1VSkV2JjYJ9yTWXcomOQ81zKmx9T0xgR2IhDaGiUQp2jg-WL4PmGmuEtSF-pM_PEMGcLiag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K_dBunJx8Qc4_r_mA8P6wOdcshwMAZq28_CAYDbpFmzz0GVmrNfTI6iSj_36AjpOzwvNZ4u6YbqCTrvw1HOXvh3tug0olp9miR3YxNvTQW8-rg_cWg5jIyPMDEUar78Opq4PfZRZirueUpd_z1p6E1d9IaRJ09iZNDe1EyMnmQdedhgkwRjU9xpKx2DDiXYzQgPISFLN8Cq2ZSXhhHRwdXUkYJ888U5Q9j_k5Kg2CXSAoB2dQAwkTaDB34vTQKwsZOfbL3uXRr3jSzNTWoGF4U3ks3BE6HsuGVBTeR7lepHmtRNDp0AmQNXNa2lDXo9vSak91Ju28rYO-JbzdrJyvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MO7ORYD3IoPloBAiy1wyFkxzHKSJomcmna1wQcH0snmMlopC_7-NxjXafJzwFr5EffWOOx50zn3AMtMvs3RqNvXv3_oCiJViV1XPqPL57dxkIxqAttxGSd4DkTpge1-3SGgW6HUOrFsigtYHS4pjxeStO4QPhkF3YVf5sBqWBzdqLlVaNruymAnzJh4x7bIXmNvEXIrXyhcy_HjieZL6zBXSbKknhjKCqchkBIES8AR4VlEYR7rKfTHl4g_FrW85xCE7V5BR8cTyDtuEkBEiYL0NENjruHCER_bo2Iwn8EC7IOx66RUwCLJfEkcxdFfMQM3AuRErMC4mjmh9NCRRVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این بیلی آیلیش هم روز به روز داره خوشگل تر و جذاب تر میشه هرشاتی از خودش منتشر می‌کنه کلی لایک میگیره :)
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72115" target="_blank">📅 15:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72114">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تحریم‌های جدید آمریکا علیه بخش هوانوردی ایران، چندین کشور را بر آن داشته است تا پروازهای ایران را محدود کنند.
محدودیت‌های تأیید/گزارش‌شده:
🇬🇪
گرجستان — ممنوعیت کلیه پروازهای ایران از ۲۱ سپتامبر.
🇦🇿
آذربایجان — ممنوعیت فعالیت شرکت‌های هواپیمایی ایرانی از ۲۲ سپتامبر.
🇮🇶
عراق — تعلیق پروازهای ایران به بغداد؛ احتمال تغییر مسیر برخی پروازها به نجف.
🇴🇲
عمان — توقف پروازهای ایران به مسقط.
🇶🇦
قطر — گزارش‌هایی مبنی بر تعلیق پروازها از مبدأ ایران.
🇹🇷
ترکیه — اعمال محدودیت‌های عمده.
برخی مسیرها همچنان فعال هستند:
🇨🇳
چین
🇦🇲
ارمنستان
🇦🇪
دبی/امارات
🇮🇶
نجف
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72114" target="_blank">📅 14:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72113">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeZxz0uPI9fBW3Sk55mAOG1jSDif_exUJTNmS2Vb12wn32nKY7Y_FrV0gOREbsbof7LB90AV3Pv77laPL1fTk2DG_h5Mn-VBuhJBDohZTuVafpF5M_0xUYrkqIaN47DrVADMJKUlCi6Xg09wcKAWhPDdYCTzJiBPRRjZFy0Frij8vrCacuFoERpICWMMBmjg9HMTG6wJey_UKux-NIdAr7Oe3Ov1Il9KJUp3Lq7OOjnuqFd8h5JyYoIcFNCjLmgiYMOIPsU4t8L-kuONapbsRZAJj1x_jqZkJh3Oe26yj5HZaqPQIXBb40KqqbKGymrphtXCsfZ9AxfEUk9B8ORmaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بازنشر کرد:«ائتلاف نتانیاهو در تازه‌ترین نظرسنجی انتخابات اسرائیل پیشتاز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72113" target="_blank">📅 13:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72112">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o41WVkUrMV0NYIMzN32HkhOnNAPKstV9wBnSpi1-ipBewjDhqDRIKtedVd8Q4VlU2kkP_AqutXRISG1g8REEidzgtpmYRdHtcAvpW2N8AKNUNsnNBxh_huNiXqAcdEvNAtmBRleShMwsCshA0XpPwNqZ6mukJF2-Z2ojuiu6dOjyTdpOTsievntGWRG46GobvZVIdxEhUStLsZ-cHBhEGE2UBoILTkT2HMhI4O4uh87YWHDOKwEYZcF2IkUm_lCZyQbWqCCG1K36Igmcp1doRab1OmQSf8fBgnEQTAuEoxiB9L3zER49SgBBasSA0IxCnQihkzseMGz5ONJsQWtGzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حال‌ و هوای یکی از دانش‌آموزان در جشن شروع سال تحصیلی جدید:
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72112" target="_blank">📅 13:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72111">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb3684649a.mp4?token=QyKD2pJPurIRIcESYyrGlCXPdWUCEZgKdASSgbzLhnVgLJOu0SO-lbeNawZqXdwx-sF7EkvEUajQ-6sV7hLhqNt1RibLb8Xpre3yxqq6Gj4mzyb2A8Jq-kV0YeISCJpVjtFI0Rdg5A54dDE4jUS9Qyw8gYjFRiUiS5bS9ucB6gWjSkn-wXa-5frnwApPdJo7ppCwNwkDsw_ECcl8USQP304gyFZPHXBVC0JpLH64_TdEX_xyRg7pN-dyk3II5Xp_nfbjLF75kekuVBWuIbxmxUm-dXk1vJg6ERgqJ_6C-GuXnBbCsaw_7xKFnc4dztDlETbJy5J_zZeFjfwuBduq3nH53hvhwvHITvxXKIQyVWLO6bsPK94CLN8tk3yAUZU_oPZovYuzv2JUtzzEuK1OkpHKGQVTmXDYpv2FdxwvPypmDGrxC3AefStq1SBvl9cDOzggJdRfzesVpM29h0IuF7FiUzp-kve8f3_Rt2kgBCHNQffDWuL_3s-8SNdGD2pvHQ1U8BzS3hxOrwbtcSs6RdysoAlRl-iOE5VZa9S-efPviGby4iTRF71jZVxCFHr75tRahmOB4Tiktxo12laioc3Q-70BUBLKxOtk_imoPrPByX6c2YWERSKgZSmrDir7YBIzKTNJUQyrl_zCz_6JBGY4mq_u7SIyIW3s7ol-eZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb3684649a.mp4?token=QyKD2pJPurIRIcESYyrGlCXPdWUCEZgKdASSgbzLhnVgLJOu0SO-lbeNawZqXdwx-sF7EkvEUajQ-6sV7hLhqNt1RibLb8Xpre3yxqq6Gj4mzyb2A8Jq-kV0YeISCJpVjtFI0Rdg5A54dDE4jUS9Qyw8gYjFRiUiS5bS9ucB6gWjSkn-wXa-5frnwApPdJo7ppCwNwkDsw_ECcl8USQP304gyFZPHXBVC0JpLH64_TdEX_xyRg7pN-dyk3II5Xp_nfbjLF75kekuVBWuIbxmxUm-dXk1vJg6ERgqJ_6C-GuXnBbCsaw_7xKFnc4dztDlETbJy5J_zZeFjfwuBduq3nH53hvhwvHITvxXKIQyVWLO6bsPK94CLN8tk3yAUZU_oPZovYuzv2JUtzzEuK1OkpHKGQVTmXDYpv2FdxwvPypmDGrxC3AefStq1SBvl9cDOzggJdRfzesVpM29h0IuF7FiUzp-kve8f3_Rt2kgBCHNQffDWuL_3s-8SNdGD2pvHQ1U8BzS3hxOrwbtcSs6RdysoAlRl-iOE5VZa9S-efPviGby4iTRF71jZVxCFHr75tRahmOB4Tiktxo12laioc3Q-70BUBLKxOtk_imoPrPByX6c2YWERSKgZSmrDir7YBIzKTNJUQyrl_zCz_6JBGY4mq_u7SIyIW3s7ol-eZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دنی دانون، سفیر اسرائیل در سازمان ملل:
ما می‌دانیم رهبران ایران کجا پنهان شده‌اند. ما می‌دانیم آن‌ها چه کار می‌کنند و چه می‌گویند.
به گمانم جانشان برایشان اهمیت دارد. آن‌ها دریافته‌اند که اگر به اسرائیل حمله کنند، تنها چند روز طول می‌کشد تا سراغشان برویم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72111" target="_blank">📅 12:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72110">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/402f33620e.mp4?token=GE_-GAK7ikIbuW7QfYlTlqJ8mHdE3WDemaFl4ig38aEtaiE7aKFTgIb1YJJw_MjWMP-OcydSMgSkmR5BBZIqxEfxKql7HOx32Lb-pSw7PJNFuy52u9RBJa60vE84-rQ84a8_t9IJBKInVefSkAxDypWB30ZBLoe9hqucMO9zbUMpWSWkjxM4uabrCNLNkzbNgRi2xvaCQqT3gRfVzczzpq3n57t0TZlPMO4j-5sN9T9Ia3XbSWkb4a-mD5fe2CYmHEcvVnIK_sAXjIxSIP7YgW5zSFd3ZxQ2YzPEuzoZbDR0mV_l5oM-PzTNZP9zRuH4gvRICFrEJ4i3pDvChwURJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/402f33620e.mp4?token=GE_-GAK7ikIbuW7QfYlTlqJ8mHdE3WDemaFl4ig38aEtaiE7aKFTgIb1YJJw_MjWMP-OcydSMgSkmR5BBZIqxEfxKql7HOx32Lb-pSw7PJNFuy52u9RBJa60vE84-rQ84a8_t9IJBKInVefSkAxDypWB30ZBLoe9hqucMO9zbUMpWSWkjxM4uabrCNLNkzbNgRi2xvaCQqT3gRfVzczzpq3n57t0TZlPMO4j-5sN9T9Ia3XbSWkb4a-mD5fe2CYmHEcvVnIK_sAXjIxSIP7YgW5zSFd3ZxQ2YzPEuzoZbDR0mV_l5oM-PzTNZP9zRuH4gvRICFrEJ4i3pDvChwURJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز یکم مهر ماه، بچه‌های میناب دیگه نیستن که برن مدرسه...
اما جاشون پیش خواهر برادرای بزرگترشون امنه
🤍
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72110" target="_blank">📅 11:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72109">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b92a5ff67f.mp4?token=aTLM6SQ3RATydUbPCylyygR0VsCrFUcm8HL7Gy__16N2lVPvQjizaRVODJ2MMuy-OT3zM18YAoHrSdzhGBGCwMNb1bKRCDzJiVjg16Sf8Jpp558hgm84Gdqd58qRa3iJASYZSoDIhS2yV28ABeYYZLe1veDeUeHjAnn3IANQ09iwocnsvbRjzMsXm5SRix6w_QFj1fWBV7m7z9zULg_jGKB1-KOH951D2pro4LFuOhWXsoC58EffzK0hO2R2TTQpOzn7XChJr1CexNIEOL_rSPb8cl-_U0hmtof-scLWWGJ_-dMfoAPNp80kxK76E3TMVhUrFEu02gX7cW1_NZtBTROf9cfdRGiKPG8edskkXU0BkCaM30NK8S6RZuLlaC5Yp9xax_jPad9zTmSiGPS1-a_-FlRWSNasPChWrnVZoxn0STQ-YklQqRF1bhO9HcYkbVIxJ0bKIvJ1o6cIFkNEZlRWEaeM3geyL_tzI1ta75WTcI54twQDvMKHFf6UyMODoTaMeLjPJNaTj-4OiwUNGXLVnEnO6lKAXuJ9BYz97Be_zENkf2idXZiwrCnr7pukByjTZvgS2dGyTdZj9aW_c_vJa1z1Xvo00up7K4MW8esUy4ZL7_f7zoOJb4hZLDBJn1JLYTTBXG4sVvGAjtuSKmYgyvpgBdehpY0hNA1m_1s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b92a5ff67f.mp4?token=aTLM6SQ3RATydUbPCylyygR0VsCrFUcm8HL7Gy__16N2lVPvQjizaRVODJ2MMuy-OT3zM18YAoHrSdzhGBGCwMNb1bKRCDzJiVjg16Sf8Jpp558hgm84Gdqd58qRa3iJASYZSoDIhS2yV28ABeYYZLe1veDeUeHjAnn3IANQ09iwocnsvbRjzMsXm5SRix6w_QFj1fWBV7m7z9zULg_jGKB1-KOH951D2pro4LFuOhWXsoC58EffzK0hO2R2TTQpOzn7XChJr1CexNIEOL_rSPb8cl-_U0hmtof-scLWWGJ_-dMfoAPNp80kxK76E3TMVhUrFEu02gX7cW1_NZtBTROf9cfdRGiKPG8edskkXU0BkCaM30NK8S6RZuLlaC5Yp9xax_jPad9zTmSiGPS1-a_-FlRWSNasPChWrnVZoxn0STQ-YklQqRF1bhO9HcYkbVIxJ0bKIvJ1o6cIFkNEZlRWEaeM3geyL_tzI1ta75WTcI54twQDvMKHFf6UyMODoTaMeLjPJNaTj-4OiwUNGXLVnEnO6lKAXuJ9BYz97Be_zENkf2idXZiwrCnr7pukByjTZvgS2dGyTdZj9aW_c_vJa1z1Xvo00up7K4MW8esUy4ZL7_f7zoOJb4hZLDBJn1JLYTTBXG4sVvGAjtuSKmYgyvpgBdehpY0hNA1m_1s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات روته دبیر کل ناتو درباره ایران:
چرا برای از بین بردن توانمندی هسته‌ای ایران، حضور ایالات متحده ضروری بود؟ چرا اکنون در ماجرای حوثی‌ها در دریای سرخ، همه نگاه‌ها به ایالات متحده دوخته شده است؟
زیرا اروپایی‌ها به نوعی از توانمندی کافی برای انجام این کار به تنهایی برخوردار نبودند. آنجا حیاط خلوت اروپا محسوب می‌شود، نه حیاط خلوت ایالات متحده.
در آینده، دستاوردِ داشتنِ یک ناتوی قوی‌تر این خواهد بود که اروپایی‌ها می‌توانند خودشان به امور حیاط خلوتشان رسیدگی کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72109" target="_blank">📅 11:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72108">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اظهارات روته دبیر‌کل ناتو درباره ایران:
می‌توان گفت که اجرای عملیات «Epic Fury» بدون بهره‌گیری از اروپا به عنوان سکویی برای اعمال قدرت ایالات متحده، غیرممکن می‌بود.
از ۲۸ فوریه سال جاری تاکنون، ۵۰۰۰ فروند هواپیما در پشتیبانی از عملیات «Epic Fury» از پایگاه‌های اروپایی به پرواز درآمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72108" target="_blank">📅 11:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72107">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72107" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72107" target="_blank">📅 11:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72106">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e20ctXbssOnUTHcNL1GUq2Kv3B05dhIppQS4XpO8O92HFYNQKmfNKSu1OYDqASGr4lnNKba26zeDm0wSY_SKQ-EJ81Jg0dGvFsKjvl3H5S4l6jOWzvjbq5BZ-W9pM-XJXvLa1DA9GrFr3OpBn-PUmxc0HZttQACHc9ThxcKMCgbLAVApvJFEqT15iGbe4KEGNOytnR2lDsNQ0uDnLeJJuVM3p6Nk7jIH5kco2V6gNPtkiNEP5szwuZc3aXJrEfYB6zwJ2u2R2ZK7qTSQTyS-QEk7j2pKZJbiJGdYZawyTZpJ-qg7rJAj-fQ6V-dsQtUGERw5UW2yL_li-TqTqtPBig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
هیجان مسابقات DOTA 2 را زنده در
TrexBet
دنبال کنید و با پیش‌بینی دقیق نتایج برنده شوید!
🦖
پوشش کامل تمام بازی‌های محبوب Esports:
‏CS2, DOTA 2, Valorant و ده‌ها گیم جذاب دیگر...
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72106" target="_blank">📅 11:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72105">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شلیک چندین موشک ضد کشتی به سمت شناورها در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72105" target="_blank">📅 11:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72104">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4629cd7c2a.mp4?token=K2mxMhq9rbDjQbADt95TJKDoaDlyX7Vd9ExjJVdtoJHtXlgMRrYZzW1zTvjHfehff3WRmHILdnzsFbhgzYEOIfLU-6Zo17VkWSN66iEQd3PtJ1hl2YcFzZbbBCOiIu1PskzYaXpUdmHgb-c24sr_vj7GfDpJbrSMopCmEJvaYb0pVuc5yo4uzk6d-XO0Km8AReG5Mhm9Rt2EXB7BYmXrDaDd1f7awNOvY8Kjo7R_M-T4fts5uFpiGPqu2CWZTkgcP8--K88YfAaSCr3FHiimwn0-_rkj8xRbO1EeEkMqOWzQ7z1bRrHiXaspv1G3j_6FdEKeyKSKa_8Is_TSZUUDuUPD_dJqUL_uwnubACSK2FfY0QyN0U2Z5dRM4mz9fm_AkhBmL94GNA_7Vp0xM522RgWpONgbGEjsTFY-RRuOjqlhl0Bu-9IECUxkFYQ36cihP4qpUN6c6ETA3ofeNOn0vUjnZjLYsFATwMZqb_d_3eu-AVEtVKOypsyHajp1HyrKrRXKoGE4FB2jhecbIhKMdSDIwjt95HVqn56LN7RP00-ulYAjRkW_aHKI35wmvaoTXNH_QpajPjMx180MIheWghEHVMJEZ8QJj8cN2ROuOkupM5RHjjmRTx5R1e9Op6enruaUNE8Jl7eZhi37dU0FOd6L5-6rZ6vVE9h7o0vK1TY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4629cd7c2a.mp4?token=K2mxMhq9rbDjQbADt95TJKDoaDlyX7Vd9ExjJVdtoJHtXlgMRrYZzW1zTvjHfehff3WRmHILdnzsFbhgzYEOIfLU-6Zo17VkWSN66iEQd3PtJ1hl2YcFzZbbBCOiIu1PskzYaXpUdmHgb-c24sr_vj7GfDpJbrSMopCmEJvaYb0pVuc5yo4uzk6d-XO0Km8AReG5Mhm9Rt2EXB7BYmXrDaDd1f7awNOvY8Kjo7R_M-T4fts5uFpiGPqu2CWZTkgcP8--K88YfAaSCr3FHiimwn0-_rkj8xRbO1EeEkMqOWzQ7z1bRrHiXaspv1G3j_6FdEKeyKSKa_8Is_TSZUUDuUPD_dJqUL_uwnubACSK2FfY0QyN0U2Z5dRM4mz9fm_AkhBmL94GNA_7Vp0xM522RgWpONgbGEjsTFY-RRuOjqlhl0Bu-9IECUxkFYQ36cihP4qpUN6c6ETA3ofeNOn0vUjnZjLYsFATwMZqb_d_3eu-AVEtVKOypsyHajp1HyrKrRXKoGE4FB2jhecbIhKMdSDIwjt95HVqn56LN7RP00-ulYAjRkW_aHKI35wmvaoTXNH_QpajPjMx180MIheWghEHVMJEZ8QJj8cN2ROuOkupM5RHjjmRTx5R1e9Op6enruaUNE8Jl7eZhi37dU0FOd6L5-6rZ6vVE9h7o0vK1TY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی:
تولید ناخالص داخلی ایران در سال ۱۹۷۸ دو برابر کره جنوبی بود. امروز، تولید ناخالص داخلی کره جنوبی پنج برابر ایران است.
وضعیت اقتصاد ایران قابل تداوم نیست؛ پایدار نیست و در آستانه انفجار قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72104" target="_blank">📅 11:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72103">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/582ee3d494.mp4?token=UgCJXb_L1FaUUgq72POuzNNo3Ns2r7DjLJSM9BqMHUJBXh98k4I5nLLrm5qdzgN5eHxQuF_dY-Q2TJTNVkJWt9IQ6VSpHdgcyknZyuPgIxbc-h2FG-7WBKVXbFjFQRnppxAiZmwB226NvshpBRS2dq8mzJ18nrN2oR_q3jxVOqfwaOhnvI8hd4-9r1yJZNPquVZaW30HNbIOUGgTw2ZklK9uKowjltKhw-7vdavfFnh8TXpczp3hEQuCauMTRC6cb_E2I8ZYrTYZcleEp9CQ4K2ktUrlykcDPXWbLBFqw5vugoLhqlCG_zp2MbKZQtUzlebhLeo6jL2x4UNl9nhjnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/582ee3d494.mp4?token=UgCJXb_L1FaUUgq72POuzNNo3Ns2r7DjLJSM9BqMHUJBXh98k4I5nLLrm5qdzgN5eHxQuF_dY-Q2TJTNVkJWt9IQ6VSpHdgcyknZyuPgIxbc-h2FG-7WBKVXbFjFQRnppxAiZmwB226NvshpBRS2dq8mzJ18nrN2oR_q3jxVOqfwaOhnvI8hd4-9r1yJZNPquVZaW30HNbIOUGgTw2ZklK9uKowjltKhw-7vdavfFnh8TXpczp3hEQuCauMTRC6cb_E2I8ZYrTYZcleEp9CQ4K2ktUrlykcDPXWbLBFqw5vugoLhqlCG_zp2MbKZQtUzlebhLeo6jL2x4UNl9nhjnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناوگان هواپیماهای باری نظامی، از جمله هواپیماهای «آنتونوف ۱۲۴» در حال فعالیت از فرودگاه لایپزیگ/هاله در آلمان مشاهده شده‌اند.
فرودگاه لایپزیگ/هاله یکی از مراکز مهم لجستیکی ناتو است که برای انتقال تجهیزات نظامی و محموله‌های فوق‌سنگین مورد استفاده قرار می‌گیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72103" target="_blank">📅 11:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72102">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6c2bb73b79.mp4?token=J8rtqH1N67Gaeb4Ll49S70FayO3GQuffMzleAx8EQYkUVSq_9FDLhLHO3m5IbdUAyV8-F4TxGrxgmb1Q9UZ3uSZzadoJ4OuBal9KT0K3zhF7h-vLW2Qgga820g9c9uQw1uVomy88oPS7-p-bRpnv_4K0mhiF0dCErL1QXtrGtYWqa6BgLT5W9t6O40g1ic_MsZBBxOxBcX09wQ7aR6g_gcMsSitOFzoBKtMe3v3bNes9I9G1QayNOoEdWDdGHDe8k6cAMsqxvHIS6Q0JxxOX0-h-dcCngJ_Xw6noU__o2x_Jg6tzYQcX9ZTWDfUxwj04gI7rej5Q574ecBlmh7D06Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6c2bb73b79.mp4?token=J8rtqH1N67Gaeb4Ll49S70FayO3GQuffMzleAx8EQYkUVSq_9FDLhLHO3m5IbdUAyV8-F4TxGrxgmb1Q9UZ3uSZzadoJ4OuBal9KT0K3zhF7h-vLW2Qgga820g9c9uQw1uVomy88oPS7-p-bRpnv_4K0mhiF0dCErL1QXtrGtYWqa6BgLT5W9t6O40g1ic_MsZBBxOxBcX09wQ7aR6g_gcMsSitOFzoBKtMe3v3bNes9I9G1QayNOoEdWDdGHDe8k6cAMsqxvHIS6Q0JxxOX0-h-dcCngJ_Xw6noU__o2x_Jg6tzYQcX9ZTWDfUxwj04gI7rej5Q574ecBlmh7D06Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کم‌ کم ربات‌های جای انسان‌ها رو دارن میگیرن....
برای اولین بار تو تاریخ، یه مبارزه رسمی بین انسان و ربات برگزار شد؛ که در آخرش ربات با یه لگد سنگین حریفشو انداخت رو زمین و ناک اوتش کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72102" target="_blank">📅 10:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72101">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2331092d7.mp4?token=orzfoI2JM4kQSzlqEtE3kVo9h3U78o0eCkdCP-4XsfYP7qXiSGurLc54zLG6Oe6ojg_zSdY5-ohtCyege3cIIJlSKMfeDYvec6hkAWBUqx22EluJI0aUwi1ZjEjhL0ft0FhltoyIBOVcFjnqLgzahZA1D89ZqsW7FpKhjClnPXqm8fPuq-PdzCVCV7IF1eJM5HthvW-y6Llb2Btu1Y5kgvgNXGKt4cRZmRLJ9sJPLby8inkCGBdk0NE6Emxdm5TAvCsetg6LKqTHyDLCPjuRAnBG7W3wrzuRLL23hOe6uy65MyW1i1I3a7HpYrpBLbyT_Rh7f8gTDP85jrh5nD1gDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2331092d7.mp4?token=orzfoI2JM4kQSzlqEtE3kVo9h3U78o0eCkdCP-4XsfYP7qXiSGurLc54zLG6Oe6ojg_zSdY5-ohtCyege3cIIJlSKMfeDYvec6hkAWBUqx22EluJI0aUwi1ZjEjhL0ft0FhltoyIBOVcFjnqLgzahZA1D89ZqsW7FpKhjClnPXqm8fPuq-PdzCVCV7IF1eJM5HthvW-y6Llb2Btu1Y5kgvgNXGKt4cRZmRLJ9sJPLby8inkCGBdk0NE6Emxdm5TAvCsetg6LKqTHyDLCPjuRAnBG7W3wrzuRLL23hOe6uy65MyW1i1I3a7HpYrpBLbyT_Rh7f8gTDP85jrh5nD1gDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لمس ممه‌های دوس دخترتون واقعا زندگی شمارو نجات میده! این یه شوخی جنسی نیست، از لحاظ علمی این موضوع کاملا ثابت شده و اینکار مثل معجزه عمل می‌کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72101" target="_blank">📅 09:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72100">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/575ce7dd12.mp4?token=nCtZ4DHEqbdkT0TmsyOIe69s_QX7tBj-PjhaK9zjdT3fajCW3tAFlyKkBmCOoGaSthrHGOQRTmlO90RpbXtZU-5p9pmkz-Lv_l4RCBMwswmVLNtP7JdALM7kL1gxOkY13QhEaPu2XtMATF2WHFmxXIuu0fH2xR49KicWWVn2A-6Vk1uFz1ndSufIBZSZuE_WT_B42HnE88mIqzIabjVvt17k0q4xBUsITJlQrIz3IgPS414zhXCRFxaSH0aIpyjlIZHLXQKNMT4k8rG0rYKfvIQAcslObMD1EAWX-zvH9qEpvfWLV8Whrf9iUOoFJ4055jnWkKU3f37Mu7LSgVzg4w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/575ce7dd12.mp4?token=nCtZ4DHEqbdkT0TmsyOIe69s_QX7tBj-PjhaK9zjdT3fajCW3tAFlyKkBmCOoGaSthrHGOQRTmlO90RpbXtZU-5p9pmkz-Lv_l4RCBMwswmVLNtP7JdALM7kL1gxOkY13QhEaPu2XtMATF2WHFmxXIuu0fH2xR49KicWWVn2A-6Vk1uFz1ndSufIBZSZuE_WT_B42HnE88mIqzIabjVvt17k0q4xBUsITJlQrIz3IgPS414zhXCRFxaSH0aIpyjlIZHLXQKNMT4k8rG0rYKfvIQAcslObMD1EAWX-zvH9qEpvfWLV8Whrf9iUOoFJ4055jnWkKU3f37Mu7LSgVzg4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی مشهد یه خانم حامی حکومت تو اتوبوس، به یه دختر بخاطر حجاب حمله‌ور شد!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72100" target="_blank">📅 09:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72099">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad662c895d.mp4?token=NnPK91ezjX7C7bNdwq_3ydjkkZ3EtdK_vWJq7GXyMdXJfAhXhahQj974uuQULz3LrffI4onPAmhHzCo9WX_nFH8kjagIN1QnEsH5VBDGE3vvxzt9Z2UpJAK2lOUCwhDFzNjMaqGQfV7IBcg97AC_alVJIZ1g67lbm28NM0yUozW0RWCXhQESxJAZSq67x_8ZK-yqMTSBdAlwQbE7GWqCIorEyF5533tzVV17Z1KT7rQFnAzDLs_iY_K6X9QVzXlTIvjqZxf9ellhW2lNZ4RL6rm3qOfCUifdYA7R0uAouI--niy2HYQjRy38mWMoWhTdAGF0GdnhKKnbB82D8487OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad662c895d.mp4?token=NnPK91ezjX7C7bNdwq_3ydjkkZ3EtdK_vWJq7GXyMdXJfAhXhahQj974uuQULz3LrffI4onPAmhHzCo9WX_nFH8kjagIN1QnEsH5VBDGE3vvxzt9Z2UpJAK2lOUCwhDFzNjMaqGQfV7IBcg97AC_alVJIZ1g67lbm28NM0yUozW0RWCXhQESxJAZSq67x_8ZK-yqMTSBdAlwQbE7GWqCIorEyF5533tzVV17Z1KT7rQFnAzDLs_iY_K6X9QVzXlTIvjqZxf9ellhW2lNZ4RL6rm3qOfCUifdYA7R0uAouI--niy2HYQjRy38mWMoWhTdAGF0GdnhKKnbB82D8487OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی در استودیو فاکس‌نیوز با مارتا مک‌کالوم:
«وقتی من میلیون‌ها ایرانی را در ۳۱ استان کشور به آمدن به خیابان‌ها فراخواندم، آن‌ها به صورت میلیونی حاضر شدند و ضمن اعلام حمایت، شعار پایان دادن به این رژیم را سر دادند.
آن‌ها از تمامی اقشار جامعه ایران، اقوام، ادیان و گروه‌های اجتماعی گوناگون بودند؛
این جلوه‌ای عالی از اتحاد و تنوع است.
بنابراین، هر کس که ادعا می‌کند پس از ما ایران دچار جنگ داخلی خواهد شد [باید بداند که] عامل اصلی این تفرقه و اختلاف، همین رژیم است.
همه ایرانیان می‌دانند که این رژیم بذر دشمنی و خصومت را کاشته است.
اما ایرانیان دریافته‌اند که پس از دستیابی به آزادی، قادرند دوباره برخیزند؛ درست همان‌طور که قرن‌ها فارغ از تفاوت‌های قومی یا مذهبی، در صلح و آرامش در کنار یکدیگر زندگی کرده‌اند.
و انقلاب «شیر و خورشید» در راه است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72099" target="_blank">📅 07:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72098">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/686ffe220e.mp4?token=W6h_nUudRVJTmvcoixJg6LOMB8qDEmJW_B46KY5w_Q7v0UkJRyFsXav7KVCIgKHvb8RGMLIt2sg5SDluEOXGRqiztzob_I6ZRKHyzKv96VaPGwpKu1Hu1Z1ehc-bcR6kAG5i6UODcWqfgvwhIJ0h1tkOEztJRYunF6n5QeGdOIvg6-YL5svTpPMYQI2QRmmKxU63TQeBV4O62SUxaiiLa3ELZEhEjUgVRWCenc86pvPR50UE2yvCOs51TGjSrQausA47uVs-kjjtBjPpKmtScgeKuNr78QeCNGtcwS2GKgrIXPSWBZ1vZCHMoLnpcJFzjWN0UkBlSjZCEg8Kr-z40w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/686ffe220e.mp4?token=W6h_nUudRVJTmvcoixJg6LOMB8qDEmJW_B46KY5w_Q7v0UkJRyFsXav7KVCIgKHvb8RGMLIt2sg5SDluEOXGRqiztzob_I6ZRKHyzKv96VaPGwpKu1Hu1Z1ehc-bcR6kAG5i6UODcWqfgvwhIJ0h1tkOEztJRYunF6n5QeGdOIvg6-YL5svTpPMYQI2QRmmKxU63TQeBV4O62SUxaiiLa3ELZEhEjUgVRWCenc86pvPR50UE2yvCOs51TGjSrQausA47uVs-kjjtBjPpKmtScgeKuNr78QeCNGtcwS2GKgrIXPSWBZ1vZCHMoLnpcJFzjWN0UkBlSjZCEg8Kr-z40w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی در اجلاس سالانه «کنکوردیا» (Concordia)، پرسشی را مطرح کرد که دهه‌هاست در سیاست بین‌الملل نادیده گرفته شده است: چرا مردم ایران در کانون گفتگوها قرار ندارند؟
جمهوری اسلامی با مذاکرات بی‌پایان یا سیاست مماشات تغییر نخواهد کرد. ایرانیانی که به دست این رژیم قتل‌عام شدند، خواهان آزادی بودند، نه توافق هسته‌ای یا کنترل تنگه هرمز.
انتخاب روشن است: یا همچنان بر روی رژیمی سرمایه‌گذاری کنیم که عامل بی‌ثباتی و تروریسم است، و یا در کنار مردم ایران بایستیم؛ کسانی که شرکای طبیعی جهان آزاد برای ساختن آینده‌ای سرشار از صلح، امنیت و فرصت‌های اقتصادی بی‌سابقه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72098" target="_blank">📅 07:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72097">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLlxPK7nn4BgZQZIH8EUSj71sQdLwVk4rHd_boEZZzz3Jvp6hp_Krp_zOZmwjN2hOQ3Jl4NOiXONEJwGljUre5olLTmAmBQvWFNrdgW8cnnujOLly7JfUTs30x9B9aFie4Lo7zGpgwrDDSNViNdEYrU2VSZJuVvroNAmfkw2eJRH_bd9uNO8sIF5f99VqP_aRdtWRlGyN0aRJ5rctizUmd2hkdjR16HZVOBAXvDIHKIhQHE0tJBa3K2gVmt0adAviM6xZL1HrtvfUK-WNdF7venqRTOiPyC14FOmzP9Wdb8vYnGX61k-EpzOFH3dnnyssA4BITdBZ6iyX9alpdxLCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛یک منبع آمریکایی به العربیه:
آمریکا درخواست ایران برای رفع محاصره را نپذیرفت.
فرصت‌های دست‌یابی به توافق محدود است.
اختلافات و موانع بزرگی همچنان میان دو طرف وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72097" target="_blank">📅 07:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72096">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wr3O64du7nSRJIh-p7kZDNDVQsq4wuDti68PwgkwXskX6G-SyFm8RfMksGDhi3i2oZUo8ucYdoNZr2aY9WBXvEt35fravSLdN-IzaT3U5gyFV3aA5qJme-mrP4eWgNHFQM3LSYYnXHPBD_Rc7LDayOymI469RMklT13A5GP4FC3qBfsoPU8ubZ-0sXe58-vlHp3IDkNFr6JWodHYoVcfvt-pNSl0iBXrxmUEUaQGh2SUG0nbTZYIu7w1QXptiMFTRkctxq5uf9EI--9GzMdTOAZMWwjfirGgZ5of2VmsBrEjFZujoOr8xhjSXaTfBJv1FXSeFqPK7-7bFPlO9vlD6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استیو ویتکاف:
امروز در حاشیه مجمع عمومی سازمان ملل، از طریق میانجی‌هایی که در طول روز میان دو طرف در رفت‌وآمد بودند، گفتگوهای مفصلی با هیئت ایرانی انجام دادیم.
آن‌ها یک دور از مذاکرات را با موفقیت به پایان رساندند؛ مذاکراتی که امیدواریم سازنده و نویدبخش باشد. میانجی‌ها به کار خود ادامه خواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72096" target="_blank">📅 06:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72095">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83dc83eba1.mp4?token=nVUk8YkrlDXYTjwJ66lzA3q7pips347gNZHmZhkj8JiU90Tyz58dEGRgnxJeDSmnIokI-YBkNy8PS5Mh10ldTaSdkwfCNHrHgNTXedNoh3MMdPCxIrmaEll_Xc_2Z2WcE8hfVpo5MROhqC53Bxq5Kv_oX1FmhDMNt2RhAHP7bvm_dpkgXh-kNnbzr-WRLS0JTUoxT2nfyWqGwT6M8s5gRwYOLTmd4Tyj_2lGjd-djmZq6CV7aY3qkKWnN8JcR5-uPJzKmotqz5giV_0C9HPA4L9xau1XATG_6ySaxUliHteoC_AGqwtAZmNr0N0G6WeJNxc-fM-gtkEDygcBmuBCeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83dc83eba1.mp4?token=nVUk8YkrlDXYTjwJ66lzA3q7pips347gNZHmZhkj8JiU90Tyz58dEGRgnxJeDSmnIokI-YBkNy8PS5Mh10ldTaSdkwfCNHrHgNTXedNoh3MMdPCxIrmaEll_Xc_2Z2WcE8hfVpo5MROhqC53Bxq5Kv_oX1FmhDMNt2RhAHP7bvm_dpkgXh-kNnbzr-WRLS0JTUoxT2nfyWqGwT6M8s5gRwYOLTmd4Tyj_2lGjd-djmZq6CV7aY3qkKWnN8JcR5-uPJzKmotqz5giV_0C9HPA4L9xau1XATG_6ySaxUliHteoC_AGqwtAZmNr0N0G6WeJNxc-fM-gtkEDygcBmuBCeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود هم رسید نیویورک
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72095" target="_blank">📅 06:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72094">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72094" target="_blank">📅 01:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72093">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72093" target="_blank">📅 01:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72092">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">صدای دوانفجار جدید در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/72092" target="_blank">📅 01:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72091">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hm6B02nrzZEL3rxkw0TnA22nBkaxeC_zIgZHBUE6enPlgL6uZQ2v9PHHFyfTyYIgpfAOUc1Yzv9Qz76JIK7ZP2sgAZV2Hg6SIckWa-b1xO-Ot66LVq3whdCMaAC_HNlpkpoIH4sx6ofAW-N1xv3qNeAoAzhy9j3zieW7FfRMpcUMlkJ_dFaxLpNOXMz5PzwUq7uknr-M5A5B-E_3jydyxE8gZ_oqZfj0EWr4CqVhVKwrKXkrm84mzZVrCnVVqyfOjB9ULGhXqPAZMoiu0IUeNyw0z9o5H3iD19mFQyOpB-xbk2OqOy0r71kuYjOlAZArzlqpwBV317yj1HelJZXIDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای‌نت:
انتظار می‌رود سخنرانی نتانیاهو در سازمان ملل به شدت بر ایران متمرکز باشد و به گفته‌ی ایدز، این سخنرانی حاوی «غافلگیری‌های» نامشخصی خواهد بود.
هیئت نمایندگی اسرائیل همچنین خود را برای احتمال مزاحمت یا خروج هماهنگ‌شده در طول سخنرانی آماده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72091" target="_blank">📅 01:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72090">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ایرنا: صدای انفجار در حوالی جزیره قشم به گوش رسید
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72090" target="_blank">📅 01:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72089">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3046a77aed.mp4?token=uUBkUV0PL-UoswaBNpJrhrTEYDbhRm24edKrDuHelTbBYYv15lgDLuPNhAd8FndhFtkqV7QkFTQyPMMPLwaDNNusOzskgeJjiwn2i5gbS69NPm9U80JWlEi4A76WmFEwiwVSTzhRXzYfehwaHaAvu86H_5h-3mztmjsw4OLWtATRI2C1HgIDIAsMf74ZJRHjRd7JIU0BB7AZQbblXoRt3Z29UnyfREcWvchFP4CR-y9xtcRsDzmT7EU7E42_sy6nYskf3JtKlfOBtoUuva_mrICNBmrPrQr-qEc-m8zttZww2IvTQT2HBMFY5Ho6zoyuSQE_SnOIz19qSxosYjeSPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3046a77aed.mp4?token=uUBkUV0PL-UoswaBNpJrhrTEYDbhRm24edKrDuHelTbBYYv15lgDLuPNhAd8FndhFtkqV7QkFTQyPMMPLwaDNNusOzskgeJjiwn2i5gbS69NPm9U80JWlEi4A76WmFEwiwVSTzhRXzYfehwaHaAvu86H_5h-3mztmjsw4OLWtATRI2C1HgIDIAsMf74ZJRHjRd7JIU0BB7AZQbblXoRt3Z29UnyfREcWvchFP4CR-y9xtcRsDzmT7EU7E42_sy6nYskf3JtKlfOBtoUuva_mrICNBmrPrQr-qEc-m8zttZww2IvTQT2HBMFY5Ho6zoyuSQE_SnOIz19qSxosYjeSPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت
ترامپ:
یا به توافق می‌رسیم، یا کار خیلی خیلی سریع تمام خواهد شد.
آن‌قدر سریع تمام می‌شود که سرتان گیج می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72089" target="_blank">📅 01:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72088">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y7Ba0R4shgo0GAGfxJ9L78pqjYSiK-y4YVr82PM1gkvPnFUkIj8s-ZYKqx16vH-lCKXwKCJCv6_OrF8QNsBfEPyxCwqCHqYf2FceO2Fi3o_Gkv3vb_wno--MHvhiMRSyWDhgxBWPFBKaXo9BKYqpAKJEqHHywN3OyEWXQCG1eKx5bBaju2hisdJ3pmc_sauV-jGWL_YcZCDDtgmpXimJEoAn9bu6_RrfMd4leDW7J80MzbWMIrxrqj16AF2Uku3nCZxVo9rV7UJ9snE3Xisb4melgZd_ulLs-not18-sc5l0pbKf8Ez3YeZV6j-vRYzIEsAFcERSjpRRaxYdyypSPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که تندروهای جمهوری اسلامی از پزشکیان تو نشست سازمان ملل دارن:
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72088" target="_blank">📅 01:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72087">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تابستون هم تموم شد و رسما وارد پاییز شدیم...
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72087" target="_blank">📅 00:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72086">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ساعت ۰۰:۴۷ بامداد چهارشنبه؛ یک انفجار در محدوده تنگه هرمز رُخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72086" target="_blank">📅 00:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72085">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a836832d.mp4?token=CSp_Vz1dDyinaTxweWA2rW316Bj61J3_TuFw91Z9ZOFi1ncDiPQ5OTWzwuO0akuP5CIcXLkj0ihpeQocBj6kPYmpgIw4XH7ErBCcUV8g3G8Jb_XHa2p5wOUC6RAGhmi3ntfFZj0voowUC8Jx-3e0PZ7PqjjhTdkA4e9UHRUrto8o5sK_sYCaDNi0Nsz0HigHWhfOsonW2VJN5Bt_MAoG-SHkU7ErYmejyZkhQyxZJd0flKP6iSqEURB1G2CgzZMZI57jyOUBzT9F3VGG24kW_6zBNu5yCKO7UHy99PMHqSJp9yF1f7q_aG9nEMdmFSK0oPN2prvP1zdiI_nSbXJOzIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a836832d.mp4?token=CSp_Vz1dDyinaTxweWA2rW316Bj61J3_TuFw91Z9ZOFi1ncDiPQ5OTWzwuO0akuP5CIcXLkj0ihpeQocBj6kPYmpgIw4XH7ErBCcUV8g3G8Jb_XHa2p5wOUC6RAGhmi3ntfFZj0voowUC8Jx-3e0PZ7PqjjhTdkA4e9UHRUrto8o5sK_sYCaDNi0Nsz0HigHWhfOsonW2VJN5Bt_MAoG-SHkU7ErYmejyZkhQyxZJd0flKP6iSqEURB1G2CgzZMZI57jyOUBzT9F3VGG24kW_6zBNu5yCKO7UHy99PMHqSJp9yF1f7q_aG9nEMdmFSK0oPN2prvP1zdiI_nSbXJOzIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
استیو و جرد امروز جلسه بسیار پرباری با میانجی‌های ایران داشتند. باید دید در ادامه چه پیش می‌آید.
به گمانم انگیزه و شتاب زیادی برای دستیابی آن‌ها به توافق وجود دارد؛ این همان چیزی است که از همه می‌شنویم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72085" target="_blank">📅 00:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72084">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e28a4d4c0.mp4?token=BbWdPRJfDdxH9a1o1CtoZT2jZs3x41gUFFHGlve4CA0uM-YRqllSLywJqmF1VRLxECFzqHUicOS3TIGPguS28CHs9tNcB3FFrmwTp__FesTDbt29Vw92L6j-VPPnwWDQpWqWM3figcnNNz1-ft2eeRiPhrQeCqQGuRA5MgXmsLxETFK8Pc6_30sDF7yL4NGQhcJEMVrjjevJuag9cI1GZsNyVXHxRXazBADNujckr31Z3H4GePXwPj9NuhtMbOArZn1K7rtvP6Gro6HoarMp17z26T31WCXBW4nIFzboYNXoPUETLb7a1uugsYEpDlCNvlAPgq65on5lRASIVoONAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e28a4d4c0.mp4?token=BbWdPRJfDdxH9a1o1CtoZT2jZs3x41gUFFHGlve4CA0uM-YRqllSLywJqmF1VRLxECFzqHUicOS3TIGPguS28CHs9tNcB3FFrmwTp__FesTDbt29Vw92L6j-VPPnwWDQpWqWM3figcnNNz1-ft2eeRiPhrQeCqQGuRA5MgXmsLxETFK8Pc6_30sDF7yL4NGQhcJEMVrjjevJuag9cI1GZsNyVXHxRXazBADNujckr31Z3H4GePXwPj9NuhtMbOArZn1K7rtvP6Gro6HoarMp17z26T31WCXBW4nIFzboYNXoPUETLb7a1uugsYEpDlCNvlAPgq65on5lRASIVoONAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
امیدوارم پیش از آنکه خیلی دیر شود، هرچه سریع‌تر کار درست را انجام دهند.
می‌دانید، زمانی فرا خواهد رسید که دیگر خیلی دیر شده باشد و ما دیگر فرصتی برای اینکه اجازه دهیم آن‌ها به عنوان یک ملت باقی بمانند، نخواهیم داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72084" target="_blank">📅 00:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72083">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تسنیم:
دیدار استیو ویتکوف، نماینده آمریکا، با عباس عراقچی، وزیر امور خارجه ایران، در حاشیه مجمع عمومی سازمان ملل متحد، پس از درخواست‌های مکرر طرف آمریکایی برگزار شد.
ایران اعلام کرد که از این جلسه برای بیان شرایط خود برای بازگشایی تنگه هرمز، از جمله لغو فوری محاصره دریایی، آزادسازی دارایی‌های مسدود شده ایران و پایان جنگ در همه جبهه‌ها، استفاده کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72083" target="_blank">📅 00:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72082">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a836832d.mp4?token=q8O-GhReAiyCCqL_k7ViRvWmbMzCkIiiN9isiQL2XvN3YxWoX6pQwUuEWOYfaXmBnSOlD9rDz3oq_ndfLRk9eMLeyNTXTpoWg3olXTovEs_cRyC4j6gQqWLxrUXC6YuFb1vyMgwdsOMWTNdRWOEZb3iQsYs1z9MVLlJpfrEug_gA68-qPQ-ynE9ch_m6mKLPt0kgSp7GRk6q9uAhAS3K_PUg05TCjIcBB1Uyj4M2UFg1RtqSETZxR8vmrPxbfPdt4HLnqkxvWDVxcBz3Jv5uZIub_Iv8etzI4GOQswewo0Zk-TzRVMzbJcXGk4ZyAdWyR4JwLXrcjJYsJcqyS-7oGTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a836832d.mp4?token=q8O-GhReAiyCCqL_k7ViRvWmbMzCkIiiN9isiQL2XvN3YxWoX6pQwUuEWOYfaXmBnSOlD9rDz3oq_ndfLRk9eMLeyNTXTpoWg3olXTovEs_cRyC4j6gQqWLxrUXC6YuFb1vyMgwdsOMWTNdRWOEZb3iQsYs1z9MVLlJpfrEug_gA68-qPQ-ynE9ch_m6mKLPt0kgSp7GRk6q9uAhAS3K_PUg05TCjIcBB1Uyj4M2UFg1RtqSETZxR8vmrPxbfPdt4HLnqkxvWDVxcBz3Jv5uZIub_Iv8etzI4GOQswewo0Zk-TzRVMzbJcXGk4ZyAdWyR4JwLXrcjJYsJcqyS-7oGTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
امروز یک نشست فوق‌العاده و مثبت بین کوشنر و ویتکاف با نمایندگان ایرانی داشتیم
واقعا در مسیر خوبی حرکت می‌کنیم اونا خیلی میخان توافق کنن اینو همه میگن
شتاب قابل توجهی برای مذاکره داشتیم
اقتصاد ایران رو منزوی کردیم اقتصاد اونارو نابود کردیم این خیلی خوبه
تنگه هرمز رو از مین ها پاکسازی کردیم و نفت جریان داره همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72082" target="_blank">📅 00:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72081">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4086006d.mp4?token=i4pCUCbYlmi_Dkxywyy4Nv-zPqa7GzdToznYvfWgWX-cBvxuSeIoBw__Zhax0VpEXjNTj3ZYd7MujoxR061t1TJEVNncpa0VIDz24GD2CFaaOwKv1a1Joysembk3110rTe5lL2cNJBXvJ3Am6NQ7Wf53YFgvUNv5EvF8vs3crsARauaax65GNJMeZ9D9yaacbWZMkDYxg92oFvaaDVi2Nr1ig603H3cujSktBKwsQMuKBx5KYASHPaYBNSvcLfpLjCtqZzJf08f1a2GeuBwGcqiiMqow34beXLLlx0iiXAvfx6SJ2eLr-MJKWsAd5zadAIteUe7kFCKnwErsTnvzVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4086006d.mp4?token=i4pCUCbYlmi_Dkxywyy4Nv-zPqa7GzdToznYvfWgWX-cBvxuSeIoBw__Zhax0VpEXjNTj3ZYd7MujoxR061t1TJEVNncpa0VIDz24GD2CFaaOwKv1a1Joysembk3110rTe5lL2cNJBXvJ3Am6NQ7Wf53YFgvUNv5EvF8vs3crsARauaax65GNJMeZ9D9yaacbWZMkDYxg92oFvaaDVi2Nr1ig603H3cujSktBKwsQMuKBx5KYASHPaYBNSvcLfpLjCtqZzJf08f1a2GeuBwGcqiiMqow34beXLLlx0iiXAvfx6SJ2eLr-MJKWsAd5zadAIteUe7kFCKnwErsTnvzVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداوسیما:
آمریکا داره آب خلیج فارس رو می‌ریزه تو امارات تا تنگه هرمز خشک بشه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72081" target="_blank">📅 23:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72080">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=e428nXvWah3dJN8yXqHGN7yXwE35Rtv5zKmLz2AgX0McJ4gBWceUs9XkYYsU_3c87hRA0pgOPoFeW6LViYQIXE-E1oY2V-AbQfsdy2P61N3HuA39QMoxWpow7eRHdeFepIyOEn8lOx1PVJY_hkQ6oKqYG3JQr51oAbZEC_VObZivY4FxjRjMENefzI89BYUalWpSO6jut-ETwFB_tCS-genL97PYkUs-l1Nslju-s902UP1-skDxVV7_gyippou9oCZo-518mBHw9ZnayUF1lki1245SGeFVj5-mCwKHGk07WygaXFKa0KN5gH1kZeAZ89UF_ZkVBdJfoKYzeVcGEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=e428nXvWah3dJN8yXqHGN7yXwE35Rtv5zKmLz2AgX0McJ4gBWceUs9XkYYsU_3c87hRA0pgOPoFeW6LViYQIXE-E1oY2V-AbQfsdy2P61N3HuA39QMoxWpow7eRHdeFepIyOEn8lOx1PVJY_hkQ6oKqYG3JQr51oAbZEC_VObZivY4FxjRjMENefzI89BYUalWpSO6jut-ETwFB_tCS-genL97PYkUs-l1Nslju-s902UP1-skDxVV7_gyippou9oCZo-518mBHw9ZnayUF1lki1245SGeFVj5-mCwKHGk07WygaXFKa0KN5gH1kZeAZ89UF_ZkVBdJfoKYzeVcGEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی آلمان یه دختر تریان (انسان‌های که فکر می‌کنن حیوانن) به یه خانم حمله می‌کنه و گازش می‌گیره، به پلیس اطلاع داده شد، هر چقدر از دختر اسم و فامیل پرسیدن فقط پارس کرد، پلیس هم اون رو برد مرکز نگهداری از حیوانات
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72080" target="_blank">📅 23:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72079">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/956bc67dd9.mp4?token=vL7E_Ck8MQ00UoyIEX9blFq7UdbjhvjJMgD-6mdfDppfWDE38ICJjBp-DSn_uVm7KlxCE6x_cMw-1vnx-ppkwtTfhwUMAVH9d93HsoDKiWwjsADpC1C4tD21LBZyYy7yKNnzVdX2FBXSDUC2oQ5i-t34uVtniv7G1co0srH9Ak90nRUvZZ-vBt8d93TJ0q5Um6Mv59rF9rtByFDQeNaKQB80T_q3YBfV84HyFDjeZ_y0c8st2P27vTzbkw_5Hr1BSt962I3NpQs34a2G6MaF4OPnJiHJkTNd4tkES8BS6dzi1zitVnVVtbDFS_0GrRK-z_8Bv2KBa9quQ9ALzBZfYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/956bc67dd9.mp4?token=vL7E_Ck8MQ00UoyIEX9blFq7UdbjhvjJMgD-6mdfDppfWDE38ICJjBp-DSn_uVm7KlxCE6x_cMw-1vnx-ppkwtTfhwUMAVH9d93HsoDKiWwjsADpC1C4tD21LBZyYy7yKNnzVdX2FBXSDUC2oQ5i-t34uVtniv7G1co0srH9Ak90nRUvZZ-vBt8d93TJ0q5Um6Mv59rF9rtByFDQeNaKQB80T_q3YBfV84HyFDjeZ_y0c8st2P27vTzbkw_5Hr1BSt962I3NpQs34a2G6MaF4OPnJiHJkTNd4tkES8BS6dzi1zitVnVVtbDFS_0GrRK-z_8Bv2KBa9quQ9ALzBZfYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی فروتن، عمو فیتیله‌ای:
این روزا وقتی دختر، پسرا میخوان باهم دوست بشن، خیلی برای همدیگه لاف میزنن!
معیار انتخابم که شده پول، قیافه، خوش گذرونی و... به نظرتون گند نزدیم به عشق و عاشقی؟
یه زمانی آدما دنبال کسی بودن که نه تنها حرفشون، بلکه سکوتشون هم بفهمه. به خودت احترام بذار و با هرکسی وارد رابطه نشو.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72079" target="_blank">📅 22:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72078">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">امیر قطر در مورد غزه:  اسرائیل به نوبه خود باید به تعهدات خود به طور کامل عمل کند: توقف قطعی عملیات، خروج از نوار غزه، لغو محاصره و ارسال بی‌قید و شرط کمک‌های بشردوستانه.  @News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72078" target="_blank">📅 21:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72077">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88614b72e8.mp4?token=HDO3zC4w97K_FYvyn8GaUL6QZWucPKux0RaJUGRIos1mqQLaqHaFOaMTE2AuRfqMQUxDrZ2Y0Es4sMh4aZILD8tkBsUNjBRUrzbYay3KZdCkwboQLufFeGX-OliDzGFtO9cp02velDzvklnFz96Z3dXbGnCV8GeHoSDHPspJ5fTgx5Pt557s_ol2fAtV2AzBQP59Pz6ITCrZjPJZRYeKSli_5bHyxACcvEfpSduJVbAUGVG1QSOuKW6aGfIAcrPzmZrxfY5g2MLZRRUK2X1NFMjLZLFsTXhwTjktk5i-uL3Ct5OpN3KQBNIBAv0sMLf14WtJXElRAU5U6if9y189RIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88614b72e8.mp4?token=HDO3zC4w97K_FYvyn8GaUL6QZWucPKux0RaJUGRIos1mqQLaqHaFOaMTE2AuRfqMQUxDrZ2Y0Es4sMh4aZILD8tkBsUNjBRUrzbYay3KZdCkwboQLufFeGX-OliDzGFtO9cp02velDzvklnFz96Z3dXbGnCV8GeHoSDHPspJ5fTgx5Pt557s_ol2fAtV2AzBQP59Pz6ITCrZjPJZRYeKSli_5bHyxACcvEfpSduJVbAUGVG1QSOuKW6aGfIAcrPzmZrxfY5g2MLZRRUK2X1NFMjLZLFsTXhwTjktk5i-uL3Ct5OpN3KQBNIBAv0sMLf14WtJXElRAU5U6if9y189RIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر قطر در مورد غزه:
اسرائیل به نوبه خود باید به تعهدات خود به طور کامل عمل کند:
توقف قطعی عملیات، خروج از نوار غزه، لغو محاصره و ارسال بی‌قید و شرط کمک‌های بشردوستانه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72077" target="_blank">📅 21:48 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
