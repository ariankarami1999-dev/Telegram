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
<img src="https://cdn4.telesco.pe/file/AE87toM8i7I9Ik1m3PaE6sNXKVe3IRgfBmbi12Bb4NiikBVO8P3-lUz3eKg4XT15Ou3140QyTohdD_np1ZuiaGpf5-ljR30M9-N-nPwN2Pjlmb42z3JogbkAM8cvdQLziDvBZmim1rYzk5umJp4UQZJtmwWQ2M0pdxQLEdOD7mgojhHtKTyde_zUXWeeGRkIYjBCcsTfwODpJkk0Z3a4T5-sUVRegbcSKF9Z2RG0G7IcBp3YH4voAytJO8Vjjmc6_6ynvy6VXyEuusMso3AjmKOKWZBywJXFLUojiU0ngNNUI3sCHghz5U4Xu0tFmk9tbyxHCMoXRPyZDGim97q_2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 13:45:33</div>
<hr>

<div class="tg-post" id="msg-66861">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=GS_o9lYqhihINSJvMvIgyBWS4DwOSq1UhsGVIqwzfC9_RmbAv3MKuKFC3dJs78MHMCr70ZcqnKS0n5s-QEBI-tR-DuAaRjws5oYQ-MPPvPgWYMRLQGDdnGFhcV123feI2qaNfF7i4BxkUlEoMlzs52j4SuxmHWPDLJqt2SQjaZ8KIy5Wv2bL5ptHHXGTx35r7kczO_elgvoyXWv_lX-drzmEMxTNQyy8YA8y1pR3kM083Wm4PswRITlkdNzCmcNKU_2yRBF9nMsWfnqiJKYIehNfz4IioqjQF93tG3jP47SuSsGjl7PFWonkRTcuJUQedzUmpDE50mSC0XYCrdQvsA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=GS_o9lYqhihINSJvMvIgyBWS4DwOSq1UhsGVIqwzfC9_RmbAv3MKuKFC3dJs78MHMCr70ZcqnKS0n5s-QEBI-tR-DuAaRjws5oYQ-MPPvPgWYMRLQGDdnGFhcV123feI2qaNfF7i4BxkUlEoMlzs52j4SuxmHWPDLJqt2SQjaZ8KIy5Wv2bL5ptHHXGTx35r7kczO_elgvoyXWv_lX-drzmEMxTNQyy8YA8y1pR3kM083Wm4PswRITlkdNzCmcNKU_2yRBF9nMsWfnqiJKYIehNfz4IioqjQF93tG3jP47SuSsGjl7PFWonkRTcuJUQedzUmpDE50mSC0XYCrdQvsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مراسمای محرم، شیر تعزیه افتاده بود دنبال یکی از لشکریان یزید، که یه لحظه جلوش رو ندید
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/news_hut/66861" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66860">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
قرارگاه مرکزی خاتم الانبیا:
🔴
پرواز هواپیماهای نظامی اسرائیل در نزدیکی حریم هوایی ایران یک تهدید مستقیم محسوب می‌شود و اگر ایالات متحده اسرائیل را مهار نکند، ایران این تهدیدها را تحمل نخواهد کرد و حق پاسخ را برای خود محفوظ می‌داند
@News_Hut</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/news_hut/66860" target="_blank">📅 13:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66857">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oo9oZVqERXKjmwXTpesSOcxfIK3aYviuAMHyDSiybq3cAD88M8EkFNjBou2OEMxQgawpJETCZBi_KOYPFCUkXYojrWD2Qz_wfk0gQat4aRY97uS5XuTmg_ZcD-QbXX1GmjEgu8INxsMgo-bu-CSy2CM1jdLhSh00Mano3jbR9X158m7A3nM9emv05alybIA524LNRuJlxjBJytZijWS2odW4x_H4Y3epDDyvISN-kS1PdlrtMnT0m-kuLQgFbHKvoIAEpxafc6xiQZqXZVL5iJLi1tRc-zW__3I4-CbYo9AGHC_TKO57IVccZasJG6s2buhPzzfNZ5mGcJDoRZTouQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7GizzHGf8hvvaBAEApqeqCRlR2ZJeOgigwCWvJutssSZOSOlhWJxBZiVfC4fDfjSVAGrbBEEruiVAgHvqtphLpqv6YlxmYIqeC-H51h7KaQQ2hq7lIto07jji0ukbnYh4MxxeZSS-dLMz1vTPnZHyjMpMZCDgfF37-ASghRIinvQE9mgB2AlhiAPLyVUEOLvieZ_bE7k8TZ8i9qOBlvn7iEsEtxFHMRsrlxwHkvR-Br4dhoFQ1ZvPs_8mjfF2ekIGILwJdG-_yW2l3UfasHw0AMuAEhXDmJNPYY-FuJQtQIM3YdRdbPAfKDOMzxcZkIh4_2absD8FCF58KiajXuWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/URih0d8VX1o8K7N46CIbvO4OH4PgK9l9tpn6x4kZnELTLrvpbM3SC7kCoOYfLBc4RcXDUyATDbcvmxFJ0W4rJE1j29p5pyQ2Om_WUcWplPjKx4uJyyYc7WuAiUmb4KbY4WMEFsvvJKxErARC9jAbaNewRqXOR0QUOw-HB8MU66oqaqNWEtRceD-K4yg_CaumXlUUuf-Mp0zGuZ_KAIfeRWrXXYDtyFXCdGAvf9m_EbiirsDVNhEg7idDTBPLtYEOleFiq0Y_Sk6aCg4pRoaE96SB-wV44GavelJHFLLJqsu2Z-XiNUCc2IRb1Q9rR_Sm0YBPq-q0HHsdvzc5zqjsPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
حملات هوایی صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/news_hut/66857" target="_blank">📅 12:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66856">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=lAf6jOf4_85WDzYRyCrMHBCu2m79MxePKfOgxW_aXTUIagQ59yQlIHxyUtH7HPdSKFEdXd6w8bvEpTBwBNfepmeIwIJu_W7C9YfxdilaXn53IvHpJiYz00lyIQYRUVofRj33c-S18WBcHuVfQokzPjC-8IYFqtUdC5xtAdKLejdfxVRvTgiJpwqBEjtjIKvlcVvvGLJRlBSij8V2wFaEKmUwl6m77EtdYEYIHvq-g0NG0dy4Ape5D-eUO_U8rDwRdZOwqUxUhFqPenibKKoMaJIHly34Qx6CpLedBH2MuJKGeBq7J_LoVLc-hXn_RAxMc4LIWBaqBhIXsa7wv0JpHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=lAf6jOf4_85WDzYRyCrMHBCu2m79MxePKfOgxW_aXTUIagQ59yQlIHxyUtH7HPdSKFEdXd6w8bvEpTBwBNfepmeIwIJu_W7C9YfxdilaXn53IvHpJiYz00lyIQYRUVofRj33c-S18WBcHuVfQokzPjC-8IYFqtUdC5xtAdKLejdfxVRvTgiJpwqBEjtjIKvlcVvvGLJRlBSij8V2wFaEKmUwl6m77EtdYEYIHvq-g0NG0dy4Ape5D-eUO_U8rDwRdZOwqUxUhFqPenibKKoMaJIHly34Qx6CpLedBH2MuJKGeBq7J_LoVLc-hXn_RAxMc4LIWBaqBhIXsa7wv0JpHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
«یک بازار جدید دیگر هم در راه داریم و آن، کشور دوست‌داشتنی ایران است.
ایران کشور زیبایی است. کسی دوست دارد به آنجا برود؟ جمهوری اسلامی ایران با مشکل تأمین مواد غذایی روبه‌رو است و ما قرار است بخشی از پول آن‌ها را بگیریم و آن را خرج کنیم. همچنین قرار است مقدار زیادی گندم، سویا و ذرت خریداری کنیم و این روند به‌زودی آغاز خواهد شد.
این برنامه هم بسیار بزرگ خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/news_hut/66856" target="_blank">📅 12:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66855">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daTywHm-ItI3_atB5Lc7sXyrTsp12sdNA6f-hQnbWUC8KNXQcfsrAQ9Rv1drS6AgOYBHI3wjyTIOtCZ-xruIFykqDfRNaam2u0c0f9ODvF8nXkQ9ssB85LyqtpGryyn4sz2i4Fwj3KlboFOq3qVA95fDN3_g1sm1arMMBJ5xDqFqYnDALo7ycURL7AQ_wBYX71-O9TvRiVN3hiGVpwWwK84ydQHqbM-O9okQ97YopEXUuiN-2nYcv5kc4x6Mk_jwNshSiUZ2r4AYVFVfy2vTtxLod6FNU3Ta4YQxN9WJenRdT9LDOE6TTQ5Jy_Hs5wbjAsdlEg1YdjM4cExmQCf3Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ:
روند خرید محصولات کشاورزی ایران از ما خیلی زود آغاز خواهد شد و من انتظار دارم که حجم آن بسیار زیاد باشد.
ما پول ایران رو گرفتیم و بجاش ذرت و سویا خودمان را دادیم!
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/66855" target="_blank">📅 11:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66854">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‼️
جی‌دی ونس درمورد ایران:
🔴
آن‌ها دائماً سعی دارند مأموریتی که دونالد ترامپ برای ما تعیین کرده است را تغییر دهند.
🔴
او در ابتدا چه گفت؟ «من می‌خواهم ارتش متعارف آن‌ها را نابود کنم. من می‌خواهم توانایی آن‌ها برای اعمال قدرت را از بین ببرم. و من می‌خواهم تضمین کنم که هرگز سلاح هسته‌ای نداشته باشند.»
🔴
آنچه دیده‌ام این است که برخی افراد سعی می‌کنند بگویند: «خب، این عالی است، اما شما باید هدف متفاوتی داشته باشید.»
🔴
به نظر من دلیل موفقیت رئیس‌جمهور این است که او از تسلیم شدن در برابر آن تمایل خودداری می‌کند.
🔴
او می‌گوید: «ما کاری را که قصد انجامش را داشتیم انجام دادیم. ما اهرم‌های دیپلماتیک، اقتصادی و نظامی باورنکردنی ایجاد کردیم. بیایید از این اهرم‌ها برای کسب پیروزی بزرگ‌تری برای مردم آمریکا استفاده کنیم.»
🔴
این همان چیزی است که او از ما خواسته است انجام دهیم. هنوز تمام نشده، اما تا اینجا همه چیز خوب پیش رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/66854" target="_blank">📅 10:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66853">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=mvPEUuA9R4oRc96JqMWkU_qpS-ynxrR_MZnrkMBzD3WnQ1uxmxuQlUW4CEumcUpIjTdSrsj-v7HBn5IKsO9VlYUtuwhqvKcKHl-nAf-B58kdkj29yZNiHgqspGGdey8yG1rnOxXje3c2budLH90gOw1qP9AoicpqEbq-dLB0gzDemAUDinYmZFxjyGf-LQhZY-lkNV79tBAVLSL3nkmz6ysN5zmNbqDVUBisGN-69wWJyM_5ToKIYk5-Wrge4otK5yzYfoPC9LSDXkXLv2i4_zzCSiAbt44cKArgu_7bcdfEvXRonTRz8ZKpxMoxq-WBW6K-nMz5bbWR60Esz7m24g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=mvPEUuA9R4oRc96JqMWkU_qpS-ynxrR_MZnrkMBzD3WnQ1uxmxuQlUW4CEumcUpIjTdSrsj-v7HBn5IKsO9VlYUtuwhqvKcKHl-nAf-B58kdkj29yZNiHgqspGGdey8yG1rnOxXje3c2budLH90gOw1qP9AoicpqEbq-dLB0gzDemAUDinYmZFxjyGf-LQhZY-lkNV79tBAVLSL3nkmz6ysN5zmNbqDVUBisGN-69wWJyM_5ToKIYk5-Wrge4otK5yzYfoPC9LSDXkXLv2i4_zzCSiAbt44cKArgu_7bcdfEvXRonTRz8ZKpxMoxq-WBW6K-nMz5bbWR60Esz7m24g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎯
ارتش اسرائیل: ۶ عضو حزب‌الله را در جنوب لبنان ترور کردیم!
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/66853" target="_blank">📅 10:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66851">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=Y-EIPrhAOrrlgNiZ7X8luJukKlcxFv7fVLhYcV4Ghi1mU5s42s8OvvDLW4c_tj9Tk24WvobqEmAHuAOqGBaBbZBqMMD41zKUW5AVRb5wRdZKby56sWKrMxDWqIBwYMS6k0Fk1EwfYL_09Fdx-aUOR26PiExAWkLQY7Z3pmtzXo6JU2VHl-0AT8M2NgN3OD_JBDhg_TgOaiAFcD0pTJxboRSF-rqWLWX-WkQVqJTDSPsqzO5rwVGeOgScfNqM55-wEviuxHY3I8S1VP6a06qFMucK-zL4pQZyLEU0MfpWpUnJ5BHF4MI0sGy7WcZ7gFmuat_NyBAJjWfQgu97bkbl6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=Y-EIPrhAOrrlgNiZ7X8luJukKlcxFv7fVLhYcV4Ghi1mU5s42s8OvvDLW4c_tj9Tk24WvobqEmAHuAOqGBaBbZBqMMD41zKUW5AVRb5wRdZKby56sWKrMxDWqIBwYMS6k0Fk1EwfYL_09Fdx-aUOR26PiExAWkLQY7Z3pmtzXo6JU2VHl-0AT8M2NgN3OD_JBDhg_TgOaiAFcD0pTJxboRSF-rqWLWX-WkQVqJTDSPsqzO5rwVGeOgScfNqM55-wEviuxHY3I8S1VP6a06qFMucK-zL4pQZyLEU0MfpWpUnJ5BHF4MI0sGy7WcZ7gFmuat_NyBAJjWfQgu97bkbl6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با روسری و ماسک اومده بوده هیئت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/66851" target="_blank">📅 09:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66850">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=E0JeZChsoT9J-jZlUqztweGxfySIm2AJlWHzvE3zr6X8FG5RnK-NuIBT8LYhIhtREFerYuEyZjG1vD65276fCS057y7e9W2KmSMDEXT62r70574E89Ii0_gyXUH7C6gqOEcFjnNOTg0rO2XxHu_LrfPoc8d0JLoKLeixFrQcgjQ7TN53Mnxde_NfXDOdZRfaiDtqEMpLaRpOWGyZHsdpznRF-mbASh32GSKy-fHzSYJRuq-Jxs_L2rl9eMfKrUr19peczuP8Y4hpug7RpoMIituWbguaMaN53TEee8W_uuSA4a_Q9EbMqggAp8o-YBdnEjRflMG1ibMBIL-azYc9Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=E0JeZChsoT9J-jZlUqztweGxfySIm2AJlWHzvE3zr6X8FG5RnK-NuIBT8LYhIhtREFerYuEyZjG1vD65276fCS057y7e9W2KmSMDEXT62r70574E89Ii0_gyXUH7C6gqOEcFjnNOTg0rO2XxHu_LrfPoc8d0JLoKLeixFrQcgjQ7TN53Mnxde_NfXDOdZRfaiDtqEMpLaRpOWGyZHsdpznRF-mbASh32GSKy-fHzSYJRuq-Jxs_L2rl9eMfKrUr19peczuP8Y4hpug7RpoMIituWbguaMaN53TEee8W_uuSA4a_Q9EbMqggAp8o-YBdnEjRflMG1ibMBIL-azYc9Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرماندهی مرکزی ایالات متحده:
جت‌های جنگنده اف-۳۵ بر روی ناو هواپیمابر یو‌اس‌اس تریپولی  (LHA 7)، ناو پرچمدار گروه آماده آبی-خاکی تریپولی/یگان سی و یکم اعزامی تفنگداران دریایی، در حال برخاستن و فرود هستند. ملوانان و تفنگداران دریایی ایالات متحده در دریای عرب در حال عملیات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/66850" target="_blank">📅 09:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66849">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال @Palang_Bet شو چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی @Palang_Bet     @Palang_Bet</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/66849" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66848">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNl1hpjsh1osc3qEo1IY9vTdgMt1lrsl9k7XNpOGYeYNcE9etLSX4-6FXacAycEooQZ8zjfNwrXwaeFo_H_goln9xD-5_jA5PSBV2-MwRipLB4qzWx0Okz1NjOmp96WgL6XayYIKQuBqRekkf_mL7eaQtiVl7wqjgyqjQ4_BEMBiAwPqKdRKcc86mZpfZHq7PJ_oniNed4KiygC8XH1yzMZsYfxXfSrl-SoWOpeaVdEtT1okbQtgzaYq_BNj4lHpT1-nwGnYIqixBHqpSWNLQ46FrdY2klwqNfLLQIDpLRt0jr3Q7qGpcuvxqYgJxuvhc4elzl6X-Fgf6hH-Z7Bpwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
@Palang_Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
@Palang_Bet
@Palang_Bet</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/66848" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66847">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFodfH1BHMEeLUV-gksrkOwWv90cafYgEer2CSI_7_-ESLtNepEXYAi0Bor2TlW1tqeBar5_MWNWf_rRLK4gMGOeYmuEvl1WRQ4uCFVKoL1WcmYDCiK2Y7kHnQI7ZifrOmbPIEKo3j40ltCe8fYbcu0O0h2yfvC6dJ2ePVUXh3XSqOAnBI9qVOAJzdxS49xptvs_N9kBTxPSrPsm1bNvmr3UHolhzOKouIBt8gfbXMj0wIa0p8eYGlyh5o7QbWnp9DuKZA84MsTkTUzR9Moru-_14xh8pLaSFTliWO9Ut8NDVZUqwnPFi3FDMJll1W-eHxRbNg9l3jadud5r5v7arQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏بر اساس گزارش وال‌استریت ژورنال (WSJ):
🔴
ایران روز پنج‌شنبه به یک کشتی باری با پرچم سنگاپور در تنگه هرمز حمله کرد؛ اقدامی که به‌عنوان آزمونی برای توافق هفته گذشته میان آمریکا و ایران جهت بازگشایی این مسیر حیاتی کشتیرانی تلقی می‌شود.
این حمله به پل فرماندهی کشتی آسیب زد، اما هیچ تلفات جانی در پی نداشت.
این حادثه چند ساعت پس از آن رخ داد که ایران به کشتی‌ها هشدار داده بود از مسیرهایی که مورد تأییدش نیست استفاده نکنند
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66847" target="_blank">📅 01:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66846">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رسانه های اسرائیلی اعلام کردند طی درگیری ارتش اسرائیل و نیروهای حزب الله در منطقه بیت یاحون در جنوب لبنان چند نفر از سربازان ارتش اسرائیل از تیپ ۷۶۹ مجروح شده و با بالگرد از منطقه تخلیه شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66846" target="_blank">📅 00:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66845">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">با بحرانی تر شدن وضعیت ونزوئلا و مفقود شدن بیش از پنجاه هزار نفر گویا به نظر می‌رسد مثل زلزله سال ۲۰۱۰ هائیتی که ایالات متحده آمریکا به این کشور نیروی امدادی/نظامی ارسال کرد دولت ترامپ هم به سمت همچین سناریویی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66845" target="_blank">📅 00:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66844">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
وقتی نت ملی بود ، تنها سرویسی که برامون قطع نشد همین بود
🔥
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66844" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66843">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHFLEHf8y9mg00my4rHF8Q-JTPMcF6taitL4U3WX5zOOSd8UgsEXP_WyRl4Qb0dKgg0WzhT82NeXrpBYJoOY0R1KtF39Zjvcv2k9p6SujCkpobVa5V343mpGLcxUL8YH5JXY5N9OQ9XnK5dBaGJw_hBQcjFEnBEtCQIsvZAOV_R0xsqJEuN6tPfsAIxSy7e_N0SmIYk92gthex5Ss_CqGkreGlTruuIfQayRuBlUzSCEyJEwJcXcpVaMOeHEZP9M7ntIZT-N5LssSXRsv-dQSiBbNoYRS5LbstwnpElf5ljgsR6-dp5fluLcJOIBND2ujMmEWTDbsyfE1M12SlTH9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
کانفینگ نامحدود برای همه اپراتورها
🔥
⚡
سرعت بالا | بدون قطعی | تحویل آنی
💵
یک‌ماهه: 380
❗️
پشتیبانی 24 ساعته واقعی
❗️
✅
سازگار با تمام خطوط
🚀
اگه سرعت مهمه، همین الان پیام بده
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66843" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66842">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CS-fH3qzGeFuZItzovKGlFk23q_0vh4wbwAU6oSoGWqg2c1z1J_g5Y6N3hKgfvQlLEqnBBVxHLi5jCR6_vADQGbJLYnrXXXjrca4E1QTVYCWAHm179PBxQNSwfAsX5HuOAxbCRFYeKUaImC_YqE5evDETrmOQInxWvLX2GACHZ3wxzpa0cSG0hl9U7cx47THTgc31m4vkwwEUcKmZts-ET4eF85uwXHh0lhrUaR8bVgAl9ya3kInpbWyRXImJG-Epe33hnMzkDa-E2T7MUMR2sbDNnFMfQPBLoxiYbYiezThlEmIfEuLxPydMLC25mzVKLnt1FjClL0IP3PqiyJ_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش از لبنان: جت‌های اسرائیلی به بیت یانون در جنوب لبنان حمله کردند.
این پس از تهدید امروز سپاه پاسداران علیه اسرائیل صورت می‌گیرد
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66842" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66841">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=JLALEFAEuJy3pWqRgagiHGzoVUTNJJe4Dq-GCeQg7NwaSHSMj03J9mo1HrrxxXs0kHT1JXfGExh2Rd4ISlafwVqCTfr7TXKtMku3thnlITfDRino0lD9nS8OSAfWO2PvjCWolP9NXy89yG9n1VW_JLr3FPIX0usIG_6wjYCOxcBLKaAhPN_Lpp5TYph4uPD5e-x8ufy0Q2eIEk6_8mTz0Ti_RxWpdAjP47QhR8hg3A0shcSQnjBFws490IWdpciMxTJxbpchu-kkttXn3G12v8od0EeBFhn-BfVHiDnzkNpLhfIR9t_VS3t3zwWbvPSA0bgv14WAW78TJRWhZe3bbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=JLALEFAEuJy3pWqRgagiHGzoVUTNJJe4Dq-GCeQg7NwaSHSMj03J9mo1HrrxxXs0kHT1JXfGExh2Rd4ISlafwVqCTfr7TXKtMku3thnlITfDRino0lD9nS8OSAfWO2PvjCWolP9NXy89yG9n1VW_JLr3FPIX0usIG_6wjYCOxcBLKaAhPN_Lpp5TYph4uPD5e-x8ufy0Q2eIEk6_8mTz0Ti_RxWpdAjP47QhR8hg3A0shcSQnjBFws490IWdpciMxTJxbpchu-kkttXn3G12v8od0EeBFhn-BfVHiDnzkNpLhfIR9t_VS3t3zwWbvPSA0bgv14WAW78TJRWhZe3bbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
«شما قبلاً آن‌ها را «دیوانه‌های دین‌سالار مذهبی» می‌نامیدید. آیا هنوز هم فکر می‌کنید این توصیف دربارهٔ رهبری کنونی هم صدق می‌کند؟»
🔴
مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ببینید، موضوع این نیست که من باور دارم این‌طور است؛ واقعیت همین است. نظام ایران توسط روحانیون، یعنی روحانیون تندرو، اداره می‌شود. همیشه هم همین بوده است... البته در بخش‌های سیاسی حکومتشان هم افرادی هستند که ظاهراً انعطاف‌پذیرترند یا تمایل بیشتری برای همکاری با ما دارند. ما در حال مذاکره با همان افراد هستیم. باید ببینیم نتیجه چه خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66841" target="_blank">📅 00:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66840">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/345e633380.mp4?token=bjmCyKpod0FvrEZTqNqs7gBTpPlzQ4ACvFsD3gC7e3iIMcAfg4kf96tOf3eDB_oDn3uQYQRPxQ_8c1XiLZ4BeTiH-EQTh3u0qy2W0riBkGOTfGKj8QoEOEZja-OfXg53rZNkhUQlQOp1VjM6SPQKctqsWRZU_lm3x9d0zoKpCTPzyrKNg4b6GQLXI-WEv8iucFPEfqQgvTxNGoXofdfnDtWAiJlnbWcGLFe3DkDbCtqE8yn2w_A8SUUlcWJ5BsvhNr6gQrdYAyn3yRgSc4KPhSLjEQpZcLwq4xzZF6ZvOJtk3KeFRE-np0ERcqIPcRo9i5iupaNH4Mh_63NGW0Tpmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/345e633380.mp4?token=bjmCyKpod0FvrEZTqNqs7gBTpPlzQ4ACvFsD3gC7e3iIMcAfg4kf96tOf3eDB_oDn3uQYQRPxQ_8c1XiLZ4BeTiH-EQTh3u0qy2W0riBkGOTfGKj8QoEOEZja-OfXg53rZNkhUQlQOp1VjM6SPQKctqsWRZU_lm3x9d0zoKpCTPzyrKNg4b6GQLXI-WEv8iucFPEfqQgvTxNGoXofdfnDtWAiJlnbWcGLFe3DkDbCtqE8yn2w_A8SUUlcWJ5BsvhNr6gQrdYAyn3yRgSc4KPhSLjEQpZcLwq4xzZF6ZvOJtk3KeFRE-np0ERcqIPcRo9i5iupaNH4Mh_63NGW0Tpmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری:‏بهای بسیار سنگینی.
رئیس‌جمهور ترامپ این جنگ را آغاز کرد،
و وعده‌های بزرگی دربارهٔ تغییر رژیم داد
و وعده‌های بزرگی به مردم ایران داد.
آیا ازنحوه‌ای که آن را به پایان رسانده،ناامید شده‌اید؟
شاهزاده رضا پهلوی:خب، نمی‌دانم هنوز تمام شده یا نه.چون همان‌طور که می‌دانید، هر چند ساعت یک‌بار ما یک توییت متفاوت از این
رئیس‌جمهور دریافت می‌کنیم و ناگهان موضع
از یک چیز به چیز دیگر تغییر می‌کند.
بنابراین من خیلی به هیچ اظهارنظری
که مطرح شده، وزن نمی‌دهم.
و در واقع، من فقط، می‌دانید،
کمی دنبال می‌کردم که
در به‌صورت زنده چه می‌گذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66840" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66839">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">#فوتبال جام جهانی فوتبال
📊
2 گل آلمان و ساحل عاج  کد:YXA6P ضریب:2.3
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
دانلود برنامه ملبت @Palang_bet</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66839" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66838">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=EadIj45nYFyBHcPkfVnQmVwRbROMKHZlNhLTa0r_CFjgnG61Buxz2Otw6bobUhNcX0U94hmF7Lnd-a8V105z-y-wXsac_y_gn7-Jbmkdxg5pIbbnd2C0IBxIbCwQ11u_dX_KQnOAi9uFg8WBqxhgaP5d8bZ16TS5BkoaKVdUpIn2bZ_MpDcxMXTbDt3DAiEXoIp31AdgaKkDklVcjaY25udT8JO5BrDmXTQK3NLU42oTP6FOsrwPv-4A9RrwuLeTQIwLuorBoWSCkDeUV28gH7GWFr4FJzEWn0MVjuMDTOoLjVP8WyKxT75cPmFHGbVGisHt81GVy9FsCGOj2lKHNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=EadIj45nYFyBHcPkfVnQmVwRbROMKHZlNhLTa0r_CFjgnG61Buxz2Otw6bobUhNcX0U94hmF7Lnd-a8V105z-y-wXsac_y_gn7-Jbmkdxg5pIbbnd2C0IBxIbCwQ11u_dX_KQnOAi9uFg8WBqxhgaP5d8bZ16TS5BkoaKVdUpIn2bZ_MpDcxMXTbDt3DAiEXoIp31AdgaKkDklVcjaY25udT8JO5BrDmXTQK3NLU42oTP6FOsrwPv-4A9RrwuLeTQIwLuorBoWSCkDeUV28gH7GWFr4FJzEWn0MVjuMDTOoLjVP8WyKxT75cPmFHGbVGisHt81GVy9FsCGOj2lKHNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مفقود شدن بیش از ۲۱ هزار نفر در پی زلزله‌های ویرانگر ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66838" target="_blank">📅 23:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66837">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFm06uSYg6159Puts4R1f_fpEhfqXtoJ7eyjgLVjtnMxjCLgrh9Lb-btuuY3_h-vV6xwg7H75UQSxhg_2dAuKDJbgb_seP1ty53gdBFDuY0mGyWxIxZs8fM0K1XGHSfJmaS5Sja1UimKL-chjGK1RkRXWkx197oI9cAl8xQ5WzG-a27Y-BBcwW7s01gOKlZpRHiJp08NJ1zljPzQ9E21hAag39Y2bjgb65f6VU6XfivzUmA5YyIQEpm781NvGvs3CbBOHOGV_nQcxLd_5dRXqDV0yrFuA6RPWy1Zm-LItURLndxvGmD88GxL09x55nvbD7pXZxljl72xUGtO84A8ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
پس از بیانیه مشترک اخیر در مسقط، تماس تلفنی سازنده‌ای با وزیر امور خارجه عمان داشتیم. ما مجدداً تأکید کردیم که ایران و عمان «برای تعریف مدیریت آینده و خدمات دریایی در تنگه هرمز» گفتگو خواهند کرد. ما مصمم هستیم و این کار را با همسایگان خود انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66837" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66836">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=oSmrcDH3bi__OqeZLupTGPKauVojLwNvDZn0_AncEwRo6JSMe5TqDC53UKXvQWc1zHzMWiGLe_0TRQL-0-0GrKELQT71uRTgxFOA42BcH6rBGa-Wx3Khpz31EhWjWYX2UWpMNfmI019aA5rb3VDt69ZPs2hqx_GWqi9-fAd2b_4GreaOiT4E6mq-x4WQ1WNSMi_xNQYE9WIsUe46FRD3RJIHCVfsvlTNVAvyacZHSchnIcXD-kzfSmynuLzEwENgXQ_zarPJKBwMTAzsVNB6JpNy8-l_KNlWOmxHSWVHYiGWQJCU0WaZZiZUN2mjldOAk_dPTYLwHuhvm7qrsV4bLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=oSmrcDH3bi__OqeZLupTGPKauVojLwNvDZn0_AncEwRo6JSMe5TqDC53UKXvQWc1zHzMWiGLe_0TRQL-0-0GrKELQT71uRTgxFOA42BcH6rBGa-Wx3Khpz31EhWjWYX2UWpMNfmI019aA5rb3VDt69ZPs2hqx_GWqi9-fAd2b_4GreaOiT4E6mq-x4WQ1WNSMi_xNQYE9WIsUe46FRD3RJIHCVfsvlTNVAvyacZHSchnIcXD-kzfSmynuLzEwENgXQ_zarPJKBwMTAzsVNB6JpNy8-l_KNlWOmxHSWVHYiGWQJCU0WaZZiZUN2mjldOAk_dPTYLwHuhvm7qrsV4bLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
روبیو درباره ایران:
ما می‌دانیم افرادی که هنوز در بالاترین سطوح آن حکومت حضور دارند، همان کسانی هستند که به همان ایدئولوژی و همان طرز فکری پایبندند که رهبران پیشین آن حکومت به آن باور داشتند.
نظام ایران همچنان توسط روحانیون تندرو رهبری می‌شود.
همیشه همین‌طور بوده و همچنان نیز همین‌طور است
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66836" target="_blank">📅 22:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66835">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=BRuj3x6ARAPp7zMP_wB_A2tiW6YjGhacu3xqvC4RHpT3vBChRpXlxD1x8Zub29qPRnynPdDc7a9l6nkqZvz95e4xTaidxRkaAQ2VNkab8ThvVEYJ_ZdPYWR2ObyYP2Ud57H2SUvjNORJuZbJsyS_DNmYaR46DiBIlVMEGBswaxNr20KU7GbTLfRZPb2az0vIwTOLJGUZ6ZpU0ZutICh187e0L0dQwQv4hXmidb4KPII4cmh9qAUc9j72N7jy51c0ysqlMYn48-Zx9foYFRWtuoP8CpEg0lyZSGnhHziUapvSQaPp0x8Xwq79f5LWElnkcgCxtAjMewkHKLtFVSxaAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=BRuj3x6ARAPp7zMP_wB_A2tiW6YjGhacu3xqvC4RHpT3vBChRpXlxD1x8Zub29qPRnynPdDc7a9l6nkqZvz95e4xTaidxRkaAQ2VNkab8ThvVEYJ_ZdPYWR2ObyYP2Ud57H2SUvjNORJuZbJsyS_DNmYaR46DiBIlVMEGBswaxNr20KU7GbTLfRZPb2az0vIwTOLJGUZ6ZpU0ZutICh187e0L0dQwQv4hXmidb4KPII4cmh9qAUc9j72N7jy51c0ysqlMYn48-Zx9foYFRWtuoP8CpEg0lyZSGnhHziUapvSQaPp0x8Xwq79f5LWElnkcgCxtAjMewkHKLtFVSxaAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
نمی‌شود برای امام حسین اشک بریزیم اما در جامعه شاهد ظلم، بی‌عدالتی، فقر باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66835" target="_blank">📅 21:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66834">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dm2dEeQh4y_skKjM6wcngDG1C3Sx3amBxupjkJggt70mQz3C87wPfFs2uBumnrMEGbRuvXSoN7l_wKJ1PU41F58xvHafyb0PYsPGQPcD1RFcWZBfCOXRw6vRMd8vElH5wVAwVu6ZXHQx32_ALO7IDQEnqDSC2oaX5l7YwgFbBLKhDkOis7vq34m75r-OirT2OXXG_KqQdXTPzRPNiMAkpOKl-U9PR5nWMaXwoCGH2yCsRXslap9HAqDxlFw7Tuv5UEML0MIm1GV18hpgkVRLDmP3Hl1sNCKPe-gYXLMU3y9VBcxKw9skFnOMhX6pf75rbqwn0Lg7ZasgrBYON-WtvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه پایانی نشست مشترک شورای همکاری خلیج‌فارس و آمریکا:
🔴
تاکید بر اهمیت بازگشایی تنگه هرمز بدون محدودیت و بدون اخذ عوارض عبور.
🔴
تاکید این که هر گونه تجارت یا سرمایه گذاری با ایران باید به انجام تعهدات آن به موجب توافق منوط شود.
🔴
تاکید بر لزوم خلع سلاح همه گروه های مسلح در غزه.
🔴
تاکید بر ادامه حمایت از دولت سوریه در بازگرداندن خدمات، فراهم کردن زمینه های بازگشت داوطلبانه پناهندگان سوری و مبارزه با تروریسم.
🔴
مذاکرات لبنان نباید به نتایج دیگر نزاع ها مشروط شود
🔴
حملات متجاوزانه گروه های شبه نظامی مورد حمایت ایران در عراق علیه کشورهای خلیجی محکوم شده و از تلاش های دولت عراق برای حصر سلاح در اختیار دولت این کشور اعلام حمایت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66834" target="_blank">📅 21:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66833">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/965348f417.mp4?token=CH7x9TwX3aIKYg8M10Weplll_oP2qMI_f30n8chzeCwlRDMEVtwdiDl0PTk0kGNQB_IijCujLlDt-lCAhHjIEUVtjRCjrjsvz_asOLWnOEA8EUhnr-uiKqBl3finE_VZ4kNxapAt3MMaP48iJn3Qbifgy-wd237_CNPXjhgEM42Mrdc6C-wGB0-l0YhpqqOhh9yy1nTiJdlutoBR_TXNBfu6y26CCPm7Na-VwER1A-e2rn2AZ07GM6yCtYVDjQT8y5kpeZN6SqpBe4Jyp84SAqvVl4nh6tSuL8lc97BAGxcg4vj_TURENcaG6MdNrLil8JK0pU1Flks8PAPHBgV5ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/965348f417.mp4?token=CH7x9TwX3aIKYg8M10Weplll_oP2qMI_f30n8chzeCwlRDMEVtwdiDl0PTk0kGNQB_IijCujLlDt-lCAhHjIEUVtjRCjrjsvz_asOLWnOEA8EUhnr-uiKqBl3finE_VZ4kNxapAt3MMaP48iJn3Qbifgy-wd237_CNPXjhgEM42Mrdc6C-wGB0-l0YhpqqOhh9yy1nTiJdlutoBR_TXNBfu6y26CCPm7Na-VwER1A-e2rn2AZ07GM6yCtYVDjQT8y5kpeZN6SqpBe4Jyp84SAqvVl4nh6tSuL8lc97BAGxcg4vj_TURENcaG6MdNrLil8JK0pU1Flks8PAPHBgV5ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
فقط یک آدم کور می‌گوید هیچ دستاوردی وجود ندارد. دستاوردهای عظیمی وجود دارد.
من همه آنها را فهرست نکرده‌ام چون می‌خواهم شما را نجات دهم. شما اینجا زیر آفتاب سوزان ایستاده‌اید - فهرست کردن همه آنها زمان بسیار زیادی می‌برد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66833" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66832">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0J4m7ZtyuWxj8PMAdFOSR21Y1e--yjrgtV_VEOMLZ6qxTxYN5MlqAzXoOnbZrtySATY2ekmgbquDGE31pz64zZQ1xH2G-jqptmLaQiQN3PPygLUQok7LD3YcywAtGpw7KYsosoE4CPpu_CCnwtFpWB8AW0Q5WrON4eUlXwCjz-rHdOPI3j5S8F9c3vKESup1wQLxZycCgszD0ACYlB3fmTtAxspMTmYHNZg6Ak52evG6xW9K6XJzN3yl5b_h1uoTqJh4yaukfFNswRKvKcV50dATNvUraOAZ-HCIky6p_MojGgF3EOP2NYtzT300yIqW7se2FYyspVnkjTNFONvMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
با نهایت تاسف از وقوع زلزله در ونزوئلا. مراتب تسلیت خود را به دولت و مردم ونزوئلا، به ویژه خانواده‌های قربانیان، ابراز می‌داریم و برای مجروحان آرزوی بهبودی سریع داریم. جمهوری اسلامی ایران با مردم ونزوئلا ابراز همبستگی می‌کند و آماده ارائه کمک‌های کامل است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66832" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66831">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">این آمار فقط مال روز اول جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو پلنگ بت جویین شو بهت آموزش میدم چطور پول دربیاری و تا اخر جام جهانی سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet @palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66831" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66830">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwJmv_LX_PH9Wt5x7I4FtLznHpbeW0mQpU8A-Thzfpwvl4keth9dMp2KGYVg7bffiry4hc_2jKo87G1vCOKts-TOKaa9GoO0VKgpZUUkPDvNB48DTmlcmDuyvtUpGBFhW4shZvkgR0rfaxjQ3V6c9R8P0elnphSLiCKXc3I0xI40JwnUxuOqfmiWRft5g7V0hxEIFdjHEHuwVzrSRyJmaJur8dlKRQxTFoooPWf1dK_PlCpt095GH2N0zHZC_EwvQo8FlFyQsRkbEr8z8cvgsaSJqGz4xshfMIfm2y1wHVG0O0Xro-D8OocGd7pChNWDuwfJLwAQvMwi4V9ZsvCYyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66830" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66829">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=vR5IPMukM5gtvdY78U7RFsyeeMmhBkW7KaMLumD-gxqI1fCuJHpWr7SX_zHMIMI7mdjh8ffcKg_jf53VRlRk_5waV-7eFqxOOQlUmRvGLTsF7Td2GNAFfbBYFTEx8XlqHmMT7miK1D-KSPcj-Ql5S51A_GZEWwfz_Tfi1oHrWP3KMbEEQUNlCp65FTUE6V5kd6s6wCIkxy1K1XaMPN79TKNTFvfAv1jt2JmsfJ4McUa4bIOFhoTOHwdwVunBXhc74wbbpNp_zLp9tF0SlBqkMvw5G2pReQO0-f2ifT8ZNRsV_Gn3MKp34Gad9k8uiT5at4bLtkb1HAAXXyqK6juBnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=vR5IPMukM5gtvdY78U7RFsyeeMmhBkW7KaMLumD-gxqI1fCuJHpWr7SX_zHMIMI7mdjh8ffcKg_jf53VRlRk_5waV-7eFqxOOQlUmRvGLTsF7Td2GNAFfbBYFTEx8XlqHmMT7miK1D-KSPcj-Ql5S51A_GZEWwfz_Tfi1oHrWP3KMbEEQUNlCp65FTUE6V5kd6s6wCIkxy1K1XaMPN79TKNTFvfAv1jt2JmsfJ4McUa4bIOFhoTOHwdwVunBXhc74wbbpNp_zLp9tF0SlBqkMvw5G2pReQO0-f2ifT8ZNRsV_Gn3MKp34Gad9k8uiT5at4bLtkb1HAAXXyqK6juBnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
من ادعا نمی‌کنم که پیامبر هستم.
اما فکر می‌کنم می‌دانم چه چیزی بقا را در منطقهٔ ما ـ و به‌طور فزاینده در سراسر جهان ـ تعیین می‌کند:
قوی‌ها زنده می‌مانند.
برای ضعیف‌ها جایی وجود ندارد.
آن‌ها طعمه می‌شوند.
و از میان می‌روند
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66829" target="_blank">📅 20:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66828">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=O4QCZlwpXNBXUd2JP3gWj4stwj-hhQdVK8_llI9vVFen0x7nQrlgGZEXJk-symLbTSEGwOqic1zP3Pt-_ulIZACbKpE43Peq9E64VizSStMFehQEgevzrU2yZJ6lfc53X6Jefp_BACz-z1byjaFF1_2qtmJ8e3jwXzPBDrNtuDMFkmsJhWevUXUVcRcWEC1IL0jiWX0OvSIvEpY3KfvbPpYcWBwCaAQIgTHrDumw-Qo2bpgXIobPgXjttKdglc2p9tz2GEImtRkoldA_781EoSJF3UWAs0NtqxG4Bw6ERg9DuNPQIm9LCGHXQixLn49M2OZ39IggzlhnhCcVROM2xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=O4QCZlwpXNBXUd2JP3gWj4stwj-hhQdVK8_llI9vVFen0x7nQrlgGZEXJk-symLbTSEGwOqic1zP3Pt-_ulIZACbKpE43Peq9E64VizSStMFehQEgevzrU2yZJ6lfc53X6Jefp_BACz-z1byjaFF1_2qtmJ8e3jwXzPBDrNtuDMFkmsJhWevUXUVcRcWEC1IL0jiWX0OvSIvEpY3KfvbPpYcWBwCaAQIgTHrDumw-Qo2bpgXIobPgXjttKdglc2p9tz2GEImtRkoldA_781EoSJF3UWAs0NtqxG4Bw6ERg9DuNPQIm9LCGHXQixLn49M2OZ39IggzlhnhCcVROM2xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بنیامین نتانیاهو: در مورد رژیم ایران، من فقط یک چیز خواهم گفت: با توافق یا بدون توافق، تا زمانی که من نخست‌وزیر اسرائیل هستم، ایران هرگز سلاح هسته‌ای نخواهد داشت. به هیچ وجه اجازه نخواهیم داد ایران بمب‌های هسته‌ای توسعه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/66828" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66827">
<div class="tg-post-header">📌 پیام #69</div>
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
پشتیبانی 24 ساعته  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66827" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66826">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N44UMwe8q28-Q-74uWtaP9m5w__GCj3Ww9kHgjiIC3AkfJ7CyxAl4HIRuAnEcRiRUBug1HDGlLLeCzlUlk6AV-PS595ZR-GZWDKzN-NjXwBVl_d4OUO4nDg-2VB2b4324kI0Z9MJpUH_6anTjhEoJMsqJEYIAsPpIZ1Za2jeYih8tJ1DkK5xjpLEV0ZMC1VTfXz_YYU7fDK_YD8f718NDWN3-muN4ZZ3xdXto2fcdiC8LFVkqz_nboxKeX24dp5MowKHIm7mgyzRL9PgFrXFm7Wg4igr7zhjwRNfReqQBUyOS7hFlvO5owzjlkoNxr_BCxfuMDumMlU8imPW6F9F7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66826" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66824">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO9aANO2Rp94H8_pHpOZD1OWzEquun0J1w1KPfUkLywkaOM2ad9Z5BfC-rHcLCwc8kgvNMSGESoraTu6vIyTNZ3uteyA-POYR5EbghfQtD_k1VpgK-AeIngy9U12aRAJzdodlpMSLr7pYdVsLQ9aru9E7CwcIPYtEDawqoFbTNjEMBZJTUU_l_2XjReMGnI6RAmJMHqxpACdwbVdoZObedPN2ypUzV4A0Rq3PLv97ULb3ixi8S4qkE2Z0Yyz2ZfuUiue7Q-bXX1p2Ohb-62gw6JZHF4Rv-C3uqnLiBksZxJiq1kYcuO_g82RHW_Cp7R1v_eRNNXdCbYFqnlGgPZWQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=fDlCVhdwwJakdI0qt23JHOP17ZKO4_QDgaxWYAKllzSDjUCn4yuAXJWVVBLhWhioqDXVLiZ6MFKi8ONMiIxQV_v8_NwUgHyvBH0uXLlGtAbks_4rroLi3A6KlMDVMyXJBbXbYrLC1-eZR2lH731vbPz9c9Ty5n1wXdoBGQCqFgI0V_3I4fyuAU33ZQONebllJvkHo0ROdV1kjwzS_vs0J2ZxqPtLmTF_DnFw4jz3R0y_LqDLIXo6bNVNoU-8BTn1145vVygZWKfj2tQeZ5U9UQBC78TMamfMZVPA8Yet1pqw-PSZUdQoCxG_k0IH6VPpCwC5Ao4Y64F8KUe8QfK6lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=fDlCVhdwwJakdI0qt23JHOP17ZKO4_QDgaxWYAKllzSDjUCn4yuAXJWVVBLhWhioqDXVLiZ6MFKi8ONMiIxQV_v8_NwUgHyvBH0uXLlGtAbks_4rroLi3A6KlMDVMyXJBbXbYrLC1-eZR2lH731vbPz9c9Ty5n1wXdoBGQCqFgI0V_3I4fyuAU33ZQONebllJvkHo0ROdV1kjwzS_vs0J2ZxqPtLmTF_DnFw4jz3R0y_LqDLIXo6bNVNoU-8BTn1145vVygZWKfj2tQeZ5U9UQBC78TMamfMZVPA8Yet1pqw-PSZUdQoCxG_k0IH6VPpCwC5Ao4Y64F8KUe8QfK6lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فستیوال محرم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66824" target="_blank">📅 19:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66823">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=UsBpEaMyDCTCDtrZDLoHtEuNRKLPnzErlz4oji0z4tPlBb3hYqaPY07VQFWmLiWUzwUCUA-W9AxoX7ZvioHQN8pbiDsiPW78Y_XHt3Lm5QVr3o4t6wMiDR20toPGtF5u1klrCgsstidVXwu5aTtPNXC8bf0wRnfH9fTG_B_EVzI66y9FSKxFBg5e1FXrSwgkY-cMiY87ILRp9En1sAKng4KVuEyPWkrBaX7MY6OvGnTwPmE5hfopB8WxIae2ESsR3JNdbnl7kOJOG1mFU-EdRLs98_Fw67Z5ddyCKDein0oG1m-Z4PTepEVpnSPgg0BvGJLV73x9Wal4X22ySAXpmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=UsBpEaMyDCTCDtrZDLoHtEuNRKLPnzErlz4oji0z4tPlBb3hYqaPY07VQFWmLiWUzwUCUA-W9AxoX7ZvioHQN8pbiDsiPW78Y_XHt3Lm5QVr3o4t6wMiDR20toPGtF5u1klrCgsstidVXwu5aTtPNXC8bf0wRnfH9fTG_B_EVzI66y9FSKxFBg5e1FXrSwgkY-cMiY87ILRp9En1sAKng4KVuEyPWkrBaX7MY6OvGnTwPmE5hfopB8WxIae2ESsR3JNdbnl7kOJOG1mFU-EdRLs98_Fw67Z5ddyCKDein0oG1m-Z4PTepEVpnSPgg0BvGJLV73x9Wal4X22ySAXpmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف پاسخ مجری صدا و سیما رو داد
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66823" target="_blank">📅 18:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66822">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0453856b46.mp4?token=J7uWg2SH8lrpIpAkMbkoxcD-9GP32YGDHGVBReZ8do1fvg7mZQrlnKYLEs5zeywbZBw4vr-qKQVzGuhW4PViaket8Px8xKHTwJlGZgFJ0w0FMqaipwtbSSRgOrqf5A5hqB0bPu1HFY52GVQNOkcSF8MEMqX-OKlb9Jy0-xIeUIMzZJyJyBqYdJgHxksUFZT_n3Ryi5RFEiXyJu_x1_5ppX_7cQev_U6s7dhYjo_bJKomFFj4CRE9XZAwA29yeTT3-KQjNobpyRBB4-DcoYJOMKAIfhnuOQTuLok9VwylRn0jsMd2Fos1IBFlDyqiZWlghgYiywk2MiXrFZCdkyvtKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0453856b46.mp4?token=J7uWg2SH8lrpIpAkMbkoxcD-9GP32YGDHGVBReZ8do1fvg7mZQrlnKYLEs5zeywbZBw4vr-qKQVzGuhW4PViaket8Px8xKHTwJlGZgFJ0w0FMqaipwtbSSRgOrqf5A5hqB0bPu1HFY52GVQNOkcSF8MEMqX-OKlb9Jy0-xIeUIMzZJyJyBqYdJgHxksUFZT_n3Ryi5RFEiXyJu_x1_5ppX_7cQev_U6s7dhYjo_bJKomFFj4CRE9XZAwA29yeTT3-KQjNobpyRBB4-DcoYJOMKAIfhnuOQTuLok9VwylRn0jsMd2Fos1IBFlDyqiZWlghgYiywk2MiXrFZCdkyvtKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
اگر کشتی‌ها در حال حرکت باشند، واکنش ما هم بر همان اساس خواهد بود.
اما اگر کشتی‌ها حرکت نکنند، این نقض توافق محسوب می‌شود و در آن صورت با یک مشکل جدی روبه‌رو خواهیم شد
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66822" target="_blank">📅 17:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66821">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50938460f0.mp4?token=i7qWMzA2gdXFZOJ0RUtdPlmlyvJCaND5_8ZDH0x22fVcr9ijWtRK2LC2UN6YYmeQDrnI-3bbgLzCx1Vk7TJhGlRyorox4rACP3uSokT-wL1L78ytg6LIhkbGWM5dDApbnfMa-s5FrOoKUEm-pd4fcFIvcupaq1EUWFNUtHQ4ZxJLUeYbJn4UP4qvZ0Vu-c6f4aDnqid8ENWmxSNh67jz8O_mKYJnoFVSQtzTwjyJXOozLyM0xv1BX2TDa2uv6Muf2Fy8PR4u7_OgXoVTNoNGQ6Xyjl_mFZrLvhh8iE8mgogDt_WdbfX9wFD4br2Ajv7BWiPr9N0Wb2isJMybHSKpRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50938460f0.mp4?token=i7qWMzA2gdXFZOJ0RUtdPlmlyvJCaND5_8ZDH0x22fVcr9ijWtRK2LC2UN6YYmeQDrnI-3bbgLzCx1Vk7TJhGlRyorox4rACP3uSokT-wL1L78ytg6LIhkbGWM5dDApbnfMa-s5FrOoKUEm-pd4fcFIvcupaq1EUWFNUtHQ4ZxJLUeYbJn4UP4qvZ0Vu-c6f4aDnqid8ENWmxSNh67jz8O_mKYJnoFVSQtzTwjyJXOozLyM0xv1BX2TDa2uv6Muf2Fy8PR4u7_OgXoVTNoNGQ6Xyjl_mFZrLvhh8iE8mgogDt_WdbfX9wFD4br2Ajv7BWiPr9N0Wb2isJMybHSKpRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
فرض کنیم که ما کاملاً دیوانه شده‌ایم و عقل‌مان را کاملاً از دست داده‌ایم و تصمیم گرفته‌ایم با ایجاد یک سیستم عوارض یا دریافت هزینه موافقت کنیم.
این قرار است چطور کار کند؟ اصلاً شدنی نیست. چون اگر کسی هزینه را نپردازد، چه اتفاقی می‌افتد؟
فرض کنید یک کشتی بگوید: “من این هزینه را نمی‌پردازم.” این مثل عوارضی یک جاده نیست که بعداً یک قبض جریمه برایش ارسال شود. به آن شلیک می‌کنند.
اگر به یک کشتی شلیک شود یا یک کشتی غرق شود، دیگر هیچ کشتی دیگری حرکت نخواهد کرد.
بنابراین چنین سیستمی نه‌تنها غیرعاقلانه است، بلکه اصلاً نمی‌تواند اتفاق بیفتد.
حتی قابل اجرا هم نیست. پس بهتر است همین حالا این خیال‌پردازی را کنار بگذارید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66821" target="_blank">📅 17:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66820">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJ6praqAha_MBkP65yUkrEm0NDEHf-w-hwTOqXynpVQWId-ECFXV0LLaYegWfNVSHUDWkxJRYEHj7N8gFukJ4u2MBFOYhko2b0UZMQaqZi2YlWkjP4vG0ctFbIubsWBHZwX70UglUX-kibrLuh_QK42Q729HP4vKsrrbkRrUpxEa3AcpcJFH4SMxVIKs8LmtgzIcqnrydAlFxL4l5UjqakNWUVdniOYUxdrPlvnruESood_klGSO3Lfw6QnocfOiKQiGsNdLLvfGGfbrMcCp8vW2UAYS-tBp9dh9bYq56pukMeYmeG1HmtRZgDsC3zAdENd1sHjT6nzbWXmQ0N_Cjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
آمریکا به دروغ ادعا می‌کند که دارایی‌های آزاد شده ما، کشاورزی آنها را می‌خرد. جالب است. تنها محصولی که ما برداشت می‌کنیم همان چیزی است که شما کاشتید: دهه‌ها بی‌اعتمادی. این محصول ارگانیک، فراوان و تولید داخل است. اما ظاهراً ایالات متحده فقط سویای تراریخته، وعده‌های عمل نشده و حرف‌های بی‌اساس صادر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66820" target="_blank">📅 17:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66819">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477cde7837.mp4?token=jh_jiZAGx0grdWvEHb7QUEEUWsl9bEnFUdBZFyv4zkcr23xgXtM3EG3Z-7MRQiCV58gW95GFTBHuj4X7CBCjP92a5RMVwRLGWx-LVIZkTbz7R_EAA-xr_xg_mT1Wt7y3t3tz7mXJKQamo4wMDVrK60BrtaXbmjzuVeywgcqTUhfeBRPuLt57JtunjHMaC4Fb55SIj1SwyepNf8YGolCRIRaycsb_jrHtGrAFoGLPx9R1ySKn0sBSN4UhONyMwOQIaViJs4mCwJm-gNGSNb548KjAlJzMJSOHZfacY0iGbujrD85aOo4IhG_ZyI0hoorXTdhTpvjkw0seSLclOSyDyjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477cde7837.mp4?token=jh_jiZAGx0grdWvEHb7QUEEUWsl9bEnFUdBZFyv4zkcr23xgXtM3EG3Z-7MRQiCV58gW95GFTBHuj4X7CBCjP92a5RMVwRLGWx-LVIZkTbz7R_EAA-xr_xg_mT1Wt7y3t3tz7mXJKQamo4wMDVrK60BrtaXbmjzuVeywgcqTUhfeBRPuLt57JtunjHMaC4Fb55SIj1SwyepNf8YGolCRIRaycsb_jrHtGrAFoGLPx9R1ySKn0sBSN4UhONyMwOQIaViJs4mCwJm-gNGSNb548KjAlJzMJSOHZfacY0iGbujrD85aOo4IhG_ZyI0hoorXTdhTpvjkw0seSLclOSyDyjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویرانی‌های بر جای مانده از زلزله مهیب ونزوئلا در شهر کاراکاس
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66819" target="_blank">📅 17:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66818">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K30xs3ZTn23nz0dITGwVfHrF8RqJPQiEmvRPou8SMslr9ukPTeWUpsAWuq0_k8VnMdm6PN1E5Hy6LKvy8pORRi2IJIJiqqHDvT9gFWIALQRl4UARH8n4k3KrDsVtF9TdQLyv01QDnZUUNQAyPEm5fNX4BE6jA7TD0BxoQLgHIIpFQ87UfK4_BfkC8lcFpByV7lcWbd5CVMlQOFa0QC25bp2QNGLqFUfx8IK81PfBpS5m-XNWzQoTH2RHAatVAWVQR2gSlzcegOuukbJmVV7zdGfb9dHNcinjfpDO8s2-A8O5P7H7rJ6aF-Hrh3PHQaVnvbhwwUaNTLqvTWrjWhV_vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل قاآنی فرمانده نیروی قدس سپاه پاسداران:
اگر اسرائیل امروز داوطلبانه از جنوب لبنان عقب‌نشینی نکند، فردا مجبور به فرار با تحقیر و شکست خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66818" target="_blank">📅 16:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66817">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=cEq7FKT7yvdPFdoL-tuMYmZHGfGBww2bLMCleOH73Bs0aPTG5rPzX8ZjC-Qp0-PMPq98B8N89c7LgDc9gkrK7D3E46QGpmf9_FsWOMGs-7rKr4wxTgMXiin69s1nm2zf6xvLPznVirlrdpbS7TQ_EZ6Y2vpS16YtwkuACPMdDfI9iKxIngdMkbrxJuGEcCIKAh_Hvm-XKjAWJys6BC3i-5cl5bvaQ9JEwntTPLbMZxlHqRSMIH3wOeEw_kbjXZIMdAoj41_EuxhjlWPVQIPM1qORUWU8ayQnebowCTqMLj5EZhPOvnpIDDg6ZPQH47LSIrjk0UOGAOWk971nBWawXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=cEq7FKT7yvdPFdoL-tuMYmZHGfGBww2bLMCleOH73Bs0aPTG5rPzX8ZjC-Qp0-PMPq98B8N89c7LgDc9gkrK7D3E46QGpmf9_FsWOMGs-7rKr4wxTgMXiin69s1nm2zf6xvLPznVirlrdpbS7TQ_EZ6Y2vpS16YtwkuACPMdDfI9iKxIngdMkbrxJuGEcCIKAh_Hvm-XKjAWJys6BC3i-5cl5bvaQ9JEwntTPLbMZxlHqRSMIH3wOeEw_kbjXZIMdAoj41_EuxhjlWPVQIPM1qORUWU8ayQnebowCTqMLj5EZhPOvnpIDDg6ZPQH47LSIrjk0UOGAOWk971nBWawXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
نیروی دریایی سپاه:
تنها کشتی هایی که از تهران مجوز دریافت کرده اند حق عبور از تنگه هرمز را دارند و با هر شناوری که از این دستور تبعیت نکند برخورد خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66817" target="_blank">📅 16:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66816">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyQWQv9t956qB7_sADt_7LGEO7autf7AcXedklp61k_mNfuTEtXBnVx6ZGwUg84bs6BYuWxYcg9liLj_IAReEOWCOv8buGt4hQtIjr1t9r1U-_d11SzlEtPBrIxN7BJolPSlvkpziY5sqKbO_EV6DgBshg517G2_ooAn0ZL5Yp4O1h9M5oDxyjQu2J2OKi4eu8pyA4gn5Ks56fQTbt2qNopi5jb2tm-sfLWVerq9T0NyYRp8xlNVhtgTN0LijzT7enzhfEbkx2f1mpLjPzhdADDCe2A6I1xwmHtT5hlfo5gFfWCT17PWecsNwMdrAVmLldM3d0_rvmYmkXZJ0NevCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت
ترامپ در تروث سوشال:
«شگفت‌انگیز! سنا رای خود درباره ایران را از ۵۰ در برابر ۴۸ مخالف، به ۵۰ در برابر ۴۷ موافق تغییر داد. رند پال و بیل کسیدی رای خود را تغییر دادند. از جان تون، لیندزی گراهام، برنی مورنو و همه سپاسگزارم. این رای به ایران هشدار می‌دهد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66816" target="_blank">📅 15:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66815">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
خبرگزاری رسمی عمان:
وزیر خارجه عمان اعلام کرد ترتیبات آینده برای تنگه هرمز شامل دریافت عوارض از کشتی‌های عبوری نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66815" target="_blank">📅 14:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66814">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=IwUopvKACKhCiBFn736r3u8zuGJ1ZFX2Yqkpm7GtO4x8A8cWaty8hVMTl1VF7zYo0f2VYCAyySTDs2FVbUoh5Ofmx5T9FbH5C6xxTUzFbMH0j01Tx2H8hAvVgjJRvrs7UZTaFxUB1NuXH4Xns14ncW0VMpFCbKk80k8AU3KpYxqQ-f_RWCfEZ8OTjUM-nv1KWabFNxLls82Zva6D4N3wyNsqCwYIJrFtLdJ-UWaP6RF0QBW8mA9I7vzSHKurtutpvbjZT9tx4_Jvfc0h21tLyIyE6RElzOoSEXgxysTCb-tvxs6GznHQgeFRbqkHE-CDEcpwfPNhu3Nrhynhc3gcIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=IwUopvKACKhCiBFn736r3u8zuGJ1ZFX2Yqkpm7GtO4x8A8cWaty8hVMTl1VF7zYo0f2VYCAyySTDs2FVbUoh5Ofmx5T9FbH5C6xxTUzFbMH0j01Tx2H8hAvVgjJRvrs7UZTaFxUB1NuXH4Xns14ncW0VMpFCbKk80k8AU3KpYxqQ-f_RWCfEZ8OTjUM-nv1KWabFNxLls82Zva6D4N3wyNsqCwYIJrFtLdJ-UWaP6RF0QBW8mA9I7vzSHKurtutpvbjZT9tx4_Jvfc0h21tLyIyE6RElzOoSEXgxysTCb-tvxs6GznHQgeFRbqkHE-CDEcpwfPNhu3Nrhynhc3gcIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره اردوغان:
🔴
او دوست من است و از جنگ دور ماند.
می‌دانید، او یکی از اصلی‌ترین گزینه‌ها برای ورود به جنگ با ایران بود.
شاید هم در طرف ایران، چون همان‌طور که می‌دانید، او طرفدار  اسرائیل نیست.
و من از او خواستم که وارد جنگ نشود. او هم وارد نشد
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66814" target="_blank">📅 14:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66813">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YL4zRlLMw-NoW7Z_chXkQiHRKXwrDeKkS_95GPUwA3mGEl1IzqFstZUvqMc7AOkI1HMMzqMNJ7AKPUcp616OPeOz5pbqK5IUV_8j0gY66ppBTE3ZxWeJsMxM01aJm5Puhen3sTarpxkxmZsGMFutUoFlc1WmtVDh22i4utoWUOsSUxHGmTtEW7lz5VDygagRhGyiuJZDEsPjWUfc77Vh797ivsTOuTBILfTHFs2c9CweLCIgJg9teKKUvQi5-CxiCc8HJOl__jAl5NS8gy1BDvLPpZi1wlMtUNgdkHTeDkDkvhjFC-UvM2dhbiwFrOSGelf4vcOuzyu5QTsfqWQ1GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو:
🔴
واشینگتن خواهان توافق با رژیم  جمهوری اسلامی است، اما نه به هر قیمتی.  هر توافقی باید واقعی، قابل راستی آزمایی و همراه با پایبندی کامل به تعهدات باشد. اگر رژیم جمهوری اسلامی به جای صدور ایدئولوژی بر رفاه مردم ایران تمرکز کند، آمریکا و شرکایش آماده همکاری خواهند بود، اما انتخاب مسیر کنونی نتیجه مثبتی نخواهد داشت. هیچ توافقی نباید امنیت، ثبات و شکوفایی شرکای آمریکا در منطقه خلیج فارس را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66813" target="_blank">📅 14:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66812">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=ckNNQinrkqo1PGRBgC9-avfDg1JAIeU8ldggS51f5Pp1GnS1Gkyr6tC4zBjXTU5ib4COfBWc2mkuYNMmeGN2LXVk1Ow5AoV3tu22IHih0HOt2n-o-L0DGjgLq1Bwns3_wAVl0Pv8VDi3M0IxOjCvS-8a30NTfsR-EX9m28ROtUk2cAzGyHQI1fPy53dJifzTPy_eKT2gMqr4DpHkzpvmbSeP7Pv2vNbxSz3nB2ChAIGHg_cQASZPNRDz1QSkgcVdd5Gqpx3LNOU_YBiDU7gCmi57gJBqe83yQrtPQAchJYRTbg6uL3q-fr2ztMuxNVbLCRWkivL6_-SsmE4RS6VeFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=ckNNQinrkqo1PGRBgC9-avfDg1JAIeU8ldggS51f5Pp1GnS1Gkyr6tC4zBjXTU5ib4COfBWc2mkuYNMmeGN2LXVk1Ow5AoV3tu22IHih0HOt2n-o-L0DGjgLq1Bwns3_wAVl0Pv8VDi3M0IxOjCvS-8a30NTfsR-EX9m28ROtUk2cAzGyHQI1fPy53dJifzTPy_eKT2gMqr4DpHkzpvmbSeP7Pv2vNbxSz3nB2ChAIGHg_cQASZPNRDz1QSkgcVdd5Gqpx3LNOU_YBiDU7gCmi57gJBqe83yQrtPQAchJYRTbg6uL3q-fr2ztMuxNVbLCRWkivL6_-SsmE4RS6VeFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حتی در کیس بیماری هم عجیبیم
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66812" target="_blank">📅 14:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66811">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=eeCri0-svgEwM0NN6QXC_d_31mrMmCE70LDuMWoZnbzlil1Q6_P6WAoXjVbW7sOCD3EQwhOp-97LJwlvL4BZRlYrTDnKNkTR_0tFtPzjw1pEhCBSZJmK4kdHdX1gCZz0smYnPQ3j4xEYWUm5P54yC2lPuHAAPak_Nkcc5xm1THIWuoJ6HdL0K6_5hhi4f-VEv8jHsKvqpyGkDGnxxQMdUoTQZYM7GF4vB3tmfVqRGCRdksOyt8ZDpWDfVPiCvPo2sR6j5sSY3TlDfRdEfoLS2Q9vLM8AKrn65araa6GqJA2Avmg60xfE5qBaJE2OObUakP-1diWpTVAv43TaZjJvpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=eeCri0-svgEwM0NN6QXC_d_31mrMmCE70LDuMWoZnbzlil1Q6_P6WAoXjVbW7sOCD3EQwhOp-97LJwlvL4BZRlYrTDnKNkTR_0tFtPzjw1pEhCBSZJmK4kdHdX1gCZz0smYnPQ3j4xEYWUm5P54yC2lPuHAAPak_Nkcc5xm1THIWuoJ6HdL0K6_5hhi4f-VEv8jHsKvqpyGkDGnxxQMdUoTQZYM7GF4vB3tmfVqRGCRdksOyt8ZDpWDfVPiCvPo2sR6j5sSY3TlDfRdEfoLS2Q9vLM8AKrn65araa6GqJA2Avmg60xfE5qBaJE2OObUakP-1diWpTVAv43TaZjJvpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود ۷۰کشتی در ۳۶ساعت گذشته از تنگه هرمز عبور کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66811" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66810">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.2 MB</div>
</div>
<a href="https://t.me/news_hut/66810" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
نسخه آپدیت شده اپلیکیشن ملبت
🔶
• لینک سایت مخصوص کاربران خارجیMELBET:
🌐
t.me/ConnectMELBET
🔶
• آدرس سایتMELBET
🌐
bitly.uk/connectmelbet
🟠
نکته: اپلیکیشن بدون فیلترشکن کار میکنه برای ورود به سایت باید سرور فیلترشکنتون رو کشور های اسیایی یا کانادا یا ترکیه تنظیم کنید</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66810" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66809">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-WXpQ4AqSuRL296hKpHenFzlX3OvpzYUg3D9sU8A1pRAXN2pQnjyXsUctHMLRd8P2KJFMHWX1b-ZbP-bk4waFk-eMHbh27OW3NF7Ff4WuUTrSswGHfdYPX-x4xU2ENou6mytskF7XX9P-hBR31pXG5Q1T0umnR8FcvOPVrcDE8758MBgPU_grAgEwyCaGo_KOx5z-MrgqFve4df80fm3fP-aubDQeZf0WbkB6ueZhUuEeVS6iLm5djZuErWvGfsRJcjXMWzyG7i5mL60HyNHQtFhWvD-4eNgYhC-UkC4FF8sfchW75uL07w5NP_oR_jr14w1u3BCPZux18sLxSIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بهترین سایت برای بت زدن سایت MELBET هست که مورد تایید ماست و خودمونم چندین ساله توش بت میزنیم
💸
با اولین واریز اگر با کد هدیه
ml_459049
ثبت نام کنید تا سقف 100 دلار 130% بیشتر شارژ میشید
واستون لینک و اپلیکیشن ملبت رو میزارم که ثبت نام کنید
🌐
https://refpa3665.com/L?tag=d_3312431m_45415c_&site=3312431&ad=45415</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66809" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66808">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=FJFeYKtGKZ4Y8j2TpcGsJx1NiADoGTsnENT4-HbLuaVk2E9mOrPhd0FhQnAhBHK10F7kP2UoRyFvHIKl4Xni4wEiN32BS9xm3thgmm3f3OVGyQJwrSMhrSNFxcFA7B3pK7XmzHvI19i2N7oNvnUzvnahLHG9vNsFVfTMH-w4w_puKapoImBO6WYOgzj6ORTfPQGE67KulJBcWyvIOlVlhmw-h5wWvuL-Ku8Us7gFo2UmVKoE9D9yzKKD1tzRwBIU3E8sJGTfa8Uq72OOB1CeljppjA2KRT1xWRqn0UYo9kNB0wl_CQCrvj4cbxPbT5H9d0-HeWGP5C7Wm_vGpaDiBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=FJFeYKtGKZ4Y8j2TpcGsJx1NiADoGTsnENT4-HbLuaVk2E9mOrPhd0FhQnAhBHK10F7kP2UoRyFvHIKl4Xni4wEiN32BS9xm3thgmm3f3OVGyQJwrSMhrSNFxcFA7B3pK7XmzHvI19i2N7oNvnUzvnahLHG9vNsFVfTMH-w4w_puKapoImBO6WYOgzj6ORTfPQGE67KulJBcWyvIOlVlhmw-h5wWvuL-Ku8Us7gFo2UmVKoE9D9yzKKD1tzRwBIU3E8sJGTfa8Uq72OOB1CeljppjA2KRT1xWRqn0UYo9kNB0wl_CQCrvj4cbxPbT5H9d0-HeWGP5C7Wm_vGpaDiBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
بسیجی‌های صادراتی دیشب تو میشیگان آمریکا نذری بین آمریکایی‌ها پخش کردن
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66808" target="_blank">📅 13:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66807">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=MINJmZKt5r173NWkXH1vXQcmJ7oQhyzNesklbhpEdfPegupZgFU0AzWh5QYs-rjcevIPZ2CM3cQQqck83ydm2_BB3ZFYXw8I3_LrTYjpnsm0fhaSRt3L7eG2dcqtsWh8_dSLnK6Wy2Tp5TcUtkVUOFCy6tHCXMV3Uplj04U7BVnJ4SbzZIMflTIOMdVh1jVe-sdyT3vfcWmc2maLBuuw8wlIaOQ7PYmguq8UwpB1QbFkPJfJs8OA4e4TDAK8GNnKs04wA96DIOz6_4ikr8gEv570N8AXtkd4VldL8Cxdz-FhcuR7zCWIfYY45vrc8Ef3x3bfo6X2YZCIphCkPl4_Noi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=MINJmZKt5r173NWkXH1vXQcmJ7oQhyzNesklbhpEdfPegupZgFU0AzWh5QYs-rjcevIPZ2CM3cQQqck83ydm2_BB3ZFYXw8I3_LrTYjpnsm0fhaSRt3L7eG2dcqtsWh8_dSLnK6Wy2Tp5TcUtkVUOFCy6tHCXMV3Uplj04U7BVnJ4SbzZIMflTIOMdVh1jVe-sdyT3vfcWmc2maLBuuw8wlIaOQ7PYmguq8UwpB1QbFkPJfJs8OA4e4TDAK8GNnKs04wA96DIOz6_4ikr8gEv570N8AXtkd4VldL8Cxdz-FhcuR7zCWIfYY45vrc8Ef3x3bfo6X2YZCIphCkPl4_Noi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنوز تو این دوره و عصر مدرن یه سری کسخل وجود دارن که با عقاید عصر حجر خودشونو بگا میدن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66807" target="_blank">📅 13:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66806">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=jsP-a0FaJrP9Sd081EAtdqLlsJeRQYU0dD-U-pw-on5WFTxj5FWQ6AIO0PVkUyG1b4VbRQH8HKABfpknNbpCLbSH_TSNTdV6ZZJlGKT2IyRYMWzIHlykJSSmmgiBQj-l4FWB8EnELy8YBzomVsNAJso23IrBUrtKZvEc6VV74vlR_C64cgGRtYj6HPi8Me2AfMr44iE_7-OkBM-XOaRzFv2AiMIQhMXHvSXzYLME3jP6lEU5rBs9ceCsrg0OhrbnsEXhwKtO7sg8r1c2iWMi82vEr8MuQg2skFdG5JNcVu_nylJY_iEbw10Zk_3e2-dx-xNbiXgkjfgfqv0b4-lsEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=jsP-a0FaJrP9Sd081EAtdqLlsJeRQYU0dD-U-pw-on5WFTxj5FWQ6AIO0PVkUyG1b4VbRQH8HKABfpknNbpCLbSH_TSNTdV6ZZJlGKT2IyRYMWzIHlykJSSmmgiBQj-l4FWB8EnELy8YBzomVsNAJso23IrBUrtKZvEc6VV74vlR_C64cgGRtYj6HPi8Me2AfMr44iE_7-OkBM-XOaRzFv2AiMIQhMXHvSXzYLME3jP6lEU5rBs9ceCsrg0OhrbnsEXhwKtO7sg8r1c2iWMi82vEr8MuQg2skFdG5JNcVu_nylJY_iEbw10Zk_3e2-dx-xNbiXgkjfgfqv0b4-lsEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرستو نظام با کلی عمل زیبایی که البته هرچیزی شد بجز زیبا: قلب من با امام حسینه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66806" target="_blank">📅 12:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66805">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f836563943.mp4?token=meHc4rZABhFHx9IgpYST5Iai-cJWDPR_rI_gV7HnZQ3N1h9Nn2YhM_qqAIV82gGEm8HcvNIJfqWXqzaSXSRdY1UB0OtiuBzIhgNAAdJjehjOhD8k67AXR56VTzyD4jDyHbxPmL4w91ftUe_wHilRpzNDdNsjjOeIz1MZODiaIsQgENZzcriufnYiZTI8PxFjg6Tdo1RVuxlaBaeVnsyvGKVDVSawi5y6Z6-MJs7sb1b8-NWsz-sqSciRO_ADTBdOydka6hHuSDo4aF0uWF5my6Q-wk88UiNZH8vynuxScasINqg2UbBu7NAH7lgtjuMQHCgySfZIYyQDfyjwp7CfKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f836563943.mp4?token=meHc4rZABhFHx9IgpYST5Iai-cJWDPR_rI_gV7HnZQ3N1h9Nn2YhM_qqAIV82gGEm8HcvNIJfqWXqzaSXSRdY1UB0OtiuBzIhgNAAdJjehjOhD8k67AXR56VTzyD4jDyHbxPmL4w91ftUe_wHilRpzNDdNsjjOeIz1MZODiaIsQgENZzcriufnYiZTI8PxFjg6Tdo1RVuxlaBaeVnsyvGKVDVSawi5y6Z6-MJs7sb1b8-NWsz-sqSciRO_ADTBdOydka6hHuSDo4aF0uWF5my6Q-wk88UiNZH8vynuxScasINqg2UbBu7NAH7lgtjuMQHCgySfZIYyQDfyjwp7CfKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از هیئت‌های گناوه بوشهر یه مداح به این شکل از جاویدنام‌های وطن یاد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66805" target="_blank">📅 12:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66804">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=p-wk4mockM9oIBVQ2N469o6ddg3V_IhvtodgkfpclK_vxlqAtlohZwjo5GXeOAhdnh6U1hC5FuCPdaGvwKJGZnHnuc-iYMFnro6R9o3eE--XNDzzXPxq5WWh-KhF2D7f393vkRDCx8EHaZrezdvHU7L-8QP_r5E0dpUabqx4NmxsSfVjMKpxz8AVduzceMRZis019QknkUfVnimE69Q0mTAGa7fySasWgLUKbIoUFZD4sdonln9lgDEnBEV1LupQJCiZUNabin4rscSX6_d04mEavWkDbzcBkd6Jqc8i2GH2921TXc8AeTbivmh9-aJTCCa8Gg9I3CjaEIazH-uSQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=p-wk4mockM9oIBVQ2N469o6ddg3V_IhvtodgkfpclK_vxlqAtlohZwjo5GXeOAhdnh6U1hC5FuCPdaGvwKJGZnHnuc-iYMFnro6R9o3eE--XNDzzXPxq5WWh-KhF2D7f393vkRDCx8EHaZrezdvHU7L-8QP_r5E0dpUabqx4NmxsSfVjMKpxz8AVduzceMRZis019QknkUfVnimE69Q0mTAGa7fySasWgLUKbIoUFZD4sdonln9lgDEnBEV1LupQJCiZUNabin4rscSX6_d04mEavWkDbzcBkd6Jqc8i2GH2921TXc8AeTbivmh9-aJTCCa8Gg9I3CjaEIazH-uSQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیره چرا شبیه یارو خپله تو آل زبیر نشسته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66804" target="_blank">📅 11:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66800">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=otfFcKeWFNJhrGNQcMHDQAuHgPPp0S2gIZjPvbDqYeO5Vu6VyrnmVtlmX2DYlSbvNs_UgCfvncMo4xVNb-ftqgvYhInXJrGr0VtvLF5JX2eyfWpQiBY8WL1dKLyLt2thawT6FnkCfRu_GYdnRBkaPOp1bpdZGHXjNl50XVZHUGEVclrfGptYAeSKOGkX5tjSNgCgDX8UCdJ21dd9pATqXpaTvE7MSQqWWllC2OpQOSrEEAvxJNoFDRgFBFib_sezHtDUxhVy2cQ89meGTqGpB41a72nGQNCQA9uZqG2Q7HlqJR0mpkUY0LazcAK-6csbJweL4PuNhOYEob-x9d9xnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=otfFcKeWFNJhrGNQcMHDQAuHgPPp0S2gIZjPvbDqYeO5Vu6VyrnmVtlmX2DYlSbvNs_UgCfvncMo4xVNb-ftqgvYhInXJrGr0VtvLF5JX2eyfWpQiBY8WL1dKLyLt2thawT6FnkCfRu_GYdnRBkaPOp1bpdZGHXjNl50XVZHUGEVclrfGptYAeSKOGkX5tjSNgCgDX8UCdJ21dd9pATqXpaTvE7MSQqWWllC2OpQOSrEEAvxJNoFDRgFBFib_sezHtDUxhVy2cQ89meGTqGpB41a72nGQNCQA9uZqG2Q7HlqJR0mpkUY0LazcAK-6csbJweL4PuNhOYEob-x9d9xnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تخریب آخرالزمانی در کاراکاس ونزوئلا پس از زلزله7.5 ریشتری
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66800" target="_blank">📅 10:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66799">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_ghgzTNGTtYLAMwmrSzJMKOKZAFF_au_j1anP_AfoOR-_MX42LWQpLgk5BIU7HTCFGP8L9R73IidLFiGJUPu9guXu-DaL2gmMo31Aj3yW-bVRHR-gYESJskD6norq915KDSws4Pi4l2fijQ6B_FhcIBq7FMYHqwRdntiAVWKTnbk5ORB4VvD997qYD6Cx_dyHmpFKsa6BIOKqyPML2OBbXsvkIS_mbRHYEDQiNc412jVeAq-dB3NmQvUA3vrUKzmtDl2NxSmFgEPSgfwe_PLrknpd4i1hVjBzkcPjHwi7bydOVgPp1_S34gRsuUiwD4pBwXBdBTGN8_p4pKF9bMa5LsG0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_ghgzTNGTtYLAMwmrSzJMKOKZAFF_au_j1anP_AfoOR-_MX42LWQpLgk5BIU7HTCFGP8L9R73IidLFiGJUPu9guXu-DaL2gmMo31Aj3yW-bVRHR-gYESJskD6norq915KDSws4Pi4l2fijQ6B_FhcIBq7FMYHqwRdntiAVWKTnbk5ORB4VvD997qYD6Cx_dyHmpFKsa6BIOKqyPML2OBbXsvkIS_mbRHYEDQiNc412jVeAq-dB3NmQvUA3vrUKzmtDl2NxSmFgEPSgfwe_PLrknpd4i1hVjBzkcPjHwi7bydOVgPp1_S34gRsuUiwD4pBwXBdBTGN8_p4pKF9bMa5LsG0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاروان اجنه و فرشتگان:
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66799" target="_blank">📅 10:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66798">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/638875c442.mp4?token=JDBzCK298PkqBjdMiIRXnSc6PSQACZ7YTRBCNm_gd7EDmF8r7LPZnj-7RkYT7RZba3mZK1hVyZzSBLCS0VAFRcpW_QDkM5rRPfDGp9EHOjgpwn2phNlOE0x560vhDv9bFJY8tJejEWepV5A4dOtGCZPFtiBu-vWUuGeTL7W3rZ_6CzxISP9njVWDd5PjOIsQFYSyYyBSYplRj5da_1esjYnE8b4EC1NoazxJyUK4CHbk2k5P8_EJ1Xc5G1OctGv15mro9_d3OEZOp-th8eqIvloJg2huim_b0DFNpu5V2Ia-H_AMax3BayS_s61erJ7G2zvSdhMHWxFt9J4gqA0_Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/638875c442.mp4?token=JDBzCK298PkqBjdMiIRXnSc6PSQACZ7YTRBCNm_gd7EDmF8r7LPZnj-7RkYT7RZba3mZK1hVyZzSBLCS0VAFRcpW_QDkM5rRPfDGp9EHOjgpwn2phNlOE0x560vhDv9bFJY8tJejEWepV5A4dOtGCZPFtiBu-vWUuGeTL7W3rZ_6CzxISP9njVWDd5PjOIsQFYSyYyBSYplRj5da_1esjYnE8b4EC1NoazxJyUK4CHbk2k5P8_EJ1Xc5G1OctGv15mro9_d3OEZOp-th8eqIvloJg2huim_b0DFNpu5V2Ia-H_AMax3BayS_s61erJ7G2zvSdhMHWxFt9J4gqA0_Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه سریزد  ، یزد
شاهکاری از معماری باستان
جایی که قرن ها پیش مردم اشیاء ارزشمند خود را در اتاقک‌های امن آن نگهداری می‌کردند
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66798" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66797">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lh2nlEs4i5VJB0Gl0FDiuCBkjNPWUhy0d_vpbfSSyU0FMTHx__EOzF0FrhEFBf1JqYYwgKdPiwN0b_mhFvqgfdAdG-piMfv_KdNDIGyw3f3icXQ5bpE1PDTBpis0NUF8cknnt2gg40h_Y3NwJXd2YTw6xrDcB5UejGu6Aamn_TBbd2tId2dgsQKKWBO9LaxUGEFC1QvIOhE3W0BOuhQoXzZeK8HX4cJJ4k9j19pxsWiWSIQUh43l2onWXFTjchuUPS5PS2O6_baGFo6qPNOv4svZ28a6kreKiIml3gPvmZfw3zgC4IeyUYt1H-jRonDboR50J2UxsmxkxUZ2HBcTvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
دونالد ترامپ:
دو زلزله بزرگ که اخیراً ونزوئلا را لرزاندند، بسیار عظیم بودند و تعداد زیادی قربانی برجای گذاشتند. ایالات متحده آمریکا آماده ارائه کمک است!
16;من دستور داده‌ام که تمام دستگاه‌های دولتی ما برای اقدام سریع آماده باشند. ما برای حمایت از دوستان جدید و فوق‌العاده‌مان حاضر خواهیم بود. گزارش‌های اولیه امیدوارکننده نیستند!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66797" target="_blank">📅 09:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66796">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‼️
از ناوشکن هسته‌ای کره شمالی رونمایی شد
🔴
رسانه‌های دولتی کره شمالی گزارش دادند کیم جونگ اون اعلام کرده است نیروی دریایی این کشور به سلاح هسته‌ای مجهز می‌شود و کشتی چوئه هیون رسماً وارد خدمت شده است.
🔴
این ناوشکن ۵۰۰۰ تنی به سلاح‌های ضد هوایی و ضد کشتی مجهز است و قابلیت حمل موشک‌های کروز و بالستیک با توان حمل کلاهک هسته‌ای را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66796" target="_blank">📅 09:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66795">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66795" target="_blank">📅 03:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66794">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66794" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66793">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lDtyQDYN3slVj0uUcxSj4VhxnlB_UrBdt4N9br9hZU9LVEF_fXbb6NTxoOMkG9QfpxyQ7OONNoIzoTQ8jnQYeMPx-bYvCQUbOZzPRZsSsZnGRVMkkZAwZfE-buemdulUUdUx3KMVHkLisCcgZf0z9nRKyqHGD97ppEDPnrC-ewe2FVFpGnJqT4PdMCtjNdorZXJDReQ8RiuSFtCTpQ1fEqRo1oLF_wphwVra_Y_05W3q0vWkblyiW0isJ6blfiMIsyGhRohjKOxny3WTJreMxcuOIrYYBL2IFyeilNHwLnH7MJ5JWZgWQ9647Sz8TignFoAhtQGbhcjaQd3GVOAVPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66793" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66792">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=nrH00JgOBjSIyVvT0xtKzFoS8RJR_HoQkcO_rOyVEBFcchjXOBnelKFT_jI1LjwAXabAY2K77WRjCfAeskvbyDnCCzs1kDJdnIU6khZg1uHW6d0tHTar-a1ZPhCVWkIgB6j_jz_I-BTH20mxG3mX8tvjNNZRlwpsvc0OarisL2qt3mDNu58bREys8rv1bBzTbqzGFsLLBtKo0fvVdLUT1zfrgvQ7tOuy37LddY_7S20N1LCHcMUYh7XHOJgSqNFOR1iVcnkapY1hllSv1p2FNEfeMWc5lutlAUhEWS44as448nvdTGtyCCLyHFvoQQmMlZBTqBfn0nQUh1NdNYPYvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=nrH00JgOBjSIyVvT0xtKzFoS8RJR_HoQkcO_rOyVEBFcchjXOBnelKFT_jI1LjwAXabAY2K77WRjCfAeskvbyDnCCzs1kDJdnIU6khZg1uHW6d0tHTar-a1ZPhCVWkIgB6j_jz_I-BTH20mxG3mX8tvjNNZRlwpsvc0OarisL2qt3mDNu58bREys8rv1bBzTbqzGFsLLBtKo0fvVdLUT1zfrgvQ7tOuy37LddY_7S20N1LCHcMUYh7XHOJgSqNFOR1iVcnkapY1hllSv1p2FNEfeMWc5lutlAUhEWS44as448nvdTGtyCCLyHFvoQQmMlZBTqBfn0nQUh1NdNYPYvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
درست در میانه یکی از مهم‌ترین مسائل، ناگهان خبر فوری منتشر می‌شود: “سنا رأی داده است که می‌خواهد ترامپ جنگ را متوقف کند.”
ایران این را می‌بیند و می‌گوید: این دیگر چیست
؟
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66792" target="_blank">📅 01:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66791">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=OHICNdyhGT7x95FEi48ZJXvSwoowvNQHN8ek1asau0UPlA9wyc7IFWBMvYk_Lz2mF5dSm8qe8xgDFnGZeWgv53itoZWaZAMoy2UiaKWCUgwBONxz6JUv5AqnQdJW7WcHpXK6o01iUj49seX3EhmT8LQwIKYTGdXmrsb56iNYgMkLRBjcI5NgcVtIC4xu-jy3NuVBbyVLDvPZL6TdnaKe4dMrFif0KGxajgawaKVLJXGSSL_L3By0zvs1WcgKmY1Ujh32CwCJLFbZYnYL4koNeDYaC31F0U4IfM4hpYm-ZPMIpMHEkoHiW7c1LL9pSEzvojL86V1P9iGBK5ldt3K_CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=OHICNdyhGT7x95FEi48ZJXvSwoowvNQHN8ek1asau0UPlA9wyc7IFWBMvYk_Lz2mF5dSm8qe8xgDFnGZeWgv53itoZWaZAMoy2UiaKWCUgwBONxz6JUv5AqnQdJW7WcHpXK6o01iUj49seX3EhmT8LQwIKYTGdXmrsb56iNYgMkLRBjcI5NgcVtIC4xu-jy3NuVBbyVLDvPZL6TdnaKe4dMrFif0KGxajgawaKVLJXGSSL_L3By0zvs1WcgKmY1Ujh32CwCJLFbZYnYL4koNeDYaC31F0U4IfM4hpYm-ZPMIpMHEkoHiW7c1LL9pSEzvojL86V1P9iGBK5ldt3K_CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره حمله به مدرسه میناب:
«نمی‌دانم که آیا آن‌ها هرگز خواهند توانست این مسئله را حل کنند یا نه.
موشک‌ها از هر طرف در حال پرواز بودند.
کسی گفت که آن موشک متعلق به ما بوده است. شاید بوده باشد، اما من هیچ چیزی ندیده‌ام که مرا به این باور برساند که واقعاً موشک ما بوده است.
موشک‌های فراوان دیگری هم توسط افراد و طرف‌های دیگر شلیک شده بودند.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66791" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66790">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">Live Volleyball</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66790" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66789">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=jqapmwTMLEArypU6GVnq5p44GoxxaBzimpujFr24esci0j5ElbjXCmiLMb0wdZj0WSfML8GSztQzkWf7R4ob9gA0oY4QaSs_9mvb79phIjCKnq8Nu6DSXCpg4e2cQk1iKuXzawZ2o15Ks6yD6P2D2TVdE2wIpvAh2M9qunStwpNmzzvZwLJxf3ZfZHLDe-cz3hswfbr6KlLWkup7rZWWxHEARtf-qHKzH5FASctWqr8YbbqT-QLc_pR22_ipd4SWW_H_mtgq4uEWUcsdMfmEUonecLWFYg6lhUPRbmHRGq72a__HSNmvLgWT-lSg0g03VmyVv2q36mnkY6Ya4edA7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=jqapmwTMLEArypU6GVnq5p44GoxxaBzimpujFr24esci0j5ElbjXCmiLMb0wdZj0WSfML8GSztQzkWf7R4ob9gA0oY4QaSs_9mvb79phIjCKnq8Nu6DSXCpg4e2cQk1iKuXzawZ2o15Ks6yD6P2D2TVdE2wIpvAh2M9qunStwpNmzzvZwLJxf3ZfZHLDe-cz3hswfbr6KlLWkup7rZWWxHEARtf-qHKzH5FASctWqr8YbbqT-QLc_pR22_ipd4SWW_H_mtgq4uEWUcsdMfmEUonecLWFYg6lhUPRbmHRGq72a__HSNmvLgWT-lSg0g03VmyVv2q36mnkY6Ya4edA7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرچم نروژ فقط یک طرح ساده نیست
🇳🇴
...
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66789" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66788">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=HjbItCn9g_9AWPabT5BB0EU-3N153eMkL52ftMno08pzENjKEzn8a842Rpe966PGVg29zhqEP9VNU2gSn_ccFxGG9rKGOwU4zwLaZ9rowp5DiHdbCqDXNjWcStMW9bb002_6q-Cr0IV-rCDfFTNgcJqyOw5Y-j-AvsiVQLQF7MIjLMADrFfYIVzgGxfqP1M6S2lFshjK74JNcb_Y_Jrl3K5AUJtbgUmVWF1SJ5sZw3_W-XmFXET7qitTdPOEhcaMHo-RyXGCwrYXN8IJhKgu-zuHHkJcUpYssLXHZ7zb10hc2mq0DuMvS57qTfR40HrvagVKpGeZYACPbGCPZhS6E6wmPs6TtY4CbxKWMHLq812jmyu986ciqio5elbWGX7COsmlI0TZ199BS2e99zfww-HUcAAaZdAQnnY2uOFDeEjEALrdIUjeStiIdg6pjbxlmlDPyTufeH7B6N9V51AsvRRPVnHQ46YdRzNZguAuWxaaLdnwMRsgO38eQfkWMHV5OdMZB690FZSeP1XRbM8F8_uqPX6g3FvnEQv0q-elJXfz-0IiBC0kpBH6mygGE-jzesjDYmzP3SiOiAbFlXzBk-omlJnqXKD1fWFCe_iRzFA_QJ-A9ZJlzoA1f9X4ZKa0B3GamYrFfe3iPBWbSiAtdAX6arxRH4B-Toi5Ngqk1rM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=HjbItCn9g_9AWPabT5BB0EU-3N153eMkL52ftMno08pzENjKEzn8a842Rpe966PGVg29zhqEP9VNU2gSn_ccFxGG9rKGOwU4zwLaZ9rowp5DiHdbCqDXNjWcStMW9bb002_6q-Cr0IV-rCDfFTNgcJqyOw5Y-j-AvsiVQLQF7MIjLMADrFfYIVzgGxfqP1M6S2lFshjK74JNcb_Y_Jrl3K5AUJtbgUmVWF1SJ5sZw3_W-XmFXET7qitTdPOEhcaMHo-RyXGCwrYXN8IJhKgu-zuHHkJcUpYssLXHZ7zb10hc2mq0DuMvS57qTfR40HrvagVKpGeZYACPbGCPZhS6E6wmPs6TtY4CbxKWMHLq812jmyu986ciqio5elbWGX7COsmlI0TZ199BS2e99zfww-HUcAAaZdAQnnY2uOFDeEjEALrdIUjeStiIdg6pjbxlmlDPyTufeH7B6N9V51AsvRRPVnHQ46YdRzNZguAuWxaaLdnwMRsgO38eQfkWMHV5OdMZB690FZSeP1XRbM8F8_uqPX6g3FvnEQv0q-elJXfz-0IiBC0kpBH6mygGE-jzesjDYmzP3SiOiAbFlXzBk-omlJnqXKD1fWFCe_iRzFA_QJ-A9ZJlzoA1f9X4ZKa0B3GamYrFfe3iPBWbSiAtdAX6arxRH4B-Toi5Ngqk1rM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی که یه عده از طرفداران حکومت با هوش مصنوعی از «مختارنامه» جدید درست کردن
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66788" target="_blank">📅 23:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66787">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukBDi11iHudKNmU6Ya5s1Ldhfure9JUk0RqAYr3Pt6W6tqsNTOXf1xHX3hswXjA57Z2vC_LIom8kT9_SVphwClwKQlLH2MjnTMx_1m20xn_0yCQef8rO-v-RlPYG3YMo71DIa9s3X_CArN1O62_TFYcGeSgd3wNiQPWLOOzuIT5SS9abqEODZbbSz4bMIxqGOw3DDto1pTuYdULII7ZjGwA0wHbJ8AoHVZOM2OvqNFxn4YTt-yJNgp4KU9g-og1DsHFK6JdxUsRZC9lrvC-KnHfO-ZehGN13q0tF9OmLm7AaL_yfK8LBqU-iBxToSd9KX9VJR9OsyCwfyFM03uttBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی وزارت امور خارجه:
اظهارات متناقض آمریکا درباره یادداشت تفاهم برای پایان جنگ به کاهش بی‌اعتمادی ایرانیان کمک نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66787" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66786">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66786" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66785">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OO4u3EwAZwUSPXTBKBzjRBD0IE1fZLhtcVrFZv7c2ykgk0J2Zeu3ojvi8GmULsO-yJi_LYlXyZRZRqVuYc-EbSFC8d9WWBtjTPzLBLYCoGYOVfMr_tPHZkyLC62E6rsHmbS1fWTRF5F5yssjwSrld9jKrT3pVzxnC-u9U1Li88oqdkI4pM_3nlPLbDxwCZfVHo_24w2W3UijJDI_eLdkQsWOAS3ncoSqjej4_d608m3XEhR2Hjeg78b_u6gT1Y0q5MtZ5nvIqtucwtLAQOTkpNRR19TQrhc1cTgSuZxV1zBhqp4iWRC-GdlkNOS4ta33cmSCNn_n0Aa_o9EE8jBDjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66785" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66783">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f56950043.mp4?token=tGIwW2ZL_hzHbgN_wI8te7MI4r6bXwk97upDKrUgxfaOAnM2CfymFC3zHLS-Mkc1ChGW78onR_wbRfuaDoNoM2uJLupi_Z0TCw1U7TDWqRPut9UjWfyPN5KEQlI1ofQi0YDuFptpVLFBWQ0CJo1wWCaut4WzjQ9v0EurURgzwRifxLYOmKqpHxiJQW3rpRHpHFSSDM4j195ITgstXk9xtGgYF_DcukO6okWIPJoFUOGF8EgjeIaQec7yHP-MYVvxDzciKSK-CmnGW6n4Qn6R3y65eaBAhaefArvfvgms_jnvHfPMDCntxW0cenChDvRU3x8VC6f8DeKbr-xZDf8X7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f56950043.mp4?token=tGIwW2ZL_hzHbgN_wI8te7MI4r6bXwk97upDKrUgxfaOAnM2CfymFC3zHLS-Mkc1ChGW78onR_wbRfuaDoNoM2uJLupi_Z0TCw1U7TDWqRPut9UjWfyPN5KEQlI1ofQi0YDuFptpVLFBWQ0CJo1wWCaut4WzjQ9v0EurURgzwRifxLYOmKqpHxiJQW3rpRHpHFSSDM4j195ITgstXk9xtGgYF_DcukO6okWIPJoFUOGF8EgjeIaQec7yHP-MYVvxDzciKSK-CmnGW6n4Qn6R3y65eaBAhaefArvfvgms_jnvHfPMDCntxW0cenChDvRU3x8VC6f8DeKbr-xZDf8X7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ازای شهادت مقام معظم رهبری چی از آمریکا گرفتید؟
قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66783" target="_blank">📅 23:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66782">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=HsG2isrk1i8XqSqEhEDCbs1_DcdFpaRGRmg5tWkfIII_fdGO-AoCnqBKOSWvWob1u1wa274SUiO-I8iTTbg_rVuYeT3lXeKG4wqZfu5AtLtEM50fSRmAYyTpU0PEjnsJloFju86ePf8WEOJFU8mmg8dovwsFi_i7stdVvQ9sHoUwopMU2X3TnSzcG1vEaWMfwlaV_N6Jm2JGN3rY4NY1XfU8P4ADv-sGbd4LgX2riREZZYTkby8meHBOJGx_ks7btVs1FzV-ZYwIpQ7H5f8Vf1KHa0ppLRfTKWWzk-aDVC7p_blrEmLDaHDeizdu3K4T2sgn12T1ePni67Lfbn9_3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=HsG2isrk1i8XqSqEhEDCbs1_DcdFpaRGRmg5tWkfIII_fdGO-AoCnqBKOSWvWob1u1wa274SUiO-I8iTTbg_rVuYeT3lXeKG4wqZfu5AtLtEM50fSRmAYyTpU0PEjnsJloFju86ePf8WEOJFU8mmg8dovwsFi_i7stdVvQ9sHoUwopMU2X3TnSzcG1vEaWMfwlaV_N6Jm2JGN3rY4NY1XfU8P4ADv-sGbd4LgX2riREZZYTkby8meHBOJGx_ks7btVs1FzV-ZYwIpQ7H5f8Vf1KHa0ppLRfTKWWzk-aDVC7p_blrEmLDaHDeizdu3K4T2sgn12T1ePni67Lfbn9_3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد ایران:
ایران خیلی خوب رفتار می‌کند. آنها با هر چیزی که من می‌خواهم موافقت می‌کنند و باید هم موافقت کنند.
در غیر این صورت، ما فقط برمی‌گردیم و کاری را که باید انجام دهیم، انجام می‌دهیم
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66782" target="_blank">📅 22:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66781">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=PTzn8qPy-lRMsXMLaQ4_WnVtEVPNXUGmWfUFRONKNA6c60xcfYKpIeZNLAt0Kj6MGt5z6DbJYMAgmCxpHN9AxJyANyydBiZvGPeoqir1bB1JbeJ1wsSiqKdJioPZYRtfafRiDj_sj_x4lTSzdeOJSRUA4aAvtnBb7jZstu5jzE7Zf_KYDAhcqBcnuQPrxLJyoTcrmQwYjzVqOb5x-7A4wkrO4lHi7P-WD5D8ll-do10MbNSVvEOH01zC-1Nl1ZUnNp9BsvBcbvCAKYb-xV_fQTb1xr_9LtGUquJVWajVwSwiKSyZwD7IvGK6qg4Og83cXawVqPA49gL5PZDkMb736Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=PTzn8qPy-lRMsXMLaQ4_WnVtEVPNXUGmWfUFRONKNA6c60xcfYKpIeZNLAt0Kj6MGt5z6DbJYMAgmCxpHN9AxJyANyydBiZvGPeoqir1bB1JbeJ1wsSiqKdJioPZYRtfafRiDj_sj_x4lTSzdeOJSRUA4aAvtnBb7jZstu5jzE7Zf_KYDAhcqBcnuQPrxLJyoTcrmQwYjzVqOb5x-7A4wkrO4lHi7P-WD5D8ll-do10MbNSVvEOH01zC-1Nl1ZUnNp9BsvBcbvCAKYb-xV_fQTb1xr_9LtGUquJVWajVwSwiKSyZwD7IvGK6qg4Og83cXawVqPA49gL5PZDkMb736Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«جنگ خیلی خوب پیش می‌رود. همانطور که
می‌دانید، ما با اختلاف زیادی در حال پیروزی هستیم. ایران امتیازات بسیار بزرگی می‌دهد. خواهیم دید چه اتفاقی می‌افتد، اما بسیار، بسیار، بسیار قدرتمند بوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66781" target="_blank">📅 22:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66780">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=pVITpPegZymLl9eNvHoILm_eY9o0hQFkcZyby1xGL5_84rf-Vlnfxc9lLa8SRqwoO6Q3ZdOgIhp3qUrj0Ia0PaNE4aNY_IFSTbfbnx3p5RJdYtUBynGU-ElxB5YtFYfNTNDPSsCuAWlrGbss9Y3itm3YtbhTjbaWWX97zsQpjWLFTZQc3I6WZUqoWnhODpgc7hJUE0ojPienEdBGAoHu1OKqNaG8q1IQlfjezLmwlioKDrYNFmQ5yinKrCGifU-Xj7KDqggnLmHy0Rqltq58jAz8vmvW_z1LLhyTY-IFYTsr6K4ducNro6hLU10fiSXcBH6AFdZpbZOT1u0sdo3bNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=pVITpPegZymLl9eNvHoILm_eY9o0hQFkcZyby1xGL5_84rf-Vlnfxc9lLa8SRqwoO6Q3ZdOgIhp3qUrj0Ia0PaNE4aNY_IFSTbfbnx3p5RJdYtUBynGU-ElxB5YtFYfNTNDPSsCuAWlrGbss9Y3itm3YtbhTjbaWWX97zsQpjWLFTZQc3I6WZUqoWnhODpgc7hJUE0ojPienEdBGAoHu1OKqNaG8q1IQlfjezLmwlioKDrYNFmQ5yinKrCGifU-Xj7KDqggnLmHy0Rqltq58jAz8vmvW_z1LLhyTY-IFYTsr6K4ducNro6hLU10fiSXcBH6AFdZpbZOT1u0sdo3bNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عبدالناصر همتی:
اگه کیفیت ذرت و گندم آمریکا خوب باشه ازشون میخریم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66780" target="_blank">📅 22:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66779">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ov0KkBnuADwy_gkZy5K0BkZw-oc3LwJ_QKHyYkXupFdjPuJVOH_fuLnZZ0XLblFAHB1adowE_OSPt-ifZ0Am2ICP8OUorEwOdBF_8rAsQ9r4ttQUHJ1-93gTfll-g3DDBuzsc05Ii_BjnL_Z1BF18vA9EVy7HNmNtNInb1qimyJfpmnoHez31ayjWUrwY2qVO8NrH0RBKkuMIAKMXdrG6FHb1kARHlifYNv3mo7q_P9GhtwXr1-XpZyr8Nr4RCZWGF0f1Aq2wnA7EG-Y7xngEexjwzYUxx3KgH9iFdoxURxHwsQ2PSZIbpz8eLIxoIuoH4NFOtRByKPmlexiWM6pwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتاق جنگ اسرائیل به مارکو روبیو:
رژیم جمهوری اسلامی و حامیانش در عمان در تنگه هرمز هزینه دریافت میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66779" target="_blank">📅 20:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66778">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=JWfNgYfnNjPdJKhFrmJXvD3HKEFoiUBUf9bgnTRrsiyZ9ajU0obtB-xzJersxM0i34daQRr8TuNgKV1IUdUtf24rxq5yJKoylDUksN1G1U9kaF5TcONq6qoT6qwjoXJ2pMkaofxUF7AC_Dt7H7r5Y7yI9MQcNcc0zXbHABYLfJ0703MXJYPM9KuxbUCJPzp0RP-5crGFfk_AHKO67bHsaQiS3wEiyn1gmZ6M3NAuauolapuTtifekQW8OoNMX9DlLxXJBT3hkj49zvclml25wef1hsAHPEHKEFClWpmo4xIu6SwtJSoQJdRXl6AwiXoR9oMYzplwi9eDEGDMftXbpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=JWfNgYfnNjPdJKhFrmJXvD3HKEFoiUBUf9bgnTRrsiyZ9ajU0obtB-xzJersxM0i34daQRr8TuNgKV1IUdUtf24rxq5yJKoylDUksN1G1U9kaF5TcONq6qoT6qwjoXJ2pMkaofxUF7AC_Dt7H7r5Y7yI9MQcNcc0zXbHABYLfJ0703MXJYPM9KuxbUCJPzp0RP-5crGFfk_AHKO67bHsaQiS3wEiyn1gmZ6M3NAuauolapuTtifekQW8OoNMX9DlLxXJBT3hkj49zvclml25wef1hsAHPEHKEFClWpmo4xIu6SwtJSoQJdRXl6AwiXoR9oMYzplwi9eDEGDMftXbpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
توافقات اخیر با رژیم جمهوری اسلامی بخشی از یک روند مذاکره‌ای و یک اقدام موقت ۶۰ روزه است.واشینگتن انتظار دارد تهران به تعهداتی که در سوئیس پذیرفته پایبند بماند و در غیر این صورت، پرزیدنت ترامپ ابزارها و گزینه‌های مختلفی از جمله بازگرداندن تحریم‌ها را در اختیار خواهد داشت.این تعهدات به صورت روشن و صریح مطرح شده‌اند و ادامه مسیر مذاکرات به میزان پایبندی رژیم جمهوری اسلامی به آن‌ها بستگی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66778" target="_blank">📅 20:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66777">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=YMREMZikNro2whZZuXrYm0fjkw62kdI99dDSgn6MW-UPTV8aL4N5GIbFeGgSDX3Cuc9YYiwqM0uelJB5gRN_jMnskm5ukEPvNF3fPcC9DH4RR-B61SV43i0F1ctlTdXB44iVejXFEBvU7hxSEOrFBJMZ58RmU-z7bcNZq8WijTHSTtVAyAbKFrEYOkMXYDZXS8Ozr0vYuAxanI-RkSid-PZo3pobHkMytd9JAnQ9NCwnUHEGoRV4ut1AeBpi5kOQlLxGMNxrdmaqVwBM98n8iopxoEiJV9ecQcI2vmdeI4-mC5MuJ8_ewSQZCnzH69OONbJk66ZPo0Pj6ERPulrFKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=YMREMZikNro2whZZuXrYm0fjkw62kdI99dDSgn6MW-UPTV8aL4N5GIbFeGgSDX3Cuc9YYiwqM0uelJB5gRN_jMnskm5ukEPvNF3fPcC9DH4RR-B61SV43i0F1ctlTdXB44iVejXFEBvU7hxSEOrFBJMZ58RmU-z7bcNZq8WijTHSTtVAyAbKFrEYOkMXYDZXS8Ozr0vYuAxanI-RkSid-PZo3pobHkMytd9JAnQ9NCwnUHEGoRV4ut1AeBpi5kOQlLxGMNxrdmaqVwBM98n8iopxoEiJV9ecQcI2vmdeI4-mC5MuJ8_ewSQZCnzH69OONbJk66ZPo0Pj6ERPulrFKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: برخی از عناصر اطلاعاتی ایالات متحده ارزیابی کرده‌اند که اسرائیل علاقه‌مند به تضعیف تفاهم‌نامه فعلی است.
🔴
روبیو: نمی‌دانم در مورد چه اطلاعاتی صحبت می‌کنید. نمی‌دانم این اطلاعات را از کجا می‌آورید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66777" target="_blank">📅 20:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66776">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=c70QLqsGtWdUR2DsJLbBL_0Ica-xcj4aTec1zVUvk2F0cZef8sT4Cok5ynz89TUQQ_TiqiIV_jWAu6Ai4pgip_SK3pkYc0Bp6f5dHoltTwklhLWB64CeX77lNi16hb5G2Oy2ewVpmxEMZeo-ShoSQo87YKFGUqcp22FHXh8e0NHAq4fTjkV3bodX-EWsj7_FONHUPxxmZSHzL8WMTtrH_hpMirtfa7OYc056KqhK4GGGMLpCa4-mpV2fEemRXul94HFVU7PQZBrHmE3o8EPmkH8KKkYQyzdhkrOTIi1L80uvtvTXwpHbdNAyBcDEmmBP3L5KpKAAHi0N5wBh73TorA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=c70QLqsGtWdUR2DsJLbBL_0Ica-xcj4aTec1zVUvk2F0cZef8sT4Cok5ynz89TUQQ_TiqiIV_jWAu6Ai4pgip_SK3pkYc0Bp6f5dHoltTwklhLWB64CeX77lNi16hb5G2Oy2ewVpmxEMZeo-ShoSQo87YKFGUqcp22FHXh8e0NHAq4fTjkV3bodX-EWsj7_FONHUPxxmZSHzL8WMTtrH_hpMirtfa7OYc056KqhK4GGGMLpCa4-mpV2fEemRXul94HFVU7PQZBrHmE3o8EPmkH8KKkYQyzdhkrOTIi1L80uvtvTXwpHbdNAyBcDEmmBP3L5KpKAAHi0N5wBh73TorA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
وقتی می‌گوییم تنگه‌ها را باز کنید، منظورمان این است که تنگه‌ها را آزاد باز کنید. آنها آبراه‌های بین‌المللی هستند.
هیچ کشوری روی کره زمین از گرفتن عوارض در تنگه‌ها حمایت نمی‌کند. این اتفاق نخواهد افتاد. ترامپ این را به روشنی بیان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66776" target="_blank">📅 20:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66775">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=vfg8JL1woyRguJ3xj7deL9a2LquEs3COAw8l-6M3Z6F0vRM4VnFRE1lgyO91rHy-dlqI1KDD_oHWYj0q4y3zN_Xxc7z9Px_A_vqRcm5ergSIe2kyea4wdz_iOGCreyn3scOchIvxjLn7GMK8v_Yk9AAtcJ6exSq-7dFh_SXVY7Hb-QKswlK2hZC3lvcCytWc_BDqj-XFTsuFqC0t8fh7F3qdZH_n9gU_T9Q3bSsYQAjgmJQ2lKTwPw5MfaB23u1q2ntno1AzAR24b3bpMw-Twi-DtpBDe7Wu1I5Pkp1eR2qUx3VZEtYlL3UX_NPnReq6x5P_fhg9YmF8xUTiBcMing" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=vfg8JL1woyRguJ3xj7deL9a2LquEs3COAw8l-6M3Z6F0vRM4VnFRE1lgyO91rHy-dlqI1KDD_oHWYj0q4y3zN_Xxc7z9Px_A_vqRcm5ergSIe2kyea4wdz_iOGCreyn3scOchIvxjLn7GMK8v_Yk9AAtcJ6exSq-7dFh_SXVY7Hb-QKswlK2hZC3lvcCytWc_BDqj-XFTsuFqC0t8fh7F3qdZH_n9gU_T9Q3bSsYQAjgmJQ2lKTwPw5MfaB23u1q2ntno1AzAR24b3bpMw-Twi-DtpBDe7Wu1I5Pkp1eR2qUx3VZEtYlL3UX_NPnReq6x5P_fhg9YmF8xUTiBcMing" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
به من گفتند: «وارد رفح نشو.»
می‌دانید چرا این را گفتند؟
چون رئیس‌جمهور ایالات متحده گفته بود ارسال سلاح را متوقف خواهد کرد.
من گفتم: «احترام زیادی برای او قائلم. او در آغاز جنگ کنار ما ایستاد. اما ما چاره‌ای نداریم. وارد رفح خواهیم شد. و اگر لازم باشد، حتی با ناخن‌هایمان هم خواهیم جنگید.»
گاهی باید بدانی چگونه حتی به رئیس‌جمهور ایالات متحده هم «نه» بگویی.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66775" target="_blank">📅 19:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66774">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=XwmVoMMvTdwFUOWBLHwO2O3EbGB-g6SIU6bR-HID75Aw8BMrMBPeXnuSa94eB_9RlTtCtDn3HrBxlJb98ofPY2uNfr_0q_n3L9p3k3-ocXCVT81U57BFVp3Ca0B6jBHv4KHRYsMsor4D8BYeT7wg1RlXog3m2pNaoGG0stDzFZV98fCBxW5DUBjQugDbYMLYbdql9zlqF82b2D9lFqGy4O5aBrZq2mCVs4_zz0GqeVyveewzZctPyLFkl-sO7Q8JQ1EMPykAH20Xx-EkLZRMl6usUC-_Fw5jZ4vrrx3NraM0zNA8QqBlQoBeo1sDPMOSF3-iYJlgwzUU2L-8xg7zHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=XwmVoMMvTdwFUOWBLHwO2O3EbGB-g6SIU6bR-HID75Aw8BMrMBPeXnuSa94eB_9RlTtCtDn3HrBxlJb98ofPY2uNfr_0q_n3L9p3k3-ocXCVT81U57BFVp3Ca0B6jBHv4KHRYsMsor4D8BYeT7wg1RlXog3m2pNaoGG0stDzFZV98fCBxW5DUBjQugDbYMLYbdql9zlqF82b2D9lFqGy4O5aBrZq2mCVs4_zz0GqeVyveewzZctPyLFkl-sO7Q8JQ1EMPykAH20Xx-EkLZRMl6usUC-_Fw5jZ4vrrx3NraM0zNA8QqBlQoBeo1sDPMOSF3-iYJlgwzUU2L-8xg7zHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست وزیر نتانیاهو:
در عملیات غرش شیران بود که من به ترامپ حمله در ایران را اطلاع دادم و هیچ اجازه  گرفتنی در کار نبود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66774" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66773">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=t5dcLX0qb4-Go69BHoT6yRRc1AskIfQj7k2oIVZNgzIokjLoZBFjuZY836JfWjkDudGaUH914rSWXBuFK8sdUxBmKx8rbUoMw9KGqKx_6-WbiEIBei4z04iZGKYGJr9VHnwnjrq-0qokoPUPUY2PIipd2IC5DXi2liiRYa-PGLi4J1-j0C9bXkanQMrPo0BCoqURWkyEe4bw4b6GAptLsCXIvh7Q55jxCaMiugAHIM-WMTqf9UQ9rRH1HWGoQHnQLTBe6KXIoLT50IzMOy3RiE3TI2MwH-0tr3Lp7wHjQxQ0DwgXecvzbYERli6VV-nsknE_e1a9j5j7EU3J2eLlAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=t5dcLX0qb4-Go69BHoT6yRRc1AskIfQj7k2oIVZNgzIokjLoZBFjuZY836JfWjkDudGaUH914rSWXBuFK8sdUxBmKx8rbUoMw9KGqKx_6-WbiEIBei4z04iZGKYGJr9VHnwnjrq-0qokoPUPUY2PIipd2IC5DXi2liiRYa-PGLi4J1-j0C9bXkanQMrPo0BCoqURWkyEe4bw4b6GAptLsCXIvh7Q55jxCaMiugAHIM-WMTqf9UQ9rRH1HWGoQHnQLTBe6KXIoLT50IzMOy3RiE3TI2MwH-0tr3Lp7wHjQxQ0DwgXecvzbYERli6VV-nsknE_e1a9j5j7EU3J2eLlAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66773" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66772">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66772" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66772" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66771">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=o9gz9ktUQWw_6D6nd-7Tm050Ou1320H8r1CKeRWI9YkmFQoeojnm4hqWcTSaKc0EOYaRAyztdVI4uiuSJd8MmqmNTpFMrrga_XCJWh5_-1_9aLitX_hRnuXMeH_mNg_FYCC_mUQTL2d6hqM2LZGi1tfsib1LR0NrE3x9xmwypWJSxlLdzbmNWi-4_FdGsx4hD8AtMyeLC2ee8M20YXbM57I2keRKBaR3dbI4C7j-vc7h1-6kUZeLooTK6sVKKJ8Wtj05M8L9bBhTzMxpU6hvl0lx1jFeamGGbJWHUWhYb54N7rIrW6FBRUa4CVynuZJULKQFb5-phMc_rSyVk_dpJasgbew2rS-98JSaZWfNDclMD15Gi78p1ze7XoGeRMk1sM7A4PLRce7Zf6zaPi1_fHvs33prQCkH9RUwLc1DbHEweYB8sSi4N-cgfM6N7MZ09JXmIiMrliKuT84JEoMNrg0ooQSviWc6CRTY4fSGVQvFHyg6a3WIbpakf-vnI9Xpguhz9jb7baaPfOyUcs1bYoOgamMHHE4vCg3cdLknCFs6VdSHXGlUhQ4ELecSBuoPKNEb7Sr0i_-9jLsy2uTk7rCDEULYtt5DadRIvJ2p1HqWwkTZe_GUEKyO37qKrPyGRTxh6rajByOTlUCchPM7sE_xilAY0AbaRO3a5z0T41E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=o9gz9ktUQWw_6D6nd-7Tm050Ou1320H8r1CKeRWI9YkmFQoeojnm4hqWcTSaKc0EOYaRAyztdVI4uiuSJd8MmqmNTpFMrrga_XCJWh5_-1_9aLitX_hRnuXMeH_mNg_FYCC_mUQTL2d6hqM2LZGi1tfsib1LR0NrE3x9xmwypWJSxlLdzbmNWi-4_FdGsx4hD8AtMyeLC2ee8M20YXbM57I2keRKBaR3dbI4C7j-vc7h1-6kUZeLooTK6sVKKJ8Wtj05M8L9bBhTzMxpU6hvl0lx1jFeamGGbJWHUWhYb54N7rIrW6FBRUa4CVynuZJULKQFb5-phMc_rSyVk_dpJasgbew2rS-98JSaZWfNDclMD15Gi78p1ze7XoGeRMk1sM7A4PLRce7Zf6zaPi1_fHvs33prQCkH9RUwLc1DbHEweYB8sSi4N-cgfM6N7MZ09JXmIiMrliKuT84JEoMNrg0ooQSviWc6CRTY4fSGVQvFHyg6a3WIbpakf-vnI9Xpguhz9jb7baaPfOyUcs1bYoOgamMHHE4vCg3cdLknCFs6VdSHXGlUhQ4ELecSBuoPKNEb7Sr0i_-9jLsy2uTk7rCDEULYtt5DadRIvJ2p1HqWwkTZe_GUEKyO37qKrPyGRTxh6rajByOTlUCchPM7sE_xilAY0AbaRO3a5z0T41E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66771" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66770">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyiZ9IGOZeqHfWwEuDo8REQV_fyTMs3HlXQR6gNCbHY29eoWO_pkl1dYBYgsVujvHort8DxNrNvtoCwBq5NSt9hX6bVmTsGBxcLTbgAJ0Vkpfn0PiwcQncH1w_bClL5A08lVdKKZ8SKfwR2mno4x5MWf1MGDBMgpgtec2bkjQtiHyX6Bx30I52p9EBRjNTtRFzF-pFCreIaxjgSpz55WPR-YdUlLMKuyNy3vESdGVTGazGgFWjnRuClNr7ULoZfzmYDsQNPHXfIZqSMFG_WBYwMbRY9tmGnrO0agUXRwBLYh0NUWe-aPDmOdNzjATuZdnwPy_Na6EohDDF6JrIKc5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت
ترامپ:
ایران به آمریکا اطلاع داده که، برخلاف گزارش‌های دردسرساز رسانه‌های فیک‌نیوز، «هیچ عوارضی، هیچ هزینه بیمه‌ای و هیچ نوع هزینه دیگری از هیچ کشتی‌ای که از تنگه هرمز عبور می‌کند، توسط ایران درخواست یا دریافت نمی‌شود. اگر این خبر نادرست باشد، مذاکرات فوراً پایان پیدا می‌کند!
همچنین، آمریکا هیچ پولی به ایران نداده و هیچ بخشی از پول‌های ایران را هم آزاد نکرده است. ما بخشی از پول‌های ایران را که کاملاً تحت کنترل خودمان است، برای حمایت از کشاورزان و دامداران آمریکایی آزاد خواهیم کرد تا با آن ذرت، گندم، سویا و محصولات دیگر خریداری شود. ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد را منحصراً از آمریکا برای آن‌ها خریداری خواهیم کرد.
از توجه شما به این موضوع متشکرم!
— دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66770" target="_blank">📅 17:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66769">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=lc0Ap4FmdSqG6Iwz3JbJxWHvG5W8jkrX54QbVFWqmxD4bzA6b39CFS1nnsZZfofBBkAHYqlpNQjvAn6Vz9Ts5fLu4red-U5c16HbTi2HYwEdlQns7meT1GLTEVFXW7ez_MPyxfAYZ8Jr6yTN6VlTvUSp3WTNJHjtUiWJVqlk9FFklmTX2CanDyhSwYnlq0gkCo5UBBIVQOjAD2xeQVJ9gg_Z_Vqd9aPNdeEL_fRI0ejOn0RwaNuSwg5Z1YYxavWmiaMnwNugN3q8LdVqMlphZgLJEfYACLn4HC0MDEaCiOKpc1LDKRHxNFhxqSu0pFUDL0graWGupgd-8gLS1DzoqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=lc0Ap4FmdSqG6Iwz3JbJxWHvG5W8jkrX54QbVFWqmxD4bzA6b39CFS1nnsZZfofBBkAHYqlpNQjvAn6Vz9Ts5fLu4red-U5c16HbTi2HYwEdlQns7meT1GLTEVFXW7ez_MPyxfAYZ8Jr6yTN6VlTvUSp3WTNJHjtUiWJVqlk9FFklmTX2CanDyhSwYnlq0gkCo5UBBIVQOjAD2xeQVJ9gg_Z_Vqd9aPNdeEL_fRI0ejOn0RwaNuSwg5Z1YYxavWmiaMnwNugN3q8LdVqMlphZgLJEfYACLn4HC0MDEaCiOKpc1LDKRHxNFhxqSu0pFUDL0graWGupgd-8gLS1DzoqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اگه
فکر می‌کنید قراره چیزی کسشر تر از این امروز ببینید عرض کنم که سخت در اشتباهید. فقط کافیه موزیک ویدئو شاهکار صداوسیما برای تیم امیر قلعه‌نویی رو ببینید تا بفهمید با کیا شدم ۹۰ میلیون
😐
😐
😐
😐
علی بیرو تو دروازه یا نیازمند ، کنارش شجاع و کنعانی میشن پدافند
تنگه هرمز ما تو دستای سعیده
شوت‌های قدوس و رامین مثل خیبرشکن، مستقیم به قلب دروازه‌ی دشمن میرن
ترابی دریبل‌زنه، نعمتی هم حامیشه، مثل هایپرسونیک از لای دفاع رد میشه
یه طرف میلاد و ازون طرف جهانبخش، پهباد شاهد رو روی دروازه میکنن پخش
حاج صفی ، حردانی و یوسفی مثل شیرن
توپ‌های علی علیپور از پاتریوت هم در میرن...
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66769" target="_blank">📅 17:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66768">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=kQEQ8upSI8y-Bll8Y3S8ZWWV32f6BLa07rKQ1qLfXLEcJCfZ8lC4yo_xa7Eivcog79gjTpYkgKMAZaBMpKMFdR7G2yDdx4-pI1VljLRB0J20-q0eAweUBBtQcbF-7V_QNQPeTgVWkrV2iGvoGfT8iUR3o-MA7d7rZAGbacByohSI2hKjaDBB9kwnPeq9tYQ1-1zE2v8MK_nTMKT5KQPcMhEWwmABRchDvbg4KtPaualfUpc9fkyzic_KYODLBvYLURAUM2WpkDPJQ2VfOAzEQdyDU4PbCzn-z5C1RduNu87vJ6jsKkqEs6eNQya27Zc0Ge9SX_Kmi5fsKJmWxucBhi1OjfWtHjN6OA6uzNYRvl8V-hnIPNfE0F_v6Y7jBTTtzxk_SBq2Ttk7aGK0NDpb8hshamdvQzSxk8eEg_QyBgoaFFnYEEKFlHJqoUv4pjZa0kdPedZLKd0CYUI-ZJtioDGlT56Zu941dm5jphJF-5bOnMqJ-ev9TVAE3OamKENYCbzwdx4scLC63WsSVaI8HskJ7NGwyWCAFztaoDBbdbMRxh1WYf2kENYFXfzQuCBsvPuWhLqcvy7U3Tslpt2aKcgdGY0wdKPh0jbUgZ2YXpaWpr4q35FfxoUH82QJArbAZ2wjVmyzf3UogzKHiXb5LF9qhgivZx7EIZFSq82zWx0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=kQEQ8upSI8y-Bll8Y3S8ZWWV32f6BLa07rKQ1qLfXLEcJCfZ8lC4yo_xa7Eivcog79gjTpYkgKMAZaBMpKMFdR7G2yDdx4-pI1VljLRB0J20-q0eAweUBBtQcbF-7V_QNQPeTgVWkrV2iGvoGfT8iUR3o-MA7d7rZAGbacByohSI2hKjaDBB9kwnPeq9tYQ1-1zE2v8MK_nTMKT5KQPcMhEWwmABRchDvbg4KtPaualfUpc9fkyzic_KYODLBvYLURAUM2WpkDPJQ2VfOAzEQdyDU4PbCzn-z5C1RduNu87vJ6jsKkqEs6eNQya27Zc0Ge9SX_Kmi5fsKJmWxucBhi1OjfWtHjN6OA6uzNYRvl8V-hnIPNfE0F_v6Y7jBTTtzxk_SBq2Ttk7aGK0NDpb8hshamdvQzSxk8eEg_QyBgoaFFnYEEKFlHJqoUv4pjZa0kdPedZLKd0CYUI-ZJtioDGlT56Zu941dm5jphJF-5bOnMqJ-ev9TVAE3OamKENYCbzwdx4scLC63WsSVaI8HskJ7NGwyWCAFztaoDBbdbMRxh1WYf2kENYFXfzQuCBsvPuWhLqcvy7U3Tslpt2aKcgdGY0wdKPh0jbUgZ2YXpaWpr4q35FfxoUH82QJArbAZ2wjVmyzf3UogzKHiXb5LF9qhgivZx7EIZFSq82zWx0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
⚠️
پشمام اینو داشته باشید. تو عراق از معاون وزیر نفت سابق این کشور حدود ۸۵ میلیون دلار اسکناس نقد از زیر زمین کشف کردن که دفن شده بوده!! فساد سیستماتیک تو کشورهای اسلامی ماشالا خوب رونق داره
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66768" target="_blank">📅 17:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66765">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c68737622.mp4?token=te4p95x4SRzoJ7fhZnbnV9JA786wV0onKzJ-uu8QD06HtSrDgYmTq6ls-IPA-2XcBvSm4sx6hipiHpWVr3FGBlDxulnLcGWPj9Vi5K_2pJTHuGF0G0VtEJIHO1EeTGWpiPKcjFzq0MQac8BG0_is9hpalJ7_2S7rlMilpWcaX3rMwxx9CgsHdlKUNW0OgY1qrvwGkFM2kxO5kH-RP0FSSxM-HD-VJg6rBbRB4VyNH0hEgytaH_fkoiUsWWUlRV_xTcIKmzkUFMFAMz0o19R6xA2xoU0BqFmwKGrA6IRc9Nn3SoOuTSqGgONkZX92fGUMB3Fa8cV6ZejyFYtfIv-baw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c68737622.mp4?token=te4p95x4SRzoJ7fhZnbnV9JA786wV0onKzJ-uu8QD06HtSrDgYmTq6ls-IPA-2XcBvSm4sx6hipiHpWVr3FGBlDxulnLcGWPj9Vi5K_2pJTHuGF0G0VtEJIHO1EeTGWpiPKcjFzq0MQac8BG0_is9hpalJ7_2S7rlMilpWcaX3rMwxx9CgsHdlKUNW0OgY1qrvwGkFM2kxO5kH-RP0FSSxM-HD-VJg6rBbRB4VyNH0hEgytaH_fkoiUsWWUlRV_xTcIKmzkUFMFAMz0o19R6xA2xoU0BqFmwKGrA6IRc9Nn3SoOuTSqGgONkZX92fGUMB3Fa8cV6ZejyFYtfIv-baw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
⚠️
ویدیوهایی که خیلی از دیروز  وایرال شده از کربلا؛
دیروز کاروان شیعه اسماعیلیه که تا امام ششم امام صادق رو قبول دارن، واسه زیارت به کربلا رفته بودن.
از اون طرف کاروان ایرانی ها هرجا اینارو میدیدن واکنش نشون میدادن..
تو یسری جاها هم نزدیک بود دعوا فیزیکی بشه که پلیسِ عراق اجازه نداد...
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66765" target="_blank">📅 16:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66764">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=PXKnNE3RvbqgN8axPWVInW4YltO2hF0mgPxIBaTxWOfXQc1FsZRqnPuTBKR6X41g8NLecQwWwnj-jhSNslm3La-CwxznQuR6T1XlgNWDqXngNTpaztV0590T6AASqe4-C_bCrk5hBtc50cF4UG4J1QKOz447HyGexbr5iQAOAxilQipRoEqkoyz6TbwOPs4ud5pIVOzg-LcZtabeQL7sigT5TxW90CDz-ztFQWmVd0j3A4-FOfxxlewOMchNl9Vxk_OiQcD_dNVvsbDo5OGLzphlkmOVthKWRdxvOc3RnVjAbofoXd00v4QiNE9mzudToCNBa_P3kEJfLo_LDeIvDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=PXKnNE3RvbqgN8axPWVInW4YltO2hF0mgPxIBaTxWOfXQc1FsZRqnPuTBKR6X41g8NLecQwWwnj-jhSNslm3La-CwxznQuR6T1XlgNWDqXngNTpaztV0590T6AASqe4-C_bCrk5hBtc50cF4UG4J1QKOz447HyGexbr5iQAOAxilQipRoEqkoyz6TbwOPs4ud5pIVOzg-LcZtabeQL7sigT5TxW90CDz-ztFQWmVd0j3A4-FOfxxlewOMchNl9Vxk_OiQcD_dNVvsbDo5OGLzphlkmOVthKWRdxvOc3RnVjAbofoXd00v4QiNE9mzudToCNBa_P3kEJfLo_LDeIvDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مترجم: «ما هرگز در مورد توانایی‌ها و تجهیزات هسته‌ای خودمون توافق نمی‌کنیم.»
پزشکیان: نه!! موشکی! موشکی را گفتم…!
مترجم: ببخشید موشکی.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66764" target="_blank">📅 16:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66763">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=AzauJ80-vBj34iTpJaWq-CHAun23T-GJ5rX4S7AJf26XyInatVGLrAmSTN88bAhVMGWZKcYCCWsfa0_MpbHvLrb-XyVGfFIB30baodkeyesk1kfCNmKr5Fa0MI2Tk-sEF046Lip3j7ph6KbPFUcKIKZFS5Ak8hHKK0bybuuUuJZi3NrXtugp3vOvXu0A7UJI43XFbYxNiAguIYGKjLpRcE7Lx6VHkuDd_BQOu39L2HMtBtydjPiDgLB1Km0Pb8RH-DJcBqfuILEIOp_6bv1_6r-MvQeRMS5x6ZrKSwdW08DSxHIZOfCD0KqB-_2laUNauMVZOpo49mQodYe7NKwwUw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=AzauJ80-vBj34iTpJaWq-CHAun23T-GJ5rX4S7AJf26XyInatVGLrAmSTN88bAhVMGWZKcYCCWsfa0_MpbHvLrb-XyVGfFIB30baodkeyesk1kfCNmKr5Fa0MI2Tk-sEF046Lip3j7ph6KbPFUcKIKZFS5Ak8hHKK0bybuuUuJZi3NrXtugp3vOvXu0A7UJI43XFbYxNiAguIYGKjLpRcE7Lx6VHkuDd_BQOu39L2HMtBtydjPiDgLB1Km0Pb8RH-DJcBqfuILEIOp_6bv1_6r-MvQeRMS5x6ZrKSwdW08DSxHIZOfCD0KqB-_2laUNauMVZOpo49mQodYe7NKwwUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
مراد ویسی: با توجه به تضمین آمریکا، که گفته در جریان مذاکرات ۶۰ روزه مقامات رو ترور نمیکنیم، احتمالا تا ده روز آینده از مجتبی رونمایی بشه.
مجتبی قراره احتمال زیاد تو مراسم تشییع باباش شرکت کنه. اگرم پیداش نشد، یه جای کار میلنگه و مجتبی حالا حالاها پیداش نمیشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66763" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66762">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=iUkYN-aqDVxC3D4VLupL4AF4d4fQx9__gugNHYXvwxA3s4vkKPCcA2NvTJe2i5hizkB54BmLrc1QoO78xkC0Io7NPRx14kI1dBV4oe0pakkdJ6REmUCMKEcHyT2sGjmfjfulcfrib6lTZ0n1XLbo0K1Hj42VT0woZanDx6NQIuJ3Wzgh2iQtdiBPVb4PVUeW5s17h_uvvRzcM1CH_LQ5Bhz4xuubFTICLlTwspw6w2iEEMskm5BEOFVGm2KSfLCILEfOZ9rZz_ErvtvFcEp9JAuIBM63tG6ukwnUrRi7WiKwl5Mc0O-CYDSrR71JNjPUwytDZuxlli3xoHa65SOIZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=iUkYN-aqDVxC3D4VLupL4AF4d4fQx9__gugNHYXvwxA3s4vkKPCcA2NvTJe2i5hizkB54BmLrc1QoO78xkC0Io7NPRx14kI1dBV4oe0pakkdJ6REmUCMKEcHyT2sGjmfjfulcfrib6lTZ0n1XLbo0K1Hj42VT0woZanDx6NQIuJ3Wzgh2iQtdiBPVb4PVUeW5s17h_uvvRzcM1CH_LQ5Bhz4xuubFTICLlTwspw6w2iEEMskm5BEOFVGm2KSfLCILEfOZ9rZz_ErvtvFcEp9JAuIBM63tG6ukwnUrRi7WiKwl5Mc0O-CYDSrR71JNjPUwytDZuxlli3xoHa65SOIZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجری شبکه دو:
کاش قبل از جلسه تفاهم نامه یه سر گلزار شهدای میناب میرفتید.
اگه محصول آمریکایی کیفیتش خوب باشه میخریم یعنی چی؟! یه کم بهتون بربخوره
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66762" target="_blank">📅 15:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66761">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTaPbKf9oHd9-yFeli9YTFo2Dd3W5FYKJIbiDY2enpN5X_EmW6wOShAyTMqTGS4T7mPtt59usRsSCPuL9EmIPWoSES_QbrwkDBsGLUFm7ejKDFG3t4VBTPPVGdEmXpv1no4OyCSyNVAlky3cxJy0BZSZKRKgLrDzwRGHwORs-eUthIY70TCzSmun7cdtcVLSoKAQYBdkhTkLKCM7rLa8Ybm7T1bI6uENO3V3keN2yZucwkkKjLjxJT-R6l8YBKCfDhNoEbhbOjPzV4VngE37mePBgajzlpyQsNgjtGlzt7EJwAGw8v1unuO-m9zOQ1zpi9gcTQAxjXIdUzo5hq70ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله دنیا جهانبخت پاشده رفته کربلا عرض ارادت به امام سوم شیعیان
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66761" target="_blank">📅 14:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66760">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPhYP2YL78qk-dVGbKZ838NCmv0OSPkwPeiToGiR8AYb_qK3wGMCSaFQ4_3NQDbPg4Tg3algcAJLOUbmWOClb2vhOi2hjAwDskiPSoWqB7LDuvbBroAHGRsNb4faOb_YCvwyuJQ0LQrJhhOAomADlqGdnKo4jPyJDuqWxK19EXemAoJ_h50e86VTTnRwHpIoLC8oqcZLtgOcqn6WJa-F5IreLkRg3J2A_saxqaMLy-vwgTjmulFahz67Z3-9_hcmfL7OutyYZ20T7w5m8RUzl5Y4fgk0tw5UUsXf0CQBZnnbG12nISnvPZ-vAySRxmvEsoTxknucd1EsHXuzvZaZCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران در آینده‌ی قابل پیش‌بینی به آژانس بین‌المللی انرژی اتمی اجازه‌ی دسترسی به سایت‌های هسته‌ای مورد نظر خود را نخواهد داد. چنین بازدیدهایی مشروط به پیشرفت قابل توجه در مذاکرات است. تبلیغات و تاکتیک‌های فشار بر محاسبات ایران تأثیری نخواهد گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66760" target="_blank">📅 14:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66759">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=VPE6N0ak6wmHCEBES48VNlIcrTJcPAB2xzsMmexboM40tAITSy2ZshzZgV7zST9f-BDb1DKzpJpkMQVD3KnnSyCOPkSai9Vij5ZK3ce31Wddo3kG2YRSG396nmaXNmjudh2Z0udqYNL-_LCrWKXzpYTg4PKh-i4yCpupBR9sis8G48Rx_eeAKwtEXmtYofrKYXkBdr4-8tSoW6k1T5zTZe83I_19R2vAtv0aCcNFo8CqiVPiz4kJz2XBveh6vb0ftw9FuNQvENMLOoKyfedYUBVhBjqyqKsAvWvIvwXCD-Zbif8P1eLHKgIkG_LQIg2Das2YqRn6EFWXaKjMPG16jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=VPE6N0ak6wmHCEBES48VNlIcrTJcPAB2xzsMmexboM40tAITSy2ZshzZgV7zST9f-BDb1DKzpJpkMQVD3KnnSyCOPkSai9Vij5ZK3ce31Wddo3kG2YRSG396nmaXNmjudh2Z0udqYNL-_LCrWKXzpYTg4PKh-i4yCpupBR9sis8G48Rx_eeAKwtEXmtYofrKYXkBdr4-8tSoW6k1T5zTZe83I_19R2vAtv0aCcNFo8CqiVPiz4kJz2XBveh6vb0ftw9FuNQvENMLOoKyfedYUBVhBjqyqKsAvWvIvwXCD-Zbif8P1eLHKgIkG_LQIg2Das2YqRn6EFWXaKjMPG16jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
یادداشت تفاهم اسلام آباد به اعلام شکست آمریکا تبدیل شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66759" target="_blank">📅 14:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66758">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJJryT84G7gJNVxlnBCdtMd92J0cCfvnynnpqLkFgrtNtturw6CJInEX9i8vlsDVbdDnnQeffow_n6FZu757N4wTbagGjv9MTy3xGS27KRPMm-lmjVSdnSESInzojZqxZMAtlTzgiMslkNgUzbXhod7Juu3Z4CsQFhRNSMXD8ug6xwu31MnseK0m3HccdnZorxXPAwQcQy7YelXldwv8fdBe106vsIVtyJSTPCV43UNefbDtd5UJ1F2A9up05k0KO2KdX5UXZUttPD2STz-UMf3YEpjoJLdj533AU2m7Pdp5ajmJwsom91X3X8pb70ab3YOmF6G9k7tNyJWnTZXqDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت فست فود برای دو نفر، قیمت سال ۹۶ !
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66758" target="_blank">📅 13:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66757">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=ajb3x8NIr1r_opEySAfxknAZC8hwcpQYQuLgOoFXOUUbf1VyIGz4HOLXSD0Jdc2_aCTck13x9Ea8tRvh043xh2umdH6bmm8RTyph7kVxlCKC03hxu0Y5vS5WvDvRsgiIn8690GePjSMdIh4Yp0-V2jPX4SpFbT4AnAyaNfICk1mZGHLrg2UgJ9Lm-3gu__zTLTipmUm9VS5pzHZYfCXbESNsrYIV0-Lc5_jumPdFx9LCz-BCVQ0OayOUPotZTvJJ2YXO8Vop1K08d0AusEnImLF5RrIU3o0SFyK_5jViR8LUqH55kzE0JUjL0VgO1Qmf1VQHIhXhNC-cOEe9DmO9zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=ajb3x8NIr1r_opEySAfxknAZC8hwcpQYQuLgOoFXOUUbf1VyIGz4HOLXSD0Jdc2_aCTck13x9Ea8tRvh043xh2umdH6bmm8RTyph7kVxlCKC03hxu0Y5vS5WvDvRsgiIn8690GePjSMdIh4Yp0-V2jPX4SpFbT4AnAyaNfICk1mZGHLrg2UgJ9Lm-3gu__zTLTipmUm9VS5pzHZYfCXbESNsrYIV0-Lc5_jumPdFx9LCz-BCVQ0OayOUPotZTvJJ2YXO8Vop1K08d0AusEnImLF5RrIU3o0SFyK_5jViR8LUqH55kzE0JUjL0VgO1Qmf1VQHIhXhNC-cOEe9DmO9zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤯
بلندترین پل جهان که به یک آبشار عظیم تبدیل شده است؛ شاهکار تازه مهندسی چین
تصور کنید روی پلی ایستاده باشید که صدها متر بالاتر از کف دره قرار دارد و در کنار آن، دیواری عظیم از آب از دل کوه به پایین سرازیر می‌شود. این دقیقاً تصویری است که این روزها از پل «هوآجیانگ» در چین توجه کاربران شبکه‌های اجتماعی را به خود جلب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66757" target="_blank">📅 12:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66756">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=IrlBIa9eZpyFN5Hm1wo8BKm9JfVq8oBhp_8sQ2Rfzin5FgVlraJx_2E-A8y10TrETW1KkRppQbAsnGMJ1bvE7AMU2zF6VpSSa__fN-F5ZxM8SpDst2OaKlMDEt2imaJgwWvxlqvCdmijgS_bDQu4XRBy-5xxpfr_OUxV747pI8CxXZLohK1CngNAIJi8ExUUZIdkt9ZsHE_7s10kuh_qae4OWR8TLF7_Fhz51azMtxdIYa1t9XNTR4a6GW4z1TLJg3-PhSG_TzRBM6YmAhYzQDuJAu9qcxvK3eRAW2Td8GWQ-n-y6qHe9ninQ6D9EF0tVfBQXkqSH9SE4AU9rhrC4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=IrlBIa9eZpyFN5Hm1wo8BKm9JfVq8oBhp_8sQ2Rfzin5FgVlraJx_2E-A8y10TrETW1KkRppQbAsnGMJ1bvE7AMU2zF6VpSSa__fN-F5ZxM8SpDst2OaKlMDEt2imaJgwWvxlqvCdmijgS_bDQu4XRBy-5xxpfr_OUxV747pI8CxXZLohK1CngNAIJi8ExUUZIdkt9ZsHE_7s10kuh_qae4OWR8TLF7_Fhz51azMtxdIYa1t9XNTR4a6GW4z1TLJg3-PhSG_TzRBM6YmAhYzQDuJAu9qcxvK3eRAW2Td8GWQ-n-y6qHe9ninQ6D9EF0tVfBQXkqSH9SE4AU9rhrC4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه سرباز روسی که با پهپاد اوکراینی روبه‌رو شده بود، از اپراتور درخواست کرد که اول دوست کنارش رو بزنه تا بتونه سیگارشو قبل مرگ تموم کنه
اپراتور پهپاد درخواستش رو قبول میکنه، اول سرباز دیگه رو میزنه و بعد سربازی که درخواست کرده بود رو میزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66756" target="_blank">📅 12:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66755">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=aE8vlkT6eyu11hx6b_fsp9w4BsbM0jgXLxn2rsYHGkgdptv3hovJhZi0BiimBDEOybc6TNBtaq3Bao8pAoGAgKEtK_k99t2Gohj1LQCd4yPyutIusFjAZFYo3CkVnV7LfqOjzislVGJ7Ieh2KejvADI9w7Le9XW79uOcquyRknbyBZTN3DxAlb_X1RB1wdk9xpr0N3i462phZqrQgA163GJAzCRQ2bD9lFgjq4UTAjmiJANfQtmvSXnxKVuQhjTYLfFnRwf44gyh0p9GJfuSLGaUTcCWhETuNn5AvzCj78YHbdTFsCGnyedthJOyc01EYEQ6nF-MAnMX-RVNMbYOqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=aE8vlkT6eyu11hx6b_fsp9w4BsbM0jgXLxn2rsYHGkgdptv3hovJhZi0BiimBDEOybc6TNBtaq3Bao8pAoGAgKEtK_k99t2Gohj1LQCd4yPyutIusFjAZFYo3CkVnV7LfqOjzislVGJ7Ieh2KejvADI9w7Le9XW79uOcquyRknbyBZTN3DxAlb_X1RB1wdk9xpr0N3i462phZqrQgA163GJAzCRQ2bD9lFgjq4UTAjmiJANfQtmvSXnxKVuQhjTYLfFnRwf44gyh0p9GJfuSLGaUTcCWhETuNn5AvzCj78YHbdTFsCGnyedthJOyc01EYEQ6nF-MAnMX-RVNMbYOqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
دیروز تو دولت اسلامی عراق یه مسئول دولتی حوصلش سر میره و اینجوری با منشی‌ش کارای ناخوشایند اسلام از جمله
لب گرفتن و ساک‌زدن
رو انجام میدن. میگن که این یارو اخراج و بازداشت شده
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66755" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66754">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b320081976.mp4?token=K2Et4YBnEN74Ji75jlIp4B9LAfBrX2TyrF6hICxc6U5kNfdpvxPbAiSsp9k2Xk-47Y4OLDS9t9lB1J-xl3ZFA69tQZ-rkK_Hwf1WNoUYxG8p00_pTKw532Sz_mOvwGPaa1a9UE-yuTpi2s2umBhJK07jVTw4rjuBVMrcsV2gyj5JTLyf5LTux5qMnx5PjSW3ypDy-RJm6UOIffwCNvYMjKgpnypeZDChmjWTVk66iMuOw0YRCTsJ8_3M1M6KA7EJBNeTncIHmn1rxT0DMWhtR0_38FfG9nmSZNPdK4qb0BRScMJuR19xS26TPmpF1h_3m9kFyko4W3RYIPCebZEMog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b320081976.mp4?token=K2Et4YBnEN74Ji75jlIp4B9LAfBrX2TyrF6hICxc6U5kNfdpvxPbAiSsp9k2Xk-47Y4OLDS9t9lB1J-xl3ZFA69tQZ-rkK_Hwf1WNoUYxG8p00_pTKw532Sz_mOvwGPaa1a9UE-yuTpi2s2umBhJK07jVTw4rjuBVMrcsV2gyj5JTLyf5LTux5qMnx5PjSW3ypDy-RJm6UOIffwCNvYMjKgpnypeZDChmjWTVk66iMuOw0YRCTsJ8_3M1M6KA7EJBNeTncIHmn1rxT0DMWhtR0_38FfG9nmSZNPdK4qb0BRScMJuR19xS26TPmpF1h_3m9kFyko4W3RYIPCebZEMog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ای که مسعود توی مراسم کاشت نهال در پاکستان بیل رو ول نمیداد
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66754" target="_blank">📅 11:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66753">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44438818f9.mp4?token=NF_5vbSHzzur7RgWeJ5NTMak23iyGmSxYRkaX1MNNjomXGSvZ_vzduI-E_EkYJTxlfPs2eEd8GEByihlqyzATn2aiYU3DwKBWbwmc3We0QR6EsHzPK87dHqUE_3-NbuRF8jnJoswvjawaXVW3azVu8idfSE5kYwgV2zqxncrpvJxNJwyV_ukIS9gSt6lDjsG4MfcaD4P2dD71iDNq_0LVvVmjcUP9yiUjKE59GiO-0yBhMZg2H0uXTQfR9F4ffRz9Er5PSVg30DbKs5Zb9AgO8l-kOXHxbnnfB6bgsbojFYPsXvpoY9mmY092lT3lfAtfnF8cHIzWmhHaLPma6a6FE_LbAnfm_rwFx6QiBBJHi8A1EgAoTiHtXPKXdyDM6iLm5a0RR-aKAQFfKOoGuzbbp9XVhtmwUx8QykOOZ5jSuVeQ3pNUCmgKCW9KOh5VFAV1yPVIXofeMraPZXbkmRx11HkmTMMcs12NhDt-u1watPrMxVbvxVLSARslrxQq8roPlkAD2e9K6vdIRGKED8wZUHR7toOcrUDBx56RVQkma6d6iQP8WYXCChsDjisGnoCNvOdjR91VYBml7bsn0qHVX0HboYAi-fqGsOhz65p3imx1i1yEnRUTIGhscf79bZ0XOCoTdy3N88Cgcz2cMRl7AMke3QRemotISzbTxdMe7Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44438818f9.mp4?token=NF_5vbSHzzur7RgWeJ5NTMak23iyGmSxYRkaX1MNNjomXGSvZ_vzduI-E_EkYJTxlfPs2eEd8GEByihlqyzATn2aiYU3DwKBWbwmc3We0QR6EsHzPK87dHqUE_3-NbuRF8jnJoswvjawaXVW3azVu8idfSE5kYwgV2zqxncrpvJxNJwyV_ukIS9gSt6lDjsG4MfcaD4P2dD71iDNq_0LVvVmjcUP9yiUjKE59GiO-0yBhMZg2H0uXTQfR9F4ffRz9Er5PSVg30DbKs5Zb9AgO8l-kOXHxbnnfB6bgsbojFYPsXvpoY9mmY092lT3lfAtfnF8cHIzWmhHaLPma6a6FE_LbAnfm_rwFx6QiBBJHi8A1EgAoTiHtXPKXdyDM6iLm5a0RR-aKAQFfKOoGuzbbp9XVhtmwUx8QykOOZ5jSuVeQ3pNUCmgKCW9KOh5VFAV1yPVIXofeMraPZXbkmRx11HkmTMMcs12NhDt-u1watPrMxVbvxVLSARslrxQq8roPlkAD2e9K6vdIRGKED8wZUHR7toOcrUDBx56RVQkma6d6iQP8WYXCChsDjisGnoCNvOdjR91VYBml7bsn0qHVX0HboYAi-fqGsOhz65p3imx1i1yEnRUTIGhscf79bZ0XOCoTdy3N88Cgcz2cMRl7AMke3QRemotISzbTxdMe7Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💢
سنای ایالات متحده با رای ۵۰ به ۴۸، قطعنامه‌ای که توسط مجلس نمایندگان تصویب شده بود را برای جلوگیری از اقدام نظامی علیه ایران مگر اینکه رئیس‌جمهور ترامپ ابتدا مجوز کنگره را کسب کند، تصویب کرد.
«همچنان ترامپ میتونه وتو کنه»
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66753" target="_blank">📅 10:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66752">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=H0lbUd_N4DfW-h0uoyCYCmn1BEZIGJPg8we6ZyXR8xypYoVYZGSK3Z3dxURT-VVN2J41rv97zqv4j9re1dt1u_mqfmlUiJGPfv5UlKCmfQe8KTf_fk_V9txly0k4n6d8ItTX7kU85hJmrHRwv0VIapL7S2IkCkDlFiKDzXFOenUl9jNjLsqzKJjANJje9gRhn3_ZGqlMYJwmEQXXh-7ubTNoYtkSPiC_-EindIMNj4fui1qRlAaikgj9ZSKGTCw3K1li5spPFGnOAYv8neE8ZY0oRUmoD2QeTteClFUQnzIagg3iyXGUDtUmm3eRR95w6HZiFBW4VzClBZwhhcUjUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=H0lbUd_N4DfW-h0uoyCYCmn1BEZIGJPg8we6ZyXR8xypYoVYZGSK3Z3dxURT-VVN2J41rv97zqv4j9re1dt1u_mqfmlUiJGPfv5UlKCmfQe8KTf_fk_V9txly0k4n6d8ItTX7kU85hJmrHRwv0VIapL7S2IkCkDlFiKDzXFOenUl9jNjLsqzKJjANJje9gRhn3_ZGqlMYJwmEQXXh-7ubTNoYtkSPiC_-EindIMNj4fui1qRlAaikgj9ZSKGTCw3K1li5spPFGnOAYv8neE8ZY0oRUmoD2QeTteClFUQnzIagg3iyXGUDtUmm3eRR95w6HZiFBW4VzClBZwhhcUjUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجیا ملونی نخست‌وزیر ایتالیا:
نمی‌توان اجازه داد ایران به سلاح‌های هسته‌ای یا کلاهک‌های هسته‌ای دست یابد، به‌ويژه با توجه به اینکه ایران موشک‌های دوربرد دارد و این مسئله را به وضوح نشان داده است.
ملونی تأکید کرد که این موضوع تنها به ایالات متحده یا کشورهای نزدیک به مرزهای ایران یا اسرائیل محدود نمی‌شود، بلکه مسئله‌ای است که نمی‌توانیم آن را اجازه دهیم یا تحمل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66752" target="_blank">📅 10:03 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
