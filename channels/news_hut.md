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
<img src="https://cdn4.telesco.pe/file/BC-mhdXhf2ejNninwu1tvFgBvD0nsx_gHeooRZ-GCUq-b51D7xteGBusRQoY7NZ-GAm1uVS_tvZlD19jremcmI5C_cmgv8BjGMaglf2e9jGWS3Uo8MR-x0sGxXmShgmBqrpj5feCFKiYYwnKWUwHLCt27MoEOJbnlkgPm_0rlEO9uQUsY6fu_XmRzXtSlurxkgjE1YpqprBtgXcjO3M_XiFh0gHuwV3QnIwZuwcB7QMP-AToBqPLAug2GetDhNEgelrT3r6PAAw9c6f3FfWhB0kx-x2IgeZgKRMeuTjAu75S25oFFXsxnRbLOwZ4XexJZrA5-QK6kuGEgumxy_ktuQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 149K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 23:36:33</div>
<hr>

<div class="tg-post" id="msg-68996">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=EqniXM4m6OMvdVX7nYhd37oSTOtnhjylTQz6K0iXvzlVTVz2QFVAjtZX-WAl79IaswW6c4iGHePJCKMSozZnk7xkFTz--Fkuoa4jVj3Leodf23bFlQsfY3F8idnhHcEikkTycY3HPsW95z_Obdx21euLYZFC6XpJKxSR58UX2MQICBYggEtOw2GTyCT2bhfymbctoyFFUGdFzl_v_B-Xkaqn0PZ8Mg62FnJAOfih4fm5SV3RLjohUktBNWtWJBQeGxRGIGKatOr6oFvekW-FoS7_FrAZLgyKS_CJvYxPzKc6AYAKJV9tS79B6xhtE3ZBX_L2Yl3oIGS8ma8InFjC2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=EqniXM4m6OMvdVX7nYhd37oSTOtnhjylTQz6K0iXvzlVTVz2QFVAjtZX-WAl79IaswW6c4iGHePJCKMSozZnk7xkFTz--Fkuoa4jVj3Leodf23bFlQsfY3F8idnhHcEikkTycY3HPsW95z_Obdx21euLYZFC6XpJKxSR58UX2MQICBYggEtOw2GTyCT2bhfymbctoyFFUGdFzl_v_B-Xkaqn0PZ8Mg62FnJAOfih4fm5SV3RLjohUktBNWtWJBQeGxRGIGKatOr6oFvekW-FoS7_FrAZLgyKS_CJvYxPzKc6AYAKJV9tS79B6xhtE3ZBX_L2Yl3oIGS8ma8InFjC2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیروزمند:
تا کی قراره ایشون ( مجتبی خامنه‌ای) بیرون نیاد؟
🎙
مجری:
تا نابودی کامل عوامل جنگ.
⏺
پیروزمند:
خب اینطوری شاید ده سال دیگه طول کشید خب ما تا کی اماممونو نبینیم؟ اینطوری همیشه در موضع ضعف میمونیم.
@News_Hut</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/news_hut/68996" target="_blank">📅 22:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68995">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1C3-VgQcfcryqgOkebK_uQ365IIOulvJo-pLPGzmcngvq6gxp1Ex58Hfgta2j1xmSjLUHa_-E09v8344vGZhO2k5rDxbCwPLHG7lJ7aQqNZXYElPU-Lk0YA9GcJYyq8xMmN39iGmoEnE_tsIO1flK473XF3cPR-jqEERP3r7f2RaPP1-JejBJXklxqXGIa5eWLkMzzhJo9J9AE3xkElaN__iOA4Viec5x0uGRWfqGTP-JE8awT5hpXZ7pBrRUmpZdETrcqSmTZGuaJn13x6uWxiA-F_5SoeVuAp3SMnBSHp0lxNf4_LbSi39qte2zIazTLnqamE5MYVlB9VbEnb9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در گفتگوی تلفنی با شبکه فرانسوی «ال‌سی‌آی» (LCI):
اگر «صددرصدِ آنچه را می‌خواهیم به دست نیاوریم»، «قطعاً» گزینه ازسرگیری جنگ تمام‌عیار علیه ایران را مد نظر دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/68995" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68994">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUc1DqU0SAG3Uh48ed3v2uA0KRGQPwuHqVSNTxRri1oMwOgi8CNC6Ys20fKWryVrVCt1JGDJc2eXDvxQB3CiOIn5_qmiArDnVI0o3uN3db95SDRnjv0V_J3aO9B18yltNBgTNsz6syH56RvvFsmmWZiSJtZNTFAj5QhNdDPpZ9AN86vurG6ELLncSPKVcs8iy_sMabdUuSgjzeDQqvj79Pd5WO0hkhKkDu3w02m65vozczk0xQs4vay7TtG85eK3iI43-Gfx1fkzGmR1z1jWuy9ATegvdJPqZXEpzTl-xFu0TTVVk0gO4IyLsfmG1xvCBfHjRSuwsdzjJtOOwz3pOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:
رئیس جمهور ترامپ روز جمعه به ارتش ایالات متحده دستور داد حملات به ایران را متوقف کند و به تقریباً دو هفته حملات روزانه پایان داد.
این تصمیم در حالی گرفته شد که مقامات عمانی در تهران مذاکراتی داشتند و گزارش‌ها حاکی از پیشرفت در جهت توافق احتمالی برای بازگشایی تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/68994" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68992">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NT066vbXZVvUEEXkVWveOlNR1CjcIztnenLL73Jx_5aqK9L1rwJNA1QcvH6n-l5hugcFT1gwlAwM1I3pb_6RxXJaKr1IVErss292kWz2MBzw74qPDH3k2M7srEgKixJxCsiKQGbVkp65zkJQJUChV6Ri62ULHgC3oRoFJxPro0v2XCGp8ljK0hSCVRk04HUVmM_xiVPLaELvWEO7AD1wO5MQ6K50ER3wEuuUL6I9DzygDTR8AK6ZPhgQ0vQN__E51A7jn8pqF6BC11cZGpAeRhSBDKUbgAtq0hmtLHUEr9bM9TKGo449D0cQuXa0oYuWa8xxHoMQWLP2nB7eCi055Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=fV0cqwTaJGmTCtq7WR-KbgLmXp9cGNPn-TLr7L_PXnekZvkMT4T4tsrFPFxNhFBrOzS7MdrKJiE9sYnXMCf-M9rI_XY5zTS9lz6ofB0GfB9AxRldAp1Y1_NvkcTfB4Ytye8y8rlw3NKdTs1xe5M91oatpCLIW8pb_XoZUKDkRDHmJ_Gu3Q1-DbuQ2xK_K8vY59JkCb5iEiVAXpEE9uaZnzSRycuDqxZwMEbCEvRAMXsha3t7YmVgCHtRHKDjefLEIKCohjxEAKCzhArLvVwQeZq5PmlRENHRpBL-Uc3q7G0dCVB0BqxqazTdqwEVyFyA6h1QblotuwrzQ3_dyRbVww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=fV0cqwTaJGmTCtq7WR-KbgLmXp9cGNPn-TLr7L_PXnekZvkMT4T4tsrFPFxNhFBrOzS7MdrKJiE9sYnXMCf-M9rI_XY5zTS9lz6ofB0GfB9AxRldAp1Y1_NvkcTfB4Ytye8y8rlw3NKdTs1xe5M91oatpCLIW8pb_XoZUKDkRDHmJ_Gu3Q1-DbuQ2xK_K8vY59JkCb5iEiVAXpEE9uaZnzSRycuDqxZwMEbCEvRAMXsha3t7YmVgCHtRHKDjefLEIKCohjxEAKCzhArLvVwQeZq5PmlRENHRpBL-Uc3q7G0dCVB0BqxqazTdqwEVyFyA6h1QblotuwrzQ3_dyRbVww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ساعاتی پیش یک هواپیمای آمریکایی در فرودگاه جده فرود آمده است. به نظر می‌رسد این هواپیما یک هواپیمای آواکس مدل E-3Sentryباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/68992" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68991">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxxS86Te4H1EutF0Ly8bwwYyp-gHoOPdqka1mKR9IAfq0gVvtFtqW6J_0Kp-4zMyLlhRvZRs1mZcvBYm-l1-rgSKq5UGs0FhZ30MDxSq_tYG9H1c7AIWSZkjiMltjhdZy8hbgt3m1bAmll1QOC_lhQ9dEZ04UdeX00IUM10sxUQX-CwioiIcTrNXSUsflvDcHPwcS0pVtgH-UaH7cx2xgxJFk_7EowM00WSpNi5d7fygb-D5YguuYtKTYcFA0pYqCXNwA915GM-ue0o80mb6zDh-LGMFOOGKdIVbgLzXk-Mi5h0pZwFsAs-Jweui1kEaZoVc9f_XXdrBnHXMr-KJjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
باراک راوید، اکسیوس:
آمریکایی‌ها دیروز برای عملیاتی گسترده‌تر در ایران آماده نشده بودند، بلکه برای حمله‌ای تدارک دیده بودند که از نظر وسعت، مشابه حملاتی بود که هر شب در طول دو هفتهٔ گذشته انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/68991" target="_blank">📅 19:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68987">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4bab692977.mp4?token=aIetjiKWkgaC8-jnSBmbD-Tq_rdUPveNXTafUpyJQ2foNQbD1wtgeMbx-p8n_W881ZfSMTSiUe_gMUlvTaPGnTltUQuUx4VCcz_6aLscxjLjgo9pf8QB2f8pFgHNgy6u3nQIoCUI_sBmPEBhGKdjz75yX_bqdZlhVzWgHJ4izCU3_moP8yVGZ0wlh64yyG56KGD9jBjt9jvoHWFX5FvM4Tbw0pWsyaQVPCm_i2JkGU2JAObisqmiq94jc2prRoSKrdj-AYM4niQ6v160jXbYxEHY7eQt27JMGpBta_GETS9XstgxJdbFKQvHdEyBIqu5Rv3U6lJkFQCHUyDe7NL3Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4bab692977.mp4?token=aIetjiKWkgaC8-jnSBmbD-Tq_rdUPveNXTafUpyJQ2foNQbD1wtgeMbx-p8n_W881ZfSMTSiUe_gMUlvTaPGnTltUQuUx4VCcz_6aLscxjLjgo9pf8QB2f8pFgHNgy6u3nQIoCUI_sBmPEBhGKdjz75yX_bqdZlhVzWgHJ4izCU3_moP8yVGZ0wlh64yyG56KGD9jBjt9jvoHWFX5FvM4Tbw0pWsyaQVPCm_i2JkGU2JAObisqmiq94jc2prRoSKrdj-AYM4niQ6v160jXbYxEHY7eQt27JMGpBta_GETS9XstgxJdbFKQvHdEyBIqu5Rv3U6lJkFQCHUyDe7NL3Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلنج شکن معروف اینستاگرام که هر چی داف بود میاورد پیش خودش و نالشون رو درمیاورد دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/68987" target="_blank">📅 19:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68986">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=PZv80O7blq0JmBQMBCnU0HAXoPp3RHXUsUgVEdNA7CJczfchTEXaFbeDnXCy425Bqf9Dd6U_5XjPJ1LPjdi8Ys49ANHPUPkjE557hmYpouIlAoblTv9pV4yKngbxkAp3I2uew26RwFex3GykuWfIEhaynI1IFjj4u4btYJBPBmvrw8hFczgpoR3yvqBOdtpSNal8BmOTOuHMtZf8JqLQCGjvPcT477oykHMKR-Oe06UFkU1Hr5ewiIvvoVms3xJfsPn0O_bBR-GBkA3Yn-gXqypIp62ZvgLD4ArVraySfVMJc_iVaKCUlQJQYnwqv-HTo0h4UKsfOTj2I1qKzfFiaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=PZv80O7blq0JmBQMBCnU0HAXoPp3RHXUsUgVEdNA7CJczfchTEXaFbeDnXCy425Bqf9Dd6U_5XjPJ1LPjdi8Ys49ANHPUPkjE557hmYpouIlAoblTv9pV4yKngbxkAp3I2uew26RwFex3GykuWfIEhaynI1IFjj4u4btYJBPBmvrw8hFczgpoR3yvqBOdtpSNal8BmOTOuHMtZf8JqLQCGjvPcT477oykHMKR-Oe06UFkU1Hr5ewiIvvoVms3xJfsPn0O_bBR-GBkA3Yn-gXqypIp62ZvgLD4ArVraySfVMJc_iVaKCUlQJQYnwqv-HTo0h4UKsfOTj2I1qKzfFiaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تیم‌شی‌هی سناتور آمریکایی:
جمهوری اسلامی گروهی افراطی و تروریست هست که 47ساله کشور رو تصرف کرده و ایدئولوژی نفرت انگیز خودش رو گسترش میده.
این رژیم اهمیتی به سیاست های حزبی یا اینکه به چه کسی رای داده‌اید نمیدهد.
آنها میخواهد همه ما را بکشند.
ما این جنگ را شروع نکردیم، اما تمامش خواهیم کرد.
حملات موشکی پراکنده به کشتی ها یا تحرک قایق ها در تنگه‌هرمز نشانه قدرت نظامی نیست بلکه دست‌و‌پا زدن یک حکومت در حال سقوط است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/68986" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68985">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSh0BmAI8gCgZd5aEPST_cvNOcTmi6Za82EDj4YQqcn1easmc7RPhbnzmSFe_ZeRnCOpBhQm27OPP7JXKFckTHBOsAk5i_jj31LvWhBVcnm_DiN52fFbDlXcn0f0GLgRYcMeiYpq9JeVHdiNMyzv4rjbTz2FDXo_afAIQ3o6aEDJN5QdnddwnJMJExQlSag8udZsA3avOYFM7m9fdl0dyPpZB5yQwpRTE8MHWzOzpu3KNj-acpX3jfidwTs7yXyemTEeWbOc_cc7XwBKVh7MiVUqthZ_Mfnltzpb2sSKpxNQPkrViDlcee9alSlq_uOPT5JtIARiMa2lMPDnmB9_TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
وای‌نت:اسرائیل انتظار داشت که ترامپ دیشب ایران را بمباران کند، اما در نهایت از اقدام علیه تهران صرف‌نظر کرد.
اسرائیل روز گذشته را در حالت آماده‌باش برای یک حمله بزرگ آمریکایی سپری کرد و انتظار وقوع آن را در طول شب داشت؛ اما سپس متوجه شد که ترامپ در حال عقب‌نشینی و دادن فرصتی دیگر به تهران است.
قطر و عمان فشارهای سنگینی بر ایران وارد کرده بودند تا پیش از وقوع حمله‌ای که تقریباً قطعی به نظر می‌رسید، کوتاه بیاید. برای نخستین بار طی ۱۳ شب گذشته، ایالات متحده هیچ‌گونه حمله‌ای گزارش نکرد.
یک منبع اسرائیلی وضعیت را این‌گونه توصیف کرد: ترامپ تمایلی به حمله ندارد و تنها به این دلیل به سمت آن متمایل شده که احساس می‌کند دیگر گزینه‌ای پیش رو ندارد.
ارزیابی اسرائیل تغییری نکرده است: احتمال دستیابی به توافقی واقعی صفر است و تهران تنها موفق شده برای خود زمان بخرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68985" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68984">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=AtdxHqrf877s56EwzUUnAMCYKIv7_7FDFDcpZNy8mdixRFPir92PFuE57vRKH5tzup55zkEqXvihyqABRiXr00sRJpL2OzBlaQ4BfHrvAokehEtoduMygaL2ht_hx0cgwUP9kN5SqGQGVuuKQ3WcyBE0zhgK0byGC_fOhHO_XLJGeU9eMlGvrTzFqODrFRptbZAXo25d0o6AAntjj-gRJY12EPYxfEtFIt4Ua1vLK3op2axI8wrbVUtVr8MLarJYcbRyVrArqBcD4N-A7yyYl3xLdq9hJaLYPRq0Yvcw-jn6q7bd-KY1LbhT18hMeO1g2z0u98inCgoIO8SUt_G6ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=AtdxHqrf877s56EwzUUnAMCYKIv7_7FDFDcpZNy8mdixRFPir92PFuE57vRKH5tzup55zkEqXvihyqABRiXr00sRJpL2OzBlaQ4BfHrvAokehEtoduMygaL2ht_hx0cgwUP9kN5SqGQGVuuKQ3WcyBE0zhgK0byGC_fOhHO_XLJGeU9eMlGvrTzFqODrFRptbZAXo25d0o6AAntjj-gRJY12EPYxfEtFIt4Ua1vLK3op2axI8wrbVUtVr8MLarJYcbRyVrArqBcD4N-A7yyYl3xLdq9hJaLYPRq0Yvcw-jn6q7bd-KY1LbhT18hMeO1g2z0u98inCgoIO8SUt_G6ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فارس با انتشار این ویدیو:
مردم جاسک، اسلحه‌ به‌ دست منتظر اومدنِ نیروهای آمریکایی هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/68984" target="_blank">📅 17:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68983">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=X752QPq-qz4qweM4B4DrJG152XOPG3Y9aJQDc0fZWx7RneZJ_epGNZ1T1IaVgvYQS3zHekseaweXNicD2FCBtRzmna2SU9kRvxPm1UAdlC-3h5FZIxGHtcTgwuZezUZcqevsIpN7eZpDDelG9CKpECv5vmRRpXiD_AEwbC5ayAXmKiL8XgEPqmWeVQLP0RqJYDlcNJQndgeYbMB0maiYnjtaAsonsDlu_tBVw7F3sTHcCyUAsCB6ABr_qu4FhdzBxHdYDpb3Pg77DS8VuYq4S7QO7MQChfYPz05379J3iehgyyqtydjTBxrw3OlS8k2se54opPLxIOiUmqQC3nhHaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=X752QPq-qz4qweM4B4DrJG152XOPG3Y9aJQDc0fZWx7RneZJ_epGNZ1T1IaVgvYQS3zHekseaweXNicD2FCBtRzmna2SU9kRvxPm1UAdlC-3h5FZIxGHtcTgwuZezUZcqevsIpN7eZpDDelG9CKpECv5vmRRpXiD_AEwbC5ayAXmKiL8XgEPqmWeVQLP0RqJYDlcNJQndgeYbMB0maiYnjtaAsonsDlu_tBVw7F3sTHcCyUAsCB6ABr_qu4FhdzBxHdYDpb3Pg77DS8VuYq4S7QO7MQChfYPz05379J3iehgyyqtydjTBxrw3OlS8k2se54opPLxIOiUmqQC3nhHaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از طرفداران حکومت، با انتشار این کلیپ آمادگی خودشو جهت
مبارزه زمینی
با آمریکایی‌ها به رخ کشید
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68983" target="_blank">📅 16:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68982">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⏺
🇾🇪
بیانیه نیروهای حوثی:
در پاسخ به تجاوز آشکار و جنایتکارانه عربستان سعودی، نیروهای مسلح یمن دو عملیات نظامی دقیق و موفقیت‌آمیز انجام دادند. عملیات نخست، با استفاده از ده‌ها فروند موشک بالستیک و پهپاد، تأسیسات حساس شرکت آرامکو در جیزان را هدف قرار داد.
عملیات دوم نیز با بهره‌گیری از تعدادی موشک بالستیک و کروز و همچنین پهپاد، تأسیسات حساس شرکت آرامکو در ینبع را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68982" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68981">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=A4i_UImjuSp181oxlxaqRUVpZdAQogr9s9ko9fPAg2WWkr_PWtsbkD1uOqAYFCUplvEJ8VtgO62_dOad4SMiFHotMrz-gRsJgwGY0nMAIS6Ijkjyet_gTqiHOPvVbwAqgWQSg2Gs3CuPXnNFqYQmG-wbdDioaaW6-cBe0s3mDZnjKJ7MfOdfssXgwdQRwXh4UEGrdtnm1TudjW2GLgDE3EnoEBWlm3wLhKnOPg2TkiHz4JhCWJCK_yNczuf_3xtWBfdkw19A5V1fod_V0aRRXiYQlW0imKTiTYAa903M0DrQKIRbuEJfMvMUeCBLxD9Z3PvCKzYVRsgeZMzx0nQsOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=A4i_UImjuSp181oxlxaqRUVpZdAQogr9s9ko9fPAg2WWkr_PWtsbkD1uOqAYFCUplvEJ8VtgO62_dOad4SMiFHotMrz-gRsJgwGY0nMAIS6Ijkjyet_gTqiHOPvVbwAqgWQSg2Gs3CuPXnNFqYQmG-wbdDioaaW6-cBe0s3mDZnjKJ7MfOdfssXgwdQRwXh4UEGrdtnm1TudjW2GLgDE3EnoEBWlm3wLhKnOPg2TkiHz4JhCWJCK_yNczuf_3xtWBfdkw19A5V1fod_V0aRRXiYQlW0imKTiTYAa903M0DrQKIRbuEJfMvMUeCBLxD9Z3PvCKzYVRsgeZMzx0nQsOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبتای دیروز پزشکیان که تا به بحث مذاکرات رسید صداوسیما سانسورش کرد:
بعد از جنگ 12 روزه، علی خامنه‌ای رسما اعلام کرد که ما دیگه با آمریکا گفتگو نمیکنیم و صداسیما هم اعلام کرد.
یه روز رفتم پیش علی خامنه‌ای و گفتم خودتون گفتید نه جنگ - نه صلح، حالا ما چکار کنیم؟ گفتش که برید مذاکره کنید و ما به دستور علی خامنه‌ای گفتگو با آمریکا رو شروع کردیم.
تو آخرین پیامش هم گفتش که برید مشکل رو حل کنید چون تو حالتِ نه جنگ - نه صلح نمیشه کاری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68981" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68980">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=fJbFRZFCCgYNwIRWjjhlHCr4kSu9UH7fEXbZE5G0wK5cmW3ukOZej7PkdStqlDdZdUKK6m4QkdWTwr3GcyHP5mg90iQWq10SWQ0FevDtcPR21ARorOjtPV9ob8HJt3xE7S3IjXN-GMk3bzwHamBPbb3ZCdsaza5Nh6GNnoKXCN7I5-mC1gaXv8-4RrwmB33mdSL13i4lhJ6XF2M0sBh6RvqG_tKRcCY0UYGjROrgpD1VtozQf3x97qf2kGrzCdZZzEJ2LXFhF63JBGGYPrGwhDrEc8uAfEAVGgirw_88-3aI1y8uePMdX7hXbCqGnH74LUs6UM--ETYZ-GaLziXSug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=fJbFRZFCCgYNwIRWjjhlHCr4kSu9UH7fEXbZE5G0wK5cmW3ukOZej7PkdStqlDdZdUKK6m4QkdWTwr3GcyHP5mg90iQWq10SWQ0FevDtcPR21ARorOjtPV9ob8HJt3xE7S3IjXN-GMk3bzwHamBPbb3ZCdsaza5Nh6GNnoKXCN7I5-mC1gaXv8-4RrwmB33mdSL13i4lhJ6XF2M0sBh6RvqG_tKRcCY0UYGjROrgpD1VtozQf3x97qf2kGrzCdZZzEJ2LXFhF63JBGGYPrGwhDrEc8uAfEAVGgirw_88-3aI1y8uePMdX7hXbCqGnH74LUs6UM--ETYZ-GaLziXSug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروهی از طرفدارهای حکومت با مقوا عکس رهبران ارشد نظام درست کردن و اومدن تو خیابون
😳
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68980" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68979">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=MHnevhGAXkWupFc21c9wSAQtHC8R_eqLaK45ptVQ5PwV1nu0cICrIAWD0U_92ALZr8k8VBvgdLv23a27lal0C4h2WHsMsOPQwDM1OkvBwza63aJmgNnAb_RU9sYh4rtD9m48JlMVkRDswjufV6v8KL_ELow-dtJ4YXOxpILwzq_zTSCxJAmtZi0EafgU2YwGJlcGqwg3efdTRM9ZSVEnDon_4GFU60TC4VR4Ylu_jr1cc4xCCCk4suYbmmcdBs8k6sWhwaaQKZdDBOzLgibQJq_dKDAunKVXUTRpVsQZIVzxvQKYjI5O1_m-lRaq3Wzd-u2VC4JJx1feqaovx0stjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=MHnevhGAXkWupFc21c9wSAQtHC8R_eqLaK45ptVQ5PwV1nu0cICrIAWD0U_92ALZr8k8VBvgdLv23a27lal0C4h2WHsMsOPQwDM1OkvBwza63aJmgNnAb_RU9sYh4rtD9m48JlMVkRDswjufV6v8KL_ELow-dtJ4YXOxpILwzq_zTSCxJAmtZi0EafgU2YwGJlcGqwg3efdTRM9ZSVEnDon_4GFU60TC4VR4Ylu_jr1cc4xCCCk4suYbmmcdBs8k6sWhwaaQKZdDBOzLgibQJq_dKDAunKVXUTRpVsQZIVzxvQKYjI5O1_m-lRaq3Wzd-u2VC4JJx1feqaovx0stjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تغییر قیمت یا سهمیه بنزین قطعی است.ما علاقه‌مند به افزایش قیمت هستیم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68979" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68978">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlaHPhx4-xCMeKVcpbu59G1NJ3OklrZv48iCBFj9Mf_i6BznpNgJX_hQyyUR-wq4rrx6qq1ebRPLm0IeXHeeXYvrAw6UMjF0zsfgls2MHhFtABSQZ-tyXHvKpj4AVU44rOnv8W-kzOaKBELt4LcbHciMWgJKEqGk6Ifb7us2ukizxFfDqDSWlnKnMGOqI9iuUALs1h-q7g8OpyiqC_G1XCzTtJMavgYnI0dbehOERq3veXJ5eTmTe8zIyhNh7sj5a9I2RCaEBC5ri3pLDo_ojF0zSL83ZmM_e456Udpc3kCWdeRGRM_7d-9c3Xh-vPeE9SCSuTzd8egwMv3gZjw5fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
در پی حوادث تنگه هرمز، طی مذاکرات سوئیس تصمیم گرفتیم برای جلوگیری از سوءتفاهم‌ها، یک خط ارتباطی مستقیم ایجاد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68978" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68977">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=phHuMXE_dxpNg2ViGJ1xbpbRGeqdbdgEKFBxI9tYbZqQAKG7Bt9RN37QHn-ZxEv2WikYVBEalUITjaf8h3--Br6hU8J1ezmfG5fNAB8PuPkuCKLWn7Ja_Wauk9e_Y8vNIXUqbCmMGB-_nqXp4XFnQ2iiVwIKD0Vk3NhqvhMdDqSkXRHqqkymVe6BbMp5dTq5hBR51sxRxPf5JhZlfQUUCcUVKnGPYKror8h4ho3IQvDDmDvnbBNgYn5t67IIBVVZYBEdd9sbLTUc5yhwnlwGrZf9W25QXhY0E9FS8zWF2n5bmb-Zg3FBs59LzDHXrq6029_4zSSYPADI9aOaLHSVLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=phHuMXE_dxpNg2ViGJ1xbpbRGeqdbdgEKFBxI9tYbZqQAKG7Bt9RN37QHn-ZxEv2WikYVBEalUITjaf8h3--Br6hU8J1ezmfG5fNAB8PuPkuCKLWn7Ja_Wauk9e_Y8vNIXUqbCmMGB-_nqXp4XFnQ2iiVwIKD0Vk3NhqvhMdDqSkXRHqqkymVe6BbMp5dTq5hBR51sxRxPf5JhZlfQUUCcUVKnGPYKror8h4ho3IQvDDmDvnbBNgYn5t67IIBVVZYBEdd9sbLTUc5yhwnlwGrZf9W25QXhY0E9FS8zWF2n5bmb-Zg3FBs59LzDHXrq6029_4zSSYPADI9aOaLHSVLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حمله موشکی حوثی های یمن به پالایشگاه جازان شرکت آرامکو
عربستان
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68977" target="_blank">📅 12:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68976">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvGz0K7XpgvaQxFRyCyWXWQ3UDmF4h2gMS8A1As14glMxi16DFJt6PIRBq07ue1q3VjRslbu2mlMxi7ekco8ErKa36ZqnY_TN9OXJkfPs-3sYr6dttFrR4GgD-EJDpWnXvoSVQAP1RCEyoFH3Uml-QaipD0ZxUXvLaTBXKpG_jyWQlMuceOvFrdxYVzYdJaWKg4Lt5AHxCXLx1YqC4cf3Xr8BGrgll2QIWAckzpbGZ66V6MRJeAYCU3NshkCzFB0Hi0saPb_TtZ884Gd2il1a9vKkIMNB9QqBAp8-J4MYj-Mcz-3V0lM1ctisfPr3fcS4NDlwpY1pnId4X-CVltUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
سازمان عملیات تجارت دریایی بریتانیا گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68976" target="_blank">📅 12:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68975">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=bmC2q_r9iy6MgP0ZnQOUUwtZwrn-TMIV-TOiUovlLoSqu6w25SbqEl9VusRpqMLRCgyoqvsFTMMascGkKXyrz3aTWB0WAfZkpRZQA_1IS-JGZDkI2k6C0-MGNl2JNkZhEVAXoosnjBq9aH9pkfZWLP_R6M6fqBHBmJt0CzrMOZ4W5aWzG9kaz6SVSk3r2AShSO2VOzckQLtqRi0were9ZBeVgQBds9eRE_8dbyqu3XIhb2R_dTWL1HF9qlwnrrz8VGXaeTEuyGj-K7EE3PLTHaz4kLQ0FyD8WB6YhKo2Bi4gFsgkjJ1LYQXhiXR0KJYYukwQmq9Q53iT-MlYE_AA3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=bmC2q_r9iy6MgP0ZnQOUUwtZwrn-TMIV-TOiUovlLoSqu6w25SbqEl9VusRpqMLRCgyoqvsFTMMascGkKXyrz3aTWB0WAfZkpRZQA_1IS-JGZDkI2k6C0-MGNl2JNkZhEVAXoosnjBq9aH9pkfZWLP_R6M6fqBHBmJt0CzrMOZ4W5aWzG9kaz6SVSk3r2AShSO2VOzckQLtqRi0were9ZBeVgQBds9eRE_8dbyqu3XIhb2R_dTWL1HF9qlwnrrz8VGXaeTEuyGj-K7EE3PLTHaz4kLQ0FyD8WB6YhKo2Bi4gFsgkjJ1LYQXhiXR0KJYYukwQmq9Q53iT-MlYE_AA3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
مجتبی خامنه ای چندماهه رهبر شده ولی حتی کسی صداشم نشنیده. اون حتی به مراسم تشییع پدرش نیومد. خیلیا هم معتقد هستن که اون مرده. نظر تو چیه؟
🇮🇱
نتانیاهو:
حرفات درسته ولی طبق ارزیابی ما اون زنده هست
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68975" target="_blank">📅 11:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68974">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">💢
ویدیو وایرال شده، پشم‌ریزون از گات تلنت
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68974" target="_blank">📅 11:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68973">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=R5UYwch4VIC1YoaGXjWulgJSCRQz-ZG2QzE30W9VZzHyOGwIZAwNmA3OasBwzT9QP1aH41mWiMJ3ZheLlHIpN7qfK6bambDq3E2wKplMuaBv9sTVpGk4GTIiRAIQRUER8_EOatxKMofha6ADtxZGkkmJU2yUz4FW43K7rrcO2qvN9gAzJLs9ON6g6_rZktovwtmfEBDOxcs4l377-mnmQAeF8BEVliGpuQvm4zRpHkeTvjSHjdl-_3LunyUIZg1vRYnzYQgyEiCRpdYc8XQ0KXBlC6SioFE2iqQaXcTb8rZVc1TJ4r7R16FIScgGsvjL2_CckT2NSMK7icGiu7VTtzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=R5UYwch4VIC1YoaGXjWulgJSCRQz-ZG2QzE30W9VZzHyOGwIZAwNmA3OasBwzT9QP1aH41mWiMJ3ZheLlHIpN7qfK6bambDq3E2wKplMuaBv9sTVpGk4GTIiRAIQRUER8_EOatxKMofha6ADtxZGkkmJU2yUz4FW43K7rrcO2qvN9gAzJLs9ON6g6_rZktovwtmfEBDOxcs4l377-mnmQAeF8BEVliGpuQvm4zRpHkeTvjSHjdl-_3LunyUIZg1vRYnzYQgyEiCRpdYc8XQ0KXBlC6SioFE2iqQaXcTb8rZVc1TJ4r7R16FIScgGsvjL2_CckT2NSMK7icGiu7VTtzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از یک تحلیلگر سیاسی که زمان پهلوی هم بوده:
یه نفر نشسته بود تو کاباره داشت ویسکی میخورد.
طرف کی بود ؟ قصاب بود !
به بغل دستیش میگه ما ک اینجا نشستیم داریم ویسکی میخوریم بعد تو ببین اون بالاسری های فلان فلان شده چه کیفی میکنن و چه بساطی دارن پس.
اینطوری ناراضی بودن مردم از پهلوی!
مردم رو اینطوری ناراضی کرده بودن روشنفکرا.
بهشون گفته بودن میدونید شما خیلی بالاتر از اینها هستید.
انقلاب رو روستایی ها نکردن انقلاب رو روشنفکرا و دانشگاهی ها کردن بعد اولین ضربه رو هم خودشون خوردن.
به مردم گفتن عاای شما وضع اقتصادیتون خیلی بهتر از اینا باید باشه ببینید اون سرمایه دارها چیا دارن که این همه خورد خوراک به شما رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68973" target="_blank">📅 10:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68972">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=k5nQmV7xVx5XmF_7OxUqHSAdTncaiYMpSU2gClH1VDVX-JIu6D8TrzYNah4O3A1qOS0PQQxJhROzcKL1gbgWIEnXvXyljZSXaD99u11C8EcECviDUa9RvXrLV6HjeU6NCYVr9EIvMEQYc5sw7MdgLdFpAE0Q9k0A8AOFSGNVVAmDYW3Hdc181o97b7mhW_W9G3ggpCbavpMUNj-jrjm_tutMK4SLlLSqzfWa18D-wj_pzBzJtmSW_3CT8-1jAP5iomeKNUnIlNWZekS47xhsRCJ2-iEX4p7gUBg0ke7Hue1ZbwKV9xbXi49xIu5Ij73JbdrpZeG77Q7uUB_SutoTfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=k5nQmV7xVx5XmF_7OxUqHSAdTncaiYMpSU2gClH1VDVX-JIu6D8TrzYNah4O3A1qOS0PQQxJhROzcKL1gbgWIEnXvXyljZSXaD99u11C8EcECviDUa9RvXrLV6HjeU6NCYVr9EIvMEQYc5sw7MdgLdFpAE0Q9k0A8AOFSGNVVAmDYW3Hdc181o97b7mhW_W9G3ggpCbavpMUNj-jrjm_tutMK4SLlLSqzfWa18D-wj_pzBzJtmSW_3CT8-1jAP5iomeKNUnIlNWZekS47xhsRCJ2-iEX4p7gUBg0ke7Hue1ZbwKV9xbXi49xIu5Ij73JbdrpZeG77Q7uUB_SutoTfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره رهبری ایران:
«حالا که همه اهالی رسانه اینجا یک‌جا جمع هستند، باید بگویم که ما به دستاوردهای فوق‌العاده‌ای رسیده‌ایم که رسانه‌ها هرگز درباره‌شان حرفی نمی‌زنند؛
برای مثال، در دوران دولت من، رژیمی که زمانی قدرتمند و هراس‌انگیز بود و بی‌وقفه به آمریکا حمله می‌کرد، سرانجام سرنگون شد
رهبران پیشین آن کنار زده شدند
و اکنون توسط یک دیکتاتور گی(همجنسگرا)اداره می‌شود که با اختلافات داخلی دست‌به‌گریبان است.
با این حال، من شخصاً برای باری وایس در شبکه CBS آرزوی موفقیت دارم. او زن فوق‌العاده‌ای است.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68972" target="_blank">📅 09:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68971">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=dGul8_zm9P7mDRfv5tIXlmPz3AqC_XLEb3TeSiiqsS5siiSfnW3JKkoQ8fKNlDt8sHOm-OlpMzA5lJTkcGd-ht4zbqB9BvuWYGbQ2FUb_Wjmx09Sradjmh8mngEyasVfHmslZBQkXeumIeqLG2IYGcqNlMWmcR7_y90mD0p8u2ao7VoeFzwFBGANfbJ9cZ2wvHfW2H4q2R2Ej3vCUhS9wXJj2x4SCQs5bhUV3-a-FcXs6yJPknNsGkXwa9g0ciXCdrFufv8rA1rzuhLwQr7WD5lVQ5VLpsSiB159jpB_PUy8arqdHY-e3b6xHuWpfqN-sLGPk8LPk9o5jC2KLgvvRGM_eYUAUhjayR1sRNi3buijnbWLRvlJHNLfMGH0uRIJZL17KczhPa_EK9AMujOXChRFL3dhKDZqy_JTK-Ad3TIVTAsphYtI50otOb9gr4Y5ZQPtyEHLXwyeR1hdq1oRXA0uVsoZ3lk7azPwqkoQJKtqHw6TCluQLNSTL_mgrDmPKUfqlIfysplDgT15iKDkLLOqSWqVB3ofRTJLd0kUCSOacHduXOxw3iLA8KkOzPUuyrZb5UjimTOUjf9bADtR7-XlDbDWzwbP9JnWbFNygnQ6Warf7wD6lAVV_QHL3Zo_cGZrpZFkcQiWvfm0FjfHL4mmZLKuS64tIlp1o7RmqQE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=dGul8_zm9P7mDRfv5tIXlmPz3AqC_XLEb3TeSiiqsS5siiSfnW3JKkoQ8fKNlDt8sHOm-OlpMzA5lJTkcGd-ht4zbqB9BvuWYGbQ2FUb_Wjmx09Sradjmh8mngEyasVfHmslZBQkXeumIeqLG2IYGcqNlMWmcR7_y90mD0p8u2ao7VoeFzwFBGANfbJ9cZ2wvHfW2H4q2R2Ej3vCUhS9wXJj2x4SCQs5bhUV3-a-FcXs6yJPknNsGkXwa9g0ciXCdrFufv8rA1rzuhLwQr7WD5lVQ5VLpsSiB159jpB_PUy8arqdHY-e3b6xHuWpfqN-sLGPk8LPk9o5jC2KLgvvRGM_eYUAUhjayR1sRNi3buijnbWLRvlJHNLfMGH0uRIJZL17KczhPa_EK9AMujOXChRFL3dhKDZqy_JTK-Ad3TIVTAsphYtI50otOb9gr4Y5ZQPtyEHLXwyeR1hdq1oRXA0uVsoZ3lk7azPwqkoQJKtqHw6TCluQLNSTL_mgrDmPKUfqlIfysplDgT15iKDkLLOqSWqVB3ofRTJLd0kUCSOacHduXOxw3iLA8KkOzPUuyrZb5UjimTOUjf9bADtR7-XlDbDWzwbP9JnWbFNygnQ6Warf7wD6lAVV_QHL3Zo_cGZrpZFkcQiWvfm0FjfHL4mmZLKuS64tIlp1o7RmqQE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بررسی اهداف احتمالی حملات آمریکا توسط فاکس نیوز زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68971" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68970">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بعد از سیزده شب، امشب جنوب آرومه و خبری از انفجار نیست، و متاسفانه این آرامش، ترسناک تره!
#hjAly‌</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68970" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68969">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfDvVr27cUJdvy4PpQ1fOk1coq49l0JfQqbOznOUWBhIMfi1D8q_3c8qdAVmCC06Y3RP9OO-xd55CmeQp5O_T3jOcslpwrX8JSstQTDer6JRE-3drbQ7V89MMdxAGmpHSMy_an31_rSHzpaaCTdxGqI3KAppLG0PfNJ3F2yOOAjiiB1FvwGFT86MHDlJ4P4WJrmhrk33zT7h5D5MIJ1Emx2nDLYMlXdEClaz4gvpGtyUc7p3cus6LSQ0FaykhWiVaSeUIW28NUbZZCrxP84l4hPAmCgJlI-zXudpLJYoBwON3HS6F-5ckxTKeWYn5NDyysfw1cxpyZwKcBdzHw9i_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه فایتوکس به نقل از مقامات اروپایی:
در اروپا این اجماع رو به افزایش است که ترامپ پیش از کاهش تنش، آن را تشدید خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68969" target="_blank">📅 03:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68968">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=jOGRppIpxGHTtgyaI2Xb97WJ7UjNU_jT4sCDHIvAWMvqW7doO798JvcLErADCMpgGe-xVCLvah1yYCfpcdp4SWBF0HC4GHW_bHQ3DkH48Z4UAJcZl-ldtoUtdHZeW412FDkqHYOplaotK-seXfCEPYT3JyKoGmyNZO1R9-OBR8yMqN11JfM7isZvYHz05OH7LGCeMieyjzIzt0YPr1zyKdg5CpQ8MIYfEYaluI6FOKvcHCFVlenQy91KKsFJ-x3fZ2KG0ps8hsmnlu_r93KnEMVakSO3MGX_-XMhq4Ee9xvI2l0FktJypD4XzMPwWTolhMSQQtnHy_nS5laI_LzQIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=jOGRppIpxGHTtgyaI2Xb97WJ7UjNU_jT4sCDHIvAWMvqW7doO798JvcLErADCMpgGe-xVCLvah1yYCfpcdp4SWBF0HC4GHW_bHQ3DkH48Z4UAJcZl-ldtoUtdHZeW412FDkqHYOplaotK-seXfCEPYT3JyKoGmyNZO1R9-OBR8yMqN11JfM7isZvYHz05OH7LGCeMieyjzIzt0YPr1zyKdg5CpQ8MIYfEYaluI6FOKvcHCFVlenQy91KKsFJ-x3fZ2KG0ps8hsmnlu_r93KnEMVakSO3MGX_-XMhq4Ee9xvI2l0FktJypD4XzMPwWTolhMSQQtnHy_nS5laI_LzQIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پدافند هوایی روسیه یک پهپاد اوکراینی را بر فراز انبار «وایلدبریز» در سن‌پترزبورگ سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68968" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68967">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByKFsJ6Q-fA7hXFjU7Pl1pYC76xlG-Gx6DrkMt0Jbh-agmNetaK29RUqZ74I1nt0IDgNPRpcVnR5o__3kq5YS2TBjevLyexPDTqQhDxjargNIwZEqlbg2zRxdCf4EWaC5OMoYDoIBhxyJed2SC9cTZmETJCmJVtFy8ofRN9Oo9aCglsEgNkdGhA7NCjQzh8X17cebgv-lsJzYHkferD1NVt8u6MIta2h9c7WUxVTaIfPeoJFsnODd7MbL708Hd-TCEzFGOQ4aIHvHdHgZtV2sSS8gml57SrtWXFza4bszGlt2DdlGj9oKAEKEXoW-L1JS0g1z2A9BCokKqYyYBxcEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ارتش‌آمریکا: یک‌کشتی مرتبط با ایران که سعی در نقض محاصره دریایی داشت رو منهدم کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68967" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68966">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITai6oi1kBPTJwLRTBmVhDhrzaCsgGuuGETgwvhB_bPj3X1hhx4cclQNoQgI5JT3mDPDCr_aPA8to3usd1oWivcPkNxuu3UhStyqSOw3IYq2shU7wRNQpE5Gmkybs5Li8Dtf969kL845DOXguaXY3DORo0J5zVxyqXq3mRzeKzxrnVS-Bc3wjNBr2P4ciMjgVZTuz8aeKTIACq8hwfNgYhSAFnOCc9rjuMxhT5xsjxes_zC4jEHy8Kiwh1iWkdE4jT2vRfZyzQQItKvyDxStQ8aavKLmBSO1ftk95nM0nmCurzDY0WlZPg7Zb4RBi7bQ6JysG5z_tkbEGcFG9IVNbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68966" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68965">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJKxgxibXg70LARwbarUj0dDgiAs7rwg-F9J2h5bkV4-lXItYYiQdnR__VdCvcP1Y0jtOz4dZfIsOQgVdFCqmJ09V5yuKc2AzdF8DrSTvtHDIZzG7YwKczNrMwTxRrqWNDy6EWlb7sYe3MXnvbaHDQC2oiUBXDlkG5FQLstAaNo__4oG4t4Sly4dS761OXzYDTrbDe6zveJiZcRBnfsjwz1fy53f8vWsrbCFgIlVTyJBMAhKwR0iFJnvgUdKaG64E1KqMgqvDBHhNdBIUfGI0Bs_SLGeptouY3M7i4XMPhOdP4bHl3LBD3julC8pS2GLHmXCwuFUo8UOvyj-jeKQNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
رکوردهایی که ترامپ تو این مدت تو مصاحبه‌هاش ثبت کرده؛
«ما ایران رو شکست دادیم.» - 106 بار
«ما ایران رو نابود کردیم.» - 95 بار
«توافق با ایران نزدیکه.» - 88 بار
«تنگه هرمز بازه.» - 75 بار
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68965" target="_blank">📅 00:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68964">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uC7L3U5zI-jD1EzEcMZJWIeMpCVhA8VGtlC-3jzofa2YQhKmENm7kKs5oW0lvXSS_etbheR8d7NRdxM6hLU_suyvDcHqzhfTMapCEkucU8bvNmzZDf6dpjqy60Y7nthh_bec9trMmQLYZbbxLZndCIbfaIncn-upl7bWv7W8KlPmLtUoDrh7vSEqY9-y8PrQgReWgNgFRNQ4q8pOIKDr_cNGTVw1TGAoYNGlU8FkmHMYCWaS3XHIdKTEurO5d-v3QCUwrLxsZR11lYz5utegw73X4tZH1Q66Ori6k9ONsauhpDdOUHAE5Mib7LBRssZmT0wv7mz61FCTtM6zDMuDJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
عربستان دقایقی پیش به بندر حدیده یمن حمله کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68964" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68963">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🎙
خبرنگار:
آیا شما در حال بررسی یک حمله گسترده به ایران هستید؟
🔴
🇺🇸
پرزیدنت ترامپ:
"ما آماده حمله هستیم. ما کاملا مسلح و آماده حمله هستیم. ما با آنها صحبت می‌کنیم. شاید یک نقطه عطف وجود داشته باشد یا نباشد... در حال حاضر، ما به طور جدی با آنها صحبت می‌کنیم. اما به نظر نمی‌رسد که بتوانند به آنجا برسند، شاید اکنون بتوانند."
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68963" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68962">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68962" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68958">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FHCO1Yw4pf2TfM_c93Of5akgJu3KJfxMW7Au7mBnZiyD775DszbCl6Dj8HOfeB_D8_c2N3QlKgwxScW_O0lbvF-zA86UfZPHUdWJc9eETXOteC7_RDEdv1BtSsecvBLMoVWMgzsG9EQNdxdd4x1kiil9rNrDvD4au2biOWkQ1M-KDDcRBfYoal0CWoXRhgfugLySPDu3gSB7N3C0WzF6nVfwLzHQiaoEZnFd2HjMhiUB8VUdoVAEJGs6LlZzSfHbu0VVEACI9kHqxOB8LQwwYx9mzkVhAMXZlOftyx_4pVpl7gdLcpWh6FJiROfsWJs6pB2xAe-yv5cJDrzoeN3DCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LcV_Uf-efJhiRMogwXdwYNrm0GvZUZp4Vr-ylniYbYOAh25CQo5xJAR2K37EXE8lLR1dsUvKt5op6o9azTxTj_vOyyc9R5r9jbGNDDgtUkJLm-t0BjqL6Pe9TxU9zZFc6gJCz04IEVo94ltNR_L2jkbGGk5jsy1FI5yu9anKTHsE20DJgUJh2JPX4H298TwrfrT3iV55dWmrXfYvRGYVjoy2N02PLcEUBhGZYR59C7rErJJ77t37Q1nVIb72q_ivKpeK_jNO7SXdELaIm3NKvO9Lb1VCxg7BTUUFtW36_9XuR2E0Gbhse_hIuaMmgj-z0YE00FrXYxvtiTmfCfQ3Bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=KkaYCevb9UETcApnXehWVAR4BnRch8KMTcHR1VYz59yjMUyw96jY4U8Z9xQOa-HUFEaqqjOSMFyhxYXDmC5uqsfAUp0O45t2y9ZWkUEUQsIUPVPB0B_yfzcpx8FMPuzq1pu5nGwGSM00w3Uz7V3H5gkNE86ZvKijvGUGSjsYDpqzpulQXL8O1B5a_WrYWl4FB6o95PaJ6u5jzM3hcuOqQhGgnXsdGrq15RJdUFsPWVt_1m-FeT00HQq-cKbd_ZEyL4NXEs6pcIWxzB_JCm5_ODlft6373ZwTfTKpdXrxRsbYHuieGEaGRrnPbAAG47MUleTy9ioAk9JLCAKp175YmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=KkaYCevb9UETcApnXehWVAR4BnRch8KMTcHR1VYz59yjMUyw96jY4U8Z9xQOa-HUFEaqqjOSMFyhxYXDmC5uqsfAUp0O45t2y9ZWkUEUQsIUPVPB0B_yfzcpx8FMPuzq1pu5nGwGSM00w3Uz7V3H5gkNE86ZvKijvGUGSjsYDpqzpulQXL8O1B5a_WrYWl4FB6o95PaJ6u5jzM3hcuOqQhGgnXsdGrq15RJdUFsPWVt_1m-FeT00HQq-cKbd_ZEyL4NXEs6pcIWxzB_JCm5_ODlft6373ZwTfTKpdXrxRsbYHuieGEaGRrnPbAAG47MUleTy9ioAk9JLCAKp175YmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
❌
🇷🇺
یک حمله دیگر با استفاده از پهپادهای اوکراینی به مرکز لجستیکی ویلبریز (Wildberries) در شهر سن پترزبورگ، روسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68958" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68957">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=kPgA5CLecnCnKWuJXRlGtrkRhpIH_lj6N0X_7WKTzmuM_--_M2Y5xRQKnYMuVVc0NzvLLT2LWwkj9bPTTBF_DPUvEc62Bog-cR8zC7Gz06OtJyLqxmHdb0tcWcrhfaGFWcDknsdft5E05V87IjMZiL00LZr8pytpSMAnZYfAFxFU0HScXIq-nvBPjcjVEW8KnNHEi8SucF4sFVbsHxzfC4abMpBu8xfAUi6pQqzmNwRJSEK56X-4HXufFy6ykHMr4pLkk_Yp88ePGM2sAHfVlOWMZaUk50_4rb4M2o3DN1Qfu0jfXytUKoWaxdCazQp3TI9SZ4hEWSiTgYU1aLUySw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=kPgA5CLecnCnKWuJXRlGtrkRhpIH_lj6N0X_7WKTzmuM_--_M2Y5xRQKnYMuVVc0NzvLLT2LWwkj9bPTTBF_DPUvEc62Bog-cR8zC7Gz06OtJyLqxmHdb0tcWcrhfaGFWcDknsdft5E05V87IjMZiL00LZr8pytpSMAnZYfAFxFU0HScXIq-nvBPjcjVEW8KnNHEi8SucF4sFVbsHxzfC4abMpBu8xfAUi6pQqzmNwRJSEK56X-4HXufFy6ykHMr4pLkk_Yp88ePGM2sAHfVlOWMZaUk50_4rb4M2o3DN1Qfu0jfXytUKoWaxdCazQp3TI9SZ4hEWSiTgYU1aLUySw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ :
وقتی توی یه جنگ
داری قاطعانه برنده می‌شی
، باید چیکار کنی؟ دست از جنگ بکشی؟
ما با اختلاف زیادی
داریم این جنگ رو می‌بریم.
همین الان هم در حال مذاکره با ایرانی‌ها هستیم و اونا
آماده انجام کارهایین که قبلاً حتی حاضر نبودن بهش فکر کنن.
🎙
خبرنگار:
شما به آکسیوس گفتید در حال بررسی یک
«حمله گسترده»
به ایران هستید. نقطه‌ای که تصمیم نهایی رو می‌گیرید چیه؟
🇺🇸
ترامپ:
ما در حال مذاکره باهاشون هستیم. شاید اصلاً به اون نقطه نرسیم، شاید هم برسیم.
🎙
خبرنگار:
ایران کی بالاخره کوتاه میاد و پای میز مذاکره می‌شینه؟
🇺🇸
ترامپ:
شاید کوتاه بیان، شاید هم برن توی یه غار و همون‌جا قایم بشن.
اونا غارهای خیلی عمیقی دارن که می‌تونن توش پنهان بشن.
ایران، باورنکردنیه، ولی شروع کرد به شلیک به همه جای خاورمیانه.
اگه سلاح هسته‌ای داشت، حتماً از اون هم استفاده می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68957" target="_blank">📅 23:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68956">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=RnrjUi4DGOwJPAhGGHD-1323mHW5Ealkc7jaDd79PHYbB8ejtLfmrmnLbZbexTEgR5mW6B0EdYvvbIymqf3vQEEt9525xQ0f5q-xwiUvBqrB9EAjXHV_3aC1PshYaZXHKZSGlIFJK5vJdo64Kr0g6w_7HTh8w_1BQCIHFpw2Zc0ozW43yzBKl7KoNSWfCmvIZk5nP9w_Sc7ZfOI6yIYT87HmDXWZ4_CkzLZ3RfNpkmhHp31_uShCUwe79B_o4kyCshawOih9RHa-mtBWfccNUv6XiaYKdZtN0NqPWMG8vLEgQP-GIuGgA2hNBEuih93rwjbIVGf3jyhsVXuYxW2ewQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=RnrjUi4DGOwJPAhGGHD-1323mHW5Ealkc7jaDd79PHYbB8ejtLfmrmnLbZbexTEgR5mW6B0EdYvvbIymqf3vQEEt9525xQ0f5q-xwiUvBqrB9EAjXHV_3aC1PshYaZXHKZSGlIFJK5vJdo64Kr0g6w_7HTh8w_1BQCIHFpw2Zc0ozW43yzBKl7KoNSWfCmvIZk5nP9w_Sc7ZfOI6yIYT87HmDXWZ4_CkzLZ3RfNpkmhHp31_uShCUwe79B_o4kyCshawOih9RHa-mtBWfccNUv6XiaYKdZtN0NqPWMG8vLEgQP-GIuGgA2hNBEuih93rwjbIVGf3jyhsVXuYxW2ewQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
یه انگل هست که باعث اسهال شدید مردم آمریکا میشه. کی دوباره میشه کاهو خورد؟
🇺🇸
ترامپ:
نمیدونم. بهش فکر نکردم. پیتر، زیاد کاهو میخوری؟
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68956" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68955">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=YP1UXHhIhHuo5k1c1xOtVKnBk_CAW6pediCuFFFB_omYp1LhdNk_hnQ3oFeQysuab6Sg8BG05oYU7wtTU26gSYaKji3tYl-WNNwdhRkJmrKyiCML92kyqabCBvls5txOskzHeywe2sS3Du4KDa4h_aUPBvacmaoKxndCvdyiHNzRDR9ztA0zEyI-cZ0xYcX8H7Wsc-jjsUcmemaukTTLPCqftR2Tb1s4Cnj--U2tTE3A_waGEK_BD50xjJvkQIaJpk1MEH1pew9ZI3Fowz3QQ6ad_qMEPmnlYuJKVMgBYrcIAf44XtxJpazwfWaG6U1bn2fSepOeaaNzx0a3oOtBvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=YP1UXHhIhHuo5k1c1xOtVKnBk_CAW6pediCuFFFB_omYp1LhdNk_hnQ3oFeQysuab6Sg8BG05oYU7wtTU26gSYaKji3tYl-WNNwdhRkJmrKyiCML92kyqabCBvls5txOskzHeywe2sS3Du4KDa4h_aUPBvacmaoKxndCvdyiHNzRDR9ztA0zEyI-cZ0xYcX8H7Wsc-jjsUcmemaukTTLPCqftR2Tb1s4Cnj--U2tTE3A_waGEK_BD50xjJvkQIaJpk1MEH1pew9ZI3Fowz3QQ6ad_qMEPmnlYuJKVMgBYrcIAf44XtxJpazwfWaG6U1bn2fSepOeaaNzx0a3oOtBvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند. اما دو روز بعد، آن‌ها گفتند: «وای، این فوق‌العاده است.»
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68955" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68954">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=QKjrir_Wwzqeyw6Ywu9YQz-XGhClTsV2M60yDtFWd3Fv_Z9K1lKRQ0EHS0k-2AFskhW5LJcskPcXu0sKwXBxflWKZMnGueyFe0XiBMoMG1_6vKf0oh4W6BQ1pf059yBhn9Kc_EQi-wuIMRIquiZ8YbZxPGlgzsfY3GfnLRguo88XbjclegHsTqmVTzd72-JTuNY7-ADNYWV-Kj5QMszqaBGI-W3ANK7P1ApsmG8DNThVnIGgnRCPUn-07gb756MN4Pt3rm1laGG1Jb4x3eINeNWSu0Ny9pQk7wkYpCzwaMpN14uN1XTdCs8PQwupc8NNEaiuKPo5aasDsBfYoa5WyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=QKjrir_Wwzqeyw6Ywu9YQz-XGhClTsV2M60yDtFWd3Fv_Z9K1lKRQ0EHS0k-2AFskhW5LJcskPcXu0sKwXBxflWKZMnGueyFe0XiBMoMG1_6vKf0oh4W6BQ1pf059yBhn9Kc_EQi-wuIMRIquiZ8YbZxPGlgzsfY3GfnLRguo88XbjclegHsTqmVTzd72-JTuNY7-ADNYWV-Kj5QMszqaBGI-W3ANK7P1ApsmG8DNThVnIGgnRCPUn-07gb756MN4Pt3rm1laGG1Jb4x3eINeNWSu0Ny9pQk7wkYpCzwaMpN14uN1XTdCs8PQwupc8NNEaiuKPo5aasDsBfYoa5WyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همین الان هم در حال مذاکره باهاشون هستیم. به نظرم هر روز که می‌گذره،
دارن جدی‌تر می‌شن.
من معتقدم
توافق، راه عاقلانه‌تره
؛ اما کاری که الان داریم انجام میدیم،
راه ساده‌تره.
همه‌چیز آماده‌ست و هر لحظه می‌تونیم اقدام کنیم.
وقتی وارد ونزوئلا شدم، همه مخالف بودن. اما فقط دو روز بعد می‌گفتن:
«وای، فوق‌العاده بود!»
الان هم خیلی‌ها دارن همین حرف رو درباره ایران میزنن.
به نظرم،
ایرانی‌ها تا اینجای کار از همیشه جدی‌تر به نظر می‌رسن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68954" target="_blank">📅 23:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68953">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=jFip_vdMjheB3Tf3Vi91DZqFuTyWrvUWYhN10wZjqpWKjstP2EIgCjjJpURniFFR2N98X2dWAFkEuKv4DiWc9NE11U_wPmgW7l8-PuaXxbMPIdV0dYsBgIgQ2DIMwVWwxOsrG9y8Fej27HyFluAfCAXx6XiToOGIC0_6L3djkwxsqvtistnUMnIfJ17pX96rxDQMYMyWnAB3QdPtteu9wqnKhlAAezrPjbJz8LmuPGtPepGEwTl6ysdEVDBf13hgx2-HaEI_YPK6V26OWyHueA6hUyIHDodtRFHSIarZSPIySPnNVq7gr9WDr7VDT2Dmb1RcewLKJMQHR5GYMraL3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=jFip_vdMjheB3Tf3Vi91DZqFuTyWrvUWYhN10wZjqpWKjstP2EIgCjjJpURniFFR2N98X2dWAFkEuKv4DiWc9NE11U_wPmgW7l8-PuaXxbMPIdV0dYsBgIgQ2DIMwVWwxOsrG9y8Fej27HyFluAfCAXx6XiToOGIC0_6L3djkwxsqvtistnUMnIfJ17pX96rxDQMYMyWnAB3QdPtteu9wqnKhlAAezrPjbJz8LmuPGtPepGEwTl6ysdEVDBf13hgx2-HaEI_YPK6V26OWyHueA6hUyIHDodtRFHSIarZSPIySPnNVq7gr9WDr7VDT2Dmb1RcewLKJMQHR5GYMraL3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما درباره بمباران نیروگاه‌های برق غیرنظامی و پل‌ها صحبت می‌کنید. بخش بزرگی از جهان این کار رو جنایت جنگی می‌دونه. شما هم همین نظر رو دارید؟
🇺🇸
ترامپ:
به این سؤال جواب نمیدم. شما از کدوم رسانه‌ای هستید؟
🎙
خبرنگار:
نیویورک تایمز.
🇺🇸
ترامپ:
حدسش رو زده بودم؛ نیویورک تایمزِ ورشکسته!
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68953" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68952">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkL6IjLmN6FNHHux7XdBCs8XqxQWojh4DJiZBILHyvNEBOi5YnSRZOv7KJ3Dw4CCX7LjFtK21SKc-cIXN22AizOi9AKMqobKzUsBx_WQTwtlRky3gi_7GaOdXZU4oj9-glBWLGFALj7J1gtHF2ZXw38E6Jxx29iHiHrhQtxKfTXTA1zcKV2tDisdAGPKcgWz_EM8cyiJ7IhQaUQYvgORKMFQSAb6oSvfcCRoZIvnIrZVxMIdPRvKv1oyLgOwYRZkXGPyexWuupfmIEwO42RsoGjssW7x48SxmHPTkaWrA1qWW9mY796KSpxxK4qYivbi1z5lQG4nJVUAo0dLToNhGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
صداوسیما:
دشمن آمریکایی دو موشک شلیک کرد که یک نفتکش (یا تانکر) حامل گاز را هدف قرار دادند؛ شناوری که از دریای عمان می‌آمد و قصد ورود به منطقه را داشت.
نیروهای آمریکایی گمان می‌کردند که این شناور قصد حمل گاز ایران را دارد. اصابت دو موشک به آن منجر به کشته شدن دو تن از خدمه و آسیب دیدن موتور شناور و در نتیجه توقف آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68952" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68951">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⏺
ثابتی خطاب به شهریاری:
تو دیپلمات وزارت خارجه بودی چجوری شدی استاندار؟
اصلا بچه شمال شرقی، چجوری الان استاندار در شمال غرب شدی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68951" target="_blank">📅 22:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68950">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🇺🇸
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا بر این باورند که رهبر عالی جدید ایران، آیت‌الله مجتبی خامنه‌ای، بسیار بیش از پدر و سلف خود به دستیابی به سلاح هسته‌ای تمایل دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68950" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68949">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCarAVTalsycuUdLpuKy69VUu87dMmHIFyCBjeaM5h_2nPC_UHKPrJ0i_nTDJTAieHqrwh2GMXKeQeJMDXCOkEtTOz06iHtxhv-ZpmyE9dywZmsw8Er5zxdk9LvXKhS14vzozSoXD__ceK1Ep8TXOGdxbyvyCdSosASjXDyTBmrRiLPNp9kd2f10pavQ9zM2iioA0Mryhk_WTEx5QckQ4OF29Y8LLxVtkgByocW5sKrRvj1omhj2fWphC9P4YQHzMyRaPPl54CC0kPRWAUFGW8gKzL6mYsAXsN8VrYC7r3Z2WlwDnbve2lxPii1eJci1duqcRVd97CYWTKId8nZjzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک‌تایمز:
رئیس‌جمهور ترامپ روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه خود دیدار کرد تا درباره تشدید حمله نظامی علیه ایران تصمیم‌گیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68949" target="_blank">📅 22:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68948">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mt-ePlSKMTgz73uKvIrw-8SoqynZracKyjjAqmtYujfNFBtCkAbWE-AjF5dLxw6YSYq_7N_LNOBXmk1lqReWJt7qvvpIZtG_ZOPiSTvDsF08xRSRQ5ldKYkXghj8WhthD1bLg0FOxrH--pepIgqaberpnFFlOwXKOtsjz2X62DKx4Pp0aOtFzqoFv1FvYPztCGxLRoiPaolC1UvUh8sZ9aUH_0nzRVLq3JHPZwZo23G4Bxcy__UoPVXhXzvv28ukOdDwhXXleRrlZbtDrEwa6f_KZ2dn1Wm-OK11VUuFoc4J976NGJbAcQbnMn--hDx2_er1MYOD0k4nq58ohv35Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68948" target="_blank">📅 21:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68947">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c449631.mp4?token=PYCSy8FbUZiNduVGOEqyIvNlF3LZvVGK2ZYFkv6uHqikHDlHJBuZZAMRxShp65UBr_oODjGSmiHAYXHk0koocLgGiTedhzQr9rx3bM2QiVHMmnqupyzReM4GRS6-2iWMtqGGngeOslmoHhkKkzcxmpC9cCICaeOQ9BDhzZ-vMImeUUKkIEKGssLPge9M5Xt2iv4ZEii4KgxLN0LbAaRsZ28jXPQ-FpyrLlkP4enmnttx9dGv5G2sZCFwRyMEZubxSnE9Y9jbOrfsAnrgl9D1joJ8iwO5BcKsqVBP84mjXmX1XEYFFJNyGKq1r-bhpeoFpOM1XEQAqH1qbeCawY-TEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c449631.mp4?token=PYCSy8FbUZiNduVGOEqyIvNlF3LZvVGK2ZYFkv6uHqikHDlHJBuZZAMRxShp65UBr_oODjGSmiHAYXHk0koocLgGiTedhzQr9rx3bM2QiVHMmnqupyzReM4GRS6-2iWMtqGGngeOslmoHhkKkzcxmpC9cCICaeOQ9BDhzZ-vMImeUUKkIEKGssLPge9M5Xt2iv4ZEii4KgxLN0LbAaRsZ28jXPQ-FpyrLlkP4enmnttx9dGv5G2sZCFwRyMEZubxSnE9Y9jbOrfsAnrgl9D1joJ8iwO5BcKsqVBP84mjXmX1XEYFFJNyGKq1r-bhpeoFpOM1XEQAqH1qbeCawY-TEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
آخرین مصاحبه اکبرعبدی با گریه:
ماهی یک میلیون تومن به خانواده ها پول میدن
وقتی روغن یک میلیون و هفتصده ، این یک میلیون روغن برای چی میخوان مردم ؟ برای جق جق در خونشون میخوان که بریزن صدا نده ؟
حالا روغن خرید ؛ باهاش چی بخره که چیزی درست کنه ؟
نمیدونم این خدا هم حرف گوش نمیکنه ، من با کسی حرفی ندارم فقط از خدا میخوام به همه کمک کنه
فرقی نمیکنه فقط به ایرانی کمک کنه
به هممون کمک کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68947" target="_blank">📅 21:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68946">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ov7JVrE1DfyE2V9XiW4qVQ_Ye6tIcwLLv_1rX7t9eFPKfVm0yF4ku7qgGcaVOz5oC4u1A2nvGabzexP7mnoZ0kpFgKgmmXkUY_PfDfPidw_xLIOUY1LCMRCb8TJqoZea5ICRXJeJpzKdLz2orH7QyPQBF5_nXqW3Sy48QO-Xpiu-1dYXDBFBQlLIEdZccp3xtkqUxeizw_xb61bsXUe9_QqBU7uzMZxLjelb0dHL_VgRtIHSQK4YTVkoPW08wKp5sEhKIo0Bn1hCBB85MgiKXAYS5z4sVW2SN5at1IoB4LbwBkJz-ZNOEAdP_AuMGIJjjbWGtpwzanasSNL84bZNYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون، در سن 66 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68946" target="_blank">📅 21:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68945">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vq2Y7WE9Cp0DTu3XGudRH8gmC2t9tJ7oR5kZxk1koU-XYiBrO6XtaQ0baMKyoT7cHmP1_v4XxqOqZsixLVHgP-D3u1xXv5XJYGdveOZTgPrp7NsUOtaplikEdb0zKvidstr-dk82kJkgMNpiCow5SFHwUcP5Nmbj6X35ApDIVdXmjzH9YFFEmyaU7ZHAlAydyEOovFLPbs8GwviNOsaPQNXvR9N7phxls4QP42E53qu0OJVFRdVX00KsslObaZqTChhkMVeSjnPgj933kzXxYPEM4muF0furE0K35jaXXL-5_w50GGkMzBKDloC6A0BhoqeSy_LTB91f0CGTW7v9-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
علی عبدالهی فرمانده قرارگاه خاتم الانبیا:
از این به بعد به ازای هر شهیدی که از ما بگیرید یدونه امریکایی رو به درک واصل میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68945" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68944">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2066d70166.mp4?token=crAV2bke5fFRkaOwuklDZqAv27kgoeCtGBb3PQNcIhXk10FrCB2iLXSuU_fHC2vE_RvK_5VFaml2HtW4CY7WfXMmS71AbBAisXEi9lHYJvQqtBHDiHZuOXDxlFRwqQUxyPUKKRv8P7aOMrDm_BU7FTVDCucsYfxyeOBdgS4ZmiUMRgki2mixwqG84E5eG37TwmAaQSfE8gI4u_50XAFBDTxpCPO9BjIjHm-JhcE-yTHs17TdSWOKAcCFYnpKtXjhSeAYD5QbXVLD9XOyeXq7GvX1EgMnGtyjjcj3YGVkae_F3OdrxYTXH0Etf279AF2RLFy2PjCnQW1Pf1e53w9qQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2066d70166.mp4?token=crAV2bke5fFRkaOwuklDZqAv27kgoeCtGBb3PQNcIhXk10FrCB2iLXSuU_fHC2vE_RvK_5VFaml2HtW4CY7WfXMmS71AbBAisXEi9lHYJvQqtBHDiHZuOXDxlFRwqQUxyPUKKRv8P7aOMrDm_BU7FTVDCucsYfxyeOBdgS4ZmiUMRgki2mixwqG84E5eG37TwmAaQSfE8gI4u_50XAFBDTxpCPO9BjIjHm-JhcE-yTHs17TdSWOKAcCFYnpKtXjhSeAYD5QbXVLD9XOyeXq7GvX1EgMnGtyjjcj3YGVkae_F3OdrxYTXH0Etf279AF2RLFy2PjCnQW1Pf1e53w9qQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما از یه بازی فکری رونمایی کرده که توش باید
بچه‌های جزیره اپستین
رو نجات بدی و ببری
بیمارستان خاتم‌الانبیا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68944" target="_blank">📅 20:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68943">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJN1coy6vT-Zv_xFuqRPCAc6KVjoIEo0bwwQX_3b90IoiusXMDHy8NDTLr1HA19Ci2B4xCVicl-Zw6UpO1Mc8vXP7TJCILPjh4PfyEnEi22M-VoNdJ2FbDTzfT2DSeWbyyO8gHIYRVd6ZPn6lQOaNSj6T9HLZ3M-glI1mFOUlmPbpEW0wk_uj_m9XNqxkxLxf9vf9CY1bl5OPNdsZGmGl-eRcVBa1uTEgPrGqEuOp5vc8w9iEL603T1YkqdSk7Vx5qknEtWYo0seID-pavtDgw5OgOra-TGA2xW-Eqzw_onv8ID06sORcgDpW4qaIr6n0bpNtUVWxvNhCqBEbIBEmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ:
رئیس‌جمهور شی در دیدار اخیرمان در پکنِ چین، به من گفت که تحت هیچ شرایطی به جمهوری اسلامی ایران سلاح نخواهد داد یا نخواهد فروخت؛ و این گفته شامل شرکت‌های چینی نیز می‌شد. با توجه به روابطمان، من به حرف او اعتماد دارم؛
ضمن اینکه خودم هم لطف‌های بسیار بزرگی در حق او انجام می‌دهم.
به همین ترتیب، رئیس‌جمهور پوتین نیز با وجود جنگ هولناکی که در اوکراین جریان دارد (و روابط همچنان برقرار است، همان‌طور که با رئیس‌جمهور زلنسکی نیز چنین است)، به من گفت که به ایران سلاح نخواهد فروخت.
او درک می‌کند که من به اوکراین سلاح نمی‌فروشم، بلکه به کشورهای عضو ناتو می‌فروشم. آن‌ها بهای کامل را می‌پردازند و من هیچ اطلاعی ندارم که آن سلاح‌ها چگونه توزیع می‌شوند.
بنابراین، به عقیده من، دو کشور عمده‌ای که اغلب در ارتباط با موضوع ایران از آن‌ها نام برده می‌شود، در این کار مشارکت ندارند. اگر چنین می‌کردند، برایشان بسیار بد تمام می‌شد؛ و قطعاً به نفعشان نبود.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68943" target="_blank">📅 19:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68939">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/padxemmdQ1yYm4QvsaMFO2ihCG_Dw9tKmkZ29Ro7gtKYzi1nWWp4wC3XMnW14bIWihF_B-NbORGIqgXQmqMT17x5dEjLBZsmA2ezSNqunMqcWzl5SZa6hiQuZtmPjW86ZPO3y4Pnz2JcOFEyMw2Q1wsDeRGeoG_j9XQhSfzdvbNOtT6eqtm94Qz10APQq4ypOtbG9wPJDei_-eoKpWTRe16lQ7niHL6GKw8QfBEAKkTYzmt9I89_7ptKf-TnZA7VPkWcypbnajuzSk6ooysCyKTTbS_ZGTO4zFg17f_xtMeNpLvN8Gw4gw7716GfTTX_NrioWIuNCb8SmMa5xqXOIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CYqpUPdMB50j4HvSsMqzibjUFeiXsLp1OheXaZT83FJKEZAjB3QbLrbiz2U31rQouJ-Eg828EdOmQZpMj94TAKL0C7tfgQ9fViSUBg2MqTAQZO5b8JVY4MzwVNC-RmGhLHRmIj7AAhnszFBzGPI4VYYlBrRkku7BIrILX075xSVkQd60N2kzXQxdwFT3kovVittgAoqDJ3hmsOYyXXOX5RLhUg4YE5VReiT7BU-SLZSBWMu2na14SVZQP_v-j6fq6dx6N8s5b2bfU8nt2Vttx1bRW8Qfrwp8-NuYpjUiEYjntaAomA9AnQRA3-_2SgcNYoA4JaoMRHYusG9NSK581w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2f491-GeaOQFC8j6FCOyXDYgXtYcLjxnPWJ64J8GywixQuVrvZSg4ZVvaqhT4iYLzXhuWjeT4ODrPXyI5LWqj_pdRLK5HKzRqipP2NCpalBl9v8M2-OwRuV3mGw0voEzhsH6_ujXqdCNhrofdVCZ-48SJoIb_MhZZiCYYYCxNQH9bQ4ktSJm8_QAIGG8a2vnpnklTgM7c93NPtUJCmK_dlfdCbyscENsNiiZQbHNvSoj5Cec0n0MRA_btSfmOm-9uUnP7Tz1IYhHDNdjYtiPkwEo0RvEYhzqQSFSzE6XDsRUDNr2WrJJGHcAELQZXu-w0aqfch6Qw9G7Ql1Q98gVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=u2Q6pSNKOyjdv1CKTHgmYXM_Z9ZK_tih9zZuhG9tZQtnOoNrnY_bbccIk-co5LuN5qzp3jUb5csvdMX9er2Cca3eJdpF0kF0GdwVNBoDn-XJ9VM_zRkcKQNV-0uH9BcfjJgwwGBF_I9Y6D38jrP50Rchg8pHw9ahtHlD1Jksnl6k-HGKLJbM8ICp05v0CjbLugPb4n2UHgiYq84pHJ1UNCIszwzlRrydvn-R-yXrkn8oNYql07W6TEYhzSzI4HQDpoybOo_y_CQLKJuMmaOM9qf3XoKawU0jGdxWIpYTZpc2tTGOtTJUely3m46GBm9KiKr4JLD6DMAf8zA-IyuLlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=u2Q6pSNKOyjdv1CKTHgmYXM_Z9ZK_tih9zZuhG9tZQtnOoNrnY_bbccIk-co5LuN5qzp3jUb5csvdMX9er2Cca3eJdpF0kF0GdwVNBoDn-XJ9VM_zRkcKQNV-0uH9BcfjJgwwGBF_I9Y6D38jrP50Rchg8pHw9ahtHlD1Jksnl6k-HGKLJbM8ICp05v0CjbLugPb4n2UHgiYq84pHJ1UNCIszwzlRrydvn-R-yXrkn8oNYql07W6TEYhzSzI4HQDpoybOo_y_CQLKJuMmaOM9qf3XoKawU0jGdxWIpYTZpc2tTGOtTJUely3m46GBm9KiKr4JLD6DMAf8zA-IyuLlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ویدیو ای از بمب‌افکن(B-1 Lancer)که گفته میشه در حملات شب های گذشته علیه اهداف نظامی در خاک ایران شرکت داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68939" target="_blank">📅 19:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68938">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=MiiYjlPLV9sZf5R4BLtLdr0ctg05hn9fHqu8XSbbCCzj4uLFXPp4xVJ2KQIX-2_YoFioZ6aqmskEjxHi8tBjfM4_Spv_wnnwRdHpMSBBcUhurQXg-BKm6enVNdhL0miC91Y3LKLBUa6i3s-pz6iibc2Vae36dSQlUCRAFLM2A7EZPdGvZbgFe3kKf6j6mntzq5DKxPza_EPVywbofD8mrfRvUupNDSuQ_kGR1yZzkVDcjEIBWSfCTUO91YdvUQ8VDiLrhLfbqVvarNUb9XGW74gzCiXyA7YOgaocoFrQigvARjqM4mJcyq-O1uHjdPjkLoesQFl-jngoAn46bOYrrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=MiiYjlPLV9sZf5R4BLtLdr0ctg05hn9fHqu8XSbbCCzj4uLFXPp4xVJ2KQIX-2_YoFioZ6aqmskEjxHi8tBjfM4_Spv_wnnwRdHpMSBBcUhurQXg-BKm6enVNdhL0miC91Y3LKLBUa6i3s-pz6iibc2Vae36dSQlUCRAFLM2A7EZPdGvZbgFe3kKf6j6mntzq5DKxPza_EPVywbofD8mrfRvUupNDSuQ_kGR1yZzkVDcjEIBWSfCTUO91YdvUQ8VDiLrhLfbqVvarNUb9XGW74gzCiXyA7YOgaocoFrQigvARjqM4mJcyq-O1uHjdPjkLoesQFl-jngoAn46bOYrrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
در هفته‌های اخیر، آشیانه خصوصی وابسته به سپاه در جزیره خارک هدف حمله قرار گرفت. در این حمله، چهار فروند بالگرد آگوستا وستلند AW109E که توسط شرکت خصوصی بالگردی خلیج فارس بهره‌برداری می‌شدند، منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68938" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68937">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1AqM2xFGnF1NTAopRptBf8iu_yy6avTJpxaI7y6q-jJId_RWSpW8mw9h2E3puEJV0Vjni7HI7IM_u134ZRcDJ-oKdk5vSLzjwcHAJLG3Ahr0k_fg_N8L2Azdbu4vpKZea5AxF8hJPVdxZqFAQh3Szc7yZUGmZb7Q_K1UJv21gk2nAxWaIGHEqB_fxxoV4HoILXbWWGwMpZVC-8l5sZbxTd_FVeFr-btxesvbiFu27-uSxrffz1VIo2HxodX0qZaq0QHotygvC1TIoxYNn_wCk9uT4YYdMhJMRu7EJMpj5LNKkM0O8Iz-b1JiQMhIbyJlh7Mecb_gr_DQk_5zTDmsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رئیس‌جمهور ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68937" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68936">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887792c366.mp4?token=ZbZtsD6yOnlXy_mXnBMSo6OQodltzVxrEKSB0DV9iHEtbj1L4bU1C03UFxqnxN1E1MGCFmbkL-cyFJNHJXPbyyztaAxHpfWJouggv7kFDtDr5jCBlXUutkFHl2OJ2hveIq-1YFakqMbWiHfSdI765BoiOe8UUp9w2F3uyyvWuHwWJci7L6nzfpyZoy8gouELeXxtm4WiCTcV5OnopR39PtH1Td8yfBBjGK8k-Es6or17zlElGpDNQptuhSk8iqyoimGqehS5c5Yc8aGTHC11RcvQzALr4ANz9T2LtEfdaBaJMRLRbuPgAJekFle5byaZiOA3LSoQuPYapbXo3_985A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887792c366.mp4?token=ZbZtsD6yOnlXy_mXnBMSo6OQodltzVxrEKSB0DV9iHEtbj1L4bU1C03UFxqnxN1E1MGCFmbkL-cyFJNHJXPbyyztaAxHpfWJouggv7kFDtDr5jCBlXUutkFHl2OJ2hveIq-1YFakqMbWiHfSdI765BoiOe8UUp9w2F3uyyvWuHwWJci7L6nzfpyZoy8gouELeXxtm4WiCTcV5OnopR39PtH1Td8yfBBjGK8k-Es6or17zlElGpDNQptuhSk8iqyoimGqehS5c5Yc8aGTHC11RcvQzALr4ANz9T2LtEfdaBaJMRLRbuPgAJekFle5byaZiOA3LSoQuPYapbXo3_985A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
❌
👑
مقایسه تسلط زبان خارجه:
وزیر امور خارجه کنونی دارای دکتری علوم سیاسی از انگلیس
با
نخست وزیر ۵۰ سال قبل ایران دارای مدرک کارشناسی علوم سیاسی از بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68936" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68935">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=EVjOiEFnBa_LM-Td5haiNJLUH6rLammqnJMTrwAYGUebq3Bmlf4IbfDenoOvBr6AseW9tjge7lbnkWLdok-qHerBxcBVzrDBK1yy5O4_JdwXpkBwowBVORI_afo8Yq1prC7iRQm0lL4tfLLysqKJEtDsIMFjPjzHGm-yPNlyJK4Mp2J-5JOorBIV1Mhx6_BdlPYx07pARL12EltNvri7TtdtJR6sJ5-1aE-24e5mxbmLsmtrCWglZ0fSzEmXxzwiq9212kQR9WVQKRGhw8QrHt7D0xtYMQA-Uas1G6gV1-Qngn-1x-keaq0-SChZm7mbYaXnt9YULB_tv8vSSmZTdpXco802w6NgFWQytMKMgSMe0Rmy4BHlT74POf2_pSrnEizkJW1LSO2R1w2kW9oUNSFgIlXm-ippPRSxtXRZHghkoZ3-Z3crONXk9rMPHbMh_do3SUdiPPCHawYBF3tH_626lBeowEfSMcoe7IzXdGse5i6xBr8orCoacn8nqLrRJvLO6vw_ZLEbI_EibIscl51jowM0aR8tTGDNVaF27Ki0lsj2DsGYD__s1gVZjLH71VKc-snbu_Fiz7ZXnUAP76XcNgc2CfrftLX0r3fM67GkN8t_MSWhe5E63_TpZj6nnzGn3My6rWXobml7ZDpQkXl0YFkzahZdRdHhdrNo_Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=EVjOiEFnBa_LM-Td5haiNJLUH6rLammqnJMTrwAYGUebq3Bmlf4IbfDenoOvBr6AseW9tjge7lbnkWLdok-qHerBxcBVzrDBK1yy5O4_JdwXpkBwowBVORI_afo8Yq1prC7iRQm0lL4tfLLysqKJEtDsIMFjPjzHGm-yPNlyJK4Mp2J-5JOorBIV1Mhx6_BdlPYx07pARL12EltNvri7TtdtJR6sJ5-1aE-24e5mxbmLsmtrCWglZ0fSzEmXxzwiq9212kQR9WVQKRGhw8QrHt7D0xtYMQA-Uas1G6gV1-Qngn-1x-keaq0-SChZm7mbYaXnt9YULB_tv8vSSmZTdpXco802w6NgFWQytMKMgSMe0Rmy4BHlT74POf2_pSrnEizkJW1LSO2R1w2kW9oUNSFgIlXm-ippPRSxtXRZHghkoZ3-Z3crONXk9rMPHbMh_do3SUdiPPCHawYBF3tH_626lBeowEfSMcoe7IzXdGse5i6xBr8orCoacn8nqLrRJvLO6vw_ZLEbI_EibIscl51jowM0aR8tTGDNVaF27Ki0lsj2DsGYD__s1gVZjLH71VKc-snbu_Fiz7ZXnUAP76XcNgc2CfrftLX0r3fM67GkN8t_MSWhe5E63_TpZj6nnzGn3My6rWXobml7ZDpQkXl0YFkzahZdRdHhdrNo_Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عباس:
چهل روز جنگ و محاصره بود هیچ کالایی کم نیومد
بله قیمت ها یکم افزایش پیدا کرد که طبیعیه
یکی از مهمون های عالی رتبه ما اومد ایران و تهران گفت من وقتی شهر دیدم تعجب کردم
گفتم این همون شهریه که جنگیده و محاصره کشیده ؟ من فک کردم الان بیام تهران شهر مفلوکیه
همه دنیا داره به ما احترام میزاره جز خودمون
من رفتم عراق حرم اونجا استقبالی که عراقی ها ازم کردن عجیب غریب بود اونم ساعت 2 شب
این استقبال از من نبود از وزیر خارجه جمهوری اسلامی اونا به من میگفتن قهرمان
عراقی ها این همه شور و شوق داشتن اونوقت صداسیما یدونشم پخش نکرد
یه نفرم اون وسط تو حرم گفت مرگ بر سازشگر
با مرگ بر عراقچی مگه مشکل حل میشه ؟ من اگه وزیرخارجه نبودم باور کن پشت لانچر بودم الان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68935" target="_blank">📅 16:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68934">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:
حمله پهپادی به مخازن لجستیکی ارتش آمریکا در صحرای عربستان.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68934" target="_blank">📅 16:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68933">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtCJwVvwCCU_mLpRyVAXg1ulHmlofpxA5tLbb7e9gXx4fw5902QMRWAkJQWFMab0XgbAIOfzuDBW47X75vJM3_aekc-AV72u8_1oaNz4Nc35KbmZjVjG4NB4XUebEwRB0_fu4zcycEFOncFg8iB8vREz61hCWUq6OhiJe09T0vYVlTbI04P2C6HOvTLAdBYZZfN8rVI12-rIMoPV9ULC2GvHWbu-82TxqXfx6nBJIRS8jpMC2G7NZh6NEMydcINddHPhV6VZykAs6wmIq0jwNXEgxD6v8ce8qz3ScRmO4h7yvvbT_hp0afrDBOXQ148D1MzJkr_UZwTVpyucD7W1kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما:
یک سر در برابر هر چشم!
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68933" target="_blank">📅 15:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68932">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3x9d-vYexz9Wj44inH69N5e1KOE5AOQSX182sHsJjB7WUJ4ApfOKxJBhOugrXrFvEQbgHz760hA9S6Am0iX49YunDhq_EFFMCLsOAe6CyuV5w8oaHiZ01L4R99rpzHCR-41pkvRdbs-wH-DHOE8TqTsiCkXLLxui54n2OhqlKhIojVe71lz2zZBGl85ssjt50723vLiiriIrds4h0yx6Ne5oMWY-Zl25-ukslXxvA1vKtOI_a3NVlVlcdoIzv3ll380Vez9F_ShrbQQvJrfbuLWRtvAtY_BtKMKigaoIGHJllTIw5LMl2CEQA8hm5vZFqJ942peD5j_2XxxNFgr9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
وزارت امور خارجه آلمان اعلام کرد که این کشور فعالیت‌های سفارت خود در تهران را کاهش داده و بار دیگر از شهروندانش خواسته است که هرچه سریعتر ایران را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68932" target="_blank">📅 15:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68930">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qTS8-o4v0FxHtSQHdQvjwFhS9t1BsDSpu_6dihaYEHJMH-EuYfi3qNu8pAupBxxJ39ktncgisKXPMv1HxWcAAqdZvCywYs9VNuMizjCnSxq1Q732fA02p_Z0E8wX0cIIe4VTVjrUGiVLSeqZ-9R-AsBqBn9cPY2rL0KlFv_PEwZG_n6tbRCONmnkVraJsl0NOXJdT2cB--Tqt0-rNODMj8GdMe62vJbGqz7VBQhxYrfl9SaGAEVxnTo7OqzK9bsBT5TUpf1ixHYEZOTWDvbX68ZkfhOfl3N7ln_lCvegkM2Zg2cd5pT0pMaShk6QMYX3LzqUHcHh46IA1SjlOVWgsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tEwmKERkBQkahg1DP5OYoEG8y45YBMAEWJKBMHbZqnDMcn0TQeqH_0v1bHQy2BV3FmEE9mgIkoHh777-D73ervl8RlCLWy6y6l9Tu-d4_7i4gQZ8PDTh4Dvz0rmiWsW2ZYhX2Hk46yoRQHu8qIxHOq3H80KFwNYL5mv2oZ2p84gmLpYCaY6ZuH8R_vOOMHeuYmYsCyBkLt9AcA5q4MpmCtOf2mY7AdLBPXrDx6vVVHA_IODVijH8Q-F_r-iSOdPAldxRc8rAT53KkoA7QOScJ6llJp6Ogfj4M7FjCI8G6Z-Nwu7sDvxTI456vbHnqeTMx_B231D7gg7mrf_QbV_a2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی شاهزاده سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68930" target="_blank">📅 14:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68929">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=GNeUoejWVOsHdtwn7n1p_1_c7pMW07J8Joh1fbTF8z52lj-bMUXzyv1TyhUbbbx_-RcjZpgCShbj6HuO9TPMuAx6hbRiBHz9uGaYozpH3TRZqXVPfpuD31q6zPLw0NzU1gmkwIKcUmcSHUXN1_hjz8TizK-PXz8hkH9R2zwLJ6NLs7EcBaYJzdQJnetFTU8Eq5R2bTR1fPXxkA4J0_e5zz698sPuwVJESm0G4BubzGk7T7L0noxFbkhmp7LMw2831Rn7GBiJ0UvDgQ-p7QXaBn89x9zj0rkI8HIHEqF6MNi4y2PL6BDulDz-n3c-8q9OXtvQPi_5C3BcEVkl3J4yXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=GNeUoejWVOsHdtwn7n1p_1_c7pMW07J8Joh1fbTF8z52lj-bMUXzyv1TyhUbbbx_-RcjZpgCShbj6HuO9TPMuAx6hbRiBHz9uGaYozpH3TRZqXVPfpuD31q6zPLw0NzU1gmkwIKcUmcSHUXN1_hjz8TizK-PXz8hkH9R2zwLJ6NLs7EcBaYJzdQJnetFTU8Eq5R2bTR1fPXxkA4J0_e5zz698sPuwVJESm0G4BubzGk7T7L0noxFbkhmp7LMw2831Rn7GBiJ0UvDgQ-p7QXaBn89x9zj0rkI8HIHEqF6MNi4y2PL6BDulDz-n3c-8q9OXtvQPi_5C3BcEVkl3J4yXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقچی:
کتاب نوشتم، «قدرت مذاکره». نتیجه‌اش هم داریم می‌بینیم.
همین دیشب یکی از وزرای خارجه آفریقایی به من زنگ زد و گفت میخواهیم دیپلمات‌های مان را بفرستیم ایران، برای آموزش!
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68929" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQunMEsG2EZ3v0c2WOizUB7GNpyh6PEXj1nhO1DKOd5QbXcSivr_DCwTjZxgJZNlfiRE7hh9EQiTJJOp7VveKNA6yN4fHLpvy3qpy3Gdkep7rzU5hLn_WvcsCe4lBqJNMvDDvIIrvtSMY40SgkhQi_CgsmFm8dF05rXtIHFA1GRK2PYN0jbBFZDzvtIcwEWkdEwB8uJqkSKPT6lU66geoe9qurWMtb6BqKRm7bl1CVEPnlVd-hf_iMBw5uugzy0cTMFl8xNwCKEyr8A-CA-NMmp_Bl3znUfDZMCbrIRBo-KF0rUniYLAUErZX8xkwvUWIdEQsprq14Ja299SwKgPew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68926">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M55Qdu-yA4mpq8BL0bg27sH7jjzd6BJVDuDY8TYzU1npyAasGdWOAGa2KOGUotdfAKnp-TeDTh9yPl_aQAwPm5Kcpfwyd783nx5e77Vn-Ce1CqzYxl6454ltRE1CcGs75fWmzK9eJmo5mvQ99AzXuPSPyXr4o-vCyWXeoy5xEGcicvRefJdofcJtKyOCm3PBNujslH9xvPy1IieEc-cH_5F0fR9GZDbsRD6wr3H1ZESCyT_in2DzwddBCE4_xdZw7KulobH8WHE9__OSZzkdygIya9yBamQFF2m6IkkPvAD47i7K1wLsxik232qlZs6ikGIJt-7gk_izM8yru_p19g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
جیک تورکس خبرنگار یهودی کاخ سفید:
نمی‌دانم چطور بگویم، اما من در خودِ «کاخ سفید» کار می‌کنم. از اطلاعاتی آگاهم که افراد زیادی به آن دسترسی ندارند و با اطمینان کامل به شما می‌گویم که آمریکا برنامه‌ای برای شکست دادن رژیم ایران دارد.
آن «کارشناسان» حسابی غافلگیر خواهند شد؛ هرچند بعدش وانمود می‌کنند که از همان اول هم می‌دانستند، پس... بگذریم.
به هر حال، خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68926" target="_blank">📅 12:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68925">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=flqVF4RBt7bexe2zvUgyoVkyr06WLkMGJiyytmSHHnJqIB7z8TV1DUDRgX2Cs5U_3XriVJGYmdL9W2LBgGRJkQGPdkP6mJQyjQ_1iyVDs3L8DRxCR833TIFkR_MP4FTjXaxWRR6Ew2rpduf4fKqDTuI0ZtJnirwPgEU6xrHGJv_4qklCR8OIvbWwA7fzgmvSJtRowyq8GnAKHR4RcPqT5L6_mBtlXq-u9y9UoabN1aEc_rMRfV87kwqoKGCweMamspgTsYMxzEk93wih6v_mkFU6HXQWlmVm__3kEyu4pB4XAlC5sxzo5UMepQ7SChkJAQ94_ZfbIBNMFI6-QoIDvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=flqVF4RBt7bexe2zvUgyoVkyr06WLkMGJiyytmSHHnJqIB7z8TV1DUDRgX2Cs5U_3XriVJGYmdL9W2LBgGRJkQGPdkP6mJQyjQ_1iyVDs3L8DRxCR833TIFkR_MP4FTjXaxWRR6Ew2rpduf4fKqDTuI0ZtJnirwPgEU6xrHGJv_4qklCR8OIvbWwA7fzgmvSJtRowyq8GnAKHR4RcPqT5L6_mBtlXq-u9y9UoabN1aEc_rMRfV87kwqoKGCweMamspgTsYMxzEk93wih6v_mkFU6HXQWlmVm__3kEyu4pB4XAlC5sxzo5UMepQ7SChkJAQ94_ZfbIBNMFI6-QoIDvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حملات ایالات متحده به ایران برای سیزدهمین شب متوالی ادامه یافت.
در این حملات، محل‌های گزارش‌شده‌ای از موشک‌ها در یزد، انبارهای سلاح در اهواز و چندین نقطه دیگر در مناطق جنوب و غرب ایران مورد هدف قرار گرفتند.
در پاسخ به این حملات، ایران صبح امروز چندین موشک را به سمت اردن، بحرین و منطقه اربیل در کردستان عراق شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68925" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68924">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=MMgMNVh8YvlUJe3oxv0lEhUfVwidcHjrshZ_xrwMamIUd-ruwU6labrXNhYOnnZ5s5uiErQe_QpPjgG52XgJlsaL_7YI0TmiQYD55bgvo-Rrl_y9m4OJ4DBRaMPGEqP5KUC0MZJY1xdFWqFKZDpGmCxAL5BzUjHGJ7xYiCCcpfItILQhzB9IZEcWEysi4_pkGRyoBllfLsNyxca9TSjGoaYOYJQwnB3T4EZFS0ZST8aHRXNJ-WekjR4yIYQhaH5ov9yuEmfh7f4wL7t-muXYvVXxt52iEFWCW5cFVIYweolZ2UXFDPT76rvAZRYeyPwmnNvLvBop5U0ahIKC-VXzvA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=MMgMNVh8YvlUJe3oxv0lEhUfVwidcHjrshZ_xrwMamIUd-ruwU6labrXNhYOnnZ5s5uiErQe_QpPjgG52XgJlsaL_7YI0TmiQYD55bgvo-Rrl_y9m4OJ4DBRaMPGEqP5KUC0MZJY1xdFWqFKZDpGmCxAL5BzUjHGJ7xYiCCcpfItILQhzB9IZEcWEysi4_pkGRyoBllfLsNyxca9TSjGoaYOYJQwnB3T4EZFS0ZST8aHRXNJ-WekjR4yIYQhaH5ov9yuEmfh7f4wL7t-muXYvVXxt52iEFWCW5cFVIYweolZ2UXFDPT76rvAZRYeyPwmnNvLvBop5U0ahIKC-VXzvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به اسم ناصر نوری گوشت سگ به مردم می‌فروخته!حالا مردم متوجه شدن و مجبورش کردن خودش بشینه تمام گوشت سگ‌هایی که داشته رو بخوره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68924" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68923">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=i8Xp_aqq2jEq9lMwa9VamHgbrfVHT_ZsglG17PRf6UjhGbNXTdqb5EvKcDatXmoOLbl08mZtGw0TdW0zrni_FKfK5_rQct8x5c3tJ02kccABQHgGj-TeybTJHki9nOrYmZ7DZuwEoqTBYChSswxM0cG1q7ANAUcEfr5j1bfO5XD9QBZeF13pOyJhbcyWO5jIA5WX0DB6p62EkkQQevsGd1b2HU-qPRnbU0Mj-gvsl-IIfk1FtgySOA3lH3SEnUy0TfuGyJE_QPysFAdcyonacqhooG2WffzSqyjMRe7jE55p6vSgIRBA_F6EmxjCbwE44bBxDFv-HyLq0DznSf8tIoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=i8Xp_aqq2jEq9lMwa9VamHgbrfVHT_ZsglG17PRf6UjhGbNXTdqb5EvKcDatXmoOLbl08mZtGw0TdW0zrni_FKfK5_rQct8x5c3tJ02kccABQHgGj-TeybTJHki9nOrYmZ7DZuwEoqTBYChSswxM0cG1q7ANAUcEfr5j1bfO5XD9QBZeF13pOyJhbcyWO5jIA5WX0DB6p62EkkQQevsGd1b2HU-qPRnbU0Mj-gvsl-IIfk1FtgySOA3lH3SEnUy0TfuGyJE_QPysFAdcyonacqhooG2WffzSqyjMRe7jE55p6vSgIRBA_F6EmxjCbwE44bBxDFv-HyLq0DznSf8tIoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از سخنرانی ترامپ درباره ایران زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68923" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68922">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=J_SNjk9_dJrAy7x_tMvA2LqWNWIRwYDQKu49ypSHQEAIGUmh964R6gbqmcxJ3Bj9RrK6cnVHdgaIqDFWDlLoN5D9haq3WH4yvDegjG8tR1FMZ0nFiG6h2noZnHPLXR6H_A-37cihVwCp9mTc0USKO8jvfxjLs12U3X5P7t-KOpXqgOjqoCyDlWQTDgSgK5uSR3ri2-_EInm9UV-Ch5roOEdUO4mXWLb2TOjV2OsaeJ1QxxgT9CFRyaVll5FXpQ8I98xbfzsCYB0TJzf6ch4nRs2WKCIlDvyISjQaH5KOdYiJ7iRk7SLAbxKddD0xBh8pzvt_C2DpmaIWAieGC-7c_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=J_SNjk9_dJrAy7x_tMvA2LqWNWIRwYDQKu49ypSHQEAIGUmh964R6gbqmcxJ3Bj9RrK6cnVHdgaIqDFWDlLoN5D9haq3WH4yvDegjG8tR1FMZ0nFiG6h2noZnHPLXR6H_A-37cihVwCp9mTc0USKO8jvfxjLs12U3X5P7t-KOpXqgOjqoCyDlWQTDgSgK5uSR3ri2-_EInm9UV-Ch5roOEdUO4mXWLb2TOjV2OsaeJ1QxxgT9CFRyaVll5FXpQ8I98xbfzsCYB0TJzf6ch4nRs2WKCIlDvyISjQaH5KOdYiJ7iRk7SLAbxKddD0xBh8pzvt_C2DpmaIWAieGC-7c_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری به ثابتی:
تنگه رو بدیم بررررره؟؟؟ مگه مال ننت بوده که بدیم بره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=Nc4DbOe0X_FiF3Ubv_AEXOsv1MYIzwWNU4ogOwHkIXMdHrHYcBvX2M0UydybLtV_zCrNlM1bawtLWahr5rkt-XdPvxh_PMhudkBqZuC4L-LKyt8jOLSQD3t4PTdlVf24e-y0vccpDPM3cFv-RURrSBJraOGufiUhOQKpvxbT35RNIBO_49c8y5tWiJnNyCvJYbXY_RKIYdixPlB8EPCoF32vbkxjHNkl4mEykH5dAwP8Xst0uu3w1Jw84MI154rnYuP9JUgDFSbTz_mi5Kp9QKx2LHL3-IKYs6lBH6XeYQA7PMgIq-JkD5E2Q27yxlDJ53NealYZP3jRuQLK1Pfoyg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=Nc4DbOe0X_FiF3Ubv_AEXOsv1MYIzwWNU4ogOwHkIXMdHrHYcBvX2M0UydybLtV_zCrNlM1bawtLWahr5rkt-XdPvxh_PMhudkBqZuC4L-LKyt8jOLSQD3t4PTdlVf24e-y0vccpDPM3cFv-RURrSBJraOGufiUhOQKpvxbT35RNIBO_49c8y5tWiJnNyCvJYbXY_RKIYdixPlB8EPCoF32vbkxjHNkl4mEykH5dAwP8Xst0uu3w1Jw84MI154rnYuP9JUgDFSbTz_mi5Kp9QKx2LHL3-IKYs6lBH6XeYQA7PMgIq-JkD5E2Q27yxlDJ53NealYZP3jRuQLK1Pfoyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جواد اوجی وزیر نفت دولت رئیسی:
ما ۱۰ خط لوله بزرگ و سراسری گاز داریم. در بهمن سال ۱۴۰۲، یک شب ساعت ۱ بود که موساد روی خط تلفن بنده آمد و گفت امشب می‌خواهیم آتش بازی کنیم‌.
از من پرسید فلانی ۳+۵ چند می‌شود؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز را زدیم. ۵ دقیقه بعد دوستان از دیسپاچینگ گاز به بنده زنگ زدند و همین خبر را تایید کردند.
تا لباس بپوشم، موساد دوباره زنگ زد و از من پرسید ۴+۵ چند می‌شود؟ من گفتم ۹، گفت خط نهم سراسری گاز را هم منفجر کردیم. سومین خط را هم زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68921" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68920">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68919">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68919" target="_blank">📅 04:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68918">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=pqxN2dsy7VRR7W-5wbpztMjXay2xoolKTOm_Iun2d_e5HtHTHB45OWN3pHhtJJ4kSLoDr16Jf07r86cL7xLX4UQRl_838gY1UqKmRhL3oKulng1ZSWPoHChVFVEuAAwLKqIP1EuoG_wul-KGkyy4seV1lK_ZN9OO59IbUmlhVjra5o6seOXn1G_jNXhaKTiu9bNL2AYC8jH89drqzMdlzvE4EDrcUT6G7f_ys0uopz2Hd76hETXSBYBC7BXoFhnjzWIRct9a9Gia68cLgIqCbSSj0-uNRZwPDLQzzbPPGGIcrpUmF-SCe7H61XMFfqm2ZSjDncwNB0DQrkV-OJTkkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=pqxN2dsy7VRR7W-5wbpztMjXay2xoolKTOm_Iun2d_e5HtHTHB45OWN3pHhtJJ4kSLoDr16Jf07r86cL7xLX4UQRl_838gY1UqKmRhL3oKulng1ZSWPoHChVFVEuAAwLKqIP1EuoG_wul-KGkyy4seV1lK_ZN9OO59IbUmlhVjra5o6seOXn1G_jNXhaKTiu9bNL2AYC8jH89drqzMdlzvE4EDrcUT6G7f_ys0uopz2Hd76hETXSBYBC7BXoFhnjzWIRct9a9Gia68cLgIqCbSSj0-uNRZwPDLQzzbPPGGIcrpUmF-SCe7H61XMFfqm2ZSjDncwNB0DQrkV-OJTkkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68918" target="_blank">📅 04:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68917">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سرعتی.npvt</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68917" target="_blank">📅 04:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68916">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q69eb39--teW8H18w15aP3OTwd6fNORpA9u3qiS39gcFKHpoOuBYnKhN1_wJuTgaUIar8doVoCrMw7Bk9ERY3k8im5AbgvkkyLwupkM6pizVSclwC8QA56TzgM4AwgB747Od7guEodjq9DGL_5ZEAgArsc3Rl8MqMkLvZvH7XxPihg9jr6OP6HFUzSuurkPSGNwYHpjLZUcKtl-U4IvhBSjOQcNej-stHm9xUZTRFW8hMy7O7RnxqcVEHG5d3jAHW-Jv7rb57ZA-XcvPC0ZUTbWqHnGOxcONYfknxWsLV2b-4lt0v8i-ehjl2oGZz5rHC1rFd6Ii2fs-QSKS_i3LpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ پدافند تهران به دلیل حضور پهپاد های شناسایی آمریکایی ها فعال شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68916" target="_blank">📅 04:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68915">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-2jujF3b7RvOipQzm5zLpQL2wtrgmQjDh5J0g12v1F2s6iLJU-A_KmFrbGTQEokbk8xJpwPry54DJInnGvT_97xcM5ZL-Qw585oZFOSzU1i0nAgONewvYQkNrN0herbQGsPoTWOeIVAsrWwaS2Jt5-iPVo_lWOmBMoEH0ZULhUwihClcains0Plqu1m3kBqrBpmvh7VgPDACC-HBmcG_pPX8LUxxiZRdJhcLizRDj2sulkNrjiOWyKt1x4VxNcLXtktVuOMDAGn75I4vBiCojZQndhkyS4UPVsVTLcJITUy0nxYoQwhLGnxoZGgRsn5RVg07_NuF6y02flVICi8nA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68915" target="_blank">📅 03:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68914">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
برق مناطقی از بندرعباس قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68914" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68913">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwUYXQHhTIZaAbR9Odfn8MaqXMBYELMlnNMlCXm9AYCLAtKIU8jDRqsAK89fyxnFkVLsQhpucnBYzmmZwen1A6k9u3NJRoU1ZWAmQM7Qwi3GC6lcZepRcn3pqj41QWvdlCNM8O8RYEHPFICeZ46IvG4SRA9HrZNpvGs2T3ForNyFXWCnKYfIGLxFVNHE5w4A7H_tHt-6K9UkgpO5Uyz1Qi62Lf7HbWspfST2lbCxRs0f-hNaeBLVMi4_5XLNJdWnn1itst8Nl1M6zJLyGrw6GoGBKGgx2GNsabyuKPFGaK3oNzbWmib_g1vUyP9Q3KdhOfu3b-LV1vSXRdzAn3IU_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بندرعباس؛ امشب  @News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68913" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68912">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🇺🇸
منابع آمریکایی: ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68912" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68911">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=m_o3sGcWYwC_v7QAe-6ZhYyNgg_ooA7NcxtVtPHYvHVVbTnN7jnskrMrEu9tnH0HRHIlFNJKKGeWlKgWTEVy3vjaXJ8cenSM4hsVEq-1c19JFrgu7bfGAovwi6zVkuo1l1BLp_R7QAjxuDQo5PxVQZ4L84GJOH5w3TRLngJ7FRSI9TaXHPHJLYCvwndfUE3sAP8E3k3LG1qD13lRXs4itm_vGuKIDZCLuFPYeUBenRcl4P4ARXghVbdXcDPgnAN8ZwOJrVDyxXD_qfUIwNNvTFg-IditMHJ1IhGZGNUpo55rzxCT85CI8sPBtu0YGfn3dRFPDCKxvHMzGEKkn4RYCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=m_o3sGcWYwC_v7QAe-6ZhYyNgg_ooA7NcxtVtPHYvHVVbTnN7jnskrMrEu9tnH0HRHIlFNJKKGeWlKgWTEVy3vjaXJ8cenSM4hsVEq-1c19JFrgu7bfGAovwi6zVkuo1l1BLp_R7QAjxuDQo5PxVQZ4L84GJOH5w3TRLngJ7FRSI9TaXHPHJLYCvwndfUE3sAP8E3k3LG1qD13lRXs4itm_vGuKIDZCLuFPYeUBenRcl4P4ARXghVbdXcDPgnAN8ZwOJrVDyxXD_qfUIwNNvTFg-IditMHJ1IhGZGNUpo55rzxCT85CI8sPBtu0YGfn3dRFPDCKxvHMzGEKkn4RYCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بندرعباس؛ امشب
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68911" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68910">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
دقایقی پیش صدای انفجارهایی در قشم امیدیه و اندیمشک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68910" target="_blank">📅 03:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68909">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=OktA7MV-hXl4OOQf9FkJp9xZtHGCQBZK2HfmOMr9XsVSTrVre93ky-2NS8025mX_gF5CVd6FN_WqJ1KolpQuyHfVqMiBPuqo7KP0s-p1T7XmMeyjRMRrI0XjwvcyulcVFUegs-_8s_cMq1mM6-GAWqkzX_l-u4T78viruqTaYvm10yuXW7qofefHmFuBBlPAQk7dN1hc7uaJRCeihme28CVIeOEq4Nz5HOGv1-9DQjkvqw9uGKq5eyn7Lqqh7iL5dyaiB3PY7qp4y7-n_UUyHNmuVuehEV83qQ1e2qPZRu8yra9oAiin3jX1_7Yk-aHwMLrw40-lrHTT6YVC6Wvi7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=OktA7MV-hXl4OOQf9FkJp9xZtHGCQBZK2HfmOMr9XsVSTrVre93ky-2NS8025mX_gF5CVd6FN_WqJ1KolpQuyHfVqMiBPuqo7KP0s-p1T7XmMeyjRMRrI0XjwvcyulcVFUegs-_8s_cMq1mM6-GAWqkzX_l-u4T78viruqTaYvm10yuXW7qofefHmFuBBlPAQk7dN1hc7uaJRCeihme28CVIeOEq4Nz5HOGv1-9DQjkvqw9uGKq5eyn7Lqqh7iL5dyaiB3PY7qp4y7-n_UUyHNmuVuehEV83qQ1e2qPZRu8yra9oAiin3jX1_7Yk-aHwMLrw40-lrHTT6YVC6Wvi7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68909" target="_blank">📅 03:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68908">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=UD2f28DFPv6f7iVIcId4le3CTkPB-AaixbvafHyvdN0ceAGXygiJWcXOqY4v0zoyR2iZ2Ftby9eKj--oVauPr8oh7-As8ZSUQ-VyjP6irKdKqfXhDR4_tUJIG3Ype38ou3_6mQWTAWNpL1H67oD-eosU35eer8MOAHghBdfdItRSPgzdkcM-cqoiWA0u0dFSk1hEnzvNs0DwgxuAaQLZfNTgAVz-MGUpJka7a4sdWMA7qrAFyoEiwQjIgijuQWML5tM3z-HQIBFF0D6K3VmsRcKcZp7z4a0Kq2W9_rfOBoim-KWYO1vkn3qli50M3vy7jC0xZTLGHieNahJVBgqpmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=UD2f28DFPv6f7iVIcId4le3CTkPB-AaixbvafHyvdN0ceAGXygiJWcXOqY4v0zoyR2iZ2Ftby9eKj--oVauPr8oh7-As8ZSUQ-VyjP6irKdKqfXhDR4_tUJIG3Ype38ou3_6mQWTAWNpL1H67oD-eosU35eer8MOAHghBdfdItRSPgzdkcM-cqoiWA0u0dFSk1hEnzvNs0DwgxuAaQLZfNTgAVz-MGUpJka7a4sdWMA7qrAFyoEiwQjIgijuQWML5tM3z-HQIBFF0D6K3VmsRcKcZp7z4a0Kq2W9_rfOBoim-KWYO1vkn3qli50M3vy7jC0xZTLGHieNahJVBgqpmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
لحظه وقوع انفجارها در تپه الله اکبردر بندرعباس، دقایقی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68908" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68907">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYRNW-1d3eEouQl9YHWZ28qn4HXzgcJ_RQZzo5VCHVtka2Er64CqzzaDfEBb4r8wxluUYOdeBvwhOOfPbl5MGqt0pbn8OMmVv9fn7Xq2n5kIkaEzDPG3GHiaDj9gD46nvlEtFTldvPOjLb0MN_SqOAFSgTlRNxSD9LdO5OmVppGWs47kc3IlR4vNsD_RZ0-5YAug7dOsPquUjkSHWWpsvuyQquiDjbzx6E-0t9O-r4tJn4jgYaIGIxGnisJx7saxvQ4VpKirTHIgV5ZGBXrtFPB3K8ZoGReO06zH4olZd1Z7jEzZMOrqFj0pahVuMeGJeKGkN5mi7hQ3aOphY_V6LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68907" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68906">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی  @News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68906" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68905">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=cqSvg2wLl2Px2UCbklIP11txhTCGGRVuO0uf3uw38KAH6Ksgk031RoRoAJySt4LsC5w5hkv1_GvnOzIdkwqFW3IMLYvEE8KAOZRyyJtSS1iwAFLlufBudxMD03wmpjqPjx_UW13TDgKIhl7xxxBuU05vLc0aCb8tvUIc14OZeo4s78H6eoxA2gPM9PCW4-iF4ja0sVFYq3vLJQNxjVb55opoxwhm2WaIDNidD9gemVBZYyImp6WzRfGOK3hYlzbJ1mHIPsNy7lDFQo5ttvYDdOZksD1EdOuJoT5c73jNdumYbaYAalZ7GlGRtQnbbRrGY3-pWfd7rav7MESUG5yETg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=cqSvg2wLl2Px2UCbklIP11txhTCGGRVuO0uf3uw38KAH6Ksgk031RoRoAJySt4LsC5w5hkv1_GvnOzIdkwqFW3IMLYvEE8KAOZRyyJtSS1iwAFLlufBudxMD03wmpjqPjx_UW13TDgKIhl7xxxBuU05vLc0aCb8tvUIc14OZeo4s78H6eoxA2gPM9PCW4-iF4ja0sVFYq3vLJQNxjVb55opoxwhm2WaIDNidD9gemVBZYyImp6WzRfGOK3hYlzbJ1mHIPsNy7lDFQo5ttvYDdOZksD1EdOuJoT5c73jNdumYbaYAalZ7GlGRtQnbbRrGY3-pWfd7rav7MESUG5yETg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68905" target="_blank">📅 02:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68903">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=SykGWl0L1GXpQUhQRMjKPzzixT5LoQlRrXzcX6XbZFizxth2lZOC-saWsZZyQVNFwY3-U0LOPWWY-SOVtLn-yZ6tYnL5G469xhofUuFff4rDQb8vpmRmZXrEgNkzCuUy-qm-jVhGAEU0leKv02zupkFqNnoRe29dfUX-f7Na8G3p6-xIhQrGg-UCp6UHKp7sMjChy0E3XBjOzswCQEgLeqSn6fJK88JiIEFIwjSXJt7dE_atpLxlUC9_pPbmPSV0aa95OeVdMf5kDfurzPSwzhQE0hp6dxoDTTYHEMBLl4vK0p-PLkGmdzExpc0EFpcFH-QRM_gME0mO3NnEkfRz0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=SykGWl0L1GXpQUhQRMjKPzzixT5LoQlRrXzcX6XbZFizxth2lZOC-saWsZZyQVNFwY3-U0LOPWWY-SOVtLn-yZ6tYnL5G469xhofUuFff4rDQb8vpmRmZXrEgNkzCuUy-qm-jVhGAEU0leKv02zupkFqNnoRe29dfUX-f7Na8G3p6-xIhQrGg-UCp6UHKp7sMjChy0E3XBjOzswCQEgLeqSn6fJK88JiIEFIwjSXJt7dE_atpLxlUC9_pPbmPSV0aa95OeVdMf5kDfurzPSwzhQE0hp6dxoDTTYHEMBLl4vK0p-PLkGmdzExpc0EFpcFH-QRM_gME0mO3NnEkfRz0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68903" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68902">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzZoPBXfQlglng7_gTOdqcv8-hJz269RjNTkaIlaf01LERuHAG7AfR9eoy9IHyO0P6y9nPDZLAt2d6M_WNt59Xe6MFIp3D-sMaCUm-9TwhCgMUEEAFMrC3_RibJCG0SXBKVlRIA78qFIQRS7JyR-wX7_G-ju0_f9gO5m_eP4iNNKj6L4MVHIsIBcGP2UsaFQVDZCHcs1KO6K_FL05USHcOgqPYvbRWSqZyEzG-d61fNx9Gm0BbIx7SJXcl_ENVf35_CsgQvM1tbDW2PnRj7r-5oMJYlJ9wsCnprPDuGR2SSqOjqTGBUVM-T0VewpVjw8k2VPwPdNli6SXdODRkaXEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی امروز ساعت ۶:۴۵ بعدازظهر (به وقت شرقی)، دور دیگری از حملات شبانه علیه اهداف نظامی ایران را آغاز کردند. این سیزدهمین شبِ پیاپیِ حملاتی است که با هدف پاسخگو کردن ایران و کاهش تهدیدات سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68902" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68901">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدیدی از حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68901" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68900">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
چندین انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68900" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68898">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=TIEV7kh9bcdozWKSzQnKXMBqGxZNwIP1PbUtgTbcWL39VvMfHOHfBMQmXaAUVUj1TklL7GU8sPrxX-H4wmktfhLbEZbngOAowup1z3adDZXTaQ4_QKVxh5DuL5Ut8K8qjanPMRmfK1PU9oASaGrOddEgrs8Tx7z0MHr7iW94FreHyOk9vzDjpqPSWBMWqm1H7LiKoprVIRpYT4sub0DLvJ6eGXN_aCbHroxRJ_cpT7srB5QR7zL4Xl-rUaXSfpuYdKerpEyfMwE10mv4-9k5lcW2aP8Sp2z5TDE1WdQ1ZgneTqdjArmfiR4025rI7pPrcDADkezqwaM-Jcl6zk377A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=TIEV7kh9bcdozWKSzQnKXMBqGxZNwIP1PbUtgTbcWL39VvMfHOHfBMQmXaAUVUj1TklL7GU8sPrxX-H4wmktfhLbEZbngOAowup1z3adDZXTaQ4_QKVxh5DuL5Ut8K8qjanPMRmfK1PU9oASaGrOddEgrs8Tx7z0MHr7iW94FreHyOk9vzDjpqPSWBMWqm1H7LiKoprVIRpYT4sub0DLvJ6eGXN_aCbHroxRJ_cpT7srB5QR7zL4Xl-rUaXSfpuYdKerpEyfMwE10mv4-9k5lcW2aP8Sp2z5TDE1WdQ1ZgneTqdjArmfiR4025rI7pPrcDADkezqwaM-Jcl6zk377A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران اهداف توسط ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68898" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68897">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=Xin5a13Tm07H7kfK2HIua7P9TIdwsk-rtS53kTI8pG6YiPvf-H2m2lQ3uVoxPMULuuJva93VoTmPStsSbGIRwzI63-tHWGVe0uHZRMnmCBkiBjMGjz7-1wdeTjU4GiNmDvPM6IJvfv9S13y60ryORVE5PFTcihmywJJgpQSLBWGS_EW4mFo9x2bX2TOgkkNCFn7tthQkCIWmmAU8u515a8uL1jnkWxJYR8576OYa-7_0GtQ6g90IZZ0F72vqTI2RHDiqpTwiAM6b1cPFJr1VsMjAGhVcz6ODJnzRhOPfk6yw9JS8kOOzzXCJNFeHI-sumE3GhJ_j50tgdlaNhpF9uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=Xin5a13Tm07H7kfK2HIua7P9TIdwsk-rtS53kTI8pG6YiPvf-H2m2lQ3uVoxPMULuuJva93VoTmPStsSbGIRwzI63-tHWGVe0uHZRMnmCBkiBjMGjz7-1wdeTjU4GiNmDvPM6IJvfv9S13y60ryORVE5PFTcihmywJJgpQSLBWGS_EW4mFo9x2bX2TOgkkNCFn7tthQkCIWmmAU8u515a8uL1jnkWxJYR8576OYa-7_0GtQ6g90IZZ0F72vqTI2RHDiqpTwiAM6b1cPFJr1VsMjAGhVcz6ODJnzRhOPfk6yw9JS8kOOzzXCJNFeHI-sumE3GhJ_j50tgdlaNhpF9uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین به اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68897" target="_blank">📅 02:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68896">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3266056eac.mp4?token=G9q8p4tWxIG-2uAEF6fQ6bwL1Qe23b7DNZ1TD3r8GyPIsd0fmlZ0f25AtK__kIz97NACs56TyKNgLa3d6XsN5zhm3cL3fwrPlFD2bUNa7NzWHF8-z8BwTDEvjqmiK10rZyP8vZztPuasQ4BOctncS9C2U-D5LXFESOnbUo8iJ7XBxqYNhiZPHWGJZvw5Ikvg9JnWjcElg5zTkhcnrd8nL5QgyhGvYoQ4fmZRKM2MX0HLdpWldJ49qw45NJ4Xt5P144KVmGeGiO1jDJ1UwPOc6wUZBID3jsmdKhf1AX9XTdP8cdYVWxwMRITheDueS6Zw7PP2wDDL7MxxA2AMl8dLHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3266056eac.mp4?token=G9q8p4tWxIG-2uAEF6fQ6bwL1Qe23b7DNZ1TD3r8GyPIsd0fmlZ0f25AtK__kIz97NACs56TyKNgLa3d6XsN5zhm3cL3fwrPlFD2bUNa7NzWHF8-z8BwTDEvjqmiK10rZyP8vZztPuasQ4BOctncS9C2U-D5LXFESOnbUo8iJ7XBxqYNhiZPHWGJZvw5Ikvg9JnWjcElg5zTkhcnrd8nL5QgyhGvYoQ4fmZRKM2MX0HLdpWldJ49qw45NJ4Xt5P144KVmGeGiO1jDJ1UwPOc6wUZBID3jsmdKhf1AX9XTdP8cdYVWxwMRITheDueS6Zw7PP2wDDL7MxxA2AMl8dLHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بمباران سنگین اهداف نظامی در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68896" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68895">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از بمباران سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68895" target="_blank">📅 02:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68894">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
فارس:
گزارش‌های اولیه از سقوط یک هواپیما در آسمان جزیرۀ قشم حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68894" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68893">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68893" target="_blank">📅 01:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68892">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نیویورک تایمز عملاً تبدیل شده به فارس و تسنیم
😐
آخ که چقد این چپ‌ها ولدزنا و حرومی هستن
#hjAly‌</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68892" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68891">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68891" target="_blank">📅 01:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68890">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bp0uGZF8m719TwKHYwSfYquJwZxmfRYFQk8tZcPehM1fz1c0FEE5eVnSr5z-sZ2_X9ZwXXnUXzlfnoEKsdTkdP-Q5_T55aKluzNzt90u4DhTf7wXo5qiT67PlaoN-oqJNHIXc-K91XQgpjf6oHzRTpBU7MLE34OS8TjLt8AKkO7pX--TZViSJxl-dHxvJoZZPCHc8e0DcKyqrYJRdBp6azZ3KOaKN9J5C1CCBwcsfxk5LY0NtNbRT1o5ereKW5Jdan1jOdkbQq8NbmMJJvQoXesEh8u5GRrVs5c2eN2PpqYbl5zoxrmmNffMdMejBnJjofLUe_VaLBXz_De-vdVoOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:
لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد.
اگرچه ممکن است این خسارات بسیار سنگین باشد، اما با این حال، این اقدامی عادلانه و منصفانه است.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/68890" target="_blank">📅 01:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68889">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=khcNebvVFc4vFxYAoZrlbKufLWZ14ZmH-TFAIb3ze_r9D4E1A13vSSZT6DJ24fzSyII1TFwgYgkDnY5CJ8gX2EyHWnJUvAgUYXKmzQRAusfgeQhVC7RUK4Sqs8m-fQubEdFdV0WvIwzZU9QWJAku67BmOSTOSBhE8jfVn73XDeVZTSs89EGI3RR7SX1cl38xDHtMsNPAje5LCFUgvGSAQRMqpjkQiODN-NjzvgYlJhUR0fQZyl_Pg-yWkx7FFCKLoi3YKX2lrKTmdVFGF5XUA1rXY0rIQJBYVB78bfv9gS1r6QJG1eoLRJxqEBx2eMDxnCEBHwIHVzNxoWI1JoI4Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=khcNebvVFc4vFxYAoZrlbKufLWZ14ZmH-TFAIb3ze_r9D4E1A13vSSZT6DJ24fzSyII1TFwgYgkDnY5CJ8gX2EyHWnJUvAgUYXKmzQRAusfgeQhVC7RUK4Sqs8m-fQubEdFdV0WvIwzZU9QWJAku67BmOSTOSBhE8jfVn73XDeVZTSs89EGI3RR7SX1cl38xDHtMsNPAje5LCFUgvGSAQRMqpjkQiODN-NjzvgYlJhUR0fQZyl_Pg-yWkx7FFCKLoi3YKX2lrKTmdVFGF5XUA1rXY0rIQJBYVB78bfv9gS1r6QJG1eoLRJxqEBx2eMDxnCEBHwIHVzNxoWI1JoI4Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
مقدار قابل توجهی از هواپیماهای باری نیروی هوایی ایالات متحده (مدل‌های C-17 و سایر هواپیماهای سنگین‌بار) امروز از اروپا به سمت خاورمیانه در حال پرواز هستند.
برای توافق دارن میان
😃
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68889" target="_blank">📅 00:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68888">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
دقایقی قبل دو فروند موشک در جریان حمله  آمریکا به محدوده روستای مسن در جزیره قشم اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68888" target="_blank">📅 00:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68887">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b133a06016.mp4?token=YUGuKYu9NtPVM2efQ0a8jneySZxHW-96XrR29pLXSaLeNKZzaWUhTojQUAsa1aIxOWktLjBa6hq6UgFObxF9KX6_JmdzKQ-95f06HAACgP7ZRIE46bXBmc4ngz6-7B6UcQUvQjn4w-C5wHlMIWX6Hw7-GNX9mBgjzbzyHdnPXuBEfljfknbeLhXKFozhc8Uwi1fqka5Bn0myhh95lENRynJkZm83yPpwEvPfV5Qs7MN2ID9BkR6ftrIhI4rNFFHCEYuxdykYdmEU0VU3ZonKX9BSjhTkmNGiK-LqjMc4s4IhGFarQEsK0Xlw01cteJpxF04rrgBQcgKsWaMc8X7l2Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b133a06016.mp4?token=YUGuKYu9NtPVM2efQ0a8jneySZxHW-96XrR29pLXSaLeNKZzaWUhTojQUAsa1aIxOWktLjBa6hq6UgFObxF9KX6_JmdzKQ-95f06HAACgP7ZRIE46bXBmc4ngz6-7B6UcQUvQjn4w-C5wHlMIWX6Hw7-GNX9mBgjzbzyHdnPXuBEfljfknbeLhXKFozhc8Uwi1fqka5Bn0myhh95lENRynJkZm83yPpwEvPfV5Qs7MN2ID9BkR6ftrIhI4rNFFHCEYuxdykYdmEU0VU3ZonKX9BSjhTkmNGiK-LqjMc4s4IhGFarQEsK0Xlw01cteJpxF04rrgBQcgKsWaMc8X7l2Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امشب تو میدان ازادی تهران
زیردریایی سپاه و سامانه‌ موشکی ذوالفقار بسیج
به نمایش گذاشتن
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68887" target="_blank">📅 23:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68886">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGY2iKBeZqiqmU4XsYY9bDW5drU4gcDgR43ROKVtO7wIV84WW9BDJVaEj0ocyEP2rbHOGFd0iuzIeglJnOPNy5ogDGaKn7NvLg-h-GCrWkC-_510Brd0f49VlapDwb513XrrrEleLGQejzCmzFxVT62eIJWP7WQvazYi4F7gnngm8T0uCoVQ5PIqyCrTtwIX5Y4_KI5jfV_IQ3DWxru5-lRLyZOUt2ccYymG5wbR6llMDOWi-DXSHCQUppIxUgBuD533qNAEtt9VgDcRr5u9iJzs-_hLZ40VxyR0dlYy744JgklARTleTPY5Gz7acSEq84HWDYPXQ_250T5h7rATxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک دیپلمات آلمانی در گفتگو با شبکه «فایتوکس» (Faytuks) می‌گوید کارکنان سفارت این کشور در ایران خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68886" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68885">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن  @News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68885" target="_blank">📅 22:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68884">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68884" target="_blank">📅 22:49 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
