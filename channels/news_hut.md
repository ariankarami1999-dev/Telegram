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
<img src="https://cdn4.telesco.pe/file/PiqEy4w_gDjrhA7C8Xik4pYxYXYPZ4OGUj1xgE2alr31Gz9u2lIEk8VvUof2_9WQ46ve0Z90I6HIh-0uwI7V83gHcJ3HrimYsCM6ihfDLU8pgfQ2eIgY7QqGVx7QF5X0Ew1ayU6ggofK5xGbdgFsKtoGrAEXKrf1bGXK79w0dlF5bmbkti3PGc025IkjDhMoYOKDGjFxNTlAUxIHjh34bI8j4ZZeGiWjbpyOLIvurYK0deNqo61GtGKr6psnIjk2pCfbxarTRKlEcGcHGeZkpWUmOWE7o3rTlx-LO2-y7m6iBkLKkHZku0GB9W4xSS8I5gZXwVY84pzDbEAN2A9Jsg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 168K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 14:58:45</div>
<hr>

<div class="tg-post" id="msg-65184">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
گزارش شنیده شدن صدای توافق‌های عمل نکرده در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/news_hut/65184" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65183">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=Ep4qVcvPr8O_sN8LxMhzFDbtzD1G-ZAzAkoc6KCIjhiLLNYHJdYxPl49QMk6DoCEbgDydUXWyuGSjbLMwPEePhCN89uIX137iWf2lgXwYtMgvSc2UUI0zkwb65B15w6RkdPbZmXvPg_bOJ78EmqoRcLEI2QV5vdPusXUFBgV0Vbxe2243qf7xqt9RAtHduo6oz85yEL-nc_CktPlsnvz3i3vFKrFXIZXhA2REfoLuoA8KHzsbW7RYKxIcW1AupvkrMCAFVXgqjSVqDhhkD-qBezIxve8Ll8Yy38E1_d-VnxolM99uCYwwxaLs-lc2TDIC0TxoTKis2M1rqaWeGckAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=Ep4qVcvPr8O_sN8LxMhzFDbtzD1G-ZAzAkoc6KCIjhiLLNYHJdYxPl49QMk6DoCEbgDydUXWyuGSjbLMwPEePhCN89uIX137iWf2lgXwYtMgvSc2UUI0zkwb65B15w6RkdPbZmXvPg_bOJ78EmqoRcLEI2QV5vdPusXUFBgV0Vbxe2243qf7xqt9RAtHduo6oz85yEL-nc_CktPlsnvz3i3vFKrFXIZXhA2REfoLuoA8KHzsbW7RYKxIcW1AupvkrMCAFVXgqjSVqDhhkD-qBezIxve8Ll8Yy38E1_d-VnxolM99uCYwwxaLs-lc2TDIC0TxoTKis2M1rqaWeGckAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: بزرگ‌ترین سرمایه ایران، «رسانه‌های فیک‌نیوز» هستن که مدام موفقیت‌های آمریکا رو کوچک جلوه میدن
شما یه پیروزی بزرگ توی یه نبرد به دست میارید
ولی اونا میگن شکست خوردید! این واقعاً چیز بدیه برای کشور ما
@News_Hut</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/news_hut/65183" target="_blank">📅 14:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65182">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ke-y9qVTSEgTdMHJxHMSXpyJqlvgpxGIwFzp68VfgGeH3tbpe07GE9g0Z5ZXDN3ezJ-Zsevzsm6FNhEYQoHtFGkrHRLfy5OKQx5_FPW6oxUGjroiazr6kY4ll5f5tS9_Qx-fCthjHA-GmiWbsF2uUQ5Xe1PW5VglL79Jsi9mfgG_sHZCgqVG7Zvgowd4WoBhzGfhTwNyLUi3wyTT_oDZ5RcKNwTs9b0PpattdaNRKChMqZxPsJnGiihCAqP_UyeAmr-H-H7dtZn8LfIRvmX89mTeuiK7D1s--XBmtilhRyvMZ7l5wb44ZsZrZ7NK51lg6Vx07LBP1J2yRrLbeMjiYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد خودروهای پلاک مناطق آزاد  تا اطلاع ثانوی تو سراسر کشور مجاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/65182" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65181">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا #وینرو  بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/65181" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65180">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqwbYiA2lRuAswD9vHc68Zf29qDzvUKiS6_SSnUkYtUULWVz_rDacch2OQAT3ISX62Go6fSqjjPa-bYr61-pqGdA5Q1Oh-RO_A37R2CkyrRaBQJRfqh2FB5GmFxjS2yoQK6m8IR9iOrITwAjwvroLfzJAY2EytEPBzClwFWXbaav4wlM0nHt8Zg7RkXx0OdhvJXwziWtBbzAgh5XTdddbd6ho24yRZ_NKeM6rAvSPfIBAaL4hS90Ts0dKUsGIE5H2R_aBr9gFxjQbsVKB4_zzVfU5fSMclACMokr-yAvAPA-qOeN9LNvN4a-pee8HFwjeZXXkSykciZKMIejMTpVTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r10
📱
@winro_io</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/65180" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65179">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=tli5eaqN6nwXw5WFK8zBJB3ziooR77-d4pCt1PK9FJzwvxsBO0-0BHvOx60gn41cAiRl7u0vFNMFns5ytD3wEHwM5IY07IWwsGK74Po5Mk1lMgbvfvVK3sqQ41RidFXWYMRY60LR4825RYGV6ZX238zpFff5GbesKYtljskAI9YO5DHwf2fqrxQ5TD3tV9VCVm_PWljp12pyBBUAwrhQaAyppA7vVTEajRz0BLuBHkHoDSRR_v-qw803k_djPP7aeqT_ZjT5P6tGbQdiNRM6Cg7Du22v2l1nGNtYAxU4aFnXSzboCaqggzlD8dr6gkCjIdrVCRi95ypqawFEWFL7eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=tli5eaqN6nwXw5WFK8zBJB3ziooR77-d4pCt1PK9FJzwvxsBO0-0BHvOx60gn41cAiRl7u0vFNMFns5ytD3wEHwM5IY07IWwsGK74Po5Mk1lMgbvfvVK3sqQ41RidFXWYMRY60LR4825RYGV6ZX238zpFff5GbesKYtljskAI9YO5DHwf2fqrxQ5TD3tV9VCVm_PWljp12pyBBUAwrhQaAyppA7vVTEajRz0BLuBHkHoDSRR_v-qw803k_djPP7aeqT_ZjT5P6tGbQdiNRM6Cg7Du22v2l1nGNtYAxU4aFnXSzboCaqggzlD8dr6gkCjIdrVCRi95ypqawFEWFL7eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: اگر عجله کنید، توافق خوبی نخواهید بست. اما به آرامی و پیوسته، فکر می‌کنم داریم به آنچه می‌خواهیم می‌رسیم — و اگر به آنچه می‌خواهیم نرسیم، به روش دیگری به آن پایان خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/65179" target="_blank">📅 11:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65178">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=dQcdVT_JQzjcbUILSm52Iw-ZDs9kaU7Yh85LGxu4158f792PCTeE5iHXN2enBkLgEsC4IwlWZgJ3QQwvM9DBrLsJD6zJpzkqMT5qRLfhCvJAIPpr7XDTIvb3QzEZ3YcSsNk9y1fxOfc-k8t5P9xZ2G5x12Cq3CtjaPpH0DERlM_0yCZfU_DCWtJjSzzaTG6kVL5B4iEi5vmnqBuBdW1BU1MDq7VQ0Q4VMVFo2ITEf8LME7CG5CFuF228kHjDFIqXeFG2ZYdnQrenXIW6XxOpb-hYgx8LRyc8Hci-ldtlI1j9GoV0-17CRDxbKqN467qFkwQgm_5xocDOKXghYx2uOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=dQcdVT_JQzjcbUILSm52Iw-ZDs9kaU7Yh85LGxu4158f792PCTeE5iHXN2enBkLgEsC4IwlWZgJ3QQwvM9DBrLsJD6zJpzkqMT5qRLfhCvJAIPpr7XDTIvb3QzEZ3YcSsNk9y1fxOfc-k8t5P9xZ2G5x12Cq3CtjaPpH0DERlM_0yCZfU_DCWtJjSzzaTG6kVL5B4iEi5vmnqBuBdW1BU1MDq7VQ0Q4VMVFo2ITEf8LME7CG5CFuF228kHjDFIqXeFG2ZYdnQrenXIW6XxOpb-hYgx8LRyc8Hci-ldtlI1j9GoV0-17CRDxbKqN467qFkwQgm_5xocDOKXghYx2uOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسین علایی: ۳ روز قبل‌ از جنگ رمضان‌ به آقای شمخانی گفتم آمریکا و اسرائیل با ترور رهبری جنگ را آغاز می‌کنند، آقای شمخانی گفت «نمی‌توانند، پيدايش نخواهند کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/65178" target="_blank">📅 09:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65177">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=GhXLsWIlgrY4YThf9mLSxZuS6ZNKfh4MOzRZcuYVczpeAS6pnuOTR5KvXPEmjgTxcWzRv0GpfXJp7ze-u3kM_1Ym-yPZjKL-dq_H0mLQVINdz_CubJuJxam1glY2jspNQk8srLWZmsiWD8N0dQsiS5GsnfhQ79JJ4KdZMiMbcybEoQxh4ZR3jeMqf8wl_JK5nQtlsBdNRdZN-YIArTBBBIdiWNwbP8mp9eg7pWjMOUsTxgWi3KDLInhigzS3lY2A1CJk1x_jFoMZEDB_6wrM9nKa18Wmd3ktcyV5kWYi6dEf0_YdEzJCHX8jA37Mbn4Fns0d0sG2l9--n8vIQQRHXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=GhXLsWIlgrY4YThf9mLSxZuS6ZNKfh4MOzRZcuYVczpeAS6pnuOTR5KvXPEmjgTxcWzRv0GpfXJp7ze-u3kM_1Ym-yPZjKL-dq_H0mLQVINdz_CubJuJxam1glY2jspNQk8srLWZmsiWD8N0dQsiS5GsnfhQ79JJ4KdZMiMbcybEoQxh4ZR3jeMqf8wl_JK5nQtlsBdNRdZN-YIArTBBBIdiWNwbP8mp9eg7pWjMOUsTxgWi3KDLInhigzS3lY2A1CJk1x_jFoMZEDB_6wrM9nKa18Wmd3ktcyV5kWYi6dEf0_YdEzJCHX8jA37Mbn4Fns0d0sG2l9--n8vIQQRHXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تجمعات شبانه حکومتی‌ها، دیشب سپاه یه قایق تندرو آورد وسط میدون و از نسل جدید قایق تندرو که ساختن رونمایی کرد
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65177" target="_blank">📅 08:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65176">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">💡
میخوای یاد بگیری چطوری با همین گوشی تو دستت از پیش بینی فوتبال سود کنی؟ سیگنال ضریب بالا و کم ریسک میخوای؟ فرصتو از دست نده همین الان عضو کانال VIP یونی بت شو
👇
➖
➖
➖
➖
➖
🎁
کسب درامد از پیش بینی فوتبال راحته اگ این کانال داشته باشی چون کارش بلده ae9: https:/…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65176" target="_blank">📅 00:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65175">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rt7cXiy6cAKFz5HBdIk3dNSW9aDfYR2Pd3zR2_cgUaB8EkN_bv3FDPgA36137YlCUCwfyvWCYFjtTYFhaVpGNHdTMF5kqBff_cpPvvXQLtPDVhyKk8gc9wCp8sWSmXzLihlOgcbhOXix1ktApI_hiNMd5Ctmp42PRmG0uYI-Y_eukhY2tQMY8vfX3JmlHtQNeZ2sUT5tShMtJAr0yBamd_aHEQZNSKYhPsnRoQI1lCh4xOwJ4qpGdBwjP7LIfbtRdB8BaVYcOzVM55jlhWbLx-FQjFWYPK8V3_HYjIbmwVsAghMAMeDTzdCfovf_zgBM51WObo0jhrQOhsV8QSbpXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💡
میخوای یاد بگیری چطوری با همین گوشی تو دستت از پیش بینی فوتبال سود کنی؟ سیگنال ضریب بالا و کم ریسک میخوای؟ فرصتو از دست نده همین الان عضو کانال VIP
یونی بت
شو
👇
➖
➖
➖
➖
➖
🎁
کسب درامد از پیش بینی فوتبال راحته اگ این کانال داشته باشی چون کارش بلده ae9:
https://t.me/+YwYFluMQ5-kyNmY8
https://t.me/+YwYFluMQ5-kyNmY8</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65175" target="_blank">📅 00:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65173">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ghWmI3A9KAy5QywdC2SiT5srph6g142-PVtpkq0sv8m4D_ASWwHu5OXA_ZUxn6i_hZfCErvyByKruL97pB86WpHATgENYPoR5-BlQNk8hxVsZLyb7m96SJufrZS29dQtRB6bY4yR3sim017uRX0lDBCIZO_HxEwQdYVLVY3HstF0gNyBnVzVxE9REfDHcQ_F0NBn0qfCrjC3JQTdgmX4fOZyrwqlXLnMhIkSBvboXYgoRfDa19wNG_x1iucoMKqs1h416F3sTZ4jPivdpbAeEr_V70tj0H1hEvJ-NinLEOa8-Aiuw2KyxkrC67VPZzL9WECJprhpSdUQ-scU-G7lQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vZuLAyDV3YarkhannnrzqKnadL_zdMq2RuafNq3urwHMid1lgfuAt36_zIE19XYuosNddOeHuXgyNnn_0RxN57n0g2oGFLyBmwgIbScGiWrpFOFtCNyqHtS1_jQ_ok3Uq6dv9VtHg8O_0J-MM2DOMg0ZZts1W6Kqk2_8AlJmwGbV48alv9iczEGIicvN_cBmy77oE8CPVMBqXsrzrvGqvyP46nXff_Q_O1W0JXq-xZ-sjbcXtF774IaNIeyIN-WJJZwcZP56d_o_pYAt0eGUnW4-NWW3i9dsmO-t-3owIJxJDAM8Dc1OnzhMA7JNSHpyFYMJtqdqy2nxwWHHKodZmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های رندوم ترامپ دلقک تو تروث سوشال!!
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65173" target="_blank">📅 00:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65172">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=Yyh9HHNY36pjqCTHbIhEE914X4tg81AbggISbHJ6ykUsYnS_s2vRFZEyynbkwQDIq1JlOl1Q0235VaAPMgtxdE4Bn67d4j_qJxtVZ_weVYRo1c78iVMRmhGJckk1pgWZi5aaocI2SHJSx78LpXZSi2_4Zpp2D49UGvW12LGdqU3u8vo7J_N8bBMLgx9AglVYWSBtS--hKUWZX8temUpGr1GSe2qClDlEmumTUeyMJZQu4jeoE4eivFtKkcJSfJTCBR9EKE8QrKXQXQmff1ZDk3S2uyXoarTT4ZUFYDDCID2S46cO_q3dxrsbqmKwAzb-3W5lX0aVE8yMFUZr6fb8qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=Yyh9HHNY36pjqCTHbIhEE914X4tg81AbggISbHJ6ykUsYnS_s2vRFZEyynbkwQDIq1JlOl1Q0235VaAPMgtxdE4Bn67d4j_qJxtVZ_weVYRo1c78iVMRmhGJckk1pgWZi5aaocI2SHJSx78LpXZSi2_4Zpp2D49UGvW12LGdqU3u8vo7J_N8bBMLgx9AglVYWSBtS--hKUWZX8temUpGr1GSe2qClDlEmumTUeyMJZQu4jeoE4eivFtKkcJSfJTCBR9EKE8QrKXQXQmff1ZDk3S2uyXoarTT4ZUFYDDCID2S46cO_q3dxrsbqmKwAzb-3W5lX0aVE8yMFUZr6fb8qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه عده تو عید قربان خاتمی، روحانی و ظریف رو بنر کنار ترامپ و نتانیاهو چاپ کردن دارن بهشون بعنوان شیطان سنگ میزنن:)))
خوب این ۳ نفر همینجا تو کشورن برین خودشون بزنین
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65172" target="_blank">📅 23:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65171">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUi1nLbGz2ky5D3B37taregwCZPJF5ifMxObkJ1TfiF6X3i_i_13n5PCxob2qf_m2pQ2Vdi3E97jl3XQ6cysjTD5OD24P6NXBrt6kvAN32ywpsbmXde4lauZky4Y8k4TT-PSm-wQbwGV4RDk6JM41YXTc6r0jZFeVAn8OQ62dz8FhbwLYihdTCdtppHLKWEZGIlxLjSJzzv471lPgv_Wz-z2OaeZrsVrbofoAuMLgk090_hRq9pxMvNvHGun84v-wABs_V_wzHWNf3tXxiZTQtmMcm-S56pVYiPzeXbOsqypGQHT-z1j533-fpbSps7y6htvx7Z0Vs5lNFJcV8JDDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آلمان
🇩🇪
-
🇫🇮
فنلاند
🏆
رقابت‌های دوستانه بین المللی
🌍
⏰
یکشنبه ساعت ۲۲:۱۵
🏟
ورزشگاه میوا آرنا
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
آلمان در
۱۰
دیدار اخیر خود،
هفت
بازی را برده و در
سه
دیدار شکست خورده است.
✅
فنلاند در
۱۰
دیدار اخیر خود،
چهار
برد و
یک
تساوی کسب کرده و در
پنج
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر آلمان
۳.۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر فنلاند
۲.۶
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۲.۵
- ضریب :
۱.۳۰
🧠
قبل از ورود، بدترین سناریو را مرور کنید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65171" target="_blank">📅 23:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65170">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=uZdTMpyLDIS_lTkxkKbTXEXhatVQOIzYz6tzt63peTHlCoHUU84Os_TMLUmFJKRVBpVL7OuVGY3AkA3X6Z70ps8Pl-kS0UiMNY28qA8CjIsN1fLoe2iLqkyq2vpoW1n9TpMjmRjJjjNeYVWbbVMjUHpKb81P8pSmXSysRWJ0UUXdI8hPiYzIOy10nINxUGm5vLyXQLxvZpNmFoGYUzjSbDyL0nzdi8xcJMaQ-o8_MAEntHWbTDdTynan_ZxJoz6v-2p-oKJ4W_IXhkvMFciIccxvrL8syXRoMY7lNRtDOZl_MS_s2I3Kpj-Xc7mV1-nDoF8wiw643Zk1J5H_-heJ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=uZdTMpyLDIS_lTkxkKbTXEXhatVQOIzYz6tzt63peTHlCoHUU84Os_TMLUmFJKRVBpVL7OuVGY3AkA3X6Z70ps8Pl-kS0UiMNY28qA8CjIsN1fLoe2iLqkyq2vpoW1n9TpMjmRjJjjNeYVWbbVMjUHpKb81P8pSmXSysRWJ0UUXdI8hPiYzIOy10nINxUGm5vLyXQLxvZpNmFoGYUzjSbDyL0nzdi8xcJMaQ-o8_MAEntHWbTDdTynan_ZxJoz6v-2p-oKJ4W_IXhkvMFciIccxvrL8syXRoMY7lNRtDOZl_MS_s2I3Kpj-Xc7mV1-nDoF8wiw643Zk1J5H_-heJ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه‌ای که معاون رئیس جمهور آرژانتین نزدیک بود ترور شود، اما اسلحه در چند سانتی متر جلوی صورتش گیر کرد و زنده ماند...
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65170" target="_blank">📅 23:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65169">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نماینده زاهدان: برخی مناطق شهر ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند
🔻
بحران کم‌آبی در سیستان‌ و بلوچستان وارد مرحله نگران‌کننده‌ای شده و به گفته نماینده زاهدان در مجلس، برخی مناطق این شهر بین ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند و زاهدان هزار لیتر در ثانیه کمبود آب دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65169" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65168">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/news_hut/65168" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65168" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65167">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7n4jhTx4CqRfLOIgydpJfq1t4PZRfKfrojDbYYWPWR2rB5V0Dn945FTmX9-wDJGzcm2C4wZvbMrq43ps3ISVFSPLff199QkwDcad1ax0Y66UT2SnPyiPMM31vCS5i8p-iY_bFIi1Or0NS8w31X4qwIrfuCdq1ngY-upAZMreODyJ9qYOL1aApw9VvW5tz90Aj9s9P0na0YYSnXUBvth6iNZtPA4gUMIF4zZqkBJXe5zuSgGkSKAn_pD39iUV5WAlo4ee_jfrAj5ZkHV9hb1SMGrmZWYYE1_iOI8HLzhLdCoXZo0VD2Jl3C4UWJqiy8lS4xVF9dIOw998aWPLnmk_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت G9:
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65167" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65166">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">کانال ۱۲ اسرائل: نتانیاهو به زودی جلسه‌ای برای ارزیابی اوضاع در شمال با حضور وزیر دفاع، رئیس ستاد کل و روسای سرویس‌های امنیتی برگزار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65166" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65165">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شاهزاده رضا پهلوی در اودسا: دنیای آزاد هنوز ماهیت جمهوری اسلامی را درک نکرده است
🔻
شاهزاده رضا پهلوی روز شنبه ۳۰ می در نشست «امنیت دریای سیاه» در اودسا، در جنوب اوکراین، با انتقاد از جمهوری اسلامی و سیاست‌های غرب در قبال تهران، گفت که «دنیای آزاد هنوز متوجه ماهیت واقعی جمهوری اسلامی نشده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65165" target="_blank">📅 22:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65164">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
⚽️
⚽️
⚽️
اخبار داغ حواشی فوتبالی و تحلیل‌های لحظه‌ای جام جهانی را از این کانال دنبال کنید
👀
اگه می‌خوای جا نمونی، همین الان بیا داخل�،
👇
👇
👇
👇
👇
👇
👇
https://t.me/+5NhkIyyAtBhmMzM1
https://t.me/+5NhkIyyAtBhmMzM1
https://t.me/+5NhkIyyAtBhmMzM1
✨
اخبار داغ  و کانال معتبر
👌
👆
👆</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65164" target="_blank">📅 22:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65163">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEZj3J_RjnpjbgrNOGOEThrRLLhdSNQODfBJn5BBOJylmgbYLOaunZPabo3g_rUkn2Pr1eNmZzsPlCGBYvm11xp2xcO4XrDb83r7DyA-ZHmoj0sBY7N8R4AuDaj8j66xPlq4tiHONjWB25a3zz484wpAuN6jpsqfzUSxf-1qUNoaGkOUWwx8bCmbnSOPxWgAl8a-KlpvfJp3hBTdAy9cS05HOeM0Im4R8R5uIw78yv8gmhIkPW0bKDFHbHNmSetRFmxSKT_74ZFeNvg-t9bAqAkMCPgaQzGjg7LSDYX0NrJMJw9vDUr1HcPh7q5dtwg7tN63HS91A5VrzO71E6OcNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته‌ای که تو تجمعات شبانه دیده شده؛
والله هزینه مذاکره بیشتر از مبارزه است
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65163" target="_blank">📅 18:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65162">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
پیت هگست: وزیر جنگ امریکا: محاصره دریایی همچنان پابرجاست و به‌صورت دقیق انجام خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65162" target="_blank">📅 18:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65161">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3vmDA-6Cto6bRNkYPDXS2VqSiQuT4BMLjY-SJeCi00pJYJ0FVH7gc_y_mq3JvnToWDXSsrUCVNOJug9g7M43jBZQOVyNy_rHhfRBMbd80ao4UVxlRXTnAeSXVwAAwjJkvrUCB_Z1fchxzE4doRrzgghzCg0eqiLstU2I-eN6YvoNl6JtHmNOifn3VFcuOks1tCqXLjjGRMwKbhdYMwPAuBl9zJmG1n6wTTU4K3pOPT9oGBeDAYi4PiuNPZ24Hx6Q0WdqQAXCeef_2mFfj0bJYGiqX4k7e1i5y6yf5jln948sECjwPOD7UaFvbM0ZEeFBvlbHcM1xywy7ZKMmd1MRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی: من فهمیدم ترامپ برای بار سوم در حال خیانت به دیپلماسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65161" target="_blank">📅 13:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65160">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65160" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
✅
🎁
کد هدیه 100 دلاری:
Sport100
🌀
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🥇
صرافی معتبر
🌐
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65160" target="_blank">📅 13:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65159">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U8rpKqA_jGyuJLnKZpj4pEe2rpg84JJCwaE43_2V9P5v2w-LHWS13_nx9miZPUWiAUKTOUIavZAYAAdomx0O_A73GB4aJzPQt6NcLwaaNcnlPRCa7iABIFS0eb3_w8hG5YPZb_0CEMzVZh7aFj3SPXmLRbKEmAmF4tef3zH8xpRyi8VVdhndRAlP7YaxeI5wnUGocFTb8C5FF3ze__F_v1wix93RzXblELxt8dlg_ycM9gkYEYa5pzjNwxgCMRN4w80JdkLU4JNMF-UDpV83_1_s6R1R5aa7khqip7rqbLL4nsU8xu-VSVzV2meKhiOlN9CO2It8gnB-FQpaw7LMYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
فینال لیگ قهرمانان اروپا
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
⚽️
🔥
😍
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65159" target="_blank">📅 13:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65158">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fD-A3YDOLOtQMjXtGo0nG0TuFyg2YGY0pvfG-u_77w9GmU0sxDhO37FlZUGYEvVEpvk57o-ftrYp5_3-t8CjJBowpdWS8wAr68Iq1lHhUlQ4S3VvmeEMl_9tTQHwG2QxqnkQs4avvPgX_ivoIqT_GQhlrpbR9mELJRc0LmpyqBf_rAxSZyFzDTA0FQPUYWv4Gqlelt5M3Ctv4DPWhnDosXbNhYvwrVWpgJshefONtn0y6GAHevMKqcduEBjusVmYj6ayu86LD01Z6EkVeaa2Kz1ui7LoPiGKgw7p40sCMwW7pQtsJRIQQRCEN8OXZEtiyqtKxa4pjPSdbnVkaSBy5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاخ سفید آخرین معاینه پزشکی ترامپ رو منتشر کرد؛ ترامپ ۷۹ ساله در «سلامت عالی» با عملکرد طبیعی ریه و سیستم عصبی قرار داره، و قلب‌ش۱۴ سال از سن‌ش جوون تره
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65158" target="_blank">📅 13:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65157">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
سازمان سنجش: کنکور ۲۹ و ۳۰ مرداد ماه برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65157" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65155">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VvTGHXsq6EWvntWw0wFJX5nzKMmF3x7DE-z6WZS7J915-H73cXFpLcFHvxUeLpLil9jH7f7TYmBW5PheBbSAeh33P3-UGf5V_77Lkm3N3aJRGboB4zPfThD3tgJocmg5qUFntVhSwOvVoz2QogBNDFDTJpGP2lpVBI2YFhmoL8kgLZVo0_88bQSE5LkX79UcIC7Kb-4yHNowdkJ8OXaSvrHLxB1t-4kj_Q2eFwLD6-q3SCDHKg6nbjb6VonTZLltKF4m9HUrbRM_Wc8RKVUvl1RPPye2xwRzbc9efpZ3lzvGm0MV1_mw6-EobB249iN9WszHkWuNmelGmi4Y_nSy_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LgvUJ3PH_qUY97SFwe97GmplZSiOA2jj07i0_FLUidCk0GsXfkfoV45cZxF6b8O1C2ToldWZmh1ZY8dbzGufBV8_LsseKjw1uGFYtkmJtCZ1WSn1CtLelh5OYfn_ZBSI79Dz9T1wNuYU2r_QFDZSIWnQ45Sa4DpqN-kpoDNwfrHA9vhYHglVXqkhE2qnuHilsiUNS9aqVsOmO1iNiYiFBPt0kHpamoo9d_H6zn552AhwZe_ZySdBsEK26RHQPxJpxEtBgNbbrGovCQ4aFYNFwZhmUSPXdq_0hTs_VZd28FpNV4J7fVKKyZLG1dBLAZvaOqx_qaNhv8w1pe3gjYsILA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ملت اینجوری دارن قربون صدقه‌ پزشکیان میرن چون حق مسلم مردم رو ازش گرفتن و نصف نیمه بهشون برگردوندن!!
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65155" target="_blank">📅 10:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65154">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qSUbmuDa0VTc3ABYmv3-eWyMM4YBR9F989j_r9kIFXoAiXIeiF_QYkAW9JY42BNx5iC5X8Z5sysejvbq_2QA83ArkcK0TFUOLaHZRvK6tbZ--GjsheMCHBj1GT5a4lQI766oCYlrRP9lXHXYMNjKmrVL0EoMbo0_v3StR7NTM179FWFYDS1bnkDI5MGYcLzvI7zt85yx4Ybo-9W_gUDt6FVfZiQXZ6Eita6J2j4TLIMb6cAkZnWsmFcPX8LPF6fijCpDC7eUbb8UwRontPrDASlhQ0-pRxQYyxKNSwnj5fP3AJ0DI2SzdCtjr7MJFGhVU3GS_CGmNeD0zhNTmDlTwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از عروسی‌ها و صیغه‌های نمادین تو تجماعت شبانه حکومتیا یه پسر ۱۷ ساله با یه دختر ۱۶ ساله تو تجمعات عروسی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65154" target="_blank">📅 08:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65153">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
😮
تنها سایتی که با عضویت بدون  واریز 500,000 تومان شارژ بی قیدو شرط میده #وینرو هست
💰
👑
#معتبرترین سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65153" target="_blank">📅 00:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65152">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAawgjpbmYPWDMtuiNTCCnrz9dFMkvnXlGecxkCSFTD0kiCg3cKui1a8Ad-tfK0Kh5vlarwpzVDsiKWLQjFmHciosvTqi4jQEuU3rdruhPDsxp2FtIB0Spo3LJ5ln0w6K57oIPG3TjIUiHz552c-09k4aMVEN5jpG9tkQzs8Da0qmbp3R_Zqb2FilsS7t-kDxth9xYxHVndg9CgUtn_MKCppZTcTFat9BEtVyoWtLPAKvEIeA0KoiNMm01ckoXJlgJ4GHBFDC8-xX59_pUZAx3mjvxsw7jUdQeOYLmVfaUHAeGsebWNgaQuf_7KhWR7MQNbnoxDacgrChyQ_lkhDYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
😮
تنها سایتی که با عضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا
a8
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65152" target="_blank">📅 00:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65151">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=vH7O9MK7ap8LE1LRKoZfHlTaKx_ryC3745FelCcgxEN1U8naE8BCumNSN7bqbiO8gZ5ol32D2gVFmp-Do5pyZgGSUO0uNcFh0gBCqPN1x7NHtSsVJq8Ma1-TYTS6tDs5seEh-D91A66QI41LC5UvvZ8K-1HsvjhmPrOnoCSr-_TUQosy51bntYeGDobGeeP-h-pssGYHabBJvT3KOGEWmwoO_syzrrAolfsYRVYTYE8CSnsVx4VPE8l3pquE1xemzLbQyhO3dNEeB12sY5W3KVF7UqujnDynQ91Mjj-44Q1TTCUCMdxdfAeuR7u7RIUrGstUnhGtJWZ-_ZLoePXh1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=vH7O9MK7ap8LE1LRKoZfHlTaKx_ryC3745FelCcgxEN1U8naE8BCumNSN7bqbiO8gZ5ol32D2gVFmp-Do5pyZgGSUO0uNcFh0gBCqPN1x7NHtSsVJq8Ma1-TYTS6tDs5seEh-D91A66QI41LC5UvvZ8K-1HsvjhmPrOnoCSr-_TUQosy51bntYeGDobGeeP-h-pssGYHabBJvT3KOGEWmwoO_syzrrAolfsYRVYTYE8CSnsVx4VPE8l3pquE1xemzLbQyhO3dNEeB12sY5W3KVF7UqujnDynQ91Mjj-44Q1TTCUCMdxdfAeuR7u7RIUrGstUnhGtJWZ-_ZLoePXh1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
اسکات بسنت، وزیر خزانه‌داری امریکا:
ما حدود ۱ میلیارد دلار از ارزهای دیجیتال ایران را توقیف کرده‌ایم — کیف‌پول‌ها را به‌طور کامل گرفته‌ایم.
برخی از دارندگان ممکن است همین الان در حال تایپ باشند و ندانند که کیف‌پول‌شان گرفته شده است.
این پولی است که از مردم ایران دزدیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65151" target="_blank">📅 00:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65150">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNRWgwO4kIgxoMI6g28TS4IVE05GCGDGsnocWgGez2uY0aYUtY8P4JNjBubHvXy9z6vM-WW8mNaL79ZgbWPYvvKGnSsBg7HWVA0_7EJhFIuWFBuIkIaycTpLdDGweHHBsvc0KD6MyAr8K4O_E1ODsI_1ugcvNsNV-8zyKwrIbQk9iqf44WZDta7CeNH5zf57YwWbxwp_4S4i5dHUFawhBMzWM_OXyyLy715wx81AJpop3AfEDH1Fq3Xb2-eb9wLvsh4KPafprcBDzT-2lKFw7SlSVWRLh53G04FfatBshMRV7puLRQJPayVJSgB629EFxlOd8cpEmTyYbQTrjFNQ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحویل بگیر آقای املاکی!!
ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس:
ترامپ باید بدونه که ایران به عنوان پیروز میدون شرایطو تعیین می‌کنه
نقد مقابل نقد، نسیه مقابل نسیه، هیچ مقابل هیچ
البته برای موضوعاتی که مورد مذاکرست نه آرزوهاش.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65150" target="_blank">📅 23:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65149">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2JOuKrhT_OCCkvm7E_-wA9mHR81QeBiBMMSRMSmDSqRAGd33WmVmjDUfMjpRYonwNUF-9RZm5duGBK5Wq5_XY7Ak1Jtua-iNoU9HMWP2yvOttch1lwUkUM75ZxIQ_nGT-Ig8IV_bbc8ofSb0BE7PURTovXyXZXdPnlQjrIEkLCNHw24G5lPm28kNkqJFyTnv3wwwFblly4Cv7QTNsSweTUPvSjcj0cVTO-y-oK7RiHvo46KoXUQC0j4odjgigd34JME6NcgESwd-jtLBpXUqF24nkUJjvcSwhuwupYYtURr4W5zCIsUj-nANrc7i1h6cTIJ8IfWl3brg91vWTEF8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمودی، رییس شورای هماهنگی تبلیغات اسلامی تهران: ستاد آماده‌ی تشییع جنازه‌ی علی خامنه‌ای هست و میخوایم با جمعیت میلیونی برگزارش کنیم ولی زمان‌ش هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65149" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65148">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKG9DR7ELvaFqA2L4dfrqWx-5rPPMhE_HLZyqaXWVmh-5l4VA_Fmubbw8Lz4CbcV0OGhIZvqRBdKJ9uizSDOoQ9KI9dEd7q_7HLvb89oE7FpDTUOyrTdUfp_6U_YiaIhQuYy9VXtgCLvCN8pJOlbpHFGm56OCbXU8HbGwrtXQ-TjJyjutmH-IYZtmnbLsgGxdfEdY2IVEV5MmfWOZNnx29Km6Of0YZcZYphBiOg0ur7MdSbF5_xYAQ74Ruvb0xqq-rFbmVt3CyGc4sElgSyauO5rOW6eo3mCnsLIAP1_VqTPrPzmCatohiP_r2LAw2oVxTWiPXpd2J-HZF1cVgbl2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پاری سن ژرمن
🇫🇷
-
🏴
󐁧󐁢󐁥󐁮󐁧󐁿 آرسنال
🏆
فینال لیگ قهرمانان اروپا‌
🇪🇺
⏰
شنبه ساعت ۱۹:۳۰
🏟
ورزشگاه پوشکاش آرنا، بوداپست
🎲
با بیش از ۶۵۰ نوع آپشن پیش‌بینی
⚡️
با بالاترین ضرایب پیش‌بینی و
بیمه صد درصدی
💯
📊
نگاهی به آمار دو تیم:
✅
پاری سن ژرمن در
۹
بازی اخیر خود در لیگ قهرمانان شکست نخورده است.
✅
آرسنال در
۱۴
بازی اخیر خود در لیگ قهرمانان شکست نخورده است.
📈
میانگین گل در
۱۰
دیدار اخیر پاری سن ژرمن در لیگ قهرمانان
۲.۹
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر آرسنال در لیگ قهرمانان
۲.۴
گل در هر بازی بوده است.
🧠
وقتی بازی با فکر انجام شود، باختی وجود ندارد.
⏩
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/CH100
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65148" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65147">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
گزارش فعالیت پدافند قشم
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65147" target="_blank">📅 21:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65146">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‼️
بقائی، سخنگوی وزارت خارجه: در این مرحله بر خاتمه جنگ متمرکز هستیم و در مورد جزئیات برنامه هسته‌ای مذاکره‌ای نداریم؛ مدیریت تنگه هرمز باید بین ایران و عمان تعیین شه
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65146" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65145">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خبرگزاری فارس به تازگی اعلام کرده ترامپ مفاد توافق ایران را تحریف می‌کند.
او ادعا کرد که ایران موافقت کرده تنگه هرمز را به صورت رایگان باز کند و مواد هسته‌ای خود را از بین ببرد هیچ‌کدام در متن اصلی وجود ندارد.
ایالات متحده باید فوراً ۱۲ میلیارد دلار از دارایی‌های مسدود شده ایران را قبل از ادامه مذاکرات آزاد کند و آتش‌بس کامل در لبنان (طبق شرایط حزب‌الله) نیز الزامی است.
این توافق هنوز در انتظار تأیید نهایی در ایران است. منابع آگاه اظهارات ترامپ را ترکیبی از حقیقت و دروغ توصیف می‌کنند تلاشی برای ادعای پیروزی زودهنگام.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65145" target="_blank">📅 20:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65144">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⭕️
رایگان بدون واریز شرط های فوتبالی ببند از همون اول موجودی 500 هزارتومانه
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65144" target="_blank">📅 20:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65143">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NehVPwKK8zLcrB6ZWxaWQPIC1CM0nBKwc5w3-efLZhHz_i7lCobsh40ZwGu0OJcvgHIG7kjgFOa8qoMEks9Q0Tcz4miAJxACYzflcoR5SDoelxllco9hRSQsE13VqPAEzAp8-roPVq4Z3iG54IoP_XaJ6_P_z6HSUl3-DfYOkeVV0RLyHAG6TFoLEeRGPHYoen9Z3oBVO-Es9dhw5VikNc3DNX5SEM9wV55c_6g1B9q4jQ7AQhHzkxqK_UaNYDKJW1M11phB0J8fu4-5d1VXRHyzKFsWjp9nAYid5pVEa-YdmR7OQfRymmT8HE6U5ktQ9owNqBZoHOjr7agUx9Berg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رایگان بدون واریز شرط های فوتبالی ببند از همون اول موجودی 500 هزارتومانه
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g8
📱
@winro_io</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65143" target="_blank">📅 20:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65142">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kF1GquuWK75sEpuQS7uZFFZoFEnrJqRwqLmPN-t529WSS3NW5xOHhma5sBMXkoaL5VZn2Vp2hMjvuCMqhEOW9HX1YOuIClpJ_Tx6sqqzMzF-YXnZukjP-M74gBjIoqavI5wcnjmHpQEiSFAVastY_UlidY8o86p3ol5kR0cB3c7h-hteSHnk7Y8pDML48BN-Xee4egYf5GXALs7etcq0H-ka-JTcH0shNGnNLDRaDjCrzaebxcFMDLaIKYZ7MHKaQT9mb6e6dubJ3D4PpoygXtY0px1uslcvp8vfJwXvJ-27cpgcG82MDgAaJzU_BymXPm_zym7i5sG-MDaELyH2RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:
۱- امتیاز رو پای میز مذاکره نمی‌گیریم؛ با موشک می‌گیریم، مذاکره فقط برای اینه که طرف مقابل بفهمه قضیه چیه
-۲ به قول و قرار و تضمین کسی اعتماد نداریم؛ فقط عملکرد مهمه. تا طرف مقابل کاری نکنه، ما هم قدمی برنمی‌داریم
-۳ برنده واقعی هر توافق کسیه که از فرداش خودش رو برای جنگ احتمالی آماده‌تر کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65142" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65141">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⭕️
🇺🇸
🚨
🚨
ترامپ در تروث : «ایران باید موافقت کند که هرگز صاحب سلاح یا بمب هسته‌ای نخواهد شد. تنگه هرمز باید فوراً باز شود؛ بدون هیچ عوارض یا هزینه‌ای، برای عبور آزادانه کشتی‌ها در هر دو جهت.
تمام مین‌های دریایی (بمب‌ها)، اگر وجود داشته باشند، باید از بین بروند. ما با مین‌روب‌های قدرتمند زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز فوراً مین‌های باقی‌مانده را پاکسازی یا منفجر خواهد کرد؛ که تعدادشان زیاد نخواهد بود.
کشتی‌هایی که به‌دلیل محاصره دریایی فوق‌العاده و بی‌سابقه ما در تنگه گرفتار شده بودند محاصره‌ای که اکنون برداشته خواهد شد می‌توانند روند «بازگشت به خانه» را آغاز کنند! از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین، زیر کوه‌هایی که عملاً در اثر حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند، دفن شده است، توسط ایالات متحده بیرون کشیده خواهد شد کشوری که طبق توافق، همراه با چین تنها کشوری است که توانایی فنی و مکانیکی انجام چنین کاری را دارد و این کار در هماهنگی کامل با جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام شده و سپس آن مواد نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی رد و بدل نخواهد شد. درباره موضوعات دیگری که اهمیت بسیار کمتری دارند نیز توافق حاصل شده است.
اکنون به اتاق وضعیت می‌روم تا تصمیم نهایی را اتخاذ کنم.
از توجه شما به این موضوع سپاسگزارم!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65141" target="_blank">📅 18:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65140">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEbFx9vgjaItp0tcd4kbGrmPSz38yYC-Ygpf8W8Ei6F6Ww0ruLUA3f4dCVOp7qcpJeqin2Rfw4v00XKcUPfIL12NCqaMKeiPWHP4gbiu5CeLDc_rxl3ga1-WsIe0GF6sSzbN_ZTnspLqsC5btcQVmw9li7q7rf5xoWso-1kdwpxncjax2pxSp13v03c4EeIqtnzs4bKyPOADFQp6sZn2gyrkJ8fvSApuG0LeVyykxEOhxLkiFU1t48kV9FQ87qXd6NY89XJwa52zWTMBtVV4HFIBk6fYswS3dWpK8_z3SkWLEr2dwqxkb0TCYFwbUffTsP9jHvFN75_wibpNe2RkhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی مشاورین املاکه
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65140" target="_blank">📅 17:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65139">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">Barko VPN_v2.2.apk</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65139" target="_blank">📅 17:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65138">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.2.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/news_hut/65138" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
بهترین فیلترشکن حال حاضر ایران
👉
💎
با همه نت ها پرسرعت کار میکنه بدون محدودیت
💎
👌
پیشنهاد ما دانلود این فیلترشکنه
🔧
لینک دانلود داخلی با نت ملی با سرعت بالا
👇
https://uploadb.com/plx39j7b72sy/Barko__v2.2.apk.html</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65138" target="_blank">📅 17:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65137">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gbqoq6LZZfJgzTn7ujWDaycAb2-OojzyAr492yalhQrL9UOB5jQn-s5KAWbhXKLfXoztwtIoX1ZsepRj-A9FI7ZazsyknLTce71YKuOp6T5_b1YejXdWh7X2pJmpLWnaY65H7Zxe2R-DUY4e9dcMO_BrOxRdNrAAg-XMxNu-txk6DUQhxoMqLqEKFrXsfp2K9TJZjm_XrDzyMyuGY3OKb3eb7RPnNo9nZyLM_wSOYpOMMQfdM9xWsJ8Id1t6tfw7FjD7uN8H5of4adOAgAGMBCEOy0-9DYS0P6aADRzn_5_9aGo1cPVGVLVmD5L9-936IyWjDlzkMjrgIGibnQ54hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نت نداشتین این دوتا شده بودن سمبل شرافت و نجابت حکومتی‌ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65137" target="_blank">📅 14:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65136">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAinGxGakIhwEaYYgHAdhqe0NNw_3araLVNxUUIOLqNME8Vt_B0v2ORD9PszR-HCUeUuS9R_adJJi8l7FZhfcRTaxs-6Id3unlQnCEn4XlAyxATHe3orROxwDTz_F4U7nRQ7tTw5cI4PgKFzAMeha9gPBJ4t0Ya2ewz7eukS142uE1DCFMft-4mKXxQQ3DDkkJf2bD9QPYc1izLT0iMbvWyaYvu_IRmzZxlmhJ30IXBZQHWpljCPMhyYWk_I4DH4mbjD9ZmDDmtONyd_ZUOsSQEb7u96ulSweGJQMV_LiT7qoFdJXlogWsLJhRnm083B0AjXUwS8uulz41hysXmN8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌های حمید رسایی تو کانالش درباره چه کسی شایسته جایگاه رهبری است با آیه‌یی از نوح و پسرش که حتی صدای خود طرفداران حکومت رو هم درآورده
خیلی‌ها میگن مجتبی رو به پسر نوح تشبیه کرده
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65136" target="_blank">📅 13:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65135">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=PpUKop3eEWhiz9Ina2b2-9NFbIe7RiI4RbHMdIgmgLm7JLSMjbUcskm8vJ11OgmCPEFMWSlt50qXxYqEHdYVYWTFLD84XGeWStW5i5Pfz_12Eve5Pw99OdVcnIsWG9EnAEdUpoXrjQeMzroufiyA7nIV8Tx-1NAHmdx5lLVNNnpBlrTAQ-Fe9P7SZZ0bsIBcQ1XI_roTYql18mQMvshDfy-WQxsYljJ1pQ7aQmzsmSaC7z5eimNqfXroEBO_GlqBc0mEanwrZgBaA_O-LfMksOo8UbHeZmSqAcvh7DRJ-h5gh45rBle4R8gcHZeDpdr9LnqkSQDFzwDiTL4Vd-6j0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=PpUKop3eEWhiz9Ina2b2-9NFbIe7RiI4RbHMdIgmgLm7JLSMjbUcskm8vJ11OgmCPEFMWSlt50qXxYqEHdYVYWTFLD84XGeWStW5i5Pfz_12Eve5Pw99OdVcnIsWG9EnAEdUpoXrjQeMzroufiyA7nIV8Tx-1NAHmdx5lLVNNnpBlrTAQ-Fe9P7SZZ0bsIBcQ1XI_roTYql18mQMvshDfy-WQxsYljJ1pQ7aQmzsmSaC7z5eimNqfXroEBO_GlqBc0mEanwrZgBaA_O-LfMksOo8UbHeZmSqAcvh7DRJ-h5gh45rBle4R8gcHZeDpdr9LnqkSQDFzwDiTL4Vd-6j0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماهواره فضایی شرکت آمازون دیشب حین پرتاب به این شکل پشم‌ریزون منفجر شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65135" target="_blank">📅 12:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65134">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⭕️
بدون واریز شرط ببند و بازی کن چون وینرو با ثبت نام و بدون نیاز به واریز
۵۰۰هزارتومان بهت میده
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65134" target="_blank">📅 12:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65133">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLze21jMCh8hEG_-GMUhMOe4bdGWa9Dj2abQhGpVCe1ux81wbtywotUHsz9dzszSiUX0ziDxuUR2hE4TQ5QLi8YjR0D18yI44sVUAFJH6685FnmxQQ25doOQL4CBV9scyg8DQNMNNBcpIoEPGgpciY7rvUoFWv2OK80WSnDsQHFLHODilfwLqL-abTBYBpF8NECA0rlmpc9OWoYKwseR-yghOAj5WHv_a9rwQ75WMUraU93g6e-MrUAiGlwx6t1IAc23zDANrdnrT3gB-osF_xIZRoHiL4eAoBXs152bwLr3Wbsl49XBxU-jSdM4Wl077CXSc_N7u_NPemOXhecp4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بدون واریز شرط ببند و بازی کن چون وینرو با ثبت نام و بدون نیاز به واریز
۵۰۰هزارتومان بهت میده
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r8
📱
@winro_io</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65133" target="_blank">📅 12:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65132">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pT35ludnnN_ClHBkuv18_4HAfo-6-TIelDSpHmiH665U_I53U6cBthNxyE2gHFpRtMNwFekIXFUGZYyAkbT6PYpRiz6FaciDELZb3oUywysBPkOIrRVxCE7xGvuh-0EfLu-4cQeLto0blnmcdLG7FYJaENqQ764pQoLqJDmy9OsjLJJB2Hjg6-wINJW7B_y8cj2HTGSM3sMXzX_687Vbct8V4SxzpuxLMk75Gz3-3Oc2TXLbgtZjdmnfRAbVIE4HJhrb3VTs3TzN3ctwpm2dm1AN6fxx86ERtRYGVxM3FBdCdnX-D2yJeY3Fo4UKXMocTwfUs2s1Rmin19Bibfo_CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
واشنگتن پست: دولت ترامپ داره به اداره چاپ اسکناس فشار میاره تا ۲۵۰ دلاری با عکس ترامپ چاپ کنه
قبلا ترامپ ۱۰۰ دلاری های با امضا خودش تونست به چاپ برسونه و اولین فرد درحال درحال خدمتی بود که این اتفاق براش افتاد
همچنین طبق قوانین امریکا عکس افراد مرده میتونه فقط رو اسکناس چاپ بشه و از سال ۱۸۶۶ که این اتفاق بی سابقه‌ست
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65132" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65131">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=Yg7Ap0z4UrFyNEOc9EHz3zTx6sXaPL8jAjz6xR68gbw_IA0InzjamqCma5P-vpRCqlRC5yetHonGSOI9pmQZO1Ld0XU1XmLcrtE5xZNc81N7se3gMUKzUvZE0dUWBWje6KOdU1KQbjsNKL3FOX4O2w_DbqTNVyym-mRioUgXH91CRSL6bpCJ14ELBEOZUkhL0imIYjts6JEVCnvTw0zz7lVJp78qWwPg0XvAFJafkjPofpctXpmPWjikn4vWHN3rMOcixv9fj4k-ZskEEbQbEHRgtxDdk8RmfrGpH7qUv2I-MXA6AsIWvqY90L45ngmwrFpTx8rU07HxqTJycJ9_1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=Yg7Ap0z4UrFyNEOc9EHz3zTx6sXaPL8jAjz6xR68gbw_IA0InzjamqCma5P-vpRCqlRC5yetHonGSOI9pmQZO1Ld0XU1XmLcrtE5xZNc81N7se3gMUKzUvZE0dUWBWje6KOdU1KQbjsNKL3FOX4O2w_DbqTNVyym-mRioUgXH91CRSL6bpCJ14ELBEOZUkhL0imIYjts6JEVCnvTw0zz7lVJp78qWwPg0XvAFJafkjPofpctXpmPWjikn4vWHN3rMOcixv9fj4k-ZskEEbQbEHRgtxDdk8RmfrGpH7qUv2I-MXA6AsIWvqY90L45ngmwrFpTx8rU07HxqTJycJ9_1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: کشور‌های عربی مثل امارات و بحرین و مراکش برای تاسیس دولت فلسطین به پیمان ابراهیم نپیوستن بلکه چون اسرائیل رو یک متحد قدرتمند علیه ایران می‌دیدن به این توافق روی آوردن
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65131" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65130">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDZdtaPN6NOVd2oVJAuuT-gUsp5joy5sGe5QfAmP4KNZ5cv-CRDvs1LkaifghhGVwBe6SuKAuzCw_OC2lnfBqy20zcNq1IHCFoY8FoF89KI1-xKavIU0-hLEBJndfRFzTK4uJqIrxPOqA6SF53PVN3d4xItL9-IPzuQ_5KPF8MinKTQJulqJ6aWOx1_LWRhuCFy5cDraZkoSPHY7gq3RDqJ33T05pcQrn8sUiY1hz6EWjYZj6-Y7fvTHOWSQajmki40SkMSlu3jKKsiadK8fMS1B484Ef_te9Kz3Qc7tEb_jH-QD2vWHp9HXMre-aY-BEyRLQPhP_8GKNkjgtu2r_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش دفاعی اسرائیل: از زمان عملیات غرش شیران تقریبا ۲۵۰۰ عضو و فرمانده حزب الله و ۸۰۰ نفر از اعضا رو از زمان شروع آتش‌بس حذف کردیم‌.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65130" target="_blank">📅 08:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65129">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
اگر همین الان توی سایت #وینرو عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر،…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65129" target="_blank">📅 01:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65128">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9LsH7ku4S5blMaydcFSywFsFbdrJuYUmDDWJnpUGfn2aHOWlJlhyPuofgcvZgAQ28crxViLjMNRTzsOPpEYfLCmbF5f5g9hk-85PfyMzOMgnRMvJIgze-PZT40HKzlUcvIeLAgQwqu_6aPBrotoRR-1YHAA8LUeM43yr1yK-egJOM_NHLi2sgn5PIfVAxaNkr6t0OL2slhFj_tkEpkyYC_XOwIgQTncWEQElyq36IV2DlR87jmdhhNo3XZ2uoZOGbzhV2ukUoUALleH9a-DZbGn5z7g31hhMq0Ek9DQCHJKJePe8pQdfAsrUfLncBrzy5Gk_o_-CxnWkQdFjkhNjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگر همین الان توی سایت
#وینرو
عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
🔴
این فرصت محدود رو از دست ندید:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a7
📱
@winro_io</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65128" target="_blank">📅 01:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65127">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
گزارش صدای انفجار و همچنین پرتاب موشک از شهر جم استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65127" target="_blank">📅 23:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65126">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011753724a.mp4?token=g7QVc0t-bkCGe2sH7WwHL_u6a3mZfkfPNWvghf6h3eSrOzDuaXC0g4euyW4xJNPq2wdrjPeDoP7H99TpWFSoZlwcTu0V2B0rFMpnNQ9VzTLBvFACqAscTOvRVDeZCopNs-pPoEExEVgpc0SeymWBbFH5r1AfP71UqmIEwsskE8DkaYysbVgQoWMOyfYm5q1bw88yEzVKN6tzm_4tzh6y1MB4VA6KI0-Q_KYfdJ0XUsq5gCZeAMmHYqcK5igmO2rfl2579TT8vth6S5w_XC21sR9bDZcMSK1Xk2SH3Zec2g47mpcMzyMA0jz8ifOL2glIiVKjhIKRlVeti2RB73vqpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011753724a.mp4?token=g7QVc0t-bkCGe2sH7WwHL_u6a3mZfkfPNWvghf6h3eSrOzDuaXC0g4euyW4xJNPq2wdrjPeDoP7H99TpWFSoZlwcTu0V2B0rFMpnNQ9VzTLBvFACqAscTOvRVDeZCopNs-pPoEExEVgpc0SeymWBbFH5r1AfP71UqmIEwsskE8DkaYysbVgQoWMOyfYm5q1bw88yEzVKN6tzm_4tzh6y1MB4VA6KI0-Q_KYfdJ0XUsq5gCZeAMmHYqcK5igmO2rfl2579TT8vth6S5w_XC21sR9bDZcMSK1Xk2SH3Zec2g47mpcMzyMA0jz8ifOL2glIiVKjhIKRlVeti2RB73vqpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا کاهش تحریم‌ها برای ایران روی میز است؟
اسکات بسنت: هیچ گزینه‌ای روی میز نخواهد بود تا زمانی که تنگه هرمز باز شود و ایرانی‌ها موافقت کنند که باید اورانیوم غنی‌شده با درصد بالا را تحویل دهند و نمی‌توانند برنامه هسته‌ای داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65126" target="_blank">📅 23:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65125">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8HCzxZ60654kcodPbOZU8t6bK6xaHtUvEZxOBhT4gemniQuOjuRUxAkPablQjKNUIkqLUHbZG8rZJElNcpe1ZXk2ReRXjtffMQtrgumXL29kufWCsRCOmGzjl4imC9TQE10MlYyjYQZI8PGSrm1Yp5h8jK24uYQcQdlwKny27Q3NE99XEitLL2oX3ZD3iRdlh_scmLgGlNMG1RyPQI3Kr85h9o-iiIIaBxhp8dDMeBtZ2hyoJ-n64UreJoTRCJ-BoVXmLQhPAiQPnkiQ3cUkiAbtdiJX-p6y3vD3QOGV8VpA27PlAMfQHDKEb-78fordFPLGM9WOYBU691G9F0ZwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
گردونه شگفت‌انگیز جام جهانی
🏆
⏩
با پیش‌بینی رقابت‌های ورزشی و بازی‌های کازینویی، مراحل هفتگی «گردونه شگفت‌انگیز» ویژه جام جهانی را تکمیل کرده و هر هفته تا دو چرخش دریافت کنید.
اطلاعات بیش‌تر و قوانین:
🔗
bfrd.link/WCW
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65125" target="_blank">📅 23:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65124">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🇺🇸
#رسمی
؛ توافق موقت ۶۰ روزه‌ی ایران و آمریکا نهایی شد و متن توافق، فقط منتظر تایید ترامپ است، هرلحظه ممکن است خبر اعلام شود
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65124" target="_blank">📅 22:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65121">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=LH_nSVGp_ZRp6Wr0IjZyXhRrapv2MmUr68dt14C82ceQ6NxClDgI7R-EHem21opXKeY4Q_ya17XtQ2DTk3AF--NQ2QumLFZWmXDThonvX_rDWn6WncGbG_Yp3rO8REAv4-MHMVFBcpnZyXSqTUK0HVBV7BT5s6vUigOoeGixHx4fKsJZrQpHCOEX8w5qk6cLwdZ1ypWAoTD0idIyvhCOS_Y4ULQwHEVJCrL6bFqTrz6MHOgBKgHBFQNqO5EfxDlJyCudzyCSKVEq9ztZPjoxvAjyvTAKb0s5LUIxIsITooMJpnOOWCseelUiV2Rt4PWKpDTnbm61vUWl-JO9gyCe1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=LH_nSVGp_ZRp6Wr0IjZyXhRrapv2MmUr68dt14C82ceQ6NxClDgI7R-EHem21opXKeY4Q_ya17XtQ2DTk3AF--NQ2QumLFZWmXDThonvX_rDWn6WncGbG_Yp3rO8REAv4-MHMVFBcpnZyXSqTUK0HVBV7BT5s6vUigOoeGixHx4fKsJZrQpHCOEX8w5qk6cLwdZ1ypWAoTD0idIyvhCOS_Y4ULQwHEVJCrL6bFqTrz6MHOgBKgHBFQNqO5EfxDlJyCudzyCSKVEq9ztZPjoxvAjyvTAKb0s5LUIxIsITooMJpnOOWCseelUiV2Rt4PWKpDTnbm61vUWl-JO9gyCe1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درحالی که جمهوری اسلامی اصرار داره یکی از بندهای توافق آتش‌بس تو لبنان باشه  نتانیاهو و اسرائیل در روزهای اخیر بشدت حملات رو علیه حزب‌الله افزایش دادن
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65121" target="_blank">📅 22:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65120">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">به گفته باراک راوید خبرنگار Axios، به نقل از دو مقام آمریکایی، یک تفاهم‌نامه ۶۰ روزه توسط تیم‌های مذاکره‌کننده ایالات متحده و ایران مورد توافق قرار گرفته است و در حال حاضر منتظر تأیید دونالد ترامپ، رئیس جمهور ایالات متحده و تصمیم‌گیرندگان ارشد در ایران است. طبق این گزارش، این تفاهم‌نامه شامل بیانیه‌ای مبنی بر «بدون محدودیت» بودن تردد دریایی از طریق تنگه هرمز، رفع تدریجی محاصره کشتی‌ها به بنادر ایران توسط ایالات متحده متناسب با افزایش تردد آزاد دریایی، تعهد ایران به عدم پیگیری سلاح هسته‌ای و تعهد به برگزاری مذاکرات در مورد از بین بردن اورانیوم غنی‌شده با خلوص بالای ایران در بازه زمانی ۶۰ روزه خواهد بود.
علاوه بر این، طبق این گزارش، این تفاهم‌نامه شامل تعهد ایالات متحده برای بحث در مورد کاهش تحریم‌ها برای ایران و آزاد کردن دارایی‌های مسدود شده ایران خواهد بود. همچنین قرار است در مورد از سرگیری جریان تجارت و کمک‌های بشردوستانه به ایران بحث شود
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65120" target="_blank">📅 19:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65119">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⭕️
توییت جدید اسکات بسنت وزیر خزانه داری ایالات متحده.
دولت ایالات متحده هیچ تلاشی برای اعمال سیستم عوارض در تنگه هرمز را تحمل نخواهد کرد.
به ویژه عمان باید بداند که وزارت خزانه‌داری ایالات متحده به شدت هر بازیگری را که مستقیم یا غیرمستقیم در تسهیل عوارض تنگه دخیل باشد، هدف قرار خواهد داد و هر شریک مایل به این کار مجازات خواهد شد.
همه ملت‌ها باید هرگونه تلاش ایران برای ایجاد اختلال در جریان آزاد تجارت را به طور کامل رد کنند. روزهای ارعاب تهران در منطقه و جهان به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65119" target="_blank">📅 19:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65118">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا #وینرو  بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65118" target="_blank">📅 19:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65117">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LK-8jVD-apyBFFDBK0_y0yH64qDMZ3o3kb7oPOWoLMbVtftZfutqqiYyxgRw57s1r9EYzdj5w2eVbhHoS88SW72LwB8I4texyBEQGL01DoTO73QoKaWRbF1y10v1i7lNLZhRUfIS7mZ0leBV2XAT5RFw1DyaWao8-ucHVdzi0PJ7A9MwAHUAC1zRspAJYYtQvi2i9MGaBisYh8k3lnvaqRz6gfAxwoZ33EbNa2aixcsVHYlchOmrIZsnFk7gW87EgYqcJ94DLWPZ6QDIlrRkmLQDqax4EmyfL-KL_jBhhS10iMJ4An_anAYYIYiKzBbBkjw8NJnlCFoHNMbqNkCPVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g7
📱
@winro_io</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65117" target="_blank">📅 19:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65116">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9Ahz2pJmtZUaicQA91jBR3xrie51pugwZNdsMWJYOngiLuy-WMv_KCwnOiiz68fFMhBDcORnSX9_BM1MKHKr6f4Sxn6U9_tVk5vXb2cqrZcRCjyyIlnvagFQuLUsaFC47FUK7aN3afg1xQtBTRiOmHC-Cg16XpbfQRwrYY4pG0p3DjPcTNkeM7Mwsg3cBj-0eQZBbgjoGpu5Dy1ck0iDOorcJE6wZgCp2rdcNL4HyVJfaDSXdyXaYD0VoDK63ajPpFgho97YkOoHomLmUOzXot3kpVw0VxlJpggT3QZT8P4sWimAbu-rSdomZMobwXIHVZkh2vI0CzBJkQraPW-Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📰
آکسیوس: اکثر شرایط تا سه‌شنبه نهایی شده بود و مذاکره‌کنندگان ایرانی بعداً اعلام کردند که تأییدیه‌های لازم برای امضا را دریافت کرده‌اند. ترامپ در جریان توافق قرار گرفت اما به میانجی‌ها گفت که «چند روز» برای بررسی آن می‌خواهد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65116" target="_blank">📅 18:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65115">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUIF31mZjcZzrZ2XpsAAj1g1mUmpbugVBjPckwYVryC5xenYiaof82kG_ymyRqawf4k3r-JMoWnTA72cp-aB9NIBmS_AUWWP5OHTCXqFCQAcM5suRDXjT9KpMFFlVGE1MBLcOCbr-x_DeOJdOkk51bywRevxXaRn2f3w4GNwe1-XFPfYXhXrWWBnJcfZU_Ta46wTWzoRetPiGobPYr5CYkN3EulrX3-pj_o-olbxoeYqXtc5cFhLIZxwRN3kBZvn7IvJsSZaR_YJeJo-wR3CVxLH-Ptr8zfq-Dz7ju9Dn007cXAHY2CeZUchY6Q-rVRjdBuzNxfpamgJ9_ok1YxFTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوارنگاره جدید میدام فلسطین از حرف جدید مجتبی خامنه‌ای درباره اسرائیل؛
" رژیم صهیونیستی 15 سال آینده را نخواهد دید"
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65115" target="_blank">📅 16:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65114">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Xi7XNTmvmO1Y96SonqylcD5TWN5VoUMt7Csd2aoEZYoh0U_p4rAA8GlTUN3qdq0jYr9FEtP-HCr1cuzIqjJ1JwuklY4DCIRXlSt5yRFoi-RFqjyNbLABPDdPdMZM6xFKU7MPTNpee1BDdhvvWrtrPSW5FWCyPds0kILUynrQozk_8din_TK2WnME_ybSxDZv-ImT9u6EuXdiQZy3IiC1xi-rb-s48rV6UmpwLgyJ38Yw0YQIjMJiZna58JFnlpS7npDgL_JgD1gNK8vKpzlUVk7sHoi3xKiaecMYKZnQg27sdl5rN7ZqYk4Y3B7phMrRFtwuMNorn0GpdYyWHtVrTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا پشمامم حقیقتا ریخت
✔️
➡️
تبانی نتیجه دقیق ضریب 15.00 رایگان
😳
10 میلیون ببند 150 میلیون ببر تضمینی
💸
فرمای تضمینی و صدرصد رایگان
⚜️
🌟
https://t.me/+BDjkK6j2gcQ3MGFk</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65114" target="_blank">📅 16:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65113">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJ2xmDM0SUXNbYP5b1ZzbkH2tlasTZzKxJHz3L-yo3r0VBHf4w7aLciwgLXyrvmR8PEad_pxXXzEmbk3gm5toxcM31-GJR-qU6gIKqA45tiO9S2PgfkHCa9otH_JXN5-714IgSMIQ8z5zTK9cNDTpemKKst93IE3B0t29gEZ1bSF0TwmgufUMIBiN0TU4U_6tRdM4NiD3nQe8SyGRM2miCpD0nHWigx1spux3mePj2SybGd6sz-yUPP1oT3dNzZDFYeN5bioJ8tkaBjvhxI6xwia4zv7fY2UTWdccYt5A1bUrlyHUDd77NcdbaQxVAAgQlCMxFJvwliApVJTA0buoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⁉️
نت بلاکس
: سه ماه پیش در چنین روزی Iran دسترسی به
اینترنت جهانی
را قطع کرد. در حالی که اتصال اکنون تا حد زیادی بازگشته است، شاخص‌ها نشان می‌دهند که کاربران هنوز با
فیلترینگ
شدید مواجه‌اند، مشابه دوره موقت بین اعتراضات ژانویه و آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65113" target="_blank">📅 16:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65112">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حملات تازه اسرائیل به جنوب لبنان؛ تل‌آویو از هدف قرار دادن زیرساخت‌های حزب‌الله خبر داد
ارتش اسرائیل اعلام کرد حملاتی را در جنوب لبنان انجام داده و زیرساخت‌های متعلق به حزب‌الله را در منطقه صور هدف قرار داده است.
ارتش اسرائیل در بیانیه‌ای کوتاه گفت این عملیات علیه «زیرساخت‌های حزب‌الله» صورت گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65112" target="_blank">📅 13:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65109">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">باراک راوید، خبرنگار آکسیوس: ایران ۴ پهپاد یک‌طرفه به یک کشتی تجاری آمریکایی شلیک کرد. ارتش آمریکا این پهپادها را سرنگون کرد و پیش از پرتاب، یک واحد پرتاب پهپاد ایرانی دیگر را در زمین هدف قرار داد.  @News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65109" target="_blank">📅 13:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65108">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/news_hut/65108" target="_blank">📅 03:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65107">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/news_hut/65107" target="_blank">📅 02:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65106">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">چرا نت من قبل از وصلی ها بهتر بود، چه وضعشششه آخه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/news_hut/65106" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65105">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">عمو Pishgiri بهم sms زده و گفته خشخاش نکارم
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/news_hut/65105" target="_blank">📅 15:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65104">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/news_hut/65104" target="_blank">📅 15:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65103">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65103" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65102">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:  @News_Hut</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/news_hut/65102" target="_blank">📅 08:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65101">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWQNe8_NLiGEGl1CN0J1Vb1I1XW9tnvzCHbPQu0O3P0fuLnJaK2N1OltS97QXprbUWoOefdwbwC8iN-9vleDW5VDXMNWF0AsUEtXoVRdHcIEVVEu2d-md7qvEj-Qm9BzgOV8nxuFR7ZEfNSC9I-Z0siDnu9a-5KkiTITqKbxAB1cYyv4f_s9zyNpnkY9DeFupHjTyVEIaSz0jVfsASVZ5Su9aIwmPDdpJl7rHNOWU1M06d7WclV7938cgnWrORI6wrBHM5G8-pGgUDaEe-8bWH6M9w6d6nNtpnVIhcCGEl8ncPhHO1aIRmLrJqf0tBStKua5SuOWl0qOMIbaLKsYVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:
@News_Hut</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/news_hut/65101" target="_blank">📅 08:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65100">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">امروز ۶ خرداد عید قربونه
@News_Hut</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/news_hut/65100" target="_blank">📅 08:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65099">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CURjG-LT5h5hT8Yb60_qWe8xgxOam0nZG3r2mNp6EJUvbfJvZFGw1GMQl1YMOE7LmqsI2SGCB4M0fHa0WoboUB55h7R5tv3ZzvNTKmLodZxUSa2L1MWb_M5wf4I0n01KDvvWH_STDj9v7Vq6f_TkJVHsjQPVSdhlxm-7TpFKNvCbE1HXudwG3gkE-ivshJfsLmpeR45CbWGzm8KkbPALbJMx9ZQhcCruCdtRPFb7ZF89ceuqW_QF-pVyGO3XbcslfQwKGKXYWBhZf4koRf8E1Jqan4pvLvi48iiuRalVfmMxOnHMyiTO5Tu07BSP2fFM7lsNIkVSxoqCrsHf4yBg7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه ها پارمیدا دیگه بعدش آنلاین نشده
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/news_hut/65099" target="_blank">📅 08:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65098">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اولین صبحِ اتصال اینترنت بخیر جوون ایرانی
🫂
#hjAly</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65098" target="_blank">📅 08:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65097">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">جالبه یه یارو مثلا نورالدین الدغیر خبرنگار الجزیره تو تهران میاد توئیت میزنه همچی تموم شده و فقط امضا بین دوطرف مونده
خبرگزاری داخلی و وابسته به حکومت همینو بعنوان خبر میزنه ینی شما بیصاب شده‌ها به منبع ندارین خودتون؟
@News_Hut</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/news_hut/65097" target="_blank">📅 03:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65096">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zs09sJhmxkAkyrFfbmC0hKS3XkqRQ17aVJcJUV9IGv0hEVkGLEO1vI7fY7gqY_34WkfvMrDxDOreDUvDvqv3oEqh5nF_le9Lm4tmRI54TdJeCwOMVRC1LkSBhk5g-8Jfxn2m_RSaAAR42vNt1-CJXsEeiW0o0umLSqcTfvPpN4yCPCQM7Kn2kBFUqP4rsW7pqyawnWnS4MMQ2-xoYDEovA_NT-AVxFas_n7xN6JSJcaJQ364e8YaCLHnOR9zVv1_ftu7VxQnvAPBKnYXUCPHPF0XZztDJVj9721PdcNwnztqY_F5lpJvYfPit_B_b3zgSlxIfx9flLLQD3HTCPUl3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:  «اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم»…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/news_hut/65096" target="_blank">📅 23:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65095">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اتاق اصناف: از این به بعد فروش سیگار نخی ممنوعه
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65095" target="_blank">📅 22:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65094">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gm0eDxgZZihT6NCiWm9N7M4G30Y2jwZkd2X_4FwqSmop1GMGaWBpYgxzWmyYGUWOInJgNwCgMI20aptdRoNk0nsSs36wP1136Hq_vd2Vf8STEbgQhFXyYTXu5okrO2wxE8eVkiZ8L9ZJWLQRu84tUwxV45uVurunYusBGjPCXity_bl7Kfa453lKRCaZ7qyGLuudUgkcMM8wiHq7wxiyv9atWrhuAaILPcpM-8N0s_U0c9C7K8uDqL7v7nfzoxJ5XSQFhPUBl3FUgxRATCtqoiDTZnyN4sonfL4XWxoILe09agaYduCRYL3x9i11KdPth_VFpV7odThwLTn7Tq1mog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: همین الان معاینه 6 ماهه‌ام تموم شد، همه‌چیز کاملا عالی بود از دکترها و کادر فوق‌العاده مرکز پزشکی نظامی والتر رید تشکر می‌کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65094" target="_blank">📅 22:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65089">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نت خونگی.npvt</div>
  <div class="tg-doc-extra">9.3 KB</div>
