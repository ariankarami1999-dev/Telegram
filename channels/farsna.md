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
<img src="https://cdn4.telesco.pe/file/tL4PrONFlb9XBXACl9nhLr6KAzjkq6VCdCCkcH7jOlK7icl5eRQa78Z9nIl2G9gvgWy5_xUqDwZErEjdZsklDz0_FvQZVJ6yHhbUIdlj91nkMx22XFoJQVKLlDsJc2uRBvOB2VGvvUALYVgOmYu1BKJmkToFem09mWDk_5qaGLN5VxC-bJ9OB6-CdpZMCdI9tPgDgnxtVLLESlmr3_NiTjrnOFlWforThTjZzd_24Xdj7P3riy7xuKfuNfO7t7daAEPcFPzUrruWKnyIgq1ZfQ66h7koA5N_RXI4V1KZeMNdXB_6HOHPrYy5kcRSsrJEEZJECysWtp43X5O8Dn_XiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 21:56:54</div>
<hr>

<div class="tg-post" id="msg-460522">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/348cd28267.mp4?token=gSwzFuljisF0rse_JCYen4tuuT8F1ohNU3wkhMPXZCQauKWbt-Vb3duqryJxTB-PWhgcqjZnr3984QIyEI135T6yd7pA2WxNh0Lt0KpD_ueVQAwyNO019oil3w9dRf1hY5yiGdWgwlWstdnZiP4bBj_eQAAll53_E4xfVF_3b5D3EL-eYJqFqzgezvO6x32G8V0xotusma71_qOtKiSQofaTdZgsKp0py3sM73K4UFUiUeudEuR2Vc2cUE3gmFF3ndXSe65LVT8KreR7wmKvHIVdNiIX04EIYS2V9zfLAciwgmyY9EOWOkguY-keVeE2lDQWG-oqdrXdGj9QZpfB3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/348cd28267.mp4?token=gSwzFuljisF0rse_JCYen4tuuT8F1ohNU3wkhMPXZCQauKWbt-Vb3duqryJxTB-PWhgcqjZnr3984QIyEI135T6yd7pA2WxNh0Lt0KpD_ueVQAwyNO019oil3w9dRf1hY5yiGdWgwlWstdnZiP4bBj_eQAAll53_E4xfVF_3b5D3EL-eYJqFqzgezvO6x32G8V0xotusma71_qOtKiSQofaTdZgsKp0py3sM73K4UFUiUeudEuR2Vc2cUE3gmFF3ndXSe65LVT8KreR7wmKvHIVdNiIX04EIYS2V9zfLAciwgmyY9EOWOkguY-keVeE2lDQWG-oqdrXdGj9QZpfB3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جان‌باختن ۱۱ شهروند سنندجی در آتش‌سوزی تانکر سوخت
🔹
رئیس مرکز فوریت‌های پزشکی کردستان: در پی وقوع آتش در یک دستگاه تانکر حامل مواد سوختی در پلیس‌راه سنندج - همدان، ۱۱ نفر از شهروندان جان خود را از دست دادند و ۵ نفر نیز مصدوم شدند.
🔹
به محض وقوع حادثه، تیم‌های…</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/farsna/460522" target="_blank">📅 21:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460521">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f1f5d2a46.mp4?token=O4yzn99_GzLSozVim-zzo-EaY260LWU6sidDDdmwBF8ljOzM4ZB4brvlXawNUjMTvPOtKSjCkwR_MxaBHOGfep-XAwcvsUIDFTUYwQRLQkBrcxq2hzIfDp_KkjD2MI7AV8SXKkmsSed4aspWbqRAWRXrkg73modhB519NcGcYrhnLgxJe46hEUV22rasG1P2tnsVy4NfbLwgQuyhzFTKeg3Nq0au85MCRbwHnbGOgT8A5x9NXhyAnGIVSOz_ZB7AX3biHXCWbArONeF-oT2iEg2MYkGt_wzL-d4cGidu9kGTyEAyYJR6Pp8bb1Q72YuD1e2hHLwMnXkJj6IUTt5_XpfF6xxf6ENW_cVCezNmXJhXmMZd6s0Ps1Mem6uckHjFwakCfLuhVwP9bnh-HkjIAxaiLKJ-nHJR80ygaQ34Gh0-yqFn5eD2ngfIFySrIV9QMdcNWzw9CHhso8Ou7xDEA8c75GVtW59Lbhz-gWmO18Tdnc52DM4i2hZmS2M3sD9Is3Qy2GN87t99Khvs2itMw-M9MfdzvddzhZeMQRO5TmLQb4_sfMX9N0np62_6EedTR27PPVSWHt_COR0SY-BFvRnI3_eeQ6izYSPzGk3sekuw1ZfQG63802sbfGIITebdVyY84uUfPaWbFhOHbDeEl_Qqd_9tUC0DyL5Je_F3nM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f1f5d2a46.mp4?token=O4yzn99_GzLSozVim-zzo-EaY260LWU6sidDDdmwBF8ljOzM4ZB4brvlXawNUjMTvPOtKSjCkwR_MxaBHOGfep-XAwcvsUIDFTUYwQRLQkBrcxq2hzIfDp_KkjD2MI7AV8SXKkmsSed4aspWbqRAWRXrkg73modhB519NcGcYrhnLgxJe46hEUV22rasG1P2tnsVy4NfbLwgQuyhzFTKeg3Nq0au85MCRbwHnbGOgT8A5x9NXhyAnGIVSOz_ZB7AX3biHXCWbArONeF-oT2iEg2MYkGt_wzL-d4cGidu9kGTyEAyYJR6Pp8bb1Q72YuD1e2hHLwMnXkJj6IUTt5_XpfF6xxf6ENW_cVCezNmXJhXmMZd6s0Ps1Mem6uckHjFwakCfLuhVwP9bnh-HkjIAxaiLKJ-nHJR80ygaQ34Gh0-yqFn5eD2ngfIFySrIV9QMdcNWzw9CHhso8Ou7xDEA8c75GVtW59Lbhz-gWmO18Tdnc52DM4i2hZmS2M3sD9Is3Qy2GN87t99Khvs2itMw-M9MfdzvddzhZeMQRO5TmLQb4_sfMX9N0np62_6EedTR27PPVSWHt_COR0SY-BFvRnI3_eeQ6izYSPzGk3sekuw1ZfQG63802sbfGIITebdVyY84uUfPaWbFhOHbDeEl_Qqd_9tUC0DyL5Je_F3nM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور مستمر مردم مراغه در میدان دفاع از وطن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/farsna/460521" target="_blank">📅 21:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460520">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a512e5e02.mp4?token=HHJfzsWuKmW4LxbiGf_VPpRFNTmZI6fFoMxMQI-V9oWASygCUnEJ4ecQu_MJP86UPx0kLKKLzQAvm1spSWUsLdatEXj0uMjzziXWl0ICDqtu7nID5akj7GKLU4BNqX3ZuONeYZoTSG9uIlrUlRXZ9V3-GS8lNDthmOzoI8kgX487aKD6JoZE3YPWKI5Q_I0j-svEbIuxdnoFydg51S8VR-kXDjmGyI8NJc0bz8XvVll3nbC3Wf--ZCqQfD8CJaPC0__sxjThLVMmUeZNF7PqBf-QvTbgnsIxqmWXoDxeJvfV40B1u28lTJBaOTAKvdSCaB89sNbigrADFjSwudJ4Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a512e5e02.mp4?token=HHJfzsWuKmW4LxbiGf_VPpRFNTmZI6fFoMxMQI-V9oWASygCUnEJ4ecQu_MJP86UPx0kLKKLzQAvm1spSWUsLdatEXj0uMjzziXWl0ICDqtu7nID5akj7GKLU4BNqX3ZuONeYZoTSG9uIlrUlRXZ9V3-GS8lNDthmOzoI8kgX487aKD6JoZE3YPWKI5Q_I0j-svEbIuxdnoFydg51S8VR-kXDjmGyI8NJc0bz8XvVll3nbC3Wf--ZCqQfD8CJaPC0__sxjThLVMmUeZNF7PqBf-QvTbgnsIxqmWXoDxeJvfV40B1u28lTJBaOTAKvdSCaB89sNbigrADFjSwudJ4Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا و یک رسوایی دیگر؛ تسلیحات کمپانی ریتون در حمله به عروسی سیریک
@Farsna</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/farsna/460520" target="_blank">📅 21:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460519">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4d1a7eb67.mp4?token=RClVfprpf-W0PhIp5CWG29zR0rEK_ZsabT0_9W_EOM9WxeMMV-_n1dPD7rjc4-YhNZngzoVmt82LAUtQHB7k5RFptT4oZJ4rGW5v4K6jnPKXQmxvqL5IHZ21mnzOmh4d47rog45R9-OKUBSmqAd1qV-WYjmrvkAWT7snYcP13N4MMvlKEwh58jCi-15bu5JjFEs7JrjHiASFkYhZgqz0GBjjOZ36Yol9QAetD5kajv8EYrRIWESUr2vHhSP4GwEvGdFZPy-WE5GhkMnRk14zSgNKOMM1no1WFE8T673LuYtPIgl-rQKsMur_ReyRRxQBCOg4_RUXm6eSWcM3sLCPWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4d1a7eb67.mp4?token=RClVfprpf-W0PhIp5CWG29zR0rEK_ZsabT0_9W_EOM9WxeMMV-_n1dPD7rjc4-YhNZngzoVmt82LAUtQHB7k5RFptT4oZJ4rGW5v4K6jnPKXQmxvqL5IHZ21mnzOmh4d47rog45R9-OKUBSmqAd1qV-WYjmrvkAWT7snYcP13N4MMvlKEwh58jCi-15bu5JjFEs7JrjHiASFkYhZgqz0GBjjOZ36Yol9QAetD5kajv8EYrRIWESUr2vHhSP4GwEvGdFZPy-WE5GhkMnRk14zSgNKOMM1no1WFE8T673LuYtPIgl-rQKsMur_ReyRRxQBCOg4_RUXm6eSWcM3sLCPWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا جنگ با ایران را کوچک نشان داد؛ هزینه‌اش اما سنگین تمام شد
@Farsna</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/farsna/460519" target="_blank">📅 21:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460518">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1afab8392c.mp4?token=tt3gHbUJJZA8qnBXvyro0wu5qLT-98ObibPZtgqYn5tUymxka1tF1nvb2X0WxYgIXAAWZwaGAwbSs3hCAinTAOBYRPphBNHCfkW88U-Ci59waDFzJz66I0KJUSPV6u2Z-dzZzietrda1DpFz1JhUzj_5t7TPLbZ3FPdYJzHVeYaD4MNuDnIPwz03xOTeAXPhh0Rn2sn6eb00hoXo7aQ2Dp6sd3QFA54DQwjzWpFQdnoj3OiFkSokaLODyvr6dTWDXHmvpMx2WPZbPqfwh1ob5ZH8k73z9PsEV3ncDVEkd7dF8RLYQGsIXD6SanqBQbTnDEa9_sHRih_bDZ2tLbbaKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1afab8392c.mp4?token=tt3gHbUJJZA8qnBXvyro0wu5qLT-98ObibPZtgqYn5tUymxka1tF1nvb2X0WxYgIXAAWZwaGAwbSs3hCAinTAOBYRPphBNHCfkW88U-Ci59waDFzJz66I0KJUSPV6u2Z-dzZzietrda1DpFz1JhUzj_5t7TPLbZ3FPdYJzHVeYaD4MNuDnIPwz03xOTeAXPhh0Rn2sn6eb00hoXo7aQ2Dp6sd3QFA54DQwjzWpFQdnoj3OiFkSokaLODyvr6dTWDXHmvpMx2WPZbPqfwh1ob5ZH8k73z9PsEV3ncDVEkd7dF8RLYQGsIXD6SanqBQbTnDEa9_sHRih_bDZ2tLbbaKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۷ شهید در ادامۀ حملات امروز اسرائیل به جنوب لبنان
🔹
در ساعات گذشته حملات وحشیانه این رژیم به روستاهای جنوب لبنان ادامه داشته است.
🔹
وزارت بهداشت لبنان گفته در حملۀ پهپادی صهیونیست‌ها به شهرک النبطیه التحتا ۳ نفر به شهادت رسیدند که با احتساب حملات اشغالگران به مناطق دیگر، شمار شهدای جنوب لبنان امروز به ۷ نفر افزایش یافت.
🔸
این وزارتخانه پیش‌تر اعلام کرده بود که شمار قربانیان تجاوز اسرائیل به لبنان از ۱۱ اسفند ۱۴۰۴ تاکنون به ۴۳۶۲ شهید و ۱۲۳۷۸ مجروح رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/farsna/460518" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460515">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63356e20d1.mp4?token=JogJNAI6LO7p06MbWbM3Dznbc2I2igP4xHfdOii4r5h2hvgZyFk3a627RETvc8xdM82cKe4QcvqcVAJyUqUrtLwvjnzqILRSO_SZG2PT7b_thY81cWdLaeOqPK1EPtiT01QH0K8Zz821Wp_F9NhpCm5sxfCN8XiI4TaTNVys9lsX-3jmADs24gFE5WltYTxCPyQD-MajLkli4ELwvaQ4MzYRwkQ2LgS_cefvIKLkO_z-rvE89pjNvgFwUTiaT_aaX_-jLfxsTJZdJUGtwL921cwMiMUh2XtOhrU2wB14x8izj3ZCqy2WfNtD6hv-T0r0ct1TsSVrgvwrQLLW2HF7mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63356e20d1.mp4?token=JogJNAI6LO7p06MbWbM3Dznbc2I2igP4xHfdOii4r5h2hvgZyFk3a627RETvc8xdM82cKe4QcvqcVAJyUqUrtLwvjnzqILRSO_SZG2PT7b_thY81cWdLaeOqPK1EPtiT01QH0K8Zz821Wp_F9NhpCm5sxfCN8XiI4TaTNVys9lsX-3jmADs24gFE5WltYTxCPyQD-MajLkli4ELwvaQ4MzYRwkQ2LgS_cefvIKLkO_z-rvE89pjNvgFwUTiaT_aaX_-jLfxsTJZdJUGtwL921cwMiMUh2XtOhrU2wB14x8izj3ZCqy2WfNtD6hv-T0r0ct1TsSVrgvwrQLLW2HF7mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایگاه علی‌السالم</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/farsna/460515" target="_blank">📅 21:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460514">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/108b3f80c2.mp4?token=XG7LejaeibHNtlfvfOkMVBtl_WcC_MtlkHEOWBgcY7fqC-16_SOPK4qmjb4kntyWqXlVKCjrIr-n27TeUQC2ImWSu6KQgLep3Hv3zNDLYBZxZgAuNxfnsp44a8J4ZuWuyGWguyuOdmNgkvibVwLpboxeib8GHLbGWWM81TU1S_38w-IGjqoZmZuqe-r1KaByJEHA_DO9NyAey2IJ1XQOz_LKBnw6bu_I2B3MnXeHbvzj6rJodyMxJ5i3k17coMITZzErRz-c_-Y1qYFEU2wjLcftdnz5FVDsqtQ3sy-i6k7VH3CCWYSuwe0LGN-0jzwzPmxM2qC6X1NsH_l-Y5gUSgz73P9Fh4x0Y5Lfslo4YgxaUKJNydjBf28N54CanicvFpeARSFo-yPSkxyZlwh_gwvlpyEy6zgpYOLA--2FctUoqG3xsvo9o54s9jPKJk-tQV8GNCuiyYvMqN3E7k0AqxIvqR1i2wdvka29KszDoOxml7UWBBBOIfFkxH54P9JQjEx3hkLAR7xLVyCuPFLSAtnvyAN6_l7E0IhcygbdTbc4KyFA4CYuvE1EpIcDrNRqkCkr8_dw2Dd1z6_KEf_7bVITyBdxNDOeaVezHign7B6oiD3QrhR75PeARCY8NnYRpO0A1SoA2aBtW0rI2KzQAUpnIR0zsa8rKSn1AIEICcM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/108b3f80c2.mp4?token=XG7LejaeibHNtlfvfOkMVBtl_WcC_MtlkHEOWBgcY7fqC-16_SOPK4qmjb4kntyWqXlVKCjrIr-n27TeUQC2ImWSu6KQgLep3Hv3zNDLYBZxZgAuNxfnsp44a8J4ZuWuyGWguyuOdmNgkvibVwLpboxeib8GHLbGWWM81TU1S_38w-IGjqoZmZuqe-r1KaByJEHA_DO9NyAey2IJ1XQOz_LKBnw6bu_I2B3MnXeHbvzj6rJodyMxJ5i3k17coMITZzErRz-c_-Y1qYFEU2wjLcftdnz5FVDsqtQ3sy-i6k7VH3CCWYSuwe0LGN-0jzwzPmxM2qC6X1NsH_l-Y5gUSgz73P9Fh4x0Y5Lfslo4YgxaUKJNydjBf28N54CanicvFpeARSFo-yPSkxyZlwh_gwvlpyEy6zgpYOLA--2FctUoqG3xsvo9o54s9jPKJk-tQV8GNCuiyYvMqN3E7k0AqxIvqR1i2wdvka29KszDoOxml7UWBBBOIfFkxH54P9JQjEx3hkLAR7xLVyCuPFLSAtnvyAN6_l7E0IhcygbdTbc4KyFA4CYuvE1EpIcDrNRqkCkr8_dw2Dd1z6_KEf_7bVITyBdxNDOeaVezHign7B6oiD3QrhR75PeARCY8NnYRpO0A1SoA2aBtW0rI2KzQAUpnIR0zsa8rKSn1AIEICcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وحدت، رمز پیروزی مردم ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/460514" target="_blank">📅 21:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460513">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7daee69212.mp4?token=P9HBGvbAIkt8H3Zf6ImOEhRFqa3qwJRPbiSfvCrj-0XYTnuz7PqI1tamljG0xVZnIIo53b0-aaJQmvUdesGDGs34_A8JbzwUMUX3nn23_87UT3XNn2uHXRx59iobNvJyvX0kiI92YbUdjtFWW4yhhiPKJGhIaHt2oj0gvRCEMuzagD9r4i950wTquWF71SK7l0G7fVwXQTvpFIuISMIp_oCP0DbMhiHaR6EzqRquHmI5zDo_0xrIMNI-C8UCqHz2ASwssiQLd6sJMXt9auGpzXrNO4QKv-AvPxuOKh4zTlXnj3VPD1nUIcitd44kzKplwA7Wmr9kd0cHjjg6S5u0OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7daee69212.mp4?token=P9HBGvbAIkt8H3Zf6ImOEhRFqa3qwJRPbiSfvCrj-0XYTnuz7PqI1tamljG0xVZnIIo53b0-aaJQmvUdesGDGs34_A8JbzwUMUX3nn23_87UT3XNn2uHXRx59iobNvJyvX0kiI92YbUdjtFWW4yhhiPKJGhIaHt2oj0gvRCEMuzagD9r4i950wTquWF71SK7l0G7fVwXQTvpFIuISMIp_oCP0DbMhiHaR6EzqRquHmI5zDo_0xrIMNI-C8UCqHz2ASwssiQLd6sJMXt9auGpzXrNO4QKv-AvPxuOKh4zTlXnj3VPD1nUIcitd44kzKplwA7Wmr9kd0cHjjg6S5u0OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ناوهای آمریکا دیگر رنگ اقتدار نمی‌بینند
@Farsna</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/farsna/460513" target="_blank">📅 21:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460512">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
نرخ سوم بنزین ۱۰ هزار تومان شد
🔹
سخنگوی دولت: نرخ کارت جایگاه سوخت از بامداد سه‌شنبه به ۱۰ هزار تومان افزایش خواهد یافت.
🔹
۶۰ لیتر بنزین ۱۵۰۰ تومان و ۵۰ لیتر بنزین ۳۰۰۰ تومانی بدون تغییر ماند؛ افزایش قیمت نرخ کارت جایگاه صرف معیشت مردم خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/460512" target="_blank">📅 21:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460511">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4bd29631.mp4?token=jvltqJqF8_OksRw4XPO3wz8xXnC7BMrS84sDiaQBZNL5eQ8TuKx20KykwMiXpWgQbkuyk8uBJDZqccBxGkqnw2zIB4YMt92hTEyfUhFKU6MknPuFGcu4OPE-MIcX2A3mrjmuU-rs3Bq1O_GRgn7IlE7Sd5c9NxFM7ysE-FTcV6x3YD_5aI1zkcjTbiRmwLaqjgQKsudR5t8zTy97dizt43ACW_aB9DFeDt9qRS1464l2PzIjW9i3WPY_r-DS8_2a2PuCPy3RhmK7ZvlgtczydsbG4Msx3FSXG5mexu1EHcmrsMNbNf4Ic6YJ5rTgMMIkjhadXiu75WsDYiSihgs11WO68hWngOro2qEBAOohEpAJx6H_4YHT8y4-aEVLnGFkjoIN5R7J418Kvsl5TD6O6Bn2v3yKEk0SP7zHW7XeXQQw0ilR75cscUYS43T2fEF_4UnkPie2nAMvbqXRIAYX_hSSZZSerISGJ5DDWxpAgFlwuB0n9HaWC65OsLoOmhbwcir_iC2v-4FaBzG_pQRLFxqM9NkxYTU2gXxrddV4fbbx2SdU3XKy3t-gV-VrApD9zRNgp_b_QbDUrZd8u6VC4c6dKuufi7K6Duf-QRyxGKtRVIU985chK-CSF3hYW9htUNrJGxo39zOSAno9Mdeo4H64RE9gxAlcSxtdtwAfEBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4bd29631.mp4?token=jvltqJqF8_OksRw4XPO3wz8xXnC7BMrS84sDiaQBZNL5eQ8TuKx20KykwMiXpWgQbkuyk8uBJDZqccBxGkqnw2zIB4YMt92hTEyfUhFKU6MknPuFGcu4OPE-MIcX2A3mrjmuU-rs3Bq1O_GRgn7IlE7Sd5c9NxFM7ysE-FTcV6x3YD_5aI1zkcjTbiRmwLaqjgQKsudR5t8zTy97dizt43ACW_aB9DFeDt9qRS1464l2PzIjW9i3WPY_r-DS8_2a2PuCPy3RhmK7ZvlgtczydsbG4Msx3FSXG5mexu1EHcmrsMNbNf4Ic6YJ5rTgMMIkjhadXiu75WsDYiSihgs11WO68hWngOro2qEBAOohEpAJx6H_4YHT8y4-aEVLnGFkjoIN5R7J418Kvsl5TD6O6Bn2v3yKEk0SP7zHW7XeXQQw0ilR75cscUYS43T2fEF_4UnkPie2nAMvbqXRIAYX_hSSZZSerISGJ5DDWxpAgFlwuB0n9HaWC65OsLoOmhbwcir_iC2v-4FaBzG_pQRLFxqM9NkxYTU2gXxrddV4fbbx2SdU3XKy3t-gV-VrApD9zRNgp_b_QbDUrZd8u6VC4c6dKuufi7K6Duf-QRyxGKtRVIU985chK-CSF3hYW9htUNrJGxo39zOSAno9Mdeo4H64RE9gxAlcSxtdtwAfEBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا آمریکا به جنوب ایران حمله می‌کند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/460511" target="_blank">📅 21:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460510">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJCkSmyOQRhRXpjC90fr7GWP68tohQ00r4AoDfCU9FBFDblD7AhUb-Nz5076kbabcjsGHhYkOgsLoCJpDwMc8nwtoUwz374Vjj9QubO1lRPkGnM2ibOgfaDyE9XZ1h9SbMDF5RoKDV-DZWDI0q7vrI-IgjuEYpFGmpVYbQAo-I-7Er6Ibh6FgGTjEx5tc_7Q2NVYjUN5J4PJamumszP1Mr67OAhRELQW1MTcMcLhdmVGf-35mC1cilFrDDL0CtlHPDjKR_QzcDtqXycikJswPfU8P0uM_InlCsoERXnG3kyn33VzkHsx5ZDhDh4l2d2O_cFoyQrDM3emXla7jW1vGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سومین مساوی پیاپی استقلال
⚽️
آلومینیوم ۰ - ۰ استقلال
@Farsna</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/460510" target="_blank">📅 20:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460509">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb438e094.mp4?token=SaqTYzHuZAkElGRBAEH0g74hU99VNtxkHZwBoCaXTy6-Mww6puULo9K9tRCHLpMaWqvudHQjiAavUgzvVW2GHC74bols0rjz7t2J2k6H1YhB-tRkrYSVTpI40r9rETklQ6B2SKIq31OMs-pfZ2VkFCT143opHrye_siboHy-YDyiCe4kyNvvwZNexL7Zzz-hs_PWyVSczztMToSskM4G5f7BVjTdU5XNoEIlplWh97xA6MjGN_Pz5FophqLw5V2pns5CoQxFxbVUvUy5lpmxpXHip8pfKXkhD_3lQTZdCbHZopGdhKtX0PeGYZN1ahf7skNqg53iLu9i5RI91ILtLoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb438e094.mp4?token=SaqTYzHuZAkElGRBAEH0g74hU99VNtxkHZwBoCaXTy6-Mww6puULo9K9tRCHLpMaWqvudHQjiAavUgzvVW2GHC74bols0rjz7t2J2k6H1YhB-tRkrYSVTpI40r9rETklQ6B2SKIq31OMs-pfZ2VkFCT143opHrye_siboHy-YDyiCe4kyNvvwZNexL7Zzz-hs_PWyVSczztMToSskM4G5f7BVjTdU5XNoEIlplWh97xA6MjGN_Pz5FophqLw5V2pns5CoQxFxbVUvUy5lpmxpXHip8pfKXkhD_3lQTZdCbHZopGdhKtX0PeGYZN1ahf7skNqg53iLu9i5RI91ILtLoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تروریست، تروریسته چه تو یک استودیو شیک تو لندن نشسته باشه، چه در روآندای آفریقا
@Farsna</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/460509" target="_blank">📅 20:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460508">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWKx3Igp1BpVnKD-oOxPprmh0fnozOSTLcU7tiPkr-zaWjNil2tn7TbJ1KuwoPkXLCoycn6AnjBLPaVDHipV8pmwI5pHggHrEua4Tzg4IMHZVBOSQrlKbHdP3nMZYOLQoUiWqZXqH9jef8bRRaJeSbTYWR7PEoAs0k26DC32o39W3tAVheRxh-4PL_B7Aw4wcI4y3d6KNtgIY-uwt-Plq95UlVtqJf_k0ruN5eQSwLNmEXV8B51EDN71P4pLRxUIWqOMsPagepGHJ8mEsLem2pElAjCe_ir5NYSnYyioPMkLniRB8B8IrSvazFjOshfTi-fW6BR3OtryDfABcks-iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی خطاب به ویتکاف: بیشتر به اینجا بیایید تا اوکراینی‌ها بتوانند بیشتر زنده بمانند
🔹
رئیس‌جمهور اوکراین پس‌از گفت‌و‌گوی امروزش با ویتکاف و کوشنر، نمایندگان ترامپ، از پایان دور نخست مذاکرات با هیئت آمریکایی خبر داد.
🔹
زلنسکی در پیامی که خطاب به فرستادگان ترامپ منتشر کرد، گفت: امروز شما حتی بهتر از سامانه‌های پاتریوت برای شهروندان ما که در پایتخت هستند، عمل کردید.
🔹
متشکرم؛ بیشتر بیایید. این‌گونه مردم ما فرصت خواهند داشت که کمی بیشتر زنده بمانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/460508" target="_blank">📅 20:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460507">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d29d757f18.mp4?token=VW6K7pzjPnnHHZyxRwwXGylmaVdqvuu7jbqHNhha0IsXvM9C236GK6B5ZGf80-Uw0nzWvO6Shg5E4iH1PxyUcpHmXkjZQASPMPCrmND3zcX_VLvv6plUA1p-oFrQNLbY0miILMZoQQWq5AkvAsEOEi1FpMTVRQqCyaFsKY66iefXGZoTkUYmcEUfPZo--Lk_EzSD-dZ_WD8lPGSk8gi1COyvFMmHPNz2XiaCox05DvBGJo1BPXYDe2e2tBtdvwxuaOgW1sHM2LtEzeJA0anrl1yk6YRopi9oViTgze-3PMREh4zvbA4BAL5IMoSRcQphbeTqGMwyYS5muaVBhMwMSBxRXxVDLSC_R1GkVTE9DzzXrcveorMWC2HVfh24ee4AS6N3S-VgOkDqoMIOmwvBQJLpTWCm_mSXYHb7tgpa2wSC7MjHUkqxdObb3OpbnDD93u8n1dVLNLcA8BUrfR5bJ65pFjXu_D48U2swoQx_h7YvUqJHUN1Tmugh8r6qLJVCELK_OmbbmfSpDejlepnSHrK-C7Xu-lIRFsH7aIWhr23BrXHG-r8RWQifWppl1AQvzzbZNmwAWq0ddicnx17EB3Nc_r-8ZsbMsJ2Zc8EaX9Knsj9n3kB-8x2g3lw_n6T1v0QRVg_QhE6wWS1und9_yGv9prmMQYcYAG5M_6YHeVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d29d757f18.mp4?token=VW6K7pzjPnnHHZyxRwwXGylmaVdqvuu7jbqHNhha0IsXvM9C236GK6B5ZGf80-Uw0nzWvO6Shg5E4iH1PxyUcpHmXkjZQASPMPCrmND3zcX_VLvv6plUA1p-oFrQNLbY0miILMZoQQWq5AkvAsEOEi1FpMTVRQqCyaFsKY66iefXGZoTkUYmcEUfPZo--Lk_EzSD-dZ_WD8lPGSk8gi1COyvFMmHPNz2XiaCox05DvBGJo1BPXYDe2e2tBtdvwxuaOgW1sHM2LtEzeJA0anrl1yk6YRopi9oViTgze-3PMREh4zvbA4BAL5IMoSRcQphbeTqGMwyYS5muaVBhMwMSBxRXxVDLSC_R1GkVTE9DzzXrcveorMWC2HVfh24ee4AS6N3S-VgOkDqoMIOmwvBQJLpTWCm_mSXYHb7tgpa2wSC7MjHUkqxdObb3OpbnDD93u8n1dVLNLcA8BUrfR5bJ65pFjXu_D48U2swoQx_h7YvUqJHUN1Tmugh8r6qLJVCELK_OmbbmfSpDejlepnSHrK-C7Xu-lIRFsH7aIWhr23BrXHG-r8RWQifWppl1AQvzzbZNmwAWq0ddicnx17EB3Nc_r-8ZsbMsJ2Zc8EaX9Knsj9n3kB-8x2g3lw_n6T1v0QRVg_QhE6wWS1und9_yGv9prmMQYcYAG5M_6YHeVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در پاسخ به یک سوال بنزینی اینگونه پاسخ دادند
@Farsna</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/460507" target="_blank">📅 20:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460506">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305ff823b4.mp4?token=Zbq7GMEsQG-p-zUzgoCeo6Ye8OFfVqFD01oYErlkZfN3FqVYHsqsPE_lDv8irJmqCz6KIeChdKQXReTI3327LjaKFu3WcKb-9PzRcxyP0k-o_Gy4mtA8pqxVLYYZF9a89j5L2Jg8r1zt4HDU_r0Q6FerhuIedsSdBCYWT0z8ma34a5P9PT0v_93xA0jKW-ZBw_A6cqdZqRjITmbcOTKKrUgx-sCsr1i3eYSrcEviDR7Dj2F_Y6P1g4L2tGe9zecGmEMKglbSOWkWdA--HBtmUsdDrQsOlkrttWTYQuO_vbkHPDrEXbw2VqERxoygDc5KN4JxuaUYBif3RbXMijIt1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305ff823b4.mp4?token=Zbq7GMEsQG-p-zUzgoCeo6Ye8OFfVqFD01oYErlkZfN3FqVYHsqsPE_lDv8irJmqCz6KIeChdKQXReTI3327LjaKFu3WcKb-9PzRcxyP0k-o_Gy4mtA8pqxVLYYZF9a89j5L2Jg8r1zt4HDU_r0Q6FerhuIedsSdBCYWT0z8ma34a5P9PT0v_93xA0jKW-ZBw_A6cqdZqRjITmbcOTKKrUgx-sCsr1i3eYSrcEviDR7Dj2F_Y6P1g4L2tGe9zecGmEMKglbSOWkWdA--HBtmUsdDrQsOlkrttWTYQuO_vbkHPDrEXbw2VqERxoygDc5KN4JxuaUYBif3RbXMijIt1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر بهداشت: شهر میناب دچار سوگ گسترده شده است
🔹
تیمی در وزارت بهداشت مسئول رسیدگی به آسیب‌های روانی جنگ شده است. @Farsna</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/460506" target="_blank">📅 20:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460505">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b0f21f01f.mp4?token=GnIjtHZhnf-iU8IqQAhxz2UCA--XNtmpRCIVIaLUkGnkxNKAn-s8AtRJuhGotbLmNF5NCFMThAoYda-366HjwAHzOswaSZ70gsDCWglzVwVlAO1L10SEDkKllxiw3nt-1ksJxA_CjHhSq0sADEjdpCfPVPfkzHuKgz3sHWF-sKs-w9Kre8-MTaIaOQ9ooIloVhTRzeaXN-seC9GuOTp3Cm7Pl3MKGCWpZuihK5nCPvJmg1dpM_wZtQ1HQopm6l1e3q905SQYlt5BHuRw-UeNxOSFhOqpBmgY29cSAcAwAsr9Ihujfbn7khOj1sn0dsq8c_TjZ03i_Tg9VdM53UOX1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b0f21f01f.mp4?token=GnIjtHZhnf-iU8IqQAhxz2UCA--XNtmpRCIVIaLUkGnkxNKAn-s8AtRJuhGotbLmNF5NCFMThAoYda-366HjwAHzOswaSZ70gsDCWglzVwVlAO1L10SEDkKllxiw3nt-1ksJxA_CjHhSq0sADEjdpCfPVPfkzHuKgz3sHWF-sKs-w9Kre8-MTaIaOQ9ooIloVhTRzeaXN-seC9GuOTp3Cm7Pl3MKGCWpZuihK5nCPvJmg1dpM_wZtQ1HQopm6l1e3q905SQYlt5BHuRw-UeNxOSFhOqpBmgY29cSAcAwAsr9Ihujfbn7khOj1sn0dsq8c_TjZ03i_Tg9VdM53UOX1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر بهداشت: در بحران‌های اخیر ۶۶ هزار مجروح را رایگان درمان کردیم
🔹
در جنگ رمضان ذخیرهٔ خون ما ۳ برابر میزان استاندارد بود. @Farsna</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/460505" target="_blank">📅 20:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460504">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72b058a2a7.mp4?token=CQtwI9zN6Mq0R8jKrUX-6ylpCI9k9AZGrrLP-ulg_7VZzlk1ZPY6iVtzyC7W1qUFmRA6UgfRwf60jKJgt9bSrk7UA5trqUE_V4LagMeVdbjEbpBaw0PHaxS_mL-q_V2ststaKKSdeC0dI-hNeKAKSCxbH55En2owGrkbEHUnUvzzlJkoy_hIPnON9rrt6CqRv1yp9b6ytlTnJ9uyKa6exWurt23_Jee7aaOKYV0QAPMjtShOWkwKQvoYPYfeJjaTyBM6mkJtalW8KmhVE_n3OGvLWCdBgqVvv5R86iSPZBoc1sU-zEbSWNNDecIf4T5zaTwupdps59aql8eqBZG7jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72b058a2a7.mp4?token=CQtwI9zN6Mq0R8jKrUX-6ylpCI9k9AZGrrLP-ulg_7VZzlk1ZPY6iVtzyC7W1qUFmRA6UgfRwf60jKJgt9bSrk7UA5trqUE_V4LagMeVdbjEbpBaw0PHaxS_mL-q_V2ststaKKSdeC0dI-hNeKAKSCxbH55En2owGrkbEHUnUvzzlJkoy_hIPnON9rrt6CqRv1yp9b6ytlTnJ9uyKa6exWurt23_Jee7aaOKYV0QAPMjtShOWkwKQvoYPYfeJjaTyBM6mkJtalW8KmhVE_n3OGvLWCdBgqVvv5R86iSPZBoc1sU-zEbSWNNDecIf4T5zaTwupdps59aql8eqBZG7jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر بهداشت: در بحران‌های اخیر ۶۶ هزار مجروح را رایگان درمان کردیم
🔹
در جنگ رمضان ذخیرهٔ خون ما ۳ برابر میزان استاندارد بود.
@Farsna</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/460504" target="_blank">📅 20:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460503">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKc_fekdHYuLhCWFlZNQ5CcRdctyjCr7JO7tjXztOEG_MfEghRPMuRdT2H_9wUjrr7Pk-v9D_sNnjOwFodmjFz2vJgsmaWD44CQ5YmOgY_kTQ_1F2Yva7pcW5nZWWQNttknN8u4Dfjiu7CeJk_11gZY2o2kUtpB8viJzqyM66qsicWTKH6B7AYzuIbta61iXUamQiy5342-zztfCkoM3dSJsbSKR3EvW28L9QhUPuzIKW37LtuD5Wmb5RSKjsHS6D58ShebE9yV86p-6EQ63aXoC0lXuyo-bb_kIAQrsMTG1jeySS1VxpgYDuypCLzwwafL1blsHXo2wQ4k_IZOUIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرعه‌کشی ۴ محصول سایپا انجام شد
🔹
در طرح فروش فوق العاده، سایپا ۴ محصول چانگان CS۵۵ پلاس، سیتروئن C۳ XR-V۱، کوییک S و سهند S دوگانه را عرضه کرد.
🔹
فروش محصولات سایپا در این دوره از عرضه در قالب ۳ سهمیه متقاضیان عادی، طرح حمایت از خانواده و جوانی جمعیت و طرح جایگزینی خودروهای فرسوده انجام شد.
🔸
ثبت‌نام‌کنندگان با‌مراجعه به
سامانهٔ فروش
می توانند از نتایج قرعه‌کشی مطلع شوند. نتایج به صورت پیامک هم به برندگان اعلام می شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/460503" target="_blank">📅 20:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460496">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MxNvdzpFYztpHKCHl05-UfPf5PfwDe20thgHm6-7mN95BkrZk2iv09OmaFGDRzh4UB2Rf8jVskn8Z7XWC6WQCT6xpSV46vfSMLyzDTXsj67c9BYl2xqyfNNszIh281rkZsKm4_wxIknfW3zPOtJnEUyaSUgXSm7-D3YGDFPwsWOIdpNGh5_FZNHDNhode0_AujVlVN6qkfnDWuR4ir0o1WlJYXB0cVkQXhRe_PSxSAkH7yHQ7j3FqyskRqaudQ4VPgRZlS9QakOEHjj5GtHg7PhGsrEkEyNDTIEIlhmb7Sy92rtVYl2QHsH-2CJ7AkZW3wlHvSNfZP1ChNDr9jgxxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tpEBzQdNGinBTLe3uvuAiWezuSEFrHj4taYCgDRom6KcQG6W8nIvAfelzKnL0pYIT63m8juUkyBdpZ1-7SjxxcIGDBBBQ8RgE0QaS4ZOW_Prdc0v6JpfnUuvVUkx5cnmggrzc9CEKEplCHixt3yTRRM_3JgLxVF7rv4i9-uDxnDYUvPJwSggAHyN48acLzL5iZNGMKTeaST2hDZttU0CFDap0N7maj-eZiIgOyb9xzby_Z_iNY6FsyF5DbNfUduOiPYo-ZL1vHnbZDqHcIe553YURtEYHp3gXLpxNJwyGFRNeDuOwSS_0GJEpqKiNZBQyHwZ8BSFzUV78RbNU_YASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FJtlE7GhYvgi9qULTWzOk7yzogTgqnTgxtCLR1O5uW0tq74pD-xpJ7OCsMVe8APZfffioK046k3gVAPO6HmiHVOVMdMe7ZOwzkvUN9tTbBfJfqaEQCohpCEWQGcOtRCMvHLDc965wKYphJHZn9zOexoYIQXVgp78fNmQvzaLSxdkyZQ88wUV5ewSDPQlCqIIvgHJInSYbhMcfwrR45pvnNfWNwfyqe39jY75vnxS5UkofxTHcJ8k3gvybC_hOIpiahPMxJ_Q5Zzx3JK1CRJP_8UVJHed6L-M7ru4Cr__wZ64r5m0s-XkC2zULErNRgta3TCAljDlTZsb4NjAPnyMkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/us3UXMdQ4RJqrT99wGtOphZh2fBeYCXOe8ZfdpO2HCmwusr9Es1SuIvaXVon9pvZv-5Ds_pV1M684iP3Fd-gzHL2upUtGeFLHar_MokFyl8nYzieHF8qkRAeaSbT_riXnma9ad6gP4-eg7YCJ8cY7tMxE4ZMPjTCcFZ-Nra77aXawxFZzAgHgFE-J0SBI_bDzHkmDcG8IQBVLCykVM05SWba8qM8uDvMFBeTlEpyaglHpIUg9-p8wRVDDuILuLVPVuGfrZSW2VWkA6gqIZHP4CAs0g4NN_riOKZ1HdEPtOvKg8Qh_FwUIxpSAAFGeW4LEfPG9mZuPwrYKbQU-PpvJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/otGyLUt600hJ_X2xHh2maCjlA7EL5fu_KqKij0yOYd_p8xIsc4xhl_52aheldAYeFsEFyewNM6Eat4HQNbYVIFBBHMQVLwgURH2zjIKDmPbvlbbjlyaxqQtMRtyvEEQC5pG3cuKIZ4Bs61LnR81eLHqCBsgt2R82Aer_AeqgaYdI1_WX5HACrvmp3HYe7zTj5qLpJHCFDM9b1jbcEj787FCvp9SBq-KqjssocnQ3T656QDuN4yxK_GaT-e55Bq6cACAjVmm8FDig-gCAGWFxFy8WqYAYVUxk-boly7bY30vy8XBLZ9AWEnWOmBhS0z7d4WxnO6g29gBLB95ThShkmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFNH_VgfYE-_J8LiudA8txmJz4W_pYiIGq37IBsNz27jneXwhdDc7bKMLX0jobPVS4vslRS2RbXD2twEBbf-4tCpJ59Il6XRrj-DeZWErdSxS6uUz9AqmWYc09jTUJICj5CMF4FivKHMEQHEmHtF9aG4oqGQ_-pZUhjEnqNjUPBFPzq90smEPR3bwHhGkqXENjHO9olnpdKFCXZGSdP0CCHylhyKdu9OumrlnjLfRKWWORmeNW1tuo65Fql-ttWYw6OP8jIe8X1R9Q4F8BViRE1a7WGJDV9TCh6bdx00zbas-coMIy_4SrQ98doOzmRNZsit8IjSKM-CHGH9p2EDnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ouGRaiPlNko36B8cWvIuMsv-P5j6n__JY7dGjfnjh8amnYUktx-uP0yi-GBc8hpJATxIVMEi5v0E7lfejBDeE9P9I7JzCkXg0lX2PIUdbW3666WqVCaMmXexAWRPM4uC4YCwIhW5oI9gv3ZB_m50GLPfuuY16ruxB4GcUzs1ninxhX4yy730fbzdWdAzAf5rta-S4OY1FPy6-vVx5hN6psK1s5LWYsHDZfGre4gT88NLI00LpTrKb4Da_P5TfrLEsH0iTS1q3MSFVTsBSro2wMBfVj-wqNIT_q59FO98b-7oNO0XYeO5DbFJlYeiiOqi8ADDIHDbhehd-0MD1XvM0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تنگهٔ هرمز در قاب غروب
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/460496" target="_blank">📅 20:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460495">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bM2rnrPKnkFAEwu-VUJ5_-uUdvjg1XE_onI_HJ7nUUkAhmxWko85-pxl6vxqGL7cjuQJ7iQsQuBHY-Vad92hxpllhmzlyGyQf-TDoMSslk5I3Xiano5CG5zDbwv1r5kV1rWjzK45A-xfyqb8Epe3-fkRSeRoZUSSSDPLdgmU3hCQvq-2kV6CStfUGV-0m3B6yCy73Aw4MVBdUrHUJhh-T8yr9arnjyFHfQf6DSt3pEiAW1ahn-lpCQZ7-csQv2Y-vb1_V6cstrRl567QObJiMRwvUrYFo_WAiTqNXhQ6-DpIuYLP0TbQlPnXSYER7TFjTfEqcak3K0_XaTR6gUx8EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به آب شیرین محتاج شد
🔹
جنگ اخیر نشان‌داد که زیرساخت‌های حیاتی رژیم صهیونیستی، از جمله نیروگاه‌های برق و تأسیسات آب‌شیرین‌کن، در شمار نقاط آسیب‌پذیر این رژیم قرار دارند.
🔹
۵ تأسیسات آب‌شیرین‌کن در پی شکوفایی جلبک‌ها و آلودگی‌های ناشی از فاضلاب غزه، پرسش‌هایی را دربارهٔ میزان آمادگی اسرائیل در برابر تهدیدات غیرنظامی و طبیعی برجای گذاشته است.
🔹
علت اصلی تعطیلی این تأسیسات، نگرانی از آسیب‌های فیزیکی ناشی از تجمع جلبک‌های رود نیل در تجهیزات بود.
🔹
سازمان آب اسرائیل با استفاده از منابع جایگزین مانند دریاچهٔ طبریه و چاه‌های آب زیرزمینی، تلاش کرده کمبود ناشی از بحران را جبران کند.
🔹
اما این اقدامات نشان‌دهندهٔ استیصال این رژیم در مواجهه با بحرانی است که ریشه در سال‌ها بی‌توجهی به تنوع‌بخشی منابع آبی دارد.</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/460495" target="_blank">📅 19:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460494">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/689e5c44b2.mp4?token=Cg_1RvUnpQ86ZMfHFvn3i0f4WdpazA3FQcxPg2pYMeRPhYTPS-0xTjRCABt6n15F6LzohcT5twlVhTAAKzyeUMj680vXtGBpLdmqjXEnZAXxOWz39Ur5hB3_sUzDJx2hLu7BVb1eUFS5e1iZtQ5vQANvORkCux-AL5VuF9oEmgKQsXGeLqEw8ynzGnX7tLNWhp0IcG2yKVfvEQC1D4so-JRTDePP5dJGtLwYW-k-eHADEYGk84SEMADVMtBNkGwUdb-kUE9KU8vgpmEdy8wxE044f6ghqVZenxypoB2ayjEbilpeyRrGMfj8wn8nas01MUgd6WwJEM-ctL6LkaHDag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/689e5c44b2.mp4?token=Cg_1RvUnpQ86ZMfHFvn3i0f4WdpazA3FQcxPg2pYMeRPhYTPS-0xTjRCABt6n15F6LzohcT5twlVhTAAKzyeUMj680vXtGBpLdmqjXEnZAXxOWz39Ur5hB3_sUzDJx2hLu7BVb1eUFS5e1iZtQ5vQANvORkCux-AL5VuF9oEmgKQsXGeLqEw8ynzGnX7tLNWhp0IcG2yKVfvEQC1D4so-JRTDePP5dJGtLwYW-k-eHADEYGk84SEMADVMtBNkGwUdb-kUE9KU8vgpmEdy8wxE044f6ghqVZenxypoB2ayjEbilpeyRrGMfj8wn8nas01MUgd6WwJEM-ctL6LkaHDag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر انرژی آمریکا گرانی گازوئیل را تقصیر اوکراین انداخت
🔹
رایت، وزیر انرژی آمریکا: حملات پهپادی اوکراین به پالایشگاه‌های روسیه مهم‌ترین دلیل افزایش قیمت گازوئیل بوده است.
🔹
از طرفی دولت بایدن هم بیش از ۱۲ پالایشگاه آمریکا را تعطیل کرد که باعث این آسیب‌ها شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/460494" target="_blank">📅 19:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460489">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پهپادها، چشم بیدار ایران در تنگهٔ هرمز
🔹
مرکز عملیات UKMTO تایید کرد، پهپادهای شناسایی ایران بر فراز تنگهٔ هرمز به طور مداوم در حال گشت‌زنی و رصد تحولات تنگه هرمز هستند.
🔹
امروز ۴ نفتکش که قصد عبور از بخش جنوبی تنگهٔ هرمز را داشتند، از این کار منصرف شده و به سرعت از تنگهٔ هرمز دور شدند.
🔹
طبق اطلاعیهٔ UKMTO علاوه بر پرواز پهپادهای شناسایی، نظارت هدفمند بر کشتی‌های تجاری و هشدارهای VHF نشان دهندهٔ قصد ایران برای تثبیت حضور در امتداد خطوط ترانزیتی کلیدی تنگهٔ هرمز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/460489" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460488">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsDoUHkSa-vm15aukbUuTerh5Gc1g0k75d9IEf9-oZF51jIxAhouiirrI20o34J1ZBa1mFmVUjk4wYACBOSSVAkkH0_LgYFi_do2mEcRRgXhAjafEtMcueE170GllP5xce3Tz2ds4T74flve17-4xcW319BBdyTymCgJc_Fuf3d65f-DgJaaeCvwFF-QQUPQJd8MZ5A21nzpeMsdoTswDz6oagFYYk-XGiiUA33FEGjFt3WH4xZR8SHNbF96JyuD7rsU01ZUJ6YspNaLYmJAPOf_dHy6uZutkDS1QyoNiuCZ4_hbBAEx8HKJR83vh0up-gOy_n7EUmYRBpm2iCOK1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف در پاسخ به خیال‌پردازی‌های بسنت دربارهٔ نفت ۴۰ دلاری: قبل از ارتفاع گرفتن، حسابی گرم کن!
🔹
نرخ گازوئیل آمریکا به «بالاترین نرخ تاریخ» رسیده است، وقتشه یه فکری کنی!
🔹
ژاپن که بزرگترین دارندهٔ اوراق قرضه آمریکاست در حال فروختن اوراق با حجم بالاست؛ با این سیاست اقتصادی ژاپن به ضرر دلار، بهت حسابی خوش بگذره!
🔹
نروژ که دارندهٔ بزرگترین صندوق ثروت ملی دنیاست، در حال فروختن ۸۰ میلیارد دلار از اوراق قرضه است. بهتره اسم نروژ Norway هم به آمریکا Americaway (مثل کاری که با دریاچه انتاریو در کانادا کردند) تغییر بدی تا یک کار موثری کرده باشی!
🔹
نرخ جذب نیرو توسط وزارت جنگ آمریکا که در واقع اسراییلی است به شدت کاهش یافته و با کمبود نیرو روبرو شده‌اید، یک کاری کن. شاید بتونی از طرح پیشنهادی اسراییل برای جذب نیروی جوان امریکایی در ازای بخشش بدهیشون استفاده کنی!
🔹
در آخر هم اینکه اعضای کمیته سیاست پولی فدرال رزرو چراغ‌های هشدار قرمز را روشن کرده‌اند و درباره روند آتی تورم و افزایش نرخ بهره صحبت می‌کنند (که با سیاست خزانه داری در تعارض است). عجب وضعی!
🔸
بسنت، وزیر خزانه‌داری آمریکا در واکنش به انتقادهای دربارۀ بسته‌بودن تنگۀ هرمز و گرانی نفت، وعده داده بود که امیدوار است بعد از پایان جنگ با ایران، جهان شاهد نفت ۴۰ دلاری باشد.
@Farsna</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/460488" target="_blank">📅 19:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460487">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
حمله اسرائیل به یک خودرو در جنوب لبنان
🔹
رژیم صهیونیستی در «النبطیه» یک خودرو را با پهپاد هدف قرار داد که به زخمی شدن چند نفر منجر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/460487" target="_blank">📅 18:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460486">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIs6G17dgqw8pF_eXbz8I-KWHoXldi2V9RRe92OrIgtWv5_LzKC9HrME4PnFEMXCzWAUpcWtRl3h80PEVZKpi_-EkOeuIFq75DgILxcJ5Bl8gBJ78b7TsTvoFkJdfL_YwSX_TlqYViK5ACaBCVpATuygkBIHijY7wZpFUhKVDxG-sqr5yWjuPIu37EDESwb0cZmeD39VpeQuO6f44dNEAanCQclL_E99hlZb4pnstczNjsQSr4XLKwFH8leJVpvk8xPpMy8AfQAPxtZrO2XRIE8x4YwWbRy5oUG53wcGDBPZSQy3P8DnACVtg19CGFMT8g0odvMtYk5PXBbFZiFgOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زن نپالی وسط مراسم ختمش زنده از زیر آوار سیل پیدا شد
🔹
یک زن سالخورده نپالی که خانواده‌اش تصور می‌کردند در سیل ویرانگر این کشور جان باخته و مراسم سوگواری او را آغاز کرده بودند، ۱۰ روز بعد به طرز معجزه‌آسایی زنده از زیر آوار خانه‌اش نجات یافت.
🔸
به گزارش رویترز، «چاندیکا کوماری شرستا» در روستای «بتراواتی» در میان یکی از شدیدترین مناطق آسیب‌دیده از سیل، زیر آوار خانه چهارطبقه‌اش گرفتار شده بود. امدادگران روز شنبه پس از شنیدن صدای کمک‌خواهی، او را در فضای باریکی که میان گل‌ولای و بقایای ساختمان ایجاد شده بود، پیدا کردند و پس از عملیاتی ۴۵ دقیقه‌ای به بیمارستان ارتش منتقل کردند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/460486" target="_blank">📅 18:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460485">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52eee8023.mp4?token=WBpfI1rghIvXH7wauTv46CAsPrfiIdcBSktVkhux3Aibac36_I4NfXBkDktiv051FzSra3VDQE3HK_yjkffdIadY8QCaE3eBOVxTzCrdmUUy4Vo-eC6cJ4nOOXDWH6MF23KfUR_iVDb8m2-XXYGMYGXnQuCb4lZUBslgqM9hKUxR9AZg6svPmgQT29MPV6E-KpSfZcT0Kxsw6l7hkO43epW5oSgh3V4QcP1ABUW837iDA1F9hT7oNJP1IpbTZk9e_YVUvF014nW8ZPMFkLiUHRgddNOjMc2yQjTQdudcunLJZgiuUEgNBLBgnZ2Z6veecSxR781B9UU9RbjZjUrC8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52eee8023.mp4?token=WBpfI1rghIvXH7wauTv46CAsPrfiIdcBSktVkhux3Aibac36_I4NfXBkDktiv051FzSra3VDQE3HK_yjkffdIadY8QCaE3eBOVxTzCrdmUUy4Vo-eC6cJ4nOOXDWH6MF23KfUR_iVDb8m2-XXYGMYGXnQuCb4lZUBslgqM9hKUxR9AZg6svPmgQT29MPV6E-KpSfZcT0Kxsw6l7hkO43epW5oSgh3V4QcP1ABUW837iDA1F9hT7oNJP1IpbTZk9e_YVUvF014nW8ZPMFkLiUHRgddNOjMc2yQjTQdudcunLJZgiuUEgNBLBgnZ2Z6veecSxR781B9UU9RbjZjUrC8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرگ ۲ کودک درپی سقوط هواپیما در آمریکا
🔹
رسانه‌های آمریکایی از سقوط یک هواپیمای کوچک در ایالت کالیفرنیا خبر می‌دهند که ۴ کشته و زخمی برجای گذاشته است.
@Farsna</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/460485" target="_blank">📅 18:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460484">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mt3yEFATSH3ummaPAIieHPajUyQZTtO_47qBib7oMFFIzIs6Ac5S3FO5zylqXITp5uLk7pASkaz7mCiqattjW19JZ9N9pA1o-RGMxS7hou2bl3bfLd5xWvK04JTh6oLHaQx4bhg6PN434oJLQfKiJx-LRUJQyA1EKabK5DAGPT1Wg1kt54AX_ZFwr7XZE1tEk_K0e2gvxOOCyb9PKu8ZBxCoTtvt15wO67lPR4S33MIfMSDYwId2-XtiYQTnrWVtX7iZVxVi_S6XEJw4FEdg13-hyHynhlryT4OQRBgCFCH-PSF6lkktAVNiwt9f-iQcO98mNCRzxH5tguYv-vYlPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازداشت عوامل رژۀ موتوری منتسب به سازمان منافقین در حوالی کرج
🔹
روز گذشته ویدئویی در فضای مجازی منتشر شد که در آن ظاهرا تعدادی از هواداران سازمان منافقین در خیابان‌هایی که گفته شده در حوالی شهر کرج قرار دارد، اقدام به حرکت با موتورسیکلت و خودرو کرده‌اند. …</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/460484" target="_blank">📅 18:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460476">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MvpAaN50vn_7WZzT-U81FF1UEdgyFl-0SHu_mInZS_NTPD9Q6bz6Fp4Ig9-4PqUQCIJjTinoZvX6Bh_R9WCZd8XljifKCmHIhhUsydAd60pMFRdXla0XmBRBj8tcHcc59tODN0BEWBVSiJA094cuCCRaWgniBCe3UrLsmzbmmbJ1Isv7nX9G8AFF66qczq7N5hW-5MRHOyyKB6rPyZW496xSDzJ-0BY55aogNteSecv-D2wcfPSJqsjMouhmhd_acdXGkzj5CZsVG1OovMu__9k1YTab4-uoxY5plwGLtlD03Awxi1tamyFNjmixnq2fX4T222_XdxfdnNbaKo3eXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T09-ohlBaVTgkXfXTumFIBb2J8327JfkWVfiWHEc6ym3lDhx0nylKOc2zQZKVYH5IIW8ro89pZPwfQuaGC8ZltgFkVu05OfPL32r1eRzFgKrwncpu1kRjfhDsFdzVS2oWHeSVnJGQVYtsU8srAYkJuo2wLrQPnak-5AV9asoqS7VX9b0xPFZn22fShlNoBFQyGg6VIDXgi-SjegYuMMGzBTpP0kYZAxudvWCtXwapbG00e7nJSl1Yc_9pkvzua1Pz57PSuPobzAf_o66wxm-u1NkWr8VxAVFuioZbQAcOIVwWVowv_h-yres7z4vZQUdxf4dYW3yxukI2GG9KJtA-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJONInkoAAZyED75MBPeIzFoNA0DaEB2PkU7MsRqPLPOVXA02xMfOD4zRbPnRvDjS_o5LNT7XCl2Bu-kwNmKsNvKhk15hofLwzbi4I7MbfVkVmemL6WqmilQcDuFOi2iT6APxg_OVXLpGU9qmh_IB9KkKGerrofgTKnKrB-UVFwAxcv3iHgP6A9cQAi7BL0DQ0zWIg1jHIL7tZSvR0odgPwEGhyKxRXts8BWmfBrFW7PW4N6Lu6zq--02oOX9mhEH8XTj_7VVrIMceyKKGfPpisvomungY0C1US0_gJjNyBMRtzLTMJg48jhEBGSQaNcdh1UlJp0AEmQJGaznDmSiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/slbK0W6h9DOSASFgd_6GbLmFxrPnZzsrrfZR39O115ckk_TJfdKc5S62o3xIqVa2A7QJUjlQi06Q_XtgpnrTwtexOYhZ334TdtFv1Ai5wo6EIjeEiI1E_kOQYexMbmxV3YyOUjtwRj2Pn8PZskSrFZLkDEh7me7uyq5EpCNh9Ae4lvGO5uAAlejrvX0OB4dIBI0UGKvdhChpiv_bi1ZPONtAd6zXFptSHmU-7k-w4VmujgR-tkStW6nB-soc4WN6iM6Qj2k-6FI4cLdTx2cWvXROgJCeLqsLOJTgncnxXGOMpGea5Qz90wib6CoVyWo3Tkk5kID7agxOqePivx0RXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FcimzKYgWGeR_CVaCqHOQi7ESJpgMIzbyUtUiUGlwVibCh59wflxT5Y5UZFt7kVgyR4lEgtdQrWi1sFTUi6g2WOIsBhYxgN2viesDVpVt54Ae1tkQw3Wj-EcV04KjZFVFpjrQxyeqXTexFt4lNY_S8vVayljIF8JcG0SaK4CvILYB4mneCIrK1axkp2cB9lvfeSy3rS0K2WXZEhrvQnjgO1rlrEyIPo5goUOjHV1nXm7rj-s4qkVXQ-vb7CRf7lwiPOnAYwbt01Ep5FCH_VJ8vUv2kb3zeQWEvHfP6K010M6wGJrPx7lFttAuO0PyMdJcANRSeDvF2mEdkPAZgidnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/schWRDfCZUozfs_-H3jp3xds0wnEMpvrgPvobvrqOT_OygWOhA5cLjJn0c7372IdplHQzFfS0nWIOP5C6m05rIxO6zUTQzpzZtFtw3jKGbQmuTA8phvVrkzNTtUg8Blj0q42JcQtIgJwxd2E4pqZvV7MJeRLuYCds81FJzA2qt4hyNWWPdrf13e7bzUmE0ie0tffIqu91Bue8pSF_JiEbw3c0pUsOgliEUaXJJgTo5XNlGg2SyEFVePrKUUKc9IJX0fDgcefizc6IuR3N9VZ-UieZuN2S5ITYD0wfRk1VLGT_a9Lz6_7JV57LWRfFMxCIXsvsvozQXRlcxnW8U1qMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W3ZbiIon1qs06cYetkfbknd_wx0IxKBxkRisUjQsqIkMsXk66tac8_U6EzPf_RjGzIZEH0VUzka9jS9Hs0H1AOCdkupZjK33Dib0p9G4kKHT8T1Hy9OidkovDPLCCklkl-5HXRaG7Unkq469KNgm3xUeorRB2i4BxOHIXupKfgsCSocZPzfscj-vKU0BWoj63uP_8IrGg5gmwbNOnUfEQRKUiMccFe2Jtb5WZahZIEYaR1ZSVVbOUzRwojKepWtfiU1GGQiCv32_8iVGJ-TiBc3m34FxcJBqm-RQ9rP4W4DwFkCDqQFJcLt2UgWVeYTfkOXCU3i1zY-Xc8oiPuiFoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7DUeXLXOs6-ajl01r2HzemavbnWrtPqSF0qT_ApoS8hX7Te57mOH9QVm7GyCcf8FrAVDebqQiYzYOOOZoaS6gzAos5ZvsCD2ZMOm4LIw09gui1CVsQS4eaLDQ1Orm4E43pRf8YEalYz6DYsrsit075nPL3RN7pJ8eqnZRteEImpts7Zv4NfI1U_li03wkduT4XrBYUSYyUNMefyYmU1YtC2bI3zdPB0rEpEJWHuPgSsKXoVKY-Bw0KdJgI32BzP_Lw4gz4CbGY9nebsx7aT8l1E4lji35qeKMB58GOWioB7GeOx_LihBPjhcQ_ZNtcCHRWLib6Mimr_8Dw8B4YPqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
مراسم وداع با خلبان شهید حسین مهدویان در قزوین
🔹
شهید «حسین مهدویان» در حملهٔ اخیر دشمن آمریکایی به خوزستان به شهادت رسیده بود.
🔸
مراسم تشییع و تدفین پیکر این شهید فردا ساعت ۱۰ صبح از امامزاده اسماعیل(ع) قزوین به سمت گلزار شهدای این شهر برگزار خواهد شد.…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460476" target="_blank">📅 18:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460474">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzdHEMlThrDBnMtFoHDn66ApcLYBIaG_E0DJeanYVsS5wdpW885LI92gGFFR_E6h5-mLhr0rmWQOa32eEwmY3t10FBLHRY5uUdmVjUXYrpohEF5cR1bduvdRfGYxf4nWSvWR7rx2amOU7_CvyW_ST30R_2Rw_RfVsb3ye9FiT4-VBbKaBiUjxdvreOilKask-Y6yCV-zTQdLufRISitnXDo-XYiolmjC_RAlJW7VZRApwT7lIY9oMZbOsSoru2krTJuStMX5Uoz8oOT-BuI9azjoz0IhAz3FErd-IvrGEyo-SZXPhiR6coTz6zk-pYMj-LZ1ThjfknDXsh4HNlyPJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف محمولهٔ اقلام ضد‌امنیتی‌ در  شمال‌غرب کشور در مرز اشنویه
🔹
قرارگاه حمزهٔ سیدالشهدای نیروی زمینی سپاه: در اقدامات اطلاعاتی پاسداران گمنام امام زمان(عج) در سازمان اطلاعات سپاه استان آذربایجان غربی، محمولهٔ تجهیزات ضدامنیتی درمرز شهرستان اشنویه کشف و ضبط گردید.
🔹
این محموله شامل ۶ قبضه سلاح کلاشینکف، ۲۸ عدد خشاب  کلاشینکف، ۶ عدد سینه خشاب، ۴۵۶ عدد فشنگ خارجی، ۷۷ عدد فشنگ ثاقب، ۲۴۶ عدد فشنگ معمولی بوده که گروهک های تروریستی تجزیه طلب با هماهنگی سرویس های جاسوسی آمریکا و رژیم صهیونیستی قصد داشتند جهت اقدامات خرابکارانه به مناطق عمقی کشور منتقل نمایند.
🔹
به همهٔ عوامل خود فروخته و سردمداران آن‌ها هشدار می‌دهیم که با رصد مستمر اطلاعاتی گروهک‌های تروریستی، با هر اقدام امنیتی بشدت برخورد می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460474" target="_blank">📅 17:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460473">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3800f6eeaf.mp4?token=atf9P5AObPBs8KKnoqp3fT9U2LZ1o1cdTECAELCh18Yp-O8evhcKiDezfwwLEQEZ-SVH0d3D5ulcx9Tkej7l_nOlHdRCIvTJkoZ7mjsUQ8HLcuEgNAtOt-MGciDO6xc10EBpCIoxpOOPPrUadbKaJpCfNDJlt8tqRkS69eVF0JgjJhkZDkzfECWvt-6jYkfXLCkHldgjqkVnYsgNGGZoG3VqjisjkQsemgjUoQ0NsmhnzSJ5noqCzFxQcBrWc5F91jvIMkSaY0i_X9jhX2P8hyZGW1O1QhM9VaRtTuHWRtG1MzDzheHFQjwK1OdHXDTSzx90hnRBtXAzmjxWWbCOMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3800f6eeaf.mp4?token=atf9P5AObPBs8KKnoqp3fT9U2LZ1o1cdTECAELCh18Yp-O8evhcKiDezfwwLEQEZ-SVH0d3D5ulcx9Tkej7l_nOlHdRCIvTJkoZ7mjsUQ8HLcuEgNAtOt-MGciDO6xc10EBpCIoxpOOPPrUadbKaJpCfNDJlt8tqRkS69eVF0JgjJhkZDkzfECWvt-6jYkfXLCkHldgjqkVnYsgNGGZoG3VqjisjkQsemgjUoQ0NsmhnzSJ5noqCzFxQcBrWc5F91jvIMkSaY0i_X9jhX2P8hyZGW1O1QhM9VaRtTuHWRtG1MzDzheHFQjwK1OdHXDTSzx90hnRBtXAzmjxWWbCOMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: ناو هواپیمابر و یک ناوشکن ارتش کودک‌کش متجاوز آمریکا مورد حمله قرار گرفت
🔹
روابط‌عمومی سپاه: نیروی هوافضای سپاه پاسداران انقلاب اسلامی با چند فروند موشک بالستیک، ناو هواپیمابر و یک ناوشکن ارتش کودک‌کش متجاوز آمریکا که برای کشتی‌های ایرانی مزاحمت ایجاد…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/460473" target="_blank">📅 17:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460472">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3882c73266.mp4?token=TwEIa8rB_8jPpP06F164IzZxs7Qz6JAK1yaKz7nv2j36Hhl9_YXtj5-BE0dkNf5KMQhC2ZZ8fTy_VqjEpN8ml9KVhbBqKyf8dootMiFPDUcXGDfXWYMYqViMphQdkNZipCzpi1Q_jWYijmNSx6xWWb1hRbxoi0RKXaTOPv_2a3HdWzyA_OXoe1nKPcXp0CRjHV-KvpHRaxJEqZnT7lqYaS8b9FspYc5N_3JYTMtfp4rSOhGbQumArG8XfRwclZE4oQ09xbaAxCBWXDsLR4qPp7J0Ks8NlNGdNjusmhbmqflNeFAq-Eo1VYgXj82Mxf8-n6vaDRj4fvxedCYPNh1PEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3882c73266.mp4?token=TwEIa8rB_8jPpP06F164IzZxs7Qz6JAK1yaKz7nv2j36Hhl9_YXtj5-BE0dkNf5KMQhC2ZZ8fTy_VqjEpN8ml9KVhbBqKyf8dootMiFPDUcXGDfXWYMYqViMphQdkNZipCzpi1Q_jWYijmNSx6xWWb1hRbxoi0RKXaTOPv_2a3HdWzyA_OXoe1nKPcXp0CRjHV-KvpHRaxJEqZnT7lqYaS8b9FspYc5N_3JYTMtfp4rSOhGbQumArG8XfRwclZE4oQ09xbaAxCBWXDsLR4qPp7J0Ks8NlNGdNjusmhbmqflNeFAq-Eo1VYgXj82Mxf8-n6vaDRj4fvxedCYPNh1PEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محمدرضا گلزار: قدردان شجاعت، فداکاری و ازخودگذشتگی عزیزانی هستیم که در روزهای سخت جنگ برای دفاع از این مرز و بوم مردانه ایستادند
🔹
در این جنگ جای بعضی آدم‌ها برای همیشه بین ما خالی شد. رفتن دانش‌آموزان میناب غمی است که با هیچ کلمه‌ای نمی‌شود حق آن را ادا کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/460472" target="_blank">📅 17:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460471">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iE17wwbHdNLesF4i8lQfaeHRJt-0n796LYwxK3cThYL5-QSMGm_ULZCIqMcd0OTSa0fCo8_sa671iI9O0MAnrlRlZ1B4iLYkFEh4gW2DOXPiXhSRLlQeNKC-6zcOmBBcogyiJyPtV3jV6pQI454IcIkVmChPPQnXPAOd8Z9JUrSUQe3gs3KyJ9dBR_hCYc8V0e46D1fsknV8g2irJWYKoVt0_3xxyBFXZdxNemtH84IDFerp_j-2YqfVpWY980P8Ky_Bm4b1Z5FmXgyDFZdOEhs13YNKG5dkO2gqpzdc8B39IKzO1ALDr2mZm1b4ntao_BKLZAWalJankHN8d1wnig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بودجه از درآمد نفتی لبریز شد
🔹
طبق اسناد رویت‌شده توسط خبرنگار فارس، ۹۱ همت درآمد نفتی در ۴ ماههٔ امسال به بودجه تزریق شده که این رقم ۲ همت از مقدار پیش‌بینی شده بیشتر بود.
🔸
دولت در پایان سال گذشته برای ۴ ماههٔ امسال ۸۹ همت برای درآمد نفتی درنظر گرفته بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/460471" target="_blank">📅 16:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460470">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bff51e3ec.mp4?token=I70a28LhXhx39v8NxmnnceGZ78LJjYPfRiAI7mgPvirwkZVPlCFauEzwvMzUDvYOO9yz8kBtdcVIFRi1XrjCxtK1V_-WwOfyi-uelWgn6eaWYZsZ05Om4_PaVIltv4RV7v1O-0OL9LDhDL1s2yKU0buhav2XiiZ842aTEm2qFbMXCDtCQsQybp7zSuugTbCKTqiu9YQ7Tn8VJVrfSRWTIZP62-u9ag3tG3nygTaHdhPOQcTwjr7mnkUUMFhRrl-OEaPCm3DilO7NjVOnXAwDwiMtpsMpVvNK5B65oDc5p6K-l9bELJkjXUbMFiHLA5MczHL8PxUshmdMoucPu7K7Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bff51e3ec.mp4?token=I70a28LhXhx39v8NxmnnceGZ78LJjYPfRiAI7mgPvirwkZVPlCFauEzwvMzUDvYOO9yz8kBtdcVIFRi1XrjCxtK1V_-WwOfyi-uelWgn6eaWYZsZ05Om4_PaVIltv4RV7v1O-0OL9LDhDL1s2yKU0buhav2XiiZ842aTEm2qFbMXCDtCQsQybp7zSuugTbCKTqiu9YQ7Tn8VJVrfSRWTIZP62-u9ag3tG3nygTaHdhPOQcTwjr7mnkUUMFhRrl-OEaPCm3DilO7NjVOnXAwDwiMtpsMpVvNK5B65oDc5p6K-l9bELJkjXUbMFiHLA5MczHL8PxUshmdMoucPu7K7Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
انصارالله یمن: جلسۀ تعدادی از فرماندهان نیروهای وابسته به سعودی را با موشک بالستیک نقطه‌زن هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/460470" target="_blank">📅 16:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460469">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
انصارالله یمن: جلسۀ تعدادی از فرماندهان نیروهای وابسته به سعودی را با موشک بالستیک نقطه‌زن هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/460469" target="_blank">📅 16:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460468">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a99eb7647.mp4?token=vKltj5Au5v8Qo93TmjfAXkY-EM8nv1EmULTFI6FvDrTq6R2U69zqPoeX3P5VoCkGrVt6kTzmzjVvWtH5jIjW312ugr8gg-cQev1_ZdcALvgn4RUveACuw-jOUhnQTPpgp0ygHEL5FGzU9fhp0a7odldIUgfettk4E4dmtZt2P2UrcdHWVQMpc2cOae742ZIGrL1hvv32SnnWJaLDPHD5C_7ff4ByWG947QZhzMvWU9_FkcbHAIBSYnqxF4zRRrBOisYxVzMpLujxJFA3IvMiUFFeZAMLqjZ4OR10pnPIS3ZBhSCDEqeQ0xuJOcTjKKHGl9p47yq0_xEWPj0BJLAwlTkGtoTyoWXeldk8Wm5Ma8qb4t0kSd1v1WFqbdEfOx7VX1yIGLUlsyZt2gzghhj6f4oP_X6ibSqgiVuL2HRvuJsSYG6n4Rppfe5oo_915XkjjZSh4KWbHX-vcDnBhUOC72Kajvta1k3Rr8yG81lCAGacJL-93JoQOQPIacbcKrTpYhq9pJ9cL7TY9JvErhK_quUNnNMrbzvBzcGFjId7r2BNH-UCE2EsD8Mjhs__G4-T1-3Fnyqhc-QexWvFt3QRFHLHx5DawtTq_e2R41ch3cMINatEfLlYW_qHyB_dSNCNlecpsjsxZORQ42uhWLyF7jkYAKjWMctjB8mj6qT34a0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a99eb7647.mp4?token=vKltj5Au5v8Qo93TmjfAXkY-EM8nv1EmULTFI6FvDrTq6R2U69zqPoeX3P5VoCkGrVt6kTzmzjVvWtH5jIjW312ugr8gg-cQev1_ZdcALvgn4RUveACuw-jOUhnQTPpgp0ygHEL5FGzU9fhp0a7odldIUgfettk4E4dmtZt2P2UrcdHWVQMpc2cOae742ZIGrL1hvv32SnnWJaLDPHD5C_7ff4ByWG947QZhzMvWU9_FkcbHAIBSYnqxF4zRRrBOisYxVzMpLujxJFA3IvMiUFFeZAMLqjZ4OR10pnPIS3ZBhSCDEqeQ0xuJOcTjKKHGl9p47yq0_xEWPj0BJLAwlTkGtoTyoWXeldk8Wm5Ma8qb4t0kSd1v1WFqbdEfOx7VX1yIGLUlsyZt2gzghhj6f4oP_X6ibSqgiVuL2HRvuJsSYG6n4Rppfe5oo_915XkjjZSh4KWbHX-vcDnBhUOC72Kajvta1k3Rr8yG81lCAGacJL-93JoQOQPIacbcKrTpYhq9pJ9cL7TY9JvErhK_quUNnNMrbzvBzcGFjId7r2BNH-UCE2EsD8Mjhs__G4-T1-3Fnyqhc-QexWvFt3QRFHLHx5DawtTq_e2R41ch3cMINatEfLlYW_qHyB_dSNCNlecpsjsxZORQ42uhWLyF7jkYAKjWMctjB8mj6qT34a0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستم داغون شده، چون محکم زدم توی سر شوهرم!
آشفتگی روانی و درگیری شدید در بین ضدانقلاب به روایت خودشان:
فاتحه ما خونده است، دیگه به شاهزاده اعتماد نداریم، سلطنت‌طلب‌ها دارن ریزش میکنند، زندگی ما داره تباه میشه، این درگیری‌ها به‌خاطر نبود سیاست و مدیریت در رضا پهلویه
@Fars_plus</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460468" target="_blank">📅 16:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460467">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phLBmOmYiDt0cQ6oYYA_XEp7zv3NotdgnVyAVUpahLqgl5apAnOFiUrbUHIlQk_T_rLMA_z0EXV8JfoasOeYXkXHT8KRMr-pGILtChciAI-2__6ygsarLZ3jjbrVL7VKKspgmI1B9giX3A1B-nnp8IoQ_AXink2ijRm2eLMwD1FXWm8P3IX_Pk47Dyd9XxyaVK3CAe8fe4xeqwnHz6xctISYJZTjdj8d6A3eKj0XPKqdmrXMQ7w6RVcIPnsKr0TVbsm1LwtH2yBpaBNoLmha8S4PuRkdHZXowGmsXi7oDExYxEZMRpRhKmyZdAENXwQvKEQCa-gw1BZQ2AlRzhhFZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگیری تیم مسلح ضدانقلاب در استان فارس
🔹
طی اقدامات سازمان اطلاعات سپاه استان فارس یک شبکۀ هشت نفره از عناصر وابسته به گروهک‌های ضدانقلاب شناسایی و دستگیر شدند.
🔹
این عناصر با هدایت جریان تروریستی سلطنت‌طلبی و بصورت محله‌محور، اقدام به تهیه سلاح و برنامه‌ریزی برای کشته‌سازی در اعتراضات احتمالی نمودند.
🔹
این افراد در اغتشاشات دی ماه ۱۴۰۴ نیز با حضور فعال، اقداماتی نظیر حمله به اماکن به‌وسیلۀ کوکتل‌مولوتوف، آتش زدن لاستیک، انسداد معابر و تخریب اموال عمومی را در دستور کار خود داشتند.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460467" target="_blank">📅 16:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460466">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phm8z5ZNvGFqR0eNfW2aaweebBAuO5jgGFQG0RVyPQdrBTVSr1-G-11_75Sce0Cqc3y6kchRPIzOwJI1TupExQXRDkijtwcAdka84wt7Zutpq18NSobFD4Pk92h6xXJo_rQjKdv54-KCwsWhbj1f356AP6la8Mbkty6osYcUz5uh8tK1hxxrXwGb6edHdTnPKKewrwgbnDq5MBkCmDyn5axdWs5MFoRPBg-wOvLQHRt1-XlxgzieEDgLpaRCyREfZDvGAWxGE0KyQf2EsNIeuNcywzhawzd8TN6ESP7JGkUNdRE9bE9ZuffCSIlEu0Iw1zTlU1L4xBeMxwqEhAAalg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرمربی پرسپولیس: بازیکنان می‌دانند غفلت کنند، نفر جایگزین آماده است
⚽️
بازی با ذوب آهن برای ما مهم‌تر از دربی است. از فیروز کریمی خیلی چیزها یاد گرفته‌ام ولی چون استقلالی است الان نمی‌توانم مشورتی از او بگیرم.
⚽️
چون امتیاز هفتۀ قبل را کامل نگرفته‌ایم محکوم هستیم بازی فردا را ببریم.
@Farsna</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/460466" target="_blank">📅 16:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460465">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCTFcYQSvIQv5Uu71znSHfUB5GHbvt2JNuuaS8ZIejZpluN7YaN2YJcr1DAsj_5PH154Mce2s2nyPjiKFlsVO5dbMbmTyjVQrH1_T7aQyJ75sfQDrsNYqfTRwRozFf6CY5MlcA5cg6Z-1-5HZzqu4L4uhqwNA4Vq9OdiROjbwxZYp7SEKvtF6d7HQk4Es7vVsmx2EVRgiIexHsI53jFS7CnwzF0xdz-Ke8sVH7NFv4bLJEYIKiG8f9TSX6xKhY2OhMH-B2ARXdQx5sLx0UPBlivnpv4LFI63h0gbxKNB6X_kB5xqjF9rE60-y8natQDvrlqdFTSExHdxA6lVwB43oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا ایران، آمریکا را تحریم اولیه و ثانویه می‌کند
🔹
ایران با قراردادن ۵۶ نفتکش متخلف در فهرست ممنوعه و هشدار تحریم همکاران آن‌ها، تسلط خود بر تنگهٔ هرمز را تثبیت کرد.
🔸
این اقدام با رکوردشکنی قیمت گازوئیل در آمریکا، سقوط ۹۰ درصدی صادرات گاز قطر، کاهش صادرات…</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/460465" target="_blank">📅 15:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460464">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e03c17e53.mp4?token=HMgvtO88Wzs74u8I6LYkT8qXbd_60lhYsEwfoJSgY0s9yOu2VyT7wc7K2PofR7GSRqRVpLeHxFgnrYc5shgsD0dp2aJxaoc_J3CaasF-iIX19bgGeymisEC5f8-GwqkGezX-BESmyaEr0bOexP9Du6ZEPHouJNvxj79JOiUFKx6RDN18PE7WNDYQ-1fgjxlUxooBODoQ7SJyOW1W3yuVIelf9vQbf3m7cYEyPZo4FJRml6wKJC3r_fEBoicyDZou191I-EPGm5pO8ILHCtGRinQ_y1NeweZLVXif1F3LBZuqMCAeq0fmdNpyQ-dXD7qbYaBjSoimDMpcNHqsY7f8GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e03c17e53.mp4?token=HMgvtO88Wzs74u8I6LYkT8qXbd_60lhYsEwfoJSgY0s9yOu2VyT7wc7K2PofR7GSRqRVpLeHxFgnrYc5shgsD0dp2aJxaoc_J3CaasF-iIX19bgGeymisEC5f8-GwqkGezX-BESmyaEr0bOexP9Du6ZEPHouJNvxj79JOiUFKx6RDN18PE7WNDYQ-1fgjxlUxooBODoQ7SJyOW1W3yuVIelf9vQbf3m7cYEyPZo4FJRml6wKJC3r_fEBoicyDZou191I-EPGm5pO8ILHCtGRinQ_y1NeweZLVXif1F3LBZuqMCAeq0fmdNpyQ-dXD7qbYaBjSoimDMpcNHqsY7f8GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ژنرال‌های ارتش آمریکا در آزمایش دروغ‌سنجی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/460464" target="_blank">📅 15:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460463">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPToJ7tE5wF0QCP-q59I0gbfeT7LQ1HyiMtAQDKBr65w7ymzyxYcUy-MIuFKmk37k_geZCi7OBJk17UqJT8EZrBPHcFldjF28bbooXgfYCSddNMZfAIXHHwquCCJ_KH-yZq1jb1Z2tPCyTWJ8XkC9vZQ6Hbr69-HurFionR5WqsUlhGhWy7mVLwCBSZhPy6Ly0Bf9RXJnCDnC8SHCY1Ufob7BcD0TtQsz4NKcUrqtAzpMSw1kQ-TeGsmgnVebngwn0LTirpvdhTkAz8Q_FWOqIaWTs1jH1OP3UXJVKukH3adXFtj5XbnSKMY36QgdxKq4W4MbzyZMQBOeaaDJUDvIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سهم بانک‌ کشاورزی از تامین‌ مالی بخش‌ کشاورزی، به ۶۵ درصد رسید
🔻
بانک کشاورزی در سال ۱۴۰۴ به تنهایی حدود ۶۵ درصد از کل تسهیلات نظام بانکی به بخش کشاورزی را پرداخت کرده؛ این رشد عملکردی حاصل تلاش این بانک برای تقویت زیرساخت های امنیت غذایی، تداوم تولید کالای اساسی، ثبات بازار و پایداری سفره هموطنان است.
🔻
درحالی که کل تامین مالی بخش کشاورزی توسط شبکه بانکی درسال ۱۴۰۴با ۴۰درصد رشد نسبت به سال ۱۴۰۳حدود ۴۵۰۵ هزار میلیارد ریال بوده است، بانک کشاورزی با پرداخت ۲۹۱۰ هزار میلیارد ریال تسهیلات به بخش کشاورزی، افزایش ۵۱ درصدی را از لحاظ مبالغ پرداختی در مقطع مشابه ثبت کرده است.
🔗
مشروح خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/460463" target="_blank">📅 15:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460462">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsUHpsz5cOvUVFDyDsUNdQ7AKCvxfCgZyRoICDfT5VLokWZ2w3zDznSxj5RO9Lr7E7ps-0-YpXN_6XGH-qGUL0NRQCWXGtV-bdWX0YD2mfyEJgcvkItDgdvvUH5pp3IFa6KvREldDmYQV7gDWCIsQe8NuqUjPW9_GZPZj1SXVi4JC0cUYw91dcYueZHsvHmyxgm2jtwjbMWAAM8YILRbwII2Cr1dKQxcEGsDXjWL-fvt9ok-KQ1REREetXS5KeeKFvMKEjmaP1_srsxZIrocYJR-CzDjdFFjYx9Vfgpu7r9nBdDILySp-5MMEIrNXdEoaLQaMW6M7iLkQEkGFzso4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
سامانه فرارفاه بانک رفاه کارگران به‌روزرسانی شد
🔹️
با هدف توسعه بانکداری الکترونیک برای ارائه خدمات مطلوب و متمایز به مشتریان، سامانه «فرارفاه» (مبتنی بر سیستم‌ عامل‌های Android، iOS و PWA) بانک رفاه کارگران به‌روزرسانی شد.
🔹️
ثبت سفته رواق به ذینفع بانک رفاه کارگران، انتقال چک دیجیتال برای اشخاص حقوقی با تأیید امضاداران مجاز، انتخاب نزدیک‌ترین شعبه هنگام افتتاح حساب غیرحضوری و امکان انتخاب تعداد برگ‌های دسته‌چک از جمله قابلیت‌های نگارش 1.19.1 برای Android و iOS و نسخه 1.1.7 برای PWA است.
🔹️
در این به‌روزرسانی، مشتریان حقیقی می‌توانند درخواست دسته‌چک ۱۰، ۲۵، ۵۰، ۱۰۰ یا ۲۰۰ برگی ثبت کنند و اشخاص حقوقی نیز امکان انتخاب ۲۵، ۵۰، ۱۰۰ یا ۲۰۰ برگ را خواهند داشت. همچنین محدودیت‌های مربوط به صدور دسته‌چک مطابق ضوابط بانک مرکزی ج.ا.ا اعمال می‌شود.
🔹️
برای فعالیت‌های انجام‌شده در برنامه فرارفاه امتیاز در نظر گرفته شده و این امتیازها در نسخه‌های بعدی قابلیت انتقال به سایر مشتریان یا استفاده از مزایای دیگر را خواهند داشت.
🔹️
این سامانه در حال حاضر از طریق فروشگاه‌های اینترنتی رایج و همچنین پورتال اطلاع‌رسانی بانک رفاه کارگران به نشانی
www.refah-bank.ir
در دسترس مشتریان این بانک قرار دارد.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/460462" target="_blank">📅 15:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460461">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/460461" target="_blank">📅 15:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460460">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پشت‌پردهٔ رژه‌های تبلیغاتی منافقین چیست؟
🔹
پس‌از انتشار چند فیلم توسط منافقین در ماه‌های اخیر با عنوان «رژهٔ کانون‌های شورشی» یا «رژهٔ هواداران»، این پرسش مطرح شده که آیا منافقین در داخل کشور از شبکه‌ای گسترده از هسته‌های تروریستی و هواداران برخوردارند؟
🔹
بررسی پروندهٔ تعدادی از افراد بازداشت‌شده نشان می‌دهد که اکثریت آنها از ارتباط این اقدامات با منافقین اطلاعی نداشته و با الگویی مشخص فریب خورده و مورد سوءاستفاده قرار گرفته‌اند.
🔹
در مقابل، تنها تعداد انگشت‌‌شماری تحت تأثیر شگردهای جذب این گروهک، با آن همکاری کرده‌اند و اکنون باید به‌دلیل همکاری با یک گروهک تروریستی، که از جمله سنگین‌ترین جرایم محسوب می‌ شود، در برابر قانون پاسخگو بوده و در دادگاه محاکمه شوند.
اما الگوی این فریب چگونه است؟
🔹
سرپل‌ های منافقین با پوشش شرکت‌‌های تبلیغاتی یا بازرگانی، جوانان مستعد را از طریق فضای مجازی شناسایی می‌کنند؛ سپس با پیشنهاد و پرداخت مبالغ قابل‌توجه، از آنها می‌‌خواهند تعدادی جوان موتورسوار یا دارای خودرو را برای اجرای یک برنامهٔ تبلیغاتی گرد هم آورند.
🔹
در مرحلهٔ بعد نیز از سازمان‌‌دهنده می‌خواهند پرچم‌‌هایی با شعارهای مشخص تهیه کند؛ شعارهایی که ظاهراً نامی از منافقین ندارند، اما از میان عبارات و شعارهای شناخته‌شده این گروهک انتخاب شده‌اند.
🔹
پس‌از اجرای برنامه و ارسال فیلم برای سرپل، منافقین تصاویر را با عنوان «رژهٔ عناصر» یا «هواداران» منتشر می‌‌کنند تا یک اقدام تبلیغاتی طراحی‌‌شده را به‌‌عنوان نشانه‌‌ای از گستردگی و نفوذ داخلی خود بازنمایی کنند.
🖼
سؤال اصلی اینجاست: اگر منافقین واقعاً از شبکه‌‌ای گسترده و سازمان‌‌یافته در داخل کشور برخوردارند، چرا برای ساخت چنین تصاویری به فریب و پنهان‌‌کاری و استفاده از جوانانی نیاز دارند که اساساً از ارتباط این اقدامات با منافقین بی‌‌خبرند؟!
@Farsna</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/460460" target="_blank">📅 15:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460456">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NXmR9eV3ykqZfMKwwrLOJ4u-fdXwqcsGd0AFcRQ9FW7bWUYoD6lRM8UEsdHnP2ecO-z9WhHX15Dk5x2fWVGAvtHZJjp6PiHxF2yu1OW7X7ICSdO9Jp4w0F5ZsCzuPkTxa5DucQYZ9dm8xQAGfhvaSIV3ZFQCRPYvIFF8ehsyeiOW4y2y_p1IvMCA3OMvieO8IIIV_90AF1zI172cIZ7iL5co-WNRk80B0puMbPkIE1DvPTk3v6UfP9LCYBMltLAWWZuY5K65E9VoDz2oYpRw9rhCrZlOaCKpQZeaFFHhvYrJbr75kFl0a1yaMT8trfbtIbUz10v0c6wz0fo1gAt2lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gxe1S94gkG9FSi_h9JBS8EvJMGhlI17elH0EHf_kI1V1wBmT8vYSshwTAKUZa6ttw8qw-cE-YNAKHhJdebMzVxgPYXepR-L6wWTCe1wiDqbClEmANgGmYBQ3ccizBduwHBQ7J-wm5FdVUK3HhS3glkIGlZB7XjimlG5ajLYU0-Io_Agd76SKI-LrnnpXYJioktTkHJdkh3UyDrQsY8T8dawS8nVq9cVnrAfEtRD0gb9DUEnkwAgO-deIyaEGTvqz491DmQDz74n9WTohSXTXXcAaAuv-Vntov7oqy8Q3T4tV3oBzQl7dnck0hGqvU-JP6LvZeA76nCtQuE98Zqd86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UF9WuS-eaR8_6yeWc8QlMHDqDawpV5Q0mAPgl2AY1IW5p7-42dKidabDTqxo99A-meFJA8vroMyjq4VkYPnfUf0xJAtECb6jrItP0e2-mKDhNIS0uWusqABXzBChT_pguLhRyX9NydKojf6m45ZJsGCcJoQw9i45gAC-THsq1w7Awj14HP_it0hSKQmwtEckcUWMG9uEPWwfL2_t_WbueLydQ9eAkjyHACqjO3aRMPq5fk12zU4aS6wdUeuaUFrs9SiND8bLnsoUN_Atb-N-35Yt0bhl8QDvJ2tOpC722-FkaOZmCYvPPkTdZiX1FLm8X3j5VgbhhzAQs9Q7dMXOiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXHC4DMFg9eKNrCc9MY_MVMznPrLUcmlRy8FsneM-R6DZkdISS0Gx84gd-ePhs56mf2s1wR7Uqh187nWbN3t4sV6xsFmsK-2B9JQ0eC1MdpTD4I5peVHoYtT620Rp3ttOACLrXaNrD5JGUnGKwa3QI6nk_53L5gsl08jUNQ07tr722oFQ-EoZvWkZYhvECxI41k1p3nviKcq70e0kUofHVGh1fXdtCfkYCOBZfNtdcS03drdqiaPRcNqudgidOoNk_PAEMZqCj_8VdgTbscUdBZYgLfOBqQD4eIVXy1C9OYEGzOBUbqnQWKbwQP68UvTytP_KaRtWKygdilXt1_-og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: تصمیم‌گیری‌ کارگروه‌ مدیریت مصرف سوخت به مردم اطلاع‌رسانی شود
🔹
ضرورت دارد آنچه در کارگروه‌های مختلف مدیریت مصرف سوخت تصمیم‌گیری می‌شود، به اطلاع آحاد جامعه رسانده شود و ابعاد مختلف آن برای مردم تبیین گردد.
🔹
می‌توانیم از ظرفیت اجتماعی پویش «جان‌فدا» نیز در راستای مدیریت مصرف سوخت استفاده کنیم.
🔹
تمام اقدامات و مراحل سیاست‌گذاری در حوزه مدیریت مصرف سوخت باید از پیوست رسانه‌ای دقیق و شفاف برخوردار باشد.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460456" target="_blank">📅 15:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460455">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89cd5fd076.mp4?token=QldtYV55QWzvz6KIW8_robJBY-hp9KkBHvf1kis6hnlp1zRMs-n2WcXOkCCd8JH3xmy9H_oy1Rb3CJM5JTmA3rKO2hMunrUDcRwLHTnMzD9x55Mbw4JkKobPP6KfJZWaY_3HoKxa_QSHNwJ22GadIdbipcsksrrlXF_1hOvbqWHlcOsn7Q21bOZmDI58dtmKTUIaGaYbUxm-rKhSR_BhMNLKy6TvQpy0A4qbXil5hL340Mz1IEBN0IH58KYHPrM1p3zue4fIkcypnjhHWjZdX1OCJJIoXEMoD8zmy524BoLAHJDajw_Al7vlciqL8yo9rmzJgVKqxH_NMfWg53xm9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89cd5fd076.mp4?token=QldtYV55QWzvz6KIW8_robJBY-hp9KkBHvf1kis6hnlp1zRMs-n2WcXOkCCd8JH3xmy9H_oy1Rb3CJM5JTmA3rKO2hMunrUDcRwLHTnMzD9x55Mbw4JkKobPP6KfJZWaY_3HoKxa_QSHNwJ22GadIdbipcsksrrlXF_1hOvbqWHlcOsn7Q21bOZmDI58dtmKTUIaGaYbUxm-rKhSR_BhMNLKy6TvQpy0A4qbXil5hL340Mz1IEBN0IH58KYHPrM1p3zue4fIkcypnjhHWjZdX1OCJJIoXEMoD8zmy524BoLAHJDajw_Al7vlciqL8yo9rmzJgVKqxH_NMfWg53xm9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنوب لبنان درحال‌حاضر در چه وضعیتی است
🔹
برخلاف برخی ادعاهای طرف‌های وابسته به رژیم صهیونیستی، تپهٔ علی‌الطاهر اشغال نشده است.
🔹
در ساعات گذشته نقشه‌ای منتشر شده مبنی‌بر اینکه ارتش رژيم پیشنهاد کرده است از مناطق مختلف جنوب لبنان به یک نوار اشغالی در طول خط مرزی با شمال فلسطین اشغالی عقب‌نشینی کند.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460455" target="_blank">📅 15:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460454">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHlsQgJMRfgs11Ck7Z1bZK0LEvahhcnN3cl4fvSS8Gd5moNTbdeZmccYR-9doWG0BW_5vuCG-VsK8M1gWTAQT9igtpmmBLCM5KMdhy2WkDvW3ewG4v4cc6pxj5FPs4xeJnep8iPq2tbR3ySpsPbx2knGX6dKqL1XzOGNKIXJ9yMU054hDU1wSREWQgi3Zp6OTHaH53fGskWQu6c-hMA0jMGT0gVtZ1WxeQqycIvuHQxLKYH-o1_-ryb4GNpJHEgS-vYxXsx49eL8LMJf4VQow3540F0mjYt1VUYZO0AY3_LyRvhOhP-RpG_fK2sN_xJ17URfuR5VLHiMFCStTgQzdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور ابلاغیه برای خداداد عزیزی
⚽️
با اعلام کمیتۀ انضباطی سرپرست تراکتور به‌دلیل تخلفات رخ داده و بدرفتاری در قبال مقام رسمی مسابقه، باید ظرف ۴۸ ساعت دفاعیات خود را ارسال کند.  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/460454" target="_blank">📅 14:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460453">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/450dcf8c32.mp4?token=GroQQBe4F70f7a-LA-6UdmIDNJJVckjEL8C_wsSByxbZXphosa_g_u8lyy8Mi90U6xwTQFNsqGFi4Q1AVHHN7YUgZnCYxDJnK3QGIXmngPMjMqQjx8LKzxRt5kxtOKe7W0DudaTjEnz4raxyrsDXWbkalzNA-MfIFMzlLmtfh3apauIu2K0jrCvII5SqnVIWsatVZ1bIQbMEb4uu7RSvLniL4be6roUvDAoDXmIBVvRpJmhO4zFswo4lJ-W2L9Jw_aS2cXyjhmzZtCa3R6_6A7A22dcfAyQakhC-tDfd-TSlpoP_Ne9M-KZqWrR8g2JtzfnlOhY8o_FUrTJWUTAcWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/450dcf8c32.mp4?token=GroQQBe4F70f7a-LA-6UdmIDNJJVckjEL8C_wsSByxbZXphosa_g_u8lyy8Mi90U6xwTQFNsqGFi4Q1AVHHN7YUgZnCYxDJnK3QGIXmngPMjMqQjx8LKzxRt5kxtOKe7W0DudaTjEnz4raxyrsDXWbkalzNA-MfIFMzlLmtfh3apauIu2K0jrCvII5SqnVIWsatVZ1bIQbMEb4uu7RSvLniL4be6roUvDAoDXmIBVvRpJmhO4zFswo4lJ-W2L9Jw_aS2cXyjhmzZtCa3R6_6A7A22dcfAyQakhC-tDfd-TSlpoP_Ne9M-KZqWrR8g2JtzfnlOhY8o_FUrTJWUTAcWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روزنامهٔ عبری معاریو: شمارش معکوس برای فروپاشی اسرائیل آغاز شده است
@Farsna</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/460453" target="_blank">📅 14:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460452">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f2cbd25a.mp4?token=mtdj6hkoP_cfqNSRctLtJvkk8fLasJtw521oK5YumjPPI-QVBAxzkch6tryO0aUz47RXsJMSrOWs3OrrYANIj1o-1sK4W3yatNkGSNENezkVlF8ABVQpPyRFnT1sw6zEiECOBVMh3gtIvEQaPuFWzHp1rWbGgRvwHIDQ_xLm8pdqYSdFbwPLhXzHFDZQAbxGbHBwKb064DH_etaOu8CZaQFU8w7XDSl89IkoBpkE2QwX5m5fLkq_-6Y0bJSbWP6R2PzWOa2KlJPcIMYp63XLUY3BrgBIDXxF0zK3U8XiAtLQjSGP8weQilZXp4AwEM5iOZuprfOrqq27cI0-WCx6dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f2cbd25a.mp4?token=mtdj6hkoP_cfqNSRctLtJvkk8fLasJtw521oK5YumjPPI-QVBAxzkch6tryO0aUz47RXsJMSrOWs3OrrYANIj1o-1sK4W3yatNkGSNENezkVlF8ABVQpPyRFnT1sw6zEiECOBVMh3gtIvEQaPuFWzHp1rWbGgRvwHIDQ_xLm8pdqYSdFbwPLhXzHFDZQAbxGbHBwKb064DH_etaOu8CZaQFU8w7XDSl89IkoBpkE2QwX5m5fLkq_-6Y0bJSbWP6R2PzWOa2KlJPcIMYp63XLUY3BrgBIDXxF0zK3U8XiAtLQjSGP8weQilZXp4AwEM5iOZuprfOrqq27cI0-WCx6dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف: حقوق و تجارت مردم نباید تحت‌تاثیر طرح مقابله با نفوذ قرار گیرد
🔹
در نشست امروز مجلس، طرح مقابله با نفوذ سرویس‌های اطلاعاتی و دولت‌ها یا نهادهای بیگانه در کشور بررسی شد و ماده ۷ و ۸ این طرح به‌دلیل وجود برخی ابهامات به کمیسیون امنیت ملی و سیاست خارجی…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/460452" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460451">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/164ee20272.mp4?token=fITjk-6Pa7tA0HWCeJ8HBORUwX49xSlt6KwcQAUOzz9AcpuWdNjYnVmh-5HPf9ytOx1AxvULXqMfMlJSib-vJutswIEgZDIpDS1mhj3zkpnadkj-kQQbGuSv4nRbN0RYEGyI0IXYTa15dmy-pymqbfXc7WtA-uqh-fnB4YRaJ_rfnZj9LX1QO3LGaektb1ohEKiH15859j70FOw_0nt5HJja5Ut3y9lOFjm5yijXs3v80v4GAf-2Lqr1j57lfAgawveqRmPfl__-DtmtnJpQnb9OPfJNFqr7H-IJ-_5V8qBhZeKCcxCenMg4mT47-naih8BIJ5lviryfyeI3DeKOFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/164ee20272.mp4?token=fITjk-6Pa7tA0HWCeJ8HBORUwX49xSlt6KwcQAUOzz9AcpuWdNjYnVmh-5HPf9ytOx1AxvULXqMfMlJSib-vJutswIEgZDIpDS1mhj3zkpnadkj-kQQbGuSv4nRbN0RYEGyI0IXYTa15dmy-pymqbfXc7WtA-uqh-fnB4YRaJ_rfnZj9LX1QO3LGaektb1ohEKiH15859j70FOw_0nt5HJja5Ut3y9lOFjm5yijXs3v80v4GAf-2Lqr1j57lfAgawveqRmPfl__-DtmtnJpQnb9OPfJNFqr7H-IJ-_5V8qBhZeKCcxCenMg4mT47-naih8BIJ5lviryfyeI3DeKOFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۹ جایگاه سی‌ان‌جی جدید افتتاح شد
🔹
مدیر طرح سی‌ان‌جی شرکت ملی پخش فرآورده‌های نفتی: به‌ازای هر ۱۶۰۰ خودرو یک جایگاه CNG در کشور وجود دارد؛ درحال‌حاضر ظرفیت توزیع CNG کشور بیش‌از ۴۰ میلیون لیتر مترمکعب در روز است.
@Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/460451" target="_blank">📅 14:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460450">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fb5fc4cfa.mp4?token=Q71d99wmS7RAG2V_xJY5456eIY_lFAIVwJFH0-XypVQg72PAAuzzeIeIMjctyxEBqZ9SwpOCPGtpdf9mc0zpE-vhBxcF9zmW0UE_hCX8vGHgklLBRMUtjU1JovEIW0hu_viVJyxnNXtRtXahTxRaQXQ8bsB3I0WcVZqVtGBME_D1OIRiDxb5uPu_LuU2dSO2_szHCx0CiNF3_mPyT9ey4A7gIWumVlUDFk29rDksHLQ-nqaYTa-yTGwVVWeeRFUyFBOWz4udGNN-1kozyIIvz4U4r-Tvrgp-HrKTEa8aRUmas2vW0z5bVgO5TA0Jia921iAdA_yticBpaf63HZhlfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fb5fc4cfa.mp4?token=Q71d99wmS7RAG2V_xJY5456eIY_lFAIVwJFH0-XypVQg72PAAuzzeIeIMjctyxEBqZ9SwpOCPGtpdf9mc0zpE-vhBxcF9zmW0UE_hCX8vGHgklLBRMUtjU1JovEIW0hu_viVJyxnNXtRtXahTxRaQXQ8bsB3I0WcVZqVtGBME_D1OIRiDxb5uPu_LuU2dSO2_szHCx0CiNF3_mPyT9ey4A7gIWumVlUDFk29rDksHLQ-nqaYTa-yTGwVVWeeRFUyFBOWz4udGNN-1kozyIIvz4U4r-Tvrgp-HrKTEa8aRUmas2vW0z5bVgO5TA0Jia921iAdA_yticBpaf63HZhlfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ نمایندۀ مشهد: قالیباف ادعای عارف دربارۀ طرح نفوذ را رد کرد
🔹
نخعی‌راد، نمایندۀ مردم مشهد در مجلس: «نیکزاد، نایب‌رئیس مجلس اعلام کرد ادعای معاون اول رئیس‌جمهور مبنی‌بر اینکه رئیس مجلس با خارج‌کردن طرح مقابله با نفوذ بیگانگان از دستور کار موافقت کرده‌، خلاف…</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/460450" target="_blank">📅 14:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460449">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVi8kI0SwCktkDudjMe0KMTGwgW0O-vii22raQYSIrm_yzSlYruEaswuMxaxU51d0GMeoadb4bLHbJhxduS-sQngp9ZdiS_FiVSWF_1cHuIpDNSHPUSmTclxMJfhu7t2Ok4x-zZf-S7qpCV7R12p9PSzhmZSfKX0FpHXrFqTX3jRblFjL6PXaDBRldPBhAYnQU00gpdxExg4GrTU9R5QoAWpeu6v5VvVgHKUUhhq7w1aOKo1JC-xn8mX_a8a3V22J1m9EUCdyy_FVk_ZQrDa1d7F-DsQ2HT9Tld4nt6_JDR9rSurCskRBR4OFS4bwvYFWpDPDA1sszHx08qfPR9c_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر عبداللهی: آمریکایی‌ها از ۸۰ سال پیش تا الان فقط از ایران نه شنیدند
🔹
رئیس ستادکل نیروهای مسلح و فرمانده قرارگاه خاتم‌الانبیا: آمریکایی‌ها بیش از ۸۰ سال است که از هیچ کشوری جواب منفی نشنیده‌اند و انتظار و تصور غلط آن‌ها پیش از تجاوز به ایران هم تسلیم این ملت بزرگ بود؛ خیالی باطل که هرگز محقق نخواهد شد.
🔹
دشمن تلاش می‌کنند خلأها و شکست‌های راهبردی خود را با جنگ نرم، شناختی و فشار اقتصادی جبران کنند، اما در این عرصه نیز قطعا کاری از پیش نخواهند برد و شکست دیگری را بر کارنامه خفت‌بار خود در جنگ نظامی علیه ایران اضافه خواهند کرد.
🔹
جمهوری اسلامی ایران به‌دلیل اعتقاد راسخ به ارزش‌های الهی و ملی، الگوی جدیدی از مقاومت را به جهانیان ارائه کرده است.
🔹
دنیای آینده با دنیای گذشته متفاوت خواهد بود؛ تفاوتی که به نفع ملت ایران و همراه با افول قطعی قدرت آمریکا رقم خواهد خورد.
@Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/460449" target="_blank">📅 14:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460448">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15f84cc0c8.mp4?token=spsETta4QwizB6GjvYhgGU45K31wLXybzpYw4oda-1Vrb47EsBxNPWj3QiFQJsMM2sLs4iiEB6zoIyDb4HvoyNKSGqWg8WymeydsCQTeDp9PenYFuC77fq6SxcWouzUw6MQo2sSWqRLc6kbreD24Mq4PVSHET6u7ld1XJe9F0N7OxCm64IIRZhDYRmZbsnfpFkyFuedeyr6UusCUOcpW_v-TySe_zQWjGdW5ELI3WGjekenTEqNddLpSKN7bTimsyL-GtsODiiCSCL7Zb_gKrfLpnpFPoZOFmXhRxvnEwvy-iIqsY0L9sx7rEl72KW1CnHi04X3WnpZrhAoeko7RtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15f84cc0c8.mp4?token=spsETta4QwizB6GjvYhgGU45K31wLXybzpYw4oda-1Vrb47EsBxNPWj3QiFQJsMM2sLs4iiEB6zoIyDb4HvoyNKSGqWg8WymeydsCQTeDp9PenYFuC77fq6SxcWouzUw6MQo2sSWqRLc6kbreD24Mq4PVSHET6u7ld1XJe9F0N7OxCm64IIRZhDYRmZbsnfpFkyFuedeyr6UusCUOcpW_v-TySe_zQWjGdW5ELI3WGjekenTEqNddLpSKN7bTimsyL-GtsODiiCSCL7Zb_gKrfLpnpFPoZOFmXhRxvnEwvy-iIqsY0L9sx7rEl72KW1CnHi04X3WnpZrhAoeko7RtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: همراهی‌نکردن کشورها با دشمنان ایران باعث شده تا تولید و تجارت در کشور ادامه یابد.
@Farsna</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/460448" target="_blank">📅 14:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460447">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08343fb206.mp4?token=Z2PmJwfndZNO-rIfIBC-WPzfzcVC76_Fh-qMKBlQ7OODynHL2selsUg23ONl-hDwUlJMVmc78PfZjJTFOl4nJw6xpQYq20lHFveG25ru9220xg8j-6UR5EDVkNYVSZDCoIy5EKGlLeWKy3WpjzAGIMymY5FUw0KxKHCXlbQdpe-UntEYLuWICWR4pIyh-38y_1F-Djr8eGyoPMbNBFqyAGW0H4T0XwYURJTzUdUSOH9YjbcR7LCRhSAMAuyn8QFBHsxs8kcNzyVEHGvDY_2Ud3wCpKkwEPiziH4VsHOrhIPdMSsofqjcq-W5FutPso9IikCFrviOg_HE0u6bksUPew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08343fb206.mp4?token=Z2PmJwfndZNO-rIfIBC-WPzfzcVC76_Fh-qMKBlQ7OODynHL2selsUg23ONl-hDwUlJMVmc78PfZjJTFOl4nJw6xpQYq20lHFveG25ru9220xg8j-6UR5EDVkNYVSZDCoIy5EKGlLeWKy3WpjzAGIMymY5FUw0KxKHCXlbQdpe-UntEYLuWICWR4pIyh-38y_1F-Djr8eGyoPMbNBFqyAGW0H4T0XwYURJTzUdUSOH9YjbcR7LCRhSAMAuyn8QFBHsxs8kcNzyVEHGvDY_2Ud3wCpKkwEPiziH4VsHOrhIPdMSsofqjcq-W5FutPso9IikCFrviOg_HE0u6bksUPew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: امروز بیش از هر زمان دیگری به عدالتی نیاز داریم که گزینشی نباشد و حقوق ملت‌ها را براساس میزان قدرت آنان اندازه‌گیری نکند.  @Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/460447" target="_blank">📅 14:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460446">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0PojgHC6oW0-GfGgIUNYZSozaOeXvVvKCXqJkQNy1L7hEfVzbEw-_T22tAOOq325_iVHdFXdlxHuQxtQirvj7ISPDi1geBX5t787dVlI95cA77g0d2ne1hwnD_wENyMzTlleqt3qCm8uSswnMQDWYHkzhK9MKIyYCu98AbJrjI7FhveDp8lA_ZoHns1_7P_ttsqf5MCTqJ3wk7IruchMwJllnW72JKeTIkROYn-RZ0Gzzv42TVoD2JQW8y1JFBWGf4T3AeMKn_H7zh9s7nUf-M0uPEkE1__9gbJBG5rabpt1Z3sk4XyZhfE1Lk8RsK5TdvO077syvKLJd3_39XkCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آهنگ: اظهار عجز برخی سیاسیون عامل جنگ ۴۰ روزه شد
🔹
مدیر گروه اقتصاد بین‌الملل مرکز پژوهش‌های مجلس: نمی‌توان مقاومت و تلاش ایران برای حفظ استقلال در منطقه‌ای که همواره محل رقابت قدرت‌های بزرگ بوده را رفتاری غیرعقلانی تلقی کرد.
🔹
جریان ساده‌ساز تصور می‌کند همین ابزارهای قدرت ایران باعث ایجاد درگیری و در نهایت جنگ شده‌اند؛ درحالی‌که واقعیت چیز دیگری است.
🔹
آن چیزی که منجر به جنگ ۱۲ روزه و جنگ ۴۰ روزه شد، نه اظهار قدرت بلکه اظهار عجز بود.
🔹
پس‌از ترور سردار سلیمانی، این انگاره تقویت شد که ایران در برابر ضربه توان پاسخگویی مؤثر ندارد و تنها واکنش لفظی نشان می‌دهد.
🔹
در نهایت پس‌از این جریانات نتانیاهو توانست ترامپ را متقاعد کند که حتی با هدف‌قراردادن رهبران ایران نیز هزینهٔ قابل‌توجهی متوجه اسرائیل نخواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/460446" target="_blank">📅 14:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460445">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J704HQ4jqZh4DTmgQjMWIvNm4M4HrIoXiod019F_R8sGjdiEWNpc9t5tieD2qExrP7RVhDkH38DiJqQ1eDclJw5e7i9NwvH8kvuPuBf9Pain2mf6S7G4-VdkDhZdG9lJOB3F6FTLkZYaz_hcT_lB_ysEfnJ_nvfNxF3peZ_DuwI_NOQgseTHh0EuNWf5KPQw1l2WdQqu7banNlEzE0vstPlyirNEcYYXuIs14mhTpNGecBN1uMkU0hv0ls87d5vSEnFZhMwcXMthjuPsimjqSQtHOxLmkzE_99rMm4arOztwHGx-SsEPNVtt78kVESCs_cf2DDLvdEGfj2ylS5F8mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تناقض در اعلام پایان خاموشی‌ها؛ این استان فردا قطعی برق دارد!
🔹
وزیر نیرو اعلام کرد که خاموشی‌های برنامه‌ریزی‌شده دیگر در دستور کار نیست و از مردم خواسته بود در صورت مشاهده هرگونه قطعی برق، موضوع را از طریق سامانه ۱۲۱ گزارش کنند.
🔹
این اظهارات به معنای پایان…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460445" target="_blank">📅 14:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460444">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0793651a.mp4?token=TpaIta0jtP0bMhaDEmtMkmu_IC-yIg0aE7xr-XHgf3ZDgXW6zpY6AJKAAak9063GuYB58zX3wSeqGYtAHipW_V_T4s4pDNhsQPbW87OR64N9AW67TjzK8OPKDaYq0xgek00H2uyXmcP4iFxbwnoW6r_Lx14n-7q7UDXas5y_F_5GZzVLFkrVDFqVmPlDXICiRgyyqgTNVXEReXay-YBOFH3nJwAYJcGXfy8fX7eHJO7aRV49Zur7-UKxilXjjWzB6wMEyEEyklzB53fgio9mlZs3xCWvlLOa-84RaZhmACPnLkmYKPBkYlTv9q0GiTSNGbkHcdpzCDejwG1dh0Y4PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0793651a.mp4?token=TpaIta0jtP0bMhaDEmtMkmu_IC-yIg0aE7xr-XHgf3ZDgXW6zpY6AJKAAak9063GuYB58zX3wSeqGYtAHipW_V_T4s4pDNhsQPbW87OR64N9AW67TjzK8OPKDaYq0xgek00H2uyXmcP4iFxbwnoW6r_Lx14n-7q7UDXas5y_F_5GZzVLFkrVDFqVmPlDXICiRgyyqgTNVXEReXay-YBOFH3nJwAYJcGXfy8fX7eHJO7aRV49Zur7-UKxilXjjWzB6wMEyEEyklzB53fgio9mlZs3xCWvlLOa-84RaZhmACPnLkmYKPBkYlTv9q0GiTSNGbkHcdpzCDejwG1dh0Y4PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ دستیار پوتین: مذاکرات با ویتکاف و کوشنر سازنده و صریح بود
🔹
یوری اوشاکوف: ویتکاف و کوشنر متعهد شدند ارزیابی‌های پوتین دربارۀ حل‌وفصل مناقشۀ اوکراین را در مذاکرات خود در کی‌یف مطرح کنند.   @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/460444" target="_blank">📅 13:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460443">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBlM4pfXNPv3-kh0ENv9qQDVjhQ35eDgvRvAe1BI_GRqndfaz4oGeCtF3klxMxfZu0Nicm9D-3EITQOzgIaxAApkJL9_4igOZQ_oKRft5x-jnyxTmw6-StkPYMxPBDWgoJvdJbBqtl7sEH7NB7J9BEXAwPn5oobH9uYmugumUURDwXrnEgEgsGHQqcfQgAaajBhzIzyDFrAOJvX5eIxGWshe_RoIYWxZUO0mngFjoMP2nw3tO_kn9uSWCuoGZxfaD3VbDTJlSzE2HpXFBI7OE_Y5Dzf5wZEmxUb7qTENCTwrt_RvhCJ4L0iY9V7T1LCWXEdGwn38tuyCQJZBmaeRqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانداری سیستان‌وبلوچستان: با رفع محدودیت پروازی فرودگاه کنارک در امروز، پروازها ازسر گرفته خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/460443" target="_blank">📅 13:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460442">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">عرضهٔ ۱۰۰ هزار سکه از ۱۸ شهریور
🔹
بانک مرکزی: برای اولین‌بار عرضهٔ «اوراق سلف موازی استاندارد تمام سکه» از ۱۸ شهریور در بورس کالا آغاز می‌شود.
🔹
در مرحلهٔ نخست ۱۰۰ هزار سکه با سررسید ۳ ماهه عرضه می‌شود و دارندگان اوراق در سررسید می‌توانند سکهٔ فیزیکی یا سود ۷ درصدی دریافت کنند.
🔹
همچنین امکان فروش اوراق پیش از سررسید به قیمت روز سکه وجود دارد.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460442" target="_blank">📅 13:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460441">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AN5ALIRo0-tDQ7yyipRuC8QRnHqDgIZa62iIiDZ8eFiZ3DuIZVnOOPqJlyY-urZEkAFtGbXa9bLvTtc1DM30fp3eK3d05t64xgh0FkBKdWQSwZmnY_iiOfL12mrh4BxJuYvoNMDR8A9NoMyWKvpR8QWz9JSZqPqMMDfat3SGnu9zcRvKJYcAgDb3CJuHcnJ9NfoFBg1Q-WCCFCQtZ41pEn1MBZhB6c8fDFJYgTD1LVO-A693F2kbAau-3RQrDKRy4dC_1Ofb81QNE1-QXUoN8OHONbAlocdrDg_YD_8coPWuQSzo7kAw8EEK7CxdjFI5IO4_vDxsmbEA8JKs803PJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح مقابله با نفوذ بیگانگان</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/460441" target="_blank">📅 13:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460440">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53de44c1e8.mp4?token=ae9xOdrvTjCFM9U9JoyhZsxW217AtBNAxfjVx4QoDDL_qCJqfLj-8_nTFS2jFod3utFBLl6WWii1aVCFPFOHBSdaYO6_egwxnDzsWMky2gZ8bnM3WIFnj6HnLR8KDhWwTv91vNNhsPOayy_-UbJLACMeGvHbwaAHt1ctnIu01VsnwcwUZARcx6rQUVnVm69u2AF4ao0z5WljdWTG5ECZyfJKzQcw04pV8vf8RHHId1LcEsXK6iXDjI_rrM1gbGU5FqOT3g2FWMA2rdjA5qW3Jmt85aU0E8xetYKLllLWVvCXNDo2vvakmKC4o3ollUpyqJk2iMx67TjBPMB7z6T5qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53de44c1e8.mp4?token=ae9xOdrvTjCFM9U9JoyhZsxW217AtBNAxfjVx4QoDDL_qCJqfLj-8_nTFS2jFod3utFBLl6WWii1aVCFPFOHBSdaYO6_egwxnDzsWMky2gZ8bnM3WIFnj6HnLR8KDhWwTv91vNNhsPOayy_-UbJLACMeGvHbwaAHt1ctnIu01VsnwcwUZARcx6rQUVnVm69u2AF4ao0z5WljdWTG5ECZyfJKzQcw04pV8vf8RHHId1LcEsXK6iXDjI_rrM1gbGU5FqOT3g2FWMA2rdjA5qW3Jmt85aU0E8xetYKLllLWVvCXNDo2vvakmKC4o3ollUpyqJk2iMx67TjBPMB7z6T5qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: سامانهٔ بارشی جدید از یکشنبه وارد کشور می‌شود
🔹
با ورود این سامانه در روزهای یکشنبه و دوشنبه در اکثر مناطق شمالی کشور شاهد بارش خواهیم بود. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/460440" target="_blank">📅 13:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460439">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بازداشت شهردار رینۀ لاریجان به اتهام اختلاس
🔹
رئیس دادگستری مازندران: در پی بررسی‌های انجام‌شده دربارۀ نحوۀ واگذاری و انتقال تعدادی از قطعات زمین متعلق به شهرداری رینۀ لاریجان، شهردار رینه بازداشت و روانۀ زندان شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460439" target="_blank">📅 12:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460438">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOclXDyQt3Z3PHVeqno7Yvjxv1rw0uXOhqPf3gOjPVRJcyyZEXYDsIO_oQ69uC9FMKwGmLvFoik72PI_RUAdQYS8gwLnnEWSX6VOFqoqWzNTc18T4_BEvb4kCbCNStfROcpT7vkUKbhNJcsXqFo0s4VyVe7fnpxkHY2K9Rh8mwOpsNy8gOaV9GnbPSoSNXh3d8pt_QxS4kfKkHTz0gOps9nfjQnf-X6tfUIiQj8BbPKClknhFT5L3S5POJd4ALjxrYG8VCCnNxDchndVyt00ca8Fjp6X6tdbxVvnLA6SmP5ZJB0EyVn9jIB2dYN6qrb7HGkuHXMAao-xQXvCtnomwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال دیدار سران روسیه، آمریکا و چین؟
🔹
در حالی که اظهارنظرها درباره دیدار روز گذشته نمایندگان دونالد ترامپ با ولادیمیر پوتین ادامه دارد، معاون وزیر خارجه روسیه درباره احتمال دیدار سه جانبه سران مسکو، واشنگتن و پکن حرف زد.
🔹
سرگئی ریابکوف در مصاحبه با خبرگزاری تاس اعلام کرد که برگزاری این نشست سه جانبه، «منتفی نیست.»
🔹
این مقام روس گفت که چنین قالب‌های سطح بالایی سیگنال‌های مهمی ارسال می‌کنند اما جنبه عملی آن به نحوه تدوین دستور کار (سه کشور) بستگی دارد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/460438" target="_blank">📅 12:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460437">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cc1768843.mp4?token=gSzB-gpVV8yLCM91-Vho95RyU138hmPPE5euzNIx8YuoY89MffCdQH9aKuxjlMpPyrc12gVPP9nC5o-xLWD8bIYvEjETeBJLuWiH_kVpNfKHxRtic9Olf8XA6wprF-ngwxMua5ZWvZtF4yYWSzWt73Y8eMx2pAG9bvlZD1OvjNkj2ydmYkTmY4rNdE3XLj5zwOcpO2rQcUKh6eL3w9UWWyQ5u4hmvmj8xs5ZTa5F7O9OHlcIU8yQehrC-5FGte7kcw1oxAA5SguPQuu5UilgYpXSY0aQ355PHQGJP2JZuMZLWToBR8mTNCIdcbvBUxHPRix5EkfBJecVzD6qQajVfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cc1768843.mp4?token=gSzB-gpVV8yLCM91-Vho95RyU138hmPPE5euzNIx8YuoY89MffCdQH9aKuxjlMpPyrc12gVPP9nC5o-xLWD8bIYvEjETeBJLuWiH_kVpNfKHxRtic9Olf8XA6wprF-ngwxMua5ZWvZtF4yYWSzWt73Y8eMx2pAG9bvlZD1OvjNkj2ydmYkTmY4rNdE3XLj5zwOcpO2rQcUKh6eL3w9UWWyQ5u4hmvmj8xs5ZTa5F7O9OHlcIU8yQehrC-5FGte7kcw1oxAA5SguPQuu5UilgYpXSY0aQ355PHQGJP2JZuMZLWToBR8mTNCIdcbvBUxHPRix5EkfBJecVzD6qQajVfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: تاکید رهبر انقلاب به پرهیز از ضعیف نمایی، دستورالعمل راهبردی برای تمام عرصه‌هاست
🔹
حفظ «انسجام درونی» و «قدرت بازدارندگی خارجی» دو ابزار مهم برای مقابله با دشمن است و هرگونه سخن یا عملی که به تضعیف این دو ستونِاساسی منجر شود،  نه تنها خلاف تدبیر…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460437" target="_blank">📅 12:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460436">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91f24840d9.mp4?token=FKehWaMmq86Mcr5oV00pkawi-VYgMd2d_raOqDriZeX4Hk4GJXR_bRPL3XSdQQ-hh9jrfUBghAZXiPXU-fgGXY-3cL6GfY0vSon9R-1UFmZVDXTz4pTUyIBSi_IcvlHdHF-kzjPHbm07hBRqCGvCl-20MX3PkL3Zwt7-wQZICtH7BDjkCPzVf_kkmwCHcVdilO5DBl-Ipo03qhRQbCvYM2q4q2QSByn1XH2im5MYGJCYqVXyglDkmugKqKADped_ne4ut6dUvrp-GEGAFB_yuzejRjFjvL77dfCq01PuouSCRb2pjRwePlWWRF7WdOe3Gaoy3vez-HThDxiUnZj_kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91f24840d9.mp4?token=FKehWaMmq86Mcr5oV00pkawi-VYgMd2d_raOqDriZeX4Hk4GJXR_bRPL3XSdQQ-hh9jrfUBghAZXiPXU-fgGXY-3cL6GfY0vSon9R-1UFmZVDXTz4pTUyIBSi_IcvlHdHF-kzjPHbm07hBRqCGvCl-20MX3PkL3Zwt7-wQZICtH7BDjkCPzVf_kkmwCHcVdilO5DBl-Ipo03qhRQbCvYM2q4q2QSByn1XH2im5MYGJCYqVXyglDkmugKqKADped_ne4ut6dUvrp-GEGAFB_yuzejRjFjvL77dfCq01PuouSCRb2pjRwePlWWRF7WdOe3Gaoy3vez-HThDxiUnZj_kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: در کنار میدان نظامی، اصلی‌ترین نبرد ما در میدان تولید و معیشت مردم است
🔹
مردمی که تا پای جان مقابل دشمن خونخوار آمریکایی ایستاده‌اند، سختی را تحمل می‌کنند اما سوء مدیریت و کم‌کاری را تحمل نمی‌کنند و ازما انتظار مدیریت سریع این میدان را دارند؛ و…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/460436" target="_blank">📅 12:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460435">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/628cd260b7.mp4?token=a3h4bnmf5jGPFvdaSISs5_Mo5eui8kTscRviTwq3kZsR_hfj_8oW_w1UakFpP4T6HOEhzNLfVEz9pB2K3TNLZinzi1ffJl3k6TApo7mBXs6FctEbn3QtfAlqq3Bd0QZ-WxFxLCiDyYlvk4-54_Q6LNEtPCZS2pkpPanMSLl43DdJMfjcTcWEVjVEhNXI_WvEkrd01DOQWd35RfO5kcbAqgzXr7lKWw8wWkL4EUtDOvMgo3XR23Vd766Kf5dyKvuSfy-ZmJUXwI9eu6Pn2A2Sut6MetOGxqP1D1ki9RGevuJTmcqOiuOvZLkBfW3yu8l9aQOyxydh7sCr-Pjl9wQ0fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/628cd260b7.mp4?token=a3h4bnmf5jGPFvdaSISs5_Mo5eui8kTscRviTwq3kZsR_hfj_8oW_w1UakFpP4T6HOEhzNLfVEz9pB2K3TNLZinzi1ffJl3k6TApo7mBXs6FctEbn3QtfAlqq3Bd0QZ-WxFxLCiDyYlvk4-54_Q6LNEtPCZS2pkpPanMSLl43DdJMfjcTcWEVjVEhNXI_WvEkrd01DOQWd35RfO5kcbAqgzXr7lKWw8wWkL4EUtDOvMgo3XR23Vd766Kf5dyKvuSfy-ZmJUXwI9eu6Pn2A2Sut6MetOGxqP1D1ki9RGevuJTmcqOiuOvZLkBfW3yu8l9aQOyxydh7sCr-Pjl9wQ0fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: آمریکایی‌ها حتماً فهمیده‌اند که دوران «پاسخ‌های متناسب» به پایان رسیده است
🔹
هرگونه تجاوز به منافع و امنیت ایران، پاسخی «سریع‌تر،سنگین‌تر و دردناک‌تر» دریافت خواهد کرد.  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460435" target="_blank">📅 12:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460434">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90cc48db21.mp4?token=CqkyaQ9Lcdlez7XAs0jNGtfDZDDPEOUTwACpXuSy09_vnBSp-xOC5R0QyOZBOG9AUrCf-82e4Wq8_X8UMozgYHInHo88XhDbgCvEgertTyWkPE02zoHMfWsrlz9eKplODxt3VmqtS5bQEmj2UZRvLQiJbmgc1yNrdlW98tQ3OCdD9Y7j00Z-Ry7sd9Cjf9S7x6GZvHIFi1MDOjiShtNVbx-XeMGErRpr5ar1ENMWwWAGINcvtVprZbAzYMMrFUi70LbO0Qy9qyrpe1PiHuKpmMUKD6u4xNjEBVtxp5INUdxn28ezEST_sRK9I_OiI9N1dsI-RHendgyUJSScySX7xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90cc48db21.mp4?token=CqkyaQ9Lcdlez7XAs0jNGtfDZDDPEOUTwACpXuSy09_vnBSp-xOC5R0QyOZBOG9AUrCf-82e4Wq8_X8UMozgYHInHo88XhDbgCvEgertTyWkPE02zoHMfWsrlz9eKplODxt3VmqtS5bQEmj2UZRvLQiJbmgc1yNrdlW98tQ3OCdD9Y7j00Z-Ry7sd9Cjf9S7x6GZvHIFi1MDOjiShtNVbx-XeMGErRpr5ar1ENMWwWAGINcvtVprZbAzYMMrFUi70LbO0Qy9qyrpe1PiHuKpmMUKD6u4xNjEBVtxp5INUdxn28ezEST_sRK9I_OiI9N1dsI-RHendgyUJSScySX7xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف:
آمریکایی‌ها حتماً فهمیده‌اند که دوران «پاسخ‌های متناسب» به پایان رسیده است
🔹
هرگونه تجاوز به منافع و امنیت ایران، پاسخی «سریع‌تر،سنگین‌تر و دردناک‌تر» دریافت خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/460434" target="_blank">📅 12:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460433">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psYH2WsSlSl1QfFc4qGuQWDb9HrgNGc6uWOeBWv45VXeDEZZj2VE0XsmN3ZdZBEDiWeF5l2hQ19kNmWgNHkKzuhhsX-WfaJvnkn4ZfU4q13OBdNxs2q413WUma5_SRc0RtLXjkgavIm5Di6BqJqt7nDC_vdYvdk-sFTcB8lVvQHIFPR6UD_Uxw_O5wt5CqwLy_kj_D2kpW6wlUb7PEtLP6t5gBlyf8Ve3PMgY45YAAM_Ayq2VwddbXQzNGqtXJJ6pkhE2xDsE0DcOn9UD11tjYGenE3nDXcegm5t7qHzoRru1OJDjUfbfvi5jb3i7pQgNh9RxdflHzG2NDfIuTlOpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس رکورد ۶ میلیون و ۷۰۰ هزار را هم شکست
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۲۲ هزار واحدی به ۶ میلیون و ۷۲۴ هزار واحد رسید و رکورد تاریخی جدیدی را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/460433" target="_blank">📅 12:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460432">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEdxEeXY6n9UBXsFTKQfCNY81Fynlr-sfbgYf1PshpcfRzNABQThDv6tpDvziD6aGB1H0VRcpqmbTn2HBO7jIDXUcAGQ4IgtBOOwIKDfenv6J5YtFdtIUlS-hGEQhyp726cYQS_NDxB4Y8KRzoZVfq9ozsLSo1XgfRg3_fbaMCy5Q-IXgVndeXRaRFEfK0y5ScBgNSdexv7DxpSCU3rOXQJXYpr0hHxUt-sjfY3crzaVI7OTAvr2Z_idXc2lh1OYOevnLa_zpgpf09bNadrx8WXDXKf6Jlhc10iOR3oxmmzROXuXPcx5e4J_ZrOLrZzXMa07K5NVt4JdtHVHJnTr6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای روحانی، دوگانۀ اصلی، «مقاومت و تسلیم» است نه چیز دیگر
🔹
اظهارات حسن روحانی دربارۀ اینکه آیا مردم حاضرند «۲۰ سال دیگر» با قدرت‌های بزرگ بجنگند، با انتقاداتی مواجه شده. منتقدان می‌گویند پیش از طرح چنین دوگانه‌ای، باید دربارۀ تجربه ۸ سال اعتماد به غرب، مذاکره و توافق و همچنین بدعهدی و فشارهای طرف مقابل توضیح داده شود.
🔹
علاءالدین بروجردی در واکنش به اظهارات روحانی تأکید کرده طرح مسئله به دوگانۀ «۲۰ سال جنگ یا راه دیگر» بدون توجه به رفتار طرف مهاجم، صورت‌مسئله را تغییر می‌دهد.
🔹
عبدالله گنجی نیز از روحانی پرسیده «راه دیگر» برای پرهیز از تقابل با قدرت‌های بزرگ دقیقاً چیست؟ آیا این راه به معنای عقب‌نشینی از حقوق هسته‌ای، توان دفاعی و موشکی یا پذیرش امتیازات جدید در برابر مطالبات طرف مقابل است؟
🔹
جواد بخشی‌الموتی، استاد دانشگاه هم  تاکید کرده که کسانی که در گذشته به‌دنبال بستن با «کدخدا» بودند و امضای کری را تضمین می‌دانستند، امروز نیز به جای پاسخ‌گویی دربارۀ نتایج آن رویکرد، تلاش می‌کنند با فرافکنی، افکار عمومی را از کارنامه خود دور کنند.
🔹
محمدامین سلیمی با اشاره به تجربۀ برجام، لوزان و سعدآباد تأکید کرده نگرانی اصلی، مذاکره با طرفی است که سابقۀ نقض تعهدات دارد و مشکل زمانی ایجاد می‌شود که پس از توافق، طرف مقابل همچنان فشار و تهدید را ادامه دهد.
🔹
محمد اکبرزاده، فعال رسانه‌ای هم خطاب به روحانی تاکید کرده: اگر متجاوز وارد خانه شود، آیا ابتدا باید از اهل خانه پرسید «دفاع کنیم یا نه؟»
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/460432" target="_blank">📅 12:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460431">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPfRXZHxQ42hH_rpm-g-OfEyQ8QZ_hjiQqYowUPLCwiY2_L2EqQSsgQUocjnH134ixxebo2eNGWyUHFvdG1VdwYmvhr9NTg2Q6aid4nMG0Jp_ChlDkKqiJs9jS0cP1P8WwKFTyj8DI7mmesdUKAXf0GFv4IoBIte1jBo98MU0QlGf0zv1PXeu4XSsQ-JctfBy6i1N3vQL3R6Qv-0cmO02SeS7zrFbFaSbT8WolY3Ak1gpXG9xxsBsz5FamRyOS35_TVfL0PHcb1KWg5OIF9Q5wAabpyLgtYT-HK5_1UTdFHmidp1_ef7vOPpky-s5JW6v-IR0xMkjKZ1fcGfMr5pJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاهان از استقلال شکایت می‌کند
🔹
باشگاه سپاهان به دلیل استفاده از یاسر آسانی در دیدار مقابل استقلال از آبی‌های تهران شکایت می‌کند.
🔹
پیش‌تر آسانی در دو بازی اول لیگ مقابل مس شهربابک و نساجی هم بازی کرده بود و طبق اخبار منتشرشده به همین دلیل شکایت‌هایی علیه…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/460431" target="_blank">📅 11:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460430">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnP-C6D_ynVeCPIWkZrPvm0sF-lZR_2__hqccbHhc1IlvmPrIhq6ZZcBZCTDWVyFM8Uw1ntG6IS1u2sot_S6mxJNPFUddY1-FxOl3KftPdZGbHHYp8Uoyy7RNkiRyCUeuZqSpRAXY0cniJPrknEfMHGYGFDG-OBy20SpJnjiWXtDYzdLCsNKz2_teacSTm4fiKlCTNzOw_3CFIGxcNABStZw-7j_Ij0eUct1EdfNroaiLhlcIA372LeOVWF_sM2WTRfOgG8mxZe0_LMRT8BFR_R54rHpyedRCPjqs3oMTRwQjkt7var_6lGHSXBlgLaDplfxViiNEEYbiKHB2FruHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت مرغ کاهش یافت
🔹
براساس گزاش میدانی، هر کیلو مرغ به ۲۷۰ هزار تومان و ران مرغ به ۲۰۰ هزار تومان کاهش یافته است.
🔹
وزارت کشاورزی اعلام کرده نهاده به حد کافی وارد شده و بخشی از آن توزیع شده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/460430" target="_blank">📅 11:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460429">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcQN5RN-XscTwLa9RNOa_eAuE7kMVw1sGvDzxJeeJw8BEWF5Ic91Q4RQO6zvdnisPJ5eyj6C-IjUK45U1qhNkl-KbMwuu0sZCjMO_QNdlLvabx_uKLD9sM6Ula9w3DwFmHcV0stiRRlAYE15FphV0dnhVjL2s81Kr9k3OAsSQvOQbsk2-9mIMtjW2wnRstQpLh0JXl-_yKMkVUefmbiWBD-Ob2GTzWx1MAFD-rdaKfw0d0vF5LjprI1A9-MUlnKH8h9u-zpKTi7wvkU2MKhUl2GTQNHwdytGler7SKx7Pyxf0explgVCIKR8tF2pVMfP5PkMtEqePF1ihRxWHlkf5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور ابلاغیه برای خداداد عزیزی
⚽️
با اعلام کمیتۀ انضباطی سرپرست تراکتور به‌دلیل تخلفات رخ داده و بدرفتاری در قبال مقام رسمی مسابقه، باید ظرف ۴۸ ساعت دفاعیات خود را ارسال کند.  @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/460429" target="_blank">📅 11:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460428">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_ZwDpHPESNz3qJofmdPjHCUSSxnCtwfMTdl-htfYGeA27Zgqi-tGscmzow7_N3dCCwC0ZVH7X2ldxVRCYi24XSgSsSClIdac559DiCqE9yLhRImDXfF92LUrfLn6gMVOQNx1Nrkncbko46EtLMVe1sKXk1naZTszvFklLYuTGD9EGpDBKc1AGC60NSPOYw5aAwVZL62JIj-mMB5A9nlN-3S0qMgQ-t_E2Q7D_TB8cuH9e2QFmrHf7cLOua67wFt-v1C4A0RvslFgdpRUJlFNxbGoLcp_lWJGxsB-zxwdQEzVl6JwZvuNnHHDeLMzu_HhMehDaqbIjMUQeH1PhDd7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نهاد مدیریت خلیج‌فارس: فهرست شناورهای متخلف بروز شد
🔹
برخی از این موارد با اطلاعات داوطلبانۀ مردم به‌دست آمده است. @Fasrna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/460428" target="_blank">📅 11:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460427">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">چمران: متروی تهران فقط تا ۱۹ شهریور رایگان است
🔹
رئیس شورای‌شهر تهران: مترو و اتوبوس‌های تندروی تهران تا ۱۹ شهریور رایگان هستند؛ ادامهٔ این طرح به شرایط پایتخت و تصمیم دوباره شورای‌شهر بستگی دارد. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/460427" target="_blank">📅 11:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460426">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvZmQ31PJb_EuvZbVnWFRAMB1tlUj7pfTQ-rVyMClUS4OcbX5gwSTewrzg58tzG6fwLndba-jtqai5AsRqTC5xdRwRIdhtZjg58gLnNoEBkHsqxPAQhJK2xbqI6JCn4-Ic7MIvVbcNuCarMvfEbZ7ewK38rwBXjp02y7xgfMaKdfxdYSF5FksgV1mpvBojzbIbOzmy4g3NvtVUU7inKF97EKK2HqJmSJLDWR6iBwMbh2GGzEgu1zSx0Rr-U-eeI2hqicIZtLnUr1rOLTjKvmQQ_96_FSSTPrAqVUd0k7dbiNIXqAgT0UxT-FFz4T2VPsceupzOLse4u699wNfKwikQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان‌باختن ۱۱ شهروند سنندجی در آتش‌سوزی تانکر سوخت
🔹
رئیس مرکز فوریت‌های پزشکی کردستان: در پی وقوع آتش در یک دستگاه تانکر حامل مواد سوختی در پلیس‌راه سنندج - همدان، ۱۱ نفر از شهروندان جان خود را از دست دادند و ۵ نفر نیز مصدوم شدند.
🔹
به محض وقوع حادثه، تیم‌های…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/460426" target="_blank">📅 10:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460425">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شهریهٔ اجباری مدارس ممنوع شد
🔹
آموزش‌وپرورش: مدارس دولتی هنگام ثبت‌نام حق دریافت هیچ‌گونه وجهی ندارند.
🔹
مدارس غیردولتی نیز تنها مجاز به دریافت شهریهٔ مصوب هستند؛ فعالیت‌های فوق‌برنامه نیز باید کاملاً اختیاری باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/460425" target="_blank">📅 10:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460424">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GorMMSFkdAzG4gOXEeC-2QDxLt2q3QUQaC3aZVBSDdYyWz5M6sNp5q20l1Eij5oqoOa1fejFtiGC2MqqH7WtD_S2DJYTIpm3FB0RSmqZQAaCKJmMzvPcTM4AEFl6k4czhhBNMp2YLGZcYVJB8X60GNCmTyI1b1aueBOO8YV2g0mcldHCPEhAxApCzJ9qp9KbVDFkoB4pj53P1p8hYixMZ09c_gftyrlE49ypD2s7uktDIW2pe87jsUAm4u1qSjMe2eavnzTBG9DjqtrN_Ux495f7q7ITpa9sHeiQYrvirWZwqOZsqb9ftSH7c7rI2clK9Jo2Pfnjnmwl2ED1M8U8yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمسایی: با تلفن و سفارش، کسی ملی‌پوش نمی‌شود
🔹
سرمربی تیم ملی فوتسال: برای حضور در اردو بازیکنان را براساس کیفیت و شایستگی انتخاب می‌کنم، نه تلفن و سفارش.
🔹
تمام ۱۴ تیم حاضر در لیگ برتر را از نزدیک دیده‌ایم و هر هفته آنالیز ویدیویی و جلسه مشورتی برگزار کردیم و به فهرست نهایی بازیکنان نزدیک شده‌ایم.
🔹
به‌زودی بازیکنان موردنظر را برای حضور در اردو دعوت خواهیم کرد. شک نکنید که خودمان را مدیون حق‌الناس نمی‌کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/460424" target="_blank">📅 10:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460423">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/147a8f9b1c.mp4?token=Gej-g7DBn9y_TiXiVOW1uPr1sRCkPOkmnpAR5c9H3e1a76m-wLRbB9kSW4j-eB-SgqXH9BUl2ftcKBIbdhu3OLwH3JsGoW34nVyOfL2x25xkD--s_qEvvlE2CgbjlGBAoJkoutDgfgbsF-gDVUgA7y7YASPHlSOV5jUZCet1zNNJmZkJaVrS9xDk3HFuABaWzHFILVcDliLtMca7FxqtzKhEsTh6i_rBxJbLWUKmGmid8zUgANbM_SGmMmL0zZ0me1GOnqjZ7xaPcunjgPopJ6mxluQDZI5M_lvNfWgKdPA40bWvBH94-Q3G6UV8W-n0eAlk0qJp6omV5U0ZU0zfaqowg9VD0UHuyxwSpF1CnjdIkf5ve-fRrXnZHvz7x4wen04DSVw4QrhKng51jMlNHcNRtiUjwsB4jIIXyx_HJMi17kuim20Th-vW-41jLjoU6lJ6ZVWDXW30cGq6HjUhj3DXsxBQvY4A17Do9ZtugI2uXH2hlHIF16i7a_ecsip6hqf7qt7evmVmZNQHzcMQwBJ4J0w0gg00Qq-kT2TsRFFofU7OEcyJNsxn7xu9LjV4wbtEy0T6v_vK5tJrFjdAoPTM9s_8J3ISWwn8y2d6GrJz0oXqRLWV5N2Kx3bypfOMpSIYLhuNrg4dFKtfh1NMHWDVG-8BnYJi4HcTOUyi3wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/147a8f9b1c.mp4?token=Gej-g7DBn9y_TiXiVOW1uPr1sRCkPOkmnpAR5c9H3e1a76m-wLRbB9kSW4j-eB-SgqXH9BUl2ftcKBIbdhu3OLwH3JsGoW34nVyOfL2x25xkD--s_qEvvlE2CgbjlGBAoJkoutDgfgbsF-gDVUgA7y7YASPHlSOV5jUZCet1zNNJmZkJaVrS9xDk3HFuABaWzHFILVcDliLtMca7FxqtzKhEsTh6i_rBxJbLWUKmGmid8zUgANbM_SGmMmL0zZ0me1GOnqjZ7xaPcunjgPopJ6mxluQDZI5M_lvNfWgKdPA40bWvBH94-Q3G6UV8W-n0eAlk0qJp6omV5U0ZU0zfaqowg9VD0UHuyxwSpF1CnjdIkf5ve-fRrXnZHvz7x4wen04DSVw4QrhKng51jMlNHcNRtiUjwsB4jIIXyx_HJMi17kuim20Th-vW-41jLjoU6lJ6ZVWDXW30cGq6HjUhj3DXsxBQvY4A17Do9ZtugI2uXH2hlHIF16i7a_ecsip6hqf7qt7evmVmZNQHzcMQwBJ4J0w0gg00Qq-kT2TsRFFofU7OEcyJNsxn7xu9LjV4wbtEy0T6v_vK5tJrFjdAoPTM9s_8J3ISWwn8y2d6GrJz0oXqRLWV5N2Kx3bypfOMpSIYLhuNrg4dFKtfh1NMHWDVG-8BnYJi4HcTOUyi3wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تودهنی فرمانده سابق سنتکام به مجری ایرانی صدای آمریکا!
🔹
ژنرال دیوید پترایوس، فرمانده پیشین سنتکام و رئیس سابق سیا: شکافی در میان نیروها در ایران وجود ندارد و رویای فروپاشی حکومت شکست خورد؛ راهبرد استقرار پایگاه‌های آمریکا در منطقه جوابگو نبوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/460423" target="_blank">📅 10:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460422">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2CQ9mhzPogWcPv-UvRerFvDQCQA8ehM6T98lnr6zkmggyMqCwkl9b3KboCjODN6FPGA7mmTfjyaEeVsap6KJ_COR7XhGKXbnDapLK33MnfT0Uk8XYbKz3XZTvmNp03u7UB_p0ad4prU84g_EszB_J-v9__3DWcpgnAMHeTrko_J4aMha6dVA-w-4xncyqoFatwW1ih3zCgmopDash1HC_XApATI5Dt1R5QETbe4MGeESPTamoWnYabsynC9PzQ1uL7cchfvzXJAa5kRdXiasIoSecabx4CiK4zKYAAl2fM_1oFmA875ACuCAdsijylv5J4I0PZ21Fq4oPfS3B-w-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بار خداداد را سنگین جریمه کنید
🔹
پیش از شروع مسابقه تراکتور و گل‌گهر مشخص بود حضور امید عالیشاه در تبریز، با توجه به سابقه تنش‌های ایجادشده میان او و هواداران تراکتور و اتفاقات جنجالی دیدار پرسپولیس و تراکتور در سال ۱۴۰۱، می‌تواند فضای ورزشگاه را ملتهب…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/460422" target="_blank">📅 09:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460421">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cc4adf04c.mp4?token=phl8vdL76HZvBYMdCCJv4DMhvuJUjH-qLWq1eg2UGd_ItGZ2C-efotibctFwjstl8g88pmaUKOikqwEgSrlLIQEGe3Yk1iFql3T-6D_WFOmVkhGX4x9041O6QCAjkFJ01kpmtQWesUxdEe0DOPMZLNYpDE1DKNVdzrJIUQHHjEMTl-YvT7khgP_TnRS1TX26wbocRXeP1V54WbN5VqTiFpovmgvV7YIqAx-Mifgvwj5isBvjVyt5FK-QD5KSTwzvb8h1xmqM0I1pIemqZfy-wFqbs8XSZJtD0RLqDug0WvfRBRSbMCJl4gp2BFdEYubbYb1OpQRdhnWOW4A-8ILx3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cc4adf04c.mp4?token=phl8vdL76HZvBYMdCCJv4DMhvuJUjH-qLWq1eg2UGd_ItGZ2C-efotibctFwjstl8g88pmaUKOikqwEgSrlLIQEGe3Yk1iFql3T-6D_WFOmVkhGX4x9041O6QCAjkFJ01kpmtQWesUxdEe0DOPMZLNYpDE1DKNVdzrJIUQHHjEMTl-YvT7khgP_TnRS1TX26wbocRXeP1V54WbN5VqTiFpovmgvV7YIqAx-Mifgvwj5isBvjVyt5FK-QD5KSTwzvb8h1xmqM0I1pIemqZfy-wFqbs8XSZJtD0RLqDug0WvfRBRSbMCJl4gp2BFdEYubbYb1OpQRdhnWOW4A-8ILx3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قبل از خوردن انگور خواص آن را بشناسید
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/460421" target="_blank">📅 09:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460420">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqwDp_NEsoOqRptnEr19I3WrDKYf_M42WI9SQM6DSBkIylOO5Kz0z3FvEur0Xf-Tqmw7RPCaeJOtAp3Nv6O_RS8hF_Kam-iqvs-x-3yT0Yr42pJkqW2O_rfm_Jgsq5Q4Uz_TFAHQQ1AdirLdviWHulof70XtOCF95SsqDireYBSGuxZmcBliFzl1ydW3XqWurZ8s5IL3YMzfrL1YZxZiuYwncEQZlqsyGobYYIhl9I0Bni87Kc7JNVDdFM0eWU93I4g9Ub0HB7Vm9lDLoiGsaKznTuHZTYI1HWXQ5kqlUGdWmnkd9MBwW3iz_Udw4X3-limUWaZEp1qOnaijZYcQBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تشدید حملات هوایی و توپخانه‌ای رژیم صهیونیستی به جنوب لبنان
🔹
ارتش رژیم اشغالگر دور جدیدی از حملات هوایی و توپخانه‌ای سنگین را به مناطق مختلف جنوب لبنان آغاز کرد که منجر به تخریب ساختمان‌های مسکونی و مراکز درمانی و شهادت دست‌کم دو نفر شد.
🔹
بامداد امروز، جنگنده‌های ارتش اشغالگر حملات هوایی گسترده‌ای را علیه چندین منطقه در جنوب لبنان، از جمله شهرک‌های «القنطرة»، «زوطر الشرقية»، «نبطیة الفوقا»، «نبطیة التحتا»، «وادی السلوقی» و «دوحة کفر رمان» انجام دادند.
🔹
گزارش‌های میدانی حاکی از آن است که در جریان حمله هوایی به شهرک «کفر رمان» در شهرستان نبطیه، یک ساختمان مسکونی سه طبقه به‌طور کامل تخریب شد. همچنین حملات متعددی به اطراف نبطیه و شهرک «عربصالیم» گزارش شده است.
🔹
هم‌زمان، توپخانه ارتش اسرائیل منطقه «نبطیة الفوقا» را هدف قرار داد که بر اثر این حملات، خسارات گسترده‌ای به «بیمارستان غندور» وارد شده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/460420" target="_blank">📅 09:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460419">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQrBrnryay0kdGrXJ51tFHlCJ5Rz7928n4pJ-yvZncRH5BQKmyc_OawhQqS1GAtqy2OupM2d87qf8Tvzjqa8iv1ZaLemMLQkOPcSOJiRZeHm61hX5EJGN-SQlraLJVqNoVRg49SHsgWqVtqgEf7E2rABpdF08IlT8lKr1eM0rC2J-1n2V_4ZPERjp2AobWgm3JA9yiVDRaait2kn4sddTtSgZmnRtMjPQiH2G0EYbwRI9Wm6RCYqnzrEDp9ylZhyLyK8rvd8xZHstQnxzGqOiXOHLk9HQh7Ok4EYvZcRPoEV8QJmYJjzQOvnNjBXQ-afHevZXvj1dJUPOe27e-r9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/460419" target="_blank">📅 09:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460418">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goJBAj66MgJkT6vJuZJDhxZ5AeZITHGbN91Ialvo7T4ZEOWWc0AqslzA-5QEfzMayBPUVjT8fJNVodbQquL_s9Xk69viZrX6M-ZUgmjS7J8aIThxW9oa_I-jlSZVHmvda23PL2F6yGDBdIVdQC8XBIOArOzFKPTq5moXDvA6vK63xJLZp5d5e8qcHQQ4N2ky9mWHp2Y4_sr6Vygd3xbiLjS-Th-iUe-15PIIxASlavshi-wCZNU50-vQsyt7jkcKilc5LzF39Je724LDIBX_TJE2RPymPfywLKXuy4Y0TKEf0w8A4yfSOYsGvcMh95QDp3iFzp1MRjk0R1PpIg5_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسهیل ورود پلاک‌های بین‌المللی به کشور
🔹
گمرک ایران با صدور بخشنامه‌ای، در راستای حمایت از گردشگری خارجی روند تردد خودروهای ورود موقت دارای پلاک بین‌المللی را تسهیل کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/460418" target="_blank">📅 09:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460417">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4309078e57.mp4?token=hEK6NPH7SNKb0BzZUuQHIYMW_1Zn3IiEq1Pxn4tB6rAQ-PNd1svUWmnLZpz9vyiHvcWPtoI40BDhZsYOG_OIgWjLObYWVxTs8X495NjKrlIclrGU8aBNaMXfBitQXycNH9QZL6cZiBbyqmbCM6PhzB42WQpiuzz5Bn7paeYBywC8e3Ubt7HqDdOxjWbTCrkyP8LvY8io5jnX3t7DcIJqyV3q2n7RhKJ9b4F4UJ-lTg0ECu7pXIqJ4121TifE8_XyDKmlNPvEbuonKUig8JvOUWKrVVlKbM6TiLGy5pS_PPofSGKIVulR5LJN1NUhjmVDf2brOqi4scsqk4ZkAjQBnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4309078e57.mp4?token=hEK6NPH7SNKb0BzZUuQHIYMW_1Zn3IiEq1Pxn4tB6rAQ-PNd1svUWmnLZpz9vyiHvcWPtoI40BDhZsYOG_OIgWjLObYWVxTs8X495NjKrlIclrGU8aBNaMXfBitQXycNH9QZL6cZiBbyqmbCM6PhzB42WQpiuzz5Bn7paeYBywC8e3Ubt7HqDdOxjWbTCrkyP8LvY8io5jnX3t7DcIJqyV3q2n7RhKJ9b4F4UJ-lTg0ECu7pXIqJ4121TifE8_XyDKmlNPvEbuonKUig8JvOUWKrVVlKbM6TiLGy5pS_PPofSGKIVulR5LJN1NUhjmVDf2brOqi4scsqk4ZkAjQBnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود سامانۀ بارشی از شمال‌غرب به کشور
🔹
هواشناسی: بعداز ظهر امروز و اوایل شب سامانۀ بارش‌زایی از شمال‌غرب وارد خواهد شد و در نیمۀ شمالی بارش‌ها آغاز می‌شود.
🔹
دوشنبه و سه‌شنبه دما در نیمۀ شمالی کشور کاهش می‌‌یابد.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/460417" target="_blank">📅 08:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460416">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O19JBmvRgF8ITQHNX3orlQmmxY0yyHNY9N7hhe7xxa93-BmZn8jg5GGC5Ew-OrKU2P1DcJeermsuRrP2UFMhYRjSSSJTFy5VIfmjIqY89jq_w2F1DpXSGO__DkTWLwmy5UDbkVo7zbwFT0cvkLBJjzLpUAjuWYvknfmELO8zeesKho-tMnc0P4vnAyIDHZELVDgKVg81HftjiVAPkfQScTinaF_0lPFlO6mw-O3P558N3BRXoupBsChwcjvX8_w0RNVNGySwUF4yTglOo7N1HCCaEoPE3efwe4Q7k24-TZ8V7Qp-8NdYP6xbOKoYrP5qeJdZ4hGGgsq8sIFSm86tOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سگ‌ها را کشتند که رضاخان بدخواب نشود
🔹
دستور مستقیم رضاشاه برای شلیک مسلسل به زائران حرم مطهر، تیر خلاص به نوزادان در گهواره و مسابقۀ شرط‌بندی روی دویدن مردان سر بریده؛ این‌ها برش‌هایی افشاشده از جنایاتی است که رسانه‌های غربی امروزه با سانسور شدید، سعی دارند آن را «عصر طلایی مدرنیزاسیون ایران» جا بزنند.
🔹
در شرایطی که دستگاه‌های تبلیغاتی غرب دوباره پروژۀ تطهیر دیکتاتوری پهلوی را فعال کرده‌اند، بازخوانی اسناد دیپلماتیک و تاریخی آمریکا و اروپا، پرده از حقیقتی هولناک برمی‌دارد؛ حکومتی که دیوارهای بنیادینش نه بر توسعۀ ملی، بلکه بر سرکوب و وابستگی کامل به بیگانگان استوار شده بود.
🔹
محمدقلی مجد مدرس مرکز خاورمیانۀ دانشگاه پنسیلوانیا، در کتاب «رضاشاه» می‌نویسد: رضاشاه هزاران نفر را حبس کرده و صدها نفر را کشته بود و بعضی‌ها را با دست‌های خودش به قتل رسانده بود. در نتیجۀ این حکومت، وحشت بر دل مردم ترس افتاده بود. به کسی نمی‌شد اعتماد کرد و احدی جرئت اعتراض یا انتقاد نداشت.
🔹
ویلیام داگلاس، قاضی دادگاه عالی ایالات متحده، در کتاب سرزمین شگفت‌انگیز و مردمی مهربان و دوست‌داشتنی، می‌نویسد که چگونه نیروهای نظامی پس از ورود به چادرها، هفت‌تیر خود را روی سر نوزادان در گهواره می‌گذاشتند و مغزشان را متلاشی می‌کردند.
🔹
داگلاس از زبان یک شاهد عینی می‌نویسد فرمانده ارتش، مسابقه شرط‌بندی عجیبی به راه انداخته بود: «سرهنگ طاوه آهنی را روی آتش سرخ کرد. با شمشیر سر جوانان لر را می‌بریدند و بلافاصله طاوه سرخ‌شده را روی گردن بریده می‌چسباندند تا جلوی خونریزی را بگیرند و شرط می‌بستند که بدن بی‌سر چند گام می‌تواند بدود!
🔹
جان گونتر سیاح آمریکایی فاش می‌کند که حتی سگ‌ها هم از قساوت اعلی‌حضرت بی‌نصیب نمی‌ماندند؛ وقتی شاه در سفر است که البته بی‌وقفه در سفر است در هر روستا و قریه‌ای که شب در آن منزل می‌کند سگ‌ها را می‌کشند، زیرا او خواب سبکی دارد و هر صدایی او را پریشان می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/460416" target="_blank">📅 08:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460415">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هوای تهران در مرز آلودگی
🔹
شاخص امروز کیفیت هوای پایتخت با رسیدن به عدد ۹۸ در محدودۀ «قابل‌قبول»، اما در مرز وضعیت آلودگی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/460415" target="_blank">📅 07:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460414">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بانک مرکزی از نظارت بر پلتفرم‌های آنلاین طلا کنار کشید
🔹
پیگیری‌ها از بانک مرکزی نشان می‌دهد بانک مرکزی قصد دارد «سامانۀ ناظر» را که بر موجودی طلای پلتفرم‌های فروش آنلاین طلا نظارت می‌کند، کاملا در اختیار ستاد مرکزی مبارزه با قاچاق کالا و ارز قرار دهد.
🔹
این یعنی بانک مرکزی مستقیم بر فعالیت پلتفرم‌های فروش آنلاین طلا نظارت نمی‌کند.
🔹
با اتصال پلتفرم‌ها به سامانۀ ناظر، موجودی طلا و دارایی هر کاربر به صورت آنلاین قابل رصد است، اما مسئولیت آن با بانک مرکزی نخواهد بود.
🔸
درحال‌حاضر یک پلتفرم به‌صورت آزمایشی به سامانۀ ناظر متصل شده، و به‌زودی مابقی پلتفرم‌های فروش آنلاین طلا به این سامانه متصل می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/460414" target="_blank">📅 07:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460413">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تداوم حملات رژیم صهیونیستی به جنوب لبنان
🔹
الجزیره: جنگنده‌های اسرائیلی در دو نوبت شهرک النبطیه الفوقا و حومۀ شهرک کفررمان در جنوب لبنان را هدف حملات هوایی قرار دادند. @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/460413" target="_blank">📅 07:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460411">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926651fb9e.mp4?token=GGCvX5sVdwxbHmo4Mb6uoGzFXD0ZHLvwI5pMBsOzv_ouX1XEsG6E7JLBhbWFcyachJzDq9UKTq25-n6ghMPUl2vNlySXHWi-7NTDBF9jAqt2sR_2Upm_FQng1pd-1oqpuUvUuICiXi7hbFtiHcxgXB4PM9fkSv7zDPhDjpvH297u5Aa8L3J4_mgCEMR2n9Fi_NRr2OpFIrtP7MPPJxFV7-63z9CNHYaeDtfXPd5ipfTA7gdYWYlx85Kg7DzMqoUePBsJ-tgQ0o_tXPnDcypuFWh3e18dsIPpvkkuA4erLWV5oAPZspUKaK4FH0-lJ5LToENTIzX1P2Fm1fE7v7-gdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926651fb9e.mp4?token=GGCvX5sVdwxbHmo4Mb6uoGzFXD0ZHLvwI5pMBsOzv_ouX1XEsG6E7JLBhbWFcyachJzDq9UKTq25-n6ghMPUl2vNlySXHWi-7NTDBF9jAqt2sR_2Upm_FQng1pd-1oqpuUvUuICiXi7hbFtiHcxgXB4PM9fkSv7zDPhDjpvH297u5Aa8L3J4_mgCEMR2n9Fi_NRr2OpFIrtP7MPPJxFV7-63z9CNHYaeDtfXPd5ipfTA7gdYWYlx85Kg7DzMqoUePBsJ-tgQ0o_tXPnDcypuFWh3e18dsIPpvkkuA4erLWV5oAPZspUKaK4FH0-lJ5LToENTIzX1P2Fm1fE7v7-gdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فوران آتشفشان در اندونزی
🔹
بامداد یکشنبه آتشفشان «آناک کراکاتوا» در اندونزی فوران کرد. در پی انتشار گستردۀ خاکستر آتشفشانی، فعالیت پروازی در فرودگاه بین‌المللی جاکارتا به‌طور موقت متوقف و تمامی پروازها لغو شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/460411" target="_blank">📅 07:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460410">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تداوم حملات رژیم صهیونیستی به جنوب لبنان
🔹
الجزیره: جنگنده‌های اسرائیلی در دو نوبت شهرک النبطیه الفوقا و حومۀ شهرک کفررمان در جنوب لبنان را هدف حملات هوایی قرار دادند.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/460410" target="_blank">📅 06:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460409">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbqznMDq20sH7VhmMyhmVK091JXv_kK1ySI-Tf2QgDO-UOy7JUtgFMfQVv60VMwotGhr_lQtNeoxSE48SomgqH_oLqeGGv2vPlPAmTPPJoA5t7OZUHNr_RQLv52eIqLYm1WmlXZoBG4hEVL--Dy_JXx9fcmlCMOjnu8W1Q0LfRbx5uPV24o2bI1WizmAFIWtVZXU4aHEBc1JapzsV3wmY-M5yHRsc3pxfjTBSze0MmE0ScK6aFzJEr_tUrZgOmxcHKBebx9iU7OUmsm7OhPjYlopGeJYOSdZvQHdpr3mttRnSGpVfTh0c6WKcXFXc98hwWAuRNAcTm_yjIcRrnAZzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کالابرگ ۳ گروه شارژ شد
🔸
سرپرستان خانوار با رقم پایانی کد ملی ۰، ۱ و ۲
🔸
خانوارهای تحت پوشش نهادهای حمایتی
🔸
خانواده‌های نیروهای مسلح
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/460409" target="_blank">📅 06:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460408">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDEQuotNHtQq40bOG6W8qZnS5rG-Sy3FErVlZXbnRSSEgbMBaYnpvHu3vUDdJ6tRHHwxPYyOAPoDNI1usOEJ9LCNQF86S8-8sRI_aJTr7xDCmou_fvc2WJsZuednInbSouHFyZq1tIkoO7pPLe8oPNp0wmq_TLdiao6YogLWJ1WEimkW3fgLn10BPpEAw8IAoWhEbFjEa20LkC65A-n31PUMqO0EAlP38f4iRJy6IcluUs4176wB_jlbQaYGQtuSS_kmynQM4TZQPCJpmmrGX11mPgatXoDxL1aEVKbat1oFKbyFj_Cw1dHDF0i7_QeZnUBM52_YrebB9s58YJ2UZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ اشتباهی جنگندۀ سعودی به مواضع خودی در یمن
🔹
وبگاه خبری «الخبر الیمنی» گزارش داد که یک جنگنده سعودی روز گذشته مواضع نیروهای «العمالقه» را در استان تعز بمباران کرده است.
🔹
طبق این گزارش، دهها تن از مزدوران وابسته به ریاض در این حمله کشته و زخمی شده‌اند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/460408" target="_blank">📅 06:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460407">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
سپاه: ناو هواپیمابر و یک ناوشکن ارتش کودک‌کش متجاوز آمریکا مورد حمله قرار گرفت
🔹
روابط‌عمومی سپاه: نیروی هوافضای سپاه پاسداران انقلاب اسلامی با چند فروند موشک بالستیک، ناو هواپیمابر و یک ناوشکن ارتش کودک‌کش متجاوز آمریکا که برای کشتی‌های ایرانی مزاحمت ایجاد…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/460407" target="_blank">📅 05:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460405">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_oU0qstf6QhF3h8JEp1EtMFl8fkfRCNzoOP0nU0r2uNT2t3V68ygQC9vtMJBCAOL_0uIKnA-fF8Qm1Z5_zgqTdz3fkwnAfHzZdQEOprDMlRjaYC6qJP7SeWJWuCVkc6LAFqYPEbhsn9RwmhyyuiJkaJVIiZgzfhX3wTs4SWlMUGibrQKXsZmX23KfLt3aXDLLqCgrfKncL2M0qixAwgoohuqe9Xnpkbg4T5ElITO8ABf7chb4mh0U2CIiBgK0gS4C9yqQU83mICe8lbyL7U8bWjj5jfvKAISODF-_rRnKQciu874WivIeP_FEjQSFi--11AvfQn7XGdvsheDQdUsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a5654e5d.mp4?token=Jyoff_o__2LPAPpaGunLTK7BZyJQPplNHDx1bPW0eyR9bSS33JXZgDn6Wsi48d8UdnC7PUqbYY9TQ_OtHMFKcyzLu1blqSGz2Ml7BB6ugL6g1bqO8D-BqV-v39wfWgBwcs0KoL5cnXwU_BXVCJnBMOHnASnFj-fzmzUYW3-PWuoXoQL8A200qedkwVd8NNgsg_oi7NfpPiQJtm8__vk5NPBBcVLuMEKj5SgPhwCh9epuZ5BajS2cycCUkkrtuWK1nE56l-tJvDx_A9nEP57H4hG7UMeLjGXdQydc72UNN0f0jnIWabjgPnWBAPKRXc5pTgqv4eUJ8mvr_vsWxfNLKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a5654e5d.mp4?token=Jyoff_o__2LPAPpaGunLTK7BZyJQPplNHDx1bPW0eyR9bSS33JXZgDn6Wsi48d8UdnC7PUqbYY9TQ_OtHMFKcyzLu1blqSGz2Ml7BB6ugL6g1bqO8D-BqV-v39wfWgBwcs0KoL5cnXwU_BXVCJnBMOHnASnFj-fzmzUYW3-PWuoXoQL8A200qedkwVd8NNgsg_oi7NfpPiQJtm8__vk5NPBBcVLuMEKj5SgPhwCh9epuZ5BajS2cycCUkkrtuWK1nE56l-tJvDx_A9nEP57H4hG7UMeLjGXdQydc72UNN0f0jnIWabjgPnWBAPKRXc5pTgqv4eUJ8mvr_vsWxfNLKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملۀ موشکی و پهپادی یمن به مواضع دشمن سعودی
🔹
منابع یمنی از شلیک حداقل ۵ موشک به سمت مواضع عناصر وابسته به ریاض در شهر تعز و بندر المخا خبر دادند.
🔹
گفته می‌شود در این حملات همزمان از چندین فروند پهپاد نیز استفاده شده است.
🔸
بندر المخا از اصلی‌ترین معابر ورود…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/460405" target="_blank">📅 04:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460404">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حملۀ موشکی و پهپادی یمن به مواضع دشمن سعودی
🔹
منابع یمنی از شلیک حداقل ۵ موشک به سمت مواضع عناصر وابسته به ریاض در شهر تعز و بندر المخا خبر دادند.
🔹
گفته می‌شود در این حملات همزمان از چندین فروند پهپاد نیز استفاده شده است.
🔸
بندر المخا از اصلی‌ترین معابر ورود سلاح و تجهیزات برای مزدوران سعودی از سوی دولت ریاض به شمار می‌رود که در هفته‌های اخیر بارها هدف حملات موشکی و پهپادی ارتش و انصارالله یمن قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/460404" target="_blank">📅 04:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460403">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rU39t3xbwJXi6Ihjpj_6lBhWaTepYlInj4NBIE-BMQ2ju4jRNeSfiuYBcEmZUChf-E1ek7ZxP09KOaEZVqXxcnLBX8ycgVTX0HmhXYvqq4eQebmzh-Cc77Z0Fm3MtdCQOb9LaGhO8KPVoNydsFYlYsl3XON_sqHJ18yUQy0H41Mc0Bn5ygkHXTaPSfy720Uj3oqWW37eVRxmWoSpuDAKKNvByxXAcfWl_BvCNEg1taAvamkjV2qqWmFFwmzw4EPbewLvXwy_NR0JkK41aP0UoI1KN5WuvnK-2Da-5RXa8hUkYZ66xk2MrdDDpnkn3K8swbUvHf1D4u2IbiMvmLLfqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ۵۰ میلیون تومان کمک بلاعوض به کسبۀ پاساژ جنت پرداخت می‌شود
🔹
داود گودرزی، معاون شهردار تهران: علاوه بر وام‌ یک‌میلیاردی، مبلغ ۵۰ میلیون تومان کمک بلاعوض تا صبح یک‌شنبه به تمامی کسبۀ بازار جنت واریز خواهد شد.
🔹
بازار جنت، بهمن‌ماه پارسال بر اثر اتصال برق…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/460403" target="_blank">📅 03:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460402">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S490FfoiBgci4WDXKsGv1ufoV0SRPVJfSe9hwMxweTyby-okU-smgg539Ec_C0IKvEFoT9iDJ_FdwC81lCcR-OWX3G1fET0TLpe0U_-KZLLBBunoUL4FvV3d1s9g9PUWBmTZT5mUyC8vNmyQQnMawJ4PvLT9CwBZ46DB1C8QsaU7OpXgMYs8lN_WiQ2TV2edt97tOKHGMPuKSA3sd6_a-ZjfT-gjsiYmrBBxfpDxSj9usrkndLmuC0Gc_7KOYau4sc6YazFIAlPioce4GOXLn9o7u2VpA5xTajWgMVL1tuN-wkLvX3RaJXzQyzwWXDMiNmzb-l07-ibfRXMxvr4GSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چت‌جی‌پی‌تی زیرفشار دروغ می‌گوید!
🔹
پژوهشگران هشدار داده‌اند چت‌بات‌های هوش مصنوعی ممکن است در برابر اصرار کاربر از پاسخ درست خود عقب‌نشینی کنند و اطلاعات نادرست او را تأیید کنند.
🔹
این رفتار زمانی رخ می‌دهد که مدل به جای پایبندی به شواهد، پاسخ خود را با نظر و ادعای کاربر هماهنگ می‌کند؛ حتی اگر ادعای مطرح‌شده نادرست باشد.
🔹
پژوهش‌ها نشان می‌دهد تکرار یک ادعا و فشار برای تغییر پاسخ می‌تواند بر تصمیم مدل اثر بگذارد؛ مسئله‌ای که با افزایش استفاده از چت‌بات‌ها برای دریافت اطلاعات، اهمیت بیشتری پیدا کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/460402" target="_blank">📅 02:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460401">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
سپاه: ناو هواپیمابر و یک ناوشکن ارتش کودک‌کش متجاوز آمریکا مورد حمله قرار گرفت
🔹
روابط‌عمومی سپاه: نیروی هوافضای سپاه پاسداران انقلاب اسلامی با چند فروند موشک بالستیک، ناو هواپیمابر و یک ناوشکن ارتش کودک‌کش متجاوز آمریکا که برای کشتی‌های ایرانی مزاحمت ایجاد کرده و در محاصرۀ دریایی شرکت داشتند را مورد حمله قرار داد.
🔹
این دو شناور جنگی پس از وارد شدن خسارت و ترس از حملۀ مجدد، مجبور به فرار از منطقۀ درگیری شدند.
🔹
دشمن متجاوز که سال‌ها با غرور کاذب وادعاهای پوشالی در منطقه جولان می‌داد، امروز ناچار به اعتراف رسمی شد که دو ناو جنگی نیروی دریایی آمریکا مورد حمله قرار گرفت. اعتراف سنتکام مبنی بر تائید این عملیات سند زنده‌ای از شکست راهبردی دشمن و اثبات قدرت تهاجمی سپاه پاسداران انقلاب اسلامی است.
🔹
در صورت ادامۀ اقدامات خصمانه و متجاوزانه، رژیم آمریکا باید منتظر پاسخ‌های سهمگین نیروهای مسلح جمهوری اسلامی ایران باشد. ما قوی‌تر از همیشه ایستاده‌ایم. پیروزی از آن ملت مقاوم ایران اسلامی است، و شکست وپشیمانی، سرنوشت قطعی متجاوزان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farsna/460401" target="_blank">📅 01:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460400">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مذاکرات ۳ ساعتۀ پوتین و فرستادگان ترامپ پایان یافت
🔹
کاخ کرملین خبر داد که مذاکرات میان ولادیمیر پوتین با استیو ویتکاف و جرد کوشنر پس از ۳ ساعت به پایان رسیده است.  @Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/460400" target="_blank">📅 01:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460399">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMM_pR-0SjKqfNQ7f4fDrqFzvNKrViGFI3gcHDj46ZfEmvCRW6Gto1FkoKC8uo_OxIp_cXu9eSzwji7qdKOgeajxxgmvfEsErQsfDK9pszPN4li5_Lq9-CLaYVgE_zkJMi1AuSOWbwJPjDWoZRUs4q2oWBCM_BAhnq2JFkMeNWhjy7OVPIPYFYdD8sc3arrsGBmTEd0NQpB7MtU5qAUhfuFSF2E_euguBARhlCxahyRQFcHx2KvooYYbYy--HzjK9T1dXLr1zivZdXsBrA9K8nMLSw0qJRhiWiOjbS_yY2leFvODvnl8PlNMxomGw5JHgISuEK2QLsmLfVcKgBGexw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بار خداداد را سنگین جریمه کنید
🔹
پیش از شروع مسابقه تراکتور و گل‌گهر مشخص بود حضور امید عالیشاه در تبریز، با توجه به سابقه تنش‌های ایجادشده میان او و هواداران تراکتور و اتفاقات جنجالی دیدار پرسپولیس و تراکتور در سال ۱۴۰۱، می‌تواند فضای ورزشگاه را ملتهب کند. پیش‌بینی‌ای که خیلی زود به واقعیت تبدیل شد و عالیشاه پیش از آغاز مسابقه با شعارهای توهین‌آمیز برخی طرفداران میزبان مواجه شد.
🔹
باشگاه تراکتور پیش از شروع بازی از هوادارانش درخواست کرده بود با توجه به حساسیت ویژه کمیته انضباطی نسبت به ایجاد تنش، از هرگونه رفتار توهین‌آمیز پرهیز کنند‌. اما اتفاقات داخل زمین و پس از مسابقه، ماجرا را وارد مرحله‌ای کاملاً متفاوت کرد.
🔹
پس از اعتراض عالیشاه به داور در پایان نیمه اول و در پی صحنه گل تراکتور، درگیری لفظی میان او و خداداد عزیزی شروع شده و پس از اخراج عزیزی نیز این تنش در رختکن ادامه پیدا کرد.
🔹
خداداد که مدعی بود عالیشاه در مسیر رختکن به وی فحاشی ناموسی کرده، با حضور مقابل رختکن تیم میهمان با این توجیه که امید یک بازی ملی هم ندارد، الفاظ بسیار زشت و توهین‌آمیزی علیه امید عالیشاه، خانواده و حتی شکل پاهای او به کار برده که هرکسی از بیان آن در یک محیط ورزشی باید عذر داشته باشد.
🔹
باشگاه گل‌گهر هم عنوان کرده صدای حرف‌های خداداد را ضبط کرده و به ارکان قضایی فدراسیون می‌برد. حتی اگر ادعای مدیر تراکتور صحت داشته باشد، از یک چهره پیشکسوت چنین رفتاری پذیرفتنی است؟ اگر قرار است با بی‌اخلاقی در فوتبال برخورد شود، چرا نباید یک بار علیه خداداد عزیزی حکم قاطعی صادر شود؟
🔹
خداداد چهره‌ای بزرگ در تاریخ فوتبال ایران است؛ فردی که نامش با یکی از ماندگارترین لحظات تاریخ فوتبال ایران گره خورده است. اما تا چه زمانی باید اعتبار فوتبالی گذشته، مجوزی برای عبور از خطوط قرمز اخلاقی باشد؟
🔹
فوتبال ایران سال‌هاست با پدیده‌ای به نام عادی‌شدن توهین دست‌وپنجه نرم می‌کند. از سکوها تا کنار زمین و حالا حتی رختکن. اگر هر بار قرار باشد بعد از چنین اتفاقاتی، چند روز جنجال رسانه‌ای شکل بگیرد و بعد همه‌چیز با یک جریمه سبک فراموش شود، طبیعی است که هر روز شاهد اتفاق بدتری باشیم.
🔹
کمیته انضباطی فدراسیون در پرونده حرکت منشوری عارف حاجی‌عیدی، هافبک سپاهان، پس از بازی با استقلال، یک جلسه محرومیت تعلیقی و جریمه ۵۰۰ میلیون تومانی در نظر گرفت که در قیاس با این تخلف منشوری به یک شوخی شباهت داشت اما اکنون ارکان قضایی باید درباره حواشی بسیار سنگین‌تر دیدار تراکتور و گل‌گهر تصمیمی قاطعانه و بازدارنده بگیرد.
🔹
این پرونده نباید با چند تذکر و جریمه معمولی جمع شود. اگر عالیشاه فحاشی را شروع کرده باید با او برخورد جدی شود اما این بار نباید از محرومیت سنگین و بازدارنده برای عزیزی شانه خالی کر‌د.
🔹
برخورد همزمان با هر دو طرف در صورت اثبات فحاشی عالیشاه به عزیزی، بهترین پیام ممکن را خواهد داشت: در فوتبال ایران، هیچ‌کس حق ندارد توهین کند و هیچ‌کس هم حق ندارد به بهانه توهین شدن، از خطوط قرمز عبور کند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/460399" target="_blank">📅 00:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460394">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bPooPVEWk5l6Y4wiNCNIlPeUemMiLC-ppL6z2SrpmX_k5uXwLapbrrekyD2S0Xw1zwxP2zjvT8U-_QYy16lYH04bCVc28qZkIoRJiwOUm5PrqLQ6Gwa0UNNPA5t1IeIJep-GALUd64ssaKyXKMpKt3pizyAauadF4JVayGsIPpocZP7SEUOv_YuCZJo63j2YYIdEB8Yt0FYAz30q232eptSBAsM920BQjORtGcbW5b0FB7BgMyFhJxJAvi7u6GZ05_gwdhBI_bwxP3fgoBvzUp8XoNYpvEbIMkXXh-pthaSZVnSHasT0rtCLadZ03JTclRmabb55sg0OXSCWVHNDag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MyVxJtmCp7RM1aYGw7Dt6MqhfN0BTV_Ow0R8yzUnOJr3lzjVl3v9aA638ryExWMiaK4N99aJLHcVsmXxRGIZeejLsXSMeZtOS0bHgHHW5Ptz6SOh8w-xvULDGDX_xS5RGekRmmAy6p0F15WVhvFwP4dV2CT3JsHFc1dglCgFoi2rJZUs26iLQKkI2wP1EJmlgJOeCdZcURFwsIHRFn2QrtPfg1v6T8TpZrVw4fDtzCaS5PKrptTjB-kKbHu5r4wdiQDcXoXYT3JQjpe9oEfJOqr5s9dhRDR827tQR8fVqUfpoZEGuTS2JmNaTuH6mHPpfWEtTPvI_ayq8rq_7LOmCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cL4JBcVwtkOUJvb4j1joNROJ8w_eY8xkgfOUg-LUmSG6go3cniXpEXF1fHZhKO02pJNMv-N49p7pgVg61yRxABIhBbaV9tdk5yYg9dvuesNPZu4xbupjHrNndklcdF65qCx1YdNADphuaKJWaHc13800LQ-Dhqo6TGu1xvGM4i9r8FqHombTwAePSBtetKKhSirPX_doCf9VOkli7gUQrwScPbcszz3YSx6gKW3dF6pRpNgcch35ckrgFOk7uf7A5szQI66NVnbhZeT_qslR4QnfuU2gxzyoAMghVGvJtH6dz3NTkWz609EsTeYd1WYjBFd-cz7NdH4ikVIiRtrZxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YaI0ULCtM_E7O8LUMEjEM3uefvo0HfA0huolrKVMJrTmdro81M24WzqBRVxOYWbj34xE3a0tAcex2YjNr8tt_269woLRsY40UJBvXMCoG1DneYyPRC8RbIn1iVNanN39q5cl3qgtk0fM6hyNiraBWgQBJVUSPXcOP-1EuGbT4s8JCljNMZvHscd_Zyo2whfepEFLWqq4m6VgV2PXECG-lYz8bG5Ovb0RPRd_nXcLYv6--ehStNGUniOrSHjqsVzO1eTSNLb0nnrC-Fsq4waZ02_BVSpjXkweULsf3bo-ReD0ng6OLwbHOooRbagcQDURzkS-M35W_O6477Q1Ck2zTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hSaKEK7boJVnBmtUONCFDa3_ZXzle534DgaeH4LCLpFFX_0ItMbnkM0UCsnp9VcfQGPQtJGLuwXHHQVCGNZtlMeKJSzNRipQnUWCmmdjmNn_yg9H3fwTjRr9hMpi76MthTpK-Sm96vqEmdEcNtFFR2scFLtkV5mk9Cefa0EQQF-7CFQm6vMERDV_8mmcVReX9dyqesivukzZanpX64OSvvpQYjzssRdzdkJmJClIFUMapNL9qxIJlYcpQBwLTOdi1cDwH4sjTcVPgjyvZaIqiTlqhb6uwPcvs-v_qEtYZDV0PITqQWxQOqXJkdR80Kx0f_GGFqm-1PVYyAj5HklJcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یک‌شنبه ۱۵ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/460394" target="_blank">📅 00:50 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
