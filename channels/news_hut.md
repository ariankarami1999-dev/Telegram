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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 00:45:30</div>
<hr>

<div class="tg-post" id="msg-68998">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_grE6OHQBPvQvezozuJenYYGsYRXjuQknrzZPEc9mW5gvXTELXK_aSk-YtmRDlCjPIsst2tPyrdAJbInR1JWlIB3UvcdiKT8wUGxsA09eBBV-XHRhZyehHMmjUDfYlqQEQJKG_KsdC9Qb8ufsn4KCdU2EuVTn_KdEq8pmmSoUqv8U4ujFPyKYku8IKjEii_lBaFJvgfJ0p9aAWSJUjY0vi9Z2rcvjaNYOYTGmpRh09VE2543mmK4fnwnoiesIjP4TR5rjWdQuc6mALXba7Kgcq2d8wV0HjNT_vdDNCy_J5bWpw_VqKYtZzHBWfi5foN-eOGT8fP3E2Dvj7DsUcJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان آمریکایی هم‌اکنون بر فراز خاورمیانه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 611 · <a href="https://t.me/news_hut/68998" target="_blank">📅 00:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68997">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
اوکراین، یک کشتی متعلق به جمهوری اسلامی را در دریای خزر هدف قرار داد!
تاکنون مرگ یک ملوان در این حمله تایید می‌شود، رئیس جمهور اوکراین می‌گوید این کشتی حامل محموله نظامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/news_hut/68997" target="_blank">📅 23:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68996">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/68996" target="_blank">📅 22:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68995">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1C3-VgQcfcryqgOkebK_uQ365IIOulvJo-pLPGzmcngvq6gxp1Ex58Hfgta2j1xmSjLUHa_-E09v8344vGZhO2k5rDxbCwPLHG7lJ7aQqNZXYElPU-Lk0YA9GcJYyq8xMmN39iGmoEnE_tsIO1flK473XF3cPR-jqEERP3r7f2RaPP1-JejBJXklxqXGIa5eWLkMzzhJo9J9AE3xkElaN__iOA4Viec5x0uGRWfqGTP-JE8awT5hpXZ7pBrRUmpZdETrcqSmTZGuaJn13x6uWxiA-F_5SoeVuAp3SMnBSHp0lxNf4_LbSi39qte2zIazTLnqamE5MYVlB9VbEnb9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در گفتگوی تلفنی با شبکه فرانسوی «ال‌سی‌آی» (LCI):
اگر «صددرصدِ آنچه را می‌خواهیم به دست نیاوریم»، «قطعاً» گزینه ازسرگیری جنگ تمام‌عیار علیه ایران را مد نظر دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/68995" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68994">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUc1DqU0SAG3Uh48ed3v2uA0KRGQPwuHqVSNTxRri1oMwOgi8CNC6Ys20fKWryVrVCt1JGDJc2eXDvxQB3CiOIn5_qmiArDnVI0o3uN3db95SDRnjv0V_J3aO9B18yltNBgTNsz6syH56RvvFsmmWZiSJtZNTFAj5QhNdDPpZ9AN86vurG6ELLncSPKVcs8iy_sMabdUuSgjzeDQqvj79Pd5WO0hkhKkDu3w02m65vozczk0xQs4vay7TtG85eK3iI43-Gfx1fkzGmR1z1jWuy9ATegvdJPqZXEpzTl-xFu0TTVVk0gO4IyLsfmG1xvCBfHjRSuwsdzjJtOOwz3pOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:
رئیس جمهور ترامپ روز جمعه به ارتش ایالات متحده دستور داد حملات به ایران را متوقف کند و به تقریباً دو هفته حملات روزانه پایان داد.
این تصمیم در حالی گرفته شد که مقامات عمانی در تهران مذاکراتی داشتند و گزارش‌ها حاکی از پیشرفت در جهت توافق احتمالی برای بازگشایی تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68994" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68992">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68992" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68991">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxxS86Te4H1EutF0Ly8bwwYyp-gHoOPdqka1mKR9IAfq0gVvtFtqW6J_0Kp-4zMyLlhRvZRs1mZcvBYm-l1-rgSKq5UGs0FhZ30MDxSq_tYG9H1c7AIWSZkjiMltjhdZy8hbgt3m1bAmll1QOC_lhQ9dEZ04UdeX00IUM10sxUQX-CwioiIcTrNXSUsflvDcHPwcS0pVtgH-UaH7cx2xgxJFk_7EowM00WSpNi5d7fygb-D5YguuYtKTYcFA0pYqCXNwA915GM-ue0o80mb6zDh-LGMFOOGKdIVbgLzXk-Mi5h0pZwFsAs-Jweui1kEaZoVc9f_XXdrBnHXMr-KJjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
باراک راوید، اکسیوس:
آمریکایی‌ها دیروز برای عملیاتی گسترده‌تر در ایران آماده نشده بودند، بلکه برای حمله‌ای تدارک دیده بودند که از نظر وسعت، مشابه حملاتی بود که هر شب در طول دو هفتهٔ گذشته انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68991" target="_blank">📅 19:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68987">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68987" target="_blank">📅 19:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68986">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68986" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68985">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSh0BmAI8gCgZd5aEPST_cvNOcTmi6Za82EDj4YQqcn1easmc7RPhbnzmSFe_ZeRnCOpBhQm27OPP7JXKFckTHBOsAk5i_jj31LvWhBVcnm_DiN52fFbDlXcn0f0GLgRYcMeiYpq9JeVHdiNMyzv4rjbTz2FDXo_afAIQ3o6aEDJN5QdnddwnJMJExQlSag8udZsA3avOYFM7m9fdl0dyPpZB5yQwpRTE8MHWzOzpu3KNj-acpX3jfidwTs7yXyemTEeWbOc_cc7XwBKVh7MiVUqthZ_Mfnltzpb2sSKpxNQPkrViDlcee9alSlq_uOPT5JtIARiMa2lMPDnmB9_TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
وای‌نت:اسرائیل انتظار داشت که ترامپ دیشب ایران را بمباران کند، اما در نهایت از اقدام علیه تهران صرف‌نظر کرد.
اسرائیل روز گذشته را در حالت آماده‌باش برای یک حمله بزرگ آمریکایی سپری کرد و انتظار وقوع آن را در طول شب داشت؛ اما سپس متوجه شد که ترامپ در حال عقب‌نشینی و دادن فرصتی دیگر به تهران است.
قطر و عمان فشارهای سنگینی بر ایران وارد کرده بودند تا پیش از وقوع حمله‌ای که تقریباً قطعی به نظر می‌رسید، کوتاه بیاید. برای نخستین بار طی ۱۳ شب گذشته، ایالات متحده هیچ‌گونه حمله‌ای گزارش نکرد.
یک منبع اسرائیلی وضعیت را این‌گونه توصیف کرد: ترامپ تمایلی به حمله ندارد و تنها به این دلیل به سمت آن متمایل شده که احساس می‌کند دیگر گزینه‌ای پیش رو ندارد.
ارزیابی اسرائیل تغییری نکرده است: احتمال دستیابی به توافقی واقعی صفر است و تهران تنها موفق شده برای خود زمان بخرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68985" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68984">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68984" target="_blank">📅 17:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68983">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68983" target="_blank">📅 16:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68982">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⏺
🇾🇪
بیانیه نیروهای حوثی:
در پاسخ به تجاوز آشکار و جنایتکارانه عربستان سعودی، نیروهای مسلح یمن دو عملیات نظامی دقیق و موفقیت‌آمیز انجام دادند. عملیات نخست، با استفاده از ده‌ها فروند موشک بالستیک و پهپاد، تأسیسات حساس شرکت آرامکو در جیزان را هدف قرار داد.
عملیات دوم نیز با بهره‌گیری از تعدادی موشک بالستیک و کروز و همچنین پهپاد، تأسیسات حساس شرکت آرامکو در ینبع را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68982" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68981">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68981" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68980">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68980" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68979">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68979" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68978">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlaHPhx4-xCMeKVcpbu59G1NJ3OklrZv48iCBFj9Mf_i6BznpNgJX_hQyyUR-wq4rrx6qq1ebRPLm0IeXHeeXYvrAw6UMjF0zsfgls2MHhFtABSQZ-tyXHvKpj4AVU44rOnv8W-kzOaKBELt4LcbHciMWgJKEqGk6Ifb7us2ukizxFfDqDSWlnKnMGOqI9iuUALs1h-q7g8OpyiqC_G1XCzTtJMavgYnI0dbehOERq3veXJ5eTmTe8zIyhNh7sj5a9I2RCaEBC5ri3pLDo_ojF0zSL83ZmM_e456Udpc3kCWdeRGRM_7d-9c3Xh-vPeE9SCSuTzd8egwMv3gZjw5fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
در پی حوادث تنگه هرمز، طی مذاکرات سوئیس تصمیم گرفتیم برای جلوگیری از سوءتفاهم‌ها، یک خط ارتباطی مستقیم ایجاد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68978" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68977">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68977" target="_blank">📅 12:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68976">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvGz0K7XpgvaQxFRyCyWXWQ3UDmF4h2gMS8A1As14glMxi16DFJt6PIRBq07ue1q3VjRslbu2mlMxi7ekco8ErKa36ZqnY_TN9OXJkfPs-3sYr6dttFrR4GgD-EJDpWnXvoSVQAP1RCEyoFH3Uml-QaipD0ZxUXvLaTBXKpG_jyWQlMuceOvFrdxYVzYdJaWKg4Lt5AHxCXLx1YqC4cf3Xr8BGrgll2QIWAckzpbGZ66V6MRJeAYCU3NshkCzFB0Hi0saPb_TtZ884Gd2il1a9vKkIMNB9QqBAp8-J4MYj-Mcz-3V0lM1ctisfPr3fcS4NDlwpY1pnId4X-CVltUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
سازمان عملیات تجارت دریایی بریتانیا گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68976" target="_blank">📅 12:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68975">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68975" target="_blank">📅 11:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68974">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">💢
ویدیو وایرال شده، پشم‌ریزون از گات تلنت
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68974" target="_blank">📅 11:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68973">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68973" target="_blank">📅 10:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68972">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68972" target="_blank">📅 09:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68971">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68971" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68970">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بعد از سیزده شب، امشب جنوب آرومه و خبری از انفجار نیست، و متاسفانه این آرامش، ترسناک تره!
#hjAly‌</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68970" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68969">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfDvVr27cUJdvy4PpQ1fOk1coq49l0JfQqbOznOUWBhIMfi1D8q_3c8qdAVmCC06Y3RP9OO-xd55CmeQp5O_T3jOcslpwrX8JSstQTDer6JRE-3drbQ7V89MMdxAGmpHSMy_an31_rSHzpaaCTdxGqI3KAppLG0PfNJ3F2yOOAjiiB1FvwGFT86MHDlJ4P4WJrmhrk33zT7h5D5MIJ1Emx2nDLYMlXdEClaz4gvpGtyUc7p3cus6LSQ0FaykhWiVaSeUIW28NUbZZCrxP84l4hPAmCgJlI-zXudpLJYoBwON3HS6F-5ckxTKeWYn5NDyysfw1cxpyZwKcBdzHw9i_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه فایتوکس به نقل از مقامات اروپایی:
در اروپا این اجماع رو به افزایش است که ترامپ پیش از کاهش تنش، آن را تشدید خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/68969" target="_blank">📅 03:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68968">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/68968" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68967">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByKFsJ6Q-fA7hXFjU7Pl1pYC76xlG-Gx6DrkMt0Jbh-agmNetaK29RUqZ74I1nt0IDgNPRpcVnR5o__3kq5YS2TBjevLyexPDTqQhDxjargNIwZEqlbg2zRxdCf4EWaC5OMoYDoIBhxyJed2SC9cTZmETJCmJVtFy8ofRN9Oo9aCglsEgNkdGhA7NCjQzh8X17cebgv-lsJzYHkferD1NVt8u6MIta2h9c7WUxVTaIfPeoJFsnODd7MbL708Hd-TCEzFGOQ4aIHvHdHgZtV2sSS8gml57SrtWXFza4bszGlt2DdlGj9oKAEKEXoW-L1JS0g1z2A9BCokKqYyYBxcEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ارتش‌آمریکا: یک‌کشتی مرتبط با ایران که سعی در نقض محاصره دریایی داشت رو منهدم کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68967" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68966">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITai6oi1kBPTJwLRTBmVhDhrzaCsgGuuGETgwvhB_bPj3X1hhx4cclQNoQgI5JT3mDPDCr_aPA8to3usd1oWivcPkNxuu3UhStyqSOw3IYq2shU7wRNQpE5Gmkybs5Li8Dtf969kL845DOXguaXY3DORo0J5zVxyqXq3mRzeKzxrnVS-Bc3wjNBr2P4ciMjgVZTuz8aeKTIACq8hwfNgYhSAFnOCc9rjuMxhT5xsjxes_zC4jEHy8Kiwh1iWkdE4jT2vRfZyzQQItKvyDxStQ8aavKLmBSO1ftk95nM0nmCurzDY0WlZPg7Zb4RBi7bQ6JysG5z_tkbEGcFG9IVNbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/68966" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68965">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJKxgxibXg70LARwbarUj0dDgiAs7rwg-F9J2h5bkV4-lXItYYiQdnR__VdCvcP1Y0jtOz4dZfIsOQgVdFCqmJ09V5yuKc2AzdF8DrSTvtHDIZzG7YwKczNrMwTxRrqWNDy6EWlb7sYe3MXnvbaHDQC2oiUBXDlkG5FQLstAaNo__4oG4t4Sly4dS761OXzYDTrbDe6zveJiZcRBnfsjwz1fy53f8vWsrbCFgIlVTyJBMAhKwR0iFJnvgUdKaG64E1KqMgqvDBHhNdBIUfGI0Bs_SLGeptouY3M7i4XMPhOdP4bHl3LBD3julC8pS2GLHmXCwuFUo8UOvyj-jeKQNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
رکوردهایی که ترامپ تو این مدت تو مصاحبه‌هاش ثبت کرده؛
«ما ایران رو شکست دادیم.» - 106 بار
«ما ایران رو نابود کردیم.» - 95 بار
«توافق با ایران نزدیکه.» - 88 بار
«تنگه هرمز بازه.» - 75 بار
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/68965" target="_blank">📅 00:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68964">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uC7L3U5zI-jD1EzEcMZJWIeMpCVhA8VGtlC-3jzofa2YQhKmENm7kKs5oW0lvXSS_etbheR8d7NRdxM6hLU_suyvDcHqzhfTMapCEkucU8bvNmzZDf6dpjqy60Y7nthh_bec9trMmQLYZbbxLZndCIbfaIncn-upl7bWv7W8KlPmLtUoDrh7vSEqY9-y8PrQgReWgNgFRNQ4q8pOIKDr_cNGTVw1TGAoYNGlU8FkmHMYCWaS3XHIdKTEurO5d-v3QCUwrLxsZR11lYz5utegw73X4tZH1Q66Ori6k9ONsauhpDdOUHAE5Mib7LBRssZmT0wv7mz61FCTtM6zDMuDJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
عربستان دقایقی پیش به بندر حدیده یمن حمله کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68964" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68963">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🎙
خبرنگار:
آیا شما در حال بررسی یک حمله گسترده به ایران هستید؟
🔴
🇺🇸
پرزیدنت ترامپ:
"ما آماده حمله هستیم. ما کاملا مسلح و آماده حمله هستیم. ما با آنها صحبت می‌کنیم. شاید یک نقطه عطف وجود داشته باشد یا نباشد... در حال حاضر، ما به طور جدی با آنها صحبت می‌کنیم. اما به نظر نمی‌رسد که بتوانند به آنجا برسند، شاید اکنون بتوانند."
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68963" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68962">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68962" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68958">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68958" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68957">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=E6si5ZWR30yx7tiHthnGMfk_w7FAXFPHmVyVtwfY187_j_KzeuzuvohqrKaHez3ZEldkj854Ub40T1CprZTsTzdplbTEWxJkPqg0gQVs-oB1QFEtoA2okHECKXIHu_9JL_NW7Oa2CqNpHGTKqdo_chBzEBSnCqcep9iOIyhUa0naE6bjmhu09pcqtw3Gvoisjxu3uUM1tOyGAeUzOCwF8awpa5Bpyk_wpWCAwQ6vBr9UPuFrU3Fit9Q4NwcjfFADhP9-WSy6urlbYzDiGEF-Z-3IV4esIrkP30Inp8NZAgephSrKb37fqDrUkBuLozoCj2ItQCIPaYAamFwGPznfww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=E6si5ZWR30yx7tiHthnGMfk_w7FAXFPHmVyVtwfY187_j_KzeuzuvohqrKaHez3ZEldkj854Ub40T1CprZTsTzdplbTEWxJkPqg0gQVs-oB1QFEtoA2okHECKXIHu_9JL_NW7Oa2CqNpHGTKqdo_chBzEBSnCqcep9iOIyhUa0naE6bjmhu09pcqtw3Gvoisjxu3uUM1tOyGAeUzOCwF8awpa5Bpyk_wpWCAwQ6vBr9UPuFrU3Fit9Q4NwcjfFADhP9-WSy6urlbYzDiGEF-Z-3IV4esIrkP30Inp8NZAgephSrKb37fqDrUkBuLozoCj2ItQCIPaYAamFwGPznfww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=bQqm3yb5bf_jp5hciJHzaLJ3UuOi8SRBeroF-m-9rWAoUxPJMz52Z4ol5vz1inZNxHXx6hfTCS-NEeqkKkr-2G1TNgXDTf_UKVbtwhsP3KdYv-fJmeXXVKL8tB_qi3baIEdD8gTUfu7PkvcraeQiC7ir9DCtDN6xUxWFC0C_R40cormD1Z-EY7F9pXQ6Ix29ys_D3bB6RhE-QYxJnFR9AcFfv7mF3XNJf1-Fb-F5jWM5GDieqcba9p-j1iNM02T6EuTicTOkEiwqhxEV88M11EGO-_yBExiEfwdKVlKWpAfZZbZOSVO6OQk2hFIX4lGaRaOWG3SMfyvrE2Alp-IYiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=bQqm3yb5bf_jp5hciJHzaLJ3UuOi8SRBeroF-m-9rWAoUxPJMz52Z4ol5vz1inZNxHXx6hfTCS-NEeqkKkr-2G1TNgXDTf_UKVbtwhsP3KdYv-fJmeXXVKL8tB_qi3baIEdD8gTUfu7PkvcraeQiC7ir9DCtDN6xUxWFC0C_R40cormD1Z-EY7F9pXQ6Ix29ys_D3bB6RhE-QYxJnFR9AcFfv7mF3XNJf1-Fb-F5jWM5GDieqcba9p-j1iNM02T6EuTicTOkEiwqhxEV88M11EGO-_yBExiEfwdKVlKWpAfZZbZOSVO6OQk2hFIX4lGaRaOWG3SMfyvrE2Alp-IYiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
یه انگل هست که باعث اسهال شدید مردم آمریکا میشه. کی دوباره میشه کاهو خورد؟
🇺🇸
ترامپ:
نمیدونم. بهش فکر نکردم. پیتر، زیاد کاهو میخوری؟
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68956" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68955">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=Y7v3wx5_r8tpWLaDlU_eZj6GiiyxuZPydV22Ed2H8nTlZEA54wSAlr16tVSDQqxKbhrYMHRU0-_hcyLAQ5qw8yhGT6R8o6YbxIf3tsIen6FucbC0E5CsrnJeXZtHiX7HAuWj2rja8AMJfz7V4M-uKE0wUBQHDg_In2qZFdiVnScKVloi05eVYIq88yp5G7BuZtVkIKB8_dUwmhJnlyMtLtStY6ynzXdi7rn3PYotKXTwK8u2PiJQnm98dsFFNFuxfBO37QlbTIwWPtIH3eV1WG2Wvo-NzGozGkJeQbyzu5R2qOyWRGSZaxWPq0e3Ou-fwaBmgDoDGA9RPp5uUyEzzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=Y7v3wx5_r8tpWLaDlU_eZj6GiiyxuZPydV22Ed2H8nTlZEA54wSAlr16tVSDQqxKbhrYMHRU0-_hcyLAQ5qw8yhGT6R8o6YbxIf3tsIen6FucbC0E5CsrnJeXZtHiX7HAuWj2rja8AMJfz7V4M-uKE0wUBQHDg_In2qZFdiVnScKVloi05eVYIq88yp5G7BuZtVkIKB8_dUwmhJnlyMtLtStY6ynzXdi7rn3PYotKXTwK8u2PiJQnm98dsFFNFuxfBO37QlbTIwWPtIH3eV1WG2Wvo-NzGozGkJeQbyzu5R2qOyWRGSZaxWPq0e3Ou-fwaBmgDoDGA9RPp5uUyEzzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند. اما دو روز بعد، آن‌ها گفتند: «وای، این فوق‌العاده است.»
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68955" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68954">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=C_8VTNe76KhMKgwRRIOR7wSmBw8hERvElNpq6S0A-H7uGB33-Tp2dacOLebXktJG1WJ4y1UL_kWzJYv0EPbZCZV3e0K6N3Cj0GgW5eK9SAKNP0R5gzIzJShpE0HTDpSQeHKYnL4zp-jQOJmprx-Mdbt37NTpI7StGFIVNpcmGWxffwVEeuKHw6b3O_LpruCPNF3OnhUB6RiTc8sUK0NitJ2YpEgeZmi6SG16YlQJwwOhvTLeUD7vC8xkeisy_gsjSKQhV_2c6rIrjM0XDDTdScrwSw-v5pVcI48d9A28Rsq86mVJhoXku7ZrP8oE9NfrYu2n-rlhbh70k0yGtNhAsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=C_8VTNe76KhMKgwRRIOR7wSmBw8hERvElNpq6S0A-H7uGB33-Tp2dacOLebXktJG1WJ4y1UL_kWzJYv0EPbZCZV3e0K6N3Cj0GgW5eK9SAKNP0R5gzIzJShpE0HTDpSQeHKYnL4zp-jQOJmprx-Mdbt37NTpI7StGFIVNpcmGWxffwVEeuKHw6b3O_LpruCPNF3OnhUB6RiTc8sUK0NitJ2YpEgeZmi6SG16YlQJwwOhvTLeUD7vC8xkeisy_gsjSKQhV_2c6rIrjM0XDDTdScrwSw-v5pVcI48d9A28Rsq86mVJhoXku7ZrP8oE9NfrYu2n-rlhbh70k0yGtNhAsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68954" target="_blank">📅 23:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68953">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=sW-LTdIZ64DvQmVvj2zmSfltBAWbq-sw3m1wW1zcKQlkjHQGW2LaQyqDZqDcEhVyJYSljRqH-8a1BYCeQw5vJ_Zm-rmLup0dKnsn8OmUQaflX6mEobXT-mG7Y3F4BRtxzLv9RyBJQLU_VvnClqzo_JXMNe78D15da_yLvTz1Mn7rvlgWd3u6Nr78HMchaXwgDc_OpLVQZe_VqhMqcJgZggLqWgBtWwsVNJThZLE5ZM6KZ6ar-fv09fciACmmb_MUfxT3lhbqOuJAATvpTduRPmaU_VXO-43gMaQdHnyIDUq0HpKwNtja6naCJQtx5l8JPaUR1ewCVmVCM8q7I2vbXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=sW-LTdIZ64DvQmVvj2zmSfltBAWbq-sw3m1wW1zcKQlkjHQGW2LaQyqDZqDcEhVyJYSljRqH-8a1BYCeQw5vJ_Zm-rmLup0dKnsn8OmUQaflX6mEobXT-mG7Y3F4BRtxzLv9RyBJQLU_VvnClqzo_JXMNe78D15da_yLvTz1Mn7rvlgWd3u6Nr78HMchaXwgDc_OpLVQZe_VqhMqcJgZggLqWgBtWwsVNJThZLE5ZM6KZ6ar-fv09fciACmmb_MUfxT3lhbqOuJAATvpTduRPmaU_VXO-43gMaQdHnyIDUq0HpKwNtja6naCJQtx5l8JPaUR1ewCVmVCM8q7I2vbXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUn8eiNJCchK9O6tk2IcDL8hH6-xYRAv0GIbQIfFNSS54KbMLMoZH0LVL9GFjzWptk1_kwrltXu0iAPUH2LSmMIUvbR7r59QwjQRrpO7Pew9bFj1F08SIcrxNV4Nx_DmWxUSlyV7QHQNNsR4TkTBMTvkhTL7jAbWxuhdEYd16WwvS4QJEjvA_nzP8snA3e-k87NnGGbmmaHCA0pqxwv3utb92PUeUogL-DYASvvZopXIiHMmvzMvtNlZHheVI3eGxSx1lKDdws9e37s6pQ946mjrsG6MaYyWtGp3eTGB8te8EnVYaYWRPKqQrpLSsyd-TZkzIeBZ-ix1x0MNo1ZkXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
صداوسیما:
دشمن آمریکایی دو موشک شلیک کرد که یک نفتکش (یا تانکر) حامل گاز را هدف قرار دادند؛ شناوری که از دریای عمان می‌آمد و قصد ورود به منطقه را داشت.
نیروهای آمریکایی گمان می‌کردند که این شناور قصد حمل گاز ایران را دارد. اصابت دو موشک به آن منجر به کشته شدن دو تن از خدمه و آسیب دیدن موتور شناور و در نتیجه توقف آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68952" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68951">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⏺
ثابتی خطاب به شهریاری:
تو دیپلمات وزارت خارجه بودی چجوری شدی استاندار؟
اصلا بچه شمال شرقی، چجوری الان استاندار در شمال غرب شدی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68951" target="_blank">📅 22:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68950">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🇺🇸
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا بر این باورند که رهبر عالی جدید ایران، آیت‌الله مجتبی خامنه‌ای، بسیار بیش از پدر و سلف خود به دستیابی به سلاح هسته‌ای تمایل دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68950" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68949">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLEqbGVImm9OKUGINVCmiZFiegvDCTru6phezb2GKMRfEOSrKwn7Jn2wf1MXvBB_rViV5huAlE7VN8BuSyiRGMyjObmSkMfX3cFDtfHHDFHzvGBRcIykrkAHTVq-iqBTqtYWz_W04E2OK0KV4kj4d8fW6DPaJZc1e5SzTJ0FvrvzybttHrPOwaVzE2VKw3tVWMnxsslKYDhDKKnReFvwpcdwHqnTo_FX3U_H8MNBi5zJSf0pvruRqlkQsRtrvMPuLOt5APVuTxXxqYD8IPs8Fe1Z-133Ls4wkVrL8JHQR0QXOhzPRLD20N4PzFIEJenV142ofwQ_p1QM7VRI_WHwtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک‌تایمز:
رئیس‌جمهور ترامپ روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه خود دیدار کرد تا درباره تشدید حمله نظامی علیه ایران تصمیم‌گیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68949" target="_blank">📅 22:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68948">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-doM7kTwJQKrlXOjzHivWO9795ekzIHZcUARH9L2i5zTsd2tUBAJ2uSGGHi1-KZQes8vjPIsPwREyCZ_tqdZds_bkLWHn0BPdDyhPZkyse7GzVYHJ7sBnxbcG-gbVtwMQuUkHt1Ryu5Ew7RSBdfACYedmReHckUAyHmUuiZCST0ErXURnRpXcNFQtvENPyD9sWb3Ll07aTZ8nTDkuXnWm-a9lCar1yL-a39TYqKlNn0ZtLWcfBWMDkkfpRoA7wajltSd4vhkfcPCO14mNvwr36kAhzbG6vRfY3P6nlCfot1BhteA8BB_KEyaZlvsxetgOgLbTSjkp_fYXrcj-06Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68948" target="_blank">📅 21:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68947">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c449631.mp4?token=MSwxPf5eWGkWVnCWd7p9ARwkWuB3apyqqzsu8bajFRT6RofkAvy97bPGLsOcng229Q4tsB67zRl76YFAImEZrSJgwfrdwMvv-Muy9qBlwN-vmRULXcjE_0fo1nDSS_qIV6Nbz8ZvT3DRFr_hvlQF26D0gHabiAsk9L-xasqnktwL3RgF6nhnIVtU30MGYRPLyl_c9JEF2C5dLr5xVKJQgJHd0XvijUl9r8L_YAMFSHg5Pku7xgL9sjNgFLPtQUywSLPKNfQY_KoP-KSEdVjvaVfdorSpextSAGfoF9imN6gFwCUVgrktj9rSbNNtEQpU2lrc4_R6Rfqf_loe4um8Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c449631.mp4?token=MSwxPf5eWGkWVnCWd7p9ARwkWuB3apyqqzsu8bajFRT6RofkAvy97bPGLsOcng229Q4tsB67zRl76YFAImEZrSJgwfrdwMvv-Muy9qBlwN-vmRULXcjE_0fo1nDSS_qIV6Nbz8ZvT3DRFr_hvlQF26D0gHabiAsk9L-xasqnktwL3RgF6nhnIVtU30MGYRPLyl_c9JEF2C5dLr5xVKJQgJHd0XvijUl9r8L_YAMFSHg5Pku7xgL9sjNgFLPtQUywSLPKNfQY_KoP-KSEdVjvaVfdorSpextSAGfoF9imN6gFwCUVgrktj9rSbNNtEQpU2lrc4_R6Rfqf_loe4um8Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68947" target="_blank">📅 21:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68946">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trML5rtKt_eaYpMWng-EnAteYnKwcDYoruqrZn9iVx07Kj-8Ja7eLfAMFlgAjoy_JDzMv5uI1S7YNwvuhAchwdjvyqH0CamrFnE652HqA8IEFlo7ytC2wPM3xlysmFXbfo8ZumiJP0IfyUIr04WjJy-CRS0k378GNLAe-Awvpo12qFYr3UX354hisNMFqOu9SClgjzfSTTkAR_Bt0q5pyquBiY5APh3oeDnnAJN5Ck0lRI8D5ODADU0kItQzammVh8SCGgkPe0vBOXcSRBuo0TOj5TPDL_gt66Cj0vIJfXeU3FqH13ELY08IOQXkBE_flnBzuXsYEshLFY_euNN92g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون، در سن 66 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68946" target="_blank">📅 21:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68945">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1z0pvD_v-jB10mLRysk27-X6pbKwAJcOagRL1ewwNf_Rm7KMf26c9ojINeyvDQweexu8Wj3rbvtoYFY5B1vm7AsU0vbm6D18bvr9HohufLKKo12Ea7yR3mio85xHfJ5f7SBL54cP9yE4WQ4da7NaodE3_MTuHTN8EJgIJUzAtOb8ezVftMjgJTgCkIMyl1pRa4YhL9u9pL9yGUmJM3mgK1UwhU3hdCRgR9WMHaQTnJTcJaCcR8wp4frLlbPJklOfxyQRx2lxSZPtc25_EmVM2hWuhO_iFjJisf9ecZLUza0ihGc-E6OmZ6jlqp58Xc9KAbWT7tM_sC5JuSOclFSUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
علی عبدالهی فرمانده قرارگاه خاتم الانبیا:
از این به بعد به ازای هر شهیدی که از ما بگیرید یدونه امریکایی رو به درک واصل میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68945" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68944">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2066d70166.mp4?token=AI_pWlt5wAO8OgwtJ28_jxt8vg-c33eeE79WazDkTCQVfGbx77vwmKtK2vxEM6yJ97AYZQeNlqjRA2dkGqQPoCTl5P7JD3k4Z5MpNE3MMQvmANRCW-7HgK6N7hbpo-HBWdVXnUXuuglTpFVAr6CPwqfASY-IWT10t4oH0gZr1lUOqSMMEsLBKVXKV_eeZUcYTkLjmrbWrQ11rEUSvKOWS2mKNJT7dIPA7ojSwFeabj3CP3C5i03GJHG1vfgDXPeYYG-tpEfPXXZC5y4Kwe3IBaggTwWkSoQDnRM3AbsQIOR-aWjxpNRVBfCkqhVol_JAH-Ttuw0LETdrLPJ_SqralQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2066d70166.mp4?token=AI_pWlt5wAO8OgwtJ28_jxt8vg-c33eeE79WazDkTCQVfGbx77vwmKtK2vxEM6yJ97AYZQeNlqjRA2dkGqQPoCTl5P7JD3k4Z5MpNE3MMQvmANRCW-7HgK6N7hbpo-HBWdVXnUXuuglTpFVAr6CPwqfASY-IWT10t4oH0gZr1lUOqSMMEsLBKVXKV_eeZUcYTkLjmrbWrQ11rEUSvKOWS2mKNJT7dIPA7ojSwFeabj3CP3C5i03GJHG1vfgDXPeYYG-tpEfPXXZC5y4Kwe3IBaggTwWkSoQDnRM3AbsQIOR-aWjxpNRVBfCkqhVol_JAH-Ttuw0LETdrLPJ_SqralQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما از یه بازی فکری رونمایی کرده که توش باید
بچه‌های جزیره اپستین
رو نجات بدی و ببری
بیمارستان خاتم‌الانبیا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68944" target="_blank">📅 20:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68943">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJ7aPw4p__IHou1Xl1H2mwFjoCdC6qWMBTh4POuMnlQeHwigcoDlrxzdjT2XjxRg9EQDvpQn2vQNrbrJtCBTKWGYx7XbpIQCF8w5YnHcqL1ZUKWgqC_W3qvkEiRKh4IPVjkYuZhkVcZDFHsIyNsGoUQ2jLQ3yMLfjb2YYL2JamM49s9PDNEnM4yvVMWhb9wgqHtYvW-R00RUYHR5Uy7pCjq8OUETeyOK-Nqf5DYoD4YRXnFW-KdjUQOs2vfSHjuVlpHgai5RvPEg0TEZVszwBd5rtGGzN-kknZVAL4p3Qo6_InMlHsAtNZRZTMR1asQYe8tv0i3aILUs3cx1YBnuIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ty8LNWVCBhjorF-DwylANVGj-16geO1Z-ltpELpFWBAgALIJjQqLaaurkyWBvir26gbjmcEUCpFRhDxjkC-aECjG-CeA4jPB16jaYwZybhEku-OcH4vXyze554HKm9g92ziRXfTthEGhVQpe1zqkj8_bPMcQxKHF1gLCxJ1DzwACwJ50ECKenSugNLpfTRd-ruhJq6zcBZEP20EE-ja8ofblYBLZF9kVRvT9fu20FSe2F-bSVUifsO1Uolv2NQcbPxjNw5j5ZgLhWWDAeFRybbhC4od0ocNrV70GPecQI_5dbQtcW8z3htf7iA2muhtOiDXMcGnQkAoHM7Tj_Z7LTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q_Jcrw42Leyd6HhP2X2F2uVGDlz_cMdf8jGExbW4eAiSE-0agbwb2nR1sCyHqhuxAz4mAWZFTKd-nMbBD6xKhs3tFEmqVoMPEdVEBqGa-hhbs3OkHs_BJ0WMgf_DQCB8pZ_8IZYQd0FfXX2VWd92Wwq3hvKnuU1mckmO5ldH41EDItIVFB930KM9j-la_BiDzTRCJkiEo49OfTJssgbYbYXcq1yEnONps4QClg4CW3Yc3aGs6MzPk233WRKwmStEBdn6S9wNf7qExSI-V1KjlXpMgYWG1Abs63uk9KUzgleblESXu_idhrfOsV2qH0ATASZRV1L_mAh72P6NOcqr5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/heVytWzS2y0JdZhs1C3S71ElONfgupCa__YFpwIDiRSJ1MwCzjTz0L4D5_IDHGAgSnG0LRmboimA_9G3FzfMqVKM4HjoxQ_55mlEwK7fXU3mzJVw0yShkshrXgfTe4uikSh8t4aer-E3hXnsODWA5ldILpFVGJ_TxdUMQqHW5AItXO0F7b4nQWbiIwLtvTYQJWTY7v5fLiY3uqiVHwOsZAnjAVlwB7ARPSh-VsbGFcjJsLftYJpS3AUsvwUOstc7dyLeGdVNHKtBLVt7YqLc6hwlVJFnIj9ZeIBiQ0qh7xbOgFhDd8Kl452-1ar4zeMjSB3t17PYfjDnvrHBqXEtRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=tMGSaULoUntKwvE8prpIpCPh5lOuMEFmbQ_x5GYkJ7uFCzDVc3gGTJqI_GIbWnzC7GtGJU3e2f-2xL9F5RCA_XYhhhj607HybpqFfmDtYRmPeaGhsY2ygr_Rn98r_zXsfp58QeoG7ksMMACOw-E4ZhpQ5H_72kE2FDqZRSLqml8Es0MYuNrEW_v9lpDd5J7A7x4ClBOb4bYwXJfsCeHKZsNUd4yfXwPQb8CZ1OM7zW4GqCIOYTG4n-k_pnnJ7cFWJrFKtSXGZIywdzA3oRGvvvKVdoV6-HNxi-wDRVf492FMlVLJIbAhsRUTfz02bjqAZms69mr923wkYxXXHhl8oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=tMGSaULoUntKwvE8prpIpCPh5lOuMEFmbQ_x5GYkJ7uFCzDVc3gGTJqI_GIbWnzC7GtGJU3e2f-2xL9F5RCA_XYhhhj607HybpqFfmDtYRmPeaGhsY2ygr_Rn98r_zXsfp58QeoG7ksMMACOw-E4ZhpQ5H_72kE2FDqZRSLqml8Es0MYuNrEW_v9lpDd5J7A7x4ClBOb4bYwXJfsCeHKZsNUd4yfXwPQb8CZ1OM7zW4GqCIOYTG4n-k_pnnJ7cFWJrFKtSXGZIywdzA3oRGvvvKVdoV6-HNxi-wDRVf492FMlVLJIbAhsRUTfz02bjqAZms69mr923wkYxXXHhl8oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ویدیو ای از بمب‌افکن(B-1 Lancer)که گفته میشه در حملات شب های گذشته علیه اهداف نظامی در خاک ایران شرکت داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68939" target="_blank">📅 19:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68938">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=CrKeIjJriO_jKfPjF9lPwnN7mQH9gaqTRjwOLokSFkaOjNqijk-1B6KboQhiqViL9R5x92jue9PWmkHb9ciavBC1axv6YdxDd3Wotml7EI0nhigPWybjrGhWB2mF9XjyA8K2tyZiNkgQK9beTw8E3xSiWR65AjmpeCvv0zZ0h7V3Ea74NgBdU7clsy15c4YQzcT_10rCyg38SRiRL8byccRZ6aqekhe9NVifFzvFrVcERPjfAl_s4IaQMKznabdPLI7mRb_o_a27amt549sXEYGeH7nD2TjrFzBcxrDdo5escvKNDpa0-bpOifNsPBXqgxij5VJKhx6AQmT2pdZjfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=CrKeIjJriO_jKfPjF9lPwnN7mQH9gaqTRjwOLokSFkaOjNqijk-1B6KboQhiqViL9R5x92jue9PWmkHb9ciavBC1axv6YdxDd3Wotml7EI0nhigPWybjrGhWB2mF9XjyA8K2tyZiNkgQK9beTw8E3xSiWR65AjmpeCvv0zZ0h7V3Ea74NgBdU7clsy15c4YQzcT_10rCyg38SRiRL8byccRZ6aqekhe9NVifFzvFrVcERPjfAl_s4IaQMKznabdPLI7mRb_o_a27amt549sXEYGeH7nD2TjrFzBcxrDdo5escvKNDpa0-bpOifNsPBXqgxij5VJKhx6AQmT2pdZjfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
در هفته‌های اخیر، آشیانه خصوصی وابسته به سپاه در جزیره خارک هدف حمله قرار گرفت. در این حمله، چهار فروند بالگرد آگوستا وستلند AW109E که توسط شرکت خصوصی بالگردی خلیج فارس بهره‌برداری می‌شدند، منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68938" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68937">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJXEOCu8BRe8eK6hnA1g3x7K36Tylero3YL9T2oYv3N9ujI5JwRyWxwpZO9gHURjll7rtsnd2jpJ75nHwzZQAsxFiLzKPMqNFL8FRYsVfA9N3IyTx-Y6yDhs_aiDC1NVbnekjcRJE-w2h7XkbbQ696PKVBQKkjPF_H0308ryMFNuX8d8JnO35SRwey3nbnglbXwHFJvr2BZJ5ySIZ3oeGgQ7mipQKvkgf13FLTLeewmAvbIBRNcETtAXAh7myr61B9waIAHEO5AOsBqCEHEOsiP0pFKpCezC8CnUqiqpxN7MrMd2h-W4BKxB78QHGYc3X6XoeAn_IZF4iiUg17maYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رئیس‌جمهور ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68937" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68936">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887792c366.mp4?token=UMk9on7RvCd3dWTy6bKaxDcBj8p1oogf6T-n383y3KPRmp2OMWJrDWZL9iTK-mc9h_J27CUUb5bI1vAc6EY-Uwoq1Us3kX8HMwTPbKcHTnMDXRCX0-VQ6wsYOjcpzwxYwdGuZeq3n-QbExPwZcy2NCVJvQR8CccqB6y3xdCSmxiMZYMNimoy9dcdUwN9DXL21kasbiFlOUC2AIgLokfaL2QUdfBP8CFjaje5NfTERa6v4jFFCq8WcJOEnYj7CamkX-1OxCOe_dR40Rmba2gGOo65sufeKrRNgPsIqByq6LtIJqOf36Eq1zwEJHj2Jf_pv1SrnDRIbc2-IWjSXQRA4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887792c366.mp4?token=UMk9on7RvCd3dWTy6bKaxDcBj8p1oogf6T-n383y3KPRmp2OMWJrDWZL9iTK-mc9h_J27CUUb5bI1vAc6EY-Uwoq1Us3kX8HMwTPbKcHTnMDXRCX0-VQ6wsYOjcpzwxYwdGuZeq3n-QbExPwZcy2NCVJvQR8CccqB6y3xdCSmxiMZYMNimoy9dcdUwN9DXL21kasbiFlOUC2AIgLokfaL2QUdfBP8CFjaje5NfTERa6v4jFFCq8WcJOEnYj7CamkX-1OxCOe_dR40Rmba2gGOo65sufeKrRNgPsIqByq6LtIJqOf36Eq1zwEJHj2Jf_pv1SrnDRIbc2-IWjSXQRA4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68936" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68935">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=CI75tqN5wgRfiba0ZiwzR9gEeqp7eRofL2If3P4oUMSrg2qL4j8jjvah8ZojJQENHcgHgazrPJb5EyuuPXmzjlJJzwIySh5GH4qZo71LjvgAUz2APg5t2ij-GBWwYn3lNLhzvr6bA596sU5wZPAjb2Q6HwGcE8t3PPTRy9VTgzBybiQMxJgzLRj3UFNtMn7TQEJhrse-xmEJ63dRC3kX0lbCyz0Hckls2seHk_byH_OHBqWh0fTPcPfyf7WyNV7JDoXHq97IJZlvyp92848kUPxT5cHtLbXHFNEMhykADxMX9VG2GS7mvIhyLd8iziHHbVeCvtw07rmJv6HT8KQ7Qm4mtIZDW_aCwPR5Nlec65jLaWlE6Mb_Ln1IVEQg_czbYYfjhXTYTcYT1O6_Dv22dZZgAxg9Yum7sLDBV8iA4kpwmGwg099F1NO_NSg8ZvYG20iAVo4O0Ww9mfxWuaSfvXmaWX4gRkVbzWKPQqlFKb8X_r6Ob4Ne7UwKyPcGleYa797c9rSly1kZBiUM-_eXst2__Oz174EwedajySqNOiOYLM6gjOxLyx94u1PSXVbJCV-MJCL26VSxF2MXCUGqCYmYZQdUwuY7S401c9cRPvBgZxk21UrHy_bYmtNOnB2nlAkiA6w3zF2tWApVUwnW97qIStrcL68Rr0dwHsfnfOk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=CI75tqN5wgRfiba0ZiwzR9gEeqp7eRofL2If3P4oUMSrg2qL4j8jjvah8ZojJQENHcgHgazrPJb5EyuuPXmzjlJJzwIySh5GH4qZo71LjvgAUz2APg5t2ij-GBWwYn3lNLhzvr6bA596sU5wZPAjb2Q6HwGcE8t3PPTRy9VTgzBybiQMxJgzLRj3UFNtMn7TQEJhrse-xmEJ63dRC3kX0lbCyz0Hckls2seHk_byH_OHBqWh0fTPcPfyf7WyNV7JDoXHq97IJZlvyp92848kUPxT5cHtLbXHFNEMhykADxMX9VG2GS7mvIhyLd8iziHHbVeCvtw07rmJv6HT8KQ7Qm4mtIZDW_aCwPR5Nlec65jLaWlE6Mb_Ln1IVEQg_czbYYfjhXTYTcYT1O6_Dv22dZZgAxg9Yum7sLDBV8iA4kpwmGwg099F1NO_NSg8ZvYG20iAVo4O0Ww9mfxWuaSfvXmaWX4gRkVbzWKPQqlFKb8X_r6Ob4Ne7UwKyPcGleYa797c9rSly1kZBiUM-_eXst2__Oz174EwedajySqNOiOYLM6gjOxLyx94u1PSXVbJCV-MJCL26VSxF2MXCUGqCYmYZQdUwuY7S401c9cRPvBgZxk21UrHy_bYmtNOnB2nlAkiA6w3zF2tWApVUwnW97qIStrcL68Rr0dwHsfnfOk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:
حمله پهپادی به مخازن لجستیکی ارتش آمریکا در صحرای عربستان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68934" target="_blank">📅 16:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68933">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4LGDsNLg9XEfgpZbOZ5UwmT5jBlAzDTI5Hn4MeU4cWEB4vF9PzAYgL0NWqU3aF1IKDjUH8Kn0V-yzu7FdZD3Vl8mSBZi1_x30XJFWw5YLYQQ4PdkiMe-rwMu1uv0UgzogKaZ82b1AeiGegHHAhUaDzFJaBn-IweXVIzp-7ptjK5VKd24tk7A90dt8o10y_K1llT_GOGogmjEmkCRkn64YL9-rM_U5wmEuuY3_d14xvr0VcylKt7e22E-9xDmd-8ooOQOCvmmaLL9gllqmDSO39USedKra391kkfC5an02jat7YmjlGe2g2Wqs9BX4xCljtiA5F1cjxGWPLvdHGEvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما:
یک سر در برابر هر چشم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68933" target="_blank">📅 15:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68932">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEO-Jw8bbTjv_3UWAKukJkpNZxtwnQQLJaPk-e031ZbXHDrDbxT11dZNJQJh0n7PldT-KIj18jrBxODhLjBeidaCZ4bkaGNaOS7deQH6Hio-v7AA6essIj4pUyxNDNXIAxe-JYWIFYpIadx6IzyVLtPDmsScc5KFpDgEH1ROH9rUdGPNy-MWYvtkt1OX2xLDIMxeC7UzwKxsguy20EeZAmyJZbvKxoUQwqWPh4AowoFhS7g1hx9iNIGnnkrAtpGR3FVPojkH1ooFWr70ozf7ePwb9qMRFML9Gfhde-s-988noKY89a1lTI59mBdS8tPR6y5hu17XEASJhw2RdQlO2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
وزارت امور خارجه آلمان اعلام کرد که این کشور فعالیت‌های سفارت خود در تهران را کاهش داده و بار دیگر از شهروندانش خواسته است که هرچه سریعتر ایران را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68932" target="_blank">📅 15:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68930">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DYChpE1esdtrMuSJA4mRKVxTmvlDX5_BoZGRDsnJD_CUvSrc7BcMWHgYbhp5DDF-6nz80IOBeN04-dwfYnttijZpcjZQZvZ_A90WwFKPezoxqrZ4J6wSw3aWwjESXxBuEPswOlI0hFOfRFuO-hv_SE7UFUTZ7nt-08N0McYPpQ8xB8dfKO8roRvTbxhyhQ36xreQ439DJ3w8NQ3hnDIyQ_11cITMZe1y7PVX9Nh24w7M63J05YBfh0bjh6ALWhXzTVw-sfeixau8SaofyaofUrennfZjPn5JCcAbUOXaMqk6QQQaK8vsRHjBs8-naBZtQQYaRR4aWi0MdMNkstD8qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LDUuwnqB1tQkvVAiNYENVEoNiIBBDhm3cgsCdJsR3sL-YUB0ajOS1igqPByq4b29-chegjeCHv72FU8kf_IizQfUJvheXHp4wpgqhc3c6Rxinv4HYvEhfcDZ5DnwRtuqHA4mDuNKvXHCdl2tKaAx9X9vpxqcLTv9mYxJELpxDj1f1u2J32qFhkfDKELTmRp2rBAtdPRH7G5o2iMmzFgy9NIf4dLv5RffHr7OpvOfsC-2o84-8zQM-CPfjlQh69Uu0RjzfmaA6wEBiI5xryvG5-04REmhBAo9cJ-w7EMxgU5AucUJ-kDa790Z3UOh6-h0Ff4trtfnAv_K3ZY2yXvJ7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی شاهزاده سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68930" target="_blank">📅 14:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68929">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=T5KCpPc32FCnClB5NRmY7GZmhqtv8WRBaWcy2N9kQDO5sTQQZpktzNsWEKDhQizyfma7WZMSPb187PLK5_kyGcFL4hcG1XQbCjqcxIl8OiDVJ9X5jrpMbOQcL0sW-TPetpzlVx6om9CM-Hknu6kBD_p-0UHb5OcYMYtSAoElCVLJ_bZPawcu8mmMtM0mqqWs_TSPVGQirBgP2m7Qn5F5aHehgecfoXj9k_0gMezj8uLNpz7elzH2HfvX_ULLaZokC1JRinyUDg5fVXEycCRabN8w59wuPk7xSAqjgQJ2_xsjiC5DFSQz2IuVwav1wUUH5c5oWmjsKKmUBnYJXc2VAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=T5KCpPc32FCnClB5NRmY7GZmhqtv8WRBaWcy2N9kQDO5sTQQZpktzNsWEKDhQizyfma7WZMSPb187PLK5_kyGcFL4hcG1XQbCjqcxIl8OiDVJ9X5jrpMbOQcL0sW-TPetpzlVx6om9CM-Hknu6kBD_p-0UHb5OcYMYtSAoElCVLJ_bZPawcu8mmMtM0mqqWs_TSPVGQirBgP2m7Qn5F5aHehgecfoXj9k_0gMezj8uLNpz7elzH2HfvX_ULLaZokC1JRinyUDg5fVXEycCRabN8w59wuPk7xSAqjgQJ2_xsjiC5DFSQz2IuVwav1wUUH5c5oWmjsKKmUBnYJXc2VAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقچی:
کتاب نوشتم، «قدرت مذاکره». نتیجه‌اش هم داریم می‌بینیم.
همین دیشب یکی از وزرای خارجه آفریقایی به من زنگ زد و گفت میخواهیم دیپلمات‌های مان را بفرستیم ایران، برای آموزش!
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68929" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpDZEcTe0lAcGlm3fGAdU2QxbllZPxF4CZaV23lzIzFSnxE71BW5BhpVswHRPCZzTEx9XMeuVuKFB5KzUwZMj9TOVIiD8-Mhs8ilYup07l_YKKxVmIMlg7giXGwFRv003BdjFkhyyi2ucFZPMJ2wLmQZPb_syiYT7ebv9BcrPjYPsd9CgwTRaZCJHhDh4_KHgPwXR3CModiw66L8PPrwl7sZ4Wrx2W9ccoI7YsaCrufjiWFU5Z0ZTgAxD2EFCH98oUWCGIG2vHTDWk5t5lxBUtat_9ErperEUXT0CdGaL2A_T-ilvsRWvcMP8cpXmDT4HKH9RgutzZjezvpJuImV6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68926">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOxbSqk8_o2PvPJf_NnUqxvyB9hKFP5q9BDyKjPzhz3H7hwNgdblmSxb7Sf3HB_aQ0ODR76jzRncBzmzaaR2HRme5GPiMqgpvf15XCut7sdHEMqdgRlbeTV8NymQAkdR-8pMsLTdWjAxYTMtUn8UrahF1kKgCOfqNC_xwYp23V-QbJdIvWn9-sbmwCIEbqypNmKjlThY6Q5dGqPRAGLzz6WfID23y0CzSezv_s_i-of-0F72uS3fO1qYuNzpfbgWVkLr-JEQSNC9UmB2I4rlCua6Ek7ftFWkqYpOt-vaGTK2R_blx0ek7Zbtn71dtvzwoXWLAeXiFwSx4ojC1Iyk6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
جیک تورکس خبرنگار یهودی کاخ سفید:
نمی‌دانم چطور بگویم، اما من در خودِ «کاخ سفید» کار می‌کنم. از اطلاعاتی آگاهم که افراد زیادی به آن دسترسی ندارند و با اطمینان کامل به شما می‌گویم که آمریکا برنامه‌ای برای شکست دادن رژیم ایران دارد.
آن «کارشناسان» حسابی غافلگیر خواهند شد؛ هرچند بعدش وانمود می‌کنند که از همان اول هم می‌دانستند، پس... بگذریم.
به هر حال، خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68926" target="_blank">📅 12:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68925">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=m7qFlBv6kABjHkcbJWsQ2sgw_ixrx_vjYpXJxbatc7wrgTppbI70r5NpTWy8HhXKtcvGN4CR6uyERAeKt-jLC_86a6XB6ZWR9qs2loNdv2aHFPUsu3Z4GTkvYrIUaw0mqUFTAZL5KH_Mz28wECMVYoCVIn2dzqGF8MvzKhi7iu12oc8E4Vk30anAql7zGFOuflNPxBhbP7qMKyaTBuZ53jeK4PCoWQi_xqmC6rVsIpHD7X3t_hJFOtdD7kMXsOCHYcx6xPMg94neTzkcjXf6bc7QE1RcLQdqLPT0Ny_v89D1nROBNkBRMrtYof_WBbHMLrzE63REsZEhImuIN7ej1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=m7qFlBv6kABjHkcbJWsQ2sgw_ixrx_vjYpXJxbatc7wrgTppbI70r5NpTWy8HhXKtcvGN4CR6uyERAeKt-jLC_86a6XB6ZWR9qs2loNdv2aHFPUsu3Z4GTkvYrIUaw0mqUFTAZL5KH_Mz28wECMVYoCVIn2dzqGF8MvzKhi7iu12oc8E4Vk30anAql7zGFOuflNPxBhbP7qMKyaTBuZ53jeK4PCoWQi_xqmC6rVsIpHD7X3t_hJFOtdD7kMXsOCHYcx6xPMg94neTzkcjXf6bc7QE1RcLQdqLPT0Ny_v89D1nROBNkBRMrtYof_WBbHMLrzE63REsZEhImuIN7ej1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حملات ایالات متحده به ایران برای سیزدهمین شب متوالی ادامه یافت.
در این حملات، محل‌های گزارش‌شده‌ای از موشک‌ها در یزد، انبارهای سلاح در اهواز و چندین نقطه دیگر در مناطق جنوب و غرب ایران مورد هدف قرار گرفتند.
در پاسخ به این حملات، ایران صبح امروز چندین موشک را به سمت اردن، بحرین و منطقه اربیل در کردستان عراق شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68925" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68924">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=SyQegTFLCLVFFWlCkpG1r-3HnUwr5tauqRaHJWGSJcLH-KC66NrWkgdWVfZBYqkauSLVnsIagrGP15j5AppCWTfNC1BaB8hOWQ8d-dBrbdT_vZclg2sV320wI7Lu6Os2HBBPAaSCA1vzFVdFwRKvl7InCWlIStltCoyyqALoXEmaK9fSlwdcU0aV9KQFSBTb2MkXWKDJk5O2QK2GwUILblgq4hLPCd6PysScn1TVNw2hcmO-rFGTRFo1bYEwh_SkgLum1iBo4bGNdkv2Xrje6SrA2E0AqQL4zoTptVIEJ1YTuIHMWlLmOPbDsqV8ONhoD31CVoAoNYjAlKWTnXa2cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=SyQegTFLCLVFFWlCkpG1r-3HnUwr5tauqRaHJWGSJcLH-KC66NrWkgdWVfZBYqkauSLVnsIagrGP15j5AppCWTfNC1BaB8hOWQ8d-dBrbdT_vZclg2sV320wI7Lu6Os2HBBPAaSCA1vzFVdFwRKvl7InCWlIStltCoyyqALoXEmaK9fSlwdcU0aV9KQFSBTb2MkXWKDJk5O2QK2GwUILblgq4hLPCd6PysScn1TVNw2hcmO-rFGTRFo1bYEwh_SkgLum1iBo4bGNdkv2Xrje6SrA2E0AqQL4zoTptVIEJ1YTuIHMWlLmOPbDsqV8ONhoD31CVoAoNYjAlKWTnXa2cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به اسم ناصر نوری گوشت سگ به مردم می‌فروخته!حالا مردم متوجه شدن و مجبورش کردن خودش بشینه تمام گوشت سگ‌هایی که داشته رو بخوره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68924" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68923">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=McrihNto_nDmuzdy2hxNqnnsAwrXGEDMFtduFcR4zauJd-QalGBPZztPcOBM9RfR9QyX0HhDuyc3iJ0dCqT6Js4YxXsd7IApwjGUQ0IVyHkTtSFEGXNL9WpxjWVet2ydYvo_32QH_ffv-gDZH3tFgHsy0NP43WERo6Xdqh35P2vyikSyswdhkQ5Xr1YhXGpgkxd0JLxyc58ifiaPvjKEo_2eYy573XmB-D-BGeIMv0D7dzDQ3p2I5keRpFJ9UV9mSmSkGbXsdlplxsF04pPNWDZtL_sePLC2DD_LaCJL-AjUOrUt0P1iBZWhHRM0iEzW3fruXS7cLR5msuQZ0CjPpYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=McrihNto_nDmuzdy2hxNqnnsAwrXGEDMFtduFcR4zauJd-QalGBPZztPcOBM9RfR9QyX0HhDuyc3iJ0dCqT6Js4YxXsd7IApwjGUQ0IVyHkTtSFEGXNL9WpxjWVet2ydYvo_32QH_ffv-gDZH3tFgHsy0NP43WERo6Xdqh35P2vyikSyswdhkQ5Xr1YhXGpgkxd0JLxyc58ifiaPvjKEo_2eYy573XmB-D-BGeIMv0D7dzDQ3p2I5keRpFJ9UV9mSmSkGbXsdlplxsF04pPNWDZtL_sePLC2DD_LaCJL-AjUOrUt0P1iBZWhHRM0iEzW3fruXS7cLR5msuQZ0CjPpYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از سخنرانی ترامپ درباره ایران زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68923" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68922">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=hp5Z0dYovT81DycIUK43A7XbkD-FhNV7WGF5B2tg9DhbsTnOJ_RpWuc4QyWGEvdXQxlXXz6ipylqRdJqYYAhSjX3WI-jWmnGe0sYZNX_52xTeZLosxMmDjmJBqEKHSlCQ-zzSXt6urlFymva6N0nhb85gNl_Y6IoM4EfvIFUAim545Y1tkiCvnDOmrq-XxBdwE9843lyLR2bEPCRvc5_a4nZq1BijlPyVz-aqRS_XEx14xf9Ivme6wnh7w_jdS3tZfoMueBRBTn-SXZ-Q60qCWwfVx5YzNfeQqC38dlsNe-93xieEc39RAB8a5ZgEdqLGk5YotRCfW1JTATR8Na9GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=hp5Z0dYovT81DycIUK43A7XbkD-FhNV7WGF5B2tg9DhbsTnOJ_RpWuc4QyWGEvdXQxlXXz6ipylqRdJqYYAhSjX3WI-jWmnGe0sYZNX_52xTeZLosxMmDjmJBqEKHSlCQ-zzSXt6urlFymva6N0nhb85gNl_Y6IoM4EfvIFUAim545Y1tkiCvnDOmrq-XxBdwE9843lyLR2bEPCRvc5_a4nZq1BijlPyVz-aqRS_XEx14xf9Ivme6wnh7w_jdS3tZfoMueBRBTn-SXZ-Q60qCWwfVx5YzNfeQqC38dlsNe-93xieEc39RAB8a5ZgEdqLGk5YotRCfW1JTATR8Na9GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری به ثابتی:
تنگه رو بدیم بررررره؟؟؟ مگه مال ننت بوده که بدیم بره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=K3LtW7nlk0H7kVonLiVOlpFXKVQ0cV5J31wmkY1eJ2O_C-11vWxpeAKdy5VEVmjhMnrJ7uRoL_7GgE78bb2JenyEDMiuE7KdTrZomoX1fobxvf60Ep6YkP83GdOBYlJ6sacANW46AZtrLNcy9MzGArEWNH7qPkef9EMnCGzPoiM7sksVgSxWfkWPGBOXCjiWf9mRIhXy18QtItUvVWXqN2RptaxOwP-G7TxKcvNgK6pZHAA95BgkeVusDBpwXmBWX0uwCrVRy6lbSQEc1ROmqHmiO-fotkUynRFdcAH4N2y_sdKMQ5hGGtzZZdGCQfQNIBTBq863pBWZukk7GusAtw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=K3LtW7nlk0H7kVonLiVOlpFXKVQ0cV5J31wmkY1eJ2O_C-11vWxpeAKdy5VEVmjhMnrJ7uRoL_7GgE78bb2JenyEDMiuE7KdTrZomoX1fobxvf60Ep6YkP83GdOBYlJ6sacANW46AZtrLNcy9MzGArEWNH7qPkef9EMnCGzPoiM7sksVgSxWfkWPGBOXCjiWf9mRIhXy18QtItUvVWXqN2RptaxOwP-G7TxKcvNgK6pZHAA95BgkeVusDBpwXmBWX0uwCrVRy6lbSQEc1ROmqHmiO-fotkUynRFdcAH4N2y_sdKMQ5hGGtzZZdGCQfQNIBTBq863pBWZukk7GusAtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68919">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68919" target="_blank">📅 04:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68918">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=ZQFHKwf6XM3LaaB-EfPGEJPOSSvuuI8YDtoCtHSZuxDuzO4eVQc4lzdw9SBZvySwVPda8tdk_Xf2n6tNu8M5rQVAOZCXVl-ztPUJEBtpKqrdEnjiHyR6N9Kk7eJMsdlhxLfoFNIWujEXTsDBj-Lp9xarYADARyBisgHvIu6sfgTcW20j3IkVDTqLtoiBRgTyRf0sI89KBflpbFUTJHWyTBdMUepFWA7T3zVf73SAjOVivc0FGgt1mtoNJMGprBmh8-TTlaR0bsOANBchVjBpMzC04uVLkseUgxxL-urwSNJvzAng9MKD4j1SqqgZrHO_UMiItf2wO6sM6UsbrZTXsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=ZQFHKwf6XM3LaaB-EfPGEJPOSSvuuI8YDtoCtHSZuxDuzO4eVQc4lzdw9SBZvySwVPda8tdk_Xf2n6tNu8M5rQVAOZCXVl-ztPUJEBtpKqrdEnjiHyR6N9Kk7eJMsdlhxLfoFNIWujEXTsDBj-Lp9xarYADARyBisgHvIu6sfgTcW20j3IkVDTqLtoiBRgTyRf0sI89KBflpbFUTJHWyTBdMUepFWA7T3zVf73SAjOVivc0FGgt1mtoNJMGprBmh8-TTlaR0bsOANBchVjBpMzC04uVLkseUgxxL-urwSNJvzAng9MKD4j1SqqgZrHO_UMiItf2wO6sM6UsbrZTXsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68918" target="_blank">📅 04:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68917">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سرعتی.npvt</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68917" target="_blank">📅 04:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68916">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPpnW1NxZSM8wA3-bLDsCI1vOyHtGoS6a2fHbIUuGiQrTJgQbkDwi2KUGRv8CXVv0Agu9wIIOOX5FeR0ejtmhQKoPVOGLbjTcoyKVFXOo2XgR8ZgTsewS5yCZo4m-gOK_eJxa4CYMH5yc5z_aMq-a9_ut0ekQGw53iW4Ym8Q22tROierUXcUH63SRaqAkPnLFNyiXpScqBUQ7am-xBcndTvEryk2irut2kV3qfDD_IE9PDKOoXDhTIXUi3_f9Kjq3evtWs9muAP-zGHYle0281sypAwUkKNdGMPsG2tAx5R0p7oTqeohuRLX2wx437a04_miAwtZWzS7XZjwJ0cf8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ پدافند تهران به دلیل حضور پهپاد های شناسایی آمریکایی ها فعال شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68916" target="_blank">📅 04:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68915">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsfkrzcqJrLI6VUrd5Q797sSXKSvbDtZoeXo0S66YkdTDrUDtbiQrU_8X8Vx8C6xefqyfb49xzFM0avosTlIWVe8Ui25tLaRS5rKndwH2NxXVyY_GLHE-H6f-LAOhwAXbMKj1Or6IQMzd2Z8SOyUJrRztxlzWl_M-pc42kBlP08A3So03qtZ8iZNUCTN_ky4SWFUEmDHws36UNTEI7_m2OGY0Yr1CNJd33mXv72rLM0fvO2FhZqbh0v9Qql3qnmKqU39YSUkepIYEBlEU7Ta4R5sENlY54_-aAn3GcvLXIRohaTc-a2ZMRrSlA4XkYecng1mRH6ECysGc3C8L04AnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
برق مناطقی از بندرعباس قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68914" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68913">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2AXXcu76nGlUHEkUYkIDhelFtVyOMOdqsmnXLdTvY55BxRWt-7fa-1AC5PWL1avLE9Ar9pf2po4iKyq88AFd-k1sdjT94KpRuzCYZR4O_8obAYYTNin4hvR_EPqKm-KoDJGZCteb251Qxxi_Igq94QDjPK2ztZpj7QK_MR3EnCz6Mj17BGHPifHnaxRp5wOXgtV993sKwyqZvk34NlSNMsQFsBCKN6OkK2iU2_vHu8IeOGHMF86PP21ZuUhSC4ugda_LLL1ItCeneyMBYSh7cTOt8BymSzLZux8BOS0s2rUs5sUcWQZHmgse4YWySQrgvM8pGOYQoQCuHCQgNeg0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بندرعباس؛ امشب  @News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68913" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68912">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🇺🇸
منابع آمریکایی: ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68912" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68911">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=UJbFzQ7lulxmip0DlKVY2qfI3nvXAIlvqJYKLQOdGS85JDmMN-hKIXRkmdl2s1fNku6WrBrj3AD0tiT9Ev3pp_UXSjZRmmhxNKyAQ5owRDpuyZCVB5KDTg1WyNnM84Bnhd_FxFUDxe9JFnNKXi517H1-hz10xBkp3Z1XK5CyzgtWDTMdRJQ2hs7-wV1dfsWw8kiXpLfA5zFMKcr2rjd6q6ixbFpT6qjUhPnDl3OgeId998ir6bQIDHyGM4zLEW8ceUoxL8iFOj38yytyVuw_C7jYZ8DmuL0tp0iWyH69CzDmAmAlWvGt7zdEupLyJSNLlUyglepLACkx21SS-SE7CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=UJbFzQ7lulxmip0DlKVY2qfI3nvXAIlvqJYKLQOdGS85JDmMN-hKIXRkmdl2s1fNku6WrBrj3AD0tiT9Ev3pp_UXSjZRmmhxNKyAQ5owRDpuyZCVB5KDTg1WyNnM84Bnhd_FxFUDxe9JFnNKXi517H1-hz10xBkp3Z1XK5CyzgtWDTMdRJQ2hs7-wV1dfsWw8kiXpLfA5zFMKcr2rjd6q6ixbFpT6qjUhPnDl3OgeId998ir6bQIDHyGM4zLEW8ceUoxL8iFOj38yytyVuw_C7jYZ8DmuL0tp0iWyH69CzDmAmAlWvGt7zdEupLyJSNLlUyglepLACkx21SS-SE7CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بندرعباس؛ امشب
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68911" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68910">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
دقایقی پیش صدای انفجارهایی در قشم امیدیه و اندیمشک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68910" target="_blank">📅 03:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68909">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=YbsQEvE6HXbh6tHiP2Hwgm8ph_tl9oM50Gcc7haHgI-hwov2jH1uq6Ru7hNke7LqABZIEmXN__Cu2kn0iFrqbNWTUh9r_XzIqIi0veRYkKKedBFNtKgbgqRjuYciCui_KPytQno4jCABHK1m8PvyYLs8TKcjjoeO00A0DW2WzODBRZd142b_JvS_Py-a1J5IuHkgHjNIpcP4q6nBAMC0Ie0U6wF8P5vq-DgqjjS-frIpdndWc1XvS1hP3dlXG6OBbTIChpmm1pzRBVY2gx16BAOrBnwnF2TcbqULuUgSrdyqEKnl8oxIS34E6anbb8JAM0dC3iJN7pHu7uer1yR72g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=YbsQEvE6HXbh6tHiP2Hwgm8ph_tl9oM50Gcc7haHgI-hwov2jH1uq6Ru7hNke7LqABZIEmXN__Cu2kn0iFrqbNWTUh9r_XzIqIi0veRYkKKedBFNtKgbgqRjuYciCui_KPytQno4jCABHK1m8PvyYLs8TKcjjoeO00A0DW2WzODBRZd142b_JvS_Py-a1J5IuHkgHjNIpcP4q6nBAMC0Ie0U6wF8P5vq-DgqjjS-frIpdndWc1XvS1hP3dlXG6OBbTIChpmm1pzRBVY2gx16BAOrBnwnF2TcbqULuUgSrdyqEKnl8oxIS34E6anbb8JAM0dC3iJN7pHu7uer1yR72g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68909" target="_blank">📅 03:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68908">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=kZjKHck-fKxtWrmGTtzRfDk6Ykp2lSY-afthFKkHYMi1WbVC8k9R8e1jbY9t9nyH-YEoHa0Uy365oI4CWhT4jbve3imDMb5NpUy6CqaKtAP3IkM7wYBJ99lpDa13pSFIstB48D_9kURyRpxfQR5kmW3va9gw3TTh6KZ8e6mmG4f0gU6HoszZrAETkAIjr0K7PkvcDutLmwrTB0j0gdNlN62sh7A7dxpRIr0RgKy1Wx2cUOu0VogSmXGHj0PwAHXm6fLvuxCbQ8HFxim3bibIxpzYEuxyd_im7XyC5-6pxxh-yzXmEN9bRmT1LFOtYWE9BnuMnWU_iA4XiUikdxcBFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=kZjKHck-fKxtWrmGTtzRfDk6Ykp2lSY-afthFKkHYMi1WbVC8k9R8e1jbY9t9nyH-YEoHa0Uy365oI4CWhT4jbve3imDMb5NpUy6CqaKtAP3IkM7wYBJ99lpDa13pSFIstB48D_9kURyRpxfQR5kmW3va9gw3TTh6KZ8e6mmG4f0gU6HoszZrAETkAIjr0K7PkvcDutLmwrTB0j0gdNlN62sh7A7dxpRIr0RgKy1Wx2cUOu0VogSmXGHj0PwAHXm6fLvuxCbQ8HFxim3bibIxpzYEuxyd_im7XyC5-6pxxh-yzXmEN9bRmT1LFOtYWE9BnuMnWU_iA4XiUikdxcBFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
لحظه وقوع انفجارها در تپه الله اکبردر بندرعباس، دقایقی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68908" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68907">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbLprXmFD-IKkEmwjyxyJSdB-qlpwPLANdFitgFiB67Bw639BuQCap91PEiWKNilazQNpqf8WSwEUGHeLpHC5EdoXH_3lp-IrgwKs3IJFNFAOwLm-XAh3CyE2H60cSIwVyQzfnFl67PKJ3ETgo4AZPSTClIUy79Wt6UA5e3Bu8dvA1TEvvFpcBfwXJWp0JuggjiQWsbkIoFmChzhpjhgX-ToGEkv-VACS8jeVvzid3pGxytruuzIAq_lOy0EiZlYIktuO2pToGUTYgPB2aauXYAbrBiAkdmPDC5_xdDaWuExzC0KA1DLnjqS7sAuhz7hpd8pDW9YolftpBqmtsbeZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68907" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68906">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی  @News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68906" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68905">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=QxJKnv2a0EmNjla40zrOOTYCcGcro8r8Q_B7jXirdLcymFsc6vLt-1VssZvAPbwnHItGpIuWInVvdNpZpLz6CHMK2JSD6vKUZ5wUfu1LAw-qXzVpm5nt1bHQACDXeTA00KWcjdKje9_UsSKvPcrN2xyeai47o3BaERW9rpJIIPMWLGm1btV7HlLLjvYbaCuZhN26xaNjIAEq-UzvinFz13m8grTG51oIMopHHkIMhZYcQD4xJG_piW9hQRp8O2PWArfrw2AH7TnihpHb1U_x9RQbQC3FlrLeMm0-f1rGcfyVre6uHC6lAk5Lig_unyF76vuDfSbDuJ6N6nKLiUMnFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=QxJKnv2a0EmNjla40zrOOTYCcGcro8r8Q_B7jXirdLcymFsc6vLt-1VssZvAPbwnHItGpIuWInVvdNpZpLz6CHMK2JSD6vKUZ5wUfu1LAw-qXzVpm5nt1bHQACDXeTA00KWcjdKje9_UsSKvPcrN2xyeai47o3BaERW9rpJIIPMWLGm1btV7HlLLjvYbaCuZhN26xaNjIAEq-UzvinFz13m8grTG51oIMopHHkIMhZYcQD4xJG_piW9hQRp8O2PWArfrw2AH7TnihpHb1U_x9RQbQC3FlrLeMm0-f1rGcfyVre6uHC6lAk5Lig_unyF76vuDfSbDuJ6N6nKLiUMnFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68905" target="_blank">📅 02:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68903">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=R_0wCbT7RbCgUsLq-xhDy9g90sVDKrqrnZ8qF47Yi8ZKPe1e6hR8hdhO9_J8fn-3ShnymvVM9YnwKuGBRZOLB6NDsjARtpdDJodam2zoLbHQDySOEcrqDPkpwblm7IeSQtgZS-KrqvlXs1nyWcGl2MdgN__q59D3aKXYpZiNMdb_Vnn9fwf5Jh0cqnVnLX5SkJHe1O0tM1yH2sq77aI5jMdbTbH9nTZcLJtsAhl9FZtpV9WhRGHKhdk3_lAsI8OplRNML88qYdDUnixRPz_LG8I7gi-pmzYRGfBD4-X9DRbUI0OrleHG9riwRMc6esLvYZRRt6E2FzgB1dCXUKvGQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=R_0wCbT7RbCgUsLq-xhDy9g90sVDKrqrnZ8qF47Yi8ZKPe1e6hR8hdhO9_J8fn-3ShnymvVM9YnwKuGBRZOLB6NDsjARtpdDJodam2zoLbHQDySOEcrqDPkpwblm7IeSQtgZS-KrqvlXs1nyWcGl2MdgN__q59D3aKXYpZiNMdb_Vnn9fwf5Jh0cqnVnLX5SkJHe1O0tM1yH2sq77aI5jMdbTbH9nTZcLJtsAhl9FZtpV9WhRGHKhdk3_lAsI8OplRNML88qYdDUnixRPz_LG8I7gi-pmzYRGfBD4-X9DRbUI0OrleHG9riwRMc6esLvYZRRt6E2FzgB1dCXUKvGQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68903" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68902">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MK15Ozq0c9nupFY6sSIXlvVgm_bBm0JcYfl1YBk7CJ9T3n7IKkGp5gh4JFqK1dsuyHWEMBwshFaYJM_iwJmHasX1FKAM-Yn1FScUVTZpxeh-9a3dsjXLiEtThuAPPwLtxi_te-HQX5LG84_XINuf-rAB54kl2ErtkdH9vUmElkrS0UWG4zR66iSzfmuSqslNkeaNDRLVVWh6kht6CjEydKkI0Z5kANp8q3mOA_MJrdeuDWCQh65mAZrGB4tSd5J6cZH4av1bh_h6HjrbOs-K9PMCLgLcstYdZD3UMotafhpncLs_u6f5xhxc6QEGk98LHxhC5OXxrHk3b0_AqC65bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی امروز ساعت ۶:۴۵ بعدازظهر (به وقت شرقی)، دور دیگری از حملات شبانه علیه اهداف نظامی ایران را آغاز کردند. این سیزدهمین شبِ پیاپیِ حملاتی است که با هدف پاسخگو کردن ایران و کاهش تهدیدات سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68902" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68901">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدیدی از حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68901" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68900">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
چندین انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68900" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68898">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=Nm6x4n32_85Kvq0HnsAf_LovFrg0wE2N60hApNI12YbaFNupMXgSA73v62w-vbrWmlCxNYb2Pl-MouxM_rQzN3AmG4Lbz8N3ZpoJt1jpT-zifbhj36WbHzqU1z2QgAKC0vzKmTGiAAi29VVywPy4IryFdxemk3oOK9ByQtzjNbPjdPVlxTkrYwMjSd87TPf3XpE8WGRTnw296oTrwq4Hx18gjaL_3pwI_BUZ8UM08yShtXwuZFfhC9R6J0IK5szV0HHbtQfa_Pe4FWIE3hJlgf6_m2GfB1Tbj3XJew8oJbEwWDY3laujLnhJ0Eqory1X-0GimQJQkmitCVR06fJlow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=Nm6x4n32_85Kvq0HnsAf_LovFrg0wE2N60hApNI12YbaFNupMXgSA73v62w-vbrWmlCxNYb2Pl-MouxM_rQzN3AmG4Lbz8N3ZpoJt1jpT-zifbhj36WbHzqU1z2QgAKC0vzKmTGiAAi29VVywPy4IryFdxemk3oOK9ByQtzjNbPjdPVlxTkrYwMjSd87TPf3XpE8WGRTnw296oTrwq4Hx18gjaL_3pwI_BUZ8UM08yShtXwuZFfhC9R6J0IK5szV0HHbtQfa_Pe4FWIE3hJlgf6_m2GfB1Tbj3XJew8oJbEwWDY3laujLnhJ0Eqory1X-0GimQJQkmitCVR06fJlow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران اهداف توسط ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68898" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68897">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=DUQo2VBs00OQhSiRSDcCoNGLCVafiRLAGYKZF2J-sGCfNPAXVq7sS098AzE2mKA97OiqBmNF3vKrBSDPStcwItjRo90szFNAuR-P2lfIvgmlfzT7vDBsEMeLgh8tRlhgMC12LkKMYHjRfqVOARXPLX4uvThSwXHnv3aml1NxT4WlWaRqGfh7H5fLpgIZJr58SFBsHaCfkfW3wbE-2fvOctUipgVPnAESyuOBdjwjbkduAGJt3JV6-_MkVRk6iiz1Z5g70TNlMxYlbSzsCXcTC1lUGHg9Ik42n3PY4JmJrN4_sI7Ck1dBmUDvS0pAH8BQ1PgZ0P6Lda9OgPSo1DHJGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=DUQo2VBs00OQhSiRSDcCoNGLCVafiRLAGYKZF2J-sGCfNPAXVq7sS098AzE2mKA97OiqBmNF3vKrBSDPStcwItjRo90szFNAuR-P2lfIvgmlfzT7vDBsEMeLgh8tRlhgMC12LkKMYHjRfqVOARXPLX4uvThSwXHnv3aml1NxT4WlWaRqGfh7H5fLpgIZJr58SFBsHaCfkfW3wbE-2fvOctUipgVPnAESyuOBdjwjbkduAGJt3JV6-_MkVRk6iiz1Z5g70TNlMxYlbSzsCXcTC1lUGHg9Ik42n3PY4JmJrN4_sI7Ck1dBmUDvS0pAH8BQ1PgZ0P6Lda9OgPSo1DHJGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین به اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68897" target="_blank">📅 02:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68896">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3266056eac.mp4?token=ew9FuU-ELu0rmzc0bof_N7vDqFgcNQTt7eJzc3cV-fn6c3eJbDA9wZj5OKADrgu4uRn0z6Ct5UNXqhE1oivduY2r4SdEDcrwtyR2OAGUDFbJUFMRbQotUb5Ej8szA2J161vgihVtiEipGv-rtbWhl6JrW7TRt9Q24kOFcbr9Y2UGAZoA1o7IvEXiHeYj3_uwgwNphNaY8NA4AjEtOLtsRr5rA8iPb1ubfrcZ-bgLUpBKXqEro5ZDcZD8r3boqjcZ-pnIfPF_0m6eGe45F2uwHIYwrVUq99d6AdnbunqD_jmon-OvNHTzVAw8xHePrEMa8xtsG1OWt2XNQuJ9aq3Jcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3266056eac.mp4?token=ew9FuU-ELu0rmzc0bof_N7vDqFgcNQTt7eJzc3cV-fn6c3eJbDA9wZj5OKADrgu4uRn0z6Ct5UNXqhE1oivduY2r4SdEDcrwtyR2OAGUDFbJUFMRbQotUb5Ej8szA2J161vgihVtiEipGv-rtbWhl6JrW7TRt9Q24kOFcbr9Y2UGAZoA1o7IvEXiHeYj3_uwgwNphNaY8NA4AjEtOLtsRr5rA8iPb1ubfrcZ-bgLUpBKXqEro5ZDcZD8r3boqjcZ-pnIfPF_0m6eGe45F2uwHIYwrVUq99d6AdnbunqD_jmon-OvNHTzVAw8xHePrEMa8xtsG1OWt2XNQuJ9aq3Jcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بمباران سنگین اهداف نظامی در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68896" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68895">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از بمباران سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68895" target="_blank">📅 02:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68894">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
فارس:
گزارش‌های اولیه از سقوط یک هواپیما در آسمان جزیرۀ قشم حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68894" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68893">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68893" target="_blank">📅 01:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68892">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نیویورک تایمز عملاً تبدیل شده به فارس و تسنیم
😐
آخ که چقد این چپ‌ها ولدزنا و حرومی هستن
#hjAly‌</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68892" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68891">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68891" target="_blank">📅 01:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68890">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drmNONf-GMxb1K0_QPuisjzx7QjpC_hqz9Qn2xZ3sGwZjCkOdoSt7ShzVR8E8rTomOcm9aKAQcS8wvLHAeAsh6o2-QhjRvfU6CQCod2NJ3DSNOM2jdPMscKv18SX1AUCU-1Sd-VwdUJozy96X9ANCB7Zkt3lC0__6U-eObC0T8ejHKZQafhDT4Xa54Ue_H9Ykt0piYg0rjpePWU83ipWQDaGrga7nhgAZYyoClc4TxPixYzsjU8Qs-qKnXOcDoqz86a6NTWSt7jeV3j65Bc8JbXgkbeiuonBbNjlRE7TCp5WE4uLUjaPK62BKUDoQTOPzR_QYdvrnrbewZk3W7KRtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=fHGGf1k84exqJS2mz_vcPLh4ImUcGqCfGyNlZWQ4L0H5ozMQHvXov1kCJTBYoqp8NwHZK5Bbn1Dw5iHk6nHJyyEBDv9PbitRqdJJlS7-Jy-cKw5XwNoiCv8toerGE8zMbJ__mX7AFvTiuVBab8p5T2t3HRZfh2mdAbx96MGNBiuG14yK_gE9vXMSj8HdNCQFMEDTb6lYT5gz7fqmpc5V9tdv3l1RhC0sRbfNtOVlVwwBbKTmKpPC62OUToCBt4sNL6s-K2smLj1_U4x3248gwHrleE6ELzntU2CvS6B6OJQSXrBvhwNamxurKlkNqjeiwwY3kb5v57fnzy0hj7PYbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=fHGGf1k84exqJS2mz_vcPLh4ImUcGqCfGyNlZWQ4L0H5ozMQHvXov1kCJTBYoqp8NwHZK5Bbn1Dw5iHk6nHJyyEBDv9PbitRqdJJlS7-Jy-cKw5XwNoiCv8toerGE8zMbJ__mX7AFvTiuVBab8p5T2t3HRZfh2mdAbx96MGNBiuG14yK_gE9vXMSj8HdNCQFMEDTb6lYT5gz7fqmpc5V9tdv3l1RhC0sRbfNtOVlVwwBbKTmKpPC62OUToCBt4sNL6s-K2smLj1_U4x3248gwHrleE6ELzntU2CvS6B6OJQSXrBvhwNamxurKlkNqjeiwwY3kb5v57fnzy0hj7PYbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
دقایقی قبل دو فروند موشک در جریان حمله  آمریکا به محدوده روستای مسن در جزیره قشم اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68888" target="_blank">📅 00:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68887">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b133a06016.mp4?token=o3yHaJJQt2WoKs65T4KC0yyaaQlZRJjESk9rdPpsgMzLLdVEswDJw6KP29z5_oAlSRoIE0F929zIhDIUw_h0NIjvCkoy3LKGnLlrmdGkGpRktIjrEfXAXwQuO8xzVNfcm5CmYht17SvFA6NhRBDXfATFGxO-c1CQEUGla3UL3cZp3dNR_fAdr4VYKNGq2d0ckW4iSRSdziJK_Ictjr8zc2Foy3-TJKuE6wLSfoGCkNyKFY9t18ru1bTXdvY5nbpXDXUPprjHvfbB3JsqoKc41Y3o_R7GQVwsLNxVLP1NBOvoR-ZtDqlyy7wHsNxwWdRWL-5qpAprNeE6FDa_VjtyyYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b133a06016.mp4?token=o3yHaJJQt2WoKs65T4KC0yyaaQlZRJjESk9rdPpsgMzLLdVEswDJw6KP29z5_oAlSRoIE0F929zIhDIUw_h0NIjvCkoy3LKGnLlrmdGkGpRktIjrEfXAXwQuO8xzVNfcm5CmYht17SvFA6NhRBDXfATFGxO-c1CQEUGla3UL3cZp3dNR_fAdr4VYKNGq2d0ckW4iSRSdziJK_Ictjr8zc2Foy3-TJKuE6wLSfoGCkNyKFY9t18ru1bTXdvY5nbpXDXUPprjHvfbB3JsqoKc41Y3o_R7GQVwsLNxVLP1NBOvoR-ZtDqlyy7wHsNxwWdRWL-5qpAprNeE6FDa_VjtyyYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امشب تو میدان ازادی تهران
زیردریایی سپاه و سامانه‌ موشکی ذوالفقار بسیج
به نمایش گذاشتن
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68887" target="_blank">📅 23:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68886">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osx4Tgp7KJII7ST0kJFeXV85mZoYtKLTGIwKcyUGTep9XyVHV2rIfzXSKeZyQKBveHlQzHEs-3NVXBp_YnlxfjC7jz0CU1v5yry-KBUIDhDGVlAYw8vOsA3QTy2ONyneK1O6PoQAu8e2jkQJhIgwCtWFjMgp_zHnad50iJ0akrAPxQIFrRFomAiqCEuoWgKyACxrKCyxpudcbfOeiWrRJR7MK4z1_XhIApuJFW03lF1l3QUFz9bByInFhv2s-nB9qgcGmVvKdp7cGEgbM_JrFQAZIdc9TQsGl5Pyp4Gl1waPxjfTL3nF_Qs0TRJN0JrEOMgsKJJTYrez4b6KjJuG-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک دیپلمات آلمانی در گفتگو با شبکه «فایتوکس» (Faytuks) می‌گوید کارکنان سفارت این کشور در ایران خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68886" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