</div>
<a href="https://t.me/news_hut/65089" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
🚨
🚨
کانفیگ‌ها و سرور هایی که بصورت منطقی براتون وصله
،
در صورت عدم اتصال می‌تونید گوشیتون رو بزارید رو حالت هواپیما و بعدا امتحان کنید
.
🌐
‌ ‌
لینک دانلود NPV با نت ملی
🛒
‌ ‌
لینک دانلود مستقیم برنامه از گوگلپلی
🛒
‌ ‌
لینک دانلود مستقیم برای آیفون - 𝐍𝐩𝐯 𝐓𝐮𝐧𝐧𝐞𝐥
🚨
🚨
🚨
تعدادی از کانفیگ های V2RAY متصل منطقه‌ای؛ یکبار کلیک کنید همه رو کپی کنید.
vless://392c0d0a-157f-4fe0-b528-11586477cbe0@185.213.165.81:38024?security=none&encryption=none&headerType=none&type=tcp#%40HutNewsPlus%20VPN
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.16.80.73:2096?path=%2F%3FTelegram%25F0%259F%2587%25A8%25F0%259F%258%D8%B97%25B3%2540WangCai2%3D&security=tls&encryption=none&insecure=1&host=sni.jpmj.dev&type=ws&allowInsecure=1&sni=sni.jpmj.dev#%40HutNewsPlus%20VPN
vless://e0a98968-eb18-417a-87e7-c8933aac5f13@31.59.40.53:52729?security=none&encryption=none&headerType=none&type=tcp#%40HutNewsPlus%20VPN
🚨
🚨
🚨
پروکسی‌های متصل منطقه‌ای با نت مخابرات:
https://t.me/proxy?server=62.3.12.2&port=8444&secret=ee6f7a6f6e2e7275f22c5421fa893965
https://t.me/proxy?server=91.107.169.174&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=176.65.128.238&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=195.254.165.4&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=5.75.248.201&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=87.248.129.5&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
@HutNewsPlus</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65089" target="_blank">📅 22:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65088">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4eH_pKzTN15E2oVQ14QS6PrVv72ypkxL23OWjNr8ubl0walOZoNHAiavuAQk98n3UV14h-n10RYK7pPOMghL6_qUfJAszrCKHhBX35l4GHFICw9FVNST3A4opEQjybaheDO-jjX1Z2rSoC_fLug9xLNOVAkOhYJsKvKp5X4qqwKYyyIAEAU1dh4pOvJkWGlZreBLvBvgQE0FpkWJu3MyYArgZZWyezSx4a9WVOZ8ePw_JmNKO0QzmnIpuUwbRJD0oeXsydWrXLxXt15kFJkAnNrseXrR1wJaeGshBUElZX585EFptVJ7M27AYvcJ5mTY9-e5jd-HIaVBY2PJPjcLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد عوده، فرمانده ارشد حماس، توسط اسرائیل ترور شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65088" target="_blank">📅 22:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65087">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEsteghlalPage</strong></div>
<div class="tg-text">Barko VPN_v2.0.apk</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65087" target="_blank">📅 22:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65086">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEsteghlalPage</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.0.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/news_hut/65086" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🤖
فیلترشکن :
🟣
Barko Vpn
🟣
v2.0
(20260108)
🔹
🔹
🔹
🔹
🔹
🔹
🔹
📝
مشخصات :
🟡
بدون قطعی 100% پرسرعت
🟡
برای تمامی اینترنت‌ها
🟡
مناسب شبکه‌های اجتماعی
🟡
اتصال خودکار
🔹
🔹
🔹
🔹
🔹
🔹
🔹
✅
تست شده و متصل !</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65086" target="_blank">📅 22:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65085">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نت بلاکس: دسترسی به نت تو ایران به ۸۶ درصد رسید، اینترنت همچنان فیلتره ولی امکان دور زدنش فراهم شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65085" target="_blank">📅 21:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65084">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=ErakbDIgGyCr-RVO4x3IZJBPt1JcC5KQI2Is6MMdratvYQ-PeqcS6b2FExruDoBl3VkdVA7OZ1VhrCbEs5uJA75DFMwFO_5ggApGV6G9-37oDkfnInZRd0sDJ7LIQw5TxlvREke04ESXzmPTKyJzVk1phTinpCIhq3UpW9HC9mp4el7f6sEoT5RDXKBEWpMuDc_e6s7tr_fKdNdVoJ6gIPBG0UV0mc0AZfNI3EtOPILQgBkZ7JCkQmZk0nPKwdiFUJ713TlWTAWSWsQHSoRSs4n-go7yao3F5TddEjwvqa7vrH4eKowwdZnbP2tG0KKpLx7ynlxkt0unDVpLHQLM-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=ErakbDIgGyCr-RVO4x3IZJBPt1JcC5KQI2Is6MMdratvYQ-PeqcS6b2FExruDoBl3VkdVA7OZ1VhrCbEs5uJA75DFMwFO_5ggApGV6G9-37oDkfnInZRd0sDJ7LIQw5TxlvREke04ESXzmPTKyJzVk1phTinpCIhq3UpW9HC9mp4el7f6sEoT5RDXKBEWpMuDc_e6s7tr_fKdNdVoJ6gIPBG0UV0mc0AZfNI3EtOPILQgBkZ7JCkQmZk0nPKwdiFUJ713TlWTAWSWsQHSoRSs4n-go7yao3F5TddEjwvqa7vrH4eKowwdZnbP2tG0KKpLx7ynlxkt0unDVpLHQLM-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کم‌کم تمامی vpn های رایگان دارند وصل می‌شن  @News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65084" target="_blank">📅 17:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65083">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFudo.</strong></div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/65083" target="_blank">📅 17:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65082">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کم‌کم تمامی vpn های رایگان دارند وصل می‌شن
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65082" target="_blank">📅 17:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65081">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMKPX</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8phP03lmJ_7fqgxmEwj82vOjLCrYlJtprJi5uu0qDA5DzuwcX2Sy8Lhz8WC-uq2ldhS9XIHZjHil_-NQJfNliX6GoEg2VGLnXoJLtL6uojJbowcZXMj8XrFxNrHzvEz-vjsBiZybHY5bqyQtIc5hLeHW3UgfsZvcaWjoP24WYQME-ltwvMoHGbJHVAktOeotCMDsjy16IK6lVRPQ-OhV4Tr5Dde5NFmhRQIvHVwzolrEd4Oe-gAA_0uWkJTwgZtoF23kDADMnQVjWIlmgELAOpwkuyJdD7M6k8_guYiRotf0dR10qIqM72OWkV_oVjt62tz4JzfCdFUAE1nYNisiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65081" target="_blank">📅 17:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65080">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMmdi</strong></div>
<div class="tg-text">درود
کسانی که نت مودم دارن میتونن با jump jump به اینترنت وصل بشن
ما هم بعد از سه ماه قطعی به جهان برگشیتم
بر باعث و بانیش لعنت
به امید آزادی ایران جونمون
❤️</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65080" target="_blank">📅 17:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65079">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.  @News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65079" target="_blank">📅 17:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65078">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqXGVd52CR3PL8DpKOFwRiEN2k4HhvZTylyfKUbBxLqOXdPYBN0SE7GQlie5cqg-1vaGVbDYzkgcZykukvEpsm0qVEdASOjgknuuIR6hgE6qBHexPRyPjAeX_WSuj9iHnTg_L4AXfB0hr2LycjMtFDLXUEmth0Yfy-MYrDShDTwBWKxTqQPuT7CILngojsiYrxV56urlseg6XiRShY6f9FWYt1H04HARKVw6uQzKKKNerUnYcZAET-N_213nNwFrN-jNXXO8PN9XmF_8BSM1xX3zeo-cauxwAaR2AM52jhKWylAWO5YIzW4VbehRhXJB4wD7Z4GTeCGRFaINnx8t2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65078" target="_blank">📅 17:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65077">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‼️
خبرگزاری انتخاب: ۴ شاکی حقیقی رفتن شکایت کردن و با دستور لغو مصوبه بازگشایی نت باعث توقف اتصال مردم به اینترنت بین‌الملل شدن.   این چهار حروم‌لقمه عبارتند از: رضا تقی پور، نماینده مجلس کامیار ثقفی، هیات علمی دانشگاه شهد و عضو شورای عالی فضای مجازی رسول جلیلی،…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65077" target="_blank">📅 14:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65076">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eb3w6lKmjpZb9aZZGUfoNvotlANFx3P_fQznid_5jYFgK_oH6AHh2A8Bx2S6IrgEhPP_LHjDWoUcMk1HbQUsNfiPtE-nY9dAJaQYq9mvzXLAPWycd_J-kuELh-lymogMyZgr2eZfG-Itktc4XdWOVyaDo-K4Ot7LAP2dkRKeTn6qVG8ikkqJ8M4JHQHv0cT6QyyNmcbnThIUoFbNIcJnN8Gn8Ao8vnjanR9TZ6O5zSRIssO570oCVKTxertKSh2qmbbZWxVhd50Jt2BktMw7FWDQx4lpr0wHL8Ke6ZOVS7EiNah0DBZyqxk0AaB0_3UlxxiUmlvRS5eAoIMt237KJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری انتخاب: ۴ شاکی حقیقی رفتن شکایت کردن و با دستور لغو مصوبه بازگشایی نت باعث توقف اتصال مردم به اینترنت بین‌الملل شدن.
این چهار حروم‌لقمه عبارتند از:
رضا تقی پور، نماینده مجلس
کامیار ثقفی، هیات علمی دانشگاه شهد و عضو شورای عالی فضای مجازی
رسول جلیلی، برادر سعید جلیلی و عضو شورای عالی فضای مجازی
محمد حسن انتظاری، عضو شورای عالی فضای مجازی
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65076" target="_blank">📅 14:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65075">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سخنگو دولت: بازگشایی اینترنت توسط پزشکیان به وزارت ارتباطات ابلاغ شد و امیدواریم تو روزهای آینده باز بشه  @News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65075" target="_blank">📅 13:56 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
