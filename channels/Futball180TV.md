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
<img src="https://cdn5.telesco.pe/file/kVPcs8LmLfkXZhz0w2Rhq5r88gGNGhPVrfCaghVghIPdy4_ff_xCDpmWDmMC0ok7cHb5E6nA9kIE3kjSmwko865LzX-QcVtKzZ37yNp12sF_pU_noeJBh-rKqVf-kNyh3dPA5T5gL2A5vG372j9iQ8T35m2u2hGWybXHDimd-Bh1SHequrgRqmrcwVXhIG1yEy4I7rRpfXUHBq3JB-pW8da0ktfsABrlmn8y1R1LLfzkM2qdOr9OT7CLRg5bs8R409YmMao7Ur0ppIF09PYpcah353HadHwE5B4OttV2PJhw0svhDGn3jgdKammbAajyW1rX8aguS-yi4myA38prnw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 430K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 23:03:40</div>
<hr>

<div class="tg-post" id="msg-105401">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
‼️
🇮🇷
❤️
کنعانی زادگان: از اول بازی استقلالی‌ها موز و سنگ به سمت ما پرتاب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/Futball180TV/105401" target="_blank">📅 22:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105400">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c06eb0d1ff.mp4?token=vtlSLvrZ5U32lGsjD_XlcNWIO9VDz1T8TVa_Y2_DnlExCb0TjhuMamrvEFSrK4kAuMnbuhYwnbvzpo4FBf4gj22UryciTnOu2s48_L85qVfMucOI-RQPG5ai1r2f4adFERDiKKfLf2HF7aFnjM73kcI_MCqiczUSuqPkD21jC9WT6zneR_i2o2gY4BlUmEc3U30HJyDeD7aziQCjSzwc6ahHV9pOlOYSmvRPNHvLO_vqN0ejUqHAafFPBAElFEZgqcaDAbgn2jXIa7C2Jr_1hjmu6Zss0rK--G5V3roO5H7wBAH1pchAak8MnRoEhFjVEHgjchNdVwIVA9ffqaScxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c06eb0d1ff.mp4?token=vtlSLvrZ5U32lGsjD_XlcNWIO9VDz1T8TVa_Y2_DnlExCb0TjhuMamrvEFSrK4kAuMnbuhYwnbvzpo4FBf4gj22UryciTnOu2s48_L85qVfMucOI-RQPG5ai1r2f4adFERDiKKfLf2HF7aFnjM73kcI_MCqiczUSuqPkD21jC9WT6zneR_i2o2gY4BlUmEc3U30HJyDeD7aziQCjSzwc6ahHV9pOlOYSmvRPNHvLO_vqN0ejUqHAafFPBAElFEZgqcaDAbgn2jXIa7C2Jr_1hjmu6Zss0rK--G5V3roO5H7wBAH1pchAak8MnRoEhFjVEHgjchNdVwIVA9ffqaScxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
📹
مارک‌کلاتنبرگ در لایو برنامه عادل فردوسی‌پور: موعود بنیادی‌فر باید حسین کنعانی‌زادگان را اخراج می‌کرد و این تنها اشتباه فاحش داور بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/Futball180TV/105400" target="_blank">📅 22:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105399">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce1c0fb29d.mp4?token=g5yGeNW-rs1dDltTCX853CCmxC56IPtTsDG20qYtfOMZcIe6ZFCvBc9tjKwV6mG4wofY5VQOi8r0ucaDVe9LkdCUYzdOGBL-3NpRQXeDhtn3jvTYMpysy7XKF8bp25kpcZ6cHgS_GgL-P5E7FhFKBfhsg8YG21BgXDYUk9G1KDuX9uCT8xbCKmTe2-pV4f48a4h1ZmxZu4fJodDMG9CSJuvHa4Gledr38kgWrlyRshv1I_qdemmPkzpckUt-wDH88n20_0rwJEbljvxex3wFACFQJjJhFBmdrGe95rjya0Ln7frYmL-DWmroK8YXSn_Es8-pkiyPHauxxVyzEeGP6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce1c0fb29d.mp4?token=g5yGeNW-rs1dDltTCX853CCmxC56IPtTsDG20qYtfOMZcIe6ZFCvBc9tjKwV6mG4wofY5VQOi8r0ucaDVe9LkdCUYzdOGBL-3NpRQXeDhtn3jvTYMpysy7XKF8bp25kpcZ6cHgS_GgL-P5E7FhFKBfhsg8YG21BgXDYUk9G1KDuX9uCT8xbCKmTe2-pV4f48a4h1ZmxZu4fJodDMG9CSJuvHa4Gledr38kgWrlyRshv1I_qdemmPkzpckUt-wDH88n20_0rwJEbljvxex3wFACFQJjJhFBmdrGe95rjya0Ln7frYmL-DWmroK8YXSn_Es8-pkiyPHauxxVyzEeGP6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
💙
سهراب بختیاری زاده: فکر می‌کنم اگر آقا مهدی (تارتار) بازی را دوباره ببیند، نظرش عوض می‌شود.
🔵
اوت دستی یکی از راهکارهای ضربه زدن به حریف است ولی ما جزو تیم‌هایی هستیم که بازیکنی نداریم بتواند اوت دستی به آن صورت در باکس حریف بیندازد.
🔵
من بازیکنانم را تحسین می‌کنم چون دو بازی را در مدت زمانی کوتاهی انجام دادند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/Futball180TV/105399" target="_blank">📅 22:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105398">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cef9c1a80.mp4?token=vFxHz_BoXKKoS-CLhmGFX1nJozeqrKnnh0PtssWmcUSr8-In5nXx_i9RUM_ulizrNrK4K5Am_L_K0jxhjx81iOyP_iMRB87J86Z_BqBD48sHwDKcqjYl1jatPyW8cqiXEdU-VwIT6wHAJyYz9MQsWYXdZ50SEvSGayQRxc4UTkPbSf9j3CFeF6W1JFpimscyVHX02f-0kIIknSezlsP95wdkp30FqMw3Ys8hjC3jqjt6SLBeLu0b7vBfhlKwplFAlOXHSNoAAWjOnXJvUZ2NyJFqBPiAhS4ht_NepK0KGALr7zQi6KBXn2D2OhWRdAP97vcBMiSMzw5oB9_27A0t_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cef9c1a80.mp4?token=vFxHz_BoXKKoS-CLhmGFX1nJozeqrKnnh0PtssWmcUSr8-In5nXx_i9RUM_ulizrNrK4K5Am_L_K0jxhjx81iOyP_iMRB87J86Z_BqBD48sHwDKcqjYl1jatPyW8cqiXEdU-VwIT6wHAJyYz9MQsWYXdZ50SEvSGayQRxc4UTkPbSf9j3CFeF6W1JFpimscyVHX02f-0kIIknSezlsP95wdkp30FqMw3Ys8hjC3jqjt6SLBeLu0b7vBfhlKwplFAlOXHSNoAAWjOnXJvUZ2NyJFqBPiAhS4ht_NepK0KGALr7zQi6KBXn2D2OhWRdAP97vcBMiSMzw5oB9_27A0t_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💙
سهراب بختیاری زاده: کسانی که بازی را دیدند، از این بازی لذت بردند و از دربی‌هایی بود که حاشیه به آن شکل نداشت.
🔵
در نیمه دوم ما تغییراتی دادیم، به دلیل اینکه در نیمه اول نظم بازی را در میانه زمین به حریف داده بودیم و این موضوع را رفع کردیم.
🔵
روی یک غافلگیری گل خوردیم ولی برگشتیم و این نکته مهمی است. می‌شد گل‌های دیگری هم بزنیم.
🔵
هیچوقت درباره داوری قضاوت نکرده‌ام ولی دو هفته است که اتفاقاتی رخ می‌دهد. در بازی با فولاد دو کارت زرد اشتباه به ما دادند و امروز هم فکر می‌کنم صحنه اسلامی، پنالتی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/Futball180TV/105398" target="_blank">📅 22:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105397">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRCTjaTm5yzyRytfC8e60VFkzNNy5mPObtDKTpA3vzLcocvwhYHjmdTDrXEzU7Bz4cTNbQgrKWQaUbPUijmbho1zTCRDhXa-61FVvb3Eb0bNcvuZnDL8yR4oAAxVyORONjKNtcaoXx6NFiUjbS-IubEncoh9R2BL0klyFRk45taB6TwzTZBSgFjObYF5IY0Ffr1ST1u1QyqDiHiKw8AIcCnC6pe71UySLJyFeja_jtv9DLc-MIaoJbdKTsFQUEfLE1J1DPBEFEtDiGI2nIH1lPOGH1R9i1gatgI2l2AbraiZsirsWwcNtR_Cl9ttgItbLjT80GsLWdX6k0BJ4sj5Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
سپاهان در بازی مقابل نفت‌آبادان به تساوی بدون‌گل دست‌یافت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/Futball180TV/105397" target="_blank">📅 22:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105396">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiBi4V9Lq9tL_i2NpZOUCpdBCqlzq5TPVJ3uBPICnH0c3hSCp7Bz8sUiQGELN1jkwvhGgt5_bD89a-jGcNf_Ny4MbJHPJsJLK3KAvEbZLzQh-AmYFpNzycEAV-lrlnouFinLv608tnZBUDBB6133m5LTSwgExurFk-U5qEh6RcUsv8AnpusFYF5yl-U1IGxDnk2Rg-qLGOGvNOOjwATxswXUFbpNhj4V0EnkfJ-HkkU2LMscCTcLXkbG9AInsVHnnEvsoSotSonOYuwGH32vdWd3S1RccBB67Ta1hgWTr94nnmCDdy7dkm6aHWnckNDNqSvtrelJv3_YW_7RWQTRDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
سپاهان در بازی مقابل نفت‌آبادان به تساوی بدون‌گل دست‌یافت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/Futball180TV/105396" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105395">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
‼️
⚠️
لحظه حمله کنعانی‌زادگان به عارف آقاسی که منجر به خونریزی گلوی مدافع استقلال شد و داور هم این صحنه را ندید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/105395" target="_blank">📅 22:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105394">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507e713ebd.mp4?token=akeDvVEYOPC8nq-AZCHzYQzbWCuAaT7cw-8vXUl8-4hizyA3QiYTVDqyjWThPXWRvjdgkhTkcEpPyDOJY8z6RQB_GwHMGn3HvZyHcA2B3DKSojQKQIyykMfiE1_1pI6nj2aZo0RbTcDUiuf1TdJZ97ETQQqyFrFyjk_w-dagoPMVNpZtOmHsRle8K3hg_vdlkXXiHmwhCJuYPv9DQhHklCQbEdYaSNFrxuldLYM6puPyldfONf0rXPoUNQpfJs4_Y-seLpMymgqZ3TOJroVFSHf9I0X6Ou4Yj8yEvZO5PWEYOpQZYA3ImQycUjna_X4aUeYrHuF1aYYNusaYkGFc3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507e713ebd.mp4?token=akeDvVEYOPC8nq-AZCHzYQzbWCuAaT7cw-8vXUl8-4hizyA3QiYTVDqyjWThPXWRvjdgkhTkcEpPyDOJY8z6RQB_GwHMGn3HvZyHcA2B3DKSojQKQIyykMfiE1_1pI6nj2aZo0RbTcDUiuf1TdJZ97ETQQqyFrFyjk_w-dagoPMVNpZtOmHsRle8K3hg_vdlkXXiHmwhCJuYPv9DQhHklCQbEdYaSNFrxuldLYM6puPyldfONf0rXPoUNQpfJs4_Y-seLpMymgqZ3TOJroVFSHf9I0X6Ou4Yj8yEvZO5PWEYOpQZYA3ImQycUjna_X4aUeYrHuF1aYYNusaYkGFc3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
❤️
تارتار در نشست خبری: گروه داوری امروز خیلی خوب عمل کرد، خسته نباشید به آنها می گویم/ امروز هم پرسپولیس خوب بازی کرد و هم استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/105394" target="_blank">📅 22:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105393">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
ترامپ: برای آغاز یک حمله ویرانگر دیگر به ایران آماده‌ایم که مدت کوتاهی خواهد بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/105393" target="_blank">📅 22:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105392">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7Ph6NOd2bi16shhNYYWHKT-vLHL45JO39HXY-B5IFce2Oe1bWhDe2loXUYlQIymWE0tQgFKavFBUDZ1oeVqyuCqfKuy2jetoCC4A-9aCcAr4BEPFlNGdJy6h_62t1GnkQWTodAHuytmqcepq2xus_rQta2q1ax2YeQBnE-jw15GO__m0SchF8LvYBo5NfcWuVS631SKZnNMb07ztzATpc8vZN4JRUEuoUFAJFLqNYpfPCFktGWft8Bn_TVe1XLTsdKKz3az7oLz7lbfeA57iNq8hKHJRiYc-Jw8cvE5SEttUP7a0yPSqEfN2rNgtZ2Dt4-L7PLSY0uoc-rDa7knfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
باشگاه استقلال با انتشار این عکس نوشت: تصویری از آسیب به گلوی عارف آقاسی که توسط کنعانی‌زادگان رقم خورد و با بی توجهی داور همراه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/105392" target="_blank">📅 22:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105391">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63becc7280.mp4?token=KXtei4f638h0qkGMXK8VbXSU6gSDVoEI1by3h0ZB1g6HMcPHUfAEa82GIGwya5kwzLJf_X2GQ3zS9Urn5by7L7oC5INeRrCbK9Z3q46qY3-xPsBZoxUYUZwTYzTVTpQJ9Q6z-vkyGND20g75ZtXT_-cQ0fwQhnVzmSrC9g94Gqp2dIwAcAMnz2YYDT9dGePZ00PDi25oX9XCXG8uzi72JAOT8ZUHMvCh6IGzRdnzUqzZO3oaORC2bBM1kdnZsP9ydGKy_7Vus5xhoda_J__HURPR43dzPSdQ__hMhVxp9FFGLgcCsrlH4OGUF3LbTdPNwv1nbmEsxKEs3eURhlIjRnedYHQe4c2AZDe9W-N0kag6JHrVPao2Afri89sYUqifmWENVvgJbFX2uBfVdavbByw3a8zGRYdnkmVpbBRgRNIBRDwJ8GpQkIZpxkxTHaTe0QyfSq0HFBHTAR1JBU3JESzVJDDLx-u36hBypvcY21f8RmqHd2jrwOa2O2b6vQXE48Lq99Akaa7sHnhlS8S4IRTAuoMGqv7vVD8cXRu2QUiMWo1t50Li-xMyNMJIPG8gp8TMYFUoGMAIbKU04MActWRIANB73qHlKh82x_yrbFsJqnS5U4DT9bwfAiKlk2hloPix3RpbGFg53-G-K1PYdO3kGXeb5RQYWp-b5HZdVOY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63becc7280.mp4?token=KXtei4f638h0qkGMXK8VbXSU6gSDVoEI1by3h0ZB1g6HMcPHUfAEa82GIGwya5kwzLJf_X2GQ3zS9Urn5by7L7oC5INeRrCbK9Z3q46qY3-xPsBZoxUYUZwTYzTVTpQJ9Q6z-vkyGND20g75ZtXT_-cQ0fwQhnVzmSrC9g94Gqp2dIwAcAMnz2YYDT9dGePZ00PDi25oX9XCXG8uzi72JAOT8ZUHMvCh6IGzRdnzUqzZO3oaORC2bBM1kdnZsP9ydGKy_7Vus5xhoda_J__HURPR43dzPSdQ__hMhVxp9FFGLgcCsrlH4OGUF3LbTdPNwv1nbmEsxKEs3eURhlIjRnedYHQe4c2AZDe9W-N0kag6JHrVPao2Afri89sYUqifmWENVvgJbFX2uBfVdavbByw3a8zGRYdnkmVpbBRgRNIBRDwJ8GpQkIZpxkxTHaTe0QyfSq0HFBHTAR1JBU3JESzVJDDLx-u36hBypvcY21f8RmqHd2jrwOa2O2b6vQXE48Lq99Akaa7sHnhlS8S4IRTAuoMGqv7vVD8cXRu2QUiMWo1t50Li-xMyNMJIPG8gp8TMYFUoGMAIbKU04MActWRIANB73qHlKh82x_yrbFsJqnS5U4DT9bwfAiKlk2hloPix3RpbGFg53-G-K1PYdO3kGXeb5RQYWp-b5HZdVOY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
📊
آنالیز گل پرسپولیس به استقلال در دربی که عدم یارگیری آبی‌پوشان مشهود است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105391" target="_blank">📅 21:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105390">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
‼️
🎙
تاجرنیا: موقعیت های استقلال بیشتر بود و حق ما برد بود/ یکی از جذاب ترین دربی‌های چند سال اخیر را شاهد بود
سهراب تیم بسیار خوبی را جمع کرده است/ من به این تیم امیدوارم
داوری بازی؟ مهم این بود تماشاگران بازی خوبی دیدند و باید 3 امتیاز را می گرفتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105390" target="_blank">📅 21:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105389">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOmjgsIU_zxz4eZoFUC0PMkxmZZz3v2W-tTuk_mK-JY9Z-k9pzquw3wOzPRc2GG8XXKK22mZ3VXG2BUt_84e6Fk_SUS99OfRx1ytxLaNYn7AVcSGzthG1Eiuv_A20hqV2R8RaF8NUqXWp4SrVymOFebMnMI0RowWFuj2MVF47fUNwMODozUPNHK66YFlqPMfX22fug61HcI8uDh_bqrYyOtwjTGRejZwHAsrnXip31meSD1EE9voEGXqvseiNwJrtznz2TF5StNWtlXNYD5QAKhziivAerejraTx6rlLI5nu-H8WZk6XHTWy8n7jFpT4jmUPIVZN7MsEDtC4xFBjpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇮🇷
🇮🇷
آمار بازی استقلال - پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105389" target="_blank">📅 21:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105388">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
شکایت رسمی پرسپولیس از استقلال؛ پای ۳-۰ وسط است!
باشگاه پرسپولیس با استناد به الزامات سازمان لیگ، از استقلال شکایت کرده است. سرخ‌ها مدعی‌اند آسانی و اشورماتف طی دو فصل اخیر بدون پروانه کار و اقامت قانونی به میدان رفته‌اند و در صورت تأیید تخلف، باید نتایج بازی‌های مربوطه ۳ بر صفر اعلام شود.
حالا باید دید سازمان لیگ با این شکایت جنجالی چه برخوردی خواهد کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105388" target="_blank">📅 21:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105387">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
خلاصه بازی استقلال یک پرسپولیس یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105387" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105385">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlJONgUKZR3Y_nXhVWlM8qKksQ4fVj1PEyo7HG5Fudx2mR09l5kPItVjrzGoFkYKjraB24AfMWkC15pdO6uQ3AxVXf-0YxBPNh66fR30iwO8jnq1wgwnqbR1dssDyYkggh4jc-GFkOxrzVkWrRIR4CWXHsShQUPPaOMQxQNLeO0R6KPDaZ4-c9LcvfMmXl9hBCq3vYhhRLevrDZ8IRiSl8FCfko9u8T61gZvpbKtCfie-FAQ78S9zdVsA9QmRGLqDbxdkaOXqbkz45zmf8eIuiFjRIJ-mZ2CxpuR1O0MTwzz852celt1BVoi9JWs48kczDRVFio1Paeh7Tvrs21L3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📊
جدول لیگ‌برتر پس از پایان بازی‌ دربی! پرسپولیس در دومین بازی بزرگ خودش هم با رقبای مستقیمش موفق به برتری نشد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105385" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105384">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHC4AxN9ufNZUi8EVfp47GxS1Nspq0OM6JunGzGN9lf03IYSSXT1saR4Eom6E005_tD7kZQcv05z46_RtBuyPdk0Pe5c0yeHjAiqoUwaLMyWzSqL69oZ2HhffP7pQGSSn77UHRJHG7hBKx6Cw6XAMzA_vWgsPKhaYZR6b8oeeC-97g3Nv84byi7rDPD3vflYBSODi4ZPFl746VFL5r1K3OEX5PNNuHoxsnzI_iVUXAimVnlWY8_O6zG2YAwwxUK3tAiYooiC-ffhVBbofnAwJxCz6L3Uj6KosbImv-lPE_VEeR9mFIM_bcoVUlx_HAq70kWIwQ30ILK5fUQkQI4m0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌پنجم لیگ‌برتر فوتبال؛ ۹۰ دقیقه هیجانی و تماشایی در اصفهان بدون برنده؛ هواداران از دیدن بازی تارتتا و گواردیولا لذت بردند!
🇮🇷
پرسپولیس
😃
-
😃
استقلال
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105384" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105383">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvBLRCxKmM0uoUN2l8pNSt3F5DbJ2Sf_VanvgHwsAuup5DVCQqKqKLuHN99WdOlxe2R978Jq_zWB_I9TM6avI7f9WwdB0jH5gFIpQ7Ow7AKJBsL2Y3dl2F85_Mh_gyyZqHYP8TQDEaaqBUKEWjgH-851G0gb2N_Qvsr61lybmr1SRey1MKr-gRU8Niz_qGrUHiXwA0O6jVDlcF7Y4Ac2WrJkfXnmBNHuwx2JskrdKdv1NsqIzvd_jNPz85P3YFWyqn-4pQugV1OmtGndkbsQ-LSQWCNwQsmFKo0ts7g8AUGIPJhJVnXH-ocDhxsH4tLU1kY8KfmIxlIkvFkJRSPT8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌پنجم لیگ‌برتر فوتبال؛ ۹۰ دقیقه هیجانی و تماشایی در اصفهان بدون برنده؛ هواداران از دیدن بازی تارتتا و گواردیولا لذت بردند!
🇮🇷
پرسپولیس
😃
-
😃
استقلال
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105383" target="_blank">📅 21:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105382">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b714d173a5.mp4?token=JPgw2wmdtdz5qgnTLj26fStaruKon5vexK8WMi0smQP4bc0Za5Hc_eJLJst01450-cLRPfOG4rR8tAOpw7sBFExfa5JSGdOA5Z1qL_Q46WJzU1QSQEKr3chLILPUh8krU4wQ2gyhJLMYo7ImxCSxn0NrvCDU63SV2Ma003O91R3GOmr0aHc7Hy3_UoZJm0UFcXicM2hj9BezqEbEua5YbKBJf7WSOCFBgLNgnNg3PXYXsDucIIdFTbCpUf0LbX1YkU-4z4LP2DiMho4u1w_0aPdRhJ72WRZlDmZlcDsH95UOr1d1ylXKogM2N9oraJCV65YAd_cySDY6Ps2BwSj1ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b714d173a5.mp4?token=JPgw2wmdtdz5qgnTLj26fStaruKon5vexK8WMi0smQP4bc0Za5Hc_eJLJst01450-cLRPfOG4rR8tAOpw7sBFExfa5JSGdOA5Z1qL_Q46WJzU1QSQEKr3chLILPUh8krU4wQ2gyhJLMYo7ImxCSxn0NrvCDU63SV2Ma003O91R3GOmr0aHc7Hy3_UoZJm0UFcXicM2hj9BezqEbEua5YbKBJf7WSOCFBgLNgnNg3PXYXsDucIIdFTbCpUf0LbX1YkU-4z4LP2DiMho4u1w_0aPdRhJ72WRZlDmZlcDsH95UOr1d1ylXKogM2N9oraJCV65YAd_cySDY6Ps2BwSj1ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
صحنه ای که بازیکنان پرسپولیس اعتقاد به هند داشتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/105382" target="_blank">📅 21:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105381">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d553ea91ff.mp4?token=ZzeUQeCHelaSsL2Lk6XkuTPDSq7lHKP-ZyqYmTzdYmOQbp3Vi9dQTQ_DIETrN0SeB5xt2F8Ygd6-basAtjXUNL1GQbOjTuSKJAesxoIpPZn94oVAiX7jTTF32OksPN6w2ZfnSlaG3pc-oU06LS9dB53D4CaD4Y0kVIWYPdpa2NMjymSdrE5JWtl34cubL1V4gwt3VTN-jpvuaENYXwElzbSHC6a900R9BlDMLJQTwp7TQVv-LXjkhkwvZFqzJ6ryk2g3w8FVi9JS_x9m8PUINbLzbTz0NqF0jSnBl52dOfSvULSIhIkhtBiiOYSRKsUxbFTHzmClItZRNDW41ZFqig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d553ea91ff.mp4?token=ZzeUQeCHelaSsL2Lk6XkuTPDSq7lHKP-ZyqYmTzdYmOQbp3Vi9dQTQ_DIETrN0SeB5xt2F8Ygd6-basAtjXUNL1GQbOjTuSKJAesxoIpPZn94oVAiX7jTTF32OksPN6w2ZfnSlaG3pc-oU06LS9dB53D4CaD4Y0kVIWYPdpa2NMjymSdrE5JWtl34cubL1V4gwt3VTN-jpvuaENYXwElzbSHC6a900R9BlDMLJQTwp7TQVv-LXjkhkwvZFqzJ6ryk2g3w8FVi9JS_x9m8PUINbLzbTz0NqF0jSnBl52dOfSvULSIhIkhtBiiOYSRKsUxbFTHzmClItZRNDW41ZFqig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوت علیپور خطرناک به بیرون رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105381" target="_blank">📅 21:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105380">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsScHz8W8nfcdpErj5GRqav6qjBMWQY7x2EpaBlW_jQ90orasx6OacfDOorHBuxjXxWQ86WN1hh0fJMrfUR875VnGwKNVUwVl9wCMW0XXHO0ftWnVv6nd92WVhaGoa0bsopWl10uLkahFCIhfl40JADZpapyq_St5Gs0GDkjVs6dJTHymdBpoX5Nk29ghhu87eem-1YDpQJd_u-0LN4T_T4VpcL1KN8hKbqyd8YCg_s2XXRECmWNpapOmoF9Fa4Eo7nv8EXdfX8e_GrCzLeM6CdpMSe3QNOB8LqTwc4-GiIbzt0SQ_ZpaNhJWyg0aP86ERPfn6JxocAgb-JkVSZILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
باشگاه استقلال با انتشار این عکس نوشت: تصویری از آسیب به گلوی عارف آقاسی که توسط کنعانی‌زادگان رقم خورد و با بی توجهی داور همراه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105380" target="_blank">📅 20:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105379">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3436b36eb0.mp4?token=JY357C2MIzy9SWYZkbXQ-KccpaHXD9QlqpfRMgtuzaGzhn7xHjqxBZIPATjEZjpN_GAWWRMjS1j0ygvl_m3Qmydz1qMW16mxFZA4U9Tre9LY7zW6ML6ED9oNXbDxdBxMpgYmcgsriLuaU7tIXf6tnZS_fsjOUEskBhX6VEoMGjPp5-HWx7zeurqMDBdA-KnrLL5tRSM-hRLvB9VUB1l1wOmTsOXYrfaURHxRi7exy6LajQuIHDvNsMDeUMTvxW1xw5Ln1eTl4sW3zU8CxPyoYUS9H1FEZQ_3AhH0U0hBDIUVT8tIVj0on7moqF6TFK6I3sX-fjaHnmOOKMPe-x8kZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3436b36eb0.mp4?token=JY357C2MIzy9SWYZkbXQ-KccpaHXD9QlqpfRMgtuzaGzhn7xHjqxBZIPATjEZjpN_GAWWRMjS1j0ygvl_m3Qmydz1qMW16mxFZA4U9Tre9LY7zW6ML6ED9oNXbDxdBxMpgYmcgsriLuaU7tIXf6tnZS_fsjOUEskBhX6VEoMGjPp5-HWx7zeurqMDBdA-KnrLL5tRSM-hRLvB9VUB1l1wOmTsOXYrfaURHxRi7exy6LajQuIHDvNsMDeUMTvxW1xw5Ln1eTl4sW3zU8CxPyoYUS9H1FEZQ_3AhH0U0hBDIUVT8tIVj0on7moqF6TFK6I3sX-fjaHnmOOKMPe-x8kZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
گل اول استقلال به پرسپولیس توسط آسانی(60)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/105379" target="_blank">📅 20:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105378">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">آسانییییییی</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/105378" target="_blank">📅 20:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105377">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یاسرررررررر</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/105377" target="_blank">📅 20:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105376">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">استقلال مساویووووو زددد</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/105376" target="_blank">📅 20:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105375">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گلگلگگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/105375" target="_blank">📅 20:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105374">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=SQdMYtvizasq40LrmpfSBHdvaig2VqZZhbSrc0eAYnXAgGtLOYvi0DzUwkj6xRLOROVTwRQYcAyMkHV5w5zI-8WCjMiES08OJYugnUxLNkTn4xtvEDjUhLJR5dEBMGz8X1nubG2dmwIabGZ9Jm5blqfvuz3YjVekafM4TR6m39qLO52X-ct2-gzYXY1uwrlxmseGxwZrtqa4ceukygb6qMiRTbsF07BvYlGS1mvSDbk7sLE4VTXhajDJWqUhZ-qSGS-iU4JvIgNdqDBLGOTzs9Fr2frBjMCoAoPUxxRolh2I3NzfzAXYzwxidaCTdplLThyE8-A3x_8RFv-Jph7DPY6Fwx-paIcdxVATMhwk_emVbWQOcpRidrZ4XRnbVSM6VPVe_sGcJ5Q_Y8hXhwaVD_SAJI_XkmcIl-zOCbsmeefLJ-_v0j_bd08Zwj3X0U_0h2M71TOtMBnwOWrOORQGfKPrKNXoB6Ap7JItKV1ZFhSzf1ssdIcFwDRCYjfjGJIK6Zz5M1Y1gkkOBRKOc9xYv8omriXFrsxPcz0XE9HDTBhs50t59qiscxLJ1FKwgqhrhmTbDFLpti4Hvyw-p4HeY7lzuQ7Q_yZY6kwHs8sLP5yy051TZjC1bsyv_U9liCSTOiHEx8cys84MkNI3BT_8NGpI7Y9XVsAdQdshN4ob7FI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=SQdMYtvizasq40LrmpfSBHdvaig2VqZZhbSrc0eAYnXAgGtLOYvi0DzUwkj6xRLOROVTwRQYcAyMkHV5w5zI-8WCjMiES08OJYugnUxLNkTn4xtvEDjUhLJR5dEBMGz8X1nubG2dmwIabGZ9Jm5blqfvuz3YjVekafM4TR6m39qLO52X-ct2-gzYXY1uwrlxmseGxwZrtqa4ceukygb6qMiRTbsF07BvYlGS1mvSDbk7sLE4VTXhajDJWqUhZ-qSGS-iU4JvIgNdqDBLGOTzs9Fr2frBjMCoAoPUxxRolh2I3NzfzAXYzwxidaCTdplLThyE8-A3x_8RFv-Jph7DPY6Fwx-paIcdxVATMhwk_emVbWQOcpRidrZ4XRnbVSM6VPVe_sGcJ5Q_Y8hXhwaVD_SAJI_XkmcIl-zOCbsmeefLJ-_v0j_bd08Zwj3X0U_0h2M71TOtMBnwOWrOORQGfKPrKNXoB6Ap7JItKV1ZFhSzf1ssdIcFwDRCYjfjGJIK6Zz5M1Y1gkkOBRKOc9xYv8omriXFrsxPcz0XE9HDTBhs50t59qiscxLJ1FKwgqhrhmTbDFLpti4Hvyw-p4HeY7lzuQ7Q_yZY6kwHs8sLP5yy051TZjC1bsyv_U9liCSTOiHEx8cys84MkNI3BT_8NGpI7Y9XVsAdQdshN4ob7FI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ضربه خطرناک آسانی به تیرک برخورد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105374" target="_blank">📅 20:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105373">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c2230f3b.mp4?token=Yi56ORVl43HZJCT0NRGJFpCy4qwVkF51lTjZMWet3teTkMF7J6x43g5ngqOB2wfcbnPKgeKDA9NX2RmTdUXy1J5Rft2MH6Us8Z0ITyFGT7nr-zT18oNT99ypOaHn4zdd20JQzdL4r5ji2C-GxbYaVu5Uds_D_vA7hr-OJ75zt7Xyyce1BFBpF5yTLjDfDMQl5aZyL1vpzGEWO77ccJQVwIFKsF5NVv5LWJNb3951fQQM8f7pvb0K2ZbhMzfGb3pSFqfi1j78UBOoeJth4pw6bS8uy_Hi_WIiT8U0_s7GxIipIiivfCS3mKeb_shEsZ0l13iP0ZBShFcttFSzUiBlBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c2230f3b.mp4?token=Yi56ORVl43HZJCT0NRGJFpCy4qwVkF51lTjZMWet3teTkMF7J6x43g5ngqOB2wfcbnPKgeKDA9NX2RmTdUXy1J5Rft2MH6Us8Z0ITyFGT7nr-zT18oNT99ypOaHn4zdd20JQzdL4r5ji2C-GxbYaVu5Uds_D_vA7hr-OJ75zt7Xyyce1BFBpF5yTLjDfDMQl5aZyL1vpzGEWO77ccJQVwIFKsF5NVv5LWJNb3951fQQM8f7pvb0K2ZbhMzfGb3pSFqfi1j78UBOoeJth4pw6bS8uy_Hi_WIiT8U0_s7GxIipIiivfCS3mKeb_shEsZ0l13iP0ZBShFcttFSzUiBlBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
گل اول پرسپولیس به استقلال توسط محمدمهدی محبی 50
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/105373" target="_blank">📅 20:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105372">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پرسپولیس زدددذذذذدذدد</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/105372" target="_blank">📅 20:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105371">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گلگلگلگگلگلگگلگلگلگلگ</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/105371" target="_blank">📅 20:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105370">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bef49689e.mp4?token=DrRu9RDvR7zixSh0w6pqumWFkJzsLCppCMWGMEFRjhZPm2l3uG6oxDIrSvjOGNwUoT-7pyWel6b5lWyepyI3gUpF7kj0CKei10A3HkqGmjpgXLwQlTC1F4CCwLyYN0TkW_53ad5utZa89cFEq57SzSJgeshhne22un8RllcjnAGczBRYM-fZQKOQyT7FWTasfTB3uhbg__A_5P3ZX5YM8Ucq8pVT4LODij57lMg2e9igUANLkXa9BByBkRCs7We2LOUtXdvWVuGrSswWEHzZUntjUPB8whEH5FoqAuWVlgdEMDbuYjnwPle4Ue-JaOkd9IulYvoeBNA-jlC02LuFLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bef49689e.mp4?token=DrRu9RDvR7zixSh0w6pqumWFkJzsLCppCMWGMEFRjhZPm2l3uG6oxDIrSvjOGNwUoT-7pyWel6b5lWyepyI3gUpF7kj0CKei10A3HkqGmjpgXLwQlTC1F4CCwLyYN0TkW_53ad5utZa89cFEq57SzSJgeshhne22un8RllcjnAGczBRYM-fZQKOQyT7FWTasfTB3uhbg__A_5P3ZX5YM8Ucq8pVT4LODij57lMg2e9igUANLkXa9BByBkRCs7We2LOUtXdvWVuGrSswWEHzZUntjUPB8whEH5FoqAuWVlgdEMDbuYjnwPle4Ue-JaOkd9IulYvoeBNA-jlC02LuFLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
مهدی تارتار خطاب به بازیکن پرسپولیس؛ پا نشو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/105370" target="_blank">📅 20:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105369">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ae4fcc9a0.mp4?token=BME-G4-SJO-aHI2FGK4UwGUm3hX3-SlpMSTxYS0XLGkRz3tawf_-2iExmic-gucrixwZV3dgK6vfP_5jgaffydNs0-5ptW8-Lnm3rXsOD1osNfx0sp6YBB7eBi42lorSCDywL2brrVA9DXpnuB_GYzzVkUqOH9OSCqZJ2WG-4iUY-BHHXaUlPcUw0KUs_hM8KKL3klPX-ZxXrIq8KJn9trx_GS6hii4gOUD_pNlQLpAKRamsG1nWF3CaD0na5xmwVaGqkXWLXoYxH2JROBdVCt4OcfPdODVeE7K1viywgbTM0-rVtkQ-VFsw7IbKD4UkmIVd7oKNXV11upagGGJjlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ae4fcc9a0.mp4?token=BME-G4-SJO-aHI2FGK4UwGUm3hX3-SlpMSTxYS0XLGkRz3tawf_-2iExmic-gucrixwZV3dgK6vfP_5jgaffydNs0-5ptW8-Lnm3rXsOD1osNfx0sp6YBB7eBi42lorSCDywL2brrVA9DXpnuB_GYzzVkUqOH9OSCqZJ2WG-4iUY-BHHXaUlPcUw0KUs_hM8KKL3klPX-ZxXrIq8KJn9trx_GS6hii4gOUD_pNlQLpAKRamsG1nWF3CaD0na5xmwVaGqkXWLXoYxH2JROBdVCt4OcfPdODVeE7K1viywgbTM0-rVtkQ-VFsw7IbKD4UkmIVd7oKNXV11upagGGJjlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
طرح هواداری دو تیم روی سکوهای نقش‌جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105369" target="_blank">📅 20:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105368">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a8cd40ab6.mp4?token=aVr2PdyfSYaiyOe-VTppd-zvSbtVEJlo-GBPvfvRWzF1-dtItRAPlAumwUvErMpZE1yx-s01ZD723fHbpnBbncmErbMj1tKkPcJ14QUJPHD-kmxnrlTonZNkrasWeF6ELCWhVDhM6-omvByjKruXfZzMVQdBOVzfHYW3bL28Jhm39yGpA2qa3bPDeH2lA-ksjXnB4EdxqX9QLsjwr7xJriXETSkcmdiB4jf8M5fECNZRApSgaWmr3GsMz-84yKDDMA0kgbfxZEmitL28Lqg-X3bB9T8gvZwFXMfLBpUeWqC2NRkoxT7PAa0yZC9-r4eHUzI1GquXIQs6t-sh4Wjn3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a8cd40ab6.mp4?token=aVr2PdyfSYaiyOe-VTppd-zvSbtVEJlo-GBPvfvRWzF1-dtItRAPlAumwUvErMpZE1yx-s01ZD723fHbpnBbncmErbMj1tKkPcJ14QUJPHD-kmxnrlTonZNkrasWeF6ELCWhVDhM6-omvByjKruXfZzMVQdBOVzfHYW3bL28Jhm39yGpA2qa3bPDeH2lA-ksjXnB4EdxqX9QLsjwr7xJriXETSkcmdiB4jf8M5fECNZRApSgaWmr3GsMz-84yKDDMA0kgbfxZEmitL28Lqg-X3bB9T8gvZwFXMfLBpUeWqC2NRkoxT7PAa0yZC9-r4eHUzI1GquXIQs6t-sh4Wjn3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
موقعیت خطرناک یاسر‌آسانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105368" target="_blank">📅 20:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105367">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a811272008.mp4?token=d_0YvEIH6yZYNXrmgUNF5sO0oAv9UvjB_pwYI0ZBbRFDbsIDw17HVMgEAtlLYTNc0JR92QxBKER592lvGv6uZx2j0Pv-jVQEq7-s4Z9J0dnBYwc8uNwsercFONrVFI5ijW0S3MhJxMuE9ItI6pinK0GcZnQ6HMoD4sbv5Co5fg0bdarqXDT2n_4JGoluwn_nsmHZfZ5-D9qaLSA3mXw9LQ7JpcSDnUVUW3hwV4q3folUT1agRg1s4Wj9ObFzXI2dqyJIPnwy6NTLAmTIb5Oqe5qtQRMpkhMFa2eAmtkve_9-Ta-930RsmPDixPaPxI97Er44n0CTPhVUg_8BOoDKnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a811272008.mp4?token=d_0YvEIH6yZYNXrmgUNF5sO0oAv9UvjB_pwYI0ZBbRFDbsIDw17HVMgEAtlLYTNc0JR92QxBKER592lvGv6uZx2j0Pv-jVQEq7-s4Z9J0dnBYwc8uNwsercFONrVFI5ijW0S3MhJxMuE9ItI6pinK0GcZnQ6HMoD4sbv5Co5fg0bdarqXDT2n_4JGoluwn_nsmHZfZ5-D9qaLSA3mXw9LQ7JpcSDnUVUW3hwV4q3folUT1agRg1s4Wj9ObFzXI2dqyJIPnwy6NTLAmTIb5Oqe5qtQRMpkhMFa2eAmtkve_9-Ta-930RsmPDixPaPxI97Er44n0CTPhVUg_8BOoDKnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
فرصت عالی علی علیپور به بیرون رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105367" target="_blank">📅 19:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105366">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a4f888f78.mp4?token=jmwlW1FinfdS3Tfhdhx1jKkmN-tjPhYDkoWRl_3DX6D-xD_7HtyW6xp5ws3RFkqnLbvYXrtmtpeM29i7OcL9WKD4NDhEjVTXKB4NovW1HyQsCa4FnkRpOWKKqADrQ5ZXrMKZcJleAHBj6nwXGSd7XpJ42HdmhUB9X-8mOtcqFk6GVSkb3fkCtdkyZ_ig-gySdk7aHJApchYM2htgIZu_gnMeCMvuGlKBfVcbR2mztOq8Ah0s5_EU-VSaTiE_6HaDCqgx87AK8YU7MvLqADE79fH_DQLLTL4Po0TN-yDO7ktXLSRad21UbWVtz2u2Y5FCfV2DO_BfHk5fJYtKr-fSbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a4f888f78.mp4?token=jmwlW1FinfdS3Tfhdhx1jKkmN-tjPhYDkoWRl_3DX6D-xD_7HtyW6xp5ws3RFkqnLbvYXrtmtpeM29i7OcL9WKD4NDhEjVTXKB4NovW1HyQsCa4FnkRpOWKKqADrQ5ZXrMKZcJleAHBj6nwXGSd7XpJ42HdmhUB9X-8mOtcqFk6GVSkb3fkCtdkyZ_ig-gySdk7aHJApchYM2htgIZu_gnMeCMvuGlKBfVcbR2mztOq8Ah0s5_EU-VSaTiE_6HaDCqgx87AK8YU7MvLqADE79fH_DQLLTL4Po0TN-yDO7ktXLSRad21UbWVtz2u2Y5FCfV2DO_BfHk5fJYtKr-fSbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
بهروز رهبری فرد: خیلی دوست داشتم که جلالی در این بازی باشد چون نقطه قوت استقلال همان سمت است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105366" target="_blank">📅 19:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105365">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYmWye0K-mxnIW4gdetwwifNFQXA-Vv2EPar0R5ZRqppqfpNPYMMdrZjansSrawdwzFn1ZsdY8JmV5vuhWcDoXHNCWMASdDZG2nm3CdOw-wKG2uxp_G_37KsE10XsSUvb9MBGevjCoUHzNnXCi0kJHaiABp6hVTjGezsE19gpb5SjFHZ4H4VC9nV11OmRKFPkVi1yVSxLoNUirDB3-0w4CBUFCwDt5kpPk1EqzZIS2ZWsmxhmipPO_BSOUikdBydJr97SSzqgx_yyhy5s40aeosy9ESYi1MzIvOH8jUmigNqEoe0uXysejr3M2CQK1v31j9Q5IiFr1fBtXEB0TmKKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
ظاهرا جدید صالح‌حردانی در بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105365" target="_blank">📅 19:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105364">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04c8c7c65b.mp4?token=WksoWu2kvJkmxXWTLeorOYl7mthhBdoJrjeQ5Qv2hoGX0J10YJnvVlaw4tRTMjZ6dxVmEXtmxDP1XVE1rjhhPOOSC-Q8YnMA4zs9m12-63ZC3J4ONk42pGMsMFq5sunfsj5inUN9kUiZbTqOpnFfJ6OfsDqSRKpSEz1qHFe1krb1FeVZ13Z0kLcjmaPVW2ootQCNoBCkxd9nHTBCgSWLG_ZOvFm-Nkb3-Jfd3jg0XinlTHsfVNc5_GcBznraRDuKV1Hr56PE2tuApDOYS0-WdWl4tm-RmvT7-1XOScbUW43xRqlSda9dxsalAEUmO19UqfY_mGKhKeSxsGRfNgW8tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04c8c7c65b.mp4?token=WksoWu2kvJkmxXWTLeorOYl7mthhBdoJrjeQ5Qv2hoGX0J10YJnvVlaw4tRTMjZ6dxVmEXtmxDP1XVE1rjhhPOOSC-Q8YnMA4zs9m12-63ZC3J4ONk42pGMsMFq5sunfsj5inUN9kUiZbTqOpnFfJ6OfsDqSRKpSEz1qHFe1krb1FeVZ13Z0kLcjmaPVW2ootQCNoBCkxd9nHTBCgSWLG_ZOvFm-Nkb3-Jfd3jg0XinlTHsfVNc5_GcBznraRDuKV1Hr56PE2tuApDOYS0-WdWl4tm-RmvT7-1XOScbUW43xRqlSda9dxsalAEUmO19UqfY_mGKhKeSxsGRfNgW8tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
😳
😳
به‌قرآن خاک کسخل‌خیزی داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105364" target="_blank">📅 18:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105363">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da52ed6cf.mp4?token=ULOXbaXjAX7wEMOTSuqH8OOFVuTZOOztfbTEFJBEDIBTX_MXAJ42G8TUT4plEmYut5_luhDYxXTvReKyS4_7SJ8Ww1-7OqkAwfkrBwPY58oYCm8BvYrSR2EEvT2WAEl3612ZTXzwp2gQYw1Wl40vxVasHlwOAJ4atmsq13Uu7DNrphC8fY3nYAhgXk0mKbuOS53ZDLlZoQnPRY1RharkjBm94SHjK8_9kWaPA8-WAzvX3NWNixMqeN1OA3eZm9XglrOwfq4dflODeJxR12NmwQ5voTEbQza2yALagZVKt2pQP-rebxvaedG-T8dFJtJQBXJq0FGRGUjUvget27yEpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da52ed6cf.mp4?token=ULOXbaXjAX7wEMOTSuqH8OOFVuTZOOztfbTEFJBEDIBTX_MXAJ42G8TUT4plEmYut5_luhDYxXTvReKyS4_7SJ8Ww1-7OqkAwfkrBwPY58oYCm8BvYrSR2EEvT2WAEl3612ZTXzwp2gQYw1Wl40vxVasHlwOAJ4atmsq13Uu7DNrphC8fY3nYAhgXk0mKbuOS53ZDLlZoQnPRY1RharkjBm94SHjK8_9kWaPA8-WAzvX3NWNixMqeN1OA3eZm9XglrOwfq4dflODeJxR12NmwQ5voTEbQza2yALagZVKt2pQP-rebxvaedG-T8dFJtJQBXJq0FGRGUjUvget27yEpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
🇮🇷
🇮🇷
هوادار استقلال به سبک هوادار معروف غنایی در جام‌جهانی، با طلسم اژدها وارد ورزشگاه شده
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105363" target="_blank">📅 18:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105362">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4866011c8d.mp4?token=bKmd6tpPFIeqObrYMaRUkRJ16yw_LmBrHLPQcH5EKu873v9UJUt0CVxyVSW9Z-xafEMYnGMpcGc3bwyDeNsQgNGyYaoqTCVqmk9q1IqO9FQwzupqyAKK9iyDjpaOHUW3FZs7NpC_5Ak9CuDRv_9exUPWydeqHNy_pGvwUTPzwz_R0jQ3XNAwQq0jHl3zK6hHK6lqTlA5i4ZwnQcBdfiosZMsL3o1llTVtbYISbAGaRgUGfbHtExxj7LaBZuqMeNgQ6USsLfa02nc7JA4rold0aDiivN_SgqCfqVzdL5oUjX2w293Aeg-eGtsntc2vP-RSUhklxq_UGbLjHSPnDq1AnZI6uA1Lz-BPZ2dnGodoYpzdiie7VodpOkWA83744XQrP1_CViIIJsnu3UXBZ_qnOUnioJ1ruWlAu18pQMUdjGC4F0KSLDbWrMH2MavYyAPDENHCrNo9IREY-5tjQDd0GejsSRrefg2c34pkRHqXSf1rmS15ZjsdKOywYDmsJlYVMyMVaWs_d2T2qPErLO7coDmkc2t1waJ7q2eeqkDpDGwL4_yJPyIdiJnCOOFGk3xLkZVQNqI_knWwml5Z9H94h7SK4fJXrL__NgYF38SVmDnLhYLziVcvwthNmbCc3ON_TXoOFhx3kJwXupqIM-HqnhMpOpmfIn3bq34lxPIrbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4866011c8d.mp4?token=bKmd6tpPFIeqObrYMaRUkRJ16yw_LmBrHLPQcH5EKu873v9UJUt0CVxyVSW9Z-xafEMYnGMpcGc3bwyDeNsQgNGyYaoqTCVqmk9q1IqO9FQwzupqyAKK9iyDjpaOHUW3FZs7NpC_5Ak9CuDRv_9exUPWydeqHNy_pGvwUTPzwz_R0jQ3XNAwQq0jHl3zK6hHK6lqTlA5i4ZwnQcBdfiosZMsL3o1llTVtbYISbAGaRgUGfbHtExxj7LaBZuqMeNgQ6USsLfa02nc7JA4rold0aDiivN_SgqCfqVzdL5oUjX2w293Aeg-eGtsntc2vP-RSUhklxq_UGbLjHSPnDq1AnZI6uA1Lz-BPZ2dnGodoYpzdiie7VodpOkWA83744XQrP1_CViIIJsnu3UXBZ_qnOUnioJ1ruWlAu18pQMUdjGC4F0KSLDbWrMH2MavYyAPDENHCrNo9IREY-5tjQDd0GejsSRrefg2c34pkRHqXSf1rmS15ZjsdKOywYDmsJlYVMyMVaWs_d2T2qPErLO7coDmkc2t1waJ7q2eeqkDpDGwL4_yJPyIdiJnCOOFGk3xLkZVQNqI_knWwml5Z9H94h7SK4fJXrL__NgYF38SVmDnLhYLziVcvwthNmbCc3ON_TXoOFhx3kJwXupqIM-HqnhMpOpmfIn3bq34lxPIrbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
شباهت گل‌های این فصل دو تیم به گل‌های به یاد ماندنی داربی‌های گذشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105362" target="_blank">📅 18:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105361">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1BdJeHVit_MMNSkJvIQGrZE-Jrf0mwAGvGKnHkSBqDhwsZqD_hFS6y1bG6smQPgKA0aWc2e3O58BFSKOM-xdzNNzCo9tPnLQSE2gSzOI0vXl_EEZlh5qZSY4vJmC_4LX36J4fD8hF_-lF-MtmSLc5FL8O_DE_roMy4bCCwWpFeEdaCAMkXhze0pKv4m7vT2ugQlOIbrqSbDKrI1tUdMqhLvDI__RfFOqZjvYwTq3pscwexQgg_jxH2iCBE6QXLAYRv_rjLbnf6P7xo3pdAEmCh6tCuD8rCHMv2gm2m7Cs8IKM3Zwo4c6lGgt7L2WAIRtvF-CWcs_QySxVyQbkdxgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇮🇷
🇮🇷
لیست‌کامل بازی امشب دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105361" target="_blank">📅 18:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105360">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e961f8ed7f.mp4?token=hoQ0fs7sXu4MGZwfUyIJnWQQCrN1dHt495z2Ner93mq3vbMD6dkh-ZFbxM8y4oLv3PRN7H4zpKArK2aGKZD0prYAU72rr3Hl-_JK8EFtxnDe3K05Dkkzo6PGfLlw8_RQZe56i5SUpzYOaFWPMefwkkkebSwu9iVx-UqfyzmYPtJUfOVDoiChZOOp3WFrHVdj5vFhmfbsw0iNCWWJ_eQF4V49YHM54PtRt_hkzRBRUPzKw55Tz9iWw9cZzi6MWcLqMvdO3RZ_AWeL3MSmZG1LtqVT5G9fH1Ur95MzRetg7C7VZNr0mrphnXnVgZsZMJpRqlN2Ei79OvdenillDKXkmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e961f8ed7f.mp4?token=hoQ0fs7sXu4MGZwfUyIJnWQQCrN1dHt495z2Ner93mq3vbMD6dkh-ZFbxM8y4oLv3PRN7H4zpKArK2aGKZD0prYAU72rr3Hl-_JK8EFtxnDe3K05Dkkzo6PGfLlw8_RQZe56i5SUpzYOaFWPMefwkkkebSwu9iVx-UqfyzmYPtJUfOVDoiChZOOp3WFrHVdj5vFhmfbsw0iNCWWJ_eQF4V49YHM54PtRt_hkzRBRUPzKw55Tz9iWw9cZzi6MWcLqMvdO3RZ_AWeL3MSmZG1LtqVT5G9fH1Ur95MzRetg7C7VZNr0mrphnXnVgZsZMJpRqlN2Ei79OvdenillDKXkmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
🇮🇷
🇮🇷
یاسر آسانی رو به هواداران پرسپولیس کری‌خوانی را آغاز کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105360" target="_blank">📅 18:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105359">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d420dd3220.mp4?token=vwWNC-SCaYTx5upRzpNgxffsiBh6LLEIlcgnwDkC5sDE5J2pTBMFOlmzxkBP0kRSEUoUbMuYCwlQXiXalH8Yp6-BGgOcT52TjdfwWqBIYz9X2-Kk6Gbfc7F2pg7__wbgOea9brYdSMeU1G6VyuP_PfcVH4uV6sz3if2Cmw50-07kyjDpuCxFy441Fedb2ATB3cEHp1inWKBtscv_YndSTU1LzQaa_8xVbTqRCx3TsBDRjYomTWXWlii58JiVZH8vy7erTuky0ONZEAhL8nI10ENIa6ESlwN7Ox38F6kJzf2V8YpvVv1ukiofuSIkci08EznTiDwcm_R21f3un5DXwjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d420dd3220.mp4?token=vwWNC-SCaYTx5upRzpNgxffsiBh6LLEIlcgnwDkC5sDE5J2pTBMFOlmzxkBP0kRSEUoUbMuYCwlQXiXalH8Yp6-BGgOcT52TjdfwWqBIYz9X2-Kk6Gbfc7F2pg7__wbgOea9brYdSMeU1G6VyuP_PfcVH4uV6sz3if2Cmw50-07kyjDpuCxFy441Fedb2ATB3cEHp1inWKBtscv_YndSTU1LzQaa_8xVbTqRCx3TsBDRjYomTWXWlii58JiVZH8vy7erTuky0ONZEAhL8nI10ENIa6ESlwN7Ox38F6kJzf2V8YpvVv1ukiofuSIkci08EznTiDwcm_R21f3un5DXwjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
سیروس دین محمدی: قبلا اگر مساوی می شد حداقل ما همدیگر را در زمین می زدیم جذاب می شد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105359" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105358">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8LRbzLwVRZJkb7Y6uTwv-5IdQgJ5EY7heRrtsqVEesGHJPu9QKmiLwDBzWsTSB6I0vLVkKzsVtjTAJkDt0PHSFDm3KJkOImqJD143pA6hmGFMd6eIlZQ4VjGjtEQ-w1Uo4nGX7lmgPmFR47-JDupbj3kAE518z7VPRNI62NVkuoE55U5EzNaAEb6MXovXqr2wnellXG_QNzgQldPk-UoMOn7Kgu1bAPhTgSaGmQB_DrKElA-b2KqjzzojJdOw_HgQKOvDxXw17KpPa2uRQUCp03yWiCo5coi8oP60cM-ZYg7eNb757UH41uii_Jh7DTC9IIrtBr5jUG6yRZLQcC1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
مقایسه نتایج سرخابی‌ها در دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105358" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105357">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105357" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/105357" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105356">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-hrujK9eBUyA87Grklk8MlV1FnvnVFaVlziulZCyLUxYMVC_WwovSne8jwxhUH7UYRHwIYVHoGzuLv49U8E_aUFduS_MBLLeFv5fXNTu3nqwiliBZPJjLt9Uqiyeg6UugNfAMk9_gIxsoM8fNOMmxdbB3EyXqvtOopTXKrVdYxk1kVSHv49XaCjERTFtyM7lOyf-7EoEkAO0PpWcyVjU28ORGXC8fr0F8kg6fB50a_pF0tnQL225jLtUwTsyRfKiF8adUyxxJcVirNy1toMsvByMfBEYF3IYYd2Tx2JOSiVPmF3uf_OcpbAzpZuG1DewGAgrFc0vTz-J7ebOvErPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
استقلال
🆚
پرسپولیس
⚽️
پیش‌بینی دربی رو در
TrexBet
از دست نده!
📉
نگاهی به 5 دربی اخیر:
2 برد پرسپولیس | 0 برد استقلال | 3 مساوی
4 گل پرسپولیس | 2 گل استقلال
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105356" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105355">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iC07juO-wf-7AgvZ-9fpaipnfXzHSROuz3WV-7HKxCAHOf0I7ZySUkP-PsjPCCsCXMTzbF3lOYD5vddcbXSJL_lR1_KaY0kXFQhD_rzWVACd00b6E7zUAill1f1_3YZwK_iYuFyhcjVKGWBQF1w4xTUGuDVi5K3l7qRQMS-249FywiNN4FvR6cQMqRs_6qG22gVYfFYu1ySPwVSBQ0KS_OWSeSvN-mdxQfahNeSWbrH1Ivqq_tQzf2w_4acU3Dac90Q4NODeBo4XesxR185RDu387xi3xwc5-74fTLEH0qKBNiNQSFrk3vFFi5Z9T4-gJHFWT6o94RKhvTHMoPcTyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب پرسپولیس مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/105355" target="_blank">📅 18:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105354">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbrUjZqRE6K8PXf7IdU0EYd8LZxaFQv7gfdNSoO3o_2gXu7G68ReIIL-bAW6ZS3Qcfv74I8xABCYOA9mf2O3gPtTcY17Zog12dJmQifSqKYV5_ieXTuEruZZIhZ9InafT9ICHjriT_HrUL2Y1_lwVKwQ4HAX-_9F3AFQB3QmS8PsYBfmynGTJk8p-D7aeSsW2sElqII79d61yKP-yrRTvQyakn162bm3j8-A4U86ZUMb6_WLi4uOFDf8OaKVk7EwcVKrtOiVsTGYvHVtgcnWXSk58z4FXt3Ql0SqgTNjqzHvkk8prFcRi-qU3FOpaXIe2VWKywiWX4_4HbnrK2RWtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب پرسپولیس مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/105354" target="_blank">📅 18:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105353">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nisZeuDhLadDZZlqHG042_ESm3unRMS-iwgQWyjhduWRigZouPoHfz6ZbhIWYboHJafBWp8yXGRlPwaTySQa6RlMtl3-qfz6Zy-YdwynHdgG-OSK6l6P4JQl51GLY0aTRLn64H3zIaHU24d_h7jvmjpRpXRzGkGmTiAnew39kGtkYbMEQysPWMEb_6WFnYof78H8OwFrCZLPIbux57DWqy0XpyX7cgNYOwnLNoAhhmXdaI2EV2W09sOYRanFZ-ywks2CgXT-XhgQKPjstIsxx_Rd_wzt4C1sStMrX4bSgXiiZaCvi0wyYvKP4Jlc4IALwpZE_jVo9YAusv27M0tfXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب استقلال مقابل پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105353" target="_blank">📅 18:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105352">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HScihtSH_gyvMudnnr9bw61FDbx0juIG2YAeSBReDcSMNkM4qx6CBQG4Helh9AJ9RfLH0VNXIGqGG1Xkv4_qkNejACTuDXhGr8Xa7kTcYBO3-uS8I889_WBc13cjXCODfhTGW4XkX_8a0d8Vm238fBgmdPcvCNNLjxAl-oYYy3-SHI3VF94SSdJwvT6vFrrwVwqYlDTW0nvGLcY22vlbBMdT0mHOUPp-T-KN25EaZDHAjM7_qghmwvpJW6xFyIMNYoPVCre_sKGQM02sI9FhNPs2N0XQ_75_k0ih-xfVSh0RmPVPhjlO43IILFWWSH6eteR3-xcJfSc4ubsVrLJXGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب استقلال مقابل پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/105352" target="_blank">📅 18:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105351">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a83d7c6e.mp4?token=PGwKau2WILkPNOQ877YlDUrNVmPMEk4EwMH7m8fyFU1Q5jLSf-CoaMCmDTv_5ujsy4J9ebMPWFjVpOKUxBIG4htuSnH3OxQs672xxkjzGbCymttAsVsj8dTgXp9GfJ0whbrKHS8H1Z25xRkuJbS54UYW4RbKFMb3uUqVmUEID8QH2DxPyVYH2ofr2oZ506HyN25IQGjOioj_98wdPJ1RyMOrspyuZE3R9v6kFnsEgHEsFK13vzWBzRirJ1OK5HPYYUn6fEigKGyhqwKmqli1tt0qfECtLtFV8udgNULPCf3k0KyPm9aYFmZk5xCd_dMQuKuCU1Aw9MR77CHubwV7Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a83d7c6e.mp4?token=PGwKau2WILkPNOQ877YlDUrNVmPMEk4EwMH7m8fyFU1Q5jLSf-CoaMCmDTv_5ujsy4J9ebMPWFjVpOKUxBIG4htuSnH3OxQs672xxkjzGbCymttAsVsj8dTgXp9GfJ0whbrKHS8H1Z25xRkuJbS54UYW4RbKFMb3uUqVmUEID8QH2DxPyVYH2ofr2oZ506HyN25IQGjOioj_98wdPJ1RyMOrspyuZE3R9v6kFnsEgHEsFK13vzWBzRirJ1OK5HPYYUn6fEigKGyhqwKmqli1tt0qfECtLtFV8udgNULPCf3k0KyPm9aYFmZk5xCd_dMQuKuCU1Aw9MR77CHubwV7Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
😳
ترمیم‌ناخن‌های علیپور در آستانه دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105351" target="_blank">📅 18:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105350">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9531a98f1.mp4?token=a_4JKuT4EkXBg_KOEk-bASA5mp1A1bPjJVFwXINpFbwAMU0ypP8aIC49O1VGd3KLvLmXlWC1PQyWEi6Szo-VkkuTDFC3buU7uqXoz4_e8gczR58QAOwljTya78hc2OtNZ2Yss7AfDb8BVJ4n8WPAILEsIngdA4KJPk_jH1R3vMbsyRD6nQiG49KC0ShKBbIzr6k430MYu16q6VmFL4kKDovH4CTLHlTFDFhDlM1h8xRxD5E-KDitcCZDTPeb4_vSrI_yEdvQFEVHpzhXM3-awz5cXM5dpjU2Q6UnMtoVz_EkBYQyIwhfWdjmAe9JYzISGWnf2WqplQpwaLg3zlMIHx00gVlnpVwpFcDdOLA4eaYIQZ2n_y9WjKAxrxBQcmcnEP1-BqVCFqqGEJJvQUusyjVLMmzVQlECqw9-NqvxGuK2XgvkZJKDPTvbDB68oVPNEAFx1hPlT2Smp3lFk1atwx9Jvlekg2gqtbdBwAI4RXMVgLhSSUf8MrpVO4mtx8mlX0DufYteuoWwvPkQo9YblDgWvYJ1dHAJL2wAxhLcfgZGb1mdDyzbvL02NcXqsfmc9_B8xLYWIzX5gy9ynyde4HZnXZr3Bp8RfVAub_-EfRByTqNgOCz387_iWNFJNf9RWfUjg9m_AROXowzEm1G15BiwSikyTz1LZYRpOSZYdRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9531a98f1.mp4?token=a_4JKuT4EkXBg_KOEk-bASA5mp1A1bPjJVFwXINpFbwAMU0ypP8aIC49O1VGd3KLvLmXlWC1PQyWEi6Szo-VkkuTDFC3buU7uqXoz4_e8gczR58QAOwljTya78hc2OtNZ2Yss7AfDb8BVJ4n8WPAILEsIngdA4KJPk_jH1R3vMbsyRD6nQiG49KC0ShKBbIzr6k430MYu16q6VmFL4kKDovH4CTLHlTFDFhDlM1h8xRxD5E-KDitcCZDTPeb4_vSrI_yEdvQFEVHpzhXM3-awz5cXM5dpjU2Q6UnMtoVz_EkBYQyIwhfWdjmAe9JYzISGWnf2WqplQpwaLg3zlMIHx00gVlnpVwpFcDdOLA4eaYIQZ2n_y9WjKAxrxBQcmcnEP1-BqVCFqqGEJJvQUusyjVLMmzVQlECqw9-NqvxGuK2XgvkZJKDPTvbDB68oVPNEAFx1hPlT2Smp3lFk1atwx9Jvlekg2gqtbdBwAI4RXMVgLhSSUf8MrpVO4mtx8mlX0DufYteuoWwvPkQo9YblDgWvYJ1dHAJL2wAxhLcfgZGb1mdDyzbvL02NcXqsfmc9_B8xLYWIzX5gy9ynyde4HZnXZr3Bp8RfVAub_-EfRByTqNgOCz387_iWNFJNf9RWfUjg9m_AROXowzEm1G15BiwSikyTz1LZYRpOSZYdRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
کری‌خوانی بازیکن اسبق پرسپولیس برای امیرحسین صادقی: آخرین باری که استقلال دربی را برد، دلار ۴ هزار تومان بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105350" target="_blank">📅 18:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105349">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a801f0de.mp4?token=tz2Cdqw3Od6Ymj0cwJk1pp3aVVCyW0qNWI77MInITv751DpuFiaP6l6_PIP9bclqPebtrmW3LUUK8Y5Vgslt8exkIytWgPxzpWt-_NeRfscf9Q5Fy614qK2WM4iY5ghwsKVstNvbRy4jgw6kZRXinxaEhA_LmY9g3eiFbhsn7_7yjtcOl6uK-Wd0d1R5IldtKuC8zyO2E4pEGUC3tou_AJsNuQKbKJLINRQGnD09rq6f6Pn3VPQOoAqel_B80K-q0bPYnijhFBegBdn0KXCWAVpRzCVOdVfNd7IuGi96uOe3mmlNe41MRjbV5DogGuP7AWtHXbLD_mZK_kIFEWfzdC_A-ZWfPW3qHSK7i-ygEKMEwpV0T2FiVZzmra18qBCIF6PrSSGMlemGEhQZ4pHgztUUIhwrwm6VrstepnpoHxmrdJnQiVqgoV9uYk0zDrm6Y3tA95PzJGnWYrCK6iyHS18albVv9cNuOJm05fVagZ07pIo8vXDt_czgdFl2SRgOOJBBiQkTSPo1ytTyaW3wsBydhO-XOQARYkCesDRiubHcJ-DkR2IwzB503qi0HP64xgko6BuApTh7l0BlAo9wXY21wpTAhFCPgHaSUuaYK6NH_IThIHVEHc5uhqAkiVufeAVYJr0Z9u4xKnKJmKzZ1VMEwKsqNem2LcgRXlCK3no" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a801f0de.mp4?token=tz2Cdqw3Od6Ymj0cwJk1pp3aVVCyW0qNWI77MInITv751DpuFiaP6l6_PIP9bclqPebtrmW3LUUK8Y5Vgslt8exkIytWgPxzpWt-_NeRfscf9Q5Fy614qK2WM4iY5ghwsKVstNvbRy4jgw6kZRXinxaEhA_LmY9g3eiFbhsn7_7yjtcOl6uK-Wd0d1R5IldtKuC8zyO2E4pEGUC3tou_AJsNuQKbKJLINRQGnD09rq6f6Pn3VPQOoAqel_B80K-q0bPYnijhFBegBdn0KXCWAVpRzCVOdVfNd7IuGi96uOe3mmlNe41MRjbV5DogGuP7AWtHXbLD_mZK_kIFEWfzdC_A-ZWfPW3qHSK7i-ygEKMEwpV0T2FiVZzmra18qBCIF6PrSSGMlemGEhQZ4pHgztUUIhwrwm6VrstepnpoHxmrdJnQiVqgoV9uYk0zDrm6Y3tA95PzJGnWYrCK6iyHS18albVv9cNuOJm05fVagZ07pIo8vXDt_czgdFl2SRgOOJBBiQkTSPo1ytTyaW3wsBydhO-XOQARYkCesDRiubHcJ-DkR2IwzB503qi0HP64xgko6BuApTh7l0BlAo9wXY21wpTAhFCPgHaSUuaYK6NH_IThIHVEHc5uhqAkiVufeAVYJr0Z9u4xKnKJmKzZ1VMEwKsqNem2LcgRXlCK3no" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
هوادار پرسپولیسی خطاب به استقلال: دربی اصلی ما با پیکانه، شما ده سال مارو نبردید
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105349" target="_blank">📅 17:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105348">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c2dc5b376.mp4?token=q4hnUw91OUXVWjvykDXaQwr14Y7kuvqhMgHwZzXUFNTNs8QklEnE8L4_KanzpRDNNglkEvLsjlQGSQpPYM3rK3rf1os539DImV5cFQGwBh6GvgM5yY9mFLozUd5wX9kTYW2u717YmQuckRdznrB0H-zEIsjNfvxTuHGrc0O_xjV9VRPod3QQAxVSm3B5LN8_FpzjAGzxLO1L0uUP__8TKOds_9wtBpky3QwlZNEisPwVDqiwRqBHpitm9T5WHLnEHFA4cRLWaxZ0Ft-REiGuNsOhqqLKxw63YSM35ptSrXjkURDQ0ImhvIprVJX9CXnxZUqtYxdOV5JFzt96vO1NDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c2dc5b376.mp4?token=q4hnUw91OUXVWjvykDXaQwr14Y7kuvqhMgHwZzXUFNTNs8QklEnE8L4_KanzpRDNNglkEvLsjlQGSQpPYM3rK3rf1os539DImV5cFQGwBh6GvgM5yY9mFLozUd5wX9kTYW2u717YmQuckRdznrB0H-zEIsjNfvxTuHGrc0O_xjV9VRPod3QQAxVSm3B5LN8_FpzjAGzxLO1L0uUP__8TKOds_9wtBpky3QwlZNEisPwVDqiwRqBHpitm9T5WHLnEHFA4cRLWaxZ0Ft-REiGuNsOhqqLKxw63YSM35ptSrXjkURDQ0ImhvIprVJX9CXnxZUqtYxdOV5JFzt96vO1NDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
کری‌خوانی هواداران کودک استقلال برای پرسپولیس: ما با پرسپولیس کری و دعوایی نداریم؛ پاس رفت آسیا قهرمان شد اما شما نشدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105348" target="_blank">📅 17:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105347">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4634665f37.mp4?token=Ypt8xhLYE6NDAk_b2j98Oxe0VElxQktWHPG4Zm2ZYEff2b9UI0JPlA02FGJnBF-D5Kj3BAN7eA9TFuATexg5SDEiSR7lz4uGnvohmoqRdlQLdPD8S6JaEqt0vqsqdoSAjUjSDPiUsm6P0-8VCs0eN1oN0j4fDx-sZBHJZA1dnwZ7sh8vHy7A7tqRTxj7iZBtKfCKQkGJDi1qXv1pKzbJ_pTCeiDUb0zlg_pKPBpUKaDwT946tghgWlH2jerOBzvT6mPQa18y-F1bVMDtTPAa7GvM1k3-ysrbZHn2DVl3bb3Bsl6c2fweN538Xor8uGsj5tmWymx_vTgLkK87YlKMmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4634665f37.mp4?token=Ypt8xhLYE6NDAk_b2j98Oxe0VElxQktWHPG4Zm2ZYEff2b9UI0JPlA02FGJnBF-D5Kj3BAN7eA9TFuATexg5SDEiSR7lz4uGnvohmoqRdlQLdPD8S6JaEqt0vqsqdoSAjUjSDPiUsm6P0-8VCs0eN1oN0j4fDx-sZBHJZA1dnwZ7sh8vHy7A7tqRTxj7iZBtKfCKQkGJDi1qXv1pKzbJ_pTCeiDUb0zlg_pKPBpUKaDwT946tghgWlH2jerOBzvT6mPQa18y-F1bVMDtTPAa7GvM1k3-ysrbZHn2DVl3bb3Bsl6c2fweN538Xor8uGsj5tmWymx_vTgLkK87YlKMmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
🔥
نمایی از ورزشگاه نقش‌جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105347" target="_blank">📅 17:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105346">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1699b2c157.mp4?token=hst-60FZEEDXcFE40o3aSv3j8hbf-FBc7ArZah1DZah4NZVZjaKEdZftZo_OiMkXmqZR9gXFaKWJ_y0pIEZDTw8e0S2NwYtrYLsEiwrDF55Nt_NlNjMeTbaYb8NRcYmA_0UeqtJJsheG_rR7FoclQ182VY-CHYI8iGG59Tz1qtwNqM32zlK9vSXEnsqj7RlhKW202KbCOFTojNDBYhL3c7Lo1mNyjKUJo8sjo-aQq6luYYls1fe5V5hQSrV5bUOi7aq_TSxhL9Ek9gxez1GG-w3Jr1bQOmR2Ckl4oGbExS4GZzsKAcnyqVBK9hBcLouHvopMdFFSk7ZD3Si_SnfIcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1699b2c157.mp4?token=hst-60FZEEDXcFE40o3aSv3j8hbf-FBc7ArZah1DZah4NZVZjaKEdZftZo_OiMkXmqZR9gXFaKWJ_y0pIEZDTw8e0S2NwYtrYLsEiwrDF55Nt_NlNjMeTbaYb8NRcYmA_0UeqtJJsheG_rR7FoclQ182VY-CHYI8iGG59Tz1qtwNqM32zlK9vSXEnsqj7RlhKW202KbCOFTojNDBYhL3c7Lo1mNyjKUJo8sjo-aQq6luYYls1fe5V5hQSrV5bUOi7aq_TSxhL9Ek9gxez1GG-w3Jr1bQOmR2Ckl4oGbExS4GZzsKAcnyqVBK9hBcLouHvopMdFFSk7ZD3Si_SnfIcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کری خوانی هواداران زن دو تیم پیش از دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105346" target="_blank">📅 17:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105345">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef377348e.mp4?token=diHZryypxyq9Z7LZ7nRzz2GC1vuBVWVumRvTCV8kUm5Ag_-A_8LpdE3NPwq_R5uKhhA060KlU_CXIA21dNBiTO4iA0q8zXpZVuz3iHyzkvYIZPsgFWjpUqPS5deaQlAnIpDsC--KiFJNbB3lyMKCFKBnQRHeZoukgxWtEMfdvZqSLu8vKSF9CJGoRjyqkLXeET03Um4TDf1zPfkgkzbl25cNL_NPQkM2xEtgfSQF_BSMIEgbWpbrr_GIKVQD5BHM2FldNEaNJjrkxIUrVcYtPOMlQ2kco8md0yUvqh7v1EzgxYIS7DLr_tPKmKreQsc_qTAg5IsQoGIXRJDdHBBfHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef377348e.mp4?token=diHZryypxyq9Z7LZ7nRzz2GC1vuBVWVumRvTCV8kUm5Ag_-A_8LpdE3NPwq_R5uKhhA060KlU_CXIA21dNBiTO4iA0q8zXpZVuz3iHyzkvYIZPsgFWjpUqPS5deaQlAnIpDsC--KiFJNbB3lyMKCFKBnQRHeZoukgxWtEMfdvZqSLu8vKSF9CJGoRjyqkLXeET03Um4TDf1zPfkgkzbl25cNL_NPQkM2xEtgfSQF_BSMIEgbWpbrr_GIKVQD5BHM2FldNEaNJjrkxIUrVcYtPOMlQ2kco8md0yUvqh7v1EzgxYIS7DLr_tPKmKreQsc_qTAg5IsQoGIXRJDdHBBfHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔥
و بالاخره جانشینان رودری معرفی شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105345" target="_blank">📅 16:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105344">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVyqehrZev87IdbD8I_2y_-zKJb09v-mfwKiO-NcZiU6cLCuCgmmZT80vwgefUjJRgiFiUXK0_FVlA0KTgqO_K_sR0mP6UI7RzDtYPq4yvYa1RE_Js2lFcpQoD9P-SODhKchpmOy6DR78Njf7oZlSL5EHd1rxuWujYiX3qnJqTxAiguj8gMvYlEoWJmE0xmVLzsIJn2SMg7LOpMrozlXJTZhzLWA1RyVcu6Zfzj9Mzj1h3GAT2HDNv8RoF7o3xsXQENgjgDMIokzM1ec2OOsCzXskerDn_k2tmzWpLtyvPoBo2tw6hlTAp8p-oFdWBnVkSWwb9KMOrRv-xaR2UWF6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: انزو فرناندز از چلسی به منچسترسیتی با رقم ۱۲۵ میلیون پوند
🤯
🤯
🤯
HERE WE GO
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105344" target="_blank">📅 16:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105343">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1Gg_3zuUVYPhyJLO56bASaZivXixyxJAvD5VN8GhuzgzjrCBexUaJBTppyyD1WVGsknjF3dt17mbkW8F9fixzqehLprdRxcgYn0SCRfMM47oAaLAdKnqh51c7-yvxvXt7q1jsKUK7dNn4FLD0qOYFM8fzKXgDe5e-mW8GRVd47DaLxSnv0HNi-0_klLDzYM3eduGQOsS8W4ONBrRmXZcZ1G8jcJO1crX0XtC3EUIeds1izGj3huF4d2mgQP6MMW_H2hjOOd54ax_4vFRk9wrn27xosIxoB8sFdURTkb1nRajLniidPNrGvLuGH68p-6PxsagF28JCx9jOXYyinCmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
مقایسه سن ترکیب اصلی رئال و بارسا؛ تیم فلیک فقط یه بازیکن متولد دهه نود داره
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105343" target="_blank">📅 16:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105342">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91b6a8d69.mp4?token=E7jW2gnEgMq2eJTjS9JMHhCW5fwp3gd4NeBMju1BW_5VATx2oE9QKtzuUuQUOfYQQ4rWNYO_bIHSBObVA7UF4uSz5BKNeAbiCepzt1_Ova33cQm-79Ua6_LKjeF8oBPpZWxRUz6BwMRPTKBywA2ConPBr2h-28pZzPnKbzXdX-CwmHMe6ZwM-TNqtb99dWwDyygnHoagPOn2rWeNRj2uVzh1boz0tFugr7SdjgefTVYgZpymbqV5mGIX9E7NwucL8bYK-qriyA8G88U-ebo7o7GI2G6OQhHrJGHYkFYHQxLmpESfJeYrZCtS5ubQGm1tbEQ68by6UHOoM-sg9ruJBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91b6a8d69.mp4?token=E7jW2gnEgMq2eJTjS9JMHhCW5fwp3gd4NeBMju1BW_5VATx2oE9QKtzuUuQUOfYQQ4rWNYO_bIHSBObVA7UF4uSz5BKNeAbiCepzt1_Ova33cQm-79Ua6_LKjeF8oBPpZWxRUz6BwMRPTKBywA2ConPBr2h-28pZzPnKbzXdX-CwmHMe6ZwM-TNqtb99dWwDyygnHoagPOn2rWeNRj2uVzh1boz0tFugr7SdjgefTVYgZpymbqV5mGIX9E7NwucL8bYK-qriyA8G88U-ebo7o7GI2G6OQhHrJGHYkFYHQxLmpESfJeYrZCtS5ubQGm1tbEQ68by6UHOoM-sg9ruJBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظ لئو. خداحافظ تا تولد یک اعجوبه دیگر در آرژانتین.
🩵
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105342" target="_blank">📅 15:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105341">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9af28d1f54.mp4?token=o5YiHAqfvXjtNhCfPWyTzijVwJYGckT6facBIf77RpPoGTvAw2oFyfg1W-6iJJ4koZavmpqgqS1cp3bYvj6m_UpFuVxg5xMM7ZKJVAJ2cCOiR1prj-_f9ur4SI6agJUW6mzFgcmpsZSk7jx8iUvgq-CHYCr54qKy5b64iZLD3pX408piNPebNjo3xssB0kJCGMxQc_FSlg1RH3OCv2e_QG2oaZX7l9PkF8qelru2KFH8mz6gmAolgXohG8vOYCHy43SzTbRx7XKmR8Zch8Pijn3FxO67f3ijcUvhewrUHL9Juuom1DXGVlQ3Qe7VJuQ2F29HDSAUfzSQ2SwZ_FcdoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9af28d1f54.mp4?token=o5YiHAqfvXjtNhCfPWyTzijVwJYGckT6facBIf77RpPoGTvAw2oFyfg1W-6iJJ4koZavmpqgqS1cp3bYvj6m_UpFuVxg5xMM7ZKJVAJ2cCOiR1prj-_f9ur4SI6agJUW6mzFgcmpsZSk7jx8iUvgq-CHYCr54qKy5b64iZLD3pX408piNPebNjo3xssB0kJCGMxQc_FSlg1RH3OCv2e_QG2oaZX7l9PkF8qelru2KFH8mz6gmAolgXohG8vOYCHy43SzTbRx7XKmR8Zch8Pijn3FxO67f3ijcUvhewrUHL9Juuom1DXGVlQ3Qe7VJuQ2F29HDSAUfzSQ2SwZ_FcdoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇮🇷
🇮🇷
دربی فقط یک بازی نیست…
⚔️
یه حسه، یه خاطره‌ست، یه جنگ برای افتخاره.
🔥
۹۰ دقیقه‌ای که هیچ‌کس نمی‌تونه نسبت بهش بی‌تفاوت باشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105341" target="_blank">📅 15:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105340">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3a4e2ac35.mp4?token=U9RpxwCgR0pAdyx008LJyhEiqxvowpx06FbqmyZVlnbB5VJZbBvZ-syazBY8oTNSEVf5wHj8-sC2Zb1c9_1uG7oIY3afv-4Y7K2TVHZniACJflfdf2TFkcqJzV7P0iJ8qOjZZXx0GuGnNuBHQjsx9cXjGHkwTJy67rCWXd8diOKaPQIjYvgexnwHBjZCQvXwXs4PIZH20PZy4RCZTCJ36LaNH_ccJ_xFyFcOolqexi5ckIGvD5hNhz5FnKWFd4MOu9UL2xCz0Jx-Zpo8_VPzIs_9e5CBT71cICI044_fkQHVtcqgzjnXddFkDrXOT1SbIaAJnk2wiH5VsbYtDA9OqW2kDTeY0Q3jHnNoXwcmm-36HluCbvidUzs91wdVxvNbmuyxtB2ffpRPuZUg1lQs4_ru4W8A6eRPyU5gzD8d17ZYwczOBfZP4REQqJriO0Tg6IM7L2fU-ihy2fUpGzwUdmsqiF3854gtPGDmqftumwz533LSP-r3nYKNO5FvYJ89IirhU0HLVUqqpQSBk8fQ6x5irL616MFyTIGI4RgETHqdnyYkNr87Dkh-kqYxSmVq1MAoAHpK44qZXrz1VH7xHqlSRehQ-GPuTgCRAbSoe0-uA0eKU1_gh3Zj8Tl9YcATQdFYnH2m97y0rEB5A73dQgA4Gk7K5Am2MqooyD_eKak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3a4e2ac35.mp4?token=U9RpxwCgR0pAdyx008LJyhEiqxvowpx06FbqmyZVlnbB5VJZbBvZ-syazBY8oTNSEVf5wHj8-sC2Zb1c9_1uG7oIY3afv-4Y7K2TVHZniACJflfdf2TFkcqJzV7P0iJ8qOjZZXx0GuGnNuBHQjsx9cXjGHkwTJy67rCWXd8diOKaPQIjYvgexnwHBjZCQvXwXs4PIZH20PZy4RCZTCJ36LaNH_ccJ_xFyFcOolqexi5ckIGvD5hNhz5FnKWFd4MOu9UL2xCz0Jx-Zpo8_VPzIs_9e5CBT71cICI044_fkQHVtcqgzjnXddFkDrXOT1SbIaAJnk2wiH5VsbYtDA9OqW2kDTeY0Q3jHnNoXwcmm-36HluCbvidUzs91wdVxvNbmuyxtB2ffpRPuZUg1lQs4_ru4W8A6eRPyU5gzD8d17ZYwczOBfZP4REQqJriO0Tg6IM7L2fU-ihy2fUpGzwUdmsqiF3854gtPGDmqftumwz533LSP-r3nYKNO5FvYJ89IirhU0HLVUqqpQSBk8fQ6x5irL616MFyTIGI4RgETHqdnyYkNr87Dkh-kqYxSmVq1MAoAHpK44qZXrz1VH7xHqlSRehQ-GPuTgCRAbSoe0-uA0eKU1_gh3Zj8Tl9YcATQdFYnH2m97y0rEB5A73dQgA4Gk7K5Am2MqooyD_eKak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
▶️
🇮🇷
🇮🇷
سریع‌‌ترین گل‌های تاریخ دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105340" target="_blank">📅 14:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105339">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_rCrZjuT_EpmI16Ea24LYj0bsmuwJEardjXHtILbKJI8bJdx1nTwazzP9NhvExhL1FONlxpkQ5xdGGcZ1pT_O-tYnXrJuw5_swwhUW7fi8i2NeL8xDEHhcU2eJdUdmNktXeIaf70X0a4K4MS0ZPcOwzYoL0mUWc7s8b23sFZj_lSQsjwY-e-RS6JYV3TIQlpIxd7sl2SN_qAN9y2ORrXUQ5L-GtL8WJamVSJH7w-FwCm50D_kcWa-OSy-dNQ4_pOaI1wT9ikkT_hfwLmx1eZ36m9KaeszxfXNgnwkZzt7rrJBuGvFbdaymWFfZ_MUz3MgnAUoaQ1j0yVH30FKdWzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
💵
قیمت دلار تو دربی قبلی ۱۲۰ بود و الان در کمتر از یک سال رسید ۲۲۰؛ قدرت گنده‌گوز منطقه
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105339" target="_blank">📅 14:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105338">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d7c8fe82.mp4?token=T0NB2t9KM8lBqFIvuilTH-0iUbgnYQS65ro0q7c0hHH-giptMqcrFZAxanDGlju-47Dj_q8rOrOi7VO8bukxPCJrmullnKpv82DuoKLCdkE557WwHnVozE_A6-G3F43pJer3mGtAUnALTd9cmnn_-4Itaj3hIiDZatsevg3se19tmYQ5684RwHEl3pvanxKuOpRmzbCnDxor_UwM6oCAMncKR1xzQcUU0b0MHyhQI_y2uVi-PkrhViY2LSzIJfq25V7kGtbwCXLaKiCc5OTgdpdfFkj1Im7MNbapA5AfrT8AfG1VJGNOUGrskvYi5bw_hT4w5U2hSpJjcE1-jfvROjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d7c8fe82.mp4?token=T0NB2t9KM8lBqFIvuilTH-0iUbgnYQS65ro0q7c0hHH-giptMqcrFZAxanDGlju-47Dj_q8rOrOi7VO8bukxPCJrmullnKpv82DuoKLCdkE557WwHnVozE_A6-G3F43pJer3mGtAUnALTd9cmnn_-4Itaj3hIiDZatsevg3se19tmYQ5684RwHEl3pvanxKuOpRmzbCnDxor_UwM6oCAMncKR1xzQcUU0b0MHyhQI_y2uVi-PkrhViY2LSzIJfq25V7kGtbwCXLaKiCc5OTgdpdfFkj1Im7MNbapA5AfrT8AfG1VJGNOUGrskvYi5bw_hT4w5U2hSpJjcE1-jfvROjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
زنده از ورزشگاه نقش‌جهان در فاصله ۵ ساعت تا دربی حساس پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105338" target="_blank">📅 14:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105337">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇷
بهترین گلهای استقلال در دربی‌های لیگ برتری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105337" target="_blank">📅 14:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105336">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇷
بهترین گلهای پرسپولیس در دربی‌های لیگ برتری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105336" target="_blank">📅 14:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105335">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfQWGdEnbMmO5oAQezBukKV80n9Ko00SkslClWQiEBRPJmrPRiJ9MNW_GeCdWhZafIhJ_wlBDx3KGJ2fB-XqD9OXN_KICM62QbbxwugBNdkfObMZJ1uSmk00BHSN9Iwa5VQQE9Y-TtunlVQ-bVUgH6TEBOmz0BLwcwMv36gIQYhXWHL6rjZxrBW34AOpBiuXZaK6Iu2IwMHnrmKrlycMVvrxrTN2D3eKs4P6eMy3O7k-QSyLUSIiOWUlwtXtSNG6st4nb4kcFJ62BYqRxHGILM7HIrEkeViMpRYMZXVlVLxEJrl843ypHwO8-wB6KKTNKFQ62p4q9yH0dviJp3Kwbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😳
💵
خارکسده
افسار پاره کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105335" target="_blank">📅 13:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105334">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhO39cyp02I62mDm7Y1H4JXN8tOjBsTFJrNGgFENbBIKpxDRuaqrcyvfNV6pQHIIkSmc_sXdxpP6pGlaO45UdNkDjqiwC4LUN1yW5I3l6NH4njlNnGKEyNvoMTe12Pf5PLV4ygL4x3lntFAG1Miz7O_MiATCHSrVemEEKPrNwLPv0-YM-Blu_P8awMIpv3sS9sDmFgpNH6tYG5QugtN8miH6DK1omEO8nGBf_ZeV37wF8rTMRXCSQ8FLdh-18QKAwjom28WNFsVjrLU3TU64foAj6W7iE8ZtgXWaVHLc3N47UVKpKOj0v958twmWOHO99k3Eqp2rFulhd6YGlsN00w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
مسیر‌ فوتبالی عجیب‌وغریب آلوارو موراتا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105334" target="_blank">📅 13:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105333">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40825ae46d.mp4?token=XhDMmXQitcjhsZenCdnfZi0kpNGYhLDmDiAJs1PhExCMSbzBDCH7UjeIGNd81_mR3GyRws-fF9G0ia69vIlpkQiBe_Qm0KuIR3X9pU7A0VnZ8ny0Zf9g2fbqkTJtiRM0O2_TUYgxuYSkk6eVIqR_jy6ykTYV1H8d5TX4z1RYBwhlrjScWq8aE_h7EkU-7aNeFrPcKKyvLhhneRLPo8AM7PWnNM3rdqZjZfX8HTBw2LNGUUl41OmJG9WLr8DWHpQ_40W9OOmhNdazbuZBvFs-FmT7fqVXXHLTRKtDz1hdJy6D8ca5sOWeyGva21G0rWdXTgBl6mK1czgjpXPlETrIag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40825ae46d.mp4?token=XhDMmXQitcjhsZenCdnfZi0kpNGYhLDmDiAJs1PhExCMSbzBDCH7UjeIGNd81_mR3GyRws-fF9G0ia69vIlpkQiBe_Qm0KuIR3X9pU7A0VnZ8ny0Zf9g2fbqkTJtiRM0O2_TUYgxuYSkk6eVIqR_jy6ykTYV1H8d5TX4z1RYBwhlrjScWq8aE_h7EkU-7aNeFrPcKKyvLhhneRLPo8AM7PWnNM3rdqZjZfX8HTBw2LNGUUl41OmJG9WLr8DWHpQ_40W9OOmhNdazbuZBvFs-FmT7fqVXXHLTRKtDz1hdJy6D8ca5sOWeyGva21G0rWdXTgBl6mK1czgjpXPlETrIag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
امیرحسین‌صادقی: اگر همین‌الان میخواستم در دربی و فوتبال بازی کنیم، دستمزدی که باید میگرفتم بیشتر از ۱۵۰ میلیارد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105333" target="_blank">📅 13:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105332">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc8f3b366.mp4?token=lL8N-UjM1L1YJS0busozqQae52m7fhyJFP6PvLxQUG5CNdpe7wuQC6SE-QmqBjjb68HydLyxttmxt1a4HsPw7fZ1mD3ZFGio_HmWKydz7a9mbR7OngP2LK9r2Zh7asrRVfRRQE6BA3YW-6ppHy7CfYqPW6GiS2o_nzX6gzQPQdOHn0m4qfkHF_E1BaRshl0D0lQ2ivAWn75IBIM9vlWuZ030L7cKSRu8aNGiUEH7SIJEiqQMOS2Mrriz36-LL_V3ccWMMreO-VWOhzCcF9io08muoLd3Hc6axhk-JpPCutotj7syJak4KS45VRQtS6NQ1Zkn9FDesq8asAFpU8lCug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc8f3b366.mp4?token=lL8N-UjM1L1YJS0busozqQae52m7fhyJFP6PvLxQUG5CNdpe7wuQC6SE-QmqBjjb68HydLyxttmxt1a4HsPw7fZ1mD3ZFGio_HmWKydz7a9mbR7OngP2LK9r2Zh7asrRVfRRQE6BA3YW-6ppHy7CfYqPW6GiS2o_nzX6gzQPQdOHn0m4qfkHF_E1BaRshl0D0lQ2ivAWn75IBIM9vlWuZ030L7cKSRu8aNGiUEH7SIJEiqQMOS2Mrriz36-LL_V3ccWMMreO-VWOhzCcF9io08muoLd3Hc6axhk-JpPCutotj7syJak4KS45VRQtS6NQ1Zkn9FDesq8asAFpU8lCug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
حمله مهدی‌فنونی‌زاده در آستانه دربی به بازیکنان سرخابی: عارف آقاسی ١۴٠ میلیارد از استقلال گرفت؛ قیمت بازیکنان فعلی ١٠٠ میلیون است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105332" target="_blank">📅 12:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105331">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105331" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105331" target="_blank">📅 12:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105330">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGbRGuPmqLiA_JdqsOVZTFxWSHdt-l20tN2L6LybN_o7zVBNDq_Sb6oWTi2X8dkLemgKl3hGjVVQw2UmiCoC0cdg1ZvYxCnhcKxdZlqwDToT1m12XnTFcscQ3UNaKWGzbLzOayfzv4wdFwNmX2LIUIlLme5YT7bMRUAccqrfkbiCbOpOsE1_RKJBzguoueUhvhVElemYEAUvSxPj8cGbirAg5VcYsOoTmyRTvmALzRzLo2AK4CAKcvIPK-KYMFPqd3c6ilacmTildP48HgkFTE_LdmJbd5-Dp18lSXZ45U2n3T63EEHBX-vKnxjmOqBSPY8K8wCk5ggguY-LoQr4rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105330" target="_blank">📅 12:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105329">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1137b6f537.mp4?token=hB7pCjIlLA8_8bwIucSQQJxClQz9nBzVHYBD-r47GAFx9q7Jh_8UuEME7b2B2GkZeyB4bal-v9L7r-ANNbVr5LYKlI9FfdPVDUipNIRaPbZlH-2XvuNViUMV5hsP_ZiBxgSzttfX5VEkKRNEWkoFd0mOx8VbyGoTHzYRcCnCiFF5tiPL_rlQi_jgtSAmnRn-4TAlu5zknOH4c6jzEYWr6rvfqszL1I2fkTsILf1oi4VdDIlLMjGRHldtsSOPVOimER_3RcUK4v7d-lKkmGnswhUoWcHbTJLz6oiy-J119XtWYbbEQiVhwpvzmDjdUT9qsfbsoZ3_NleM8exINLJExye8378wC-aGANV4_b_LkE2pmvjt23D4sEW1hWp2QF-7UmcwFsdE1cxhkPswiK4ebKU0zfuG7wJj5j9c8xvURBcAWTlB6tq8aVluUr3Q2Uq3EylYAOVbEP0hRz1JD--W0A880-yKWM0h0gUh_IIn5dtTN6TggbYV62SPWXB9tcIEDV4HZG63cK1dzn4SP6k-F_9Bga5jFe9QpuTaJ-fXivsaXN-wBSjlKxpck_-OBwNVFe5kti8CqhEB-pbg4bxaZbJywqX5sJ4Z7wpzt1hkHIvP-51PuzB31-oKljAKvboJMk-YW4mki19qJxZrnLPniR2npCyNVcMicQRGfKQ6LqY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1137b6f537.mp4?token=hB7pCjIlLA8_8bwIucSQQJxClQz9nBzVHYBD-r47GAFx9q7Jh_8UuEME7b2B2GkZeyB4bal-v9L7r-ANNbVr5LYKlI9FfdPVDUipNIRaPbZlH-2XvuNViUMV5hsP_ZiBxgSzttfX5VEkKRNEWkoFd0mOx8VbyGoTHzYRcCnCiFF5tiPL_rlQi_jgtSAmnRn-4TAlu5zknOH4c6jzEYWr6rvfqszL1I2fkTsILf1oi4VdDIlLMjGRHldtsSOPVOimER_3RcUK4v7d-lKkmGnswhUoWcHbTJLz6oiy-J119XtWYbbEQiVhwpvzmDjdUT9qsfbsoZ3_NleM8exINLJExye8378wC-aGANV4_b_LkE2pmvjt23D4sEW1hWp2QF-7UmcwFsdE1cxhkPswiK4ebKU0zfuG7wJj5j9c8xvURBcAWTlB6tq8aVluUr3Q2Uq3EylYAOVbEP0hRz1JD--W0A880-yKWM0h0gUh_IIn5dtTN6TggbYV62SPWXB9tcIEDV4HZG63cK1dzn4SP6k-F_9Bga5jFe9QpuTaJ-fXivsaXN-wBSjlKxpck_-OBwNVFe5kti8CqhEB-pbg4bxaZbJywqX5sJ4Z7wpzt1hkHIvP-51PuzB31-oKljAKvboJMk-YW4mki19qJxZrnLPniR2npCyNVcMicQRGfKQ6LqY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
چرا محمودفکری مانند کریم باقری در تیم ملی فوتبال ایران موفق نشد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105329" target="_blank">📅 12:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105328">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7p1kAJJgJHmeIT_Q0862ftWFXR11fCApKSeii7i9NvZ8N71RTGNyo40Lx5-P3STQv1kbfwOrrmtp_BFOd7ifLPub_PxBiOQrryTMECzYTjgiFFEglOGZP6kG_KqSh2uYx5JeuLSeJ4kmrddonhLheykoHMej9CymF3RgIuY21egJfSe7kjhlwnxcoD_u4sW3YmGk8cye7NGh8pF6GwOlxaILoksSBq2RkcTPk02VjJ4qnG7_6tI_TwuZOZ6eLrPC22EHmtBVKjeZ_yhOug4IPqUaimg0mr5SO_j_Hpd5n80-OwmBY1TH_lu3mF4NaQV2TrZXu0ClWZr7Hv3H4-xFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💸
🇮🇷
🇮🇷
ارزشمندترین بازیکنان فعلی سرخابی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105328" target="_blank">📅 11:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105327">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f75defa90.mp4?token=ONEicbSkrF6nY55XHZ9aXBruTxJRr4J-JHzyiEP7qSOPSlw14EQfG2asbut75mnhRAFYciayrogGfg6i8IFP-0L_0-OJw_9BpfNRAvFYHMQD_-vxVUJN0Km1s32pjRv5Q_hYMb49PoWZW6IJyiFfbBnXlfD2Ctm98fjQABvO64qai_ZKpG5G39hRUMw5nOtfDJdg4ft-l83Lrs-TAxWBO5uN7_yE7n4pFBV4OPKONTy9BysXLIOlCJDEBoYXHe_tK8queXNVjUMLwHZzxd2tHTJGYndJi2jc68bj1Xx7kOYh4ZAOpJ6z3R2zeQyYkgEHLF5CFBEIx7yvGOFelO7K231lMFgEhSDe5zKCf7HKlHYakNcZGoN6O1IAuVOmTxpQ5Xp0KOpxNe7TBvK_f7ZloFZMktqU4R-6IHaJAvPHM4EbxSPIvNF2ZoehBHisvBx3c_nC2bC57V3Zx5Fd4YpDedEJ8X2wpOoSUYdqHdkh8TN94s68Xl-5PRdHnN1o7jDqbchnRbSxAP4CVrQGSxK8JNkNiwMjcorGI8R05ieJHy3q9UuIq8WSgCRGdV9u1i8pejR1w5NGAEaUdQB8_2jEgLp7ic2ndq4ktzQ2qrO-836C_MFppfu9LxFWac-ywMdtzMz77hoNDmszzhA-om1-OOuicy7-u8Q6sn98i8Bn1go" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f75defa90.mp4?token=ONEicbSkrF6nY55XHZ9aXBruTxJRr4J-JHzyiEP7qSOPSlw14EQfG2asbut75mnhRAFYciayrogGfg6i8IFP-0L_0-OJw_9BpfNRAvFYHMQD_-vxVUJN0Km1s32pjRv5Q_hYMb49PoWZW6IJyiFfbBnXlfD2Ctm98fjQABvO64qai_ZKpG5G39hRUMw5nOtfDJdg4ft-l83Lrs-TAxWBO5uN7_yE7n4pFBV4OPKONTy9BysXLIOlCJDEBoYXHe_tK8queXNVjUMLwHZzxd2tHTJGYndJi2jc68bj1Xx7kOYh4ZAOpJ6z3R2zeQyYkgEHLF5CFBEIx7yvGOFelO7K231lMFgEhSDe5zKCf7HKlHYakNcZGoN6O1IAuVOmTxpQ5Xp0KOpxNe7TBvK_f7ZloFZMktqU4R-6IHaJAvPHM4EbxSPIvNF2ZoehBHisvBx3c_nC2bC57V3Zx5Fd4YpDedEJ8X2wpOoSUYdqHdkh8TN94s68Xl-5PRdHnN1o7jDqbchnRbSxAP4CVrQGSxK8JNkNiwMjcorGI8R05ieJHy3q9UuIq8WSgCRGdV9u1i8pejR1w5NGAEaUdQB8_2jEgLp7ic2ndq4ktzQ2qrO-836C_MFppfu9LxFWac-ywMdtzMz77hoNDmszzhA-om1-OOuicy7-u8Q6sn98i8Bn1go" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
مارک‌کلاتنبرگ: پنالتی تراکتور در بازی مقابل شمس‌آذر گرفته نشد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105327" target="_blank">📅 11:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105325">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZCCwLpGQ-D_75hRTnxVdYqCqzQ9ENFC_nODzgHdGyPmkvHy-u6RHE2EtoZyJTIjsBawZm8w5Eo22HWBfSQ4l__fQg3nu9SV4Q4vSLl2rGJJ99jgTzjV8LoEj46sG8xgk8D_w-UJtdIk5ZYfT-TaFAovnT6KWzd0-lt1MQjrXkzQ_MHT6Ln9kHKqZH5wGIep1JZIygrXqk8rPgKk9ZZs0z-QYhqYBhlTNwiKAXPpgg5gTCBiIJ95dhkPl_OzILkaNw-vmoq5cu7ACedxkgz81lTqr0gbLjFWhbTklFEMefUvPzz41xAkflWfLkQCryWyQ1q2qgCVfNOxe_WK5EfReUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VKuBkaSB__DDa72YDEUUkiFNzVRly3bPjQ8QWndZOj_NxzE_SaKvTatIkjlgaQYx3rsQXKj6qt8BhVp9VeeJljyvEyUGLG14Mrawh_gqR7GX2Kj8bpDH0V1e4IXaeLHm2Mazlg3XscerXC3kCOY_cNGOR37cEpzZ2yx9X45ce8GvZ3W5eunmSPEt92niXv89VVHkCij0k7X7LYH2XIf5L0IGMBnY9H0XFD2MftvOJY_zvZ0Bn8ZUNMevpjt4xe6m8W4txN88Vyc0SuHL6IiosDN1ubi7hBte0tqsa9zS50LxGes-Csfc2gUNcKuLYgOik2VoIKMejdy8vWzczOz2CQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
پوستر سرخابی‌ها برای دربی امروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105325" target="_blank">📅 11:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105324">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">▶️
👀
🇮🇷
🇮🇷
مروری بر دیرهنگام‌ترین‌گل‌های دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105324" target="_blank">📅 11:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105323">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHpDA8yfzidtt2yEagXrGMAhzSfECTLHsjaWWCO32f_2TuLepFbGY6YekEV1JsUwG55DKVqBh0znCeL3VcX1Vb5-Ff9CmvlTQvQkdb-32XRZ_h0AMRTLyUjcb1LIgbEe67ISG2i0kMFXUIEAy-Bsia3WQe6XDwpb3PB0-gayvDI83y7VrSeNCtYLRcY22mMYu9D8jPwy2EsfNn8Dxxy9ekuW7UOW6vCnQC-MLc2kJhP7NF6VFnRVpTqK_Nk5GBOUnl8CEZaEzTD5wfRWmoj2jxL97-OUm60UPxakvHgZ1XvMfZ7b2VEY_5AhJxT7yYCcfZyzyFqHaDwKyspTD0xe4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✅
🇮🇷
🇮🇷
مقایسه افتخارات رسمی سرخابی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105323" target="_blank">📅 10:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105322">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a3bce317a.mp4?token=CYBzW2jjONq4IgVZTOrpKe-Sbjt9AyxDvY0kWspSeFAFP41z9QN54hCZKkfH18HMoXvlDvF96_8TIDaC4EzPhgundUNDLag_W-BdMepiCj82Qa-vA_9-1ivH01D93DcwkSdu-fOz5mlYXEMLy6IhdXSN0kBUmkldHtALtNO-24brQx-UZ3kmPs0eo12YLEu3icvVNflfNHc92JCkJkjb2QsED7X4tmk_cIX2nOH8ch5-dg7xU_n0QLpN6XY5Ul3f7u2odo7OyXnWS8eYOpZXCaEaac0WEH4VgZ2gowSnKDxuNwtir3BySSubc35zYAmNHFKsX1goilu9JS0F38OGBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a3bce317a.mp4?token=CYBzW2jjONq4IgVZTOrpKe-Sbjt9AyxDvY0kWspSeFAFP41z9QN54hCZKkfH18HMoXvlDvF96_8TIDaC4EzPhgundUNDLag_W-BdMepiCj82Qa-vA_9-1ivH01D93DcwkSdu-fOz5mlYXEMLy6IhdXSN0kBUmkldHtALtNO-24brQx-UZ3kmPs0eo12YLEu3icvVNflfNHc92JCkJkjb2QsED7X4tmk_cIX2nOH8ch5-dg7xU_n0QLpN6XY5Ul3f7u2odo7OyXnWS8eYOpZXCaEaac0WEH4VgZ2gowSnKDxuNwtir3BySSubc35zYAmNHFKsX1goilu9JS0F38OGBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😂
🇮🇷
محمد نوری سرمربی صنعت‌نفت در کنفرانس خبری دیروز تیمش بازهم شاهکار خلق کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105322" target="_blank">📅 10:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105321">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✅
🇮🇷
🇮🇷
سه‌دقیقه فوق‌العاده شنیدنی و دیدنی با نوید استادرحیمی از دربی‌های جنجالی و خاطره‌انگیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105321" target="_blank">📅 09:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105320">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca6813881.mp4?token=C6INRLYrkrev9DpFaknK6U8ubfDG41jgrK_y2i-m86FnObgjg6obtmEcG9Uf_HowJIzvWaQZ_X6FcbSQCutUI3Bw2DvWQASZOiMYhSnBzK4IvOSpN4dlcnMLI6h_6-wbHAagrTaBHFkS-PpfrCJYJahh6Rn1eakQovHrzpZnGOvhwsQCVe1BZZr4oLo5DQPBcI8O2o5JbjK3FACY24KN13S79wSqqxiTDwKDYeNdC6QAQ0SeNWp2HWxMVEqPaahPxK15EvK-fGv24PfR3PQancSwYbjUtW9BrOv8G9_FQ_8Cfmi3GLPDB4jTGHP72mmV9U1SoeJFj4zEMKwzoghdZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca6813881.mp4?token=C6INRLYrkrev9DpFaknK6U8ubfDG41jgrK_y2i-m86FnObgjg6obtmEcG9Uf_HowJIzvWaQZ_X6FcbSQCutUI3Bw2DvWQASZOiMYhSnBzK4IvOSpN4dlcnMLI6h_6-wbHAagrTaBHFkS-PpfrCJYJahh6Rn1eakQovHrzpZnGOvhwsQCVe1BZZr4oLo5DQPBcI8O2o5JbjK3FACY24KN13S79wSqqxiTDwKDYeNdC6QAQ0SeNWp2HWxMVEqPaahPxK15EvK-fGv24PfR3PQancSwYbjUtW9BrOv8G9_FQ_8Cfmi3GLPDB4jTGHP72mmV9U1SoeJFj4zEMKwzoghdZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
🇮🇷
فقط اونجایی که صداسیما زیر نویس میکرد دیگه نیاین ظرفیت تکمیله
🥲
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105320" target="_blank">📅 09:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105319">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇷
🇮🇷
یه ایرانی رفتی از دربی کشور زیمباوه برامون ویدیو گرفته؛ به دربی سرخابی‌های خودمون تشبیه‌ش کرده
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105319" target="_blank">📅 09:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105318">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوووووری
❌
شورای تامین استان اصفهان در صورت تشدید حملات و درگیری‌ها تا ساعات آینده صبح فردا جلسه‌فوری تشکیل خواهد داد و در صورت ملتهب بودن شرایط قرار است بازی دربی را بدون تماشاگر اعلام کنند. هرچند تا این لحظه سطح درگیری‌ها به نواحی…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/105318" target="_blank">📅 08:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105317">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ebf67c803.mp4?token=p951tuyC6GI1nYxjsRoUQPZiv8M0CwVYFMjp7mI-IUTCzqu2ndIsd3cKThBuCvXjdUL98XDXzDdvemt71kYDPsWXfGeWBm3Xov6riaxfVql3zv36SAnxXd0HH380-wshNCjojy-MBTauu13yTTmbfMNwNBeGJ_7K2IiYYzhx6cxtfXkBN5Aw7Pl3iFZJGtiPKp49GYXKUQIBrNsl2aqv63bt6cOrtJZsuitNgQuhGNhWinYcCHJgE1I3wSA5YRprrla7ImTt80VsuIbhcrFcsGerCODkU6geOv_QIBSIdwxUxJjSx5t1GsZrXVd7pKjtP693f8DRYdN8kSNkB8eZo54jzPPGLKVFoKDS4acWDqPhlbAGN6GwIRqNB8dR3ONSuNwu8NEWsHtehs_nrgliRMVUxH-EqKuo4o1vBuoluHn1VBsxoJChLRkj1kvcLA-nPDiFGc58zEUt7Kw4LB8jDTeI_9S5a5szrtQH1TM9yfzSsrGf0GhZi5H-DcMadRcOlVAGCze7LhDD4VwJsBz4i9d_eEmXM02jSX2WaSjlg8GixfPf31QnQFODiqDu-oflGxyfc7WhWeXeNOTghIZQhIxdWlVi0yEk2QyElXPF3Me0TnXKVH8jQOM0xAI2fzo5tboN3k8DIK-vljIFJX2rwdGwvtFr1R3_Hs108FYmzao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ebf67c803.mp4?token=p951tuyC6GI1nYxjsRoUQPZiv8M0CwVYFMjp7mI-IUTCzqu2ndIsd3cKThBuCvXjdUL98XDXzDdvemt71kYDPsWXfGeWBm3Xov6riaxfVql3zv36SAnxXd0HH380-wshNCjojy-MBTauu13yTTmbfMNwNBeGJ_7K2IiYYzhx6cxtfXkBN5Aw7Pl3iFZJGtiPKp49GYXKUQIBrNsl2aqv63bt6cOrtJZsuitNgQuhGNhWinYcCHJgE1I3wSA5YRprrla7ImTt80VsuIbhcrFcsGerCODkU6geOv_QIBSIdwxUxJjSx5t1GsZrXVd7pKjtP693f8DRYdN8kSNkB8eZo54jzPPGLKVFoKDS4acWDqPhlbAGN6GwIRqNB8dR3ONSuNwu8NEWsHtehs_nrgliRMVUxH-EqKuo4o1vBuoluHn1VBsxoJChLRkj1kvcLA-nPDiFGc58zEUt7Kw4LB8jDTeI_9S5a5szrtQH1TM9yfzSsrGf0GhZi5H-DcMadRcOlVAGCze7LhDD4VwJsBz4i9d_eEmXM02jSX2WaSjlg8GixfPf31QnQFODiqDu-oflGxyfc7WhWeXeNOTghIZQhIxdWlVi0yEk2QyElXPF3Me0TnXKVH8jQOM0xAI2fzo5tboN3k8DIK-vljIFJX2rwdGwvtFr1R3_Hs108FYmzao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
روایت فرشید باقری از درگیری عجیب سیدجلال و مهدی رحمتی در دربی ۸۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/105317" target="_blank">📅 08:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105314">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
اگه استقلالی هستی، به هیچ وجه این کانال رو از دست نده!
⭐️
💙
📸
پوشش کامل بازی‌ها با عکس و فیلم‌های اختصاصی توسط خبرنگاران و عکاسان ما
📰
اخبار و حواشی داغ آبی‌ها
🎁
🎁
و قسمت جذاب کار: هر هفته قرعه‌کشی به همراه کلی جایزه
🔥
🔥
اینجا فقط یک عضو ساده نباش، محتواتو بفرست…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/105314" target="_blank">📅 01:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105313">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTzlb9pWndldtn9Olx9KWUlf2EnxsH4kifBHBxgq270EkYX2IG983PDC_evvEasbNgP9-xtazVPWA0H-FVKMcXuoNUNfgWB7Qj29o94ODhDl9-0k40ahInko7E56RjyllFBKLF4lE6ZoPufOANIvap9P0GNHyoO9czPonLiJyiBHYr8iy3_pcAd9a-4_ybqh1WV_LWHoeaslpxtxt11meYb5-uFQAcbcME5gw-78MpAsJFNwynpwXOUwICcvbWHk7uEFIYZHt16vKD0dSDNb62hHVn0YbEG4AWvAuPT9YnHZy9z5vTWO5P6LcnRpyOHLd9IceSM3Po1--TDx5oIOBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگه استقلالی هستی، به هیچ وجه این کانال رو از دست نده!
⭐️
💙
📸
پوشش کامل بازی‌ها با عکس و فیلم‌های اختصاصی توسط خبرنگاران و عکاسان ما
📰
اخبار و حواشی داغ آبی‌ها
🎁
🎁
و قسمت جذاب کار: هر هفته قرعه‌کشی به همراه کلی جایزه
🔥
🔥
اینجا فقط یک عضو ساده نباش، محتواتو بفرست و منتشرش کن
🔥
با استقلال... برای استقلال
👇
💙
@Esteghlaal_twitter
@Esteghlaal_twitter</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/105313" target="_blank">📅 01:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105312">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/105312" target="_blank">📅 01:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105311">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⭕️
⭕️
با توجه به نزدیکی به دربی پایتخت و بازدهی فوق‌العاده تبلیغات تا پایان هفته، اگر تمایل به همکاری و انجام تبلیغات مدنظر خود داشته باشید، با ×تخفیف ویژه× در مجموعه تبلیغاتی تیوا با بیش از ۱۵ کانال مختلف ورزشی و غیر ورزشی در خدمت شما عزیزان هستیم   برای هماهنگی…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/105311" target="_blank">📅 01:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105310">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
⚠️
یک فرد ناشناس در مشهد با خودرو به تجمعات جانفدایان ولایت حمله کرده و تعدادی کشته شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/105310" target="_blank">📅 01:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105309">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f42b196ef1.mp4?token=p3Z1wSfncWXd_s0KRZscbn60QNIK5FuxaEIdeP7Bw8Rl2DVuxciLBQYRNK_-izkV81FMU2dOhSzB_ENgSL9xaflE4XXYV5UHR0wWUrD0u_KgQA04PHx6_NLOunctjXf98OozjCDdXF0XvOxifMN4UHR5MDWp0dvXQnMECJ6NLW4I-XQUwKJw2zJkhFxmR_z6uqPZnaAHVZZolSSbKuxuq1EJvsWscer5Jk04LYcHRTvfTp698ZovkWyDgK9wQgnYsH9i6Dpdizvvxu_Fz-I_KXfg-019HHZc9GxaJ_ebLU-iPdf9AdUU6zF5HUyypst7uYsGPCjrkPS0HoYN1dzgBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f42b196ef1.mp4?token=p3Z1wSfncWXd_s0KRZscbn60QNIK5FuxaEIdeP7Bw8Rl2DVuxciLBQYRNK_-izkV81FMU2dOhSzB_ENgSL9xaflE4XXYV5UHR0wWUrD0u_KgQA04PHx6_NLOunctjXf98OozjCDdXF0XvOxifMN4UHR5MDWp0dvXQnMECJ6NLW4I-XQUwKJw2zJkhFxmR_z6uqPZnaAHVZZolSSbKuxuq1EJvsWscer5Jk04LYcHRTvfTp698ZovkWyDgK9wQgnYsH9i6Dpdizvvxu_Fz-I_KXfg-019HHZc9GxaJ_ebLU-iPdf9AdUU6zF5HUyypst7uYsGPCjrkPS0HoYN1dzgBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚠️
تصاویر دوربین مداربسته از حملات پیاپی به نزدیکی یک مراسم عروسی سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/105309" target="_blank">📅 00:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105308">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0ZKGxJbMrjBGQlmO0kvBnj7vMsXXurlMWExKcqncNG-8C2l9uqPe8AbzJKcM3FYWwSioT4RcmA-na84p0mChJ7IsBe29v6Mo8-cwnwOxB5DNnbhSD6__RwFYSucUOhS4SRebCGztC1UT0FYUa0jxzCYfgWOQoT0LNQasZrH-EmQcexGX5QhQy2qalKvzz-b4qlklpi_BYHW8OVc5COiZEoMAlyzz1MZags0IKZCsmZgWEQalsfPhZoEH5LvpExOozh1J8Ikkk7Z45UfluL1r7GOrJexx1BOd8A_ffkgWMLnR8MvRT0UqWrUNUQ8QOiBKJP-k1zFG9xa6eOsKIMtWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوووووری
❌
شورای تامین استان اصفهان در صورت تشدید حملات و درگیری‌ها تا ساعات آینده صبح فردا جلسه‌فوری تشکیل خواهد داد و در صورت ملتهب بودن شرایط قرار است بازی دربی را بدون تماشاگر اعلام کنند. هرچند تا این لحظه سطح درگیری‌ها به نواحی…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/105308" target="_blank">📅 00:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105307">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوووووری
❌
شورای تامین استان اصفهان در صورت تشدید حملات و درگیری‌ها تا ساعات آینده صبح فردا جلسه‌فوری تشکیل خواهد داد و در صورت ملتهب بودن شرایط قرار است بازی دربی را بدون تماشاگر اعلام کنند. هرچند تا این لحظه سطح درگیری‌ها به نواحی…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/105307" target="_blank">📅 00:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105306">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180
#فوووووری
❌
شورای تامین استان اصفهان در صورت تشدید حملات و درگیری‌ها تا ساعات آینده صبح فردا جلسه‌فوری تشکیل خواهد داد و در صورت ملتهب بودن شرایط قرار است بازی دربی را بدون تماشاگر اعلام کنند. هرچند تا این لحظه سطح درگیری‌ها به نواحی اطراف استان اصفهان نرسیده و این اتفاق تقریبا بعید است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/105306" target="_blank">📅 00:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105305">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cf9805271.mp4?token=T2SnG4FQyYnbJZnFQTy4r3f8KqGTQi0Zk7Bo5DnbEKG8ZqvM1_LeOrZF3VCvAstsXK2s8p1ccdqTl135KfhoDz0HtMIkpACQRTVrjdmpsQtWWDX4HM7nKJEk1AeKtGzMsaXApk7PLk_AXRZmxffOzHdXGtmf3Uuc_XxM_BcSWKQiAoUHGnERbiQGJjgvsSLzQ1qEngjTxjthGdzCL8Kqtq3Ya3ZiTzaQuNc9DVRv56FF9guaBHgV7d-iYNbGQl6Zl3o07iARiLMKq5CnqvA5q2YJ0yxbj9meNfm2cXcaq0Nft3xIkhci8_dYFJqkMS1eXRuCILXJNhzHMiIpxsscAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cf9805271.mp4?token=T2SnG4FQyYnbJZnFQTy4r3f8KqGTQi0Zk7Bo5DnbEKG8ZqvM1_LeOrZF3VCvAstsXK2s8p1ccdqTl135KfhoDz0HtMIkpACQRTVrjdmpsQtWWDX4HM7nKJEk1AeKtGzMsaXApk7PLk_AXRZmxffOzHdXGtmf3Uuc_XxM_BcSWKQiAoUHGnERbiQGJjgvsSLzQ1qEngjTxjthGdzCL8Kqtq3Ya3ZiTzaQuNc9DVRv56FF9guaBHgV7d-iYNbGQl6Zl3o07iARiLMKq5CnqvA5q2YJ0yxbj9meNfm2cXcaq0Nft3xIkhci8_dYFJqkMS1eXRuCILXJNhzHMiIpxsscAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
⚠️
یک فرد ناشناس در مشهد با خودرو به تجمعات جانفدایان ولایت حمله کرده و تعدادی کشته شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/105305" target="_blank">📅 00:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105304">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcaf59f19.mp4?token=CP1UPBA6W71OaQcvmNRnZUZOn2-KP_UCNpLG7Au7T7_TpnI7fC4aZKz_qePQ5B97py1QVKEk8ml_IbBK58MlfKflsMWnFc_5v0q72NAdXA_xwmSwv7ahEaK4qpxFOot_mozBAT8-rXoO7KKJ8ghcDZMtxt6oaKsSSBZnviMkQ6DD54FhykLQoRTANAlOaG68Vwyi4usOr1gH8W_AiuGRyuCSGqf71KCirheUJx5nGw60hPe4wmLzvCWjR5eg1Aa_2FRAI6mf1sooWPIIx8gFAHeM6Yb-Z_k6yDPjF4dTWUn7sndg4jfZI4jfav3e5IngxvCfl7NbizPVQ3HfMk_0EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcaf59f19.mp4?token=CP1UPBA6W71OaQcvmNRnZUZOn2-KP_UCNpLG7Au7T7_TpnI7fC4aZKz_qePQ5B97py1QVKEk8ml_IbBK58MlfKflsMWnFc_5v0q72NAdXA_xwmSwv7ahEaK4qpxFOot_mozBAT8-rXoO7KKJ8ghcDZMtxt6oaKsSSBZnviMkQ6DD54FhykLQoRTANAlOaG68Vwyi4usOr1gH8W_AiuGRyuCSGqf71KCirheUJx5nGw60hPe4wmLzvCWjR5eg1Aa_2FRAI6mf1sooWPIIx8gFAHeM6Yb-Z_k6yDPjF4dTWUn7sndg4jfZI4jfav3e5IngxvCfl7NbizPVQ3HfMk_0EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
جملات قصار و واکنش منصوریان به حکم انضباطی علیه الطلبه؛ از جیب خودم خرج می‌کنم رای برگردد! مستقیم می‌ریم CAS؛ یونس محمود ١۵ سالش بود من بوندسلیگا بازی می‌کردم
❌
⚠️
در شرایطی که دیدار الطلبه و نوروز در هفته سوم لیگ عراق با برتری ۱-۰ شاگردان علیرضا منصوریان به پایان رسیده بود، کمیته انضباطی فدراسیون فوتبال عراق حکم به شکست ۳-۰ الطلبه داده است.
😀
دلیل این تصمیم حضور همزمان ۲ بازیکن الطلبه با پیراهن شماره ۷۷ اعلام شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/105304" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105303">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0Z7USyswxkIoCaG83kBReHNLmes_Tqy4ILl2j6akU1d-Nz33ezSI9_NOSLpZrsJoQkwN1uYHs97zDaMHFHP44cpSXTEyQ8TQL1p3s-VeXMN26lMBJUeU-qdNhF7-OAsyS_O3drcAJrX3vuhA0W6kAqkjUhMW6-khFJTk7XBCfuaMXR_5VMyK0ZObzCD_Vgq5GlfCYCDRKHi1Rz-ElxiBUCRp5POkF06SQ_25Qg8zDqougiCwZ7PcNPyIBG457TrWvLCCygW7zcIYh8w5UndSp3gMiEDgYLX-IkmI_UZBruDkCWQ8n7rh1lypQesVl-cY__yTjslY1rWx523FrCEVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رسمی؛ اندیایه با قراردادی پنج ساله به ارزش 65 میلیون پوند از اورتون به سیتی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/105303" target="_blank">📅 23:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105302">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
گزارشات فعالیت شدید پدافندی در شرق تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/105302" target="_blank">📅 23:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105301">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👍
🇮🇷
بانوان جذاب ملوانی در بازی با پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/105301" target="_blank">📅 23:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105300">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f706e532c0.mp4?token=EkJ9-XlFeHtO3ODl5SAOg2VAmhvgzB-KOSxikh5-jqJWgkXK9Oj8DVvHE-V0GMqIPBemKTudKrAtLq_hUQ88uxn7kpQZ2O8jKS18ykz_zaLIXy1IHbNbnm03KU1jStubWn57fYwSpGRzcOm9DnjyruQz9jrotFMQ165qgmV01BzhWNVLcsqaa_eb3cId15rBw2NKG0XV0c3ghtHgNL-PJtouiWIiHas-4F1piqzpPZq_i54Q70dNNMKSNCmVZbBInDpjbEEgtkyLTCyRu5_kjLCqBaXmmVcZ4NAV8ucoqmYjXZ2wYk7Q6p_RGg48mJkoy1tMmn17s0zUpfetcBJN_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f706e532c0.mp4?token=EkJ9-XlFeHtO3ODl5SAOg2VAmhvgzB-KOSxikh5-jqJWgkXK9Oj8DVvHE-V0GMqIPBemKTudKrAtLq_hUQ88uxn7kpQZ2O8jKS18ykz_zaLIXy1IHbNbnm03KU1jStubWn57fYwSpGRzcOm9DnjyruQz9jrotFMQ165qgmV01BzhWNVLcsqaa_eb3cId15rBw2NKG0XV0c3ghtHgNL-PJtouiWIiHas-4F1piqzpPZq_i54Q70dNNMKSNCmVZbBInDpjbEEgtkyLTCyRu5_kjLCqBaXmmVcZ4NAV8ucoqmYjXZ2wYk7Q6p_RGg48mJkoy1tMmn17s0zUpfetcBJN_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🔴
خداداد عزیزی: داور عجله داشت بازی تمام شود
. چجوری 2 دقیقه اعلام کردید؟ وقت اضافه را کی می‌گیره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/105300" target="_blank">📅 22:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105299">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f17ff9c0b.mp4?token=KnMzfvszTTbJ_hd3VhVmwJLe16mHXUjcLLmxGnz5ZC4byrVOQk4ATX-P-SVhJaRZfo4L7fEGH-u00lUyqLWWWoDVz74KQJQBDNHIG3soITyIWQ-b6WO8GnVsOdwTJTaCft2Gy3N-iE-d-6ZUHegBpySWrLbdfKtsaNYOdedTxEwPCzxbKKQFdelWSgFvKCiENY6HIAcg_RbzLhAcXS5KXrPYKsm3Yd9IxFTV-640gOLvMeM3cK9Bh3wp9m3ANoe0Yv1zUqwBXBW4D2KwMxXd0WTJwVzJoEUgNPyqv0CII3i_O4PM0jTgnc4ZuNp1aR4kcciM9c0siTk00S8PWn7v2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f17ff9c0b.mp4?token=KnMzfvszTTbJ_hd3VhVmwJLe16mHXUjcLLmxGnz5ZC4byrVOQk4ATX-P-SVhJaRZfo4L7fEGH-u00lUyqLWWWoDVz74KQJQBDNHIG3soITyIWQ-b6WO8GnVsOdwTJTaCft2Gy3N-iE-d-6ZUHegBpySWrLbdfKtsaNYOdedTxEwPCzxbKKQFdelWSgFvKCiENY6HIAcg_RbzLhAcXS5KXrPYKsm3Yd9IxFTV-640gOLvMeM3cK9Bh3wp9m3ANoe0Yv1zUqwBXBW4D2KwMxXd0WTJwVzJoEUgNPyqv0CII3i_O4PM0jTgnc4ZuNp1aR4kcciM9c0siTk00S8PWn7v2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇮🇷
🇮🇷
همچنان از بانوان پرشور اهوازی در حاشیه بازی استقلال و فولاد خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/105299" target="_blank">📅 22:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105298">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344f252bb4.mp4?token=hWYQFxBov_lRn5OoPtGetnk25nxSfIv9kvu67wjc-S9TAAvqU592w3Ubi9-SX7fhQeKVP_WZcoOec3tiBKfvAcEoxcM1CZyDyF_b2xWJfdpvwymnl_qArJThCQKOy3VeoUHGAv7MDhxeosOWH8hSleLLG0H8j9Up04J79suPYHYFyhyKCYqVdfPHtOgAeLnlIHnaXmTmFYAEGOBn2g6DXcjTN1MfMBSkjVul8ils_znAwtvDCiNeMRQdc-dvokN1C94Kck333zRBv0u3fpwn_weR5KVWbxhTq5QSIvGCtybFI-NSZtaFfAgg3ZWf8UbRqMSc389w86rURgk-ONU2-30l12biUTBXBvHt-7MmzirxJ7L-3OhrottKyfbzPfv_A9YoVqVDd1cMm4Ju-RVBmr1Z5WmANHUdj2WTHQ6X5-B0vvNNrA9p494ZXg7RgFc2u09CFX-cT_FFn-U-brQ6dj1NoU5Csd7MHDEL6NDiDuRAQZWFinOf0n8w5PZkUYiS6idIs5xl4al6xYgZiDnBupKYxVbWVCtXBMfp4OKbwyM4PDNR9VRr2srfqB-MajTIMdClE1oeVkn-4UV2s4khPpe3gsx8enuwB_g2TE1r4CK3aFRUeiE_BoYPrbTQ6ccqtRYmMnw49o8-knbPLdGkVYFY1_-tJDuFiKJvUEoiQgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344f252bb4.mp4?token=hWYQFxBov_lRn5OoPtGetnk25nxSfIv9kvu67wjc-S9TAAvqU592w3Ubi9-SX7fhQeKVP_WZcoOec3tiBKfvAcEoxcM1CZyDyF_b2xWJfdpvwymnl_qArJThCQKOy3VeoUHGAv7MDhxeosOWH8hSleLLG0H8j9Up04J79suPYHYFyhyKCYqVdfPHtOgAeLnlIHnaXmTmFYAEGOBn2g6DXcjTN1MfMBSkjVul8ils_znAwtvDCiNeMRQdc-dvokN1C94Kck333zRBv0u3fpwn_weR5KVWbxhTq5QSIvGCtybFI-NSZtaFfAgg3ZWf8UbRqMSc389w86rURgk-ONU2-30l12biUTBXBvHt-7MmzirxJ7L-3OhrottKyfbzPfv_A9YoVqVDd1cMm4Ju-RVBmr1Z5WmANHUdj2WTHQ6X5-B0vvNNrA9p494ZXg7RgFc2u09CFX-cT_FFn-U-brQ6dj1NoU5Csd7MHDEL6NDiDuRAQZWFinOf0n8w5PZkUYiS6idIs5xl4al6xYgZiDnBupKYxVbWVCtXBMfp4OKbwyM4PDNR9VRr2srfqB-MajTIMdClE1oeVkn-4UV2s4khPpe3gsx8enuwB_g2TE1r4CK3aFRUeiE_BoYPrbTQ6ccqtRYmMnw49o8-knbPLdGkVYFY1_-tJDuFiKJvUEoiQgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇮🇷
حمله شدید اللحن شجاع خلیل زاده به عادل فردوسی پور: همه می دانند فردوسی پور با تراکتور مشکل دارد!
💬
شجاع خلیل زاده: من دو سال است که فحش می‌خورم اما خم به ابرو نیاوردم/ فشارهای زیادی روی من است و خدا را شاهد می‌گیرم که در مقطعی می‌خواستم از فوتبال خداحافظی کنم اما این کار را انجام ندادم/ دو سال فحاشی به من شد. تمامی این فحش‌ها تقدیم به عادل فردوسی‌پور/ همه مردم تبریز می‌دانند عادل فردوسی‌پور با تراکتور مشکل دارد/ از زمان برنامه 90 همین بود، الان هم همین است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/105298" target="_blank">📅 22:24 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
