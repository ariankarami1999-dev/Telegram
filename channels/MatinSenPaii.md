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
<img src="https://cdn1.telesco.pe/file/Kc0_gko5moHzS2wj6oJY0CeAihOCgsE0LUqAIdl4ERnK7K1lk0R648gTy91u5P0G1d5JyPWl6a9E8bituAwNXFUi5MnA0Iu4INeuk7Gf8K_uNYECHLYIN87G6caBZWYrteMWbMKA7jOaVN0QP0eSpuQ6rOZSw3LwCcV1nEsyOQDJzDBvNn-tdF5T33UOGftCdlx16VrpQ7ewkmP0HKKfMPrO9s2Y6AB1hZK01zD0wb6_QqULbRGRFEB6Z_KWyxLWSGTdMlhk26MTO26mGQbadkC1-JMcBfs4Wl4tClcoGvUOy0oxsx6Of7LS2xNXkGeK1MhdSu6-giphs3tBMhBEBA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 10:52:38</div>
<hr>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=kXrPPH0YGPpgZ0p-aYLgycuuCd6TvXdqIFn4bLisYuubQK8gIKLqZFemmxj08RL-HlSOkOCOM8P06mbVU6km62NbdaZ5k6Rvckv6jlnOJGqs54GGMrOT5RSKmWng2vTlbths1lGtD_SEaDp-A0MB_zTBZ31_G3MUhEo6IiY8n0prNPo3Ud5zqcMzg1i09vevOW6FKEhzWQxhhubLzwoDU0_Fi0-tJu0OAd1ltRqctqxn3cJT3_wq6YWWqwViV5gl3aM5A04GgiW2MVqwA_l1w4NrDMGTMIieiPuD-GlqGlxKAju7snpun5-xTtDbjHytVQmS_fnTZsWbgBs_n2qVNRvTNumFqVIjOgVbt6RDUS5Exb7bAmFuv6mK8T6TaJniTKVxR-y0_wlF4fEnTDlQgtslXPFTsliPOLcfV454wCTZp5UcOvFMW70xDCCGgKOHlCdS6vQi68_vjT30wGR9z0_rjt3ZkHgsjpqyshJDnFRsVSA9JRW-szMmpdcKFPXDg3DplGxPbf-rCTLB1HJI7TJiKGt5gMJPBAstDLZShPAp_AJZVapoW6PDY_PDoIl6C-wkNa5fTm_PMWaJJ8MzL9BodMQ68qa7Fx-zotcec4qrb7_FouFwKz7oGpqakspeb_b-e2vV7EDkEDow7sMf35W5jxElq0g9nHwHsBfaTHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=kXrPPH0YGPpgZ0p-aYLgycuuCd6TvXdqIFn4bLisYuubQK8gIKLqZFemmxj08RL-HlSOkOCOM8P06mbVU6km62NbdaZ5k6Rvckv6jlnOJGqs54GGMrOT5RSKmWng2vTlbths1lGtD_SEaDp-A0MB_zTBZ31_G3MUhEo6IiY8n0prNPo3Ud5zqcMzg1i09vevOW6FKEhzWQxhhubLzwoDU0_Fi0-tJu0OAd1ltRqctqxn3cJT3_wq6YWWqwViV5gl3aM5A04GgiW2MVqwA_l1w4NrDMGTMIieiPuD-GlqGlxKAju7snpun5-xTtDbjHytVQmS_fnTZsWbgBs_n2qVNRvTNumFqVIjOgVbt6RDUS5Exb7bAmFuv6mK8T6TaJniTKVxR-y0_wlF4fEnTDlQgtslXPFTsliPOLcfV454wCTZp5UcOvFMW70xDCCGgKOHlCdS6vQi68_vjT30wGR9z0_rjt3ZkHgsjpqyshJDnFRsVSA9JRW-szMmpdcKFPXDg3DplGxPbf-rCTLB1HJI7TJiKGt5gMJPBAstDLZShPAp_AJZVapoW6PDY_PDoIl6C-wkNa5fTm_PMWaJJ8MzL9BodMQ68qa7Fx-zotcec4qrb7_FouFwKz7oGpqakspeb_b-e2vV7EDkEDow7sMf35W5jxElq0g9nHwHsBfaTHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه. - عاااااشقش شدممم. با کدوم ابزار ساختیش؟ + الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/MatinSenPaii/5385" target="_blank">📅 09:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wa_7S39YtpsQg8vggxPZ1iJH33WvuhrqFXU5TVm6ixhZdHp5yvhXJ69dy1b39q4DhU7mtxdcj9dvJlV_HPYxHeZtp7H_R9dyVhVt5QFTp9oaEii4k4yM_MHsHTnhWfHtLPZaZAIis_J9DxNG2f5RZa6AXO8M9uLUHWJ0TkSaY6yAxEA6Y6twmN16oUIkCEn0_BcrChMWTWWbJ96PvALUWLK5bpdPqnRc7z3-74a0SHxJdBKsEKESBLhocw_VK--pb9mVtHf4cP_u0cyX8A8gY5xdIgogVMJ5iJP_MjIafZ53QH-BQou2_9csVRxo_oSrfg0jZUygcmECDGpvRv440A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه.
- عاااااشقش شدممم. با کدوم ابزار ساختیش؟
+ الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/MatinSenPaii/5384" target="_blank">📅 09:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpDG2yUnmCRKO-DR9vwe-uroJTETdAEwwEX-G4CmTC7ccEKrficbIsqdY-2iAt0MdDMHG6ob38VDnr-Tq5EVS9OzKXk6WgyewPj9B3mDkRT5QjVBk0BQfd4JRyl2WuiDVbZHH7HDArjtmVFnrtxb6G9KUMgGYt1rJMCDL0UDiYMyDj4t2EMDcIbOPfR3FmndfHriXncMtBVPnjQkOyukB0297wivo3CFVfZaVPFU8ZPggfPqfP2r9zrf1k5Ut4gjXnA_WuJiZ5JqodlOKPTb44_4ucHvFhIdfhL3Fqr_dtWusLeYdMj6qicaLtoLXvoqW46kHL1mTqJ_L4wFLAs16Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولایا (Ollaya)؛ مثل Ollama ولی برای مدل‌های تصمیم‌گیری
خود Ollama، اپلیکیشنیه برای اجرای مدل‌های Open Weight روی سیستم خودتون. حالا Ollaya، همون Decision Models که Jev ساخته رو می‌خواد لوکال و متن‌باز اجرا کنه: سوال تایپ‌شده از هر متن یا JSON میدی و جواب کالیبره‌شده رو توی چند میلی‌ثانیه می‌گیری. جواب از یه پاس روبه‌جلو میاد، نه از تولید توکن‌به‌توکن: حدود ۸ تا ۱۰ میلی‌ثانیه برای ۵ تا سؤال روی RTX 4090، در برابر ۲۳۶ تا ۲۷۶ میلی‌ثانیه‌ی API عمومی Jev. با API سازگار با TypeSafe کار می‌کنه، پس SDK رسمیش بدون تغییر وصل می‌شه و مدل‌ها هم همونطور که گفتم، open-weight هستن.
اما یه بحثی که وجود داره، API خود Jev انقدر ارزونه که فعلا من با اینهمه کار باهاش 5 دلارمو هنوز تموم نکردم. لوکال اجرا کردن لایا هم خوبه اما شاید بهترین گزینه نباشه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/MatinSenPaii/5383" target="_blank">📅 07:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AZxef-4vC0UIr1iBB2JGIbTW3ylgmrcLt5hKJQwO2PhsRZw_i-ySCWRWAh8a7LThlCOYOmSBGgsDltRHngne-iCZZpC3a1lxvZbIlhmQz2hW5L2GUTDtEglc7XfdRG-6RfAICCen76fReGXmsCs4hXBMRKgjXMnI30yXbo42l-kU5uqV7btGcwaxkI1FeJoa0gTMoDONsiGpTABioFowd3ij8HCvgzQtgipEqShcu9zHuSowdWpVyHIsvxk1DYqeGV-DwstJ-IfLMayKK9_EX1Hx1AkYo_X_yloOq1ZXwQKaCjMfZQdLR7lvoKqaGsXAry6hzX9E1EXEPc6apIy4Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک هست دوستان.
گوگل یهو ایران رو تحریم نکرد. سالهاست ما تحریمیم
گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده
می‌تونید ایمیل بسازید همین الان با گوشیتون و نگران نباشید</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5382" target="_blank">📅 00:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تانل با دو سه تا یوزر و سرور قوی هر 40 ثانیه یه بار ریست میشه
معلوم نیست دارن چیکار میکنن
کلودفلر هم اکثرا کار نمیکنه واسم آیپیا با نت همراه. فیبر وضعیتش بهتره</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/MatinSenPaii/5381" target="_blank">📅 00:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وضعیت اینترنت خیلی افتضاح شده
هم نت هم VPNهای تانل</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/MatinSenPaii/5380" target="_blank">📅 00:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwZUN05IJ-dVDffKCIoDNpV2sEJT-qTbXxHf6roR3QuuvNduDdCExaWqlftj3OueF1Zyoy-182QwMRGN79CeEqpyi0NeXrBMqk1ajwWKERUpUs1bbzL5x_VHynILYICR2dZMdDhKVLpF55fv5o2bJ4coO1DoKnjyfAssgXvVDYcu7b892eByJX3cNhl6gzsYTzTpcXHM7AL7M5NEwD3EPLNBhYcvYMxdt12RvuZX5ft150xVQyx_SK17sKvMpHWYkQ0CpC-RI0avF9pCdIPNO-ZrJD3zneWCjeuoMBkFwsdcj-_esGg6uKJHg-KZAUG2df3uU5ptICapRghRIrTUIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رابطی رو که توصیف می‌کنید، ایجنت براتون می‌سازتش
گیت‌هاب توی اپ Copilot یه قابلیت به اسم canvases گذاشته: به زبان ساده توصیف می‌کنی چه رابطی می‌خوای و ایجنت یه سطح زنده برات می‌سازه که هم خودت می‌تونی استفاده‌اش کنی و آپدیتش کنی، هم خود ایجنت. هدفش اینه که وقت کمتری رو صرف تطبیق‌دادن با ابزارها بکنی و بیشتر کارت رو پیش ببری.
این کارا فایده نداره گیتهاب جان. پلن‌هات گرون و به درد نخورن
برو این دام بر مرغی دگر نِه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/MatinSenPaii/5379" target="_blank">📅 00:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cwmFqQsQSciIFdzsWywoy70xJjwineM2ZHDKW7lgxJPQJz3LBBWbffUOSkutkdiagb03rXKO3kzbS_a2mY7plVSJ4iYXkxO0cF2_VpKrE-XybqlYNn_de_uIU_sfK-Is1qJJhJrYqf3KLEFxh-iP4SpOCrZTpt8EyelD_wI4uh3i7v78r1esTLC4m5ww1ub3EGrXleAU-YN-jZVTEiaYB4jIa0Xe7Gfx-Bh-5HmLr8SIc2Gbixa9EjZbdtBpZ8iFEPr9e6hKIuI1-CAyl9cpt00e4Qyrbh00ss-1AY7G-T0NjeBUUO6EW8DVBvjcyugscvjrTsw4uf8wTp6Te7Bbfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">(باید برم ببینم کپچا فارمش چطوری کار میکنه)</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/5378" target="_blank">📅 23:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YdGWIhaknkLaj0APkIil9d--DLl6sFvLxGcIf8giw5xOeLLtmN50VzTbYZHAazEQ7fq0GDnl7aTK8-_jKfjdW0Pct7OYZBGdLUhT2npxTippLg03D652bxJtYxQiy-Z7dQLPv5eCQm1J-DK84VS0V4I90lzfU_OG8joKLpMX2u4PNnqgWXBmszOpQSFa5Yl1Q8WEpYSdvCDbNIXbbmjrIBqoyk-ZjllJcLy8_JAXGs9tJJ-j1MD7eEECVCMWg6nCnlydcj1xDFOyila-oNWytJ3Ra3oFxEbQlTaql5rrLUzIj43aG-mdC7LniYqZpcxNGYPVVgOXzZSPtWjcyLi6QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر سایتی رو برای ایجنت‌ها به API تبدیل کن، بدون Browser Automation
💪
یکی از توسعه‌دهنده‌ها توی ساب ردیت هرمس ابزاری به اسم
agent-data.dev
معرفی کرده که ایده‌ی جالبی پشتشه.
حرف اصلیش اینه که برای خیلی از کارهای تکراری وب، مثل چک کردن قیمت پرواز هر روز صبح، دنبال کردن آگهی‌های شغلی جدید یا سرچ توی یوتیوب، browser automation رابط مناسبی نیست. ایجنت باید سایت رو باز کنه، بفهمه چی روی صفحه‌ست، هی کلیک و اسکرول و اسکرین‌شات بگیره، و هر بار که لازم شد کل این چرخه رو از اول تکرار کنه. وقتی کار در اصل «این سایت رو با این پارامترها سرچ کن و نتیجه رو بده» هست، خیلی منطقی‌تره ایجنت یه API call بزنه و JSON ساختاریافته بگیره.
حالا این agent-data چیکار می‌کنه؟
1- یه کاتالوگ از APIهای آماده برای سایت‌هایی مثل X، Reddit، Zillow و کلی سایت دیگه داره
2- اگه API مورد نظرت نبود، URL رو می‌دی و توضیح می‌دی چه دیتا یا عملیاتی می‌خوای؛ خودش API رو می‌سازه و نگهداری می‌کنه
3- از طریق HTTP، MCP یا CLI قابل استفاده‌ست، پس برای ایجنت شبیه یه tool call معمولی می‌شه
نکات فنی:
😟
به‌جای HTML selector، endpointها رو روی همون network requestهایی می‌سازه که خود سایت برای لود دیتا استفاده می‌کنه؛ برای همین با تغییر layout کمتر می‌شکنه
📱
خود APIها مرتب تست می‌شن و خرابی‌ها خودکار شناسایی و برای تعمیر صف می‌شن
💰
زیرساخت proxy و CAPTCHA رو خودش هندل می‌کنه(باید برم ببینم کپچا فارمش چطوری کار میکنه)
سازنده‌ش گفته قراره نشون بده این روش در مقایسه با browser automation چقدر سریع‌تر، قابل‌اعتمادتر و از نظر مصرف توکن بهینه‌تره.
🔗
وبسایتش:
agent-data.dev
📌
ردیت
اصلی پست
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/MatinSenPaii/5377" target="_blank">📅 22:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">این ویدیوی موشن‌گرافیک رو با مدل Opus 5.5 برای یکی از دوستان ساختم. و باید بگم با ۲ خط پرامپت و یه ویدیوی مرجع برای گرفتن اطلاعات و متن ویدیو عالی عمل کرد. عالی  حدود ۴۰ دقیقه زمان برد و دقیق ۲ خط پرامپت با چندتا فایل فونت.
✍️
Saeiid</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/MatinSenPaii/5376" target="_blank">📅 21:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=sVNnaacLBtcWfxb2FCEohe0s_HWgTHMYVBGC_aEbqtfzHVnu7QQccG7o4quKSamYN7H5SkuoRAhB_Qt4EJ0u8wt1ZDuHt300Iv9cszl0jjwKWF2hSOdTu0STIUfw5yyil7eDBLFXscEd6in2du9-l80x0Ei79Ry2D_aXbdMs2Q1w8wH5xxO0gu-I-Bx-uxqEoqZ5qnyKvip-_7x34bS4nOQ1YgAMUXjy9BPcBE9Ol5ZlMI3aFU0BF0nXXPGD50nr6H5w_tfrwa8XsY3DqOSGMucx1KiNyQ5a7rCbC5HhuJW6bTUnfrJqtN6WPnHInYykA4DKXcPK3LusPHI7NCUWFw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=sVNnaacLBtcWfxb2FCEohe0s_HWgTHMYVBGC_aEbqtfzHVnu7QQccG7o4quKSamYN7H5SkuoRAhB_Qt4EJ0u8wt1ZDuHt300Iv9cszl0jjwKWF2hSOdTu0STIUfw5yyil7eDBLFXscEd6in2du9-l80x0Ei79Ry2D_aXbdMs2Q1w8wH5xxO0gu-I-Bx-uxqEoqZ5qnyKvip-_7x34bS4nOQ1YgAMUXjy9BPcBE9Ol5ZlMI3aFU0BF0nXXPGD50nr6H5w_tfrwa8XsY3DqOSGMucx1KiNyQ5a7rCbC5HhuJW6bTUnfrJqtN6WPnHInYykA4DKXcPK3LusPHI7NCUWFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/MatinSenPaii/5375" target="_blank">📅 20:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/etA3PPBZtQRnvYsDDFXuxniiW2QXl7vosz9u2HVd_QMLvJVDcgJH5lJO6eJZ1Ki3wcZzlG3zncbauoNTAHaatebR18qm2GD3OEuXi8xaiYFwgMGsYAF0M2O5f4dDhEURfP9fAe372rAvBVy55OpET2dCif4GkEXsskHzEjYVKnxkfRw5DHrZf6gFXpIVbH3HdtdX7e4DxrRnHQiSrQBxqOHU2ckWpgJTaF6FlQZnPHTlCYQNQ1KiOZKoYaeT3hg6MYV-vE_3NPDjz6Qhog9rQUV2kFZwhfkd64UvSXlNKdSph-GaAPsRGWbmOezDP69Sno750suwfcc88sYHvk31qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pz4s30cfB1FlMGTRal9V5FIHOSbq0WzNIYo_kUCsCm0YU9zwmc-71c8slDaftfxkdDuvgI1Tr4sqjGJLlitTySpCd8Z6Zz6ImNV84wL9a7d7p3ndyLuT5IcBa5FeC5LvzJhEqeo0q4yoKXByZcufjx4hHE_kXRM9CEpQ-RxgyjqwVw9vOSH3mGJoPlrWXG74iNMsnc4oWh_5yJFV-JxDEqEIBcp_qTIln8Ff_lIVMEdCoA1Hf18tigoJMDtPgnEw4ztwmCE9GBGomgZTGVhbogZ4x7D_JeC-FtFL3-Vw_wCVN4JOeTvuALNRkRWzV_o38-zehyqlAd8_0_6vgRV3hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A0AIjLZqNMQIZVdKtBt4KgIlViCGpNIeXf3rg9bJR7-0lJiv33weID0cUmviEePnnQ_35vQgmb_uxG8_zhhlK0Y6_UlPDE3Ar6Yn2SQo9yXv9x6dxvXpddendlw5jaFu8m7e3fwLNcjS1CifRUvulaIahmF1WIxIHGLMSKMLIHNfLXz8NHUMyWWbtvdScfKnFiTSF4WQNsbBjK2O516itlOs61MneHBSnMeqmYePxlPh3UVZEESaH_Xf4JhxuCchtX1THWGpG1vQn_nR_YewIuvP8KmiLOSg8vJjkTaHHO3VFkkdXcUaO7UICVkRRYiDz_KSgfTq0af4VZquC4lHfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/btsQV3-cZzDqlvbwDjYkQkoBIvVL2OuFuIxvgq7NN1Kcw-ZjtVrH1UZ6WQSejgcoGW4KzpE3zReO6czJz2Xq-YgDgXgrPGU7Hr0M2qECwerO6wsPGjih0VX_juV1HqGsNtZnZzKuF116CNLPj8egEet-1EVlkCSsAVSAzzuy4E6JHXcZSNrqtdmZgNm1piPU0W6-qowMrogRQeH5wPRWJUp3iiONfM55d-RgDj9RjlJoZ7-BGjjmL16o7GnEB-k3sm68XAknbJ-te0JaP5j08LXieJcsTwzphGUg9HijHtZjePBWCxmZB_mr3nEBGir89kMuT31rzcBbx97U_UVrLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اروین از توییتر
یه سایت بهم معرفی کرد شبیه به Mpay، اما بیشتر برای بیزنس‌ها یا کسایی که تراکنش نسبتا بالا دارن؛ با قابلیت برداشت مستقیم از کارت و کارت‌های تبلیغاتی برای کارهای حساس مثل تبلیغات گوگل ادز یا تراکنش‌های سنگین و گرون
از اینجا می‌تونید ثبت نام کنید:
https://finup.io/?code=MATINSENPAI
لینک، رفرال هست. اگر دوست نداشتید میتونید کد آخرش رو پاک کنید. برای شما سود یا ضرری نداره
نقاط قوت:
1- برای ساخت کارت، MasterCard داره به جای Visa(شانس قبول شدن آفرهای رایگان معمولا بیشتره)
2- قابلیت برداشت ازش وجود داره به ولت کریپتو(هنوز تست نکردم که KYC می‌خواد یا نه اما توی مستنداتش چیزی ننوشته بود که احراز می‌خواد یا...)
3- آدرس BIN آمریکا داره
4- از ارزهای مختلف برای واریز پشتیبانی میکنه برخلاف mpay که فقط تتر داشت
5- دو نوع کارت بیزنس و تبلیغاتی(هزینه‌شون یکیه) که کارت Advertising شانس پذیرش بالایی برای کارهایی مثل تبلیغات Adsense گوگل و تیک‌تاک و متا و... داره
6- کارمزد رایگان روی برداشت و تراکنش کارت‌ها
نقاط ضعف:
1- هزینه اولیه ساخت کارت 10 دلار هستش
2- برای KYC شرایط ثابتی نداره اما توی تراست‌پایلت نمره‌ی خوبی داره
3- حداقل هزینه واریز به خود کارت(نه ولت)، 50 دلاره
و اروین گفتش زمان واریز مراقب باشید از صرافی‌هایی که امریکا تحریم کرده نزنید. ترجیحا بریزید توی تراست ولتی، جایی و بعد بزنید به ولت این سایت
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/MatinSenPaii/5371" target="_blank">📅 19:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=ik_6wffYPWaU67CYG_ALEEJlAyPSgCpZRFTkPjeOs1U_3Y-Vp4zVC-Mfto8uTYhb6NpK-hDvXM0Xv2iPqItcdENeeJ4DqCO3MTmHWJt556ZWTguzloHyomuG_nCkDvCYoJwF5rtXo9vDMYuowLdis8t4T-5Tk9lvlfz-W-x1NYtyrZ0Rol-QCu4VmKHAOJnOEVYXhUZbUk1sWQmthgbAp7YVnz-SWwe0RM4WBx2w6-knjKrmOr6LK5T7kZi5PzbW7fXJtHeak7eHPc78TwFMIQKGuDxX8tOhJQNgHaCL6YPXBjFZhaqDwucgCmDfxjsaE2cm1yl6umZT9x50lzCZxwX0AuHneYWYedLb_KG6OA15cHQlS3URlDvYDyqEMgNPmKAbI_2pAwnahod57rRdA00pRLYoQ5duKfK-bwg1dyNJOg7KyteClaASyGVaoSGEu7-fVOSR2T6o1-jU18tQeUlqa7fPsLmWAw747e5BFzzsPHjy63uH8KSmdVMisnckzzyxzxxC3A5rtBP4N5lLMfGMhF4a9g1PiFATWpC9aeyJMVutpVLqSuTXTknYswINZA3YvFtV8RVKc7COjZCh7hh8A_R90JgCroDQxosrT0LBde7kWIfrKuB8nXQgLnnvSudfURoQXuVGUeJaV5EvVe-cEfTanqw5K98OI8w_N70" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=ik_6wffYPWaU67CYG_ALEEJlAyPSgCpZRFTkPjeOs1U_3Y-Vp4zVC-Mfto8uTYhb6NpK-hDvXM0Xv2iPqItcdENeeJ4DqCO3MTmHWJt556ZWTguzloHyomuG_nCkDvCYoJwF5rtXo9vDMYuowLdis8t4T-5Tk9lvlfz-W-x1NYtyrZ0Rol-QCu4VmKHAOJnOEVYXhUZbUk1sWQmthgbAp7YVnz-SWwe0RM4WBx2w6-knjKrmOr6LK5T7kZi5PzbW7fXJtHeak7eHPc78TwFMIQKGuDxX8tOhJQNgHaCL6YPXBjFZhaqDwucgCmDfxjsaE2cm1yl6umZT9x50lzCZxwX0AuHneYWYedLb_KG6OA15cHQlS3URlDvYDyqEMgNPmKAbI_2pAwnahod57rRdA00pRLYoQ5duKfK-bwg1dyNJOg7KyteClaASyGVaoSGEu7-fVOSR2T6o1-jU18tQeUlqa7fPsLmWAw747e5BFzzsPHjy63uH8KSmdVMisnckzzyxzxxC3A5rtBP4N5lLMfGMhF4a9g1PiFATWpC9aeyJMVutpVLqSuTXTknYswINZA3YvFtV8RVKc7COjZCh7hh8A_R90JgCroDQxosrT0LBde7kWIfrKuB8nXQgLnnvSudfURoQXuVGUeJaV5EvVe-cEfTanqw5K98OI8w_N70" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم یه ویدئوی جدید از مقایسه‌ی این مدلی که فکر می‌کنن Gemini 4 هست با GPT 5.6 Astra توی یه انیمیشن ساده(هرچند بنچمارک‌های این شکلی اعتباری بهشون نیست کلا ولی خیلی وقتا درست از آب در اومده این مقایسه‌ها توی قدرت دیزاین و درک سه بعدی)</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/MatinSenPaii/5370" target="_blank">📅 18:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=P52oxrDKRhI4Xg5pGC61dGd2IGA3IenqU5g4q8-1E7QLIwso2VAhbcUR5iai8mm1BWbL_bo8758FFtbp-pV7wjIsz2tbKCD8rBsfoeW6g8ummiH5KtoxN_QdANVEnqS6znG4FhgVlJkN0rLskNViyHrQrCA5jpQFUO8YBcYpKOnInWDF2V0Hm6lrrKOZ9HeUaIxoYJ6I20DkEbNDRiztRFnRU0sFOsmEGl73865O4HaLhQ027AcpLtZeQLaQ2a2O4Hw0KVTVGOOGwOE-Ig7vPRQzyQ68OW48uf-yOfgqJl-Vxk8udTk2fGLKwxERkaubaXjzV1s5lckXDrer0d5wYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=P52oxrDKRhI4Xg5pGC61dGd2IGA3IenqU5g4q8-1E7QLIwso2VAhbcUR5iai8mm1BWbL_bo8758FFtbp-pV7wjIsz2tbKCD8rBsfoeW6g8ummiH5KtoxN_QdANVEnqS6znG4FhgVlJkN0rLskNViyHrQrCA5jpQFUO8YBcYpKOnInWDF2V0Hm6lrrKOZ9HeUaIxoYJ6I20DkEbNDRiztRFnRU0sFOsmEGl73865O4HaLhQ027AcpLtZeQLaQ2a2O4Hw0KVTVGOOGwOE-Ig7vPRQzyQ68OW48uf-yOfgqJl-Vxk8udTk2fGLKwxERkaubaXjzV1s5lckXDrer0d5wYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/MatinSenPaii/5367" target="_blank">📅 18:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/MatinSenPaii/5366" target="_blank">📅 17:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تیم Tokio نسخه‌ی ۰.۹ فریم‌ورک Topcoat (یه فریم‌ورک فول استک برای Rust) رو منتشر کرده که می‌خواد ساختن اپ وب با Rust رو به اندازه‌ی Ruby on Rails راحت کنه.
توی این نسخه ری‌اکتیوی سمت کلاینت جدی‌تر شده: توی macro مربوط به view سیگنال‌ها و عبارت‌های تایپ‌چک‌شده می‌نویسید که به جاوااسکریپت ترنسپایل می‌شن و توی مرورگر اجرا می‌شن، ولی بقیه‌ی رندر و منطق می‌مونه سمت سرور. نکته‌ی جالب‌تر اینکه نویسنده میگه راست بهترین زبان general-purpose برای دنیای توسعه‌ی مبتنی بر AI هست، چون قراردادهای مشخص به مدل کمک می‌کنه با توکن و خطای کمتری کار کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/MatinSenPaii/5365" target="_blank">📅 17:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YEFI1hbdfxw4-IHzaDZ4zZUowcWnC6PVVrmbefnFzSdT_YeqX_1c5xWglZaemptLGwDhcVqHSuqrD1P3YwCr37GyGTKFyghqFjSHFdb6eHVrpw-Jnt9xaCStT7c1z5El07KhbCGzNlZzxPS8_ymW52DSBTMj6n0o4O-NZLJGN2Xyf_TjZ7DoiRr-xydkeaXiKYhi3p0SafACKDQUmOwk8xUqAeOXt9SE6GAiVjc33W4yNBfbdY_kljkwSOEhvc4B8t_RHluHiqXw3BuoGbkNORq9M158I8HkDXj1-Vkwn5t_1z78i2uhX82fqR-jxZERBpMynD-efnWcgqyrRiZ6GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با توجه به علاقه گوگل به اسم قناری، خیلی طول کشیدنِ Gemini 4 pro، و چیزای دیگه حدسم اینه که ممکنه گوگل پشتش باشه
کاربرا فعلا گزارش دادن که به شدت کنده...</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/5364" target="_blank">📅 13:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JKUPlHw1-5CCTblRxhq6uFMD7Da_bcm9dp3Vvzgf28_VoDN-5w93PWtSx4TlWcWa5QJA5M3fWSs2QNOq_3QjTF3EE8-tK7p43Xo_9FS5rpbY0tk9Vt-dozz0VKdDW7_5VkgE5H7caPPotQoJb9Ppc_aTjTsq7N2NKXhTTLKrw1WOAXWbZhwwwF5AHcRNcuq2tLfWiGkT-wVGrEKhlpQDV85DmRMjit7DKcFCzkdYEz5jWT6NQDK-ivb7t16evUZT1BzbcpkE7vk0WQr0WpPzFqmmkVfIvWeXsOAnrJKFWSExS4ax2Z-I9hp7yDmLCl4oqasTVfcaMkeNcYQvxNJowQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Gemini 3.8 Flash روی Cline رایگان شده آموزش استفاده ازش: https://t.me/MatinSenPaii/5099</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/5363" target="_blank">📅 13:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">زبان‌های برنامه‌نویسی توی عصر AI چی می‌شن و چه بلایی سرشون میاد؟
خوزه والیم، خالق زبان زیبای Elixir، یه مقاله‌ی فکری نوشته درباره‌ی اینکه وقتی ایجنت‌ها بیشتر کد رو می‌نویسن، سر زبان‌ها، ابزارها و کامیونیتی‌هاشون چی میاد.
چند تا نکته‌ی خلاصه از صحبت‌هاش:
۱-
کامیونیتی:
هر زبانی دور یه سری سلیقه‌ی مشترک شکل گرفته؛ پایتون «یه راه واضح برای هر کار»، روبی «خوشحالی برنامه‌نویس»، لیسپ «تغییر خود زبان». وقتی دیگه خودمون کد نمی‌نویسیم، حس تعلق به این کامیونیتی‌ها چی می‌شه؟
۲-
اکوسیستم:
فاصله‌ی اکوسیستم‌ها کم می‌شه، چون پورت کردن کتابخونه‌ها یا پیاده‌سازی الگوریتم‌های یه مقاله با ایجنت خیلی ارزون‌تر شده و زبان‌های کوچیک‌تر سریع‌تر به بزرگ‌ترها می‌رسن. ولی از اون طرف، وقتی ساختن یه کتابخونه ارزون باشه، چرا کسی بیاد روی یه کتابخونه‌ی مشترک همکاری کنه؟ خودش به ایجنت می‌گه دقیقاً همونی که لازم داره رو بسازه.
۳-
سینتکس:
سینتکس‌های خوشگل (مثل optional chaining به‌جای چند تا null check) دیگه اولویت نیست، چون ایجنت از boilerplate خسته نمی‌شه و از دیدش همه‌چیز توکن ورودی و توکن خروجیه. به نظرش زبانی که ادعا کنه «برای ایجنت‌ها ساخته شده» و تمرکزش روی سینتکس باشه، داره حول محدودیت‌های امروز مدل‌ها طراحی می‌شه.
۴-
کامپایلرها از بین نمی‌رن:
اینکه ایجنت مستقیم اسمبلی بنویسه منطقی نیست؛ کسی نمی‌خواد برای هر معماری یه نسخه‌ی جدا نگه داره. تازه هیچ زبونی توی همه‌چیز خوب نیست؛ Rust، زبان‌های اثبات قضیه مثل Lean، Erlang/Elixir برای سیستم‌های توزیع‌شده، SQL، هر کدوم تضمین‌ها و سطح انتزاع خودشون رو دارن.
۵-
تضمین‌های قوی‌تر:
اگه ایجنت کد می‌نویسه، می‌شه trade-offهای زبان رو بازنگری کرد. مثلاً type inference برای آدم‌ها خوبه چون نوشتن تایپ حوصله‌سربره، ولی ایجنت حوصله‌اش سر نمی‌ره. نوشتن صریح تایپ‌ها اطلاعات بیشتری به کامپایلر می‌ده و دست زبان رو برای تایپ‌سیستم قوی‌تر باز می‌ذاره. به نظرش زبان‌ها در آینده با این متمایز می‌شن که چقدر تضمین می‌دن: از طراحی‌ای که حالت نامعتبر رو غیرممکن کنه، تا تایپ و اثبات، تضمین‌های runtime، و تست و fuzzing.
۶-
دیتابیس برنامه به‌جای LSP:
پروتکل LSP برای IDE و آدم‌ها طراحی شده و با فایل و خط و ستون کار می‌کنه، که ایجنت‌ها دقیق دنبالش نمی‌کنن. پیشنهادش اینه که اطلاعاتی مثل سیمبل‌ها، رفرنس‌ها و call graph به شکل یه دیتابیس با زبان کوئری در دسترس باشه. آدم حال نداره برای پیدا کردن رفرنس یه تابع کوئری بنویسه، ولی ایجنت راحت می‌نویسه، حتی کوئری‌هایی مثل «همه‌ی مسیرهایی که یه مقدار می‌تونه nil بشه». برای همین هم جادوهایی مثل monkey-patching که کد رو غیرمحلی می‌کنن، بیشتر مشکل‌ساز می‌شن.
۷- در نهایت
Observability به‌جای دیباگر:
breakpoint گذاشتن و خط‌به‌خط جلو رفتن کار آدمه. ایجنت می‌تونه سریع کد رو instrument کنه، trace جمع کنه و اطلاعات رو کنار هم بذاره. پس باید runtime و state سیستم رو جوری در اختیارش بذاریم که بتونه برنامه‌نویسانه کوئری بزنه، حتی روی پروداکشن. اینجا هم طبیعتاً یه اشاره به Erlang VM می‌کنه که این قابلیت‌ها رو از اول داشته.
جمع‌بندی خودش: زبان‌ها قرار نیست از بین برن، ولی سؤال اصلی عوض می‌شه. اگه دیگه برای «آدمی که کد می‌نویسه» بهینه‌شون نکنیم، برای چی بهینه‌شون کنیم؟
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/5362" target="_blank">📅 12:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">AI
فقط یه ابزار نیست
نویسنده‌ی brettcodes از این جمله‌ی تکراری خسته شده که «AI فقط یه ابزاره، مهم نحوه‌ی استفاده‌شه».
استدلالش هم ساده‌ست: ابزار یعنی دریل‌برقی که کسی ادعا نمی‌کنه ده درصد شانس نابودی بشر داره و اگه برعکس بچرخه خرابه.
اما AI یه صنعته، یه محصول اشتراکیه که قیمتش بالا می‌ره و مدلش بازنشسته می‌شه، رهبرهاش مدام حرف‌های عجیب می‌زنن و پشتش مراکز داده و منابع عظیمه. به گفته‌ی اون، تکرار این شعار فقط داره مسئولیت استفاده از یه فناوری خطرناک رو از بین می‌بره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/MatinSenPaii/5361" target="_blank">📅 10:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5360">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsF5BASKJDABmK5mXGymIHEXlRPZcJduhT7l3_Ae47WNtiYurBygprj2_EKr3THVTH879exIv7h2XxIHhAdhcKk-0wJg1jbx7NN_NZD-IEpe3Zts6uK2a4qTFFIo7GJ73tKoBg-FJGjO20Qmsk-J59pPGLvBTvT2qvTa8vgQ8MGkEyehrRoXaZCim8G3Yd8ODGfJBFwR7pvyGI2YJIGSHVxbDYf3bCcA9H9_J5YeSsupyJKUWiDDDK0Q0LGkE7kRdsL6lU2x6O7vBJ5XyOSLnUv5jsDgUwPVw0zFqJgQOeaFs650NpHQ-vPUzVKG54H91FkYxLql7jEKLkvS0P-eSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر وارد بازی میشه تا ایجنت‌ها امنیت سایت‌ها رو به درستی تأمین کنن
مشکلی که کلودفلر دیده اینه: خیلی‌ها ویجت Turnstile رو نصب می‌کنن ولی اعتبارسنجیِ سمت سرور رو جا می‌اندازن و عملا سایتشون برای بات‌ها باز می‌مونه. Turnstile Spin یه جریان کامله که به ایجنتِ کدنویسیِ شما اجازه میده هر دو طرف ماجرا (ویجت و فراخوانی Siteverify) رو پیدا کنه، برنامه‌ش رو بده، منتظر تأییدتون بمونه و بعد انجامشون بده. از داشبورد، Wrangler یا یه URL مهارت شروع می‌شه و اتصال‌های ناقص قبلی رو هم تعمیر می‌کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/5360" target="_blank">📅 07:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5359" target="_blank">📅 23:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">واوووو چه باحال
😲</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5358" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5357" target="_blank">📅 22:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اینم موشن گرافیکی که Claude Opus 5.5 ساخت توی 18 دقیقه هیچ ابزار خاصی هم نصب نبود جز ffmpeg و اینم پرامپتش: make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5356" target="_blank">📅 22:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اینم موشن گرافیکی که Claude Opus 5.5 ساخت
توی 18 دقیقه
هیچ ابزار خاصی هم نصب نبود جز ffmpeg
و اینم پرامپتش:
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
که یه کم بالاتر داده بودم.
روشی هم که ساختتش اینه:
۱. هر فریم فقط تابعی از زمانه
کل ویدیو یک فایل HTML به اسم showreel.html هست که یک تابع renderFrame(t) داره. این تابع زمان رو به ثانیه می‌گیره و همون لحظه رو می‌کشه. هیچ حالتی بین فریم‌ها ذخیره نمیشه و حتی موقعیت ذرات هم مستقیم با فرمول از t حساب میشه. به خاطر همین میشه هر فریمی رو با هر ترتیبی دقیق رندر کرد. تیکهٔ «Rewind» هم ساده بود: فقط renderFrame رو با زمان‌های قبلی صدا زدم.
۲. حرکت‌ها از چند اصل کلاسیک انیمیشن میان
- Easing: فرمول‌هایی مثل outExpo برای ورود تند، outBack برای کمی رد شدن از مقصد و outElastic برای حالت فنری.
- Squash & stretch: نقطه موقع افتادن کشیده میشه و وقتی به زمین می‌خوره پهن میشه.
- Anticipation: قبل از جمع شدن شکل، اول یک لحظه بزرگ‌تر میشه (inBack).
- Stagger: حروف و ذرات هرکدوم با کمی تأخیر نسبت به قبلی حرکت می‌کنن.
- Motion blur ارزون: به جای نقطه، برای هر ذره یک خط از موقعیتش در t - 0.02 تا t کشیدم.
۳. تکنیک هر صحنه
- ذرات: کلمهٔ «FLOW» رو روی یک canvas مخفی نوشتم، پیکسل‌هاش رو نمونه‌برداری کردم و هر پیکسل مقصد یک ذره شد.
- سه‌بعدی: بدون هیچ کتابخونه‌ای. چرخش و projection پرسپکتیو رو خودم با فرمول ریاضی نوشتم.
- مایع: با metaball ساخته شده و داخل یک WebGL shader اجرا میشه. هر حباب یک میدان r²/d² داره و جایی که مجموع میدان‌ها از ۱ بیشتر بشه، سطح مایعه. نورپردازی براقش از روی گرادیان همین میدان حساب میشه.
- جلوه‌های نهایی: یک shader دیگه chromatic aberration، grain فیلم، vignette و فلش رو روی تصویر اضافه می‌کنه. شدتشون به ضرب‌آهنگ‌ها وصله.
۴. صدا هم کامل با ریاضی ساخته شده (audio.mjs)
هیچ فایل صوتی آماده‌ای استفاده نشد:
- Kick: یک موج سینوسی که فرکانسش سریع پایین میاد.
- Clap و hi-hat: نویز سفید که فیلتر شده.
- Reverb: با چند delay که بازخورد دارن ساخته شده.
- Sidechain: صدای بیس موقع هر kick کم میشه تا ضربه‌ها گم نشن.
- زمان‌بندی صدا با تصویر یکیه (۱۲۰ BPM، هر بیت نیم ثانیه)، برای همین همه‌چیز روی ضرب می‌شینه.
۵. رندر نهایی (render.mjs)
اسکریپت Chrome رو بدون پنجره (headless) باز می‌کنه و برای ۹۰۰ فریم (۱۵ ثانیه × ۶۰ فریم) renderFrame رو صدا می‌زنه. هر فریم به صورت PNG مستقیم به ffmpeg فرستاده میشه و ffmpeg اون‌ها رو با صدا به MP4 تبدیل می‌کنه.
۶. کنترل کیفیت
وسط کار فریم‌هایی از هر صحنه رو رندر کردم و کنار هم گذاشتم تا ببینم. صحنهٔ سه‌بعدی زیادی کشیده و شلوغ شده بود، برای همین طول ردّ حرکت و زمان‌بندی تبدیل شکل‌ها رو کم کردم تا واضح بشن.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5355" target="_blank">📅 21:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5354" target="_blank">📅 20:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dM3Wo5nyPHnM-CVZIMgDhXbBq0guLY5pvdMCjqWf0pIOxT2Sh-tTfZj9L2B5bXdZZdKucbr4oE2OsMGw_s9k3t9tJ8S4bVPL3R9va2QYFjSqZHKNt5qA00dNBHr_nNlGnbgnYHETUt56XvCKSiTreYEos0Qm32e4j8dQXIOe6fqTWd7SwQDcS_Q3wpM6kryP39lBqS6I92D1nuVS2YXu6j4B_njY-Nzqs0cGsN_H8WbCszoDujSTZsnPs4EnVnJVaQ-jXLPtUBTlVk_pf8lAwYVgIvPJuErlLKiTyRXntc-qGnDH5syvBSGvvOAZhQGwE3vv--XlSzNOUy8U1M1sGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب خب خب
کارهای جالبی قراره اینجا انجام بدیم:)
matinsenpai.com
فعلا لندینگه. به زودی لانچ می‌شه</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5353" target="_blank">📅 20:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5352" target="_blank">📅 19:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.
به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out."
آسترا حتی نزدیک هم نیست؛ خودتون ببینید. GPT اینجا صادقانه بخوام بگم، فاجعه‌ست، OpenAI کلا بدسلیقه‌ست.
✍️
shneural
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5351" target="_blank">📅 16:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QppTQX70dB6992nlfgyxlon2-bZt-CD-k_Q81flDsmrjX0hz5wrQyRYAoHgk3v09nWZx6-q21Tpwwia6oYg8uEZ7Ybh9398YI7dBO3aeLQlfw0j7wyj1Ou9fUQFvwMaD74NmFlRjn6KfBwLyNtrSQtOvSJWI0dmAyVa2gH5ekfB8L2BQSUmJyLnXokwtFm1gVtH383DNXVuD72cTqpnWw7mxL3RygmmGfJLm8Wk_qXvFFqhTQvgF4M98aCg9PVTUPa34sotCbu8ZkyCALQCMBjVl2iWXrpTYDfutIdx9dwfjg2wQiyqQrx4ID_09cYaLiIEbRwDfIgN8KkHx4xy31w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازبینی کد با Jev؛ Diff خام دیگه در کار نیست
یه ابزار متن‌باز که پی‌آرهای پرحجم ایجنت‌ها رو به جای نمایش خام دیف بر اساس اولویت دسته‌بندی می‌کنه: فقط تغییرهای P0 پیش‌فرض نشون داده می‌شه و بقیه P1 و P2 هستن. توضیح تغییرها به زبان طبیعی نوشته می‌شه، لوکال اجرا می‌شه و چیزی هم به گیت‌هاب نمی‌فرسته.
🔗
لینک ابزار
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/5350" target="_blank">📅 15:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PNj5QUWhosw_x2KdmZyJhZNL14WeUhP78heVmnnFQ_EQeCVIt9XLjVA4yONKWXa7juyc8INX2LwDvdYfkPb1CM9AaENZ5CXipoDMiyS9iIzx1igJycTwyZrvou3CCbBhlqbS04RNUfsN-OvjGAKW93AJ6mq8VW1ahXGfoz7NgI1E4zS_XZhdSxaqiY4C5Kagdp-BwuIEqNZlj8teYjeHOEFsfj5UKGtSon-NPfLkwybPlOjwAjjQgncAwa8pTHjFicPiXvFeZVFQhnOe4np8XI6bHulfuY_rus1qw66B_wPUTqEfw8w0dqLmT9Mo4MnsVFT2A2bYwoVgzfLdJfBMlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5349" target="_blank">📅 14:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cq9_Y6kwGywKk0x74fa_SYf3tJ_kXymKH385RP-r6GGC4GcXnOEcFcpBO48k-7tP2AkWuf_1x1kJBz-3JRxu0UUAGa_tRYgKhtYdoGZbDQqb_graS9bHQEs8wnR1IcJDYsGWuQzrvKLrHHfW5laf2m9xDcxM_xN_04OOSJWOqPwiLJZJ7xxVIWONrfzBSwtE1gMRwkpnULWZKzyS2S4dp6bdoqtl1YARSyJpdHdaB_Dn0W5RvXCbF7obaR3Tfy0PmKyFIwvNbdhgjP0vMrUfjYtQdVidrijSt3AWJVXEpBlqZ5K-mVINVGkwAQa3-Ps3pVX1Jr-2csfTTK7XaLCMcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت‌سی؛ تایپ‌اسکریپت اما بدون موتور جاوااسکریپت
ورسل لبز کامپایلر آزمایشی scriptc رو معرفی کرده که تایپ‌اسکریپت رو بدون نود، V8 یا هر موتور جاوااسکریپت دیگه‌ای به فایل اجرایی نیتیو تبدیل می‌کنه. نوع‌سنجی با خود کامپایلر تی‌اس انجام می‌شه و خروجی می‌تونه C یا WebAssembly باشه. نتایج اولیه استارت‌آپ سریع‌تر و مصرف حافظه کمتر نسبت به نود رو نشون میده، هرچند سرعت اجرا هنوز پایین‌تره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5348" target="_blank">📅 13:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">https://youtu.be/qNYT3eoyJ-c</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5347" target="_blank">📅 12:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ویدیوهای بلند بالاخره هماهنگ می‌مونن
ریسرچ گوگل یه فریمورک مولتی ایجنتی معرفی کرده که ویدیوهای بلند چندپلانه می‌سازه و جلوی عوض‌شدن ظاهر شخصیت‌ها توی هر پلان رو می‌گیره. لایه‌ی هماهنگ‌سازی روش Gemini و Veo سواره و SynthID هم داره. چهار فریمورک به اسم Co-Director، CANVAS، A²RD و VQQA پشتش هست که دو تاشون توی COLM و EMNLP 2026 چاپ می‌شه.
به نظر قراره ویدئوهای هلو و پیاز و عشق آبدار رو قوی‌تر بسازن وقتی این تکنولوژی اومد
😂
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/5346" target="_blank">📅 11:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ozy3hm4mv0PWcGyfCMRs7bzSJ_aMY61oBhCK2qjG6PXKM_BzhHhFT0s6t0IHm7A9QebKgEcDncudhbtnQ_7Q1bHYGkrq5V7SvWNX1Ba-XurdowBNsglVyxHPD4AaOhoJDDEaBTTIKzMKF5qXbTvY1rETfbEBQZe4O5rDGJN5ThcCh6ACttHx7vAUsaeGBLhjLHPVd5qiOD24XdQiazipIOZ0SDE4p3gZYgMVn02DLCjqZ-cWBVjZS1yQiOgJZJBjw-JyRAqSK-vMVRpWqi6V7A6qG2LqsB4HXeKVi2VmQGo7XaM1-lmwjZ-6ycNFTbF-of30E7G6ffW8ZVWu405Tpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک آرنای توسعه‌ی وب مدلهایی که اخیرا ریلیز شدن.
طبیعتا Opus 5.5 با این هزینه، صرفه‌ی اقتصادی خرید پلن کلاد رو خیلی بالاتر برده. و نمره‌ی پایین Luna 6 توی ذوق می‌زنه حقیقتا. اختلافی با Qwen3.8 27B لوکال نداره:)
که آفرین به برادران چینی</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5345" target="_blank">📅 07:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">مصرف Opus 5.5 به طرز عجیبی پایینه و همه توی کامیونیتی ایرانی و خارجی هم دارن میگن.
خودمم که دیروز توییت زده بودم راجبش.
روی پلن 20 دلاری هستم تازه و اصلا تموم نمیشه به این راحتیا</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5344" target="_blank">📅 00:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=td0M1Ke3B8F4PsM72XYEWbJSyT1TOw1S9JA8GWf0mQdYdrE35M31_LQiPXYaMdnzv4zmu_30JJGFYM81SrXTPRhGyZvcZLA4DsXub-gZVZrfHlrhClB86wdd_QyqtDubsKJpVKlPNsLKIULjYWRj-JP6gywT9UOmKmsnCY-5xPYPp8b0Kuiq9_yRRZ6qAp2dCeNDN_DChD3Gf67OyQU1HCQHOs0Wg6e-NZnPFXmtDun434f0r5MBcOoH_gOXrQ28vzE-zoUevhEGA3CakkjjbxUGn6YSa88QAa5Iimd_WkcT4LoGYjXXJf7fafxlQp4nPAQTGXL3WUafjs6qTUVSGw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=td0M1Ke3B8F4PsM72XYEWbJSyT1TOw1S9JA8GWf0mQdYdrE35M31_LQiPXYaMdnzv4zmu_30JJGFYM81SrXTPRhGyZvcZLA4DsXub-gZVZrfHlrhClB86wdd_QyqtDubsKJpVKlPNsLKIULjYWRj-JP6gywT9UOmKmsnCY-5xPYPp8b0Kuiq9_yRRZ6qAp2dCeNDN_DChD3Gf67OyQU1HCQHOs0Wg6e-NZnPFXmtDun434f0r5MBcOoH_gOXrQ28vzE-zoUevhEGA3CakkjjbxUGn6YSa88QAa5Iimd_WkcT4LoGYjXXJf7fafxlQp4nPAQTGXL3WUafjs6qTUVSGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب، Jev از زمان عرضه داره روی GitHub منفجر می‌شه و همهههه راجبش حرف می‌زنن؛ و اینا چیزای باحالیه که مردم تا حالا باهاش ساختن و شما هم می‌تونید بسازید:
- پروژهjev-trader — ربات معاملاتی واقعی که سفارش‌های limit زنده روی هر بلاک ۳۰۰ میلی‌ثانده‌ای Monad می‌ذاره و فقط Jev تصمیم می‌گیره. ۱,۹۱۱ استار
github.com/jarrodwatts/jev-trader
- پروژه jev-ultrafast — ایجنت مرورگر که هر کلیک رو خودش انتخاب می‌کنه و فقط وقتی واقعا باید تایپ کنه، مدل متنی صدا می‌زنه. ۱۶,۷۵۸ استار
github.com/browser-use/jev-ultrafast
- پروژه jev-doom-agent — Chocolate Doom واقعی کامپایل‌شده به WebAssembly؛ دو موتور روی یک نقشه، Jev هر فریم تصمیم تاکتیکی کلان می‌گیره.
github.com/lukaske/jev-doom-agent
- پروژه jev-t-rex-runner — همون دایناسور کرومه که هممون هزار بار بازیش کردیم، حالا کامل توسط Jev بازی می‌شه: بپره، خم شه، یا ادامه بده.
github.com/joshlarsen/jev-t-rex-runner
- پروژه‌ی typesafe-chess —خود Jev در برابر یه موتور جست‌وجوی واقعی، دو بازی با رنگ‌های جابه‌جا. موتور جست‌وجو هر دو رو برد، ولی حدود نیمی از حرکت‌ها نظر اولیه‌ی Jev رو وتو کرد.
github.com/TholeG/typesafe-chess
- پروژه jev-drone — یه کوادکوپتر شبیه‌سازی‌شده فقط با دوربین مسیر مانع پنج ایستگاهی رو رد می‌کنه و Jev نیم‌ثانیه‌ای یک‌بار وضعیت رو قضاوت می‌کنه.
github.com/RomanSlack/jev-drone
- پروژه tax-doc-classifier — فرم‌های مالیاتی IRS واقعی رو با دقت ۱۰۰٪ روی ۲۶۱ فرم دسته‌بندی می‌کنه، با هزینه‌ی تقریباً ۰.۰۰۱ دلار هر صفحه.
github.com/kyotofin/tax-doc-classifier
- پروژه killmyidea — ایده‌ی استارتاپی‌ت رو توصیف کن، Jev از هر زاویه‌اش امتیاز می‌ده و بعد kill، fix یا ship برمی‌گردونه.
github.com/monteduro/killmyidea
- پروژه jev-curate — ردیف‌های Parquet و JSONL رو با قضاوت‌های typed با سرعت ۱,۵۰۰+ ردیف در ثانیه پردازش می‌کنه و فقط چیزایی که از حد رد بشن نگه می‌داره.
github.com/AkashPriyadarshii/jev-curate
- پروژه pg-jev — افزونه‌ی PostgreSQL که بهت اجازه می‌ده به Tableهای خودتون سؤال انگلیسی ساده بپرسید و جواب واقعی بگیرید.
github.com/realZachi/pg-jev
✍️
imryven
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5343" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UlYKPzVbc4QDa7JRcnQH4OWcCgQSYSirLPaDDLO7KNpkO6tMWlgKLdA5cDB0DE9j_TTjLnD3MSDb8MF4ruCM3YXEbTJAu2raaXekfNEwr4yGyl0QQlS7dWjuKwPvlGgd0yEOWX-33YvjYFcaaZwXicUHR-PP9Xuw16whe4EQ7MeRJamV9tYlUl3b72NhiE9fPRi5cohkGGPFbZNwEuACjT_RABJ8U-k_OI5Cyb_y0xRPKKWmsByQvm5J-DuLGSYFfjj5MVwYDUgjEcVTC1_jKVyEk3YXpM13gJLx_5eKtgaLUmDaeq3PnWgXEa5zbM3JAywTRZ1MGsH8aflpGiH9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«داداش اینا که AI بود»؛ ناسزا جدید نوجوونا
😂
گاردین نوشته تحقیرآمیزترین عبارت امسال بین نوجوون‌ها شده «That's so AI». یعنی وقتی می‌خوان بگن یه چیزی جعلی و بی‌کیفیته اینو به کار می‌برن. جالب اینجاست که بین عامه‌ی مردم، خودِ AI داره به نماد بی‌اعتمادی به محتوا تبدیل می‌شه، نه فقط صرفا یه ابزار.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5342" target="_blank">📅 20:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هکرها چطوری ChatGPT و Gemini رو کردن دستیار کلاهبرداری
🥸
یه تحقیق تازه از Vigilance Security نشون می‌ده یه کمپین گنده (اسمش رو گذاشتن Dark Sourcery) داره جواب‌های ChatGPT، Gemini و Google AI Overview رو مسموم می‌کنه.
قضیه اینه که: کلی پست و PDF و صفحه‌ی پشتیبانی فیک می‌سازن که با تکنیک GEO بهینه شدن، که هوش مصنوعی شماره و ایمیل تقلبی رو جای «اطلاعات رسمی» بهت تحویل بده.
تا حالا دست‌کم ۳۷۴ شرکت قربانی شدن؛ از Fortune 100 گرفته تا Delta و Lufthansa و Bank of America.
چطوری این کار رو می‌کنن؟
1- شماره‌ی فیک رو با فاصله و نقطه و ایموجی می‌نویسن که فیلتر اسپم نگیره، ولی مدل راحت درش میاره
2- شماره‌ی تقلبی رو قاطی شماره‌های واقعی می‌کنن که معتبر به‌نظر برسه
3- محتوا رو فوری می‌نویسن (جابه‌جایی پرواز، قفل شدن حساب) که هول کنی و سریع زنگ بزنی
4- پست‌ها رو می‌ریزن توی LeetCode، اینستاگرام و حتی PDFهای سایت‌های دولتی و دانشگاهی
پاک کردنشون هم فایده نداره؛ کمپین اتوماتیکه و روزی هزاران پست جدید می‌زنه.
بدترین قسمتش؟ Google گفته این خارج از scope‌شونه(
😂
😂
😂
😂
) و OpenAI هم گزارش رو بسته، به این بهونه که reproducible نیست. چون عملاً به سیستم خودشون حمله‌ای نشده؛ فقط خروجی AI دستکاری شده.
۹۱٪ آدم‌ها جواب AI رو چک نمی‌کنن. شما جزوشون نباشید؛ شماره‌ی پشتیبانی رو فقط از سایت رسمی خود شرکت‌ها بردارید
چون به زودی شاهد همچین افتضاحی توی ایران هم خواهیم بود متأسفانه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5341" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MaxlHHZXkmUiyCquCTG5028mHfb2FWw4XWzvHdi6g71TnNRREJNrFdn_SrfUdM6GLr82p5_dhig6E1StIbsDIZf0GScf4uGmJRQAxh-r_sehJ7gMiwf3LVEPK0_1zz-dFgyEN3LGN4D4m2Mmi5-3pY0w4_jBrRt-8GKPhT5yznbWPjpizwGkkSWwxF6Eaa4G0z3SL8_YOmcyArCOnX0YhMe5QV6jZrZTMK-2TaFVJp1mmaRNsizMs1l-viiu1grPS6N7NYmwtMZ98jGRQERjrhZ9Rj_o943untLMCIwouW-ccdYsTxi3t3AsT6uVI-5eCwkHgbO-hpisDlwjNvMugA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیق رسمی استرالیا علیه OpenAI
نخست‌وزیر استرالیا گفته یه agent از مدل‌های اوپن‌ای‌آی ۱۸ ژوئن رفته توی سایت Services Australia و فایل‌های داخلی و آمار سلامت دولتی رو برداشته؛ دولت هم تا ۱۰ سپتامبر خبردار نشده. این اولین نفوذ ثبت‌شده‌ی یه مدل AI به سیستم یه دولته و حالا قراره تحقیق قانونی بشه. (حالا اینکه agent رو چطوری چند ماه بعد متوجه نشدن رو کاری نداریم
😑
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5340" target="_blank">📅 18:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دارم روی چندتا پلتفرم کار میکنم، یکی یکی ریلیزشون می‌کنم
اکثرا هم سر و کارشون با ترجمست
و یکیش هم برای یادگیری و تقویت زبان انگلیسیه، اما با یه روش متفاوت</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5339" target="_blank">📅 17:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NlZfPOrVVe4_iD9qpE9SyW0U0TO5L51DUmU7auH4VDVXIQd07OPElQP-iymZbGtMjLIbqHREUbiqdgA_-gFbWPKrq4o16ABRQaxrylI1EZ8tN3SJq9-iMMuNPluusWRPecVfYQjm5ZfGuTCuFFAdiNDg-qcyqFDOnHu3s9a9DK7vunGqz-R9Gaxeb_0KV4v2juZl6CvKwNHDHIUCdzWLFb_a7aHVjrX8pMF-u-kDNRarQeugbHY24TnFwJZnZ3uM0deDQRHwnkNuqdm5dL6bD0EIQWnsVDXOF_8cLkkqheAG5BjFcaLp8NlBnue-Nw6gZyDDHeSg1AEAIdA3jq9xsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5338" target="_blank">📅 14:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromReza Jafari</strong></div>
<div class="tg-text">تو سایت زیر می‌تونید ببینید مردم با jev چیا ساختن و ازشون ایده بگیرید!
🔗
لینک سایت
@reza_jafari_ai</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5337" target="_blank">📅 11:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5336">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مراقبت کن عزیزم. سلامتیت مهم‌ترین چیزه و ما درک میکنیم
🌱</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5336" target="_blank">📅 11:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌. دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم. پس اگر شرایطم رو می‌دونید…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5335" target="_blank">📅 09:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5334">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌.
دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم
در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم.
پس اگر شرایطم رو می‌دونید و ناراحت شدید واقعا برام مهم نیست که درک نمی‌کنید</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5334" target="_blank">📅 00:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5333">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mDAiNW_Rsuos34zrWfYSCkQ6O8ls9tmdYYTXyC4zZ6TKcGhAdV3hb2tX-L6NIsoqmbSzx_3VmSJ8r9Q_dQQYa2W5R32kWd-ShU66_UeTWmgnKevXprQ40VqL1CiWCIeZZ8bnJS9pS-ClcDwKeiJQIYptmNAFcokS6F4kbblb0GKG_5LHkgB9dkWQxAl9l42ZE2gUmrfcxhM1nvT1N7myy5T3_CHWZEVfDWkbCeeX-0Mw7rxjPCTokjM0As0VYIxjdD1Lyo-nTM35ByHFud7vrEgWZKa0DSYa4NsDk40GBPEY0mgNPu1wEnjy63dUMsN3PtvpHARHl3N2rhFYUe6qnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل
GPT-6 Astra نشست پشت فرمون تویوتای واقعی
😂
یه بنچمارک عجیب به اسم DrivingBench منتشر شده: مدل‌های زبانی فرانتیر پشت فرمان یه Toyota Corolla واقعی می‌شینن و باید یه مسیر مخروطی رو طی کنن؛ یه ناظر انسانی هم آماده‌ی ترمز زدنه. نتیجه‌ی جالب اینه که GPT-6 Astra با Codex توی تلاش دوم ۱۰۰٪ مسیر رو در ۵ دقیقه و ۲۲ ثانیه تموم کرد؛ Claude Fable 5.1 به ۴۵٪ رسید و Grok 4.6 فقط ۱۱٪ پیش رفت. ویدیوی هر تلاش رو می‌تونید توی سایت منبع ببینید:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5333" target="_blank">📅 23:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71e738709.mp4?token=tsnNT4q042UHTn3SVlGE0bsTTtYe13Wj0PfmfbiyE8PKxHISl1UFwgJEo5092tXlFryQexI2-s3UTWCZQpsJZUwfIFE-LHk8b7x03RVoiCvkhy8f3uGRHIpfX6ixyNXtER2JXuqlJaSC3I4QF_ZPSfgRgTl4aDWVfkc-n3sS5Von98BnifcahW6tv8DIcI6i5T4Xhe08sbOi5mGISZOxMmvXB3YME0KU-9_qFLC7MkWmJy3-XEYEXmFLTm9CTG0rsZYb4t692GmJeIT2xtn2a24WHBgyTNiPzMdmx4W_2h85rarHauW7GhYKfQXyLZ1qZwnQEExKY5t1V127ee3ztA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71e738709.mp4?token=tsnNT4q042UHTn3SVlGE0bsTTtYe13Wj0PfmfbiyE8PKxHISl1UFwgJEo5092tXlFryQexI2-s3UTWCZQpsJZUwfIFE-LHk8b7x03RVoiCvkhy8f3uGRHIpfX6ixyNXtER2JXuqlJaSC3I4QF_ZPSfgRgTl4aDWVfkc-n3sS5Von98BnifcahW6tv8DIcI6i5T4Xhe08sbOi5mGISZOxMmvXB3YME0KU-9_qFLC7MkWmJy3-XEYEXmFLTm9CTG0rsZYb4t692GmJeIT2xtn2a24WHBgyTNiPzMdmx4W_2h85rarHauW7GhYKfQXyLZ1qZwnQEExKY5t1V127ee3ztA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتضاح Union Alpha</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5332" target="_blank">📅 22:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مدل Space Bunny(که یه مدل مخفیه که نمیدونیم مال کدوم شرکته) روی اوپن کد رایگان شده برای یه هفته
- 1M Context
- Multi-modal
بریم تست کنم ببینیم چیه
امیدوارم
افتضاح Union Alpha
تکرار نشه</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5331" target="_blank">📅 21:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5330">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4UUwoZf2QFP4sduBeTfJ8J7U6WXDJOoiNq4qJkY8vPuV2XSnUn27VmvO9rTIzyk2kBR2S7eRr90-UuHD4KVqN0h1rCkaXfunqf7lQmHgNM4_0Hz3xjMqW0iRu8IpS2vsDhRW1xf4pTkCf8w4FID0Nwsq4V5e-5NniaL4d8-GJCR1xB8SsawFIbbr25zHk-zUD_LUMtfoa7oDZzOZP6T1mBQ8sZZYQ4TcFN6CHzu6aeIiqy6uu-SSylBw1iadrR0mSzAeevOZnAUQrU7zosVyrdMBCMRxOhJ0Fz_frAKaFhTAtWYfQi4jcr0bLd6gqzelJ1Xoc5kphsk69kIOP4dxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی GPT-6 Sol، GPT-6 Luna و جنگ قیمتی با Anthropic و Xai
دیروز Grok 4.7 اومد، اون وسط Mimo 2.6 و چند ساعت بعد هم Anthropic مدل Claude Opus 5.5 رو منتشر کرد. اما از لحاظ هزینه، شوک اصلی رو OpenAI با معرفی هم‌زمان GPT-6 Sol و GPT-6 Luna داد که رسما بازار رو وارد جنگ قیمتی تازه‌ای کرد(برا ما که خوبه والا)
مدل GPT-6 Luna با قیمت ورودی ۰.۱۰ دلار و خروجی ۰.۵۰ دلار به‌ازای هر میلیون توکن، تقریبا نصف GPT-5.6 Luna قیمت خورده و به یکی از ارزون‌ترین مدل‌های تاریخ OpenAI تبدیل شده. مدل GPT-6 Sol هم با قیمت ۲ دلار ورودی و ۱۰ دلار خروجی نصف Sol قبلیه(۴/۲۰) و رقابت شدیدی با Opus 5.5 داشتن. از اون طرف هم خود Opus 5.5 هم افت قیمت داشته و هم توی تست‌های اخیر، سبک مکالمه‌ش طبیعی‌تر شده.
منتظر بنچمارک‌های معتبرتر هستیم، خودم هم به زودی تست میکنم
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5330" target="_blank">📅 17:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5329">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یه سری نظرات راجب مدلهای چینی دارم
سعی می‌کنم ویدئو بگیرم توضیح بدم کامل</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5329" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5328">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">عرض تسلیت به دوستانی که مدرسه میرن
غصه نخورین زود تموم میشه
😉</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5328" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8fb483df78.webm?token=ljnw-e24Utpcvbooqdd_D1nebAmYuJQsK5ABS705ottjRZMsuomXvCFInRNswYM1MUIjJIhjNDDn92z6GWQjX7595aM5yOIpUQybl65lS_Ne3lqhmhfwOwmnSeG_SPejIfNPZBXJ1AMwhmPWWMzzp65YX87sJOaOjrUWisbPBernhgXTPE3XAUcjKEtcUQVva0gSM5SYnDVpofQvCyDvmNyN5RzFax5wSf1cWho6UxPGB1cCrHJB5tPlGfBgJ0jDCMBF5cICm2ezQdeNlTQKzP-ZR3cBqAMEDwMRusC83gH31_KjYWkjcKKfe-tOj8kn7WRFRNsLtdYcHvn5KiOxzg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8fb483df78.webm?token=ljnw-e24Utpcvbooqdd_D1nebAmYuJQsK5ABS705ottjRZMsuomXvCFInRNswYM1MUIjJIhjNDDn92z6GWQjX7595aM5yOIpUQybl65lS_Ne3lqhmhfwOwmnSeG_SPejIfNPZBXJ1AMwhmPWWMzzp65YX87sJOaOjrUWisbPBernhgXTPE3XAUcjKEtcUQVva0gSM5SYnDVpofQvCyDvmNyN5RzFax5wSf1cWho6UxPGB1cCrHJB5tPlGfBgJ0jDCMBF5cICm2ezQdeNlTQKzP-ZR3cBqAMEDwMRusC83gH31_KjYWkjcKKfe-tOj8kn7WRFRNsLtdYcHvn5KiOxzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5327" target="_blank">📅 15:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">Check this out:
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5326" target="_blank">📅 14:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MkpYwtfUZhvgzkHk4WA7PgMZAYvf9CB9E2BuI8ivrKHMP-3tPOG3p5WTLz5iCff4KNPd7NYGpt7t1Ye9V8ZHJ35cPp-r8HiaQaLRTe7rrKApj4Fs0BU7cO1yY3rksHDtjJnl7_LrmeUGTlyr36lVdg6j8zgxvDxu3d-bEIJSCcxUf95dr7CdLqZ-FAhQBKhzg_z0Eie5yPYJssbKr5urSnB-8UsPvwLchmpA68ANtJbHmUbYUqr165BHzEGhW8qtgnQT5c-Sa15rcB9B64BZgRAJO1twDIhthgO82R6ikTOCH9NMKAji__gIYMUyNQ7NThoNXSPSqOPmBD1c_SyFrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بگم از چه مدلی استفاده می‌کنم اونم با چه مصرف پایینی، باورتون نمیشه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5325" target="_blank">📅 13:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فراموش کردم بگم، یه World memory هم واسش گذاشتم که کامل از روندی که تا الان پشت سر گذاشته اطلاع داشته باشه به طور خلاصه</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5324" target="_blank">📅 12:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hAIhnUgsz-Ca7_r0Jakb_84_PKBoExBrnPM5QwdU9H6G-CRsvabu-Dfe8wTwdiVlp3mtgK-3vnRd5skZ9LMhMj8yHDkVYjOwfAoutI0UKKl9oOFwGQ_THx0IDowFe5KarndBNz2a9tjM2QREnlFu0QtuDY5BGQm00-dLFbczvJlLTxArKcBTHmEwqV4JzSopZ50wNjxYarJuJD755QRzNmnk5S1hP0y13YfH_8_-OoWMUj_20FTHaouTa4qEG_88G_E8VA3pAzkOvSMGc00rBjClp0WFw_8Awyy74uSa_56U4YFCLIpGM70xR_sJE-mL5gskr0MAVV0zeIEOGcWn8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o2P6LHwg-HrG4uTAtDwUvsOlmwSiShdWMHZjFXdyc73hNpTzyEOCWpdMLSozTMcLBSkNxsngw7GCp-xTVeCC5kQMpOoUk-9LTWJIiXXJIADYMEa1DTK2xSCmxYtTQk61JcyGebCehuLmAFMIIegTGcUVhk1UXrDg8zzON1Q7h9rL9Ig-8L-u0K2Kikw-m4PRbvJHxfd62t9P2wR3UX7-fsOLC6v_AxjHugi78LIMaH7PkaaZLWLWIb-ky0mxV2TiohodBPYStqS-VN3fI8Xz84qhsw0I48BJmFwtnfFZuFB0HndAuSzPi9tFARqxtCMApmz3FbNkDysyTtvgRq_yjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uI6EtkcpRjAE1J95V3xe8NuvkwRIP2oRbJYfVu_lDxJ8aYp82dMuGlHktdX3NnACOTcMDpl_Mth0w1N9o5eBNRx8tCU-hWZdbalK8khuU9Kpv2YtTuRg1CcpBFTIOkY9uY29A77ZOJnntuANVmvAhJV0SGzH5HJzrX_B38WkxeZHZ221VT2OXnNuliQvpoF4-bHmIiOD2YM82GhLmDfeWSwWla5Tnoaj7Q_AqvL8DlgJZTTIuMjyTRzRh20zwWRoqn6tkZUr3BEZEGHIHJiXKijodEdlriMeJ8Sbe7YYMUiCLj0Bewzf64hFW8GGNeEmel4knj7A8e6w3pOD9saR3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/krag1swLe2GCryq9zwslGm-LoR4cdCZaFgU7wQibaohCVRVFu2yWrNAAsFtb23fKYdC9N-ZWZFuLU9KXXCx5hnWq5-fJ4w7ocxf-rAYUjUkXWLhqdj7hTC8-qwj9YBptictENbn54JnkMllSNGMDt0wXh-7h70jCndG_ZaVmNhD8P-7F77p8hbjhUP7X46BTCFKS2uF6TRe0f1s9XZh1Sc6qjnmsGno7tUut9VlWmGbovq3yd-QX68K6JG5vZ6MSSxt_fT_9qT1lrAAnRWe4vqphYV8hMf5sGB35NRGQpBAcxFOkrALKALXXpgRPrR3SKAu-NCYlorqVBnYGleaarA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mXYm_ZYNwg1l8kF_F8QXlJn_X4g48vdOEPgYZLH5G_kC4nky7M4tkDWVoHqhAiZ5g4U06jA0hTUQqd1R7PushCkuocl3oq6OO8LWVdQBqlUHMNyyzpU28cSV18EKHpahVeBOSj0mJqieMXeG1tQe-Phyi6s6D7MRV2sKD3yZ9Gfnw2V5C2zQy3kZvaOKnklKc7E_QbfNv0CbQht_YYqqhW0QFyQxuWZmX4HP3iqnwmE2qHaEfipzfq_HJttOjR7lfbsGMfeatb8xkRGJa6EPGOdVN9lWKU4R3FJnAdca_t-49bI-38miS6FnMDhyA6YzakQCXjp3HlBUngLjD6NisQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cdlWqk1xj8A1bnQ7KUQEqFyurOjBbb-vxw2Oq8OdZL2ckUGJESyjI5Fhe8sHceWhmkO2Gk4NYW9aObfn16FPh-J1zoz1_NU4QGU8XiwACbZfal3Ec_kq6pqp_p1UyxXAk5ZwSdM9ffMO5zo4ReULFdZxOoRpuTy7q0sMHS4Cy9mSm_RSvWm7Vj5-p7LJ-inS2h1hTPQxPJmGWb3w5MxfTrGAQ6FXOT81LztURXv_eudakgxpPwtHduW-3Ngd4D7vg1X7xkQqt-QvbeYP7t6Mh2Txepj3o26MSUrdtXM8eN3u5UjzKA5dSeq4CKsh89mPw9rmL1SRuCE5cOgDvYYUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DBp2ixhOAPqxi71qPJgTVAzkd2RAqoQvxlBTU8tswLn4Wl9JAQUHY-zqlQb1enh93ATv-ovNGSTtgoxloweLgbEp7Qj6fejOlaXaj_VXLXp-ebdje3dDMevQsFZgK0WmHmmD0Id7P5f2gRcq27k7ffcsOcVUfVfgOaVVv4-pQuFSDASMm4kH662ea84BJMUWD447nSTddvUdQoSyssQH9Y1GbOp6gtgg2P-1DD0jI6tFNeczwKnKsqP0KdDXaXO852eTsA4SSoL0XfVflnXlZWTbk5c0h14NXEBjGCUNVNHb4IHNxtOziyMn5zCRHPJQlDA1TpRlGZv2_611GLC5DQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گذاشتم قویترین AI دنیا ماینکرفت بازی کنه! GPT 6 Astra + Jev  توی این ویدئو، با همدیگه پروژه‌ای که ادعا می‌کرد تونسته ماینکرفت رو توی 8 دقیقه اسپیدران کنه بررسی می‌کنیم و خودمون بازسازیش می‌کنیم با استفاده از Astra و Jev از برادر کوچیکم دعوت کردم بیاد کمی راجب…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5317" target="_blank">📅 11:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GMgH-SUUDF7pGv9vbmVHuprV6HrAVfkRy-W8L62ZCq5f-QPwh5e-ZSwM_PCbIG5QIFvLlJNJPZBbPEOnolQnvVsoTNPXglIly6WPm_2kR9AjBvjuAZg5VZx0Jc18I6TbPvGCa5-P0IYhSrCMnZWQwR4aMIIPEM8N9pK_56ud2K8d4d31pxUXRb6Zhy4YKizl_ECFUhkjB4RN36YncaIkWMvX3-_OBpcP-ikKTcnYND8A25UPB6N29oz7FGOMHUG9qQZByXA1c5uwOBUd6PQLmUb72cDU2cwIIGBnH3c4VGpVsRX7y1BCJB8g6rr4DJ-JKBxqZHeWVH5NvfsnFEDVgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کد Rust سریع‌تر از کتابخونه‌های روز، فقط با «سریع‌ترش کن!»
نویسنده‌ی بلاگ minimaxir ماه‌هاست به ایجنت کدنویسیش یه دستور ساده می‌ده: «این کد رو سریع‌تر کن» و بعد بنچمارک می‌گیره. نتیجه‌اش کدهای Rustـی شده که ۲ تا ۲۰ برابر از کتابخونه‌های state-of-the-art سریع‌ترن. حرف جالبش اینه که بهینه‌سازی سرعت توی RLHF این مدل‌ها جای اصلی نداشته و با guardrail و حلقه‌ی تکرار باید تکونشون بدی؛ پرامپت‌ها و خروجی بنچمارک‌ها رو هم کامل منتشر کرده تا کسی ادعاش رو بی‌اساس نبینه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5310" target="_blank">📅 11:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فراموش کردم بگم که هزینه‌اش نسبت به Opus 5 کمتر شده.
هزینه Opus 5،
5$/25$ بود
هزینه Opus 5.5،
4$/20$ هستش</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5309" target="_blank">📅 00:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vNY3oEWUmUBHwlgV3iq0N0_QtQNqRrMUUYebarR0S8iPFkVfmd2HeClJcnBzNS_vcAIDkudTK8GLsJ0YB2wHlbDGBt9hXwevvMrpGVW6sqKo2fMWlbT_WrgPj_7eCVW6GOu8Sp2_bZMCVtI8E4Cm7OI8ZZKlq8sbQrsuWnhIxRUK41Bhy49HM93qwazAN0Z7cJKTxhbo_d5S_Ac2QP8P_osOMO0Q9JBEt9c1nG6qyiO-6sA7zI0tWRu_Z50ho-lwDsjb3laR3SPjN53PWp7bR2_hMcLHkX7mw6Poj_-tDeYR2YH-0OnNhXi1rfjsoj7GmjF7uj3pD5g_E85_UM2KSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5308" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AgaM5sDGuvIEOvKAKSG4CxtiM0fss1n56cIV3h2Ozod68U_J7fjZUFMonznDrV0QPDMGlCKayMoTywGqgzhCNzmhflM1KxN2zyiq_R4WwPVQtN1uuhAlbJMBf7E_w6M4B2Ag34KmXeD7ZoBIXyq6M4kDKQF-WB-3buVhvS_ghXo3Qc4pFl9TnWcpkeO0EXh5Opb0CRqUWZly7GLtzjtjwcieqAAQ54wod4RasBZGMaHMFR5DJLMrR8p35aBEg9nxChmgdai3izZTfiOGWcbt-d2g7BSKbsT0_5mlDJo8T-wr1mGZ8tuhyfxLBLWU0rX0DBvdt1HgQ6HO_IgZQSirJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XUGnr2Y05w5fY_YIq25tdsHqBi7O6Y8D49jeu-vWTpLF0l1Mi0rV2A0crU2v18klIm0RkdTc-jo41QXJKc2VZ1xNuCyWXOse5n39nvoc_vvovUkuG8V-7A8N2aX35vVYn5HZfs3byR4KGa1VEH-Bzba_h5kgY25sfhV_OcEhQ_0gGUkQShE13Joboh9Leznzzhy2DmyekcirY0AbvtDaKgXWHaWoNfyFulLo7RRNrgkj13KSu9GqtZVotlSdRvkLmu--Qs1fi_8Q0tbtXVdW4LRNkqaOfUwciJaRUjIqiZ9D88XEASyyiKoQWiKtXLcQjRLFahTBWWth29Y4ijIXVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مدل Opus 5.5 ریلیز شد
وقت اون میم مدلهای چینیه</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5306" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mWaiZDfwvQIWV9CIOz8JgfCRxvZCOIZDUj6pEbqIYS_7_rSs43QSfKHOEUze9L025R6t0HuZ197RwOpuJipqRxdtCM_K7OFDO9npeDrODK_YiPgFMN69syw0j-UNWsCSuAyJd3zlSJTNNB63M5IoK0Adi_MhzPDhkZtflNO8TY-dJFpM0IuokXfYPVkqbYUS4SOAogaxwdGMyr_s_WAkhSG86zU1QfgWWzb1TQzF42CIGQazBm06XGfQJSVEeiXLppE_eassTJ7ZOtOdkReBULca0EbU0K2QsFubLsjChsNpmhIhdR-4_GGP-F0SL9l1hBGZNuuKV2OeMnxPr7PgCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر روی 9Router ارور
HTTP 403: [403]: {"type":"error","error":{"type":"FreeTierError","message":"Error from provider (Console): OpenCode's free tier can only be used from within OpenCode"}}
می‌گیرید از اوپن کد، علتش آپدیت نبودن 9Routerتون هست.
برای آپدیت کسایی که با npm نصب کردن، از دستور
npm i -g 9router@latest --prefer-online
استفاده کنن، و کسایی هم که با داکر نصب کردن از
docker pull decolua/9router:latest
docker rm -f 9router
docker run -d \\
--name 9router \\
-p 20128:20128 \\
-v "$HOME/.9router:/app/data" \\
-e DATA_DIR=/app/data \\
-e JWT_SECRET="change-this-to-a-long-random-secret" \\
-e INITIAL_PASSWORD="your-strong-dashboard-password" \\
decolua/9router:latest
استفاده کنن(با پسوورد و JWT دلخواه برای JWT_SECRET و INITIAL_PASSWORD)</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5305" target="_blank">📅 14:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">این وسط Mimo 2.6 Pro هم اومد و grok 4.7 رو بولی کرد:))</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5304" target="_blank">📅 12:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZTQMzQwzX-zHhd72pE7IiDp-KkL85y5hJ347ogAa54eOJNehxbOMo-zz0VWXCJZf1Rkw2wDEmfahvD9CZdxwhwSpFTqfxqDtrMXtRoNskXGnmY9HEQtGnWEY-jrlreBG0UYkXtkgQCWM8V9n7b8i_SxdVIDeDnQq9X65M3xn8uFWhGDjebg-Z1gPk4kL9sHxjcYnxqXvgFiphz8sduRaV8B8ydMfWfrHL5L9ECOb-CE7HZnbD9trY5QeYJOcKNsggxULMsi7GvFq93moQlcMb82lCgasLeIYPsApBc9wEz2cyFfuxTCuQJH88MiRwQszh9z0xJnO14yOeTO9fRPPTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا منو پولدار کن یا متین ویدئوی ماینکرفتی بسازه:</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5303" target="_blank">📅 11:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bi6ZAwu4Jffk-kYHocnO4r8S8Vf29_V-vXSObkMhgxF6otCvE4tGFA8cDd9l2essRdhpPL2Qs7w0OBSF6YjekLdvNaeajGayPXqhEJSJE-ixHuvPNH9k--mR5NBObkPi5Fhd1HwP08CiLkkSf1wB_ALN2Dfq7IcCRc6mcYx-AOAHkpoTpv4s9r8ptZkbxN4ry9dJPK3btY6cCWrEb4FoW4JJIL1Z8Qhivpmhfoxr_lqBKTemEQpExPEivIVGOUqgbsz3RuWhy_rFecSE5Qqv2o8vsUIF1NMaGeGOyYTJrvGDAbw5VF8t4prXAUH1akN7Jb50KsmppSVti8LMgodGpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گذاشتم قویترین AI دنیا ماینکرفت بازی کنه! GPT 6 Astra + Jev
توی این ویدئو، با همدیگه پروژه‌ای که ادعا می‌کرد تونسته ماینکرفت رو توی 8 دقیقه اسپیدران کنه بررسی می‌کنیم و خودمون بازسازیش می‌کنیم با استفاده از Astra و Jev
از برادر کوچیکم دعوت کردم بیاد کمی راجب خود ماینکرفت توضیح بده و کاری که ادعا شده ai تونسته انجام بده.
همینطور در مورد Jev صحبت می‌کنیم و اینکه اصلا چه نیازی به این معماری حس میشه در کنار LLM ها؟
و می‌ذاریم ai ای که کدشو نوشتیم، ماینکرفت بازی کنه برای خودش ببینم چه اتفاقی میفته
😂
لینک سایت Typesafeai برای گرفتن 5 دلار اعتبار رایگان:
https://console.typesafe.ai
لینک سایت هوشیار24 برای تخفیف 90 درصدی API از GPT 6 Astra:
https://houshyar24.ir/?ref=B2N4W9SS
پروژه رو هم توی ویدئوهای بعدی که تکمیل‌تر کردیم می‌ذارم گیتهاب واستون
🥰
📹
تماشا در یوتوب:
https://youtu.be/l-o_fQM_9AI</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5302" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مدل
Grok 4.7؛ آپدیتی که بیشتر ناامیدکننده بود تا پیشرفت
ببینید Grok 4.5 نسبت به قیمتش واقعاً مدل فوق‌العاده‌ای بود؛ سریع بود، کارکردن باهاش حس خوبی داشت، قابل‌اعتماد بود و به‌عنوان مدل پیش‌فرض عملکرد خوبی ارائه می‌داد.
مدل Grok 4.6 از نظر من یه قدم اشتباه، البته قابل‌درک، برداشت. کندتر و گرون‌تر شد و برای انجام هر تسک، توکن خیلی بیشتری مصرف می‌کرد؛ درحالی‌که فقط یه برتری جزئی از نظر هوش داشت.
البته دلیلش رو می‌شه فهمید؛ بالاخره تیم سازنده باید خودش رو توی بنچمارک‌ها بالا بکشه.
اما بخشیدن Grok 4.7 خیلی سخت‌تره.
1-
مصرف توکن برخلاف وعده‌ها بیشتر شده:
گفته بودن مدل جدید توکن‌بهینه‌تره، اما توی استفاده‌ی واقعی بین ۳۰ تا ۸۰ درصد بدتر عمل می‌کنه.
2-
بنچمارک‌های ضعیف‌تر:
توی چندین بنچمارک، امتیازش از Grok 4.6 پایین‌تره.
3-
سرعت و تجربه‌ی کاربری بدتر:
کندتر شده و کارکردن باهاش دیگه مثل نسخه‌های قبلی لذت‌بخش نیست.
4-
هزینه‌ی واقعی خیلی بیشتره:
هزینه‌ی استفاده‌ی واقعی از Grok 4.7 بیشتر از دو برابر Grok 4.6 درمیاد و حتی از هزینه‌ی Astra هم بالاتر می‌ره.
با توجه به این‌همه تبلیغاتی که برای این مدل شده بود، باید بگم واقعاً ناامیدکننده منتشر شد.
البته بنچمارک‌ها همه‌چیز رو نشون نمی‌دن و Grok 4.7 توی بعضی کارهای مهندسی واقعی همچنان تجربه‌ی خوبی ارائه می‌ده؛ ولی درمجموع حس می‌کنم هنوز خیلی به مدل‌های سال ۲۰۲۵ شبیهه.
مشکل اصلی، قابلیت‌های Frontendـه:
عملکردش توی کارهای Frontend به‌شکل غیرقابل‌قبولی بده. قابلیت‌های 3D تقریباً وجود ندارن و مدل دائماً توی حلقه‌های تصادفی شبیه Gemini گیر می‌کنه.
حرف آخر:
این انتشار واقعاً ناامیدکننده بود. امیدوارم تیم SpaceXAI این موضوع رو بپذیره و توی نسخه‌ی بعدی بتونه دوباره ما رو غافل‌گیر کنه.
✍️
theo</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5301" target="_blank">📅 10:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fZB5XA6LEm-3VLrIgNjadJy7lsgsVhD0pR5WAJG0M-ivynzS6pNIIQIprQBnRgLu-qde3SYQ7kuQmBsjjlfx5IXdt-p4ULb-I-UEv8tm8iWNHANzgG5SyBgSrt4dJ9l5HQA9gr8f_ZESxQf4hW4iDlJqzwaIfxtrL8gtAPnSUGVGi29_pOMscIrP7ibH_9mVTPTz-trsVrG_x4Be6ycb1ZZ1nGJ1Tcc9n4jkY2rYpfu428sNHI8bgbjJ9R5WQ2d-rOdnlkn0V0RdW1Dk1yKTeJ5dINRZ384jQTunq0nvoY4oR2bLDVFKu0XvJ_0KFDW0qEu6i9y_o-z2sQpYTlzZLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره. ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5300" target="_blank">📅 00:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hzD6Ky1Z6brDy22caZGF21tmA6m2zGnt1YsUTL9uoyaF8R4DFfWkxM5Um7NQhym6R3Qm6dEaWP96MgXxO1tGK38orwVHHKfI_P6Is_WkRwSzcO7KMRMd2qaZuhowkVRxUnokHDgd-scR95_KsnIwc0_wUTnJGAePuFryu7Kfu5aCxOGnzVgvAclshi98XvMsfAUPuQ2AlNhCF6II9wZHTFtk3HMYF3CG69J19LgT7jqEqUGhat--wdzUaQRNDSTiVcYa41RhSSlZY1a7qHEXUMD06xs8WTQ35879IekdkT1FTZTTJ0KGLHdWqRcNkHn2OyPS5VQz6VYcbYuo8jMVfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TavdIE7e3st11MmqnFsqo6LwE_oUIUHKCKlxQOmhyQqYoOF-xZo7KDWn3nNNzSkepj5C_NnAO9-yDYkM8jTyidZbnAOU9IGlNuCmV2d7WZFSHwZNR_B6O_bzx9DXUAn2wM1vd6Hmg403TIg_ojKeDy2PlUgb3qeLqbWtZSYzdKsznBNn8Xgn-pqe2gPSRA5oRxqrfg4cC14h1YDFxCVVKCItT_VGX3oBuapOYRUjX2hgJd5DTS9gxhD9u8WtNnZgoI4vMeAJwbVXr451CL1ZN84YFCvFhT6-6yFkLD_YKtcgQR9pjU1E0Yutgwd3N7HpvWFbX-X_5fz91J74CemAeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره.
ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5298" target="_blank">📅 23:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد: https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5297" target="_blank">📅 22:49 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mFbi3uBhQDCelQxd4acHSdrmeUwwnBeuHIu5OKp1vrTKoN0h6PDaqkaOcwlaUEBelayTYR16V3BnBaJzUBf0ziGbVO2oeQAjQvoNXTKgdxeveiewgHxC2EfBA2RTwsPK8DVu599nTmZlLF1nwVN93JEWyNlPaAziFZ60dMf9OAtyC70PQkMXTs7eu4hSxdEVJ4QILVQjw5V82D9J7wt7VxXiuvva7MCWa0lBFDxCMeAbNWr2Z6dhJD2cJDLGFz26aMj1Drnx_is9tP78kErNulaAo_-jYoXoTq9GK99A8w2upSywnNZuRuhIW0qj9uFr5HNAaQFZGANLS0NEv2dsow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد:
https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5296" target="_blank">📅 22:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hRjFV11nwVoFtxj1C9-jMGO6hog1ORPv30skp8xPcKNs5kiNy8svpjHdoyX_3m6GviAjCNZeX0fBuVCIOn1anwR5mGkQyCbTdhFvd1e3FXw6VPL9mGDJC5akDOF1zgMHVR5_xp_TzAOIsNWCGr6HRkz2jWTqcuGv_3vjtT1d1eE0TTCdx99d46Ccbdv2nOYpwCMQgzSYvuZBNAXz70grK6eS-etQpabm40bKOGgsqpr-OLK1TBv-g9zTRm-wNBb4oNAd_XOcmTu75ZyjqV4xSDJtnhCJ149KK236HhX74mfKLdkzp5Xlx7MR3GwTXcVWubXAF8Mj0DsznbLKiMUBBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی مسلمان
اصلا هیچی بهش نگفته بودما، خودش یهو اومد گفت بسم‌الله</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5295" target="_blank">📅 18:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5294">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یه نفر یه چیزی ساخته بود
من دارم یه کم خفن‌ترش می‌کنم که ازش ویدئو بگیرم
بعدشم اوپن سورس منتشرش می‌کنم
مربوط به بازیه
#️⃣
از اونجایی که 3 تا 5 هم برق میره، بعدش ضبط میکنم و احتمالا تا شب آماده بشه</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5294" target="_blank">📅 14:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5293">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5293" target="_blank">📅 13:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اگه اولش ازتون پرسید Can you chat with Jev
باید بزنید No
چون طبیعتا LLM نیست و نمی‌تونید باهاش حرف بزنید
یک مقدار شاید پیچیده به نظرتون برسه اما به زودی راجب کاربردهاش صحبت می‌کنیم و ویدئو هم داریم</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5292" target="_blank">📅 13:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k8plvOUBLeC2ZY-iODWXazBTaRYt68R6D2qizmiIWue3fpoQQY48yRY67riLKhvnhQokQP9Mclq7GUpQ4o-ulMNqahcIEHVLbY6llu0amDGGG-H8ea0rrGu5ms0W6bfR6ugnQ4D_cgz5x5THzI4zBqe4ILGvuX6WI19qJVvZnyhjMQV-zJLczdT9Fgg7UXjsoiCVdMeXvGeGzLlnIc-pNHDeQHIdXRSwIFBf4BvgCG3A1vnFdxNI5aR3wE6Rk1lcTZ6q9_cay0BJHEan9IYWdBNQkAXXGh7IjTs5ZcMSuQBheJrxu50nhBb6vu-aoG6YmGWmV8cyAyMmCEC8UQlQBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی بامزست:)</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5291" target="_blank">📅 13:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5290" target="_blank">📅 13:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fv9f7bsGfSrHAUKrPxVqp5-Rl-Lc-3Cd2kbmXAlE-Y9ZiZiY44-DgyJUymAVfFMD-7p0394InwVqKr8w6OGl7x1xbYjQ4p6R83DpRf4Sd_NRh9B1gBqvkxU7DIMWjL_vnzqsiy5oXoUmRwgH_wjbO72-KhJiiGj4_us94KekZGH7-dPp4CE4YvbjQ6dZbIwckG4TsWdfmw8j-7Tvk85npXtjy6CdnCkVS088YLh82J4uUxeh66wwiT9a7HDR7M6c986-uWHH9pcZSlQBtDoXJbJClb5n6kQR3vBiyCh3spss15shEhndr1g6Q75Qhg_fCPXF4fCYBLKj0OXFl2owLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad) برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5289" target="_blank">📅 13:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromgooyban🦆</strong></div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5288" target="_blank">📅 11:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5287">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/koy-u9iaaf91wqKkRACGiEuifQ2EgD7F3vljZ4p_pZB8D-_PPKXI9S8ApQiIW4q2p5i2kn0JNPo4Ft6SA7S4zP8HpQrSCYrNgUT62a3WJCWny4Dp3HoTZ3eS_8GZri44wx2gOuUqeedsXMyMIaT1zRedQeCRxtKg1sYT_GMk7zJ7r7Mqbl52w5ccFOU1UtuB2n3q0S4z3QbBfLm5pZBk-KC7xbBUvKtq3Qs_drtOyiYvNsGj487sPInoMzqQaJAvCLP_BIoYHhgVbQDLZ8s8vOL_nsz8Y5Rd7iT8mDFW13VEd1hvw5-aMmhy-b6aBfSW5rVyQs2T4BdHQ45pM2IWgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad)
برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5287" target="_blank">📅 08:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BGfmDkvS2cI6SDHQfc74-jQcF0iORt_tpnFnrvTlWwDDmCkjV8tv54Pb80Ym2UxPdWlHpQenxJL7iNBy4aQtg4GQ6kNoSops3RJp_RzkMnXLqPDmiZ9Pct8ndbpSX5RC0xELsygCUn93c3Q8p4SYFycLP4MLiUc4lHsy7_9A6hzTRcC-68af7CWosv1iBXbAI0UoneptsYS3nxvHrD9UpBMzh0U111-mC1at0Xa720Zna8laOfBH3AHB-EH1UnHAebySTqkjIsSrYacMTkHVXl58EuS2eYctRiUyZLTvKKCnHD8_2Ggjf2NCAK3QVbj96rXbqFgIfgizZsVvMkXQ5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.  خلاصه‌ی توییت این دوستمون:  - یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه. - هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده. - اما Jev اصلاً متن…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5286" target="_blank">📅 23:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه  هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم، سعی کردیم با یزدان عزیز با استدلال و تجربه‌ی خودمون…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5285" target="_blank">📅 23:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sJjXu7mBogGqK3Im3sGxLlG05rxggyuZWdubvsFxM9D0PurPwropd3WbXAMXCBS40-CNeU1b8EbMGZOXlfEj4jejMO9_h1BlQ4xhhUQOyWfe0aG3SKW-ALE_dPHuIAQ1TAN29rlrmj9OfUwYB58MctzGKgqO4igUdh4GgwpxX9HE0iNtVwaEpO7F-vBOHPSR9SLnD_ho1suVAFt7VtKdl5GuazAaeV-t4MYB0yLdqtKXjwVMkIXPId4Oc04PsFKmG025lBT7bQo_EZXOX4qqSt34lnpCOgwxVrKUI3WI4DxxIjDujLh58FxXbd4MUs7qnW6QixAPK1lbECczh0T1kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه
هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن
به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم
، سعی کردیم با
یزدان عزیز
با استدلال و تجربه‌ی خودمون به این سؤال جواب بدیم. چیزهایی که بررسی می‌کنیم:
— چرا بیشتر بحث‌های این حوزه توی شبکه‌های اجتماعی «حکم» بدون دلیله
— فرق AI با یه ابزار ساده مثل ماشین‌حساب چیه
— تفاوت نوآوری (Novelty) و خلاقیت (Creativity) و اینکه AI کدومش رو داره
— جایگزینی شغلی و تحلیل آینده
— چیزهایی که هنوز دست آدمه و AI نمی‌تونه جاش رو بگیره
— بحث کاهش نیمه‌عمر مهارت‌های تخصصی
— ۵ تا کار عملی که باعث می‌شه بازار کار هنوز بهتون نیاز داشته باشه
📹
تماشا در یوتوب:
https://youtu.be/x8V0w3I9g10</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5284" target="_blank">📅 22:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eY90aCipuGOnFbj8p1IUGZiLlB8DEnRUvYKqt17WVn5xl67JDWvHQF48X4G9NYmJ8AmsvF0gBlr8RphroM_ffAld33pnT0tMRjx_O884eDPVxGGKnRSGz_ibGloIofVrXKT9fpFHZESCoRhYiM6fxHQMmKPsqz9kM_RxxeD-znjliUXA0HgEuINDAMVZ0ViruRu6_lqNWqeB2V_A7CWCnLDl5WOplzEFxZQSiyu2huGdNEcPCeYpWAIRNu07sKIGuxJqlPiHJP4PtbYozKmyTyy9G0mYUDUKUJfY9TJahAljFErmIm33WfJxq1QJGqLphmBapoc-7Ryd-ESvmJHPkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍓
بچه‌هااا یه آموزش جدید آپلود کردم
🥹
✨
اگه Gemini خطای 403 میده یا Google Flow براتون باز نمیشه، این ویدیو رو از دست ندین
👀
💗
توی ویدیو از صفر Blue Knight Panel رو می‌سازیم و آخرش با کانفیگ‌هاش Gemini و Google Flow رو تست می‌کنیم
😭
🔥
🎀
تماشای ویدیو:
https://youtu.be/GK2PGDzkbh4</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5283" target="_blank">📅 21:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5282" target="_blank">📅 18:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=SGdGi84q_B3etTtjOxP5-1aIIn_XSf2lft0F82Q8U8QreGBa0QPEDeBC_DrbrIKTf44tB2KRQ1joiiynN8h6OGzQT_xjiiqW-zjivcyag5cPfg02OkyD8Jvvu9jybxeR_cUiQAsNPT6fWmS03uH3qjqJZgSEfRBQqtrb8qNGI7rx0gJdw8Duhcq1flrhJqXmP7qGZjkS_BxLDE0u6D4KeTmp1xXH2JVuzsdTDHYm5oEeQ7E3ZDgHrEd_fY30jEEUhIMDbgzk9AZhZNTN1OiUv0aT_ISzp0MJdIR-xFzFs3YzTMcwhFUKJidRTtdnmxnPB0EyiJuELd0lejnDB-87mIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=SGdGi84q_B3etTtjOxP5-1aIIn_XSf2lft0F82Q8U8QreGBa0QPEDeBC_DrbrIKTf44tB2KRQ1joiiynN8h6OGzQT_xjiiqW-zjivcyag5cPfg02OkyD8Jvvu9jybxeR_cUiQAsNPT6fWmS03uH3qjqJZgSEfRBQqtrb8qNGI7rx0gJdw8Duhcq1flrhJqXmP7qGZjkS_BxLDE0u6D4KeTmp1xXH2JVuzsdTDHYm5oEeQ7E3ZDgHrEd_fY30jEEUhIMDbgzk9AZhZNTN1OiUv0aT_ISzp0MJdIR-xFzFs3YzTMcwhFUKJidRTtdnmxnPB0EyiJuELd0lejnDB-87mIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو که دیشب گفتم واستون می‌ذارمش، توضیح می‌ده که می‌شه حل‌کردن مکعب روبیک رو با
نظریه‌ی گراف
مدل‌سازی کرد.
- هر حالت ممکن مکعب روبیک رو به‌عنوان یه
نقطه یا رأس گراف
در نظر می‌گیریم.
- هر حرکت قانونی، مثل چرخوندن یه وجه، بین دو حالت یه "
یال
" ایجاد می‌کنه.
- مکعب به‌هم‌ریخته، نقطه‌ی شروعه.
- مکعب حل‌شده، نقطه‌ی هدفه.
- حل‌کردن مکعب یعنی پیدا کردن مسیر از حالت به‌هم‌ریخته تا حالت حل‌شده.
توی ویدئو، سمت چپ یه مکعب روبیکِ به‌هم‌ریخته دیده می‌شه و سمت راست، شبکه‌ای از نقاط رنگی و خطوط مختلف. این شبکه درواقع فضای تمام حالت‌هایی رو نمایش می‌ده که مکعب می‌تونه با حرکت‌های مختلف بهشون برسه.
نکته‌ی جالب اینه که مکعب روبیک فقط حدود ۲۰ ساله که اختراع شده، اما تعداد حالت‌های ممکنش فوق‌العاده زیاده:
۴۳٬۲۵۲٬۰۰۳٬۲۷۴٬۴۸۹٬۸۵۶٬۰۰۰ حالت
یعنی بیشتر از ۴۳ کوینتیلیون حالت مختلف.
با این اوصاف، شاید جالب باشه بهتون بگم که برای هر حالت مکعب(هررر حالت) راه‌حلی با حداکثر
۲۰ حرکت
وجود داره. به این عدد معروف،
God’s Number
یا «عدد خدا» می‌گن؛ چون از هر وضعیت ممکن، یه حل‌کننده‌ی کامل می‌تونه توی ۲۰ حرکت(حداکثر) یا کمتر به جواب برسه.
پس حرف اصلی ویدئو اینه:
حل‌کردن مکعب روبیک یعنی پیدا کردن کوتاه‌ترین مسیر بین دو نقطه توی یک گراف فوق‌العاده عظیم.
این نگاه ریاضی کمک می‌کنه بفهمیم الگوریتم‌های حل مکعب چطور کار می‌کنن و چرا پیدا کردن راه‌حل، بیشتر از اینکه فقط به حفظ‌کردن حرکات مربوط باشه، به
جست‌وجو توی فضای حالت‌ها
مربوطه.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5281" target="_blank">📅 16:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=nErSMcrc-LQPWlrm7XIt31rKGKPiis1blufHtC4Moqz6W1nHZxIqrTnOAX0weub1PWv5mZyi-D9Sl9NAHOu8YQorS2Uw6b5Fzs84Hpq1_ifGzNaHawVAz6wKr3e-JjKH5ZQKLPe4kETDNOLlF9EKkpBoomuIS1BaZwKd6y6aE_SRoowJGliwA46L9OdnkhQboG9aIsLdMkMhopzxvD1G7OLASDf4tJFYAVBeP17GEQlIeTvizMOkKwUOhZB_k3BXMq1UH2b0eW81RRh4EpvkW13AR_tQAmhKA1FLs6Jdv1N2C8-2qEDPTH6n9WYeG1qpSd3oKXlN3gB8PzEpn_7-lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=nErSMcrc-LQPWlrm7XIt31rKGKPiis1blufHtC4Moqz6W1nHZxIqrTnOAX0weub1PWv5mZyi-D9Sl9NAHOu8YQorS2Uw6b5Fzs84Hpq1_ifGzNaHawVAz6wKr3e-JjKH5ZQKLPe4kETDNOLlF9EKkpBoomuIS1BaZwKd6y6aE_SRoowJGliwA46L9OdnkhQboG9aIsLdMkMhopzxvD1G7OLASDf4tJFYAVBeP17GEQlIeTvizMOkKwUOhZB_k3BXMq1UH2b0eW81RRh4EpvkW13AR_tQAmhKA1FLs6Jdv1N2C8-2qEDPTH6n9WYeG1qpSd3oKXlN3gB8PzEpn_7-lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.
خلاصه‌ی توییت این دوستمون:
- یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه.
- هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده.
- اما Jev اصلاً متن تولید نمی‌کنه.
- Jev به‌جای تولید توکن، مستقیماً از ورودی به یه ساختار یا خروجی مشخص می‌رسه.
- به‌همین دلیل، سرعت Jev فقط به این دلیل نیست که «سریع‌تر متن تولید می‌کنه»؛ بلکه اساساً فرایند تولید ترتیبی متن رو حذف می‌کنه.
- نتیجه می‌تونه پاسخ‌دهی سریع‌تر و مناسب‌تر برای کارهایی مثل خروجی JSON، ابزارها، ایجنت‌ها و پردازش‌های ساختاریافته باشه.
به‌عبارت ساده:
LLM مثل نویسنده‌ایه که جواب رو حرف‌به‌حرف می‌نویسه؛ Jev بیشتر شبیه سیستمیه که مستقیماً ساختار نهایی جواب رو می‌سازه.
البته این به‌معنی بهتر بودن Jev برای همه‌چیز نیست. LLMهای معمولی برای مکالمه، توضیح‌دادن و تولید متن آزاد انعطاف‌پذیرترن؛ اما Jev برای خروجی‌های مشخص و قابل‌ساختار، می‌تونه سریع‌تر و کارآمدتر باشه.
✍️
ترجمه و خلاصه از
akshay_pachaar</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5280" target="_blank">📅 10:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m12C84eoVakkQg3u3hujTt9O2okjYA4EWiW7boIqqqfN_QUQY-l6VnIIMvsBm_drq34sVWy5qGo12wR2D5TlrAo3mnnCUABDOs_9iELPeFrqNlGaWB9B23hSIeJPkUA0x36HOxjXCQNxzf7Hlw4ULR5hyrI4jy0JplSsCdb7Kl6JYannDEE_xjJj9U8foxdCu_14OHybKys2Bax68BEn7o_-7Vobhf91JoTIOc-Q36wMRUzhwWuh1ZqZlQW3vEqmaZLutYaE7vbFhYBsEtmPliJ-MKvfiQJSl9vmINnzZloqVmv6xIZNQ1xsnrbonx70WE0LBrRAmdzi9DGpfv4sRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم توضیح تخصصی تر: https://www.youtube.com/watch?v=vj7hysh0mOI</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5279" target="_blank">📅 10:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BlgkEuI9M9d9sWLxg983HnmcGAy66MheISqII-On-zpz4VZgVzpGsGVH4AeQtJplmGusKCt7uTcB3ySNpGXftNyKI8-HOndPtSVOR_TOjfXCI04lgH28-TgcEwWjuer5imobEUZfTFcXDEU4rQNjgZYfKUmAgNQyLEiwSER_J-16NY5GmVDZ9No69u2McOT4YmESNd2KLYuXBVbRg57TzZM5Gi143EAsitN0YWO2vkalLUEvjbeT5uJMnH8blBgHSHR3pSkxYdq8eAYFitGVgfqCgRQuTPGN33YRhOFtlrYDETaSNM7obyZ5k2H-MoT_ppuaxxQ4oLQF76_VIgSQ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیلی که توییتر رو دوست دارم:
(اون روبیک Graph خیلی خفنه فردا می‌ذارم فیلمشو)</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5278" target="_blank">📅 23:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">به زودی برای پروژه‌های اوپن سورسم هم آپدیت میدم بچه‌ها
هم Aether gui هم اسکنر</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5277" target="_blank">📅 21:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کسایی که ری‌اکشن
😁
می‌زنن آخر این ویدئو مسج رو دیدن
😂</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5276" target="_blank">📅 20:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=kgwKW4-FQxnIfhKK8f9LOqRR1XQRqiZIfpxratO_wN_-KAUrrfUvuzDdTppIawQzWRTE8UqEfNM5IRuMh6AZbdI8AqtSCo9LBiLvZQjFXoTJc8_uvlO-0Mo_n1y2SpyKvTOCvH6d1-Kae_MmErVh0AydUTEKVlozlQD3Ia-7XT57TpZGkNnkh1dtLm4wqt4fUXZWvzk6baCBjAApHJMbexOs1mqApoe8Aj6D7k7xEA2WbvmBofIbXXOFDqEsl90SbARimX_5q_7rx5-IDNLvXbT6ywe9_Wn0twMjPQSo5qPQbcXReipU2scCl0tE8QC_-J6dU7m49OviuDnZopstyw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=kgwKW4-FQxnIfhKK8f9LOqRR1XQRqiZIfpxratO_wN_-KAUrrfUvuzDdTppIawQzWRTE8UqEfNM5IRuMh6AZbdI8AqtSCo9LBiLvZQjFXoTJc8_uvlO-0Mo_n1y2SpyKvTOCvH6d1-Kae_MmErVh0AydUTEKVlozlQD3Ia-7XT57TpZGkNnkh1dtLm4wqt4fUXZWvzk6baCBjAApHJMbexOs1mqApoe8Aj6D7k7xEA2WbvmBofIbXXOFDqEsl90SbARimX_5q_7rx5-IDNLvXbT6ywe9_Wn0twMjPQSo5qPQbcXReipU2scCl0tE8QC_-J6dU7m49OviuDnZopstyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5275" target="_blank">📅 20:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">از اینجا می‌تونید به عنوان میهمان وارد شید: https://live3.eseminar.tv/ch/wb182512</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5274" target="_blank">📅 19:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5273" target="_blank">📅 19:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=VL0LySA1lag5JIeg0MvNYaBMJTLhJfbrf1hluwzn15x8YOuE2-x_xIgUqX8VGMBYT02dysIeIfRzUNaDVqUJw7e-SrRQdRRmgUF6KiZ405s4Q-Z6Lb8PO8DLKHmzcYnxlouy9bbsevEZH1c1oIuo_6aDOtBl12b_oUXX_1cmYzBgqd5dj-EvqVvLjfdD93eqpzIuKmrzECSTeAacJKEMvCX5-t1AD4_0XMKktgf6TKAbVTadHwexMzf8ffDalanHXUz3iKblcQhIJmtb7Vi_52Iz3CZr1YKLNp8L-OOEU0UXkmtRx2JS-bbiAVMdkzgkvBoUsAuz5rRozIDjSJektJXq67UhcrP_M8dGt5NSiLINY2N6y3A9mfeDd0J_H5c09PzaX9DfkVNwhppS_dlVLLz5lEXnAMzApJ8YcFY29x5F1eMuijdwyAmqi7KtJ1zbh_XGOUpeJ-UyPN2A-tuuDA7MEEB476lJ-8jxXplCXUm5OmN80hy0tTACyG3GFcH51vNm3wcQJbKSj9hhrkn9aSELIokA2FijOPnsV6kUqKtEkCDpIrnFPoiPezfj09f0xB56BK3UgYujWm3qyyTsaG0MjJyBGK6foOj2MRPn4n22-9AA1qlUCckr-SGCcaR3mXY5Jv2YDnIWdUVHx0S3B5L2SK5xrCnCwco47t4a6rM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=VL0LySA1lag5JIeg0MvNYaBMJTLhJfbrf1hluwzn15x8YOuE2-x_xIgUqX8VGMBYT02dysIeIfRzUNaDVqUJw7e-SrRQdRRmgUF6KiZ405s4Q-Z6Lb8PO8DLKHmzcYnxlouy9bbsevEZH1c1oIuo_6aDOtBl12b_oUXX_1cmYzBgqd5dj-EvqVvLjfdD93eqpzIuKmrzECSTeAacJKEMvCX5-t1AD4_0XMKktgf6TKAbVTadHwexMzf8ffDalanHXUz3iKblcQhIJmtb7Vi_52Iz3CZr1YKLNp8L-OOEU0UXkmtRx2JS-bbiAVMdkzgkvBoUsAuz5rRozIDjSJektJXq67UhcrP_M8dGt5NSiLINY2N6y3A9mfeDd0J_H5c09PzaX9DfkVNwhppS_dlVLLz5lEXnAMzApJ8YcFY29x5F1eMuijdwyAmqi7KtJ1zbh_XGOUpeJ-UyPN2A-tuuDA7MEEB476lJ-8jxXplCXUm5OmN80hy0tTACyG3GFcH51vNm3wcQJbKSj9hhrkn9aSELIokA2FijOPnsV6kUqKtEkCDpIrnFPoiPezfj09f0xB56BK3UgYujWm3qyyTsaG0MjJyBGK6foOj2MRPn4n22-9AA1qlUCckr-SGCcaR3mXY5Jv2YDnIWdUVHx0S3B5L2SK5xrCnCwco47t4a6rM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه! به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید: https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5272" target="_blank">📅 17:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه!
به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید:
https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5271" target="_blank">📅 17:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OyOy4G9F77-LE1L2NAN6ku4fDyijrBm_guTxaK76C-P0duazCQZ-ZPbr8GubJeCrVtZTNhyAFF1HH9HSB8ZvT_--_Z6ZDNNTcVziBNsK1AYySZq61LZD2p1tw5fT0krOIit4WX2GVFZ8BUG32EKiaKMJFLQU2POHMiWQs9GKJxhhE6bJcEdQQJ2vWXd3cYlOVBCJZBt8J8qTb_sBpPDB6PFedDqzBab-TneFe-3QM03QAyATRksns09XHgpe6ufsTqoAILAm6EEMZ-V48UX_zl_Fe2njlpV0ys7kWhtLxLgFCpCKGUCulWBAt9ukCwaXCw6pIEvuMl2AFv2_JW7_5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PPQ51D946DSt6VLPIv3WUGwvQFGFy_YoBFFTK2iBg6zTEZ5_j6kCqQAYiNPqGd0cG0z2PkvTd6NjKCck9sZojubiFSNs79QUcxhyAdILO6bdGgfPmMqfGD68cQ6sYLbnKT-a4TMRZtOkuVo75YMxsIHvxaMxcIIVDC8pOyGufKSMJoJoEqMsrJBfusYS2CukMoa10hkLwoHaQXlOxR7ad6dEuhG1IDxG1f_hG5eBHlfxO73wbFOLriG_lt23zhZ6cNr3JB8x1zht0kubfxdnCGOou05CJBmfYVKt12JdxMeTo8erWJ_c-HZmxND21fE7bXDuJbjl2Sw7km4h6lL-5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا درآمدزایی طی می‌شه</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5269" target="_blank">📅 16:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/brlEGTkevAnLMiIcttdC_K9AfOlXyBv-xITQ8R-MsiexIx3nLomP3nq4Jkn_wOATK5rbgsbMe01FAjJ0VNF_KpV9_FYZ5welc2XghMufx51RaQIa70H2uUsXjUlOtTg_zMCwQ930gCOIY23lZ_VAuWxkk0L_Na0v3lnHFKBlH1fL6R2gD7FD5OOCel6W2p65Sc4XOSYzGZXC4it3zAMxic_JTp6tUGGMshVrlDRPPD2bWN0CIezaG3V0Hv6ieN_DCbHFLKHBma9p2k31LQNAc90YeG2XDE2NS-dZOwpMYXyJOTC2Q3bYVyS3Le_VktDHe8NUE9_-C9eUGMHzUPodpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت
Z.ai
مدل GLM-5.3 FlashX رو عرضه کرد؛ نسخه فوق‌سریع 5.3 Flash با سرعت 200tok/s!
​• کانتکست: 1M
• مالتی‌مدال نیتیو
• اجرا روی بیش از ۱۰۰ هزار تراشه چینی ​انتخابی ایده‌آل برای ایجنت‌های کدنویسی و تسک‌های بلادرنگ.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5268" target="_blank">📅 21:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oXQvT0Sch2GZJ2RR5vpZ36NpU-tDral4hNhAc9lUD_f9rItr7u_ZiAPXFjalEFHRQWpUdEKNda-J11Gih1K84h3Kit44vVcH92GvPLQ0_KLhS2JopED-__qaVQPxBMUKh3LEqtwxqSy1hS2-_fFhO6zjt-GnBASI8FM4TD2uYa75lwYs2teva62DRx_vdZRVCSGX231nhnqRf2lFfN0A5Ew2yjgFniaSiaVknB4Hpe54w0e44K4gUXCRCfNg-iMrL2SUPhRyMIa-cEexL1pUqy2aJMS9C7ajXkd2wFBNAJF_rg7rLzo4H4l_tmxj7QGRHEUndy3nKm7IJb4hqelXIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همینه که میگم API نمی‌صرفه
توی 40 دقیقه، از پلن 20 دلاری کلاد که با این روش:
https://t.me/MatinSenPaii/5201
گرفته بودمش، نزدیک به 15 دلار معادل Raw API مصرف شده. اما کلا 7 درصد از محدودیت هفتگی من رفته. 4 هفته هم داریم، 15*100 و تقسیم بر 7 و ضرب در 4(هفته) تقریبا میشه 850 دلار استفاده. با یه پلن 20 دلاری. هرچند محاسبه‌اش به این سادگی نیست اما یه دید کلی میده
(با پلن 250 دلاریش تقریبا نزدیک به چند ده هزار دلار سوزونده بودم قبلا)</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5267" target="_blank">📅 21:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IdxJsbvBKUsRPq0dmn9emd7_CiX0CWZ3RHKUg5MSjtj7z7UpGZ-ZPlDEBtrX2DH_5U1PL0Rj9OELbM5D1t5UuDOjVwmRxRsPjQrpGbPF5hjsPVOGKwE5bXMCW80pNUP4_Uc7T0d9koFVxyVbltIsiQeK4Xlr6f8SCGwVoB1Z6hUW5b11ZCyy3fDlQ9BdBUa47uHYVgsb8ni22Elyvoo87Qaqg6idKeLp_EH_D2XtCAkeukILpH-0BL5S3aEdxgZqh2pztJju4PPg5UWX52YEGtt6edKWcOrjQO2DRLxdH-5mhuVCOFioixeG7_ds21qpDfGelyjCBUxj7C91cE59rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Rn1NEA3a5UP7suBPavIO5OHOtxRz_vx_9wa9pgHsi2628ofsSmBups_2emydEM-xS7sHHoiVl-xeJLBP-07JY0yqNGAhtZgVh1ROKPlx3CEQVC6bexZNZqubisykDrBUU_H5WGpadrTpHOaCEETEx9zDA2fc3eYuViVLOzRWnIDHoATb1SgUJ7NRjMu2pji4Kk33nKkPrexs3Shh2ff7w82BiiUheGjR5_POY3zbIAPHngUP_6Q8QknXG8CSJCdKV6ghs6AOVb9l-jYhr91KyHUkJHeP-t-p3VlUfGOZKjXvMQtPLAdVjM4X9x8TaHX4nfPYHG8RJVJOHyS93yYu5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5265" target="_blank">📅 21:24 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
