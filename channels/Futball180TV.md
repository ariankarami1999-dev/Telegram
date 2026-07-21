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
<img src="https://cdn5.telesco.pe/file/c1-UUzRPDMFrpp37Aitenah-07p7dfFkpTx1A6kUPIDn7JMtW6-bjggYRcZZXi85beImwQcNEQ1e8q76v7bf-662xcH5Q_IH2fEDp781lsSLpw6F9EUrPTj8H7xVj9fHtCE1v1S5LZCQD8Im712MoA2JZyjhRWq88mpcxG5qRY8Qf1zoQxUy1bsfbMzNkWRQG0Y-TzN4rDYsp8d0eZJS2ZBSfLY32FudILw2B4VqOrEVnHvH4J5AI7w46ENNiP63GhiN8VLUKCQ-x2xg1LUsWAL7zo4au_PF2GVaeh3sV4taxUZpFpJRrHQWC7U1Dk496tLjxxhSJUQMNPOM_EJ8sA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 548K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 15:36:11</div>
<hr>

<div class="tg-post" id="msg-101447">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53a9000335.mp4?token=Gd1KFX4R-pBIKVvzS3NgPWQOGzKiVdFHT23_6Enxir_WjbEXkTyG1s4W45ocB68pHvclchc_1f5Z4misLPtU8-9dEGj6-SaFOJwyZcb166CDtSHsZtKQfUF7E02PfR3NxAfURVDa3m1tjdFbUMs2yQv_oA2tOVGTr0C50K94DXwbDFwUDd-ZAdglmjSZKCEj6woiuFjCG19as6yumr6jnch3biJfZJuFXv7mg_JxuHdva5o4jFB1ThXCKPJmYRU-jaAs24DnYkjAY0qPupT9GH8tZuYTcqxoI2MzVAJ9uKkFDDNcJh_Tmby4o_kwmu2UnVLOgqwH6x830MJAmqSi6I6QxeFowWluH3BDPB4bQQImpy_EEeMZt8Iey0FHM537pmK5rwASxuPTJg-rv_fOzyCxfxDSwlttNWkJbhDeSNmJs9xQVR5az69W2d4PjT5crMiPcWUJ8ba3PSZ0FAr0kL4xkKArJePgBr-cObrenETI_I5c4nSwHMEi0Q2_SXHHvfr6aJ-qKZwhpDyjHxW3jrSERT_A3olqO_sFb3UgG95j5Kd2XUhodPuxrxemltIIYofuFeoV7_Q7EdxyB5Bd6s1qesx0WDsrpZ-1k1yAex_wtwo-G824pKoGFL8aoTyw6D9u_Avxvujzh6bakLWzUU8fQg3-PXYodeMGDgt9vzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53a9000335.mp4?token=Gd1KFX4R-pBIKVvzS3NgPWQOGzKiVdFHT23_6Enxir_WjbEXkTyG1s4W45ocB68pHvclchc_1f5Z4misLPtU8-9dEGj6-SaFOJwyZcb166CDtSHsZtKQfUF7E02PfR3NxAfURVDa3m1tjdFbUMs2yQv_oA2tOVGTr0C50K94DXwbDFwUDd-ZAdglmjSZKCEj6woiuFjCG19as6yumr6jnch3biJfZJuFXv7mg_JxuHdva5o4jFB1ThXCKPJmYRU-jaAs24DnYkjAY0qPupT9GH8tZuYTcqxoI2MzVAJ9uKkFDDNcJh_Tmby4o_kwmu2UnVLOgqwH6x830MJAmqSi6I6QxeFowWluH3BDPB4bQQImpy_EEeMZt8Iey0FHM537pmK5rwASxuPTJg-rv_fOzyCxfxDSwlttNWkJbhDeSNmJs9xQVR5az69W2d4PjT5crMiPcWUJ8ba3PSZ0FAr0kL4xkKArJePgBr-cObrenETI_I5c4nSwHMEi0Q2_SXHHvfr6aJ-qKZwhpDyjHxW3jrSERT_A3olqO_sFb3UgG95j5Kd2XUhodPuxrxemltIIYofuFeoV7_Q7EdxyB5Bd6s1qesx0WDsrpZ-1k1yAex_wtwo-G824pKoGFL8aoTyw6D9u_Avxvujzh6bakLWzUU8fQg3-PXYodeMGDgt9vzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
علیرضا جهانبخش: در مکزیک زیاد بهمون بد نگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/Futball180TV/101447" target="_blank">📅 15:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101446">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f60626ee05.mp4?token=MEJ7exygErkyjO2cPn-LMnU6oa3goN6hu3J7cnTZ2A2Iutw4TrU-voFqeFXDY4yIjECoTWQJgP9_o_UyHgvK6JkU6ztFriUqVSd7xKn3EHVZQdJSCFqxOgRKOodv7EKg5tmHCfP8DSBa5XkZ384bm9WEwEQw96M6xsqhbkgAV1_EaYNGbFEkBPr4WVB_rmDpB7LXSrRGYze123yWpC3W5jEsMh2wHFZ8ZX_JMouOWzAxjYMEA11I8mu9Gh82XxMVZcYjqwZdxdJS1dCIYM6w-sSHsTld8bWor3SG1HqO1oWGuVBehc_08bfpPj9k4G7C5t7DR3-ku5jBgdlA78O8Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f60626ee05.mp4?token=MEJ7exygErkyjO2cPn-LMnU6oa3goN6hu3J7cnTZ2A2Iutw4TrU-voFqeFXDY4yIjECoTWQJgP9_o_UyHgvK6JkU6ztFriUqVSd7xKn3EHVZQdJSCFqxOgRKOodv7EKg5tmHCfP8DSBa5XkZ384bm9WEwEQw96M6xsqhbkgAV1_EaYNGbFEkBPr4WVB_rmDpB7LXSrRGYze123yWpC3W5jEsMh2wHFZ8ZX_JMouOWzAxjYMEA11I8mu9Gh82XxMVZcYjqwZdxdJS1dCIYM6w-sSHsTld8bWor3SG1HqO1oWGuVBehc_08bfpPj9k4G7C5t7DR3-ku5jBgdlA78O8Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
👤
محبوبیت خریدنی نیست...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/101446" target="_blank">📅 15:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101445">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_YeiiLTyWmaH4X-4Pp40TK58SvpC1FwYmasRiL5vky26KBl1VHSRAZgoWJc4Iqn76iFh0Malplc4jxOSJE7V7kWgpZNAhCbRKn0-HnGPa2g_Au64Jo4f4AuyXtUDVggmOyCDLuJgYTu5athBfloyKWLwPxhpVHAsx_GhsdULAqgsQyfZzftQS_gnULgNJ4c8_ZBzW6LmHR1NJCRhJdlVhtN1Wk1kxnatV5QDpG4QTIVffGwkdege6sQluIvcR7gDFoMc_oNZn6MhEUqZEy5os-4lOHqzIWx0fsR2WssppZDWiEpSuTupAxtCioYLrKSN6qP0P_Kak3Y1R6ZcB8xdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
تعطیلات تابستانی رافینیا و زیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/Futball180TV/101445" target="_blank">📅 14:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101444">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hag7ki8B7t2PcGfpUqBZEPw0VwcwqlTlF-5lZUEqtoJGyqVAYAe9JgnLhDUZ5n4OkL0REOS0aa4_qgptFdEyI30e4sZTdSIKLwGs98vRnAv9_ykjKjqp1e9pMqRQUrhziZV_XxdkZbCUuD3a48pEIBm6_Hq4x5htGQvjbXuMqwZBqTUW0dTtOcVFfSDZMvpYaNRpXA48EY5H7UADXYBrlcrVNSFS3Cu-5a4h8oWN_ua_O8CW_gV6aTw8jM7AW5IjFde_7v-EoE6KXqD7Z4fjczRNt-NOTLzI_huNpRG20HGNeMGba5KjzJhL5hfunxfr0Y2qXbBfQ9q50jte8rH8bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔵
علیرضا کوشکی دقایقی‌پیش قرارداد خود را با استقلال تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/101444" target="_blank">📅 14:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101443">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8a4b410a.mp4?token=B8M6Bf6QyO22vL3GZpiScB0GU_S-i2y5C3J4hD1oigH0xAYWtoYHLURYNymH1nPGuKYRBjHBAt0mlPMTHGiulYcw3vdrI_ndWWv2IZg0l6uD3-_FYsErqv7xb5PSD6CPJHX7ruNJZ9JXu3ABc93zrjVU5N_pOVFBnlRUIn1756hTctmoxMGlPfsnWMe9QCkMlO7NSpc8HRglLaS4huNmf4Yf0SaRqk_D1ASX6rKFIwcJH0gx7H1HpYCdFbRjukq9fselPeuTagfS3scjvuBqQ4ie7pdNWvg8ufXoagQtLepaneFiO7PeZlouIz0WtI90eY8QowXJNgKrACagWuU85g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8a4b410a.mp4?token=B8M6Bf6QyO22vL3GZpiScB0GU_S-i2y5C3J4hD1oigH0xAYWtoYHLURYNymH1nPGuKYRBjHBAt0mlPMTHGiulYcw3vdrI_ndWWv2IZg0l6uD3-_FYsErqv7xb5PSD6CPJHX7ruNJZ9JXu3ABc93zrjVU5N_pOVFBnlRUIn1756hTctmoxMGlPfsnWMe9QCkMlO7NSpc8HRglLaS4huNmf4Yf0SaRqk_D1ASX6rKFIwcJH0gx7H1HpYCdFbRjukq9fselPeuTagfS3scjvuBqQ4ie7pdNWvg8ufXoagQtLepaneFiO7PeZlouIz0WtI90eY8QowXJNgKrACagWuU85g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
عکس یامال روی پهپاد انتحاری شاهد قبل از شلیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/101443" target="_blank">📅 14:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101442">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aD6oYlT3Nm_lBiTb6btSHhjodKvsPH81tp089KsqiccI9hDIPn5GlgGqYcHWmlZnSB4fxhqrNIV-CVmH90GdWq4zJMOL0r5YmG4P22J9n3R0VZgcpHOfM4entr2hHY98sNplSxitIjE7ukpErU9dsY3gGx9USPlE7kM2zhR0TmPse4S4vSPm7kXCpMcueaRdOxsHXd6XDqvZRopp1Rb_Dyg-H50EchSvIGuY9EvMO4yq3VHe3b9B768yRlWXvPqePzlBC_E7rD1Su8qnGmfdb9kjnviokLDHe2F45A6cN8An9t43BmM-FIiSNtwxW0NCkgbLr9c-VKrypIwaqLquUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رامین‌رضاییان با انتشار این استوری تقریبا جدایی خودش از استقلال رو اعلام کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101442" target="_blank">📅 14:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101441">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eouL5Z5Ji27Gig83aBAXLqQlDbOp6aX9g_GBsmtoHx7x5cWxj46B35nC043M9pSANAHb5CAsRYoqzPdY32MfyfafYAgJyk1BycTw1IW1V5Pdm3-77MLHf3oQzhEVEfz_Zl9h_AmjPUp4RoEhyhkvh0vTfd3OW4zJV0Ku1ieoImgpc-VNIOMQWRFY3lnAw3gpWYg2BHj_AfaVLfRCvpwhHTJJDPLl8cUCcs4dRv9Fkk1N7Crih4dDzdTRbHxfbu4Ql9s27vplSH9-G5CZVe00fvLa13UAUdP5nkP54NLtmNyvX3e_KdoHpP7cLYyXXZ2wFbKOaQf6QW2PS2GBszq0_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🔥
لیگ‌های بزرگ اروپایی چه زمانی آغاز می‌شوند؟
🏴󠁧󠁢󠁥󠁮󠁧󠁿
[31] روز تا بازگشت لیگ برتر انگلیس باقی مانده است.
🇪🇸
[25] روز تا بازگشت لیگ اسپانیا باقی مانده است.
🇫🇷
[33] روز تا بازگشت لیگ فرانسه باقی مانده است.
🇩🇪
[38] روز تا بازگشت بوندسلیگا آلمان باقی مانده است.
🇮🇹
[33] روز تا بازگشت سری آ ایتالیا باقی مانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/101441" target="_blank">📅 14:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101440">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0fd702ff.mp4?token=CAMNrIBEL9bVxfqy7D8a4X4fd-9N7bQcu9cxOF61VvBV3fjhATgYL4ZNpud_RA3DMAc8CEzaaRjHMh98KWYOtmC66M-Y6U0LeOwjlkFoaHQ8hhKn6zcqqIev3g_bwQnqoc1xBdo7XqaOAqc409-t_kLzXtW35DL5R42R98WWaV90dYRJdy3T-ThmVPYTulWovUdwgflT3N8AALqhgiGj7AQQ1NTufJX8pBY-wHyYESCPEoAqOxrtfQq72djk6VMQuUzvQZBO3TsHROcCN25UG_OHJS3Hep1pBiHrRxM0eFeutTbBCBw-gAu5SwyM8Wvs3rvB3djQBXJuHbyC6YImnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0fd702ff.mp4?token=CAMNrIBEL9bVxfqy7D8a4X4fd-9N7bQcu9cxOF61VvBV3fjhATgYL4ZNpud_RA3DMAc8CEzaaRjHMh98KWYOtmC66M-Y6U0LeOwjlkFoaHQ8hhKn6zcqqIev3g_bwQnqoc1xBdo7XqaOAqc409-t_kLzXtW35DL5R42R98WWaV90dYRJdy3T-ThmVPYTulWovUdwgflT3N8AALqhgiGj7AQQ1NTufJX8pBY-wHyYESCPEoAqOxrtfQq72djk6VMQuUzvQZBO3TsHROcCN25UG_OHJS3Hep1pBiHrRxM0eFeutTbBCBw-gAu5SwyM8Wvs3rvB3djQBXJuHbyC6YImnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
خانواده سلطنتی اسپانیا در مراسم استقبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/101440" target="_blank">📅 14:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101439">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری؛ متئو مورتو: برخی از اعضای مدیریتی رئال‌مادرید درحال پیشنهاد به پرز برای بازنگری در مسئله جذب رودری است. این بازیکن از سبد خرید پرز حذف شده و حالا با درخشش فوق‌العاده‌ای در جام‌جهانی مجددا نظر مادرید رو جلب کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101439" target="_blank">📅 13:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101438">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e455125710.mp4?token=srurpYpFxij1ZDcAdXRD2QFW8i9HDVVMJanSUKfC9iumg8sMiXzzEnZd4TG4-PMt3e96YOYpwavzUUExrvewHFXsNSQDsFGSvZzEPknjNGeTpjNLGXftREOMTqeUx3EYv8y8gmfYwE0j8Gip6VQUcg5_93szuQly_zZMsl02-3KyWlfz0eW8BTQY1bB3hUOaJ8Uemaz8EvOVglphnsaV_296FM95uq-2UAlW5uSjC5t0VCbj2FhaOu3Ei8mJw9RSg01MUjgTld_D9Si1MS-p4HHfLfmWA9AhbgDrLEmZ6PNKG-FiNr1Yk9q22JCAQp3HnaeDk3AEZV-A4H2rJYEnHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e455125710.mp4?token=srurpYpFxij1ZDcAdXRD2QFW8i9HDVVMJanSUKfC9iumg8sMiXzzEnZd4TG4-PMt3e96YOYpwavzUUExrvewHFXsNSQDsFGSvZzEPknjNGeTpjNLGXftREOMTqeUx3EYv8y8gmfYwE0j8Gip6VQUcg5_93szuQly_zZMsl02-3KyWlfz0eW8BTQY1bB3hUOaJ8Uemaz8EvOVglphnsaV_296FM95uq-2UAlW5uSjC5t0VCbj2FhaOu3Ei8mJw9RSg01MUjgTld_D9Si1MS-p4HHfLfmWA9AhbgDrLEmZ6PNKG-FiNr1Yk9q22JCAQp3HnaeDk3AEZV-A4H2rJYEnHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
دیس فوق سنگین ابوطالب به قلعه نویی: ما تو غار کنار عادل فردوسی‌پور هستیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/101438" target="_blank">📅 13:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101437">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7wpS2OZL6i2F0a0rfSOnjmHDXz6ZRHxYIkxEkVKOxMhGtngEm9eumt6RN91AAD4ikPB_Q_KNczWE1am24UjrfN4a1iW4DPV8dMUaBTP9zbEGeWp0ey8m0MqokPVBgpI-jkkxngRR3bPOi1GwNjtRbT0yHxrOrDvNN-V9Kwasfjwxy6OKrOFkRBasTbZqH3sm6EO0j9DGUl3RpFfapWpqSMuc770YpO6tUqt3oejTOwlyPF5xX9Fxw-PdU3jl2D_h_KCaNhWWhEYyGGc-OZux9yttV12jpFDqe1hCg2EwDcJHVIBfB3oza6wldwpOf9NNPjcy0mus-kyrimlqI8TfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری
؛ متئو مورتو: برخی از اعضای مدیریتی رئال‌مادرید درحال پیشنهاد به پرز برای بازنگری در مسئله جذب رودری است. این بازیکن از سبد خرید پرز حذف شده و حالا با درخشش فوق‌العاده‌ای در جام‌جهانی مجددا نظر مادرید رو جلب کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/101437" target="_blank">📅 13:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101436">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b01qnqpWiSJtGe76zuSFxho60ebc_nIlXhWIjxd_nJbgBMCSQRZAIgUik5NBuN98xkbMr8IEd-28p6ZiLYzd43Oys7zItVN4wfNgLxuLEvdIT4cT-C75fImpDeRv_6gDRIsKV5H-dl7_JZbpMWXz2la_kkH_aZy93vHUOJ1cj09KVneQbThACrmOSiNpqwVcbUCFW3xhwnvZnM4KZvV5SZawC-MZHgw6EQnESuzbXD40Bn7tKTmEgUYSQgy8n0r5tXwK-QEuvD5Xl9VuoZ5shbYaqnQPcm9cxKUpQ_FDYf__yZMsmxQnhvgeaQLRs7pVQIJ4_i6sdPU8oFmYkwyMGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
جسی‌بسو بازیکن جوان تیم کلوب‌ بروژ بلژیک به باشگاه بارسلونا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101436" target="_blank">📅 13:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101435">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_فوتبال‌180 #فوری
🔴
🔵
برخلاف اخبار منتشر شده در دقایق اخیر، باشگاه پرسپولیس تا این لحظه هیچ مذاکره‌‌ای با کوشکی و اسلامی دو بازیکن استقلال انجام نداده و این اخبار برای بازارگرمی و مختل شدن روند تمدید قرارداد این نفرات است. گفتنی‌ست که آبی‌پوشان…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/101435" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101434">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5cbab8fd.mp4?token=VSRsO1WpEoqJ7hTxJgXfDf7919QmqCHqQpct49MVyJPpx6wEZu45IVniWoWpyO51BaF8x8jarVBP8BuY2koYynN1ASkxz2enRJeE7sWTfV6zXxnZsapR6M4Xlcjy9m_g2Q5r5yEcOWpqJzFfAsKhwmxBYwAl70m75m0T8z5SA8skojL5l3Be1XLDyjrStQkRx8dtvNGmmbOx4s63jYu4AFfUeSYivZRt7sHHgi9ASXfft_2gI_5wFbQveqkd6Axfqs4oUPr9Sd7tG9jgTmO4hR1B5KdnCqE8LlAj4eh3a0ThywmjgS1tATjWd6QFmgUMYqyo2sNRzc8utpW_I5yE2juIKFHLZTtwZwKT9ha_U8bgEXvAXnTf6GhElcSnwLyCDqACOsxLtn1MLa7uqZ14Ph9IP9_jOPVWkVQ_-jsOZV80yWJGVMC8MiHMq81Kd39IqbmzCg7ti6Ov0jqmIjdqFR4C3JJ3ydCdLAN_RSav_5O3WSdRBS3fCpQs10vqPyz5KQdRHo8ndT63ahcufiD_e1P9k4Ejf2DNRDWTtin-6AsaiheVWBHaRStloZoGOVI5Sp71qs7Q2R-BQ47iC1uLVevV3hQPssNdCgTjwDAL-olqzF0gQtlPV7fCPdDs5ZSzX-f7_SuqGhOi83vw7aq-KvT3OxELK_t6MorlRt4IGhk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5cbab8fd.mp4?token=VSRsO1WpEoqJ7hTxJgXfDf7919QmqCHqQpct49MVyJPpx6wEZu45IVniWoWpyO51BaF8x8jarVBP8BuY2koYynN1ASkxz2enRJeE7sWTfV6zXxnZsapR6M4Xlcjy9m_g2Q5r5yEcOWpqJzFfAsKhwmxBYwAl70m75m0T8z5SA8skojL5l3Be1XLDyjrStQkRx8dtvNGmmbOx4s63jYu4AFfUeSYivZRt7sHHgi9ASXfft_2gI_5wFbQveqkd6Axfqs4oUPr9Sd7tG9jgTmO4hR1B5KdnCqE8LlAj4eh3a0ThywmjgS1tATjWd6QFmgUMYqyo2sNRzc8utpW_I5yE2juIKFHLZTtwZwKT9ha_U8bgEXvAXnTf6GhElcSnwLyCDqACOsxLtn1MLa7uqZ14Ph9IP9_jOPVWkVQ_-jsOZV80yWJGVMC8MiHMq81Kd39IqbmzCg7ti6Ov0jqmIjdqFR4C3JJ3ydCdLAN_RSav_5O3WSdRBS3fCpQs10vqPyz5KQdRHo8ndT63ahcufiD_e1P9k4Ejf2DNRDWTtin-6AsaiheVWBHaRStloZoGOVI5Sp71qs7Q2R-BQ47iC1uLVevV3hQPssNdCgTjwDAL-olqzF0gQtlPV7fCPdDs5ZSzX-f7_SuqGhOi83vw7aq-KvT3OxELK_t6MorlRt4IGhk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
🔵
باشگاه استقلال با انتشار این ویدیو نوشت: برای بعدی آماده‌اید؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/101434" target="_blank">📅 13:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101433">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8rJE5AzDhndZeZsdo3Zcps67huw-S_idOX0pknW8fO5qgHFkWKpA7JDaPbUq3bIQn7cLlG9V-2QA21zoJMJYR7D62ZodnRvvJOQRn0VWRR3nDzqRwFrLwE--8yKnfIXyJgXtB7QLr6g8IA1WFVnRL1hFnXZ6v8ukdt5N4l2afmcRTJbLLr__jsC2bu48lgnqlvbSQhnSjhNUTEScaCTaFB8KchhMdgPm8g32VGVce1YNTQuRrhn_YATGDEgeAWJLs_1C5rTUT69RqZ-slTV6W_AWBWuG_SxoZ8f7t53V4I1sk7YB_PZ5um_0O1bSe7LPrjXZimX4gAdaLqR4b5NQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
🚨
نشریه(L’Équipe): رئال‌مادرید بدنبال عقد قرارداد با فران‌تورس ستاره بارسا رفته
کاملا جدی این خبر رو زده
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/101433" target="_blank">📅 13:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101432">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7351cc80a0.mp4?token=LfC_jrK7efy3tOx1p9JZLm_NTJL-jCOZKlznUOlrhx91KZmR2ekkvq25yWEEqtL0E2D4VypRvpKbxtyQfw4J6gm7XUuQuuZw2j4l6yxHvbItsMQfzKzlLGeSJFwKQ1rznvA4eRtwolHEo0-QRDB_Nf600ZZNOjA4tvKM74F6-H4WvlEHmUuEq1ZC-1oxohjiCm53L5qoFZ8qMvt-TD-0vwsdShYk6zBQg81Kaf-sKQNubVrXSiyishF8u4e6vSm9V65AN0KOODaBv1ZhUy8dKvk08FslqoOvteoZN7fVS0Z-FFRKmxSeWSMFkg6BDJ6GMS46E3Qpqy_URlKIDPXjKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7351cc80a0.mp4?token=LfC_jrK7efy3tOx1p9JZLm_NTJL-jCOZKlznUOlrhx91KZmR2ekkvq25yWEEqtL0E2D4VypRvpKbxtyQfw4J6gm7XUuQuuZw2j4l6yxHvbItsMQfzKzlLGeSJFwKQ1rznvA4eRtwolHEo0-QRDB_Nf600ZZNOjA4tvKM74F6-H4WvlEHmUuEq1ZC-1oxohjiCm53L5qoFZ8qMvt-TD-0vwsdShYk6zBQg81Kaf-sKQNubVrXSiyishF8u4e6vSm9V65AN0KOODaBv1ZhUy8dKvk08FslqoOvteoZN7fVS0Z-FFRKmxSeWSMFkg6BDJ6GMS46E3Qpqy_URlKIDPXjKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کنایه نیکبخت‌واحدی به ممدحسین‌میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/101432" target="_blank">📅 13:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101431">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0edf1184b.mp4?token=ESHoVIKt3QWZj8XLEL4fXzGsTSwxwH7blDTQfDwqSK-v3tGOxJjijz-FPXO4y544kI2qp8HXYEv4Tb7WhsC2AhOrAGsFwBG9QCV9sSsSqQwziOrsLB7gvb-vJC40PDzgAgWUCH62kbsCKoYcEYyTpF3ahmxhK2xvBa-y31KkxSx0o3VwgnlWmk4Y7MJ5x0RmEje1fBSy2zZOBhZPKHj_B_WQ55xepCwflXRh0HOmTbwuNQjtEKzadlrU7VDHX_1YPGA-VqE200RPILkfkvlmqRIf9inoA19iH1X1A-pYhplUVDnljq8nnchnlmecbgMyawwT2xQWmtImsfsZ1zSPAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0edf1184b.mp4?token=ESHoVIKt3QWZj8XLEL4fXzGsTSwxwH7blDTQfDwqSK-v3tGOxJjijz-FPXO4y544kI2qp8HXYEv4Tb7WhsC2AhOrAGsFwBG9QCV9sSsSqQwziOrsLB7gvb-vJC40PDzgAgWUCH62kbsCKoYcEYyTpF3ahmxhK2xvBa-y31KkxSx0o3VwgnlWmk4Y7MJ5x0RmEje1fBSy2zZOBhZPKHj_B_WQ55xepCwflXRh0HOmTbwuNQjtEKzadlrU7VDHX_1YPGA-VqE200RPILkfkvlmqRIf9inoA19iH1X1A-pYhplUVDnljq8nnchnlmecbgMyawwT2xQWmtImsfsZ1zSPAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
داغ‌عشق پرنسس لئونور به گاوی دیروز تازه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101431" target="_blank">📅 12:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101430">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556a03bf67.mp4?token=uC9mfc1wkSnTpEu90ZSAo-4Si046-kpYnpRsuw04Mjtd1weA3AD3omRN4cB8Dn4buT9rGse66j6yt1FaK0EiUUwZMVcSR0stDIvcsK1TT_SnJS3-04oIZlJJFutKwys4twMS9wvaY34ATeJlOmbkt_4AYJ8eOmgb6K3Id8TbisAFJX9tULS1taNFkarpXEIOVMO-DNbgmnh7bXQ9WOcvZGLaM9wbu-bJrJ2DJvO_S39kGFGUtcuZUNHnnKhkUVODpS0TQGcwEMxmki5J1L0o1P6io_ZTqmEf9Jt0rci94rASw0xtdt4LI77GHQcZbMsUwiDO0HCJ_oAYcVK_YgMIpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556a03bf67.mp4?token=uC9mfc1wkSnTpEu90ZSAo-4Si046-kpYnpRsuw04Mjtd1weA3AD3omRN4cB8Dn4buT9rGse66j6yt1FaK0EiUUwZMVcSR0stDIvcsK1TT_SnJS3-04oIZlJJFutKwys4twMS9wvaY34ATeJlOmbkt_4AYJ8eOmgb6K3Id8TbisAFJX9tULS1taNFkarpXEIOVMO-DNbgmnh7bXQ9WOcvZGLaM9wbu-bJrJ2DJvO_S39kGFGUtcuZUNHnnKhkUVODpS0TQGcwEMxmki5J1L0o1P6io_ZTqmEf9Jt0rci94rASw0xtdt4LI77GHQcZbMsUwiDO0HCJ_oAYcVK_YgMIpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇦🇷
استقبال مردم آرژانتین از اعضای تیمشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101430" target="_blank">📅 12:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101429">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44603a4d54.mp4?token=NFL2bOO4kKRXRWGmNIE9QvZYVQtTmt8f8VsFcO7uSuEol4tBuOEFXoNxAQCs6EnUxvsVqk-5UyZhrArc-JQ7kblmsXd6hUnBvyFbMboWJp0ZmaOBwkpezaVvDWBSNbnA6-y1H1t4yK8xZ9CedTpz6uTPE4TsXFkMl1ewALnvqpUObe0c0Smfc-Uuthd1mUqXSJRhRxVOeKSH9rdgg2FNTKoxo6o20VW6MqNEbXN4PxhpcLy9jQG6GqIpy5TwUZqQyk4cH9-p3pz0HHOCE8vFtW7B928y6pgGcOt7vfQSSRNmgnU3mqyGmU-XGGC3yGV9GgZnKprzm6q3ADWUgexAwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44603a4d54.mp4?token=NFL2bOO4kKRXRWGmNIE9QvZYVQtTmt8f8VsFcO7uSuEol4tBuOEFXoNxAQCs6EnUxvsVqk-5UyZhrArc-JQ7kblmsXd6hUnBvyFbMboWJp0ZmaOBwkpezaVvDWBSNbnA6-y1H1t4yK8xZ9CedTpz6uTPE4TsXFkMl1ewALnvqpUObe0c0Smfc-Uuthd1mUqXSJRhRxVOeKSH9rdgg2FNTKoxo6o20VW6MqNEbXN4PxhpcLy9jQG6GqIpy5TwUZqQyk4cH9-p3pz0HHOCE8vFtW7B928y6pgGcOt7vfQSSRNmgnU3mqyGmU-XGGC3yGV9GgZnKprzm6q3ADWUgexAwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حضور ترامپ در فینال جام جهانی، ورزشگاه را به یکی از امن‌ترین نقاط تبدیل کرد! از بالگردهای امنیتی و نیروهای ویژه تا تدابیر حفاظتی چندلایه؛ همه‌چیز برای حفاظت از ترامپ در بالاترین سطح آماده شده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101429" target="_blank">📅 12:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101425">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/co-DkvzbSi9KWK-ZQknG6a5UHIQI0HNYlFbZlEFBYuzBNJ0HxNED3AUfO6-QjEmrpXuRL0yJDHyksx26D2AkSRLN_PhWoGzrMoUjYP5ZTR0ADuPSNrKS3mh2urJGUAlsQxuObpZlRQjObZeZtUgsAs0tHw-vKfsGb5qBci30CDsBC0VhoBX6QnZlAelWL0IxK3blcTtdg9t6BEQFIAMu52MWYWa7LbYSJmR_u7LjPyqEkFgJWA7Amq-f4ggESJkYB1xa538FHezwC-0aLLzvl7HGDP2Nl0x3__Y4_D0zOlHo9I2soc60xzT-2Mnzo5c9asR1EQZh9gncJbWmUPvI4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IfTeh8xssZa_5JIwUYX8sfGCVkn95cn-wQKEI1TH0sIfLUPBK0Qh-YFIybDFbOYNxmZv2ZfMy21JxONU7LyQscziPilL3h1wfp2vpDYYg32ftq1jXDFfOgUqw74hHtjH9lQKYndOnjFe1hGsdpeLWU_RzwvsyMb3XIbbL2-VO9-mEVi_cpy8avdrlh2Tp-GHWznvIQZtcoBpv3PPrYYMR1eNv-nVH1TTYn_xspSK0Hk6GQmPgasx7YcCLH0oGgfOfRG6eWRzLtNZq0fLZVT0suWSZxP3D_HOdp-3P0Np-HuJrHMOwVObcpDM4S6UkOsFB1ZBXvhQ9fgYx-y-KyEjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z9zJaAB_OUQZX-Jd1SuPvXJMB0uZu55UPsfroDntnbcn6uWgZH-zE_gTQOcQpA96Rbcu6ACl-SRoDIkUI9qRWkxs0QvSM2e3Q12kmsotslt5l9Xd2ELuLXmskT84koqaBRCRmarBS5hN44lXe39zRq0WC3UUOPIuzaSLAHBuTk2jcfvxZWEgP-cbUl5TOFcZgDZxjTiuDfi6rcnlCEom1JK77kfIHOLeHE9H7zrhLtQUr-4ERP4grhF9xgGZqQl2NJvJKWx0Ub4fgt2aCG1JsEgGz8aBnsd2f4nrac-Te6Xqp3s61dtOBPkE7CL_FXtnknfb94gI5IEkee14TXLtWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vcKw5U-jYvB2IuHlxWq1WDNBdOzWi0NVY_tT4gQiK1f0u9aIe7lW6K1s3fQgSZqHsGoFyQjky8aRyrfKuzlqnD52T_pR68doYMglrerkZpgE9EZIQn9TWt-GIbDry0sT0rfca0rse006lQmR4vQI1NtFL-N9trP9p-YrCS9ODO7BIgDo_Yl9OQg4JcssJNeTT56nVbLLT2fixk8YrmDnOuZgHW7nukZJkkII5ESV0qd4sXCTxEKNHYqGckwTrXf9-tmsEZzBjuRY1tZ2htxT8c2ltXlrjRnXj4sZbwvqdcaK3yJbvYXgBcT1F-VOUFswHcPz2bmY6i2hxxGWhsmHRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
رونمایی باشگاه‌میلان از کیت‌دومش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101425" target="_blank">📅 11:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101424">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfPbzucTC6EWk_j21DEQMrrG2FmQ4irsRRTqDFBJ9HJCxVCx-m-ij442a1_s5q87juU3XJqi6oK8MA8gdO48TTQ5fSwbeJ4n2Gqgs_rDPWtCnDs5pT0Ja25L5yXiomUR661wi6z-1awR7oydY-nXVqAD6eO2AQTA2kaLlwzLM4nnordTDfaFeCdq_SocdL5fZo3L4QK0yg7zHkOIpekeSmz3UCtJ8jKcgNVPzL8FohELk6c9FwUJaSvqbUaVeOfDGsLaMGpEYQpxTPNHOl3svudyKFviAMNLqJXtm1yrvyszty2PzPw9XlH_aH8Nii1xWvgNf7s_yEReqpOAiyWBCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔵
بهرام‌گودرزی مدافع چپ جوان آلومینیوم اراک با عقد قراردادی ۵ ساله به استقلال پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/101424" target="_blank">📅 11:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101420">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmrASAEMMOE57-9eYd8SduNq7yfzy5oyHnCcutbhvCjdfGYLfmBFF5oKR6-UlV1AMEe1s3_qmuwDTpPJjBigT4an4W1Co3RxiWT1boxNaFniBwcXyqvJcwOVSrrRcP5UDW4g1MzjE9DxWowK1Q-udhbm29jvw_WeYHQr69heehnrup-zZLUiqf_Zt42CSbdt90ttQ_XDV1MJrs1kXLBN1FfNd35CNfe60uOGKLLQZoVkfEoRwZMshMSvmWUfGVbLrd-OYfSX8GSKoASgnNzW3LapFCn4d5zKOR3Hy4C1dnNNuZTs7_v6WkA1anONqKi36BsbOVUuZ8_Sqz_g9gBZ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/On3EXAHguG5Dg_Sm9SvYA7fkBSYc3BR5oKrTlwV7CiVOYxxNCbRDgmHpK2zu_iMnFu6fmlSmyPj2NGTa47g_H5EYEjcVPPR-sXy7ZQ0I_x96WDOsxdQQMryOKusefEFhM7cjZSfiM_yF2SGhG6OsRarG-jbuPdBZgcZI4mdMBi4izupzDkG-mzbPZPmnp5IO8_1zT4-92jr6il9eVePB-V_m_Wvhj9C1UOAIfKRP82Cr6H3EeNX6PQGFwQjOoF5_Io5o7eMr-lwY39FeYAMcaRid8_WIDhZmVgxxh4pmVNnR51ty63RiXZ4sLZpMx1EfcXOX4o7b1WWRyX2nubCDYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SMnvsXzBBEb9KpUvDCCj0vkNia1CiRc8a5efMVGZzvC0jh6vDYC-SemspudFPbYp7X_jtmqxHjv5rlmcdkswoQfi7W1X6BY8O5F9LGnva7ADQxznhqZuvIlcr4_cnkyUAxXT1F8gTchW0-q1cG--FFTrRIoA4Mvl8xvfWOXS-NvHCOL4a7iEX9_cEowQNGhRmlCEpA5k1kmnkDBxo02XiwqYU0_N04nj7eRTxbrxo4rdrcp1PJjnQDD9Lppz9QhzY4yroUEYrVMavKhCzMBltD5FoQIz_fL7lQoEWGKsDZwSF7_obISzpRLvDU1nDI-cenX6IvInjWlvkvLFVNRn5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O8fYHrtYVviBeGjJopBai7LbxG0f7FU9jZZxiSqmqRj3-0yBogThxVuY9oVHUS0gaFOXTqK9RRNxOh_1xti0jGbs22bQqAfGjwyauIwbKOu9HQElUpV4j6zdo9RiLqvPNmYZretvBfJgptli1a75NwyJ9oChNKwQii6haquDhKt6qLvYEm_JMlT_F1VbTBdO4tY_bJCJeCH-RlIACOGtqCL9QeeiFo1PuPWv9Uo1YdgUFNsiXuGoKuSfmqXoV8HQBmiGp8EfpjA5PD-hENvHpH_Gyi-k7x9_mOkmqlJIozyldUuWejITtSaNnNjXdULtvBwgvb3efflCUapjKB156A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
رونمایی باشگاه یوونتوس از کیت‌صورتی رنگ دوم خود در فصل‌آینده مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/101420" target="_blank">📅 11:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101419">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2kiGjt8ezf7JwDyozsp6_WCSvSnEc0EnOby7mXIrObXYAQTwqa_aBXHyynI5jmVQRkHcUL-r9GCtERtv0-rMxrq34Ue7bmO9E_zRbufbUeXNK5hQxYAIfDhoASXBcATOu9OD56fHPlFirjUFZx6u_wmnagtqIAPRFLvKhT-8J8JIojzxl5MNYRW4OKMDVf4NWznVA-Tbc4uj3pR_cGftoxA_Q6NtxwBzIqXkDu797JiSvU6TvMrNgJWHSabgotRt4gjN_tfCADxYjZ4vsOfc_qjhHzA4sNp_ngwFmHW1hpAUkyX1avVM87zjR_PmhyhuUsdjq1ahNb0KG6tviV4Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180 #فوری
🔵
باشگاه استقلال با چندین ستاره‌جوان لیگ‌برتری به توافق نهایی رسیده اما تا باز شدن پنجره نقل‌وانتقالات آبی‌پوشان، هیچ امضای قرارداد رسمی صورت نخواهد گرفت. هرچند شانس بازشدن پنجره استقلال کم است اما پیگیری‌های وکلای خارجی این باشگاه…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/101419" target="_blank">📅 11:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101418">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e1b98bea2.mp4?token=GL4E7V8GCJ8t-F25cJbIV_wO8mHFI3bR20ZbI2oGmFWMY_lDFTuMeQew9AOr2tJMl3YqWp6u6ujb6mAEEHqtbli60yi_MzF2t88INQF8ZYI9PXhop8OngofKbKLbiI1ieJGJJAlzRWkQT_NslyBuurTn3SFA9zZEdtU7V728prHrMoUAr0cX2G6n98NJDBxB3-WCOS1EP4qrDS_239ORl9ktCE2mrjJ6gg48IuhHENcpEYNuTIeqHAgp7XkMmJy5gQMqRADnD5v5YWHsY1rZdfJCK8RzconSVxIynfzypemiaNibmfjpjFDuDG_hybQtuw9VRTi8GDqltp8iP32RiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e1b98bea2.mp4?token=GL4E7V8GCJ8t-F25cJbIV_wO8mHFI3bR20ZbI2oGmFWMY_lDFTuMeQew9AOr2tJMl3YqWp6u6ujb6mAEEHqtbli60yi_MzF2t88INQF8ZYI9PXhop8OngofKbKLbiI1ieJGJJAlzRWkQT_NslyBuurTn3SFA9zZEdtU7V728prHrMoUAr0cX2G6n98NJDBxB3-WCOS1EP4qrDS_239ORl9ktCE2mrjJ6gg48IuhHENcpEYNuTIeqHAgp7XkMmJy5gQMqRADnD5v5YWHsY1rZdfJCK8RzconSVxIynfzypemiaNibmfjpjFDuDG_hybQtuw9VRTi8GDqltp8iP32RiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
پایان‌یک‌عصر طلایی از سه‌اسطوره تاریخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/101418" target="_blank">📅 11:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101417">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3c9a3d75e.mp4?token=HWkqN_knp1usw_HbXN_fdKbVbA4OgjVtdxBWQsgiX22YqyilGF9NA0rmZaeCGuM6FqKI7fUnbz5wxigLaslbGv3_6idNsR0DuvUhcrheeDf09RHXXUXMDO-C8pqeEQ8gFBR3xQCbyJgQaqUHMFKHiSrdSZeduMQJ5zgeZRus-h8QWdARNb6lAyUxJC_RWRqSZ0SeSsj36j8SQT7bYSR68Ba-io-pb4-tAOB8bso-8BYJgiedCaqOT1JYOGMqA-dlsAePy4poif23nr-jleDypyNK4q8poXha36bWiPzRGrGTS67KAcQ0VKnrAQ1X53iV2PAUc_tDkDXbupIDEFK2UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3c9a3d75e.mp4?token=HWkqN_knp1usw_HbXN_fdKbVbA4OgjVtdxBWQsgiX22YqyilGF9NA0rmZaeCGuM6FqKI7fUnbz5wxigLaslbGv3_6idNsR0DuvUhcrheeDf09RHXXUXMDO-C8pqeEQ8gFBR3xQCbyJgQaqUHMFKHiSrdSZeduMQJ5zgeZRus-h8QWdARNb6lAyUxJC_RWRqSZ0SeSsj36j8SQT7bYSR68Ba-io-pb4-tAOB8bso-8BYJgiedCaqOT1JYOGMqA-dlsAePy4poif23nr-jleDypyNK4q8poXha36bWiPzRGrGTS67KAcQ0VKnrAQ1X53iV2PAUc_tDkDXbupIDEFK2UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تک‌تیرانداز‌های مت‌لایف برای تامین امنیت ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101417" target="_blank">📅 11:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101416">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fcd52d97f.mp4?token=Ud-TiYhLHiobie1hpxl_fEAWQMqNZhxGtnCyMzrO_P0H-mudGK2eiM9apc2A7pjt5lSB0tLYyRLTl6NPIyAa1v52Xc5uj5twZ-9Ebwvx0hJ8GYlRXTmhJpOmARZ2mv9xp8rmhC1TtC_2KC6T9aD7VSRndwKco3AqZlha4azSlE71kaBVvp4aPTfiwEpVPl8SQJzieuPaFcl42xfdxUQm32XCP98nD_SuTctrfew7Fh77Zi1LUxs6GU7IVXZmtA10XYw8F65SqWFqdJSjlc22Ampiga0nNiHvNDIdWPLkqhTfNxZeWcfDb12IdxX0wtaHL1Lo0N0dsih5YSDr0UdI8038khtf4MTisMnQHiJByY8F5MY_VOcVRZM5t-AeP10LH2a2XhvUbDcsvdWDlrSwRkFSx7Dv_pEyrDP6LMj1rDKeC5OCffolNbVHGLt6hNV2g8FHOGc48LK0b_BHZ3zOPinwf3eWLCdhg2TJpn9EW9gUfTkv_amcnTDNzROdBGgzIAGSd6_38SRNpqZSl8N_vYgJHHgIQyQjbYB5LbJ5aMbyXTAi12Vq_sNuqybRk5u7QykbpPENssv8JyQwp82NLa8d73KUUeRv438E4jd12UNpQGCtR3SrJRRNzo9mEQp6AfdvfCvPtRlKiipmslLXbla18nVG_zVZdr8-LVpe8GM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fcd52d97f.mp4?token=Ud-TiYhLHiobie1hpxl_fEAWQMqNZhxGtnCyMzrO_P0H-mudGK2eiM9apc2A7pjt5lSB0tLYyRLTl6NPIyAa1v52Xc5uj5twZ-9Ebwvx0hJ8GYlRXTmhJpOmARZ2mv9xp8rmhC1TtC_2KC6T9aD7VSRndwKco3AqZlha4azSlE71kaBVvp4aPTfiwEpVPl8SQJzieuPaFcl42xfdxUQm32XCP98nD_SuTctrfew7Fh77Zi1LUxs6GU7IVXZmtA10XYw8F65SqWFqdJSjlc22Ampiga0nNiHvNDIdWPLkqhTfNxZeWcfDb12IdxX0wtaHL1Lo0N0dsih5YSDr0UdI8038khtf4MTisMnQHiJByY8F5MY_VOcVRZM5t-AeP10LH2a2XhvUbDcsvdWDlrSwRkFSx7Dv_pEyrDP6LMj1rDKeC5OCffolNbVHGLt6hNV2g8FHOGc48LK0b_BHZ3zOPinwf3eWLCdhg2TJpn9EW9gUfTkv_amcnTDNzROdBGgzIAGSd6_38SRNpqZSl8N_vYgJHHgIQyQjbYB5LbJ5aMbyXTAi12Vq_sNuqybRk5u7QykbpPENssv8JyQwp82NLa8d73KUUeRv438E4jd12UNpQGCtR3SrJRRNzo9mEQp6AfdvfCvPtRlKiipmslLXbla18nVG_zVZdr8-LVpe8GM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
پشمام بنگلادشی‌ها بعد باخت لیونل‌مسی اینجوری حالشون کیری شده و غش کردن
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101416" target="_blank">📅 11:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101415">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhE8OSHk4Nb6XbG5v5u-gwLAxIYPCFQ7TbCZ-k_3d--VGa88efE-bf0PAm665Xd8LTxnEsmZ-JjEkIw20oH9yIPIIhU1zMWoPQDbDJhizvtcQnLs5RRs_rSMAqk4v7ucN_FKZI6z-fpoDXUzgB86iqQOnRAhQyNr1C5YbPhEVvlrm4s4Hv2BkfEOQgTUfs_ZCoENnuSdLRHl8MNT78lZSDiX5wevGCSNB8kMZcB3TtNknahQNoGV7SAaIZozhB8rXNM4y2ekqE7FjLsx2YM4BFsBB-uH4XzEgfKUr6m0Kocr21nxeRx5nCG_qDYLVI3xQDKPSUs6kb1YfHvVG-EXZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استقلال در فصل‌آینده لیگ‌نخبگان آسیا در سید اول و تراکتور در سید سوم قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101415" target="_blank">📅 10:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101414">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a52a115e8.mp4?token=FH5Mhq38mwbifoxDN9cbIpZJb-YG9rHwL7ULHEUJLGMBGsnMZ9SvxxKzfgSWvSx4LBFVjOf_ZKsWuD_EVIQtyxc7Acbm_9rnfFWqyJb4aPxhoXVqXBsRLzZZnQvK_1tkcFZU1p6_KkM8LpLwP7TI1gQ0jpxptMvHjLn1b15WHqS7PkKVsN7av8kqbzQyAdpEXYy0mqOm_BshX2bDISbeQ-31SyAGFBPa9UwPlw86cojoUxWBLly_tkZfpCIp8X3PJ_cRF1chp8iWQVNxrJ3Hsy4xH33xdl-2n08Cb8y8NYCGuDneeZRTxYoD3XGNE0arQf5u9ewCeRgDcZOb3ZYxpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a52a115e8.mp4?token=FH5Mhq38mwbifoxDN9cbIpZJb-YG9rHwL7ULHEUJLGMBGsnMZ9SvxxKzfgSWvSx4LBFVjOf_ZKsWuD_EVIQtyxc7Acbm_9rnfFWqyJb4aPxhoXVqXBsRLzZZnQvK_1tkcFZU1p6_KkM8LpLwP7TI1gQ0jpxptMvHjLn1b15WHqS7PkKVsN7av8kqbzQyAdpEXYy0mqOm_BshX2bDISbeQ-31SyAGFBPa9UwPlw86cojoUxWBLly_tkZfpCIp8X3PJ_cRF1chp8iWQVNxrJ3Hsy4xH33xdl-2n08Cb8y8NYCGuDneeZRTxYoD3XGNE0arQf5u9ewCeRgDcZOb3ZYxpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مراسم ختم مردم ایران برای لیونل‌مسی
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101414" target="_blank">📅 10:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101413">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBklY2l9aDpAREKz1pamfdEdc6X_BfVt-iPiKiY6z0cxIZ4ndreKyWepBZMG2_IbiCULFBorWIdeA80uYYeh-MLsWoxQ2Q5vcOmU1-zjI_gBLR70QJyX5W8moTi_jutX1ruhspVwJX5JcRZCnE5A_E254pi_537usW4SDv4sxVC2c8wkGgs8p9G7NQd0YWkogATGIQxeHEOWSlIKFIxZvxq_XgZDUOlyiKDxpN2MTlASB_AVHcnXQd2e83s1NnSU-dtLYsOD7ppi1Qgq3IImbAZmgZEUmdEO4FJafAdD2SBqmohQgx82I_Q40SZ8dA5litF3FnoGblnFn36eFGzYpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لوکا مودریچ در ماه اکتبر از فوتبال ملی خداحافظی خواهد کرد
بازی اسپانیا مقابل کرواسی آخرین بازی او خواهد بود.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101413" target="_blank">📅 10:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101412">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/342ba6a359.mp4?token=so-Yr_imqOG0cXiVvapEc2cyA5f0iTuZBEGrhJF71OBPguoiSc1gJs0Qo5vKbq859gYt4sKnNZdQ0PissccmkwFn0J6QzmB_Y8kM_lducnh9my2472oNXUA_pTAplNFVvkrZeMxnTtPXFfJ1BNKhH2ueMhdgSsdHPOlHIJrl1Sf6pZe2zUodvBeOFz8sD_wZh_te0p1z_zSol0PkuVYPvmcynHSgaGDVlunCHXzQOSVTSeRDN46CrOwEcEKAkCO5l1DrJ7DtlFFehM-G4-gzGa_o8Q5nlhe0PVuO4nJtZR7cBA22NKK1ZPuy6b1IjY_GOQSguCfcP6c6xmgAkKdASg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/342ba6a359.mp4?token=so-Yr_imqOG0cXiVvapEc2cyA5f0iTuZBEGrhJF71OBPguoiSc1gJs0Qo5vKbq859gYt4sKnNZdQ0PissccmkwFn0J6QzmB_Y8kM_lducnh9my2472oNXUA_pTAplNFVvkrZeMxnTtPXFfJ1BNKhH2ueMhdgSsdHPOlHIJrl1Sf6pZe2zUodvBeOFz8sD_wZh_te0p1z_zSol0PkuVYPvmcynHSgaGDVlunCHXzQOSVTSeRDN46CrOwEcEKAkCO5l1DrJ7DtlFFehM-G4-gzGa_o8Q5nlhe0PVuO4nJtZR7cBA22NKK1ZPuy6b1IjY_GOQSguCfcP6c6xmgAkKdASg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
همزمانی شگفت‌انگیز عصر مسی و رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101412" target="_blank">📅 10:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101411">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/061bd5d306.mp4?token=aeS9Lyv_L6ZS23rARYzaZqDOJQRJodYVeOftWctu6B9vfvcHEe4aeqTzqJIkekbvKaeZn2fqbQiuDZmZEYniPv0pq4ROE87D-hLY95kgrtzAcqJFDwDhGhlT-itlmKsCUwXd86Ouly1zOdiY50WIvzUmXlqDkWv36Urm8GkfHQRr4lldqrhwcEwGz2dFtkQUiSDAa6n1cwGpDAbJH2axwX3wcXTozrsaOiYZp_A49o0aMvXUhw--LikC1JqyZMm11vklnYlxY_0I5ey-T-R_g-h0bl1fsTllDPeHe-hxUqOTNfFzCz33dDWzMF2EmkzcX0g_OQqp07vTbqAiNIQwWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/061bd5d306.mp4?token=aeS9Lyv_L6ZS23rARYzaZqDOJQRJodYVeOftWctu6B9vfvcHEe4aeqTzqJIkekbvKaeZn2fqbQiuDZmZEYniPv0pq4ROE87D-hLY95kgrtzAcqJFDwDhGhlT-itlmKsCUwXd86Ouly1zOdiY50WIvzUmXlqDkWv36Urm8GkfHQRr4lldqrhwcEwGz2dFtkQUiSDAa6n1cwGpDAbJH2axwX3wcXTozrsaOiYZp_A49o0aMvXUhw--LikC1JqyZMm11vklnYlxY_0I5ey-T-R_g-h0bl1fsTllDPeHe-hxUqOTNfFzCz33dDWzMF2EmkzcX0g_OQqp07vTbqAiNIQwWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
استقبال مقامات دولتی آرژانتین از تیم فوتبال این کشور در بدو ورود به بوئنس‌آیرس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101411" target="_blank">📅 10:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101410">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔥
▶️
اجرای زیبای شکیرا از این نمای دیدنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101410" target="_blank">📅 09:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101409">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
❌
⭕️
سروش‌رفیعی با انتشار ویدیویی رسما از تیم‌پرسپولیس جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101409" target="_blank">📅 09:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101408">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_C1YjHMJrHKhAGOrGJsKfkVa98VjBF1YqgGTMIp9jFNV-CGfLARK6PrTXEtR6X3HWPqlqZpvrxSSICWshj0pa6aT-VvGIScI2MIBem4pt3aM0fy0OVSviU_Aaw9a7pHbAHtvvuIyCFq-DSFjk_DjnC8Ng2ryLOq1MDeR8xv2EwPWq4gPTHhSFjDw7SPofj3Xprxm4J2-a50FTRXf5Dd9FKEFxeJomB1rzWBjH20ZR07WPdk6LFM-SdnO3DjFQFggVslq-f4St_SVx79vs27rH_4MdMXZbBpeaNvvkR3oMS-kP5mPB67s7N34IE9Da6oHhZoq_CVS1msflUEe5B0XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برندگان جایزه توپ‌طلا جام‌جهانی از سال ۲۰۰۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101408" target="_blank">📅 09:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101407">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18768f80f3.mp4?token=fAHad0-HUOVOwegMn6YCKg9jPeTQ-uojQaCggqlxqZ6Fjok1JRKn1VfPdN_rIIuK-HCvcbTUsRxuMHPfS8ehtBxpc1_vUbrJ4V5BGrqJVIjmiyOK8EM6gl3giBPdJknkn1n6tZVIKfwgfAI2TpMWcfUpNxAj_JyTj3pMvYWDF2W9VYkTGkcTaS5pDgEVGHok_vsRgFhskwqH_6W2QfprNcuo4i1dNI3fPNsxrleN5DYw4mKz8FKrahRJnVcK5LKSqkSye-5xn7DJgqx4fbrA2RB4Q6JkDv7RuU2XthP88NWDKUDEx_1ttqLMBH8jpoCnKNqQ9Zar9_8y00I7_EQjCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18768f80f3.mp4?token=fAHad0-HUOVOwegMn6YCKg9jPeTQ-uojQaCggqlxqZ6Fjok1JRKn1VfPdN_rIIuK-HCvcbTUsRxuMHPfS8ehtBxpc1_vUbrJ4V5BGrqJVIjmiyOK8EM6gl3giBPdJknkn1n6tZVIKfwgfAI2TpMWcfUpNxAj_JyTj3pMvYWDF2W9VYkTGkcTaS5pDgEVGHok_vsRgFhskwqH_6W2QfprNcuo4i1dNI3fPNsxrleN5DYw4mKz8FKrahRJnVcK5LKSqkSye-5xn7DJgqx4fbrA2RB4Q6JkDv7RuU2XthP88NWDKUDEx_1ttqLMBH8jpoCnKNqQ9Zar9_8y00I7_EQjCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
بسیجی‌ها گله‌ای ضد مسی شدن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101407" target="_blank">📅 09:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101406">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33df2c440b.mp4?token=lhkDlNjeyAgOO4pWvo835QyEno9etR7weAzSBm92nQZ4AagxhElqgkxGlinM2o8nMoFW5fgXuqXT2MGimVi7CLLZxSX_9aRNHN3XI8CqPLunbdF7rUnqGl0Uyw9Q1eDVxTaofyAjoY-StTzSXTjFpmFOez6itV5qLgfTUHxT0LdxQlpZubI3zyBwTh6AOBuB5Ur5q8VUe9IYxsVtOJeSggF8_VTYjX3kqxHhTW_S411H50MyQS2eZjl4SNXcye4qPeBa8c6ZCc3PtK8XOiln_U1AFk6T02Nc0rmFP8SZ6d6corLtfk1OBR-QwAHWy1A-Ex4HkC6nAHwboJ5Y3jCJDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33df2c440b.mp4?token=lhkDlNjeyAgOO4pWvo835QyEno9etR7weAzSBm92nQZ4AagxhElqgkxGlinM2o8nMoFW5fgXuqXT2MGimVi7CLLZxSX_9aRNHN3XI8CqPLunbdF7rUnqGl0Uyw9Q1eDVxTaofyAjoY-StTzSXTjFpmFOez6itV5qLgfTUHxT0LdxQlpZubI3zyBwTh6AOBuB5Ur5q8VUe9IYxsVtOJeSggF8_VTYjX3kqxHhTW_S411H50MyQS2eZjl4SNXcye4qPeBa8c6ZCc3PtK8XOiln_U1AFk6T02Nc0rmFP8SZ6d6corLtfk1OBR-QwAHWy1A-Ex4HkC6nAHwboJ5Y3jCJDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال وسط این همه آدم تو جشن قهرمانی اسپانیا شرتشو کشیده پایین و میرقصه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/101406" target="_blank">📅 07:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101405">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30588621a9.mp4?token=taGnY-Gl3Rxtx4Ta07ojiVPV7JLeCu_udcguzVQ9jBkq1T-DNli951Q5Sr9wNiJO4AAaAL5hC-T68njsHxhh9X1wY35vy5PTKsrzC9XPC_Zz50XSA94dLN8NCmGtnMrNJXbHamVfVpvNHBbX67ssHO3eBEtjIM4gBPS7c8hs5hia-uN0e27sHfJe6_c2FFN4SQMDuFWICBq3JF2xboT4uMfxE_rRVItjwYpcCa_CMJnLGD97Xeni7Xc4tL7OymQWBOLwQYzJ1_igQRj6WGpOATL9UDs6bFZQg5Vpz3tBYnQIPhIgC0JEIV9QCJZJcxglvVb5Wvw1sjgUDLCFB1h5Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30588621a9.mp4?token=taGnY-Gl3Rxtx4Ta07ojiVPV7JLeCu_udcguzVQ9jBkq1T-DNli951Q5Sr9wNiJO4AAaAL5hC-T68njsHxhh9X1wY35vy5PTKsrzC9XPC_Zz50XSA94dLN8NCmGtnMrNJXbHamVfVpvNHBbX67ssHO3eBEtjIM4gBPS7c8hs5hia-uN0e27sHfJe6_c2FFN4SQMDuFWICBq3JF2xboT4uMfxE_rRVItjwYpcCa_CMJnLGD97Xeni7Xc4tL7OymQWBOLwQYzJ1_igQRj6WGpOATL9UDs6bFZQg5Vpz3tBYnQIPhIgC0JEIV9QCJZJcxglvVb5Wvw1sjgUDLCFB1h5Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤣
ناراحتی امیر قلعه‌نویی؛ برای اسکالونی کلیپ ساختید اما برای من نه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/101405" target="_blank">📅 07:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101404">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3R0EXmPwpD3G_Ue1tPHM5nKKlGPj2ZrRkZsU_kZYuHh60Eun0k6UgnNykpeOYQrhVFlPyFbk8FWdny2xWyao9_YxsE9nfV4-_u6Ha6xAdStMXwKKAsTQshvNubJZlneyTH3GMGzOyPRvVaOpjWG-10J9Xr5R20uzayvoJVrzYVp2qshNapvvYw57fJ9iJWR6F8OEXDhpuFcOVZxsjlF_JftxifQF5BgrYp54KaeRlNUqe7imDxoNt1PCuvylT2AAmIFFhaVu8yWrR4-vNRSaR3qyqDdglhkxYIgdpDXFnhBXmlc8axWKXu6U8aIhi5pEWqqaqw8BQk8nvBrWZ79eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
فوری از هرنان کاستیو، خبرنگار آرژانتینی:
لیونل مسی به هم‌تیمی‌هایش گفته که فینال جام جهانی، آخرین بازی او با پیراهن تیم ملی آرژانتین بوده.
😬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/101404" target="_blank">📅 03:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101403">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvyewI5ixQmqRX7NKfZv90GAp7pIVabUdetDf99rP9HmA5jZohN3lBuUI0lGlGxd_QZCXl0P1v2nNJl2h1J0COt38etQrpJqb591HkPpwrtnl55soPyBv87SSFRtfYxgQH5GsD-WjjQG9dfg8pVqQK_YATEMjFwfLgDAKILOekB8lV8c78QV6iLo59B5lSq78kTlRJgswEslUc_yLqeVujz5OTufK9q7FO-4RZnF2hqDyTpog9iYDArryrVIeDgw8929IeSZYaXDB0SP_-pr3IMasEMHMnoN35_lpcaWfM_bxP2Tf_kicyNlYBdr4OAGcHNOp6mLmOZbvnqxgiwVSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇴
||
آمار و دستاوردهای ارلینگ هالند در دوران فوتبالش به مناسبت تولد 26 سالگی‌ غول نروژی:
🏟️
[419] بازی
⚽️
[359] گل
🔴
[66] پاس گل
🏆
لیگ برتر انگلیس [2 بار]
🏆
لیگ قهرمانان اروپا [1 بار]
🏆
جام باشگاه‌های جهان [1 بار]
🏆
جام حذفی انگلیس [2 بار]
🎖
کارابائو کاپ [1 بار]
🏆
سوپر کاپ اروپا [1 بار]
🏆
جام حذفی آلمان [1 بار]
🎖
جام خیریه [1 بار]
🏆
لیگ اتریش [1 بار]
🏆
جام اتریش [1 بار]
🏆
جام اطلس [1 بار]
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/101403" target="_blank">📅 02:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101402">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzeXIoV6UxCPplFkxZ1hde8Zsh-2ka7TfHTBYjb8LZVYtX0ShV86n5c7bL55yAdNHCKSlbgEJAlGATrLeoQdkMaU1qNwXLrekbXMaqD6Cd1Rb8r0u8Zh70z_4_KdvIkeJflNBfT_UM3tMMdo4fmFxmVsiKEQhglCq3gOASNHC4qYe7jAucnK3yF_INvBOxSPDPJWQztmI-vxJYRM004kbvJp65IsAtni-S811Kvd881pPFrwBbsnHI5jrErMAiGqeMso_W95l1bjJwA6EKr4er5tn4j1uYWtvPEcsaNq1Mv3Dy4OfirFpHnh6KWsd8zIp7Eh0Dlr1a2sbXZV9CvlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
‼️
گلوبو برزیل: ترکیب بدترین بازیکنای مطرح جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/101402" target="_blank">📅 02:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101401">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🎙
عادل فردوسی‌پور:
افتخار می‌کنم دایی و باقری با یک تماس آمدند؛ یک ریال به هیچ میهمانی پول ندادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/101401" target="_blank">📅 02:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101400">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzoJINYBMS4dm5CKx9MnrnR8BPL7sfVjIkjm63_gWapR4nIFBKLNFgd4pbhIY0lHEboRHmTEszj5DG1vn92IO3ilozJ87lzWrcP7QsJlE0gnneWszEqX0q1Ozm6ECLiAR6eOzlFyKY_UwGVWcIwn9KALnPxb8H7n7u2colGvFqfjEhMm_j6COlqFowCecd5KzG3k2ZGHz3O4rNYH0rMsyaZ_afB-aTSRmzGmXIvn9S_FEprsiPhvWFzwn-wFR6wjf7u6OwwEwM3ZfHjiYRxTGVvsN3hA3E3ULm9lKbkpVnxtNhhb6As0_Y7ThHjCrdtDByHySjV8VLy6tkY_E3pVrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
اسطوره وینیسیوس بعد عمل زیبایی در برزیل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/101400" target="_blank">📅 01:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101399">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/101399" target="_blank">📅 01:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101398">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qB63G7uwgaIwLENKyzAs0RxNEbww2GgeFci45S7OYN3mwM4_P1CJoIJ1nIsgM2EmisXi4iS7r2v1k0ecG61i9lIkmD6em09kwaObLDO5z-UcDsKmK-6CH0_-HEVQlAYnCDSHc-TnWrNlKBCykHRFRLvFqnC71KHLEQ4ewLT3UzrnQqGlZGUfjNVtCVBfxX3NqnV7y7qb4mY_ozzx2gh7c7nD--qccXYPdrS1FsJSNqIDfec2eNfWZUVA1dXkoRxa6HnFT5Qlczd9ZOzlafjVOQkrNqzcP5AHuqwUGzM-7pk8L9yj2N7fkOOJ2SjjBV2yA_L1bOqtpKb6OdVxffg4kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/101398" target="_blank">📅 01:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101397">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e202619a75.mp4?token=ESnzJg99IThEJ3xn_lisVFnyi8cMRj8ca93cPYWaMewnGk-v_1naB7qgb56NKvcPiI6a4G2BDHstDlUKzz-d_Vt-9e_6rGoZGgHEtQr8fIF9jV37l-ijnJ4JyndXqolotwqskNFEUCB2nl5YkS3UUt30mdgWhIGUoH9zNzxxM7yCzZ808hli5zrtWol7eYrgd0mrrRpoIn4-PfEG1wltSTu5z17tv0sb5Usk3ClxuB9i-1mTNG7iD9b2pZNY7ACQelyJV5ivfDZ6n76gULN_gm-hu8MnMOlZx2D0mg6DpKGMqD9G5XpIfhidip2cwj2P6grPWyRZy91K-bJ0PV_jOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e202619a75.mp4?token=ESnzJg99IThEJ3xn_lisVFnyi8cMRj8ca93cPYWaMewnGk-v_1naB7qgb56NKvcPiI6a4G2BDHstDlUKzz-d_Vt-9e_6rGoZGgHEtQr8fIF9jV37l-ijnJ4JyndXqolotwqskNFEUCB2nl5YkS3UUt30mdgWhIGUoH9zNzxxM7yCzZ808hli5zrtWol7eYrgd0mrrRpoIn4-PfEG1wltSTu5z17tv0sb5Usk3ClxuB9i-1mTNG7iD9b2pZNY7ACQelyJV5ivfDZ6n76gULN_gm-hu8MnMOlZx2D0mg6DpKGMqD9G5XpIfhidip2cwj2P6grPWyRZy91K-bJ0PV_jOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
عادل فردوسی‌پور در ادامه: من بله قربان گو نبودم، نخواهم بود و نخواهم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/101397" target="_blank">📅 01:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101396">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piLJNNk7Zbu9fZg8OQj5X9_c8DuXIjBMx8SMWhZ_Xs7IuzjJ9U-F3XpS2ax-AVFPklcrsukDp4W9uC1OZVi0rFx810TA5nM-88U2jjA25_mjruCfXfg1keXrY_7OvSsBJREnRyciRh6idZNjHbDLeseKyP5BzZPLbzdeMzwuDw4kLBDarF8GC941hKoq1TOQ9AvvH86xcZGCy4DjiU_R-59RJyN00ztopddEeuE9KfdAF6euXT1O4TSIOXdAuB0QPylDxMfCPjmstMFlw26IOHMH8WqsXtnddwglqqa-Afo4jqPZlRLWEUVJiNMVVGa6W0frOdXL6NczjcFov71RfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر قهرمانی اسپانیا
🇪🇸
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101396" target="_blank">📅 01:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101395">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135a7fe008.mp4?token=k134COIgGO5zKkB5W9VmCZgpVA-i__PmKqsJcopaPMD724Ocf7o2SjGdpWn75_X8kJFlDGVqkeEZIkmqbimKGhrik_Mt4_tsNP-ayB9xmxv4gKnQCR1D-ja7uV63pqZLI2EIR8GrKM7au9nrBF19cd-R-c3RS6SEozaRk4SVaHGPnUcUYn0Sbpj-TQxDhF9THNm2nFmKomlZFc4YRs6sDC1fE0pSoPpeWtliotc1CGfP9OZYKpiqDtYjWK_tqh8gGvAdNZ145NlnNvLsY9YUqwE6CFwfk8cMpjov9DJHxot2-tA8GTrIHQHAv-gzsbVlBwK4DhyFVaXz8OIZ5rY3og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135a7fe008.mp4?token=k134COIgGO5zKkB5W9VmCZgpVA-i__PmKqsJcopaPMD724Ocf7o2SjGdpWn75_X8kJFlDGVqkeEZIkmqbimKGhrik_Mt4_tsNP-ayB9xmxv4gKnQCR1D-ja7uV63pqZLI2EIR8GrKM7au9nrBF19cd-R-c3RS6SEozaRk4SVaHGPnUcUYn0Sbpj-TQxDhF9THNm2nFmKomlZFc4YRs6sDC1fE0pSoPpeWtliotc1CGfP9OZYKpiqDtYjWK_tqh8gGvAdNZ145NlnNvLsY9YUqwE6CFwfk8cMpjov9DJHxot2-tA8GTrIHQHAv-gzsbVlBwK4DhyFVaXz8OIZ5rY3og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لطفا هوش مصنوعی رو متوقف کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/101395" target="_blank">📅 01:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101394">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
👍
بغض عادل از صحبت‌های حاج‌رضایی: جایگاه اجتماعی با پول خریدنی نیست. در آخر، تن شریف باقی می‌ماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/101394" target="_blank">📅 01:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101393">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_yGSMGE3yDwYxQXCiTmPTVFSWUnsyucEy342YJONZvM0bziSBAscGd1Y_pBSornjiCGAa3olgBLWi_0psoxZa_kiodYSsBrknPtuays_R4JvuW_goUeOw0TSD0w4TrwBZgJk1zrG6FQ3Pezpm1C96E8fOrNo_uVV2vjlN8Jm0H4k2CN2LRwk5SxnxOe3O0wGsrwND4ZejVr4QdKk6u6ZikTDiG7EV-wz8F3M502dBpBhih7yfUkN5kPrDTeWEuHhhmgfNstuDLobJ2X6ChjQPK9vPbq5FnF8GkiHJK78APJmDbCpk2czKFhce0rmsA_kssY615FCyOoDjWbtoTwNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
توضیحات عادل فردوسی‌پور در لایوش در ارتباط با فیلتر شدن 360: بدترین راه رو برای ساکت‌ کردن گروه من انتخاب کردید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/101393" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101392">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQ4Uw6cKs7zoqB7R-s12UzxUNeHFUbWDBfpUqwmE7UonsgrD3uRx6i7HuYC-croQneOAVGQXysWKIA0jNZ1L5_4hw0Qijy9QF8VPbE6yjYfSuY7y3QIUeD0Y5XmPB2dtPFt3TBqbsUAqur28mRbjJT3zbnBY1WfUoF8_t6z8rcqTOZjLEoEJTfnKf71y96pXzz8abGjqohsBvPLVXB-urmHRgsQCYVNiFpd8acDd-o2fZu9apZjfhwBm4CclcM-4QnMQG1-bRrof8cP0SXBnZ6OpzYN_MsLvHJKii_ttZ_bsEPb1NbtjvXKxHFHLZnhlu22x8NT4UK2vjbHSzq_q4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
دی مارتزیو: لوکا مودریچ و میلان در مراحل پایانی تمدید قرارداد هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/101392" target="_blank">📅 01:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101391">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gen3bXcTbluuLUVuVIR0CguPv3Cj5XQlLCE0MuoR5zO7R5HK_fHlhinle7gj-QCzkzNmSuvBSnRzzo9RA5Uj5Oy-D9eY4NvJ8aKC3QQoC1Fm_FIACQd4_3ptnYMI7p-KrWEfW4IFozLwuIU8W73DzfnHQB-_cr9TfKhiVN5sayqTkvjCSUuQmG-4yTDfgruWkoVph66PtdqldalcpuNivuHL__VMqDPWpElL7fgAo27x04dxLQYyZKRTN2WiPN3LlgR8HzRMrWrY5oq8cXugfWWzJFdij-76UQI-LaUIVbtVBLj_zyf7CFYSiqV9_AgQTqYj3FACxvWW15dMup5PYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
کیت جدید اسپانیا با دو ستاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/101391" target="_blank">📅 01:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101390">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d1fa4b0ee.mp4?token=njJEW6_s1cZDYgRFca1QPZj85ZwJcEbvCGR-bMn41R2DDT123L6clH3OxXuypPsGZxnYgxu5TnaFWKblBbU-embztgtniwEHqSFyNZporGB8-7p5HA6nFLRFbz32EHRXQZmwRaY8qamHIablMkrRpN_rb170Lv4Xf-pocUUFRpdWENPjHLgE6Hyjcy9TRHUztuTOhxRJcQvb7a9tPgLEtM8ruRQBiCXkJ35G0l_ayFjkoXFZl_HnjCVOawnhCgsOPxGmYcYyqz3gLM76Dx8YoYBTcOxqvq3iyJQiBYPFgtnhonr1XzOfxN42g4s4K2OFKxSrdnBb8znGR9ZJ0_Wc6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d1fa4b0ee.mp4?token=njJEW6_s1cZDYgRFca1QPZj85ZwJcEbvCGR-bMn41R2DDT123L6clH3OxXuypPsGZxnYgxu5TnaFWKblBbU-embztgtniwEHqSFyNZporGB8-7p5HA6nFLRFbz32EHRXQZmwRaY8qamHIablMkrRpN_rb170Lv4Xf-pocUUFRpdWENPjHLgE6Hyjcy9TRHUztuTOhxRJcQvb7a9tPgLEtM8ruRQBiCXkJ35G0l_ayFjkoXFZl_HnjCVOawnhCgsOPxGmYcYyqz3gLM76Dx8YoYBTcOxqvq3iyJQiBYPFgtnhonr1XzOfxN42g4s4K2OFKxSrdnBb8znGR9ZJ0_Wc6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوکوریا با صدای معروفش در جشن قهرمانی
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/101390" target="_blank">📅 01:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101389">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
شنیده شدن صدای انفجار در شیراز و اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/101389" target="_blank">📅 00:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101388">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گزارشات از حملات ارتش آمریکا به بندرعباس، قشم، سیریک و چابهار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/101388" target="_blank">📅 00:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101387">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7IQTrKTjkF0JVSGs1PIr1fEOSvaqwO8H6yF8jWbdt72fTBX967FeEKzzIMHK1zmVFJE1J2e5ynlKkEc9UIpAe5IKPQ8SYZbtGFbKhKCoXdngr5mbNya4l-3UBpZYXdNY_sQ8L1jzmIcm8L1SglpnzHcI5NNdGwvXKf5Spt-FG8I4N3YR0esc7pPLPymvvJ0wfkt76M_2jiQsoh5M-Egie0Ysbnf84hN0RZIEialFmAj2IpVWbxoN5e-5VCRRcgRBw4ViG2QZvYm_VKnCWcjqJCBZphNI8a7eSaF9zbe_F6Z9u7S_ACys_tVGWG9CoqYNxjjoZP9_8Q4Ep57VMG1jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تی‌ان‌تی اسپورت: فینالیسیما بین اسپانیا و آرژانتین در ماه نوامبر برگزار خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/101387" target="_blank">📅 00:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101386">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rr5JdO_Ax3qMF-XBQqtT-ViCprHSS5hCsXzhmJ-ls5aF1co5ug31G_wSUhUxhrFby67TlKuIpu_4tKZ3p-pDdUtqTBgDcu3EQsfUEF_BBEo0OMTTyROyTHpGOP2AeTUwQ7UQfbTJt_tIsYSGfzAtwTnsQTp54KtO8f4xexy8mC89duCUwnCxmxgHdKNIlJA70mWPIIoxjq-g3UtrIe5yS-ZlKZwqNdeAJy8m8EYOhF_HvOqku7v5ivJHGK_Q8sEtQ7Rqh-PhGLTQMHuHuSaJf6xpjM2ipLekQPfumbjgZu3JV4b7DoCkjzxcAwYL1vsVmXk_ywDPJMSv8fyS5fq92Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
#فکت
؛ پشماتون از معجزه خط دفاعی اسپانیا بریزه که اونای سیمون در کل جام‌جهانی 10 تا سیو داشته و کلا هم یه گل خورده درحالیکه مارتینز فقط در فینال مقابل اسپانیا 11 تا سیو داشته
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/101386" target="_blank">📅 00:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101385">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nrq8i3UpOD4hbP0PwWEVdHFGLOsS8pzw6hD1-6nJOsac3eTXwBF3ob0vw-pn-Zu9fuK5fIXuGCPA_pSZGhOwpuHljbXs6sL6Li_gI8291YgTdr-TSEVQSJ3LFUX7yKQADJ0JxbZWV8UbevpIzkz7BaFCBpf6OjxHW5pfmuk8IaKALbvs6CM-KoExpzwjG5seyxLTh2GqGP2q5EUX9Uhfj3yMLVwkPxLwMSeRIXFKlp0oqo3bJSWg9Ohls19Lxep2-X69vbCWzgOU4iH86p9VrCSqiQfHOOazRSTT3PrLv8UaLbL_wM3DKLorWfocEsGhCFFZ_gkc60K1djdlB5xa0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوکوریا تو جشن قهرمانی اسپانیا
😂
😂
😂
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/101385" target="_blank">📅 00:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101384">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H6l4KmywUHbXc1ZZAMwRHAtNjjewbx000KOgadsblSxXYLIcuKMg-A1B3z2K3qMLLBnviLOGy0JfSbEy-BtrxUgx_bUrZ_YNj531sAGzjK-_6GgpDrEkoHljw2_k0jO_sLB4207GzqHCAZsV1ehBWby310xj_UTwzN5NChsGf2GZ_YRYph1bx91078t5go1DxouR4-Hzd8gi0ogOh-3EQwIlSA0y2BQCqVuzD3m40FbgdSbFJhqJGpIAREfXg-FdQ7lnVWneypkooH8Q5_pzwQEtYzoEOqVFnKYd2aaN8VoZUUf3DO8x1KQ4GR_jEhk3yMMzyEXz0bHA-w6y-lIsbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو شکیرا با کیت اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/101384" target="_blank">📅 00:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101383">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2968949297.mp4?token=bZirzDcv7uGSczfx-5Q_dw3ci11_y76_ZcwZSB8EReGH_w6eXoCPVmqeLXnyzfxJcfAmJO8cduy_i07lU3NdqYm1MjQwvwrxAhUK40CStUQtXOqXPYKuYgpz0oUfHEln_ZCzYZ07xC3mU4QryB7YfGKqpE7tkjSmLDofJRqoQtjrTBPbVOCJ_9wKfYOwQeLKLOe6dbxXKA4Vk9dsk9HtytY7MA7zg6oilGBg7scW6ASwa_kXqt3_75vM_Eemnr3dtxvhqW04dCAODf5nvvr3CzNaAn3jFopbYRHtJYuBDOI2qY88I3-AjONXsiAD2lB_CRKR98CqM0fo81dg3SNBlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2968949297.mp4?token=bZirzDcv7uGSczfx-5Q_dw3ci11_y76_ZcwZSB8EReGH_w6eXoCPVmqeLXnyzfxJcfAmJO8cduy_i07lU3NdqYm1MjQwvwrxAhUK40CStUQtXOqXPYKuYgpz0oUfHEln_ZCzYZ07xC3mU4QryB7YfGKqpE7tkjSmLDofJRqoQtjrTBPbVOCJ_9wKfYOwQeLKLOe6dbxXKA4Vk9dsk9HtytY7MA7zg6oilGBg7scW6ASwa_kXqt3_75vM_Eemnr3dtxvhqW04dCAODf5nvvr3CzNaAn3jFopbYRHtJYuBDOI2qY88I3-AjONXsiAD2lB_CRKR98CqM0fo81dg3SNBlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
توضیحات عادل فردوسی‌پور در لایوش در ارتباط با فیلتر شدن 360: بدترین راه رو برای ساکت‌ کردن گروه من انتخاب کردید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/101383" target="_blank">📅 00:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101382">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0990cab9b2.mp4?token=eusWOCBBqCFw_yvngF-mBlTRrVK3Dji6A10fJf8tbtr5Mt28fcHDfkDaDdl_ZYHB_ADr1xWR8B5AX4ahjHqUzJf8VxIGEz--iyA7gSj1r90MwE4AUwln_TM9jfZdlnWHUfAVq4LiLJk5ljOWDw28hJNd3LKRobg7GyzKnawZW2ry9cv0wn7iMoPF7WuGHAkdPF3GeVk6xohphhoc8Q7g_RL1wIOTu3_JBTbP5NHCThvuDagT_1BkE7RnmX5-yONXMgGWVguQcuS81xRKbvfzQisX9wG0cBNxmjft3PfMahpstwny4lcT1u_Zng2QIckV9W_R0cVFqSRyYuyn8p3U0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0990cab9b2.mp4?token=eusWOCBBqCFw_yvngF-mBlTRrVK3Dji6A10fJf8tbtr5Mt28fcHDfkDaDdl_ZYHB_ADr1xWR8B5AX4ahjHqUzJf8VxIGEz--iyA7gSj1r90MwE4AUwln_TM9jfZdlnWHUfAVq4LiLJk5ljOWDw28hJNd3LKRobg7GyzKnawZW2ry9cv0wn7iMoPF7WuGHAkdPF3GeVk6xohphhoc8Q7g_RL1wIOTu3_JBTbP5NHCThvuDagT_1BkE7RnmX5-yONXMgGWVguQcuS81xRKbvfzQisX9wG0cBNxmjft3PfMahpstwny4lcT1u_Zng2QIckV9W_R0cVFqSRyYuyn8p3U0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال با آهنگ معروفش رفت بالای استیج
🇪🇸
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/101382" target="_blank">📅 00:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101381">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گزارشات از حملات ارتش آمریکا به بندرعباس، قشم، سیریک و چابهار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/101381" target="_blank">📅 00:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101380">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fdecc8438.mp4?token=lCRmxPv9L9Jk-oPx6YbXZavKAaJGT4qX8GfMp5mtv_U4AEJGNCVkcMoiN41frOBjNPKbhJefTCZjjFMV7Prg3fA77NdgpsDwO8pst7W9jw32WSYwy9iiwx2-FEB_JAFdDW6MUc8cdklrk0TdEQnJMyUIwr5pULFCQU1wsuvziFuE_-HWTlhAfU4y0v8cgHIXY4TKCgJGlR6CRVBeEvhMwHjRDXvcjmU4vRpBwHYJOFTvqGRKvsHJO2ska7r69g-QxTsT080MLuGDyFbd2lhNez-ekOTkns0g3y9mnoWRSTiqyN8TDmD_GL0w0rY8ZR7pTCKlH35G8NO7WP5z-8_Jkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fdecc8438.mp4?token=lCRmxPv9L9Jk-oPx6YbXZavKAaJGT4qX8GfMp5mtv_U4AEJGNCVkcMoiN41frOBjNPKbhJefTCZjjFMV7Prg3fA77NdgpsDwO8pst7W9jw32WSYwy9iiwx2-FEB_JAFdDW6MUc8cdklrk0TdEQnJMyUIwr5pULFCQU1wsuvziFuE_-HWTlhAfU4y0v8cgHIXY4TKCgJGlR6CRVBeEvhMwHjRDXvcjmU4vRpBwHYJOFTvqGRKvsHJO2ska7r69g-QxTsT080MLuGDyFbd2lhNez-ekOTkns0g3y9mnoWRSTiqyN8TDmD_GL0w0rY8ZR7pTCKlH35G8NO7WP5z-8_Jkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
قلعه نویی: آمده ام بگویم شرمنده مردم ایران هستم می توانستیم مردم را بیشتر خوشحال کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/101380" target="_blank">📅 00:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101379">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpD9DB4_v0MEWLjZbLwYG9K0F0sOZeLSVsVdrmi39BrG7pQ3XxAhl4hfG-MTAXa9IVg7uWHVyLZ4XWQdjnX2D2-gqf4gkWg_-6T37QrHdHMvIPVPNM1mxVHn3njSwdulm2e3k5oLc8ZXa21lnEkfWiPEhVZB7B4kI2jxPhXktqWBqmMEgCOPvsEGyFaR0iloFvTUY9uhOJvDnG2m5RInrMPDER3QP939RcrQa8D3G9ZkXgHNYI8aO9wzlSjF9ns_ukQ-T1KB_mESjO909k5DZ59Verj0bLG6hbrrec8A14otlhn33yWDn22Hu3F09NcDmGEofcE3EqFTDJv3RfLq2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به گفته آاس نزدیک به 1.8 میلیون نفر در جشن قهرمانی اسپانیا حاضر بودن
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/101379" target="_blank">📅 23:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101378">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1bf2a3334.mp4?token=jhYEpfe0Ga21cvc1qsUi1SWnshsGb7r90oslIbxffIfhxQpYfp5BDOGfRyjyRyWTsC3suDViNxgQa_dVS2944qDVv_6Eo_QxX0LKJdlXsIHER1eQLZof9T-t529i4H0eC6q87IMCZuRTf40cVaJShL883mQqaPzcaP8TXsKGMwXZsO-yuWfnVOORU2HvPRt2QWTI6MQLRFm9oZrFiDE1D6vy0jpkBIH8zO56oGH3IRP7YzxgMbvjLVlOG36NmkdXY2eMofUsBmKdwFaOWSLE0z7_6Tjj6fDgjBm-cm2qptsKPHDiaCPwI4m6zCdXnQqFWuvXzBJvJUOaBqW3FlbL6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1bf2a3334.mp4?token=jhYEpfe0Ga21cvc1qsUi1SWnshsGb7r90oslIbxffIfhxQpYfp5BDOGfRyjyRyWTsC3suDViNxgQa_dVS2944qDVv_6Eo_QxX0LKJdlXsIHER1eQLZof9T-t529i4H0eC6q87IMCZuRTf40cVaJShL883mQqaPzcaP8TXsKGMwXZsO-yuWfnVOORU2HvPRt2QWTI6MQLRFm9oZrFiDE1D6vy0jpkBIH8zO56oGH3IRP7YzxgMbvjLVlOG36NmkdXY2eMofUsBmKdwFaOWSLE0z7_6Tjj6fDgjBm-cm2qptsKPHDiaCPwI4m6zCdXnQqFWuvXzBJvJUOaBqW3FlbL6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قلعه نویی: در همه جای دنیا انتقاد از سرمربی تیم ملی وجود دارد اما آنجا حسادت و عقده گشایی ندارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/101378" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101377">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q038_OYTrk8Bma67PG75ILwyfQEz0-nmEDhpBWQhmDvJzJN90A9YSgdlbKJ1W5EVGQhbbM1F54Ngxh6JCbBTNkrpiH1qwVAtyoi26OJMvaVlzhzTwm6wDGc6bVZrD9mCxUFrS4PkwoUQXxPoC5LhL0CPfEJiDgeZclCDkWc_tsdNuAieLRJtH5Bb7OkjsbEJq2C0Awif-H_Rojsujcw9LUZdoNoN9V_BGfBaFhOn2d7465JS9sbyFFxklzwoA0xYO19A3JdweVV3UNYSdF55k5tBkEoZkwRuBF1FQixdJuTPRjsTot7K8RFpG8T3UP9tWukLueDUxJp_6sv9UY4dIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان دوران به صورت قرضی از النصر راهی بنفیکا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/101377" target="_blank">📅 23:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101373">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BHYBjH-cUMzLQtg_n6y3jxuNP62CrqjRYSXb3kzaQjK6WDGMYSyM6mxFqA3aihMV8PJsdo0F2kZqqpzd5ueqv6h8Y4lKSQGggSO7oUQobCZ058m-vEi9xIp4j0L62tWqPoFp_TWTaRhd1KkcXCL5VjalGOOdlxu2c-1lgsuyB8Hym-xYUJ9yMCiy4-mjeaHEFlHylUo6adF-K0BTmmc1W8_7gaxvmrkjXef6AX0kVvtEhebqE-7gBlc0lg7helWm37dYqShMcTJ_rbceO6utRdDG7ZJkYHV133LE2Hmw33smccsuN3bRNlK0queJt2aD2PpsUOax9DDu-EzGvihftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNL9PVZ81WihKbtOxMyhF7XCAVjdjtV1zqzQV5Z2kYlhTuGuO2QaKS2YSF97aV-pfy_usVAFyow-R9_mZkyfaLd0uy-GVm3OxhicdHZAws5j8WRYxUruTbuaZrNurd_h4Qj7BeTqyBPAr7TXiosL2KGZT1yXL0GUnIEnhN4_BKO20kX9nei0IfhWFpOGJsUru9wiUpPI_DRrTR383qVR3z7KDOuR90fkaPUG2KB5iXgVxWgku-aPy7cOuYcTLxFVtYQLSoEytAXtTL_GAfR3Fd8L7CWzdbJoypXRRuZffncJKyTSf4KaNA_0mJXbvH9kw_tfs4YscMIy2CCG0vm51g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tr18BhD2gV1ZiUnLnhipkZYtBQ0LLzdqPTgvD9UcL1YLmujKwV9dmlAN9EQ8Pt_As4aIKbgfsQfNdfozT1H5MTJsii4OIb3flgSc7bEMS9on9x1iePZQbixQF8vm1l81mTplpwfX9mlkGWgnul1pactUGtoyKHPFkF7LHyUlwqHP7fFc95AdB6Fl6-P3V1dHdsuQ4f5zIRsm_poGkvZuChHCYBvQlc5wPmAClwzONgf2KkSHzUoFrkEVnvMioj44IPjmPLcOSIvVBywycW0IsEoox8IfUwLzDZlfKLSIaSVKXZPVMxWidK_4KjO0VqGThm-iXLPYr14ZPFTRYlAHGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/koYVukIAYKbyxr5r17UdoVV_B9IU5TqE17rcfcGlwu7PnEmyiqpG9zDu5ZcJvozyVKzG99yOxWCfwDdm3H5LfErkKjb9kMsm-9KS0SaKg6tC-zm8X4bz-qn0BPEZ_xBqajuOBRs4TtQGbFpTHEvu_SoKTtEEf685ug1HKFKl603BgWlVV7TZDMzaUJcZB2hlolTILN5Bev5cx4XfDtJqMdMqcUnS_FKQxeaQHlgOfksic6_xsoLqYhyAmqS8Y7GoCsvLefWQDOvcMycm7eUfWW-f-PwMKYSIsziXCu2NNJkO7-bsqmPXs7LYgZktXWYmzOGN-9ZRaTBxwRCt3SChCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
| اولین تمرین منچستر سیتی تحت هدایت انزو مارسکای ایتالیایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/101373" target="_blank">📅 23:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101372">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kpcc9Se2k0RAWtPaLvE-4ZfckN3DW0ZsDLXO0UUEVyHGfh2KGMdXhsXJO1kXEBaKoFKh2wklpoAUpEqSBWQ3YFRfmmf9YFts8iTz1qK9wdsY1dRIFeiCzpY1flk_bw5GWZ-jjjOxo3LoGB7rymkQZ4XwXhy6-du5UwH8a1wY68rgWrwnze_dyvcz3QTce9OKMqUC-u8BPTzsP6hNq4YSXJdkQKKLEHANmGcpqbwHE8_6JYGw8BMNqDTaXaqydxLiiCDNW536ys8mkRz84KA-cLsqlQZ6dy-S7Gi8VnvVTs2ZTvrDAqFt3dORHMhWst5JUOJ2js2GkdNBh6fNa4tnDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔵
فوریییی از فابریزیو رومانو:  رودری آرزو داره که پیراهن رئال مادرید رو بپوشه اما پریز مانع این انتقال شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/101372" target="_blank">📅 23:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101371">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9632195436.mp4?token=d2Rmrp8XwU2rIgiO6-5_yc9Xd_VAZJirarnYuHci1_x-Lgu0HWgUNzeNRRcSBVYbnhCAmwBvewz38spmwd74b07qxJmGmlwbN1X9mxozN1zbhxMMye-sUZxc8JGl4cxDjt_PvQpMeq5jH9lfiklhel9GmovAg00gr10Q5e-97RP7SIcr9ARh67jPf0J-HZRgn4bkAH0k3oD6kecVBlq1tuvzkLHHCo4yEF53M8OqJN_mD0qzgWUy7n4UaMqiH7byisSAwyUNCdxJmHdQiPCdddl3Gh2R02sxikmnQI3ELOcornXOhUDkFpZ4nL5uEcQ8Shy0w80ab2mXyF0urPIU0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9632195436.mp4?token=d2Rmrp8XwU2rIgiO6-5_yc9Xd_VAZJirarnYuHci1_x-Lgu0HWgUNzeNRRcSBVYbnhCAmwBvewz38spmwd74b07qxJmGmlwbN1X9mxozN1zbhxMMye-sUZxc8JGl4cxDjt_PvQpMeq5jH9lfiklhel9GmovAg00gr10Q5e-97RP7SIcr9ARh67jPf0J-HZRgn4bkAH0k3oD6kecVBlq1tuvzkLHHCo4yEF53M8OqJN_mD0qzgWUy7n4UaMqiH7byisSAwyUNCdxJmHdQiPCdddl3Gh2R02sxikmnQI3ELOcornXOhUDkFpZ4nL5uEcQ8Shy0w80ab2mXyF0urPIU0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
تاجگذاری لامین‌یامال در شهر مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/101371" target="_blank">📅 22:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101370">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tb9jGJ6U82bEsD3KUNt6b5xQYkdrbhKFIx9DQNPqqFiwW3GFngxQk6VuEkcBYpEzItlonzL4eBv2GT64k_jaWM9Lp_0jJjKWmfVSImyCzisrMr0qCbUZJIKTx4kYfgf6MDecyyjMnrJuMUJ28pQ0e0B9gpAlfBoLIgTGWJwGqbPiJ-mECKmECoE5tcDmtBMeVZPirRh4_kH27HF3r8ZJ3Q0l7hpKq64Jt9JpdyuGv5LHKlG5a_VigSUltqh83-6lZVDhTJ_6m8WM1a80uQ6khFkNh17vauE2w0_sNCWwnNeWJC3j_Cg5Evdag8C2SXcu6ZzmEnLDFmRTkm0z4gwAJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال این بنرو از یه هوادار تو جشن قهرمانی امروز اسپانیا گرفته که روش نوشته شده:«هفتمین دورهٔ مسابقات ولادا دل آنیو (یه تورنومنت بوکس بین آدمای معروف)، بین پاردس و گاوی.»
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/101370" target="_blank">📅 22:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101369">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇹
🔴
فابریزیو رومانو:
🔻
منچستر یونایتد این تابستان به مارکوس رشفورد فرصت جدیدی خواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/101369" target="_blank">📅 22:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101368">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDu66vhfogDxPVLiWx37lG-s2RhEHwxzPB2AIcz_VclpLKD7W-lyzGDwvfbNz7h7W9p-neVsPdx56a9C15jAAcOx9tTSy2a1iLXYx5KU8UD2ZT1ia1EiKfda9qSE7i9wlXhfGulGlQpMJjGSn-eDXHAHorbkJJr9AitmO3oJp7aG5ioBQLpCRGpcIl6WARIyQ3VTjpVDEtuITzprRHSj_Bf8TfDEmf3G-evny17Ob1i0teFds53xooyP640QJdRZs2AGzQtrviFj2_sJqT_8aWTJ-Lz4-C0FBFYMehu008OAijq7TrrLenMVOHLp7c6BTxLolhmLaSuXt-wRZpK5ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔵
فوریییی از فابریزیو رومانو:
رودری آرزو داره که پیراهن رئال مادرید رو بپوشه اما پریز مانع این انتقال شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/101368" target="_blank">📅 22:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101367">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5ybHhcsvRDW_5CBxV6TDpGdw8Mp2zAt8fvu-MVQfv2w4VZKpBqUtrA_VIm0-npYpOSbc9rMeIsQGM_ynCrAyRC-R1Pys1_bPwMOVTZZFFrNrDoBQ11rj8s7SWSec94DGrve3HR6cM8EPP8L_vmdizfLaDIaZmA3kGPztt8kNhgiIo0CBHMAz6eG0aJXLWOHIJ6os28wwZeqfHaO1E9Qqmn_ORiMgHN1X5Gz3JhdLQV9Ce3L-JQxWsE8-4K8kQGZbd0f1YjlGXm0CJ0Ks3x4nUB2UMtnVGRn6YF9D1gaOD2bbIYjD021nUapBr6U_j2QfJjRaecadRWV6C00cV8PBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دزدی قهرمانانه لامین‌یامال از اسطوره مسی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/101367" target="_blank">📅 22:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101366">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e69c82de10.mp4?token=bic7bgUoHREkG-suUVZG6OdvlDcaTtt7Za7SzzxWZTNoT8x4-_cykzU3ttD2_N5-tf5MuLvyVctC_0AvJoEnYXyqJ_j0akEPeNLrsUvbNGXho7C_XQXvjYonEu10WY-InIOldnugYAYvMfDDwh9HLFnhUS39smhxfDl7GyGPEWac6b1ieE6sT7tyQkx6ZIQGvb8PJrx-TWomyVIBxXJlupZUUvrCv_bDs8DU8kQyenegI1ON-KzI6Hsi9O5KctZrn6JqayYZXRzh9ol6kpI4xbKC-iskNxWum6mGGNIx9Q7j6XdKwMStDJGF9Q8c9nnWd9BaOxkYTl8AKEho-QsnZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e69c82de10.mp4?token=bic7bgUoHREkG-suUVZG6OdvlDcaTtt7Za7SzzxWZTNoT8x4-_cykzU3ttD2_N5-tf5MuLvyVctC_0AvJoEnYXyqJ_j0akEPeNLrsUvbNGXho7C_XQXvjYonEu10WY-InIOldnugYAYvMfDDwh9HLFnhUS39smhxfDl7GyGPEWac6b1ieE6sT7tyQkx6ZIQGvb8PJrx-TWomyVIBxXJlupZUUvrCv_bDs8DU8kQyenegI1ON-KzI6Hsi9O5KctZrn6JqayYZXRzh9ol6kpI4xbKC-iskNxWum6mGGNIx9Q7j6XdKwMStDJGF9Q8c9nnWd9BaOxkYTl8AKEho-QsnZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
کارلس پویول: "من فکر میکنم اگه این تیم ملی آرژانتین به فینال رسیده، همه‌ش به خاطر مسی بوده. به نظرم اونا به مسی تکیه کردن و اون بود که تیم رو تا فینال بالا آورد. من به احترامش کلاهم رو برمیدارم. همیشه و تا ابد از لئو مسی ممنونم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/101366" target="_blank">📅 21:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101365">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a26571e61.mp4?token=KDDOJhE2RXYsevbVcsKlyEqbKhhYAykCKkAQZ-xZ3QxZLBltnSWwQSzH1i0i8tIRcqNo6IiR_e01d1r9DYR6zhM35Utx_7a6uukOwHISnkOzKYz6HCsLYjaCee2ZEmcmsaPufLCMt5S9_wrO5GBoQgEcjhRHmCqdjKDL4qbY_D5_G3BvR6EiLLJMxsYLvURKU_gXv3r4FnnQTiykrhVcqNKYRKjODLJ2gb2oNXxsyyF_96NirqCU-jH72C7QjetCuf8D_f7-TUHJAS2xupAtaNRztauCTAMTOO35ygudQrT_4wobl6UHbylBg3qZqCHyA_0ABS56YjKK9iE6QBG6JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a26571e61.mp4?token=KDDOJhE2RXYsevbVcsKlyEqbKhhYAykCKkAQZ-xZ3QxZLBltnSWwQSzH1i0i8tIRcqNo6IiR_e01d1r9DYR6zhM35Utx_7a6uukOwHISnkOzKYz6HCsLYjaCee2ZEmcmsaPufLCMt5S9_wrO5GBoQgEcjhRHmCqdjKDL4qbY_D5_G3BvR6EiLLJMxsYLvURKU_gXv3r4FnnQTiykrhVcqNKYRKjODLJ2gb2oNXxsyyF_96NirqCU-jH72C7QjetCuf8D_f7-TUHJAS2xupAtaNRztauCTAMTOO35ygudQrT_4wobl6UHbylBg3qZqCHyA_0ABS56YjKK9iE6QBG6JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
🏆
پرنسس‌های اسپانیا بیشتر از اسطوره رونالدو دستشون به جام‌‌قهرمانی‌جهان خورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/101365" target="_blank">📅 21:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101364">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpuporIS0MFLB_7-Ndpe7mtY698GZ_hqvujsJKfyG253v8daGV1lG1a2pugms13RAxHo0kY6AzNgnQqPRBosKFDVMQI9f-7HiJzTWAT9I-4ebQWcyBjTkn8G8aC1J9iKJFPkoqi4nbUSArtcoLOQYQdjO4bFas2BGUKZR7X2A7GXZ35CBxdr93iEyUDGOUDzPYRCkk4oKkr75iBpai_xLZWQiSPxiMAOXPaZcPgot859vvarzm3xXd9EJv8kTT2pG3zkzO6V2AlL3bI-BMkxc0hvmbBTA7FT-Lx5wYNZAREB4GoqidD9Kzjo9XsJLp0vAYqrkqizC2v1B6GaAPERqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال 2010 خوان کاپدویلا دفاع چپ تیم ملی اسپانیا  قبل از بازی فینال سکه ای در چمن دفن کرد تا کمک کنه اسپانیا قهرمان  جام جهانی بشه.
🔻
شب گذشته به مارک کوکوریا گفت همون کار رو انجام بده چون هر دو دفاع چپن و کوکوریا هم این کار رو انجام داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101364" target="_blank">📅 21:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101363">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnTFWPMMD5cYvzye2l3O39VSfLEk_d_iJjZl8_GWrDQUuX9DQ1FoSZ4qq7X50j46BtSKIgQ5Wj8w--MbL6Gja_SUQeRN8polKNmh389gTip7gLQ-RVEbgmtbl4YgGHc5YKYhb54EKBYxnASrP14gi9qOWiyeqZaXF7oSYpJYLvdTmB5Qz4yD6Vt3cKYDIGal2we2mZR22U7PD_ckZTxeMCoxljiDCCGTRr9cx-wlc1k_3BdpODlb6d8DwW86EEOWfhid3xYo6kSFaEvPLcnfKYoIWQ8DlLkoL8Z-ZrRUJ3Axebh4vByLo1fuucJk4GXDvYWZcKd0maBsyI_q8cSLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📸
مسی، اسطوره فوتبال، از طریق صفحه اینستاگرام خود:
🔺
"درد بسیار زیاد است و التیام این زخم زمان می‌برد. اما من تمام چیزهای خوب را نیز به یاد خواهم داشت... مسابقاتی که نتیجه را تغییر دادیم و تمام تلاش خود را به کار گرفتیم، و این خاطرات برای همیشه در ذهن باقی خواهند ماند. با حمایت یک کشور کامل، و در کنار تلاش و زحمات این تیم، ما دوباره به یکی از بهترین‌های جهان تبدیل شدیم.
🔻
امروز، درک آنچه انجام دادیم دشوار است، اما این تیم به فینال دو دوره متوالی جام جهانی رسید.
🔻
از صمیم قلبم، از تمام پیام‌ها و تبریک‌های شما سپاسگزارم. ما بار دیگر به عنوان یک کشور متحد بودیم و در کنار هم، افتخار بزرگی را به خاطر اینکه آرژانتینی هستیم، به اشتراک گذاشتیم.
🔺
همچنین، به اسپانیا بابت قهرمانی تبریک می‌گویم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101363" target="_blank">📅 21:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101362">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
😔
لیونل‌مسی در بدو ورود به آرژانتین: درد بسیار زیاد روحی را تجربه میکنم. زمان بسیار زیادی باید بگذرد تا درد من التیام یابد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101362" target="_blank">📅 21:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101361">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqA3iDGDYvQbFLS7xvoAPntReAKEFCGCVVYjY3Q_SOnbRS_GdcdIIFeG9iGdtHjKVXoTGINEDjLjpNtFRJQE1yAuah9TF9f1Zzeht9QCHillw2OTEuqtFYLmpvFCLs_M5_-U-HC3FgKMt3vs5g5foBgD3uJEObCUC_bdMCjje-RQQROwqVcwffzv-nIR8ssm-ndP2lWQowCdk_rSBbprt8x-MwJllEWz4q69hLByBdlQLkHHA2awIM9tgubuAIhhqo_0JYrmCbyPsEQXA6PNtGyl0dakuXhoTgSAU8VGW0WxqUH8727bguAdq8u-eHUMjEZJWemmJv9PGNdZUPE7tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🇪🇸
انتظاری‌که مردم از بازیکنان اسپانیا بعد قولشون درباره قهرمانی دارن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101361" target="_blank">📅 21:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101360">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erWEaal7dLZ4wpBv_P1V-7yL3B9fEizht00EJmcN9Qf-6ebRUu6qeRzcGl3n4bh6fPBg5z3QgonftIZOeXvYROhDMJpuS6bY3gLcY4Tv3dj3LvqZYlKhgGterYN4OFvtpjYOBQXXPdiWdtdAzItW6y61XVoQPpeJD7QEjhsbUOTgmM8t94QxtRkLb5Hk3-TaE0hnLwr9qAPjzlwBNJ1KsZZwTyWU7N_jzAmw__mH0TxYIT8lt9dhFYsUY3Obpgwdn7BylhimMW8NRjj-caj-yN6ENjvn1Z2ldaQEfp_vfhGqUBSgsT3YXFexH7ZoRuJFVOzO0xEbHoMmnEeSBZln6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصاحبه قدیمی سرالکس فرگوسن: حمله خوب براتون پیروزی میاره، دفاع خوب براتون جام میاره!
🇪🇸
اسپانیا در جام جهانی:
🇨🇻
کیپ‌ورد - 0 گل خورده
🇸🇦
عربستان - 0 گل خورده
🇺🇾
اروگوئه - 0 گل خورده
🇦🇹
اتریش - 0 گل خورده
🇵🇹
پرتغال - 0 گل خورده
🇧🇪
بلژیک - 1 گل خورده
🇫🇷
فرانسه - 0 گل خورده
🇦🇷
آرژانتین - 0 گل خورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/101360" target="_blank">📅 21:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101359">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZy9_CW90W9Juie4sBfKEFGdjH-OAYZmF5l1-4n7PLNYOnNp3T65D8aN2Kb-u_YdPj1RoinsxsTdSz3Pqk1Choxk__gyspYDa1b7KrhgOrxaZN66ssdA3Bky7y2m3SRm37jUdDP3ZYpsuBi7cj6Fwcpr6rtRc_UGt2Mpf1dOK0y_hAFhjnvFXUB_LTlrLWAfwjQ3DPtpiTYH4hU5UpXnryYREV30AbZ-H2Qvqo1fsCwRs5d7kPVbq3ii2ytsG4cfVgAM0dtIJkiLQbtu1fJ-6MEuVBdk7V-jx7Orsop9nxj-YDfzSo1brnp_KVxllXXH-utmKAqvY3avncuZl0PPKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
‼️
کریستیانو رونالدو، یک ویدیو از یک شبکه اسپانیایی لایک کرده است که در آن درباره فیفا و آرژانتین صحبت می‌شود:
آرژانتین تیمی بود که باید حدود پنج مسابقه پیش از این از مسابقات حذف می‌شد، اگر کمک‌هایی که از فیفا دریافت کرد، نبود.
و فیفا یکی از فاسدترین سازمان‌ها در جهان است.
به همین دلیل، من اصلاً از آرژانتین نمی‌ترسم، بلکه از اینفانتینو (رئیس فیفا) بسیار می‌ترسم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101359" target="_blank">📅 20:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101358">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
نایا: احتمال دارد تا ساعات آینده ایران به کویت حمله زمینی کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101358" target="_blank">📅 20:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101357">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31a87807a.mp4?token=eO_IMTt7TJaYskD_m8o5Mupyr6kRGy_rEN1KoPcJXVmSOR5h7K_2vzcyid2de2p4fgFz-1JQtbaKg_1Rf_CNwBs89qrTz1kLImtA3UCG-_3w6p9TiMmJP7Luf356NW8aWjdTfbSvqgRSH7PK_M6k-wqWseSqh_ixRO_uoPyREqPhVKz_9Rjb4ARH5fvlG-_c4IjsmrNkrw8AaXbAIrcQi41ZKTPZXUFqunIG14ORVh3GxwktAUZ5-zzCdVPSwG4hqGameBLC1Sar31KjT06voLmlDXzbuEPNWn8BvYUqkjEjHsrbBQB6rBAofsucBB4VXrJGbfDZfiWhrtMP36KLuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31a87807a.mp4?token=eO_IMTt7TJaYskD_m8o5Mupyr6kRGy_rEN1KoPcJXVmSOR5h7K_2vzcyid2de2p4fgFz-1JQtbaKg_1Rf_CNwBs89qrTz1kLImtA3UCG-_3w6p9TiMmJP7Luf356NW8aWjdTfbSvqgRSH7PK_M6k-wqWseSqh_ixRO_uoPyREqPhVKz_9Rjb4ARH5fvlG-_c4IjsmrNkrw8AaXbAIrcQi41ZKTPZXUFqunIG14ORVh3GxwktAUZ5-zzCdVPSwG4hqGameBLC1Sar31KjT06voLmlDXzbuEPNWn8BvYUqkjEjHsrbBQB6rBAofsucBB4VXrJGbfDZfiWhrtMP36KLuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پایان دوران ستارگان دهه‌اخیر فوتبال جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101357" target="_blank">📅 20:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101356">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
نایا: احتمال دارد تا ساعات آینده ایران به کویت حمله زمینی کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/101356" target="_blank">📅 20:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101355">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgwqYn9GxntkU1Qts5-hQoKtxcwk2ynn09mdbmTY8na_VwN9fvhtxv2u8Rc4_3dUcfQ_BBgJvcbHPFVErtpT9WZl6vETqnnaqyBRcjnzZutT8HVEDXUI0lqq9Gq45nt5idGjteao9_RhgOjzni28MRYWJlh1w-x_ZEOhnS9oiKwfC6jKHEJNyIc7zRWSXbyDzqkrTtrc7YBHzOr-mnYopwlKWwC8KhAtzazO6wYtRAl24qLzqYPr4lkgCuk327z8dScZlVJdv_uKPPzs3OWil_Mm1y9vKmCdm5BAStLM8LuKZMKb6qGVlayIJaX2T-TU9GYTQmcnKtOF2QQnmRJwuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ: هر بار که ایران یک سرباز آمریکایی را به قتل برساند، بهای این قتل را چندین برابر پرداخت خواهد کرد!
این دستورالعمل به پیت هگست، وزیر جنگ، دنیل کین، رئیس ستاد مشترک نیروهای مسلح، و تمام فرماندهان ارشد نظامی ابلاغ شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/101355" target="_blank">📅 20:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101354">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896a99e3b8.mp4?token=QLFXpxcYRWZ40YH5qxpjB_v7Nab359f7eFXvFF8nK6swN20DVgO9EfyFU4pcaKAyGsOX9M3rZG2VZe7P0_LuDaoPZ5QEhgiHFsHKCgzPDijNOXMPoCktP7ZM21gtRClu6mIWh_V1GjKYurBZLyJrdLbQaomkezqvLszBq0Ec168bO3iFPCcw7PEOpIw5l85um96Gpb-MEAOiKc92KvWuGN-MlwjgofxuQouPhURI5W5L4SqJI3iX1sixMCDD91eSvvohUZ3QrMK_WzVKf2wLvz5ZHCGT9ZMTKN2_nvFW3QWbdxcHZFFfhAHjtft4ySZiUk1j3t0WuSuH7afId_EPjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896a99e3b8.mp4?token=QLFXpxcYRWZ40YH5qxpjB_v7Nab359f7eFXvFF8nK6swN20DVgO9EfyFU4pcaKAyGsOX9M3rZG2VZe7P0_LuDaoPZ5QEhgiHFsHKCgzPDijNOXMPoCktP7ZM21gtRClu6mIWh_V1GjKYurBZLyJrdLbQaomkezqvLszBq0Ec168bO3iFPCcw7PEOpIw5l85um96Gpb-MEAOiKc92KvWuGN-MlwjgofxuQouPhURI5W5L4SqJI3iX1sixMCDD91eSvvohUZ3QrMK_WzVKf2wLvz5ZHCGT9ZMTKN2_nvFW3QWbdxcHZFFfhAHjtft4ySZiUk1j3t0WuSuH7afId_EPjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
لب‌بازی امباپه و اکسپوزیتو در میامی حین فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/101354" target="_blank">📅 20:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101353">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6f0f5682.mp4?token=uHmOi-DDSJ-lTAksk5bsmdiXcZfAiEtLW6bIDv70kl6CFWrYBcwXAZnK1jrVsn7wMgTF8_hI5C0Sye3jTfEFUZuMwXrBqk2yQlELBM-0aNVRMgN94zUVXQsLX2R6j_4RQ85UphFMARtoWzDsf9qiVur3zPYkLNi13t9w5OMZ-AvccxqPt66fyz9TKCiONzxWlCzQcCHLV9iL9UEbRgKe-bChDtQC1nMfPi1WGxX0myibuC2R6BkMY2aXsZya7KsVYdtVFqU_pUDHPFhJgEo22Pgu45SH81_tzU3RbZW9myEROPofcV8qakYeIdJr0vzeG-9Pey505xJNNDj3SwaVLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6f0f5682.mp4?token=uHmOi-DDSJ-lTAksk5bsmdiXcZfAiEtLW6bIDv70kl6CFWrYBcwXAZnK1jrVsn7wMgTF8_hI5C0Sye3jTfEFUZuMwXrBqk2yQlELBM-0aNVRMgN94zUVXQsLX2R6j_4RQ85UphFMARtoWzDsf9qiVur3zPYkLNi13t9w5OMZ-AvccxqPt66fyz9TKCiONzxWlCzQcCHLV9iL9UEbRgKe-bChDtQC1nMfPi1WGxX0myibuC2R6BkMY2aXsZya7KsVYdtVFqU_pUDHPFhJgEo22Pgu45SH81_tzU3RbZW9myEROPofcV8qakYeIdJr0vzeG-9Pey505xJNNDj3SwaVLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😂
صداوسیما مثلا دیشب اومده با ریوالدو داشته مصاحبه می‌کرده فقط چرا ننه ریوالدو مقنعه سرشه رو نمیفهمم
😢
😢
😢
😢
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/101353" target="_blank">📅 20:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101351">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTNWKxXfavKiZwB2KzZnAz_RmiqQHyt2e6J0mrp9B27b0-ZkFxquros-cChCDiVABj-DGH8h7goaVaGz9gQg0hxZ9w95MyJwRxm5lCj6_Kvn5pUVLis7L2SVoobzz87Jupe1mSdcZkP4-DwTwudtAl0hopwxNL7kQy2f0NTZgr4KkZGZc72V1GWCAYeEB6HPRP688R8paRSnuTIO20zOcJ43ttyY7PJ92wL3YupSNDvAaL7bQN1RevsmAmwNBQRMjz9ceQEVzYscvW1hVwyaLG06v9ClPMFg8an1GIGZGpUQxlXXqyx9UDZXhTejJacFncRWfeYM7NHuv2uAorxnYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RjW_LbEK_80xS4A8T_-y0KrzxMR1o44sUmb1Rq7Lv8VlSaTysvI1bQm29f1KPfBrLDI7d8C3jHPPi4EoFEtNf6K2fFdjRi5ZHY8efkNBMc5EsDrm_HrFctqldiS2t1Layl7qmzEQAGSC2muiBRzTMGKyKn16QB3Xo9E4nE-jFd3DPP04zETJnKPum9k2XR2f4KMxbqrndzRGnoNSTFGsYndF30CgF1AHhKRSz0wDZGzxCWMIGhk550bRbA1dFts8xwcnsH5f1CS1bQbAcLVUBiHX5tR8pEHNXaW4q1RSYz3TF9hEi2QlnU7WnrYO1XlS7jtxBwo1HyC9Pji57zLYAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👍
اسپید، یوتیوبر معروف دیشب حین اجرا در اختتامیه جام جهانی مقابل چشم میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101351" target="_blank">📅 19:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101350">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ihd9VAeymAVA3M7ayDa72fImv1qC_B49ozgsR5LJ_IW_jxq9wbSanntTxQiye3u_GrZ-prxJ3ftzi1Zlh9gT5V9eYPpSJZR-MOmR4W_6k5ocUzrKmj-W9qcPnuzbNACBVJ9vQAbCVR7v8TVV_wpfJHgREFrGUVcAy6IFv7_oR43o6FmWvlLZ0kj6JnSCcki9YPgCXfX-48SVHA60ssiQBUfSjK28_afbVXcIrZUkJW3zwjv8YS1i8nyatprzvC9Uxas6U859yVzQHvk5HdnKVhuqrQKk0GvwTy_cAJgFg5fLHWmUqIkzLxmmR2RhrJs9jRkOl2tHZ4OBtxGjBPoIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بالاترین میزان حضور تماشاگر در یک دوره از تاریخ مسابقات جام جهانی
✔️
جام جهانی 2026: بیش از 6 میلیون تماشاگر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101350" target="_blank">📅 19:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101349">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6626cfb5.mp4?token=hK8GOaXSsLv1TBILDICGXBFsr7mMMOo15x2v3XtIhAgIwzzln1Zsl2kxUPiTpnNWc0kr3fBCL1qHptAM_aqZQrIzJufsR46ZPuSmIduoPDfKCVQjVvVbrETEFqp7GWdJdeRi0ux6c_7xQIzFmR4f5igZ6KE9X82G0_mhosQYgZZQW6hYB_KRCwMxT_ZmQ_dta420HOYMHDmEkPuNvw1WEPlJTCn3s7ZHumRabmczfg6HUqu_Lcw34ySICfws7-O21HqqpJwUq490-quxaVDdbBibNHbL-mhUv_DSQfnO0qHhNjOxYMXHsLFP2znaiZX71PN3cXqwY0YrCSVVBPTpCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6626cfb5.mp4?token=hK8GOaXSsLv1TBILDICGXBFsr7mMMOo15x2v3XtIhAgIwzzln1Zsl2kxUPiTpnNWc0kr3fBCL1qHptAM_aqZQrIzJufsR46ZPuSmIduoPDfKCVQjVvVbrETEFqp7GWdJdeRi0ux6c_7xQIzFmR4f5igZ6KE9X82G0_mhosQYgZZQW6hYB_KRCwMxT_ZmQ_dta420HOYMHDmEkPuNvw1WEPlJTCn3s7ZHumRabmczfg6HUqu_Lcw34ySICfws7-O21HqqpJwUq490-quxaVDdbBibNHbL-mhUv_DSQfnO0qHhNjOxYMXHsLFP2znaiZX71PN3cXqwY0YrCSVVBPTpCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
هوادار تیم‌ملی اسپانیا بعد قهرمانی جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101349" target="_blank">📅 19:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101348">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0058133a45.mp4?token=EczE6HRXlEm6CE29kfv3oV12OnVNHh81jqK3vZYICQUKDcbZZuv_Lvw8IVcZS6pSmzgznVz7GRNyUdr9LTevrJy2Nmi0RSDjhQ-WacOHp1jpJ0WZm62J80g5x4g_OGvaWEmdxmPa980eu0fG-vPE36eG-B_qJv2LqmE6iy8bg3msQb7trSoUX-JyfJuLhRMvRpsKEih2LW5P--n99-s5UkIvKlIBabqZ4brfm2hUZ5L_LA2aN6T1xrOj7J4bN0y-y2sWhbGmiGxyUvCx8BVtvTMfdwZuII5GcB7-nos0yaJvvWfr-Aw3ovqn2-HXo536sV7m9CFn1iC5kpobmyA69hf4_-GL0vCBeNQV6WncgWAgXcSwovxLVMeN3p1MzwM4IcmW6SZPHQgF5mEOca-sRW2fcMu_kDRcSPH7-xe8dRHljn-CU43vDA0e2R-3ntAL1KqVtXHHaJ3KYka8xN2RTkgR4uW_DXkzdkUHKrpGc_hN1GpBAKPE5fft9BKFbymLpDTFqKGXh4RsK1JXWO0QwT6jdb0pe68Wd_DUI3YHBIFqxs88hCO8ufbJGP39c5J1xkZV2sG81xp4zVDH2sOadKbcm-f6nncXysPN1ZMV_QpCUKEqyqvl6QN9FFDhuIwiAKhR2VIk8WtVlsFiuIc8kKrAtoIoiXFTYDk_EtpRMc8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0058133a45.mp4?token=EczE6HRXlEm6CE29kfv3oV12OnVNHh81jqK3vZYICQUKDcbZZuv_Lvw8IVcZS6pSmzgznVz7GRNyUdr9LTevrJy2Nmi0RSDjhQ-WacOHp1jpJ0WZm62J80g5x4g_OGvaWEmdxmPa980eu0fG-vPE36eG-B_qJv2LqmE6iy8bg3msQb7trSoUX-JyfJuLhRMvRpsKEih2LW5P--n99-s5UkIvKlIBabqZ4brfm2hUZ5L_LA2aN6T1xrOj7J4bN0y-y2sWhbGmiGxyUvCx8BVtvTMfdwZuII5GcB7-nos0yaJvvWfr-Aw3ovqn2-HXo536sV7m9CFn1iC5kpobmyA69hf4_-GL0vCBeNQV6WncgWAgXcSwovxLVMeN3p1MzwM4IcmW6SZPHQgF5mEOca-sRW2fcMu_kDRcSPH7-xe8dRHljn-CU43vDA0e2R-3ntAL1KqVtXHHaJ3KYka8xN2RTkgR4uW_DXkzdkUHKrpGc_hN1GpBAKPE5fft9BKFbymLpDTFqKGXh4RsK1JXWO0QwT6jdb0pe68Wd_DUI3YHBIFqxs88hCO8ufbJGP39c5J1xkZV2sG81xp4zVDH2sOadKbcm-f6nncXysPN1ZMV_QpCUKEqyqvl6QN9FFDhuIwiAKhR2VIk8WtVlsFiuIc8kKrAtoIoiXFTYDk_EtpRMc8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن باشکوه دیشب مردم مظلوم لبنان در بیروت برای قهرمانی اسپانیا
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101348" target="_blank">📅 19:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101346">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79908eeea2.mp4?token=p-_WpHnZcSSd15awYLHSOT5thSICapaz36lSm2HnvnA9TKnwbDrb-ZO5XNVgBcGoxQ3TnPi37WNmN9aimEc7g6866Sytu_-w50PVRh4aiKZTrXsgc0nNv2a7Ivrmb-vC-H31ZZU9JXNacIDKjRU59xJJ9OiWBFZ8BmLC8S5teebKD4DQg9CdtrgrJDEHvMyOL9E_JlT8Nm9HdSf5bK6e_YuCRRLmFx34Umd7qaVlVsY3W4cqf4RuxnMV7zZz8iQ3A3b5I_UaN4Nxr4sdue_PtIZWnqTe6PDhPtsgbLk_XsPwwg-Kas7rNPy6JI7En-LxmaD3PFOHX-TjmtxyFszd5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79908eeea2.mp4?token=p-_WpHnZcSSd15awYLHSOT5thSICapaz36lSm2HnvnA9TKnwbDrb-ZO5XNVgBcGoxQ3TnPi37WNmN9aimEc7g6866Sytu_-w50PVRh4aiKZTrXsgc0nNv2a7Ivrmb-vC-H31ZZU9JXNacIDKjRU59xJJ9OiWBFZ8BmLC8S5teebKD4DQg9CdtrgrJDEHvMyOL9E_JlT8Nm9HdSf5bK6e_YuCRRLmFx34Umd7qaVlVsY3W4cqf4RuxnMV7zZz8iQ3A3b5I_UaN4Nxr4sdue_PtIZWnqTe6PDhPtsgbLk_XsPwwg-Kas7rNPy6JI7En-LxmaD3PFOHX-TjmtxyFszd5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇺🇸
بخور بخور پرزیدنت در جایگاه ویژه فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101346" target="_blank">📅 19:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101345">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-LMRqohWCUFcXJfRvYGe3wpVj2Xem8PASNHqOAhePTknVkr0tiZ8ieFztKKtUOKL8VHRplrynx3LhSGWYqgNthexrz7S2Wkcs75RFeQBfmqYgztH8zjwfllZortwpisoYIYEnJaAdzMMQ7oM7mA-5DxjM-xfzBYSo3PLVY8I3UXt14FtMfEME_BYedEQI86JTcF-u1tpZRlMUjLMVKdQ3QT5kZGlFZeVQEmc78pqxcdsIt7aFoguvQpQqtS8GulXnP98Gsz9D2Cv-WoFOEOtQLBpR0TVGxgG2ECzJH40KuWExHYiarb8SQwOmgJeLynIjzIjphthHNb7Bh46aeGzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه با ۱۰ گل اقای گل این دوره جام جهانی هم شد. برای اولین بار دو جام پیاپی یک بازیکن اقای گل جام شد.
و برای اولین بار یک بازیکن در یک فصل آقای گل لیگ داخلیش، چمپیونزلیگ و جام جهانی شد.
عملکرد فردی: کم‌نظیر
عملکرد تیمی: فاجعه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101345" target="_blank">📅 19:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101344">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8EbmW51Y9il30lNf5o3hR0Rn2et22tJvQfDhJNcN_cQqf3acog773_ZqGHqxw3MwSIw0DooPpeYNg4Y2GZMx7MhFkqVK2TQtXuzgVVArSivxLCHwg5cebO-bC8xsjkQ-R_usyAhVc1jcZy6gM5ZOxWEYaDz5OFN7pDGmgZqNCFE97aLA7pqeGT5xTQog77lv9KlYv2Es7IQqEO2JVltS9UJNP-x1dPpgUAeCfwjli7ZYHp-xmddMlo81fY902JFPcHY8O4jkumm9ZutMwFVIYf3zSMXrmgbwlyAgKl8RluqyHTTbYKegsxq_Gcl-7xbjriwht2HK-Td6_bKe8kIGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بایرن مونیخ از تمدید قرارداد لایمر تا سال 2029 خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101344" target="_blank">📅 19:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101343">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773a69b961.mp4?token=tMif8DLCT4WDnJp6anXwy2fErt1UxJJqg5PGr2_AhmIqyIvt8hXQEprEgx-nxWQ0ClsW3EGCPos_5RrxijZXmRqDmhZXF0pHY4H0_rlMjuV81qD4dHVZTzsoM7TNQXLirYC47pQSF_HFGIAmICj44bi-N82Ugorf5G2sgCivVkxMORHqCflu0xZ2FqtAILeWYPcPfeAJzC_OOtpLjQq9u9BxVZ8_eNe4TyUn_ufItdHxbOtw8cYq1Kzh4faJXN_jXNWApWRkk7udy-oOP4qSu9Q9yuFnDwD7Uob205BWPXg6o_8DLYCyPaBEz5zJOVtCpuLzKI9yshoFUPFucnTYSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773a69b961.mp4?token=tMif8DLCT4WDnJp6anXwy2fErt1UxJJqg5PGr2_AhmIqyIvt8hXQEprEgx-nxWQ0ClsW3EGCPos_5RrxijZXmRqDmhZXF0pHY4H0_rlMjuV81qD4dHVZTzsoM7TNQXLirYC47pQSF_HFGIAmICj44bi-N82Ugorf5G2sgCivVkxMORHqCflu0xZ2FqtAILeWYPcPfeAJzC_OOtpLjQq9u9BxVZ8_eNe4TyUn_ufItdHxbOtw8cYq1Kzh4faJXN_jXNWApWRkk7udy-oOP4qSu9Q9yuFnDwD7Uob205BWPXg6o_8DLYCyPaBEz5zJOVtCpuLzKI9yshoFUPFucnTYSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های زیبای دلافوئنته درباره اسکالونی
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101343" target="_blank">📅 19:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101342">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5N6v4VLXCgErhnk1AugQbcDy4A8A-V9BbFRcMM35t1trSlPbwHesq36HTWEwaAssdotlK5nhuAyyBfRnfWPUITE4dRrHvgxaZYIj10goc82p_jdjKJd-FgtWvtWnA-Hw_pm7WRlz_yucByVFYspsu-7s1ctISwTJ1j-YrII6hziiR0g4x6FIGaCZKQoaIwniUQkkmQ5XejfcUBW0q_2wuJp3IBYaT-eMSo1A1Na3e5NmdZa2q4De7LkVfZlDl4MVCMQ3Nau9DKFw5lP3SZDNfmE4MIaMQoI5kresEQsJgzjBnWNhgrrapTAh4VGdn6gddinFsxv0PIBelEr_uZJbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
#فوووووری
؛ به نقل از منابع آرژانتینی، لیونل‌مسی تا امروز تصمیم به خداحافظی از دنیای ملی نگرفته و احتمال داره در کوپا ۲۰۲۸ نیز شرکت کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101342" target="_blank">📅 18:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101341">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f3ee1c7be.mp4?token=sE7mVG2tXARYhh0w-io9gbidBgnSoyQjoz9KPh4g78jSjwzbkbvwgV9HryFhfy-J2H4Uva-YcVDobGo7De8jFIi-aZI2lSpM3GJGWVIkRmFNfzFWgI4JgJDZXtXjUuDxrzLydls0DSsAp3crxQqVDDf1UBPg4MDjUQM_hf01ktqEQ3H-tOeROqiyp03HiaoYoimPQgraLUwP0xePvbtf804FMHPupN0I-6EWeRCkQY_nsDZ21qFREr_t1kusbAJOXfg_C67JgEnAw8Jo7MWy3q3K6pvDQUmti-LIkxZlsHFApZJHZc0kmeHEcDdnrn8yZaHzOwHkr4vt4MYwtN8mlSzFTGCiFDE79kIRjalxfaGOcy2dotaLrFuNA142Kwo4whnVSS6ZcFg3Z5eQ1bHmkRb_0l9TOQFfgTqe-ZlhpbOLATk68v3kEmK5BWp2SMZdAT_SjJ2EyuphfQ0WqFgGTHG2F__oKB0i6Gw6BaNraPKYZX7MwXqXJPfVJUWhcgON37MRXTkkkluAZRAinvOrciQcUAvpmmUTxouRI7X7oVaQRXX42OlwVJjutR239e2BrzAYjp17gzh0S20hQG13XoQUHb5HCqnoPF4UTwdM4SyHatJhkmuDO1xgsoexkrYcUxORrh5cbJVZfRZcNAaKAsXVMpLml6cCvjJSlBTGZjM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f3ee1c7be.mp4?token=sE7mVG2tXARYhh0w-io9gbidBgnSoyQjoz9KPh4g78jSjwzbkbvwgV9HryFhfy-J2H4Uva-YcVDobGo7De8jFIi-aZI2lSpM3GJGWVIkRmFNfzFWgI4JgJDZXtXjUuDxrzLydls0DSsAp3crxQqVDDf1UBPg4MDjUQM_hf01ktqEQ3H-tOeROqiyp03HiaoYoimPQgraLUwP0xePvbtf804FMHPupN0I-6EWeRCkQY_nsDZ21qFREr_t1kusbAJOXfg_C67JgEnAw8Jo7MWy3q3K6pvDQUmti-LIkxZlsHFApZJHZc0kmeHEcDdnrn8yZaHzOwHkr4vt4MYwtN8mlSzFTGCiFDE79kIRjalxfaGOcy2dotaLrFuNA142Kwo4whnVSS6ZcFg3Z5eQ1bHmkRb_0l9TOQFfgTqe-ZlhpbOLATk68v3kEmK5BWp2SMZdAT_SjJ2EyuphfQ0WqFgGTHG2F__oKB0i6Gw6BaNraPKYZX7MwXqXJPfVJUWhcgON37MRXTkkkluAZRAinvOrciQcUAvpmmUTxouRI7X7oVaQRXX42OlwVJjutR239e2BrzAYjp17gzh0S20hQG13XoQUHb5HCqnoPF4UTwdM4SyHatJhkmuDO1xgsoexkrYcUxORrh5cbJVZfRZcNAaKAsXVMpLml6cCvjJSlBTGZjM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا اینقدر طرفدار داخلی داشته و‌ نمیدونستیم
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101341" target="_blank">📅 18:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101340">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101340" target="_blank">📅 18:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101339">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIeChJChhF-p63lkUAMsfPoEIZtSIK_tStbnyeROThsxaImIqHT8irD2kQ-5x0uc7rfO__d_9bz0J8-WQ0-bSsmuUPeFcouQxbhzVyeWzstc1MP3GpXecuk-B8398PnKLnHUyULzw8ATQyftHbs2204HSJrhGh5JL1H3omScPvuMlZ0_Kkb1w3NgjZ5itZnqcrWUeYj_h00DZJZ7rW7VFlqrUFr0lGd9d2MBSR_dN-hzJeII9BIAzBFmH40VxkgBpbyH89ASRsuefGhW_gixQCv3Glw5nzqoTFRj2982bFRDl3vh1auA9CDClqbiZu7RdDdilKxkZ_dVzPmJOSQkvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101339" target="_blank">📅 18:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101338">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilUXeIDvqZ1xEqEluOQRiJ2TJQC2g3Spjx1PPCXgyLjDcSgkxItNcoQ-ccTn1FszjTKF-Ek2KvZ17eBM8XgsFnz7dwAKHGWaRm9WXmeVEC-jj9fXSTWvOAWl3YwAQZZvFA6okCy1bzRqCsbkKvw9a3m4q9u6pn2xjrwga6M7_71bfRa_qcPOwirrRNeL7nQUyv33Nbm8WeS_qg-W1gxjTlToWgbQ9w8l_6G9dmGD18pmHAGgy3wrlTZ-VLTBQ4UzluSCSVTjITsCaaqveM2IjbBKlfTUS-R4crIF-aw0cGRvkOgmbzTgV1idL4Osv6RFBjkuP50ZdldgUst5o_BP2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب جام جهانی براساس سایت آنالیز اپتا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101338" target="_blank">📅 18:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101337">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqF9pVA10gW3RaKi5WjRqxe6bwJWhMch4Nf58b7hBEPdvTu8yMJ1OiLymGRXcg7K4Yt61ZTP5LlRmv7OSoOheYIwN00DRb8T2oVbuwHeMmpjT1VAIfN5SrrtYofv0JgQv2qiGNq-oGRFDafHg2ST3sBtf2QzDRm5EEB4vZoAeHjKjKfjLzyNSwWg9lX1Am8i7Ch9W30nVFiXxYBpnlbfjtzz3aBD6GlT-uCknITcIe0piKLrjuiu2j6YUVk9mzU3EtxfOCkLYqKFU3YNnT7-ESRbdiNqRgwK2ex9RPL3f2PrXeQdF8OqeIdEz7A6kopmkLFzUbAKv1scbnn5LRLvQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیوید اورنشتین:
انتظار می‌رود مارکوس رشفورد دوباره به ترکیب منچستریونایتد بازگردد. این بازیکن همچنان به بررسی پیشنهادهای دریافتی از بارسلونا، پاریس سن ژرمن، بایرن مونیخ یا رئال مادرید علاقه‌مند است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101337" target="_blank">📅 18:20 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
