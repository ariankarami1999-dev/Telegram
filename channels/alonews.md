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
<img src="https://cdn4.telesco.pe/file/hejHqzUpMzzX9DxeFZL0MfxDD0g86OSyNx5bvdbsZnjmU0RhnERMh9wkGfThcuplrm1pwJPscV-f4dZsc-qlsHLAH5WPw0R6v9dz4VIKYStW4aZKhb2gXPRB8CRSPQ_Y1Yim_ILwW-8nQzmeJQMR3_Y7zWyfqVumHNnva8RMgLzzJE3RsF2XNVbISMxSby9bvK_J9Ic-frPQp88XPOpvy3crmWJrzeGHSgo8BWLsGSREj9yP3xAAoVQ-x0DX67zBISIIMbJqUgv6s2XjMzEVPQfJr4qbINQHH0_jFlrdr7GBpRMA-EhRvo_XWxeK-pE9k3Pob-vk3utejqwmeSv7Lg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 933K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 18:42:55</div>
<hr>

<div class="tg-post" id="msg-147744">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c27adce909.mp4?token=VESmLcAabX2l-6MVSWC5Uo5k7j8aQFPcc3bVjsCvBsvYsHDHX3WVEgg31lj12_JasCu67PZRh3p7cxKnyg6dV9GwpB3dhbzTfRCECuG8LeaG4sF5a70epXxwAwu2yvGZ4OGi6O3G0-RsZnQhHf6nngZm7thflaCyuF94BqlXaMprmObWio-odhpa2GwQgk_Kw4KxREHTJkQIIvZv1ErxldqQEJkc9XvQBNbNHgz3iShoI2-I3ck_PZT-G34ByprKi9-q_3UGTI-3G-ALpxz6mxRYknumx5mV5d62Stf7W5FfvM6BqL38hMGNZJmsK00gYiKQ274ZMQg2ukAKRC5CHYd6B11GY6r59XGGNiBtAtXLrpMhOEtoob81NM454N_X_jO7QDaZFI7ET9vnPVTNVtvCUgomn28f54nK6-1Hgby1_TCpR3tCI8_oEuFnDOnTxSj9MFKffcvOOhKM_mdUMPVri0N2Cd5NYBKin1cz5aUifazyj5w1nv5SKryo9r9TbeZFezO3V5VnoSrpWcEgZKC_yZSUcwgXM_JB5iiEQHJKP9XDt97MA8G2m4S6Im9IBkKWZUjjfl8fu_Q2De2Hpm_mIXNwaza6MQLegLALCDyVF1Mofo-cchhFkY29c5Ucc6mu9Y9hyD6Hx8Zpui9texQbwD3fnQy531AJswqFhmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c27adce909.mp4?token=VESmLcAabX2l-6MVSWC5Uo5k7j8aQFPcc3bVjsCvBsvYsHDHX3WVEgg31lj12_JasCu67PZRh3p7cxKnyg6dV9GwpB3dhbzTfRCECuG8LeaG4sF5a70epXxwAwu2yvGZ4OGi6O3G0-RsZnQhHf6nngZm7thflaCyuF94BqlXaMprmObWio-odhpa2GwQgk_Kw4KxREHTJkQIIvZv1ErxldqQEJkc9XvQBNbNHgz3iShoI2-I3ck_PZT-G34ByprKi9-q_3UGTI-3G-ALpxz6mxRYknumx5mV5d62Stf7W5FfvM6BqL38hMGNZJmsK00gYiKQ274ZMQg2ukAKRC5CHYd6B11GY6r59XGGNiBtAtXLrpMhOEtoob81NM454N_X_jO7QDaZFI7ET9vnPVTNVtvCUgomn28f54nK6-1Hgby1_TCpR3tCI8_oEuFnDOnTxSj9MFKffcvOOhKM_mdUMPVri0N2Cd5NYBKin1cz5aUifazyj5w1nv5SKryo9r9TbeZFezO3V5VnoSrpWcEgZKC_yZSUcwgXM_JB5iiEQHJKP9XDt97MA8G2m4S6Im9IBkKWZUjjfl8fu_Q2De2Hpm_mIXNwaza6MQLegLALCDyVF1Mofo-cchhFkY29c5Ucc6mu9Y9hyD6Hx8Zpui9texQbwD3fnQy531AJswqFhmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر انرژی ایالات متحده، کریس رایت:
خدا را شکر که پرزیدنت ترامپ در مسائل مربوط به انرژی، دیدگاه‌های منطقی و معقولی دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/alonews/147744" target="_blank">📅 18:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147743">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2394ff45bb.mp4?token=TsWcwR46Rn_xHnMhv9dvbL_GVmxiD7PSAa7y_e8SWeWIS8vVd_QLZKd3aMLRXkXJM6nSQAFoGzEV_zxB3Xss4oKp34EWNZOGCm6OmAFAwrZXtQRNwqmsF7uBDh5Q3z04iu1tr5h5iVOTVZY-_CEl3DTgVfXRH5vVjIJzj-Le0dHhn-n1oVHQq3wEv2_RpolHXaVhXd3kkZINDAQFMSNiZqmV92BZDk_JViN5wi-u63k7oUMUhLj_Kveajm-7OaqSEUr3sCKDNu4PFKTFJKJXeVgsebn-6hIC94CVGECzchQEXLJ1NBVtim5diGGqQVYZBvCMuL6hVAiw3yvLjpAzyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2394ff45bb.mp4?token=TsWcwR46Rn_xHnMhv9dvbL_GVmxiD7PSAa7y_e8SWeWIS8vVd_QLZKd3aMLRXkXJM6nSQAFoGzEV_zxB3Xss4oKp34EWNZOGCm6OmAFAwrZXtQRNwqmsF7uBDh5Q3z04iu1tr5h5iVOTVZY-_CEl3DTgVfXRH5vVjIJzj-Le0dHhn-n1oVHQq3wEv2_RpolHXaVhXd3kkZINDAQFMSNiZqmV92BZDk_JViN5wi-u63k7oUMUhLj_Kveajm-7OaqSEUr3sCKDNu4PFKTFJKJXeVgsebn-6hIC94CVGECzchQEXLJ1NBVtim5diGGqQVYZBvCMuL6hVAiw3yvLjpAzyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری
: آیا شجاعت کافی دارید تا زمانی را تعیین کنید که قیمت‌های انرژی کاهش می‌یابند؟
🔴
کریس رایت
،
وزیر انرژی
: من قطعاً نمی‌توانم رفتار و اخلاق مقامات ایرانی را پیش‌بینی کنم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/alonews/147743" target="_blank">📅 18:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147742">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
همزمان با سالگرد زنده یاد مهسا امینی، فضای اکثر نقاط کشور امنیتی شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/alonews/147742" target="_blank">📅 18:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147741">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NZ0IEMES2ksO0j-wp-FFQXSEhqwBHknTGyR3xU0g8HxZh3MJ4s_KI1uxilWGA3tTFYm3iijUggu9zZw3tjHhIpG5pH6yrZt1b07-fM70ULcsiCTWGIKTr9zcnwrhlrHMvC3LYDs4fT0bg3Gx907pyfihxveeqzAhNcUEG1w1P-_RJrbrTs9FZ8RF8y4GqSvZVcWfr7EKij0rM8mGK0i3-cw4N7GADPYU4VYBO05Qa0flNMrN6NkZ_pg224slXVQuArqujeVvIZFGDqM7diAnvtdm6GVVL-iZg9HIhlD3roX1QQ0cxNxZtMvsF3fOklBMQpbU22D87zjiuDZ4hPbbFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حوثی‌ها قطعات جنگنده اف ۱۵ عربستانی رو تو فرغون ریختن و بردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/147741" target="_blank">📅 18:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147740">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
نتانیاهو: ما با یک حمله جهانی علیه دولت اسرائیل و نیروهای دفاعی اسرائیل مواجه هستیم.
🔴
در این حمله، دولت اسرائیل و سربازان اسرائیل نه‌تنها به‌عنوان مرتکبان جنایات جنگی — که بزرگ‌ترین حماقت قابل تصور درباره منصف‌ترین ارتش جهان است — بلکه به‌عنوان آزاردهندگان اقلیت‌ها نیز تصویر می‌شوند.
🔴
دولت اسرائیل مانند جزیره‌ای از پیشرفت، جزیره‌ای از تحمل و جزیره‌ای از امنیت است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/147740" target="_blank">📅 18:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147739">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/070959ba10.mp4?token=OqFCD1KRQWfKZRJxP053mKSduR6Itx_1umtRo0coxCWMDN06q0z6-LF2D0rE85f35-JsKjTqDkjD68L5VbBx1nuBfCrqUx-DAFJtJnsRc82fKXPCZC96AU4hh-WP8j1oiwcxtk19CAOcCcNxqZBwhSPN47bmEtGX5gze8opTXLzJkRlsZu8d8m4wFxAVS9aXYTnigjaL-sP5Ad-akWfKtkDo4Avg6BTbraohDqh2OcUTZnEtPecsYDmv2yU-_Up63nCA4EAskLB2AdrqkldLSLHePwnz5IDmc5d8NBy_h-zjtOtfyATgC3_5KYRubMIn0qhKzHRjX7Ju0INA7cMMUZMs9tEDaOsruY08q-7qIKEO0wPVSfQsCPKLKm8OkFihHiVzsCrihJkxyNso3Ixu1zBUtSXwEelo40Ef8XbpJC1dZ9l0-Er6ukm9zjVicY56TU_yD5O6LMzxPVSyPEFMqiDuWU5fpLYtsN7timFFkbzguFEzqktaV7-nP0tG8zpb0nOxLaWixzNkDgshohLYJIekm9x7naMIo06JBJ_ZeLKZRnuEiOTDmFSGbznwySM4wNO-nEo8j01wqlVU0DWsO58batSDs8lpduoiLLHwhTgeSSc6QETiwPgKy1x2vdmeR4bLxlOtcvQbFTaKHj7XrWaIhwWxLT2gIyxLuRjRyA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/070959ba10.mp4?token=OqFCD1KRQWfKZRJxP053mKSduR6Itx_1umtRo0coxCWMDN06q0z6-LF2D0rE85f35-JsKjTqDkjD68L5VbBx1nuBfCrqUx-DAFJtJnsRc82fKXPCZC96AU4hh-WP8j1oiwcxtk19CAOcCcNxqZBwhSPN47bmEtGX5gze8opTXLzJkRlsZu8d8m4wFxAVS9aXYTnigjaL-sP5Ad-akWfKtkDo4Avg6BTbraohDqh2OcUTZnEtPecsYDmv2yU-_Up63nCA4EAskLB2AdrqkldLSLHePwnz5IDmc5d8NBy_h-zjtOtfyATgC3_5KYRubMIn0qhKzHRjX7Ju0INA7cMMUZMs9tEDaOsruY08q-7qIKEO0wPVSfQsCPKLKm8OkFihHiVzsCrihJkxyNso3Ixu1zBUtSXwEelo40Ef8XbpJC1dZ9l0-Er6ukm9zjVicY56TU_yD5O6LMzxPVSyPEFMqiDuWU5fpLYtsN7timFFkbzguFEzqktaV7-nP0tG8zpb0nOxLaWixzNkDgshohLYJIekm9x7naMIo06JBJ_ZeLKZRnuEiOTDmFSGbznwySM4wNO-nEo8j01wqlVU0DWsO58batSDs8lpduoiLLHwhTgeSSc6QETiwPgKy1x2vdmeR4bLxlOtcvQbFTaKHj7XrWaIhwWxLT2gIyxLuRjRyA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کشته‌شدنِ دو نفر به خاطر یه آینه بغل !
🔴
یه جوونی با ماشین داشته تو خیابون میرفته که با یه موتوری درگیر میشه و موتور سوار میزنه آینه بغل ماشین رو میشکونه؛
🔴
راننده ماشین هم میفته دانبال موتور سوار و میزنتش زمین که متاسفانه راننده موتور فوت میکنه و امروز هم حکم قصاص راننده ماشین اجرا و اعدام میشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/147739" target="_blank">📅 18:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147738">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
جروزالم پست اسرائیل: عبدالملک الحوثی، فرمانده حوثی‌ها، بزرگترین پیروزی نظامی خود را در سال‌های اخیر به دست آورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/147738" target="_blank">📅 18:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147737">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFQeiXZQP-G6ovxfD5vVmkH0ARAYSi7qse_2W624T-icpf19XvRzGVWKSwwpalWwSkLP4fv0wJ39fwvL6DcoaCDxNwYJuK1Po1udJ5VCKNwLO2KPrCSi5tMvmqRJrFcG5Q7fYyGBCe174efd02FQdbJyHCJz8l0JnUma0oE0Ws3AacVefc4dTkpCOGTBKnkQ7ZBbvylhSW4fSu-kJ7IkE3jg0Vh-DJg3FoeB6BuXARsYBO_ZvTX8_hc4ylpJIT9Cjx15I3tgeJd_xa9QRzLB2Js-nKWSp6ko2LPVviewOFg5_QcIcZY5KrmQsU0S63EEorGMyR_XMIsLoCJi7Y2sfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حوثی های یمن تصویر سرنگون شدن جنگنده F-15 عربستان سعودی را منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/147737" target="_blank">📅 17:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147736">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
نیویورک‌تایمز: تصویب فروش ۲.۸ میلیارد دلاری بمب‌های سنگین، می‌تواند یکی از بزرگ‌ترین محموله‌های تسلیحاتی آمریکا برای اسرائیل باشد
🔴
این قرارداد پیشنهادی شامل ۴۰ هزار بمب یک‌تنی خواهد بود؛ تسلیحاتی که استفاده از آن‌ها در غزه و لبنان به دلیل آسیب‌هایی که به غیر نظامیان وارد می‌کند، با انتقاد بین‌المللی مواجه شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/147736" target="_blank">📅 17:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147735">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 250 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/147735" target="_blank">📅 17:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147734">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
فاکس‌نیوز به نقل از وزیر انرژی آمریکا: روز گذشته (سه‌شنبه)، ۱۸ میلیون بشکه نفت از خلیج فارس جریان یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/147734" target="_blank">📅 17:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147733">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
روسیه: هر آنچه از آمریکا شنیده می‌شود را با نهایت جدیت دنبال می‌کنیم
🔴
در حال حاضر هیچ گفت‌وگویی درباره «ثبات راهبردی» بین مسکو و واشنگتن وجود ندارد
🔴
هنوز فرصت برای جلوگیری از رقابت تسلیحاتی در فضا از دست نرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/147733" target="_blank">📅 17:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147732">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXtdLovYrzFFRmmqqXr93k2dzQ0VzF5BGteWG_30ZSUCha_P2lHldTv2LHe2BYVJL4bRqK3LXZmqhfyv1-vdlsA54Jh86v0sHxpqdYXjySnPWAF6zPa8Y2i8ffLmBsaa5j0sJwUPOYwFveYcxmVnxjCuc2nzHu14rLeN7__x0--Tg1Ravkb-Hs0gBPh1ZZnsZbgRshxucpUk4k0tvX0DzF9fZdijGinZ8FFt2FJ1wIPLaDSPex8N_DkoMetb8V2YdW_6FI6oXnWXbcbGhPBT3rsEEwWLmss0d7lkKVNNtdQ6GDwaJfDCTOZZZWK5s0myCpge2yUECQe4hqXZmtps2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقامات سعودی به شبکه ۱۲ اسرائیل گفتند که ریاض به طور فزاینده‌ای از عملکرد دولت ترامپ به دلیل عدم اقدام قاطعانه آمریکا علیه حوثی‌ها (انصارالله) ناراضی است.
🔴
یک منبع سعودی نزدیک به خانواده سلطنتی گفت که حوثی‌ها از عدم اتخاذ "تصمیم عملی" توسط واشنگتن سوءاستفاده می‌کنند و این امر باعث می‌شود که عربستان سعودی "هزینه آن را در عمل بپردازد".
🔴
یک مقام سعودی دیگر نیز با ابراز خشم از عدم حمایت منطقه‌ای، گفت: "از پاکستان یا ترکیه چیزی جز بیانیه‌ها به دست نیامده است" و افزود که ریاض احساس می‌کند رها شده است، در حالی که در حال بررسی یک استراتژی جدید برای تأمین امنیت دریای سرخ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/147732" target="_blank">📅 17:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147731">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
مجله تایم: جنگ ۵ هفته‌ای ترامپ، هفت‌ماهه شد؛ اهرم ایران از هرمز به باب‌المندب رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/147731" target="_blank">📅 17:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147730">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbca1430d1.mp4?token=ppG3gOrCD3XIfowrBeXhjdrmfLcDIipYK3H8VHKRd78g7s96lHYkhFswkJWMdDm8vHyO7hC_FtHL-M3OeZa7aOwtEhd9QkaJ4NHxGQQ5RJStN-CPM_DyAPvbW0XfcsucsMpzcSUf8YNjEPT7SWeoiuyGe_vjgFVtAJkhE2XR5Qmrm8Z0XjmsOb5_Id5dN4ZY7Jb8Qc4OPC16BAN9fO3lZSz_CVU4XAoVltKDFiQgCUgeQgT1q9eTdRWaBoMdHSBtsF51PqYH-INbYdkN1OhG587s3rCA4jrE0i1EqeB0NygkWZeU-XVLivWx_5srkl7VvOCw6uLckmcZWa5u8U4_Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbca1430d1.mp4?token=ppG3gOrCD3XIfowrBeXhjdrmfLcDIipYK3H8VHKRd78g7s96lHYkhFswkJWMdDm8vHyO7hC_FtHL-M3OeZa7aOwtEhd9QkaJ4NHxGQQ5RJStN-CPM_DyAPvbW0XfcsucsMpzcSUf8YNjEPT7SWeoiuyGe_vjgFVtAJkhE2XR5Qmrm8Z0XjmsOb5_Id5dN4ZY7Jb8Qc4OPC16BAN9fO3lZSz_CVU4XAoVltKDFiQgCUgeQgT1q9eTdRWaBoMdHSBtsF51PqYH-INbYdkN1OhG587s3rCA4jrE0i1EqeB0NygkWZeU-XVLivWx_5srkl7VvOCw6uLckmcZWa5u8U4_Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شلیک توپخانه ارتش اسرائیل (IDF) به مناطق المنصوری و بیت یحون در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/147730" target="_blank">📅 17:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147729">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سوئد کارمند سفارت ایران را اخراج و سفیر را احضار کرد
🔴
سوئد روز چهارشنبه در راستای اعلام حمایت خود از اسرائیل، یکی از کارمندان سفارت ایران در استکهلم را اخراج کرده و سفیر ایران را نیز به وزارت خارجه احضار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/147729" target="_blank">📅 17:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147728">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
رویترز به نقل از منابع آگاه: عربستان پس از آنکه حملات پهپادی به خط لوله نفتی مهم این کشور آسیب وارد کرد، عرضه محموله‌های نفت خام برای پالایشگاه‌های آسیایی را از طریق انتقال کشتی به کشتی در نزدیکی عمان افزایش داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/147728" target="_blank">📅 17:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147727">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
حوثی های یمن: اخبار منتشر شده در خصوص حمله به جده و مکه را قویا تکذیب می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/147727" target="_blank">📅 17:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147726">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
فاکس نیوز: در اوایل این هفته، یک کشتی آمریکایی با حداقل چهار پهپاد و یک موشک از سوی ایران مورد حمله قرار گرفت. چندین پرسنل آمریکایی در این کشتی حضور داشتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/147726" target="_blank">📅 16:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147725">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUBo-tVOkxro3NbrjhEWQhl8wD1LmqA-K8Y5RPgkrKBc9GeKrHY-bRU-ju3YjPEJS1-AZigtcWb3wvFq_U3wuPditMTwdNCUPvZJYR6ogk1IbUqEHO0vcsids-f9kPrj2lr3d_PWzBgH6COeE3rF2ul841FK9TzpFcDyz7Ep6BhkwWY-6iZObmjkCBM5INcI_53j2Scxwu8Nk3aE7nz82Rucj-gD9SHBr0o3KbKflcN5hlerk77o_VDCcDGDiK058ahADA4-3cdbiiXuEysGPJd4e5oBhrp_ornQsqWyp0Rv1VVkadtSqO72QY-_C2mWcxEYb9t2KCRpkdwbMBY4lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاکس نیوز: در اوایل این هفته، یک کشتی آمریکایی با حداقل چهار پهپاد و یک موشک از سوی ایران مورد حمله قرار گرفت. چندین پرسنل آمریکایی در این کشتی حضور داشتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/147725" target="_blank">📅 16:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147724">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwRDgPacSMG-kh0F2jwcV6LjVmIuBG6Dbvx4DfSz-uRgbVSOgdL7zCAVi4vf9rqPPgJBsQjVD7kqBW8los9IR3Z9Z4vRJX5VLa32Daid7zn77PHdXMkaye0WSUzDbAxAmxKSPLgCdViZ6YMVwDcv5BBqBBj-pFTJLhwKbv6pViVfw3l-K70m7ReBkPW1V6j_cowMR3qIb79h32irxs5gjmWgc21aqhfjsMzOqV2yXZdH2Dred53daLyGSaFSY1X1UudoROsf1bGvOT-xJL5ton3yYiC_aj9958n-MGsbLFkXwQyG2LHvjVOgbC4GjCVt2lB57OPj19sFiqwiI4BcLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
فعالیت گسترده نیروی هوایی آمریکا بین پایگاه‌های این کشور در اروپا و خاورمیانه و ارسال و جابه‌جایی تجهیزات
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/147724" target="_blank">📅 16:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147723">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">به نظرتون کدوم بیشتر رشد میکنه؟</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/147723" target="_blank">📅 16:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147722">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32bc6d9887.mp4?token=CJQMwGclHBiL__TyUz1lc7nzCW4RaUsyxf-gliPodcqImsYs7pS4yi1LJrGBUnr-QuRu60wF_HhawhruSPAq5zS2HQdgspyvoajAIbBI1NDiwp8QnbqAa0gbi7ajkT7muHgtIp7nxEK8ygPOVFC7MpGiTw7rrin8_npsHUHMOQTguZThI1hVrhhHLA_QwOjvIxWekMRKiwdU0KTiLj1FbQSGX3NRqohuwfL4z5d5-TLhWHv9gryg53OtSBbzkFR7F_K_Iy78vAQF5P3tyTXDhrLBkjxxTgGrZQZa3n0ngPQ2G7YjRm33Uv4TuAOqdEOflkzv7rR95osVVO1gLTXiWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32bc6d9887.mp4?token=CJQMwGclHBiL__TyUz1lc7nzCW4RaUsyxf-gliPodcqImsYs7pS4yi1LJrGBUnr-QuRu60wF_HhawhruSPAq5zS2HQdgspyvoajAIbBI1NDiwp8QnbqAa0gbi7ajkT7muHgtIp7nxEK8ygPOVFC7MpGiTw7rrin8_npsHUHMOQTguZThI1hVrhhHLA_QwOjvIxWekMRKiwdU0KTiLj1FbQSGX3NRqohuwfL4z5d5-TLhWHv9gryg53OtSBbzkFR7F_K_Iy78vAQF5P3tyTXDhrLBkjxxTgGrZQZa3n0ngPQ2G7YjRm33Uv4TuAOqdEOflkzv7rR95osVVO1gLTXiWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب تو تهران دوتا دختر با موتورشون چند ساعت پشت یه ماشین تو ترافیک گیر کرده بودن؛
بعد دیگه خسته میشن، میان پایین و می‌بینن اصلا ماشینه راننده نداره و طرف پارک کرده رفته...
[
@AloTweet
]|</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/147722" target="_blank">📅 16:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147721">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
بازیگر ایرانی معروف هالیوود و برنده خرس نقره‌ای: ایرانی با پرچم اسرائیل بیناموسه!
🔴
گویا وی هم قراره به ایران بیاد و به صداسیما دعوت بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/147721" target="_blank">📅 16:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147720">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b8ab3224c.mp4?token=QvwtmTXuTyg3AwbMw6Jyt42TJ06LBNO2Ke8bFANAkZh06VJJPKfSQ1UQa8UFm1d2m6eD9TAGzz9G5TibfUznis3Tor7KG1BlPmPSASf0sG5usOaf_zC8WGwnJU940vJ60WKNvMRwlR7mhJvlxZDMq_6JcuWotD5ZL-BxifWn4bCfjuqDHyJJThUWb7oZ5izDTrngeE1Nc0T0rd07746DW7IvO9r8ojXDZHFQDXmD5vW1yyW7W_tlB4gQVnKpmkX9KC4_FTA4ixkM01XJwAs53i9QmCnM4XvbrT-RJA26MI2w23ujjn_r05sXl91FpN6Tc6QrPy4vKEVZ8ygnFBHkxA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b8ab3224c.mp4?token=QvwtmTXuTyg3AwbMw6Jyt42TJ06LBNO2Ke8bFANAkZh06VJJPKfSQ1UQa8UFm1d2m6eD9TAGzz9G5TibfUznis3Tor7KG1BlPmPSASf0sG5usOaf_zC8WGwnJU940vJ60WKNvMRwlR7mhJvlxZDMq_6JcuWotD5ZL-BxifWn4bCfjuqDHyJJThUWb7oZ5izDTrngeE1Nc0T0rd07746DW7IvO9r8ojXDZHFQDXmD5vW1yyW7W_tlB4gQVnKpmkX9KC4_FTA4ixkM01XJwAs53i9QmCnM4XvbrT-RJA26MI2w23ujjn_r05sXl91FpN6Tc6QrPy4vKEVZ8ygnFBHkxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بازیگر ایرانی معروف هالیوود و برنده خرس نقره‌ای: ایرانی با پرچم اسرائیل بیناموسه!
🔴
گویا وی هم قراره به ایران بیاد و به صداسیما دعوت بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/147720" target="_blank">📅 16:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147719">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
بلومبرگ: پالایشگران ژاپنی پس از تعطیلی خط لوله نفت عربستان، خرید نفت از خاورمیانه را افزایش داده‌اند
🔴
آن‌ها اخیراً نفت خام عمان را خریداری کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/147719" target="_blank">📅 16:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147718">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
تعلیق پروازهای ماهان به استانبول، آنکارا و مسقط
🔴
هواپیمایی ماهان پروازهای بین‌المللی خود در مسیرهای ترکیه و عمان را تا اطلاع ثانوی متوقف می‌کند
🔴
بر اساس بخشنامه‌های ابلاغ‌شده، پرواز تهران–مسقط از ۲۶ شهریور و پروازهای تهران–استانبول و تهران–آنکارا از ۳۰ شهریور لغو خواهند شد
🔴
اطلاعیه این تغییرات به دفاتر خدمات مسافرت هوایی ارسال شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/147718" target="_blank">📅 16:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147717">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c3ece0c92.mp4?token=rCl5sm9rN65f3huN_gw3z_MbwbJWNmk3HJ_pkrahikCM95mI8mZddbXFXKsIpfeA9RwaO3nsvSTO2z3hyc3w09jwcgLGB8jXdMrX_bXQ65L-6ld0VuuOaljZvX88xN8xEbmZnVlWu7tUBQfLpPKJH7DBIFBaX0Cp2yAmJZiMzzdeXWc-kBLNQA4EuQgiN_FzAwfTOU5dkbnCHF6Ks20hmze1s5XYZwPwCfCukUEv74IEAb7IKh6QriFpIKxcBems53hkXqCKNK8P54m00kgMAXBCYhwNtTXz58Un_X8CUinPn1Z9kmLEVJgepPwXfeECbvdRm1lIOqa9c08k9wG-_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c3ece0c92.mp4?token=rCl5sm9rN65f3huN_gw3z_MbwbJWNmk3HJ_pkrahikCM95mI8mZddbXFXKsIpfeA9RwaO3nsvSTO2z3hyc3w09jwcgLGB8jXdMrX_bXQ65L-6ld0VuuOaljZvX88xN8xEbmZnVlWu7tUBQfLpPKJH7DBIFBaX0Cp2yAmJZiMzzdeXWc-kBLNQA4EuQgiN_FzAwfTOU5dkbnCHF6Ks20hmze1s5XYZwPwCfCukUEv74IEAb7IKh6QriFpIKxcBems53hkXqCKNK8P54m00kgMAXBCYhwNtTXz58Un_X8CUinPn1Z9kmLEVJgepPwXfeECbvdRm1lIOqa9c08k9wG-_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرقت گوشی دختر جوان در اسلامشهر در کسری از ثانیه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/147717" target="_blank">📅 16:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147716">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
اورزولا فن در لاین، رئیس کمیسیون اروپا روز چهارشنبه احتمال تبدیل شدن کانادا به نخستین «عضو وابسته» اتحادیه اروپا را مطرح کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/147716" target="_blank">📅 16:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147715">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
رسانه عبری: بن سلمان خود را در برابر حملات انصارالله تنها می‌بیند؛ در حالی که تأسیسات انرژی عربستان هر روز منفجر می‌شوند، آمریکا و اروپا هیچ کمکی نمی‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/147715" target="_blank">📅 15:59 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147713">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFioCslQi50x6YdTf2ym8tt36zkh4h3nO0DUwH-4F9jOpG6DMUEOS7f_cUReOY0gHHsy_7YaaCObiniFJhqPv2jR2R2KaCipg-WNrmmrvSIblsh82EyyO-2ALIHc9N83WCAWI2kfxiTV2VMKufp1EqJsuPvcJE93UlCZ0WcF09uNET8Ib3hG2E_ghRHdDvMsKRfMXDVFdY7MRppC9S1ZGzJlA7HVt2sYEYaH9uKVSDNl3QERtoP1IDoIGC6afq5rmqvmiAU4UeP1BWdw6nX8pVGZfurV3clzn5mCc8jZRx0XF51Nl2FvRIvQYuZryRFE5zZk3clazNSfLhT03w_uTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f303351168.mp4?token=tcUCx4-duLTG9zzlM3sE_rCHHfXmnUp84lNytOzMvsZQ2l_-cHxYnF-tekOD7sgKv2JiHkQk4pmk2kwzvdGMlUUdqznbAEXCHkFR-xpBwnVpiRS3mOaJMRZdaSLL27Li1tCkqY2nBM0NmValjpRTTXe77G_t0YqoMJtQfdzMz3a81aV7KUUYP30knInjWKBe4nQxJKFz17EvdxwhSJ4OZl6LS4AZKDxzKRixO418Rvq8xVtdLuIGEAslBMZb8_IWz99WUv-dHEnAVxvcNnmgJ1qElTD-nfKALvdlNgOz8PqhLmwGCQX747RmX1q16k2C3kMZv6Z-MSgNzvdoARj7iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f303351168.mp4?token=tcUCx4-duLTG9zzlM3sE_rCHHfXmnUp84lNytOzMvsZQ2l_-cHxYnF-tekOD7sgKv2JiHkQk4pmk2kwzvdGMlUUdqznbAEXCHkFR-xpBwnVpiRS3mOaJMRZdaSLL27Li1tCkqY2nBM0NmValjpRTTXe77G_t0YqoMJtQfdzMz3a81aV7KUUYP30knInjWKBe4nQxJKFz17EvdxwhSJ4OZl6LS4AZKDxzKRixO418Rvq8xVtdLuIGEAslBMZb8_IWz99WUv-dHEnAVxvcNnmgJ1qElTD-nfKALvdlNgOz8PqhLmwGCQX747RmX1q16k2C3kMZv6Z-MSgNzvdoARj7iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آنتون گرویس، ژنرال ارشد روسی و فرمانده تیپ زرهی چهارم، در پی یک عملیات پهپادی که توسط نیروهای سامانه‌های بدون سرنشین اوکراینی (SBS) در منطقه دونتسک انجام شد، کشته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/147713" target="_blank">📅 15:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147712">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
دولت گرجستان در پی اجرای تحریم‌های جدید آمریکا علیه شرکت‌های هواپیمایی ایرانی، ورود پروازهای تمامی شرکت‌های هواپیمایی ایرانی به این کشور را از دوشنبه ۳۰ شهریور (۲۱ سپتامبر) متوقف خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/147712" target="_blank">📅 15:48 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147711">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
بابک زنجانی: به‌ مردم ماشین برقی رایگان بدید تا بنزین صرفه جویی شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/147711" target="_blank">📅 15:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147710">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
رئیس کمیسیون انرژی: در پاییز و زمستان امسال به دلیل کمبود شدید گاز احتمال قطع گاز خانگی در برخی استان ها وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147710" target="_blank">📅 15:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147709">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNBu_ozUOHXEZmxif1C2sWqfp_u5FXUHFqlcURFFew82hA9ZN9hOEB1slwoZshRh6HA4kP9hfsejBMpIcF0fpdZ5y9wspxQt0FhyDInxrYSwffbXrTmgvbcY7Cl0SvragguW75N8VN0KyJm14QG-nityK6-RoqmedOGFGIN_-4SBxXqpnOfXMi4sOaD81_zK2vMjfmi56qLMg246QfOAR98xHrQeLwyexvUE0BspNBCwGB8hOGPqJKKglUWM53Wr80Gy1fYOMOk9JoZ69e-0wl7sd0Hzw-3f0bF9NCqQGVfYiTEJUEW_RiOxvcJQQfudlkzK75FFPcPidwP_ESKpLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سرگئی لاوروف، وزیر امور خارجه روسیه، گفته است که اگر ایالات متحده از توافق‌های «آنجاکج» عقب‌نشینی نمی‌کرد و اروپا نیز این کشور را از آن توافق‌ها «دور نمی‌کرد»، «ما اکنون یک سال است که بدون جنگ زندگی می‌کردیم»
🔴
او این موضوع را «یک واقعیت آشکار» خواند و گفت: «نتیجه‌گیری خود را بگیرید.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/147709" target="_blank">📅 15:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147708">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/862138e439.mp4?token=roIP1q6GmO9jFAHa6PeKakjE259wSXGw06iw_5etts6pmTSiHpOo0D_wk6n64deV41LCvYtg3MIu2D12seSEIVcD9J34Ey5-Q_KBakIDpNj5rib6_h6Y5O2orv1YJv7bltQj16_pVjJ17Z_eiO35ga5k3TRriOOdREmbqUfyeK8eS5I7d3Ot99vvZCeEJAIUuczTdXv9tO13g2Yxh5Qb7mGnhIkkTJpa0_1MEi6xkR6YG9VInS0WSfEzRhPVmd7UTIfFeBFBa_tWOBaD4QdzS8HGFs2j-ogxdQR7akRaa-DY1GLyULzyh8cZ-Fv9LiZotAVTuiDMDmhbx3CWPpDsqA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/862138e439.mp4?token=roIP1q6GmO9jFAHa6PeKakjE259wSXGw06iw_5etts6pmTSiHpOo0D_wk6n64deV41LCvYtg3MIu2D12seSEIVcD9J34Ey5-Q_KBakIDpNj5rib6_h6Y5O2orv1YJv7bltQj16_pVjJ17Z_eiO35ga5k3TRriOOdREmbqUfyeK8eS5I7d3Ot99vvZCeEJAIUuczTdXv9tO13g2Yxh5Qb7mGnhIkkTJpa0_1MEi6xkR6YG9VInS0WSfEzRhPVmd7UTIfFeBFBa_tWOBaD4QdzS8HGFs2j-ogxdQR7akRaa-DY1GLyULzyh8cZ-Fv9LiZotAVTuiDMDmhbx3CWPpDsqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه آخوند: تجاوز رو آزاد کنین!
چرا دخترا با هر پوششی میتونن بیان بیرون؟ پس باید برای آقایون هم آزادی باشه و اگه دلشون خواست به دخترا تعرض کنن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/147708" target="_blank">📅 15:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147707">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
روسیه: امارات و ایران به لطف قدرت بریکس، موفق به غلبه بر اختلافات خود شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147707" target="_blank">📅 15:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147706">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
حوثی‌های یمن: تاسیسات آرامکو در ینبع و یک پایگاه هوایی در خمیس مشیط عربستان سعودی رو هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/147706" target="_blank">📅 15:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147705">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
اتفاق وحشتناک برای طلا
‼️
‼️
👇
👇
👇
👇
https://t.me/+cs85WnZxgpM1NjRk
https://t.me/+cs85WnZxgpM1NjRk</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/147705" target="_blank">📅 15:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147704">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75f7c18dc4.mp4?token=fiYMTlzh-jkRvUeZ1jzBuMeGMsJ8jdk5e1K5311krsmIInPf_wlSeZMoZnMrHJdAv-DrMC6lmbu5WnYN_nhTLF33iSuyihrByxMtHUHch3pGd9lW_arftmyeQapCjV-0WNlPKeuyarrwLiesQSvoNZXVxRlWNowb0o6CqxtdM-f3gIIJ_TMlUq0oz276ZwOmj4xXyEoJ4x4Zw21AycgFPtD2-kgEovIjnd0sc6VtYL8uMZ72XMRfwhKZNI8fdUZ7RojSfw5bRB8G522250hcDTG104gZ-Rfxykk3o8aGjfqGaCe4bnsrBZMB-_KJ7MTXk4iTg4n5UrHBWQh8gggw_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75f7c18dc4.mp4?token=fiYMTlzh-jkRvUeZ1jzBuMeGMsJ8jdk5e1K5311krsmIInPf_wlSeZMoZnMrHJdAv-DrMC6lmbu5WnYN_nhTLF33iSuyihrByxMtHUHch3pGd9lW_arftmyeQapCjV-0WNlPKeuyarrwLiesQSvoNZXVxRlWNowb0o6CqxtdM-f3gIIJ_TMlUq0oz276ZwOmj4xXyEoJ4x4Zw21AycgFPtD2-kgEovIjnd0sc6VtYL8uMZ72XMRfwhKZNI8fdUZ7RojSfw5bRB8G522250hcDTG104gZ-Rfxykk3o8aGjfqGaCe4bnsrBZMB-_KJ7MTXk4iTg4n5UrHBWQh8gggw_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جلسه  شورای امنیت درباره تنگه باب‌المندب
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147704" target="_blank">📅 15:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147703">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68da57faf0.mp4?token=KD3L_7A-z4xF2nJOMD03u97HRe5o6M8UNfP1y21KIFUe1BPXXp24DMsu9x6czrO3dfXrs5cI6RWGrK7nAnvdAmvElb1B75ru5_zBOZVxK2km9YUpE5MK86C_Ps8_TTgVAugYDdv7P7iTE0HI7Tn_Ne0tlmisNPXZTM32TiXVaNrGntbWe9K5xxf4uryqTASMmFIbFqi6puugc_MeHJ3D2m9vTJrLovgcagu5SodZ0cievg4GKkbJQyFld57oDBPLaB6ZwC56mgX6SyWqagxLEbLg3nA0ebjegIGA2lj-OP37TN9qnIrSqWjfstufbs0RJgH8jZVWsVM0eKFGJ8OE_JJxJXdqXl77Svu-45AEafhx5Cg-rc7XhMVAyRB74W77XH7cHTE_Of8H5zJ0tMBTFp2e5a30cPS4PgyWcDlWrCamYTWv0Si7b7oBhLjaX0UCYpk2YqucAvImmI787JVQGBUZ3vbbOqrP4FU7Gm8CjCq4XaNkTQ3_QbP8t3y7ZJ4sZThA0KTPylJ8liBEjlLQVfWYoR9F0j4KYpiOXCDAUeiYqExpphQ1flSDxRyI8H0ngC3hMJg6mkMnX_EYTKRGWGvbh-Kivqh7CGVYenPb_HwOdogWf5sKZPH_nVBNV_xIjmtWOwh-o2Wp0jzXRn85eErK4kClulL19e9blwASwGU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68da57faf0.mp4?token=KD3L_7A-z4xF2nJOMD03u97HRe5o6M8UNfP1y21KIFUe1BPXXp24DMsu9x6czrO3dfXrs5cI6RWGrK7nAnvdAmvElb1B75ru5_zBOZVxK2km9YUpE5MK86C_Ps8_TTgVAugYDdv7P7iTE0HI7Tn_Ne0tlmisNPXZTM32TiXVaNrGntbWe9K5xxf4uryqTASMmFIbFqi6puugc_MeHJ3D2m9vTJrLovgcagu5SodZ0cievg4GKkbJQyFld57oDBPLaB6ZwC56mgX6SyWqagxLEbLg3nA0ebjegIGA2lj-OP37TN9qnIrSqWjfstufbs0RJgH8jZVWsVM0eKFGJ8OE_JJxJXdqXl77Svu-45AEafhx5Cg-rc7XhMVAyRB74W77XH7cHTE_Of8H5zJ0tMBTFp2e5a30cPS4PgyWcDlWrCamYTWv0Si7b7oBhLjaX0UCYpk2YqucAvImmI787JVQGBUZ3vbbOqrP4FU7Gm8CjCq4XaNkTQ3_QbP8t3y7ZJ4sZThA0KTPylJ8liBEjlLQVfWYoR9F0j4KYpiOXCDAUeiYqExpphQ1flSDxRyI8H0ngC3hMJg6mkMnX_EYTKRGWGvbh-Kivqh7CGVYenPb_HwOdogWf5sKZPH_nVBNV_xIjmtWOwh-o2Wp0jzXRn85eErK4kClulL19e9blwASwGU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان چندسال قبل: مهسا امینی همینجوری نمرد بلکه زدن کشتنش
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147703" target="_blank">📅 15:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147702">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRCBPP-QNqaZGslN7CTzMaXSv1ZNPWCFwMRxY6jSIjHTAPdhtYnDK7uqorE-0X3FhssCBLpOgJixRXW_dJ_huLoGwsSlDQdKEyS5cX_eZCLBlPCc0HCKeZETU26c6rlJfZ6LeeO6EPAM4wwdFTcAWonCL3H_nWlV0NP8YtisWcphj5dfcoxzPxx-ChFA5ZudOIJoAefe75SPVCHIUiowmw2NZS47lonZqklcA7O5fM-RzAymyeo0pgYKdFIvw675io1QdiUc8syLna4RktocvUYVUFCC9r7kuDKZ2TiLqGeeTvh_6d2wsVecT5n3igIkiwSDI6-Y4f-rm5ciefrJgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز سالگرد جاویدنام مهسا امینی است دختری که فقط بخاطر چندتار مو توسط ظالمین کشته شد
🔴
یاد و نامش تا ابد جاویدان
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/147702" target="_blank">📅 15:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147701">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
نتانیاهو: پیام ما روشن است. هیچ تروریستی مصونیت ندارد و حماس در غزه نخواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147701" target="_blank">📅 14:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147700">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
رویترز: مقامات آمریکایی این هفته در عمان با نمایندگان گروه حوثی دیدار کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147700" target="_blank">📅 14:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147699">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
برخورد ناوهای هند و پاکستان در آب‌های بین‌المللی
🔴
یک ناو نیروی دریایی پاکستان در شمال دریای عرب با یک ناو جنگی هند که در حال گشت‌زنی بود، برخورد کرد. هند در پی این حادثه، دیپلمات ارشد پاکستان را احضار و نسبت به رفتار «غیرقابل قبول و غیرحرفه‌ای» نیروهای دریایی این کشور اعتراض کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147699" target="_blank">📅 14:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147698">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
رویترز: مقامات آمریکایی این هفته در عمان با نمایندگان گروه حوثی دیدار کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147698" target="_blank">📅 14:48 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147697">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">به نظرتون کدوم بیشتر رشد میکنه؟</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/147697" target="_blank">📅 14:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147696">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال: دو نفتکش با پرچم کشورهای خارجی که عازم آمریکا بودند، هنگام عبور از تنگه جبل‌الطارق هدف حملات سایبری قرار گرفتند. واشنگتن تاکنون عامل این حملات را شناسایی نکرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147696" target="_blank">📅 14:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147695">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
یک پهپاد اسرائیلی در ارتفاع پایین بر فراز شهر بعلبک و روستاهای اطراف در حال پرواز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147695" target="_blank">📅 14:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147694">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
کاتز وزیر دفاع اسرائیل: ارتش دفاعی اسرائیل در صورت دریافت دستور آماده است تا حماس را نابود کند و ماموریت را به پایان برساند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/147694" target="_blank">📅 14:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147693">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKQGaGPuxNY5FVsYGDsA0lJ0LmHxetSxrU-IfG6faqQhkwOtKsqADwV-HXXdnzenPdvgiGJ2xu7M-pn3fyhOcb8n0QetIUtYZc_3YAeOTBaSbDX7np5GOUWDZkamJh06tjFZYizCi3lkINcb3yGNBfFmYmYhd_xPLqt2gMJYz8q1Y5lv-DXFeVsD2xcne5tBieyrqwN7ikyB_EFCa3j9qQVBgw24gwYCX2WeKUD1gfjY2iEvIiIPnAy6viESa96GHiCLjuLpgZO-5zgu6XLV7rSKD3_iAF4MywaIq0iks94u7b5fuU5aC9AH5GZI0y-D-nBgdKTmUPKlEH7tb280lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیوارنگاره جدید میدون ونک:
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/147693" target="_blank">📅 14:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147692">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
رئیس‌جمهور لبنان به خبرگزاری فرانسه: ما به دنبال توافق امنیتی با اسرائیل هستیم که می‌تواند مقدمه‌ای برای توافق صلح باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147692" target="_blank">📅 13:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147691">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی مجلس:
به زودی اروپا باید منتظر پاسخ ما به ارسال پرونده هسته ای ایران به شواری امنیت باشد و عواقب آن را بپذیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/147691" target="_blank">📅 13:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147690">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
وزیر رفاه: برای مردم عزیزمون کالابرگ رو حداقل ۳۰۰ هزارتومن زیاد میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/147690" target="_blank">📅 13:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147689">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
رو دلار و طلا سرمایه گذاری کردید؟
آره
✔️
نه
❌</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/147689" target="_blank">📅 13:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147688">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
دبیر کمیسیون فرهنگی: شادمهر عقیلی اگر برگردد و در چارچوب اخلاقی نباشد، با او برخورد می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/147688" target="_blank">📅 13:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147687">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
پیش‌بینی بارش‌های پاییزی فراتر از نرمال در کشور
🔴
رئیس سازمان هواشناسی: نقشه‌های پیش‌بینی نشان می‌دهد بارش‌های کشور در پاییز فراتر از نرمال خواهد بود و این وضعیت تا حدودی در اوایل زمستان نیز ادامه دارد.
🔴
هرچه به فصل زمستان نزدیک‌تر شویم، سیگنال بارش‌های فراتر از نرمال در نقشه‌های پیش‌بینی کمرنگ‌تر می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/147687" target="_blank">📅 13:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147686">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: بزرگ ترین حمله را نتانیاهو تدارک دیده است
🔴
۴۰ هزار بمب و ۲۰ هزار کلاهک جنگی: تسلیحاتی که دولت ترامپ در قالب یک قرارداد عظیم در اختیار اسرائیل قرار خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/147686" target="_blank">📅 13:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147685">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
زلنسکی: روسیه دو بار تلاش کرد هواپیمای من را هدف قرار دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/147685" target="_blank">📅 12:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147684">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmIwMaU-eknVkXrCTSrKVCgQaqx6qVtfDLpf-WbWAkxV-XVlrUIlrdkdxVBdVxq0QfNLriPH49g2k8uE6MP2Lj6h5gAjg6Z-1rzGN38Eh_kEvGQyVCTFOmoXlS2K4C1-ktJnjlVdDHFpqOAi2qvRrPZX1LeU0OJ5acQr_t9bhsbSE6ZkABLTitQ8gTl-DiZzhok0cdvKwUKUIkFCtf2RheCEQyEgkihWahTCmcLX5eJKYqQOkd0SPU0c2NWNdWe7W3Hl8f8kxlOVPVx8FpwLiCnGXb6P5DsTdoWX0ORckI41bLczpFK6ZPFtuK2nWK4HxKMsHBRscg9BwkKJ1FgQ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای سازمان ملل متحد قرار بود در فرودگاه صنعا فرود بیاید، اما قبل از فرود، مسیر خود را تغییر داد و به فرودگاه بازگشت. این اتفاق همزمان با حضور یک هواپیمای سوخت‌رسانی سعودی در نزدیکی یمن رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/147684" target="_blank">📅 12:48 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147683">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20c0324d63.mp4?token=gIENMVFfun1_N_aRftt-BzRiYsMHlu5d-wyXfGNaD-ViMhFrdDjU33lanGeMuWs3_U39e-bPus_LoJyTAWjjTOdXNOJE-KQqRJNbzNNSNIyhaAd4_rZAAgkJzmLn9o9s8ApG7Z7eYEs9uUKSwTKldUJyQRPQlHds5rRRX6ngzLAZgr5kB6oFdnFLRf9C8py1TU8WMiC9o282r4DaFDa91--_fAIxsBkGTfbIm29WLx9bXybx9Xk4sAGOv93fPg4Z-oEiMJwQgYQcZxd_-M0zPePAwR0ZfibAIQ2pnjQ09UxU9o1yev2b5KbmPe1ecKIxAHa0vYxT7Xin0CGitIf16Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20c0324d63.mp4?token=gIENMVFfun1_N_aRftt-BzRiYsMHlu5d-wyXfGNaD-ViMhFrdDjU33lanGeMuWs3_U39e-bPus_LoJyTAWjjTOdXNOJE-KQqRJNbzNNSNIyhaAd4_rZAAgkJzmLn9o9s8ApG7Z7eYEs9uUKSwTKldUJyQRPQlHds5rRRX6ngzLAZgr5kB6oFdnFLRf9C8py1TU8WMiC9o282r4DaFDa91--_fAIxsBkGTfbIm29WLx9bXybx9Xk4sAGOv93fPg4Z-oEiMJwQgYQcZxd_-M0zPePAwR0ZfibAIQ2pnjQ09UxU9o1yev2b5KbmPe1ecKIxAHa0vYxT7Xin0CGitIf16Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موج تازه‌ی بازداشت بانوان توسط پایداریا در کابل
🔴
دست کم ۲۰ زن و دختر در کابل بازداشت شدند و  گروه خودخوانده طالبان از تشدید نظارت بر حجاب و موسیقی خبر می دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/147683" target="_blank">📅 12:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147682">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzzeogplRETTSSQVJBT_w-EIPbSS0zgi30_ydY2vPcVWyFizN0xwv3QVzFt753AMNjKQ8LbDr76_SJXJivemcClKezdaevhR8ZUYta8y7QBeW_PdJJN9-maxSzgchGnIicGEwQ4LUsB8ocJQZwn9O8NI0wVSazcygnM4EP99iTGvtoGi17l2g_3LeKAkUaHYrOIcxg-h9uCqDAWmz1rkAQJiLAWOxLgyTRns5OOnt44xQZCUpFkipvSR4nu8jNPNK3Cr24FhlvlRNcJZrIVfdzEeePxoyGYYFz8BN4DRR9QfTf9Ixw0jWeQ4w8fyJZhmY7Px4cGgm69KDcz4TIna6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
تخفیف فضایی تپسی‌فود
🔥
تا 50⁒ تخفیف ویژه رستوران‌ها
همین حالا غذات رو از تپسی‌فود بگیر
🔥
از اینجا سفارش بده
👇
https://tapsi.food/?utm_source=telegram&utm_medium=social&utm_campaign=fz0625
⚠️
مخصوص تهران و مشهد، کلیک کن
☝️</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/147682" target="_blank">📅 12:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147681">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a02cc6cfc9.mp4?token=jZ5SUTfw1Rjvx2GuGG9bns5wNQEpYi6IWFHCslftHR1UzhFX5VjHutNEozntCdFliq8MiSjO9TX3dcA3U1YW4EpeWByOVKw9Qw_53WtALNoln6WWmjEvkV3tfzIXBtigSwCxf0m_2RhzrjJvAcTpxifZXLiRpRinR8mY_nbcr-7fOzLlpTOFT-1biUUL10Z1wTxo17C1ap6nxBL-fEBd8exaFiBoheR0Olu8v8Otc07xcrU9JkQV9XpsMt3EplOJXQ7NJF0JDBUdtsJ2gt3DyJcDsLVA91x2FHRL4ZDGYPZQ10tG8grssk72ZDZweCacCAbxdZfFdQjcb5RaokBlBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a02cc6cfc9.mp4?token=jZ5SUTfw1Rjvx2GuGG9bns5wNQEpYi6IWFHCslftHR1UzhFX5VjHutNEozntCdFliq8MiSjO9TX3dcA3U1YW4EpeWByOVKw9Qw_53WtALNoln6WWmjEvkV3tfzIXBtigSwCxf0m_2RhzrjJvAcTpxifZXLiRpRinR8mY_nbcr-7fOzLlpTOFT-1biUUL10Z1wTxo17C1ap6nxBL-fEBd8exaFiBoheR0Olu8v8Otc07xcrU9JkQV9XpsMt3EplOJXQ7NJF0JDBUdtsJ2gt3DyJcDsLVA91x2FHRL4ZDGYPZQ10tG8grssk72ZDZweCacCAbxdZfFdQjcb5RaokBlBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هلی برن نیروهای ویژه اسرائیل روی سقف یک خانه در اطراف کرانه باختری
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/147681" target="_blank">📅 12:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147680">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
بلومبرگ: پاکستان در حال بررسی گزینه‌های خود در مورد یک نفتکش سرگردان در دریای سرخ در نزدیکی خط لوله شرق به غرب عربستان سعودی است و هشدار می‌دهد که هرگونه حمله به این کشتی به عنوان "عمل جنگی" تلقی خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/147680" target="_blank">📅 12:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147679">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سی‌ان‌ان : گزارش‌ها، چهارده ماهواره جاسوسی روسی چند روز قبل از حمله ایران، بر فراز یک پایگاه نظامی آمریکایی در عربستان سعودی پرواز کردند.
🔴
مقامات آمریکایی گفتند که اطلاعات جمع‌آوری‌شده ممکن است با ایران به اشتراک گذاشته شده باشد و این امر به انجام حمله دقیق، که شامل موشک‌ها و پهپادها بود و باعث زخمی شدن ۱۲ سرباز آمریکایی شد، کمک کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/147679" target="_blank">📅 12:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147678">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
تو سایت های شرط بندی احتمال حمله نظامی یا اتمی ترامپ به ایران تا قبل مهر ماه به 84% رسیده!
🔴
بالاترین عدد تو دو ماه اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/147678" target="_blank">📅 11:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147677">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سخنگوی ارتش پاکستان: توافق مکه روابط با ایران را تحت تأثیر قرار نمی‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/147677" target="_blank">📅 11:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147676">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5da33205e.mp4?token=dPDxRbvO6RFzj-g4MuNl-AcfqGR0iJeHxQMO5MZPILPdaKAJsSvv4f3kYLS63ySp5MhxvoRM8Pv7jxVZ9b7qZ-WlaBox720THDdP-dRmdSAY20FNG_eA-ZW0mCTPeLpc0RNBhqyZGfwRD9rxs3r0JbVioIlVQhK_3qGPawnBxdKSCZkwLzcC7R5qwBnFhDvbXWt_ncqt3ZW-I5-3ZqKuT8jtVF_YPWBKC_INoMjs10mrugo7OqUhmYi1zIDhXnwbOW09NBxt78uIOPX4XhcsAiTcas6EWILpcSithMcREWwDHkKievFHt8ms_jMSA1rhKRf1QX6dl4ogpZFcZ2W8_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5da33205e.mp4?token=dPDxRbvO6RFzj-g4MuNl-AcfqGR0iJeHxQMO5MZPILPdaKAJsSvv4f3kYLS63ySp5MhxvoRM8Pv7jxVZ9b7qZ-WlaBox720THDdP-dRmdSAY20FNG_eA-ZW0mCTPeLpc0RNBhqyZGfwRD9rxs3r0JbVioIlVQhK_3qGPawnBxdKSCZkwLzcC7R5qwBnFhDvbXWt_ncqt3ZW-I5-3ZqKuT8jtVF_YPWBKC_INoMjs10mrugo7OqUhmYi1zIDhXnwbOW09NBxt78uIOPX4XhcsAiTcas6EWILpcSithMcREWwDHkKievFHt8ms_jMSA1rhKRf1QX6dl4ogpZFcZ2W8_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
‏اعتصاب عمومی در سنندج و شماری دیگر از شهرهای استان کردستان بخاطر سالگرد جاویدنام مهسا امینی
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/147676" target="_blank">📅 11:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147675">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رو کدوم سرمایه گذاری میکنید؟</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/147675" target="_blank">📅 11:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147674">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
لحظه رهگیری موشک بالستیک حوثی‌ها توسط سامانه پاتریوت بر فراز مکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/147674" target="_blank">📅 11:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147673">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
یدیعوت آحارونوت: هواپیمای نتانیاهو از ترس اقدامات شهردار نیویورک، در فرودگاه جان اف کندی به زمین نخواهد نشست
🔴
مقامات امنیتی اسرائیل نگرانند که زهران ممدانی، در طول سفر نتانیاهو به سازمان ملل مشکلاتی برای او [اجرای حکم بازداشت] به وجود آورد؛ نیوآرک یا یک فرودگاه نظامی در نزدیکی نیویورک در حال بررسی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/147673" target="_blank">📅 11:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147672">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وزیر خارجه چین: از ایران و آمریکا می‌خواهیم به تفاهم اسلام‌آباد بازگردند و درباره مسائل باقی مانده، وارد رایزنی‌های جدی و اساسی شوند
🔴
طرف‌ها اقدامات مؤثری برای بازگشایی تنگه هرمز اتخاذ کنند
🔴
نمی‌خواهیم شاهد کشیده شدن تنش‌های منطقه‌ای به یمن و دریای سرخ باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/147672" target="_blank">📅 11:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147671">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
بلومبرگ: شرکت کشتیرانی ژاپنی: بازار LNG با اختلال طولانی مدت در تنگه هرمز روبرو است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/147671" target="_blank">📅 10:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147670">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به‌بزرگی ۳.۷ ریشتر در عمق ۱۰ کیلومتری، کنارتختهٔ فارس را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/147670" target="_blank">📅 10:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147669">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eccbab7fa2.mp4?token=oXna3LQUb6Ha6kuOa0cHUhaTtwJ6V3R_PKwvEwOUMZVC524bLQoVf8ACXFc6doPS-r-5-cPoP5XLff0QQotijEgnOkwhcXT1qU5jfixk9wuvDKayOVkm6X51S6iYhuV0oCC5qiGtsECIfo_bw4eDWeHV4wlJd7Cl8JzpRhMRgpETSvMXJX_l7S2N6kzL9vXl5fVFzn5x7gu6FwmKIaf0sJcrbF0sUcoMxYxzVlveyTBOhci16PQQHfJBMHu5qtZeCjm_9oPNEGzsBVycvLbBx5fIM13M1MpRwQdUGJ8GJ4ZnpzjB5DQk6nzEHqlvMWyUYudu1l_vGYFlg2ED87RGtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eccbab7fa2.mp4?token=oXna3LQUb6Ha6kuOa0cHUhaTtwJ6V3R_PKwvEwOUMZVC524bLQoVf8ACXFc6doPS-r-5-cPoP5XLff0QQotijEgnOkwhcXT1qU5jfixk9wuvDKayOVkm6X51S6iYhuV0oCC5qiGtsECIfo_bw4eDWeHV4wlJd7Cl8JzpRhMRgpETSvMXJX_l7S2N6kzL9vXl5fVFzn5x7gu6FwmKIaf0sJcrbF0sUcoMxYxzVlveyTBOhci16PQQHfJBMHu5qtZeCjm_9oPNEGzsBVycvLbBx5fIM13M1MpRwQdUGJ8GJ4ZnpzjB5DQk6nzEHqlvMWyUYudu1l_vGYFlg2ED87RGtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس: ترامپ تنها رئیس‌جمهور ۴۰ سال گذشته ست که حاضر بوده بگوید: «بله، نتانیاهو شریک خوبیه، اما من و نتانیاهو در این موضوع نظر متفاوتی داریم»
🔴
یا «نتانیاهو در این مورد اشتباه می‌کند» یا حتی«از دیدگاه اسرائیل، نتانیاهو در این مورد حق داشته ، اما مردم آمریکا چیز دیگری میخواهند.»...
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/147669" target="_blank">📅 10:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147668">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XSwNclDdWFgUJ6uHGP11UZAjQ9ogfWZF1BdEPzNcEyJt2wbUAd7P3UKDFfZzMLOYvi3UJuqim1RWlPIW2EBXn97Wu03nzKVAcXLu1ZhbcT5ua-dH7dd16FohwobNA2QEaY5cmrWCBbG2lYq7Pk-PJ5gP_UbCuXt9R41otrp6-mIye5bg5D2pqFswbQUMHpJELATm5YTRascz54MVvLu0nfXPLhraCHr8CbSMHTee6iHmBcCuqu6rKWfeZWGQScUxLZdW1Vhs_lCznCtFqTkfj6eY5C_BNmkceb2WgESkFtPZIfyAfyquyuE6XOSf53vCU1mcvr0AZxmAOyKPUkY1Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهباز شریف، نخست‌وزیر پاکستان: حمله پهپادی منتسب به حوثی‌ها علیه مکه را محکوم کرد و گفت مردم پاکستان از «این اقدام توهین‌آمیز» نگران و ناراحت هستند.
🔴
حوثی‌ها این حمله به مکه را رد کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/147668" target="_blank">📅 10:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147667">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ca794428.mp4?token=lEYMjGkJysTA8P77mHmVeFEUBozVxOE4Nt0-0JIY4qmg8BeR_WepG_agj_Wdj5l_1yduAbPqMAMDOmJx03ry4VYKBRjqMaWp9XkDPjXWpc5HE232VmxHpaj1slrV1QV0b24eDaldBwKUVZ6QgmNtuFXXTctDcFS6OHNqUC91CXig4aZRSBbjRl_RR6-c0VCWQXMGYZVvo0RJ5OWq1HsbQz8q34hLrNJurCC3jspcp9fJjh6qOAPBQa7DpM8ASaie6pAgG_GK0h_BLOG6NUnmcuFFgDmV8W9Fpl1Y_d1rHcho4Ft1gJG1clsN9qJzy3okdhx8kFCdA0e1omyKm4kUcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ca794428.mp4?token=lEYMjGkJysTA8P77mHmVeFEUBozVxOE4Nt0-0JIY4qmg8BeR_WepG_agj_Wdj5l_1yduAbPqMAMDOmJx03ry4VYKBRjqMaWp9XkDPjXWpc5HE232VmxHpaj1slrV1QV0b24eDaldBwKUVZ6QgmNtuFXXTctDcFS6OHNqUC91CXig4aZRSBbjRl_RR6-c0VCWQXMGYZVvo0RJ5OWq1HsbQz8q34hLrNJurCC3jspcp9fJjh6qOAPBQa7DpM8ASaie6pAgG_GK0h_BLOG6NUnmcuFFgDmV8W9Fpl1Y_d1rHcho4Ft1gJG1clsN9qJzy3okdhx8kFCdA0e1omyKm4kUcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه رهگیری موشک بالستیک حوثی‌ها توسط سامانه پاتریوت بر فراز مکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/147667" target="_blank">📅 10:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147666">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
جی دی ونس: اسرائیل در زمینه فناوری نظامی و تبادل اطلاعات، شریک مهمی برای آمریکا بوده است؛ اما در عین حال، ایالات متحده همیشه و در همه مسائل با اسرائیل هم‌نظر نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/147666" target="_blank">📅 10:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147665">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
افزایش ۶۰ درصدی ثروت ترامپ بعد از بازگشت به کاخ سفید.
🔴
نشریه "فوربس" گزارش داد که ثروت دونالد ترامپ از ابتدای دوره دوم ریاست جمهوری در آمریکا، به میزان ۲.۷ میلیارد دلار افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/147665" target="_blank">📅 10:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147664">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a47484293.mp4?token=rlN5ja8HMIPkADImueFEIwx2CTzJkx491lKuhh-wz5EBTE4k2DJJp1MCUFh1I8SPCfIUuWT5EOQE0D9F8f9PDSptokI8ORtnMt9GhbJzRsgBtf-fAoa7l7c1EhN_osOM2ERIZhRyO3TSwgTTK8lA10Uynf8p0eaQ1KgPj4HgL3wmw2Eq9Arcz_01Xl073Lzu9kx5jTF9lZWqKackG09In66fwwEgI_BWdU4xRYuK-AB1rMn5Wt833NAOz5Ey-ZY6jUQWtFET4Xp66JoNGUxIZeqfF5LJSOYhd7D9IKsv69dOQ-1tkefHxIxLPNvMjIt1XGmoBLhNPcJik-OZo_p_LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a47484293.mp4?token=rlN5ja8HMIPkADImueFEIwx2CTzJkx491lKuhh-wz5EBTE4k2DJJp1MCUFh1I8SPCfIUuWT5EOQE0D9F8f9PDSptokI8ORtnMt9GhbJzRsgBtf-fAoa7l7c1EhN_osOM2ERIZhRyO3TSwgTTK8lA10Uynf8p0eaQ1KgPj4HgL3wmw2Eq9Arcz_01Xl073Lzu9kx5jTF9lZWqKackG09In66fwwEgI_BWdU4xRYuK-AB1rMn5Wt833NAOz5Ey-ZY6jUQWtFET4Xp66JoNGUxIZeqfF5LJSOYhd7D9IKsv69dOQ-1tkefHxIxLPNvMjIt1XGmoBLhNPcJik-OZo_p_LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس: «حتی اگر در همه مسائل با ما موافق نباشید، طرف مقابل درگیر دیوانگی شده است.
🔴
آنها تحت تأثیر افرادی هستند که می‌خواهند همه‌چیز را از دیگران بگیرند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/147664" target="_blank">📅 10:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147663">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/220ab7f29d.mp4?token=Rpu6EkD8an3dYpJWjnXaZjN4vXI8izvzfuRg1hvOoFc8_Im_n2dCiRUxl-WrG6Vb9oQKmCmWqMVEdg40cT7iA0DdvC9mKtD_9e6WdnMIC3VuWYSadNajtcGqDfz3iJErwTI1RSrfKtbFk99HsY02hHlZQqvF-M-RJvoBg11HoTKGi_sOy7dewWvbEMBxZWrqlpl3SIgwAIxJvIpoR-VDnBVm85zcLvnkbXdsJ4dOYwDJ8q0IjrWrgJ9O1Df3koJf4seSdc8T1qaUkdZma4XarzV3DRsqVnkdHCSXpaq8BGE-apKXl7i1fClaN1uy5bnag9dBhRK7Tynuta462gmthQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/220ab7f29d.mp4?token=Rpu6EkD8an3dYpJWjnXaZjN4vXI8izvzfuRg1hvOoFc8_Im_n2dCiRUxl-WrG6Vb9oQKmCmWqMVEdg40cT7iA0DdvC9mKtD_9e6WdnMIC3VuWYSadNajtcGqDfz3iJErwTI1RSrfKtbFk99HsY02hHlZQqvF-M-RJvoBg11HoTKGi_sOy7dewWvbEMBxZWrqlpl3SIgwAIxJvIpoR-VDnBVm85zcLvnkbXdsJ4dOYwDJ8q0IjrWrgJ9O1Df3koJf4seSdc8T1qaUkdZma4XarzV3DRsqVnkdHCSXpaq8BGE-apKXl7i1fClaN1uy5bnag9dBhRK7Tynuta462gmthQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس: خروج آمریکا از معادلات خاورمیانه می‌تواند به بحران جهانی انرژی منجر شود
🔴
جی‌دی ونس درباره ایران گفت: «اگر آمریکا عملاً به خاورمیانه بگوید که از این پس خودتان باید از پس مسائل برآیید، تا زمانی که ایران به حمله به کشتی‌ها ادامه دهد، نتیجه آن ناگزیر یک بحران جهانی انرژی خواهد بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/147663" target="_blank">📅 10:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147662">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
صدراعظم آلمان: ایران فورا تنگه هرمز و حوثی ها فورا باب المندب را باز کند؛ ایران باید برنامه هسته‌ای خود را متوقف کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/147662" target="_blank">📅 09:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147661">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AoOHbuUHPGDyZMG9zVpBZkotl0fqO3bWKDih8RAt88uoPTNJUORu7GICWieymi2zHEyjB8gIC634fidwqdCpFUjp87XX0FkTLiMiDTCK7dWheZVxJNd_-lt-O9mHI40inLkhnp6KtiVmFVA5SPmpkfwF6FTDkZE7Q1mF186_J99H1f0IolLgC23S_7zLGR5zrjoKS6XI4ejghiyeT-suvLWJcUgQsbdiRhMA9vZxYeKUq3Y7NASixG6XSm8PJP06SRZH3zvPbo_gRoSXpDNS0X3rFFXApQJ8R7n_4nT2HkbV31K_FNXOKCCijKijPl31ssTG7JRJw68XhtIRKRtEuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لهستان
:
در واکنش به حملات جاری روسیه به اوکراین، جنگنده‌های خود را در حریم هوایی نزدیک به مرز اوکراین به پرواز درآورده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/147661" target="_blank">📅 09:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147660">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e663b6aabb.mp4?token=hQL7bNR9hERoF2_G4-3awjny8GPAKXTASk4gFO0aMyFxOWM9xZp3KsXa-lhSfZHqtuFn5X-c4gDtyvzpNw0z-4J8fVWJGnFU0MsQUlxMO-jj113kmp1DGcK3ZQ_NvJqVb_ANFufTCAewir8PfEPQ8Tr8Nd68nWY6HeUyNAmH9FnrgcjnzNW1kMEpfEt0ogWz4oyPzmm6GUQr9fJb_nllJNFU188PAlw7jm1ADDZ3N5MTrAQ4pM6018RE0Y1_NJ856ymbb1jec_HSvoY085GckS2X2DjBEoo9ZWaBz883_lZ_IQ459FDoeDyHVxmcy6cZB2u99bbKZLZYsRtPmn81SYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e663b6aabb.mp4?token=hQL7bNR9hERoF2_G4-3awjny8GPAKXTASk4gFO0aMyFxOWM9xZp3KsXa-lhSfZHqtuFn5X-c4gDtyvzpNw0z-4J8fVWJGnFU0MsQUlxMO-jj113kmp1DGcK3ZQ_NvJqVb_ANFufTCAewir8PfEPQ8Tr8Nd68nWY6HeUyNAmH9FnrgcjnzNW1kMEpfEt0ogWz4oyPzmm6GUQr9fJb_nllJNFU188PAlw7jm1ADDZ3N5MTrAQ4pM6018RE0Y1_NJ856ymbb1jec_HSvoY085GckS2X2DjBEoo9ZWaBz883_lZ_IQ459FDoeDyHVxmcy6cZB2u99bbKZLZYsRtPmn81SYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس: «ما نمی‌توانیم اجازه دهیم سیاست خارجی آمریکا در خاورمیانه تابع دولت اسرائیل باشد.
🔴
ما زمانی که با دیگران توافق داشته باشیم، با آنها همکاری خواهیم کرد و زمانی که اختلاف داشته باشیم، با آنها مخالفت خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/147660" target="_blank">📅 09:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147659">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
یحیی فست: اف-۱۵ سعودی را در آسمان مأرب سرنگون کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/147659" target="_blank">📅 09:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147658">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
سخنگوی ارتش پاکستان: روابط برادرانه ما با ایران، عاملی تعیین کننده در موفقیت روند میانجی‌گری بین تهران و واشنگتن محسوب می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/147658" target="_blank">📅 09:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147657">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
یحیی فست: اف-۱۵ سعودی را در آسمان مأرب سرنگون کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/147657" target="_blank">📅 09:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147656">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fd5bb0a95.mp4?token=fjK07gvLb-zE9wMp_iceLvep1AsQZIe9yZTCySeyyCf89xHrhmsahK0tUE67Z4maESECAdKorCGeI_9JVKpBJYRyqIhrlpAhuuEJ5CqP40AxR7HirVkW16JAcEwgzHhjiXw3n_OqbWd_NlS6L14ZvV4Vdo2DBDbCLClEg-X-t_8_5WRUfADr2lxmca30JPPGS_al2JFiAusmQsaKuCuswku3L8KCym6nnynzin9pC75KulJnI2WLN7BUN83VMiI4U2TlZjTHocgo3Mri5DEHg8WeY0XeVhkVfLR0EaTXlY7Q2M2mq3gCYgA-8GkZQkuFMQTWRSPoNWVSpcDKy8FvFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fd5bb0a95.mp4?token=fjK07gvLb-zE9wMp_iceLvep1AsQZIe9yZTCySeyyCf89xHrhmsahK0tUE67Z4maESECAdKorCGeI_9JVKpBJYRyqIhrlpAhuuEJ5CqP40AxR7HirVkW16JAcEwgzHhjiXw3n_OqbWd_NlS6L14ZvV4Vdo2DBDbCLClEg-X-t_8_5WRUfADr2lxmca30JPPGS_al2JFiAusmQsaKuCuswku3L8KCym6nnynzin9pC75KulJnI2WLN7BUN83VMiI4U2TlZjTHocgo3Mri5DEHg8WeY0XeVhkVfLR0EaTXlY7Q2M2mq3gCYgA-8GkZQkuFMQTWRSPoNWVSpcDKy8FvFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برنی سندرز درباره هوش مصنوعی: احتمال خطر هوش مصنوعی احتمالاً بیشتر از سلاح‌های هسته‌ای است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/147656" target="_blank">📅 09:09 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147655">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K09FTr4ZOhE-N7u0E6hbqGYe-FucvjdTjqIge29CqdACyaSTXKqWWzMVrFPypaMM9pRVu-TAjZ2qUJXgILRAkuQ1GTv65oG_qRBo9lYPjtmIEkeOU8iV4u9GZ5b9oVkV9t9AQrgxkIwWK_cOwY94lxE1-Pds9JRjssCgck59m8dduNvN1TIH7_d5JrYvwgU4nNkVQuNuHU4dkzn0SkzbUQ1n3vlGOaP3xi2Sp1ekgWC9ox529Mwowje5RMN1ZGUfBIuXwMaTjtd6jiuw_231FHuMa3uD5FTIdcDpU6bewF92P-VUbeQZYapsCEQWnMAUr_YNnqLbMIYJdGOFrJLN9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت آمریکا:توصیه می‌شود که سفر به عربستان سعودی مورد بازنگری قرار گیرد، زیرا خطر هدف قرار گرفتن منافع آمریکایی توسط پهپادها و موشک‌های ایرانی وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/147655" target="_blank">📅 09:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147654">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54e6dfc0ba.mp4?token=qRV7dCUlaaOA0nOdYbF6TSt0WbqJru3gfpr_QoxLKE6cs31bxoZ3fC7nc_mYB1OaFC9h13L9fXR_q8Jo2I54Fezemw2LJj6oZ_uAgGJaRc-Gjtyo2r0Kh2WIQynjJLzeiHnzc1NEu0a1h4CaqXU10phS3uL-rrSfWTTQX7gh9zy0yaingoznjR7_NiC4XYXCTtjPlAKfo-YtYGtqPjmC1enXPvkSCXr_6-9ig0x65tlK8ShhGjHQDstIMmYdIBysSFoHFiEjNF0uwlXgZ8E-ndzb2O-4xIU9vMk5C2lZtR_keKb_XIMzuljOSKWX9A8YjzDAFCPMbmV8RI16KPF0bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54e6dfc0ba.mp4?token=qRV7dCUlaaOA0nOdYbF6TSt0WbqJru3gfpr_QoxLKE6cs31bxoZ3fC7nc_mYB1OaFC9h13L9fXR_q8Jo2I54Fezemw2LJj6oZ_uAgGJaRc-Gjtyo2r0Kh2WIQynjJLzeiHnzc1NEu0a1h4CaqXU10phS3uL-rrSfWTTQX7gh9zy0yaingoznjR7_NiC4XYXCTtjPlAKfo-YtYGtqPjmC1enXPvkSCXr_6-9ig0x65tlK8ShhGjHQDstIMmYdIBysSFoHFiEjNF0uwlXgZ8E-ndzb2O-4xIU9vMk5C2lZtR_keKb_XIMzuljOSKWX9A8YjzDAFCPMbmV8RI16KPF0bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی در سفر به پکن با وانگ یی، همتای چینی خود دیدار و رایزنی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/147654" target="_blank">📅 09:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147653">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b7b36ce4e.mp4?token=P9O5KF3Q861Gx_hUcCZIyHmtIBLe2QL_i0JOItcWB7geesjtto0s68_xJZCJ4yHIopsaanP9wuJK9VWGgZ88rZKXwPl2G7CQJ8X5ThRz5bKIpF_N0zbqF9iVKd3eLd7wM5vJxc2HGOeNWlYQDUBqL7ja-l1gzzLbFRN-LHe9Waq694VSRzegjr6dFw8WqMjI4ar8LR-cq9l8CqjiCrT6-J4gPN9ZWlT83Vj6GdnXVNNT60_VANWRHqE3gGlfmnK1ZP7f8HToIhtzgPOIjfszU8CW5bpWvYlIZPELGeDJa3yw5jJq45uehNUo_B7BmnCwSuVcSeDkqFP23fnx9vMg7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b7b36ce4e.mp4?token=P9O5KF3Q861Gx_hUcCZIyHmtIBLe2QL_i0JOItcWB7geesjtto0s68_xJZCJ4yHIopsaanP9wuJK9VWGgZ88rZKXwPl2G7CQJ8X5ThRz5bKIpF_N0zbqF9iVKd3eLd7wM5vJxc2HGOeNWlYQDUBqL7ja-l1gzzLbFRN-LHe9Waq694VSRzegjr6dFw8WqMjI4ar8LR-cq9l8CqjiCrT6-J4gPN9ZWlT83Vj6GdnXVNNT60_VANWRHqE3gGlfmnK1ZP7f8HToIhtzgPOIjfszU8CW5bpWvYlIZPELGeDJa3yw5jJq45uehNUo_B7BmnCwSuVcSeDkqFP23fnx9vMg7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقوط مرگبار بالگرد خبری آمریکا هنگام پوشش تصادف
🔴
در پی سقوط یک بالگرد خبری شبکه «ان‌بی‌سی لس‌آنجلس» هنگام پوشش صحنه یک تصادف مرگبار میان یک خودروی شاسی‌بلند و اتوبوس، ۳ نفر جان خود را از دست دادند و یک نفر دیگر زخمی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/147653" target="_blank">📅 08:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147652">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
گرجستان پرواز شرکت‌های هواپیمایی ایرانی را متوقف می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/147652" target="_blank">📅 08:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147651">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
سپاه: بامداد امروز پنجاه و دومین پهپاد MQ-9 ارتش آمریکا را در جزیره قشم زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/147651" target="_blank">📅 08:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147650">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وزیر خارجه چین: ادامه درگیری بین واشنگتن و تهران به نفع هیچ‌کس نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/147650" target="_blank">📅 08:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147648">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
در حرکتی بسیار عجیب دادگستری هرمزگان پلاک ۱۶۳ خودرویی که بیش از یک بار در یک روز سوختگیری کردن رو به عنوان خودروی متخلف منتشر کرد و اعلام کرد از این به بعد هر خودرویی بیش از یک بار در طول روز سوختگیری کنه متخلف به حساب میاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/147648" target="_blank">📅 08:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147647">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
۵ فروند هواپیمای سوخت‌رسان آمریکایی در نزدیکی تنگه هرمز در حال پرواز هستند و فعالیت هواپیماهای ترابری بین پایگاه‌های آمریکا در اروپا و خاورمیانه نیز افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/alonews/147647" target="_blank">📅 02:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147646">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fbd3251f05.mp4?token=I-D_aXYFV4kvu7zJ0t6lEnuoLZUAP7BYx8qhygElL3rx3fkkKw5fMuZPZIfyC9WmgALfBE19VgKaZ8nd4r0jr2yK4sZVGGgwXVn4BabC-UvElCSmKvfdMS3FRrxvA2XMKEhiK4_6oIF8p35adqIiZad-09HKHNHHljEC7HCNG1bzlW_CBisD66cHrdJjU4-Uc6M3SuRZ2vf3S9VdbVRKOfQOVYY5aH5o3RmtHUdJRH13XYTxTI-zLzk4o88vnQ2rWs8Ev-8MBpEQuq9jzi68-ga0FNUHq67xYjYwqSKqEosI8wghfFxqduZVQZUaefORtScsBRUpk3xq0XYNPyvhtw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fbd3251f05.mp4?token=I-D_aXYFV4kvu7zJ0t6lEnuoLZUAP7BYx8qhygElL3rx3fkkKw5fMuZPZIfyC9WmgALfBE19VgKaZ8nd4r0jr2yK4sZVGGgwXVn4BabC-UvElCSmKvfdMS3FRrxvA2XMKEhiK4_6oIF8p35adqIiZad-09HKHNHHljEC7HCNG1bzlW_CBisD66cHrdJjU4-Uc6M3SuRZ2vf3S9VdbVRKOfQOVYY5aH5o3RmtHUdJRH13XYTxTI-zLzk4o88vnQ2rWs8Ev-8MBpEQuq9jzi68-ga0FNUHq67xYjYwqSKqEosI8wghfFxqduZVQZUaefORtScsBRUpk3xq0XYNPyvhtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب عادل فردوسی پور از پوریا پورعلی بازیکن پرسپولیس سوال کرد که میدونی چطوری مهدی زارع تو حموم پاشو بُرید؟
پورعلی برگشت گفت آره بابا، من با مهدی زارع، دوتایی باهم رفته بودیم زیر دوش
🏳‍🌈
عادلم هر کاری کرد نتونست جلو خودشو بگیره و ۳۰ ثانیه فقط خندید
🤣
@AloSport</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/alonews/147646" target="_blank">📅 02:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147645">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوری/درگیری‌ موشکی در نزدیکی تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/alonews/147645" target="_blank">📅 01:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147644">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">در عجبم عرزشی‌ها طلاهاشون میدن تا خونه‌های لبنانی‌ها ساخته بشه اما وقتی میگیم همون پولو بدید تو سیستان و بلوچستان خونه بسازیم میگن وظیفه دولته!  [@AloTweet]</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/alonews/147644" target="_blank">📅 01:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147643">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQ4REF5-tDLL38OQwR0MGRhe8kBYFQdlDr5lcYQ449wYL7LkNFr0Jas1vOLc5rK4_ET3Dt4Ti003DM0PtyjUKwG3TgjbHrV0mXI8yrBozKOOfsV9f4flWBe2RjLplTTkdLhIdmsNpaH3c9dr_fN_FV_Q2VfmuGvp6jy1xPBZ2srUdSn_1dReAHbUyR5rTvx6hUOyCSgkkUQwVuRZ9P3Wk_sphKiCOaM93HO0_OROav2bWB5ZnGppRSiM_anRGucN0s6dTtr5jZw-Oh8K33tDNB-gehe8sWbaE_8mb139XhRAiBHnEytJpsl0xYYfvEUzn6RF6gZEpbG3ZGCK8wlfsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجلس نمایندگان آمریکا با رأی ۲۳۲ به ۱۴۷ و ۴۷ رأی «حاضر»، طرحی برای آغاز روند استیضاح دونالد ترامپ را کنار گذاشت؛ بنابراین این طرح پیش از رسیدن به رأی‌گیری درباره خودِ استیضاح، عملاً متوقف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/alonews/147643" target="_blank">📅 01:30 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
