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
<img src="https://cdn4.telesco.pe/file/R40UbZuKXA7oHquC-G2mIX8M-XVY2G5K45mKiYWzmyM7Y8IC8aF2lKcOZKgPfQOhstpgzVBR84thxhnEadibitDgChbtUtpP0y7kzdVPWLkNL4pbosr9P5SN00hk0GFDiztVgAXU9SFR3MIM4wb8CwxTMKTnSbvWD4YfpxVIf5NU52RKCNZAYm46QpU9uTRmQn9AL6naKhUbevfmlH6QOUphOr-ChHMXJIPZPsOt5mL8yja3Isj8jFPcjw5FaIOPJrXqjqKeUX2qVogNzpFGSinYqLAe52_VYS7NoXiGTMcPsX_lP4g4se35PFVZL01yXA7KHth-kSkokaNx0LMZtA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 179K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 19:01:30</div>
<hr>

<div class="tg-post" id="msg-67911">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
حمله موشکی ایران به موقعیت یگان موشکی نیرو زمینی ارتش آمریکا در کویت.
گفته می‌شود این یگان در حمله دیشب به جنوب ایران حضور گسترده داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/news_hut/67911" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67910">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb024df7a1.mp4?token=MeXz-Fm3CgYdUtEXS650SDsZZg68F857XRiKZoO5iF4k-mMDKmMexXfU3XEte1jS61LNRK2BOkAacizpdboB40yKJ2e0XD2BJyuw73VoHxNkSkyhdEciDtOntHglZRq8bzzGUFuLhftc75Aqub5iqXq_Cji1W07npL4ygEdxZiDLDQqEplijhTS4UHR6yjkEoeQmKOjVfTawUgfdbQmJtycNC7G8NDZ6WVaFO6pDheNZllsT1xtGy5TUXMZc2-2oDR-8G_9iRvA3N3oCTMsR1_V-OXyHBt0nC3YZZhJvdd06tpA9VADCCUyMtWMg2HOtA8HYt7qHkVZm9TJqTZfL4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb024df7a1.mp4?token=MeXz-Fm3CgYdUtEXS650SDsZZg68F857XRiKZoO5iF4k-mMDKmMexXfU3XEte1jS61LNRK2BOkAacizpdboB40yKJ2e0XD2BJyuw73VoHxNkSkyhdEciDtOntHglZRq8bzzGUFuLhftc75Aqub5iqXq_Cji1W07npL4ygEdxZiDLDQqEplijhTS4UHR6yjkEoeQmKOjVfTawUgfdbQmJtycNC7G8NDZ6WVaFO6pDheNZllsT1xtGy5TUXMZc2-2oDR-8G_9iRvA3N3oCTMsR1_V-OXyHBt0nC3YZZhJvdd06tpA9VADCCUyMtWMg2HOtA8HYt7qHkVZm9TJqTZfL4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کویت کمی قبل
@News_Hut</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/news_hut/67910" target="_blank">📅 18:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67909">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAHQHJve8eiPrwKc7YI1gtctGefso7dw2saA1BWC-JZqIy1a23SBFC7ZIxjWGRqwDN0YAAmNzq41jsnv0vBctwH2fa40_fWmefiQur3u8PiBUQ70XTa1XnGLKpSdxREeUOTSgl1akJ4YqLAGnD_TZ8kC_SqT_r19kqFW4KFmlKgzc5O-DBYc9F2Z4PQ5fUC4hj-YvrGWChHbtSpGs04f37emRecSVEXwYdMR8VV0c4cplOqCn7qGYumJi07fPFVCEAKke4SPLze8wKx_uaF921iKkAp0mc4kTE3Whnno2-ObT3bxZCjEPuH1SypCAplk_4J7KspSjvK4PGfFiPEl5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دو انفجار در کویت و برخواستن ستون دود
@News_Hut</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/news_hut/67909" target="_blank">📅 18:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67908">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09b038fd4d.mp4?token=ge2YwuTE_XX4zb7Pf91ot3nKHyMY_mbJJeOCBm1rYjvh-Vi7M_MXs3VnYGQ4pgkhPfv6lT3bsIun91CscyWrBB4vzxWAEJQpm1kJnKrHlFMZyed7BjqGaYu_TTlFhhYxlNyZdaE5Ii5eZzfRaeuhMa5IWFCuSLDrzvLPx73wQl4hKeBR2WB7T6iqoxxxaI15GCPHfaQ4J8SNJSbKXtSq_6gs0-usOfACfwhXCJrr0BVoLJRIKNeIDb0e4LGthF7WgA6paO4E-13SeMJm06-YXyJMNzE1aPwAT8550b94yU2We6VAbMKR983QaeEpbnYpfdnw4O-OaOODlSAdDud97w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09b038fd4d.mp4?token=ge2YwuTE_XX4zb7Pf91ot3nKHyMY_mbJJeOCBm1rYjvh-Vi7M_MXs3VnYGQ4pgkhPfv6lT3bsIun91CscyWrBB4vzxWAEJQpm1kJnKrHlFMZyed7BjqGaYu_TTlFhhYxlNyZdaE5Ii5eZzfRaeuhMa5IWFCuSLDrzvLPx73wQl4hKeBR2WB7T6iqoxxxaI15GCPHfaQ4J8SNJSbKXtSq_6gs0-usOfACfwhXCJrr0BVoLJRIKNeIDb0e4LGthF7WgA6paO4E-13SeMJm06-YXyJMNzE1aPwAT8550b94yU2We6VAbMKR983QaeEpbnYpfdnw4O-OaOODlSAdDud97w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پرزیدنت ترامپ:
ما آخرین جلسه را با آنها داشتیم، آنها دیروز با یک توافق موافقت کردند، یک توافق عالی برای ما. نه هسته ای، نه این، نه آن، نه هیچ چیز. آنها همه چیز را رها کردند.
و بعد از آن اتاق را ترک کردند. و سپس در عرض یک ساعت یک پهپاد و یک کشتی را به آب انداختند.
گفتم شما افراد مریض هستید. شما افرادی مریض هستید
.
@News_Hut</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/news_hut/67908" target="_blank">📅 18:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67907">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550c5fbdb2.mp4?token=bkRrmFUrsEOYGYcHuE27V7mu_XKvi6St7TiJzMFGeFQPAMXjQWHdwSFA67KIb_AMfUuTXQpJlFElgnPzBXB-Yf1Tm6ZjwBezPM1YgXoomjummNOHkMHhSNARWHQQ8_fKD6C0gxx9HOLa8sEk8uDhMHHDugdGYvOiL_MzxXoD1d0aSULBv7qC-wta-znXli5mZq9N3zphS1VTVUR8OnLgQak66W_AbK2XOuqFBXmywB5l4I8XIams4fKhGEOLNuwu7-3QUmzdGEvhreXsILy6xwfG1_QOgVqMkGlq6XOLOt17vewLjzRmGw8r3sV60qNVcP2J2IpA0Vj4V5N2M8LILJVbCDkgMHwJEhkqCwY2ibWVknrNI3ynRSAwwbI3JUX9L6afyWcMGydNVGdt9IrtWJ7Ze6L_p430oynbsxrtGWpDsNcvdtDq-ry1BJjrQ5kro79mhTJF5Wl4PtZQsJvDs-DW8-NgJPSILp2iE-iRJEuRUvP55V9IB7eF3G0uHiLc29scM2QbhqzqKjvNX-m4BaKFIM_KRwN50xuRJW6530VWlTETs-7Xi_0UT68cCenR5KAfENWeVn8j29FHmVsyjDFTi60Q1p0kZSlvfcOKUJ2_IJYDhkTuuEmfpEqEXpZs69HEfPGVFUlRMHaDDeYXxFQ0pFps4qQ3oie6JksLWmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550c5fbdb2.mp4?token=bkRrmFUrsEOYGYcHuE27V7mu_XKvi6St7TiJzMFGeFQPAMXjQWHdwSFA67KIb_AMfUuTXQpJlFElgnPzBXB-Yf1Tm6ZjwBezPM1YgXoomjummNOHkMHhSNARWHQQ8_fKD6C0gxx9HOLa8sEk8uDhMHHDugdGYvOiL_MzxXoD1d0aSULBv7qC-wta-znXli5mZq9N3zphS1VTVUR8OnLgQak66W_AbK2XOuqFBXmywB5l4I8XIams4fKhGEOLNuwu7-3QUmzdGEvhreXsILy6xwfG1_QOgVqMkGlq6XOLOt17vewLjzRmGw8r3sV60qNVcP2J2IpA0Vj4V5N2M8LILJVbCDkgMHwJEhkqCwY2ibWVknrNI3ynRSAwwbI3JUX9L6afyWcMGydNVGdt9IrtWJ7Ze6L_p430oynbsxrtGWpDsNcvdtDq-ry1BJjrQ5kro79mhTJF5Wl4PtZQsJvDs-DW8-NgJPSILp2iE-iRJEuRUvP55V9IB7eF3G0uHiLc29scM2QbhqzqKjvNX-m4BaKFIM_KRwN50xuRJW6530VWlTETs-7Xi_0UT68cCenR5KAfENWeVn8j29FHmVsyjDFTi60Q1p0kZSlvfcOKUJ2_IJYDhkTuuEmfpEqEXpZs69HEfPGVFUlRMHaDDeYXxFQ0pFps4qQ3oie6JksLWmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
و شما بدیهی است که یک شبه دور جدیدی از حملات را آغاز کردید. ایران یک شبه گفت تنگه هرمز بسته است.
سنتکام امروز صبح بیرون آمد و گفت تنگه هرمز باز است. کدام است، آقای رئیس جمهور، و چگونه می خواهید پاسخ دهید؟»
🔴
ترامپ:
"این باز است، و من نمی خواهم در مورد آن صحبت کنم زیرا می خواهم زندگی لیندسی گراهام را گرامی بدارم، بنابراین نمی خواهم در مورد آن صحبت کنم. قبل از تماس به شما گفتم.
آره بازه ما دیشب آنها را بمباران کردیم. آنها افراد بسیار بسیار شرور و بیمار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/news_hut/67907" target="_blank">📅 18:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67906">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‼️
یک فایل پنج‌ساعته از مکالمات بی‌سیم نیروهای سرکوب‌گر در اصفهان به ایران اینترنشنال رسیده که نشان می‌دهد نیروی انتظامی با مجوز استفاده از سلاح جنگی، در ۱۸ و ۱۹ دی‌ماه با کلاشنیکف و وینچستر به معترضان شلیک کردند.
دقایقی از مکالمات نیروهای انتظامی در بی‌سیم را در این ویدیو بشنوید.
@News_Hut</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/news_hut/67906" target="_blank">📅 18:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67905">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f43409a1c.mp4?token=osHH0o5DQ9Vb3pazSjjxaB9oOKa2Peilp1Y7yO39h9ipmLcai_0_yY8UN5h4XoDx0X10eyeq2omw9LXI5oT2jyah-bZGCp8csp4GGeL7VGETO77vgOwNR1LXeMfR0CuQsAWENwpySrhm8uwCNCQDJnpRsH6UzBZxmQLE8KH9OmmD2LDwyjFPmANjOWYUqFF_QjvyfE95pDGIt65r7QkjOukTQWAIEpN0uNOokK3arjhG9GW2PxD1x779BAS7EUBCip_ZzNpCyDC3qADcSj0IdcGq8vpknSldiEne8TepkKn58Nz9KOMPcqvnEANYNz1cPQp_-Ps8cXww1bfVMlN0LSSpLGQg_SOmOlu5rpMU0JXri8zdSXKNVQvcK2NtuvMCEbSsqPLQcyvkzGy4Uyj96tknmQNq324ACbwwTi0FoIWir3XcYWmdQ3ysCs5z_WM6bM26Z148NfPhi6h4vSq7xe2OcCbdTYfgn8Oesd_PlCiFFz0BzlvYm-4-QKQQgp8gqBFB8jDUOd97kfd5ah9RMdI2a6-HAAZq9gGGcyg1ANXqHJkTMbo0Ctl9FGH2PMRr7CW7rA79YHbiteCv0dfonBeCl1KBz1A6Zkab4O1JRvGx9wFFqPKB7x7rAsNrJPcaCcDo1W6X_CAK8ndcA2j9MHjbLOg80D4MpYQzMiaOqyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f43409a1c.mp4?token=osHH0o5DQ9Vb3pazSjjxaB9oOKa2Peilp1Y7yO39h9ipmLcai_0_yY8UN5h4XoDx0X10eyeq2omw9LXI5oT2jyah-bZGCp8csp4GGeL7VGETO77vgOwNR1LXeMfR0CuQsAWENwpySrhm8uwCNCQDJnpRsH6UzBZxmQLE8KH9OmmD2LDwyjFPmANjOWYUqFF_QjvyfE95pDGIt65r7QkjOukTQWAIEpN0uNOokK3arjhG9GW2PxD1x779BAS7EUBCip_ZzNpCyDC3qADcSj0IdcGq8vpknSldiEne8TepkKn58Nz9KOMPcqvnEANYNz1cPQp_-Ps8cXww1bfVMlN0LSSpLGQg_SOmOlu5rpMU0JXri8zdSXKNVQvcK2NtuvMCEbSsqPLQcyvkzGy4Uyj96tknmQNq324ACbwwTi0FoIWir3XcYWmdQ3ysCs5z_WM6bM26Z148NfPhi6h4vSq7xe2OcCbdTYfgn8Oesd_PlCiFFz0BzlvYm-4-QKQQgp8gqBFB8jDUOd97kfd5ah9RMdI2a6-HAAZq9gGGcyg1ANXqHJkTMbo0Ctl9FGH2PMRr7CW7rA79YHbiteCv0dfonBeCl1KBz1A6Zkab4O1JRvGx9wFFqPKB7x7rAsNrJPcaCcDo1W6X_CAK8ndcA2j9MHjbLOg80D4MpYQzMiaOqyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از  فعالیت موشک‌های رهگیر پاتریوت بر علیه موشک‌های ایرانی در پایگاه موفق السلطی اردن از دید سرباز آمریکایی طی درگیری‌های روز‌های اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/67905" target="_blank">📅 17:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67904">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=TuxnvlKbLE_WVYhEKZXoqvufc9mgd3O8m2nx_tvnAnaV_HOI5Ej3xrdB699NPTyi3erwx1GjFJfkD2G5IGP4JtWgVhSGK36F5XPxtNfHKXOlsd9pMWA0K55yuntzqXi3HgmFuF_Anix5TF6yVIo4nARnK-DPVTNm21-QZr3Avyfdwd5es9vrHGRfTuu3HschQLFT0zkJHwwEXXvua5ZbQ_mxA-eedtwpBlOK_AwnHZrRZljj1_z4CgUcArADCileKruBB7Ib3NxKjcBSQzok0ODH83SmkRl350NscAwidza7QhlcasG4dyB_WV7sxiUwwlDxJwG1OJm1m4lRwDhqJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=TuxnvlKbLE_WVYhEKZXoqvufc9mgd3O8m2nx_tvnAnaV_HOI5Ej3xrdB699NPTyi3erwx1GjFJfkD2G5IGP4JtWgVhSGK36F5XPxtNfHKXOlsd9pMWA0K55yuntzqXi3HgmFuF_Anix5TF6yVIo4nARnK-DPVTNm21-QZr3Avyfdwd5es9vrHGRfTuu3HschQLFT0zkJHwwEXXvua5ZbQ_mxA-eedtwpBlOK_AwnHZrRZljj1_z4CgUcArADCileKruBB7Ib3NxKjcBSQzok0ODH83SmkRl350NscAwidza7QhlcasG4dyB_WV7sxiUwwlDxJwG1OJm1m4lRwDhqJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب شدن سرباز بر اثر انفجار اشتباهی در تمرین پدافند هوایی روسیه(نزدیک بود همرزمش رو هم بگا بده)
👅
👅
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/67904" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67903">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdilalHrhKLhH7bidO7-k_5VSdW3re6k2CijH1dCl60pTqvMDPcfslW1wB7f5nkPDvkuaLLIf24JYRxRxo4rylUr3JPhw7YZPF5G8_55VKrDl_EX0tiVivun5cyokNcmufLVDvGFK2xvpHG6U86KZYksNENzXG9vAiT_CjEGW4o5_Nalrfx0uLa2LClFc7656qc5RPK3crpFW6XK_NY3e7K6FjEu5ScbnHlXo52tU8tZxlyN4eSaKPTGStdauU242cj3mIl0RvPuPN92izihEO8rOcHHC2zsNs6Mqh3hZVUfC_IfT4C6fElf3kNQXg1BSFFn4Zq_PXBIw8f8xJiZxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
تنگه هرمز برای تمامی کشتی‌هایی که قصد عبور قانونی از این آبراه بین‌المللی را دارند، باز است. نیروهای آمریکایی در این منطقه مستقر هستند و آماده‌اند تا از آزادی تردد دریایی اطمینان حاصل کنند، علی‌رغم اقدامات تهاجمی، آزار و اذیت، تهدیدها و اظهارات غیرمنطقی ایران. ایران کنترل این تنگه را بر عهده ندارد. ترددها به روال عادی خود ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/67903" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67901">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyeUt8Lzx7vLhRvpyLWmIqz9VkvEJDFZvX-84Rn2415lpSwoOANAxxlgUa3QzaMIlL47pS4bJPbRmuxZDpVozLCemRRltpoD5ZcH0p8tsFUapey_FzTEhitkMw7jf6McRLjkEp-dxSln5UhDbQ3k5AQWZiFDodsqo7Rlf8rDLYgZ7nxgtUAPV24n1HRdrP4lmThGMn98CMfMY3z964USVbjXy8pbhE-yJ6l0p71OxWhhNNtzWAqMUX4fRZU5aPVv-aGmh-NzBR9hLiUjrCoFFtfsVGHWJL9QbdIQGll6GgC5tQB6clpZZKAVovQbfZINpSnRZW52drrGN5cMaMGDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa15fb6f3.mp4?token=bbWN_PnA3EgZCCOddGwDOObZLgqk-x9uuhdexS2LGuazOOMdt7S0bM3Hob_eNj6j7TYpV3xAfSaQICfXN4iaCljzavv7jTNHEYYYSLuPU4M076q4pl11nKZ4KT_dr8Kok4yvM1QElAY38DeYW_Uusqi8dBMeAu3hAzIzclDRthog6XfFj7aYkSBGW4qZY2tjKW9iJ1DOjxKLiH09JPG7pwu6S8copQSeyVe9gUZzQWsNazxGo_JdWgg-EuJlKPPfMAysWB-AFhHynCs-4tZ6iVyW77P2-oB-Fw09XYY9MMB67TSSpS-TL4ayGriIilcB2dkJBj5RmxvK6x3NnrtrYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa15fb6f3.mp4?token=bbWN_PnA3EgZCCOddGwDOObZLgqk-x9uuhdexS2LGuazOOMdt7S0bM3Hob_eNj6j7TYpV3xAfSaQICfXN4iaCljzavv7jTNHEYYYSLuPU4M076q4pl11nKZ4KT_dr8Kok4yvM1QElAY38DeYW_Uusqi8dBMeAu3hAzIzclDRthog6XfFj7aYkSBGW4qZY2tjKW9iJ1DOjxKLiH09JPG7pwu6S8copQSeyVe9gUZzQWsNazxGo_JdWgg-EuJlKPPfMAysWB-AFhHynCs-4tZ6iVyW77P2-oB-Fw09XYY9MMB67TSSpS-TL4ayGriIilcB2dkJBj5RmxvK6x3NnrtrYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از اینکه صداسیما رسما مرگ لیندزی گراهام رو تبریک گفت
فیلم تبریکش بشدت در رسانه های جهانی وایرال شده و گویا برخی دنبال ربط دادن مرگش به جمهوری اسلامی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67901" target="_blank">📅 15:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67900">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFdw40W9grpatxFeJ7v_7Wm4wGAld8aIG6kV-8KWs1a2BJpaUqK_YS78QTRkmB9esGrCVTJDioEQNDivKj5urfomolVVx8LG3MEPq0dMlVL0JjriegcWL6uWnp1xJnvUChuKd5Ag6nlnI35unLcw5tGyRFmSZ1NbFhBqs8KkAk6AkY0Ffe_7d4N5I6YOH_P13-5dm0wuy56nMAyTFeh0bDErsvALsMXvaGwR60k0Ci2YzMeBHiYwkrSe8l6V87Cl9I9SgP7pTyvox3fq-aNx9USMIRR20VsbzO0AhGRrAOSyI7FPsunkjhPb_JK1fqbmKzODWLw-UTQBabT4PnpIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پس از شلیک چندین موشک بالستیک به کشور قطر در طول شب گذشته، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، ضمن ابراز همدردی صمیمانه، به خانواده و مردم قطر تسلیت گفت و مراتب تسلیت خود را به مناسبت درگذشت امیر سابق قطر اعلام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67900" target="_blank">📅 15:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67899">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f465c542d7.mp4?token=FY_kaN2JVs_ibE1RSt4Y7Sy12qJfj-sp5ZlS4NRiKXJZCg-q_ugEO3scJP0ZmNHLmbqtQNfn25UJuTAFZw9l-E_i6p0kVO2xIG7_M_UhOqC0I_IDM-zkTKF9_RHT2pM_9XcKt-HSb368-eh-kebT0Zf8PGFBgE-I5bBRLi33_39ts53zae75kBpCy3Jvd-h8BvCoqk43evMnQ3mSa0jRGOYR-sWACETwcTnCnDyDF27tb5XH5mWR2MraIUyvOEbRNHVqdaMiTPr4zQ8RWJ67Id6Jpuq_tuhcx6hFEQnyHJ7gvgNdQgNPNSrKtBf5NbIGlSpwr6rol8eKfdtGjc7OAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f465c542d7.mp4?token=FY_kaN2JVs_ibE1RSt4Y7Sy12qJfj-sp5ZlS4NRiKXJZCg-q_ugEO3scJP0ZmNHLmbqtQNfn25UJuTAFZw9l-E_i6p0kVO2xIG7_M_UhOqC0I_IDM-zkTKF9_RHT2pM_9XcKt-HSb368-eh-kebT0Zf8PGFBgE-I5bBRLi33_39ts53zae75kBpCy3Jvd-h8BvCoqk43evMnQ3mSa0jRGOYR-sWACETwcTnCnDyDF27tb5XH5mWR2MraIUyvOEbRNHVqdaMiTPr4zQ8RWJ67Id6Jpuq_tuhcx6hFEQnyHJ7gvgNdQgNPNSrKtBf5NbIGlSpwr6rol8eKfdtGjc7OAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش ممد سامتینگ در حالی که تندرو ها دارن شعار
«مذاکره با دشمن خیانت است به میهن»
میدن در مراسم چالسپاری خامنه‌ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67899" target="_blank">📅 14:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67898">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
نتانیاهو در حال بررسی سفر به منظور شرکت در مراسم خاکسپاری لیندی گراهام است. احتمالاً ترامپ نیز در آنجا حضور خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67898" target="_blank">📅 13:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67897">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVFtAQ86MAylaXfE7xOaqQ3mHT6fOeoOEW2DM7IobdnCoVwfo-d93goVNcNkv2b-PCYCzzNWOha40_pn_Bqu8QAKblkDrF1Xw9wxIMfhDA8oOf85yxA5fOwc-xKoNZBC3NJrIbWqxwPWPWT7hADqt5GYcKNf021KJTkesZFqaV8pn3Okb_u_RwX8l2ol-N6XYm_V5d_UczPLFxrXYR4tBN5YMO3rKTySzd15pmIM8h2VoLUR9Q8QBD944DOINdGvKDvjJBftGTQnE3XKwpDvyidhi2riQOdGyKBcEvQQjvkznX6yC4bnNMO6fqgaHgvK3Z1O1jng-WkeMYJwROWf-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمیدرضا دهقان از اعضای پدافند ارتش در منطقه جاسک طی حمله بامداد امروز ارتش امریکا کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67897" target="_blank">📅 12:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67896">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvULATMieiLPn4GUZSNcv6Mc5K65DginSdhqU8Yk1YUM4ZpVxwm8W6KLY5_XSV--29MFEKc11Os2MQRGrKRrR3zyjXRA4-XhzLka-Vez6jVMIhmXR8dWcvkMDxJRsH3CPaL__QUxDw3R3fjpIq-GHgbfJ_HRhVYtBbyDPH3i4Mi4Qn4Eay4mlqb7G4IRo0k-TDiz4Hbzz6VczWwKqEJUfs7GNJRAxaEeFOM9IA1rz17u4Ov0j4CMPqZTjUQjBLAAjxCRybUrgk7yNgkGk7sfWSrQi3BncNq_uLnDeSV_rQKavPGsLMCXfApewE1tpLa7TChOWMiA-MAvmE2jLAem7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
واکنش مرندی عضو تیم مذاکره کننده به درگذشت سناتور لیندسی گراهام:
چقدر بد؛ من میخواستم او قبل از رفتن به جهنم قیمت بازار نفت را ببیند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67896" target="_blank">📅 12:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67895">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nF51OQyDSp1xoZijJUQBXccZOt-aQ_8tKQtdo1w47FLcLRc1pjREjqAc0qy7L6c28qLz9Ohng7wL59REulM201hrmJNfz08PNhQXCfqvVumC71iwq4Rc4uB6vEwiNCzClnsS_EjHPwl2KTKbbIAQ63ABgLXWCIZODW0L8rpe7dYvVYvTaANg3CG5_MLsOc93NNrN2Euqe0_Wj9CgOY5jCJVZw3hHk0IYDJ0JDH_8GtyUNn7ozqJLYjx_h9fiJwnE_8AytGcjIALjDgJL6CXBohhQjcAc1JwzW3idCcEvaVVYjrs5H32fjPhL93opd7Tz0nP-Vs40Uhwwp0h1pAsCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
👑
شاهزاده رضا پهلوی:
از درگذشت ناگهانی سناتور لیندزی گراهام، دوستی ثابت‌قدم برای مردم ایران و مدافعی سرافراز برای آزادی، عمیقاً اندوهگینم.
در لحظاتی که نیاز به موضع‌گیری اخلاقیِ صریح و درست بود، سناتور گراهام در جانب حق ایستاد. آنگاه که دوستانِ واقعی کمیاب بودند، او در مبارزه علیه استبداد، در کنار مردم ایران ایستاد.
او از صدای خود بهره گرفت تا اطمینان حاصل کند که صدای مبارزانِ راه عدالت در راهروهای قدرت شنیده می‌شود.
حمایت او از «انقلاب شیر و خورشید» ایران، لقب «عمو لیندزی» را در میان ایرانیان برایش به ارمغان آورد.
یاد او همواره با سپاس و احترامی عمیق گرامی داشته خواهد شد. ما مراتب تسلیت عمیق خود را به خانواده، عزیزان و همکاران سناتور گراهام، و همچنین به مردم کارولینای جنوبی و ایالات متحده ابراز می‌داریم.
روحش شاد و یادش گرامی باد؛ و باشد که دیگران راه مبارزه برای آزادی را ادامه دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67895" target="_blank">📅 11:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67894">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTcdl1PxT_ym1lUzYmLFKk0kM-KMwTNj5WQoSEFOQqfdMnacomg4QJ6cAiSetwUFIWpNdX7w2R1o6A9RNmaS85xntGpTQ8RzYOqdEn_srUMfZxeMELP8EhkhBL4tKEmrX1_di9X2x7aYDr0Xn5UEy0OyvhXkliO-_ZBkANw60685jn-6OYCgCiSTBniY44gl3UcAezoS_ncRxJJkfp7VRDqbmXUp8g5h6RtPaCdOfX4kQh-yd1boSZ2WcePN1BMEFu7lcjeCoKntzg61adCFIJlHrHqE34ezozxLdQHL_wvLCoTw6C_-a257I3pQpS9LO5AE7nbz0W1aL8G2GG_fvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو نخست وزیر اسرائیل در سوگ مرگ لیندسی گراهام:
من و سارا با مردم آمریکا به خاطر از دست دادن دوست عزیزمان، سناتور لیندزی گراهام، غمگین هستیم.
در ملاقات اخیرمان گفتم: "لیندسی دوست بزرگ اسرائیل و دوست عزیز من است. ما هیچ دوستی بهتر از لیندسی نداریم.
لیندزی فهمید که امنیت اسرائیل و آمریکا جدایی ناپذیر هستند. او زندگی خود را وقف دفاع از آمریکا، تقویت اتحاد ما و ایستادگی برای جهان آزاد کرد.
اسرائیل یکی از بزرگترین دوستان خود را از دست داده است. آمریکا یک میهن پرست بزرگ را از دست داده است. من یک دوست عزیز را از دست داده ام
.
قلب ما با خانواده لیندزی و با مردم آمریکا در این زمان سخت است. باشد که ارزش ها و ابتکارات او همچنان ما را به سوی پیروزی و صلح رهنمون سازد و یادش همیشه پر برکت باد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67894" target="_blank">📅 11:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67893">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5JO8oj6TiPXfxFXFBEuLvRR2Bsuy94cEGAXykRSA8cSSKRZgQIMLhJshrS3Q-oyEmr8H400ayLSp9v4tC7lGeCNC9Q0DVt_n-d-OIvTPIhv1zVGCLDQTiZrCIamQYMKZSOesEEg5C2msFvjd0KXB03mtXO-M6G0Jj9BX30NKyei9Mux2LHFV_Nqojlac9BvbgVQIN89ttbiVBYk6v-gWzQIeyB3-IyFQDVXUrAxOfQltC_2YAH4Zc9glqexmN9YwJnkWLYMQwlGujeQ3dg8Wkuh0-6qxMNGUsWJ3pEQb9KwS-F3WSv1kAXtpVCjl9bpeH56Ig-XFb5fkUYGDH0kdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ:
سناتور لیندی گراهام، یکی از بزرگترین شخصیت‌ها و سناتورهایی که تا به حال می‌شناختم، از دنیا رفت. او همیشه فعال بود و یک آمریکایی واقعی بود. ما لیندی را بسیار دلتنگ خواهیم شد. جزئیات و برنامه‌های مراسم تشییع پیکر او متعاقباً اعلام خواهد شد. چه خبر غم‌انگیزی!
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67893" target="_blank">📅 10:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67892">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDxQXll24mOFqniywF86zHqRxVkVRtLfGz6kh33rdtqOYUSN4kmNh2NkmZRKTrF8DTUISOULKLrca2BejnbnfV69vdDUqqyjNVn8NZOMjhPlOs0WW9gfhdQ0ajKovNPyRPDmQ02BCSVejSSRpx0PAYUX1E0uetnpZg8DMFetJAItkOVbGrSNeymMr4kfgmlHiVswpPch_7VDETiU_-S6ML10PN1g-iQCO2UKbISlb8cxk9Gnr3JxcxNrfVQz9n5FGPjr607dc6UQFeWCc6MhwmjNAHs2Tz-4nL3FhTE4S5XSUPgtbovAKvpbbNq-mCFKWJyGUKWB0amDAULUehCOWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ان‌بی‌سی‌ نیوز:
در حال بررسی صدای ضبط شده از بی‌سیم پلیس مربوط به واکنش نیروهای امدادی به یک مورد ایست قلبی در خانه لیندسی گراهام است.
این شبکه همچنین گزارش می‌دهد که عکس‌هایی از شخصی دریافت کرده است که به احتمال زیاد لیندسی گراهام است و او را روی برانکارد از خانه خارج میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67892" target="_blank">📅 10:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67891">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CB61_-4et-npGTWkU8NgnGhAPRZkL6pKlsoj619ZtOvrqSHNw449PhnBFTsWk4MFHyp0soElm2Cw6JWHJdzey3raaxY8UvF5QFU9kz4z-SGQevsjfgFWneJ2Opoyiy_66t0BbHYP6Av3S9F9l8ls5UuXd9A6E4qKy-q67dSyphukUokdJVt7XR8bdrIRndcnYBZrP71RhcILiBbEuN-j-p2xATpBlaJ1ft42EXMslMxTFk4RaX2XwvKReC4LP0OqILPXmJ8ZNTswX3ZfKWm9bVqIaJ4ydUD8n0fjXhb4WgYJLQhcL2BW8u-Si7X2sran_uJiYiliUySlxtQ7O-0EJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RIP, great man
🫡
🖤
#hjAly‌</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67891" target="_blank">📅 10:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67890">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHG_1B8n8RvtXkKBE7rWeTqDsRP47F56MLCmeLzAlNbXj6NZS05ytPJeYT0HNrpuwypBAS-IbtmUyOfWRs-66qyL-A12KAAQVmKNcS0daiDN6mPl1n1yIG4XpqWjyBcTWug5dcwclj7EvKv7jhagHTfdp8z9oK_BllCFS1VU-W_vDMpBd5bODeBj2Ae80OPzfJn6RQItkAzdTSpCbkcSBbo4ye8piJ9pIAjDUtJPS5C5Fkt-1t5HiRKpHviNSYR1kh2WH8555W2PbdPjFz5EknO3F30i5AFwobZi96Gk71-rSzezGNVRUL_Ej-66qO3FifJOWvbP_o2859JOnMwvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
بیانیه دفتر سناتور لیندسی گراهام:   دفتر لیندزی گراهام، سناتور ارشد جمهوری‌خواه، اعلام کرد که او شامگاه شنبه پس از یک بیماری کوتاه و ناگهانی درگذشت.  @News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67890" target="_blank">📅 09:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67889">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJTJxusanixgKxANJOn2Z8UqavpcDW4MrKxUrX_2sIeDHRr-KJATF76LAnp7DM0ntAzU62wbf3G7JBgZMaGsnu-qODMXxfbD9gNghxP40zC8Nqd3Zx413lHp7B76yfILIzJKi6grFO8_Z1dn7Jx_fYGvvwfYdf-xa1Cr-aibGDmHJLBRsTnXoCtBLCQ46d4HyAwIgo_XCdWtRyiUXmfWQUdmtHaUT_W10JgPOcpLdO2Fq7n3aPD0iUXC62rs5GLfqn661mp5sXJrLV8Xpdp2s2X_phA_Xa59-F7L7ooGBoWNWcJUlMcamLX37nVgwqQXSnLGQiNuODckzPyyzDwBBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
بیانیه دفتر سناتور لیندسی گراهام:
دفتر لیندزی گراهام، سناتور ارشد جمهوری‌خواه، اعلام کرد که او شامگاه شنبه پس از یک بیماری کوتاه و ناگهانی درگذشت
.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67889" target="_blank">📅 09:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67887">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVMjXNhhi-NHuR80GLac8HYbXdzZy4spU5MQTiUwUyeX_wzM8lpYXw7V_WS5BWkBnrLyiIRPkIFujiU17WCa8otAUCUWP4foQIhTbtqoN39ihmQHmFMEBXvj_6Mi4683ivFY6ajKGk1mNtPs23iThd1Ozfg14VpgLcdG2H1VTjFQon8e0u2lhsQoDPAIkg21KLl1QzEuYXTMABJTr_cD1vhkV_x39k3oCpX_OS-3QyRMhnqLCqd5EfO-0j_mvVMvM8BF3_tC31EDdYmRdzQ6GEoouxrx7NF8opaxbJOTG7pLL9lP076KeiQEqYyIzyYO2NioMsX5VkWLRpN_pBVxRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
#فوری
؛
لیندسی گراهام سناتور جمهوری‌خواه آمریکایی و از حامیان انقلاب شیر و خورشید درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67887" target="_blank">📅 09:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67886">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
تصاویری که سپاه از حمله به پایگاه های آمریکایی در منطقه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67886" target="_blank">📅 09:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67885">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=AHAG5g2pJwwfcSRYzYvdvxbPDeusJAvZwJTWau0Wir2Q2VxNwG4S3pYe5i8bcSPkqBeg8avnIuDEa7VbHvypthz817HOyQDBGZYmTTMj9dnMHpfqLfQ2066r4jBFOMqUZtW58dNP9J9K2HsA5I3W9ZebrPBFNxQOS-Shs8DVhRwWoqzUrnZ-h6h4oXnFzNlOwpnnOs90MGeeZWgH1WGcTuETNiheyG9wsj18ACj2PGDZRQzM7bHJxIIBFU4SpIbnyzFB_y5N5Pk7eWmstYmV9drN1wwVJLPzj6RdaYqMFBXqt45p7ehvkeeq60Lr1DhImtpj-3FCmfCgNJdnZaMAxYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=AHAG5g2pJwwfcSRYzYvdvxbPDeusJAvZwJTWau0Wir2Q2VxNwG4S3pYe5i8bcSPkqBeg8avnIuDEa7VbHvypthz817HOyQDBGZYmTTMj9dnMHpfqLfQ2066r4jBFOMqUZtW58dNP9J9K2HsA5I3W9ZebrPBFNxQOS-Shs8DVhRwWoqzUrnZ-h6h4oXnFzNlOwpnnOs90MGeeZWgH1WGcTuETNiheyG9wsj18ACj2PGDZRQzM7bHJxIIBFU4SpIbnyzFB_y5N5Pk7eWmstYmV9drN1wwVJLPzj6RdaYqMFBXqt45p7ehvkeeq60Lr1DhImtpj-3FCmfCgNJdnZaMAxYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سرباز روس خودشو به موش مردگی زده تا کوادکوپتر اوکراینی شکارش نکنه
اپراتور اوکراینی میگه: «نگاه کن لعنتی طوری نقش بازی میکنه که دی کاپریو جلوش کم میاره»
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67885" target="_blank">📅 09:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67884">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spRZpgH3M9a4ZXIVqVTy5elMjS8yRS4ruoiITPZAJ0nKZagDJRD7PtiFNVkRG06VsogLAulSaYAU1md3gflyrkPzpmnBLuMGXC00GscUSkUXrP1juVhjK5sVnz_aKOQJQKqga8avcIGJg80_upJeNEbXlt1t3XqBXx2qz6exlnfZkkIxKn_v6OZrmPRuJQ6w-WRhB5hwQYvTMss9cvGnZln7n_1MWA6_IIgZW0LW1Pm4TiTuk209SI_Q7qDEoc0DEx2hMjLCVmiCmxTFLop7_f17hTl-7TP9drnG9Kccoqv2N7-AQJez2aomHrR4LNHJjly3iSq0TvN4LzdkXr3w6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
قاليباف: دوران معاملات یک‌طرفه به پایان رسیده است. به شما گفته‌ایم: به قول خود پایبند باشید، یا عواقب آن را بپذیرید. واقعیت در حال نزدیک شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67884" target="_blank">📅 07:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67883">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=QFdu2H_R4Nk7otBKyVUIVgzkNfwPi-TSAniY273mIgOm8_Zgx1ocb8kwHCcx1_czbFAUjkXFenCneJIIa0tK6wP3jKzgtA2SGPrBUY8G3XGsR0D6A0XDoUfpOg4-X28Ispd3GJ3h5QaXGNQ7bNIy4hEwKsH1F2wvXzYzm7GkFYvVDdcDAIlVzF9MquaqKTxltohP8hBt_uAE4sng-Efc7wF_P-yDlZiTOxjwfjiEBXCl5sk9kyhB-bDLwWzf79z3gP7K1wBiBuuucdeidjiWovprrmueJIhKTJyy3oUZUwAYy6LeRTHOxz2BenXTOobp9K2A6T2kPJ6dYe_2e4BpEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=QFdu2H_R4Nk7otBKyVUIVgzkNfwPi-TSAniY273mIgOm8_Zgx1ocb8kwHCcx1_czbFAUjkXFenCneJIIa0tK6wP3jKzgtA2SGPrBUY8G3XGsR0D6A0XDoUfpOg4-X28Ispd3GJ3h5QaXGNQ7bNIy4hEwKsH1F2wvXzYzm7GkFYvVDdcDAIlVzF9MquaqKTxltohP8hBt_uAE4sng-Efc7wF_P-yDlZiTOxjwfjiEBXCl5sk9kyhB-bDLwWzf79z3gP7K1wBiBuuucdeidjiWovprrmueJIhKTJyy3oUZUwAYy6LeRTHOxz2BenXTOobp9K2A6T2kPJ6dYe_2e4BpEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
ادامه حملات سپاه به کشور قطر
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67883" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67882">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
سپاه مدعی شد: مراکز لجستیکی که به کشتی‌ها و سکوهای سوخت‌رسانی متعلق به ایالات متحده در بندر الدقم در عمان خدمات‌رسانی می‌کردند، در یک حمله شدید و غافلگیرانه منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67882" target="_blank">📅 07:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67880">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=CruRm8Q7w9QrtbmAgqSb4ETHSf_aJSXhvpYWSBm4bkT9Ye0wLsIGq0mRnc8L_y0Fb5Jb09xMDJIiAnib4mqot-08_hSINzWcAbGhUwDMz4rXR_OYatTxqpnPUl5C5jwynMCOQu6UAMmTyLpImy-xe97hiPjJGeoiuuWoMrbLOZEHRBKM7bckFPUCwhH_oGIyDctmUEIjNOUPgpPcUNPdMznpU8grcB6yvCBy5ms2isOh9A-B9K8k4gVsgZ4XHxSHZ4wamPoAUQDRtWfyg0piBXJk2eoG7L7ukxdiMYUUp-KGbzqkPBuW8XkwWu5pkbUINbNZ3BE7H2ZbEycSy6GB8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=CruRm8Q7w9QrtbmAgqSb4ETHSf_aJSXhvpYWSBm4bkT9Ye0wLsIGq0mRnc8L_y0Fb5Jb09xMDJIiAnib4mqot-08_hSINzWcAbGhUwDMz4rXR_OYatTxqpnPUl5C5jwynMCOQu6UAMmTyLpImy-xe97hiPjJGeoiuuWoMrbLOZEHRBKM7bckFPUCwhH_oGIyDctmUEIjNOUPgpPcUNPdMznpU8grcB6yvCBy5ms2isOh9A-B9K8k4gVsgZ4XHxSHZ4wamPoAUQDRtWfyg0piBXJk2eoG7L7ukxdiMYUUp-KGbzqkPBuW8XkwWu5pkbUINbNZ3BE7H2ZbEycSy6GB8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
تقابل سامانه پاتریوت در قطر با موشک‌های شلیک شده سپاه پاسداران جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67880" target="_blank">📅 07:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67879">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سوپرگل تماشایی خولیان آلوارز مقابل سوئیس</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67879" target="_blank">📅 07:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67878">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
سپاه پاسداران مدعی شلیک و نابود کردن یک کشتی تجاری دیگر در آب‌های خلیج‌فارس شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67878" target="_blank">📅 07:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67877">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فکت:
شما چند ساعت دیگه می‌رید امتحان بدین ولی من زیر باد کولر می‌خوابم
😎
#hjAly‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67877" target="_blank">📅 06:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67876">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=KE4rNvqQaQNEUgmaq7nFUOl3_yb9V2WjayTzFBd0dA8yK_6RlE4-qqqktlHQbGX4pwrTnsLCEm55agSfwWV93vbithU_2KBVWAU9VtUuPVQj_LuJSSFyXTaa52mWLCNNY-zN3OPdIkXaWzFYkyAJvh10FNPJ1FeDIGyR9xxckh2BKXPdZIpqUhraGH9PzceBXUb4dHHAzwnu45i6Egc8KWrBm-XhvtGKmA9ONUw5W7dOehr_T4tROf1QElcDC3n9SIZH42Q327zm5IzkgFikVgrODdraeq_A25opUOLexkj1CVR78Gs27va3Vcdnqz0iYDij68hWY4cYq9xrvDAHig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=KE4rNvqQaQNEUgmaq7nFUOl3_yb9V2WjayTzFBd0dA8yK_6RlE4-qqqktlHQbGX4pwrTnsLCEm55agSfwWV93vbithU_2KBVWAU9VtUuPVQj_LuJSSFyXTaa52mWLCNNY-zN3OPdIkXaWzFYkyAJvh10FNPJ1FeDIGyR9xxckh2BKXPdZIpqUhraGH9PzceBXUb4dHHAzwnu45i6Egc8KWrBm-XhvtGKmA9ONUw5W7dOehr_T4tROf1QElcDC3n9SIZH42Q327zm5IzkgFikVgrODdraeq_A25opUOLexkj1CVR78Gs27va3Vcdnqz0iYDij68hWY4cYq9xrvDAHig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات سپاه به بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67876" target="_blank">📅 06:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67875">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/67875" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">1میلیون شارژ کن 1.200 میلیون تحویل بگیر با پشتیبانی آنلاین ۲۴ ساعته
😍
🔵
برداشت آنی
👌🏼
⚽️
تنها سایت مورد
#
تایید
ما
✅
اپ اختصاصی با
دسترسی راحت</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67875" target="_blank">📅 06:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67874">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFqFfvBTJjJ7lFaZWQ20GUfxsEhT7b4l0sZL362xyuKjSDxAwAA3hgfubxEJEwEKoMWF9l5QbACU4SqX3H2uDNG3JuD124-gt66ByVdJ-6Gou4vbWjJ7fwDBR6-afE9Ox2D9yRqgW75svvM4DNJNvX3AlgixPj3ZpU1A6t8QU0pYWcHR0fB-qT1wGDl3oXyPVcPdGy0t2GyYXBY1ufRXswxE3kCXBFSftY0pHi1JZ0WsOpev35wn7bssYWat3d76ux4agw8POvLPqW8bfpH1L6F8C0cG2S_TpRa-QLTZXV4XRPoRv_umtr_TIx4BF4kUYIF7sOfVnKYuEhzNyKpLNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
تنها سایتی که توی جام جهانی هوای مردم‌ رو‌داشته تا باخت سنگین ندن
⛔
📣
خودم بدون نگرانی از باخت شرط میبندم با کمترین استرس
🛍
از این لحظه 20% شارژ اضافی همیشگی یعنی به ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان بدون قیدو شرط میده
💰
🤩
🤩
درصد هم برگشت وجه در  صورت باخت،دیگه چی میخوای؟!
🌐
betinja.bet
🌐
betinja.bet
کانال هدایا
a20
@betinjabet</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67874" target="_blank">📅 06:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67873">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1IDSRizctgL5jm_uBooUaoi_CBHl5Lgw4mN5WifmY7nCQ2ZY8MnFenpm4w6rmtmb5DSvbK6A1kVOyCOY4o0VW6iVMnfzlQ2RusljihG3nbmDbk0ft-6vnDf6E7ftjuD0HT5FUtXOh1GMTaBuLNMcvaZJLD5iEdibf23P36z0BpS6Oh_55-PRxJN2Ta5Dr3deTK_tUmFyfY_hrZRsi6PX_IqEeifYfwAsXkY3fJvLMMNC3PPAbjW2ORxkw1QzIIU1Sf70r6SPaslC0xmao65q7kaQJSy8kfctqcJgJkwVRxTMSZdCQO8gB9cQcMOO3pdJjwzzcw6YL0-FD5zVYM2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/news_hut/67873" target="_blank">📅 04:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67872">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نتانیاهو: تو جام جهانی طرفدار آرژانتیم،</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67872" target="_blank">📅 04:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67871">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپمپ بنزین</strong></div>
<div class="tg-text">ما که منتظریم اقا
❤️</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67871" target="_blank">📅 03:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67870">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67870" target="_blank">📅 03:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67869">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67869" target="_blank">📅 03:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67868">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
هرگونه خبری مبنی به حمله به تهران یا فعال شدن پدافند تهران کاملا فیکه
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67868" target="_blank">📅 03:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67867">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گروهمونو که دارین؟
😴
https://t.me/+5NElXlQWt_05OTlk</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67867" target="_blank">📅 03:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67866">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff21f4d079.mp4?token=uIy-5h9ds4LsyuAuXF8XcPeA8bnyj-th8gbuftvNKclAPpCPhrtuyLh3k-WrzDtilxlwYg2GGIXs9flpbipWe6OcCO3DZ451iDp5q3N77l191bZE-7W4J160YuPGskd7AsjUG9rJXuLMlfm6rqPIFrdvhMMwAijPLccFHGIkWYVFmbOgR6RvjgwKTx1NaUWJDM1X_jOu88lSfNJk8wF9SEV9NJ3CgQRDqep05cjfKtNXLMK6raSEzl6tFalQdRTofUj4Gw-vEh57KwMNLEc0Ojpa334kt7kfzL44zaHnlJ6-LJTEvblqFzKMWWYWkRne65zuYpDulIqNX_OVKTfeJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff21f4d079.mp4?token=uIy-5h9ds4LsyuAuXF8XcPeA8bnyj-th8gbuftvNKclAPpCPhrtuyLh3k-WrzDtilxlwYg2GGIXs9flpbipWe6OcCO3DZ451iDp5q3N77l191bZE-7W4J160YuPGskd7AsjUG9rJXuLMlfm6rqPIFrdvhMMwAijPLccFHGIkWYVFmbOgR6RvjgwKTx1NaUWJDM1X_jOu88lSfNJk8wF9SEV9NJ3CgQRDqep05cjfKtNXLMK6raSEzl6tFalQdRTofUj4Gw-vEh57KwMNLEc0Ojpa334kt7kfzL44zaHnlJ6-LJTEvblqFzKMWWYWkRne65zuYpDulIqNX_OVKTfeJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش نمیدونم صدات به جایی بند هست نمیدونم چی  جونه مادرت یکاری کن امتحانا تعویق بخوره</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67866" target="_blank">📅 03:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67865">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRazis</strong></div>
<div class="tg-text">داداش نمیدونم صدات به جایی بند هست نمیدونم چی
جونه مادرت یکاری کن امتحانا تعویق بخوره</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67865" target="_blank">📅 03:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67864">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فکت:
شما چند ساعت دیگه می‌رید امتحان بدین ولی من زیر باد کولر می‌خوابم
😎
#hjAly‌</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67864" target="_blank">📅 03:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67863">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑨𝒕𝒆𝒏𝒂</strong></div>
<div class="tg-text">آخرین باری که کل کشور باهم دینی خوندیم رئیس جمهور مملکتو خرس خورد
امسالم که اینجوری شد
فکرکنم سال دیگه انقلاب شه
😂</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67863" target="_blank">📅 03:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67862">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4QpZwuMfnVuMVwlbyj17Xp8ROXbOtojqxF5K9qGP6ECCor-tOxd_DlvJhfna_tkFP8n3wFBQBNmou2lWAXkblJKhvDeeH_KOb-JNhL-LxAJyyG72NUNZjbVMgvklzN9J_OGK0tNKv0LSL8b1ruTZyJW-96ou09C_oDY95jTKMQCzB-HYvtctaxtf0-v6zbkrr-mvbxSl_WCQZkN5GGnsB1cQorK0_FCsuyRSn9LYy4uL36CC1zPIZ6YhXO3GpSzxblohzyZ9DTv5r1e9Bum4uE0lliSFs4oWxM-kXjzOU69SoAPR1TJ7Grx9yYz8yEh_Ts266NFCvUcNYOJ4T3-FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقیش اینه به تعویق بیفته حداقلِ حداقل تو جنوب کشور، ولی اینطور کل سیستم امتحانات نهایی بهم می‌ریزه و باید بخش هاییش داخلی بشه، و البته با این مسئولایی که ما داریم چنین چیزی بعیده #hjAly‌</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67862" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67861">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dB7u_zCQjhir9OA8Id7Gm3walAjL6qbx9OSkhsfGCC41bgR_Citm3WTrV21PE35YnPKCtxnHz3ozLFHHBlTCPbfulzY28aL4nGjf2cXPm0ddIwIMr_DB64xy44LgWoREEsIl3XT2yuxoNVKSHJHr93jwAaBwswKsTJUWKJT4eZAony1bZpatngENB_b6Gtwqqr0Iez3gceTd-F1nN9L7iIRXy2C59Vvagp5sAgm2Bp0dw-WUhU3fHQD0sN14tB_5XhVNvtJGXEIHnvAmVtz_xDPRrYPnWxgXKTgn5UkIdHSyc9rlvEL5lHQjk0p345Khoy38pch6SSIpQ-9Zbt7jkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابا اونایی که نهایی دارن بخوابید توروخدا، تعوووویق نمیفته نمیفتههه #hjAly‌</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67861" target="_blank">📅 03:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67860">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3HFhGe_qq66GNRNFiaY59sRf1zobNY1DkA_iK0aLE3D7ZhN91Rk8mUwaXLrG43L6-b2GMX1uYV6gsqG6UYP0KOKxVNV2yczT9N7Td5Fbl-d94t5G4O_P50jUEsOoRcuZu-eHewjY52mH4RsfC4EzgFaHd7_Gd6J-oN302gmKHsNbpiOg145MO-BqUvVdNrBu9nhoqBa7dL1uj0MFtSr1KdG6t9hRHHx47Mk6_5_qsJy7Zgko6Die9eipre9GddVQbWS7_r53L44Y7WnKX1O8nTM0zo_eb924mxFJ34hI9HLFRNtjilUb3r80UPTlUYAeFrN2g1jkm25ICGKDF_74w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67860" target="_blank">📅 03:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67859">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzJ_qQDuul-JlwDlpUhJMtL5X5VeXoHBAcj94slQe-KqjCcUkaVghDH1vaj4lKRB4kpC0bMxh48TvJ0HawffCc1FUAVHZU40UVeD1dzAhkct4JOCjDXMAgnNyC8CFBeZjoaQxrwQGFZAvrmkiSv0sf1PWjHD_13DvAwSwXyhtOYYi72dr3XGzLr5L45lAFsEMVr9xQpVKjOaPTzrnctCSWt6OkP_R-BIbFCSiiiNQEKYpE_5VSMkKH1fd-TH2y_koYoZBaUjW3ZkNeyA5g48DXxZpmdXUspjgIFcVI47qO-OSFNISWx8Ana9L2ZwI9m7yar-tVjZyEY90ce4TU-guw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ پیت هگست:  ایران انتخاب ضعیفی داشت. حالا پرداخت می کنند.  @News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67859" target="_blank">📅 03:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67858">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
نایا:
دو انفجاری که در جزیره قشم شنیده شد، نتیجه درگیری‌هایی در آب‌های خلیج فارس بود.
نیروی دریایی سپاه پاسداران انقلاب اسلامی و ارتش ایران با ناوهای جنگی آمریکایی درگیر شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67858" target="_blank">📅 03:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67857">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
دو انفجار در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67857" target="_blank">📅 03:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67856">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=MzJdOI0c2L927fRbFUncWDv99Y1iNMLlmAXuLktsPgk7duFf2gMgMDvLWhtjN6SdHhJf-RJ5d6yYwXeJw3iL4zkDsTPunbiHdYaBj1fIV6zSQcA1gINIeE5iVsDmsLM2XGBAmT9rXAAqX3D-fSU0jl2p6BI1qCjGC9afaqeVZWqqqZ67xDtKWlN97oVnyadmRSX0M9b2u0dkr9lFDKIjOWHoH5TR7g9kYkTrCVTgR0AjDjshEUx_eldNOZk7jKf0VEI7ZlFtMUzom6BCpKI2_HFTcHrRzgqbIjpMtX02lGSfahsrYsSb_nMKHr2HGI2yxdovACrbp1NdY1VDSUyOlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=MzJdOI0c2L927fRbFUncWDv99Y1iNMLlmAXuLktsPgk7duFf2gMgMDvLWhtjN6SdHhJf-RJ5d6yYwXeJw3iL4zkDsTPunbiHdYaBj1fIV6zSQcA1gINIeE5iVsDmsLM2XGBAmT9rXAAqX3D-fSU0jl2p6BI1qCjGC9afaqeVZWqqqZ67xDtKWlN97oVnyadmRSX0M9b2u0dkr9lFDKIjOWHoH5TR7g9kYkTrCVTgR0AjDjshEUx_eldNOZk7jKf0VEI7ZlFtMUzom6BCpKI2_HFTcHrRzgqbIjpMtX02lGSfahsrYsSb_nMKHr2HGI2yxdovACrbp1NdY1VDSUyOlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فارس:
گزارش زندۀ خبرنگار صداوسیما از آخرین جزئیات حمله به جنوب ایران
تا این لحظه سه انفجار در بندرعباس، و سه انفجار در سیریک تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67856" target="_blank">📅 03:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67855">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
خبرنگار صدا و سیما در عسلویه: صدای ۴ انفجار در این منطقه شنیده شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67855" target="_blank">📅 03:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67854">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
چابهار رو زدن
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67854" target="_blank">📅 03:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67853">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
❌
شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67853" target="_blank">📅 03:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67852">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpn8oSx8yG9aYHLmy_UAY5lx8tYVDipRpdYWBn2t0GPthiacqrzspn_D5rREvojUbeA5JO8fiQHcAnmrH8Kf-AdGz39Qqs2wKyajoaFatQNrDIWdOImbuvWPNnkmhjyxpObxGaHB4zQgnRq9Ob3AvqPn7l-xvC8WWhlsS2tVh1Y3VGaNgkeCfdjr4qmP1N1ZYsDlIzCPllcX5DPBz5Hzgtrr4gBQoC1KthkUsdcpAO-W-sVKV6hlgyrR_JZUI0cd4Y_40dE9mZSR_NlZHCuMFSmWe7qITfrrzMfB0zCneLtProB4ayXWuV-nArSpd_ZFOGprQBkGrKbP_8oa1u3uyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ پیت هگست:
ایران انتخاب ضعیفی داشت. حالا پرداخت می کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67852" target="_blank">📅 03:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67851">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed7140b74.mp4?token=EU-Dg-wIAb0_WhPcVylEiJeD3IF4rpSwyvcanEzaMk8TsXb1qZZT3JW_Es3eIwUcpTG918uMIddzthXJbJ4vrPIDqmy5V-rOFA-Mmi0uABN4HKR5ilkUbN2uNgp4jL1CWo6TAtRN4SGsA1Mmbq126kPqO5T28LIbKcUbPKcQVM-7G2NSTNQOlLFJyJBmdUSYOaW7MqPqoDs-k2lnlq1B3FY_FhyfZUYEZ6gI_REDRLvz3pVKVy8NQ8L08R8s1_QdehK_HWN3Hx3Larus209Wg9OFauVPhnV4sOHdSBiiNYSmZU-ficDSc_4py6ImYewKF-mdd5yY-g76qQeNWDlBmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed7140b74.mp4?token=EU-Dg-wIAb0_WhPcVylEiJeD3IF4rpSwyvcanEzaMk8TsXb1qZZT3JW_Es3eIwUcpTG918uMIddzthXJbJ4vrPIDqmy5V-rOFA-Mmi0uABN4HKR5ilkUbN2uNgp4jL1CWo6TAtRN4SGsA1Mmbq126kPqO5T28LIbKcUbPKcQVM-7G2NSTNQOlLFJyJBmdUSYOaW7MqPqoDs-k2lnlq1B3FY_FhyfZUYEZ6gI_REDRLvz3pVKVy8NQ8L08R8s1_QdehK_HWN3Hx3Larus209Wg9OFauVPhnV4sOHdSBiiNYSmZU-ficDSc_4py6ImYewKF-mdd5yY-g76qQeNWDlBmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
شلیک موشک های آمریکایی از بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67851" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67850">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام):
ساعت 7:15 بعد از ظهر امروز پس از اینکه نیروهای سپاه پاسداران انقلاب اسلامی به یک کشتی کانتینری با پرچم قبرس که از تنگه هرمز عبور می کرد، M/V GFS Galaxy که در حال عبور از تنگه هرمز بود، به طور آشکار، نیروهای فرماندهی مرکزی ایالات متحده، سومین دور حملات خود را علیه ایران آغاز کردند. یکی از خدمه غیرنظامی ناپدید شده است و کشتی به دلیل آتش سوزی داخل کشتی و خسارت قابل توجه موتورخانه قادر به ادامه سفر نیست.
ایران فرصت دیگری برای نشان دادن پایبندی به یادداشت تفاهم پس از پاسخگویی به حملات قبلی به کشتی‌های تجاری در اختیار داشت، اما باز هم شکست خورد.
در پاسخ، ایالات متحده هزینه سنگینی را با ادامه کاهش توانایی ایران برای حمله به کشتی‌های دریایی غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه عبور می‌کنند، تحمیل می‌کند. این حملات به دستور فرمانده کل قوا انجام می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67850" target="_blank">📅 03:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67849">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16f69bf83.mp4?token=JmA_DyyHSxlAAi0VRQvm_JcNVOwl4ONFe2tTFJZIrz95l0OCi31zETECfxCa24Tf_3vCdpOWyz0ojytxfVW6dvNok3-SGfAdrkquYVNzHrpwnq4anpKrRTyy_2lgQFtnyjOUAajWyqmv54gOI-Auct_piuwm_ez6C5zzMLYSm-lGverdbnzws8zY_Ryei_HjfrGdHoFvmm63eporwT4L4uCcbxaCDFZxq5K1E5xCoITYiZl2QZjxp0ZI1P0WFRMsBbNcLh__iG0dU1Ha9O1ZcN3I8Uf_38DZBBG_WqsRZIGFx4gjAd52rCXlH4AfYDjxtt1o048Ob5kJWVaD2f5_cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16f69bf83.mp4?token=JmA_DyyHSxlAAi0VRQvm_JcNVOwl4ONFe2tTFJZIrz95l0OCi31zETECfxCa24Tf_3vCdpOWyz0ojytxfVW6dvNok3-SGfAdrkquYVNzHrpwnq4anpKrRTyy_2lgQFtnyjOUAajWyqmv54gOI-Auct_piuwm_ez6C5zzMLYSm-lGverdbnzws8zY_Ryei_HjfrGdHoFvmm63eporwT4L4uCcbxaCDFZxq5K1E5xCoITYiZl2QZjxp0ZI1P0WFRMsBbNcLh__iG0dU1Ha9O1ZcN3I8Uf_38DZBBG_WqsRZIGFx4gjAd52rCXlH4AfYDjxtt1o048Ob5kJWVaD2f5_cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67849" target="_blank">📅 03:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67848">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇺🇸
🇮🇷
باراک راوید به نقل از یک مقام ارشد آمریکایی:
ارتش آمریکا در پاسخ به شلیک سپاه به سمت یک کشتی تجاری، چند هدف ایرانی در منطقه تنگه هرمز رو هدف حمله قرار داده .
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67848" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67847">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67847" target="_blank">📅 03:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67846">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67846" target="_blank">📅 03:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67845">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
بوشهر رو بد زدن
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67845" target="_blank">📅 03:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67844">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
چند انفجار در اهواز و بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67844" target="_blank">📅 03:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67843">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
تصاویر بیشتری از اقدامات تهاجمی آمریکا که از بحرین آغاز شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67843" target="_blank">📅 03:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67842">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=ZUjFqULYdvv-XHFWsr4rpiEJioCgblUOYC-ffpyHuukCOSTaOHEGNyPhcaTPCFurtiK5ZGzB74H0nbj__lN4ChpeW6JZFljdU9kpYQeLeP0gFRWVEKCfh1yCGJa9PW-koA-7SB6cHaqBXNeJOEj1DrPsDxJKoq9Pm_FJbkZ-RRATD_EV131-XwkMpg_rQz95UzgR_BQVlDwmiHJ90I30_w_qs5q8_qe-s73n9wO9XaMSiYBGsyQ8EWdeDgImTXVVLIP3BMOrwFrW6lBnXmrji0iOosnf5wpYewBHWMLKz6h3qu9Vl2Uf_bnF9RulWLEEnKb7XsMRtfLqlALRnOd5EIQZ3bs1d7FdP6VIFuMpncPfrwJ_sInutwMUIh3Cwf8FFBHhhsKkAU0FwCzy9FXOH6kiyqjVs_3sDStRQaR_6LUaAbPLr6w_c3DFRv1gew0ZSCjRXozebeXICZQWMLz2yZPwMM_Jm15BAHQ4yi72apMOyPEQYC4HgCb1ewli7bj6wJpS4-OkaHlapRLgas3_IYALl30W6NbBDoQJW7rxdKYub28J7Okm2GRuiOm4PLBEuZmX_FvYcDdaIF6zAnZDyKI0mvb6EWFCVlZ6K7SwaBfTDlDNHH9zGcXt4KPfv-46vmbobzs8FWsqirJAVlSfGdV2E8fv70dMQtsSIFsWXsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=ZUjFqULYdvv-XHFWsr4rpiEJioCgblUOYC-ffpyHuukCOSTaOHEGNyPhcaTPCFurtiK5ZGzB74H0nbj__lN4ChpeW6JZFljdU9kpYQeLeP0gFRWVEKCfh1yCGJa9PW-koA-7SB6cHaqBXNeJOEj1DrPsDxJKoq9Pm_FJbkZ-RRATD_EV131-XwkMpg_rQz95UzgR_BQVlDwmiHJ90I30_w_qs5q8_qe-s73n9wO9XaMSiYBGsyQ8EWdeDgImTXVVLIP3BMOrwFrW6lBnXmrji0iOosnf5wpYewBHWMLKz6h3qu9Vl2Uf_bnF9RulWLEEnKb7XsMRtfLqlALRnOd5EIQZ3bs1d7FdP6VIFuMpncPfrwJ_sInutwMUIh3Cwf8FFBHhhsKkAU0FwCzy9FXOH6kiyqjVs_3sDStRQaR_6LUaAbPLr6w_c3DFRv1gew0ZSCjRXozebeXICZQWMLz2yZPwMM_Jm15BAHQ4yi72apMOyPEQYC4HgCb1ewli7bj6wJpS4-OkaHlapRLgas3_IYALl30W6NbBDoQJW7rxdKYub28J7Okm2GRuiOm4PLBEuZmX_FvYcDdaIF6zAnZDyKI0mvb6EWFCVlZ6K7SwaBfTDlDNHH9zGcXt4KPfv-46vmbobzs8FWsqirJAVlSfGdV2E8fv70dMQtsSIFsWXsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر بیشتری از اقدامات تهاجمی آمریکا که از بحرین آغاز شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67842" target="_blank">📅 03:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67841">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/todRNwf-DS5UHXz_c96CJW9PIqmt2jWF68TZxvXF5KfHh7hrvgfTqoOA5P92TW4Y5rtK1zVTCkTXqoWnI2_jQwIs855ot4c-VcexJsf8FrLhJUCq9J45qcHtNsCDAR0TVFC7Mxzgrs-O9giyWpCQ5wN3pAyYR3CuPr58NYuxnGDE7BmCvwEu4bqTiILk0AyOmexsoXEI5JtsKvXleJ28OMAiRDCz5zoXKsUNGPX1yslBg1IunM6wV9Kc5H2u4xZxghgkRPOfWjDW4GPyoXlhMmsoXczgWKNYVE05Jv4NyGnYuxZzPWLYYhe0tgIuTjaFzCQGE9x5eEuuOb6v2zsFoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
منتسب به بندر دیر
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67841" target="_blank">📅 02:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67840">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
چند انفجار شدید در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67840" target="_blank">📅 02:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67839">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
کاتز، وزیر دفاع اسرائیل:   من و نخست وزیر نتانیاهو به ارتش دستور دادیم برای انجام عملیات نظامی مستقل تو خاک ایران آماده بشن.  @News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67839" target="_blank">📅 02:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67838">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
انفجار های شدید در عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67838" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67837">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b4e512f5.mp4?token=nh6kyrX3URD03CEzB6VN047txKRcZxUcIF145P1-MYSEDsPPlYjA7qbMejmn61GwbVSyDB48ZFn48er0Dcp70fdTsb4UG-DbBiBUDZyHf8_Q2RZ66tri67kVkl44L91I9AXWTuQC1orqdOYKZfE9XnxkrD89V73f8W3b1nJIkXEr9cd33qRf_Y6QjME7CtfI1zYHvQ0cJ4xwg1UEvZAmeEqpmkPfK1IPj8MsYKok--syM6XMr1uMuE5hT9eyqUV-9KBBfhZnhjTewDHd8fF-wsAsAkI1tf-mzBQN6c0mDBZsQT8WgggBFELsH40SsGzH4nHJNML60PYJnO_heZOeRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b4e512f5.mp4?token=nh6kyrX3URD03CEzB6VN047txKRcZxUcIF145P1-MYSEDsPPlYjA7qbMejmn61GwbVSyDB48ZFn48er0Dcp70fdTsb4UG-DbBiBUDZyHf8_Q2RZ66tri67kVkl44L91I9AXWTuQC1orqdOYKZfE9XnxkrD89V73f8W3b1nJIkXEr9cd33qRf_Y6QjME7CtfI1zYHvQ0cJ4xwg1UEvZAmeEqpmkPfK1IPj8MsYKok--syM6XMr1uMuE5hT9eyqUV-9KBBfhZnhjTewDHd8fF-wsAsAkI1tf-mzBQN6c0mDBZsQT8WgggBFELsH40SsGzH4nHJNML60PYJnO_heZOeRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شلیک موشک از بحرین به سمت اهدافی در جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67837" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67836">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خسته شدیم از این چص‌حملات خدایی، قشنگ بزنید جاکشا
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67836" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67835">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
ارتش آمریکا رسما حملاتش به ایران رو آغاز کرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67835" target="_blank">📅 02:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67834">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از حمله به بندر دیر و بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67834" target="_blank">📅 02:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67833">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67833" target="_blank">📅 02:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67832">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش‌های اولیه مبنی بر شنیده شدن صدای انفجار در منطقه عسلویه منتشر شده است. منتظر تایید این خبر هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67832" target="_blank">📅 02:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67831">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4398edce9.mp4?token=lRsZOt9u9uPdvX5YKnv1O1zpsigSWtS6n2HYHo2_E5nVvgrV28UyasDFhJd2TyYgEId0RFllgVPxYscehmTQoqtgezrsJm_LAzg0AaNWVUB3x0uPyRDuVYH-lz2ri5iGABxlcptmOqsDK9wxoxMCMY-U1z0rCTEnuuDzkhq1xT1KcMgwkuOZIXsafHbCiiR3B8s25OCaVNE0JcOnBSq2p74R15uwdknBwRIlaiAF3xSuaaYgX9WSs8kQ-HugNQmur3Gb5VwZt_d0shx0gHDep4CZUIksQwcvNBk-7-JwhYRGUOM9BuMn6cySFSl1ueikYyXbv2sQjL2gtZJplTdv4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4398edce9.mp4?token=lRsZOt9u9uPdvX5YKnv1O1zpsigSWtS6n2HYHo2_E5nVvgrV28UyasDFhJd2TyYgEId0RFllgVPxYscehmTQoqtgezrsJm_LAzg0AaNWVUB3x0uPyRDuVYH-lz2ri5iGABxlcptmOqsDK9wxoxMCMY-U1z0rCTEnuuDzkhq1xT1KcMgwkuOZIXsafHbCiiR3B8s25OCaVNE0JcOnBSq2p74R15uwdknBwRIlaiAF3xSuaaYgX9WSs8kQ-HugNQmur3Gb5VwZt_d0shx0gHDep4CZUIksQwcvNBk-7-JwhYRGUOM9BuMn6cySFSl1ueikYyXbv2sQjL2gtZJplTdv4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
کاتز، وزیر دفاع اسرائیل:
من و نخست وزیر نتانیاهو به ارتش دستور دادیم برای انجام عملیات نظامی مستقل تو خاک ایران آماده بشن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67831" target="_blank">📅 02:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67829">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
تابناک:
گزارشات تایید نشده از حضور تکاوران ویژه دریایی سپاه  "S.N.S.F" به صورت تیم های غواص مین ریز  و قایق های تندرو در تنگه هرمز مخابره میشود.
این تکاوران از یگان های نخبه دریایی ایران مستقر در مناطق دریایی سپاه در خلیج فارس هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67829" target="_blank">📅 02:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67828">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بابا اونایی که نهایی دارن بخوابید توروخدا، تعوووویق نمیفته نمیفتههه
#hjAly‌</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67828" target="_blank">📅 02:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67827">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🇮🇷
سردار عظمایی فرمانده نیروی دریایی سپاه پاسداران کسی که دستور شلیک موشک به سمت کشتی در تنگه هرمز رو داد.  @News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67827" target="_blank">📅 02:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67826">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HuazLIkl6TnceR1SWyq0UpjI_gw8fpx9RJc_V1dzd2vDpPS1PzzEnRio5L9HQnHwVKdioABPyoDZGs-K3W9KTk-Sofl9DBiAsixU8JyMNPFxSpR9kKpUmmeD7vJLTMEqBGXcIegaR9XWT9sDJdIF_q-HKdFcIJEIBKFSdkBhPfQbOv1LLrAFN3Ur4IO-DfY79oDBL2zCOg8j0qwmfjM4YvJwKN-XAnFI43dY8QsB49eua2rct83ZDsYny8aKO4DwLtLFMe9bW6yqTveoHegWqnGEArYStnRgRgPK9K5Y4WJ5uySKR48Jw8AHyBQEamrH5_k_doKSvCVTna7V9YEi1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حدود 35 دقیقه پیش یک موشک کروز ضد کشتی از سیریک به سمت تنگه هرمز پرتاب شد.  @News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67826" target="_blank">📅 02:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67825">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWpM_tdb2zeroKLGlpjusNXkDFsF_v3LcL2RnbRCvpqZ2rBkHyLdsGL7kFwcZK2QNiT9M_R02myPn0tbZfDMSqtKyvC2BGT4h2yvT557LcqCt5kiVVSWXqnbhssm6pQNGQfHE0cdQ4kD4ZdQbJXDT1horJLt6OOYOgnVXASC61jqbGXeVBuy1xPI0gMl2SdoNTZQFiTfY53Xrtoc655J_tKk7HrUDfQJGN_u4_kbosJ9U8hkmIqEm1qY8p0z1_HUyLGnphJ5qjRUdEAWRDmac7jG5ha-ot0I7Qa8_roZ7-CyRI0gixlEEV6OprIsgbLR0UuFdRJVT9MVRr_clTL5HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هم اکنون زیرنویس شبکه خبر
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67825" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67824">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxZ6swV8JLEJLX9hJ28XsIuPixjI0nE5Hh8hknslJjC5v0hMpvHjyb2EnroEAY-TiDNp9mHbvp-1zTtw82_Rtttam5aegzQ08lH8R_mG9EONoRIIN84ks_UXfXFSHqfY6ae4SUU90Rv16MS6F-s_igBRZFJmCfFFqZzTZwiqtRqncOsTlw06leRuztoSfNVX-3xtSdtpfXKmoUnOccq_eLVrpI-7OIaFPCoWZyXzJhqif2MR5_P6IYrz0AFmo6SOUlCYrvCO2e4LzmtuWmreMWsCu54Zq8fGC4axP9PwDFrI4s07nEXn6QePFuDh9H5Zna3nGfqnZI3hqL95fKpwFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سردار عظمایی فرمانده نیروی دریایی سپاه پاسداران کسی که دستور شلیک موشک به سمت کشتی در تنگه هرمز رو داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67824" target="_blank">📅 01:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67823">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
صابرین نیوز :
به دستور مقام معظم رهبری، حضرت آیت‌الله خامنه‌ای، مدظله العالی ورود به تنگه هرمز مسدود شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67823" target="_blank">📅 01:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67822">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
حدود 35 دقیقه پیش یک موشک کروز ضد کشتی از سیریک به سمت تنگه هرمز پرتاب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67822" target="_blank">📅 01:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67821">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🇮🇷
بیانیه سپاه :
همون‌طور که توی بیانیه قبلی گفته بودیم، هرگونه دخالت خارجی و تعیین غیرقانونی مسیر حرکت کشتی‌ها در تنگه هرمز، با واکنش قاطع ما روبه‌رو می‌شه و روند افزایش تردد دریایی در این تنگه رو مختل می‌کنه.
چند ساعت پیش، با وجود این هشدارها، چند کشتی با تحریک طرف‌های خارجی سعی کردن از مسیرهای غیرمجاز عبور کنن و به اخطارها و دستور تغییر مسیر هم توجهی نکردن.
در نتیجه، یکی از این کشتی‌ها که با خاموش کردن سامانه‌های خودش امنیت دریانوردی رو به خطر انداخته بود، هدف تیراندازی هشداردهنده قرار گرفت و متوقف شد.
از این لحظه و با توجه به شرایط امنیتی ایجادشده در پی دخالت‌های غیرقانونی خارجی،
تنگه هرمز تا اطلاع ثانوی بسته می‌شه
و تا زمانی که مداخلات آمریکا در این منطقه ادامه داشته باشه،
هیچ کشتی‌ای اجازه عبور از این تنگه رو نخواهد داشت.
همچنین اگر دشمن متجاوز به بهانه این حادثه، که خودش باعث به وجود اومدنش شده، دوباره دست به حمله بزنه، پاسخ ما قاطع خواهد بود و پایگاه‌های جدید دشمن در منطقه رو هدف قرار میدیم.
کشورهایی هم که اجازه دادن نیروهای آمریکایی و اسرائیلی از خاکشون برای این اقدامات استفاده کنن، مسئول عواقب این دخالت‌ها هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67821" target="_blank">📅 01:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67820">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
#فووووری
؛سپاه پاسداران انقلاب اسلامی از مسدود شدن کامل تنگه هرمز خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67820" target="_blank">📅 01:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67819">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2Zpq_tBUNRZJJEEPhoUdSIlSwpT5Wl0xUyidin2iZorjoF-YIeaeNU7cUln0rp_XNmgjFOHJ_AGtqDXLhsj1Zcfhkgts6svYZUMFP5Ekt989NCDws0a0Ak-suWSn4JyZ-7JW9RN1jCZz3g5WEDdKwouu1o42A5JLrZ7ZOkrS1qWC40am2tZLcQgVP1VSZ6I16lWFaJiWzOxIksvSmU6Vf-rgZdLg90dLt34uVmJ2ebddM-gDb2hAziVuaN8zqZmGhjXjA5Q_RXL0Qxa8VIL_XtXhsgBEv1bammbT2Q1xP9Ei4m0Zwm0H_0yt2-L21aRt1w1OXLISKwrOilux5BCgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67819" target="_blank">📅 01:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67815">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G0o4W1Ks1fI_BQXF4OhKAF9noSD5asH0Aj0HiIrJeutTJ8oi6_5e5xApSYVeTz63Q8Pdee6EdqwVGzLqYOnA7D2pgbJkhTuW36S5ouKciI53pYomJW__ZistN9bn_yLirtHpw31ATP0J76DFVqKcpRzg-rcebrHOFnmtCJdu0GZQ1XBcFWAm1PearyCo3NO0ATyr0F9x-ifKHs64P4xHMz9cbzPnG-Hy341yEHjMPUjtlpLXmxs4v3BMJ1mE2bYpFTRJchu0fFvj6Wl9SGx_75x6K3w2--ucpVlxl1Fmd5qej_Tcy1ixPvmNZ7Rxb2FqsKonc88ZFToS4jZ3h0JZFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JMxDrRcjEje87vxOot3lhzyiDglZppZLWybInF6258JFHwyqKLA-T_lkBUSP-m5D4uVmTPWc37JcPXCZN5UZqaME95YdxxfzGEfmSKuzemmF0Y0TNoxf4W_WM_La8rlUbIHPucv157Tt1OYxTCM7UVq6IyQrgnikuurpQhWNiylam2DHnS2YhOi1yPXwXYLIjtkjqP_sXGncVX9PTYKFFM2VK3I2L-khacH_A8pL38qK-C5uo3CrA8YKaP6lpjfSgZMZnK7xungVRUVM-J3ffD19UOqh4T8x1lt_Q-7jQwiHbrKzon-7gxtRiVjSVeXzaPhzaTrTod_E9bAheaPxwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gxlizxXC9PrbB1KbfeWrgZLz6y6hSXl35g-5TF7GhMDe5rW-g_u5vsSzUTIaoP6JLv0xsX2YbshxQIQ6h09HGCZbSRvIxUuSJrrspO3s1FHkiHVB2SIIYYsgi2xtDYmVEgrE4MswnXxjQBIKruR4M59xUFPe2hHd75pNBU9aEnXGE0MT12D_Cw7SiFXNaec1hUdZ2gl1LrBkYoloszl44FHUYBL9H4uUWflpFo2qv5bX2QrYRirZw9-Zy3LnKxmkJpucdaZ5EX3G3WGoOERAFiCjWriimx0PSlmVFXamxsHRcDOv4dPcn3BkY_SyswbJOOmZ-y4bvtto0OeOi9zdHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ad5DWTtPAAddnmvZ4L_FTOv2AY6iciGqOu1f8zARFdvUF4of5dLUg3xhT08L4OSdlLGTgY3RS66Py0NypCUXm9pBm5Bz3V688L6b3VqoCHRl72XK8XWwgeXZOLlE3y9djK2RXADmUN__X1YRRR58BRlfBS7nqCpBR6N7cB3tpLptz7X5WPDMgNcrkIYzq6cGB3fCh_bAbM6CW2E_tUHgzrm0GKiSDSLLhPuWMLMigMHPe3g01RFEnRr1T4hmEOTTp727LrJ9_0SKmKpFNU3fC8bWiJISV0KBH0B0L4a4jIdz8W09gPx8gSf5Eta55HLcy4E8HRtF75R71Y9S6FCNvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚠️
هواپیماهای باری نظامی آمریکایی از نوع C-17 در سه پایگاه نظامی که توسط ایالات متحده در داخل اردن اداره می‌شوند، فرود آمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67815" target="_blank">📅 00:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67814">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbae51b67.mp4?token=Ak9Y3A0V4uEbAaxBg8OHEF5P2JnPwnQPK3GCVzvVLN3jfExX1HxaxHuVGp9W4eT3mgWKHSd-126KKCxaFbAxKh37F12j8IzzVf_hxYOJNjoH8ZVNcwhx28yk8WHcrN_ErR2sWsiZXG8BnEZ8jGDatwuGa2C2aMrqxe2z026txzDLZrabbnFXp9m2pvHYPJ2u2dw5wddX_AXCrs0Dh9psLqVvl2gPBrAzkwpxpHg_mSvRIwP2S8lROIWps_2p481lkm5UJxvyLSx0V68y9VqgZlMxeWomm8sHTB00wcNx0jRUKbALZM0qB3ZBv0K6OsMCbX1IsLmQujypxIKWs2v3Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbae51b67.mp4?token=Ak9Y3A0V4uEbAaxBg8OHEF5P2JnPwnQPK3GCVzvVLN3jfExX1HxaxHuVGp9W4eT3mgWKHSd-126KKCxaFbAxKh37F12j8IzzVf_hxYOJNjoH8ZVNcwhx28yk8WHcrN_ErR2sWsiZXG8BnEZ8jGDatwuGa2C2aMrqxe2z026txzDLZrabbnFXp9m2pvHYPJ2u2dw5wddX_AXCrs0Dh9psLqVvl2gPBrAzkwpxpHg_mSvRIwP2S8lROIWps_2p481lkm5UJxvyLSx0V68y9VqgZlMxeWomm8sHTB00wcNx0jRUKbALZM0qB3ZBv0K6OsMCbX1IsLmQujypxIKWs2v3Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک پسر هیجده ساله یه رولزرویس رو یک روز بعد از ترخیص شدنش از رو کفی دزدیده
یعنی رولزرویس رو تریلی ماشین‌بر بوده این با هیجده سال سن اومده دزدیدتش.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67814" target="_blank">📅 00:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67813">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzw8LQUSL46ajrpECNUzYP-_68_JB-5zLzCuEXnzMb9UfgWTj-NeO_ORxWajeyyhvcXMTLGSRD-LDs9J3akmca4baqMUkbPnJfNQNNGCwjIcIahjfygiYwKfOXo_cS8a0IIMd2siLsv1XpG4AwY3Ywmbkk7ha8gUwGAoZEC3oTk0_8WyByiEFqVAdPXC3Twpkw2SlgYzT7yaeV5TikF7imc8LaaKY8SXS7zGJKYjQUg5XL1ceFDvWc49TXAabWDezi-87TsphRbsxDBH_JSoCR5nXSqxxRVgXOCcDk2S2dMPHiPjYe0tgYDuIDh_cSuX0FyxpnrNSnZk78yc5jVV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کانال 14 اسرائیل:
اعلامیهٔ مهلت ۲۴ ساعته دولت ترامپ، که روز جمعه، ۱۰ جولای، صادر شد و از ایران خواسته بود تا حملات در تنگه هرمز را متوقف کند و از آزادی تردد کشتی‌ها در این منطقه اطمینان حاصل کند، در ۳ ساعت آینده به پایان می‌رسد.
این توییت دو ساعت قبل زده شده و تقریبا یک ساعت دیگه مهلت یک روزه ترامپ تموم میشه
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67813" target="_blank">📅 00:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67812">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
🇺🇸
مهلت اعلام‌ شده ترامپ تا پایان روز شنبه به‌وقت شرق آمریکا ادامه داره که میشه حدود ساعت ۷:۳۰ صبح روز یکشنبه به وقت تهران…
تا اون موقع به ایران فرصت داده ترامپ که اعلام بکنه که تنگه هرمز بازه…
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67812" target="_blank">📅 23:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67811">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c50mlv4Mhu24xroWwXfu8sHREDOl55pkKTqAsgqaTOtECz9ctc14DOfthXaJ6vRkcGhluXx1krq6vFxDes4urufpFd4KyDhH6_WBNuHzfEsjPcTGy_suzuXiu7z2UITIvbKPWA_5kJMsaeQuwjcvkYjCbL3_RRvt-lm9sinhgJMqCN6zPDmpgbnr9JLO8vIH--CEiTvtUte1OFV4lToM42oC_tFKTP9RhoYbJGSOxGCVVp6MSmFbconmuzol_O_8BhG8gWkBl2NetbHd8024Dh0g7l13D8WNoMr01L2SUn8AP0D4RXZRMBCucE5C-5ML1p2WikkhNZUv2fN0O1n40Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پویان مختاری گرداننده‌ی سایت های قمار که خودشو مخالف شاهزاده رضا پهلوی جلوه داده بود و معتقد بود عاشق جمهوری اسلامیه؛
امروز صبح ساعت ۶ با هواپیما به فرودگاه امام تهران اومد؛ که توسط وزارت اطلاعات بازداشت و راهی گونی و منتقل به طویله شد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67811" target="_blank">📅 23:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67810">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9S4UUQlbiqiKhtQB5ioD88LoV5R2eLGnxBzINsd61heaPd0owODHznceiVnYnWw4-aoe_u-EKIeVKYQxF6I1XqYEdiocbCDOzQxeL_0XDaxyFJJHZyGNVFs6E9US2YU4yoF5-aa-jw0v-s2j77_L6WrNZ7cesYg0a2O3geqZlTDqBldEhQ4c9-_Rgbl0IS6roR2-eBPPnHuUckj3hfMwKQ1wSvhrsu00dYI1yGHPNMSC8TVaGZmjQ3wAP6FBVmVNxPLth-OxyuvU9WF7PB61uqM_1jy0AhKQEJQaox9jgsbZk4F2j97-cj79Ky9uQ1X3TLwVcmRGxcLCvu_P2BFlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علی قلهکی:
قرار بود سفرِ عراقچی به عمان منجر به صدور بیانیه مشترک درباره مسیرِ شمال و جنوبِ تنگه هرمز گردد و در ادامه نیز «قالیباف» و «ونس» به مذاکره اضافه شوند که با بازگشت عراقچی، گمانه‌زنی‌ها درباره به بُن‌بست رسیدن دیپلماسی در مورد «بند ۵ تفاهم‌نامه»، بیش از همیشه تقویت شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67810" target="_blank">📅 23:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67809">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
اکسیوس:
ایران نتوانست در این جلسه، موافقت عمان با این پیشنهاد را جلب کند و مجبور شد این پیشنهاد را برای بحث و بررسی داخلی در تهران مطرح کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67809" target="_blank">📅 22:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67808">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a62buPGOqrD-dojHB1w9J0QdSsKtHRCxiHclkAhAL_JJ0aPqNIs7T5Qtig7cpqFDX8a1IK2_KNNpvmaykowMmEs1tRw_3SZD0vb2pBIo6k1dED3yX8dCEwMWscKVrv7tt_vzUBUrrTFIi7Kdzvq7bZqo_ZET6zwZbqxE0ou14qRiDuUOHWTniqozFu261PPzUQ59yKoovZo3TaZW-pdt1fj8ILzxCRKfu8efy8xW0hfFp3XmLcQydB4Nesc8hF3qv0dcVJdJWdzTx81oeX35EB_d-0UOB-L4wwOYHBjgShhqRtlLuKoaWJZavR24mVyZmHGGEskYCftfD27q649mPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سی‌ان‌ان:عمان پیش نویسی را برای مدیریت کشتیرانی از طریق تنگه هرمز با استفاده از دو کریدور جداگانه کنترل شده تهیه کرده است.
بر اساس این پیشنهاد که هنوز نهایی نشده است، کریدور جنوبی از طریق آب‌های سرزمینی عمان برای کشتیرانی آزاد در شرایط پیش از جنگ باز می‌ماند.
کشتی‌هایی که از کریدور شمالی از طریق آب‌های سرزمینی ایران استفاده می‌کنند، به تایید قبلی تهران نیاز دارند، اگرچه ایران هزینه‌های ترانزیت را تحت ترتیب پیشنهادی اعمال نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67808" target="_blank">📅 22:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67807">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d2e49f67.mp4?token=Kq6zN6847VF4bfhv2q1VgHsm9GeQiuOA5e-1gP4rtLN3HzJxvYT4IJYzofnns4QK3c0a6OgiziUrOXUdkL1yL1OnRztjG16VgxpLzvexG1kjSomUc06x6_jlFZfinhImfUc79xSNR78t9n-fX_XfeV6X-IXsTK5H7JK0uS8qLkRU00luQU-mAvpR7OiRO_1-KG3GJBVl-YOGmTOKbX0xWwSXaH2dUGWMw-K0Z0Xq4Of17Fu885y07WxoTBn5pu8O4_uXVkyPFxTBZLboY6TyJKDCW82zo1zfK0-wiB3Dqm7er3IHHa33MMXf07HxNbtB-DPE3jBz5cyexpGtHoV-EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d2e49f67.mp4?token=Kq6zN6847VF4bfhv2q1VgHsm9GeQiuOA5e-1gP4rtLN3HzJxvYT4IJYzofnns4QK3c0a6OgiziUrOXUdkL1yL1OnRztjG16VgxpLzvexG1kjSomUc06x6_jlFZfinhImfUc79xSNR78t9n-fX_XfeV6X-IXsTK5H7JK0uS8qLkRU00luQU-mAvpR7OiRO_1-KG3GJBVl-YOGmTOKbX0xWwSXaH2dUGWMw-K0Z0Xq4Of17Fu885y07WxoTBn5pu8O4_uXVkyPFxTBZLboY6TyJKDCW82zo1zfK0-wiB3Dqm7er3IHHa33MMXf07HxNbtB-DPE3jBz5cyexpGtHoV-EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سی‌ان‌ان: برای نخستین بار جزئیاتی از حمله موشکی رژیم جمهوری اسلامی به ناو آبراهام لینکلن منتشر شد
.
شبکه سی‌ان‌ان در گزارشی به موضوع شلیک موشک‌های رژیم جمهوری اسلامی به ناو هواپیمابر یو اس اس آبراهام لینکلن پرداخت و جزئیات تازه‌ای از این رخداد را منتشر کرد.
این گزارش در حالی منتشر می‌شود که تنش‌های نظامی میان واشینگتن و تهران همچنان در سطح بالایی قرار دارد و موضوع امنیت ناوگان آمریکا در منطقه بار دیگر مورد توجه رسانه‌های بین‌المللی قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67807" target="_blank">📅 22:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67806">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
کانال 15 اسرائیلی:
ایالات متحده منتظر پاسخ ایران به درخواست‌هایش مبنی بر توقف حملات به کشتی‌ها در تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67806" target="_blank">📅 21:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67804">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08bce6837f.mp4?token=ckLHL7a-PGChTYw7sBZGQpBgNY-rRFQMtMEvMKJG1c7DC5g8g1I_SkIzQbjr3KJt1TNxO-D6EONMtxWdT5AjyAYLs8oy7GET6myuqaLanu-g_ujOdikAfIlbs7zG2Ba3NUUh8-qRQoW4gZSEa9J-jgmqfHL9mE2NOmOX4FstrejIfNj1AYUceyqpeLR2YyFaMukXhgLQsK8tDmJyUd8RKVKoNTfUCSUwXIb6PhfXpNZUGwgSKYrcyWVj96RicElZpdIJG-dkRHmou53ZWVT6281uK9hZJXLScPLzRu686jIXfkyB6jntuMM5nV0Tfef-X2kaHMqAvTVKupzC0GioTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08bce6837f.mp4?token=ckLHL7a-PGChTYw7sBZGQpBgNY-rRFQMtMEvMKJG1c7DC5g8g1I_SkIzQbjr3KJt1TNxO-D6EONMtxWdT5AjyAYLs8oy7GET6myuqaLanu-g_ujOdikAfIlbs7zG2Ba3NUUh8-qRQoW4gZSEa9J-jgmqfHL9mE2NOmOX4FstrejIfNj1AYUceyqpeLR2YyFaMukXhgLQsK8tDmJyUd8RKVKoNTfUCSUwXIb6PhfXpNZUGwgSKYrcyWVj96RicElZpdIJG-dkRHmou53ZWVT6281uK9hZJXLScPLzRu686jIXfkyB6jntuMM5nV0Tfef-X2kaHMqAvTVKupzC0GioTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ارتش دفاعی اسرائیل:تروریست‌های حزب‌الله در حال انتقال موشک‌های ضدتانک در داخل منطقه امنیتی در جنوب لبنان بودند.
این تروریست‌ها موشک‌های ضدتانک را به یک ساختمان در آن منطقه منتقل کردند، که نیروهای دفاعی اسرائیل (IDF) آن را از هوا هدف قرار دادند تا این تهدید را از بین ببرند.
پس از این حمله، انفجارهای ثانویه شناسایی شدند که نشان‌دهنده وجود سلاح در داخل ساختمان بود
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67804" target="_blank">📅 20:50 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
