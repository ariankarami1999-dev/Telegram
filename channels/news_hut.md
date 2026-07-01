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
<img src="https://cdn4.telesco.pe/file/dZgscLsOJWDZJWaENpraM0Vmeti-gSV910qZ7AmchnSSzfgu5t1fm_WcOp3yVF_zQea3eJPGaBK8R2DKsUmTSgIDeJPYpYVEuuNTj_7bcUg5IPEm-j_uEWLBQIV9zNWSygz-zyE07ICylBZK_R6TY-s97Bz3gn4BFOo6kMM1udyxh3e23EYJJoE2Xf1T8L5xUu-C-gE-iIpYJUJWe4KKDjp_GhKDA0sZvSV_ULbQFGUI42J5CcOqWPN-m79qldGh451HsOZD4ELIgHcycADi3_PYervWGfulEAKfj0FTWjCwHtI5XFIO3uJivAPewBXS9xP-VVDdTYGaJArHWm99YQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 215K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 00:15:32</div>
<hr>

<div class="tg-post" id="msg-67165">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
🚨
نماز میت بر جنازه علی‌خامنه‌ای توسط یکی از مراجع تقلید خونده میشه و خبری از مجتبی خامنه‌ای نیست
@News_Hut</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/news_hut/67165" target="_blank">📅 00:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67164">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44959f900a.mp4?token=tF9i-9Gv0_PBo7O9E4j_8cMZsDOuOgOm2v2hEXWZ6nmjpRuscDWGs2hty4-ptL5SANvJKMZChAabFX4uwJvdx-F-aK0Ppz-s8zgabY0Y_Qo1fUbVRiai11X7WlWz-czHgBeAl-3H65ipX5brbCdyySx24nVZrgzZL6iCUKq6H8-S8XX3KIyQu2tQ2aUrWD2yBQdyt_Yxp2RceN3Vg1tZ9_ac1-oG7t1XQTwQeAdm7Egro2PUzsJLyLE30p8IjUFEE_LTyWHTzlvRWDzAy9K6yPQg1MBTGNzQVyOSFMVczO0EOyW9oWBUpX2P7CpcaYShGw9ebU_Ql3egQ9JWgt7rsw7og210w_Lmw6RP6XkW8zokDRjoauo_vMr7xV_MCf8IWNOmKYsdE-A4bFSJu7SYypHz5ZZ_0MClvp7Xyu939YwZG7rCt4SLY3chgwEhcOvk5zDqZI_z5_krD4TkYoWi2-AbNYYhA90hBNn7SFw03JxHNZfnjFlu_Pt-zmvYwnIMkdyX2UqE1pE5a9xAJRVCx6Gn6WUA0qnlm9lfVw6OAqQAUkpqJiVdsYN_t_l_D2xUX5TqaJ5R6Wr5HOQjzRxoLglujGg4qb05vCfH3bef2Sg7rINDeZOHYT-bxLOt1Gp8eClgP9JvIDFCo0ilSiMw-Fs-OqIG6YAfEjQudhk9XHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44959f900a.mp4?token=tF9i-9Gv0_PBo7O9E4j_8cMZsDOuOgOm2v2hEXWZ6nmjpRuscDWGs2hty4-ptL5SANvJKMZChAabFX4uwJvdx-F-aK0Ppz-s8zgabY0Y_Qo1fUbVRiai11X7WlWz-czHgBeAl-3H65ipX5brbCdyySx24nVZrgzZL6iCUKq6H8-S8XX3KIyQu2tQ2aUrWD2yBQdyt_Yxp2RceN3Vg1tZ9_ac1-oG7t1XQTwQeAdm7Egro2PUzsJLyLE30p8IjUFEE_LTyWHTzlvRWDzAy9K6yPQg1MBTGNzQVyOSFMVczO0EOyW9oWBUpX2P7CpcaYShGw9ebU_Ql3egQ9JWgt7rsw7og210w_Lmw6RP6XkW8zokDRjoauo_vMr7xV_MCf8IWNOmKYsdE-A4bFSJu7SYypHz5ZZ_0MClvp7Xyu939YwZG7rCt4SLY3chgwEhcOvk5zDqZI_z5_krD4TkYoWi2-AbNYYhA90hBNn7SFw03JxHNZfnjFlu_Pt-zmvYwnIMkdyX2UqE1pE5a9xAJRVCx6Gn6WUA0qnlm9lfVw6OAqQAUkpqJiVdsYN_t_l_D2xUX5TqaJ5R6Wr5HOQjzRxoLglujGg4qb05vCfH3bef2Sg7rINDeZOHYT-bxLOt1Gp8eClgP9JvIDFCo0ilSiMw-Fs-OqIG6YAfEjQudhk9XHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قالیباف خطاب به مخالفین مذاکره: بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید
نه در دیپلماسی کمک می‌کنید؛ نه در جنگ!
@News_Hut</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/news_hut/67164" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67163">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeEbQi8T2PC_sQqd4hKtH5vzOSgidP3JASufOrlidF1eEZaY4o-yRsCLKsjT_3fsH-K5zptddt4LtVRZ-ioni_Y9E6UbclXyeuRixzMGabj5ChOKHV5V5qSkdn0mX4IzM34HopQfn2DffcN59hq_qWfbvHSs4ExMnLPsIbYkDB2xUeBWhE4SuJUDLWvuoIXfaK7bpN1TYEtJ616qILHX7IStR-60MRKgkqH0wkfyobryJ0wKaeGm8K8fk40BzqS-ypFN8nSHfGw4wBiinMsnt70YY-MhmmaOhguLJFvOs7KgtfgDp5_HeiGHf_G0NkheESvTscOdaiPUnpa41kv0uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
برخی مطرح کردند که چرا اعلام شده ۲۰ میلیون بشکه نفت در اختیار فلان مجموعه قرار گرفته و این موضوع را افشای اطلاعات داخلی دانستند. اگر بار دیگر نیز چنین شرایطی پیش بیاید، نه ۲۰ میلیون بشکه، بلکه ۱۰۰ میلیون بشکه هم در اختیار آنان قرار خواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/news_hut/67163" target="_blank">📅 23:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67162">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=XDFDKIXpOjeRpaQCs5lqIhMbjDJf2S6fPFf1Z12CkBVOIxHnAlkzXs2zkGci3tYawplQ-3J5HPlKCNo1pkq0hkL_a_CHqBTGfegG4103-zxJGyf0gk6BNBq1mvxmWc_voQUGzwZQOdNcuTrYQxVGY5Jt6nDt2NQW9AT3hucP2j0C_3E8GffqEmONerOMULdTJToCDqrSlu2ufgRM88jqjOEW-Clewjw-CmL3VxkSCxyESx__s-Q1iJYx0ZcULGU2KLJHA4pgNHgr9tGLN6pX0kBTBSzdNGNhEzcyf_Hzi-p4vF0KWPV-YlCKiqCM-zK-xFFHka83-xNn73uyrvM-5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=XDFDKIXpOjeRpaQCs5lqIhMbjDJf2S6fPFf1Z12CkBVOIxHnAlkzXs2zkGci3tYawplQ-3J5HPlKCNo1pkq0hkL_a_CHqBTGfegG4103-zxJGyf0gk6BNBq1mvxmWc_voQUGzwZQOdNcuTrYQxVGY5Jt6nDt2NQW9AT3hucP2j0C_3E8GffqEmONerOMULdTJToCDqrSlu2ufgRM88jqjOEW-Clewjw-CmL3VxkSCxyESx__s-Q1iJYx0ZcULGU2KLJHA4pgNHgr9tGLN6pX0kBTBSzdNGNhEzcyf_Hzi-p4vF0KWPV-YlCKiqCM-zK-xFFHka83-xNn73uyrvM-5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله پسر سردار طاهری به پزشکیان:
مگه نفت بابات بود که می‌گی ۲۰میلیون بشکه نفت دادیم به نیروهای مسلح تا بجنگن؟ اگر نیروهای مسلح نبودن ما نمی‌تونستیم اینجا شعار بدیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/67162" target="_blank">📅 23:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67161">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=rZudH1BrsrnPKWAgesSDejGtQsB1lakyDOPWRMo4LAkycWr-amMHuihK4NPc1UMXyEJO_FcC6ZH0bs9KWinjrliIc0qnu5fYdPhnzZLgG7ZRHn3pxibbJKE4u50o22a9URMGyafVQAJJxcBapu3_q7i2Mwe1a4leKiyXUHBEY3K_nPUJp0LIwTdgny2TLwxiMWtzCJyLFNudV8y3X2s0iGYaQR23pLcsAV-SK253moRkajXdYyRLMfLSbXjxLXd30ZAVDKSzUWktksLyqDwEZK8s0pujO0yfI5nrptisYS5uugR_7aQPgzccUzQr9IqorYUXRJAlYhBFHm_s9HFmsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=rZudH1BrsrnPKWAgesSDejGtQsB1lakyDOPWRMo4LAkycWr-amMHuihK4NPc1UMXyEJO_FcC6ZH0bs9KWinjrliIc0qnu5fYdPhnzZLgG7ZRHn3pxibbJKE4u50o22a9URMGyafVQAJJxcBapu3_q7i2Mwe1a4leKiyXUHBEY3K_nPUJp0LIwTdgny2TLwxiMWtzCJyLFNudV8y3X2s0iGYaQR23pLcsAV-SK253moRkajXdYyRLMfLSbXjxLXd30ZAVDKSzUWktksLyqDwEZK8s0pujO0yfI5nrptisYS5uugR_7aQPgzccUzQr9IqorYUXRJAlYhBFHm_s9HFmsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیروز کریمی:
قلعه نوعی 5 سانت رو تحمل کرد 10 سانت رو تحمل کرد، 30 سانت رو دیگه کجاش بذاره
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/67161" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67160">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=G2hmaQQMk6cm6Mu-h0cBwmJs-BDvwrbVkRO6MpiSVhZMIzVKS3lNhhAdFTAItTVf_HR5d-elmbQRuLvV1XWr0bzDEuhI_VGTtQZH4EfriPttgIwiMC-ixRGx88AqSGMGFKM88G6qHfoQ8aaTjyfi38mtlFPUmpkSM1XV_yc0ZROPbCCrHsLGVb8leT4hObhoN6ZJVYFEsU6J5Y046cQ97-Dfius3VZUe2AP_j3hCxHkSRL-KY4odabqDKTam2jGSTr0EVjQOeLaQA3r_KeNUMdkeS2SwcAsjx7xIrEmJ_tRjEGAyR2bNAXCts1cDccNjJ7tVn7M2EN1YZddiVk-raw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=G2hmaQQMk6cm6Mu-h0cBwmJs-BDvwrbVkRO6MpiSVhZMIzVKS3lNhhAdFTAItTVf_HR5d-elmbQRuLvV1XWr0bzDEuhI_VGTtQZH4EfriPttgIwiMC-ixRGx88AqSGMGFKM88G6qHfoQ8aaTjyfi38mtlFPUmpkSM1XV_yc0ZROPbCCrHsLGVb8leT4hObhoN6ZJVYFEsU6J5Y046cQ97-Dfius3VZUe2AP_j3hCxHkSRL-KY4odabqDKTam2jGSTr0EVjQOeLaQA3r_KeNUMdkeS2SwcAsjx7xIrEmJ_tRjEGAyR2bNAXCts1cDccNjJ7tVn7M2EN1YZddiVk-raw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: آیا می‌توانید قول بدهید که آمریکا قبل از تمام شدن ۶۰ روز تفاهمنامه، دوباره وارد جنگ تمام‌عیار نشود؟
​
🔴
جی‌دی ونس: ترامپ تا وقتی که مجبور نباشد، نیروهای نظامی را دوباره به جنگ نمی‌فرستد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/67160" target="_blank">📅 21:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67159">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل‌ از مقام آمریکایی:
در مذاکرات دوحه تفاهمی حاصل شد تا اوضاع هفته آینده آرام بماند تا در اجرای تفاهم‌نامه پیشرفت حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/67159" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67158">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7lhaT-Ic-nzi2RP-gJ6aoXDmytJ48npqmADdjt_pvuZlI8GynlaWq6dyaWY-_xvo4RMN9JfbPQoPMz5JwlivucEEubEBlXAYXwg2KOySckxSlw7Pn2vdl0puQoqOIM9E7mOKZ_GupbKhCPNE8zeVeL9xeRXpsnw2njNO3SAMAzs1kd2h-7Oy0wwwh8pTZHH6sR9bvrZgBPthyLAxM1Z_WaAFuSF_fj4OvLgeeCG2GU8BF3gM4B2Le2gl125KkXy2nghuWQJOKQIKvXeHPUEtJJ4o1a1r586EFLAMY2UNP3uBZWm0firfaUUaTrBPIUilhXZokXyNV9dLizrUNmPBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:همزمان با از سرگیری مذاکرات در دوحه، ایالات متحده تلاش می‌کند تا ایران را از پرداخت عوارض منصرف کند.
مذاکره‌کنندگان آمریکایی و ایرانی در دوحه برای مذاکراتی با تمرکز اصلی بر تنگه هرمز حضور دارند و دولت ترامپ مدعی است که ایران از توافق هسته‌ای سود بسیار بیشتری نسبت به عوارض عبور و مرور در این تنگه خواهد برد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/67158" target="_blank">📅 21:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67157">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=XsgOeTfRZNAtgj1_2wzfhS15JGFW5YsLBTtdna1h08tYT7GoFF4OsROpk13MficBFPbR3zL49Z273nSAaprgaAWoyO0hwMATzqshhFq2wj5SqDq_J-vcE2ujbdGSfm-c567HHY8OP-kTbusnApPG5jd7c_Q21K-1ZypcjQTohNJa2JMw0-tMrEXk3QM9piqeZ4SdQBytcp3XXBjLZ7S4kFYj6KuUZyetEihcFbTYmsHOROJr1r49HSdAqJbHqlPDA_mbGrxLz2zEvM1fy55w31wnPtzx3hkePkOPeaW1gkuXOvvoeQUNMmr10ERLGLlN3azw7A3SF5Q_8AOP6CZ4_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=XsgOeTfRZNAtgj1_2wzfhS15JGFW5YsLBTtdna1h08tYT7GoFF4OsROpk13MficBFPbR3zL49Z273nSAaprgaAWoyO0hwMATzqshhFq2wj5SqDq_J-vcE2ujbdGSfm-c567HHY8OP-kTbusnApPG5jd7c_Q21K-1ZypcjQTohNJa2JMw0-tMrEXk3QM9piqeZ4SdQBytcp3XXBjLZ7S4kFYj6KuUZyetEihcFbTYmsHOROJr1r49HSdAqJbHqlPDA_mbGrxLz2zEvM1fy55w31wnPtzx3hkePkOPeaW1gkuXOvvoeQUNMmr10ERLGLlN3azw7A3SF5Q_8AOP6CZ4_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«روند خلع سلاح هسته‌ای ایران به‌خوبی پیش می‌رود... بازار سهام تقریباً هر روز در حال ثبت رکوردهای جدید است. قیمت نفت به‌شدت کاهش یافته است... و اکنون از زمانی که من حمله به ایران را برای جلوگیری از دستیابی آن به سلاح هسته‌ای آغاز کردم نیز پایین‌تر است.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/67157" target="_blank">📅 20:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67156">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1792b01078.mp4?token=YdVFFGXbuGn3SnZrpmnwSsiSVmS0ZtltsLbQ7DLbM7-KGJxZOr_6gXto7KdaeRUI-8WILn3bj2ddifVrRlXpYVhuFG9RwsGooP-AIyK1TsnHhCqPoBvcKQZgxQZcgS3sqnWRZwuUFEo-YrPHiKEGEoa5proFsCPciQGjU6ZDkMh9Pwoic-sd4BBMEOIzoOs5x1tExvFKuQ4HarK8hxbGMxhHPeILjbXKwU-fdMFV9boteggfkVylzYAKwJ1ak-cEpIh4l7wIYxDQcZ0yL_ZGgfJ1wWkBfTkSFt1cZV7x0uIWU5a9NvhWs5ARfv6SOptzU_i6L6VgIm3ymV9u0TvMAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1792b01078.mp4?token=YdVFFGXbuGn3SnZrpmnwSsiSVmS0ZtltsLbQ7DLbM7-KGJxZOr_6gXto7KdaeRUI-8WILn3bj2ddifVrRlXpYVhuFG9RwsGooP-AIyK1TsnHhCqPoBvcKQZgxQZcgS3sqnWRZwuUFEo-YrPHiKEGEoa5proFsCPciQGjU6ZDkMh9Pwoic-sd4BBMEOIzoOs5x1tExvFKuQ4HarK8hxbGMxhHPeILjbXKwU-fdMFV9boteggfkVylzYAKwJ1ak-cEpIh4l7wIYxDQcZ0yL_ZGgfJ1wWkBfTkSFt1cZV7x0uIWU5a9NvhWs5ARfv6SOptzU_i6L6VgIm3ymV9u0TvMAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قائم‌پناه، معاون پزشکیان:
اگر قرار باشد هر آنچه رهبری می‌گوید اجرا کنیم که دیگر نهادی نباید وجود داشته باشد
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/67156" target="_blank">📅 20:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67155">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=u6yLzMW0FIlFugXaN476XM-9Y-9U2ikHLmne3vpdT9sp4Jgm46xVZrvdMwBySyI5q7Hhpxj2SfezHpSZI_AsFN7lpKmoSiDqQ3X4eFXeqagYY8uq46rZ1xQMaGEITi2ulEqHOJaCTj5th6zQGQ2srb3caYSqBarjkeFCS9OXGe82cwUkcl5Oic9puslo1glcdzclP7nPYEVoeiCYhI4byVFrqnO9rBllOPM-uIS7IPAN0amwn4z0nohl5F7il3JlAdXU8sdrxeaA36g7Df-dD7G2Zn0UxJaLYrvyOsN37wBbC3HQrvgM7biFrGNsK11UL9NlytSEbIfaXxcyrzpKOaIvdZZqFnowEZrloLWKMmpHhb6YjWNEFg0pTRedWFoNcfAhMrct9pMtQrOnPWSfp8wn26lN5wZqCINYZzJZYgxilWZGVQzYn4zU__p9WXsnvFh6ci3a0w-yU7cPGJWTHi5xB_GfB_dcyI-FvIRpaEZFCSvukSlWjW_Mcysevz9oWQ1cgKXc6vHFbW0nRAeMOu_UWwOlBsVgUPm5p979bNbZ1A4oJzRjfqpm7Mq9WooX7WprgRB4T0Ka6W66wgQiEBXqnGZQ5ImKnTm9z8C9N_B2-b02iM_LZJprwbP5pxxl1v1RFxpDhOKMedtWzXRnmRiSMqxXNhUew9PbZWIAVoY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=u6yLzMW0FIlFugXaN476XM-9Y-9U2ikHLmne3vpdT9sp4Jgm46xVZrvdMwBySyI5q7Hhpxj2SfezHpSZI_AsFN7lpKmoSiDqQ3X4eFXeqagYY8uq46rZ1xQMaGEITi2ulEqHOJaCTj5th6zQGQ2srb3caYSqBarjkeFCS9OXGe82cwUkcl5Oic9puslo1glcdzclP7nPYEVoeiCYhI4byVFrqnO9rBllOPM-uIS7IPAN0amwn4z0nohl5F7il3JlAdXU8sdrxeaA36g7Df-dD7G2Zn0UxJaLYrvyOsN37wBbC3HQrvgM7biFrGNsK11UL9NlytSEbIfaXxcyrzpKOaIvdZZqFnowEZrloLWKMmpHhb6YjWNEFg0pTRedWFoNcfAhMrct9pMtQrOnPWSfp8wn26lN5wZqCINYZzJZYgxilWZGVQzYn4zU__p9WXsnvFh6ci3a0w-yU7cPGJWTHi5xB_GfB_dcyI-FvIRpaEZFCSvukSlWjW_Mcysevz9oWQ1cgKXc6vHFbW0nRAeMOu_UWwOlBsVgUPm5p979bNbZ1A4oJzRjfqpm7Mq9WooX7WprgRB4T0Ka6W66wgQiEBXqnGZQ5ImKnTm9z8C9N_B2-b02iM_LZJprwbP5pxxl1v1RFxpDhOKMedtWzXRnmRiSMqxXNhUew9PbZWIAVoY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی‌ونس:
«من واقعاً فکر می‌کنم ایالات متحده، فارغ از اینکه مذاکرات در نهایت به چه نتیجه‌ای برسد، در موقعیت بسیار خوبی قرار دارد.
اگر مذاکرات موفقیت‌آمیز باشد، که بدیهی است ما می‌خواهیم چنین باشد، با ایرانی روبه‌رو خواهیم بود که به‌طور دائمی دگرگون شده است.
از سوی دیگر، اگر ایرانی‌ها رفتار مناسبی نداشته باشند، برنامه هسته‌ای آنها همچنان نابود شده است، توان نظامی متعارف آنها همچنان از بین رفته است و ایالات متحده نیز در مقایسه با ایران همچنان در موقعیتی بسیار قدرتمندتر قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/67155" target="_blank">📅 19:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67154">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=pTZleJ4O-YnTke34vt2LDWdZ4JlnC7Gmen3tB56fTkVVhCX2QQvX48fmpbM75avOdOt8E2AM4tuaqBHUJTPpsM1SxRgLNXRo1qhwKVugskbHLvD4kefTZn8UhrkNU_kmVVstOiz2BWNIXptW0ykNjQ2UosNYn5FZugkYze8jJJXYbLZ5Wl_vEVU3hsl_cqnqTbglOVWrddFoHMrPCi6ETUJ-CS8k3C6pEMH05xVQBHeg1KiOmcwQqmKOmOLt_qiqmrb5p-_zRSRS3LkGtCggSE9oDtPHN1W0WL0iYZ5lg6vGcYOZFvnOrhPxKgEq66oJdQdpjvsJfdvdoEP0H91DRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=pTZleJ4O-YnTke34vt2LDWdZ4JlnC7Gmen3tB56fTkVVhCX2QQvX48fmpbM75avOdOt8E2AM4tuaqBHUJTPpsM1SxRgLNXRo1qhwKVugskbHLvD4kefTZn8UhrkNU_kmVVstOiz2BWNIXptW0ykNjQ2UosNYn5FZugkYze8jJJXYbLZ5Wl_vEVU3hsl_cqnqTbglOVWrddFoHMrPCi6ETUJ-CS8k3C6pEMH05xVQBHeg1KiOmcwQqmKOmOLt_qiqmrb5p-_zRSRS3LkGtCggSE9oDtPHN1W0WL0iYZ5lg6vGcYOZFvnOrhPxKgEq66oJdQdpjvsJfdvdoEP0H91DRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه عده کسخلِ پا شدن رفتن فرودگاه که از بازیکن‌های تیم میلی جمهوری اسلامی استقبال کنن. مثلا می‌خواستن شبیه هواداران تیم ملی نروژ به سبک وایکینگی تشویقشون کنن که اینطوری ریدن
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/67154" target="_blank">📅 19:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67153">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDJsvY-k3nQIop3kZT_kC77Fat9Mw5L827i1q2iH6STE7m1C4SqKsTLKAowN3o6jE_foJ9Ur1Bcbs3BpjpGC3Du-xidc_Mx2QroNjumzy6e_TB5Ppjgs-L0O8XrZZh-MfZAn36qJk5QDxYQX1VtiGdqF_PcQe-gbz_WVst-fKsh7fxrg1fxHh5kOXtsPUSzhx4i12LMH2he5Z5nwKW4W6Xc5T6i3Ea4MDPpmAjbPMJ5Pc_JqnXKcO1ekxxgSbxmDP-GiuGy0yZaBU24Kik0bi1O63fKjtReqmvkFTQAPVmyKQK6L4xGBiBa8lqseBQuA-MSgCqLn5mVQDtCigd35SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
به اعضای تیم ملی فوتبال کشورمان که امروز به ایران عزیز بازگشتند، خداقوت می‌گویم.
تلاش و مبارزه با تمام وجود و تا آخرین لحظه، مهم‌تر از پیروزی است.
کار علمی، حفظ روحیه، رویکرد تحولی و انگیزه بالا شرط پیروزی در آینده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/67153" target="_blank">📅 18:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67152">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=BviUrXP9ErR23H58UynfnTn3cXI6U0q-dsGpzvBJ9FjXJV1XiZ9G0HvIiSsP3n8QLJXln9F_xPlcGQq-B6GwC4hdq-8gimfPRMbZH9vq3eKYbv2nkY0edVDs34VpGOGH-teYpCDnzmpB5wddZ4j4FKXhRjmEcRNdrdkJgsSr3SNmWhQtopR8N4EitbHk8Ft1YjOk3ZH8UohW0l5mP8s_kHO6femCwxSVep_AeUEgRLGfQlhXscfKPpAE_llABhWPv8qP28D1OvEXTO36iQ_Qs6oflif0uqODpFHTf0JYwZxVGLGUSqAXTioa_DL14_JsTW5jRdmPZaUdezY67bttLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=BviUrXP9ErR23H58UynfnTn3cXI6U0q-dsGpzvBJ9FjXJV1XiZ9G0HvIiSsP3n8QLJXln9F_xPlcGQq-B6GwC4hdq-8gimfPRMbZH9vq3eKYbv2nkY0edVDs34VpGOGH-teYpCDnzmpB5wddZ4j4FKXhRjmEcRNdrdkJgsSr3SNmWhQtopR8N4EitbHk8Ft1YjOk3ZH8UohW0l5mP8s_kHO6femCwxSVep_AeUEgRLGfQlhXscfKPpAE_llABhWPv8qP28D1OvEXTO36iQ_Qs6oflif0uqODpFHTf0JYwZxVGLGUSqAXTioa_DL14_JsTW5jRdmPZaUdezY67bttLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی‌ونس:
ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی، بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/67152" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67151">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=TgTgkXCCE0s0AQZ3nirTu-6KvzCqbSDPJMh3ewQn1PIht0UP7zuAaY5j7LWZlpO63rrzXO4Gwj-1MJvwjfgaBijfpd9x-KasGnv8dPQFDGlwVSlh6F2EelkaZA5OwwMKOcZUCS83CZD_gjqJ9FL-I9lJkzICa4ofVS07p315SNfebtJ9Jesq_rNzmB0HpdPru7uGGwoP7cB99RqUA-00U7tQxdFQfkyV1blswp3RRe9mU-Iu-BqizEjhkP264EndjxwWgCSl5VpDvalwmQECWnwnQyQRWpkJkxSpEzy14CorXxUEOYAedjLFnHABnFtCKBCg0VPJhuQ9A9xtF29AYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=TgTgkXCCE0s0AQZ3nirTu-6KvzCqbSDPJMh3ewQn1PIht0UP7zuAaY5j7LWZlpO63rrzXO4Gwj-1MJvwjfgaBijfpd9x-KasGnv8dPQFDGlwVSlh6F2EelkaZA5OwwMKOcZUCS83CZD_gjqJ9FL-I9lJkzICa4ofVS07p315SNfebtJ9Jesq_rNzmB0HpdPru7uGGwoP7cB99RqUA-00U7tQxdFQfkyV1blswp3RRe9mU-Iu-BqizEjhkP264EndjxwWgCSl5VpDvalwmQECWnwnQyQRWpkJkxSpEzy14CorXxUEOYAedjLFnHABnFtCKBCg0VPJhuQ9A9xtF29AYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت‌ترامپ :
روند خلع سلاح هسته‌ای ایران به‌خوبی
پیش می‌رود… بازار سهام تقریباً هر روز رکورد تازه‌ای ثبت می‌کند.
برای سه شب هم محکم بهشون حمله کردیم
الان هم روند مذاکرات خیلی خوبه.
قیمت نفت به‌شدت کاهش یافته، حتی نسبت به  زمانی که حمله به ایران را آغاز کردم ،
الان نفت رسیده به ۶۷ دلار،  پایین آمده.
هرگز به سلاح هسته‌ای دست پیدا نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/67151" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67150">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 نظر شما راجع به عملکرد پزشکیان و دولت او حول و حوش مسائل جاری در کشور چیست؟</h4>
<ul>
<li>✓ بسیار ضعیف</li>
<li>✓ فاجعه بار</li>
<li>✓ شکست مطلق</li>
<li>✓ بعدها شاهد عواقب خوب و بد خواهیم بود</li>
</ul>
</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/67150" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67149">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‼️
آخوند قاسمیان:
واشنگتن رو اشغال کنید؛ ترامپ رو دستگیر کنید و بیاریدش پیش مجتبی.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/67149" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67148">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=Y7EZ9AHCsqQj9aXeSIJ3ThS2Vk8AA3DRJ9vhovHCGVzXTtcYIQULzng4yzJn6Gz8c_AYiS0NtaCFhpf98e_EPnHKeSla0Lh2PzdeBpdmDx7P-9VWCWeyedFPzxmw1y7OlJhgEEaly0xUyG-5XQg3d3H2CIxj_VWYeb_0a-EmZQLEVcqPfmF7virdiLOK6p2wRzl6ZnTSVTJKOJRVndzywhLp8gUmbh0KnjqBXSRPZj9uOFty74ZhpCs0pG9Pzm-Y2Q3BfMxK9hmvfZfX4V5M8UbHWSjS7ZFp6zzDU9VybMxOc2nqJ7lc-9tgStTVg6cR4sTCLDDsD5wTRwPa_zFmVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=Y7EZ9AHCsqQj9aXeSIJ3ThS2Vk8AA3DRJ9vhovHCGVzXTtcYIQULzng4yzJn6Gz8c_AYiS0NtaCFhpf98e_EPnHKeSla0Lh2PzdeBpdmDx7P-9VWCWeyedFPzxmw1y7OlJhgEEaly0xUyG-5XQg3d3H2CIxj_VWYeb_0a-EmZQLEVcqPfmF7virdiLOK6p2wRzl6ZnTSVTJKOJRVndzywhLp8gUmbh0KnjqBXSRPZj9uOFty74ZhpCs0pG9Pzm-Y2Q3BfMxK9hmvfZfX4V5M8UbHWSjS7ZFp6zzDU9VybMxOc2nqJ7lc-9tgStTVg6cR4sTCLDDsD5wTRwPa_zFmVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله امروز اوکراین به پالایشگاهی در حاشیه مسکو
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/67148" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67147">
<div class="tg-post-header">📌 پیام #82</div>
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
📣
همراه با تست رایگان  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/67147" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67146">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSfTUN30H_OcR1kJxKly1chstwYJlES1lD_3V46UsGz2OClU1IVPCVqRXeegxwGVo6AKyOb-eMdfteEsM552SGz47y5l4h2Ey_5W-HrdhtFL1YG0v2LYwWxiHMFV5sNN46r4bgby17ZqvDaztIt2p0Y1K0Sb3lYz6bN0SDHbcnTG3NPvCM_xNpPv50oBthHEMgNSfLEKKycEtEgBQlJnZnFXqrYmGVeC1IiRGR_kLrzN7yPW7b3qXnXv-Vt1w0B6CnkX031JM6KtYZttwWyf7-mPf1-q5y2icPo7k923jq9qbTySEx7xxY3rQSquqzR0WV2k8zO29NxJlysDGGz43A.jpg" alt="photo" loading="lazy"/></div>
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
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/67146" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67145">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=AQYcS4U2-KJZG2666sP_-BIK3DbNcBj5Ss1oh84J_MbhlnCt64rS-nPU_eKGYfMMSgJHZnpWxmFlIBgdbPvYwMJ2kYhJp9o5i6Ymdm44QWjyHz-nSS9cuwc1V7CsWEOLPu0cjCTmctQtuioZKf_M5qbeZh-PuEoiWv6daj_9xrm8mdR4GM6p6z7pYxJItrrAzHmSafUixTDDu7_mra5x_2TPInHdury4Cl0gXIoo3QnawiymSwZeiSUI64naF8-jz32XTFrCbOeV105Z4JiXt3MEMHl6DqIW8a8UpKT7_p8P6r-Z8jWvOJaXWc9NqESM_btZEj62fVAITEJeC0Akyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=AQYcS4U2-KJZG2666sP_-BIK3DbNcBj5Ss1oh84J_MbhlnCt64rS-nPU_eKGYfMMSgJHZnpWxmFlIBgdbPvYwMJ2kYhJp9o5i6Ymdm44QWjyHz-nSS9cuwc1V7CsWEOLPu0cjCTmctQtuioZKf_M5qbeZh-PuEoiWv6daj_9xrm8mdR4GM6p6z7pYxJItrrAzHmSafUixTDDu7_mra5x_2TPInHdury4Cl0gXIoo3QnawiymSwZeiSUI64naF8-jz32XTFrCbOeV105Z4JiXt3MEMHl6DqIW8a8UpKT7_p8P6r-Z8jWvOJaXWc9NqESM_btZEj62fVAITEJeC0Akyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها)
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/67145" target="_blank">📅 17:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67144">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=n8nLRibO90FhVP_XPk792WNZIyVctDAXkluffn7eav75bDK2qGt5FnrQvJwgncd9EAHBbjaAUw1pui6sgFLUVhEXH8xeuS4_IotIffnw2YCWSccvtPYxFhO5NzEcsC8Lulm-U1PuZ5qjd6KcpSS0R8XeBwFW6akRvPZlylTKoGCJVa8Uk4SEMKQ6qGOn85oo1UpuaRdvc1t8X6BZKOUhKKu35VcsJDI3xkfMdNRK--ze0gU0LvSBNgkM4prU7k_y27kROlTGCKHt7oj3PCQb2CF4QYOni2mgEftxQf4HTH27DJpJT30TVuR0QGY7GeOvxHjLlvsbe9yJly9Umo65OA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=n8nLRibO90FhVP_XPk792WNZIyVctDAXkluffn7eav75bDK2qGt5FnrQvJwgncd9EAHBbjaAUw1pui6sgFLUVhEXH8xeuS4_IotIffnw2YCWSccvtPYxFhO5NzEcsC8Lulm-U1PuZ5qjd6KcpSS0R8XeBwFW6akRvPZlylTKoGCJVa8Uk4SEMKQ6qGOn85oo1UpuaRdvc1t8X6BZKOUhKKu35VcsJDI3xkfMdNRK--ze0gU0LvSBNgkM4prU7k_y27kROlTGCKHt7oj3PCQb2CF4QYOni2mgEftxQf4HTH27DJpJT30TVuR0QGY7GeOvxHjLlvsbe9yJly9Umo65OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه جالب و جنجالی یه پسر نوجوون ایرانی که در حال وایرال شدنه:
🔴
خبرنگار: اگه یه دزد خفتت کنه، موبایلتو میدی؟
🔴
پسر بچه: آره، جونم مهم تره
🔴
خبرنگار: خب اونطوری ساعت و دستبند و هر چی داری ازت میخواد.
🔴
پسر بچه: آره ولی جونم مهم تره، اگه ندم به قتل میرسونتم.
🔴
خبرنگار: فرض کنیم آمریکا خفتگیره، الان یعنی ما بیایم موشکی و هسته‌ای رو تحویل بدیم؟
🔴
پسر بچه: وقتی چاقو زیر گلوته و زورت به خفتگیر نمی‌رسه، باید هرچی میخواد بهش بدی، اگه ندی میکُشتت و بعدش خودش وسایلتو برمیداره.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/67144" target="_blank">📅 17:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67143">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1012800172.mp4?token=k9-7fXupnsW6ab199FL12jQbi7qwSDCvJOs36cglTf0gg_06xJPDs7Sk2yAItGajoLV0OQAlqInwI3FDV0_U58flFLLiNfCZthYgqw3vRBHR6CAPJveqlRBM8tezMO9sydD_DQ2kw9nGMOFp_FvXmFBBni_tTZAWPcSNbMWfH-JXm9nEJVoQDmfHo9d8styx9A7bfxgjEaFZzGlzl2J_hL625BotYKGflyCE-2s_BTrTerwV_7SbMwJJji_pBu5APaPINGyK3-JtQ4b-gzaxsHRR0IBlHX8d4oefGjCSrjYyTBVi8fN1pdKFHgQQLbacPNd0O74vMWpQNDImc2iolw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1012800172.mp4?token=k9-7fXupnsW6ab199FL12jQbi7qwSDCvJOs36cglTf0gg_06xJPDs7Sk2yAItGajoLV0OQAlqInwI3FDV0_U58flFLLiNfCZthYgqw3vRBHR6CAPJveqlRBM8tezMO9sydD_DQ2kw9nGMOFp_FvXmFBBni_tTZAWPcSNbMWfH-JXm9nEJVoQDmfHo9d8styx9A7bfxgjEaFZzGlzl2J_hL625BotYKGflyCE-2s_BTrTerwV_7SbMwJJji_pBu5APaPINGyK3-JtQ4b-gzaxsHRR0IBlHX8d4oefGjCSrjYyTBVi8fN1pdKFHgQQLbacPNd0O74vMWpQNDImc2iolw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یک تحلیلگر ژئوپلیتیک چینی می‌گوید امضای تفاهم‌نامه توسط دونالد ترامپ، بیش از آنکه نشانه کاهش تنش باشد، تلاشی برای عبور از «گرمای تابستان» در منطقه است.
🔴
به گفته او، با وجود امضای این تفاهم، نشانه‌های میدانی حاکی از آن است که ایالات متحده همچنان در حال آماده‌سازی گزینه‌های نظامی است. این تحلیلگر معتقد است حدود ۶۰ هزار نیروی آمریکایی در منطقه مستقر شده‌اند و مقدمات لازم برای هرگونه اقدام احتمالی فراهم شده است.
🔴
و پیش‌بینی می‌کند در صورت ادامه روند کنونی، تحولات جدی ممکن است حداکثر تا مارس سال آینده اتفاق بیفتد یا حتی ممکن است از همین دسامبر شروع شود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/67143" target="_blank">📅 16:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67142">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=miAhmThbTeZx68dPuya350RtJ9ECD7wCIledpQOUi5obvTw4pZxFa2FNp5epg9qLOyW6GysKIRN5-32ZZbP1r3nGo7xvX75dJY3GGtJoOI3W1kJcAYHCpnLv4bWOW1ElZXLgkr3D4gG550-40qj3zMm5cH5mrgeTTfRF-I5aVKBq4CtdMUX0tuasguMWVNAmFVwY8D6k-EN1OjdUYzW6D7ede6AISRuCy7mfnVLgbSWk65XZRdwcc1wjMWRyCO9FB1E5Bfq9XLsC6vKs8Y_GZVlsxFWOUnduDsRfzvgec_61G4m-Gh0PR43bjKMlQAJj9W8sNxj218oSAIO4MNBsgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=miAhmThbTeZx68dPuya350RtJ9ECD7wCIledpQOUi5obvTw4pZxFa2FNp5epg9qLOyW6GysKIRN5-32ZZbP1r3nGo7xvX75dJY3GGtJoOI3W1kJcAYHCpnLv4bWOW1ElZXLgkr3D4gG550-40qj3zMm5cH5mrgeTTfRF-I5aVKBq4CtdMUX0tuasguMWVNAmFVwY8D6k-EN1OjdUYzW6D7ede6AISRuCy7mfnVLgbSWk65XZRdwcc1wjMWRyCO9FB1E5Bfq9XLsC6vKs8Y_GZVlsxFWOUnduDsRfzvgec_61G4m-Gh0PR43bjKMlQAJj9W8sNxj218oSAIO4MNBsgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهریه‌خانم‌چیه؟یه‌پهباد‌ شاهد بخوره‌تو‌قلب تل‌آویو
😐
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/67142" target="_blank">📅 16:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67140">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t4o19LWr8EYrsrcFAQUM_i8d0YJGbzhYtTpmdMCn8EvJrSu4IYTV-ezxgpOrdQqh9HRpjzwdBRV6bxRbhlRLrzO6n6uhLOa1j24OfdkS_ea104g4Xx9QY6gUPtMCOtBlSzOyB3SIfyYFZevWGTs-5uMV3sSKDQC9C7n421r2Y9eSMgm2Tn-5E07enXVY-91bMeFqVs5sjX6er2wbg05ebPw-TyM7-4LyiXZ_xYxVapzlMb3-CvviKdWDI_egWLHH1m1d2Lt88r1paWRTyflo9i55Fsp5ZM-eP7-Jy-TsN39aQgV5KJfh9JsDF8rJ6p_MHqS4-oVdYv0mMGV9jDodJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CP5xAFxAnBMEJJ4H_vYG6ykWF5EdlCdCYS8gPvisl5EuOnfOG_EQBZFUhms_eQ7s-YijbvDPtN9OXgZIQ2fjZwBts3E3QjvNsL6EImfnHk-xzvzJnieQxGBNhg0eTOH8ndNClTAchD8-a8bRtEVG5C5hsF8gnD2F1KVv6SF-VCW-uBQWbbM7EWMXy2liiMb5oJweKis4UA5KnKaaxzh6YMmRjhARKJyW3VNrD1zZ8Ayy98E23pdKUAMb3Mf94f_brJ6HMgfGjtOQe0JCGsE60fyMMAnskAc2vC284N0vNNMwybczhPKpNPXC6zlkwBzubUCumGGmi_rcu6avEUAoIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
کاتز وزیر دفاع اسرائیل:مجتبی خامنه ای برای کشته‌شدن نشان‌گذاری شده.
عباس عراقچی:هر تهدیدی علیه مردم و رهبری ما، پاسخی قدرتمند و فوری دریافت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67140" target="_blank">📅 15:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67139">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muKHLE1EV3fS-MuL96WKr8aJM9c-5pOAI13XLu6ohPJodzun5vUlESJ5s90nxENXndtY9RLeG0wzS-RrosQ_l2pWSM17PxKQnH4arkgka7Ctvhj9oEZC-2b19jMx23Icj0lrgfj9GCUEQjfK3GHihWG9ysWGTq6ECKpm8yLqWvoRTvBDOsSFusjOini0ZW61AAZOoLFWLHAQqUxI95zisHoeOKSyXetTUEZLvnIunpNtN8FC9JtSdqG2jgQGqEmuL8ddH2P3S7wG-AGAi0FxHSmx3WIFafBW54Lz8HqkrvkbC_eU7RGsLBJtu1HORt0cFzEwRTvFSCunDrh5i4brRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
علاوه بر ناو باکسر، ناو USS Portland (LPD 27) نیز وارد غرب آسیا شد، کاربرد اصلی این ناو انتقال خودروهای نظامی و تفنگداران از دریا به ساحل است
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67139" target="_blank">📅 14:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67138">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9GAg31E927Gvtc4fcGSmG5A4wjEqR4nG7KnSKjcBWJFGSn3oMgTwIiYS5DTaeu0Q5_-X4fN_LnN0-FvoMl8x8ymU2er_p-HigWXQ-9UKv7jIFHl2ypz1qfgldv7fVJXkBUATEr4i2kQadb7u8kqaPx0nScL2FkWqppxAH-6JX6_NeRj8IpHWfLVYF5_q9wDxXLNuea8mNxHzR4uVbVH866Mm7OSrc3_8hqiog9iu9Cv7gWCotY4ucIUHAm96YjGxmdZfdeCdKGRC4r76LgUq43JuoiHXuFQvaQH-RzHVM8dOCZF03c-BfHArbQNn7Tw-I5MIom2JD3MgGsbFWfOxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
مفاد تفاهم‌نامه اسلام‌آباد کاملاً واضح و برای همه قابل مشاهده است. رئیس‌جمهور آمریکا متعهد شده است که دست‌نشانده‌های خود در تل‌آویو را خفه کند. اگر آنها از ارباب خود سرپیچی کنند، ایران آنها را تربیت خواهد کرد. هرگونه تهدیدی علیه مردم و رهبری ما با پاسخ فوری و قدرتمند مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67138" target="_blank">📅 14:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67137">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xd3KYniJF69BqoGt__stAookSI17f5oHn7-CUsMMK8gEVgBOiRhKxjJ4UKHfrjUTS_hY4p6kdDfXAeCEogsktMeA3E-u1yVFco05eAqnnfa7VSFscBeMlA7lg2ocRgUUOiNoA_jOJGwS1CJGyFe2hj8Oemr0Cfeq3SbV-fcVId2YbWz9UG-36GKM6Yau8qYUvzXivG2Rg1_SsWa_PkAE0ElDpsanLcT1utuZ0IwjQAyTDVBymXaumng6Pmh0kZjWlhjF9E_W26Lan2WxNmAuX2weyOoQXp5dLulOj9CFMkMdEiW4z65uEealThAbnfUFluH2IC2zu5ukvzHpAmSCuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران به سرعت در حال بازسازی زیرساخت‌های غیرنظامی خود، ذخیره سازی منابع حیاتی، پیشرفت سیستم‌های تسلیحاتی جدید، جایگزینی هزاران تله نابود شده، به کارگیری فناوری‌های نوظهور و گسترش شبکه پایگاه‌های زیرزمینی و مراکز فرماندهی و کنترل خود است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67137" target="_blank">📅 13:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67136">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک منبع آگاه:
گفت‌وگوهای فنی غیرمستقیم میان آمریکا و جمهوری اسلامی در دوحه آغاز شده است
قطر و پاکستان میانجی این مذاکرات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67136" target="_blank">📅 13:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67135">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=WE0c0c0DfaXYXlXcpIusj4fxpVy1VRhHw3CI-loT0iA_7eyB5UsZ1ZrkJ8ly3K3EE2J4SKoFdZGLKJEiuWN9zNzU-3OdHPBAOF_pcSATEC8x-HDTRIkwlVSpmQG1DiV9oKhL-Z12tQLYqcd6XNSjKLYvQQ6xrJSVweoYYCC8KN5Yc7O1fNh6z1tcttcpv5B-E-80nZAgcutHgVW-G-6mIRLcK_rXVwQ0pWfEbio8lcHAp9EV6vPNL5vpDusZTY8sy66TgmX-MXMQbfS06oGcPzVgnksBF8EA-XcAJXo2N_50epY223CWKPUcUmnMCPBNl8JGZdnKjx7NZz6YdHlQYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=WE0c0c0DfaXYXlXcpIusj4fxpVy1VRhHw3CI-loT0iA_7eyB5UsZ1ZrkJ8ly3K3EE2J4SKoFdZGLKJEiuWN9zNzU-3OdHPBAOF_pcSATEC8x-HDTRIkwlVSpmQG1DiV9oKhL-Z12tQLYqcd6XNSjKLYvQQ6xrJSVweoYYCC8KN5Yc7O1fNh6z1tcttcpv5B-E-80nZAgcutHgVW-G-6mIRLcK_rXVwQ0pWfEbio8lcHAp9EV6vPNL5vpDusZTY8sy66TgmX-MXMQbfS06oGcPzVgnksBF8EA-XcAJXo2N_50epY223CWKPUcUmnMCPBNl8JGZdnKjx7NZz6YdHlQYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این کلیپای محرم چرا تموم نمیشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67135" target="_blank">📅 12:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67130">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ihrVMRgKFKEuYa21H1P3PPVzF2t1di7Tvc8b_hJwh-WPMqigY8GO-CwTlQasvLJtH7Tw3eL0zu2WmDxNUN8mjeVbSwanuwqOIjEciDkci5o_zJm9_DOrE885CTP-VggoVsUXZ3XkoAvUdabnHuVHSHjYRxvLiD4FXqP7xkNrGIfoVNozzhwTLvw0-6qopiO6A4hpj3sqiVi41bZsgzRWWX157lKd6zVtKUgBOuNYLNQz6Moh4GRf2uOJnkBx0AStzb2lttQvmLGkdUHdAKzeu37XHnASNZSMR5EwJ7X6tX2wPdII5tH0hRH73WFPEhdLZny3dlShweKEdQb21b7gYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OPFGB-6-QNjI37pvReiXN_U3NX5ujeWZR5xy-P3ydVysN3Gqvd5iYYItY6UylOVInHK13YcEC45Eq2TAWNr2YjGE3JNLakIP6lvU_0zCIoq96QNNG6MuXUQkq2CwRlaV7LrwTv5tskMVG3QOCAVHhfzJnVc4ZMFe5HHSzli5yvQEmgbwKMgoxmpXRvTWWLSiXmyBWHC0YQc39B2ov7k9RCwRpXDx7ZZQx0yMnZRyoZuYdLb10fbyhOgKPuRnhOnMDlQR8Qg6CSSdFF2Z9C8PybIvYP_ME8E1LxBTNKtiUFA9I_TG9EN3Nr9mpc_uEyWzfWzk4EgrWTQ7_GX_ywUq5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=bP5hgPvEnAEt9TYNBYMrSVjgbjFpUh-U4oVUb0n7DfUDiyhVz_gbCavv1kIo_fJhhwJhFST5VE-ncEk9cI7EqThooxj7E_7t6CgykhgAWG3lfUma5t12Fi4USw4QYCSF3TRIT-b-VwS4Gjy_3ohAQsgT3TPwaKJkVUWQqnTqqV-O9XsDZ_LS-0FQe1eqHgSRx5blWDVaW3gbZRTOzKFKdPkz6L0MqrkhqHTfkTIJk0VA109zDtNl3gPmipctuz0NnqpCCY_WgZ8XbEynMp6sfO8qtmwfMDzkFowsRvjJOmbObx9Psw2b83GZ1_iE7E0Mz9PsFx35D-_4QO0Rqwxp5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=bP5hgPvEnAEt9TYNBYMrSVjgbjFpUh-U4oVUb0n7DfUDiyhVz_gbCavv1kIo_fJhhwJhFST5VE-ncEk9cI7EqThooxj7E_7t6CgykhgAWG3lfUma5t12Fi4USw4QYCSF3TRIT-b-VwS4Gjy_3ohAQsgT3TPwaKJkVUWQqnTqqV-O9XsDZ_LS-0FQe1eqHgSRx5blWDVaW3gbZRTOzKFKdPkz6L0MqrkhqHTfkTIJk0VA109zDtNl3gPmipctuz0NnqpCCY_WgZ8XbEynMp6sfO8qtmwfMDzkFowsRvjJOmbObx9Psw2b83GZ1_iE7E0Mz9PsFx35D-_4QO0Rqwxp5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر منتشرشده از پایتخت ونزوئلا، آسمان کاراکاس را در زمان غروب با رنگ سرخ و نارنجی پررنگ نشان می‌دهد؛ بر اساس‌گزارش‌ها، گردوغبار برخاسته از زمین پس از زمین‌لرزه‌های اخیر با پراکنده‌کردن نور خورشید،این منظره غیرمعمول را بر فراز شهر ایجاد کرده است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67130" target="_blank">📅 11:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67129">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c160c90364.mp4?token=koGvrGrgtRFpn3U8gfgkoEpPgSzGz9ve3HzNrw4Z2E8c5JaOI5Y2wO2VVMNM0mEBFIJSeRkT8wWvITsBTNz3-ZopC-SYhzcufb1Hd7GH0Pt8aWLwCERdwhgVkzP3tphVn-hm36N3K0TI0m2qnZ200K_3fEz9sG6-4xtdAkvFdpoQCL2Ho0cnprFYTZ4KzydD9JUwIAQql_9LvEdpnNST03XpAHcolmfsACig4dj3c514wUr1FvbPuQqkEAcA8mS_5vpdeO-pOKjvvOBRITbaITP5HOgqDxSM08GhFGc4o9--zkv1p-cvk-003DRWIeYy40FCgPAbmiruGnWtxPTx9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c160c90364.mp4?token=koGvrGrgtRFpn3U8gfgkoEpPgSzGz9ve3HzNrw4Z2E8c5JaOI5Y2wO2VVMNM0mEBFIJSeRkT8wWvITsBTNz3-ZopC-SYhzcufb1Hd7GH0Pt8aWLwCERdwhgVkzP3tphVn-hm36N3K0TI0m2qnZ200K_3fEz9sG6-4xtdAkvFdpoQCL2Ho0cnprFYTZ4KzydD9JUwIAQql_9LvEdpnNST03XpAHcolmfsACig4dj3c514wUr1FvbPuQqkEAcA8mS_5vpdeO-pOKjvvOBRITbaITP5HOgqDxSM08GhFGc4o9--zkv1p-cvk-003DRWIeYy40FCgPAbmiruGnWtxPTx9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌نویی
:
خوشحالم که بزرگان دنیا یعنی آقای مورینیو و
تریلی هانری
از تیمی که من ساختم تعریف کردن.
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67129" target="_blank">📅 11:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67128">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=RHK17VwYI69YkrM3OL4uNF1lBExvOuZVkLvmiHlIemgGLO8zi6aF-7pBY7Pcg3ItsuMYa3SrllzfoBJUTFwZV30HI75Fe4BjJw9Nx_bCLYLJr-WqpvRmidJvc2e8bSjZUqPDBDKxfZRP_dQ8YkxQ35RIY3ev9LscCKsFKq_WdsyW9Tb88GFdSdH51Mc0sGOWP7qpEV3OBG_ssMeCgTxFvVR0mVMXf-Y7xhL02SAOXrEfbO6U680B9PX-N8npMWNotJ7BWHTX6IVDFD_FZ6jpKuX6IcYn0dld0ovEUMFRb2RYFEs6BVS2T2kqMHQBK0nFCnNkYeKjyHd0nW4lCOcE0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=RHK17VwYI69YkrM3OL4uNF1lBExvOuZVkLvmiHlIemgGLO8zi6aF-7pBY7Pcg3ItsuMYa3SrllzfoBJUTFwZV30HI75Fe4BjJw9Nx_bCLYLJr-WqpvRmidJvc2e8bSjZUqPDBDKxfZRP_dQ8YkxQ35RIY3ev9LscCKsFKq_WdsyW9Tb88GFdSdH51Mc0sGOWP7qpEV3OBG_ssMeCgTxFvVR0mVMXf-Y7xhL02SAOXrEfbO6U680B9PX-N8npMWNotJ7BWHTX6IVDFD_FZ6jpKuX6IcYn0dld0ovEUMFRb2RYFEs6BVS2T2kqMHQBK0nFCnNkYeKjyHd0nW4lCOcE0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
سازمان انتقال خون باید خون‌های زنانه و مردانه را از هم جدا کند زیرا قاطی شدن این خون‌های نامحرم با هم در رگ‌ها موجب ازدیاد گناه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67128" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67127">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d22600661.mp4?token=Ts2CaefJn9-B_4RKsd_M8ULzrmAJL-aD-qGWAt3dyEwqez6bxy5cocec14oscT1MTbSOIoLH37oLdlrr3TdfWrYKJg3VZ8xA7hfPEmwQmu0MUwZkZkZyVXJ-SKJ5kIORbfxK7iqCx5qVzmXzPtV57U8zjTQ3PM5zgTU9WcfYD-0X5DJrd_mKfTCszamsXRtGESjQYZmAGZuKx-XrEIkyU6Cyn2pIA72M8_xNJRwoQJ01HVjyRw4Gg7b5e5j0UJHm_7IrrRcTKl2h9hxKMmdmIm5du04d4lLqHgWVsd0cJloNnP1tbbF5EV6-ADJpPVJzM1dLQO2pd28EnYziPnzfaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d22600661.mp4?token=Ts2CaefJn9-B_4RKsd_M8ULzrmAJL-aD-qGWAt3dyEwqez6bxy5cocec14oscT1MTbSOIoLH37oLdlrr3TdfWrYKJg3VZ8xA7hfPEmwQmu0MUwZkZkZyVXJ-SKJ5kIORbfxK7iqCx5qVzmXzPtV57U8zjTQ3PM5zgTU9WcfYD-0X5DJrd_mKfTCszamsXRtGESjQYZmAGZuKx-XrEIkyU6Cyn2pIA72M8_xNJRwoQJ01HVjyRw4Gg7b5e5j0UJHm_7IrrRcTKl2h9hxKMmdmIm5du04d4lLqHgWVsd0cJloNnP1tbbF5EV6-ADJpPVJzM1dLQO2pd28EnYziPnzfaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر ممدانی شهردار مسلمان نیویورک درباره مرگ خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67127" target="_blank">📅 10:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67126">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=DcFkeDMwwKiZK7oEi1_8Zm3k9d71o5HSbCR7Xabysr4IvTJjFdV5ytWR1VOBh7cnRW1pVkyfoQfAR3jyb5dzLWHSaHU9aQF4n5iAeHagAQqMueTHh8LIn3i2xgidg5-oTDdR10XHDpYoxo77hD96rTZY5Rbb43kGCDDGvvknrZVHFEM0y6TbnvP90eOZALwAkNCJqQBKfh8dZl8Bv6JVzplb2Vb1NdjT4IIFSh7CE1_s4yXtGPd2aKkD1c_IQM_RPVoP5LQB7cCEikM6D3jtdyNUggRYodk_l3YZypJk9G7dDck188uX69sgSOB0OgGveUhOocq_jH5upAR-Wa31AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=DcFkeDMwwKiZK7oEi1_8Zm3k9d71o5HSbCR7Xabysr4IvTJjFdV5ytWR1VOBh7cnRW1pVkyfoQfAR3jyb5dzLWHSaHU9aQF4n5iAeHagAQqMueTHh8LIn3i2xgidg5-oTDdR10XHDpYoxo77hD96rTZY5Rbb43kGCDDGvvknrZVHFEM0y6TbnvP90eOZALwAkNCJqQBKfh8dZl8Bv6JVzplb2Vb1NdjT4IIFSh7CE1_s4yXtGPd2aKkD1c_IQM_RPVoP5LQB7cCEikM6D3jtdyNUggRYodk_l3YZypJk9G7dDck188uX69sgSOB0OgGveUhOocq_jH5upAR-Wa31AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
نمایشی که قراره بزودی از عرازشه ببینیم:
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67126" target="_blank">📅 10:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67125">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCT3_NXYSZxCFMBfF8BN4Dw4wLTo_H8vZbucz-8kg2GkUDCsBWQ08DumbiA-CpFAkkELGDm3lV3a9k4ouvPXyPg5roKJPd4YrO9mRlQAkI_Pz6YJJUHxX-meRLHMjLQr3SbNKenoOMBZ-DXivMI-GNlIU_H1WN3Q6S6_3ro97LI2X0YMfzNxRIq-Cuib7TMCbpc5XtH9GfgV72VXhVqSx6R89LtiMiaXYvDndvcV9ch-r-i-MXIq4zZV0pNrVXwfvC3A2iMjOYLw8A8xFCsv7jVG9UPqMDsAEbjKqD3zx6fL_NDY0DxJfXRjInwu6ZL9N5ile4r9E9nqVyG2YK9yHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
به گفته مقامات آمریکایی آشنا با این بحث، رئیس جمهور ترامپ بازگشت به جنگ تمام عیار با ایران را بررسی کرده و در روزهای اخیر چندین گفتگو با وزیر دفاع پیت هگست و رئیس ستاد مشترک ارتش ژنرال دن کین در مورد حملات بیشتر داشته است، اما تصمیم گرفته است که فعلاً به مذاکرات دیپلماتیک ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67125" target="_blank">📅 09:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67124">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDlVsXuYkgex4cXmcG6FtY6gM5VnIIl-ljQa4ulKUbFRHAKS7thGD9Vess8xy9kZFHqbL_CkpITJuNxsYzLbOE6ycn3yY6zuSNO1pWdYgrO6WsJAQdEea5Y7Lm0ek7je5_8mtVTcBhsfJoDIwS2Is_VBIWZSPeKnHO86zWHso96hvXbhb90WSW5c7KKBVmwCqbGEdHhR1aowBfUqlI024OxFVZL3vjj2zrc3SQwHWUHSAiKbVCtBsDUK1qsimSwXPNB2Od7Q0AZWYq3nu8grKJ7oSSDhaLoeXX1OKsgwQwEBDu35FZzgCVlgeDpyXpX0gke4WIhJ1RmHlbrmMnPalw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
فرماندهی مرکزی ایالات متحده:ناو آبی خاکی USS Boxer آمریکا شامل ۲۲۰۰ تفنگدار دریایی وارد منطقه خاورمیانه شد.
گروه آماده به خدمت آبی-خاکی Boxer (ARG) و یازدهمین واحد اعزامی تفنگداران دریایی در حال حاضر به عنوان بخشی از یک استقرار برنامه‌ریزی شده در خاورمیانه فعالیت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67124" target="_blank">📅 09:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67123">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67123" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67122">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VBZP8MqyC4gmX50_urVH6Nc0pJvYEA_1fe8hUHDyp4JTTTum6DUWjSfDz3lQNR_dEsYRMmkOBOFJrk-4XS-ePcaKS08Y0lcD3l0YzWR4mhWnTIA-4wCdtzv3f3u0XMtYIQQPpbjkwwOtRbKGXM6qoiTYfiHgssqEihShLu-m_rHFWeV1PPHfxweCM7xgEjCVUM1p7hNYVp3j6kDz7avIP69q8X97cmyGKwga3OxkTrEcGuLsX2s_Of5NvbczDcmnnvwoNr-xJHShPlHhNMA9eXeRisF7PcBXI5qE_5qfIzszxoqwLFsVCIl9jY63FU_fTOZON0r9KirrB7dwnt6fow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67122" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67121">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=gDlE3ewdTEJgOtGgf8OPS69ct2yde49ZHYdRj_USfvCOKzxKXAIqAfxmQ--5vYYZfqaWYhthBvfNB8G8tpnzDbY_uxHDlkwLUeYKMwvNQDr82Dd4V-UK8eR5oeGj23WpsISapIhKb7uakE2EmVai6xnwVEc3vMf5PXFhlyD1rFK7OmE7NIXR4VVe5Ryx9WxZLHMyShJ-q7yLiVHX0FaLvaTDFVunjrAMwQJVl39li6lr7QBTyUcAp3izyF9xy9zoiKbUVAsWJOIlQIlU9VYyD9jcL1kQwUnKUo3PbWUzKVKNz2CS9Ma-pMlG8hNc-kGv42_3_L0gdM3-9cBnn0o3Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=gDlE3ewdTEJgOtGgf8OPS69ct2yde49ZHYdRj_USfvCOKzxKXAIqAfxmQ--5vYYZfqaWYhthBvfNB8G8tpnzDbY_uxHDlkwLUeYKMwvNQDr82Dd4V-UK8eR5oeGj23WpsISapIhKb7uakE2EmVai6xnwVEc3vMf5PXFhlyD1rFK7OmE7NIXR4VVe5Ryx9WxZLHMyShJ-q7yLiVHX0FaLvaTDFVunjrAMwQJVl39li6lr7QBTyUcAp3izyF9xy9zoiKbUVAsWJOIlQIlU9VYyD9jcL1kQwUnKUo3PbWUzKVKNz2CS9Ma-pMlG8hNc-kGv42_3_L0gdM3-9cBnn0o3Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
کریس رایت، وزیر انرژی ایالات متحده:
ایران هنوز به هیچ وجه همکاری نکرده است.
جریان نفت از طریق تنگه هرمز به لطف ارتش ایالات متحده است. هنوز هیچ همکاری از سوی ایران صورت نگرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67121" target="_blank">📅 02:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67120">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDPm1IG0DToG7qm7CKlzYLT__B3RDlhbVhVNdEX8fVN62jUQrmVKxB-QKjir9_pAHgrapwsO6qVgM2vs6__ibAiViNdpzNli8ebd5j6NKwWBM_FG5uXELEY_0vfD0Xb376pNkGtPB7IVlT5k9SnoLXIC3yo9tMJo7vTNbLTo-3BRabeg6FYzEZ6E52i4HsjlkvtOs9WOAC6oEOQCcvnEHsNaUExQEWzfi0H45MS4bIWCy7lVsn_EVWuQ9VzOr2hMuP6Lyi7yqtUVmbWgpgnmOBfiBIhPAvXH3hg-tJ3zvG2ueINEUjQd-abiZtWqBBn12FAfzoYVmJe0vn5_iIrfLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر منسوب به تابوت علی‌ خامنه‌ای و خانوادش
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67120" target="_blank">📅 01:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67119">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=UcJB0t5a9xdLoP39qaspbrn-V1FiJ9WoW_Cz04yDUrEHWyIQJXv3H8XWgLp3UuSOh-OoPL8udXNpsVovve20QJoanuIotIQwyQRJzNXFokdnUU1gUw-G8-YIaB3jiUtD7HzZPUeX6B6-3Sh7ZbKorSkU94BS1J1odflG_Rd4TkNRCP0acMD0VcK6UFciIMjCBMRyTy7ZuI0Wb8em8eziT3D3HfoE7t7EMQs0ndseMlVS0L8gqjy50d3fPJYk5TL25YkMZNcuIhokBikBvkGMAs3qp01KBjNApgK9udcgNS-eh9fGnlg_mMr2jhZElIbp-FzEc6oAo7cWiBNSHnPx1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=UcJB0t5a9xdLoP39qaspbrn-V1FiJ9WoW_Cz04yDUrEHWyIQJXv3H8XWgLp3UuSOh-OoPL8udXNpsVovve20QJoanuIotIQwyQRJzNXFokdnUU1gUw-G8-YIaB3jiUtD7HzZPUeX6B6-3Sh7ZbKorSkU94BS1J1odflG_Rd4TkNRCP0acMD0VcK6UFciIMjCBMRyTy7ZuI0Wb8em8eziT3D3HfoE7t7EMQs0ndseMlVS0L8gqjy50d3fPJYk5TL25YkMZNcuIhokBikBvkGMAs3qp01KBjNApgK9udcgNS-eh9fGnlg_mMr2jhZElIbp-FzEc6oAo7cWiBNSHnPx1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
بخش سانسور شده صحبت‌های قالیباف در صداوسیما:
قالیباف در قسمت پخش نشده این سوال، می پرسد: خریدهای قبلی این اقلام که در طول ۱۵ سال گذشته انجام می‌شده، از کجا بوده؟ آیا ال‌سی اینها در لندن باز می شد یا نه؟ چرا الان مهم شد و این حرف‌ها را میزنند؟
🔴
چون نمی‌خواهند بپذیرند با مجوز اوفک صادرات نفت انجام می‌شود.
​
🔴
این قدرت جمهوری اسلامی است به آن افتخار کنید و پای آن بایستید. این سند شکست آمریکاست و ما با عزت آن را انجام دادیم.
​
🔴
گویا حداقل ۲۰دقیقه از این مصاحبه پخش نشده که نکات مهمی را در خود داشته است.
​
🔴
برخی قطع صحبت رییس مجلس را با بازگشت روزی‌طلب به معاونت سیاسی مرتبط می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67119" target="_blank">📅 01:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67118">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=gYt-8lFya_nvLHKHVfTNuXlyQXpaorzqaq72Ylv73lZ1iEwgYRePWd0-AsE6SaF1PPmwtzTDfK1Bh4233dFwjlBdheAv_kHQ1J8ABdPCEmMIMjSEve4lecL5WYHdkawUKASTjtliS2MZ9UqMrPfUj0Rb9COuyyGJSn3FPfBOrM5RbQDY7h4Fuk0faz6zznqLLuFccBsJBfJFFTmsf7XtvmxsdyPtuUitLp-fu98pKM6BPqml3FhzOwZfaqOgFAr4xvdEwXVu-WX3wsqGPDZpufDfFqYNtQAn8mjeftb0eECPysmcgv3e9bBdV-MuJm9olYR7AhA0M9eRX4ki1kxdVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=gYt-8lFya_nvLHKHVfTNuXlyQXpaorzqaq72Ylv73lZ1iEwgYRePWd0-AsE6SaF1PPmwtzTDfK1Bh4233dFwjlBdheAv_kHQ1J8ABdPCEmMIMjSEve4lecL5WYHdkawUKASTjtliS2MZ9UqMrPfUj0Rb9COuyyGJSn3FPfBOrM5RbQDY7h4Fuk0faz6zznqLLuFccBsJBfJFFTmsf7XtvmxsdyPtuUitLp-fu98pKM6BPqml3FhzOwZfaqOgFAr4xvdEwXVu-WX3wsqGPDZpufDfFqYNtQAn8mjeftb0eECPysmcgv3e9bBdV-MuJm9olYR7AhA0M9eRX4ki1kxdVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
قالیباف وقتی گفت توافق خرید غلات و گندم در ازای پول های بلوکه شده برای دولت سیزدهم بوده است، مصاحبه اش در صداوسیما قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67118" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67117">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640225b559.mp4?token=A7TK4lmUZnafTXMusnCAVsimRF5BIOojlOAIhI8XkHXZVaZqk62NAlHxzqWXOrStZht04_A5OQBASMezvnfl4RXzl7Z58a-_oCwkS4-wGCZSswy_Xg5aDtivLMlUSw2hoCJr-VrLIDRUdjSKSKKLeFiyUsC_nmNIAnM6v3Z8VEdvX25wjYXklsEZjBEV_XlMJ5qARkNKMG8chgAAeotRVzQa3_OMku1qTVqLJCfD-QtHsqIZi58mLdfWKMZw-q1hsZhxvqrMo_D99cO92tUFbytrqCaouHs9_EyQTxOyqGW94oCzrLo_ajIvbcR2p7v5N5A--N2Ddunf9_MhBrYung" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640225b559.mp4?token=A7TK4lmUZnafTXMusnCAVsimRF5BIOojlOAIhI8XkHXZVaZqk62NAlHxzqWXOrStZht04_A5OQBASMezvnfl4RXzl7Z58a-_oCwkS4-wGCZSswy_Xg5aDtivLMlUSw2hoCJr-VrLIDRUdjSKSKKLeFiyUsC_nmNIAnM6v3Z8VEdvX25wjYXklsEZjBEV_XlMJ5qARkNKMG8chgAAeotRVzQa3_OMku1qTVqLJCfD-QtHsqIZi58mLdfWKMZw-q1hsZhxvqrMo_D99cO92tUFbytrqCaouHs9_EyQTxOyqGW94oCzrLo_ajIvbcR2p7v5N5A--N2Ddunf9_MhBrYung" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
لحظه قطع شدن گفتگوی محمد باقر قالیباف، توسط صدا و سیما
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67117" target="_blank">📅 00:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67116">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e29288f186.mp4?token=okAtY6qFHeO8bH1L1Y79-Ki7AixhohO3gbVkSNoxNWcpbVdYHhfBCcNNsySyNZfuC0n0psKXcKF-YrS7b-Kfd1RsK_s_oOlmL_KmoitFNA5e07mQUXMg2IoWs3lujNVTFraFtOLSXSIx0iLSOQoF5RrVs0-l1bNQXtWAOaHu4KC5Kf-Qb1lahJ88MZVLopKeO9_qKYoZiELSY6gyuSWAAaW_jJCgiXYXe2LpxShKzgNkbxk8QB4JdoONsLP7chSheaFXWfZd0_iYeb_pNt510rPhedjjcyk1LYpxG29ihFO6kmsHu-bS0uOzYrgp3odxDTne_aU0l_aIgX4v9mw8nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e29288f186.mp4?token=okAtY6qFHeO8bH1L1Y79-Ki7AixhohO3gbVkSNoxNWcpbVdYHhfBCcNNsySyNZfuC0n0psKXcKF-YrS7b-Kfd1RsK_s_oOlmL_KmoitFNA5e07mQUXMg2IoWs3lujNVTFraFtOLSXSIx0iLSOQoF5RrVs0-l1bNQXtWAOaHu4KC5Kf-Qb1lahJ88MZVLopKeO9_qKYoZiELSY6gyuSWAAaW_jJCgiXYXe2LpxShKzgNkbxk8QB4JdoONsLP7chSheaFXWfZd0_iYeb_pNt510rPhedjjcyk1LYpxG29ihFO6kmsHu-bS0uOzYrgp3odxDTne_aU0l_aIgX4v9mw8nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
این خانم، عالیه نصیف از چهره های وابسته به رژیم جمهوری اسلامی، شش دوره بدون وقفه نماینده پارلمان عراق است، او در رقابت‌های پارلمانی چند ماه پیش گفت: «کاری می‌کنیم فاسدان از پنجره فرار کنند». حالا خودش به دلیل فساد کلان دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67116" target="_blank">📅 00:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67115">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e563023c29.mp4?token=d8Hy1jU0aii_pm44U5vVyAIAmerp30jcd-qOqlSyqSOeAYA7glULypalUB_XKYpSe_jrD_6xzsV41MhcCL976aT51yj5ynCDstYZOF-3WmIO3w91-4Aulzp0gveEjMBVhNlHnNSXZOD1B6831J8-HRdwPyap-20CXE1b9IMYLC3qEQkZEwLsnKn5FmAAoO6A6lUWWqgtqMON9YC5MyYHI-wddezavqFv1c95YA1a7TGQFOULhVvYtgECzSPF5tyu0vvhpjLFxh9jGqZKGpu1RG3shoeh6H06jIpEqov8WDlbAlZM1unH62QRTExJdz9cHjBrv9KMSfMynNFliiKTew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563023c29.mp4?token=d8Hy1jU0aii_pm44U5vVyAIAmerp30jcd-qOqlSyqSOeAYA7glULypalUB_XKYpSe_jrD_6xzsV41MhcCL976aT51yj5ynCDstYZOF-3WmIO3w91-4Aulzp0gveEjMBVhNlHnNSXZOD1B6831J8-HRdwPyap-20CXE1b9IMYLC3qEQkZEwLsnKn5FmAAoO6A6lUWWqgtqMON9YC5MyYHI-wddezavqFv1c95YA1a7TGQFOULhVvYtgECzSPF5tyu0vvhpjLFxh9jGqZKGpu1RG3shoeh6H06jIpEqov8WDlbAlZM1unH62QRTExJdz9cHjBrv9KMSfMynNFliiKTew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سعید آجرلو از اعضای تیم رسانه‌ای مذاکره‌کننده جمهوری اسلامی در اظهاراتی در پخش زنده شبکه خبر رویکرد علی خامنه‌ای رهبر کشته شده جمهوری اسلامی درباره مذاکرات را اشتباه خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67115" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67114">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7yBlaGYUa9syIUc8OhFxV54dilsgIu9wyOvwA-NWJ5TSC4WjcGPN4d1bO1pVicc2hlO2poE94nSwmCfbPfPWGwsEOJRqAFGa5SktLtR7x66rrhHPdWuqjuV3zu_zQzbxV3vJNujVCBjRfq3z1V5LXx29D7-HSLlpWHJ59yC_i8gMti_tgn2xTcz8vOTxzFMG_WzNR5fg3BEMvJ9pK9fIIJQty5jw4AQIVwNdKZq1jxoSCnY0VaRznvLYqwBs35P84q7vt3F7XxSghW5Ctv8JfhziPqfZLHwSZc60-zV-HW6kPEA1E7B79eN9KqMs0kebvp2sFphea-HESTtBsz39Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌿
جدیدترین روش ترک اعتیاد  گیاهی
بدون درد، بدون خماری، با انگیزه‌ای نو برای زندگی
🌟
✅
ترک فقط در ۵ روز
✅
درمان کاملاً طبیعی
✅
بدون داروهای شیمیایی
✅
بدون بازگشت
✅
همراه با پشتیبانی روانی و انگیزشی
💚
بازگشت به آرامش، بازگشت به خود واقعی‌ات
💪
تو می‌تونی! ما کنارت هستیم تا دوباره بدرخشی…
♦️
جهت مشاوررایگان فرم زیررا پر کنید
👇🏻
https://app.epoll.ir/74570725
عدد 6 را به شماره زیر ارسال کنید
👇🏻
🆔
@Sahar77631
☎️
09923413672</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67114" target="_blank">📅 23:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67113">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSY7xqriUriL9Lo0sb9t7hS9fP1nd3TJ0FcMzRQgBZfFrPdplt41m11DZayyLQvz_hAxZ2V5NRJ0uX5e6R82K9ObQ2S4A7YuQgp7xdE1-CMLvjcS5SiqD0Qi32evULhOIqmAbXpp_c-4mxralr3zkEdmBAs9eTO_7vZGzKlzzkkTu3iwmgc3BZiUfylQX6KvkqhJ4rjMKzyfk-E3pW9gZEg3USCEk4lXhAx8Z4U0cJjyR0oRimIbyUyDVzI5AW0hJ165SAjNhnTSEejSxWqE5wlok4svvu7sMbBn5A7pPScB1FcVcJhd9jvnGmD4hQ4GojGULZvOkyButopkGXkfhHJ_s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSY7xqriUriL9Lo0sb9t7hS9fP1nd3TJ0FcMzRQgBZfFrPdplt41m11DZayyLQvz_hAxZ2V5NRJ0uX5e6R82K9ObQ2S4A7YuQgp7xdE1-CMLvjcS5SiqD0Qi32evULhOIqmAbXpp_c-4mxralr3zkEdmBAs9eTO_7vZGzKlzzkkTu3iwmgc3BZiUfylQX6KvkqhJ4rjMKzyfk-E3pW9gZEg3USCEk4lXhAx8Z4U0cJjyR0oRimIbyUyDVzI5AW0hJ165SAjNhnTSEejSxWqE5wlok4svvu7sMbBn5A7pPScB1FcVcJhd9jvnGmD4hQ4GojGULZvOkyButopkGXkfhHJ_s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دو موشک فلامینگو اوکراینی به یک کارخانه تسلیحاتی روسیه در ولگوگراد اصابت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67113" target="_blank">📅 23:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67112">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=PDczC6-uzALz-Y6_ARWsWyoJoKBas72IYMpwvDxCepRCY1WKR842ndoF1juVbQ74-sToycB5CZVCMoV8njIVSjkhzD9H4_8r2luJaztquKAY3CaCGjEeZc19RT4tBndZ4v-xhrZtMIoj5WMSgzy5h23spHZ0uhEg8Gp88hFKbHEXLPUFhD4-KmjAnK00arTYgcAfVKHo3lKhBGBOX4I6sKLDWXy1z1zbap8bBsuAdOiU48NG66KmpA3WhVnBzx_ljqJbZwnzJN9TdgfTQTfsmpJsxjqJRIqpTevO0dzo5TN7SrX9xOGGNord6kKJvLZo1MkG2HiChHxja805dMW0fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=PDczC6-uzALz-Y6_ARWsWyoJoKBas72IYMpwvDxCepRCY1WKR842ndoF1juVbQ74-sToycB5CZVCMoV8njIVSjkhzD9H4_8r2luJaztquKAY3CaCGjEeZc19RT4tBndZ4v-xhrZtMIoj5WMSgzy5h23spHZ0uhEg8Gp88hFKbHEXLPUFhD4-KmjAnK00arTYgcAfVKHo3lKhBGBOX4I6sKLDWXy1z1zbap8bBsuAdOiU48NG66KmpA3WhVnBzx_ljqJbZwnzJN9TdgfTQTfsmpJsxjqJRIqpTevO0dzo5TN7SrX9xOGGNord6kKJvLZo1MkG2HiChHxja805dMW0fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازدید بنیامین نتانیاهو از منطقه امنیتی در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67112" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67111">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=hO1jUdrv5R0bZEaD7oscP6--UHo1BIuRGrX0RQ7sj_JvkTR8mOu1-2cP7Tle6EjqBCazMy1CYITUG1q9ub-zWWgAyCN_EvLB-4EE9DR7Qfs2H3LN3g-Qb9bmGR6kDMYXqHkUcDBhM6domHZinBWXeJ-7RftqFBRLLzHnoFg7LFwFF3F-P_pg4cCkg7Wjf6aTiK0QlkxNp-qacg7csd4LponumN5xu2a1AsExFjwmvXCdrTC7s9Dbx3huU7z0JIBq-OLVpoIZGZ9URdqt1HOhofvSSrovFcl4qaNNQqTTeH978qOJp1vEZkPzyXAAgGBibvrjgk0seoVVB8D6Bn87XHi-a-SBisfFqQvoQwURsZIyM_xMDN1xZt8YfToVK0jq86LjvY1-_Pvyt9q45LLVTAefJvnB1pjTiMtwTnshjex092fGs-IIWGV8G6D5MNBk2LWJ2Z12qwKyiKXudvyc7vBd77KdI2i-RRVp_Y3ppCOsNR0wfe8ypom_Dii0XGAigMivOGxMOk3Oc93uom0z3I2cqZd9LVvRHnlpl9JMDwzeGA0PsTyhvAeYPR9ITr8HchZCZNLgoxPRydIxwpWNoQ4dTbTT5iYafjjNnnb9RIyd736KrkFx56DVlQhWGMIPZPm4LCY1YUp625VpsBc4iiMq3U4svnxlXSPoZrzkJmo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=hO1jUdrv5R0bZEaD7oscP6--UHo1BIuRGrX0RQ7sj_JvkTR8mOu1-2cP7Tle6EjqBCazMy1CYITUG1q9ub-zWWgAyCN_EvLB-4EE9DR7Qfs2H3LN3g-Qb9bmGR6kDMYXqHkUcDBhM6domHZinBWXeJ-7RftqFBRLLzHnoFg7LFwFF3F-P_pg4cCkg7Wjf6aTiK0QlkxNp-qacg7csd4LponumN5xu2a1AsExFjwmvXCdrTC7s9Dbx3huU7z0JIBq-OLVpoIZGZ9URdqt1HOhofvSSrovFcl4qaNNQqTTeH978qOJp1vEZkPzyXAAgGBibvrjgk0seoVVB8D6Bn87XHi-a-SBisfFqQvoQwURsZIyM_xMDN1xZt8YfToVK0jq86LjvY1-_Pvyt9q45LLVTAefJvnB1pjTiMtwTnshjex092fGs-IIWGV8G6D5MNBk2LWJ2Z12qwKyiKXudvyc7vBd77KdI2i-RRVp_Y3ppCOsNR0wfe8ypom_Dii0XGAigMivOGxMOk3Oc93uom0z3I2cqZd9LVvRHnlpl9JMDwzeGA0PsTyhvAeYPR9ITr8HchZCZNLgoxPRydIxwpWNoQ4dTbTT5iYafjjNnnb9RIyd736KrkFx56DVlQhWGMIPZPm4LCY1YUp625VpsBc4iiMq3U4svnxlXSPoZrzkJmo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف: اگر می‌توان گره ای را با دست باز کرد چرا با دندان باز کنیم؟
🔴
کسی می تواند خوب مذاکره کند که برای جنگ آماده باشد.
🔴
مذاکره با آمریکا مذاکره با یک دشمن بد عهد است که هر لحظه فرصت پیدا کند علیه ما اقدام خواهد کرد.
🔴
ما در شرایطی با جنگ و آتش اقدامات تلافی جویانه ای را علیه رژیم انجام داده ایم.
🔴
خوب است ببینیم شیخ نعیم قاسم  و مردم لبنان درباره این تفاهم چه می گویند و برخی دوستان ما در داخل چه می گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67111" target="_blank">📅 22:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67110">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c10065584.mp4?token=njJ_3426HvD7sUkEUEsOSeFqRZcqcCUw_q8lm_Izz7L6aefbBKsKAfpW_fIuP5Iw4oRUI1DoAkxago0Q8LzUi4IK9c82ZeWtxWagAI8xdn263rSwGH30Fte_64GZ4ZZH7EPM7AnTk6N5XNpMlgWOvQxGbjafRKfS8nPMr8RRKo5hxbIcDU6hKDCsAFjx49GPxkb9tyb8h_BlYR3hnfRU96N_899tYRttFi-rTqR7n3hbX80DSVN3qDxH-O0vfZaAVO3j-jfs_K-IWGOduO1dTIGCpdyJ-M2vBgqyQLlEDrZ6Hj4JylOt37Y6lrtjWj_zKf7vk6VCG5fVloW8UubWjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c10065584.mp4?token=njJ_3426HvD7sUkEUEsOSeFqRZcqcCUw_q8lm_Izz7L6aefbBKsKAfpW_fIuP5Iw4oRUI1DoAkxago0Q8LzUi4IK9c82ZeWtxWagAI8xdn263rSwGH30Fte_64GZ4ZZH7EPM7AnTk6N5XNpMlgWOvQxGbjafRKfS8nPMr8RRKo5hxbIcDU6hKDCsAFjx49GPxkb9tyb8h_BlYR3hnfRU96N_899tYRttFi-rTqR7n3hbX80DSVN3qDxH-O0vfZaAVO3j-jfs_K-IWGOduO1dTIGCpdyJ-M2vBgqyQLlEDrZ6Hj4JylOt37Y6lrtjWj_zKf7vk6VCG5fVloW8UubWjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
تعهد ما نسبت به باز کردن تنگه هرمز و ادامه مذاکرات منوط به پایان جنگ در لبنان است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67110" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67109">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
قالیباف:
غنی‌سازی حق ماست و خط قرمز ما در این زمینه مشخصه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67109" target="_blank">📅 22:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67108">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=ndl8_Sn8FEUoMFDwW1RLu0E-Y6TQVIGDHVTN5BRPQ5e8Jn-HpxfLP_1_ThyzID8zqaGWRDhjW3AslHxVR4nDxPx0B7UVQWhSXbrjGXKwsFwUV1ZhAxhbiSVjHS94Daifg1Pc3VItmqq9JLToEeyAsTVMtmAaW3OGfv2JJfx7WKFc0ab4b0dyWSdgWK90DJETLz1RNf8Vxc6q4XtvVlUhTNwqE0psV8EASHuxvk2gt0TdymPN5F5fGqnlMCPZX4FmiUnPLDXWsn_aHpp3VsDQrv4ScLkLbOo31mxUbFx3wpQR_UxBaAP6HaZPiuLon10foHkBpgoYIyVZp5i7qH24vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=ndl8_Sn8FEUoMFDwW1RLu0E-Y6TQVIGDHVTN5BRPQ5e8Jn-HpxfLP_1_ThyzID8zqaGWRDhjW3AslHxVR4nDxPx0B7UVQWhSXbrjGXKwsFwUV1ZhAxhbiSVjHS94Daifg1Pc3VItmqq9JLToEeyAsTVMtmAaW3OGfv2JJfx7WKFc0ab4b0dyWSdgWK90DJETLz1RNf8Vxc6q4XtvVlUhTNwqE0psV8EASHuxvk2gt0TdymPN5F5fGqnlMCPZX4FmiUnPLDXWsn_aHpp3VsDQrv4ScLkLbOo31mxUbFx3wpQR_UxBaAP6HaZPiuLon10foHkBpgoYIyVZp5i7qH24vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
اگر نخواهند در گفت‌وگو به تعهدات خود عمل کنند، آماده جنگ هستیم.
🔴
اتفاقات شب‌های اخیر خلیج‌فارس را نقض آتش بس می‌دانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67108" target="_blank">📅 22:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67107">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745f2de194.mp4?token=W1Q3MBdBNfriL56j5-eHADZtupXniMp8k3xFWLqF0LeSMlDgCrqD6xHw2lh6gc6D14R4-7X3dLP2-4Sfr2UVQHeJMHOhh8xgF3Pc-iSiRhg5D7EQebSSEISHuIhO67fdGcQRVtj_9ptXIfG6zoF-5W6jaX4F3eTTVY9y7LL7UOA-6FhOXEyFFccG3a8kt_FmBnnnayRAVdQ3EPO5pccr6MqBZ3w-E7Y5fdB9tPqgC-Cc2LwKjXpeCM3O1AhypVGZu7Ddqp4hJoWp0AkUkoLfEIBBnk3x3tW5hehkGEN4mun92X630WhwAb2YYq7W1RZ0jqWpgrH3jDoglcgsB-XUog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745f2de194.mp4?token=W1Q3MBdBNfriL56j5-eHADZtupXniMp8k3xFWLqF0LeSMlDgCrqD6xHw2lh6gc6D14R4-7X3dLP2-4Sfr2UVQHeJMHOhh8xgF3Pc-iSiRhg5D7EQebSSEISHuIhO67fdGcQRVtj_9ptXIfG6zoF-5W6jaX4F3eTTVY9y7LL7UOA-6FhOXEyFFccG3a8kt_FmBnnnayRAVdQ3EPO5pccr6MqBZ3w-E7Y5fdB9tPqgC-Cc2LwKjXpeCM3O1AhypVGZu7Ddqp4hJoWp0AkUkoLfEIBBnk3x3tW5hehkGEN4mun92X630WhwAb2YYq7W1RZ0jqWpgrH3jDoglcgsB-XUog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
دو اقدامی که پس از امضای تفاهم‌نامه، در شامگاه ۲۴ خرداد رخ داد، اعلام پایان جنگ از سوی نخست‌وزیر پاکستان و توییت ترامپ درباره برداشته شدن محاصره دریایی بود که از اتفاقات مهم تفاهم‌نامه به شمار می‌رود.
ما در حال دنبال کردن دوران گفت‌وگو برای تحقق ماده ۱۳ تفاهم‌نامه هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67107" target="_blank">📅 22:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67105">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bzosnaR8fHlsQgxlebHd12OnIGFuSS9RvvLmUdCJxZOoDRMgEaO18eelJrNzJGaPWq_3wL8Z5K9eOLATOXUz246Ayh2pbz9E0pPopKfvEc1_a-MYNYdrToby2tUXWDLsutoFqMJjrA3eM2nZYBPJd2Ab5hzUjcqp9DtCsYD2rhhL5vGsWZtp3XQIm450mrDEUB1jE8El1p7bBpNf-t-rWohRkAK0p7u0lgjyIsMW5FEw-dUahNeWWtop8DKaSuLA3a1HY0ZAXYgvnRL3PwimEQthpZOKoPx5Mo8JnIJKRF7QqLqqm91jIboW06d3aTnT4crheMmAP9NTpUM5i3lMSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FFiN72qXGnZ-71rJYZ6LHusxN3luuVSw-5RUyj3_8MsOjo2sdxIqb7-D36fR6kHw4zJdioDvdzXaT1l0DSanIblQmvtnztSGRCO7gUiCblI2BDCiZ5pywQL5Uahr8HttWtdv9T7KpBT7pm37IwyDC0nREO3jyOyvgCYpHENkc-yeBex1bNxSQK4PHTg1pndcIwJuGuGL8w3wbfHPqBQ9Ayy71dBKQayKw71IgLKVQ4XWHswjNpIZdvYzNxpvOMO8tS7LT7pBBj5hj99UYKZ63bsbhL4-eciM6cMwwzYF_DHEb0xu1y_-Kkf-8nzGhPSECIlLrqpFB-KZ5g1ndZ3brw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صفحه اسرائیل به فارسی:
چرا هر کجا این تصاویر به دیوار است، دزدی و فساد هم هست؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67105" target="_blank">📅 22:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67104">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzzLF_odMOozT6wzUqlf5JNlqFBio76tq0m6f0MCnaPOgHu3FR-SFbYwZ4EDfc1fmwvjKGLLvnrCYnFfrgA6EhHLHYCHtn9_ZtXxSfQcjapBfJWaC1GeUL6HT9pz4KUU5Z-xtgG02RTz7xDSkjii3y7hg-yApjeu5W_c-4JgAF417cmqhoF54Mosvwhe3fzsLPOLBUL_GZcVa590AWsiLpuOaVv5N93ic-Zr0hBq7khKSZc0p2up6jbqUcqxQ2Uku9Xy9AhLIXkPdWpOY_xDumu-3gM7c3P5iVYIwP3emPUyjDwcmAVCSTAb7rxEZ8GxVxmsnzpcJiQ9KuxIJUYO-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وال استریت ژورنال:
اختلاف نظر میان میانه‌روها و تندروهای ایران بر سر اهدافشان در مذاکرات با آمریکا، پیشرفت آنها را کند کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67104" target="_blank">📅 21:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67101">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H7rGS-bwL1QspPY6N6Hj_vxOKFv9Ih1GlTYOr0MyPbxxAoPFa0POqFTB4wGwSuWwaEg-cg-aCwj0pbDVEzrdun0b_swun8hV16vuhPzlLRV-iDQpQJfeffoCiEU31lLR-ZFeUb7KKG9bahB9OMMpJcsPW6SHqQ3X3DjhzZ-PCZJwnayV8M2TXBjPhPYRM9anpSy3fKUt35UDYQkMXr1Zv-mVx-9jHcqtzLx09Uo8oOW8taOu33LlHY7VhOLnS4y-WGxmmSPav7ipaqzmb7Q3odxODnzSawHNvLEaN7jfq4JIjU9Hz7jm4Lm955bOfzrig4zF-173THwXgpPZoo2tsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gr8GgXqHGYVxsa7tffz-Adh88i3J6Z0MvwvbxKQ0ROAnRCwBWRy6Nnwun0UXc5_S8PWEQtIlBJy4VwqFWy810hHHIMYCQPje8Q9a-zbZGJISX6caHb_q6GtAvsIBOn69n1Xl7vASZdfDRwaqciIjdxb0HQSpQPqofpBaHf8cmvnEx1Q6rriWnvowiWYnQDLS91XtsC6xV23LvnAMxJy_XwdMfYjv6_K9Ovw-ODaTqBZqQ3AmB8IVXDhWVdPa86uKZGn28DzA0FcTTTopX6r7bEL-iPbpXUG6pBV1IqcufPhmwyeHeN3iR70WcS4FtjNEFHg0N2-msiIT52V-SxT-XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AfKprmbTT6EuImVQ56ajwIoUDftJjlO3p8DhVEfiyoSwvMP2tE3I1YqwBFBuIs2JOXktO7kQmuX-PLmmJQjY27LUrhs4BrfQ91uje1u-f6wYTKyic_APoeD2eVZAhYBVllUvathPQiPScJN9LTcEQ-_7O6z4xu0_dXasj8zleScbdiMxrIlkImSR_NC-lJFZiS1Q4KrBqRMFtbcDRVvqyiUvOdt2rloph2uxHIgnr0Wp-9SLp8JLK-UG2ENud2NV37KQkmPAboN7N2GyCHOYwxbnoCDzdW2JwmP5yJl9ibeLot63PkSeTJHrmpRjL7j1UK0abnEVLCDH_eAEm1AdDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سنتکام تصاویری از آموزش شبانه تفنگداران دریایی ایالات متحده در جایی در خاورمیانه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67101" target="_blank">📅 21:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67100">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=HJd-IvDYcdss85HCagfrT7bBZXJE5r_axc2kx2JJ5S95ALRhd64Ikk390eNAvyctEe6lq4Tu08IRoyuUXi5_RZasdWdYLVOm4uFjd81r2OIYsMubaJ495DF5NzlDnTeStAk5b7yjVHPNUe1E2BzV9PbfnF9xkTwwEI2rqMC-hcZH_W8bnu-HoWXvTFLZB74CrlVJpXx9uAVrcpAlnzsJU7PtwLgJSduwUeKSOasYiMzGTY-QP_VW2E__S8LS0Q8K9V04UfjhrDwimxgBoqIuynOSHgrLvz0dEgEhvdfXD23Z5rLrVuAN3M6vh9xeiD63poz87XOvWUzKDRVIuuylJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=HJd-IvDYcdss85HCagfrT7bBZXJE5r_axc2kx2JJ5S95ALRhd64Ikk390eNAvyctEe6lq4Tu08IRoyuUXi5_RZasdWdYLVOm4uFjd81r2OIYsMubaJ495DF5NzlDnTeStAk5b7yjVHPNUe1E2BzV9PbfnF9xkTwwEI2rqMC-hcZH_W8bnu-HoWXvTFLZB74CrlVJpXx9uAVrcpAlnzsJU7PtwLgJSduwUeKSOasYiMzGTY-QP_VW2E__S8LS0Q8K9V04UfjhrDwimxgBoqIuynOSHgrLvz0dEgEhvdfXD23Z5rLrVuAN3M6vh9xeiD63poz87XOvWUzKDRVIuuylJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه با مدیر داخلی بهشت
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67100" target="_blank">📅 20:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67099">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=g8sPqJuRKDJ0msvyvC9DTVTuSLKiEEF-y68r5NoA6fL_inuMy12Y1nqOy8ZRlNKD9AWaW9K9Ku4FyTk379Aknlo6OsKSVX3WVSzOIqBxgGDKLmFEYnixdILSVJpixFVOggefjMReERvhch58SyEIj8GRZA-raeW88EHPh6owX8-1L9VpCTyv7xFgolJB4m0ZNYBJJyDSxiS5X_9uGvyFXB8DNpaiGOjjXaMBt4RLEyp-oHJINsK7kEjSevbGNx21BMwt3iiWqigTzMJolbGGkT3C_p6xn4XMveQkfwO6LvhFHh9q1RUTDjfCYR85qBthI3M_DYDgi88zwZl36jDqsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=g8sPqJuRKDJ0msvyvC9DTVTuSLKiEEF-y68r5NoA6fL_inuMy12Y1nqOy8ZRlNKD9AWaW9K9Ku4FyTk379Aknlo6OsKSVX3WVSzOIqBxgGDKLmFEYnixdILSVJpixFVOggefjMReERvhch58SyEIj8GRZA-raeW88EHPh6owX8-1L9VpCTyv7xFgolJB4m0ZNYBJJyDSxiS5X_9uGvyFXB8DNpaiGOjjXaMBt4RLEyp-oHJINsK7kEjSevbGNx21BMwt3iiWqigTzMJolbGGkT3C_p6xn4XMveQkfwO6LvhFHh9q1RUTDjfCYR85qBthI3M_DYDgi88zwZl36jDqsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏در فضای مجازی این ویدیو به عنوان لحظه‌ی ترور خالد خالدی نیروی جمهوری اسلامی در پاوه منتشر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67099" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67098">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJ6mFjnKY7KZUwYx8E1G-z0RTfjpT_QF_GlfjRmjKcta9BQ_MSh0piLsxdRgx5MVYF3lbTwxjabfxL7aJv0Si-OEjNXI84RSIhJs3rkQ_QeiI_N01y15jpMhVxxsU9JxRQaS49vgPXRkINIrSkZqHPrrlfh0r8bjHIeBDnkM63IxK79qF6NsHcRxPA5C6a5c_chcvu5K1ybTzHYrNiKqDW-NEjuYQdCq0oiwWCeYS2HuQ72hXFhL8UAl__mXzH6oxYSrM5eLnzdxPuIiYPnu4xJ6hfg35W90CJgMRaLa5YM270PNUlW7K9eb_toX4JlD9hvfSCMbp6lkIfx6ttoSbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
علی حسین قاضی زاده تحلیلگر اینترنشنال:
‏ایران اینترنشنال نسخه‌ای از دستورالعمل محرمانه شورای عالی امنیت ملی را مشاهده کرده است که از مدیران رسانه‌ها می‌خواهد طی ۴۸ ساعت منتهی به آغاز مراسم تشییع جنازه علی خامنه‌ای اخبار مرتبط با مذاکرات و توافق را از اولویت پوشش خارج کنند و بر پوشش مراسم متمرکز شوند.
ساده اینکه از بازماندگان نظام می‌خواهد که چند روز تکه‌تکه‌ کردن یکدیگر برای تصاحب حکومت را رها کنند و به چال کردن رهبر ملعون‌شان مشغول شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67098" target="_blank">📅 19:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67097">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUSQRcLCzIJTAFO81_hiAVhQ5qnrFPR61wqEFOxVAkUcfzqH5j1hosm4Eimlu2Rtt5bDrnryEkRWWiDcuOYqjQrQArR4YzYJmf467ZtdtXZewcdfLvZVICK5AVFQuUmzGRqrXdPyu0iIX8TAtxXf8RWs8Gf_SActMHz9dNrW-3BdEWkbuCHDP8L63GBq2XIF9IFMcJSCcU2pFTzHXysxdr11jFabB6HuOdXqeLAyKcMlCZjN_OwRLaUmHSCTOqFH-wpsFVf1tUDL3DuFAk5bSihEkanSo2F53ZF_NfHLyDTRj06cHIYadIF2x4Q9P0mlx9H_4LY3jw4hxKKZr82NTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ناو آبی خاکی «یو‌اس‌اس باکسر» آمریکا در حال نزدیک شدن به منطقه
🔴
بر اساس گزارش‌های منتشرشده، ناو آبی خاکی «یو‌اس‌اس باکسر» نیروی دریایی آمریکا در حال نزدیک شدن به منطقه خلیج فارس و آب‌های پیرامون رژیم جمهوری اسلامی است. تاکنون مقام‌های آمریکایی جزئیات بیشتری درباره ماموریت یا مقصد نهایی این شناور نظامی منتشر نکرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67097" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67096">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=VtyVRNLWOybvw07xrMXe4h1zEFjmh-7Q91iHXVRTIK9x9xWC3LSHCNwx50_1r2pQjMPTTkNf5MnyQ5DKwKNzk-IwcZfGQ9tvSMFZ2mX0llrD5c-6DC3Yya10QjSt4_YN4WmdHq1fN1yjXjEVrassN7NI-xf8SzXu4S9rRsuXQtetaslPPPgU6iOOsbvpFJ1uxEb6Sce_8SO3hg_BY2WxT8vWfo-w1lESThhsGv8MDxldnnQsFjQO1X3BjUAW_1kc2cslMabnNBtJppd7dwPNzeBPEnB_4jwmfu6fMrFjzftx0qWbEkYzFMIJpdobLZQcFv6s5vKL5J3jmHl7m640sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=VtyVRNLWOybvw07xrMXe4h1zEFjmh-7Q91iHXVRTIK9x9xWC3LSHCNwx50_1r2pQjMPTTkNf5MnyQ5DKwKNzk-IwcZfGQ9tvSMFZ2mX0llrD5c-6DC3Yya10QjSt4_YN4WmdHq1fN1yjXjEVrassN7NI-xf8SzXu4S9rRsuXQtetaslPPPgU6iOOsbvpFJ1uxEb6Sce_8SO3hg_BY2WxT8vWfo-w1lESThhsGv8MDxldnnQsFjQO1X3BjUAW_1kc2cslMabnNBtJppd7dwPNzeBPEnB_4jwmfu6fMrFjzftx0qWbEkYzFMIJpdobLZQcFv6s5vKL5J3jmHl7m640sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
مارکو روبیو:
تفاوت اصلی این تفاهم‌نامه با برجام اینه که برجام یک توافق واقعی با تعهدات و چارچوب مشخص بود،
اما این یکی عملاً چیزی جز یک کاغذ امضاشده نیست؛
متنی که فقط می‌گه طرفین قرار است درباره ادامه گفت‌وگوها، باز هم گفت‌وگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67096" target="_blank">📅 18:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67095">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=l5j75ZivgstMF6vhii5p6hRuyUvlqd4qYkDU1If1XEFpyS9O7LabUVVEIPbBzhNKvjdjtsfGQ455tlY1Ua2_NSN3VZH29eG8ZMSp16Zw03TbzpO2FUJQZRRJd_ppKFPvaqwnJ2gyJmH1dwFhbO9s3IUI-GwkE2fZkXSnnSzfHLzlVnDZk6K2ura7qfJjhK0diykrvCPak8-hnWFJI5S9qldP5pMWel3oIO-dt3wyGNxb2FOTnvFLa2XvXmwV9tiC8JUGcNZt6PoeyYr3c5oqL_7IL1cfL6KYneuP9g7zG66guwzg87o7hVH_rT5XM3XmWAHJ4II5ssFbADjZZWwFLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=l5j75ZivgstMF6vhii5p6hRuyUvlqd4qYkDU1If1XEFpyS9O7LabUVVEIPbBzhNKvjdjtsfGQ455tlY1Ua2_NSN3VZH29eG8ZMSp16Zw03TbzpO2FUJQZRRJd_ppKFPvaqwnJ2gyJmH1dwFhbO9s3IUI-GwkE2fZkXSnnSzfHLzlVnDZk6K2ura7qfJjhK0diykrvCPak8-hnWFJI5S9qldP5pMWel3oIO-dt3wyGNxb2FOTnvFLa2XvXmwV9tiC8JUGcNZt6PoeyYr3c5oqL_7IL1cfL6KYneuP9g7zG66guwzg87o7hVH_rT5XM3XmWAHJ4II5ssFbADjZZWwFLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی روسیه در زاپوروژیه اوکراین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67095" target="_blank">📅 18:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67094">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=qxEfvkaK7x49EICVFDc53erZRZnPYdAMuByx4i02gG4ES2waPXEO4yRY6YSSrxsZYdKYitid5MuJnruFlrptJZAQ7Baa-Min-TV6muDUtQQJO32q2s2bb6SN_Inf6KDnlVVxZjnY1LDcxDS3tIsohTUGeI0v0l5RYMueAlfbTzPRyrmPfrHucUwj9whn9rKw8VkVKtED0T0HLQCWGQnYvlRQ5gqIx3v04QUbCILDpEISaU9wqv3FX3FmLU_Fji1BmDtnxbtbQvZa3AGp1zf2pMkVEcY6qJhNrOhwMziwJBoJvFnXQtvs82UDRUcc8qZQknX4ToVFfznkBmBWKZiOvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=qxEfvkaK7x49EICVFDc53erZRZnPYdAMuByx4i02gG4ES2waPXEO4yRY6YSSrxsZYdKYitid5MuJnruFlrptJZAQ7Baa-Min-TV6muDUtQQJO32q2s2bb6SN_Inf6KDnlVVxZjnY1LDcxDS3tIsohTUGeI0v0l5RYMueAlfbTzPRyrmPfrHucUwj9whn9rKw8VkVKtED0T0HLQCWGQnYvlRQ5gqIx3v04QUbCILDpEISaU9wqv3FX3FmLU_Fji1BmDtnxbtbQvZa3AGp1zf2pMkVEcY6qJhNrOhwMziwJBoJvFnXQtvs82UDRUcc8qZQknX4ToVFfznkBmBWKZiOvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
پلیسا شوهر طرفو دستگیر میکنن زنه یهو میرسه به پلیسا میگه وایستید لطفا میخوام باهاش حرف بزنم یهو بعدش...
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67094" target="_blank">📅 17:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67093">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⏸
🇺🇸
نوه‌ترامپ رفته کاخ‌سفید گردی و با این ویدیو مکان‌های مختلف استقرار بابا بزرگش رو نشون مردم داده
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67093" target="_blank">📅 17:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67092">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c791837da.mp4?token=bRGi1twHjbX8IlRor3yNBtwePsCHrHul-tQ51LoFBf3T3SUWztVOoJooeGu_6CAiLgjlFwWrwtBnvExmEyumNqwMLJ6dc4s9WXfXYKma-ikxfFlDeUmaJEG6qRgQu4XVFeISXNZm2UaxudGS8QFuHmfCoWooyYzHWgp0w1zhwB7Ihm5zOYwJH1YB6_OZfaKaLzvPv3UZZgx_K_E0TT2co1Vn9vk5GWee3jOOn4JZs-xl0VdFWAk9APz4esTxDbXJGaqOaUl3JPEdYOtM17G308Hcp_1UoYo2XXsVYJQIZeWsHwdw_U20gk0d8xyRm42kYFgTcAAOtpa7pnpIGctoP3ydE7Cc1IWLTHwHC97PLO0AI-tKAzp3GxfaQ1jH_u0pLo4sf6qrQ5xgkJRhryMAU9CvNSuTlvQvNVdHeHT2JgMl_MdOmLoJMJbFtHOAsf_jRyMEDL546waj2gQv4RurNLU7_LrE9ur2xCGQxImz04AyDcjRROhR4nwGv09SmMbvb7Hh3NC8qgHbjaE7Wk6aBcDGv0nAgUfUv7GEraMBN0-WYQIJ_vgod29JtawpYUWi36LPVyDwwCkIvMsiYa2QrrZUMruLqpgw2bQX4eduDS8Jfx1P7kckb2ZnSdtDHBjQZMjTVUBjBbxi6ArFP9K6a3OY3Nn57EeH39mf-s6NST4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c791837da.mp4?token=bRGi1twHjbX8IlRor3yNBtwePsCHrHul-tQ51LoFBf3T3SUWztVOoJooeGu_6CAiLgjlFwWrwtBnvExmEyumNqwMLJ6dc4s9WXfXYKma-ikxfFlDeUmaJEG6qRgQu4XVFeISXNZm2UaxudGS8QFuHmfCoWooyYzHWgp0w1zhwB7Ihm5zOYwJH1YB6_OZfaKaLzvPv3UZZgx_K_E0TT2co1Vn9vk5GWee3jOOn4JZs-xl0VdFWAk9APz4esTxDbXJGaqOaUl3JPEdYOtM17G308Hcp_1UoYo2XXsVYJQIZeWsHwdw_U20gk0d8xyRm42kYFgTcAAOtpa7pnpIGctoP3ydE7Cc1IWLTHwHC97PLO0AI-tKAzp3GxfaQ1jH_u0pLo4sf6qrQ5xgkJRhryMAU9CvNSuTlvQvNVdHeHT2JgMl_MdOmLoJMJbFtHOAsf_jRyMEDL546waj2gQv4RurNLU7_LrE9ur2xCGQxImz04AyDcjRROhR4nwGv09SmMbvb7Hh3NC8qgHbjaE7Wk6aBcDGv0nAgUfUv7GEraMBN0-WYQIJ_vgod29JtawpYUWi36LPVyDwwCkIvMsiYa2QrrZUMruLqpgw2bQX4eduDS8Jfx1P7kckb2ZnSdtDHBjQZMjTVUBjBbxi6ArFP9K6a3OY3Nn57EeH39mf-s6NST4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
قمه کشی ارازل اوباش میان مردم در شب عاشورا رودبند دزفول که با دخالت پلیس خاتمه یافت
😐
😂
تاریخ ویدیو 1405/3/4 امامزاده رودبند
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67092" target="_blank">📅 17:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67091">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=CXpoWoP5mx7pCUIMg6Jl5QWTYO1QGccv-u4SODIVVBKZMOOj8j2UPEaRfPNjiaYj5x5MhUbP1US_hZS4SwI0iWPJyUL18h5vt_PgCAfu9HVv7-AiqfKdHdFgsYumWj2kOvh-C5SFjl1DGruzuzoq2Df9wVo6D7PUevCXy2kVRocSUhQ5DYxp7z3IN36CbYu1QKpQBXEk9EyEfjbtW9PMdzgjxYpA1814hqPgXM0VgBdasi5icl6m9PWZAxX_lruRz-e6nsfbJ2SktbIhd2VGQHwttwdIKQcQETggTAtaQM5UI9CkS7HVRV9ML4hmptQQDiv5U7wLmhQ-MaZmqzuxoDRGTGy2cFnPD9LlsZbhPdiWR3qxdzzgFJBgd6GipkvKeZ4jU7s0gFVC6nF-lLfyscTJ4ZVUjQngUCVGBuEdCUFEDenf2NUpd0IWMziNOptohz5ovm2JgVfPS8W5GEkpsC12gVqZQP6BANoarC1c7xz2Nm3VivoOBRli16Bl5DG_a0hNsgOdIBM3B3B0owR_3X0-fWn1R70nO6YHQUQoPJn1zn4h_mLSx-AX-l-NFRlmDToQAsZu4VWy21vzyKOm7p2d_H6rtBZ5tHJDYZdO3aYCW7AziQbKa3odpQrqspDNzbfThcezDkAPjhFY7IbcstT8Q3wR8u7aEd4us2oDs6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=CXpoWoP5mx7pCUIMg6Jl5QWTYO1QGccv-u4SODIVVBKZMOOj8j2UPEaRfPNjiaYj5x5MhUbP1US_hZS4SwI0iWPJyUL18h5vt_PgCAfu9HVv7-AiqfKdHdFgsYumWj2kOvh-C5SFjl1DGruzuzoq2Df9wVo6D7PUevCXy2kVRocSUhQ5DYxp7z3IN36CbYu1QKpQBXEk9EyEfjbtW9PMdzgjxYpA1814hqPgXM0VgBdasi5icl6m9PWZAxX_lruRz-e6nsfbJ2SktbIhd2VGQHwttwdIKQcQETggTAtaQM5UI9CkS7HVRV9ML4hmptQQDiv5U7wLmhQ-MaZmqzuxoDRGTGy2cFnPD9LlsZbhPdiWR3qxdzzgFJBgd6GipkvKeZ4jU7s0gFVC6nF-lLfyscTJ4ZVUjQngUCVGBuEdCUFEDenf2NUpd0IWMziNOptohz5ovm2JgVfPS8W5GEkpsC12gVqZQP6BANoarC1c7xz2Nm3VivoOBRli16Bl5DG_a0hNsgOdIBM3B3B0owR_3X0-fWn1R70nO6YHQUQoPJn1zn4h_mLSx-AX-l-NFRlmDToQAsZu4VWy21vzyKOm7p2d_H6rtBZ5tHJDYZdO3aYCW7AziQbKa3odpQrqspDNzbfThcezDkAPjhFY7IbcstT8Q3wR8u7aEd4us2oDs6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
😳
عاشورا برا این اراذل هرچه نداشته باشه یه خوبی داره و اونم اینه که تا سال‌ها سوژه میتونن دست مردم برا خنده بدن
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67091" target="_blank">📅 16:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67090">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=V1kv3DOqISHbIR5R6v7TFDHdGj17JR7lSCnLDdcMhzo3feozqhA5DClS5q5MS7BAGG9N7b5-rbYMCaz7KL9TbCumslOxcatwgA72jDN43h92gKnKPQqK8AbKKnCT4WcA4JGK1rWLNM2QUaRnuhKjB_cdWQWsTwGYHjjlBlhOn6ftrjByM0KdzPhQrGV0QfsSE21mIY69HnNOolHHI0BpMAlu3tOSeMcdoCjfy1MvUg4wE8SfuhHLUN5J_FZlFRylvr3AugaPdtSKazMvIMTmmrl1WJbwteratFoUx8Ik-Hv2QuJjL2txEM_Mq8b1qsx3IxSKuo1EULkVt0WhZhGBhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=V1kv3DOqISHbIR5R6v7TFDHdGj17JR7lSCnLDdcMhzo3feozqhA5DClS5q5MS7BAGG9N7b5-rbYMCaz7KL9TbCumslOxcatwgA72jDN43h92gKnKPQqK8AbKKnCT4WcA4JGK1rWLNM2QUaRnuhKjB_cdWQWsTwGYHjjlBlhOn6ftrjByM0KdzPhQrGV0QfsSE21mIY69HnNOolHHI0BpMAlu3tOSeMcdoCjfy1MvUg4wE8SfuhHLUN5J_FZlFRylvr3AugaPdtSKazMvIMTmmrl1WJbwteratFoUx8Ik-Hv2QuJjL2txEM_Mq8b1qsx3IxSKuo1EULkVt0WhZhGBhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی وزارت خارجه: اساساً برنامه‌ای برای دیدار با آمریکایی‌ها در هیچ سطحی نداشته‌ایم که بخواهیم از آن منصرف بشویم
🔴
گفت‌وگوهای دوحه دربارهٔ اجرای بندهایی از یادداشت تفاهم است و با هیئت قطری انجام خواهد شد.
🔴
اجرای بند آزادسازی دارایی‌های ایران در حال انجام است و امیدواریم کار به نتیجهٔ مطلوب برسد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67090" target="_blank">📅 16:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67089">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iswywR3GJnPoMNhGDqfOACm5vMgAbrOLqbPkVOZVrYmmJuhED1e4pneBls8sexDlPDCm-_0KtlUVC7MpkvjPrvXkZhv1FwWMBCNaWVPSHY7xL9QRd61hcNOYpttJQT3mkT9zO9G-xowIO3ZnTK8puz6Qg9aPi_7xm-P3PxY5cEG0Aml1l30ejqufT2fI53HqHTngaFUD80b93949S97ycQwpvyl5ZTKMdVyiPBHHr5cM3quBWcSWAA839fz-MEF_fIfc9EMZRLHWdDBDjB53PDIFJa5qUtRgQWpNLm7EYRmUYss8sxAOGdaONPJu595NgNW0bYb87nsdgKNCIyTYQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
مذاکرات غیرمستقیم میان هیئت‌های آمریکا و ایران فردا با حضور میانجی‌ها در قطر برگزار می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67089" target="_blank">📅 15:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67088">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0oVckDT_-6iZ5Q_bf6EIEbkYLDSp2NmvXNWKtLTFspcsg6qoJn3yML3tLSe3_nXBzo-58mSH04pUQdt7bl5b0_jml_jjnwbfV8Npt3ZNbTiZD8fiiGfm-1qAs6IrqV-8iJNucYR03DGchENpE60Rb-yI2XJ_zOCPxcfdr4SH-PGrsXqGKDvToHqv76IdjNcoYGg70skb8D19_HOLUOEc9rMuuUjuDqag9YNXG7HIISXu-dsGcG6OHigYV-DMvAfR4hHPYjQVcZRG6GtTNja6258P650jI3vl8hsXY7q-YYRWR7_mGV9-qggKq-qGcGp00frh2NiBuGJEPmeWHaePw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه همشهری با این تیتر ترامپ رو تهدید کرد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67088" target="_blank">📅 15:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67087">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=Rb61BTAis3PoKQTvT172O1QziLGqn6SmAZVSd0Y_MuJ3YWHK81xHCXKbtzP8JT_CHAJB-GeESO9iVytXo0iDnsvIbwzyzJPnsmeYt_lTEC3w9ubhvhdNSBYzky9RYPQWP5Gd1sTpZ1xxm4Yvt5QsjN9gNdt1LR6WZuJ1XnnhkfnZXqiG95AbwDbjFZvW-0E3x_nb2IZ2P5xZZH6nS1qygThKdwN7UpgUbwjKlo75RpqJWf0NxE7HBO5WxkDL2xLkdL2bpJjcWzii9QWRtkv7OgqFycPd5hMigd2ePVTyU6OpMmXMR5grUsLBUKsScCC5AgB1RNbQwAs8IBEACpUXIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=Rb61BTAis3PoKQTvT172O1QziLGqn6SmAZVSd0Y_MuJ3YWHK81xHCXKbtzP8JT_CHAJB-GeESO9iVytXo0iDnsvIbwzyzJPnsmeYt_lTEC3w9ubhvhdNSBYzky9RYPQWP5Gd1sTpZ1xxm4Yvt5QsjN9gNdt1LR6WZuJ1XnnhkfnZXqiG95AbwDbjFZvW-0E3x_nb2IZ2P5xZZH6nS1qygThKdwN7UpgUbwjKlo75RpqJWf0NxE7HBO5WxkDL2xLkdL2bpJjcWzii9QWRtkv7OgqFycPd5hMigd2ePVTyU6OpMmXMR5grUsLBUKsScCC5AgB1RNbQwAs8IBEACpUXIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
ویدیوهای جدید از زلزله ۷.۸ ریشتری که در ۸ ژوئن ونزوئلا را لرزاند، در ساعات اخیر به سرعت در فضای مجازی پخش شده‌اند و لحظات پرتنشی را که در طول این لرزش قدرتمند تجربه شده است، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67087" target="_blank">📅 14:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67083">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ig36ZzP2jMRs50RJCyhwppEgLz9ZEcuoDdJCUoh9jwFmbzoCIuMdfiXXO8YDRQi3vMqIL2l0yG_ed8vNVoCttS9p0Nd2Kf7AaO36HbOVGsIMAzt49RvF7QsakYdyH2dUcjza811j2Mr9Em8PygXeVGgeoxmbBlI7NCHkGfYIpZRMVzaWs4PdjKMRM3ShsXxVtLHyvyxXiGkTDKPf2CkbEg1BFvcbs3WTJ_P92kOcsP2MvMuG-8esVOrnOEX5OObElNgNnvs4R1WDGtLVfN2DZX-MJn_cWKBTopa-7dhbtkDKPBwY_1z0eDMQYCdQwGPrY0ZVvzAq98BKetUkQtF27w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N0Rw0HC2aR7Z374cGGFy98mX1yPMR8h9A3Ow_VIfiVooFxs-KmsbGRvS1q5vQMAyowBGP6zJ809h-mGXXe-9xvQz61F3YE5LhryBGkJ3gogyDrsyTv0tBZCbM5atuMCvCpq0ijLSkWwzGayVSxGjSb8tEa_AWUIdvDPXrdWX5ZeGV8NZNLGHdBvS46VwNEfDKDPWhrR9tVx6joOLKX43lHQIVWXNRkd7L5hUmILNf7BEZdrAsCyDZUK9hq-rUdgx_4chIhSFVNfz0AYWV173I-cfvqBslDdUA09g4wLSzc0HwjR17F-rLA-CA3Eix4ueWskkDFG5gsgeLLBDL2G5LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tAHTyJBCfRlTpcafVGSk1iyooPq5-EmteuIZRKOaPebvFc2765YQsuEV9YF5A9Rfitfh9uS_DC5L2me1hpN8eY6QTeCTJ1iRO6MoynBDDiEACl7IYqe8hOvvGyQLHVfcOcJfA5tVFvrWLvsS6VWYQAM901IhP_CFMMs6joGudO12IE0K4SNu4_HFAobbtpEuTdiEAwPIzH8C8vR9WXzPzMrCWMr2vqslCDPGHk2pYYOKZVh6u6nB2XyuDFqndy9t1rc-7VIfISPV_bdq7xLr9oz2VRD9IEkjbfi9uc0a6iRxuFHmKfs0dCGbQimN3ltmvySvXW7wBkae8Vz3ELS5dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T7AtQJP_2W6IFIW8Okh7igaxvXOmWae3QHkQcOqO8sXqQh5LA1fUn52w0HiEU-lxhF8cMhX8HjGUQD36tpptNXqjhaXPIg1sTDD5V6WWMUUnY1LMkdD6bMUZlEJhHbFrQMGWhPOl4_uc4GB2LYPHZsA6tibkYcjX953tKd4jutTb1G6idut6BR4rHPXLi0kM0b-U6op_P00QN46tctQJ3mlkpP7WY4ZR9xqO_Fb0ZCKs5eV8YsBWEPhor1yPlvJ10_GkbhjEEIZ74cmPVZR8HNsrysQchbl11sPOg0Uotm_XK7MwDGVhSRyVz5eIbsrppaUkr8Q0oFCFhQXQ6SxWdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😂
یه پسر 19ساله به اسم آقا سامیار، اومده چندتا عکس از تولد خودش به همراه دوستاش تواینستاگرام پست کرده؛
حالا به دلایلی نامعلوم، این پست تولد آقا سامیار تو اینستاگرام فارسی به شدت وایرال شده و بیش از چندمیلیون بازدید گرفته:
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67083" target="_blank">📅 14:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67082">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
⚠️
قالیباف: سوپرانقلابی هایی که هیچ غلطی برای این انقلاب نکردند، ازهمه طلبکار هستند
این ویدیو از قالیباف مربوط به سال ۱۴۰۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67082" target="_blank">📅 14:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67081">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی وزارت خارجه قطر :
هیئت ایرانی از اومدن به دوحه منصرف شدن و مذاکرات لغو شد.
۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67081" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67080">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
جرد کوشنر و استیو ویتکاف، فرستادگان آمریکا، در دوحه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67080" target="_blank">📅 14:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67079">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
هیچ نشستی در سطح عالی میان آمریکا و ایران برنامه‌ریزی نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67079" target="_blank">📅 14:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67078">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/enfKOI18s_FxvhRJrukwP7lnVYRo7HoNNoiDzlCDGloJW7abCvkd0W93gxFBaMF22J6beHalpTlComempIQUChNox5tBZBKaAvcUSCqe2iVJrSYguJAkDzQ85RBG3aois-TsD2Y5Fp65BTAxbRWeBoEsd0i301os4NOHqZjG85Pvd4b5yfVWKbTx3KkN8Umr0G333z5EDhkjKISSkZU6NljWi8OfVmUrdOlQFqEbCXf1mxKEzah3rV8La7Y63pQ3bO-Cv5Cpx6FeSG5btuVFnlK_fXV0Zsjh1Op3STWrAZ68n7_G-64FofclZjoVTuqrd6hAfdihTDTAgHpC5jaHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افت رتبه همه دانشگاه‌ های ایران در رتبه‌بندی کیواس ۲۰۲۶.
این فقط یک خبر آموزشی نیست؛ گزارشی از هزینه انزوای علمی کشور است.
رشد دانشگاه‌ها را با قطع اینترنت ، فیلترینگ، دیوارکشی دیجیتال و انزوای دانشجویان متوقف کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67078" target="_blank">📅 13:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67077">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSWJXPY7GOWDPcZT-G39icd-YrlpvTM4sDnfCntaoffRj8sR-uCbe-Fqh3BqFfl96t16vcsvDUKPfFmRmX2ifku-V3LrrvoXZWbu-y7lJAMT5ClZYKwen7TAQnFB7qMYlK67RXdjh24-VLYdL7D1nvHi5gNegt-Ir18wfWBqLHCm-mMrwjrbcj9ho3xrqwXIAi280rRsLXaLaXlKHL6AfikJ7kx6AnmN5EwhoAcpiSWpgzMGTuI2mhYBexRk7XHcoAVOy_0R_U5Sh4Rf-SkwTDXjrYGZnSqOGCDBIp3txz9cR8wTUUjAu5fyJCCIOjtqhZzI7u4GqXW2yskKbdLxNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
💢
فرماندهی حمله جهانی نیروی هوایی ایالات متحده برای اولین بار تایید کرد که یک بمب‌افکن پنهان‌کار B-2 یک موشک ضد کشتی برد بلند (LRASM) را بر فراز اقیانوس آرام شلیک کرده است. ادغام جدیدترین موشک ضد کشتی آمریکا در این بمب‌افکن تاکنون برای عموم ناشناخته بوده است.
💢
نیروی هوایی ایالات متحده اکنون توانایی انجام حملات اشباعی ضد کشتی را مستقیماً از قاره اصلی ایالات متحده دارد، در حالی که پروفایل پنهان‌کاری خود را حفظ می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67077" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67074">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0_wWDOwhlvg4ih52a_TQpU7WONuaA8arhGJtterOCWZLMERaxAHevMF_2lHdivKGUax_T3H-lCagxwuVKUrxHPjOFQ9mKDvDUZnVT4VMKd6WergrkKzW276VkufvxQEaHrVSlMl8bC8boAMcQaQlvUekMz78_aT2VjWDWLiOtmNdQZnnbvVmCUX_Aw8_3lKjUan4--eR-i0fGe06TSbMf1aa_MrJ8g838nRR578lX0RFFKE80ipdx5adyCJ-RWNfLn0FGgOwNikL03RQ3Jzl4dLjYLlXUFOxBqfEa6w6sF0D2QxNBO3mIcT4UUFOVqny15hVkLk8798SWk0oHDLzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚠️
🇺🇸
مولین، وزیر امنیت داخلی آمریکا: خیلی خوشحال شدم ایران از جام جهانی حذف شد. انقدر خوشحال شدم که رقصیدم. نصف اعضای تیمشون سپاهی بودن و هربار برای ورود و خروجشون کلی اذیت میشدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67074" target="_blank">📅 12:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67071">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h-JTfouUvf7r0iJnEbOHc6Tgn0iFmfxdf56QvVRORk8G_0GI4VuPdf99peGarytnziwAiAeIZyNcuyPtugkCwwueo1IMhDYuUKfUFTIbPA2BfSwB4ab2CCpFcIybD9xHiOpMFLF3p6wXRACDN4l-Yv4vIejZuViLIvI-yfc4KCctwROCDgylep8N0AIUptvHST9zZGPDbLUKScNHbvDdOR2Lsgek9HkhbwoGmymf7qMI-RU1U0unVDeoZ6HcDKax4Df8AM8kfgsUkikiQkMreNbYHngyNhfdQevpldJsi3pzjw8mSDGRzyDhutKXAdjdzZprZSAgSBp1XHun1C5IIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/obkziRbPw98j-THNuzuoGb0nH4LxeF4-7p7OLrxFl48DUcBsjNzqY_kQ1MTFmRUJ1ar3Q0br6IEhLyrtfLUjDgSxjupjuFf6nQBG8V7aouoHtABv3yYeeaP6z2FAem1UX7Ai9c92n-TkEvHRi4yth_wbxMbUk2Xw1pSNakryQ8Jfa3LNJAxXYMZTDQ3G7B2fBJE-tsjVNuCHTRF0dlHNZSOKhe3x09jD41mx1WEwU3UKngSVh5uauXAQc9ugzfbYocUyoa5j6QmJXyov_BOdL3B7NDz6ZUaoJU7bcX2tyvdhqMFxfLg4OmVVHrBZCPI73FnM2Jiq2Zfaeh6zxRpyFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Syc-ijB1cKCzo3CU5Q_jMWlCl8Lmk7o0N_vIzJkA4b3Xek6l8N2g1eNXSDbY-uZoA5f7w7Q5y3BjjIYTd3js3uX9dV3La8rlfhMZOpGvgqeHoQYAJKBIoec8PouGZFfOubze-GGJYgVIPHDI2kE2PEO3aK5uNO5hbF_szMJgFtvUsGubTfJlueH2Tzh_iZOPG5sRwqvk2tifwg8m8zy9v9_l7nLmQfS7VnUCZYi4cSoS4PNNWFT4K0Q-teRKGLplWFqva81PycCcWyA8DOwLIknaLe2KTH2IICD7_kRRR3lzUAeQCNBQl-2_w5CNNjaY9AzNdidQJbdqcuVby0LIIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اشتباه نکنید، این زیرزمین خونه والتر وایت نیست، این بخشی از دلارها و طلاهای کشف‌شده در منزل یکی از نمایندگان پارلمان عراقه. حالا شما به این فکر کن توی جمهوری اسلامی از دون‌پایه‌ترین عضو  تا کله‌گنده‌ترین فرد چه اموال و میراثی از مملکت رو چپاول کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67071" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67070">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-pfq8ac9YCYBTnf3r8j8bM7yswa9Eu7r_bIgQd2uCOH-fO4a6TFaCSrkUXjAsbtiCtejVPiqkkiOKDBvM97CvztYkmMkS6ajsvfcnRIjwZriCmnCxjgBW5OlVBPnVZRMdrn26zRYyJi0rkurmelo9hEko2mGvsYGWut_1qhAocRpoMZvhS2NP_VMdwRBhKHuvVTb0ZurwkdNnexJPwKxjWpe5-UFuQnMs0HC_ToG_KlnM5Uy08xFY5xwrOF0VLqxO61vLZk8WKeBKw2HhUzJ0DYnOKzcoFcUhdyt3YZtLB_14W5Zyn5yCAJD0eikB3laQY13LLJdpV8H8wABc38YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
اموال کشف شده تو خونه یکی از نماینده های مجلس عراق
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67070" target="_blank">📅 10:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67069">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=dLXKywU00BSkMJ99KsP0vn4ZzUzSbmJSiwdI_bs2cgcwfiMN_I3sCxM-P30gvjJ0O7hj5pX_9DoF_LJI3GE6ORXRq7OaPnatSrpJ_QXv9D2fFCzfMXLOv_dsCCIoW_Ezbdwi-t1-7pbyTpBRPqrtkQEsT_lWUOUd6HIUIPZ8_13jqv11_qsZUCelQhJfwP7Lfu4N0Z1ZvobY1TNc5j6RKCmiDQbVWR-Y3gTxyNrLyv0WkO_xRcE0ALgSrvaZSpZtgfi2uAE6bjpDC8IfTR--zBSCRu7T0M_3gTb3hz0nomml8B2i1F20NnD7HUGF6CWPDjctsafkrxdtuuSUYUJcdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=dLXKywU00BSkMJ99KsP0vn4ZzUzSbmJSiwdI_bs2cgcwfiMN_I3sCxM-P30gvjJ0O7hj5pX_9DoF_LJI3GE6ORXRq7OaPnatSrpJ_QXv9D2fFCzfMXLOv_dsCCIoW_Ezbdwi-t1-7pbyTpBRPqrtkQEsT_lWUOUd6HIUIPZ8_13jqv11_qsZUCelQhJfwP7Lfu4N0Z1ZvobY1TNc5j6RKCmiDQbVWR-Y3gTxyNrLyv0WkO_xRcE0ALgSrvaZSpZtgfi2uAE6bjpDC8IfTR--zBSCRu7T0M_3gTb3hz0nomml8B2i1F20NnD7HUGF6CWPDjctsafkrxdtuuSUYUJcdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مداح:
رو هلیکوپترشون غیرت داشتن بهتون حمله کردن و علی خامنه‌ای رو هنوز دفن نکردید.
۱۰۰ میلیارد دلار پولتون دست اوناست، و میخوان ۶ میلیاردشو بهتون سویا و ذرت بدن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67069" target="_blank">📅 10:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67068">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=kQlOYzKitnbGzw2Xqz3sdNpitlOGzIdPZOmLBhpfJ_Msmp3ZVB1DJvxnj_0CcLmBez-hHCQhWDwmA-mIdogqFUQe8tRrpw8qiiTRVLq-Q_ssQEsyTd7hP9-tG59VilNQSSMiQIExIfgCSV15UUm5_vWaYXgL4PHU3-79F9ovZtXtyotqj3VnhSIf6O2MfN0okmU88XAXQaQGG5KWGOExW22Grpb342Ji2g1SKBBK9VkSJ9urPy7Py8Heuh8AVT4o5flZZ3EgdBAF6hhvFjSZanR1Gc4Wu5sZVh59Deh9YRynLnuBYz2LtWlyZsZDeb8Tn-Vl53jGHRjpGUwvCz0vbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=kQlOYzKitnbGzw2Xqz3sdNpitlOGzIdPZOmLBhpfJ_Msmp3ZVB1DJvxnj_0CcLmBez-hHCQhWDwmA-mIdogqFUQe8tRrpw8qiiTRVLq-Q_ssQEsyTd7hP9-tG59VilNQSSMiQIExIfgCSV15UUm5_vWaYXgL4PHU3-79F9ovZtXtyotqj3VnhSIf6O2MfN0okmU88XAXQaQGG5KWGOExW22Grpb342Ji2g1SKBBK9VkSJ9urPy7Py8Heuh8AVT4o5flZZ3EgdBAF6hhvFjSZanR1Gc4Wu5sZVh59Deh9YRynLnuBYz2LtWlyZsZDeb8Tn-Vl53jGHRjpGUwvCz0vbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از سخنگوی‌زن‌قرارگاه خاتم‌الانبیا هم‌رونمایی‌شد
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67068" target="_blank">📅 10:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67067">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=CeGVI_hrY1UharZvubo2GdtJ0Wk8hTJ_v43gV68kaJrNZXEZP99DhOQ3N5Z95U0daUT26EXcyRblJLWEcdGuU9cxED3ZdsKPVJHAk0eMXvT2_KI9etjflawMMItLmhCAQRbLhH4ClVJBsy7k4kWgh1TNCa8ydoesrgK_iKHnjastMfxsyf0PQkKoCwuIR4IDVWOswB-LpDRGE6TFr4WL2Ewoc17wTC2oClcWF-LGMbQ1IFjQvIbmfvlxmVsHYDu25v5EOVC8tGavoBwD9PefIW1WiqhOZmAktMywxzBNfLs_TR3DkuZRKjK2C7OMpL5Qi3sj3l2N_ap3_33VxuoF7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=CeGVI_hrY1UharZvubo2GdtJ0Wk8hTJ_v43gV68kaJrNZXEZP99DhOQ3N5Z95U0daUT26EXcyRblJLWEcdGuU9cxED3ZdsKPVJHAk0eMXvT2_KI9etjflawMMItLmhCAQRbLhH4ClVJBsy7k4kWgh1TNCa8ydoesrgK_iKHnjastMfxsyf0PQkKoCwuIR4IDVWOswB-LpDRGE6TFr4WL2Ewoc17wTC2oClcWF-LGMbQ1IFjQvIbmfvlxmVsHYDu25v5EOVC8tGavoBwD9PefIW1WiqhOZmAktMywxzBNfLs_TR3DkuZRKjK2C7OMpL5Qi3sj3l2N_ap3_33VxuoF7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس تلویزیون:
جنگ تمام نشده در وقت استراحت بین دو نیمه هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67067" target="_blank">📅 09:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67066">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=K9_-anIKYHS2Pswc5KMe9f1_mJc5gmNWiFFygMYltUHMsJstZfffIsILM81BWtefehXLlHVR1PxgL74fAXUsOZOopCGDyOjV_ELokpUfDSh5KUdubZK4HCxFMuooo13RJHwalBU2v0fJ19RKpoOz-QwX1qULgSPiY0Bj0DyUlJTg6D85czBrJcfIdbdO01odMAtRaexJW7MEkhvZrXl8Znd84xTq7gJPBUBpJOEaNTlc2MnywsJarqvshcuonl1kf_HxAp4qXXaeGhAutzt_EveLLauNt09Ih8ItXiC0UeJuFJRD0jLNozSKxAv3YWexxj68jM5BanqKIi9zTA-eZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=K9_-anIKYHS2Pswc5KMe9f1_mJc5gmNWiFFygMYltUHMsJstZfffIsILM81BWtefehXLlHVR1PxgL74fAXUsOZOopCGDyOjV_ELokpUfDSh5KUdubZK4HCxFMuooo13RJHwalBU2v0fJ19RKpoOz-QwX1qULgSPiY0Bj0DyUlJTg6D85czBrJcfIdbdO01odMAtRaexJW7MEkhvZrXl8Znd84xTq7gJPBUBpJOEaNTlc2MnywsJarqvshcuonl1kf_HxAp4qXXaeGhAutzt_EveLLauNt09Ih8ItXiC0UeJuFJRD0jLNozSKxAv3YWexxj68jM5BanqKIi9zTA-eZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسعود پزشکیان در جریان مناظره‌های انتخابات ریاست‌جمهوری ۱۴۰۳ با مقایسه وضعیت امروز و دوران قبل از انقلاب گفت:
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67066" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67065">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67065" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67064">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hscl29TEj1gOgXJBokDmrW8HUQjqYGgfOJEmiBo7OSCQykAj51RXP6244KjdLvYyMJvF7oizR2tXZ3yOFfi7Pc1qMLwMIIJfNS8oYEAt7QdxMZfi8Rwe7yMIBbY2NCmbnlKJy6JFk8LVVEZe3ivjB4dotTGKshAcSjioJ3VJqlz1ySSmQYJmlK0cHdBG7tnmpeStG4Di_7P_EKS00k0VGLDLUg39R-C7d0xoa_qZQCBP-7w8gKHkqzPTLj96czC38vaDO1zBvY7uDzG_24g1luhFE4X3-wPH8QABqbcJe5kAbMaQrh7vrE4_l373dLC1tges7rXdsJlS2nK06KvzUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67064" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67063">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر جنگ اسرائیل:
احتمال دارد جنگ مجدد با ایران طی دو روز رخ دهد.
وی اعلام کرد که نیروهای دفاعی اسرائیل آماده عملیات و هدف قراردادن ایران در صورت استفاده ایران از موشک‌های بالستیک خود در راستای دفاع از لبنان هستند.
او از آماده‌باش کامل نیروهای اسرائیل خبر داد  اما خاطرنشان کرد در مذاکره و اقدامات آمریکا در راستای ایرانی‌ها دخالت نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67063" target="_blank">📅 02:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67061">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdfOkpQc-wwRbAp1nVN5j2MSy4KsMELssBbGFveuVl9AUH5u0sTIHnjR2_MFq_J9f-QilWmy23mmdXWGMyjhhTe6M0l3q4kJSD4_73NEs7dsNEPcB-F_0qtTN72WtfHSf706N7IQJ4lNDaaHkOj_t400U7tBMkkNJMczOnSDu1uhHJDpEUI0N5nkTY1TD--EXU2giFXhlYruev5jGYg4Z2KCOn3TWJCYTVYEVLe0eMnuNLfT9_GSbAY3OUc9iUmwjGLH7RqeCdr0fSxUcZtMri0YL-ZF4Vh8Id_6kbXn58bu4O8Ocgf_ZVbA9XmY6axVhm2_BeT6Nxd8m0T3wDt7AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویری از بیمارستان پاوه و هجوم خانواده های نیرو های امنیتی به این بیمارستان،به نظر تلفات و زخمی ها بالاست.
«کشته شدن سه پاسدار تا کنون تایید شده است.
سیروس درویشی،خالد خالدی،برهان کریسانی»
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67061" target="_blank">📅 01:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67060">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
گزارش‌ها از درگیری و حادثه امنیتی بین نیروهای کرد و نیروهای نظامی در شهر پاوه ارسال شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67060" target="_blank">📅 01:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67059">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpkpfnuOXxR8505DqhN_eVKxijrSQNH3-a0aTjultphL5TzatrIbWz_m2vYWI3S5uya9UWbXnllPMylxzbdicqAsAoTzbfLpwjBQFcZId2Fd5gRcWnYn5osIAyZZYRyBHBJDfbInMbplzHkdxz8aon8k41iQ_qV39dxZFE2FPIHDPVDVzNIM9jYtI05f1vIDVhQLhsyttwdYcQXJuYDHX7H_1NcJv4IEXLqZPofQwneOMduWUI4PInxQQA9hABUjycQFFcXdfIVwqdOsSwZX6XSPJ-1dE9TOX8vVh5YDFhNP491xkkvkFaaOLGqeL4Ee1ZRp8p_T382yHEWCKh7cvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
تفاهم امری طرفینی است. اگر طرف آمریکایی به تفاهم نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم.
رویکرد ما در مقابل رجزخوانی‌های نامعقول و تهدیدهای بی‌پشتوانه، تکیه بر عقلانیت و کرامت انسانی در تصمیم‌گیری‌ها و دفاع قاطع و بی‌پروا به هنگام عمل است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67059" target="_blank">📅 01:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67058">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
این نشست در دوحه شاید مهم باشد، شاید هم نه.
خواهیم دید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67058" target="_blank">📅 01:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67057">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15a452960e.mp4?token=eDqrPiTsCHKM_8Rw3WkgwwOL2FOmyIUAlszTBZEaRKQTDnsKE3WJaIY08DIgLhS7m9rNXHnj2Ijmt7PVTQBSLxbspYoENMHIavClod1zuvbH9G0vU6I24Xvp32FRKk_Xkob-2RTePXSCdJ2knevXjAH4ObBnWMUc96uoLGHpmShoHJMHnLjJbZgSvHBjt2fODj9hUfBz7khRL9uD4WRGBBlvBDNkQJuHfRUEYYxPHKyeMloWH3afPCNl1usINC586CNu4Q9BSqMC1tofIp-2NKYHyEzqPhp630l9Y-nl9gUrf-WpydG-OdwVLdxyaGmdXCc_qQSQl7vh9ff4UL8EOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15a452960e.mp4?token=eDqrPiTsCHKM_8Rw3WkgwwOL2FOmyIUAlszTBZEaRKQTDnsKE3WJaIY08DIgLhS7m9rNXHnj2Ijmt7PVTQBSLxbspYoENMHIavClod1zuvbH9G0vU6I24Xvp32FRKk_Xkob-2RTePXSCdJ2knevXjAH4ObBnWMUc96uoLGHpmShoHJMHnLjJbZgSvHBjt2fODj9hUfBz7khRL9uD4WRGBBlvBDNkQJuHfRUEYYxPHKyeMloWH3afPCNl1usINC586CNu4Q9BSqMC1tofIp-2NKYHyEzqPhp630l9Y-nl9gUrf-WpydG-OdwVLdxyaGmdXCc_qQSQl7vh9ff4UL8EOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ درباره کمونیسم:
این سوسیالیسم نیست؛ در واقع کمونیسم است. آن‌ها از واژه “سوسیال دموکرات” استفاده می‌کنند چون خیلی خوش‌آهنگ به نظر می‌رسد، اما در واقع درباره کمونیسم صحبت می‌کنید.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست، شاید از زمان تأسیس آن. این شامل جنگ جهانی اول، جنگ جهانی دوم، حملات ۱۱ سپتامبر و حمله پرل هاربر هم می‌شود.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست. بعضی‌ها وقتی این را می‌گویم می‌خندند، اما افراد آگاه خواهند گفت: “می‌دانید، احتمالاً حق با اوست.”
این در واقع وارد کردن کمونیسم به ایالات متحده آمریکا است. هیچ‌چیز تا این حد خطرناک نبوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67057" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67056">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKDCbq7cd6ymKLxcSHocpIfGilf2kmbvoPuNAxe_FBBIqAb8I3bHOUuwgHG465fIHMOiq6hcfyyR1icZ5pOdtkEJh5OtCL3_1WwlqJqzYo7K_uNK5d1ACmMy7wBVaVO4A83XB-m6Qb19WZAGCOwRfmGExzCAyk2LXp2TecqEGNFzFmWlTtFAgcbnh7_gKejoCaNC_kTl55WzqWiApo2Oo3gapflBas8yUL4zPRqD-JF_eiyLTLzSk39qme--eXXt0rx0n52fII5t7KB05DHmLs7nOzVPVoR8j6RA4gAxTcFfQOENft_e5Iyp1Ippi9IgpDKHqiH3vto1r7fIFBUC-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67056" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67055">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=HI4Zo3dOGN2_6Ux5hJvAO63CyRpOTBJGUbZpznROXXHPOnRkoNioPyhs_zN4WPitWLE8blebJozxaz8Huw1aVRqbAhQy4duXcbsBfIsnq12k9DBwlDdVbxHL1gckmL7AgvEhDu5_OnOXfJWv03t1kGoGqylgFrNcZnBTjASDpWFStbYUjaQNev6OZMnUTXKiN8uRWDatOffFTp-5w5N5VLr09TbTOJGtk-eL_ZsOhDznInjvkdwa5oZNb3tiXBh3-cDE1Nmh7cc8sXfO6QhmAIcX8AwffyoMAnMDO3gQExMupEyVV4RlFGPYGQITS9r9CkwpxT5AL83syEeG2LP_CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=HI4Zo3dOGN2_6Ux5hJvAO63CyRpOTBJGUbZpznROXXHPOnRkoNioPyhs_zN4WPitWLE8blebJozxaz8Huw1aVRqbAhQy4duXcbsBfIsnq12k9DBwlDdVbxHL1gckmL7AgvEhDu5_OnOXfJWv03t1kGoGqylgFrNcZnBTjASDpWFStbYUjaQNev6OZMnUTXKiN8uRWDatOffFTp-5w5N5VLr09TbTOJGtk-eL_ZsOhDznInjvkdwa5oZNb3tiXBh3-cDE1Nmh7cc8sXfO6QhmAIcX8AwffyoMAnMDO3gQExMupEyVV4RlFGPYGQITS9r9CkwpxT5AL83syEeG2LP_CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67055" target="_blank">📅 00:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67054">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1336110317.mp4?token=Yy72A27S_itV6T3eJLA5RLh4n2ms2RjPOhJldl2X8_CjNRf0W2dyd4_SDE65seTx3jQC9yncO9ji49UtO8pk6L8lXKijmf30t-VW0uGWUCr_mThMKjIgOTmigHjpGSAVusCGtLnA4y9XuVCU938He3yMo_lvDJmO46zGfBj7527wVtkco5QJxoOoM8vmSDsynXo06Pg0-prS9YIuvUawT2EkL9Y_bNDWTa17s7sy6f_FG9-aaQpRZXYA26EtcbfS83k_HG9FqywcPwsXOkwEGEl52Q_qyyvb4OgUKNVZ_dR52h7OWd2qXj9pZIDKvmQfsiJ0z6cn5x6vxRKy9A7Fbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1336110317.mp4?token=Yy72A27S_itV6T3eJLA5RLh4n2ms2RjPOhJldl2X8_CjNRf0W2dyd4_SDE65seTx3jQC9yncO9ji49UtO8pk6L8lXKijmf30t-VW0uGWUCr_mThMKjIgOTmigHjpGSAVusCGtLnA4y9XuVCU938He3yMo_lvDJmO46zGfBj7527wVtkco5QJxoOoM8vmSDsynXo06Pg0-prS9YIuvUawT2EkL9Y_bNDWTa17s7sy6f_FG9-aaQpRZXYA26EtcbfS83k_HG9FqywcPwsXOkwEGEl52Q_qyyvb4OgUKNVZ_dR52h7OWd2qXj9pZIDKvmQfsiJ0z6cn5x6vxRKy9A7Fbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادگاه محاکمه ترامپ و نتانیاهو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67054" target="_blank">📅 23:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67053">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e959102c72.mp4?token=KHN98u-JY9_xfCUJf9Qk-4By-e_lG02gyaeVduAy5IZ7aVXLNKWB39YzJilNU_6amx0FXwx2pLGroGj8wS6kt_q6ixSQd_Ed_Gotd1XobMOKfNkyq8IkXhK_c_kVTmU9Ul1uNkkGVg7nkylyZU-AhYR8uOviDTCo7qPdL5gyWk1XHAIXbTE0epiZc_nY9iPGb3Ihokrc0eXctY9sLXWYYB_oJyISKa9fiQLpc0MSX3KjZkUov2p5UO30U5j10pFoa_vuTOU_Joc7hS0kLch9_V03uNUqBmt_Y2U4tOjJE46dD5idyIHvZk5gQEEovHp6cZEQo-i9mb-ufr3_lm9GJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e959102c72.mp4?token=KHN98u-JY9_xfCUJf9Qk-4By-e_lG02gyaeVduAy5IZ7aVXLNKWB39YzJilNU_6amx0FXwx2pLGroGj8wS6kt_q6ixSQd_Ed_Gotd1XobMOKfNkyq8IkXhK_c_kVTmU9Ul1uNkkGVg7nkylyZU-AhYR8uOviDTCo7qPdL5gyWk1XHAIXbTE0epiZc_nY9iPGb3Ihokrc0eXctY9sLXWYYB_oJyISKa9fiQLpc0MSX3KjZkUov2p5UO30U5j10pFoa_vuTOU_Joc7hS0kLch9_V03uNUqBmt_Y2U4tOjJE46dD5idyIHvZk5gQEEovHp6cZEQo-i9mb-ufr3_lm9GJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عزاداری پدر جاوید‌نام داوود عباسی بر سر مزار فرزندش.
جاوید‌نام داوود عباسی یکی دیگر از کشته شدگان اعتراضات ۱۸و۱۹ دی ماه ۱۴۰۴ ایران بود.
داوود عباسی روحت شاد
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67053" target="_blank">📅 23:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67052">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcdVaBb76xfgxmBox6hMjfhkwfGxawI0N1IkdhVzPwZ5oywYIz60fDBdoE6mUX1StQYm8SINSOPTJ-dcM_32LWVEvXNTUR6Q5lvyGUzgX-tPVpSpY8FeCipTjFOwkYjH0eB3G6SWrdqpvcR_ejeKvzoJgpjxK2Jz_y3DK8fJRFHJQ823Uq0VPOxJSe5o6_JlGvJaORAb4jRa8toY2GCaayKiR3dyBxVufKciwXKBfbKnXlXK02mFRne4qHLrTK4_lC22UhUS3xMJ5fazquwllWSz_75OkjBHD0HhnGUXpdN5VvSC1tcKkGlEZp7AkiV-esXtxs5zmlWWlYKsVVbhFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری فارس
:
معاون سیاسی نیروی دریایی سپاه طی سانحه کشته شد
.
دریادار دوم محمد اکبرزاده، معاون سیاسی دفتر نمایندگی ولی فقیه در نیروی دریایی سپاه، ساعاتی پیش در یک سانحۀ رانندگی بر اثر واژگونی خودرو در یکی از جاده‌های استان کرمان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67052" target="_blank">📅 22:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67051">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‼️
اسماعیل بقائی: هیئت کارشناسی ایران برای پیگیری اجرای تفاهمات عازم دوحه می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به وضعیت اجرای بندهای مختلف یادداشت تفاهم از جمله در رابطه با موضوع فروش نفت و دسترسی آزاد به دارائی‌های مسدودشده ایران گفت: در رابطه با تعهد آمریکا طبق بند ۱۰ (فروش نفت) مجوزهای لازم از سوی آمریکا صادر شده و پیگیر روند اجرای آن هستیم. در رابطه با بند ۱۱ (آزادشدن دارایی‌های مسدودشده ایران) نیز فرآیند اجرایی شدن آن در حال پیگیری است. در این چارچوب، همین هفته هیاتی کارشناسی از جمهوری اسلامی ایران به دوحه اعزام می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به شروع مذاکرات برای توافق نهایی در چارچوب گروه‌های کاری تعیین شده، گفت: هنوز وارد مرحله مذاکره برای توافق نهایی نشده‌ایم؛ طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ و تداوم اجرای آنها است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67051" target="_blank">📅 21:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67050">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‼️
بقائی سخنگوی وزارت خارجه: هیچ‌گونه مذاکره‌ای با طرف آمریکایی طی روزهای آینده در دستور کار نیست
🔴
طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم و اینکه نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیات ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله بند ۱۱ انجام می‌شود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67050" target="_blank">📅 21:19 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
