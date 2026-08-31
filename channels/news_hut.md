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
<img src="https://cdn4.telesco.pe/file/DpwU85WkkTHmIyBfLtCzPo4brBpvbgP3fZ-pkYF9o8no2I3h4w79Z23_9HDg87q2lu8aChM1QNjilYl0ez_efsZjHF1Ihq9x3BYQJIOKomEwnLg_MihA34yjV2Otzx6y_2oggQrFkyyA7yWhQRoQZwvMcjYUOLbLzQq1iIzQg7ZXoUh9WpeWiW-0awuCBklTq0iaYcX-6mqhVZd9FSs3s5GpMHqCGlaVVrODG5EeraxV4nAt-j85dwltDMa0VuREfFOXNWetRtbqRTE2843y-iEKRoKE3MVNRWIZfDARnSp7Lf9fKe14708Un0ShIr01wja48lJe99_tqrU7rTQOhg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 114K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 01:27:09</div>
<hr>

<div class="tg-post" id="msg-70894">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🇮🇷
دقایقی قبل سه موشک از سیریک استان هرمزگان به سمت شناور ها در تنگه هرمز شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/news_hut/70894" target="_blank">📅 00:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70893">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):  گزارشی مبنی بر وقوع حادثه‌ای میان یک نفت‌کش و نیروهای نظامی در اقیانوس هند دریافت کرده است. به شناورها توصیه می‌شود ضمن در نظر گرفتن آخرین اطلاعات مربوط به امنیت دریایی، نسبت به شرایط عملیاتیِ در حال تغییر هوشیار…</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/news_hut/70893" target="_blank">📅 00:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70892">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0EY8wprVwSEm4vhKw117kz0dhw1J0N2qe8Hccb7_dEWQkc3Tlu7epGDCzyaMmaDHSNS4YDte2I-F3ncoDL3gB1WVaEtONlT-bO3_fSuQKz3Z9mfQOJi4llFQmPw39cI8Jm7te7UqXjbUCWzFjlLsLA1A6LCt8f4lgeeXZ221HlyeVhh-CMQDeONuDkwKjtscwMBPinNkWSbTEDaYYt6qtp8H-VQZwWmkp2Yg8goLdp5GJs2Z3OFB0Nl3K74uL0Jbcq2uz_9cS3zcOq7WoWksFQgbVvMW7nyKjf4jLzHAC1KFWIAIwGfh8AqJlC-0IkvV0uH7RY1GW7QE_01lGBIZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO)
:
گزارشی مبنی بر وقوع حادثه‌ای میان یک نفت‌کش و نیروهای نظامی در اقیانوس هند دریافت کرده است.
به شناورها توصیه می‌شود ضمن در نظر گرفتن آخرین اطلاعات مربوط به امنیت دریایی، نسبت به شرایط عملیاتیِ در حال تغییر هوشیار باشند. مقامات ذی‌ربط در جریان موضوع قرار گرفته‌اند و تحقیقات در این خصوص ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/news_hut/70892" target="_blank">📅 00:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70891">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1acb363e.mp4?token=ZCMB7iB5xXvE_FZyXJyXS8zna0lKZkDB5NYuTVTj1vKvnqTDV-25p_eh5tvEJD-ERqdjw_EoXAvNlaoUtbXqsBeP6ZOVuG3eoeCmHxuzwgdjIrPi84aWtDuj9ThCsSzTM7f2_gUYgY9HYz9Hrgz0_ofjJ0E62DYlr1jZI4gsARDO7Dq53du0cKOAKyhYXWjJXqn19EdAKDAE8QdjZHC8XWyeLSyqq-BU7_omSk6fnw4TSvSSYTpsmXtAWvltHjhuIje2fAqMZmiDaO7g3TwRzrxE-atyj-Lk8cDTEznihrEWKdVXBbY_Ui9JRpcL0qoctHe7MwyZ15rzKJ9yjYPgu4cwkC0_xeJO98ilUC-6nAhO4nFim4ri9Qglniszue9W85BaUDSDFBp55rbsG7wzXOtUnF2riTDRnxb2EcbN-Cxw5O6Ga68jufXxjy5FdE_RXD3om-kdJ3uE611roh49pOSsY2PhbvWnjUmoMxriSEFrdXWcD7fo9_Otj8YC5SNVeYR2upe_bhrstHzmb099vxsM4IVxN8gra1-t8_w0K_2wpuh2sb9AtosvfAmiGgDWwCr99ktsB4kxfBJ1uNq6KXsLRIKmgN8BUj2BeK4T3-Lh9M923oLYZLQ3FyHsf75SZ9hmjHSDj8zlSohqcE5y2sy-1fcOxrPdj3grggB47hc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1acb363e.mp4?token=ZCMB7iB5xXvE_FZyXJyXS8zna0lKZkDB5NYuTVTj1vKvnqTDV-25p_eh5tvEJD-ERqdjw_EoXAvNlaoUtbXqsBeP6ZOVuG3eoeCmHxuzwgdjIrPi84aWtDuj9ThCsSzTM7f2_gUYgY9HYz9Hrgz0_ofjJ0E62DYlr1jZI4gsARDO7Dq53du0cKOAKyhYXWjJXqn19EdAKDAE8QdjZHC8XWyeLSyqq-BU7_omSk6fnw4TSvSSYTpsmXtAWvltHjhuIje2fAqMZmiDaO7g3TwRzrxE-atyj-Lk8cDTEznihrEWKdVXBbY_Ui9JRpcL0qoctHe7MwyZ15rzKJ9yjYPgu4cwkC0_xeJO98ilUC-6nAhO4nFim4ri9Qglniszue9W85BaUDSDFBp55rbsG7wzXOtUnF2riTDRnxb2EcbN-Cxw5O6Ga68jufXxjy5FdE_RXD3om-kdJ3uE611roh49pOSsY2PhbvWnjUmoMxriSEFrdXWcD7fo9_Otj8YC5SNVeYR2upe_bhrstHzmb099vxsM4IVxN8gra1-t8_w0K_2wpuh2sb9AtosvfAmiGgDWwCr99ktsB4kxfBJ1uNq6KXsLRIKmgN8BUj2BeK4T3-Lh9M923oLYZLQ3FyHsf75SZ9hmjHSDj8zlSohqcE5y2sy-1fcOxrPdj3grggB47hc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا استفاده از سلاح هسته‌ای علیه ایران را منتفی دانسته‌اید؟
🇺🇸
ترامپ:
من هرگز چنین حرفی نمی‌زنم، اما پاسخ «بله» است. هیچ دلیلی برای آن وجود ندارد. چه سوال احمقانه‌ای. آن‌ها از نظر نظامی کاملاً شکست خورده‌اند.
من آن‌ها را شکست داده‌ام، آن‌وقت باید علاوه بر آن از سلاح هسته‌ای هم استفاده کنم؟ چه سوال احمقانه‌ای.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/70891" target="_blank">📅 23:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70890">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4ca68587.mp4?token=Bndr2fGlvKupq5ucyy8geCuubA10yNfyW_dryQvVz_SzZZO6Bzm6ZUvgcygsq2LtAk18HDypg2_sHZTvLIOvc1bhPFQw_osIAFTxGerslDXOri-DAMHEF1gevS-cWoQ9EOtBUXNO-mUG3ETPlC1QC5BK34WaMhJzWdBO7ks-4U4idbnLo7P55nOx51OlkXLD-myJjYKKU8o8RlrpR8obafrm-MhOaLV0uO5mQpH4Xutv7Mxi1N2LdeReVAKdJRFtAI5UkTm9z8nRPYXfcaEXuZpMrm1QrL1Z1K-94Fm4xafwtuL9Q_X7cW6fulDvFCb0T8NC3okiVc-LwIsI4V1FcIGmg_1OIPQ1KJBYiF8DUZGD1PQ9GyYc3B0h-R2aLUm1DyNM8K7aNSzc_eTvwBmbUamwjRjckbWLeE7Tg13a_USfhrjR5Pt5uAdaEmY-m2A7_YJ-ajn1sCks5AeU1ELL8LNaUA9DBySamL9wNqQwmE96m_N8cJLe4AXmknlMYueMGnINdwSIPvfpNFCpt6hAmY92g1uL7kM1Wj8RhK3ex_kb4m7cQth_9tRbHf_iokSrAjGLph0W5FJY-QfNDLzSnM21LOHwLcKH0SlaVLwQ2u4DFt3dzBFCfkfEN8AJbvKsZ8ZzZM6YtVFeM3P7B_2RXHRXjzXUmc_JSRLpd8DGyUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4ca68587.mp4?token=Bndr2fGlvKupq5ucyy8geCuubA10yNfyW_dryQvVz_SzZZO6Bzm6ZUvgcygsq2LtAk18HDypg2_sHZTvLIOvc1bhPFQw_osIAFTxGerslDXOri-DAMHEF1gevS-cWoQ9EOtBUXNO-mUG3ETPlC1QC5BK34WaMhJzWdBO7ks-4U4idbnLo7P55nOx51OlkXLD-myJjYKKU8o8RlrpR8obafrm-MhOaLV0uO5mQpH4Xutv7Mxi1N2LdeReVAKdJRFtAI5UkTm9z8nRPYXfcaEXuZpMrm1QrL1Z1K-94Fm4xafwtuL9Q_X7cW6fulDvFCb0T8NC3okiVc-LwIsI4V1FcIGmg_1OIPQ1KJBYiF8DUZGD1PQ9GyYc3B0h-R2aLUm1DyNM8K7aNSzc_eTvwBmbUamwjRjckbWLeE7Tg13a_USfhrjR5Pt5uAdaEmY-m2A7_YJ-ajn1sCks5AeU1ELL8LNaUA9DBySamL9wNqQwmE96m_N8cJLe4AXmknlMYueMGnINdwSIPvfpNFCpt6hAmY92g1uL7kM1Wj8RhK3ex_kb4m7cQth_9tRbHf_iokSrAjGLph0W5FJY-QfNDLzSnM21LOHwLcKH0SlaVLwQ2u4DFt3dzBFCfkfEN8AJbvKsZ8ZzZM6YtVFeM3P7B_2RXHRXjzXUmc_JSRLpd8DGyUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شرایط وحشتناک بازار با قیمت بالای دلار.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/70890" target="_blank">📅 23:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70888">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iReVn0kQpskLd4lTn6-KTipo7l2DHElOjd2TZCUHG1bLq33nIumKd-cXAGnhGlnC5qrzUU33N3ib-lxryX_2nm7ChFllmtadMquolYa4zZtSs-gje1_vzcI7aJAiBifTZ-vsNkHGktn7cv5hu8Jy2tttVOezRXyzFjZzSuNruFmlQu8oge61Wux8_pqRInEA0UMNmoSzbNOEkrKT_1upLCgc1leNjb-oFneb-_1HYmWCk9Tc3o1QZrb-KPHchJyTo-Ni5hL_2_fDyXO9Xj3tZqsp34_1kZ3-YwmTdi2E3XjfHBHg95YtbI4W9IKDVe8e19WI35lt8udXKrXdl43TdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M6D5TEsFe5wHRJhkmjKrgIoNBD7G4x2vGICKds-WBPbkeniNRtsEVJdxycmge4tRMKlxwNxlWZlx4cgq6YmlNFUlygepAjc79mCai7dwVvBM1umiem1VjF_WM74s8oehNaeypMJ1qFKk5wNCLr0KCfRsnD3eQ5bTndQVA1IczxC_whHI1bR_V1V-ihAOJ9dwtqewgvM47wg2PoVapmn7l00_h1IS0HV5enGbCdcpoFYI-jkR7weXy_9zeSbIUxKS2kAkUuHQHsD3sPdtqo_yGKYmN1_LYFZHLBYZTfebmh4fnfRvfObVwykE2wu2KMosNvAr0AT31rSeJEr9EmxXYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سلنا گومز و همسرش:
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/70888" target="_blank">📅 23:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70887">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f7f766eae.mp4?token=SU_eXnnawLJ3u898lf8zsZ-OgZUrQzHjx3oxCzBzzrdr-YuG_2P6AT-BkwaVGnbHeRDrbMc7t1L1HUq2yW3-k_3lwztGWuOwtESYaxvK6ijnfWY7qgjWuu7U_-AaA7LzsVFiTVf6gqKgI-PXssoxsF9avg1blvrlGCG0b1SF3dp-lL8UQ7Gei7LF029zZkqjcR8_HNOcFDdrZQBACSMFFa_zjXs3pmcHQeXlkJ88DfJxYbNmuM7A9CEmji_7AJV1G-0MuBnEibkMRwyQigzOaAL2rLbELF6rShb6U1UnCbOZgf9RU2ENtn-LCY3ZOkr_2ilEOx6XeCX7AeJU40EqZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f7f766eae.mp4?token=SU_eXnnawLJ3u898lf8zsZ-OgZUrQzHjx3oxCzBzzrdr-YuG_2P6AT-BkwaVGnbHeRDrbMc7t1L1HUq2yW3-k_3lwztGWuOwtESYaxvK6ijnfWY7qgjWuu7U_-AaA7LzsVFiTVf6gqKgI-PXssoxsF9avg1blvrlGCG0b1SF3dp-lL8UQ7Gei7LF029zZkqjcR8_HNOcFDdrZQBACSMFFa_zjXs3pmcHQeXlkJ88DfJxYbNmuM7A9CEmji_7AJV1G-0MuBnEibkMRwyQigzOaAL2rLbELF6rShb6U1UnCbOZgf9RU2ENtn-LCY3ZOkr_2ilEOx6XeCX7AeJU40EqZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کنسرت محسن نامجو در پاریس، ۷ آذر ۱۳۹۱
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/70887" target="_blank">📅 22:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70886">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0452a7515b.mp4?token=UTEGLMQB4Gj__qZNYFIyvhmzVtRokTvPWr_MfsIq7nC4fSjeIlULv-RrfhIpoiJjXcW0sdEeR-Go8jcpdfdwlleYZB6dj7on8PxeROx8eI7hsSdJoFdAGbZaiy42EjWDDeOqL9476RhNj5PI-45WriHCCykEb63N58ORqDGEyOl1fTfzRaQ4k83yODua98zRjoziHdh4a1EroCGbrlgOSaox3LHNmeExZNNB4GH4Jwm5DQYaoyHYeIL82ESdzxp2t_rU2Dk-4p3__Ok11Yfv82SFigaKNHVvXZ9n1GCQTYH1dFi5e1gRVsQe_RIhgCKGdIlbFJZibcYtHmfGsDL8_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0452a7515b.mp4?token=UTEGLMQB4Gj__qZNYFIyvhmzVtRokTvPWr_MfsIq7nC4fSjeIlULv-RrfhIpoiJjXcW0sdEeR-Go8jcpdfdwlleYZB6dj7on8PxeROx8eI7hsSdJoFdAGbZaiy42EjWDDeOqL9476RhNj5PI-45WriHCCykEb63N58ORqDGEyOl1fTfzRaQ4k83yODua98zRjoziHdh4a1EroCGbrlgOSaox3LHNmeExZNNB4GH4Jwm5DQYaoyHYeIL82ESdzxp2t_rU2Dk-4p3__Ok11Yfv82SFigaKNHVvXZ9n1GCQTYH1dFi5e1gRVsQe_RIhgCKGdIlbFJZibcYtHmfGsDL8_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبتای بدل ایرانی آنجلینا جولی:
تا حالا یک دفعه هیچکی دست رد رو به من نزده.
به هر مردی میگم با من ازدواج بکن نه نمیاره.
از هر جای دنیا باشه سریع خودشو میرسونه پیش من.
بعد دوستام میگن تو مهره مار داری دعانویست رو بده به ما.
علتی که اون هم قبول میکرد این بود که چون من شبیه آنجلینا جولی بودم، او میخواست این وجود رو در کنار خودش داشته باشه که مثلا مهمونی میره، پیش دوستاش میره پز بده.
من حتی بیماری‌های مشترک با خانم آنجلینا جولی دارم. هم قلشون هستم. ما ژنتیکمون مثل همه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70886" target="_blank">📅 21:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70885">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
📰
اکسیوس:
ترامپ طرحی را برای حملات محدود علیه ایران در نزدیکی تنگه هرمز بررسی کرد.
وزیر جنگ از طرح «حملات محدود» علیه ایران که ترامپ در حال بررسی آن است، حمایت می‌کند.
طرح «حملات محدود آمریکا» علیه ایران هنوز تصویب نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70885" target="_blank">📅 20:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70884">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⏺
🚀
فارس:انهدام یک فروند پهپاد MQ9 در شرق تنگه هرمز
دقایقی قبل، یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70884" target="_blank">📅 19:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70883">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f517057c.mp4?token=wBtnk8YviofleUf8iUMB_5EhpsROtRzHeXWWBKM5MgLs02_9hYg0xmaKnzZx0h11NKL9LHdifBiZIFQgdE4HghAP9LodAJNtVqatZz4C776nRdCKba5UYV-ynsZNaLlG81u8XljAh8x7E-JBJZqepfkCUQOdKAYFAYf1akqkgJ2W1EoUoVsq4JSyR-Ie5sZm6uMV95uXN3nkrjZ_ztAzHWpOcQHinBcq4OP-1foa9zpFMJBZa18mEdHbDLjXdkzY-4LkIpRY62V3Dcjqf9kOkREAg_D-Wl_cXAPWrRjfyM3518QJNBwWH88R2OCBhfZH0o0LzIG0mMrkqo1tMvinzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f517057c.mp4?token=wBtnk8YviofleUf8iUMB_5EhpsROtRzHeXWWBKM5MgLs02_9hYg0xmaKnzZx0h11NKL9LHdifBiZIFQgdE4HghAP9LodAJNtVqatZz4C776nRdCKba5UYV-ynsZNaLlG81u8XljAh8x7E-JBJZqepfkCUQOdKAYFAYf1akqkgJ2W1EoUoVsq4JSyR-Ie5sZm6uMV95uXN3nkrjZ_ztAzHWpOcQHinBcq4OP-1foa9zpFMJBZa18mEdHbDLjXdkzY-4LkIpRY62V3Dcjqf9kOkREAg_D-Wl_cXAPWrRjfyM3518QJNBwWH88R2OCBhfZH0o0LzIG0mMrkqo1tMvinzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🎙
فرزانه صادق وزیر راه:
به علت از بین رفتن زیرساخت‌ها هواپیما بدون رادار هدایت می‌شوند و تعداد پروازها کمتر شده است
👌
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70883" target="_blank">📅 19:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70882">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇦🇷
پست جدید لئو مسی از خاطراتی که واسه تیم ملی آرژانتین ساخت
🩵
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70882" target="_blank">📅 19:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70881">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70881" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
http://TrexBet.com</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70881" target="_blank">📅 19:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70880">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyZ7_Fhg2OBUZNVbg9B4uBtUt9TPf2MMdWyQJkoWEGijH3KpuViHC563AMjWZqFThl4FLHJlNIM5bkvpZYf-smbGD4YjIz_jcmqMfO9rNJ1jKcTuWrUorZNIBSU788STm0ZsIfEv1qD_V0LXbIEDBS-sYiQA2gXRu4Gd9eNeX-v0L91pzzGqcI6_9eGpUDDh9vasKgvk7QxUMYO-1gmuF4GzQ1GoEoOAcGfvvq_guEENZG-ALir4Nf88YIqs1kiJMgoCO0-YjVa1__POC2wWstxn4BtZ3WGlW81QCoX4esql4vO1kj69pkososmBpUrarOGE428hrb-pWGWzZNF5Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
میکس پیشنهادی ضریب
〰️
برای بچه‌های
TrexBet
🦖
Code TrexBet:
SKCU6
آموزش استفاده از کد شرط در سایت بین المللی تیرکس بت</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70880" target="_blank">📅 19:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70879">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8uCQ53S67N_UCgJOQ0DsnC8rbFhp0EDfT5RHWOjGOjqCpvqqxpLPHvteQboZf6cgjaMzo-0bthUmV4RUxYiy-fnlsr9pQt6PKOTdc9fojpv1Jn7u4mKwZijQN__6bVflbW3EASU2MUMvmQ5x8VTeiLVT_1JdhtggfcJicjTnBTPgQSji6mMD1iQU6qFaNtDtb2vIvHpWfuHu_daSumNJSGoR36jH2q45H8A7yeYjBbPdE5HzTPeWazi8YaTrOlXlP43ZKeio1iQtAXVwWeUyhDSwStrTH7JiKX1t0SVeGm0j8P5OUaiewAm9kAwWRJ9ze_ViZwyxlB8qEYyINvy9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
💋
#فوری
؛لیونل مسی اسطوره فوتبال جهان از تیم ملی آرژانتین خداحافظی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70879" target="_blank">📅 19:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70878">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9510f51c.mp4?token=jTcPALFHQKmgC8xKM0gjnJ0FBRgA7DHMx5Qr7-7ONyLU9D0XDUQTmSdC1UhhW1CW0KknP9nmlcYmTljSfcJIp736NEn5iDKKkzH2afZC0-iE_Yddx_aV0eVsj5yZqm8f8M2V6G8swIsApJEl-7-RThc5otDv8k2VEUxcHePPUVFM_iqHjVI6OasdDBn1TGUE9dzLmcBWKi4gQu9Pq5pR16HQQ-oGksPyIaGwX0BwDWgnHpxbKAGbO84tzqYFTrZ-B8y2M0Gp8eaJu0nTBrMkxuVUD50IoEijLQOefpnhneRTbrKYD_mQ35EXfo8pXHzVeOQk-aitgzL7Hn7Z4JB2hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9510f51c.mp4?token=jTcPALFHQKmgC8xKM0gjnJ0FBRgA7DHMx5Qr7-7ONyLU9D0XDUQTmSdC1UhhW1CW0KknP9nmlcYmTljSfcJIp736NEn5iDKKkzH2afZC0-iE_Yddx_aV0eVsj5yZqm8f8M2V6G8swIsApJEl-7-RThc5otDv8k2VEUxcHePPUVFM_iqHjVI6OasdDBn1TGUE9dzLmcBWKi4gQu9Pq5pR16HQQ-oGksPyIaGwX0BwDWgnHpxbKAGbO84tzqYFTrZ-B8y2M0Gp8eaJu0nTBrMkxuVUD50IoEijLQOefpnhneRTbrKYD_mQ35EXfo8pXHzVeOQk-aitgzL7Hn7Z4JB2hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدرضا نقدی:
ما انتظار پیروزی را داشتیم، زیرا به وعده و یاری خداوند یقین و اطمینان داشتیم.
اما انتظار نداشتیم که پیروزی به این آسانی به دست آید.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/70878" target="_blank">📅 18:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70877">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8caf499f90.mp4?token=iLvM0IlrdilUfxcOoMHe5NJUVSQvfMi0DgU-kDL_hVmgJ1nMxUtQwgnbSSpHUtM7CgVKJ2xnIJTgo6izy8asFpQ8qk9QTp8yhebf__Mm7vgrO8aHKyYSnpzHDhr5ztZnXcPGIlXriNFsRpZsrfztKYMEPWuKo8UElh3bTWgq-ZpUJkgkUWBd2NgdTw4736oxiik634toLfDtwRXmTizE_P2HhVW8dxSHA3O66fIH0zrbgXbNuE_Z9UkwEo__wS9Jk9rrN6W3wWF71UXsvy6965RG4PNXmR6Woe7wxCLB9_ZWgCZ7lrHsRPuLpaG0bHPYoftFprudDQUcSQgCDUKHMoikgNsI3hX8wrCa4jUPSKQFjlZFwOUDKjTWXurnIJVlawp21ZJvZl5mYtFOaBss55x74UDPk2dWMtOD1DltSK9DRujtU_deH9eyfCDBsFipgxJjbz9yp3DfW5Al0IL1u3pmv4MlGHqLthaHDTuab4kQRE4MFQc8QRL28aIEPlbKrCmbDEUEpI1iUkt1oOdiutfcbLP-PIE4LXPjphpm5mNZ1fedHFmsvfnNDUiRLhuq-hjPTvGHzsN3NJL3YrfYQXp77Aw_wORo1KiiDyFeOEjrIvYkogmRS4RguEe2AjShBaeOQiSPD2jXvS5yHEuzhfJUtnLVoWDQCx7VZZ1YyPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8caf499f90.mp4?token=iLvM0IlrdilUfxcOoMHe5NJUVSQvfMi0DgU-kDL_hVmgJ1nMxUtQwgnbSSpHUtM7CgVKJ2xnIJTgo6izy8asFpQ8qk9QTp8yhebf__Mm7vgrO8aHKyYSnpzHDhr5ztZnXcPGIlXriNFsRpZsrfztKYMEPWuKo8UElh3bTWgq-ZpUJkgkUWBd2NgdTw4736oxiik634toLfDtwRXmTizE_P2HhVW8dxSHA3O66fIH0zrbgXbNuE_Z9UkwEo__wS9Jk9rrN6W3wWF71UXsvy6965RG4PNXmR6Woe7wxCLB9_ZWgCZ7lrHsRPuLpaG0bHPYoftFprudDQUcSQgCDUKHMoikgNsI3hX8wrCa4jUPSKQFjlZFwOUDKjTWXurnIJVlawp21ZJvZl5mYtFOaBss55x74UDPk2dWMtOD1DltSK9DRujtU_deH9eyfCDBsFipgxJjbz9yp3DfW5Al0IL1u3pmv4MlGHqLthaHDTuab4kQRE4MFQc8QRL28aIEPlbKrCmbDEUEpI1iUkt1oOdiutfcbLP-PIE4LXPjphpm5mNZ1fedHFmsvfnNDUiRLhuq-hjPTvGHzsN3NJL3YrfYQXp77Aw_wORo1KiiDyFeOEjrIvYkogmRS4RguEe2AjShBaeOQiSPD2jXvS5yHEuzhfJUtnLVoWDQCx7VZZ1YyPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سردار محمدرضا نقدی:
همه فوتبالیست‌ها با توپی بازی می‌کنند که طبق استانداردهای یکسانی ساخته شده است، اما همه آن‌ها رونالدو نیستند.
گل زدن نیازمند فردی با انگیزه، هوش و توانایی است؛ کسی که بداند چگونه از آن ابزار استفاده کند.
آمریکایی‌ها صد برابر ما سلاح در اختیار دارند و از موشک‌ها و پهپادهای بهتری برخوردارند، اما نمی‌توانند به‌طور مؤثر از آن‌ها استفاده کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/70877" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70876">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc022b8a9.mp4?token=Ib33fc2xl3uSMWgDsHsvCtj6w_nGctCnGBcrVqxKEm0l420G5DTweR4nsRD3NWGcTOufnIYi2hEocsMGodh-HhuRY0lAxGda8bxbiC4n1LCfB4nq3_nxfeWNaqwtEqgMwVns70QksouXs1LyQs5btH_ktN9GH-xB_Feu1vWxkbdPm_5NYRhc6nW0pdNh4jbDa-jWCRWQOccgWX4hyNvRBBJE0xLRVHOeCU2sF61lzgnA1mrFQBKUUP3Ckhx_sMZEKuuvdK2er-wM4f1yHCyJkrHnkyJqmPZadqGlIHN-8xnGALOQc3i1UyG-QOZR7Q5W6pawUXuWKZ29Ptn-THUJDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc022b8a9.mp4?token=Ib33fc2xl3uSMWgDsHsvCtj6w_nGctCnGBcrVqxKEm0l420G5DTweR4nsRD3NWGcTOufnIYi2hEocsMGodh-HhuRY0lAxGda8bxbiC4n1LCfB4nq3_nxfeWNaqwtEqgMwVns70QksouXs1LyQs5btH_ktN9GH-xB_Feu1vWxkbdPm_5NYRhc6nW0pdNh4jbDa-jWCRWQOccgWX4hyNvRBBJE0xLRVHOeCU2sF61lzgnA1mrFQBKUUP3Ckhx_sMZEKuuvdK2er-wM4f1yHCyJkrHnkyJqmPZadqGlIHN-8xnGALOQc3i1UyG-QOZR7Q5W6pawUXuWKZ29Ptn-THUJDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ماموران نیروی انتظامی روز دوشنبه ۹ شهریور ۱۴۰۵، به سمت کارگران معترض به استخدام‌های رانتی در پالایشگاه لیشتر گچساران تیراندازی کردند.
در این تیراندازی چند معترض زخمی شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/70876" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70875">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbEBkEvhefNG-Ynw7mMf039yGDsZHYGZeM_NpHrxS2TDha6-1qkmx42KzgteP0O8A1RWCPv9gYmeHAv8hqQ9oGGXcpKvXX2Of1A2guZfWFzqnZS3aoEphmNXoEXltb0TT9s0f32Vjphn36_OBWv2-TQ0QflPFNvepTG9d5GRlrRVwL1uxtcuKhCj_eI5V53SNQXdAMItE9TkRIwnKyHATwn6oFQj4CrhrWbYudySrbzLySfMtf3IXZn3sQ6YIEYoUKE5RCc94iL23xpCewx9qYkvJzR7jHKc7xcM8vK_mHccWNGdas2wSBSknxWPU6p2CjvQHAUsmmiCG1HWDOzQEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضع خیلی قاراشمیش (یاغی)
وزارت نیرو اومده هشدار داده که مردم بنزین و گازوئیل غیرمجاز تو خونه، زیرزمین یا حیاط انبار نکنن، چون خطر آتش‌سوزی و انفجار داره و ممکنه با افزایش قیمت سوخت بیشتر بشه این کار.
گفته فقط اگه واقعاً لازم بود، مقدار خیلی کم و استاندارد با رعایت کامل ایمنی نگه دارین و موارد مشکوک رو به ۱۲۵ یا نیروهای انتظامی خبر بدین.
خلاصه مواظب جون و مال خودتون و همسایه‌ها باشین، این کارا خطرناکه و به نفع کسی نیست.
@Moris_news</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/70875" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70874">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237073d371.mp4?token=sKPxXUhkNoYkYVnvTqOprXIm6MTCGGVbmhXsK6k5WoG9_gAmLzpD3NJ5DLOt5kZLeUFhWMEwCrt1084rlIvfABJqjkG6jUs6bc3do1ecwDmrGJsOgO1jtYBuAS4KXx1Y3mwGN6J3qmVIFhAwMaoFxgXf6xjgpP9yyv-DnMWhLdWpymhDS8Q9TkJRRZnnVSixLPC_0o-pnFoTPTfDExvZ0BZgT8tOf1d415NsZV7sv4En4ERe1sbBlTcj1TptaBgf6x2Q9zMDULNf7p4Rj94H_BbLZ0wsJV0U5MWEmIb_HtHKioNn6wmXNcCiQzmqWAgtPs19Vf10Zj4BfobhXn7Gmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237073d371.mp4?token=sKPxXUhkNoYkYVnvTqOprXIm6MTCGGVbmhXsK6k5WoG9_gAmLzpD3NJ5DLOt5kZLeUFhWMEwCrt1084rlIvfABJqjkG6jUs6bc3do1ecwDmrGJsOgO1jtYBuAS4KXx1Y3mwGN6J3qmVIFhAwMaoFxgXf6xjgpP9yyv-DnMWhLdWpymhDS8Q9TkJRRZnnVSixLPC_0o-pnFoTPTfDExvZ0BZgT8tOf1d415NsZV7sv4En4ERe1sbBlTcj1TptaBgf6x2Q9zMDULNf7p4Rj94H_BbLZ0wsJV0U5MWEmIb_HtHKioNn6wmXNcCiQzmqWAgtPs19Vf10Zj4BfobhXn7Gmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه سری دختر اکیپی قرار دعوا گذاشتن پسرا هم دوره کردن و تشویقشون میکنن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70874" target="_blank">📅 18:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70873">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48f793f615.mp4?token=MW-PZfV_gGbL1b7VaxSETmgLkvhhRyTdXjTOeH-WiEAPz7vtEOyqNOulldmxzh1R8MtDkiKxApgvqcKwVOCIDlBAqdTDeqDsEwkUqxJ9-lwDj4vcznLypEYRVu7hfBSu3rQq-yKHihKLa2Nz81DECt1M2c_4e_Jgwz0znQ2cIvFeJUylZrPHdox93bAHgpZTQDfaSt6FytyZp4tcS0ODF_KwbxVONtgmyCUIfGV3EMa0pnFXwBwJgQHMPEKm5fQ1TPzkep7p-gvpqTSH-7QITR-fFYtse8myocS5dR8f75z7DFWpQPvisURp1UA7K7H3wQYvbtzXh1gAGM2RfWIKnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48f793f615.mp4?token=MW-PZfV_gGbL1b7VaxSETmgLkvhhRyTdXjTOeH-WiEAPz7vtEOyqNOulldmxzh1R8MtDkiKxApgvqcKwVOCIDlBAqdTDeqDsEwkUqxJ9-lwDj4vcznLypEYRVu7hfBSu3rQq-yKHihKLa2Nz81DECt1M2c_4e_Jgwz0znQ2cIvFeJUylZrPHdox93bAHgpZTQDfaSt6FytyZp4tcS0ODF_KwbxVONtgmyCUIfGV3EMa0pnFXwBwJgQHMPEKm5fQ1TPzkep7p-gvpqTSH-7QITR-fFYtse8myocS5dR8f75z7DFWpQPvisURp1UA7K7H3wQYvbtzXh1gAGM2RfWIKnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
بسنت وزیر خزانه‌داری آمریکا:
می‌خواهم از اتحادیه اروپا و بانک مرکزی اروپا به خاطر بیانیه قوی‌شان در حمایت از اقدامات اقتصادی ما علیه رژیم ایران تشکر کنم.
و این گروه با هم، به این حکومت وحشتناک چهل‌وهفت‌ساله آن‌ها پایان خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/70873" target="_blank">📅 17:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70872">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0baed51151.mp4?token=BhnEobZvrVNR4_wpZ_vAu5ND6bsKSCjSEzbCErigIQH1GCHOkf3XWJuqKJAkBH0-Gw0LV8p_SC4XmoUPELe14HWLbp7ehjrwt0QWziz2zr8LCRY-m_4t4jq63UorEqBW4iSsEPIvmLi6TAU813QToGt2ueLJ25Ytmw_P299urL1mcGZp1peuS8foF0EW7y5BMbsWU3Xgy_woc4pwcP7Za9b_cJID3RpvdiTulF8CQ_EXRNmBy83e5jcDLhuCWG1jpCzL0Qq8LsmJgmEfApSvMR_OQ42LKC9i4wFq9FshhYano4TXVCYfvvWw8FJL81Ujel_5y_9COlzibFlHiYnJig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0baed51151.mp4?token=BhnEobZvrVNR4_wpZ_vAu5ND6bsKSCjSEzbCErigIQH1GCHOkf3XWJuqKJAkBH0-Gw0LV8p_SC4XmoUPELe14HWLbp7ehjrwt0QWziz2zr8LCRY-m_4t4jq63UorEqBW4iSsEPIvmLi6TAU813QToGt2ueLJ25Ytmw_P299urL1mcGZp1peuS8foF0EW7y5BMbsWU3Xgy_woc4pwcP7Za9b_cJID3RpvdiTulF8CQ_EXRNmBy83e5jcDLhuCWG1jpCzL0Qq8LsmJgmEfApSvMR_OQ42LKC9i4wFq9FshhYano4TXVCYfvvWw8FJL81Ujel_5y_9COlzibFlHiYnJig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🟥
فاکس‌نیوز به نقل از ترامپ:
همین الان با رئیس‌جمهور ترامپ صحبت کردم؛ او به فاکس‌نیوز گفت که ایالات متحده به حمله ایران به نیروهای آمریکایی در اردن — که دیشب رخ داد — پاسخ خواهد داد.
رئیس‌جمهور گفت: «ما ضربه سختی به آن‌ها خواهیم زد. پاسخی در کار خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/70872" target="_blank">📅 17:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70871">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puq4Sy8Obe_gPR842Y40_eKzhnCqPViJplqZVjYAEmiXA-c1WTVp2ljft75JOvbaMDqlHe0PSvcRUvW7dsBieNmIHXWD6HdLq2gd5kL2YKma1uFr7QdnWex9vJe-4Qh95re62N5P7jZf1Z6jsOvFDzqtiJaOqBmeVfA242w_JMMltkxQ1hmT3JvSqxEEAQmHQbkWb3mlWNCcwaoLInPoaS76FgQMwHO51fZKml72IUa4ZNS7dPqjdyX3WeEuLPLeGgylKbNNJOLnw1ZwA6s7EnLEpITh-WQdUxU1Cyy46rrntkcfYU7W5cf4X1pZpMpeDhgqEGvNBd55hU0HoLyzjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
🇺🇸
پرزیدنت ترامپ:ایران رسماً یک کشور شکست‌خورده است. کارش تمام است!
آن‌ها نه نیروی دریایی دارند، نه نیروی هوایی و نه پول ملی؛ حقوق سربازان یا نیروهای پلیس خود را نمی‌پردازند، نرخ تورم به ۳۰۰ درصد رسیده و رهبری‌شان دچار آشفتگی کامل است و توانایی نمایندگی شایسته کشور را ندارد.
تنها چیزی که دارند «اخبار جعلی» (از سوی آمریکا)، تمایل به کشتار معترضانشان (که اکنون شمار کشته‌شدگان به بیش از ۱۰۰ هزار نفر رسیده است؛ آن‌ها باید به جرم جنایات جنگی علیه بشریت محاکمه شوند!) و البته ردیفی از «چرندیات» است.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/70871" target="_blank">📅 17:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70870">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا بدونید شما اگه عاشق ترین فرد دنیام باشی بعد از حدود دوسال هیجان رابطتتون میاد پایین بعد از رابطتتون تکلیف مشخص میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/70870" target="_blank">📅 17:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70869">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841288ee9e.mp4?token=luMTin1h13fPjuAk9CymWRxobqFvGxwWrE99DsmS-Lq5fEF2Jtmt7cIYpN-41XIjN3yHQBdGNXN3-dS5YrZM2q0L7OQp4hiu_YIjX_MW-Py1mthE7SCZ1COYgq6HkWbTox-6cp2wV0bLHV5rsAs5iNHidnKYYPx2jkxxOD7hKdsO7DiMmQVsrjwBycRkd13IUEM1EBakul1kRdbNwgr2TFz51tAjTZ2h_fot6IYShGX7_uMX-x9gtsHtW4IMij21LHZqrVd3glgyLRZhEKbwa09rJ-4qGvJq8xqvucSHgaJinNdMu-7LKQ-rEDkfOhrPM5wr9UphukLEXrKINlQOnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841288ee9e.mp4?token=luMTin1h13fPjuAk9CymWRxobqFvGxwWrE99DsmS-Lq5fEF2Jtmt7cIYpN-41XIjN3yHQBdGNXN3-dS5YrZM2q0L7OQp4hiu_YIjX_MW-Py1mthE7SCZ1COYgq6HkWbTox-6cp2wV0bLHV5rsAs5iNHidnKYYPx2jkxxOD7hKdsO7DiMmQVsrjwBycRkd13IUEM1EBakul1kRdbNwgr2TFz51tAjTZ2h_fot6IYShGX7_uMX-x9gtsHtW4IMij21LHZqrVd3glgyLRZhEKbwa09rJ-4qGvJq8xqvucSHgaJinNdMu-7LKQ-rEDkfOhrPM5wr9UphukLEXrKINlQOnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کاظم غریب‌آبادی، معاون وزیر امور خارجه:
این اقدامات تجاوزکارانه با پاسخی مناسب مواجه خواهد شد.
حضور بیگانگان باید از این منطقه حذف شود و آن‌ها باید درس‌های جدی بیاموزند تا دیگر دست به تجاوز علیه کشور ما نزنند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70869" target="_blank">📅 16:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70868">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3748363c9b.mp4?token=JwZCX_lS43vUne_E6cGrIhIXsUZesxhLhCA5JL0aOj_Co_DLVmmJJxIuWGgIB3J40STEP0vp74YnCV72cA8d3JF-v4VWn3DiCYSzzowLarFe9Ll2fdUL1C2GnwitwjU3FMSJOEu7xCbiLp7bKIs37CcRjsJxK3eLVoOWoyGUJYSn0DccH1pRxcK2n7DyksZ7UEEqs7piQRJlocx1wj6yaGdOTjr4lDiziXIR0YWg4irk4DBf-qif3Q7hwWssumLRTvLtbvtZJZgsoE8vHakQwukoO193yFY6rfj6kqAUOfDwJHIjRNgg3DVjeA-y0F9U0CIf1nAkE6JeMW1_wRqPIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3748363c9b.mp4?token=JwZCX_lS43vUne_E6cGrIhIXsUZesxhLhCA5JL0aOj_Co_DLVmmJJxIuWGgIB3J40STEP0vp74YnCV72cA8d3JF-v4VWn3DiCYSzzowLarFe9Ll2fdUL1C2GnwitwjU3FMSJOEu7xCbiLp7bKIs37CcRjsJxK3eLVoOWoyGUJYSn0DccH1pRxcK2n7DyksZ7UEEqs7piQRJlocx1wj6yaGdOTjr4lDiziXIR0YWg4irk4DBf-qif3Q7hwWssumLRTvLtbvtZJZgsoE8vHakQwukoO193yFY6rfj6kqAUOfDwJHIjRNgg3DVjeA-y0F9U0CIf1nAkE6JeMW1_wRqPIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسئولین شهر مراغه رفتن سر چاه فاضلاب میگن با یاد رهبر شهید پروژه رو افتتاح میکنیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70868" target="_blank">📅 16:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70867">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUoTZ2ZYFej4Nn5RJfcqkHlI7ZFnR4FC0TRi6UVLJG2Ug0V3WmejJIxoOlbcDXDrGA4vgQwikuFgQEVwLkH8_gfg0qEPppZO1uUOv9n5aW2dYLWGBmClTQnASrYWehcM9hZtMzqmj2BTqIm-chwiNJ3ZDajs63NC4sXovwwFtu1fmJk5MLhrFD5TJ87JUJeg-2WJAj5mpCt10BDJS3EBeLJjQ2cREyK45Dh-p_2I1UfD-0VeYdFhY5BU53CRvsy1h7ytaCEUBTmzLP9kXX3BhqzGMbxAEbKxsMFfFkXVxU-AG2b-S9tv9X1AFyKWOdTiuaFBZuovOCIFpO3Tel_Y0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
عباس عراقچی:
نتانیاهو به زبان عبری آشکارا می‌بالد که چگونه دولت آمریکا را فریب داده و به نفع اسرائیل، آن را به جنگ با ایران کشانده است.
او صراحتاً و با خنده از این می‌گوید که چگونه با اختصاص ۱۰۰۰ ساعت زمان پخش در شبکه‌های آمریکایی، بر آمریکا «تأثیر» گذاشته است.
اما به زبان انگلیسی، از رهبری رئیس‌جمهور آمریکا تمجید می‌کند.
مار خوش‌خط‌ و خال.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70867" target="_blank">📅 15:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70866">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0638c8610c.mp4?token=r9r3gXl0Yfues-TOyCfm0bL18bNLO-E7sI6VZXvGEzKULQyjcinIxS4UGDKcdII7ruw9VXWG2WYDzszpeU7KLWhvq1QgBEkvZtRionnAhiNKsdyqac2e_JFr7R0iBdw1-p-d4apgeE8jEzHT4hHWdWnhYN61fgSN0S7qyN7fmZ-mnxvzAmWedXRU4i8hvswkA3XqfCKtl9YCwJlYUMBRyDlzRT-Q8-bJloezplIIAgtOMMgOuNCS9IrsniTJEO4OKRlQAmFzv6Y1qO3ol4aGK0pHfbpiKuvOlSM2BseiuQftBuKWKwOSxCpzAUBtLoxEgixjAKzP3TTTyUBFS_p5tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0638c8610c.mp4?token=r9r3gXl0Yfues-TOyCfm0bL18bNLO-E7sI6VZXvGEzKULQyjcinIxS4UGDKcdII7ruw9VXWG2WYDzszpeU7KLWhvq1QgBEkvZtRionnAhiNKsdyqac2e_JFr7R0iBdw1-p-d4apgeE8jEzHT4hHWdWnhYN61fgSN0S7qyN7fmZ-mnxvzAmWedXRU4i8hvswkA3XqfCKtl9YCwJlYUMBRyDlzRT-Q8-bJloezplIIAgtOMMgOuNCS9IrsniTJEO4OKRlQAmFzv6Y1qO3ol4aGK0pHfbpiKuvOlSM2BseiuQftBuKWKwOSxCpzAUBtLoxEgixjAKzP3TTTyUBFS_p5tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه وایرال شده از صداوسیما:
یه نفرو آوردن برای مصاحبه؛ بعد خود مجریه فکر‌ میکنه صداش نمیره تو میکرفون؛ به اون میگه اینا رو بگو اونم همونا رو تکرار میکنه
😂
آخرشم میگه دم غیرتت گرم به‌به چه شیرزنی بود
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70866" target="_blank">📅 15:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70864">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b1fde9913.mp4?token=uSQS0XWSmzWU-vypK6ZxPAtUlcvULBokWwUDwEUKc4SaAgbmxziriTDy66PsiVoVUFZQJ9qPmHue69dVe_ruWktvlX_OzNeIP-YZYUUmICuP7MZVFG6vXVVqH9uE71OUt5YFkSqj6Vr2FFKFfXCz_DG15bfOqJUs561e3R-baq4tELTsDdk95QNwJnOnKki6lmgHrnLG1B_CPTbRvxzfPAv7Fl_siIgXKAxuO6SAlHMIJ9FXg4Ik7dGl0Gv10WF14qerH1SF5Q6q2GqPKpIVEiaAt1jgd5_0-v4uvBMJfFA9CbpSjj87WvHmgQ6L7EM0hIZU_fvkpGWEsDna41L03g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b1fde9913.mp4?token=uSQS0XWSmzWU-vypK6ZxPAtUlcvULBokWwUDwEUKc4SaAgbmxziriTDy66PsiVoVUFZQJ9qPmHue69dVe_ruWktvlX_OzNeIP-YZYUUmICuP7MZVFG6vXVVqH9uE71OUt5YFkSqj6Vr2FFKFfXCz_DG15bfOqJUs561e3R-baq4tELTsDdk95QNwJnOnKki6lmgHrnLG1B_CPTbRvxzfPAv7Fl_siIgXKAxuO6SAlHMIJ9FXg4Ik7dGl0Gv10WF14qerH1SF5Q6q2GqPKpIVEiaAt1jgd5_0-v4uvBMJfFA9CbpSjj87WvHmgQ6L7EM0hIZU_fvkpGWEsDna41L03g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حواستون به دوربین مخفی توی ویلاها و اقامتگاه‌های اجاره‌ای باشه!
موارد واقعی از جاسازی دوربین مخفی داخل وسایل معمولی مثل ساعت، شارژر، دتکتور دود و حتی گیرنده‌ها و وسایل کنار تلویزیون گزارش شده.
پس وقتی جایی رو اجاره می‌کنید، مخصوصاً اتاق خواب و فضاهای خصوصی، یه نگاه به وسایلی بندازید که مستقیم به سمتتون قرار گرفتن. سوراخ خیلی ریز یا لنز غیرعادی روی یه وسیله می‌تونه ارزش بررسی داشته باشه.
البته اینکه «جدیداً بعضی ویلا‌دارهای ایران داخل رسیور ماهواره دوربین می‌ذارن» رو نمی‌شه به‌عنوان یک اتفاق فراگیر و تأییدشده گفت؛ امکان و نمونه چنین کاری وجود داره، ولی تعمیمش درست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70864" target="_blank">📅 14:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70863">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0345fee55.mp4?token=BEyPkiI-vGkA0HTEj9Mp_NQ2cjWI2Pwi-32ES9pucXcZXNPqPwd1Ms5Z82eVj6V7p6tAknx0hWRyPorL7zxfJIAfKAv2cTXOgH5_VvFCk21ifmGXYaUsaPl4ZfGOfn8nja0j0xaiCkosobKfilXF4ZcRrhn2kXs2dvcKWyK59A4o2XqdF9DlREyJUeDWXRJKhmjRSxycTlSbL5Q0EsZX32rru9STB1GiZQJB7kBi5zOSaFdN7ju9lZuRceARLIWu1foX1Z6m_1_MTqlOWVQR_WM_XmEjC7po3ktJjPhD5EADqGGxfRw7MvHDAUt-39Gd58r5zvRc7r5uj_EUfMKKZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0345fee55.mp4?token=BEyPkiI-vGkA0HTEj9Mp_NQ2cjWI2Pwi-32ES9pucXcZXNPqPwd1Ms5Z82eVj6V7p6tAknx0hWRyPorL7zxfJIAfKAv2cTXOgH5_VvFCk21ifmGXYaUsaPl4ZfGOfn8nja0j0xaiCkosobKfilXF4ZcRrhn2kXs2dvcKWyK59A4o2XqdF9DlREyJUeDWXRJKhmjRSxycTlSbL5Q0EsZX32rru9STB1GiZQJB7kBi5zOSaFdN7ju9lZuRceARLIWu1foX1Z6m_1_MTqlOWVQR_WM_XmEjC7po3ktJjPhD5EADqGGxfRw7MvHDAUt-39Gd58r5zvRc7r5uj_EUfMKKZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
پست جدید اسرائیل به فارسی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70863" target="_blank">📅 13:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70862">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K14LfXfXcwrMxX3inPHXYSaoRhvtPYyNC2lreEVGXbGM1SouODDp2UB4JFWjkFHo1qXv0eYJLrFq3ICFjlldwKiQzj4BB4BDz7k6XLsI9Z91Du07IcVjOYhKg2s1gcfIjfbQBfZt9U3CGnbmqWXYoRZ89OiZZQrVQNRIl2VPSnp622LjfsE6nuMmpqG8jxYh7AKLEezv_PEDlJ19nR8hZsS55bmRWxky5o3tkZMj4OBQN0908aiyfeJWPC-ZhXEB3swt4PSR3hOTwfUT19N94Ii7Eju_0a91nd7O7-YLm5c9bywB1ZAYyT2RbWTHtKGgw50qnPQUZkOGPoy8JNLd4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت، وزیر خزانه‌داری آمریکا، به خبرگزاری آسوشیتدپرس گفت که دولت ترامپ قصد دارد در راستای کارزار خود برای قطع دسترسی ایران به نظام مالی بین‌المللی، در هفته جاری یک بانک دیگر را تحریم کند.
بسنت اظهار داشت که واشنگتن به کشورهایی که همچنان با ایران مراودات تجاری دارند فشار خواهد آورد تا روابط مالی خود را قطع کنند، وگرنه با اقدامات تلافی‌جویانه آمریکا مواجه خواهند شد؛ او در این باره هشدار داد: «اگر ناچار شویم، این کار به مثابه خشونت مالی خواهد بود.»
انتظار می‌رود بسنت این موضوع را در جریان نشست‌های گروه ۲۰ در «اشویل» — از جمله در گفتگو با مقامات چینی — پیگیری کند. وی تأکید کرد که در خصوص اعمال تحریم علیه پکن به دلیل ادامه تعاملاتش با ایران، «همه گزینه‌ها روی میز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70862" target="_blank">📅 13:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70861">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d9350e95.mp4?token=C5GoXr_SPnr5x5182slF-fmZBKQdog_X6TxbLS69AnsEvnVB1FI4HWqEtHH7gljUWNPqM_6beBcZ8oRohOUYuDTn_wc-q0e6n6nPemhprfKjTLLIFh69WFjMc3GDOLgiaCQqLdkqlNTV5lpKNCt-vQq_wpjYKKq-wUV6ktCoydYs03MezARNz2oGkCPVM-K6sBVER-4RxEJYZ25hhy4eKHWvTKnWdD7xpIR3lvKn9ZR-VDHVmlK4gm6GM80XlNsxLCxHDeF0RjSHLyFb3kal3z2pIxgqX23Fa7YARfMMfWKEOXEddGO3nrkE8mmWoDxSYGFoXRQ0_CiDgMl3mo-CpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d9350e95.mp4?token=C5GoXr_SPnr5x5182slF-fmZBKQdog_X6TxbLS69AnsEvnVB1FI4HWqEtHH7gljUWNPqM_6beBcZ8oRohOUYuDTn_wc-q0e6n6nPemhprfKjTLLIFh69WFjMc3GDOLgiaCQqLdkqlNTV5lpKNCt-vQq_wpjYKKq-wUV6ktCoydYs03MezARNz2oGkCPVM-K6sBVER-4RxEJYZ25hhy4eKHWvTKnWdD7xpIR3lvKn9ZR-VDHVmlK4gm6GM80XlNsxLCxHDeF0RjSHLyFb3kal3z2pIxgqX23Fa7YARfMMfWKEOXEddGO3nrkE8mmWoDxSYGFoXRQ0_CiDgMl3mo-CpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
🇺🇸
ترامپ با هوش مصنوعی جزیره خارک رو نابود کرد.
جزیره خارگ دارد به تلی از خاکستر و آوار تبدیل می‌شود!!!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70861" target="_blank">📅 12:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70859">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ae1b8230.mp4?token=qnvHGszSqmNt9zXH-wWuZtH3y2mSYE5PqRkkfOF-DxDe_9YV6wEDEzzK7WXDDBIM10U1WhEtQMZfqwnAhmoI8c1bPHPZLeZyQf4kPIhRVNumAT1EJExvBjVpkWqiUDvVR37qkY3jEGheo85AQlwaBhQQlqzfVg3cf0oOGMHoBZ1wBgsi58sGG0gvpH7EbJz8hDi1x3_LxzRnn__r30WijwWRPeXfWsIHFhyvU8E7NsHPWF6eiFKrClQrHX2p4U7FDTBphDavzKd16EM1W4I0NMtX6ciZGlERQND6UrCZBdJbwzfqYxiQ3tZ5EzcdSJpeY5sQxkFAmwfnrnY9NYgZwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ae1b8230.mp4?token=qnvHGszSqmNt9zXH-wWuZtH3y2mSYE5PqRkkfOF-DxDe_9YV6wEDEzzK7WXDDBIM10U1WhEtQMZfqwnAhmoI8c1bPHPZLeZyQf4kPIhRVNumAT1EJExvBjVpkWqiUDvVR37qkY3jEGheo85AQlwaBhQQlqzfVg3cf0oOGMHoBZ1wBgsi58sGG0gvpH7EbJz8hDi1x3_LxzRnn__r30WijwWRPeXfWsIHFhyvU8E7NsHPWF6eiFKrClQrHX2p4U7FDTBphDavzKd16EM1W4I0NMtX6ciZGlERQND6UrCZBdJbwzfqYxiQ3tZ5EzcdSJpeY5sQxkFAmwfnrnY9NYgZwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آزاده اخلاقی همسر محسن نامجو:
بی‌ناموس تو که چهارتا ورقه گرفتی دستت گفتی دارم میرم همین سرکوچه تو آمریکا پرینت بگیرم، تو فرودگاه امام چیکار میکنی؟ چرا چمدون من رو اصلا بردی؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70859" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70858">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70858" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70858" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70857">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKrnFogNmbedFjbrtDR73zOHWi3J1F_8jbozpIqJ6oUVEmiuFrZtmGHErDhhcdVDkLLkgE7V7Qk_NlIwq-36wVn4XdmTdBB6pHvnHcr9-eeZzu11a98piLkLLGR0W2XBBQO-r0aGLuEeZkxJ6LjYze-gHMIA5fyqwTbIxoBmwLsx_Yqv9Q61U4aCD0L7cvs2_5MVQUCW1M_fplJRW5YqEFKZKNHciCL4prilbeHuicba5kQGav7qnAzqqnDa7sJ30MBiMRJznnWlWTro-vezOEKJfid10kWc--4Oc7uKnusl7tNH-JgxV6XV02N_MjGOzSP058EaekB3J-xfUcKNeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آرسنال
🆚
استون ویلا
رایو وایکانو
🆚
لیدز یونایتد
رم
🆚
لچه
بولونیا
🆚
آتالانتا
ختافه
🆚
اوساسونا
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70857" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70856">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/862d93bdfa.mp4?token=eK9FThb6cK9QvuyvoIlcgjgtXLj4GNoZS_CPI7V1cuchkGuYpd3Ytt0J36XI6J4JfgNzM0ptm4PQqJycIdqgaT7arreXEVIO3_C54PpZf2okzYHxHZfSJVjQZNSmM7Cl8iUNu0xvD_RwMw8ac9mkBteiUXB7eWN7fz54u24hGh1cv5Z3U05q1O8M4CBvLjgTIEP6Wi8YDnyOnFX9ZKbqQDtQm47a36uLoiMKj41BGd9V7ZMqShUiYWq8W9DlW0CR4O72WrX-vVH2dyCIFabq8Cm-Y3g16_6yUQm_6QafXsDE2CrlKVzG0f_IENLckYLj1hDcpekI47biU39tRAskLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/862d93bdfa.mp4?token=eK9FThb6cK9QvuyvoIlcgjgtXLj4GNoZS_CPI7V1cuchkGuYpd3Ytt0J36XI6J4JfgNzM0ptm4PQqJycIdqgaT7arreXEVIO3_C54PpZf2okzYHxHZfSJVjQZNSmM7Cl8iUNu0xvD_RwMw8ac9mkBteiUXB7eWN7fz54u24hGh1cv5Z3U05q1O8M4CBvLjgTIEP6Wi8YDnyOnFX9ZKbqQDtQm47a36uLoiMKj41BGd9V7ZMqShUiYWq8W9DlW0CR4O72WrX-vVH2dyCIFabq8Cm-Y3g16_6yUQm_6QafXsDE2CrlKVzG0f_IENLckYLj1hDcpekI47biU39tRAskLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبتای ایشون که داره وایرال میشه:
با این شرایطِ گرونی، هیچ دلیلی نداره که شما به دختر مردم غذای مفتی بدی.
اصلا به حرف کساییم که میگن مردایی که پول میگیرن پرنسسن و لَنگن گوش ندین.
خیلی از دخترا بخاطر اینکه حوصلشون سر میره با شما میان بیرون و یه غذا میخورن، پس دنگتونو بگیرین.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70856" target="_blank">📅 11:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70855">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/553aa7e97e.mp4?token=F2mR47k_Yc9rqhasQI-JABVAzpIaGOtxq0Vi4E6_Cm2050TPwp0HoCz34B4sGN6gN564NlcMpX_QKhF0uHiZMaQvY_LBXDjWLfElVnpICAmKjl_worFjiiLAZdUWsM9cRutfzXtBMQr6TcdpXOuMRNT_UCthuK9dxif4qvXMDMPoin6JqvVcYvcRgB1rFsXLk_Dx_nUzc-sF2MlRlkwcJmfSGGj5I6MCu_5JfoQmegqWpDP1X30HO9vV2st2D2WmFj3zARwG1E6MM-YTq0xyBNpRw4yor9AtypRNGCjVaeEpqgY2s25Z3FzP8P92zzIde1WsABuGwsmCzxYDX65KaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/553aa7e97e.mp4?token=F2mR47k_Yc9rqhasQI-JABVAzpIaGOtxq0Vi4E6_Cm2050TPwp0HoCz34B4sGN6gN564NlcMpX_QKhF0uHiZMaQvY_LBXDjWLfElVnpICAmKjl_worFjiiLAZdUWsM9cRutfzXtBMQr6TcdpXOuMRNT_UCthuK9dxif4qvXMDMPoin6JqvVcYvcRgB1rFsXLk_Dx_nUzc-sF2MlRlkwcJmfSGGj5I6MCu_5JfoQmegqWpDP1X30HO9vV2st2D2WmFj3zARwG1E6MM-YTq0xyBNpRw4yor9AtypRNGCjVaeEpqgY2s25Z3FzP8P92zzIde1WsABuGwsmCzxYDX65KaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وایرال شده از طرفدار حکومت با پوششی جالب که میگه:
آقا فکر کنید شعب ابی طالب هستیم و محاصره مون کردن
این محاصره از شعب ابی طالب سخت تر نیست که
ما مذاکره نداریم و آمریکا هیچ غلطی نمیتونه بکنه
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70855" target="_blank">📅 11:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70854">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10096c1b11.mp4?token=VkwbrQCtFXstR2Hi4WXoH890oNL-qQ1EW6AQj58-Ptxt341FriwNMsII0bTkjjtsP6FdtYI46KG9VcFveYznkFGM77Jc_ADTWhy4Hj0kLLPDYHZrXAT0Jk2dYS5Lvy_fo0wfsAI5W4T43HRnMj_6z6b77Tfsa1oQNwdORu66KK7MqP_j5R61cs3OyWpxULI09q3MNFmt5M-qVG7hOVsNZKJaB60Xlh4j8FcLVO4VadCi43FZGr8dcROabNrN9eg8LAWp7qCZN282qUQyL1nlXKBTfkvrOJVN5vliscXVo5AzgcB2iaaksB8If5tEb8DFOhBAZSD1Vn1iV15kUTjEoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10096c1b11.mp4?token=VkwbrQCtFXstR2Hi4WXoH890oNL-qQ1EW6AQj58-Ptxt341FriwNMsII0bTkjjtsP6FdtYI46KG9VcFveYznkFGM77Jc_ADTWhy4Hj0kLLPDYHZrXAT0Jk2dYS5Lvy_fo0wfsAI5W4T43HRnMj_6z6b77Tfsa1oQNwdORu66KK7MqP_j5R61cs3OyWpxULI09q3MNFmt5M-qVG7hOVsNZKJaB60Xlh4j8FcLVO4VadCi43FZGr8dcROabNrN9eg8LAWp7qCZN282qUQyL1nlXKBTfkvrOJVN5vliscXVo5AzgcB2iaaksB8If5tEb8DFOhBAZSD1Vn1iV15kUTjEoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
رهبرانشان از میان رفته‌اند.
تمام... خب، تمام تجهیزات ضدهوایی‌شان، منظورم این است که همگی نابود شده‌اند.
آن‌ها آدم‌های سرسختی هستند؛ آدم‌های باهوشی هستند. اما... خب، بسیار شرورند.
تا سه ماه پیش، پنجاه و دو هزار معترض را کشتند و متأسفانه، شمار بسیار زیادی را هم به آن فهرست افزوده‌اند. حتی سراغ کسانی که معترض هم نیستند می‌روند؛ به خانه‌هایشان هجوم می‌برند، آن‌ها را با خود می‌برند و به ضرب گلوله می‌کشند.
خب، این‌ها آدم‌هایی بسیار خشن و شرور هستند و اگر سلاح هسته‌ای در اختیار داشتند، اسرائیل نابود می‌شد.
اگر من رئیس‌جمهور نبودم، اسرائیل از بین رفته بود. دیگر اسرائیلی وجود نداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70854" target="_blank">📅 10:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70853">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEdltD7nRHTHDpPP0MNloi6f6o_IqxAS2UwH_9MOVsP_VdKKKHD5LudAMM1XjrIk8x0_w4zBnZFy7rwAHtNLz0smzIUxGxchJKUSMdTU9jdCd_Nshn3e57Yt5k5knaglzjo1FGhDYuAey79R7EaRs8m6RTuulAar7qh22u5TRx48Q69S9jIefY7u_2WpJlUsTOAWOj-uyVMKsQbXP3Hiy63kf6DFvDNFV7L9KMHZiVtyfxxpmAIfaAwgh1VyQUKHYY-qfXyTFHjR4WizxqHrVjZEtG9grM7i6GKcgeiI1bGxbKzyomndW4ff8nQ11xmaL-yEymGOr-1Yv5YXkGXgZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
〰️
سنتکام:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران در بیانیه‌ای اخیر مدعی شد که حملات نیروهای آمریکایی برای جلوگیری از مین‌گذاری سپاه در تنگه هرمز، «اقدامی تجاوزکارانه» بوده است. این ادعا کاملاً نادرست است.
✔️
واقعیت: نیروهای آمریکایی علیه یگان‌های مین‌گذار سپاه که در تنگه هرمز تهدیدی قریب‌الوقوع ایجاد کرده بودند، دست به اقدامی محدود و دقیق زدند. در واقع، ایران عامل ایجاد این تهدید بود و ارتش ایالات متحده برای حفاظت از دریانوردان غیرنظامی، کشتی‌های تجاری و جریان آزاد تجارت جهانی، آن تهدید را خنثی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70853" target="_blank">📅 10:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70852">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef58f7de4.mp4?token=kDsoxvj3876ljhE_QaFA_Y3c2ek1mZKazR8AsB_Phsx1TEICMXOLOzbJucU9oxYL-9VWSiE0pGf4WRUIqWHHIIKnCLhCBc4z7D_08oFPkbraqeqIrNFuLA-WuIZ6JRIJlCVIn0Evj-MHpKk613gr4M7UwHjCfQHsk8JZCg-PVqxAeS1eHOwUokzFUOvLa2XDR-o393oCGZJpeZvRKT4AtdzUqayyccO35-ABgDJj52SfWHQnFHN7Pj9OY8kYc3b4NKGGtZZS37AL1ghGTCh00pCxkko7t0KxSBlKg4C_qP9vgvmrEARaW9Uq3w7v-k5mJ5DiRvTuy8rvMHtzcyKKAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef58f7de4.mp4?token=kDsoxvj3876ljhE_QaFA_Y3c2ek1mZKazR8AsB_Phsx1TEICMXOLOzbJucU9oxYL-9VWSiE0pGf4WRUIqWHHIIKnCLhCBc4z7D_08oFPkbraqeqIrNFuLA-WuIZ6JRIJlCVIn0Evj-MHpKk613gr4M7UwHjCfQHsk8JZCg-PVqxAeS1eHOwUokzFUOvLa2XDR-o393oCGZJpeZvRKT4AtdzUqayyccO35-ABgDJj52SfWHQnFHN7Pj9OY8kYc3b4NKGGtZZS37AL1ghGTCh00pCxkko7t0KxSBlKg4C_qP9vgvmrEARaW9Uq3w7v-k5mJ5DiRvTuy8rvMHtzcyKKAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سرهنگ خلبان بهمن فرقانی، جانشین فرمانده پایگاه چهارم شکاری دزفول :
زمان جنگ، آخوند رسول منتجب‌نیا به پایگاه ما آمد و پیشنهاد داد برای بستن تنگه هرمز، فاصله عمان تا ساحل ایران را با قایق‌های موتوری با طناب به هم دیگه ببندیم تا عرض تنگه بسته بشه
به ریشش خندیدم و گفتم: «چرا مزخرف می‌گویی؟»
زیرآبم را زد و از نیروی هوایی اخراجم کرد!"
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70852" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70851">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8771a258e.mp4?token=FvzxafToLuLMiK5TBDzy8NGFbqmcfhNWVugQInSc80uZKc1PQ_8ZDSWDTY-LJ1U1gbo3nNVLFa-otOjtk5T7uEbzDzOezQB9S7LUvCYxiRRkjRaXENRcc09LYwSz2dnVhb2ceDxzchmFPFAsTwr7XF_fe0IiJ0YgyMlbv1-24nx_-3cc14_jJtQ_mYB2PRJSjHg5IZj5Ny7lc945MkJsAcCeAgXXV_H2SPZtjFwZsnSUM3eKWkrSVjgRWS_OdH-XJPhDBG1YlL8I3-qJLKeTWb6m3DEjAnFL3BKAW_aaZbMBaVdT9Dy5YdESVFi69MP-lCOBHZzQqEjYZoSEEvzzu1g5uqhaXLpj4QkWp3pjsMgwylrxpU96RH3oU1F9M-83IA6It1RG_VHQhkxILPl0sL-U2b7cU75iguekuF8_8mu-uGKxZdrRflRxi1wA3g1TUr0XkrFdC36hE9CjO1hgPLfO4N1-I_wQT6XnYf_O2HeIXt4oH0PnJLQDnl9yH0f1ZY3AlWQQNJPwbnHhBQYInMedzKoi8vkm0jZuZDDW5PG6iXgUmtdcdk0aDFIK03KwDMEnMXTKO28Tw0tVBEkKcYi6xkHo3YDbZT4Qm3nhk6v3CVgPCCGok6RpGMJVcApzcFp1ZEIeIiH8eg1BloO3AQCfn0QgXW3vPpBJYTS8KwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8771a258e.mp4?token=FvzxafToLuLMiK5TBDzy8NGFbqmcfhNWVugQInSc80uZKc1PQ_8ZDSWDTY-LJ1U1gbo3nNVLFa-otOjtk5T7uEbzDzOezQB9S7LUvCYxiRRkjRaXENRcc09LYwSz2dnVhb2ceDxzchmFPFAsTwr7XF_fe0IiJ0YgyMlbv1-24nx_-3cc14_jJtQ_mYB2PRJSjHg5IZj5Ny7lc945MkJsAcCeAgXXV_H2SPZtjFwZsnSUM3eKWkrSVjgRWS_OdH-XJPhDBG1YlL8I3-qJLKeTWb6m3DEjAnFL3BKAW_aaZbMBaVdT9Dy5YdESVFi69MP-lCOBHZzQqEjYZoSEEvzzu1g5uqhaXLpj4QkWp3pjsMgwylrxpU96RH3oU1F9M-83IA6It1RG_VHQhkxILPl0sL-U2b7cU75iguekuF8_8mu-uGKxZdrRflRxi1wA3g1TUr0XkrFdC36hE9CjO1hgPLfO4N1-I_wQT6XnYf_O2HeIXt4oH0PnJLQDnl9yH0f1ZY3AlWQQNJPwbnHhBQYInMedzKoi8vkm0jZuZDDW5PG6iXgUmtdcdk0aDFIK03KwDMEnMXTKO28Tw0tVBEkKcYi6xkHo3YDbZT4Qm3nhk6v3CVgPCCGok6RpGMJVcApzcFp1ZEIeIiH8eg1BloO3AQCfn0QgXW3vPpBJYTS8KwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یک سرهنگ فراجا:
متأسفانه مدتی عده‌ای از مراجعه کنندگان و یا به تعبیری ارباب رجوع به ما مراجعه می‌کنند و در خصوص گرانی‌ها معترض‌اند و هر بار که به ما مراجعه فکر می‌کنند، فکر می‌کنند که مسبب و اینکه ما از دست ما کاری بر می‌آید و نمی‌توانیم برایشان انجام بدهیم.
آقایون مسئول، عزیزان مسئول، به خدا گرانی بیداد می‌کند. آقای برادر تعزیرات، آقای بازرسی کننده، آقای بازرس اتحادیه، به خدا با کت و شلوار اتو شده و موهای ژل زده و عینک دودی نمی‌توان با فساد مبارزه کرد.
آقا یه جای کارو درست کنید که یه جای دیگر را بخواهید گوش‌نظر بدید. تو رو به خدا، تو رو به هر کسی که می‌پرستید وضعیت معیشت مردم را درست کنید.
فکر می‌کنند به عنوان پلیس ما از جای دیگه درآمد داریم، از جای دیگه خرید می‌کنیم. به خدا این چنین نیست. ما هم مثل همه شماها از همین فروشگاه‌ها خرید می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70851" target="_blank">📅 09:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70850">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78504efb49.mp4?token=ZHIf6Dq0YzIjdJenc0hXX1gbJekhSXI1I0IW6HeGrHaVE5aFCzFj5iCR_iRWys2JtZZcDtHySGDVvDkWp51pq00vfxp0Yk4DfMaZUE5D6e64wMR_Mh2v10MTovYMPKuZeoFwgozx7EfegUUuhuVNhIslso_cBWwgdZYRw0UQ6EGykFq5WIF0-YdsMZ5gJqmVIiDIxW-QbqRkosfZowvxGzgGFY6CoyzvJwfvRNVxtdldoIHFH5vYkeMFTJhYqUHuhHiVa3jtuCcqN2iJECvHe-9sbZYo6znFXL-Ap76MprlJWkyq5ARmJZ6n7aAn9Ki5BbWFf8EBOx-5gZGfvaJ_hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78504efb49.mp4?token=ZHIf6Dq0YzIjdJenc0hXX1gbJekhSXI1I0IW6HeGrHaVE5aFCzFj5iCR_iRWys2JtZZcDtHySGDVvDkWp51pq00vfxp0Yk4DfMaZUE5D6e64wMR_Mh2v10MTovYMPKuZeoFwgozx7EfegUUuhuVNhIslso_cBWwgdZYRw0UQ6EGykFq5WIF0-YdsMZ5gJqmVIiDIxW-QbqRkosfZowvxGzgGFY6CoyzvJwfvRNVxtdldoIHFH5vYkeMFTJhYqUHuhHiVa3jtuCcqN2iJECvHe-9sbZYo6znFXL-Ap76MprlJWkyq5ARmJZ6n7aAn9Ki5BbWFf8EBOx-5gZGfvaJ_hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل به فارسی:
جمهوری اسلامی و سپاه پاسداران سال‌هاست که ثروت و منابع ملی ایران را صرف تروریسم و جنگ‌افروزی می‌کنند، در حالی که سهم مردم از این ثروت، ایستادن در صف‌های طولانی و بحران کمبود بنزین است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70850" target="_blank">📅 09:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70849">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70849" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/70849" target="_blank">📅 02:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70848">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pci6o0eTGFCz_NwAzRETbdzC0R2_qwnGi-OYSwwjMSwWoPtkheVW8M2hDnWHsVSNpAWqD4i3qyfwgWjyRPTXS4_OsskmzVC-So_a3hG8GxP8qyKS0EEOzDj2_JF3XEUxkSCYfI-rkXW2x3JXGF3QqcUA_jC5zMYqxsBbPtz9TRs5RP0I5zfPl_EXoSoQT4jvxP6oBZTXf4W3DyzbVKrnDjmaEwokqUFrR8w-3QJkctPUvOjqB0yVbgMx_CRzAZ9jFzollC6odMBW4-Mi58FT_eho5CsSMugwFJf1Lgw9Z5yFP2nHnFQy-RkpgdgpxbCI0MZwYdk2n5qrldGL947r8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/70848" target="_blank">📅 02:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70847">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
نایا:حملات موشکی به قطر.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/70847" target="_blank">📅 01:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70846">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-text">یادآوری: علی خامنه‌ای، دیکتاتور و بزرگترین جلادِ وقتِ خاورمیانه در ساعت ۹:۳۰ دقیقه صبحِ ۹ اسفند ۱۴۰۴ توسط ارتش اسرائیل و آمریکا، تکه تکه و تجزیه شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/70846" target="_blank">📅 01:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70845">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بچه ها بزارید منم این وسط یچیزیو یادآوری کنم
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/70845" target="_blank">📅 01:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70844">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMr. NOBODY</strong></div>
<div class="tg-text">خواست پاتریوت رو با لهجله بیریتیش بگه اذیتش نکنین</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/70844" target="_blank">📅 01:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70843">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromɴᴀᴢɪ</strong></div>
<div class="tg-text">امیر پهن مغز پتریوت چیه؟</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/70843" target="_blank">📅 01:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70842">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQubp_xF1bLWEzvCUISfZqpFbbFII55dP1jz8XarrsitxqxcsSSgrKZyQRnfOrCKm4wnOV5_Nw5Y3Vq3aeN8UtFfwDAOudnmsGuq4MgYKgki0CAhHANitPMJx77ARQKqaJRfvd1UmAZgFsIpOUYfwiBVKejr_M6GozjviI08CqQPANMYqRHqPkoqnP4Xm9RL7WGkudZ7yANT-admEPHfTEa36xIExQty6vZA3ILvDUs4zDj2eymLFYRQMNdsZr3oMbNaeUKYk0w91O1KtlJfmns9FttHOhtC8NlKgX9mRpmHIqXqtkZiTELimh1u3KvEmoKaBzjQvdh1HNuYETgR8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا حالا برخورد موشکی صورت نگرفته، اکثرا رهگیری شدن #hjAly‌</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/70842" target="_blank">📅 01:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70841">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f04fa470bb.mp4?token=ZIQ_aR1qj6S97AaqQ3b8K5bJJ691U9LAkN4j_FqIQI-zbDOq1MoEb2DtW5DeD82z48gMRZIHEya82IXWatcrOrqCoUUYJ6ayYAwPUfnmGizn42gTp_C9rFGGB-bmzpubXexo9tuwiXwiONLUxU49niyLPevA90JB4W66o633DG7mbwuYcgUeX_NOuR2c1RZ8l33qiEeu1CwOT6kkeIoZbpz6F6hrzhPILjkQ9jnHtxxVaPD-e-nZ3QOgGX9wk94MDVlVEbjBLfAOanv2zR0MzffAjaLDW3EDykCF1u0Fb-4WDpAO1b6ZMc4Z3mG6Ln3d82kejI1jL9jD5f9UBdg-WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f04fa470bb.mp4?token=ZIQ_aR1qj6S97AaqQ3b8K5bJJ691U9LAkN4j_FqIQI-zbDOq1MoEb2DtW5DeD82z48gMRZIHEya82IXWatcrOrqCoUUYJ6ayYAwPUfnmGizn42gTp_C9rFGGB-bmzpubXexo9tuwiXwiONLUxU49niyLPevA90JB4W66o633DG7mbwuYcgUeX_NOuR2c1RZ8l33qiEeu1CwOT6kkeIoZbpz6F6hrzhPILjkQ9jnHtxxVaPD-e-nZ3QOgGX9wk94MDVlVEbjBLfAOanv2zR0MzffAjaLDW3EDykCF1u0Fb-4WDpAO1b6ZMc4Z3mG6Ln3d82kejI1jL9jD5f9UBdg-WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رهگیری دو موشک سپاه پاسداران بر فراز اردن
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/70841" target="_blank">📅 01:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70840">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
فعالیت پدافند در اردن  @News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/70840" target="_blank">📅 01:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70839">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:  از خرم‌آباد صدای انفجار شنیده شد.  @News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/70839" target="_blank">📅 01:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70838">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:
از خرم‌آباد صدای انفجار شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/70838" target="_blank">📅 01:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70837">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">صدای انفجار شدید تو خرم‌آباد شنیده شده
#hjAly‌</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/70837" target="_blank">📅 01:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70836">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44471a1938.mp4?token=Zy6DZNUDVJW_e6vzOpV1_GuCSAnqkdVKDPBn0-JeVHuIn-vauCidaEac3zFJcmE-IvyLAOqHsAPmK_lgrHVH6krgwXH6eQkSVbqjlHb6FwRt8j7Hj8EKjpQacpdBpXGsbl80kcW_y9mI6H2SDLrONnmPKL3FM1nuG6xvfDPyOkrhiYj5m6V5450ioZD6v0JlehaKScvLuFu9GppyAEDnJ_-tN32oBOe0znXN4-rJk_VOx9IzaAo-BMNKAZhW1Auw4UnKICxZ7_vrg7c3BgMkmfiP56qyWILfz9EuSdDrwrv2F7Xqlic_GJSCcjg2-KJNW66XGD1Pwhxt4G3TJnoA_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44471a1938.mp4?token=Zy6DZNUDVJW_e6vzOpV1_GuCSAnqkdVKDPBn0-JeVHuIn-vauCidaEac3zFJcmE-IvyLAOqHsAPmK_lgrHVH6krgwXH6eQkSVbqjlHb6FwRt8j7Hj8EKjpQacpdBpXGsbl80kcW_y9mI6H2SDLrONnmPKL3FM1nuG6xvfDPyOkrhiYj5m6V5450ioZD6v0JlehaKScvLuFu9GppyAEDnJ_-tN32oBOe0znXN4-rJk_VOx9IzaAo-BMNKAZhW1Auw4UnKICxZ7_vrg7c3BgMkmfiP56qyWILfz9EuSdDrwrv2F7Xqlic_GJSCcjg2-KJNW66XGD1Pwhxt4G3TJnoA_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعالیت پدافند در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/70836" target="_blank">📅 01:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70835">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خبر متوقف شدن پروازای فرودگاه مهرآباد هم فیکه #hjAly‌</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/70835" target="_blank">📅 01:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70834">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
منابع عربی:شنیده شدن صدای انفجار در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/70834" target="_blank">📅 01:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70833">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🔴
گزارش ها از شلیک موشک از نقاط مختلف کشور به سمت اهداف آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/70833" target="_blank">📅 01:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70832">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">همه‌ی خبرایی که رسانه‌ها بخاطر ویو گرفتن به ترامپ نسبت می‌دن فیکه، هیچی نگفته درمورد حملات امشب  تلگرام یه‌پا شده روبیکا... #hjAly‌</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/70832" target="_blank">📅 01:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70831">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbAeYUyDK4M_FCgQi1FGbwn4dX-6eVCyFDrMuJqTwfxoHa44dPB7_3LvAJYaRf9kT2Sqyyx0nfqS_bEtohVtyG8nAp19Ps-AxGezjJzXSIl--Jo02WEbJfca0dxwn-7idwphoXDX4zbUsMPCweWni1bjtrNi4BQVaW3Lo67Nnfe2ZAmfjEaHi6FKjolxz0OM2VfK5_FHqtTajNHpp5wAyXfHS7rDcRplGeTI4h20_G_RK2hwi7kolYDoPHpzd72bHHIfC5KrKnLal8ot246tkN1sGZY7ZA-WhQvExDsKDUq7Yo7w3uSVN7vcOpBGEvDWkrdduAo8CjJhrTPHQTNIzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/70831" target="_blank">📅 01:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70830">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e895af3e4.mp4?token=qRNzT9qoJbq6zVjpYQejjZSRgXzSbVKx7rNu-gRqEyTGe4piTR4pt3-NK_udgmgKDO1zm3UMS7cG_knBfTAKq9xCLZbepTn9Ms2uBCWY6jMLWZNaopWvGKfMfq9J3qaq-3-mTKVy-RdpbzfZvDSto9QGyFg4k_ztDh1SBGPLGOdv8z0sJ7UjMUu3iDqrV4lOVdhK89WPYsLyOaS5RJhPHWmqDPsOXSpsj-2nFSDI0H_86EKKd2oLWmtH68B8OY8hVyLUMX2I_VYwXrIaM7AmjVNroeTF3NBmHZ0BQ0TKneAThAgTLQScx2-H1-iqpkuWm6ORDU65w99dIVyRgQIbOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e895af3e4.mp4?token=qRNzT9qoJbq6zVjpYQejjZSRgXzSbVKx7rNu-gRqEyTGe4piTR4pt3-NK_udgmgKDO1zm3UMS7cG_knBfTAKq9xCLZbepTn9Ms2uBCWY6jMLWZNaopWvGKfMfq9J3qaq-3-mTKVy-RdpbzfZvDSto9QGyFg4k_ztDh1SBGPLGOdv8z0sJ7UjMUu3iDqrV4lOVdhK89WPYsLyOaS5RJhPHWmqDPsOXSpsj-2nFSDI0H_86EKKd2oLWmtH68B8OY8hVyLUMX2I_VYwXrIaM7AmjVNroeTF3NBmHZ0BQ0TKneAThAgTLQScx2-H1-iqpkuWm6ORDU65w99dIVyRgQIbOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش ها از شلیک موشک از سایت موشکی بیدگنه
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/70830" target="_blank">📅 00:58 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70829">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">همه‌ی خبرایی که رسانه‌ها بخاطر ویو گرفتن به ترامپ نسبت می‌دن فیکه، هیچی نگفته درمورد حملات امشب
تلگرام یه‌پا شده روبیکا...
#hjAly‌</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/70829" target="_blank">📅 00:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70828">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoHGW6QZyFWykqcYdekIh-G2AK3XRgZjvbnfx0X7DmPNPj95MCAUOfVVRcTplxO2HHvFIX254NUysE2vVCHFbkgEqVuPUn3xCH8dUZtddSSd-5QY-GVthllqsn1s4meBu_u56jb1s2cu-kbN5q0D7gOycmEU-_eO92xf36Cu47tX57nBy6p9BR6km7OeeB_MZbT5FbZ39iCw1jUXFkx8uPtUi2TqqBNzd1dYN26oTI56mXfvcRvE0YHj7VUBQDtrqaTw2jE_QXimbZ9xITRVYAZVw6FvGVhJZWZ14n4D7lYoxXWmjhhtpcc3w7mdLV3askT8QTksiPc68VboVBh_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
ابراهیم عزیزی:
یک بار دیگر اراده ما را بیازمایید و بهایی سنگین‌تر بپردازید.
انتقام در راه است؛
فقط فرار کنید!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/70828" target="_blank">📅 00:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70827">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06c56b11a.mp4?token=JsCyJQpH0KPkhzor1qTFXbJEDWerGJISMAc2_T4_qWlu7F7dminY3RIKbIS_vhLzievnG2u6LsfdqbymX1nvGb1PnACS4O_77kJ87nAB63zLkz2_EGzQRhKEs5vCoBeq84h3TNdUQpqxMsxebSndr9CDyEAluk0DUJ09mSJWptumlhMMA5dPMbQD9-XrmrKiOlZYr7-LUAPI7MP7-ORTelWg0DCNueJODO_FULh0Y5qnHwyZxIBRhPWKOzn_fARexVHRcxnQIwOui_VrzZkeingxfoV8ugn89h9P9-kWsHVRoG7dI1zH6ObHDptZYgThFt4x92q9wlIIMJajKchOJ5EGhtDkyFFJp20J7Tm0DiyeR1D9-qQbMJLVwlFk-S6dir0ka_LXCxsddyLb4aDHhJ8FBPtDPd1-K9gcjhxkhNaVyRS_CJ_yl4UO31WqAzk1R0QPGph4Vv7Y2VttcYFrSMoi4527HTGu_vu-s0LRuXA7qYHkrBE2RKe4MXa3GckEMEz7KaJXjioLFQIKxI50xelIlSIrl5EH8B515BXXFhU5BADJfxJ4anC4Im0Srt_u-0pxbfeBjpxMSdlbZ8LOdFG_0rz0ttEjr9AvOGOUBSn-mqtK22wPe7KWFT0ESeAbz_7oPsQoYisDz86Z538iA-bnDSGg6mcPXd5p74J2eJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06c56b11a.mp4?token=JsCyJQpH0KPkhzor1qTFXbJEDWerGJISMAc2_T4_qWlu7F7dminY3RIKbIS_vhLzievnG2u6LsfdqbymX1nvGb1PnACS4O_77kJ87nAB63zLkz2_EGzQRhKEs5vCoBeq84h3TNdUQpqxMsxebSndr9CDyEAluk0DUJ09mSJWptumlhMMA5dPMbQD9-XrmrKiOlZYr7-LUAPI7MP7-ORTelWg0DCNueJODO_FULh0Y5qnHwyZxIBRhPWKOzn_fARexVHRcxnQIwOui_VrzZkeingxfoV8ugn89h9P9-kWsHVRoG7dI1zH6ObHDptZYgThFt4x92q9wlIIMJajKchOJ5EGhtDkyFFJp20J7Tm0DiyeR1D9-qQbMJLVwlFk-S6dir0ka_LXCxsddyLb4aDHhJ8FBPtDPd1-K9gcjhxkhNaVyRS_CJ_yl4UO31WqAzk1R0QPGph4Vv7Y2VttcYFrSMoi4527HTGu_vu-s0LRuXA7qYHkrBE2RKe4MXa3GckEMEz7KaJXjioLFQIKxI50xelIlSIrl5EH8B515BXXFhU5BADJfxJ4anC4Im0Srt_u-0pxbfeBjpxMSdlbZ8LOdFG_0rz0ttEjr9AvOGOUBSn-mqtK22wPe7KWFT0ESeAbz_7oPsQoYisDz86Z538iA-bnDSGg6mcPXd5p74J2eJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
#فوری
؛نتانیاهو درباره ایران:
من این رژیم را به زانو درخواهم آورد. به این امر متعهد هستم. این کار شدنی است.
آن‌ها بسیار ضعیف‌تر از گذشته شده‌اند و در موقعیتی متزلزل قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/70827" target="_blank">📅 00:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70826">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو درباره ایران:
آن‌ها از برنامه هسته‌ای دست نکشیده‌اند. ما آن را به عقب راندیم، اما آن‌ها کاملاً قصد دارند برنامه هسته‌ای خود را برای تولید بمب‌های اتمی از سر بگیرند.
بنابراین، این تهدید از بین نرفته است. ما این سرطان، این غده سرطانی را ریشه‌کن کردیم. می‌دانید که اگر سرطان را ریشه‌کن نکنید، می‌میرید. این همان کاری بود که ما انجام دادیم.
اما سرطان ممکن است دچار متاستاز (گسترش) شود و در صورت بروز متاستاز، می‌تواند دوباره به تهدیدی تازه و بسیار جدی تبدیل گردد.
ایران می‌خواهد برنامه هسته‌ای خود را از سر بگیرد.
من پیش‌تر یک بار مانع این کار آن‌ها شدم و تا زمانی که نخست‌وزیر باشم، مانع انجام آن خواهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/70826" target="_blank">📅 00:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70825">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAqbvgqjDBFcUhv6_LLEogaT_GMIVhfpHk9aHlH0F0WVsXfxOHnQ-AyUymuLz4oChrBfHP2lPfpW1wQggAAbKqcktwE-uEnfR6nLC_fPKeVxjFQKY6DxixGSCutGdsjfv0Pq5KQIs53kxT2nZnG807JEk9SWYdx7YsKoaFMjA9tsHZPX1VLIo5fzYnykDkwGpurWeDnRLlDGnm_Tj-j-XglRHnnyrwyYvlVZp_Et8pM__o4hoKvTpw6KbjHZ293HEG50olicq_ZRmYI8snqOXOngoh_Ls98bwFa6r1q229Wd6HPotE5Zyakt2pNn30kkAU5MK7wu594mRxo5NNbJPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
سخنگوی سپاه پاسداران انقلاب اسلامی:
این اقدام، یک خطای راهبردی و مهلک از سوی دولت ترامپ در چارچوب جنگ اقتصادی است؛ اشتباهی که کفه ترازو را به زیان طراحان آن تغییر خواهد داد و هزینه‌های سنگینی در پی خواهد داشت.
دشمن پیامدهای این محاسبات نادرست را در هر دو عرصه اقتصادی و نظامی متحمل خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/70825" target="_blank">📅 00:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70824">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
مجدد صدای انفجار در جزیره لارک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/70824" target="_blank">📅 00:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70823">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوری؛سپاه پاسداران:   تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد  @News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/70823" target="_blank">📅 23:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70822">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوری
؛سپاه پاسداران:
تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/70822" target="_blank">📅 23:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70820">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-MSRwVLE85uICbKHDzT4F-JLKZTnHkzSpd3tumb3kvsISg9acBLxusvf6KK8o9IGK0cmwqY7A3OJ5T5pkG2P89pibJfH_q-3KMD6YhnpgDkvWi9SxtT3lS8bg40oLTxVEoDnTK6Dtq1Rihtcfy-Grlef_CT-AdN8Gh_B79fppVnzlFF1tYmXnVNjE0QXCBwAyBRlwFmlRL9XblsV_HqAOUaWQoEwkwQwTzzlW8oBeG-Je9RXhrfxSZzkVXH2s7oMrXteTwjH24dR6S5DM3ufVai5oUS-tP6pgL6CvTGpxKXRF7FBddXauGKccOBHzP95BNxR4Oa-kKjBlJLOM1vQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d778b593.mp4?token=Z9yeYeRCaF4dC3J4mWbIVqcOQjdtmQVYPPQ84D_f2C3jyJQcELbw-owp0SELKxHbPOEQDby7AC8wUlBB0ncFDJhzDof9zSzvGqBIAEEBvGkiTvVAorKiInsm2gUg5nwUVqQct2h8YQjdodetR1l3Wm6Z9ZZ--2wITWoS4WX3AFjjc2RY1mmqw2rTOeoHLQ2oFZ0YLSgNk-GGTcoOWGhI60vKq6-_z2h1DTIpfPeo0Yg1QCZ-wOYatmnWv71X6RXn_Rge_kSJ6HbEN58ycwwuB0bdXNt_KImzZSyEdO-1CeJms3lv5ootsng3zXHUzbpd9K4FOmGfzYZ_lzsCX2Bi8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d778b593.mp4?token=Z9yeYeRCaF4dC3J4mWbIVqcOQjdtmQVYPPQ84D_f2C3jyJQcELbw-owp0SELKxHbPOEQDby7AC8wUlBB0ncFDJhzDof9zSzvGqBIAEEBvGkiTvVAorKiInsm2gUg5nwUVqQct2h8YQjdodetR1l3Wm6Z9ZZ--2wITWoS4WX3AFjjc2RY1mmqw2rTOeoHLQ2oFZ0YLSgNk-GGTcoOWGhI60vKq6-_z2h1DTIpfPeo0Yg1QCZ-wOYatmnWv71X6RXn_Rge_kSJ6HbEN58ycwwuB0bdXNt_KImzZSyEdO-1CeJms3lv5ootsng3zXHUzbpd9K4FOmGfzYZ_lzsCX2Bi8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
یه نمایشگاه عراقی اومده پژو پارس گذاشته برای فروش؛
و اما کامنت مردم همیشه در صحنه :))
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/70820" target="_blank">📅 23:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70819">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
#فووری؛ باراک راوید به نقل از مقام امریکایی: امریکا امروز به دو پرتابگر ایرانی در جزیره لارک حمله کرد  نیروهای سپاه پاسداران سعی داشتن موشک‌های حامل مین دریایی به تنگه هرمز شلیک کنند که قبل از پرتاب توسط امریکا منهدم شدن @News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/70819" target="_blank">📅 23:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70818">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ua5l-_2eSrjwViHXQweW2_DxNk8R1KttgQQ22iBUZbbPxAvrZjHdDYDb5qFcgAxFVjXlWekJGTbHRWAbdy7W7Cuy5_mkY12lSWImPkFtmfI7Dk4pupiafa5AJlmpt_iiXFu_AfWQLGTLmvaLMZ9DfEW9YkmN-yjGp3YK5PAzzy36YVXNiPBbFw4wOdMJgdZYM35EdGNsbj01pU2UZimx7EMi9P8jJgafV4CqDvaXeiTX9FrnEG2s8G3WiOB794ifhv8jpvlXe2LINxGnxKbMDTP7yoAr0O9witR8TAwm0IZaxo3T2ID74Tvrit59QoFash9GXR3J54iuA2SJIu9-_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووری
؛ باراک راوید به نقل از مقام امریکایی: امریکا امروز به دو پرتابگر ایرانی در جزیره لارک حمله کرد
نیروهای سپاه پاسداران سعی داشتن موشک‌های حامل مین دریایی به تنگه هرمز شلیک کنند که قبل از پرتاب توسط امریکا منهدم شدن
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/70818" target="_blank">📅 23:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70817">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6826005e4.mp4?token=UVQtF9S_zyjbOubo4D0XOvkNDZ4cGroNxHhgeCgwhlIKUFHq1LXXTULYm3Va_rLoD1PcAoXU7q9KFkLzsfAiufnQ16Xh__j6cvaqmsGTZvNFIgXIsf6a85W8A1yVLQw938LP3LfeFp7YDyLOPYbp1Nq-AsiuiV9VOQsYTESGMDmr-PGzfvPooMVPpzJFO5R8Wnl2cRLKBrkz6WXtl9qBgiQv-7qECuVJ61CCakATk5vtDO7XJIVNop2dCTNMIryWrUkeiiEoc7N5Vz3elVBOrOIhGgDC1JFvE4IbNWbiMkoZIJLMCoaZoZvrO2-puF2rx7ZTxQKHRyZ7USpLt8U8tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6826005e4.mp4?token=UVQtF9S_zyjbOubo4D0XOvkNDZ4cGroNxHhgeCgwhlIKUFHq1LXXTULYm3Va_rLoD1PcAoXU7q9KFkLzsfAiufnQ16Xh__j6cvaqmsGTZvNFIgXIsf6a85W8A1yVLQw938LP3LfeFp7YDyLOPYbp1Nq-AsiuiV9VOQsYTESGMDmr-PGzfvPooMVPpzJFO5R8Wnl2cRLKBrkz6WXtl9qBgiQv-7qECuVJ61CCakATk5vtDO7XJIVNop2dCTNMIryWrUkeiiEoc7N5Vz3elVBOrOIhGgDC1JFvE4IbNWbiMkoZIJLMCoaZoZvrO2-puF2rx7ZTxQKHRyZ7USpLt8U8tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
محسن نامجو در کنسرت نیویورک، شانزده شهریور نود و دو
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/70817" target="_blank">📅 23:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70816">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d075c961c.mp4?token=Q39qxb2Z5IA3AWnwb6AsDJNUrzck51fhtJxCoM28ltoQugPgCvUYbxbpvruRq5Eh9_ujQexVZfjg6Sn1QM1lY1o-By6l1Lv9fqBKsHR_UgwodsvVmGfH1PxYKCtEeDQnfXAAslYObV7Zk6NJnLi2T-3zZLnICZ6xkCtM2ktRC8q8DH4YVnwJdp4yjHmJcKYVuPxIbLfsAwMShoR5M-dawA54UgYtgmTbPsbHhkrIZjThhR6Jtu30md7Y3pYGLCbJ5m_bODnR2T2Os9tCjgUT3uG6PFyM6Ze3VL0s5RGJxq6N-Dhj8UinCT6bs4eBnOTNHuGjGnrRvEm7Jdxl8JzzqpdLebP9L1d2_NPx3L_eXLbNBbcD8hjPNX2YxPa0Zw5mvqbLYTPVqJHFg60_fVmnUfRCGqfVkcm2hE0n0beYP__G2N2Pc7fl1tXXfyYFfz9TVw1OD_60077ASMx96JJBtbWMREKlVTMi6RSxCed7yRtYhqm7rQLOs0vYDK11EcT1EgPBIrzIW2sfvBHySVF0lmjO5s1JDD5oUFIhigJWQJbRfhdVApM3ylKurg-GpqogqcLe_FbI0CGSU8BVcGQfSMaFHHlB2JE7SXfydNzfLPcaf8I3pp9CdKN-8hgk5iffa9xivQkVAB1cy5DzsHyyWDtesYuAOyLGTf7pC45dqjc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d075c961c.mp4?token=Q39qxb2Z5IA3AWnwb6AsDJNUrzck51fhtJxCoM28ltoQugPgCvUYbxbpvruRq5Eh9_ujQexVZfjg6Sn1QM1lY1o-By6l1Lv9fqBKsHR_UgwodsvVmGfH1PxYKCtEeDQnfXAAslYObV7Zk6NJnLi2T-3zZLnICZ6xkCtM2ktRC8q8DH4YVnwJdp4yjHmJcKYVuPxIbLfsAwMShoR5M-dawA54UgYtgmTbPsbHhkrIZjThhR6Jtu30md7Y3pYGLCbJ5m_bODnR2T2Os9tCjgUT3uG6PFyM6Ze3VL0s5RGJxq6N-Dhj8UinCT6bs4eBnOTNHuGjGnrRvEm7Jdxl8JzzqpdLebP9L1d2_NPx3L_eXLbNBbcD8hjPNX2YxPa0Zw5mvqbLYTPVqJHFg60_fVmnUfRCGqfVkcm2hE0n0beYP__G2N2Pc7fl1tXXfyYFfz9TVw1OD_60077ASMx96JJBtbWMREKlVTMi6RSxCed7yRtYhqm7rQLOs0vYDK11EcT1EgPBIrzIW2sfvBHySVF0lmjO5s1JDD5oUFIhigJWQJbRfhdVApM3ylKurg-GpqogqcLe_FbI0CGSU8BVcGQfSMaFHHlB2JE7SXfydNzfLPcaf8I3pp9CdKN-8hgk5iffa9xivQkVAB1cy5DzsHyyWDtesYuAOyLGTf7pC45dqjc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇵
🇨🇳
تصاویر بالگرد چینی از  سرچشمه سیلاب مرگبار در مرز چین و نپال
یک بالگرد چینی خود را به نقطه‌ای رساند که در آن یک یخچال طبیعی فروپاشیده و حجم عظیمی از آب آزاد شده بود.
این حجم آب با حرکت به سمت نپال، خسارات گسترده‌ای بر جای گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/70816" target="_blank">📅 22:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70813">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gvAOmvaGM5siWofOuizEJcwrUSyT5x5WQz0zDb65JXE-j0ZYyxYTcW3NHB8a7IvvQkeeGQuRjgz8z9FuM6Rss7uJXWbN4ksZGD-ApCuNqzUBtGuQQ-Rj2FnedLS1ueM6orEJ-LN4QUI5fmNPHDt8vj6Mng4vQo4GSLbWiO47oZ-x03blwMgvoFcqikb_aE2jhzL47GTwPLPiedKyKXnVQpdKHCYtcqlsHV-EPK7pERz0A5JMkbyE_ntoFE0oUWwZ_yHUz3Dn6wVjQiVPO2aB5WXJslA9j2jWYm6_pftDnBH0uwqX-jw-l65U-RK4ga6cc3yZUpcE2r0Eo9R_1yGfOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vWxSS7mZ1YNn4ooeFWFNodhRgMs2qMJ7LawObFH6J1-DCdZsHtqTJuYhZHqlhGMyjF1gSUNuSAd7Kk2YJlrxdC383GFiNktkWFm8F6g6ylaV6SuUZUZWH6xBykRqTiv5pFC71bF-LafsYD7cskXGClyiZ8HR3ydaXcCVZXDoAXtRULPJASy8L20vQnXsztWZM9Y-JWRb_AwWdc0-dVY_0E3SArAe5ObzEFz2cb3-Ld7EDIVOTicF99ayAvAAp95iLJgVfndX3ukC4sQP-OZHQBGG1zPa5N__2aKKlMfW9KG8KrWAkzFJI-MfPwiQExZgjno4B2hai_bXm5TkpcKmZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r4w50KjSPEyZbc0Fhk9hop_i2H_SX3PFOv6SYp5aWGSPFE-7CAYU1WO-LCUKKgGYJ-l5xbLJ0Qag5K_FFBh1c2C6G2f_fyhvO_VvR37oOjtyKk39LPld--3Lc0uJDlaeGiJGA8jRu2aZWUf7WAHHxU49Lb492Ajx7M6h9p2DiEff7cVdzP04jpLQtu8xG-bP8wrmMoZYoHxNwpe9ulxld04ZEJKVhlOGwo5ArmL0VKRUTD2AhfFlAlSH_NcjT_2s2gPyQPPPF-53BsOiuVGG6axy8ChunPurmboLntNar78yPJjZhuxI59s6-ZinWzUxiEGN67GLp90bOpWxs3up3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
از کیوت‌ترین عروسک ایران به اسم:
کون‌کش، رونمایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/70813" target="_blank">📅 21:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70812">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cedd59487c.mp4?token=qqviy15q7IEs_e7IfG8lk1W9cKHLXCD2xtTIv2xTz83e2W_HaRXP7jwayv5Tk4xfF40wh_yipuTR6B1KEFjomoQFXQbCi9zXKlZNwOMGM0i8hm04-D82GxVsIITlm3hhncaOGhmGxsIG5kEwwhAbEhnW85FovJXnTh7UAtUurGhy-sHxRdIjqt_O7bSTgFwSZvPOOjKRSMUsK7sBk5JD00wODAXLpyMr2AWriq72OwmxeLV9vM8-avMk4Dlt6ZAsHK3z2WC39cTNWbIHCsvu-FkqwSPMqbi0JRKjz4lTfxnI8UabZDiTZH6yJD-0pZFgu-605fm0FVJgDgACcyWiDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cedd59487c.mp4?token=qqviy15q7IEs_e7IfG8lk1W9cKHLXCD2xtTIv2xTz83e2W_HaRXP7jwayv5Tk4xfF40wh_yipuTR6B1KEFjomoQFXQbCi9zXKlZNwOMGM0i8hm04-D82GxVsIITlm3hhncaOGhmGxsIG5kEwwhAbEhnW85FovJXnTh7UAtUurGhy-sHxRdIjqt_O7bSTgFwSZvPOOjKRSMUsK7sBk5JD00wODAXLpyMr2AWriq72OwmxeLV9vM8-avMk4Dlt6ZAsHK3z2WC39cTNWbIHCsvu-FkqwSPMqbi0JRKjz4lTfxnI8UabZDiTZH6yJD-0pZFgu-605fm0FVJgDgACcyWiDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکتر برا مراجعه کنندش تزریق لب انجام داده و از شدت ریدمان، خودشم نتونست جلوی خندشو بگیره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/70812" target="_blank">📅 20:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70811">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruUoXL4Pb4rdGzAd4ZRAswJEcmGFREp7Th4z4gpUwt6t7jvqZcWwax3xZRDUUq0vdaf-U6CxqxProUublaewzIelRyOtyxCkKN0Mm_UaGUgaGNkJG3BDGnDd-2GrK2wNprYzVIAba6NoLpL5HUxw5hzDJ9098hxB281oGcoLJxSBaXd7XTsh5mjvW-Zl8FDhecBuZzyiv-b7ynZiKD490lfdbbaYAWAL00K6MCl_MVEB1ibKIRA-JxSpf1kCJpcIVBzw8KcXOSi-S4wuxg3P5-iOZcx29ygQ3aZPwYBiygthJn0g-YcKUss2B9-onD4TIDuKJaua66uuvbvV9riYCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا UKMTO:
یک نفتکش هنگام عبور از تنگه هرمز در مسیری به سمت داخل (شمال)، در موقعیتی تقریباً ۱۲ مایل دریایی در شمال «خصب» عمان، هدف اصابت یک پرتابه ناشناس قرار گرفته است.
این حادثه هیچ‌گونه تلفات جانی یا پیامدهای زیست‌محیطی در پی نداشته است.
موقعیت مکانی حمله نشان می‌دهد که این شناور هنگام استفاده از مسیر کشتیرانی تعیین‌شده توسط ایالات متحده در آب‌های عمان، هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70811" target="_blank">📅 20:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70810">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQuN4MYNXgIf6TNEZrJxWdVTeuK3MTw5SJFjYUHmf5DMR6VPLejns9IxPsZx_uDO-Xh5gYZ0jhVhVDo0uKAAbwLANlIyhZF1GOdU6Y0zam5fqHMI_bkD-xF2M9EhxDqBWyg7ofsFZlb9t-gz68dCO4CwyToE8dQezRADzskRolBnTEsUV2iNided7XQT3am48AYzgLNufxz2RYabA7zClZ3EvxHKhf8TbAi8WgKDrhW48PEif2lo7chCsbVGmgZ3SPyWf0Kb6NsdraQWshgVeyDk1jIoqkVl6gPO0YUM1Rl1iAPWUX0prEJ9lvHqFTKSKiwThfi2Rqg40jwy-sWHCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ برای اینکه لج کانادایی‌ها رو دربیاره، اسم دریاچه کانادا(Lake Ontario) رو گذاشت «دریاچه آمریکا»؛
کانادایی‌ها هم کم نیاوردن و از لج ترامپ اسم دریاچه رو گذاشتن «دریاچه هرمز» و تاجایی که میتونستن این موضوع رو تو فضای مجازی وایرال کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70810" target="_blank">📅 19:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70809">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ce04d5d87.mp4?token=GT6fCHB_R7g2FH1NCRJV0V2Zzpjeja8gLj9-pPy6Gn7BtqJBtvP6Uok7PXnzpX3YquYId2-blXh4ErFMF5AkqQ6xC4xiEpA3FHAelLyOV51ZcMOVB28aKkr5BH6gFRSm6R6qB1CvMGv5NzOtfkny80gx3rW7wey0WSoofi9IMjWpSy9D_yB1bgtHt4t-GAwk44R1LOQ5VAlN7MF5xnA6vlb2HiKd0b5ZRF6VO1ekYhdNX66M8CpmYe4x5JZXG2Zx5gMMOgo0DMSP0ZQan6an3yhfzXPy3oq6K033uxK2I3xE4P-kZr33cshNiwA1nlQK-EpsqS6XqVyB4LA_RMBctw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ce04d5d87.mp4?token=GT6fCHB_R7g2FH1NCRJV0V2Zzpjeja8gLj9-pPy6Gn7BtqJBtvP6Uok7PXnzpX3YquYId2-blXh4ErFMF5AkqQ6xC4xiEpA3FHAelLyOV51ZcMOVB28aKkr5BH6gFRSm6R6qB1CvMGv5NzOtfkny80gx3rW7wey0WSoofi9IMjWpSy9D_yB1bgtHt4t-GAwk44R1LOQ5VAlN7MF5xnA6vlb2HiKd0b5ZRF6VO1ekYhdNX66M8CpmYe4x5JZXG2Zx5gMMOgo0DMSP0ZQan6an3yhfzXPy3oq6K033uxK2I3xE4P-kZr33cshNiwA1nlQK-EpsqS6XqVyB4LA_RMBctw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
حمله پزشکیان به صداوسیما:
مسعود پزشکیان، رئیس‌جمهور ایران، از سازمان صداوسیما به دلیل سانسور خود و سایر حامیان تفاهم‌نامه با آمریکا انتقاد کرد و این نهاد را به اتخاذ رویکردی افراطی متهم ساخت.
پزشکیان خطاب به جبلی رئیس صداوسیما: «این روزها دیگر اصلاً تلویزیون آن‌ها را تماشا نمی‌کنم. آن‌ها مایه وحدت نیستند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70809" target="_blank">📅 18:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70808">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58b978362a.mp4?token=eLXs9_rqv1FMMaojoEbhEJbVynnhe5drUNwwGtfnXZ-bpYrEAq28Wpqcu_E_0Rb-oA-UE7H3AFRdw-rKw9BEUsCtsKCkPIoCK5jubY3kV8AnCD40jQC8Su93-hhC8_agwkHoIXVKOesaOSqmdr0wGUaUs2D1w2rz-7p0-KkoywbL489r46qq1Vx0c1_AUpAdF6dH2oZC76OOh9L3W_VoMpgwSD9B3PBMKaNvpGASNtW_jxNqaYtQ3Ni9toSNRJpnBZlosQk7_QWwR4aYQZuy14CRs_HRxRknNqrLHxsVSCiawsYxmSJ_gp76WpdjFRQOQPauhF0WiY6qO7ph0hbydw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58b978362a.mp4?token=eLXs9_rqv1FMMaojoEbhEJbVynnhe5drUNwwGtfnXZ-bpYrEAq28Wpqcu_E_0Rb-oA-UE7H3AFRdw-rKw9BEUsCtsKCkPIoCK5jubY3kV8AnCD40jQC8Su93-hhC8_agwkHoIXVKOesaOSqmdr0wGUaUs2D1w2rz-7p0-KkoywbL489r46qq1Vx0c1_AUpAdF6dH2oZC76OOh9L3W_VoMpgwSD9B3PBMKaNvpGASNtW_jxNqaYtQ3Ni9toSNRJpnBZlosQk7_QWwR4aYQZuy14CRs_HRxRknNqrLHxsVSCiawsYxmSJ_gp76WpdjFRQOQPauhF0WiY6qO7ph0hbydw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امیر ابراهیم رسولی، دستیار قالیباف:  ما تا آخرین روز خون‌خواه رهبرمان هستیم امّا پوشکی که من برای فرزندم قبل از جنگ می‌خریدم ۳۶۰ هزار تومان بود. امروز همان پوشک ۸۶۵ هزار تومان است. باید آرمان و شعار را با واقعیات جامعه تطابق بدهیم.  @News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70808" target="_blank">📅 18:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70807">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6pzi_1XMM3czKWG_-2iBnvc1fVgcyc8BPsJqDOZ3pYlXVuGEpIy89Fj88VLvB83wTtOnNVMWLmBSt7u5uHzChxgvQXVkAPCA_6lDKCLZzN0BUuHzaUxXXTBqC4JMNMs_BpDx0mlL9TnNuLEeRKzzs17VxzCvMXtwd69JR7E2WaQSW-EH5SKxaAHogJUsMNnkCoBR1HCh_Mk-sQRlMp2hhiQvr7ecYzIs_Q_8NYm65kXQDrJ30NvtdNRysXlf5l-rUcJjqwHnrqEbHF2_cI03fOm_IlqAake3qyKkHxr7Rj534-bJBFVXN8oKXCxye9iBTh1oF5O4KtE-jEl5HAqig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70807" target="_blank">📅 18:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70806">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اوپراتور های حروم‌خور ایرانی مشخصه رو بسته های اینترنتی ضریب می‌ذارن، من صبح یه ۴ گیگ هفته‌ای گرفتم الان تموم شد، آخه چطور ممکنه فقط چن ساعت اینستا بودم
😐
از سال ۲۰۱۳ تو اینستا بودم قدیما با مودم یدونه ۳ گیگ می‌خریدیم تا یماه می‌رفت، شما دیگه مرز های وقاحت و خارکصگی رو جابجا کردین خدایی
#hjAly‌</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70806" target="_blank">📅 18:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70804">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SY26WKbld92tmD9thN6d2Knq4TFvrbchKsnCQS6fzINLwGn8TzNyK_T7_7om010x6Nk9NPavtYZGKBDW1ZxKGJfV-CF4EF-qmKSZu3GCS276zX6LE3qQNFooHgB_92lUWPcQPMNlQ8b28wYrvfPJjh2aNIWjuKCraU7f_wJFOpi7JsE1PKeM6mjgdFfl9AFv-S3P6FEviH_AeM75UqcOEujIa-i_yOhU3IzB5nCr637cQYBltOuqxi1fmFPeoNOd82ue7d1RF9scFZjGK3tKgj_fvuPZ3zOxSU6j5Hzvst63E8bOHqX4_c2rAhMkD7FYKa2Q-K0HwwRiGnW0LpK4qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sFtADxOrv3ees38IZBTw1qw5H8FX8r-LEWl9uFUdvnYE4ODNrlKEccEwifxpiW5f0L8KApdWCrDXWFybyoKZ678ygFKR96EiiO2mKnAd92RAvyh-xq7Hhj263gjCbJWhFg9vcIJOnY4QljFgoQeFkL-vfC3fgnpKmw9geTYX-MDcgIvsSw_7TRbYMpmQrEEtU62EUAD5iWaIVwSeNSBZxE_9ZtSU3tYlYwy8c6lgsgdV-cKUKYOL06EYOE1KTLDnI53FL4uk9bGSCNqFTNDI8wer1d7kC_uV7JNboyv89bc5kIY0sQKl4oBqwAN7cidGI4iSNIqwW_RmPX64n62NbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تصاویر جدید مادورو در زندان های آمریکا که گویا در اونجا از ایرانیا خوشحال تره.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70804" target="_blank">📅 17:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70803">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55cc84ead5.mp4?token=GFadt4rnlvp6_Hz-ImvbyP8O3GO_DOKowGAbTDC659EBuiCMla_XWpZ7oukuxrXl_9HAPUqAQ4wbwnuenG9EOW3qZGTJqquaioF8ydENVX1SqfRCUrczaCHsll7JJJhfzp1RRJZjCVGzq93Er8zOkQz6a_WANA2GomFOc2WTSZLq_CgI29Mc216cSGqyd7RmAxV44smcXnxDaZrAqWonFInIIeMTVotFa5sxSSCR7Xb1klwFl51eT0lk2-3qD0gfw9M_spxDa1K-D7ijZHBzBeYEgk5nenguo_Q-A4gkjxYYK_hifKPDUmH6oCI5iWi3lwNXo9p7GuivrBcpm9otsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55cc84ead5.mp4?token=GFadt4rnlvp6_Hz-ImvbyP8O3GO_DOKowGAbTDC659EBuiCMla_XWpZ7oukuxrXl_9HAPUqAQ4wbwnuenG9EOW3qZGTJqquaioF8ydENVX1SqfRCUrczaCHsll7JJJhfzp1RRJZjCVGzq93Er8zOkQz6a_WANA2GomFOc2WTSZLq_CgI29Mc216cSGqyd7RmAxV44smcXnxDaZrAqWonFInIIeMTVotFa5sxSSCR7Xb1klwFl51eT0lk2-3qD0gfw9M_spxDa1K-D7ijZHBzBeYEgk5nenguo_Q-A4gkjxYYK_hifKPDUmH6oCI5iWi3lwNXo9p7GuivrBcpm9otsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
حرفای وایرال شده رحمان و رحیم پایتخت درباره ازدواج :
ازدواج نباید دوقلو باشن چون ممکنه این وسط اشتباه بگیریم اونارو
آقا کاره دیگه یهو دیدی در رفت دیگه نشد جمع بکنی
سارا و نیکا هم خب اون زمان تازه بچه بودن کلا نمیشد
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70803" target="_blank">📅 17:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70802">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d5696dbdc.mp4?token=lM_gBROwCIjImdGvKNqkWM8oZzoceAThN36uzIfD8wHzt_OANxHmqaIfgTsOjSXSXJxuo9hhkSHP_ukOG3pAKDzvz3KPlGqxwFYItt-J5b0f6aHSu1xfA6w43rh7PNDfOW0Tdh9sS_lq3qQDz1lpMs83VuIxQ2Pi0SsxEwfcUvatHS6_r1bFhVNqfaMe3oNXufeulkReEAlrPl4RaW3NcF5RuziuWaZ88bs2Q3CCqE7jLS8X6CrlGHq1osyzRSeZIgdu_Es_C8_Bb-qnHU-H3gFHd-DO2UifxLcqvNyGcNVr7ooG8JYDomFX2zo9eSKLmoEK-yR_yS_XxcDTqSRoVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d5696dbdc.mp4?token=lM_gBROwCIjImdGvKNqkWM8oZzoceAThN36uzIfD8wHzt_OANxHmqaIfgTsOjSXSXJxuo9hhkSHP_ukOG3pAKDzvz3KPlGqxwFYItt-J5b0f6aHSu1xfA6w43rh7PNDfOW0Tdh9sS_lq3qQDz1lpMs83VuIxQ2Pi0SsxEwfcUvatHS6_r1bFhVNqfaMe3oNXufeulkReEAlrPl4RaW3NcF5RuziuWaZ88bs2Q3CCqE7jLS8X6CrlGHq1osyzRSeZIgdu_Es_C8_Bb-qnHU-H3gFHd-DO2UifxLcqvNyGcNVr7ooG8JYDomFX2zo9eSKLmoEK-yR_yS_XxcDTqSRoVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صادق الحسینی کارشناس اقتصاد :
کیفیت بنزین رو جوری پایین آوردن که تا ۳ ماه آینده تعداد زیادی از خودروها قراره تعمیرگاه صف بکشن و موتور تعمیر کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70802" target="_blank">📅 17:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70801">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1befe3460.mp4?token=H79F0k6Az6XAskXWd1lxYt456m0MeI5IS7uc9LTTe3SfABmNsNpnzCx1FznDXHDGqlsdTA0jfVQuikgpVBi3ZuuWN2iF_DanbLVovxwfWMCDsSR4c80Bh-tOchhW9lidlwdaCdhHWV5zef1JyrQnJLFZWlnLj8rzoDNCn35y97b_J1uvk4Yx0cVKitAwxN6smZC8R9bRd5QZTJSyAMrg1-pxJrrqo6p2gjfMOiwQAlvLxeCTjbPHp-GonWjCSsh1oGkj1fiz8xyvPDnkiliw1P3607UfCTv2qOpBTxsUpVOaq0CZ3sTZSmsVr4iJbdlOLfsF4S3JKjpuwYCtKzbv2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1befe3460.mp4?token=H79F0k6Az6XAskXWd1lxYt456m0MeI5IS7uc9LTTe3SfABmNsNpnzCx1FznDXHDGqlsdTA0jfVQuikgpVBi3ZuuWN2iF_DanbLVovxwfWMCDsSR4c80Bh-tOchhW9lidlwdaCdhHWV5zef1JyrQnJLFZWlnLj8rzoDNCn35y97b_J1uvk4Yx0cVKitAwxN6smZC8R9bRd5QZTJSyAMrg1-pxJrrqo6p2gjfMOiwQAlvLxeCTjbPHp-GonWjCSsh1oGkj1fiz8xyvPDnkiliw1P3607UfCTv2qOpBTxsUpVOaq0CZ3sTZSmsVr4iJbdlOLfsF4S3JKjpuwYCtKzbv2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
پایین کشیدن تصویر مجتبی خامنه‌ای در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70801" target="_blank">📅 16:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70800">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c5ff11496.mp4?token=hXdXG3JoWR3TVlK0s43Ja4dYx9SPKLc6jx4jeDTwHyua2wk5dVE5dUoyzg_zOjVKH_jtOmkYGZEKzgVFOJmVjh7QX-Xmec9QDsPTn_xlVS5hsMb2F7LEmK9ivdNwyOXg6HA_PaJWisRJP3R8hdZiU9Fm_8kUihMPJmigw7yrJztlloj6tpyfaf-My--zIOCZ-80BThOMqCBQ4hORNzKKuMwlf2yErz2xwVD1g_gagxYje6qD5BosO-pNqRpUlw7kjytQofFUzS9Uzx4rwdjVO0Pu7OK3rFy2AmlhZIkRJiPXyM2azeP20IwX02Y6xxiWQo1b-u1XtS2oBcAmzAvsBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c5ff11496.mp4?token=hXdXG3JoWR3TVlK0s43Ja4dYx9SPKLc6jx4jeDTwHyua2wk5dVE5dUoyzg_zOjVKH_jtOmkYGZEKzgVFOJmVjh7QX-Xmec9QDsPTn_xlVS5hsMb2F7LEmK9ivdNwyOXg6HA_PaJWisRJP3R8hdZiU9Fm_8kUihMPJmigw7yrJztlloj6tpyfaf-My--zIOCZ-80BThOMqCBQ4hORNzKKuMwlf2yErz2xwVD1g_gagxYje6qD5BosO-pNqRpUlw7kjytQofFUzS9Uzx4rwdjVO0Pu7OK3rFy2AmlhZIkRJiPXyM2azeP20IwX02Y6xxiWQo1b-u1XtS2oBcAmzAvsBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این دوربین مخفی و تلاش این خانم برای اینکه جلوی خفتگیر رو بگیره خیلی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70800" target="_blank">📅 16:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70799">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fdd874dd6.mp4?token=d5vyvSXRHtKeuu4FIbc0utFTyuYhn9cdAw_S1h9T65ofPDhrt7UUwZoSHppFQpJHvUACORJRCW0Ljo-GO2HyTiBhQElr18Hr3GXjQXpsrCS2tWQNlAZ0ylt3VjU2KmFfaCEE1dYRiwjnLlLlt4Y011KpRKRCzbYWtCvhugwJ-wgkIS5B4D6dyJf07fXWQkb44mKs-aXqKGQpReqdW6k8PgD6Hokxlt99TU0svsJjnEglYQF7AstqlPsozv-SrWXN0lEogajsEP8vtEmTHw4s7NKPOeN2IOKtZv-PeUAc9hqgzaFcymUEFJKUNjSUArNqJ9MQmtInxmJoAD7apfwNXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fdd874dd6.mp4?token=d5vyvSXRHtKeuu4FIbc0utFTyuYhn9cdAw_S1h9T65ofPDhrt7UUwZoSHppFQpJHvUACORJRCW0Ljo-GO2HyTiBhQElr18Hr3GXjQXpsrCS2tWQNlAZ0ylt3VjU2KmFfaCEE1dYRiwjnLlLlt4Y011KpRKRCzbYWtCvhugwJ-wgkIS5B4D6dyJf07fXWQkb44mKs-aXqKGQpReqdW6k8PgD6Hokxlt99TU0svsJjnEglYQF7AstqlPsozv-SrWXN0lEogajsEP8vtEmTHw4s7NKPOeN2IOKtZv-PeUAc9hqgzaFcymUEFJKUNjSUArNqJ9MQmtInxmJoAD7apfwNXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان درباره کسایی که میگن تحریم هیچ اثری نداره:
نمی‌دونم چی به اینا باید بگم فقط همین رو میگم که عقلم خوب چیزیه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70799" target="_blank">📅 15:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70798">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/036dee7c15.mp4?token=IU1yuAbShpVzO6LSFinCVAsbULGskbjlI8nprbGvrWYEdrMtYMCa1uC9QOpNihgpaxj2Fb4pWOtkIL1qs4JKFxt2D65gnawODG5Rck9Ar0sn-ZkD5ImNeA8y592bH0JGkhbiiulVcv0v_Ev6GzTlADNG1GmKhWXOdSFH7b4FtmKQGe4hAdnS2MS6_QhHowAjHne_f1uxUEDhz64lPMgIpk3DRd_L--Fh9TbcGWpJtEK7JtchQkFcE7LEG2_rXMHLh84qBreJL1fZb9E7O2drt4ZlNscUHmI-95wpbecx-QThrDT2V41aWEwGmOhmPz8jn72bnQrV3T7DDUYPbQ4Jmw5bWCdLwG1qPHzv_F-6uobb1vX3yZpGnV_finxswdWo6XS4WkxwJ5y5P7x4ZMsJK2km9doRvn8lIB1q-cnuvhqTsf0DAViBNs95wZ5WiWVHZqSDinu3pXyqxp7EIEuOT-UK3GNh2uPfFBDedmcFqSyUVJkmTfpAFxDABLHSWk-27_Nq4AyHTakFIHdgi6DfGUBimcuC42ETn47MhjKYiPhC2NjxXcZSlvZ_yt8Ewn9wxfOzd2VqlrihY06zI3Gz2SozcLZGesngSyRm98S7wyNMcCAVrEuTAnJ5NjAaZVccHOnM3yqYqtBiyoam0JczLCZCDU_xYuhqK_JAXRCy3os" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/036dee7c15.mp4?token=IU1yuAbShpVzO6LSFinCVAsbULGskbjlI8nprbGvrWYEdrMtYMCa1uC9QOpNihgpaxj2Fb4pWOtkIL1qs4JKFxt2D65gnawODG5Rck9Ar0sn-ZkD5ImNeA8y592bH0JGkhbiiulVcv0v_Ev6GzTlADNG1GmKhWXOdSFH7b4FtmKQGe4hAdnS2MS6_QhHowAjHne_f1uxUEDhz64lPMgIpk3DRd_L--Fh9TbcGWpJtEK7JtchQkFcE7LEG2_rXMHLh84qBreJL1fZb9E7O2drt4ZlNscUHmI-95wpbecx-QThrDT2V41aWEwGmOhmPz8jn72bnQrV3T7DDUYPbQ4Jmw5bWCdLwG1qPHzv_F-6uobb1vX3yZpGnV_finxswdWo6XS4WkxwJ5y5P7x4ZMsJK2km9doRvn8lIB1q-cnuvhqTsf0DAViBNs95wZ5WiWVHZqSDinu3pXyqxp7EIEuOT-UK3GNh2uPfFBDedmcFqSyUVJkmTfpAFxDABLHSWk-27_Nq4AyHTakFIHdgi6DfGUBimcuC42ETn47MhjKYiPhC2NjxXcZSlvZ_yt8Ewn9wxfOzd2VqlrihY06zI3Gz2SozcLZGesngSyRm98S7wyNMcCAVrEuTAnJ5NjAaZVccHOnM3yqYqtBiyoam0JczLCZCDU_xYuhqK_JAXRCy3os" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنلاین شاپ های اینستاگرام برای ویو دست به هرکاری میزنن
مثلا این ویدیو با ترفند شیک باسن باعث شد میلیونی ویو بگیره
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70798" target="_blank">📅 15:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70797">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0459b57f2.mp4?token=ozdcIFI10k8zTdVUF4pxHgIf2o6_lPNVn2JB9w7DTOYAgrqx5fu3bFiabccezR1i8vSGxNO58jeTBO3DgpB5vFcTxr7H13qnNHWTKk5MAzbNCgoOTY0APFHDfwX2qhVUQWBRDNSU3g_sq1vOEKKq_O8VJfc0I0WwSj3w66JEKYeFHpjJbo__Q7vOam1AcoScZ3yguhrvY4sT7dQfCpYZ5wbN3d7s7EJzLQmb2kW48-Qd52SRA9lBHZThs52QTsxBY6mdc50eXJXZWPW0lRXdim8WyUMGWcQzvaPTSpr2rFMiByf3D3FI-UDGeK6_aNCU42OQbQbGdDLywBZbxpLCAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0459b57f2.mp4?token=ozdcIFI10k8zTdVUF4pxHgIf2o6_lPNVn2JB9w7DTOYAgrqx5fu3bFiabccezR1i8vSGxNO58jeTBO3DgpB5vFcTxr7H13qnNHWTKk5MAzbNCgoOTY0APFHDfwX2qhVUQWBRDNSU3g_sq1vOEKKq_O8VJfc0I0WwSj3w66JEKYeFHpjJbo__Q7vOam1AcoScZ3yguhrvY4sT7dQfCpYZ5wbN3d7s7EJzLQmb2kW48-Qd52SRA9lBHZThs52QTsxBY6mdc50eXJXZWPW0lRXdim8WyUMGWcQzvaPTSpr2rFMiByf3D3FI-UDGeK6_aNCU42OQbQbGdDLywBZbxpLCAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
آیفون 17 پرو از ارتفاع ۳۰ کیلومتری سقوط کرد و سالم موند!
آیفون 17 پرو رو با قاب محافظ
RhinoShield AirX
از یه بالن، از ارتفاع
۳۰ هزار و ۶۰۷ متری
زمین ول کردن!
باورکردنی نیست، ولی گوشی بعد از این سقوط وحشتناک
کاملاً سالم موند
و حتی یه آسیب جدی هم ندید.
🔥
🏆
این اتفاق توسط
گینس
به‌عنوان «بلندترین سقوط تلفن همراه درون قاب محافظ روی عوارض طبیعی زمین» ثبت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70797" target="_blank">📅 14:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70796">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omjsdcxc6Eclk-IxoBGRs9eMBT1esi89_TDSa4bLsHedwxanWdWodbc0OWB8Re4wQ6Ii3pCSPisPznZQCec93LNQXvHTmooc7SWYzVpPwChw_gS-U4fV9hc-O2WJJ7hiSFR-Z-4st6qoAwNCwZ41Hdsae2rkNs54H6IH2A2DdqUfu9wsoCKXJdcmfLnSCese3ElDtTnZU8Sb7DhVDholIhLSKqP_td4qB8sgcazLDtYyVCKDxDrJhsMlJIcCx2Ljpk3mRpenlfX5dBqveoPAe3eoTHsxt5LWzeMwGXUXDcO0MSGGyVxV7oJCXZzIX6SO0Vt9u8NnRooy0arjlBctKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تصویر ماهواره‌ای از بقایای شناورهای غرق‌شدۀ جمهوری اسلامی:
تصویر ماهواره‌ای تازه،بقایای ناوچه‌های جماران،نقدی و بایندر را نشان می‌دهد که در حملات اخیر آمریکا طی جنگ ۴۰روزه غرق شدند.
در این تصویر همچنین بقایای احتمالی یک شناور کلاس دلوار و دو شناور گشتی کلاس هندیجان دیده می‌شود.
محوطۀ پیرامونی نیز آثار گستردۀ تخریب ناشی از حملات را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70796" target="_blank">📅 13:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70795">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45caa5a649.mp4?token=iRsWnnlFfWlEC89kzgWVh1IcyghO_04ENB9d5mEyvasmIasyr1MyNuNk3_GQnmVbOUidlSSjwiVQA9E1aHBviWQ2lAL2pA9ErVS2BJm1fOJvv2TTrekk6abNRdjbMv4KPhNOs3r11paKATPpe5z1AzRplVQatVtAMdrweM1Fjov4hfffW4uyOyvHoUnQcMhDZ2eXd7840L-qQdAtna31QAU9z65JPqdb3-1o2zBW2yhBnlGfheA8DtKnIm6MIzGfZiVNjICXyiu3a9JY_sebjFe07CVeLQH4VRGZC0Hhr6Pz4l5g9o5GI144cQsm9sgFeI9LmaV7fpO_BeFFiR5iqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45caa5a649.mp4?token=iRsWnnlFfWlEC89kzgWVh1IcyghO_04ENB9d5mEyvasmIasyr1MyNuNk3_GQnmVbOUidlSSjwiVQA9E1aHBviWQ2lAL2pA9ErVS2BJm1fOJvv2TTrekk6abNRdjbMv4KPhNOs3r11paKATPpe5z1AzRplVQatVtAMdrweM1Fjov4hfffW4uyOyvHoUnQcMhDZ2eXd7840L-qQdAtna31QAU9z65JPqdb3-1o2zBW2yhBnlGfheA8DtKnIm6MIzGfZiVNjICXyiu3a9JY_sebjFe07CVeLQH4VRGZC0Hhr6Pz4l5g9o5GI144cQsm9sgFeI9LmaV7fpO_BeFFiR5iqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
تاکر کارلسن، تحلیلگر آمریکایی:
در نشست‌های پنتاگون درباره نحوه واکنش به ایران، گزینه استفاده از سلاح‌های هسته‌ای تاکتیکی بررسی شده است.
روسیه، آمریکا و اسرائیل در حال بازنگری در دکترین‌های هسته‌ای خود هستند و آمریکا نیز این موضوع را بررسی می‌کند.
سلاح‌های هسته‌ای تاکتیکی با وجود قدرت انفجاری کمتر، همچنان تسلیحات هسته‌ای محسوب می‌شوند و استفاده از آنها علیه اهدافی در ایران در پنتاگون مورد بحث قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70795" target="_blank">📅 12:28 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70794">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9d50eba94.mp4?token=Z7Xw7curDCSVTE-yypmZr2-bc1ILCmrZN_KXibRd1N4o3bKKd3r2dKeY7zqXrBv41GBfSjfEq251VPr3VOikBzkl6gRjgXS9nT_1DSKJKvlSGnGp031J9G8YflPUNdXDcnjGz1hV68x9o7rrhZBUGjQufF7Iao-Fncku6VI0cjDUox0fc7IH80sUhEVuwAP7Xt6daWJeS9xzIvnZqjDL9aoLpTxTN4eM85cDc-0tpaqkZytt3kVjz-jXm5Y1FWVYuR5NiTi1haFW7owByhQY6-R5BGVgMC6BYzNuePCKRYiw-_j63wI4jYgY3AWPjJzlRq38vaD8vkEHsbgM-CfTig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9d50eba94.mp4?token=Z7Xw7curDCSVTE-yypmZr2-bc1ILCmrZN_KXibRd1N4o3bKKd3r2dKeY7zqXrBv41GBfSjfEq251VPr3VOikBzkl6gRjgXS9nT_1DSKJKvlSGnGp031J9G8YflPUNdXDcnjGz1hV68x9o7rrhZBUGjQufF7Iao-Fncku6VI0cjDUox0fc7IH80sUhEVuwAP7Xt6daWJeS9xzIvnZqjDL9aoLpTxTN4eM85cDc-0tpaqkZytt3kVjz-jXm5Y1FWVYuR5NiTi1haFW7owByhQY6-R5BGVgMC6BYzNuePCKRYiw-_j63wI4jYgY3AWPjJzlRq38vaD8vkEHsbgM-CfTig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدویی از روش جالب روشن کردن مشعل گاز با فلر
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70794" target="_blank">📅 12:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70793">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70793" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70793" target="_blank">📅 12:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70792">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zq2E0BboVYMN8xHvNe3FvN5XRs1AY3Zffpw22Tkw7ySXSco2jx6-r5g2QOH7lTnF_7anPONxVLIUe6iGGuTn1km-Fid5PV9eiOKYSzH6sZKDDJMtJ6noUQ_ESIxvpbkj02wDswElIBT8xoik60xRboudPBVWjwVJyVLA1g9jngyVeiLf1hGdGK3kU5jtfTfPhC4LT6tLy_Vy6mUUb4tsvaE0xjsaVVg6KzCjYFZrssD8iQNy_yHLma7gALcov-Kds9lE__LZkbDeapQyTLCshkEkuxIIVQrLjyxAbP57pkOWyxHFvLmtpX8MZKb379WyZOSHPS183zZGOb6PCrYtYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN
.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70792" target="_blank">📅 12:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70791">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26b95ccb0b.mp4?token=UqqtuhjFXU2DA4oXd7cQCWbX9SyXa9eNS-VR5tjYDFO4QfDw668SZ3V-MNPulNKpCtb7GDTbNN6fCQs71DEqkE592mzJbjMcJR9n7vAG8ULQqwiC8FQoDh5lsirr1XQTGYNtBGExLn2M6LDCvfime0Sqxc105N1rRz_jF4q-t7piazhGSbciaKNVm9G7UJL0exvpdXQwEtdF_nG0XuERbIc7lIrMTv1_Y5XS74Iqee3F3BWqKOFQWFhZaLlc0MwqgRIQ2E-H8OuKvB3IJipTkPqsWL-HyCm017BRvGmc8BrFnajMU3RW7QXSVbqW3dCxF2_O3SPnjYUdFybiBfcK24EhJtEpQixfa3DSOVbVQ5xOVXd5w7QeSO2HGwLfIzXMeQKzRnQaoib72LPJGjdMlGLChZ9FK69RIk1Y27ynhbvq0sIG5UXfnojUUx9cNm8NXEr93XsKPEYEieZnUqhS3mKArYnVOqgmBpYd9joNFPF9dhLzW_d80FsE2-teKkmxjLqS9M6N4-LA5c2J9jCMxLNaGyLbHJVjnvj7_DH4JjTPX88t9YSGPPkiD-4R1_HrT72Ag5KXQQx3tdL8q2mRWT_OKvAAxb8vAQd39M-LmQNYVqxtJDg4BpLFvDynxnMOFjUC_DUwPLwf4qDdVxj3-nDqLoy3naCDtA19VOmsdaI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26b95ccb0b.mp4?token=UqqtuhjFXU2DA4oXd7cQCWbX9SyXa9eNS-VR5tjYDFO4QfDw668SZ3V-MNPulNKpCtb7GDTbNN6fCQs71DEqkE592mzJbjMcJR9n7vAG8ULQqwiC8FQoDh5lsirr1XQTGYNtBGExLn2M6LDCvfime0Sqxc105N1rRz_jF4q-t7piazhGSbciaKNVm9G7UJL0exvpdXQwEtdF_nG0XuERbIc7lIrMTv1_Y5XS74Iqee3F3BWqKOFQWFhZaLlc0MwqgRIQ2E-H8OuKvB3IJipTkPqsWL-HyCm017BRvGmc8BrFnajMU3RW7QXSVbqW3dCxF2_O3SPnjYUdFybiBfcK24EhJtEpQixfa3DSOVbVQ5xOVXd5w7QeSO2HGwLfIzXMeQKzRnQaoib72LPJGjdMlGLChZ9FK69RIk1Y27ynhbvq0sIG5UXfnojUUx9cNm8NXEr93XsKPEYEieZnUqhS3mKArYnVOqgmBpYd9joNFPF9dhLzW_d80FsE2-teKkmxjLqS9M6N4-LA5c2J9jCMxLNaGyLbHJVjnvj7_DH4JjTPX88t9YSGPPkiD-4R1_HrT72Ag5KXQQx3tdL8q2mRWT_OKvAAxb8vAQd39M-LmQNYVqxtJDg4BpLFvDynxnMOFjUC_DUwPLwf4qDdVxj3-nDqLoy3naCDtA19VOmsdaI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانم که کلینیک بیماری زنان داره تعریف میکنه که یه خانم 56 ساله بهش مراجعه کرده و گفته که همسر 67ساله‌ام از وقتی بازنشست شده، روزی چندبار باهام رابطه داره؛
قسمت عجیب ماجرا اینجاست که جدیدا یه فانتزی‌ای پیدا کرده که میگه سرت رو بکن تو ماشین لباسشویی تا از پشت باهات رابطه داشته باشم!!
الانم این خانم سوزش شدید پیدا کرده و مجبور شده موضوع رو به پسرش بگه تا اون بره باباش رو از خر شیطون بیاره پایین...
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70791" target="_blank">📅 12:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70787">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6bb7d34aa2.mp4?token=JsAhGf0_yo9hjR-CdvrIw8bYb5i9L9fKtxO8XOmpXv88UKhxm48pXK4bSw3_XJnYqmD3xWIEOoCugcyn859CGxSO41XtfHuflZyWU8qJYqfm-f-T5FxAgO67K_1Qy9mrZP5l7bMGEWOxKLfigKtONZBsvJCfWjRB5PAcswn3VQw--ubChrIjtbtiMv61DOycVTS9IclvohYYKy1wlgjWtEBnYUYW0KYUDd70MDZSCVNwH6HlmKpLkb0EKAGhQ_qc-pRG1myGj3Fz9MOPEtqzrvYsJ77Z6rTEAfusVLPWzdnsqgMcUC-KIVE_u2CznYX5hZDC-M9YRZHw8nqIglbOcw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bb7d34aa2.mp4?token=JsAhGf0_yo9hjR-CdvrIw8bYb5i9L9fKtxO8XOmpXv88UKhxm48pXK4bSw3_XJnYqmD3xWIEOoCugcyn859CGxSO41XtfHuflZyWU8qJYqfm-f-T5FxAgO67K_1Qy9mrZP5l7bMGEWOxKLfigKtONZBsvJCfWjRB5PAcswn3VQw--ubChrIjtbtiMv61DOycVTS9IclvohYYKy1wlgjWtEBnYUYW0KYUDd70MDZSCVNwH6HlmKpLkb0EKAGhQ_qc-pRG1myGj3Fz9MOPEtqzrvYsJ77Z6rTEAfusVLPWzdnsqgMcUC-KIVE_u2CznYX5hZDC-M9YRZHw8nqIglbOcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روز پیش توی باشگاه انقلاب تهران مسابقات و ایونت تنیس برگزار شد که حسابی سر و صدا کرده:
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70787" target="_blank">📅 11:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70782">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f98f823a9.mp4?token=ANSan5S946-O3ZTaVGNUwtT61lhUhwCT-LCAsL78nEauHQ_Q5TvLgYU60vyFh5w4mfk1fFNIF95_NhOhPJldjGL-HZSsl8VSF0UisYTWX9pvoDqEbN-fhE8ICp7-igilyVT9QxB0qKSmtsmYmHoGt4j7Io1RsR0AHW1lYb867wLPIOJr_HgjGQgVwOLmIWIPGOwR3PFai9U1fQYYn7yL2xYSZ7J8C2tSjer89aNcgJpn0dH6PKmRgiQgyK9L_aIA7mAegbzApmDvUraiuUIwz6mIbxL7vUHzPrB3oXo3nOSbfvIOih0A3hJgII44CSOfM-TibRo39uzv7pYeLTYmAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f98f823a9.mp4?token=ANSan5S946-O3ZTaVGNUwtT61lhUhwCT-LCAsL78nEauHQ_Q5TvLgYU60vyFh5w4mfk1fFNIF95_NhOhPJldjGL-HZSsl8VSF0UisYTWX9pvoDqEbN-fhE8ICp7-igilyVT9QxB0qKSmtsmYmHoGt4j7Io1RsR0AHW1lYb867wLPIOJr_HgjGQgVwOLmIWIPGOwR3PFai9U1fQYYn7yL2xYSZ7J8C2tSjer89aNcgJpn0dH6PKmRgiQgyK9L_aIA7mAegbzApmDvUraiuUIwz6mIbxL7vUHzPrB3oXo3nOSbfvIOih0A3hJgII44CSOfM-TibRo39uzv7pYeLTYmAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
🇳🇵
🇨🇳
ویدیو اختصاصی جدیدی که توسط نیویورک تایمز به دست آمده و تأیید شده است، واضح‌ترین تصویر از ریزش کوه لانگتانگ لیرونگ در ۲۶ آگوست را که باعث سیل فاجعه‌بار نپال-تبت شد، ارائه می‌دهد.
کوهنوردان قبل از اینکه یخ، سنگ و آوار به دره فرو بروند و ابری از گرد و غبار عظیم را به هوا بلند کنند، صدای ترک بزرگی را شنیدند.
فیلم دیگری، آوارهایی را که بلافاصله پس از ریزش به سمت پایین تپه حرکت می‌کنند، به تصویر می‌کشد - آغاز فاجعه‌ای که جوامع پایین‌دست را ویران خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70782" target="_blank">📅 11:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70780">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ABIFMo8zNFs2LJEd3LqvQybefWE8quz34oIoDy8bDuvp1UZtMc6XoCb3ARbpY0SqczxcoWw0Nh0fwFB4DdAvqnjl-JPMoEHqsCE969_fGQpWoOclVoI9XfUWa48bPrMWqLE24k3AkiygkzKA6LUO99kmHwtG6lRCRCtvQ3qZwXxpfJhE-5S-fADbNkLPyKzqfREsud7sq32pQjYpweyA0y1WH3h7lLG8pV5eH6OZ8_HkuwdYrGo-1gWIbkmhm_LXZiBxVwWsgpEh2MW3Gwjd_da0PjUWp0XRIu0LTXbSpcsZeM4cBJHYXE-rbKcFr6uBe6LraWmdIjTsY_odHAqgFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k-2tf1ERKMDVSZQA2-K1alZFNx1X3G-VHC2bWm8jvvOOpWmsLSmGisP5ZBwWMbBix84FAZpVB1kD67-JzRPBfMT1gCEKHT4MkUY8c3bP1WIS9ch9us9vb81i8x0QGkvjLz5Gxm30dm73lYcudeUkTAGrKsJYUvsc3PaTIerOZomEN1ZpwvhQ9cMiCgo-flm6tOFiSS6bkJ3j7UGdC2k4zvmksLRwfSpudMosll1jZmzMPoulplI9SyRGUHgcIkyuwnhqReTE3yt2F5gWoSuSLd7Rn3RKXY0Zag4g1x0o7-ony70eFt_sZNJGHhxMY7n5QouSUEFsHRMzc02PhlnjQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
استوری یوسف، پسر مسعود پزشکیان:
مسائل رو ناموسی نکنید که هیچکس نتونه درباره‌اش حرف بزنه!
اگه تو غنی‌سازی منفعت داریم، دنبال کنیم و اگه نداریم، متوقفش کنیم.
اگه تو داشتن توان موشکی و پهپادی منافع داریم، دنبال کنیم و اگه نداریم، دست برداریم.
اگه بریم سمت هسته‌ای، دیگه فقط آمریکا و اسرائیل نمیان سراغ‌مون و اونوقت یه اجماع جهانی علیه ایران شکل می‌گیره.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70780" target="_blank">📅 10:32 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
